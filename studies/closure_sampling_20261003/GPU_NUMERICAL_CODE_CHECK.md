# Static numerical-code check

2026-10-03. Scoped review of the complete runner, sampler, and fixed protocol,
using the previously inspected maintained finite-network APIs and canonical
compression equations. No training or GPU experiment was launched by this
reviewer. Only this report was written. This is an implementation review,
not an independent review of the research theorem or a numerical-validity pass.

Inspected SHA-256 snapshots:

| File | SHA-256 |
| --- | --- |
| `gpu_sampling_experiment.py` | `2721dc8fb8f569ff6296267c4426c9ba153c49b0697734acf889867cce263bfc` |
| `neuron_sampling_setup.py` | `f3199851e30e267bab005b06ccf16f68f05b0307695d9d4cbca64aa2ddc28f02` |
| `GPU_SAMPLING_PROTOCOL.md` | `8dc345251e17eb35892e554d244c1b7bae26e1b287df66647f4c55bcaabbb8bb` |

## Findings

No blocking algebraic error was found in the inspected dense or weighted
training equations. The final runner was reread completely after the
coordinator's pre-campaign repairs. The equations and sampler are unchanged;
the partial-output and training-prediction repairs are present. The following
findings delimit this static review:

1. **Resolution validity is not decided by the runner.** Its `pilot` and
   `refine` modes emit ordinary trajectories. They do not compare time steps,
   floating-point precision, or angular/time panels; apply the joint 5%-of-
   dense-discrepancy and absolute `1e-4` thresholds; classify unresolved cases;
   or implement the single permitted time-step remedy. The coordinating task
   must perform and record those checks before drawing scientific conclusions.
   The coordinator reports that this external pilot comparison passed, with
   maximum solver discrepancy about `2.57e-5`, sampling-metric change about
   `9.6e-6`, and matched dense discrepancy about `.00787`; core discrepancies
   were about `1e-16`. These are coordinator-reported results, not artifacts
   independently inspected here. The new `--panel-offset` supports a nested
   doubled panel: size 514, offset 0 contains the original size-257,
   offset-.5 panel at odd indices. Keeping offset .5 at both sizes would not.

2. **The 20-minute global budget requires external coordination.** Each
   invocation starts its own deadline after imports and provenance. Independent
   pilot, worker, and refinement invocations do not share a campaign clock.
   The coordinator reports actively monitoring that global budget. Existing
   deadline/memory checks occur at observations and provide periodic guards.

3. **Partial-trace preservation is repaired.** The final runner creates the
   case directory before setup and saves `partial_observations.npz` when an
   exception interrupts the evolution loop. It retains all collected circle
   panels, training predictions, residuals, and feature motion. This covers the
   ordinary timeout/nonfinite failure path under the prescribed aligned times.

4. **Training-prediction archival is repaired; aggregate reporting is external.**
   Exact signed training prediction vectors are now saved alongside the circle
   panels. `scaled_sup` is recorded, while scaled RMS and endpoint errors must
   be derived downstream. The coordinator will derive those values and the
   protocol's cellwise medians, width-growth factors, and decision rules.
   Settlement currently uses
   the end-to-end prediction difference between the final time and ten units
   earlier, not the largest excursion among all observations in that interval;
   reports should state that definition precisely.

The original runner snapshot
`a0e7f6b70a0df915c15da6e4c971f87563419160eca0c44dedfac0d8a7f7b2d2`
was inspected first; its repaired archival findings were communicated before
the scientific campaign. A `.detach()` added to diagnostic comparisons removes
an autograd warning without changing the checked numerical quantities.

## Equations and independence

The runner's `Batch(A,M,w)` stores the dense mixer as `M=W`, and the reduced
mixer as `M=K=B diag(mu)^(-1)`. For normalized input rows `U`, positive first-
and second-population masses `mu,nu`, the reduced fields are

```
H = tanh(A U.T)
G = tanh(K diag(mu) H)
f = w.T diag(nu) G
```

With two equally weighted training examples, write `c=y-f` and
`delta=w[:,None]*(1-G^2)`. The implemented velocities are

```
A_dot = ((K.T diag(nu) delta) * (1-H^2) * c) U
K_dot = (delta*c) H.T
w_dot = G c
```

These are exactly the canonical weighted equations in the stated coordinates,
with the physical loss factor `2/m=1`. Uniform masses `1/n` and `K=nW`
recover the maintained dense flow. The two Heun stages update every parameter
block simultaneously. The nonorthogonal geometry uses the actual input matrix
in both forward evaluation and first-layer velocity.

`validate_core` contains substantive checks against the maintained public RHS
and complete Heun update, uniform-weight specialization, a nonuniform
rectangular autograd gradient oracle, and an array-only restart. The autograd
metric factors for `A,K,w` are respectively `mu`, `nu*mu`, and `nu`, which are
correct. These checks were inspected, not executed by this reviewer. They use
float64 even when the requested campaign dtype is float32; the separate pilot
precision comparison remains necessary if that fallback is selected.

Dense readouts start exactly at zero. The reference and independent control
use seeds `s` and `s+10000` and their own residuals. The reduced `fields`, RHS,
and Heun functions depend only on their state, masses, and fixed training data.
Zero-padded batched coordinates stay zero and do not influence active nodes.
Saved reduced restarts contain all of this model data and no dense arrays.

The sampler uses only initialization, labels, and fixed directions. Its
`w_dot`, first backward derivative, and second derivatives of the two hidden
features agree with differentiation at zero readout; the mixer second-
derivative contribution is included in factored form. No future state or
trained residual enters setup. Bases, approximate cubature, local Gram
whitening, and the weighted reverse action are mutually consistent. Exact
cubature/source matching is deliberately not claimed. Optimizer success flags,
discarded directions, mass conditioning, forward/reverse defects, and initial
Gram gaps are retained for inspection. Unsuccessful SLSQP statuses are recorded
but do not by themselves abort construction.

The setup witness still remains as a local variable during evolution, although
no reduced update consults it. Thus the reduced model is autonomous; the
current experiment's process memory nevertheless includes unused full-width
setup workspace in addition to its separately retained dense reference.

The practical sampler uses 16 initialized half-circle probe directions plus
the two training directions, derivative orders two forward and one backward,
basis rank at most eight, singular tolerance `1e-10`, and total prescribed
mass-floor fraction `.05`. Selected widths span 8 through 25. At selected
width eight the default basis rank is seven; otherwise it is at most eight.
The cubature feature lists therefore contain up to 29 or 37 constant/product
moments, fitted using only 8--25 positive masses. Approximate matching and
subsequent local Gram whitening are substantive heuristics. Their measured
source/Gram defects must accompany performance; they do not inherit the
exact-real theorem's approximation guarantee.

## Counts, controls, and schedules

For equal selected width `N`, the declared model count
`N^2+3N` moving plus `2N+6` fixed scalars is correct. The six fixed data scalars
are the two two-dimensional directions and two labels. Diagnostic selected
indices and the padded batched experiment are separate overheads. Integer
schedule arithmetic was checked without importing or running the experiment:

| Dense width | `(anchor,p)` order: `(128,1),(128,2),(256,1),(256,2),(512,1),(512,2)` |
| --- | --- |
| 512 | `N=8,8,13,13,20,20`; counts `110,110,240,240,506,506` |
| 1024 | `N=9,10,14,15,21,22`; counts `132,156,272,306,552,600` |
| 2048 | `N=10,11,15,17,22,25`; counts `156,182,306,380,600,756` |

Deduplication is correct. Each geometry worker has 18 cases, giving 36 across
the two prescribed angles. Default labels, seeds, time step, observation
cadence, and 120/240 horizon branch match the protocol. At time 120, any moving
model missing the training threshold extends the whole case to 240; the
frozen control does not trigger extension. All comparisons use shared times.

The frozen-hidden control is the exact readout flow for the initial training
Gram `G0`: its coefficient vector is
`G0^(-1)(I-exp(-t G0)) y`, evaluated through eigendecomposition and `expm1`.
Its query predictions use only the initial training-query feature Gram. This
is the intended mechanism control. The formula assumes a strictly positive
initial Gram eigenvalue; the tested random distinct-input configurations have
that property almost surely, and the eigenvalues are reported.

Primary maximum error, RMS of the angular time maxima, endpoint metrics, and
the matched independent-dense denominator are computed correctly. Initial zero
predictions and undefined correlations retain the maintained diagnostics'
conventions. Scientific claims remain finite-grid and finite-horizon claims;
none of the reviewed numerical code establishes an asymptotic exponent or the
theorem's exact-real construction.

## Empirical archive audit after completion

The scoped follow-up independently recomputed results directly with NumPy;
it did not import the analysis functions or rerun training. Inputs were the
complete `analyze_gpu_sampling.py`, all raw archives, records, source snapshots,
provenance, and status files under the five generated directories with prefix
`gpu_sampling_20261003_` and suffixes `main_orthogonal`,
`main_nonorthogonal`, `pilot_coarse`, `pilot_fine`, and `refine_2048`, together
with the `analysis` directory. Paths are relative to
`data/generated/closure_sampling_20261003/`. This section replaces the earlier
coordinator-only status of the numerical results above with direct checks.

All 78 observation/restart archives matched their record hashes. Every archived
source matched its provenance hash. Main and width-2048 refinement runs used
the runner hash in the first table; pilot runs used
`a625f78fb78f3329dadec7246c8312c51a4751563c7cfe9d1debbf72812bf668`.
A complete pilot-to-main source comparison confirmed only the previously
reviewed diagnostic/archival changes, with no flow or sampling change.

Additional checked SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| `analyze_gpu_sampling.py` | `5998f06ec3abc4be5af713a17480ca5f30ee2d3b966e1dc00f15719daddada4c` |
| `analysis/summary.json` | `719c0c25a6a07fb5c7810dfdcf0c3e2d357b51aaa29110e3a70cf8f4bf33fd4b` |
| `analysis/cell_summary.csv` | `b396bd7c27c16765c9a6d758152ffc97b5195381a6b0be7a2b7ffdef237a443a` |
| `analysis/width_scaling.png` | `acf843aafaaf67c52225b3b0b784bc48651701afcfdba902df700b0b3f90deb7` |
| Raw-archive manifest, defined below | `91498a5cb42c8e3b197eca0591ac6e486a85a650519df92724e3ba28a784149b` |

The manifest hash is SHA-256 of lexicographically sorted lines
`relative_path + "\t" + archive_sha256 + "\n"`, for all 78 `.npz` files,
with paths relative to `data/generated/closure_sampling_20261003/`.

### Primary quantities and fitting

The main archive contains exactly the prescribed 36 configurations and 216
schedule rows, representing 180 distinct reduced models after deduplication.
Predictions have axes `(saved time, model, query)`. The audit independently
subtracted model zero, maximized absolute error over time and query, computed
the angular RMS of each query's time maximum, and recomputed endpoint errors.
These quantities agree with all case records and `all_comparisons.csv`.
Paired ratios use that same case's independently initialized dense model,
never a ratio of medians or a different seed/width baseline.

Every model count was verified against actual restart array sizes, including
the six fixed training-data scalars, and against the maximal permitted integer
width in its budget. Reconstructing reduced final predictions from saved
`A,K,w,mu,nu` and the query directions agrees with recorded predictions within
`1.1102230246251565e-16`; training predictions agree within
`5.551115123125783e-17`. All archived arrays are finite. Recorded core checks
across the five invocations have maximum discrepancy
`1.1102230246251565e-16`.

All models fit and settle under the prescribed tests. The largest final
training residual RMS is `1.9869136761227874e-7`; the largest ten-unit prediction
change is `7.265397628519743e-7`. Checking the largest excursion over *all*
saved times in that last interval gives the same maximum, so the earlier
end-to-end wording distinction does not alter these settlement results.
Only `n2048_s7303_a60_sign+1` extended to time 240: its largest moving-model
residual at time 120 was `1.0488615261703633e-6`, correctly triggering the
whole-case branch. Its final residual was below `8.74e-12`. Other cases ended
at time 120. Both hidden feature layers moved in every moving model; the
smallest recorded final motion RMS across these models was approximately
`.02998` and `.03371`, respectively.

For anchor 512 and exponent two, the independently recomputed descriptive
aggregate over the 12 geometry/sign/seed cases at each width is:

| Dense width | Retained scalars | Median paired error ratio | Median absolute primary error |
| --- | ---: | ---: | ---: |
| 512 | 506 | 0.5551551942206495 | 0.007070046631761498 |
| 1024 | 600 | 1.5048344960059432 | 0.007204039863937424 |
| 2048 | 756 | 2.7485305717473265 | 0.0074992076088002384 |

These aggregates do not replace the protocol's decisions, which use medians
over three seeds in each separate geometry/sign/width cell. Every cell median
and min/max range in `cell_summary.csv` was independently reproduced. The six
resulting schedule decisions are:

| Anchor | Exponent | Largest cell median paired ratio | Largest scaled-error growth, 512 to 2048 | Decision |
| --- | ---: | ---: | ---: | --- |
| 128 | 1 | 25.5401813 | 1.53281874 | Disfavored tested witness |
| 128 | 2 | 17.4643734 | 1.36033105 | Disfavored tested witness |
| 256 | 1 | 9.73305056 | 2.71215633 | Disfavored tested witness |
| 256 | 2 | 7.16937259 | 1.93136402 | Disfavored tested witness |
| 512 | 1 | 6.63718951 | 2.28141809 | Disfavored tested witness |
| 512 | 2 | 6.52840182 | 2.04655327 | Disfavored tested witness |

Thus every tested schedule fails the competitive criterion; all also cross
the predeclared negative-discriminator threshold of a cell median ratio above
three. The conclusion concerns these six finite-budget heuristic samplers.
It provides no lower bound on an optimal logarithmic exponent, no exclusion
of other constants or constructions, and no refutation of the exact theorem.

### Numerical validity and figure

Matching actual saved query coordinates and physical times independently
gives the following resolution checks. The numerical threshold is the smaller
of `1e-4` and 5% of the matched dense discrepancy, as required.

| Check | Largest same-point prediction change | Largest primary-metric change | 5% dense threshold | Applied threshold |
| --- | ---: | ---: | ---: | ---: |
| Pilot, width 512 | `2.5704682616645158e-5` | `9.634316204501503e-6` | `3.9345351632910435e-4` | `1e-4` |
| Opposite-sign 60-degree seed 7301, width 2048 | `2.4823427724390834e-5` | `9.054169458344585e-6` | `1.467045298112394e-4` | `1e-4` |

Both pass. The pilot changes `dt=.2` to `.1`, observation spacing one to `.5`,
and 257 queries to 514; its actual fine offset is one, placing the original
coarse queries at even fine-panel indices with exactly identical stored
coordinates. Fine time indices are likewise even. The width-2048 check halves
the time step and retains identical observation times and query directions.
All runs use float64, one numerical CPU thread, and disabled TF32. No fallback
or further solver remedy was used. These are the prescribed sampled checks,
not error certificates for every scientific configuration or continuum query.

The plotting function was inspected completely and the PNG was viewed.
Its four panels group the intended geometry and label sign; lines use three-
seed cell medians of `sqrt(n)` times the primary maximum, and shaded bands use
the corresponding min/max over those same three seeds. The independent-dense
control's 72 stored control rows were checked against raw arrays, including
the frozen-control values. The figure displays anchor 512 only, with the two
exponents and both controls. It uses all saved times in each case, including
the one authorized extension, and exactly the 257 main-run circle directions.
The bands are descriptive ranges, not confidence intervals.

All 180 distinct sampler diagnostics report successful cubature optimizer
steps and no discarded selected-Gram numerical modes. This does not mean
source approximation was exact: basis truncation discarded 28--63 resolved
source directions; cubature Gram operator errors ranged from approximately
`.0300` to `.9347`, and initial training-Gram Frobenius errors ranged from
`.00121` to `.2546`. Minimum positive masses ranged from `.002` to `.02958`,
mass ratios from `15.75` to `168.73`, and reduced initial training-Gram gaps
from `.0310` to `.2362`. These diagnostics support interpreting the outcome
as evidence about this deliberately truncated numerical witness.

Both main statuses contain 18 completed cases and zero failures. Recorded
worker wall times are `66.5756` and `71.6522` seconds; each peaks at
`428752384` GPU-allocated bytes, well below 8 GiB. The separate width-2048
refinement took `12.2962` seconds. Process statuses do not independently
certify a shared launch timestamp, but the verified recorded work is far
inside the externally monitored 20-minute budget. No training was launched
during this empirical audit.
