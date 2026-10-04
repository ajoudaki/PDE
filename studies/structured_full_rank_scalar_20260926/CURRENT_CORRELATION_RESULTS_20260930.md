# Current-correlation continuation: a compact construction, no joint repair

2026-09-30. This fresh bounded round **does not close the hard-circle gap**.
Two new autonomous current-correlation closures were derived, frozen and
tested. Both fit training MSE 0.001, but neither improves both hard tasks
over the previous bounded-Gram model. The practical raw RMS 0.05 target
remains unmet. No transfer sweep, new dense training or third candidate
was run. All negative results are retained in the existing study.

There is one useful constructive result: an exact shared transport identity
reduces the Gaussian candidate to **m²+m evolving aggregates and zero query
ODE states**, with O(m²) static training matrices. This meets the desired
dynamic-size form, but its tested prediction errors reject it as an accurate
replacement. Mathematical coherence and compactness do not rescue that
failed empirical claim.

## Comparison and frozen decision

The canonical target is the same bias-free two-hidden-layer tanh network,
normalized unit-circle inputs, full Gaussian width 1024 initialization,
seed 1 and canonical mobilities (n,1,n). All models stop at their own first
training **MSE 0.001** crossing, not RMSE 0.001 and not a common physical time.
The metric is sqrt(mean((scalar−dense)²)) on 256 uniform circle angles.
No teacher error, amplitude normalization, alignment or fitted decoder is
used. The exact saved dense endpoints and their predictions are reused.
Scalar readout starts at zero; the finite dense readout starts tiny, as in
the preceding experiments. No new block-Gaussian replacement is introduced.

The [protocol](CURRENT_CORRELATION_PROTOCOL_20260930.md) froze at most two
candidates and the three focus tasks. An unchanged candidate could transfer
only after halving **both** hard baseline errors and keeping smooth error
at most 0.02, with numerical gates. Neither qualifies. There were exactly
six primary fits and two predeclared tighter close-pair checks, all complete.
The previous four repair rounds were not reopened or repeated.

| Model | Close pair: near_pair_sin9 | Hard cluster: cluster_triple_cos9 | Smooth control: cluster_triple_cos1 |
|---|---:|---:|---:|
| Previous bounded-Gram baseline, reused |0.240264|0.252676|0.010079|
| A: projected current feature/readout gate |0.151161|0.708189|0.014764|
| B: current Gaussian covariance/transport |0.342895|0.831930|0.008819|

A improves the close pair but worsens the hard cluster. B slightly improves
the smooth control but worsens both hard cases. Their smooth-control fits
do not support strong-label fidelity. All six primary fits had zero recorded
accepted-step loss rise and trained in 0.033–0.517 seconds with one BLAS thread.

![Fitted functions](../../data/generated/structured_full_rank_scalar_20260926/current_correlation_20260930/figure/current_correlation_functions.png)

## Exact dependencies before approximation

Use c for readout, h_a=tanh(z_a) for second-layer features, p_a for first-layer
features, d_a=1−h_a², e_a=1−p_a², and alpha=2/m. Averages are over their
appropriate layer. The exact dense equations contain the current operator

    B_ab = <p_a p_b> I + (x_a·x_b) W diag(e_a e_b) Wᵀ,
    c' = −alpha sum_b r_b h_b,
    h_a' = −alpha sum_b r_b diag(d_a) B_ab diag(d_b) c.

Consequently the current weighted gate Gram D_ab=<c² d_a d_b> satisfies

    D_ab' = 2<c c' d_a d_b>
            −2<c² d_a d_b (h_a z_a' + h_b z_b')>.

The first term requires <c h_s d_a d_b>; middle-layer gate motion introduces
<c³ h_a d_a d_b d_s>; first-layer gate motion additionally contains the
current W-dependent backward response. These formulas are exact at finite
width. Storing D, feature norms and readout energy does not by itself
produce their autonomous evolution. No general nonclosure or impossibility
theorem on the canonical training orbit is inferred.

Both candidates deliberately replace B_ab by its **initial normalized
trace** beta_ab times the identity. This trace is calculated from the same
Gaussian realization and includes both hidden parameter blocks. It is a
positive input-indexed Gram, but discards current first-layer evolution and
anisotropic matrix reuse. The distinct second approximation is how each
candidate represents the current readout/activation correlations.

## The two completed constructions

[Candidate A](CURRENT_CORRELATION_ROUTE_A_20260930.md) stores r, the symmetric
current feature Gram K, and readout energy q. It approximates a gate by

    D_a^A = (1−K_aa)[I−lambda_a h_a tensor h_a],
    lambda_a = 2/(1−K0_aa).

The rank-one term comes from a Gaussian fourth-moment projection; the
additional saturation factor is an imposed closure. The weighted gate Gram
is then a current expression in K,f=y+r,q, including f_a f_b K_ab. Exact
Gram evolution closes these variables without dividing by q. Its augmented
Gram positivity, loss decrease, readout-energy identity, feature-norm bound
and training aliases are exact surrogate identities. This operator is not
necessarily a positive contraction like a physical tanh gate. It also has
an artificial one-input radial barrier and confines training feature/readout
vectors to their initial abstract span. Neither the old cubic theorem nor a
strong-label approximation bound carries over.

[Candidate B](CURRENT_CORRELATION_ROUTE_B_20260930.md) closes the joint
readout/preactivation law by a centered Gaussian. Let
q=<c²>, u_a=<c z_a>, V_ab=<z_a z_b> and
s(v)=E[sech²(sqrt(v)xi)] for a standard Gaussian xi. Its output is
f_a=u_a s(V_aa). Gaussian identities explicitly close q',u',V' after
the frozen trace-mobility approximation. The resulting equations also
have a gradient-flow interpretation, proving loss decrease, covariance
positivity, the canonical readout-energy identity, bounded outputs and
aliases. The projected backward Gram is distinguished from the full
Gaussian expectation of c² times two gates.

The exact shared decoder follows because the frozen mobility A=beta is
invertible on these tasks. If F contains the initial abstract preactivation
vectors, current vectors/readout remain FR and Fb. Evolve only R and b;
recover q=bᵀV0b, u=RᵀV0b and V=RᵀV0R. For a passive input x,

    ell_x=A⁻¹A_x,       d_x=(R−I)ell_x,
    u_x=bᵀ(k0_x+V0 d_x),
    V_xx=V0_xx+2k0_xᵀd_x+d_xᵀV0d_x,
    f_x=u_x s(V_xx).

Differentiation gives exactly the original passive covariance ODE. Thus
this is an equivalent representation of the same candidate, not a new
approximation or an interpolation correction. R and b are aggregate
initial/current correlation coordinates; F, neurons and trajectories are
not retained. An entirely new input still needs its initialization
contractions. A finite initial weight realization has not been compressed
into a width-independent arbitrary-input coefficient oracle.

B's link uses 128 fixed positive **univariate** quadrature nodes, with its
consistent derivative. No node evolves or represents the neural population.
Preflight comparisons to adaptive scalar integration had errors below
2.2e-13 on the declared variance grid through 1000. Numerical function
evaluation is a separate approximation, not an additional neural Taylor
order. B already changes the initial training kernel: relative matrix
changes are 2.85% on the pair and 2.72% on the cluster, with weak-direction
kernel ratios 0.933 and 0.712. These defects were recorded before fitting;
the method was not calibrated to remove them.

## Current-correlation and same-state evidence

The [saved-state diagnostic](CURRENT_CORRELATION_DIAGNOSTIC_20260930.md)
separates two exact omitted terms:

    D − q mu muᵀ = Cov(c²,d_a d_b) + q Cov(d_a,d_b),
    mu_a=1−K_aa.

They can cancel. Replacing mean gates by their exact joint Gram does not
uniformly reduce error. Readout/gate association is large on the close pair
**and the smooth control**; it is not a unique classifier of the hard failures.
Even the hard cluster's relatively small 7.7% naive D matrix error coexists
with 77.1% error in its derivative when exact marginal derivatives are supplied.
The exact first-layer contribution supplies 48.7% and 43.8% of the hard cases'
lower tangent in the weakest initial-kernel direction. Endpoint observations
do not establish the time or cause of trajectory separation.

The separately frozen [same-state test](CURRENT_CORRELATION_SAME_STATE_20260930.md)
supplies exact dense current moments to each candidate's approximation map,
without evolving or fitting anything:

| Conditional approximation at the exact dense state | Close pair | Hard cluster | Smooth control |
|---|---:|---:|---:|
| A weighted gate Gram relative Frobenius error |0.755669|0.508999|0.741950|
| A full lower tangent relative Frobenius error |0.911702|0.651300|0.727494|
| B Gaussian output-link raw circle RMS |0.055173|0.183219|0.082828|
| B Gaussian output-link training RMS |0.069291|0.255968|0.119940|

Thus these approximations have nonzero errors even when their current
moments are exact. The Gaussian ansatz's smooth-control same-state error is
larger than its fitted-function error; different trajectory and map errors
can cancel. These rows are neither additive pieces of the primary RMS nor
an intrinsic lower bound for every scalar closure. No diagnostic supplied
coefficients or feedback to a fit.

An additional **posthoc analysis of already saved matrices** separates A's
two lower-response errors exactly:

    N_A − N_dense = beta0 ⊙ (G_A − D_dense)
                    + (beta0 ⊙ D_dense − N_dense).

The first term is the gate-map defect through the frozen mobility; the
second remains even with the exact current weighted gate Gram. This added
analysis performed no neural evaluation, integration or candidate change.

| Error remaining with exact current gates | Close pair | Hard cluster | Smooth control |
|---|---:|---:|---:|
| Relative lower-tangent Frobenius error |0.688683|0.354630|0.064144|
| Signed relative error along current residual |−0.707152|−0.838072|+0.073050|
| Signed relative error along initial weak direction |−0.707664|−0.729139|−0.468653|

Thus the shared frozen, isotropic hidden-response approximation still
underestimates lower-layer learning along the residual by **71% and 84%**
at the two hard dense endpoints. A's apparently modest 7% close-pair
directional error instead combines opposing gate and hidden-response errors
of approximately 78% and 71%. Improving one alone need not improve the
combined approximation. These observations do not separate freezing in
time from isotropization, or give trajectory/output error lower bounds.
They identify a concrete additional closure defect beyond current gates.

## Costs and numerical coverage

Q includes 256 circle points and all original training aliases.

| Candidate / m | Training dynamic | Query dynamic | Full-panel dynamic | Serialized training numerical coefficients | Serialized query coefficients |
|---|---:|---:|---:|---:|---:|
| A /2 |6|1032|1038|80 bytes|10320 bytes|
| A /3 |10|1295|1305|168 bytes|14504 bytes|
| B /2 |6|0|6|2160 bytes|10320 bytes|
| B /3 |12|0|12|2288 bytes|14504 bytes|

The B training column includes 2048 bytes for the scalar quadrature and the
small initial diagnostic Gram. Its serialized human-readable metadata adds
13948/14000 bytes, excluded from numerical coefficient counts. Actual model
arrays also retain derived slacks/lambdas or query solves: A uses 14608/18960
bytes including triangle indices; B uses 16608/23008 bytes including nested
link arrays, excluding Python object/metadata overhead. Dynamic state arrays,
solver stages and working temporaries are additional.

Both methods have O(m²) training coefficients (B adds the constant scalar
quadrature), O(Qm) query coefficients and O(m³) matrix-contraction RHS work.
A additionally does O(Qm²) query work at every step; B only needs
O(Qm²+QJ) post-training decoding with J=128. Its 0.0022-second panel decode
is material relative to the much cheaper A readout of already evolved queries.

Coefficient construction still evaluates the full initialized width 1024
network. It took 0.038–0.044 seconds per candidate/task, with transient dense
weights and batch-forward arrays. The constructor discards those arrays;
primary/refinement runs load saved aggregate coefficients and never create
neural arrays. O((m+Q)n²) construction work is separate from width-independent
scalar runtime. No end-to-end asymptotic speedup or measured peak-memory
certificate is claimed.

The six primary integrations totaled 1.2004 seconds. The two numerical checks
added 0.2344 seconds. On the close pair, rtol/atol 1e-8/1e-10 versus
1e-9/1e-11 changes the whole predicted function by 1.54e-11 RMS for A and
1.15e-10 for B. These reproduce the negative close-pair findings to far more
precision than needed. Hard-cluster and smooth-control integrations were
single new executions with saved-state audits; no all-case tolerance
reproduction is claimed because the promising-candidate branch did not open.

Training aliases agree within 1.6e-14, passive training-RHS independence is
exact, and nested 128/256 RMS changes are at most 7.2e-8. Endpoint loss,
energy, covariance/Gram and claimed bound checks pass. Small negative
augmented eigenvalues are at most 1.1e-14 in magnitude. A's potential
nonphysical gate bound violation is a model limitation, not a claimed
invariant; none was observed at these three scalar endpoints. B's largest
endpoint variance is 3.285 and its link refinement differences are below 1e-13.
These are numerical checks, not a dense-fidelity theorem or a certified
whole-circle quadrature bound. [The scoped audit](CURRENT_CORRELATION_RESULT_AUDIT_20260930.md)
records exact coverage, source hashes, producer checks and limitations.

## Claim status and stopping decision

| Claim | Type and status | Evidence / remaining obligation |
|---|---|---|
| Weighted-gate evolution requires the displayed mixed correlations | Exact finite-network identity, checked | Direct differentiation and dense-RHS finite differences |
| A and B are explicit autonomous aggregate models with stated invariants | Exact surrogate identities; implementation algebra checked | Complete route derivations and independent-formula checks |
| B's passive queries need no evolving states | Exact representation identity, checked | Shared transport proof and derivative/alias tests |
| Either frozen candidate repairs both hard circle functions | Empirically rejected on this panel | Six new focus fits; neither passes the frozen gate |
| Exact mean/joint gates alone classify or repair the old errors | Disfavored as a blanket explanation | Directional cancellations and smooth control |
| Exact current weighted gates suffice with the frozen trace mobility | Rejected as an accurate endpoint operator on the hard cases | Remaining residual-direction underestimation of 71% / 84%; no trajectory lower bound |
| A few current aggregate channels can accurately compress the dense flow | Open | Need a controlled closure of current anisotropic response and readout/feature dependence |
| Global or arbitrary-accuracy dense-fidelity theorem | Not established | No approximation-source estimate for these new closures |

The previous bounded-Gram method remains the best tested joint repair in
this study. The new exact transport identity is retained as a useful decoder
construction, separately from its unsuccessful Gaussian closure. The next
high-value theoretical obligation is to preserve the current directional
hidden response without replacing its matrix action by a scalar trace, while
retaining a controlled output-relevant readout closure. Naming another moment
is insufficient: its evolution and closure defect must be derived. The
exact-gate conditional comparison provides direct evidence for this obligation,
without claiming that it alone explains the final prediction error. This
report launches no further experiment; the bounded continuation is closed.

## Reproduction and ownership

Root owns protocol, runner, transport reduction, plot, synthesis and README.
Scoped route A and B authors derived/implemented their candidates; a separate
scoped checker audited their algebra and saved results. The A author performed
the same-state pass without reading primary fit outcomes. This is internal
study work, not independent complete promotion review. No other study was
read, no maintained scientific files were edited, and no Git write occurred.

All arrays, source snapshots, configurations, hashes and raw diagnostics are
under `data/generated/structured_full_rank_scalar_20260926/current_correlation_20260930/`.
The driver refuses existing output directories. Run from the repository root;
use new output names for any separately authorized reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/structured_full_rank_scalar_20260926/run_current_correlation.py --methods projected --output fresh_preflight_A --preflight
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/structured_full_rank_scalar_20260926/run_current_correlation.py --methods projected --output fresh_focus_A --coefficients-from fresh_preflight_A
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/structured_full_rank_scalar_20260926/run_current_correlation.py --methods gaussian --output fresh_preflight_B --preflight
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python studies/structured_full_rank_scalar_20260926/run_current_correlation.py --methods gaussian --output fresh_focus_B --coefficients-from fresh_preflight_B
```

For the predeclared close-pair refinement add
`--tasks near_pair_sin9 --rtol 1e-9 --atol 1e-11` and a fresh output name,
reusing the corresponding preflight coefficients. Standalone algebra checks
are `check_current_projected_correlation.py` and
`check_current_gaussian_correlation.py`; neither trains. Plot producer:
`plot_current_correlation.py`. Exact executed commands are retained in each
run manifest. Commands document reproduction and do not authorize another
campaign after this round's stopping decision.
