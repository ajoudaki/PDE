# Three-input local-limit extension: convergence and existence check

This note verifies the extension of the local-limit and stability portions of `/tmp/TWO_INPUT_LOCAL_LIMIT_PROOF.md`. It does not supply the separate strict-feature-learning argument.

Let there be three inputs with normalized Gram matrix

\[
G_{ab}=x_a^\top x_b/d,\qquad G\succeq0,\qquad G_{aa}=1.
\]

No lower eigenvalue bound, and no invertibility, is needed for the convergence construction. In particular it covers pairwise nonparallel triples lying in a two-dimensional span. The labels obey \(|y_a|\le1\); the requested sign labels are included.

Replace every data-index sum in (M1), (M4), and the appendix recursions by a sum from 1 to 3. Use initial first-layer root triples \(N(0,G)\). This is a valid Gaussian-root input to the finite-program result even when \(G\) is singular: write the root as \(G^{1/2}\gamma\), with \(\gamma\) a standard Gaussian triple. No conditioning argument requires \(G^{-1}\). The singular-covariance derivative convention in appendix equations (4) and (9) is unchanged.

The local time can be chosen uniformly over all such Gram matrices and labels. Indeed \(|G_{ab}|\le1\), each absolute row sum is at most 3, and \(\|G\|_{\rm op}\le3\). All estimates below depend on these upper bounds, not a lower eigenvalue.

The readout recurrence becomes

\[
B_{k+1}\le B_k+6\Delta\|\phi\|_\infty(1+\|\phi\|_\infty B_k),
\qquad B_0=0.
\]

For \(k\Delta\le T\le1\), its geometric sum gives

\[
B_k\le C_0T,\qquad |r_{a,k}|\le C_0,
\qquad |\delta_{a,k}^{(2)}|\le C_0T,
\]

with one common constant for every allowed geometry and label pattern. The sums of absolute training-memory coefficients in the forward and backward equations remain bounded by \(C_0T\) and \(C_0T^3\), respectively.

Use the same accumulated response quantities \(\mathcal A_k,\mathcal C_k\), now summing over three input indices. The first-layer derivative estimate becomes

\[
J_{k+1}\le
\left(1+C\Delta[1+\mathcal A_k+\sum_{b=1}^3|\eta_{b,k}|]\right)J_k+C\Delta.
\]

Consequently

\[
J_k\le CT\exp\left(CT(1+\mathcal A_{k-1})+
C\Delta\sum_{s<k}\sum_{b=1}^3|\eta_{b,s}|\right).
\]

There is no need for independence among the backward Gaussian slots. Their marginal variances are at most \(C_0^2T^2\). Jensen's inequality over the \(3k\) summands and the scalar Gaussian exponential bound give

\[
\begin{aligned}
\mathbb E\exp\left(C\Delta\sum_{s<k,b}|\eta_{b,s}|\right)
&\le\frac1{3k}\sum_{s<k,b}
\mathbb E\exp(3Ck\Delta|\eta_{b,s}|)\\
&\le2\exp\left(\frac92 C^2 C_0^2 T^4\right).
\end{aligned}
\]

Thus the original response estimate remains

\[
\mathcal C_k\le CT\exp(CT(1+\mathcal A_{k-1})+CT^4).
\]

The readout and second-layer derivative bounds are unchanged in form:

\[
\sum_{b,s}\left|
\frac{\partial\delta_{a,k}^{(2)}}{\partial\xi_{b,s}}
\right|\le C_1TV_k,
\]

\[
V_k\le\max\{V_{k-1},
1+C_1T(\mathcal C_k+C_0T)V_{k-1}\}.
\]

Choose \(M_A=2C_1\), then \(M_C\), then one \(T_0>0\) with

\[
C_1T_0^2(M_C+C_0)\le\tfrac12
\]

and with the preceding exponential bound at most \(M_CT\) when \(\mathcal A_{k-1}\le M_AT\). The same causal induction gives

\[
\mathcal A_k\le M_AT,\qquad
\mathcal C_k\le M_CT,\qquad V_k\le2.
\]

The constants used to choose \(T_0\) are common to all normalized three-input configurations and all labels of magnitude at most 1. This proves a common positive time, independent of width, actual learning rate, auxiliary proof mesh, input dimension, and the smallest nonzero input Gram eigenvalue.

For each \(a\), the full backward response remains a centered Gaussian of variance at most \(CT^2\), plus a possibly dependent remainder bounded in absolute value by \(CT\). Hence

\[
\sup_{\Delta>0}\max_{a,k:k\Delta\le T_0}
\mathbb E\exp\left(c\left|
(W_k^{(2)})^*\delta_{a,k}^{(2)}
\right|^2\right)\le C.
\]

The localization inequality (M9) is coordinatewise and does not involve \(G\). Multiplication by \(G\) in the first-layer differential equation costs at most the fixed factor 3. Consequently (M11) and (M14) hold with the metric

\[
d=\sum_{a=1}^3
\left(\mathbb E|Z_a^{(1)}-\widetilde Z_a^{(1)}|^2\right)^{1/2}
+\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+\left(\mathbb E|W^{(3)}-\widetilde W^{(3)}|^2\right)^{1/2}.
\]

The order of limits stays the same: fixed cutoff and coarse mesh, first \(n\to\infty\) with any \(\eta_n\to0\); then mesh to zero; then cutoff to infinity. This proves the same unique autonomous flow, joint empirical/probe convergence, kernel convergence, hidden path-law convergence and integrated squared hidden-speed convergence on \([0,T_0]\).

Singular \(G\) only encodes exact first-layer relations. If \(Gc=0\), then \(\sum_a c_ax_a=0\), so \(\sum_a c_a z_a^{(1)}=0\) at initialization and every finite update. The limiting root law has the same relation, and (M4) preserves it because \(c^TG=0\). There is no need to invert this coordinate description.

The three kernel blocks retain their formulas, with indices 1 through 3, and are positive semidefinite for all times by their Gram interpretations. Even if \(G\) is singular, the gradient-flow and kinetic-energy identities do not need an inverse. At finite width,

\[
\frac{\|\dot W^{(1)}\|_F^2}{n}=4r_n^TK_n^{(1)}r_n,
\quad
\|\dot W^{(2)}\|_F^2=4r_n^TK_n^{(2)}r_n,
\quad
\frac{\|\dot W^{(3)}\|_2^2}{n}=4r_n^TK_n^{(3)}r_n.
\]

For the first identity, substitute the exact first-weight velocity and use \(x_b^Tx_c/d=G_{bc}\). Thus singular geometry poses no hidden problem for parameter energy, either. Hidden-preactivation energies already follow from the velocity comparisons in the source proof, with three instead of two summands.

Conclusion: the LOCAL limit theorem extends in full to three inputs; the convergence part even permits parallel or antiparallel inputs. Pairwise nonparallel assumptions belong only to the strict activity/nondegeneracy conclusions, whose proof must be rechecked separately because the original two-input argument used positive definiteness of \(G\) and exchange symmetry.
