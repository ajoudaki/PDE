#!/usr/bin/env bash
set -euo pipefail

reference_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
action="${1:-}"

case "${action}" in
  gpu-preflight)
    exec /usr/bin/timeout --signal=TERM --kill-after=15s 120s \
      python "${reference_dir}/gpu_preflight.py"
    ;;
  cpu-validation)
    exec /usr/bin/timeout --signal=TERM --kill-after=15s 150s \
      python "${reference_dir}/run_reference.py" \
      "${reference_dir}/configs/validation_cpu.json"
    ;;
  gpu0-validation)
    exec /usr/bin/timeout --signal=TERM --kill-after=15s 210s \
      python "${reference_dir}/run_reference.py" \
      "${reference_dir}/configs/validation_gpu0.json"
    ;;
  gpu1-validation)
    exec /usr/bin/timeout --signal=TERM --kill-after=15s 210s \
      python "${reference_dir}/run_reference.py" \
      "${reference_dir}/configs/validation_gpu1.json"
    ;;
  production)
    frozen_config="${reference_dir}/configs/FROZEN_PRODUCTION.json"
    unlock="${reference_dir}/PRODUCTION_UNLOCK.json"
    if [[ ! -f "${frozen_config}" || ! -f "${unlock}" ]]; then
      echo "Scientific production remains locked: frozen config/unlock absent." >&2
      exit 3
    fi
    exec /usr/bin/timeout --signal=TERM --kill-after=30s 86430s \
      python "${reference_dir}/run_reference.py" "${frozen_config}"
    ;;
  successor-01)
    successor_config="${reference_dir}/configs/FROZEN_SUCCESSOR_01.json"
    unlock="${reference_dir}/PRODUCTION_UNLOCK.json"
    if [[ ! -f "${successor_config}" || ! -f "${unlock}" ]]; then
      echo "Successor-01 remains locked: frozen config/unlock absent." >&2
      exit 3
    fi
    exec /usr/bin/timeout --signal=TERM --kill-after=30s 2430s \
      python "${reference_dir}/run_reference.py" "${successor_config}"
    ;;
  *)
    echo "usage: $0 {gpu-preflight|cpu-validation|gpu0-validation|gpu1-validation|production|successor-01}" >&2
    exit 64
    ;;
esac
