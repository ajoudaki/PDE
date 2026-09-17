# Frozen experiment design — 2026-09-14

## Question and competing outcomes

Does the autonomous closure predict the loss, hidden-activation Gram evolution
and final output of a wide nonlinear network when three sign changes occur
inside a 90-degree arc? Accurate agreement, visibly wrong predictions, and
numerically unresolved comparisons are separate outcomes. The experiment tests
these explicit finite approximations, not convergence of the hierarchy.

## Model and data

Use the established small-readout bias-free two-hidden-layer tanh architecture:
u(theta)=(cos(theta),sin(theta)), physical x=sqrt(2)u,
h1=tanh(W1 u), h2=tanh(W2 h1), f=c^T h2/n.
Initialization is independent Gaussian in layer order with variances 1, 1/n,
1/n^2 for W1,W2,c. Loss is the unhalved uniform mean squared residual; physical
block mobilities are (n,1,n). All blocks learn with simultaneous explicit Heun.
No bias, whitening, fitted clock correction or trajectory-derived coefficients.

Sixteen distinct deterministic training angles, four equally spaced in each
interval [0,5], [25,35], [55,65], [85,90] degrees. Cluster labels are respectively
+1,-1,+1,-1, as clarified by the user. Endpoint spreads are one-sided to retain
all points in [0,90]. Equal training weights 1/16. Evaluation angles do not
participate in training. The alternating target requires three sign transitions
in this arc, retaining a nonlinear task with strongly correlated inputs.

## Fixed run menu and observables

T=100, primary step h=.01, saved times 0,.5,...,100. Network widths 2048 and8192,
seeds 11,29,47 at each width, float32, TF32 disabled. Controls: width8192 seed11
h=.005 float32; width2048 seed11 h=.01 float64. All seeds use NumPy PCG64 draws
in float64 before casting, exactly as the maintained initializer. No seed selection.

Closure orders N=1,3,5: standard maintained initializer with Q=2048,P=1024 and
Q=4096,P=2048, float64, h=.01. Step controls: N=3 at base quadrature h=.005 and
N=5 at fine quadrature h=.005. Thus at most 8 network and 8 closure trajectories.
Main plots use all N at the same base quadrature; refined results are controls,
shown separately and reported even if they disagree.

Store loss, predictions, raw activation RMS and movement from initialization RMS,
and both complete activation Grams G_l(a,b)=mean_i h_l(x_a)h_l(x_b) (weighted
population expectations for closures). The observation panel concatenates the
16 training inputs and 128 equally spaced passive unit-circle directions.
Save final states and direct final predictions on a dense 1440-angle circle plus
training angles. Radial plot is (R+f(theta))u(theta), with common R=2 unless this
would make any radius nonpositive, in which case use R=max|f|+1, explicitly label
R. Include training locations at R and target markers at R+y. Also supply an
ordinary output-versus-angle plot, since a shared radial plot can hide errors.

Reference is the mean of the three width8192 realizations, with their spread;
loss reference averages losses, not the loss of the mean output. Gram errors
are ||Gclosure(t)-Gref(t)||_F/||Gref(t)||_F on training and passive-circle panels
separately. Compare to a frozen Gram baseline Gref(0); its error quantifies actual
feature evolution. A stronger fitting baseline freezes both hidden layers and
trains the readout with the same mobility, computed exactly using
f(t)=y+exp(-2t G2(0)/16)(f(0)-y), separately for each network realization.
Store initial/final and selected-time Gram heatmaps for both layers.

## Gates and decision criteria

Before scientific execution, verify GPU equations and a nonzero-state Heun step
against maintained finite-network velocity/forward and autograd, double precision
absolute discrepancy <=1e-10; verify Gram/RMS identities and closure observation
agreement with maintained predict. Check nonfinite values, symmetry and PSD
(min eigenvalue >=-1e-5), loss nonincrease up to 1e-5, exact data/schedules.
Failed correctness gates stop the affected implementation until fixed, with
failures retained. Deterministic implementation verification is allowed.

Step and float precision gates: maximum absolute loss/prediction difference
<=.005 and maximum relative Gram difference <=.01. Quadrature gate: corresponding
differences <=.02 and <=.03. Width discrepancy and seed range are reported as
uncertainty, not suppressed. These are modest diagnostic tolerances, not theorem
constants. Failed quadrature gates mean population accuracy remains unresolved;
computed finite curves can still be displayed honestly.

For each fixed closure, empirical strong agreement means maximum loss difference
<=.05, maximum relative Gram errors <=.10 on both training layers, and dense-circle
endpoint RMSE<=.10. A clear mismatch means any of these exceeds twice its threshold;
between these values is inconclusive. Quadrature and discretization uncertainties
qualify every interpretation. No monotone improvement with N is assumed. Report
actual continuous metrics regardless of categorical thresholds. Compare closure
Gram errors with frozen errors over the interval and at T without dividing by
near-zero evolution at t=0.

## Resources, provenance and stop

Use the two local RTX3090 GPUs for networks, CPU single-thread BLAS for closures.
Maximum two simultaneous GPU workers and two closure workers, 600 seconds per
worker, 20 minutes total scientific compute, 8 GiB generated-data cap and at least
3 GiB remaining disk. No outcome-dependent added seeds, orders, widths or horizons.
Stop after the fixed menu, or on budget/correctness failure; retain incomplete runs
and report gaps. Plotting/verification are bounded postprocessing, not new training.

Record explicit commands, environment, seed/dtype/device, source SHA256 hashes,
Git HEAD and used-source changes, input hashes, elapsed time, exit status and output
hashes. Fresh output directory run_001; never overwrite a consumed run. Preserve
unique implementation in the flat study, data/logs/checkpoints/figures only under
its generated namespace. Final README records evidence and limitations; no promotion.
