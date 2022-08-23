from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import numpy as np
import sys
import os

smiles = pd.read_csv(sys.argv[1], sep=',', header=None, names=['smiles'])
id_col = np.arange(0, len(smiles) ,1)
id_col = [str(x) for x in id_col ]
smiles.insert(0, column = 'id', value = id_col)

smiles.to_csv('maip.csv', index=False)

url = 'https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/submit/mmv_job'
file = {'input1': open('maip.csv', 'rb')}
payload = { 'standardise': 'true','dl__ignore_cache': 'false'}

r = requests.post(url, files=file, data = payload)
print(r.status_code)

soup = BeautifulSoup(r.text, features = 'html.parser')
job_id = str(soup.text)
job_id = job_id.split(':')[1].strip().translate({ ord(c): None for c in "\"}" })

download_url = 'http://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/outputs/' + job_id + '/predictions.csv'
download_response = requests.get(download_url,allow_redirects=True)
print(download_response.status_code)
#print("Job ID : ", job_id)

now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print("Current Time =", current_time)

open( sys.argv[2] , "wb").write(download_response.content)
print("Results saved in maip_predictions.csv")

os.remove('maip.csv')


