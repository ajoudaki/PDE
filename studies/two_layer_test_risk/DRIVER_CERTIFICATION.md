# Complete enclosure assembly for the fixed matched-loss coefficient

Author: coordinator, 2026-09-10. This document specifies how the retained
`certificate_driver.py` and `certificate_kernel.cpp` combine the proved
analytic bounds. It is part of approach B. Until an executed, checked
enclosure excludes zero, it asserts no sign.

The mathematical input is precisely CUBIC_DERIVATION (13)--(19), with the
original two lower Gaussian roots, three fixed training labels, four named
upper slots, and zero passive weight. The operative exact coefficient and
actual-flow remainder are unchanged. The preceding diagnostic arrays do not
enter this calculation.

## Input constants and outward intervals

An interval has rational endpoints. Each elementary interval operation first
computes its endpoint extrema in Python integer/Fraction arithmetic, then
rounds the lower endpoint down and the upper endpoint up to multiples of
`2^-96`. Thus rounding in this layer enlarges the enclosure explicitly.
Addition, negation and multiplication use the endpoint sum/sign/product
rules. Reciprocal is used only for an interval with strictly one sign, and
division multiplies by its reciprocal. The general nonnegative-integer
power uses repeated interval products, preserving enclosure even when this
overestimates a square near zero. No floating-point comparison decides an
interval's mathematical sign.
An exact rational scalar is multiplied into the endpoints before outward
rounding. In particular the tiny Taylor coefficients are not first widened
to the absolute dyadic grid and then multiplied by large powers. A preflight
audit caught that inefficient ordering before any coefficient run; the
corrected order and an explicit trigonometric-width gate are independently
tested and preserve the same rigorous interval semantics.

Pi is enclosed by

\[
 \pi=16\arctan(1/5)-4\arctan(1/239).
 \tag{D1}
\]

For each arctangent the producer sums the first 64 terms of its alternating
power series exactly and encloses the remainder by the next positive term.
This series follows by integrating the geometric series for `1/(1+x^2)`;
the integrated remainder has the sign and bound of that next term.
For completeness, the tangent addition formula gives
`tan(4 arctan(1/5))=120/119` and
`tan(4 arctan(1/5)-arctan(1/239))=1`. The angle is between zero and pi/2,
so it is pi/4. This proves (D1), not merely a numerical pi assumption.
The resulting rational interval is checked to lie inside `(25/8,22/7)`.

Square roots of positive rational endpoints are bounded by integer square
roots after multiplication by `2^192`. If `a=floor(sqrt(v)*2^96)`, then
`a/2^96<=sqrt(v)<(a+1)/2^96`; flooring the rational argument before the
integer square root gives that same integer a. Endpoint monotonicity then
encloses `sqrt(5)` and `1/sqrt(2pi)`. Labels are the exact intervals for
`p=(1/3,(1-sqrt(5))/12,(1-sqrt(5))/12)`. Their absolute sum is checked
below `P=27/50`. The binary64 labels passed to the kernel are independently
checked against the same P bound. The sum of their individual interval
deviations is denoted `epsilon_p`.

For every circle node and training angle, sin and cos are enclosed by their
Taylor polynomial of degree 79. The actual nonzero terms are summed using
the outward interval operations above. Every argument has absolute value
at most five, including `3 alpha`. The real Taylor remainder is at most
`5^80/80!`, since every real derivative of sin or cos is bounded by one.
This covers both the polynomial truncation and uncertainty in its argument;
no library trigonometric error assumption enters the proof. The binary64
values passed to the kernel are treated as exact dyadic constants, whose
errors are subsequently charged through their covariance discrepancy.

The normal-density constant passed to the kernel is checked to differ from
the exact `1/sqrt(2pi)` by less than `10^-15`. Received binary64 inputs are
echoed by the kernel as their integer IEEE bit patterns and compared with
the intended inputs. Reported primitive sums are also returned as bits;
the driver converts those bits to exact dyadic rationals before enlarging
them by error intervals. Thus decimal parsing or printing is not an
unexamined precision assumption.

## Certified grid selection before integrand evaluation

For either specified dyadic root matrix A, let
`c_j=max_i |A_ij|`, in exact rational arithmetic. For the preregistered
exponent target `B=26`, put

\[
 a_j=\min\{7,3/(4c_j)\},\quad
 h_j^*=\frac{6a_j}{B+a_j^2/2},\quad
 h_j=2^{-10}\lfloor2^{10}h_j^*\rfloor,
 \quad m_j=\lceil8/h_j\rceil.
 \tag{D2}
\]

When `c_j=0`, take `a_j=7`. A zero fourth upper column can instead be
omitted exactly. All retained axes must pass
`0<h_j<=1`, `1<=m_j<=200`, `8<=m_j h_j<=9`. The dyadic spacings are
exactly representable. The driver additionally verifies, by rational
comparison,

\[
 c_ja_j\le3/4<\pi/4,\qquad
 6a_j/h_j-a_j^2/2\ge B,\qquad h_j^2\le18/B.
 \tag{D3}
\]

Since pi>3, these imply the strip exponent and Gaussian-mass bounds used
in CERTIFIED_ERROR (E1)--(E5), with truncation radius at least eight.
They require no accuracy guarantee for a transcendental grid calculation.
In at most four dimensions the resulting analytic error envelope is

\[
 e_{\rm rule}\le 5\,10^{-11} M_{\rm strip}
                         +6\,10^{-15}M_{\rm real}.
 \tag{D4}
\]

The proof and finite rational exponential lower bounds are in
CERTIFIED_ERROR. The same inequalities with the conditionally authorized
target B=30 allow the envelope `10^-12 M_strip` when
`M_real<=M_strip`. The actual floating-point sums are not normalized to
unit Gaussian mass. Training moments computed with three roots are
bounded by the same conservative four-dimensional envelope; they must
not be artificially multiplied by a passive rule mass.

Grid selection depends only on the specified root-column sizes and the
predeclared target. It does not use the value or sign of the coefficient.
The slight rational conservatism relative to (E5) changes work, not the
theorem or error envelope.

## Enclose the two Gaussian laws and all primitive moments

Each reported primitive is enlarged first by `10^-9`, the proved arithmetic
envelope in CERTIFICATION_ENGINE. The checked kernel input and compiler
contracts are retained in the run. KERNEL_REVIEW and the deterministic
kernel test provide independent verification, separately from that proof.

For the lower law, the exact input directions are enclosed as above. Their
original Gram G is obtained by interval dot products. The actual dyadic
directions `u_hat` used in the sum have exact rational Gram
`G_hat=u_hat u_hat^T`. Let `epsilon_G` enclose the maximum entry difference.
Both matrices are positive semidefinite, including the original singular G.
The covariance perturbation proof CERTIFIED_ERROR (E6)--(E8) gives these
primitive radii in addition to arithmetic and analytic rule error:

| Lower primitive | Strip / real bound | Covariance-error radius |
|---|---|---|
| `Q_ij=E[h_i h_j]` | `1 / 1` | `2 epsilon_G` |
| `L_ab=E[e_a e_b]` | `4 / 1` | `3 epsilon_G` |
| `T_abij=E[e_a e_b h_i h_j]` | `4 / 1` | `9 epsilon_G` |

The producer retains all entries, including the response tensor. Their
intervals enclose the true lower expectations, rather than moments for a
whitened or independent-sample substitute.

For the upper law, ordinary floating-point linear algebra chooses a convenient
four-by-four matrix `A_hat` whose training rows have zero fourth column.
These calculations are **not** used as a theorem that its covariance equals
Q. Treat its stored entries as exact dyadic numbers and form
`Q_hat=A_hat A_hat^T` exactly. This matrix is positive semidefinite by its
construction. Let `epsilon_Q` enclose its largest entry discrepancy from
the already certified lower Q intervals. This directly charges any error
in the solve, square root, covariance conditioning or clipping of a tiny
negative conditional variance. No inverse of the true passive covariance
appears in a proof, and no smoothness of the selected factor is needed.

With `H_i=tanh(Y_i), d_i=tanh'(Y_i), dd_i=tanh''(Y_i)` and
`S=sum p_a H_a`, the table specifies each additional radius. Row names
are exactly the kernel output groups. The column labelled p-error charges
the difference between the dyadic supplied labels and the exact labels.

| Group | Exact expectation | Strip / real bound | Price radius | p-error |
|---|---|---|---|---|
| ES2 | `E S^2` | `P^2 / P^2` | `2P^2 epsilon_Q` | `2P epsilon_p` |
| V, dynamic_V | `E S^2 d_a d_b`, `E S^2 d_x d_b` | `4P^2 / P^2` | `9P^2 epsilon_Q` | `2P epsilon_p` |
| ddgram, dynamic_dd | `E d_a d_b`, `E d_x d_a` | `4 / 1` | `3 epsilon_Q` | `0` |
| ESdd, dynamic_ESdd | `E S dd_a`, `E S dd_x` | `4P / P` | `5P epsilon_Q` | `epsilon_p` |
| dynamic_C | `E H_x S d_a d_b` | `4P / P` | `9P epsilon_Q` | `epsilon_p` |
| dynamic_Hdd | `E H_x dd_a` | `4 / 1` | `5 epsilon_Q` | `0` |
| dynamic_SH | `E S H_x` | `P / P` | `2P epsilon_Q` | `epsilon_p` |

Each radius is the sum of its arithmetic, rule, Price and p-error terms.
The Price constants follow by expanding the finite label sums in (E8).
For p-error, `|S-S_hat|<=epsilon_p`, and
`|S^2-S_hat^2|<=(P+P)epsilon_p`; all other real factors have magnitude
at most one. Both label sums are checked below P, so the same constants
apply. This error analysis does not suppress a matrix-response mean.

## Exact contraction and matching subtraction

The interval assembly uses training-only indices a,b,i,j and passive x=3.
Define

\[
 M_{bj}=p_j E[d_jd_b]+\mathbf1_{j=b}E[Sdd_b],
\]
\[
 D_{ab}=L_{ab}V_{ab}+\sum_{i,j}T_{abij}M_{ai}M_{bj},
 \quad \mathcal A=\sum_{a,b}p_ap_b(G_{ab}D_{ab}+Q_{ab}V_{ab}).
 \tag{D5}
\]

All factors in these equations have the enclosing intervals above.
The producer verifies `B0=E S^2` has a strictly positive lower endpoint,
then encloses `beta=8 mathcal A/(3B0)`. It must verify the resulting
interval lies in `[-1/10,1/10]`, which closes the explicit hypothesis
of ANGULAR_CERTIFICATE. Training quantities are recomputed within each
node's primitive rule; all resulting beta intervals enclose the same
exact number and must overlap. Their intersection is recorded as an
additional consistency check. Each independently valid node interval is
used for its own clock term, so this intersection is not needed to repair
an invalid summand.

For the passive coefficient, the implemented formulas are exactly
ANGULAR_CERTIFICATE (A6)--(A7): `J_x=4F_x+(4/3)B_x`,
`a_x=2 E[S H_x]`. In particular, both the `p_i E[d_i d_x]` and
`E[S dd_x]` response terms enter F, and both `E[d_x d_a]` and
`E[H_x dd_a]` response terms enter B. These are the explicit contraction
of both directions of the same initialized matrix, not an independent
Gaussian replacement. The unweighted input Gram G remains the true
correlated rank-two Gram; labels p carry the mean-loss normalization.

The exact symmetry-reduced periodic mean is enclosed by the interval sum

\[
 C_N=\frac2{256}\,2[J_0-\beta a_0]
 +\frac4{256}\sum_{j=1}^{63}
 2\cos(6\pi j/256)[J_j-\beta a_j].
 \tag{D6}
\]

The teacher factors are certified trigonometric intervals. The raw teacher
projection and clock subtraction are separately saved, as is their difference.
Adding `[-10^-6,10^-6]` to the nodal enclosure covers the remaining circle
error by ANGULAR_CERTIFICATE. This produces an enclosing interval for the
exact chi, including every stated approximation axis.

## Decision and finite-time consequence

Only a strictly positive lower endpoint or strictly negative upper endpoint
decides the sign. All comparisons use exact rational endpoints. A zero-crossing
interval is inconclusive. No coarse/fine agreement or empirical confidence
level enters this decision. The final claim remains conditional on inspection
of the full mathematical and executing source, rather than trusting a flag.

If the certified lower endpoint is c>0, combine it with the already proved
`|Delta(t)-chi t^3|<=M t^4` on `[0,T]`. Then for
`0<t<=min(T,c/(2M))`, one has `Delta(t)>=c t^3/2>0`.
The negative case is identical after reversing signs. T,M retain their
original fixed-model, width-independent local scope; no evaluated time
radius or quantitative width rate is added by the certificate.

## Reproduction and ownership

The source command, run only after component audits, is

```sh
python -B studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_20260910_01
```

The output directory must be fresh and inside this study's generated namespace.
It receives the compiled binary/log, exact constants, complete primitive input
text and output bits for every angle, root/error evidence, nodal intervals,
aggregate interval, source hashes, runtime, compiler and Python/NumPy versions,
and exit status, including failures. NumPy only proposes a root factor whose
covariance error is explicitly enclosed; its floating accuracy is not assumed.
Every bulk operation is on CPU, with a one-process calculation and fixed
per-call/overall resource limits. No network parameters are trained.

Root owns this proof, the driver, final synthesis and sole Git transaction.
Other agents own their original arithmetic, integration and audit sources.
The source contracts and complete scientific dependencies are unchanged
from the checked previous study except for this new coefficient enclosure.
