# Independent adversarial audit of the quartic-flat response note

## Verdict and provenance

**PASS, within the stated local scope.** The global tangent flow, full
fixed-driver initial-state Jacobian bound with exponent 20, driver derivative,
signed L1 composition, and all finite Gaussian moments are proved correctly.
The displayed finite-dimensional adjoint identities, prescribed-forcing
existence result, cubic late-injection counterexample, and finite-angle
zero-orbit calculations also pass. I found no required mathematical correction
to those statements. The exponent 20 is an admissible upper bound; optimality
is not claimed or established.

This is a theorem about the displayed two-coordinate systems. It is not a
network response theorem, an estimate for an endogenous driver-selection map,
or a transfer from the tangent equation to arbitrary finite-angle states.
Failure of angle-uniform constants is **not an obstruction to the user's
quantifier**: one activation must be independent of data, but proof constants
may depend on the fixed data and T. Likewise, the late-injection example
excludes a bound uniform over unrestricted signed drivers; it does not exclude
bounds involving their size or the structure of actual network forcing.

Audit date: 2026-09-05. The sole mathematical source inspected was
`/tmp/l3-two-sample-Un7kw9/QUARTIC_FLAT_GATE_RESPONSE.md`, all 846 lines,
including its final line. Before analysis its computed SHA256 was

```text
7c88a195b9ad250bed56d1dde43de3cd5f04558911b710e413ec253b2c346777
```

This equals the user-supplied hash. I personally read
`/etc/codex/skills/solve-math-rigorously/SKILL.md` in full. I inspected no
research histories, other proof files, or other reviews, consulted no other
agents or external mathematical sources, and performed no numerical or
computational experiments. File reading, line counting, hashing, and writing
this review are administrative operations, not experiments. The candidate was
not edited. Line references below refer to this exact candidate.
After writing the review, I rechecked the candidate: it still had 846 lines
and the identical SHA256 recorded above.

The audit proceeds by reconstructing the invariant and orbit bounds, checking
the conversion to fixed-driver derivatives, and then independently checking
composition, forcing, and the finite-angle boundary. In particular, bounded
derivatives at fixed terminal contrast are never substituted for derivatives
at fixed driver time.

I retain the candidate's notation: e > 0 is fixed, L = 1+e,
a(z) = 1+e/(1+z^4), b = a', F(s) = (1+s)(1+s+e), and
B = 1+|M_0|+sqrt(e)|V_0|. Vector and operator norms are Euclidean.

## 1. Activation, global flow, and the exceptional orbit

Lines 20-52 are correct for every fixed e > 0. The positive integrand defining
A is even, so A is odd. Splitting the positive half-line at 1 gives the stated
bound 4/3. For g(z) = (1+z^4)^(-1), differentiating

\[
g^{(k)}(z)=\frac{P_k(z)}{(1+z^4)^{k+1}}
\]

produces numerator

\[
P_{k+1}(z)=(1+z^4)P_k'(z)-4(k+1)z^3P_k(z).
\]

Starting with P_0 = 1, its degree is at most 3(k+1). The resulting rational
functions tend to zero at infinity and are continuous everywhere. Thus all
positive derivatives of A are bounded. The first derivative of phi also has
its constant term 1; it remains bounded, although phi itself is unbounded.
The nonconstant A' proves nonaffinity. Direct differentiation gives

\[
b'(z)=\frac{4ez^2(5z^4-3)}{(1+z^4)^3},\qquad b(0)=b'(0)=0.
\]

The stated bounds 1 <= a <= L and |b| <= 4e follow separately on |z| <= 1
and |z| >= 1. No smallness assumption on e is used.

For the vector field G(M,V) = (Vb(M),a(M)), integration on either side of
r = 0 gives

\[
|V(r)|\le |V_0|+L|r|,\qquad
|M(r)|\le |M_0|+4e|V_0||r|+2eLr^2.
\]

These bounds also hold uniformly for initial states in a compact
neighborhood on a fixed bounded driver interval. The smooth field is bounded
and Lipschitz on a containing ball. The integral map is a contraction on a
sufficiently short interval; at any finite maximal endpoint the bounded
field makes the path Cauchy, and the limiting state allows continuation.
This verifies global existence and uniqueness in both time directions.

The same compact neighborhoods justify the C1 dependence used in lines
117-129: subtracting integral equations gives continuous dependence, and the
uniform first-order Taylor remainder of G gives convergence of difference
quotients to the solution of J_r = DG(X(r))J, J(0) = I. The integral
inequality used here can be obtained by iterating an integrable Lipschitz
majorant: its n-fold ordered integral is bounded by the nth power of its
total integral divided by n!. Thus this argument requires only finite
compact-interval bounds, not the later driver-uniform estimate.

Since V_r >= 1, V tends to opposite infinities as r does and crosses zero
exactly once. In particular there cannot be a driver-uniform bound on V.

The zero common orbit must be treated transversely, not merely differentiated
within the line M = 0. Here the candidate does so correctly:

\[
\Psi_r(0,V_0)=(0,V_0+Lr),\qquad
DG(M,V)=\begin{pmatrix}Vb'(M)&b(M)\\b(M)&0\end{pmatrix}.
\]

Every entry of DG vanishes on that orbit. The full variational equation
therefore gives D Psi_r(0,V_0) = I_2, including transverse perturbations,
and the driver derivative is (0,L), for every finite signed r. The singular
invariant is neither needed nor assigned a value at zero. There is no
exceptional-orbit gap.

## 2. Invariant, excursion, and integrability

For M_0 != 0, write M_r = h(r)M with

\[
h(r)=-\frac{4eV(r)M(r)^2}{(1+M(r)^4)^2}.
\]

On finite intervals h is continuous, so the integrating-factor identity
M(r) = M_0 exp(integral h) preserves the nonzero sign. This justifies every
subsequent division by M or M_0 on these orbits.

Differentiating the displayed Lambda in lines 165-173 gives

\[
\Lambda'(M)=\frac{L+(2+e)M^4+M^8}{2eM^3}
 =\frac{F(M^4)}{2eM^3}=-\frac{2a(M)}{b(M)}.
\]

Consequently d(V^2 + Lambda(M))/dr = 0. Lambda is even and its restriction
to the positive half-line is strictly increasing from minus infinity to
plus infinity. Hence the invariant uniquely gives m(v) on the initial
sign branch for every real v. Strict monotonicity and surjectivity of V
identify this implicit orbit with the actual global flow.

With Y = v^2 and X = m^2, differentiation gives

\[
m_Y=f(m)=-\frac{2em^3}{F(m^4)},\qquad
X_Y=-\frac{4eX^2}{(1+X^2)(1+X^2+e)}\in[-e,0].
\]

The last interval follows from (1+X^2)^2 >= 4X^2. Therefore, with
c = |m(0)|,

\[
|m(v)|\le c,\qquad
c^2-M_0^2\le eV_0^2,\qquad c\le B.
\]

This proves the excursion bound for either sign of M_0, with the already
checked zero orbit supplying the remaining case.

In the identity for Lambda(c)-Lambda(M_0), all three displayed terms in
lines 214-217 are nonnegative. Retaining just the inverse-square term gives

\[
\frac{c^2}{M_0^2}\le 1+\frac{4eV_0^2c^2}{L}
 \le 1+\frac{4B^4}{L}.
\]

Thus no uncontrolled inverse power of a small M_0 is hidden in c/|M_0|.
This step is essential to uniformity across states approaching the zero
orbit.

Since F is increasing on nonnegative arguments,

\[
\frac{d}{dY}\frac1{m^2}=\frac{4e}{F(m^4)}
 \ge\frac{4e}{F(c^4)}.
\]

Integration from Y = 0 proves the envelope with
kappa = 4ec^2/F(c^4). Independently, as |v| tends to infinity the invariant
forces m to zero. Set H = V_0^2+Lambda(M_0); multiplying the invariant
by m^2 gives

\[
v^2m^2=Hm^2+\frac L{4e}-\frac{2+e}{4e}m^4-\frac{m^8}{12e}
 \longrightarrow\frac L{4e}.
\]

Hence |m(v)| is asymptotic to sqrt(L)/(2 sqrt(e)|v|). The assertion that
|m| has no integrable majorant on a nonzero full orbit is correct; using an
integral of |m| in the clock estimate would fail. The proof instead uses

\[
\int_{\mathbb R}|m|^3\,dv
 \le\frac{c^2\sqrt{F(c^4)}}{\sqrt e},\qquad
\int_{\mathbb R}|m|^6\,dv
 \le\frac{c^5\sqrt{F(c^4)}}{\sqrt e},
\]

\[
\sup_v |v|\,|m(v)|^3
 \le\frac{c^2\sqrt{F(c^4)}}{2\sqrt e}.
\]

The first follows by the substitution t = sqrt(kappa)v and the
antiderivative t/sqrt(1+t^2) of (1+t^2)^(-3/2); the second uses
|m|^6 <= c^3|m|^3; the third uses |t|/(1+t^2)^(3/2) <= 1.
All resulting powers of c are nonnegative, so there is no small-c
singularity in these estimates.

## 3. All four fixed-driver derivatives and the exponent 20

The derivatives at fixed terminal contrast, in lines 254-269, are

\[
J(v)=m_{M_0}(v)=\frac{\Lambda'(M_0)}{\Lambda'(m(v))}
 =\left(\frac{m(v)}{M_0}\right)^3
   \frac{F(M_0^4)}{F(m(v)^4)}>0,
\]

\[
m_{V_0}(v)=-2V_0f(m(v)),\qquad m_v(v)=2vf(m(v)).
\]

The sign of m_{V_0} is correct because 1/Lambda'(m) = -f(m).
The implicit derivative is legitimate on either nonzero sign branch;
neither v nor V_0 is a denominator.

For Y >= Y_0, the cubic ratio is at most one and F(m^4) >= L, giving
J <= (K/L)B^8. For 0 <= Y <= Y_0, the F ratio is at most one and
c/|M_0| <= rho B^2, giving J <= rho^3 B^6. With the candidate's
constants this proves J <= jB^8 on the entire orbit. The looser B^14
orbit estimate mentioned in lines 296-298 is also valid.

Using F(c^4) <= K B^8 and the integral bounds above gives exactly

\[
\int|m|^3\le I B^6,\qquad \int|m|^6\le I B^9,\qquad
\sup |v||m|^3\le I B^6.
\]

The last bound deliberately discards a factor 1/2. Since
|f(m)| <= (2e/L)|m|^3 and |V_0| <= B/sqrt(e), the bounds
|m_{V_0}| <= d B^4 and |m_v| <= h B^6 follow with the displayed d,h.

The decisive distinction is the clock

\[
r=\int_{V_0}^{V(r)}\frac{dv}{a(m(v;M_0,V_0))}.
\]

Its terminal derivative is 1/a(m(V)) > 0. At each finite r and nonzero
M_0 it is a finite integral with a C1 integrand in a neighborhood of the
parameters. This permits ordinary parameter differentiation. The full-orbit
integrals above are used only afterward as bounds; no differentiation of
an improper integral or interchange with an infinite supremum occurs.

Holding r fixed and differentiating gives

\[
V_{M_0}=a(m(V))\int_{V_0}^{V}
 \frac{b(m)m_{M_0}}{a(m)^2}\,dv,
\]

\[
V_{V_0}=\frac{a(m(V))}{a(M_0)}+
 a(m(V))\int_{V_0}^{V}\frac{b(m)m_{V_0}}{a(m)^2}\,dv.
\]

The second formula includes the moving lower endpoint. Both remain true
for V < V_0 with the oriented integral. The common coordinate then requires

\[
M_{M_0}=m_{M_0}(V)+m_v(V)V_{M_0},\qquad
M_{V_0}=m_{V_0}(V)+m_v(V)V_{V_0}.
\]

These are the full fixed-driver derivatives, not the fixed-contrast ones.
At r = 0 they give V_{M_0} = 0, V_{V_0} = 1, M_{M_0} = 1 and
M_{V_0} = -2V_0 f(M_0)+2V_0 f(M_0) = 0, a check on both the lower
endpoint and the chain term.

For V_{M_0}, use |b(m)| <= 4e|m|^3, a >= 1, a(m(V)) <= L,
and J <= j B^8. This yields |V_{M_0}| <= kj B^14. For V_{V_0},
use the pointwise product bound

\[
|b(m)m_{V_0}(v)|\le\frac{16e^2}{L}|V_0||m(v)|^6.
\]

Its clock contribution is at most 16e^(3/2) I B^10 and its endpoint
contribution is at most L. Therefore |V_{V_0}| <= ell B^10.
The terminal chain terms now give

\[
|M_{M_0}|\le (1+hk)jB^{20},\qquad
|M_{V_0}|\le (d+h\ell)B^{16}.
\]

The exponent 20 is precisely 8+6+6 in the first chain contribution.
None of the other entries requires a larger exponent.

The driver derivative is G itself, so

\[
\|\partial_r\Psi_r\|\le |Vb(M)|+a(M)
 \le (L+4eI)B^6.
\]

The sum of the four absolute matrix entries bounds the Euclidean operator
norm. Consequently the proposed explicit constant

\[
C_e=(1+hk)j+kj+(d+h\ell)+\ell+L+4eI
\]

works, with K = 2(2+e), rho = sqrt(1+4/L), j = K/L+rho^3,
I = sqrt(K/e), d = 4sqrt(e)/L, h = 4eI/L, k = 4eLI, and
ell = L+16e^(3/2)I. These constants are finite for every fixed e > 0.
At M_0 = 0 the sum of norms is 1+L, which is covered because ell >= L
and j > 1. Thus no limiting argument through the singular invariant is
needed to include that line. Since B >= 1, exponents 26 and 30 follow too.

As a separate algebraic consistency check on the full Jacobian, on a
nonzero orbit put beta = -2V_0 f(M_0). Then m_{V_0}(v) = beta J(v),
so the two clock formulas imply
V_{V_0} = a(M)/a(M_0)+beta V_{M_0}. Taking the determinant after the
terminal chain rule cancels both chain terms and gives

\[
\det D\Psi_r=J(V)\frac{a(M)}{a(M_0)}
 =\frac{b(M)}{b(M_0)}>0.
\]

Here f = b/(2a), and b is nonzero on the sign branch. Independently,
differentiating the two-by-two determinant in J_r = DG J gives
(det J)_r = Vb'(M)det J, while d(log|b(M)|)/dr = Vb'(M), confirming
the same formula with initial determinant one. Thus a bounded forward derivative
does not entail a uniformly bounded inverse along reached states.

## 4. Signed L1 composition and Gaussian moments

For q in L1 locally, r(t) = integral_0^t q is absolutely continuous,
with bounded image on each finite interval. Composing it with the C1 flow
therefore gives an absolutely continuous path and

\[
\frac{d}{dt}\Psi_{r(t)}(x_0)=q(t)G(\Psi_{r(t)}(x_0))
\]

almost everywhere. This chain rule can be justified directly on the compact
driver image: the C1 derivative is bounded and uniformly continuous there,
and its first-order increment formula combines with absolute continuity of
r. No inverse of r(t), monotonicity, or nonvanishing q is involved.

For uniqueness, any two proposed paths on [0,T] lie in a common ball, where
G has a finite Lipschitz constant K_0. Their difference is bounded by
K_0 integral |q| times their pointwise difference. Absolute continuity of
the integral of |q| permits a finite partition with K_0 integral |q| < 1
on each piece. Taking the supremum first on the initial piece and then
successively on later pieces proves equality. This checks the claim of
exactly one locally absolutely continuous solution for signed q.

For the C1 solution map in lines 450-473, the primitive map from L1[0,T]
to C[0,T] has norm at most one. At any fixed (x_0,q), all arguments
(r(t),x_0) and their sufficiently small perturbations belong to one compact
subset of finite-dimensional space. Uniform continuity of D Psi there gives
a Taylor remainder that is uniformly o(|delta x_0|+||delta q||_1), proving
Fréchet differentiability into C and continuity of that derivative. Its
value is exactly

\[
\delta X(t)=D\Psi_{r(t)}(x_0)\delta x_0+
 \partial_r\Psi_{r(t)}(x_0)\int_0^t\delta q(s)\,ds.
\]

The bound C_e B^20(|delta x_0|+||delta q||_1) is independent of the
base driver and T. It is a derivative bound, not a bound on the size of the
solution itself. If a driver is selected by some other state, the resulting
delta q must still be estimated. The candidate explicitly makes this
distinction, so it does not omit an endogenous-driver derivative while
claiming to control one.

For measurability, the response is continuous in r for each x_0, and jointly
continuous before taking the supremum. Its supremum over real r equals the
supremum over rational r, a countable supremum of continuous functions of
x_0. For any p > 0,

\[
S(x_0)^p\le C_e^p(1+|M_0|+\sqrt e|V_0|)^{20p}.
\]

The sum inequality in lines 486-487 holds by subadditivity when its exponent
is at most one and by convexity when it is at least one. A scalar Gaussian
with positive variance has density proportional to
exp(-(v-m)^2/(2 sigma^2)); multiplying by any fixed positive power of |v|
leaves an integrable tail, since that power is eventually bounded by a
constant times exp(v^2/(8 sigma^2)) and the shifted quadratic still has a
strictly negative leading coefficient. A zero-variance Gaussian is constant.
Applying these facts to the two marginals proves all the asserted finite
moments, including noninteger p, nonzero means, dependence, and singular
covariance. No independence assumption or threshold involving pe or variance
has been imported. The same pathwise bound applies to the derivative
operator of the solution map. It supplies no moments for uncontrolled
selection derivatives or for the full state supremum in V.

## 5. The common channel and the limits of the invariant

The identities in lines 499-546 follow from actual finite-dimensional
differentiation. For h = phi(M), k = a(M)V,

\[
dh=a(M)dM,\qquad dk=b(M)VdM+a(M)dV,
\]

so an incoming pair (p,q) produces preactivation adjoints
(a(M)p+b(M)Vq,a(M)q). Applying this rule first at layer 3, then through
W, then at layer 2, and finally through U gives

\[
p_3=0,\quad q_3=C,\quad
p_2=W^*[Cb(M_3)V_3],\quad q_2=W^*[Ca(M_3)],
\]

\[
p_1=U^*[a(M_2)W^*[Cb(M_3)V_3]
             +b(M_2)V_2W^*[Ca(M_3)]],
\]

\[
q_1=U^*[a(M_2)W^*[Ca(M_3)]].
\]

These expressions use coordinatewise multiplication inside the brackets.
The pair (p_1,q_1) consists of incoming adjoints at (h_1,k_1). The final
local pullback gives bottom Euclidean gradient components
(a(M_1)p_1+b(M_1)V_1q_1,a(M_1)q_1), exactly the right-hand side of
(32). A common scalar multiplying the gradient can be included in the
drivers. No population-space or network-dynamics theorem is needed for these
finite-dimensional identities.

In the scalar example U = W = C = 1, M_1 = 0, V_1 = 1, one obtains
M_2 = 1, V_2 = L, M_3 = phi(1) > 0, V_3 = a(1)L > 0.
Both terms in p_1 are strictly negative because b is strictly negative at
positive arguments and all their other factors are positive. Thus p_1 < 0
at M_1 = 0. This is a decisive counterexample to a universal algebraic
vanishing factor M_1 in p_1; no merely formal appeal to higher layers is
being used.

For the forced local equation, differentiating the invariant wherever
M != 0 cancels the q terms and gives

\[
\frac{d}{dt}(V^2+\Lambda(M))
 =\Lambda'(M)a(M)p
 =\frac{(1+M^4+e)^2}{2eM^3}\,p.
\]

The coefficient is asymptotic to L^2/(2eM^3). Its sign on the negative
half-line is correctly retained. There is no regular extension of this
invariant identity through a zero crossing. Such a crossing is possible:
take q = 0 and p = 1, so M increases with speed a(M) >= 1. The underlying
equation remains smooth. The scalar adjoint example above shows why the
displayed network algebra alone supplies no cancellation of this singular
coefficient; it does not prove impossibility of other estimates.

For prescribed integrable p,q, the finite-horizon bounds also check:

\[
|V(t)|\le |V_0|+LQ_t,
\]

\[
|M(t)|\le |M_0|+LP_t+4e|V_0|Q_t+2eLQ_t^2,
\qquad P_t=\int_0^t|p|,\quad Q_t=\int_0^t|q|.
\]

The last term follows from integral Q_s |q(s)| ds = Q_t^2/2, valid
because Q is absolutely continuous with derivative |q| almost everywhere.
On a containing ball the local Lipschitz coefficient is at most a constant
times |p|+|q|. Small-integral intervals give contraction and uniqueness;
the bounds permit continuation at every finite endpoint. This argument is
for prescribed drivers, exactly as stated, and does not assume these bounds
remain valid for an unspecified closed feedback law.

The trained-operator terms in lines 583-593 are also correct product rules:
differentiate Uh_1 and Uk_1 to get dot(U)h_1 + U dot(h_1) and
dot(U)k_1 + U dot(k_1), where

\[
\dot k_1=b(M_1)V_1\dot M_1+a(M_1)\dot V_1.
\]

The corresponding W identities follow the same rule.
Thus p_3 = 0 alone does not turn the moving top preactivation into the
isolated two-coordinate flow.

## 6. Common-forcing variation and the cubic late injection

For the base p = 0 solution and a direction eta in L1[0,T], the claimed
first variation exists. Here is a justification independent of merely
writing its formal equation. For |epsilon| <= 1, the preceding forced
growth bounds put the solutions with p = epsilon eta into a common compact
ball. Write H(M,V) = (a(M),0). Both G and H have uniformly continuous
derivatives there. The integral difference inequality first gives
||X_epsilon-X||_infinity <= C |epsilon|, with C finite for the fixed
q,eta,T; iterating the integrable Lipschitz majorant as in section 1
justifies that estimate. Taylor expansion of G, followed by division by
epsilon, has a remainder tending uniformly to zero after integration
against |q|. Also H(X_epsilon)eta converges in L1 to H(X)eta.
Applying the same difference inequality proves convergence of the quotient
to the unique solution of

\[
\dot{\delta X}=q(t)DG(X(t))\delta X+H(X(t))\eta(t),
\qquad \delta X(0)=0.
\]

For t >= s, the homogeneous propagator is

\[
K(t,s)=D\Psi_{r(t)-r(s)}(X(s)).
\]

The flow property identifies its base trajectory with X(t); differentiating
in t gives the homogeneous equation almost everywhere and K(s,s) = I.
Its coefficients are integrable, and K and its parameter dependence are
bounded on the fixed compact time square. Integrating the resulting
inhomogeneous equation, or differentiating the integral, verifies

\[
\delta X(t)=\int_0^t K(t,s)(a(M(s))\eta(s),0)\,ds.
\]

The theorem bounds K in terms of the reached state X(s), as in (37).
It does not bound this propagator in terms of the original state alone.
For M_0 = 0, DG vanishes throughout the base orbit, so K = I and
delta X(t) = (L integral_0^t eta,0). This is an exact first-order response,
not a claim that the finite-epsilon forced solution stays on zero.

For the nonzero example, take x_* = (c,0), c > 0, and reach
x_R = (m_R,R) in positive driver time r_R. The clock and invariant give

\[
R/L\le r_R\le R,\qquad
R^2+\Lambda(m_R)=\Lambda(c),\qquad
Rm_R\longrightarrow\frac{\sqrt L}{2\sqrt e}.
\]

The return time -r_R must be frozen at its nominal value during
differentiation. At its terminal point (c,0), m_v = 2v f(m) = 0.
Consequently the fixed-driver common-to-common entry really is the
fixed-terminal-contrast entry at this particular terminal point:

\[
\left.\partial_{M_{\rm in}}[\Psi_{-r_R}]_M\right|_{x_R}
 =\frac{f(c)}{f(m_R)}
 =\left(\frac c{m_R}\right)^3\frac{F(m_R^4)}{F(c^4)}.
\]

As F(m_R^4) tends to L, this is asymptotic to

\[
\frac{8e^{3/2}c^3}{\sqrt L F(c^4)}R^3.
\]

This check rules out the potential error of differentiating a return time
chosen separately for each perturbed state.

For the piecewise driver on [0,3], the first interval reaches x_R, the
middle interval has q = 0, and the last interval applies exactly the fixed
map Psi_{-r_R}. During the middle interval p = epsilon and V is constant;
at epsilon = 0 the common first variation after one time unit is a(m_R).
It follows that

\[
\left.\frac{d}{d\varepsilon}M_\varepsilon(3)\right|_{0}
 =a(m_R)\frac{f(c)}{f(m_R)}
 \sim\frac{8e^{3/2}c^3\sqrt L}{F(c^4)}R^3.
\]

The direction 1_[1,2] has L1 norm exactly one. The horizon is exactly
3 and B = 1+c is fixed, whereas ||q_R||_1 = 2r_R tends to infinity.
Thus the asserted failure of a bound depending only on the original state,
uniform over signed q for arbitrary common-forcing directions, is proved.
It requires no impulse, no asymptotic replacement of the actual equations,
and no uniformity of the differentiation remainder over R.

There is no conflict with the original-state theorem. For p = 0 the full
outward-return map is Psi_0, whose initial-state derivative is I. The late
injection has not passed through the outward derivative. In addition,
differentiating Psi_tau(Psi_h(x)) = Psi_{tau+h}(x) in h at zero proves
D Psi_tau(x)G(x) = G(Psi_tau(x)); this explains the driver-direction
cancellation. Replacing G by H gives no such general identity. It does
hold on the exceptional zero orbit, consistently with its separate exact
calculation; the sentence in lines 700-704 is correctly read as denial of
a general identity, not denial at every individual state.

## 7. Finite-angle boundary and Gaussian thresholds

This section audits the displayed ODE (42) as a local equation. Its use as
the actual dynamics of any particular finite-angle network is not assumed.
For 0 < delta < 1 and mu^2 = 1-delta^2, subtracting the rational
expressions for a(M+delta V) and a(M-delta V) gives

\[
b_\delta(M,V)=
 -\frac{4eMV(M^2+\delta^2V^2)}
 {[1+(M+\delta V)^4][1+(M-\delta V)^4]}.
\]

The coefficient 4, the sign, and all powers of delta in (43) are correct.
Because a takes values in [1,L], the absolute difference of two of its
values is at most e. Thus |b_delta| <= e/(2delta), and
1 <= a_delta <= L. At every fixed positive delta the vector field is
smooth and bounded, so the same compact-interval construction and
continuation prove the claimed global C1 flow.

At M = 0, evenness of a and oddness of b give the invariant zero line,
V_r = alpha_delta(V) = 1+e/(1+delta^4 V^4), and

\[
\partial_M b_\delta(0,V)
 =\frac{b(\delta V)}{\delta}
 =-\frac{4e\delta^2V^3}{(1+\delta^4V^4)^2}
 =\frac{\alpha_\delta'(V)}{\delta^2}.
\]

The other two off-diagonal derivatives vanish:
partial_V b_delta(0,V) = 0 and partial_M a_delta(0,V) = 0.
The remaining diagonal derivative is partial_V a_delta = alpha_delta'.
The full fixed-driver linearized system is therefore diagonal, with
coefficients mu^2 alpha_delta'/delta^2 and alpha_delta'. Since V_r is
strictly positive, integration using V as the variable gives exactly

\[
D\Psi_r^\delta(0,V_0)=
\begin{pmatrix}
[\alpha_\delta(V(r))/\alpha_\delta(V_0)]^{\mu^2/\delta^2}&0\\
0&\alpha_\delta(V(r))/\alpha_\delta(V_0)
\end{pmatrix}.
\]

Thus (44) really is the full Jacobian at fixed r, including transverse
common perturbations; it is not a derivative of a selected terminal state.
Because V_r >= 1, the orbit traverses every real contrast. Alpha_delta
is maximized at zero, so the maximum of the common entry is attained at
that terminal contrast and equals

\[
J_{\delta,\max}(V_0)
 =\left[\frac{L}{\alpha_\delta(V_0)}\right]^{\mu^2/\delta^2}.
\]

If V_0 = 0 the maximum is 1 and occurs at r = 0. The positive exponent
mu^2/delta^2 is needed here and follows from the strict delta range.

For |V_0| > 1, evaluating the already-computed derivative at the chosen
parameter delta = 1/|V_0| gives

\[
\log J_{\delta,\max}(V_0)
 =(V_0^2-1)\lambda_e,\qquad
\lambda_e=\log\frac{2L}{L+1}>0.
\]

No derivative of that parameter choice is taken. This legitimate family
of evaluations disproves a bound C_e B^N valid simultaneously for all
initial contrasts and all angles, for any fixed finite N, since
B = 1+sqrt(e)|V_0| on this line and a positive quadratic exponential
eventually exceeds every polynomial. It does not disprove a bound whose
constant depends on a fixed delta.

For the upper bound, with V_0 != 0 put u = delta^2 V_0^2 > 0. Algebra
and integration of 1/(1+x) <= 1 give

\[
\log\frac{L(1+u^2)}{L+u^2}
 =\log\left(1+\frac{eu^2}{L+u^2}\right)
 \le\frac{eu^2}{L+u^2}.
\]

Multiplying by mu^2/delta^2 <= 1/delta^2 = V_0^2/u and using
(u-sqrt(L))^2 >= 0 yields

\[
0\le\log J_{\delta,\max}(V_0)
 \le\frac{eV_0^2u}{L+u^2}
 \le\frac{eV_0^2}{2\sqrt L}.
\]

At V_0 = 0 this remains true because the logarithm is zero. In particular,
the supremum over angles is finite for each fixed initial contrast; loss
of a polynomial bound is a tail-growth assertion, not pointwise infinity.

Let Z be Gaussian with finite mean m and positive variance sigma^2, and
let p > 0.
Raising the last exponential bound to p and multiplying by the Gaussian
density leaves an exponent with quadratic coefficient

\[
\frac{pe}{2\sqrt L}-\frac1{2\sigma^2}.
\]

This is negative precisely under the displayed sufficient condition
pe sigma^2 < sqrt(L). The finite mean adds a linear term, and completing
the square then gives integrability. The supremum over delta is measurable
because (45) is continuous in delta on its open parameter interval, so its
supremum can be taken over the rationals there. Thus (48) concerns
E[(sup_delta J_delta,max)^p], exactly as stated, rather than the weaker
sup_delta E[J_delta,max^p]. The other diagonal entry and the zero-orbit
driver derivative have norms at most L. Adding these bounded terms does
not change the sufficient moment condition for the complete response.
The example e = 1/10, sigma^2 = 1, p = 4 satisfies it, since
2/5 < sqrt(11/10).

Conversely, for centered Z, evaluation at delta = 1/|Z| on |Z| > 1 gives
the lower bound exp(p lambda_e(Z^2-1)) for the pth power of the angle
supremum. After multiplication by the centered Gaussian density, its tail
is a positive constant times

\[
\exp\left[\left(p\lambda_e-\frac1{2\sigma^2}\right)v^2\right].
\]

If the quadratic coefficient is positive the integral diverges; if it is
zero the integrand is a positive constant on an infinite-measure set, so
it still diverges. This verifies the equality case in lines 820-826.
The candidate correctly labels the upper sufficient threshold as
nonoptimal and does not assert that these two criteria exhaust the gap
between them. No endpoint claim at pe sigma^2 = sqrt(L) is inferred from
the sufficient upper bound. A zero-variance Gaussian is deterministic and
has finite moments of the pointwise finite angle supremum.

At each fixed positive delta,
J_delta,max <= L^(mu^2/delta^2), a deterministic constant, so this
zero-orbit response has all finite moments without a variance restriction.
Finally, for fixed V_0 the earlier upper bound
e V_0^2 u/(L+u^2) tends to zero as delta tends to zero; hence
J_delta,max tends to 1. For fixed finite r, V(r) stays bounded by
|V_0|+L|r|, and alpha_delta(V) = L+O(delta^4) uniformly on this bounded
range. The logarithm of the ratio of alpha factors is therefore
O(delta^4); multiplying by mu^2/delta^2 makes the common-entry logarithm
O(delta^2). Thus both diagonal entries tend to one at fixed r, consistently
with the tangent zero-orbit identity, while the contrasts of order
1/delta in the counterexample prevent uniformity over the Gaussian tail.

## 8. Required corrections and scope of acceptance

**Required corrections to the local theorem and the specified auxiliary
equations: none.** In particular, the following suspected failure modes
are resolved by the displayed arguments:

- The orbit derivative is converted to the full fixed-driver derivative
  through both clock endpoint differentiation and the terminal chain rule.
- M_0 = 0 is handled by the full variational equation, without using a
  singular invariant or assuming transverse derivatives vanish.
- Signed L1 drivers are handled by composition and an integrable Lipschitz
  argument; neither an invertible clock in physical time nor a sign condition
  is required.
- The B^20 accounting uses integrable cubic and sixth powers of the orbit,
  with no hidden negative power of c or M_0. All finite Gaussian moments
  then follow from a polynomial bound, including singular covariance.
- The common forcing is present in the actual finite-dimensional adjoint
  calculation. Its invariant defect is a limitation of that invariant, and
  the cubic late-injection example proves the stronger stated failure of
  driver-uniform common-forcing response.
- The finite-angle zero-orbit calculation is at fixed driver time. The
  Gaussian upper condition is sufficient, and the lower divergence
  condition includes equality for the centered Gaussian as claimed.

The references to an unspecified arctangent gate or earlier theorem in
lines 7, 226-227, 663-665, and 845-846 are contextual comparisons, not
dependencies in any accepted derivation. This audit does not certify an
external arctangent theorem that is not defined in the candidate. If those
comparisons are intended as additional standalone theorem claims, their
activation and equations must be supplied and the comparisons derived, or
the comparisons removed. That conditional editorial issue does not require
any change to the proved quartic statements.

Likewise, the remarks about full networks, population products, trained
operators, and angle-limit transfer correctly delineate additional work;
they are not missing hypotheses in the isolated theorem. This PASS cannot
be used as certification of those additional conclusions. Failure of a
constant uniform over all angles, or of a forcing derivative uniform over
drivers of unbounded size, must not be promoted to failure of the user's
data-independent activation goal with data- and T-dependent proof constants.
