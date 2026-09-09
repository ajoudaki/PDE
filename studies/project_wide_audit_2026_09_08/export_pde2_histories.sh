#!/usr/bin/env bash
# Run manually with sudo. Copies only the 19 explicitly inventoried histories.
# Does not change source permissions, copy credentials, or operate on Codex tasks.
set -euo pipefail

if [[ $EUID -ne 0 ]]; then
  echo "Please run this helper with sudo from your normal terminal." >&2
  exit 1
fi

pde_manifest=/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/PDE2_HISTORY_PATHS.txt
mapfile -t pde_histories < "$pde_manifest"
if [[ ${#pde_histories[@]} -ne 19 ]]; then
  echo "Expected exactly 19 listed history files; no export created." >&2
  exit 1
fi
for pde_history in "${pde_histories[@]}"; do
  case "$pde_history" in
    /home/codex-b/.codex/sessions/*.jsonl) ;;
    *) echo "Unexpected source path; no export created." >&2; exit 1 ;;
  esac
  if [[ ! -f "$pde_history" || -L "$pde_history" || ! -r "$pde_history" ]]; then
    echo "Missing, symlinked, or unreadable source: $pde_history" >&2
    exit 1
  fi
done

pde_export_dir=$(mktemp -d /home/amir/pde-history-export.XXXXXX)
install -d -m 700 -o amir -g amir "$pde_export_dir"
for pde_history in "${pde_histories[@]}"; do
  pde_destination="$pde_export_dir/${pde_history##*/}"
  if [[ -e "$pde_destination" ]]; then
    echo "Duplicate destination; partial export retained at $pde_export_dir" >&2
    exit 1
  fi
  install -m 600 -o amir -g amir -- "$pde_history" "$pde_destination"
done
echo "Copied ${#pde_histories[@]} history files. Originals unchanged."
echo "Export directory: $pde_export_dir"
