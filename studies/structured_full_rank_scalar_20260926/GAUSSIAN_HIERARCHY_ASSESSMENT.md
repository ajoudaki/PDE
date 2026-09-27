# Gaussian-faithful initialization and efficient scalar dynamics

Theoretical continuation requested on 2026-09-26. No training or numerical
experiment was run. This report synthesizes three fresh scoped routes in this
study and their subsequent algebraic audit. It is not a promotion or a complete
proof of the target conjecture.

## Answer and target

A hierarchy satisfying both requirements is plausible, but a width-independent
polynomial accuracy–cost theorem has not been established. Full rank is not the
missing theorem: one must control repeated adaptive use of the initialized
matrix and its transpose, then efficiently approximate the resulting evolving
law. Plain HD has adverse empirical evidence on the clustered cosine-9 task;
this does not disprove every structured replacement.

The desired target is the canonical nonlinear two-hidden-layer tanh flow in
the README, with bounded normalized inputs and labels, fixed sample count m,
and every prescribed finite horizon T. The output metric is the supremum over
t in [0,T] of circle RMS difference from the canonical Gaussian population
output. Whole-circle uniform error is stronger and requires a separate spatial
regularity estimate. If that population object is not deterministic, its
limiting randomness must be coupled rather than independently redrawn.

The approximation must be autonomous and restartable, initialized only from
the prescribed initial law and dataset, and have state, coefficient storage,
and RHS cost independent of the original width n. Accuracy may determine an
initialization order k, a response-memory order P, and a representative count q.
One joint polynomial bound after selecting all these parameters is required;
polynomial cost with every other parameter held fixed is insufficient.

Two corrections to overly broad interpretations are necessary:

* Low-rank initialization alone does not force future gradients into a fixed
  subspace. Restricting learned weights to a frozen dictionary does. Gradient
  outer products may create new directions even from a low-rank initial matrix.
* Neither the existing experiments nor the scoped operator obstructions prove
  that Gaussian population observables admit no finite scalar approximation.
  The unresolved question is efficient approximation with controlled error.

## Concrete candidate: independent Gaussian blocks with global learning

For n=bk set

\[
W_0^{(k)}=\operatorname{diag}(G_1,\ldots,G_b),\qquad
(G_\beta)_{ij}\overset{\rm iid}{\sim}N(0,1/k).
\]

Each block and the entire matrix are full rank almost surely. Keep iid first
weights, the original canonical learning equations, and unrestricted learned
middle weights. The initialized matrix has O(nk) storage; that alone does not
remove width. At finite memory order P, the learned correction is a sum of mP
evolving outer products. Absorbing scalar coefficients into their factors,

\[
W=W_0^{(k)}+\frac1n\sum_{\ell=1}^{mP}a_\ell b_\ell^T,
\qquad
(Wh)_\beta=G_\beta h_\beta+
\sum_\ell a_{\ell,\beta}\left(\frac1n b_\ell^Th\right).
\]

The transpose has the corresponding formula with a and b exchanged. Thus all
initial-matrix reuse stays inside a k-neuron block, while learned interactions
couple every pair of blocks through scalar averages. The learned correction
is not constrained to the initial block pattern or frozen directions.

The exact fixed-k population description is a distribution of evolving blocks.
It is infinite dimensional. Approximate its expectations using q moving
representative blocks, all driven by the same residuals and global overlaps.
This yields an actual finite autonomous ODE with

\[
1+qk(d+1+2mP)\quad\text{dynamic scalars},\qquad qk^2\quad\text{static coefficients}.
\]

No n-neuron arrays survive. These are moving group characteristics, not an
exact closure of a handful of low-order moments. Each query input is evaluated
from the current block states and history contractions; test inputs need not
be inserted into training or predetermined on a mesh. The complete causal
equations and costs are in [BLOCK_HIERARCHY_ROUTE.md](BLOCK_HIERARCHY_ROUTE.md).

For the population convention the initial readout is zero: its finite-n
standard deviation 1/n vanishes. Using fresh finite-surrogate readout variance
1/(qk)^2 instead is an additional approximation and must be recorded.

## A genuine small positive rate, with its restricted scope

For one training input, let h=tanh(wu), Q=E[h²], and
Q_k=k^{-1} sum_{j=1}^k h_j². Conditional on the first features, every initial
second-layer block preactivation is exactly Gaussian with variance Q_k.
Define psi(v)=E[tanh²(sqrt(v)Z)] for Z standard Gaussian. With zero initial
readout and label y, the initial output velocities are

\[
\dot f_k(0)=2y\,\mathbb E\psi(Q_k),\qquad
\dot f_G(0)=2y\,\psi(Q).
\]

Write M=sup_z |(tanh²)''''(z)|, which is finite. The Gaussian heat identity gives
psi''(v)=E[(tanh²)''''(sqrt(v)Z)]/4, including the one-sided value at zero.
Taylor's formula, E[Q_k-Q]=0, and Var(Q_k)=Var(h²)/k give

\[
|\dot f_k(0)-\dot f_G(0)|
\le \frac{|y|M\operatorname{Var}(h^2)}{4k}
\le \frac{|y|M}{16k}.
\]

In fact M=16. Writing u=tanh²(z), direct differentiation gives
(tanh²)''''(z)=-8(1-u)(2-15u+15u²). The quadratic lies between -7/4 and 2
on [0,1], so the absolute value is at most 16, attained at zero. Thus the
last bound is simply |y|/k, uniformly over the input scale. The full
Gaussian differentiation justification is in the scoped audit note.

This is an actual O(1/k) initial training-velocity comparison. It does not
bound the trained trajectory. The repeated-action statistic also improves:
E[k^{-1}tr((G_k^TG_k)^2)]=2+1/k, whereas orthogonal HD has this statistic
identically one and the dense Gaussian limit is two. Neither statistic alone
is a training-output theorem.

## Exact outstanding bounds and the efficiency trap

For blocks bounded by ||G||op<=R, bounded data, fixed k,P,T, coupling sampled
blocks to iid population blocks gives a finite-observable estimate of the form

\[
\mathbb E\sup_{t\le T}|f_{k,q,P}(t,u)-f_{k,P}(t,u)|
\le C_{k,P,T,R}/\sqrt q.
\]

The route note provides the bounded-state estimates and the coupling/Gronwall
argument. A whole-circle extension needs spatial regularity and uniform
sampling control. These are separate from the initialization identification.

Crucially, spectral control alone does not make the stability constant
dimension free. The first-layer derivative contains the term
phi''(wu) Delta(wu) (G^T delta_2). Its multiplication-operator bound requires
||G^T delta_2||infinity, and the spectral estimate gives only R sqrt(k) times
||delta_2||infinity. The conservative constant therefore includes
exp(C_{P,T} sqrt(k)), rather than a polynomial in k. Adaptive sub-Gaussian
backward-field estimates might improve it; independence cannot be assumed
after training has reused G and G^T.

The other missing estimate is identification of the large-block population
law with the canonical Gaussian trained population:

\[
\|f_{k,P}-f_{G,P}\|_T\le C_{P,T}k^{-\alpha},\qquad \alpha>0.
\]

One block is a small dense network, but this does not prove
lim_{k->infinity} lim_{b->infinity} f_{b,k,P}
=lim_{k->infinity} f_{1,k,P}. A consistency estimate for an imposed-history
block response, plus stable self-consistency, is needed. Gaussianity of the
first multiplication and matching spectra do not establish this interchange.

For clarity, suppose both displayed identification and the stronger sampling
estimate C_{P,T} k^beta/sqrt(q) were established in the desired circle metric.
Then the triangle inequality would give

\[
\mathbb E\|f_{k,q,P}-f_{G,P}\|_T
\le C_{P,T}(k^{-\alpha}+k^\beta/\sqrt q).
\]

At fixed P, k of order epsilon^{-1/alpha} and q of order
epsilon^{-2} k^{2beta} give stored size of order
epsilon^{-2-(2beta+2)/alpha}, up to fixed structural factors. This is a
conditional illustration of the requested polynomial tradeoff, not a proved
rate. To reach uncompressed Gaussian training, add a width-uniform response
truncation error and include the growth in P of all constants and costs.
Fixed-width memory convergence cannot silently supply that final term.

## What the stronger fast-transform literature supplies

Wang, Zhong and Fan give generalized-invariant ensembles built from independently
scrambled delocalized orthogonal bases and a prescribed singular-value law.
Their Example 2.26, Proposition D.1(b1), Lemma D.9 and Theorem 2.22 support
fixed tree tensor-network/AMP universality under the stated hypotheses.
A Gaussian-matched candidate has two scrambled Hadamard bases around positive
diagonal singular values whose squares approach MP(1). It is full rank and
has O(n) storage and O(n log n) forward/transpose application. The covered
AMP theorem uses the appropriate Onsager coefficients; it is not a theorem
for arbitrary unmodified neural gradient flow. The source verifies a stronger
form of reuse agreement than matching spectrum alone.
[Primary source](https://arxiv.org/pdf/2206.13037).

The detailed source scope is in [FAST_HIERARCHY_ROUTE.md](FAST_HIERARCHY_ROUTE.md).
We have not imported a complete theorem for this study's tanh training flow.
Even such a universality transfer would leave the efficient scalar evaluation
of its history law to prove. This candidate addresses Gaussian faithfulness
more directly; independent blocks address finite representation more directly.

## Claim status and interpretation

| Claim | Status |
|---|---|
| Block initialization is full rank and admits exact forward/transpose block equations | Exact algebra |
| Learned corrections globally couple blocks and preserve moving features | Exact algebra |
| Block initial output velocity approaches the Gaussian value at O(1/k) | Elementary proved comparison, one sample |
| Fixed-k bounded-block particle error has a q^{-1/2} coupling route | Scoped finite-horizon estimate; constants may be exponential in sqrt(k) |
| Block hierarchy gives polynomial-cost Gaussian training approximation | Open |
| Fast spectral replacement has relevant published fixed-program universality | Source-supported in its stated scope; neural-flow transfer open |
| HD agrees with the Gaussian fitted function on clustered cosine-9 in the population limit | Disfavored by saved wide results, not disproved |
| Every scalar compression or every structured initialization must fail | Unsupported |

The strongest working conjecture is a randomized polynomial hierarchy for
fixed bounded tasks, fixed depth, and finite T, using moving block/history
representatives. The strongest unresolved issues are the joint stability
constant and Gaussian trained-law identification. An all-time or independently
stopped final-fit theorem needs additional long-time/crossing control.

The root checked the three scoped notes and corrected a preliminary claim
that operator-norm bounds alone gave dimension-free block stability. The
corrected dependence appears above. This is internal theoretical analysis,
not an independently reviewed proof of the target. No new empirical evidence
was generated. See also [EFFICIENT_HIERARCHY_AUDIT.md](EFFICIENT_HIERARCHY_AUDIT.md).
