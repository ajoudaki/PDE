# Complete combined isolated adversarial audit

**Verdict: PASS for the three stated claims and their composition. No required mathematical fixes.**

This verdict covers A's causal auxiliary rank-and-query theorem, B's deterministic comparison with the canonical finite-width flow using the same fixed clipping, and C's transfer when the common deterministic clipping bound satisfies \(R_n=o(\log n)\). It does not certify an uncut, population, global-time, original-unfiltered-rank, physical-clock, exact-GD, or velocity/kernel theorem.

## Audited files and scope

All six authorized files were read completely. The final three candidates contain 995, 411, and 163 lines; the three dependencies contain 257, 312, and 323 lines, respectively. All final supplied hashes match.

| Label | File | Verified SHA-256 |
|---|---|---|
| A | CAUSAL_FILTERED_QUERY_RANK.md | 7406ffb9c24e8359e7e188c70eb3863ff5aeb9179df3d7bba92103b98aedcfd1 |
| B | FILTERED_QUERY_CLIPPED_STABILITY.md | cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b |
| C | FILTERED_QUERY_GROWING_CLIP_TRANSFER.md | c1d5d50c8720cb3285c3aa15608b08cb9b0bfde968951c33cbe0338df1548fcd |
| Adaptive dependency | PANAHI_ADAPTIVE_GRAM_MARTINGALE.md | 6cec745dde896fa2932592b126f48488618cd426a45de1fa03598fd467bdb4b5 |
| Euler dependency | PANAHI_EULER_PERTURBATION_SIZE.md | 5c5b7a7fe40a670da99f3d188c7bbbba22b969ef1cecdeb21ac6027f7538809b |
| Integrated dependency | INTEGRATED_INITIAL_QUERY_COMPRESSION.md | 2c97e9fe8c4e9b3a66d7efdf80f825f8c7bb6275649518c47fc001aef6b57c73 |

All these files are in /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z. The solve-math-rigorously skill was read directly and applied. No candidate was edited by this audit. No ledgers, master notes, other project context, experiments, or subagents were used.

During this audit the user supplied one presentation-only revision of B, replacing its diagonal derivative notation by explicit \(\phi'(z^{(1)})^2\) coordinate multiplication. The revised block was rechecked and the final B hash above verified. Its mathematical identities and bounds are unchanged. The standalone report remains untouched at its historical B hash, 9e611d03ff2e82b0acd6f17d2786ed6e5d84c06777672aee6dc86a6c934edb55.

The external checks were confined to Panahi v1's perturbation definition in equation (9), and the rectangular Freedman inequality already explicitly cited by the authorized adaptive dependency. Neither Panahi's distribution comparison nor its complex-continuation claim is assumed. The previous standalone B verdict is not used as a substitute for the reconstruction below.

Vector norms are ordinary Euclidean norms \(\|\cdot\|_2\), with factors \(1/\sqrt n\) written explicitly. The stated readout coordinate bound uses \(\|\cdot\|_\infty\). Matrix norms are operator or Frobenius norms as marked; all finite products use ordinary transpose \(T\). Below, \(r_n\) denotes A's effective-rank ceiling, while \(R_n\) denotes C's clipping bound. These are different quantities.

For A and C, fix \(S>0\) and an integer \(n\ge2\), with
\[
 \eta=n^{-2},\quad N=\lceil Sn^2\rceil,\quad
 T=N\eta\le S+1,\quad K=N+1,\quad
 \sigma=n^{-1/4},\quad \epsilon=\varepsilon=n^{-1/8},\quad
 \ell_n=\log(e+n).
\]
For a history matrix \(X\), its effective rank is
\[
 \rho(X)=\operatorname{tr}[XX^T(XX^T+\sigma^2I_n)^{-1}].
\]
The four matrices \(X\) are \(\Theta^{(2)},\Omega^{(2)}/\sqrt n,\Theta^{(3)},\Omega^{(3)}/\sqrt n\), including warmups. Columns have no extra mesh weight and are not divided by the number of calls. B's reconstruction below also applies to its full stated parameter range, beyond this particular choice of mesh and filter scale.

## 1. Oracle definition, exact scaling, initialization, and causality

For one of the two initial matrices, put \(G=\sqrt n W_0\). For raw reverse and forward arguments \(v_l,h_l\), the source arguments and exact responses are
\[
 \theta_l=\frac{v_l}{\sqrt n},\qquad \omega_l=h_l,\qquad
 G^T\theta_l=W_0^Tv_l,\qquad
 \frac1nG\omega_l=\frac1{\sqrt n}W_0h_l.
\]
Thus the forward source response must be multiplied by \(\sqrt n\) to become the raw forward field, whereas the reverse source response is already raw.

With source covariance \(I\), one mixture component, and source parameter \(z=0\), equation (9) has an inclusive upper-triangular forward Gamma term and a strictly upper-triangular reverse term. It assigns direct noises \(\sigma U/\sqrt m\) to the source forward response and \(\sigma V\) to the raw reverse response. A exchanges the names of two independent arrays. For \(m=n\), both resulting raw direct noises have coordinate variance \(\sigma^2\). This definition check agrees with A(13)--(16). [Panahi v1, equation (9)](https://arxiv.org/pdf/2603.09310v1#page=4).

In particular, the actual raw errors are exactly
\[
 e_l^{\rm rev}=\sqrt n\,k_l+\sigma U_l,\qquad
 e_l^{\rm for}=\sqrt n\,g_l+\sigma V_l,
\]
and hence
\[
 \frac{\|e_l^{\rm rev}\|_2}{\sqrt n}
 \le\|k_l\|_2+\sigma\frac{\|U_l\|_2}{\sqrt n},\qquad
 \frac{\|e_l^{\rm for}\|_2}{\sqrt n}
 \le\|g_l\|_2+\sigma\frac{\|V_l\|_2}{\sqrt n}.
\]
There is no extra or missing width factor.

Each matrix receives exactly \(K=N+1\) query pairs: one warmup, then \(l=j+2\) for \(0\le j<N\). At either warmup, \(\theta_1=0\), so \(t_1=0\), \(g_1=0\), and the strict sum gives \(k_1=0\). The two forward noises remain. Consequently
\[
 z_0^{(2)}=W_0^{(2)}h_0^{(1)}+\sigma V_1^{(2)},\qquad
 z_0^{(3)}=W_0^{(3)}\phi(z_0^{(2)})+\sigma V_1^{(3)}.
\]
These equalities describe the declared calls. The algorithm does not separately evaluate exact canonical fields. Its discarded reverse warmup outputs are still counted in the total number of noise vectors.

For a fixed matrix label \(b\in\{2,3\}\), reveal all primitive seeds, both matrices, all direct-noise arrays, and the other matrix's entire Gamma array in \(\mathcal H^{(b)}\). This sigma-field is independent of its own \(\Gamma^{(b)}\). A's half-step filtration then reveals only its own leading square, followed by its next off-diagonal row, followed by its next column including the diagonal.

Induction verifies the needed measurability. Before call \(l=j+2\), state \(j\) is a function of the seeds and calls through \(l-1\) of both matrices. The other matrix's past computations are functions of the already revealed primitive arrays and the own past square; their realized transcript is not being declared independent. Both current arguments of both matrices are selected from this pre-step state. Therefore \(\theta_l\) is measurable before the own fresh row, and \(\omega_l\) is measurable before the own fresh column; in this particular algorithm both are selected even before the row. The current lower call, seen from the upper filtration, uses arrays already in \(\mathcal H^{(3)}\) and the upper past. It reveals no fresh upper Gamma entry.

The warmup also satisfies this induction: the upper forward argument is generated by the lower warmup, whose primitive inputs are in \(\mathcal H^{(3)}\). The subsequent fresh row and fresh column have their original independent Gaussian laws conditional on the respective pasts. Revealing the initial matrices themselves is legitimate for this Gamma argument; no distributional conditioning theorem for adaptive matrix queries is invoked.

Finally, finiteness and measurability hold without any good event. Every finite regularized Gram matrix is positive definite; positive-diagonal Cholesky factorization and inversion are continuous there. The inverse \(F^{-1}\) exists on all of \(\mathbb R\), and all remaining coordinate maps are continuous. Induction through finitely many calls and updates gives finite measurable registers almost surely.

## 2. Independent reconstruction of the adaptive estimate

Suppress the matrix label and use \(m=n\), the only dimensions required by A. At every leading prefix the exact Gram factors satisfy
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,\qquad
 A_{\omega,l}^TA_{\omega,l}=\frac1n\Omega_l^T\Omega_l+\sigma^2I_l.
\]
The positive-diagonal upper Cholesky convention makes the columns
\[
 t_i=(\Theta_lA_{\theta,l}^{-1})_i,\qquad
 s_i=\frac1{\sqrt n}(\Omega_lA_{\omega,l}^{-1})_i
\]
permanent as \(l\) increases. Indeed an upper-triangular inverse has zero entries below its diagonal, so column \(i\) uses only the first \(i\) query columns and the leading Cholesky block.

The Gamma terms to be estimated are exactly
\[
 g_l=\frac1{\sqrt n}\sum_{i\le l}t_i(\Gamma A_{\omega,l})_{il},
 \qquad
 k_l=\frac1{\sqrt n}\sum_{i<l}s_i(\Gamma^T A_{\theta,l})_{il},
\]
where each product uses the leading \(l\)-by-\(l\) Gamma block. The second sum is strict.

The covariance matrices
\[
 \mathsf T_l=\sum_{i\le l}t_it_i^T,\qquad
 \mathsf S_l=\sum_{i\le l}s_is_i^T
\]
are bounded above by \(I_n\). For example,
\[
 \mathsf T_l
 =\Theta_l(\Theta_l^T\Theta_l+\sigma^2I)^{-1}\Theta_l^T
\]
has eigenvalues \(d_i^2/(d_i^2+\sigma^2)\). Their traces are the effective ranks. The permanent-column representation proves prefix monotonicity as well as \(\|t_i\|_2,\|s_i\|_2\le1\).

Define, as in A(24),
\[
\begin{aligned}
 B_{l-1/2}&=\sum_{i\le l,j<l}t_i\Gamma_{ij}s_j^T,&
 B_l&=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\\
 \mathfrak a_l&=\sum_{j<l}s_j\Gamma_{lj},&
 \mathfrak b_l&=\sum_{i\le l}t_i\Gamma_{il}.
\end{aligned}
\]
The increments are \(t_l\mathfrak a_l^T\) and \(\mathfrak b_ls_l^T\). Their fresh vectors, conditional on the respective preceding half-steps, have laws
\[
 \mathfrak a_l\sim N(0,\mathsf S_{l-1}),\qquad
 \mathfrak b_l\sim N(0,\mathsf T_l).
\]
The first coefficient \(t_l\) is known before the row, and the second coefficient \(s_l\) before the column. Consequently \(B\) is a matrix martingale. Bounded coefficients and Gaussian moments give finite moments at every finite horizon, regardless of raw query magnitudes.

The Gram identity gives
\[
 \frac{s_i^T\omega_l}{\sqrt n}
 =(A_\omega-\sigma^2A_\omega^{-T})_{il}.
\]
For \(i<l\) the inverse-transpose entry vanishes, and on the diagonal it equals \(1/A_{\omega,ll}\). The analogous identity for \(t_i^T\theta_l\) proves
\[
 g_l=\frac1nB_l\omega_l+
       \frac{\sigma^2}{\sqrt n A_{\omega,ll}}\mathfrak b_l,\qquad
 k_l=\frac1{\sqrt n}B_{l-1/2}^T\theta_l+
       \frac{\sigma^2}{\sqrt n A_{\theta,ll}}\mathfrak a_l.
\]
This verifies the residual terms, including the strict reverse triangle. The Schur complement
\[
 A_{ll}^2
 =\sigma^2+y^T[I-X(X^TX+\sigma^2I)^{-1}X^T]y
 \ge\sigma^2
\]
implies \(\sigma^2/A_{ll}\le\sigma\).

For completeness, the localization in the dependency is valid for the actual histories. With deterministic thresholds \(r_\theta,r_\omega\) and \(r=\max(r_\theta,r_\omega)>0\), permanently stop accepting increments before a known rank would exceed its threshold. Before a row, the current reverse rank and previous forward rank are known. Before a column, the current forward rank is also known. These indicators are predictable. They do not change the histories used as coefficients, and all increments are accepted on the final rank event.

For an accepted row \(X_l=t_l\mathfrak a_l^T\), conditional second moments are
\[
 \mathbb E[X_lX_l^T\mid\text{past}]
   =(\operatorname{tr}\mathsf S_{l-1})t_lt_l^T,\qquad
 \mathbb E[X_l^TX_l\mid\text{past}]
   =\|t_l\|_2^2\mathsf S_{l-1}.
\]
For an accepted column \(Y_l=\mathfrak b_ls_l^T\), they are
\[
 \mathbb E[Y_lY_l^T\mid\text{past}]
   =\|s_l\|_2^2\mathsf T_l,\qquad
 \mathbb E[Y_l^TY_l\mid\text{past}]
   =(\operatorname{tr}\mathsf T_l)s_ls_l^T.
\]
Summing along a path gives
\[
\begin{aligned}
 W_{\rm left}
 &\preceq r_\omega\sum_{\text{accepted rows}}t_lt_l^T
        +\sum_{\text{accepted columns}}\|s_l\|_2^2 I_n
 \preceq2r_\omega I_n,\\
 W_{\rm right}
 &\preceq\sum_{\text{accepted rows}}\|t_l\|_2^2 I_n
        +r_\theta\sum_{\text{accepted columns}}s_ls_l^T
 \preceq2r_\theta I_n.
\end{aligned}
\]
The trace restrictions bound the sums of squared column norms, and the Gram contractions bound the sums of outer products. This step incurs no factor \(K\).

Set
\[
 u=\log(4K/\alpha),\qquad v=\log(4n/\alpha),\qquad
 c(r)=\sqrt{2r+4u},\qquad
 L(r)=2\sqrt{rv}+\frac23c(r)v.
\]
Truncate each accepted increment when the norm of its fresh Gaussian vector exceeds \(c(r)\). Conditional symmetry leaves the truncated increments centered; their second moments decrease in positive-semidefinite order, and their operator norms are at most \(c(r)\). If \(Z\) is an accepted fresh vector with covariance eigenvalues \(\lambda_i\in[0,1]\) of sum at most \(r\), then
\[
 \mathbb E[e^{\|Z\|_2^2/4}\mid\text{past}]
 =\prod_i(1-\lambda_i/2)^{-1/2}\le e^{r/2}.
\]
Markov's inequality gives a conditional truncation probability at most \(e^{-u}\). The union over at most \(2K\) half-steps costs at most \(\alpha/2\). On the rank event outside this failure, the truncated process agrees with the original process at every half-step, and every fresh-vector norm is at most \(c(r)\).

The rectangular Freedman inequality applies to a zero-initialized matrix martingale with bounded increment operator norms and bounded left and right predictable quadratic variations. With dimensions \(n,n\), increment bound \(c(r)\), and variation bound \(2r\), its maximal tail bound is
\[
 2n\exp\!\left[-\frac{x^2}{2(2r+c(r)x/3)}\right].
\]
Adaptation, centering, integrability, and both variation hypotheses were verified above for the truncated process. The stated form and constants agree with the dependency's cited [Tropp, Corollary 1.3](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf#page=3).

For \(x=L(r)\), direct expansion gives
\[
 L(r)^2\ge4rv+\frac23c(r)vL(r).
\]
Thus the Freedman failure probability is at most \(\alpha/2\). Adding the truncation failure proves A(27), including its maximum over every half-step and its event-intersection form. No conditioning on a final adaptive history has occurred.

The exact Gamma identities now imply
\[
 \|g_l\|_2\le\frac{L(r)\|h_l\|_2}{n}
                 +\frac{\sigma c(r)}{\sqrt n},\qquad
 \|k_l\|_2\le\frac{L(r)\|v_l\|_2}{n}
                 +\frac{\sigma c(r)}{\sqrt n}.
\]
These hold at the actual query arguments, whose magnitudes may subsequently be bounded on the same event. A real, rather than integer, ceiling \(r\) presents no difficulty for the stopping thresholds.

## 3. First pass: actual-state bounds without a rank premise

For a matrix with independent \(N(0,1/n)\) entries, a \(1/4\)-net of the unit sphere has at most \(9^n\) points. Approximating both vectors in a bilinear form gives
\[
 \|W_0\|_{\rm op}
 \le2\max_{x,y\text{ in the net}}|x^TW_0y|.
\]
Each fixed form has variance \(1/n\); the Gaussian tail at four and a union bound give \(2\cdot9^{2n}e^{-8n}\). For the two matrices and the readout with coordinate variance \(n^{-2}\), the failure probability of A's initialization event is therefore
\[
 p_0(n)=4e^{-(8-2\log9)n}+2ne^{-n^2/2}.
\]
This checks the exact exponential constants in A(4).

Take \(\alpha=n^{-2}\). There are \(4K\) direct-noise vectors, each in \(\mathbb R^n\). The bound
\[
 \mathbb E e^{\|Z\|_2^2/4}=2^{n/2}\le e^{n/2}
\]
gives
\[
 \mathbb P(\|Z\|_2^2>2n+4u)\le e^{-u}.
\]
Thus A's direct-noise event, with
\[
 D_n=\sqrt{2+4u/n},\qquad u=\log(4Kn^2),
\]
fails with probability at most \(\alpha\). It holds irrespective of the later histories generated by those noises.

Every effective rank is at most \(n\), without any bound on query magnitudes. Apply the adaptive estimate with \(r=n\) to each matrix. Intersecting these two events with initialization and direct noise gives \(E_C\) with
\[
 \mathbb P(E_C^c)\le p_0(n)+3n^{-2}.
\]
Since \(K\le(S+2)n^2\), \(u,v\le C_S\ell_n\), where \(\ell_n=\log(e+n)\). Consequently \(D_n\le C_S\) and \(L(n)/\sqrt n\le C_S\ell_n\). The raw oracle outputs satisfy
\[
 \frac{\|\mathcal R_l\|_2}{\sqrt n}
 \le C_S\ell_n\frac{\|v_l\|_2}{\sqrt n}+C_S\sigma,\qquad
 \frac{\|\mathcal F_l\|_2}{\sqrt n}
 \le C_S\ell_n\frac{\|h_l\|_2}{\sqrt n}+C_S\sigma.
\]
These estimates do not presuppose bounded reverse queries.

Here is the resulting noncircular order of bounds on \(E_C\). Write \(c_\phi=\pi/2\) and \(B_4=1+(S+1)c_\phi\). Bounded activations first give
\[
 \|W_j^{(4)}\|_\infty\le B_4,\qquad
 \frac{\|\delta_j^{(3)}\|_2}{\sqrt n}\le B_4,\qquad
 \|M_j^{(3)}\|_F\le T B_4c_\phi.
\]
The upper reverse query and its learned correction then give
\[
 \frac{\|q_j^{(2)}\|_2}{\sqrt n}\le C_S\ell_n,\qquad
 \frac{\|\delta_j^{(2)}\|_2}{\sqrt n}\le C_S\ell_n.
\]
The second inequality needs only \(|\tau(v)|\le|v|\) and \(|\phi'|\le1\). Summing the slow updates yields
\[
 \frac{\|a_j^{(2)}\|_2}{\sqrt n}\le C_S\ell_n,\qquad
 \|M_j^{(2)}\|_F\le C_S\ell_n,\qquad
 \frac{\|R_j^{(1)}\|_2}{\sqrt n}\le C_S\ell_n^2.
\]
The rank-one identity used throughout is
\[
 \left\|\frac1nuv^T\right\|_F
 =\frac{\|u\|_2\|v\|_2}{n}.
\]
It follows that the lower reverse output is bounded by \(C_S\ell_n^2\) after division by \(\sqrt n\), and both forward outputs by \(C_S\ell_n\).

Finally, \(\lambda=\eta/\epsilon=n^{-15/8}\in(0,1]\) makes the three register filters convex combinations. Apply them to the bottom displacement \(x_j^{(1)}-x_0^{(1)}\), and to the two preactivations. Their bounded targets and warmup values imply
\[
 \max_{j\le N}\frac{\|x_j^{(1)}-x_0^{(1)}\|_2}{\sqrt n}
 \le C_S\ell_n^2,\qquad
 \max_{j\le N}\frac{\|z_j^{(2)}\|_2\vee\|z_j^{(3)}\|_2}{\sqrt n}
 \le C_S\ell_n.
\]
No bound on \(F(z_0^{(1)})\) is needed. The bounds use neither B nor a small-rank assumption, and their constants do not depend on the clipping level.

## 4. Actual-history regularity, integer rank lemma, and localization

Subtracting successive filter updates gives
\[
 \frac{\|x_{j+1}^{(1)}-x_j^{(1)}\|_2}{\sqrt n}
 \le C_S\eta\ell_n^2/\epsilon,\qquad
 \frac{\|z_{j+1}^{(\ell)}-z_j^{(\ell)}\|_2}{\sqrt n}
 \le C_S\eta\ell_n/\epsilon\quad(\ell=2,3).
\]
The derivative of \(\phi\circ F^{-1}\) is \(\phi'(F^{-1}(x))^2\le1\), so the first bound transfers to \(h^{(1)}\); the second transfers to \(h^{(2)}\). Also,
\[
\begin{aligned}
 \delta_{j+1}^{(3)}-\delta_j^{(3)}
 ={}&(W_{j+1}^{(4)}-W_j^{(4)})\odot\phi'(z_{j+1}^{(3)})\\
 &+W_j^{(4)}\odot[\phi'(z_{j+1}^{(3)})-\phi'(z_j^{(3)})],
\end{aligned}
\]
and therefore
\[
 \frac{\|\delta_{j+1}^{(3)}-\delta_j^{(3)}\|_2}{\sqrt n}
 \le\eta c_\phi+2B_4
           \frac{\|z_{j+1}^{(3)}-z_j^{(3)}\|_2}{\sqrt n}
 \le C_S\eta\ell_n/\epsilon.
\]
The primitive has increment at most \(C_S\eta\ell_n\) after division by \(\sqrt n\). Summation over adjacent increments supplies the feature-time Lipschitz constants for all four actual histories. A deterministic
\[
 M_*=C_*(S)\ell_n^2/\epsilon
\]
dominates them.

This estimate is only for mesh columns. The upper reverse warmup is zero, while its first mesh query is \(\delta_0^{(3)}/\sqrt n\) at the same time; no Lipschitz estimate across this pair is justified or used. A retains the warmup column exactly. The other three warmup arguments repeat the first mesh argument (both lower reverse arguments are zero). Allowing one extra approximation direction for every warmup is conservative and valid.

Here is the independent rank-lemma reconstruction. Let \(X\) be one full history, with one warmup and \(N\) mesh columns. For an integer \(1\le d\le N\), partition mesh indices into the \(d\) nonempty blocks
\[
 \lfloor(a-1)N/d\rfloor<i\le\lfloor aN/d\rfloor.
\]
Replace each mesh column by its block's first column and keep the warmup exactly, giving \(Y\). Each block spans at most
\[
 \eta(\lceil N/d\rceil-1)\le T/d.
\]
Thus
\[
 \operatorname{rank}Y\le d+1,\qquad
 \|X-Y\|_F^2\le N M_*^2T^2/d^2.
\]
For the orthogonal projection \(P\) onto the columns of \(Y\), put
\[
 Q_X=XX^T(XX^T+\sigma^2I)^{-1}.
\]
Since \(0\preceq Q_X\preceq I\) and \(Q_X\preceq XX^T/\sigma^2\),
\[
\begin{aligned}
 \rho(X)
 &=\operatorname{tr}(PQ_X)+\operatorname{tr}((I-P)Q_X)\\
 &\le d+1+\sigma^{-2}\|(I-P)X\|_F^2\\
 &\le d+1+\frac{NM_*^2T^2}{\sigma^2d^2}.
\end{aligned}
\]
This argument works for every realized matrix, including adaptive matrices and histories with more columns than rows.

Set
\[
 x_*=(NM_*^2T^2/\sigma^2)^{1/3},\qquad
 d=\min\{N,\max\{1,\lceil x_*\rceil\}\}.
\]
If \(0<x_*\le N\), then \(d\le x_*+1\) and \(d\ge x_*\), so the last bound is at most \(2+2x_*\). If \(x_*=0\), \(d=1\) gives two. If \(x_*>N\), the exact dimension bound \(K=N+1\le2+2x_*\) suffices. Hence
\[
 \rho(X)\le r_n:=\min\{n,K,2+2x_*\}.
\]
This includes \(N=1\), and the ceiling is deterministic even though \(X\) is random. Without a separate warmup, the same proof gives the Euler dependency's bound \(\min\{K,1+2(KM^2T^2/\sigma^2)^{1/3}\}\). Its integer optimization is also valid at zero Lipschitz constant.

For A's parameters,
\[
 x_*\le C_S(n^2n^{1/4}n^{1/2})^{1/3}\ell_n^{4/3}
       =C_S n^{11/12}\ell_n^{4/3}.
\]
Prefix monotonicity of the permanent-column traces extends this estimate to every prefix of each of the four histories. It holds on \(E_C\), the event obtained before any small-rank premise. No frozen-history Gaussian identity has entered this rank argument.

Apply the adaptive theorem again, with this deterministic \(r_n\), to the same two original processes and arrays. For each matrix \(b\), let \(F_b\) be its final-rank event intersected with violation of the refined martingale or residual bounds. The theorem gives \(\mathbb P(F_b)\le n^{-2}\) unconditionally. Since \(E_C\) implies both final-rank events,
\[
 \mathcal E_n^\tau=E_C\setminus(F_2\cup F_3)
\]
has
\[
 \mathbb P(\mathcal E_n^\tau)
 \ge1-p_0(n)-5n^{-2}.
\]
This is A(4). It does not require conditioning the second application on \(E_C\), resampling, or independence between the two resulting bad events.

The refined size calculation is
\[
 \frac{L(r_n)}{\sqrt n}
 \le C_S\!\left(\sqrt{r_n/n}\,\ell_n+
                         n^{-1/2}\ell_n^{3/2}\right)
 \le C_S n^{-1/24}\ell_n^{5/3}
       +C_S n^{-1/2}\ell_n^{3/2}.
\]
All raw forward arguments have Euclidean norm divided by \(\sqrt n\) at most \(c_\phi\); upper reverse arguments have bound \(B_4\); lower reverse arguments have bound \(C_S\ell_n\). Since \(r_n\le n\), the residual term obeys \(\sigma c(r_n)/\sqrt n\le C_S\sigma\). Including direct noise gives
\[
 \max_{b,l}
 \frac{\|e_l^{(b),\rm rev}\|_2\vee\|e_l^{(b),\rm for}\|_2}{\sqrt n}
 \le C_Sn^{-1/24}\ell_n^{8/3}
      +C_Sn^{-1/2}\ell_n^{5/2}+C_S\sigma.
\]
The middle term is absorbed by the first because their ratio is \(n^{-11/24}\ell_n^{-1/6}\le1\). This proves A(6), with \(\sigma=n^{-1/4}\), on the same event as the rank bound. The primitive bound A(60) follows directly by the triangle inequality and \(N\eta=T\).

For A's separately mentioned \(S=0\) case, \(N=0,K=1\), Gamma terms vanish, reverse histories are zero, and forward ranks are at most one. Its warmup-only assertion is valid and is not needed for C, which assumes \(S>0\).

## 5. Exact A-to-B identification and continuous versus discrete memories

From this section onward, hats denote A's algorithm, and unhatted variables denote B's canonical finite-width reference flow. The common matrices \(W_0^{(2)},W_0^{(3)}\), bottom seed \(z_0^{(1)}\), and readout \(W_0^{(4)}\) are identical in the two processes. The scalar clipping map is also identical. Only the algorithm's layer-two and layer-three warmup registers are noisy.

At \(k=j\) and \(l=k+2\), the four outputs identify as follows:

| A's declared raw output | B's output | Exact initial-matrix action |
|---|---|---|
| \(\mathcal R_{k+2}^{(2)}\) | \(\widehat T_k^{(2)}\) | \((W_0^{(2)})^T\widehat a_k^{(2)}\) |
| \(\mathcal F_{k+2}^{(2)}\) | \(\widehat F_k^{(2)}\) | \(W_0^{(2)}\widehat h_k^{(1)}\) |
| \(\mathcal R_{k+2}^{(3)}\) | \(\widehat T_k^{(3)}\) | \((W_0^{(3)})^T\widehat\delta_k^{(3)}\) |
| \(\mathcal F_{k+2}^{(3)}\) | \(\widehat F_k^{(3)}\) | \(W_0^{(3)}\widehat h_k^{(2)}\) |

The error in each entry is the output minus the action in the last column, evaluated on that same actual argument. Both constructions form
\[
 \widehat q_k^{(2)}
 =\widehat T_k^{(3)}+(\widehat M_k^{(3)})^T\widehat\delta_k^{(3)},
 \qquad
 \widehat\delta_k^{(2)}
 =\phi'(\widehat z_k^{(2)})\odot\tau(\widehat q_k^{(2)}),
\]
with \(\widehat\delta_k^{(3)}=\widehat W_k^{(4)}\odot\phi'(\widehat z_k^{(3)})\). The five slow updates in both are exactly
\[
\begin{aligned}
 \widehat a_{k+1}^{(2)}-\widehat a_k^{(2)}
     &=\eta\widehat\delta_k^{(2)},\\
 \widehat M_{k+1}^{(2)}-\widehat M_k^{(2)}
     &=\frac{\eta}{n}\widehat\delta_k^{(2)}(\widehat h_k^{(1)})^T,\\
 \widehat M_{k+1}^{(3)}-\widehat M_k^{(3)}
     &=\frac{\eta}{n}\widehat\delta_k^{(3)}(\widehat h_k^{(2)})^T,\\
 \widehat R_{k+1}^{(1)}-\widehat R_k^{(1)}
     &=\eta(\widehat M_k^{(2)})^T\widehat\delta_k^{(2)},\\
 \widehat W_{k+1}^{(4)}-\widehat W_k^{(4)}
     &=\eta\widehat h_k^{(3)}.
\end{aligned}
\]
The three filters are likewise identical, with coefficient \(\eta/\epsilon=\eta/\varepsilon\), and targets
\[
 x_0^{(1)}+\widehat T_k^{(2)}+\widehat R_k^{(1)},\qquad
 \widehat F_k^{(2)}+\widehat M_k^{(2)}\widehat h_k^{(1)},\qquad
 \widehat F_k^{(3)}+\widehat M_k^{(3)}\widehat h_k^{(2)}.
\]
All target factors and slow-update factors are pre-step quantities. No updated readout, primitive, or learned matrix is substituted. The current upper reverse query enters the current lower backward field in both constructions.

The integrated dependency gives the exact continuous identities
\[
 M^{(\ell)}(s)=\frac1n\int_0^s
       \delta^{(\ell)}(u)(h^{(\ell-1)}(u))^T\,du
       \quad(\ell=2,3),
\]
\[
\begin{aligned}
 R^{(1)}(s)
 &=\int_0^s(M^{(2)}(t))^T\delta^{(2)}(t)\,dt\\
 &=\frac1n\int_0^s h^{(1)}(u)(\delta^{(2)}(u))^T
                    [a^{(2)}(s)-a^{(2)}(u)]\,du.
\end{aligned}
\]
The second equality follows by interchanging continuous integrals over \(0\le u\le t\le s\); the finite trajectories are continuous on a compact interval, so the integrands are integrable. These identities remain true with clipping because they use the stated rank-update equations, not a special formula for \(\delta^{(2)}\).

The exact discrete identities are
\[
 \widehat M_k^{(\ell)}
 =\frac{\eta}{n}\sum_{i<k}
           \widehat\delta_i^{(\ell)}(\widehat h_i^{(\ell-1)})^T,
\]
\[
\begin{aligned}
 \widehat R_k^{(1)}
 &=\frac{\eta^2}{n}\sum_{0\le u<i<k}
          \widehat h_u^{(1)}(\widehat\delta_u^{(2)})^T
                                  \widehat\delta_i^{(2)}\\
 &=\frac{\eta}{n}\sum_{u<k}
       \widehat h_u^{(1)}(\widehat\delta_u^{(2)})^T
                  [\widehat a_k^{(2)}-\widehat a_{u+1}^{(2)}].
\end{aligned}
\]
The index \(u+1\) is essential: it excludes the diagonal increment. Thus A(22a), B's simultaneous returned-memory update, and the continuous integrated representation agree in precisely the required sense. Discrete sums are compared with continuous integrals by quadrature; they are not equated at finite mesh.

The integrated dependency's four initial-matrix arguments are \(h^{(1)},a^{(2)},h^{(2)},\delta^{(3)}\), exactly the four arguments used by A. Its supplied-trajectory regularity is not imported to prove A's regularity. Its integration-by-parts estimates for the learned memories are consistent with the identities above, but B obtains its comparison directly from the five slow equations. The Euler dependency's frozen Gaussian isometries are also not applied to adaptive histories; only its exact triangular formulas and deterministic column-approximation principle enter the present chain.

## 6. Reconstruction of B and the precise clipping dependence

For the deterministic argument, enlarge \(S\) to \(\max\{1,S\}\) if needed and put \(T_0=\max\{1,S\}+1\). Let \(c=\pi/2\) and choose explicit constants
\[
\begin{gathered}
 U=1+cT_0,\quad J_3=cT_0U,\quad P_3=M+J_3,\\
 Q=P_3U+1,\quad J_2=cT_0Q,\quad P_2=M+J_2.
\end{gathered}
\]
They depend only on \(S,M\), not on clipping. Under B's paired error bound \(b\le1\), both the reference and algorithm satisfy
\[
 \|W^{(4)}\|_\infty\le U,\qquad
 \frac{\|\delta^{(3)}\|_2}{\sqrt n}\le U,\qquad
 \|M^{(3)}\|_F\le J_3,
\]
\[
 \frac{\|q^{(2)}\|_2}{\sqrt n}\le Q,\qquad
 \frac{\|\delta^{(2)}\|_2}{\sqrt n}\le Q,\qquad
 \|M^{(2)}\|_F\le J_2,
\]
\[
 \frac{\|a^{(2)}\|_2}{\sqrt n}\le T_0Q,\qquad
 \frac{\|R^{(1)}\|_2}{\sqrt n}\le T_0J_2Q.
\]
Hats may be inserted throughout these bounds. The trained matrix operator bounds are \(P_2,P_3\). The same sequential argument as in the first pass proves them, now using the small raw query errors instead of the coarse logarithmic oracle bound. Convexity of the filters bounds the bottom displacement and both preactivations, independently of \(R\), since the initial field errors satisfy \(d_0\le1\).

This strengthening is used only after A's second pass has already proved small errors; it introduces no circularity into the rank proof.

The reference vector field is locally Lipschitz at each finite width, including for merely Lipschitz clipping. The bounds above, together with
\[
 \frac{\|(z^{(1)})'\|_2}{\sqrt n}\le P_2Q,
\]
prevent finite-time escape of every parameter on \([0,T_0]\). The local ODE existence and continuation theorem therefore gives a unique solution throughout this interval. No uniform bound on the initial bottom coordinates is required.

The transform \(F(z)=z+z^3/3\) is a global increasing bijection, with \(F'=1/\phi'\). Hence
\[
 (x^{(1)})'=(W^{(2)})^T\delta^{(2)},\qquad
 x^{(1)}=x_0^{(1)}+(W_0^{(2)})^Ta^{(2)}+R^{(1)}.
\]
Both \(F^{-1}\) and \(\phi\circ F^{-1}\) are 1-Lipschitz. The reference differentiation formulas, including the revised explicit notation in final B, are
\[
 (h^{(1)})'
 =\phi'(z^{(1)})^2\odot(W^{(2)})^T\delta^{(2)},
\]
\[
 (z^{(2)})'=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
                      +W^{(2)}(h^{(1)})',\qquad
 (z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
                      +W^{(3)}(h^{(2)})',
\]
\[
 (\delta^{(3)})'
 =h^{(3)}\odot\phi'(z^{(3)})
  +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})',
\]
\[
 (q^{(2)})'
 =h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
           +(W^{(3)})^T(\delta^{(3)})'.
\]
For layers two and three, \((h^{(\ell)})'=\phi'(z^{(\ell)})\odot(z^{(\ell)})'\). All terms and width factors are retained.

Explicit Euclidean velocity bounds after division by \(\sqrt n\) are
\[
\begin{aligned}
 V_x&=P_2Q,& V_2&=c^2Q+P_2V_x,&
 V_3&=c^2U+P_3V_2,\\
 V_{\delta3}&=c+2UV_3,&
 V_q&=cU^2+P_3V_{\delta3}.&
\end{aligned}
\]
Here \(V_x\) also bounds the first activation velocity, and \(V_2,V_3\) bound the corresponding activation velocities. Every displayed constant is independent of \(R\).

For the middle backward field, subtraction instead of differentiating the clipping gives
\[
 \frac{\|\delta^{(2)}(s)-\delta^{(2)}(t)\|_2}{\sqrt n}
 \le\frac{\|q^{(2)}(s)-q^{(2)}(t)\|_2}{\sqrt n}
       +2R\frac{\|z^{(2)}(s)-z^{(2)}(t)\|_2}{\sqrt n}
 \le(V_q+2RV_2)|s-t|.
\]
Write \(V_{\delta2}=V_q+2RV_2\). The five reference slow right sides have respective time-Lipschitz constants
\[
\begin{aligned}
 &V_{\delta2},\\
 &cV_{\delta2}+QV_x,\\
 &cV_{\delta3}+UV_2,\\
 &cQ^2+J_2V_{\delta2},\\
 &V_3.
\end{aligned}
\]
For the returned memory, these two terms bound the time difference of \(M^{(2)}\) times \(\delta^{(2)}\), and \(M^{(2)}\) times the time difference of \(\delta^{(2)}\), respectively. All five constants are at most \(C_{S,M}(1+R)\).

For each slow equation \(y'=f\), its exact reference step is
\[
 y(s_{k+1})-y(s_k)=\eta f(s_k)+\rho_k.
\]
The residual satisfies \(\|\rho_k\|_2/\sqrt n\le L_f\eta^2/2\) for vector variables and \(\|\rho_k\|_F\le L_f\eta^2/2\) for matrix variables, by integrating \(L_f(t-s_k)\) over the step. Thus the sum of all five local quadrature errors is at most \(C_{S,M}(1+R)\eta^2\). This does not require temporal regularity of the query noise or of hatted derivatives.

Now use B's scalar errors, with their ordinary norms explicitly specified:
\[
 A_k=\frac{\|\widehat x_k^{(1)}-x^{(1)}(s_k)\|_2}{\sqrt n},\quad
 B_k=\frac{\|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2}{\sqrt n},\quad
 C_k=\frac{\|\widehat z_k^{(3)}-z^{(3)}(s_k)\|_2}{\sqrt n},
\]
\[
\begin{aligned}
 E_k={}&\frac1{\sqrt n}\big(
 \|\widehat a_k^{(2)}-a^{(2)}(s_k)\|_2
 +\|\widehat R_k^{(1)}-R^{(1)}(s_k)\|_2
 +\|\widehat W_k^{(4)}-W^{(4)}(s_k)\|_2\big)\\
 &+\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_F
  +\|\widehat M_k^{(3)}-M^{(3)}(s_k)\|_F,\qquad
 D_k=\max_{i\le k}E_i.
\end{aligned}
\]
These are scalar errors, not definitions of new norms. At initialization \(E_0=A_0=0\) and \(B_0+C_0=d_0\).

For \(p=\eta/\varepsilon\in(0,1]\), subtraction of the exact reference target at time \(s_k\) gives
\[
 A_{k+1}\le(1-p)A_k+p((M+1)E_k+b)+\eta V_x.
\]
The last term is the reference increment to \(s_{k+1}\), not a target perturbation multiplied by \(p\). The geometric sums satisfy
\[
 \sum_{r=0}^{m-1}p(1-p)^r\le1,\qquad
 \eta\sum_{r=0}^{m-1}(1-p)^r\le\varepsilon.
\]
They hold also at \(p=1\). Therefore
\[
 \max_{i\le k}A_i\le(M+1)D_k+b+\varepsilon V_x.
\]
The layer-two target difference is at most \(P_2A_k+cE_k+b\), by putting the hatted trained matrix on the activation difference and the reference activation on the matrix difference. The layer-three target difference is at most \(P_3B_k+cE_k+b\). Consequently
\[
\begin{aligned}
 \max_{i\le k}B_i
 &\le B_0+P_2\max_{i\le k}A_i+cD_k+b+\varepsilon V_2,\\
 \max_{i\le k}C_i
 &\le C_0+P_3\max_{i\le k}B_i+cD_k+b+\varepsilon V_3.
\end{aligned}
\]
Successive substitution proves
\[
 \max_{i\le k}(A_i+B_i+C_i)
 \le K_{S,M}(D_k+b+\varepsilon+d_0)
\]
with no \(R\) dependence and no instantaneous circular absorption. Initial warmup errors enter directly, without a factor \(1/\varepsilon\).

The top backward difference satisfies
\[
 \frac{\|\widehat\delta_k^{(3)}-\delta^{(3)}(s_k)\|_2}{\sqrt n}
 \le\frac{\|\widehat W_k^{(4)}-W^{(4)}(s_k)\|_2}{\sqrt n}
      +2UC_k.
\]
Using \(P_3\), the Frobenius matrix difference, and the reverse query error yields
\[
 \frac{\|\widehat q_k^{(2)}-q^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b.
\]
The exact fixed-clipping subtraction then gives
\[
 \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b+2RB_k.
\]
The readout estimate uses its coordinate bound; the middle estimate uses the bound \(|\tau|\le R\). An ordinary Euclidean bound on the unclipped middle query would not justify the latter step.

For clarity, all five slow right-side differences are controlled as follows, with reference values evaluated at \(s_k\):
\[
\begin{aligned}
 &\frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}\|_2}{\sqrt n},\\
 &c\frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}\|_2}{\sqrt n}
       +Q A_k,\\
 &c\frac{\|\widehat\delta_k^{(3)}-\delta^{(3)}\|_2}{\sqrt n}
       +U B_k,\\
 &Q\|\widehat M_k^{(2)}-M^{(2)}\|_F
       +J_2\frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}\|_2}{\sqrt n},\\
 &C_k.
\end{aligned}
\]
Vector right sides are measured by their Euclidean norm divided by \(\sqrt n\), and matrix right sides by Frobenius norm. The returned-memory estimate includes both its matrix error and its backward-field error. Every coefficient is bounded independently of \(R\), except the single linear clipping factor already present in the middle backward difference.

Together with quadrature and the filter estimate, this proves
\[
 E_{k+1}\le E_k+\Lambda\eta(D_k+f),\qquad
 \Lambda=C_{S,M}(1+R),\qquad
 f=b+\varepsilon+d_0+\eta.
\]
Summing from zero and maximizing gives
\[
 D_k\le\Lambda T_0f+\Lambda\eta\sum_{i<k}D_i.
\]
Induction yields
\[
 D_k\le\Lambda T_0f(1+\Lambda\eta)^k
       \le\Lambda T_0f\,e^{\Lambda T_0}.
\]
Combining with the filter bound proves B(9), and more precisely
\[
 \max_{k\le N}(A_k+B_k+C_k+E_k)
 \le C_{S,M}(1+R)e^{C_{S,M}(1+R)}
                    (b+\varepsilon+d_0+\eta).
\]
This verifies C's quantitative extraction. There is no exponential in \(1/\varepsilon\), and the clipping dependence inside the exponential is linear. Both conclusions follow from the actual simultaneous dynamics and exact reference quadrature, not from an assumed residual along a supplied trajectory.

## 7. Growing-clipping composition, warmup, and rate

Set \(E_n(S)=\max_{0\le k\le N}(A_k+B_k+C_k+E_k)\), exactly the distance in C and B(9).

For each prescribed deterministic \(\tau_n\), let \(\mathcal E_n^{\tau_n}\) be the event constructed in A. Its constants and failure allowance are uniform over admissible prescribed maps; the event itself may depend on the map. No simultaneous event over all maps, and no random selection of a map after seeing the arrays, is asserted.

On that event the initialization bounds give \(M=8\) for B. Every raw query error has Euclidean norm divided by \(\sqrt n\) at most
\[
 B_n=C_Sn^{-1/24}\ell_n^{8/3}+C_Sn^{-1/4}.
\]
B(6) bounds a sum of the two orientations for each layer. The correct choice is therefore
\[
 b=2B_n.
\]
This factor is present in C and is absorbed only subsequently into a constant.

The direct-noise warmup gives, relative to the exact canonical initial fields,
\[
 \frac{\|\widehat z_0^{(2)}-z_0^{(2)}\|_2}{\sqrt n}
 \le\sigma D_n,\qquad
 \frac{\|\widehat z_0^{(3)}-z_0^{(3)}\|_2}{\sqrt n}
 \le(8+1)\sigma D_n.
\]
Thus \(d_0\le10\sigma D_n\le C_Sn^{-1/4}\). These estimates compare the same original seeds and readout; no zero-readout evolved trajectory or exact-forward algorithm initialization is substituted.

Eventually \(b\le1\) and \(d_0\le1\). Also
\[
 \eta=n^{-2}\le\varepsilon=n^{-1/8}\le1,\qquad
 N\eta\le S+1.
\]
With B's harmless enlargement of the horizon parameter for \(0<S<1\), all of its hypotheses hold on the same event. No further probabilistic conditioning or failure allowance is needed.

For C's deterministic bound \(R_n\ge1\) and common map satisfying
\[
 |\tau_n(v)|\le\min\{|v|,R_n\},\qquad
 |\tau_n(v)-\tau_n(w)|\le|v-w|,
\]
the preceding comparison yields
\[
 E_n(S)
 \le C_S(1+R_n)e^{C_S(1+R_n)}
       n^{-1/24}\ell_n^{8/3}
\]
for all sufficiently large widths. All remaining terms, namely \(\varepsilon,\eta,d_0\) and the \(n^{-1/4}\) query contribution, are bounded by a constant times \(n^{-1/24}\ell_n^{8/3}\).

To make the last rate explicit, take \(C_S\ge1\) large enough in this inequality and define
\[
 d_n(S)=
 \frac{\log C_S+\log(1+R_n)+C_S(1+R_n)
                    +(8/3)\log\ell_n}{\log n}.
\]
This is nonnegative and deterministic for the prescribed sequence \(R_n\). The assumption \(R_n=o(\log n)\) gives \(d_n(S)\to0\), and the displayed comparison is exactly
\[
 E_n(S)\le n^{-1/24+d_n(S)}.
\]
The same event has probability at least
\[
 1-4e^{-(8-2\log9)n}-2ne^{-n^2/2}-5n^{-2}
\]
after ignoring finitely many widths. The upper bound on \(E_n(S)\) tends to zero, so the error tends to zero in probability. This proves C's three stated conclusions: the quantitative diagonal rate, its event probability, and convergence in probability.

The sequence \(d_n(S)\) can depend on the prescribed clipping-bound sequence. No universal rate sequence over all possible \(o(\log n)\) choices is needed or claimed.

## 8. Reconstruction of fields and audit of excluded inferences

B's constraint-discrepancy claim follows from the same target subtraction. Define the fully reconstructed fields
\[
 \widetilde z_k^{(2)}
 =(W_0^{(2)}+\widehat M_k^{(2)})
        \phi(F^{-1}(\widehat x_k^{(1)})),\qquad
 \widetilde z_k^{(3)}
 =(W_0^{(3)}+\widehat M_k^{(3)})\phi(\widetilde z_k^{(2)}).
\]
Then
\[
 \frac{\|\widehat z_k^{(2)}-\widetilde z_k^{(2)}\|_2}{\sqrt n}
 \le B_k+P_2A_k+c\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_F,
\]
and
\[
\begin{aligned}
 \frac{\|\widehat z_k^{(3)}-\widetilde z_k^{(3)}\|_2}{\sqrt n}
 \le{}&C_k+P_3B_k+c\|\widehat M_k^{(3)}-M^{(3)}(s_k)\|_F\\
 &+P_3\frac{\|\widehat z_k^{(2)}-\widetilde z_k^{(2)}\|_2}{\sqrt n}.
\end{aligned}
\]
Their vanishing is a consequence of the state comparison. These constraints are not imposed during the auxiliary recursion.

The following boundaries are respected throughout the three notes:

1. A proves ranks for its own filtered, perturbed histories, including when its prescribed map is identity. It does not prove ranks for the original unfiltered process. B and C compare states and do not supply that missing rank statement.
2. C compares two processes with the same width-dependent map \(\tau_n\). A growing upper bound \(R_n\) alone neither makes these maps converge to identity nor controls the mass of backward queries above the cutoff. The theorem consequently does not remove clipping.
3. Without bounded clipping, the middle difference retains
   \[
    [\phi'(\widehat z^{(2)})-\phi'(z^{(2)})]\odot q^{(2)}.
   \]
   For the purely algebraic choice \(q^{(2)}=\sqrt n\,e_1\), \(z^{(2)}=0\), and \(\widehat z^{(2)}=e_1\), the Euclidean query norm divided by \(\sqrt n\) equals one and the preactivation difference divided by \(\sqrt n\) equals \(1/\sqrt n\), but
   \[
    \frac{\|[\phi'(\widehat z^{(2)})-\phi'(z^{(2)})]
                      \odot q^{(2)}\|_2}{\sqrt n}=\frac12.
   \]
   Thus the available query bound supplies no width-independent multiplier estimate. This checks the logical caveat, not a dynamical counterexample.
4. The mesh is in feature time. The physical clock, possible clock degeneracy, and canonical raw-GD discretization are not justified by these results. In particular \(F(z+v)-F(z)=(1+z^2)v+zv^2+v^3/3\), so a transformed feature-time Euler update is not silently an exact raw-GD step.
5. Register derivative errors can involve \(1/\varepsilon\). The state estimate does not prove their convergence. The integrated dependency's identity
   \[
    (W^{(2)})^T\delta^{(2)}
     =\frac d{ds}[(W_0^{(2)})^Ta^{(2)}]
             +(M^{(2)})^T(a^{(2)})'
   \]
   retains the separate derivative issue. No population state-space construction, common limiting law, uncut uniqueness, autonomous restart, or required kernel/velocity theorem is inferred.

The coarse first-pass bounds, actual-history rank event, refined query estimates, initialized deterministic comparison, and growing-clipping rate therefore form a complete chain for exactly the stated auxiliary-to-clipped finite-width claim.

## Required fixes

None. A, final B at hash cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b, C, and their stated composition withstand the complete reconstruction above.

## Optional presentation suggestions

1. Use different symbols in the candidates for A's effective-rank ceiling and C's clipping bound; both currently use \(R_n\). The distinction is mathematically clear in context, and this report uses \(r_n\) and \(R_n\).
2. C could display the explicit formula for \(d_n(S)\) above, making its dependence on the prescribed clipping-bound sequence immediately visible.
