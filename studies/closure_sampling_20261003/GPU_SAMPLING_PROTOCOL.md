# Bounded numerical test of practical neuron compression

2026-10-03. User-authorized GPU continuation of the same sampling study.
This protocol is fixed before inspecting training results. Two RTX 3090
devices have passed computation checks; the Miniconda Python has PyTorch
2.9.0+cu130. No maintained code or mathematical theorem is being changed.

## Decision question and hypotheses

Can a practical initialization-only truncation of the proved response-space
sampler match a realized dense network about as well as an independent
dense copy, using retained state budgets proportional to log(n) or log(n)^2?
H1 is that such small coordinated samplers already suffice at these widths.
H0 is that their response truncation/quadrature bias exceeds dense variability
or grows relative to it as n increases. Failure concerns this practical
witness, not an impossibility theorem or a refutation of the exact-real
construction. Three widths cannot identify an optimal asymptotic exponent.

## Canonical reference and tested configurations

Use the maintained `pde.finite_torch.NetworkEngine` initialization and
contraction conventions, with the readout explicitly set to zero.
The reference is the actual width-n, two-hidden-layer tanh network,
Gaussian read-in and mixer variances 1 and 1/n, no biases, mean squared
loss, and mobilities (n,1,n). All layers train in physical time.
Torch inputs are already normalized directions x/sqrt(2).

- Widths: 512, 1024, 2048.
- Input directions: (1,0) and (cos(angle),sin(angle)), angle 90 or 60 degrees.
- Fixed labels: (0.2,0.1) and (0.2,-0.1). This is a modest fixed numerical
  label scale, not a certified numerical value of the theorem's unspecified
  small-label threshold.
- Three predetermined seed pairs: reference seeds 7301, 7302, 7303;
  independent dense seeds 17301, 17302, 17303. The same seed numbers are used
  across widths/configurations; initializations of different widths are not
  assumed nested or independent when estimating trends.
- A preliminary numerical-validity run uses seed 6291 at width 512,
  angle 60 degrees and opposite signs. It is not a fourth scientific replicate.

There are 36 paired scientific configurations. Assign 90-degree cases to
GPU 0 and 60-degree cases to GPU 1. Each case runs both dense copies and
all distinct reduced models in batches, using the same physical step times.

## Practical sampler and retained state

The full proof uses potentially enormous initial derivative lists. The
experiment instead uses a bounded initialized dictionary: training and
16 fixed circle-probe responses, second-order hidden responses, and the
first nonzero backward responses, with paired W0/W0.T actions. No trained
snapshot, target trajectory, or future residual is an input to setup.

The implementation uses truncated source bases (rank at most 8), selected
original neurons, approximate positive moment matching, and a projected
mixer with a consistent weighted adjoint. A positive mass floor and any
discarded numerical modes are reported. Its source/Gram errors are measured.
These deliberate practical approximations mean the exact theorem does not
automatically certify this implementation.

For equal selected width N, count N^2+3N moving coordinates and 2N+6
fixed coordinates (two mass vectors, training directions, labels):
P=N^2+5N+6. No original full-width array is part of the reduced runtime.
Diagnostic archives and dense reference storage belong to the experiment,
not the proposed reduced model. The sampler may store the equivalent matrix
K=B diag(mu)^(-1), whose weighted forward and transpose operations remove
division by small masses; this has the same dimension and exact dynamics.

For each p in {1,2} and anchor S in {128,256,512}, impose

    budget(n) = S * (log(n)/log(512))^p.

Choose the largest integer N with N^2+5N+6 <= budget(n). Deduplicate
identical N within a case. These constants and exponents are not adjusted
after seeing errors. Report actual state counts rather than only log labels.

## Observables and matched controls

Use 257 equally spaced, half-cell-offset circle angles, distinct from setup
probes, plus exact training directions. Observe every physical unit of time.
The primary discrepancy is the largest absolute prediction difference over
all sampled times and the 257-angle panel. Also record the circle-RMS of
the pointwise-in-angle time maximum, endpoint-panel errors, training residuals,
feature motion in both layers, and sqrt(n) times every prediction error.

Matched baseline: independent dense copy versus the reference, at identical
width, data, solver settings, times, and query panel. Report each compressed
error divided by this dense-versus-dense discrepancy, not merely by 1/sqrt(n).

A frozen-hidden dense readout solution, computed from the original initialized
2x2 Gram and initial query features, supplies a cheap mechanism control.
It receives no trained features. If it matches the moving network as well as
the reduced model, the experiment cannot distinguish nonlinear representation
tracking from the small-label approximation on this observable.

## Discriminators and limits of inference

For a fixed state schedule, call performance competitive over this grid only
if its median compressed/dense discrepancy ratio is <=1.5 in every geometry,
sign and width cell, all fits/numerics pass, and its median sqrt(n)-scaled
error grows by no more than a factor 1.5 from width 512 to 2048 in each
geometry/sign case. Report all individual replicates, including failures.
A ratio above 3 or a growth factor above 2 is evidence against that specific
budgeted witness. Intermediate outcomes are inconclusive.

These are empirical discriminators, not confidence bounds, a time-continuum
supremum certificate, or a proof of a growth exponent. Do not fit or claim
an optimal p from only these three close logarithmic scales.

## Numerical validity, branches and stopping

Use simultaneous Heun, initially dt=0.2, through T=120. If any dense or
reduced trajectory has training residual RMS >1e-6, continue that whole case
on the same clock to at most T=240. No further fit-rescue or sampler tuning
is authorized by this protocol. Endpoint is called settled only if residual
RMS <=1e-6 and the last 10 physical units change predictions by <=1e-5.
Otherwise report finite-horizon data and unsettled models explicitly.

All scientific work uses float64 if the bounded validity timing supports it;
otherwise the predeclared fallback is float32 with TF32 disabled and a
float64 comparison on the pilot. Check dt versus dt/2 on the pilot and
the largest-width opposite-sign 60-degree seed-7301 case. Check the pilot
on doubled angular/time panels. Numerical differences must be <=5% of
the matched dense discrepancy and <=1e-4, or classify that case as unresolved.
The single permitted remedy is halving dt once; no iterative solver tuning.

Before the campaign, check the fast batched RHS/Heun against the maintained
public API at tiny width and check the weighted uniform-mass specialization.
Check a weighted loss directional derivative and own-state restart. All
states must remain finite. Report mass/Gram conditioning; do not silently
drop failed samplers or replace initializations.

Hard budget: two GPU workers, at most 20 minutes of campaign wall time,
at most 8 GiB GPU allocation per worker, one pilot, the 36 scientific cases,
and the stated resolution checks. If a resource limit is reached, retain
partial results and stop. Do not start a larger sweep. The implementation
may be repaired for genuine bugs before the scientific run, with source
hashes distinguishing any invalidated output.

## Provenance and outputs

Keep sources in this study and all outputs in fresh subdirectories of
`data/generated/closure_sampling_20261003/`. Record full configurations,
commands, source hashes, Python/Torch/CUDA/device metadata, dtype/thread
settings, seeds, timing, actual model counts, initial setup diagnostics,
raw prediction panels, fit/feature traces, and validity comparisons.
Each run refuses an existing output path. Preserve failed runs. The final
report and README will distinguish practical-sampler evidence, exact-theorem
scope, and unresolved asymptotic questions. No Git or shared-code writes.
