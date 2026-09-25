# Autonomous response moments: construction and numerical results

Status: internally checked construction, conditional theorem, and finite
numerical evidence. No promotion or unconditional population theorem.

The response-moment closure approximated the dense learned function on all
five tested configurations. Error decreased at each tested increase P=1,3,7.
On the original hardest case the circle RMS was 0.2363,0.0730,0.00466, compared
with 0.7564 for the previous derivative dictionary at 72 vectors. At P=3 the new
history has 48 vectors. These methods retain different fixed information:
the response-moment model retains W0, while the previous dictionaries replace
the entire middle matrix. This is evidence for compressing the evolving
correction, not a matched-total-storage superiority result.

## Construction and proof status

MOMENT_CONSTRUCTION.md gives the complete autonomous F,K,Q,E in the agreed
m1,m2 notation. The current moments describe the full response history in
accumulated learning activity. Their triangular ODE coefficients are derived
by differentiating the moving-interval integrals. The first P coefficients
are exact moments of the surrogate's evolving responses; only reconstructing
the history cross product from these coefficients is approximate.

An exact tanh response lift makes the ODE rational, initialized on the actual
tanh manifold. Integration by parts supplies equivalent weighted derivative-
moment coordinates. Thus no nonzero Taylor radius, freely trained basis,
external trajectory fit or arbitrary damping law is assumed. Both W0 and its
transpose remain actual coupled operators. Learned interactions use current
population contractions of response moments. All updates vanish at zero
residual; the RMS lift uses a separately defined stationary extension there.

The single middle-matrix defect is a product of two endpoint projection
errors. It vanishes exactly at initialization for every random realization.
Under uniform finite total activity, activity-Lipschitz forward histories and
bounded variation of the normalized backward source (including its initial
prefix jump), the relative defect is bounded by a constant/sqrt(2P-1).
This is a mathematical conditional bound, not an empirical fitted rate.

With a common bounded forward region, uniform gradient loss decay, bounded
velocity per residual and the required perturbation/stability controls, the
small-defect estimate yields uniform-in-time convergence by finite-time
perturbation plus uniform tail control. None of these global hypotheses has
been proved from input compatibility alone. Width-uniform constants and the
population limit remain open. The detailed proof and independent audit are
RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md and MOMENT_INDEPENDENT_CHECK.md.

## Experimental design

The network is the same bias-free two-hidden-layer tanh model at n=2048,
NumPy seed20260920, with original unhalved mean-square loss and gradient-flow
mobilities(n,1,n). No Adam, SGD, initialization rescaling or label scaling.
Every run's three initialized weight arrays match the selected original dense
archive bitwise. Outer-layer dynamics are canonical; the derived middle-layer
defect is the sole physical change.

The first two cases were two_outliers_alternating and quadrant_alternating.
The initial protocol allowed quadrant_pairs after their validation. The
user then explicitly requested additional hard original tasks. The next two,
quadrant_center_edges and equal_mixed_odd, were selected by the larger prior
error of derivative 38 and old 45 dictionaries. This is a deliberate historical
stress test, not an unbiased statistical sample. No rotations, fresh seeds
or negative control were added.

Each original case has 8 equal-weight training samples. For equal_mixed_odd,
opposite-label antipodal pairs were combined into 4 representatives. The
bias-free odd network has exactly the same empirical loss and gradient under
this quotient; the archived trigonometric roundoff discrepancy was checked.
The current closure also preserves this duplication identity. Its actual
state count uses 4 samples. All represented inputs are pairwise nonparallel
and non-antiparallel.

Each trajectory stops at its own first training-MSE 0.001 crossing. RMS means
predicted-function discrepancy from the dense network over 8192 equally spaced
circle angles, with a nested 4096-grid check. There is no imposed full-circle
label function, so these are approximation errors rather than generalization
errors against test labels. Common-time 2048-node snapshots give additional
trajectory comparisons; they are not continuous-time supremum certificates.

Float64 adaptive Heun used both GPUs. The primary and refined tolerances were
6.25e-5 and1.5625e-5, atols 100 times smaller; four cases received an additional
3.90625e-6 level after the initial drift checks. The original six primary
runs failed the sampled activation-drift gate and remain recorded. Selected
refinements pass the activation, physical-loss, prediction-refinement and grid
gates. The final campaign has 34 closure trajectories and 8 newly refined dense
references, within the prospective 44-trajectory/3600-GPU-second cap. Recorded wall time
sums to 981.37 seconds; counted integration time is 973.36 seconds.

## Comparison to the frozen historical target

These errors retain the original selected dense references, so they can be
compared directly to frozen historical baseline scores and the main plot.
Orders in different methods do not mean equal sizes.

| Configuration | P=1 | P=3 | P=7 |
|---|---:|---:|---:|
| Two outliers, alternating | 0.236313 | 0.0729531 | 0.00466307 |
| Quadrant, alternating | 0.341407 | 0.0456972 | 0.00164765 |
| Quadrant, paired labels | 0.0192803 | 0.00281547 | 0.000120383 |
| Quadrant, center/edges | 0.0456043 | 0.00487212 | 0.00130221 |
| Equal mixed labels | 0.0123936 | 0.000520130 | 0.00000938810 |

For 8 represented samples the history-vector counts are 16,48,112 and the
learned-matrix rank bounds are 8,24,56. For the 4-sample quotient they are 8,24,56
vectors and 4,12,28 rank. These are response-history factors, not optimized
frozen-dictionary coefficients.

A representative comparison near the 48-vector middle budget, using the same
archived targets, is:

| Configuration | Response moments48 | Derivative38 | Old dictionary45 | Gaussian45 | Orthogonal45 |
|---|---:|---:|---:|---:|---:|
| Two outliers, alternating | 0.07295 | 0.86829 | 0.54976 | 1.37927 | 1.30283 |
| Quadrant, alternating | 0.04570 | 0.12068 | 1.28883 | 2.46188 | 2.48105 |
| Quadrant, paired labels | 0.002815 | 0.104996 | 0.165388 | 0.550726 | 0.599156 |
| Quadrant, center/edges | 0.004872 | 0.127471 | 0.471448 | 0.512078 | 0.502740 |

The equal-mixed quotient already gives 0.01239 with 8 history vectors, versus
old 8=0.10464, Gaussian 8=0.17246, orthogonal 8=0.17392 and derivative 6=0.38078.
Again, these counts do not match total fixed storage because W0 is retained.

## Fresh dense reference validation

The new errors reached the numerical sensitivity of four archived targets.
The predeclared branch therefore reran canonical dense flow at 1.5625e-5 and
3.90625e-6. These comparisons are kept separate from historical-baseline
comparisons; historical errors were not silently transferred to new targets.

| Configuration | P=1 vs fresh target | P=3 vs fresh target | P=7 vs fresh target | Dense level1/2 RMS change |
|---|---:|---:|---:|---:|
| Quadrant, alternating | 0.341318 | 0.0456113 | 0.00155234 | 0.0000744304 |
| Quadrant, paired labels | 0.0192813 | 0.00281761 | 0.000118502 | 0.0000626933 |
| Quadrant, center/edges | 0.0455816 | 0.00487776 | 0.00130764 | 0.0000127927 |
| Equal mixed labels | 0.0123995 | 0.000525665 | 0.00000370787 | 0.000000321361 |

Every order trend survives the fresh references. The smallest digits are not
all numerically resolved: paired-label P7 is comparable to dense-refinement
sensitivity, and equal-mixed P7 is below its own closure primary/refined RMS
change (8.59e-6). These rows support errors on roughly 1e-4 and 1e-5 scales,
respectively, rather than precision claims at every printed digit. The
refinement differences are empirical sensitivities, not certified bounds.

## State cost and limits

For the 8-sample cases actual moving state counts are 71,683 / 137,221 / 268,297
for P=1/3/7, including lifted responses and redundant implementation coordinates.
The exact physical dense network has 4,200,448 moving scalars. The moment
model also retains 4,194,304 fixed W0 entries. Consequently this reduces the
description of the learned correction; it does not reduce total storage below
a dense implementation that stores only its current matrix.

The moving-state count grows linearly with the number of represented samples.
Input dimension 2 alone has not removed that dependence. No width trend,
universal statistical claim, training-to-infinite-time empirical certificate
or asymptotic observed rate is established by these runs.

## Artifacts and validation

- Protocol: MOMENT_EXPERIMENT_PROTOCOL.md, including the prospectively frozen
  user-authorized extension and reference-refinement branch.
- Inputs: HARD_BENCHMARK_INPUTS.md and ADDITIONAL_BENCHMARK_INPUTS.md.
- Engines: moment_engine.py and orthogonal_moment_engine.py; rational RHS,
  factorized learned actions, and exact defect diagnostics.
- Reproducers: run_moment_experiment.py, its frozen initial version, and
  refine_dense_reference.py. Each run records source hashes.
- Numerical selection and plots:
  data/generated/neural_response_memory_20260922/analysis01/metrics.json,
  summary.md, rms_vs_vectors, fresh_reference_rms, loss_vs_time,
  endpoint_functions and matched_time_rms(PNG/PDF pairs).
- Independent check: MOMENT_INDEPENDENT_CHECK.md. It verifies algebra,
  canonical normalization, initialization, saved full-circle predictions,
  physical loss, quotient equivalence, references and refinement gates.

Both engines passed 11 CPU identity tests, including the exact initial dense
velocity, moment transport, shared transpose, reconstruction derivative,
rational lift and zero-residual behavior. No maintained docs/code or Git
index was changed; unrelated concurrent edits were preserved.
