# Whole-circle component: complete frozen review text

This is the initialized observation component of the bounded reference
candidate. It uses the same exact canonical model, T=1/200 and two-atom law as
H3_candidate_reference_v1.md. Its code is H3_circle_kernel.py, with
H3_circle_kernel_test.py; the complete outward arithmetic and integration
primitive is H3_shorttime_solver.py. Current b is supplied by that certified
reference evolution, including its saved-state uncertainty.

Before initialization the fixed configuration is degree 7, 8192 Simpson
subdivisions on [0,8], 60 decimal digits. The current b interval radius budget
is 1e-8, input coordinate radii sum budget 1e-6, output conversion reserve 1e-40.
The numerical error plus the separately proved analytical envelope 2.417e-6
must be below 1e-5. The declared one-core, 8-GiB numerical budget applies.
No coefficient from an unvalidated sizing calculation is used.

## 2. Hermite identities with a contained completeness argument

Let gamma be the standard normal probability measure. Define the probabilists'
Hermite polynomials by

    He_0=1, He_1=x, He_(n+1)=x He_n-n He_(n-1).

The generating identity is

    exp(tx-t²/2)=sum_(n>=0) He_n(x)t^n/n!.

It follows by differentiating the exponential in t and matching the recursion
and first two coefficients; its Taylor series is entire for each x. For jointly
standard normal X,Y with covariance rho in [-1,1], completing the square gives

    E exp(sX-s²/2) exp(tY-t²/2)=exp(rho s t).

Derivatives at zero can pass through expectation: on a bounded s,t set every
required derivative is dominated by a fixed polynomial in |X|+|Y| times
`exp(C(|X|+|Y|))`, integrable by Cauchy–Schwarz and Gaussian exponential
moments. Matching coefficients yields

    E He_m(X)He_n(Y)=1_(m=n) n! rho^n.                 (K1)

This includes rho=+/-1, either directly or by L2-continuous Gaussian coupling.
At rho=1 the normalized polynomials are orthonormal in L2(gamma).

They are complete. Suppose f in L2(gamma) is orthogonal to every polynomial.
The finite signed measure eta=f gamma has finite total variation by
Cauchy–Schwarz. For every complex z,

    F(z)=integral exp(zx) d eta(x)

is well defined. On |z|<=R, `|f(x)| exp(R|x|)` and the corresponding
polynomial multiples are integrable, again by Cauchy–Schwarz. Expanding exp
and using dominated convergence makes F entire with coefficients
`integral x^n f dgamma/n!`, all zero. Hence `F(it)=0` for every real t.

Here is the Fourier uniqueness fact needed for this last condition. Convolve
eta with a centered normal density of variance s>0. The identity

    normal_s(x-y)=(1/(2pi)) integral exp(-s t²/2) exp(it(x-y)) dt

follows by the one-dimensional Gaussian integral (complete the square, or
differentiate the Gaussian cosine integral and solve its resulting first-order
equation). Fubini is valid because eta has finite total variation and
`exp(-s t²/2)` is integrable. The convolution is zero because F(-it)=0.
For every bounded Lipschitz function b, convolution against the Gaussian
converges uniformly to b as s decreases to zero, with error at most
`Lip(b)*sqrt(s)*E|G|`. Thus `integral b d eta=0`. Approximating a compact set
inside an open set by continuous distance functions, then Borel sets by
compact/open approximations of finite Borel measures, shows eta=0. Therefore
f=0 almost everywhere. This proves completeness.

For any f in L2(gamma), orthogonal finite sums converge to f: their squared
coefficient sum is bounded by ||f||2², the partial sums are Cauchy, and the
residual is orthogonal to every polynomial, hence zero. Parseval follows.
Combining this with (K1), finite truncation, and Cauchy–Schwarz gives

    E f(X)f(Y)=sum_(n>=0) (E f(G)He_n(G))² rho^n/n!.    (K2)

The series converges absolutely and uniformly for |rho|<=1 because the sum
of its nonnegative coefficients is ||f||2². This proof needs no temporal
analyticity, moment-generating function of a trained field, or Stieltjes
representation.

## 3. The two composed initialized kernels

Write

    q=E tanh²G,
    alpha_n=(E tanh(G)He_n(G))²/n!,
    h(rho)=sum alpha_n rho^n.

Oddness makes all even coefficients zero. Parseval gives `sum alpha_n=q>0`.
For unit u,v, `(g.u,g.v)` are jointly standard normal with covariance u.v,
so their first-feature covariance is h(u.v). Initial forward source calls
have no earlier reverse response; the resulting pair `(A0 tanh(g.u),
A0 tanh(g.v))` is centered Gaussian with variances q and covariance h(u.v).
This is exactly the H2 initialization, with a common forward law.

Next put

    v=E tanh²(sqrt(q)G),
    beta_n=(E tanh(sqrt(q)G)He_n(G))²/n!,
    H(s)=sum beta_n (s/q)^n,          |s|<=q,
    K(rho)=H(h(rho)).

Here v is the upper feature variance called `k` by the short-time solver;
it is not that solver's separately named reverse-source variance `v`.

Again the even coefficients vanish and `sum beta_n=v`. Formula (K2) proves
that K(u.v) is the initialized upper hidden covariance. At the orthogonal
reference the upper Gram is v times the identity and its readout coefficients
are `(b,-b)`, where `b'=1-vb`, `b(0)=0`. Thus the exact cheap observation is

    fF(t,u)=b(t)[K(u1)-K(u2)].                            (K3)

This scalar readout equation is cited only to identify the supplied current b
and its bound `0<=b(t)<=t<=T`. The circle module neither solves it nor stores t.

## 4. Positive tails and the outer Lipschitz bound

Let `f(x)=tanh(sqrt(q)x)` and `c_n=E f He_n`. Gaussian integration by parts
and the Hermite recursion give

    E f'(G)He_(n-1)(G)=E f(G)He_n(G)=c_n, n>=1.

Indeed the derivative of `He_(n-1) normal_density` is
`-He_n normal_density`; the boundary term vanishes because f,f' are bounded
and the remaining factor is polynomial times a Gaussian. Bessel applied to
f' therefore yields

    sum_(n>=1) n beta_n
      =sum_(n>=1) c_n²/(n-1)! <= E f'(G)² <= q.          (K4)

For a,b in [-1,1], `|a^n-b^n|<=n|a-b|` by factoring their difference.
Consequently H has Lipschitz constant at most one on [-q,q]. This argument
does not require differentiation of an endpoint power series.

Let p(rho)=sum_(odd n<=7) alpha_n rho^n and
`P(s)=sum_(odd n<=7) beta_n(s/q)^n`. Nonnegativity ensures
`|p(rho)|<=sum_(n<=7)alpha_n<=q` on the entire correlation interval.
Writing

    A_tail=q-sum_(n<=7)alpha_n,
    B_tail=v-sum_(n<=7)beta_n,

gives, uniformly for |rho|<=1,

    |K(rho)-P(p(rho))| <= A_tail+B_tail.                (K5)

The first term follows from the Lipschitz bound for the full H; the second
from the positive outer tail and `|p/q|<=1`. This is a uniform certificate
including perfect correlation and anticorrelation, not a grid comparison.

## 5. Certified one-dimensional coefficient integration

For sigma=1, then sigma=sqrt(q), integrate simultaneously

    E tanh²(sigma G),
    E tanh(sigma G)He_n(G),      n=1,3,5,7.

All five integrands are even. The latter four need not be nonnegative, so
their omitted tails are bounded symmetrically. q is an interval before sigma
is evaluated; every upper-layer integral propagates the entire sigma interval.
The positive lower bound for q is checked before any division.

For the fourth-derivative bound write an integrand as
`Q(x,h,sigma) normal_density(x)`, with h=tanh(sigma x). Its exact derivative
has polynomial factor

    DQ=partial_x Q+sigma(1-h²)partial_h Q-xQ.             (K6)

The implementation applies this operator four times to `He_n(x)h`, and to h²
for the variance, retaining exact integer coefficients and powers of sigma.
For sigma in [0,1] and |h|<=1, every remaining monomial is bounded by its
coefficient magnitude times `sup_x |x|^j normal_density(x)`.
The maximum occurs at sqrt(j), or zero for j=0. Outward elementary arithmetic
and ceiling supply the verified table through degree 11:

    (1,1,1,1,1,2,5,11,30,88,269,871).

The resulting fourth-derivative bounds for n=1,3,5,7 and variance are

    411, 2511, 24277, 328533, 1098.

For reference, the inherited contained Simpson proof has nonpositive Peano
kernel on one double subinterval with absolute integral 1/90 after scaling.
Summing and doubling the even integral on [0,R] gives

    Simpson error <= R^5 M4/(90 N^4).                   (K7)

Its kernel proof, outward Decimal implementation, and pi normalization were
read in H3_candidate_reference_v1; no unvalidated quadrature library is invoked.
At the fixed R=8,N=8192 the largest coefficient Simpson bound is below
`2.656e-8`, before division by sqrt(n!) or squaring into spectral mass.

For tail moments `J_j=E[|G|^j 1_{|G|>R}]`, Mills' bound and integration by
parts give

    J0<=2 phi(R)/R, J1=2 phi(R),
    J_j=2 R^(j-1)phi(R)+(j-1)J_(j-2), j>=2.

Since |tanh|<=1, the absolute tail of the nth coefficient is bounded by
`sum_j |He_n[j]| J_j`. The largest of these four tail bounds is below
`3.910e-9`. The variance omitted tail is nonnegative and is added as
`[0,J0]`; the signed Hermite coefficient tail is added symmetrically.
All interval evaluation widths, q uncertainty, Simpson bounds, and Gaussian
tails are included before computing alpha_n and beta_n by interval squaring
and division by the exact integer n!.

## 6. Interval coefficients, exact midpoint evaluator, and uniform error

Denote exact rational centers of the coefficient intervals by a_n,b_n,Q and
their summed radii by e_alpha,e_beta; denote the radius of q by e_q. Rational
means exact Fraction conversion of decimal endpoints and rational division
by two, not a floating midpoint. Let `qlo,qhi` be its endpoints and
`S_alpha=sum a_n`.

The stored midpoint kernel is

    s_hat(rho)=clip_( [-1,1] )(sum a_n rho^n/Q),
    K_hat(rho)=sum b_n s_hat(rho)^n.

Every requested rational correlation is evaluated by exact rational arithmetic.
The clip only protects the midpoint model from interval-induced mass excess;
it neither discards a Gaussian mode nor changes the exact target. Since the
true finite inner ratio s lies in [-1,1], projection cannot increase its error:

    |s-s_hat| <= e_alpha/qlo + S_alpha e_q/(qlo Q).

The true finite outer polynomial has Lipschitz constant at most qhi on
[-1,1] by (K4). Changing its coefficients separately costs e_beta. Thus

    E_parameter=qhi[e_alpha/qlo+S_alpha e_q/(qlo Q)]+e_beta,
    E_kernel=A_tail_upper+B_tail_upper+E_parameter,     (K8)

where the two tail upper bounds use the variance upper endpoint minus the
sum of mass lower endpoints. Every expression in (K8) is exact rational
arithmetic. If an interval contradicts positive Parseval mass, initialization
fails rather than masking it.

Let the supplied current b interval have midpoint b0 and radius e_b, retaining
the true current value. Intersect it with the exact invariant bound [0,T].
Then for every unit u,

    |fF(t,u)-b0[K_hat(u1)-K_hat(u2)]|
       <=2|b0| E_kernel+2 vhi e_b
       <=2T E_kernel+2 vhi e_b.                         (K9)

The first term compares the two kernel values; the second uses `|K|<=v`.
It is essential to include the supplied b uncertainty, particularly after a
restart. The API rejects intervals whose radius exceeds the declared 1e-8
budget. It does not assert that arbitrary supplied b values solve the scalar
reference equation.

The final exact rational midpoint and radius are converted by the inherited
outward interval operations, giving a returned enclosure. A reserve of 1e-40
is included in the reported uniform numerical error for representing the
midpoint output in Decimal. To justify this conservative reserve: all output
midpoints and error radii here have absolute value below one; at precision
at least 60 each correctly rounded conversion/addition has absolute error
below 1e-59. A fixed number below ten of these final operations costs below
1e-57. The API rejects lower Decimal precision. Initialization interval
rounding already belongs to (K8) and is not charged twice.

The `prediction(b,u1,u2)` API requires exact rational unit coordinates and
checks `u1²+u2²=1` exactly. It performs no unvalidated sine/cosine operation.
All rational circle points are available via
`((1-a²)/(1+a²),2a/(1+a²))` and the missing endpoint. The formula defines a
continuous function on the entire real unit circle and (K9) holds there;
rational evaluation is an exact input interface, not a restriction of the
mathematical supremum to a finite grid.

The additional `prediction_box(b,u1_interval,u2_interval)` accepts an arbitrary
represented unit direction. Its promise is enclosure of every actual point in
the supplied box intersected with the unit circle. Boxes whose squared norm
range excludes one are rejected. Clipping coordinate intervals to [-1,1]
retains every possible unit point. At the exact rational coordinate midpoints,
evaluate the same midpoint kernel. Its Lipschitz constant is bounded by

    L_mid=(sum n a_n/Q)(sum n b_n),                       (K10)

because coefficient centers are nonnegative, powers on [-1,1] have Lipschitz
constant n, and scalar clipping has Lipschitz constant one. If the coordinate
radii sum to e_u, the further prediction error is at most
`|b0| L_mid e_u <= T L_mid e_u`. This term, with the fixed e_u budget 1e-6,
is included in the reported uniform numerical bound. Every computable unit
direction can be supplied by successively refined rational/decimal coordinate
enclosures, so this numerical interface covers the entire represented circle
and charges its input rounding. It does not treat an enclosure of a coordinate
as an exact trigonometric value.

The state needed by this observation component is q,v and eight coefficient
intervals, plus the supplied current b interval. Its streamed quadrature needs
only a fixed list of interval accumulators, never a tensor node array or a
history. Serialization preserves all interval endpoints and reconstructs the
same fixed certificate. It adds no evolving variable or time coordinate.

## 7. Tests, execution, and limits

Before integration, seven deterministic static tests pass. They verify the exact
Hermite covariance identity through degree seven against expansion of
`Y=(3/5)X+(4/5)Z` with independent normal monomial moments; the fourth derivative
of the normal density against its explicit polynomial; consistency with the
existing h² derivative envelope; exact linear-kernel evaluation and
serialization; domain and interval-budget rejection; and the parameter bound
against exact rational linear-kernel perturbations. These checks use no
training trajectory and no empirical resolution comparison.
The seventh test covers an irrational unit direction through outward sqrt
intervals, a rational unit point in a nonzero-width coordinate box, and rejection
of a box disjoint from the unit circle.

The main initialized quadrature run writes its fixed configuration before
any integral is evaluated. The inherited analytical envelope N1
is a separate proof component: adding `2.417e-6` to a passing numerical bound
does not turn this module into an arbitrary-accuracy C-H3 solver. The degree,
reference law, time horizon, and error thresholds are not selected from a
trajectory. The active nonorthogonal/nonatomic family, arbitrary joint
observations, and terminating full nonlinear refinement remain outside this
component.


## Numerical claims and reproduction interface

The fixed initialized computation reports first omitted Hermite mass below
.000480719508, second omitted mass below .000014597495, parameter error in one
kernel below 3e-10, and total kernel error below .000495317302. Its uniform
numerical prediction error including b/input/rounding budgets is below
4.959364e-6. Adding the 2.417e-6 analytical envelope gives 7.376364e-6 < 1e-5.
These are claims for fresh independent reproduction, not premises of the
integration or Hermite proofs. Recorded initialization runtime was 4.437536 s,
peak RSS 17380 KiB; timing may vary on reproduction.

The combined H3_reference_solver.py driver initializes this component,
serializes and reloads its kernel.json, and supplies the preserved reference
readout interval. prediction_box encloses the prediction at every represented
unit direction in the supplied box. The combined wrapper adds the cumulative
canonical-GF analytical remainder. The exact rational midpoint model also
defines a continuous function on the entire circle; no finite angular grid is
used to justify its uniform bound.

This component does not refine the nonlinear dynamics, remove the fixed-order
error floor, support a broader law family, or implement every admissible joint
observation tuple. The original full C-H3 obligations remain distinct.
