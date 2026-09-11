# Independent complete adversarial review B — frozen C.4.8 version 2

**Verdict: PASS for the entire frozen mathematical package and its stated scope.**
I found no required mathematical correction and no missing scientific input.
The bounded, centered actual influence, the Hilbert mean-square sampling
remainder and Gaussian limit, and the width-first actual finite-GF bridge are
supported by the supplied proofs. This is one independent scientific review;
it does not replace the other review, integration review, or promotion approval.

Reviewer: `/root/review_v2_b`. Review date: 2026-09-11 (UTC).

## Isolation, ownership, and complete reading

I worked from the neutral `review_packet_v2.md` assignment in a fresh reviewer
context. I am distinct from `/root`, `source_response_route`,
`statistical_route`, `weak_topology_route`, `promotion_selector`, and reviewer A.
I did not author or assemble the candidate. I did not read another version,
another review, an internal or selector report, author components, the study
README/history, another study, or Git history. I used no inherited verdict.
No communication with the other reviewer occurred. The coordinator's late
metadata-only status request supplied no scientific finding; my input-integrity
verification was performed independently.

I personally read every scientific line in these exact scopes:

| Input | Complete read coverage |
|---|---|
| `proposal_C4_8_v2.md` | 1–1552, including all response and statistical proofs |
| `promotion_edits_v2.json` | 1–23 |
| `check_gaussian_calculus.py` | 1–146 |
| `check_sampling_hoeffding.py` | 1–368 |
| `docs/global_nonlinear.md` | 1840–2453; 2924–3440; 3836–4946; 5268–11436 |
| `docs/special_data_limits.md` | 3785–4286, complete III.F.1–10 |
| `docs/finite_dynamics.md` | 1–227, complete §§1–4 |
| `docs/README.md` | 1–284 |
| `docs/NOTATION.md` | 1–98 |
| `AGENTS.md` | 1–47 |
| `RESEARCH_WORKFLOW.md` | 1–224, including all promotion requirements |

The global-nonlinear read comprises 8,411 assigned lines. Its unread complement
was not a scientific input. Complete-file hashing is an integrity operation,
not a read of that complement's scientific contents. I read the two required
skills `solve-math-rigorously` and `investigate-conjectures`, and the latter's
applicable `adversarial-audit.md`, `research-contract.md`, and
`decisive-experiments.md` references. This was a proof review and deterministic
verification, without training experiments, sweeps, or external retrieval.

Truncation repairs: an initial combined guide/process read was followed by a
complete separate read of `docs/README.md` and `docs/NOTATION.md`; the workflow
was also reread completely. A candidate read omitted part of its first source
section, so lines 132–292 were reread explicitly. A combined dependency read
truncated finite dynamics; all of lines 1–227 were reread separately. The
remaining scientific inputs were read in consecutive bounded chunks with no
unrepaired gap. Both complete deterministic-check implementations and their
complete generated reports were inspected.

Only this report and the assigned B-owned generated scratch were written.
Candidate, established sources, instructions, and Git state were not edited.
No Git operation was performed, consistent with the neutral assignment.

## Frozen-input integrity

All eleven complete-file digests were measured before scientific reading and
again after reading and deterministic validation. In each row, **the before
digest and after digest are identical to the displayed digest** and match the
packet. The explicit two-column machine record is
`data/generated/trained_prediction_sampling/review_v2_B/input_integrity.json`.

| Input | SHA256 before = SHA256 after |
|---|---|
| `studies/trained_prediction_sampling/proposal_C4_8_v2.md` | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| `studies/trained_prediction_sampling/promotion_edits_v2.json` | `50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c` |
| `studies/trained_prediction_sampling/check_gaussian_calculus.py` | `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef` |
| `studies/trained_prediction_sampling/check_sampling_hoeffding.py` | `4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a` |
| `docs/global_nonlinear.md` | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/README.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

## Mathematical audit and actual attacks

### 1. Model, carrier, and dependency closure — PASS

The candidate uses the same two-hidden-layer tanh network, full first row,
unhalved law-integrated squared loss, stored variances `(1,1/n,1/n²)`, and
mobilities `(n,1,n)` as C.4.7. The finite rank is `Δhᵀ/n`; its ordinary
Frobenius norm equals the product of the two normalized vector norms. Thus the
Hilbert–Schmidt increment and end-block normalizations match the actual finite
gradient flow. Population zero readout is the limiting initialization; the
finite random readout remains present in the final bridge.

I checked the needed established argument rather than accepting the C.4.7
label. III.F constructs the common generated action and its actual adjoint by
fixed-program conditioning, singular-query regularization, finite unions, and
dense completion. A.1–2 supplies value and named-source extensions for the
unbounded backward products. C.4.7's cap is obtained through separate clock-to-
raw and law-transport inductions, not the unsatisfiable absolute cap inequality
N19. Its weighted source pulse, old-source density, and same-passive-input
comparison prevent dependence on inverse atom masses or the maximum cost of a
far low-mass contaminant. The raw comparison upgrades to Hilbert–Schmidt norm
with the exact rank inequality. Strong completion identifies the actual
equation and gives value continuity and finite GF capture.

The C.4.5 reference fitting and its strict numerical margins are backed by the
contained rational certificate, which I reran. C.4.6 keeps finite-first
differentiation separate from population response; its weighted query proof
uses a learned cavity with its own residuals, conditional estimates on the
column-independent event, and the actual finite readout. C.4.7 identifies its
contamination derivative with that same response. The C.4.8 identification at
the reference therefore has the stated dependency, while the new proof at
general base laws does not require a finite-network tangent theorem there.

### 2. Exact source recursions and frozen source derivatives — PASS

I recomputed the two orientations in S2–S7. The forward coefficient is
`α + γ Cξ`; the reverse coefficient is `β + 1_past γ Cζ`. The current
reverse coefficient is `E[c φ″(Z)]` for the distinguished current slot only.
Duplicated or singular source slots retain their prescribed coordinate
expressions. Treating every current input as an additional diagonal response
would give a spurious support-size factor; the displayed recursion avoids it.
Residuals, contractions, and covariance entries are frozen only for these
named-source derivatives, not for the mass responses later in the proof.

I attacked the possible accumulation of unweighted Gaussian maxima and repeated
source diagonals. S10 uses the weights `h_k p_a/T`, adding unused time mass at
zero when needed. It bounds the exponential moment of the integrated weighted
absolute query without time or input independence. In S11–S15 the full tensor
sums satisfy product and partition inequalities. The highest lower jet has
coefficient `2R₀D₀ + 4R₀ q_k`; its integrated propagator has every fixed finite
moment. The remaining terms use lower jet orders. This proves the stated
moment induction without applying `A₀` on arbitrary Lp input spaces.

For the upper jets, the forward coefficient density `f₀ h_s p_a`, bounded
readout, and strictly earlier memories give the pointwise scalar Volterra
bound S16–S17. Repeated differentiation of one old source keeps one injection
mass; the proof correctly uses tensor sums rather than inventing a product of
masses. The increment estimate S18 retains an interval-length factor after
every fixed source derivative because each differentiated difference contains
an increment jet. Its maximum over nodes is bounded by the absolute update
sum. These facts are precisely the input needed for the later cancellation.

### 3. Full mass response and mesh-uniform closure — PASS

I checked S19–S20 by differentiating the Gaussian density: there are two mixed
parameter/source terms with factor 1/2, a covariance second-derivative term
with factor 1/2, and the two-covariance fourth-source term with factor 1/4.
Adding `ηI`, applying integration by parts, and passing uniformly on compact
parameter sets establishes the formulas also at rank loss and one-sided
boundaries. This differentiates covariance entries, not covariance square
roots. At each fixed graph the required polynomial envelopes exist; their
degree need not be uniform in graph length. The later tensor estimates,
rather than that fixed-graph envelope, provide the uniform bounds.

The chronological order is legitimate. Current lower expressions depend only
on earlier reverse slots and coefficients. They first determine forward
covariances and α; forward and upper expressions then determine β and reverse
covariances before the lower update. There is no current-node fixed-point
equation hidden inside the Gaussian derivative formulas.

I verified all product terms in S23–S27 and S37–S42. In particular the mass
derivative of `γ=-2hp r` contains both the direct mass and residual response,
and its mixed derivative contains both mass/first-response cross terms.
Covariance responses enter every expectation through S22 and S38. The second
recursion retains all readout, gate, action-coefficient, and residual cross
terms; its highest unknown is linear with the same base coefficients.

The principal attack was whether S28 requires a time partition that becomes
finer as derivative history or moment order grows. It does not. For a fixed
interval, explicit lower responses are linear combinations of history,
direct mass forcing, and current coefficient forcing. The last part contains
an interval sum and is bounded by `C_{j,p} ℓ E`; its constants use only base
jets and moments. Products involving old responses enter the additive history
term. After splitting the reverse-covariance matrix into old-old and remaining
blocks, a new source derivative annihilates the boundary lower expression.
S18 therefore makes the remaining Gaussian terms `CℓE`, including the full
α-row sum (third source derivatives).

This first controls forward covariance and α, then F, then upper explicit
responses, upper covariance, β and D. The chain S32–S36 bounds every component
of E. Only low fixed source orders and finitely many finite base moments are
used to select `C_*ℓ≤1/2`. Once E is absorbed, higher separately fixed moments
follow without further absorption. The number of groups is bounded by
`2T/ℓ+1`, independent of the mesh. For second mass response the products of
first responses are known forcing of size `CS R`; the new unknown covariance
uses exactly the same boundary cancellation. The fifth base source tensors
and third explicit first-response tensors required by S38 are already
available. Thus S43 closes with base-dependent interval size as claimed.

This verifies the actual mechanism for S1/P7. A generic smooth ODE theorem on
an ambient L² ball would not justify that conclusion and was not substituted.

### 4. Boundary masses and actual Borel-law influence — PASS

For a fixed support, the finite chronological expectation formulas extend to
zero masses by Gaussian regularization and finite-graph polynomial envelopes.
Admissible segments and rectangles are limits of interior ones. Neither the
uniform constants nor the recursions divide by positive masses. The zero
direction gives zero response, and adding a new atom is covered by a zero-mass
slot. Appending a shorter last Euler step represents a recomputed observation
at an interpolation time, so the full time interval and passive circle are
covered.

The nested radii have adequate slack: a law within `δ_Y/2` contaminated by at
most `min(1/2,δ_Y/(4D_Y))` moves by at most `δ_Y/4`. The finite derivative
bound therefore holds throughout the required segment in the larger analytic
region. The uniform second derivative gives the `2Mε²` contamination
remainder. Comparing two mesh derivatives with the same forward quotient
produces a `4Mε` limsup difference, so pointwise value convergence in
`C(circle)` suffices to construct the actual derivative in that space.

I attacked the use of empirical or quantized laws for nonatomic μ. The proof
does not require total-variation convergence. The forward quotients are
jointly continuous in `(Q,z)` under W1, and their uniform Cauchy estimate
extends from finite laws by density. Their uniform limit is jointly
continuous on the compact law/atom domain. This supplies both Bochner
measurability and boundedness. Centering first follows from the exact finite
mass identity and then passes by weak convergence of integrals of continuous
Banach-valued functions. The finite partition-of-unity argument given there
justifies this norm convergence.

Common finite quantization contracts variation mass for the admissible law
segments and rectangles used later, and their open analytic region leaves
the necessary transport slack. Thus P11 identifies actual mixture derivatives
as integrals of the centered field; P12 requires only four value limits.
No second derivative of the completed flow is silently assumed. P13 provides
an explicit recursion-and-limit characterization independent of mesh and
quantization. It retains the actual three trained blocks and source feedback.

### 5. Localization and Hilbert sampling remainder — PASS

I independently checked the sampling argument. R3 implies the one-dimensional
derivative Lipschitz bound by a small parallel rectangle and hence Taylor's
estimate R9, including one-sided endpoints. Boundedness of F and a fixed
contamination length give the local bound on every atom response in R10.
The diameter-zero case is separately disposed of by centering.

The finite continuous test partition yields R11 by two transports of cost
`2ε` and a discrete unmatched-mass coupling. With the displayed b, the cutoff
support lies inside the radius-`r_loc/2` ball. Its first and second kernels are
bounded. The product identity R14 is exact; the localized first kernel is
centered correctly. A sufficiently fine rectangular subdivision works for
the stated open cover, and summing its mixed differences gives the global
bound with the sum of side-length products equal to one. This closes the
exceptional-law problem without assuming a global population flow. The
bounded-variable exponential-moment calculation gives the stated exponential
probability for leaving the finite-test neighborhood, for every Borel μ.

The bias telescoping uses a fresh independent observation at each step; its
linear term has conditional mean zero even though the intermediate kernel is
centered under a different law. R17 follows with size `2M_*/m`. For the Hilbert
Hoeffding decomposition, inclusion–exclusion, conditional centering and
orthogonality hold for Bochner conditional expectations. A double replacement
has four orthogonal copies for each component containing the two replaced
indices. The factor 1/4 in R19 is correct, and `||D_ijT||≤4M_*/m²` gives the
claimed `2M_*²/m²` higher-order bound, including m=1 when the pair sum is empty.

The base `Q_m=μ/m + Σ_{j≥2}δ_{Z_j}/m` keeps the first-projection Taylor segment
inside probabilities, including atomic and nonatomic μ. Centering its quotient
introduces at most `4M_*/m` error. W1 convergence and the assumed L²(μ;H)
continuity, with a bounded global kernel, justify convergence of its expected
squared difference. Bias, higher components, and the centered first-projection
error are orthogonal, giving exactly R23. Its three terms prove
`m E||r_m||²→0` without a quantitative W1 rate or a modulus rate for the
influence. Bounded extensions transfer this result via the exponentially rare
exceptional event; arbitrary finite-valued extensions give only the stated
probability transfer unless the additional moment condition holds.

### 6. Gaussian covariance, spatial tests, and actual finite GF — PASS

The population map has no external random environment. The centered bounded
H-valued influence is square integrable. Positivity, self-adjunction, and the
trace formula follow by Tonelli and Parseval. The Gaussian series converges in
L²(H) because its eigenvalues are summable. Zero covariance and singular rank
are admitted. The scalar characteristic-function expansion has its dominated
second-order remainder, finite-dimensional projections have the Gaussian
limit, and their orthogonal tail second moment is uniform in sample size.
The bounded-Lipschitz projection comparison therefore proves the Hilbert CLT.
The mean-square remainder and Cauchy–Schwarz also give the trace/m expansion.

The continuous atom-to-`C(circle)` field makes the displayed spatial kernel
continuous. Boundedness justifies Fubini and identifies its integral operator
with the Hilbert covariance. The theorem concerns H convergence and continuous
linear spatial tests; it does not claim a stronger function-space CLT from
the Hilbert argument alone.

For all finite sample outcomes, including laws outside U_Y, P18 gives finite
time bounds in the correct raw finite norms. Local smoothness and these
bounds prove continuation and measurable H-valued endpoint predictions. The
loss need not have a population solution on the exceptional outcomes.

At each fixed m, conditioning on the observations leaves the prescribed
initialization unchanged. On `μ_m∈U_Y`, C.4.7.NW1 applies to each separately
fixed law. Convergence in initialization probability of the capped error
implies convergence of its conditional expectation, and bounded convergence
then integrates over samples. On the complement, two bounded-Lipschitz test
values differ by at most two. Thus P20 follows without any finite-width moment
or rate assumption. Taking width first at fixed m, and only then m→∞, proves
P6. A simultaneous fluctuation rate or a finite-width derivative interchange
has not entered this argument.

## Deterministic validation and evidence

All commands below ran from `/home/amir/Codes/PDE`, with Python 3.10.12, and
exited zero. No randomness, training, or numerical integration of a learned
trajectory was used.

```text
python studies/trained_prediction_sampling/check_gaussian_calculus.py --output data/generated/trained_prediction_sampling/review_v2_B/gaussian_report.json
python studies/trained_prediction_sampling/check_sampling_hoeffding.py --output-dir data/generated/trained_prediction_sampling/statistical_checks/review_v2_B
python data/generated/trained_prediction_sampling/review_v2_B/reference_certificate.py
```

The Gaussian program uses independent-normal substitution and rational
polynomial arithmetic as its oracle. All six identities passed, including
the rank-one line in a changing-rank covariance family. The Hoeffding program
fully enumerates 16 Bernoulli states and six replacement pairs with exact
fractions. All 748 checks passed. Every order 1–4 is nonzero, and the pair
bound has strict slack `30270672/390625`. The exact remainder identity has
both sides `548332/3125`, with all three orthogonal contributions nonzero.

I extracted the complete contained reference certificate from the allowed
C.4.5 dependency body into B scratch and reran it unchanged. Its output was

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

The exact assertions certify q>.39, q<.4, v>.2, a₀>.3 and r₀>.6, including
the reference m≥.1 bound. Decimal output is only a summary of those rational
inequalities.

Supplemental reviewer checks, retained in
`review_v2_B/supplemental_identity_checks.json`, verified R14 on nontrivial
exact rational corner values (both sides `-115/231`), the zero-rank Gaussian
boundary `C(t)=t`, `G(x)=x⁴` (second derivative 6 at t=0), and the finite
rank normalization at n=3 (both squared quantities `98/3`). These are identity
checks; the neural estimate and asymptotic conclusions rest on the proofs
audited above. Each proposed summary replacement has exactly one occurrence
in its authorized read scope, and its wording matches the theorem's fixed
horizon, smaller-law-neighborhood, mean-square and width-first scope.

| Generated evidence | SHA256 |
|---|---|
| `review_v2_B/gaussian_report.json` | `74379f1ba103d4dbb1f24ab221c3d38eb247ac3d364339b07a828f1378342e6c` |
| `statistical_checks/review_v2_B/report.json` | `66f0e6937881ee30b64169b97880ac9ff97a27a70933e6a077902d3d16731275` |
| `review_v2_B/reference_certificate.py` | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| `review_v2_B/reference_certificate_output.txt` | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` |
| `review_v2_B/supplemental_identity_checks.json` | `dcecf4fd0753e8ddc2aa0bc773e5ae65f3ccea17a83b26cccd2a593aed8ff5c7` |
| `review_v2_B/input_integrity.json` | `0a561bffa7e8edc643014d46667ee8b8d09ddd04eb18162bc6c672afca9ddf35` |

All evidence paths in this last table are relative to
`data/generated/trained_prediction_sampling/`.

## Required corrections, presentation, and final verdict

Required corrections: **none**. Missing inputs: **none**. Unresolved
correctness objections after the attacks above: **none**. No presentation
change is needed for the mathematical verdict.

The exact frozen candidate and its summary edits **pass** this independent
complete review. The supported conclusion is for each separately fixed Borel
law in the stated positive smaller W1 neighborhood, at physical time 40,
with the stated bounded extension and width-first finite-GF limit. It includes
no finite-width fluctuation rate, simultaneous sampling/width rate, raw-GD
extension, ambient L² tangent assertion, or nondegeneracy assertion.
