# Alternating-circle fitting: checked finite experiment

At the selected case m=254, the n=1024, p=1 closure met the frozen fitting
criterion in all three high-gain rescue attempts. Dense width 55 and the separate
total-size control, dense width 105, each met it in none of their three rescue
attempts. All three architectures failed the criterion in all canonical attempts
at this m. The closure successes were reached during Adam, without readout
polishing, and their saved states pass ordinary float64 independent replay.

This is an observed optimization advantage on these labels under the declared
solver and budget. The unsuccessful dense runs do not establish a capacity
lower bound. The result also does not assert convergence of a closure hierarchy,
equivalence to physical gradient flow, or prediction of unseen labels.

## Selected comparison and parameter accounting

Fit means unhalved training MSE <=0.001 and zero sign errors; RMS=sqrt(MSE).
The rescue multiplies only the initial first-layer weights by m/2=127, before
any closure dictionary is built. Canonical and rescue results remain separate.

| Model | Trainable scalars | Retained predictor scalars | Canonical fits | Rescue fits | Rescue RMS range |
|---|---:|---:|---:|---:|---:|
| Dense width 55 | 3190 | 3190 | 0/3 | 0/3 | 0.589435–0.648557 |
| Closure n=1024, p=1 | 3087 | 11279 | 0/3 | 3/3 | 0.0312831–0.0315973 |
| Dense width 105 | 11340 | 11340 | 0/3 | 0/3 | 0.241476–0.312843 |

The width 55 comparison approximately matches trainable parameters. The width 105
comparison approximately matches total retained predictor size. The closure's
8192 frozen dictionary scalars are included in its total; they are not trainable.
Temporary source matrices, optimizer workspace and diagnostic copies are excluded
from retained predictor size for the accounting in the frozen protocol.

The three closure rescue MSEs were 0.000998389, 0.000978630 and 0.000993181,
all with zero sign errors. Their maximum absolute residuals were respectively
0.235899, 0.244066 and 0.286906. Thus success is the stated MSE/sign criterion,
not exact interpolation or a pointwise 0.001 error bound. Width 55 rescue sign
errors were 40, 50, 42; width 105 rescue sign errors were 8, 8, 16.

## Why m=254 was selected

The fixed ladder used equally spaced points theta_j=2*pi*j/m and labels (-1)^j
for m=30,62,126,254. Each m/2 is odd, so antipodal labels have the opposite sign,
consistent with the bias-free odd tanh architecture. No points or labels were
selected after training.

| m | Width 55 canonical fits | Width 55 rescue fits | Gate consequence |
|---:|---:|---:|---|
| 30 | 3/3 | Not run | Canonical fit found |
| 62 | 2/3 | Not run | Canonical fitted parameter witnesses found after readout polish |
| 126 | 0/3 | 1/3 | Rescue fit found |
| 254 | 0/3 | 0/3 | First m>55 with no fit in all six declared attempts |

Consequently only m=254 received the conditional closure and width 105 comparison.
No unreported rescue runs were used at m=30 or 62. The width 55 success at m=126
already refutes a blanket claim that width 55 cannot fit more than 55 of these labels.

## Every original seed and initialization

Each cell is **checked training MSE (number of sign errors)**. These are all
30 original attempts; the three same-settings reproductions are listed separately.
A dagger marks an explicit high-precision adjudication with the original float64
agreement failure retained in the evidence. It does not mark a rejected attempt.
Values are rounded here; the CSV retains full numerical precision.

| Model | m | Initialization | Seed 20260921 | Seed 20260922 | Seed 20260923 | Fits |
|---|---:|---|---:|---:|---:|---:|
| Dense width 55 | 30 | canonical | 0.000879699201 (0) | 0.000858318088 (0) | 0.000817613534 (0) | 3/3 |
| Dense width 55 | 62 | canonical | 8.06906863e-11 (0)† | 4.89366421e-10 (0)† | 0.689410635 (18)† | 2/3 |
| Dense width 55 | 126 | canonical | 0.999999957 (62)† | 1 (62) | 1 (68) | 0/3 |
| Dense width 55 | 126 | rescue | 0.000960690308 (0) | 0.0444559431 (2) | 0.135491905 (4) | 1/3 |
| Dense width 55 | 254 | canonical | 1 (134) | 1 (130) | 1 (130) | 0/3 |
| Dense width 55 | 254 | rescue | 0.356142054 (40) | 0.420626248 (50) | 0.347433631 (42) | 0/3 |
| Closure n=1024, p=1 | 254 | canonical | 1 (132) | 1 (134) | 1 (118) | 0/3 |
| Closure n=1024, p=1 | 254 | rescue | 0.000998388513 (0) | 0.000978630137 (0) | 0.000993180934 (0) | 3/3 |
| Dense width 105 | 254 | canonical | 1 (126) | 1 (128) | 1 (124) | 0/3 |
| Dense width 105 | 254 | rescue | 0.0854728764 (8) | 0.0583107452 (8) | 0.0978707265 (16) | 0/3 |

Success counts are the primary result. Training stops as soon as the fitting
threshold is attained. In particular, m=30 losses near 0.0008 and m=62 polished
losses near 1e-10 do not mean that m=62 is easier; their stopping mechanisms differ.
No minimum across initializations replaces the seed-specific outcomes above.

## Optimization, readout dependence and budget

All models used float64 CUDA full-batch optimization in equivalent coordinates
W,middle,v=c/n, with at most 8000 Adam steps, the same two learning rates and
LBFGS settings, followed where prescribed by an unconstrained least-squares
readout solve with rcond=1e-12. This is optimization, not time integration of the
physical gradient-flow equations. Identical caps/settings do not imply identical
executed iteration counts or arithmetic cost.

The m=254 closure rescues fit after 3141, 1725, 3453 Adam steps and stopped before
LBFGS or readout polishing. Their attempt times were 10.861, 6.561, 11.653 seconds.
Both dense rescue suites used all 8000 Adam steps, then LBFGS and readout polishing,
and still failed the criterion. Saved gradients, norms, saturation, phase traces,
polish rank and conditioning diagnostics remain in each attempt's record.

At m=62 the two width 55 successes depended on the prescribed linear readout solve:
both pre-polish best MSEs were essentially 1. Their canonical readout norms grew
to approximately 1.91e12 and 1.10e13. The study has no weight-norm bound, so these
are admissible finite parameter witnesses, with their numerical sensitivity
explicitly checked below. The third seed remained a failure after polishing.
The width 55 m=126 rescue success was reached during LBFGS.

There were 33 launched attempts: 30 original attempts and 3 reproductions, within
the maximum 39. Summed worker-process wall time was 821.842654 seconds of 2500;
this includes worker setup and output and is not elapsed time on one GPU.
All recorded attempt times respected the 60-second cap; the maximum was 36.942
seconds. The complete launch manifest also preserves the pauses for numerical
adjudication; no attempt was discarded or retrained during those pauses.

## Numerical verification and reproductions

The independent checker replayed all 33 saved attempts and checked output hashes.
Its final campaign audit passed the literal seed/gate sequence, source/config
provenance, dictionary construction, parameter counts, timing limits and
reproduction selection. This is an internal experimental check, not a promotion
review or theorem about representational capacity.
All initializations matched the prescribed construction (largest reported array
discrepancy 5.45e-15). The separate analysis implements both forward formulas
directly in NumPy and recomputes each initial, best and final loss/sign count.

Twenty-nine attempts pass the strict float64 replay tolerances: maximum prediction
discrepancy 1e-8 and MSE discrepancy 1e-9. Four polished canonical width 55 attempts
(all three m=62 seeds and m=126 seed 20260921) exceed the strict prediction tolerance.
Their failures remain visible in the raw records, CSV and red crosses in the
all-attempt figure. Independent evaluation of the saved best parameters at 60
and 90 decimal digits stabilizes every affected fit decision; record, checkpoint
and dataset hashes tie those decisions to the original artifacts. The m=62
adjudicated MSEs are 8.06906863e-11, 4.89366421e-10, 0.689410635; the m=126 adjudicated
MSE is 0.999999957. Higher-precision replay interprets stored binary64 weights
and samples as exact real inputs; it is numerical precision stabilization,
not an interval-arithmetic certificate. It does not erase the original float64
reproduction discrepancies.

All m=254 attempts, including the three reproductions, pass the strict float64
checks. Therefore the selected closure advantage does not depend on accepting
one of the high-precision exceptions.

For each selected-case model, the lowest-MSE original attempt was reproduced
with exactly the same settings in a fresh directory. These are numerical
reproductions, not extra independent seeds. The losses and fit classifications
agreed exactly in the saved evaluation results, stronger than the required
MSE agreement of 1e-6.

| Model | Repeated seed | Initialization | Reproduced MSE | Sign errors | MSE difference | Outcome |
|---|---:|---|---:|---:|---:|---|
| Dense width 55 | 20260923 | rescue | 0.347433631002 | 42 | 0 | no fit |
| Closure n=1024, p=1 | 20260922 | rescue | 0.000978630136503 | 0 | 0 | fit |
| Dense width 105 | 20260922 | rescue | 0.0583107451745 | 8 | 0 | no fit |

Complete independent checks and their scope are recorded in
[fit_check.md](/home/amir/Codes/PDE/studies/alternating_circle_fit_capacity_20260921/fit_check.md),
[campaign_audit.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/check_scratch/campaign_audit.json),
[producer_replay.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/check_scratch/producer_replay.json), and
[numerical_adjudications.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/check_scratch/numerical_adjudications.json).

## Representability controls and remaining claim boundary

The checker separately constructed finite-weight dense-network witnesses with
q=m/2 active neurons: widths 55,55,63,127 for m=30,62,126,254, respectively,
padding when q<=55. All four have numerically checked MSE below 2e-28 and zero
sign errors. Their saved construction/replay evidence is in
[witness_summary.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/check_scratch/witnesses_v2/witness_summary.json) and
[replay_summary.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/check_scratch/witnesses_v2/replay_summary.json).
They were not optimizer warm starts or trained baselines.

The first two constructions establish explicit width 55 representability at
m=30/62; the trained width 55 m=126 rescue also supplies a fitted witness. The
width 127 construction at m=254 is an upper-bound witness, not a lower bound
excluding widths 55 or 105. Their m=254 failures remain finite optimization
failures under this suite. Only three fixed seeds, this circle orientation,
these labels and this prescribed gain were tested. A general architecture-level
capacity ordering or generalization advantage remains open.

## Artifacts and reproduction

- [All attempt metrics](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/attempts.csv), [group counts](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/groups.csv), [readout checkpoints](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/readout_states.csv), and [analysis provenance](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/analysis.json).
- [Every attempt: log-MSE against m](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/all_attempts_mse.png) ([PDF](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/all_attempts_mse.pdf)).
- [Selected-case loss traces](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/selected_m254_loss.png) ([PDF](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/selected_m254_loss.pdf)); faint lines are all evaluations, bold lines running minima, and stars readout polishing.
- [Selected-case predictions and actual training labels](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/selected_m254_predictions.png) ([PDF](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/analysis01/selected_m254_predictions.pdf)); no between-sample ground truth is invented.
- [Complete run manifest](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/run01/run_record.json), including exact worker commands, frozen configuration/source hashes, every seed, termination status and reproduction pairing.

The analysis command was:

```bash
/home/amir/miniconda3/bin/python -B studies/alternating_circle_fit_capacity_20260921/fit_analyze.py --run-root data/generated/alternating_circle_fit_capacity_20260921/run01 --out data/generated/alternating_circle_fit_capacity_20260921/analysis01 --selected-m 254 --adjudications data/generated/alternating_circle_fit_capacity_20260921/check_scratch/numerical_adjudications.json
```

Run from `/home/amir/Codes/PDE`. For another analysis replay, choose a fresh output
directory: the script refuses to overwrite an existing directory. Raw training
artifacts are read-only inputs to analysis. These results remain study-local and
have not been promoted to established repository theory or maintained APIs.
