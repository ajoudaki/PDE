# Deferred Gaussian queries with controlled omissions

Date: 2026-10-02. Claim status: self-contained exact finite-dimensional derivations and a conditional tracking proposition; no empirical validation, independent review, or promotion. This is a finite-width simulator construction, not an autonomous population law.

The useful foothold is to **retain every revealed constraint and omit only sufficiently small unexplored query components**. Legendre compression of learned increments does not itself justify compression of Gaussian conditioning. The two approximations have different errors.

## 1. Exact causal oracle

Consider one initialized hidden matrix $W\in\mathbb R^{n\times n}$, with independent $N(0,1/n)$ entries, independent of initial roots. Its matrix calls may alternate between forward and transpose directions. Queries and reveal/skip decisions must depend only on roots, independent auxiliary randomness, and previous revealed answers or deterministic functions thereof.

Store orthonormal right and left bases $U\in\mathbb R^{n\times r}$, $V\in\mathbb R^{n\times s}$, and their exact images

\[
Y=WU,\qquad Z=W^\top V.
\]

Empty bases are allowed. Write $P_U=UU^\top$, $P_V=VV^\top$. Consistency requires $V^\top Y=Z^\top U$. Let \(\mathcal H\) include roots, independent randomness already used for query selection, all query vectors and all revealed answers; the current query is measurable from it. Given this transcript,

\[
W\mid\mathcal H\overset d=
M+(I-P_V)\widetilde W(I-P_U),\qquad
M=YU^\top+VZ^\top(I-P_U),                 \tag{1}
\]

where \(\widetilde W\) is an independent matrix with the original entry law.

**Derivation.** In orthonormal coordinates extending $U,V$, the constraints specify every block except the block mapping $U^\perp$ to $V^\perp$. That block remains an independent isotropic Gaussian. The displayed $M$ solves both constraints and has zero unspecified block: $MU=Y$, while consistency gives $M^\top V=U Y^\top V+(I-P_U)Z=Z$. This proves (1) for fixed constraints. For adaptive queries, condition first on the existing transcript: the next direction is then fixed, and revealing its answer imposes only the next linear constraint. Induction proves the same formula. Other independent initialized matrices can be interleaved by the same argument.

For a forward query $h\in\mathbb R^n$, let $e=(I-P_U)h$. If $e=0$, return $Mh=Y U^\top h$. Otherwise an exact new reveal is:

\[
u=e/\|e\|_2,\qquad
y=VZ^\top u+(I-P_V)g/\sqrt n,\quad g\sim N(0,I_n),
\]

then append $u,y$ to $U,Y$, leaving $V,Z$ unchanged. Return $Y_{\rm old}U_{\rm old}^\top h+\|e\|_2y$. The new column has the conditional law of $Wu$, and $V^\top y=Z^\top u$ preserves consistency.

For a reverse query $b\in\mathbb R^n$, let $e=(I-P_V)b$. If $e=0$, return $M^\top b=ZV^\top b$. Otherwise set

\[
v=e/\|e\|_2,\qquad
z=UY^\top v+(I-P_U)g/\sqrt n,
\]

append $v,z$ to $V,Z$, and return $Z_{\rm old}V_{\rm old}^\top b+\|e\|_2z$. Again the mixed constraints are preserved. Zero residuals require neither division nor sampling; saturated subspaces leave no unexplored block.

At any finite stopping point, complete $W$ using (1). Induction and conditional integration show that this completion has the original Gaussian law and reproduces every revealed answer. Thus the sampler can be coupled to **one fixed quenched matrix**, not fresh matrices at successive times. With skips, this is equivalence to the same approximate algorithm run against a fixed Gaussian matrix; it is not equivalence to exact training.

This mechanism is existing prior: Lu's **Householder Dice**, Algorithm 1 and Theorem 1, samples adaptive forward/transpose Gaussian calls without constructing the matrix, with $O(nN)$ storage and $O(nN^2)$ work for $N$ calls. Its Gaussian construction and proof were inspected completely; the orthonormal-coordinate proof above also handles repeated or dependent queries without adding a direction. Any prospective advance here is selective revelation combined with paired response memory. [Lu, arXiv v2, §3.2](https://arxiv.org/html/2101.07464v2#S3.SS2).

## 2. Exact omission bounds and the conditioning trap

Fix an RMS tolerance \(\varepsilon>0\). If \(\|(I-P_U)h\|_2/\sqrt n\le\varepsilon\), a skipped forward call returns $Mh$ without revealing anything. Formula (1) gives

\[
\mathbb E\left[\frac{\|Wh-Mh\|_2^2}{n}\mid\mathcal H\right]
=\left(1-\frac{s}{n}\right)\frac{\|(I-P_U)h\|_2^2}{n}
\le\varepsilon^2.                                      \tag{2}
\]

The reverse formula exchanges $U,r$ with $V,s$. For $e\ne0$, the random normalized squared error $\|Wh-Mh\|_2^2/n$, divided by \(\|e\|_2^2/n^2\), has conditional law \(\chi^2_{n-s}\). These innovations are correlated across calls through the same unrevealed matrix. Conditional second moments do not justify independent error accumulation or a uniform-in-time bound without additional reasoning.

A stronger simultaneous bound avoids that issue. For the coupled fixed completion,

\[
W-M=(I-P_V)W(I-P_U).                                    \tag{3}
\]

Consequently, on \(\|W\|_{\rm op}\le K\), every skipped call, adaptively chosen or otherwise, satisfies

\[
\frac{\|(W-M)h\|_2}{\sqrt n}\le K\varepsilon,\qquad
\frac{\|(W^\top-M^\top)b\|_2}{\sqrt n}\le K\varepsilon.    \tag{4}
\]

This is pathwise for all transcripts; no union over call times is needed. The bound applies to approximate-path queries, not unobserved exact-path queries. For example, the manuscript's elementary net estimate gives
\(\Pr\{\|W\|_{\rm op}>K\}\le2\exp\{n\log81-nK^2/8\}\); a fixed sufficiently large $K$ therefore works with probability tending to one. For fixed depth, union only over initialized matrices.

Skips reveal no unknown quantity and so preserve (1). **Forgetting previously revealed constraints is different.** Their outputs may already have entered nonlinear current states. Conditioning on that state is generally not equivalent to conditioning only on retained linear combinations. Replacing a transcript by its first $q$ Legendre moments and resetting the discarded block to an independent Gaussian therefore has no justification from (1).

At a fixed transcript $M$ and $M^\top$ are exact adjoints. If enrichment occurs between a forward and backward pass, they correspond to different transcripts. Either replay after enrichment until a complete pass adds no directions, or explicitly analyze the routine as an inexact evaluation of the fixed-$W$ vector field. The latter is sufficient below, but is not necessarily an exact gradient of one reconstructed mean matrix. A replay loop has at most $2n$ additions per matrix in exact arithmetic; its practical cost remains a concern.

The paper's learned increment omits a product of forward and backward projection tails. Equations (2)–(4) instead contain a **single query tail**. The paper's near-quadratic order rate cannot be assigned to this new approximation.

## 3. A bounded-rank condition

For one actual forward query sequence $h_0,h_1,\ldots$, define its normalized variation through the computation by

\[
A_h=\sum_j\|h_{j+1}-h_j\|_2/\sqrt n.
\]

Append only if its normalized distance $\|(I-P_U)h_j\|_2/\sqrt n$ exceeds \(\varepsilon\), and never remove a direction. Once a query has triggered an append, that entire query lies in the new span. At the next append triggered by this sequence, its normalized distance from the preceding selected query must therefore exceed \(\varepsilon\). Summing variation over these disjoint intervals proves

\[
N_h\le1+A_h/\varepsilon.                                \tag{5}
\]

For several interleaved sample sequences, assign each append to its triggering sequence; additions from other sequences only enlarge the span. Hence $r\le\sum_a(1+A_{h_a}/\varepsilon)$, capped by $n$. Apply the identical argument to reverse sequences for $s$. Continuous bounded-variation paths use their total variation instead of the displayed sum.

The bound is independent of integration-step count and width **if the actual query variation is**. It includes jumps and replay evaluations induced by enrichment. Variation measured only on dense training is not a certificate for the approximate algorithm. Initial vectors of arbitrarily large norm cost at most one initial direction per sequence.

There is a narrower consequence of the manuscript's Theorem thm:alltime. Fix $L\ge2$ hidden layers, $m$ examples, input dimension $d$ and the training inputs; use canonical mobilities $(n,1,\ldots,1,n)$, squared mean loss, independent first-weight entries $N(0,1)$, hidden entries $N(0,1/n)$, and exactly zero readout. Each activation is $C^1$, with globally bounded and globally Lipschitz derivative. Let $h_a^{(\ell)}$ denote sample $a$'s layer-$\ell$ activation and $f_a$ its prediction. Require limiting initial top-feature Gram $\Gamma_{w,\infty}(0)=\lim_n[(h_a^{(L)}(0)^\top h_b^{(L)}(0))/(mn)]_{ab}\succeq2\lambda I_m$ for some $\lambda>0$, and label RMS $Y_{\rm lab}=(m^{-1}\sum_a y_a^2)^{1/2}\le Y_*$, with the manuscript's fixed small-label threshold. The subscript distinguishes label size from image matrix $Y$. Write $\rho(t)=(m^{-1}\sum_a(f_a(t)-y_a)^2)^{1/2}$ for residual RMS.

On the common initialization events from eq:at-good-event, equations eq:at-speeds and eq:at-fitting give $\|\dot h_a^{(\ell)}\|_2/\sqrt n\le C Y_{\rm lab}\rho$ and $\int_0^\infty\rho\,dt\le Y_{\rm lab}/\kappa$ for dense and every exact order-$q$ closure path. Therefore

\[
\int_0^\infty\|\dot h_a^{(\ell)}(t)\|_2/\sqrt n\,dt
\le C Y_{\rm lab}^2/\kappa.
\]

Equation (5) consequently bounds forward rank by $m(1+C Y_{\rm lab}^2/(\kappa\varepsilon))$ per link, uniformly in width, order and horizon on those events. Constants and $Y_*$ depend on fixed depth, data, activation bounds and Gram gap. This is a conditional consequence of the manuscript, not a new independent audit of its theorem; general-depth reverse-query variation and the perturbed oracle trajectory require further arguments.

**Two-hidden-layer tanh corollary.** Under those same small-label assumptions, specialize to $L=2$ and $\phi=\tanh$. The initialized middle matrix is queried forwards on $h_a^{(1)}$ and backwards on $\delta_a^{(2)}=w\odot(1-(h_a^{(2)})^2)$, where powers are coordinatewise. The readout equation, unchanged by order-$q$ compression, and $|h_{a,i}^{(2)}|\le1$ imply

\[
\|\dot w\|_\infty
\le\frac2m\sum_a|f_a-y_a|\le2\rho,\qquad
\frac{\|\dot w\|_2}{\sqrt n}\le2\rho,\qquad
\|w(t)\|_\infty\le2\int_0^t\rho\,du\le\frac{2Y_{\rm lab}}{\kappa}.
\]

The last inequality uses $w(0)=0$. Differentiating the displayed backward query gives

\[
\dot\delta_a^{(2)}
=\dot w\odot(1-(h_a^{(2)})^2)
-2w\odot h_a^{(2)}\odot\dot h_a^{(2)}.
\]

Applying the coordinate bounds and eq:at-speeds, then integrating eq:at-fitting, yields

\[
\frac{\|\dot\delta_a^{(2)}\|_2}{\sqrt n}
\le\left(2+\frac{4C Y_{\rm lab}^2}{\kappa}\right)\rho,\qquad
\int_0^\infty\frac{\|\dot\delta_a^{(2)}\|_2}{\sqrt n}\,dt
\le\left(2+\frac{4C Y_{\rm lab}^2}{\kappa}\right)\frac{Y_{\rm lab}}{\kappa}.
\]

Consequently the combined right/left greedy dictionary rank along either exact dense or exact closure trajectory is at most

\[
r+s\le
2m+\frac m\varepsilon\left[
\frac{C Y_{\rm lab}^2}{\kappa}
+\left(2+\frac{4C Y_{\rm lab}^2}{\kappa}\right)\frac{Y_{\rm lab}}{\kappa}
\right],                                               \tag{5a}
\]

also capped by $2n$. This closes the exact-path variation gap in both directions for this specific architecture, uniformly in width, memory order and horizon. The reverse query here is $\delta_a^{(2)}$, not $(f_a-y_a)\delta_a^{(2)}/\rho$; no normalized-residual derivative is needed. Oracle-induced trajectory perturbations, replay jumps and numerical integration remain outside this corollary.

With $R=r+s$, dictionary storage is $O(nR)$ and work per call is $O(n(1+R))$, including all images and both bases; paired memory adds $O(Lmnq)$ state. This is potentially linear in width, but $R\ll n$ is a substantive condition, and retained Gaussian constraints remain moving state. A hard rank cap must report failure or change the stated guarantee when reached.

## 4. Conditional compact-horizon coupling

Let $S_{n,q}$ denote the paper's complete order-$q$ moment state: first weights, readout, clock and raw paired moments. At fixed initialized matrices its exact autonomous equation is \(\dot S=F_{n,q}(S)\). Use a norm formed from Euclidean RMS norms of its vector blocks and ordinary scalar norms; coefficients may depend on fixed $q,m,L$. The oracle state additionally contains its retained bases and images.

Assume on a comparison region through $T$:

1. $F_{n,q}$ is Lipschitz with constant \(\Lambda\).
2. Its sequential forward/backward evaluator has perturbation bound $B\eta$ when each initialized-matrix call has RMS error at most \(\eta\).
3. Exact and approximate trajectories remain in that region; all query tests use their actual current inputs, and time-discretization error is separately controlled.

At finite $n,q$, smooth activations and a bounded compact region provide finite such constants. Their uniformity in $n$ is an additional assumption. Equation (4) implies that the oracle routine evaluates $F_{n,q}$ with defect at most $BK\varepsilon$. Let $e_0=\|\widetilde S(0)-S(0)\|$; revealing all initialization queries exactly makes $e_0=0$. Since enrichment does not reset $S$, subtracting the integral equations gives

\[
\|\widetilde S(t)-S(t)\|
\le e_0+\int_0^t\{\Lambda\|\widetilde S(u)-S(u)\|+BK\varepsilon\}\,du
\le e_0e^{\Lambda t}+BK\varepsilon\frac{e^{\Lambda t}-1}{\Lambda}. \tag{6}
\]

The fraction is $t$ when \(\Lambda=0\). If the exact output map is $C_{\rm out}$-Lipschitz and its approximate evaluator has sensitivity $B_{\rm out}$, prediction error is at most $C_{\rm out}\|\widetilde S-S\|+B_{\rm out}K\varepsilon$. A strict comparison-region margin can exclude exit once (6) is smaller than that margin. Discrete integration requires its own stability/error term; per-call bounds alone do not certify an integrator.

Width-uniform approximate-path $A_h,A_b,B,\Lambda$, continuation under oracle perturbations, sampling/concentration rates, and any all-time analogue remain open here. In particular, backward gating multiplies perturbations by learned carriers; bounded activation slope and bounded Gaussian operator norm alone do not establish width-uniform Lipschitz constants in RMS. The manuscript's cutoff/tail comparison suggests a weaker modulus may be preferable.

Bordelon–Pehlevan's nonlinear DMFT solver already samples Gaussian population paths with two-time covariance and causal response kernels, iterating kernel self-consistency. It retains the time grid; inspecting Algorithm 1 does not reveal a fixed-$q$ temporal Galerkin scheme. Neither its Gaussian processes nor the finite-program Tensor Programs description license independent refreshing of reused disorder. [Bordelon–Pehlevan, Appendix B](https://arxiv.org/html/2205.09653v3); [Yang–Hu, Tensor Programs IV](https://proceedings.mlr.press/v139/yang21c.html).

The cheapest decision is the authorized query-rank screen, followed—only if favorable—by coupled approximate/exact oracle training. It must measure both directions, stability under time refinement, and subsequent trajectory error. Low learned-increment rank alone is insufficient. Even success would establish a cheaper large-width simulator before it establishes a finite-history population solver.

Automatic differentiation through this sampler needs a separate coupling argument. Keeping its Gaussian seed fixed while changing a training intervention changes adaptive bases and generally the completed $W$. That derivative is not automatically the fixed-$W$ intervention derivative. A shared oracle across branches, or explicit tangent queries $W\,dh$ and $W^\top db$ consistent with the same completion, are possible repairs to investigate. Neither samplewise attribution nor interchange of an expectation and derivative is claimed here.

Sources inspected: current manuscript setting/memory construction; complete relevant Gaussian construction and continuation subsection in `paper/proof_alltime.tex`; fixed-order limitation at the end of `paper/proof_tracking.tex`; DMFT comparison subsection in `paper/comparison_appendix.tex`; `docs/index.qmd`, `docs/notation.qmd`; Lu's complete Gaussian algorithm/proof. External DMFT comparison was independently inspected by a scoped assisting agent; author code was not audited. No experiments were run for this note. Source HEAD: `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`; manuscript SHA256 `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95`; Gaussian proof SHA256 `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d`.
