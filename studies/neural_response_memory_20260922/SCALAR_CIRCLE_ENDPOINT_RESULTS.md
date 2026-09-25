# Scalar closure as a final full-circle predictor

Subsequent authorized continuation: [efficient long-time scalar training](SCALAR_LONG_TIME_RESULTS.md)
now reaches MSE1e-6 in all four eight-input configurations. The time2048
observations below remain literal capped results; they do not describe
eventual fitting. The continuation compares the newly fitted functions and
records its separate integration and Fourier-encoding qualifications.

2026-09-25. User-requested endpoint continuation of the scalar aggregate test.
The passive extension defines an approximate output at every circle angle
using only scalar Fourier coefficients and scalar training states. It needs
no neuron populations after initialization. Comparing each model at its own
training-loss stopping time gives a materially different assessment from
maximum error along a common training clock.

On the four-sample mixed-label task, the dense reference and both scalar
methods reach training MSE 1e-6,
but order-four full-circle RMS differences are 0.1778--0.2053, about 20--23%
of the dense function's RMS size. On the eight-sample alternating task, every
dense reference reaches the target, but neither scalar method reaches it by
t=2048. Those cases have no qualified matched-loss endpoint comparison.
All spatial and numerical validity checks pass. The new metric does not
erase the earlier trajectory discrepancy; it answers the user's different,
function-level question.

## Every-angle scalar construction

Training inputs alone determine the residuals and vector fields. For a passive
input at angle phi, initialize scalar mixed tensors

    K_phi,b = D_b f_phi,
    C_phi,bc = D_c K_phi,b,
    Q_phi,bcd = D_d C_phi,bc.

The initialized dense network is used once to compute these coefficients.
There is no fitting to a trained dense network or its future trajectory.
As in the original candidate, Q is frozen; derivative indices stay ordered.
Define finite scalar integrals driven by the candidate's own training outputs:

    z'_b   = -(2/M)(f_b-y_b),
    I'_bc  = z_c z'_b,
    J'_bcd = I_cd z'_b,

all starting at zero. The exact passive readout for this truncated system is

    f_hat(phi,t) = f_phi(0) + sum_b K_phi,b(0) z_b(t)
                  + sum_bc C_phi,bc(0) I_bc(t)
                  + sum_bcd Q_phi,bcd(0) J_bcd(t).

The [mathematical check](SCALAR_CIRCLE_ENDPOINT_THEORY_CHECK.md) derives the
formula and verifies that passive inputs do not enter the training loss or
change its factor 2/M. The order-two baseline keeps only f(0)+K(0)z.

Each initialized coefficient function of phi is stored as a Fourier
polynomial through mode 64. Fourier projection commutes with the displayed
linear readout. Consequently arbitrary-angle evaluation requires only the
stored Fourier coefficients, trigonometric functions and current scalar
integrals. It does not call a network evaluator. There are 65 complex output
coefficients at the endpoint: 130 stored real entries, of which the imaginary
constant is redundant, giving 129 independent real coefficients.

This is a finite spatial approximation, not an exact finite representation
of arbitrary initialized functions. Its error was checked on the entire
1024-angle grid and 32 additional off-grid angles separately. Every model
passed at mode 64; no larger Fourier basis was needed. The largest observed
absolute Fourier/direct-passive difference is 8.59e-8, far below the measured
dense/candidate discrepancy. These are numerical checks, not a rigorous
uniform error bound at every unsampled angle.

## Endpoint definition and circle metric

The [protocol](SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md) was fixed before execution.
The canonical architecture, initialization, physical mobilities, data and
normalization are unchanged: three hidden tanh layers, widths 128/256,
seeds 20260920/20260927 and two literal tasks from deep_circle_cases.json.
The actual engine inputs are U=(cos(phi),sin(phi))=x/sqrt(2); no second input
rescaling occurs.

Each model starts afresh at the same random initialization and stops at its
own first numerically detected downward crossing of training MSE 1e-6. The
maximum physical time is 2048. This is a tolerance-defined training endpoint,
not an assertion of convergence to an infinite-time limit or permanence below
threshold. Event detection brackets successive accepted adaptive steps and
uses their dense interpolation; refinement tests the resulting endpoint.

The primary comparison, when both models reach the target, is

    E = sqrt((1/(2*pi)) integral_0^(2*pi)
             |f_hat(phi,T_scalar)-f_dense(phi,T_dense)|^2 d phi).

Thus the training times may differ. Uniform angular quadrature estimates E;
the dense endpoint function is the target. No labels are assigned to unseen
angles, so this is predictor agreement, not risk against a supplied true
circle-label function. Relative error is E divided by dense-function RMS.

The fixed practical agreement threshold is E<=0.1. E>0.2 is adverse; the
intermediate region is inconclusive under the protocol. Unfitted pairs are
reported separately and never counted as matched-endpoint successes or as
measurements of eventual infinite-time disagreement.

## Matched endpoints: four-sample mixed-label task

All dense, order-two and order-four runs in this table attain training MSE
1e-6. Times and errors use the fine solver resolution.

| Width | Seed | Dense time | Order-four time | Circle RMS | Relative RMS | Frozen-kernel circle RMS | Order-four verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| 128 | 20260920 | 16.19235 | 51.44138 | 0.182113 | 20.39% | 0.199181 | Inconclusive |
| 128 | 20260927 | 15.60331 | 53.58292 | 0.183115 | 20.49% | 0.207662 | Inconclusive |
| 256 | 20260920 | 16.28880 | 42.01336 | 0.177821 | 19.89% | 0.206205 | Inconclusive |
| 256 | 20260927 | 16.69084 | 57.65265 | 0.205285 | 22.95% | 0.179352 | Adverse |

The three intermediate cases are not classified as practical agreement.
Order four modestly improves the frozen-kernel endpoint in three cases and
is worse in one; no uniform endpoint advantage is established. A much smaller
training residual than circle discrepancy shows why evaluating only the
training sample outputs would miss the remaining function difference.

## Alternating-label task: endpoints not reached by the scalar models

Dense reaches training MSE 1e-6 in all four configurations. Both scalar models
reach the physical-time cap, with no numerical failure or wall cap. The
following candidate/dense discrepancies compare the capped scalar function
with the fitted dense function; they are diagnostics only, not qualified
matched-loss endpoint errors.

| Width | Seed | Dense fitting time | Order-four time | Order-four training loss | Capped circle RMS | Frozen-kernel training loss |
|---|---:|---:|---:|---:|---:|---:|
| 128 | 20260920 | 142.58168 | 2048 | 0.730977 | 3.920474 | 0.891416 |
| 128 | 20260927 | 150.89438 | 2048 | 0.625786 | 6.061748 | 0.873222 |
| 256 | 20260920 | 148.48791 | 2048 | 0.681337 | 8.507390 | 0.877329 |
| 256 | 20260927 | 169.36254 | 2048 | 0.666474 | 6.645079 | 0.884934 |

These results do not decide what happens after the declared cap. They show
that this experiment cannot rescue the candidate as a useful final-function
approximation on the harder task. Circle outputs outside the training arc
can differ greatly even when the candidate's training loss remains bounded.

## Numerical checks, scalar storage and scope

All 48 primary integrations complete with either a fitted endpoint or the
declared time cap, at rtol 1e-7 and 1e-9, atol=rtol/100 and max_step=2 using
DOP853. No conditional rtol=1e-11 run, angular refinement or Fourier enlargement
is triggered. Endpoint functions are compared at each resolution's own stop.
Maximum measured coarse/fine circle sensitivity is 2.61e-5. The largest change
in reported RMS between 512 nested angles and all 1024 is 9.21e-10. All gates
pass; these sensitivities are diagnostics, not certified error bounds.

Ten deterministic engine tests cover rectangular initialization against a
combined-input oracle, moving-direction derivatives, training-probe identity,
explicit passive equations, no feedback, disabled neural runtime functions,
restart and Fourier identities. The independent implementation and saved-output
audit is recorded in [SCALAR_CIRCLE_ENDPOINT_AUDIT.md](SCALAR_CIRCLE_ENDPOINT_AUDIT.md).
It passes 1194 checks, including all 48 primary and six reproduced endpoints,
independent dense evaluation, ordered scalar contractions and decision rescoring.
One complete six-trajectory configuration was rerun from fresh initialization;
all its saved scientific NPZ arrays match bit for bit. An additional saved-data
analysis passes 645 checks. Large cancelling terms in the capped scalar
readouts are checked against long-double contractions and explicit rounding
bounds; their discrepancy is at most 1.79e-8 and does not change conclusions.

The augmented order-four dynamics adds M+M^2+M^3 signature scalars: total
moving state 168 at M=4 and 1168 at M=8. Original fixed training Q uses 256
and 4096 entries respectively. The mode-64 passive coefficient representation
stores 11050 and 76050 real entries using complex arrays (10965 and 75465
independent real coefficients). Labels, initial-state copies and solver
workspace are additional. At the final endpoint only 130 real Fourier entries
are needed to evaluate the trained scalar function, once training is finished.
All these sizes are independent of neural width, but the M=8 training
representation is larger than the width-128 dense parameter count. Thus finite
scalar storage does not by itself establish a memory advantage in every case.

Initialization still uses the original dense network; the aggregate training
and readout do not. Scientific archives retain initialization probes and dense
reference checkpoints for checking, independently of what the scalar runtime
needs. The primary campaign took 116.687 seconds by the final log clock
(116.684 seconds in campaign.json before final serialization) on one CPU worker with one
BLAS thread, including 44.700 seconds of initialization and 70.161 seconds of
integration. Process high-water RSS was 223756288 bytes, about 213 MiB; this is
not a separately measured per-model peak. No accuracy-matched speedup is claimed.

This study supports the every-angle scalar construction and quantifies this
candidate's endpoint accuracy on the declared cases. It supplies no general
nonclosure result, hierarchy-convergence theorem, all-time endpoint guarantee
or error bound for arbitrary data. The previous matched-time negative result
remains valid in its own scope; it was insufficient on its own to answer this
new endpoint question. No maintained source, promotion or Git-index change.

## Files and reproduction

Source: scalar_circle_probe_engine.py, test_scalar_circle_probe_engine.py,
run_scalar_circle_endpoints.py, check_scalar_circle_endpoints.py and
analyze_scalar_circle_endpoints.py. Generated namespaces under
data/generated/neural_response_memory_20260922 are scalar_circle_endpoint_primary01,
scalar_circle_endpoint_reproduction01 and scalar_circle_endpoint_analysis01.
The separate [audit receipt](../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_audit01.json)
is scalar_circle_endpoint_audit01.json. The primary source snapshot and hashes
are in its sources/ and manifest.json. Replays require fresh output directories.

Views: [all eight circle functions](../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_analysis01/scalar_circle_endpoint_all_eight.png),
[representative functions and differences](../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_analysis01/scalar_circle_endpoint_representatives.png),
[matched endpoint table](../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_analysis01/primary_fitted_pairs.csv)
and [separate capped comparisons](../../data/generated/neural_response_memory_20260922/scalar_circle_endpoint_analysis01/capped_function_comparisons.csv).

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PYTHONDONTWRITEBYTECODE=1
/home/amir/miniconda3/bin/python -B -m unittest discover \
  -s studies/neural_response_memory_20260922 -p test_scalar_circle_probe_engine.py -v
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_scalar_circle_endpoints.py \
  --output data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary_new \
  --mode campaign --budget 780
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/run_scalar_circle_endpoints.py \
  --output data/generated/neural_response_memory_20260922/scalar_circle_endpoint_reproduction_new \
  --mode reproduction --budget 120
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/check_scalar_circle_endpoints.py \
  --deterministic \
  --runs data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary_new \
  --reproduction data/generated/neural_response_memory_20260922/scalar_circle_endpoint_reproduction_new \
  --json data/generated/neural_response_memory_20260922/scalar_circle_endpoint_audit_new.json
/home/amir/miniconda3/bin/python -B studies/neural_response_memory_20260922/analyze_scalar_circle_endpoints.py \
  --input data/generated/neural_response_memory_20260922/scalar_circle_endpoint_primary_new \
  --reproduction data/generated/neural_response_memory_20260922/scalar_circle_endpoint_reproduction_new \
  --output data/generated/neural_response_memory_20260922/scalar_circle_endpoint_analysis_new
```

The bounded requested campaign is complete. Its unused compute budget does
not constitute an additional training or model-tuning experiment.
