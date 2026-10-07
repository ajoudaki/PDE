# Finite-order probability reduction for the insertion source

2026-10-07. Scoped continuation after explicit authorization to read the
original finite-neuron insertion proofs. This note gives a quantitative
moment/collision reduction and identifies the exact numerical local estimate
still needed. It does not assert a polynomial stochastic success width for
the trained source. The completed original-initialization/dense-fitting
theorem is in `EXPLICIT_FITTING_WIDTH.md`.

The scientific model, Gaussian initialization, zero readout, original label
allowance, and physical optimizer remain those of that fitting note and the
assigned integrated source. Write \(\lambda=\gamma/m\),
\(Y=\|y\|_2/\sqrt m>0\), \(S=16Y/\lambda\), and
\(\ell_n=\log(en)\). The case \(Y=0\) is stationary. Activation values
may grow linearly; first and second derivatives have the stipulated strip
bounds. Real third derivatives are bounded by Cauchy's formula on a disk
of radius \(a/4\), applied to the bounded half-strip second derivative.
Thus \(\sup_{\mathbb R}|\phi'''|\le4\beta/a\le\beta^2/4\).

## 1. What reading the original proofs resolves

The original `DEPTH_CAVITY_ROUTE.md`, Sections 4--5, and
`UNBOUNDED_INSERTION_CHECK.md`, Section 3, exhibit the powers
\[
a=1/100,\quad b=1/10,\quad \kappa=1/1000,\quad
\|U\|\le n^{-1/25},\quad \epsilon_{n,p}=C_pn^{-1/30}.
\tag{1}
\]
Here \(U\) is the nonlinear remainder after subtracting the Gaussian
linear variation, and \(p\) is the number of deleted neurons in one
layer. They compare a Gaussian exponent near \(n^{0.79}\) with a
control entropy near \(n^{0.625}\). They also give the exact retained
equation, including both omitted directions and the adaptive residual.
For an interior deletion set \(I\),
\[
\dot\Theta=-\frac2m\sum_a r_a\left[
\nabla_\Theta\mathcal F_a(\Theta,e)
+D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right],
\]
\[
\mathcal F_a=nf_n(v_a),\quad r_a=\mathcal F_a/n-y_a,\quad
e_a=\sum_{i\in I}W^{(j+1)}_{:,i}h_{a,i}^{(j)},\quad
q_a=\sum_{i\in I}W^{(j)\top}_{i,:}\delta_{a,i}^{(j)}.
\tag{2}
\]
The mobility coordinates are
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
Deleting an activation means a rectangular cavity with normalization still
\(n\); it does not mean replacing its preactivation by zero. At the top,
the omitted prediction offset multiplies the retained gradient and reverse
force, as specified in the unbounded check.

The original proofs do not specify numerical bounds on \(C_p\), their
control-speed constants, or the exponents denoted by \(C_L\) in
\((\log n)^{C_L}\) and \((1+M_n)^{C_L}\). Their statements explicitly
take \(n\to\infty\) at each fixed \(p\), before taking \(p\to\infty\).
Reading these proofs therefore identifies the missing calculation, but
does not itself supply a finite-confidence theorem. A reference to their
internal PASS statements does not replace that calculation.

## 2. A small deterministic exponent controls collisions

Use the *unchanged* integrated source constants
\[
\eta=\min\{1,(1024C_{\rm abs}W_{\rm G})^{-1}\},\qquad
\mathcal B=1024e^2L,\qquad
K_{\rm src}=16C_{\rm abs}(1+C_G),
\]
\[
C_G=32\max\{1,H_{\max},\max_j\tau_j\},\qquad
W_{\rm G}=128\{1+H_{\max}+s\max_jV_j+\max_jG_j\}.
\tag{3}
\]
These quantities are the recurrences in `UNBOUNDED_COMPRESSOR_BRIDGE.md`,
(5)--(10) and (22). In particular \(s\ge1\),
\(\max_j\tau_j=\tau_1\), and \(V_1=\tau_1\). If
\(M=\max\{1,H_{\max},\max_j\tau_j\}\), then
\(W_{\rm G}\ge128M\) and \(1+C_G\le33M\). Hence
\[
2\eta K_{\rm src}\le\frac{1+C_G}{32W_{\rm G}}
\le\frac{33}{4096}<\frac1{100}.
\tag{4}
\]
On the source's stopped coordinate-maximum event, define, for one sample
and layer,
\[
X_i=\sup_z|z_{a,i}^{(j)}(z)|+
S^{-1}\sup_z|k_{a,i}^{(j)}(z)|,\qquad B_i=e^{\eta X_i}.
\]
The suprema use the same stopped time domain as the source. Its maximum
bound gives \(X_i\le2K_{\rm src}\sqrt{\ell_n}\), so (4) yields
\[
0\le B_i\le e^{\sqrt{\ell_n}/100}
\le e^{1/100}n^{1/100}=:W_n.
\tag{5}
\]
This has an absolute numerical exponent and holds for every \(n\ge1\);
there is no unspecified onset in (5). The coordinate-maximum event is a
stopped local-insertion conclusion preceding joint-budget removal in the
integrated proof. Its failure probability remains part of the local event
that must be quantified, rather than an assumed consequence of fitting.

Here is a general finite-order lemma. Let \(E\) be any event, let
\(0\le B_i\le W\) on \(E\), and suppose, for all distinct index sets
\(I\) with \(1\le |I|\le p\),
\[
\mathbb E\left[\mathbf1_E\prod_{i\in I}B_i\right]\le D^{|I|},
\qquad D\ge1.
\tag{6}
\]
No independence of the \(B_i\) or of \(E\) is assumed. Then
\[
\mathbb E\left[\mathbf1_E
\left(\frac1n\sum_iB_i\right)^p\right]
\le D^p\exp\left\{\binom p2\frac{W}{Dn}\right\}.
\tag{7}
\]
To prove it, classify an ordered \(p\)-tuple by its partition into
\(k\) equal-index blocks. On \(E\), retain one factor per distinct
index and bound its \(p-k\) repeated factors by \(W^{p-k}\). For a
fixed partition there are at most \(n^k\) choices of distinct labels,
and (6) bounds the remaining product by \(D^k\). If \(j=p-k\), the
number of such partitions is at most
\(\binom{\binom p2}{j}\): map each block to the star joining its least
element to the others; the resulting \(j\)-edge graph determines the
partition. Thus its count is at most \(\binom p2^j/j!\). Summing over
\(j\) gives (7).

With \(W=W_n\) from (5), the very simple sufficient gate
\(n\ge4p^3\) makes the exponential in (7) at most \(e\). The proof
uses only distinct-root moments through order \(p\). It never requests
Gaussian exponential moments at coefficient \(p\eta\) for repeated
copies of a single main reference. This removes the potentially
\(e^{Cp^2}\) collision loss in a direct application of the old argument.

Apply this lemma to every sample/layer and let \(E\) include the common
initialization and local events. If the distinct-product base in (6) is
at most sixteen, then
\[
\Pr\{\text{joint budget hit},E\}
\le e mL(16L/\mathcal B)^p
\quad(n\ge4p^3).
\tag{8}
\]
Indeed a sample's layer sum reaching \(\mathcal B\) forces one layer
average to reach \(\mathcal B/L\); apply Markov and then the union bound.
The explicit choice
\[
p=\max\left\{1,\left\lceil
\frac{\log(4emL/\delta)}{\log(\mathcal B/(16L))}
\right\rceil\right\}
\tag{9}
\]
makes (8) at most \(\delta/4\). What remains is a finite-width local
event and the finite-width version of (6), not a collision estimate.

## 3. Explicit propagation of a common-cavity Gaussian correction

The following lemma separates the remaining error term from the main
conditionally independent references. Suppose, for a set of \(k\)
distinct indices, there is a pathwise upper bound on \(E\)
\[
B_i\le A_i e^{a E_i},\qquad A_i,E_i\ge0,\qquad a\ge0.
\tag{10}
\]
Assume, after dropping the indicator, that
\(\mathbb E\prod_iA_i^2\le D_0^{2k}\), and that the Gaussian
supremum corrections satisfy the unconditional bounds
\[
\log\mathbb E e^{uE_i}\le u\mu+u^2v^2/2
\quad\text{for every }u\ge0.
\tag{11}
\]
The corrections need not be mutually independent. Cauchy--Schwarz between
the two products, and Holder with \(k\) equal exponents for the correction
factors, give
\[
\mathbb E\left[\mathbf1_E\prod_iB_i\right]
\le D_0^k\exp\{ak\mu+a^2k^2v^2\}.
\tag{12}
\]
Thus \(a\mu+a^2pv^2\le\log(16/D_0)\), with \(D_0<16\), is an
explicit sufficient condition for (6) at every \(k\le p\).

For a centered Gaussian process expressed as a supremum of linear
functionals with coefficient norms at most \(v\), its supremum is
\(v\)-Lipschitz in its Gaussian roots. The concentration proof in the
fitting note therefore proves (11), with \(\mu\) an upper bound for
its mean. A deterministic dyadic entropy bound is enough to supply this
mean; conditioning on retained initialization is allowed only when the
whole reference coefficient process is measurable there.

For the projected singleton-to-common-cavity error in the old argument,
both complete independently stopped paths omit the particular paired
root. Radial projection of their *whole difference path* onto a fixed
Euclidean ball preserves that independence. If a quantitative local lemma
gives normalized Gaussian radius
\[
v=C_p n^{-49/100},
\tag{13}
\]
and metric cover bound \(N(\epsilon)\le C(1+A/\epsilon)^2\), dyadic
grids starting at radius \(v\) give
\[
\mu\le C_{\rm num}v\sqrt{\log(2+C)+\log(2+A/v)}.
\tag{14}
\]
One derives this by bounding the level \(j\) maximum of at most
\(C(1+2^jA/v)^2\) Gaussian increments, each of standard deviation
at most \(2^{1-j}v\), by its Gaussian tail and integrating that tail.
The resulting series is a numerical multiple of
\(\sum_{j\ge0}2^{-j}v\sqrt{\log(2+C)+\log(2+A/v)+j}\), which is
bounded by (14). This argument does not require independence between
the increments. It also shows explicitly where the unknown local
coefficient \(C_p\) enters.

For complex-minus-real errors, the assigned integrated source gives a
radius proportional to
\[
(\lambda c J_*^{\rm time})\ell_n^{-1/2}
\left[1+(S^2/\eta)\log(e+\ell_n)\right].
\tag{15}
\]
Its source allowance implies \(S^2/\eta\le1\). The width function
\((1+\log(e+x))^{3/2}/\sqrt x\) is bounded by \(3\sqrt3\) for
\(x\ge1\): use \(\log(e+x)\le2+\log x\) and maximize
\((3+u)^{3/2}e^{-u/2}\), \(u=\log x\ge0\). A smaller contour
coefficient can therefore keep finite-order correction moments bounded,
instead of waiting for their radii to vanish at each fixed moment order.
To turn this observation into a certified choice of \(c\), the metric
cover constants in (14) must also be made explicit on the complex contour.
The source's asymptotic mean statement alone does not perform that step.
No smaller label allowance is needed for the algebra (10)--(15).

## 4. An explicit local-net inequality before any asymptotic absorption

The old local exponents can be made quantitative once their raw
coefficients are known. The following calculation records that interface
without declaring the coefficients bounded by an unproved polynomial.

Consider \(q\) real scalar control functions on \([0,T]\), with amplitude
at most \(M\) and Lipschitz constant at most \(D\sqrt n\). For uniform
accuracy \(\tau=n^{-1/8}\), sample at spacing at most
\(\tau/(4D\sqrt n)\), round values on a mesh of spacing at most
\(\tau/2\), and interpolate. The elementary net cardinality satisfies
\[
\log N_{\rm ctrl}\le
q(2+4TDn^{5/8})\log(1+4Mn^{1/8}).
\tag{16}
\]
The source has \(q=2mp\) real controls for an interior deletion. For a
complex contour, use \(q=4mp\) real component controls and approximate
each component to accuracy \(\tau/2\); the resulting complex sup error
is at most \(\tau\). The charged net bound is then
\(q(2+8TDn^{5/8})\log(1+8Mn^{1/8})\), in place of (16). A separate
finite terminal-time grid contributes its actual logarithmic cardinality.
The conditioning is on the autonomous retained cavity; the controls are
deterministic during this calculation and may be chosen adaptively only
after the uniform event has been established.

For fixed controls, suppose every needed linear Gaussian map, as an
operator on the concatenation of the \(2p\) omitted roots, has norm at
most \(A n^\kappa\ell_n^k\), with \(\kappa=1/1000\). Every coordinate
then has variance at most \(A^2 n^{-1+2\kappa}\ell_n^{2k}\).
The tail at \(n^{-b}/4\), \(b=1/10\), is at most
\[
2\exp\left[-\frac{n^{1-2b-2\kappa}}
{32A^2\ell_n^{2k}}\right].
\tag{17}
\]
The full Euclidean image has expected norm at most
\(\sqrt{2p}A n^\kappa\ell_n^k\), because its Gaussian input has
dimension \(2pn\) and covariance \(I/n\). A Gaussian Lipschitz tail
then bounds its Euclidean norm by \(n^{1/100}\) provided the expectation
is below half that threshold; the remaining tail is stronger than (17).

For a concatenated root vector \(\zeta\sim N(0,I_{2pn}/n)\), the
quadratic fluctuation below is explicitly the centered form
\(\zeta^\top R\zeta-\operatorname{tr}(R)/n\). An operator bound of
the same size gives Hilbert--Schmidt bound at most
\(\sqrt{2pn}A n^\kappa\ell_n^k\). Diagonalizing the symmetric part,
using the exact Gaussian-square moment generating function, and bounding
\(-\log(1-u)-u\) by \(u^2/[2(1-|u|)]\), proves the tail
\[
2\exp\left[-c_{\rm num}\min\left\{
\frac{n^{1-2b-2\kappa}}{pA^2\ell_n^{2k}},
\frac{n^{1-b-\kappa}}{A\ell_n^k}\right\}\right].
\tag{18}
\]
Independent-root bilinear forms use the symmetric block matrix with
off-diagonal blocks \(R/2,R^\top/2\). Equations (17)--(18) are bounds
for one real scalar test. For a complex test with target modulus threshold
\(u\), test its real and imaginary parts at threshold \(u/2\) and
union their failures. Thus the leading factor two becomes four and, at
the displayed coordinate threshold, the denominator 32 in (17) becomes
128. In (18) one may divide the numerical exponent constant by four.
The numerical constant for one real test can, for example, be
chosen as \(1/1024\) at the thresholds above.

These tail estimates are initially for the finite control and terminal-time
grids. A pointwise operator bound does not justify interpolation to every
control or time, and hence does not yet justify substituting adaptive
controls. The interpolation step also needs a root-norm event and
deterministic moduli of the response maps. For each fixed deletion set,
Gaussian norm concentration gives
\[
\Pr\{\|\zeta\|_2>2\sqrt{2p}\}\le e^{-pn}.
\tag{18a}
\]
Indeed its mean norm is at most \(\sqrt{2p}\), and its Lipschitz
coefficient in standard Gaussian roots is \(1/\sqrt n\). This failure
must also be included in any union over deletion sets.

For the linear maps, the needed control modulus is supplied by (26)--(27).
If two control histories differ in sup norm by at most \(\tau\), define
\(V_n(\tau),Z_j(\tau),H_j^{\rm lin}(\tau),K_j^{\rm lin}(\tau),
D_j^{\rm lin}(\tau)\) by replacing only \(A_n,B_n\) there by
\(\tau,\tau\). Keep the reference coefficients \(M_n,M_\delta\),
\(J_n\), and all layer bounds unchanged. The linear response is linear
in the controls at the fixed cavity, so those recurrences bound its
operator difference. If \(\Omega_{\rm lin}(\tau)\) is their maximum,
(18a) bounds every corresponding vector difference by
\(2\sqrt{2p}\,\Omega_{\rm lin}(\tau)\). Thus the explicit sufficient
linear interpolation gate is
\[
2\sqrt{2p}\,\Omega_{\rm lin}(n^{-1/8})\le n^{-b}/4.
\tag{18b}
\]
The separately introduced lower-adjoint probes do not depend on these
control histories; their terminal-time modulus still requires a bound.

The missing quadratic interface is a numerical bound
\(\Omega_{\rm quad}(\tau)\) on the operator difference of each
quadratic response matrix when the controls change by \(\tau\).
For two centered forms, (18a) then bounds their difference by
\[
(\|\zeta\|_2^2+2p)\Omega_{\rm quad}(\tau)
\le10p\,\Omega_{\rm quad}(\tau).
\]
The trace contribution is included here using
\(|\operatorname{tr}(R-R')|/n\le2p\|R-R'\|_{\rm op}\).
One must prove this modulus and a gate
\(10p\Omega_{\rm quad}(n^{-1/8})\le n^{-b}/4\).
Likewise, for terminal-time mesh size \(h\), linear and quadratic
operator moduli \(\Omega_{{\rm lin},t}(h)\) and
\(\Omega_{{\rm quad},t}(h)\) must satisfy the corresponding gates
with factors \(2\sqrt{2p}\) and \(10p\). Bounds for those quadratic
and terminal-time moduli are not established by (26)--(27). These are
explicit remaining interfaces; a finite-grid probability estimate is
not presented as the continuum, control-uniform insertion event.

The union over all same-layer sets of size at most \(p\) adds at most
\(\log(pL)+p\log n\) to the logarithm of the number of tests. Combining
(16)--(18) gives a finite-grid failure estimate *in terms of*
\(M,D,A,k,T\), the number of coordinate/form tests, and the terminal-time
grid. Their dependence on the physical parameters and deletion count
must still be supplied. Writing a tail as \(e^{-n^{7/10}}\) before
paying these quantities merely restores the original eventual-width gap.

The nonlinear closing inequality has the same issue. Define the remainder
coefficient \(A_R\) to include the original block expansion's entire
fixed numerical multiplier. Its integrated remainder is then bounded by
\[
A_JA_R\ell_n^k n^{\kappa}
\left[n^{-8/100}+u^2+Tn^{-48/100}
+A_{\rm src}n^{-1/2}\right],
\quad u\le n^{-1/25}.
\tag{19}
\]
Here \(A_J,A_R,A_{\rm src}\) must be actual raw propagator, remainder,
and omitted-source coefficients, with that multiplier already included
in \(A_R\); this display defines their required roles rather than importing
numerical values. There is no uncharged fixed multiplier when applying
the following sufficient gate to improve the remainder cap:
\[
4A_JA_R(1+T+A_{\rm src})\ell_n^k
\le\tfrac12 n^{1/25-\kappa}.
\tag{20}
\]
It is legitimate to solve (20) after proving the coefficient bounds. It
is not legitimate to absorb a depth-dependent logarithmic power into
\(\beta^{CL}\) without a numerical bound on that power and its onset.

## 5. Remaining local obligations

There are two useful structural directions, neither claimed proved by
this note. First, one should use the exact derivative formulas rather
than preserve the old \((1+M_n)^{C_L}\) bound. The forward recursions
through derivative order three contain only a fixed derivative order.
The exact Hessian contains one reference-carrier diagonal. A careful
third-order gradient expansion may therefore replace the depth-dependent
power by a fixed power of \(1+M_n\), with a \(\beta^{CL}\) coefficient.
The complete local Gaussian-map and nonlinear-remainder recurrences must
be written to certify this, including the reverse-source probe and the
adaptive residual terms.

Second, carrier differences should be estimated after division by \(S\).
The old absolute error \(C_pn^{-1/30}\) leads in the stop transfer to
\(\exp\{\eta C_pn^{-1/30}(1+1/S)\}\), which introduces an inverse-label
width. Scaling the learned mobility-coordinate variation and all backward
responses by \(S\), while leaving preactivations and forward features
unscaled, is a possible repair. The deleted forward controls retain
amplitude independent of \(S\), the reverse controls divided by \(S\)
are bounded by the joint budget, and the top prediction offset divided
by \(S\) is of order \(\operatorname{polylog}(n)/n\). These observations
do not by themselves prove the scaled insertion lemma. Its mixed
forward/backward remainders and projected common-cavity path radius must
be established in those norms.

To close a polynomial stochastic-width theorem, it is enough to supply
these raw local bounds with polynomial dependence on \(m,p,1/\lambda\)
and \(\beta^L\), a fixed numerical logarithmic exponent, and no inverse
power of \(S\); then (9), (12), and (16)--(20) expose all remaining
finite-width choices. The shrinking-contour argument must also verify
the complex metric constants. The source moment proof as currently
written does not supply these numerical facts, even after all five
authorized original notes are read.

The results actually established here are the absolute collision exponent
(4), the finite-order collision lemma (7), the confidence choice (9),
the common-cavity correction bound (12), and the explicit local-net
interfaces (16)--(20). Their distinction from the unproved local
coefficient ledger is essential.

## 6. Exact amplitude scaling and quantitative linear-map recurrences

The amplitude scaling mentioned above does give the following exact
identities and coefficient bounds. They are useful independently of a
completed finite-neuron probability proof. Write
\[
\bar u=(\Theta-\Theta_0)/S,\quad
\overline{\mathcal F}_a(\bar u,e)
=\mathcal F_a(\Theta_0+S\bar u,e)/S,\quad
\bar r_a=\overline{\mathcal F}_a/n-y_a/S,\quad \bar q_a=q_a/S.
\]
Because the original readout is zero,
\(\overline{\mathcal F}_a=\bar u_w^\top h_a^{(L)}\).
The exact retained equation (2) becomes
\[
\dot{\bar u}=-\frac2m\sum_a\bar r_a
\left[\nabla_{\bar u}\overline{\mathcal F}_a
+D_{\bar u}h_a^{(j-1)\top}\bar q_a\right].
\tag{21}
\]
In particular \(D_{\bar u}h=S D_\Theta h\), whereas
\(\nabla_{\bar u}\overline{\mathcal F}=\nabla_\Theta\mathcal F\).
The scaled backward fields are \(\bar k=k/S\), \(\bar\delta=\delta/S\).
Their gradient blocks are
\[
\nabla_{\bar u_A}\overline{\mathcal F}_a
=S\bar\delta_a^{(1)}v_a^\top,\quad
\nabla_{\bar u_{H^{(j)}}}\overline{\mathcal F}_a
=S\bar\delta_a^{(j)}h_a^{(j-1)\top}/\sqrt n,\quad
\nabla_{\bar u_w}\overline{\mathcal F}_a=h_a^{(L)}.
\tag{22}
\]
The residual used in (21) remains the forward residual; no reverse-source
term is added to it. On an allowed source contour,
\(2\int\bar\rho\,|dt|\le1\), where \(\bar\rho=\rho/S\), and
\(\bar\rho\le\lambda/8\). There is no inverse power of \(S\) in
these bounds.

Let
\[
M_n=\eta^{-1}\log(2n\mathcal B),\quad
A_n=b+sM_n,\quad B_n=sM_n,\quad
\tau_* =\max_j\tau_j,\quad f_* =\max_j f_j,
\quad\Gamma=\sqrt{\mathcal K},
\]
where the symbols on the right are the integrated source recurrences.
The stopped forward and scaled reverse controls have amplitudes at most
\(A_n,B_n\). Their time Lipschitz coefficients are explicit as well.
Using the source's \(V_j\) from its equation (9), set
\[
T_L=2sH_L+2tM_nV_L,\qquad
T_j=10sT_{j+1}+2s\tau_{j+1}^2H_j+2tM_nV_j\quad(j<L),
\]
\[
D_n=\max\{\lambda s\max_jV_j/4,\lambda\max_jT_j/8\}.
\tag{23}
\]
Both controls have Lipschitz constant at most \(D_n\sqrt n\) on each
real or straight complex contour segment. Indeed
\(\|\dot z^{(j)}\|_{2,n}\le2S^2\bar\rho V_j\), and differentiating
the scaled backward recursion gives
\(\|\dot{\bar\delta}^{(j)}\|_{2,n}\le\bar\rho T_j\).
The three terms in \(T_j\) propagate the upper derivative, change the
mixer, and change the gate. The gate multiplies the reference scaled
carrier bound \(M_n\) once; the recurrence is affine in \(M_n\).
The value \(D_n\) in (23) can therefore be substituted for \(D\) in
(16), without an unknown control-speed constant.

The scaled variational propagator is the original one: differentiating
(21) at zero sources gives the same negative-Gram generator and residual
Hessian as before scaling. More explicitly,
\(D^2_{\bar u}\overline{\mathcal F}=S D^2_\Theta\mathcal F\),
and \(\bar r=r/S\). Its bound, retaining the finite coefficient, is
\[
J_n=2\exp\{SA_*+(S^2D_*/\eta)\log(2n\mathcal B)\}
\le2e^{1/4}(2\mathcal B)^{1/4000}n^{1/4000}.
\tag{24}
\]
Here the full original source allowance gives
\(SA_*\le1/4\), \(S^2D_*/\eta\le1/4000\). The factor two permits
the short complex pieces already controlled by the deterministic contour
gate; on real forward paths it is unnecessary.

At a zero-source reference put
\[
B_a=D_{\bar u}\bar\delta_a^{(j+1)},\qquad
C_a=D_{\bar u}h_a^{(j-1)},\qquad
M_\delta=A_*+S D_*M_n.
\]
The augmented Hessian estimate gives
\(\|B_a\|\le M_\delta\), \(\|C_a\|\le S f_*\). Exact external
differentiation of (21) gives
\[
\bar P_a=-\frac2{mn}
\nabla_{\bar u}\overline{\mathcal F}_a\bar\delta_a^{(j+1)\top},
\quad\bar Q_a=-\frac2m\bar r_a B_a^\top,
\quad\bar T_a=-\frac2m\bar r_a C_a^\top.
\tag{25}
\]
The rank-one term has norm at most \(2\Gamma\tau_*/m\). Consequently,
for a contour of length at most \(T\), the Gaussian linear variation
of \(\bar u\), regarded as an operator on the concatenated omitted
roots, has norm at most
\[
V_n=\sqrt p\,J_n
\{A_n(2T\Gamma\tau_*+M_\delta)+S f_*B_n\}.
\tag{26}
\]
This follows by integration of (25), using the activity bound, then
Cauchy--Schwarz over the \(p\) root pairs. It does not use independence
of adaptively chosen controls.

All forward and backward linear-map bounds are now given by explicit
layer recurrences. With the source's \(P_j\), define
\[
Z_j=P_j(SV_n+\sqrt p A_n),\qquad H_j^{\rm lin}=sZ_j,
\]
\[
K_L^{\rm lin}=V_n,\qquad
D_j^{\rm lin}=sK_j^{\rm lin}+tM_nZ_j,\qquad
K_j^{\rm lin}=10D_{j+1}^{\rm lin}
+S\tau_{j+1}V_n+\sqrt p B_n\quad(j<L).
\tag{27}
\]
The added reverse-port term is included at every layer as an upper bound;
only one such port is present in an interior deletion. Matrix variations
cost \(S\tau_{j+1}V_n\), since the physical mixer variation is the
scaled Euclidean block divided by \(\sqrt n\). All symbols in
(23)--(27) are finite displayed formulas from authorized inputs. In
particular their dependence on \(p\) is through \(\sqrt p\), and none
contains \(1/S\). These recurrences replace the unspecified linear-map
constant in (17). The separate quadratic response maps, terminal-time
moduli, and nonlinear bootstrap still need their matching numerical audit.

The learned-column and learned-row small sources also retain their
amplitude factors after scaling. Direct integration of (22) gives
\[
\|W^{(j+1)}_{:,i}-x_i\|_2
\le S^2\tau_*A_n/\sqrt n,\qquad
\|W^{(j)\top}_{i,:}-y_i\|_2
\le S^2H_{\max}B_n/\sqrt n.
\]
Therefore the forward remainder and the scaled reverse remainder satisfy
\[
\|e_a-\sum_i x_i a_{a,i}\|_2
\le\frac{pS^2\tau_*A_n^2}{\sqrt n},\quad
\|\bar q_a-\sum_i y_i\bar b_{a,i}\|_2
\le\frac{pS^2H_{\max}B_n^2}{\sqrt n}.
\tag{28}
\]
At the top, the scaled prediction offset is at most
\(pM_nA_n/n\), and multiplies both terms in the square bracket of
(21). These are rigorous scaled identities and bounds. They remove an
inverse-label factor from the stated *inputs* of a local proof; they do
not yet assert its required normalized coordinate-error conclusion.

## 7. Input record

Read completely after authorization:
`UNBOUNDED_ACTIVATION_CANDIDATE.md`, `UNBOUNDED_INSERTION_CHECK.md`,
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`, and
`DEPTH_CAVITY_PROBABILITY_CHECK.md`, all in
`studies/dense_cutoff_population_rate_20261001/`. The earlier assigned
integrated and current-study inputs are those recorded in the fitting
note. Other linked older-study artifacts were not fetched. The new note
does not amend any source or claim a fresh independent review. No
experiment, Git mutation, or promotion was performed.

The five original-source SHA-256 hashes at completion, in the order just
listed, are:

- `e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713`
- `bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578`
- `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`
- `77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977`
- `e8ec625d60753186ee5a74e67458e1f048c7edc313dc0155de54cf193e307993`
