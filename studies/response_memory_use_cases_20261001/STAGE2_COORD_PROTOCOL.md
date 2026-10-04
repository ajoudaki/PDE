# Stage 2 coordination: frozen protocol before scientific execution

This route extends the user-reopened temporal-coordination question. Its adverse
prior evidence is retained: centered-history deletion failed the original circle
threshold and q1 beat higher-order corrupted-write repair. New real domains and
exact full-marginal controls test a different, explicitly declared discriminator;
they do not overturn those results by definition.

## Object, hypothesis, and domains

Observe canonical dense two-hidden-layer tanh Euler training, Gaussian hidden
initialization, zero readout, mobilities (n,1,n), unhalved MSE, no normalization.
Use root-prepared Fashion-MNIST 0 versus 6, California housing bounded regression,
and UCI-HAR moving versus stationary. Root records source/split preprocessing.
Inputs are already unit-norm API rows. Use the first 512 training rows in the
provided deterministic split; all provided validation/test rows are held out.
No labels from these sets select an edit, training horizon, sign, or permutation.

The exact observer stores h^(1) and b=r delta^(2) before each equal physical-time
step. Full-trajectory reversal is the primary marginal-preserving intervention:
replace each b_i partner by b_(N-1-i), then add the resulting increment difference
to the endpoint hidden matrix. This preserves the complete separate empirical
histories, their means, all unpaired moments, and cross-sample backward snapshots.
A simultaneous reversal is the exact zero-effect control. Physical time replaces
the old activity observer; no autonomous-closure theorem is claimed.

H1: chronological feature/credit pairing has functionally relevant directional
information beyond means, edit size, singular spectrum, both edit Grams, and the
linear current-gradient loss term. H0: effects are small or are explained by
these nuisance controls. An endpoint experiment identifies only the effect of
this declared weight intervention, not an ordinary-GD retraining counterfactual.

## Fixed interventions and controls

At each frozen endpoint record:

- No edit and exact reconstruction/parity.
- Full reversal; two fixed seeded random time permutations; reversal separately
  in the first, middle and final thirds of training (fixed before data).
- Mean-only q1 increment replacing the full increment, and physical-time
  Legendre q4/q8/q16/q32 observer replacements. These use exact interval integrals.
- For the full-reversal edit: five independent singular-mode sign scramblings,
  preserving E E^T and E^T E exactly; five independent random left/right rotations
  with identical singular values; and its negative (same Grams).
- Hidden current-gradient ascent and descent, each exactly norm-matched to the
  reversal edit. No line search and no held-out-label selection are used.
- Simultaneous-reversal control; explicit marginal and Gram invariant checks.

Primary measurements are held-out MSE change relative to the untouched endpoint,
held-out prediction RMS change, and the full-reversal excess damage over the
median of five Gram-preserving sign controls. Report validation/train/test
separately. Accuracy is secondary for classifications. Save the current hidden
loss-gradient projection and exact remainder for each edit on training data.
Report first-layer feature relative motion and mean squared tanh nonlinearity.
Fixed third-window reversals diagnose temporal localization; no winning window
is selected as a replacement primary.

An empirical positive coordination result requires, separately in at least two
of the three domains, all four fresh seeds to show positive full-reversal damage,
median relative MSE damage >=10%, median excess over sign controls >=5% of base
MSE, and median nonlinear training-loss remainder at least half of the absolute
training-loss change. The latter rejects an explanation solely by the ordinary
linear gradient projection; it does not make higher-order curvature novel.
Current-gradient ascent/descent and isotropic controls remain mandatory even if
these thresholds pass. A stronger mechanistic interpretation requires explaining
any comparable current-gradient damage; it is not granted by threshold crossing.
Threshold misses reject this registered cross-domain directional claim. Failed
numerical or feature-motion gates make the corresponding domain inconclusive.

## Pilot, confirmation, numerical and width checks

Pilot seed 3101 on all three domains, n=256, T=32, eta=1/16. These are excluded
from confirmation. Hyperparameters and scientific interventions stay fixed.
If pilot numerical divergence occurs, halve eta globally once before confirmation,
recording the cause; do not change T, data, labels, n, or thresholds. Finite but
poor fitting is reported, not used to select an extended horizon.

Confirmation seeds 3201,3202,3203,3204 on all three domains, same settings.
Regardless of positive/negative outcome, repeat seed 3201 on all three domains
with eta halved, and seed 3202 at n=512 as a width stress. Base/refined prediction
RMS discrepancy must be <=0.02 and relevant effect must exceed twice its
step-refinement change. Report width stress without pretending it is a theorem.

All main operations use float64, one CPU thread, TF32 off, GPU1. Exact update
parity, means, simultaneous-permutation, same-spectrum and same-Gram controls
must have relative errors <=1e-9. Nonfinite values invalidate a case. Relative
first-layer feature motion >=0.03 and tanh nonlinearity RMS relative to its
preactivation >=0.05 are required to call the experiment nonlazy/nonlinear.
These gates do not require fitting; empirical losses remain reported.

## Continued training and reachable optimizer branch

Each main confirmation endpoint receives five fixed T=4 ordinary continuation
solves: no edit, q1, full reversal, the first Gram-preserving sign control, and
norm-matched gradient descent. All receive the identical budget and source labels.
This tests persistence versus immediate perturbation sensitivity. It does not
restore historical marginal equality during the continuations.

After endpoint confirmation, regardless of sign, run one independent seed 3301
per domain for five causal training arms: ordinary dense; mean-only block write;
block-reversal write; Gram-preserving sign control for the reversal edit; and
norm-matched current-gradient descent. A causal arm trains normally for each
fixed block T=8, observes that block, applies its declared edit, then proceeds
for four blocks total T=32. At a boundary it uses only already observed training
history. These are reachable trajectories of explicitly changed optimizers;
none is ordinary GD with fixed global trajectory marginals. No held-out target
chooses the operation. One seed/domain makes this branch a stress/feasibility
check, not independently confirmed optimizer superiority.

## Source checks, budget, and terminal rule

Before scientific execution, independently test dense velocities against autograd,
all three block mobilities, source Flow one-step parity, direct discrete increment,
zero-activity handling, permutation means/second moments, exact permutation
expectation and variance by finite enumeration, sign-Gram invariance, and Legendre
interval quadrature. Preserve code and configuration hashes and source snapshots.

Total planned scientific solves: 3 pilots +12 confirmations +3 step refinements
+3 width stresses +60 short continuations +15 causal arms =96, within100fits.
Counting every short continuation as one solve is deliberately conservative.
Stop at75 GPU-process minutes,100fits, or completion, whichever occurs first.
Deterministic tiny oracle tests are logged separately. No post hoc dataset,
phase-window, corruption, learning-rate or intervention search is authorized.
Sources remain flat stage2_coord_* / STAGE2_COORD_* in this study; outputs use
fresh stage2_coord_* generated namespaces. No shared README, paper, Git edits.

## Supervisor-requested exact compression diagnostic

Added after pilot/main-confirmation execution, before numerical/width repeats.
The supervisor requested Legendre reflection diagnostics, without changing any
scientific training configuration, intervention, threshold, or seed. Reflection
is diagonal: the mode j acquires (-1)^j. q1 is blind to reversal; only odd modes
contribute to the edit. Reconstruct q4/q8 reversal edits from the coefficients
already retained for every pilot/confirmation. Those old sources did not save
q16/q32 coefficients, so no such retrospective reconstruction is claimed.
Numerical/width repeats additionally retain all q4/q8/q16/q32 coefficients and
report reversal-edit/operator errors, fixed-endpoint prediction errors, and the
proved odd-tail product bound. These are diagnostics, not extra training solves.
Original producer bytes are preserved as stage2_coord_experiment_v1.py; each
existing run contains its exact source snapshot and SHA256 manifest.
