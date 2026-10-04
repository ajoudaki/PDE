# Authorized reference-only split FWHT completion

Frozen 2026-10-02 before the new implementation or GPU execution. This narrow
amendment follows explicit user authorization to repair the width32768 kernel
resource ceiling. It does not reopen architecture, theorem or dataset search.
Original POPULATION_COST_PROTOCOL.md, prior producers, outputs and failure logs
remain unchanged. The scientific target, seeds8001--8032, quarter-circle law,
width32768, float32/TF32 training, dt=.02, horizon40, compact observables,
reference-resolution gates, primary tolerance and cost/bootstrap decision rules
are unchanged. All128 existing candidate trajectories and their measured costs
are reused without alteration.

For a vector x=(a,b) with each half of length16384, the normalized Sylvester
transform is H32768 x = ((S16384 a+S16384 b),
(S16384 a-S16384 b))/sqrt(32768), where S16384 is the unnormalized Sylvester
transform. Compute the first14 increasing-bit butterfly levels independently
inside the halves, and the final cross-half butterfly in a second kernel.
Apply the original normalization only at the end. The operation order, signs,
coordinate order and all surrounding mixer permutations remain unchanged.
The first kernel uses16384 lanes per program rather than32768.

A separate fast_training_split_reference.py contains the producer; original
fast_training.py is untouched. Widths other than32768 retain the original
kernel. Before any training, verify a small float32 batch against a direct
PyTorch butterfly and float64 NumPy reference, involution, explicit Hadamard
basis signs, full forward/transpose mixing with the stored sign/permutation
arrays, and the adjoint identity under IEEE matmul. Preserve the original
3e-6 action/adjoint tolerance; require relative float64-reference discrepancies
below3e-6 and exact basis-sign agreement. Verify unchanged lower-width output
bitwise. Any failed numerical/resource gate stops this branch.

Decide feasibility within10 wall minutes of15:36:04 UTC. Conditional on all
checks passing, run the original32 reference seeds on GPU1 only, stopping on
any failed oracle or resource limit. Combined verification and reference GPU
process time is capped at12 minutes; the entire branch is capped at20 wall
minutes. No replacement widths/seeds, tolerance relaxation, candidate reruns,
new baselines, broad engineering or additional experiment follows this branch.

Source validation may recognize exactly this frozen reference-only producer
and amendment in addition to the original accepted candidate source pairs.
Validate complete artifacts and both predeclared reference-resolution gates
before evaluating accuracy-cost comparisons. A failed resolution gate blocks
that calculation in this amendment. Reference runtimes are reported as campaign
overhead, never used as candidate cost or as an optimized-kernel speed claim.
The kernel dispatch difference is disclosed even though its real-arithmetic
operator and floating-point butterfly order are unchanged. A pass is supporting
finite numerical population evidence only; no broad architectural conclusion
or promotion follows.
