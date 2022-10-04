# Antimalarial activity prediction
## Model identifiers 
- Slug: maip-malaria
- Ersilia ID: eos4zfy
- Tags: Plasmodium falciparum, Antibiotic, Malaria, Bioactivity

# Model description
Antimalarial Activity prediction from ChEMBL
- Input: SMILES
- Output: Score (Higher score indicates Higher antimalarial potential) 
- Model type: Regression
- Training set: (number of compounds and link to the training data)
- Mode of training: Online

# Source code
- Code: Code: The model uses the web application available at https://www.ebi.ac.uk/chembl/maip/
- Checkpoints: N/A

# License
The GPL-v3 license applies to all parts of the repository.

# History 
- We have developed a python script that accesses the web server available at https://www.ebi.ac.uk/chembl/maip/ to run the predictions.
- `requests` and `BeautifulSoup` libraries are used to post the input to the server and fetch the results.
- Model was incorporated to Ersilia on 10/04/2022

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
