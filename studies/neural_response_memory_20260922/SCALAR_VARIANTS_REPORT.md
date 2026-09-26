# Scalar predictions: controlled comparison and terminal network decoding

2026-09-25. Internally checked research result, not promoted material.

The fixed response-basis construction produces substantially better unseen
predictions than the earlier zero-tail scalar hierarchy on this task. With
12 modes per layer at width16, its terminal decoded network differs from the
dense fitted function by circle RMS **0.016993**, with sampled maximum error
**0.031275**. The same unchanged rank at width32 gives circle RMS **0.035234**
but fails the predeclared primary-panel gate. Thus there is a useful concrete
scalar predictor and decoder, but no demonstrated width-independent accuracy
guarantee or total-memory saving.

This construction changes the approximation family. It projects dense response
dynamics onto initialization-dependent population modes; it does not validate
the original cutoff of the P-order aggregate hierarchy. Its coordinates are
weighted population averages and reduced matrix coefficients, all ordinary
scalars. No neuronwise activation evaluation or initialized n-by-n matrix
action occurs during its ODE integration.

## Contract and evidence

The experiment followed the predeclared [protocol](SCALAR_VARIANTS_PROTOCOL.md).
Use three hidden tanh layers, normalized circle inputs, no biases, width16,
seed20260920, and canonical gradient-flow mobilities (n,1,1,n). Train only at
10 and125 degrees with labels+1 and−1. Stop each candidate at its first training
MSE .001, or horizon40 if it does not fit. The actual decoded network receives
no additional training. Dense and candidate endpoints may have different times.

Primary passive angles30,60,90 are absent from training losses, normalizations,
basis selection and gradient directions. The acceptance gate is internal
training RMS sqrt(.001), passive RMS<=.05, maximum error<=.10. A valid decoder
additionally needs actual-network training RMS<=.05 and the same passive gates.
No coefficients use future dense responses. This is a single-seed development
comparison, not a statistical study.

Authoritative numerical products are
`data/generated/neural_response_memory_20260922/scalar_variants01/`:
`scores_final.json`, `validation.json`, each cell's `result.json`, saved
checkpoints, runtime tables, decoders and interpolated solutions.
`circle_predictions.npz` contains the4096-angle evaluation arrays.
The whole-circle numbers are uniform quadrature estimates, not certified
continuum supremum bounds or errors against an unknown target function.

## Complete primary comparison

All errors below compare with the width16 dense model at its own fitting
endpoint. The scalar outputs use each candidate's own fitting endpoint.

| Construction | Moving scalars | Passive RMS | Passive max | Decoder passive RMS | Decoder training RMS | Outcome |
|---|---:|---:|---:|---:|---:|---|
| Frozen boundary K3 | 92 | .160060 | .255944 | — | — | Failed accuracy |
| Tangent boundary K3 | 94 | .121094 | .161890 | — | — | Failed accuracy |
| Frozen boundary K5 | — | — | — | — | — | 50000-boundary cap |
| Tangent boundary K5 | — | — | — | — | — | 50000-boundary cap |
| Gradient-span linear potential | 2 | .172187 | .219229 | .282810 | .373243 | Failed accuracy |
| Gradient-span quadratic potential | 2 | .340086 | .454029 | .270588 | .326031 | Did not fit by T=40 |
| Curvature-span quadratic potential | 6 | .120075 | .179472 | .119679 | .232411 | Failed accuracy |
| Curvature-span cubic potential | 6 | .142480 | .229557 | .119192 | .139994 | Failed accuracy |
| Response basis, rank4 | 104 | .131691 | .220560 | .027272 | .117150 | Failed accuracy and decoded fit |
| Response basis, rank8 | 272 | .067634 | .076454 | .052914 | .030857 | Intermediate; outside gate |
| Response basis, rank12 | 504 | .032077 | .047489 | .022075 | .041847 | Passed both gates |
| Response basis, rank16 | 800 | 6.89e−9 | 1.13e−8 | 7.39e−9 | .031623 | Full-rank implementation control |

The quadratic gradient-span row is a terminal T=40 comparison, not a fitted
endpoint: its internal training RMS is .308147. All other integrated primary
candidates reached the internal fitting target. Full rank exceeds dense state
dimension and is explicitly excluded from compressed success. Rank12 is the
only genuinely reduced primary candidate passing both internal and decoder
gates, so its selection did not require a tie-break.

At60 degrees specifically, dense predicts .643160; the earlier zero-tail K5
single-point closure predicted .206443. The rank12 internal response is .669044
and its decoded network predicts .662719. Their absolute errors are .025884
and .019558, compared with the previous .436718. The old failure remains valid
for its own approximation; it was not a Fourier-only failure.

## New angles, full function and width check

The selected rank12 model was extended to passive angles0,150,210,270,330,
with unchanged basis, training coefficients and selection rule. At width16,
additional-panel internal RMS/max are .022025/.047489; decoded RMS/max are
.016204/.030353. Adding these queries changes the primary outputs by at most
3.21e−9 and training outputs by1.82e−9, consistent with solver error.

Because this bias-free tanh network is odd under input reversal,210 and270
degrees repeat30 and90 up to sign, while330 repeats150. The additional panel
therefore adds only two distinct directions modulo180 degrees. The circle
evaluation is a useful further spatial check, not4096 independent tests.

| Quantity | Width16 | Width32, unchanged rank12 |
|---|---:|---:|
| Primary internal RMS | .032077 | .070541 |
| Primary internal max | .047489 | .121700 |
| Primary decoder RMS | .022075 | .057436 |
| Primary decoder max | .030353 | .098710 |
| Additional internal RMS | .022025 | .007596 |
| Additional decoder RMS | .016204 | .006582 |
| Whole-circle decoder RMS | .016993 | .035234 |
| Whole-circle decoder sampled max | .031275 | .099102 |
| Actual decoder training RMS | .041847 | .034955 |
| Population P1 circle RMS, comparison | .018223 | .002647 |

Width32 fails the frozen primary rule even though pooling all eight passive
angles would give a smaller RMS. In particular, the internal prediction at60
is .119381 versus dense −.002319. The decoded prediction is .096391.
`scores_final.json` applies the original three-angle gate explicitly and
reports additional-panel errors separately. Earlier partial pooled summaries
are superseded by this final scoring file. No width32 rank retuning was run.

The whole circle is obtained by decoding weights once and evaluating the
ordinary fitted network at arbitrary new inputs. The4096 evaluation inputs
were never evolved by the scalar ODE. At width16 the circle decoder uses the
original three-query run; additional-query evolution is unnecessary to obtain
the whole function. At width32 the predeclared extended run is used.

![Circle comparison](../../data/generated/neural_response_memory_20260922/scalar_variants01/circle_comparison.png)

## The principled construction

Let Q_l have r columns with Q_l^T Q_l/n=I. Its columns are selected only from
initial active forward responses, backward responses, response velocities,
their quadratic products and individual cubes, together with the constant
field. Layer3 also includes the initial readout in its feature bank. A fixed
SVD rule makes ranks nested; no trained snapshots or passive samples select Q.

For a neuron field v, the coordinates a=Q_l^T v/n are weighted population
averages. Replace v by Q_l a. Nonlinear field products are evaluated through
the fixed scalar tensor

\[
T^{(l)}_{ijk}=\frac1n\sum_\nu Q_{l,\nu i}Q_{l,\nu j}Q_{l,\nu k},
\qquad (a\star_l b)_i=\sum_{jk}T^{(l)}_{ijk}a_jb_k.
\]

Retain projected initialized operators
\(C_l=Q_l^T W_{l,0}Q_{l-1}/n\). Runtime evolves modal activations for active
and passive inputs, a readout b, first-layer increment A, and middle increments
B2,B3. The forward operator in modal coordinates is C_l+B_l. Tanh gates use
\(e_l-a_l\star_l a_l\), and backward propagation uses the corresponding
transposed operators and the same projected products. The first-layer, middle
and readout velocities are canonical residual-weighted outer products in
these coordinates. Only the two active residuals enter these velocities.
Activation velocities follow the full chain rule, including both changing
weights and changing preceding activations.

This preserves nonlinear training feedback and the actual initialization's
retained correlations. It projects each elementary product/operator action;
it is not exact projection of the entire composed nonlinear vector field.
The omitted directions and failures of product closure are its approximation.

The terminal decoder is explicit:

\[
\widetilde w=w_0+Q_1A,\quad
\widetilde W_l=W_{l,0}+\frac1n Q_lB_lQ_{l-1}^T\ (l=2,3),\quad
\widetilde c=Q_3b.
\]

The initialized middle matrices are stored in the separate decoder, detached
from the runtime ODE. Decoded activations are recalculated using tanh. Internal
modal activations need not equal projections of those recalculated activations;
that consistency error is why both readouts must be measured. The decoder
readout initially projects c0, so the reduced physical network is not identical
to the original initialization. The error argument includes this initial error.

## What the theory does and does not establish

The boundary variants retain the old hierarchy. Freezing omitted factors at
their exact initialized contractions recovers initial retained velocities;
adding exact initialized residual/clock directional derivatives also recovers
initial accelerations. Algebra checks pass, but late-time omitted correlations
are uncontrolled. The K3 errors and K5 compilation caps show that these repairs
do not yet yield a small accurate witness.

The polynomial-potential variants use the exact initial output derivatives in
whitened parameter directions. Their autonomous gradient flow satisfies
\(\dot E=-\|\dot z\|^2\), and its polynomial potential is nonnegative.
Consequently \(\|z(t)-z(0)\|\le\sqrt{tE(0)}\), giving global finite-time
existence of that scalar ODE. This strong stability property does not control
its Taylor remainder or discarded parameter directions. The accurate local
jets and poor decoded fits demonstrate that distinction on this task.

The response-basis model also has an exact internal loss dissipation identity.
Tensor symmetry makes every projected multiplication operator self-adjoint.
Its backward chain is the adjoint of its forward velocity chain, giving a
changing positive semidefinite output tangent matrix. For the combined modal
parameter blocks p=(A,B2,B3,b),

\[
\dot f=-\frac2M J(z)J(z)^T(f-y),\qquad
\dot E=-\|\dot p\|^2\le0.
\]

This is an identity for the internal outputs; it does not certify the decoded
network's loss, boundedness of every auxiliary activation, or dense fidelity.
See [the detailed derivation](SCALAR_RESPONSE_BASIS_THEORY.md).

A precise finite-time comparison uses the dense polynomial response lift F,
the modal law G and its affine reconstruction Psi. Define the consistency
defect \(d(z)=F(\Psi z)-D\Psi G(z)\). If both trajectories stay in a common
region where F has Lipschitz constant Lambda, subtraction and Gronwall give

\[
\|X(t)-\Psi z(t)\|
\le e^{\Lambda t}\|X(0)-\Psi z(0)\|
+\int_0^t e^{\Lambda(t-s)}\|d(z(s))\|\,ds.
\]

This gives the same separation of error production and feedback amplification
as the earlier accumulator argument. On a bounded region, output Lipschitz
constants turn it into an observable bound. Small rank-dependent source
bounds and a common-region bootstrap are still required. Neither the
experiments nor internal loss dissipation establishes them. Full rank is exact
at fixed finite width; that fact does not prove accurate compression with rank
independent of width. No unconditional scalar rank-versus-accuracy theorem or
all-time guarantee is claimed.

## Complexity and numerical controls

For J active-plus-passive inputs, the response-basis state has
\(2r^2+(3J+3)r\) scalars. Its training core with two inputs has396 at r12;
each passive input adds36. The actual primary run has504 versus560 dense
parameters. The extended run has684, exceeding the width16 dense state, but
below the width32 dense state2144. At fixed r,J, runtime state/table dimensions
do not depend on n. Initialization and terminal decoding still depend on n.

Static product/operator tables occupy44192 bytes on the primary panel and
44272 on the extended panel, before decoder storage. These already exceed the
dense parameter arrays at both tested widths. The decoded initial matrices
and bases also need storage. This is a demonstration of scalar autonomous
dynamics with a width-independent moving dimension, not an end-to-end memory
or speed improvement. Population P1 is both smaller here (177/353 moving
states) and much more accurate at width32, but retains neuron populations.

Primary preparation/solve times in seconds are: frozen K3 2.602/.590;
tangent K3 4.272/5.061; response ranks4,8,12,16 respectively
.003/.034, .004/.054, .004/.059, .006/.117. Potential variants take
.002–.038 preparation and .009–.016 integration. Frozen/tangent K5 stop during
preparation after19.290/10.723 seconds when boundary counts reach50001.
Their peak RSS is472/391 MB; no changed resource cap or retry was used.
All phase records, including failures and refinements, sum55.859 measured
preparation/solver wall seconds; these are not instrumented CPU timings.

Module algebra checks cover exact initialized identities, no passive
feedback, scalar-table-only runtime and each family's stated exact properties.
Full rank agrees with fitted dense outputs within1.13e−8. Refining the best
completed variant in each family from rtol1e−7/atol1e−9 to1e−9/1e−11 changes
outputs by3.68e−6 at most (tangent tail); rank12 changes by4e−9. Reference
changes are below2e−9. These are much smaller than the observed model errors.
Common-time401-point trajectory comparisons are saved separately; rank12's
maximum passive discrepancy over its fitting interval is .062001, so its
terminal accuracy is not asserted uniformly over that interval.

One runner API repair before basis fits selects the module-level decoder;
it does not change a model equation. A later analysis repair applies primary
gates to the original three angles rather than diluting them with additional
angles. Original results and source hashes are preserved. The scoped audit is
[SCALAR_VARIANTS_AUDIT.md](SCALAR_VARIANTS_AUDIT.md).

## Research-state update

| Claim | Status and precise scope |
|---|---|
| Explicit scalar-only nonlinear training law with a terminal weight decoder | Exact construction; checked against full rank |
| Close width16 unseen and whole-circle predictions | Empirically supported for the selected rank12 witness and this initialization |
| Same rank passes the accuracy rule at width32 | Fails the primary rule on this witness |
| Better initialized boundary jets alone repair the original small hierarchy | Disfavored by K3; K5 accuracy inconclusive because of resource caps |
| Stable small polynomial loss implies dense prediction fidelity | Unsupported; poor fitted/decoded results despite exact dissipation |
| Arbitrarily accurate width-independent scalar compression | Open; source estimates and stability/bootstrap remain missing |
| Earlier zero-tail/Fourier scalar failures | Unchanged for those constructions |

The next mathematical bottleneck is a usable bound on discarded response
products and initialized-operator leakage along the trained path. It must
control decoder consistency as well as the internal loss. The present bounded
campaign stops after its predeclared width branch; no unreported rank, seed,
geometry or label search was performed.

## Reproduction

Run `run_scalar_variants.py --phase references --out <fresh-directory>` first,
then each primary `--phase cell --variant <name>` from the protocol. Run tree
cells in separate processes. The protocol specifies the refinements and
conditional extended/width branches. Final scoring uses
`run_scalar_variants.py --phase analyze --score-file scores_final.json --out ...`
and `analyze_scalar_variants.py --out ...`; plotting uses
`plot_scalar_variants.py --out ...` in an environment with matplotlib.
The saved config, per-cell source hashes and exact arrays determine the witness.
