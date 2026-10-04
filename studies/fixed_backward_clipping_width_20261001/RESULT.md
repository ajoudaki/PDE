# Fixed clipping: root-width fluctuations, unresolved population bias

2026-10-01. This study investigates whether a fixed positive backward-response clipping threshold suffices to prove all-time root-width prediction error for the actual q=1 closure. It uses the current paper's canonical initialization and fixed random mixer. The full requested width-rate theorem remains open. Any fixed positive cap gives all-time root-width fluctuations around finite-width conditional means, together with a unique clipped population limit. The continuation now bounds the deterministic bias by C_mu(Y/n+Y^3), where Y is label RMS; the nonvanishing Y^3 remainder prevents this from being a proved width-convergence rate at fixed labels.

## Exact model and conditions

There are two tanh hidden layers, fixed finite training data, Gaussian read-in A_0 with variance-one entries, Gaussian fixed mixer W_0 with variance-1/n entries, zero readout and value memories, initial keys h_a(0), and initial clock one. Use the normalized q=1 variables k_a=bar(h)_a/tau and v_a=-2bar(delta)_a. In particular

\[
B=W_0+\frac1{mn}\sum_a v_a k_a^T
\]

is a derived action, not an independently trained matrix. For a fixed M>0 let C_M be hard coordinatewise clipping to [-M,M]. Clip recursively after the tanh gates, before multiplying by residuals:

\[
d_a=C_M(w\odot\operatorname{sech}^2(Bh_a)),\qquad
\ell_a=C_M(\operatorname{sech}^2(Ax_a/\sqrt d)\odot B^Td_a).
\]

Use these d_a,ell_a in the usual q=1 value and read-in updates. The readout, key and residual-RMS clock equations are unchanged. Complete equations and normalization are in [FITTING_AND_THRESHOLD.md](FITTING_AND_THRESHOLD.md).

Assume the limiting initial readout-feature Gram has a positive margin and that the fixed label RMS Y is sufficiently small, independently of width. The result is not asserted for arbitrary unscaled ±1 labels. The clipping threshold is fixed independently of width and time. The error target in this note is the clipped closure's own population predictor, not the original unclipped predictor or the dense population predictor.

## Results proved in the component derivations

**Fitting.** On an initialization event G_n with probability at least 1-C/n, the clipped flow exists globally, fits exponentially, and all state variables converge. The fitting proof uses the readout Gram and bounds the effect of hidden motion; it does not assert that clipped backpropagation remains a gradient flow. Explicit sufficient constants, uniform in M, are given in [FITTING_AND_THRESHOLD.md](FITTING_AND_THRESHOLD.md).

**A concrete cap.** Any fixed M>0 is admissible for the regularity and centered fluctuation conclusions. M=1 is one concrete choice. The proof gives

\[
\|w(t)\|_\infty\le2\int_0^t\rho(s)\,ds\le2Y/\lambda.
\]

Thus the top clip is inactive if M>=2Y/lambda, including M=1 under the explicit fitting restriction. The lower clip can remain active. Increasing M is not needed to obtain width-independent Lipschitz constants; the constants can grow with M.

**Own population limit.** For every fixed M>0 the modified closure defines a unique strong population evolution on the canonical generated Gaussian spaces, with the actual initialized operator and its adjoint. Its predictor f_M is deterministic. Finite-width predictors converge to f_M uniformly over all time in the integrated query metric for each fixed finite-second-moment test law. This is a qualitative convergence theorem. Its proof is in [CLIPPED_POPULATION_ROUTE.md](CLIPPED_POPULATION_ROUTE.md).

**All-time root-width fluctuations.** Let

\[
\bar f_{n,M}(t,x)=\mathbb E[f_{n,M}(t,x)\mid G_n].
\]

For every fixed query x,

\[
\mathbb E\left[\sup_{t\ge0}|f_{n,M}(t,x)-\bar f_{n,M}(t,x)|^2\mid G_n\right]
\le\frac{C_{M,x}}n.
\tag{1}
\]

For every fixed probability law mu with finite fourth input moment, including circle and sphere laws, this also gives

\[
\mathbb E\left[\int\sup_{t\ge0}|f_{n,M}(t,x)-\bar f_{n,M}(t,x)|^2\,d\mu(x)\mid G_n\right]
\le\frac{C_{M,\mu}}n.
\tag{2}
\]

The fourth-moment requirement belongs to this centered quantitative argument; its merely-second-moment extension is not proved. The time supremum is inside the input integral. Neither a spatial supremum nor an all-time unconditional expectation over bad initialization events is asserted. Equation (2) includes the fitted endpoint and implies root-width accuracy around the conditional mean at each fixed confidence, after adding P(G_n^c)<=C/n. The proof is in [CONCENTRATION_ROUTE.md](CONCENTRATION_ROUTE.md). The bar notation replaces the earlier m_{n,M}, to keep m reserved for sample count.

The heart of (1) is an all-time comparison of two initialized trajectories. Fixed clipping makes

\[
|C_M(p\operatorname{sech}^2z)-C_M(p'\operatorname{sech}^2z')|
\le |p-p'|+2M|z-z'|.
\]

The exact residual equation can be written with the readout Gram as the dominant contracting term. The remaining scalar kernels have width-independent Lipschitz constants: move the actual transpose action into the forward side of their scalar contractions and use the bounded clipped lower response. Residual damping and finite total activity then make the complete prediction path Lipschitz in Gaussian initialization with constant C_M,x/sqrt(n).

To control the whole time interval in mean square, the proof also bounds prediction-velocity sensitivity by C_M,x(1+t)exp(-ct)/sqrt(n). Extend these scalar velocity functions off G_n, apply Gaussian Poincare at each time, and integrate their standard deviations. The integrable sensitivity replaces a union bound over infinitely many times. This argument uses the actual reused mixer; it does not declare trained neurons independent.

## Exactly what remains unresolved

Define the paper-style metric

\[
\mathcal E_\mu(f,g)=\left(\int\sup_{t\ge0}|f(t,x)-g(t,x)|^2d\mu(x)\right)^{1/2}
\]

and the deterministic bias

\[
\beta_{n,M,\mu}=\mathcal E_\mu(\bar f_{n,M},f_M).
\]

The component results give

\[
\left(\mathbb E[\mathcal E_\mu(f_{n,M},f_M)^2\mid G_n]\right)^{1/2}
\le\frac{C_{M,\mu}}{\sqrt n}+\beta_{n,M,\mu},
\qquad \beta_{n,M,\mu}\longrightarrow0.
\tag{3}
\]

For the last convergence, on G_n the all-time predictors have a common bound C(1+||x||/sqrt(d))Y. Qualitative convergence from the population route, truncation in x and bounded convergence therefore give conditional mean-square convergence in the all-time input metric. Jensen, first for the time supremum and then under the input integral, transfers it to the conditional mean.

What is missing is

\[
\beta_{n,M,\mu}\le C_{M,\mu}/\sqrt n.
\tag{4}
\]

Concentration and uniqueness of the limit do not imply (4). For example, the abstract random variables n^(-1/4)+n^(-1/2)tanh(Z) have root-width fluctuations and converge to zero, but their error to zero is larger. This example only refutes that inference; it is not a counterexample to the clipped closure.

The available fixed-program Gaussian estimates lose constants as the training mesh is refined. Clipping makes the coordinate maps regular but does not prevent successive W_0 queries from being arbitrarily close. The resulting small history-Gram eigenvalues obstruct the direct use of inverse-Gram estimates uniform in the mesh. A quantitative argument that respects those dependencies and cancellations is still needed to prove (4). This is a missing proof, not evidence that every fixed positive cap fails.

Accordingly, **M=1 is certified for fitting, a unique clipped population limit, and centered root-width fluctuations; no fixed positive M is yet certified here for the complete root-width population error.** M=0, which freezes feature learning, is excluded as a solution. Comparison with the original unclipped system would additionally require a separate clipping-bias estimate.

## Continuation: the full bias is bounded, but not at a vanishing width rate

The new [FULL_ERROR_CHECKPOINT.md](FULL_ERROR_CHECKPOINT.md) proves, for a test law with finite second moment and sufficiently large n,

\[
\beta_{n,M,\mu}\le C_\mu(Y/n+Y^3),
\qquad
\left(\mathbb E[\mathcal E_\mu(f_{n,M},f_M)^2\mid G_n]\right)^{1/2}
\le C_\mu(Y/\sqrt n+Y^3).
\tag{5}
\]

Its proof explicitly bounds actual feature learning by comparison with the initialized-feature readout trajectory, whose own mean bias is O(Y/n). The remaining feature-learning contribution is O(Y^3) in prediction, at both finite and infinite width. This remainder is retained, not treated as zero. At fixed labels, (5) is not the missing estimate (4).

The new exceptional-initialization proof gives P(G_n^c)<=C exp(-cn) for a sufficiently large fixed initialized operator cap and proves |f_{n,M}(t,x)|^2<=Y^2t for every initialization and query. Thus on a finite horizon [0,T] the unconditional full RMS population error is bounded by

\[
C_\mu(Y/\sqrt n+Y^3)+C Y\sqrt{T+1}\,e^{-cn/2}.
\tag{6}
\]

The last term cannot be controlled for all time by sending T to infinity. The remaining all-time tasks are a vanishing root-width estimate for the feature-learning bias and, if an all-initialization RMS theorem is required, a predictor moment bound on exceptional initializations. The new cavity and width-doubling routes isolate concrete response-trace estimates but do not prove them. No counterexample to the desired full theorem has been obtained.

## Verification and files

The coordinator derived and checked the fitting and explicit-threshold result. The threshold route independently checked its complete final proof and constants. The population and concentration routes were independently assigned, then checked against one another by the coordinator. A smooth-versus-hard clipping mismatch in an initial concentration draft was corrected; all current statements use the hard clip above. The completed fresh scoped [REVIEW_CHECK.md](REVIEW_CHECK.md) supports the three partial results and verifies the final source hashes. Its one regularity clarification in the abstract transfer lemma was applied and checked. The coordinator read the complete report. The quantitative population-bias gap remains open. No promotion or manuscript edit is implied.

The threshold note [THRESHOLD_ROUTE.md](THRESHOLD_ROUTE.md) also derives an unbounded Gaussian initial lower-response tangent law and a qualified lower-cap activation example. Neither is used as a counterexample to the population-width conjecture. No numerical experiment was run.

For the continuation, the fresh scoped [FULL_ERROR_CHECK.md](FULL_ERROR_CHECK.md) reconstructs (5)–(6) through the complete checkpoint derivation and supports those partial bounds. The conditional estimates are explicitly restricted to sufficiently large n; the checker caught the need to exclude widths where the positive-Gram good event is impossible. The supplied own-population construction is an explicit input to this check. The coordinator read all new route notes and the complete check. This does not certify the missing root-width feature-learning bias or the all-time exceptional-event moment.
