#!/usr/bin/env bash
set -euo pipefail

study_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
run_dir="${PDE_LONG_HORIZON_OUTPUT_ROOT:-$study_dir/../../data/generated/resnet_dense_long_horizon}"
cd "$study_dir"

export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MPLCONFIGDIR="${TMPDIR:-/tmp}/dense_mup_mpl"

python -m unittest discover -s tests -v
python run_all.py --config config/protocol.json --output-root "$run_dir"
python make_manifest.py --output-root "$run_dir"
