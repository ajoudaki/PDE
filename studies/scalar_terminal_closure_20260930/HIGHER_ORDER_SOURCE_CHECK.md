# Internal source check of the q=2/q=3 circle producer

Date: 2026-09-30.

Verdict: **PASS for the frozen producer's model equations, scalar observer,
matched comparison, and admitted numerical protocol.** The final complete
source has SHA256

`1773a2428b83af247c1b7eb360bcbce95f6eb9ef563322160998f3c18cd1a30a`.

The audit includes the final source and correction of the concrete
provenance/checkpoint issues identified in its earlier draft. Cumulative
accounting outside timed producer work remains the caller's responsibility;
one narrow asynchronous partial-history caveat is recorded below. No
width-1024 training has been run by this checker. This source verdict
does not certify an unobserved empirical outcome or the terminal theorem's
full-tube hypotheses.

## Inputs

The complete scientific inputs read for this check are
`HIGHER_ORDER_EXPERIMENT_PLAN.md` and `HIGHER_ORDER_SCALAR.md`, together
with the current manuscript's setting and learning-speed closure in
`paper/main.tex`, lines 178–443. The allowed q=1 implementation dependency,
`circle_terminal_experiment.py`, was previously read completely and its
unchanged hash was reverified. No linked review or other study was read.
Shared instructions and the previously read `solve-math-rigorously` skill
also apply.

Input SHA256 values:

- Plan: `919f07d4e76372d1e0e8fc0f65ad49f96b6cd4dd3a261d2814877759879d258a`.
- Higher-order derivation: `848e0903b4a42aafa5c6b24c4e83be4c59531c5b77efa4147113e97e7c17cfe2`.
- Complete manuscript file containing the permitted passage:
  `fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605`.
- q=1 producer: `f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba`.

## Independently recovered equations

The manuscript stores raw moments \(\bar h_j,\bar\delta_j\) and uses
the unhalved mean squared loss, input \(u=x/\sqrt d\), and clock speed
\(\rho=\|r\|_2/\sqrt m\). With
\(K_j=\bar h_j/\tau\), \(V_j=-2\bar\delta_j\), and \(c_j=2j+1\),
differentiation gives exactly

\[
\dot K_j=\frac\rho\tau\left[
H-(j+1)K_j-\sum_{i<j}c_iK_i\right],
\]
\[
\dot V_j=-2D\operatorname{diag}(r)
-\frac\rho\tau\left[jV_j+\sum_{i<j}c_iV_i\right].
\]

Here each mode is an \(n\times m\) matrix with examples as columns.
The extra \(-K_j\) term in the forward equation comes from differentiating
\(1/\tau\); there is no corresponding extra value term. Transforming
back verifies
\(\dot{\bar h}_j=\rho K_j+\tau\dot K_j\) and
\(\dot{\bar\delta}_j=-\dot V_j/2\) with the manuscript's raw equations.

The reconstructed matrix is

\[
B=W_0+\frac1{mn}\sum_{j<q}c_j V_jK_j^T.
\]

Its forward action and true transpose must retain these matched mode
pairs. In particular, replacing this sum with the outer product of two
weighted endpoint sums would add cross-mode terms and would define a
different model.

For each example, let the mode-column matrices be \(V,K\), set
\(D_c=\operatorname{diag}(c_j)\), and let the lower-triangular matrix
\(T\) have diagonal entries \(j\) and entries \(T_{ji}=c_i\) for
\(i<j\). Direct entrywise multiplication gives

\[
T^TD_c+D_cT+D_c=cc^T.
\]

Consequently, with \(K^*=\sum_jc_jK_j\) and
\(V^*=\sum_jc_jV_j\), differentiation of the matched reconstruction
gives

\[
\dot B=-\frac2{mn}(D\operatorname{diag}(r))(K^*)^T
+\frac\rho{mn\tau}V^*(H-K^*)^T.
\]

This is an identity for the derivative, not an alternative reconstruction
of \(B\). It is valid at zero residual without division by \(\rho\).

The outer-layer velocities remain
\(\dot w=-2Gr/m\) and
\(\dot A=-2(\mathcal E\operatorname{diag}(r))U^T/m\), with fields
computed using the full order-q matrix. The normalized circle inputs need
no second division by \(\sqrt2\). Initialization has only \(K_0=H_0\),
all higher \(K_j=0\), every \(V_j=0\), \(w=0\), and \(\tau=1\).
Duplicating the initial feature into all modes would violate the unit-
prefix moment initialization.

## Query response and scalar count

For query blocks denoted by a subscript \(q\), the exact train-to-query
response is

\[
C_q=\frac2m\left[
\frac{G_q^TG}{n}
+(U_q^TU)\odot\frac{\mathcal E_q^T\mathcal E}{n}
+\frac{D_q^TD}{n}\odot\frac{H_q^TK^*}{n}\right],
\]
\[
b_q=\frac1{m\sqrt m\tau}
\left[\frac{D_q^TV^*}{n}\odot
\frac{H_q^T(H-K^*)}{n}\right]\mathbf1_m.
\]

The output velocity is \(-C_qr+\|r\|_2b_q\). Fields in these expressions
still use matched-mode \(B\) and its true transpose; only the two
explicit memory contractions use endpoint sums.

The autonomous terminal state is unchanged:
\(\dot r=-Cr+\|r\|_2b\), \(\dot z=r\), \(\dot s=\|r\|_2\).
At the handoff \(z=s=0\), and the observer is
\(f_0-C_qz+b_qs\). It has \(2m+1=17\) moving coordinates. With
64 real odd Fourier coefficients for each of ten functions and the
training \(C,b\), fixed storage remains \(640+64+8=712\), totaling
729 model numbers. Antipodal oddness is preserved at every finite order:
the query network remains bias-free, query backward responses are even,
and the explicit query feature/input factors are odd.

The full order-q state has \(3n+2qnm+1\) moving numbers for the two-
dimensional inputs. At \(n=1024,m=8\), this is 35,841 for q=2 and
52,225 for q=3, plus the fixed 1,048,576-entry mixer. These setup costs
are separate from the terminal count.

## Independent bounded arithmetic check

Before the producer was available, this checker ran a standalone NumPy
calculation derived directly from the displayed manuscript equations.
It used seed 613091, width 7, three training examples, five queries,
clock 1.7, and random nonzero memories in **every** retained mode. No
time integration or training was performed. Maximum absolute errors were:

| Order | Raw versus normalized B | Forward raw-velocity transform | Backward raw-velocity transform | Full B derivative versus endpoint identity | Query velocity identity |
|---|---:|---:|---:|---:|---:|
| 1 | 5.55e-17 | 1.39e-16 | 0 | 5.55e-17 | 5.55e-17 |
| 2 | 2.22e-16 | 8.88e-16 | 0 | 4.44e-16 | 5.55e-17 |
| 3 | 2.22e-16 | 1.78e-15 | 0 | 4.44e-16 | 1.11e-16 |

The direct query velocity used separate readout, full \(\dot B\), and
first-layer chain-rule contributions. These tests support the algebra
at nontrivial higher-mode states; they are not producer execution tests
or evidence of trajectory accuracy.

## Complete producer audit

The complete draft producer was read, concrete issues were sent to its
author, and the complete final frozen source was then reread. The final
hash above is the applicable source identity. Only this report was written
by this checker; no producer or running process was changed.

### Full model and query implementation

`initial_state` creates arrays of shape `(q,n,m)`, places the initial
feature only in mode zero, leaves every higher key and every value zero,
and sets readout zero and clock one. Every task/order/resolution starts
independently from these conditions; it does not append modes to q=1
or restart from another resolution's trained state.

`fields` applies the fixed mixer plus a loop over matched mode actions
\(c_jV_j(K_j^TH)/(mn)\). Its backward action uses the literal transpose
\(W_0^TD\) plus \(c_jK_j(V_j^TD)/(mn)\). No endpoint-product matrix or
cross-mode reconstruction is substituted. `materialized_middle`, used
only by tiny checks, constructs the identical matched-mode matrix.

`velocity` uses weighted lower-mode prefix sums, updating each prefix
**after** computing the current mode velocity. Thus each mode receives
exactly the indices below it, with the correct weights. Forward diagonal
dilation is \(j+1\), value diagonal dilation is \(j\), and value forcing
is \(-2r_ad_a\) in every mode. Outer-layer rates, width/input factors,
and \(\rho=\|r\|_2/\sqrt m\) match the manuscript equations. Every
velocity vanishes at zero residual, including clock and all higher modes.

`endpoint_sums` takes weights \(1,3,5\) along the mode dimension.
`response` uses those sums only in the explicit memory contractions of
the query coefficients. Its forward/backward query fields still call the
complete `fields` function. The output derivative therefore has the exact
normalization and row/column orientation derived above. Query blocking
does not introduce state or alter those contractions.

The full closures use the already checked simultaneous RK4 routine from
the hash-verified q=1 helper. Its stage states include both moving outer
layers, every value/key mode, and the shared clock. There is no blockwise
update, time reparameterization, clipping, projection, or mixer resampling.

### Exact matching to the dense reference

`verified_initialization` loads the saved \(A,W_0,w\), requires the
declared shapes, checks \(A,W_0\) by exact array equality against the
stipulated seed/order generator, and checks that the stored readout is
exactly zero. Those verified arrays are saved in the new run and used for
every independent closure initialization.

The final source also checks the complete training geometry. The normalized
input array, labels, and training angles must agree with the frozen dense
reference's task JSON; labels and angles must additionally agree with its
saved curves. This closes the draft's weaker labels-only check. The
reference task JSON is included in the frozen reference hashes.

Both new closures integrate to the fixed original physical endpoints,
244.5 and 346.375, irrespective of whether they fit sooner. These endpoints
lie on each permitted dyadic grid. A closure that remains above the fitting
threshold at its fixed endpoint is marked unfitted; no horizon extension
is introduced.

The coarse closure uses the original coarse dense reference; fine and
optional 1/32 closure runs use the original fine dense reference. The
source recomputes and records the dense coarse/fine sensitivity. At 1/32,
the denser closure observation grid does not manufacture new dense
measurements: interpolation is used only in the saved plotting curve,
and quantitative loss errors use exact intersections of the two physical
time grids. Endpoint query comparisons reuse the identical dense query
grid and exact same final time.

Successful reuse of the dense target still requires the recorded dense
refinement gate to pass. A closure/scalar sensitivity result by itself
does not certify that separate reference gate; the report must retain
both pieces of evidence.

### Handoffs, scalar stage, and refinement decisions

Coarse handoffs are captured at the first checked losses at or below
0.1, 0.01, and 0.001. Fine and optional refined runs use precisely those
coarse-selected physical times. Their dyadic grids contain those times
exactly, so the direct equality used by the source is valid. Each
resolution records its own actual state and response at that common time.
Missing handoffs are listed explicitly.

Stage 1 completes the mandatory two tasks and both orders, records the
full-closure comparisons, and saves handoff coefficients without evaluating
the scalar continuations. Stage 2 requires a complete closure-only input
run and copies it to a fresh output root. This enforces the planned
separation of closure fidelity from the second compression step.

`evaluate_scalar` invokes the same 17-state residual/integral system and
DOP853 tolerances as the earlier campaign. The Fourier coefficient column
ordering is \((f_0,C_1,\ldots,C_8,b)\), and the final linear combination
is \((1,-z_1,\ldots,-z_8,s)\). Exact panel coefficients are retained for
the untruncated observer. Both the raw static function and the Fourier
static function are reported as controls. The source separately reports
internal residual MSE, Fourier-predictor training MSE, and exact/Fourier
training consistency errors.

The closure refinement gate uses endpoint RMS at most 0.002 and exact
common-time loss change at most 0.001. Stage 2 adds the primary scalar
endpoint RMS threshold 0.002. If a present primary scalar prediction
fails its new gate, the code permits one additional 1/32 closure run with
the same horizon and switch times, unless that refinement was already used
in Stage 1. Thus there are at most eight baseline runs and four unique
additional refinements across both stages. A missing primary handoff is
reported as unavailable and cannot pass the scalar gate; the code does not
invent another switch or tune the mode count to obtain it.

The final selected resolution is fine or the one permitted refined run;
the sensitivity verdict remains explicit if it fails. Numerical completion,
fitting, dense-output fidelity, and scalar-to-closure fidelity have separate
fields. The source does not turn successful training loss into an unseen-
output accuracy claim.

### Source freezing, budget, and partial artifacts

The helper's SHA256 is checked against its declared fixed value. Stage 1
saves hashes and copies of the producer, helper, task inputs, and plan,
and records hashes of the dense reference initialization, task JSON,
results, curves, endpoint states, and summaries.

Before Stage 2, the final source verifies both the current scientific
source files and their Stage-1 copies against the saved hashes. It also
rechecks every frozen dense reference hash. This prevents the draft's
possibility of silently replacing copied task/plan files before a later
refinement. Each handoff file is independently checked against its
captured digest before scalar evaluation, so changed response coefficients
are rejected.

Stage 2 saves the original closure results/provenance separately and
immediately initializes a new incomplete scalar result record. A failure
before the first completed scalar case can no longer leave an inherited
complete closure result mislabeled as current scalar success. Each
resolution also preserves its original closure-only curves and summary.

The `Budget` checks a finite positive allowance no greater than 3600,
uses a real-time alarm, checks wall time and process high-water RSS,
and rejects nonfinite state blocks or nonpositive clock values. RHS and
query-block boundaries are guarded; the alarm also bounds scalar solver
work between explicit guards. Loaded BLAS thread pools are limited to two,
and the campaign is sequential. High-water RSS conversion is correct for
the current Linux environment, with an explicit Darwin alternative.

Stage 2's allowance is capped by \(3600\) minus recorded previous producer
seconds. Source/input hashing, initial artifact copying, independent
analysis, and tiny checks outside those timed regions are not all included
in that producer total. The caller must supply a remaining allowance that
also reserves those costs, as the command-line help states. Source review
alone cannot certify the external cumulative accounting. Saving a failure
checkpoint after disabling the timer can take additional time and also
needs that reserve.

The earlier draft could checkpoint a newly accepted RK state with the
previous loop time. The final version fixes this by storing the accepted
state and its physical time in a single tuple reference before updating
the live loop state. An exception writes that tuple, so the checkpoint
state and timestamp remain aligned even if the alarm arrives between
loop statements. A pending alarm is disabled before writing the checkpoint,
preventing a second deadline exception from interrupting recovery.

One narrow residual caveat remains for **timeout-only partial artifacts**:
the time, loss, and residual history lists are appended in three separate
Python operations. An asynchronous alarm between those operations can
leave their saved lengths unequal. A partial-artifact reader must retain
their common complete prefix and use the explicit checkpoint state time
separately; it must not silently pair unequal arrays. The accepted
checkpoint can also legitimately be one step later than the last completed
observation. This does not affect complete successful trajectories, and
no running source change was requested after the final freeze.

## Producer tiny-check coverage and remaining validation

The source's 55 tiny checks cover q=1 reduction, matrix-form raw moment
equivalence, explicit matched-matrix forward/backward fields, full matrix
derivative versus the endpoint identity, a dense-plus-defect identity,
direct chain-rule query velocity, central directional differences at
non-initial higher-mode states, zero-residual stopping, and prefix
initialization. The tests retain genuinely nonzero higher modes, avoiding
a vacuous q=1-only check inside a larger array.

The supervisor and producer author report that all 55 checks passed for
the final frozen source in `higher_order_checks_02`. This checker audited
their complete implementation and independently executed the separate
bounded arithmetic calculation reported above; it did not rerun the
producer checks or inspect unassigned empirical outcomes.

Independent analysis of the saved campaign still needs to reconstruct
the raw moments, matched-mode matrix/actions, endpoint predictions,
handoff coefficients, Fourier/scalar outputs, time grids and all
sensitivity metrics. The source exposes the required full moment states
and hashes. Its correctness neither predicts whether q=2/q=3 improve
dense fidelity nor supplies a terminal-tube certificate, a population
limit, or an initialization-only scalar compression theorem.
