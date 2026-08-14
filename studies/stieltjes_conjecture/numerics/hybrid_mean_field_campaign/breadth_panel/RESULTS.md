# Breadth-panel local validation result

Status: **terminated by the preregistered two-failure hard stop**.

A and V fail local numerical gates and are scientifically inconclusive; M passes local validation only.  The two-failure hard stop terminates the panel before any width screen or two-input run is authorized or recorded, so this round adds no Stieltjes evidence.

## Frozen-gate outcome

| config | local outcome | max h2/h1 Keff | max h2/h1 Kdir | max h2/h1 Q2 | decisive failed gates |
|---|---|---:|---:|---:|---|
| A | fail (inconclusive) | 0.02589% | 0.02592% | 0.01375% | w_cosine, driver_max |
| M | pass (local-pass-only) | 0.04066% | 0.03996% | 0.02005% | none |
| V | fail (inconclusive) | 0.01917% | 0.01881% | 0.00928% | w_cosine |

All three coarse/fine kernel comparisons pass the frozen 0.20% ceiling. M's separately required Q2 comparison also passes.  A nevertheless fails because its fine-run driver maximum is 0.29284% (limit 0.20%) and its minimum sampled-W update cosine is 0.981127203 (floor 0.995).  V fails because its fine-run minimum sampled-W cosine is 0.990178347. Unchanged-update fractions were retained as red flags and were not promoted to gates.

M is only a qualification of this FP32 Euler method for that configuration.  No width ladder is authorized or recorded, so M is not a finite-width Stieltjes compatibility result.

## Provenance and scope

The analyzer verified 23 locked source/data hashes, the lock-implied bundle, the execution unlock, all six manifest/raw hashes, the exact point contracts, deterministic/TF32 settings, resource caps, common initial and prefix digests, and exactly six completed ledger reservations.  The raw archives remain ignored; their digests are retained in `VALIDATION_RESULT.json`.

Actual summed outer runtime was 26.075 s; peak recorded allocation was 0.657 GiB GPU and 0.946 GiB host RSS.

By the frozen contract, two local-method failures stop the entire panel.  Therefore no one-input width screen, two-input validation, Stieltjes-bound comparison, or evidential claim is authorized or recorded in this round.

The frozen protocol and point JSON deliberately retain their prospective pre-execution headers; this report and VALIDATION_RESULT.json are the terminal decision artifacts.

## Reproduction

From the repository root, run `python studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/breadth_panel/validation_analysis.py --check` to reverify the locally preserved, Git-ignored NPZ arrays against the tracked manifests and result.  Use `--write` instead of `--check` to regenerate both compact outputs.

`VALIDATION_RESULT.json` SHA-256: `38f901805fd2b25c4678b556f74d5c49b99a0d56cd836458951d29fdfe2352c9`.
