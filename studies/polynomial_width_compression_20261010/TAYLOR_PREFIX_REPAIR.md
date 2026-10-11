# Uniform endpoint tests over a random domain prefix

2026-10-10. Scoped proof repair of the endpoint paragraph in
`TAYLOR_ROUTE.md`, Section 5. This note changes neither that candidate nor
the paper. It proves a replacement for the endpoint/control discretization,
conditional on the raw local map estimates (35) already asserted there.
It does not independently certify those estimates or the rest of the
candidate's source theorem.

The repair is to discretize the domain level as well as the endpoint.
Every endpoint in the Gaussian union is retracted using only the cavity's
own stop. After that event is constructed, a level below the actual common
stop is selected. Consequently every actual control history used for the
selection lies inside the actual common domain. No analytic extension of a
clamped control field is needed.

## 1. Inputs and precise conclusion

Keep the candidate's notation

\[
\ell=\log(en),\qquad \kappa=1/4000,\qquad N=m+p,
\qquad
\mathcal C=\beta^{1000L}(1+\lambda^{-1})^2,
\]

\[
\mathcal A=\mathcal C^4(N+d+u+1)^8,
\qquad
n\ge \left\lceil(\mathcal A/\delta)^{40000}\right\rceil,
\quad 0<\delta<1/4.
\tag{1}
\]

Here \(u\ge1\) is the maximum deletion count, \(\beta\ge10\),
\(L\ge2\), and \(0<\lambda\le1\). In particular the candidate's
elementary width calculation gives

\[
\mathcal A\ell^{16}\le n^{1/1000},\qquad
u\le n^{1/8000},\qquad
\ell\le n^{1/16000}.
\tag{2}
\]

The domain \(D_s\) and retraction \(P_s\) are exactly (6) of the
candidate. Put

\[
H=128\ell/\lambda,
\qquad
\mathscr R=[-h(0),T_+]+i[-h(T_+),h(T_+)].
\tag{3}
\]

Each side of \(\mathscr R\) is at most \(H\), every canonical
real-then-vertical contour has length at most \(H/2\), and
\(\operatorname{Lip}(P_s)\le9/8\). The base-propagator, activity,
operator, and pole bounds proved in the candidate apply to canonical
contours inside each independently stopped cavity.

The local estimates used here are the following explicit interface. For
at most \(u\) deleted neurons, bounded deterministic scalar controls
on one such contour define each required Gaussian linear map \(L\)
and each symmetric quadratic matrix \(R\). At the original stopped
control amplitudes their bounds are

\[
\begin{aligned}
\max(\|L\|,\|R\|)&\le
 \mathcal C\sqrt u\,n^\kappa\ell^5,\\
\max(\|L_1-L_2\|,\|R_1-R_2\|)&\le
 \mathcal C\sqrt u\,n^\kappa\ell^4
 \|c_1-c_2\|_\infty.
\end{aligned}
\tag{4}
\]

For actual analytic controls and cavity fields, their complex derivatives
on a common pre-stop domain satisfy

\[
\max(\|L'\|,\|R'\|)
\le\mathcal C\sqrt u\,n^{\kappa+1/2}\ell^8.
\tag{5}
\]

There are at most \(4u(N+1)^2\) real control components. Their
amplitudes and arclength Lipschitz constants are bounded respectively by

\[
M=\mathcal C\ell,\qquad D=\mathcal C\sqrt n\ell^3.
\tag{6}
\]

These are deliberately loose versions of the candidate's (35) and the
following derivative/control paragraph. The distinction between (4) and
(5) is essential: (4) is a one-dimensional forced-ODE estimate; (5)
is used only for the actual analytic controls inside their common
domain. No terminal derivative bound for an arbitrary two-dimensional
control extension is an input or a conclusion.

The conclusion is a Gaussian event, formed without conditioning on
full-network survival, on which all the source's linear coordinate,
Euclidean-image, probe, and centered quadratic bounds hold at every
point of every admissible common prefix, including an adaptively chosen
prefix. Its failure probability remains at most
\(e^{-n^{0.7}}<\delta/16\), as in (37) of the candidate.

## 2. Cavity-dependent endpoints with a deterministic level mesh

Fix a deletion set and condition only on retained initialization. Let
\(\sigma_c\in[0,1]\) be that cavity's own stopping level. It is
measurable in the conditioned information. The omitted incoming rows and
outgoing columns remain independent centered Gaussian roots. After
discarding nonexistent boundary blocks, pad their concatenation if
necessary to write

\[
g\sim N(0,I_r/n),\qquad r\le2un.
\tag{7}
\]

First-layer incoming rows need not be included in (7): there is no
retained reverse port below that layer, and their actual values may enter
the scalar controls covered uniformly below. Failed cavity initialization
tests give identically zero reference maps, as prescribed in the source.
The remaining argument concerns cavities passing their own tests.

For each cavity coefficient \(b_c\), the optional complete extension
is explicitly

\[
b_c^{\mathrm{ext}}(z)=b_c(P_{\sigma_c}z),\qquad z\in\mathscr R.
\tag{8}
\]

This is a retained-measurable continuous extension. It is not claimed to
be holomorphic. In particular, we never solve a complex ODE by treating
\(b_c^{\mathrm{ext}}\) as a holomorphic coefficient outside
\(D_{\sigma_c}\).

We need a bound in the domain level. For \(s,t\in[0,1]\),
clipping the real coordinate to moving intervals gives

\[
|X_s(x)-X_t(x)|\le T_+|s-t|\le H|s-t|.
\]

The imaginary clipping radius is \(s h(X_s(x)_+)\). Since
\(h'\le1/8\), its change is at most
\((h(T_+)+H/8)|s-t|\le(9H/8)|s-t|\).
Clipping a fixed real number to \([-a,a]\) is 1-Lipschitz in
\(a\ge0\). Bounding Euclidean norm by the sum of coordinate
increments therefore proves

\[
\sup_{z\in\mathscr R}|P_sz-P_tz|\le3H|s-t|.
\tag{9}
\]

Choose

\[
\xi=\frac{n^{-2}}{1+\mathcal A\ell^8},\qquad
J_s=\left\lceil16H/\xi\right\rceil,
\qquad s_j=j/J_s\quad(0\le j\le J_s).
\tag{10}
\]

Let \(\mathscr G\) be the rectangular product grid including both
endpoints of both coordinate intervals of \(\mathscr R\). Partition
each side of length \(a\) into \(\lceil8a/\xi\rceil\) equal
intervals, giving spacings no greater than \(\xi/8\) without arbitrary
oversampling. For every pair
\((s_j,q)\in\{s_0,\ldots,s_{J_s}\}\times\mathscr G\),
define the test endpoint

\[
z_{j,q,c}=P_{\min(s_j,\sigma_c)}q.
\tag{11}
\]

All these endpoints are fixed after conditioning on the cavity and lie
inside its own stopped domain. The finite endpoint family is therefore
independent of the omitted roots. Its dependence on \(\sigma_c\)
is harmless; dependence on the full-network stopping level would not be.

For an endpoint \(z_{j,q,c}=x+iy\), use the following explicit
arclength parametrization on the common deterministic interval \([0,H]\):

\[
\zeta(t)=\operatorname{sgn}(x)\min(t,|x|)
 +i\operatorname{sgn}(y)
       \min((t-|x|)_+,|y|),
\tag{12}
\]

where \(\operatorname{sgn}(0)=0\). Its moving part has length
\(|x|+|y|\le H/2\); afterward it is constant. Its derivative is
one of \(1,-1,i,-i,0\) almost everywhere. Its real part stays
between zero and \(x\), and its final vertical segment has the
fixed real coordinate \(x\). Thus the complete moving contour lies
in \(D_{\min(s_j,\sigma_c)}\). At a negative real coordinate
this remains true because the vertical radius is the constant
\(\min(s_j,\sigma_c)h(0)\).

No norm estimate on an extrapolated cavity coefficient is used: every
nonconstant piece of (12) lies in the domain where the independently
stopped source estimates hold. Freezing after the endpoint adds zero
activity, zero contour length, and the identity propagator. The two
corners of the parametrization do not affect the integral equation.

## 3. The maps tested on a contour

For clarity, the Gaussian maps can be defined without referring to any
control extension in the plane. Fix a contour (12). Write
\(\bar u_c\) for the normalized cavity displacement and
\(\bar r_a=\bar F_a/n-y_a/S\), where
\(\bar F_a=F_a/S\). In an interior deletion at layer \(j\),
let \(x_i\) and \(y_i\) select from \(g\) the omitted outgoing
column and incoming row. For deterministic complex scalar histories
\(\alpha_{a,i}(t),b_{a,i}(t)\), set

\[
e_a(t)=\sum_i x_i\alpha_{a,i}(t),\qquad
\bar q_a(t)=\sum_i y_i b_{a,i}(t).
\tag{13}
\]

The normalized retained vector field at ports \((e,\bar q)\) is

\[
\mathcal F(\bar u;e,\bar q)
=-\frac2m\sum_{a=1}^m\bar r_a
\left[\nabla_{\bar u}\bar F_a
 +D_{\bar u}h_a^{(j-1)\top}\bar q_a\right].
\tag{14}
\]

The full omitted top offset is a separate nonlinear source in the
candidate; it is not added to the frozen Gaussian forcing here. At the
zero-port cavity, define

\[
\mathsf A=D_{\bar u}\mathcal F,
\]

\[
\begin{aligned}
\mathsf B_a^e
&=-\frac2{mn}\nabla_{\bar u}\bar F_a\,
                       \bar\delta_a^{(j+1)\top}
  -\frac2m\bar r_a(D_{\bar u}\bar\delta_a^{(j+1)})^\top,\\
\mathsf B_a^q
&=-\frac2m\bar r_a(D_{\bar u}h_a^{(j-1)})^\top.
\end{aligned}
\tag{15}
\]

All coefficients in (15) are evaluated at \(\zeta(t)\). Define
the Gaussian linear parameter variation by the absolutely continuous
solution

\[
\frac{dV}{dt}
=\zeta'(t)\left[\mathsf A(\zeta(t))V(t)
 +\sum_a\{\mathsf B_a^e(\zeta(t))e_a(t)
          +\mathsf B_a^q(\zeta(t))\bar q_a(t)\}\right],
\qquad V(0)=0.
\tag{16}
\]

Equivalently, if \(J_\zeta(t,r)\) is the homogeneous propagator,

\[
V(t)=\int_0^tJ_\zeta(t,r)\zeta'(r)
 \sum_a\{\mathsf B_a^e(\zeta(r))e_a(r)
         +\mathsf B_a^q(\zeta(r))\bar q_a(r)\}\,dr.
\tag{17}
\]

This is a linear map of \(g\), for every deterministic history.
The source's explicit propagator and forcing bounds prove (4) on
exactly these integrals. They require only bounded measurable histories,
not holomorphic histories. For example, their unabsorbed parameter-map
bound is

\[
\sqrt u\,J_0n^\kappa
\{A_n(2(H/2)\Gamma\tau_*+M_\delta)+Sf_*B_n^{\rm ctrl}\},
\tag{18}
\]

with the source's amplitude bounds \(A_n,B_n^{\rm ctrl}\),
\(\Gamma=\sqrt{\mathcal K}\), and the source's explicit
\(J_0,\tau_*,M_\delta,f_*\). The superscript on
\(B_n^{\rm ctrl}\) distinguishes a control-amplitude bound from
the candidate's unrelated logarithmic factor \(B_n\).
Formula (18) follows directly from (17), the activity bound
\(2\int\rho/S\le1\), and Cauchy--Schwarz over the omitted
root blocks; it introduces no full-network conditioning.

All required endpoint maps are obtained from (16) by the source's
explicit linear forward/backward recursions. For example,

\[
\begin{aligned}
z_{[1]}^{(k)}&=S V_{\sqrt nW^{(k)}}h_c^{(k-1)}/\sqrt n
 +W_c^{(k)}h_{[1]}^{(k-1)}+e_{[1]}^{(k)},\\
h_{[1]}^{(k)}&=\phi_k'(z_c^{(k)})\odot z_{[1]}^{(k)},\\
\bar k_{[1]}^{(k)}&=W_c^{(k+1)\top}\bar\delta_{[1]}^{(k+1)}
 +S V_{\sqrt nW^{(k+1)}}^\top\bar\delta_c^{(k+1)}/\sqrt n
 +\bar q_{[1]}^{(k)},\\
\bar\delta_{[1]}^{(k)}&=\phi_k'(z_c^{(k)})\odot\bar k_{[1]}^{(k)}
 +\phi_k''(z_c^{(k)})\odot\bar k_c^{(k)}\odot z_{[1]}^{(k)}.
\end{aligned}
\tag{19}
\]

The first-layer matrix term is \(SV_{W^{(1)}}v_b\), and the
top carrier variation is \(V_w\). The ports are zero except at
their prescribed deletion locations. Forward maps use all declared
inputs; backward maps use training drivers.

The additional response maps are defined by differentiating (30) of
the candidate, including its separate omitted response port
\(\sum_i x_i\chi_{ba,i}\). Explicitly the differentiated
hidden-layer terms are

\[
\bar\delta_{a,[1]}c_{ab,c}
 +\bar\delta_{a,c}c_{ab,[1]}
 +(SV_{\sqrt nW^{(k)}}/\sqrt n)\bar Q_{ba,c}^{(k-1)}
 +W_c^{(k)}\bar Q_{ba,[1]}^{(k-1)},
\]

\[
c_{ab,[1]}=
\frac{h_{a,[1]}^\top h_{b,c}+h_{a,c}^\top h_{b,[1]}}n,
\qquad
\bar Q_{ba,[1]}=
\phi'\odot\bar R_{ba,[1]}
 +\phi''\odot\bar R_{ba,c}\odot z_{b,[1]}.
\tag{20}
\]

The direct lower reverse observables and their probe family are retained:
with \(C_a=D_\Theta h_a^{(j-1)}\), they are the source's
linear maps \(C_bC_a^\top\bar q_a\),
\(C_a^\top y_i\), and the reference forward images of
\(C_a^\top y_i\) at every declared input. These are evaluated
at the same endpoint and depend on the root through the displayed
linear argument only. This repair uses their norm and derivative
estimates from the candidate's (35); it does not omit them from the
Gaussian event. Boundary cases delete nonexistent ports and blocks.

If \(E_i\) selects one root block and \(Lg\) is a linear
field to be paired with it, define

\[
R=\tfrac12(E_i^\top L+L^\top E_i),\qquad
\mathcal Q_R(g)=g^\top Rg-\operatorname{tr}(R)/n.
\tag{21}
\]

The transpose is algebraic. Real and imaginary parts are tested
separately. Thus every Gaussian test is now an explicitly defined
linear map or centered quadratic form on a contour inside the cavity's
own domain.

## 4. One-dimensional control nets and Gaussian probabilities

Use \(\tau=n^{-1/8}\). Divide \([0,H]\) into
\(K_c=\lceil16DH/\tau\rceil\) equal intervals and round each
real component at every node to the nearest multiple of \(\tau/8\).
Linearly interpolate the rounded values. Use every resulting sequence
whose nodal values lie in \([-M-\tau/16,M+\tau/16]\).
This is a deterministic finite family, independent even of the cavity.

For a real \(D\)-Lipschitz history of amplitude at most \(M\),
the error of interpolation of its unrounded samples is at most
\(D H/(2K_c)\le\tau/32\). Rounding contributes at most
\(\tau/16\). Each real-component error is therefore below
\(\tau/8\), and each complex-component error is below \(\tau\).
The net histories have complex amplitude at most twice the common
amplitude envelope \(M\). Their derivatives are irrelevant to the fixed-contour
Gaussian test: (16)--(19) require their values and (4) requires their
supremum distance only.

For an actual analytic control on the moving part of (12), compose it
with \(\zeta\), and hold its terminal value fixed afterward.
It is \(D\)-Lipschitz on \([0,H]\). Indeed its derivative on
each moving piece has magnitude at most \(D\), and the sum of
the two arclength distances bounds the difference across the corner.
The frozen part has derivative zero. This is exclusively a
one-dimensional extension of an already valid contour restriction.

The logarithm of the net size is bounded by

\[
4u(N+1)^2(2+16DH/\tau)
       \log(1+32M/\tau)
\le\mathcal A\ell^8n^{5/8}\le n^{0.627}.
\tag{22}
\]

Here \(DH=128\mathcal C\lambda^{-1}\sqrt n\ell^4\),
\(\log(1+32M/\tau)\le\ell\) at (1), and the numerical
coefficient is covered, for example, by

\[
16384\,u(N+1)^2\mathcal C\lambda^{-1}\le\mathcal A.
\]

For this last inequality use
\(u(N+1)^2\le(N+d+u+1)^3\) and
\(\mathcal C^3/\lambda^{-1}\ge
\beta^{3000L}(1+\lambda^{-1})^5>16384\).

The loose common envelope \(M\) need not coincide with the original
per-type stopped amplitudes. To cover the entire net, use the affine
dependence of each map on the scalar controls. Equation (16) has a
control-independent homogeneous propagator and forcing linear in the
controls; the algebraic endpoint recursions (19)--(21) preserve that
dependence. Control-independent probe maps give the possible constant
term. Thus the control-difference estimate in (4) is the bound for a
linear operator on control histories, independent of their amplitudes.
Its extension to larger amplitudes follows by scaling a difference into
the original allowed control ball. At zero controls the first line of
(4) applies. Every net history has norm at most \(2\mathcal C\ell\),
so the common operator bound on the full loose-envelope net is

\[
\mathcal C\sqrt u\,n^\kappa\ell^5
+2\mathcal C^2\sqrt u\,n^\kappa\ell^5
\le4\mathcal C^2\sqrt u\,n^\kappa\ell^5
\le\mathcal A\ell^{16}n^\kappa
\le n^{1/800}<n^{1/200}.
\tag{23}
\]

Here \(4\mathcal C^2\sqrt u\le\mathcal A\) follows from its
definition in (1). This explicitly pays for the enlarged control envelope;
it is not an assertion that all net controls obey the original per-type
amplitudes. The same linear difference bound continues to give (28).

Fix any net test conditional on its cavity. At threshold
\(t=n^{-1/10}/8\), a complex linear coordinate has tail at most

\[
4\exp(-n^{0.79}/256)\le4e^{-n^{0.78}}.
\tag{24}
\]

For completeness, if \(A\) is a real symmetric matrix and
\(g\) has law (7), diagonalization of the Gaussian square moment
generating function gives

\[
\Pr\{|g^\top Ag-\operatorname{tr}(A)/n|>a\}
\le2\exp\left[-\frac18\min\left\{
\frac{n^2a^2}{\|A\|_{\rm HS}^2},
\frac{na}{\|A\|}\right\}\right].
\tag{25}
\]

One derivation uses
\(-\log(1-v)-v\le v^2/[2(1-|v|)]\) for \(|v|<1\)
in the product moment generating function, restricts the exponential
parameter to \(n/(4\|A\|)\), and applies exponential Markov
to both signs. The constant \(1/8\) is weaker than the resulting
optimized bound. For the real and imaginary parts of (21),
\(\|R\|_{\rm HS}^2\le2un\,n^{1/100}\).
Set \(a=t/\sqrt2\) in (25). The complex tail is at most

\[
4\exp\left[-\min\left\{
\frac{n^{0.79}}{2048u},
\frac{n^{0.895}}{64\sqrt2}\right\}\right]
\le4e^{-n^{0.78}}.
\tag{26}
\]

The final inequalities in (24) and (26) follow from (1)--(2),
which imply \(n^{0.01}\ge256\) and
\(n^{0.009875}\ge2048\). This checks the original scalar
threshold, rather than enlarging it to pay for the new mesh.

The Euclidean image has expectation at most
\(\sqrt{2u}\,n^{1/200}<n^{1/100}/4\). Its norm is
\(n^{-1/2+1/200}\)-Lipschitz as a function of a standard real
Gaussian vector. Gaussian norm concentration at threshold
\(n^{1/100}/2\) therefore gives a tail at most
\(e^{-n^{1.01}/32}\), smaller than (26).
The extra factor \(1/2\) reserves the interpolation margins.

On the root-norm event \(\|g\|\le2\sqrt{2u}\), (21) gives

\[
|\mathcal Q_{R_1}(g)-\mathcal Q_{R_2}(g)|
\le(\|g\|^2+r/n)\|R_1-R_2\|
\le10u\|R_1-R_2\|.
\tag{27}
\]

This includes the trace difference. A linear image costs only
\(2\sqrt{2u}\|L_1-L_2\|\le10u\|L_1-L_2\|\).
The root-norm failure is at most \(e^{-un}\), by padding to
\(2un\) coordinates and using the Gaussian square moment formula.
Equations (2), (4), and (27) bound control interpolation by

\[
10\mathcal C u^{3/2}n^{\kappa-1/8}\ell^4
\le10n^{-0.12375}<n^{-1/10}/8.
\tag{28}
\]

## 5. Selecting an arbitrary common prefix after the event

Suppose now that the full path and this cavity have a common pre-stop
domain \(D_\sigma\), with \(0\le\sigma\le\sigma_c\).
The level \(\sigma\) may depend arbitrarily on the omitted roots.
Fix \(z\in D_\sigma\), choose \(q\in\mathscr G\) with
\(|q-z|\le\sqrt2\xi/8\), and choose the largest mesh level
\(s_j\le\sigma\). Then

\[
0\le\sigma-s_j\le\xi/(16H),\qquad
z_{j,q,c}=P_{s_j}q\in D_{s_j}\subseteq D_\sigma.
\tag{29}
\]

The canonical contour to this endpoint is inside \(D_\sigma\).
Therefore the actual controls are defined on its entire moving part and
are approximated by the deterministic one-dimensional net of Section 4.
This is the first point where actual adaptive controls are substituted.

For endpoint interpolation, fix these actual control *functions* on
\(D_\sigma\), including their dependence on the roots. On its
interior, the cavity coefficients and these functions are holomorphic.
The linear equation corresponding to (16) has holomorphic coefficients
and forcing. It has a unique holomorphic solution with value zero at the
origin. The applicable elementary ODE fact is that a linear equation
\(V'=AV+f\) with holomorphic \(A,f\) on a simply connected
planar domain has a single-valued holomorphic solution for any initial
value. Local power-series existence and uniqueness give solutions near
each point; a Gronwall bound on any compact path permits continuation;
uniqueness and simple connectivity give path independence.

The hypotheses hold here: \(D_\sigma\) is vertically fibered
over an interval with positive continuous half-height when \(\sigma>0\),
so its interior contracts vertically to that interval and is simply
connected. Canonical contours remain inside it up to boundary limits.
The solution restricted to a canonical contour is precisely (16) by
uniqueness. Applying the algebraic recursions (19)--(21) gives the
holomorphic maps \(L(z)\) and \(R(z)\) for these fixed actual
functions. Their derivatives satisfy (5). This assertion is never made
for a net history or the clamped field (8).

By (9) and the spatial Lipschitz bound,

\[
\begin{aligned}
|z-P_{s_j}q|
&\le |P_\sigma z-P_{s_j}z|
     +|P_{s_j}z-P_{s_j}q|\\
&\le3H(\sigma-s_j)+(9/8)|z-q|\\
&\le(3/16+9\sqrt2/64)\xi.
\end{aligned}
\tag{30}
\]

Join \(z\) to \(P_{s_j}q\) by applying \(P_\sigma\)
to their straight joining segment. This curve stays inside
\(D_\sigma\), fixes both endpoints, and has length at most

\[
\frac98(3/16+9\sqrt2/64)\xi<\xi/2.
\tag{31}
\]

No convexity of \(D_\sigma\) is used. Integration of (5)
along this rectifiable curve and (27) show that either a linear image
or a centered quadratic value changes by at most

\[
10u\mathcal C\sqrt u\,n^{\kappa+1/2}\ell^8\xi
\le10n^{-3/2+\kappa}<n^{-1/10}/8.
\tag{32}
\]

Here \(\mathcal C u^{3/2}\le\mathcal A\), so the denominator
in (10) pays the complete parameter and logarithmic coefficient.
At a stopping boundary, first apply the argument at strictly smaller
levels and take continuous limits. If \(\sigma=0\), the only
point is zero, already one of the level-zero endpoints, so no limiting
or interpolation argument is needed.

Combining the net threshold, (28), and (32) gives at most
\(3n^{-1/10}/8<n^{-1/10}\) for each scalar or centered
quadratic test. The Euclidean-image threshold in Section 4 and the same
absolute interpolation estimates give the bound \(n^{1/100}\).
These are simultaneous pathwise conclusions for every admissible
\(\sigma\). Selecting a random \(\sigma\) therefore adds
neither conditioning nor a probability loss. After selection, the actual
variations need not have a Gaussian law; only the already proved uniform
bounds are used. Likewise \(\operatorname{tr}(R)/n\) remains
an evaluated frozen-map trace, not an asserted conditional mean of an
adaptively selected quadratic form.

## 6. Cost of the extra level mesh

The spatial grid and the level grid have cardinalities at most

\[
|\mathscr G|\le(2+8H/\xi)^2,
\qquad J_s+1\le2+16H/\xi.
\tag{33}
\]

Using \(\lambda^{-1}\le\mathcal A^{1/8}\) and (2),

\[
H/\xi
\le256\mathcal A^{9/8}\ell^9n^2
\le256n^{2.001125}.
\]

At (1), \(2+16H/\xi\le n^3\). Consequently
\(|\mathscr G|\le n^6\), and the full endpoint family has
at most \(n^9\) members. Repeated endpoints for levels above
\(\sigma_c\) cause no problem.

The candidate has at most \(\mathcal A n^3\) tests per endpoint
and at most \(uLn^u\) deletion choices. By (22), the logarithmic
union cost, including a numerical factor four, is at most

\[
n^{0.627}+\log(4\mathcal A)+12\log n
 +\log(uL)+u\log n<n^{0.65}.
\tag{34}
\]

For example (2) bounds \(u\ell\) by \(n^{0.0001875}\),
and all remaining logarithmic terms by \(20\ell\); the slack
from exponent \(0.627\) to \(0.65\) is ample at (1).
Thus (24)--(26), followed by the union over deletion sets, give

\[
4\exp(n^{0.65}-n^{0.78})
 +uLn^u e^{-un}
\le e^{-n^{0.7}}<\delta/16.
\tag{35}
\]

All estimates are first proved conditionally on each cavity, with
uniform deterministic upper bounds, and then integrated over its retained
initialization. Cavities need not be independent for the final union.
The additional level mesh changes only the polynomial number of endpoint
tests. It changes neither the width (1), the radius, the Taylor panel
count, nor the retained-state count.

## 7. Replacement and claim boundary

The endpoint paragraph after (36) of `TAYLOR_ROUTE.md` can be replaced
by the construction (10)--(12), the one-dimensional Gaussian/control
event of Section 4, and the lower-level selection (29)--(32). The
endpoint count becomes \(n^9\) in place of \(n^6\), and (34)
shows that the claimed failure exponent (37) is unchanged.

Merely retracting a fixed grid by the full common stopping level would
not establish this conclusion: that level can depend on the omitted
roots, so the resulting test coefficients are not frozen Gaussian
coefficients. Nor does the cavity's own retraction provide actual
controls beyond the full common prefix. The lower deterministic level in
(29) is what resolves both issues.

This closes that specific prefix/endpoint gap given (4)--(6). The raw
augmented-map ledger, nonlinear insertion remainders, initialization,
moment composition, and dense-run variability claim remain separate
proof obligations of the candidate; no conclusion about their independent
review status is drawn here.

Inputs inspected: the complete `TAYLOR_ROUTE.md`; the complete
`INSERTION_MAP_MODULI.md`; the directly relevant normalized forcing and
map formulas in `QUANTITATIVE_INSERTION_WIDTH.md`; the local map,
response, and first-exit sections of `FULL_FINITE_SOURCE_PROBABILITY.md`;
and the independently stopped cavity, local insertion, uniform Gaussian,
and flaring-domain passages of `paper/compact_foundations.tex`. Required
rigorous-math and canonical/neural notation instructions were read. No
review report, study history, unauthorized study, frozen archive, Git operation,
or shared-file edit was used.
