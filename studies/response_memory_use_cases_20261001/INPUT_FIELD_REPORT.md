# Input-function response memories: corrected canonical results

The fixed input-function construction learns from fresh observations without permanent per-observation memory slots. At the corrected canonical circle scale, it improves over training only the first layer and readout on all five confirmation seeds, with **12.3% lower median RMSE**. The stronger rank-matched factor control nevertheless outperforms it on every seed. The preregistered streaming-learning criterion passes; a competitive practical advantage over adaptive low-rank factors is not demonstrated.

This report supersedes the original report's interpretation as a canonical model result. A root audit found an extra input division by sqrt(2). Exact old source, protocol, report and derivation copies are retained as `*_INPUT_SCALED_V1.*`, and old generated results remain available as the explicitly input-scaled variant. The correction reran the same 81 configurations and seeds, without teacher or dictionary reselection. All 81 canonical fits completed, bringing the route total to 162 fits under the explicitly revised 180-fit ceiling. Canonical logged GPU stages took 28.63 seconds including validity checks, with 27.14 seconds in fit loops. Together with the original stages this is 57.37 logged GPU seconds, plus interpreter/CUDA startup, well below the original 20 GPU-minute ceiling. There were no failed or excluded fits.

## Normalization, algorithm and exact claims

Raw canonical inputs are \(x(\theta)=\sqrt2(\cos\theta,\sin\theta)\), with uniform angle \(\theta\). The source `Flow` API already receives \(x/\sqrt d\), so for \(d=2\) its rows are \((\cos\theta,\sin\theta)\), of norm one. The original rows had norm \(1/\sqrt2\), making first-layer preactivation variance 1/2 instead of 1 under the same Gaussian initializer. This changes the model. See [the normalization reconciliation](INPUT_FIELD_NORMALIZATION.md).

The network has two hidden tanh layers, width \(n=128\), no biases, an exactly zero initial readout, unhalved mean-square loss, and mobilities \((n,1,n)\). For the hidden connection let \(h\) denote its current input activation, \(\delta\) its current backward response excluding the residual, \(r=f-y\), and \(\rho=(\mathbb E r^2)^{1/2}\).

Replace sample-indexed moments by moments indexed by fixed orthonormal input functions \(\psi_c\), \(c=1,\ldots,C\). The forward and backward sources are \(\rho\mathbb E[h\psi_c]\) and \(\mathbb E[r\delta\psi_c]\), with the source closure's Legendre dilation. The clock satisfies \(\dot\tau=\rho\), \(\tau(0)=1\); initial zeroth forward moments are \(\mathbb E[h(0)\psi_c]\), and all backward moments start at zero. For time modes \(j=0,\ldots,q-1\), reconstruct

\[
W^{(2)}=W_0^{(2)}-\frac{2}{n\tau}
\sum_{c=1}^C\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{c,j}^{(2)}\bar h_{c,j}^{(1)\top}.
\]

The first layer and readout keep the canonical equations. All current fields are computed through the reconstructed network. Fresh batches estimate the sources and residual RMS. The learner keeps fixed \(W_0^{(2)}\), moving moments, first-layer weights, readout, and clock, but no growing input bank.

For uniform m-point inputs, \(\psi_c(x_a)=\sqrt m\,1[a=c]\) makes the new moments equal the source moments divided by \(\sqrt m\), exactly recovering its \(-2/(nm\tau)\) reconstruction. A separate exact statement says that orthogonal input/time projection of any one pair of square-integrable histories leaves only the product of their omitted parts in the interaction. These identities do not establish closed-loop trajectory equivalence. Nonlinear batch RMS and products of correlated moment estimates do not give an unbiased stochastic-dense algorithm. Complete definitions and the same-history proof are in [the derivation](INPUT_FIELD_DERIVATION.md).

## Fixed deterministic panels after correction

The original teachers remain unchanged: \(y_A=\sin\theta+0.5\sin3\theta\) and \(y_B=\sin3\theta+0.3\cos5\theta\). On seeds 101–103, 128-node quadrature, \(q=3\), and common physical time 64, the corrected median prediction RMSE to dense flow divided by teacher RMS was:

| Input representation | Teacher A | Teacher B |
|---|---:|---:|
| C=5 | 0.02952 | 0.02100 |
| C=9 | 0.002589 | 0.001235 |
| C=17 | 0.000578 | 0.000459 |
| Per-node source closure, q=3 | 0.000616 | 0.000759 |

At seed 101 and C=17, q=1,3,5 give raw prediction discrepancies 0.00722, 0.000457, 0.0000491 on A; on B they give 0.000838, 0.000339, 0.000430. Thus the three time orders are not monotone on both tasks, and no temporal convergence rate is inferred. Doubling quadrature nodes from 128 to 256 changes predictions by 4.92e-8 and 8.21e-8.

Teacher B, C=5 and q=3 were chosen in the original input-scaled pilots and **kept fixed before the canonical rerun**. These corrected panels were not used to reselect them. The generic C=5 Fourier dictionary has only two active odd modes in exact symmetric quadrature, cos(theta) and sin(theta); constant and frequency-two modes vanish. All five slots stay allocated, and sampling noise can excite the otherwise vanishing modes. This favorable symmetry limits generalization of the compactness result.

## Fresh-observation confirmation and controls

Each main run processes 4096 fresh batches of 64 angles through time 128 at Euler step 1/32: 262144 observations, with no replay dataset. The fixed 32-step CUDA graph block overwrites its buffers on replay. The 256 unlabeled initial quadrature nodes are discarded after constructing the prefix. Every algorithm uses batch-generator seed 600000 plus the model seed. Captured/eager updates and matching random batches are checked; final batch fingerprints match across all compared algorithms.

Held-out RMSE on 2048 uniform angles for the five fixed confirmation seeds:

| Seed | Field C5,q3 | Dense | Readout only | First layer + readout | Rank15 factors |
|---|---:|---:|---:|---:|---:|
| 201 | 0.019081 | 0.013002 | 0.364395 | 0.020548 | 0.011194 |
| 202 | 0.015682 | 0.012120 | 0.305747 | 0.017829 | 0.008734 |
| 203 | 0.017052 | 0.011652 | 0.381390 | 0.020038 | 0.010515 |
| 204 | 0.019029 | 0.013035 | 0.395960 | 0.021208 | 0.010142 |
| 205 | 0.018024 | 0.012193 | 0.381848 | 0.020747 | 0.009427 |
| Median | **0.018024** | **0.012193** | **0.381390** | **0.020548** | **0.010142** |

The factor control uses \(W_0+AB\), rank 15, \(A(0)=0\), independent \(B_{ij}(0)\sim N(0,1/15)\), unit factor mobilities, and outer mobilities n. It matches the field's allocated rank bound and factor-array budget, not its effective numerical rank or tangent metric.

Field median RMSE is 4.73% of readout-only RMSE, and hidden-activation RMS movement ranges from 0.4234 to 0.4504. The original dense gate \(\mathrm{RMSE}_{field}\le1.25\mathrm{RMSE}_{dense}+0.02\) passes. The field's median error is still 47.8% above dense, so the additive 0.02 tolerance must remain visible. Compared with the frozen-internal control, the field has 12.3% lower median RMSE and wins on all five seeds. This is a modest, consistent benefit from evolving the internal connection under the tested algorithm. Rank15 factors beat the field on every seed; the field's median error is 77.7% higher. Most of the readout-only performance gap is still accounted for by learning the first layer and readout.

![Canonical truncation and streaming controls](../../data/generated/response_memory_use_cases_20261001/input_field_canonical_analysis/input_field_summary.png)

## What changes after normalization correction

Both columns use identical configurations and confirmation seeds. The old column is retained as a different input-scale experiment, not combined with the canonical evidence or counted as additional canonical replication.

| Median held-out RMSE | Original API norm 1/sqrt(2) | Canonical API norm 1 |
|---|---:|---:|
| Field C5,q3 | 0.033570 | 0.018024 |
| Dense | 0.024003 | 0.012193 |
| Readout only | 0.540893 | 0.381390 |
| First layer + readout | 0.034351 | 0.020548 |
| Rank15 factors | 0.019226 | 0.010142 |
| Field / frozen-internal median ratio | 0.9773 | 0.8772 |
| Field / factor median ratio | 1.7461 | 1.7772 |

The correction strengthens the evidence for a small benefit from the learned internal connection: previously its comparison with frozen-internal training was mixed across seeds, now it wins on all five. It does not reverse the main competitive conclusion because the matched-rank factors remain better.

## Numerical checks, storage and costs

The corrected CPU audit passes 146 assertions, maximum error 6.66e-16. It explicitly checks unit API row norm and correspondence to raw x/sqrt(d), indicator-basis state/RHS/Euler parity, Fourier orthogonality, the product projection identity, and restarting from saved state plus fixed initialized weights with fresh observations. The short Euler refinement ratio is 2.0030. Each GPU stage also passes exact observed captured/eager fresh-batch parity.

At seeds 201 and 202, halving the step to 1/64 changes field predictions by 0.000676 and 0.001194 RMS, and target RMSE by at most 8.70e-5. The corresponding dense prediction changes are 0.000497 and 0.000944. Finer runs consume twice as many batches per unit physical time, so this is the declared joint step/noise sensitivity check, not a deterministic order estimate. Increasing prefix quadrature from 256 to 512 nodes changes predictions by 5.71e-8. Every numerical gate passes, and every corrected final state is directly checked finite. No all-time or population-limit theorem follows.

| Model | Moving scalars | Fixed parameter scalars | Retained sum |
|---|---:|---:|---:|
| Dense | 16768 | 0 | 16768 |
| Field C5,q3 | 4225 | 16384 | 20609 |
| Rank15 factors | 4224 | 16384 | 20608 |
| First layer + readout | 384 | 16384 | 16768 |
| Readout only | 128 | 16640 | 16768 |
| Per-node q3 closure, 128 nodes | 98689 | 16384 | 115073 |

The field uses 3.97 times fewer moving scalars than dense and 23.36 times fewer than 128 permanent sample slots. Its **total retained parameter and memory count exceeds dense by 23%**, because it also retains the initialized dense matrix. Dense SGD already needs no observation-specific state, so the construction resolves a limitation of sample-indexed response memory rather than a limitation of dense SGD. The frozen-internal control needs only 384 moving scalars; the field's modest extra accuracy costs substantial additional state relative to that comparator.

On this small captured test, median confirmation runtimes including capture and evaluation are 0.595 seconds for field and 0.266 seconds for dense. There is no speedup claim. Saved raw CUDA allocation/peak values include evaluation tensors, graph pools and process-lived stream workspaces and grow across sequential fits; they are unisolated allocator diagnostics, not a valid comparative memory benchmark.

## Claim status

| Claim | Status in the corrected scope |
|---|---|
| Indicator basis exactly recovers source Flow | Exact algebra and numerical parity |
| Same-history omitted interaction is a product of projection tails | Exact under orthogonal product projection |
| Finite dictionary needs no permanent observation slots | Implemented and restart-tested |
| Useful feature learning on the fixed fresh-input circle task | Supported over five confirmation seeds |
| Evolving the internal connection improves over fixed internal weights | Modest benefit on all five seeds; median RMSE improves 12.3% |
| Superior accuracy to matched-rank factors | Contradicted on all five tested seeds |
| Lower total storage or faster training than dense | Unsupported in this implementation |
| Unbiased stochastic equivalence, hierarchy convergence or all-time validity | Open; no theorem transfer |
| Robustness to other dimensions, input laws or distribution shifts | Untested |

The remaining practical obstacle is competitive value against strong matched-state methods, not merely demonstrating feature movement. This correction does not authorize or execute a new search for a favorable task.

## Provenance and reproduction

The source baseline remains unchanged. Canonical GPU directories under `data/generated/response_memory_use_cases_20261001/` are `input_field_canonical_deterministic`, `input_field_canonical_stream_pilot`, `input_field_canonical_stream_confirmation`, and `input_field_canonical_refinement`. Each contains exact source/protocol snapshots, commands, configurations, source/configuration/environment hashes, result JSON, prediction arrays, time snapshots and validity checks. CPU results are in `input_field_canonical_checks`; derived metrics and figures are in `input_field_canonical_analysis`. Old `input_field_*` result directories remain preserved and classified as input-scaled variants.

From the repository root, use a fresh destination for every fit command:

```bash
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_checks.py --out FRESH_CHECKS.json
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage deterministic --out FRESH_DETERMINISTIC
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage stream --teacher B --C 5 --seeds 101,102,103 --out FRESH_PILOT
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage stream --teacher B --C 5 --seeds 201,202,203,204,205 --out FRESH_CONFIRMATION
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage refine --teacher B --C 5 --seeds 201,202 --out FRESH_REFINEMENT
MPLCONFIGDIR=/tmp/input_field_matplotlib /home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/input_field_analyze.py --root data/generated/response_memory_use_cases_20261001 --prefix input_field_canonical --out data/generated/response_memory_use_cases_20261001/input_field_canonical_analysis
```

The derivation links primary sources on HiPPO, LoRA and GaLore; that limited comparison is not an exhaustive novelty review. No other study, archived book material, or other route's outcomes supplied this investigation. No maintained manuscript or API was edited.
