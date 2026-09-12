# Independent relevance and placement screening

Date: 2026-09-12. Selector: `/root/relevance_selector`.

**Verdict: accept the complete combination for canonical assembly in a new
C.4.9 subsection of docs/global_nonlinear.md.** The suitable scope is a short
nonlinear slow-time selection theorem for the stated single-added-atom family,
with whole-circle prediction capture and positive added-atom risk and paired
second-hidden-activation margins. This is a relevance and placement decision,
not acceptance for promotion, a complete adversarial PASS, or user approval.

The coordinator's final ready notice was received, SLOW_SELECTION.md was read
completely at its supplied frozen hash, and the corrected FINITE_CAPTURE.md
was reread completely. The scientific sections 1–4 of the subsequently allowed
CONTROL_TUBE_APPLICATION_NOTES.md were also read. The verdict concerns these
final component inputs together; no canonical assembly was reviewed.

## Result being selected

Keep the established two-hidden-layer tanh model, Gaussian initialization,
stored variances `(1, 1/n, 1/n^2)`, raw mobilities `(n, 1, n)`, output division
by `n`, and unhalved square loss. In normalized inputs, let

\[
 \nu_*={1\over2}\delta_{(e_1,1)}+{1\over2}\delta_{(e_2,-1)},\qquad
 \mu_{\varepsilon,p}=(1-\varepsilon)\nu_*+
                     \varepsilon\delta_{(u_\alpha,y)},
\]
\[
 u_\alpha=(\cos\alpha,\sin\alpha),\qquad
 p=(\alpha,y)\in[\pi/4-1/1216,\pi/4+1/1216]\times[3/8,5/8].
\]

Physical inputs are `sqrt(2)u`. The reference endpoint `theta_dagger` is the
actual fitted population endpoint of C.4.5 on its original Gaussian carrier.
With `G=(g(e1),g(e2))`, `M=G*G`, and `Pi=I-G M^{-1}G*`, the combination
constructs a unique strong trajectory on a common positive interval satisfying

\[
 \dot{\bar\theta}_p=-2(f_{\bar\theta_p}(u_\alpha)-y)
                  \Pi_{\bar\theta_p}g_{u_\alpha}(\bar\theta_p),
 \qquad \bar\theta_p(0)=\theta_\dagger.
\]

It preserves the two fitted reference predictions. The original, fixed-mixture
population GF, trained from the original initialization, selects this path at
`t=tau/epsilon`, uniformly over the parameter box and every compact slow-time
interval `[tau_min,tau0]` with `tau_min>0`. Whole-circle prediction follows
from the full latent trajectory. The corresponding actual finite GF prediction
and paired hidden observations are captured by taking width to infinity at
each fixed positive epsilon and only then taking epsilon to zero.

At the common final slow time, the added atom's squared error decreases by a
strictly positive uniform amount relative to the fitted reference predictor.
A fixed-readout contrast proves a strictly positive uniform paired displacement
of the second hidden activations at `(e1,e2,u_alpha)`. The same-array finite
reference comparison is at the same physical time `tau/epsilon`; its population
limit approaches the fitted endpoint afterwards. No finite-width endpoint is
required. Choose the final common episode as the minimum of the construction
and activity intervals.

## Exact comparison with established coverage

| Established source | Existing result and boundary | Distinct value of the proposed combination |
|---|---|---|
| C.4.1–C.4.3 | Local canonical strong evolution for general bounded-label circle laws, stability and sampling replacement, and joint sampling/width capture of raw GD on the local interval. | The candidate starts its limiting constrained trajectory at a learned endpoint and identifies it from original mixture training on a singularly long physical interval. The local theorem alone supplies neither step. |
| C.4.5 | Global fitting and a determining whole-circle predictor for the special two-atom reference; quantitative finite-time behavior in a very small neighborhood of that reference, actual finite-network capture, and early paired movement of both hidden layers. It excludes a global changed-law flow or changed-law fitted endpoint theorem. | The fitted reference endpoint is a dependency. The candidate identifies an additional nonlinear episode selected after fitting by a specified changed law. Its late second-hidden margin has a different baseline and time scale from the early two-layer activity theorem. |
| C.4.6 | Actual finite-GF first response at every fixed physical horizon, followed by the width limit; a bounded homogeneous reference propagator and controlled forced response; endpoint normal/tangential decomposition through the limiting projection. | The projection is existing structure. A unique moving constrained trajectory, its whole-circle predictions, and its selection by the original fixed-mixture evolution at `tau/epsilon` are new conclusions. First response, including an `O(T)` forced bound, does not establish them or the nonlinear risk margin. |
| C.4.7 | Constructed nonlinear changed-law flow and actual finite-GF capture through physical time 40 near the reference, for a substantially broader class of Borel laws; finite-contamination first-order identification with a width-first remainder. | The candidate trades that broad law scope for a single-atom family and a physical interval growing like `1/epsilon`. It proves the additional source control and actual-feedback continuation needed on that interval. It does not supersede the broader fixed-time result. |
| C.4.8 | Actual influence, uniform first and second mass response and statistical prediction fluctuation results through fixed physical time 40, including whole-circle function-space statements. | The candidate supplies deterministic nonlinear selection on a different time scale, not a new influence expansion or fluctuation theorem. Extending fixed-order response estimates to this scale is not its proof. |
| III.F.1–III.F.11 and A.1–A.4 | Common Gaussian carrier, actual adjoint and source corrections, fixed-program laws and observation extensions, strong-chain and scalar-gradient conventions. | These remain foundations. The candidate preserves their finite-program order of limits and derivative conventions; it adds a duration-independent controlled source estimate and its nonlinear application. |

The scientific gain is distinct, even though the model, reference endpoint,
canonical gradient and fixed-program capture machinery are shared. The new
control estimate is a necessary part of the gain: closeness in total control
mass to the full original reference history replaces a bound tied to physical
time 40. It includes the reference tail after a prefix, each old source slot,
the current passive query, and controls on cells with zero reference mass.
Omitting these features would leave the endpoint and long-time application
unsupported.

## Assumptions and integration check

The conditional statements in the individual modules form a closed proposed
combination at the screening level:

1. CONTINUATION_CONTROL_TUBE proves uniform source caps, query tails and
   controlled completion for deterministic control histories in its full
   reference-history tube. The allowed application notes spell out the
   endpoint-prefix passage and named-source continuity conventions.
2. SLOW_SELECTION verifies this tube condition for the actual-feedback Euler
   programs before completing their trajectories. Its residual recurrence and
   first-exit argument supply continuation through the required physical
   interval. Its construction from arbitrarily long reference prefixes
   supplies the common constrained existence interval used by
   CONDITIONING_ACTIVITY. Neither actual-mixture existence nor the endpoint
   source cap is left as a theorem premise.
3. The along-path `L4` estimates justify differentiation of `G`, `M` and
   `B=G M^{-1}`. The exact identity `theta'=epsilon V+B r'`, its product-rule
   integration, and the residual bound identify the singular limit. This
   avoids assuming an ambient twice differentiable vector field or extending
   a finite-order response expansion to long times.
4. CONDITIONING_ACTIVITY supplies strict three-input endpoint conditioning
   and nonlinear finite-episode risk and second-hidden margins. Its common-time
   premise is supplied by SLOW_SELECTION; its finite paired observation premise
   is supplied by FINITE_CAPTURE and SLOW_SELECTION's joint-program bridge.
5. The corrected FINITE_CAPTURE retains the actual finite Gaussian readout.
   Its fixed-oracle cutoff induction handles the vanishing readout error
   before the actual-GF comparison. The finite bridge needs only a fixed
   positive epsilon's finite horizon; no uniform-in-epsilon width estimate
   or finite-width endpoint assumption enters.

No apparent blocking correctness gap was identified in this comparison.
This statement is limited to relevance screening and the displayed
cross-module dependencies; it is not the complete proof audit required of
the final two reviewers. The cap closure, endpoint-prefix limit, actual-feedback
Euler stopping argument, strong product rule, and finite-readout bridge remain
substantive parts of the final review packet. They cannot be replaced by a
statement that another author checked them.

Keep these qualifications in the canonical theorem and summaries:

- The open family is the relative interior of the displayed position/label
  rectangle for one added atom. It is not an open ball of arbitrary data laws.
- The theorem gives a common positive, potentially very small slow-time
  episode. It does not establish all slow times, convergence to a new fitted
  endpoint, or global changed-law fitting.
- The original-mixture selection limit excludes slow time zero. Population
  convergence is uniform in the parameter box; the stated finite-network
  probability limit is for each fixed parameter. There is no arbitrary joint
  width/epsilon rate and no raw-GD extension.
- Risk improvement concerns the newly trained atom relative to the fitted
  reference. Whole-circle prediction determination is not an unseen-risk,
  teacher-risk or superiority-to-a-frozen-model theorem.
- Positive late activity concerns paired second-hidden activations. It does
  not prove a late first-hidden margin. Comparisons use the same neuron
  indices and initialization, not a chosen coupling of separate marginal limits.
- The constrained strong flow and its reached-state restart are on the
  canonical carrier and the proved local region. Finite-program approximation
  does not assert an exact finite-dimensional closure of the latent state.
- Positivity constants come from qualitative endpoint conditioning and uniform
  estimates. They are not advertised as useful numerical lower bounds.

## Smallest suitable placement and maintenance cost

Add **C.4.9, “Slow nonlinear prediction selection from the fitted reference”**
to docs/global_nonlinear.md. This continues the reference/response/nonlinear
sequence in C.4.5–C.4.8. A new chapter would separate the theorem from nearly
all its dependencies; merging it into C.4.6 would conceal its different
nonlinear and time-scale conclusion; merging it into C.4.7 would blur its
narrower law family and stronger time horizon. C.4.8 needs no new statistical
claim. Only concise navigation and scope updates in docs/README.md and the
C.4 overview are needed; no maintained code addition is justified here.

The canonical subsection should contain one theorem with its exact limit
order, followed by the controlled-source lemma and endpoint application,
conditioning and activity argument, constructed strong selection proof, and
actual finite-GF transfer. Reuse canonical model and gradient notation,
the established reference construction, existing explicit source identities,
and III.F's fixed-program theorem by precise cross-reference. Retain all new
control-mass transport, cap closure and selection estimates in the canonical
proof. Incorporate the application notes' scientific details where used,
rather than leaving a dependency on an author-check file. Remove historical
route references and reconcile state names, physical versus normalized inputs,
and local conditioning constants during assembly.

Maintenance cost is substantial: the four components total 2,715 lines before
the 330-line scientific supplement, whereas the current destination chapter
has about 13,000 lines. These source lengths include repeated setup, source
interfaces and finite-capture explanations; they are not a recommendation to
append all files verbatim. The distinct long-time selection result warrants
one complete subsection, but not parallel restatements of the endpoint,
first-response theory, broad fixed-time law theorem or fixed-program
foundations. The assembled proof must remain self-contained through established
canonical references and proceed to the separate paired reviews and user
approval required by Part 2.

## Assignment and independence

The assignment is to compare the complete proposed combination of
CONTINUATION_CONTROL_TUBE.md, CONDITIONING_ACTIVITY.md, FINITE_CAPTURE.md and
SLOW_SELECTION.md with the established book, assess distinct value, scope,
duplication, assumptions and maintenance cost, and select the smallest suitable
destination. It is not an authoring task, a search for a rescue proof, or either
of the two required complete adversarial reviews.

This selector started in a fresh context with the neutral scoped assignment.
It did not author or assemble any candidate. The coordinator supplied allowed
source paths, the proposed scope, readiness information, contributor metadata
and intended assembly placement. Coordination messages also contained
author-completion assertions; these were not used as scientific evidence.
No study README, route file, source-coverage file, verification report,
prior verdict, task history, other study or other reviewer's findings was read.
Historical file names and internal author check statements occur inside the
permitted candidate files; those statements were not used as evidence of
correctness. Repository status was inspected as metadata only. The selector
did not follow links to historical sources from the candidates.

Contributor identities supplied by the coordinator:

| Component | Author / assembler |
|---|---|
| CONTINUATION_CONTROL_TUBE.md | `/root/continuation_route` |
| CONDITIONING_ACTIVITY.md | `/root/conditioning_route`; its fixed-readout contrast was suggested by coordinator `/root` |
| FINITE_CAPTURE.md | Coordinator `/root` |
| SLOW_SELECTION.md | `/root/geometric_route`, using explicit coordinator candidate algebra and the source module |
| CONTROL_TUBE_APPLICATION_NOTES.md, scientific sections 1–4 | `/root/continuation_route` |
| Future canonical assembly | Coordinator `/root` |

The selector is distinct from all of these contributors and is ineligible to
serve as one of the final paired reviewers. The coordinator remains the sole
Git writer. This selector writes only this report; no established file, Git
index or other study artifact is changed.

## Actual source coverage

The following complete ranges were read, including displayed proofs. Initial
long-output truncations were repaired by narrower subsequent reads. Hashes of
line ranges include the original line endings, using one-based inclusive
ranges. Headings elsewhere in the two established chapters were searched only
to locate the assigned sections.

| Source | Actual coverage |
|---|---|
| AGENTS.md | Complete |
| RESEARCH_WORKFLOW.md | Complete, including all of Part 2 |
| docs/README.md | Complete, 284 lines |
| docs/NOTATION.md | Complete, 98 lines |
| docs/global_nonlinear.md | A.1–A.4 and following B heading, lines 1840–1902; C.4 introduction and complete C.4.1–C.4.3, lines 3836–4947; complete C.4.5–C.4.8, lines 5269–12991 |
| docs/special_data_limits.md | Complete III.F.1–III.F.11, lines 3785–4326; the adjacent established III.S, lines 4327–4583, was also returned by an overinclusive range and read, but is not used in the screening conclusion |
| CONTINUATION_CONTROL_TUBE.md | Complete, 873 lines |
| CONDITIONING_ACTIVITY.md | Complete, 687 lines |
| FINITE_CAPTURE.md | Complete initial 161-line version, then complete corrected final 175-line version; final hash below |
| SLOW_SELECTION.md | Complete final 980-line version, after ready notice |
| CONTROL_TUBE_APPLICATION_NOTES.md | Introductory material and complete scientific sections 1–4, lines 1–330; later author-review/hash sections not read |

The scientific complement of the established book was not audited. In
particular C.4.4, the main global theorem, the full B.1 and C.1–C.3 proofs,
other special-data sections, and maintained code were not read in this
screening. The selected sources contain the reference endpoint construction,
its source proof, the source/control algebra needed for comparison, actual
finite capture and the current nonlinear/statistical boundaries. No result
from the unread complement is used to certify a new candidate proof. No
external theorem or literature-priority claim is imported. The offered
CANONICAL_STATEMENT_DRAFT.md was not read; this decision precedes review of a
canonical assembly.

Required skills read completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md`
and `/etc/codex/skills/investigate-conjectures/SKILL.md`. Applicable references
read completely: research-contract.md, evidence-ledger.md and
adversarial-audit.md under the latter skill. No experiment-design or proof-search
reference was needed because no new research or experiment was performed.

## Source hashes

The observed Git HEAD before substantive work and again after the established
comparison was `03c92125fdb930608e1a44c192c601bc352a2b0d`; the shared staged list
was empty. Other work was present and preserved. The chapter content hashes
below agree with those printed inside the candidate components.

| File | SHA-256 |
|---|---|
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| docs/README.md | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| docs/special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| CONTINUATION_CONTROL_TUBE.md | `175492fdd14a51395187cb586f2aa63b634bd688a01cbd84f3a9a043efd06cbc` |
| CONDITIONING_ACTIVITY.md | `ad0d84de8803be29b21da6aa9ea66a4b9276559a258644fcd0179a4212625243` |
| FINITE_CAPTURE.md, corrected final version | `3b3201e262f0165534c92607d25633fb98fa0cc1f8bf8de7a3bdc83264825e44` |
| SLOW_SELECTION.md | `79b6d1e0fc9992c62f20eedaafc05baf42cf10394de647be4f12910350665442` |
| CONTROL_TUBE_APPLICATION_NOTES.md, complete-file fingerprint only | `2aa6a7b8c0490079697d3fe44e2fe5e0ed72d59825db43c0609189c4e242779c` |

All listed instruction, guide, chapter and final component hashes were checked
again before freezing this report and were unchanged. The initial finite
bridge was edited between its first read and its first hash operation; no
reliable hash is assigned to that superseded 161-line read. Only the corrected
175-line version is the final input here. The application-notes full-file
fingerprint does not imply that its unread later sections were consulted.

| Exact established range | SHA-256 |
|---|---|
| global_nonlinear.md:1840–1902 | `b8d0c759f9f423c5465a6c08f2ac20be077d78bd6d0db124b287436bfc23e352` |
| global_nonlinear.md:3836–4947 | `d81dfa74ae7df7b94fdff3e94657b002de7287407c19af999196f3a572a8107f` |
| C.4.5, global_nonlinear.md:5269–6902 | `4e35f6b1dc336083aaefc4cc8ad15a40e42af1e6b93eadc37da0a32a32b00933` |
| C.4.6, global_nonlinear.md:6903–8976 | `0bcc4bdf9ea8a02fa7337b42b09395924097f109a56191354e4129806ba071eb` |
| C.4.7, global_nonlinear.md:8977–11439 | `afd6a78ff9c25dfe06847730ae54f6ec41ab3129c8b10dc3d11e097774a10a3b` |
| C.4.8, global_nonlinear.md:11440–12991 | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| III.F, special_data_limits.md:3785–4326 | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| Incidental III.S, special_data_limits.md:4327–4583 | `3f1229c938625f6ddd80a3dc2d8e0554b5b522687d91c911a3d70c4747a550ed` |
| CONTROL_TUBE_APPLICATION_NOTES.md:1–330, actual scientific input | `f4b43a2349a015ad09de3fcd13c253e93ca44b5c61fdf46ea9461d0b8984727a` |

| Skill/reference | SHA-256 |
|---|---|
| solve-math-rigorously/SKILL.md | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| research-contract.md | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| evidence-ledger.md | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| adversarial-audit.md | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

Hashing, bounded source reads, shared Git metadata checks and writing this
report were the only executed operations supporting this screening. No training run,
numerical approximation of the learned flow, certificate rerun, code test,
Git mutation or external retrieval was performed. The complete proof and
reproduction gates of Part 2 remain separate from relevance screening.
