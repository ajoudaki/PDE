# Independent integration review of proposed edition v4

**Verdict: PASS for the assigned integration scope. No required correction was found.**
The assembled C.4.9 matches the frozen scientific addition, its summaries retain
its actual scope, and the complete current baseline is preserved outside the
specified changes. This verdict is an integration judgment; it is not a new
whole-book proof audit, a substitute for the separately required paired scientific
reviews, or approval to promote the edition.

## Identity, assignment and isolation

Reviewer: `/root/integration_v4`. Review date: 2026-09-12.
The neutral assignment was `INTEGRATION_ASSIGNMENT_v4.md`, 77 lines, SHA-256
`41bfc848b789bdca6d61915a1c9b9fbae7551d5cccc618a98906d400c4c0da06`.
My incoming assignment supplied the allowed files, proposed-edition identity,
expected fingerprints, output ownership and excluded identities. It supplied
no desired verdict or prior scientific finding. I am distinct from all authors,
assemblers, selectors, paired reviewers and prior integration reviewers named
there. I had no inherited author discussion, prior review or study history.

I read the shared AGENTS.md and RESEARCH_WORKFLOW.md instructions, including
the independent-review and promotion instructions, without doing author startup.
I used the complete `solve-math-rigorously` and `investigate-conjectures` skills,
and the latter's complete `research-contract.md` and `adversarial-audit.md`
references. I did not conduct a proof-search campaign, reconcile a research
history, or run an experiment. The complete solve-math skill was reread after an
initial combined output truncated part of it.

I did not read the study README, proposal, author reports, source-coverage files,
correction or refresh records, selector report, any other review, other studies,
Git history, task discussions or the producer's recorded validation verdict.
I did not inspect `validate_proposed_edition_v4.py`: the mechanical reconstruction
below was written independently. No scientific material was fetched from the web
or another agent. I did not delegate portions of this review or exchange findings
with another reviewer. The coordinator is the only recipient of my findings.
No Git command was run. I wrote only this report and my assigned scratch directory.

Shared-instruction fingerprints at the check were:

- AGENTS.md: `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba`.
- RESEARCH_WORKFLOW.md: `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12`.

## Actual complete new-material coverage

I read every line of the 2,329-line `CANONICAL_ADDITION_v3.md`, including the
source-control proof, its named-coefficient supplement, endpoint conditioning,
hidden contrast, original-mixture construction, singular limit, finite-GF bridge
and completion. The untruncated contiguous reads were 1–450, 451–900, 901–1350,
1351–1800, 1801–2250 and 2251–2329. No proof body or supplement was skipped.

| New scientific unit | Canonical lines | Assembled global_nonlinear.md lines |
|---|---:|---:|
| Statement, scope and proof architecture | 1–190 | 12994–13183 |
| Unit A, including A-supplement.4 | 191–962 | 13184–13955 |
| Unit B | 963–1427 | 13956–14420 |
| Unit C | 1428–2118 | 14421–15111 |
| Unit D | 2119–2304 | 15112–15297 |
| Completion | 2305–2329 | 15298–15322 |

For duplicate representations I read the complete shared scientific text and
checked its exact correspondence, rather than treating a matching hash as a
substitute for reading. The actual assembled suffix, lines 12994–15322, is
byte-for-byte the complete canonical text. Every line of the 2,363-line patch
was independently parsed, every old/context line was checked against the live
baseline, every hunk count and position was checked, and every produced line was
compared with the assembled file. The patch's complete scientific insertion is
therefore the same fully read text, with no omitted or altered scientific line.
I additionally read the patch headers, overview hunk, append boundary and guide
hunks in their patch presentation.

I read the complete 578-line `PROPOSED_GUIDE_v4.md`, including the full strategic
roadmap and all older summaries. The reads were 1–300 and 301–578, with 400–465
reread to repair a truncated combined output. I read the complete 577-line
`INTEGRATION_BASE_GUIDE_v4.md` in clean 1–200, 201–400 and 401–577 reads.
The actual current `docs/README.md` is byte-identical to that fully read baseline;
the assembled `docs/README.md` is byte-identical to the fully read proposed guide.
Thus the complete current and assembled guides, including their roadmap, were
covered, not just the two edit targets.

I read all 26 lines of `PROPOSED_EDITS_v4.json`, both manifests, and the complete
98-line notation contract. Current and assembled `docs/NOTATION.md` are exactly
that contract. The three new summary locations are assembled
`docs/global_nonlinear.md:3851` and assembled `docs/README.md:448,568`.
Their surrounding overview and complete guide context were read.

## Exact older scientific scope and unread complement

The complete assigned established source units were read from the original
`docs/global_nonlinear.md`:

| Unit | Original lines | Coverage |
|---|---:|---|
| C.4 overview and local theorem scope | 3836–3980 | Complete assigned unit |
| C.4.5 statement/scope and endpoint reference proof | 5269–5781 | Complete assigned unit |
| C.4.6 model, response equation and theorem | 6903–7168 | Complete assigned unit |
| C.4.7 model, theorem and observation contract | 8977–9169 | Complete assigned unit |
| C.4.8 model and theorem | 11440–11528 | Complete assigned unit |

These are 1,206 assigned original-source lines. The C.4.6/C.4.7 reads were repeated
in smaller outputs after a combined output truncated their first display.

I enlarged the allowed frozen-excerpt scope for two interface checks:

- `DEPENDENCIES_GLOBAL_v1.md:45–155`, corresponding to original
  `docs/global_nonlinear.md:1876–1986`. This includes the complete established
  A.4 scalar-gradient and strong-chain-rule unit, with adjacent A.3 ending and
  B.1 opening material exposed by the read. The point of this check was the
  scalar-gradient reference in new C.1; I did not import a new B.1 conclusion.
- `DEPENDENCIES_GLOBAL_v1.md:5585–5788`, corresponding to original
  `docs/global_nonlinear.md:8123–8326`. This includes the complete section 6
  population-envelope argument, C.4.6.S40–S45, and adjacent S39 and part of section
  7 through S48. The point was to verify the precise endpoint envelope, moment
  and simultaneous-active-clock interface used in new B.2. The preceding cavity
  proof and the rest of section 7 were not independently audited.

I also encountered the old append-boundary lines 12989–12991 as the frozen
patch's required context. They were used to verify preservation and placement,
not as an additional scientific dependency. Whole-file label searches exposed
navigation locations for A.4 and C.4.6.S40–S44. Existing III.F headings and named
C.4.7 equation tags were checked as reference-target metadata.

All other old chapter material is an explicitly unread scientific complement.
It was used only as bytes for preservation/fingerprint comparisons and as
existing heading/tag metadata for reference resolution. In particular, I did
not read the complete Gaussian dependency excerpt, the complete 8,901-line
global dependency excerpt, or the other eight unchanged documentation files as
scientific inputs. I did not audit maintained code or run its examples because
this is a documentation-only addition with no code or empirical claim. The full
guide was read as assigned, but its descriptions of other chapters did not
license importing those chapters' unassigned proofs.

## Fingerprints and exact assembly checks

Every frozen packet hash and line count in `INTEGRATION_INPUTS_v4.json` matched.
That manifest itself has SHA-256
`954199594f675752d51fd08e08bc0c58fdf539f6ea8582fa85b059b260df76c3`.

| Input | Lines | SHA-256 |
|---|---:|---|
| CANONICAL_ADDITION_v3.md | 2329 | `c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879` |
| INTEGRATION_BASE_GUIDE_v4.md | 577 | `3f341b52fa6449a4008602f573590b1528158bd1370f17bc26db032813799f5e` |
| PROPOSED_GUIDE_v4.md | 578 | `26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e` |
| PROPOSED_EDITS_v4.json | 26 | `491c43614bc1438ad55f9c0df668bb7e774f6acce457e3f6a0ed89fe3ea07b91` |
| PROPOSED_EDITION_v4.patch | 2363 | `f15934b5cf3b2b9db9bc7bab32109a8146ba9f0d31baef36d99a89ca9a0c3dbd` |
| DEPENDENCY_NOTATION_v1.md | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| DEPENDENCIES_GLOBAL_v1.md | 8901 | `6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942` |
| DEPENDENCIES_GAUSSIAN_v1.md | 550 | `c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77` |
| DEPENDENCY_MANIFEST_v1.json | 44 | `75f8b2ae6716fb88d8f89306b78a104a2bffc62e1bf67bb64474b8298d5b415a` |

The live scientific source fingerprints match the older dependency manifest:

- Original `docs/global_nonlinear.md`, 12,991 lines:
  `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05`.
- Original `docs/special_data_limits.md`, 27,274 lines:
  `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489`.

The older guide fingerprint in `DEPENDENCY_MANIFEST_v1.json` is not the live-guide
baseline for this review. I used the explicitly assigned v4 baseline instead,
and its full bytes and fingerprint equal the live guide. No old guide was
silently substituted for the current roadmap.

The assembled `standalone_v4/docs/global_nonlinear.md`, 15,322 lines, hashes to
`7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.
The assembled guide hashes to
`26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e`.

I independently reconstructed the edition in memory in two ways:

1. Apply the unique chapter-overview replacement, append one separator newline
   and the complete canonical addition; apply the two unique guide replacements
   in their specified order.
2. Parse and apply every unified-patch hunk against the live baseline, verifying
   all context bytes, deletions, line counts and resulting line positions.

Both constructions reproduce both assembled files exactly. Independently
regenerating the full unified diff reproduces all 2,363 patch lines exactly.
There are exactly four hunks: chapter overview `(3848,6)->(3848,7)`, chapter
append `(12989,3)->(12990,2333)`, guide table `(445,7)->(445,7)` and guide scope
`(565,6)->(565,7)`. No other path occurs in the patch.

Both guide old targets occur exactly once when applied. Both new targets occur
exactly once when reversed. Reversing them recovers the entire 577-line baseline.
The entire roadmap block between its heading and “Chapters and their exact roles”
is byte-preserved. Removing the appended canonical text and separator and reversing
the overview addition recovers the entire live chapter, including its unread
complement. The documentation file sets are identical: ten files, exactly two
changed and eight byte-identical. The unchanged files are NOTATION.md,
arctan_limits.md, continuous_depth.md, finite_dynamics.md,
finite_optimization_and_controls.md, gaussian_calculus.md, linear_dynamics.md
and special_data_limits.md. Their individual before/after hashes are retained
in the evidence JSON. There is no code hunk or code API change.

## Scientific interfaces, notation and summary checks

### Exact model and metric

The new theorem uses the same two-hidden-layer, bias-free tanh network as
C.4.5–C.4.8: normalized `u=x/sqrt(2)`, readout divided by n, independent centered
Gaussian stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, unhalved mean
squared loss and physical GF. The nonzero finite Gaussian readout is retained
in the actual networks and actual-readout proxies. The zero population readout
is its limit, not a finite initialization reset.

The raw state `(w,K,c)` retains the full first row and `A=A0+K`; only K is
Hilbert–Schmidt. The actual adjoint is used throughout. The finite raw metric
has the correct factors `||dW1||F^2/n + ||dW2||F^2 + ||dc||2^2/n`. The rank
identity for `ab^T/n` matches the population tensor HS norm. Every finite hidden
difference is normalized by sqrt(n), or by n after squaring; no population
operator is subtracted from a matrix on another carrier.

### Reference, endpoint and conditioning

The endpoint prescription is exactly the established reference feature equation
with the one-half weights and first `b=1` stopping time. The model's physical
clock is `ds/dt=2(1-b)`, and the imported raw endpoint bound and 76-Lipschitz
whole-circle bound agree with the complete assigned C.4.5 proof. This checks
both the factors and the endpoint used to initialize the limiting equation.

The parameter rectangle has nonempty interior in location and label, and every
added input has nonzero dot product with both anchors. The bound
`|f_dagger(u_alpha)|<=1/16` yields `5/16<=y-f_dagger(u_alpha)<=11/16`.
The resulting initial added-atom risk is at least `25/256`; it is not multiplied
by epsilon when defining the claimed gain. The family is robust within its
specified single-atom parameters, not an open neighborhood of arbitrary Borel
laws.

The imported C.4.6 envelope is a moment bound for a countable simultaneous
representative with Fubini for active clocks. New B.2 correctly uses it without
assuming independence from the initial row or sample-path continuity of all
passive queries. Its positive-probability intersection argument uses the
Gaussian-box lower bound against the envelope's much smaller tail. The subsequent
sign-pattern argument needs distinct nonantipodal directions, which the present
three-input family satisfies. The middle-block Gram lower bound does not assume
injectivity of the trained action. Its compact-family minimum supplies the
projection's finite two-by-two inverse; this adds a conditioning result and does
not misrepresent C.4.6's previously more permissive pseudoinverse scope.

### Source control, continuation and the slow clock

The source estimate is explicitly for deterministic controlled finite programs.
Named differentiation freezes deterministic controls and retains both orientations,
old source slots and the distinguished current slot. Zero controls and covariance
rank loss are handled without dividing by a reference coefficient. Unit A and its
supplement keep width, zero forcing and mesh refinement in the stated separate
orders. Nothing in the summaries turns this into a uniform probabilistic estimate
over arbitrary random finite-network controls.

The construction of the constrained episode uses full reference prefixes and
small appended control mass, retains the initialized carrier and source history,
and then completes Euler approximations by the one-reference Osgood estimate.
Existence and uniqueness are proved for the specified initialized/reached states;
they are not inferred merely from continuity on an ambient Hilbert ball. The
finite-GF bridge uses these constructed population paths rather than assuming a
changed-law endpoint or extending C.4.7's fixed-time conclusion without a new
argument.

I checked the exact residual algebra with the mixture weights. With
`r=(f(e1)-1,f(e2)+1)` and `v=r_p g_p`, the equations are
`theta'=-(1-epsilon)G r-2 epsilon v` and
`r'=-(1-epsilon)M r-2 epsilon G* v`.
For `B=GM^{-1}` and `V=-2(I-GM^{-1}G*)v`, they give exactly
`theta'=epsilon V+B r'`. The absolute-continuity estimate for B along reached
curves is supplied before integration by parts. This is the bridge to the
slow clock; a fixed-order response expansion is not extrapolated to times
of order `1/epsilon`.

The original law is fixed from physical initialization in every actual run.
The proof's reference-prefix decomposition does not prescribe pretraining or
a law switch. The uniform population slow-time convergence is on every
`[tau_-,tau0]` with `tau_->0`; excluding zero is necessary because the original
initial state differs from the fitted endpoint. The positive tau0 is fixed
independently of epsilon, even though its constants need not be practical.
Unit B's final reduction of the existence time preserves the earlier estimates.

### Risk, hidden motion and width order

The exact identities `f_p'=-2r_p||Pi g_p||^2` and
`(r_p^2)'=-4r_p^2||Pi g_p||^2` give the claimed positive added-atom risk margin.
The hidden contrast fixes the endpoint readout and coefficients, so its derivative
isolates hidden adaptation. Its strictly positive derivative is retained over
a finite interval by continuity and a first-exit bound. Cauchy–Schwarz then
produces a positive average second-hidden activation displacement. The argument
does not confuse hidden parameter movement with activation movement, and it does
not state a first-hidden displacement margin.

NS9 uses a reference network trained from the same arrays, including readout,
and compares it with the mixture network at the same physical time. Joint
same-layer proxy observations preserve this pairing. Only after fixed-epsilon
finite-width capture does the population reference tend to its endpoint as
epsilon decreases. Thus the final hidden quantity is late second-layer motion
relative to matched reference fitting, not early movement from initialization.

For every fixed epsilon the horizon `tau0/epsilon` is finite. Unit D takes width
first with a fixed proxy mesh and cutoff; those proof choices may depend on the
fixed epsilon. Its cutoff is chosen before making the mesh sufficiently fine.
The result supplies neither a simultaneous width/epsilon rate nor raw-GD
capture. Auxiliary raw Euler programs are proof approximations, not a theorem
about the raw-GD optimizer.

### Guide, placement and references

The new chapter overview and both guide summaries accurately identify the
finite nonlinear episode, original fixed-mixture training, whole-circle
prediction, added-atom risk, paired second-hidden adaptation and width-first
finite-GF bridge. Both guide additions explicitly exclude a final changed-law
endpoint and an out-of-sample risk guarantee. Reading them with the complete
guide does not turn prediction characterization into generalization, a depth
advantage or an efficient independent solver. The unchanged roadmap is explicitly
a plan; preserving it creates no new theorem claim.

Appending C.4.9 after C.4.8 is coherent with the assigned earlier coverage: it
extends the fitted-reference/response/nearby-law sequence to a finite nonzero
slow-time adaptation. Repeated model/state definitions within the new proof
units keep the interfaces readable. They do not replace established content,
introduce contradictory normalizations, or require a maintenance correction.
I found no duplication requiring a scientific rewrite.

All six relative links appearing on changed lines resolve to existing files
and, where present, existing heading fragments. This includes the three new
links to the unique C.4.9 heading. The proof contains 127 explicit equation tags,
all distinct within the new addition. Display delimiters are balanced and
properly ordered: 153 pairs in the addition; inline delimiters have 409 pairs.
The proposed guide has one display pair and 11 inline pairs. Local equation
and auxiliary-constant conventions are stated. The established targets
C.4.6.S40–S44 and C.4.7.N5/N7/N8/NE each exist once.

I specifically checked the “scalar-gradient argument in A.4” reference in new
C.1. The established chapter has an A.4 titled “Scalar gradient and strong-chain
rules”, and its complete body supplies the claimed scalar result. The new
unit-A subsection with a different descriptive title is not evidence of a missing
proof. No correction was required for that reference. This was a resolved check,
not an inherited objection.

The canonical text has no dependency on a study path, generated report, versioned
review, author conversation or internal verdict. The existing Gaussian-program
and chapter references are present in the standalone documentation. I checked
new/changed links, not the availability of all old external literature links or
all unmodified code-guide links in a documentation-only copy.

## Actual checks, evidence and completion

All commands ran from `/home/amir/Codes/PDE`. Scientific reads used the explicit
file paths and line ranges recorded above. Initial and final SHA-256 comparisons
used Python's hashlib over complete bytes. The independent deterministic check
is retained at:

`data/generated/nonlinear_prediction_selection/integration_v4/check_integration.py`

Reproduction command:

```text
python data/generated/nonlinear_prediction_selection/integration_v4/check_integration.py
```

The executed run exited 0 and passed 2,779 granular assertions, including all
patch-line, hunk, fingerprint, preservation, changed-link and delimiter assertions.
This count includes per-line mechanical checks; it is not a count of independent
scientific tests. The complete result and individual documentation hashes are in
`integration_v4/check_results.json`; the first recorded run started at
2026-09-12T10:44:50.733704+00:00. The environment was Python 3.10.12,
Linux 5.15.0-151-generic, x86_64, glibc 2.35. Supplemental target, instruction,
manifest and delimiter evidence is in `integration_v4/reference_checks.json`.
The final rerun and fingerprints are retained in `integration_v4/final_check.txt`.

There were no missing inputs, unresolved correctness or integration objections,
required corrections, proposed scientific edits, experiments or established-file
writes. Earlier truncated displays were repaired before this report. The complete
new scientific text, current/proposed guides, required old source scope and exact
assembly were covered as recorded above. The final conclusion remains **PASS
for this frozen v4 integration scope, with no required correction**. A different
scientific packet or changed dependency would require a new assessment of the
affected scope; this report does not grant promotion authority.
