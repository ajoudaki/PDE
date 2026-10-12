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
cp "$work/exp_storage.png" "$img/"
# Insight 2 uses only the spectrum panel (left half of the spectra figure).
convert "$work/exp_spectra.png" -gravity West -crop 52x100%+0+0 +repage "$img/exp_spectrum.png"
# Insight 1 uses the top row of the Legendre moment illustration from plot_figures.py.
python3 "$here/../../../plot_figures.py" --only moments --out "$work/plots" > /dev/null
pdftocairo -png -singlefile -r 500 "$work/plots/moments.pdf" "$work/moments" 2>/dev/null
convert "$work/moments.png" -fill '#FBFAF7' -opaque white -gravity North -crop 100x60%+0+0 +repage \
  "$img/moments.png"
convert "$work/exp_accuracy.png" \( -size 3250x60 xc:'#FBFAF7' \) "$work/exp_trajectory.png" -append \
  "$img/exp_combined.png"
