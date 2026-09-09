#!/usr/bin/env bash
# Standalone exporter: no writes to the PDE repository, no global installs.
set -euo pipefail
PDE_EXPORT_ENTRY="${BASH_SOURCE[0]}"
while [[ -L "$PDE_EXPORT_ENTRY" ]]; do
  PDE_EXPORT_BASE="$(cd -P -- "$(dirname -- "$PDE_EXPORT_ENTRY")" && pwd)"
  PDE_EXPORT_ENTRY="$(readlink -- "$PDE_EXPORT_ENTRY")"
  [[ "$PDE_EXPORT_ENTRY" == /* ]] || PDE_EXPORT_ENTRY="$PDE_EXPORT_BASE/$PDE_EXPORT_ENTRY"
done
PDE_EXPORT_DIR="$(cd -P -- "$(dirname -- "$PDE_EXPORT_ENTRY")" && pwd)"
exec python3 -B "$PDE_EXPORT_DIR/export_book.py" "$@"
