# Independent source audit: Dynamics of Finite Width Kernel and Prediction Fluctuations in Mean Field Neural Networks

Audited source: Bordelon and Pehlevan, arXiv:2304.03408v3, 7 November 2023; supplied `tp_dmft/fluct2023.pdf`, all 44 pages including Appendices A–N. Important equations were checked in the rendered PDF, including Appendix I.2, p.36. No code was executed or fetched. No existing study findings, manuscript, or another review was consulted. A prior π-limit reading supplied no evidence for this audit; there were no prior findings on this source. The directly cited 2022 DMFT paper and Tensor Programs IV were completely read as separate assigned primary sources, not through another review.

## Assumption ledger and coverage

- **Model:** fixed depth (L), common width (N), fixed input dimension (D), fixed finite dataset of (P) examples; iid standard Gaussian parameter initialization. Internal weights have (N^{-1/2}) normalization, input weights (D^{-1/2}), scalar output (f=(\gamma N)^{-1}w^L\cdot\phi(h^L)). Here (\gamma) equals the 2022 paper's (\gamma_0), not its width-dependent (\gamma).
- **Optimizer:** gradient flow (\dot\theta=-N\gamma^2\nabla\mathcal L), principally square loss; discrete gradient descent is analyzed in a shallow linear special case. Population-risk “online learning” means an exact distributional gradient, expressly excluding SGD sampling noise. Dataset averaging can be incorporated in the error signal or time convention and must be kept consistent.
- **Observables:** normalized feature/gradient kernels and predictions; fluctuations over initialization. Leading covariance is (N^{-1}\Sigma). This is not a pathwise operator-norm approximation bound. “Variance contribution to loss” is a trace of prediction covariance, not generally the statistical variance of the scalar loss.
- **Activation/regularity:** nonlinear formal derivations require derivatives, integrable moments, and a suitable saddle expansion; experiments include ReLU and tanh. No complete rigorous assumptions for the claimed expansion and remainder are furnished. Main §10 explicitly says the argument has physics-level rather than theorem-level rigor.
- **Horizon/limits:** fixed finite training horizon and finite time grid before width asymptotics. The lazy section additionally uses background subtraction. (P/N), (D/N), depth, richness, and long time are not controlled uniformly by the stated inverse-width series. The paper itself demonstrates breakdown as sample count or dimension becomes comparable to width.
- **Reconstructed coverage:** block inversion, causal fluctuation propagation, the lazy covariance solution, initial-output covariance, shallow test-point chain rule, linear fourth moments, discrete two-layer recurrences, and generic saddle-expansion orders. The full deep tensor Hessian was read but not independently certified entry by entry. No claimed empirical curve was reproduced.

## Claim 1 — Propagator formula is useful formal algebra, not the stated real Gaussian over all variables

**Source:** Propositions 1–2, p.4; Appendices D–E, Eqs.25–50, pp.21–29.

For the primal/dual sector with Hessian

\[
H=\begin{pmatrix}0&U^\top\\ U&\kappa\end{pmatrix},
\]

direct multiplication verifies

\[
-H^{-1}=\begin{pmatrix}
U^{-1}\kappa U^{-\top}&-U^{-1}\\
-U^{-\top}&0
\end{pmatrix}.
\]

Thus the physical primal block is a positive semidefinite covariance if (\kappa\succeq0). Equivalently, solving the linear response equation (U\delta q=\xi), with (\operatorname{Cov}(\xi)=\kappa), gives that same covariance. This independently verifies the core covariance-propagation mechanism. The response variables (A,B) require the additional Schur complement actually supplied in Eqs.42–45 and Algorithm 1; the simple block formula alone is not a substitute for it in a deep model.

**Formal versus rigorous:** Appendix D assumes the full action Hessian is negative semidefinite and speaks of a Gaussian over all order parameters. Its own nonzero primal/dual block rules this out on the real space: with a zero primal diagonal block and invertible nonzero (U), the quadratic form (2y^\top Ux+y^\top\kappa y) takes both signs. Dual variables originally live on Fourier/imaginary contours. A contour-integral Gaussian and its physical covariance block are legitimate formal devices; they are not a real joint Gaussian probability distribution with that full inverse Hessian. No contour, concentration, saddle uniqueness, or tail estimates establish the advertised remainder rigorously. This is a substantive assumption mismatch in the exposition, but the paper explicitly qualifies the method as formal, and the checked physical block algebra survives.

**Remainder check:** Proposition 1's statement that truncation linear in the cubic-and-higher remainder (V) contains all leading and subleading terms for any observable is too broad. Consider the ordinary, well-defined one-dimensional Laplace density

\[
p_N(x)\propto e^{N[-x^2/2+a x^3/6-bx^4/24]},\qquad b>a^2/3,
\]

whose unique maximum is zero. For (O(x)=x^2), Gaussian expansion yields

\[
\mathbb E_Nx^2=\frac1N+\frac{5a^2/4-b/2}{N^2}+O(N^{-3}).
\]

The term linear in (V) supplies (-b/(2N^2)), but the omitted quadratic term supplies (5a^2/(4N^2)), at the same subleading order. For a fixed smooth observable with a generic nonzero constant/linear/quadratic expansion, the displayed terms do suffice for the usual absolute (N^{-1}) correction; for covariance, they justify only its leading (N^{-1}\Sigma), not the entire next coefficient. **Minor proposition-scope correction.** The leading covariance order used in the paper remains intact within the formal expansion.

## Claim 2 — Missing finite-width initial-output noise in the advertised general action

**Source:** main Eq.1 and §3, p.3; explicit subtraction in §5, p.5; Appendix E Eq.32/34, pp.23; I.1 Eqs.78–82 and I.2 Eqs.87–90, pp.34–36; compare J Eq.97 and K Eq.122.

The full and shallow kernel-based actions enforce

\[
\Delta(t)=y-\int_0^tK(s)\Delta(s)\,ds,
\]

so their prediction-fluctuation formulas enforce exactly (f(0)=0) and zero initial prediction variance. This is not the finite-width iid-Gaussian network of main Eq.1. Already in one hidden layer,

\[
f_N(x,0)=\frac1{\gamma N}\sum_{i=1}^N a_i\phi(h_i(x)),\qquad
N\operatorname{Cov}(f_N(x,0),f_N(x',0))
=\frac{\mathbb E[\phi(h(x))\phi(h(x'))]}{\gamma^2},
\]

because readout (a_i\sim N(0,1)) is independent of hidden initialization. For linear activation and unit normalized input, this is (1/\gamma^2\), while Eq.82 predicts zero. This discrepancy is at the **leading order being calculated**, not at a discarded higher order.

**Severity: major scope/model mismatch for the claimed general leading-fluctuation recipe.** Background-subtracted training (\widetilde f(\theta)=f(\theta)-f(\theta_0)) has exactly zero initial prediction and makes these initial conditions appropriate, but the paper explicitly introduces that model only in the lazy section. Extending the qualifier to the relevant rich experiments is a possible interpretation, not an established source statement. Alternatively, the action must include the random initial-output boundary source and its joint correlations. The algebraic-output actions of Appendices J/K do include such randomness, demonstrating that the paper contains different boundary treatments. A complete deep correction requires tracking the appropriate joint sources, not merely changing a scalar initial value after the fact.

**Survives:** the zero-initial-output/background-subtracted fluctuation mechanism and the limiting mean dynamics; the counterexample does not refute either. No code audit was authorized/performed, so this report does not assert which convention produced the plots. The issue blocks using Eqs.32/82/90 as a complete initialization-fluctuation result for the unmodified stated rich network.

## Claim 3 — Lazy covariance equation survives; explicit eigenfunction and test formulas need correction

**Source:** Proposition 3 and following paragraph, pp.5–6; Appendix H.1–H.2, Eqs.70–77, pp.33–34; Appendix I.2 Eq.86, p.36.

For the explicitly background-subtracted lazy model, let (K_N=K_\infty+N^{-1/2}Z) and (\Delta_\infty(t)=e^{-K_\infty t}y). The first prediction perturbation satisfies

\[
\delta\Delta(t)=-\int_0^t e^{-K_\infty(t-s)}Z e^{-K_\infty s}y\,ds.
\]

This directly implies Proposition 3's covariance PDE and Eq.75, independently of the path integral. If (y=\psi_j) is a kernel eigenvector, define

\[
F_{kj}(t)=\frac{e^{-\lambda_jt}-e^{-\lambda_kt}}{\lambda_k-\lambda_j},\qquad
F_{jj}(t)=t e^{-\lambda_jt}.
\]

Then (\Sigma_{k\ell}(t,s)=\operatorname{Cov}(Z_{kj},Z_{\ell j})F_{kj}(t)F_{\ell j}(s)). The main-text expression omits the transient subtraction terms; as printed it is nonzero at (t=0) and singular at equal eigenvalues. **Minor explicit-solution error**; the PDE and appendix integral formula supply the repair.

**Independent test-point chain rule:** with one training input (x), test input (x_\star), and (c=x\cdot x_\star/D), a shallow model obeys

\[
\dot h_\star=\gamma\Delta\,c\,z\phi'(h),\qquad
K_\star=\mathbb E[\phi(h)\phi(h_\star)]+c\,\mathbb E[g g_\star].
\]

Eq.86 instead places (\phi'(h_\star)) in the field update and omits (c) from the backward contribution to (K_\star). Both defects were verified in the rendered page. For linear activation at initialization with orthogonal unit-norm inputs, the true (K_\star=0), whereas the printed expression gives (1). **Minor local formula errors with direct consequences for test-prediction calculations if used literally.** They recur in the displayed test action and require consistent repair there. The finite-time test-variance plots cannot be certified from the printed expressions alone; the general covariance-propagation architecture is still reusable.

## Claim 4 — Solvable examples support qualified variance claims, not universal denoising or all-time accuracy

**Source:** §6–§8, pp.6–9; Appendices I.3–M, pp.36–44.

The shallow linear change of variables (v_\pm=(h\pm z)/\sqrt2) gives (\dot v_\pm=\pm\gamma\Delta v_\pm). This verifies the Gaussian solvability and causal kernel sensitivities. In the whitened (P)-sample problem, decomposition into the target direction and (P-1) orthogonal directions explains the trace-of-covariance contribution

\[
N^{-1}\Sigma_y(t,t)+(P-1)N^{-1}\Sigma_\perp(t,t).
\]

Replacing (P-1) by (D-1) in the population linear model explains the analogous (D/N) effect. This is not a uniform proportional-limit theorem and is not a statement about minibatch SGD noise.

**Fourth-moment check:** Appendix J Eq.107 appears to copy the variance of (h^2+z^2) into the variance of (hz). With (a=\mathbb E[v_+(t)v_+(s)]) and (b=\mathbb E[v_-(t)v_-(s)]), independence gives

\[
\operatorname{Cov}(h(t)z(t),h(s)z(s))=\tfrac12(a^2+b^2),
\]

not ((a+b)^2+(a-b)^2=2(a^2+b^2)). At initialization the correct value is (1), while the printed (\kappa_y) is (4). This is a **minor, factor-four local error** in a leading coefficient; the target/orthogonal dimension count survives. The online covariance formula Eq.128 has the correct Wick structure. Main Eq.9 also omits the minus sign in residual decay; its referenced scalar dynamics require (\dot\Delta_y<0) for positive residual.

For discrete shallow linear training, direct expansion of (h_{t+1}=h_t+\eta\gamma\Delta_tz_t) and its symmetric (z) update independently reproduces main Eq.10. In fact these recurrences hold for empirical finite-width (f,K) as well, with random initial conditions; the infinite-width system selects their deterministic limiting initialization. They illustrate possible edge-of-stability behavior but do not guarantee bounded dynamics for every large (\eta\gamma\), nor prove an all-time covariance remainder.

The paper's own Fig.5 shows that stronger feature learning can increase the *absolute* peak prediction variance in deep models, even while normalized kernel signal-to-noise improves. Thus “richer is closer” must specify relative versus absolute error, time matching, and architecture. The scalar lazy correction Eq.77 likewise permits finite width to improve early loss when the mean-kernel correction is positive. These are qualifications present in the source, not contradictions requiring a universal negative result.

Appendix G.2's rate formulation additionally needs its stated commuting-kernel special case for the simplification (\|\Delta\|^2=y^\top e^{-2R}y). In general (T=e^{-R}) need not be symmetric, and the correct expression is (y^\top e^{-R^\top}e^{-R}y). For example successive symmetric positive matrices (\operatorname{diag}(1,2)) and (\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}) do not commute. The general transition-matrix identity survives, but the simplified exponential must not be promoted to arbitrary time-varying kernels.

## Claim 5 — Empirical support and computational cost

**Source:** Figs.2–7 and §10, pp.5–10; Appendices A–B/F/N, pp.15–19,28–29,44.

- Fig.2: shallow ReLU, (N=100), (P=10), (\gamma=0.05), ensemble 500; checks lazy covariance dynamics.
- Fig.3: shallow tanh, one training point and one test point with input overlap (0.5), (N=256), ensemble 1000; studies squared deviations, means, and variances for several richness values.
- Fig.4 explicitly shows the leading inverse-width approximation failing when (P/N) or (D/N) becomes large. Fig.5 uses a depth-four linear network. Fig.6 is a shallow linear large-step example at (N=500).
- Fig.7: six-layer CNN, CIFAR-10, widths 32–256, eight-member ensembles, fixed (\gamma=0.2), MSE. Minibatches of 256 are shared across ensemble members, so the experiment principally isolates initialization differences conditional on the batch sequence. Richness experiments use ten-member ensembles at width 64. Raw learning rates are intentionally rescaled with (\sqrt\gamma\), rather than simply holding the theoretical (\gamma^2\)-rescaled time constant. These are not numerical evaluations of the full deep fluctuation tensors on CIFAR-10.
- The fitted CNN rate is approximately (0.017-0.394/N); a quadratic fit shown is (0.017-0.430/N-6.929/N^2). Such fits support a finite-width rate effect but do not identify a unique microscopic cause, a remainder bound, or an asymptotic theorem. The paper labels the mean-kernel explanation as a hypothesis. Ensembling with finitely many models also leaves residual variance and does not exactly measure the infinite-ensemble bias.

The source explicitly notes (O(P^4T^4)) Hessian entries at fixed depth. Restoring depth, the full dense matrix has dimension (m=O(LP^2T^2)), storage (O(m^2)), and generic inversion (O(m^3)=O(L^3P^6T^6)); the latter is a direct dense-algebra derivation, not a claimed optimized lower bound. Monte Carlo samples, field sensitivities, and the preliminary DMFT solve add further costs. Linear or shallow symmetries reduce them in the examples. No general time-memory cutoff or forgetting theorem is provided; “dynamical filtering” of variance is not memory compression.

## Bottom line

The checked core is a formal linear-response/propagator method for initialization fluctuations, with illuminating special-case reductions and empirical evidence that feature learning can alter variance favorably. It is not a rigorous uniform finite-width remainder theorem. The most consequential source-level issue is the unqualified switch to exactly zero initial prediction in the general and shallow kernel actions; several displayed special-case coefficients and test formulas also need correction. These findings do not establish that the experimental implementation is wrong, nor invalidate the corrected formal response method.
