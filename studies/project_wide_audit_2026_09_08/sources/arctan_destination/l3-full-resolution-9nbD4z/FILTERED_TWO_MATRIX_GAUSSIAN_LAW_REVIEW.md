# Isolated hostile audit: filtered two-matrix Gaussian law

Verdict: **PASS for the stated scoped chain.** No required mathematical fix was found. The exact finite adaptive transcript law, the replacement realization's stated conditional innovation, and the bounded-Lipschitz comparison of the canonical clipped mesh state augmented by the middle query are justified. This certifies neither the full theorem nor any uncut, population, physical-time, or exact-GD conclusion.

## Audit boundary and frozen inputs

I first read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely. I read all 511 lines of the candidate and all lines of its three named dependencies. The latter were accepted as proved dependencies, as instructed; their statements, recurrences, and application hypotheses were checked. I did not inspect their further source files, any other candidate, any prior review or ledger, or any external source. No experiment, subagent, or source operation was used. Only this review was written, using `apply_patch`.

All four SHA-256 digests matched the supplied values before the audit:

| File in this directory | SHA-256 |
|---|---|
| `FILTERED_TWO_MATRIX_GAUSSIAN_LAW.md` | `db98d04b7f92c8d341ab0e0f54defd845e37750decc0b8c62e33f1b278aecb33` |
| `CAUSAL_FILTERED_QUERY_RANK.md` | `7406ffb9c24e8359e7e188c70eb3863ff5aeb9179df3d7bba92103b98aedcfd1` |
| `FILTERED_QUERY_CLIPPED_STABILITY.md` | `cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b` |
| `FILTERED_QUERY_GROWING_CLIP_TRANSFER.md` | `c1d5d50c8720cb3285c3aa15608b08cb9b0bfde968951c33cbe0338df1548fcd` |

Line references below refer to these frozen files. Panahi v1 equations (8)--(9) are motivation only. No Gaussian comparison or continuation theorem from that source is used in this review or required by the candidate's new proof.

## 1. Declared recursion, scales, and causal access

Candidate lines 24--111 agree with rank-note lines 129--200. For each hidden matrix label \(b=2,3\), the raw arguments are \(v_l^{(b)},h_l^{(b),\mathrm{query}}\in\mathbb R^n\), with
\[
\theta_l^{(b)}=v_l^{(b)}/\sqrt n,\qquad
\omega_l^{(b)}=h_l^{(b),\mathrm{query}},\qquad
G_0^{(b)}=\sqrt n\,W_0^{(b)}.
\]
Consequently \(G_0^T\theta_l=W_0^Tv_l\) and \(G_0\omega_l/\sqrt n=W_0h_l^{\mathrm{query}}\). Both candidate outputs are raw \(n\)-vectors. The forward output has not inadvertently been divided by another \(\sqrt n\). The Gamma terms in candidate (4) equal \(\sqrt n\,k_l\) and \(\sqrt n\,g_l\) in the rank note, respectively; each direct noise has coordinate variance \(\sigma^2\).

For either label, write the upper Cholesky factor at a larger prefix as
\[
A_{l+1}=\begin{pmatrix}A_l&c\\0&a\end{pmatrix},\qquad
A_{l+1}^{-1}=\begin{pmatrix}A_l^{-1}&-A_l^{-1}c/a\\0&1/a\end{pmatrix}.
\]
Thus the first \(l\) columns of the inverse have zero appended coordinate, and the columns \(t_i,s_i\) in candidate (2) are permanent. Positive regularization makes every diagonal and inverse finite, even with repeated or zero queries or \(K>n\). Moreover,
\[
\sum_{i\le l}t_it_i^T
=\Theta_l(\Theta_l^T\Theta_l+\sigma^2I)^{-1}\Theta_l^T\preceq I,
\]
and the identical calculation with \(\Omega_l/\sqrt n\) gives the bound for \(\sum s_is_i^T\). The eigenvalues along singular directions are \(d^2/(d^2+\sigma^2)\). These facts justify candidate lines 34--55, including all prefixes.

The exact network query maps matter. With \(\phi(z)=\arctan z\), \(F(z)=z+z^3/3\), and \(\psi=\phi\circ F^{-1}\), they are
\[
h_j^{(1)}=\psi(x_j^{(1)}),\quad
h_j^{(2)}=\phi(z_j^{(2)}),\quad
h_j^{(3)}=\phi(z_j^{(3)}),\quad
\delta_j^{(3)}=W_j^{(4)}\odot\phi'(z_j^{(3)}).
\]
At update \(j=0,\ldots,N-1\), the call index is \(l=j+2\), and
\[
(\theta_l^{(2)},\omega_l^{(2)})=(a_j^{(2)}/\sqrt n,h_j^{(1)}),\qquad
(\theta_l^{(3)},\omega_l^{(3)})=(\delta_j^{(3)}/\sqrt n,h_j^{(2)}).
\]
All four arguments are chosen before either current pair. The current upper reverse output then defines
\[
q_j^{(2)}=\mathcal R_{j+2}^{(3)}+(M_j^{(3)})^T\delta_j^{(3)},\qquad
\delta_j^{(2)}=\phi'(z_j^{(2)})\odot\tau(q_j^{(2)}).
\]
The slow updates, all using the displayed pre-step factors, are
\[
\begin{aligned}
a_{j+1}^{(2)}&=a_j^{(2)}+\eta\delta_j^{(2)},\\
M_{j+1}^{(2)}&=M_j^{(2)}+\eta\delta_j^{(2)}(h_j^{(1)})^T/n,\\
M_{j+1}^{(3)}&=M_j^{(3)}+\eta\delta_j^{(3)}(h_j^{(2)})^T/n,\\
R_{j+1}^{(1)}&=R_j^{(1)}+\eta(M_j^{(2)})^T\delta_j^{(2)},\\
W_{j+1}^{(4)}&=W_j^{(4)}+\eta h_j^{(3)}.
\end{aligned}
\]
The other three updates relax \(x^{(1)},z^{(2)},z^{(3)}\), with coefficient \(\eta/\varepsilon\), toward, respectively,
\[
x_0^{(1)}+\mathcal R_{j+2}^{(2)}+R_j^{(1)},\qquad
\mathcal F_{j+2}^{(2)}+M_j^{(2)}h_j^{(1)},\qquad
\mathcal F_{j+2}^{(3)}+M_j^{(3)}h_j^{(2)}.
\]
This is precisely rank-note (19)--(22) and stability-note (5)--(7). In particular,
\[
R_j^{(1)}=\frac{\eta^2}{n}\sum_{0\le u<r<j}
h_u^{(1)}(\delta_u^{(2)})^T\delta_r^{(2)}.
\]
The strict time triangle is preserved; \(M_{j+1}^{(2)}\) is never substituted for \(M_j^{(2)}\) in the returned-memory update.

Warmups also match exactly. Lower call 1 uses \(v_1^{(2)}=0\) and \(h_0^{(1)}\); upper call 1 uses \(v_1^{(3)}=0\) and \(\phi(z_0^{(2)})\), after the lower forward output. Here \(t_1=0\), so both Gamma corrections vanish, but forward direct noise remains:
\[
z_0^{(2)}=W_0^{(2)}h_0^{(1)}+\sigma V_1^{(2)},\qquad
z_0^{(3)}=W_0^{(3)}\phi(z_0^{(2)})+\sigma V_1^{(3)}.
\]
Discarding the warmup reverse outputs from the state does not delete them from the observed transcript. In the replacement rule the same warmup outputs are \(\sigma Z_1^{\mathrm{rev}}\) and \(A_{\omega,11}Z_1^{\mathrm{for}}\), since \(t_1=0\). Thus no zero-noise or exact canonical warmup is being substituted.

Every state is a finite measurable function of the declared outputs and the independent seeds \(z_0^{(1)},W_0^{(4)}\). No state update separately evaluates an original hidden matrix. The larger filtration used inside the proved rank estimate is not being imported as observed data for the exact-law argument.

## 2. Frozen covariance: all blocks and all endpoints

This calculation is made at deterministic query vectors, not under conditioning on an adaptive history. Suppress the hidden-matrix label only in this section. All outputs are centered linear functions of finitely many independent Gaussian entries, so equality of their covariance matrices suffices for their frozen joint laws.

Upper triangularity gives
\[
\sum_{i\le\min(l,k)}A_{\theta,il}A_{\theta,ik}
=\theta_l^T\theta_k+\sigma^2\mathbf1_{\{l=k\}}
=V_\theta(l,k),
\]
and the forward identity has \(\omega_l^T\omega_k/n\), giving \(V_\omega(l,k)\).

Expanding the original Gamma terms gives the forward coefficients
\(
t_i\Gamma_{ij}A_{\omega,jl},\ i,j\le l
\)
and the reverse coefficients
\(
s_p\Gamma_{qp}A_{\theta,qk},\ p<k,\ q\le k.
\)
For two forward outputs, equality of both Gamma indices yields
\[
\sum_{i\le\min(l,k)}t_it_i^T
\sum_{j\le\min(l,k)}A_{\omega,jl}A_{\omega,jk}
=T_{\min(l,k)}V_\omega(l,k).
\]
The \(G_0\) and direct-noise contribution is \(V_\omega(l,k)I\). For two reverse outputs, the outer sum is \(p<\min(l,k)\), while the factor sum is \(q\le\min(l,k)\). The result is \(V_\theta(l,k)(I+S_{\min(l,k)-1})\). Thus candidate (7)--(8) have the correct distinct endpoints.

For the cross block, the \(G_0\) term is \(\theta_k\omega_l^T/\sqrt n\). Matching \(\Gamma_{ij}=\Gamma_{qp}\) imposes
\[
i=q\le\min(l,k),\qquad j=p\le\min(l,k-1).
\]
Therefore, with the candidate's definitions
\[
a_{l,k}=\sum_{i\le\min(l,k)}t_iA_{\theta,ik},\qquad
b_{l,k}=\sum_{j\le\min(l,k-1)}s_jA_{\omega,jl},
\]
the original cross covariance is exactly
\[
\operatorname{Cov}(\mathcal F_l,\mathcal R_k)
=\theta_k\omega_l^T/\sqrt n+a_{l,k}b_{l,k}^T.
\]

In the replacement rule, the forward-forward contributions from \(Z^{\mathrm{for}},Z^{\mathrm{rev}},\Lambda\) are, respectively,
\[
V_\omega(l,k)I,\qquad
(\omega_l^T\omega_k/n)T_{\min(l,k)},\qquad
\sigma^2\mathbf1_{\{l=k\}}T_l.
\]
Their sum is the same forward-forward block. The reverse-reverse contributions are
\[
V_\theta(l,k)I,\qquad
(\theta_l^T\theta_k)S_{\min(l,k)-1},\qquad
\sigma^2\mathbf1_{\{l=k\}}S_{l-1},
\]
which sum to the same reverse-reverse block.

The \(Z^{\mathrm{for}}\) cross term is \(\theta_k b_{l,k}^T\); the \(Z^{\mathrm{rev}}\) cross term is \(a_{l,k}\omega_l^T/\sqrt n\). A Lambda cross term would need \(\Lambda_{il}=\Lambda_{kj}\), hence \(i=k\le l=j<k\), which is impossible. There are no other cross terms because the three arrays are independent.

Subtracting the replacement cross block from the original gives
\[
(\theta_k-a_{l,k})(\omega_l/\sqrt n-b_{l,k})^T.
\]
If \(l<k\), permanence and \(\Omega A_\omega^{-1}A_\omega=\Omega\) give \(b_{l,k}=\omega_l/\sqrt n\). If \(l\ge k\), \(\Theta A_\theta^{-1}A_\theta=\Theta\) gives \(a_{l,k}=\theta_k\). The difference vanishes in every case, including \(l=k\). Empty sums at call 1 present no exception.

At a frozen history the original direct-noise blocks occur once each with coefficient \(\sigma I_n\) and are independent of all \(G_0,\Gamma\) terms. Thus the full covariance dominates \(\sigma^2I_{2nK}\), and every principal prefix is positive definite. This reasoning does not claim that the adaptive output vector has an unconditional Gaussian law.

## 3. Why the adaptive-law step is valid

Candidate lines 208--267 contain the necessary argument; frozen covariance equality alone is not being substituted for a proof about adaptive observations. Here is its posterior reconstruction, including the singular residual covariance that arises after the first observation.

Let the primitive vector be \(g\sim N(0,I_d)\), and let \(y_j=L_j(y_{<j})g\). At a prescribed prefix, put \(H=L_{<j}(y)\), \(K=HH^T\), and
\[
\mu=H^TK^{-1}y_{<j},\qquad P=I-H^TK^{-1}H.
\]
Inductively the conditional law of \(g\) given the past is \(N(\mu,P)\). The first instance follows by the orthogonal decomposition in the candidate. Although \(P\) is generally singular, a linear image of this conditional Gaussian still has a well-defined Gaussian law.

With \(B=L_j(y_{<j})\), the next mean and covariance are
\[
B\mu=K_{j,<j}K_{<j,<j}^{-1}y_{<j},\qquad
Q=BPB^T=K_{j,j}-K_{j,<j}K_{<j,<j}^{-1}K_{<j,j}.
\]
The assumed positive definiteness of the stacked covariance makes \(Q\) positive definite. For a centered Gaussian residual \(r\) of covariance \(P\), the two vectors
\[
Br,\qquad r-PB^TQ^{-1}Br
\]
have zero cross covariance and therefore are independent: their joint Gaussian characteristic function factors, even if the second covariance is singular. The posterior after the next observation is consequently
\[
\mu+PB^TQ^{-1}(y_j-B\mu),\qquad
P-PB^TQ^{-1}BP.
\]
The block inverse of the covariance of the rows \([H;B]\) identifies these expressions with
\[
L_{\le j}^TK_{\le j}^{-1}y_{\le j},\qquad
I-L_{\le j}^TK_{\le j}^{-1}L_{\le j}.
\]
This closes the induction and proves candidate (12), without any independence assertion about the primitive vector after earlier observations.

For completeness, the resulting next-output density at a prescribed prefix is
\[
\frac{\exp[-(y_j-B\mu)^TQ^{-1}(y_j-B\mu)/2]}
{(2\pi)^{\dim(y_j)/2}\det(Q)^{1/2}}.
\]
It is measurable in the past, is positive, and integrates to one in \(y_j\). Thus these expressions define conditional kernels; their values at null histories can be chosen by the same formulas. Sequential conditioning establishes that they are versions of the actual kernels. No differentiability of the query maps, Jacobian formula for an adaptive map, or external comparison theorem is needed.

Two systems with identical frozen prefix covariance matrices have identical first kernels and identical subsequent kernels by these formulas. Iterated integration proves equality of the whole transcript law. Independent external seeds can be fixed first and then integrated out; they survive jointly in the equality. This does not permit fixing the original hidden matrices as external seeds, because those matrices are components of the Gaussian primitive being observed.

## 4. Combined chronology and the variables preserved by the law

Use one Gaussian primitive vector containing both matrices' arrays. Conditional on fixed \(z_0^{(1)},W_0^{(4)}\), order the output blocks as lower warmup reverse/forward, upper warmup reverse/forward, and then lower reverse/forward followed by upper reverse/forward at each update.

For a fixed candidate transcript all query coefficients in this ordering are functions of earlier output blocks. Upper warmup uses the earlier lower output. Later calls use the pre-step state. An upper argument cannot depend on its own fresh output through the current lower pair, since both upper arguments were selected before that pair. The more general single-matrix allowance that a forward query may depend on its current reverse output is also compatible with this sequential ordering.

Frozen blocks belonging to different matrices have zero covariance because their Gaussian primitives are independent. Within either matrix the calculations above apply, even if its queries were chosen using the other matrix's earlier outputs. Interactions alter coefficient functions, not the frozen independence of the primitive coordinates.

Every chronological prefix is covered, including one ending after a reverse output. Such an output needs \(\theta_l\), earlier \(s_i,Z_i^{\mathrm{for}}\) with \(i<l\), and no current \(\omega_l\). Hence a completion by arbitrary finite later outputs and queries leaves all already included rows unchanged. Prefix covariance equality follows from the full frozen calculation. For both matrices combined, the original covariance dominates \(\sigma^2I_{4nK}\), and the corresponding prefix bounds follow as well.

The sequential lemma therefore proves candidate lines 311--326 for every finite number of calls (one warmup plus the declared updates). Growth of \(K\) with \(n\) causes no problem for an exact finite statement. Finiteness of each recursion follows from finite arithmetic, measurable finite query maps, and regularized Cholesky factors. The identity map is allowed here; the exact law uses none of the clipped stability constants.

The preserved variables are the declared outputs and their measurable functions, jointly with \(z_0^{(1)},W_0^{(4)}\). They include \(M^{(2)},M^{(3)},R^{(1)}\), the state registers, activations, and \(q^{(2)},\delta^{(2)},\delta^{(3)}\). The learned matrices in this statement mean the increments \(M^{(2)},M^{(3)}\). The original \(W_0^{(2)},W_0^{(3)}\), and therefore full matrices \(W_0^{(b)}+M^{(b)}\) as observed coordinates, are not carried into the replacement law. Candidate lines 109--111 and 315--320 explicitly respect this restriction.

## 5. Actual upper-reverse innovation and learned-memory bound

Work solely in the all-replacement construction. A precise past for upper reverse call \(l=j+2\) is generated by the two non-matrix seeds, upper \(Z_i^{\mathrm{rev}},Z_i^{\mathrm{for}}\) for \(i<l\) and upper \(\Lambda_{ab}\) for \(a,b<l\), together with lower primitives through its completed current pair \(l\). Every earlier state and the current lower pair are measurable with respect to this past.

The reverse reveal at upper call \(k\) uses \(Z_k^{\mathrm{rev}}\) and \(\Lambda_{ki},i<k\). The forward reveal uses \(Z_k^{\mathrm{for}}\) and \(\Lambda_{ik},i\le k\). These two triangles are disjoint and together exhaust each completed square. Earlier upper calls have revealed neither \(Z_l^{\mathrm{rev}}\) nor \(\Lambda_{li},i<l\). Current lower computations use upper variables only through earlier upper outputs; their own new primitives are independent of the entire upper primitive collection. Therefore the specified fresh upper variables remain mutually independent standard Gaussians independent of this past. No future upper variable has entered it indirectly.

Both \(\theta_l^{(3)}=\delta_j^{(3)}/\sqrt n\) and the necessary Cholesky coefficients are past-measurable. Splitting the replacement reverse formula gives exactly
\[
\begin{aligned}
m_l^{(2)}&=\sum_{i<l}Z_i^{\mathrm{rev},(3)}A_{\theta,il}^{(3)}
+\sum_{i<l}s_i^{(3)}(Z_i^{\mathrm{for},(3)})^T\theta_l^{(3)},\\
\nu_l^{(2)}&=A_{\theta,ll}^{(3)}Z_l^{\mathrm{rev},(3)}
+\sigma\sum_{i<l}s_i^{(3)}\Lambda_{li}^{(3)}.
\end{aligned}
\]
Thus \(m_l^{(2)}\) is predictable for this enlarged primitive past, and
\[
\operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
=(A_{\theta,ll}^{(3)})^2I_n
+\sigma^2\sum_{i<l}s_i^{(3)}(s_i^{(3)})^T.
\]
The extra sum is an actual conditional covariance contribution. It cannot be dropped or replaced by a diagonal matrix. There are no cross terms because the newly exposed primitive entries are independent. This proves candidate (13)--(15), including
\[
q_j^{(2)}=m_{j+2}^{(2)}+(M_j^{(3)})^T\delta_j^{(3)}+\nu_{j+2}^{(2)}.
\]
In particular, conditional on this past, the complete query is Gaussian with the displayed possibly unbounded mean plus learned memory. It is not asserted to be centered or unconditionally Gaussian. This particular covariance is not automatically the conditional covariance given only the smaller observed-output past.

Let \(E_4=\{\|W_0^{(4)}\|_\infty\le1\}\). It is measurable already in the non-matrix seeds. Since
\[
W_j^{(4)}=W_0^{(4)}+\eta\sum_{r<j}\phi(z_r^{(3)}),\qquad
\delta_j^{(3)}=W_j^{(4)}\odot\phi'(z_j^{(3)}),
\]
and \(|\phi|\le\pi/2\), \(0<\phi'\le1\), on \(E_4\) and \(N\eta\le S+1\),
\[
\|W_j^{(4)}\|_\infty\le B_4=1+(S+1)\pi/2,\qquad
\|\delta_j^{(3)}\|_2/\sqrt n\le B_4.
\]
No clipping or query-error bound is needed for these inequalities. The Cholesky squared diagonal is its diagonal Gram entry minus a nonnegative Schur term, so
\[
(A_{\theta,ll}^{(3)})^2\le\|\theta_l^{(3)}\|_2^2+\sigma^2
\le B_4^2+\sigma^2.
\]
Together with \(\sum_{i<l}s_i^{(3)}(s_i^{(3)})^T\preceq I\), this proves candidate (17).

For each coordinate, its conditional moment generating function is that of a centered scalar Gaussian whose variance is at most \(B_4^2+2\sigma^2\). Completing the square gives candidate (18). For \(x\ge0\), exponential Markov bounds with parameters \(x/(B_4^2+2\sigma^2)\) and its negative give candidate (19). These statements hold at each eligible past on \(E_4\). Since \(W_{0,i}^{(4)}\sim N(0,n^{-2})\), the scalar Gaussian tail and a union bound give \(\mathbb P(E_4^c)\le2ne^{-n^2/2}\).

The learned term is also correct coordinatewise, with the exact \(1/n\) scale:
\[
(M_j^{(3)})^T\delta_j^{(3)}
=\eta\sum_{r<j}h_r^{(2)}\frac{(\delta_r^{(3)})^T\delta_j^{(3)}}{n}.
\]
Cauchy--Schwarz bounds the absolute scalar product divided by \(n\) by \(B_4^2\), and every coordinate of \(h_r^{(2)}=\phi(z_r^{(2)})\) is at most \(\pi/2\) in absolute value. Hence the coordinate bound is \((S+1)(\pi/2)B_4^2\), as in (20). All learned increments are present.

The constants are uniform over eligible calls for bounded \(\sigma\) and a fixed feature horizon, but a single-call tail is not a constant-threshold all-call probability bound. For example, union bounding over \(N\) update calls and \(n\) coordinates produces the factor \(2nN\) in front of the Gaussian exponential, in addition to the failure probability of \(E_4\). Nor is the innovation generally independent of the past as a vector: its conditional covariance is random. Most importantly, none of these estimates bounds the predictable \(m_l^{(2)}\) sufficiently to supply a clipping-uniform tail for the complete middle query.

## 6. Application of the three proved dependencies

For each width the same prescribed deterministic map must be used in the reference, all-original recursion, and all-replacement recursion. Its hypotheses are
\[
|\tau_n(u)|\le\min(|u|,R_n),\quad
|\tau_n(u)-\tau_n(v)|\le|u-v|,\quad
R_n\ge1,\quad R_n=o(\log n).
\]
A cap alone would not suffice; these domination and Lipschitz conditions are supplied by the candidate's explicit adoption of the three notes' parameters and allowed maps. No event uniform over all maps is being asserted.

The rank theorem, equations (4)--(6), supplies for this map an event with complement probability at most
\[
p_n=4e^{-(8-2\log9)n}+2ne^{-n^2/2}+5n^{-2}.
\]
On that same event both initial hidden operator norms are at most 8, the readout satisfies \(E_4\), and each raw query error obeys
\[
\|e_l\|_2/\sqrt n\le
B_n=C_Sn^{-1/24}\log(e+n)^{8/3}+C_Sn^{-1/4}.
\]
This controls errors on the actual perturbed queries, which are precisely the queries required by stability-note (5). No unperturbed query history has been substituted. Stability-note (6) bounds a sum of reverse and forward error sizes, so its input is \(b=2B_n\), eventually at most 1. The growing-cap note explicitly uses this factor of two.

The direct-noise event and the noisy warmup identities give the sum of the two initial preactivation errors divided by \(\sqrt n\) at most \(10\sigma D_n\le C_Sn^{-1/4}\), where \(D_n\le C_S\) is the rank note's direct-noise bound. Thus the stability parameter \(d_0\le1\) eventually. The bottom seed and readout are identical across this coupling; no bound on individual coordinates of the bottom seed is needed.

The remaining inputs are exactly
\[
\eta=n^{-2},\quad \varepsilon=n^{-1/8},\quad
\sigma=n^{-1/4},\quad N=\lceil Sn^2\rceil,\quad K=N+1,
\]
with \(0<\eta\le\varepsilon\le1\) and \(N\eta\le S+1\). For \(0<S<1\), use \(\max(1,S)\) in the stability theorem. All its hypotheses then hold with \(M=8\) on the same event, after discarding finitely many widths as the growing-cap note permits.

The reference is the canonical clipped feature flow, with its exact canonical initial fields and tiny Gaussian readout, satisfying
\[
\begin{aligned}
z^{(2)}&=W^{(2)}h^{(1)},&z^{(3)}&=W^{(3)}h^{(2)},\\
\delta^{(3)}&=W^{(4)}\odot\phi'(z^{(3)}),&
q^{(2)}&=(W^{(3)})^T\delta^{(3)},\\
\delta^{(2)}&=\phi'(z^{(2)})\odot\tau_n(q^{(2)}),&
(z^{(1)})'&=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'&=\delta^{(2)}(h^{(1)})^T/n,&
(W^{(3)})'&=\delta^{(3)}(h^{(2)})^T/n,\\
(W^{(4)})'&=h^{(3)}.
\end{aligned}
\]
Here primes on the trajectory denote feature-time derivatives, whereas \(\phi'\) is the activation derivative. With \(x^{(1)}=F(z^{(1)})\), \(M^{(b)}=W^{(b)}-W_0^{(b)}\), and the stated integrated \(a^{(2)},R^{(1)}\), this is exactly the reference in the stability theorem.

The growing-cap note's quantitative estimate is
\[
E_n(S)\le C_S(1+R_n)e^{C_S(1+R_n)}
(b+\varepsilon+d_0+\eta).
\]
Here \(E_n(S)\) is precisely the maximum state distance in stability-note (9), not a new choice of vector norm. Each of \(b,\varepsilon,d_0,\eta\) is bounded by a constant times \(n^{-1/24}\log(e+n)^{8/3}\). Because \(R_n=o(\log n)\), the logarithm of the entire remaining prefactor divided by \(\log n\) tends to zero. This proves the deterministic good-event rate \(n^{-1/24+o(1)}\). A cap of order \(\log n\), without a further small-constant condition, would not follow from this argument; the candidate does not assert it.

## 7. Augmenting the mesh state by the ordinary middle query

Candidate (21) is exactly stability-note (19). To check its independence from the clipping cap, at mesh time \(s_j\) expand
\[
\widehat\delta_j^{(3)}-\delta^{(3)}(s_j)
=(\widehat W_j^{(4)}-W^{(4)}(s_j))\odot\phi'(\widehat z_j^{(3)})
+W^{(4)}(s_j)\odot[\phi'(\widehat z_j^{(3)})-\phi'(z^{(3)}(s_j))].
\]
Since \(\|\phi''\|_\infty\le2\), its Euclidean norm divided by \(\sqrt n\) is bounded by the readout error divided by \(\sqrt n\) plus \(2B_4\|\widehat z_j^{(3)}-z^{(3)}(s_j)\|_2/\sqrt n\). Also,
\[
\begin{aligned}
\widehat q_j^{(2)}-q^{(2)}(s_j)
={}&(W_0^{(3)}+\widehat M_j^{(3)})^T
(\widehat\delta_j^{(3)}-\delta^{(3)}(s_j))\\
&+(\widehat M_j^{(3)}-M^{(3)}(s_j))^T\delta^{(3)}(s_j)
+e_{T,j}^{(3)}.
\end{aligned}
\]
The operator norm of \(W_0^{(3)}+\widehat M_j^{(3)}\) is bounded independently of \(R_n\), because \(\|\widehat M_j^{(3)}\|_{\rm F}\le(S+1)(\pi/2)B_4\). The second product is bounded by the matrix Frobenius error times \(\|\delta^{(3)}(s_j)\|_2/\sqrt n\le B_4\). These facts prove candidate (21). The factor \(2R_n\) enters only in the subsequent difference of \(\phi'(z^{(2)})\odot\tau_n(q^{(2)})\), as the dependencies state.

Explicitly, the state distance between two mesh arrays is
\[
\begin{aligned}
d_{\mathrm{state},n}=\max_{0\le j\le N}\bigg\{&
\frac{\|\widehat x_j^{(1)}-x^{(1)}(s_j)\|_2+
\|\widehat z_j^{(2)}-z^{(2)}(s_j)\|_2+
\|\widehat z_j^{(3)}-z^{(3)}(s_j)\|_2}{\sqrt n}\\
&+\frac{\|\widehat a_j^{(2)}-a^{(2)}(s_j)\|_2+
\|\widehat R_j^{(1)}-R^{(1)}(s_j)\|_2+
\|\widehat W_j^{(4)}-W^{(4)}(s_j)\|_2}{\sqrt n}\\
&+\|\widehat M_j^{(2)}-M^{(2)}(s_j)\|_{\rm F}
+\|\widehat M_j^{(3)}-M^{(3)}(s_j)\|_{\rm F}\bigg\}.
\end{aligned}
\]
The augmented distance adds
\[
\max_{0\le j<N}\|\widehat q_j^{(2)}-q^{(2)}(s_j)\|_2/\sqrt n.
\]
The distinction between state indices \(j\le N\) and query indices \(j<N\) is correct: the final update produces state \(N\), but no query at state \(N\) is declared. The augmented distance is at most \((1+C_S)d_{\mathrm{state},n}+b\) on the good event, and therefore has the same \(n^{-1/24+o(1)}\) bound on the full growing mesh. If the two non-matrix seeds are retained as extra coordinates, any ordinary product metric contribution for them is zero on this coupling.

Let \(f_n\) be any deterministic measurable test with \(|f_n|\le1\) and Lipschitz constant at most 1 for this distance. Coupling the canonical clipped and all-original arrays gives
\[
|\mathbb E f_n(\text{canonical clipped})-\mathbb E f_n(\text{all original})|
\le n^{-1/24+o(1)}+2p_n.
\]
On the good event this follows from the distance bound; on its complement it follows from \(|f_n|\le1\). The exact transcript law then replaces only the second expectation by the all-replacement expectation. There is no attempt to transfer the original event, the original matrices as observed coordinates, or a conditional Gaussian law through this equality. This proves candidate (22) with exactly its probability allowance. No integrability or limit exchange is required.

## 8. Findings and limits of certification

Required mathematical fixes: **none** for the stated scoped chain.

Two non-blocking wording clarifications would make the boundaries more explicit. State \(x\ge0\) next to candidate (19), the conventional domain of the tail parameter. In candidate lines 429--432, qualify the absence of a Gaussian law for the complete query as an absence of an *unconditional* Gaussian-law conclusion; given the explicitly enlarged past, (15) is already Gaussian with its displayed mean and covariance. Neither clarification changes a proof step or the verdict.

The critical attacks resolve as follows:

| Attack | Audit result |
|---|---|
| Frozen covariance versus adaptive law | Pass: the measurable sequential posterior induction supplies the missing logical bridge explicitly. |
| Prefixes, endpoints, and width factors | Pass: strict reverse/inclusive forward sums, half-pair prefixes, \(l=j+2\), and raw output scales all match. |
| Two interacting matrices and noisy warmups | Pass: the combined output chronology gives predictable coefficients; warmup forward noise remains present. |
| Preservation of original hidden matrices | Excluded correctly; only transcript-computable increments and states, plus independent non-matrix seeds, survive jointly. |
| Fresh upper innovation after current lower pair | Pass: the reveal triangles and pre-step queries leave the identified upper primitives independent of the specified past. |
| Actual innovation covariance and learned memory | Pass: the non-diagonal covariance term and all upper learned increments are included with the correct \(1/n\) factors. |
| Single-call versus all-call scope | Correctly separated: pointwise conditional tails have uniform constants, while full-mesh state/query comparison comes from the three dependencies. |
| Growing clipped augmented bounded-Lipschitz transfer | Pass for each prescribed admissible map and \(R_n=o(\log n)\), with the stated probability allowance. |

The exact law is an equality of finite-dimensional adaptive transcript distributions, not an unconditional Gaussianity claim. The innovation formulas belong to a specified replacement realization and filtration. The canonical conclusion is a bounded-Lipschitz comparison of two width-dependent clipped arrays on a fixed feature horizon, not convergence to an identified population process. It does not transfer arbitrary tail indicators or conditional laws to the canonical flow.

There is no bound here closing the predictable \(m_l^{(2)}\) term, no uncut clipping removal, no coordinate-independence conclusion, no limiting population existence or uniqueness, no autonomous restart, and no physical-clock, exact-GD, kernel, or velocity theorem. The full theorem remains open.
