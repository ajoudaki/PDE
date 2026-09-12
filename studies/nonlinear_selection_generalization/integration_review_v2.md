# Independent integration review of proposed C.4.10, edition v2

**Disposition: PASS for the assigned integration scope. No required correction.**

Reviewer: `/root/integration_review_v2`. Date: 2026-09-12.

The reviewed edition is
`data/generated/nonlinear_selection_generalization/edition_validation_v2_20260912_01/edition/`,
identified by integration manifest SHA-256
`b5fcdf928d4bcc964f626a176bd129c84662c9a66a900501b1143c7b2fb25b9a`.
This report evaluates the complete new assembled material and its specified
interfaces. It is not a fresh proof audit of the older book and does not replace
the separate paired scientific reviews or user approval required for promotion.

## Identity, isolation and authority

I began with the neutral `integration_assignment_v2.md`. I did not author or
assemble the candidate, select its placement, or conduct either named scientific
review. The identities in the assignment were treated only as exclusions. No
project research history, study README, old packet, internal check, prior report,
other reviewer's findings, other study, chat transcript or Git history was read.
There was no delegation. No scientific findings were requested from other agents.

I independently read the required `solve-math-rigorously` and
`investigate-conjectures` skills, plus the latter's complete
`references/adversarial-audit.md` and `references/research-contract.md`. The
contract and adversarial references were used to check target independence,
information available to the stop, distinct claim levels and limit order. No
experimental reference was needed: there was no training or empirical experiment.
No specialized external result was imported; the candidate supplies the elementary
measure-separation, compactness, comparison and sampling arguments it uses here.

Before substantive work, live `AGENTS.md`, `RESEARCH_WORKFLOW.md` and
`docs/NOTATION.md` were hashed and matched their frozen copies. Both parts of
the frozen workflow were read. Before scratch writes, read-only Git metadata
was recorded: HEAD `b384475316cc0e18bab14438f0140f8f2ede6c9a`, index SHA-256
`328563951b03e92245c4f164501f85677ef40a54be6581a73a3fd87b1a5e06d8`, and
status. These metadata observations were not scientific inputs. No Git write,
checkout, worktree, input edit or established-file edit occurred. Writes were
confined to this report and the assigned fresh scratch directory
`data/generated/nonlinear_selection_generalization/integration_review_v2/`.

## Actual read coverage

All line ranges below are inclusive. Byte comparisons and hashing are recorded
separately from reading proofs.

| Input | Actual reading |
|---|---|
| `integration_assignment_v2.md` | Complete, lines 1–69, first input read. |
| `scientific_manifest_v2.json` | Complete, lines 1–127. |
| `integration_manifest_v2.json` | Complete, lines 1–20. |
| `candidate_addition_v2.md` | Every line 1–1693, including all proof bodies, initially in ranges 1–300, 301–600, 601–900, 901–1200, 1201–1450 and 1451–1693. |
| Assembled `docs/global_nonlinear.md`, new section | Every line 15324–17016, directly reread from the actual edition in ranges 15324–15923, 15924–16523 and 16524–17016. These are exactly the candidate's 1693 lines. |
| Assembled `docs/global_nonlinear.md`, older interface | Complete C.4.9 model, theorem, scope and proof architecture at original/assembled lines 12994–13183. |
| `candidate_docs_README_v2.md` | Complete, lines 1–580: 1–210, 211–400 and 401–580, with repair described below. |
| `frozen_docs_README_v2.md` | Complete, lines 1–578: 1–300 and 301–578. |
| Assembled `docs/README.md` | Complete, lines 1–580, directly reread as 1–300 and 301–580. |
| `frozen_AGENTS_v2.md` | Complete, lines 1–47. |
| `frozen_WORKFLOW_v2.md` | Complete, lines 1–224, including both parts. |
| `frozen_NOTATION_v2.md` | Complete, lines 1–98. |
| `assemble_packet_v2.py` | Complete, lines 1–110. |
| `validate_edition_v2.py` | Complete, lines 1–108. |
| `frozen_global_nonlinear_v2.md` scientific interfaces | Exactly 10–30, 52–66, 786–820, 916–932, 2385–2470, 2850–2875 and 3649–3674, 226 assigned lines total. |
| Frozen dependency heading metadata | Relevant headings in `frozen_global_nonlinear_v2.md`; all heading lines in `frozen_special_data_limits_v2.md` locating III.F and III.F.1–III.F.11. No additional scientific bodies were fetched. |

Two aggregate tool outputs truncated portions of otherwise successful reads.
The candidate guide's affected 401–500 range was reread completely in a new
call. The affected scientific 1201–1450 range was reread completely in a
standalone call. Both repaired outputs were complete; both ranges were also
subsequently read in full from the actual edition. No scientific line of the
candidate or new assembled section remains unread.

The older complement of `docs/global_nonlinear.md` outside the assigned
C.4.9 range and specified frozen interface ranges was **not proof-audited**.
All proof bodies of `frozen_special_data_limits_v2.md` were **unread** in this
integration review. Heading and equation-label metadata searches do not change
that coverage. Full-file hashes, source-slice reconstruction and byte comparisons
were performed over these older files without treating their proofs as read.
No additional older scope proved essential to this integration assessment.

`scientific_assignment_v2.md` was hashed and checked for byte/line counts solely
as a manifest member; its contents were not read. The four author assembly-unit
hashes appearing in the scientific manifest were read as manifest data only;
the author-unit files themselves were neither read nor independently hashed.

## Frozen hashes and exact correspondence

The following SHA-256 values were checked against the manifests and rechecked
at completion. Names without a prefix below refer to the assigned study folder.

| File or identical copies | Checked SHA-256 |
|---|---|
| `integration_assignment_v2.md` | `1757fb1e056b2ed59acd73eba2f290be88aa7bd5dd882831e544ff2ab2efbeec` |
| `integration_manifest_v2.json` | `b5fcdf928d4bcc964f626a176bd129c84662c9a66a900501b1143c7b2fb25b9a` |
| `scientific_manifest_v2.json` | `cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7` |
| `candidate_addition_v2.md` | `b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d` |
| `frozen_global_nonlinear_v2.md` | `e8e4a8cfc485bf6330dfbbea871c830bbc5e44d3d571b526442d614a0520218c` |
| `frozen_special_data_limits_v2.md` | `65bda2d0ea6f3b202098466382e8e37cbb359658c8171dcd7a8e15da8724c6c1` |
| `frozen_AGENTS_v2.md`, live/edition `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `frozen_WORKFLOW_v2.md`, live/edition `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `frozen_NOTATION_v2.md`, live/edition `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `frozen_docs_README_v2.md`, live `docs/README.md` | `26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e` |
| `candidate_docs_README_v2.md`, edition `docs/README.md` | `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c` |
| `assemble_packet_v2.py` | `1b15be2ce2ff93c88af08fe961f38b103874378c2fe3e7e496e4f9ab6f35933d` |
| `validate_edition_v2.py` | `6a747c207416fb21bb3406a4e10709cbf546b947b67b4ad7d2ec47189e1d65cb` |
| `scientific_assignment_v2.md` (metadata only) | `6d6774ec35ceab6f1011a9dbf2832b2eca95cc156e96750a96b25b196a91f555` |
| Live original `docs/global_nonlinear.md` | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| Edition `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| Live/edition `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |

All eleven scientific-manifest members match their declared hashes, byte
counts and line counts. All six edition files match the integration manifest;
the edition contains precisely those six files. Both frozen dependency files
were independently reconstructed byte for byte from their declared slices of
the unchanged live sources.

The edition chapter equals the entire original chapter, followed by exactly
one newline separator and the entire candidate. All **679,806 old bytes and
15,322 old lines** are preserved. The candidate is **70,286 bytes and 1693
lines**, beginning at assembled line 15324. No old chapter content is replaced.

The guide equals its frozen original after removing exactly two copies of the
declared C.4.10 summary and the one declared roadmap paragraph. The resulting
changes are the roadmap insertion at candidate lines 302–303, the chapter-row
addition at line 450, and the scope-paragraph addition at line 570. No earlier
wording or link is removed or altered. The proposed established edits therefore
remain exactly the appended section and these three guide additions.

## Component checks and findings

### Model, clocks, state and old interfaces — PASS

NG1–NG3 agree with the complete assigned C.4.9 model: two bias-free tanh hidden
layers, physical input `x=sqrt(2)u`, actual stored Gaussian variances
`(1,1/n,1/n^2)`, readout division by `n`, mobilities `(n,1,n)`, and physical GF
of the unhalved mean-square loss. The raw Hilbert metric and finite comparison
metric retain the appropriate visible normalization factors. Only `K` is
Hilbert–Schmidt; the initialized Gaussian action and its true adjoint survive.

The reference endpoint is a mathematically specified consequence of the full
reference feature flow. It is not imposed as a finite-network reset. The old
swap symmetry is a deterministic population-law symmetry; the candidate uses
it in the population risk lower bound without assuming it for each finite
initialization. The endpoint bounds imported into NSC3, NSS3 and NGL1 agree
with the assigned R19 interface, with separate larger neighborhood constants.

The source-interface reading confirms the crucial distinction between
integrated control closeness to the **complete** reference history and a
standalone tail bound. The new section retains the radius and mesh threshold,
uses the assigned support-independent CT36 interface, and explicitly pays the
omitted reference suffix. It does not reset a reused source. The fixed-program
and scalar strong-derivative interfaces are used at their stated scope;
fixed-program width identification is not asserted for a transcript growing
with width. Strong completion, Borel-law extension and fixed-width comparison
have actual proof bodies in the new section.

The slow clock is `tau=epsilon t`. Capture excludes zero slow time and takes
width first for each fixed positive contamination and sample. The physical
stop is `T/epsilon`. The new statements do not inherit raw GD, the time-40
sampling theorem, a simultaneous rate, or an all-time changed-law endpoint.

### Target family and observation laws — PASS

NG4–NG6 prescribe the density and regression family independently of a trained
answer. The Fourier coefficients vary inside a weighted summability budget;
the density has full-circle support and bounds independent of width, sample
size and contamination. Oddness and anchor interpolation are explicit class
restrictions. `E_N` includes the fixed reference residual as an analysis
generator; it is not used to define the target coefficients.

The label-margin calculation checks out: writing `t=|cos(alpha)sin(alpha)|`
gives the displayed bound `|q_0|<=1-h/4`; target perturbation and bounded noise
each consume at most `h/8`. Conditional centering removes the noise from the
population force, but retains its separate sampling contribution.

The training sample consists of iid **added** observations, independent of
initialization. Its anchor masses are exactly `(1-epsilon)/2`. This is not an
iid sample of the whole mixture and does not hide a rare-component count.
Excess risk is measured under the independent test-input law `p rho` and
subtracts irreducible label variance. In contrast, hidden displacement uses
the fixed probability measure `(rho+delta_e1+delta_e2)/3`. NGL17 explicitly
states that its positive lower bound concerns this sum, not the circle-only
part. NGL22 is its correctly normalized, same-array finite counterpart.

Boundary cases are separated properly: `D=0` admits the uniform density;
`R=0` remains in the approximation class but is excluded from the positive
robust-margin assertion; `N=0` already has a nonzero target space; and zero
noise removes the noise summand and its failure allowance. Continuation and
finite-GF capture admit repeated or singular empirical configurations even
though the population generalization law has a full-support density.

### Conditioning, approximation, stopping information and margins — PASS

The continuum argument distinguishes injectivity from coercivity. Its
compact-operator discussion explicitly rules out a positive bound on the
entire odd function space. The positive constants `lambda_N` and
`lambda_(H,N)` come only from the declared finite-dimensional spaces and
compact density class. Deleting exact generator dependencies avoids assuming
that a redundant Gram matrix is invertible. No bound uniform in `N` or
numerically evaluated conditioning is claimed.

The approximation statement retains both the target tail and nonlinear state
motion in `A_N(T)`. Two elementary lower-norm inequalities in NGL7 account for
possible cancellation between mode images; they do not assume the images of
orthogonal residual components are orthogonal. Multiplication by the integrating
factor yields the stated forcing-to-decay ratio
`2(1+2 L_0^2/lambda_N)`. The text explicitly declines universal consistency
from decreasing the target tail alone.

Input and noise forcing are evaluated on the deterministic population path.
The proof does not assume empirical learned features are independent of their
own labels. The second-moment, time-integral and union-bound calculation leads
to NGL8 with separate failure allowances. The inverse modulus and its branch
condition are consistent; `d_*<=1/2` makes the threshold strictly admissible.

The strict theorem is for the finite-cap subfamily NGL14, not every infinite
Fourier target. Its coefficient budget is `9R/16<R`. Swap antisymmetry of the
reference and symmetry of the prescribed perturbation give the initial risk
margin; the exact circle norm of `h(cos+sin)` is `3/8`. The deterministic stop
in NGL16 depends only on the reference and class, including its finite-cap
conditioning, and is chosen before training. It uses no unknown density,
target coefficient realization, changed-law trajectory or observed test risk.
The contrast used to prove hidden motion may involve the target and density;
it is a proof observable, not information required by the stop or optimizer.

The hidden argument integrates a derivative bound over the positive episode
and controls an actual hidden-activation displacement. It does not substitute
parameter motion or an initial derivative for that displacement. NGL20–NGL23
retain spare risk and hidden margins through sampling, width and contamination
limits. More samples after those limits can raise the success probability;
there is no asserted uniform width threshold over the robust class.

No blocking scientific concern emerged from reading the entire added argument
and checking these interfaces. This statement does not certify unread older
dependency proofs or substitute for the separate complete scientific reviews.

### Guide summaries, placement and duplication — PASS

Appending C.4.10 after C.4.9 is coherent: the earlier assigned theorem treats
an open single-atom family and its added-component improvement; the new
section supplies bounded-law continuation, continuum target conditioning and
sampling-to-excess-risk conclusions. Repetition of the model and endpoint
notation at the new subsection boundaries makes the package locally readable
and does not create conflicting definitions.

Both guide summaries accurately name full-circle densities, independently
specified Fourier targets, bounded centered noise, finite-mode approximation,
separate sampling/noise bounds, a class-determined stop, robust risk improvement,
circle-plus-anchor hidden motion and ordered actual-GF limits. The roadmap
paragraph expressly retains the approximation floor and unevaluated constants.

The unchanged guide distinguishes C.4.5's fixed-time transfer, C.4.6's
separately fixed horizons and homogeneous propagation, C.4.7's nonlinear
continuation through time 40, C.4.8's time-40 sampling limit and width-first
bridge, and C.4.9's finite slow-time single-atom episode. The new summaries
do not remove those qualifications or turn them into C.4.10's theorem.

### Links, notation and independence from study artifacts — PASS

Both newly added Markdown links target the one actual heading
`C.4.10. Generalization during a finite added-data episode`, whose fragment is
`c410-generalization-during-a-finite-added-data-episode`. There are no new
Markdown links within the appended section and no deleted old guide links.
All 103 new equation tags are unique, disjoint from the older chapter's tags,
and every named new tag citation resolves. Display and inline math delimiters
are balanced. The older section names cited by the new text have matching
heading definitions in the supplied edition/dependencies.

Persistent model notation, residual sign, operator orientation and input
normalization agree with the full notation contract. Auxiliary constants and
fields are defined in their local subsections. The explicit pullback convention
resolves physical versus normalized-input notation in the force and sampling
formulas.

The mathematical addition contains no `studies/`, generated-data path, chat
dependency, historical verdict, local absolute path or retained array. Its
necessary established chapter and III.F dependency are included in the selected
edition. Its proofs require no new maintained API or experiment. The six-file
edition is a selected proof workspace: unchanged guide links to unrelated
chapters or the implementation guide are not all present there. No whole-site
link, exporter, PDF or unrelated-code validation is claimed or required by this
assignment.

## Commands, observations and limitations of deterministic checks

Working directory for all repository commands: `/home/amir/Codes/PDE`.

Actual read commands were `cat` for the assignment, manifests, full process,
notation and assembly/check code; `sed -n` for the exact reading intervals
listed above; and `rg -n` restricted to headings/new equation metadata. The
two truncated aggregate reads were repaired as recorded in the coverage table.
`sha256sum` initially checked the live/frozen shared instructions and integration
manifest. A read-only Python metadata check recorded all manifest/edition
hashes, original-byte preservation, initial Git metadata and scratch creation
in `initial_checks.json`.

I wrote and ran the independent deterministic checker with the actual command:

```text
python data/generated/nonlinear_selection_generalization/integration_review_v2/check_integration.py
```

It exited **0** with `PASS: deterministic integration assertions`. Its source
SHA-256 is `833e9a7f33098ca49522292a215fac5f5a82674bb5e61bd0c724fca0e6f5911a`.
The environment was Python 3.10.12, GCC 11.4.0,
`Linux-5.15.0-151-generic-x86_64-with-glibc2.35`. No extra numerical library was
used. The full result is retained in scratch `deterministic_checks.json`, and
the exact three-hunk guide difference in `guide_diff.txt`.

The checker independently verifies all declared file hashes/sizes/line counts,
six-file edition inventory, live shared-instruction equality, exact source-slice
correspondence, original chapter preservation, candidate/edition correspondence,
the three guide additions, new links, heading target, equation-tag uniqueness
and references, and absence of study/array paths. It also checks selected exact
scalar algebra, the robust coefficient budget and circle integral, and four
inverse-modulus round trips with positive-branch tests. The largest observed
round-trip relative error was `1.214306433183765e-15` (tolerance `2e-14`).
The finite rational grid used for the label inequality is a sanity check; the
uniform inequality is justified by the displayed algebra, not by that grid.

The provided assembly/check programs were read but not executed. The assembler
would create frozen study inputs, which is outside this review's write scope.
The provided validator also executes an older Gaussian certificate outside the
assigned proof-reading intervals. Repeating that certificate was unnecessary
for the present integration checks; no historical validation output was read
or adopted. The independent checker supplies the relevant deterministic
assembly checks without enlarging scientific reading scope. Neither checker
can certify the analytic continuation or learning proofs by passing assertions.

At completion, the independent checker was run again successfully. All frozen
inputs, the six edition files, live instruction/notation files and preserved
source bytes still matched. This report records the original review disposition;
no input was changed to make a check pass.

## Required corrections

None for this frozen edition under the assigned integration scope.

## Optional suggestions

1. The two compact guide summaries could say that strict positive margins hold
   “on a finite-cap subfamily.” The current phrase “robust unseen-risk
   improvement” is compatible with the actual theorem, whose subfamily is
   explicit, but the extra words would make the distinction from the general
   infinite-series approximation bound easier to see directly in the guide.
2. Qualify references to the scalar-gradient “A.4” as the chapter's Appendix
   A.4, and to the reference source argument as C.4.9 proof unit A.4. Their
   contexts and subject matter identify the intended locations already;
   qualification would reduce navigation ambiguity.

These are optional presentation suggestions, not unmet scientific obligations
or conditions attached to this PASS. The reviewed bytes remain the edition
identified above. Any adopted edit should be handled under the workflow's
review/correspondence rules rather than silently attributed to this report.

**Final disposition: PASS.** The complete new material is assembled faithfully,
the assigned old interfaces and summaries retain their scope, the intended
changes preserve existing material, and no mandatory integration correction
was found. Promotion authority and the separate scientific-review gates remain
outside this report's disposition.
