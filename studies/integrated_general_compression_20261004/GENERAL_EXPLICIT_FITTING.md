# Explicit general dense fitting without bounded or normalized activation values

2026-10-04. Coordinator derivation for the merged theorem. This extends the
real fitting argument in closure_sampling_20261003/
EXPLICIT_UNBOUNDED_NORMALIZATION_ROUTE.md, removing its forward-normalization
assumption and making its initialization width threshold quantitative.
This component concerns dense fitting and physical bounds; it does not
by itself establish a compressor or independent-dense comparison.

## 1. Canonical model and explicit constants

Fix L>=2, d,m>=1, training vectors v_a=x_a/sqrt(d) of Euclidean norm one,
and deterministic labels y_a. All hidden layers have width n. Write

\[
 z^{(1)}(v)=Av,\quad z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\quad
 h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\quad
 f_n(v)=w^\top h^{(L)}(v)/n.
\]

Initialize A with independent N(0,1) entries, W^(ell) with independent
N(0,1/n) entries, independently between blocks, and w=0. The loss is
m^(-1)sum_a r_a^2, r_a=f_n(v_a)-y_a. The exact physical flow is

\[
 \delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
                 W^{(\ell+1)\top}\delta_a^{(\ell+1)},
\]
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
          r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
 \tag{1}
\]

It suffices here that every phi_ell is C^2, with bounded first and second
real derivatives. Define

\[
 b=\max_\ell|\phi_\ell(0)|,\quad
 s=\max\{1,\max_\ell\|\phi_\ell'\|_\infty\},\quad
 t_2=\max_\ell\|\phi_\ell''\|_\infty.
\]

The requested strip class satisfies these conditions. No bound on
activation VALUES, centering, or normalization is imposed.
For Z~N(0,1), define the one-dimensional Gaussian recursion

\[
 q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
 \qquad H=\max\{1,\sqrt{q_1},\ldots,\sqrt{q_L}\}.
 \tag{2}
\]

All quantities are finite because |phi_ell(z)|<=b+s|z| for real z.
For the training set, define

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\quad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),
\]
\[
 \gamma=\lambda_{\min}(Q^{(L)})>0,\quad
 \lambda=\gamma/m,\quad Y=\|y\|_2/\sqrt m.
 \tag{3}
\]

Here gamma is the user's UNWEIGHTED covariance gap. Every diagonal of
Q^(ell) equals q_ell, so lambda<=H^2/m. There is no need to assume
lambda<=1 or silently replace it by a capped value.

The following finite constants are explicit:

\[
 D_\ell=s(9s)^{L-\ell},\quad U_1=D_1,\quad
 U_\ell=2HD_\ell\quad(\ell\ge2),
\]
\[
 F_1=sU_1,\quad
 F_\ell=s(2HU_\ell+9F_{\ell-1})\quad(\ell\ge2),
\]
\[
 F=F_L=s^2\left[(9s)^{2L-2}
       +4H^2\sum_{j=0}^{L-2}(9s)^{2j}\right].
 \tag{4}
\]

In particular F>=max(1,U_1,...,U_L,F_1,...,F_L).

## 2. A fully specified initialization width

For confidence parameter 0<delta<1, set

\[
 A_*=s^2+t_2(b+\sqrt2sH),\quad
 T_L=\sum_{j=0}^{L-1}A_*^j,\quad
 e=\min\{1/4,\gamma/(2m)\},\quad
 M_4=8b^4+96s^4H^4,
\]
\[
 h=\min\{1/2,H/[4(8s)^L]\},\qquad P=(1+2/h)^d,
\]
\[
 N_{\rm fit}(\delta)=\left\lceil
 \max\left\{
 1,\ \frac{\log(8L/\delta)}{8-2\log9},\quad
 \frac{d\log9+\log(8/\delta)}{8-\log9},\quad
 \frac{2L(m^2+P)M_4T_L^2}{\delta e^2}
 \right\}\right\rceil.
 \tag{5}
\]

All denominators are strictly positive. The constants in (5) depend only
on the displayed activation moments/derivatives and problem parameters.
This is a conservative explicit threshold, not an optimized one.

For every n>=N_fit(delta), with probability at least 1-delta,

\[
 \|A_0\|_{\rm op}/\sqrt n\le8,\qquad
 \max_{2\le\ell\le L}\|W_0^{(\ell)}\|_{\rm op}\le8,
\]
\[
 \sup_{\|v\|=1,\,1\le\ell\le L}
          \|h_0^{(\ell)}(v)\|_2/\sqrt n\le3H/2,
\]
\[
 \lambda_{\min}\left(\frac{\mathsf H_0^\top\mathsf H_0}{mn}\right)
 \ge\lambda/2,
 \quad\mathsf H_0=[h_0^{(L)}(v_a)]_{a=1}^m.
 \tag{6}
\]

## 3. General all-time theorem on the same event

For every label vector satisfying

\[
 0<Y\le\frac{\gamma}{8mH\sqrt F},
 \tag{7}
\]

the solution exists for all physical time, all its parameters converge,
and its final predictions fit every training label. On event (6),
simultaneously for all t>=0,

\[
 \|A(t)\|_{\rm op}/\sqrt n<9,\quad
 \max_{\ell\ge2}\|W^{(\ell)}(t)\|_{\rm op}<9,\quad
 \sup_{\|v\|=1,\ell}\|h^{(\ell)}(t,v)\|_2/\sqrt n<2H,
\]
\[
 \lambda_{\min}\left(\frac{\mathsf H(t)^\top\mathsf H(t)}{mn}\right)
 \ge\lambda/4,\qquad
 \rho(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\lambda t/2},\qquad
 \int_0^\infty\rho(t)\,dt\le2Y/\lambda.
 \tag{8}
\]

Use the parameter norm

\[
 \|\theta\|_{\rm par}^2=
 \|A\|_F^2/n+\sum_{\ell=2}^L\|W^{(\ell)}\|_F^2+\|w\|_2^2/n.
\]

Then

\[
 \int_0^\infty\|\dot\theta(t)\|_{\rm par}\,dt
 \le2Y/\sqrt\lambda,\qquad
 \|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda.
 \tag{9}
\]

The sharper hidden displacement bounds are

\[
 \frac{\|A(t)-A_0\|_F}{\sqrt n}
 \le8U_1Y^2/\lambda^{3/2},\quad
 \|W^{(\ell)}(t)-W_0^{(\ell)}\|_F
 \le8U_\ell Y^2/\lambda^{3/2},
\]
\[
 \sup_{\|v\|=1}\frac{\|h^{(\ell)}(t,v)-h_0^{(\ell)}(v)\|_2}{\sqrt n}
 \le8F_\ell Y^2/\lambda^{3/2}.
 \tag{10}
\]

The whole-sphere endpoint tail is fully explicit:

\[
 \sup_{\|v\|=1}|f_n(\infty,v)-f_n(t,v)|
 \le16\left(H^2+FY^2/\lambda\right)
       \frac Y\lambda e^{-\lambda t/2}
 \le\frac{65}4H^2\frac Y\lambda e^{-\lambda t/2}.
 \tag{11}
\]

If Y=0, the readout and all moving parameters remain at initialization,
and f_n is identically zero. No division by Y is needed in that case.

## 4. Proof of the quantitative initialization event

Two 1/4 nets in the unit spheres, each of cardinality at most 9 to its
ambient dimension, give ||W||op<=2max_net|u^T Wv|. Scalar Gaussian
tails therefore imply

\[
 \Pr\{\|W_0^{(\ell)}\|_{\rm op}>8\}
 \le2e^{-(8-2\log9)n},\qquad
 \Pr\{\|A_0\|_{\rm op}/\sqrt n>8\}
 \le2e^{-(8-\log9)n+d\log9}.
 \tag{12}
\]

The second and third width terms in (5) make their union loss at most
(L-1)delta/(4L)+delta/4<delta/2.

We next quantify covariance propagation. For a centered Gaussian pair
with covariance C and diagonal at most 2H^2, let
Psi_ell(C)_ab=E phi_ell(Z_a)phi_ell(Z_b). Differentiating its Gaussian
density and integrating by parts gives, along a covariance direction E,

\[
 D\Psi_\ell(C)[E]_{ab}=
 \tfrac12 E_{aa}\mathbb E[\phi_\ell''(Z_a)\phi_\ell(Z_b)]
 +E_{ab}\mathbb E[\phi_\ell'(Z_a)\phi_\ell'(Z_b)]
 +\tfrac12 E_{bb}\mathbb E[\phi_\ell(Z_a)\phi_\ell''(Z_b)].
 \tag{13}
\]

The same formula for a diagonal entry collects these three terms into
E_aa E[(phi')^2+phi phi'']. Linear growth and bounded derivatives
justify the integrations and differentiation by Gaussian domination.
For singular covariance endpoints, apply the integrated formula first
to C+epsilon I along the segment, and let epsilon decrease to zero.
Dominated convergence proves the same difference bound on the positive
semidefinite cone. Cauchy--Schwarz gives E|phi(Z)|<=b+sqrt(2)sH, hence

\[
 \|\Psi_\ell(C)-\Psi_\ell(C')\|_{\max}
 \le A_*\|C-C'\|_{\max}
 \tag{14}
\]

whenever both covariance diagonals are at most 2H^2. The scalar variance
map has the same Lipschitz coefficient.

For such Gaussian inputs, E|phi(Z)|^4<=M_4: use
(u+v)^4<=8(u^4+v^4) and E Z^4<=12H^4. The conditional variance of a
product phi(Z_a)phi(Z_b) is then at most M_4 by Cauchy--Schwarz.
Every initialized hidden layer has n conditionally independent Gaussian
rows with covariance equal to its preceding empirical feature Gram.
Chebyshev therefore bounds each empirical covariance entry's deviation
from its conditional expectation by M_4/(n epsilon^2) at tolerance
epsilon=e/T_L. The first layer obeys the same statement without
conditioning, with covariance Q^(0).

Use an h-net on the query sphere of cardinality at most P, obtained
by a maximal h-separated set and the disjoint-ball volume bound. At each
layer we need the m^2 training covariance entries and only the P
individual net-query squared norms, not the entire combined Gram.
Inductively, as long as preceding deviations have passed their tests,
(14) bounds every covariance error by
epsilon sum_(j=0)^(ell-1) A_*^j<=e. Thus each conditional input variance
is at most H^2+e<2H^2, closing the condition used in Chebyshev. A stopped
conditional union bound over all L layers gives total failure at most

\[
 \frac{L(m^2+P)M_4T_L^2}{ne^2}\le\delta/2.
 \tag{15}
\]

On this event the top training empirical Gram differs entrywise from
Q^(L) by at most e<=gamma/(2m). Its operator error is at most me, so
its least eigenvalue is at least gamma/2. Dividing by m proves the last
line of (6).

On the matrix event, v -> h_0^(ell)(v)/sqrt(n) is Lipschitz in Euclidean
norm with coefficient at most (8s)^ell. A net-query norm is at most
sqrt(H^2+e)<=sqrt(5/4)H. The off-grid increment is at most
(8s)^L h<=H/4, including the case h=1/2. Since
sqrt(5/4)+1/4<3/2, the sphere bound in (6) follows. The two losses
(12),(15) sum to at most delta. No population-training comparison has
been used.

## 5. Proof of all-time fitting and physical bounds

Work initially until the first exit from mixer caps nine, feature cap
2H, or mean readout-Gram gap lambda/4. Backward propagation on this
tube gives ||delta_a^(ell)||_2/sqrt(n)<=D_ell||w||_2/sqrt(n).
Each hidden block's velocity in its normalized Frobenius norm is at most
2rho U_ell||w||_2/sqrt(n), by Cauchy--Schwarz in the sample index.

The flow (1) has the exact energy identity

\[
 -\frac d{dt}\rho^2=\|\dot\theta\|_{\rm par}^2.
 \tag{16}
\]

The readout block alone yields
-d(rho^2)/dt>=4(lambda/4)rho^2=lambda rho^2. Therefore
rho(t)<=Y exp(-lambda t/2) and int rho<=2Y/lambda on the stopped
interval. Weighted Cauchy--Schwarz and (16) give

\[
 \left(\int\|\dot\theta\|_{\rm par}\right)^2
 \le\left(\int\frac{\|\dot\theta\|_{\rm par}^2}{\rho}\right)
      \left(\int\rho\right)
 \le(2Y)(2Y/\lambda).
 \tag{17}
\]

This is first applied while rho>0. If zero loss is reached, every velocity
vanishes and continuation is constant. Because w_0=0, (17) bounds its
RMS norm by 2Y/sqrt(lambda). Integrating the hidden velocity estimates
gives the first two bounds in (10).

For arbitrary unit query v, Lipschitz continuity of phi and the tube
bounds give the feature subtraction recursion

\[
 \frac{\|h^{(1)}(t,v)-h_0^{(1)}(v)\|_2}{\sqrt n}
 \le s\frac{\|A(t)-A_0\|_F}{\sqrt n},
\]
\[
 \frac{\|h^{(\ell)}(t,v)-h_0^{(\ell)}(v)\|_2}{\sqrt n}
 \le s\left[2H\|W^{(\ell)}(t)-W_0^{(\ell)}\|_F
       +9\frac{\|h^{(\ell-1)}(t,v)-h_0^{(\ell-1)}(v)\|_2}{\sqrt n}
       \right].
\]

This proves the final bound in (10), with (4)'s exact F_ell.
Under (7), all hidden displacements and feature displacements are at most

\[
 8F Y^2/\lambda^{3/2}\le\sqrt\lambda/(8H^2)\le1/(8H).
 \tag{18}
\]

Thus the matrix caps improve from nine to at most 8+1/8, and the feature
cap improves from 2H to at most 3H/2+H/8. The change of the training
feature matrix divided by sqrt(mn) has operator norm at most
sqrt(lambda)/(8H^2)<=sqrt(lambda)/8. Its minimum singular value therefore
stays at least sqrt(lambda)(1/sqrt(2)-1/8)>sqrt(lambda)/2. This strictly
improves the stopped Gram gap. No finite first exit is possible.

For fixed finite n, all parameter norms remain bounded on every finite
time interval by (17), so the locally Lipschitz finite-dimensional field
continues globally. Its finite total path length implies convergence of
every parameter. Exponential residual decay proves interpolation.

Finally ||dot w||_2/sqrt(n)<=4Hrho. The instantaneous version of the
feature recursion gives ||dot h^(L)(v)||_2/sqrt(n)<=2rho F||w||_2/sqrt(n).
Consequently

\[
 |\dot f_n(t,v)|\le8(H^2+FY^2/\lambda)\rho(t).
\]

Integration proves (11). Its last simplification uses
FY^2/lambda<=lambda/(64H^2)<=1/64 and H>=1. The bound is uniform on
the whole sphere and in physical time, including the limit. This
completes the general fitting proof.

## 6. Relation to the proposed beta envelope

For the strip class, define the contract's activation envelope explicitly:

\[
 \beta_\partial=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,
 \frac{16}{a},\quad
 \max_{\ell,\,j=1,2,3}\sup_{|\operatorname{Im}z|\le a/2}
          |\phi_\ell^{(j)}(z)|\right\}.
\]

It is finite because the first derivative is bounded on the full open
strip and Cauchy's formula bounds its derivatives on the half-strip.
In particular beta_partial>=10. Then b<=beta_partial, s<=beta_partial,
and the Gaussian recursion gives
H<=(2beta_partial)^L. Since 9s>=9,

\[
 F\le\frac{21}{20}H^2s^2(9s)^{2L-2},\qquad
 8H\sqrt F\le H^2(9s)^L
 \le36^L\beta_\partial^{3L}\le\beta_\partial^{5L}.
\]

Hence the explicitly simpler cap

\[
 Y\le(\gamma/m)\beta_\partial^{-5L}
 \tag{19}
\]

already implies (7). In particular the proposed much smaller
beta_partial^(-62L) cap is sufficient for this REAL FITTING component.
This does not prove it sufficient for every probabilistic source budget,
complex analytic source estimate, compact runtime, or dense fluctuation
comparison. Those are separate bridges in the merged study.

The exact Gaussian moment formula (2) is preferable to its beta envelope
for normalized or otherwise variance-stable activations: when all q_ell=1,
H=1 and (4)--(11) recover the sharper normalized fitting formulas without
making normalization a hypothesis of this general theorem.
