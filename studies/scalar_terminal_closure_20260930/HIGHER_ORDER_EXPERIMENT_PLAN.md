# q=2 and q=3: closure fidelity, then terminal scalar fidelity

Precommitment, 2026-09-30, recorded before new implementation or training.
Direct continuation of this study at the user's request. No other study is
an input. This plan does not change the earlier q=1 campaign.

## Question and competing outcomes

Does increasing the manuscript's learning-speed response-memory order to
q=2 or q=3 reduce the unseen-output error against dense width 1024 on the
two alternating-label tasks? Separately, does freezing their exact scalar
residual/query responses preserve those higher-order closures accurately?
Both orders and both tasks are mandatory; no favorable-order selection.
Successful fitting alone is insufficient. A higher order may improve or
worsen dense fidelity; a scalar continuation may add a separate error.

Use the actual shifted-Legendre closure in paper/main.tex, with the unit
prefix, tau(0)=1, tau_dot=sqrt(mean residual squared), zero readout and zero
backward memories. For mode j=0,...,q-1, use normalized forward memory
k_j=bar h_j/tau and value memory v_j=-2 bar delta_j. Only k_0 initially
equals the initial feature; every higher forward mode initially vanishes.
The reconstructed middle matrix is W0+sum_(a,j)(2j+1)v_(a,j)k_(a,j)^T/(mn).
Mode dilation couplings and both moving outer layers must be retained.

The exact query/residual response is obtained by replacing the q=1 key
and value in the prior response formula with the endpoint sums
sum_j(2j+1)k_j and sum_j(2j+1)v_j. This is to be checked algebraically and
against the complete mode velocities before training. It does not replace
the full reconstructed matrix with an outer product of those sums.

## Fixed experimental specification

Tasks: two_outliers_alternating and quadrant_alternating, exact arrays from
circle_task_inputs.json. Width 1024, seed 20260920, float64, same Gaussian
A and W0 and exact zero readout as circle_width1024_02/initialization.npz.
Use those saved arrays after checking their hashes against the generator.
No change of activation, rates, input normalization, clock, labels or mixer.

Reuse the previously independently checked dense trajectories and endpoint
states in circle_width1024_02, at their exact original common final times:
244.5 for two_outliers_alternating, 346.375 for quadrant_alternating.
Integrate every new closure to that task's same physical time. Compare
closure/dense loss curves at common times and predictions on the same 8192
midpoint-shifted circle queries. An endpoint is called fitted only when its
MSE is <=1e-6. If any higher-order closure has not fitted, report unfinished
fitting at the fixed horizon; do not extend the horizon under this plan.

First finish and assess the full-closure comparisons. Capture scalar handoff
coefficients during those runs, but evaluate/report the scalar continuation
as a separate second stage. Switch at the first coarse crossing of MSE
0.1, 0.01 (primary), and 0.001. Refined runs use the exact same switch times.
No scalar coefficient adjustment, extra Fourier modes, or chosen late switch
may replace the primary result. Report all switches as sensitivity evidence.

Scalar method: rdot=-C r+norm(r)b with frozen exact higher-order response
coefficients; integrate r and norm(r) as in the prior campaign. Same 17
moving and 712 fixed scalars (729 total), including 32 odd Fourier modes
for ten query coefficient functions, constructed from 2048 uniform samples.
Save untruncated query coefficients separately for diagnostics. Explicitly
report Fourier prediction training MSE as well as internal residual MSE.
The full-width pre-switch computation remains part of the setup cost.

## Numerical validity and decision rules

Full closures: independent RK4 runs from initialization, dt=1/8 and 1/16.
Scalar: DOP853, rtol=1e-10, atol=1e-12. Tiny deterministic checks must cover
q=1 reduction, raw/normalized moment equivalence, full B derivative versus
endpoint-sum identity, query derivative by central differences, initialization
and zero-residual stopping. Check the actual nonzero higher modes too.

Coarse/fine gates: endpoint closure RMS difference <=0.002, maximum
common-time loss difference <=0.001, primary scalar endpoint RMS difference
<=0.002. Dense reference refinement is reused and explicitly reported.
If a new gate fails, allow one dt=1/32 closure run to the same horizon and
same switches. Report failure if the 1/16 versus 1/32 gate still fails.
No numerical failure authorizes scientific parameter retuning.

Primary dense-fidelity threshold remains circle RMS <=0.05 and sign
disagreement <=1%, applied first to the closure and then to its scalar
model. Scalar-to-closure fidelity requires RMS <=0.01 and max error <=0.05.
Report RMS/max errors, sign disagreement (also away from |dense|<0.05),
loss curves and max common-time loss errors, endpoint MSE, switch times,
Fourier-only error and untruncated freezing error, static-handoff control,
coefficient contraction diagnostics, counts, timings, memory and provenance.
An eigenvalue diagnostic does not certify the theorem's complete tube bounds.

## Bound and outputs

One sequential CPU training worker, two BLAS threads, 4 GiB working memory,
3600 seconds cumulative new numerical training/analysis wall time. At most
eight baseline task/order/resolution runs and four triggered refinements.
Tiny checks and source review precede training. Preserve partial failures.
Scientific source/checks stay in this study; all new generated output uses
fresh directories under data/generated/scalar_terminal_closure_20260930/.
Freeze source/input/plan hashes and environment, retain initial/final/moment
states, handoffs and raw trajectories, and independently reconstruct saved
outputs. Produce readable loss/output plots and a report; update README.
No manuscript, book, maintained-code, Git index, commit or push changes.

The conclusion concerns one seed, two finite tasks, finite observation times
and a dense circle grid. It is neither a uniform-circle certificate nor a
full-training scalar compression theorem or a width-uniform result.
