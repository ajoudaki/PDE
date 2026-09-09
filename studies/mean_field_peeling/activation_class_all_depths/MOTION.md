# Part N. Nonzero initial motion and kernel variation at every depth

## Statement and scope

Let \(L\ge2\) be any fixed finite integer. Let \(u_i=x_i/\sqrt d\), \(i=1,2,3\), satisfy \(\|u_i\|=1\) and \(\Gamma_{ij}=\langle u_i,u_j\rangle\le1-\delta\) for \(i\ne j\), where \(\delta>0\). The requested absolute separation \(|\Gamma_{ij}|\le1-\delta\) is a special case. Let \(y_i\in\{-1,1\}\), \(p_i=y_i/3\), and

\[
\phi(z)=a(1+z)+e\psi(z),\qquad
\psi\in C^2(\mathbb R),\quad \psi\text{ bounded and nonconstant},\quad
\max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1.
\]

For the requested activation class assume \(a\ge4\) and \(0<e\le1\). In fact the proof below needs only

\[
                         0<e<a.                         \tag{N.1}
\]

For this initial-motion statement alone, any one fixed \(e\in(0,1]\) and any one fixed \(a\ge2\) work at every fixed finite depth. The full global theorem uses the larger gain selected in (M.4). Put \(\alpha=a-e>0\), \(B=a+e\). Then

\[
\alpha\le\phi'(z)\le B,\quad |\phi''(z)|\le e,
\quad |\phi(z)|\le a(1+|z|)+e.                          \tag{N.2}
\]

Use the canonical initialized Gaussian actions associated with independent first-layer entries \(N(0,1/d)\), independent higher-layer entries \(N(0,1/n)\), and population readout \(C(0)=0\). The actions and their transposes are the same initialized matrices in both orientations; their population extensions have genuine adjoints. All conclusions below concern these actions, not arbitrary bounded substitutions for them.

Every hidden raw block, every sample preactivation at every hidden layer, and every sample feature at every hidden layer has a nonzero initial acceleration along any canonical strong physical gradient flow from this initialization. More precisely, the accelerations are \(9V^\ell,9U_j^\ell,9T_j^\ell\), with the directions defined below. For the original raw metric and the sum of all true kernel blocks,

\[
p^TK_{\rm total}(t)p
=p^TK_{\rm total}(0)p+18t^2\|V\|_{\rm hidden}^2+o(t^2),
\qquad \|V\|_{\rm hidden}>0.                            \tag{N.3}
\]

The algebraic initialization statement is within the canonical Gaussian construction. Parts G and V have supplied the strong global physical solution needed for its interpretation as acceleration. It does prove the relevant chain rule from the stated strong regularity. No uniform positive numerical lower bound over \(L,e,\psi\) is claimed or needed.

The proof uses constant and linear Gaussian projections for forward positivity, fresh reverse sources for bottom motion, and fresh forward innovations for all upper samples. It never compares the nonlinear network with an affine network, and never needs a sign condition on \(\psi'\) or \(\psi''\).

## N.1. All forward Grams are positive definite

Write \(Z_i^1\) for the first Gaussian projection, with covariance \(\Gamma\), and recursively

\[
h_i^\ell=\phi(Z_i^\ell),\quad
Z_i^\ell=A_\ell h_i^{\ell-1}\ (\ell\ge2),\quad
D_i^\ell=\phi'(Z_i^\ell),\quad
Q_\ell=(E[h_i^\ell h_k^\ell])_{ik}.
\]

At initialization every \(Z^\ell\) is a centered Gaussian tuple. Its coordinates have the same marginal variance: this is true at layer 1 and propagates because the diagonal of the next covariance is \(E[\phi(Z_i^\ell)^2]\).

For any centered Gaussian tuple \(Z\) with equal marginal variance \(s^2>0\), define

\[
\mu_s=E\phi(sG)=a+eE\psi(sG),\qquad
b_s=E\phi'(sG)=a+eE\psi'(sG),
\]

where \(G\sim N(0,1)\). Integration by parts gives \(E[Z_i\phi(Z_i)]=s^2b_s\). The boundary term vanishes by linear growth and Gaussian decay. The Gaussian regression identity \(E[Z_k\mid Z_i]=\operatorname{Cov}(Z_k,Z_i)Z_i/s^2\) remains valid for singular tuples. Consequently

\[
r_i=\phi(Z_i)-\mu_s-b_sZ_i
\]

is orthogonal both to constants and to every coordinate \(Z_k\). Therefore the uncentered feature Gram is exactly

\[
Q=\mu_s^2\mathbf1\mathbf1^T+b_s^2\operatorname{Cov}(Z)
       +(E[r_ir_k])_{ik}.
\]

Since \(\mu_s,b_s\ge\alpha\), this proves

\[
Q_1\succeq\alpha^2(\Gamma+\mathbf1\mathbf1^T),\qquad
Q_\ell\succeq\alpha^2Q_{\ell-1}\quad(\ell\ge2).          \tag{N.4}
\]

Here is a direct quantitative proof that the augmented input Gram is positive, including singular \(\Gamma\). For \(c\in\mathbb R^3\),

\[
c^T(\Gamma+\mathbf1\mathbf1^T)c
=(\sum_i c_i)^2+\|\sum_i c_i u_i\|^2.
\]

When all nonzero coefficients have one sign, the first square is at least \(\|c\|^2\). Otherwise, after changing overall sign and permuting coordinates, write \(c=(r_1,r_2,-b)\) with \(r_1,r_2\ge0\), \(A=r_1+r_2>0\), \(b>0\). Put

\[
D=\{r_1(1-\Gamma_{13})+r_2(1-\Gamma_{23})\}/A\in[\delta,2].
\]

Projection onto \(u_3\) bounds the quadratic form below by

\[
(A-b)^2+((1-D)A-b)^2.
\]

The corresponding \(2\times2\) positive matrix has determinant \(D^2\) and trace \(D^2-2D+4\le4\), so its smaller eigenvalue is at least \(\delta^2/4\). Since \(A^2+b^2\ge\|c\|^2\),

\[
\Gamma+\mathbf1\mathbf1^T\succeq\delta^2I_3/4,
\qquad Q_\ell\succeq\alpha^{2\ell}\delta^2I_3/4>0.       \tag{N.5}
\]

Feasibility implies \(\delta\le2\), which also handles the one-sign case. Thus \(Z^\ell\) has full three-dimensional Gaussian support for every \(\ell\ge2\).

## N.2. Backward sources and every hidden block

Define

\[
H=\sum_i p_i h_i^L,\quad
\beta_i^L=D_i^LH,\quad
q_i^\ell=A_{\ell+1}^*\beta_i^{\ell+1},\quad
\beta_i^\ell=D_i^\ell q_i^\ell\ (\ell<L),\quad
S_\ell=(E[\beta_i^\ell\beta_k^\ell])_{ik}.
\]

The raw hidden directions and sample directions are

\[
V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\qquad
V^\ell=\sum_i p_i\beta_i^\ell\otimes h_i^{\ell-1}
\quad(2\le\ell\le L),                                  \tag{N.6}
\]

\[
U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1,\qquad
T_j^\ell=D_j^\ell U_j^\ell,\qquad
U_j^\ell=V^\ell h_j^{\ell-1}+A_\ell T_j^{\ell-1}
\quad(\ell\ge2).                                      \tag{N.7}
\]

All norms and products are in their own layer probability spaces. In particular

\[
\|V\|_{\rm hidden}^2=d\|V^1\|_2^2+
                         \sum_{\ell=2}^L\|V^\ell\|_{\rm HS}^2.
\]

First \(S_L\succ0\). If \(v^TS_Lv=0\), full support and continuity give

\[
\left[\sum_i p_i\phi(z_i)\right]
\left[\sum_i v_i\phi'(z_i)\right]=0
\quad\text{for every }z\in\mathbb R^3.
\]

The first factor has no open zero set, because its derivative in coordinate \(i\) is \(p_i\phi'(z_i)\ne0\). Thus its nonzero set is dense, and the second factor vanishes identically by continuity. Differentiating in coordinate \(i\) gives \(v_i\phi''(z_i)=0\) for every \(z_i\). Bounded nonconstant \(\psi\) cannot have \(\psi''\equiv0\): such a function would be affine and bounded, hence constant. Since \(e>0\), \(\phi''\not\equiv0\), and \(v=0\).

The exact initialized transpose formulas are

\[
q_i^\ell=\zeta_i^\ell+\sum_k R^\ell_{ik}h_k^\ell,
\qquad \operatorname{Cov}(\zeta^\ell)=S_{\ell+1},        \tag{N.8}
\]

where each reverse source group \(\zeta^\ell\) is centered Gaussian and independent of all forward source groups and first-layer roots. The deterministic response coefficients are

\[
R^{L-1}_{ik}=E[p_kD_i^LD_k^L+
                 \mathbf1_{i=k}H\phi''(Z_i^L)],
\]

\[
R^\ell_{ik}=E[\mathbf1_{i=k}\phi''(Z_i^{\ell+1})q_i^{\ell+1}
                    +D_i^{\ell+1}R^{\ell+1}_{ik}D_k^{\ell+1}]
\quad(\ell<L-1).                                      \tag{N.9}
\]

Section N.4 derives and justifies these formulas. They include both the current curvature term and the next-layer return. Neither return is assumed positive or discarded.

Conditionally on \(Z^\ell\), (N.8) gives

\[
\operatorname{Cov}(\beta^\ell\mid Z^\ell)
=\operatorname{diag}(D^\ell)S_{\ell+1}\operatorname{diag}(D^\ell)
\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3.
\]

Backward induction from \(S_L\succ0\) proves

\[
S_\ell\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3\succ0
\quad(\ell<L).                                        \tag{N.10}
\]

The same formula applies at layer 1 even if \(Z^1\) is singular. Applying it componentwise in (N.6) and summing gives

\[
d\|V^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)\sum_i p_i^2>0.
\]

For every matrix block,

\[
\|V^\ell\|_{\rm HS}^2
=\operatorname{tr}(\operatorname{diag}(p)S_\ell
                  \operatorname{diag}(p)Q_{\ell-1})
\ge\lambda_{\min}(S_\ell)\lambda_{\min}(Q_{\ell-1})
                         \sum_i p_i^2>0.                \tag{N.11}
\]

The inequality follows by pairing \(S_\ell\succeq\lambda_{\min}(S_\ell)I\) with the positive matrix \(\operatorname{diag}(p)Q_{\ell-1}\operatorname{diag}(p)\), then using the analogous bound for \(Q_{\ell-1}\).

For the bottom samples,

\[
\|U_j^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)
                  \sum_i\Gamma_{ji}^2p_i^2
\ge\alpha^2\lambda_{\min}(S_2)p_j^2>0,                 \tag{N.12}
\]

using \(\Gamma_{jj}=1\). This proves every hidden block and every bottom sample is nonzero.

## N.3. Exact return recursion and an innovation at every upper layer

Fix one sample \(j\). Define deterministic coefficients

\[
c^1_{ji}=\Gamma_{ji}p_i,
\qquad
c^\ell_{ji}=p_i(Q_{\ell-1})_{ij}
          +c^{\ell-1}_{ji}E[D_j^{\ell-1}D_i^{\ell-1}]
\quad(2\le\ell\le L).                                \tag{N.13}
\]

No sign of these coefficients is required. Let \(\xi_{T_j^{\ell-1}}\) denote the primitive source of the added forward query \(A_\ell T_j^{\ell-1}\), belonging to the same oriented source group as the three original coordinates \(Z_i^\ell\). The exact recursion is

\[
U_j^\ell=\xi_{T_j^{\ell-1}}+\sum_i c^\ell_{ji}\beta_i^\ell
\qquad(2\le\ell\le L).                               \tag{N.14}
\]

To prove the base case, (N.8) at layer 1 and (N.7) show, differentiating in the named reverse source \(\zeta_i^1\),

\[
\partial_{\zeta_i^1}T_j^1=D_j^1c^1_{ji}D_i^1.
\]

The same-matrix forward response rule therefore reads

\[
A_2T_j^1=\xi_{T_j^1}+\sum_i\beta_i^2
                               c^1_{ji}E[D_j^1D_i^1].
\]

Adding \(V^2h_j^1=\sum_i p_i(Q_1)_{ij}\beta_i^2\) proves (N.14) for \(\ell=2\).

Now suppose (N.14) is proved at some \(2\le\ell<L\). Its primitive forward source belongs to the \(A_\ell\) forward group, which is independent of the \(A_{\ell+1}^*\) reverse group \(\zeta^\ell\). These are distinct named formal slots even if a covariance is singular. Formula (N.8) consequently gives the exact derivative

\[
\partial_{\zeta_i^\ell}T_j^\ell
=D_j^\ell c^\ell_{ji}D_i^\ell.
\]

Applying the forward response rule to \(A_{\ell+1}T_j^\ell\), then adding \(V^{\ell+1}h_j^\ell\), gives (N.14) at \(\ell+1\) with exactly (N.13). This proves (N.14) at every depth, with all transpose returns retained.

Regress the Gaussian source \(\xi_{T_j^{\ell-1}}\) on the three original forward sources \(Z^\ell\). Their covariance is \(Q_{\ell-1}\succ0\). Since oriented source covariances are the full input second moments, the independent regression remainder \(\varepsilon_{\ell j}\) has variance

\[
\sigma_{\ell j}^2
=\inf_{b\in\mathbb R^3}
       \left\|T_j^{\ell-1}-\sum_i b_i h_i^{\ell-1}\right\|_2^2.
                                                               \tag{N.15}
\]

This is linear regression without an intercept: the sources are centered, while their covariance is the **uncentered** input Gram. The conditional-variance bounds below hold for this precise regression because every competitor \(\sum_i b_i h_i^{\ell-1}\) is measurable in the conditioning variables.

At \(\ell=2\), all \(h_i^1\) are measurable in \(Z^1\), so (N.10) yields

\[
\begin{aligned}
\sigma_{2j}^2
&\ge E\operatorname{Var}(T_j^1\mid Z^1)\\
&\ge\alpha^4\lambda_{\min}(S_2)
                     \sum_i\Gamma_{ji}^2p_i^2
\ge\alpha^4\lambda_{\min}(S_2)p_j^2>0.                \tag{N.16}
\end{aligned}
\]

The remainder \(\varepsilon_{2j}\) is independent of \(Z^2\) and of the separate reverse group \(\zeta^2\), if present. By (N.8), all \(\beta_i^2\) are functions of \((Z^2,\zeta^2)\); at \(L=2\) they are functions of \(Z^2\) alone. Thus (N.14), after regression, is

\[
U_j^2=\varepsilon_{2j}+F_{2j}(Z^2,\zeta^2),
\]

with the unused reverse argument omitted at the top. In particular \(\|U_j^2\|_2^2\ge\sigma_{2j}^2\).

For the induction step assume \(2\le\ell<L\) and \(\sigma_{\ell j}^2>0\). Exactly the same regression in (N.14) gives

\[
U_j^\ell=\varepsilon_{\ell j}+F_{\ell j}(Z^\ell,\zeta^\ell),
\]

where \(\varepsilon_{\ell j}\) is independent of the displayed pair. Therefore

\[
\operatorname{Var}(T_j^\ell\mid Z^\ell,\zeta^\ell)
                  =(D_j^\ell)^2\sigma_{\ell j}^2.
\]

Testing (N.15) for the next layer against this conditional variance proves

\[
\sigma_{\ell+1,j}^2\ge E[(D_j^\ell)^2]\sigma_{\ell j}^2
                          \ge\alpha^2\sigma_{\ell j}^2>0.       \tag{N.17}
\]

The new remainder belongs to the next forward source group and is independent of its original forward tuple and separate reverse group; at the top there is no reverse group to condition on. Thus it cannot cancel the other terms of (N.14). Combining (N.16) and (N.17),

\[
\|U_j^\ell\|_2^2\ge\sigma_{\ell j}^2
       \ge\alpha^{2\ell}\lambda_{\min}(S_2)p_j^2>0
\quad(2\le\ell\le L).                                \tag{N.18}
\]

Together with (N.12), this covers every sample and layer. Finally \(\|T_j^\ell\|_2\ge\alpha\|U_j^\ell\|_2>0\). The three samples' new forward sources may be mutually correlated. No step assumes otherwise; one may prove the result with one fixed augmented transcript per sample and then take their finite union.

## N.4. The same-matrix source formulas and unbounded products

Only the finite Gaussian foundation is needed here. This section states its precise specialization, checks the actual query schedule, and proves its derivative-valid extension for every unbounded product used above. Oddness, monotonicity of the perturbation, and affine perturbation estimates play no role.

The actual finite initialization transcript, with normalized finite inner products, is as follows. First reveal the first-layer roots and calculate all three ordinary forward calls at each layer. Next form \(H\), the three top \(\beta_i^L\), and, descending through the layers, the three calls \(A_{\ell+1}^*\beta_i^{\ell+1}\) and the gates \(\beta_i^\ell\). For one fixed sample \(j\), form \(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\) and \(T_j^1\). Then ascend through layers \(2,\ldots,L\): make the one added query \(A_\ell T_j^{\ell-1}\), add \(\sum_i p_i\langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n\beta_i^\ell\), and apply the gate to obtain \(T_j^\ell\). These are all the action probes used. Their empirical contractions converge to the \(Q\) coefficients; replacing these finitely many convergent scalar coefficients by their limits changes the normalized vector errors by \(o_P(1)\), because all participating vector norms are bounded in probability. One may therefore use deterministic limiting coefficients in the source calculation.

Here is the needed finite-program statement and why its use is legitimate. For a fixed finite list of independent \(N(0,1/n)\) matrices, reused in both orientations, fixed finite root tuples with finite second moment, and coordinate instructions that are \(C^1\) with bounded first derivatives, same-layer empirical laws and second moments converge. For an initialized forward query on \(h\), and reverse query on \(u\), their scalar source formulas are

\[
Ah=\xi_h+\sum_s u_sE[\partial_{\zeta_s}h],\qquad
A^*u=\zeta_u+\sum_r v_rE[\partial_{\xi_r}u],             \tag{N.19}
\]

where the sums use the previously queried inputs in the opposite orientation. Sources belonging to distinct orientations or matrices are independent; within one group the covariance is the full Gram of its query inputs. Formal derivatives freeze deterministic coefficients and covariance parameters and differentiate distinct named source slots.

The conditioning proof covers any fixed finite number of matrices: condition successively on the current transcript. A coordinate instruction reveals no new matrix randomness. A matrix query conditions only that matrix's residual Gaussian factor on one further linear observation; the other residual factors retain their product conditional law. Induction over the finite instruction list gives the stated conclusion with \(L-1\) matrices.

For explicit verification of (N.19), if old calls are \(AV=Y\), \(A^TU=Q\), Gaussian conditioning gives

\[
A\mid\mathcal H=M+P_{U^\perp}\widetilde A P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}Q^TP_{V^\perp},
\]

initially when the indicated Grams are nonsingular. Indeed \(M\) satisfies the two constraints and is orthogonal to all homogeneous solutions \(P_{U^\perp}KP_{V^\perp}\), so isotropic Gaussian projection proves the conditional law. With \(h_\perp=h-P_Vh\), the new answer is a regression term plus an opposite-orientation response and

\[
                     \|h_\perp\|_nP_{U^\perp}g_n.
\]

The removed Gaussian projection satisfies \(E[\|P_Ug_n\|_n^2\mid\mathcal H]=\operatorname{rank}(U)/n\to0\). The response coefficient is obtained from

\[
E[q_sh_\perp]=E[\zeta_sh_\perp],\qquad
E[\zeta h_\perp]=\operatorname{Cov}(\zeta)
                                  E[\nabla_\zeta h_\perp].
\]

The first identity uses the old-return representation of \(q_s\) and orthogonality to \(V\); the second is Gaussian integration by parts. Substituting the old forward source representations cancels the derivatives of the regression projection, leaving exactly (N.19). The covariance of the resulting new forward source with old sources is \(E[h v_r]\), and its variance is \(E[h^2]\). This proves (N.15), including the fact that conditioning on transpose queries cannot erase its positive innovation.

Singular first-layer roots are allowed and do not need an inverse. In this particular proof all original matrix forward Grams \(Q_\ell\) and backward Grams \(S_\ell\) are positive definite once established; for a separate fixed sample the augmented forward Gram is positive definite by (N.16)–(N.17). Alternatively Part F's singular-query extension uses fresh small input noises, converging finite covariance square roots and bounded action norms; it does not assume continuity of pseudoinverses. No extra probabilistic independence of matrix answers and their inputs is being introduced.

The untruncated coordinate products in the present program are not themselves globally bounded-derivative instructions, so they need a separate justification. Let \(\tau_M\) be smooth, equal to the identity on \([-M,M]\), with \(|\tau_M(q)|\le|q|\), \(|\tau_M'|\le1\), and bounded range. Such clips can be obtained by integrating a smooth cutoff. At the top use

\[
\beta_{i,M}^L=D_i^L\tau_M(H).
\]

Its derivative in the named forward source \(Z_k^L\) is

\[
D_i^L\tau_M'(H)p_kD_k^L
 +\mathbf1_{i=k}\phi''(Z_i^L)\tau_M(H).
\]

This is bounded in absolute value by a fixed constant times \(1+|H|\), independently of \(M\). The top forward fields have all finite moments, so dominated convergence gives the first line of (N.9). The clipped fields converge in \(L^2\), their Grams converge, and coupling the resulting Gaussian reverse sources via finite positive-semidefinite covariance square roots gives convergence of the sources and (N.8) at layer \(L-1\).

Suppose (N.8) has been justified at layer \(\ell+1\). Its explicit expression is a finite Gaussian source plus a deterministic linear combination of linear-growth Gaussian functions. Thus it has all finite moments. Its derivative in \(Z_k^{\ell+1}\) is \(R^{\ell+1}_{ik}D_k^{\ell+1}\). For the next clipped gate \(D_i^{\ell+1}\tau_N(q_i^{\ell+1})\), the required derivative is

\[
\mathbf1_{i=k}\phi''(Z_i^{\ell+1})\tau_N(q_i^{\ell+1})
 +D_i^{\ell+1}\tau_N'(q_i^{\ell+1})R^{\ell+1}_{ik}D_k^{\ell+1}.
\]

At fixed outer cap, remove all earlier caps; then let \(N\to\infty\). The final envelope is a constant times \(1+|q_i^{\ell+1}|\), which is integrable. This proves the second line of (N.9), the next source covariance, and (N.8) at layer \(\ell\). Repeating this explicit finite step proves the whole backward chain with only \(C^2\) regularity.

Here is an explicit coherent clipping program for all added forward queries. Let the backward caps at layers \(1,\ldots,L-1\) be \(N_1,\ldots,N_{L-1}\), and the top cap be \(N_L\). Thus

\[
\beta_i^{L,N}=D_i^L\tau_{N_L}(H),\quad
q_i^{\ell,N}=A_{\ell+1}^*\beta_i^{\ell+1,N},\quad
\beta_i^{\ell,N}=D_i^\ell\tau_{N_\ell}(q_i^{\ell,N}).
\]

Use these same \(\beta_i^{\ell,N}\) both as reverse query inputs and in the block contributions. Give each added forward gate its own cap \(M_\ell\):

\[
U_j^{1,N,M}=\sum_i\Gamma_{ji}p_i\beta_i^{1,N},\qquad
T_j^{\ell,N,M}=D_j^\ell\tau_{M_\ell}(U_j^{\ell,N,M}),
\]

\[
U_j^{\ell,N,M}=A_\ell T_j^{\ell-1,N,M}
                  +\sum_i p_i(Q_{\ell-1})_{ij}\beta_i^{\ell,N}
\quad(\ell\ge2).
\]

At all fixed caps these are legitimate bounded-derivative coordinate instructions and initialized action calls. Their source formulas have the exact form

\[
U_j^{\ell,N,M}=\xi_{T_j^{\ell-1,N,M}}
                     +\sum_i c^{\ell,N,M}_{ji}\beta_i^{\ell,N},
\]

with \(c^{1,N,M}_{ji}=\Gamma_{ji}p_i\). To derive the next coefficient, the previously established backward formula gives

\[
\partial_{\zeta_i^\ell}\beta_k^{\ell,N}
=\mathbf1_{i=k}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
\]

The current forward primitive source is a different named slot from \(\zeta_i^\ell\), so

\[
\partial_{\zeta_i^\ell}T_j^{\ell,N,M}
=D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
       c^{\ell,N,M}_{ji}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
                                                               \tag{N.22}
\]

Consequently, for \(\ell<L\),

\[
c^{\ell+1,N,M}_{ji}=p_i(Q_\ell)_{ij}
 +c^{\ell,N,M}_{ji}E[D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
                          D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N})].
                                                               \tag{N.23}
\]

This proves the full capped source recurrence, rather than assuming a limit of the uncapped formula. In particular define finite deterministic bounds

\[
C^1_{ji}=|\Gamma_{ji}p_i|,\qquad
C^{\ell+1}_{ji}=|p_i(Q_\ell)_{ij}|+B^2C^\ell_{ji}.
\]

Then \(|c^{\ell,N,M}_{ji}|\le C^\ell_{ji}\), and the derivative in (N.22) is bounded by \(B^2C^\ell_{ji}\), uniformly in **all** caps. No smallness of these constants with depth is required.

First remove the backward caps in the descending dependency order established above, at fixed forward caps. Actual action continuity and the bounded gate comparisons give \(L^2\) convergence of \(q,\beta,U,T\) successively; their source Grams converge as well. Couple the finite source vectors through covariance square roots. Along a coupled subsequence their arguments converge almost surely; continuity and the bound \(B^2C^\ell_{ji}\) pass (N.22)–(N.23) under expectation. Next remove the forward caps in ascending order \(M_1,M_2,\ldots,M_L\), holding later caps fixed. The already identified incoming \(U_j^\ell\) is in \(L^2\), so \(\tau_{M_\ell}(U_j^\ell)\to U_j^\ell\) in \(L^2\). The subsequent initialized answers converge by bounded actions. In (N.22), the outer clip derivative tends to one and its integrand remains bounded by \(B^2C^\ell_{ji}\); (N.23) therefore converges to (N.13) at that layer. This proves the uncapped (N.14) and its bounded formal source derivative at every step. Each resulting \(U_j^\ell,T_j^\ell\) is, from its explicit source expression, a bounded gate times finite sums of Gaussian sources and linear-growth Gaussian functions, so it also has all finite moments.

To identify these limiting formulas with the actual uncut action answers, use bounded initialized action norms and bounded multiplier continuity. If \(z_m\to z\) in probability and \(q_m\to q\) in \(L^2\), then

\[
\|D(z_m)q_m-D(z)q\|_2
\le B\|q_m-q\|_2+\|[D(z_m)-D(z)]q\|_2\to0.
\]

For the second term restrict \(q\) to a bounded set, use bounded convergence in probability there, and then make its \(L^2\) tail small. Matrix action errors are bounded by the action norm times their input errors. Explicitly, a gate clipping error obeys

\[
\|D(z)[q-\tau_M(q)]\|_2
\le2B\|q\mathbf1_{|q|>M}\|_2
\le4B\|(|q|-M/2)_+\|_2\longrightarrow0.
\]

The same inequality holds in empirical normalized norm. Joint \(\mathcal W_2\) convergence of an incoming finite-array field implies convergence of the squared norm of \((|q|-M/2)_+\), since this is a 1-Lipschitz transformation followed by its second moment. Thus the empirical clipping tail is small after taking width to infinity and then \(M\to\infty\). The high-probability uniform bounds on the finitely many initialized matrix norms transfer this error to the next actual answer. Apply this gate/action step in the exact finite schedule above. A triangle inequality, with fixed caps first, identifies the full uncut finite-array law and its second moments, as well as its canonical action answers. The source laws, current responses, and input covariances all survive the ordered removal of the clips.

## N.5. Physical acceleration and the coefficient 18

Let a strong physical gradient-flow solution in the original raw Hilbert metric exist on a right neighborhood of zero. Its current hidden actions are their initialized actions plus Hilbert–Schmidt increments. Denote the residual-free physical backward fields by

\[
b_i^L(t)=D_i^L(t)C(t),\qquad
b_i^\ell(t)=D_i^\ell(t)A_{\ell+1}(t)^*b_i^{\ell+1}(t).
\]

The physical loss is \(\tfrac12\sum_i(f_i-y_i)^2\), so the exact raw updates are

\[
C'=-\sum_i r_i h_i^L,\quad
(\theta_h^1)'=-d^{-1}\sum_i r_i b_i^1x_i,\quad
A_\ell'=-\sum_i r_i b_i^\ell\otimes h_i^{\ell-1}.
\]

Since \(C(0)=0\), the initial predictions vanish, \(r_i(0)=-y_i=-3p_i\), all hidden first derivatives vanish, and

\[
C'(0)=3H,\qquad C(t)/t\longrightarrow3H.
\]

Strong multiplier continuity from Section N.4 and operator-norm continuity of the Hilbert–Schmidt action increments give, successively from the top,

\[
b_i^\ell(t)/t\longrightarrow3\beta_i^\ell.
\]

Substitution in the exact raw updates yields

\[
\theta_h'(t)/t\longrightarrow9V,\qquad
\theta_h(t)=\theta_h(0)+\tfrac92t^2V+o_{\rm raw}(t^2).  \tag{N.20}
\]

For a strong \(C^1\) \(L^2\) curve \(z(t)\) and bounded continuous \(\phi'\), the identity

\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=\frac{z(t+h)-z(t)}h
  \int_0^1\phi'(z(t)+s[z(t+h)-z(t)])\,ds
\]

and bounded multiplier continuity prove the strong chain rule. Combining it with the product rule for a strongly differentiable field and an operator differentiable in Hilbert–Schmidt norm proves recursively

\[
(z_j^\ell)'(t)/t\longrightarrow9U_j^\ell,\qquad
(h_j^\ell)'(t)/t\longrightarrow9T_j^\ell.               \tag{N.21}
\]

Since the initial first derivatives are zero, (N.20)–(N.21) are the claimed nonzero strong right second derivatives.

To compute the kernel coefficient without assuming an ambient \(L^2\)-to-\(L^2\) Fréchet derivative of the activation, put

\[
T=\sum_jp_jT_j^L.
\]

Genuine adjunction and (N.6)–(N.7) give the following exact telescoping identity. At a matrix layer,

\[
\sum_jp_j\langle\beta_j^\ell,U_j^\ell\rangle
=\|V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle q_j^{\ell-1},T_j^{\ell-1}\rangle
=\|V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle\beta_j^{\ell-1},U_j^{\ell-1}\rangle.
\]

The final bottom sum is \(d\|V^1\|_2^2\), and the top sum is \(\langle H,T\rangle\). Hence

\[
                         \langle H,T\rangle=\|V\|_{\rm hidden}^2.
\]

Writing \(H(t)=\sum_jp_jh_j^L(t)\), (N.21) gives

\[
H(t)=H+\tfrac92t^2T+o_{L^2}(t^2),\qquad
\|H(t)\|_2^2=\|H\|_2^2+9t^2\|V\|_{\rm hidden}^2+o(t^2).
\]

The hidden part \(g_h(t)\) of the raw gradient of \(\sum_i p_i f_i(t)\) satisfies \(g_h(t)/t\to3V\) by the same backward calculation, so

\[
\|g_h(t)\|_{\rm hidden}^2=9t^2\|V\|_{\rm hidden}^2+o(t^2).
\]

The true raw kernel identity is

\[
p^TK_{\rm total}(t)p=\|H(t)\|_2^2+\|g_h(t)\|_{\rm hidden}^2.
\]

Adding its two terms proves (N.3). All \(L\) hidden blocks occur in \(\|V\|_{\rm hidden}^2\), and each is strictly positive by Section N.2. The coefficient 18 and the nonzero accelerations therefore persist at every fixed depth with the same fixed activation. The severe depth-dependent smallness imposed by an affine comparison is unnecessary for this initial-motion conclusion.
