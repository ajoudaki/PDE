# Offline radial experiment explorer

`pde.radial_explorer` validates supplied data and embeds them in the
adjacent `pde/radial_explorer.html` template. **Distribute both files.**
D3 7.9.0 is inlined with its attribution. Generated HTML works locally
without a server or network request. The interface supplies experiment,
width and seed selectors, playback, model toggles and hover/pinned values.
Use [prediction views](PREDICTION_VIEWS.md) for static plots and sphere previews.

## Data and export

`make_case(id, label, query_inputs, training_inputs, labels, models, ...)`
accepts the unit circle inputs used by `pde.compression_data` and `pde.compression`.
Each model supplies its own `times[T]`, `curves[T,Q]`, and actual
`trainPredictions[T,M]`. Optional source IDs and provenance remain attached.
Query directions, curve columns, and query IDs are sorted together by angle;
training arrays retain their ordering. No training or model evaluation happens
inside the exporter.

Models use distinct IDs and a display name. Generic methods need no special
metadata. `kind="network"` additionally supplies `width` and `seed` for the
selectors; `network-mean` requires width. Legacy closure records and optional
zero-initialized analytic NTK arrays are also supported. 

```python
case = make_case("run-a", "Run A", queries, inputs, labels, model_records)
write_explorer(output_path, {"cases": [case]})
write_explorer(empty_path, {"cases": []})  # load files later in the browser
```

Existing JSON case or bundle files can also be combined without training:

```bash
PYTHONPATH=code python -B -m pde.radial_explorer run-a.json run-b.json --out data/established/explorer.html
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

Run the commands in [the compression guide](COMPRESSION.md). The
[radial example](scripts/example_radial_explorer.py) creates two toy
experiments with three/four training inputs, 96 queries and three saved
times through 0.04. Only Dense width 64, seed 17 shares initialization
with its compression models; other variants exercise selectors. It
writes case JSON, populated/empty HTML and source/output hash manifests
into a fresh directory. It is an operational example, not a fitting
or approximation experiment.

Schema tests check arrays, weighted losses, endpoints, IDs and safe
export. The Node test executes the actual bundled D3 and application
with a DOM/SVG stand-in; it checks controls, alignment and finite SVG
paths. It does not assess browser layout or pixels.
