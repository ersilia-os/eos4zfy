# MAIP: antimalarial activity prediction

Scores compounds for blood-stage antimalarial activity against Plasmodium falciparum. MAIP was built by Bosc and colleagues at the European Bioinformatics Institute from an unusual foundation: several pharmaceutical companies contributed proprietary screening results, which were combined with public data into a consensus model without any single dataset being disclosed. That breadth is its main strength, since antimalarial screening data are otherwise fragmented across organisations that rarely pool them.

This model was incorporated on 2022-08-23.Last packaged on 2026-08-12.

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
- **Interpretation:** Score for blood-stage Plasmodium falciparum activity, where higher values indicate greater predicted potency.

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
- **Image Size (Mb):** `655.77`

**Computational Performance (seconds):**
- 10 inputs: `31.48`
- 100 inputs: `20.71`
- 10000 inputs: `40.17`

### References
- **Source Code**: [https://www.ebi.ac.uk/chembl/maip/](https://www.ebi.ac.uk/chembl/maip/)
- **Publication**: [https://doi.org/10.1186/s13321-021-00487-2](https://doi.org/10.1186/s13321-021-00487-2)
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
