# Historical response memories as a repair instrument

The useful result is qualified. Four Legendre modes recover the recorded
hidden-matrix writes of two corrupted samples accurately enough to reproduce
an exact-history repair. After an equal amount of clean training, repair
improves evaluation MSE in all five fresh initializations, with24.64% median
reduction. Only four meet the original10% practical-effect threshold. Giving
ordinary cleanup25% more training time removes the advantage in two cases.
This is evidence for a diagnostic/editing instrument, not a competitive
unlearning algorithm or an independently confirmed broad repair method.

## Exact object and intervention

Use the canonical two-hidden-layer tanh dense flow in MODEL_RECONCILIATION.md,
with m=12 normalized circle rows at angles2pi*a/12+.13. The target is
sin(theta)+.5sin(3theta). Reverse labels at indices1 and7, an antipodal pair.
The data remain consistent with network oddness. All initializations have
zero readout and canonical Gaussian hidden weights. Train to T=32 with Euler
step1/64. Pilots use n128/seeds101--103; confirmations n256/seeds201--205.
Evaluation is the fixed512-point interlaced circle grid with the clean teacher.

For sample a at Euler step i, let h_(a,i) be its first hidden feature,
delta_(a,i) its residual-free second-layer response, r_(a,i) its residual,
and rho_i the RMS residual. The exact recorded matrix write is

\[
\Delta W_a=-\frac{2\eta}{mn}\sum_i
r_{a,i}\delta_{a,i}h_{a,i}^{\top},\qquad
W^{(2)}_T-W^{(2)}_0=\sum_a\Delta W_a.
\]

For positive activity interval length S=sum_i eta*rho_i, regard h_a and
b_a=r_a delta_a/rho as piecewise constant on intervals of mass eta*rho_i.
Set b_a=0 when rho_i=0; such intervals have zero activity mass and zero write.
Let p_j(xi)=sqrt((2j+1)/S) P_j(2xi/S-1) be the orthonormal Legendre functions
on[0,S]. Define H_(a,j)=integral h_a p_j and D_(a,j)=integral b_a p_j. Then

\[
\Delta W_a^{(q)}=-\frac2{mn}\sum_{j=0}^{q-1}D_{a,j}H_{a,j}^{\top}.
\]

This follows by pairing the orthogonal projections of the two histories;
it is not a finite-q equality for arbitrary histories. The complete integral
equals the discrete write exactly. The artificial initialization prefix is
excluded: these are **observer moments of the actual dense trajectory**, not
the autonomous closure's prefix-including state. No dense history is fed into
an autonomous learner or used to claim autonomous approximation accuracy.

For q<=8, moments can be accumulated online without recording the trajectory.
For degree k, store J_k=integral_0^S h(xi)(xi/S)^k dxi and its b counterpart.
On appending a constant interval of mass deltaS, put alpha=S/(S+deltaS).
Changing the old normalized coordinate gives alpha^k J_k; integrating the new
constant interval gives h(S+deltaS)(1-alpha^(k+1))/(k+1). Their sum is the new
J_k. Expanding shifted Legendre polynomials in powers then produces H_j,D_j
with the normalization above. This is an exact coordinate calculation for
piecewise-constant histories, checked against independent analytic interval
integrals. High-degree power-basis numerical stability is not asserted.

At T, subtract the sum of recorded writes for the corrupted pair from the
hidden matrix, retaining the first layer and readout. Compare q1/q4/q8 edits
with the exact per-sample matrix accumulator. Then restore clean labels and
train all models for exactly two more time units. Controls are no edit and
a current clean hidden-gradient edit with Frobenius norm matched to the
exact historical edit. This needs identification and correction of the bad
labels. It does not infer which examples were wrong.

## Every fresh confirmation

All entries are clean512-point evaluation MSE after the same T_clean=2.

| Seed | No edit | Current gradient | q1 history | q4 history | Exact history | q4 reduction |
|---|---:|---:|---:|---:|---:|---:|
| 201 | .057843 | .057423 | .039994 | .042155 | .042184 | 27.12% |
| 202 | .050670 | .065458 | .048345 | .050146 | .050168 | 1.03% |
| 203 | .059346 | .055255 | .042132 | .043830 | .043844 | 26.14% |
| 204 | .056977 | .051955 | .040283 | .042940 | .042967 | 24.64% |
| 205 | .042841 | .051020 | .036956 | .038463 | .038477 | 10.22% |

The maximum q4 operator error for the corrupted pair is.002224 relative
Frobenius norm. The largest q4-versus-exact repaired MSE difference is2.88e-5.
The online/offline moment discrepancy is at most4.37e-11. q1 repairs better
than exact history on all five confirmations, emphasizing that reconstructing a historical write
more faithfully does not automatically optimize the downstream repair objective.

At n256, storing two q4 vectors per sample uses2nq=2048 coordinates versus
n^2=65536 for a per-sample matrix accumulator, a32-fold count reduction. The
audit implementation deliberately also retains full histories and exact
accumulators for comparison; it does not demonstrate a measured memory saving.
The dense learner itself remains dense.

## Stronger controls and adverse evidence

After confirmation, a fixed nuisance audit compared historical and current
gradient edits with the same line search alpha in{0,.25,.5,1,2,4}, selected
only by immediate corrected training loss. Both then receive T_clean=2.

| Seed | Line-searched history | Line-searched gradient | No edit, T_clean=2.5 |
|---|---:|---:|---:|
| 201 | .041218 | .051256 | .043924 |
| 202 | .048093 | .058139 | .038006 |
| 203 | .044472 | .053057 | .045855 |
| 204 | .042457 | .049045 | .043076 |
| 205 | .038546 | .046426 | .032174 |

The historical direction beats this stronger gradient direction in5/5 cases,
but beats the slightly longer ordinary cleanup in only3/5. There is no
end-to-end compute or practical-method superiority claim. These are additional
controls on the same frozen checkpoints, not five new independent replications.

The other planned question was whether destroying centered temporal pairing
would produce a large functional loss. On the three clean pilots, removing
centered pairing increased evaluation RMS by2.68%,3.03%,6.48%. Centered terms
had16--18% of the total-write Frobenius norm, but the prespecified20% practical
damage criterion did not pass on all three pilots. One-sided rotations and
singular-value-matched random perturbations are retained in the raw records.
This route was stopped without a favorable-window or longer-horizon search.
The joint-rotation invariance and second-moment controls passed numerically;
the desired large-damage mechanism did not. The implementation omitted the
planned matched random controls for the removal/half-removal arms and did not
save their dense-prediction differences; rotation controls were executed.
These omissions are recorded rather than claiming complete coordination-panel
execution. They do not affect the separate repair comparison.

## Validity and reproduction

The exact sum-of-writes oracle agrees with the dense update to below4e-14
relative. Initial pilot code uses offline analytic interval integration;
confirmation code adds the online observer, retaining both for comparison.
Seeds201/202 were rerun at step1/128 from their original initialization; the
largest repair-MSE change is4.65e-5. The small seed202 benefit remains positive
and exceeds twice that numerical change, but still falls below the original
10% practical-effect criterion. This is not a uniform practical confirmation.

Source: history_probe_initial.py, history_probe.py, history_controls.py.
Protocols: HISTORY_PROTOCOL.md and HISTORY_CONTROL_PROTOCOL.md. Generated
runs: history_pilot01, history_pilot02, history_confirm01, history_refine01,
history_controls01. Every trajectory run records configuration, source hashes,
software, timestamps, exit status and checkpoint hashes. Original pilot source
is preserved separately. The figures and complete numeric table are in
`history_summary/`, produced by history_analyze.py; its manifest hashes every
consumed result. Scientific trajectory runs total13 (including clean pilots
and two half-step repeats), followed by60 primary and65 additional cleanup
solves. The later control executes cleanup for all six multipliers in each
direction before selecting solely by immediate training loss, plus five longer
no-edit cleanups. Original trajectory-run wall sections total70.43seconds, including
their primary cleanups, before the lightweight saved-checkpoint controls.

Fresh confirmation from repository root (choose an unused output directory):

```sh
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/history_probe.py --panel repair --width 256 --seeds 201 202 203 204 205 --device cuda:1 --out data/generated/response_memory_use_cases_20261001/history_fresh
```

This is physical intervention on one parameter block of a jointly trained
network. Other samples' writes and both outer layers were influenced by the
corruption. Subtracting the corrupted samples' recorded terms does not undo
those influences, reconstruct a leave-out counterfactual, or certify forgetting.
No promotion or manuscript edit is part of this result.

The [independent internal review](HISTORY_INDEPENDENT_REVIEW.md) freshly
reproduced seed201 in7.26 CPU seconds, matching every scientific metric and all20
saved arrays exactly. Independent gradient, interval-quadrature and online-moment
oracles passed. It also identified two unused robustness gaps: the observer
normalization is undefined for a wholly zero-activity trajectory, and the driver
does not automatically mark a failed q64 approximation gate inconclusive. These
prototypes are restricted to this positive-activity benchmark; every retained
run passes the q32 approximation gate. No claim of a generally robust library
API is made. The exact initial protocol has now been restored as
HISTORY_PROTOCOL_INITIAL.md, with bytes verified against the original pilot
producer hash14cd38e3a460d9bd925ed69140ec1d184a2facc3f9701aa306dbff2d970c7e0b.
This source-preservation action occurred after the review; the original review
correctly records that it was not supplied those separate initial bytes.
