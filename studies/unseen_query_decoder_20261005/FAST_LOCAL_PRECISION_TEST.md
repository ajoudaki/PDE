# Local precision for quantized metric acquisition

2026-10-06. Scoped author continuation; no experiment, Git operation,
independent review or promotion. The main result is an exact acquisition
lemma for a specified finite source. It removes causal amplification from
rounding the selected metric. It does not yet replace the source/decoder's
entire `R Theta` precision by local precision.

The mechanism is to round each noisy scalar acquisition to a fixed grid.
Fresh scalar Gaussian noise keeps the completed source away from the grid
boundaries with high probability. A sufficiently accurate rounded metric
then produces exactly the same rounded scalar at every step. The metric
may depend on the completed source: the proof uses a uniform error bound,
not independence of the metric from the noise.

## 1. Contract and finite source

Keep the original dense nonlinear model, full label allowance, physical
matrix-answer tape, unseen sphere inputs, physical times and fitted endpoint.
The finite source and metric below are implementation objects in that
contract, not a new network or a population limit. Setup may inspect the
completed virtual source and is charged. No future scalar-answer table is
retained and query evaluation does not replay scalar training.

Let `R` bound named row fields and matrix calls, `P <= C R^2` the scalar
pair acquisitions, and `D <= C R` the packet dimension. The following
finite-source hypotheses are explicit; particularly, local precision of
this source is not a conclusion of the lemma.

1. The source has independent finite root packets `Z_i`, `1 <= i <= n`,
   independent of standard scalar Gaussians `E_1,...,E_P`. At a given
   packet and scalar prefix, a fixed deterministic finite evaluator
   produces named dyadic row fields. Each old field keeps its creation-time
   scalar arguments. Its implementation may round internal operations;
   identical arguments must give identical bit strings.
2. Every scalar reduction is a pair of those named fields, including the
   constant field. Field values have modulus at most `B >= 1`. Products
   and sums defining the empirical pair are exact on the finite operand
   grid; division by `n` is retained rationally until the scalar rounding.
3. Fix dyadic `0 < h <= eta <= 1`. Write `Q_h` for rounding to the nearest
   multiple of `h`, using a fixed tie convention. At update `r`, set

   \[
   A_r=\frac1n\sum_i u_r(Z_i;C_{<r})v_r(Z_i;C_{<r}),\qquad
   C_r=Q_h(A_r+\eta\widehat E_r).                         \tag{1}
   \]

   The finite scalar mark `Ehat_r` is a function only of `E_r` and any
   independent sampler bits for that mark. A coupling satisfying the
   error requirement below is part of the finite Gaussian sampler.
   Hence `A_r` is independent of the fresh `E_r` conditional on the full
   root array and preceding scalar marks. The numerical value of `A_r`
   is allowed to depend arbitrarily on that past.

Apply the exact finite-table construction of `SANE_METRIC_PACKETS.md`
to the completed dyadic field table, including the constant column. It
selects `q <= C R` original packets and a positive metric `M` such that
every realized pair satisfies

\[
 A_r=u_r(I;C_{<r})^T Mv_r(I;C_{<r}),\qquad |M_{ab}|\le4.  \tag{2}
\]

The source-derived metric is fixed after this construction. No assertion
is made that (2) holds at a different scalar prefix.

Round its symmetric entries with maximum entry error `epsilon_M`, obtaining
`M_0`, and retain

\[
 \widehat M=M_0+q\epsilon_M I_q.
\]

Taking `epsilon_M` to be the dyadic rounding-grid step gives

\[
 \widehat M\succeq M,\qquad
 \|\widehat M-M\|_{\rm op}\le2q\epsilon_M,\qquad
 |u^T(\widehat M-M)v|\le2q^2B^2\epsilon_M               \tag{3}
\]

for all selected operand vectors bounded by `B`. The last bound follows
from `||u||_2,||v||_2 <= sqrt(q) B`.

## 2. A conditional Gaussian rounding-boundary bound

For a real scalar `a`, standard Gaussian `E`, grid `h > 0` and noise
`eta > 0`, put `X=a+eta E`. Its rounding boundaries are
`h(Z+1/2)`. For `0 < v <= h/2`,

\[
 \Pr\{\operatorname{dist}(X,h(\mathbb Z+1/2))\le v\}
       \le2v\left(h^{-1}+\eta^{-1}\right).              \tag{4}
\]

Here is a proof uniform in `a`. If `f` is the Gaussian density of `X`,
then `integral |f'| = 2/(eta sqrt(2 pi))`. For any real `s`, integrate
the inequality

`f(s+kh) <= f(x)+ integral_[s+kh,s+(k+1)h] |f'|`

over `x` in that interval and sum in `k`. This gives

\[
 \sum_{k\in\mathbb Z}f(s+kh)
 \le h^{-1}+\int_{\mathbb R}|f'(x)|\,dx
 \le h^{-1}+\eta^{-1}.
\]

Integrating this periodic density over a length-`2v` interval proves (4).
The same argument holds conditional on any sigma field relative to which
`a` is measurable and `E` is still independent standard Gaussian.

## 3. Exact tape reproduction at local metric precision

Fix `0 < delta_acq < 1` and define

\[
 \zeta=\frac{\delta_{\rm acq}h}{64P}.
\]

Assume the finite noise sampler has a coupling with the independent
Gaussians such that, with failure probability at most `delta_acq/2`,

\[
 \max_r\eta|\widehat E_r-E_r|\le\zeta.                  \tag{5}
\]

Choose

\[
 \epsilon_M\le\frac{\zeta}{2q^2B^2}.                   \tag{6}
\]

Copy the selected finite packets and scalar noise marks exactly; do not
round them again. The compact acquisition is

\[
 \widehat C_r=Q_h\left(
 u_r(I;\widehat C_{<r})^T\widehat M
 v_r(I;\widehat C_{<r})+\eta\widehat E_r\right).         \tag{7}
\]

The bilinear form in (7) can be computed exactly as a sum of dyadic
products, followed by the exact outer grid rounding. More generally the
lemma permits an additional absolute arithmetic error at most `zeta`
inside each occurrence of `Q_h` in (7).

**Lemma.** With probability at least `1-delta_acq`,

\[
                     \widehat C_r=C_r\quad(1\le r\le P).
                                                               \tag{8}
\]

The equality is literal equality of the finite scalar values. It holds
despite the private metric and selected packets depending on the completed
source, including all scalar noise marks.

**Proof.** Define, along the actual finite source,
`X_r=A_r+eta E_r`. The conditional version of (4), with `v=4 zeta`,
is applicable by hypothesis 3. Since `h <= eta`,

\[
 \Pr\{\operatorname{dist}(X_r,h(\mathbb Z+1/2))\le4\zeta\}
 \le16\zeta/h=\delta_{\rm acq}/(4P).
\]

Union over the `P` updates. Except on probability `delta_acq/4`, every
source pre-rounding shadow value `X_r` lies more than `4 zeta` from its
rounding boundaries. Intersect with (5). This event has probability at
least `1-3 delta_acq/4`, which is at least the asserted probability.

Induct on `r`. If the prefixes coincide, determinism gives exactly the
same selected row values as those used in the source table. Equations
(2), (3), and (6) bound the change in the empirical pair by `zeta`.
The finite noise mark changes `X_r` by at most `zeta`; the optional
compact arithmetic contributes at most a further `zeta`. Both source
and compact pre-rounding values are therefore within `3 zeta` of `X_r`.
They lie in its same rounding cell and give identical next scalars.
The empty prefix starts the induction. No estimate on the behavior of
any field at a different prefix is used. QED.

This argument does not store corrections fitted to future outputs or
modify the original scalar noise marks. Exact equality at each step
prevents an off-tape field from ever being evaluated on this event.

## 4. Counted precision and space consequence

Choosing the coarsest dyadic step satisfying (6), the metric entries need

\[
 b_M\le C+\log_2 h^{-1}+\log_2 P+2\log_2 q
                  +2\log_2 B+\log_2\delta_{\rm acq}^{-1}.\tag{9}
\]

Their integer parts are bounded by (3) and `|M_ab| <= 4`. No smallest
metric eigenvalue or inverse of the metric enters this count.

The marks in (5) require error at most `zeta/eta`; their fractional
precision is

\[
 C+\log_2(\eta/h)+\log_2(P/\delta_{\rm acq}),            \tag{10}
\]

plus their Gaussian cutoff's integer-part cost. This is a counted finite
sampler, not a continuous-Gaussian oracle: for example choose cutoff
`T_E^2 >= 2 log(8P/delta_acq)`. Quantized inverse-normal sampling with
coordinate error `zeta/eta` requires
`O(T_E^2 + log(eta/zeta))` uniform bits per mark and polynomial working
precision. The Gaussian-CDF/bisection construction in
`SANE_DECODER_CORE.md`, Section 5, supplies such sampling work and scratch;
the cutoff and coupling failures are included in (5).

If named field values have `p_f` fractional bits, exact dyadic bilinear
arithmetic needs `O(2p_f+b_M+log(q+2)+log(B+2))` bits, plus the
scaled-noise word allowance. Exact empirical source summation and rational
division add `O(log(n+2))` bits. These costs are local and do not grow
by one word length per earlier phase.

In particular, **if** the valid finite source, its packet generator and
its deterministic coefficient/row evaluator already use
`p_loc = O(Theta+log(R/delta_acq))` bits, and
`log h^-1, log eta^-1, log B <= C p_loc`, then the selected packets,
metric, scalar marks, scalar history and the existing coefficient arrays
use

\[
                         O(R^2p_{\rm loc})               \tag{11}
\]

bits. The lemma proves the metric/acquisition part of this implication.
It does not prove the premise about finite source and row precision.
Activation/data evaluator descriptions, actual evaluator workspace,
query seeds and median workspace are additional, unchanged costs.

The existing exact construction on this finite table costs
`O(n R^5 p_loc^3)` bit operations and
`O(n R p_loc+R^3 p_loc)` peak bits, besides source generation and later
decoder storage. Exact rational metric intermediates have `O(R p_loc)`
bits; only the rounded entries from (9) are retained. These are the
substitutions in `SANE_METRIC_PACKETS.md`, (14)--(15), with table word
allowance including `log n`. No compact initialization-memory claim is
made.

For the Taylor envelope `R=O(Z^(5/2))`, `Theta=O(Z)` with the fixed
problem factors shown in `FAST_COMPOSITION.md`, (11) is a conditional
`Z^6` acquisition base. Even a successful full precision closure would
not by itself make this base a fourth- or fifth-power bit bound.

## 5. What scalar rounding changes in the posterior argument

Equation (1) differs from the original unrounded scalar transcript. Its
rounding cannot simply be dropped from the proof. There are, however,
two exact local facts for an ideal version using continuous `E_r` and
Gaussian root packets.

First, a quantized noisy update is postprocessing of
`A_r+eta E_r`. Conditional on the previous rounded prefix, the fresh
noise remains independent. For bounded pair tests `|A_r| <= B_F`,
the usual Gaussian-channel entropy estimate therefore remains

\[
 I(Z_{1:n};C_{\le P})\le
                   \frac P2\log(1+B_F^2/\eta^2).         \tag{12}
\]

Indeed the pre-rounding conditional variance is at most `B_F^2+eta^2`;
the maximum-entropy Gaussian bound subtracts the independent noise entropy,
and deterministic rounding cannot increase mutual information. Sum these
conditional bounds by the chain rule. This statement assumes bounded
tests, exactly as the original information interface does.

Second, on a completed prefix the exact identity becomes

\[
 C_r=A_r+\eta E_r+e_r,\qquad |e_r|\le h/2.               \tag{13}
\]

Exchangeability, the posterior entropy identity and the scalar-noise
maximal estimate in `RECALIBRATION_FREE_MOMENTS.md` consequently give

\[
 |\nu_c F_r-c_r|\le\eta\sqrt{P/\beta}+h/2.              \tag{14}
\]

Here `nu_c` is the common posterior row marginal and `beta` is the
failure allocation used in that note, not the activation envelope.
The empirical version has the same added `h/2` term on its posterior
noise event. Thus the common-Gram tolerance must explicitly include
`h/2`; one needs `R(eta T_rho+h/2+other errors) <= tau/4` at the
chosen ridge `tau`. If its logarithmic certificate is local, this
requirement is local as well.

For finite noise and root samplers, one must transfer (12)--(14) from
their specified continuous reference or prove an appropriate finite
channel substitute. Data processing by itself does not supply a
Gaussian channel when the noise has already been discretized. The metric
lemma alone does not perform that transfer.

## 6. The raw-answer proposal and its exact unresolved interface

The completed-call argument in `FAST_LOCAL_KERNEL_AUDIT.md` remains
valid after **common deterministic postprocessing** of the completed
answer and augmentation. In particular, its joint total variation bound
can be followed by identical rounding of physical answers and scalar
marks. Future physical queries may depend on those rounded values.
The proof filtration may retain their raw Gaussian ancestors, because
the rounded query is still predictable in that larger filtration.

At a shared raw history, suppose every rounded old answer differs from
its raw ancestor coordinatewise by at most `h_y`, and the old query
and answer RMS bounds are `b`. A pairing involving a query and an answer
changes by at most `b h_y`; a pairing involving two rounded answers
changes by at most `2b h_y+h_y^2`, by Cauchy--Schwarz. Old query fields
are the same rounded predictable vectors in both programmes. Adding a
fresh scalar reduction error at most `eta u+h/2` therefore changes
the current coefficient inputs locally by

\[
 e_{\rm mom}\le C\{(b+1)h_y+h_y^2+\eta u+h\}.           \tag{15}
\]

There is no causal-depth multiplier in (15). Under the one-call caps,
the same proof as that audit gives a conditional raw answer-law cost
bounded conservatively by

\[
 C z^{220}\{\sqrt n\,e_{\rm mom}+n\eta^2\},\qquad
 z=C(2+R+b+\sigma^{-1}),                                \tag{16}
\]

provided its stated smallness and positive-covariance conditions hold.
Its augmentation uses the approximate law of the fresh innovation marks
conditional on the raw answer. Those marks, including deterministic
rounded versions, reveal no extra matrix information given that answer.
The private metric is not inserted into this posterior filtration.

This verifies the proposed shared-history *local comparison*. It does
not yet specify an implementable finite source with these exact kernels.
The missing numerical step can be stated narrowly. In the shadow call,

\[
 t=Ag+\eta e,\qquad
 y=\widetilde m+Bt+\sqrt{\widetilde\beta}\,g,              \tag{17}
\]

the coefficients must be frozen before the fresh moments, and (17) must
remain affine in the raw independent Gaussian vectors. Rounding `t`
before inserting it in the displayed `y`, or mixing it into a new PSD
projection, changes that Gaussian marginal. It is not covered by merely
postprocessing the completed pair.

One sufficient implementation interface is to keep (17) as a proof-only
shadow and prove that the actual finite calculation rounds to exactly
the same final fields. Conditional on the old history, each `t` marginal
has standard deviation at least `eta`, and each `y` marginal has standard
deviation at least `sigma/2` under the audit's smallness condition. If a
finite affine evaluation has component error at most `epsilon_aff`,
(4) bounds a rounding mismatch for a component of standard deviation
at least `s` and output grid `h_out` by

\[
                  2\epsilon_{\rm aff}(h_{\rm out}^{-1}+s^{-1}).
                                                               \tag{18}
\]

Union over all `n+O(R)` components and `R` calls costs their count in
the probability budget and its logarithm in precision. Independence of
these components is unnecessary. The same common conditional augmentation
can include rounded innovation coordinates needed by later row operations.
Thus a polynomially bounded local affine evaluator would require only
local logarithms, `log n`, and `log R` at this particular boundary.

To use this proposal for the actual decoder, one must still establish all
of the following for one explicit finite schedule:

- The same independent finite root packets drive the source and the query
  row evaluator; no raw answer-noise vectors are revealed to the posterior.
  Every innovation mark retained for later use is either common
  postprocessing at a completed call or part of its explicitly attached
  conditional kernel. No matrix call is inserted halfway through (17).
- All finite intermediate computations, protections and row-field reuse
  satisfy the local shadow error required by (18). Recomputing the shared
  row DAG from identical finite packets/prefixes must give the same bits.
- Noisy and rounded *physical scalar reductions* satisfy a physical
  forcing estimate. `FAST_TAYLOR_NOISE.md`, Section 6, supplies a local
  principal-output-error mechanism, including empirical averages, but it
  has not here been matched instruction by instruction to every new
  reduction, guard and augmentation in this modified source.
- The passive posterior/reference proof, common-Gram ridge and uniform
  numerical query argument apply to this rounded source law with their
  added errors, actual finite sampler and field regularity. The all-time
  and endpoint conclusions require that complete transport, not just (16).

The local-TV mechanism is therefore compatible with a route to local
precision, and the metric rounding obstacle has a proved repair. These
facts do not certify all four interfaces or establish a full local-
precision compact decoder.

## 7. Claim status and provenance

| Statement | Status |
|---|---|
| Gaussian boundary estimate (4) | Proved uniformly in adaptive conditional means |
| Rounded metric reproduces the finite tape, (8) | Proved under the explicit finite-source and sampler hypotheses |
| Metric precision (9), acquisition count (11) | Proved implication; locally precise source remains a premise |
| Continuous-noise quantized entropy/moment identities (12)--(14) | Proved local replacements; finite-noise transfer separate |
| Raw-history moment bound and Gaussian-call estimate (15)--(16) | Conditional on the displayed shared raw history and one-call caps |
| Affine shadow rounding criterion (18) | Proved local criterion; actual complete schedule not verified |
| Replace all `R Theta` decoder precision by `Theta+log R` | Open |
| Original whole-sphere/all-time/endpoint accuracy and fast query | Unchanged; not established by this lemma |

Complete scoped inputs read: `FAST_LOCAL_KERNEL_AUDIT.md`,
`FAST_TAYLOR_NOISE.md`, `FAST_COMPOSITION.md`, `SANE_DECODER_CORE.md`,
`SANE_METRIC_PACKETS.md`, `RECALIBRATION_FREE_MOMENTS.md`,
`NOISY_SCALAR_HISTORY_ACQUISITION.md`, and
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`. No review or other-study source was
opened. The research and rigorous-proof skills and their contract,
evidence and adversarial references were read. The required private
canonical-notation skill returned permission denied; the supervisor's
explicit fallback used `docs/notation.qmd` and locally defined notation.
Only this assigned artifact was written in this continuation.
