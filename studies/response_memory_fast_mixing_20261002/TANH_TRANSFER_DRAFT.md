# Candidate bridge from Lipschitz iteration universality to the actual learner

Author derivation, 2026-10-02. **Conditional draft, not an established theorem.**
The matrix-iteration universality premise below still needs a complete proof
or verified external import. This file isolates a possible way around the
unbounded backward-response product; it must not be read as closing the
external universality gap. No experiment or other study is a proof dependency.

## Target and remaining premise

Use exactly the two-hidden-layer tanh q=1 equations in TRAINING_PROTOCOL.md,
with raw moment rows H_a,D_a, first matrix A, readout w and tau>=1. Let m,d,
the training/query list, labels, positive step size eta and number J of Heun
steps be fixed independently of width n. Compare iid Gaussian W0 with the
four-signed-permutation Hadamard ensemble having asymptotically quarter-circle
singular values. Initial A has iid N(0,1) rows; w=D=0, H=h(0),tau=1.
Only predictions and bounded empirical feature observables at these finitely
many times are targeted, not uniform ODE time or all-time fitting.

**Unproved premise (P).** For these two matrix ensembles, every fixed finite
computation using W0/W0^T, independent Gaussian/constant initial coordinate
channels, globally Lipschitz coordinate maps of the full past, and continuous
Lipschitz scalar feedback from bounded empirical coordinate averages has
identical deterministic limits for its bounded empirical observables.
Redundant and initially zero channels are permitted. Operator norms are
uniformly bounded with probability tending to one.

Wang--Zhong--Fan's literal AMP theorem is narrower than this formulation.
A possible proof embeds the computation into an alternating AMP with history,
adds back its deterministic Onsager terms inside the coordinate maps, and
regularizes zero covariance channels by independent Gaussian innovations of
size epsilon. Scalar feedback is frozen at its recursively identified limits;
finite-step Lipschitz stability then removes that freezing and the epsilon
perturbation. Each step of this reduction, including the rectangular ordering
and positivity of regularized covariances, remains to be verified. The
polynomial computation-tree corollary does not by itself imply (P).

Conditional on (P), the following clipping argument is a proposed transfer
proof for the ACTUAL tanh equations. Its point is that no all-moment bound for
an adaptive backward field needs to be presumed.

## Deterministic finite-step bounds

Write Y=max_a |y_a|. If |w_i|<=M at a stage then |f_a|<=M and |r_a|<=M+Y.
Consequently |dot w_i|<=2(M+Y). One Heun step gives the coordinate bound

    M_next <= (1+2 eta+2 eta²) M + (2 eta+2 eta²)Y.

The same bound holds when any read-in backward channel is clipped, because
only bounded h,g enter this estimate. Starting at M=0 supplies a bound for
every stage depending on eta,J,Y, not n or the clipping thresholds. It bounds
rho, and hence tau between1 and a finite constant. Since |h_i|<=1,
|dot H_ai|<=rho; since |delta_ai|<=M,
|dot D_ai|<= (M+Y)M. These yield uniform coordinate bounds for H,D at every
full or predicted Heun stage, again independent of clipping thresholds.

The reconstructed transpose action is

    W0^T delta_a - 2 sum_b H_b (D_b^T delta_a)/(mn tau).

Its second term has a uniform coordinate bound from those moment bounds.
The first term p_a=W0^T delta_a satisfies

    ||p_a||_2/sqrt(n) <= ||W0||_op M.

Thus, on ||W0||_op<=C, at most n C²M²/R² coordinates have |p_ai|>R.
This is deterministic and does not use independence of p from W0.

## A bounded metric for the read-in

Ordinary normalized Frobenius distance of A is unnecessarily strong for
bounded feature/prediction observables. Define

    d_A(A,A')² = (1/n) sum_i min(||A_i-A'_i||_2²,1),

where A_i is row i. Together with normalized Euclidean distances of bounded
w,H,D and absolute tau distance, this defines a product metric on the
scientific states. In this metric h_a=tanh(Ax_a/sqrt(d)) is Lipschitz, with a
constant depending only on the fixed input. Both activation derivatives and
bounded products of coordinate channels inherit corresponding bounds.
For rows, the elementary inequality

    min(||a+v-a'-v'||,1)
       <= min(||a-a'||,1)+||v-v'||

permits read-in updates to be bounded without controlling large row values.
The original and clipped algorithms have the same Gaussian A0.

At an individual RHS evaluation replace p_a by clip(p_a,[-R,R]) ONLY in the
read-in velocity. At a common input state, this changes the read-in update
only in rows where at least one of the m p_ai exceeds R. Therefore its local
error in d_A is at most sqrt(m) C M/R, times a fixed finite number of row
updates if the evaluation is implemented as separate Heun instructions.
The amplitude of the changed row is irrelevant to this metric. Other
state components at that instruction are unchanged.

The clipped update is Lipschitz in the product metric. For example the
read-in product difference can be split as

    phi'(a) clip(p,R)-phi'(a') clip(p',R)
     = [phi'(a)-phi'(a')] clip(p,R)
        +phi'(a')[clip(p,R)-clip(p',R)].

The first term is bounded by a constant times R d_A, and the second by the
normalized L2 difference in p, which is at most C times the difference in
delta. Forward matrix actions similarly cost C; all reconstructed memory
coefficients are empirical products of bounded channels. Thus each clipped
instruction has a finite Lipschitz constant depending on R and fixed data,
but not n or the incoming values of A. Bounded-state extensions of w,H,D,tau
make its coordinate maps globally Lipschitz without changing valid paths.

## Why different thresholds are used at different instructions

A single threshold R with an error estimate R^J/R would not prove anything.
Instead enumerate the finite Heun computation chronologically and telescope
from the original program to the fully clipped one by replacing its
instructions from LAST to FIRST. When replacing instruction j, its suffix
already consists of clipped instructions with fixed finite Lipschitz
constants L_(j+1),...,L_N, whereas its prefix may still be unclipped.
The deterministic coordinate bounds above hold for every such hybrid.

For a requested total observable error epsilon, choose the final threshold
R_N large enough, then R_(N-1), and so on backwards, so that

    (sqrt(m) C M_j/R_j) product_(k>j) L_k <= epsilon/N.

All thresholds are finite constants chosen independently of n. Summing the
N hybrid comparisons bounds every requested bounded Lipschitz observable
difference by a fixed multiple of epsilon, under either matrix ensemble.
Both full and predicted Heun states must be included in this straight-line
instruction enumeration; they are not silently identified.

The fully clipped program is covered by (P). Its empirical observables have
the same deterministic limit for the two ensembles. For a sequence of
tolerances tending to zero, the preceding deterministic comparison makes
these common limits Cauchy and forces the original bounded observables to
have the same limit. The exceptional operator-norm event has vanishing
probability. Thus the conclusion is convergence in probability unless an
almost-sure eventual norm bound and countable probability-one construction
are additionally supplied.

## Outstanding audit obligations

1. Prove/import premise(P) in full. This is the principal missing step.
2. Formalize the finite straight-line Heun hybrid state, including both stages
   and all reused buffers, and verify the d_A Lipschitz bound for each instruction.
3. Specify the desired bounded empirical observables: predictions, sample
   feature Grams, and bounded state test functions qualify; unbounded A moments
   and the entire physical parameter trajectory are not supplied by this metric.
4. Retain fixed m,d,J,eta. No exchange of width and physical-time limits follows.

The same finite-instruction argument could cover an explicitly unrolled dense
gradient method. Any useful response-memory distinction concerns its bounded
history representation and implementation, not exclusive universality.
