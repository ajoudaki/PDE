# Feature learning with 4–16 interacting training inputs

2026-10-07. Bounded empirical continuation of the unchanged causal
feature–response system. Global proofs and the two-input cubic approximation
remain paused. This report supersedes the two-input experiments as the latest
numerical checkpoint, not as a general theorem.

Subsequent numerical update:
[the 16-input integration repair](RESIDUAL_FILTER_RESULT.md) resolves a finer
dense reference and removes observed loss instability with a different,
consistent stepping rule. Its lower-layer accuracy target still fails, with
unresolved particle/mesh error. This report preserves the original 52-run
Euler cohort and its failed checks; the new results do not retroactively
certify these paths or their mechanism ablations.

## Headline

The full causal system tracks **both hidden layers' training–training and
training–passive similarity changes** on the 4- and 8-input panels. Across
the observed training horizon, its ensemble-mean block-RMS discrepancies are
3.6–11.8% of the corresponding dense feature movement. These are same-Euler-mesh
comparisons with explicit sampling and time-step limitations, not a
continuous-time or high-probability accuracy guarantee.

The 16-input test does **not** pass: relative discrepancies are 57–67%, and
both the dense and causal calculations are strongly time-step sensitive.
Even the two prescribed dense RK4 resolutions disagree late in training.
Agreement inside an inflated dense-variability envelope would be misleading
here; this case remains numerically unresolved.

Three conclusions about mechanism emerge:

- Initialization predicts the early **direction**, not the whole trajectory:
  all tested blocks pass the predeclared alignment threshold at 20% loss
  reduction, but the lower-layer direction turns strongly later for 16 inputs.
- Learned middle-layer memory redistributes feature work across layers.
  Removing it increases lower-layer motion while reducing upper-layer motion,
  at matched training progress, in both the dense and causal controls.
- Reciprocal return is not merely an amplifier of neuron movement. In the
  altered causal circuit, removing it can increase individual lower-feature
  displacement while weakening the pairwise similarity changes that the full
  circuit builds. This is a reproducible-on-two-seeds, same-mesh observation;
  that ablation has no dedicated step-refinement run.

The activation-sensitivity control has a large late numerical bias. Its
full-horizon quantitative effect is **inconclusive**, not a confirmed fourth
success. The evidence does not justify simplifying away history, reciprocal
return, or nonlinear gates.

## 1. Fixed setup and predictions before testing

We use two hidden tanh layers of dense width \(n\), input dimension \(d=8\),
\(m=4,8,16\) training inputs, and four passive inputs. Write
\(v_a=x_a/\sqrt d\), so \(\|v_a\|=1\). The dense fields and prediction are

\[
h_{1,a}=\tanh(Av_a),\qquad
h_{2,a}=\tanh(Wh_{1,a}),\qquad
f_a=w^\top h_{2,a}/n.
\]

Entries of \(A(0)\) are independent standard Gaussians, entries of \(W(0)\)
are independent Gaussians of variance \(1/n\), and \(w(0)=0\). The training
deficit is \(c_a=y_a-f_a\), only for \(a\le m\). The loss is
\(m^{-1}\sum_{a\le m}c_a^2\). Passive inputs never enter the forcing sums.
The dense physical gradient flow and the same \(2/m\) normalization in the
causal solver are independently checked in
[the implementation audit](MULTISAMPLE_IMPLEMENTATION_CHECK.md).

Training directions are nested prefixes of 16 fixed, perturbed directions
around four nonorthogonal centers; geometry seed 6201 and perturbation
amplitude 0.65 were fixed before training. Pairwise training inner products
range over approximately \([-0.338,0.522]\), \([-0.481,0.792]\), and
\([-0.661,0.897]\) in the three panels. Labels have both signs and unequal
magnitudes between 0.25 and 0.70. Four passive directions are normalized
versions of \(v_1+v_2\), \(v_1-0.6v_2\), \(v_3+v_4\), and
\(e_5+e_6-e_7\). Their labels are neither supplied nor used. All vectors and
labels are saved with every trajectory; the exact generation rule is in
[the driver](multisample_experiment.py). These amplitudes are exploratory,
not certified against the original conservative small-label condition.

The [README precommit](README.md#multisample-feature-trajectory-phase-2026-10-07)
and [mechanism predictions](MULTISAMPLE_MECHANISM_PREDICTIONS.md) preceded the
scientific runs. They specified:

1. Full-system tracking of both feature-similarity blocks in both layers
   throughout training, including changes from initialization.
2. Cosine alignment at least 0.7 between the exact initial Gram acceleration
   and the observed change at 20% loss reduction; also report 50% and 80%.
   Training off-diagonals must be checked separately. There is no sign rule
   based only on label products for these correlated inputs.
3. Reciprocal-return removal changes feature trajectories and passive
   predictions even when the modified model fits the labels.
4. Removing learned middle writes shifts later feature motion toward the
   first layer. Anchored-affine controls test whether evolving activation
   sensitivity matters, subject to their own numerical resolution.

No sample geometry, labels, seed, horizon, or mesh was selected after observing
the results. There were no additional scientific runs after a numerical gate
failed.

## 2. What was compared, and at which times

The measured uncentered feature similarity is

\[
C^\ell_{ab}(t)=\frac1n h_{\ell,a}(t)^\top h_{\ell,b}(t)
\]

for the dense model, and the corresponding population expectation, estimated
using \(N\) particles, for the causal model. It is not cosine-normalized or
mean-centered. The population particle count \(N\) is not the dense width
\(n\). Layer \(\ell=1,2\) and pairs \(a,b\le m\) give the
training–training block; \(a\le m<b\le m+4\) gives training–passive.

All primary runs used 48 Euler updates, with normalized time
\(2t/m\in[0,19.2]\) and normalized step 0.4; equivalently the physical
horizon is \(9.6m\) and step \(0.2m\). We compared **every one of the 49
saved times**, not only the fitted endpoint. The complete causal history law
in [the candidate](CANDIDATE_SYSTEM.md) is unchanged. Its generalization from
two training inputs to a panel changes array dimensions and tangent indexing,
not equations or population closure.

The primary dense mean uses widths 1024, seeds 101, 202, 303. The primary
causal mean uses 512 particles, seeds 1701, 1702, 1703. Additional runs
measure dense-width change (512 versus 1024), particle-size change (512 versus
1024 at seed 1701), and causal Euler step change (0.4 versus 0.2 at 256
particles). Same seed identifiers do not guarantee a perfect common-random
coupling after Gaussian history factorization changes rank.

For each realization, subtract its own initial Gram before averaging to
measure feature change. For a given block, the reported change error is
the maximum over saved times of the RMS, across its entries, of the difference
between the two mean changes. Relative error divides this by the maximum
over saved times of the dense mean change's block RMS. The two maxima need
not occur at the same time. These are **not** maximum pointwise relative
errors, which become singular near initialization.

### Full blockwise accuracy

| Training inputs | Hidden layer | Pair block | Dense movement, RMS | Change error, RMS | Relative change error | Change error, largest entry | Absolute-Gram error, largest entry |
|---:|---:|:---|---:|---:|---:|---:|---:|
| 4 | 1 | training–training | 0.05599 | 0.004727 | 8.44% | 0.009477 | 0.01752 |
| 4 | 1 | training–passive | 0.04597 | 0.003858 | 8.39% | 0.006686 | 0.02093 |
| 4 | 2 | training–training | 0.12018 | 0.004299 | 3.58% | 0.008848 | 0.01464 |
| 4 | 2 | training–passive | 0.09811 | 0.004213 | 4.29% | 0.006508 | 0.01154 |
| 8 | 1 | training–training | 0.04576 | 0.005380 | 11.76% | 0.01530 | 0.02845 |
| 8 | 1 | training–passive | 0.04873 | 0.005384 | 11.05% | 0.01577 | 0.02180 |
| 8 | 2 | training–training | 0.10197 | 0.006288 | 6.17% | 0.01315 | 0.01906 |
| 8 | 2 | training–passive | 0.10550 | 0.006443 | 6.11% | 0.01418 | 0.01588 |
| 16 | 1 | training–training | 0.09525 | 0.06030 | 63.31% | 0.14061 | 0.15226 |
| 16 | 1 | training–passive | 0.09640 | 0.05752 | 59.66% | 0.13262 | 0.13945 |
| 16 | 2 | training–training | 0.11151 | 0.07511 | 67.35% | 0.19249 | 0.19078 |
| 16 | 2 | training–passive | 0.14511 | 0.08248 | 56.84% | 0.18991 | 0.19128 |

All columns take their stated maximum over time. The 16-input rows are
retained failure diagnostics for the coarse discrete calculation, **not**
estimates of well-resolved continuous-flow accuracy.

For 4 and 8 inputs, the mean of the three pairwise dense **maximum-time**
block-RMS change discrepancies is 0.00616–0.01048 and 0.00806–0.00977,
respectively. The maximum is taken separately for each pair before averaging;
this need not equal the maximum of the mean pairwise curve. Every corresponding
causal-versus-dense mean discrepancy is smaller. Absolute-Gram entrywise
discrepancies are also smaller than the mean pairwise dense comparator in
those eight rows. This is a descriptive comparison of **ensemble means with
individual-run variability**. Averaging reduces sampling noise; it is not
a probability guarantee, a coupled-path result, or a claim that a single
512-particle draw always outperforms a dense draw.

The predeclared diagnostic envelope was three combined run standard errors,
plus measured particle-size and dense-width changes, separately for each
time, entry, layer and block. No block has three consecutive same-entry
exceedances by more than 0.005 or 20% of its dense entrywise movement. But
the 16-input envelope is enlarged by unstable trajectories and is not useful
evidence of accuracy. Its failed time-resolution gate and 57–67% relative
errors take precedence. This avoids treating a loose variability comparator
as a successful explanation of learning.

Time-resolved machine-readable errors and variability are in
`multisample_v1/analysis/accuracy_curves.csv` and `accuracy_curves.npz`;
`blockwise_accuracy.csv` contains this table's unrounded values.

![Both hidden layers throughout the recorded horizon](../../data/generated/transparent_learning_dynamics_20261007/multisample_v1/analysis/feature_trajectory_changes.png)

![Error curves and the descriptive dense comparator](../../data/generated/transparent_learning_dynamics_20261007/multisample_v1/analysis/feature_trajectory_errors.png)

The first figure shows the size of the Gram change, not its direction.
The second actually subtracts the matrices before taking RMS, so similarly
sized but differently directed feature changes do not count as agreement.

## 3. Numerical accuracy: what is controlled and what is not

Dense RK4 references used normalized steps 0.1 and 0.05 at width 512,
seed 101, for all three panels. Maximum common-grid discrepancies over the
whole panel and horizon were:

| Training inputs | Prediction | Layer-1 Gram | Layer-2 Gram | Refinement decision |
|---:|---:|---:|---:|:---|
| 4 | \(6.22\times10^{-8}\) | \(1.49\times10^{-8}\) | \(3.15\times10^{-8}\) | passes |
| 8 | \(1.43\times10^{-6}\) | \(3.63\times10^{-7}\) | \(6.89\times10^{-7}\) | passes |
| 16 | 0.03510 | 0.003303 | 0.008924 | fails |

The predeclared tolerance is 0.00001 or 1% of the corresponding observed
change, whichever is larger. This is a refinement diagnostic, not a rigorous
ODE error bound. The causal primary calculation remains Euler: a well-resolved
dense RK4 reference does not magically give the population calculation the
same accuracy.

Against the finer RK4 dense path, the primary dense Euler calculation has
maximum layer-2 Gram biases 0.01354, 0.02785, and 0.41881 for 4, 8, and
16 inputs. The matched-particle causal 0.4-to-0.2 step change has maximum
block-RMS differences:

| Training inputs | Layer 1, training–training / training–passive | Layer 2, training–training / training–passive |
|---:|:---|:---|
| 4 | 0.00193 / 0.00149 | 0.00393 / 0.00311 |
| 8 | 0.00323 / 0.00343 | 0.00590 / 0.00635 |
| 16 | 0.10293 / 0.10663 | 0.12449 / 0.15877 |

Therefore the 4- and 8-input **matched-Euler** agreement is informative,
while its few-percent numbers must not be recast as controlled continuous
population-flow errors. In particular, the measured time sensitivity is
comparable to some of the smaller mean discrepancies. One particle-doubled
draw and one step-halved draw do not establish convergence rates.

There is a concrete explanation for the 16-input numerical failure. Along
the finer dense RK4 path, the largest training-kernel eigenvalue grows from
1.273 to 28.45. In normalized time the residual equation is
\(dc/d(2t/m)=-Kc\). Freezing its linearization, Euler multiplies an
eigenmode by \(1-h\lambda\). At normalized step 0.4, the largest value of
\(h\lambda\) is about 11.38, far outside the interval \([0,2]\) that
contracts a positive scalar mode. For RK4 step 0.1, its scalar amplification
polynomial \(1-z+z^2/2-z^3/6+z^4/24\), evaluated at \(z=2.845\), also
has magnitude exceeding one. This supports a stiffness/time-resolution
diagnosis; it is not a proof that numerical error is the only possible model
discrepancy. At 4 and 8 inputs the maximum eigenvalues are 1.570 and 4.987.

No extra mesh was searched after this failure. The proper next numerical
repair is a stable, refinement-checked integrator for the existing causal
law and matched dense paths—not changing the model to fit the coarse curve.
The present phase makes no fitted-endpoint claim for 16 inputs.

## 4. Which mechanistic predictions survived?

### 4.1 An early direction, followed by genuine turning

At zero readout the hidden velocities vanish. The exact initialized Gram
acceleration can be computed from the initialized dense fields and labels;
its full formula and derivative checks are in
[the prediction note](MULTISAMPLE_MECHANISM_PREDICTIONS.md) and
[the implementation check](MULTISAMPLE_IMPLEMENTATION_CHECK.md).
No trajectory coefficient is fitted. We compare the direction of
\(t^2(C^\ell)''(0)/2\) with \(C^\ell(t)-C^\ell(0)\).
The saved acceleration is with respect to physical time, not normalized time.

The following cosines use the **first saved fine-RK4 time** reaching each
loss fraction. Off-diagonal training entries avoid explaining only neuron
norm growth. Each entry lists training–training off-diagonal / training–passive.

| Training inputs | Layer | 20% loss reduction | 50% loss reduction | 80% loss reduction |
|---:|---:|:---|:---|:---|
| 4 | 1 | 0.998 / 0.996 | 0.982 / 0.966 | 0.920 / 0.871 |
| 4 | 2 | 0.998 / 0.996 | 0.977 / 0.962 | 0.895 / 0.861 |
| 8 | 1 | 0.996 / 0.994 | 0.946 / 0.924 | 0.770 / 0.724 |
| 8 | 2 | 0.996 / 0.993 | 0.945 / 0.917 | 0.758 / 0.701 |
| 16 | 1 | 0.982 / 0.979 | 0.748 / 0.785 | 0.089 / 0.314 |
| 16 | 2 | 0.983 / 0.980 | 0.803 / 0.828 | 0.483 / 0.617 |

The 20% prediction survives in every block. This is not just an infinitesimal
test. Nevertheless, direction alignment does not imply a good Taylor amplitude:
by 80% reduction, the quadratic prediction overstates the change norm by
factors about 1.64–2.11, 2.33–3.31, and 4.80–6.66 in these displayed blocks.
No further cubic or scalar-clock refinement is attempted.

The 16-input early-window comparison is separately resolved even though its
late trajectory is not. The independent mechanism check compares both RK4
grids through the last common saved time preceding the 80%-reduction crossing
and finds maximum layer-2 Gram disagreement about \(3.7\times10^{-6}\).
Its interpolated crossing cosines
differ by less than 0.00034 between grids. Interpolating within the first
crossing interval gives, for example, 0.107 instead of 0.089 for the lower
training off-diagonals; both show the same pronounced turn. This is explicitly
a localized refinement check, not salvage of the failed full horizon.

Interpretation: the initial sensitivity-weighted association selects an early
feature-change direction. As different residuals evolve, the circuit's
history-weighted writes need not remain parallel to that initial direction.
The data reject a universal continuation along one frozen feature direction;
they do not yet uniquely apportion its rotation among residual reweighting,
reciprocal return, and changing activation sensitivity.

### 4.2 Learned middle memory redistributes where the work is done

For 8 training inputs, compare full dynamics with a frozen dense middle
matrix, and independently with both learned middle-memory directions removed
from the causal equations. The readout and first layer continue to learn.
Initial lower-feature acceleration is unchanged exactly; the prediction
concerns later redistribution, not an initial effect.

At the first saved time reaching **99% loss reduction in each model**, measure
the RMS feature displacement from initialization, averaging over neurons and
the specified input panel. Relative changes caused by removing middle writes
are:

| Implementation, two seeds | Layer 1, training | Layer 1, passive | Layer 2, training | Layer 2, passive |
|:---|:---|:---|:---|:---|
| Dense, freeze middle matrix | +25.2% to +28.1% | +26.5% to +28.1% | −8.6% to −8.0% | −11.5% to −11.4% |
| Causal, remove learned middle memory | +27.6% to +30.0% | +29.6% to +30.8% | −7.6% to −7.5% | −10.1% to −9.4% |

The dense full-horizon training–passive Gram contrasts have block RMS
0.0150–0.0172 in layer 1 and 0.0353–0.0378 in layer 2. The independently
implemented causal contrasts are 0.0145–0.0156 and 0.0361–0.0370. Their
agreement in direction and scale is stronger mechanistic evidence than
observing that both models eventually fit.

For dense seed 101, halving the frozen-middle control's Euler step changes
these passive Gram curves by block RMS 0.00260 and 0.00310, respectively;
these are smaller than the observed contrasts. Passive output changes under
the ablation reach 0.0988–0.1045 over inputs and time in the dense runs, and
0.1051–0.1117 in the causal runs. The dense control's own passive-output
step change is 0.01116. The full-model Euler bias and the absence of a
separate causal-ablation refinement remain qualifications; this is not a
continuum intervention theorem.

Mechanistically, disabling an upper write does not simply subtract its
contribution from the full trajectory. Remaining trainable paths compensate.
The lower layer moves further to supply representations that the upper
learned association would otherwise help construct. Passive inputs inherit
that redistribution despite supplying no force themselves.

### 4.3 Reciprocal return organizes shared geometry, not just motion size

For 8 inputs, remove both reciprocal corrections while retaining learned
middle memory and recomputing sensitivities for the altered causal circuit.
This is a causal-circuit intervention, not automatically another dense
gradient flow. Both seed identifiers fit to final relative losses below
\(6.2\times10^{-6}\), but passive output contrasts reach 0.144–0.162.
The maximum-time Gram-change contrasts, block RMS, are:

| Layer | Training–training, two seeds | Training–passive, two seeds |
|---:|:---|:---|
| 1 | 0.0283–0.0291 | 0.0265–0.0272 |
| 2 | 0.0466–0.0474 | 0.0448–0.0455 |

These substantially exceed the full system's measured mean discrepancies on
the same panel. Their signs/directions are consistent across the two seeds.
However, the ablation has no dedicated half-step or larger-particle run;
the full-system refinement is not a bound on its altered dynamics.

A post-test, explicitly exploratory diagnostic sharpens the interpretation.
At matched 99% loss reduction, lower individual-feature displacement grows
by 21–26% on training inputs and 24–28% on passive inputs when reciprocal
return is removed. Yet the RMS **off-diagonal** training–training Gram change drops from
about 0.0463–0.0465 to 0.0257–0.0265; the training–passive change drops from
0.0471–0.0481 to 0.0338–0.0355. The projection of the altered lower Gram
change onto the full system's direction retains only 49–52% of its training
amplitude and 63–66% of its passive amplitude. The training block in this
exploratory diagnostic excludes the diagonal; all passive entries are also
cross-input. Thus diagonal feature-norm shifts alone cannot explain the effect.

Thus “less feature movement without feedback” would be the wrong explanation.
The same initialized map's forward/backward reuse helps organize displacement
into shared sample geometry. Removing that return can make neurons move
more while building weaker common associations. This observation preserves
the distinction between learned memory and reciprocal memory; it does not
establish necessity for every dataset or a quantitative all-time theorem.

### 4.4 Activation sensitivity: do not turn unresolved numerics into a claim

The dense anchored-affine control replaces each tanh by its tangent map at
that neuron's initialized preactivation, using the same fixed derivative in
backpropagation. Weights still learn. It is a different forward model with
matched derivatives, not deletion of one term from the full-model trajectory.
It has exactly the same initial feature acceleration as full tanh.

On the primary mesh its passive-Gram contrasts are large: layer-1 block RMS
0.0416–0.0449, layer-2 block RMS 0.0888–0.0928. But seed 101's own step
halving changes these curves by 0.0330 and 0.0749, and changes a passive
prediction by as much as 0.232. Most of the apparent late contrast is therefore
comparable to unresolved time-step sensitivity. The proposed full-horizon
activation-effect test is **inconclusive**. We retain nonlinear sensitivity
in the full system and do not infer a trustworthy effect size from this control.

A narrower, explicitly post-test stage comparison is informative. At each
model's first saved 99%-loss-reduction crossing in seed 101, the coarse
affine/full passive-Gram RMS contrasts are 0.01953 and 0.04651 in the two
layers. Replacing both paths by their available refinements gives 0.01985
and 0.04619. The affine control's own refinement changes those stage Grams
by 0.00147 and 0.00356; full Euler versus fine RK4 changes them by 0.00172
and 0.00409. This supports a restricted fitting-stage effect, not the late
trajectory. Actual attained relative losses differ (0.00828 versus 0.00995
on the refined paths), and this refined comparison uses one seed. The full
model's refined passive RMS derivative-gate changes at the endpoint are
0.1696 and 0.2221, confirming that the activation sensitivities do evolve.
Neither statistic isolates a single gate's causal contribution. Activation
remainders and their readout projections were not saved and are not claimed
as measured. Details are in
[the mechanism check](MULTISAMPLE_MECHANISM_CHECK.md#4-activation-sensitivity-measured-drift-and-a-restricted-early-contrast).

### 4.5 Old writes are evaluated against current features

The following exact discrete identity checks the learned-readout memory,
including passive inputs:

\[
f_a^k=\frac{2\Delta t}{m}
       \sum_{j<k,b\le m}c_b^j C^2_{ab}(k,j).
\]

It says that a training residual writes a feature at its own time \(j\),
but the later prediction evaluates its overlap with the **current** feature
at time \(k\). The mechanism is not a sum against a frozen kernel, and a
passive point participates on the evaluated side without becoming a source.

Reconstructing every prediction on the three seed-1701 full causal runs from
saved residuals and two-time similarities gives maximum errors below
\(2.0\times10^{-15}\). In the 8-input run, the last four passive predictions
are approximately \((-0.2320,0.4714,0.00633,0.8616)\); contributions from
writes after the first half of the horizon are only
\((-0.00319,0.00185,0.00054,0.00288)\). Early writes persist in a changing
representation. This split is an exact accounting on the observed causal
path, not an intervention that erases later writes and reruns learning.
The identity also holds algebraically in the unresolved 16-input calculation,
which cannot turn it into a validated continuous-flow mechanism there.

## 5. Checks, reproducibility, and claim boundary

The campaign completed the predeclared 30 dense and 22 causal trajectories
without nonfinite states or extra scientific runs. Summed numerical execution
time was 557.835 seconds, excluding later serialization and analysis. Largest
recorded process peak RSS was 5882.9 MiB. All runs used float64 and one BLAS
thread. The source hashes in every run record agree; no numerical source was
edited while the campaign ran.

The generalized producer reproduces the frozen two-input code within
\(1.11\times10^{-16}\), and its additional response probes, passive-force
exclusion, dense gradients, Gram acceleration and exact memory identities
passed bounded implementation checks. Across the 22 scientific causal runs,
the largest analytic covariance-factorization discrepancy is
\(5.60\times10^{-9}\) and largest discarded innovation variance is
\(1.93\times10^{-12}\). These describe Gaussian factor arithmetic, **not**
particle sampling error or a bound on model accuracy.

One driver-interface defect was discovered: unsupported combinations of
implementation and ablation names silently select the full model. Every
one of the 52 saved configurations was checked against the valid pairing
table and is unaffected. The historical producer remains frozen for
reproduction; use only the valid combinations listed in
[the implementation check](MULTISAMPLE_IMPLEMENTATION_CHECK.md).

Reproduction and analysis sources:

- [Dense/panel driver](multisample_experiment.py),
  [generalized causal producer](causal_panel_simulator.py), and
  [exact cohort list](run_multisample_cohorts.py).
- [Blockwise analysis](analyze_multisample_experiment.py), which reads saved
  arrays and launches no trajectories.
- [Implementation checks](MULTISAMPLE_IMPLEMENTATION_CHECK.md),
  [independent arithmetic check](MULTISAMPLE_ACCURACY_CHECK.md), and
  [independent mechanism analysis](MULTISAMPLE_MECHANISM_CHECK.md).
- Raw arrays, configurations, source hashes, diagnostics and analysis outputs:
  `data/generated/transparent_learning_dynamics_20261007/multisample_v1/`.

Run each cohort once in a fresh generated output location; the driver refuses
to overwrite a run. From the repository root, analysis alone is:

```bash
python studies/transparent_learning_dynamics_20261007/analyze_multisample_experiment.py
```

This is a completed **bounded empirical phase with mixed outcomes**, not
an independently reproduced full campaign and not promotion to established
theory. The exact identities and local derivative checks are distinct from
the empirical agreement. Still missing are resolved continuous population
trajectories for the harder panel, dedicated refined reciprocal/affine
controls, broad geometry/activation/depth coverage, and the original-scope
full-trajectory dense-variability guarantee. Global proofs remain paused.

The defensible next step is numerical stability repair of the same causal
system on the unresolved panel, with a fresh bounded contract—not another
two-input cubic approximation and not new global proof machinery.
