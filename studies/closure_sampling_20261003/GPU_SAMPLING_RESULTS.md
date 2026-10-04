# GPU results: practical log-state neuron sampling

2026-10-03. Bounded numerical continuation under
[GPU_SAMPLING_PROTOCOL.md](GPU_SAMPLING_PROTOCOL.md). The sweep is complete;
no additional optimization or training sweep was launched after inspecting
the results.

## Conclusion

The tested practical sampler is fast and can be accurate with very few
neurons, but **none of the tested log(n) or log(n)^2 state schedules
consistently matched dense-versus-dense variability across all three widths**.
The strongest schedules worked well at width 512, then their prediction
error was roughly flat while the dense-copy discrepancy decreased.
All models fitted their training data. Much of the discrepancy remained
on unseen inputs at the numerically settled endpoint.

This is evidence against these particular budgeted, low-order samplers.
It neither identifies an optimal exponent nor proves that p=1 or p=2 is
impossible. It does not test the full theorem's potentially enormous
initial-derivative construction. That distinction is substantive.

## What was actually run

The reference is the realized canonical dense network with two width-n
tanh hidden layers, no biases, independent Gaussian read-in/mixer, zero
readout, and mobilities (n,1,n). It follows the maintained
`pde.finite_torch.NetworkEngine` equations in physical time. Batched hot
contractions were checked against its public RHS and complete Heun step.

The fixed grid was:

- n = 512, 1024, 2048;
- training directions separated by 90 or 60 degrees on the circle;
- labels (0.2,0.1) and (0.2,-0.1);
- three independent seed pairs per width/geometry/sign cell;
- two dense copies and all reduced models trained with their own residuals;
- float64 on the two RTX 3090 GPUs, TF32 disabled, Heun dt=0.2;
- 257 unseen circle directions observed every physical unit of time.

The numerical label size is fixed and modest. The theoretical small-label
threshold was not quantified numerically; these runs do not certify that
the chosen scale lies below it. The nonorthogonal cases are empirical
extensions beyond the proved orthogonal-pair theorem.

There were 36 paired cases, 72 dense trajectories and 180 distinct reduced
trajectories. Deduplicated models supply 216 declared budget comparisons.
The main workers completed in 66.6 and 71.7 seconds respectively, with
peak allocated GPU memory about 409 MiB each. The pilot and final
half-step check added only a few seconds and 12.3 seconds respectively.
The total was far below the 20-minute cap.

All cases ran through physical time 120. One case, extended by the
predeclared residual rule, continued to 240. Every recorded model met the
settlement criteria: maximum final residual RMS was 1.99e-7; the largest
final-versus-ten-time-units-earlier prediction change was 7.27e-7.
These are numerical endpoint diagnostics, not an infinite-time certificate.

## The numerical sampler and its differences from the theorem

[neuron_sampling_setup.py](neuron_sampling_setup.py) uses only the original
initialization, labels, training directions and 16 fixed half-circle probes.
It computes initialized forward responses through physical derivative order
two and backward responses through order one, with W0 and W0.T partners.
There are no trained snapshots, future residuals or target-trajectory inputs.

The practical implementation retains source rank at most eight, selects
original neurons, fits positive approximate cubature weights, and normalizes
the selected source frames to produce a mixer with bounded weighted operator
norm. The total prescribed mass-floor fraction is .05. The full source and
moment errors, selection diagnostics, optimization statuses and numerical
rank decisions are archived. No optimizer failure or selected-Gram numerical
mode deletion occurred in the main sweep.

These choices deliberately replace the theorem's large initial-response
space and exact cubature with a cheap finite approximation. In particular,
8--25 weights approximately fit up to 29 or 37 product/constant moments.
The resulting source mismatch is not covered by the exact theorem's error
bound. The rank-eight cap is also fixed over this limited width range.

Runtime is a fully autonomous weighted tanh network. It stores its read-in,
readout and a learned small mixer, and evolves all of them. The code stores
K=B diag(mu)^(-1), giving forward mixing K diag(mu) and reverse mixing
K.T diag(nu); this is an exact coordinate change of the weighted dynamics.
No division by a tiny mass is required at runtime. A saved reduced restart
contains no full-width state. The comparison process also holds the original
dense references and diagnostic/setup workspace; reported model counts are
not a claim about the entire experiment process's memory.

For selected width N in both layers, the total retained model count is

    moving = N^2 + 3N,
    fixed  = 2N + 6,
    total  = N^2 + 5N + 6.

The fixed part includes both neuron mass vectors, training directions and
labels. We imposed budgets

    S * [log(n)/log(512)]^p,
    S in {128,256,512}, p in {1,2},

and selected the largest N within each budget. No constants were changed
after observing performance.

## Quantitative results

The primary error E is the maximum absolute prediction discrepancy over
all saved physical times and the 257 query directions. The paired dense
baseline is the same error between the independent dense copy and the
reference. Ratios below are medians of the 12 paired comparisons at each
width, pooling the four fixed geometry/sign cells with three replicates
each. They are not confidence bounds.

For the largest anchor budget, S=512:

| n | p=1 total state | p=2 total state | p=1 median E / dense baseline | p=2 median E / dense baseline |
|---:|---:|---:|---:|---:|
| 512 | 506 (N=20) | 506 (N=20) | 0.56 | 0.56 |
| 1024 | 552 (N=21) | 600 (N=22) | 1.70 | 1.50 |
| 2048 | 600 (N=22) | 756 (N=25) | 2.51 | 2.75 |

The p=2 median absolute errors were 0.00707, 0.00720 and 0.00750.
Thus their sqrt(n)-scaled medians increased from 0.160 to 0.231 to 0.339.
This looks like an approximation floor over these widths, rather than
the desired clear decay at the dense-variability scale.

The larger p=2 model is not uniformly better than p=1: the node/weight and
projection constructions are not nested, and no monotonicity theorem applies.
The complete seed ranges and cell medians are retained in the CSV outputs.

At n=2048, for the largest p=2 budget:

| Input angle | Label signs | Median absolute E | Median paired E / dense baseline |
|---:|---|---:|---:|
| 90 degrees | same | 0.00719 | 2.99 |
| 90 degrees | opposite | 0.00548 | 1.78 |
| 60 degrees | same | 0.00670 | 2.08 |
| 60 degrees | opposite | 0.00802 | 6.53 |

The median of paired ratios is generally not the ratio of two medians.
In particular, the last cell contains one especially small dense baseline,
so three replicates cannot establish a precise population-level ratio.

The smaller anchor budgets were less accurate. Across cells, the worst
median paired ratios were 25.54 and 17.46 for S=128, p=1 and p=2;
9.73 and 7.17 for S=256; and 6.64 and 6.53 for S=512. All six schedules
fail the predeclared competitive criterion. This criterion requires every
cell median ratio <=1.5, settled fits and numerical validity, and at most
1.5-fold growth in median sqrt(n)-scaled error from 512 to 2048.

![Width-scaled prediction errors](../../data/generated/closure_sampling_20261003/gpu_sampling_20261003_analysis/width_scaling.png)

The plot shows medians and seed ranges for the largest anchor. A flat curve
would be consistent with root-width scaling over the tested range. The
compressed curves do not consistently remain flat. The falling dense-copy
curves also show that these three seed pairs are not a precise asymptotic
rate estimator.

## What the errors reveal about learning

Training failure is not the explanation: every smaller model fitted both
labels. For S=512,p=2, the median ratio of endpoint error to maximum-over-time
error was .975; 24 of 36 cases retained at least 90% of their peak discrepancy
at the endpoint. The missing fidelity is largely in the selected function
on unseen inputs.

Both hidden layers moved substantially. For S=512,p=2, final training-averaged
feature RMS motions ranged from .030 to .086 in the first layer and .039 to
.113 in the second. The corresponding dense ranges were .035--.083 and
.045--.116. These trajectories did not freeze the hidden representations.
Matching an RMS motion is not a complete comparison of feature geometry.

The exact frozen-hidden dense readout control had a median error-to-dense-copy
ratio of 2.58 over the 36 cases. It was especially inaccurate in the
nonorthogonal opposite-sign setting. The reduced models therefore can track
meaningful nonlinear movement, while still selecting noticeably different
unseen-input functions.

The bounded setup has a visible source-approximation error. For the largest
p=2 schedule, median initial forward-response weighted RMS errors were .0491,
.0402 and .0371 as n increased; reverse-response errors were .0105, .0101 and
.00898. Initial training-Gram Frobenius errors decreased from .0105 to .00417.
These are setup diagnostics, not a decomposition proving which error caused
the final discrepancy. Together with successful fitting and near-flat query
errors, they support investigating the truncated response representation and
approximate cubature before interpreting p as the limiting issue.

## Numerical checks and evidence level

- Batched RHS and complete Heun parity with the maintained code: errors
  at most 1.12e-16 on the deterministic tiny test.
- Nonuniform weighted rectangular gradient check against autograd: 9.55e-18.
- Array-only own-state restart: exactly matching continuation.
- Width-512 pilot, dt=.2 versus .1 and nested doubled time/query panels:
  maximum same-point difference 2.58e-5; primary-metric change 9.64e-6.
- Width-2048 nonorthogonal opposite-sign refinement: maximum difference
  2.49e-5; primary-metric change 9.06e-6.
- Both refinement checks passed the predeclared minimum of 1e-4 and 5%
  of the dense-copy discrepancy. All scientific runs used float64.
- Every raw observation/restart hash was verified during analysis. No failed
  runs or unfavorable cases were omitted.

The checks establish meaningful finite-panel, finite-time empirical evidence.
They do not certify a continuum supremum, high-probability asymptotics or a
minimal state dimension. The exact theorem remains internally checked and
separate; this practical variant has no inherited all-time approximation
guarantee. Numerical bias, sampler bias, model error and dense variability
are kept distinct.

## Reproduction and artifacts

Source files:

- [GPU_SAMPLING_PROTOCOL.md](GPU_SAMPLING_PROTOCOL.md), fixed before training;
- [neuron_sampling_setup.py](neuron_sampling_setup.py), initialized sampler;
- [gpu_sampling_experiment.py](gpu_sampling_experiment.py), validated GPU runner;
- [analyze_gpu_sampling.py](analyze_gpu_sampling.py), metric recomputation and plots;
- [GPU_NUMERICAL_CODE_CHECK.md](GPU_NUMERICAL_CODE_CHECK.md), equation and evidence audit.

The main runner SHA-256 is
`2721dc8fb8f569ff6296267c4426c9ba153c49b0697734acf889867cce263bfc`;
the sampler hash is
`f3199851e30e267bab005b06ccf16f68f05b0307695d9d4cbca64aa2ddc28f02`.
Every run archives the exact used source copies, full command arguments,
library/device settings and source hashes. The pilot used an earlier runner
with identical equations; the subsequent revision added partial-output
preservation, raw training predictions and a detached debug norm only.

From the repository root, use the Miniconda interpreter and fresh output
directories. The actual primary commands, run concurrently on the two GPUs,
were:

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/gpu_sampling_experiment.py --mode run --device cuda:0 --angle 90 --output data/generated/closure_sampling_20261003/gpu_sampling_20261003_main_orthogonal
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/gpu_sampling_experiment.py --mode run --device cuda:1 --angle 60 --output data/generated/closure_sampling_20261003/gpu_sampling_20261003_main_nonorthogonal
```

The runner refuses an existing output directory. Reproduction therefore
requires different output names. Pilot and refinement commands are in their
`provenance.json` files; the fine pilot used dt=.1, panel=514,
panel-offset=1 and observe-every=.5. The panel contains the original angles
at its even indices, so the resolution comparison uses exact matched points.

Raw output roots are the two directories above, plus
`gpu_sampling_20261003_pilot_coarse`, `gpu_sampling_20261003_pilot_fine`,
and `gpu_sampling_20261003_refine_2048` under the same generated namespace.
Each main and refinement case retains predictions, signed training predictions,
losses/feature diagnostics, final reduced restarts, setup diagnostics and file
hashes. The earlier pilot archives omit signed training predictions.

The derived tables, all 216 comparisons, both refinement records, summary
JSON and PNG/PDF figure are in
`data/generated/closure_sampling_20261003/gpu_sampling_20261003_analysis/`.
Recompute them with the analysis script's `analyze` and `validity` subcommands,
whose `--help` and archived invocation record specify their arguments.

The bounded test is finished. The retained result is a concrete practical
accuracy limitation, not a negative theorem about coordinated sampling or
an estimate of the optimal logarithmic exponent. No manuscript, maintained
code, other study, Git index, commit or remote was changed.
