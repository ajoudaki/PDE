# A proved late complex sector from the residual normal geometry

2026-10-08. One bounded independent theoretical route, frozen before reading
another live route. This note proves a complex sector for the original nonlinear
neural gradient flow under its existing fitting event. The sector is not an
additional analytic-domain assumption. Its explicit starting time is of order
`log n`; this does **not** prove near-squared-logarithmic retained storage.
The quantitative obstruction is the early part of the trajectory, not a
failure of complex continuation at the fitted endpoint.

The new statements are the residual-sector lemma in Section 2, its fully
specified neural specialization in Section 3, and the resulting early/late
source-rank decomposition in Section 4. They are internally derived results,
not independently reviewed or promoted results. No experiment or Git operation
was performed.

## 1. Contract and the exact residual equations

There are `m` training inputs and `p` passive inputs, fixed before initialization.
Write their normalized versions as \(v_i=x_i/\sqrt d\), with
\(\|v_i\|_2=1\). Only \(i\le m\) have labels. The canonical network is

\[
\begin{aligned}
z_i^{(1)}&=Av_i,&z_i^{(j)}&=W^{(j)}h_i^{(j-1)},&
h_i^{(j)}&=\phi_j(z_i^{(j)}),\\
f_i&=w^\top h_i^{(L)}/n,&r_a&=f_a-y_a,&
\mathcal L&=m^{-1}\sum_{a=1}^m r_a^2.
\end{aligned}                                                    \tag{1}
\]

Here \(A\in\mathbb R^{n\times d}\),
\(W^{(j)}\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\).
The initialization has independent first entries \(N(0,1)\), middle
entries \(N(0,1/n)\), and exactly zero readout. All blocks train with
mobilities \((n,1,\ldots,1,n)\). Define the residual-free responses by

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot
 W^{(j+1)\top}\delta_a^{(j+1)}.                                  \tag{2}
\]

The activations are real on the real axis, holomorphic for
\(|\operatorname{Im}z|<a\), and have bounded first derivative there;
their values need not be bounded. Use the original full label interval
in `PANEL_BOUND.md` (3), without an extra small-label restriction. Set

\[
Y=\|y\|_2/\sqrt m>0,\qquad \lambda=\gamma/m>0,
\qquad S=16Y/\lambda,\qquad \ell=\log(en).
\]

The zero-label branch is the exact constant trajectory and needs none of
the divisions below.

Use Euclidean normalized parameter coordinates

\[
u=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]

Their Euclidean norm is exactly the paper's parameter norm. The gradient
\(\xi_a=\nabla_u f_a\), a vector in the direct sum of the parameter
blocks, has blocks

\[
\xi_a=
\left(\frac{\delta_a^{(1)}v_a^\top}{\sqrt n},
 \left(\frac{\delta_a^{(j)}h_a^{(j-1)\top}}n\right)_{j=2}^L,
 \frac{h_a^{(L)}}{\sqrt n}\right).
\]

Define the normalized residual \(e=r/\sqrt m\), the matrix
\(X(u)=m^{-1/2}[\xi_1(u),\ldots,\xi_m(u)]\), and its algebraic
Gram \(C(u)=2X(u)^\top X(u)\). Their exact equations are

\[
\dot u=-2X(u)e,\qquad \dot e=-C(u)e.                            \tag{3}
\]

All transposes in complex continuations of these formulas are algebraic
transposes. Norms and norm derivatives use the ordinary Hermitian norm.
For real parameters, \(C\) is real symmetric positive definite on the
fitting event. The existing dense theorem gives, at every real time,

\[
C(u(t))\succeq \frac\lambda2 I_m,\qquad
\|e(t)\|_2\le Ye^{-\lambda t/2},\qquad
\|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda.                         \tag{4}
\]

The first inequality follows already from the top feature Gram, whose
normalized gap is at least \(\lambda/4\). The first matrix divided by
\(\sqrt n\), and all middle matrices, have operator norm below
\(8+1/8\). These are consequences of the existing full label interval,
not assumptions added by this route.

## 2. Residual-sector lemma

Let an analytic least-squares system have the exact form (3). Fix a real
state \(u_0\), residual \(e_0\), and constants \(b,G,\mu>0\).
Suppose the maps in (3) are holomorphic on a neighborhood of the closed
complex Euclidean ball \(\|u-u_0\|_2\le b\), and throughout that ball

\[
\|X(u)\|_{\rm op}\le G,\qquad
C(u_0)\succeq\mu I_m,\qquad
\|C(u)-C(u_0)\|_{\rm op}\le\mu/4.                            \tag{5}
\]

If

\[
\|e_0\|_2\le\frac{\mu b}{16G},                              \tag{6}
\]

the solution from \(u_0\) extends holomorphically to the entire open
sector \(|\arg\zeta|<\pi/3\), together with a neighborhood of its
vertex and every finite point of its two boundary rays. For
\(\zeta=se^{i\vartheta}\), \(s\ge0\), \(|\vartheta|\le\pi/3\),

\[
\|e(\zeta)\|_2\le\|e_0\|_2e^{-\mu s/4},\qquad
\|u(\zeta)-u_0\|_2\le\frac{8G}{\mu}\|e_0\|_2\le b/2.
                                                                  \tag{7}
\]

This is a theorem with checkable local-ball hypotheses. Section 3 checks
every hypothesis for the neural model using explicit constants.

To prove it, first continue along a ray, provisionally stopped on the
ball boundary. Equations (3) become
\(de/ds=-e^{i\vartheta}C(u)e\) and
\(du/ds=-2e^{i\vartheta}X(u)e\). Since \(C(u_0)\) is real symmetric,

\[
\begin{aligned}
\frac12\frac d{ds}\|e\|_2^2
&=-\operatorname{Re}\{e^*e^{i\vartheta}C(u)e\}\\
&\le-\bigl(\mu\cos\vartheta-\|C(u)-C(u_0)\|_{\rm op}\bigr)
       \|e\|_2^2
\le-\frac\mu4\|e\|_2^2.
\end{aligned}
\]

Integration proves the first estimate in (7); integration of
\(\|du/ds\|_2\le2G\|e_0\|_2e^{-\mu s/4}\) proves the second.
The state stays in half the ball, so it cannot reach the stopped boundary.
Local holomorphic Picard iteration extends the ODE at every finite point:
on a smaller parameter ball its analytic vector field and derivative are
bounded, and the integral Picard map contracts when the complex time
radius times that derivative bound is below one. A finite-length failure
of continuation is therefore impossible.

For completeness, ray continuation does give one holomorphic function,
not unrelated raywise branches. Solve on \(0\le q\le1\) the equation
\(dU/dq=\zeta[-2X(U)e(U)]\), \(U(0)=u_0\). The preceding bound gives
this solution for every \(\zeta\) in the sector. On each compact
subinterval in \(q\), parameter-dependent Picard iterations are
holomorphic in \(\zeta\); finitely many such intervals cover
\([0,1]\). Uniqueness identifies their endpoint with the ray solution.
This supplies a single locally holomorphic endpoint map. The strict
ball margin and the strict bound \(\mu/4>0\) also give a neighborhood
at every finite boundary point.

Every ray has a limiting parameter state by the integrable velocity in
(7). These limits coincide with the real fitted limit. On the circular
arc \(Re^{i\vartheta}\), its state derivative has norm at most
\(2G\|e_0\|_2e^{-\mu R/4}\); the arc length is at most
\(2\pi R/3\). The difference between two points on that arc therefore
tends to zero. Passing to the ray limits proves their equality. This
argument gives a common sectorial fitted limit without claiming that any
single exponential clock is analytic through its compact endpoint.

## 3. Explicit neural ball and sector start

Here are conservative coefficients that verify (5). They depend on
\(L,a,Y,\lambda\), and activation derivative bounds, with no hidden
exponential dependence on \(m\). Let

\[
b_\phi=\max_j|\phi_j(0)|,\quad
s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\},
\quad
t_2=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\},
\quad R_w=1+2Y/\sqrt\lambda.
\]

Define positive structural recurrences

\[
\begin{gathered}
H_1=\max(1,b_\phi+11s),\qquad
H_j=\max(1,b_\phi+11sH_{j-1}),\\
B_j=R_ws(11s)^{L-j},\qquad
P_1=1,\qquad P_j=H_{j-1}+11sP_{j-1},\qquad P_* =\max_jP_j,\\
G=H_L+B_1+\sum_{j=2}^L B_jH_{j-1},\qquad
C_k=R_w(11s)^L.
\end{gathered}                                                    \tag{8}
\]

The local \(H_j,B_j\) here are new ball estimates; they are not silently
identified with the smaller source-event recurrences in `PANEL_BOUND.md`.
For \(M\ge0\), put

\[
\begin{gathered}
\kappa_L(M)=1,\\
\kappa_j(M)=11s\kappa_{j+1}(M)+11t_2MP_{j+1}+B_{j+1},\\
D_j(M)=s\kappa_j(M)+t_2MP_j,\\
J(M)=sP_L+D_1(M)+
 \sum_{j=2}^L\{H_{j-1}D_j(M)+B_jsP_{j-1}\}.
\end{gathered}                                                    \tag{9}
\]

All these expressions are finite scalar recurrences. In particular
\(J\) is affine with nonnegative coefficients. Set

\[
\mu=\lambda/2,\qquad
c_b=\min\left\{1,\frac a{4P_*},\frac\mu{16GJ(C_k)}\right\},
\qquad b_n=\frac{c_b}{\sqrt n},
\qquad
t_{\rm sec}=\frac1\mu
 \log_+\frac{16GY\sqrt n}{\mu c_b}.                           \tag{10}
\]

For every real anchor \(t_0\ge t_{\rm sec}\), the neural solution
extends to the sector

\[
\zeta=t_0+se^{i\vartheta},\qquad
s\ge0,\quad |\vartheta|\le\pi/3,                             \tag{11}
\]

and stays within parameter distance \(b_n/2\) of \(u(t_0)\).
It obeys (7), with \(e_0=e(t_0)\), on this entire sector. Thus for
every real \(t>t_0\) it is analytic on a neighborhood of the closed disk

\[
|\zeta-t|\le(t-t_0)/2.                                       \tag{12}
\]

The disk lies strictly inside (11), since its radius divided by
\(t-t_0\) is \(1/2<\sin(\pi/3)\).

We verify the neural specialization in detail. A parameter displacement
of norm at most one increases each operator bound in (4) by at most
one, so all normalized first and middle operators remain below eleven.
It also leaves readout RMS below \(R_w\). Up to a first activation-strip
exit on a straight segment from the real anchor, the forward recursion
and \(|\phi_j(z)|\le b_\phi+s|z|\) give

\[
\frac{\|h_i^{(j)}\|_2}{\sqrt n}\le H_j,\qquad
\frac{\|z_i^{(j)}(u)-z_i^{(j)}(u_0)\|_2}{\sqrt n}
 \le P_j\|u-u_0\|_2.                                        \tag{13}
\]

The coordinate displacement is consequently at most
\(\sqrt nP_*b_n\le a/4\). Starting from real preactivations, this
strictly prevents an exit from \(|\operatorname{Im}z|<a/2\). The
argument works for every declared input, indeed for every real unit
input, on the whole closed ball. The operator and strip margins imply
holomorphy on a neighborhood of that ball. Backward propagation gives
\(\|\delta_a^{(j)}\|_2/\sqrt n\le B_j\), and (8) gives
\(\|\xi_a\|_2\le G\). Hence \(\|X\|_{\rm op}\le G\) by
the Frobenius bound and the exact \(m^{-1/2}\) normalization.

At the real anchor define the carriers
\(k_a^{(L)}=w\) and
\(k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}\) for \(j<L\).
Their RMS bounds imply the valid coarse coordinate bound
\(\max_{a,j}\|k_a^{(j)}(u_0)\|_\infty\le\sqrt n C_k\).
This uses no extra probabilistic carrier theorem. Subtracting the
backward recursion at an arbitrary ball state and this real anchor,

\[
\Delta\delta^{(j)}=
 \phi_j'(z^{(j)}(u))\odot\Delta k^{(j)}
 +[\phi_j'(z^{(j)}(u))-\phi_j'(z^{(j)}(u_0))]\odot k^{(j)}(u_0),
\]

gives RMS difference at most \(D_j(M)\|u-u_0\|_2\), where
\(M=\sqrt nC_k\). The carrier recursion gives \(\kappa_j(M)\):
its changed mixer costs \(B_{j+1}\), and its propagated response
costs \(11D_{j+1}(M)\). Combining these estimates with (13) in the
three gradient blocks proves

\[
\|\xi_a(u)-\xi_a(u_0)\|_2\le J(M)\|u-u_0\|_2,
\qquad
\|X(u)-X(u_0)\|_{\rm op}\le J(M)\|u-u_0\|_2.                \tag{14}
\]

For complex matrices the algebraic transpose still has the same
operator norm as the original matrix. Subtracting the two algebraic
Grams and using (14) therefore yields

\[
\|C(u)-C(u_0)\|_{\rm op}
 \le4GJ(\sqrt nC_k)b_n
 \le4GJ(C_k)c_b\le\mu/4.                                    \tag{15}
\]

The middle inequality uses positive affineness:
\(J(\sqrt nC_k)\le\sqrt nJ(C_k)\) for \(n\ge1\).
Equations (4) and (10) give
\(\|e(t_0)\|_2\le\mu b_n/(16G)\), exactly (6). This proves
(11)–(12) from the existing neural hypotheses, with no new Gaussian
event and no assumption of an enlarged stopped cavity domain.

Every required source curve is bounded on (11) by

\[
\|q(\zeta)\|_\infty\le M_{\rm sec}\sqrt n,
\qquad M_{\rm sec}=8\max_j\{H_j,B_j\},                       \tag{16}
\]

where \(q\) is any \(h_i^{(j)}\), initialized forward image,
\(\delta_a^{(j)}\), or initialized transpose image. Equation (16)
uses the initial operator bound eight and converts RMS to a coordinate
bound. It covers all \(m+p\) forward sources and the \(m\) training
backward sources. No passive label or passive Gram inverse is introduced.

For fixed admissible data and activations, (10) is quantitatively

\[
t_{\rm sec}=\lambda^{-1}\log n+O_{L,a,\phi,Y,\lambda}(1)
\quad\text{as }n\to\infty.                                 \tag{17}
\]

This is a width-uniform formula for the start time, not a width-uniform
positive analytic neighborhood of the whole training interval.

## 4. Consequence for source rank and retained storage

The source event already gives disks of radius

\[
r_n=\frac{a}{1024\lambda (Y/\lambda)^2U_{\rm fin}(S)\sqrt\ell}
\quad\text{through }T_0=32\ell/\lambda.
\]

Assume the eventual gate \(t_1=t_{\rm sec}+r_n\le T_0\).
On \([0,T_0]\) combine that event with (12) to obtain the proved radius

\[
\varrho(t)=
\begin{cases}
r_n/2,&0\le t\le t_1,\\
(t-t_{\rm sec})/2,&t_1\le t\le T_0.
\end{cases}                                                   \tag{18}
\]

This is positive, continuous, nondecreasing, and Lipschitz with constant
\(1/2\). Every associated disk has a holomorphic neighborhood and
coordinate source bound \(M\sqrt n\), where
\(M=\max\{M_0,M_{\rm sec}\}\), with \(M_0\) from `PANEL_BOUND.md`.
The adaptive panel lemma in `ADAPTIVE_APPROXIMATION.md`, whose Taylor-tail
and exact-image argument applies verbatim, gives the following explicit
number of panels:

\[
J_{\rm panels}\le
1+5\frac{t_1}{r_n}
 +5\log\frac{T_0-t_{\rm sec}}{r_n}.                          \tag{19}
\]

Indeed \(\int_0^{t_1}dt/\varrho(t)=2t_1/r_n\), the remaining
integral is \(2\log[(T_0-t_{\rm sec})/r_n]\), and the lemma multiplies
their sum by \(2+1/2\). This explicit estimate separates the early cost
from the now logarithmic late cost.

For prescribed source tolerance \(\eta>0\), let

\[
K=\max\left\{0,\left\lceil\log_2\frac{8M\sqrt n}{\eta}
                    \right\rceil\right\},\qquad
F=2(2m+p),\qquad B=2m+d+1,
\qquad R=B+FJ_{\rm panels}(K+1).                             \tag{20}
\]

Each Taylor polynomial has coordinate tail at most \(\eta/8\).
Coefficients at real anchors are computed by the existing finite
initial-data continuation/jet evaluator. Compute each initialized
forward or transpose image from its computed preimage, so the image
pairing remains exact. The rank estimate does not retain an exact
endpoint, a complex-contour trajectory oracle, or a time-indexed forcing.
Anchors, source vectors and jets are discarded after selection.

The original coordinate selector and corrected nonlinear optimizer then
have precisely the sufficient retained inventory

\[
1020(L+1)R^2+36R+10m(d+1)+pd+(m+p)+D_{\rm alg}.               \tag{21}
\]

It includes all dense selected metrics, inverse caches, initialized
mixers, learned matrices, training work arrays, declared data, outputs
and evaluator storage. A rank bound cannot be substituted for the
quadratic term. The exact panel-span reduction can replace the first
input dimension in \(B\) by at most \(m+p\), with its separately counted
\(O((m+p)d)\) map/input overhead.

For either original variability-scale accuracy or the stronger output
target \(Y/n\), the prescribed tolerance has \(K+1=O(\ell)\),
including the actual comparison factor \(e^{64\sqrt\ell}\). From
(17) and (19),

\[
J_{\rm panels}=O(\ell^{3/2}),\qquad
R=O(\ell^{5/2}),\qquad
\operatorname{storage}=O(\ell^5).                            \tag{22}
\]

The late portion alone costs \(O(\log\ell)\) panels and hence
\(O(\ell\log\ell)\) coefficient vectors per source. The early portion
still determines (22). No smaller logarithmic power has been proved.

The inherited source-to-runtime comparison remains
\(\sup_{t\in[0,\infty]}\max_i|f_C(t,v_i)-f_n(t,v_i)|
\le\mathcal A_n\eta+\mathcal D e^{-8\ell}\).
It uses the same physical-time optimizer and the same fitted-tail
argument, including the endpoint. The newly proved sector does not
replace that comparison or silently narrow its label allowance.

## 5. Exact obstruction left by this route

The generic analytic-domain question has been advanced: a fixed-width
neural fitted path has a sector of aperture \(2\pi/3\), with explicit
polynomial-width source bound and explicit start time, under the
original fitting conditions. Neither analytic stable-manifold theory,
nonresonant spectra, nor a common endpoint-analytic scalar clock was
assumed. Irrational residual decay rates do not obstruct this result.

The decisive width loss occurs in (13): a normalized parameter ball of
radius \(b\) controls every individual preactivation only by
\(\sqrt nP_*b\). For an arbitrary parameter ball this factor is real,
not just an algebraic mistake. At the first layer, for a unit input
\(v\), changing one row of \(A\) by \(i\sqrt n b\,v^\top\) has
normalized parameter norm \(b\) and changes its preactivation by
\(i\sqrt n b\). Thus the present isotropic-ball argument cannot certify
a width-independent activation-strip margin from its stated hypotheses.
This example is a local parameter direction, not a claim that a trained
complex trajectory reaches it or that the neural compression conjecture
is false.

Replacing the coarse carrier estimate by the existing
\(O(S\sqrt\ell)\) real carrier bound improves the Gram-continuity
radius in (15), but does not remove this first-layer pole-control cost.
Conversely, proving the sector starts at a width-independent positive
time would still leave \(O(r_n^{-1})=O(\sqrt\ell)\) early panels if
the original strip were the only early information. That would yield
third-power storage, not near-second-power storage, with this recipe.

More precisely, if an improved argument supplied the same sector from
an onset \(t_*(n)\), while keeping only the original early strip, (19)
would give

\[
R=O\!\left(F\ell\left[1+\frac{t_*(n)}{r_n}
                         +\log\ell\right]+B\right).         \tag{23}
\]

Near-squared-logarithmic storage therefore requires
\(t_*(n)/r_n\) to be bounded by iterated-logarithmic factors, or a
separate approximation theorem eliminating the early-strip cost.
An ordinary \(O(1)\) or \(O(\log\log n)\) burn-in does not suffice
with the current early-strip estimate.

The missing obligation is consequently a quantitative complex
**reachable-state** estimate near early times, or a nonpolynomial source
approximation that bypasses that domain. It must control both forward
features and training adjoints, including their exact initialized
images. The residual-sector lemma by itself cannot supply this
anisotropic reachability information. No general no-go statement, new
probability theorem, or claim of near-second-power storage follows from
this bounded round.

Inputs read completely were the assigned `ADAPTIVE_APPROXIMATION.md`,
`CLOCK_GEOMETRY.md`, and `PANEL_BOUND.md`, the maintained notation
contract, and the required mathematical skill files and references.
Current-paper passages read were the complete global-fitting and uniform-tail
proof (around lines 9074–9210), the full late analytic-extension subsection
(around lines 12522–12661), and the complete explicit complex-endpoint
subsection (around lines 18949–19191). No other study, live route,
empirical output, or history was read. Only this note was written.
