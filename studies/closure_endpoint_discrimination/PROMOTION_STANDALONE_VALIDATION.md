# Standalone validation of the combined proposed edition

Current corrected edition: `promotion_20260916/integrated03`, source manifest
SHA256 `3808b2228bd2b5dc76c64ba42736dbfd19b2418be25d04a75627c4a813ec673c`.
Its fresh validation is recorded at the end. The initial integrated02 checks
below remain preserved with their original scopes and harness correction.

Coordinator: `/root`, 2026-09-16. This is the Part 2.4 standalone check, not a
scientific or integration review. No live docs/code or Git index was changed.
The independently prepared additions retain their separate originating-study
provenance. Combining their frozen additions is promotion-stage coordination.

The edition is
`data/generated/closure_endpoint_discrimination/promotion_20260916/integrated02/`.
Its source manifest SHA256 is
`c0f902a99ce737d2d4833e9b9e5a07ed70dc4d34a1cba023f0eb671638e4e503`.
`PROMOTION_INTEGRATE_EDITION.py` is the flat retained assembly source. It checks
the three candidate manifests and established dependencies, copies the canonical
docs/code only, applies twelve additions plus four precisely scoped edits, and
preserves 56 existing files byte for byte. No repository, Git directory, worktree,
study source, conversation, archived array, or historical verdict is part of the
maintained edition. Four frozen originals support exact preservation checks.
`ASSEMBLY.json` records source/destination hashes and the complete baseline.

## Executed standalone checks

From `/home/amir/Codes/PDE`, using the retained harness:

```sh
python3 studies/closure_endpoint_discrimination/PROMOTION_VALIDATE_EDITION.py --edition data/generated/closure_endpoint_discrimination/promotion_20260916/integrated02 --device cpu --python /home/amir/miniconda3/bin/python --run root_cpu02
python3 studies/closure_endpoint_discrimination/PROMOTION_VALIDATE_EDITION.py --edition data/generated/closure_endpoint_discrimination/promotion_20260916/integrated02 --device cuda:0 --python /home/amir/miniconda3/bin/python --run root_cuda02
```

The harness launches all actual library commands with the edition as working
directory and its code as the sole added Python path. Numerical thread limits
are one; bytecode is disabled; CUBLAS_WORKSPACE_CONFIG is `:4096:8`; temporary
directories and fresh outputs are inside its `data/established/`. Resource limits
were recorded before training: 600 seconds total, 120 seconds per command,
fixed tiny producer settings only. CUDA access used the authorized GPU tool
execution; no installation or new training campaign occurred.

CPU validation completed all 13 commands, including structural links/imports,
five boundary fixtures, sixteen maintained initializer tests, seven maintained
solver tests, NumPy-only package import, both complete new guides' Python
examples, the four circle suites, twelve general-p1 suites, both maintained
producers, exact general-p1 repeat, and independent NumPy replay. The complete
command window was 12.994 seconds. CUDA producer/general-p1 validation completed
in 11.067 seconds. These windows include child-process setup/imports and outputs,
and do not measure a solver speed ratio.

All seven new local Markdown links, including both added chapter-fragment
targets, were also checked by the retained harness's `check_added_links`
function. The exact targets and checker hash are recorded in
`data/established/root_links/record.json`. This supplements the library-wide
structural file-link check; it does not claim to revalidate every old fragment.

**Harness correction retained:** the first harness revision set
PDE_TEST_DEVICE but omitted the circle suite's separate CIRCLE_TEST_DEVICE.
Therefore its circle test invocations in root_cuda01/root_cuda02 actually used
CPU. Their records remain unchanged and must not be cited as CUDA suite evidence.
The circle producer did use its explicit CUDA command, and each independent
scientific reviewer ran the correctly selected CUDA suite. Root separately ran
the exact unmodified circle suite with CIRCLE_TEST_DEVICE=cuda:0, one thread and
a 120-second limit; all four tests passed in 1.048 seconds. Its full command,
environment, source hash, exit status and original output are in
`data/established/root_cuda_circle_supplement/`. The retained harness now sets
and records both device selectors plus the circle scratch directory.

## Fresh producer/replay results

| Check | CPU | CUDA:0 |
|---|---:|---:|
| Circle maximum final CPU-reference discrepancy, p=1,3,5 | 3.470e-18 | 1.735e-18 |
| Circle own-state continuation | exact at all three orders | exact at all three orders |
| General-p1 independent NumPy prediction/Gram replay, maximum discrepancy | 2.220e-16 | 1.110e-16 |
| General-p1 same-configuration repeated saved arrays | exact | exact |
| Circle peak allocated CUDA bytes | not applicable | 34,144,768 |
| General-p1 peak allocated/reserved CUDA bytes | not applicable | 33,610,752 / 35,651,584 |

The circle producer uses d=2, p=1,3,5, Q=64, P=32, four steps of .005 and four
fixed weighted input directions. The general-p1 producer uses d=3, n=P=16,
nominal antithetic P with eight stored base rows, nine input rows, seed101 and
ten steps of .005. Its synthetic law includes zero and repeated inputs.
Input generation and all numerical sources are maintained in the proposed
edition. No retained study array was used. The complete original records,
source/output hashes, environment and failed/successful process logs are in
the named edition-local output directories.

The general producer explicitly separates initialization/transfer, data/current
state setup, each synchronized integration, observations/analysis/checkpoint
writing, and its delimited work window. Process RSS and CUDA peaks include
both systems; retained tensor counts are separate. The circle producer also
separates initialization/transfer, evolution and observations. These measurements
show the recipes operate within their limits, not faster training or matched
prediction accuracy.

## Scope and remaining gate

These checks establish finite implementation agreement, own-state restart,
reproducible finite examples and standalone operation. They do not establish
quadrature accuracy, ODE convergence for arbitrary steps, learned-network
approximation, general-d trained-network convergence, universal improvement
with order, or historical MNIST/PCA/circle endpoint claims. No such empirical
claim is included. The complete fresh scientific and integration reviews,
concrete user approval, and post-approval correspondence checks remain distinct.
Historical packets/checks, the corrected harness record, and adverse campaign
evidence are preserved. Established docs/code and the shared index remain
unchanged by this work.

## Corrected integrated03 validation

The general-p1 constant-correlation correction, extra regression test and
complete dictionary proof dependencies were frozen as first_order_dimension_mnist
`frozen_v3` before this edition was assembled. Both old adverse reports remain
in that study. Circle candidate04 and the explanatory insertion are unchanged.

The same retained harness was executed with `--edition
data/generated/closure_endpoint_discrimination/promotion_20260916/integrated03`,
`--device cpu --run root_cpu03` and `--device cuda:0 --run root_cuda03`, using
`/home/amir/miniconda3/bin/python`. It now explicitly records both correct test
device selectors. All 13 CPU commands and all six CUDA commands passed. This
includes all 13 general-p1 tests and all four circle tests on the requested
device, fresh bounded producers, independent NumPy replay and exact repeat
arrays. Both guides, NumPy-only import, library boundary tests, affected old
tests, all new local links and their added chapter fragments pass.

All inputs, resource limits, environment, command vectors, wall durations,
original outputs and source/output hashes are in edition-local
`data/established/root_cpu03/validation.json` and
`data/established/root_cuda03/validation.json`; no old output was consumed.
The final state/reference discrepancies and replay discrepancies are unchanged
at the displayed precision from the earlier table. The exact proposed diff is
`PROMOTION.diff`, SHA256
`ea6d1b79bbcde9247b8093066360f32818495c8f34eb77f90cd991d8a304b302`.
Twelve new files and four existing-file edits are mapped; 56 unrelated existing
files remain byte-identical. The four original edited-file baselines are frozen
for integration review. All maintained source hashes remain unchanged after
validation. The fresh scientific pair and separate fresh integration review
remain requirements; these checks do not substitute for them.

## Corrected metric edition integrated04

Frozen source manifest `1220b4160830a79513b0c025a2746797f16e6e1a91f1c498118914ce43adf808`;
exact diff `6cf28af320ec117b1fcfcbbdad17bc01739e56b157a3299bea9f3a0522175c96`.
It combines general-p1 frozen_v4 with byte-identical accepted circle and explanatory
packets. The v3-to-v4 scientific changes are only the comparison module, its tests
and its numerical guide; the neutral assignment path version also changes.

Fresh standalone validation records are inside integrated04/data/established/:

- `root_cpu04/validation.json`: all 13 commands pass in 13.0804 seconds, including
  16 general-p1 tests, four all-order circle tests, the maintained dependency/boundary
  suites, both guides, clean package import, both producers and independent replay.
- `root_cuda04/validation.json`: all six commands pass in 11.6955 seconds on
  cuda:0, with both correct device selectors explicitly recorded; the same 16
  general-p1 and four all-order circle tests execute on CUDA.
- Each run checks all 74 frozen source hashes before and after and the seven
  added local links/fragments. Exact commands, environment, original logs and
  generated-output hashes are retained in these records.

Before training, both command windows recorded a 600-second total limit,
120 seconds per command, one numerical thread and fixed tiny inputs/seeds.
Independent NumPy replay errors are 2.220446049250313e-16 CPU and
1.1102230246251565e-16 CUDA; repeated arrays match exactly. Prediction relative
RMS in this tiny example is about 1.067, explicitly showing that successful
operation/replay is not a neural-approximation conclusion. No fit, benchmark,
dataset campaign or favorable accuracy claim is selected from these outputs.

The complete scientific pair and subsequent independent integration review
remain separate gates. These coordinator checks do not substitute for them.

## Integration-only discovery adapter: integrated05

The original complete [integrated04 review](PROMOTION_INTEGRATION_REVIEW_FINAL.md)
requires optional-Torch test discovery to preserve the existing NumPy-only
contract. It is retained unchanged, SHA256
`6d54f53f268da99cc153ca724f82321f9ebd03881fcd54419fac461690438b98`.
The coordinator read it completely. No scientific correction was identified.

[Exact adapter scope](../first_order_dimension_mnist/PROMOTION_OPTIONAL_TEST_DISCOVERY.md):
guarded optional imports/setup and explicit tensor-class skips. All 16 test
bodies and all scientific modules/proofs/recipes are unchanged. The assembler
verifies literal test-body preservation against frozen_v4 and records both hashes.
This integration-only correction requires a new complete integration review,
without changing the scientific content cleared by the original paired reviews.

Final source manifest `83e0e4b3c1238880e7a8d87fdb251233a41b491462c8fa3e14a0fa3443c6ff3e`.

- `root_cpu05/validation.json`: 14 commands pass in 13.7522 seconds.

- `root_cuda05/validation.json`: 6 commands pass in 11.8599 seconds.

NumPy-only discovery now runs all 16 cases: eight NumPy tests pass and eight
tensor tests explicitly skip. With Torch, all 16 pass on CPU and actual CUDA.
Both full four-test circle suites and fresh producers/analyzers also pass;
links, guide examples, dependency checks and all 74 frozen hashes pass.
No skipped case is counted as a Torch pass. The fresh independent integration
review is separately pending.

The fresh complete [integrated05 review](PROMOTION_INTEGRATION_REVIEW_05.md)
passes with no required correction. Coordinator root read every line of its
original report and checked complete coverage, neutral input provenance, actual
CPU/CUDA evidence, unchanged test bodies and all frozen hashes. The final check
found no live baseline drift. The full accepted report SHA256 is
`3a19eab8cfa97258342ff6ee0aa9ac96210028d86ce71f13188d18f170d335fe`.
User approval remains required; no live integration or Git transaction occurred.
