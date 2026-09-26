# Broad-ridge canonical-flow pilot

**Closed: this pilot did not produce the desired separation.** The width-244
dense model fitted the training sample to normalized RMS 0.008335 with only
21% growth in median first-weight norm. Its unseen error was 1.11859, worse
than zero prediction. None of the four models improved on zero prediction at
its terminal unseen panel. All runs were compute-capped, so this does not
establish eventual failure or a population width lower bound.

Common comparison time: **30.0**. Horizon censored: **True**.

One fixed target and one initialization; the two tolerances are numerical reproduction, not seed replication.

| Model | Training normalized RMS | Unseen normalized RMS | Median W norm ratio | Numerical gates |
|---|---:|---:|---:|---|
| Closure · 1024 | 0.991216 | 1.00067 | 1.001 | True |
| Dense · 244 | 0.9904 | 1.00027 | 1.001 | True |
| Dense · 492 | 0.990697 | 1.00039 | 1.001 | True |
| Full dense · 1024 | 0.989718 | 1.00079 | 1.001 | True |

Error one is the zero predictor baseline. Passive data do not enter updates.

Comparison decisions: `{"width244": {"training_error_ratio": 1.0008242518899373, "passive_error_ratio": 1.0004032173406245, "encouraging_signal": false}, "width492": {"training_error_ratio": 1.0005244044468613, "passive_error_ratio": 1.00028094620952, "encouraging_signal": false}}`.

![Loss](../../data/generated/broad_ridge_canonical_probe_20260921/analysis01/loss.png)

This bounded-time pilot does not prove a width lower bound or an all-time fitting failure.
All individual terminal times, status flags, numerical comparisons and raw metrics are retained in analysis.json.

Worker process seconds: 884.540 / 960.

Manifest SHA-256: `527825aea2cdb99fdb1a699cb4113f9c66e0846f6b61fe7908b58ebfe9c8e2ce`.

## Actual tighter-tolerance endpoints

**These endpoints have different physical times and are not a matched-time ranking.**
Every cutoff is recorded explicitly. Small training error demonstrates fitting of this sample, not learning of the population target.

| Model | Last physical time | Training normalized RMS | Unseen normalized RMS | Median W norm ratio | Status |
|---|---:|---:|---:|---:|---|
| closure1024 | 130.065 | 0.553599 | 1.01243 | 1.107 | wall_censored |
| width244 | 242.326 | 0.00833515 | 1.11859 | 1.21 | wall_censored |
| width492 | 147.505 | 0.124484 | 1.04147 | 1.172 | wall_censored |
| width1024 | 96.8769 | 0.874396 | 1.01556 | 1.046 | wall_censored |

![Full saved loss curves](../../data/generated/broad_ridge_canonical_probe_20260921/analysis01/loss_with_endpoints.png)

Training curves use every accepted-step loss. Passive curves connect saved evaluations; neither line extends beyond its observed cutoff.

Independent replay covered 8 runs; maximum saved-prediction error was 0 and terminal-RHS error 2.08e-16.
Replay SHA-256: `6271301976934089eb9c343aa1e132df07ea0cb9e758abb71f75e3420920a46b`.

## Descriptive supplement for the matched predictors

The three matched predictors have resolved checkpoints through time 100.
The full-width reference stopped before that checkpoint at the fine tolerance, so this supplement does not replace the precommitted all-four comparison.

| Model | Training normalized RMS | Unseen normalized RMS |
|---|---:|---:|
| closure1024 | 0.927083 | 1.01947 |
| width244 | 0.876239 | 1.01875 |
| width492 | 0.868205 | 1.01674 |
