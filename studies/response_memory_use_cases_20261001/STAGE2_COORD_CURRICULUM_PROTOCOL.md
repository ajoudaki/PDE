# Support-shift continuation: frozen54-solve extension

The root explicitly allocated48 fresh full fits plus6 half-step checks from its
reserve after the fixed-support result was frozen. This continues the same
coordination investigation with nonstationary input support and unchanged truth.
It cannot supersede the adverse fixed-support conclusion. No other route's
outcomes were read. All choices below are frozen before group inspection or runs.

## Input-only groups and equal exposure

Use the same first512 training rows and all designated validation/test rows.
Fashion group A has reconstructed standardized mean pixel value <= its training
median, where the standardized pixels are X[:-1]/X[-1] (the final input is the
normalized constant coordinate). Group B is the complement. This measures the
clipped standardized appearance, not unprocessed physical brightness.
Housing group A has reconstructed standardized longitude (feature index7) <=
its training median; B is its complement. HAR A contains the lower floor(K/2)
of K sorted training-subject IDs; B contains the remainder. The subject boundary
is the midpoint of the adjacent IDs and also partitions held-out subjects.
Test-subject identity never changes training groups. No group uses target values.
Record counts, original activity/class distributions, and all thresholds.
Empty training/test groups or a single-class training subgroup in a classification
domain invalidate that domain; do not redraw or choose a new grouping. An absent
validation subgroup is explicitly unavailable, not an empty-group domain failure.

Let m_A,m_B be group sizes. On the fixed union of m=512 inputs, define sample
loss weights lambda_A(a)=1[a in A]/m_A and analogously lambda_B. The balanced
joint weights are (lambda_A+lambda_B)/2. Loss is sum_a lambda(a) r_a^2; all three
parameter blocks use the corresponding weighted negative gradients, with the
same mobilities(n,1,n). Canonical dense initial laws and zero readout are unchanged.
The observer is b_a=m lambda(a) r_a delta_a^(2), so the unchanged factor2/(mn)
in the finite-sum identity reproduces the actual weighted Euler updates.

Four schedules, each T=64 and eta=1/16:

1. Joint: balanced joint weights throughout.
2. AB: only A for t<32, then only B.
3. BA: only B for t<32, then only A.
4. Alternating: eight blocks of length8, A/B/A/B/A/B/A/B.

Every example has exactly the same integrated loss weight64/(2m_group) under
all schedules. Check this discrete identity before execution. Different dynamics
and endpoints still arise because order changes; equal exposure is not trajectory
equality. n=256 and all other architecture/data settings remain unchanged.

## Interventions and controls

Record complete pre-update h and weighted b. At the frozen endpoint compare:

- No edit; q1 global write replacement; within-half reversal of b (each half
  separately, preserving membership in the two coarse phases).
- Swap the two backward half-histories, retaining their within-half order.
  For AB/BA this exchanges the phase in which each sample's credit meets its
  evolving features. Both complete separate empirical histories are preserved.
- The identical operators on joint and alternating runs; this is essential to
  distinguish support-phase alignment from ordinary temporal drift.
- For swap and within-half reversal separately, five Gram-preserving sign
  scramblings and one isotropic same-spectrum edit; current balanced-joint and
  last-phase gradient descent/ascent, all norm-matched to the swap edit.
- Phasewise q1/q4/q8/q16 reconstructions of the SWAP EDIT, not just of the original
  write; report operator and prediction error against exact swap. Phasewise q1
  knows both phase means and is a stronger simpler baseline than global q1.
- Apply the centered residual E_swap-E_swap,q1 as a separate diagnostic edit.
  This residual itself is not asserted to preserve the complete empirical
  marginals. It tests how much effect remains beyond the two phase means.

For each method record training/validation/test global MSE, A and B subgroup MSE,
prediction RMS changes, and classification accuracy where applicable. Save curves
at physical times0,8,...,64 for both support groups and the same global test.
Compute every intervention without evaluation-driven selection. Report weighted
joint and active-phase training losses separately. No winning phase/window is
selected after the fact.

## Registered discrimination

For schedule s, let D_s=(testMSE_swap-testMSE_within)/testMSE_base. Subtract its
matched sign contrast: C_s=D_s-[median(testMSE_sign_swap)-
median(testMSE_sign_within)]/testMSE_base. For each seed define
F=[C_AB+C_BA]/2-C_joint. This fixed difference-in-differences is the primary
phase-alignment contrast; alternating is a mandatory secondary nuisance control.
Positive support for useful phase chronology requires, in at least two domains:
F>0 in all four seeds and median F>=0.05; median centered-residual edit damage
relative to base>=0.02 averaged over AB/BA; and the phasewise-q1 edit explains
less than half the full-swap absolute test-loss change on the median of the
8 sequential endpoints. Last-task bias remains an alternative if A/B subgroup
changes simply exchange the favored group or matched gradient edits suffice;
the report must resolve or retain that objection explicitly. Threshold crossing
alone does not identify a unique biological or optimizer mechanism.

Failure rejects this specified positive cross-domain phase-alignment claim.
Small or mean-dominated effects cannot be relabeled a positive high-order
coordination result. A materially harmful coordination effect may be reported
as exploratory signed evidence, preserving the original direction and thresholds.

## Seeds, checks, storage, and stopping

Fresh seeds3401,3402,3403,3404, all four schedules and all three domains:48fits.
Repeat3401 joint and AB on every domain at eta=1/32:6fits. These are step checks,
not additional confirmation seeds. Difference-in-differences needing BA refinement
is not certified if untested BA discretization could explain it; global prediction
RMS discrepancy<=0.02 and AB-vs-joint contrast larger than twice its refinement
change are minimum checks, not a license to overstate the broader contrast.
All exact observer/permutation/Gram checks<=1e-9, no nonfinite parameters,
relative feature motion>=0.03 and tanh nonlinearity>=0.05. Validate weighted
velocities by independent autograd and exposure equality before scientific runs.
Phasewise swapped-coefficient product-tail bounds accompany the compression
comparison. Endpoints and fixed-time curves are saved; no causal retraining
identity is claimed by the endpoint swaps.

No architecture/group/horizon/permutation tuning is allowed. Stop at54solves,
60 GPU-process minutes or completion, whichever occurs first. The original route
has finished96 solves, so these54 consume the explicit root reserve, not its
original100-fit allocation. GPU1 only; one CPU thread, float64, TF32 off.
All artifacts remain in the owned flat study namespace and fresh generated runs.

Preflight clarification before any fits: HAR validation uses subjects27–30, so
all validation rows belong to B under the fixed14.5 training-subject boundary.
The first preflight stopped on this metadata-only condition. The grouping stays
unchanged, and validation-A metrics are stored as null; training/test both retain
both support groups. The empty-group gate above is clarified to match the
supervisor's original “where well-defined” subgroup-reporting requirement. No
scientific training outcome informed this clarification.

Interpretation clarification at report freeze: the declared fixed union support
means all512 inputs remain available, and the observer computes their forward
features even when their current loss weight is zero. This was the executed
implementation throughout. No replay-free or unavailable-future-input continual
learning claim is made; logged inactive-group losses do not choose updates.
