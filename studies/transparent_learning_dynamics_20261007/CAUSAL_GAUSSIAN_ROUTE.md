# Causal Gaussian route: exact conditioning and a proposed aggregate law

Status: independently derived and frozen for comparison on 2026-10-07. This is a research route, not an internally checked theorem of all-time approximation. No other route or verdict was consulted before this file was written.

## Scope and conclusion

Scientific inputs were the supervisor's self-contained model assignment only. I read the required research, rigorous-proof and canonical-notation skills, the neural-response-memory reference, and shared process instructions. I did not read the book, code, study history, other studies, literature or other agents' scientific results. I ran no experiment and made no Git operation. The precise established small-label class was not supplied; it is therefore a missing input for the eventual theorem, not a license to replace that class by a smaller one.

The concrete result is an exact conditional law for every adaptive forward or transpose query to an initial Gaussian weight matrix. Its conditional mean contains an explicit cross-direction correction. That correction leads to a genuinely aggregate, causal scalar recursion on a finite time mesh. A one-query convergence lemma and the first nonzero top-layer backward-query limit are proved below directly. They identify an actual bridge beyond a formal Gaussian ansatz. Identification of the full nonlinear gradient flow, quantitative width bounds, and uniform all-time approximation remain open.

The proposed continuous law retains two-time feature and backward kernels and two response measures per internal interface. Its primitive randomness consists of scalar Gaussian processes, with no neuron-indexed dense matrices. This is a distributional reduction with growing history, not yet a finite autonomous all-time surrogate.

## Model and exact history equations

There are $p\geq m$ evaluated inputs $v_a=x_a/\sqrt d\in\mathbb R^d$, with $\|v_a\|=1$; only $a\leq m$ are training inputs. Define their fixed Gram matrix by $S_{ab}=v_a^\top v_b$. All hidden layers have width $n$, and the fixed depth is $L\geq1$. The assigned forward map is

\[
z_{1,a}=Av_a,\qquad h_{\ell,a}=\phi_\ell(z_{\ell,a}),\qquad
z_{\ell,a}=W_\ell h_{\ell-1,a}\quad(2\leq\ell\leq L),
\qquad f_a=\frac1n w^\top h_{L,a}.
\]

Activations act coordinatewise, are analytic in the assigned complex strip, and have bounded derivative there; their values may grow. The training residual and squared loss are

\[
c_a=y_a-f_a,\qquad \mathcal L=\frac1m\sum_{a=1}^m c_a^2.
\]

Write $\kappa=2/m$. The backward signals, also defined for passive evaluated inputs, are

\[
\delta_{L,a}=w\odot\phi'_L(z_{L,a}),\qquad
\delta_{\ell,a}=\phi'_\ell(z_{\ell,a})\odot W_{\ell+1}^\top\delta_{\ell+1,a}.
\]

The physical gradient flow is

\[
\dot A=\kappa\sum_{b=1}^m c_b\delta_{1,b}v_b^\top,
\quad \dot W_\ell=\frac\kappa n\sum_{b=1}^m c_b\delta_{\ell,b}h_{\ell-1,b}^\top,
\quad \dot w=\kappa\sum_{b=1}^m c_bh_{L,b}.
\]

Initially, $A(0)$ has independent $N(0,1)$ entries, the matrices $G_\ell=W_\ell(0)$ have independent $N(0,1/n)$ entries, all these matrices are independent, and $w(0)=0$.

Define finite-width, two-time empirical kernels

\[
C^{(n)}_{\ell;ab}(s,t)=\frac1n h_{\ell,a}(s)^\top h_{\ell,b}(t),\qquad
D^{(n)}_{\ell;ab}(s,t)=\frac1n\delta_{\ell,a}(s)^\top\delta_{\ell,b}(t).
\]

Integrating the parameter equations and multiplying by current vectors gives the following exact identities on every interval on which the flow exists:

\[
\begin{aligned}
z_{1,a}(t)
 &=A(0)v_a+\kappa\sum_{b=1}^m\int_0^t c_b(s)S_{ba}\delta_{1,b}(s)\,ds,\\
z_{\ell,a}(t)
 &=G_\ell h_{\ell-1,a}(t)
   +\kappa\sum_{b=1}^m\int_0^t c_b(s)
     C^{(n)}_{\ell-1;ba}(s,t)\delta_{\ell,b}(s)\,ds,\\
W_\ell(t)^\top\delta_{\ell,a}(t)
 &=G_\ell^\top\delta_{\ell,a}(t)
   +\kappa\sum_{b=1}^m\int_0^t c_b(s)
     D^{(n)}_{\ell;ba}(s,t)h_{\ell-1,b}(s)\,ds,\\
w(t)&=\kappa\sum_{b=1}^m\int_0^t c_b(s)h_{L,b}(s)\,ds,\\
f_a(t)&=\kappa\sum_{b=1}^m\int_0^t c_b(s)C^{(n)}_{L;ba}(s,t)\,ds.
\end{aligned}
\]

The first approximation has not occurred. In particular, the actions $G_\ell h(t)$ and $G_\ell^\top\delta(t)$ remain adapted actions of the same Gaussian matrix.

Differentiating the output, using the assigned mobilities, also gives

\[
\dot f_a=\kappa\sum_{b=1}^m K^{(n)}_{ab}c_b,
\quad
K^{(n)}_{ab}=C^{(n)}_{L;ab}(t,t)+S_{ab}D^{(n)}_{1;ab}(t,t)
 +\sum_{\ell=2}^L C^{(n)}_{\ell-1;ab}(t,t)D^{(n)}_{\ell;ab}(t,t).
\]

For example, the $W_\ell$ contribution is
\(\kappa\sum_b c_b(\delta_{\ell,a}^\top\delta_{\ell,b}/n)
(h_{\ell-1,a}^\top h_{\ell-1,b}/n)\).
Each summand is a Gram matrix or a Gram matrix Hadamard product, so the training restriction of $K^{(n)}$ is positive semidefinite. This exact residual identity is not itself a closed aggregate model.

## Exact two-sided conditioning of an adaptive Gaussian matrix

This lemma applies separately to each $G_\ell$. Suppress its layer index. Suppose the transcript has revealed forward products $GH=Y$ and backward products $G^\top D=X$, where

\[
H,Y\in\mathbb R^{n\times r},\qquad D,X\in\mathbb R^{n\times s}.
\]

The columns of $H,X$ live in the input population and those of $Y,D$ in the output population. Queries are chosen using earlier transcript entries and auxiliary randomness independent of unrevealed Gaussian matrices. A global transcript may interleave queries to different matrices.

Let $H^+=(H^\top H)^\dagger H^\top$, with $\dagger$ denoting the Moore–Penrose inverse, and define orthogonal projections $P_H=HH^+$ and $P_D=D(D^\top D)^\dagger D^\top$. Conditional on the transcript,

\[
G\ \stackrel{\mathrm{law}}=\ M+(I-P_D)\widetilde G(I-P_H),
\qquad
M=YH^++D(D^\top D)^\dagger X^\top(I-P_H),
\tag{1}
\]

where $\widetilde G$ is an independent matrix with independent $N(0,1/n)$ entries. Formula (1) is valid with dependent or empty histories as well.

To prove it first fix a consistent transcript. The homogeneous constraint space is exactly

\[
\{B:BH=0,\ B^\top D=0\}
=\{(I-P_D)B(I-P_H):B\in\mathbb R^{n\times n}\}.
\]

The displayed $M$ satisfies both constraints: compatibility gives $D^\top Y=X^\top H$, so $MH=Y$ and $D^\top M=X^\top$. Its first summand has row space in the span of $H$, and its second has column space in the span of $D$; both are orthogonal, in Frobenius inner product, to the homogeneous space. An isotropic Gaussian vector conditioned on affine linear constraints is its minimum-norm feasible mean plus the orthogonal projection of independent isotropic Gaussian noise. This last fact follows by choosing an orthonormal basis of the constraint space and its orthogonal complement: Gaussian coordinates in the two subspaces are independent. It proves (1).

Adaptivity does not change the formula. At each stage the next query vector is a fixed measurable function of the past transcript and independent auxiliary randomness. Conditional on that past, revealing its output is one further linear observation of the current Gaussian remainder. Induction gives (1); it also preserves the product of conditional Gaussian remainders for independently initialized matrices. The query-generation mechanism itself must not inspect unobserved matrix entries.

For a new forward input $h\in\mathbb R^n$, define

\[
a=(H^\top H)^\dagger H^\top h,\qquad h_\perp=h-Ha.
\]

Then

\[
Gh=Ya+D(D^\top D)^\dagger X^\top h_\perp
  +\frac{\|h_\perp\|}{\sqrt n}(I-P_D)\xi,
\qquad \xi\sim N(0,I_n),
\tag{2}
\]

conditionally on the transcript. For a new backward input $d\in\mathbb R^n$, define

\[
b=(D^\top D)^\dagger D^\top d,\qquad d_\perp=d-Db.
\]

The transpose version is

\[
G^\top d=Xb+H(H^\top H)^\dagger Y^\top d_\perp
  +\frac{\|d_\perp\|}{\sqrt n}(I-P_H)\xi'.
\tag{3}
\]

Here $\xi'$ is a fresh standard Gaussian vector conditional on the prior transcript. The second deterministic term in each equation is the cross-direction, or Onsager, correction. It is generally order one. Removing the projection from the fresh noise is asymptotically harmless for finitely many retained queries, but removing this mean term is not.

## A proved one-query aggregate limit

Here is a precise modest limit statement that requires no general neural-network limit theorem. Take finitely many past columns. Assume that the joint input-population arrays $(H,X,h)$ and output-population arrays $(Y,D,V)$, for any finitely many additional existing output variables $V$, have empirical laws converging in probability against bounded Lipschitz tests. Assume all empirical second moments and cross moments used below converge to those of deterministic limiting laws. After removing exact dependent columns, assume the limiting Gram matrices of $H$ and $D$ are positive definite. Empty histories are allowed.

Use the same capital letters for their scalar-population limits, now finite random vectors. Set

\[
\begin{aligned}
\Gamma_H&=\mathbb E[HH^\top],&
a&=\Gamma_H^{-1}\mathbb E[Hh],& h_\perp&=h-H^\top a,\\
\Gamma_D&=\mathbb E[DD^\top],&
q&=\Gamma_D^{-1}\mathbb E[Xh_\perp],&
\sigma^2&=\mathbb E[h_\perp^2].
\end{aligned}
\]

Then the new output-population empirical law converges, against bounded Lipschitz tests, to the joint law of

\[
\bigl(Y,D,V,\ Y^\top a+D^\top q+\sigma Z\bigr),
\qquad Z\sim N(0,1)\text{ independent of }(Y,D,V).
\tag{4}
\]

All expectations of input-population variables are evaluated in the input law, and expectations of output-population variables in the output law. There is no pairing of arbitrarily matched neurons across populations.

Proof: empirical moment convergence and continuity of matrix inversion give convergence of the two coefficient vectors and $\sigma_n$. Their changes contribute vanishing normalized squared norm because the empirical squared norms of $Y,D$ are bounded in probability. Conditional on the transcript,

\[
\mathbb E\left[\frac1n\|P_D\xi\|^2\mid\text{transcript}\right]
=\frac{\operatorname{rank}D}{n}\longrightarrow0.
\]

Thus (2) differs in normalized Euclidean norm by $o_{\mathbb P}(1)$ from the coordinatewise expression in (4) with independent $Z_i$. A bounded Lipschitz empirical test changes by $o_{\mathbb P}(1)$, by Cauchy–Schwarz. Conditional on the existing array, its independent-Gaussian empirical average has variance at most $4\|\psi\|_\infty^2/n$. Its conditional mean is the existing empirical average of the bounded Lipschitz function obtained by integrating $Z$. The assumed empirical convergence identifies that limit. This proves (4).

The transpose statement follows from (3):

\[
\begin{aligned}
b&=\Gamma_D^{-1}\mathbb E[Dd],& d_\perp&=d-D^\top b,\\
r&=\Gamma_H^{-1}\mathbb E[Yd_\perp],&\tau^2&=\mathbb E[d_\perp^2],\\
x_{\mathrm{new}}&=X^\top b+H^\top r+\tau Z'.
\end{aligned}
\tag{5}
\]

The proof permits $\sigma=0$ or $\tau=0$; it never divides by an innovation variance. This is a one-query propagation result conditional on actual joint empirical and moment limits. It is not a proof that those hypotheses hold through the whole neural program. In particular, bounded-Lipschitz convergence alone does not propagate the unbounded products required by later queries.

## A nonzero correction proved at the first backward sweep

Consider any top matrix $G_L$ with $L\geq2$. Let $H\in\mathbb R^{n\times p}$ collect the initial lower-layer features, independent of $G_L$, and set $Q_n=H^\top H/n$. Assume its empirical row law converges to a deterministic law with second moments and $Q_n\to Q>0$ in probability. This full-rank assumption is local to the following lemma, not a new assumption on the requested final approximation theorem.

Take one Euler step of length $\eta>0$. Since $w^0=0$, all hidden parameter updates at that step vanish, and

\[
w^1=\kappa\eta\sum_{b=1}^m y_b\phi_L(G_LH_b).
\]

For sample $a$, the next top backward input is $d_i=T_a(Z_i)$, where $Z=G_LH$ and

\[
T_a(z)=\kappa\eta\left(\sum_{b=1}^m y_b\phi_L(z_b)\right)\phi'_L(z_a).
\]

Conditional on $H$, the $Z_i$ are independent $N(0,Q_n)$. On the event $Q_n>0$, whose probability tends to one, equation (3), with no previous backward query, gives exactly

\[
G_L^\top d
=H Q_n^{-1}\frac{Z^\top d}{n}
 +\frac{\|d\|}{\sqrt n}(I-P_H)\xi.
\tag{6}
\]

Conditional laws of large numbers give

\[
\frac{Z^\top d}{n}\longrightarrow\mathbb E[ZT_a(Z)],\qquad
\frac{\|d\|^2}{n}\longrightarrow\mathbb E[T_a(Z)^2],\qquad Z\sim N(0,Q).
\]

These laws of large numbers need only Gaussian moments: bounded $\phi'_L$ implies at most linear growth of $T_a$, and bounded $Q_n$ bounds the requisite fourth moments. Since $Q_n$ converges in probability, the argument applies on events with bounded $Q_n$ whose probabilities tend to one as the bound increases. Continuity of the Gaussian expectations follows by writing $Z=Q_n^{1/2}U$ with $U$ standard normal and applying dominated convergence.

Gaussian integration by parts gives $\mathbb E[ZT_a(Z)]=Q\mathbb E[\nabla T_a(Z)]$. To verify it directly, differentiate the density $\rho_Q$, use $z\rho_Q=-Q\nabla\rho_Q$, and integrate each coordinate; Gaussian decay removes the boundary terms. The strip assumption bounds $\phi''_L$ on the real line by Cauchy's formula on an interior circle, so the derivatives have integrable growth.

It follows from (6) and the preceding one-query proof that the limiting backward field in the lower population is

\[
X_a=\sum_{b=1}^p H_b\,\mathbb E[\partial_bT_a(Z)]
  +\sqrt{\mathbb E[T_a(Z)^2]}\,\xi,
\tag{7}
\]

where $\xi\sim N(0,1)$ is independent of the limiting lower feature row $H$, and $Z\sim N(0,Q)$ is used only to compute the coefficients. Extend $y_b=0$ for $b>m$. Then

\[
\mathbb E[\partial_bT_a(Z)]
=\kappa\eta\left[
y_b\,\mathbb E[\phi'_L(Z_b)\phi'_L(Z_a)]
 +\mathbf1_{b=a}\,\mathbb E\left[
 \left(\sum_{c=1}^m y_c\phi_L(Z_c)\right)\phi''_L(Z_a)
 \right]\right].
\tag{8}
\]

Even a linear activation retains the first term. For one sample with $\phi(z)=z$, (7) becomes

\[
G_L^\top G_LH\ \leadsto\ H+\sqrt{\mathbb E[H^2]}\,\xi
\]

after cancelling the nonzero scalar $\kappa\eta y$. This is consistent with the nontrivial action of $G_L^\top G_L$; an independent-Gaussian backward ansatz would incorrectly remove the $H$ term. No cancellation is used when $y=0$: the original backward field is exactly zero.

This establishes one actual feature-learning query at arbitrary fixed depth, under the stated lower-feature convergence assumption. It does not establish the complete first backward sweep through all layers or a positive-time flow theorem.

## Proposed aggregate construction on a finite time mesh

Fix a time step $\eta$ and a finite number of steps $N$. Euler updates admit exactly the history formulas above with integrals replaced by left sums. At step $k$, compute the forward pass in increasing layer order, the output and residuals, then the backward pass in decreasing layer order. Append each requested $G_\ell h_{\ell-1,a}^k$ or $G_\ell^\top\delta_{\ell,a}^k$ to that matrix's transcript. Queries can be made in a fixed sample order. Redundant queries are retained or removed using their exact linear relations.

The proposed limiting construction makes the following replacement, which is the first approximation in this construction:

1. Each layer is represented by the joint law of one scalar neuron's finite history.
2. Every empirical inner product is replaced by the corresponding expectation in that law.
3. Every new Gaussian action is generated by (4) or (5), using a fresh independent scalar normal for that layer-population query.

For example,

\[
z_{\ell,a}^k=g_{\ell,a}^k
 +\kappa\eta\sum_{s<k}\sum_{b=1}^m
c_b^s C_{\ell-1;ba}(s,k)\delta_{\ell,b}^s,
\]

where $g_{\ell,a}^k$ is generated by (4), and

\[
r_{\ell-1,a}^k=x_{\ell-1,a}^k
 +\kappa\eta\sum_{s<k}\sum_{b=1}^m
c_b^s D_{\ell;ba}(s,k)h_{\ell-1,b}^s,
\quad \delta_{\ell-1,a}^k=\phi'_{\ell-1}(z_{\ell-1,a}^k)r_{\ell-1,a}^k,
\]

where $x_{\ell-1,a}^k$ is generated by (5). Also

\[
w^k=\kappa\eta\sum_{s<k,b\leq m}c_b^s h_{L,b}^s,
\qquad f_a^k=\mathbb E[w^k h_{L,a}^k],\qquad c_a^k=y_a-f_a^k.
\]

The initial first-layer scalar Gaussian vector has covariance $S$. Its exact first-layer history update is the scalar version of the first identity above. This specifies the coefficient provenance: expectations are computed from the previously constructed scalar laws and supplied input Gram matrix, labels and activations. They are not supplied from a dense trajectory.

This law is aggregate in a substantive sense. At fixed $N,p,L$, the number of Gaussian scalar innovations and history coordinates is independent of $n$. The number of moment coefficients is at most order $L(pN)^2$, while each layer's Gaussian integral dimension is at most order $pN$. The law can be defined by finite-dimensional Gaussian integrals; approximating those integrals is a separate numerical task. It retains no dense initialization and no neuron-indexed learned parameter array. Computational complexity in the time history can nevertheless be large. A finite Gaussian-integral description is not by itself an efficient finite-coordinate differential equation.

The exact conditioning proof and the one-query lemma justify every individual replacement if the required preceding joint moment limits and stable-rank hypotheses hold. They do not yet justify all replacements together for the assigned unbounded analytic activation class.

## Proposed response-kernel form before discretization

The mesh construction suggests a continuous scalar law with one local process per layer. Define its two-time moments by

\[
C_{\ell;ab}(s,t)=\mathbb E[h_{\ell,a}(s)h_{\ell,b}(t)],\qquad
D_{\ell;ab}(s,t)=\mathbb E[\delta_{\ell,a}(s)\delta_{\ell,b}(t)].
\]

For $1\leq\ell<L$, write $r_{\ell,a}$ for the scalar backward field before multiplying by $\phi'_\ell(z_{\ell,a})$. Set $r_{L,a}=w$, so $\delta_{\ell,a}=\phi'_\ell(z_{\ell,a})r_{\ell,a}$ at every layer. The same $w$ is used for all samples in the top local process.

Response kernels need actual definitions. Add deterministic probe functions $\epsilon_b(s)$ to the right-hand side of the local equation for $r_{\ell,b}(s)$, holding all deterministic population kernels and residuals fixed. If the first variation exists as a bounded linear functional on continuous probe paths, define its expected representing measure by

\[
\left.\frac{d}{du}\mathbb E[h_{\ell,a}^{\,u\epsilon}(t)]\right|_{u=0}
=\sum_{b=1}^p\int_{[0,t]}\epsilon_b(s)R^h_{\ell;ab}(t,ds).
\tag{9}
\]

Likewise, add a probe to the local equation for $z_{\ell,b}(s)$, holding the population coefficients fixed, and define

\[
\left.\frac{d}{du}\mathbb E[\delta_{\ell,a}^{\,u\epsilon}(t)]\right|_{u=0}
=\sum_{b=1}^p\int_{[0,t]}\epsilon_b(s)R^\delta_{\ell;ab}(t,ds).
\tag{10}
\]

These definitions include any atom at $s=t$. They are responses of a single local process; differentiating the population kernels or residuals would describe a different perturbation. Existence of these derivatives and interchange with expectation are requirements, not proved facts here.

Introduce centered Gaussian processes $\eta_{\ell,a}$ for $2\leq\ell\leq L$ and $\xi_{\ell,a}$ for $1\leq\ell<L$, with proposed covariances

\[
\mathbb E[\eta_{\ell,a}(s)\eta_{\ell,b}(t)]=C_{\ell-1;ab}(s,t),\qquad
\mathbb E[\xi_{\ell,a}(s)\xi_{\ell,b}(t)]=D_{\ell+1;ab}(s,t).
\]

Different primitive Gaussian families are independent. Let $\zeta\sim N(0,S)$ initialize the first layer. The candidate local equations are

\[
\begin{aligned}
z_{1,a}(t)
 &=\zeta_a+\kappa\sum_{b=1}^m\int_0^t c_b(s)S_{ba}\delta_{1,b}(s)\,ds,\\
z_{\ell,a}(t)
 &=\eta_{\ell,a}(t)
 +\sum_{b=1}^p\int_{[0,t]}\delta_{\ell,b}(s)R^h_{\ell-1;ab}(t,ds)\\
 &\hspace{1em}+\kappa\sum_{b=1}^m\int_0^t c_b(s)
 C_{\ell-1;ba}(s,t)\delta_{\ell,b}(s)\,ds,\qquad 2\leq\ell\leq L,\\
r_{\ell,a}(t)
 &=\xi_{\ell,a}(t)
 +\sum_{b=1}^p\int_{[0,t]}h_{\ell,b}(s)R^\delta_{\ell+1;ab}(t,ds)\\
 &\hspace{1em}+\kappa\sum_{b=1}^m\int_0^t c_b(s)
 D_{\ell+1;ba}(s,t)h_{\ell,b}(s)\,ds,\qquad 1\leq\ell<L,\\
w(t)&=\kappa\sum_{b=1}^m\int_0^t c_b(s)h_{L,b}(s)\,ds,\\
h_{\ell,a}(t)&=\phi_\ell(z_{\ell,a}(t)),\qquad
\delta_{\ell,a}(t)=\phi'_\ell(z_{\ell,a}(t))r_{\ell,a}(t),\\
f_a(t)&=\mathbb E[w(t)h_{L,a}(t)],\qquad c_a(t)=y_a-f_a(t).
\end{aligned}
\tag{11}
\]

Only the explicit training sums run over $b\leq m$. Passive inputs contribute no training drift. Probes are allowed at all evaluated samples so that passive observables have their correct response law.

The response terms in (11) have positive signs for the assigned convention $c=y-f$ and matrix decomposition. Their signs are not determined by informal analogies with other Onsager formulas. Their finite-query origin is precisely the second terms of (2) and (3). Equations (9)–(11) require a limiting integration-by-parts/cavity identification to turn regression coefficients into response measures; that identification is proposed, not proved.

The forward response $R^h_{\ell}$ should have no atom at $t$: a backward-field perturbation first changes a training velocity and then a future feature. The backward response $R^\delta_{\ell}$ generally does have an atom because the backward signal depends on the current forward field. At the top layer its direct instantaneous part is

\[
R^\delta_{L;ab}(t,\{t\})
=\mathbf1_{a=b}\,\mathbb E[w(t)\phi''_L(z_{L,a}(t))],
\]

when the stated probe convention and continuity hold. Its history part includes the response of the integral defining $w$. On the first Euler sweep, those two contributions are exactly the two terms in (8). Dropping either is already contradicted by that proved finite-step calculation when that term is nonzero. For lower layers, the atom also contains the derivative of their local backward field through the instantaneous upper-layer response term.

There is no assertion here that (11) is already a well-posed Volterra equation. Causality, measure-valued responses, endpoint conventions and the deterministic self-consistency equations must be established. The finite query construction gives an unambiguous discrete reference against which a continuum derivation can be checked.

## Remaining bridges and hostile checks

| Claim | Current status | Missing implication |
|---|---|---|
| Rank-one history formulas and output tangent identity | Exact; proof above | None within finite-width existence interval |
| Adaptive two-sided Gaussian posterior | Exact; proof above | None for predictable linear-query transcripts |
| One-query empirical-law propagation | Proved under stated moment and stable-rank hypotheses | Verify hypotheses through the neural program |
| First nonzero top transpose action | Proved under its stated lower-feature limit and positive Gram hypotheses | Propagate down and through later times |
| Finite-mesh scalar construction | Explicit aggregate candidate | Joint moment propagation, dependent histories, and quantitative errors |
| Response-measure equations (11) | Formal candidate with finite-step checks | Cavity/response identification, existence, uniqueness, continuum limit |
| Compact-time gradient-flow limit | Open | Uniform mesh error and limiting-law stability |
| Quantitative finite-width all-time approximation | Open | Width rates, residual tail control, all-time stability and finite approximation complexity |

The sharp target for the width bridge is convergence in probability, on each fixed $T$, of every evaluated output and every finite collection of two-time feature/backward kernels, uniformly over their times in $[0,T]$, to a unique law generated from $S,y,\phi_\ell$ by the candidate construction. The intended final target further asks for quantitative finite-width approximation uniformly for $t\geq0$ on the already admitted small-label class. That class was not provided to this scoped route; its hypotheses cannot be checked here. Fixed depth and finite sample/validation count may enter the constants. Constants and representation complexity must not depend on neuron count through hidden dense state, or on the unknown dense trajectory.

The important surviving obstructions are concrete:

* **Nearly dependent histories.** At initialization all backward signals vanish; repeated early queries and vanishing labels create singular history Grams. Positive initial feature Gram does not imply positive Gram for every later history stack. Pseudoinverses make the exact identities valid, but do not give continuous or uniformly bounded coefficients. One possible repair is to discard directions whose limiting innovation variance vanishes and bound their entire matrix action by the Gaussian operator norm times their input error. That still requires a proof that all subsequent nonlinear products remain controlled. It is not supplied here. Requiring generic labels or an extra lower bound on every history Gram would narrow the task and is not an acceptable final fix.

* **Unbounded local products.** Bounded activation derivatives do not make products such as $w\phi'(z)$ globally Lipschitz jointly in $(w,z)$. Fixed-mesh propagation therefore needs sufficient moment bounds and a justified localization argument. Weak empirical convergence from the one-query lemma alone cannot be iterated through all required products.

* **No hidden dense oracle.** The exact posterior alone is a finite-width parameter reconstruction and would not meet the aggregate goal. The proposed law (4)–(5) replaces its empirical coefficients by deterministic scalar-law expectations and removes all dense matrices. Only this further step is the reduction. Its identification with the network remains an obligation.

* **Growing memory.** Finite-mesh storage grows with $N$. Continuous Gaussian paths and response measures are not finitely many real coordinates. A separate causal finite-dimensional approximation theorem, including coefficient provenance and restartability, is needed if the final target requires a finite autonomous system.

* **Limit order.** The current bridge concerns $n\to\infty$ at a fixed number of queries. Sending $N\to\infty$, the step size to zero, and then $T\to\infty$ requires separate estimates. The exact flow identities do not permit interchanging those limits.

* **Long-time control.** Positive initial limiting feature Gram provides initial coercivity only. To convert compact-time convergence to an all-time result one needs estimates, within the original small-label class, that keep an appropriate training kernel coercive or otherwise control the residual tail and sensitivity of the response law. A finite path-length estimate by itself would not bound Gaussian regression conditioning or nonlinear response amplification.

* **A falsifier that is already resolved for the naive witness.** Independent Gaussian forward/backward actions with no correction fail (7)–(8), even with a linear activation. This rules out that witness, not the Gaussian-response route or the broad approximation objective.

The highest-leverage next theorem is a rank-robust, fixed-mesh joint moment limit for the actual neural program, built from (1)–(5), covering zero labels and the exact analytic activation class. It is smaller than the all-time problem, uses a precise finite causal algorithm, and would establish the missing identification step before attempting continuum response measures or all-time compression.
