# An energy-dissipating, locally Lipschitz approximation at fixed depth two

2026-09-08. This is a partial theoretical result for the exact contract in
`../CONTRACT.md`. No experiment or external theorem is used.

**Established here:** a new family of global, energy-dissipating population
approximations on the original canonical action spaces. They retain the genuine
adjoint and the original raw metric, are locally Lipschitz, and have a
cap-independent compact-time raw energy bound. Their comparison estimate costs
one power of the cap, and their defects occur only in the entire first-layer
direction and the readout direction. The actual finite random readout can be
retained.

**Not established:** removal of the caps. A uniform exponential tail estimate
for two specified fields would suffice, but is not proved here. Thus this note
does not establish the requested global canonical true gradient flow or its
actual finite-width limit. The new result removes the energy/stopping
circularity for this approximation family; it does not infer compactness from
energy.

## 1. Exact state, metric, and gradient

Put \(u_i=x_i/\sqrt d\) and \(w=\sqrt d W\). On the actual canonical layer
spaces \(H_j=L^2(\Omega_j)\), write

\[
\Theta=(w,U,C),\qquad A=A_0+U,
\quad \|\delta\Theta\|^2
=\|\delta w\|_{L^2(\Omega_1;\mathbb R^d)}^2
+\|\delta U\|_{\mathrm{HS}}^2+\|\delta C\|_2^2.
\]

There is no remaining factor \(d\) in the first term after this change of
variable. The initialized action \(A_0\) is bounded, its reverse is \(A_0^*\),
and its Hilbert--Schmidt norm is not assumed finite. Define

\[
\begin{split}
z_i&=w\cdot u_i,&h_i&=\phi(z_i),&v_i&=Ah_i,&k_i&=\phi(v_i),\\
f_i&=\langle C,k_i\rangle,&r_i&=f_i-y_i,&
b_i&=C\phi'(v_i),&q_i&=A^*b_i.
\end{split}
\]

Here \(\phi(z)=\tfrac34(1+z)+\tfrac14\tanh z\), so
\(|\phi(z)|\le 1+|z|\), \(3/4\le\phi'\le1\), and
\(\|\phi''\|_\infty\le1/2\). With
\((b\otimes h)a=b\langle h,a\rangle\), the true raw gradient is

\[
g_w=\sum_i r_i\phi'(z_i)q_i u_i,\qquad
g_U=\sum_i r_i b_i\otimes h_i,\qquad
g_C=\sum_i r_i k_i.                                      \tag{1}
\]

Along any strong path to which the raw equations apply,

\[
\frac{d}{dt}E
=\langle g_w,\dot w\rangle+
\langle g_U,\dot U\rangle_{\mathrm{HS}}+
\langle g_C,\dot C\rangle.                              \tag{2}
\]

For completeness, the chain rule needed here is along a path, not a claim that
the activation map is continuously Frechet differentiable on an ambient
\(L^2\) ball. A \(C^1\), \(L^2\)-valued preactivation path has almost-everywhere
absolutely continuous coordinate representatives. The scalar chain rule gives
\(\dot h_i=\phi'(z_i)\dot z_i\). Its right side is \(L^2\)-continuous: split
the difference into the velocity difference and a bounded multiplier
converging in probability against one fixed \(L^2\) velocity, and use dominated
convergence along almost-sure subsequences. The bounded-action product rule
then gives \(\dot v_i=\dot U h_i+A\dot h_i\), and the same argument applies to
\(k_i\). Differentiate \(\langle C,k_i\rangle\) and use the genuine adjoint.
This proves (2).

## 2. Smooth scalar and vector caps

Choose a smooth nonincreasing \(\eta:[0,\infty)\to[0,1]\) equal to one on
\([0,1]\) and zero on \([2,\infty)\). Such a function is explicit: on
\(1<s<2\) use
\(\eta(s)=\rho(2-s)/(\rho(2-s)+\rho(s-1))\), where
\(\rho(t)=e^{-1/t}\) for \(t>0\) and zero otherwise, and extend by the stated
constants. Set

\[
\tau_R(s)=\operatorname{sgn}(s)R\int_0^{|s|/R}\eta(a)\,da,
\qquad \chi_R(s)=\begin{cases}\tau_R(s)/s,&s\ne0,\\1,&s=0.\end{cases}
\]

Then \(\tau_R\) is smooth, odd, nondecreasing, and 1-Lipschitz;
\(\tau_R(s)=s\) for \(|s|\le R\);
\(|\tau_R(s)|\le\min\{|s|,2R\}\); and \(0<\chi_R(s)\le1\).
For \(q\in\mathbb R^3\), let

\[
H_R(q)=\chi_R(|q|)q.                                    \tag{3}
\]

This map is smooth and 1-Lipschitz, equals the identity on \(|q|\le R\), and
has magnitude at most \(2R\). Indeed its radial derivative is
\(\tau_R'(|q|)\in[0,1]\), its two tangential eigenvalues are
\(\tau_R(|q|)/|q|\in[0,1]\), and it is the identity near zero. Integrating its
Jacobian on a segment proves the Lipschitz assertion.

The cap size is monotone: if \(S\ge R\), then
\(\tau_S(s)\ge\tau_R(s)\) for \(s\ge0\), since
\(d[R\tau_1(s/R)]/dR=\tau_1(s/R)-(s/R)\tau_1'(s/R)\ge0\).
Consequently

\[
|H_R(q)-H_S(q)|\le |q|\mathbf1_{|q|>R},\qquad
|\tau_R(g)-\tau_S(g)|\le |g|\mathbf1_{|g|>R}.             \tag{4}
\]

## 3. The approximation and its exact dissipation

For the moment write the equations with their true, unmodified forward and
backward fields. Set \(Q=(\sum_i q_i^2)^{1/2}\), pointwise on the first layer,
and define

\[
\boxed{\quad
\dot w=-\chi_R(Q)g_w,\qquad
\dot U=-g_U,\qquad
\dot C=-\tau_R(g_C)=-\chi_R(g_C)g_C.
\quad}                                                  \tag{5}
\]

The same scalar \(\chi_R(Q)\) multiplies the entire first-layer row direction.
This detail is essential: clipping the three sample terms separately need
not preserve their alignment with their sum. At the top we clip the entire
readout direction. The adjacent-layer update is its true gradient update.

Substitution in (2) gives the exact identity

\[
E'=-\int\chi_R(Q)|g_w|^2
-\|g_U\|_{\mathrm{HS}}^2
-\int\chi_R(g_C)|g_C|^2
\le-\|\dot\Theta\|^2.                                  \tag{6}
\]

The inequality follows from \(\chi_R^2\le\chi_R\), block by block. Hence

\[
\int_0^T\|\dot\Theta_R\|^2\,dt\le E(0),\qquad
\sup_{t\le T}\|\Theta_R(t)-\Theta(0)\|\le\sqrt{TE(0)}.   \tag{7}
\]

This is a dissipative preconditioning of the true gradient. It is not asserted
to be the true gradient flow of the original metric at finite \(R\). Its
dissipation is nevertheless for the original loss and bounds speed in that
original metric.

## 4. A legitimate locally Lipschitz construction

The formal system (5) must still be constructed; its top backward gate has an
ambient \(L^2\) obstruction when \(C\) is arbitrary. Fix a horizon \(T\) and
take

\[
M=1+2RT,\qquad \widehat C=\tau_M(C).
\]

In the backward calculation only, use
\(\widehat b_i=\widehat C\phi'(v_i)\) and
\(\widehat q_i=A^*\widehat b_i\), and use them in the first two right sides
of (5). Keep the true forward predictor \(f_i=\langle C,k_i\rangle\) and the
third right side \(-\tau_R(\sum_i r_i k_i)\). This defines an autonomous
extension on the whole raw Hilbert space for this fixed pair \((R,T)\).

On any fixed primal ball, forward propagation and residuals are Lipschitz in
raw norm, with a constant independent of \(R,M\). The capped top gate obeys

\[
\|\widehat b_i-\widehat{\bar b}_i\|_2
\le\|C-\bar C\|_2+M\|v_i-\bar v_i\|_2,                 \tag{8}
\]

because \(|\tau_M|\le2M\), \(\|\phi''\|_\infty\le1/2\), and
\(\tau_M\) is 1-Lipschitz. Also
\(\|\widehat b_i\|_2\le\|C\|_2\). The genuine adjacent action gives

\[
\|\widehat q_i-\widehat{\bar q}_i\|_2
\le\|A-\bar A\|_{\mathrm{op}}\|\widehat b_i\|_2
+\|\bar A\|_{\mathrm{op}}
  \|\widehat b_i-\widehat{\bar b}_i\|_2.                \tag{9}
\]

For the first block, use \(H_R\) before the gate difference:

\[
\|\phi'(z_i)H_R(\widehat q)_i
-\phi'(\bar z_i)H_R(\widehat{\bar q})_i\|_2
\le\|\widehat q-\widehat{\bar q}\|_{L^2(\mathbb R^3)}
+R\|z_i-\bar z_i\|_2.                                 \tag{10}
\]

The rank-one inequality
\(\|b\otimes h-\bar b\otimes\bar h\|_{\mathrm{HS}}
\le\|b-\bar b\|_2\|h\|_2+\|\bar b\|_2\|h-\bar h\|_2\)
controls the second block. The third block uses the 1-Lipschitz scalar cap.
Equations (8)--(10) show a Lipschitz constant

\[
K_{B,T}(1+R),                                           \tag{11}
\]

on a primal ball of radius \(B\), where \(K_{B,T}\) is independent of \(R\).
There is no product \(RM\): the Lipschitz constant of \(H_R\) in its incoming
argument is one. Its size \(2R\) is used only for the separate first-layer
forward-gate difference.

The extension's field norm on that ball is bounded by a constant \(K_B\)
independent of \(R,M\). This follows from
\(|\tau_M(C)|\le|C|\), \(|H_R(q)|\le|q|\),
\(|\tau_R(g)|\le|g|\), bounded actions, and bounded slopes. For example, if
the raw distance from initialization is at most \(B\), then

\[
\|h_i\|_2\le2+B,\quad
\|A\|\le\|A_0\|+B,\quad
\|k_i\|_2\le1+(\|A_0\|+B)(2+B),\quad
\|b_i\|_2\le B,
\]

with the evident extra initial-readout term if it is nonzero. These bounds
bound residuals and all three direction norms by a polynomial in
\(B,\|A_0\|\), and the fixed labels.

Local existence and uniqueness for the extension follow directly by Picard
iteration of its integral equation on a sufficiently short interval: the
field bound preserves a closed path ball and the product of interval length
and (11) can be made less than one. Completeness gives the fixed point, and
the field's continuity gives a strong \(C^1\) solution.

Starting from population \(C(0)=0\), the third equation gives, pointwise,

\[
|C(t)|\le2Rt\le2RT<M.                                  \tag{12}
\]

The integral equation supplies pointwise representatives, so no pointwise
ODE assumption is being added. Thus the extension is inactive throughout
\([0,T]\): \(\widehat C=C\), and this solution satisfies (5), (6), and (7).
Initially \(E(0)=3/2\) for the contract's three \(\pm1\) labels.

If a maximal solution ended before \(T\), (7) would put it in a fixed raw
ball. The cap-independent field bound on that ball makes the path Cauchy at
the endpoint. Its limiting readout still satisfies (12), since an \(L^2\)
limit of functions bounded by \(2RT\) has the same almost-everywhere bound.
Local existence for the extension then continues the solution, a
contradiction. Hence the approximant is global on the prescribed horizon.

For fixed \(R\), different choices of \(T\) agree on overlaps: on an overlap
their pointwise readout bounds make both extensions inactive, and (8)--(10)
compare the resulting paths with a common larger readout bound. Gronwall
therefore identifies them. Thus (5) defines a single global approximating
trajectory for each \(R\), while the locally Lipschitz extension is only its
construction device.

## 5. Actual finite initialization and finite query compatibility

In width \(n\), use \(w=\sqrt d W\), the genuine transpose, and the unchanged
initial arrays from the contract. The raw norm is

\[
\|\delta w\|_n^2+\|\delta A\|_F^2+\|\delta C\|_n^2,
\]

and \(b\otimes h\) is the actual matrix \(bh^T/n\). Thus (1), (5), and (6)
hold with normalized sums, with the initialized \(C_n(0)\) retained exactly.
The finite system is locally Lipschitz; its energy identity gives global
finite-dimensional continuation at every width.

The pointwise bound is now

\[
\|C_n(t)\|_\infty\le\|C_n(0)\|_\infty+2Rt.             \tag{13}
\]

For deterministic fixed-cap width comparisons one may use the extension
level \(M=2+2RT\). On the event
\(\|C_n(0)\|_\infty\le1\), the extension is inactive for the entire finite
path. Since \(C_{n,j}(0)\sim N(0,n^{-2})\), the elementary Gaussian tail and
a union bound give

\[
\Pr\{\|C_n(0)\|_\infty>1\}\le2n e^{-n^2/2}\longrightarrow0.             \tag{14}
\]

Also \(\mathbb E\|C_n(0)\|_n^2=n^{-2}\). At each fixed finite transcript,
its removal is therefore a Lipschitz perturbation tending to zero; it is not
removed from either actual finite dynamics or same-width comparisons. For
example, conditional on initialized hidden features,
\(\mathbb E[f_{n,i}(0)^2\mid k_i]=n^{-3}\|k_i\|_n^2\); bounded initialized
feature second moments give \(E_n(0)\to3/2\) in probability.

All extra coordinate instructions are smooth and globally Lipschitz at
fixed \(R,M\): \(H_R\), \(\tau_R\), and
\((v,C)\mapsto\phi'(v)\tau_M(C)\). Forward activations have bounded
derivative. The rank updates are expanded through their exact same-layer
contractions, and residuals are the same causal scalar feedback. Thus the
new finite programs satisfy the coordinate-regularity hypotheses in the
existing finite-query Gaussian construction. This paragraph checks
compatibility; it does not independently reprove that construction or claim
the uncut GF/GD observation bridge. In particular all matrix reuse and current
returns must still be included when the new finite programs are compiled.

## 6. A one-cap comparison and the exact defects

Let \(\Theta_R\) and \(\Theta_S\), \(S\ge R\), be these population paths on
\([0,T]\). Their raw balls, residuals, action norms, and true field \(L^2\)
norms have common bounds by (7). The same estimates apply with \(S=\infty\)
to any bounded-primal true strong competitor, if one exists. Define

\[
\mathcal T_S(R,t)
=\|Q_S(t)\mathbf1_{Q_S(t)>R}\|_2
+\|g_{C,S}(t)\mathbf1_{|g_{C,S}(t)|>R}\|_2.              \tag{15}
\]

There is a constant \(K_T\), independent of \(R,S\), such that

\[
\|\dot\Theta_R-\dot\Theta_S\|
\le K_T(1+R)\|\Theta_R-\Theta_S\|+K_T\mathcal T_S(R,t).
                                                               \tag{16}
\]

The important top-gate splitting is asymmetric:

\[
b_{R,i}-b_{S,i}
=(C_R-C_S)\phi'(v_{S,i})
+C_R[\phi'(v_{R,i})-\phi'(v_{S,i})].                    \tag{17}
\]

Use \(|C_R|\le2RT\) in the second term. This gives
\(\|b_R-b_S\|_2\le K_T(1+R)\|\Theta_R-\Theta_S\|\)
without any pointwise bound on \(C_S\). Apply the genuine adjoint and bounded
actions to compare \(q_R,q_S\). In the first direction, split
\(H_R(q_R)-H_S(q_S)\) into its 1-Lipschitz argument difference and (4).
Use the size of \(H_R(q_R)\) only for the independent \(z_R-z_S\) gate
difference. The second block uses (17) and the rank-one inequality. The third
uses the 1-Lipschitz readout cap and (4). Residual differences cost only a
cap-independent forward Lipschitz constant. This proves (16), with no
\(R^2\) and no additional readout-amplitude defect.

At a single approximating state, its difference from the true raw field is
exactly

\[
F_R(\Theta_R)-F(\Theta_R)
=\big((1-\chi_R(Q_R))g_{w,R},\ 0,\
       (1-\chi_R(g_{C,R}))g_{C,R}\big),                 \tag{18}
\]

where \(F=-g\). Since \(|g_w|\le\|r\|_2 Q\),

\[
\|F_R(\Theta_R)-F(\Theta_R)\|
\le K_T\mathcal T_R(R,t).                              \tag{19}
\]

Thus the cap error is determined by the true first-layer incoming vector
\(q\) and the true readout velocity \(g_C\). There is no modified top
backward gate along these approximants and no adjacent-layer defect.

## 7. The remaining tail obligation can use exponential tails

A sufficient, unproved condition is

\[
\sup_{S\ge1}\sup_{t\le T}\mathcal T_S(R,t)
\le K_T e^{-c_T R},\qquad R\ge1.                       \tag{20}
\]

SubGaussian tails are a stronger sufficient condition. Unlike direct use of
(16) over a long interval, the following argument shows that (20) suffices
with any \(c_T>0\). This is an explicit bridge statement, not evidence that
(20) holds.

First (20) implies, for every integer \(p\ge2\),
\(\sup_{S,t}\|g_{C,S}(t)\|_p\le K'_T p\). To verify this, the squared-tail
bound gives \(\Pr(|g|>u)\le K_T^2e^{-2c_Tu}/u^2\) for \(u\ge1\).
Integrate \(p\int_0^\infty u^{p-1}\Pr(|g|>u)\,du\), absorb \(u\le1\),
and bound the resulting exponential integral by a factorial. Its \(p\)-th
root is at most a constant times \(p\). Minkowski and
\(|\tau_S(g)|\le|g|\) yield

\[
\sup_{S,t\le T}\|C_S(t)\|_p\le T K'_T p.               \tag{21}
\]

Conversely such a moment bound gives exponential squared-amplitude tails:
choose an integer \(p\) proportional to \(u\), apply Markov to \(|C|^p\),
and then use Cauchy--Schwarz with the uniformly bounded fourth moment.
Thus \(C_S\) has a uniform bound of the form in (20), with different
constants. This uses no independence in time.

The elementary uncut gate estimate at a level \(L\) is

\[
\|\phi'(z)q-\phi'(\bar z)\bar q\|_2
\le\|q-\bar q\|_2+\frac12L\|z-\bar z\|_2
+2\|\bar q\mathbf1_{|\bar q|>L}\|_2.                  \tag{22}
\]

Apply (22) first with incoming \(C\), then with incoming \(q_i\), retaining
bounded-action estimates between them. Each factor \(L\) multiplies a
forward state discrepancy; the second application does not multiply the
first application's incoming-field discrepancy by \(L\). Hence, for two
approximating states at any times in \([0,T]\),

\[
\|F(\Theta)-F(\bar\Theta)\|
\le K_T(1+L)\|\Theta-\bar\Theta\|+K_Te^{-c'_T L}.       \tag{23}
\]

For distance \(s\le1\), take
\(L=\max\{1,(c'_T)^{-1}\log(1/s)\}\). Enlarge constants for \(s\ge1\).
On the bounded raw ball (23) becomes

\[
\|F(\Theta)-F(\bar\Theta)\|
\le K''_T s\log(B_T/s),                                \tag{24}
\]

where \(B_T\) can be chosen larger than \(e\) times the diameter of the
ball. The function on the right is increasing throughout the relevant
distance range, and its reciprocal has divergent integral at zero.

Here is a direct Cauchy argument, without invoking an external Osgood
theorem. For caps \(S\ge R\), (19), (20), and (24) give an integral
inequality for their distance with forcing at most
\(\delta_R=K_Te^{-c_T R}\). Introduce its scalar majorant \(Y\), with
\(Y(0)=\delta_R\),
\(Y'=aY\log(B/Y)+\delta_R\), choosing \(B\) larger if needed.
While \(Y\) is in the bounded comparison range, \(Y\ge\delta_R\) and
\(\log(B/Y)\ge1\), so
\(Y'\le(a+1)Y\log(B/Y)\). Integration of
\((\log(B/Y))'\ge-(a+1)\log(B/Y)\) gives

\[
\sup_{t\le T}\|\Theta_R(t)-\Theta_S(t)\|
\le B(\delta_R/B)^{\exp(-(a+1)T)}\longrightarrow0.      \tag{25}
\]

A first-exit argument justifies remaining in that range for all large
\(R\). The integral comparison with \(Y\) follows by first crossing, using
the monotonicity of the right side. This proves the asserted Cauchy bridge
from (20). Strong continuity of the true gates then passes the integral
equations to a true strong flow. The same estimate with only the reference
flow's tails gives uniqueness against bounded-primal strong competitors;
no moment assumption on the competitor is needed. The true chain rule
supplies its energy identity. This conditional conclusion is for population
cap removal; the actual finite GF/GD joint observations still require their
own finite-program and ordered-observation transfer.

## 8. Two useful refinements

### A residual-weighted improvement of the construction

There is an alternative to (5) with a weaker tail target. Set

\[
p_i=r_iq_i,\qquad P=(\sum_i p_i^2)^{1/2},\qquad
\dot w=-\sum_i\phi'(z_i)H_R(p)_i u_i
       =-\chi_R(P)g_w,                                 \tag{26a}
\]

and leave the adjacent and readout updates as in (5). Every result in
Sections 3--6 remains valid with \(Q\) replaced by \(P\), and with a
constant depending on the common compact-time primal bound. Here is the
additional check, so the statement does not rely on a formal replacement:

\[
\|p_i-\bar p_i\|_2
\le |r_i|\|q_i-\bar q_i\|_2
   +|r_i-\bar r_i|\|\bar q_i\|_2.                     \tag{26b}
\]

Residuals and true incoming \(L^2\) norms are bounded on the primal ball;
residuals are forward Lipschitz. Thus (9), (10), and (17) still give one cap
factor, and the energy identity uses the same nonnegative common multiplier
on \(g_w\). The first-block defect is bounded by
\(\sqrt3\|P\mathbf1_{P>R}\|_2\), since
\(|g_w|\le\sum_i|p_i|\le\sqrt3 P\).

For this alternative family, uniform exponential squared-amplitude tails
of **\(P\) and \(g_C\)** suffice in Section 7; unweighted \(q_i\) tails are
not needed there. To verify the uncut comparison, write the first direction
as \(\sum_i\phi'(z_i)p_i u_i\), apply (22) with incoming field \(p_i\), and
use (26b). The upper gate still needs only the readout tails obtained from
the \(g_C\) moment bound. This proves (23)--(25) with that weaker hypothesis.
Once raw states converge strongly, every true \(q_i=A^*[C\phi'(v_i)]\)
converges in \(L^2\) by bounded-multiplier continuity, regardless of whether
an exponential tail for unweighted \(q_i\) was proved.

This variant more directly uses the physical residual in the tail target.
It is still an unresolved tail-production problem, not an unconditional cap
removal result. The construction and original target in (15) were retained
above to keep the two approximation families distinct.

### Curvature decay itself

There is a modest unconditional improvement for this particular activation.
For all real \(x,y\),

\[
|\phi'(x)-\phi'(y)|\le
\frac{4|x-y|}{1+|x|}.                                  \tag{26}
\]

To prove it, when \(|x-y|\ge(1+|x|)/2\), the left side is at most \(1/4\),
which is smaller than the displayed bound. Otherwise, if \(|x|\le3\), use
\(\|\phi''\|_\infty\le1/2\). If \(|x|>3\), every intermediate point
\(z\) has \(|z|\ge(|x|-1)/2\), and
\(|\phi''(z)|\le2e^{-2|z|}\le2e^{1-|x|}\le4/(1+|x|)\).
The mean-value theorem completes the proof.

Consequently a gate comparison may cap the ratio
\(|q|/(1+|z|)\) instead of \(|q|\), at the price of the weighted defect
\(\|q\mathbf1_{|q|/(1+|z|)>R}\|_2\). This can help if a separate reachable
state argument proves that large incoming fields track the corresponding
preactivation. No such relation is established here.

Decay alone cannot bound \(C\phi''(v)\) on an ambient raw ball: hold \(v\)
in a fixed interval where \(|\phi''|\) is bounded below, and let \(C\) have
an unbounded \(L^2\) amplitude on that event. The pointwise multiplier is
unbounded. This is the previously identified ambient obstruction, not a
counterexample about the canonical reached states.

For one scalar equation \(z'=a(t)\phi'(z)\), the change
\(s=\int_0^z1/\phi'(v)\,dv\) gives \(s'=a(t)\), with uniformly bounded
coordinate distortion. It does not flatten the actual first-layer system
\(\dot z_i=-\sum_j\Gamma_{ij}r_j\phi'(z_j)q_j\): after the same componentwise
change its coefficients contain
\(\Gamma_{ij}\phi'(z_j)/\phi'(z_i)\). Their derivatives still multiply
incoming fields. Thus this scalar observation does not close the
three-sample continuation problem, including the allowed singular Grams.

## 9. Exact research-state change and dependencies

The prior `three_sample_near_identity_all_depths/ENERGY_GALERKIN_ROUTE.md`
proved energy-preserving finite-partition approximants but left strong
canonical compactness open. The prior
`three_sample_odd_activation_depth2/SOURCE_AND_CONTINUATION.md` identified the
two past-response families and the loss of the true energy identity under
ordinary internal gate clipping. Those gaps are not contradicted here.

The new construction uses the actual canonical spaces directly, supplies
uniform physical energy control before any source-tail argument, and has
smooth coordinate instructions compatible with the finite Gaussian program
machinery. It is especially useful at two hidden layers: bounding the
readout through its velocity makes the only upper backward gate Lipschitz,
and a common radial preconditioner repairs the remaining first-layer gate
without altering its gradient alignment.

All new analytic claims above were derived internally. The existence of the
canonical bounded initialized action and its genuine adjoint is part of the
contract and existing construction, not a new arbitrary-operator
substitution. No higher-moment operator bound, independent reverse action,
compactness from energy, or Gaussian law of trained fields is assumed.

The single remaining issue for this route is to prove (20), or another
direct strong Cauchy mechanism, for these actual energy-dissipating
approximants with their full response chronology. Establishing that issue
would change the continuation claim; the present construction by itself
does not.
