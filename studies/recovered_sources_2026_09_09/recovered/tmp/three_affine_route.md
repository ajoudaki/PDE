# Three-sample physical control: a rigorous large-gain route

This note does **not** establish the originally proposed unit-slope family
`1+z+e arctan(z)`. It establishes a different, permitted activation-design
route if a delta-dependent affine gain is allowed:

\[
\phi_{a,e}(z)=a(1+z)+e\arctan z,\qquad a=a_\delta\ge1,
\quad 0\le e\le1.
\]

The raw metric, architecture, initialization, and physical loss flow remain
exactly those in the two-sample proof, with three samples. In particular
the population initial readout is zero. The estimates below work for the
actual loss flow and for the usual auxiliary gates clipping only the
nonlinear backward term. No clipped energy identity is assumed.

## 1. A quantitative augmented-input Gram bound

Let \(\Gamma\) be the three-sample input correlation matrix, and put
\(d_{12}=1-\rho_{12}\), \(d_{13}=1-\rho_{13}\),
\(d_{23}=1-\rho_{23}\). Direct determinant expansion gives

\[
\det(\Gamma+\mathbf1\mathbf1^T)
=2\det\Gamma+2d_{12}d_{13}d_{23}\ge2\delta^3.
\]

The augmented Gram is positive semidefinite and has trace 6. If its
eigenvalues are \(\lambda_1\ge\lambda_2\ge\lambda_3\), then
\(\lambda_1\lambda_2\le9\), whence

\[
\Gamma+\mathbf1\mathbf1^T\succeq mI_3,
\qquad m=2\delta^3/9.                                      \tag{1}
\]

Feasible triples necessarily have \(\delta\le3/2\):
\(0\le\|u_1+u_2+u_3\|^2\le9-6\delta\), where
\(u_a=x_a/\sqrt d\). Thus \(m\le3/4\). For larger delta the
three-sample quantifier is empty.

## 2. Initial feature singular value

All comparisons use a common canonical generated action space containing
the initial programs for both activations. The initialized actions have
operator norm at most 10. Write \(F_3:\mathbb R^3\to H_3\)
for the matrix whose columns are the three top features.

For the affine activation \(a(1+z)\), initial Gaussian propagation gives

\[
a^{-6}F_{3,\mathrm{aff}}^*F_{3,\mathrm{aff}}
=\Gamma+(1+a^{-2}+a^{-4})\mathbf1\mathbf1^T\succeq mI_3.
                                                               \tag{2}
\]

At initialization, \(\|h_e^1-h_0^1\|\le\pi/2\). Successive
use of the same initialized actions and \(|e\arctan z|\le\pi/2\)
gives, sample by sample,

\[
\|h_e^2-h_0^2\|\le(11\pi/2)a,
\qquad
\|h_e^3-h_0^3\|\le(111\pi/2)a^2.
\]

Consequently

\[
\sigma_{\min}(a^{-3}F_3(0))
\ge\sqrt m-\frac{111\pi\sqrt3}{2a}.
\]

For \(a\ge700/\sqrt m\), this is at least \(\sqrt m/2\).
This argument uses no nonlinear covariance eigenvalue theorem.

## 3. Uniform bounds on a small raw ball

Use the full raw Hilbert displacement norm

\[
E(\Theta)^2=d\|w-w_0\|_{L^2(\mathbb R^d)}^2
+\|A-A_0\|_{\rm HS}^2+\|B-B_0\|_{\rm HS}^2+\|C\|_2^2.
\]

Take

\[
R=\sqrt m/20000<1,
\qquad a=10^6/\sqrt m.                                  \tag{3}
\]

On \(E\le R\), each first preactivation norm is at most 2,
and both current actions have norm at most 11. Put
\(U_\ell=a^{-\ell}h^\ell\). For either the actual activation or
its affine comparator,

\[
\|U_1\|\le5,\qquad \|U_2\|\le58,\qquad \|U_3\|\le641.
                                                               \tag{4}
\]

Indeed the normalized recursion is

\[
U_1=1+z^1+(e/a)\arctan z^1,
\]
\[
U_2=a^{-1}+AU_1+(e/a^2)\arctan(aAU_1),
\]
\[
U_3=a^{-2}+BU_2+(e/a^3)\arctan(a^2BU_2).
\]

Its derivatives in the normalized preactivation argument are bounded
by 2. Comparing a state to its initialization with the same activation,
and denoting its raw displacement by E, gives

\[
\|U_1-U_1(0)\|\le2E,
\]
\[
\|U_2-U_2(0)\|\le2(5E+10\cdot2E)=50E,
\]
\[
\|U_3-U_3(0)\|\le2(58E+10\cdot50E)=1116E.
                                                               \tag{5}
\]

Thus, throughout this ball,

\[
\sigma_{\min}(F_3)
\ge a^3(\sqrt m/2-1116\sqrt3R)
\ge a^3\sqrt m/4.
\]

In particular the actual readout kernel obeys

\[
F_3^*F_3\succeq a^6mI_3/16.                              \tag{6}
\]

## 4. The clipped physical flow also dissipates loss

Let \(g(z)=(1+z^2)^{-1}\), and let \(\tau_N\) be an odd,
1-Lipschitz truncation with \(|\tau_N(q)|\le|q|\). At each backward
gate replace the actual gate \((a+eg(z))q\) by

\[
aq+eg(z)\tau_N(q).
\]

Each gate has L2 output norm at most \(2a\|q\|\), uniformly in N.
In particular both actual and clipped backward fields satisfy

\[
\|b^3_a\|\le2a\|C\|,
\quad \|b^2_a\|\le44a^2\|C\|,
\quad \|b^1_a\|\le968a^3\|C\|.                           \tag{7}
\]

Let \(D_h\) be the actual hidden loss gradient, and
\(\widehat D_h\) the hidden descent direction used by the clipped
system. Cauchy--Schwarz over the three samples, (4), and (7) give
blockwise bounds with coefficients
\(\sqrt3(968,220,116)\). Since
\(968^2+220^2+116^2<10^6\),

\[
\|D_h\|_{\rm raw},\ \|\widehat D_h\|_{\rm raw}
\le2000a^3\|C\|\|r\|_{\mathbb R^3}.                    \tag{8}
\]

The readout equation is unchanged: \(\dot C=-F_3r\).
The exact chain rule for the actual loss along the clipped direction is

\[
\dot L=-\|F_3r\|^2-\langle D_h,\widehat D_h\rangle.
\]

The second term is not assigned a sign. Instead, (6), (8), and
\(\|C\|\le R\) give

\[
\dot L\le-a^6\left(m/16-4\cdot10^6R^2\right)\|r\|^2
\le-\lambda\|r\|^2,
\qquad \lambda=a^6m/32.                                 \tag{9}
\]

Here \(4\cdot10^6R^2=m/100\), which is less than
\(m/16-m/32\). This is a cap-uniform dissipation estimate derived
without a clipped gradient or radial identity.

The readout direction has norm at most
\(641\sqrt3a^3\|r\|\). Combining it with (8) gives the useful
loose uniform estimate

\[
\|\dot\Theta\|_{\rm raw}\le4000a^3\|r\|.               \tag{10}
\]

Since \(r(0)=-y\), \(\|r(0)\|=\sqrt3\). Equation (9) implies

\[
\|r(t)\|\le\sqrt3e^{-\lambda t},
\qquad
\int_0^\infty\|r(t)\|dt\le\tau_0:=32\sqrt3/(a^6m).
                                                               \tag{11}
\]

Consequently every clipped prefix that stays in the ball satisfies

\[
E(t)\le\int_0^t\|\dot\Theta\|dt
\le128000\sqrt3/(a^3m)<R/2,                              \tag{12}
\]

with the choice (3). The strict inequality is immediate after inserting
\(a^3=10^{18}m^{-3/2}\): its left side is
\(128000\sqrt3\,10^{-18}\sqrt m\), whereas
\(R/2=\sqrt m/40000\).

For every fixed finite cap the vector field is locally Lipschitz in the
raw Hilbert state: the only nonlinear backward product is
\(g(z)\tau_N(q)\), whose L2 Lipschitz constant on pairs is bounded
by \(N\|g'\|_\infty\) in z and 1 in q; forward activations are
Lipschitz, and all other operations are bounded bilinear actions.
Picard contraction gives local existence. The strict stopped estimate
(12) prevents ball exit. On this ball (10) gives a bounded velocity,
and the fixed-cap local Lipschitz bound gives ordinary continuation.
Hence every fixed-cap physical flow exists globally and satisfies
(6), (9)--(12), uniformly in its cap.

If an uncut strong flow is constructed as a strong limit of these
systems, these estimates pass to it. For that flow the usual exact
loss energy identity also holds, and (6) alone already provides the
stronger uncut gradient lower bound. The uncut construction and
response-tail estimates are a separate remaining analytic obligation;
they are not used to establish the preceding cap-uniform bounds.

## 5. Bounded affine reference for every residual-clock prefix

For any clipped system define residual time
\(s(t)=\int_0^t\|r(v)\|dv\). Where the residual is nonzero, its
normalized coefficients \(\gamma_a=r_a/\|r\|\) satisfy
\(\|\gamma\|_2=1\), and its clock duration is at most \(\tau_0\).
After exact fitting extend by zero coefficients if needed.

More generally, let \(\gamma:[0,\tau_0]\to\mathbb R^3\) be any
measurable coefficient curve with \(\|\gamma(s)\|_2\le1\).
Consider the affine controlled equation

\[
\Theta'=-\sum_{a=1}^3\gamma_a(s)\nabla f_{a,\mathrm{aff}}(\Theta),
\qquad \phi_{\mathrm{aff}}(z)=a(1+z).
\]

Its vector field is polynomial in the raw state and measurable in s,
with uniform bounded-ball Lipschitz constants. The integral equation
has local contraction solutions. On the same ball (10), with
\(\|r\|\) replaced by \(\|\gamma\|\le1\), bounds its velocity by
\(4000a^3\). Thus all its prefixes satisfy

\[
E(s)\le4000a^3\tau_0=128000\sqrt3/(a^3m)<R/2.
\]

This proves a single, cap-independent affine primal bound on every
controlled residual-clock prefix. It needs no symmetry, loss decrease,
or scalar radial lemma. Piecewise-constant Euler coefficients give the
same stopped bound directly, including prefixes arising from a
population Euler response construction.

Therefore a generalized three-sample response lemma may take fixed
arguments depending only on \(\delta\): the gain a, the above
physical/clock bounds, and the coefficient norm bound
\(\|\gamma\|_1\le\sqrt3\). It may then choose a sufficiently small
\(e_\delta\le1\). This note does not itself prove that response lemma.

## 6. Uniform nonaffinity from proximity to initialization

At initialization every preactivation is centered Gaussian. Its
standard deviation is at least 1 for \(a\ge1,e\ge0\): the first is
1, and the Gaussian covariance recursion together with
\(|az+e\arctan z|\ge a|z|\) gives larger variances thereafter.

For \(G\sim N(0,1)\), let

\[
\eta_*:=\inf_{\sigma\ge1}
\inf_{\alpha,\beta}\mathbb E[\arctan(\sigma G)-\alpha-\beta\sigma G]^2.
\]

This is strictly positive. For finite positive sigma, a zero error
would make arctangent affine everywhere, by Gaussian full support and
continuity. Its value is continuous in sigma. Symmetry gives mean zero,
and writing the regression in G coordinates gives

\[
\mathcal R(\sigma G)
=\mathbb E\arctan(\sigma G)^2
-(\mathbb E[G\arctan(\sigma G)])^2.
\]

Dominated convergence (with the integrable dominator \(\pi|G|/2\)
for the second term) gives the strictly positive limit
\(\pi^2(1-2/\pi)/4\) as \(\sigma\to\infty\). Compactness of a
large finite sigma interval then proves the claim.

The preactivation version of (5) gives

\[
\|z^1-z^1(0)\|\le E,
\quad \|z^2-z^2(0)\|\le25aE,
\quad \|z^3-z^3(0)\|\le558a^2E.
\]

Combining with (12), the worst bound is
\(71424000\sqrt3/(am)\). One can enlarge a, while keeping R fixed,
until this is less than

\[
t_*:=\min\{1/2,\sqrt{\eta_*}/[2(1+\pi)]\}.
\]

All previous requirements are lower bounds on a, so this enlargement
preserves every estimate. The L2 regression stability argument in the
audited proof, applied with initial standard deviation lower bound 1,
then gives \(\mathcal R(z_a^\ell(t))\ge\eta_*/4\) for every layer,
sample, time, and finite cap, and for the strong uncut limit. Finally

\[
\inf_{\alpha,\beta}\mathbb E[\phi_{a,e}(Z)-\alpha-\beta Z]^2
=e^2\mathcal R(Z).
\]

Thus every \(e>0\) selected by the response construction has a global
strict activation-nonaffinity margin. No Gaussianity at trained times
is asserted or needed here.

## 7. Exact remaining limitations

1. A delta-dependent affine gain changes the originally named family.
   These lemmas do not prove the unit-slope family can be used globally.
2. The local fixed-program/response, cap-removal, uniqueness, and finite
   width/raw-GD bridges still need to be verified for three samples and
   the controlled residual clock. Section 5 discharges the needed bounded
   affine-reference premise and Section 4 supplies a cap-independent
   global physical bootstrap before uncut existence.
3. Positive hidden initial accelerations and a changing total kernel
   require an independent three-sample calculation. They are not implied
   merely by the Gram lower bound or the activation nonaffinity margin.

No numerical experiment was used.
