# Deterministic Gaussian cubature with all finite moments

Status: contained author proof candidate and arithmetic audit; not an independent
review, trajectory experiment, or certified training calculation. Author:
`/root/h3v2_scope`, 2026-09-13. This supplements the frozen scope proof and the
coordinator's numerical route. The scope proof was left unchanged, SHA256
`2c4c6ad2cee83ac0302a4d6beb0152f19127167f1c9ed10f6a611b83b33384dd`.

Scientific input scope: complete `H3_v2_route_coordinator.md` and complete
`H3_v2_arithmetic.py`, plus previously read required instructions and skills.
No other route file, study, web source, or trajectory was read or evaluated.
After the draft, the compiler author sent an implementation summary; this
note does not treat that summary as a verified compiler premise. Local
Python Decimal primitive docstrings were inspected to verify their rounding
contract. The initially audited arithmetic SHA256 is
`8547ce730fc3c0fc8200d678b7903fecb9de03d5c16b5faa49d2ad9df1d6b20d`.
Findings in section 7 refer to that version; arithmetic edits belong to the
coordinator.

## 1. Exact construction and conclusion

For integer base `b≥2`, write a nonnegative integer in its finite base-b
expansion `k=sum_(j=0)^(ell-1) a_j b^j` and define its radical inverse

\[
 h_b(k)=\sum_{j=0}^{\ell-1}a_jb^{-j-1},\qquad h_b(0)=0.
\]

Let `b_1,b_2,...` be successive primes, and use the **first positive** indices
`k=1,...,Q`. In dimension `d≥1`, set `m=ceil(d/2)` and form the joint tuple
`(h_(b_1)(k),...,h_(b_(2m))(k))`. For each pair, put

\[
 r_j=\sqrt{-2\log h_{b_{2j-1}}(k)},\quad
 \theta_j=2\pi h_{b_{2j}}(k),\quad
 (z_{2j-1},z_{2j})=(r_j\cos\theta_j,r_j\sin\theta_j).
 \tag{1}
\]

Retain the first `d` coordinates, and write
`Gamma_(Q,d)=Q^(-1) sum_(k=1)^Q delta_(z(k))`. Dimension zero means the
unit law on the unique empty tuple.

**Theorem.** For every fixed finite `d` and every real `1≤p<∞`,

\[
 \mathcal W_p(\Gamma_{Q,d},\gamma_d)\longrightarrow0,
 \qquad \gamma_d=N(0,I_d),                              \tag{2}
\]

where the distance uses the ordinary Euclidean norm. For every finite
`p>0`, the powers `|z|^p` are uniformly integrable over **all** the rules
`Gamma_(Q,d)`. Thus every continuous function of polynomial growth,
including every finite polynomial and every joint mixed polynomial moment,
has convergent cubature averages. The coordinates in (1) are evaluated
jointly at the same index `k`. They are not independent at finite `Q`;
their limiting joint law is the product standard Gaussian law.

More generally, let `a_Q→a` be a convergent finite coefficient vector and
suppose `F(a,z)` is continuous, with
`|F(a',z)|≤C(1+|z|^r)` for all `a'` in a neighborhood of this convergent
sequence, for finite nonnegative `C,r`. Then

\[
 Q^{-1}\sum_{k=1}^Q F(a_Q,z(k))
       \longrightarrow\int F(a,z)\,d\gamma_d(z).          \tag{3}
\]

The same conclusion applies simultaneously to any fixed finite collection
of such integrands, including named-source derivatives with polynomial
Gaussian envelopes. Section 5 explains the finite causal initializer
consequence. No limit in growing source dimension or growing program length
is asserted.

## 2. Equidistribution and a quantitative one-coordinate bound

Fix a coordinate base `b` and a depth `r`. A half-open digit interval
`[a/b^r,(a+1)/b^r)` specifies the first `r` fractional base-b digits of
`h_b(k)`. Those are exactly the reversed last `r` base-b digits of `k`.
Consequently membership in that interval is equivalent to one residue
class for `k modulo b^r`. Terminating expansions cause no exception because
the intervals are half-open and are interpreted by this finite digit rule.

For several distinct prime bases, a product of such intervals specifies one
residue modulo each of the pairwise coprime numbers `M_j=b_j^(r_j)`. To
verify the simultaneous assertion directly, let `M=prod_j M_j`. The Euclidean
algorithm supplies `c_j` with `c_j(M/M_j)=1 modulo M_j`. The integer
`sum_j a'_j c_j(M/M_j)` has the desired residues `a'_j`. Any two solutions
differ by a multiple of each `M_j`, hence by a multiple of `M`. Thus exactly
one class modulo `M` is selected. Among `1,...,Q` its cardinality differs
from `Q/M` by at most one. The empirical frequency of the product digit
interval therefore converges to its volume `1/M`.

These intervals give a finite rectangular partition at every chosen tuple
of depths. For a continuous function on `[0,1]^(2m)`, choose those depths
large enough that its oscillation on each cell is small. The integral and
the sample average both lie between the corresponding finite lower and upper
step sums; the empirical cell frequencies converge as just proved. Then let
the mesh diameters go to zero. This proves joint equidistribution of the
first positive Halton points against every continuous test. It also handles
the boundary of the cube, which has zero Lebesgue mass.

We need more than this qualitative assertion near radial coordinates zero.
Define the one-dimensional star discrepancy, with strict upper endpoints,

\[
 D_{Q,b}=\sup_{0\le t\le1}
 \left|Q^{-1}\#\{1\le k\le Q:h_b(k)<t\}-t\right|.
\]

For an aligned block of integers `a b^r≤k<(a+1)b^r`, write `k=a b^r+j`.
Then

\[
 h_b(k)=h_b(j)+b^{-r}h_b(a),\qquad 0\le j<b^r.
\]

The first term ranges once through the grid `l/b^r`, `0≤l<b^r`, in a
permuted order; the second is one common offset in `[0,b^(-r))`. There is
therefore exactly one point in every cell of length `b^(-r)`. For any
threshold `t`, the number below it differs from `b^r t` by at most one:
all fully included cells contribute exactly one, and there is at most one
partially included cell.

Write `Q` in base b. Greedily partition the integer interval `[0,Q)` into
aligned blocks, first its largest powers of b, then the smaller powers.
Every block starts at a multiple of its length because all preceding
lengths are multiples of it. The number of blocks is the sum of the base-b
digits of `Q`, at most `(b-1)(floor(log_b Q)+1)`. Adding the block errors
gives this bound for the unnormalized discrepancy of indices `0,...,Q-1`.
Replacing the point at index zero by the point at index `Q` changes a
threshold count by at most one. Therefore

\[
 D_{Q,b}\le\frac{1+(b-1)(\lfloor\log_b Q\rfloor+1)}{Q}
 \le\frac{b}{\log b}\frac{\log(bQ)}{Q}.                 \tag{4}
\]

The estimate is allowed to exceed one at small `Q`; it is still a valid
upper bound. Only finitely many bases are used at fixed dimension.

Finally, for `1≤k≤Q`, the denominator of the finite radical inverse is
`b^ell≤bk≤bQ`. Its numerator is an integer between one and `b^ell-1`.
In particular

\[
 \frac1{bQ}\le h_b(k)\le1-\frac1{bQ}.                  \tag{5}
\]

Both logarithms and Box–Muller radii in (1) are consequently finite for
every fixed positive rule. Starting at index zero would violate this.

## 3. Logarithmic tails and every Gaussian moment

For one coordinate put `X_k=-log h_b(k)≥0` and `M_Q=log(bQ)`.
Equation (5) gives `X_k≤M_Q`. Equation (4), applied at `e^(-t)`, gives

\[
 Q^{-1}\#\{X_k>t\}\le e^{-t}+D_{Q,b},\qquad t\ge0.    \tag{6}
\]

For a nonnegative random variable `X`, a finite real `p>0`, and `L≥0`,
the elementary integral identity

\[
 X^p\mathbf1_{X>L}
 =L^p\mathbf1_{X>L}+\int_L^\infty p t^{p-1}
                                  \mathbf1_{X>t}\,dt
\]

holds pointwise (with the evident interpretation at `L=0`). It follows by
integrating the derivative of `t^p` from `L` to `X` when `X>L`. Averaging
this nonnegative identity and using (6), with the empirical survival
function zero above `M_Q`, gives

\[
 Q^{-1}\sum_{k=1}^Q X_k^p\mathbf1_{X_k>L}
 \le I_p(L)+D_{Q,b}M_Q^p,                              \tag{7}
\]

where the entire left side is zero if `M_Q≤L`, and

\[
 I_p(L)=L^p e^{-L}+\int_L^\infty p t^{p-1}e^{-t}\,dt.
\]

For fixed `p`, `I_p(L)→0`. For example, any fixed power of `t` is at most
`e^(t/2)` for all sufficiently large `t`, as is seen by comparing `log t`
with `t`; the remaining exponential integral tends to zero.

This gives a uniform tail estimate, not just convergence at a fixed cutoff.
From (4),

\[
 D_{Q,b}M_Q^p\le\frac{b^2}{\log b}M_Q^{p+1}e^{-M_Q}.
\]

For `L≥p+1`, the function `t^(p+1)e^(-t)` is nonincreasing for `t≥L`.
If `M_Q>L`, the preceding display is thus at most
`(b²/log b)L^(p+1)e^(-L)`. If `M_Q≤L`, the empirical tail is zero. Therefore

\[
 \sup_{Q\ge1}Q^{-1}\sum_{k=1}^Q X_k^p\mathbf1_{X_k>L}
 \le I_p(L)+\frac{b^2}{\log b}L^{p+1}e^{-L}
 \longrightarrow0.                                    \tag{8}
\]

For a uniform variable on `(0,1)`, `-log U` has survival exactly `e^(-t)`,
so `I_p(L)` is also its exact `p`-moment tail. Equation (8) supplies the
empirical uniform integrability which qualitative equidistribution alone
does not provide.

For the Gaussian tuple in (1), let `X_j=-log U_(2j-1)` and `S=sum_j X_j`.
Before dropping a possible final coordinate, the squared norm is exactly
`2S`; afterwards it is at most `2S`. For `p>0` and `R>0`,

\[
 |z|^p\mathbf1_{|z|>R}
 \le(2m)^{p/2}\sum_{j=1}^m
 X_j^{p/2}\mathbf1_{X_j>R^2/(2m)}.                     \tag{9}
\]

Indeed `S≤m max_j X_j`, and `S>R²/2` implies
`max_j X_j>R²/(2m)`. The maximum term is included in the displayed sum.
This argument uses no independence of the empirical coordinates. Apply (8)
separately to the finitely many radial-coordinate bases. The right side of
(9), averaged over the rule, tends to zero uniformly in `Q` as `R→∞`.
Thus all powers `|z|^p`, `p>0`, are uniformly integrable, with an explicit
majorant from (8),(9). In particular every such empirical moment is bounded
uniformly over `Q`.

## 4. Joint Gaussian limit and Wasserstein convergence

The Box–Muller map is continuous where all its radial coordinates are
positive. For a bounded continuous test `f` of its output, multiply
`f(BoxMuller(u))` by continuous cutoffs that vanish for a radial coordinate
below `epsilon` and equal one when all radial coordinates exceed
`2epsilon`. Extend the product by zero on the radial boundary. The result
is continuous on the cube, so its averages converge by section 2.
The error is at most a fixed multiple of `||f||∞` times the probability
that some radial coordinate is at most `2epsilon`. For the uniform law
this is at most `2m epsilon`; for the empirical law (4) gives the same
bound plus the sum of the finitely many discrepancies, which tends to zero.
First send `Q→∞`, then `epsilon→0`. This proves weak convergence to the
pushforward of joint independent uniforms.

For one independent uniform pair, set `u=exp(-r²/2)` and `v=theta/(2pi)`.
The absolute Jacobian in polar variables is
`r exp(-r²/2)/(2pi)`. Ordinary polar change of variables therefore gives
the Cartesian density `(2pi)^(-1)exp(-(x²+y²)/2)`. Distinct uniform pairs
are independent under product Lebesgue measure, so all `2m` Cartesian
coordinates are independent standard Gaussians. Dropping the last
coordinate when `d` is odd gives `gamma_d`. This proves the claimed weak
limit. It also shows directly that its moments of all finite orders are
finite, since exponential radial decay dominates polynomial powers.

To pass from weak convergence to all continuous polynomial-growth
integrals, multiply a test by a continuous cutoff on a ball of radius
`R`. Its bounded continuous part converges weakly. The two tail errors
vanish by (8),(9) and the Gaussian moment tails. This includes `|z|^p`
and every signed or mixed polynomial; an absolute value of a fixed
polynomial is bounded by `C(1+|z|^r)`.

Here are the coupling details yielding (2). Fix `p≥1` and a large ball
whose boundary has zero Gaussian mass. Partition its interior into finitely
many Borel cells of diameter at most `eta` and Gaussian-null boundaries,
for example by a finite rectangular grid and the ball boundary. Weak
convergence gives convergence of the cell masses. Couple their common
mass within the same cell, paying at most `eta^p`. Couple all unmatched
mass arbitrarily. Its portions inside the ball have mass tending to zero
and bounded `p`-cost. Its portions outside the ball are controlled by
`|x-y|^p≤2^(p-1)(|x|^p+|y|^p)` and the uniform `p`-moment tails already
proved. If a nonzero unmatched mass remains, its normalized product law
provides that coupling; if it is zero, no residual coupling is needed.
Let `Q→∞`, then `R→∞` and `eta→0`. The resulting coupling costs tend to
zero, proving `Wp→0`. The argument uses the entire same-point tuple.

## 5. Coefficient-dependent integrals and finite initialization

Let `a_Q→a` and `F` satisfy section 1's assumptions. On a fixed closed ball
`|z|≤R`, joint continuity and compactness of the convergent coefficient set
imply `sup_|z|≤R |F(a_Q,z)-F(a,z)|→0`. For the complement, the common
polynomial envelope and (9) make

\[
 \sup_Q\int_{|z|>R}|F(a_Q,z)|\,d\Gamma_{Q,d}(z)
 \longrightarrow0.
\]

The constant in `1+|z|^r` is controlled by the tail probability, which is
also bounded by a higher polynomial tail (or Markov followed by (9)). The
same tail bound holds for `F(a,z)` under the Gaussian law. Split (3) into
the local-uniform coefficient difference, the fixed truncated-integrand
weak-convergence difference, and these two tails. Sending first `Q`, then
`R`, proves (3).

More generally, a sequence `F_Q` may replace `F(a_Q,·)` if it converges
locally uniformly to `F` and has a common polynomial envelope. The identical
proof applies. For vector-valued outputs satisfying these conditions,
their joint pushforward laws converge in every `Wp`: bounded tests give
weak convergence, and every output `p`-moment tail is bounded by an input
moment tail of some finite higher degree using the common polynomial
envelope. This also retains the joint law of the Gaussian root and all
outputs, rather than only their separate marginals.

The following precise finite causal application is useful for the proposed
initializer. Fix a finite graph, a finite root/source dimension, and a
strict covariance regularizer `tau>0`. At each stage its new deterministic
coefficients are finite integrals of continuous functions of the current
Gaussian tuple and earlier deterministic coefficients. Assume:

1. Each value and each named-source derivative which is integrated is a
   continuous finite expression with a common polynomial Gaussian envelope
   whenever its earlier finite coefficient vector ranges over a compact set.
2. Every finite algebraic coefficient operation is continuous at the exact
   coefficients; divisions have nonzero exact denominators. Covariances are
   assembled as full uncentered Grams of the retained joint operands, with
   `tau I` added before a Cholesky factor is taken.
3. Reevaluated prior expressions retain their specified earlier deterministic
   response coefficients. All source slots and every within-population
   correlation needed by an integrand are evaluated from the same joint
   Gaussian tuple.

Under these hypotheses, replacing all such Gaussian integrals by the joint
rules `Gamma_(Q,d)` makes every coefficient converge to its exact-integral
counterpart as `Q→∞`. Prove this by finite causal induction. The initial
coefficient list is fixed. Convergence at an earlier stage puts its
coefficients in a compact set. The new integrands then satisfy (3), so all
their integral coefficients converge. A Gram plus `tau I` has every
eigenvalue at least `tau`; its exact Cholesky pivots are strictly positive.
The recursion

\[
 L_{ii}=\sqrt{G_{ii}-\sum_{k<i}L_{ik}^2},\qquad
 L_{ji}=\frac{G_{ji}-\sum_{k<i}L_{jk}L_{ik}}{L_{ii}}
\]

proves continuity of its entries on positive definite matrices by induction.
Finite reevaluation of previous expressions under this convergent factor
converges locally uniformly and preserves a polynomial envelope. This
establishes the induction's next stage. There are finitely many stages,
so the proof terminates. It is not a fixed-point or self-consistency claim
for an infinite refreshed transcript.

In the tanh initialization language, the required envelope property has a
direct syntactic proof. Roots and Gaussian sources are affine coordinates.
Tanh, sine, cosine, and their fixed finite-order derivatives are bounded;
finite sums, finite products and affine action-source formulas preserve
polynomial envelopes. The chain/product rules for a **fixed** finite
named-source derivative create only finitely many such factors. On compact
coefficient sets their constants are uniform. Bounded first features and
bounded readout factors satisfy the same property. No assertion that an
arbitrary `L²` product is integrable is substituted for this graph argument.

If covariance regularization is subsequently removed, do so **after** the
fixed-positive-regularizer cubature limit. Exact Gaussian laws are continuous
in their finite covariance matrices, including singular limits: positive
semidefinite square roots converge, since every convergent subsequence of
bounded roots has a positive semidefinite limit whose square is the limit
matrix, and that positive square root is unique by diagonalization. Couple
them as `G_j^(1/2)Z`; bounded covariances give every common polynomial
moment envelope. Formula (3)'s truncation argument, now on this Gaussian
coupling, passes the finite integrals and named derivative expectations.
One must separately check that the finite exact regularized program's
covariance and coefficient recursion converges to the intended source
program. This lemma supplies that continuity mechanism; it does not assume
Cholesky is continuous at a singular endpoint and does not replace a missing
source-semantic proof of the initializer.

The construction's prefix property is exact: increasing Gaussian dimension
keeps the same first prime bases and the same coordinate pairs. With odd
dimension it temporarily drops one already defined partner and restores
that partner at the next dimension. Thus no new request resamples an old
coordinate. The theorem nevertheless fixes the final finite graph and its
dimension before taking `Q→∞`.

## 6. Arithmetic refinement at a fixed finite rule

This section states a **parametric arithmetic contract**, so that a practical
Decimal backend or a separate rational backend can discharge it with its
own implementation proof. At precision index `P`, assume exact integer
control and rational constants, and approximations to addition,
subtraction, multiplication, division, `log`, `sqrt`, `exp`, `sin`, and
`cos` whose errors tend to zero locally uniformly on compact subsets of
their domains as `P→∞`. Division denominators must stay away from zero;
logarithm inputs must stay positive; square-root inputs must stay
nonnegative. Exact-real comparisons with a strict limiting margin must
eventually return the corresponding branch. The backend must support an
unbounded sequence of such precision indices for a literal executable
refinement theorem.

**Finite arithmetic composition lemma.** Every fixed finite graph of these
operations, with exact operands in those domains and strict margins at its
tests and denominators, converges to its exact-real evaluation, provided
approximate square-root operands remain nonnegative. Strictly positive
exact radicands guarantee that last property eventually; a known zero
radicand can instead be returned as zero exactly. Prove the statement
by induction on its instructions: preceding approximate operands converge
and hence stay in one compact subset of the required domain; continuity
and local uniform consistency give convergence of the next instruction.
Strict inequalities and nonzero denominators persist for all sufficiently
large `P`. The finite induction retains all joint outputs. Branches at
periodic reduction boundaries are handled explicitly below instead of
assuming a strict margin there.

Rounding a real or rational basic-operation result to a multiple of
`10^(-P)` gives absolute error at most `10^(-P)` by integer division. Thus
an unbounded-integer rational implementation can meet the basic-operation
part without an exponent ceiling; elementary-function consistency remains
its own required implementation check. Inputs defining exact constants
are retained as integers/fractions or exact strings, rather than first
rounded through float64.

For each fixed `Q,d`, every uniform coordinate is an exact positive
rational bounded away from zero and one by (5). The finite graph consisting
of its integer radical inverses, divisions, logarithms, square roots,
trigonometric evaluations and matrix operations is covered by this lemma
and the details below. The existing Decimal implementation provides a
useful concrete illustration inside its admissible range. Section 7
distinguishes that range from literal unbounded refinement and records
an original scalar-context bug; this note does not audit a subsequently
added arithmetic backend.

The initially inspected `Decimal.ln` and `Decimal.exp` docstrings explicitly state
correct rounding with `ROUND_HALF_EVEN`; `Decimal.sqrt` states correct
rounding at full precision with the same mode. For fixed inputs in their
respective domains, these primitive contracts give an absolute error
tending to zero as precision increases. Their continuity then handles
converging input sequences. In particular every fixed radical-inverse
division converges to its exact rational, `ln U` converges for `U>0`, and
the resulting nonnegative square root converges. The expression

\[
 \tanh x=\operatorname{sign}(x)
          \frac{1-e^{-2|x|}}{1+e^{-2|x|}}
\]

has denominator at least one; its implementation converges at every fixed
real input and is continuous at zero. None of these steps requires a
uniform guarantee at arbitrary input magnitude for a fixed precision.

For clarity, the transcendental helpers also have elementary convergent
constructions if a primitive contract is not adopted: the exponential
series with a geometric bound on the eventual term ratios gives rational
upper and lower enclosures after range reduction; square root has rational
bisection on a bounded positive interval; and, after multiplying a positive
rational by a power of two into `[1,2]`,

\[
 \log x=2\sum_{k=0}^{\infty}\frac{v^{2k+1}}{2k+1},
 \qquad v=(x-1)/(x+1),\quad |v|\le1/3,
\]

follows by integrating the geometric series for `1/(1-v²)`. The remaining
power-of-two contribution uses the same series for `log 2`. Its tail is
bounded by a geometric series. These constructions produce arbitrarily
narrow rational enclosures at every fixed input and demonstrate the
mathematical arithmetic model without a precision or exponent ceiling.

The implemented pi formula is Machin's identity

\[
 \pi=16\arctan(1/5)-4\arctan(1/239).                    \tag{10}
\]

To verify it, put `alpha=atan(1/5)`, `beta=atan(1/239)`. The tangent
double-angle formula gives `tan(2alpha)=5/12` and
`tan(4alpha)=120/119`. Hence
`tan(4alpha-beta)=(120*239-119)/(119*239+120)=1`.
The angle lies strictly between zero and `pi/2`: `alpha<1/5`,
`alpha>1/5-(1/5)^3/3`, and `0<beta<1/239` give positivity and an upper
bound `4/5<pi/2`. Thus it is `pi/4`, proving (10). The elementary bound
`pi>2` suffices: `pi/4=atan(1)=integral_0^1 (1+t²)^(-1)dt>1/2`.

For `|x|<1`, integrating the finite geometric expansion of `1/(1+t²)`
gives the alternating arctangent series with error bounded by the first
omitted absolute term. At `x=1/5,1/239`, terms decrease geometrically.
The code forms successive powers and stops after a term smaller than
`10^(-(P+10))`. The number of terms is `O(P)`; for sufficiently high
precision the computed term ratio is still below a fixed number less
than one. Every fixed prefix converges to its exact prefix. The cumulative
rounding error is bounded by a constant times `P` times unit roundoff,
because the absolute sum of terms and all partial sums are bounded
independently of `P`. The exact tail and the rounding error therefore both
tend to zero. The final rounding of (10) to precision `P` also vanishes.
The ten guard digits are useful numerically but are not a fixed error
floor in this argument.

The sine/cosine helper reduces `x` modulo its computed `2pi` to an interval
whose endpoints converge to `±pi`, then uses the ordinary Taylor series.
For a fixed bounded input set, the integer quotient used in reduction is
bounded. Consequently using `pi_P` rather than `pi` changes the phase by
at most a fixed multiple of `|pi_P-pi|`, which tends to zero. At a branch
boundary the two possible reduced limits differ by `2pi`, so their sine
and cosine agree. All sufficiently high precisions can represent that
fixed finite quotient; no persistent modulo failure occurs within the
stated arithmetic model.

The reduced arguments are eventually bounded by four. In each Taylor
recurrence, the absolute ratio after a fixed initial number of terms is
at most `16/((a)(a+1))≤1/2`; the ratio decreases subsequently. Hence the
stop threshold is reached in `O(P)` steps and bounds an exact tail tending
to zero. Bounded intermediate absolute sums and `O(P)` operations bound
rounding error by `O(P)` times unit roundoff, tending to zero. At `x=0`
the sine loop returns zero and the cosine loop returns one directly. This
proves convergence of the implemented trig helper at every fixed input,
and locally uniformly in bounded input sets.

Combining the primitive and helper limits proves convergence of every
entry of `gaussian_points(Q,d,Arithmetic(P))` to (1) at fixed finite
`Q,d`, provided all scalar conversions and arithmetic execute in the
requested precision context. Finite averages and products then converge.
For positive regularized covariance matrices and ridge Grams, the exact
Cholesky pivots are positive. Induction in its finite recursion shows
that computed pivots are positive for all sufficiently high precision
and that every matrix entry converges. Forward substitution has nonzero
diagonal denominators and the same induction proves convergence of the
inverse-lower solve. A finite-precision unresolved pivot may raise an
error; it must not delete an eigenmode or silently modify the dimension.

Thus the valid numerical order is: precision to infinity for each fixed
finite point rule, graph, and positive regularizers; point count to infinity
at fixed graph and regularizers; only afterwards any justified covariance
regularizer limit and dictionary-order limit. These statements do not
prove convergence along an arbitrary joint schedule of all axes.

## 7. Implementation findings and executed checks

The deterministic audit is recorded in
`data/generated/observable_hierarchy/h3_v2_cubature_exact_checks/arithmetic_audit.json`.
No trajectory was computed. The direct tests found the following.

**Scalar conversion context bug.** In the initially audited source,
`Arithmetic.real()` performs unary-plus Decimal rounding and Fraction
division in the ambient context, without entering `self.context()`.
With ambient precision 28,
`Arithmetic(80).real(Fraction(1,3))` returned 28 digits, whereas the same
call inside `with ar.context()` returned 80 digits. Thus a caller that
builds fixed coefficients through direct `real()` calls can retain a
28-digit error floor despite increasing its arithmetic setting.
`gaussian_points()` itself wraps its conversion and arithmetic block in
the correct context, so this bug does not invalidate that function's
fixed-rule convergence under its own wrapper. The coordinator was asked
to make `real()` enter its own precision context (optionally via an
internal already-in-context helper), and subsequently reported applying
that repair. This audit has not tested that later source version. No
coordinator file was edited here.

**Avoidable integer-string limit.** The Decimal conversion path uses
`Decimal(str(value))`. For very large Python integers, this may hit the
interpreter's integer-to-string digit limit before Decimal receives the
number. Direct `Decimal(value)` for integral inputs avoids that limit;
NumPy integer values can first be converted to Python `int`. This matters
to a literal unbounded-index implementation of radical inverses. The
coordinator was sent this suggestion as well.

**Backend range versus mathematical refinement.** The installed backend
reports finite `MAX_PREC=MAX_EMAX=999999999999999999` and
`MIN_EMIN=-999999999999999999`. Setting its exponent range to those extrema
does not make them mathematically unbounded. The `P→∞` proof in section 6
is a theorem about the specified arbitrary-precision rounding model; it
is not a claim that this one installed Decimal implementation accepts
every integer precision and every exponent. If a literal executable
unbounded-refinement statement is required, the rational-enclosure
constructions in section 6 need an implemented fallback, or that backend
limitation must remain explicit. The coordinator subsequently authorized
and began a separate unbounded-integer rational backend. Its proof and
tests are a separate way to discharge section 6's arithmetic contract;
they are outside this note's audit scope. A fixed float64 fallback would
not discharge the contract. Ordinary finite resource limits also remain
separate from convergence.

**Helper preconditions.** `radical_inverse()` documents `index≥1,base≥2`
but does not validate them itself. A negative index never reaches zero
under its repeated `divmod` loop. Its present `gaussian_points()` caller
supplies validated positive indices and prime bases, so the valid-use
theorem is unaffected. A public reusable helper should reject invalid
arguments rather than loop indefinitely. `primes()` likewise receives a
valid integer count internally; no broader helper-domain claim is used.

For a finite numerical conformance check, seven joint Gaussian points in
dimension five were computed at 40 and 80 decimal digits. Their largest
entrywise difference was less than `1.6×10^-39`. This only checks the
two helper executions on that finite case; the convergence and moment
claims are proved in sections 2–6, not inferred from this comparison.
The scope-proof hash remained unchanged. The cubature proof itself makes
no monotone-error, discrepancy-rate-in-dimension, practical cost, training
accuracy, or useful finite-precision conditioning claim.
