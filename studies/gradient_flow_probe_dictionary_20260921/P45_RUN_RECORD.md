# P4/p5 extension execution record

P45_PROTOCOL.md was written before implementation completion and before
training. The independent derivation agrees with the root's expansion:
p4 retains the p3 raw spans; p5 has 14 lower and24 upper prescribed generators.
The finite Taylor oracle independently checks the middle coefficients through
t6, including non-diagonal empirical Grams. The finite training candidate uses
the population-derived moments rather than asserting exact finite-jet equality.

Available conservative prior balance2174.519788134843 seconds. This extension
has a hard new2100-second summed GPU-worker ceiling. Initial training reservation
four workers at400 seconds each,1600 total; preflight reserve60 and analysis/audit
reserve120 are included within2100. Unused reservations are released on finish.
Conditional extra attempts are reserved later only after the prescribed gate.

Producer p45_run.py imports the unchanged original adaptive-Heun trajectory
producer and original initialization reader. All invocations use the existing
/home/amir/miniconda3/bin/python -B, CUDA float64, with PYTHONDONTWRITEBYTECODE=1
and OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. Exact argument arrays,
initial checkpoint/array hashes and all critical source hashes are written
into each invocation's config. No existing result or producer is overwritten.

GPU availability check found two idle RTX3090s, apart from unrelated small
allocations. No unrelated process was changed. Both GPUs are accessed through
the already authorized sandbox escalation. No installation or checkout copy.

## Completed base runs

The130 independent CPU implementation checks passed with maximum error
1.5543122344752192e-15; the independent finite Taylor oracle passed through t6.
The finalized-source GPU preflight passed in2.3129771314561367 seconds.
Observed raw numerical ranks at width4096 were(6,12) forp4 and(14,24) forp5.
The largest ridge condition was33442.620667703355 and the largest triangular
relative residual was1.4337795969246945e-16. Both are within protocol gates.

| Output root | Worker | Device | Level | Worker seconds | Fitted |
|---|---:|---|---:|---:|---:|
| p45_primary01 | 0 | cuda:0 | 0 | 13.308539018034935 | 2/2 |
| p45_primary01 | 1 | cuda:1 | 0 | 40.610396940261126 | 2/2 |
| p45_refined01 | 0 | cuda:0 | 1 | 18.34347839280963 | 2/2 |
| p45_refined01 | 1 | cuda:1 | 1 | 43.513886753469706 | 2/2 |

All eight newly requested trajectories fitted; total new training-worker
time115.7763011045754 seconds. Release all four base reservations. The archived
full-network and p3 trajectories were read, not rerun. Each new model retains
its own first accepted MSE0.001 crossing and all preceding loss/state records.

The root's direct-state audit p45_analysis01 completed in8.19337148219347
seconds oncuda:0. All six rows (including archived newp3) are valid. Largest
new-model cross-tolerance endpoint discrepancy is0.004622831437816721, below
0.01. There are no extra-eligible cells; no conditional run is authorized or
reserved. Root recomputation gives identical RMS ordering at both tolerances.
Training, preflight and root analysis have used126.282649718225 seconds;
independent audit accounting will be added when complete.

## Independent audit and terminal accounting

The independent p45_independent_check.py worker used cuda:1 and the same
Python/environment. It replayed all 112 saved snapshots in 12 trajectories,
including the four archived dense references, in 20.054256800562143 seconds.
Maximum prediction discrepancy4.440892098500626e-15, independent basis
discrepancy1.2434497875801753e-14; all fitting and numerical gates passed.
An earlier invocation of the checker under an interpreter without Torch
exited before GPU work; it is not a training attempt and no result was replaced.

Its raw1165-check audit retains14 broad historical manifest flags, confined
to four original-study ancillary files: README.md, scaling_independent_check.py,
scaling_radial_export.py and scaling_width4096_plots.py. The manifest had
included every sibling Python file. CPU-only dependency-graph reconciliation
confirmed all executed producer/dictionary/engine sources match and these
four files were not trajectory inputs. Raw flags remain preserved in
p45_independent01; no scientific-source mismatch was excused. The independent
metrics were frozen before reading the root's analysis. All156 agreement
checks passed with maximum scalar difference1.3322676295501878e-15.
Root read the full raw audit, independent checker, P45_INDEPENDENT_AUDIT.md
and reconciliation evidence.

Terminal new charged GPU-worker time146.33690651878715 seconds:
115.7763011045754 training +2.3129771314561367 preflight
+8.19337148219347 root replay +20.054256800562143 independent replay.
Conservative cumulative charge3971.817118383944 of6000 seconds;
remaining2028.182881616056 seconds. Release every unused reservation.
No extra cell is eligible, no worker remains active, and the requested
bounded p4/p5 protocol is complete. No further training is authorized by
this completed protocol. Tracked working tree and shared Git index are
unchanged; concurrent untracked studies were preserved.
