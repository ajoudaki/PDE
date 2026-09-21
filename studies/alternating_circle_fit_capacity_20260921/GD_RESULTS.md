# GD-only alternating-circle fitting results

The high-gain GD ladder produced a candidate at m=126, but the registered separation did not survive both step caps. Closure fits were 2/3 at maximum step 1 and 1/3 at maximum step 0.5; dense width 55 fitted 0/3 and 0/3, respectively. This does not establish a step-cap-insensitive fitting advantage within the frozen wall-time and step budgets.

There was a clear training-error advantage at m=126 under both step caps: all six original high-gain closure attempts had zero sign errors and MSE between 0.000999884 and 0.001660463. Dense width 55 had MSE 0.296–0.330 and 14–22 sign errors; dense width 105 had MSE 0.0344–0.118 and 4–8 sign errors. At m=30 and m=62, both the closure and width 55 fitted all three seeds. These are finite optimization outcomes, not representation lower bounds.

This report concerns full-batch simultaneous gradient descent with canonical mobilities (n,1,n) and scalar Armijo backtracking. It uses no Adam, momentum, clipping, least-squares readout solve, optimizer warm start or quasi-Newton stage. A fit requires unhalved training MSE ≤0.001 and zero nonpositive signed margins. The high-gain initialization multiplies W by m/2; the canonical control uses gain 1.

## Checked fit counts

| m | Initialization | Maximum step | Model | Fits / 3 | Valid / 3 | Best-MSE range |
| --- | --- | --- | --- | --- | --- | --- |
| 30 | high | 1 | width55 | 3/3 | 3/3 | 0.00094136–0.00098818 |
| 30 | high | 1 | closure1024 | 3/3 | 3/3 | 0.00094394–0.00099471 |
| 62 | high | 1 | width55 | 3/3 | 3/3 | 0.00099637–0.00099842 |
| 62 | high | 1 | closure1024 | 3/3 | 3/3 | 0.00099857–0.00099996 |
| 126 | high | 1 | width55 | 0/3 | 3/3 | 0.29625–0.33032 |
| 126 | high | 1 | closure1024 | 2/3 | 3/3 | 0.00099988–0.0014476 |
| 126 | high | 1 | width105 | 0/3 | 3/3 | 0.034353–0.11803 |
| 126 | high | 0.5 | width55 | 0/3 | 3/3 | 0.29632–0.33036 |
| 126 | high | 0.5 | closure1024 | 1/3 | 3/3 | 0.00099999–0.0016605 |
| 126 | high | 0.5 | width105 | 0/3 | 3/3 | 0.03436–0.11805 |
| 126 | canonical | 1 | width55 | 0/3 | 3/3 | 1–1 |
| 126 | canonical | 1 | closure1024 | 0/3 | 3/3 | 1–1 |
| 126 | canonical | 1 | width105 | 0/3 | 3/3 | 1–1 |

The independently computed selected case is 126; the recorded case is 126. Selection agrees: yes. The first-candidate stopping rule is valid: yes.

## Step-cap and initialization controls

For width55, separation at maximum step 1: yes; at maximum step 0.5: no; registered separation at both caps: no.

For width105, separation at maximum step 1: yes; at maximum step 0.5: no; registered separation at both caps: no.

With canonical gain 1, the separate checked fit counts were width55: 0/3; closure1024: 0/3; width105: 0/3.

At maximum step 0.5, the following closure attempts reached the wall-time limit with zero sign errors but remained above the strict MSE fit threshold: seed 20260921, MSE 0.00166046271, 28173 accepted steps, physical clock 3417.73438; seed 20260923, MSE 0.00110538965, 28165 accepted steps, physical clock 3419.85938. They count as nonfits under the frozen protocol; no continuation was run.

Halving a maximum scalar step is a learning-rate sensitivity check. It does not prove convergence to continuous gradient flow. Realized steps and physical clocks below must be considered because the same wall-time/step/evaluation caps can terminate architectures at different points. Canonical initialization results are separate controls, not additional high-gain seeds.

## Optimization endpoints at the selected case

| Model | Gain | η max | Accepted steps | Physical clock | Attempt seconds | Realized η range | Final Q range | Stops |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| width55 | high | 1 | 30000–30000 | 1000.5–1306 | 57.141–60.519 | 0.015625–1 | 3.0705e-05–8.8923e-05 | step_limit: 3 |
| closure1024 | high | 1 | 24353–27183 | 3301.9–3454 | 59.813–70.951 | 0.015625–1 | 1.6281e-05–4.1648e-05 | fit_reached: 2, time_limit: 1 |
| width105 | high | 1 | 30000–30000 | 921.02–1013.1 | 58.137–61.324 | 0.015625–1 | 8.9097e-06–5.9427e-05 | step_limit: 3 |
| width55 | high | 0.5 | 30000–30000 | 997.39–1301.6 | 56.964–60.771 | 0.015625–0.5 | 8.6244e-05–0.00017995 | step_limit: 3 |
| closure1024 | high | 0.5 | 27076–28173 | 3299.6–3419.9 | 64.847–71.023 | 0.015625–0.5 | 1.8988e-05–5.7972e-05 | fit_reached: 1, time_limit: 2 |
| width105 | high | 0.5 | 30000–30000 | 917.7–1009.5 | 57.374–61.681 | 0.015625–0.5 | 8.4663e-06–0.00012316 | step_limit: 3 |
| width55 | canonical | 1 | 10000–10000 | 10000–10000 | 13.51–14.223 | 1–1 | 1.022e-15–2.853e-15 | physical_clock_limit: 3 |
| closure1024 | canonical | 1 | 10000–10000 | 10000–10000 | 17.59–18.652 | 1–1 | 5.387e-21–2.0233e-19 | physical_clock_limit: 3 |
| width105 | canonical | 1 | 10000–10000 | 10000–10000 | 13.684–14.411 | 1–1 | 3.2893e-16–3.2091e-15 | physical_clock_limit: 3 |

## Every original attempt

MSE, RMSE and sign errors are recomputed from the best saved canonical arrays. Q is the physical squared gradient norm at the final accepted state. Exact values, initial/final diagnostics, wall times, realized step ranges and all replay discrepancies appear in attempts.csv.

| m | Model | Gain | η max | Seed | Initial MSE | Best MSE | RMSE | Sign errors | Steps | Clock | Final Q | Stop | Valid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | width55 | high | 1 | 20260921 | 0.9998 | 0.00098053 | 0.031313 | 0 | 274 | 70.312 | 0.00035721 | fit_reached | yes |
| 30 | width55 | high | 1 | 20260922 | 1.0002 | 0.00094136 | 0.030682 | 0 | 341 | 82.375 | 0.00018042 | fit_reached | yes |
| 30 | width55 | high | 1 | 20260923 | 1.0001 | 0.00098818 | 0.031435 | 0 | 219 | 68.25 | 0.00074069 | fit_reached | yes |
| 30 | closure1024 | high | 1 | 20260921 | 1 | 0.00099471 | 0.031539 | 0 | 1274 | 594.19 | 9.2021e-05 | fit_reached | yes |
| 30 | closure1024 | high | 1 | 20260922 | 1 | 0.00098133 | 0.031326 | 0 | 831 | 780.5 | 0.00010392 | fit_reached | yes |
| 30 | closure1024 | high | 1 | 20260923 | 1 | 0.00094394 | 0.030724 | 0 | 614 | 432.31 | 0.00029211 | fit_reached | yes |
| 62 | width55 | high | 1 | 20260921 | 1 | 0.00099842 | 0.031598 | 0 | 5326 | 376.59 | 0.00029658 | fit_reached | yes |
| 62 | width55 | high | 1 | 20260922 | 1 | 0.00099637 | 0.031565 | 0 | 10830 | 639.06 | 0.00023738 | fit_reached | yes |
| 62 | width55 | high | 1 | 20260923 | 0.99993 | 0.00099722 | 0.031579 | 0 | 2121 | 238.44 | 0.0001009 | fit_reached | yes |
| 62 | closure1024 | high | 1 | 20260921 | 1 | 0.00099857 | 0.0316 | 0 | 3701 | 1620.3 | 0.0010039 | fit_reached | yes |
| 62 | closure1024 | high | 1 | 20260922 | 1 | 0.00099996 | 0.031622 | 0 | 4903 | 1446.3 | 5.3068e-05 | fit_reached | yes |
| 62 | closure1024 | high | 1 | 20260923 | 1 | 0.00099994 | 0.031622 | 0 | 2640 | 1416.1 | 4.1862e-05 | fit_reached | yes |
| 126 | width55 | high | 1 | 20260921 | 1.0001 | 0.3237 | 0.56895 | 22 | 30000 | 1306 | 3.0705e-05 | step_limit | yes |
| 126 | width55 | high | 1 | 20260922 | 0.99998 | 0.29625 | 0.54429 | 14 | 30000 | 1000.5 | 8.5326e-05 | step_limit | yes |
| 126 | width55 | high | 1 | 20260923 | 1.0001 | 0.33032 | 0.57474 | 22 | 30000 | 1002.4 | 8.8923e-05 | step_limit | yes |
| 126 | closure1024 | high | 1 | 20260921 | 1 | 0.0014476 | 0.038048 | 0 | 27183 | 3454 | 2.7449e-05 | time_limit | yes |
| 126 | closure1024 | high | 1 | 20260922 | 1 | 0.00099992 | 0.031622 | 0 | 24353 | 3301.9 | 4.1648e-05 | fit_reached | yes |
| 126 | closure1024 | high | 1 | 20260923 | 1 | 0.00099988 | 0.031621 | 0 | 26160 | 3437.8 | 1.6281e-05 | fit_reached | yes |
| 126 | width105 | high | 1 | 20260921 | 0.99998 | 0.081244 | 0.28503 | 4 | 30000 | 929.36 | 4.6517e-05 | step_limit | yes |
| 126 | width105 | high | 1 | 20260922 | 1 | 0.11803 | 0.34355 | 8 | 30000 | 921.02 | 5.9427e-05 | step_limit | yes |
| 126 | width105 | high | 1 | 20260923 | 1 | 0.034353 | 0.18535 | 4 | 30000 | 1013.1 | 8.9097e-06 | step_limit | yes |
| 126 | width55 | high | 0.5 | 20260921 | 1.0001 | 0.32377 | 0.56901 | 22 | 30000 | 1301.6 | 0.00017995 | step_limit | yes |
| 126 | width55 | high | 0.5 | 20260922 | 0.99998 | 0.29632 | 0.54435 | 14 | 30000 | 997.39 | 8.6811e-05 | step_limit | yes |
| 126 | width55 | high | 0.5 | 20260923 | 1.0001 | 0.33036 | 0.57477 | 22 | 30000 | 999.95 | 8.6244e-05 | step_limit | yes |
| 126 | closure1024 | high | 0.5 | 20260921 | 1 | 0.0016605 | 0.040749 | 0 | 28173 | 3417.7 | 1.8988e-05 | time_limit | yes |
| 126 | closure1024 | high | 0.5 | 20260922 | 1 | 0.00099999 | 0.031623 | 0 | 27076 | 3299.6 | 4.8468e-05 | fit_reached | yes |
| 126 | closure1024 | high | 0.5 | 20260923 | 1 | 0.0011054 | 0.033247 | 0 | 28165 | 3419.9 | 5.7972e-05 | time_limit | yes |
| 126 | width105 | high | 0.5 | 20260921 | 0.99998 | 0.081282 | 0.2851 | 4 | 30000 | 926.83 | 0.00012316 | step_limit | yes |
| 126 | width105 | high | 0.5 | 20260922 | 1 | 0.11805 | 0.34359 | 8 | 30000 | 917.7 | 3.391e-05 | step_limit | yes |
| 126 | width105 | high | 0.5 | 20260923 | 1 | 0.03436 | 0.18536 | 4 | 30000 | 1009.5 | 8.4663e-06 | step_limit | yes |
| 126 | width55 | canonical | 1 | 20260921 | 1 | 1 | 1 | 66 | 10000 | 10000 | 2.4364e-15 | physical_clock_limit | yes |
| 126 | width55 | canonical | 1 | 20260922 | 1 | 1 | 1 | 64 | 10000 | 10000 | 1.022e-15 | physical_clock_limit | yes |
| 126 | width55 | canonical | 1 | 20260923 | 1 | 1 | 1 | 60 | 10000 | 10000 | 2.853e-15 | physical_clock_limit | yes |
| 126 | closure1024 | canonical | 1 | 20260921 | 1 | 1 | 1 | 60 | 10000 | 10000 | 9.8701e-20 | physical_clock_limit | yes |
| 126 | closure1024 | canonical | 1 | 20260922 | 1 | 1 | 1 | 62 | 10000 | 10000 | 2.0233e-19 | physical_clock_limit | yes |
| 126 | closure1024 | canonical | 1 | 20260923 | 1 | 1 | 1 | 66 | 10000 | 10000 | 5.387e-21 | physical_clock_limit | yes |
| 126 | width105 | canonical | 1 | 20260921 | 1 | 1 | 1 | 62 | 10000 | 10000 | 3.2893e-16 | physical_clock_limit | yes |
| 126 | width105 | canonical | 1 | 20260922 | 1 | 1 | 1 | 64 | 10000 | 10000 | 1.1413e-15 | physical_clock_limit | yes |
| 126 | width105 | canonical | 1 | 20260923 | 1 | 1 | 1 | 64 | 10000 | 10000 | 3.2091e-15 | physical_clock_limit | yes |

## Reproductions

Reproductions use the first successful seed in increasing order, or seed 20260921 when no seed fitted, with the same device and settings. They are not additional seeds. The registered stability gate compares fit status and final endpoint MSE (absolute difference ≤1e−6). Unequal accepted-step counts involving a wall stop are separately labelled time-censored; their common accepted-step prefix is compared without extra training. Prefix equality does not replace the endpoint gate.

| Model | η max | Expected seed | Actual seed | Final-MSE difference | Same fit | Stable | Time-censored | Identical shared trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| width55 | 1 | 20260921 | 20260921 | 0 | yes | yes | no | yes |
| closure1024 | 1 | 20260922 | 20260922 | 0 | yes | yes | no | yes |
| width105 | 1 | 20260921 | 20260921 | 0 | yes | yes | no | yes |
| width55 | 0.5 | 20260921 | 20260921 | 0 | yes | yes | no | yes |
| closure1024 | 0.5 | 20260922 | 20260922 | 0 | yes | yes | no | yes |
| width105 | 0.5 | 20260921 | 20260921 | 0 | yes | yes | no | yes |

| Model | η max | Seed | Best MSE | RMSE | Sign errors | Steps | Clock | Final Q | Stop | Valid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| width55 | 1 | 20260921 | 0.3237 | 0.56895 | 22 | 30000 | 1306 | 3.0705e-05 | step_limit | yes |
| closure1024 | 1 | 20260922 | 0.00099992 | 0.031622 | 0 | 24353 | 3301.9 | 4.1648e-05 | fit_reached | yes |
| width105 | 1 | 20260921 | 0.081244 | 0.28503 | 4 | 30000 | 929.36 | 4.6517e-05 | step_limit | yes |
| width55 | 0.5 | 20260921 | 0.32377 | 0.56901 | 22 | 30000 | 1301.6 | 0.00017995 | step_limit | yes |
| closure1024 | 0.5 | 20260922 | 0.00099999 | 0.031623 | 0 | 27076 | 3299.6 | 4.8468e-05 | fit_reached | yes |
| width105 | 0.5 | 20260921 | 0.081282 | 0.2851 | 4 | 30000 | 926.83 | 0.00012316 | step_limit | yes |

## Numerical and budget audit

All independent NumPy train/circle/endpoint-gradient replays passed: yes. All accepted-step Armijo/clock/evaluation traces passed: yes. The separate construction, source, gradient and update-pair checker passed: yes. All attempt decision gates passed: yes.

The manifest contains 45 attempts (39 originals and 6 reproductions). Total worker-process wall time is 1771.514s / 2500s; budget arithmetic passed: yes. Campaign status: complete.

Independent analysis took 58.12s for the complete process, including imports, replay, plots and report export. Together with the separate checker's 92.32s and a conservative 20s preflight allowance, the combined checking/analysis total is 170.44s / 300s. The external timing record is [timing.json](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/timing.json).

Each attempt was capped at 30,000 accepted steps, 90,000 training forward evaluations, physical clock 10,000, and 75 seconds including initialization and export, with five seconds reserved for export. Wall/step/clock caps are endpoint descriptions, not proofs of a converged minimum. Gradient-floor endpoints are precision-limited; tanh backward uses 1−h² and rounded saturation can make it zero. Saturation fractions and all endpoint gradients are retained in attempts.csv. A failed line search or unexplained numerical discrepancy blocks the affected comparison.

The dataset, odd antipodal parity, all seeds, gains and stages are frozen. Width 55 matches trainable scalar count approximately (3,190 versus 3,087); width 105 matches total retained predictor scalars approximately (11,340 versus 11,279). The closure count includes 8,192 frozen dictionary scalars and excludes the discarded source A. These are parameter-count controls, not equal-width, equal-compute or generalization comparisons.

## Artifacts

- [All raw-array diagnostics](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/attempts.csv)
- [Machine-readable audit](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/analysis.json)
- [Sample ladder figure](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_sample_ladder.png)
- [Separate independent checker](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_check_scratch/replay.json)

- [Learning curves versus physical clock](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_selected_m126_physical_clock.png)
- [Learning curves versus accepted updates](/home/amir/Codes/PDE/data/generated/alternating_circle_fit_capacity_20260921/gd_analysis01/gd_selected_m126_accepted_steps.png)

The strongest defensible claim is empirical performance under these finite attempts. Failure to fit cannot establish that either architecture lacks a fitting representation. The controls do not establish asymptotic convergence, a continuous-flow limit, generalization, or a universal sample-efficiency advantage.
