#!/usr/bin/env bash
# Rasterize the paper's experiment figures for the deck (paper colour instead of white).
# exp_combined stacks the end-of-training comparison above the whole-trajectory figure.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
figs="$here/../../../figures"
img="$here/../img"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
for name in accuracy trajectory storage spectra; do
  pdftocairo -png -singlefile -r 500 "$figs/exp_$name.pdf" "$work/exp_$name" 2>/dev/null
  convert "$work/exp_$name.png" -fill '#FBFAF7' -opaque white "$work/exp_$name.png"
done
cp "$work/exp_storage.png" "$work/exp_spectra.png" "$img/"
convert "$work/exp_accuracy.png" \( -size 3250x60 xc:'#FBFAF7' \) "$work/exp_trajectory.png" -append \
  "$img/exp_combined.png"
