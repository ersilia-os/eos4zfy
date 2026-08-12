"""Local MAIP scorer — reproduces the released chembl/maip_public model.

Scoring is the released model's naive-Bayes joint log-likelihood of the positive
(active) class: score = X . feature_log_prob_[1] + class_log_prior_[1], where X is the
feature-based Morgan fingerprint (radius 3, binary) of the standardised molecule mapped
through the model's DictVectorizer vocabulary. The vocabulary and the positive-class
log-probabilities are extracted from the original joblib artifacts into the numpy arrays
in model/checkpoints/ (gitignored, persisted via eosvc); class_log_prior_[1] == 0.0 for
this model.
"""
import os

import numpy as np
from rdkit import Chem
from rdkit import RDLogger
from rdkit.Chem import rdMolDescriptors
from standardiser import standardise

# silence RDKit and standardiser chatter (matches the upstream CLI)
RDLogger.logger().setLevel(RDLogger.CRITICAL)
for _logger in (
    standardise.break_bonds.logger,
    standardise.neutralise.logger,
    standardise.unsalt.logger,
    standardise.rules.logger,
):
    _logger.setLevel(50)

# resolve checkpoint paths relative to this file (code/ -> framework/ -> model/checkpoints)
CHECKPOINTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "checkpoints")
)
FEATURE_IDS = np.load(os.path.join(CHECKPOINTS_DIR, "feature_ids.npy"))  # sorted ascending
FEATURE_LOG_PROB_POS = np.load(os.path.join(CHECKPOINTS_DIR, "feature_log_prob_pos.npy"))
PRIOR_POS = 0.0  # class_log_prior_[1] of the released MAIP model
MORGAN_RADIUS = 3


def _score_one(smiles):
    """Score a single SMILES; return np.nan if it cannot be parsed or standardised."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return np.nan
    try:
        mol = standardise.run(mol, output_rules_applied=[])
    except Exception:
        # standardiser rejects e.g. pure salts / solvates, exactly as the upstream CLI does
        return np.nan
    fingerprint = rdMolDescriptors.GetMorganFingerprint(
        mol, MORGAN_RADIUS, useFeatures=True, useCounts=False
    ).GetNonzeroElements()
    if not fingerprint:
        return np.nan
    fids = np.fromiter(fingerprint.keys(), dtype=np.int64)
    vals = np.fromiter(fingerprint.values(), dtype=np.float64)
    # map feature ids -> vocabulary columns via binary search; drop features unseen in training
    idx = np.clip(np.searchsorted(FEATURE_IDS, fids), 0, FEATURE_IDS.shape[0] - 1)
    valid = FEATURE_IDS[idx] == fids
    return float(np.sum(vals[valid] * FEATURE_LOG_PROB_POS[idx[valid]]) + PRIOR_POS)


def predict(smiles_list):
    """Return an (n, 1) array of MAIP scores, one row per input SMILES (np.nan on failure)."""
    return np.array([[_score_one(smi)] for smi in smiles_list], dtype=np.float64)
