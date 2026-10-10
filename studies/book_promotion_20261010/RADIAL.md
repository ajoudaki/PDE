# Interactive radial experiment explorer

This is the multi-experiment HTML interface meant by the user's radial-viewer
request. It adapts `paper/interactive/circle_explorer.html`, retaining its radial
and output-versus-angle plots, experiment/width/seed selectors, training-time
slider, playback, model toggles, and hover/pinned values. Alignment can use
physical time, training loss, or supplied recorded endpoints. Local JSON files
can be loaded together; experiment IDs must be distinct. Clear experiments
removes the current collection before loading replacements.

The reusable source is `radial_explorer.html`; `radial_explorer.py` validates
and embeds supplied data. D3 7.9.0 remains inlined with its original attribution,
so the generated HTML needs no server, CDN, or network access. The original
embedded campaign payload is removed. The simpler single-experiment viewer
in `visual_core.py` remains useful for circle/sphere array previews; it is a
different interface.

## Data and export

`make_case(id, label, query_inputs, training_inputs, labels, models, ...)`
accepts the unit circle inputs used by `data_core.py` and `compression_core.py`.
Each model supplies its own `times[T]`, `curves[T,Q]`, and actual
`trainPredictions[T,M]`. Optional source IDs and provenance remain attached.
Query directions, curve columns, and query IDs are sorted together by angle;
training arrays retain their ordering. No training or model evaluation happens
inside the exporter.

Models use distinct IDs and a display name. Generic methods need no special
metadata. `kind="network"` additionally supplies `width` and `seed` for the
selectors; `network-mean` requires width. Legacy closure records and optional
zero-initialized analytic NTK arrays are also supported. The adapter accepts
all 15 cases and 124 model records in the original payload; that was a schema
compatibility check, not scientific validation of its results.

```python
case = make_case("run-a", "Run A", queries, inputs, labels, model_records)
write_explorer(output_path, {"cases": [case]})
write_explorer(empty_path, {"cases": []})  # load files later in the browser
```

Existing JSON case or bundle files can also be combined without training:

```bash
python studies/book_promotion_20261010/radial_explorer.py run-a.json run-b.json --out data/generated/book_promotion_20261010/explorer.html
```

Use a fresh output filename: the exporter replaces that named output. The HTML
template and source JSON inputs are protected from CLI overwrite. JSON is
escaped before embedding, and display names enter the page through text nodes.

## Alignment and interpretation

Loss is the unhalved weighted squared training error; weights are nonnegative
and sum to one. Supplied scalar losses are checked against actual training
predictions. Separate `lossTrainPredictions`, `lossLabels`, and `lossWeights`
preserve a provided mean of seed losses, rather than replacing it with the loss
of the mean prediction.

Physical-time mode uses the common recorded time interval. Between saved times,
the viewer linearly interpolates predictions and recomputes their training
loss. Loss mode selects the first saved descending bracket of the requested
loss and solves within that interpolated bracket; it does not recover an exact
training trajectory. Missing common ranges disable the corresponding mode.
Recorded-endpoint mode allows different model times and does not infer fitting
or convergence. An endpoint outside the saved frames needs its own endpoint
loss or training predictions; a legacy externally reported endpoint loss
without those predictions can only be checked for finiteness and sign.

Angular hover values use periodic linear interpolation on the actual supplied
grid. Relative query RMS uses equal weights on that grid and the selected
network as reference; it is not a continuous-circle error certificate. Radial
distance is a positive offset plus signed output; the dashed ring denotes zero.
Scales stay fixed through playback for the current selection. Changing visible
methods or network realization can change the scale.

## Reproduce the small example and checks

```bash
PYTHONPATH=code:studies/book_promotion_20261010 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/book_promotion_20261010/radial_example.py --out data/generated/book_promotion_20261010/my_radial_example
PYTHONPATH=code:studies/book_promotion_20261010 /home/amir/miniconda3/bin/python -B -m unittest discover -s studies/book_promotion_20261010 -p 'test_radial*.py' -v
```

The example creates two toy circle experiments, with three and four training
inputs, 96 queries, and three saved times through 0.04. It includes Dense
width/seed variants and the existing Legendre, Harmonic, and Taylor cores.
Only the width-64 seed-17 Dense run shares initialization with the compression
models. This bounded integration example is not a fitting or approximation
experiment. Individual case JSON, a combined bundle, populated/empty HTML,
and a settings/source/output-hash manifest are written to a new directory.

Nine Python tests check arrays, losses, endpoints, provenance alignment, and
safe export. One Node test executes the actual application and bundled D3 with
a small DOM/SVG stand-in, checking the controls and alignment computations.
It checks SVG path finiteness but does not assess browser layout or pixels.
No browser-rendering review is claimed.

The completed example is at
`data/generated/book_promotion_20261010/radial_example01/explorer.html`.
Validation is recorded in `radial_validation01/validation.json` under the same
generated-data root. All of this remains study-owned and unpromoted.
