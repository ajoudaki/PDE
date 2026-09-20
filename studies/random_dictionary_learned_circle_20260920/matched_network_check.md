# Matched-network independent checks

## Deterministic launch preflight — PASS

Scope: the frozen `MATCHED_NETWORK_PROTOCOL.md`,
`matched_network_benchmark.py`, explicitly assigned dictionary/trajectory
sources, and their maintained implementation dependencies. No other study
or other agent's analysis was used. This is a scoped internal method check,
not an independent promotion review. No training trajectory was run.

Command:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/matched_network_check.py --device cuda:1 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_preflight01
```

The CUDA float64 preflight completed in 1.5105106458 seconds on the assigned
device. Machine-readable checks, exact command/environment, and the complete
checked source-hash map are in
`data/generated/random_dictionary_learned_circle_20260920/matched_network_preflight01/preflight.json`.
Source hashes were identical before and after the checks. The frozen producer
hash is `9e938bda173dc9747d0fb9fc33fb289a85a9bcddaad2b038784b29c38e026482`;
the protocol hash is
`5d16c1683d03b58eba45817e55358acf1738433bd785c017605dd470392b84fd`.
The exact original checker source was preserved before adding the raw replay
mode as `matched_network_preflight01/checked_source.py` in the same generated
directory. Its SHA256 matches the checker hash recorded by the preflight:
`f825893647936d5d89f58e3d280e0a568a8f9df94c3d36f9d5ebc4b942e322b1`.

Thirteen grouped checks passed: three count tables, six actual small-network
widths, three dictionary orders, and one full-basis equivalence check.

- Independently fixed parameter counts and smallest covering widths agree:
  trainable matches 55, 58, 75 and total-size matches 105, 221, 397. Every
  preceding width falls below its declared budget.
- All six coupled initializations equal the prescribed scaled prefixes
  exactly; arrays are independent owned copies; both initial hidden-motion
  diagnostics are exactly zero.
- For every actual smaller width, predictions, unhalved weighted loss, and
  all three physical-flow blocks agree with independent automatic
  differentiation of a separately written network formula. The test uses
  nonuniform positive sample weights and a fixed, nondegenerate parameter
  perturbation without integrating any flow. The largest absolute residual
  was 6.8174632606e-16. It verifies width-specific output normalization and
  mobilities, rather than only the tiny initialization gradients.
- All three dictionary orders agree with independently enumerated
  Chebyshev powers evaluated by `cos(k acos(x))`, including the two redundant
  p5 constant tails. Reconstructed regularized Cholesky factors satisfy the
  triangular identity; the largest absolute residual is 1.3011813849e-13.
  The largest regularized Gram condition is 114876.6531, below 1e10.
  Independently associated initialized middle-action contractions agree to
  2.5535129566e-15. Initial closure hidden-motion diagnostics are zero.
- With complete scaled coordinate bases at width 11, the closure and dense
  network agree in predictions and every RHS block at a nondegenerate
  perturbed state. The largest absolute residual is 9.7144514655e-17.

No launch-blocking implementation or protocol inconsistency was found.
These algebraic checks do not establish numerical convergence of later
training trajectories, successful fitting, or either model's superiority.
Saved trajectories require a separate raw replay and refinement check.

After adding the independent replay mode, the unchanged preflight branch
was rerun on the released CUDA device. `matched_network_preflight02/preflight.json`
records PASS for all thirteen groups in 0.9565104842 seconds and freezes the
extended checker source. This second check also ran no training trajectory;
the producer and protocol hashes are unchanged.

## Counting and comparison interpretation

The two budgets are different scientific controls. The trainable budget is
`3n + K1*K2`; minimal retained model storage is
`n*(K1+K2) + 3n + K1*K2`. The latter excludes duplicate caches, diagnostic
initial copies, implicit uniform quadrature weights, and construction/solver
workspace. It is not actual engine retained memory. Keeping redundant p5
columns in both budgets follows the frozen protocol; no numerical rank
threshold silently reduces the budget.

Fixed prefix coupling preserves the exact canonical Gaussian marginal law
at each small width, without selecting outcomes. It does not equate initial
functions or equalize the full initialization information retained by the
dictionary and the small network. The producer correctly installs the
coupled origin in each fresh engine before observing hidden displacement.
Each network uses its own width in physical-flow normalization.

## Independent saved-trajectory replay

PASS for all 40 base trajectories from `matched_network_primary01` and
`matched_network_refined01`. Every trajectory is fitted. The independent
checker ran on the released `cuda:0` device, without importing the analyzer
or reading its results, and finished in 4.4798512757 seconds. Its complete
frozen record is
`data/generated/random_dictionary_learned_circle_20260920/matched_network_independent01/independent.json`.

Command:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/random_dictionary_learned_circle_20260920/matched_network_check.py --device cuda:0 --out data/generated/random_dictionary_learned_circle_20260920/matched_network_independent01 --runs data/generated/random_dictionary_learned_circle_20260920/matched_network_primary01 data/generated/random_dictionary_learned_circle_20260920/matched_network_refined01
```

The final checker SHA256, matching `matched_network_preflight02`, is
`238050370a0a2d9916bff8ec2c1f92a6245c69d5e57c7354a1fe9fe08df01c37`.
The replay verifies source/protocol hashes and fixed configuration fields;
records hashes of configuration, completion, summary and raw checkpoint
files; checks every state's finiteness and shapes; recounts model/trainable
parameters and actual engine bytes; verifies exact initialization coupling;
independently reconstructs dictionary algebra; and verifies both evaluation
grids and training inputs/labels.

Direct formulas independently replay every saved circle snapshot, every
endpoint, and initial/final training losses. The largest absolute snapshot
prediction difference is 6.8833827527e-15 and the largest endpoint difference
is 8.1046280798e-15, against the declared absolute tolerance 1e-10. Trace
lengths/times, accepted step bounds, local-error acceptance, loss monotonicity,
and the first recorded threshold crossing also pass. These are saved-state
and solver-record checks, not a rigorous exact-flow error certificate.

All 20 case/model refinement checks pass. The largest sampled endpoint
change between numerical levels is 0.0038649122, below 0.01. No extra
resolution trajectory is eligible under the frozen protocol. The largest
8192-versus-nested-4096 RMS change is 4.4408920985e-16; the largest sampled
maximum change is 7.7610023886e-6. The four completed training workers used
496.1704935804 summed seconds; replay time is separate and contains no
training trajectory.

Refined-level circle RMS discrepancy from the fitted full-network endpoint:

| Case | p | Ours | Small: trainable match | Small: total-size match |
|---|---:|---:|---:|---:|
| quadrant_alternating | 1 | 2.21164510 | 0.14244771 | 0.19867117 |
| quadrant_alternating | 3 | 1.29655808 | 0.08577603 | 0.08339533 |
| quadrant_alternating | 5 | 0.82847057 | 0.42220335 | 0.03036053 |
| two_outliers_alternating | 1 | 1.06862455 | 0.10604294 | 0.03042664 |
| two_outliers_alternating | 3 | 0.44508125 | 0.10383443 | 0.05515419 |
| two_outliers_alternating | 5 | 0.41735774 | 0.24295390 | 0.02676815 |

All twelve comparisons favor the smaller exact network at both selected
numerical levels, with every declared validity gate passing. This is the
result for the two fixed geometries and one coupled initialization. It does
not establish a universal ordering, a capacity theorem, or an asymptotic
rate. Increasing dictionary order improves the closure's RMS discrepancy in
these cases, but does not overtake either matched comparator here.

The integer rule rounds upward for both budgets, giving each smaller-network
comparator slightly more parameters than its matched budget. The trainable
comparison uses widths 55, 58, 75; the total-size comparison uses 105, 221,
397. Both retain the predetermined prefix coupling, with no seed/neuron
selection or time rescaling. These caveats accompany the finite comparison;
the result is not a capacity lower bound for either model family.

After freezing the independent result, an explicitly authorized comparison
against `matched_network_analysis01` passed. The agreement record is
`matched_network_independent01/agreementcheck.json`. All 36 model/level
metric records agree: 288 scalar comparisons across both circle grids have
maximum absolute difference 1.7763568394e-15. All 20 endpoint selections and
refinement gates agree, with maximum refinement discrepancy difference
2.7478019859e-15. All twelve valid comparison verdicts agree. The agreement
record hashes both independently completed output sets and uses absolute
tolerance 1e-12; it does not replace the earlier raw replay.
