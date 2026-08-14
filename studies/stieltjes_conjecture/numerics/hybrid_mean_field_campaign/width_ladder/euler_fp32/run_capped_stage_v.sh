#!/usr/bin/env bash
set -u

here="$(cd "$(dirname "$0")" && pwd)"
point="${1:-}"
device="${2:-}"
case "$point" in
  # The engine enforces the scientific 60/120-second caps.  The five-second
  # outer margin exists only so it can serialize a fail-closed manifest.
  v_n8192_h1e5) cap=65 ;;
  v_n8192_h5e6) cap=125 ;;
  *) echo "unknown frozen Stage-V point" >&2; exit 64 ;;
esac
if [[ -z "$device" ]]; then
  echo "usage: run_capped_stage_v.sh POINT cuda:N" >&2
  exit 64
fi
timeout --signal=TERM --kill-after=5s "${cap}s" \
  python3 "$here/run_stage_v_point.py" --point "$point" --device "$device"
status=$?
if [[ $status -ne 0 ]]; then
  python3 "$here/run_stage_v_point.py" --point "$point" --finalize-timeout
fi
exit "$status"
