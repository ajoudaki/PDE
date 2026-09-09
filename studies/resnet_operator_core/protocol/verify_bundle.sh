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
    if [[ ! -f results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz ]]; then
      echo "Raw evidence is absent. Run protocol/reproduce_full.sh first." >&2
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
