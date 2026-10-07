# Independent reconstruction of the noisy Taylor source

2026-10-06. Bounded independent mathematical review, conditional on the
inherited scientific source and fitting events. No experiment, Git operation,
maintained-file edit, author history, or other review was used. This report
concerns the physical source and its local compiler interface, not a complete
decoder. It was frozen before any subsequent assembly audit by this reviewer.

## Verdict

**The exact-arithmetic noisy physical-source argument reconstructs.** The
matrix-noise precision, activation-value precision, Taylor degree, and
initialized-call bounds (1), (2), and (30) follow under the stated inherited
events and gates. The causal coefficient cap, centered composition estimate,
and activation-arithmetic count in Section 8 also reconstruct.

**The final parameter simplification in (39) needs a qualification.** Its
first bound retains `log(e+R)`, whereas the source's `Z` does not contain an
input-dimension or sample-count logarithm. The supplied material does not
explicitly justify absorbing both into that `Z`. The safe operation bound is

\[
 \chi_{\rm local}\le
 C\{B(1+r)Z+\log(e+m+d)\}.
\]

Equivalently, retain the first bound in (39), enlarge `Z` by
`log(e+m+d)`, or cite an applicable deterministic input-size gate. This is a
parameter-accounting qualification, not a failure of the physical forcing
argument. The finite-arithmetic realization is supported with the endpoint
rounding clarification below and its explicitly retained input-description
cost. No conclusion about a globally expanded row function or the full
unseen-query decoder is certified.

## Frozen inputs and scope

All six scientific files below were read completely. Hashes were checked at
the start and again before writing this report where an assigned hash existed.

| Input | SHA-256 |
|---|---|
| `FAST_TAYLOR_NOISE.md` | `57487cc133f4868c485bba535735be5feb9559589e72896262a416104ba992a0` |
| `SANE_TAYLOR_SOURCE.md` | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `PHYSICAL_NOISY_PROGRAM_BRIDGE.md` | `b20650d28fe3a4c8ebc76105bd5f4347503bd0485bcced588dd1680bc65cadc6` |
| `NOISY_TWO_ORIENTATION_TRANSCRIPT.md` | `0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac` |
| authorized `../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md` | `f3e277e9591be6e48357a13217927c05bcc2c59843a26a3fa5423ae5afc4c7d8` |

Shared `AGENTS.md`, the requested research and rigorous-proof skills, the
canonical-notation skill, its neural-network reference, and the adversarial
audit reference were read. Linked scientific sources outside the assignment
were not retrieved. In particular, this review accepts the supplied Gaussian
source event as an interface; it does not independently prove its insertion
or fitting theorem.

## Reconstruction of the physical argument

Use the source notation: `r=m/gamma`, `Y=||y||_2/sqrt(m)>0`,
`S=16Yr<=1`, `ell=log(en)`, and `B=beta^(100L)`. The evolving
parameter displacement is measured by

\[
 \|u\|=\|A-A_0\|_F/\sqrt n
       +\sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F
       +\|w\|_2/\sqrt n.
\]

The normalized state is `bar u=u/Y` and normalized time is `tau=t/r`.
Residuals remain `r_a=f_n(v_a)-y_a`; backward carriers and gates are
residual-free. These conventions give precisely the three physical gradient
formulas (5), including the hidden-layer factor `1/n`.

In the coordinates
`Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)`, the physical gradient
is `-(2/m) sum_a r_a grad_Theta(n f_n(v_a))`. Hence the displayed
response identity in Section 2 contains `2r/m`, with no missing `n` or
label factor. The supplied response maximum and residual RMS `2Y` give

\[
 \|\partial_\tau z^{(j)}\|_\infty
 \le4YrS U_{\rm fin}\sqrt\ell
 =\tfrac14 S^2U_{\rm fin}\sqrt\ell.
\]

Multiplication by `4h_j`, `U_fin<=beta^(72L)`, and the chosen step
bound proves (13). Parameter movement and forward computational defects
each contribute less than the stated scalar-disk slack. The needed scalar
domain is centered at a computed real preactivation, so no estimate raises
that potentially large real center to the interpolation degree.

For one patch, freeze the actually realized answer errors into
`N(xi)=sigma sum_(k<K) zeta_k xi^k`. Their RMS on `|xi|<=4` is at
most `2 sigma sum_(k<K)4^k <= sigma 4^K`. This is a proof device.
At coefficient order `k`, formal composition uses only state coefficients
already computed and noise coefficients of order at most `k`. The frozen
polynomial activations, their derivatives, and the same physical gradient
formulas therefore define a holomorphic nonautonomous field whose Taylor
recurrence is exactly the noisy recurrence. No future noise is needed to
select an earlier query or interpolation center.

Forward subtraction has RMS defect at most `beta^(4L) delta`.
Backward subtraction needs one reference carrier maximum: split a gate
difference times the reference carrier from the new gate times the carrier
difference. The reference maximum enters once in the layer induction.
Its additive backward noise need not itself contain `S`; condition (22),
which is proportional to `S`, ensures the perturbed carriers stay within
the allowed cap. The pre-normalization field bound recorded in Section 4
then gives

\[
 \frac rY\,C\beta^{80L}
 [Y(1+S\sqrt\ell)+S+S^2]\delta
 \le C\beta^{80L}(1+r)^2\sqrt\ell\,\delta.
\]

Here `S/Y=16r` removes the apparent inverse-label loss. The larger
`C_N=B^2(1+r)^2 sqrt(ell)` safely dominates it. For a Jacobian,
normalizing the state cancels the amplitude normalization, leaving the time
factor `r`, not `r/Y`. The first two activation derivatives and the same
carrier/residual bounds consequently give `2 Lambda_j`. This argument does
not require differentiating an interpolation center as the physical state
varies: centers are frozen within the local field.

The contraction in (24) maps the `d_n/2` ball into itself and has factor
at most `8h_j Lambda_j<=1/4`. Subtracting the true field first gives
the better stability exponent `Lambda_j`, despite the perturbed field's
`2 Lambda_j` Jacobian bound. Cauchy on the radius-`2h_j` circle
then produces (26). The multiplier is
`1+2h_j Lambda_j+2*2^(-K)`, so multiplying it over patches costs
at most `exp(2E+1)`. The stated choices of `K` and `delta` leave
more than the claimed `epsilon/8` slack. The block-parameter error is
`Y` times this normalized error; output sensitivity and the inherited
tail give the claimed parameter-defined, all-time sphere approximation.

## Interpolation and finite arithmetic

The contour argument in Section 3 is valid. After subtracting `phi(x)`,
the contour value bound is `4 beta alpha`, while the nodal product ratio
is at most `2^(-J)`. The sum of absolute Lagrange weights is at most
`5^J`. Two Cauchy differentiations cost `alpha^(-2)`, and
`alpha^(-1)<=beta` gives exactly the `C beta^2` envelope in (16).
Thus (17) supplies values and two derivatives on the required disk with
`O(J+log(delta^(-1))+log(beta))` value bits. The real mesh construction
is continuous and `3 beta`-Lipschitz; it does not assume continuity of
the underlying rounded evaluator.

The local arithmetic precision argument has the needed structure. A
principal coefficient error can be frozen at its node as a polynomial
defect. An integrated-state coefficient error `e[k+1]` contributes the
velocity coefficient `(k+1)e[k+1]/h_j`. Learned rank-factor errors are
controlled by the two-factor product subtraction and polynomially many
summands. Normalization costs at most `1/Y<=n`; even an arbitrary hidden
matrix coordinate defect costs a further factor `n` in Frobenius norm.
The stated `(n+1)^3` and polynomial factors in (31a) therefore leave
ample room. Equal patch lengths prevent a tiny last-step reciprocal.
Centered interpolation and the coefficient norm bound prevent an
unjustified `J log(n)` working-precision cost.

There are three minor corrections to the literal exposition:

1. At line 392, replace “(21) is at most delta” by “the RMS bound in
   (21) is at most delta.” The chosen `sigma` ensures
   `sigma 4^K<=delta/4`; it does not ensure
   `sqrt(n) sigma 4^K<=delta`. The proof already uses the correct
   coordinate bound `sqrt(n) delta`, so its conclusion is unaffected.
2. At lines 642–644, an independently rounded endpoint is not literally
   obtained by adding constant forcing to the same nonlinear field while
   preserving its previously computed polynomial. The direct exact remedy
   is to add its norm as an endpoint defect to (26). Choosing this defect
   at most `h_j eta` changes only the numerical coefficient of
   `h_j eta`. The lower bound on `h_j` and (31a) already pay for this.
3. Implementing (36) literally may need one extra call to `A_phi(x)`
   per center when zero is not an interpolation node. Thus the earlier
   exact `2nmLHJ` routine-call count becomes at most
   `2nmLH(J+1)`. Alternatively choose odd `J`, so zero is a node.
   No precision, source-vector, or asymptotic work bound changes.

## Gaussian chronology and local compiler interface

All labels, orientations, and query coefficients depend only on the
external first-layer Gaussian columns and observed answers. Raw noises are
not separately exposed. The exact posterior theorem therefore applies,
including adaptive interlacing of matrix labels and orientations. Freezing
future coefficients for a pathwise proof does not alter that filtration.
The raw-noise event costs at most `R exp(-cn)`. Innovation caps must
remain the larger polynomial-in-`sigma^(-1)` caps (32); the note correctly
does not assume small innovations conditional on the full matrix tape.

The sequential budget map (33) is causal, fixes every sequence of total
absolute mass at most its budget, and has the claimed factor-two `l1`
Lipschitz bound. Before the first saturation index both outputs agree with
their inputs; the discrepancy in remaining budgets is bounded by the prefix
error, and the displayed sign split bounds the entire remaining output
tail by another copy of the input discrepancy. Thus the argument is
dimension-independent. Cauchy's coefficient estimate makes this cap
inactive on the good program with strict slack.

The centered interpolation representation and truncated-convolution
telescoping estimate give (38). In particular, the geometric factor
`2/8<1` controls the whole activation/gate composition, rather than
raising a raw `sqrt(n)` coordinate cap to degree `J`. Polynomially
many terms and gapped one-call posterior formulas prove the first bound
in (39). This is an operation-level statement only; recursive substitution
can still accumulate a factor proportional to the number of phases in the
logarithmic sensitivity.

For the last inequality in (39), (2) only implies

\[
 \log(e+R)\le C\{Z+\log(e+m+d)\}.
\]

An input-size gate may allow further absorption, but it must be supplied.
For example, a first-layer dot product has maximum-coordinate Lipschitz
constant `||v||_1`, which can be `sqrt(d)` for a unit input; a raw
coordinate cap alone does not remove this input-size dependence. Section 6
already retains a logarithmic input-description exception, whereas (39)
does not. This review does not declare the stronger absorption false under
every possible inherited gate; it is not established by the explicit
assigned interface.

Finally `J<=CK` follows from the chosen tolerances, and
`H>=64B(1+r)T sqrt(ell)` dominates every term in `K`.
Consequently `K<=CH<=C mLH`, proving
`mLH K^3<=C(mLH K)^2<=CR^2`. This counts activation arithmetic per
row. It excludes value-routine work, bit cost, posterior arithmetic, and
the cost of expanding an entire history. The report certifies no stronger
interpretation.

## Narrow correction check after the original report was frozen

The original report above was frozen at SHA-256
`572f852ed624940ceb4ffe40716e0a99d53b87d143768e25fef422be95334745`.
The supervisor then requested a narrow recheck of corrections to the source,
whose new SHA-256 is
`71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c`.
This addendum checks those stated changes only, using the original source
scope and the elementary inequalities below. It does not import results
from the separately requested assembly audit or change the frozen review
history above.

All four recorded issues are resolved in the corrected source: its `Z`
now contains `log(e+B(1+r)(m+d+2))`; the forcing premise specifies the
RMS bound; endpoint rounding is an additive endpoint defect; and the value
call count allows `J+1` samples per center. The enlarged `Z` bounds
`log(e+R)` directly from (2), so the last inequality in (39) is now
supported without an unstated input-size gate.

The additional finite ceiling rule is also valid. If `x=T/h>1` and a
certified rational upper bound `u` satisfies `x<=u<=x+1/4`, then
`H=ceil(u)` satisfies

\[
 \lceil x\rceil\le H\le\lceil x\rceil+1,
 \qquad x\le H<x+5/4<3x.
\]

Consequently `h/3<T/H<=h`; an exact equality decision for `x` is
unnecessary. Every source-disk and left-sum upper bound persists, while
`h_j^(-1)` changes by only a universal factor. The lower bound on `H`
used for `K<=CH` is unchanged. No resource exponent or label allowance
changes. The corrected source passes this bounded reconstruction, with the
same inherited-event, evaluator-interface, and source-only limitations.
