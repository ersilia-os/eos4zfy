# MAIP: antimalarial activity prediction

Prediction of the antimalarial potential of small molecules against the blood stage of Plasmodium falciparum. MAIP is a consensus naive-Bayes model derived from 6.5 million malaria bioactivity values across 11 proprietary compound collections, combined without ever sharing the underlying compound structures. This version runs the model fully locally using the open-source weights released by ChEMBL under the MIT license, reproducing the scores of the previous online-server implementation.

This model was incorporated on 2022-08-23.Last packaged on 2026-04-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4zfy`
- **Slug:** `maip-malaria`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Antiparasitic activity`, `Antimicrobial activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates greater predicted likelihood of blood-stage antimalarial activity

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| maip_score | float | high | Score of the antimalarial potential of small molecules against the blood stage of Plasmodium falciparum |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4zfy](https://hub.docker.com/r/ersiliaos/eos4zfy)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4zfy.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4zfy.zip)

### Resource Consumption
- **Model Size (Mb):** `15`
- **Environment Size (Mb):** `563`
- **Image Size (Mb):** `405.42`

**Computational Performance (seconds):**
- 10 inputs: `59.82`
- 100 inputs: `51.68`
- 10000 inputs: `1304.87`

### References
- **Source Code**: [https://github.com/chembl/maip_public](https://github.com/chembl/maip_public)
- **Publication**: [https://doi.org/10.1021/acsmedchemlett.3c00369](https://doi.org/10.1021/acsmedchemlett.3c00369)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

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
