# Independent source audit: Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks

Audited source: Bordelon and Pehlevan, arXiv:2205.09653v3 (4 October 2022), supplied `tp_dmft/dmft2022.pdf`, 55 pages including Appendices A–P. All pages and appendix equations were read; selected displayed mathematics, including p.53 Eq.174, was checked in the rendered PDF. No source code, training, existing study findings, manuscript, or other review was used. I previously digested a different π-limit paper, but had no prior findings on this paper. This report is source-first and independent of the other assigned audits.

## Assumption and coverage ledger

- **Model:** fixed depth (L), hidden widths (N), fixed input dimension (D), scalar output, and fixed training set size (P). The main model has no bias; extensions address bias, multiple outputs, unequal widths, CNNs, momentum, discrete time, and Langevin dynamics.
- **Initialization/scaling:** independent standard Gaussian trainable weights; first-layer normalization (D^{-1/2}), internal normalization (N^{-1/2}), output (f=(\gamma\sqrt N)^{-1}w^L\cdot\phi(h^L)). Rich scaling is (\gamma=\gamma_0\sqrt N), with fixed (\gamma_0>0); initial output tends to zero. Gradient flow is (\dot\theta=-\gamma^2\nabla_\theta\mathcal L). Consequently the kernel governing predictions is (K=\gamma^2\nabla f\cdot\nabla f), not the unscaled Jacobian Gram matrix.
- **Activation/regularity:** the theory introduces twice differentiable activations; experiments include tanh and ReLU. Higher-order perturbation formulas need additional derivatives and integrability not supplied by the initial twice-differentiable assumption. No general quantitative theorem with explicit regularity constants is proved.
- **Observables/norm:** two-time empirical feature and gradient kernels, normalized by (1/N); the main empirical agreement metric is Frobenius cosine alignment, not a relative-error norm. It cannot detect an overall multiplicative discrepancy by itself.
- **Horizon and limits:** fixed dataset and fixed finite observation horizon/time grid before (N\to\infty). The continuous-time saddle derivation is formal. Appendix K.3 explicitly distinguishes (N\to\infty) then long time from finite-(N) equilibration then (N\to\infty), and calls their relationship open.
- **Scope of reconstruction:** independently reconstructed parameter/output normalization, Gaussian-innovation versus response structure, linear closure, regularized stationary identity, large-richness scalar timescale, leading saddle bias sign, and dense solver cost. Did not certify every multi-output/CNN/Langevin Hessian index or re-prove a rigorous path-space limit.

## Claim 1 — Feature-learning DMFT and Gaussian/response structure

**Source:** main §§2–3, Eqs.1–10, pp.3–5; Appendix D, Eqs.19–58, pp.22–30; Appendices M–O, pp.42–46.

**Claim and justification level:** a self-consistent stochastic-process description of deep rich training, obtained by Gaussian initialization integration and a large-(N) stationary-action calculation. The paper itself says the derivation is not entirely rigorous (main §7, p.10). This qualification matters: lack of a concentration theorem is not, by itself, a hidden proof error.

**Independent check:** integrating the exact weight update gives terms involving (\Delta_\alpha(s)\Phi_{\mu\alpha}^{\ell-1}(t,s)g_\alpha^\ell(s)), and the backward analogue involving (G^{\ell+1}\phi(h^\ell)). Reusing the same initial matrix in the forward and backward passes also induces response terms. The auxiliary innovations (u^\ell,r^\ell) are Gaussian with covariances (\Phi^{\ell-1},G^{\ell+1}); the actual fields (h^\ell,z^\ell), obtained from nonlinear causal equations involving those innovations, generally are **not Gaussian**. Setting the response kernels (A=B=0) corresponds to the independently resampled-backward-matrix approximation derived in Appendix O, not to an exact simplification of ordinary training.

**Dependency check:** the supplied Tensor Programs IV main and complete supplement were independently read in the preceding assigned source audit. Appendix N.6's discrete stochastic-process correspondence is consistent with the Gaussian-plus-response mechanism. It does not by itself prove the continuous-time assertion: Appendix M explicitly leaves verification of the continuous-time limit to future work, and a finite discrete-program theorem does not supply uniform step-size or long-time bounds automatically.

**Localized errors:** main Eq.3 omits the factor (\gamma^2) when identifying the effective kernel with (\nabla f\cdot\nabla f); Appendix D.1 uses the gradient of (\gamma f) and D.8 Eq.59 gives the correct normalization. Algorithm 1's sample estimators for (A,B) omit the (\gamma_0^{-1}) in the definitions used by Eq.10 (compare Appendix D.7's explicit rescaling). Appendix M Eq.132 interchanges (u,r) in its final response definitions relative to Eq.10 and the preceding derivation. These are **minor, locally repairable transcription/normalization defects**, not evidence that the implemented experiments used the wrong equations.

**Survives:** a well-motivated, nonperturbative, formal finite-horizon DMFT with necessary causal response corrections, numerically tested in selected models. No demonstrated all-time theorem, error rate, unique saddle, or universal convergence of the numerical fixed-point solver.

## Claim 2 — Linear closure and what the solvable example actually establishes

**Source:** main §4.1, Eq.11, pp.5–6; Appendix F, Eqs.68–83, pp.32–34.

For a linear activation, write (h=u+\gamma_0 Cg), (g=r+\gamma_0 Dh). Algebra gives

\[
h=(I-\gamma_0^2CD)^{-1}(u+\gamma_0Cr),\qquad
\operatorname{Cov}(h)=(I-\gamma_0^2CD)^{-1}
[H_{\rm prev}+\gamma_0^2CG_{\rm next}C^\top]
(I-\gamma_0^2CD)^{-\top}.
\]

The analogous formula for (g) follows by exchange. This independently reproduces Eq.71. On a finite explicit causal grid, (C,D) are strictly causal, so the inverse exists as a finite nilpotent-series inverse; no small-(\gamma_0) expansion is required. This algebra does not establish convergence of the outer self-consistency iteration.

For one hidden layer and whitened sample Gram matrix, let (y=\|\mathbf y\|), (\Delta\) be residual magnitude, and (H_y) the target-direction feature covariance. The equations imply

\[
\dot H_y=2\gamma_0^2\Delta(y-\Delta),\quad
\dot\Delta=-2H_y\Delta,\quad
H_y^2-\gamma_0^2(y-\Delta)^2=1.
\]

Thus Eq.78 and the rank-one final feature spike follow. This is an exact calculation within the limiting shallow linear dynamics. For general input Gram matrix, Eq.74 should initialize (H(0)=K^x), not (I); the latter is correct only in the whitened subsection.

**High-richness qualification:** Eq.81's logistic approximation has the actual initial condition as an unstable stationary point, which the source acknowledges. The preceding statement that the learning timescale is simply proportional to (1/\gamma_0) misses the initial boundary layer. For fixed (0<c<1), the exact time to reach (f=cy) is

\[
t_c=\frac12\int_0^{cy}\frac{df}{(y-f)\sqrt{1+\gamma_0^2f^2}}
=\frac{\log\gamma_0+O(1)}{2y\gamma_0},\qquad \gamma_0\to\infty.
\]

The logarithm follows by integrating the intermediate region (1/\gamma_0\ll f\ll y), where the integrand is (1/(2y\gamma_0 f)). A prescribed nonzero alternative initial output removes this startup logarithm. **Minor asymptotic overstatement**, not failure of the exact scalar solution or its acceleration conclusion.

## Claim 3 — Regularized endpoint is a conditional identity, not guaranteed nonzero convergence

**Source:** main §4.2 and Fig.3, pp.6–7; Appendix J, Eqs.98–99, pp.36–37.

Assume square loss, positive decay (\lambda>0), a differentiable homogeneous predictor of degree (\kappa>0), and convergence to a stationary predictor and kernel. Euler's identity gives

\[
\dot f(x)=\mathbf k(x)^\top(\mathbf y-\mathbf f)-\lambda\kappa f(x).
\]

At stationarity, ((K+\lambda\kappa I)\mathbf f=K\mathbf y). Therefore

\[
f(x)=\mathbf k(x)^\top(K+\lambda\kappa I)^{-1}\mathbf y.
\]

This independently verifies Eq.98, with the effective kernel normalization of Claim 1. It also holds at finite width under the stated stationarity assumptions. It does not compute the learned final kernel, prove convergence, or justify exchanging width and time limits; it is not a ridge formula for arbitrary losses.

**Counterexample to the unqualified Appendix J sentence that (\gamma_0>0) implies a nontrivial endpoint:** take the allowed one-hidden-layer linear model with one unit-norm input and nonzero target (y). Write neuron variables (a_i,h_i), (f=(\gamma_0N)^{-1}\sum_i a_ih_i). Then

\[
\dot a_i=\gamma_0(y-f)h_i-\lambda a_i,\quad
\dot h_i=\gamma_0(y-f)a_i-\lambda h_i.
\]

For (E=N^{-1}\sum_i(a_i^2+h_i^2)),

\[
\dot E=4\gamma_0^2f(y-f)-2\lambda E
\le 2(\gamma_0|y|-\lambda)E,
\]

using (2\gamma_0|f|\le E) and discarding the nonpositive (-4\gamma_0^2f^2). Hence (\lambda>\gamma_0|y|) forces all parameters, predictions, and kernels to zero even in the rich regime. **Minor scope correction:** rich scaling permits the nontrivial fixed points observed in Fig.3, but does not guarantee them for every decay/data choice. The representer identity survives unchanged.

## Claim 4 — Perturbative orders survive formally; printed coefficient/remainder assertions need qualification

**Source:** Appendix P.1–P.7, Eqs.143–175, pp.46–53.

The symmetry of the centered backward innovations supports vanishing odd feature-learning corrections under a sufficiently smooth, symmetry-respecting expansion. The paper explicitly starts by assuming a power series (P.2). It supplies no uniform remainder bound, no radius of validity for a general nonlinear trajectory, and no width-uniform control allowing its small-(\gamma_0) expansion to substitute for a finite-width theorem. Formal (O(\gamma_0^4)) is not a proved trajectory-error estimate. The nonlinear coefficient display also has local algebra errors: Gaussian covariance differentiation has coefficient one for an observable (r r^\top), whereas Eq.164's final expression retains a spurious (1/2); the full general coefficient should be re-derived rather than copied.

**Independent saddle-bias check:** after the explicit sign convention (S\mapsto-S), Eqs.171–173 use density proportional to 
\(e^{-\delta^\top H\delta/2-U(\delta)}\), with (\delta=\sqrt N(k-k_*)\). Expansion gives the mean-shift term

\[
-N^{-1/2}\nabla O(k_*)\cdot\mathbb E_0[\delta U(\delta)],
\]

not the plus sign in Eq.174 (visually verified). For the elementary globally confining potential (S(x)=x^2/2+a x^3/6+b x^4/24), take (b>a^2/3), so zero is the unique stationary point. With (O(x)=x), direct Gaussian expansion yields 
\(\mathbb E x=-a/(2N)+O(N^{-2})\); the printed sign predicts (+a/(2N)). **Minor formula error:** reversing that sign repairs this calculation; it does not reverse the formal (N^{-1/2}) fluctuation scale or (N^{-1}) mean-correction order.

The claimed Gaussian distribution over the complete vector including dual fields is a formal contour-integral device, not automatically a real positive Gaussian measure: its Hessian has off-diagonal primal/dual blocks and need not be positive definite on the real space. A physical covariance requires the appropriate inverse block after treatment of dual contours. A rigorous remainder additionally needs saddle isolation, admissible contour deformation/tail control, and regularity. These are **acknowledged formal-method limitations**, not a falsified claimed rigorous central-limit theorem. The source says the full finite-width Hessian was not yet numerically evaluated (p.54).

## Claim 5 — Width-free numerical representation still retains growing time history

**Source:** main §4 and Table 1, pp.5,10; Algorithm 1 and §C, pp.19–21; CNN extension Eq.89, p.35.

Table 1's dense DMFT kernel storage (O(P^2T^2)) and work (O(P^3T^3)) suppress fixed depth, Monte Carlo sample count, and outer iterations; (T) here is the number of time grid points. A dense (PT\times PT) Gaussian covariance factorization/inversion explains the cubic estimate. At fixed (L), state includes two-time feature, backward, and response kernels; explicit dependence is at least (O(LP^2T^2)) for those arrays. Sampling many trajectories and their path derivatives adds sample-dependent work/state; retaining versus streaming these samples is an implementation tradeoff. CNNs replace the sample-time indexing by sample-spatial-time indexing, giving the source's (O(P^3|S|^3T^3)) work.

There is no proved time-truncation/forgetting approximation. Algorithm 1's damping factor (\beta=0.6) mixes successive *solver estimates*, not old and recent physical training times. Weight decay exponentially weights historical updates, but the paper does not bound the error of cutting off that history. The claim of roughly 15 solver iterations at depth four is empirical, not a contraction theorem.

**Evidence:** Fig.1 uses a small CIFAR subset ((P=10)), three hidden tanh layers, and width up to 2500; Fig.2 tests deep linear dynamics; Fig.3 tests a shallow regularized ReLU example. Fig.4 shows response-free and small-feature-learning approximations failing in a richer deep linear regime. CNN width-consistency tests in Fig.5 do not solve the full CNN DMFT on that dataset. Most runs are single wide networks; the checklist identifies Fig.1's repeated-run error bars as an exception. These support selected finite-horizon agreement, not generic normwise error rates, fixed-memory long-time simulation, universal kernel convergence, or an all-dataset generalization improvement theorem.

## Bottom line

The central surviving contribution is a feature-learning, history-dependent formal DMFT with empirically necessary response terms and useful exact linear reductions. It is not a rigorous general finite-width error theorem or a fixed-size general nonlinear dynamical closure. Several printed normalization and perturbation-coefficient errors are locally repairable; the unconditional nonzero-endpoint wording and pure inverse-richness startup timescale require narrowing. No fatal defect of the core formal DMFT construction was established by this bounded reconstruction.
