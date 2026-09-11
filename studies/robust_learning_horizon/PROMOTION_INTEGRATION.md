# Approved P1 incorporation

On 2026-09-11 the user approved promotion:

> btw, I approve of promoting this to the established part, please follow the gates workflow for this

This approval applies to the exact two-file [P1 proposal](PROMOTION_PROPOSAL.md),
manifest SHA256
`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.
The proposal's pending wording is preserved as its historical checkpoint.
The coordinator applied the reviewed editions without scientific changes.

## Gates and approval scope

The independent [relevance screen](RELEVANCE.md) selected the narrow C.4.5
addition and guide update. Complete original scientific
[review A](P1_REVIEW_A.md), [review B](P1_REVIEW_B.md), and separate
[integration review](P1_INTEGRATION_REVIEW.md) each accepted exact P1 without
required corrections. [P1_REVIEW_COMPLETION.md](P1_REVIEW_COMPLETION.md)
retains author/reviewer identities, isolation, complete reading and execution
evidence, input/report hashes and the coordinator's full-report verification.
[P1_VALIDATION.md](P1_VALIDATION.md) records standalone validation.

A fresh bounded [gate evidence check](PROMOTION_GATE_CHECK.md), distinct from
scientific review, verified all frozen inputs, assignments, full reports,
review output inventories, standalone records and current dependencies:
151 hash checks and 43 correspondence checks passed. The coordinator read
this complete report and verified its SHA256
`38c0713b05d426931d67b4cbf31c19bac23578ae1753da2b9638e6e15d56a145`.
The gate check's evidence SHA256 is
`ef7cda722266ca077d6cc70646e47999971ebbf57286835697a7af10b50d1410`.
The completed original reviews remain reusable under Part 2 because their
complete evidence and all scientific inputs are unchanged. No new scientific
verdict is being substituted for them.

The incorporated theorem retains `T=40`, `delta=exp(-exp(3000))`, the
whole-circle reference endpoint, population and empirical risk bounds `1/4`,
and both-layer paired activity at `1/200`. The formal sufficient GD condition
remains `eta_k sqrt(n_k)->0`, with the reviewed proof's existing sharper-step
remark unchanged. No later conversational frozen-feature comparison was added.
The extraordinarily small certified neighborhood and absence of a proved
feature-learning advantage remain explicit limitations.

## Exact candidate-to-live mapping

| Live destination | Reviewed complete source | Final SHA256 |
|---|---|---|
| `docs/global_nonlinear.md` | [P1_GLOBAL_EDITION.md](P1_GLOBAL_EDITION.md) | `d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1` |
| `docs/README.md` | [P1_DOCS_README.md](P1_DOCS_README.md) | `7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e` |

The baseline hashes were respectively
`1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9`
and `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e`.
Immediately before writing, the coordinator verified both live baselines,
all manifest inputs, every dependency span and its complete live source hash.
Only the exact accepted transition was applied: five chapter scope replacements,
the complete 1,633-line C.4.5 addition, and two guide replacements. Existing
proof bodies are preserved. The live heading begins at chapter line 5260.
Both live files equal both their reviewed sources and the newly reconstructed
validation editions byte for byte. All other scientific dependencies remain
unchanged.

## Actual integration checks

Working directory: `/home/amir/Codes/PDE`; Python `3.10.12`.
The fresh deterministic validation command was:

```sh
python studies/robust_learning_horizon/validate_candidate.py --inputs studies/robust_learning_horizon --output data/generated/robust_learning_horizon/promotion_integration_01/edition
git diff --check -- docs/global_nonlinear.md docs/README.md
cmp docs/global_nonlinear.md studies/robust_learning_horizon/P1_GLOBAL_EDITION.md
cmp docs/README.md studies/robust_learning_horizon/P1_DOCS_README.md
```

All exited zero. The validator reconstructed the exact edition, verified
frozen inputs/dependency excerpts, checked the new markup and embedded
certificate correspondence, and ran both exact-rational certificates.
Both certificates exited zero with empty stderr. Their stdout hashes are:

| Output | SHA256 |
|---|---|
| Reference certificate stdout | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` |
| Transfer certificate stdout | `97089ac3bf0eebb7a3b7058c4bc1e2e64c6f6af6321af84ff86569d9d0806df5` |

The reference stdout was
`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.
The transfer certificate reported PASS, including transport constant `661180`,
risk Lipschitz constant `44928`, raw speed `4082`, response exponent `2880`,
response prefactor `225400`, and the theorem's stated times, radius and activity.

All generated integration evidence is under
`data/generated/robust_learning_horizon/promotion_integration_01/`:

| Record | SHA256 |
|---|---|
| `preflight.json` | `b6e9142511cf01ce169a2cef2c5f73f4b2f655b8d7ac95fa8dcb81eb66a0ff69` |
| `edition/validation.json` | `7b7a22c05384443d9497df414311fc89da4331461aba65e29d2434623e8e5eb7` |
| `post_integration.json` | `c971d48564d0e932ef8f84848726b77a5e114e319570f348d6a0b651af9d3e71` |

The initial preflight stopped before any live write when it encountered an
unreadable unrelated inherited maintenance report. This failed attempt is
retained in `preflight_attempt_01.json`. The corrected preflight follows the
workflow's metadata-only rule for unreadable inherited files. Fourteen
unrelated working files were preserved: readable contents were hash checked;
eight unreadable files were checked only by size, modification time, mode and
ownership. None was edited, staged or adopted by this task. The index was empty
before integration.

These are deterministic assembly, correspondence and arithmetic checks, not
a proof-assistant certification, training experiment, renderer test or new
whole-book proof audit. The original independent full reviews supply the
scientific and placement review. No generated product is included in commits.

## Scoped commit

The coordinator is the sole Git writer and uses the common nonblocking
`pde-writer.lock` for each short stage/verify/commit transaction. The checked
pre-integration HEAD was `0ecf05026913c678bef57b3967962effc73c453d`.
The integration commit is
`bee4161f810048cff84dcbac1e61ea7abe097e1d`
(`Promote reviewed robust learning horizon as established C.4.5`). Under the
lock the coordinator rechecked HEAD, the empty index and all five owned file
hashes, staged only those files, verified the staged names and bytes, and ran
the staged whitespace check. The committed paths and bytes then matched those
exact inputs, and the index was empty after the commit. The other three files
in that commit are this record, the study README and the fresh gate report.
`promotion_integration_01/commit_inputs.json` and `integration_commit.json`
retain the transaction's exact inputs and result. This final study-record
update records the completed integration without changing either established
file. The original frozen packet, assignments and full reports are unchanged.

Promotion is complete for this exact package. No required gate, correction or
approval remains outstanding.
