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
than only the corrections. Completion and evidence verification are pending.

## What no review can supply

The full-class local closure result and the bounded orthogonal fitting
result are distinct theorems. Neither proves a substantial-learning
horizon for all unbounded activations, a correlated-input fitting
neighborhood at that horizon, or an implemented general-activation solver.
The source-response and exponential-tail premises in the longer-horizon
theorems remain premises. No counterexample to the requested full C-X2
theorem has been established. The rare-event calculation excludes a
particular ambient local-Lipschitz proof tool only.
