# Fit folder

This model has source type **External** and is trained on **proprietary data**, so no
training data or training code is reproduced here.

MAIP is a consensus naive-Bayes model derived from 6.5 million malaria bioactivity values
across 11 proprietary compound collections, combined without ever sharing the underlying
compound structures. The pre-trained weights are released by ChEMBL under the MIT license
(https://github.com/chembl/maip_public) and are shipped in `model/checkpoints/` (as the
extracted numpy arrays `feature_ids.npy` and `feature_log_prob_pos.npy`).

Reported model performance (external validation, from the source publications):
- ROC AUC 0.82 on the St. Jude Screening Set (MetaModel consensus; Bosc et al. 2021,
  J. Cheminform., https://doi.org/10.1186/s13321-021-00487-2).
- 7-fold / 12-fold hit-rate enrichment in prospective experimental screening
  (Bosc et al. 2023, ACS Med. Chem. Lett., https://doi.org/10.1021/acsmedchemlett.3c00369).

This folder is retained (rather than removed) only to satisfy the eosvc artifact layout,
which expects both `model/checkpoints/` and `model/framework/fit/` to be present.
