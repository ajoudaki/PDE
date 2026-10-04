# Scoped check of fixed hard clipping

Date: 2026-10-01. Internal mathematical check, not promotion review.

## Verdict

The exact recursively **hard-clipped** order-one tanh closure supports the partial results claimed in the three reviewed notes. I found no substantive gap in their deterministic fitting theorem, all-time initialization stability and centered root-width concentration, or construction and qualitative all-time identification of the closure's own population predictor. The abstract rate-transfer lemma initially omitted regularity hypotheses; its final version now explicitly assumes local absolute continuity and an almost-everywhere differential inequality, resolving that issue.

The requested all-time root-width error to one fixed population predictor remains unproved. The missing estimate is quantitative population bias, or an equivalent quantitative comparison for the reused Gaussian action uniform under mesh refinement. Neither concentration nor qualitative population identification supplies it. This is an unresolved proof obligation, not a disproof of the proposed rate.

The centered root-width assertion covers a fixed query, and the integrated all-time test metric for laws with a finite fourth input moment. The qualitative own-population assertion covers finite second input moments. No reviewed argument establishes the root-width assertion for every finite-second-moment test law, an all-time unconditional finite-width mean bound, or a spatial supremum over a continuum of test inputs.

## Input scope and actual coverage

I read the complete final versions of `FITTING_AND_THRESHOLD.md`, `CONCENTRATION_ROUTE.md`, and `CLIPPED_POPULATION_ROUTE.md`. The concentration note was read only after its hard-clipping correction; its hash was checked before and after review. Thus no result for a smooth tanh cap was accepted as a result for hard clipping.

I read the required `/etc/codex/skills/solve-math-rigorously/SKILL.md`; all of `docs/notation.qmd`, `paper/results.tex`, and `paper/proof_alltime.tex`; the setting and order-one raw-moment/reconstruction passages in `paper/main.tex` (lines 175–218 and 292–389); the complete exact-conditioning passage, fixed-program coupling/concentration/stopping and continuation discussion in Sections 5.9–5.11, and contained probability/continuity specializations A.1–A.4 in `docs/02-gaussian-reuse.qmd`; and the complete arctangent Sections 3–4 in `docs/03-local-population.qmd` (fixed-mesh identification, common actions, clipped flows). The actual Gaussian-reuse reads were lines 106–205 and 1208–1888; incidental boundary text adds no proof dependency.

The arctangent passages were checked as a construction method. Their different activation, depth, clipping placement, and clock were not imported as a theorem for the present dynamics. The complete generic fixed-Gaussian-computation lemma and proof in `paper/proof_alltime.tex` supply the fixed-program dependency directly. The separate strict-rank theorem behind the quantitative feature-ascent example is not needed here; I checked the displayed inverse/Schur dependence of that example's quantitative argument, not its entire earlier strict-rank proof.

I did not read this study's README, `THRESHOLD_ROUTE.md`, `RESULT.md`, another study, another review, archived material, or Git history. No numerical experiment or Git operation was performed. My only write is this report. In particular, reading the whole all-time appendix does not certify the manuscript's unmodified all-order theorem or its separate tracking proof; those are outside this check's conclusion.

## Model and deterministic fitting

The manuscript's degree-zero moment equations give exactly

\[
k_a=\bar h_{a,0}/\tau,\qquad v_a=-2\bar\delta_{a,0},\qquad
B=W_0+\frac1{mn}\sum_a v_a k_a^T,
\]

with \(\dot k_a=(\rho/\tau)(h_a-k_a)\), \(\dot v_a=-2r_ad_a\), and \(\dot\tau=\rho\). There is no missing clock factor. The reviewed modification is

\[
d_a=C_M(w\operatorname{sech}^2 z_a),\qquad
\ell_a=C_M(\operatorname{sech}^2(Au_a)B^Td_a),
\quad C_M(s)=\max(-M,\min(M,s)).
\]

Products are coordinatewise where appropriate. Residuals multiply these fields only in the update equations. The matrix used backward is the actual transpose of the reconstructed forward matrix. The zero initial readout and values, matching keys, and clock one agree across all three notes.

The hard-clipping inequality is valid, including at its corners:

\[
|C_M(p\operatorname{sech}^2z)-C_M(p'\operatorname{sech}^2z')|
\le |p-p'|+2M|z-z'|.
\]

At fixed \(p\), the map is locally absolutely continuous; its derivative is bounded by \(2M\) outside saturation and vanishes inside saturation, almost everywhere. At fixed \(z\), it is 1-Lipschitz in \(p\). Consequently its Nemytskii map is globally Lipschitz in the corresponding product of \(L^2\) spaces. This special relative gate-derivative bound is not implied merely by a bounded Lipschitz activation derivative.

I checked all constants in the fitting note. In particular, the useful averaged bound is

\[
\frac1m\sum_a\|v_a\|_\infty
\le4\int_0^t S(s)\frac1m\sum_a|r_a(s)|\,ds
\le2S(t)^2.
\]

It yields \(\|B-W_0\|_F\le2S^2\), without the weaker extra factor \(\sqrt m\). With \(D=K_0+2\), the bounds

\[
\|\dot B\|_F\le8S\rho,\qquad
\max_a\|\dot g_a\|_2/\sqrt n
\le C_hS\rho,\qquad C_h=8+4X^2D^2
\]

are correct on \(S\le1\). Gram subtraction gives \(\|\Gamma_w(t)-\Gamma_w(0)\|_{op}\le C_hS^2\). The exact prediction equation contains the hidden-motion term; it is not treated as a positive gradient Gram:

\[
\dot r=-2\Gamma_wr+e,\qquad \|e\|_m\le2C_hS^2\rho.
\]

Thus \(\dot\rho\le(-2\lambda+4C_hS^2)\rho\). The declared
\(s_* =\min\{1,\sqrt{\lambda/(4C_h)}\}\) and
\(Y\le\lambda s_*/2\) give \(\rho\le Ye^{-\lambda t}\) and \(S\le Y/\lambda\le s_*/2\), excluding the provisional stopping boundary. The locally Lipschitz vector field, the lower bound \(\tau\ge1\), and the integrable block velocities justify global continuation and convergence of all blocks. Zero residual is a state equilibrium; the \(Y=0\) case is stationary.

Finally, \(\|w\|_\infty\le2Y/\lambda\) proves exact inactivity of the upper hard clip at every \(M\ge2Y/\lambda\). Since \(s_*\le1\), \(M=1\) suffices under this fitting restriction. This statement gives no inactivity guarantee for the lower transpose field. The sensitivity proof may require a further reduction of the small-label/activity threshold; the explicit fitting threshold alone is not claimed to imply every sensitivity constant.

## Stability, velocity kernels, and centered concentration

Direct differentiation verifies every normalization in the concentration note's residual kernel identity. Writing \(p_b=w\operatorname{sech}^2z_b\) for the ordinary, unclipped output derivative, the first-layer term is

\[
K^A_{ba}=(u_a^Tu_b)\frac1n
p_b^TB(\operatorname{sech}^2(Au_b)\ell_a).
\]

The value term comes from \(\dot v_a=-2r_ad_a\), and the clock/key term from \(\dot k_a=(\rho/\tau)(h_a-k_a)\). In particular, clipping the training field does not permit replacing \(p_b\) by \(d_b\) when differentiating the prediction.

The claimed kernel Lipschitz bound is sound. For the potentially dangerous first-layer contraction, one changes factors in the displayed order, using \(\|w\|_\infty\le2s_*\), \(\|\ell_a\|_\infty\le M\), bounded \(\|B\|_{op}\), and the hard-clipping inequality. This avoids an unsupported coordinate bound on \(B^Tp_b\). Its magnitude is \(O(s_*^2)\); the other hidden term is \(O(s_*^2)\), and the key term is \(O(s_*^3)\). Hence the readout Gram retains a coercive term in the equation for the residual difference after making the activity threshold smaller if necessary.

The pairwise inequalities

\[
D'\le C_M\rho^1(D+\varepsilon)+C_MR,
\qquad R'\le-\kappa_1R+C_M\rho^2(D+\varepsilon)
\]

are therefore justified for the two trajectories on the good event. Integrating the second first and then applying Gronwall to the first uses finite residual activity and gives a constant independent of physical horizon. Its convolution form also yields \(R(t)\le C_M(1+t)e^{-ct}E(0)\). The initial metric is at most \(C/\sqrt n\) times Euclidean distance in the standard Gaussian roots \((A_0,G_0)\).

Replacing the output index by a passive query gives a prediction Lipschitz factor \(1+\|x\|/\sqrt d\), but the direct velocity Lipschitz bound contains \(1+\|x\|^2/d\). The second factor of \(\|x\|\) can arise from changing the first activation gate in \(K^A_{xa}\). The report correctly retains this distinction instead of silently using a second-moment assumption for its fourth-moment conclusion.

The good event has complement probability \(O(n^{-1})\): bounded iid first-feature moments give mean-square covariance error \(O(n^{-1})\); conditioning on the first matrix gives the same second-layer covariance error; bounded Hessians of products of tanh make the Gaussian covariance map Lipschitz even at singular covariances by regularization. Markov's inequality then gives the Gram margin, while A.3 supplies the matrix-norm probability bound.

The extension step also checks out. For all sufficiently large widths the good set is a nonempty closed subset of finite-dimensional Gaussian root space. A fixed countable dense subset gives a jointly measurable scalar McShane extension of the prediction velocity. Clipping this extension to its deterministic integrable-in-time velocity bound preserves both its exact values on the good set and its Lipschitz constant. The root space dimension does not enter Gaussian Poincare's constant. The contained Ornstein–Uhlenbeck proof applies to the bounded Lipschitz extended velocity after smooth convolution.

Integrating the centered extended velocities and using Minkowski gives

\[
\mathbb E\sup_{t\ge0}|F_n^{ext}(t,x)-c_n(t,x)|^2
\le\frac1n\left(\int_0^\infty L_x(t)\,dt\right)^2.
\]

This proves the time supremum without an invalid union bound over time or an unproved vector-valued concentration statement. The extension agrees with the actual flow on the good event because both start at zero prediction. Its center differs by \(O(n^{-1})\), uniformly in time at fixed query, from the actual mean conditional on the good event. The asserted conditional root-width estimate follows. Fixed-horizon unconditional means are controlled by the global finite-time bound \(|f_n(t,x)|\le Y(e^{2t}-1)\); that bound does not give an all-time unconditional mean estimate.

## Own population construction and qualitative width limit

The construction's use of the fixed-program theorem satisfies its hypotheses. The Gaussian first rows are independent iid roots, the middle matrix is independent of them and reused in both orientations, and the scalar coefficients are frozen at causally determined population values. Rational linear combinations, smooth bounded coordinate instructions, approximations to the globally Lipschitz hard-clipped map, and finite unions form a countable instruction collection.

The complete conditioning proof in the all-time appendix treats singular covariance by adding independent query noise, taking the width limit first, and then removing noise by same-array operator stability and covariance-square-root continuity. No continuity of a pseudoinverse is assumed. It is sufficient for qualitative convergence, with no claimed noise-uniform width rate.

Passing finite operator inequalities to finite generated spans and then completing gives bounded common forward and reverse actions. Including a dense family of bounded functions of finite node tuples makes those spans dense in the generated \(L^2\) spaces. Passing the finite transpose pairing identity establishes actual Hilbert adjunction. The reverse action is not an independently resampled Gaussian map.

For the present order-one closure, the learned action is a finite sum \(m^{-1}\sum_a v_a\otimes k_a\). Rank-one subtraction bounds it in operator norm on bounded state sets. The hard-clipping inequality controls both backward maps directly in \(L^2\), including unbounded incoming carriers. The residual and prediction maps are locally Lipschitz there. Thus contraction of the integral equation gives a unique local strong solution; finite activity and the same deterministic fitting bounds make it global and convergent. Strong chain rules only along the resulting curves are required, not unrestricted Fréchet differentiability of a nonlinear activation map on all of \(L^2\).

At a fixed physical horizon and fixed mesh, the frozen-coefficient Euler oracle is a finite Gaussian program. Its finitely many contraction errors vanish by joint second-moment convergence. The displayed pairing difference bound and finite instruction induction transfer this to actual empirical Euler feedback. Uniform local Lipschitz and speed bounds then supply the ordinary \(C_{M,T}\Delta\) Euler error, uniformly in width on the initialization event. Taking width first and then refining the mesh identifies the compact-time flow. Uniform approximation of the globally Lipschitz hard-clipped map by smooth maps removes its corners with the same Lipschitz bound. None of these passages needs a quantitative bound uniform over the number of Gaussian instructions.

A fixed passive query requires finitely many additional forward instructions. Its exponential velocity tail has factor at most \(C(1+\|x\|/\sqrt d)\), so truncating physical time upgrades compact-time convergence to the all-time metric. For a law of finite second moment, this deterministic square-integrable envelope, boundedness on the good event, and convergence in probability give the stated integrated qualitative limit. The width limit is the deterministic population predictor of this particular clipped closure, not automatically the dense-training population or the unclipped closure's population.

As a further qualitative consequence of the two valid partial results, the extension centers do converge to this population predictor: the extension's contribution off the good event is controlled by its deterministic envelope and the vanishing event probability, while on the good event it is the actual flow. Boundedness and the qualitative limit give convergence of its expectation in the all-time test norm. This proves only \(c_n-f_M=o(1)\), without a numerical rate.

## Blocking gaps and boundaries

The exact decomposition is

\[
f_{n,M}-f_M=(f_{n,M}-c_n)+(c_n-f_M).
\]

The first term has the verified centered root-width bound in the stated query class; the second has only qualitative convergence. A deterministic displacement \(n^{-1/4}\) can coexist with centered fluctuations of order \(n^{-1/2}\), so substituting qualitative convergence for a bias estimate is logically invalid. This observation does not construct a counterexample to the neural dynamics.

Finite activity controls amplification of an available source error. It does not bound the source error created by reused Gaussian actions. The abstract rate-transfer lemma now has sufficient regularity, and its integration and Gronwall steps are correct, but no compatible finite/population source estimate satisfying its root-width premise has been supplied.

The history-Gram objection is also correct and appropriately limited. For adjacent history columns,

\[
\lambda_{min}(G_\Delta)
\le\tfrac12\|H(t+\Delta)-H(t)\|_2^2
\le\tfrac12L^2\Delta^2.
\]

The reviewed quantitative fixed-program route uses inverse-Gram and inverse-Schur constants. Consequently a fixed positive clipping cap does not by itself make that route uniform as the mesh tends to zero. Discarding exactly dependent columns does not handle nearly dependent ones. This blocks the cited proof technique, not every possible proof of root-width bias.

The strongest verified conclusion is therefore: fixed positive hard clipping, including the width-independent choice \(M=1\), gives a well-defined small-label order-one dynamics with uniform fitting, a unique own population limit, qualitative all-time prediction convergence, and all-time root-width fluctuations around suitable finite-width deterministic centers. Quantitative convergence to the fixed population remains open. These arguments also do not establish universal nonzero feature motion for all data and labels; in particular zero labels give the stationary solution.

## Final source fingerprints

SHA-256 hashes below refer to the reviewed final contents; full-file hashes do not mean that unassigned passages were read or certified.

```text
edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2  FITTING_AND_THRESHOLD.md
4331e895f388b238ced358cfa101390b80681c3797fa36b5b8ba7e319312d8f5  CONCENTRATION_ROUTE.md
63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082  CLIPPED_POPULATION_ROUTE.md
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1  paper/results.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92  docs/02-gaussian-reuse.qmd
3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd  docs/03-local-population.qmd
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7  /etc/codex/skills/solve-math-rigorously/SKILL.md
```
