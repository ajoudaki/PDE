# A real-value activation backend for local continuation setup

2026-10-06. Post-freeze refinement explicitly requested by the supervisor after
the core continuation candidate was frozen. The supervisor proposed the
Chebyshev activation replacement; this note supplies its construction and
error analysis. It is an author-derived candidate, not an independent review.
The reviewed pre-cleanup SHA-256 was
25e8c6dd6381d46b561a839339d538ea38926f4130af62dfb848f91cc6f54cbb.
The subsequent presentation-only cleanup expands the logarithm alias everywhere
and removes its definition; no formula, exponent, bound, or hypothesis changes.

The mathematical activation class is unchanged. The disposable dense setup
solver uses polynomial approximants to the original activations, constructed
from real activation values. Its defect is measured against the original
nonlinear dense vector field. Exact initial source additions and the retained
Harmonic runtime use the original activations.

The result removes the high-order activation-derivative oracle from
LOCAL_CONTINUATION_SETUP.md. It gives near-quadratic arithmetic plus explicit
real scalar activation-value calls, in the original exact-real cost model.
As for any algorithm taking an arbitrary analytic function as input, a cost
for obtaining its scalar values must be specified separately; analyticity
alone cannot make an unspecified or noncomputable function evaluable.

The input and notation are those of the corrected core note, whose frozen
SHA-256 is
 c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe.
The source event, full original label interval, and original width gates are
retained. All bounds below are deterministic on that event. The notation and
process-skill qualification stated in the core note also apply here.

## 1. Domain to be approximated

Use \(P_*,G,L_n,b_n,V,M_c,Z_n\) from equations
(6)--(14) of the core note, with the corrected
\(b_n\le a/(16\sqrt nP_*)\). Thus the exact network throughout every moving
parameter ball has preactivation imaginary parts at most \(7a/16\).

We need a bound on preactivation real parts for every real query, including
when the parameters are on a complex time disk. Let
\(H_{\max}^{\rm src}=\max_jH_j^{\rm src}\),
\(G_d=16\sqrt{d+3}\), and let \(U\) be the explicit source coefficient in
(S.25) of RESULT.md. One sufficient bound at the exact disk centers is

\[
Z_*=(K_{\rm src}+G_dH_{\max}^{\rm src}+1+US^2)\sqrt{\log(en)}
       +a/8+\sqrt nP_*Z_n.
\tag{A1}
\]

Indeed the initial whole-sphere coordinate bound is
\((G_dH_{\max}^{\rm src}+1)\sqrt{\log(en)}\). The real velocity bound
\(|\partial_tz_i^{(j)}|\le2\rho SU\sqrt{\log(en)}\), integrated using the
source activity bound \(\int2\rho\,dt\le S/2\), adds at most
\(US^2\sqrt{\log(en)}\). The short complex time pieces add at most
\(8YSUr_t\sqrt{\log(en)}=a/8\). After \(T_0\), compare with
\(\theta(T_0)\) in the late safe ball; the forward endpoint estimate adds
at most \(\sqrt nP_*Z_n\). The extra \(K_{\rm src}\sqrt{\log(en)}\) in (A1)
also covers the early training-coordinate maximum. Only real query
vectors are needed here; no polynomial is evaluated on a complex query sphere.

Every original preactivation at a state in one of the moving balls therefore
satisfies

\[
|\operatorname{Re}z|\le Z_*+a/16,\qquad
|\operatorname{Im}z|\le7a/16.
\tag{A2}
\]

At fixed structural parameters, \(Z_*=O(\sqrt{\log(en)})\). Define

\[
B=8(Z_*+a+1),\qquad
\tau_o=\operatorname{arsinh}\frac{31a}{64B},\qquad
\tau_i=\operatorname{arsinh}\frac{29a}{64B},\qquad
\Delta=\tau_o-\tau_i.
\tag{A3}
\]

For \(\tau>0\), write \(\mathcal E_\tau\) for the filled ellipse with boundary
\(z=B(w+w^{-1})/2,\ |w|=e^\tau\). Its semiaxes are \(B\cosh\tau\)
and \(B\sinh\tau\). The outer ellipse is strictly inside the activation
half-strip because its imaginary semiaxis is \(31a/64<a/2\).
Moreover \(B\ge8a\), so

\[
0<\Delta<1,\qquad \Delta\ge\frac{a}{64B},\qquad \tau_o<1.
\tag{A4}
\]

For the lower bound, integrate the derivative of \(\operatorname{arsinh}x\)
between \(29a/(64B)\) and \(31a/(64B)\); it is at least \(1/2\)
on that interval.

The inner ellipse contains every disk of radius \(a/512\) around every point
at distance at most \(a/512\) from a point of (A2). Its real coordinate
divided by its real semiaxis is at most \(1/8\), while its imaginary
coordinate divided by the imaginary semiaxis is at most
\((7/16+2/512)/(29/64)=226/232\). Their squared sum is less than one.
This verifies the domain for activation substitution and derivative
estimation below, with strict margin.

## 2. Explicit real-node Chebyshev construction

Let \(b=\max_j|\phi_j(0)|\) and let \(s\) be the original first-derivative
bound on the half-strip. On \(\mathcal E_{\tau_o}\),

\[
|\phi_j(z)|\le M_\phi,\qquad M_\phi=b+s(B+a).
\tag{A5}
\]

Integrate the bounded derivative on the segment from zero to \(z\), which
lies in the half-strip, and use \(|z|\le B\cosh\tau_o\le B+a\).

Fix a desired value/first/second derivative accuracy \(\epsilon>0\), and put

\[
C_a=\max\{1,512/a,2(512/a)^2\},\qquad
\epsilon_p=\epsilon/C_a,
\]
\[
D=\max\left\{1,\left\lceil
 \Delta^{-1}\log\max\{e,24M_\phi/(\epsilon_p\Delta)\}
 \right\rceil\right\},\qquad N_\phi=4(D+1).
\tag{A6}
\]

At the real nodes \(x_r=B\cos(2\pi r/N_\phi)\), evaluate the original
activation. Define

\[
\widetilde c_0=\frac1{N_\phi}\sum_{r=0}^{N_\phi-1}\phi_j(x_r),
\qquad
\widetilde c_k=\frac2{N_\phi}\sum_{r=0}^{N_\phi-1}
       \phi_j(x_r)\cos(2\pi kr/N_\phi),\quad 1\le k\le D,
\]
\[
\psi_j(z)=\sum_{k=0}^D\widetilde c_k T_k(z/B),
\tag{A7}
\]

where \(T_k(\cos u)=\cos(ku)\). Thus \(\psi_j\) has real coefficients
and is computed from \(N_\phi\) real calls to \(\phi_j\).

Here is the error estimate, including the finite coefficient rule.
For \(g(u)=\phi_j(B\cos u)\), shifting a Fourier contour within
\(|\operatorname{Im}u|\le\tau_o\) gives
\(|\widehat g_k|\le M_\phi e^{-|k|\tau_o}\). The function is even.
Its Chebyshev coefficients are \(c_0=\widehat g_0\) and
\(c_k=2\widehat g_k\) for \(k\ge1\). Also
\(|T_k(z/B)|\le e^{k\tau_i}\) on \(\mathcal E_{\tau_i}\), by its
Laurent formula on the ellipse boundary and the maximum modulus principle.
Consequently the degree-\(D\) exact coefficient tail is at most

\[
\frac{2M_\phi e^{-(D+1)\Delta}}{1-e^{-\Delta}}
\le \frac{4M_\phi}{\Delta}e^{-(D+1)\Delta}.
\tag{A8}
\]

Absolute Fourier convergence permits interchange with the finite sum. The
discrete Fourier coefficient is
\(\sum_{q\in\mathbb Z}\widehat g_{k+qN_\phi}\), since the discrete sum of
\(e^{i\ell u}\) vanishes unless \(N_\phi\) divides \(\ell\). For
\(0\le k\le D<N_\phi/2\), this gives

\[
|\widetilde c_k-c_k|
\le\frac{4M_\phi e^{-(N_\phi-D)\tau_o}}
           {1-e^{-N_\phi\tau_o}}.
\]

The factor four safely includes the constant coefficient. Since
\((D+1)\Delta\ge1\), the denominator is at least \(1/2\). Summing the
coefficient error on the inner ellipse and using \(N_\phi=4(D+1)\) yields

\[
\left|\sum_{k=0}^D(\widetilde c_k-c_k)T_k(z/B)\right|
\le8M_\phi(D+1)e^{-2(D+1)\tau_o}
\le\frac{8M_\phi}{\Delta}e^{-(D+1)\Delta}.
\tag{A9}
\]

For the last inequality use \(x e^{-x}\le1\) with
\(x=(D+1)\tau_o\), and \(\tau_o\ge\Delta\).
Equations (A6), (A8)--(A9) show that
\(\sup_{\mathcal E_{\tau_i}}|\psi_j-\phi_j|\le\epsilon_p/2\).

The reserved half also permits inexact real value calls: if each value in
(A7) has absolute error at most

\[
\epsilon_{\rm eval}=
\frac{\epsilon_p}{4(D+1)e^{D\tau_i}},
\tag{A10}
\]

the resulting extra polynomial error on the inner ellipse is at most
\(\epsilon_p/2\). Bound every coefficient perturbation
by \(2\epsilon_{\rm eval}\) and sum \(D+1\) terms.

Cauchy's integral formula on the disks checked after (A4) gives, at every
point at distance at most \(a/512\) from the rectangle (A2),

\[
|\psi_j-\phi_j|\le\epsilon,\qquad
|\psi_j'-\phi_j'|\le\epsilon,\qquad
|\psi_j''-\phi_j''|\le\epsilon.
\tag{A11}
\]

The derivative factors are \(512/a\) and \(2(512/a)^2\), precisely those
included in \(C_a\). Exact calls make (A10) unnecessary; finite-accuracy calls
only require polynomially small error in the regime analyzed below.

## 3. Error in the training vector field

Replace every activation by \(\psi_j\) only in a disposable setup network,
and call its gradient-flow vector field \(\widetilde F\). We compare this
polynomial field to \(F\) at the same parameter value \(u\) in a moving
ball of the core note. Use the core coefficients \(H_j,B_j\), and define

\[
U_0=0,\qquad U_j=1+11sU_{j-1},\qquad U_*=\max_jU_j,
\qquad K_j=R(11s)^{L-j}.
\tag{A12}
\]

Superscripts \(0\) and \(p\) below distinguish the original and polynomial
activation evaluations at this one parameter state. If

\[
\epsilon\le\min\left\{1,U_*^{-1},
       \frac{a}{5632\sqrt nU_*}\right\},
\tag{A13}
\]

then induction over the layers gives

\[
\frac{\|h^{p,(j)}-h^{0,(j)}\|_2}{\sqrt n}\le U_j\epsilon,
\qquad
\frac{\|z^{p,(j)}-z^{0,(j)}\|_2}{\sqrt n}
 \le11U_{j-1}\epsilon.
\tag{A14}
\]

The first preactivations agree. At the next layer the unchanged matrix costs
eleven, and the activation difference splits into its error at the polynomial
argument plus the original activation's \(s\)-Lipschitz change. Every
preactivation coordinate discrepancy is at most
\(11\sqrt nU_*\epsilon\le a/512\), so (A11) applies at every induction
step. Also \(\|h^{p,(j)}\|_2/\sqrt n\le H_j+1\).

For \(M\ge0\), define backward error coefficients by descending recursion:

\[
Q_{L+1}(M)=0,\qquad
Q_j(M)=11(s+1)Q_{j+1}(M)+K_j+11t_2M U_{j-1}.
\tag{A15}
\]

If the original carriers at \(u\) have maximum \(M\), then

\[
\frac{\|\delta^{p,(j)}-\delta^{0,(j)}\|_2}{\sqrt n}
\le Q_j(M)\epsilon.
\tag{A16}
\]

The changed carrier costs \(11Q_{j+1}\epsilon\) at \(j<L\), while
at \(j=L\) it is zero. The polynomial gate has modulus at most \(s+1\).
The gate discrepancy multiplied by the original carrier contributes
\(\epsilon K_j+t_2M(11U_{j-1}\epsilon)\), by (A11) and (A14).
These are exactly the terms in (A15).

For the training vector field take \(M=M_c+1\). Set

\[
Q_\xi=U_L+Q_1(M)+
\sum_{j=2}^L\{Q_j(M)(H_{j-1}+1)+B_jU_{j-1}\},
\qquad Q_f=RU_L,
\]
\[
C_F=2Q_f(G+1)+2(2Y+G)Q_\xi.
\tag{A17}
\]

Subtracting the gradient blocks gives
\(\|\widetilde\xi_a-\xi_a\|_2\le Q_\xi\epsilon\).
Subtracting the predictions gives
\(|\widetilde f_a-f_a|\le Q_f\epsilon\).
If also \(Q_\xi\epsilon\le1\), the polynomial gradient norm is at most
\(G+1\). Splitting the factors in the residual-gradient product in (2)
of the core note, and using the original residual bound \(2Y+G\), proves

\[
\sup_{\text{moving ball}}\|\widetilde F-F\|_2
\le C_F\epsilon.
\tag{A18}
\]

All training constants in (A15)--(A18) grow at most like
\(O(\sqrt{\log(en)})\) at fixed structural parameters.

## 4. Modified restart and a combined defect budget

Keep the real signed-stability constants \(A_n,C^{\rm r},J^{\rm r}\)
and \(C_{\rm src}\) from the core note. For a positive source horizon \(T\)
and target nodal error \(\delta_{\rm node}\), define

\[
e_d=e^{-A_n}\min\left\{\frac14,
 \frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},
 \frac{\delta_{\rm node}}{4C_{\rm src}n},\frac{b_n}{16}\right\},
\]
\[
\zeta_F=\min\{e_d/(2T),b_nL_n/4,V/2\},\qquad
\widehat R_n=\min\{r_t/2,(8L_n)^{-1}\}.
\tag{A19}
\]

Choose \(\epsilon\) satisfying (A13), \(Q_\xi\epsilon\le1\), and
\(C_F\epsilon\le\zeta_F\). A further source-output requirement is imposed in
the next section. Construct the activation polynomials once using (A6)--(A7).

There is a uniform derivative bound for the field perturbation in each ball
of radius \(b_n/2\) about the exact complex reference:

\[
\|D(\widetilde F-F)\|_{\rm op}\le2\zeta_F/b_n.
\tag{A20}
\]

For a unit complex parameter direction, the disk of radius \(b_n/2\)
about any such state remains in the original ball of radius \(b_n\).
Apply the vector-valued Cauchy integral formula to
\(\widetilde F-F\), using (A18). This proves (A20) without a
dimension-dependent conversion of coordinate derivatives.
The polynomial field is therefore \(2L_n\)-Lipschitz on that smaller ball.

The exact restarted solution of \(\dot v=\widetilde F(v)\) exists on the
complex disk of radius \(\widehat R_n\) whenever its real initial anchor
has distance at most \(b_n/8\) from the true original trajectory.
Repeat the core Picard map for the error, now with integrand
\(\widetilde F(\theta+e)-F(\theta)\) and error ball of radius \(b_n/2\).
Its contraction factor is at most \(2L_n\widehat R_n\le1/4\).
Its forcing at \(e=0\) is at most \(\zeta_F\). The map sends that ball
to radius at most

\[
b_n/8+\widehat R_n\zeta_F+(1/4)(b_n/2)
\le9b_n/32<b_n/2.
\]

The fixed point has error at most
\((b_n/8+b_n/32)/(1-1/4)=5b_n/24<b_n/4\).
Its velocity is at most \(V+\zeta_F\le2V\).
Thus its degree-\(K\) Taylor polynomial, on a half-radius real panel, has
tail at most \(2V\widehat R_n2^{-K}\). If this is at most \(b_n/4\),
the polynomial remains inside the smaller ball. Its defect against the
polynomial field is at most \(2V(2K+5)2^{-K}\), by the same differentiated
geometric series as the core proof. Its defect against the original field is
therefore at most

\[
2V(2K+5)2^{-K}+\zeta_F.
\tag{A21}
\]

Choose

\[
K=\max\left\{8,
\left\lceil2\log_2\max\{1,16TV/e_d\}\right\rceil,
\left\lceil\log_2\max\{1,8V\widehat R_n/b_n\}\right\rceil\right\}.
\tag{A22}
\]

The first error term in (A21), integrated over the horizon, is at most
\(e_d/2\), because \(2K+5\le4\,2^{K/2}\) for \(K\ge8\).
The second term contributes at most \(e_d/2\) by (A19).
Use \(N_{\rm step}=\lceil2T/\widehat R_n\rceil\) panels and the
explicit coefficient recurrence (30) of the core note, with
\(\widetilde F\) in place of \(F\).

The prefix induction from the core proof now gives
\[
\sup_{[0,T]}\|u(t)-\theta(t)\|_2
\le2e^{A_n}e_d
\le\min\{b_n/8,\delta_{\rm node}/(2C_{\rm src}n)\}.
\tag{A23}
\]
It justifies every successive restart and reserves half
the nodal error for evaluating sources with the activation polynomials.

## 5. Source values without derivative calls to the original activations

The original passive-query carrier RMS is at most \(K_j\) throughout the
operator/readout tube. Hence its coordinate maximum is at most
\[
M_q=\sqrt n\max_jK_j.
\]
Use (A15) with \(M=M_q\), and define
\[
C_p=8\sqrt n\max\{U_*,\max_jQ_j(M_q)\}.
\tag{A24}
\]
Choose, finally, the single sufficient scalar tolerance
\[
\epsilon=\min\left\{1,U_*^{-1},
\frac{a}{5632\sqrt nU_*},Q_\xi^{-1},
\frac{\zeta_F}{C_F},\frac{\delta_{\rm node}}{2C_p}\right\}.
\tag{A25}
\]
All denominators are positive; \(Q_\xi,C_F\) in this expression are
the training constants from (A17).

At each time/query node evaluate the network at \(u(t)\), using
\(\psi_j,\psi_j'\). Equations (A14), (A16), and RMS-to-coordinate
conversion show that the coordinate error from replacing the activations is
at most \(\sqrt n\max(U_*,\max_jQ_j(M_q))\epsilon\). Initialized
image actions cost at most eight in Euclidean norm, so every family, including
each image, has error at most \(C_p\epsilon\le\delta_{\rm node}/2\).
The original-activation source at \(u(t)\) differs from its true source at
\(\theta(t)\) by at most the other half, by (A23) and the core source
comparison. Every family has the required total coordinate tolerance.

Form initialized images directly from their computed base vectors. Pairing
therefore remains exact, and identical scalar coefficient quadrature preserves
it. The approximated training field and passive evaluations do
not introduce independent approximations to members of a pair.

The exact initialized additions to the source spaces are a separate operation:
evaluate their features with the original \(\phi_j\), and form their original
matrix images exactly in the same exact-real model as RESULT.md. These take
\(O(Lmn)\) real activation-value calls and \(O(mP)\) arithmetic. Initial
backward fields vanish because the readout is zero. No derivative call to the
original activation is required by this setup backend. The final compressed
network still evaluates the original activation and derivative during its
specified runtime; the polynomials are discarded after setup.

## 6. Degree, cost, and the ordinary Euler comparison

Fix the full admissible structural parameters, take
\(T=O(\log(en))\), and let \(\log(1/\delta_{\rm node})=O(\log(en))\).
Then (A19), (A24)--(A25) imply
\(\log(1/\epsilon)=O(\log(en))\): \(C_p=O(n)\), the training error
coefficients are \(O(\sqrt{\log(en)})\), and
\(e^{A_n}=\exp(O(\sqrt{\log(en)}))\). Equations (A3)--(A6) give
\[
D=O(\log(en)^{3/2}),\quad N_\phi=O(\log(en)^{3/2}),\quad
K=O(\log(en)),\quad N_{\rm step}=O(\log(en)^{3/2}).
\tag{A26}
\]
Also \(D\tau_i=O(\log(en))\), so the sufficient value-call accuracy
(A10) is polynomially small in \(n\). This is a precision requirement,
not a proof about a particular floating-point library.

Computing the coefficients in (A7) by cosine recurrences costs \(O(LD^2)\)
arithmetic and \(O(LD)\) retained coefficient words. It uses
\(O(LD)\) scalar activation calls and trigonometric calls at real arguments.
No complex activation values or high derivatives are requested.

Convert each Chebyshev polynomial to ordinary polynomial coefficients, or
evaluate its truncated series by the three-term Chebyshev recurrence.
Both give \(O(DK^2)\) arithmetic for one online degree-\(K\) scalar
composition, and \(O(DK)\) sufficient workspace. Each of the
\(D\) recurrence products is a convolution; accumulating its successive
coefficients through \(K\) costs \(\sum_{k\le K}O(k)=O(K^2)\).
The derivative polynomial can be prepared in \(O(D^2)\) arithmetic and
evaluated with the same bound.

Let \(N_t,N_x\) be the certified time/spatial quadrature node counts.
Including polynomial passive-query evaluations, a sufficient source-value
arithmetic bound is
\[
O\!\left(
LD^2+N_{\rm step}[mPK^2+LmnDK^2]
+PKN_t+PN_tN_x+LnDN_tN_x+mP
\right).
\tag{A27}
\]
In addition, there are \(O(LD+Lmn)\) original scalar activation-value
calls and \(O(LD)\) elementary trigonometric calls. A sufficient streamed
memory bound, before adding the unchanged source coefficient/selection arrays,
is
\[
O(PK+LmnDK+LD+Ln).
\tag{A28}
\]
At fixed parameters all arithmetic and call counts in (A27)--(A28),
and the certified quadrature/selection/assembly costs, are
\(n^{2+o(1)}\). If scalar activation values are unit-cost primitives,
this is the total arithmetic bound. If a concrete value routine is supplied,
add its explicitly requested costs at the arguments and tolerances above.
Nothing assumes an arbitrary analytic activation has an efficient
representation merely because it satisfies a strip bound.

For the user's comparison, ordinary explicit Euler with numerical step
\(h\) over physical horizon \(T\) takes
\(\Theta(mPT/h)\) arithmetic before query/source processing, up to its
activation costs. If its accuracy requirement calls for \(h=n^{-1/2}\)
at fixed structural parameters, that work is \(n^{5/2+o(1)}\);
the present high-order setup has \(n^{2+o(1)}\) work. This is a conditional
comparison using the stated Euler step requirement. The theorem does not
claim that every dense solver must use such a step, or prove a lower bound
against high-order dense solvers. It shows that covering the full physical
source horizon need not carry the width-dependent first-order time-step cost.
