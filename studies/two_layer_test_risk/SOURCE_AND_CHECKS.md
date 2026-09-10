# Source and internal-check evidence

This records research evidence, not promotion approval. Main coordinator is
the only Git writer. Initial HEAD was
`02af27154186dd3e45f83989a8ddf78e92ebceff`; the shared index was initially empty.
Unrelated dirty exporter/maintenance paths were not adopted.

## Main coordinator's complete relevant reading

- Root `AGENTS.md` and both parts of `RESEARCH_WORKFLOW.md`.
- `docs/README.md`, `docs/NOTATION.md`, `code/README.md`, and
  `studies/repository_refactor_2026_09_09/CONTINUATION_DISPOSITION.md` in full.
- `docs/global_nonlinear.md`: sections 2 and 3 (lines 181--500),
  A.1--A.4 (1835--1893), and the complete C introduction/C.1--C.3
  (2449--3829), including the weighted-loss correction at the end.
  This includes the operative strong-solution construction, response/tail
  proof, finite-program Gaussian conditioning, singular covariance handling,
  every-mesh comparison, activity proof and normalization correction.
- `docs/finite_dynamics.md`: introduction and complete sections 1--4
  (1--227), the exact all-block gradients, kernels, energy and norm bounds.
  Subsequent quadratic/RMS/ReLU model variants are not used.
- `docs/gaussian_calculus.md`: introduction and sections 1--4 (1--262),
  complete moving-flow jet section 7.1 (1824--2155), and complete finite
  depth/batch jet section E (5338--5473). No all-order Taylor convergence or
  order-one-readout theorem is imported. The general nonlinear Gaussian
  response dependency is read in global_nonlinear section 3/A.1--A.2 above.
- `code/pde/finite_jets.py` lines 1--304, including the full called
  `finite_flow_jets` producer, and its finite-network argument, scaling,
  callback and parameter dependencies (finite_network lines 1--340).
  The test uses supplied deterministic states, not initialization or GD APIs.
- Both required SKILL.md files, and investigate-conjectures references
  research-contract, evidence-ledger, adversarial-audit,
  proof-search-orchestration and decisive-experiments in full.

Truncated aggregate source reads were repaired by smaller subsequent reads.
Historical disposition/verdicts were used for scope and source routing only;
the source proof bodies supply the arguments. No external theorem or web
source is required beyond the contained arguments in these dependencies.

## Source SHA-256 at reading

```text
a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517  AGENTS.md
4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442  RESEARCH_WORKFLOW.md
4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453  docs/README.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101  docs/global_nonlinear.md
a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a  docs/finite_dynamics.md
d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e  docs/gaussian_calculus.md
00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774  code/README.md
0dfdfcca323de9f8147529cfd18fa15cc5ff2899143f0af728c625531dea4f48  studies/repository_refactor_2026_09_09/CONTINUATION_DISPOSITION.md
a8e22e14c7ce387636a7981a5e80556b975f83f8cf6a2b85ab22af877f5cca4c  code/pde/finite_jets.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
```

## Finite deterministic identity check

Executed from `/home/amir/Codes/PDE`:

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/two_layer_test_risk/check_finite_identity.py --output data/generated/two_layer_test_risk/finite_identity_20260910_01
```

Python 3.10.12, NumPy 1.26.4, float64 CPU arithmetic, one linear-algebra
thread. No seed or random draw; the full width-five matrix state is fixed
in the source. No optimizer steps or training trajectory were computed.
The zero-readout algebra check is deliberately a derivative identity check,
not a replacement for the canonical finite random initialization.

The independent closed-form cubic identity agrees with the maintained
moving-residual producer. It also agrees at two passive inputs evaluated
from the parameter jets and with the separately expanded kernel. All ten
absolute discrepancies are below `9e-19`; the declared tolerance was
`1e-11` (stricter than the preregistered `1e-9` validity gate). Exit status 0.
The training contraction is positive, the matched cubic loss term cancels,
and a separate nonzero finite readout gives positive initialized hidden
kernel trace `0.0038079887665557707`, confirming that finite initial tangent
kernel and finite frozen-readout kernel must not be identified.

The tested finite-state clock coefficient `0.13940654541708933` is not the
population coefficient; it carries no Gaussian/test-risk claim. Source hash:
`fbf00ca6267536e9126b2dde3cfa416e352643044b45b155c233bf7a8bff7edf`.
Complete machine output: `data/generated/two_layer_test_risk/finite_identity_20260910_01/result.json`.
Fresh reproduction must use a new output directory; existing runs are rejected.

Population integral checks and their limitations are recorded separately in
`QUADRATURE.md`, with their complete producer and fresh-run outputs.

## Initial-phase frozen promotion checks and closeout (historical)

The exact proof-only proposal is described in `PROMOTION_PROPOSAL.md`.
The independent selector accepted its narrow scope, separately from the
internal adversarial check. Two fresh complete scientific reviewers and a
separate fresh integration reviewer then read their frozen neutral packets,
without author history or other verdicts. The coordinator read their original
full reports completely (repairing one truncated aggregate display of A by
reading its complete final portion) and independently verified these hashes:

```text
a8616e0d06dd5bb56c3a9352b487abc159d1e9547f12c31f3ce5fcb08a2cddce  PROMOTION_REVIEW_A_V1.md
f7708394f6bc9d06de5dacff2b562db1740faf8667b4f12fcff9424f121ee13d  PROMOTION_REVIEW_B_V1.md
a80224517eff46e8348da8164a2bf4be170d939d6183e2932380181a4d851c85  PROMOTION_INTEGRATION_V1.md
b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4  PROMOTION_C4.md
b8fbd4ae8b07f23ac717d79eea6c82f180f7d2c23e36ebe48b970d907e0ad6ea  assemble_promotion.py
028cba4a0ff9c166c484dadbb290391fe1c25f6b5c7204a1c6e3d33616273727  check_promotion_integration.py
```

The scientific verdicts are ACCEPT; integration is PASS, with no required
corrections. Original reports remain unchanged. The integration check source
was copied byte-for-byte from reviewer scratch into the study for durable
retention; its original execution and outputs remain in the frozen run.
The proposal documents its required generated execution location. No unique
proof or verification source is left only in generated data.

Assembly was executed once with exit 0:

```sh
python -B studies/two_layer_test_risk/assemble_promotion.py --output data/generated/two_layer_test_risk/promotion_v1
```

The frozen manifest is
`data/generated/two_layer_test_risk/promotion_v1/manifest.json`, SHA-256
`14316c7a0162fdc81788efabdce1f08b2a7d219adbd8fd8960f295274d5345b7`.
Assembly validation is `promotion_v1/validation.json`, SHA-256
`fa418e16e1586924084004314edc462573637544a18ba8a513c2bd5eac6bc420`.
The separate review executed
`python -B data/generated/two_layer_test_risk/promotion_v1/integration_scratch/check_integration.py`
with exit 0; its `check_results.json` and `guide.diff` are in that same scratch
directory. Both assembly and independent review ran the standalone
`python -B code/tools/check_library.py` from the proposed edition, passing all
12 included files. Full commands and outcomes are in the original integration
report. The coordinator also checked manifest integrity, exact old chapter
prefix preservation, one-sentence guide scope, balanced displayed math and
absence of study dependencies. No training or additional quadrature was run.

These are proof-only edition checks, not a recertification of unchanged
implementation APIs or a whole-book scientific review. The integration
report names its complete new/dependency coverage and unread older complement.
The risk coefficient's sign/nonvanishing remain open after all reviews.
Root instructions were reread and their unchanged hashes confirmed at closeout.
Established book/code edits still require user approval of the exact package.

Final structural checks passed for all 20 owned study files: Python syntax,
relative local links, frozen candidate/assembler hashes, all 12 unchanged
maintained edition sources, and an empty shared index before the transaction.
The eight inherited dirty review files under
`studies/repository_refactor_2026_09_09/reviews/` are unreadable to this task:
`ANALYZER_PATH_PLAN_ACCEPTANCE_REPORT.md`,
`ANALYZER_PATH_PLAN_ACCEPTANCE_acceptance.py`,
`ANALYZER_PATH_PLAN_ACCEPTANCE_evidence.json`, `EXACT_CAPTURE_ROUND2_B.md`,
`GUIDE_ADVISORY_INTEGRATION.md`, `INCORPORATION_FINAL_INTEGRATION.md`,
`MAIN_ROUTING_PATCH_ROUND1_record-python`, and
`MAIN_ROUTING_WRAPPER_ACCEPTANCE_record-python`. They were inspected only
through Git status and file metadata and were not modified. Other unrelated
dirty files were fingerprinted for preservation; none enters this commit.

## Signed continuation: complete scientific check

The user reopened the exact scalar-sign obligation. Both required skills and
all applicable references were read again, and current root instructions and
operative proof/source versions were verified unchanged. The existing
strong-flow coefficient/remainder proofs were adopted, not restarted. The
continuation used analytic structure (approach A) and certified deterministic
integration (approach B), with no third route, training or witness search.
The full component proofs/checks are linked from the current README.

Before coefficient execution the README froze B=26, the 256-angle rule reduced
to 64 values, dyadic Gaussian grids with radius at least eight, every error
axis and a two-run/30-CPU-minute budget. The second run was reserved for one
fresh reproduction if the first interval excluded zero. Both runs succeeded:

```sh
python -B studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_20260910_01
python -B studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_reproduction_20260910_01
```

The second command was executed by fresh isolated reviewer A (its recorded
command omits `-B` but disables bytecode through the environment). No other
full coefficient run was made. Production used 31.17975 CPU seconds and the
fresh reproduction 30.66773, well below the 900-second per-run bound.
Python 3.10.12, NumPy 1.26.4, GCC 11.4.0, Linux x86_64, binary64 nearest
rounding and 64-bit long-double significand were recorded. The exact build
flags exclude fast-math and fused contraction. Metadata records platform,
source/Git hashes, all limits, commands, runtime, exit status and precision.
No random draw or training trajectory is used.

The two `result.json` files have identical SHA-256
`89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`.
Root independently checked identity of all 322 invariant files: 128 primitive
inputs, 128 bit-exact primitive outputs, 64 nodal enclosures, constants and
result. Timing/provenance metadata are intentionally different. Both exact
chi/beta intervals lie strictly inside SIGN_THEOREM (S2), as checked by
integer/Fraction comparison. The finite-time implication then uses the
already controlled remainder, not a numerical trajectory approximation.

The fresh full scientific packet was assembled by
`python -B studies/two_layer_test_risk/assemble_sign_review.py --output data/generated/two_layer_test_risk/sign_review_v1`.
Its manifest SHA-256 is
`133358ebec642bfec1af8b46a2d239e7ef93877a36825c21d08260a58b350bbc`.
Both isolated reviewers read all 6,031 packet lines, including complete
operative population proof/corrections, and audited all approximation and
arithmetic axes. Their original full reports are SIGN_REVIEW_A_V1 (ACCEPT)
and SIGN_REVIEW_B_V1 (PASS), with no required corrections. Both independently
reconstructed the 64 scalar enclosures through separate rational interval
implementations of the full four-slot response formula. Reviewer A also
executed the reserved fresh coefficient reproduction. Root read both
original reports completely, repaired one small truncation in A with a
separate contiguous read, verified their hashes, and checked all 625 frozen
source/book/packet/evidence hashes. This is a complete study-result check;
any new canonical edition has its own separate promotion gates.

The independent checker sources have been copied byte-for-byte out of reviewer
scratch into `check_sign_review_a.py`, `check_sign_review_b.py`, and
`check_sign_review_b_scalars.py` for durable source retention. Their original
executed paths, exact commands and hashes are in the full reports. They are
review-evidence programs with frozen paths, not maintained general APIs.
To repeat them, reproduce the packet at the required original layout and
execute a copied checker in a fresh scratch tree after updating only its
explicit input/output path constants; never overwrite the retained original
review evidence. Such a new execution needs a new provenance record.
The two reviewer-harness mistakes (scalar metadata treated as a list, and
invalid interval-nesting expectation under distributive regrouping) are
preserved in the reports and raw logs. Neither required changing the
scientific producer or running another Gaussian calculation.

The old uncertified Gauss--Hermite convergence failure remains an adverse
historical diagnostic; only the new enclosure proves a sign. Analytic
structure alone also failed to settle that sign, as SIGN_STRUCTURE records.
The preflight small-Taylor-coefficient interval-efficiency defect was corrected
before the first new coefficient run; original evidence and the exact scalar
ordering fix are retained in DRIVER_REVIEW. All component internal checks
passed at the frozen production versions.

Final scientific proof/source and review hashes:

```text
18979c2a785b63752e0f3019f0266699f8852055512d566fba1a1c412bbb8a28  SIGN_THEOREM.md
00fb949d4401797676fcaa31d09cb067532bf3359e7d0731071a2cb18d9bc599  SIGN_STRUCTURE.md
bcf7fa482d948b73c7ba82b60f514776dbd6d3609a3fb429744aaf507a76c9ad  CERTIFIED_ERROR.md
52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16  CERTIFICATION_ENGINE.md
a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2  ANGULAR_CERTIFICATE.md
871a474c95a36790604c882949ad1cd5870d0965fe11d16c3380fa134793f3de  DRIVER_CERTIFICATION.md
a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1  certificate_driver.py
9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9  certificate_kernel.cpp
cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149  angle_error_bound.py
3313df40cbf8170c423d4951bf06aff9733c3260c6d76e01cb3f3d8cee6de989  check_certificate_driver.py
cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1  check_certificate_kernel.py
15a595a83264033ca10ea7d5978bc995f49f230bb08163c24ec5a22901d854c9  ANGULAR_REVIEW.md
1a2aa8cef758733e43073690fd252829452638c0e2f842009d78b8329de80e44  KERNEL_REVIEW.md
d07509a0ea86e0cf745aa96bd21abf4e1546ca4f0ccbe99b2b2fda1e9d99249b  DRIVER_REVIEW.md
5f62ac040df9e426011ce2e21a650c67fe7c8586577aeedc8fa3b9eb7838b178  SIGN_REVIEW_A_V1.md
48c340dd861f26d04cd807e5a6da607e3e60b41d833946fefb88b566035cb959  SIGN_REVIEW_B_V1.md
54f38d9a46381eb6808605a435691103d6c5339b176aa29136fa552d55f2aadc  SIGN_RELEVANCE.md
3676752b44e46bee29408ce800290e76348cf640b34fd725878d4d4e3ce62601  check_sign_review_a.py
0d63f4de6cbb4e6d049409b4217b079a03e89b82826c67ee55d2117e56a30d3c  check_sign_review_b.py
7ac50eff1ccbdb017c1e00a33ea6666b69fef9dd018f0b122ee495ba8041beb6  check_sign_review_b_scalars.py
```

## Signed canonical edition and final promotion gates

The independent selector's SIGN_RELEVANCE accepted narrow assembly. The
complete canonical proof is PROMOTION_SIGN_C4_V2, the optional six-file tool
is mapped in SIGNED_PROMOTION_PROPOSAL, and both guides are supplied in full
in the frozen edition. The original unsigned proposal and all original
reports remain unchanged and cover only their earlier scopes.

Internal canonical checking and its corrections are retained in
SIGN_CANONICAL_CHECK, SIGN_NOTATION_ASSEMBLY and
SIGN_NOTATION_CORRESPONDENCE. The last report was copied byte for byte from
`signed_notation_20260910_01/correspondence_audit.md`; it is internal author
assistance, not an isolated promotion verdict. The final inverse edit map
preserves all 80 displays under explicit notation changes, all 60 tags,
all signed bounds and numerical budgets. Early replacement defects in
preflight notation are retained in the report; none entered the frozen
reviewed V2. The coordinator read all final content, complete changes and
the canonicalizer, repairing a clipped small display with a focused read.
PROMOTION_CODE_ASSEMBLY records complete numerical source correspondence
and standalone checks of the candidate wrapper. These internal records did
not substitute for the subsequent fresh gates.

Assembly command, exit zero:

```sh
python -B studies/two_layer_test_risk/assemble_signed_promotion.py --output data/generated/two_layer_test_risk/signed_promotion_v1
```

Manifest SHA256:
`bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3`.
It freezes 16 packet files, 18 edition files and 1,160 raw-evidence files.
The standalone structural check passed all 17 included Markdown/Python
files. The full existing chapter's 183,317 bytes/3,829 lines are preserved;
the new C.4 is appended after one separator. Nine destinations change or
are added. No live established destination was edited.

Two fresh isolated reviewers distinct from all authors/assemblers and the
selector received only the neutral assignment and complete frozen sources.
Original full scientific reports SIGNED_PROMOTION_REVIEW_A_V1 (468 lines)
and SIGNED_PROMOTION_REVIEW_B_V1 (932 lines) accepted the exact edition with
no required correction. Each read every candidate/dependency/scientific-code
line and complete guides, audited the source correspondence to the executed
producer, rebuilt its identical binary, checked both complete raw runs and
independently reassembled the full four-slot response using its own outward
interval arithmetic (110 and 112 bits). No new Gaussian coefficient rule
was evaluated. The original two full executions exhaust the preregistered
budget; target 30 has no full-run result.

The separate fresh independent SIGNED_PROMOTION_INTEGRATION_V1 (426 lines)
accepted exact preservation, notation, interfaces, placement, guides and
standalone behavior. Its full read scope and older unread complement are
explicit. It performed two exact saved-bit replays and actual wrapper-failure
checks; it did not claim a third successful coefficient execution or a
whole-book/library audit. check_signed_integration.py is retained flat as
its complete unique source. Scientific review sources are embedded in full
in their original reports and match their executed scratch files.

The coordinator read all three original reports completely, including all
embedded checker source; repaired the initial truncated A display by complete
consecutive reads; and read the full integration checker. Frozen manifest,
all 1,194 payload files, candidate mappings and all current source/dependency
hashes were independently verified. This also verifies the nonoperative
builder/assembler hashes which were not available inside the integration
reviewer's isolated inputs. The integration verdict does not rely on those
hashes. Two historical source-comment filenames remain explicitly nonblocking
and unchanged at the accepted hashes.

Review evidence preserves adverse checks: A's original AST comparison included
a moved metadata query and was narrowed to scientific operations; a huge
Fraction diagnostic display was simplified without changing deciding exact
inequalities. B's combined two-run replay hit its 60-CPU-second cap; separate
unchanged per-run mathematical checks passed in 44.235 and 44.860 CPU seconds.
Integration's initial scalar-bit metadata indexing error was corrected only
in its checker, then both full replays passed in about 24 CPU seconds each.
None changed the frozen scientific source or counts as a new coefficient run.
Mock successes and intentionally failed workers are only interface tests.

The full source-to-destination mapping, supported runtime/precision limits,
unevaluated time window, reproduction scope and all approval boundaries are
in SIGNED_PROMOTION_PROPOSAL and the tool guide. The mathematical conclusion
is complete; promotion awaits approval of the exact reviewed addition.

Final promotion report hashes:

```text
c7ba5ec25282590789f43ca6b7751fa602c95ab2cbbedea3bd6f0578a3395ec5  SIGNED_PROMOTION_REVIEW_A_V1.md
326b84743805a2b37cdef861588c3b8179138b2858a2e220d4c5230bb4e82962  SIGNED_PROMOTION_REVIEW_B_V1.md
9005a15bba85f0dbee96222ef3ae8651cbe3197a6334ffe0e5a06a6bcb901af2  SIGNED_PROMOTION_INTEGRATION_V1.md
4573f1e9f262f8a0caddfb6dfb617271ee2a073144f3b60ac95ea355a7d848cf  check_signed_integration.py
9a135a98f0c66db6843ccb6b1ce06e959b8eb961a15f909f04e15989c74e6e4d  SIGN_NOTATION_CORRESPONDENCE.md
dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc  PROMOTION_SIGN_C4_V2.md
36dd0b21dea51647dcbb9aef7c958d8f2ddadc397529e629ada5b122af0d2810  PROMOTION_certificate.py
```

The final coordinator integrity check exited zero:

```sh
python -B studies/two_layer_test_risk/check_signed_closeout.py --output data/generated/two_layer_test_risk/signed_closeout_20260910_01
```

It verified every frozen payload/current-source hash, report identity,
all recorded integration/B outputs and A's principal outputs, all four
embedded reviewer programs against executed source, exact chi/beta bounds,
21 Python source syntax trees and the current record/proposal links. This
is integrity verification, not a substitute for the complete proof reviews.
Checker SHA256 is
`60393b34867d80bd16d13bf9fe1ba5d6553af2d77bf5fd0c7665b5136f3dfbb6`;
result SHA256 is
`f8239d53391368fb66fe4a4b7aec4902d7a367c626f89c483e4374dd319878ce`.
No frozen scientific input was edited after any final review.

The closing Git transaction uses only explicit owned study files and the
common nonblocking writer lock. Its generated before/after metadata is in
`data/generated/two_layer_test_risk/signed_commit_20260910_01/`.
Unrelated readable dirty files are fingerprinted; the eight inherited
unreadable review files listed above remain metadata-only. No foreign file
is staged, reverted, moved or adopted. The two trailing TeX escaped spaces
in frozen SIGN_THEOREM lines 118/130 are intentionally preserved; the staged
whitespace check disables only end-of-line blank warnings after explicitly
verifying that these are the only two such owned lines.
