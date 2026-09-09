#!/usr/bin/env bash
set -euo pipefail

bundle_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python_bin="${PYTHON_BIN:-python}"
cd "$bundle_root"
sha256sum --check SNAPSHOT_MANIFEST.sha256
"$python_bin" verify_source_only.py --snapshot
echo "Compact result snapshot verification passed."
