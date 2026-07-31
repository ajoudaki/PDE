#!/usr/bin/env bash
set -euo pipefail

bundle_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python_bin="${PYTHON_BIN:-python}"

export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0

cd "$bundle_root/dense_mup_pde_repro"
PYTHONPATH=src "$python_bin" -m unittest discover -s tests -v

cd "$bundle_root/agent_outputs/numerics"
PYTHONPATH=. "$python_bin" -m unittest -v test_operator_hermite_pde.py

cd "$bundle_root/dense_mup_pde_repro"
PYTHONPATH=src "$python_bin" verify_evidence.py

cd "$bundle_root"
"$python_bin" verify_reproduced_core.py

echo "Canonical regenerated-evidence verification passed."
