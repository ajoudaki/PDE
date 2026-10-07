# Author-style reconstruction of the Taylor-source assembly

2026-10-06. Bounded assembly audit, not a fresh independent review and not
promotion. The lead supplied suggestions during this phase, and revisions
were discussed with the lead. This report is explicitly separate from the
previously frozen independent source reconstruction in
`FAST_TAYLOR_NOISE_CHECK.md`.

## Verdict and scope

**PASS for the conditional assembly stated in `FAST_COMPOSITION.md`, at
SHA-256 `77f5deaffcd7133e6bafb0c1b2e8cf216399bbf787503812e8667ea2e5da53cc`.**
The source-to-core interface, physical versus normalized noise convention,
passive statistical transport, coordinatewise-median schedule, and displayed
resource substitutions reconstruct. The revised Section 7 supplies actual
transport arguments; it does not merely restate a passive-query premise.
No unresolved interface gap was found in this bounded audit of that version.

This is a conditional-on-inherited-results verdict. It retains the complete
source/fitting label intersection and scientific good events, the original
eventual-width qualifications, the nonzero-label gate `nY >= 1`, the
sampling gate, the supplied evaluator costs, and the original comparison
with the dense-pair accuracy certificate. It is not a new independent proof
of the inherited local source theorem, dense-center theorem, or the query
generator theorem. In particular it is not a full-decoder promotion verdict.
The query uses a width-order statistical block, not logarithmically many
samples. The finite-bit representation has logarithmic power `17/2` in
the displayed envelope, not the proposed fourth/fifth-power target.

Two substantive distinctions were necessary during reconstruction:

- A physical noisy backward action and a label-normalized noisy backward
  action at the same nominal noise scale are different observations. The
  final assembly keeps the former and normalizes its observed fields only
  afterwards.
- A finite-training-panel complex radius cannot be substituted for the
  whole-sphere radius. Nor can one shorten the activation strip without
  rechecking the label allowance. The final assembly avoids both moves:
  it integrates the original real whole-sphere response estimate.

These are repaired in the checked version. The source-only report has not
been revised using any assembly argument.

## Inputs and reading boundary

All the following assembly inputs were read completely. Unless explicitly
qualified, paths are in `studies/unseen_query_decoder_20261005/`.

| Input | SHA-256 |
|---|---|
| `FAST_COMPOSITION.md` | `77f5deaffcd7133e6bafb0c1b2e8cf216399bbf787503812e8667ea2e5da53cc` |
| `FAST_TAYLOR_NOISE.md` | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `SANE_METRIC_PACKETS.md` | `1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea` |
| `FAST_UNIFORM_QUERY.md` | `e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9` |
| `COMPILER_PARAMETER_ACCOUNTING.md` | `00c017e1b39e96de79ca062b207514cef5cb045507f7cef4ed4975b69fa07c6e` |
| `RECALIBRATION_FREE_MOMENTS.md` | `710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea` |
| `COST_CONTRACT.md` | `3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c` |
| `DENSE_BUDGET_GEOMETRY.md` | `50950e2df4d5d9e9eb20201769da7afee39ef2dee389f1ab97744a25ef88df0e` |
| `SOURCE_SUPREMUM_EXTENSION.md` | `8623e2d8adaf3b730274dd704fcbd44533a67fe67d47e18ce38701b7d6cb6a6f` |
| Authorized `studies/integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md` | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |

The original source assignment also authorized and completely read
`SANE_TAYLOR_SOURCE.md`, `PHYSICAL_PARAMETER_ACCOUNTING.md`,
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`, `NOISY_TWO_ORIENTATION_TRANSCRIPT.md`,
and the integrated `GENERAL_TRAJECTORY_LOWER_BRIDGE.md`; their hashes and
source-only conclusions are recorded in `FAST_TAYLOR_NOISE_CHECK.md`.
The latter report, including its narrow source-correction addendum, is
frozen at `96aee21ba4522d11f49965a0c4b948fed79432ee3840b3eb97d19d885c453f66`.

No other reviewer report, study README/history, experiment, Git operation,
or maintained-file edit was used. Required research/proof/notation skills
were applied. The notation discipline matters here: residual RMS, physical
backward fields, normalized row fields, numerical caps, and statistical
caps have different roles and are not interchanged.

## 1. Taylor source to the causal row compiler

Write `r=m/gamma`, where `m` is the training sample count and `gamma` the
feature-Gram gap. Let `R` count named fields/actions and let `Theta` bound
local numerical logarithms. Use the assembly's

\[
 Z=\log(en)+\log\!\left(e+
 (m+d+2)\beta^{100L}(1+r)/\delta\right).
\]

This `Z` includes dimension, confidence, and activation/depth factors; it
is not the smaller original source-local expression. The corrected source
also includes its previously missing `log(m+d)` term.

For `H` patches and order `K`, the principal forward and backward
coefficient vectors, initialized-matrix images, residual-weighted backward
coefficient vectors, and required Gaussian/activation fields number
`O(mLHK+d)=O(R)`. Real activation samples are row fields. They do not make
every scalar arithmetic operation a new acquired field.

A learned matrix coefficient contains `O(mLHK^2)` scalar rank weights.
This does not require that many distinct output vectors: terms with the
same output factor are grouped. The application of a learned matrix is a
linear combination of at most `CR` distinct row fields, with coefficients
prepared from acquired pair moments. No per-row dense matrix or matrix
inverse has been introduced.

The empirical quantities remain pair reductions. These include the
readout/residual convolutions, history/query/innovation Grams, and the
Frobenius contractions of learned rank sums. The latter are scalar sums
of products of pair moments, not new empirical fourth moments. Naming a
residual-weighted backward field before acquiring its pairs is legitimate
because its residual weights are already causal scalar arguments.

The chronology runs coefficient order by coefficient order, with forward
layers increasing and backward layers decreasing. A field retains the
scalar arguments from its creation phase; later scalar updates do not
retroactively alter it. There are at most `CR` phases. Acquiring all pairs
of current fields in parallel does not multiply this count by the number
of pairs. The resulting graph sensitivity is `exp(CR Theta)`.

Section 8 of the corrected source supplies the necessary *local*
certificate. Its causal coefficient cap is 2-Lipschitz in coefficient
`l1`; centered series composition uses a bounded coefficient increment
and costs `O(J+log K+log beta)` in the logarithm of its local Lipschitz
constant. It does not raise a coordinate cap of order `sqrt(n)` to the
Taylor order. Furthermore `NK^3 <= C(NK)^2 <= CR^2` for
`N=mLH`, since `K <= CH <= CN`. Thus the claimed per-row scalar arithmetic
bound and the core's local-map convention agree.

The selected metric construction requires its specified exact-product
dyadic reduction: first round operands, multiply exactly on their common
finer grid, and then perform the scalar reduction/rounding. With at most
`R` selected packets, the bilinear error amplification contributes only
`O(log R)` guard bits. There is no inversion of the retained metric and
no assumed spectral gap for a history Gram. `O(R^2)` retained words at
`CR Theta` bits each give `CR^3 Theta` retained bits.

## 2. Keep the physical observation law

The source observes physical actions

\[
                  W^\top u+\sigma\zeta,
\]

with the physical backward vector `u`. A construction observing
`W^top(u/Y)+sigma zeta` has different signal-to-noise ratios. The normalized
compiler convention cannot be identified with the physical source tape.

The final assembly resolves this correctly. Posterior conditioning always
uses the physical source queries and answers. Dividing an already observed
field by the known nonzero label RMS `Y` is deterministic processing, not
another initialized-matrix observation. Normalized pairs remain pairs of
named fields. On the inherited gate `nY >= 1`, the new amplitude and local
Lipschitz costs are at most `n`, hence only `O(log(en))` additional
numerical logarithms. The gate is visible; no inverse-label power is
silently placed in a universal constant. Raw-label acquisition,
normalization accuracy, and output-scale encoding remain explicit costs.

Fresh passive noise can have a smaller known positive variance. The
conditioning formula uses the original training variances, and numerical
floors use the stated minimum of the training/query scales. Adding
`C[log(en)+L log beta]` bits to the fresh query noise precision is absorbed
by `Theta`. Raw answer noises and private selected packets are never
added to the observed conditioning sigma-field.

## 3. Why the passive statistical interface transports

Prediction closeness alone would not establish this interface. It also
needs a small cap for completed passive fields, a controlled conditional
mean mixer, and the finite-rank/common-Gram normal form. The final
Section 7 supplies each one as follows.

### 3.1 Actual feature caps preserve the full label class

Set `S=16Yr <= 1` and let `rho(t)` be residual RMS. On the inherited
real fitting event, `rho(t) <= Y exp(-t/(4r))`, so

\[
                    \int_0^\infty\rho(t)\,dt\le S/4.
\]

Let `R_a^(j)(x)` denote the residual-free preactivation response to the
gradient associated with training sample `a`. The integrated bridge's
whole-sphere event gives
`max_{a,j,x,i}|R_{a,i}^(j)(x)| <= SU sqrt(log(en))`. The exact physical
identity is `dot z^(j)(x)=-(2/m) sum_a r_a R_a^(j)(x)`. Applying
Cauchy--Schwarz to this sample average, then integrating over the queried
real interval, gives

\[
 \sup_{t,x,i,j}|z_i^{(j)}(t,x)-z_i^{(j)}(0,x)|
 \le 2SU\sqrt{\log(en)}\int\rho(t)\,dt
 \le \tfrac12 S^2U\sqrt{\log(en)}.
\]

There is no complex radius or strip width in this estimate. The queried
horizon is within the inherited source horizon at the retained eventual
width, and the stored continuation uses the certified frozen endpoint.

The finite-panel and whole-sphere formulas for `U_j` differ only in the
nonnegative additive term `64 q_{j-1}` versus
`16 sqrt(d+3) q_{j-1}`. Their other coefficients do not recursively depend
on this replacement. Hence

\[
 U\le\max\{1,\sqrt{d+3}/4\}\,U_{\rm fin}
   \le\beta^{72L}\sqrt{d+3}.
\]

The final inequality uses the full-`S <= 1` ledger in
`PHYSICAL_PARAMETER_ACCOUNTING.md`, not a sharper estimate requiring an
extra small-label condition. This comparison is the key repair to the
earlier radius-based appendix.

Initialization on an `n^(-2)` sphere mesh, conditional Gaussian row tails,
and the initialized RMS/operator bounds give
`C beta^(3L) sqrt((d+1)Z)`. The mesh cardinality is at most `(Cn^2)^d`;
only its logarithm enters the tail estimate. Input Lipschitz bounds extend
from the mesh. Adding the displayed movement, the activation slope, and
the parameter-polynomial approximation error is safely covered by

\[
                 B_{\rm pass}=C\beta^{110L}\sqrt{d+1}\,Z^{3/2}.
\]

In particular the pointwise error contributed by the normalized parameter
error is at most `C beta^(4L) Y sqrt(n) n^(-10)`, and `Y <= beta^(3L)`
makes it harmless in this loose cap. Allocate the initial Gaussian failure
explicitly. The fresh noise RMS event costs at most `CL exp(-cn)` for
each complete good training tape and can be coupled uniformly over the
query through the same raw noise fields.

The geometry note's smooth value cap, applied with fixed slack above
`B_pass`, is identity on completed physical passive fields. Its first two
derivatives have the required bounds with no new width power. The much
larger history/coefficient/innovation caps remain numerical safeguards;
they are not substituted for `B_pass` in statistical estimates.

### 3.2 Mean mixers and finite-rank covariance repair

For an initialized Gaussian hidden matrix `W`, with entries of variance
`1/n`, Gaussian two-net tails give `E ||W||_op^2 <= C`. Let `F_j` be the
observable physical-call filtration. Predictability gives the correct
Gaussian posterior, and

\[
                M_j=\mathbb E[\|W\|_{\rm op}^2\mid F_j]
\]

is a nonnegative martingale. The first-crossing inequality with allocated
failure `delta/[C(L+1)]` controls all prefixes simultaneously. Conditional
Jensen then yields
`||E[W|F_j]||_op <= sqrt(C(L+1)/delta)`. This argument is independent
of the integrator and transcript length. It does not condition a Gaussian
likelihood on a realized small-operator-norm event.

The learned Taylor displacement is measurable at a completed current
state and is a stored rank-factor sum. Its operator norm is bounded by
the true displacement plus the proved parameter error. The existing
norm guard can be imposed with slack without changing the good-event
trajectory. Adding this displacement to the posterior mean gives the
required mean-mixer bound.

Concatenating learned factors and posterior-mean history factors produces
the same row normal form as in the geometry note. The posterior covariance
correction has rank at most `R`; its discarded contribution has expected
squared RMS at most `CR/n` times the explicitly retained feature/noise
factors. A passive layer uses each initialized matrix only once, so its
input is independent of the next centered matrix under the posterior
representation. The fixed-depth weak-moment recursion therefore applies.

The common Gram is built from raw retained pairs and dominates the
posterior/empirical mark Grams after the prescribed ridge and coupling.
No history spectral gap is assumed. Scalar-summary noise and arithmetic
are still chosen with the conservative `exp(CR Theta)` comparison; noisy
empirical pairs are not treated as exact posterior Grams.

Finally the new scalar-summary law is the same exchangeable noisy-average
law required by `RECALIBRATION_FREE_MOMENTS.md`. Its information bound,
all-prefix event, and posterior interval-center argument apply to this
predictable physical tape. Private metric acquisition contributes through
the certified prefix error ball, not through additional conditioning data.
The independent dense-center comparison still requires its stated
eventual-width inequality. Merely obtaining an `n^(-1/2+o(1))` rate would
not suffice, and the final assembly explicitly retains that obligation.

## 4. Counted implementation and substitutions

Set the common word size to `w=CR Theta`, including integer ranges. The
independent stage seeds use `C(L+1)R^2 Theta^2` bits. One coordinate of
the median estimator retains at most `C(d+1)R Theta` block means of
`CR Theta` bits each. Computing coordinates successively with the same
seed reproduces the same vector of medians as the simultaneous version.
The incoming context and prepared scalar coefficients must stay fixed
until the entire vector is completed; guards are then applied to that
completed vector. This schedule adds at most `CR` row-stream passes and
does not add a new probability union or alter the query theorem.

The query block length remains
`s=floor(n/(128 Khat))`, with `K_+ <= Khat <= 2K_+` and
`n >= 512 K_+`. Here `K_+` is the specified scalar-summary information
bound, not a replacement accuracy parameter. In particular `s <= n` is
the valid simplification; no polylogarithmic row count is established.

The modular internal table reconstructs:

| Resource | Checked bound |
|---|---|
| Retained bits | `C[R^3 Theta+(L+1)R^2 Theta^2]` |
| Peak training/query bits | `C[R^3 Theta+(d+L+2)R^2 Theta^2]` |
| Initialization work | `CnR^8 Theta^3` |
| Peak initialization bits | `C[nR^2 Theta+R^4 Theta+(L+1)R^2 Theta^2]` |
| All scheduled updates | `CR^7 Theta^3` |
| One query | `C(L+1)[s(d+1)R^7 Theta^5+R^7 Theta^3]` |

For example, Gaussian row generation in dimension at most `CR` costs
`CRw^4=CR^5 Theta^4`; ordinary row arithmetic and stream/hash costs are
no larger. The coordinatewise stream count supplies the remaining
`s(d+1)R^2 Theta` factor. Stage preparation is reused, rather than being
repeated for every median coordinate. The metric construction accounts
for initialization's expanded dyadic scratch and exact rank/swap work.

The source-generation bound is also included without an extra gate:

\[
 (nR^5+R^6)\Theta^4
 \le(nR^6+R^7)\Theta^3\le 2nR^8\Theta^3,
 \qquad \Theta\le R,\quad n,R\ge1.
\]

With `M=m+d+2` and `G=1+r`, substitute
`R <= C beta^(201L) M G^2 Z^(5/2)` and
`Theta <= C beta^(102L) G Z`. The leading unslackened powers are

- `R^3 Theta`: `beta^(705L) M^3 G^7 Z^(17/2)`;
- `nR^8 Theta^3`: `n beta^(1914L) M^8 G^19 Z^23`;
- `nR^2 Theta` and `R^4 Theta`: activation powers `504L` and
  `906L`, with respective factors `nM^2G^5Z^6` and `M^4G^9Z^11`;
- `R^7 Theta^3`: `beta^(1713L) M^7 G^17 Z^(41/2)`;
- `(L+1)s(d+1)R^7 Theta^5`: at most
  `Cn beta^(1919L) M^8 G^19 Z^(45/2)`.

The stated rounded activation exponents `710,1920,910,1720,1920`
therefore cover all rows, including stage seeds and one-coordinate median
storage. The logarithmic and gap-ratio powers in the assembly are correct.

The evaluator-call counts also survive the coordinatewise schedule:
`CnR^3` for initialization, `CR^4` for updates, and
`C(L+1)[s(d+1)R^3 Theta+R^2]` for a query. Their actual evaluator work,
descriptions and live scratch remain additions, not unit-cost oracle
assumptions. Original input/certificate encodings and output writing are
likewise explicit. Certified upper enclosures for integer orders and
precision levels avoid undecidable exact-boundary tests; the stated
constant-factor dyadic/time-boundary slack does not change these powers.

## Closing limitation

The assembly gives a coherent smaller Taylor-source conditional algorithm
under the inherited scientific interfaces. Its high activation/depth and
sample/gap powers are conservative upper bounds, not mathematical gaps
by themselves. Conversely, the width-order sampling and the stated bit
power are real limitations of this construction, not quantities that can
be hidden in initialization or an eventual-width threshold. A new
logarithmic-query or fourth/fifth-power complete representation would
require a further argument and a separate review.
