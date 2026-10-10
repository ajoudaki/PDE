# Array-based prediction views

For the original **multi-experiment interactive radial explorer**, including
time/loss alignment and width/seed selection, see [RADIAL_EXPLORER.md](RADIAL_EXPLORER.md).
The functions below provide static plots and simpler array-preview viewers.

`pde.prediction_views` supplies radial circle plots, sphere prediction/error plots,
and standalone HTML viewers. It consumes supplied arrays and performs no model
evaluation, training, archive loading, or experiment selection. The module
imports NumPy; static plots additionally need Matplotlib. Generated viewers
need only a browser and work from a local file without servers, CDNs, or external
libraries. 

## Inputs and small interface

Let $N$ be query count and $T$ saved frame count. `queries` is a finite array
of shape `(N,2)` for the circle or `(N,3)` for the sphere, with unit rows.
These directions are the normalized model inputs $v=x/\sqrt d$ used by
`pde.compression`; no further normalization is applied. `predictions`
maps nonempty model names to finite arrays of shape `(N,)` or `(T,N)`.
All entries must have the same shape after promoting `(N,)` to `(1,N)`;
there is no implicit broadcasting, time alignment, or query reordering across
models. NumPy arrays or convertible CPU tensors without gradients work.

```python
plot_circle(queries, predictions, *, frame=-1, reference=None,
            training_inputs=None, training_labels=None)  # -> Figure
plot_sphere(queries, predictions, *, frame=-1, model=None, reference=None,
            training_inputs=None)                        # -> Figure
write_viewer(path, queries, predictions, *, times=None, reference=None,
             training_inputs=None, training_labels=None,
             title="Prediction comparison")              # -> Path
```

The static functions return a Matplotlib figure; the caller saves and closes
it. `frame=-1` selects the last frame. The circle plot overlays all supplied
models. The sphere plot selects `model` (the first supplied name by default)
and, when requested, displays the reference and signed difference beside it.
`reference` must name a supplied prediction array. Training inputs, if present,
are unit rows in the same dimension. Circle training labels are optional scalar
values aligned with those inputs.

The viewer provides model and reference selectors, a frame slider, and playback.
`times`, if provided, is a strictly increasing finite array of length `T`;
frames without times are labelled as frame indices. The viewer starts with
the first reference and another model when available. Changing any selector
redraws the plots and recomputes the displayed statistics. Model names and the
title enter the page through text nodes; embedded JSON escapes HTML-sensitive
characters. `write_viewer` creates parent folders and replaces its named output
file, so callers should choose a explicit output location.

## What the encodings mean

For a signed circle value $f_j$ at unit direction $v_j$, the plotted point is

$$
\left(1+0.8\frac{f_j}{M}\right)v_j,
\qquad M=\max_j|f_j|,
$$

where the actual scale also includes every supplied model/frame and any plotted
training labels. An identically zero collection uses $M=1$ to keep a valid
scale. Thus radius stays between $0.2$ and $1.8$: negative values remain at the
same input angle. The dashed radius-one ring means zero, and radial ticks
display signed values. Curves connect samples in angular order and close around
the circle; they do not evaluate the unknown function between queries.
Training labels appear at their signed radii. Without labels, training
directions appear on the zero ring and are identified as locations.

Sphere plots show colors at the supplied queries, without surface interpolation
or lighting. The front orthographic view maps $(x,y,z)$ to $(x,y)$ for $z\ge0$;
the back maps it to $(-x,y)$ for $z<0$. The equator belongs to the front so every
query and training direction is assigned to exactly one hemisphere. Marker
overlap can occur under projection; apparent disk area is not sphere area.
Black dots are training locations, not label magnitudes. Prediction panels share
one symmetric blue–white–red scale across models and frames. Signed-error
panels use a separate common symmetric scale. Each bar has three compact
ticks at its negative limit, zero, and positive limit.

For selected prediction $f_j$ and supplied reference $g_j$ at the same query,
the signed error is $f_j-g_j$. The displayed sample statistics are

$$
\operatorname{RMS}_{\rm sample}
=\sqrt{\frac1N\sum_{j=1}^N(f_j-g_j)^2},
\qquad
\operatorname{max}_{\rm sample}=\max_{1\le j\le N}|f_j-g_j|.
$$

They use all queries, including both sphere hemispheres, with equal weights.
They are discrepancies against the supplied reference, not automatically errors
against a true target. Even exact target values at queries would yield sample
errors, not exact continuum norms or uniform certificates. Nonuniform query
sets receive no quadrature correction. Static error scales cover every supplied
model/frame against the named reference. The viewer's error scale covers all
pairwise reference choices at every supplied frame/query; changing the reference
therefore does not silently change the scale. No historical campaign claim is
encoded in these displays.

## One reproducible core example

[example_compression.py](scripts/example_compression.py) connects `pde.compression_data.toy_data`
to the existing Dense, Legendre, Harmonic, and Taylor implementations in
`pde.compression`, then calls these visualization functions. It uses four
training directions, 96 query directions, width 64, hidden depth two, and just
three saved times through `0.04` in dimensions two and three. This is an
operational integration check, not an approximation experiment or certificate.
Its Harmonic source setup uses the documented tiny dense rollout; Taylor uses
the origin-jet mode. All inputs are generated by the maintained example.

From the repository root, choose an output directory that does not exist:

```sh
PYTHONPATH=code OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python -B code/scripts/example_compression.py --out data/established/compression_example
```

It writes circle and sphere PNG/PDF plots, offline HTML viewers, the supplied
arrays, and its own small reproduction manifest. Open either HTML file directly
in a browser; each is independent of its adjacent files. An analytic target can
also be supplied as another named array if desired, repeated explicitly across
frames when constant.

## Checks and limits

The tests check signed geometry, fixed scales, complementary hemispheres,
safe embedded JSON and the actual viewer control logic in Node with a
DOM/canvas stand-in. Node absence produces an explicit skip. This is
not a browser-layout or screenshot comparison. The small viewer has no
external resource dependency. See [reproduction commands](COMPRESSION.md).
