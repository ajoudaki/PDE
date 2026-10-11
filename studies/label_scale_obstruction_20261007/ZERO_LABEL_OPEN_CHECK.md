# Independent check: open zero-label extension

## Verdict and frozen scope

**PASS.** ZERO_LABEL_OPEN_EXTENSION.md proves unconditional
high-probability fitting of the actual finite-width, fully trained
gradient flow on the specified open neighborhood in dimension four.
It proves eventual exponential loss decay, not merely small loss at
a fixed time or convergence of a population reference.

The active pair has arbitrary fixed amplitude. Other label coordinates
belong to a positive-radius neighborhood of zero; the first two label
ratios also remain close to the specified opposite-sign pair. This is
not an arbitrary-label theorem. The common deterministic time and rate
apply to each fixed dataset in the neighborhood. No simultaneous
probability event over all datasets is asserted.

This is an internal mathematical check, not promotion. No blocking
mathematical issue was found.

The complete candidate was read at SHA-256:

    a6990d3a43e773455f560274acc5abba57c9b5693a657e0a3f0d95c0937b41f0

Only its authorized status line was changed to “internally checked
theorem”; all mathematical text was left unchanged. Its final hash is:

    5cbd8ffa45eca9f2bc7be0f277dde2700aa52366c5bc8c8dafa25a5371da6556

The complete authorized dependencies were:

- GAUSSIAN_POSITIVE_GEOMETRY.md:
  d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574
- GAUSSIAN_NONORTHOGONAL_EXTENSION.md:
  37a4f9fea1e64c2404c066358a82f2611f733c6496512d6179bef501424f9b11
- Maintained docs/12-three-sample-learning.qmd, III.F.1–11.

No other reviewer findings, other study, experiment, new active-$k$
extension, or current revised zero-label base theorem was used. The
ridge-independence assertion cited to INTRINSIC_SYMMETRY_ROUTE.md was
verified directly below; that file and UNCONDITIONAL_POPULATION_ROUTE.md
were not read.

## 1. Exact equations and normalization

For unit inputs, the network is
$U=\tanh(AX)$, $H=\tanh(WU)$, $f=H^\top w/n$,
$r=f-y$, and $\mathcal L=\|r\|_2^2/m$.
The mobilities $(n,1,n)$ give exactly (7), including the outer first
gate in $\dot u_b$ and the factor $1/n$ in $\dot W$.
The kernel formula (8), its positivity, and
$\dot r=-(2/m)Kr$ are correct.

In the parameter metric

$$
\|\Delta\theta\|_{\mathrm{par}}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|_2^2/n,
$$

the squared speed is $-\dot{\mathcal L}$.
For $\|v\|_{2,n}=\|v\|_2/\sqrt n$, the rank-one operator is
$b\otimes u=bu^\top/n$, with ordinary Frobenius norm
$\|b\|_{2,n}\|u\|_{2,n}$. Thus all tangent-feature normalizations agree.

The reference trains two samples while retaining denominator $m$.
Its time in the usual two-sample normalization is $2t/m$.
Its feature clock satisfies

$$
\dot s=\frac4m(a-g),\qquad
\frac2m\int_0^t
 (|\widehat r_1(v)|+|\widehat r_2(v)|)\,dv=s(t)
$$

at the population level. The rate in (13) and the clock bound (14)
therefore have the correct factors.

The clock bounds (10) follow by integrating $p_n'$ and $p_np_n'$.
They apply to the actual full residual and, separately, to the active
reference coefficients using the active reference loss. Together with
the first-layer velocity they preclude finite-time escape of the
smooth finite-dimensional ODE.

## 2. Conditional Gaussian queries and passive Gram

Condition on $\sigma(A_0e_1,A_0e_2,W_0)$. The evolving active reference
variables, $\bar W$, and $\bar w$ are measurable with respect to this
sigma-field. Passive-plane projections of $A_0$ are independent of it
and iid across neurons. The frozen full first-layer matrix contains
these unused roots, but is not what is meant by the active trained
state in this conditioning argument.

For a fixed passive input and time,

$$
F(G)=n^{-1}\bar w^\top\tanh(\bar W\tanh G)
$$

is an odd function of an independent standard Gaussian vector.
It has conditional mean zero and gradient norm at most
$\|\bar W\|_{\mathrm{op}}\|\bar w\|_2/n$. Gaussian Poincare gives
the claimed conditional variance $C_T/n$. Conditioning additionally
on the initialized middle-norm event does not alter those roots.

The passive first features are constant under the reference, so the
displayed time derivative bound for $\bar f_b$ has no missing
first-layer term. A finite grid, the variance bound, and this
width-uniform time Lipschitz bound prove $q_n(T)\to0$ in probability.
Neither independence between passive queries nor independence across
times is needed.

Conditional active–passive first-feature inner products have mean zero
and variance at most $1/n$: their active coefficients are fixed and
bounded, and passive rows are independent, centered, and bounded.
Thus the block-diagonal Gram limit used in (19) is valid.

For completeness, passive covariance positivity needs no additional
source. Choose a direction with nonzero projections $\alpha_b$ having
distinct squares. The excluded directions lie in finitely many proper
hyperplanes because the passive inputs are distinct and nonantipodal.
All odd Taylor coefficients of tanh are nonzero: writing
$\tanh t=\sum_{j\ge0}c_jt^{2j+1}$, its differential equation gives
$c_0=1$ and

$$
(2j+1)c_j=-\sum_{p+q=j-1}c_pc_q\quad(j\ge1).
$$

Inductively $(-1)^jc_j>0$. A linear relation among
$\tanh(\alpha_bt)$ then gives a Vandermonde system in the distinct
$\alpha_b^2$, multiplied by the invertible diagonal entries $\alpha_b$.
Every coefficient is zero. Continuity and full Gaussian support
convert a zero Gaussian quadratic form into this pointwise relation.
Hence $Q_{\mathrm{pas}}\succ0$ even for a singular passive input Gram.

## 3. Endpoint first-feature and middle-kernel gaps

The orthogonal dependency constructs a strong scalar feature path to
the finite endpoint $g=a$. For opposite labels, exchange/sign symmetry
makes the active first-feature eigendirections common and contrast.
The natural-coordinate nonextinction estimate preserves
$\|\xi_1+\xi_2\|_2>0$ on the finite feature interval. Oddness and
injectivity of $\psi=\tanh\circ\zeta^{-1}$ give $u_1+u_2\ne0$.
The other direction is nonzero because $u_1=u_2$ would imply
$h_1=h_2$ and contradict $g=a>0$.
Thus both active eigenvalues and the combined endpoint margin
$\mu_*$ are positive.

The reference readout normalized norm is at least $a/2$ at late fixed
times, since the active contrast prediction is bounded by that norm.
With readout supremum $S$ and action bound $M$, at most $a^2/8$ of
its squared readout mass lies where
$|\bar z_b|>\sqrt8SM/a$. Therefore, for every sample,

$$
\|\bar b_b\|_{2,n}^2
\ge (a^2/8)\operatorname{sech}^4(\sqrt8SM/a)=\beta_*>0.
$$

Schur positivity gives
$\bar K_W\succeq(\mu_*\beta_*/2)I=\lambda_*I$.
This covers all passive directions as well as the active ones.
The endpoint constants $S,M,\mu_*,\beta_*,\lambda_*$ do not deteriorate
when one subsequently chooses a later fixed time.

## 4. Active backward-tail dependency

The tail theorem in the complete nonorthogonal dependency, Sections
3–4, was checked directly because it is substantive here:

- Orthogonal natural coordinates remove the dangerous first-gate
  derivative from the sensitivity equation.
- With $W_0=Q/\sqrt n$, a general matrix perturbation has forcing
  $O(\|\Delta Q\|_F)$ in unnormalized state variation, whereas a
  single-entry perturbation has forcing $O(n^{-1/2})$.
- The sensitivity constant grows at most exponentially in
  $\|Q/\sqrt n\|_{\mathrm{op}}^2$. The stated Gaussian operator
  tail gives its uniform expectations for sufficiently large widths.
- Integration by parts includes the learned middle increment. Its
  coordinatewise rank-one integral is uniformly bounded, so the mean
  bound on each active reverse coordinate is valid uniformly in
  conditioned first-layer roots.
- Lipschitz extension from the convex initialized norm ball,
  Gaussian concentration, and an exponentially negligible bad event
  give the asserted dimension-free coordinate tails.
- Orthogonal fixed-program convergence identifies deterministic
  empirical tail norms. Fatou bounds those limits. A normalized
  time derivative bound and a finite time grid give uniformity on
  each fixed interval.

The fixed-program hypotheses also hold: $\zeta(G)$ has finite second
moment; root generation itself need not be Lipschitz; clipped
coordinate instructions have bounded derivatives; learned actions
unroll into the original Gaussian matrix, its transpose, and scalar
contractions; and the mesh is fixed before the width limit.
No independence between a trained matrix and its adaptive reverse
query is assumed.

Replacing the second active input by its negative changes its label
to positive but leaves the parameter loss unchanged. Its top gate,
and hence $b_2,B_2$, are unchanged. Thus the supplied equal-sign tail
proof applies to this opposite-sign pair after the stated time
rescaling. Adding unused passive roots changes no hypothesis.

## 5. Only active tails enter the comparison

The reference coefficient vector $\widehat r$ is correctly distinguished
from its evaluated full residual. Exactly,

$$
r-\widehat r=(f-\bar f)-(y-y^0)
 +(0,0,\bar f_3,\ldots,\bar f_m).
$$

This proves (26). The forward and upper-backward bounds (25) follow
from the normalized error, bounded operator norms, and the
pointwise-bounded reference readout. In particular,

$$
\|b_b-\bar b_b\|_{2,n}
\le\|w-\bar w\|_{2,n}
 +2\|\bar w\|_\infty\|h_b-\bar h_b\|_{2,n}.
$$

Subtracting the first-feature velocities in the order
$\Gamma$, residual coefficients, $B$, and finally gates leaves
exactly

$$
\Gamma^0_{bc}\widehat r_c
 (D_bD_c-\bar D_b\bar D_c)\bar B_c.
$$

It vanishes for every passive index $c$. All previous differences
contribute at most $C_T(E_n+\delta^2+q_n(T)^2)$ to $E_n'$.
For the two remaining indices, the region $|\bar B_c|\le2R$
contributes $C_TR E_n$. On the complement, bounded feature
differences and
$|\bar B_c|\mathbf1_{\{|\bar B_c|>2R\}}
\le2(|\bar B_c|-R)_+$
give precisely the tail-norm remainder in (28).
No passive reverse-field tail term is missing.

Passive residuals, including nonzero perturbed passive labels, still
enter the actual full dynamics through the ordinary difference terms.
Nothing is frozen in the actual network.

The initialization comparison follows from
$A_0^\top A_0/n\to I_4$. The Gram perturbation bound follows from
$\|X\|_{\mathrm{op}},\|X^0\|_{\mathrm{op}}\le\sqrt m$.
Gronwall gives (30), with constants uniform for sufficiently small
fixed perturbations. Since
$e^{C_TR-c_TR^2}\to0$, choosing finite $R$ first and a fixed
positive radius second gives arbitrarily small comparison error
before taking width large. The radius does not shrink with width.

## 6. Finite-width all-future capture

Metric-ball continuity does not need a pointwise bound on an arbitrary
perturbed readout. At a center with readout bound $P$, write

$$
b_b-\bar b_b=(w-\bar w)(1-h_b^2)
 +\bar w[(1-h_b^2)-(1-\bar h_b^2)].
$$

Only the center readout multiplies a gate difference. The first term
is controlled directly in normalized $L^2$. Unit inputs, a bounded
center middle action, and tensor-product differences therefore give
the width-uniform tangent-feature continuity stated in Section 5.
No center first-layer norm bound is required.

A sufficiently small parameter radius makes the tangent-feature
perturbation less than $\sqrt\lambda/2$, preserving a center kernel
gap $\lambda$ as at least $\lambda/4$. Write $R=\|r\|_2$ and
$Q=r^\top Kr$. Until first exit,

$$
\|\dot\theta\|_{\mathrm{par}}=\frac2m\sqrt Q,\qquad
-R'=\frac{2Q}{mR},\qquad Q\ge\frac{\lambda}{4}R^2.
$$

Thus $\|\dot\theta\|_{\mathrm{par}}\le-(2/\sqrt\lambda)R'$.
If $R(T)<\rho\sqrt\lambda/2$, the total pre-exit path length is
strictly less than $\rho$, ruling out exit. Exact dissipation then
gives exponential loss decay at rate $\lambda/m$. If $R(T)=0$,
the flow is stationary and the conclusion is immediate.

The actual snapshot need not be close to the reference in full
parameter metric. The argument does not require that assertion:
feature comparison transfers its residual and tangent gap, the
clock comparison transfers its sharp readout/action bounds, and
capture is centered at the actual snapshot itself.

In particular, (31) gives $p_n(T)\le S$ for small enough comparison
error, hence $\|w(T)\|_\infty\le S$ and
$\|W(T)\|_{\mathrm{op}}\le M$. These are not incorrectly inferred
from normalized $L^2$ closeness.

## 7. Order of choices and final claim

The choices are noncircular:

1. Fix the base dataset and amplitude; obtain its finite endpoint
   and the deterministic late-state bounds and margin.
2. Choose the capture radius with conservative bounds
   $P=S+1$, $L=M+1$, $\lambda=\lambda_*/2$.
3. Choose a single deterministic late time $T$ with a strict
   reference residual margin and the endpoint first-feature gap.
4. At that fixed time, choose comparison tolerance, finite $R$,
   and then fixed positive neighborhood radius $\varepsilon$.
5. For each fixed dataset in the neighborhood, send width to
   infinity and intersect the finitely many comparison events.
6. Apply finite-width capture for the entire future $[T,\infty)$.

The finite-horizon constants are uniform over a small neighborhood
because input norms are one and labels are uniformly bounded.
Thus a common deterministic $T$ and rate
$c=\lambda_*/(2m)>0$ really follow. Width convergence is used only
on $[0,T]$, not over infinite time.

Shrinking the radius preserves distinctness, nonantipodality, and
the two active label signs. Requiring every passive label to be
nonzero gives a nonempty open subset; their small magnitudes can
have any prescribed signs. For $m>4$, input-rank deficiency persists
automatically.

The claimed high-probability fitting and eventual exponential bounds
therefore follow. This does not supply a useful quantitative width
threshold, a uniform radius over degenerating base geometries, a
simultaneous probability event over the neighborhood, or a theorem
for arbitrary label ratios.
