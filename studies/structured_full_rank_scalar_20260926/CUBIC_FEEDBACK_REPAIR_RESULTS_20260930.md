# Locating and repairing the large scalar-response errors

2026-09-30. Continuation of the user's requested small-state feedback
repair. These are internally checked experimental results and exact
identities of the specified surrogate models, not promoted theory or a
new approximation theorem for strong-label neural training.

## Main finding

The large errors are not a numerical clock problem. Two substantive
approximations fail together: a low-order feature expansion leaves the
bounded tanh regime, and the positive completion of the training kernel
is extended to unseen inputs using the **initial** kernel. That extension
accumulates a large passive-output correction. Removing the completion
helps but does not repair the trajectories. Self-consistent readout
feedback and bounded feature-Gram evolution help further.

The best single construction across the two hard cases is the bounded
moving-Gram model: circle RMS errors fall from **1.20563 to 0.24026** and
**1.33777 to 0.25268**. The smooth-label control improves from 0.04256 to
0.01008. This is a substantial partial repair, **not a satisfactory fix**:
the predeclared practical target was 0.05 on both hard cases.

The training state remains quadratic in sample count. However, this best
model evolves m+1 passive scalars per queried input; its full 256-point
test panel is not an O(m²)-state decoder of the entire circle. This cost
is reported explicitly below. It must not be presented as solving the
user's stronger compact arbitrary-input-decoder requirement.

## Comparison and safeguards

All primary comparisons use the same dense Gaussian initialization,
width n=1024, seed 1, tanh, canonical mobilities (n,1,n), and the same
labels. The scalar models start at zero readout; the canonical dense
readout is tiny rather than exactly zero. Previous direct checks put
that difference at 1.22e-5 on the checked pair. No block replacement,
Fourier approximation, test-label fitting, target-trajectory forcing,
histogram, or neuron ensemble is introduced in the scalar RHS.

Every reported fitted model stops at its own first training **MSE 0.001**
crossing. This is RMSE approximately 0.03162, not RMSE 0.001. The primary
metric is the raw RMS of scalar minus dense output over 256 equally spaced
circle angles. The dense endpoints are reused and replay-verified; no
new dense training was needed. Different stopping times mean this is a
fitted-function comparison, not a common-physical-time error bound.

The focus tasks are a close opposite-label pair, an oscillating three-point
cluster, and the same clustered inputs with smooth labels. The latter
separates input conditioning from the need for strong feature learning.
Protocols were frozen before each candidate's training; the fourth round
is explicitly disclosed as an extension of the three-round stopping rule.
All adverse results are retained. No coefficients were tuned to test error.

## What is demonstrably wrong in the old closure

Let K0 be the initial training Gram, and M,N the old evolving response
contractions. The old tangent kernel is

    Theta = K0 + M + M.T + N + Q,   Q = M.T K0^-1 M.

Q ensures positivity. Training consistency then adds to the cubic test
decoder the initial-kernel interpolation

    k0(x,train) K0^-1 Delta,   Delta' = -(2/m) Q r.

These identities can be checked directly in the implemented equations.
The RMS size of that extra test correction is **1.0994 / 1.2684** on the
two hard cases. It is not harmless merely because Q is positive. Deleting
it only from the final decoder breaks agreement with the model's own
training outputs. Removing Q from the dynamics and consistently rebuilding
the decoder instead lowers error to **0.7277 / 0.7066**: substantial, but
still much too large.

The upstream response approximation is also outside its small-motion
regime. Its reconstructed second-order hidden features exceed tanh's
[-1,1] range on **34.72% / 39.86%** of the circle-neuron entries. For the
hard cluster, the actual dense lower-layer tangent response in the weakest
initial Gram direction is 0.33219, versus 0.02812 in the scalar response
term—almost a factor twelve. The scalar positive completion contributes
0.14681 in that direction, compensating in a different manner and with a
different test extension.

An additional exact diagnostic is the readout energy q=mean(c²). Any
canonical tanh trajectory satisfies

    q' = -(4/m) r.T f,       |f(x)|² <= q.

For the near pair, the old scalar trajectory implies q=5.4503, while its
largest test output is 2.9515, greater than sqrt(q). Thus its output cannot
simultaneously have bounded tanh features and the canonical readout energy
implied by its own training trajectory. This is a structural inconsistency,
not a loss-stopping discrepancy. The cluster passes this necessary bound
despite its large error, so energy alone is insufficient.

Endpoint diagnostic evidence does not isolate the first physical time of
failure or give an additive causal decomposition. The dynamical ablations
below are the stronger evidence about possible repairs. See the complete
[diagnostic](CUBIC_DENSE_DIAGNOSTIC_20260930.md) for all values and limits.

## Repairs tested with small state

Each entry is circle RMS versus the same fitted dense reference.

| Model | Close pair | Oscillating cluster | Smooth cluster |
|---|---:|---:|---:|
| Original cubic closure |1.205628|1.337774|0.042561|
| Remove positive completion consistently |0.727692|0.706588|0.045579|
| Self-consistent bilinear feedback, cubic query restoration |0.462366|1.069132|0.042139|
| Moving Gram and energy, no saturation gate |0.304873|0.450843|0.025668|
| **Moving Gram, energy, saturation gate** |**0.240264**|**0.252676**|**0.010079**|
| Explicit initial/current overlap, gated |0.170062|0.935008|0.020882|
| Overlap plus one derived readout-response direction, gated |0.123898|0.476534|0.022301|
| Same extra direction, ungated |0.395375|0.406725|0.047380|

The gate is (1-Kaa)/(1-K0aa), motivated by tanh'=1-h² and initialized to
one. It changes feedback inside the ODE; it does not clip outputs. Its
replacement of neuronwise derivative correlations by aggregate factors is
still a closure approximation, not an exact identity of dense training.
The ungated comparison isolates its contribution. An extra mode helps
some cases, but simply adding another response direction does not fix the
hard cluster. The mode is derived from the initial kernel and labels,
never from the fitted dense function.

The bounded-Gram construction evolves r and the upper triangle of K:
m+m(m+1)/2 training states. Its exact surrogate identities ensure positive
training kernel, nonincreasing loss, bounded Gram diagonals, the readout
energy identity, and vanishing dynamics at zero residual. It is globally
well posed at finite times under the stated positive initial Gram. These
properties establish a coherent stable model; **they do not bound its
distance from the dense network**. The full equations, proof, and remaining
arbitrary-query cubic defect appear in
[the construction](CUBIC_ENERGY_REPAIR_ROUTE_20260930.md).

## Transfer across all nine tasks

The same bounded-Gram model, with no per-task tuning, passed the frozen
factor-three improvement gate on both hard cases and was therefore tested
on the six remaining tasks.

| Task | Original RMS | Bounded-Gram RMS | Training states | Total states with passive panel |
|---|---:|---:|---:|---:|
| pair_cos3 |0.121253|0.057493|5|779|
| pair_orthogonal_cos1 |0.045205|0.009672|5|779|
| near_pair_sin9 |1.205628|0.240264|5|779|
| cluster_triple_cos9 |1.337774|0.252676|9|1045|
| cluster_triple_cos1 |0.042561|0.010079|9|1045|
| triple_wide_mixed |0.007535|0.003085|9|1045|
| quartet_mixed |0.039916|0.050157|14|1314|
| broad_ridge6 |0.043183|0.019216|27|1861|
| alternating3 |0.089800|0.052033|9|1057|

Eight of nine improve; quartet_mixed slightly worsens. All reach the same
training target. Alternating3 has six original inputs but three effective
ones after the exact odd-symmetry reduction; all original training aliases
are included in the passive panel. Dynamic counts include 256 circle
queries and the original training aliases. Static training coefficients
cost O(m^4); each passive query requires O(m^3) static coefficients and
m+1 evolving scalars. Initialization contracts width-dependent arrays.
The experimental runner also retains initial arrays in outer locals;
only its scalar model RHS/state is width independent.

The nine bounded-Gram integrations took about 4.71 seconds in total with
one BLAS thread; the slowest was the hard cluster, 2.62 seconds. Tighter
solver tolerances on the three focus tasks changed circle predictions by
at most 5.21e-9 RMS. Nested 128/256-point RMS estimates differ by at most
1.01e-5 on this panel. Training aliases and positive-Gram/energy bounds
passed their numerical checks. These are numerical consistency checks,
not certified error bars or a continuum-input convergence theorem.

## What remains unresolved

Training loss obeys r'=-(2/m) Theta_train r, whereas an unseen output
obeys f'(x)=-(2/m) Theta(x,train) r. Positivity of Theta_train can make
training stable and successful while the **cross** kernel remains wrong.
Stopping correctly at zero residual freezes that already wrong function.
This explains why terminal stability, though necessary for a good closure,
does not repair the strong-learning approximation by itself.

The evidence identifies specific faulty feedback/projection steps and
shows that a few coherent aggregate changes can substantially reduce
their damage. It does not prove that one further scalar will suffice,
that all scalar compression is impossible, or that this collection of
surrogates is a convergent hierarchy. The remaining missing information
includes correlations of activation gates, current backward responses,
and feature directions; retaining only their separate means or norms does
not determine the required contractions.

## Reproduction and artifacts

All generated products live under
`data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/`.
The ablation, round2, round2_transfer, round3, round3_mode and numerical-check
subdirectories retain per-run JSON, arrays, hashes, and commands. Sources
for earlier evolving drivers were snapshotted. The diagnostic and geometric
decoder subdirectories contain no new training. The bounded-model result
audit is [recorded separately](CUBIC_BOUNDED_REPAIR_RESULT_AUDIT_20260930.md).
That audit found two transitive imports missing from the round2 source
snapshot. A labeled posthoc `provenance_supplement/` preserves them; both
hashes agree with the preceding original-cubic run's manifest. It is not
misrepresented as a contemporaneous round2 snapshot.

The driver refuses to overwrite an existing output directory. For example,
from the repository root, use a **fresh** output name:

```sh
python studies/structured_full_rank_scalar_20260926/run_cubic_feedback_repair.py \
  --methods bounded --tasks near_pair_sin9 cluster_triple_cos9 cluster_triple_cos1 \
  --output fresh_reproduction
```

The exact-curvature extension and its result are recorded below. Its source
and coefficient arrays are saved separately from all the earlier models.

## Exact curvature test: a useful negative result

The final extension adds the exact initial hidden-feature Hessian, including
both tanh curvature terms and the mixed change of the first and middle
weights. For fixed initial response directions and scalar displacement eta,
the feature/readout contraction is A+L eta+eta.T H eta/2. Its readout and
hidden scalar coordinates follow the exact gradient flow of this surrogate's
loss. This adds **no dynamic states**: 6/12 for the two-/three-input base
models and 9/16 with the previously derived extra readout-response mode.
No query ODE states are required. Static coefficients are more expensive,
O(m^6) for training and O(m^5) per query; this is not a cost-free term.

Both versions passed direct mixed-Hessian finite differences and exact
gradient/energy/kernel identities before any training. All six fits reached
MSE 0.001. No positive eigenvalues were discarded on this panel.

| Model | Close pair RMS | Oscillating cluster RMS | Smooth cluster RMS |
|---|---:|---:|---:|
| Exact quadratic features, base directions |0.742543|0.401269|0.025694|
| Same, one additional response direction |0.807132|0.651542|0.024531|

Neither passes the joint factor-three improvement gate. No transfer panel
or higher-degree sweep was triggered. Construction took 0.43–0.63 seconds
per case; integrations took 0.020–0.140 seconds. These timing figures
exclude the separate diagnostic below.

There is a sharper way to identify the failed approximation. Reconstruct
the actual weights represented by the scalar endpoint, then evaluate the
**exact tanh** network at those same weights. This diagnostic changes
neither the directions nor the state; it isolates the polynomial feature
map from the actual nonlinear map at that state. It uses width-dependent
arrays only for checking and is not a proposed scalar decoder or a new fit.

| Base quadratic model | Scalar training MSE | Exact-tanh training MSE at same lifted weights | Circle RMS, surrogate minus exact lift |
|---|---:|---:|---:|
| Close pair |0.001|0.490538|0.486820|
| Oscillating cluster |0.001|1.472212|1.248500|
| Smooth cluster |0.001|0.000211|0.018174|

The added-mode version has the same qualitative mismatch: exact-lift MSE
0.5494 / 0.9337 on the hard cases, versus 0.000195 on the smooth control.
This is direct evidence that the finite Taylor feature map has become a
bad representation at the hard scalar endpoints. Adding its exact next
curvature term does not keep training inside a regime where that expansion
is reliable. It does **not** prove that fixed-direction restriction is the
sole problem or that a different small nonlinear aggregate closure cannot
work. It also does not allocate all dense trajectory error to the Taylor
map: the surrogate followed its own different training path.

Full derivation and cost:
[quadratic-feature route](CUBIC_QUADRATIC_FEATURE_ROUTE_20260930.md).
Code: [model](cubic_quadratic_feature_repair.py),
[frozen experiment driver](run_cubic_quadratic_repair.py).
[Saved-result audit](CUBIC_QUADRATIC_RESULT_AUDIT_20260930.md) replays
the contractions, fingerprints, and diagnostic without training.

## The remaining correlation cannot be inferred from a norm alone

One exact dense identity makes the residual approximation concrete.
For a training input a, let h2_a be its second-layer activation, h1_a its
first-layer activation, and c the readout. The middle-weight contribution
to its tangent-kernel diagonal is

    <h1_a²> <c² (1-h2_a²)²>
      = <h1_a²> [<c²> - 2<c² h2_a²> + <c² h2_a^4>].

Here brackets are neuron averages in the appropriate layer. The readout
energy and feature Gram diagonal alone do not determine the two weighted
correlations on the right. Off-diagonal kernels need corresponding joint
correlations between inputs. These are precisely the kinds of correlations
that mean-gate factorization can lose as training concentrates backward
signal on a changing set of neurons.

This identifies a concrete next mathematical obligation, not a completed
two-term closure: differentiating those weighted correlations introduces
additional quantities, so merely naming them does not give an autonomous
or accurate O(m²) model. No claim is made that storing just these two
families would fix the remaining error. The experiments justify rejecting
the old positivity/interpolation shortcut and naive extra Taylor order;
they do not yet settle that correlation-closure problem.

![Saved fitted-function comparison](../../data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/feedback_repair_functions.png)

All dynamic candidate metrics are exported to
`cubic_feedback_repair_20260930/all_dynamic_repairs.csv`. No further
experiments are queued at the end of this bounded investigation.
