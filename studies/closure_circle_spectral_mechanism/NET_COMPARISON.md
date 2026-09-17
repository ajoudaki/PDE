# Actual networks, the tanh–sine shape, and closure order

2026-09-14. Same-study empirical validation under [NET_PLAN.md](NET_PLAN.md); no promotion to established theory or code.

**The same one-parameter curve describes the actual wide networks well. Moving from N1 to N3 improves agreement in all three tested geometries, while N3 to N5 has a geometry-dependent effect.** At 15° the additional improvement is very small; at 30° the measured error increases slightly; at 90° it decreases. These observations support the shared shape description and the usefulness of higher closure order, but do not establish monotone convergence of the hierarchy.

We trained actual dense, bias-free, two-hidden-layer tanh networks at widths 1024 and 4096, with three independent seeds at each width and separation δ=15°,30°,90°. Two same-seed numerical controls bring the total to 20 trajectories. All mildly settled at physical T=100, with largest training MSE 6.88×10⁻¹². The closure outputs used here are the previously saved N1,N3,N5 predictions for exactly the same data; none was adjusted to the networks. The [four-page figure report](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/network_comparison_report.pdf) displays the raw curves, a circle view, template fits and full-function errors.

## The one-parameter description survives the network comparison

The two labels are −1 and +1 at θ=μ−δ/2 and μ+δ/2, with μ=45°. We fitted

\[
 g_\kappa(\theta)=
 \frac{\tanh\!\left(\kappa\sin(\theta-\mu)\right)}
 {\tanh\!\left(\kappa\sin(\delta/2)\right)},
 \qquad .02\le\kappa\le30.
\]

Only κ was fitted. The phase, label amplitude and separation remain fixed by the data. Each fit uses 720 alternating directions from a 1440-point circle; the remaining 720 directions measure reconstruction error. This heldout panel checks the description of a saved network function. It supplies no new teacher labels and does not turn the template into a predictor trained from the two atoms alone.

| Separation | κ of width-4096 mean | Individual-seed κ range | Mean-curve heldout RMS error | Individual-seed heldout error range |
|---|---:|---:|---:|---:|
| 15° | 6.372 | 6.332–6.395 | 1.797% | 1.769–1.814% |
| 30° | 4.206 | 4.184–4.218 | 1.629% | 1.609–1.651% |
| 90° | 2.151 | 2.138–2.158 | 0.683% | 0.687–0.733% |

Every widest-width seed passes the predeclared 5% reconstruction criterion, with no fitted parameter at its allowed boundary. Fitting the mean curve is performed separately from fitting each seed; its κ is not defined as the average of seed κ values. The closest label pair selects the largest κ, giving a steeper transition and flatter outer lobes in this family. The dynamics selecting κ remain unresolved.

Finite networks can break reflection symmetry around μ, although a bias-free tanh network remains exactly antipodally odd. This is a possible source of template residual, because every gκ is odd under reflection θ↦2μ−θ. For the normalized circle L2 norm, let Rf(θ)=f(2μ−θ) and f±=(f±Rf)/2. Reflection preserves angular measure, and its even and odd eigenspaces are orthogonal: changing variables under reflection changes the sign of the inner product of an even and an odd function. Hence

\[
 \|f-g_\kappa\|_2^2
 =\|f_- - g_\kappa\|_2^2+\|f_+\|_2^2.
\]

The same identity holds on both aligned interleaved panels. It gives the irreducible residual due to reflection asymmetry without fitting a phase. For the width-4096 mean curves, that asymmetry is only 0.048%, 0.055% and 0.072% relative RMS at 15°,30°,90°. It accounts for 0.070%, 0.116% and 1.12% of the corresponding template residual energy. Most of the remaining small residual is therefore a departure of the symmetric network shape from the exact one-parameter family, rather than mean-curve reflection asymmetry.

## Full network functions determine the order comparison

For each network reference f, the primary error is ||f_N−f||₂/||f||₂. A separate shape distance compares f_N/||f_N||₂ and f/||f||₂. No gain, phase or clock is fitted to a closure. Every endpoint here is also a common-T100 comparison; the separate saved T100 measurements agree up to their circle-panel and floating-point evaluation differences.

| Separation | N1 error versus network mean | N3 error | N5 error | Observed N3→N5 change |
|---|---:|---:|---:|---|
| 15° | 3.986% | 2.923% | 2.908% | Near tie |
| 30° | 1.892% | 1.632% | 1.672% | Slight increase |
| 90° | 1.701% | 0.814% | 0.661% | Decrease |

These are the width-4096 mean references. All three seeds individually favor N3 over N1 in every geometry at both widths. Increasing width from 1024 to 4096 changes no mean-error ordering. The [error plot](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/closure_network_errors.png) includes every seed rather than only the mean.

The unit-RMS shape errors at width 4096 are 1.161%,0.952%,0.931% for N1,N3,N5 at 15°; 0.921%,0.819%,0.828% at 30°; and 1.574%,0.729%,0.575% at 90°. Thus gain differences explain part of the raw discrepancy, especially for closely spaced labels, but do not account for all of it.

Comparing fitted κ gives a compatible, less complete picture:

| Separation | Network mean κ | N1 κ | N3 κ | N5 κ |
|---|---:|---:|---:|---:|
| 15° | 6.372 | 5.989 | 6.088 | 6.089 |
| 30° | 4.206 | 4.039 | 4.061 | 4.057 |
| 90° | 2.151 | 2.319 | 2.222 | 2.200 |

At 15° the higher orders move κ toward the network but remain displaced; at 30° N5 is slightly farther away than N3; at 90° both order transitions improve it. Agreement of a fitted scalar alone would not establish agreement of the actual functions, because each template leaves a nonzero residual. The full-function errors above are the evidence for approximation accuracy.

The predeclared hierarchy statistic pairs both closure errors against the same network seed. If E_N,s=||f_N−f_s||₂², its gain is D_s=E_low,s−E_high,s. A transition passes the stated gain gate only when the mean squared error falls by at least 10%, the mean gain exceeds twice its sample standard error, and it exceeds twice the measured same-seed time/precision-control effect. At width 4096 the measured reductions are:

| Separation | N1→N3 mean squared-error reduction | N3→N5 reduction | Predeclared gain gate |
|---|---:|---:|---|
| 15° | 46.00% | 0.96% | First transition only |
| 30° | 25.32% | −4.88% | First transition only |
| 90° | 75.96% | 31.92% | Both transitions |

A positive reduction means improvement. This gate concerns the tested finite networks and measured numerical effects; it is not a convergence theorem. Network step/precision controls were run at 30° only, so their use as a numerical scale at 15° or 90° is a transferred diagnostic rather than a matched check. The N3→N5 transition at 90° also fails the seed-uncertainty gate at width 1024, despite a favorable mean direction there. Its resolution is width-dependent.

Closure quadrature matters for the smaller order differences. At 30°, the doubled-quadrature closures preserve N1>N3 and N5>N3 error for every network seed at both widths, as do the half-step closures. Against width 4096, however, the N1→N3 reduction falls from 25.32% to 18.56%, and the N3→N5 error increase falls from 4.88% to 0.77%. The observed ordering survives these controls; the small N3/N5 difference is not accurately resolved in magnitude. A conservative extra audit comparing gains to twice the sum of the individual closure-control effects leaves the fully controlled-improvement flag false. This extra flag is separate from the predeclared gain gate. There is no matched closure quadrature control at 15°, and the available 90° closure controls refine quadrature but not time step. Accordingly, the evidence supports observed order improvements with these qualifications, not universal monotone approach to an infinite-width target.

## Width, numerical accuracy and evidence scope

The network is

\[
 f_n(\theta)=\frac{c^\top\tanh\!\left(V\tanh(W_1u_\theta)\right)}n,
 \qquad u_\theta=(\cos\theta,\sin\theta).
\]

The physical inputs are x=√2u, so this expression matches the maintained first-layer division by √d. Initialization has independent W1 entries N(0,1), V entries N(0,1/n), and stored c entries N(0,1/n²). Simultaneous Heun approximates gradient flow for the unhalved mean squared loss with block mobilities (n,1,n). Main h=.02 and float32 with TF32 disabled; the retained controls use h=.01 at n=4096 and float64 at n=1024, both for δ=30°,seed1729. The first-layer and readout scaling, dense middle matrix, small random initial readout, and all trained weight blocks are part of the comparison.

The 1024-versus-4096 mean-curve discrepancies are 0.141%,0.065%,0.299% for 15°,30°,90°. At width 4096, the circle RMS of pointwise sample SD, relative to the mean curve RMS, is 0.344%,0.230%,0.256%; the estimated mean standard errors are 0.199%,0.133%,0.148%. These quantify the three available seed realizations. Neither a seed standard error nor a difference between two width means bounds the bias to infinite width. Reusing the same seed numbers at different widths does not make their generated initial matrices a paired-width construction.

For clarity, ensemble error and average seed error are related exactly by

\[
 \frac1S\sum_s\|f_N-f_s\|_2^2
 =\|f_N-\bar f\|_2^2
  +\frac1S\sum_s\|f_s-\bar f\|_2^2.
\]

Expanding f_N−f_s=(f_N−f̄)+(f̄−f_s) proves the formula because the cross terms sum to zero. The reported seed errors retain this finite-seed dispersion; the error of the mean curve does not include it. The analyzer checks this identity numerically.

The network half-step comparison has relative circle RMS 1.67×10⁻⁶; the float32-versus-float64 comparison has 1.22×10⁻⁶. Both are well below the .002 tolerance. The largest observed antipodal-oddness discrepancy is 2.38×10⁻⁷, and the largest relative 1440-versus-720 bandwidth difference is 7.29×10⁻⁹. All saved-array finiteness, source/configuration identities and listed output hashes pass the analyzer checks. The [independent replay verification](../../data/generated/closure_circle_spectral_mechanism/network_verification_main/verification.json) checks all 20 records and initialization digests, and re-evaluates all eight retained final states on all 1440 directions with NumPy: maximum discrepancy 2.51×10⁻⁷. Its additional comparison with the maintained finite-network API on 144 directions has maximum discrepancy 4.44×10⁻¹⁶. The unretained twelve full states could not be independently scanned or replayed, and endpoint checks do not certify every intermediate state or constitute a second training campaign.

The fixed conditional width-8192 branch was recommended because the 30° N3→N5 gain criterion failed. It was not launched: reserving its prescribed 280 MiB from 1.683 GiB free space would violate the plan's 1.5 GiB minimum. This is a resource-limited missing width check, not a failed scientific trajectory. The [branch decision](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/wide_decision.json) records the reason and input hashes; no further training or deletion was performed.

The conclusions are empirical for these three sparse-circle laws, these initializations, two finite widths and T=100. The three chosen separations were fixed before network training. They do not identify an N→∞ limit, justify exchanging width/order/long-time limits, explain the law selecting κ, or measure generalization to an independently specified teacher function. The previously established study observation about closure shape gains an actual-network reference; the prior mark-degree and angular-parity discussion is unchanged.

## Reproduction and ownership

The full machine-readable results are [analysis_final/summary.json](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/summary.json); [curves.npz](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/curves.npz) contains the exact plotted derived curves. The source is [NET_ANALYZE.py](NET_ANALYZE.py), SHA256 `8d222ec78848d23874e50f05877f44b5c0511fa2d62463c162f9feebcc8ccff0`. Its ten deterministic checks pass in [analyzer_selftest_final.json](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analyzer_selftest_final.json): exact and boundary κ recovery, reflection decomposition, separation of gain and shape, ensemble error decomposition, the paired-gain thresholds, and a single-harmonic spectral oracle. Final analysis and all four plots took 7.03 wall seconds; the preliminary analysis took 0.67 seconds.

From `/home/amir/Codes/PDE`, the final analysis was produced by:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  /home/amir/miniconda3/bin/python -B \
  studies/closure_circle_spectral_mechanism/NET_ANALYZE.py \
  --campaign data/generated/closure_circle_spectral_mechanism/network_comparison_001 \
  --output data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final
```

Reproduction must replace the output with a fresh child directory. The program does no training. The companion images are [raw curves](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/network_closure_curves.png), [radial curves](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/network_closure_radial.png), [template fits](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/network_template_fits.png), and [closure errors](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/closure_network_errors.png). Hollow markers on the radial plot identify training directions at the zero-output ring; filled markers show the labels. Signed prediction is the displacement from that ring, avoiding ambiguity about negative polar radii.

Scoped contributor network_circle_analysis owns NET_ANALYZE.py and this report. Scientific inputs read were this study's README, PLAN, INSIGHT and complete relevant ANALYZE code, selected campaign_001 configurations and analysis_final arrays/summary, NET_PLAN, the newly generated network campaign, and the supervisor-supplied final verification report; maintained inputs were docs/NOTATION.md and code/pde/finite_network.py. Required workflow and research/mathematics skills were also read. No other study, task history, or external scientific source was used. Root owns the network producer, main study record and final synthesis. The observations and interpretations here are same-study checks, not an isolated promotion review.
