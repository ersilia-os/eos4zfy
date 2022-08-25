from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sys
import os

smiles = pd.read_csv(sys.argv[1], sep=',', header=0, skiprows=1, names=['smiles'])
id_col = np.arange(0, len(smiles) ,1)
id_col = [str(x) for x in id_col ]
smiles.insert(0, column = 'id', value = id_col)

smiles.to_csv('maip.csv', index=False)

url = 'https://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/submit/mmv_job'
file = {'input1': open('maip.csv', 'rb')}
payload = { 'standardise': 'true','dl__ignore_cache': 'false'}

r = requests.post(url, files=file, data = payload)

soup = BeautifulSoup(r.text, features = 'html.parser')
job_id = str(soup.text)
job_id = job_id.split(':')[1].strip().translate({ ord(c): None for c in "\"}" })

download_url = 'http://www.ebi.ac.uk/chembl/interface_api/delayed_jobs/outputs/' + job_id + '/predictions.csv'
download_response = requests.get(download_url,allow_redirects=True)

open( sys.argv[2] , "wb").write(download_response.content)

pred = pd.read_csv(sys.argv[2])
pred2 = pred[['smiles','model_score']]
pred2.rename(columns = {'smiles':'SMILES'}, inplace = True)

pred2.to_csv(sys.argv[2], index = False)


