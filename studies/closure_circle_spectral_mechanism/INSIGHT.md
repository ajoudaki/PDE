# Closure order, angular spectrum, and learned feature geometry

2026-09-14. Internally checked theory and an exploratory, bounded numerical study. Inputs are maintained repository theory/code and this study's new artifacts. This report does not import another study's experiments and does not promote its findings to established material.

Follow-up: the user subsequently requested actual-network validation. [NET_COMPARISON.md](NET_COMPARISON.md) adds20 dense-network runs, their tanh–sine fits and direct closure errors. References below to lacking a finite-network comparator describe this original first pass; they do not describe the completed follow-up.

The strongest principle supported here is: **closure order resolves interactions in the initialized population; input geometry and nonlinear feature adaptation determine the angular functions those interactions produce.** Fourier analysis makes the resulting shapes intelligible, but N is not a Fourier cutoff. N1 already supports sharp, saturated transitions and higher odd harmonics. N3 and N5 enrich the population interactions governing those transitions; they need not increase angular bandwidth.

We ran75 trajectories, covering15 data configurations with2–4 equally weighted inputs on the circle, plus quadrature/time-step controls. The outputs are real-valued regression predictions, with no sign applied to their plotted values. All trajectories mildly settled at T100–120, with training MSE at most1.31e-10. The nonlinear endpoints below mean these finite settled observations. Frozen-kernel endpoints are computed analytically at infinite time, so their comparison does not penalize slow kernel learning.

## What the two-point experiment reveals

Write u_theta=(cos theta,sin theta). The two data points have angles mu−delta/2 and mu+delta/2, with labels−A and+A. The main sweep uses mu=45degrees, A=1, and delta=15,30,60,90,150degrees. We also rotate selected pairs and repeat them at A=.2.

For a stationary frozen initial tangent kernel k, put D_delta=k(0)−k(delta). Its exact fitted output is

\[
 f_{\mathrm{NTK},\infty}(\theta)
 =A\frac{k(\theta-\mu-\delta/2)-k(\theta-\mu+\delta/2)}{D_\delta}.
\]

With the unhalved probability-weighted square loss used here, its time-dependent output is this same shape times 1−exp(−D_delta t). This stationary balanced pair has no change in normalized shape during frozen-kernel training.

If hat k_m is the complex Fourier coefficient of k, then

\[
 \widehat f_m=-2iA e^{-im\mu}\widehat k_m
 \frac{\sin(m\delta/2)}{D_\delta}.
\]

Thus even the frozen baseline changes spectrum when the sample spacing changes. However, the initial kernel strongly weights the first harmonic. At15degree separation the fitted NTK output has99.419% of its angular energy in the first harmonic. It fits the nearby opposite labels through a large excursion elsewhere on the circle.

The nonlinear closures use a different shape. Define the normalized RMS angular frequency

\[
 k_{\mathrm{rms}}=\sqrt{\frac{\sum_m m^2|\widehat f_m|^2}{\sum_m|\widehat f_m|^2}}
 =\frac{\|f'\|_2}{\|f\|_2}.
\]

The15degree pair gives:

| Model | k_rms | Energy in harmonics m≥3 | Maximum absolute output |
|---|---:|---:|---:|
| Frozen population NTK |1.023|0.581%|5.633|
| N1 |1.673|10.145%|1.560|
| N3 |1.687|10.245%|1.542|
| N5 |1.688|10.262%|1.542|

These are observed values at this spacing; paired numerical refinement is available at30 and90degrees, not15degrees. The analogous30degree learned/frozen distinction is well resolved by those controls.

The first harmonic alone can interpolate any such pair:

\[
 f(\theta)=A\frac{\sin(\theta-\mu)}{\sin(\delta/2)}.
\]

Its maximum is A/sin(delta/2), diverging as the labels approach. Therefore closely spaced opposite labels force a steep slope, but they do not alone force high normalized frequency. One must measure amplitude as well. For any continuously differentiable antipodally odd interpolant, short-arc Cauchy–Schwarz and the opposite arc imply

\[
 k_{\mathrm{rms}}\|f\|_2=\|f'\|_2\ge\frac{2A}{\sqrt{\pi\delta}},
\]

where delta is in radians and the circle L2 norm uses normalized angular measure. A bounded output amplitude or energy then forces increasing frequency as separation shrinks. This is an amplitude–frequency constraint with no N in it.

## A simple reconstruction of the learned curve

The following one-parameter family interpolates the two labels exactly:

\[
 f_\kappa(\theta)=A\frac{\tanh\!\left(\kappa\sin(\theta-\mu)\right)}
 {\tanh\!\left(\kappa\sin(\delta/2)\right)}.
\]

Small kappa approaches the large-amplitude sinusoidal interpolant. Increasing kappa creates a steep central transition and flatter outer lobes. This describes the measured nonlinear endpoints well. Across all four orders in the main unit-amplitude,45degree-midpoint spacing sweep, an interleaved circle grid gives relative reconstruction RMS error between0.34% and2.62%. At15degrees N1 has kappa=5.989 and2.20% error; N5 has kappa=6.089 and2.20% error. At150degrees the corresponding kappas are1.450 and1.188, with0.71% and0.34% error.

The reconstruction was fitted to720 samples of the already learned output and checked on the other720 samples. It is a compact description, not a new predictor learned only from the two training labels, and not a theorem identifying the endpoint. In particular, the dynamics selecting kappa remain unresolved. The9th-order odd Fourier reconstruction at15degrees has approximately4.2–4.4% error, illustrating that a nonlinear one-parameter description can be more economical than a short angular Fourier truncation.

At30degrees, reducing labels from±1 to±.2 changes the learned curve even after dividing out the label amplitude: relative output differences are43–45%, and unit-RMS shape differences are13–14%. A frozen zero-initialized kernel is exactly linear in labels and cannot have this amplitude dependence. These amplitude cases did not receive their own refinement controls, so they are supporting observations rather than the strongest resolved numerical witnesses.

## What N actually retains

Let z label the lower initialized population and xi the upper population. Let b_N(z) and beta_N(xi) be the fixed normalized mark dictionaries. With expectations over the respective populations, the predictor has the exact form

\[
 a_t^{(N)}(\theta)=\mathbb E_z\!\left[b_N(z)\tanh\bigl(w_t(z)\cdot u_\theta\bigr)\right],
\]
\[
 f_t^{(N)}(\theta)=\mathbb E_\xi\!\left[c_t(\xi)\tanh\!\left(
 \beta_N(\xi)^\top M_t^{(N)}a_t^{(N)}(\theta)\right)\right].
\]

The raw dictionaries span polynomials of total degree at most N in bounded coordinates of the initialized marks: four lower coordinates and two upper coordinates. They are ridge-normalized. The moving w and c themselves are not degree-N polynomial approximations. The finite middle action is B2 M B1*, where B1* takes moments against b_N and B2 synthesizes a population function from beta_N. This compresses the interaction between populations; it does not impose a maximum theta frequency.

Under exact sign symmetry, only odd mark degrees are active:

| Order | Active mark degrees | Lower / upper active dimensions |
|---|---|---:|
| N1 |1|4 /2|
| N2 |1|4 /2|
| N3 |1,3|24 /6|
| N5 |1,3,5|80 /12|

The N2 statement requires exact sign-symmetric integration and the same ridge as N1. The maintained implementation uses different ridges and finite, non-sign-paired quadrature. Accordingly exact numerical equality is not asserted, but all seven main pair geometries give N1/N2 relative circle discrepancies at most0.0105%.

Every state is antipodally odd in its input: f(theta+pi)=−f(theta). Therefore all even angular harmonics vanish for every order. But compositions of tanh generate arbitrarily high odd harmonics already at fixed N. THEORY.md gives an explicit representable-state construction; it does not prove that every such state is reachable by training from the prescribed initializer.

The natural candidate criterion for order sufficiency concerns unresolved mark dependence in the forward activations and backward sensitivities. Larger N can capture interactions those quantities have with cubic and quintic mark functions. A high-frequency angular output can nevertheless arise from a few mark channels. Conversely, correcting unresolved mark interactions can change low-frequency amplitudes, phase relationships and hidden geometry. An a priori endpoint error bound from these proposed resolution measures has not been proved here.

## Evidence that the feature geometry changes

Each closure satisfies an exact evolving-kernel equation

\[
 \dot f_t(\theta)=-2\sum_a p_a K_t(\theta,\theta_a)
 \bigl(f_t(\theta_a)-y_a\bigr),\qquad K_t=K_{c,t}+K_{w,t}+K_{M,t}.
\]

All three blocks are positive semidefinite, as derived with the actual population gradient metric in THEORY.md. Only the readout block is nonzero at initialization. Freezing each closure's own initial kernel separates nonlinear feature adaptation from differences in the initial approximations.

For the30degree pair, learned versus own-frozen fitted outputs differ by53–55% relative circle RMS. Even after each output is divided by its own RMS, shape discrepancies are24–25%. Quadrature refinement changes the nonlinear outputs by at most0.12%, and halving the time step changes them by at most0.000031%. Thus an initial-kernel discrepancy or a pure gain adjustment does not explain the observed learned shapes.

The Gram matrices show the corresponding hidden change directly. Normalize their off-diagonal entry by the square root of the two diagonal entries. For N1 at30degrees this hidden-activation cosine changes approximately

| Layer | Initial | Final |
|---|---:|---:|
| First hidden layer |+0.85|+0.17|
| Second hidden layer |+0.82|−0.79|

Nearby inputs become much more distinguishable in the first layer and nearly opposed in the second. This supports a mechanism of a localized transition in learned feature coordinates. It does not establish an endpoint variational principle favoring minimum overshoot.

The Fourier representation of the tangent kernel changes as well. At30degrees its off-diagonal squared-Frobenius fraction grows from0.055–0.250% initially to62–64% finally for N1,N3,N5. This measures departure from stationarity of the kernel itself. Sparse-point supervision already couples Fourier modes through its nonuniform data measure, even when the underlying frozen kernel is stationary; those two sources of coupling should not be conflated.

## Three/four points and the limits of a frequency hierarchy

We tested three alternating labels at spacings20,40,60degrees and four alternating labels at15,30,45degrees. Additional lobes and harmonics appear under all orders. For example the N1 three-point40degree curve has88.3% of its angular energy above the fundamental. The numerical size of that particular curve's order difference is provisional because its quadrature check fails.

Four points15degrees apart give k_rms=2.613,2.765,2.967 for N1,N3,N5: increases of5.8% and7.3%. This is an exploratory witness for the user's frequency hypothesis, but this geometry lacks the matched refinement controls required for a resolved hierarchy claim. Four points30degrees apart instead give2.782,2.770,2.817, with complete passing controls. No pair spacing meets the preset5% increase criterion at both order transitions. At wider pair spacings the small observed changes can even decrease with N. These results support geometry-dependent redistribution of angular energy rather than a universal monotone bandwidth rule.

The strict architectural interpretation “N1 only represents the first angular harmonic, N3 only up to3, N5 only up to5” is excluded by the theory and by resolved tails beyond those orders at30degrees. The weaker hypothesis “higher N usually fits actual-network endpoints better” remains a different question: there is no finite-width network reference in this first pass and no ground-truth labels away from the observed atoms. Less overshoot is a measured geometric property, not by itself superior generalization.

## Evidence, limits and artifacts

The frozen PLAN.md specifies all75 runs, stopping, controls and claim thresholds. All75 saved endpoints replay through the maintained NumPy implementation with maximum absolute error5.33e-15; kernel formulas, gradient metric, restart and analyzer synthetic tests also pass. These correctness checks do not guarantee quadrature resolution. Two of13 quadrature controls exceed the preset2% relative circle tolerance: three-point40degree N1 (4.18%) and N5 (2.57%). The remaining quadrature checks and all10 time-step controls pass. There was no post hoc extra simulation to repair or hide these failures.

Changing pair orientation produces smaller but nonzero differences in the fixed coordinate-anchored closure dictionary: raw curve discrepancies are approximately2.6–2.8% for N1 and0.7–1.0% for N3/N5 in the tested cases. Since only one orientation received refinement controls, rotational bias reduction remains a qualified observation. Rotating the full initialization together with the data is a different, covariant experiment.

N=0 is not the maintained NTK: the API does not support it, and a hypothetical constant-only closure would remain at zero under this initializer. All figures use an independently derived, properly normalized population initial tangent kernel as the NTK comparator.

The full [figure report](../../data/generated/closure_circle_spectral_mechanism/plots_final/spectral_mechanism_report.pdf), [numerical summary](../../data/generated/closure_circle_spectral_mechanism/campaign_001/analysis_final/summary.json), [NumPy replay verification](../../data/generated/closure_circle_spectral_mechanism/verification_final/verification.json), [closure derivation](THEORY.md), [NTK derivation](NTK_THEORY.md), and [internal synthesis audit](SYNTHESIS_AUDIT.md) retain the evidence and exact hypotheses. The useful new explanation is the amplitude–frequency tradeoff produced by learned hidden geometry, with N resolving the population interactions behind that geometry. The law selecting the final shape within this nonlinear family remains open.
