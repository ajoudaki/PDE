# Independent integration review of C.4.9, frozen edition v3

**Frozen-edition verdict: PASS for the assigned integration scope. Current-live
application: HOLD for the concurrent guide-preservation issue recorded below.**

This is a separate fresh integration review, not a whole-book proof audit,
an author check, or a substitute for the paired adversarial reviews. The frozen
addition and the actual assembled edition agree exactly. The new theorem,
its proof interfaces, its summaries, and its finite/population normalizations
are consistent with the selected established context. The old global chapter
is recoverable byte for byte after removing precisely the proposed additions.
The final fingerprint check subsequently found a new live guide insertion;
the frozen replacement guide must not overwrite it.

## Independence and assignment evidence

- Reviewer identity: `/root/integration_v3`.
- Neutral assignment: `INTEGRATION_ASSIGNMENT_v3.md`, 68 lines,
  SHA-256 `3d514d5b40f429213141426ce3880cb39256f846925b1443f385c957fafbba2b`.
- The review began from that assignment and the coordinator's neutral frozen-file
  instructions. No author discussion, previous candidate, correction record,
  prior verdict, paired review, selector finding, study README, proposal,
  source-coverage record, author report, Git history, other task, or other study
  was read. The identities listed in the assignment were used only to establish
  separation; this reviewer is not any listed author, selector, or earlier reviewer.
- Read root `AGENTS.md` and `RESEARCH_WORKFLOW.md`, including the independent
  review and promotion instructions. Read the required
  `solve-math-rigorously/SKILL.md` and `investigate-conjectures/SKILL.md`, and
  the latter's `research-contract.md` and `adversarial-audit.md` references.
  An initially truncated combined skill-tool response was repaired by a complete
  separate read of the mathematical skill. No uncorrected truncation remains
  in the scientific reads listed below.
- Findings were communicated only to the coordinator. No subreview findings
  were obtained. No Git command, established-file edit, training experiment,
  external-source retrieval, or author validation report was used.
- Writes are confined to this original report and
  `data/generated/nonlinear_prediction_selection/integration_v3/`.

## Exact read coverage and unread complement

Read every line of `CANONICAL_ADDITION_v3.md`, lines 1–2329, in consecutive
nontruncated ranges 1–380, 381–760, 761–1140, 1141–1520, 1521–1900,
1901–2329. This includes:

| Candidate lines | Complete new unit examined |
|---|---|
| 1–190 | Model, determining equation, theorem NS1–NS9, scope, proof architecture |
| 191–865 | Proof A: controlled source statement, control clock, named sources, reference anchor, temporary-cap moments, comparison and cap closure |
| 866–962 | Complete A-supplement: clipping, forcing, zero-forcing continuity, raw-to-clock defect and limit order |
| 963–1427 | Proof B: endpoint conditioning, gradient continuity, hidden contrast, finite episode and positive margins |
| 1428–2118 | Proof C: source interface, Osgood construction, reached derivatives, original-mixture continuation and singular selection |
| 2119–2304 | Proof D: actual finite GF, actual initial readout, one-reference comparison, normalization, whole-circle and paired observations |
| 2305–2329 | Completion, common time selection, iterated limits and probability margins |

Read the complete proposed guide (285 lines), edit specification (16 lines),
notation dependency (98 lines), review manifest (42 lines), and dependency
manifest (44 lines). The proposed guide retains its v1 filename as assigned.

The actual assembled `docs/global_nonlinear.md` was consumed in full for exact
byte comparisons, with scientific interpretation restricted to the assigned
old context and the complete new material. Its C.4.9 is lines **12994–15322**,
exactly the 2329 already-read candidate lines, with no transformation or omitted
body. Its new overview sentence is line **3851**. The actual assembled guide
is byte-identical to the completely read proposed guide; its exact changed
lines are **155 and 275**. Thus no new assembled scientific text lies outside
the complete textual reading. The unchanged complement was not treated as
having received a new scientific audit.

For the 2363-line patch, manually read its headers/overview/append opening
(1–85) and ending/guide hunks (2335–2363), and independently parsed **every
line** and applied **every hunk** in memory against the original files. Its
interior added body is exactly the complete candidate already read; the guide
changes are exactly the complete guide already read. This accounts for the
whole patch without mistaking a shortened diff display for full coverage.

Read original `docs/README.md` (284 lines) and `docs/NOTATION.md` (98 lines)
completely. Read these original `docs/global_nonlinear.md` ranges completely,
as assigned:

- 3836–3980: C.4 overview, local model, theorem, observations and limitations.
- 5269–5781: C.4.5 statement/scope plus complete reference model, feature
  evolution, clock, fitting, endpoint and prediction estimates through the
  selected endpoint-proof unit. This was split at 5530/5531 without a gap.
- 6903–7168: C.4.6 model, clock tangent, response equation, theorem,
  homogeneous propagation and finite-width observation scope.
- 8977–9169: C.4.7 model, nonlinear theorem and observation contract.
- 11440–11528: C.4.8 model and theorem, including its separately ordered
  sampling/width limit.

Enlarged actual reading, only within the permitted frozen dependency excerpts,
was as follows. Ranges here are lines in `DEPENDENCIES_GLOBAL_v1.md`:

- 1–120: header and original source lines 1840–1951. This includes the complete
  A.1–A.4 value, named-source, action-bound and scalar-gradient specializations,
  plus the beginning of B.1. In particular the reference to the contained
  scalar-gradient argument in A.4 resolves to the existing chapter A.4.
- 5590–5723, corresponding to original 8128–8261: the end of the preceding
  source estimate, the complete feature-segment population-envelope unit
  S40–S45, and the opening of the next forcing-continuity unit. This verifies
  the endpoint envelope and its simultaneous active-clock meaning used in B.
- 6790–6934, corresponding to original 9328–9472: source-cap statement context
  and the complete exact source equations/construction-order unit N2–N8.
  This verifies the transpose/source, diagonal-slot and frozen-coefficient
  interfaces used in A.
- 3680–3785, corresponding to original 6218–6323: reference source-chain,
  clipping, singular covariance and zero-forcing continuity details, followed
  by the beginning of the fresh-root estimate. No proof outside the actually
  displayed lines was represented as reread.
- One targeted `rg -n` query within that same allowed dependency file displayed
  heading/reference matches for A.4, III.F, C.4.5.2, S40–S44 and N5/N7/N8.
  Those isolated matches served reference location only; they were not imported
  as independently audited proofs of the unread surrounding material.

The rest of the old global chapter and all other old scientific chapters are
an **explicitly unread scientific complement**, apart from the source units
above. Their bytes were used for preservation/hashes and their headings for
link targets only. `DEPENDENCIES_GAUSSIAN_v1.md` was fingerprinted, not read as
an additional scientific proof. The original Gaussian-program proof and the
older rational reference certificate were not re-audited or rerun in this
integration review. They remain established dependencies, not new evidence
claimed by this report. No maintained API was used or changed.

## Fingerprints and correspondence

The independently computed complete fingerprint inventory is retained in
`data/generated/nonlinear_prediction_selection/integration_v3/input_hashes.json`.
Principal SHA-256 values are:

| Input | SHA-256 |
|---|---|
| `CANONICAL_ADDITION_v3.md` | `c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879` |
| `PROPOSED_GUIDE_v1.md` | `d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5` |
| `PROPOSED_EDITS_v3.json` | `46e1c92ed0d6c78940c8a7f60a966ca357e1883317ba8bb3cc977493da40e73f` |
| `PROPOSED_EDITION_v3.patch` | `ce121bad1089ca01e471c5c0a20fbfb8ef58f428258eba6b36ae9dd7e7b5b573` |
| `REVIEW_MANIFEST_v3.json` | `394c052a06f241d36dd9b502dff26b121796323787c2608a50e6b5f9bb61608e` |
| Original `docs/global_nonlinear.md` | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| Assembled `docs/global_nonlinear.md` | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| Original guide / frozen dependency guide | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| Original / frozen / assembled notation | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

All eight authorized review-manifest entries tested match both their recorded
hash and line count. All dependency-manifest content hashes and original
source fingerprints match. Entries naming the paired-review assignment and
certificate script were not opened merely because they occur in the manifest.

The independent assembly is exactly: replace the uniquely specified old
overview string once; append one separating newline and the frozen candidate;
replace the guide with the frozen proposed guide. The independently applied
four patch hunks produce the same two assembled files. Removing the append
and reversing the one overview replacement recovers all 12991 original global
lines byte for byte. The other eight documentation files, including notation,
are unchanged. The patch contains no code operations.

## Scientific interface and scope findings

**Model, loss, and normalization: pass.** The finite network retains two tanh
hidden layers, no bias, `u=x/sqrt(2)`, final division by width, independent stored
Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, and unhalved mean square.
These match C.4–C.4.8 and the notation contract. The raw finite metric has row
and readout squared norms divided by n, and the middle Frobenius squared norm
without that division. Its rank representative is `a b^T/n`, giving the product
of the two explicit RMS norms, exactly matching the population Hilbert–Schmidt
rank norm. No finite array is subtracted from an operator on another carrier.
Only K is Hilbert–Schmidt; A0 remains the bounded initialized action with its
actual adjoint. Typed aliases w, A, c have established precedents.

**Reference endpoint and conditioning: pass within the stated old-source
interface.** The feature equation and stop at the first b=1 state agree with
C.4.5.1, including the one-half coefficients and clock `ds/dt=2(1-b)`.
The raw endpoint error, norms, symmetry, and 76 input-Lipschitz bound used by
the new proof have the stated established values. B does not treat the old
C.4.6 possibly singular Gram discussion as an already supplied positive gap:
it supplies a new first-feature independence argument and a middle-rank Gram
lower bound. The protected-row argument uses a positive-probability intersection,
not independence of the envelope and the Gaussian roots. Sign changes separate
the finite nonantipodal directions. Positivity then passes over the specified
compact angle interval, and the nonzero readout follows from fitting. This
does not require injectivity of the trained action or an ambient gate margin.

**Source interface and local strong dynamics: pass.** CT13–CT16 match the
read source equations after replacing the specialized residual coefficients
with deterministic controls. The old/current source distinction and inactive
slot convention are retained. Joint source differences use cross-program Gram
covariances, not a claimed Lipschitz square-root map at rank loss. In A's
bootstrap, raw proximity uses only reference tails before the changed-program
cap is invoked. Current alpha precedes current beta, avoiding a current-row
assumption. The A-supplement explicitly orders fixed-graph width, zero forcing,
and mesh refinement. Control mass rather than elapsed physical time bounds the
source history; the reference tail is retained at every splice. This is the
needed additional interface beyond the old T=40 result.

The proof uses the bounded endpoint readout on the appropriate side of product
subtractions and obtains a one-reference Osgood modulus. It does not infer
local Lipschitz continuity of the ambient raw vector field or a Frechet
derivative for an L2-valued hidden map. C constructs a strong path from source
controlled Euler programs, then proves uniqueness against an arbitrary strong
competitor using tails only on the constructed path. Scalar/strong curve
chain rules and reached L4 products justify the derivatives actually used.

**Original fixed mixture and slow interval: pass.** The mixture is present
at physical initialization and never changes during a run. With anchor
residual vector r, its exact equations are
`theta'=-(1-epsilon)G r-2 epsilon v` and
`r'=-(1-epsilon)M r-2 epsilon G* v`.
Consequently `theta'=epsilon V+B r'`, with the factor two inside V and
`B=G M^-1`. This reproduces the tangent projection and the slow scale without
promoting the old first-order response to a nonlinear long-time expansion.
The post-prefix discrete contraction and control-mass estimates precede the
completion to actual mixture population GF. The endpoint-prefix comparison
takes epsilon to zero at fixed b and only subsequently b to infinity. The
unshifted statement excludes slow time zero, where the actual state is the
original initialization. A positive common existence time is constructed in
C and only decreased in B/completion; no vanishing epsilon-dependent activity
interval is used.

**Risk and actual hidden representation change: pass.** The new risk is
`R_nu` on the trained added atom, without multiplying it by epsilon. The
endpoint symmetry and angular bound give `5/16 <= y-f_dagger <= 11/16`.
The projected risk identity is `d(r^2)/d tau=-4 r^2 ||Pi g||^2`.
The local lower bounds give the stated positive gain
`25 kappa tau0/1024`. The fixed-readout hidden contrast has initial derivative
at least `5 kappa/8`; its continuity and the first-exit radius retain a positive
derivative through the finite interval. Its Cauchy–Schwarz bound is
`|Delta O|^2 <=30 T0^2 J2`. Thus the conclusion is a positive **second-hidden
activation** displacement, not merely moving hidden weights or readout.
Both reference and mixture use the same initial primitives, and finite J2
compares actual flows at the same physical time. There is no late first-hidden
margin claim and no implication that feature learning beats a frozen model.

**Finite-width bridge and retained initialization: pass.** D states the
population hypotheses actually established by C for each fixed positive
epsilon and its finite physical horizon. The actual initial Gaussian readout
is kept in the finite flow and finite proxy. A zero-limiting-readout oracle is
only a fixed-program comparison, handled by cutoffs and second-moment laws;
it does not reset a run. Hard and soft empirical tails have explicit RMS
normalization. The proxy comparison takes width at fixed mesh/cutoff, then
uses the Gaussian tail against the cutoff amplification and refines the mesh.
This supports width first at fixed epsilon; no simultaneous rate, arbitrary
growing-width horizon, raw-GD extension, or finite-n endpoint is asserted.
Finite same-array unions and bounded activation products support the paired
quantity. The endpoint enters only in the later epsilon limit.

**Guide, placement, and nonduplication: pass.** The C.4 overview and both guide
changes accurately describe a finite added-data episode, positive added-atom
risk gain, paired second-hidden adaptation, original fixed-mixture GF, and
width-first finite capture. The guide explicitly disclaims a final changed-law
endpoint and out-of-sample risk guarantee. Calling the family open means the
nonempty interior in the atom's location/label parameters; the theorem proves
the uniform result on its enclosing compact rectangle. It is not summarized
as a neighborhood of every probability law.

C.4.9 is naturally placed after the same-model nonlinear/response/statistical
sections. Its positive slow episode at order 1/epsilon is different from the
selected old fixed-T=40 nonlinear and fluctuation results, from the fitted
reference endpoint itself, and from an infinitesimal response. The repeated
model and raw-gradient setup supports a self-contained new theorem and proof
interfaces; I found no duplication that impairs correctness or maintenance.
No new proof relies on a study, conversation, historical verdict, or generated
training output. The main whole-circle prediction conclusion is a
characterization, not a generalization guarantee.

## Independent checks, commands, and outcomes

All commands ran from `/home/amir/Codes/PDE`. Scientific reads used explicit
`cat`/`sed -n` paths and the bounded `rg -n` dependency lookup specified above.
The complete executable independent checks are retained in the assigned
scratch, not in maintained code:

1. `python data/generated/nonlinear_prediction_selection/integration_v3/check_integration.py`
   exited **0**. Its original output is `integration_v3/checks.json`.
   It independently checks exact edit reconstruction, candidate/assembled
   correspondence, all 2363 patch lines and four hunks, old-global recovery,
   manifest/source hashes, eight unchanged documentation files, new fragments,
   absence of study dependencies in the addition, the complete guide's local
   links, and math delimiter/tag checks. The reported 153 display pairs and
   409 inline pairs are balanced. NS1–NS9 and CT1–CT45 are each defined once
   and their references resolve. There are 127 equation tags overall, with
   numeric namespaces local to the declared proof units.
2. `python data/generated/nonlinear_prediction_selection/integration_v3/check_algebra.py`
   exited **0**. Output: `integration_v3/algebra_checks.json`.
   Exact rational arithmetic checks the projected residual identity and
   anchor preservation on an independent full-rank finite Gram, the projected
   risk identity, residual interval endpoints, risk/prediction margin
   coefficients, the L2/L24 to L12 interpolation exponent 1/11, and the
   three-L12/one-L4 Holder exponents. These are algebra sanity checks, not a
   training experiment or empirical support for a population theorem.
3. A separate local label scan found no missing C-unit numeric labels. The
   apparent B-unit matches `(2)` and `(3)` were inspected and are `sqrt(2)`
   and `sqrt(3)` expressions, not equation references. A9 and A10 each have
   one definition. Reference resolution to the older chapter A.4 was checked
   against its complete scalar-gradient unit rather than declared broken
   from the local proof-letter collision.

All three new C.4.9 navigation links resolve to the unique new heading.
The complete guide link check records one **inherited packaging limitation**:
`../code/README.md` is absent from the documentation-only standalone bundle.
A metadata check confirms it exists in the live repository. That link is
unchanged, its text concerns older implementation material, and the new
theorem uses neither that guide nor code execution as a dependency. Therefore
this is not a required correction to the frozen new scientific integration.
It does mean this report does not claim that every inherited relative link
works when the docs-only bundle is distributed in isolation. External
bibliographic URLs and the unread whole-book references were not network-tested.

No author validator or recorded author verdict was run/read, and no whole-book
or empirical reproduction result is inferred from these deterministic checks.

## Final source-drift check and required preservation correction

After saving the body of this report, a final reread of all recorded input
fingerprints failed its unchanged-source assertion for **live `docs/README.md`
only**. The frozen candidate, proposed guide, patch, manifests, original global
chapter, and assembled edition remained unchanged. The failed assertion is an
actual final check result, not hidden by the earlier passing checks.

The original guide hash was
`5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f`.
The current live guide has 568 lines and SHA-256
`327c295c1c61e70ff58e5ffc8b6e51971a2d77fe8d12ac4ddbec33fb4941f00c`.
An explicit comparison against the allowed frozen dependency guide shows one
284-line insertion, current lines **148–431**, after original line 147. All
other original guide lines remain unchanged. I read the complete displayed
insertion to establish its role: it is the strategic roadmap, explicitly
identified as planning rather than additional established theorems. This is
the only additional final scientific-context reading beyond the scope inventory
above; it came directly from the allowed live guide, not a study or task history.
No finding from it was imported to justify the C.4.9 proof.

The exact final check results and difference ranges are retained in
`integration_v3/final_source_drift.json`. The coordinator was notified of the
drift and the precise preservation consequence.

**Required correction for applying to current live sources:** retain the entire
concurrent roadmap when preparing the proposed guide, refresh the corresponding
guide edit/patch/assembled edition and their baseline fingerprints, and obtain
the required fresh integration correspondence review of that revised scope.
`PROPOSED_EDITS_v3.json` currently specifies full replacement with the frozen
285-line guide. Executing that replacement now would delete the concurrent
insertion. This blocks current-live application even though it does not identify
a scientific flaw in the frozen addition. A source refresh must not be silently
represented as the exact frozen edition reviewed here.

No correction to the **frozen new scientific text** was found. No missing
scientific input prevented the assigned frozen-edition review. The independent
checks and interface/scope findings support the frozen-edition PASS, limited
to the exact original baseline fingerprints recorded above. They do not assert
that the changed live guide is identical to that reviewed baseline.

## Completion

This report is the reviewer's complete original report. PASS applies only to
the complete new integration against the precisely declared older read scope;
it neither certifies the unread complement afresh nor authorizes promotion.
The current-live guide-preservation HOLD must be resolved. Paired complete
scientific review and the workflow's user approval remain separate requirements
for changing established material.
