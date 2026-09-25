# Internal final activation-circle evidence check

This is an internal check of the bounded, single-seed experiment, not promotion
or a proof of hierarchy convergence. The independent panel rescore, inventory,
accounting, and eight cross-GPU repetitions pass. All 82 completed saved states
have passing replay evidence after one isolated recheck; the original failed
initialization-hash check remains recorded and its cause is unknown. The
bounded campaign is complete, while unavailable fitted comparisons and the
exhausted SELU refinement remain scientifically inconclusive. The reviewer
launched no training or GPU work, sent no process signals, and changed no
frozen campaign dependency.

## Independent panel arithmetic

`check_activation_final_metrics.py` imports NumPy only for numerical work; it
imports neither the producer nor the analyzer. It reads each valid run's saved
training and circle predictions, checks archive hashes/CRC and metadata,
independently selects the two finest available resolutions, and recomputes
circle RMS, nested-grid change, solver sensitivity, physical-loss/time gates,
availability, and the order-comparison margins.

The append-only receipt
`data/generated/neural_response_memory_20260922/activation_circle_audit_final01/panel_rescore01.json`
passes with no failures. Every recomputed score, sensitivity, loss, time, and
ranking scalar agrees exactly with the recorded value. All gates and verdicts
agree. Coverage is 66 valid scientific trajectories, 72 matched-loss rows,
24 primary slots, three common-loss fallback rows, 27 matched-time rows, and
72 order comparisons. The 15 unavailable primary slots are retained explicitly.

The checked final metrics hash is
`d2b2e522152dfaabb65df268b50bc21b847d0267b7e5c0c76f2dfc4e0a2b271e`.
The independent checker hash is
`eae5ba7fd6d6b6c135ce2ab496381488fcaf2c223dd3a918d94239e87d2864ad`;
its receipt hash is
`0a064bf80318735cdb7d9e7d420da1e041f044bbbb7d73428b391c06f7a0141c`.
The exact command is retained in that receipt. Reproduction recipe:

```bash
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
/home/amir/miniconda3/bin/python studies/neural_response_memory_20260922/check_activation_final_metrics.py \
  --metrics data/generated/neural_response_memory_20260922/activation_circle_analysis_final03/metrics_summary.json \
  --output data/generated/neural_response_memory_20260922/activation_circle_audit_final01/panel_rescore02.json
```

## What the final accuracy numbers support

All nine available primary comparisons pass the protocol's numerical gates.
Their circle RMS errors at each model's own training-MSE `.001` crossing are:

| Activation/task | P1 | P2 | P3 |
|---|---:|---:|---:|
| GELU, two outliers | 1.439745959 | 0.242388805 | 0.024854432 |
| GELU, quadrant | 5.783894822 | 0.663486173 | 0.260103786 |
| Sigmoid, two outliers | 0.664149236 | 0.268268541 | 0.241369637 |

Only GELU P3 on the two-outlier task satisfies the declared circle-RMS `.1`
coarse-agreement threshold. The other eight measured primary comparisons are
resolved coarse disagreements. The other 15 primary slots are unavailable;
they must not be described as demonstrated agreement or disagreement at the
fitted endpoint.

All 72 remaining shared-loss comparisons pass their numerical gates, but this
statement applies only where the selected finest trajectories share a saved
crossing. Of 27 fixed-time diagnostics, 15 pass and 12 remain numerically
inconclusive (12 fail the dense-relative sensitivity gate; two of those also
fail the closure-relative gate). Fixed-time diagnostics do not independently
authorize further trajectories under this protocol.

The sigmoid quadrant fallback uses training MSE `.1`, with P1/P2/P3 circle
errors `0.267296612`, `0.203490369`, and `0.157355042`. These are secondary
coarse disagreements, not substitute fitted-endpoint results.

There are 70 resolved order improvements and two resolved worsenings. Both
worsenings compare P2 with P3 at training MSE `.5` for sigmoid: quadrant
error increases by `0.150928811` against observed sensitivity margin
`0.000552277`; two-outlier error increases by `0.030434810` against margin
`0.000656125`. Thus the data do not support a blanket monotonicity claim.

## Inventory and the exhausted SELU refinement

The final analyzer records all 64 scheduled primary configurations as valid,
plus two valid additional-resolution trajectories. Of these 66 trajectories,
28 reach target loss and 38 stop at the wall limit. The original external
resource interruption is separately retained as one failed attempt; it is not
a numerical failure and is not counted as a valid scientific trajectory.

An independently delegated inventory check reconstructs exactly the 64 logical
primary keys: eight activation/task cases, four models, two tolerances. Their
successful executions split 34/4/26 across the original and two continuation
roots; the additional external interruption makes 65 actual primary attempts.
All 32 case/model selections use the two smallest executed scientific
tolerances. Saved crossing sets independently yield 72 available/96 missing
loss comparisons and 27 available/45 missing fixed-time comparisons.

The two extra executions exactly match the primary analysis's gate-triggered
requests: SELU/two-outlier dense and P3 at tolerance `7.8125e-7`. At loss `.9`,
the primary P2 row failed the dense-relative gate, and P3 failed both relative
gates. Their original circle errors were `9.099414608736058e-6` and
`5.028104348879406e-7`; common dense sensitivity was
`1.0101774407366468e-6`, while P3 sensitivity was
`6.981700893406861e-7`. These failed diagnostics are preserved in
`activation_circle_analysis_primary03/metrics_summary.json`.

**The extra executions did not resolve those failed comparisons.** Both were
wall-capped. The finest dense run stopped at MSE `0.9091679344253312`, time
`1.3173730968005097`, before any requested loss crossing. The finest P3 run
stopped at MSE `0.8859327767198272`, time `1.6974608968805511`, after crossing
`.9`. Using the required common finest dense reference therefore removes all
three former SELU `.9` comparisons. Evaluated rows decrease from 75 to 72 and
missing rows increase from 93 to 96; the two failed rows were not demonstrated
to pass. Empty final `required_refinements` and `unresolved_after_refinement`
lists mean no further authorized refinement branch remains. They do not
establish SELU fidelity or eliminate the missing evidence.

## Final accounting and state checks

Summing the executed job charges in the original primary, continuation01,
continuation02, refinement03, and repetition03 receipts, then adding the
original receipt's pilot carry-in, independently reproduces the controller's
total `18424.841682184488` integration seconds. This includes the external
interruption and all eight repetitions, and is below the unchanged 33,000-second
limit. The 83 executed attempts comprise eight pilots, 65 primary attempts,
two additional resolutions, and eight repetitions; the limit is 113 including
the permitted external restart. Cancelled-before-launch rows are retained but
neither charged nor counted as executed.

The final replay plan contains 82 unique completed saved states in 21 batches:
eight pilots, 66 scientific trajectories, and eight repetitions. Its run set
exactly matches the independent inventory. The interrupted attempt has no
completed saved-state summary and is explicitly excluded; the 55 historical
cancelled-before-launch rows are also explicitly excluded.

The original 82 replay records contain 2,677 passing integrity/trace checks and
499 passing physical-prediction/diagnostic panels. Maximum absolute differences
are `4.68158845023936e-12` on the circle,
`6.307843136710289e-12` on training predictions, and
`6.252776074688882e-13` on diagnostics, below the unchanged `2e-9` replay limit.

**One original run-level audit failure is retained.** In
`activation_circle_audit03/replay_batch_018.json`, the repeated SELU/two-outlier
dense trajectory at `7.8125e-7` returned `initialization_hash=false`. Its other
19 checks and both physical panels passed, with exactly matching circle and
training predictions. Consequently, the immutable original workflow remains
`complete_with_audit_failures` and records 81/82 run-level replay passes.

The independent fresh CPU regeneration in
`activation_circle_audit_final01/initialization_recheck01.json` matches the
summary/manifest's canonical initialization hash. The coordinator then ran the
same frozen checker on only that same saved run, without retraining or changing
inputs, tolerances, or gates. `activation_circle_audit03/replay_recovery01.json`
passes all checks, including initialization, and both physical panels again
match circle/training predictions exactly. Its SHA-256 is
`3bae14a06b7ad2abe021b1b1590bf8194e6136928e6b4d117b9aba9458917973`.
Thus aggregate saved-state coverage is 82/82 after the retained failure and
isolated recheck. The original checker did not record its computed hash, so the
cause of the initial discrepancy is undetermined; no hardware or software
cause is inferred and the original failure is not erased.

All eight raw repetition results pass every check, including the GPU swap and
unchanged runner/backend. They cover dense and P3 on the two-outlier task for
each activation. The four fitted GELU/sigmoid repeats have equal endpoints
with exact states, events, and accepted traces. The four capped ReLU/SELU
repeats have different wall-limited endpoints, but exact nonempty shared trace
prefixes and exact shared observations/checkpoints; different capped endpoints
are not mislabeled as equal. Cross-GPU coverage is therefore 8/8,
not merely the resource-amended numerical-only assessment.

The reviewer checked every individual boolean and panel result, compared
standalone batch/reproduction files with the embedded workflow records,
verified the isolated recovery is for the sole failed run, and confirmed the
final metrics remained unchanged. The derived receipt
`activation_circle_audit_final01/final_receipt_check01.json` passes all 14
aggregate checks and preserves input hashes (receipt SHA-256
`a955beca8677eb9063335e5d6eba90d1032304a78421a4b64cc528957b2f3f3b`).
The historical workflow SHA-256 remains
`dc641e9a40da7a8dd95f116886529d790df74e86c3104baec0b97c3815914523`.
