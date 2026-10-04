# Frozen circle-RMS growth selection

2026-10-03T21:59:37.431152+00:00. Frozen before any validation seed is evaluated.

Calibration selected N0=48, response rank16, P0=2550. Its largest sqrt(n)*E over all12 calibration cases was 0.07516408706344334, below the predeclared0.10 margin. Rank12 at the same count had maximum0.07764335792216384, so the predetermined error tie-break chose rank16. N96/rank24 failed positive-mass construction on one case and is globally disqualified; the original failed run and recovery are retained. No sampler or flow source changed during recovery.

The same low-order initialization-only source family, rank16,32 setup probes and massfloor .05 are fixed for allvalidation. Four budget rules P_budget(n)=2550[log(n)/log(512)]^p, p=0,1,2,4 are tested. Select the largest N with N^2+5N+6<=budget. Repeated identicalmodels atn512 are computational aliases, not additional independent replicates.

| n | p | N | actual P |
|---:|---:|---:|---:|
| 512 | 0 | 48 | 2550 |
| 512 | 1 | 48 | 2550 |
| 512 | 2 | 48 | 2550 |
| 512 | 4 | 48 | 2550 |
| 1024 | 0 | 48 | 2550 |
| 1024 | 1 | 50 | 2756 |
| 1024 | 2 | 53 | 3080 |
| 1024 | 4 | 59 | 3782 |
| 2048 | 0 | 48 | 2550 |
| 2048 | 1 | 53 | 3080 |
| 2048 | 2 | 59 | 3782 |
| 2048 | 4 | 72 | 5550 |
| 4096 | 0 | 48 | 2550 |
| 4096 | 1 | 55 | 3306 |
| 4096 | 2 | 64 | 4422 |
| 4096 | 4 | 87 | 8010 |
| 8192 | 0 | 48 | 2550 |
| 8192 | 1 | 58 | 3660 |
| 8192 | 2 | 70 | 5256 |
| 8192 | 4 | 102 | 10920 |

Validation: n512,1024,2048,4096; freshreference seeds8511--8515; independentdense seed+10000; angles60,90; labels(.2,+/-.1). No held-out trajectory ormetric was read before freezing.

Calibration summary SHA256: `51f8f55e74a95bdda0dc58898cf4b9e88f8b4792358b2ced36d231ac30e483b0`.
Protocol SHA256: `b603672426f6d5c5a95ebb0a71c87194a45939659802a030ed5cd102b8c4fbc3`.

Generated calibration roots: gpu_rms_growth_20261003_calibration_90, _60, _60_resume; analysis: gpu_rms_growth_20261003_calibration_analysis. Source/instance/failure records are preserved.
