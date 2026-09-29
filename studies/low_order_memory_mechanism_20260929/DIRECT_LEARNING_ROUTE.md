# Direct terminal-function theorem for finite memory

This is a scoped theoretical route using only `MODEL.md`, `docs/notation.qmd`,
and the required mathematical/research skills. No experiments or other study
inputs were used. The results below are internally derived, not promoted book
material. They concern the closure itself, with every prescribed layer
trainable. A frozen-feature predictor appears only as an explicit comparator.

## Result and scope

For one nonzero training input, two hidden layers, arbitrary finite width, and
zero initial readout, every fixed memory order has an exact small-label
interpolation theorem. Its terminal test function has the expansion

\[
 f^{(q)}_\infty(x;y)
 =\frac{\kappa_x}{\alpha}y+\Gamma_x y^3+\Theta_x y^5
   +q^2\Psi_x\,y|y|^5+O_K(|y|^7).                         \tag{1}
\]

The remainder is uniform for test inputs in any fixed compact set \(K\).
The coefficients \(\Gamma_x\) and \(\Psi_x\) are explicit below. The three
coefficients through degree five are independent of fixed \(q\). At
\(x=2x_0\), both \(\Gamma_x\) and \(\Psi_x\) are nonzero for almost every
prescribed Gaussian initialization. Thus:

* actual hidden learning changes the terminal function at cubic order;
* memory order changes it first at degree six, with
  \(f^{(q)}_\infty-f^{(1)}_\infty=(q^2-1)\Psi_x y|y|^5+O_K(|y|^7)\);
* for every finite \(q\), the terminal predictor at \(2x_0\) is generically
  five times continuously differentiable, but not six times differentiable,
  as a function of the label at zero.

The last statement is an intrinsic footprint of the absolute-residual clock
and the constant initial history interval. It does not arise from lack of
smoothness of tanh. None of these are all-label or width-limit claims, and the
small-label remainder bounds are not uniform in \(q\).

We prove the one-sample path reduction first, then interpolation and its
Taylor coefficients, and finally verify that the displayed effects are
nonzero under the actual Gaussian law.

## Setup and exact path reduction

Take \(m=1,L=2,x_0\ne0,n\ge2\), \(\phi=\tanh\), and the initialization in
`MODEL.md`. The same derivation works at \(n=1\), but no width-one reduction
is made. Write \(M=W_2^0\), \(g=\|x_0\|^2/d>0\). Fix any integer
\(q\ge1\).

For a nonzero label let \(\sigma=\operatorname{sign}(y)\), \(z=|y|\), and,
on the interval before fitting, set

\[
 s(t)=2\int_0^t|r(v)|\,dv,
 \qquad \tau=1+s/2.
\]

This report's \(s\) is twice the activity increment \(\tau-1\).
Write the physical readout as \(w=\sigma\omega\), and let
\(\delta=\omega\odot\phi'(W_2h)\), where
\(h=\phi(W_1x_0/\sqrt d)\). Then all hidden states and \(\omega\)
follow the same path, independently of \(z\) and \(\sigma\):

\[
\begin{aligned}
 W_1'&=[\phi'(W_1x_0/\sqrt d)\odot W_2^T\delta]x_0^T/\sqrt d,\\
 \omega'&=\phi(W_2h),\\
 B_k'&=\tfrac12h-
 \frac{kB_k+\sum_{j<k}(2j+1)B_j}{s+2},\\
 C_k'&=-\tfrac12\delta-
 \frac{kC_k+\sum_{j<k}(2j+1)C_j}{s+2},\\
 W_2&=M-\frac{2}{n(1+s/2)}\sum_{k=0}^{q-1}(2k+1)C_kB_k^T.
                                                               \tag{2}
\end{aligned}
\]

Primes mean \(d/ds\). To check the signs, before interpolation
\(r=-\sigma|r|\) and physical backpropagation equals \(\sigma\delta\).
Hence \((r/|r|)\delta_{\rm physical}=-\delta\), in every moment and
first-layer equation. No division by a vanishing residual is used: (2) is
used only on the pre-fitting interval, and its local solution constructs
the physical solution below.

For a test input \(x\), let

\[
 F_x^{(q)}(s)=\frac{\omega(s)^T
 \phi(W_2(s)\phi(W_1(s)x/\sqrt d))}{n},
 \qquad F^{(q)}=F_{x_0}^{(q)}.
\]

Physical predictions are \(\sigma F_x^{(q)}(s(t))\) and the scalar clock
obeys

\[
 \dot s=2(z-F^{(q)}(s)),\qquad s(0)=0.                       \tag{3}
\]

All right sides of (2) are smooth in a neighborhood of the initial state
and \(s=0\), because \(s+2\ne0\). The finite-dimensional local ODE
existence and smooth-dependence theorem therefore supplies a unique smooth
path there. This theorem applies to a smooth vector field on an open set;
that open set can be chosen with \(|s|<1\), with no restriction on the
finite parameters other than lying in a sufficiently small neighborhood
of their initial values.

## Local interpolation is a complete physical-time statement

Define initial quantities, for arbitrary \(x\), by

\[
\begin{gathered}
 p_x=W_1^0x/\sqrt d,\quad h_x=\tanh p_x,\quad
 a_x=\tanh(Mh_x),\\
 E_x=\operatorname{diag}(\operatorname{sech}^2p_x),\quad
 D_x=\operatorname{diag}(\operatorname{sech}^2(Mh_x)).
\end{gathered}                                               \tag{4}
\]

An unsubscripted quantity is evaluated at \(x_0\), and put

\[
 \alpha=\|a\|^2/n,\quad \kappa_x=a^Ta_x/n,\quad
 g_x=x_0^Tx/d,\quad k_x=h^Th_x/n,\quad k=k_{x_0}.
                                                               \tag{5}
\]

At initialization all hidden velocities vanish and \(\omega'(0)=a\).
Consequently \(F(0)=0\) and \(F'(0)=\alpha\). Suppose \(a\ne0\).
Choose \(s_0>0\) so that the path exists on \([0,s_0]\) and
\(\alpha/2\le F'(s)\le2\alpha\) there. For every
\(0<z<F(s_0)\) there is a unique \(s_*(z)\in(0,s_0)\) with
\(F(s_*)=z\). Equation (3) has a solution for all physical times,
increasing toward \(s_*\). In fact, with \(v=s_*-s\), the mean value
theorem gives

\[
 -4\alpha v\le\dot v\le-\alpha v,
 \qquad
 s_*e^{-4\alpha t}\le v(t)\le s_*e^{-\alpha t}.              \tag{6}
\]

It stays below \(s_*\) at every finite time, so the reduction is valid
throughout. Every state converges to the finite value of its smooth path
at \(s_*\), and the training residual converges to zero exponentially.
More precisely,

\[
 \lim_{t\to\infty}-\frac1t\log |r(t)|=2F'(s_*).
                                                               \tag{7}
\]

For (7), \(\dot v/v=-2(F(s_*)-F(s))/v\to-2F'(s_*)\);
integration gives the logarithmic rate, and
\(|r|/v\to F'(s_*)>0\). The label zero leaves the initialized network
stationary. The original physical vector field is locally Lipschitz
because it is built from smooth functions and \(|r|\), so this
constructed solution is also its unique solution.

Under the prescribed Gaussian law, \(a\ne0\) almost surely. Indeed,
\(p\) has independent nondegenerate Gaussian coordinates since \(g>0\),
so \(h\ne0\) almost surely. Conditional on \(h\ne0\), the coordinates
of \(Mh\) are independent Gaussians of variance \(\|h\|^2/n>0\).
Therefore \(Mh\), and hence \(a\), is nonzero almost surely.

This is a local-label theorem at every finite width. It proves convergence
in physical time, not merely the existence of a fitting parameter vector.

## Explicit cubic learned-function correction

Set

\[
 v=Da,\qquad U=gE^2M^Tv,\qquad
 T_x=D_x\{g_xME_xEM^Tv+k_xv\},\qquad T=T_{x_0}.
                                                               \tag{8}
\]

The leading path coefficients, for every fixed \(q\), are

\[
\begin{aligned}
 W_1(s)&=W_1^0+\frac{s^2}{2}(EM^Tv)x_0^T/\sqrt d+O(s^4),\\
 W_2(s)&=M+\frac{s^2}{2n}vh^T+O(s^4),\\
 h_{x_0}^{(1)}(s)&=h+\frac{s^2}{2}U+O(s^4),\\
 h_x^{(2)}(s)&=a_x+\frac{s^2}{2}T_x+O_K(s^4),\\
 \omega(s)&=sa+\frac{s^3}{6}T+O(s^5).
                                                               \tag{9}
\end{aligned}
\]

To derive the first two formulas, \(\delta(s)=sv+O(s^3)\).
Integrating the first equation of (2) gives the first formula. Also
\(C_0=-s^2v/4+O(s^4)\) and
\(B_0=(1+s/2)h+O(s^3)\), while every higher-mode product
\(C_kB_k^T=O(s^5)\). Substituting into the reconstruction gives the
second formula. Applying the chain rule to the test preactivation gives

\[
 W_2(s)h_x^{(1)}(s)
 =Mh_x+\frac{s^2}{2}\{g_xME_xEM^Tv+k_xv\}+O_K(s^4),
\]

which gives the fourth formula and, by integrating \(\omega'=h_{x_0}^{(2)}\),
the fifth. The absence of a cubic hidden-state coefficient is also checked
in the next section, where one further parity order is needed.

Consequently

\[
 F_x(s)=\kappa_xs+c_xs^3+O_K(s^5),\quad
 c_x=\frac{T^Ta_x}{6n}+\frac{a^TT_x}{2n},                   \tag{10}
\]

and

\[
 F(s)=\alpha s+\beta s^3+O(s^5),\qquad
 \beta=\frac{2}{3n}\left[g\|EM^Tv\|^2+k\|v\|^2\right]>0.
                                                               \tag{11}
\]

The strict inequality uses \(g>0,k>0,v\ne0\); in particular, the
trained middle layer contributes the strictly positive second term.
The first term measures the first-layer contribution. It too is positive:
if \(M^Tv=0\), then \((Mh)^Tv=0\), whereas
\(\sum_i(Mh)_i\tanh((Mh)_i)\operatorname{sech}^2((Mh)_i)>0\)
when \(Mh\ne0\). The diagonal matrix \(E\) is invertible.

Inverting (11) at zero gives

\[
 s_*(z)=z/\alpha-\beta z^3/\alpha^4+O(z^5).
\]

Thus

\[
 f_\infty^{(q)}(x;y)=\frac{\kappa_x}{\alpha}y+
 \Gamma_xy^3+O_K(|y|^5),\qquad
 \Gamma_x=\frac{c_x}{\alpha^3}-\frac{\kappa_x\beta}{\alpha^4}.
                                                               \tag{12}
\]

With the initial hidden features frozen, the same readout equation would
give exactly \(y\kappa_x/\alpha\). Therefore a nonzero \(\Gamma_x\)
is a genuine hidden-learning contribution, after matching the final
training fit. It is not just a speed change along training predictions.

Uniformity on a compact test set follows because the state path lies in a
fixed finite parameter neighborhood, and all derivatives through the
required order of \(\tanh(W_2\tanh(W_1x/\sqrt d))\) are continuous
and bounded on the product of that neighborhood with the compact set.

## First memory-order effect and the sixth-order loss of smoothness

The constant prefix in the moments is essential for this calculation.
For \(k\ge1\), its contribution cancels the contribution of a constant
continuation. Using the integral interpretation in `MODEL.md`,

\[
 B_k(s)=\frac12\int_0^s
  [h_{x_0}^{(1)}(u)-h]\,
  p_k\left(\frac{2+u}{2+s}\right)du,
 \qquad
 C_k(s)=-\frac12\int_0^s
  \delta(u)p_k\left(\frac{2+u}{2+s}\right)du.                \tag{13}
\]

Here \(p_k(1)=1\), and for each fixed \(k\) its value in this integral
is \(1+O(s)\). Equations (9) therefore imply

\[
 B_k=\frac{s^3}{12}U+O(s^4),\quad
 C_k=-\frac{s^2}{4}v+O(s^3)\quad(k\ge1),\qquad
 \frac{B_0}{1+s/2}=h+\frac{s^3}{12}U+O(s^4).              \tag{14}
\]

To locate the first *odd* coefficient of \(W_2\), one must also exclude
an order-five term in \(C_0\). The following Taylor bootstrap does so:

1. Zero readout gives vanishing first hidden velocities and
   \(\omega=sa+O(s^3)\), \(\delta=sv+O(s^3)\).
2. The \(k=0\) reconstruction uses \(B_0/(1+s/2)=h+O(s^3)\);
   higher-mode products begin at order five. Hence \(W_2\) has no
   coefficient of order three. Integrating the first-layer equation
   also gives no coefficient of order three in \(W_1\).
3. The top features consequently have no coefficient of order three,
   so \(\omega\) has no coefficient of order four. Multiplying it by
   the top activation derivative shows that \(\delta\) has no
   coefficient of order four. Therefore
   \(C_0=C_{0,2}s^2+C_{0,4}s^4+O(s^6)\), with no order-five term.
4. The first-layer velocity likewise has only orders one and three
   through order four. Thus \(W_1\), and its first-layer features,
   have only orders zero, two and four through order five.

The order-five coefficient of \(W_2\) is therefore entirely the
\(C_{0,2}\) times the order-three moving-average feature in (14), plus
the higher-mode products displayed there. Since
\(\sum_{k=0}^{q-1}(2k+1)=q^2\),

\[
 W_2(s)=M+s^2M_2+s^4M_4+
 \frac{q^2s^5}{24n}vU^T+O(s^6).                           \tag{15}
\]

The coefficients \(M_2,M_4\), and all lower-order first-layer and
readout coefficients, are independent of fixed \(q\). For completeness,
extra reconstructed forcing of order five in \(W_2\) first affects
the top features at order five, \(\omega\) at order six,
\(\delta\) at order six, and the integrated first-layer weights and
\(C_0\) at order seven. Thus it cannot feed back and modify the
coefficient in (15). This also justifies the stated common coefficients.

The order-five coefficient of the top test feature is
\(q^2D_xv(U^Th_x)/(24n)\), while integrating its training value
gives the order-six readout coefficient
\(q^2Dv(U^Th)/(144n)\). Multiplying readout and test features yields

\[
 F_x^{(q)}(s)=\kappa_xs+c_xs^3+e_xs^5+q^2\zeta_xs^6+O_K(s^7),
                                                               \tag{16}
\]

where \(e_x\) is common to all fixed \(q\), and

\[
 \zeta_x=
 \frac{(a_x^TDv)(U^Th)}{144n^2}
 +\frac{(a^TD_xv)(U^Th_x)}{24n^2}.                         \tag{17}
\]

The scalar inverse in the interpolation theorem exists smoothly on a
signed neighborhood of zero because \(F'(0)=\alpha>0\). Inverting
(16), writing \(e=e_{x_0}\), gives

\[
\begin{aligned}
 s_*(z)={}&\frac z\alpha-\frac\beta{\alpha^4}z^3
 +\left(\frac{3\beta^2}{\alpha^7}-\frac e{\alpha^6}\right)z^5
 -\frac{q^2\zeta_{x_0}}{\alpha^7}z^6+O(z^7),\\
 \Theta_x={}&\kappa_x\left(\frac{3\beta^2}{\alpha^7}-\frac e{\alpha^6}\right)
             -\frac{3c_x\beta}{\alpha^6}+\frac{e_x}{\alpha^5},\\
 \Psi_x={}&\frac1{\alpha^6}
             \left(\zeta_x-\frac{\kappa_x}{\alpha}\zeta_{x_0}\right).
                                                               \tag{18}
\end{aligned}
\]

Substituting \(z=|y|\) and multiplying predictions by
\(\operatorname{sign}(y)\) proves (1). The fifth coefficient is
well-defined by \(e_x=(\partial_s^5F_x^{(1)})(0)/5!\);
its explicit expanded polynomial is unnecessary for the cubic and
memory-order conclusions.

Each side of the label-zero map is smooth, and its Taylor jets have no
even terms of degrees two or four. The term
\(q^2\Psi_x\operatorname{sign}(y)|y|^6\) therefore gives matching
derivatives through order five and unequal one-sided sixth derivatives
\(\pm6!q^2\Psi_x\), whenever \(\Psi_x\ne0\).
This establishes the claimed differentiability exactly. It is not an
inference about differentiability from a bare remainder bound.

## The two effects are generically nonzero under Gaussian initialization

Here “generic” means outside a set of zero probability for the full
prescribed finite-dimensional Gaussian initialization, not only on a
special invariant subspace. We establish nonvanishing of the explicit
analytic coefficient functions by a deterministic witness; this witness
is not substituted for the random model in the theorem.

Fix \(x=2x_0\). In a witness initialization choose
\(p=t e_1\), \(M=e_1e_1^T\), with \(t>0\). This is realizable by
\(W_1^0=t\sqrt d\,e_1x_0^T/\|x_0\|^2\). Only the first coordinate is
active in the witness. In this paragraph use scalar letters for that
coordinate, so \(h=\tanh t\), \(a=\tanh h\),
\(E=\operatorname{sech}^2t\), \(D=\operatorname{sech}^2h\).
For a test input \(\lambda x_0\), the quantities in (8) reduce to

\[
 T=D^2a(gE^2+h^2/n),\qquad
 T_\lambda=D_\lambda Da
       (\lambda gE_\lambda E+hh_\lambda/n).
\]

The numerator of the cubic correction satisfies

\[
 c_\lambda-\frac{\kappa_\lambda}{\alpha}\beta
 =\frac{a}{2n}\left(T_\lambda-\frac{a_\lambda}{a}T\right).
                                                               \tag{19}
\]

Expanding \(\tanh t=t-t^3/3+O(t^5)\) gives

\[
\begin{aligned}
 a_\lambda&=\lambda t-\tfrac23\lambda^3t^3+O(t^5),\\
 T&=gt+(1/n-14g/3)t^3+O(t^5),\\
 T_\lambda&=\lambda gt+
     [\lambda/n-\lambda g(2\lambda^2+8/3)]t^3+O(t^5),\\
 T_\lambda-(a_\lambda/a)T
    &=\tfrac43\lambda g(1-\lambda^2)t^3+O(t^5).
\end{aligned}
\]

At \(\lambda=2\), (19) is
\(-4gt^4/n+O(t^6)\), which is nonzero for sufficiently small \(t>0\).
Equivalently, the everywhere analytic numerator
\(\alpha c_{2x_0}-\kappa_{2x_0}\beta\) is nonzero at this witness.

For the memory coefficient, (17) instead gives the exact scalar identity

\[
 \zeta_\lambda-
       \frac{\kappa_\lambda}{\alpha}\zeta_{x_0}
 =\frac{UaD}{24n^2}
      [aD_\lambda h_\lambda-a_\lambda Dh].                 \tag{20}
\]

All factors outside the bracket are positive. For \(z>0\),

\[
 \frac{\tanh z}{z\operatorname{sech}^2z}
   =\frac{\sinh(2z)}{2z}
\]

is strictly increasing: its derivative has the sign of
\(2z\cosh(2z)-\sinh(2z)\), which vanishes at zero and has derivative
\(4z\sinh(2z)>0\). Since \(h_2>h>0\), the bracket in (20) is
strictly negative at \(\lambda=2\). Thus the analytic numerator
\(\alpha\zeta_{2x_0}-\kappa_{2x_0}\zeta_{x_0}\) is also not
identically zero.

We use the elementary fact that a nonzero real analytic function on
\(\mathbb R^N\) has a Lebesgue-null zero set. One proof is induction
on \(N\): select a last-coordinate value \(t_0\) for which the
restriction to the first \(N-1\) coordinates is not identically zero.
By induction its zero set is null. Outside that exceptional set, the
one-dimensional analytic slice is not identically zero, hence has a
discrete, measure-zero zero set. Fubini's theorem on bounded boxes
finishes the proof; for \(N=1\), isolated zeros follow from the first
nonzero Taylor coefficient at a zero. The identity theorem ensures a
nonzero analytic function cannot have an accumulation of zeros on an
interval. The Gaussian law on \((W_1^0,M)\) has a Lebesgue density with
strictly positive variances in every coordinate, so both zero sets have
Gaussian probability zero.

It follows that, almost surely, \(\Gamma_{2x_0}\ne0\) and
\(\Psi_{2x_0}\ne0\). On the same probability-one event, each finite
\(q\) has its own sufficiently small label neighborhood satisfying
the theorem. Any finite collection of memory orders can use the minimum
of those neighborhoods.

The same conclusion holds at a genuine same-radius, nonparallel test
point. More precisely, fix any \(x\) with
\(\lambda=x_0^Tx/\|x_0\|^2\in(0,1)\). In the witness above,
\(p_x=\lambda t e_1\) and \(g_x=\lambda g\), even if \(x\) has a
component perpendicular to \(x_0\). Thus every witness calculation in
(19)--(20) still applies. The cubic bracket has leading coefficient
\(\tfrac43\lambda g(1-\lambda^2)t^3\ne0\); the memory bracket is
strictly positive because \(0<h_\lambda<h\) and the displayed
hyperbolic-sine ratio is strictly increasing. Both analytic numerators
are therefore nonzero functions for this fixed test input, and the same
zero-set argument proves \(\Gamma_x\ne0\) and \(\Psi_x\ne0\) almost
surely. In particular, when \(d\ge2\), choose a unit vector \(e\)
perpendicular to \(x_0\) and set

\[
 x=\tfrac12x_0+\tfrac{\sqrt3}{2}\|x_0\|e.
\]

Then \(\|x\|=\|x_0\|\), its angle from \(x_0\) is \(\pi/3\), and
both the cubic hidden-learning effect and the sixth-order memory effect
are almost surely nonzero there. The probability-one statement concerns
each test point fixed before initialization; no simultaneous assertion
over an uncountable set of test points is needed.

## What is proved, and what remains open

Proved for the canonical finite-width closure: the common one-sample
parameter path, complete small-label convergence in physical time,
strictly positive cubic acceleration of the training prediction,
uniform-on-compact terminal test-function expansion, almost-sure cubic
departure from the frozen-feature terminal function, the explicit
sixth-order memory-order difference, and generic failure of sixth label
differentiability at zero.

This route does not prove interpolation for arbitrary label size, global
positivity of \(F'(s)\), uniformity in width or memory order, any population
limit, or an implicit variational characterization of the endpoint.

The direct obstruction to an elementary global monotonicity proof is already
visible at \(q=1\). Put \(A=-2C_0\), \(H=B_0/\tau\),
\(W_2=M+AH^T/n\), and retain \(\delta=\omega\odot\phi'(W_2h)\).
Then \(A'=\delta\), \(H'=(h-H)/(s+2)\), and differentiating the
training prediction yields

\[
\begin{aligned}
 F'(s)={}&\frac{\|h^{(2)}\|^2}{n}
 +\frac{g\|\phi'(W_1x_0/\sqrt d)\odot W_2^T\delta\|^2}{n}\\
 &+\frac{\|\delta\|^2 H^Th}{n^2}
 +\frac{(\delta^TA)(\|h\|^2-H^Th)}{n^2(s+2)}.             \tag{21}
\end{aligned}
\]

The last two terms involve current/history alignment and have no sign from
the model definition alone. No reachable-state inequality controlling
them was proved here. Their formal indefiniteness is an obstruction to
this proof route, not a counterexample to all-label interpolation.

The local theorem avoids that unproved global step while retaining trainable
hidden layers, the exact reused matrix and transpose, Gaussian width, the
prescribed initial history, and the actual finite-memory update.
