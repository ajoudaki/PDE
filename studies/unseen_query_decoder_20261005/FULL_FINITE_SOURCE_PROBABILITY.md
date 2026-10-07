# Finite-confidence composition for the training-query source

2026-10-07. Internally checked scoped author result. This file assembles the all-deletion
initialization, normalized nonlinear insertion, independent-cavity moments,
and finite-confidence stopping argument. The added calculation is the
training-response observable needed to remove the complex pole stop. It is
not an independent reconstruction or a decoder error theorem.

**Status:** the finite set of training queries has a fresh independent
reconstruction in FULL_FINITE_SOURCE_PROBABILITY_CHECK.md, at frozen hash
`2a7bfd057b33d79970d39fa2a98340203bc8e80b55944e5ef49f200ff4510c40`.
It verifies the new augmented-response calculation and finite probability
composition with the very conservative polynomial width (3) below.
The raw derivative normalization clarification requested there is included
below; it changes neither the Gaussian grid nor the width. No claim
about a whole-sphere *complex* source or the decoder's final comparison
error is made. The maintained dense fitting theorem already supplies the
whole-sphere real trajectory and endpoint statements used by the physical
solver.

## 1. Statement, preserved assumptions, and probability allocation

Use exactly the network, independent Gaussian initialization, zero readout,
loss, and physical optimizer of `EXPLICIT_FITTING_WIDTH.md`. Thus

\[
z_a^{(1)}=Av_a,\quad z_a^{(j)}=W^{(j)}h_a^{(j-1)},\quad
h_a^{(j)}=\phi_j(z_a^{(j)}),\quad f_a=w^\top h_a^{(L)}/n,
\quad r_a=f_a-y_a,
\]

where \(v_a\in S^{d-1}\), \(m\ge d\), and

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad \dot W^{(j)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(j)}h_a^{(j-1)\top},
\quad \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\]

The backward definitions are
\(k_a^{(L)}=w\), \(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)}\),
and \(k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}\).
Let \(\gamma>0\) be the unweighted population feature-Gram gap,
\(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m\), and
\(S=16Y/\lambda\). The activation strip and \(\beta\) are exactly
those of the fitting note, including unbounded activation values.

Retain the complete original intersection of label conditions. In
particular retain the fitting condition
\(Y\le\lambda/(8H\sqrt F)\), with its original \(H,F\), and
\(S\le S_*^{\rm src}\) from
`UNBOUNDED_COMPRESSOR_BRIDGE.md` (10). All source constants
\(H_j,k_j,\tau_j,P_j,f_j,A_*,D_*,H_*,D_0,D_1,C_F,C_{\rm abs},
V_j,G_j,W_{\rm G},\eta,\mathcal B,K_{\rm src}\)
retain their exact finite recurrences (5)--(10), (22) of that file.
These constants are deterministic functions of depth and the activation
envelope; they are not additional probabilistic assumptions. In particular
\(\mathcal B=1024e^2L\). No smaller label condition is substituted.

For \(0<\delta<1/4\), set

\[
p=\max\left\{1,\left\lceil
 \frac{\log(4emL/\delta)}{\log(64e^2)}\right\rceil\right\},
\qquad \ell=\log(en),
\tag{1}
\]

\[
\mathcal A=\beta^{2000L}(1+\lambda^{-1})^4(m+d+p+1)^4.
\tag{2}
\]

The proposed explicit sufficient width is

\[
n\ge \left\lceil(\mathcal A/\delta)^{20000}\right\rceil.
\tag{3}
\]

At each such individual width, the claimed event has probability at least
\(1-\delta\). It contains the original full-network fitting event and
has these source properties on a neighborhood of the closed time rectangle

\[
\mathcal D_n=[-r_t,32\ell/\lambda+r_t]+i[-r_t,r_t],
\qquad
r_t=\frac1{p\beta^{100L}(1+\lambda)\sqrt\ell}:
\tag{4}
\]

all training forward/backward sources are holomorphic; their original RMS
bounds hold; every joint sample budget is below \(\mathcal B\); and

\[
\max_{a,j,i,z\in\mathcal D_n}|z_{a,i}^{(j)}(z)|
 \le K_{\rm src}\sqrt\ell,\qquad
\max_{a,j,i,z\in\mathcal D_n}|k_{a,i}^{(j)}(z)|
 \le SK_{\rm src}\sqrt\ell.
\tag{5}
\]

The four actual source families and initialized images therefore have
the original RMS and coordinate-magnitude bounds on (4). All probabilities
are over the actual finite initialized network. No lower bound on positive
\(Y\) is present. At \(Y=0\), the predictor is exactly stationary;
no formula dividing by \(S\) is used for that branch.

The exponents in (3) are intentionally loose: the activation factor is
\(\beta^{40000000L}\), the gap factor is
\((1+m/\gamma)^{80000}\), and the displayed algebraic confidence factor
is \(\delta^{-20000}\). The factor involving \(p\) is only logarithmic
in confidence. This is a sufficient theoretical bound, not a proposed
practical onset.

## 2. A single event initializes every required cavity

Apply the fitting initialization proof with failure \(\delta/32\).
Its actual sphere-net argument gives initial feature RMS at most
\(11H/8\), not merely the displayed weaker \(3H/2\), and normalized
training Gram at least \(\lambda/2\). Its conditional Gaussian argument
also gives, outside probability \(\delta/32\),

\[
Z_0:=\max_{a,j,i}|z_{a,i}^{(j)}(0)|
 \le 2H\sqrt{2\log(64nmL/\delta)}.
\tag{6}
\]

The stopped Chebyshev calculation in its Section 6 gives initial sample
budgets at most \(8L\), with failure at most \(15mL/(16n)\).
Every carrier initially vanishes. Gaussian norm concentration adds the
event that every initialized hidden row and column has Euclidean norm at
most two, with failure at most \(4nL e^{-n/2}\). The first-layer
incoming rows do not enter a reverse source and need no such norm bound.

Delete a set \(I\) of at most \(p\) neurons from one layer. This is
rectangular removal of activations, always with normalization \(n\).
Set \(A_0^{\rm init}=b+sZ_0\). Zero-embedding the cavity features,
the missing vector at the deletion layer has norm at most
\(\sqrt p A_0^{\rm init}\). All subsequent initialized forward
differences have Euclidean norm at most

\[
D_{\rm init}=(8s)^L\sqrt p A_0^{\rm init}.
\tag{7}
\]

Indeed the first omitted forcing is a restriction of the initialized
mixer applied to the omitted feature vector; its operator norm is at
most eight. Each later difference is multiplied by a mixer and an
activation slope, costing at most \(8s\). Restriction of any first
weight or hidden operator cannot increase its norm. Formula (7) holds
simultaneously for all deletion sets; no union over cavity Gram laws is
needed.

The width (3) makes

\[
D_{\rm init}/\sqrt n\le\min\{H/8,\sqrt\lambda/32\}.
\tag{8}
\]

Thus every cavity starts with training feature RMS below \(3H/2\)
and normalized feature-matrix least singular value at least
\((1/\sqrt2-1/32)\sqrt\lambda\). The fitting proof uses only
training feature bounds for a training cavity. Under its *unchanged*
label condition the later feature-matrix motion is at most
\(\sqrt\lambda/8\). Hence every cavity retains a singular value
strictly above \(\sqrt\lambda/2\), and has the original
\(\lambda/4\) Gram margin and physical tube. No whole-sphere cavity
feature estimate is needed here; the full network's whole-sphere estimate
remains the one in the fitting theorem.

The initial joint-budget comparison additionally needs coordinate
localization. At any layer above the deleted layer, condition on all lower
initialized layers. The difference vector in (7) is then independent of
the current Gaussian row. Project it onto the deterministic ball of
radius (7) before pairing. Each coordinate pairing has variance at most
\(D_{\rm init}^2/n\), so at threshold \(n^{-1/10}\) its tail is

\[
2\exp\{-n^{4/5}/(2D_{\rm init}^2)\}.
\tag{9}
\]

Here (7) can first be replaced by the deterministic upper bound obtained
from (6). Projection agrees on the initial event. This conditioning is
performed before restricting the current matrix by its operator event.
There are at most \(pLn^p\) deletion sets and \(mLn\) scalar tests
per set. Their union in (9) has probability below \(\delta/32\)
under (3). At the deleted layer retained coordinates agree exactly.
Consequently each cavity initial sample budget is at most
\(e^{\eta n^{-1/10}}8L+p/n<\mathcal B/2\).

The fitting failure, (6), initial budget failure, row/column norm failure,
and (9) total less than \(\delta/4\). Denote this common initial
event by \(E_0\). Each independent cavity also has its *own*
initialization test. If it fails, all its Gaussian reference paths are
defined to be zero. This convention is used before integrating any omitted
root and is essential when later dropping \(1_{E_0}\).

## 3. Scaled local insertion and explicit finite gates

Use mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\) and
\(\bar u=(\Theta-\Theta_0)/S\). Forward ports remain unscaled,
while \(\bar k=k/S\), \(\bar\delta=\delta/S\), and
\(\bar q=q/S\). The exact retained equation is

\[
\dot{\bar u}=-\frac2m\sum_a\bar r_a
 [\nabla_{\bar u}\bar F_a+D_{\bar u}h_a^{(j-1)\top}\bar q_a],
\quad \bar F_a=F_a/S,\quad \bar r_a=r_a/S.
\tag{10}
\]

In particular \(D_{\bar u}h=S D_\Theta h\). Zero initial readout
makes \(\bar F_a=\bar u_w^\top h_a^{(L)}\); it introduces no
inverse activity into a derivative coefficient. At the top, retain the
complete omitted prediction offset multiplying both terms in (10).

Full joint budgets stop at \(\mathcal B\); cavity budgets stop at
\(2\mathcal B\). Temporary full maxima are twice (5), and cavity
maxima four times (5). Full and cavity pole stops are respectively
\(3a/8\) and \(7a/16\). Training response stops are specified in
Section 4. References are autonomous cavities stopped by their own rules.

On these stops the raw carrier cap is

\[
M_n=\eta^{-1}\log(2n\mathcal B)\le M_0\ell,
\qquad M_0=\eta^{-1}[1+\log(2\mathcal B)],
\tag{11}
\]

and the propagator satisfies the finite, unabsorbed estimate

\[
\|J(t,s)\|\le J_0 n^{1/4000},\qquad
J_0=2e^{1/4}(2\mathcal B)^{1/4000}.
\tag{12}
\]

This follows from the original allowance
\(SA_*\le1/4\), \(S^2D_*/\eta\le1/4000\), real negative-Gram
contraction, and the short-contour norm cost at most two.

Use all the explicit Gaussian-map recurrences in
`QUANTITATIVE_INSERTION_WIDTH.md` (23)--(28) and
`INSERTION_MAP_MODULI.md` (4)--(22). They include the adaptive-residual
rank-one term, the independent reverse probes, and centered quadratic
traces. Sections 4--5 below add the training response maps. No constant
depending implicitly on deletion count is imported.

For later finite estimates the following coefficient ledger is useful.
It bounds coefficients after removing the displayed powers of \(\ell\),
\(n\), and \(\sqrt p\). The entries are intentionally enlarged.

| Quantity | Bound |
| --- | --- |
| All persistent source constants except \(\eta^{-1}\), \(M_0\) | \(\beta^{80L}\) |
| \(\eta^{-1}\), \(M_0\), raw control amplitudes | \(\beta^{80L}\) |
| Coefficients (4)--(20) of `INSERTION_MAP_MODULI.md` | \(\beta^{300L}(1+\lambda^{-1})\) |
| Added training-response map/modulus coefficients | \(\beta^{1000L}(1+\lambda^{-1})^2\) |
| Scaled local nonlinear and learned-source coefficients, including contour length | \(\beta^{1000L}(1+\lambda^{-1})^2(1+p)^2\) |

For the first rows, substitute \(H_j,P_j\le\beta^{3L}\),
\(k_j\le\beta^{5L}\), \(\tau_j\le\beta^{6L}\) in the explicit
source sums. This gives \(A_*\le\beta^{11L}\),
\(D_*\le\beta^{8L}\), \(H_*\le\beta^{13L}\),
\(D_0\le\beta^{30L}\), \(C_{\rm abs}\le\beta^{32L}\),
\(W_{\rm G}\le\beta^{23L}\), \(\eta^{-1}\le\beta^{57L}\),
and \(K_{\rm src}\le\beta^{42L}\). Numerical factors and finite
sums are paid using \(L\le\beta^L\), \(\beta^L\ge100\).
For the map row, the largest operation is a backward forcing with one
factor \(M_0\); time differentiation adds one further such factor.
Their propagation multipliers are \(10s\). Direct substitution gives
the stated \(300L\) envelope, with horizon degree one. Section 4
gives the additional products accounting for the next row. The last row
uses the complex coefficient \(\beta^{240L}\), cutoff degree at most
three, and at most one contour-length factor.

The width (3) implies the single useful absorption inequality

\[
\mathcal A\ell^{16}\le n^{1/1000}.
\tag{13}
\]

To check it, put \(u=\log\mathcal A\ge4000\log10\).
At \(\log n=20000u\),
\(\log\mathcal A+16\log(1+\log n)\le17u<20u\).
Here \(\log(1+20000u)\le u\). The difference only improves
thereafter because the derivative of
\(\log n/1000-16\log(1+\log n)\) is positive. Replacing
\(\mathcal A\) by \(\mathcal A/\delta\) enlarges the available
right side. Formula (13) is the actual finite absorption used below.

For deterministic controls and a fixed cavity, every enlarged linear map
has operator norm at most \(n^{1/200}\); each centered quadratic
matrix has the same bound. Their Gaussian input dimension is at most
\(2pn\). Coordinate thresholds \(n^{-1/10}/8\), the Gaussian
square calculation, and (13) give tails at most
\(4e^{-n^{0.78}}\). The Euclidean-image thresholds \(n^{1/100}\)
have stronger tails: their means are bounded by
\(\sqrt{2p}\,n^{1/200}<n^{1/100}/2\), and Gaussian Lipschitz
concentration supplies the remaining margin. Independent lower probes
and their forward images are included in this statement.

The enlarged controls have amplitude bounded by a coefficient times
\(\ell\), speed bounded by a coefficient times \(\sqrt n\ell^3\),
and at most \(4p(m+1)^2\) real components. A mesh at accuracy
\(n^{-1/8}\) has logarithmic cardinality at most
\(\mathcal A\ell^8 n^{5/8}\le n^{0.627}\). Linear and centered
quadratic control interpolation errors are less than
\(n^{-1/10}/8\): apply their operator moduli and
\(\|g\|\le2\sqrt{2p}\), retaining the trace contribution
\(2p\|\Delta R\|\). A terminal mesh of size
\(n^{-2}/(1+\mathcal A\ell^8)\) makes time interpolation smaller
than the same threshold and has at most \(n^6\) points. The number
of coordinate, probe, norm and pairing tests is at most
\(\mathcal A n^3\). A union over all \(pLn^p\) deletion sets,
the control nets and terminal grids therefore has failure less than

\[
\exp(-n^{7/10})<\delta/16.
\tag{14}
\]

All reference operations in this argument are measurable in retained
initialization. Actual adaptive controls are substituted only after the
uniform event has been established.

## 4. The additional training-response calculation

This section supplies the part not proved by the earlier h/δ map note.
It is needed even though the final real query set is the entire sphere:
only the finite training set needs a complex neighborhood in the physical
solver.

For evaluated training sample \(b\) and driving sample \(a\), define

\[
R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta F_a,
\quad Q_{ba}^{(j)}=\phi'_j(z_b^{(j)})\odot R_{ba}^{(j)},
\quad \bar R_{ba}^{(j)}=R_{ba}^{(j)}/S,
\quad \bar Q_{ba}^{(j)}=Q_{ba}^{(j)}/S.
\tag{15}
\]

The exact recurrences are

\[
\bar R_{ba}^{(1)}=\bar\delta_a^{(1)}v_a^\top v_b,
\quad
\bar R_{ba}^{(j)}=\bar\delta_a^{(j)}
 \frac{h_a^{(j-1)\top}h_b^{(j-1)}}n
 +W^{(j)}\bar Q_{ba}^{(j-1)},
\quad \bar Q_{ba}^{(j)}=\phi_j'(z_b^{(j)})\odot\bar R_{ba}^{(j)}.
\tag{16}
\]

There is no division by activity in (16)'s coefficients. Equivalently,
use the effective network whose physical hidden parameters are unchanged
and whose readout is \(\bar u_w\). Its ordinary mobility-gradient
response is exactly \(\bar R\): preactivations do not depend on the
readout, so the readout block of that gradient has no contribution.

Use the explicit mixed-endpoint constants \(r_j,q_j,e_j,T_Q\) of
the integrated source (24). For finite training pairs, replace its
whole-query Gaussian multiplier \(16\sqrt{d+3}\) by 64 and define

\[
U_1=4sK_{\rm src},\qquad
U_j=2\{sK_{\rm src}[H_{j-1}^2+f_{j-1}^2+ST_Q
 +S^2H_{j-1}q_{j-1}]+64q_{j-1}+1\}.
\tag{17}
\]

The same recurrence has \(U_*:=\max_jU_j\le\beta^{72L}\):
\(g\le\beta^{10L}\), \(r_j\le\beta^{13L}\),
\(q_j\le\beta^{14L}\), \(e_j\le\beta^{21L}\), and
\(T_Q\le\beta^{27L}\), together with the preceding bound on
\(K_{\rm src}\), verify this. The temporary full response caps are
\(2U_j\sqrt\ell\), the cavity caps \(4U_j\sqrt\ell\).
All normalized responses initially vanish.

Here are the local additions to the Gaussian-map event. If the deleted
layer is \(j\), its retained response recurrence at layer \(j+1\)
has the additional port
\(\sum_{i\in I}x_i\bar Q_{ba,i}^{(j)}\).
The learned-column correction is bounded by the product of the learned
column bound and the actual response cap. The deleted contribution to
\(n^{-1}h_a^\top h_b\) is at most
\(p(b+sM_n)^2/n\); multiplying it by a response of RMS at most
\(\tau_j\) gives an allowed \(n^{-1/2}\) vector remainder.
These terms cannot be dropped when transferring a response cap across a
deletion.

There is also a direct reverse observable below the deleted layer. At
layer \(j-1\), write \(C_b=D_\Theta h_b^{(j-1)}\). The exact
unscaled observable is

\[
Q_{ba,\mathrm{full}}^{(j-1)}
 =C_b[\nabla_\Theta F_a+C_a^\top q_a].
\tag{18}
\]

Thus the normalized additional observable is \(C_bC_a^\top\bar q_a\).
Its reference linear term must be included, together with every reference
forward variation obtained by applying the lower forward Jacobians to
\(C_a^\top y_i\). These are centered Gaussian vectors, with
operator coefficients bounded by a fixed power of \(\beta^L\).
They are the additional probes in (14).

For completeness, the nonlinear control of (18) is explicit. Put
\(\xi=C_a^0{}^\top y_i\). On the Gaussian probe event,
\(\|\xi\|\le\beta^{20L}\), and all its reference forward
variations have coordinate maximum at most \(d_0=n^{-1/10}\).
Along a hidden-parameter displacement of norm at most \(N+u\),
subtract the directional forward recurrences in direction \(\xi\).
Each changed gate multiplies its reference directional feature, at most
\(d_0\) per coordinate. The terms
\(\xi_H\Delta h/\sqrt n\) and
\(\Delta H Dh_0[\xi]/\sqrt n\) retain their width factor.
Propagation uses only the perturbed mixers and slopes. Consequently

\[
\|(C_b^1-C_b^0)\xi\|
 \le\beta^{50L}(d_0+n^{-1/2})(N+u).
\tag{19}
\]

The other term in the product subtraction,
\(C_b^1(C_a^1-C_a^0)^\top y_i\), is bounded by the reverse-probe
estimate of `FIXED_ORDER_INSERTION_JETS.md` (21), multiplied by
\(\|C_b^1\|\le\beta^{10L}\). Summing (19) and that estimate
with the actual controls \(|\bar b_{a,i}|\le sM_n\) gives

\[
\|C_b^1C_a^1{}^\top\bar q_a
       -C_b^0C_a^0{}^\top\bar q_a\|
 \le\beta^{70L}(1+p)(1+M_n)
 [d_0(N+u+(N+u)^2)+(N+u+(N+u)^2)/\sqrt n].
\tag{20}
\]

This bound retains the small coordinate factor. An arbitrary operator
bound on \(C_b^1-C_b^0\) would not suffice.

The rest of the augmented remainder follows directly from (16). For
the feature pairing \(c_{ab}=h_a^\top h_b/n\), its first variation
is at most \(\beta^{10L}(N+u)/\sqrt n\), and its Taylor remainder
is at most

\[
\beta^{40L}\{(R+P)/\sqrt n+(N+u)^2/n\},
\quad R=d_0N+d_0u+u^2,\quad P=(N+u)^2/\sqrt n.
\tag{21}
\]

This is obtained by the exact product subtraction used for the gradient
block in the fixed-order lemma. Multiplication by a reference
\(\bar\delta\) uses its RMS and cancels the first \(\sqrt n\).
Products of two changed factors retain \(1/\sqrt n\).
For \(\bar Q=\phi'(z)\bar R\), use the exact gate subtraction
used there for \(\delta=\phi'(z)k\). Its homogeneous term contains
the perturbed bounded slope; the reference \(\bar R\) cap occurs
only in the additive gate remainder. In the next layer, propagation is
by the perturbed mixer. Hence there is no power of a coordinate cutoff
growing with depth. Equations (20)--(21), and these two exact product
subtractions, give the common augmented remainder bound

\[
\beta^{240L}(1+p)^2(1+M_n+4U_*\sqrt\ell)^3
 [R+P+d_0(N+u+(N+u)^2)]
\tag{22}
\]

in complex Euclidean norm. The coefficient is enlarged to cover learned
response ports and the omitted feature-pairing term, each with its
additional \(n^{-1/2}\) factor. The linear response and derivative
on the unlocalized parameter remainder are kept separate, as in the
scaled insertion lemma. Every auxiliary scalar Taylor segment is inside
\(a/2\) under its stated local strip gate; fourth derivatives, if
used in differentiating the enlarged maps, are at most \(\beta^4\)
there by Cauchy's formula for \(\phi''\).

The map and modulus ledger in Section 3 can also be checked without a
new implicit graph constant. Differentiate (16) once: the terms are a
linear backward response times \(c_{ab}\), a reference backward
response times the scalar pairing variation, a changed mixer times a
reference \(\bar Q\), and a propagated linear \(\bar Q\).
The linear gate term is \(\phi''\bar R_0 z_{[1]}\), so it adds
one reference response cap. Including (18)'s direct map and the response
port, every linear map has coefficient bounded by

\[
\beta^{100L}(1+M_0+4U_*)^2(1+C_0)^2,
\tag{23}
\]

times \(\sqrt p n^{1/4000}\ell^5\), where \(C_0\) is the
maximum of the raw coefficients (4)--(20) in
`INSERTION_MAP_MODULI.md` and one. The control modulus uses the same
coefficient and at most \(\ell^4\); the time modulus uses it and
at most \(\sqrt n\ell^8\). With the preceding \(300L\) bound,
(23) is at most \(\beta^{1000L}(1+\lambda^{-1})^2\).
Products and transposes giving quadratic matrices preserve these bounds.

To check the essential control speed, differentiate (16) in time. The
potentially large gate product is
\(\phi''\dot z\,\bar R\); use the *stopped coordinate* bound
on \(\bar R\) and the RMS bound on \(\dot z\). Its RMS has
no factor \(\sqrt n\). All other terms use the previous layer's
RMS response speed, \(\dot{\bar\delta}\), normalized feature
pairing speed, and mixer speed. Induction gives an RMS speed bounded
by a coefficient times \(\ell^2\). Conversion to a scalar control
speed costs one \(\sqrt n\), exactly the speed charged in Section 3.
For time differentiation of the linear maps the reference coordinate
speeds cost that same single \(\sqrt n\); all propagated derivative
terms use \(10s\). This verifies the entropy exponent used in (14).

## 5. Nonlinear bootstrap and transfer of all stops

For each deletion set, subtract its independently stopped zero-source
reference and its Gaussian linear variation. Write the remaining scaled
mobility displacement as \(U\), with
\(\|U\|\le u=n^{-1/25}\) on a first-exit prefix. The uniform
event (14) gives linear Euclidean radius \(N=n^{1/100}\) and vector
coordinate radius \(d_0=n^{-1/10}\), including the enlarged
observables and all needed probes.

`SCALED_INSERTION_REMAINDER.md` (20), with its complex coefficient,
keeps the exact reverse force and adaptive residual. Its integrated
forcing, including learned directions and the complete top offset, is
bounded by

\[
\mathcal A\ell^8 n^{1/4000}
 [n^{-8/100}+u^2+n^{-48/100}+n^{-1/2}].
\tag{24}
\]

This uses \(2\int\bar\rho|dt|\le1\), contour length at most
\((32/\lambda+2)\ell\), and (12). By (13), (24) is strictly
less than \(n^{-1/25}/2\). Thus continuity closes every scaled
parameter remainder. All local size and strip gates in the fixed-order
lemma also follow from (13), including
\(d_0+\beta^{10L}u+\beta^{30L}(R+P)<a/32\).

The forward/backward Taylor estimates, the reverse probe correction
below the deleted layer, and (22) then give on the common stopped prefix

\[
\max_{\mathrm{retained}\ a,j,i}
 (|\Delta z_{a,i}^{(j)}|+|\Delta\bar k_{a,i}^{(j)}|)
 \le n^{-1/30},
\quad
\max_{a,b,j,i}|\Delta\bar R_{ba,i}^{(j)}|\le n^{-1/30},
\tag{25}
\]

and ordinary Euclidean discrepancies of lower features and upper scaled
responses at most \(2n^{1/100}\). The matrix source corrections
retain \(S^2\) where present; no unscaled error has been divided by
\(S\) after taking a bound.

Running maxima differ by the same coordinate bounds. For each sample,

\[
\mathcal H_a^{-I}\le e^{2\eta n^{-1/30}}\mathcal H_a+p/n
 <2\mathcal B\qquad(\mathcal H_a\le\mathcal B).
\tag{26}
\]

Equation (25) also transfers the doubled coordinate and response caps,
and the pole gap \(a/16\). Therefore no cavity stop can occur first.
This is a strict-margin prefix argument; full-network survival is never
an event on which a Gaussian law is conditioned.

The singleton scalar trace calculation from the integrated bridge,
Sections 3--4, now has a finite error at most \(n^{-1/40}\).
The contributions to this error are (25)'s nonlinear endpoint error,
centered forms on (14), the learned small sources, and the adaptive
rank-one trace. The latter is at most
\(\mathcal A\ell^8 n^{-1+1/4000}\). The nonvanishing direct,
reverse, and residual-Hessian traces remain exactly the source's displayed
ones, with their actual control amplitudes. Its RMS scalar absorption
therefore gives

\[
Z_{a,i}+K_{a,i}/S\le C_{\rm abs}
 [1+G_{h,a,i}+G_{\delta,a,i}/S+
       \overline G_{h,i}+\overline G_{\delta,i}]+n^{-1/40}.
\tag{27}
\]

Here each reference belongs to the independently stopped singleton;
bars are sample RMS, not maxima over samples. The coefficient is the
original singleton coefficient, independent of \(p\).

The scalar Gaussian references on the stopped complex rectangle have
bounded coefficient RMS. For deterministic interpolation of a root-paired
reference, a safe raw derivative bound also pays the single
\(\sqrt n\) conversion from the normalized Euclidean bound;
it is at most \(\sqrt n\) times a coefficient times \(\ell^2\).
A time mesh of size \(n^{-2}\) still makes its interpolation error
negligible and has at most
\(n^5\) points after (13). The coordinate maxima use Gaussian
tails at \(C_G\sqrt\ell\), where
\(C_G=32\max(1,H_{\max},\tau_*)\). Including neurons, samples,
layers and interpolation, failure is at most \(n^{-100}\).
Equation (27) then improves the temporary coordinate stops to (5).
This maximum step uses variance and a grid, not the moment argument.

For the training responses, the same row-insertion expansion now uses
the added observable (18). Its direct reverse mean is
\(\delta_{a,i}\operatorname{tr}(C_bC_a^\top)/n\); its exterior
mean is the mixed endpoint trace from integrated (24). The independent
incoming/outgoing cross forms are centered. The actual learned-row
correction and direct feature pairing supply the other terms of (17).
The normalized scalar error is at most \(n^{-1/40}\) by (22)--(25).
A Gaussian grid with multiplier 64 handles all \(m^2\) training
pairs, with additional failure at most \(n^{-100}\). Thus (17)
strictly improves the response caps, in increasing layer order, to

\[
\|R_{ba}^{(j)}\|_\infty\le S U_j\sqrt\ell.
\tag{28}
\]

The exact time equation is
\(\dot z_b^{(j)}=-(2/m)\sum_a r_aR_{ba}^{(j)}\).
Following the real solution to its nearest anchor and then at most two
short pieces, (28) gives total preactivation displacement at most
\(8YSU_*p^{-1}\beta^{-100L}(1+\lambda)^{-1}\le a/8\).
The residual-growth, operator, activity and variational margins are those
proved at every width in `POLYNOMIAL_SOURCE_WIDTH.md`, and only improve
when divided by \(p\). Thus the full pole stop is strictly improved.
The order is local comparison, coordinate maximum, training response,
pole improvement, and finally budget removal. No complex Gram positivity
is used.

## 6. Common-cavity corrections at the finite moment order

For \(I\ni i\), the singleton and \(I\)-cavity both omit the
particular root paired with their lower feature or upper scaled response.
Their complete independently stopped difference path is independent of
that root. Project that complete path onto the deterministic Euclidean
ball of radius \(4n^{1/100}\). It agrees with the difference on
the successful full prefix by (25), and projection is nonexpansive.
Its normalized Gaussian radius is

\[
v_n=4n^{-49/100}.
\tag{29}
\]

Raw normalized derivative bounds give a rectangular coefficient modulus
at most \(\beta^{300L}(1+\lambda)\ell^3\). The rectangle has
side length at most \((64/\lambda+4)\ell\). The explicit Gaussian
rectangle lemma therefore gives, for the supremum \(E_i\) of a
projected error (also for its sample RMS),

\[
\log\mathbb E e^{uE_i}
 \le u\mu_n+2u^2v_n^2,
\qquad
\mu_n\le 256v_n\sqrt{\log(e+
 \beta^{400L}(1+\lambda^{-1})\ell^4/v_n)}+2v_n.
\tag{30}
\]

The constants absorb the sum of the two independent cavity moduli.
The two paths need not be independent of one another. In the real
restriction their sum of activity clocks also proves (30).
By (3), \(p\mu_n+p^2v_n^2<10^{-3}\).

On the common cavity, real Gaussian references have the integrated
source's conditional squared-exponential bound, including the sample
RMS version. At exponent at most \(8\eta\) this gives a main
one-neuron exponential moment below four. Distinct omitted root pairs
are independent conditional on that cavity. The complex corrections on
(4) obey `FINITE_COMPLEX_MOMENT_GATE.md` (2), now with its derivative
hypotheses verified by (28) and the joint budget: their \(p\)-th
root exponential moments are at most \(e^{\beta^{-10L}}\).

Apply Cauchy--Schwarz to split main references from correction products,
then Hölder with at most \(p\) factors to the latter. Equation (30)
pays for all projected corrections, and the finite complex moment bound
pays for all complex-minus-real corrections. The factors
\(\eta C_{\rm abs}\le(1024W_{\rm G})^{-1}\) leave their required
moment coefficient below eight. The deterministic scalar remainder in
(27) is paid directly. The resulting distinct-root bound is

\[
\mathbb E\left[1_E\prod_{i\in I}
 e^{\eta(Z_{a,i}+K_{a,i}/S)}\right]\le16^{|I|},
\qquad 1\le |I|\le p.
\tag{31}
\]

The event \(E\) contains initialization, all local Gaussian events,
and the two finite maximum events. It is removed only after the pathwise
bound by the nonnegative independent-cavity references. There is no
assumption of independence among training samples, projected corrections,
or full-network events.

## 7. Collisions, budget removal, and confidence dependence

On \(E\), the maximum (5) and the unchanged source constants imply

\[
B_i:=e^{\eta(Z_{a,i}+K_{a,i}/S)}
 \le e^{\sqrt\ell/100}\le e^{1/100}n^{1/100}.
\tag{32}
\]

The numerical inequality \(2\eta K_{\rm src}<1/100\) is proved
in `QUANTITATIVE_INSERTION_WIDTH.md` (4). The finite collision lemma
there, applied to (31)--(32), gives

\[
\mathbb E\left[1_E(n^{-1}\sum_iB_i)^p\right]\le e\,16^p
\quad\text{provided }n\ge4p^3.
\tag{33}
\]

If a sample budget reaches \(\mathcal B\), one layer average is at
least \(\mathcal B/L\). Markov and the union over \(mL\) sample
and layer pairs consequently give

\[
\Pr(\text{a budget is hit},E)
 \le emL(16L/\mathcal B)^p\le\delta/4.
\tag{34}
\]

Initialization costs less than \(\delta/4\), (14) costs less than
\(\delta/16\), and both maximum events together cost less than
\(\delta/16\), by (3). All stops therefore disappear with total
failure less than \(\delta\). Strict margins give holomorphy on
a neighborhood of the closed rectangle, completing the proposed source
claim (4)--(5). The dense real fitting and endpoint statement are already
part of \(E_0\); no new limit exchange is involved.

A confidence dependence polynomial only in \(\log(1/\delta)\)
cannot hold for the *unchanged coordinate event* (5), with a coefficient
\(K_{\rm src}\) independent of confidence. Already
\(z_{1,1}^{(1)}(0)\sim N(0,1)\), so success implies
\(|G|\le K_{\rm src}\sqrt{\log(en)}\). For fixed admissible data
and activation, Gaussian integration over
\([u,u+1/u]\), \(u\ge1\), gives

\[
\Pr(|G|>u)\ge
 \frac{2}{\sqrt{2\pi}u}e^{-(u+1/u)^2/2}.
\tag{35}
\]

For \(n\) bounded by any fixed polynomial in
\(\log(1/\delta)\), this lower bound at the stated \(u\) exceeds
\(\delta\) for sufficiently small confidence parameter. This only
rules out that stronger confidence target for the fixed event (5).
It does not rule out a redesigned source with an explicit
\(\sqrt{\log(1/\delta)}\) coordinate allowance, nor a polynomial
confidence width such as (3).

## 8. Scope, new dependency, and provenance

The earlier deterministic and finite-moment notes remain correct at their
stated conditional scope. The new closure step is the finite augmented
training-response estimate (18)--(23), together with its use in the
all-deletion bootstrap, pole stop and probability composition. Its exact
formula was recovered from the separately authorized
`studies/closure_sampling_20261003/ACTIVATION_CLASS_EXTENSION_ROUTE.md`
and `ACTIVATION_CLASS_EXTENSION_CHECK.md`, both read completely. Those
older files contain qualitative graph constants, not the numerical width
(3); this candidate does not infer (3) from their PASS verdicts.

The similarly named `ACTIVATION_EXTENSION_ROUTE.md` and
`ACTIVATION_EXTENSION_CHECK.md` in the dense-cutoff study were also read
after explicit permission. They concern initialization and parity and are
not used for the complex source calculation. No further older-study
references were followed.

Complete bodies used for the scalar local/probability argument were
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`,
`DEPTH_CAVITY_PROBABILITY_CHECK.md`, and `UNBOUNDED_INSERTION_CHECK.md`
in the authorized dense-cutoff study; the integrated source sections
1--8; and the current-study fitting, finite-order, fixed-jet, scaled-jet,
map-modulus and complex-moment notes. The full reference constant and
label definitions are those explicitly retained in Section 1. No other
new-route output was read. No experiment, Git mutation, promotion, or
write outside this assigned file was performed.

The candidate changes the source event's width quantifier; it does not
assert that a passive decoder has the original independent-dense-pair
error certificate. The factor \(p\) in (4) has the already documented
Taylor-patch cost. Any final resource theorem must charge it. The separate
fresh review reconstructed the augmented source port, direct reverse
observable, probe forward-image event, fixed cutoff degree, and the single
\(\sqrt n\) control-speed factor. This closes the finite training-source
probability interface at its stated scope, not the decoder or promotion.
