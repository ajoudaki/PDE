# Independent integration review of the frozen proposed edition v1

Reviewer: `/root/integration_v1`. Date: 2026-09-12.

**Verdict: integration requires one correction.** The assembled edition agrees
exactly with the frozen addition, proposed guide, edit specification and patch.
Placement, preservation, new links and the substantive scope summaries pass.
Proof unit D.2 does not consistently distinguish ordinary finite Euclidean
tails from normalized empirical L2 tails. The finite/population normalization
must be made explicit before this edition is accepted. This finding does not
claim that the theorem is false; it identifies a necessary correction at its
finite-width interface.

## Assignment, independence and retained evidence

The assignment was `INTEGRATION_ASSIGNMENT_v1.md`, SHA-256
`2fb8c9be8805388fef1a4b81fc55881bf8a213bb52eeab5d91d4679628242b4e`.
I received only the neutral integration assignment, allowed input paths,
candidate and assembled hashes, prohibited identities, and output ownership.
I am distinct from all named authors, assembler, selector and paired reviewers.
I did not read study history, the study README, routes/components, internal
checks, source-coverage records, selector findings, paired reviews, Git history,
or other tasks' scientific discussion. I did not communicate findings to any
reviewer or author other than the coordinator.

During the final checks the coordinator asked me to finish v1 unchanged and
said that a corrected packet would follow separately. That message supplied
no correction, argument, verdict or other review. I did not inspect any such
packet and did not use that scheduling information as scientific evidence.

I read current `AGENTS.md` and `RESEARCH_WORKFLOW.md`, including the independent
review and integration requirements. I applied both required skills,
`solve-math-rigorously` and `investigate-conjectures`, and read the latter's
research-contract, adversarial-audit and evidence-ledger references. There was
no training experiment, external scientific retrieval, Git operation, or edit
to established material. The coordinator remains the only Git writer.

My only writes are this report and
`data/generated/nonlinear_prediction_selection/integration_v1/`:

- `check_integration.py`: independent deterministic assembly checks.
- `checks.json`: complete hashes, environment, patch/hunk correspondence,
  preservation, delimiter and new-link results.
- `guide_diff.txt`: the exact original-to-proposed guide difference.
- `notation_scaling.json`: exact finite/population normalization examples and
  the mapping of the additional permitted source reads.
- `reference_targets.json`: existing equation-label and heading targets,
  checked as metadata rather than as additional scientific source bodies.

This is the complete original v1 report. Its negative finding and the original
packet must be retained even if a corrected edition is later reviewed.

## Complete new-material coverage

I read every scientific line of `CANONICAL_ADDITION_v1.md`, lines 1–2300,
in contiguous reads 1–500, 501–1000, 1001–1500, 1501–1900 and 1901–2300.
This covers the complete model/theorem, proof architecture, A.1–A.6,
A-supplement.4, B.2–B.5, C.1–C.7, D.1–D.2 and final assembly of the theorem.
No proof subsection, supplement or final finite observation assertion was
omitted.

The entire appended C.4.9 in the actual assembled chapter, lines
12994–15293, was reviewed through that completely read canonical text and
an independent byte-for-byte comparison of the entire appended sequence.
There are no differing or unread new lines hidden behind this correspondence:
all 91,656 appended bytes equal the fully read candidate. I also directly
read the actual assembled C.4 overview and D.2's finite-tail interface.
This is content-equivalent coverage, not a claim that I independently reread
the same proof twice.

I read the complete `PROPOSED_GUIDE_v1.md`, lines 1–285, and the complete
original `docs/README.md`, lines 1–284. One combined output truncated a part
of the proposed guide; I repaired it with a complete standalone read. I
directly read both changed guide passages in the actual assembled README
(the chapter table at line 155 and scope paragraph at line 275). The assembled
guide equals the complete proposed guide byte-for-byte.

I read all 16 lines of `PROPOSED_EDITS_v1.json`, all 42 lines of
`REVIEW_MANIFEST_v1.json`, all 44 lines of `DEPENDENCY_MANIFEST_v1.json`, and
the full 98-line notation contract. The frozen and original notation are
byte-identical. An initially truncated combined read was repaired by the
complete original-notation read and this exact comparison.

I covered the complete 2,334-line patch by reading its complete added text
through the canonical section and guide, reading all hunk headers and
surrounding context, and independently parsing and applying every patch line.
The parser verifies every context/removal line, both old and new hunk lengths,
and both resulting files against the actual assembled edition. No author
validation script or recorded validation verdict was used.

## Exact older scientific read scope and unread complement

The following original `docs/global_nonlinear.md` units were read completely:

| Original lines | Unit and purpose |
|---|---|
| 3836–3980 | C.4 overview, local model/theorem and its limits |
| 5269–5781 | C.4.5 statement, scope and complete selected reference endpoint proof |
| 6903–7168 | C.4.6 model, data-response equation and theorem |
| 8977–9169 | C.4.7 model/theorem and finite observation contract |
| 11440–11528 | C.4.8 model/theorem and width-first sampling statement |

Two additional interfaces were checked from the expressly permitted frozen
dependency excerpts:

| Frozen dependency lines | Exact original correspondence | Reason |
|---|---|---|
| 9–67 | 1840–1898 | Complete A.1–A.4 value, product, initial-action and scalar-gradient specializations; resolves the C.1 reference to the established A.4 |
| 5603–5719 | 8141–8257 | Complete C.4.6.3 subsection 6, including S40–S45; verifies the endpoint envelope and its actual countable-source meaning |

The dependency file's provenance/header lines 1–8 were also read. Exact
substring comparison established both original line mappings. I inspected
heading metadata across that frozen file to locate these interfaces.

The scientific unread complement is every other line of the original global
chapter, except for the three unchanged terminal lines exposed as patch
context, and the bodies of all other chapters. I read only the existing III.F
heading targets in `docs/special_data_limits.md`; I did not read or import that
chapter's proof bodies for a fresh proof audit. Frozen C.4.5.2 and C.4.7 source
sections were additionally scanned for equation labels only, not read as
scientific sources. Complete other documentation files were used only for
byte-preservation comparisons. No maintained code source was read or changed.

The full original guide and notation were read as required. Their descriptions
of other chapters were not used to extend this scientific proof scope. This
review therefore does not certify the entire older book, the complete older
Gaussian/cavity machinery, or the prior numerical certificate anew.

## Fingerprints and exact correspondence

| Artifact | SHA-256 |
|---|---|
| Canonical addition | `e53cefcd3aa58c456d8cee49bc7bff8c6330bffb1f05b9d8baa3646074189404` |
| Proposed guide / assembled guide | `d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5` |
| Proposed edits | `0493be3c29d2499826320e3324dea54a77ec865b494e0db0e169a438d3c9c006` |
| Proposed patch | `5dbd49d308eb2ecc131e061cb9138aa4d9928728626e483f15ecf27599660837` |
| Original global chapter | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| Assembled global chapter | `e1fe233b152d3803e993bdc1de1642d54d82ddba7afd4603992920dcf33dc1ae` |
| Original/frozen notation | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Original/frozen guide | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| Frozen global dependencies | `6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942` |
| Frozen Gaussian dependencies, fingerprint only | `c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77` |
| Review manifest | `357a7b3bc9e805749fb8c5f3383400edfce0bdc56277861ce74987b0d65d67e7` |
| Dependency manifest | `75f8b2ae6716fb88d8f89306b78a104a2bffc62e1bf67bb64474b8298d5b415a` |

All eight checked review-manifest entries match their recorded hash and line
count. The original global source hash matches the dependency manifest and
the neutral supplied assembled/candidate hashes match exactly.

The independent deterministic command was run from `/home/amir/Codes/PDE`:

```text
python data/generated/nonlinear_prediction_selection/integration_v1/check_integration.py
```

It exited 0 under Python 3.10.12, GCC 11.4.0, Linux 5.15.0-151-generic,
glibc 2.35. Its results are retained in full in `checks.json`:

- The old overview text has exactly one occurrence. Replacing that occurrence,
  adding one separating newline and appending the canonical addition reproduces
  the assembled global chapter exactly.
- The patch's global hunks are old 3848/6 → new 3848/7 and old 12989/3 →
  new 12990/2304. Its guide hunks are old 152/7 → new 152/7 and
  old 272/6 → new 272/7. Strict replay reproduces both assembled files.
- The documentation file inventory is identical. Only `README.md` and
  `global_nonlinear.md` differ. `NOTATION.md`, `arctan_limits.md`,
  `continuous_depth.md`, `finite_dynamics.md`,
  `finite_optimization_and_controls.md`, `gaussian_calculus.md`,
  `linear_dynamics.md`, and `special_data_limits.md` are byte-preserved.
- All three new C.4.9 links resolve to the single matching heading. The new
  canonical text contains no study path, generated-data path, internal review
  reference or author-check dependency.
- The candidate has 153 balanced display-delimiter pairs, 409 balanced inline
  delimiter pairs and 127 distinct equation tags. The guide has one balanced
  display pair. This is a delimiter/target check, not a claim of rendered-browser
  testing or validation of every older link.

Other actual checks used `cat`/`sed` for the complete ranges listed above,
`rg -n` for candidate references, patch hunk metadata and permitted source
headings, and direct Python exact-substring/normalization calculations.
The original normalization examples and source mappings are retained in
`notation_scaling.json`; their complete arithmetic is specified below.

## Interface, scope, placement and duplication findings

**Model interface passes.** Two bias-free tanh hidden layers, equal width,
stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, unhalved mean-square
loss and physical GF agree with the selected C.4 material. The residual has
the established sign. Physical inputs and normalized directions are related
by `x=sqrt(2)u`. The learned middle increment is Hilbert–Schmidt while the
initialized action is only bounded, and the same action's true adjoint is
retained. The finite initial readout is retained throughout.

**Reference interface passes.** The feature equation and first `b=1` stopping
rule reproduce C.4.5's reference prescription, with `s_dagger<=10` and the
actual raw endpoint. The constants used from that reference agree with R18–R23.
The selected C.4.6 source subsection supports the envelope, active-clock
bound and fixed-input L4 bound used in B.2; no independence of that envelope
and first roots is claimed. The new raw anchor Gram is distinct from C.4.6's
clock-tangent Gram, so proving positivity here does not contradict C.4.6's
earlier allowance for a singular endpoint Gram.

**Claim boundaries pass.** NS1 is a fixed compact location/label rectangle
with nonempty interior and inputs nonorthogonal to both reference directions.
The guide's open-family wording is supported by this interior; it does not
claim an open neighborhood in the space of all laws. NS3 recomputes features
and the projection from the current full state. It preserves exactly the two
reference predictions. No changed-law endpoint, general arbitrary-law
long-time theorem or frozen-kernel closure is asserted.

The fixed positive interval is `[0,tau0]` in slow time, with a and j independent
of epsilon. The actual law is `(1-epsilon)nu_*+epsilon nu` from physical time
zero. C.6 constructs that original flow; C.7 derives the slow scale from
`theta'=epsilon V+B r'`, bounds the integrated normal remainder and removes
the fixed physical prefix in the stated order. NS5 excludes zero slow time;
the population endpoint is not silently substituted as an actual training
initialization. Width is first for each separately fixed positive epsilon,
and the growing physical horizon is finite at that stage. No simultaneous
epsilon/width bound or raw-GD extension appears.

**Risk and feature observables pass in scope.** NS6 compares the risk of the
reference endpoint with the selected episode on the added trained atom, with
no epsilon weighting. The exact derivatives in B.5 are
`f'=-2r||Pi g||^2` and `(r^2)'=-4r^2||Pi g||^2`; the lower residual and projected
gradient bounds give the displayed finite margin. This is not risk on passive
circle inputs or an out-of-sample distribution.

NS7 concerns second-hidden activation displacement, verified by a fixed-readout
hidden contrast. NS9 uses actual mixture and reference networks with the same
initial arrays at the same physical time. The reference endpoint is taken
only after the width limit and then epsilon→0. These are paired second-layer
observations, not differences between freely coupled marginal laws. There is
no new first-hidden margin. The whole-circle prediction statement is a
characterization and convergence claim; both guide additions expressly exclude
an out-of-sample risk guarantee.

**Placement and preservation pass.** C.4.9 extends the same fitted-reference
sequence after the response, finite-horizon changed-law and sampling sections.
Appending it and adding its two guide summaries is a coherent, limited
integration. The different roles and fixed horizons of C.4.1–C.4.8 remain
unchanged. Repeated model/state definitions in the proof units serve their
local norm and source contracts; their duplication does not require a rewrite.
No experimental recipe or maintained-code addition is needed for this
proof-only proposal.

**Reference checks pass.** The potentially ambiguous A.4 citation in C.1 has
an actual target: established global-nonlinear A.4, whose complete scalar
gradient proof was read. It is not a missing claim in local proof unit A.4.
Existing targets C.4.5.2.R5–R7, C.4.7.N5/N7/N8 and III.F are present.
The short full-state initialization notation `(g,A0,0)` is immediately
disambiguated by the explicit raw `(w,K,c)=(g,0,0)` prescription; no correction
is required for the scientific meaning. Generic local constants and labels
are explicitly scoped, and completion qualifies its B.5 references.

## Required correction N1: finite tail and hidden norm normalization

Location: canonical lines 2150–2252, chiefly 2202–2244; assembled chapter
lines 15143–15245, chiefly 15195–15237. This is proof unit D.2.

D.1 defines the population tail as `tau_R(v)=||v 1_{|v|>R}||_2`.
D.2 then explicitly makes all finite vector norms ordinary Euclidean and
uses a finite metric with factors `1/sqrt(n)` on row/readout differences.
Nevertheless the finite proxy's soft tails, hard tails, and final comparison
display are written with the same unnormalized `||.||_2` / `tau_R` notation.
The text then says these finite tails converge to the population L2 tails
at fixed cutoff. That statement needs the empirical RMS normalization.

This is not a discretionary stylistic request. With a deterministic finite
vector `q_i=2` and cutoff R=1, the ordinary Euclidean tail is `2sqrt(n)`,
whereas its empirical L2 tail and the population L2 tail of the constant
variable 2 are both 2. The executed arithmetic for n=1,4,100 gives ordinary
tails 2,4,20 and normalized/population tails 2,2,2. Thus the claimed tail
passage does not hold under D.2's literal stated finite norm convention.
Taking width first at fixed R cannot remove the missing factor.

The same interface is visible in the rank identity used in the finite
comparison: the population identity
`||a tensor b||_HS=||a||_2||b||_2` corresponds at finite width to
`||ab^T/n||_F=||a||_2||b||_2/n`. For a=b=ones(n), the finite left side is 1
and the unnormalized vector-norm product is n. The final hidden-field bound
also needs `||h2-h2bar||_2/sqrt(n)` when applied to finite states.

The required repair is narrow:

1. Define the finite empirical tail explicitly, for example
   `tau_(R,n)(q)=||q 1_{|q|>R}||_2/sqrt(n)`, separately from the population tail.
2. Put that finite tail into the proxy-tail convergence and the `d_n`
   comparison. For the Euclidean product inequality either divide all terms
   by `sqrt(n)`, or write its tail term as `sqrt(n) tau_(R,n)(qbar)`.
   Normalize finite soft tails in the interpolation paragraph as well.
3. State the finite rank and finite hidden-field counterparts with their
   displayed factors; retain the existing population identities unchanged.

These changes make the finite argument obey the shared notation contract and
make its fixed-program second-moment passage literally correct. I found no
separate need to alter the theorem's constants, iterated limits, risks or
paired-observation definitions. I am not certifying a future correction in
advance; its actual assembled wording must receive the required fresh review.

## Completion and limits of this verdict

The complete assigned v1 integration scope has been checked, with the exact
older read boundary and enlarged interface reads above. No required input is
missing. Exact assembly, preservation, new links, placement, summary scope and
the selected established interfaces pass. N1 remains an unresolved required
normalization correction, so the frozen v1 edition does **not** receive an
unqualified integration PASS.

This review supplies neither another paired adversarial verdict nor user
promotion approval. It does not audit the unread older scientific complement,
reproduce any training experiment, or claim browser-rendered validation. All
original findings and deterministic evidence remain attached to the hashes
above. No established material was modified.
