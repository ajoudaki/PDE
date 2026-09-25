# Orders five and six: width2048 eight-input comparison

Increasing this scalar truncation from order4 to orders5/6 does not produce
a reliable further improvement in the tested learned circle function.
Order5 fits all eight labels but is worse on the first seed. Its small apparent
gain on the second seed is numerically unqualified. Order6 develops loss growth
and solver failure on both seeds, so there is no matched-loss test endpoint.
This is evidence about this frozen-terminal hierarchy, not all aggregate
closures or a theorem that every higher order must fail.

## Fixed comparison

Use the same bias-free three-hidden-layer tanh dense network, all layers of
width2048, the same NumPy parameter draws and physical mobilities(n,1,1,n),
and the eight alternating labels at circle angles10,...,80 degrees. Dense
references were trained on GPU and audited in SCALAR_WIDE_RESULTS.md.
The new initialized tensors throughT6 were computed on GPU1 in float64.
The subsequent scalar ODEs use no neuron populations or dense matrices.

Every reported fitted test function is taken at its own first detected
training MSE1e-6 crossing. Test inputs never feed back into training.

| Order | Seed20260920: circle RMS | Seed20260927: circle RMS | Training outcome |
|---:|---:|---:|---|
|2|160.44930|193.55456|Both fit, analytic spectral flow|
|4|39.27422|63.81087|Both fit|
|5|40.63438|63.35941, diagnostic only|Both fit|
|6|No matched endpoint|No matched endpoint|Loss growth, then solver failure|

Order5/order4 error ratios are1.03463 and0.992925. Thus the first seed is3.46%
worse; the second nominal change is only0.71% better, below the frozen1%
resolved-improvement margin even before its failed consistency gate.
The previous order2-to-order4 improvements of4.09x and3.03x do not continue
as a comparable gain here. No monotone-convergence conclusion follows from
any finite list of orders.

There is also an exact reason to distinguish odd and even orders. Under
readout sign reversal, Tp(W,-c)=(-1)^p Tp(W,c). At exactly c=0, T5=0, so
freezing it makes the entire order5 closure reduce to order4, including
passive outputs. The actual small nonzero readouts give T5/T4 entry-RMS
ratios about1.40e-4/1.29e-4. This identifies a structural near-degeneracy
at initialization; it is not a long-time error bound or an explanation of
order6 instability. SCALAR_HIGH_ORDER_PARITY.md contains the full proof,
scope, descriptive norms and artifact hashes.

## Numerical qualification and limits

Primary order5 rtol1e-7/1e-9 endpoint differences were .003267/.005446 RMS,
above the .002 threshold. The predeclared single rtol1e-11 refinement was
therefore run for both seeds. Comparing the latest two resolutions gives
.000520824/.00125141 RMS changes and acceptable fitting-time changes.

The passive-training consistency check has a separate1e-4 RMS threshold.
Its latest peak values are8.64443e-5 and1.63211e-4. The first passes; the
second fails. Therefore the second seed's order5 circle value remains a
diagnostic, despite fitted training state and small grid-refinement change.
No extra unregistered refinement or alteration of the closure is made.

Direct1024-point circle discrepancy and the optional Fourier representation
are different claims. Both nested512/1024 quadrature gates pass. Both order5
Fourier encodings fail the strict RMS1e-5 gate at modes64,128 and256; at256,
off-grid RMS errors are1.684e-5 and3.898e-5. Thus the first direct-grid
comparison is qualified while the complete encoded-function claim remains
unresolved. This encoding limitation does not invalidate its direct-grid
disagreement or manufacture a missing order6 fitted endpoint.

Fresh first-seed training and passive coefficients were regenerated from
the original parameters, and both orders were integrated again. Order5 uses
the selected rtol1e-11 and order6 repeats rtol1e-9. Coefficients, order5
training/circle endpoints and the order6 failed trajectory reproduce bit
for bit. Reproducing a numerical failure does not qualify its terminal
state as an accurate solution. The reproducibility and saved-data receipts
are recorded in SCALAR_HIGH_ORDER_AUDIT.md; internal checking remains
separate from promotion.

The nine initializer tests pass on GPU, nine generic-engine tests pass,
and the runner passes a separate exactly solvable fitting/readout test.
The independent combined audit passes3,671 checks covering original
coefficients, frozen sources, all twelve research integrations, seven
passive replays, endpoint scoring and reproduction. An audit PASS means
the stated failures and limitations were reported correctly; it does not
turn a failed accuracy or numerical-validity gate into a success.

## What makes order six fail in these runs

For residual r=f-y and L=||r||^2/M, the scalar equations give exactly

    L' = -4 r^T Theta r / M^2,
    L'/L = -(4/M) rho,  rho = r^T Theta r / (r^T r).

The canonical dense Theta is a positive semidefinite gradient Gram matrix.
Freezing a higher derivative tensor does not preserve that constraint on
the evolving scalar Theta. Negative rho then makes the loss increase.
This is a structural issue of the truncated equations, separate from the
long physical fitting times handled by the implicit solver.

Negative rates are observed well before terminal solver failure and agree
across the two tolerances. Examples from archived segment boundaries are
t≈850.768,L≈.680936,rho≈-.00451641 on the first seed and
t≈226.357,L≈.839507,rho≈-.00560923 on the second. These are first saved
negative-rate boundaries, not a claim of continuous monotone growth from
then onward. The minimum sampled fine losses are .47346 and .80117.

Fine order6 runs stop near physical times1629.85790 and318.604784, after
large loss growth, when BDF requires a step smaller than floating-point
time spacing. Failure times are close across tolerances, but terminal
losses differ by orders of magnitude. Those terminal states are not
numerically converged endpoints. The evidence supports reproducible loss
growth and computational failure of this candidate under these controls,
not a proved finite-time singularity or permanent nonfitting theorem.

## Computation and scalar size

The highest training tensors were initialized in about25 GPU seconds per
seed. The32-query order6 feasibility pilot took41 seconds and about5.84GiB
of GPU allocation, below its12GiB cap. Since order6 did not fit, its full
circle coefficients were not computed. Original order5 circle coefficients
took about54 GPU seconds per seed, using exact antipodal oddness for passive
queries and retaining all eight training directions.

The recorded active-work subtotal is579.50 seconds, well below the10800-second
budget. It sums concurrent CPU/GPU work, not elapsed campaign time; standalone
process startup, source-copy and scoring overhead are not fully recorded.
Peak allocated GPU memory is5.838GiB and peak process RSS is.999GiB.

The selected order5 integrations took22.41/27.11 CPU seconds, followed by
8.26/10.88 seconds of scalar passive replay. Dense reference integrations
took26.92/29.25 GPU seconds. These timings use different hardware and omit
shared initialization from integration costs; they are not an accuracy-matched
speedup claim. Physical order5 fitting times are47273.90 and46088.04.

Order5 has4680 moving training scalars,4680 local signature scalars and32768
fixed terminal entries. Order6 has37448+37448 moving scalars and262144 fixed
terminal entries. Passive coefficients add input-dependent storage. These
are width-independent scalar tensors; their cost grows rapidly with sample
count and closure order. The width2048 dense model has8,394,752 moving parameters.

## Retained implementation and reproduction

SCALAR_HIGH_ORDER_PROTOCOL.md is the frozen experiment design.
SCALAR_HIGH_ORDER_INITIALIZATION.md proves the ordered-word initialization
recursion and independent multijet oracle. SCALAR_HIGH_ORDER_ENGINE.md
derives the exact8-by-8 Schur elimination used by BDF and the passive transport.
run_scalar_high_order.py performs initialization, scalar integration and
readout; launch_scalar_high_order.py sequences the primary scalar runs.
analyze_scalar_high_order.py recomputes scores and figures from saved data.

Generated data under data/generated/neural_response_memory_20260922/:

- scalar_high_order_training01: both original fullT1..T6 training tensors.
- scalar_high_order_pilot01: bounded32-query feasibility evidence.
- scalar_high_order_primary01: all primary/refinement trajectories and readouts.
- scalar_high_order_probes01: original order5 passive tensors and exact query rows.
- scalar_high_order_training_reproduction01, scalar_high_order_probes_reproduction01,
  scalar_high_order_reproduction01: fresh first-seed repetition.
- scalar_high_order_analysis01: endpoint table, numerical gates and scientific figures.
- scalar_high_order_audit* receipts: independent algebra, saved-state and kernel checks.

All source snapshots, input/output hashes, commands, device/precision settings
and actual caps are retained. No maintained-source, promotion or Git-index
change is part of this continuation.
