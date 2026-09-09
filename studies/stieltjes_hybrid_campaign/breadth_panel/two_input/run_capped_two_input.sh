#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 6 ]]; then
  echo "usage: $0 CONFIG LOCK UNLOCK POINT DEVICE OUTPUT_ROOT" >&2
  exit 64
fi

config="$1"
lock="$2"
unlock="$3"
point="$4"
device="$5"
output_root="$6"
here="$(cd "$(dirname "$0")" && pwd)"

wall_seconds="$({
  python -c '
import json, sys
document = json.load(open(sys.argv[1], encoding="utf-8"))
matches = [p for p in document["points"] if p["id"] == sys.argv[2]]
if len(matches) != 1:
    raise SystemExit("point must occur exactly once")
value = float(matches[0]["caps"]["wall_seconds"])
if value <= 0:
    raise SystemExit("wall cap must be positive")
print(value)
' "$config" "$point"
})"

exec timeout --foreground --signal=TERM --kill-after=15s "${wall_seconds}s" \
  python "$here/run_two_input_point.py" \
  --config "$config" \
  --lock "$lock" \
  --unlock "$unlock" \
  --point "$point" \
  --device "$device" \
  --output-root "$output_root"
