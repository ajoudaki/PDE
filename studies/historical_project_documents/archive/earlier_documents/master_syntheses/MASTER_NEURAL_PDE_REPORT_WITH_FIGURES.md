# Master report: the finite neural-PDE conjecture, evidence, causal theory, and remaining proof program

**Date:** 26 July 2026  
**Model:** standard fully dense Euclidean \(\mu\)P residual network  
**Limit order:** width first, residual depth second  
**Primary observables:** training outputs, loss, and depth-indexed hidden Gram matrices  
**Status:** authoritative synthesis through the nonlinear scalar stress test, parity-correct Hermite audit, degree-seven tail analysis, compactness analysis, and the recovered mean-field response/Wick calculus

**Figure note:** this edition embeds only pre-existing, provenance-traced
figures from the archived experiments. No experiment was rerun and no new
figure was generated for this edition.

## Executive conclusion

The project has established a substantive finite-PDE phenomenon, but not yet the full arbitrary-accuracy theorem.

The strongest current empirical statement is:

> A literal, autonomous, width-independent, nonlinear operator–Liouville PDE derived from the standard dense Euclidean \(\mu\)P architecture predicts nonlazy output and hidden-Gram training dynamics with low error across the canonical benchmark and a broad set of held-out configurations.

This is no longer plausibly explained by a fixed linear or gain-adjusted-linear model. In the deliberately nonlinear scalar sine stress, the paired dense linear control missed the nonlinear dense Gram path by \(15.95\%\), while the nonlinear PDE matched the dense Gram and output paths within \(2.50\%\) and \(2.81\%\). Thus the PDE captures a substantial part of nonlinear feature-learning dynamics beyond the tested linear controls.

The strongest current theoretical statement is different:

> At every finite Hermite cutoff, wherever the displayed flow is well posed, the proposed PDE is an exact projected Euclidean gradient system with a shared forward/transpose operator, a positive-semidefinite tangent kernel, direct moment readouts, loss dissipation, and an autonomous current state.

What remains unproved is the identification and convergence statement:

> Increasing the parity-correct source-Hermite cutoff has not been shown to produce a Cauchy sequence converging to the ordered dense limit with arbitrary accuracy.

The latest hierarchy evidence is mixed but informative:

- the old adverse \(P=5\to15\to35\) comparison was invalid because even Hermite shells are exactly inert;
- the properly defined newly opened odd-shell source contracts by factors of \(17\)–\(34\) at the first corrected rung;
- individual high-shell amplitudes weaken and adjacent dominant defects are almost orthogonal;
- nevertheless, aggregate projective state and observable Cauchy increments grew through degree seven by factors \(1.322\) and \(1.636\);
- the apparent high-degree turnover in the scalar study did not replicate across well-conditioned cubature scrambles;
- higher source Hermites changed the scalar Gram prediction by only about \(0.25\%\)–\(0.34\%\), and did not improve the finite dense-reference error systematically: degree three gave a small improvement, while degree eleven was worse than degree one.

The correct interpretation is therefore not “Hermites diverge,” but also not “Hermites converge”:

> The low-order PDE is highly effective, while pure-Hermite arbitrary-accuracy convergence remains an open compactness-and-stability problem.

The single highest-leverage analytic target is:

\[
\boxed{
\text{propagated source-mode compactness/weighted regularity}
\;+\;
\text{uniqueness and cutoff-uniform forced stability}.
}
\]

The elaborate earlier mean-field calculus is directly relevant, but only after separating two different constructions:

1. The fixed-order derivative/Wick calculus computes exact feature-orbit and induced physical-time jets, activation-derivative trees, and Gaussian contractions at every fixed order. It is an excellent local algebra and audit engine. Ordinary truncation of the limiting feature-time Wick series is not a convergence mechanism: it was rigorously disproved in the unbounded quadratic/Gaussian model by factorial coefficient growth and zero radius, and the associated physical-time closures fail uniformly.
2. The oriented causal-response/Onsager calculus tracks chronological \(W\) versus \(W^\top\) reuse, nonlinear derivative trees, conditional Gaussian means, learned rank-one insertions, and finite history coordinates. Its pure depth-propagation tail has a genuine factorial Volterra bound. This is the most promising causal bridge to the present PDE and the leading fallback if static Hermites alone are insufficient.

The recommended proof architecture is consequently hybrid:

1. use the Gaussian derivative/Wick machinery to propagate a source-weighted regularity class and to derive and control the conditional/Onsager terms;
2. use the chronological response hierarchy to control depthwise propagation and forced stability;
3. prove trained iid-depth homogenization by separating the surviving conditional mean from centered innovations;
4. if a response component is not determined by the static Hermite state, promote it to a finite autonomous history coordinate rather than returning to a dense matrix.

The current verdicts are:

| Claim | Verdict |
|---|---|
| A genuine finite neural PDE was constructed and integrated | Established |
| It has exact finite-cutoff gradient, transpose, PSD-kernel, autonomy, and dissipation structure | Established |
| It predicts active, nonlinear feature learning rather than a lazy trajectory | Strongly supported |
| Its success is explained by a fixed gain-adjusted linear network | Rejected in the designed scalar stress for Gram dynamics |
| It is finely tuned only to the original data and labels | Strongly disfavored by the 14-case transfer study |
| The pure source-Hermite hierarchy is empirically Cauchy | Not established |
| The pure source-Hermite hierarchy is empirically divergent | Not established; the original adverse argument was invalid |
| The finite PDE is the ordered \(n\to\infty\), then \(L\to\infty\) limit | Open |
| Arbitrary-accuracy compact-time approximation | Open |
| Uniform all-time approximation | Open |
| A response-enriched finite PDE can repair pure-Hermite failure | Plausible and causally motivated, not yet emitted or proved |

## 1. The hierarchy of claims

Several logically different statements have appeared in the project. They must remain separate.

### Level I: finite-PDE internal correctness

For every finite Hermite cutoff, the displayed operator–Liouville system is a genuine finite-source PDE with exact internal gradient and transpose identities wherever its flow is well posed.

This level is established.

### Level II: practical low-order dense-network approximation

One small PDE predicts finite dense-network outputs and hidden Grams accurately over the tested active transient and plateau, without case-specific fitting.

This level is strongly supported on the tested regimes.

### Level III: compact-time convergence of the explicit Hermite family

For every \(T<\infty\), increasing the complete parity-correct Hermite degree should converge uniformly on \(0\le t\le T\) to an infinite operator flow.

This level is open. It is the immediate mathematical bottleneck.

### Level IV: identification with the ordered dense limit

The infinite operator flow must be identified with

\[
n\to\infty\quad\text{at fixed }L,
\qquad
L\to\infty\quad\text{second},
\]

including the correct trained conditional/Onsager mean.

This level is open, though there is favorable finite-grid and homogenization evidence.

### Level V: uniform all-time approximation

Compact-time convergence must be upgraded to

\[
\sup_{t\ge0}d_{\rm obs}<\varepsilon
\]

using dissipation, residual arclength, eventual contraction, or another valid tail mechanism.

This level is open.

### Level VI: broad finite-neural-PDE existence

Even if the pure Hermite witness fails, some fixed architecture-local finite PDE family—possibly enriched by response/history coordinates—may still approximate the dense observables to arbitrary accuracy.

This is the broad project conjecture and remains open.

This claim stack matters. Level II can be scientifically valuable even if Level III fails. Conversely, Level III would not by itself prove Levels IV and V.

## 2. Canonical dense model

Fix \(m\) samples \(x_1,\ldots,x_m\in\mathbb R^d\), labels \(y_1,\ldots,y_m\), width \(n\), residual depth \(L\), and \(\Delta=L^{-1}\). The standard dense residual network is

\[
h_r^0=Bx_r,\qquad z_r^\ell=W_\ell h_r^\ell,
\]

\[
h_r^{\ell+1}
=h_r^\ell+\frac{\gamma}{L}\phi(z_r^\ell),
\qquad 0\le\ell<L,
\]

\[
f_r=\frac1n a^\top h_r^L,
\qquad
\mathcal L=\frac12\sum_{r=1}^m(f_r-y_r)^2.
\]

For the canonical theory and principal experiment, \(\phi=\tanh\). Every \(W_\ell\in\mathbb R^{n\times n}\) is fully dense and unconstrained. All of \(B\), \(a\), and every \(W_\ell\) train.

Initialization is independent:

\[
B_{ij}\sim N(0,1),\qquad
a_i\sim N(0,A^2),\qquad
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right).
\]

Ordinary Euclidean \(\mu\)P gradient flow uses

\[
\eta_B=n,\qquad
\eta_a=n,\qquad
\eta_{W_\ell}=L.
\]

There is no orthogonalization, activation-natural preconditioner, quotient geometry, low-rank parameterization, tied matrix, frozen block, or specially designed closure optimizer.

With \(e=f-y\), unit-output adjoints satisfy

\[
p_r^L=a,\qquad
p_r^\ell=
\left(I+\frac{\gamma}{L}W_\ell^\top D_r^\ell\right)
p_r^{\ell+1},
\qquad
D_r^\ell=\operatorname{diag}\phi'(z_r^\ell),
\]

and \(\beta_r^\ell=D_r^\ell p_r^{\ell+1}\). The exact parameter flow is

\[
\dot W_\ell
=-\frac{\gamma}{n}\sum_q e_q\,
\beta_q^\ell(h_q^\ell)^\top,
\]

\[
\dot a=-\sum_q e_qh_q^L,
\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
\]

The finite-network output satisfies

\[
\dot f=-\Theta^{n,L}e,
\]

where

\[
\Theta^{n,L}_{rq}
=G^{h,L}_{rq}
+(x_r^\top x_q)G^{p,0}_{rq}
+\frac{\gamma^2}{L}\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
\]

Every block is positive semidefinite, hence

\[
\dot{\mathcal L}=-e^\top\Theta^{n,L}e\le0.
\]

These identities anchor both the finite PDE and the later stability arguments.

### 2.1 Ordered target

The target is not a smooth interpolation of the raw iid matrices \(W_\ell\). The correct order is

\[
\boxed{
n\to\infty\text{ at fixed }L,
\qquad
L\to\infty\text{ second}.
}
\]

The irreducible target observables are

\[
\mathcal O_\vartheta(t)
=\left(f_\vartheta(t),G_\vartheta^h(\cdot,t)\right),
\]

where

\[
G^h_{rq}(s,t)
=\lim\frac1n h_r(s,t)^\top h_q(s,t).
\]

Loss is determined by \(f\). Tangent-kernel convergence is valuable but is not required in the minimal observable norm.

The formal canonical laboratory is a fixed compact neighborhood \(\mathcal U\) around

\[
X=I_3,\quad
y=(0.8,-0.55,0.35),\quad
\sigma_w=0.65,\quad
A=\gamma=1.
\]

The transfer experiments explore a substantially broader empirical family, but the sharp theorem should first be proved on one explicit compact \(\mathcal U\), then enlarged.

### 2.2 Model assumptions versus proof assumptions

The model assumptions are:

- fixed finite \(m,d\);
- iid Gaussian initialization;
- fully dense untied residual matrices;
- Euclidean \(\mu\)P learning rates;
- \(1/L\) residual scaling;
- squared loss and gradient flow;
- width-first, depth-second limiting order;
- a bounded smooth activation for the principal positive program.

The unproved proof hypotheses are separate:

- existence of the ordered trained limit;
- trained-depth homogenization;
- correctness of the retained conditional/Onsager mean;
- sufficiency of the immutable neuron label;
- source-mode compactness or weighted regularity;
- uniqueness and cutoff-uniform forced stability;
- an all-time tail mechanism.

No report should silently promote the second list into established properties of the model.

## 3. What counts as a finite neural PDE

An admissible accuracy-dependent family must satisfy the following.

1. At each approximation order it has a finite-dimensional source coordinate and finitely many fields, independent of network width \(n\), original layer count \(L\), and requested horizon.
2. It contains no \(n\times n\) matrix, width-indexed vector, finite-network checkpoint, or source dimension growing with \(n\).
3. Its initialization, drift, and readouts are emitted by a fixed architecture-local compiler using the model equations, activation, initialization law, fixed basis, finite Gaussian expectations, static parameters, and current PDE moments.
4. It cannot read positive-time dense outputs, Grams, kernels, fitting times, target trajectories, fitted closure constants, or arbitrary real encodings.
5. Its current state determines its future under the same equations; hidden replay integrals are forbidden unless promoted to explicit finite state.
6. The approximation ordering is fixed before positive-time reference data are observed.
7. Outputs and Grams are direct current moments, not separately fitted decoders.
8. Projection is applied after the width limit to the limiting operator representation; it is not a low-rank replacement of the finite dense network.
9. One family must work over the declared parameter class \(\mathcal U\), rather than encode one known curve.

Without these clauses, finite-dimensional existence is vacuous: an arbitrary continuous target curve can be packed into a two-state ODE or a one-source PDE.

## 4. The explicit operator–Hermite Liouville PDE

The immutable source-neuron type is

\[
\theta=\left(B_i(0),a_i(0)/A\right)
\sim\mu=N(0,I_{d+1}).
\]

Let \(\{\phi_\nu\}\) be normalized multivariate Hermites in \(L^2(\mu)\), ordered by complete total degree. At cutoff \(r\), retain all \(|\nu|\le r\). Their number is

\[
P_r=\binom{d+1+r}{r}.
\]

The initial action of one dense row on a slow query \(v(\theta)\) is represented cylindrically by

\[
(W_r^0v)(\theta,\varepsilon)
=\sigma_w\sum_{|\nu|\le r}
\varepsilon_\nu\langle\phi_\nu,v\rangle_\mu,
\qquad
\varepsilon\sim N(0,I_{P_r}).
\]

This is a post-width-limit Gaussian operator projection, not a rank-\(P_r\) finite network.

For each physical depth \(s\), training time \(t\), and target-neuron type \(\theta\), let \(\rho_{s,t}^{\theta}\) be the conditional law of the current row coefficients \(w=(w_\nu)\). Define

\[
H_{\nu q}(s,t)
=\int\phi_\nu(\theta)h_q(s,\theta,t)\,d\mu(\theta),
\]

\[
z_q(s,\theta,w,t)
=\sum_{|\nu|\le r}w_\nu H_{\nu q}(s,t),
\]

\[
\beta_q(s,\theta,w,t)
=\phi'(z_q)p_q(s,\theta,t).
\]

The row law obeys

\[
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\cdot\left(\rho_{s,t}^{\theta}V\right)=0,
\]

\[
V_\nu
=-\gamma\sum_qe_q^{(r)}\beta_qH_{\nu q}.
\]

The forward depth field satisfies

\[
\partial_sh_q(s,\theta,t)
=\gamma\int\phi(z_q)
\rho_{s,t}^{\theta}(dw),
\]

\[
h_q(0,\theta,t)=b(\theta,t)^\top x_q.
\]

The adjoint uses the same row coefficients:

\[
-\partial_sp_q(s,\theta,t)
=
\gamma\sum_{|\nu|\le r}\phi_\nu(\theta)
\int\mu(d\theta')
\int w_\nu\beta_q(s,\theta',w,t)
\rho_{s,t}^{\theta'}(dw),
\]

\[
p_q(1,\theta,t)=a(\theta,t).
\]

The trainable input and readout fields evolve as

\[
\dot b(\theta,t)
=-\sum_qe_q^{(r)}p_q(0,\theta,t)x_q,
\]

\[
\dot a(\theta,t)
=-\sum_qe_q^{(r)}h_q(1,\theta,t).
\]

Initialization is

\[
b(\theta,0)=B_i(0),\qquad
a(\theta,0)=A\theta_{d+1},
\]

\[
\rho_{s,0}^{\theta}
=N(0,\sigma_w^2I_{P_r}).
\]

The readouts are

\[
f_q^{(r)}(t)
=\int a(\theta,t)h_q(1,\theta,t)\,d\mu(\theta),
\]

\[
G_{qk}^{h,(r)}(s,t)
=\int h_q(s,\theta,t)h_k(s,\theta,t)\,d\mu(\theta).
\]

At every finite cutoff, the same coefficients define the forward and transpose actions. The PDE obeys

\[
\dot f^{(r)}=-\Theta_re^{(r)},
\qquad
\Theta_r\succeq0,
\]

\[
\dot{\mathcal L}_r
=-(e^{(r)})^\top\Theta_re^{(r)}\le0.
\]

These are exact identities of the finite PDE. They do not prove that the PDE is the dense-network limit.

### 4.1 Exact parity reduction

For odd activation and symmetric Gaussian initialization, sign equivariance gives

\[
b(-\theta)=-b(\theta),\quad
a(-\theta)=-a(\theta),\quad
h_q(-\theta)=-h_q(\theta),\quad
p_q(-\theta)=-p_q(\theta).
\]

Therefore all even-degree hidden coefficients vanish:

\[
H_{\nu q}=0
\quad\text{for even }|\nu|.
\]

Even learned row coordinates have zero velocity and remain inert. In the original four-label problem,

| Maximum degree | Full mode count | Active odd modes |
|---:|---:|---:|
| 1 | 5 | 4 |
| 2 | 15 | 4 |
| 3 | 35 | 24 |
| 4 | 70 | 24 |
| 5 | 126 | 80 |

Thus the proper nontrivial ladder is

\[
P=5\to35\to126\to\cdots,
\]

not \(5\to15\to35\). The compiler and cubature should enforce this symmetry exactly.

## 5. The up-to-date conjectures

Define

\[
d_{\rm obs}(\mathcal O,\widetilde{\mathcal O})
=
\|f-\widetilde f\|_2
+\sup_{s\in[0,1]}
\|G^h(s)-\widetilde G^h(s)\|_F.
\]

### 5.1 Broad finite-neural-PDE existence conjecture

There exists one predeclared admissible architecture-local family
\(\{\mathsf P_k\}_{k\ge1}\), with unique global autonomous solutions, such that

\[
\boxed{
\inf_{k\ge1}
\sup_{\vartheta\in\mathcal U}
\sup_{t\ge0}
d_{\rm obs}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\mathsf P_k,\vartheta}(t)
\right)
=0.
}
\]

This is the irreducible project claim. It includes existence of the ordered dense target.

### 5.2 Explicit pure-Hermite witness conjecture

Let

\[
E_r=
\sup_{\vartheta\in\mathcal U}
\sup_{t\ge0}
d_{\rm obs}
\left(
\mathcal O_\vartheta(t),
\mathcal O_\vartheta^{(r)}(t)
\right),
\]

with \(E_r=\infty\) if the ordered target or the finite PDE is not uniquely globally well posed.

The exact non-effective existence claim inside the fixed operator–Hermite family is

\[
\boxed{\inf_rE_r=0.}
\]

The stronger canonical Galerkin statement is

\[
\boxed{\lim_{r\to\infty}E_r=0.}
\]

The latter rules out success only along a favorable subsequence. A computable \(r(\varepsilon)\), convergence of \(\Theta_r\), an a posteriori residual certificate, and a uniform restart-neighborhood theorem are further strengthenings rather than hidden clauses.

### 5.3 Compact-time theorem target

Assume first that an infinite parity-reduced operator flow \(Y^{(\infty)}\) exists, with observables \(\mathcal O^{(\infty)}\). The strategically correct first theorem is internal convergence of the finite operator family:

\[
\boxed{
\forall T<\infty,\qquad
\lim_{r\to\infty}
\sup_{\vartheta\in\mathcal U}
\sup_{0\le t\le T}
d_{\rm obs}
\left(
\mathcal O_\vartheta^{(\infty)}(t),
\mathcal O_\vartheta^{(r)}(t)
\right)
=0.
}
\]

This separates the source-Galerkin problem from dense-limit identification and from the later all-time tail argument.

### 5.4 Ordered dense-limit identification

The separate identification theorem is

\[
\boxed{
\mathcal O_\vartheta^{(\infty)}(t)
=
\mathcal O_\vartheta(t)
}
\]

on compact training intervals, where the right-hand side is the ordered width-first, depth-second dense limit. This step contains the trained iid-depth homogenization and conditional/Onsager identification problems.

Only the combination of Sections 5.3 and 5.4 yields compact-time convergence of the explicit Hermite PDEs to the dense target.

### 5.5 Response-enriched fallback conjecture

Failure of pure Hermites would not refute the broad claim. A fixed family with maximum source degree \(r\) and mode count \(P_r\), chronological response grade \(K\), nonlinear tree grade \(J\), and depth approximation \(N\) could satisfy

\[
\lim_{\ell\to\infty}
\sup_{\vartheta\in\mathcal U}
\sup_{0\le t\le T}
d_{\rm obs}
\left(
\mathcal O_\vartheta(t),
\mathcal O_{\vartheta}^{r_\ell,K_\ell,J_\ell,N_\ell}(t)
\right)
=0
\]

along a fixed predeclared diagonal schedule. This is the leading causal fallback, not an already implemented theorem.

## 6. Theoretical support for the explicit PDE

### 6.1 Exact projected Euclidean gradient

At finite width, define the projected row coefficient

\[
w_{\ell i,\nu}^{n}
=
\sum_{j=1}^nW_{\ell,ij}\phi_\nu(\theta_j)
\]

and the hidden coefficient

\[
H_{\nu q}^{n,\ell}
=\frac1n\sum_{j=1}^n
\phi_\nu(\theta_j)h_{q,j}^\ell.
\]

Because the immutable labels do not train,

\[
\dot w_{\ell i,\nu}^{n}
=-\gamma\sum_qe_q\,
\beta_{q,i}^\ell H_{\nu q}^{n,\ell}.
\]

The Liouville velocity is therefore the direct projection of the ordinary Euclidean \(\mu\)P gradient, not a fitted curve law.

### 6.2 Hermite completeness

For every fixed \(u\in L^2(\mu)\),

\[
\|(I-\Pi_r)u\|_{L^2(\mu)}\to0.
\]

For a source-weighted Gaussian Sobolev norm

\[
\|u\|_{\mathcal H_\gamma^s}^2
=\sum_\alpha(1+|\alpha|)^s|u_\alpha|^2,
\]

one has

\[
\|(I-\Pi_r)u\|_{L^2(\mu)}
\le
(r+1)^{-s/2}
\|u\|_{\mathcal H_\gamma^s}.
\]

This proves convergence for a fixed sufficiently regular query. It does not provide a cutoff-uniform bound for the trained family.

### 6.3 Correct shared transpose

Dense training repeatedly reuses \(W\) and \(W^\top\). Treating the backward action as fresh independent Gaussian noise deletes the conditional/Onsager mean. The finite PDE instead uses the exact Hilbert adjoint of the same projected row action.

This algebraic structure is necessary. Its identification with the trained dense conditional mean after the ordered limit remains open.

### 6.4 Centered depth homogenization

Each residual slice is weighted by \(1/L\). If centered fast-depth innovations remain sufficiently decorrelated,

\[
\operatorname{Var}
\left(
\frac1L\sum_{\ell=1}^L\xi_\ell
\right)
=O(L^{-1}),
\]

while conditional means and coherent learned components remain \(O(1)\). The numerical variance slopes are almost exactly those predicted by this mechanism.

The unresolved issue is training-induced cross-depth dependence and the exact conditional mean.

### 6.5 Dissipation and residual gating

Both the dense network and every finite PDE satisfy a loss-dissipation identity. This prevents uncontrolled loss growth and explains why a small residual-compatible error need not accumulate linearly forever.

However, loss controls only selected parameter velocities. It does not coerce all hidden directions, give Hermite compactness, or prove an all-time kernel floor.

### 6.6 Exact chronological depth-response bound

At finite \(n,L\), the forward training velocity obeys

\[
v_r^{\ell+1}
=
\left(I+\frac1L A_r^\ell\right)v_r^\ell
+\frac1L F_r^\ell.
\]

The term containing \(k\) chronologically ordered dense-Jacobian continuations has a simplex-volume factor. Under the finite-time envelope

\[
\Lambda_T
=\sup_{t\le T}
\frac1L\sum_\ell\|A_r^\ell(t)\|_{\rm op}<\infty,
\]

the pure propagation tail satisfies

\[
\left\|
v-\sum_{k=0}^Kv^{[k]}
\right\|
\le
B_Te^{\Lambda_T}
\frac{\Lambda_T^{K+1}}{(K+1)!}.
\]

The backward hierarchy has the same exact-source bound. This is a real-axis Volterra/Dyson expansion in residual depth, not a Taylor series in training time.

It does not control source-substitution error, nonlinear chain-rule branches, or every high-to-low Gaussian contraction. Those are the remaining response residual.

## 7. Direct empirical evidence

### 7.1 Canonical benchmark

Against the pooled \(n=256,L=32\), 128-seed dense reference:

| Metric | Result |
|---|---:|
| PDE feature motion | \(0.633801\) |
| Dense feature motion | \(0.639909\) |
| Maximum output gap | \(1.0753\times10^{-2}\) |
| Maximum loss-of-ensemble-mean gap | \(1.8457\times10^{-3}\) |
| Maximum absolute Gram gap | \(1.9408\times10^{-2}\) |
| Gram-increment surface gap | \(7.2433\times10^{-3}\) |
| Gram-increment gap / PDE feature motion | \(1.1428\%\) |

The Gram discrepancy is statistically resolved, with \(p\) approximately \(0.003\). The correct wording is “close but distinguishable,” not “exact” or “below the noise floor.”

The same fixed PDE remained flat from \(t=8\) to \(t=32\), with output and Gram drift around \(4\)–\(5\times10^{-13}\). This rules out a short local-time Taylor fit in the simulated PDE. Dense comparisons were principally through \(t=8\), so this is not all-time dense validation.

![Canonical PDE versus dense loss, outputs, and Gram evolution](figures/pde_vs_dense_curves.png)

*Figure 1. Original canonical comparison. The \(P=5\) PDE closely tracks the
finite dense ensemble over the active transient, including the full
time-by-depth Gram-increment field. The discrepancy is small but statistically
resolved, so the correct conclusion is “close,” not “exact.”*

![Autonomous PDE plateau continuation](figures/pde_plateau_tail.png)

*Figure 2. Original autonomous \(t=8\to32\) PDE continuation. The residual and
Gram drift are at numerical floor. This rejects a short-time Taylor-fit
interpretation of the simulated PDE, but it is not a dense-network all-time
theorem.*

### 7.2 Generalization without retuning

The same \(P=5\) PDE was tested on 14 preregistered configurations:

- four label changes;
- two input geometries;
- \(m=2,3,4,5\);
- \(\tanh\), normalized erf, and normalized arctangent;
- two crossed stress cases.

| Full-curve normalized error | Median | Maximum |
|---|---:|---:|
| Gram increment | \(1.71\%\) | \(4.14\%\) |
| Output increment | \(1.46\%\) | \(1.83\%\) |
| Loss | \(0.63\%\) | \(1.97\%\) |

All cases showed active feature learning. The PDE/dense feature-motion ratio stayed between \(0.977\) and \(1.023\). Label transfer was especially clean, with maximum Gram/output/loss errors \(1.56\%/1.47\%/1.41\%\).

Qualifications:

- the simultaneous 95% critical increment was \(5.94\%\), larger than the \(5\%\) equivalence threshold, so the deliberately severe joint certification was underpowered;
- six configurations were unresolved at the PDE-resolution level;
- four failed the two-window plateau requirement: X2 passed the final window but not the previous one, while M4, M5, and I2 remained active at \(t=32\);
- this is broad descriptive portability, not a uniform theorem over an infinite problem class.

![All-case normalized errors and simultaneous uncertainty bounds](figures/generalization_all_case_errors.png)

*Figure 3. Existing 14-case error summary. Every observed Gram, output, and
loss error is below the \(5\%\) line, while the black joint upper-confidence
bounds show why the deliberately severe simultaneous certification remained
boundary/unresolved.*

![All-case PDE and dense Gram-motion curves](figures/generalization_gram_motion_curves.png)

*Figure 4. Existing PDE-versus-dense Gram-motion curves for all 14 transfer
configurations through \(t=32\). The curves show active, nonlazy feature
motion; the harder \(M4\), \(M5\), and \(I2\) cases remain visible.*

### 7.3 Ordered-limit diagnostics

Successive width-correction ratios were

\[
0.462,\qquad0.488,\qquad0.518,
\]

and the tested depth-correction ratio was

\[
0.578.
\]

These are favorable finite-grid trends, but heuristic remaining tails were still \(4.2\%\)–\(5.1\%\) in width and \(1.75\%\) in depth.

The trained centered-depth variance slopes were

\[
-1.00219\quad\text{forward},
\qquad
-0.99982\quad\text{backward}.
\]

This strongly supports \(L^{-1}\) centered variance. It does not validate the retained conditional/Onsager mean.

These scaling and variance results came from a reduced \(T=0.5\), single-configuration diagnostic with four coupled roots, not from the full 14-case transfer study.

### 7.4 State sufficiency and stability diagnostics

A perturbation invisible to all retained \(P\le35\) coordinates and to current output, Grams, adjoints, and tangent kernel produced a maximum continuation gap of \(0.332\%\). No gross projectability counterexample was found, but one null attack cannot prove static-state sufficiency.

Two independent \(P=5\) cubature scrambles differed by only \(0.0335\%\) in the normalized observable metric. Low-order numerical consistency is favorable; high-order cofinal resolution remains much harder.

Short shadow discrepancies were tiny. No worst-direction, cutoff-uniform stability estimate has been obtained.

## 8. Adversarial audit of the nonlazy-linear hypothesis

“Linear explainability” has several distinct meanings. The experiments address them differently.

### 8.1 Lazy or frozen-feature explanation

The canonical PDE hidden Gram moved by \(0.6338\), essentially the same \(O(1)\) amount as the dense reference. Every generalization case showed active feature motion.

This explanation is rejected.

### 8.2 Exact identity or deep-linear activation

For

\[
\phi_c(z)=\frac{\tanh(cz)}{c},
\]

the dense nonlinear versus identity Gram distances were

\[
22.44\%,\quad36.38\%,\quad45.82\%
\]

for \(c=1,2,4\), while the matched nonlinear PDE errors were

\[
1.20\%,\quad1.09\%,\quad1.18\%.
\]

Using the identity PDE on the nonlinear target produced correspondingly large errors. Exact identity/deep-linear dynamics are rejected.

### 8.3 Pure training-clock explanation

After reparameterizing trajectories by fractional loss progress, the \(c=2\) nonlinear and identity Gram paths remained \(27.14\%\) apart, while the PDE contrast error was \(1.34\%\).

A scalar time reparameterization is rejected.

### 8.4 Fixed gain-adjusted linear explanation

The first \(c=2\) experiment left this loophole open: the initialization-gain-matched linear control was only \(3.46\%\) from the nonlinear dense Gram curve, with 95% interval \(3.25\%\)–\(3.67\%\).

The later scalar stress used

\[
\phi(z)=\frac{\sin(2.5z)}{2.5},
\]

which is smooth, odd, bounded, and 1-Lipschitz. At initialization, \(62.14\%\) of its Gaussian \(L^2\) energy lies outside its best linear Hermite component.

| Comparison | Gram | Output | Loss |
|---|---:|---:|---:|
| Initialization-gain linear vs degree-11 sine PDE | \(17.70\%\) | \(7.12\%\) | \(7.51\%\) |
| RMS-gain linear vs sine PDE | \(8.68\%\) | \(3.95\%\) | \(4.68\%\) |
| Paired dense linear vs dense sine | \(15.95\%\) | \(6.55\%\) | \(6.95\%\) |
| Degree-11 sine PDE vs dense sine | \(2.50\%\) | \(2.81\%\) | \(5.54\%\) |

All eight paired dense seeds had Gram separation between \(14.40\%\) and \(18.75\%\).

Therefore:

> The fixed initialization-gain control fails directly in paired dense Gram dynamics. The RMS-gain control also fails against the nonlinear PDE Gram path and is therefore strongly disfavored, although it was not separately run as a paired dense control. The nonlinear PDE captures most of the dense nonlinear difference.

Qualifications:

- the dense stress used \(n=128,L=16\) and eight paired seeds;
- the PDE loss error was \(5.54\%\), just outside the joint \(5\%\) rule;
- the experiment does not rule out every adaptive, time-dependent, or state-dependent linear surrogate.

![Earlier activation-linearity falsification study](figures/activation_linearity_smoking_gun.png)

*Figure 5. Existing figure from the earlier activation-continuation study. It
decisively rejects the identity/deep-linear explanation and shows the matched
nonlinear PDE tracking the \(c=2\) Gram curve. It also records the then-open
\(3.46\%\) gain-matched loophole; that loophole was closed later by the scalar
sine stress summarized in the table above, for which no pre-existing figure
was available.*

### 8.5 Why low source degree is not a linear activation model

Every source cutoff evaluates the complete nonlinear functions \(\phi(z)\) and \(\phi'(z)\). The cutoff acts only on dependence on the immutable Gaussian neuron label.

Thus

\[
\text{activation nonlinearity}
\neq
\text{source-label Hermite complexity}.
\]

This explains how a degree-one source model can reproduce strongly nonlinear activation dynamics.

### 8.6 The surviving “less interesting” explanation

The serious live downgrade is:

> The tested outputs and Grams may lie on an exceptionally low-complexity nonlinear manifold in the immutable neuron label, so the small PDE is an excellent nonlinear surrogate but not the first rung of a convergent arbitrary-accuracy hierarchy.

That would not make the result trivial. The PDE would remain autonomous, width-independent, nonlinear, nonlazy, and portable. It would downgrade the theory from a systematic arbitrary-accuracy construction to a robust low-order closure with a possible error floor.

## 9. What higher source Hermites currently do

In this section, “degree” means maximum retained Hermite degree, while \(P\) denotes the corresponding total mode count. For the four-label canonical problem, degrees \(1,3,5\) correspond to \(P=5,35,126\).

### 9.1 The superseded adverse comparison

The old \(P=5\to15\to35\) comparison treated the exactly inert quadratic shell as a physical refinement. With parity-paired cubature,

\[
P=5\equiv P=15
\]

to \(10^{-17}\) at positive time. The old ratios \(2.54\)–\(26.53\) were ratios against numerical symmetry leakage.

The old rank-five POD advantage was also not an equal-active-rank comparison: five active POD mixtures were compared with four active linear Hermites plus an inert constant. It suggests possible basis inefficiency, but does not prove it.

### 9.2 Correct newly opened odd-shell source

On the proper \(P=5\to35\to126\) ladder, the lifted newly opened source ratio was

\[
0.0290,\quad0.0320
\quad\text{at }t=0.25,
\]

and

\[
0.0589
\quad\text{at }t=0.5.
\]

This is a \(17\)–\(34\times\) contraction. It is not the actual trained aggregate tail.

Actual high-to-low feedback grew by factors \(1.389\), \(1.461\), and \(1.423\); observable-generator defects grew by factors \(1.424\), \(1.644\), and \(1.759\). The observable differences were only \(0.0021\%\)–\(0.0079\%\), but their adjacent ordering was noncontracting.

### 9.3 Degree-seven common-reference mechanism

At \(t=0.25\):

- aggregate state commutator ratio: \(1.3257\);
- observable-generator ratio: \(1.6174\);
- shell-cardinality-adjusted state ratio: \(0.9056\);
- RMS-per-mode ratios for \(c,\dot c,h,p\): \(0.865,0.865,0.903,0.965\);
- actual trained \(\dot c\) shell ratio: \(1.2665\).

More than \(99.998\%\) of each dominant \(B\)-defect stayed in its newly added Hermite shell. The adjacent weighted cosine was

\[
4.62\times10^{-4}.
\]

This disfavors a few-mode resonance. What is ruled out at that checkpoint is coherent alignment of the adjacent dominant \(B\)-increments. The new shell contains more, individually weaker, nearly orthogonal modes. Aggregate summability is still unproved.

### 9.4 Actual coupled Cauchy ledger

At \(t=0.25\):

| Metric | Degree \(3\to5\) | Degree \(5\to7\) | Ratio |
|---|---:|---:|---:|
| Projective state error | \(1.3116\times10^{-3}\) | \(1.7338\times10^{-3}\) | \(1.3219\) |
| Observable gap | \(2.1913\times10^{-5}\) | \(3.5846\times10^{-5}\) | \(1.6358\) |
| Feedback commutator | \(7.2584\times10^{-3}\) | \(9.6224\times10^{-3}\) | \(1.3257\) |

The final-time realized secant quotients were \(1.08921\) and \(1.08771\), a ratio of \(0.99862\). This found no increase in amplification for that one realized forcing direction. It is not a worst-case propagator norm and does not prove cutoff-uniform stability.

### 9.5 Scalar degree-eleven and degree-thirteen ladder

For the sine stress at \(y=2\), distances to degree 11 were

\[
0.339\%,\;0.369\%,\;0.297\%,\;0.205\%,\;0.194\%
\]

for degrees \(1,3,5,7,9\). At \(y=4\), distances to degree 13 were

\[
0.247\%,\;0.274\%,\;0.233\%,\;0.178\%,\;0.174\%,\;0.115\%
\]

for degrees \(1,3,5,7,9,11\).

There is a small broad reduction after degree three, but no monotonicity. The complete correction is below \(0.34\%\).

Against the dense sine mean, higher order did not improve the Gram error systematically:

\[
2.4235\%\quad\text{at degree 1},
\]

\[
2.3671\%\quad\text{at degree 3},
\]

\[
2.4972\%\quad\text{at degree 11}.
\]

Degree three therefore gave a small improvement over degree one, but degree eleven was worse than degree one.

For canonical \(\tanh\), two well-conditioned degree-\(13\) scrambles gave

\[
\frac{E_{11\to13}}{E_{9\to11}}
=0.958,\qquad1.913.
\]

The apparent turnover did not replicate. The corresponding Gram effects were only \(0.00462\%\) and \(0.00608\%\).

### 9.6 Current Hermite verdict

The strongest honest statement is:

> Higher source Hermites make very small corrections and show favorable shellwise structure, but no replicated aggregate Cauchy contraction has been observed.

This is a major gap for the arbitrary-accuracy pure-Hermite theorem. It is not a problem for the current low-order practical accuracy.

## 10. The exact analytic obstruction after the latest correction

Let

\[
H=L^2(\mu)
\]

be the immutable source-neuron Hilbert space, and let a common isonormal process \(W\) act by

\[
\mathbb E[W(u)W(v)]
=\langle u,v\rangle_H.
\]

The embedding \(Iu=W(u)\) has Hilbert adjoint \(T_W=I^\ast\):

\[
\langle T_W\beta,u\rangle_H
=\mathbb E[\beta W(u)],
\]

\[
\|T_W\beta\|_H\le\|\beta\|_2.
\]

In Hermite coordinates,

\[
T_W\beta
=\sum_\nu\phi_\nu
\mathbb E[\epsilon_\nu\beta].
\]

This yields an important correction to the earlier tail report:

> Malliavin differentiability is not separately required merely to define the frozen transpose or to prove consistency on one fixed compact trajectory.

The Riesz adjoint is bounded. It is not compact. Taking

\[
\beta_\nu=\epsilon_\nu
\]

gives

\[
T_W\beta_\nu=\phi_\nu,
\]

so

\[
\sup_{\|\beta\|_2\le1}
\|(I-\Pi_r)T_W\beta\|_H=1
\]

for every finite \(r\).

For a learned row field \(c\in L^2(\theta,\omega;H)\), define

\[
T_c\beta=\mathbb E_{\theta,\omega}[c\,\beta].
\]

The total shared transpose is

\[
\boxed{
A_c^\ast\beta
=\sigma_wT_W\beta+T_c\beta.
}
\]

Both the frozen and learned terms must be controlled in any weighted tail estimate.

Thus strong projection convergence is uniform on compact sets, not on the energy-bounded unit ball.

### 10.1 What the energy identity gives

In the Lagrangian characteristic metric, the finite systems satisfy an identity of the form

\[
-\dot{\mathcal L}_r
=
\|\dot b_r\|^2
+\|\dot a_r\|^2
+\int_0^1\|\dot c_r(s)\|^2\,ds.
\]

Consequently, for every fixed \(T\), this identity directly controls the trainable Lagrangian state:

\[
\sup_r\sup_{t\le T}
\|(b_r,a_r,c_r)(t)\|<\infty,
\]

and

\[
\|(b_r,a_r,c_r)(t)-(b_r,a_r,c_r)(s)\|
\lesssim |t-s|^{1/2}.
\]

The derived depth fields \(h_r,p_r,\beta_r\) require separate cutoff-uniform forward/backward boundary-value estimates before the same conclusion applies to a full state \(Y_r\). Even after those estimates, energy boundedness does not give source-mode compactness.

### 10.2 Why plain \(L^2\) stability is false

The adjoint nonlinearity contains

\[
(z,p)\mapsto\phi'(z)p.
\]

For two states,

\[
\delta\beta
=
\phi'(z)\delta p
+\widetilde p
\left[\phi'(z)-\phi'(\widetilde z)\right].
\]

The second term contains \(\widetilde p\,\delta z\). On an \(L^2\) ball, both factors may be only \(L^2\), so the product need not lie in \(L^2\). The obstruction is already present at initialization because

\[
p(1,\theta)=a(\theta)=A\theta_{d+1}
\]

is an unbounded Gaussian coordinate.

Therefore the previously convenient claim of cutoff-uniform local Lipschitzness in plain \(L^2\) is false.

### 10.3 Strongest valid compact-time reduction

Two proof routes remain.

**Compactness and uniqueness.** If

\[
\{Y_r(t):r\ge1,\;0\le t\le T\}
\]

is norm-precompact in a topology controlling the nonlinear drift and the output/Gram readouts, and the limiting Hilbert problem is unique, energy equicontinuity plus compact-set consistency yields strong convergence in \(C([0,T])\). Alternatively, weak compactness must be supplemented by convergence of norms or energy and a weak–strong uniqueness principle.

The cutoff acts only on the row/query operator coordinate. Write

\[
\mathcal P_r
=
\mathrm{Id}_{\rm slow}\oplus\Pi_r
\]

for the corresponding block projection, which leaves \(b,a,h,p\) unprojected and applies \(\Pi_r\) only to the source index of the learned row/operator block.

**Forced stability.** If an infinite solution \(Y\) exists and projected flows obey a cutoff-uniform forced gain \(G_T\), then

\[
\sup_{t\le T}\|Y_r(t)-\mathcal P_rY(t)\|
\le
G_T
\int_0^T
\|F_r(\mathcal P_rY)-\mathcal P_rF(Y)\|\,dt.
\]

Compactness of the fixed limiting trajectory makes the consistency defect vanish.

The decisive compact-time bundle is therefore:

\[
\boxed{
\begin{array}{l}
\text{collective source-mode compactness or propagated weighted regularity,}\\
\text{uniqueness or weak–strong uniqueness,}\\
\text{cutoff-uniform forced stability in a stronger-to-weaker topology.}
\end{array}
}
\]

The measured \(0.99862\) secant-gain ratio is compatible with this program, but it is not a uniform stability theorem.

## 11. What is established, disfavored, and open

### 11.1 Established

- The finite-\((n,L)\) Euclidean \(\mu\)P gradients, adjoints, PSD tangent kernel, and loss dissipation are exact.
- A literal width-independent operator–Liouville PDE was written and integrated.
- Its finite-cutoff forward/transpose pairing is exact.
- Its finite-cutoff projected-gradient, PSD-kernel, output, Gram, autonomy, and restart identities are exact.
- The canonical low-order PDE produces \(O(1)\) feature motion and a genuine plateau.
- The parity reduction for odd activation and symmetric initialization is exact.
- The old initial-source/feature-time Wick–Taylor compiler is false for the unbounded quadratic/Gaussian model; its associated physical-time closures fail uniformly.
- A one-time row law or a finite Gram list is not an exact general closure of dense matrix reuse.
- Replacing \(W^\top\) by an independent Gaussian copy is algebraically wrong.
- Raw iid depth matrices do not become a smooth nondegenerate matrix field \(W(s)\).

### 11.2 Strongly supported or strongly disfavored

- Accurate low-order PDE prediction across the tested dense benchmarks is strongly supported.
- Fine tuning to one label or input configuration is strongly disfavored.
- Static/lazy feature learning, exact identity dynamics, and pure training-clock explanations are rejected.
- The initialization-gain explanation is rejected by paired dense runs in the scalar sine stress. The RMS-gain control is rejected relative to the nonlinear PDE Gram path, but was not separately run as a paired dense control.
- Centered trained-depth innovations exhibit the predicted \(L^{-1}\) variance scaling.
- A gross failure of static-state sufficiency was not found.
- A few-mode high-shell resonance is disfavored; coherent alignment of adjacent dominant \(B\)-increments is ruled out at the tested degree-seven checkpoint.
- Ordinary time-stepping error and low-order cubature noise are not credible explanations of the canonical PDE/dense discrepancy.

### 11.3 Open

- Existence and uniqueness of the ordered trained dense limit.
- Identification of the infinite operator PDE with that limit.
- The correct trained conditional/Onsager mean after depth homogenization.
- Sufficiency of the static immutable label.
- Pure-Hermite compact-time convergence.
- Collective source-mode compactness or a propagated weighted regularity estimate.
- Cutoff-uniform forced stability and weak–strong uniqueness.
- Cofinal high-order cubature convergence.
- Uniform approximation on an infinite activation/data class.
- Compact-time-to-all-time control.
- A fully emitted and proved response-enriched finite PDE.
- Whether the successful low-order PDE has a nonzero irreducible error floor.

### 11.4 Model-specific negative results that must not be overgeneralized

The earlier quadratic/Gaussian network has unbounded polynomial feedback and an unbounded trainable Gaussian readout. Its formal limiting feature-time Wick series has zero radius, its associated physical-time closures fail uniformly, and a later causal-DMFT analysis yields an instantaneous-fitting step trace in the natural relaxed class.

Those results rule out the corresponding continuous uniform finite closure for that model. They do not prove a no-go theorem for the present bounded residual-\(\tanh\) model.

Normalization also fails to produce exact finite natural moment closure, but it introduces signed cancellations, so the positive-coefficient quadratic lower bound does not transfer automatically.

## 12. The fixed-order mean-field derivative/Wick calculus

The earlier notes developed a detailed algebra for computing arbitrary fixed-order training derivatives and their Gaussian mean-field limits.

The key phrase is **arbitrary fixed order**:

> For every selected order \(k\), the calculus emits a finite expression and a finite Gaussian contraction. It does not emit one finite state closed under all orders, and it does not imply convergence of the resulting feature-time Wick series or of the induced physical-time closure.

### 12.1 Feature-time reduction

For the earlier single-output squared-loss model with centered initialization \(H(0)=0\), the physical gradient flow for label \(y\) follows the same parameter orbit as readout ascent under a scalar residual clock:

\[
\dot\tau=2(y-H(\tau)),
\qquad
f(t)=H(\tau(t)).
\]

The displayed loss derivatives below specialize to \(y=1\).

Writing

\[
k_j=H^{(j+1)}(0),
\]

the first loss derivatives are universal polynomials:

\[
\mathcal L'(0)=-4k_0,
\]

\[
\mathcal L''(0)=16k_0^2-8k_1,
\]

\[
\mathcal L'''(0)
=-64k_0^3+112k_0k_1-16k_2.
\]

Under antipodal symmetry, the even feature-time derivatives vanish. With

\[
A=H'(0),\qquad B=H'''(0),\qquad C=H^{(5)}(0),
\]

one obtains

\[
H(\tau)
=A\tau+\frac{B}{3!}\tau^3+\frac{C}{5!}\tau^5+\cdots.
\]

Thus low-order loss coefficients can be expressed exactly through finitely many network-dependent Gaussian jets.

### 12.2 Activation and normalization derivatives

For a normalized activation map

\[
N(x)
=
\frac{\phi(x)}
{\sqrt{\langle\phi(x)^2\rangle+\varepsilon}},
\]

the calculus explicitly computes \(N'\), \(N''\), \(N'''\), and in principle all higher derivatives.

For example, with \(y=\phi(x)\), \(s^2=\langle y^2\rangle+\varepsilon\), \(y_p=\phi'(x)p\), and \(r_p=\langle y,y_p\rangle\),

\[
N'[p]
=\frac{y_p}{s}
-\frac{yr_p}{s^3}.
\]

The second and third derivatives add:

- higher activation derivatives \(\phi'',\phi'''\);
- derivatives of reciprocal normalization factors;
- outer-product projector attachments;
- Bell-partition terms;
- disconnected population contractions.

The jets are propagated through the network as

\[
v_1,v_2,v_3
\longrightarrow
z_1,z_2,z_3
\longrightarrow
u_1,u_2,u_3,
\]

then through differentiated backpropagated messages and Hessian-gradient blocks.

One resulting exact coefficient has the form

\[
B_{\rm RMS}
=2T_{\rm RMS}+4Q_{\rm RMS},
\]

where \(T_{\rm RMS}\) is an explicit forward third-jet contraction and \(Q_{\rm RMS}\) is a sum of squared Hessian-gradient contractions. Wick expansion reduces these to finite combinations of expectations of

\[
\phi(G),\quad
\phi'(G),\quad
\phi''(G),\quad
\phi'''(G),\ldots
\]

and Gaussian moments.

### 12.3 The algebraic objects it tracks

At increasing order, the calculus generates:

- ordered \(W\) and \(W^\top\) reuse words;
- activation-derivative trees;
- Bell partitions from composite and reciprocal derivatives;
- learned rank-one insertions;
- projector and outer-product attachments;
- population-moment contractions;
- Wick pairings and disconnected components.

This machinery is exact and highly useful for:

- checking model scalings;
- deriving initial jets;
- proving symmetry and parity identities;
- generating independent code-level audits;
- deriving source-response equations;
- identifying which moments or histories a proposed closure omits.

### 12.4 Why it did not close

Even a frozen-block moment recurrence has the form

\[
M_{p,r}'
=c_1M_{p-1,r+2}
+c_2M_{p+1,r}
+c_3M_{p,r+2}.
\]

No finite polynomial-moment cutoff is invariant.

For the unbounded quadratic/Gaussian model, the failure is stronger. Along odd \(k\), with \(m=(k+3)/2\), the limiting Wick–Taylor coefficients satisfy

\[
c_k
\ge
m!\,b_\gamma^m q_0^{k+1}
\binom{k+2}{2}.
\]

Hence

\[
\limsup_{k\to\infty}c_k^{1/k}=\infty.
\]

The formal limiting feature-time Wick series has radius zero. Its positive partial sums, when inserted into the residual clock, create a physical-time initial boundary layer rather than a uniformly convergent closure. This is not a blanket statement about the exact finite-width physical-time Taylor series.

### 12.5 Correct use in the present project

The calculus should not be used to argue:

\[
\text{“we can compute all Taylor coefficients”}
\Longrightarrow
\text{“the Taylor series converges”}.
\]

Its best current use is different:

> Differentiate the forward, adjoint, row, and conditional-response equations with respect to immutable Gaussian source variables; then estimate finitely many source derivatives in a weighted norm.

Compactness requires some finite positive source regularity \(s>0\), not training-time analyticity or an all-orders Taylor theorem.

## 13. The causal response and Onsager calculus

The later calculus attacks the actual causal difficulty: dense matrices are reused in both orientations and accumulate learned low-rank history.

### 13.1 Exact memory identities

At finite \(n,L\),

\[
W_\ell(t)
=
W_\ell^0
-\frac1n\sum_q
\int_0^t
e_q(\tau)
\beta_q^\ell(\tau)
h_q^\ell(\tau)^\top
d\tau.
\]

Therefore

\[
W_\ell(t)h_r^\ell(t)
\]

and

\[
W_\ell(t)^\top\beta_r^\ell(t)
\]

depend on two-training-time covariances and responses. Eliminating \(W_\ell\) exactly produces memory; it does not yield a current-Gram closure.

This is why two networks can share the same current row marginals, outputs, Grams, and present forward/backward actions while differing in a future response direction.

### 13.2 Exact chronological hierarchy

Let

\[
v_r^\ell=\partial_t h_r^\ell,
\qquad
A_r^\ell=\gamma D_r^\ell W_\ell.
\]

Then

\[
v_r^{\ell+1}
=
\left(I+\frac1L A_r^\ell\right)v_r^\ell
+\frac1L F_r^\ell.
\]

The response field \(q^k\) records \(k\) ordered dense-Jacobian continuations:

\[
q^{k,\ell+1}
=
q^{k,\ell}
+\frac1L A_r^\ell q^{k-1,\ell}.
\]

The backward fields \(r^k\) retain the reversed orientation \(A^\top\). Under the finite-time operator envelope \(\Lambda_T\),

\[
\left\|
v-\sum_{k=0}^Kq^k
\right\|
\le
B_Te^{\Lambda_T}
\frac{\Lambda_T^{K+1}}{(K+1)!}.
\]

The factorial is the volume of an ordered depth simplex. It is unaffected by the zero-radius training-time result.

For a coupled approximation, the backward source is itself truncated. The additional error

\[
e^{\Lambda_T}E_{A,K,T}
\]

must be controlled separately. This is the main reason the pure Dyson bound is not already a closure theorem.

### 13.3 Oriented grammar

The causal algebra distinguishes

\[
\mathsf F_{r,j}u
=
\operatorname{diag}(\phi^{(j)}(z_r))Wu,
\]

\[
\mathsf B_{r,j}u
=
W^\top
\operatorname{diag}(\phi^{(j)}(z_r))u,
\]

and the learned insertions

\[
\mathsf U_qu
=
\beta_q\langle h_q,u\rangle,
\qquad
\mathsf V_qu
=
h_q\langle\beta_q,u\rangle.
\]

Word order and orientation are never commuted.

The proposed response compiler has distinct complexity axes:

- \(K\): chronological response grade;
- \(J\): nonlinear derivative-tree complexity;
- \(N\): depth approximation;
- algebraic population coefficients;
- historical coefficients \(\kappa_\alpha\), each with an autonomous residual-gated ODE.

Sequential joint conditioning of \(W^0u\) and \((W^0)^\top v\) produces the correct conditional mean. At initialization, it recovers the elementary Onsager/Stein identity

\[
\mathbb E
\left[
(W^0)^\top\varphi(W^0h)
\mid h
\right]
=
\sigma_w^2
\mathbb E[\varphi'(Z)]h.
\]

### 13.4 What survived audit

The following are real:

- the finite-network \(q/r\) identities;
- the pure chronological factorial tail;
- the orientation-preserving conditioning formulas;
- the necessity of conditional response/history information;
- rapid empirical decay with response grade.

Across the completed finite-matrix response runs, median output errors decreased from

\[
8.51\times10^{-3}
\quad(K=0)
\]

to

\[
9.77\times10^{-7}
\quad(K=3),
\]

while Gram errors decreased from

\[
2.50\times10^{-2}
\]

to

\[
6.08\times10^{-6}.
\]

These surrogates retained dense matrices. They are strong causal compression evidence, not admissible finite PDEs.

![Response-grade error contraction across sixteen long-horizon runs](figures/order_convergence.png)

*Figure 6. Existing long-horizon \(q/r\) response-grade summary. Output and
all-depth Gram errors contract sharply from \(K=0\) to \(K=3\) across the 16
completed runs. Every surrogate here still retains the dense matrices.*

![Representative exact and response-projected trajectories](figures/representative_curves.png)

*Figure 7. Existing representative \(T=32\) response-hierarchy trajectory,
including loss, Gram motion, prefix errors, and Gram speed. This is
finite-matrix causal-compression evidence, not a compiled width-independent
Liouville PDE and not an infinite-time certificate.*

The earlier \(K/J/N\) prose compiler did not actually emit all tag tables, historical coordinates, conditional kernels, and finite drift DAGs. It must not be described as an implemented finite PDE.

## 14. Exact bridge between Hermites, responses, and Onsager terms

The two calculi connect through Gaussian integration by parts and the shared isonormal row.

### 14.1 Hermite coefficients are Gaussian responses

For a sufficiently regular function \(F(\theta)\) of the immutable Gaussian source label \(\theta\) and normalized source Hermites \(H_\alpha(\theta)\),

\[
\mathbb E[F(\theta)H_\alpha(\theta)]
=
\frac{1}{\sqrt{\alpha!}}
\mathbb E[\partial_\theta^\alpha F(\theta)].
\]

Thus a high Hermite coefficient is a high Gaussian source-response coefficient. This does not make it a high training-time derivative.

The relevant expansion axes are:

| Axis | Meaning |
|---|---|
| Training-time jet order | Repeated differentiation along gradient flow |
| Maximum source Hermite degree \(r\), mode count \(P_r\) | Dependence on immutable Gaussian neuron labels |
| Response grade \(K\) | Chronologically ordered dense-Jacobian reuse |
| Tree grade \(J\) | Nonlinear chain-rule branching |

Convergence in one axis does not imply convergence in another.

### 14.2 Riesz/Stein representation of the transpose

The frozen shared transpose is

\[
T_W\beta
=
\sum_\nu\phi_\nu
\mathbb E[\epsilon_\nu\beta].
\]

When Gaussian differentiability is available,

\[
\mathbb E[\epsilon_\nu\beta]
=
\mathbb E[\partial_{\epsilon_\nu}\beta].
\]

This is first-order Stein differentiation in the row-noise coordinate \(\epsilon_\nu\). The coordinate is indexed by the source basis function \(\phi_\nu\), but a large source degree \(|\nu|\) is not a high derivative order in \(\epsilon\). Source-label differentiation \(\partial_\theta^\alpha\) and row-noise differentiation \(\partial_{\epsilon_\nu}\) are distinct operations.

Therefore the same coefficient can be viewed as:

- a Hermite transpose coefficient;
- a Gaussian directional response;
- an Onsager/Stein coefficient.

This is a precise mathematical connection, not an analogy.

### 14.3 Learned row response

Choose a common Lagrangian characteristic coupling of the row law and write the row characteristic as

\[
w_\mu
=\sigma_w\epsilon_\mu+c_\mu(\epsilon),
\]

\[
z_q
=\sum_\mu w_\mu H_{\mu q},
\qquad
\beta_q=\phi'(z_q)p_q.
\]

Define

\[
R_{\nu\mu}
=\partial_{\epsilon_\nu}c_\mu.
\]

The Eulerian law \(\rho\) does not in general determine this coupling or \(R\). Therefore the following response lift is a theorem device only if its estimate is shown to be invariant under the admissible coupling; otherwise \(R\), or only the query contractions it generates, must be promoted to explicit response-enrichment state.

Holding the slow macroscopic fields fixed in the local tagged response,

\[
\partial_{\epsilon_\nu}\beta_q
=
\phi''(z_q)p_q
\left[
\sigma_wH_{\nu q}
+\sum_\mu R_{\nu\mu}H_{\mu q}
\right].
\]

Since

\[
\dot c_\mu
=-\gamma\sum_qe_q\beta_qH_{\mu q},
\]

the local row response obeys

\[
\boxed{
\dot R
=-\gamma\sum_qe_q
\phi''(z_q)p_q
\bigl[(\sigma_wI+R)H_q\bigr]
\otimes H_q.
}
\]

Global perturbations of \(e\), \(p\), and \(H\) belong to the larger \(q/r\) hierarchy and should not be silently folded into this local equation.

On such a characteristic lift, this identity exposes the mechanism that the plain \(L^2\) argument misses:

- the dangerous transpose tail is not generated arbitrarily;
- it is produced through the trained query family \(H_q\);
- the learned row response \((\sigma_wI+R)H_q\) controls how Gaussian reuse creates Onsager feedback;
- source-label and row-noise derivatives generate related activation-derivative and Bell trees computed by the old calculus, while remaining distinct derivative systems.

### 14.4 What higher Hermites do and do not mean for Onsager corrections

Higher Hermites are not simply “higher Onsager corrections.”

- An Onsager term is a conditional mean caused by reusing the same random operator.
- Hermite degree resolves how that conditional mean depends on immutable Gaussian source directions.
- Chronological response grade resolves how many ordered dense reuses occur through depth and training.

Onsager effects can occur at very low source degree. Conversely, a high source Hermite can encode nonlinear label dependence without adding chronological memory.

The correct synthesis is a multi-axis hierarchy, not an identification of source degree \(r\) or mode count \(P_r\) with response grade \(K\).

## 15. A concrete theorem program

### 15.1 Weighted source space

Let the Gaussian number operator be

\[
\mathsf N\phi_\nu=|\nu|\phi_\nu,
\]

and define

\[
H_\gamma^s
=D((I+\mathsf N)^{s/2}).
\]

Then

\[
\|(I-\Pi_r)u\|_{L^2}
\le
(1+r)^{-s/2}
\|u\|_{H_\gamma^s}.
\]

A targeted sufficient estimate on every compact interval is

\[
\sup_r\sup_{t\le T}\mathcal E_s[Y_r(t)]<\infty
\]

for some \(s>0\), where \(\mathcal E_s\) controls:

\[
\sum_q
\left(
\|h_q\|_{H_\gamma^s}^2
+\|p_q\|_{H_\gamma^s}^2
\right),
\]

\[
\int_0^1
\mathbb E
\left[
\|c\|_{H_\gamma^s}^2
+\sum_q
|p_q|^2
\left\|
(I+\mathsf N)^{s/2}
(\sigma_wI+R)H_q
\right\|^2
\right]ds,
\]

together with the fourth-moment or Gaussian-Orlicz control needed for products involving the unbounded terminal adjoint.

This is a sufficient route, not a necessary formulation of compactness. Because \(R\) lives on a Lagrangian response lift, this estimate closes the pure Eulerian state only after coupling-invariance or a law-determined representation is proved. Otherwise it is an estimate for a response-enriched state.

### 15.2 How the response identity controls the transpose tail

The local response formula gives schematically

\[
\|T_W\beta_q\|_{H_\gamma^s}^2
\lesssim
\|\phi''\|_\infty^2
\mathbb E
\left[
|p_q|^2
\left\|
(I+\mathsf N)^{s/2}
(\sigma_wI+R)H_q
\right\|^2
\right].
\]

For the learned transpose,

\[
\|T_c\beta\|_{H_\gamma^s}
\le
\left(
\mathbb E
\|c\|_{H_\gamma^s}^2|\beta|^2
\right)^{1/2}.
\]

Consequently,

\[
\|(I-\Pi_r)A_c^\ast\beta\|_{L^2}
\lesssim
(1+r)^{-s/2}C_T.
\]

This would directly prove the collective transpose-tail estimate that energy boundedness alone cannot provide.

### 15.3 Strong-to-weak stability

The right product topology is stronger than plain \(L^2\). For example,

\[
\|\phi'(z)p-\phi'(\widetilde z)\widetilde p\|_2
\le
\|p-\widetilde p\|_2
+C\|\widetilde p\|_4
\|z-\widetilde z\|_4.
\]

This suggests a stability map of the form

\[
H_\gamma^s\cap L^4
\longrightarrow L^2,
\]

or a Gaussian-Orlicz analogue. The old derivative trees should be estimated by Gaussian product/Moser inequalities rather than summed coefficient by coefficient.

### 15.4 Ordered proof sequence

The most economical proof sequence is:

1. **Fixed-depth causal width limit.** Prove joint row/column conditioning, learned row history, and reciprocal Onsager responses at each fixed \(L\).
2. **Trained residual-depth homogenization.** Decompose every reused action into conditional mean plus centered innovation; prove the centered sum is \(O(L^{-1/2})\).
3. **Reachable response equations.** Derive \(R=D_\epsilon c\), or only the smaller query-restricted family \((\sigma_wI+R)H_q\).
4. **Weighted reachable regularity.** Propagate \(\mathcal E_s\) or prove direct compactness of the dynamically generated query family.
5. **Compactness and identification.** Use the weighted compact embedding, energy equicontinuity, Riesz consistency, and uniqueness or weak–strong uniqueness.
6. **Cutoff-uniform forced stability.** Use the chronological \(q/r\) propagator rather than a false global \(L^2\) Lipschitz constant.
7. **All-time upgrade.** Prove finite residual arclength, integrable residual, eventual coercivity, or a valid tail contraction.

### 15.5 Conditional Galerkin conclusion

Assume:

1. a well-posed infinite operator flow \(Y\);
2. compatible initial block projections \(\mathcal P_rY(0)\);
3. the weighted trajectory bound from Steps 3–4;
4. a cutoff-uniform forced gain \(G_T\);
5. an explicit nonlinear consistency estimate

\[
\|F_r(\mathcal P_rY)-\mathcal P_rF(Y)\|
\le
C_T(1+r)^{-\alpha}
\]

for some \(\alpha>0\).

The product estimates may yield an exponent \(\alpha\) smaller than \(s/2\). Under these assumptions, for every \(T\),

\[
\sup_{t\le T}
\|Y_r(t)-\mathcal P_rY(t)\|
\lesssim
G_TC_T(1+r)^{-\alpha},
\]

up to the compatible initial projection defect.

Locally Lipschitz output and Gram readouts then converge.

This would resolve internal pure-Hermite compact-time convergence to the infinite operator flow. It would not yet identify that flow with the dense ordered limit or prove all-time accuracy.

### 15.6 Branch criterion

The calculus should decide whether the pure state is sufficient.

- If the weighted estimate closes with \((b,a,\rho)\), continue with the pure-Hermite proof.
- If a specific response or two-time coefficient remains \(O(1)\) and is not determined by \((b,a,\rho)\), promote it to explicit finite \(\kappa\)-state.
- If the required response family grows without a summable tail, the broad finite-PDE conjecture is in danger.

This is a causal decision rule, not an aesthetic preference for one representation.

## 16. Alternative causal and mathematical foundations

### 16.1 Hybrid Hermite–response PDE

This is the strongest fallback and probably the best overall theorem target.

Retain:

- source Hermites through maximum degree \(r\), with mode count \(P_r\);
- the first \(K\) oriented \(q/r\) continuations;
- nonlinear trees through grade \(J\);
- only the historical \(\kappa_\alpha\) coordinates required by cyclic conditioning dependencies;
- a fixed depth approximation \(N\).

Hermites compress immutable disorder. Responses compress causal reuse. Historical \(\kappa\)'s Markovize the small part of training memory that survives homogenization.

The finite-matrix response experiments give strong evidence for rapid decay in \(K\). The key missing step is to emit a genuinely width-independent minimal response PDE and prove its full nonlinear outgoing residual, not merely the pure propagator tail.

This route is preferable to reviving the entire earlier prose compiler unchanged.

### 16.2 Prelimit-first causal Galerkin

Instead of first postulating a fully infinite PDE, work at finite \(n,L\):

1. derive the exact pathwise response truncation;
2. control its source-substitution error;
3. take \(n\to\infty\) at fixed response grade using joint Gaussian conditioning or tensor-program methods;
4. prove trained-depth homogenization;
5. remove the response, source, and depth cutoffs.

This preserves the correct order of limits and makes the Onsager term emerge from explicit conditioning rather than assumption.

It is technically heavier, but it is the most causally transparent route to identification with the dense model.

### 16.3 Exact DMFT/Volterra state plus finite memory realization

An exact causal DMFT naturally contains two-time covariance and response kernels. One can make it autonomous by adding an age coordinate or by retaining its memory state.

If the memory kernels admit architecture-derived finite approximations—such as a positive-real sum of exponentials—finite auxiliary variables can Markovize them.

This is mathematically honest, but it requires:

- the exact fixed-depth DMFT;
- a proof of kernel regularity or decay;
- a non-oracular rational approximation;
- stability of the resulting auxiliary-state system.

Without those estimates, finite-memory fitting is only another empirical surrogate.

### 16.4 Variational convergence of gradient flows

Every finite operator PDE has exact projected-gradient structure and a PSD tangent kernel. This invites an evolutionary \(\Gamma\)- or Mosco-convergence argument:

- equicoercivity in a weighted source space;
- convergence of energies and metric slopes;
- lower semicontinuity of dissipation;
- well-prepared initial data;
- convergence of curves of maximal slope.

This route may replace a cutoff-uniform local-Lipschitz theorem. It does not remove the compactness problem: the loss is noncoercive in many hidden directions, and the dynamics are not globally convex.

A modulated-energy or weak–strong uniqueness argument is more plausible than a simple contraction theorem.

### 16.5 Mori–Zwanzig organization

Projecting the exact causal DMFT onto the static operator state gives:

- a Markov drift;
- a memory kernel;
- an orthogonal residual.

The memory kernel is essentially the omitted response sector. If it has integrable decay or admits a controlled rational approximation, finite auxiliary states could produce a causal Markov closure.

At present, this is an organizing identity and a diagnostic for missing state. There is no kernel-decay theorem that makes it an independent solution.

### 16.6 Co-moving architecture-derived bases

The held-out POD result suggests that static Hermites may not be dimension-optimal, but trajectory-fitted POD violates the non-oracular requirement and the comparison was not equal active rank.

A legitimate alternative would have to be fixed by the architecture or recomputed autonomously from current PDE moments—for example, an affine Gaussian transport or a basis generated by a fixed source operator.

Such a moving basis introduces its own connection/commutator terms. It is worth considering only if the pure weighted-Hermite estimate fails for basis-efficiency rather than missing memory.

### 16.7 Padé, Borel, Koopman, and Carleman approaches

These are lower priority.

- Padé or Borel resummation of the training-time jet requires a summability or real-axis error theorem. The quadratic zero-radius result shows that matching all initial coefficients does not identify the positive-time trajectory.
- The proliferating message hierarchy argues strongly against a natural finite polynomial or Koopman invariant subspace.
- Generator Galerkin on a compact reachable class reduces in substance to the current Liouville program.
- Trajectory-trained EDMD, POD, or neural surrogates violate the architecture-local anti-oracle standard unless used only as exploratory diagnostics.

## 17. What would resolve or falsify the theory

### 17.1 Sufficient resolution of the pure-Hermite claim

A compact-time theorem would follow from:

1. an infinite operator flow;
2. a cutoff-uniform source-weighted bound with compact embedding;
3. consistency of the projected shared transpose;
4. uniqueness or weak–strong uniqueness;
5. cutoff-uniform forced stability.

An all-time theorem would additionally need a uniform tail mechanism.

### 17.2 Evidence that would seriously falsify pure Hermites

Any one of the following would be decisive:

- a uniform positive lower bound on adjacent observable Cauchy increments along a cofinal, numerically resolved odd-degree sequence;
- a dynamically reachable family with bounded energy but source tails escaping to arbitrarily high Hermite degree;
- two states identical in the entire proposed static operator state but with an \(O(1)\) future observable separation;
- a provable failure of uniqueness or unbounded cutoff forced gain in every plausible weighted topology;
- a nonvanishing full outgoing residual after all numerical resolution axes are controlled.

The current experiments show none of these.

### 17.3 Evidence that would force response enrichment

If a response/history coefficient:

- survives the ordered dense/depth limit at \(O(1)\);
- is not a function of \((b,a,\rho)\);
- has a summable chronological or kernel tail;

then pure Hermites are incomplete but the broad finite-PDE conjecture is strengthened: the missing state has been identified and can be added finitely.

### 17.4 Evidence that would threaten the broad conjecture

The broad conjecture would be in serious danger if:

- no finite response/history sector gives a vanishing residual;
- causal memory has a noncompact, nondecaying continuum essential to the observables;
- the ordered dense observable limit itself fails to exist;
- or all admissible finite systems incur a fixed positive observable error.

No current result establishes such an obstruction for the bounded residual model.

## 18. Strategic priorities

The next theoretical work should spend effort in the following order.

### Priority 1: response-weighted compactness estimate

Derive the equations for

\[
(\sigma_wI+R)H_q,
\qquad
T_W\beta_q,
\qquad
T_c\beta_q,
\]

and attempt a finite-\(s\) Gaussian Sobolev/Orlicz energy estimate. This goes directly at the make-or-break pure-Hermite gap.

### Priority 2: conditional/Onsager identification

At fixed depth, derive the joint row/column cavity law after training. In residual depth, prove that centered innovations vanish while the conditional mean converges to the shared-transpose term in the operator PDE.

### Priority 3: forced stability by response propagation

Use the \(q/r\) hierarchy and its ordered-depth factorial bound to establish a strong-to-weak perturbation estimate. Do not rely on plain \(L^2\) local Lipschitzness.

### Priority 4: minimal enrichment branch

If the weighted estimate exposes a surviving history variable, add only that variable or its query-restricted response family. Avoid rebuilding an unnecessarily large universal response compiler.

### Priority 5: all-time tail

After compact-time convergence, use:

- residual integrability;
- finite state arclength;
- eventual kernel coercivity;
- or a modulated contraction around the plateau.

The observed plateau makes this plausible, but it should not be attempted before the compact-time identification problem is settled.

## 19. Final assessment

The project has passed the point where the neural-PDE idea is merely speculative.

It now has:

- a literal finite PDE derived from the canonical architecture;
- exact finite-cutoff geometric and causal identities;
- direct prediction of \(O(1)\) nonlazy feature motion;
- broad transfer across tested data, labels, sample counts, and activations;
- a nonlinear stress in which fixed-gain linear controls fail badly while the PDE remains accurate on Gram and output dynamics;
- strong evidence that the old adverse Hermite conclusion was caused by a parity-invalid diagnostic;
- a precise localization of the remaining pure-Hermite problem to collective compactness and forced stability;
- an older causal response calculus capable of supplying the missing Onsager and propagation structure.

It does not yet have:

- a replicated aggregate Hermite Cauchy trend;
- a propagated source-weighted regularity theorem;
- a cutoff-uniform stability theorem;
- identification of the shared transpose with the ordered dense conditional mean;
- a rigorous ordered dense limit;
- or an all-time approximation theorem.

The most defensible final formulation is:

> There is strong theoretical and empirical evidence for a nontrivial, nonlinear, autonomous, portable low-order neural PDE for standard dense Euclidean \(\mu\)P feature learning. The explicit pure-Hermite hierarchy is a plausible but unproved arbitrary-accuracy witness. Its decisive compact-time gap is collective source-mode compactness together with uniqueness and cutoff-uniform forced stability. The recovered causal response/Onsager calculus provides the most credible route either to prove that gap or to identify the minimal response/history enrichment needed if pure Hermites are insufficient.

This is a meaningful causal theory program. It is not yet a completed theorem.

## 20. Supersession and source map

This report uses later findings whenever they replace an earlier conclusion.

### Foundational negative and stability reports

- `approximate_single_source_conjecture_resolution(1).md`
- `approximate_single_source_stability(1).md`
- `adversarial_audit_report(1).md`
- `mean_field_single_source_conjecture_audited_resolution(2).md`
- `normalized_mean_field_taylor_closure_audit(1).md`

Their surviving contribution is the fixed-order calculus, residual-clock stability, anti-oracle discipline, and model-specific no-go results. Their quadratic negative results are not generalized to bounded residual \(\tanh\).

### Causal response and conjecture reports

- `dense_euclidean_continuous_depth_npde_audit.md`
- `dense_euclidean_continuous_depth_pde_conjecture(1).md`

Their exact \(q/r\) identities, orientation rules, Onsager conditioning, and factorial depth-response bound survive. Their proposed full \(K/J/N\) compiler was not actually emitted as a complete executable finite PDE.

### Direct PDE and adversarial audit

- `REPORT.md`
- `final_adversarial_pde_audit(1).md`
- `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`

These establish the first literal operator–Hermite PDE and its finite-cutoff audits. Their early operator-order interpretation is superseded by the parity-correct analysis.

### Generalization and linearity

- `PDE_GENERALIZATION_FINAL_REPORT(3).md`
- `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`
- `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`

The scalar sine stress supersedes the original \(3.46\%\) gain-linear ambiguity for Gram dynamics. It does not establish a joint \(5\%\) loss result or improve the pure-Hermite convergence claim.

### Proof-obligation and Hermite-tail reports

- `PDE_PROOF_OBLIGATION_STUDY_FROZEN_REPORT.md`
- `PDE_LEAN_SALVAGE_REPORT.md`
- `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`
- `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`
- `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`

The parity report retracts the original \(5\to15\to35\) hierarchy warning. The common-reference and compactness reports supersede the claim that the lifted outgoing source is the actual trained tail. The Riesz-adjoint analysis supersedes a separate Malliavin-tail requirement for boundedness, while leaving collective source-mode compactness open.

### Specific superseded claims

1. **Superseded:** “The first Hermite refinements worsen strongly with \(P\).”  
   **Current:** the old denominator was an exactly inert even shell; corrected aggregate contraction remains unobserved.

2. **Superseded:** “The outgoing trained tail contracts \(17\)–\(34\times\).”  
   **Current:** the lifted newly opened source contracts; the actual trained aggregate tail does not yet contract.

3. **Superseded:** “Malliavin-gradient tail compactness is separately necessary to define the transpose.”  
   **Current:** the Riesz adjoint gives boundedness and fixed-compact-trajectory consistency; collective source-mode compactness is still necessary.

4. **Superseded:** “Flow amplification is not the problem.”  
   **Current:** one realized secant quotient did not increase; uniform stability remains open.

5. **Superseded:** “Low \(P\) may only capture an effectively linear activation.”  
   **Current:** low \(P\) captures a strongly nonlinear sine regime; \(P\) truncates source-label dependence, not activation nonlinearity.
