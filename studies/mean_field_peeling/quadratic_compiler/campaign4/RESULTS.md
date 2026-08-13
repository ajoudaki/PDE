# Campaign 4 result: the full two-block metric quadrant

## Outcome

Campaign 4 did not falsify the finite-order output-kernel Stieltjes
conditions.  It replaces the previously tested one-dimensional metric ray by
the entire closed two-parameter quadrant and proves the relevant signs there
exactly.

For

$$
D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W,
\qquad \alpha,\beta\geq0,
$$

the exact output feature jets through order nine imply

$$
\mu_0,\mu_1,\mu_2,\mu_3\geq0,
$$

as well as

$$
\mu_0\mu_2-\mu_1^2\geq0,
\qquad
\mu_1\mu_3-\mu_2^2\geq0
$$

throughout the closed quadrant.  All six quantities are strictly positive at
every nonzero point of the quadrant and vanish only at
$(\alpha,\beta)=(0,0)$.  These are algebraic certificates: after exact
cancellation, every numerator coefficient is strictly positive and every
denominator is strictly positive on the whole closed quadrant.  No numerical
grid is used for the sign conclusion.

This is substantially stronger finite-order evidence than the old diagonal
test $\alpha=\beta$.  It is still not an all-order Stieltjes theorem.

## Exact object and its training interpretation

The network, quadratic activation, Gaussian initialization, mean-field
normalization, and one-sample objective are unchanged from the canonical
experiment.  The three pieces of the feature-ascent generator differentiate
the readout weights, first-hidden variables, and middle weights respectively:

$$
D_a,\qquad D_u,\qquad D_W.
$$

Campaign 4 varies the relative strengths of the latter two blocks while
fixing the readout coefficient to one.  Thus $\alpha$ and $\beta$ are genuine
block-metric, or equivalently block learning-rate, parameters.  The old
Campaign-1 family is exactly the diagonal

$$
\alpha=\beta=\lambda.
$$

For the one-sample squared loss $(1-f)^2$, metric gradient descent obeys

$$
\dot\theta
=2(1-f)\bigl(\nabla_a f+\alpha\nabla_u f+\beta\nabla_W f\bigr).
$$

Consequently it follows the same parameter-space path as the corresponding
feature-ascent system, with only a scalar change of time.  If $F_{\alpha,
\beta}(s)$ is the deterministic feature-ascent output curve and

$$
K_{\alpha,\beta}(y)
=F'_{\alpha,\beta}\!\left(F_{\alpha,\beta}^{-1}(y)\right),
$$

then the loss-driven output satisfies

$$
\dot f=2(1-f)K_{\alpha,\beta}(f).
$$

This reduction is exact at the formal-jet level.  Whenever the deterministic
mean-field curve exists globally, it is also the exact time-change identity
for that curve.  Establishing that the formal $K$ identifies the global
mean-field trajectory remains a separate open obligation.

## Exact bivariate feature jets

Let $C_{k,w,a}$ denote the exact sector with $w$ middle-weight hits and $a$
readout hits.  The remaining $k-w-a$ hits are first-hidden hits.  The compiler
therefore reconstructs

$$
F_{\alpha,\beta}^{(k)}(0)
=\sum_{w=0}^k\sum_{a=0}^{k-w}
C_{k,w,a}\alpha^{k-w-a}\beta^w.
$$

The first jet is

$$
F'(0)=27+48\alpha+36\beta.
$$

The third jet is

$$
\begin{aligned}
F^{(3)}(0)={}&103680\alpha+335232\alpha^2+227328\alpha^3\\
&+19440\beta+321408\alpha\beta+419328\alpha^2\beta\\
&+42768\beta^2+200448\alpha\beta^2+15552\beta^3.
\end{aligned}
$$

The fifth jet is

$$
\begin{aligned}
F^{(5)}(0)={}&1214300160\alpha^2
+5638201344\alpha^3
+7743799296\alpha^4
+2980184064\alpha^5\\
&+474958080\alpha\beta
+6660361728\alpha^2\beta
+15942279168\alpha^3\beta
+9280290816\alpha^4\beta\\
&+41640480\beta^2
+1789724160\alpha\beta^2
+9805307904\alpha^2\beta^2
+9508257792\alpha^3\beta^2\\
&+125971200\beta^3
+1869225984\alpha\beta^3
+3756367872\alpha^2\beta^3\\
&+95738112\beta^4
+462827520\alpha\beta^4
+11197440\beta^5.
\end{aligned}
$$

The seventh and ninth jets contain respectively 30 and 45 nonzero
monomials.  Their complete exact coefficient tables are in
`results_order9.json`; they are not abbreviated inside that artifact.
Coefficientwise parity gives

$$
F^{(0)}(0)=F^{(2)}(0)=F^{(4)}(0)=F^{(6)}(0)=F^{(8)}(0)=0.
$$

On the canonical point $(\alpha,\beta)=(1,1)$, the five nonzero jets are

$$
\begin{aligned}
F'(0)&=111,\\
F^{(3)}(0)&=1\,685\,184,\\
F^{(5)}(0)&=77\,400\,633\,120,\\
F^{(7)}(0)&=7\,315\,868\,433\,079\,296,\\
F^{(9)}(0)&=1\,181\,161\,141\,825\,400\,561\,664.
\end{aligned}
$$

More strongly, substituting $\alpha=\beta=\lambda$ reproduces every
coefficient of every accepted Campaign-1 polynomial through order nine, not
only its value at $\lambda=1$.

The family is not a removable overall scaling.  Already the distinct
$\alpha$ and $\beta$ coefficients of $F'(0)$ and the nine independently
varying monomials of $F^{(3)}(0)$ rule out reduction to the old diagonal
parameter.  For example, the exact off-diagonal point $(2,3)$ gives

$$
(F'(0),F^{(3)}(0),F^{(5)}(0))
=(231,14\,798\,496,2\,845\,728\,662\,304).
$$

## From the jets to the Stieltjes moments

Write

$$
F(s)=sA(s^2),
\qquad
A(r)=a_0+a_1r+a_2r^2+a_3r^3+a_4r^4+O(r^5),
$$

so that

$$
a_j=\frac{F^{(2j+1)}(0)}{(2j+1)!}.
$$

Exact series inversion yields

$$
K(y)=a_0+\mu_0y^2-\mu_1y^4+\mu_2y^6-\mu_3y^8+O(y^{10}),
$$

with

$$
\mu_0=\frac{3a_1}{a_0^2},
$$

$$
\mu_1=\frac{6a_1^2-5a_0a_2}{a_0^5},
$$

$$
\mu_2
=\frac{7a_0^2a_3-26a_0a_1a_2+21a_1^3}{a_0^8},
$$

and

$$
\mu_3
=\frac{-9a_0^3a_4+48a_0^2a_1a_3+20a_0^2a_2^2
-144a_0a_1^2a_2+90a_1^4}{a_0^{11}}.
$$

The first ordinary and shifted $2\times2$ Hankel determinants are

$$
\Delta_1=\mu_0\mu_2-\mu_1^2,
\qquad
\Delta_1^+=\mu_1\mu_3-\mu_2^2.
$$

For reference, the shifted numerator can also be computed directly from the
$a_j$ as

$$
\begin{aligned}
a_0^{16}\Delta_1^+={}&
45a_0^4a_2a_4-49a_0^4a_3^2-54a_0^3a_1^2a_4
+124a_0^3a_1a_2a_3\\
&-100a_0^3a_2^3-6a_0^2a_1^3a_3
+164a_0^2a_1^2a_2^2\\
&-222a_0a_1^4a_2+99a_1^6.
\end{aligned}
$$

This identity was evaluated exactly, rather than inferred from sampled
values.

## Exact sign certificates

Every reduced rational expression has a denominator equal to a positive
integer times a power of

$$
16\alpha+12\beta+9.
$$

In particular,

$$
\operatorname{den}(\Delta_1^+)
=93002175(16\alpha+12\beta+9)^{16}.
$$

Its value at the origin is the explicitly checked positive integer

$$
172334907882131965754175.
$$

Thus the denominator is strictly positive on the entire closed quadrant,
including both axes and the origin.

The exact expanded numerator facts are:

| quantity | total degree | nonzero terms | sign of every coefficient | zero set on $\alpha,\beta\geq0$ |
|---|---:|---:|---|---|
| $\mu_0$ | 3 | 9 | positive | origin only |
| $\mu_1$ | 6 | 25 | positive | origin only |
| $\mu_2$ | 9 | 49 | positive | origin only |
| $\mu_3$ | 12 | 81 | positive | origin only |
| $\Delta_1$ | 12 | 81 | positive | origin only |
| $\Delta_1^+$ | 18 | 169 | positive | origin only |

The zero-set statement requires slightly more than coefficientwise
nonnegativity.  In every case the constant coefficient is zero, while both a
pure positive power of $\alpha$ and a pure positive power of $\beta$ occur
with positive coefficient.  Hence the polynomial is positive in the open
quadrant and on either positive axis, and it vanishes only when both
parameters vanish.  The certificate records this boundary-stratum check
explicitly.

At $(0,0)$ only the readout block moves.  The feature curve is linear,
$F(s)=27s$, so $K$ is constant and all four nonconstant moments vanish.  The
common zero at the origin is therefore expected, not an algebraic accident.

The observed term counts $9,25,49,81$ for $\mu_0,\ldots,\mu_3$ form the
finite pattern $(2r+3)^2$.  This may reflect a useful support geometry, but no
all-order claim is made from four cases.

## Independent MFP checks

The computation used two routes with different terminal organization.

1. `bivariate_reference.py` retains the whole labelled forest and computes
   the terminal Wick expectation directly.  It is deliberately restricted
   to low order.
2. `sector_wrapper.cpp` invokes the audited connected-tree recursion.  Each
   pair $(w,a)$ is evaluated in a separate process with checked unsigned
   512-bit arithmetic.  Bridge removal, exact binomial Leibniz convolution,
   and vertex-partition Wick evaluation are inherited without semantic
   modification from the accepted sector engine.

The routes agree on every bivariate coefficient through order five.  That is
3 coefficients at order one, 9 at order three, and 18 at order five.  They
also agree at the preselected off-diagonal point $(2,3)$ and at the additional
points $(3,1)$, $(0,1)$, and $(1,0)$.

An independent hostile audit reconstructed all five odd jets directly from
the 125 atomic sector files, without trusting the merged result.  It then
recomputed the four moments and both determinants from the displayed
formulas, checked every coefficient table, verified the complete sector
manifest, rebuilt the production binary, and reproduced the Campaign-1
diagonal identities exactly.

## Resource and durability record

The production computation respected the preregistered limits:

| measurement | value |
|---|---:|
| atomic exact sectors | 125 |
| cumulative production wall time | 1131.036 s |
| cumulative wall cap | 1800 s |
| virtual-memory cap per sector | 4 GiB |
| highest derivative | 9 |

Every sector was atomically written and hashed before the next was run.  The
full sector directory is only about 50 KiB and is intentionally retained as
durable exact evidence.  Resident peak memory was not separately measured;
the reported 4 GiB figure is the enforced virtual-memory limit, not an RSS
measurement.

The durable test suite has twelve tests.  It includes clean compilation from
source, exhaustive production-versus-reference comparison through order
five, exact off-diagonal gates, all 125 sector identities and hashes, exact
certificate replay, denominator-at-origin checks, diagonal Campaign-1
identity, and provenance hashes.

## What this campaign establishes—and what it does not

Established:

- the exact two-parameter output jets through order nine;
- strict positivity of all four accessible moments off the degenerate
  origin;
- strict positivity of the first ordinary and first shifted $2\times2$
  Hankel determinants off the origin;
- all these signs uniformly over the complete unbounded quadrant
  $\alpha,\beta\geq0$;
- exact compatibility with both the canonical point and the full earlier
  diagonal metric family.

Not established:

- positivity of higher Hankel determinants;
- an all-order Stieltjes representation for any or all metric points;
- moment determinacy;
- a representing measure varying regularly with $(\alpha,\beta)$;
- identification of the formal kernel with the actual global mean-field
  trajectory.

The principal conclusion is therefore finite but strong: the first shifted
test did not merely survive a few additional numerical settings.  It survives
as an exact algebraic inequality on a genuine two-dimensional, unbounded
family of block metrics.

## Durable artifacts

- `PROTOCOL.md`: frozen object, gates, cap, and claim boundary.
- `sectors/`: all 125 atomic exact sector outputs.
- `results_order9.json`: complete merged bivariate jets and sector manifest.
- `certificates_order9.json`: exact moments, determinants, coefficient tables,
  denominator checks, and boundary zero-set certificates.
- `bivariate_reference.py`: transparent low-order whole-forest oracle.
- `sector_wrapper.cpp`: isolated production entry point.
- `run_sectors.py`: checkpointed, cumulative-budget sector runner.
- `postprocess.py`: exact formal inversion and quadrant certificates.
- `provenance_order9.json`: commands, hashes, limits, measurements, and gates.
- `test_*.py`: reproducible acceptance and clean-checkout tests.

