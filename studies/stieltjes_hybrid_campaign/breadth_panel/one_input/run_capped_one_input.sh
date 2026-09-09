#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: $0 EXTERNAL_SECONDS RUNNER_ARGS..." >&2
  exit 64
fi

seconds="$1"
shift
if [[ ! "$seconds" =~ ^[1-9][0-9]*$ ]]; then
  echo "EXTERNAL_SECONDS must be a positive integer" >&2
  exit 64
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec timeout --signal=TERM --kill-after=5 "${seconds}s" \
  python "$script_dir/run_one_input_point.py" \
  --external-timeout-seconds "$seconds" "$@"
