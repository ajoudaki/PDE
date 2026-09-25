# Independent check of the 100-image, width-4096 MNIST comparison

Status: PASS for data, algebra, isolation, all eight primary runs, the final
analysis and both swapped-GPU reproductions. This is an internal numerical
audit, not an independent promotion review or a convergence theorem.

## Scope and independence

The check reads the frozen MNIST100_PROTOCOL.md, the specified scientific
equations, producer/runner/analyzer sources and designated data/run artifacts.
It does not use another audit's findings. check_mnist100_moments.py is adapted
from the earlier checker, with the nested subset, width, tolerance schedule,
source provenance and state dimensions checked explicitly. Previous audit
receipts are not imported. Within this audit, immutable completed runs may be
reused only after verifying their archive, summary and checkpoint hashes,
along with the checker and dataset hashes.

Predictions are recomputed in NumPy from checkpoint arrays using independently
written, per-order contractions. The checker does not call the producer's
prediction or factor-action methods for saved-state reconstruction. Small
analytic checks additionally reconstruct the full matrix and use PyTorch
autograd; one width-4096 full-matrix oracle checks the final P3 state separately.
Only tiny synthetic verification evolutions are run by the auditor.

For P3 at rtol 3.125e-6, the width-4096 full-matrix oracle agrees with the
factor actions to 3.55e-15 forward and 3.33e-15 for the transpose. Predictions
on 17 held-out images agree to 6.66e-16. The probe includes five independent
columns, and the matrix is reconstructed only inside this audit.

## Data and equations

The checker decodes the original IDX images and labels and verifies raw SHA256
and compressed-resource MD5 checksums. It independently reproduces the original
500-per-class selection, then the new 50-per-class parent-row selection, both
with seed 20260924 and the declared shuffle. Selected IDs and parent positions
match exactly. Every inherited validation array matches bitwise. Pixel
normalization matches the raw arrays exactly, and every image has unit
Euclidean length. Counts are 50/50 training and 1010/974 validation for 3/8.
There are no exact pixel duplicates between the selected training and
validation arrays. Official train/test indices belong to separate arrays;
matching integer IDs alone would not be a duplicate.

Frozen prepared SHA256:
`a57a903d382cbbb6d3ca79915ee6b9d371691d21d290decdf1f3f9e5e884c9a4`.

For P=1,2,3, independent initial and noninitial calculations verify the forward
and transpose actions, outer-weight velocities, Legendre moment transport,
middle-matrix derivative, defect identity and exact initial tangency. The
canonical gradients are independently differentiated from the unhalved mean
squared loss with output divided by n and mobilities (n,1,n). The largest
initial algebra discrepancy is 1.11e-15. The largest noninitial discrepancy,
including a central finite-difference derivative, is 5.90e-13. A separate
quadrature/finite-difference moving-interval oracle agrees to 1.81e-11.

A nonlinear scalar ODE independently checks the Heun continuous extension and
the loss-crossing bisection; its root-time discrepancy is explicitly separated
from finite-step integration error. Changing both validation images and labels
in tiny end-to-end runs leaves moving states, accepted step sequences,
local error ratios, training predictions and traces bitwise identical. This verifies that held-out
values do not enter numerical evolution or loss-based event decisions.

## Exact storage accounting

The direct moment state has nd+n+2nMP+P+1 float64 scalars. The dense moving state
has nd+n+n^2. For n=4096, d=784, M=100:

| Model | History scalars | Correction rank bound | Moving state MiB | Fixed W0 MiB | Moving plus fixed MiB |
|:---|---:|---:|---:|---:|---:|
| Dense | — | — | 152.531250 | 0 | 152.531250 |
| P1 | 819200 | 100 | 30.781265 | 128 | 158.781265 |
| P2 | 1638400 | 200 | 37.031273 | 128 | 165.031273 |
| P3 | 2457600 | 300 | 43.281281 | 128 | 171.281281 |

The rank bounds follow directly from at most MP outer products; they are not
measured numerical ranks. The history-coordinate storage is smaller than the
dense learned matrix by factors 20.48, 10.24 and 6.827 respectively, before
the retained W0 is counted.

The implementation also retains initialization clones. Counting unique
engine and current-state tensor storages, while excluding solver stages,
query/workspace and CPU data, gives 305.661407 MiB for dense and
196.411461, 208.911499, 221.411537 MiB for P1/P2/P3. The source-derived formulas
were checked against actual unique storage addresses on small dimensions.
These totals differ from mathematical-state storage because the dense engine
retains its initialized middle matrix as well as its current one. Measured
CUDA peaks, recorded by each scientific run, are the appropriate broader
allocation measurements. Neither count alone is a universal memory advantage.

## Saved states, numerical comparisons and reproducibility

All eight primary trajectories reached all five loss milestones, including
the selected primary training MSE .001. Across 56 saved observations, the
largest independent training-prediction discrepancy is 3.55e-15 and the
largest held-out prediction discrepancy is 6.44e-15. The largest discrepancy
between recomputed checkpoint loss and its requested milestone is 7.08e-14.
Accepted time increments, local error ratios, state dimensions, C=s+1,
retained W0, source/data hashes and canonical initialization draws pass.
Every run has the same independently regenerated initialization SHA256:
`5fc2a6ae306d63a6302b6b2c8fb7bc28b9b03f4f971bb9475f1fb195a0fe6797`.

The analysis check reproduces all 15 comparison rows, 56 label-metric rows,
exported scatter points and paired errors, loss-endpoint selection, numerical
gates and order-comparison verdicts. The maximum discrepancy in reported RMS
is 4.34e-19. Every declared numerical gate passes at every milestone and the
independent refinement-request set is empty, confirming the branch decision.
At training MSE .001 and rtol 3.125e-6:

| P | Validation RMS from dense | Own tolerance-refinement RMS |
|---:|---:|---:|
| 1 | 0.003247560410435 | 0.000003931163438 |
| 2 | 0.001084434749989 | 0.000002118397081 |
| 3 | 0.001199224207447 | 0.000001658860353 |

The dense refinement change is 0.000048104382269. All three discrepancies
satisfy the declared coarse .1 agreement criterion with the observed margins.
P3 is slightly worse than P2 at the primary endpoint: the gap
0.000114789457458 exceeds their summed observed margins 0.000099986021971.
The declared rule resolves that worsening, so these data do not support a
monotone improvement with P. Observed refinement changes remain sensitivity
diagnostics, not rigorous error bounds.

Dense and P3 were each repeated once at rtol 3.125e-6 on the other GPU.
Every saved final-state/trace/prediction/ID array is bitwise identical
(16 dense arrays and 20 P3 arrays). Every array in all five loss checkpoints
is also bitwise identical (20 dense and 40 P3 arrays, including physical
times and W0 where applicable). All matched prediction RMS differences are
exactly zero. Configuration, source hashes, initialization, data identity and
the swapped GPU assignments were checked. Reconstructing repeat predictions
again is unnecessary because both states and exported outputs are identical.

These remain single-subset, single-initialization, matched-own-loss empirical
results; no common-time tracking or width-uniform theorem follows.

Audit artifacts are under
`data/generated/neural_response_memory_20260922/mnist100_audit01/`.
The final consolidated receipt is `final02/audit.json`; full checkpoint
reproduction evidence is `reproductions.json`. `all_primary.json`,
`analysis_check.json` and `finest_p3_pair.json` preserve incremental receipts.
`retained_tensor_accounting.json` checks the implementation-storage formula.
Exact final checker commands are in `CHECKER_COMMANDS.sh`.

The first consolidation command used an overbroad directory wildcard that
also included `source_snapshots`, which has no run summary. That audit command
stopped with a missing-file error; its log and synthetic scratch remain under
`final.log` and `final/`. The corrected command explicitly discovers only
completed run-summary parents. No scientific run or artifact was changed.

Final checker SHA256:
`a0642608a43e63f2c04b7de78dc25b3fcc5812135f546bce119e22870f3cae7b`.
Checkpoint-reproduction helper SHA256:
`252ba9c6a9f7e90301de6848c791c62dabcaf509f70c1060e2f777d1af08ffdb`.
Runner SHA256:
`a5d5b0f75b2ff99651737d0fa3ac7f344f9744beeba84e2f7265593dde964df3`.
Analyzer SHA256:
`83514bfd4b0611612a85992d6f6c92705c212db492792b84b2cf3f33ed9cbdad`.
Protocol SHA256:
`94956d0202bc5d6269a4f94741a32f0c5d796b808bda96ba089cfa48c3c57d54`.
The consolidated receipt also records both engine and producer hashes; every
scientific run's recorded source hashes match those files.
