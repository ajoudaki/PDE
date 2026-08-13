# Bounded follow-up portfolio: frozen plan and current outcomes

## Current verdict

**Status as of 13 August 2026:** Campaign 4 is complete and supplies a new
exact two-parameter finite-order certificate.  Campaign 5 completed exact
three-input feasibility and novelty work through order five, together with
exact positivity of the two available moments $\mu_0,\mu_1$, but its
order-seven resource gate failed, so it did not reach a Hankel test.
Campaign 6 is closed as protocol-inconclusive and supplies no accepted new
order-thirteen bound.  The output-kernel Stieltjes conjecture is therefore
neither proved nor falsified.

The portfolio was frozen in
[`NEXT_CAMPAIGN_PORTFOLIO.md`](NEXT_CAMPAIGN_PORTFOLIO.md) before its decisive
outputs were inspected.  It deliberately separated three claim levels:

1. exact fixed-order mean-field-peeling (MFP) identities;
2. exact finite Hankel inequalities for named parameter families; and
3. the all-order Stieltjes conjecture and its global mean-field
   interpretation.

Only the first two levels were within this round's reach.  No finite-order
pass below is promoted to an all-order theorem.

## Common mathematical object

For an odd formal mean-field feature jet $F$ with $F'(0)>0$, define

$$
K(y)=F'\!\left(F^{-1}(y)\right)
$$

and write

$$
K(y)=F'(0)+\mu_0y^2-\mu_1y^4+\mu_2y^6-\mu_3y^8+\cdots.
$$

Equivalently,

$$
R(x)=\frac{K(\sqrt{x})-F'(0)}{x}
=\sum_{r\geq0}(-1)^r\mu_rx^r.
$$

The formal Stieltjes conjecture says that $(\mu_r)_{r\geq0}$ is the moment
sequence of a nonnegative measure on $[0,\infty)$.  It would imply positivity
of every ordinary and shifted Hankel matrix.  This portfolio tests only the
finite matrices made available by the computed jets.

## Frozen decisions versus observed outcomes

| Campaign | Frozen primary decision | Observed outcome | Accepted claim update |
|---|---|---|---|
| 4. Independent block metrics | Compute the exact output jet through $F^{(9)}(0)$ for the full quadrant $(\alpha,\beta)\geq0$ and certify or refute the first ordinary and shifted $2\times2$ Hankel inequalities without a grid | Completed within its cap.  Every accessible moment and both determinants have exact positive-coefficient numerator certificates; strict away from the degenerate origin | Upgraded to an exact finite-order continuum certificate over a genuine two-dimensional unbounded family |
| 5. Three equicorrelated inputs | Gate $F^{(3)}$, then $F^{(5)}$, and run sectorized $F^{(7)}$ only if the novelty and resource gates authorize it; the first scientific endpoint is the exact full-interval ordinary $2\times2$ Hankel test | Stages A/B completed exactly and proved genuine three-color/non-scaling dependence.  A post-hoc exact Sturm audit proves $\mu_0,\mu_1>0$ throughout the interval.  The final-source zero-W-hit order-seven pilot did not finish by 1,800 seconds, so Stage C failed closed | **Inconclusive at the Hankel endpoint.**  Exact jets through order five and the two lower moment signs are accepted, but no $\mu_2$ or Hankel PSD claim is accepted |
| 6. Threshold-aware canonical order thirteen | Seek a rigorous interval or one-sided certificate separating the exact D13 threshold, under a two-CPU-hour initial cap and mandatory fresh D9/D11 and provenance gates | Closed before D13 production.  The tested envelopes were far too loose, and a hostile audit found that the mandatory regression/provenance gate was not completed | **Inconclusive.**  No new D13 certificate and no evidence either for or against the conjecture |

Neither conditional branch was launched.  Campaign 5's failed order-seven
gate makes the four-input prerequisite false.  The metric-ray order-eleven
pilot is not recommended in this round because the portfolio has reached its
precommitted marginal-evidence stop; it remains a possible future campaign
only after a new cost projection or structural reason changes that decision.

## Campaign 4: exact independent block-metric quadrant

### Frozen object and why the parameters are genuine

Campaign 4 kept the canonical one-input, two-hidden-layer quadratic network
and varied the relative metric on its three parameter blocks:

$$
D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W,
\qquad \alpha,\beta\geq0.
$$

The readout-block coefficient fixes the removable common clock.  Thus
$\alpha$ and $\beta$ are genuine relative learning-rate parameters rather
than an overall scale.  The first derivative already distinguishes them:

$$
F'(0)=27+48\alpha+36\beta.
$$

For one-sample squared loss, metric gradient descent follows the same
parameter-space path as feature ascent with a scalar time change.  Its output
therefore obeys, at the formal-jet level,

$$
\dot f=2(1-f)K_{\alpha,\beta}(f).
$$

This preserves the intended training interpretation.  It does not by itself
establish the separate global mean-field-trajectory theorem.

### Exact result

The compiler evaluated all 125 atomic sectors required through order nine
and reconstructed

$$
F_{\alpha,\beta}^{(k)}(0)
=\sum_{w=0}^k\sum_{a=0}^{k-w}
C_{k,w,a}\alpha^{k-w-a}\beta^w
$$

for $k=1,3,5,7,9$.  Exact series inversion then proves throughout the closed
quadrant

$$
\mu_0,\mu_1,\mu_2,\mu_3\geq0,
$$

$$
\Delta_1=\mu_0\mu_2-\mu_1^2\geq0,
\qquad
\Delta_1^+=\mu_1\mu_3-\mu_2^2\geq0.
$$

All six expressions are strictly positive whenever
$(\alpha,\beta)\neq(0,0)$.  At the origin only the readout block moves,
$F(s)=27s$, so $K$ is constant and every nonconstant moment vanishes.

The sign proof is algebraic, not sampled.  After exact reduction, every
denominator is a positive integer times a power of
$16\alpha+12\beta+9$, while every nonzero numerator coefficient is positive.
The numerator term counts are 9, 25, 49, and 81 for
$\mu_0,\ldots,\mu_3$, 81 for $\Delta_1$, and 169 for $\Delta_1^+$.  Pure
positive powers of both variables certify the two boundary axes as well as
the open quadrant.

### Validation and resource scope

The whole-forest reference route and connected-sector route agree on every
coefficient through order five.  The completed result also passes:

- the full earlier diagonal identity $\alpha=\beta=\lambda$ through order
  nine;
- the canonical point $(1,1)$ through order nine;
- independent off-diagonal and coordinate-axis checks;
- direct reconstruction from all 125 atomic sector files; and
- source, manifest, hash, checked-arithmetic, and certificate replay audits.

The production sectors used 1131.036 cumulative wall seconds under the frozen
1800-second cap and a 4 GiB virtual-memory limit per sector.  This establishes
a strong but finite statement: the first shifted test survives a genuine
two-dimensional unbounded metric family.  It does not establish higher
Hankel positivity or an all-order representation.

The authoritative campaign artifacts are the
[`frozen protocol`](../mean_field_peeling/quadratic_compiler/campaign4/PROTOCOL.md),
[`result report`](../mean_field_peeling/quadratic_compiler/campaign4/RESULTS.md),
[`exact jets`](../mean_field_peeling/quadratic_compiler/campaign4/results_order9.json),
[`exact Hankel certificates`](../mean_field_peeling/quadratic_compiler/campaign4/certificates_order9.json),
and [`provenance record`](../mean_field_peeling/quadratic_compiler/campaign4/provenance_order9.json).

## Campaign 5: exact three-input structure, inconclusive Hankel test

The frozen family is

$$
G_3(\rho)=(1-\rho)I_3+\rho\mathbf1\mathbf1^\top,
\qquad -\frac12\leq\rho\leq1,
$$

with equal labels and scalar channel
$g=(f_1+f_2+f_3)/3$.  Unlike the two-input family, it can expose the genuine
three-color invariant
$\rho_{12}\rho_{23}\rho_{31}$; under equicorrelation this becomes $\rho^3$.
That makes the family scientifically nonredundant, even though the attempted
run did not reach the frozen order-seven Hankel endpoint.

The campaign was intentionally staged.  Orders three and five were
feasibility, novelty, and resource gates only.  The intended scientific
endpoint required the exact full-interval signs of

$$
\mu_0,\quad\mu_1,\quad\mu_2,
\quad\mu_0\mu_2-\mu_1^2.
$$

### Exact Stage A/B results

The transparent labelled-Wick route and checked connected compiler agree
through order three.  The accepted normalized derivatives are

$$
F_3'(0;\rho)=\frac{141+80\rho^2+112\rho^4}{3},
$$

$$
F_3^{(3)}(0;\rho)=\frac{J_3(\rho)}{81},
\qquad
F_3^{(5)}(0;\rho)=\frac{J_5(\rho)}{729},
$$

where the complete exact integer polynomials $J_3,J_5$ are preserved in the
campaign report and raw artifacts.  They reproduce the accepted one-input
derivatives at $\rho=1$, while a mechanical two-color specialization
reproduces the independent Campaign-2 equal-label jet through order five.
All applicable parity, normalization, canonical-endpoint, two-color, and
sector-partition gates passed.

A subsequent exact post-hoc audit uses only these already accepted jets.
Exact Sturm root counts on $[-1/2,0]$ and $[0,1]$ prove

$$
\mu_0(\rho)>0,
\qquad
\mu_1(\rho)>0
\quad\text{for }-\frac12\leq\rho\leq1.
$$

This is a durable lower necessary-moment certificate, not the preregistered
Hankel endpoint.  It supplies neither $\mu_2$ nor a determinant.

The computation exposes a terminal three-color moment containing
$3\rho+6\rho^2+6\rho^3$, so the cyclic odd dependence is witnessed rather
than inferred only from an aggregate coefficient.  The scale-invariant ratio

$$
\mathcal I(\rho)
=\frac{F_3'(0;\rho)F_3^{(5)}(0;\rho)}
{F_3^{(3)}(0;\rho)^2}
$$

takes distinct exact values at $\rho=-1/2,0,1$.  Thus the family is not a
separate rescaling of input, output, or time.  These are genuine exact MFP
extension results, but the frozen protocol explicitly classified them as
feasibility and novelty rather than Stieltjes success.

### Failed Stage-C gate

The order-seven compiler was separately frozen and graded by W-hit count.
Before production it had to pass three representative pilots, at W-hit
sectors $0,3,7$, each under 4 GiB and 1,800 seconds, with all pilot cost
debited against the six-CPU-hour campaign cap.  The final-source W0 pilot
produced no completed order-seven result by its cutoff.  W3 and W7 were then
stopped, no production sector was launched, and the durable runner was made
unconditionally fail closed.

The written projection rule was frozen about thirteen minutes after the W0
pilot launched, but before any pilot completed, before any order-seven
coefficient existed, and before the 1,800-second failure boundary.  The W0
process was terminated at the next polling boundary, at most 26.050744
seconds late; no post-cutoff output was accepted and the full tail was charged
to the conservative budget debit.  These are procedural imperfections in
prospective timing purity, but they cannot bias a favorable acceptance: the
observed outcome failed the rule and closed the branch.

Consequently there is no accepted $F_3^{(7)}$, no $\mu_2$, no $\Delta_1$,
and no three-input Hankel PSD pass or counterexample.  The accepted post-hoc
$\mu_0,\mu_1$ certificate does not repair any of those missing claims.

The authoritative sources are the
[`Campaign 5 protocol`](../mean_field_peeling/quadratic_compiler/campaign5_b3/PROTOCOL.md),
[`final result report`](../mean_field_peeling/quadratic_compiler/campaign5_b3/RESULTS.md),
[`partial-moment certificate`](../mean_field_peeling/quadratic_compiler/campaign5_b3/certificates_lower_moments.json),
[`Stage-C projection rule`](../mean_field_peeling/quadratic_compiler/campaign5_b3/STAGE_C_PROJECTION_PLAN.md),
and [`failed-closed provenance`](../mean_field_peeling/quadratic_compiler/campaign5_b3/provenance_stage_c_projection.json).

## Campaign 6: bounded D13 threshold probe

### Frozen decision target

Let $D_{13}=F^{(13)}(0)$.  With all lower moments fixed at their accepted
canonical values, the next shifted Hankel determinant is nonnegative exactly
when

$$
D_{13}\leq T,
$$

where

$$
T=
\frac{
982497059836127136743897882036793220177491977764234839125040220839477248
}{
7556538848269898446547697632297780206383
}
=1.300194546159283\ldots\times10^{32}.
$$

The campaign sought threshold separation rather than the full D13 integer.
Its mandatory interpretation gate required a fresh independent reproduction
of every order-nine Wick-pair sector and the accepted order-eleven total,
together with complete per-run provenance.

### Downgraded outcome

The best pre-existing accepted positive-subsum lower bound remains

$$
D_{13}\geq
50\,393\,647\,763\,255\,899\,049\,472\,742\,772\,736
=0.38758544\ldots\,T.
$$

Campaign 6 derived a candidate unrestricted-pairing upper envelope, but it is
approximately $5.10\times10^{29}T$ and is therefore useless for the decision.
Its exact-small-component hybrid remained more than $10^{21}$ above the exact
answer already at order eleven, while its positive retained branch recovered
less than 59% there at cap 14.  These calibration trends supplied no credible
path to threshold separation under the allowed extension budget.

More importantly, the campaign failed its frozen interpretation gate.  It
loaded accepted D9/D11 tables and reproduced the D9 total, but did not freshly
reproduce every D9 sector or the D11 total, and it did not retain the required
per-run provenance records.  The new endpoints are therefore diagnostics,
not accepted certificates.  No D13 production run, old multi-day enumeration,
or old eight-hour root-class run was launched or resumed.

The campaign is correctly classified **inconclusive**.  Failure of a loose
upper envelope and an insufficient retained lower subsum is failure of those
bounding mechanisms, not evidence for the conjecture.  Further D13 work is
not authorized merely by adding compute.  It first needs a graph-sensitive
omitted-mass lemma that either:

1. bounds leading-width Wick partitions of large decorated trees within a
   small calibrated factor;
2. aggregates disjoint positive structural families without enumerating all
   P14 bases; or
3. proves a nonlocal two-generation transport identity replacing the already
   false local charging rules.

See the [`frozen Campaign 6 protocol`](../mean_field_peeling/quadratic_compiler/campaign6_f13_threshold/PROTOCOL.md)
and the [`downgraded campaign report`](../mean_field_peeling/quadratic_compiler/campaign6_f13_threshold/CAMPAIGN_REPORT.md).

## Evidence ledger after the completed outcomes

| Claim | Claim level | Status | Evidence and limitation |
|---|---|---|---|
| Independent block-metric signs through $F^{(9)}$ | Exact finite construction and finite Hankel inequalities | **Established** | Exact quadrant certificates and audited atomic sectors; says nothing at higher order |
| Three-input equicorrelation through order five | Exact fixed-order MFP extension and lower necessary moment signs | **Established** | Faithful natural-loss reduction, genuine triangle invariant, nontrivial scale-free dependence, exact F1/F3/F5 gates, and exact $\mu_0,\mu_1>0$ on the full interval |
| Three-input equicorrelation Hankel signs | Proposed finite Hankel family | **Inconclusive** | The order-seven pilot gate failed; no $\mu_2$ or $\Delta_1$ was computed |
| Campaign 6 separates the D13 threshold | Finite canonical Hankel decision | **Inconclusive** | Tested bounds do not separate $T$ and the mandatory interpretation gate failed |
| Canonical $F^{(13)}(0)$ and $\mu_5$ | Exact fixed-order coefficient | **Open** | Accepted lower bound reaches only $38.76\%$ of $T$ |
| All-order Stieltjes moment property | All-order formal theorem | **Open** | Finite passes are compatible evidence only |
| Identification with an actual global mean-field trajectory | Global limit/trajectory theorem | **Open** | Not addressed by these campaigns |

## Conditional branches and current stop decision

The portfolio permitted at most one conditional branch after Campaigns 4--6.
Neither is authorized in this round:

- four inputs required Campaign 5 to complete order seven and demonstrate
  compiler growth compatible with a bounded continuation.  Campaign 5 failed
  that prerequisite, so B=4 is not authorized;
- metric-ray order eleven would reach a genuinely larger ordinary Hankel
  matrix, but it still begins with a two-hour pilot and can expand to a much
  larger run.  After one strong Campaign-4 finite pass and two failed
  discriminating endpoints, this is additional marginal coefficient evidence
  rather than a response to a newly exposed mechanism.

The correct portfolio decision is therefore to stop: do not launch the
metric-ray order-eleven pilot under this campaign authorization.  This does
not reject the mathematical value of that test.  It can be reconsidered in a
new frozen round if a compiler improvement yields a substantially cheaper
projection or if a theoretical mechanism makes that particular $3\times3$
family discriminating rather than merely cumulative.  Campaign 4's pass does
not itself authorize more coefficient collection, and Campaign 6's failure
does not authorize a larger D13 budget.

## Minimal durable integration of the completed portfolio

This section is an integration checklist, not a current claim update.  It
prevents the same outcome from being restated inconsistently across reports.

### `CURRENT_RESEARCH_STATE.md`

Make four localized changes:

1. Update the opening status and claim table to add Campaign 4's exact
   two-parameter certificate and Campaign 5's exact order-five structural
   extension plus partial $\mu_0,\mu_1$ signs, while stating that Campaign 5
   reached no Hankel endpoint and Campaign 6 supplied no accepted certificate.
2. Extend **“Exact parameter-family extension campaigns”** with a concise
   Campaign 4 quadrant result and Campaign 5's exact-through-order-five,
   two-moment-positive but Hankel-inconclusive result; link detailed
   algebra to this report and the campaign-local reports rather than copying
   full coefficient tables.
3. In the D13 discussion, append the bounded Campaign 6 downgrade: no new
   accepted interval, failed regression/provenance gate, no production run,
   and the graph-sensitive omitted-mass lemma required before more compute.
   Preserve the old budget-four timeout as historical evidence rather than
   silently replacing it.
4. Update Sections 14 and 16 so Campaign 4 and Campaign 5's accepted
   low-order structural results appear at the correct finite claim level,
   Campaign 5's Hankel test and Campaign 6 remain
   inconclusive, and this outcome report plus all three campaign directories
   enter the durable artifact map.

### `EXACT_PARAMETRIC_CAMPAIGNS.md`

Add Campaign 4 as the next completed parametric section, including its exact
loss reduction, two-block metric definition, order-nine gate, whole-quadrant
certificate, boundary degeneration, validation, and resource stop.  Add
Campaign 5 as a completed feasibility/novelty campaign: include the scalar
equal-label reduction, admissible $\rho$ interval, genuine triangle invariant,
exact F1/F3/F5 provenance, partial $\mu_0,\mu_1$ Sturm certificate,
nonconstant scale-free ratio, Stage-C chronology,
failed pilot gate, and terminal stop.  Do **not** list it among Hankel passes.
Update the comparative evidence ledger, the campaign count, and open
obligations accordingly.  Campaign 6 belongs in this portfolio/D13 record,
not as a “parametric pass.”

### `../mean_field_peeling/README.md`

Change the compiler summary from “three isolated parameter campaigns” to the
completed portfolio description, add Campaign 4's independent block-metric
extension, and describe Campaign 5 as an accepted exact-through-order-five
grammar extension with two positive lower moments and an inconclusive
order-seven Hankel endpoint.  Record the
bounded Campaign 6 probe as a stopped, protocol-inconclusive D13 attempt and
leave “full quadratic order thirteen” open.  Do not promote these
model-specific compiler extensions into the open general MFP theorem.

### Artifact indexes

Update only the following indexes:

- [`README.md`](README.md): link this portfolio outcome and distinguish the
  Campaign 6 non-result from accepted parameter evidence;
- [`CURRENT_RESEARCH_STATE.md`](CURRENT_RESEARCH_STATE.md), Section 16: add
  links to Campaigns 4--6 and this synthesis;
- [`../mean_field_peeling/quadratic_compiler/README.md`](../mean_field_peeling/quadratic_compiler/README.md): add campaign-local entries and exact claim levels;
- [`../mean_field_peeling/README.md`](../mean_field_peeling/README.md): update
  its maintained-source summary as above.

The theory index needs no new D13 certificate entry because Campaign 6
created none.  Bulk logs, binaries, caches, and transient checkpoints remain
outside the durable Git artifact set.

## Final portfolio bottom line

Campaign 4 materially strengthens the exact finite-order evidence: the first
ordinary and shifted $2\times2$ output Hankel inequalities survive over the
entire independent two-block metric quadrant.  Campaign 6 correctly stopped
after its bounded methods proved incapable of separating the next canonical
threshold and after its mandatory interpretation gate was found incomplete.
Campaign 5's exact low-order extension and two necessary moment signs are
useful, but its Hankel endpoint is inconclusive.  The four-input prerequisite
is therefore unmet, and the
metric-ray order-eleven pilot is stopped on marginal-value grounds rather
than allowed to begin another potentially expanding coefficient campaign.

$$
\boxed{\text{one stronger finite certificate, two inconclusive endpoints;
central conjecture still open.}}
$$
