# Discriminate full-spectrum and singular-basis effects

Frozen before either extra condition is implemented or trained. Existing
quarter-circle confirmation is positive, but the independent Gaussian return
energy sees the fourth singular moment and is completely blind to the right
orthogonal basis. Neither a positive return check nor a fast implementation
therefore demonstrates preservation of learned dynamics. The audit identified
these specific competing explanations; this test does not seek better labels
or a better task score.

Keep the exact confirmation data, q=1 equations, width8192, physicalT40,
dt=.02, IEEE float32, seeds7501--7505. Add precisely two mixer conditions:

- Two-point: half the singular values0 and half sqrt(2), using the same fast
  signed/permuted Hadamard bases. Mean square1 and fourth moment2 match the
  Gaussian law; sixth moment4 differs from its value5. This is not a full-rank
  Gaussian model. Its purpose is to falsify a fourth-moment-only explanation.
- Unmixed right basis: retain the quarter-circle singular array and all signs
  and permutations, but remove ONLY the right Hadamard factor. Its singular
  spectrum and left covariance are unchanged. The expected independent
  Gaussian-probe return energy is therefore exactly unchanged, but adaptive
  coordinatewise learning need not be. This is a diagnostic, not a competitive
  architectural baseline.

No added arm reads Gaussian trajectories during training. Use the same five
aggregate metrics defined before confirmation. Save initial first/second-layer
Grams as well as full recorded Gram trajectories; report initial ensemble
discrepancies separately, so an initial forward mismatch cannot be hidden.

Each explanation is challenged if its extra arm's prediction AND second-layer
Gram distances exceed twice the quarter-circle distances, with the ordering
remaining true after omission of any one of the five paired seeds. Otherwise
call the discriminator inconclusive; do not increase width, horizon or choose
a favorable metric. This is an empirical distinction on one data task, not a
universality theorem or a novel statement about all singular-basis laws.

At most10 trained trajectories,5GPU-process minutes, oneGPU; no new fit after
a negative outcome. Width128 explicit-matrix and adjoint checks first, maximum
relative error3e-6. If these scientific comparisons are later called internally
reproduced, repeat their exact10 trajectories in a fresh directory (separate
verification allowance, no new statisticalreplicates). No tuning campaign,
trained Fastfood/ACDC benchmark or classification-advantage claim follows.
