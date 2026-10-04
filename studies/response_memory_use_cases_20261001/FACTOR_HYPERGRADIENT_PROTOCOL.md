# Moving low-rank factor hypergradient control

Precommitted 2026-10-01 before implementation or fitting. This is an authorized
post-confirmation adversarial control, not a fresh blind confirmation. Inputs
are the frozen `baseline_compact_flow.py` and `hypergradient.py` implementations
and `HYPERGRADIENT_PROTOCOL.md`. No other studies or route outcomes are inputs.
The canonical-notation and investigate-conjectures skills govern this addition.

The decision is whether a conventional nonlinear low-rank learner of the same
moving-state size can design useful labels. A successful control would weaken
an attribution of label-design utility specifically to response memory. A poor
control would establish only the tested comparison; it cannot rule out other
factor initializations, ranks, optimizers or learning rates.

For eight support inputs x_a=(cos(theta_a),sin(theta_a)), theta_a=2*pi*(a+.13)/8,
use teacher sin(3*theta)+.4*cos(theta), 32 outer angles shifted by .37 grid cells,
and 256 test angles shifted by .71 cells. Width is n=512; Gaussian hidden-weight
initialization seeds are 201 and 202. The two hidden layers use tanh, exact zero
readout c, and no biases or additional input normalization. The inner loss is
unhalved mean square error over eight examples.

The control state is W1 in R^(n x 2), c in R^n, A in R^(n x 8), and B in
R^(8 x n). Its second matrix is W2=W2,0+AB, with fixed Gaussian W2,0 of variance
1/n. Its forward pass is h1=tanh(W1*x), h2=tanh((W2,0+AB)*h1), f=c^T*h2/n.
W1 and c have mobility n; A and B have mobility lambda, with all three values
lambda=.25,1,4 reported separately. Lambda=1 is exactly source `LowRankFlow`.
A initializes at zero; B uses NumPy default_rng(20260924) standard normals
divided by sqrt(8), exactly as in that source. Thus the moving state contains
19n=9728 coordinates, versus 19n+1=9729 for order-one response memory with
eight supports. Both retain the full fixed n-by-n Gaussian second matrix.
Initializers and unrolling/checkpoint buffers are counted separately where
applicable; matching moving coordinates is not a claim about peak memory.

Labels start at the teacher values. Each design uses exactly 24 Adam steps,
learning rate .05, clipping labels to [-3,3] after every step. Inner integration
is Euler at dt=1/32 through T=8, differentiating through all 256 steps. No
stopping-time, rank, horizon, task, initialization or optimizer search occurs.
Final labels are selected without test access.

The primary observable is test mean square error after **dense retraining**
with the original identical Gaussian initialization and the designed labels,
divided by dense test error with original labels. The factor learner's own
outer and test losses, its prediction discrepancy from dense, hidden-activation
movement and compute/storage costs are separate diagnostics. Every rate and
seed is retained; no favorable rate is declared a winner. The parent study may
compare these fixed controls with its already-frozen response-memory result.
For this report, a dense error ratio at most .8 is useful improvement, a ratio
at least .9 fails the original 20% improvement threshold, and intermediate
values are inconclusive. These categories make no superiority claim.

Before fitting: in float64 at n=32, compare every state coordinate and query
prediction against LowRankFlow at one and 32 Euler steps, tolerance 1e-10,
for lambda=1. For each lambda, also compare the analytic velocity with an
independent materialized-network autograd loss gradient at a nonzero factor
state. At T=1, check a label directional hypergradient by central differences
with epsilon=1e-4 and 5e-5, relative disagreement at most 1e-4. Nonfinite loss,
gradient or final state invalidates the corresponding fit. Main precision is
float32; CPU threads are one and TF32 is off. GPU1 is the sole device used.

After each final design, replay dense training at dt=1/32 and 1/64. Record
the original-label dense baseline at both steps. Report whether improvement
persists under refinement and whether MSE sensitivity is below 10% of claimed
improvement. Factor own-objective evaluation uses the original dt; no factor
step-size optimization follows a bad outcome.

Hard budget: 180 inner solves and five GPU-minutes. Planned count is 144
optimization solves, six factor final replays, twelve dense final replays,
four dense original-label replays =166 main solves. Validations run on CPU
and **still count**: one lambda=1 directional finite-difference validation
(five short solves), plus functional and source parity trajectories (two
short solves), totaling173 solves. Independent velocity checks at all three
rates use no inner integration. Stop before any operation that would exceed
180 solves or five minutes of allocated GPU process time. No new scientific
branch is authorized after results. Save exact code and protocol snapshots,
hashes, commands, environment, timestamps, per-iteration losses and every
attempted final label vector.
