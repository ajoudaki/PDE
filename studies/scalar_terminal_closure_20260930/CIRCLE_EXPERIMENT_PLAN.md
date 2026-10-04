# Width-1024 circle comparison: frozen terminal scalar response

Precommitted before implementation/training, 2026-09-30. The user explicitly
requests an executed scalar-ODE versus dense n=1024 test on the repository's
circle tasks, including unseen-circle predictions at the end of training.
This continues the scalar-terminal study. Other unpromoted studies are not
inputs. The paper's portable circle bundle is an authorized manuscript input.

## Decision question and comparisons

Does the terminal scalar continuation accurately predict the remaining q=1
loss and unseen-input function, and how close is the resulting function to
a dense network trained on identical data and initialization?

The three models are dense physical gradient flow, the exact finite-width
q=1 system, and the proposed scalar continuation initialized from a q=1
handoff. A static prediction at handoff is the matched no-continuation control.
Comparing scalar to q=1 isolates second-compression error; comparing q=1 to
dense isolates the first-closure discrepancy. Dense and q=1 remain distinct.
The scalar model does not claim initialization-only compression.

H1: sufficiently late scalar continuation adds little error to q=1 while
improving over retaining the unchanged handoff function. H0: loss fitting
alone does not preserve the unseen function; scalar continuation may have
material query error even when its training residual converges.

## Fixed scientific configuration

Use all five two-hidden-layer circle tasks from the paper portable bundle:
two_outliers_alternating, quadrant_alternating, quadrant_pairs,
quadrant_center_edges, equal_mixed_odd. Each has eight training points.
Exact stored angles/labels and source hashes will be copied to study-owned
circle_task_inputs.json before training. Physical x=sqrt(2)(cos theta,sin
theta); implementation stores u=x/sqrt(2), with no second normalization.

Width is 1024, activation tanh, no biases. Draw A_0~N(0,1) and independent
W_0~N(0,1/n) using NumPy default_rng seed 20260920 in that order; use exactly
the same arrays in dense and q=1 and across tasks. Stored readout is exactly
zero in both models, matching this study's q=1 definition. Historical paper
figures used width 2048 and small random readout; these runs are new matched
comparisons, not reproductions of those archived endpoints.

Dense mobility is (n,1,n), unhalved mean square loss. Thus with normalized
inputs u, dense velocities are

    wdot=-2 g r/m,
    Adot=-2 (ell*r) u.T/m,
    Wdot=-2 (d*r) h.T/(mn).

q=1 uses the exact README/terminal-theorem equations including moving keys,
the activity clock, and both actions of the same fixed W0. No Gaussian
resampling, PSD projection, clipping or dense-retrained substitute is allowed.

The primary handoff is first checked q=1 training MSE <=0.01. Fixed secondary
handoffs at MSE <=0.1 and <=0.001 test earlier/later truncation. Capture all
three during one q=1 trajectory; never choose the best after inspection.
There is one seed and five prespecified tasks, no favorable-task selection.

## Autonomous scalar predictor on the entire circle

For each handoff retain the exact m-by-m training response C and norm-drift
b from TERMINAL_SCALAR_THEOREM.md. Evolve rdot=-Cr+||r||b. Append the m
integrated residuals (derivative r) and the integrated residual norm
(derivative ||r||), all zero at handoff. This gives 2m+1=17 moving scalars.

At a query x, the exact output derivative has the same cross-response form:

    fdot(x)=-sum_a C(x,a) r_a + ||r|| b(x).

Freeze these query coefficients and the initial query output at the handoff.
Then the query prediction is its handoff value minus C(x,:) times integrated
residual plus b(x) times integrated residual norm. This is the theorem's
passive-observable extension, sharing its integrated controls across queries.

Represent the m+2 query coefficient functions (handoff output, m columns
of C, and b) by exactly 32 odd Fourier frequencies 1,3,...,63, with cosine
and sine coefficients. No constant/even modes are kept: the bias-free tanh
predictor and its query response are odd under x -> -x. Form coefficients
from 2048 uniform angle samples at handoff. No future target outputs or
unseen labels enter their construction. Validate independently on 8192
midpoint-shifted uniform circle queries.

For m=8, fixed model numbers are 64+8+10*64=712; evolving numbers are 17,
total 729 (optional labels/metadata reported separately). The query panel
is evaluation output, not retained model state. This one-width count is
not an asymptotic o(n) theorem. Initialization/handoff still uses full q=1
states and the fixed dense mixer; report that cost explicitly.

Save also untruncated frozen query coefficients on the diagnostic panel to
separate Fourier-representation error from terminal-freezing error. Those
diagnostic arrays are not part of the deployable scalar model. The 32-mode
model remains the primary result even if its spatial approximation fails.

## Integrators, validity and endpoints

Use float64 throughout. Dense and q=1 are integrated by simultaneous RK4
with coarse step 1/8 and an independent refined run with step 1/16, each
starting from the exact same initializer. No adaptive learning-rate tuning.
The coarse run stops when both models have MSE <=1e-7 at a common physical
time, or at physical time 512. The refined run reaches the same final time
and captures handoffs at the identical coarse-selected times, avoiding
spurious switch-time differences in the refinement comparison. A settled
fitting comparison requires both refined final losses <=1e-6; otherwise
report an unfinished fit at the recorded horizon.

Scalar systems use SciPy DOP853 with rtol=1e-10, atol=1e-12, and their own
residual feedback. They are compared to full q=1 at equal physical times.
This is numerical ODE integration, not exact dynamics or a GD theorem.

Validity gates: finite states throughout; dense RHS parity with maintained
finite_network on tiny deterministic instances; q=1 train/query derivative
identity checked by central directional differences; Fourier reconstruction
and shared-integral observer checked independently. Refinement requires
endpoint circle RMS change <=0.002 for dense and q=1 and <=0.002 for the
primary scalar prediction, and maximum observed common-time training-loss
change <=0.001. Report measured values and gate failures, not just PASS.

If a refinement gate fails, run only that task once more at step 1/32 up
to the same final time, within the total budget. Use 1/16 versus 1/32 as
the valid comparison only if the same gates pass. No further refinement or
scientific parameter changes are authorized by this plan. If coefficients
are not contractive, record it; do not alter them. Actual terminal tube
bounds are not certified by an eigenvalue diagnostic alone. The antipodal
task additionally reports the margin restricted to its odd residual space.

## Metrics, decision thresholds and controls

Report all five tasks and all three handoffs, including failures:

* Training loss curves at common times, scalar-vs-q1 absolute loss error.
* Final circle RMS and maximum prediction errors: scalar-vs-dense,
  q1-vs-dense, scalar-vs-q1, and static-handoff-vs-q1.
* Sign disagreement with the dense reference; also disagreement away from
  |dense prediction|<0.05. These are imitation diagnostics, not test error
  against an unknown ground-truth label function.
* Scalar-vs-q1 Fourier truncation contribution, full-query tail movement,
  frozen coefficient contraction diagnostics, handoff/endpoint losses and
  times, state counts, timings, peak RSS, and source/environment provenance.

Predeclared useful-fidelity threshold for the requested dense comparison:
circle RMS <=0.05 and sign disagreement <=1%. For the second-compression
step: scalar-vs-q1 circle RMS <=0.01 and maximum error <=0.05. A meaningful
improvement over static handoff is RMS reduction by at least factor two
when static tail movement exceeds ten times the numerical sensitivity.
These are experimental decision thresholds in label units, not theorem
constants. Passing training loss alone is not a pass for unseen outputs.

Report finite-grid evidence, not a uniform whole-circle certificate or
an exact infinite-time endpoint. No unknown test labels are manufactured.

## Hard budget and artifacts

One sequential CPU training worker, at most two BLAS threads, 4 GiB working
memory, 3600 seconds cumulative training/analysis wall time, at most ten
baseline task/resolution pairs plus five triggered refinements. A bounded
performance-only matrix/RHS timing probe and tiny deterministic checks may
run before training; they cannot change task/seed/thresholds. Stop at the
budget or declared terminal condition and retain partial failures.

Source and checks stay in this study. Every execution uses a fresh run
directory under data/generated/scalar_terminal_closure_20260930/. Save
configuration, source and input hashes, initial/final states, handoff states
and coefficients, observations, endpoint curves, environment, commands and
exit status. Plot loss trajectories and final signed outputs around the
circle with training points; show all tasks, consistent scales and clear
model labels. Update the study README and empirical report. No paper,
maintained book/code, Git index, commit or push is part of this experiment.
