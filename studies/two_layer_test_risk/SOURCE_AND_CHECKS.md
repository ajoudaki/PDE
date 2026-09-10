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

## Frozen promotion checks and closeout

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
