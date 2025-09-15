# MAIP: antimalarial activity prediction

Prediction of the antimalarial potential of small molecules. This model is an ensemble of smaller QSAR models trained on proprietary data from various sources, up to a total of >7M compounds. The training sets belong to Evotec, Johns Hopkins, MRCT, MMV - St. Jude, AZ, GSK, and St. Jude Vendor Library. The code and training data are not released, using this model posts predictions to the MAIP online server. The Ersilia Model Hub also offers MAIP-surrogate as a downloadable package for IP-sensitive queries.

This model was incorporated on 2022-08-23.


## Information
### Identifiers
- **Ersilia Identifier:** `eos4zfy`
- **Slug:** `maip-malaria`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `P.falciparum`, `Malaria`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher antimalarial potential

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| maip_score | float | high | Score of the antimalaria potential of small molecules |


### Source and Deployment
- **Source:** `Online`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4zfy](https://hub.docker.com/r/ersiliaos/eos4zfy)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4zfy.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4zfy.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `384`
- **Image Size (Mb):** `321.29`

**Computational Performance (seconds):**
- 10 inputs: `50.87`
- 100 inputs: `37.52`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://www.ebi.ac.uk/chembl/maip/](https://www.ebi.ac.uk/chembl/maip/)
- **Publication**: [https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00487-2](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00487-2)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4zfy
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4zfy
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
