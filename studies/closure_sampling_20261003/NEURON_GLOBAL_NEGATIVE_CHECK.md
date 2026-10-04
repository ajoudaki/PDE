# Complete check of the canonical-marginal neuron lower bound

2026-10-03. Collaborative internal mathematical check, not an isolated
promotion review. The complete candidate `NEURON_GLOBAL_NEGATIVE.md` was
read and independently reconstructed at SHA-256
`0eeba02726f8f3bec3dbe5026d857402ca091c69b5c382bf6b9ae55731e98e80`.
The source was not edited.

**Verdict: PASS for the complete stated scope.** The fixed-positive-time
prediction lower bound and the sufficiently-small-label fitted-endpoint
lower bound both hold for any coupling whose width-$n$ and width-$N$
initialization marginals remain canonical. Both estimates are uniform in
arbitrary deterministic positive memory orders, including width-dependent
orders. No mathematical correction is required.

This is specifically a restriction on reducing neuron count while
retaining the **canonical smaller-width marginal law** and then running
that width's original closure. It is not a lower bound for general
initialization-dependent weighted cubature, a projected mixer, modified
response dynamics, or all autonomous neuron reductions. The query law in
the all-time consequence is a point mass at one fixed orthogonal sphere
query, not uniform sphere measure.

The additional scientific input inspected for this check was the complete
initialization, projection-estimate and all-order fitting/continuation
portion of `paper/proof_alltime.tex`, ending before its Gaussian reference
construction. That file's SHA-256 is
`f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d`.
The canonical-notation skill and neural reference, rigorous-math skill,
and research-contract/adversarial-audit instructions were applied.
No experiment, literature search, source edit, or Git operation was used.

## 1. Model and probability contract

At width $k$, the model has independent standard-Gaussian first weights
$A_0\in\mathbb R^{k\times d}$, independent mixer entries
$(W_0)_{ij}\sim N(0,1/k)$, and exactly zero readout. It trains only
on $x_1=\sqrt d\,e_1$ with label $y>0$, using its original order-$q$
residual-RMS closure and the canonical outer-weight updates. Its query
is $x_*=\sqrt d\,e_2$, with $d\ge2$.

The first-weight velocity has the form $v(t)e_1^\top$. Consequently
$g=A(t)e_2=A_0e_2$ is unchanged and is an independent $N(0,I_k)$
vector conditional on that network's training initialization
$(A_0e_1,W_0)$. Every training state, including every moment and clock,
is measurable from this training initialization. The query prediction is

\[
 F_k(t,g)=\frac1k w(t)^\top\tanh(W(t)\tanh g).
\tag{C1}
\]

It is odd in $g$. Neither independence between the two widths nor
conditional Gaussianity of one query column after conditioning on both
networks is asserted or needed.

The sampler in the candidate's equation (6) satisfies the marginal
contract: conditional on externally chosen index sets, all selected
first-weight entries are independent $N(0,1)$, all rescaled mixer entries
are independent $N(0,1/N)$, and the two selected matrices are independent.
This conditional joint law does not depend on the chosen sets, so mixing
over those sets preserves it. The sets may depend on one another but
must be independent of initialization for that corollary. More general
selection is covered only when the resulting marginal law is still
canonical.

## 2. Short-time estimates and initial fluctuation

On $\|W_0\|_{\rm op}\le M$, the readout inequality
$\|w(t)\|_\infty\le y(e^{2t}-1)$ gives a fixed interval on
which $r<0$, $|r|\le2y$ and $\|w(t)\|_\infty\le Cyt$.
While $\|W\|_{\rm op}<M+1$, first-layer motion has normalized
norm at most $C_My^2t^2$.

The useful step in controlling mixer motion is to subtract the constant
initial forward feature before applying projection contraction. If
$u=h^{(1)}-h^{(1)}(0)$ on the clock history, its prefix is zero and
every order $q\ge1$ retains the constant term exactly. The reconstructed
increment is therefore a constant-feature rank-one term plus
$-(2/k)\int(\Pi_qb)(\Pi_qu)^\top$. Their bounds are
$C y^2t^2$ and $C_My^4t^4$, respectively. Choosing a fixed small
$t_0(M)$ closes the tube with no width or order dependence.

This proves the candidate's bounds

\[
 \|W(t)-W_0\|_{\rm op}\le C_My^2t^2,\qquad
 \frac{\|h^{(2)}(t)-h_0^{(2)}\|_2}{\sqrt k}\le C_My^2t^2,
\]

\[
 \frac{\|w(t)-2yt h_0^{(2)}\|_2}{\sqrt k}\le C_Myt^2.
\tag{C2}
\]

The last bound includes the term $-2f h^{(2)}$ in the readout
velocity; dropping it would give an unjustified stronger power of $y$.
The candidate retains it correctly. Finite-order moment integral
formulas and $\tau\ge1$ justify continuation through $t_0$.

For the initialized query kernel
$K_k(g)=k^{-1}h_0^{(2)\top}\tanh(W_0\tanh g)$, condition first
on the independent lower feature vectors $h=\tanh(A_0e_1)$ and
$u=\tanh g$. The upper-row pairs are independent conditional
Gaussians. Their covariance approaches $Q I_2$, where
$Q=\mathbb E\tanh^2(G)>0$. On the candidate's compact covariance
set, the determinant is at least $3Q^2/16$ and both variances are
bounded above by one. Continuity and nonconstancy of
$\tanh Z\tanh Z_*$ give a common positive conditional variance.
Thus $\mathbb E K_k^2\ge c_0/k$ for all sufficiently large $k$.
No unconditional upper-row independence was substituted for this
conditional calculation.

The Gaussian net estimate makes the complement of
$\|W_0\|_{\rm op}\le10$ exponentially small in $k$. Since
$|K_k|\le1$, removing this event costs exponentially little in its
second moment, preserving the $1/k$ lower bound.

## 3. Query remainder and conversion to a probability lower bound

Differentiate (C1) with respect to the unused Gaussian column. The
gradient is

\[
 \nabla_gF_k=\frac1k\operatorname{diag}(\operatorname{sech}^2g)
  W^\top\{w\odot\operatorname{sech}^2(W\tanh g)\}.
\tag{C3}
\]

For $R_k=F_k-2ytK_k$, subtraction has exactly three contributions:
changed readout, changed matrix, and changed upper gate. The bounds
(C2), $\|h_0^{(2)}\|_\infty\le1$, and bounded tanh derivatives
give

\[
 \sup_g\|\nabla_gF_k\|_2\le C_Myt/\sqrt k,
 \qquad \sup_g\|\nabla_gR_k\|_2\le C_Myt^2/\sqrt k.
\tag{C4}
\]

Oddness removes the conditional means. Gaussian Poincare then gives
$\mathbb E_gR_k^2\le C_My^2t^4/k$ and
$\mathbb E_gF_k^2\le C_My^2t^2/k$. Applying the same inequality
to the square of an odd $L$-Lipschitz function gives
$\mathbb E H^4\le5L^4$: its second moment is at most $L^2$ and
$\operatorname{Var}(H^2)\le4L^2\mathbb EH^2$. All functions here
are bounded at fixed training states, so these Sobolev and integrability
conditions hold. This verifies the fourth-moment estimate as well.

Let $\mathcal G$ be the intersection of the two width-specific
bounded-mixer events. For any coupling,

\[
 \|[F_N(t)-F_n(t)]\mathbf1_{\mathcal G}\|_{L^2}
 \ge\frac{yt}{\sqrt N}
       (2c_1-Ct-C\sqrt{N/n}).
\tag{C5}
\]

The $L^2$ triangle inequality alone proves this inequality; no control
of the covariance between the two predictions is required. Fixed small
$t_*>0$ and fixed small $\eta>0$ make its bracket positive for
$N/n\le\eta$. The fourth moment of the difference is at most
$Cy^4t_*^4/N^2$. Applying the second-moment lower-tail inequality
to $|F_N-F_n|^2\mathbf1_{\mathcal G}$ produces a probability bounded
below independently of both widths, orders and $0<y\le1$.
The error threshold is a fixed positive multiple of $y/\sqrt N$.

For the small-label scope of the question, the all-time trajectories
also exist and fit on the events checked below. More generally, bounded
tanh also prevents finite-time blowup at each fixed order: the readout
bound controls $\rho$ and $\tau$ on every bounded physical interval,
projection contraction bounds the reconstructed mixer there, and then
the first-weight equation and moment integral formulas bound the full
raw state. Thus the use of an all-time supremum as a consequence of the
positive-time theorem introduces no finite-time existence issue.

## 4. The training-only fitting event is sufficient

The endpoint argument uses

\[
 \mathcal T_k=\{\|W_0\|_{\rm op}\le10,
       \|A_0e_1\|_2/\sqrt k\le2,
       G_k\ge\gamma\},\qquad
 G_k=\|h_0^{(2)}\|_2^2/k.
\tag{C6}
\]

This event is measurable from training initialization only. Its
exponentially small complement follows from three valid marginal
estimates: the mixer norm tail, the chi-square tail for $A_0e_1$,
and bounded-variable concentration first for
$\|\tanh(A_0e_1)\|_2^2/k$ and then conditionally for $G_k$.
The monotonicity of $\tanh^2(\sqrt Q\,G)$ in $Q$ for each real
$G$ supplies the positive uniform conditional mean used in the last
step. A fixed $\gamma>0$ suffices.

The exact fitting subsection of `paper/proof_alltime.tex` needs the
initialized hidden-operator bound, initialized **training** preactivation
RMS bound and initial readout-feature Gram gap. Its full first-matrix
Frobenius bound, included elsewhere in its good-event definition for
whole-input conclusions, is not used in this fitting bootstrap. For this
one-sample model, all changing first-weight coordinates are in the first
column. Consequently the fitting argument applies on (C6) without
conditioning on $A_0e_2$. This distinction is essential and is handled
correctly in the candidate.

For sufficiently small $0<y\le y_*$, the source proof gives,
uniformly in width and every $q\ge1$,

\[
 |r(t)|\le ye^{-\kappa t},\quad \int_0^\infty|r|\le Cy,
 \quad \|\dot W\|_F+\|\dot A\|_F/\sqrt k
          +\|\dot h^{(2)}\|_2/\sqrt k\le Cy|r|.
\tag{C7}
\]

The mixer velocity here includes the closure defect. In the fitting
proof its contribution is bounded by $Cy^{5/2}|r|$, which is at
most $Cy|r|$ for $y\le1$. Thus integrating the velocity estimate
does supply $O(y^2)$ total mixer movement, even though an earlier
coarse reconstruction estimate in that proof was only $O(y^{3/2})$.
There is no unjustified strengthening of that earlier bound.

Integrating (C7) proves all three displacement bounds in the candidate's
(34), convergence of physical parameters and interpolation. The raw
vector field is locally Lipschitz for $\tau>0$ and vanishes entirely
when $r=0$, so uniqueness forbids a first finite zero of a residual
that starts at $-y$. The residual remains negative. All assumptions
needed for the endpoint readout integral therefore hold.

## 5. Independent reconstruction of the endpoint estimate

Define $S=2\int_0^\infty|r(t)|dt\le Cy$. Integrating the readout
velocity and using the upper-feature displacement gives

\[
 w_\infty=S h_0^{(2)}+e,\qquad
 \|e\|_2/\sqrt k\le Cy^3,\qquad
 \|w_\infty\|_\infty\le Cy.
\tag{C8}
\]

Interpolation implies $y=S G_k+O(y^3)$: both the feature-change
pairing and the $e$ pairing have that size. Since $G_k\ge\gamma$,
putting $\alpha_k=y/G_k$ yields

\[
 y\le\alpha_k\le y/\gamma,
 \qquad
 \|w_\infty-\alpha_kh_0^{(2)}\|_2/\sqrt k\le Cy^3.
\tag{C9}
\]

The coefficient $\alpha_k$ depends on training initialization only.
Its lower bound is pointwise and does not require independence from
$K_k$ or from the other network.

The endpoint predictor is still (C1), using the converged $W,w$ and
the same unused Gaussian $g$. For
$R_k^\infty=F_k(\infty,g)-\alpha_kK_k(g)$, the three terms of
the gradient subtraction are bounded using (C9) and
$\|W_\infty-W_0\|_{\rm op}\le Cy^2$. This gives

\[
 \sup_g\|\nabla_gR_k^\infty\|_2\le Cy^3/\sqrt k,
 \qquad
 \sup_g\|\nabla_gF_k(\infty,g)\|_2\le Cy/\sqrt k.
\tag{C10}
\]

Oddness and the same Gaussian inequalities prove the candidate's (41):
second moments at most $Cy^6/k$ and $Cy^2/k$, and fourth moments
at most $Cy^{12}/k^2$ and $Cy^4/k^2$, respectively. The endpoint
is defined on $\mathcal T_k$, where the preceding fitting argument
proved its existence; no endpoint is presumed on the complementary
initializations.

## 6. Arbitrary coupling and event restrictions at the endpoint

Let $\mathcal T=\mathcal T_N\cap\mathcal T_n$ under any allowed
coupling. The conditional Gaussian query bounds are established under
each network's own marginal conditioning. The intersection need not
be measurable from either training initialization separately. The
following two elementary inequalities are sufficient:

\[
 \mathbb E[|X_k|^p\mathbf1_{\mathcal T}]
 \le\mathbb E[|X_k|^p\mathbf1_{\mathcal T_k}],
 \qquad p\ge1,
\tag{C11}
\]

\[
 \mathbb E[K_N^2\mathbf1_{\mathcal T}]
 \ge\mathbb EK_N^2
       -\mathbb P(\mathcal T_N^c)-\mathbb P(\mathcal T_n^c).
\tag{C12}
\]

In (C11), endpoint variables may be extended by zero off their own
fitting events. In (C12), $K_N$ exists everywhere and $|K_N|\le1$.
The exponentially small probabilities are controlled from the two
canonical marginals, irrespective of their dependence. Thus (C12)
preserves a $c/N$ second moment for sufficiently large $N$ and
$N/n\le\eta\le1$.

Using (C9)--(C12), the endpoint difference $D_\infty=F_N(\infty)-
F_n(\infty)$ satisfies

\[
 \begin{aligned}
 \|D_\infty\mathbf1_{\mathcal T}\|_{L^2}
 &\ge \|\alpha_NK_N\mathbf1_{\mathcal T}\|_{L^2}
       -\|R_N^\infty\mathbf1_{\mathcal T}\|_{L^2}
       -\|F_n(\infty)\mathbf1_{\mathcal T}\|_{L^2}\\
 &\ge\frac y{\sqrt N}\bigl(c-Cy^2-C\sqrt{N/n}\bigr),\\
 \mathbb E[|D_\infty|^4\mathbf1_{\mathcal T}]
 &\le Cy^4/N^2.
 \end{aligned}
\tag{C13}
\]

Choose a single sufficiently small fixed positive $y$, and then a
sufficiently small fixed bound on $N/n$. The first bracket is bounded
below by a positive constant. For
$Z=|D_\infty|^2\mathbf1_{\mathcal T}$,
$\mathbb P\{Z\ge\mathbb EZ/2\}\ge(\mathbb EZ)^2/
(4\mathbb EZ^2)$ gives the claimed positive-probability lower bound
at size $c'_y/\sqrt N$. The event lies inside $\mathcal T$, so
both endpoint predictions appearing in it are defined and interpolate.

All constants in this argument depend only on the fixed deterministic
initialization bounds, tanh and the chosen fixed small label. The
training events are independent of the memory order, and the estimates
hold at every positive integer order. The theorem quantifies over
deterministic orders; it does not silently condition on an
initialization-selected random order.

## 7. Consequences and limits of the verdict

For $N\to\infty$ with $N=o(n)$, the fixed-time discrepancy
$c_y/\sqrt N$ eventually exceeds every prescribed $C/\sqrt n$.
Its positive probability therefore rules out a root-original-width
all-time guarantee at all confidence levels $1-\delta$ with
$\delta$ below the theorem's probability constant. The analogous
statement holds at the fitted endpoint for its fixed small label.
For bounded $N$, the candidate's separate fixed-width argument is
also valid: a bounded-mixer event retains a nonzero initial query
kernel second moment, a sufficiently small fixed time preserves it,
and the original width-$n$ query prediction tends to zero in probability.

The conclusion requiring order-$n$ neuron count follows within the
specified class, with the proportionality constant allowed to depend on
the desired error constant and the fixed label. Since $q\ge1$, this
also rules out $Nq=o(n)$ in that class. It does not constrain every
possible weighted selection scheme, and it does not claim a lower
bound under uniform sphere query measure. Those exclusions are stated
explicitly in the source and are essential to this PASS verdict.
