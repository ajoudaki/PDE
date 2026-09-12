# Whole-circle initialized Hermite-kernel certificate

Status: complete candidate kernel proof and executed initialized
quadrature/evaluation component; seven static tests and its declared numerical
preflight pass. Not independently audited, not a complete C-H3 solver. No canonical, neural, or surrogate
trajectory is evaluated by this component. The current readout coefficient b
is an input to its observation map.

Owned files: `H3_circle_kernel.py`, `H3_circle_kernel_test.py`, this note.
The outward Decimal primitives are imported from `H3_shorttime_solver.py`.
The short-time worker explicitly confirmed that the imported primitives are
frozen, then froze that complete module at SHA-256
`cf3b479826c8900bc4097d023128330c380df415d83b2a782054c5e565542e6b`.
Its driver/checkpoint code is not called by this component.

## 1. Fixed contract and precommitment

Use exactly the canonical two-hidden-tanh model and initialization of H2,
physical unhalved-loss GF, T=1/200, Y=1, and the reference law
`nu*=.5 delta_(sqrt(2)e1,+1)+.5 delta_(sqrt(2)e2,-1)`. All expectations below
are initialized population/Gaussian expectations. The two forward calls use
the same initialized operator A0. This component extends the cheap frozen
readout prediction observation to the entire circle; paired hidden motions
remain the separate short-time component.

Before numerical integration the configuration is fixed:

- Hermite degree 7 in each of the two compositions; only odd degrees 1,3,5,7.
- Composite Simpson with 8192 subintervals on [0,8], doubled by even symmetry.
- 60 Decimal digits with outward endpoint widening at each operation.
- At most 60 core seconds, one core, 8 GiB, in a fresh
  `data/generated/observable_hierarchy/H3_circle_preflight_*` directory.
- The numerical whole-circle prediction error plus the separately supplied
  analytical envelope `2.417e-6` must be below `1e-5`.
- A supplied current b interval must enclose the actual zero-initial reference
  readout coefficient and have radius at most `1e-8`. Its prior error is retained.
- For arbitrary represented unit directions, the supplied two coordinate
  intervals have radii summing to at most `1e-6`; input uncertainty is charged.

The coordinator's unvalidated degree-sizing calculation is motivation only;
none of its values is a premise or coefficient. All coefficients and discarded
mass bounds are computed anew by the declared certified integrator. There is
one initialized quadrature run, no resolution sweep or trajectory selection.
Static polynomial and derivative tests precede that run.

Scientific inputs newly read: H3_contract, frozen H3_route_shorttime, the
shorttime solver and test, and H3_shorttime_numerics sections through its
execution record. Earlier allowed H2/notation/source dependencies and the
required research/mathematical skills remain the input scope. No other study
or unknown trajectory is used. The inherited analytical GF-to-frozen-prediction
bound is (N1) of H3_shorttime_numerics; this note's new theorem concerns the
initialized kernel and its numerical evaluation.

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
read in H3_shorttime_numerics; no unvalidated quadrature library is invoked.
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

### Completed one-run certificate

The unmodified final circle implementation and its seven tests were executed
in the fresh directory
`data/generated/observable_hierarchy/H3_circle_preflight_20260912_01/`.
The wrapper fixed CPU affinity to one allowed core, 8 GiB address space,
55 CPU seconds and a 55-second subprocess timeout; numerical thread counts
were one. The tests took 0.053 seconds and returned exit 0. The initialized
integrator returned exit 0, taking 4.437535464763641 seconds, with recorded
peak RSS 17,380 KiB. Python was 3.10.12 on Linux x86_64.

The exact interval/rational record proves the following rounded-up bounds:

| Quantity | Certified upper bound |
|---|---:|
| First Hermite omitted mass | 0.000480719508 |
| Upper Hermite omitted mass | 0.000014597495 |
| Midpoint coefficient/covariance parameter error in one kernel | 3.0e-10 |
| Combined one-kernel error | 0.000495317302 |
| Whole-circle numerical prediction error, including the b/input budgets | 4.959364e-6 |
| Numerical error plus the separate analytical 2.417e-6 envelope | 7.376364e-6 |

The computed interval variances were

    q in [0.3942944903090732473317575252387,
          0.3942944904866078761856040015029],
    v in [0.2364504103765712170993170372833,
          0.2364504106220189679293365896358].

The displayed decimal variance endpoints are rounded outwards; full endpoints
are saved. There was no changed resolution or numerical-validity repair run.
After serialization, a static check reconstructed the certificate, verified
identical records, and evaluated its e1 prediction at the directly enclosed
scalar expression `b=(1-exp(-v*.005))/v`. The result enclosed the independent
frozen e1 expression `b*v`. This was evaluation of a known scalar formula,
not a time-stepped trajectory. A box for `(1/sqrt(2),1/sqrt(2))` enclosed the
exact symmetry value zero. The corresponding b interval radius was below
`5.186e-12`, comfortably inside the declared 1e-8 budget.

Reproduce from the repository root, with the declared one-core/memory/time
limits applied by the calling environment:

```text
python -B studies/observable_hierarchy/H3_circle_kernel_test.py
python -B studies/observable_hierarchy/H3_circle_kernel.py --output data/generated/observable_hierarchy/H3_circle_preflight_FRESH
```

The script requires a fresh output directory. `configuration.json` is written
before initialized integration; `result.json` contains full q/v/coefficient
intervals, raw coefficient integrals, exact rational tails/errors, runtime,
environment, and the implementation/dependency hashes. A consumer reconstructs
`CircleKernel.from_record(result['kernel'])`, then supplies its saved current b
interval to `prediction` or `prediction_box`. This does not initialize, fit,
or recompute the evolution from time zero.

| Frozen item | SHA-256 |
|---|---|
| H3_circle_kernel.py | ec4975ae0f469755f0fa025e4b4b0b185f6b05fd97dbfa74bd60d34e61ffdef2 |
| H3_circle_kernel_test.py | 6550f472cc5876307832e62ed8a0cb451bccfe9a3deafe67ce9d86fb9a1aeb45 |
| H3_shorttime_solver.py | cf3b479826c8900bc4097d023128330c380df415d83b2a782054c5e565542e6b |
| configuration.json | 0a48ebecd531c93dddcb23fb2ec0b0301edf4c409fa23597473c527392fabe9f |
| result.json | 3ceed8636ac2e2c7a1074b519690a5d68f21c827ad75ad7d40555fe6e400173a |

Pre-edit HEAD was `c7f316153fbe5d7367bf482da98b8e87189f0ba3`, with empty
index; concurrent files were preserved. This worker changed only its three
assigned source/proof/test files and the authorized generated run products.
No Git mutation or established-material change was made. This record remains
a study component pending the coordinator's complete independent audits.
