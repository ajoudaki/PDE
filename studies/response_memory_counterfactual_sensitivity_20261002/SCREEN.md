# Counterfactual significance screen: interacting data sources

**Assessment.** The strongest plausible use is predicting when removing two data sources destroys a generalization behavior even though removing either separately appears safe. Paired response histories could make the required training-path sensitivity cheaper in *moving state*. They do not currently provide a new identifiable causal quantity or an established computational advantage over exact differentiation of training. The paper's missing result is convergence of intervention sensitivities, not another endpoint decomposition.

Scope: scientific assessment and proposed calculation only; no experiment launched. Inputs were the current `paper/main.tex`, its complete `results.tex`, maintained `docs/index.qmd` and `docs/notation.qmd`, and primary literature below. This assesses the stated theorems' relevance, not their proofs.

## The consequential question

Fix two disjoint training groups $A,B\subseteq\{1,\ldots,m\}$, the initialization, optimizer, and physical stopping time $T$. For the paper's network,

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\quad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
f_a=w^\top h_a^{(L)}/n.
\]

The middle recurrence applies for $2\le\ell\le L$. Write $r_a=f_a-y_a$, and introduce explicit source-weight interventions

\[
\mathcal L_{u,v}(\theta)=\frac1m\sum_a
\bigl[1+u\mathbf1_A(a)+v\mathbf1_B(a)\bigr]r_a^2,
\qquad \dot\theta=-\mathcal D\nabla_\theta\mathcal L_{u,v}.
\]

Here $\theta$ contains all weights, and $\mathcal D$ has the paper's block mobilities $(n,1,\ldots,1,n)$. Keeping denominator $m$ fixed prevents source removal from silently changing the learning-rate schedule. For a specified held-out distribution $\nu$, define

\[
\mathcal J(\theta)=-\mathbb E_{(x,y)\sim\nu}
\bigl(f_\theta(x)-y\bigr)^2,\qquad
J(u,v)=\mathcal J(\theta(T;u,v)).
\]

The joint-removal interaction is

\[
I_{AB}=J(-1,-1)-J(-1,0)-J(0,-1)+J(0,0).
\]

A substantially negative $I_{AB}$, with small individual removal losses, exposes a pruning failure that individual attribution misses. Its practical consequence is retaining at least one of two mutually supporting data sources. The tractable local target is $\partial_u\partial_vJ(0,0)$; converting it into a prediction of $I_{AB}$ requires a separately validated finite-intervention approximation. A derivative alone does not establish safe full deletion.

I would reject “can a readout repair this behavior?” as the primary history claim. With the final features and repair data supplied, best squared-loss readout repair is already a linear least-squares problem. History can explain how those features arose, but is unnecessary for that decision.

## What paired history actually adds

The paper's exact hidden update is

\[
W^{(\ell)}(T)-W_0^{(\ell)}
=-\frac{2}{nm}\sum_a\int_0^T
r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}\,dt,
\]

where $\delta_a^{(L)}=w\odot\phi'(z_a^{(L)})$ and

\[
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

For the baseline, the clock obeys $\dot\tau=\rho$, $\tau(0)=1$, with $\rho^2=m^{-1}\sum_a r_a^2$. With shifted Legendre polynomials $p_j$, the stored moments are

\[
\bar h_{a,j}^{(\ell-1)}=\int_0^\tau h_a^{(\ell-1)}p_j(\xi/\tau)\,d\xi,\qquad
\bar\delta_{a,j}^{(\ell)}=\int_0^\tau
\frac{r_a\delta_a^{(\ell)}}{\rho}p_j(\xi/\tau)\,d\xi.
\]

The unit prefix uses initial forward responses and zero backward responses. Their weighted outer products reconstruct the learned hidden action. They retain where earlier forward features met earlier backward learning signals, a structured representation that a final gradient or Hessian does not describe.

However, a sample-indexed summand is an accumulated *write*, not its causal contribution under removal. Changing $A$'s weight changes every sample's residual, forward feature, and backward response. Even the first derivative of the integral contains the direct $A$-write plus derivatives of all three factors for every sample. Subtracting the $A$-moments omits this feedback. First-layer and readout effects must also be included.

There is no information-theoretic separation from dense weights plus the known training algorithm and initialization: they permit rerunning the counterfactual. Nor do terminal moments automatically answer arbitrary retrospective interventions. A fixed finite moment set does not uniquely identify arbitrary histories; queries must have been propagated online, or require a justified replay/reconstruction procedure.

## The actual competing calculation

Let $F=-\mathcal D\nabla\mathcal L_{0,0}$, and let $F_A,F_B$ be the same gradient contributions restricted to each group. Along the baseline trajectory, define $s_A=\partial_u\theta$, $s_B=\partial_v\theta$, and $s_{AB}=\partial_u\partial_v\theta$. Smooth tanh networks admit the exact sensitivity equations

\[
\begin{aligned}
\dot s_A&=DF\,s_A+F_A,\\
\dot s_B&=DF\,s_B+F_B,\\
\dot s_{AB}&=DF\,s_{AB}+D^2F[s_A,s_B]
+DF_A\,s_B+DF_B\,s_A,
\end{aligned}
\]

with all sensitivities initially zero. Here $D$ denotes differentiation in the physical weights. The test-score derivative includes both $D\mathcal J\,s_{AB}$ and $D^2\mathcal J[s_A,s_B]$, evaluated at time $T$. Directional automatic differentiation evaluates these without constructing full Hessian or third-derivative tensors.

This exact unrolling/forward-sensitivity calculation is the strongest baseline: it already includes changing features and their historical feedback. Forward sensitivities for two predetermined groups need no growing checkpoint archive. A practical first-order history competitor is [SOURCE](https://arxiv.org/html/2405.12186v2), which approximates unrolling with a few stationary trajectory segments; its experiments use six checkpoints. SOURCE is relevant evidence that history-aware attribution is established, although its additive first-order score is not itself a fair mixed-interaction baseline.

Endpoint alternatives must include [second-order group influence](https://proceedings.mlr.press/v119/basu20b.html), which corrects parameter sensitivity, and [interaction-aware influence](https://arxiv.org/html/2605.15675v1), which includes target curvature. Comparing only to additive influence would manufacture an advantage. The novelty opportunity is accurate compressed **trajectory** derivatives, not discovering that data interactions exist.

## Required result and costs

First extend the moment sources and clock consistently to the weighted loss, then differentiate with respect to $u,v$, including reconstruction, first layer, and readout. Prove convergence of the resulting mixed test derivative to the dense one, uniformly on a specified intervention neighborhood and finite horizon, at an order independent of width. Value convergence from the paper does not imply derivative convergence. A mixed finite difference amplifies an absolute prediction error by $O(\varepsilon^{-2})$; sending its step to zero without stronger control is invalid. The activation hypotheses require strengthening for second-order flow sensitivities. A positive residual on the finite horizon permits clock differentiation; uniform-in-time sensitivity needs additional treatment of residual-zero degeneracy. Neither weighted-intervention nor derivative tracking is the paper's current theorem.

For one group pair, let

\[
P=(L-1)n^2+n(d+1),\qquad
S_q=2(L-1)mnq+n(d+1)+O(1).
\]

Dense forward sensitivities use approximately $4P$ moving numbers; the proposed calculation uses approximately $4S_q$, plus the shared fixed initialization's $(L-1)n^2$ numbers. Thus total memory remains quadratic in width: only the additional evolving/tangent storage becomes linear when $mq\ll n$. A constant number of directional passes preserves the paper's per-step asymptotic cost

\[
O(Lmn^2+Lm^2nq+Lmnq+nmd),
\]

with larger constants for second derivatives. There is no automatic runtime acceleration. For $k$ simultaneously queried groups, all first and mixed derivatives require $O(k^2S_q)$ storage; samplewise all-pairs attribution can therefore cost $O(Lm^3nq)$. Arbitrary post-training queries would additionally need replay or saved states. Fixed initialization, source data, and their provenance cannot be omitted from cost accounting.

## Cheapest decisive calculation

Use one predetermined two-hidden-layer tanh network, width $512$, zero readout, canonical Gaussian initialization, and eight non-antipodal circle inputs

\[
x_j=\sqrt2(\cos(j\pi/10),\sin(j\pi/10)),\quad
y_j=(-1)^j,\quad j=0,\ldots,7.
\]

Fix $A=\{2,3\}$, $B=\{4,5\}$; evaluate held-out squared error against $y(\vartheta)=\cos(10\vartheta)$ on a fixed 64-point interior angular grid. Fix $T=80$. Labels are deliberately outside the paper's guaranteed small-label range: this is a usefulness screen in nonlinear feature learning, not theorem confirmation.

Compute the exact dense mixed sensitivity and the differentiated closures at $q=1,3,7$. Verify the dense sensitivity using three perturbed dense trainings at each of downweighting steps $0.1$ and $0.05$, sharing the baseline. Compare with second-order endpoint influence, and with an otherwise identical frozen-hidden-feature calculation; the latter detects interactions already explained by readout learning or the test loss's curvature. Report Hessian conditioning and sensitivity to the endpoint estimator's regularization: an undefined singular-Hessian formula is not a defeated baseline. No search over groups or seeds should select a favorable instance.

Precommit: a useful signal must exceed numerical uncertainty twentyfold; the dense derivative check must agree within 2%; $q=7$ must predict its sign and magnitude within 10%, with improved error from $q=3$, while the strongest tested endpoint estimate has at least 30% error. Match numerical tolerances and report total resident memory and wall time. If the signal is absent, hidden features barely move, or the frozen-feature control reproduces the interaction, this test does not establish feature-mediated value. A positive screen requires two fresh seeds before making a utility claim; stop after this bounded comparison.

**Verdict:** worth one bounded sensitivity screen, but not yet a compelling independent significance claim. Success would establish a cheaper representation for a known causal calculation. Failure of derivative accuracy despite excellent trajectory accuracy would directly identify why the present compression theorem is insufficient. Neither outcome licenses interpreting stored sample moments as unique ownership of learned knowledge, extrapolating infinitesimal effects to full deletion, or transferring fixed-seed conclusions to stochastic training distributions.
