# Independent source audit: Adaptive kernel predictors from feature-learning infinite limits of neural networks

Audited source: Lauditi, Bordelon, and Pehlevan, ICML 2025/PMLR 267; supplied `tp_dmft/adaptive2025.pdf`, all 32 pages, including Appendices A–H. Rendered pages 4, 5, 24, and 31 were checked for the limit order, action, stochastic-source, and cost claims. No source code was fetched or executed. No manuscript, existing study findings, or another review was consulted. I previously read an unrelated π-limit paper, but had no prior findings on this source. The directly cited 2022 DMFT primary source was independently read in full as an assigned source; it was used to check the claimed DMFT specialization rather than to substitute for reading this paper.

## Assumption ledger and audit coverage

- **Architecture/scaling:** fixed input dimension (D), fixed dataset size (P), fixed depth (L), all hidden widths (N\to\infty). Internal normalization is (N^{-1/2}), first-layer normalization (D^{-1/2}), output preactivation (s=(\gamma_0N)^{-1}w^L\cdot\phi(h^L)), and output (f=\sigma(s)). Initialization is iid standard Gaussian; Bayesian prior precisions are denoted (\lambda_\ell).
- **Two distinct models:** aNBK takes equilibrium at finite width first, then width to infinity at fixed (\beta,\gamma_0). aNTK intends noiseless gradient flow with a positive, fixed weight-decay coefficient, then width to infinity, then a stationary long-time limit. The printed common SDE does not implement that second model at fixed prior precision without an additional scaling; see Claim 1.
- **Data/activation/loss:** principal examples are scalar square-loss binary regression, not multiclass classification. The Bayesian argument is advertised for general nonlinear activations, including nonhomogeneous tanh; the stationary aNTK identity needs a homogeneous pre-readout network. General readout/loss claims concern residuals (\Delta_\mu=-\partial\mathcal L/\partial s_\mu), not necessarily (y-f). Independent calculations below use the consistent square-loss convention (\mathcal L=\frac12\sum_\mu(y_\mu-s_\mu)^2).
- **Norm and evidence:** empirical kernel alignments are Frobenius cosines, insensitive to an overall kernel scale. No normwise width-error rate, sample-complexity theorem, posterior mixing bound, or solver convergence rate is provided.
- **Limit/horizon:** the two limit orders are not identified with each other. Fixed-time DMFT reasoning cannot automatically justify width/time interchange. Endpoint algebra is conditional on stationary limits; equilibrium saddle reasoning is conditional on normalizable single-site measures and appropriate saddle dominance.
- **Reconstructed coverage:** conditional Bayesian readout, homogeneous stationary identity, temperature/decay scaling, Gaussian-versus-response fields, action normalization and layer count, a superlinear-activation integrability counterexample, linear matrix covariance, scalar overlap asymptotics, and solver state/work. All appendices were read, but every CNN index and every implementation detail was not independently reconstructed.

## Claim 1 — The two adaptive predictor identities survive with explicit model and endpoint conditions

**Source:** main Eqs.3–14 and Table 1, pp.4–6; Appendix A.1–A.2, pp.13–17; Appendix E/F, pp.23–27.

### aNBK: independent finite-width readout calculation

Fix hidden features (H_{i\mu}=\phi(h_i(x_\mu))), let (\Phi=N^{-1}H^\top H), and use a Gaussian readout prior of precision (\lambda_L>0). For the stated likelihood scaling, direct Gaussian completion gives

\[
\mathbb E[s\mid H,\mathcal D]
=\Phi(\Phi+\lambda_L\beta^{-1}I)^{-1}y,
\]

and a test mean

\[
\mathbb E[s(x)\mid H,\mathcal D]
=\Phi(x)^\top(\Phi+\lambda_L\beta^{-1}I)^{-1}y.
\]

The conditional training-output covariance is

\[
\operatorname{Cov}(s\mid H,\mathcal D)
=\frac1{\gamma_0^2N}\Phi(\lambda_LI+\beta\Phi)^{-1}.
\]

Thus main Eq.5 follows if the learned feature kernels concentrate at a suitable deterministic posterior saddle. At finite width one must still average the nonlinear kernel predictor over the hidden-feature posterior. This derivation neither assumes Gaussian hidden preactivations nor proves their concentration. Appendix A.2 Eq.40 is missing a prefactor (\beta/\lambda) relative to Eq.39; main Eq.5 has the correct normalization.

### aNTK: independent stationary calculation

Use (\rho>0) for the actual weight-decay rate, to distinguish it from Bayesian prior precision. If the pre-readout (s(\theta,x)) is homogeneous of degree (\kappa), and

\[
\dot\theta=-\gamma_0^2N\nabla_\theta\mathcal L-\rho\theta,
\]

Euler's identity gives

\[
\dot s(x)=\mathbf k_s(x)^\top\Delta-\rho\kappa s(x),\qquad
K_s=\gamma_0^2N\nabla s\cdot\nabla s.
\]

At a stationary limit and for square loss/linear readout,

\[
s(x)=\mathbf k_s(x)^\top(K_s+\rho\kappa I)^{-1}y.
\]

This verifies the intended Eq.11 without invoking infinite width: it is already a finite-width stationary identity. It does not prove convergence, determine the final kernel, or remove the dependence of that kernel on training history. For unequal layer decay rates the coefficient is the appropriate weighted sum of layer homogeneity degrees, not automatically (\lambda_L\kappa). For nonlinear output (\sigma), the relevant kernel is the pre-readout (s)-Jacobian Gram matrix; the printed identification with the (f)-Jacobian Gram matrix in §3.2 is not correct without the chain-rule factors and the learning-rate normalization. Appendix E's unscaled-network convention supplies the intended normalization.

**Temperature/decay mismatch:** Eq.3 has drift (-\lambda\beta^{-1}\theta). Taking (\beta\to\infty) at fixed (\lambda), as Table 1 says, removes *both* noise and decay. Eqs.13–14 and Appendix E instead use fixed positive decay (-\lambda\theta). To recover the intended aNTK model from that common SDE, one must hold (\rho=\lambda/\beta>0) fixed (so prior precision grows with (\beta)), or switch explicitly to a separately parameterized noiseless model. This is a **repairable but substantive parameter-convention error**, not a failure of the stationary ridge identity. The two proposed predictors cannot literally both be identified with the printed fixed-(\lambda) limits of Eq.3.

Appendix F correctly acknowledges a zero/nonzero endpoint threshold in its single-point ReLU example: for (y=1), a nonzero solution has (\Delta=\rho/\gamma_0) and (\mathbb E h^2=\gamma_0-\rho), requiring (\gamma_0>\rho). Substitution into (K=2\mathbb E h^2) and the ridge identity gives (f=1-\rho/\gamma_0), confirming consistency. Merely stating (\gamma_0>0) would not suffice. Its following prose reverses an inequality once and calls the positive-residual solution “interpolation”; these are minor wording defects.

## Claim 2 — Bayesian min–max construction needs corrected action and an integrability domain

**Source:** main Eqs.6–8 and Algorithm 1, p.5; Appendix A Eqs.23–31, pp.13–15; G.2 Eq.88, p.29.

The intended single-site normalizer is a *normalized Gaussian expectation*

\[
Z_\ell=\mathbb E_{h\sim N(0,\Phi^{\ell-1}/\lambda_{\ell-1})}
\exp[-\tfrac12\phi(h)^\top\widehat\Phi^\ell\phi(h)].
\]

Appendix A Eq.23 and G.2 use this normalization. Main Eq.7 omits the covariance-dependent Gaussian normalizer. It is not a harmless constant when differentiating with respect to the previous kernel: using it literally adds spurious log-determinant derivatives. Main Eq.6 and Appendix Eq.30 also sum the single-site terms only through (L-1), although all (L) hidden-layer terms are needed. For (L=1), the printed action has no (Z_1), and stationarity in (\widehat\Phi^1) incorrectly forces (\Phi^1=0). Appendix Eq.25's full sum and the explicit linear action Eq.41 make the intended repair clear. **Minor local action transcription errors**, but Algorithm 1 must not be implemented literally from Eqs.6–7 as printed.

### Integrability counterexample to the broad activation scope

Consider one hidden layer, one unit-normalized training input, nonzero target (y), (\beta,\gamma_0,\lambda_0,\lambda_1>0), and the homogeneous activation (\phi(h)=h^2). This activation is not excluded by the stated homogeneous/general-nonlinearity scope. Eq.31c requires

\[
\widehat\Phi^1
=-\frac{\gamma_0^2y^2}{\lambda_1(\beta^{-1}+\Phi^1/\lambda_1)^2}<0
\]

for every finite proposed feature moment. Consequently the proposed single-site normalizer contains

\[
\int_{\mathbb R}\exp[-\lambda_0h^2/2+|\widehat\Phi^1|h^4/2],dh=\infty.
\]

There is no finite normalizable saddle density of the claimed form. In contrast, the original finite-width posterior with nonnegative square loss is normalizable because its likelihood is bounded by one against a proper Gaussian prior. Thus this is not just an invalid choice of the original Bayesian model.

**Severity: major activation-domain gap for the claimed general construction.** The saddle/importance-sampling prescription needs an explicit integrability domain and exclusions or different analysis for such superlinear activations. Restricting to the tested bounded tanh and suitable normalizable ReLU/linear saddles avoids this particular counterexample; it does not prove global saddle uniqueness or convergence of alternating stochastic optimization. The conditional kernel readout identity from Claim 1 also survives. Singular input Gram matrices additionally require Gaussian expectations on their support, rather than ordinary full-dimensional inverse/determinant formulas.

The identification of a locally stationary solution with a globally dominating min–max solution is formal. No proof is supplied that every numerical fixed point is globally dominant, that posterior kernels have a unique deterministic limit, or that the proposed inner/outer iteration converges. The description in Appendix A that zero temperature makes the posterior *uniform* over loss minimizers is too strong: the Gaussian prior and local geometry continue to weight minimizers.

## Claim 3 — The advertised deep DMFT solver omits response terms required by its cited dependency

**Source:** main Eq.13 and Algorithm 2, p.6; Appendix E Eq.75 and following sampling paragraph, p.24; directly cited Bordelon–Pehlevan 2022 main Eq.10 and Appendices D.7/O, pp.29–30,46.

The identities obtained by integrating the trained weights can indeed be written with raw sources

\[
\xi^\ell(t)=N^{-1/2}W^{\ell-1}(0)\phi(h^{\ell-1}(t)),\quad
\psi^\ell(t)=N^{-1/2}W^\ell(0)^\top g^{\ell+1}(t).
\]

But these sources are not generally independent Gaussian processes with just the feature/gradient covariances: the vectors multiplied by an initial matrix have subsequently depended on that same matrix. The cited 2022 DMFT derives a Gaussian innovation **plus causal response** decomposition. This paper's p.24 sampling paragraph replaces the raw sources by Gaussian draws without those response terms.

**Independent reuse check:** let (W_{ij}\sim N(0,1/N)), and let (a,b) be independent standard Gaussian vectors. A backward-driven input update (b_1=b+\epsilon W^\top a) gives

\[
Wb_1=Wb+\epsilon WW^\top a,
\qquad \mathbb E[(Wb_1)_i a_i]=\epsilon.
\]

This nonzero order-one correlation is the simplest forward/backward reuse effect; replacing the updated forward source by an independent Gaussian innovation loses it. The response kernels in the cited primary derivation account for exactly this structure. Fixed positive decay does not remove such correlations at finite training time.

**Severity: major gap in the general deep stochastic solver description.** It is not merely lack of rigorous justification: even the intended formal model needs the missing response closure. The source's actual G.3 implementation explicitly restricts to **one hidden layer**, where the input source is fixed and the readout source is a scalar Gaussian shared across examples; that special case does not have the problematic internal forward/backward reuse. The supplied shallow MLP/CNN aNTK experiments therefore do not test the advertised general deep sampling recipe.

At a genuinely stationary bounded limit, decay can suppress explicit initial-source terms and yield the necessary algebraic fixed-point constraints of Appendix F. That does not prove that the response-free transient dynamics selects the correct stationary solution. Appendix F.2 itself shows why first/second-moment fixed-point constraints do not determine the full limiting density: a different initialization can retain a different final distribution. Thus endpoint algebra and a correct general deep endpoint solver must be kept separate.

## Claim 4 — Linear overlap result mostly survives; matrix order and finite-temperature asymptotics need repair

**Source:** main Eqs.15–17, p.7; Appendix A.3 Eqs.41–51, p.18; A.5 Eq.60, p.20.

For a linear activation and previous-layer covariance (C=\Phi^{\ell-1}/\lambda_{\ell-1}), the normalized single-site Gaussian has covariance

\[
\Phi^\ell=(C^{-1}+\widehat\Phi^\ell)^{-1}
=(I+C\widehat\Phi^\ell)^{-1}C
=C(I+\widehat\Phi^\ell C)^{-1}.
\]

The printed Eqs.15/42a instead place (C) on the left of ((I+C\widehat\Phi^\ell)^{-1}). This is wrong for noncommuting matrices. For instance (C=\operatorname{diag}(1,2)) and (\widehat\Phi=-0.1\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}) give a positive definite true precision, but the printed covariance is

\[
\frac1{0.7}\begin{pmatrix}0.8&0.1\\0.4&1.8\end{pmatrix},
\]

which is not even symmetric. The correct covariance has both off-diagonal entries (0.2/0.7). **Minor, locally repairable matrix-order error.** The whitened rank-one reduction commutes and therefore does not test this defect.

With (\Phi^0=I), (\|y\|=1), and all (\lambda_\ell=1), the scalar saddle equations conserve (c_\ell\widehat c_\ell), yielding

\[
c_\ell=\left(1+\frac{\gamma_0^2c_L}{(\beta^{-1}+c_L)^2}\right)^\ell.
\]

This independently verifies the main overlap equation and its exponential dependence on the layer index for a fixed final solution. At fixed finite (\beta), its small-richness expansion is

\[
c_L=1+\frac{L\gamma_0^2}{(1+\beta^{-1})^2}+O(\gamma_0^4),
\]

not (1+L\gamma_0^2) unless a low-temperature approximation is also imposed. The large-richness exponent (2L/(L+1)) survives at fixed positive (\beta), as does (c_L\sim L\gamma_0^2/\log(L\gamma_0^2)) at large depth, because then (c_L\gg\beta^{-1}). These are asymptotics of the already width-limited scalar equation, not a simultaneous growing-depth/width theorem.

For completeness, a normalized small-tilt expansion is 
\(\mathbb E_V A=\mathbb E_0A-\frac12[\mathbb E_0(AQ)-\mathbb E_0A\,\mathbb E_0Q]+\cdots\), (Q=\phi(h)^\top\widehat\Phi\phi(h)\). Appendix Eq.60 has the wrong sign/coefficient on the normalization contribution. This local perturbative display should not be used as a checked coefficient formula; the nonperturbative Gaussian expectation remains the defining object.

## Claim 5 — Computational savings are model-specific; experiments do not certify a generic history-free solver

**Source:** main Figs.1–5, pp.3,7–9; Appendices A.1/F/G, pp.15–16,26–31.

The Bayesian method retains two (P\times P) kernels per layer, independent of physical training time: kernel state is (O(LP^2)). But Monte Carlo batches add (O(BP)) per sampled layer, plus differentiation workspace. The stated dense importance-sampling work (O(t_{\rm outer}t_{\rm inner}BP^2)) suppresses depth and Gaussian factorization/kernel-regression (P^3) work. (B=20000), roughly 200 inner iterations, up to 20000 outer iterations, and (P\le1000) are reported. These are computation budgets, not certified convergence/accuracy bounds. The paper explicitly says finite-network training is often cheaper.

General dynamic DMFT retains (O(LP^2T^2)) two-time kernel state and has a quoted dense (O(P^3T^3)) cost at fixed depth and sample budget. Appendix G.6 claims an (O(TP^3)) fixed-point version and points to E.1, but E.1 supplies the time-history CNN equations, not a complete justified general history-free algorithm. Appendix F explicitly states that stationary moments do not determine the full density and that tracking history may remain necessary. The quoted speedup is therefore **unsupported as a general deep endpoint algorithm** by the supplied derivation.

The implemented one-hidden-layer solver is a different, valid simplification: with (S=20000) sampled neuron states, it can update (h\in\mathbb R^{P\times S}), (z\in\mathbb R^S), and current residuals directly. At dense input Gram matrix, an implementation uses (O(SP+P^2)) current-state memory and (O(SP^2)) work per step, without a two-time kernel table. This follows from the shallow neuron ODE, not from a general time-forgetting theorem. No general truncation window or cutoff-error estimate is given. Printed G.3 also has local implementation-description defects: decay increments need the step-size factor, the last backward kernel should be (\mathbf1\mathbf1^\top) for a scalar readout, and the shallow NTK is (\Phi^0\odot G^1+\Phi^1), not the displayed scalar trace plus a matrix. No claim is made here that the actual software implements those typos.

**Evidence and limits:**

- The main shallow tests use two-class CIFAR-10 regression and widths around 5000; CNN comparisons use one convolutional layer with (8\times8) nonoverlapping patches and widths around 1024. Small-data overfitting and an optimal richness rather than monotonic improvement are expressly reported.
- Deep Bayesian tanh tests use a 50-example MNIST subset. Fig.4 reports layerwise cosine agreements of 97%, 81%, 73%, and 89%, not uniformly near-exact agreement; there is no numerical error budget separating finite width, posterior equilibration, importance sampling, and optimization.
- Appendix Fig.7's deep Bayesian solver is warm-started from perturbed empirical final-network kernels. This is a disclosed local consistency/stability check, not an independent from-data prediction of those same kernels. Fig.4 uses the lazy initialization and is the stronger independent solver test.
- Langevin simulations use fixed step size (5\times10^{-4}), inverse temperature 50, 20000 steps, and sampling every 1000 steps after step 5000. No mixing-time diagnostic or step-size extrapolation proves equilibrium. Gradient descent uses step size (10^{-3}), 20000 steps. The main width descriptions and appendix defaults vary, so figure-specific statements should be preferred.
- NNGP posterior risk includes a prediction-variance term, whereas NNGPK is its mean kernel predictor. Comparing either with a deterministic adaptive method answers a different baseline question; variance removal alone does not prove that finite-width mean shifts always worsen test loss. The paper's finite-width monotonicity discussion is empirical/generalizing, not a theorem.

## Bottom line

The conditional Bayesian readout and regularized homogeneous stationary kernel identities are sound and useful. The linear whitened overlap mechanism also survives independent reconstruction. Stronger claims require correction or qualification: the SDE limit must retain decay explicitly, the Bayesian saddle needs a normalizability domain, and the general deep dynamical solver needs response terms. The supplied evidence supports selected adaptive-kernel predictors and a shallow numerical method, not a rigorous universal endpoint theorem or a generic fixed-memory deep nonlinear compression scheme.
