#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON_BIN:-python}"

cd "$project_dir"

case "${1:-}" in
  source)
    PYTHONPATH=src "$python_bin" -m unittest discover -s tests -v
    ;;
  evidence)
    input_dir="$("$python_bin" -B -c 'from runtime_paths import INPUT_ROOT; print(INPUT_ROOT)')"
    if [[ ! -f "$input_dir/results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz" ]]; then
      echo "Raw evidence is absent in $input_dir. Select PDE_OPERATOR_INPUT_ROOT or reproduce into that run directory." >&2
      exit 2
    fi
    PYTHONPATH=src "$python_bin" -m unittest discover -s tests -v
    PYTHONPATH=src "$python_bin" verify_evidence.py
    ;;
  *)
    echo "usage: $0 {source|evidence}" >&2
    exit 2
    ;;
esac
