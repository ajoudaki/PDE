# What the causal feature–response system explains through learning

2026-10-07. User-directed analytical/numerical phase. Global-proof work is
paused. This report concerns the existing candidate, not a new compression
theorem or a promotion into the book. The numerical experiment contract was
recorded in README.md before the campaign.

## Headline

The candidate now has evidence beyond initialization: on the declared
two-hidden-layer tanh example it follows dense training through substantial
fitting, including an unlabeled passive input. Its reciprocal terms matter
even when a response-off surrogate fits both training labels. Learned middle
memory and initialized reciprocal feedback have different effects on where
feature learning occurs.

A particularly transparent simplification emerged. For this symmetric
two-sample example, feature learning follows an amplitude-independent orbit;
the residual controls how quickly and how far training travels along it.
A one-state cubic approximation, with coefficients calculated solely at
initialization, predicts both hidden-layer cross-similarity curves well on
the tested label amplitudes. A frozen-kernel residual clock does not.

The simplification has a resolved limitation: its cubic passive-output
approximation is accurate at the smaller amplitudes but misses about 13% at
Y=0.6 with opposite labels, even though its training-feature curves remain
accurate. The full causal passive law is therefore retained; it must not be
replaced by the successful training-mode reduction.

These are a local analytical reduction plus finite numerical evidence. They
do not establish the original all-time dense-variability guarantee, arbitrary
depth/data accuracy, or a small Markov closure for general data.

## 1. Shared setup and what was compared

There are two tanh hidden layers of dense width n, no biases, and normalized
inputs

\[
v_1=e_1,\qquad v_2=e_2,\qquad v_3=(2e_1+e_2)/\sqrt5.
\]

Only inputs 1 and 2 train. Their labels are \(Y(1,s)\), with \(s=\pm1\).
Input 3 is passive and has no label or training weight. The initialization
has independent first-layer entries of variance one, middle entries of
variance \(1/n\), and exactly zero readout. We use the canonical mean-square
loss and block mobilities \((n,1,n)\). In particular the physical loss factor
\(2/m\) is one, not two.

Write \(f_a\) for prediction and \(C^\ell_{ab}\) for the normalized inner
product of hidden features of inputs a,b in layer \(\ell\). For finite-width
runs all reported changes subtract that run's own initialized Gram; its
cross entries are not set artificially to zero.

Dense widths were 256,512,1024, with independent seeds 101,202,303,404.
The principal mechanism curves use width512; width1024 supplies the larger
matched reference. We used fixed \(Y=0.075,0.15,0.6\), through physical time24.
Opposite labels were tested at all three amplitudes; same labels at 0.6.
These amplitudes are exploratory numerical instances, **not certified
instances of the original conservative small-label cap**. They do not shrink
with width. No claim about the complete original activation/data class follows.

Two distinct reference comparisons were made:

- Dense RK4 at step0.1, with step0.05 checks, for the physical-time mechanism
  and analytical approximation.
- Dense simultaneous Euler and the autonomous population-history solver on
  the *same* step 0.4 mesh; step 0.2 was checked separately. This avoids charging
  Euler bias to the population formulation.

The population solver uses two interacting Monte Carlo quadrature populations,
not a realized dense network. It evolves the full first-tangent history in
CANDIDATE_SYSTEM.md and computes its own coefficients. Population sizes1024
and4096, with independent complete-run seeds1701,1702,1703 as specified in the
run plan, assess quadrature variability separately from physical dense width.
There is no fit to a future dense trajectory.

## 2. The useful reduced dynamics: a learned fitting clock

In the symmetric deterministic population flow, \(f_2=s f_1\). Define the
accumulated residual \(u\) by

\[
\dot u=Y-f_1,\qquad u(0)=0.
\]

All parameter velocities share this residual factor. After factoring it out,
the remaining feature-learning orbit depends on the label direction s, not
on its amplitude Y. The same input sign symmetry identifies the two training
orbit functions for s=+1 and s=-1. Changing Y changes the stopping point;
changing s reverses the sign of cross-feature alignment.

This is an exact symmetry statement for the compatible population flow on
an interval of existence. It is not an exact identity of an individual iid
dense realization, or something justified merely by averaging its residuals.
Nor is it yet a scalar closure: the whole output along the orbit is unknown.

The first nonlinear orbit coefficient closes a useful approximation:

\[
\dot u=Y-0.2364504105\,u-0.1811526358\,u^3,
\qquad u(0)=0,
\]
\[
f_1\approx0.2364504105\,u+0.1811526358\,u^3,
\qquad f_2\approx s f_1,
\]
\[
C^1_{12}\approx s\,0.1067554683\,u^2,
\qquad C^2_{12}\approx s\,0.1914828843\,u^2.
\]

Every displayed coefficient is an initial Gaussian expectation, not a
regression coefficient. ANALYTICAL_LEARNING_PROFILES.md gives the complete
formulas; RESIDUAL_CLOCK_CHECK.md independently checks the symmetry,
normalization, exact adjoint contraction and Taylor factorials.
The choice to try this resummation was motivated by discrepancies already
observed in this cohort. It is exploratory model development, not a held-out
confirmatory test, even though its coefficients were not fitted.

The linear coefficient is the initial top-feature variance. The positive
cubic coefficient is a sum of middle-learning and squared backward-return
contributions. Thus feature learning increases the response of the trained
output mode at this order:

\[
\frac{d f_1}{du}\approx0.2364504105+0.5434579073\,u^2.
\]

This explains more than a changing kernel. Signed, sensitivity-filtered
feature associations increase the ability to fit that label direction;
the resulting faster reduction of the residual limits additional feature
writes. The geometry of the orbit and the speed of training on it are
different effects.

### The discrepancy that led to this simplification

Keeping the initial fitting rate would give
\(u=Y(1-e^{-0.2364504105t})/0.2364504105\). That expression is the correct
leading small-label clock, but at Y=0.6 it overpredicts final cross-feature
changes by over a factor of four. It must not be extrapolated as the actual
late-training clock.

Replacing it by the initialization-derived cubic equation fixes most of this
discrepancy in the tested example:

| Y | Dense change in C1 at time24 | Cubic prediction | Dense change in C2 | Cubic prediction |
|---:|---:|---:|---:|---:|
|0.075|−0.00960|−0.00940|−0.01697|−0.01686|
|0.15|−0.03034|−0.02931|−0.05370|−0.05258|
|0.6|−0.15813|−0.15454|−0.27691|−0.27719|

Dense entries are four-run means at width512 and opposite labels. More
importantly, over the complete saved grid on [0,24], the largest discrepancy
is 3.4% of the corresponding observed final mean feature change (across the
two layers and three amplitudes). This is not pointwise relative error,
not a bound for every dense realization, and not a statistically certified
population bias. Monte Carlo width variability is visible in the raw records.

The exact local coefficients do not certify a cubic truncation at moderate u.
Its observed success here is empirical. In particular, the scalar training
clock alone does not determine a passive input: its own orbit observable
must also be retained or approximated.

## 3. Learned memory and reciprocal feedback do different jobs

The full candidate retains both learned-middle history sums and the reciprocal
responses due to using the same initialized map in both directions.
We tested two different deletions, recomputing every control's own residuals,
moments and responses:

- No learned middle memory removes *both* learned forward and backward sums.
  Its dense counterpart freezes the middle matrix while retaining its true
  transpose, first-layer training and readout training.
- No reciprocal correction removes both applied R terms. This is a deliberate
  surrogate law, not a canonical gradient flow or a claimed exact model of
  independently untied dense feedback.

At Y=0.6, opposite labels, matched Euler step0.4 and time24:

| System | Change in C1 | Change in C2 | Passive prediction |
|---|---:|---:|---:|
|Dense, width1024, four runs|−0.1525|−0.2685|0.3527|
|Full causal, population4096, three runs|−0.1480|−0.2634|0.3543|
|Causal without reciprocal correction|−0.0683|−0.1743|0.3271|
|Causal without learned middle memory|−0.1819|−0.2006|0.3506|

The corresponding frozen-middle dense control, width512 on the same Euler
mesh, gives (−0.1888,−0.2012,0.3549). The restricted training system and its
causal counterpart show the same qualitative redistribution between layers.
These counterfactual differences are not an additive decomposition of one
unchanged full trajectory.

Removing reciprocity changes first-layer alignment by about0.080 and upper
alignment by0.089, while its final training residual remains below
1.9e−6. Thus fitting the training labels does not identify the learned
representation or passive prediction. The first layer still develops some
alignment later in the response-off law; one must not extend its vanishing
leading initialized coefficient into a claim of zero motion at every time.

Removing middle learning, in contrast, produces *more* first-layer motion
and *less* second-layer alignment by the end. Feature learning reallocates
across the remaining trainable blocks. “Less learned memory means uniformly
less feature learning” is not supported.

### Instantaneous curvature is not the whole return

In the full causal simulation, the accumulated upper backward cross-responses
to constant shifts of the historical training primitives are approximately
−0.603 and +0.588 in the two directions at time24. The same-time self-curvature
term for input1 is about−0.467, but its strict-past self-response sum is+0.750.
Thus the self-return has net positive coefficient about0.283. Keeping only
the same-time curvature would even give its sign incorrectly.

These are discrete, coordinate-qualified response sums, not a proved continuum
density or a decomposition of response-field energy. Their values have largely
stabilized by time8 and persist when the residual is tiny: the learned state
retains sensitivity to earlier interactions after new writes have nearly stopped.

## 4. Activation sensitivity and the passive input

For orthogonal training inputs the exact first-layer feature velocity is

\[
\dot h_{1,a}=(y_a-f_a)\operatorname{sech}^4(z_{1,a})\,b_{1,a},
\qquad a=1,2.
\]

The squared derivative is a real selection mechanism: both the incoming
training sensitivity and the conversion from preactivation to feature motion
contribute a gate. Initial-gate quartiles show far less movement in saturated
neurons, although that descriptive association alone does not separate gates
from correlated backward carriers.

For a dynamical control we replaced both activations by their fixed affine
expansions at initialization, separately for each neuron/input on the declared
panel. Forward values and derivatives are changed consistently. This is a
different transductive gradient model, not tanh with an arbitrary surrogate
gradient, and not a globally linearized parameter model.

At Y=0.6, width512, RK4 through time24, passive predictions are:

| Control | Passive prediction, mean of four runs |
|---|---:|
|Full nonlinear training|0.35790|
|Middle matrix frozen|0.35517|
|Initialization-anchored affine activations|0.31723|
|Readout only, features frozen|0.27576|

The full-minus-affine difference is0.04067 with paired standard error0.00289.
This isolates the importance of retaining nonlinear activation evolution
relative to that specified control; it is not a pure backward-gate-only effect.

The passive input really changes representation: the full-model RMS changes
are about0.153 in the first layer and0.237 in the second. Its initial geometry
sets the mixture of training forces it receives, but those forces change its
features, not merely its readout on a fixed kernel. No validation label is
ever supplied. With same-sign training labels its mean final prediction is
about0.666; no target is available to call either value better generalization.

### A useful failure: the training clock does not close passive behavior

The passive initial Gaussian contractions were independently evaluated before
their trajectory comparison, with quadrature refinement and a rotated-coordinate
check. For opposite labels they give the cubic orbit approximation

\[
f_3\approx0.1092310312\,u+0.1034591019\,u^3.
\]

| Y | Dense passive output at24 | Cubic prediction | Maximum grid error / final mean output |
|---:|---:|---:|---:|
|0.075|0.03513|0.03511|0.40%|
|0.15|0.07294|0.07213|1.12%|
|0.6|0.35790|0.31162|12.93%|

Using the actual measured integrated residual in the last case gives0.32047,
still far from0.35790. The main discrepancy is therefore not removed by fixing
the clock alone. The omitted higher nonlinear terms in the passive orbit
observable matter before they visibly spoil the two training cross Grams.
At Y=0.6 with same-sign labels the separately derived passive cubic gives
0.68498 versus0.66609, with maximum normalized grid discrepancy3.27%.

This result limits the proposed reduction, not the full history-state system.
The safe simplification is a training-mode explanatory approximation plus
retained passive feature/response observables. We have not established a
closed low-order equation for those passive observables at moderate labels.
No coefficients were refitted after this failure.

## 5. Accuracy and numerical controls actually established

The full causal solver's maximum difference from the width1024 dense Euler
*ensemble mean*, over all three outputs and all61 saved times, was0.00291
at Y=0.15 and0.00874 at Y=0.6. For orientation, the mean of the six pairwise
dense-versus-dense grid-supremum discrepancies was0.00698 and0.01719.
This is a finite empirical comparison of means and sample variability,
not the requested mathematical variability guarantee.

For both layer cross-feature changes and the passive prediction, the observed
mean discrepancy stays inside the preregistered diagnostic envelope: three
combined run-level standard errors, plus observed population-size change,
plus observed dense-width change. This envelope has no simultaneous-coverage
or unknown-bias guarantee. With only two/three population replicates, precision
is limited; a smaller systematic error remains unresolved. The predeclared
sampling-floor branch added two population8192 runs at Y=0.6. Their largest
all-panel mean prediction discrepancy from the same dense reference is0.00407;
the two cross-feature discrepancies are0.00345 and0.00325. This supports the
same coarse conclusion but does not resolve small systematic bias or establish
monotone population convergence.

Time errors are kept separate. At Y=0.6, halving the population Euler step
changes the mean top-feature statistic by as much as0.0099 on common times.
That is not negligible, so the strongest full-system comparison is the
matched-Euler statement, not a high-precision continuous-time validation.
The dense RK4 mechanism curves have much smaller integration differences:
step-halving changes predictions by at most6.5e−8 and the recorded kernel
blocks by at most1.6e−7 in the full-mode check. Frozen-middle and affine
controls have their own retained refinement runs.

Other controls:

- Independent maintained-API RHS/kernel comparison: maximum discrepancy
  2.8e−17.
- Exact two-sided dense Euler memory reconstruction: discrepancy below7e−16.
- Loss identity checked against velocity energy and centered directional
  differences; the latter differed by less than1e−11.
- Global label-sign symmetry, frozen-block velocities and exact readout-only
  matrix-exponential predictions checked; the last differed by8e−10.
- Population tests check frozen-coefficient formal primitive derivatives,
  singular zero primitives, same-time curvature, output history identity,
  passive non-feedback and both ablations.
- Initial Gaussian quadrature at orders100/160 agrees within6.6e−9 across
  the recorded constants; this is a refinement check, not an interval enclosure.
- Maximum covariance-factor discrepancy in the population runs is1.7e−9;
  maximum single discarded innovation variance is7.9e−13. Reducing the
  relative rank tolerance from1e−12 to1e−14 changes predictions by less4e−7
  in the checked run. Changed retained ranks can change random-stream coupling,
  so this paired difference is not a rigorous tolerance-to-output bound.

The primary comparison snapshot records77 dense and21 causal trajectories.
Including the final population-size check gives77 dense and23 causal
trajectories, plus the small implementation pilot/tests, within the declared
run budget. Recorded trajectory wall-time sum is about491 seconds; maximum
process RSS is about1.25 GiB (about661 MiB before the size8192 refinement).
This is a research diagnostic, not an efficiency comparison or deployment
claim. The population histories have quadratic memory and cubic contraction
work in the number of time steps.

## 6. Exact identities, approximations and open claims

**Exact/algebraically checked:** canonical gradient and memory identities;
finite chronological first-tangent equations; the passive training exclusion;
population symmetry reduction conditional on its flow realization; initial
Gaussian derivative coefficients and their positive-contraction explanation.

**Approximations:** cubic truncation of the example's orbit; finite population
quadrature; tiny Gaussian-innovation truncation; Euler/RK4 discretization;
fixed-panel/grid comparisons. The reciprocal-off and affine controls are
specified different dynamical systems, not approximation theorems.

**Empirically supported here:** the full candidate's matched-Euler predictions
and two-layer cross-feature dynamics; the distinct effects of learned middle
memory and reciprocity; nonlinear passive representation change; and the
initialization-only cubic clock over the tested learning window.

**Still missing, deliberately not pursued in this phase:** original-scope
full-trajectory dense-variability theorem, arbitrary data/depth validation,
general low-state Markov closure, and controlled moderate-amplitude error
for the cubic example. Accuracy of a training-mode reduction does not imply
accuracy of every passive orbit observable.

No discrepancy in this cohort requires changing the full causal equations.
The useful correction was to the explanatory approximation: do not use the
initial exponential fitting rate throughout feature learning. Evolve the
residual with the feature-enhanced response instead. The next discriminating
extension would break the two-sample symmetry, where there is no reason for
a single shared clock to remain adequate; that experiment has not been run.

## Reproduction and evidence

Sources: dense_learning_experiment.py, causal_population_simulator.py,
run_causal_experiment.py, analyze_learning_experiment.py and
compare_causal_experiment.py in this study. Run with single-thread BLAS and
PYTHONDONTWRITEBYTECODE=1. The dense source remained frozen throughout its
campaign; the population wrapper checks startup/end source hashes.

Every trajectory directory under
data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/
contains its configuration/provenance record and raw NPZ output. Main summaries
are analysis_v2/summary.json, comparison_v1/summary.json and
passive_comparison/summary.json. The passive Gaussian coefficients and complete
refinement record are in passive_quadrature/coefficients.json. The first analysis
attempt saved valid numerical results but failed only at plotting because
matplotlib was unavailable; analysis_v1 was preserved, and analysis_v2 uses
a Pillow-generated data plot. No trajectory was discarded or selected for
favorable agreement.

The final two-run population refinement and updated execution totals are in
final_manifest/refinement.json. final_manifest/sha256.json hashes the retained
raw trajectory arrays, configurations, analysis snapshots and numerical source
files. Earlier analysis counts are explicitly snapshots, not cohort sizes.

The four-panel figure is
[learning_mechanisms.png](../../data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/analysis_v2/learning_mechanisms.png).
Analytical details are in ANALYTICAL_LEARNING_PROFILES.md and
RESIDUAL_CLOCK_CHECK.md. EXPERIMENT_AUDIT_PLAN.md audits control meanings and
the dense implementation. CAUSAL_SIMULATOR_IMPLEMENTATION.md records the
population algorithm, memory, runtime and approximation boundaries.
CAUSAL_NUMERICAL_AUDIT.md separately audits the solver and later-time/passive
probe derivatives. EXPERIMENT_EVIDENCE_CHECK.md reconstructs the reported
metrics and their limitations from the frozen primary analysis snapshots.
