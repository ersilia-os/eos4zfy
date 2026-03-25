from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
import csv
import os
import io
import tempfile
from time import sleep

sys.stdout.reconfigure(line_buffering=True)

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

SUBMIT_URL = 'https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/submit/mmv_job'
POLL_INTERVAL = 20  # seconds between status checks
MAX_WAIT = 3600      # 60 minutes

session = requests.Session()


def run_maip(smiles_chunk):
    """Submit a SMILES list to MAIP and return [model_score, ...]. Raises on failure."""
    df = pd.DataFrame({'id': range(len(smiles_chunk)), 'smiles': smiles_chunk})
    tmp_fd, tmp_csv = tempfile.mkstemp(suffix=".csv")
    os.close(tmp_fd)
    df.to_csv(tmp_csv, index=False)
    try:
        # Submit with retry on transient connection/SSL errors
        print(f"Submitting {len(smiles_chunk)} compounds to MAIP...")
        for attempt in range(10):
            try:
                with open(tmp_csv, 'rb') as fh:
                    r = session.post(SUBMIT_URL, files={'input1': fh},
                                     data={'standardise': True, 'dl__ignore_cache': False})
                if r.status_code == 200:
                    break
                print(f"  Submission attempt {attempt + 1} returned status {r.status_code}, retrying...")
            except requests.exceptions.RequestException as e:
                print(f"  Submission attempt {attempt + 1} failed ({e}), retrying...")
            sleep(POLL_INTERVAL)
        else:
            raise RuntimeError("Submission failed after retries")

        job_id = str(BeautifulSoup(r.text, 'html.parser').text)
        job_id = job_id.split(':')[1].strip().translate({ord(c): None for c in '\"}'})
        print(f"  Job submitted: {job_id}")
        download_url = f'https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/outputs/{job_id}/predictions.csv'

        # Poll download URL until ready or timeout
        dl = None
        for elapsed in range(0, MAX_WAIT, POLL_INTERVAL):
            try:
                r = session.get(download_url, allow_redirects=True)
                if r.status_code == 200:
                    dl = r
                    break
                print(f"  Waiting for results... ({elapsed + POLL_INTERVAL}s elapsed)")
            except requests.exceptions.RequestException as e:
                print(f"  Network error while polling ({e}), retrying...")
            sleep(POLL_INTERVAL)
        else:
            raise TimeoutError(f"Job {job_id} timed out after {MAX_WAIT}s")

        print(f"  Results ready for {len(smiles_chunk)} compounds.")
        return pd.read_csv(io.StringIO(dl.content.decode('utf-8')))['model_score'].tolist()
    finally:
        os.remove(tmp_csv)


def get_chunk_size(n):
    """Return next smaller chunk size in the fallback hierarchy: 1000 → 100 → 10 → 1."""
    for size in [1000, 100, 10]:
        if n > size:
            return size
    return 1 if n > 1 else None


def process(smiles_chunk):
    """Run MAIP, recursively splitting into smaller chunks on any failure."""
    try:
        return run_maip(smiles_chunk)
    except Exception as e:
        size = get_chunk_size(len(smiles_chunk))
        if size is None:  # single molecule failed
            print(f"  Molecule failed, filling with NaN.")
            return [float('nan')]
        print(f"  Batch of {len(smiles_chunk)} failed ({e}), splitting into chunks of {size}...")
        results = []
        for i in range(0, len(smiles_chunk), size):
            results.extend(process(smiles_chunk[i:i + size]))
        return results


print(f"Processing {len(smiles_list)} compounds.")
outputs = process(smiles_list)
print(f"Done. {sum(1 for o in outputs if o != o)} NaN(s) out of {len(outputs)} compounds.")

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["maip_score"])  # header
    for o in outputs:
        writer.writerow([o])
