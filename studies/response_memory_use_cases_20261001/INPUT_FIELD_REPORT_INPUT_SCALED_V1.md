# Input-function response memories: completed route report

The construction works as a bounded-state streaming learner on the tested
circle task. It learns much better than readout-only training, using no
permanent memory slot for any arriving observation. **The experiment does
not establish a practical advantage for the response-memory mechanism:**
training only the first layer and readout performs almost identically with
much less moving state, and matched-rank trained factors perform better.
The narrow preregistered learning criterion passes; the stronger architecture
advantage remains unsupported.

All 81 planned fits completed. The logged GPU stages took 28.74 seconds from
manifest creation through completion, including validity checks, of which
27.16 seconds were fit-loop wall time. Interpreter/CUDA startup is additional;
the campaign is far below its first 20 GPU-minute cap. No extension, extra
teacher, Hadamard variant, failed fit, or excluded seed is hidden.

## Construction and scope

Inputs are uniform circle angles with normalized rows
\(x(\theta)=(\cos\theta,\sin\theta)/\sqrt 2\). The tested network has two
hidden tanh layers, width 128, no biases, a zero initialized readout, and
unhalved mean-square loss with source mobilities \((n,1,n)\). Write \(h\)
for the current first-layer activation, \(\delta\) for the current
second-layer backward response excluding the residual, \(r=f-y\), and
\(\rho=(\mathbb E r^2)^{1/2}\).

Replace sample labels on the moments by C fixed orthonormal input functions
\(\psi_c\). Retain the original time modes and dilation equations, but use
sources \(\rho\mathbb E[h\psi_c]\) and
\(\mathbb E[r\delta\psi_c]\). Set \(\dot\tau=\rho\), \(\tau(0)=1\),
initialize zeroth forward moments by \(\mathbb E[h(0)\psi_c]\), and initialize
all backward moments to zero. For time modes \(j=0,\ldots,q-1\), reconstruct

\[
W^{(2)}=W_0^{(2)}-\frac{2}{n\tau}
\sum_{c=1}^C\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{c,j}^{(2)}\bar h_{c,j}^{(1)\top}.
\]

The first layer and readout keep the canonical equations; all fields are
evaluated through the current reconstructed network. In a stream, each source
and the residual RMS use the current fresh batch. The fixed input law is
essential to the chosen orthonormal basis. This is a new algorithmic extension
of the source closure, with additional input truncation and stochastic errors.

For uniform m-point data, \(\psi_c(x_a)=\sqrt m\,1[a=c]\) gives moments equal
to the source moments divided by \(\sqrt m\), recovering exactly its
\(-2/(nm\tau)\) reconstruction. Separately, orthogonal input/time projection
on any one fixed pair of histories leaves only the product of their omitted
parts in the integrated interaction. Neither identity proves that feedback
trajectories agree. Shared noisy sources, their correlated histories, the
nonlinear RMS clock, and products of moment estimates prevent an unbiased
stochastic-dense interpretation. Full definitions, scaling, and proof of the
same-history identity are in [the derivation](INPUT_FIELD_DERIVATION.md).

## Deterministic input and time truncation

The teachers were fixed before fitting:
\(y_A=\sin\theta+0.5\sin 3\theta\) and
\(y_B=\sin 3\theta+0.3\cos 5\theta\). Both respect the odd architecture but
require higher harmonics. On seeds 101–103, 128-node uniform quadrature,
\(q=3\), and common physical time 64, the median prediction discrepancy to
dense flow, divided by teacher RMS, was:

| Input functions | Teacher A | Teacher B |
|---|---:|---:|
| C=5 | 0.02339 | 0.02333 |
| C=9 | 0.001320 | 0.001025 |
| C=17 | 0.000988 | 0.000654 |
| Per-node source closure, q=3 | 0.001016 | 0.000986 |

This separates input truncation from the already present time truncation. At
seed 101,C=17, increasing q from 1 to 3 to 5 reduced raw dense discrepancies from
0.00601 to 0.000550 to 0.000142 on A, and from 0.00294 to 0.000483 to 0.000299 on B.
Doubling quadrature nodes 128→256 changed predictions by 4.0e-8 and 5.9e-8.
These are finite, common-time checks, not convergence-rate estimates.

The preregistered choice rule selects B from its smaller C=17 normalized
error, then selects the smallest qualifying C, namely 5. The choice was frozen
in [the branch record](INPUT_FIELD_BRANCH.md) before streaming fits. The
generic C=5 Fourier dictionary contains only two active odd modes in exact
symmetric quadrature, cos(theta) and sin(theta); constant/frequency 2 modes
vanish. All five slots remain allocated, and finite batches can excite the
otherwise vanishing modes. Compactness partly uses this circle symmetry.

## Fresh observations and strong controls

Each run sees 4096 fresh batches of 64 angles, or 262144 observations, at
Euler step 1/32 through time 128. Arriving observations are generated inside
the fixed 32-step CUDA graph block; graph buffers are overwritten on replay,
and no growing sample-indexed state is created. There is no replay dataset.
The only initialization quadrature is 256 unlabeled input nodes, discarded
after prefix construction. All algorithms use the same batch PRNG seed
600000+model seed. Captured/eager updates and batch equality were checked,
and final batch fingerprints match across all compared algorithms.

Fresh confirmation seeds 201–205 gave held-out RMSE on 2048 uniform angles:

| Seed | Field C5,q 3 | Dense | Readout only | First layer + readout | Rank 15 factors |
|---|---:|---:|---:|---:|---:|
| 201 | 0.033570 | 0.024003 | 0.543418 | 0.035039 | 0.017579 |
| 202 | 0.031463 | 0.024109 | 0.476386 | 0.032554 | 0.016178 |
| 203 | 0.034605 | 0.022328 | 0.540893 | 0.034351 | 0.020085 |
| 204 | 0.033839 | 0.026111 | 0.551881 | 0.036840 | 0.019226 |
| 205 | 0.033136 | 0.022374 | 0.534662 | 0.032533 | 0.020263 |
| Median | **0.033570** | **0.024003** | **0.540893** | **0.034351** | **0.019226** |

The factor comparator uses \(W_0+AB\), rank 15, \(A(0)=0\), independent
\(B_{ij}(0)\sim N(0,1/15)\), unit factor mobilities, and outer mobilities n.
It matches the field's allocated correction-rank bound and factor-array
budget, not an effective singular-value rank or a tangent metric.

The field's median RMSE is 6.21% of readout-only RMSE, while its final hidden
activation RMS movement is 0.393–0.432. It passes the predeclared dense gate
\(\mathrm{RMSE}_{field}\le 1.25\mathrm{RMSE}_{dense}+0.02\). Its median error
is nevertheless 40% above dense, so the additive 0.02 tolerance must not be
hidden. The field is only 2.3% better than the frozen-internal control by
median and loses to that control on two of five seeds. The rank 15 factor
control beats it on every seed. These controls leave ordinary outer-layer
feature learning as a strong explanation for the apparent benefit.

![Deterministic truncation and streaming controls](../../data/generated/response_memory_use_cases_20261001/input_field_analysis/input_field_summary.png)

## Validation, state and costs

The CPU check has 144 assertions, including indicator-basis scaling, source
RHS and Euler parity, Fourier orthogonality, the tensor-product projection
identity, and restarting from saved moving coordinates plus fixed initialized
weights while presenting new observations. Maximum error is 6.66e-16. Short
Euler step refinement gives a difference ratio 1.996. CUDA graph/eager
fresh-batch updates have zero observed state discrepancy in the bounded check.

For confirmation seeds 201 and 202, halving the step to 1/64 changes field
predictions by 0.00128 and 0.00252 RMS and target RMSE by at most 8.4e-5. The
dense control changes by 0.000841 and 0.00194 prediction RMS. The finer runs
consume twice as many fresh batches per physical time, so this is the
predeclared joint step/noise sensitivity check, not a deterministic order
estimate or a comparison of identical continuous noise paths. Doubling the
prefix to 512 nodes changes field predictions by 5.8e-8. Every numerical gate
passes; all confirmation/refinement states are directly checked finite.

| Model | Moving scalars | Fixed parameter scalars | Retained sum |
|---|---:|---:|---:|
| Dense | 16768 | 0 | 16768 |
| Field C5,q 3 | 4225 | 16384 | 20609 |
| Rank 15 factors | 4224 | 16384 | 20608 |
| First layer + readout | 384 | 16384 | 16768 |
| Readout only | 128 | 16640 | 16768 |
| Per-node q 3 closure,128 nodes | 98689 | 16384 | 115073 |

The field reduces moving coordinates by 3.97 times against dense and 23.36
times against 128 permanent sample slots. **Its total retained parameter and
memory count exceeds dense by 23%.** Dense SGD itself already needs no
per-observation memory, so this result solves a limitation of sample-indexed
response memory, not a limitation of dense SGD.

On this tiny captured test, median confirmation runtimes were 0.595 seconds
for field and 0.269 seconds for dense, including capture and evaluations.
There is no speedup claim. Raw CUDA allocated/peak bytes are saved per fit;
they include evaluation tensors, graph pools and process-lived CUDA stream
workspaces, and grow across sequential fits. Those unisolated values are
allocator diagnostics, not a valid model-to-model memory benchmark.

## Claim status and remaining obstacle

| Claim | Status after this route |
|---|---|
| Indicator functions exactly recover source Flow | Exact under uniform finite input law; algebra and parity checked |
| Same-history input/time defect is an omitted-tail product | Exact for square-integrable histories and orthogonal product basis |
| Finite dictionary learner needs no permanent observation slots | Implemented and restart-tested |
| Useful feature learning on the selected fresh-input circle task | Empirically supported over five new seeds and the stated gates |
| Response memory explains an advantage beyond learned outer layers | Unsupported; strong control nearly matches it |
| Better accuracy than matched-rank adaptive factors | Contradicted on all five tested confirmation seeds |
| Lower total storage or faster training than dense SGD | Not supported by this implementation |
| Unbiased streaming approximation, population convergence or all-time guarantee | Open; not supplied by projection algebra or source theorem |
| Generalization to other input laws, dimensions or shifting streams | Untested |

The next scientific obstacle is to find a preregistered regime in which the
memory-trained internal connection matters relative to a learned first layer
and readout, and in which matched-state adaptive factors do not already solve
the task better. This report does not authorize or execute that new search.
The finite streaming construction and exact scaling remain useful even though
the current evidence does not identify a winning practical application.

## Reproduction and provenance

The source baseline is unchanged. Each GPU run directory contains exact source
snapshots, the protocol, source/configuration/environment hashes, command,
environment, frozen run list,
per-fit JSON, predictions and time snapshots. Old snapshots precede the
logging-only finiteness addition. Original CPU checks and the later
restartability audit are retained separately. Generated directories are
`input_field_deterministic`, `input_field_stream_pilot`,
`input_field_stream_confirmation`, `input_field_refinement`,
`input_field_checks`, `input_field_checks_restart`, and `input_field_analysis`
under `data/generated/response_memory_use_cases_20261001/`.

From the repository root, use a fresh destination in each command:

```bash
/home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_checks.py --out FRESH_CHECKS.json
/home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:1 --stage deterministic --out FRESH_DETERMINISTIC
/home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:1 --stage stream --teacher B --C 5 --seeds 101,102,103 --out FRESH_PILOT
/home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage stream --teacher B --C 5 --seeds 201,202,203,204,205 --out FRESH_CONFIRMATION
/home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_experiment.py --device cuda:0 --stage refine --teacher B --C 5 --seeds 201,202 --out FRESH_REFINEMENT
MPLCONFIGDIR=/tmp/input_field_matplotlib /home/amir/miniconda 3/bin/python studies/response_memory_use_cases_20261001/input_field_analyze.py --root data/generated/response_memory_use_cases_20261001 --out data/generated/response_memory_use_cases_20261001/input_field_analysis
```

Primary-literature positioning against HiPPO, LoRA and GaLore is recorded in
the derivation, with direct sources. This is a limited comparison, not an
exhaustive novelty review. No study external to the authorized baseline, no
other route's findings, and no archived book material supplied this analysis.
