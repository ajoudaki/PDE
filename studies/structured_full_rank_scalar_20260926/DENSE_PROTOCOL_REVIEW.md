# Dense initialization comparison: protocol review

2026-09-26. Scoped design review only; no experiment was run by this author.
This is a continuation of the present study under new empirical authorization.
It compares fully trainable dense networks; the fixed-`P` theorem is not being
used as a dense-training accuracy theorem. Recommendations below should be
frozen in the runner configuration before scientific runs.

## Decision and model controls

The empirical question is whether inexpensive full-rank **initializations**
produce circle test RMS comparable to independent Gaussian initialization,
after the same dense dynamics have been applied. It is not whether the
initial operators have the same law, or whether a structured parameterization
can train as well while preserving its structure.

Use the same two-hidden-layer, bias-free tanh architecture, output
`f=c^T h2/n`, unhalved training MSE, and original clock as the study model.
The corresponding dense gradient flow is

    wdot = -2/m sum_a r_a delta1_a u_a^T
    Wdot = -2/(m n) sum_a r_a delta2_a h1_a^T
    cdot = -2/m sum_a r_a h2_a.

Thus the gradient mobilities in the order `(w,W,c)` are `(n,1,n)`.
Every entry of `W` is trainable after initialization. Do not reorthogonalize,
reapply a Hadamard factorization, project onto the initial structured family,
or substitute the response-memory ODE. Use one dense RHS implementation for
all seven methods after their initialization matrices have been materialized.

Within each task/width/seed, share exactly the Gaussian first weights and
stored readout `c_i=g_i/n` across methods. Independently initialize two
Gaussian middle matrices `G1,G2`, each with iid `N(0,1/n)` entries. Use separate
recorded random streams for each candidate's signs, Gaussian diagonal, and
permutation. The Gaussian replicate is a middle-initialization baseline with
outer randomness held fixed, not a fully independent network replicate.

Freeze the precise multiplication order and normalization of `HD`, `HDHD`,
and the Gaussian-diagonal/Fastfood candidate. For normalized `H`, sign-only
products have Frobenius norm squared exactly `n`; iid Gaussian and a standard
Gaussian diagonal between orthogonal factors have expected value `n`.
Do not normalize each Gaussian realization to exact Frobenius norm unless
that is a separately named control: it changes the Gaussian law. A diagonal
Gaussian factor yields a different singular-value law from iid Gaussian;
that is an intended candidate difference, not a numerical defect.
For reflection rank four, choose four distinct Walsh columns. Share its
endpoint signs with the signed-diagonal control to isolate the four modes.

## Twelve target/geometry cases

Root's proposed twelve-case suite is appropriate. Every target must satisfy
`g(theta+pi)=-g(theta)`; even harmonics or an offset are incompatible with the
bias-free architecture. Keep teachers at their declared native amplitudes,
including cosine extrema `+/-1`, and report errors divided by each teacher's
circle RMS. The RMS normalizer is determined by the teacher, never fitted
from the trained predictors or sparse training labels.

The following table fixes the structure and identifies remaining configuration
choices. Angles are radians unless a factor of `pi` is shown.

| Case | Teacher | Training angles / purpose |
|---|---|---|
| `pair_cos1` | `cos(theta)` | `0,0.9`; smooth sparse interpolation |
| `pair_cos3` | `cos(3 theta)` | `0,pi/3`; opposite labels without antipodal inputs |
| `nearpair_sin9` | `sin(9 theta)` | `-pi/18,+pi/18`; nearby opposite labels |
| `triple_book_cos3` | `cos(3 theta)` | `0,-pi/5,+pi/5`; symmetric sparse case supplied by root |
| `triple_asym_mix` | fixed odd-harmonic mixture | `0.13,1.02,2.41`; asymmetric sparse case |
| `cluster_triple_cos9` | `cos(9 theta)` | `-pi/9,0,+pi/9`; clustered alternating labels |
| `broad_ridge6` | fixed broad odd ridge | six irregular half-circle angles |
| `sharp_ridge8` | fixed sharp odd ridge | eight angles including both sides of its transition |
| `alternating_cos3_6` | `cos(3 theta)` | `j pi/3`, `j=0,...,5` |
| `alternating_cos5_10` | `cos(5 theta)` | `j pi/5`, `j=0,...,9` |
| `alternating_cos9_18` | `cos(9 theta)` | `j pi/9`, `j=0,...,17` |
| `multiscale12` | fixed odd-harmonic mixture | twelve irregular angles |

The mixture coefficients, ridge slopes/orientations, and every remaining angle
must be explicitly frozen before the pilot. If root has not selected these,
one admissible concrete choice is:

    mixture(theta) = cos(theta)+0.5 sin(3 theta)+0.25 cos(5 theta)
    multiscale(theta) = cos(theta)+0.5 sin(3 theta)+0.25 cos(9 theta)
    broad(theta) = tanh(1.5 cos(theta-0.37))
    sharp(theta) = tanh(6 sin(theta-0.41))
    broad_angles = [0.07,0.43,0.94,1.41,2.13,2.77]
    sharp_angles = [0.03,0.24,0.39,0.43,0.61,1.34,2.17,2.94]
    multiscale_angles = [0.04,0.21,0.46,0.69,0.93,1.19,
                        1.42,1.67,1.91,2.18,2.49,2.86].

These suggestions are choices to freeze, not a second suite to search after
seeing results. All cosine/sine frequencies above are odd, and
`tanh(k cos(theta-phi))` and `tanh(k sin(theta-phi))` are odd under an antipodal
shift. Uniform teacher RMS is `1/sqrt(2)` for a single sine or cosine;
a sum of distinct harmonics has squared RMS equal to half the sum of squared
coefficients. Compute ridge normalizers once on a much finer frozen circle
quadrature, with a doubling check.

**Antipodal redundancy.** The full-circle peak grids in the three alternating
cases contain exact duplicate information: for odd `k`, point `j+k` is
antipodal to point `j`, with the negative label. Every admissible predictor
is odd. Its residual and parameter derivative both change sign, so the two
per-point loss gradients are identical. Averaging over all `2k` points is
therefore exactly equivalent to averaging over the first `k` points. Report
both nominal and effective sample counts. This is an unusually useful
correctness control; it must not be described as `2k` independent constraints.
Retaining the full grids is acceptable, although folding them in half saves
work without changing the dynamics.

## Primary metrics and decision rules

For teacher RMS `R_g>0`, report normalized circle test error

    E = sqrt(mean_grid (f(theta)-g(theta))^2) / R_g.

Retain the unnormalized values as well. The primary paired quantity is each
candidate's `E-E_G1`, at the same endpoint definition. Also report:

- Gaussian replicate difference `E_G2-E_G1`;
- circle function distance `RMS(f_candidate-f_G1)/R_g` and the analogous
  `RMS(f_G2-f_G1)/R_g`;
- training loss, fraction reaching each training threshold, first-hit physical
  times, final physical time, numerical-validity status, and budget censoring.

A small difference in target RMS does not imply similar functions; the two
function-distance diagnostics prevent that conflation. Gaussian replicate
variation is context for practical equivalence, not permission to inflate a
margin after seeing a disappointing candidate.

Root's proposed preregistered practical closeness margin is defensible:

    absolute_RMS_margin = 0.02 R_g + 0.05 mean_seed(RMS_G1),

with a separate one-sided noninferiority allowance `0.10 R_g`. Keep these
claims distinct: a candidate can be not worse without being close, and can
be much better while failing two-sided closeness. For uncertainty summaries,
resample paired seed blocks and recompute the Gaussian-dependent margin in
each resample; do not pretend its estimated Gaussian term is a fixed known
number. Twelve seeds support useful screening, but not an assertion of
universal equivalence over task families. Publish all paired seed values.

Report each task and width. An equally weighted aggregate across the frozen
24 task/width strata is a secondary summary; it cannot conceal a failing
clustered or alternating case. Any confidence intervals should be explicitly
identified as descriptive unless a simultaneous inference procedure was
preregistered. A wide interval crossing the chosen margin is inconclusive,
not evidence of sameness.

## Endpoint and common-clock comparisons

Integrating every run to physical `T=300` permits a genuine common-clock
comparison. Save the first accepted-step snapshots meeting MSE `1e-6` and
`1e-8` when attained, but continue to the common horizon. Report threshold
endpoints separately from fixed-time outputs. Freezing a stopped predictor
and labeling it an output at later physical time would invalidate the
common-clock comparison.

Training MSE `1e-6` does not by itself bound future change in circle output.
Measure `RMS(f_at_1e-8-f_at_1e-6)` and its teacher-normalized value whenever
both thresholds are reached; likewise measure drift from the threshold
snapshot to the common horizon. These are empirical endpoint-sensitivity
checks, not a theorem derived from small training loss.

For matched-threshold comparisons, report the paired convergence mask and
how many candidate/Gaussian pairs are missing an endpoint. Never silently
compare only an easier subset of candidate seeds. Fixed-time results include
all numerically valid runs, whether they trained successfully or not.

At `T=300`, conditionally extend hard cases according to a rule frozen before
runs. To compare common extended times, extend all methods in the selected
(task,width,seed) block, including methods that had already fitted. A suitable
trigger is that any method in that block has not reached `1e-6`; extend the
whole block to `1500`, then optionally to the declared final cap. If the wall
budget prevents this, mark incomplete blocks as budget-censored and retain
the complete `T=300` comparison. Do not give favored candidates extra time
through a post hoc choice of which individual runs to extend.

## Numerical validity gates

Use float64 and one explicit dense RHS for all methods. Before the scientific
runs, require these small-width checks:

1. Dense materialized structured products agree with their factored forward
   and transpose actions to relative error below `1e-12` on test vectors;
   normalized Hadamard factors satisfy `H^T H=I` to that tolerance.
2. A separately derived gradient or central directional finite difference
   matches the dense loss gradient for each parameter block. Test a few
   perturbation sizes and non-saturated parameters; require agreement near
   `1e-6` relative, with an absolute tolerance for near-zero components.
   Compare the RHS with the gradient after applying mobilities `(n,1,n)`.
3. Check `f(-u)=-f(u)` to floating-point accuracy, the loss-gradient energy
   identity `dL/dt=-(n||grad_w L||^2+||grad_W L||^2+n||grad_c L||^2)`, and
   full versus antipodally folded alternating datasets. The latter must give
   the same RHS and trajectory to rounding tolerance.
4. Verify that off-family entries of `W` change after an update and that no
   structured projection is present. Initialization alone is structured.

For Heun with proposed `dt=0.05`, the pilot should decide numerical resolution
only. Preselect its task/seed/method blocks, covering a sparse easy case and
at least the clustered alternating and highest-frequency cases at width256.
Compare `dt` and `dt/2` at identical physical times. A practical gate is
circle **function** discrepancy below `0.002 R_g` and test-RMS discrepancy
below `0.001 R_g`; these are much smaller than the practical closeness margin.
Any material loss increase, nonfinite quantity, failed refinement gate, or
unstable convergence classification requires a smaller frozen step before
scientific runs. Endpoint threshold-time variation is also reported; if an
endpoint exists on only one resolution, its convergence classification is
not numerically certified. Resolve failing cases uniformly by predeclared
rules, not method-specific manual tuning.

Evaluate circle errors on2048 and4096 equispaced points without a duplicate
endpoint. Require their RMS estimates to differ by at most `0.0005 R_g`;
otherwise double again under the predeclared numerical branch or mark the
metric unresolved. When comparing two predicted functions, use exactly the
same evaluation angles and quadrature. The test grid is evaluation only and
must not influence training, early stopping, candidate selection, or labels.

## Budget, provenance, and stopping

The planned `12 tasks x 2 widths x 12 seeds x 7 methods` is2016 scientific
runs before refinements/extensions. At `T=300,dt=0.05`, it requires about
12.1million Heun steps or24.2million RHS evaluations. If the nominal training
sample counts sum to about85 over the12 tasks, the three leading dense
matrix products cost approximately42TFLOP in total, before overhead.
This is arithmetic accounting, not a measured runtime prediction. Forty-eight
wall-clock minutes with eight workers may suffice, but it is not guaranteed;
`T=1500/3000` extensions multiply work in selected blocks by factors5/10.
Avoid BLAS oversubscription: freeze worker count and per-worker BLAS thread
count, and measure pilot throughput before committing the complete schedule.

Freeze deterministic block ordering and extension priority so a wall-time cap
does not preferentially remove slow methods. Reserve time for saving raw
results and summary generation. The hard terminal stop applies even when
scientific results are inconclusive. Record every unstarted, failed,
nonconverged, or budget-censored run rather than removing it from denominators.

Preserve exact task arrays and teachers, seeds and random-stream mapping,
method formulas, source hash, precision, solver/step, environment/thread
settings, actual physical endpoint, threshold snapshots, circle predictions,
training metrics, and all validation flags. Any post-pilot code change requires
rerunning the affected correctness check. No empirical outcome from this
protocol proves the scalar theorem, Gaussian universality, or a no-go claim.
