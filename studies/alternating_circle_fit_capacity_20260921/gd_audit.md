# Independent audit of the GD-only campaign

The checker was derived and written before viewing GD campaign outcomes.
It imports neither `gd_benchmark.py` nor its helper routines. It uses direct
NumPy forward/backward contractions and the neutral initialization recipe.
The earlier `gd_check.py` and `gd_check.md` remain frozen and unchanged.

The complete frozen producer method and permitted initialization/data helper
definitions were reviewed. The implemented updates are simultaneous full-batch
scaled GD in stored `(W,middle,c)` coordinates with mobilities `(n,1,n)`.
Its scalar Armijo slope is the corresponding squared gradient norm. Every
trial reads the same previous state, all parameters are committed together,
and only accepted states enter the best-state selection. No momentum, Adam,
readout solve, clipping, Heun stage, or optimizer warm start is invoked.
The initialization helper implements the stated dictionary with the same
source matrix and its transpose and preserves the actual Gaussian readout.

Frozen scientific source SHA-256:

- `gd_benchmark.py`: `521421ddc8a3918e9ab5373d1959425499a80a55cbe8796fe025adf008b482af`.
- `GD_PROTOCOL.md`: `794723de3bdfcb9a95e1d906bf6b2b3486f561f854ae22284f30d623753f5a8f`.
- Selected helper source `fit_benchmark.py`: `6d16168b069ccbfef078bbe748fb0e760689187531e671901c8618f797f104a1`.

The replay checks all saved initial, best, and final training and circle-grid
predictions; initialization draws, fixed dictionary arrays and contraction;
source/configuration/artifact hashes; scalar counts; every accepted-step trace
entry's step, clock, slope and Armijo arithmetic; saved full before/after GD
pairs and their rejected trial scales; seeds, case-selection gates, controls,
reproductions and declared budgets. Retained parameter-pair updates use
`atol=2e-10, rtol=2e-11`; predictions use the protocol's `1e-8` maximum absolute
error and `1e-9` MSE error. Independent gradient norms use
`atol=1e-11, rtol=2e-8`, and physical squared gradient norms use
`atol=1e-12, rtol=2e-8`. Direct float64 replay may differ at roundoff level
because NumPy and CUDA associate contractions differently.

All accepted steps have trace arithmetic coverage. Only retained parameter
pairs have a full parameter update replay, so the audit does not claim full
trajectory recomputation. A finite gradient-floor endpoint is labelled
precision-limited and is not a convergence certificate. A wall-censored
reproduction with different step counts is distinguished from a discrepancy
at a common step. No additional training is authorized or run by the checker.

The replay has a hard 200-second CPU computation cap and records its elapsed
time and exact invocation in `gd_check_scratch/replay.json`. The earlier
CPU/GPU fixed-state preflights passed all nine test states on CPU, CUDA 0 and
CUDA 1; their immutable reports remain in the same scratch folder.

## Completed replay and validity verdict

Independent numerical/evidence audit: **PASS**, all 45 attempts and all campaign
checks, with no checker changes or reruns after freezing it. The campaign has
39 original attempts and six reproductions. The replay checked 815,613 accepted
steps' trace arithmetic and 220 retained full before/after parameter pairs.
Maximum independent prediction discrepancy, over initial/best/final training
and circle-grid predictions, was `3.1530333899354446e-14`. Maximum retained
parameter-update discrepancy was `1.7319479184152442e-14`. All source,
configuration, protocol and output hashes passed. All Gaussian source draws,
dictionary arrays and state/scalar counts passed. No numerical failure is
being reclassified as non-fitting.

The six predeclared reproduction choices and seeds were correct. Each repeated
fit status and endpoint MSE matched; all shared accepted-step MSE traces were
identical, and accepted step sizes and physical clocks were identical. None of
these six comparisons required the time-censoring exception. Some original
closure attempts did end at their wall limit, which remains a finite-budget
stop rather than an optimization or capacity certificate.

Worker-process wall usage was `1771.514387384057` seconds, within the registered
2500-second limit. Individual and reserved-batch budget checks passed. The
independent replay invocation was:

```text
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /usr/bin/time -f 'EXTERNAL_WALL_SECONDS=%e' /home/amir/miniconda3/bin/python -B studies/alternating_circle_fit_capacity_20260921/gd_replay.py
```

The script measured `91.0460748411715` seconds; the external process measurement
was `92.32` seconds. With the supervisor's conservative 20-second allowance for
earlier preflights, this leaves `187.68` seconds of the combined 300-second
check/analysis budget for the separately assigned final analysis. This is one
read-only replay; no training was performed by the checker.

Evidence hashes:

- Frozen checker `gd_replay.py`: `1976a6b4122b9d2f932f84d8190843e6dfcd7a293eae5d153c0bbb6e6cc4da01`.
- Audited terminal `gd_run01/run_record.json`: `b7a8be09dc00ccdef6f0620a659acf6b6dd8f77b92e4025a84fc5671a95b52bb`.
- Independent `gd_check_scratch/replay.json`: `594714ff950ae9a5aae3d10015a2bed543a7c45ecca1bca3c1dc1b846a5e463e`.

## Scientific gate and limits

**The registered separation requirement at both step caps did not pass.**
Numerical validity and successful reproductions do not change that decision.
At 30 and 62 samples, dense55 and closure1024 each fitted all three seeds. At
126 samples the original step cap produced the first candidate and correctly
stopped the size ladder:

| Initialization and maximum step | Dense55 fits | Dense105 fits | Closure1024 fits |
| --- | ---: | ---: | ---: |
| High gain, `eta_max=1` | 0/3 | 0/3 | 2/3 |
| High gain, `eta_max=0.5` | 0/3 | 0/3 | 1/3 |
| Canonical gain 1, `eta_max=1` | 0/3 | 0/3 | 0/3 |

The half-cap closure runs that missed the MSE target still classified all
training labels correctly: their best MSEs were approximately `0.00166046` and
`0.00110539`, both above the unchanged `0.001` threshold. Both ended at a wall
limit. The original-cap closure miss also ended at a wall limit, with best MSE
approximately `0.00144763` and zero sign errors. The high-gain dense failures
ended at the 30,000-step cap. The canonical controls reached the physical-clock
cap with MSE near one. These endpoints support statements about this bounded
optimizer and these initializations only.

The architectures did not stop at equal realized physical times: at 126
samples, high-gain dense endpoints were around `918–1306`, while closure
endpoints were around `3300–3454`. Their caps were shared, but the different
stopping times prevent treating the endpoint comparison as a comparison at
one common physical horizon. Maximum-step halving is a sensitivity check;
neither it nor the replay establishes convergence to GF, a capacity lower
bound, or an initialization-independent closure advantage. No run at 254
samples was added after the first-candidate stop.
