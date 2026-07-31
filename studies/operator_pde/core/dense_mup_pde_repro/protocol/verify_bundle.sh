#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
archive_root="$(cd "$project_dir/.." && pwd)"

case "${1:-}" in
  snapshot)
    bash "$archive_root/verify_source_only.sh"
    bash "$archive_root/verify_snapshot.sh"
    ;;
  source)
    bash "$archive_root/verify_source_only.sh"
    ;;
  evidence)
    if [[ ! -f "$project_dir/results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz" ]]; then
      echo "Raw evidence is absent. Run protocol/reproduce_full.sh first." >&2
      exit 2
    fi
    bash "$archive_root/verify_reproduced_core.sh"
    ;;
  *)
    echo "usage: $0 {snapshot|source|evidence}" >&2
    exit 2
    ;;
esac
