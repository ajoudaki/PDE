#!/usr/bin/env bash
set -euo pipefail

export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MPLCONFIGDIR="${TMPDIR:-/tmp}/dense_mup_mpl"

python -m unittest discover -s tests -v
python run_all.py --config config/protocol.json
python make_manifest.py
