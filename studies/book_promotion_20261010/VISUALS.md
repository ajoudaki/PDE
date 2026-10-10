# Array-based prediction views

For the original **multi-experiment interactive radial explorer**, including
time/loss alignment and width/seed selection, see [RADIAL.md](RADIAL.md).
The functions below provide static plots and simpler array-preview viewers.

`visual_core.py` supplies radial circle plots, sphere prediction/error plots,
and standalone HTML viewers. It consumes supplied arrays and performs no model
evaluation, training, archive loading, or experiment selection. The module
imports NumPy; static plots additionally need Matplotlib. Generated viewers
need only a browser and work from a local file without servers, CDNs, or external
libraries. This is study-owned support, not promoted plotting infrastructure.

## Inputs and small interface

Let $N$ be query count and $T$ saved frame count. `queries` is a finite array
of shape `(N,2)` for the circle or `(N,3)` for the sphere, with unit rows.
These directions are the normalized model inputs $v=x/\sqrt d$ used by
`compression_core.py`; no further normalization is applied. `predictions`
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
file, so callers should choose a study-owned output location.

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

The study's [support_example.py](support_example.py) connects `data_core.toy_data`
to the existing Dense, Legendre, Harmonic, and Taylor implementations in
`compression_core.py`, then calls these visualization functions. It uses four
training directions, 96 query directions, width 64, hidden depth two, and just
three saved times through `0.04` in dimensions two and three. This is an
operational integration check, not an approximation experiment or certificate.
Its Harmonic source setup uses the documented tiny dense rollout; Taylor uses
the origin-jet mode. No paper figure driver is imported.

From the repository root, choose an output directory that does not exist:

```bash
PYTHONPATH=code:studies/book_promotion_20261010 MPLCONFIGDIR=/tmp/pde-matplotlib OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python studies/book_promotion_20261010/support_example.py --out data/generated/book_promotion_20261010/visual_support/example01
```

It writes circle and sphere PNG/PDF plots, offline HTML viewers, the supplied
arrays, and its own small reproduction manifest. Open either HTML file directly
in a browser; each is independent of its adjacent files. An analytic target can
also be supplied as another named array if desired, repeated explicitly across
frames when constant.

## Source scope and provenance

The implementation is a small rewrite of the reusable encoding contracts,
not a copy of the paper renderers or embedded archived runs. The inspected
source functions were `paper/scripts/figures.py::polar_xy`,
`draw_circle_panel`, `sphere_color`, `sphere_camera`, `SphereSurface`
(`__init__`, `locate`, `texture_coordinates`), `SphereDrawing`,
`visible_segments`, `draw_globe`, and `draw_colorbar`. The source uses fixed
archived grids and a barycentrically interpolated sphere surface; this module
uses arbitrary supplied unit queries and deliberately displays sphere samples
directly. Circle signed offsets, zero labels, complementary hemispheres, common
scales, and statistics before display conversion are retained. The source
README's circle/sphere contract sections and `paper/interactive/README.md`
informed the offline time/model controls; no historical HTML data or inlined D3
was copied. Required notation instructions and `docs/notation.qmd` govern the
input and residual conventions.

SHA-256 hashes of the consulted source files at implementation time:

| Path | SHA-256 |
|---|---|
| `paper/scripts/figures.py` | `2c6e6385fd4add52ae3af2c589bf7f291914aaab6e4eb71a4047f8a484704c0a` |
| `paper/scripts/README.md` | `fab5bdb4b5e6f38c65332958bb118dc67dc156aa64b6bc748c07f91721eede21` |
| `paper/interactive/README.md` | `805e899fb9641043d3ff891fe7bbeaa206364c64c4134d7d66712128e10efd2c` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `studies/book_promotion_20261010/compression_core.py` | `770ceab1dc5917eb14759071002d824ae45feaabfc85be1e7f228945d3cdb3a6` |

These are source snapshots, not a request to import or read those files at
runtime. The example records hashes of the actual local support modules it uses.

## Bounded checks

```bash
PYTHONPATH=studies/book_promotion_20261010 MPLCONFIGDIR=/tmp/pde-matplotlib /home/amir/miniconda3/bin/python -m unittest discover -s studies/book_promotion_20261010 -p test_visual_core.py -v
```

Seven tests check negative/zero/positive radial geometry, no radial folding,
sphere camera signs and complementary masks, shape/time/reference rejection,
scales shared across models and frames, signed sphere differences, compact
colorbar ticks, escaped HTML labels, and executable viewer control updates.
The last test runs the actual embedded JavaScript in Node with a small
DOM/canvas stub, changes model/reference/frame for both geometries, verifies
updated sample metrics and redraw calls, and exercises play/pause. Node absence
causes that test to skip explicitly. This validates the control logic rather
than browser typography; representative PNGs are also inspected separately.
