# Two hidden layers: a complete proof of the joint width and learning-rate limit

We consider one input, equal to (1), and target (1). At width (n), the first preactivation (z^{(1)}=W^{(1)}) and output weight (W^{(3)}) are vectors in (mathbb R^n), and (W^{(2)}) is an (n)-by-(n) matrix. Throughout, (W^{(3)}) means the rescaled output weight. Put

\[
h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
h^{(2)}=\phi(z^{(2)}),\qquad \phi(s)=\arctan s,
\]
\[
f_n=\frac{(W^{(3)})^\top h^{(2)}}n,\qquad r_n=f_n-1,\qquad L_n=r_n^2.
\]

All initial entries are independent, with
\[
z_{0,i}^{(1)}\sim N(0,1),\quad W_{0,ji}^{(2)}\sim N(0,1/n),\quad
W_{0,j}^{(3)}\sim N(0,1/n^2).
\]
Define the derivatives without the loss residual by
\[
\delta^{(2)}=W^{(3)}\odot\phi'(z^{(2)}),\qquad
\delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)}.
\]
Thus \(\delta^{(\ell)}=n\,\partial f_n/\partial z^{(\ell)}\). The exact GD being analyzed is
\[
\begin{aligned}
z_{k+1}^{(1)}&=z_k^{(1)}-2\eta_n r_{n,k}\delta_k^{(1)},\\
W_{k+1}^{(2)}&=W_k^{(2)}-\frac{2\eta_n r_{n,k}}n\delta_k^{(2)}(h_k^{(1)})^\top,\\
W_{k+1}^{(3)}&=W_k^{(3)}-2\eta_n r_{n,k}h_k^{(2)}.
\end{aligned} \tag{1}
\]
We use the clock \(t=k\eta_n\), interpolate these three parameters linearly, and recompute the other network quantities from them. The proof applies whenever \(\eta_n\sqrt n\to0\), in particular to \(\eta_n=n^{-2}\).

We will construct one deterministic population evolution, prove that every fixed finite collection of its forward and backward measurements is the limit of the corresponding finite-network measurements, and prove uniform convergence of predictions, losses, and all three kernel blocks on every finite time interval. We also prove convergence of the two hidden trajectory laws and their integrated squared speeds. At small positive times both hidden layers move, the activation remains non-affine on their distributions, and the kernel changes.

Capital letters \(Z^{(\ell)},H^{(\ell)},X^{(1)}\) denote individual population coordinates. We keep \(W^{(2)},W^{(3)},\delta^{(\ell)}\) for their population counterparts, explicitly identifying when we have moved to population quantities. An expectation always concerns coordinates belonging to the same layer. For a scalar population variable \(V\), write \(\|V\|_{L^2}=(\mathbb E V^2)^{1/2}\); finite vectors always use \(\|v\|_2/\sqrt n\), with the width normalization visible.

First consider the continuous finite-width flow associated with (1). Set
\[
F(s)=s+s^3/3,\qquad x^{(1)}=F(z^{(1)}).
\]
Since \(F'(s)\phi'(s)=1\), this flow becomes
\[
\begin{aligned}
\dot x^{(1)}&=-2r_n(W^{(2)})^\top\delta^{(2)},\\
\dot W^{(2)}&=-\frac{2r_n}{n}\delta^{(2)}(h^{(1)})^\top,\\
\dot W^{(3)}&=-2r_nh^{(2)}.
\end{aligned} \tag{2}
\]
The change of coordinates is exact for the flow. Euler with proof mesh \(\Delta\) means replacing each derivative in (2) by its forward difference. In particular,
\[
x_{k+1}^{(1)}=x_k^{(1)}-2\Delta r_{n,k}(W_k^{(2)})^\top\delta_k^{(2)}.
\tag{3}
\]
This is Euler for the transformed flow; transforming the GD iterates in (1) produces an additional defect, estimated below.

Iterating the Euler matrix update gives
\[
W_k^{(2)}=W_0^{(2)}-\frac{2\Delta}{n}
\sum_{s<k}r_{n,s}\delta_s^{(2)}(h_s^{(1)})^\top.
\tag{4}
\]
Consequently, for any appropriate vectors \(v,u\),
\[
W_k^{(2)}v=W_0^{(2)}v-2\Delta\sum_{s<k}r_{n,s}\delta_s^{(2)}
\frac{(h_s^{(1)})^\top v}{n},
\tag{5}
\]
\[
(W_k^{(2)})^\top u=(W_0^{(2)})^\top u-2\Delta\sum_{s<k}r_{n,s}h_s^{(1)}
\frac{(\delta_s^{(2)})^\top u}{n}.
\tag{6}
\]
Thus training adds a finite sum of rank-one matrices. At fixed \(\Delta\) and \(T\), only finitely many initial-matrix calls and scalar contractions need to be understood.

There is a logical detail here: the empirical coefficients in (5)–(6) are random. We first analyze an auxiliary finite system, the oracle, using deterministic population residuals and contractions in their place. Those numbers will be constructed below from the initial population action; they are not assumptions about the empirical network. We then prove that its empirical contractions approach the supplied numbers, and compare it with the empirical-feedback Euler system.

The matrix calculation needed for this construction is elementary Gaussian conditioning. For example, the first forward call is
\[
z_0^{(2)}=W_0^{(2)}h_0^{(1)}.
\]
Conditional on \(h_0^{(1)}\), its coordinates are independent centered Gaussians of variance \(\|h_0^{(1)}\|_2^2/n\). Hence the initial population coordinates satisfy
\[
Z_0^{(1)}\sim N(0,1),\quad H_0^{(1)}=\phi(Z_0^{(1)}),\quad
Z_0^{(2)}\sim N(0,\mathbb E[(H_0^{(1)})^2]).
\tag{7}
\]
In the oracle, \(W_0^{(3)}=0\) and \(r_0=-1\). Its first update leaves \(h_0^{(1)}\) and \(W_0^{(2)}\) unchanged and gives
\[
W_1^{(3)}=2\Delta\phi(z_0^{(2)}),\qquad
\delta_1^{(2)}=2\Delta\phi(z_0^{(2)})\odot\phi'(z_0^{(2)}).
\]
The next transpose call depends on the matrix already used in the forward pass. Define, for nonzero \(b\),
\[
P_{b^\perp}=I-\frac{bb^\top}{b^\top b}.
\]
Conditioning each Gaussian row on its observed dot product with \(h_0^{(1)}\), and then summing the rows with coefficients \(\delta_{1,j}^{(2)}\), gives
\[
(W_0^{(2)})^\top\delta_1^{(2)}
\overset d=
\frac{(z_0^{(2)})^\top\delta_1^{(2)}}{\|h_0^{(1)}\|_2^2}h_0^{(1)}
+\frac{\|\delta_1^{(2)}\|_2}{\sqrt n}P_{(h_0^{(1)})^\perp}\gamma^{(1)}.
\tag{8}
\]
Here equality is conditional in distribution, and \(\gamma^{(1)}\sim N(0,I_n)\) is independent of the preceding history. The first term supplies precisely the overlap required by
\[
(h_0^{(1)})^\top(W_0^{(2)})^\top\delta_1^{(2)}
=(z_0^{(2)})^\top\delta_1^{(2)};
\]
the second is perpendicular to \(h_0^{(1)}\).

After the first layer moves, the next initial-matrix call is \(W_0^{(2)}h_2^{(1)}\). Condition on both previous observations. Multiplying the resulting conditional matrix by \(h_2^{(1)}\) gives
\[
\begin{aligned}
W_0^{(2)}h_2^{(1)}\overset d={}&
\frac{(h_0^{(1)})^\top h_2^{(1)}}{\|h_0^{(1)}\|_2^2}z_0^{(2)}\\
&+\frac{[P_{(h_0^{(1)})^\perp}(W_0^{(2)})^\top\delta_1^{(2)}]^\top h_2^{(1)}}{\|\delta_1^{(2)}\|_2^2}\delta_1^{(2)}\\
&+\frac{\|P_{(h_0^{(1)})^\perp}h_2^{(1)}\|_2}{\sqrt n}
P_{(\delta_1^{(2)})^\perp}\gamma^{(2)}.
\end{aligned} \tag{9}
\]
The first response retains the old forward answer. The second supplies the remaining overlap required by the old transpose answer. The last term disturbs neither observation. Formula (5), with population coefficients for the oracle, then adds the learned rank-one correction to obtain its actual preactivation node.

We now prove the finite Gaussian fact needed to repeat this argument, including the case of dependent query directions. The proof below requires only empirical convergence against continuous measurements with at most quadratic growth. It does not claim convergence against arbitrary discontinuous functions.

Consider a fixed finite calculation starting from iid coordinate tuples with finite second moments, independent of \(W_0^{(2)}\). Its instructions are fixed globally Lipschitz coordinate functions, linear combinations with deterministic coefficients, and calls to \(W_0^{(2)}\) or its transpose. Root tuples may include both \(z_0^{(1)}\) and \(F(z_0^{(1)})\). Then all same-layer joint empirical laws have deterministic limits, including their second moments.

For precision, the distance between two laws used here is the smallest root-mean-square distance between random vectors having those laws, usually denoted \(\mathcal W_2\). For empirical laws, matching coordinates gives the bound
\[
\mathcal W_2\!\left(\frac1n\sum_i\delta_{v_i},\frac1n\sum_i\delta_{\widetilde v_i}\right)^2
\le\frac1n\sum_i\|v_i-\widetilde v_i\|_2^2.
\tag{10}
\]
Convergence in this distance means weak convergence together with convergence of second moments. Thus it includes all dot products of a fixed joint tuple.

First, the Gaussian matrix has a uniform operator bound with exponentially high probability. A \(1/4\)-net of the Euclidean unit sphere has at most \(9^n\) elements. Using two such nets,
\[
\mathbb P(\|W_0^{(2)}\|_{\rm op}>M)
\le 2\,9^{2n}\exp(-nM^2/8).
\tag{11}
\]
Indeed the operator norm is at most twice the largest bilinear form on these nets, and each bilinear form is \(N(0,1/n)\). Choose a fixed sufficiently large \(M\).

To avoid inverting almost-dependent query directions, temporarily add \(\varepsilon\xi\) to the input of each matrix call, where each \(\xi\) is a new independent standard Gaussian vector. Fix \(\varepsilon>0\). This is only a device for the proof; we will remove it.

Suppose previous calls have revealed
\[
W_0^{(2)}V=Y,\qquad (W_0^{(2)})^\top U=R.
\]
The columns of \(V\) are old first-layer input vectors, the columns of \(U\) are old second-layer input vectors, and \(Y,R\) contain the respective answers. Their column counts are fixed. All coordinates derived from these answers give no further information once the answers and roots are fixed. Gaussian conditioning therefore leaves
\[
W_0^{(2)}\overset d=
Y(V^\top V)^{-1}V^\top
+U(U^\top U)^{-1}R^\top P_{V^\perp}
+P_{U^\perp}\widetilde W_0^{(2)}P_{V^\perp}.
\tag{12}
\]
Here \(P_{V^\perp}=I-V(V^\top V)^{-1}V^\top\), and similarly for \(U\); terms for an empty column list are zero. The fresh matrix has independent \(N(0,1/n)\) entries. The first two terms obey both recorded equations; the remaining Gaussian matrix lies in exactly the directions that leave those equations unchanged. Orthogonal components of a centered isotropic Gaussian are independent, which proves (12), including for adaptive queries: each input is chosen from the earlier answers before its new answer is observed.

For a new right-side input \(v\), multiplication gives
\[
W_0^{(2)}v\overset d=Y\alpha_n+U\beta_n+
\frac{\|P_{V^\perp}v\|_2}{\sqrt n}P_{U^\perp}\gamma,
\tag{13}
\]
where
\[
\alpha_n=(V^\top V/n)^{-1}(V^\top v/n),\qquad
\beta_n=(U^\top U/n)^{-1}(R^\top P_{V^\perp}v/n).
\]
The transpose case exchanges the two layer populations.

Inductively, all the normalized products in these expressions converge. The perturbation guarantees invertibility of their limiting input Gram matrices: when a new column \(a+\varepsilon\xi\) is added to any old input list, conditional Gaussian second-moment calculations give
\[
\frac{\|P_{V^\perp}(a+\varepsilon\xi)\|_2^2}{n}
=\frac{\|P_{V^\perp}a\|_2^2}{n}+\varepsilon^2+o_{\mathbb P}(1).
\tag{14}
\]
The cross term has conditional variance at most \(4\varepsilon^2\|a\|_2^2/n^2\), and only a fixed number of Gaussian directions are removed. Its limiting squared distance is at least \(\varepsilon^2\). Successive Schur complements therefore stay positive; all the finite Gram inverses in (13) converge.

Consequently the response coefficients and Gaussian variance converge. The projection removes finitely many directions, and
\[
\mathbb E\!\left[\frac{\|P_{U}\gamma\|_2^2}{n}\,\middle|\,\text{history}\right]
=\frac{\operatorname{rank}(U)}n\longrightarrow0.
\tag{15}
\]
After removing this negligible projection and replacing coefficients by their limits, the new coordinates are an old coordinate function plus independent scalar Gaussians. For a bounded Lipschitz measurement, conditional empirical variance is at most a constant divided by \(n\). Its conditional mean is the old empirical average of the measurement averaged over one scalar Gaussian, which converges by the previous induction step. The conditional variance of the new squared norm is also \(O((1+\|Y\alpha_n+U\beta_n\|_2^2/n)/n)\). Thus second moments converge as well. This proves the enlarged joint \(\mathcal W_2\) convergence. Lipschitz coordinate operations preserve it, closing the induction at fixed \(\varepsilon\).

Finally couple the perturbed and unperturbed calculations using the same roots and matrix. On the event in (11) and the event that the finitely many \(\|\xi\|_2/\sqrt n\) are bounded, induction through the finite instructions gives
\[
\max_{\text{constructed }v}\frac{\|v^{\varepsilon}-v\|_2}{\sqrt n}
\le C\varepsilon,
\tag{16}
\]
where \(C\) depends on the fixed calculation but not on \(n\) or \(0<\varepsilon\le1\). Each coordinate map multiplies a difference by its fixed Lipschitz constant, and each matrix call by at most \(M\), plus the new perturbation. Both events have probability tending to one. By (10), the deterministic limiting laws for \(\varepsilon>0\) form a Cauchy family in \(\mathcal W_2\); its limit is also the limit of the unperturbed empirical laws, first taking \(n\to\infty\), then \(\varepsilon\to0\). This proves the finite Gaussian fact without assuming stability of a singular unperturbed Gram matrix.

Now we turn these compatible finite calculations into one population matrix action. Take a countable collection of initial calculations, closed under rational linear combinations, initial-matrix calls in both directions, the Lipschitz maps used above, and a countable family of bounded Lipschitz functions of finite coordinate lists that is dense among continuous functions on compact sets. Include constants, clipping at every integer level, and products with a clipped factor. Finite joint limiting laws are consistent because every union of finitely many calculations is another such calculation. They therefore define two countable random coordinate collections, one per layer. Let their probability spaces contain exactly the information generated by these coordinates.

Identify two first-layer probes whenever
\[
v\sim\widetilde v\quad\Longleftrightarrow\quad
\frac{\|v-\widetilde v\|_2^2}{n}\longrightarrow0
\quad\text{in probability},
\tag{17}
\]
and do the same separately on the second layer. The limiting mean-square distance is \(\mathbb E[(V-\widetilde V)^2]\), so these classes are precisely the corresponding population random variables, identified when equal almost surely. Define
\[
W_0^{(2)}[v]=[W_0^{(2)}v].
\]
The definition is independent of representatives because (11) gives
\[
\frac{\|W_0^{(2)}v-W_0^{(2)}\widetilde v\|_2^2}{n}
\le M^2\frac{\|v-\widetilde v\|_2^2}{n}
\]
on an event of probability tending to one. Linearity passes from the finite matrix, as does
\[
\mathbb E[(W_0^{(2)}V)^2]\le M^2\mathbb E[V^2].
\tag{18}
\]
Taking all mean-square limits extends this action uniquely to every square-integrable variable on the first-layer probability space. The density needed here follows from the included bounded coordinate functions: finite-coordinate measurable functions approximate any variable on the generated space, and bounded continuous functions approximate them in mean square. The transpose action extends the same way in the reverse direction. Passing the exact finite identity
\[
\frac{u^\top W_0^{(2)}v}{n}
=\frac{[(W_0^{(2)})^\top u]^\top v}{n}
\]
to population expectations shows that this reverse action is precisely the adjoint:
\[
\mathbb E[U\,W_0^{(2)}V]=\mathbb E[((W_0^{(2)})^*U)V].
\tag{19}
\]
Arbitrary fixed real coefficients are obtained by rational approximation; the same stability estimates identify any finite computation using them with this population construction.

On these fixed spaces the population state is \((X^{(1)},W^{(2)},W^{(3)})\). Its derived variables and dynamics are
\[
\begin{gathered}
Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\phi(Z^{(1)}),\quad
Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),\\
f=\mathbb E[W^{(3)}H^{(2)}],\quad r=f-1,\quad
\delta^{(2)}=W^{(3)}\phi'(Z^{(2)}),\\
\dot X^{(1)}=-2r(W^{(2)})^*\delta^{(2)},\qquad
\dot W^{(2)}=-2r\delta^{(2)}\otimes H^{(1)},\qquad
\dot W^{(3)}=-2rH^{(2)}.
\end{gathered} \tag{20}
\]
The rank-one action means
\[
(\delta^{(2)}\otimes H^{(1)})V
=\delta^{(2)}\mathbb E[H^{(1)}V].
\]
Initially \(X_0^{(1)}=F(Z_0^{(1)})\), the matrix action is (18), and \(W_0^{(3)}=0\). Only three evolving objects are used; the population coordinate spaces themselves are infinite dimensional.

We next prove that (20) has a unique solution at every finite time and that Euler approximates it uniformly. The same estimates will apply at finite width. Measure two population states by
\[
d=\|X^{(1)}-\widetilde X^{(1)}\|_{L^2}
+\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}.
\tag{21}
\]
At finite width replace each variable's \(L^2\) norm by its Euclidean norm divided by \(\sqrt n\); call this distance \(d_n\). The operator norm is the largest amplification of root-mean-square size.

Both \(F^{-1}\) and \(\phi\circ F^{-1}\) are 1-Lipschitz. The functions \(\phi,\phi'\) are bounded and Lipschitz. If both operator norms are at most \(M\) and both output weights are pointwise bounded by \(B\), then
\[
\begin{aligned}
\|Z^{(2)}-\widetilde Z^{(2)}\|_{L^2}
&\le (\pi/2)\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+M\|X^{(1)}-\widetilde X^{(1)}\|_{L^2},\\
\|\delta^{(2)}-\widetilde\delta^{(2)}\|_{L^2}
&\le\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}
+B\operatorname{Lip}(\phi')\|Z^{(2)}-\widetilde Z^{(2)}\|_{L^2},\\
\|(W^{(2)})^*\delta^{(2)}-(\widetilde W^{(2)})^*\widetilde\delta^{(2)}\|_{L^2}
&\le\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}\|\delta^{(2)}\|_{L^2}
+M\|\delta^{(2)}-\widetilde\delta^{(2)}\|_{L^2}.
\end{aligned} \tag{22}
\]
The output difference obeys Cauchy–Schwarz with \(|H^{(2)}|\le\pi/2\), and
\[
\|a\otimes b-\widetilde a\otimes\widetilde b\|_{\rm op}
\le\|a-\widetilde a\|_{L^2}\|b\|_{L^2}
+\|\widetilde a\|_{L^2}\|b-\widetilde b\|_{L^2}.
\]
Hence the vector field is Lipschitz in (21) on these bounded sets, with a constant independent of width.

Existence can be proved directly by iteration of the integral equations. On a sufficiently short time interval, the map \(\Theta\mapsto\Theta(0)+\int_0^t\dot\Theta(\Theta(s))\,ds\) preserves a closed set of continuous paths with the indicated bounds and contracts the supremum of (21). This set is complete: mean-square limits preserve a common pointwise bound on \(W^{(3)}\). Taking the time interval shorter than the reciprocal of the Lipschitz constant proves existence and uniqueness.

To continue the solution, differentiation of the output, using (19), gives
\[
\dot f=-2rK,\quad \dot L=-4r^2K,\qquad
K=K^{(1)}+K^{(2)}+K^{(3)},
\tag{23}
\]
where
\[
\begin{aligned}
K^{(1)}&=\mathbb E\!\left[(\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)})^2\right],\\
K^{(2)}&=\mathbb E[(H^{(1)})^2]\,\mathbb E[(\delta^{(2)})^2],\\
K^{(3)}&=\mathbb E[(H^{(2)})^2].
\end{aligned} \tag{24}
\]
These formulas also follow by differentiating along square-integrable parameter directions: the gradients of (L) in (Z^{(1)},W^{(2)},W^{(3)}) are (2r\delta^{(1)},2r\delta^{(2)}\otimes H^{(1)},2rH^{(2)}). For matrix perturbations use the Hilbert–Schmidt inner product, under which the displayed rank-one action is the gradient. The update (W^{(2)}(t)-W_0^{(2)}) lies in that space because it is the integral of rank-one actions of bounded Hilbert–Schmidt norm. Thus (20), transformed back to (Z^{(1)}), is gradient flow for this loss, with the same scaling as (1).

The chain rules used here hold along these mean-square differentiable paths: bounded scalar derivatives give convergence of difference quotients by domination, first for bounded directions and then by mean-square approximation. We are not asserting that every coordinatewise nonlinear map is differentiable in operator norm on all of (L^2).

Since \(K\ge0\), \(|r(t)|\le|r(0)|\). Therefore, on \([0,T]\),
\[
\|W^{(3)}(t)\|_\infty\le\|W^{(3)}(0)\|_\infty+\pi|r(0)|T,
\]
\[
\|\dot W^{(2)}\|_{\rm op}\le\pi|r(0)|\|W^{(3)}\|_{L^2},\qquad
\|\dot X^{(1)}\|_{L^2}\le2|r(0)|\|W^{(2)}\|_{\rm op}\|W^{(3)}\|_{L^2}.
\tag{25}
\]
These bounds prevent finite-time blow-up. At finite width, (11), the initial law of large numbers for (F(z_0^{(1)})), and (\|W_0^{(3)}\|_\infty\to0) in probability put the same bounds on an event of probability tending to one.

Let the vector-field bound and Lipschitz constant on a slightly larger bounded set be \(M_T,L_T\). One exact flow step of length \(\Delta\) differs from its Euler step by
\[
\left\|\int_t^{t+\Delta}[\dot\Theta(\Theta(s))-\dot\Theta(\Theta(t))],ds\right\|
\le \frac12L_TM_T\Delta^2.
\]
Consequently the accumulated error satisfies
\[
e_{k+1}\le(1+L_T\Delta)e_k+C_T\Delta^2,
\qquad \max_{k\Delta\le T}e_k\le C_T'\Delta.
\tag{26}
\]
To justify the bounded set for Euler, stop at a first exit. The bound proves that the (X^{(1)}) and operator components remain inside their margins. Although (21) does not control the output supremum, its update gives
\[
\|W_k^{(3)}\|_\infty\le\|W_0^{(3)}\|_\infty+
\pi\Delta\sum_{s<k}|r_s|.
\]
Up to the stop, (22) and (26) make \(|r_s|\le|r(0)|+C_T\Delta\); choose the supremum margin larger than \(\pi T(|r(0)|+1)\). For small \(\Delta\) no first exit is possible. Thus (26), also between grid times, holds for both population and finite-width Euler.

We can now define and compare the oracle precisely. Attach the word “oracle” as a subscript to its finite arrays; it denotes the auxiliary system, not another normalization. For fixed population Euler mesh \(\Delta\), all the numbers
\[
r_k=\mathbb E[W_k^{(3)}H_k^{(2)}]-1,\quad
\mathbb E[H_s^{(1)}H_k^{(1)}],\quad
\mathbb E[\delta_s^{(2)}\delta_k^{(2)}]
\tag{27}
\]
are deterministic. Start the oracle from the same (z_0^{(1)},W_0^{(2)}) as the finite network and from (W_{\mathrm{oracle},0}^{(3)}=0). In order at each step set
\[
h_{\mathrm{oracle},k}^{(1)}=\phi(F^{-1}(x_{\mathrm{oracle},k}^{(1)})),
\]
\[
z_{\mathrm{oracle},k}^{(2)}=W_0^{(2)}h_{\mathrm{oracle},k}^{(1)}
-2\Delta\sum_{s<k}r_s\delta_{\mathrm{oracle},s}^{(2)}\mathbb E[H_s^{(1)}H_k^{(1)}],
\tag{28}
\]
\[
h_{\mathrm{oracle},k}^{(2)}=\phi(z_{\mathrm{oracle},k}^{(2)}),\qquad
\delta_{\mathrm{oracle},k}^{(2)}=W_{\mathrm{oracle},k}^{(3)}\odot\phi'(z_{\mathrm{oracle},k}^{(2)}),
\]
\[
\begin{aligned}
x_{\mathrm{oracle},k+1}^{(1)}=x_{\mathrm{oracle},k}^{(1)}-2\Delta r_k
\bigg((W_0^{(2)})^\top\delta_{\mathrm{oracle},k}^{(2)}
-2\Delta\sum_{s<k}r_sh_{\mathrm{oracle},s}^{(1)}\mathbb E[\delta_s^{(2)}\delta_k^{(2)}]\bigg),\\
W_{\mathrm{oracle},k+1}^{(3)}=W_{\mathrm{oracle},k}^{(3)}-2\Delta r_kh_{\mathrm{oracle},k}^{(2)}.
\end{aligned} \tag{29}
\]
This is a fixed finite Gaussian calculation. Its output weights obey the deterministic coordinate bound (\pi\Delta\sum_{s<k}|r_s|). Hence the product defining (\delta^{(2)}) can be replaced, without changing any oracle value, by a globally Lipschitz map that clips its first argument above this bound. All other maps meet the finite Gaussian lemma. Its limiting variables are exactly the population Euler variables: this follows instruction by instruction from (5)–(6) at population level and the already constructed action (18)–(19).

Record its finite matrix memory as
\[
W_{\mathrm{oracle},k}^{(2)}=W_0^{(2)}-\frac{2\Delta}{n}\sum_{s<k}
r_s\delta_{\mathrm{oracle},s}^{(2)}(h_{\mathrm{oracle},s}^{(1)})^\top.
\]
Its actual matrix action is not exactly the oracle preactivation (28). Their difference is
\[
\begin{aligned}
W_{\mathrm{oracle},k}^{(2)}h_{\mathrm{oracle},k}^{(1)}-z_{\mathrm{oracle},k}^{(2)}
=-2\Delta\sum_{s<k}r_s\delta_{\mathrm{oracle},s}^{(2)}
\left(\frac{(h_{\mathrm{oracle},s}^{(1)})^\top h_{\mathrm{oracle},k}^{(1)}}n-
\mathbb E[H_s^{(1)}H_k^{(1)}]\right).
\end{aligned} \tag{30}
\]
The analogous backward discrepancy is the same sum with (h_{\mathrm{oracle},s}^{(1)}) multiplying the empirical-minus-population (\delta^{(2)}) contraction. These are exact identities.

Let (\zeta_n) be the largest absolute error among the finitely many contractions in (30), their backward versions, the output averages, and the squared normalized norms of the oracle vectors. The finite Gaussian result proves (\zeta_n\to0) in probability. In particular the oracle vector norms remain bounded. Put
\[
e_{n,k}=\frac{\|x_k^{(1)}-x_{\mathrm{oracle},k}^{(1)}\|_2}{\sqrt n}
+\|W_k^{(2)}-W_{\mathrm{oracle},k}^{(2)}\|_{\rm op}
+\frac{\|W_k^{(3)}-W_{\mathrm{oracle},k}^{(3)}\|_2}{\sqrt n}.
\]
Equations (22) and (30) bound every forward, backward, and residual difference by (C_{T,\Delta}(e_{n,k}+\zeta_n)). Subtracting the updates gives
\[
e_{n,k+1}\le(1+C_{T,\Delta}\Delta)e_{n,k}+C_{T,\Delta}\Delta\zeta_n.
\tag{31}
\]
Initially (e_{n,0}=\|W_0^{(3)}\|_2/\sqrt n=O_{\mathbb P}(n^{-1})). Since (N=\lceil T/\Delta\rceil) is fixed, summing this recurrence proves (\max_{k\le N}e_{n,k}\to0). We have therefore proved the actual finite Euler width limit without feeding random scalar coefficients into the Gaussian lemma.

The same argument controls any fixed finite set of extra forward and backward measurements: expand each learned-matrix use by (5) or (6), use the population contraction to construct its oracle version, and add its empirical contraction errors to (\zeta_n). There are only finitely many such errors. For continuity of these measurements, allow arbitrary finite compositions of bounded Lipschitz coordinate maps, (F^{-1}), linear combinations, and the current (W^{(2)},(W^{(2)})^*). Products use a clipped bounded factor. Induction on these operations, using (22), gives an error at most (C_{\mathrm{measurement}}d_n) for two states on the same finite space, and (C_{\mathrm{measurement}}d) on the population spaces.

Choose a countable dense collection of those measurements. For each finite list of same-layer measurements, compare its joint empirical law in (\mathcal W_2), including dot products. The action-law distance is the sum of these bounded distances with weights (2^{-j}), over a fixed enumeration of finite lists. By (26) and (31), its finite-flow versus population-flow error, for any fixed list, has the form
\[
C_T\Delta+o_{\mathbb P,n\to\infty;\,\Delta}(1)+C_T\Delta.
\tag{32}
\]
For any requested accuracy, choose a small fixed (\Delta), then take (n\to\infty). Uniform time continuity of each fixed measurement, supplied by (22) and the bounded derivatives, gives uniformity on ([0,T]). The summable weights extend this to the action-law distance. This statement also holds for any finitely many time points jointly, by appending all those measurements to the same finite oracle calculation before taking the limit.

The population evolution is autonomous on the state just constructed. To see this also at the level of its measured law, start the collection of measurements at a current state instead of at initialization, and take all their mean-square limits on each layer. These spaces are preserved by the current action and adjoint and by the coordinate operations. If two current measured laws agree, sending each measurement to its counterpart preserves every squared norm and inner product. It extends to a surjective linear isometry between the two generated spaces, commutes with the coordinate functions, intertwines the current action and adjoint, and sends (\delta^{(2)}\otimes H^{(1)}) to its counterpart. The integral iteration proving existence stays in these spaces. Uniqueness therefore identifies the future laws of the two states. Restarting at time (s) and evolving for time (t) gives the same law as evolving for (s+t); no extra historical information is required.

It remains to pass from flow to the exact GD in (1), and to justify the unbounded observables. For a single GD step let (b=-2r_n(W^{(2)})^\top\delta^{(2)}), the transformed first-layer velocity. The letter (b) is used only in the following cubic calculation. Coordinatewise,
\[
F(z^{(1)}+\eta_n\phi'(z^{(1)})\odot b)
=F(z^{(1)})+\eta_nb
+\eta_n^2z^{(1)}\odot\phi'(z^{(1)})^2\odot b^2
+\frac{\eta_n^3}{3}\phi'(z^{(1)})^3\odot b^3.
\tag{33}
\]
On the bounded state set, (\|b\|_2/\sqrt n\le C_T), hence (\|b\|_\infty\le C_T\sqrt n). Since (\sup_s|s|\phi'(s)^2<\infty), the extra terms in root-mean-square norm are at most
\[
C_T(\eta_n^2\sqrt n+\eta_n^3n).
\]
The other two parameter updates already are Euler updates. Adding the (O(\eta_n^2)) local flow error and summing the recurrence as in (26) gives
\[
\sup_{t\le T}d_n(\Theta_n^{\mathrm{GD}}(t),\Theta_n^{\mathrm{flow}}(t))
\le C_T(\eta_n+\eta_n\sqrt n+\eta_n^2n)\longrightarrow0
\tag{34}
\]
with probability tending to one. Stop first on a larger bounded set, as before. The output supremum is controlled separately by its sum of bounded activation updates and the residual bound transferred from the flow. This closes the stop. At intermediate times (33) with (0\le\eta\le\eta_n) controls the transformed coordinate of the linearly interpolated raw parameter, so (34) holds for the specified interpolation.

Here is the required control for quantities containing a possibly large backward coordinate. For this paragraph only, write (p=(W^{(2)})^\top\delta^{(2)}) at finite width and (P=(W^{(2)})^*\delta^{(2)}) in the population. This abbreviation names the same repeatedly used backward measurement, not a new network state. Equations (22), (32), and (34) show uniformly in time that the empirical joint law of ((z^{(1)},p)) converges in (\mathcal W_2) to that of ((Z^{(1)},P)). The latter laws form a compact (\mathcal W_2) family because these population variables are continuous in mean square.

Consequently the squared tails vanish uniformly:
\[
\lim_{A\to\infty}\limsup_{n\to\infty}
\mathbb P\left(\sup_{t\le T}\frac1n\sum_i p_i(t)^2\mathbf1_{|p_i(t)|>A}>\varepsilon\right)=0.
\tag{35}
\]
For completeness, if (p,P) are coupled, splitting according to (|P|\le A/2) gives
\[
\mathbb E[p^2\mathbf1_{|p|>A}]
\le4\mathbb E[(p-P)^2]+2\mathbb E[P^2\mathbf1_{|P|>A/2}].
\]
Compactness gives uniformly small population tails by a finite cover; the uniform (\mathcal W_2) convergence then proves (35).

Clip (p) to ([-A,A]). For fixed (A), both (phi'(z^{(1)})\operatorname{clip}_A(p)) and (phi'(z^{(1)})^2\operatorname{clip}_A(p)) are Lipschitz measurements. Their squared errors from the unclipped fields are bounded by the tail in (35), since (|\phi'|\le1). Applying (W^{(2)}) to their difference multiplies its root-mean-square size by at most its operator bound. Thus, first taking (n\to\infty), then (A\to\infty), proves uniform convergence of the three kernel blocks in (24), with finite expectations replaced by normalized coordinate sums. It also proves convergence of the squared speeds computed from
\[
\dot Z^{(1)}=-2r\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)},
\]
\[
\dot Z^{(2)}=-2r\left\{\mathbb E[(H^{(1)})^2]\delta^{(2)}
+W^{(2)}[\phi'(Z^{(1)})^2(W^{(2)})^*\delta^{(2)}]\right\}.
\tag{36}
\]
The prediction and loss converge uniformly as well, directly from bounded activations and the output-weight bound.

For GD, the first-layer interpolated slope is its gradient at the left endpoint. The derivative of (z^{(2)}=W^{(2)}\phi(z^{(1)})) uses those constant parameter slopes and the current interpolated activation. To compare it with (36) at the endpoint, on (|p_i|\le A) the change in (phi'(z_i^{(1)})) times its first-layer slope is bounded by (C_T\eta_nA^2); on the complement both terms are bounded by (C_T|p_i|). The other product-rule errors are (O(\eta_n)) in root-mean-square norm by bounded matrix slopes. Equation (35), then (n\to\infty) at fixed (A), then (A\to\infty), proves
\[
\int_0^T\frac{\|\partial_tz_n^{(\ell),\mathrm{GD}}(t)\|_2^2}{n},dt
\longrightarrow\int_0^T\mathbb E[(\dot Z^{(\ell)}(t))^2],dt,
\qquad \ell=1,2.
\tag{37}
\]
These statements are in probability. No fourth-moment assumption on the evolving backward field is needed.

For the trajectory-law claim, use (\mathcal W_2) on continuous scalar paths with the supremum distance. If (I_\pi z) is polygonal interpolation on a partition of mesh at most (a), absolute continuity and Cauchy–Schwarz give
\[
\|z-I_\pi z\|_\infty^2\le4a\int_0^T|\dot z(t)|^2,dt.
\tag{38}
\]
After coordinate averaging, (37) bounds the empirical distance to this finite-grid representation by (O_{\mathbb P}(\sqrt a)). The population bound is identical; mean-square continuous velocities admit absolutely continuous sample paths by integrating a jointly measurable version and applying Fubini. At fixed partition, joint grid-law convergence follows from (32) and (34), including second moments. Polygonal interpolation is a continuous linear map of the finite grid vector. Let (n\to\infty) at fixed partition, then (a\to0) in (38). This proves, separately for the two layers,
\[
\frac1n\sum_i\delta_{z_{n,i}^{(\ell),\mathrm{GD}}(\cdot)}
\longrightarrow\operatorname{Law}(Z^{(\ell)}(\cdot))
\quad\text{in }\mathcal W_2(C([0,T])).
\tag{39}
\]

Finally we verify the claimed feature learning. Only for this calculation define the following fixed initial population quantities, each of which recurs:
\[
m=\mathbb E[(H_0^{(1)})^2]>0,\quad
U=H_0^{(2)}\phi'(Z_0^{(2)}),\quad \nu=\mathbb E[U^2]>0,\quad
P_0=(W_0^{(2)})^*U.
\]
The row-conditioning calculation (8), without its (2\Delta) factor, gives
\[
P_0=\frac{\mathbb E[Z_0^{(2)}U]}mH_0^{(1)}+\sqrt\nu\,\Gamma^{(1)},
\tag{40}
\]
where (\Gamma^{(1)}\sim N(0,1)) is independent of the first-layer root. Put
\[
d=\mathbb E[(\phi'(Z_0^{(1)})P_0)^2]>0,\qquad
S_0=mU+W_0^{(2)}[\phi'(Z_0^{(1)})^2P_0].
\]
The positivity of (d) follows from the positive independent Gaussian variance in (40) and (phi'>0). By adjunction,
\[
\mathbb E[US_0]=m\nu+d>0,
\tag{41}
\]
so (S_0\ne0) in mean square.

Initially (r=-1) and (W^{(3)}=0). Dividing the integral equations (20) by successive powers of (t), using bounded scalar derivatives and mean-square continuity, gives
\[
\begin{aligned}
W^{(3)}(t)&=2tH_0^{(2)}+O_{L^2}(t^2),&
\delta^{(2)}(t)&=2tU+O_{L^2}(t^2),\\
Z^{(1)}(t)-Z_0^{(1)}&=2t^2\phi'(Z_0^{(1)})P_0+o_{L^2}(t^2),\\
W^{(2)}(t)-W_0^{(2)}&=2t^2U\otimes H_0^{(1)}+o_{\rm op}(t^2),\\
Z^{(2)}(t)-Z_0^{(2)}&=2t^2S_0+o_{L^2}(t^2).
\end{aligned} \tag{42}
\]
To check the orders directly, (25) first gives (W^{(3)}=O(t)), then (delta^{(2)}=O(t)), and hence (X^{(1)}-X_0^{(1)},W^{(2)}-W_0^{(2)},Z^{(2)}-Z_0^{(2)}=O(t^2)). Substitution into the output-weight and derivative equations gives the first line. Substitution once more gives the remaining lines. For example (dot X^{(1)}(t)/t\to4P_0), and applying the bounded derivative of (F^{-1}) gives the first preactivation expansion.

Let (k_3=\mathbb E[(H_0^{(2)})^2]>0). Equations (24), (41), and (42) yield
\[
K^{(1)}(t)=4dt^2+o(t^2),\quad K^{(2)}(t)=4m\nu t^2+o(t^2),
\]
\[
K^{(3)}(t)=k_3+4(m\nu+d)t^2+o(t^2),\quad
K(t)=k_3+8(m\nu+d)t^2+o(t^2).
\tag{43}
\]
The two squared displacements have leading terms (4dt^4) and (4\mathbb E[S_0^2]t^4); their squared speeds have leading terms (16dt^2) and (16\mathbb E[S_0^2]t^2). Thus both hidden layers move and every kernel block has a positive integral on sufficiently short nonzero intervals. Also
\[
f(t)=2k_3t+o(t),\qquad L(t)=1-4k_3t+o(t).
\]
Both initial preactivation laws in (7) are nondegenerate Gaussians. Their variances remain positive by mean-square continuity. For either layer the error of the best affine fit to the activation is
\[
\operatorname{Var}(\phi(Z^{(\ell)}))-
\frac{\operatorname{Cov}(Z^{(\ell)},\phi(Z^{(\ell)}))^2}{\operatorname{Var}(Z^{(\ell)})}.
\tag{44}
\]
It is initially positive: equality would force (arctan) to agree with an affine function on a full-support Gaussian law and hence everywhere by continuity. The moments in (44) are continuous in mean square because (phi) is bounded and Lipschitz. This error therefore remains positive for both layers on a common interval ([0,T_*]). Equations (34), (37), (39), and (43) establish all the asserted convergence and feature-learning claims.
