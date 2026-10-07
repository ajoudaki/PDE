# What changing time can save, and what would require a new construction

2026-10-05. Bounded route assessment accompanying the theorem in RESULT.md.
Statements below are labelled as identities, consequences, or open routes.
They are not new all-time compression guarantees.

## 1. Where the present logarithmic power comes from

For a fixed task put ell=log(en), only in this section. The historical
source proof uses a physical horizon T=O(ell), a complex time radius
O(ell^-1/2), and an angular radius O(ell^-1/2). Approximation to a fixed
inverse power of n adds a factor O(ell) to polynomial degrees.

The time degree is therefore O(ell^(5/2)). Spherical degree is
O(ell^(3/2)), and the sum of spherical harmonic dimensions through that
degree is O(ell^(3(d-1)/2)). Multiplying and then retaining quadratic
matrices gives

\[
 R=O_{\mathrm{task}}((\log n)^{3d/2+1}),\qquad
 \operatorname{storage}=O_{\mathrm{task}}((\log n)^{3d+2}).
\]

The historical source uses a joint weighted-degree cutoff rather than a
literal full tensor product. That improves constants, including factorial
dimension factors, but gives these same logarithmic powers.

The new theorem in RESULT.md proves that the angular source factor cannot
be removed by a cleverer fixed linear space: with high probability at
least c_d(log n)^(3(d-1)/2) directions are necessary already at t=0.
The proof allows the space to depend jointly on all initialized neurons.
It is not a Monte Carlo lower bound or an argument based solely on the
single largest neuron.

Even eliminating all time cost would leave the current quadratic storage
at least of order (log n)^(3d-3). This limits any improvement within that
architecture to at most five log powers, regardless of d. It does not
claim those five powers are attainable.

## 2. Legendre versus Chebyshev and a new clock

**Exact basis fact.** The first p+1 Legendre polynomials and the first
p+1 Chebyshev polynomials both form bases of degree-at-most-p polynomials
on a fixed interval. For a vector-valued polynomial, the two coefficient
lists differ by an invertible scalar matrix. Their coefficient spans in
neuron space are identical. Thus an exact change of basis cannot change
the required source rank. Projection rules can of course select different
approximants, and stability constants may differ.

**Potentially substantive change.** Using

\[
 \tau(t)=\int_0^t\rho(s)\,ds,\qquad
 \rho(t)=\left(\frac1m\sum_a(f_n(t,v_a)-y_a)^2\right)^{1/2},
\]

changes the function being approximated by temporal polynomials. Under
the inherited exponential fitting bound, tau has a finite endpoint and
its total length has no log n factor. This can improve temporal degrees
if sufficiently strong analytic control in tau is established. Using
tau in a source proof alone need not alter the autonomous compressed
runtime; it would change the source space constructed at preprocessing.
The final comparison would still have to use the same physical t.

**What is not yet established.** Real bounded path length does not imply
a holomorphic neighborhood of the closed tau interval with width
independent of n. Away from rho=0 the real change of variables is valid,
but the complex continuation of sqrt(sum r_a^2/m), its complex zeros,
and the inverse map require estimates. Endpoint regularity can also be
an issue. For example, the deterministic analytic curve
(e^-t,e^(-3t/2)) becomes (1-tau,(1-tau)^(3/2)) under
tau=1-e^-t. This example only demonstrates a reparameterization issue;
it is not a counterexample for the canonical trained network.

The same issue appears in the formal residual linearization near a
fitted endpoint: distinct decay rates can turn into noninteger powers
of the remaining activity. Orthogonal initialization makes the initial
limiting training Gram diagonal with a common eigenvalue, but does not
by itself prove equality of the final nonlinear decay rates or analytic
regularity in the activity clock.

Piecewise Legendre approximants on physical or activity-time panels are
an alternative. They avoid requiring one analytic extension through the
endpoint, at the price of counting panels and controlling the final tail.
No improved global panel-count theorem is established in this note.

**Firm conclusion.** Even a perfect resolution of all these temporal
issues cannot evade RESULT.md's initialization obstruction while retaining
the same full-feature source contract and quadratic storage.

## 3. Why tanh's angular cost is not just a worst-neuron artefact

The proof in RESULT.md gives the initialized covariance eigenvalue bound

\[
 \nu_k\ge c_d k^{-2(d+1)/3}\exp(-C_d k^{2/3})
                         \quad(k\text{ odd}).
\]

This is a lower bound, not a claim of a matched asymptotic formula. Its
proof balances two precisely controlled exponents: the Gaussian Hermite
coefficient costs exp(-C sqrt(p)), whereas turning degree p into spherical
degree k costs exp(-C_d k^2/p). Taking p about k^(4/3) makes both costs
exp(-C_d k^(2/3)). Therefore harmonics through degree c_d(log n)^(3/2)
remain visible above root-width feature error.

An intuitive version is that neurons with larger Gaussian slopes produce
sharper tanh transitions. The slopes are rare, but their combined harmonic
contribution is still relevant at accuracy decreasing as a power of n.
The theorem uses all these contributions through a positive covariance
sum and finite-sample concentration, rather than requiring every neuron
to have a bounded slope.

## 4. A real escape route: approximate the output rather than all features

Here is an exact finite-width identity, with no population-limit assumption.
Let g_n(0,v) be the initialized second-layer feature vector. Define

\[
 K_n(s)=E\left[\frac{g_n(0,u)^\top g_n(0,v)}n\right]
                  \quad\text{for }u\cdot v=s.
\]

This is well-defined: right-rotational invariance of A_n and independence
of W_n show that the expectation depends only on u dot v. Since w_n(0)=0,
the exact output derivative is

\[
 \dot f_n(0,v)=\frac2m\sum_a y_a
                        \frac{g_n(0,v_a)^\top g_n(0,v)}n.
\]

Taking expectations gives

\[
 \boxed{E\dot f_n(0,v)=\frac2m\sum_{a=1}^m y_a K_n(v_a\cdot v).}
                                                               \tag{1}
\]

The same one-variable function occurs in all m terms. Thus the mean
onset response admits a separated representation involving only the
training projections. This holds for both same-sign and opposite-sign
labels. It does not claim an efficient method for computing K_n, a uniform
finite-run concentration estimate, or a nonlinear all-time closure.

For orthogonal training inputs, K_n(0)=0 exactly. To see this, reflect
the first-layer Gaussian rows across the direction v_a: g_n(0,v_a)
changes sign while g_n(0,v_b), b!=a, is unchanged. The initialization
law is unchanged, so the cross expectation vanishes. The diagonal is
positive. Similarly, the limiting top-feature training Gram is gamma I,
where, for independent standard normal variables as needed,

\[
 \gamma=E\tanh^2\!\left(\sqrt{E\tanh^2(Z)}\,Z\right)>0.
\]

This explains why orthogonal data are attractive for an observable-based
compression. It does not simplify the whole hidden-feature family to the
same extent: RESULT.md applies to that family unchanged.

## 5. Why the onset identity is not yet a trained compressor

Hidden feature motion starts at second order in t and is quadratic in
the labels. Write, only in this calculation, b=m^-1 sum_a y_a g_n(0,v_a)
and D_a=diag(1-g_n(0,v_a)^2). Differentiating the actual equations gives

\[
 \dot w_n(0)=2b,\qquad \dot A_n(0)=\dot W_n(0)=0,
\]

\[
 \ddot W_n(0)=\frac4{mn}\sum_a y_aD_ab\,h_n(0,v_a)^\top,
\]

\[
 \ddot A_n(0)=\frac4m\sum_a y_a
 \operatorname{diag}(1-h_n(0,v_a)^2)
 W_n(0)^\top D_ab\,v_a^\top.                             \tag{2}
\]

All these are exact, finite-width formulas. The vector b couples samples
before multiplication by their different nonlinear gates. Orthogonality
of the input vectors does not make these gates, b, or the fixed mixer
separate into m independent systems. For example, even the scalar-neuron
case with two orthogonal inputs and nonzero first weights has nonzero
cross-label products in (2) on an open set of initializations. This example
only rules out an exact algebraic decoupling; it is not a width-rate result.

Consequently a positive theorem would need to control the evolving scalar
response and its feedback, rather than preserve every hidden source or
truncate training at onset. A fixed small Y does not justify discarding
the nonlinear terms when n tends to infinity: a fixed O(Y^3) prediction
error eventually exceeds n^-1/2.

One plausible new construction would retain only the directions relevant
to the m evolving responses and to the queried output, with an adaptive
or structured representation of the pairing operators. To certify it,
one must close the residual and representation error equations, control
all input queries, count both moving and fixed storage, and compare at
the same physical time through the endpoint. Those estimates are open
here. The new lower theorem neither rules them out nor supplies them.

## 6. Research outcome

The requested reduction of the dimension-dependent logarithmic exponent
has **not** been obtained for a trained predictor. What is proved is a
reason the proposed temporal route cannot achieve it in the existing
architecture, even with optimally coordinated source selection. A genuine
reduction from 3d toward d or sqrt(d) needs a change in which neural
quantities are approximated or in their quadratic retained representation.
The exact onset identity shows why such a change is not excluded by the
hidden-feature obstruction. No universal impossibility result is claimed.
