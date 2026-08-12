# MAIP — Malaria Inhibitor Prediction
# Local re-implementation of the open-source model released by ChEMBL
# (https://github.com/chembl/maip_public), replacing the previous online-server call.
# Inference logic lives in maip_predict.py; checkpoints (model/checkpoints/) are
# gitignored and persisted via eosvc.
import sys

import numpy as np
from ersilia_pack_utils.core import read_smiles, write_out

from maip_predict import predict

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read SMILES from the .csv input (single column with header)
_, smiles_list = read_smiles(input_file)

# run model (one row per input molecule, order preserved, np.nan for failures)
outputs = predict(smiles_list)
if outputs.shape != (len(smiles_list), 1):
    raise ValueError(
        f"Expected model output shape ({len(smiles_list)}, 1), got {outputs.shape}."
    )

# write output
write_out(outputs, ["maip_score"], output_file, np.float32)
