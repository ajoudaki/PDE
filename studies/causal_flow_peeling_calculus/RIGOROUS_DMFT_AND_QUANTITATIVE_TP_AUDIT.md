# Rigorous DMFT and Quantitative Tensor-Program Audit

## Bottom line

The blanket statement “DMFT has no rigorous theorems” is false.  There are
rigorous bounded-time DMFT theorems for important first-order methods with one
random design matrix.  They do **not** cover the present deep, fully trainable,
multi-matrix network, and their limiting object uses two-time covariance and
response kernels.  They are therefore not an invocation-level solution to the
program contract.

Their proof architecture is nevertheless materially relevant.  In
particular, it cleanly separates:

1. a dimension-uniform exact-flow/Euler comparison;
2. a fixed-mesh Gaussian/AMP state-evolution theorem;
3. a contraction argument for the limiting response/covariance system; and
4. mesh removal and path-law tightness.

For the arctangent network, item 1 becomes routine after clipping the
unbounded backward multipliers.  The exact remaining problem is to remove the
hidden clip uniformly.  Rigorous DMFT does not make that obligation disappear.

## 1. Two rigorous references and their exact scope

### 1.1 Discrete rigorous DMFT

Gerbelot, Troiani, Mignacco, Krzakala, and Zdeborova prove a discrete-time
DMFT by iterative Gaussian conditioning for a class of first-order methods
with one Gaussian design matrix.  The result allows nonseparable update maps,
but the number of estimator columns is fixed and the induction is over each
fixed finite iteration horizon.  The paper explicitly restricts its theorem
to discrete dynamics and builds memory kernels in the effective recursion.
See the [published-paper preprint](https://arxiv.org/abs/2210.06591).

This is rigorous, but it is no stronger for our mesh problem than fixed-step
MFP: it does not supply uniform control as the number of gradient steps tends
to infinity.

### 1.2 Continuous-time rigorous DMFT

Celentano, Cheng, and Montanari prove compact-time convergence for flows
parametrized by one iid subgaussian `n x d` design matrix, with `n/d` tending
to a positive constant and a fixed number `k` of state columns.  Their
Assumption 1 requires the update `ell_t(r;z)` **and its Jacobian** to be
globally Lipschitz, uniformly in time and the auxiliary seed.  Their Theorem
1 proves existence and uniqueness of a sextet consisting of two effective
processes and two-time covariance/response kernels; Theorem 2 proves weak
convergence of empirical coordinate path laws on `C([0,T])`.  See the current
[full preprint](https://arxiv.org/abs/2112.07572).

The proof has two separate stability layers:

- at finite width, bounded source operator norm plus the global Lipschitz
  hypothesis gives a width-uniform Euler estimate;
- at the limit, exponentially weighted Volterra norms make the map between
  covariance and response kernels contractive, giving existence, uniqueness,
  and convergence of the discretized DMFT to continuous time.

This is a genuine rigorous DMFT theorem.  Its final state, however, is a
two-time memory system, and its finite-dimensional flow has a single random
design acting in the special first-order form covered by the paper.

### 1.3 Rigorous adaptive Langevin cavity and response convergence

Fan, Ko, Loureiro, Lu, and Shen prove path-space propagation of chaos and
convergence of averaged linear responses for an adaptive Langevin diffusion
driven by one random design through `X^T X`.  Their proof is fully rigorous:
it combines a fixed-step DMFT approximation, convergence of the discrete
DMFT fixed point to continuous time, and a direct finite-system
discretization estimate.  A separate dynamical leave-one-out argument
identifies the response kernels.  See the
[full 2025 preprint](https://arxiv.org/pdf/2504.15556).

The assumptions doing the stability work are explicit.  The scalar drift is
twice continuously differentiable with globally bounded first and second
derivatives, and the adaptive empirical-law map is globally Lipschitz with
controlled derivatives.  In the response proof, products of discrete
Jacobian matrices have uniformly bounded operator norm; the leave-one-out
remainders are then controlled coordinatewise and in averaged moments.

This is valuable confirmation that a dynamical cavity can rigorously identify
an order-one response kernel.  It does not discharge the present gate: the
depth-three arctangent network has the unbounded Hessian multipliers `A` and
`r_2`, multiple trained nested sources, and leading alternating two-color
response complexes.  The very uniform Jacobian bound used by the paper is
what fails here.  Its limiting description is also path/two-time based.

## 2. Why neither theorem applies directly

The depth-three feature flow violates the invocation hypotheses in several
independent ways.

1. It contains two independent persistent square Gaussian matrices, each
   queried in both forward and transpose orientation through nested
   nonlinear fields.
2. Every matrix is also trained by a rank-one update.  Eliminating the learned
   part produces self-consistent time integrals of forward and backward Gram
   kernels, not the paper's single `X^T ell_t(X theta;z)` form.
3. Before clipping, derivatives of the gate contain the unbounded multipliers
   `A` and the hidden response `r_2`.  The global Lipschitz-Jacobian assumption
   therefore fails; the rare-coordinate counterexamples show that it cannot
   be repaired by normalized energy bounds alone.
4. The rigorous limiting state is explicitly history/two-time based.  It can
   serve as proof scaffolding, but using it as the final answer violates the
   frozen one-time restartability contract.

Packing the layer sources into a block Gaussian matrix does not by itself
solve points 2--3: it changes notation, not the nonlinear update class or the
missing clip-uniform response estimate.

## 3. What can be reused faithfully

For fixed clips on `A` and every hidden `r_l`, mobility coordinates make the
network vector field dimension-uniformly bounded and Lipschitz on a source
operator-norm localization.  Consequently the finite-width Euler lemma from
the rigorous continuous-DMFT proof has a direct analogue:

\[
 \sup_{t\le T}\|X_n(t)-X_{n,h}(t)\|
 \le C_{K,R,T}h,
\]

uniformly in width.  Fixed-program MFP then evaluates every fixed mesh, and
the Euler-first Cauchy construction yields a unique clipped compact-time
limit.  This part needs no forest expansion.

The Volterra contraction proof is also a useful template for a **proof-only**
marked-cavity response system: introduce exponentially weighted norms, prove
the response map is a contraction from independently bounded primal
coefficients, and use the resulting kernel only to establish a clip-uniform
tail/occupation estimate.  The kernel may then be discarded when passing the
finite-width semigroup identity to the source-coupled one-time character.

The make-or-break condition is that the contraction constants be uniform in
the hidden clip.  The cited theorem obtains its constants from a deterministic
global Lipschitz bound.  In our model that bound grows with the clip, so a new
signed mobility/cavity estimate is necessary.  Calling the existing theorem
does not prove it.

## 4. July 2026 quantitative tensor-program result

Agazzi, Mosig Garcia, and Trevisan prove an `O(sum_m m^(-1/2))` Wasserstein
bound for each fixed Lipschitz Netsor program, with the constant depending on
the program's structural constants.  Their theorem supports repeated use of
the same forward matrix and quantitative empirical-kernel laws.  See the
[full preprint](https://arxiv.org/abs/2607.06290).

Three details prevent a direct growing-mesh invocation here:

1. program length and nonlinearities are structural constants, and the stated
   theorem gives no uniform modulus as the length tends to infinity;
2. the proof uses smooth dependence on finite Gram matrices after a
   nondegeneracy reduction, whose conditioning can deteriorate badly for the
   nearly collinear queries created by a fine time mesh;
3. the displayed Netsor language has forward `W h` MatMul instructions but no
   theorem-level transpose-MatMul rule tying `W^T` to the same source.  It
   therefore does not replace MFP for the exact forward/backward program
   without a new extension.

This paper can improve finite-width rates for a compatible clipped subprogram,
but it does not supply the missing mesh-uniform or hidden-clip-uniform theorem.

## Strategic verdict

Rigorous DMFT should not be ignored.  Its reusable contribution is the
Euler/AMP/contraction architecture and, especially, the idea of bounding a
proof-only response system in an exponentially weighted Volterra space.  It
is not an API-level solution.  A successful adaptation must prove one new
multi-layer theorem: a marked-cavity/response contraction whose constants are
uniform in the hidden clip and whose output is a current-time occupation or
tail certificate.  If that theorem cannot be proved without assuming the
desired adaptive-source stability, then the DMFT-inspired route is merely the
original obstruction in two-time notation and must be rejected.
