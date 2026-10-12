#!/usr/bin/env bash
# Render the deck's LaTeX math plates to transparent PNGs in ../img.
# 12 pt text at 396 dpi, shown at half size, matches the deck's 33 px body text.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
cd "$here"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
for name in theorem feature nth selected axis; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$work" \
    "$here/$name.tex" > "$work/$name.log" || { tail -20 "$work/$name.log"; exit 1; }
  pdftocairo -png -transp -singlefile -r 396 "$work/$name.pdf" "$here/../img/$name"
done
