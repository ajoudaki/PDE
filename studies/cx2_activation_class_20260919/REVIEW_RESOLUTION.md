# Internal review record for the C-X2 partial result

This record concerns the exact partial and conditional results in
`PARTIAL_RESULT.md`, not completion of C-X2 or promotion. The study's first
scoped commit is `6a39978fd161a12de3ae410bfaefad878251ea7b`.

## Frozen inputs and independence

The complete packets are generated under
`data/generated/cx2_activation_class_20260919/review_r1_inputs/` and
`review_r2_inputs/`. Their manifests are also retained as
`REVIEW_R1_INPUTS.json` and `REVIEW_R2_INPUTS.json` in this study. Each packet
contains all four candidate proof files, the deterministic check, canonical
notation, complete necessary book sections, and the finite implementation
with its complete repository import dependencies. They do not depend on
another study or a historical verdict.

Each reviewer starts with a neutral assignment and no inherited discussion,
reads all inputs and required skills, independently checks all claims and
scope, reproduces the bounded deterministic checks, and verifies the input
hashes before and after review. Reports preserve objections. The author and
assembler identities are excluded from reviewer selection. Reviewer writes
are confined to their assigned report and generated scratch. These are
internal scientific reviews; there is no promotion/integration verdict.

`ALTERNATIVE_PROOF.md` is a separate author exploration outside both frozen
packets. None of the reviews applies to that file by association.

## First complete reviews and corrections

Reports `INTERNAL_REVIEW_R1_A.md` and `INTERNAL_REVIEW_R1_B.md` each cover
all 5,636 input lines and reproduce the two supplied-state tests. Both
support the principal partial/conditional conclusions subject to the same
two narrow corrections in `SOURCE_PROOF.md`:

1. Section 3 must say that the cap `B` bounds the source-response row
   `sum_q |beta_iq|`, whereas the actual backward coefficient row `D`
   additionally contains the learned Gram term and is bounded by `D_*`.
2. The passive preactivation's named derivative has bound
   `M sqrt(m)` times the maximum clock pulse. The additional factor `M`
   arises only after applying the outer activation. The corrected text
   distinguishes both bounds, including when `M<1`.

Both corrections have been applied to the author file. No other scientific
input changed between packets. Three trailing spaces were also removed
before the first scoped commit; the original frozen packet remains intact.
The source proof now has 651 lines, and the complete second packet has
5,643 lines. The change neither enlarges a conclusion nor closes the
long-horizon gap.

The supervisor personally read both full reports. Direct recomputation
verified every frozen SHA256, every reviewer's before/after hash record,
all hashes printed in the reports, and both successful test run records.
The frozen maintained dependencies remain exact excerpts or copies of the
current maintained sources. Machine-readable evidence is
`data/generated/cx2_activation_class_20260919/supervisor_r1_verification.json`.

## Fresh complete review of the corrected package

Two new isolated reviewers received only their neutral assignments and
the complete second packet. These reviews inspect the whole result rather
than only the corrections. Both completed all 5,643 input lines, repaired
truncated reads, reproduced the supplied identity tests, and accepted the
expressly partial and conditional conclusions without required corrections:

- `INTERNAL_REVIEW_R2_A.md`, reviewer `cx2_partial_review_r2_a`;
- `INTERNAL_REVIEW_R2_B.md`, reviewer `cx2_partial_review_r2_b`.

The supervisor personally read both full reports and verified their hashes,
all thirteen input hashes, reported coverage, retained before/after checks,
test logs, and exact correspondence with the current author files and
maintained dependencies. The R2-A initial check was originally displayed
in the reviewer's tool output. At the supervisor's request, the reviewer
preserved that original command/output with its tool-response identifier;
it was not recomputed and relabeled as an earlier check. No original wall
timestamp was supplied, and none is invented.

R2-A additionally checked every raw gradient, mobility-weighted velocity
and kernel block by independent finite differences on twelve supplied-state
activation/geometry combinations. Its source is preserved byte-for-byte as
`review_r2_a_checks.py`; outputs remain in the generated namespace.
These checks and the single guide API update are not training experiments.

The final manifest SHA256 is
`e157377112c43577948b3a90c8966ff929ebc5c8154d29fc98416898a5e7bf37`.
Final report SHA256 values are:

- R2-A: `1a681f4d5e52bd0734a36460d11eb6e7b08e976b7a84f258eda5365dc9942599`;
- R2-B: `6fe6b7cc22b3ffc5a58a09d80feab78aa7e5497e0b8b66b13f73927d4de27c8a`.

Machine-readable supervisor verification is retained as
`data/generated/cx2_activation_class_20260919/supervisor_r2_verification.json`.
The source corrections and R1 records were committed in
`5d88ee2f34c82da750b97c76507a07cffea3f5d9` before these final reports.
No reviewed scientific input changed during or after the R2 audits.

## What no review can supply

The full-class local closure result and the bounded orthogonal fitting
result are distinct theorems. Neither proves a substantial-learning
horizon for all unbounded activations, a correlated-input fitting
neighborhood at that horizon, or an implemented general-activation solver.
The source-response and exponential-tail premises in the longer-horizon
theorems remain premises. No counterexample to the requested full C-X2
theorem has been established. The rare-event calculation excludes a
particular ambient local-Lipschitz proof tool only.
