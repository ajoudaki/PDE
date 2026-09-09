#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: $0 POINT_ID CUDA_DEVICE" >&2
  exit 64
fi

campaign_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
point_id="$1"
cuda_device="$2"
config_path="${campaign_dir}/configs/FROZEN_WIDTH_LADDER.json"
unlock_path="${campaign_dir}/PRODUCTION_UNLOCK.json"
run_root="${campaign_dir}/runs/frozen_width_viability_20260819"

case "${point_id}" in
  n2048_r16) outer_seconds=195 ;;
  n4096_r16) outer_seconds=615 ;;
  n4096_r2_halfstep) outer_seconds=135 ;;
  n8192_r8_shard0|n8192_r8_shard1) outer_seconds=1215 ;;
  *)
    echo "unknown frozen point: ${point_id}" >&2
    exit 64
    ;;
esac

exec timeout --signal=TERM --kill-after=5s "${outer_seconds}s" \
  python3 "${campaign_dir}/run_width_point.py" \
  --config "${config_path}" \
  --point "${point_id}" \
  --device "${cuda_device}" \
  --run-root "${run_root}" \
  --unlock "${unlock_path}"
