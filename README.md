# MAIP: antimalarial activity prediction

Prediction of the antimalarial potential of small molecules. This model is an ensemble of smaller QSAR models trained on proprietary data from various sources, up to a total of >7M compounds. The training sets belong to Evotec, Johns Hopkins, MRCT, MMV - St. Jude, AZ, GSK, and St. Jude Vendor Library. The code and training data are not released, using this model posts predictions to the MAIP online server. The Ersilia Model Hub also offers MAIP-surrogate as a downloadable package for IP-sensitive queries.

## Identifiers

* EOS model ID: `eos4zfy`
* Slug: `maip-malaria`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher score indicates higher antimalarial potential

## References

* [Publication](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00487-2)
* [Source Code](https://www.ebi.ac.uk/chembl/maip/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos4zfy)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4zfy.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos4zfy) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-021-00487-2) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!