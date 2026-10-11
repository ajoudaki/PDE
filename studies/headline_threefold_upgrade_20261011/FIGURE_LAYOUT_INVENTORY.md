# Static-figure layout inventory for `paper/compact.tex`

## Scope and result

This is a layout/asset inventory only. It covers every top-level PDF, PNG, and
SVG in `paper/figures/`; it excludes the HTML gallery, manifests, data, and
plotting/training scripts. PDF pages were rendered for visual inspection, but
no experiment was run and no source asset was edited.

- Static files: **77** = **44 PDF + 22 PNG + 11 SVG**.
- Unique stems: **44**. Every stem has a PDF, so the appendix can use one
  consistent PDF-first policy.
- Printable PDF panels: **50** = 43 one-page PDFs plus the seven pages of
  `experimental_gallery.pdf`.
- `experimental_gallery.pdf` is the only multipage PDF.
- No PDF has a large accidental outer white margin that warrants TeX
  `trim`/`viewport`. A 72 dpi white-background bounding-box check found only
  ordinary design margins; the larger side margins in a few slide-style
  figures are part of their layout.

In the table below, a stem plus its listed extensions is the complete literal
file list: for example, `learning_clocks` with `pdf,png,svg` means the three
files `learning_clocks.pdf`, `learning_clocks.png`, and
`learning_clocks.svg`. PDF sizes are MediaBox width x height in points
(72 pt/in).

## Complete inventory

| Stem | Extensions | PDF pages | PDF MediaBox (pt) | Aspect |
|---|---:|---:|---:|---:|
| `circle_deep` | pdf | 1 | 813.127 x 726.168 | 1.12 |
| `circle_deep_radial` | pdf,png,svg | 1 | 468.000 x 396.500 | 1.18 |
| `circle_shallow` | pdf | 1 | 1065.320 x 627.656 | 1.70 |
| `circle_shallow_radial` | pdf,png,svg | 1 | 468.000 x 396.500 | 1.18 |
| `circles_deep` | pdf | 1 | 469.213 x 153.387 | 3.06 |
| `circles_shallow` | pdf | 1 | 469.213 x 153.387 | 3.06 |
| `clocks` | pdf | 1 | 357.756 x 169.105 | 2.12 |
| `compression_checks` | pdf | 1 | 829.200 x 242.400 | 3.42 |
| `compression_logarithmic` | pdf | 1 | 678.000 x 242.400 | 2.80 |
| `compression_validation` | pdf | 1 | 678.000 x 242.400 | 2.80 |
| `experimental_gallery` | pdf | 7 | 864.000 x 504.000 (each) | 1.71 |
| `factors` | pdf | 1 | 471.955 x 250.003 | 1.89 |
| `frozen_ntk_radial_preview` | pdf,png | 1 | 451.573 x 222.286 | 2.03 |
| `learning_clocks` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `learning_controls_equal_mixed_odd` | pdf,png | 1 | 495.800 x 215.877 | 2.30 |
| `learning_controls_gallery` | pdf,png | 1 | 508.108 x 935.877 | 0.54 |
| `learning_controls_gallery_a` | pdf | 1 | 508.108 x 575.877 | 0.88 |
| `learning_controls_gallery_b` | pdf | 1 | 508.108 x 395.877 | 1.28 |
| `learning_controls_quadrant_alternating` | pdf,png | 1 | 488.420 x 215.877 | 2.26 |
| `learning_controls_quadrant_center_edges` | pdf,png | 1 | 489.653 x 216.375 | 2.26 |
| `learning_controls_quadrant_pairs` | pdf,png | 1 | 489.541 x 215.877 | 2.27 |
| `learning_controls_two_outliers_alternating` | pdf,png | 1 | 489.541 x 215.877 | 2.27 |
| `learning_in_motion` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `mechanism` | pdf | 1 | 513.461 x 169.453 | 3.03 |
| `memory_mechanism` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `mnist` | pdf | 1 | 459.496 x 168.682 | 2.72 |
| `mnist_residuals` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `mnist_rms` | pdf | 1 | 512.400 x 348.412 | 1.47 |
| `mnist_scatter` | pdf | 1 | 868.658 x 296.400 | 2.93 |
| `moments` | pdf | 1 | 484.265 x 144.220 | 3.36 |
| `order_decay` | pdf | 1 | 457.576 x 249.829 | 1.83 |
| `order_sensitivity` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `orders` | pdf | 1 | 434.325 x 159.097 | 2.73 |
| `paired_projection` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `same_rank` | pdf | 1 | 398.739 x 166.692 | 2.39 |
| `same_rank_dynamics` | pdf,png,svg | 1 | 825.120 x 405.720 | 2.03 |
| `same_rank_radial_preview` | pdf,png | 1 | 422.913 x 220.323 | 1.92 |
| `sphere3_time` | pdf,png | 1 | 331.200 x 216.000 | 1.53 |
| `sphere3_tradeoff_endpoint` | pdf,png | 1 | 331.200 x 216.000 | 1.53 |
| `sphere3_tradeoff_max_time` | pdf,png | 1 | 331.200 x 216.000 | 1.53 |
| `sphere_comparison` | pdf,png,svg | 1 | 468.000 x 362.939 | 1.29 |
| `sphere_orders` | pdf,png,svg | 1 | 468.000 x 362.939 | 1.29 |
| `trajectory` | pdf | 1 | 441.399 x 129.791 | 3.40 |
| `trajectory_rms` | pdf | 1 | 309.356 x 132.904 | 2.33 |

The extension accounting is exact:

- PDF+PNG+SVG (11 stems): `circle_deep_radial`,
  `circle_shallow_radial`, `learning_clocks`, `learning_in_motion`,
  `memory_mechanism`, `mnist_residuals`, `order_sensitivity`,
  `paired_projection`, `same_rank_dynamics`, `sphere_comparison`,
  `sphere_orders`.
- PDF+PNG (11 stems): `frozen_ntk_radial_preview`,
  `learning_controls_equal_mixed_odd`, `learning_controls_gallery`,
  `learning_controls_quadrant_alternating`,
  `learning_controls_quadrant_center_edges`,
  `learning_controls_quadrant_pairs`,
  `learning_controls_two_outliers_alternating`,
  `same_rank_radial_preview`, `sphere3_time`,
  `sphere3_tradeoff_endpoint`, `sphere3_tradeoff_max_time`.
- PDF only: the remaining 22 stems in the table.

## Duplicate and alternate-presentation audit

Visual inspection supports treating all same-stem PNG/SVG files as format
copies of their PDFs. They should not be inserted separately when the request
is to include each unique static figure; prefer the PDF and retain the raster
and SVG files as source/distribution alternatives.

The following are **not accidental duplicates** and should remain if “all
existing figures” means every distinct PDF stem:

- `circle_deep_radial` and `circles_deep` present essentially the same family
  of radial panels in different assemblies (two-row annotated plate versus a
  panoramic strip). The shallow pair behaves the same way.
- `learning_controls_gallery` is the tall five-row composite of the five
  separate `learning_controls_*` plates. `learning_controls_gallery_a` and
  `_b` are the page-friendly three-row and two-row partition of that same
  gallery. These are alternate assemblies, not format copies.
- The seven `experimental_gallery` pages are slide-style composite
  presentations. Pages 1, 2, and 4--7 visibly reuse/reframe material from
  `memory_mechanism`, `learning_in_motion`, `learning_clocks`,
  `paired_projection`, `mnist_residuals`, and `order_sensitivity`,
  respectively; page 3 reframes the control-family material. The pages add
  headings, annotations, or layout changes and are not exact copies of the
  standalone PDFs.
- `sphere3_tradeoff_endpoint` and `sphere3_tradeoff_max_time` look very similar
  at thumbnail scale but differ in their reported statistic/labels; keep both.

## Geometry hazards

- **Tall:** `learning_controls_gallery` (aspect 0.54) needs a height cap and
  effectively owns most of a page. `learning_controls_gallery_a` (0.88) is
  also portrait-oriented. Do not size either only by `width=\linewidth`.
- **Very wide (aspect at least 2.7):** `circles_deep`, `circles_shallow`,
  `compression_checks`, `compression_logarithmic`, `compression_validation`,
  `mechanism`, `mnist`, `mnist_scatter`, `moments`, `orders`, and
  `trajectory`. These work best as full-width strips paired vertically with
  another panel.
- **Multipage:** `experimental_gallery.pdf` needs seven explicit insertions
  using `page=1` through `page=7`; a plain `\includegraphics` inserts only its
  first page.
- **Large MediaBoxes:** `circle_deep`, `circle_shallow`, `learning_*`,
  `memory_mechanism`, `mnist_residuals`, `order_sensitivity`,
  `paired_projection`, and `same_rank_dynamics` exceed ordinary text width in
  their native coordinates. This is harmless for vector PDFs when
  `width`/`height` plus `keepaspectratio` are supplied.
- **Outer whitespace:** none is severe. At 72 dpi, the largest ordinary outer
  margin totals were roughly ten percent of width (`paired_projection` and
  some slide-style layouts). TeX cropping is not justified and risks removing
  intentional labels/callouts.

## Compact printable packing recommendation

Use a nonfloating atlas after the bibliography: `\clearpage`, an unnumbered
heading, then explicit page groups. Add `graphicx`; place each panel in a
centered block with an external, uniform label/caption (at least `\small`, so
the identifier does not shrink with the art). For ordinary paired landscape
panels, use approximately

```tex
\includegraphics[width=.98\linewidth,height=.38\textheight,
                 keepaspectratio]{figures/<stem>.pdf}
```

Use `.35--.37\textheight` if two captions are long. Explicit `\newpage` after
each pair prevents float drift and nearblank float pages. A local
`\raggedbottom` is preferable to vertically stretching the inter-panel gap.
For `experimental_gallery`, add `page=<n>` to the options.

The following 25 two-panel sheets include all 50 PDF panels exactly once and
pair alternate presentations where that is informative:

1. `circle_deep` + `circles_deep`
2. `circle_shallow` + `circles_shallow`
3. `circle_deep_radial` + `circle_shallow_radial`
4. `compression_checks` + `compression_logarithmic`
5. `compression_validation` + `factors`
6. `experimental_gallery` p.1 + `memory_mechanism`
7. `experimental_gallery` p.2 + `learning_in_motion`
8. `experimental_gallery` p.3 + `learning_controls_equal_mixed_odd`
9. `experimental_gallery` p.4 + `learning_clocks`
10. `experimental_gallery` p.5 + `paired_projection`
11. `experimental_gallery` p.6 + `mnist_residuals`
12. `experimental_gallery` p.7 + `order_sensitivity`
13. `frozen_ntk_radial_preview` + `same_rank_radial_preview`
14. `learning_controls_gallery` + `trajectory`
15. `learning_controls_gallery_a` + `learning_controls_gallery_b`
16. `learning_controls_quadrant_alternating` +
    `learning_controls_quadrant_center_edges`
17. `learning_controls_quadrant_pairs` +
    `learning_controls_two_outliers_alternating`
18. `mechanism` + `clocks`
19. `mnist` + `mnist_rms`
20. `mnist_scatter` + `moments`
21. `order_decay` + `orders`
22. `same_rank` + `same_rank_dynamics`
23. `sphere3_time` + `sphere3_tradeoff_endpoint`
24. `sphere3_tradeoff_max_time` + `sphere_comparison`
25. `sphere_orders` + `trajectory_rms`

Two sheets need custom sizing:

- Sheet 14: cap `learning_controls_gallery` at about
  `.69--.72\textheight`, then use the very wide `trajectory` as a full-width
  strip at about `.14--.17\textheight`. Keep both external labels compact.
- Sheet 15: cap `learning_controls_gallery_a` at about `.58--.61\textheight`
  and `_b` at about `.25--.28\textheight`. Width-only sizing would overfill.

If the internal text in sheet 3 or sheets 23--24 proves too small in the final
PDF, preserve the same 25-sheet count by using two columns within the allotted
sheet only after a print-size check; do not crop. The safest default is the
full-width, vertically stacked height-capped placement above.

## Scratch evidence

The rendered PDF pages and the labeled contact sheet are under
`data/generated/headline_threefold_upgrade_20261011/figure_layout_scratch/`.
They are inspection aids, not replacement publication assets.
