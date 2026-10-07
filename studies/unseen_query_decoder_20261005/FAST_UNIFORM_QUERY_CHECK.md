# Independent bounded reconstruction of the fast uniform query note

2026-10-06. Independent mathematical check of the complete
`FAST_UNIFORM_QUERY.md`, including its coordinatewise-median option.
No experiment, Git operation, maintained-source edit, or other-study input.
Only this report is written. This is an internal check, not promotion or
a new review of the inherited scientific source theorem.

## Frozen inputs and verdict

The original target SHA-256 is
`6e7a71d637ea1bf809610ece249deef484237ba74225fafff981d62b34cff5cd`.
The complete permitted dependencies read were:

| Input | SHA-256 |
|---|---|
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `SANE_METRIC_PACKETS.md` | `1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea` |
| `SHORT_SEED_PRIOR_BLOCKS.md` | `78e5f21ce787adac48b5ca745f330af92c87330934dd1634132c0b2308c35201` |
| `RECALIBRATION_FREE_MOMENTS.md` | `710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea` |
| `DENSE_BUDGET_SELF_NORMALIZED.md` | `80de0e2890bc69331f4046ce24f0e1a3dbe00cf52f53e9635f965d22fd34eb36` |
| `COST_CONTRACT.md` | `3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The conditional probability argument and resource counts pass this
reconstruction. There is one minor specification correction: the sentence
after (8) needs an explicit upward safety offset when constructing its
CDF threshold. The displayed condition (8) itself is sufficient, and the
correction changes neither an exponent nor a probability budget.
There is no other unresolved finding in this bounded scope.

The scientific source event, physical comparison, posterior common-Gram
interface, causal sensitivity/compiler interface, and stated block-PRG
theorem remain imports. This verdict does not establish them afresh.
The Taylor-source remark is checked only as conditional exponent
arithmetic; its source was outside the assignment and was not read.
No study README, other review report, or unassigned scientific artifact
was read. Shared instructions and the requested research, rigorous-proof,
and canonical-notation skills, including the neural reference and relevant
research-contract/adversarial-audit references, were read and applied.

## The threshold correction

Put \(\Delta=2^{-b}\) and \(p_T=\Phi(-T)\). Upward rounding alone
of a certified approximation or upper endpoint need not produce a number
at least \(p_T+\Delta\), as (8) requires. For example, rounding a
number slightly above a grid point can add much less than one grid unit.
Increasing only the upper slack does not establish the lower inequality.

A concrete finite rule is to obtain a certified upper endpoint
\(u_\Phi\in[p_T,p_T+\Delta/2]\), then set

\[
 a_T=\Delta\left\lceil u_\Phi/\Delta\right\rceil+\Delta.
\]

It obeys
\(p_T+\Delta\le a_T\le p_T+(5/2)\Delta\), hence (8).
Certified absolute CDF error below \(\Delta/4\) supplies such an
upper endpoint. This is a clarification of the construction, not a
counterexample to the existence or sufficiency of a threshold obeying
(8). All following checks use the explicit condition (8).

## Probability and precision reconstruction

Condition on the complete source and its actual numerical prefixes.
For stage \(\ell\), conditioning additionally on seeds of stages
\(1,\ldots,\ell-1\) makes the incoming context at each external
code deterministic. Projection guards make it admissible even after an
earlier failure. The independent stage-\(\ell\) seed is therefore
eligible for its fixed-context guarantee. This proves Lemma 1 without
conditioning on success, enumerating all possible intermediate vectors,
or assuming continuity of the implemented median.

The sphere normalization estimate (5) is correct. Counting its dyadic
coordinate codes, the within-patch coordinate, and the finitely many
prefix/patch/stage indices gives
\(\log|\mathcal A|=O((d+1)R\Theta)\). With fixed incoming
moments, the imported row sensitivity controls external perturbations;
the integrated Gaussian inequalities control propagated incoming-moment
perturbations. A recurrence with \(O(R)\) stages and logarithmic
per-stage factor \(O(\chi)\) has total logarithmic factor
\(O(R\chi)\). Thus the specified external precision suffices,
including deterministic normalization error. This is an exact-reference
continuity argument and does not assert continuity of finite arithmetic.

For each stream let \(E\) denote the flag event, and let \(B_a\)
denote a specified coordinate/side failure at a reached code. Conditional
on the earlier seeds, the bound is

\[
 \Pr_{\rm gen}\!\left(E\cup\bigcup_a B_a\right)
 \le \Pr_{\rm iid}(E)+\zeta_E
      +\sum_a\left[\Pr_{\rm iid}(B_a\cap E^c)+\zeta_a\right].
\]

The tail is charged once per stage. The context union multiplies only
the statistical and distinguishing errors. The tail flag needs a fixed,
padded packet schedule across all contexts; the note imposes it. A test
for \(B_a\cap E^c\) keeps the same scalar block sum and threshold
count as the core test, plus one OR bit. Hardwired contexts, coefficients,
and target thresholds are permitted by the imported nonuniform test
interface and are not decoder data. These tests read every row block
once. The actual output algorithm need not have their small state.

When a flag is absent, its entire uniform cell lies in the unclipped
quantile interval. The inverse-density derivative bound gives (9).
The coupled exact Gaussian coordinates are iid before any conditioning;
intersecting a failure event with \(E^c\) does not require them to
remain iid conditional on \(E^c\). The event inclusion into an ideal
statistical failure, using separate threshold margins, is valid.

Because \(N=Js\), \(s\le n\), and
\(J=O((d+1)R\Theta)\), the logarithms of the row, stage, and
coordinate counts are \(O(\Theta)\). Therefore
\(T^2=O(\Theta)\) makes the tail probability small enough. Taking
\(b,b'=O(R\Theta)\) with sufficiently large constants pays for
both \(e^{T^2/2}\) and the row sensitivity \(e^{O(R\chi)}\).
The CDF/quantile algorithm's cutoff condition \(T^2=O(w)\) holds
for \(w=O(R\Theta)\). The external entropy need not enter this
cutoff or row precision.

For the statistical block, \(sh\le1/128\) implies product-law
total variation at most \(1/16\). Posterior second moments give
Chebyshev failure at most \(1/16\) at threshold \(4B/\sqrt s\).
The prior block therefore fails with probability at most \(1/8\).
For an odd \(J\), the probability of at least half failing is at
most \(2^J(1/8)^{J/2}=2^{-J/2}\). Coordinate union gives (13);
the scalar second moment uses the bound \(B^2\) in place of \(B\).
This is a whole-product-law comparison before PRG substitution.

Choosing \(J\) and the log inverse distinguishing error proportional
to \(F=O((d+1)R\Theta)\), with constants covering all sides,
coordinates, stages and codes, pays for their union. The whole-row
randomness is \(O(Dw)\); the between-row tester state is
\(O(w+\log N)\). Hence
\(A=O(Dw+F+\log N)=O(R^2\Theta)\) and
\(E_0=O(\Theta)\). The resulting \(Q\) seeds use
\(O(QR^2\Theta^2)\) bits. Their independence and all their
initial random bits are expressly retained and charged.

The exact weak inequalities in the imported moment note preserve linear
dependence on variance error after integrating the fresh Gaussian.
Projection and the variance maximum do not enlarge the required exact
moment discrepancy. They propagate the local bounds (16) at fixed depth.
When \(s=\lfloor1/(128\widehat h)\rfloor\) is positive, the
usual floor comparison gives the same root-width logarithmic scale.
The explicit width gate remains necessary. The posterior-center and
dense-reference assembly remain conditional on their imported events.

## Work, storage, and repeated median computation

For \(w=O(R\Theta)\) and \(J=O((d+1)R\Theta)\), current
coefficient storage is \(O(R^3\Theta)\). Earlier stage outputs
fit in \(O(QRw)=O(R^3\Theta)\), since \(Q=O(R)\).
External codes, packet scratch, and generator scratch fit below these
terms. The selected acquisition base is \(B_{\rm in}+O(R^3\Theta)\).

| Median implementation | Median-array bits | Stream passes per stage |
|---|---:|---:|
| Store all coordinate block means | \(O((d+1)R^3\Theta^2)\) | 1 |
| Store one coordinate's block means | \(O((d+1)R^2\Theta^2)\) | \(O(R)\) |
| Search the finite median grid | no full block-mean array | \(O(Rw)\) |

The coordinatewise option freezes the incoming context and prepared
coefficients, restarts the identical deterministic stream, and delays
projection until the whole vector and scalar are complete. Its medians
are consequently identical to the all-array medians. The one-pass
failure tests still characterize those medians; no repeated-read PRG
claim enters. In-place sorting costs
\(O(QRJ\log(J+2)w)\) bit operations with no second mean array.
This verifies (20a) and (20b), including the reuse of preparation.

One packet has internal work bounded by
\(O(R^5\Theta^4)\), while all preparations cost
\(O(QR^7\Theta^3)\). Multiplying the packet count
\(O(Qs(d+1)R\Theta)\) by that packet cost proves (1).
The three implementations therefore admit the internal work bounds

\[
\begin{array}{ll}
\text{all arrays:}&
 O\!\left(Q[s(d+1)R^6\Theta^5+R^7\Theta^3]\right),\\
\text{one coordinate:}&
 O\!\left(Q[s(d+1)R^7\Theta^5+R^7\Theta^3]\right),\\
\text{threshold search:}&
 O\!\left(Q[s(d+1)R^8\Theta^6+R^7\Theta^3]\right).
\end{array}
\]

For these same choices the additional activation/data work is, respectively,

\[
 C Q\left\{
 \begin{array}{l}
 s(d+1)R^2\Theta+R^2,\\
 s(d+1)R^3\Theta+R^2,\\
 s(d+1)R^4\Theta^2+R^2
 \end{array}\right\}
 T_{\phi,\rm data}(CR\Theta).
\]

These alternatives mean separate bounds, not a sum. Preparation is reused
in each. One live \(S_{\phi,\rm data}(CR\Theta)\), retained
evaluator code, actual data/certificates, query/time access, output work,
and the contract's label-normalization/output-scale costs remain additions.
No evaluator bound follows from analytic regularity alone.

The physical substitution in (21) is correct for the all-array option.
Its separate powers of \(Z\) are 20 for acquisition, 16 for seeds,
22 for stored means, 46 for stream work and 48 for preparation. The
corresponding inverse-gap powers are 10, 8, 11, 23 and 24; the displayed
coarse envelopes dominate them. The stream/preparation activation
exponents 2807 and 2708 are below 3000. Equation (21) must not be
silently reused for the more expensive coordinatewise implementation.
Initialization still includes \(nR^2\Theta\) temporary bits and
\(R^4\Theta\) exact-metric scratch, as the note explicitly states.

## Remaining claims

The conditional-variance identity and sine example in (22)--(23) are
correct and establish only the absence of automatic residual-variance
decay. Lemma 3 follows from the same whole-block comparison applied to
each residual, including the zero-second-moment case. Its accuracy
requires a posterior-valid residual bound and a counted control mean;
prior residual accuracy alone is not asserted to suffice.

For Proposition 4, the two value laws have variance \(1/4\) and means
\(\pm2a\), so one-sample relative entropy is \(32a^2\).
Product total variation is at most \(4a\sqrt N\), while the required
testing success forces it to be at least \(1/2\). Thus (28) is correct.
Its oracle restriction is essential and stated explicitly. It gives no
query-time lower bound for a decoder that sees packets and row formulas.

The note therefore supports the smaller conditional seed/storage/work
construction, with the minor threshold rule above clarified. It does not
prove polylogarithmic query work, a fourth- or fifth-power full bit-memory
bound, an effective stochastic width threshold, or a lower bound against
all neural query algorithms.

## Narrow recheck of the corrected threshold rule

The supervisor applied the requested rule, with corrected target SHA-256
`e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9`.
The changed Section 3 and its surrounding flag/coupling argument were
read again. Its certified upper endpoint, ceiling to the mesh, and one
additional mesh unit give exactly the bounds proved above. The added
rounding/addition uses only the existing precision and does not change
the probability, seed, workspace, work, or evaluator estimates.

Final verdict for that corrected target: **PASS within the stated
conditional, bounded scope; no unresolved finding.** The imported
scientific/compiler/PRG hypotheses and all limitations recorded above
remain unchanged. The original finding and original hash are retained
only to identify precisely what this narrow recheck resolved.
