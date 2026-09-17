# Actual wide networks against the H4 observable computation

This completed experiment was moved into its own study at the user's request. The [study README](README.md) gives current locations; [RELOCATION.json](RELOCATION.json) maps historical paths and hashes. All original run files and the frozen plan remain byte-identical. The exact original six source/report files are retained in [the original-source archive](WIDE_GPU_20260914_ORIGINAL_SOURCES.zip); this report updates navigation and reproduction instructions only.

The requested GPU experiment is complete. At the tested resolutions, the order-5 closure gives closely matching loss and predictions, and a close first-hidden-layer RMS curve. Its second-hidden-layer activation RMS remains about 0.013 below the width-8192 mean at the largest discrepancy; its movement from initialization is underestimated by up to 0.0234. Increasing closure order from 1 to 3 to 5 improves these observed comparisons. These are measurements against actual finite networks, not an infinite-width accuracy certificate.

All 16 declared network trajectories and all eight closure trajectories completed. The network campaign took 236.52 seconds on two RTX 3090 GPUs; the concurrent closure campaign took 127.63 seconds. All saved-data validation passed. The complete reproducible evidence is in [the generated run](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/), with [machine-readable comparisons](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/comparison.json) and seven CSV tables.

## Contract and matched systems

The user's 2026-09-14 request authorized an actual wide-network comparison on the same data, using this machine's GPUs. The [frozen plan](WIDE_GPU_20260914_PLAN.md) preceded implementation and scientific trajectories. This study-owned experiment does not change or promote the maintained book or APIs.

The finite model is the original bias-free two-hidden-layer tanh network:

\[
 u=x/\sqrt2,\qquad
 h^1_n(t,u)=\tanh(W_1(t)u),\qquad
 h^2_n(t,u)=\tanh(B(t)h^1_n(t,u)),\qquad
 f_{n,t}(u)=\frac1n c(t)^\top h^2_n(t,u).
\]

Independent Gaussian initialization has variances 1, 1/n, and 1/n² for W1, B, and c respectively. The weighted unhalved loss is

\[
 \mathcal L_n(t)=\sum_a p_a(f_{n,t}(u_a)-y_a)^2.
\]

All three blocks evolve with gradient-flow mobilities (n,1,n). Dense matrices are stored and trained without a frozen kernel, matrix approximation, minibatching, bias, clipping, or optimizer adaptation. Explicit Heun approximates this finite gradient flow; the experiment is not a claim about an exact ODE trajectory or a default optimizer's learning-rate convention.

Widths are 2048 and 8192, with seeds 11, 29, and 47 for both data cases. The larger model contains 67,133,440 trainable parameters. Primary runs use float32 with TF32 and reduced-precision accumulation disabled, h=0.01, and T=40. Two width-8192 seed-11 runs halve h; two width-2048 seed-11 runs use float64. Each control retains the same Gaussian draw order, seed, and float64 source-initialization hashes as its baseline. The finite random readout is retained.

The literal H4 archived working inputs, labels, probabilities, and passive circle panel were copied without coordinate changes. The shared [input metadata](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/inputs.json) preserves exact hexadecimal array values and archive provenance; its NPZ SHA256 is `7833fae1371391987845315f76904900c7f1d3c01e6cc27ace709a270651104d`.

- **Axis case:** two orthogonal normalized inputs, labels +1 and −1, equal weights, from archived `atom_n3`. The original theorem-supported positive perturbation radius was unresolved at its working precision, so this working law is exactly the two axes. This experiment does not resolve that positive radius.
- **Arc case:** the archived exploratory radius-1/20 rule, eight midpoint nodes on each arc, 16 equal-weight inputs total, with the original quarter-turn orientation. It is the same fixed finite data law for both methods. No theorem for this resolved positive radius through T=40 is asserted here.

Fresh closures use the maintained initializer and equations, orders N=1,3,5, initialization quadrature Q=1024, population quadrature P=512, and h=0.005. They retain the original order-dependent ridges: 1/4096, 1/16384, and 1/36864 respectively. The supplied epsilon_cov=0.001 is unused by this tanh initializer, as recorded in its metadata. The two additional N=3 controls use Q=2048 and P=1024, preserving that order's ridge. All start afresh. The matching axis N=1/3/5 and arc N=3 baselines reproduce all six original archived observation times exactly, including paired arrays and prediction summaries; the fresh trajectories never consume archived states.

## What is compared

There are 206 shared saved times from 0 to 40, including early times 0.005, 0.01, 0.02, 0.05, 0.1 and every 0.2 thereafter. The h=0.01 networks observe t=0.005 by affine interpolation of their actual Heun endpoints followed by nonlinear field evaluation; this observation never feeds training. Other observations lie on the integration mesh.

The raw hidden activation RMS and paired movement RMS are different observables:

\[
 R_{\ell,n}(t)=\left[\sum_a p_a\frac1n\sum_{i=1}^n h^\ell_{n,i}(t,u_a)^2\right]^{1/2},
 \qquad
 D_{\ell,n}(t)=\left[\sum_a p_a\frac1n\sum_{i=1}^n
 \big(h^\ell_{n,i}(t,u_a)-h^\ell_{n,i}(0,u_a)\big)^2\right]^{1/2}.
\]

Closure versions use their population quadrature weights. Each paired statistic uses its own initialization; there is no matching of individual network neurons to closure particles. Initial raw-RMS differences are included in the comparison. Second and initial/current cross moments are saved to audit the formulas.

Prediction error is computed on the same 128 normalized circle directions, including inputs away from training data. The main metric is the maximum over saved times of the circle RMS difference. Thus a quoted 0.0071 is an absolute RMS in output units, not a relative error near prediction zeros, not the worst individual circle-coordinate error, and not a certified continuous-time supremum. Mean curves average each observable across all three seeds; mean loss is not recomputed from mean predictions. All individual-seed comparisons, pairwise seed differences, width differences, time-integrated RMS, and terminal values remain in the CSVs.

## Observed comparisons

Each entry below is the maximum absolute discrepancy over saved times against the **width-8192 three-seed mean**. N=3 refined doubles both closure quadratures. No unfavorable order is omitted.

| Data | Closure | Circle prediction RMS | Loss | Raw RMS layer 1 | Raw RMS layer 2 | Movement RMS layer 1 | Movement RMS layer 2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Axes | N=1 | 0.028033 | 0.019631 | 0.009564 | 0.041061 | 0.008762 | 0.095133 |
| Axes | N=3 | 0.015846 | 0.017958 | 0.004888 | 0.025802 | 0.005360 | 0.038192 |
| Axes | N=5 | 0.007093 | 0.007285 | 0.002698 | 0.012655 | 0.002545 | 0.023203 |
| Axes | N=3 refined | 0.011578 | 0.011399 | 0.003390 | 0.025503 | 0.004063 | 0.039701 |
| Arcs | N=1 | 0.028177 | 0.019520 | 0.009194 | 0.042823 | 0.008876 | 0.095141 |
| Arcs | N=3 | 0.016008 | 0.017910 | 0.004665 | 0.026093 | 0.005534 | 0.038349 |
| Arcs | N=5 | 0.006811 | 0.007122 | 0.002547 | 0.013008 | 0.002647 | 0.023377 |
| Arcs | N=3 refined | 0.011718 | 0.011348 | 0.003190 | 0.026023 | 0.004206 | 0.039825 |

For N=5, the maximum circle-coordinate differences are 0.020640 and 0.019491 (axes/arcs); time-averaged circle RMS differences are 0.006520 and 0.006287. Against individual width-8192 seeds, the maximum circle RMS ranges from 0.006117 to 0.009204 on axes and from 0.005796 to 0.008795 on arcs. These ranges prevent the seed-mean figures from hiding individual realizations.

Terminal values provide scale for the remaining hidden discrepancy:

| Data | Method | Loss at 40 | R1(40) | R2(40) | D1(40) | D2(40) |
|---|---|---:|---:|---:|---:|---:|
| Axes | Network 8192, seed mean | 1.5271e-12 | 0.701551 | 0.706382 | 0.302829 | 0.430749 |
| Axes | Closure N=5 | 9.2439e-15 | 0.704245 | 0.693766 | 0.301962 | 0.409625 |
| Arcs | Network 8192, seed mean | 2.3747e-4 | 0.706460 | 0.710788 | 0.316215 | 0.440149 |
| Arcs | Closure N=5 | 2.5367e-4 | 0.708836 | 0.697781 | 0.314065 | 0.418892 |

The N=5 second-layer terminal raw RMS is about 1.8% lower, and its terminal movement RMS about 4.8–4.9% lower, than the network mean. N=1's much larger movement discrepancy shows why agreement in training loss alone does not establish agreement of hidden trajectories. Improvement in the maximum-over-time comparisons does not mean every individual quantity improves monotonically: the N=3 arc terminal loss, 2.3866e-4, is closer to the network terminal loss than N=5's value.

![Loss and raw hidden RMS](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/figures/loss_and_hidden_rms.png)

![Hidden movement and prediction errors](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/figures/hidden_movement_and_prediction_error.png)

The horizontal scale expands early physical training time. Dark blue is the width-8192 mean and its range across three seeds; dashed gray is the width-2048 mean. In the rightmost prediction-error panels, blue shading instead shows the largest per-seed circle RMS deviation from the width-8192 mean. The separately saved [terminal circle predictions](../../data/generated/wide_network_closure_comparison/WIDE_GPU_20260914_202109Z/figures/final_circle_predictions.png) show the full output functions on the common panel. All figures also have PDF versions.

## Controls and limits

Finite RHS blocks agree with maintained NumPy velocities and independent weighted-loss autodifferentiation on nonorthogonal data with non-small readout. Maximum tested relative RHS differences are about 3e-16 in float64 and 2e-7 in float32. Weighted gradient energy, matched control initializations, and raw/paired moment identities passed. These fixtures test scaling independently of the small scientific initialization.

All four network time/precision controls pass the declared 0.005 cutoff. Their largest circle RMS discrepancy is 0.000205914 (arc half-step control); the largest hidden movement RMS discrepancy is 0.000127643, and the largest loss discrepancy is 8.31485e-6. These are much smaller than the N=5 second-layer discrepancy. There were no nonfinite saved observations or substantial saved loss increases in any trajectory; this is not a proof of discrete energy monotonicity between observations.

Changing network width from 2048 to 8192 changes the seed-mean circle prediction RMS by at most 0.004327, raw RMS by at most 0.001653, movement RMS by at most 0.007715, and loss by at most 0.007015 across both cases. Pairwise width-8192 seed discrepancies reach 0.005858 in circle RMS, 0.003890 in raw RMS, 0.008399 in movement RMS, and 0.008132 in loss. Two widths and three seeds do not establish that 8192 is the infinite-width limit or provide certified confidence intervals.

Closure quadrature is the material unresolved numerical issue. Doubling Q and P at N=3 changes circle RMS by up to 0.005452 and loss by up to 0.007123, exceeding the plan's 0.005 numerical-control cutoff. Hidden raw RMS changes by at most 0.001981 and movement RMS by at most 0.003049. The N=3 refinement is not an N=5 error bound; no N=5 quadrature refinement was declared or run. Consequently, although the observed N=5 comparisons meet the plan's observable thresholds, the complete frozen agreement verdict remains **inconclusive** under the numerical-control requirement. It would be incorrect to attribute every measured gap solely to closure order, or to claim quadrature convergence.

The definite empirical conclusion is that these computed N=5 curves closely track these actual wide networks, with a visible second-hidden-layer bias. The stronger claim of resolved population-closure accuracy remains open. The bounded campaign is finished; additional width or quadrature campaigns are not silently added.

## Evidence status and update

| Claim | Status | Supporting and limiting evidence |
|---|---|---|
| These N=5 computed loss/prediction/raw-RMS curves are close to these finite networks | Empirically-supported at the tested resolutions | Both matched data cases and all three wide seeds; full saved curves and individual comparisons. Does not certify continuous time or an asymptotic limit. |
| The remaining second-layer movement gap is explained entirely by GPU precision or the tested time step | Strongly-disfavored within the tested controls | Network numerical changes are far smaller than the roughly 0.0234 discrepancy. Precision is controlled at width2048; step size at width8192. |
| The full frozen numerical agreement criterion is established | Inconclusive | N=5 meets observable differences, but N=3 quadrature diagnostic exceeds the numerical cutoff and does not bound N=5. |
| The finite hierarchy and finite network converge to the same continuum limit at a known quantitative rate | Open in this experiment | Neither two network widths nor three closure orders establishes a rate or commuting limits. Existing theorems retain their own stated scope. |

This evidence adds a direct actual-network comparison to the original closure-only H4 tests. It supersedes no theorem or archived result. The causal update is that tiny training loss alone is demonstrably an insufficient diagnostic of hidden accuracy, while higher closure order improves the tested full observables. The most useful unresolved numerical discriminator is a separately planned closure-quadrature refinement at N=5, together with enough width/seed resolution to separate finite-network variation; it was not part of this completed campaign.

## Reproduction and provenance

The [network runner](WIDE_GPU_20260914_NETWORK.py), [closure runner](WIDE_GPU_20260914_CLOSURE.py), [analysis](WIDE_GPU_20260914_ANALYSIS.py), and [plotter](WIDE_GPU_20260914_PLOTS.py) are study-owned. Each execution record preserves configuration and input/output hashes, source hashes, arithmetic, commands, seed, timings, and available environment metadata. Network campaign metadata stores the Git HEAD and dirty-path metadata before full trajectories; unrelated concurrent work is untouched. Root reviewed the finite and closure implementations; a scoped second agent inspected finite scaling and scheduling, and a separate analyst checked saved-data identities and comparison formulas. These checks are not promotion reviews.

Network Python was `/home/amir/miniconda3/bin/python` (3.10.14), with NumPy 1.26.4, PyTorch 2.9.0+cu130, CUDA 13.0, NVIDIA driver 580.65.06, and two 24-GiB RTX3090 GPUs. Closures ran under `/usr/bin/python` (3.10.12), also with NumPy 1.26.4. Aggregate network worker wall time was 443.47 seconds; peak PyTorch allocated memory among runs was 1,889,176,064 bytes (about 1.76GiB). The 32-step timing-only calibration selected the originally declared width8192 branch. No fallback, failed trajectory, extra seed, or outcome-driven configuration selection occurred.

The current closure runner prepares data from the study-owned [exact input specification](WIDE_GPU_20260914_INPUTS.json), without opening the original H4 study archives. Future runs reproduce this experiment's closure trajectories; they explicitly do not repeat the legacy H4 archive-comparison diagnostic. Its completed original checks remain in the unchanged historical records. The evolution, initializer parameters, and observation formulas are unchanged by relocation.

To reproduce into a fresh, empty directory under `data/generated/wide_network_closure_comparison/`, set `WIDE_GPU_RUN` to that directory, create it, and run these commands from the repository root. The GPU command requires an environment with device access. The closure and network campaigns can run concurrently; each has its own bounded supervisor.

```bash
PYTHONDONTWRITEBYTECODE=1 /usr/bin/python studies/wide_network_closure_comparison/WIDE_GPU_20260914_CLOSURE.py --output "$WIDE_GPU_RUN" --prepare-only
CUDA_VISIBLE_DEVICES=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/WIDE_GPU_20260914_NETWORK.py --output "$WIDE_GPU_RUN" --campaign
PYTHONDONTWRITEBYTECODE=1 /usr/bin/python studies/wide_network_closure_comparison/WIDE_GPU_20260914_CLOSURE.py --output "$WIDE_GPU_RUN" --run
PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/WIDE_GPU_20260914_ANALYSIS.py --output "$WIDE_GPU_RUN"
MPLCONFIGDIR=/tmp/pde-wide-matplotlib PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/wide_network_closure_comparison/WIDE_GPU_20260914_PLOTS.py --output "$WIDE_GPU_RUN"
```

The current output directory is immutable experimental evidence; do not use it as the fresh reproduction target. Scientific sources were unchanged during their campaigns. Analysis and plotting are deterministic postprocessing of saved trajectories, apart from timestamps and rendered-file metadata.
