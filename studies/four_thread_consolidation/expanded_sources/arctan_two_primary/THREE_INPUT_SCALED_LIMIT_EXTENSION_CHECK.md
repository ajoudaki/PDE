# Three-input local limit with initialization and learning-rate constants

This extends the existence/convergence portion of `/tmp/THREE_INPUT_LOCAL_LIMIT_PROOF.md`. Strict feature-learning expansions must incorporate the constants separately.

## A simple sufficient family

Keep the three fixed normalized inputs, their Gram matrix \(G\), the forward normalization, output normalization, activation, and summed loss unchanged. Initialize independently by

\[
W_{0,ij}^{(1)}\sim N(0,\sigma_1^2),\qquad
W_{0,ji}^{(2)}\sim N(0,\sigma_2^2/n),\qquad
W_{0,j}^{(3)}\sim N(0,\sigma_3^2n^{-2\beta}),
\]

where \(0<\sigma_1,\sigma_2<\infty\), \(0\le\sigma_3<\infty\), and \(\beta>0\). Exact zero readout is allowed. Use layer learning-rate multipliers \(n\kappa_1,\kappa_2,n\kappa_3\), with \(0<\kappa_\ell<\infty\). The exact updates become

\[
\begin{aligned}
z_{a,k+1}^{(1)}&=z_{a,k}^{(1)}
-2\eta_n\kappa_1\sum_bG_{ab}r_{n,b,k}\delta_{b,k}^{(1)},\\
W_{k+1}^{(2)}&=W_k^{(2)}
-\frac{2\eta_n\kappa_2}{n}\sum_b
r_{n,b,k}\delta_{b,k}^{(2)}(h_{b,k}^{(1)})^\top,\\
W_{k+1}^{(3)}&=W_k^{(3)}
-2\eta_n\kappa_3\sum_b r_{n,b,k}h_{b,k}^{(2)}.
\end{aligned}
\]

For every positive \(\eta_n\to0\), the same local theorem holds, with population first-layer root \(N(0,\sigma_1^2G)\), population initial readout zero, and initial Gaussian matrix action of variance scale \(\sigma_2^2\). Each population differential equation acquires its respective factor \(\kappa_\ell\). The positive existence interval depends on fixed scale bounds but not on width, actual learning rate, auxiliary mesh, or a lower Gram eigenvalue. For scale parameters in a fixed compact set with finite upper bounds, the existence time can be common. Positivity of the scales is needed for the strict feature-learning claims, not for the estimates themselves.

The weighted prediction kernel is

\[
K=\kappa_1K^{(1)}+\kappa_2K^{(2)}+\kappa_3K^{(3)}.
\]

Thus \(\dot f=-2Kr\) and \(\dot L=-4r^TKr\). One can either retain the old unweighted block definitions and display these coefficients, or define weighted blocks explicitly. Omitting the coefficients from the prediction equation would be incorrect.

## Every bridge in the proof

The Gaussian root theorem permits \(\sigma_1^2G\), even when singular, by writing the root as \(\sigma_1G^{1/2}\gamma\). Initial matrix operator concentration changes only to

\[
\mathbb P(\|W_0^{(2)}\|_{\rm op}>M)
\le2\,9^{2n}\exp[-nM^2/(8\sigma_2^2)].
\]

Choose \(M\) large compared with \(\sigma_2\). The construction of the common bounded action and its adjoint is unchanged.

Here is the exact correction to the response formulas. Keep \(A,C\) defined as expectations of derivatives with respect to the actual Gaussian slots. Their covariances now are

\[
\mathbb E[\xi_{a,k}\xi_{b,s}]
=\sigma_2^2\mathbb E[H_{a,k}^{(1)}H_{b,s}^{(1)}],
\qquad
\mathbb E[\eta_{a,k}\eta_{b,s}]
=\sigma_2^2\mathbb E[\delta_{a,k}^{(2)}\delta_{b,s}^{(2)}].
\]

Both derivative-response sums acquire a factor \(\sigma_2^2\):

\[
W_0^{(2)}H_{a,k}^{(1)}
=\xi_{a,k}+\sigma_2^2\sum_{b,s<k}C_{ak,bs}\delta_{b,s}^{(2)},
\]

\[
(W_0^{(2)})^*\delta_{a,k}^{(2)}
=\eta_{a,k}+\sigma_2^2\sum_{b,s\le k}A_{ak,bs}H_{b,s}^{(1)}.
\]

Consequently, the two complete recursions are

\[
Z_{a,k}^{(2)}=\xi_{a,k}+
\sum_{b,s<k}
\left(\sigma_2^2C_{ak,bs}-2\kappa_2\Delta r_{b,s}
\mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}]\right)
\delta_{b,s}^{(2)},
\]

\[
P_{a,k}=\eta_{a,k}+
\sum_{b,s\le k}
\left(\sigma_2^2A_{ak,bs}
-\mathbf1_{s<k}2\kappa_2\Delta r_{b,s}
\mathbb E[\delta_{b,s}^{(2)}\delta_{a,k}^{(2)}]\right)
H_{b,s}^{(1)}.
\]

The variance factor multiplies the initial-matrix responses, not the trained rank-one memory.

The readout estimate is now

\[
B_{k+1}\le B_k+6\kappa_3\Delta\|\phi\|_\infty
(1+\|\phi\|_\infty B_k),\qquad B_0=0.
\]

Thus \(B_k\le C_0T\), \(|r_{a,k}|\le C_0\), and \(|\delta_{a,k}^{(2)}|\le C_0T\), with constants depending on \(\kappa_3\). The forward and backward training-memory row sums remain \(O(T)\) and \(O(T^3)\). The derivative recurrences then retain the form

\[
\mathcal C_k\le CT\exp[CT(1+\mathcal A_{k-1})+CT^4],
\]

\[
V_k\le\max\{V_{k-1},1+C_1T(\mathcal C_k+C_0T)V_{k-1}\},
\qquad \mathcal A_k\le C_1TV_k,
\]

after absorbing fixed factors \(\kappa_1,\kappa_2,\kappa_3,\sigma_2^2\) into constants. The same short-time induction gives \(\mathcal A_k,\mathcal C_k=O(T)\), \(V_k\le2\), and a Gaussian backward tail bound uniform over meshes. No lower eigenvalue of \(G\) enters.

The localization, Euler Cauchy, existence, uniqueness, autonomy, oracle and actual-GD comparison arguments are therefore unchanged. They use finite upper bounds for the readout supremum and matrix operator norm. For the actual initial readout, for every \(\varepsilon>0\) and \(\sigma_3>0\),

\[
\mathbb P(\|W_{n,0}^{(3)}\|_\infty>\varepsilon)
\le2n\exp[-\varepsilon^2n^{2\beta}/(2\sigma_3^2)]\to0,
\]

and

\[
\mathbb E\left[\|W_{n,0}^{(3)}\|_2^2/n\right]
=\sigma_3^2n^{-2\beta}\to0.
\]

The oracle can therefore still start from zero readout. Its initialization discrepancy vanishes, and the actual readout supremum is bounded with probability tending to one. These are precisely the two initialization obligations in the original bridge. There is no special role for \(\beta=1\).

The same kernel, probe, hidden-path and hidden-velocity convergence statements follow. The physical parameter-speed identities include the squared learning multipliers:

\[
\|\dot W^{(1)}\|_F^2/n=4\kappa_1^2r^TK^{(1)}r,
\quad
\|\dot W^{(2)}\|_F^2=4\kappa_2^2r^TK^{(2)}r,
\quad
\|\dot W^{(3)}\|_2^2/n=4\kappa_3^2r^TK^{(3)}r.
\]

Accordingly \(-\dot L\) is the sum of these three quantities divided by their respective \(\kappa_\ell\).

## Converging learning-rate constants

The same theorem allows \(\kappa_{\ell,n}\to\kappa_\ell\in(0,\infty)\). The sequences are eventually uniformly bounded. In the oracle comparison, replacing the actual coefficients by their limits adds a vector-field forcing bounded by

\[
C\sum_{\ell=1}^3|\kappa_{\ell,n}-\kappa_\ell|.
\]

The bound follows from the already proved uniform mean-square bounds on each component velocity; it requires no extra differentiability or finite-coordinate tail estimate. The comparison bracket therefore becomes

\[
\|W_{n,0}^{(3)}\|_2/\sqrt n
+(1+R)(\eta_n+\Delta)
+\sum_\ell|\kappa_{\ell,n}-\kappa_\ell|
+e^{-cR^2}+o_{\mathbb P}(1).
\]

All terms vanish in the existing order of limits. No convergence rate for \(\kappa_{\ell,n}\) is required. The same coupling argument would also permit converging positive \(\sigma_{1,n},\sigma_{2,n}\), with an additional vanishing initialization discrepancy, but fixed scales are already a sufficient family.

## Separate bounded, nonvanishing readout extension

Suppose instead the initial readout coordinates are iid copies of an independent random variable \(W_0^{(3)}\) with \(|W_0^{(3)}|\le B_0<\infty\). Keep that same initialization in the finite oracle and in the population state. The local existence/convergence argument still closes, but the limiting system and its small-time expansion are different.

For the finite-program step, a bounded scalar root can be represented as a bounded measurable function of an independent Gaussian root, using its quantile function. All response derivatives are taken with respect to forward/backward Gaussian slots, not that initial-root coordinate. Equivalently one can use the finite Gaussian conditioning theorem with an independent bounded root. Fixed-program moments and the needed response derivatives remain valid.

The changed estimates are

\[
\|W_k^{(3)}\|_\infty,\ |\delta_{a,k}^{(2)}|
\le C(B_0+T),\qquad
\mathbb E\eta_{a,k}^2\le C(B_0+T)^2.
\]

The backward learned-memory row sum is now \(O(T)\), not \(O(T^3)\). Differentiating the readout still contributes \(CTV_k\), since its independent initial root has zero derivative in every forward Gaussian slot. Differentiating the second-layer backpropagated field contributes at most \(C(B_0+T)V_k\). Thus

\[
\mathcal C_k\le CT
\exp[CT(1+\mathcal A_{k-1})+CT^2],
\]

\[
V_k\le\max\{V_{k-1},
1+C(B_0+T)(\mathcal C_k+CT)V_{k-1}\},
\qquad
\mathcal A_k\le C(B_0+T)V_k.
\]

Take an \(O(1+B_0)\) cap for \(\mathcal A_k\), an \(O(T)\) cap for \(\mathcal C_k\), and choose \(T_0>0\) so the coefficient of \(V_{k-1}\) in the second alternative is at most \(1/2\). The same causal induction gives \(V_k\le2\), bounded response row sums, and a mesh-uniform Gaussian tail for \(P_{a,k}\). All existence/convergence bridges follow. The initial readout discrepancy is zero because the oracle uses the actual sampled root.

This does **not** retain the earlier \(t^2\) leading hidden displacement or the old proof of nonconstant kernel. With a nonzero initial readout, hidden training usually begins at order \(t\). Those strict conclusions require a separate calculation. Also, unbounded \(O(1)\) Gaussian initial readout is not covered by this bounded-readout proof; its supremum and population essential supremum are unbounded, so additional localization is needed.

The safe primary claim is therefore: arbitrary positive finite first/second initialization scales, any polynomially vanishing Gaussian rescaled readout, and positive finite converging layer learning multipliers preserve the full local-limit proof; bounded nonvanishing iid readout preserves local existence/convergence by the explicitly modified bootstrap, but is a different initial-state theorem.
