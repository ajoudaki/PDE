# Frozen first-pass experiment: angular spectrum versus learned geometry

User authorization: theory and new simulations for sparse points on the circle,
varying spacing, labels and point count. No prior study evidence is an input.
This plan is fixed before scientific training; source hashes will be frozen
when the validated worker and driver are complete. Research results remain
exploratory outside the maintained narrow-law theorem.

## Model and competing explanations

Same maintained two-hidden tanh closure, Gaussian initializer, physical
unhalved weighted MSE and simultaneous Heun, with normalized u=(cos theta,sin
theta), physical x=sqrt(2)u. Main N=1,2,3,5, Q4096/P2048, float64, h=.02.
N=0 is not supported and is not relabeled NTK. The separate true limiting
initial tangent kernel and each closure's own frozen initial kernel are
analytic frozen-feature baselines. No learned clock/amplitude/phase correction
is applied to a comparator.

H_frequency: higher N consistently increases normalized angular bandwidth.
H_geometry: N changes approximation of initialized-mark interactions; all
orders can create odd angular harmonics, and learned kernel geometry,
amplitude/overshoot and orientation explain differences better than a fixed
angular cutoff. H_initial: differences chiefly come from the initial kernel,
with negligible nonlinear feature adaptation. These are distinct empirical
hypotheses; no universal average-superiority theorem is presumed.

## Fixed cases, in waves

All input atoms have equal weights. Angles below are degrees, converted to
radians before evaluation. Two-point labels are [-A,+A].

Wave pairs: angles rotation+[-delta/2,+delta/2], A=1, delta in
[15,30,60,90,150], rotation=45; all four orders. Also rotation=0 at delta30,90,
all four orders. Thus 28 main trajectories. These are nonduplicate,
nonantipodal opposite-label inputs.

Pair controls: delta30,rotation45 at all four orders, both doubled Q/P and
half-step h=.01; delta90,rotation45 at N1,3,5 doubled Q/P. These 11 controls
retain the same physics and data. No extra parameter search follows failures.

Wave multi, permitted once the pair worker correctness checks pass and the
pair wave finishes within budget: smaller regression amplitude A=.2 at
pair delta30,90 rotation45, orders1,3,5 (6 runs); three-point angles
45+[-delta,0,+delta], labels[1,-1,1], delta20,40,60 at orders1,3,5 (9 runs);
four-point angles45+delta*[-1.5,-.5,.5,1.5], labels[-1,1,-1,1], delta15,30,45
at orders1,3,5 (9 runs). Controls at triple delta40 and quadruple delta30:
orders1,3,5 doubled Q/P and half-step (12 runs). Total maximum75 trajectories.
No width sweep is included in this first pass: this question compares the
specified closures and correct limiting frozen NTK, not a new neural-width
identification claim.

## Observations and stopping

Each trajectory starts from the maintained initializer, reaches at leastT100,
and is sampled every10 time units on 720 uniform circle directions plus its
training set. It stops after training MSE<=1e-6*A^2 and whole-circle max drift
<=.002*max(A,max|f|) over each of the last two20-unit windows. MaximumT600.
Mild finite settling is a diagnostic, not an infinite-time assertion. A run
at the cap without these gates remains explicitly unsettled. Training-fit
comparisons use relative MSE<=1e-4 and are also reported at common physical
T100; stopped times are never silently treated as common clocks.

Final1440-point predictions permit an independent half-grid spectral check.
Keep complete final frozen/dynamic state in lossless NPZ and exact data,
configuration, source/input hashes, environment, observation arrays and status.
Keep all failures and capped runs. No cleanup of another study is authorized.

Primary measurements: Fourier energy fractions in m=1, m>=3, m>=5, m>=7;
normalized RMS frequency sqrt(sum m^2|fhat_m|^2/sum |fhat_m|^2); mode attaining
99% energy; mean-zero/even-mode leakage; full-circle output amplitude and
overshoot versus label amplitude; circle RMS/max distances between orders,
true NTK and each own frozen-kernel prediction; training loss and final drift.
Normalized bandwidth, not raw slope or coefficient magnitude alone, tests
frequency use. Counterexamples to strict angular cutoff require tail energy
above1e-4 and ten times measured integration/step/grid uncertainty.

For each pair curve, fit diagnostic templates: first harmonic; odd Fourier
truncations through3,5,9; and one-parameter normalized tanh(k*sin(theta-mid))/
tanh(k*sin(delta/2)), times A, with k in[.02,30]. Template errors are measured
on the whole circle and an interleaved half grid; these post-training
reconstructions are descriptive, never new trainable baselines or claims of
endpoint optimization. Three/four-point curves use the fixed Fourier menu.

At initial/final state measure both hidden-layer Fourier energy, paired
hidden motion, training activation Grams, M singular values, and tangent-kernel
blocks on128 uniform circle directions. Fourier off-diagonal kernel energy
measures stationarity, including its initial coordinate/finite-rule error.
The finite-data training operator is not claimed Fourier-diagonal even when
the underlying kernel is stationary.

## Validity and interpretation

Worker fields/RHS/Heun, gradient metric and tangent blocks must agree with
maintained NumPy and independent autograd within1e-10 on declared finite test
states; exact lossless disk restart and prediction replay are required.
Reject nonfinite states, wrong source/data, significant loss increase above
1e-6*max(1,A^2), Gram PSD below-1e-8, or Fourier grid relative difference above
.005 for a bandwidth claim. Main/fine/half-step controls compare at T100 and,
separately, at their settled fits. Endpoint error thresholds: relative circle
RMS<=.02 for Q/P and<=.002 for step. Failed controls narrow findings to their
measured numerical witness; no claim of converged-order accuracy follows.

H_frequency is supported on a tested matched-fit case only when k_rms grows
by at least5% at each N1->N3->N5 transition and changes exceed three times the
control variation; reversed changes satisfying the same margins disfavor its
universal form. Near ties are inconclusive. H_initial is disfavored for a case
when learned/own-frozen relative circle RMS>.05 and paired hidden motion>.02,
with discrepancy exceeding five times numerical controls. Rotation discrepancy
uses f_rot(theta+rotation) vs f_base(theta) on common panels; a persistent
value>.02 is significant only above five times quadrature/step discrepancies.
N1/N2 proximity is tested and its ridge and finite-parity qualifications kept.
No winner selected after observing the circle is presented as preregistered.

## Hard resources and terminal stop

Scientific execution is at most1200 wall seconds from the first wave start,
at most120seconds per trajectory, two GPU workers and one CPU thread each.
New study output cap600MiB, minimum free disk1.5GiB. Existing outputs are not
removed. A budget or correctness failure stops dependent work; retain partial
status and report the actual obstruction. No automatic time/storage extension.
Postprocessing and final checks have at most five minutes and no new training.
Stop after the two waves or at the limits, with an honest unresolved conclusion
for any untested or numerically confounded proposed principle.
