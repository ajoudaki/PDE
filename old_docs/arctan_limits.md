# Arctangent limits with a tiny stored readout

This chapter proves two joint width and learning-rate limits for one input
\(x=1\), one target \(y=1\), and \(\phi(z)=\arctan z\). The two-hidden-layer
result is global on every fixed finite physical interval. The
three-hidden-layer result holds on an explicit positive local interval.

All conventions specialize the shared [notation contract](NOTATION.md).

Here \(L\) counts hidden layers, \(m=d=1\), and all hidden widths equal
\(n\). The loss is \(\mathcal L_n=(f_n-1)^2\). The block mobilities are
\(n,1,\ldots,1,n\), so all fixed mobility multipliers
\(\kappa_\ell\) equal one. Initial first weights have law \(N(0,1)\),
hidden entries have law \(N(0,1/n)\), and stored readout entries have law
\(N(0,n^{-2})\); the limiting initial readout is zero.

Finite hidden coordinates are \(z^{(\ell)},h^{(\ell)}\), and population
coordinates are \(Z^{(\ell)},H^{(\ell)}\). Every population contraction is
within one layer \(\Omega_\ell\); no neuron pairing across layers is used.
A finite transpose is \(T\), while a population adjoint is \(*\).
The state distances below compare objects on the same underlying spaces.
Between widths, convergence is of measured laws, not an operator-norm
identification between different spaces. Population matrix actions can
be bounded without being Hilbert–Schmidt. Their trained increments are
integrals of rank-one actions
\[
(U\otimes V)g=U\,\mathbb E_{\ell-1}[Vg],
\qquad U\in L^2(\Omega_\ell),\ V,g\in L^2(\Omega_{\ell-1}),
\]
whose finite representative is \(uv^T/n\).
Every finite norm is an ordinary Euclidean, Frobenius, or operator norm;
the factors \(1/\sqrt n\) and \(1/n\) are displayed. The finite
parameter metric generating the stated mobilities is
\[
\frac{\|dz^{(1)}\|_2^2}{n}
+\sum_{\ell=2}^L\|dW^{(\ell)}\|_{\rm F}^2
+\frac{\|dW^{(L+1)}\|_2^2}{n}.
\]

Physical time is \(t\), the actual GD step is \(\eta_n\), and \(\Delta\)
is only a proof mesh. For L2 assume \(\eta_n\sqrt n\to0\); for L3 take
\(\eta_n=n^{-2}\). Raw weights are linearly interpolated and all hidden
quantities are recomputed from those weights. The exact continuous
coordinate change is \(F(z)=z+z^3/3\). In L3 the feature clock
\(ds/dt=2(1-f)=-2r\) is used only on the proved positive-clock interval.
Neither transformation changes the definition of raw GD.

The internal proof dependencies are: [global L2 proof](#l2-global);
[local L3 statement](#l3-local), [Gaussian sources](#l3-source),
[common actions](#l3-actions), [response bounds](#l3-bootstrap),
[clipping and GD bridge](#l3-bridge), [gradient structure](#l3-gradient),
and [feature learning](#l3-features).

<a id="l2-global"></a>

## 1. Global theorem for two hidden layers

We consider one input, equal to \(1\), and target \(1\). At width \(n\), the first preactivation \(z^{(1)}=W^{(1)}\) and output weight \(W^{(3)}\) are vectors in \(\mathbb R^n\), and \(W^{(2)}\in\mathbb R^{n\times n}\). Throughout, \(W^{(3)}\) is the stored readout with the initialization stated below. Put

\[
h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
h^{(2)}=\phi(z^{(2)}),\qquad \phi(s)=\arctan s,
\]
\[
f_n=\frac{(W^{(3)})^T h^{(2)}}n,\qquad r_n=f_n-1,\qquad \mathcal L_n=r_n^2.
\]

All initial entries are independent, with
\[
z_{0,i}^{(1)}\sim N(0,1),\quad W_{0,ji}^{(2)}\sim N(0,1/n),\quad
W_{0,j}^{(3)}\sim N(0,1/n^2).
\]
Define the derivatives without the loss residual by
\[
\delta^{(2)}=W^{(3)}\odot\phi'(z^{(2)}),\qquad
\delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)}.
\]
Thus \(\delta^{(\ell)}=n\,\partial f_n/\partial z^{(\ell)}\). The exact GD being analyzed is
\[
\begin{aligned}
z_{k+1}^{(1)}&=z_k^{(1)}-2\eta_n r_{n,k}\delta_k^{(1)},\\
W_{k+1}^{(2)}&=W_k^{(2)}-\frac{2\eta_n r_{n,k}}n\delta_k^{(2)}(h_k^{(1)})^T,\\
W_{k+1}^{(3)}&=W_k^{(3)}-2\eta_n r_{n,k}h_k^{(2)}.
\end{aligned} \tag{L2.1}
\]
We use the clock \(t=k\eta_n\), interpolate these three parameters linearly, and recompute the other network quantities from them. The proof applies whenever \(\eta_n\sqrt n\to0\), in particular to \(\eta_n=n^{-2}\).

We will construct one deterministic population evolution, prove that every fixed finite collection of its forward and backward measurements is the limit of the corresponding finite-network measurements, and prove uniform convergence of predictions, losses, and all three kernel blocks on every finite time interval. We also prove convergence of the two hidden trajectory laws and their integrated squared speeds. At small positive times both hidden layers move, the activation remains non-affine on their distributions, and the kernel changes.

**Theorem 1 (global compact-time joint limit).** For every fixed
\(T<\infty\) and every positive step sequence satisfying
\(\eta_n\sqrt n\to0\), the raw GD interpolant in (L2.1) and the finite
gradient flow with the same initialization have the same deterministic
population limit on \([0,T]\). On their common finite space their state
distance (L2.21), with finite Euclidean norms divided by \(\sqrt n\), tends
to zero uniformly in time in probability. Across widths the convergence
is in joint measured laws: every fixed finite same-layer list of the
measurements defined below converges uniformly in time in
\(\mathcal W_2\), with finitely many specified times also allowed jointly.
The conclusions include prediction, loss, all three kernel blocks,
hidden preactivation and feature path laws in
\(\mathcal W_2(C([0,T]))\) for the supremum metric, and their integrated
squared speeds. The population flow exists uniquely for every finite
time and restarts from every reached state. Both hidden layers move,
the total kernel changes, and the activation has strictly positive
best-affine-fit error on a common initial interval. Compact-time
convergence makes no assertion uniform over an arbitrary growing \(T_n\).

The proof first constructs the Gaussian action and its adjoint, then
the global population flow. A fixed proof mesh separates width
convergence from continuous-time approximation. The exact cubic defect
finally links this proof mesh to raw GD.

Capital \(Z^{(\ell)},H^{(\ell)},X^{(1)}\) denote population coordinates.
For \(\ell=1,2\), write
\(\mathcal H_\ell=L^2(\Omega_\ell)\) and
\(\mathbb E_\ell\) for expectation on that layer.
The population types are
\(X^{(1)}\in\mathcal H_1\),
\(W^{(2)}:\mathcal H_1\to\mathcal H_2\), and
\(W^{(3)}\in\mathcal H_2\);
\(\delta^{(\ell)}\in\mathcal H_\ell\) is the population backward
coordinate when population variables are in use.
Unsubscripted \(L^2\) norms in the estimates refer to the displayed
variable's layer. Generic Gaussian conditioning expectations refer to
the probability space of that calculation. Finite vector sizes always
remain \(\|v\|_2/\sqrt n\).

### 1.1 Transformed flow and exact matrix memory

First consider the continuous finite-width flow associated with (L2.1). Set
\[
F(s)=s+s^3/3,\qquad x^{(1)}=F(z^{(1)}).
\]
Since \(F'(s)\phi'(s)=1\), this flow becomes
\[
\begin{aligned}
\dot x^{(1)}&=-2r_n(W^{(2)})^T\delta^{(2)},\\
\dot W^{(2)}&=-\frac{2r_n}{n}\delta^{(2)}(h^{(1)})^T,\\
\dot W^{(3)}&=-2r_nh^{(2)}.
\end{aligned} \tag{L2.2}
\]
The change of coordinates is exact for the flow. Euler with proof mesh \(\Delta\) means replacing each derivative in (L2.2) by its forward difference. In particular,
\[
x_{k+1}^{(1)}=x_k^{(1)}-2\Delta r_{n,k}(W_k^{(2)})^T\delta_k^{(2)}.
\tag{L2.3}
\]
This is Euler for the transformed flow; transforming the GD iterates in (L2.1) produces an additional defect, estimated below.

Iterating the Euler matrix update gives
\[
W_k^{(2)}=W_0^{(2)}-\frac{2\Delta}{n}
\sum_{s<k}r_{n,s}\delta_s^{(2)}(h_s^{(1)})^T.
\tag{L2.4}
\]
Consequently, for any appropriate vectors \(v,u\),
\[
W_k^{(2)}v=W_0^{(2)}v-2\Delta\sum_{s<k}r_{n,s}\delta_s^{(2)}
\frac{(h_s^{(1)})^T v}{n},
\tag{L2.5}
\]
\[
(W_k^{(2)})^T u=(W_0^{(2)})^T u-2\Delta\sum_{s<k}r_{n,s}h_s^{(1)}
\frac{(\delta_s^{(2)})^T u}{n}.
\tag{L2.6}
\]
Thus training adds a finite sum of rank-one matrices. At fixed \(\Delta\) and \(T\), only finitely many initial-matrix calls and scalar contractions need to be understood.

There is a logical detail here: the empirical coefficients in (L2.5)–(L2.6) are random. We first analyze an auxiliary finite system, the oracle, using deterministic population residuals and contractions in their place. Those numbers will be constructed below from the initial population action; they are not assumptions about the empirical network. We then prove that its empirical contractions approach the supplied numbers, and compare it with the empirical-feedback Euler system.

<a id="l2-gaussian"></a>

### 1.2 Adaptive Gaussian actions and singular queries

The matrix calculation needed for this construction is elementary Gaussian conditioning. For example, the first forward call is
\[
z_0^{(2)}=W_0^{(2)}h_0^{(1)}.
\]
Conditional on \(h_0^{(1)}\), its coordinates are independent centered Gaussians of variance \(\|h_0^{(1)}\|_2^2/n\). Hence the initial population coordinates satisfy
\[
Z_0^{(1)}\sim N(0,1),\quad H_0^{(1)}=\phi(Z_0^{(1)}),\quad
Z_0^{(2)}\sim N(0,\mathbb E_1[(H_0^{(1)})^2]).
\tag{L2.7}
\]
In the oracle, \(W_0^{(3)}=0\) and \(r_0=-1\). Until the oracle comparison below, the vectors in these first-call examples are oracle vectors. Its first update leaves \(h_0^{(1)}\) and \(W_0^{(2)}\) unchanged and gives
\[
W_1^{(3)}=2\Delta\phi(z_0^{(2)}),\qquad
\delta_1^{(2)}=2\Delta\phi(z_0^{(2)})\odot\phi'(z_0^{(2)}).
\]
The next transpose call depends on the matrix already used in the forward pass. Define, for nonzero \(b\),
\[
P_{b^\perp}=I-\frac{bb^T}{b^T b}.
\]
Conditioning each Gaussian row on its observed dot product with \(h_0^{(1)}\), and then summing the rows with coefficients \(\delta_{1,j}^{(2)}\), gives
\[
(W_0^{(2)})^T\delta_1^{(2)}
\overset d=
\frac{(z_0^{(2)})^T\delta_1^{(2)}}{\|h_0^{(1)}\|_2^2}h_0^{(1)}
+\frac{\|\delta_1^{(2)}\|_2}{\sqrt n}P_{(h_0^{(1)})^\perp}\gamma^{(1)}.
\tag{L2.8}
\]
Here equality is conditional in distribution, and \(\gamma^{(1)}\sim N(0,I_n)\) is independent of the preceding history. The first term supplies precisely the overlap required by
\[
(h_0^{(1)})^T(W_0^{(2)})^T\delta_1^{(2)}
=(z_0^{(2)})^T\delta_1^{(2)};
\]
the second is perpendicular to \(h_0^{(1)}\).

The next update is
\[
x_2^{(1)}=x_0^{(1)}-2\Delta r_1(W_0^{(2)})^T\delta_1^{(2)},\qquad
h_2^{(1)}=\phi(F^{-1}(x_2^{(1)})),
\]
where \(r_1=2\Delta\mathbb E_2[\phi(Z_0^{(2)})^2]-1\).
Thus the next initial-matrix call is \(W_0^{(2)}h_2^{(1)}\). Condition on both previous observations. Multiplying the resulting conditional matrix by \(h_2^{(1)}\) gives
\[
\begin{aligned}
W_0^{(2)}h_2^{(1)}\overset d={}&
\frac{(h_0^{(1)})^T h_2^{(1)}}{\|h_0^{(1)}\|_2^2}z_0^{(2)}\\
&+\frac{[P_{(h_0^{(1)})^\perp}(W_0^{(2)})^T\delta_1^{(2)}]^T h_2^{(1)}}{\|\delta_1^{(2)}\|_2^2}\delta_1^{(2)}\\
&+\frac{\|P_{(h_0^{(1)})^\perp}h_2^{(1)}\|_2}{\sqrt n}
P_{(\delta_1^{(2)})^\perp}\gamma^{(2)}.
\end{aligned} \tag{L2.9}
\]
Here \(\gamma^{(2)}\sim N(0,I_n)\) is independent of the previous history. The denominators in (L2.8)–(L2.9) are positive almost surely for \(\Delta>0\), because the initial Gaussians are nondegenerate and \(\phi'(s)>0\). The first response retains the old forward answer. The second supplies the remaining overlap required by the old transpose answer. The last term disturbs neither observation. Formula (L2.5), with population coefficients for the oracle, then adds the learned rank-one correction to obtain its actual preactivation node.

We now prove the finite Gaussian fact needed to repeat this argument, including the case of dependent query directions. The proof below requires only empirical convergence against continuous measurements with at most quadratic growth. It does not claim convergence against arbitrary discontinuous functions.

Consider a fixed finite calculation starting from iid coordinate tuples with finite second moments, independent of \(W_0^{(2)}\). Its instructions are fixed globally Lipschitz coordinate functions, linear combinations with deterministic coefficients, and calls to \(W_0^{(2)}\) or its transpose. Root tuples may include both \(z_0^{(1)}\) and \(F(z_0^{(1)})\). Then all same-layer joint empirical laws have deterministic limits, including their second moments.

For precision, the distance between two laws used here is the smallest root-mean-square distance between random vectors having those laws, usually denoted \(\mathcal W_2\). For empirical laws, matching coordinates gives the bound
\[
\mathcal W_2\!\left(\frac1n\sum_i\delta_{v_i},\frac1n\sum_i\delta_{\widetilde v_i}\right)^2
\le\frac1n\sum_i\|v_i-\widetilde v_i\|_2^2.
\tag{L2.10}
\]
Convergence in this distance means weak convergence together with convergence of second moments. Thus it includes all dot products of a fixed joint tuple.

First, the Gaussian matrix has a uniform operator bound with exponentially high probability. A \(1/4\)-net of the Euclidean unit sphere has at most \(9^n\) elements. Using two such nets,
\[
\mathbb P(\|W_0^{(2)}\|_{\rm op}>M)
\le 2\,9^{2n}\exp(-nM^2/8).
\tag{L2.11}
\]
Indeed the operator norm is at most twice the largest bilinear form on these nets, and each bilinear form is \(N(0,1/n)\). Choose a fixed sufficiently large \(M\).

To avoid inverting almost-dependent query directions, temporarily add \(\varepsilon\xi\) to the input of each matrix call, where each \(\xi\) is a new independent standard Gaussian vector. Fix \(\varepsilon>0\). This is only a device for the proof; we will remove it.

Suppose previous calls have revealed
\[
W_0^{(2)}V=Y,\qquad (W_0^{(2)})^T U=R.
\]
The columns of \(V\) are old first-layer input vectors, the columns of \(U\) are old second-layer input vectors, and \(Y,R\) contain the respective answers. Their column counts are fixed. All coordinates derived from these answers give no further information once the answers and roots are fixed. Gaussian conditioning therefore leaves
\[
W_0^{(2)}\overset d=
Y(V^T V)^{-1}V^T
+U(U^T U)^{-1}R^T P_{V^\perp}
+P_{U^\perp}\widetilde W_0^{(2)}P_{V^\perp}.
\tag{L2.12}
\]
Here \(P_{V^\perp}=I-V(V^T V)^{-1}V^T\), and similarly for \(U\); terms for an empty column list are zero. The fresh matrix has independent \(N(0,1/n)\) entries. The first two terms obey both recorded equations; the remaining Gaussian matrix lies in exactly the directions that leave those equations unchanged. Orthogonal components of a centered isotropic Gaussian are independent, which proves (L2.12), including for adaptive queries: each input is chosen from the earlier answers before its new answer is observed.

For a new right-side input \(v\), multiplication gives
\[
W_0^{(2)}v\overset d=Y\alpha_n+U\beta_n+
\frac{\|P_{V^\perp}v\|_2}{\sqrt n}P_{U^\perp}\gamma,
\tag{L2.13}
\]
where
\[
\alpha_n=(V^T V/n)^{-1}(V^T v/n),\qquad
\beta_n=(U^T U/n)^{-1}(R^T P_{V^\perp}v/n).
\]
The transpose case exchanges the two layer populations.

The induction statement is joint \(\mathcal W_2\) convergence of every finite tuple of previously constructed vectors on each layer. Equivalently, the average of any continuous measurement \(\psi\) with
\[
|\psi(s)|\le C(1+\|s\|_2^2)
\]
converges to its population expectation. The choices \(\psi(s)=s^2\) and \(\psi(s,t)=st\) give the required squared norms and contractions. Revealing each fresh input noise first extends the old tuple by independent Gaussian coordinates; conditional averaging proves this extension exactly as for the fresh output noise below. Thus all the normalized products in (L2.13) converge. The perturbation guarantees invertibility of their limiting input Gram matrices: when a new column \(a+\varepsilon\xi\) is added to any old input list, conditional Gaussian second-moment calculations give
\[
\frac{\|P_{V^\perp}(a+\varepsilon\xi)\|_2^2}{n}
=\frac{\|P_{V^\perp}a\|_2^2}{n}+\varepsilon^2+o_{\mathbb P}(1).
\tag{L2.14}
\]
The cross term has conditional variance at most \(4\varepsilon^2\|a\|_2^2/n^2\), and only a fixed number of Gaussian directions are removed. Its limiting squared distance is at least \(\varepsilon^2\). Successive Schur complements therefore stay positive; all the finite Gram inverses in (L2.13) converge.

Consequently the response coefficients and Gaussian variance converge. Write \(P_U=I-P_{U^\perp}\) for projection onto the column span of \(U\). This projection removes finitely many directions, and
\[
\mathbb E\!\left[\frac{\|P_{U}\gamma\|_2^2}{n}\,\middle|\,\text{history}\right]
=\frac{\operatorname{rank}(U)}n\longrightarrow0.
\tag{L2.15}
\]
After removing this negligible projection and replacing coefficients by their limits, the new coordinates are an old coordinate function plus independent scalar Gaussians. For a bounded Lipschitz measurement, conditional empirical variance is at most a constant divided by \(n\). Its conditional mean is the old empirical average of the measurement averaged over one scalar Gaussian, which converges by the previous induction step. The conditional variance of the new squared norm is also \(O((1+\|Y\alpha_n+U\beta_n\|_2^2/n)/n)\). Thus second moments converge as well. This proves the enlarged joint \(\mathcal W_2\) convergence. Lipschitz coordinate operations preserve it, closing the induction at fixed \(\varepsilon\).

Finally couple the perturbed and unperturbed calculations using the same roots and matrix. On the event in (L2.11) and the event that the finitely many \(\|\xi\|_2/\sqrt n\) are bounded, induction through the finite instructions gives
\[
\max_{\text{constructed }v}\frac{\|v^{\varepsilon}-v\|_2}{\sqrt n}
\le C\varepsilon,
\tag{L2.16}
\]
where \(C\) depends on the fixed calculation but not on \(n\) or \(0<\varepsilon\le1\). Each coordinate map multiplies a difference by its fixed Lipschitz constant, and each matrix call by at most \(M\), plus the new perturbation. Both events have probability tending to one. By (L2.10), the deterministic limiting laws for \(\varepsilon>0\) form a Cauchy family in \(\mathcal W_2\); its limit is also the limit of the unperturbed empirical laws, first taking \(n\to\infty\), then \(\varepsilon\to0\). This proves the finite Gaussian fact without assuming stability of a singular unperturbed Gram matrix.

### 1.3 Common population actions and their adjoints

Now we turn these compatible finite calculations into one population matrix action. Take a countable collection of initial calculations, closed under rational linear combinations, initial-matrix calls in both directions, the Lipschitz maps used above, and a countable family of bounded Lipschitz functions of finite coordinate lists that is dense among continuous functions on compact sets. Include constants, clipping at every integer level, and products of bounded globally Lipschitz factors. In every such product, clip each factor that is not already bounded; all coordinate instructions in this collection must be globally Lipschitz. Finite joint limiting laws are consistent because every union of finitely many calculations is another such calculation. They therefore define two countable random coordinate collections, one per layer. Let their probability spaces contain exactly the information generated by these coordinates.

Identify two first-layer probes whenever
\[
v\sim\widetilde v\quad\Longleftrightarrow\quad
\frac{\|v-\widetilde v\|_2^2}{n}\longrightarrow0
\quad\text{in probability},
\tag{L2.17}
\]
and do the same separately on the second layer. The limiting mean-square distance is \(\mathbb E[(V-\widetilde V)^2]\), so these classes are precisely the corresponding population random variables, identified when equal almost surely. Define
\[
W_0^{(2)}[v]=[W_0^{(2)}v].
\]
The definition is independent of representatives because (L2.11) gives
\[
\frac{\|W_0^{(2)}v-W_0^{(2)}\widetilde v\|_2^2}{n}
\le M^2\frac{\|v-\widetilde v\|_2^2}{n}
\]
on an event of probability tending to one. Linearity passes from the finite matrix, as does
\[
\mathbb E_2[(W_0^{(2)}V)^2]\le M^2\mathbb E_1[V^2].
\tag{L2.18}
\]
Taking all mean-square limits extends this action uniquely to every square-integrable variable on the first-layer probability space. The density needed here follows from the included bounded coordinate functions: finite-coordinate measurable functions approximate any variable on the generated space, and bounded continuous functions approximate them in mean square. The transpose action extends the same way in the reverse direction. Passing the exact finite identity
\[
\frac{u^T W_0^{(2)}v}{n}
=\frac{[(W_0^{(2)})^T u]^T v}{n}
\]
to population expectations shows that this reverse action is precisely the adjoint:
\[
\mathbb E_2[U\,W_0^{(2)}V]=\mathbb E_1[((W_0^{(2)})^*U)V].
\tag{L2.19}
\]
Arbitrary fixed real coefficients are obtained by rational approximation; the same stability estimates identify any finite computation using them with this population construction.

### 1.4 Global population flow and proof-mesh stability

On these fixed spaces the population state is \((X^{(1)},W^{(2)},W^{(3)})\). Its derived variables and dynamics are
\[
\begin{gathered}
Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\phi(Z^{(1)}),\quad
Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),\\
f=\mathbb E_2[W^{(3)}H^{(2)}],\quad r=f-1,\quad
\delta^{(2)}=W^{(3)}\phi'(Z^{(2)}),\\
\dot X^{(1)}=-2r(W^{(2)})^*\delta^{(2)},\qquad
\dot W^{(2)}=-2r\delta^{(2)}\otimes H^{(1)},\qquad
\dot W^{(3)}=-2rH^{(2)}.
\end{gathered} \tag{L2.20}
\]
The rank-one action means
\[
(\delta^{(2)}\otimes H^{(1)})V
=\delta^{(2)}\mathbb E_1[H^{(1)}V].
\]
Initially \(X_0^{(1)}=F(Z_0^{(1)})\), the matrix action is (L2.18), and \(W_0^{(3)}=0\). Only three evolving objects are used; the population coordinate spaces themselves are infinite dimensional.

We next prove that (L2.20) has a unique solution at every finite time and that Euler approximates it uniformly. The same estimates will apply at finite width. Measure two population states by
\[
\rho=\|X^{(1)}-\widetilde X^{(1)}\|_{L^2}
+\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}.
\tag{L2.21}
\]
At finite width the corresponding distance is explicitly
\[
\rho_n(\theta,\widetilde\theta)
=\frac{\|x^{(1)}-\widetilde x^{(1)}\|_2}{\sqrt n}
+\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+\frac{\|W^{(3)}-\widetilde W^{(3)}\|_2}{\sqrt n}.
\]
The operator norm is the ordinary Euclidean operator norm; the common
factor \(1/\sqrt n\) cancels between input and output sizes.

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
\end{aligned} \tag{L2.22}
\]
The output difference obeys Cauchy–Schwarz with \(|H^{(2)}|\le\pi/2\), and
\[
\|a\otimes b-\widetilde a\otimes\widetilde b\|_{\rm op}
\le\|a-\widetilde a\|_{L^2}\|b\|_{L^2}
+\|\widetilde a\|_{L^2}\|b-\widetilde b\|_{L^2}.
\]
Hence the vector field is Lipschitz in (L2.21) on these bounded sets, with a constant independent of width.

Existence can be proved directly by iteration of the integral equations. On a sufficiently short time interval, the map \(\Theta\mapsto\Theta(0)+\int_0^t\dot\Theta(\Theta(s))\,ds\) preserves a closed set of continuous paths with the indicated bounds and contracts the supremum of (L2.21). This set is complete: mean-square limits preserve a common pointwise bound on \(W^{(3)}\). Taking the time interval shorter than the reciprocal of the Lipschitz constant proves existence and uniqueness.

To continue the solution, differentiation of the output, using (L2.19), gives
\[
\dot f=-2rK,\quad \dot{\mathcal L}=-4r^2K,\qquad
K=K^{(1)}+K^{(2)}+K^{(3)},
\tag{L2.23}
\]
where
\[
\begin{aligned}
K^{(1)}&=\mathbb E_1\!\left[(\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)})^2\right],\\
K^{(2)}&=\mathbb E_1[(H^{(1)})^2]\,\mathbb E_2[(\delta^{(2)})^2],\\
K^{(3)}&=\mathbb E_2[(H^{(2)})^2].
\end{aligned} \tag{L2.24}
\]
Their finite representatives are
\[
K_n^{(1)}=\frac{\|\delta^{(1)}\|_2^2}{n},\quad
K_n^{(2)}=
 \frac{\|\delta^{(2)}\|_2^2}{n}
 \frac{\|h^{(1)}\|_2^2}{n},\quad
K_n^{(3)}=\frac{\|h^{(2)}\|_2^2}{n}.
\]
These formulas also follow by differentiating along square-integrable parameter directions: the gradients of \(\mathcal L\) in \(Z^{(1)},W^{(2)},W^{(3)}\) are \(2r\delta^{(1)},2r\delta^{(2)}\otimes H^{(1)},2rH^{(2)}\). For matrix perturbations the relevant inner product is defined first on rank-one changes by
\[
\langle a\otimes b,c\otimes d\rangle
=\mathbb E_2[ac]\,\mathbb E_1[bd],
\]
and extended by linearity and completion. This is the population version of the ordinary sum-of-squared-entries geometry, called the Hilbert–Schmidt geometry. In particular,
\[
\langle \delta^{(2)}\otimes H^{(1)},A\rangle
=\mathbb E_2[\delta^{(2)}\,A H^{(1)}],
\]
so the displayed rank-one action is the matrix gradient. Here \(A\) denotes a matrix-action perturbation. The update \(W^{(2)}(t)-W_0^{(2)}\) lies in that space because it is the integral of rank-one actions of bounded Hilbert–Schmidt norm. Thus (L2.20), transformed back to \(Z^{(1)}\), is gradient flow for this loss, with the same scaling as (L2.1).

The chain rules used here hold along these mean-square differentiable paths: bounded scalar derivatives give convergence of difference quotients by domination, first for bounded directions and then by mean-square approximation. We are not asserting that every coordinatewise nonlinear map is differentiable in operator norm on all of \(L^2\).

Since \(K\ge0\), \(|r(t)|\le|r(0)|\). Therefore, on \([0,T]\),
\[
\|W^{(3)}(t)\|_\infty\le\|W^{(3)}(0)\|_\infty+\pi|r(0)|T,
\]
\[
\|\dot W^{(2)}\|_{\rm op}\le\pi|r(0)|\|W^{(3)}\|_{L^2},\qquad
\|\dot X^{(1)}\|_{L^2}\le2|r(0)|\|W^{(2)}\|_{\rm op}\|W^{(3)}\|_{L^2}.
\tag{L2.25}
\]
These bounds prevent finite-time blow-up. At finite width, (L2.11), the initial law of large numbers for \(F(z_0^{(1)})\), and \(\|W_0^{(3)}\|_\infty\to0\) in probability put the same bounds on an event of probability tending to one.

Let the vector-field bound and Lipschitz constant on a slightly larger bounded set be \(M_T,L_T\). One exact flow step of length \(\Delta\) differs from its Euler step by
\[
\left\|\int_t^{t+\Delta}[\dot\Theta(\Theta(s))-\dot\Theta(\Theta(t))]\,ds\right\|
\le \frac12L_TM_T\Delta^2.
\]
Consequently the accumulated error satisfies
\[
e_{k+1}\le(1+L_T\Delta)e_k+C_T\Delta^2,
\qquad \max_{k\Delta\le T}e_k\le C_T'\Delta.
\tag{L2.26}
\]
To justify the bounded set for Euler, stop at a first exit. The bound proves that the \(X^{(1)}\) and operator components remain inside their margins. Although (L2.21) does not control the output supremum, its update gives
\[
\|W_k^{(3)}\|_\infty\le\|W_0^{(3)}\|_\infty+
\pi\Delta\sum_{s<k}|r_s|.
\]
Up to the stop, (L2.22) and (L2.26) make \(|r_s|\le|r(0)|+C_T\Delta\); choose the supremum margin larger than \(\pi T(|r(0)|+1)\). For small \(\Delta\) no first exit is possible. Thus (L2.26), also between grid times, holds for both population and finite-width Euler.

### 1.5 Deterministic coefficients, empirical feedback, and measured laws

We can now define and compare the oracle precisely. Attach the word “oracle” as a subscript to its finite arrays; it denotes the auxiliary system, not another normalization. For fixed population Euler mesh \(\Delta\), all the numbers
\[
r_k=\mathbb E_2[W_k^{(3)}H_k^{(2)}]-1,\quad
\mathbb E_1[H_s^{(1)}H_k^{(1)}],\quad
\mathbb E_2[\delta_s^{(2)}\delta_k^{(2)}]
\tag{L2.27}
\]
are deterministic. Start the oracle from the same \(z_0^{(1)},W_0^{(2)}\) as the finite network and from \(W_{\mathrm{oracle},0}^{(3)}=0\). In order at each step set
\[
h_{\mathrm{oracle},k}^{(1)}=\phi(F^{-1}(x_{\mathrm{oracle},k}^{(1)})),
\]
\[
z_{\mathrm{oracle},k}^{(2)}=W_0^{(2)}h_{\mathrm{oracle},k}^{(1)}
-2\Delta\sum_{s<k}r_s\delta_{\mathrm{oracle},s}^{(2)}\mathbb E_1[H_s^{(1)}H_k^{(1)}],
\tag{L2.28}
\]
\[
h_{\mathrm{oracle},k}^{(2)}=\phi(z_{\mathrm{oracle},k}^{(2)}),\qquad
\delta_{\mathrm{oracle},k}^{(2)}=W_{\mathrm{oracle},k}^{(3)}\odot\phi'(z_{\mathrm{oracle},k}^{(2)}),
\]
\[
\begin{aligned}
x_{\mathrm{oracle},k+1}^{(1)}=x_{\mathrm{oracle},k}^{(1)}-2\Delta r_k
\bigg((W_0^{(2)})^T\delta_{\mathrm{oracle},k}^{(2)}
-2\Delta\sum_{s<k}r_sh_{\mathrm{oracle},s}^{(1)}\mathbb E_2[\delta_s^{(2)}\delta_k^{(2)}]\bigg),\\
W_{\mathrm{oracle},k+1}^{(3)}=W_{\mathrm{oracle},k}^{(3)}-2\Delta r_kh_{\mathrm{oracle},k}^{(2)}.
\end{aligned} \tag{L2.29}
\]
This is a fixed finite Gaussian calculation. Its output weights obey the deterministic coordinate bound \(\pi\Delta\sum_{s<k}|r_s|\). Hence the product defining \(\delta^{(2)}\) can be replaced, without changing any oracle value, by a globally Lipschitz map that clips its first argument above this bound. All other maps meet the finite Gaussian lemma. Its limiting variables are exactly the population Euler variables: this follows instruction by instruction from (L2.5)–(L2.6) at population level and the already constructed action (L2.18)–(L2.19).

Record its finite matrix memory as
\[
W_{\mathrm{oracle},k}^{(2)}=W_0^{(2)}-\frac{2\Delta}{n}\sum_{s<k}
r_s\delta_{\mathrm{oracle},s}^{(2)}(h_{\mathrm{oracle},s}^{(1)})^T.
\]
Its actual matrix action is not exactly the oracle preactivation (L2.28). Their difference is
\[
\begin{aligned}
W_{\mathrm{oracle},k}^{(2)}h_{\mathrm{oracle},k}^{(1)}-z_{\mathrm{oracle},k}^{(2)}
=-2\Delta\sum_{s<k}r_s\delta_{\mathrm{oracle},s}^{(2)}
\left(\frac{(h_{\mathrm{oracle},s}^{(1)})^T h_{\mathrm{oracle},k}^{(1)}}n-
\mathbb E_1[H_s^{(1)}H_k^{(1)}]\right).
\end{aligned} \tag{L2.30}
\]
The analogous backward discrepancy is the same sum with \(h_{\mathrm{oracle},s}^{(1)}\) multiplying the empirical-minus-population \(\delta^{(2)}\) contraction. These are exact identities.

Let \(\zeta_n\) be the largest absolute error among the finitely many contractions in (L2.30), their backward versions, the output averages, and the squared normalized norms of the oracle vectors. The finite Gaussian result proves \(\zeta_n\to0\) in probability. In particular the oracle vector norms remain bounded. Put
\[
e_{n,k}=\frac{\|x_k^{(1)}-x_{\mathrm{oracle},k}^{(1)}\|_2}{\sqrt n}
+\|W_k^{(2)}-W_{\mathrm{oracle},k}^{(2)}\|_{\rm op}
+\frac{\|W_k^{(3)}-W_{\mathrm{oracle},k}^{(3)}\|_2}{\sqrt n}.
\]
Equations (L2.22) and (L2.30) bound every forward, backward, and residual difference by \(C_{T,\Delta}(e_{n,k}+\zeta_n)\). Subtracting the updates gives
\[
e_{n,k+1}\le(1+C_{T,\Delta}\Delta)e_{n,k}+C_{T,\Delta}\Delta\zeta_n.
\tag{L2.31}
\]
Initially \(e_{n,0}=\|W_0^{(3)}\|_2/\sqrt n=O_{\mathbb P}(n^{-1})\). Since \(N=\lceil T/\Delta\rceil\) is fixed, summing this recurrence proves \(\max_{k\le N}e_{n,k}\to0\). We have therefore proved the actual finite Euler width limit without feeding random scalar coefficients into the Gaussian lemma.

The same argument controls any fixed finite set of extra forward and backward measurements: expand each learned-matrix use by (L2.5) or (L2.6), use the population contraction to construct its oracle version, and add its empirical contraction errors to \(\zeta_n\). There are only finitely many such errors. For continuity of these measurements, allow arbitrary finite compositions of bounded Lipschitz coordinate maps, \(F^{-1}\), linear combinations, and the current \(W^{(2)},(W^{(2)})^*\). All coordinate instructions must be globally Lipschitz. In a product, both varying factors must be bounded, either intrinsically or by clipping. Products containing the unbounded backward field are added only later through the explicit tail argument. Induction on these operations, using (L2.22), gives an error at most \(C_{\mathrm{measurement}}\rho_n\) for two states on the same finite space, and \(C_{\mathrm{measurement}}\rho\) on the population spaces.

Choose a countable dense collection of those measurements. For each finite list of same-layer measurements, compare its joint empirical law in \(\mathcal W_2\), including dot products. For a fixed enumeration of these finite lists, the action-law
distance is
\(\sum_{j\ge1}2^{-j}\min\{1,\mathcal W_2(\mu_j,\widetilde\mu_j)\}\),
where \(\mu_j,\widetilde\mu_j\) are their joint laws on the ordinary
Euclidean coordinate space. By (L2.26) and (L2.31), its finite-flow versus population-flow error, for any fixed list, has the form
\[
C_T\Delta+o_{\mathbb P,n\to\infty;\,\Delta}(1)+C_T\Delta.
\tag{L2.32}
\]
For any requested accuracy, choose a small fixed \(\Delta\), then take \(n\to\infty\). Uniform time continuity of each fixed measurement, supplied by (L2.22) and the bounded derivatives, gives uniformity on \([0,T]\). The summable weights extend this to the action-law distance. This statement also holds for any finitely many time points jointly, by appending all those measurements to the same finite oracle calculation before taking the limit.

The population evolution is autonomous on the state just constructed. To see this also at the level of its measured law, start the collection of measurements at a current state instead of at initialization, and take all their mean-square limits on each layer. These spaces are preserved by the current action and adjoint and by the coordinate operations. If two current measured laws agree, sending each measurement to its counterpart preserves every squared norm and inner product. It extends to a surjective linear isometry between the two generated spaces, commutes with the coordinate functions, intertwines the current action and adjoint, and sends \(\delta^{(2)}\otimes H^{(1)}\) to its counterpart. The integral iteration proving existence stays in these spaces. Uniqueness therefore identifies the future laws of the two states. Restarting at time \(s\) and evolving for time \(t\) gives the same law as evolving for \(s+t\); no additional past information is required.

### 1.6 Exact raw GD, unbounded observables, and trajectories

It remains to pass from flow to the exact GD in (L2.1), and to justify the unbounded observables. For a single GD step let \(b=-2r_n(W^{(2)})^T\delta^{(2)}\), the transformed first-layer velocity. The letter \(b\) is used only in the following cubic calculation. Coordinatewise,
\[
F(z^{(1)}+\eta_n\phi'(z^{(1)})\odot b)
=F(z^{(1)})+\eta_nb
+\eta_n^2z^{(1)}\odot\phi'(z^{(1)})^2\odot b^2
+\frac{\eta_n^3}{3}\phi'(z^{(1)})^3\odot b^3.
\tag{L2.33}
\]
On the bounded state set, \(\|b\|_2/\sqrt n\le C_T\), hence \(\|b\|_\infty\le C_T\sqrt n\). Since \(\sup_s|s|\phi'(s)^2<\infty\), the extra terms in root-mean-square norm are at most
\[
C_T(\eta_n^2\sqrt n+\eta_n^3n).
\]
The other two parameter updates already are Euler updates. Adding the \(O(\eta_n^2)\) local flow error and summing the recurrence as in (L2.26) gives
\[
\sup_{t\le T}\rho_n(\Theta_n^{\mathrm{GD}}(t),\Theta_n^{\mathrm{flow}}(t))
\le C_T(\eta_n+\eta_n\sqrt n+\eta_n^2n)\longrightarrow0
\tag{L2.34}
\]
with probability tending to one. Stop first on a larger bounded set, as before. The output supremum is controlled separately by its sum of bounded activation updates and the residual bound transferred from the flow. This closes the stop. At intermediate times (L2.33) with \(0\le\eta\le\eta_n\) controls the transformed coordinate of the linearly interpolated raw parameter, so (L2.34) holds for the specified interpolation.

Here is the required control for quantities containing a possibly large backward coordinate. For this paragraph only, write \(p=(W^{(2)})^T\delta^{(2)}\) at finite width and \(P=(W^{(2)})^*\delta^{(2)}\) in the population. This abbreviation names the same repeatedly used backward measurement, not a new network state. Equations (L2.22), (L2.32), and (L2.34) show uniformly in time that the empirical joint law of \((z^{(1)},p)\) converges in \(\mathcal W_2\) to that of \((Z^{(1)},P)\). The latter laws form a compact \(\mathcal W_2\) family because these population variables are continuous in mean square.

Consequently the squared tails vanish uniformly:
\[
\lim_{A\to\infty}\limsup_{n\to\infty}
\mathbb P\left(\sup_{t\le T}\frac1n\sum_i p_i(t)^2\mathbf1_{|p_i(t)|>A}>\varepsilon\right)=0.
\tag{L2.35}
\]
For completeness, if \(p,P\) are coupled, splitting according to \(|P|\le A/2\) gives
\[
\mathbb E[p^2\mathbf1_{|p|>A}]
\le4\mathbb E[(p-P)^2]+2\mathbb E[P^2\mathbf1_{|P|>A/2}].
\]
Compactness gives uniformly small population tails by a finite cover; the uniform \(\mathcal W_2\) convergence then proves (L2.35).

Clip \(p\) to \([-A,A]\). For fixed \(A\), both \(\phi'(z^{(1)})\operatorname{clip}_A(p)\) and \(\phi'(z^{(1)})^2\operatorname{clip}_A(p)\) are Lipschitz measurements. Their squared errors from the unclipped fields are bounded by the tail in (L2.35), since \(|\phi'|\le1\). Applying \(W^{(2)}\) to their difference multiplies its root-mean-square size by at most its operator bound. Thus, first taking \(n\to\infty\), then \(A\to\infty\), proves uniform convergence of the three kernel blocks in (L2.24), with finite expectations replaced by normalized coordinate sums. It also proves convergence of the squared speeds computed from
\[
\dot Z^{(1)}=-2r\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)},
\]
\[
\dot Z^{(2)}=-2r\left\{\mathbb E_1[(H^{(1)})^2]\delta^{(2)}
+W^{(2)}[\phi'(Z^{(1)})^2(W^{(2)})^*\delta^{(2)}]\right\}.
\tag{L2.36}
\]
The prediction and loss converge uniformly as well, directly from bounded activations and the output-weight bound.

For GD, the first-layer interpolated slope is its gradient at the left endpoint. The derivative of \(z^{(2)}=W^{(2)}\phi(z^{(1)})\) uses those constant parameter slopes and the current interpolated activation. To compare it with (L2.36) at the endpoint, on \(|p_i|\le A\) the change in \(\phi'(z_i^{(1)})\) times its first-layer slope is bounded by \(C_T\eta_nA^2\); on the complement both terms are bounded by \(C_T|p_i|\). The other product-rule errors are \(O(\eta_n)\) in root-mean-square norm by bounded matrix slopes. Equation (L2.35), then \(n\to\infty\) at fixed \(A\), then \(A\to\infty\), proves
\[
\int_0^T\frac{\|\partial_tz_n^{(\ell),\mathrm{GD}}(t)\|_2^2}{n}\,dt
\longrightarrow\int_0^T\mathbb E_\ell[(\dot Z^{(\ell)}(t))^2]\,dt,
\qquad \ell=1,2.
\tag{L2.37}
\]
These statements are in probability. No fourth-moment assumption on the evolving backward field is needed.

For the trajectory-law claim, use \(\mathcal W_2\) on continuous scalar paths with the supremum distance. If \(I_\pi z\) is polygonal interpolation on a partition of mesh at most \(a\), absolute continuity and Cauchy–Schwarz give
\[
\|z-I_\pi z\|_\infty^2\le4a\int_0^T|\dot z(t)|^2\,dt.
\tag{L2.38}
\]
After coordinate averaging, (L2.37) bounds the empirical distance to this finite-grid representation by \(O_{\mathbb P}(\sqrt a)\). The population bound is identical; mean-square continuous velocities admit absolutely continuous sample paths by integrating a jointly measurable version and applying Fubini. At fixed partition, joint grid-law convergence follows from (L2.32) and (L2.34), including second moments. Polygonal interpolation is a continuous linear map of the finite grid vector. Let \(n\to\infty\) at fixed partition, then \(a\to0\) in (L2.38). This proves, separately for the two layers,
\[
\frac1n\sum_i\delta_{z_{n,i}^{(\ell),\mathrm{GD}}(\cdot)}
\longrightarrow\operatorname{Law}(Z^{(\ell)}(\cdot))
\quad\text{in }\mathcal W_2(C([0,T])).
\tag{L2.39}
\]
The same statements hold for finite gradient flow. To include hidden
features, apply the 1-Lipschitz path map \(z(\cdot)\mapsto\phi(z(\cdot))\).
For their velocities use
\[
\partial_t h_n^{(\ell)}
 =\phi'(z_n^{(\ell)})\odot\partial_tz_n^{(\ell)},
\qquad
\dot H^{(\ell)}=\phi'(Z^{(\ell)})\dot Z^{(\ell)}.
\]
The joint preactivation/velocity laws and second moments have already
been obtained by the truncation argument for (L2.36)–(L2.37).
On a fixed velocity truncation these new products are Lipschitz
measurements. Their squared errors outside it are bounded by the
velocity's squared tails, uniformly in time. Thus truncation followed
by its removal proves convergence of integrated squared feature speeds
as well as preactivation speeds.

### 1.7 Nonzero hidden motion, kernel change, and nonaffinity

Finally we verify the claimed feature learning. Only for this calculation define the following fixed initial population quantities, each of which recurs:
\[
\mu_1=\mathbb E_1[(H_0^{(1)})^2]>0,\quad
U=H_0^{(2)}\phi'(Z_0^{(2)}),\quad \nu=\mathbb E_2[U^2]>0,\quad
P_0=(W_0^{(2)})^*U.
\]
The row-conditioning calculation (L2.8), without its \(2\Delta\) factor, gives
\[
P_0=\frac{\mathbb E_2[Z_0^{(2)}U]}{\mu_1}H_0^{(1)}+\sqrt\nu\,\Gamma^{(1)},
\tag{L2.40}
\]
where \(\Gamma^{(1)}\sim N(0,1)\) is independent of the first-layer root. Put
\[
\gamma_1=\mathbb E_1[(\phi'(Z_0^{(1)})P_0)^2]>0,\qquad
S_0=\mu_1U+W_0^{(2)}[\phi'(Z_0^{(1)})^2P_0].
\]
The positivity of \(\gamma_1\) follows from the positive independent Gaussian variance in (L2.40) and \(\phi'>0\). By adjunction,
\[
\mathbb E_2[US_0]=\mu_1\nu+\gamma_1>0,
\tag{L2.41}
\]
so \(S_0\ne0\) in mean square.

Initially \(r=-1\) and \(W^{(3)}=0\). Dividing the integral equations (L2.20) by successive powers of \(t\), using bounded scalar derivatives and mean-square continuity, gives
\[
\begin{aligned}
W^{(3)}(t)&=2tH_0^{(2)}+O_{L^2}(t^2),&
\delta^{(2)}(t)&=2tU+O_{L^2}(t^2),\\
Z^{(1)}(t)-Z_0^{(1)}&=2t^2\phi'(Z_0^{(1)})P_0+o_{L^2}(t^2),\\
W^{(2)}(t)-W_0^{(2)}&=2t^2U\otimes H_0^{(1)}+o_{\rm op}(t^2),\\
Z^{(2)}(t)-Z_0^{(2)}&=2t^2S_0+o_{L^2}(t^2).
\end{aligned} \tag{L2.42}
\]
To check the orders directly, (L2.25) first gives \(W^{(3)}=O(t)\), then \(\delta^{(2)}=O(t)\), and hence \(X^{(1)}-X_0^{(1)},W^{(2)}-W_0^{(2)},Z^{(2)}-Z_0^{(2)}=O(t^2)\). Substitution into the output-weight and derivative equations gives the first line. Substitution once more gives the remaining lines. For example \(\dot X^{(1)}(t)/t\to4P_0\), and applying the bounded derivative of \(F^{-1}\) gives the first preactivation expansion.

Let \(k_3=\mathbb E_2[(H_0^{(2)})^2]>0\). Equations (L2.24), (L2.41), and (L2.42) yield
\[
K^{(1)}(t)=4\gamma_1 t^2+o(t^2),\quad K^{(2)}(t)=4\mu_1\nu t^2+o(t^2),
\]
\[
K^{(3)}(t)=k_3+4(\mu_1\nu+\gamma_1)t^2+o(t^2),\quad
K(t)=k_3+8(\mu_1\nu+\gamma_1)t^2+o(t^2).
\tag{L2.43}
\]
The two squared displacements have leading terms \(4\gamma_1 t^4\) and \(4\mathbb E_2[S_0^2]t^4\); their squared speeds have leading terms \(16\gamma_1 t^2\) and \(16\mathbb E_2[S_0^2]t^2\). Thus both hidden layers move and every kernel block has a positive integral on sufficiently short nonzero intervals. Also
\[
f(t)=2k_3t+o(t),\qquad \mathcal L(t)=1-4k_3t+o(t).
\]
Both initial preactivation laws in (L2.7) are nondegenerate Gaussians. Their variances remain positive by mean-square continuity. For either layer the error of the best affine fit to the activation is
\[
\operatorname{Var}(\phi(Z^{(\ell)}))-
\frac{\operatorname{Cov}(Z^{(\ell)},\phi(Z^{(\ell)}))^2}{\operatorname{Var}(Z^{(\ell)})}.
\tag{L2.44}
\]
It is initially positive: equality would force \(\arctan\) to agree with an affine function on a full-support Gaussian law and hence everywhere by continuity. The moments in (L2.44) are continuous in mean square because \(\phi\) is bounded and Lipschitz. This error therefore remains positive for both layers on a common interval \([0,T_*]\). Equations (L2.34), (L2.37), (L2.39), and (L2.43) establish all the asserted convergence and feature-learning claims.

<a id="l3-local"></a>

## 2. Local theorem for three hidden layers

The theorem below holds on an explicit positive physical interval. Its
proof is given in §§3–8. Global continuation of this population solution
is not asserted.

### Network, exact algorithm, and interval

There is one input and one target, both equal to one. All three hidden
layers have width \(n\). The first preactivation \(z^{(1)}\) and the
stored readout \(W^{(4)}\) are \(n\)-vectors. The two hidden matrices
\(W^{(2)},W^{(3)}\) are \(n\) by \(n\). With \(\phi=\arctan\), set
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 f_n=\frac{(W^{(4)})^T h^{(3)}}n,\qquad
 r_n=f_n-1,\qquad \mathcal L_n=r_n^2,
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot(W^{(3)})^T\delta^{(3)},\quad
 \delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)}.
 \tag{L3.1}
\]
The initialization blocks are independent, with
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{L3.2}
\]
Use the exact raw updates, with \(\eta_n=n^{-2}\),
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,
\]
\[
 W^{(\ell)}_{k+1}
 =W^{(\ell)}_k-\frac{2\eta_n r_{n,k}}n
           \delta^{(\ell)}_k(h^{(\ell-1)}_k)^T,
 \qquad\ell=2,3,
\]
\[
 W^{(4)}_{k+1}=W^{(4)}_k-2\eta_n r_{n,k}h^{(3)}_k.
 \tag{L3.3}
\]
Physical time is \(t=k\eta_n\). Between these times interpolate the
raw parameters linearly and recompute all hidden preactivations and
features from the interpolated parameters. Finite gradient flow
means the differential equations with the same right-hand sides
divided by \(\eta_n\).
At GD mesh nodes, velocities mean right-hand derivatives; use the
left-hand derivative at \(T_0\) if it is a terminal mesh node.

Here is one explicit, very conservative positive interval. Let
\[
 a=\pi/2,\quad A=a^2+e,\quad
 M_p=2^{1/p}\exp\!\big(A(2a+1)+2pA^2a^2\big)\quad(p=1,2),
\]
\[
 A_3=a^2+AM_1,\quad
 C_3=(1+2a)\exp((1+2a)A_3)+a^2,\quad Q=a(1+C_3),
\]
\[
 C_2=(2Q+C_3)M_2+Q^2,\qquad
 S_0=\min\{1,(2C_2)^{-1},(2C_3)^{-1}\},\qquad
 T_0=\frac14\min\{S_0,(4a^2)^{-1}\}.
 \tag{L3.4}
\]
The constants are deliberately not optimized. They are finite explicit
numbers determined by \(\arctan\), not by an unproved continuation
or moment assumption.

### Theorem 2: conclusions on the explicit local interval

There are three fixed neuron probability spaces, with bounded initial
matrix actions \(W^{(2)}_0,W^{(3)}_0\) and their reverse actions.
They are constructed from the joint limits of finite Gaussian matrix
calculations, preserving every reused transpose. There is a unique
local uncut population state
\[
 X^{(1)}(t),\qquad W^{(2)}(t),\qquad
 W^{(3)}(t),\qquad W^{(4)}(t),\qquad 0\le t\le T_0.
 \tag{L3.5}
\]
Here \(X^{(1)}=F(Z^{(1)})\), \(F(z)=z+z^3/3\);
the two matrices are bounded actions between the adjacent population
spaces; and the readout is the typical population coordinate.
Initially \(Z^{(1)}_0\) is standard Gaussian and \(W^{(4)}_0=0\).
This is a finite list of evolving fields and operators, not a
finite-scalar description.

Use (L3.1) on these spaces with capital population coordinates
\(Z^{(\ell)},H^{(\ell)}\), population backward coordinates
\(\delta^{(\ell)}\in L^2(\Omega_\ell)\), adjoints \(*\), and
ordinary pointwise products within each layer.
Then
\[
 f=E_3[W^{(4)}H^{(3)}],\quad r=f-1,\quad \mathcal L=r^2,
\]
\[
 \frac{dX^{(1)}}{dt}=-2r\,(W^{(2)})^*\delta^{(2)},\quad
 \frac{dW^{(2)}}{dt}=-2r\,\delta^{(2)}\otimes H^{(1)},
\]
\[
 \frac{dW^{(3)}}{dt}=-2r\,\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{dt}=-2r\,H^{(3)}.                       \tag{L3.6}
\]
The rank-one action is explicitly
\((U\otimes V)B=U E_{\ell-1}[VB]\) for
\(U\in L^2(\Omega_\ell)\) and \(V,B\in L^2(\Omega_{\ell-1})\).
Uniqueness holds among continuous integral solutions on these fixed
spaces with bounded operator and mean-square parameter norms.
The same uniqueness holds when restarting from a reached state on
any remaining subinterval of the constructed interval.

In the raw coordinate \(Z^{(1)}\), (L3.6) is the gradient flow of
\(\mathcal L\): use \(L^2(\Omega_\ell)\) lengths for the vector fields and
Hilbert–Schmidt length for trained matrix changes.
The present state alone determines its derivatives; the Gaussian
response coefficients in the proof are not prescribed external
inputs to its evolution.

For each fixed same-layer finite list of network measurements,
the joint empirical law of both finite GD and finite gradient flow
converges uniformly in \(t\in[0,T_0]\), in probability, to the
corresponding population law. Convergence includes second moments.
The class includes finite compositions of the current states,
globally Lipschitz coordinate functions, bounded products, and
both orientations of both current matrices; finitely many specified
times may be used jointly. It also includes the named backward
fields in (L3.1) and the hidden preactivation and feature velocities.
No coordinatewise pairing across distinct hidden layers is asserted.

Equivalently, for any such finite same-layer coordinate list and any
fixed continuous measurement \(\psi\) of at most quadratic growth,
its empirical average approaches its population expectation uniformly
in time. Thus prediction, residual, and loss converge uniformly.
The four finite kernel blocks
\[
 \frac{\|\delta^{(1)}\|_2^2}{n},\qquad
 \frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2},\qquad
 \frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2},\qquad
 \frac{\|h^{(3)}\|_2^2}{n}
 \tag{L3.7}
\]
converge uniformly to the expectation formulas in
[§7](#l3-gradient).
For every hidden layer, the empirical law of its entire preactivation
path converges, including second moments of the supremum norm, to
the law of its population path. Integrated squared velocities
converge to the corresponding population integrals.

With the same finite initialization, GD and finite gradient flow
also approach one another uniformly in the state distance
\[
\rho_n(\theta,\widetilde\theta)
=\frac{\|F(z^{(1)})-F(\widetilde z^{(1)})\|_2}{\sqrt n}
+\sum_{\ell=2}^3\|W^{(\ell)}-\widetilde W^{(\ell)}\|_{\rm op}
+\frac{\|W^{(4)}-\widetilde W^{(4)}\|_2}{\sqrt n}.
\] No operator-norm comparison across different
widths or between different underlying spaces is asserted.

Every hidden layer learns a nonconstant feature trajectory.
More precisely, there are nonzero square-integrable variables
\(V^{(\ell)}\) such that
\[
 Z^{(\ell)}(t)-Z^{(\ell)}_0=2t^2V^{(\ell)}+o(t^2),\qquad
 H^{(\ell)}(t)-H^{(\ell)}_0
   =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2)
 \tag{L3.8}
\]
in mean square, and both displayed leading variables have positive
mean-square size. The three hidden kernel blocks are positive
constant multiples of \(t^2+o(t^2)\); hidden feature squared-speed
integrals have positive \(T^3\) leading coefficients. Explicit
initial Gaussian formulas are given in [§8](#l3-features).
The total kernel is nonconstant, the loss decreases, and the
activation's best affine-approximation error on each hidden
distribution remains strictly positive on a common initial interval.

### Proof dependencies

The proof is the following chain of proved lemmas, with no additional assumptions on the original network.

1. [§3](#l3-source) proves the exact finite
   Gaussian source representation, including both independent
   matrices, both transposes, empirical training feedback, and
   singular covariance cases.
2. [§4](#l3-actions) realizes those finite calculations
   on common population spaces and proves the fixed-clipping flow
   and its fixed-clipping width limit.
3. [§5](#l3-bootstrap) proves a tail bound uniform
   in the Euler mesh and clipping level on the explicit \(S_0\).
   Its displayed scalar equations are precisely the equations
   proved in item 1 and realized by item 2.
4. [§6](#l3-bridge) uses this bound to remove clipping,
   prove local uniqueness and restartability, and establish
   convergence from the actual raw GD, not merely from a
   transformed or population-feedback scheme. In particular its
   source identification and tail estimate are established in §§3–5.
5. [§7](#l3-gradient) proves that the resulting autonomous
   evolution is a genuine gradient flow with all four kernel
   contributions.
6. [§8](#l3-features) derives the strictly nonzero initial
   hidden movement from this flow and the initial Gaussian action
   laws, using the local flow constructed in §§3–7.

The theorem and its restart statement apply only within the interval
constructed here.


<a id="l3-source"></a>

## 3. Fixed-mesh source identification

This is a fixed finite-program result. Its constants may depend on the number of steps, the step size, and the clipping level. It proves neither mesh-uniform response bounds nor a continuous-time limit.

### Statement and conventions

Fix an integer \(N\), a feature-time proof step \(\Delta>0\), and a
smooth clipping function \(\tau_R\) with
\(|\tau_R(q)|\le |q|\), \(|\tau_R'(Q)|\le1\), and
\(|\tau_R(q)|\le2R\). Let \(\phi(z)=\arctan z\) and
\(F(z)=z+z^3/3\). The independent finite matrices
\(W_0^{(2)},W_0^{(3)}\) have independent \(N(0,1/n)\) entries and
are independent of the iid standard Gaussian coordinates \(z_0^{(1)}\).
Initially the auxiliary finite readout is \(W_0^{(4)}=0\).
The zero initialization is removed at the end of this section.

Consider the exact finite-width discrete calculation

\[
x^{(1)}_0=F(z^{(1)}_0),\quad
h^{(1)}_k=\phi(F^{-1}(x^{(1)}_k)),\quad
z^{(2)}_k=W_k^{(2)}h^{(1)}_k,\quad h^{(2)}_k=\phi(z^{(2)}_k),
\]
\[
z^{(3)}_k=W_k^{(3)}h^{(2)}_k,\quad h^{(3)}_k=\phi(z^{(3)}_k),\quad
\delta^{(3)}_k=W_k^{(4)}\odot \phi'(z^{(3)}_k),\quad
q^{(2)}_k=(W_k^{(3)})^T\delta^{(3)}_k,
\]
\[
\delta^{(2)}_k=\phi'(z^{(2)}_k)\odot\tau_R(q^{(2)}_k),\quad
q^{(1)}_k=(W_k^{(2)})^T\delta^{(2)}_k,
\]
\[
x^{(1)}_{k+1}=x^{(1)}_k+\Delta q^{(1)}_k,\quad
W_{k+1}^{(2)}=W_k^{(2)}+\frac\Delta n\delta^{(2)}_k(h^{(1)}_k)^T,
\]
\[
W_{k+1}^{(3)}=W_k^{(3)}+\frac\Delta n\delta^{(3)}_k(h^{(2)}_k)^T,
\qquad W_{k+1}^{(4)}=W_k^{(4)}+\Delta h^{(3)}_k.
\]

For every fixed same-layer tuple of its nodes through step \(N\), its empirical law converges in probability in \(\mathcal W_2\) to the scalar construction below. In particular, all the pairwise contractions used below converge. Covariance matrices may be singular.

There are four mutually independent centered Gaussian groups

\[
(\xi^{(2)}_k)_k,\quad(\xi^{(3)}_k)_k,\quad
(\zeta^{(1)}_k)_k,\quad(\zeta^{(2)}_k)_k,
\]

also independent of \(Z_0^{(1)}\), with covariances

\[
\mathbb E_\ell\xi^{(\ell)}_k\xi^{(\ell)}_s
=\mathbb E_{\ell-1} H^{(\ell-1)}_kH^{(\ell-1)}_s,\qquad
\mathbb E_{\ell-1}\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_s
=\mathbb E_\ell\delta^{(\ell)}_k\delta^{(\ell)}_s,
\quad\ell=2,3.
\]

The scalar equations are

\[
X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{r<k}Q^{(1)}_r,
\quad H^{(1)}_k=\phi(F^{-1}(X^{(1)}_k)),
\]
\[
Z^{(2)}_k=\xi^{(2)}_k+\sum_{s<k}a^{(2)}_{ks}\delta^{(2)}_s,
\quad Q^{(1)}_k=\zeta^{(1)}_k+\sum_{s\le k}b^{(2)}_{ks}H^{(1)}_s,
\]
\[
Z^{(3)}_k=\xi^{(3)}_k+\sum_{s<k}a^{(3)}_{ks}\delta^{(3)}_s,
\quad Q^{(2)}_k=\zeta^{(2)}_k+\sum_{s\le k}b^{(3)}_{ks}H^{(2)}_s,
\]

where
\[
H_k^{(\ell)}=\phi(Z_k^{(\ell)}),\quad
W_k^{(4)}=\Delta\sum_{r<k}H_r^{(3)},\quad
\delta_k^{(3)}=W_k^{(4)}\phi'(Z_k^{(3)}),\quad
\delta_k^{(2)}=\phi'(Z_k^{(2)})\tau_R(Q_k^{(2)}),
\]
and

\[
a^{(\ell)}_{ks}
=\mathbb E_{\ell-1}\frac{\partial H^{(\ell-1)}_k}
                    {\partial\zeta^{(\ell-1)}_s}
 +\Delta\mathbb E_{\ell-1} H^{(\ell-1)}_kH^{(\ell-1)}_s,
\qquad s<k,
\]
\[
b^{(\ell)}_{ks}
=\mathbb E_\ell\frac{\partial\delta^{(\ell)}_k}
                    {\partial\xi^{(\ell)}_s}
 +\Delta\mathbf1_{s<k}\mathbb E_\ell\delta^{(\ell)}_k\delta^{(\ell)}_s,
\qquad s\le k.
\]

Every derivative is a derivative of the explicit finite coordinate expression with respect to the named Gaussian source coordinate. Previously calculated deterministic coefficients and covariance parameters are held fixed. Distinct source coordinates remain distinct formal arguments even if their joint Gaussian law is singular. Coefficients themselves need not be invariant under a different off-support extension; their contracted correction is invariant.

### Finite Gaussian conditioning, with two matrices

We first prove the needed source rule for a fixed finite calculation with deterministic scalar coefficients, globally Lipschitz \(C^1\) coordinate instructions having bounded first derivatives, and finitely many independent Gaussian matrices, each reusable in both directions. The root coordinate tuples are iid with finite second moments and independent of the matrices. The initial tuple may contain both \(z_0^{(1)}\) and
\(F(z_0^{(1)})\); its second moment is finite because the Gaussian
has a finite sixth moment. No global Lipschitz property of \(F\) is used.

Condition on the complete adaptive transcript. For one selected finite matrix \(W\), write its previous observations as

\[
WV=Y,\qquad W^T U=Q.
\]

The other matrices cause no change to the following formula. Conditional residuals of the independent matrices remain independent: inductively, a query is measurable from the current transcript, and its newly observed answer imposes a linear constraint only on the queried matrix. Coordinate calculations reveal no further randomness.

When the two input Gram matrices are invertible, Gaussian orthogonal projection gives

\[
W\mid\mathcal H\ \overset d=
Y(V^T V)^{-1}V^T
+U(U^T U)^{-1}Q^T P_{V^\perp}
+P_{U^\perp}\widetilde W P_{V^\perp}.
\tag{S.1}
\]

For a new input \(h\), put
\(\alpha_n=(V^TV/n)^{-1}(V^Th/n)\) and
\(h_\perp=h-V\alpha_n\). Then

\[
Wh=Y\alpha_n+U\beta_n+
\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g,
\quad
\beta_n=(U^T U/n)^{-1}(Q^T h_\perp/n),
\tag{S.2}
\]

in conditional law, with fresh standard Gaussian \(g\). The transpose formula is identical with the two sides interchanged.

Assume for the moment that all limiting input Gram matrices are positive definite. Induction on the finite transcript proves joint \(\mathcal W_2\) empirical convergence: all coefficients in (S.2) converge by the previous induction hypothesis; the removed projection has conditional mean squared normalized squared norm \(\operatorname{rank}(U)/n\); after removing it, conditional averaging of independent Gaussian coordinates gives joint weak convergence and second-moment convergence. Globally Lipschitz coordinate instructions preserve \(\mathcal W_2\) convergence. This works unchanged with two interleaved matrices.

### Why the response coefficient is the source derivative

The response identification follows directly from the conditioning formula.
Use typed population variables \(V_r\in L^2(\Omega_{\ell-1})\)
for previous forward inputs and \(U_s\in L^2(\Omega_\ell)\) for previous
transpose inputs to \(W_0^{(\ell)}\). Put
\(\Gamma_U=(\mathbb E_\ell[U_sU_t])_{st}\). By induction write

\[
Y_r=\xi_r+\sum_s D_{rs}U_s,
\qquad D_{rs}=\mathbb E_{\ell-1}\partial_{\zeta_s}V_r,
\]
\[
Q_s=\zeta_s+\text{a linear combination of previous forward inputs}.
\]

Unavailable and future-source derivatives are zero. Let \(\alpha\)
be the limiting least-squares coefficients and
\(H_\perp=H-\sum_r\alpha_rV_r\). Orthogonality gives
\(\mathbb E_{\ell-1}[V_rH_\perp]=0\) for each previous forward
input. Hence the response part of \(Q_s\) drops out of its pairing
with \(H_\perp\):

\[
\mathbb E_{\ell-1}[Q_s H_\perp]=\mathbb E_{\ell-1}[\zeta_s H_\perp].
\]

The Gaussian group \(\zeta\) is independent of the roots and other
source groups and has covariance \(\Gamma_U\). Gaussian integration by parts yields

\[
\mathbb E_{\ell-1}[\zeta H_\perp]
=\Gamma_U\,\mathbb E_{\ell-1}\nabla_\zeta H_\perp.
\]

Thus (S.2)'s limiting coefficient is

\[
\beta=\mathbb E_{\ell-1}\nabla_\zeta H
       -\sum_r\alpha_r\mathbb E_{\ell-1}\nabla_\zeta V_r.
\]

After substituting the decompositions of \(Y_r\) into (S.2), their old responses cancel the second term. The resulting rule is exactly

\[
W_0^{(\ell)}H
=\xi_H+\sum_s U_s\,\mathbb E_{\ell-1}\partial_{\zeta_s}H.
\tag{S.3}
\]

The new source is
\(\xi_H=\sum_r\alpha_r\xi_r+\sigma G\), where
\(\sigma^2=\mathbb E_{\ell-1}[H_\perp^2]\) and \(G\) is a fresh
standard Gaussian independent of the preceding sources. Consequently
\[
\operatorname{Cov}(\xi_H,\xi_r)=\mathbb E_{\ell-1}[HV_r],
\qquad \operatorname{Var}(\xi_H)=\mathbb E_{\ell-1}[H^2].
\]
Source groups for the two orientations of a matrix are independent;
the actions themselves are related by adjunction and their responses. The same argument applies separately to \(W_0^{(2)}\) and \(W_0^{(3)}\) at every interleaved call.

In (S.3), \(W_0^{(\ell)}H\) denotes the limiting matrix-answer
coordinate; §4 realizes all such answers as one bounded action.
The proof uses the complete derivative of \(H\) as its finite coordinate
expression. It does not discard derivative paths passing through calls to the other matrix.

### Removing singular-Gram difficulties

For each matrix call, temporarily replace its input \(h\) by
\(h+\varepsilon\gamma\), where \(\gamma\) is a fresh independent
standard Gaussian vector, revealed just before that call. At fixed
\(\varepsilon>0\), projecting off the earlier input span gives
\[
\frac{\|P_{V^\perp}(h+\varepsilon\gamma)\|_2^2}{n}
=\frac{\|P_{V^\perp}h\|_2^2}{n}+\varepsilon^2+o_{\mathbb P}(1).
\]
The cross term has conditional variance at most
\(4\varepsilon^2\|h\|_2^2/n^2\), and the discarded Gaussian
projection has fixed rank. Thus every successive limiting Schur
complement is at least \(\varepsilon^2\). All limiting query Gram
matrices are positive definite, so the preceding proof applies.
The fresh input noises are additional independent roots; (S.3)
is applied to the perturbed query inputs.

For the fixed finite program, couple perturbed and unperturbed calculations using the same original matrices and roots. On the event that all the finitely many matrix operator norms and input-noise normalized norms are bounded, induction through the instructions gives

\[
\max_v\frac{\|v^\varepsilon-v\|_2}{\sqrt n}\le C\varepsilon,
\tag{S.4}
\]

where \(C\) depends on the fixed program, but not on \(n\) or
\(0<\varepsilon\le1\). The event has probability tending to one. The matrix bound follows, for example, by a fixed-net Gaussian tail bound and a union bound over the two matrices.

The scalar source constructions converge as \(\varepsilon\downarrow0\) as well. A detailed finite induction suffices: source covariance entries are second moments of previously constructed inputs; Gaussian covariance square roots are continuous even at singular positive-semidefinite matrices; all previously constructed scalar coordinate functions and their source derivatives are continuous in the finite deterministic coefficient list. Their first derivatives have deterministic bounds at each fixed instruction because the coordinate instructions have bounded first derivatives. Therefore Gaussian coupling, \(\mathcal W_2\) convergence, and dominated convergence pass both second moments and expected source derivatives to the \(\varepsilon=0\) recursion. No inverse or pseudoinverse is used in this last continuity step. Combining this fact with (S.4) identifies the unperturbed empirical limit with (S.3).

For completeness, degenerate Gaussian Stein also directly explains the absence of ambiguity. If \(\zeta\) has covariance \(\Gamma\) and the population vector
\(U\) has second-moment matrix \(\Gamma\), then

\[
\mathbb E[\zeta g]=\Gamma\mathbb E\nabla g,\qquad
U^T(I-\Gamma^+\Gamma)v=0\quad\text{a.s.}
\]

for every deterministic vector \(v\). Thus replacing \(\mathbb E\nabla g\) by
\(\Gamma^+\mathbb E[\zeta g]\) may change individual coefficients,
but cannot change \(U^T\mathbb E\nabla g\). One must not assert convergence of finite pseudoinverses at a rank drop.

### Application and the empirical training coefficients

Unroll \(W_k^{(2)}\) and \(W_k^{(3)}\) into their initial matrices plus their finite learned rank-one sums. Each forward trained call has the extra term

\[
\Delta\sum_{s<k}\delta^{(\ell)}_s
                \frac{(h^{(\ell-1)}_s)^T h^{(\ell-1)}_k}{n},
\]

and each transpose trained call has the extra term

\[
\Delta\sum_{s<k}h^{(\ell-1)}_s
                \frac{(\delta^{(\ell)}_s)^T\delta^{(\ell)}_k}{n}.
\]

Freeze these finitely many contractions at the population values constructed causally. This produces an oracle with deterministic coefficients, to which the proved finite conditioning/source lemma applies. At each stage the population contraction involves only already constructed variables, so this definition is not circular.

The oracle and actual finite Euler calculation agree asymptotically. Indeed,
\(|\delta_k^{(2)}|\le2R\) coordinatewise, while
\(|W_k^{(4)}|\le N\Delta\pi/2\) gives a coordinate bound for
\(\delta_k^{(3)}\). The product defining \(\delta^{(3)}\) can therefore be extended to a globally Lipschitz \(C^1\) map by smoothly clipping the readout argument outside a slightly larger interval. Every other required coordinate map is already globally Lipschitz. Root tuples have finite second moments. All oracle norms and all initial matrix operator norms are bounded with probability tending to one. On that event,

\[
\left|\frac{u^Tv-\bar u^T\bar v}{n}\right|
\le \frac{\|u-\bar u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
+\frac{\|\bar u\|_2}{\sqrt n}\frac{\|v-\bar v\|_2}{\sqrt n}.
\]

Finite induction through the unrolled calculation bounds actual/oracle error by a constant times the largest oracle contraction error. Every such error converges to zero by the lemma. No growing-mesh estimate is used. Adding the learned terms to (S.3) gives exactly the stated \(a^{(\ell)}_{ks}\) and \(b^{(\ell)}_{ks}\) formulas.

The causal initial-matrix call order at step \(k\) is
\(W_0^{(2)}h_k^{(1)}\), \(W_0^{(3)}h_k^{(2)}\),
\((W_0^{(3)})^T\delta_k^{(3)}\),
\((W_0^{(2)})^T\delta_k^{(2)}\). Thus forward response sums use \(s<k\), while transpose response
sums use \(s\le k\). This order also proves that every covariance extension and every derivative coefficient is known when needed.

As explicit checks on the current-source terms,

\[
b^{(3)}_{kk}=\mathbb E_3[W_k^{(4)}\phi''(Z^{(3)}_k)],
\]
\[
b^{(2)}_{kk}
=\mathbb E_2[\phi''(Z^{(2)}_k)\tau_R(Q^{(2)}_k)]
 +b^{(3)}_{kk}\mathbb E_2[\phi'(Z^{(2)}_k)^2\tau_R'(Q^{(2)}_k)].
\]

The second term on the last line is a current-step return through the other matrix; omitting it would be incorrect. Earlier-source derivatives also retain every such path.

Finally, replacing \(W_0^{(4)}=0\) by iid \(N(0,n^{-2})\) entries changes no fixed-mesh limit. Couple the two finite calculations; the initial readout difference is
\(\|W_0^{(4)}\|_2/\sqrt n=O_{\mathbb P}(n^{-1})\), its initial coordinate supremum is bounded with probability tending to one, and the same fixed-step Lipschitz comparison applies. This last statement is only for fixed \(N,\Delta,R\).

### Scope of the result

The displayed scalar representation, the four independent Gaussian source groups, all current/previous response terms, and singular covariance cases are justified at each fixed clipped finite mesh. Individual off-support derivative coefficients require the stated formal-expression convention. This proof supplies no bound uniform in \(N\), \(\Delta\downarrow0\), or \(R\uparrow\infty\).


<a id="l3-actions"></a>

## 4. Common population actions and clipped flows

This section constructs the common population state for the local
three-hidden-layer limit and proves existence at every finite feature time
for each fixed clipping level. The finite Gaussian calculation is proved
in §3; removal of clipping will use the local estimates in §§5–6.

Throughout, \(\phi(z)=\arctan z\), \(a=\pi/2\), and
\(F(z)=z+z^3/3\). Write \(E_\ell\) for expectation over the neuron
population of hidden layer \(\ell\). These are three separate
populations; a neuron index in one layer is not paired with an index
in another.

### Constructing both directions of both initial matrices

Consider the following countable collection of finite calculations.
At finite width their roots are \(z^{(1)}_0\) and \(F(z^{(1)}_0)\),
where \(z^{(1)}_{0,i}\) are independent standard Gaussians. Include
the constant vector on each layer, rational linear combinations,
and multiplication by either initial Gaussian matrix
\(W^{(2)}_0,W^{(3)}_0\), in either direction. Include
\(\phi,F^{-1}\), the smooth clipping functions used below at integer
levels, and a countable family of bounded globally Lipschitz
coordinate functions dense among continuous functions on every
compact subset of each finite-dimensional coordinate space.
Products are included only after clipping their varying factors to
fixed bounded intervals, so these coordinate instructions are
globally Lipschitz. Smooth versions can be used for the countable
dense family. Treat \(F(z^{(1)}_0)\) as part of the initial root tuple;
no global Lipschitz claim about \(F\) is needed.

Any finite union of these calculations is another finite calculation.
The fixed-program Gaussian conditioning proof therefore gives
consistent, deterministic joint limiting laws of all their nodes,
separately for each layer. Countably many consistent finite laws
define a countable random coordinate collection on its product
measurable space. Denote the resulting probability spaces by
\(\Omega_1,\Omega_2,\Omega_3\), retaining exactly the information
generated by their coordinate slots.

For a square-integrable scalar population variable \(U\), write
\[
 \|U\|_{L^2(\Omega_{\ell})}=(E_\ell U^2)^{1/2}.
\]
This is a population mean-square size, not a new normalization of a
finite vector. Finite vector sizes remain \(\|u\|_2/\sqrt n\).
Let \(\mathcal H_\ell=L^2(\Omega_\ell)\), the set of population
variables with finite mean-square size, identifying variables equal
with probability one.

The finite matrices have operator norms at most \(10\) with
probability tending to one. A \(1/4\)-net on each unit sphere has
at most \(9^n\) points, and the scalar Gaussian bound gives
\[
 \mathbb P(\|W^{(\ell)}_0\|_{\rm op}>10)
 \le 2\,9^{2n}\exp(-100n/8),\qquad \ell=2,3.
\]
For every finite rational linear combination of existing nodes,
pass the exact finite matrix norm inequality to its limiting second
moment. There are only countably many such combinations. Consequently
the assignment to the corresponding matrix-answer node satisfies
\[
 \|W^{(\ell)}_0 U\|_{L^2(\Omega_{\ell})}\le10\|U\|_{L^2(\Omega_{\ell-1})}.             \tag{A.1}
\]
If two expressions define the same input in mean square, (A.1) shows
that they define the same output. Thus the assignment is a linear
map on the span of the coordinate nodes.

That span is dense in \(\mathcal H_\ell\): bounded functions of
finitely many coordinate slots approximate any square-integrable
variable on the generated probability space; bounded continuous
functions approximate those finite-coordinate functions in mean
square; and the included countable bounded Lipschitz family
approximates the continuous functions on compact sets. Clipping
and restricting to a compact set control the discarded tails.
Equation (A.1) extends each initial matrix action uniquely to every
square-integrable input. The same construction extends its reverse
action. Passing the exact finite transpose identity gives
\[
 E_\ell[V\,W^{(\ell)}_0U]
 =E_{\ell-1}[U\,(W^{(\ell)}_0)^*V].                      \tag{A.2}
\]
The star names precisely this reverse action. Both directions are
retained throughout training, not independently resampled.

Real scalar coefficients and other globally Lipschitz coordinate
maps can be approximated by this collection when needed. For each
fixed finite calculation propagate its approximation errors and
use (A.1) at every matrix call. This identifies all fixed-step clipped
Euler calculations below on these same three spaces with the
finite-width laws given by Gaussian conditioning.

### State and clipped equations

For \(U\in\mathcal H_\ell\), \(V\in\mathcal H_{\ell-1}\), define
\[
 (U\otimes V)B=U\,E_{\ell-1}[VB].                        \tag{A.3}
\]
Its operator norm is \(\|U\|_{L^2(\Omega_{\ell})}\|V\|_{L^2(\Omega_{\ell-1})}\); its reverse
action is \(V\otimes U\).

Choose smooth odd functions \(\tau_R\), for integers \(R\ge1\), with
\[
 \tau_R(x)=x\ (|x|\le R),\quad
 |\tau_R(x)|\le\min\{|x|,2R\},\quad
 0\le\tau_R'(x)\le1.                                    \tag{A.4}
\]
For example integrate a smooth even function equal to one on
\([-1,1]\), zero outside \([-2,2]\), and between zero and one,
after scaling its argument by \(R\).

The state is
\[
 X^{(1)}\in\mathcal H_1,\quad
 W^{(2)}:\mathcal H_1\to\mathcal H_2,\quad
 W^{(3)}:\mathcal H_2\to\mathcal H_3,\quad
 W^{(4)}\in\mathcal H_3.
\]
The matrix actions are bounded linear maps. Initially they are the
two actions just constructed, \(X^{(1)}_0=F(Z^{(1)}_0)\), and
\(W^{(4)}_0=0\). The forward and clipped backward calculations are
\[
 Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\phi(Z^{(1)}),
 \quad Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),
\]
\[
 Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}),
 \quad \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),
\]
\[
 \delta^{(2)}_R
 =\phi'(Z^{(2)})
   \tau_R\!\left((W^{(3)})^*\delta^{(3)}\right).          \tag{A.5}
\]
Products are within their stated layer. In feature time \(s\),
\[
 \frac{dX^{(1)}}{ds}=(W^{(2)})^*\delta^{(2)}_R,\quad
 \frac{dW^{(2)}}{ds}=\delta^{(2)}_R\otimes H^{(1)},
\]
\[
 \frac{dW^{(3)}}{ds}=\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{ds}=H^{(3)}.                            \tag{A.6}
\]
Clipping is a proof device. In general (A.6) is not gradient ascent
for the original predictor; no bound below assumes it is.

Use the state distance
\[
 \begin{aligned}
 \rho(\theta,\widetilde\theta)={}&
 \|X^{(1)}-\widetilde X^{(1)}\|_{L^2(\Omega_1)}
 +\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}\\
 &+\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}
 +\|W^{(4)}-\widetilde W^{(4)}\|_{L^2(\Omega_3)}.
 \end{aligned}                                         \tag{A.7}
\]
For finite-width states replace population mean-square sizes by
ordinary Euclidean sizes divided by \(\sqrt n\). All bounds below
hold with the same constants in either setting.

### Bounds independent of clipping

On \(0\le s\le S\), integration of the readout equation gives
\[
 |W^{(4)}(s)|\le as\quad\hbox{with probability one}.      \tag{A.8}
\]
Thus \(\|\delta^{(3)}(s)\|_{L^2(\Omega_3)}\le as\). Using (A.3)--(A.5),
\[
 \|W^{(3)}(s)\|_{\rm op}\le10+\frac{a^2s^2}{2},
\]
\[
 \|W^{(2)}(s)\|_{\rm op}
 \le10+\frac{10a^2s^2}{2}+\frac{a^4s^4}{8}.              \tag{A.9}
\]
Indeed
\(\|\delta^{(2)}_R\|_{L^2(\Omega_2)}\le
\|W^{(3)}\|_{\rm op}\|\delta^{(3)}\|_{L^2(\Omega_3)}\).
The first equation of (A.6) then bounds both the mean-square velocity
of \(X^{(1)}\) and its displacement on every fixed \(S\).
All four velocities in (A.7) are bounded by a finite constant depending
only on \(S\), not on \(R\).

Harmless enlargements of these bounds also hold for transformed
Euler with \(M\Delta\le S\), and for nonzero readouts with an initial
coordinate bound at most one: sum the same polynomial estimates.
No gradient identity is required. The identical bounds hold for
an uncut finite feature flow, since
\(\|\delta^{(2)}\|_{L^2(\Omega_2)}\le
\|W^{(3)}\|_{\rm op}\|\delta^{(3)}\|_{L^2(\Omega_3)}\).

On these bounded sets, (A.6) has Lipschitz constant at most
\(C_S(1+R)\) in (A.7). To see the important product estimates, first
use the pointwise readout bound in
\[
 \begin{aligned}
 &\|W^{(4)}\phi'(Z^{(3)})
 -\widetilde W^{(4)}\phi'(\widetilde Z^{(3)})\|_{L^2(\Omega_3)}\\
 &\qquad\le \|W^{(4)}-\widetilde W^{(4)}\|_{L^2(\Omega_3)}
       +2aS\|Z^{(3)}-\widetilde Z^{(3)}\|_{L^2(\Omega_3)}.
 \end{aligned}
\]
The displayed coefficient uses a zero-initial-readout reference.
For two paths with initial coordinate readout bounds at most one,
replace \(2aS\) by \(2(1+aS)\). This and the operator bounds make
the full backward action
\((W^{(3)})^*\delta^{(3)}\) Lipschitz in (A.7). Changing the middle
gate in (A.5) costs at most
\(4R\|Z^{(2)}-\widetilde Z^{(2)}\|_{L^2(\Omega_2)}\), since the clipped
factor is at most \(2R\). Changing its input costs at most the
difference of the full backward actions. The forward and reverse
maps and (A.3) give the asserted bound. Only the readout itself
needs a common pointwise bound, not its difference.

### Existence, uniqueness, and the fixed-clipping width limit

For fixed \(R\), iterate the integral equations (A.6) on a short
interval. Work in a closed set of continuous paths with slightly
enlarged operator and mean-square bounds, and impose the pointwise
bound \(|W^{(4)}(s)|\le as\). Every integral iterate preserves
the latter. The path set is complete in the supremum of (A.7):
a common pointwise bound survives mean-square convergence.
A sufficiently short interval makes the integral map a contraction
and preserves the other enlarged bounds. Its unique fixed point
is the local solution. No differentiability of every coordinate
map on an unrestricted \(L^2\) ball is asserted.

The bounds (A.8)--(A.9) allow this argument to restart finitely many
times on any fixed finite \(S\), for fixed \(R\). Thus each clipped
flow exists uniquely for all feature times. Its state velocity is
bounded and its vector field is Lipschitz, so integrating a one-step
Euler defect gives the recurrence
\[
 e_{k+1}\le(1+C_S(1+R)\Delta)e_k+C_{R,S}\Delta^2.
\]
It follows that
\[
 \sup_{s\le S}
 \rho(\theta^{R,\mathrm{Euler}}(s),\theta^R(s))
 \le C_{R,S}\Delta.                                    \tag{A.10}
\]
Use constant Euler interpolation here; movement inside one step
is included in the bound. The same estimate is uniform in finite
width on the indicated initialization event.

At fixed \(R,\Delta,M\), Gaussian conditioning and the finite-step
oracle comparison identify the finite Euler empirical laws with
the population Euler laws on these common spaces. Tiny Gaussian
readout initialization changes no such limit: its normalized
size tends to zero and its coordinate maximum is bounded with
probability tending to one. Apply (A.10), first fixing \(\Delta\)
while width tends to infinity, then sending \(\Delta\) to zero.
This proves the fixed-\(R\) width limit uniformly on \([0,S]\).

This statement includes every fixed finite calculation from the
current state using matrix actions in either direction, globally
Lipschitz coordinate maps, and bounded products. Its difference
is bounded by a constant times (A.7). Joint empirical convergence
includes second moments, initially by the Gaussian calculation
and then by the mean-square comparisons in (A.10). Hence continuous
measurements of at most quadratic growth on each finite node list
converge as well. A measurement is an ordinary function of the
listed coordinates, averaged over neurons; trained coordinates
are not asserted independent.

All conclusions here concern fixed clipping unless explicitly
stated otherwise. Removing clipping requires the separate
mesh-uniform local tail estimate and comparison argument.
Extending the resulting uncut flow beyond that local interval
requires a further continuation theorem.


<a id="l3-bootstrap"></a>

## 5. Mesh-uniform local response bootstrap

### Frozen-coefficient scalar system

Write \(a=\pi/2\), \(\phi=\arctan\), \(F(x)=x+x^3/3\), and
\(\chi=\phi\circ F^{-1}\), so
\[
 |\phi|\le a,\quad |\phi'|\le1,\quad |\phi''|\le2,\qquad
 |\chi|\le a,\quad |\chi'|\le1.
\]
Let \(\Delta>0\), \(S=M\Delta\le1\), and consider indices
\(0\le k\le M\). The population scalar Euler equations identified in §3 are
\[
 X^{(1)}_{k}=F(Z^{(1)}_{0})+\Delta\sum_{r<k}Q^{(1)}_{r},\qquad
 H^{(1)}_{k}=\chi(X^{(1)}_{k}),
\]
\[
 Z^{(2)}_{k}=\xi^{(2)}_{k}+\sum_{r<k}a^{(2)}_{kr}\delta^{(2)}_{r},
 \qquad H^{(2)}_{k}=\phi(Z^{(2)}_{k}),
\]
\[
 Z^{(3)}_{k}=\xi^{(3)}_{k}+\sum_{r<k}a^{(3)}_{kr}\delta^{(3)}_{r},
 \qquad H^{(3)}_{k}=\phi(Z^{(3)}_{k}),
\]
\[
 W_k^{(4)}=\Delta\sum_{r<k}H^{(3)}_{r},\qquad
 \delta^{(3)}_{k}=W_k^{(4)}\phi'(Z^{(3)}_{k}),
\]
\[
 Q^{(2)}_{k}=\zeta^{(2)}_{k}+\sum_{v\le k}b^{(3)}_{kv}H^{(2)}_{v},\qquad
 \delta^{(2)}_{k}=\phi'(Z^{(2)}_{k})\tau_R(Q^{(2)}_{k}),
\]
\[
 Q^{(1)}_{k}=\zeta^{(1)}_{k}+\sum_{v\le k}b^{(2)}_{kv}H^{(1)}_{v}.
\]
Assume a differentiable clipping function satisfying
\[
 |\tau_R(x)|\le|x|,\qquad |\tau_R'(x)|\le1.
\]
The deterministic coefficients are
\[
 a^{(\ell)}_{ks}
 =\mathbb E_{\ell-1}\frac{\partial H^{(\ell-1)}_{k}}{\partial\zeta^{(\ell-1)}_{s}}
       +\Delta\,\mathbb E_{\ell-1}[H^{(\ell-1)}_{k}H^{(\ell-1)}_{s}],
 \qquad s<k,
\]
\[
 b^{(\ell)}_{ks}
 =\mathbb E_\ell\frac{\partial\delta^{(\ell)}_{k}}{\partial\xi^{(\ell)}_{s}}
       +\Delta\mathbf1_{\{s<k\}}
                         \mathbb E_\ell[\delta^{(\ell)}_{k}\delta^{(\ell)}_{s}],
 \qquad s\le k.
\]
All displayed source derivatives are formal derivatives of the scalar
program with its deterministic coefficients held fixed. They are not
derivatives of a covariance factorization. This convention is essential,
including when source covariance matrices are singular.

The four centered Gaussian source groups have covariance
\[
 \mathbb E_\ell[\xi^{(\ell)}_{k}\xi^{(\ell)}_{s}]
     =\mathbb E_{\ell-1}[H^{(\ell-1)}_{k}H^{(\ell-1)}_{s}],\qquad
 \mathbb E_{\ell-1}[\zeta^{(\ell-1)}_{k}\zeta^{(\ell-1)}_{s}]
     =\mathbb E_\ell[\delta^{(\ell)}_{k}\delta^{(\ell)}_{s}].
\]
Within each group arbitrary correlations across times are allowed.
The groups are independent by the source-identification lemma in §3.

Define deterministic row sums
\[
 U_k=\sum_{s\le k}|b^{(2)}_{ks}|,\qquad
 V_k=\sum_{s\le k}|b^{(3)}_{ks}|.
\]
At \(k=0\), \(W_0^{(4)}=0\), both backward Gaussian variances are zero,
and \(U_0=V_0=0\).

### Bottom response: one factor of the source-time mesh

Suppose \(U_r\le1\) for every \(r<k\). Differentiating the bottom
recursion with respect to \(\zeta^{(1)}_{s}\) gives
\[
 \left|\frac{\partial X^{(1)}_{j}}{\partial\zeta^{(1)}_{s}}\right|
 \le\Delta\mathbf1_{\{s<j\}}
 +\Delta\sum_{r<j}\sum_{v\le r}|b^{(2)}_{rv}|
                   \left|\frac{\partial X^{(1)}_{v}}{\partial\zeta^{(1)}_{s}}\right|.
\]
Discrete Gronwall, also using \(|\chi'|\le1\), yields
\[
 \left|\frac{\partial H^{(1)}_{j}}{\partial\zeta^{(1)}_{s}}\right|
 \le\Delta e^S\quad(s<j\le k).
\]
Consequently, with the fixed constant
\[
 A=a^2+e,
\]
one has
\[
 |a^{(2)}_{js}|\le A\Delta\quad(s<j\le k).                   \tag{B.1}
\]
No size estimate on a realization of \(Q^{(1)}\), and no derivative of a
Gaussian covariance, is used in this step.

### Middle response and its exponential envelope

Assume additionally \(V_r\le1\) for all \(r<k\). Put
\[
 \mathcal S_j=\sum_{s\le j}
       \left|\frac{\partial Z^{(2)}_{j}}{\partial\xi^{(2)}_{s}}\right|,
 \qquad
 \overline{\mathcal S}_j=\max_{v\le j}\mathcal S_v,
\]
\[
 E_j=\exp\left(A\Delta\sum_{r<j}(2|Q^{(2)}_{r}|+V_r)\right).
\]
The source derivative of the clipped middle backward field satisfies
\[
 \left|\partial\delta^{(2)}_{r}\right|
 \le2|Q^{(2)}_{r}|\,|\partial Z^{(2)}_{r}|
       +|\partial Q^{(2)}_{r}|.
\]
For a derivative with respect to a \(\xi^{(2)}\) source,
\[
 |\partial Q^{(2)}_{r}|
 \le\sum_{v\le r}|b^{(3)}_{rv}|\,|\partial Z^{(2)}_{v}|.
\]
Using (B.1), summing the absolute source derivatives, and applying
discrete Gronwall gives
\[
 \overline{\mathcal S}_j\le E_j\quad(j\le k).             \tag{B.2}
\]
For an individual \(\zeta^{(2)}_{s}\) derivative there is instead the
additional source term \(\mathbf1_{\{r=s\}}\). Its first effect on
\(Z^{(2)}_{j}\) carries \(a^{(2)}_{js}\), so the same argument gives
\[
 \left|\frac{\partial Z^{(2)}_{j}}{\partial\zeta^{(2)}_{s}}\right|
 \le A\Delta E_j,\qquad s<j\le k.                       \tag{B.3}
\]
There is no dependence on \(\zeta^{(2)}_{j}\) in \(Z^{(2)}_{j}\).

The envelope has uniform moments despite the unbounded Gaussian part
of \(Q^{(2)}\). Indeed
\[
 |W_r^{(4)}|\le aS,\qquad |\delta^{(3)}_{r}|\le aS,
 \qquad \operatorname{Var}(\zeta^{(2)}_{r})\le a^2S^2,
\]
and
\[
 |Q^{(2)}_{r}|\le|\zeta^{(2)}_{r}|+aV_r.
\]
If \(V_*=\max_{r<j}V_r\), Jensen's inequality over the finitely many
times, followed by the one-variable Gaussian exponential bound, gives,
for \(p\ge1\),
\[
 \begin{aligned}
 \mathbb E_2 E_j^p
 &\le e^{pA(2a+1)SV_*}
       \mathbb E_2\exp\left(2pA\Delta\sum_{r<j}|\zeta^{(2)}_{r}|\right)\\
 &\le 2\exp\left(pA(2a+1)SV_*+2p^2A^2a^2S^4\right).
 \end{aligned}                                           \tag{B.4}
\]
For \(j=0\), \(E_0=1\) directly. For \(j>0\), the Jensen step is
\[
 \exp\left(2pA\Delta\sum_{r<j}|\zeta^{(2)}_{r}|\right)
 \le\frac1j\sum_{r<j}
              \exp(2pAj\Delta|\zeta^{(2)}_{r}|).
\]
Only the marginal variances of the Gaussian sources enter this
calculation. Neither their time independence nor independence of a
source from the bounded response shift is needed.

For explicit fixed constants, let
\[
 M_p=2^{1/p}\exp\left(A(2a+1)+2pA^2a^2\right).
\]
Under \(S,V_*\le1\), (B.4) implies \(\|E_j\|_{L^p(\Omega_2)}\le M_p\).
Equations (B.3) and the definition of \(a^{(3)}\) therefore give
\[
 |a^{(3)}_{js}|\le A_3\Delta,\qquad
 A_3=a^2+A M_1,\qquad s<j\le k.                         \tag{B.5}
\]

### Top response is bounded pointwise

Let
\[
 T_j=\sum_{s\le j}
       \left|\frac{\partial Z^{(3)}_{j}}{\partial\xi^{(3)}_{s}}\right|,
 \qquad \overline T_j=\max_{v\le j}T_v.
\]
Since \(W_j^{(4)}=\Delta\sum_{r<j}H^{(3)}_{r}\),
\[
 \sum_{s\le j}\left|
       \frac{\partial\delta^{(3)}_{j}}{\partial\xi^{(3)}_{s}}\right|
 \le\Delta\sum_{r<j}T_r+2aS T_j
 \le(1+2a)S\overline T_j.                               \tag{B.6}
\]
Together with (B.5), this implies the deterministic bound
\[
 \overline T_j\le\exp((1+2a)A_3S^2)\quad(j\le k).
\]
Taking expectations in (B.6) and adding the learned term gives
\[
 V_k\le(1+2a)S\exp((1+2a)A_3S^2)+a^2S^3
       \le C_3S,                                       \tag{B.7}
\]
where
\[
 C_3=(1+2a)\exp((1+2a)A_3)+a^2.
\]
In particular, the current row \(b^{(3)}_{k\cdot}\) is bounded before
estimating the current \(Q^{(2)}_{k}\).

### Current middle backward field and bottom response

Equation (B.7) gives
\[
 \|Q^{(2)}_{k}\|_{L^2(\Omega_2)}\le aS+aV_k\le QS,\qquad Q=a(1+C_3).
                                                               \tag{B.8}
\]
These are population norms on \(\Omega_2\). The same bound holds at earlier indices under
the same bootstrap argument.

Differentiating the current middle backward field with respect to the
\(\xi^{(2)}\) source row and using (B.2) gives
\[
 \sum_{s\le k}
  \left|\frac{\partial\delta^{(2)}_{k}}{\partial\xi^{(2)}_{s}}\right|
 \le(2|Q^{(2)}_{k}|+V_k)\overline{\mathcal S}_k.
\]
Cauchy--Schwarz and (B.4), (B.7), (B.8) yield
\[
 \begin{aligned}
 U_k
 &\le(2\|Q^{(2)}_{k}\|_{L^2(\Omega_2)}+V_k)
                      \|\overline{\mathcal S}_k\|_{L^2(\Omega_2)}
       +S\max_{r\le k}\|\delta^{(2)}_{r}\|_{L^2(\Omega_2)}^2\\
 &\le[(2Q+C_3)M_2+Q^2]\,S=:C_2S.                      \tag{B.9}
 \end{aligned}
\]
In the last line \(S\le1\) and
\(\|\delta^{(2)}_{r}\|_{L^2(\Omega_2)}\le\|Q^{(2)}_{r}\|_{L^2(\Omega_2)}\le QS\) were used.
There is no circular use of \(U_k\) in either (B.7) or (B.9).

### First-exit closure and source dependencies

Choose the explicit positive horizon
\[
 S_0=\min\left\{1,\frac1{2C_2},\frac1{2C_3}\right\}.
\]
Fix any \(S=M\Delta\le S_0\). If \(k\) were the first index at which
\(U_k>1\) or \(V_k>1\), all earlier rows satisfy the bootstrap
hypotheses. The estimates above give
\[
 V_k\le C_3S\le\frac12,\qquad
 U_k\le C_2S\le\frac12,
\]
a contradiction. For use of the earlier-index bound in (B.9), apply
(B.7)--(B.8) at each \(r\le k\); their premises involve only rows strictly
earlier than \(r\). Equivalently, induct simultaneously on the sharper
conclusions \(U_r\le C_2S\), \(V_r\le C_3S\).

The causal order for the current index is
\[
 a^{(2)}_{k\cdot}\ \longrightarrow\ H^{(2)}_{k}\
 \longrightarrow\ a^{(3)}_{k\cdot}\ \longrightarrow\
 \delta^{(3)}_{k}\ \longrightarrow\ b^{(3)}_{k\cdot}\
 \longrightarrow\ Q^{(2)}_{k},\delta^{(2)}_{k}\
 \longrightarrow\ b^{(2)}_{k\cdot}.
\]
More explicitly:

- \(H^{(1)}_{k}\) uses only bottom response rows with time \(<k\).
- \(H^{(2)}_{k}\) uses only middle backward fields at times \(<k\).
- The derivative of \(H^{(2)}_{k}\) with respect to a past \(\zeta^{(2)}\)
  source consequently uses only \(b^{(3)}\) rows with time \(<k\).
- The top scalar recursion uses only its own \(\xi^{(3)}\) source group
  once its deterministic \(a^{(3)}\) row is fixed.
- The current \(b^{(3)}\) row determines the bounded shift of
  \(Q^{(2)}_{k}\), after which the current \(b^{(2)}\) row is estimated.

Thus differentiating the explicit scalar program under the stated
frozen-coefficient convention retains every permitted source path.
If a different convention differentiates the deterministic coefficient
selection or a covariance square root, these derivative estimates do not apply to
that different derivative.

### Uniform local tail actually obtained

The closure gives, uniformly in \(k\le M\), \(M\), \(\Delta\), and \(R\),
\[
 Q^{(2)}_{k}=\zeta^{(2)}_{k}+\beta^{(2)}_{k},\qquad
 \operatorname{Var}(\zeta^{(2)}_{k})\le a^2S^2,\qquad
 |\beta^{(2)}_{k}|\le aC_3S.
\]
The shift may depend on the Gaussian source; its deterministic amplitude
bound suffices. For \(x>0\),
\[
 \mathbb P\bigl(|Q^{(2)}_{k}|>aC_3S+x\bigr)
 \le2\exp\left(-\frac{x^2}{2a^2S^2}\right).              \tag{B.10}
\]
Consequently \(\|Q^{(2)}_{k}\|_{L^p(\Omega_2)}\le C S\sqrt p\) for \(p\ge2\), with
a constant independent of mesh and clipping. The same conclusion
holds for \(\delta^{(2)}_{k}\), since clipping and the gate do not increase
its absolute value.

This estimate is obtained on \(S\le S_0\). The constants above are
deliberately conservative; no claim is made that \(S_0\) contains the
full optimization feature horizon.

### The proof mesh and raw GD

The displayed population bottom update is Euler in \(X^{(1)}=F(Z^{(1)})\):
\[
 X^{(1)}_{k+1}=X^{(1)}_{k}+\Delta Q^{(1)}_{k}.
\]
It is not exactly the map obtained by applying \(F\) after one ordinary
Euler step in \(z^{(1)}\). It is a valid discretization of the same
continuous transformed equation, and its scalar finite-program
response representation must be justified for that discretization.
This distinction does not alter any estimate above, but it matters
when stating which finite algorithm has been identified.


<a id="l3-bridge"></a>

## 6. Removal of clipping, raw GD, and physical time

This section removes clipping using the source-identification lemma
in §3, its common-space realization in §4, and the mesh-uniform tail
bound in §5. These preceding results establish the representation used
here. No tail assumption is imposed on a competing uncut solution.
All conclusions below hold on the explicit local interval.

### Setting and the established representation lemma

Let \(\phi=\arctan\), \(a=\pi/2\),
\[
F(z)=z+z^3/3,\qquad \chi=\phi\circ F^{-1}.
\]
Both \(F^{-1}\) and \(\chi\) are 1-Lipschitz, and \(|\chi|\le a\).
There are three layer probability spaces and bounded initial
operators \(W_0^{(2)},W_0^{(3)}\) between adjacent \(L^2\) spaces,
together with their adjoints. These are the population actions
generated by the two independent Gaussian initial matrices.
The transformed state is
\[
\Theta=(X^{(1)},W^{(2)},W^{(3)},W^{(4)}),
\]
and its forward and backward measurements are
\[
Z^{(1)}=F^{-1}(X^{(1)}),\quad H^{(1)}=\chi(X^{(1)}),
\quad Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),
\]
\[
Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}),
\quad \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),
\]
\[
Q^{(2)}=(W^{(3)})^*\delta^{(3)},\qquad
\delta_R^{(2)}=\phi'(Z^{(2)})\tau_R(Q^{(2)}),\qquad
Q_R^{(1)}=(W^{(2)})^*\delta_R^{(2)}.
\]
Choose continuously differentiable clipping maps satisfying
\[
\operatorname{Lip}(\tau_R)\le1,\quad
\tau_R(x)=x\ (|x|\le R),\quad
|\tau_R(x)|\le |x|,\quad |\tau_R(x)|\le2R.
\]
Take integer \(R\ge1\); write \(R=\infty\) for the identity map.
Only the middle backward field is clipped. The feature-time
vector field is
\[
\mathcal V_R(\Theta)=
\left(Q_R^{(1)},\
\delta_R^{(2)}\otimes H^{(1)},\
\delta^{(3)}\otimes H^{(2)},\
H^{(3)}\right),                                        \tag{C.1}
\]
where \(U\otimes V\) has the layer-typed meaning fixed at the
beginning of the chapter.
Initially \(W_0^{(4)}=0\) and \(X_0^{(1)}=F(Z_0^{(1)})\), with
\(Z_0^{(1)}\sim N(0,1)\).

The finite-width version uses \(x^{(1)}=F(z^{(1)})\), replaces
adjoints by transposes, and uses \(uv^{T}/n\) for \(u\otimes v\).
Each population \(L^2\) norm is replaced by \(\|v\|_2/\sqrt n\).
Its initial hidden matrices have independent \(N(0,1/n)\) entries,
and its first-layer coordinates are iid standard Gaussians.

**Lemma 6.1 (representation and uniform exponential moment).** For every fixed clipping level \(R\)
and fixed finite transformed Euler mesh on \([0,S_0]\), the
population action Euler program has exactly the scalar
Gaussian/response representation of [§3](#l3-source), estimated in
[§5](#l3-bootstrap), with the prescribed initialization
and the frozen-coefficient derivative convention. In particular,
for some deterministic \(K<\infty\), independent of \(R\), mesh,
and time index,
\[
\mathbb E_2\exp\left(\frac{(Q_{R,k}^{(2)})^2}{K^2}\right)\le2.
                                                               \tag{C.2}
\]
**Proof.** Section 3 identifies the finite empirical-feedback Euler
program with the four Gaussian source groups and the full formal response
derivatives, including singular queries. Section 4 realizes these same
finite joint laws on the common population action spaces. Thus the Euler
coordinates on those spaces satisfy exactly the recursion of §5.
Its first-exit argument gives a Gaussian part with variance at most
\(a^2S_0^2\) and a shift bounded by \(aC_3S_0\), uniformly in the
mesh and clipping level. The one-variable Gaussian tail bound there,
integrated against \(e^{x^2/K^2}\), gives (C.2) for a sufficiently large
deterministic \(K\). No covariance inverse is taken in this passage.
This proves both the representation and the exponential moment before
they are used below.

Measure two states on the same spaces by
\[
\begin{aligned}
\rho(\Theta,\widetilde\Theta)
={}&\|X^{(1)}-\widetilde X^{(1)}\|_{L^2}
 +\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}\\
&+\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}
 +\|W^{(4)}-\widetilde W^{(4)}\|_{L^2}.                 \tag{C.3}
\end{aligned}
\]
Write \(\rho_n\) for its finite-width counterpart. No operator-norm
distance between operators acting on different widths is asserted.
Across widths the conclusion concerns their joint measured laws.

### Uniform primal bounds and fixed-cutoff well-posedness

Fix a feature horizon \(S\le S_0\). The following bounds depend on
\(S\), an initial operator bound \(M\), and an initial normalized
readout bound, but not on \(R\) or width. With zero readout,
\[
\|W^{(4)}(s)\|_\infty\le as,\qquad
\|W^{(4)}(s)\|_{L^2}\le as.
\]
For every finite cutoff, and for an uncut solution while it exists,
\[
\|\delta^{(3)}\|_{L^2}\le\|W^{(4)}\|_{L^2},\qquad
\|\delta_R^{(2)}\|_{L^2}
\le\|Q^{(2)}\|_{L^2}
\le\|W^{(3)}\|_{\rm op}\|W^{(4)}\|_{L^2}.
\]
Successively integrating the last three blocks of (C.1) gives finite
polynomial bounds on \(W^{(3)},W^{(2)}\). For instance the coarser
bounds
\[
Q=aS,\qquad R_3=M+aQS,\qquad R_2=M+aR_3QS              \tag{C.4}
\]
bound the readout \(L^2\) norm and the two operator norms.
Also
\[
\|Q_R^{(1)}\|_{L^2}\le R_2R_3Q.
\]
These estimates hold for positive-step Euler paths whose step sum
is at most \(S\), and for their straight interpolants.
With a nonzero initial readout of \(L^2\) norm at most one, use
\(Q=1+aS\) instead. The norm of every block of (C.1), in the norm
associated with (C.3), is bounded by a constant \(C\) independent of
cutoff and width.

Suppose both hidden operator norms and readout \(L^2\) norms are
bounded as above, and a reference state's readout has pointwise
bound \(B\). Successive forward differences give
\[
\|Z^{(2)}-\widetilde Z^{(2)}\|_{L^2}
\le a\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
 +R_2\|X^{(1)}-\widetilde X^{(1)}\|_{L^2},
\]
\[
\|Z^{(3)}-\widetilde Z^{(3)}\|_{L^2}\le C\rho.
\]
For the top gate, place the bounded readout in the second term:
\[
\delta^{(3)}-\widetilde\delta^{(3)}
=\phi'(Z^{(3)})(W^{(4)}-\widetilde W^{(4)})
 +[\phi'(Z^{(3)})-\phi'(\widetilde Z^{(3)})]
       \widetilde W^{(4)}.
\]
Therefore
\[
\|\delta^{(3)}-\widetilde\delta^{(3)}\|_{L^2}
 +\|Q^{(2)}-\widetilde Q^{(2)}\|_{L^2}\le C\rho.           \tag{C.5}
\]
The constant uses the reference pointwise bound \(B\); it does not
use a pointwise bound on the other readout.

For two states clipped at the same \(R\), (C.5), boundedness of
\(\tau_R\), and \(\operatorname{Lip}(\phi')\le2\) give
\[
\|\delta_R^{(2)}-\widetilde\delta_R^{(2)}\|_{L^2}
\le C(1+R)\rho.
\]
The rank-one inequality
\[
\|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
\le\|u-\widetilde u\|_{L^2}\|v\|_{L^2}
 +\|\widetilde u\|_{L^2}\|v-\widetilde v\|_{L^2}
\]
now proves
\[
\|\mathcal V_R(\Theta)-\mathcal V_R(\widetilde\Theta)\|
\le C(1+R)\rho.                                           \tag{C.6}
\]
All these estimates are identical at finite width.

For each fixed \(R\), Picard iteration in continuous paths with
the norm (C.3) gives existence and uniqueness on a short interval.
The set imposing a common readout pointwise bound is closed in
\(L^2\): a convergent sequence has an almost-everywhere convergent
subsequence preserving that bound. The integral update of the
readout preserves the bound \(as\), and (C.4) permits continuation
to all of \([0,S]\). The same proof works at finite width.
The Euler local error is at most
\(\tfrac12 C^2(1+R)\Delta^2\), because of the velocity bound and
(C.6). A discrete Gronwall estimate consequently gives
\[
\sup_{s\le S}\rho(\Theta_{R,\Delta}(s),\Theta_R(s))
\le C_{R,S}\Delta,                                     \tag{C.7}
\]
and the identical estimate in \(\rho_n\), uniformly in width on the
initial operator-bound event. The estimates (C.4) directly control
the Euler paths, so no assumption about monotonicity of a clipped
predictor is used.

### The asymmetric estimate and removal of clipping

Compare an uncut state \(A\), or a state clipped at \(R'\ge R\),
with a reference state \(B\) clipped at \(R\). In (C.5) take \(B\)
as the bounded-readout reference. Keeping the activation derivatives
explicit, the exact decomposition is
\[
\begin{aligned}
\delta_{R'}^{(2)}(A)-\delta_R^{(2)}(B)
={}&\phi'(Z_A^{(2)})[\tau_{R'}(Q_A^{(2)})-\tau_{R'}(Q_B^{(2)})]\\
&+(\phi'(Z_A^{(2)})-\phi'(Z_B^{(2)}))\tau_R(Q_B^{(2)})\\
&+\phi'(Z_A^{(2)})[\tau_{R'}(Q_B^{(2)})-\tau_R(Q_B^{(2)})].
\end{aligned}                                                        \tag{C.8}
\]
This also holds when \(R'=\infty\). The last bracket vanishes on
\(|Q_B^{(2)}|\le R\) and is at most \(2|Q_B^{(2)}|\) otherwise.
To avoid discontinuous tail measurements define the 1-Lipschitz
continuous function
\[
b_R(q)=(|q|-R/2)_+.
\]
Then \(|q|\mathbf1_{\{|q|>R\}}\le2b_R(q)\), and (C.8) implies
\[
\|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
\le C(1+R)\rho(A,B)+C\|b_R(Q_B^{(2)})\|_{L^2}.             \tag{C.9}
\]
The constant depends only on the common primal bounds and the
reference readout pointwise bound, not on \(R'\).

By (C.7) and (C.5), for each fixed \(R\) the Euler \(Q^{(2)}\) variables
converge in \(L^2\) to \(Q_R^{(2)}(s)\), at every fixed \(s\).
An almost-everywhere convergent subsequence and Fatou's lemma
therefore pass (C.2) to the exact clipped solution:
\[
\mathbb E_2\exp((Q_R^{(2)}(s))^2/K^2)\le2
\qquad(0\le s\le S).                                  \tag{C.10}
\]
The constant is the same for every \(R\) and \(s\).
If \(\mathbb E e^{q^2/K^2}\le2\), then
\[
\mathbb E[q^2\mathbf1_{\{|q|>u\}}]
\le4K^2e^{-u^2/(2K^2)}.
\]
For example, use
\(q^2e^{-q^2/(2K^2)}\le2K^2/e\) and the exponential moment.
Consequently
\[
\sup_{s\le S}\|b_R(Q_R^{(2)}(s))\|_{L^2}
\le 2K e^{-R^2/(16K^2)}=:\varepsilon_R.                \tag{C.11}
\]

Subtracting two integral equations and applying scalar Gronwall
to (C.9) yields
\[
\sup_{s\le S}\rho(\Theta_{R'}(s),\Theta_R(s))
\le e^{C(1+R)S}
\left[\rho(\Theta_{R'}(0),\Theta_R(0))+CS\varepsilon_R\right].
                                                               \tag{C.12}
\]
For common initialization, the right side tends to zero as
\(R\to\infty\), uniformly in \(R'\ge R\). The clipped solutions
therefore have a limit \(\Theta\) in the complete space of
continuous paths with distance (C.3). It retains the primal bounds
and the readout pointwise bound.

There is no unresolved passage through an unbounded product here:
(C.5) gives \(Q_R^{(2)}\to Q^{(2)}(\Theta)\) in \(L^2\), and (C.9),
now evaluated at the limiting state and its clipped reference,
gives
\[
\sup_{s\le S}
\|\mathcal V_\infty(\Theta(s))-\mathcal V_R(\Theta_R(s))\|
\le C(1+R)\sup_s \rho(\Theta(s),\Theta_R(s))+C\varepsilon_R
\longrightarrow0.
\]
Pass to the limit in the integral equations. The result is an
uncut solution of (C.1), and the uniform velocity convergence also
makes it continuously differentiable in the Banach norm.

If \(\widetilde\Theta\) is any other uncut integral solution with
the same initialization and bounded primal norms on this interval,
apply (C.9) against \(\Theta_R\). No tail bound for
\(\widetilde\Theta\) is used. Its own bound may change \(C\), but
\(e^{CR}\varepsilon_R\to0\) still holds. Thus (C.12) implies
\(\widetilde\Theta=\Theta\). This proves uniqueness in the
bounded-primal solution class on the common population spaces.

This uniqueness also permits restarting along the constructed
trajectory inside the same local interval. Fix
\(0\le\sigma<S\le S_0\), and let \(\widetilde\Theta\) be any
bounded-primal uncut solution on \([\sigma,S]\) with
\(\widetilde\Theta(\sigma)=\Theta(\sigma)\). Compare it with
the restriction of \(\Theta_R\), whose initial discrepancy at
\(\sigma\) is already controlled by (C.12). For constants
\(C_0,C_1\) independent of \(R\),
\[
\begin{aligned}
\sup_{\sigma\le s\le S}
\rho(\widetilde\Theta(s),\Theta_R(s))
\le{}&e^{C_1(1+R)(S-\sigma)}
\left[\rho(\Theta(\sigma),\Theta_R(\sigma))
 +C_1(S-\sigma)\varepsilon_R\right],\\
\rho(\Theta(\sigma),\Theta_R(\sigma))
\le{}&C_0S e^{C_0(1+R)S}\varepsilon_R .
\end{aligned}
\]
Both right sides tend to zero because
\(\varepsilon_R=2K e^{-R^2/(16K^2)}\). Hence
\(\widetilde\Theta=\Theta\) on \([\sigma,S]\).
This is restart uniqueness only within the already constructed
feature interval; it supplies no continuation beyond \(S_0\).

### Fixed-program laws, empirical feedback, and the finite tails

The finite Gaussian construction in §3 supplies the following
width comparison. At fixed \(R,\Delta\),
expand both learned matrices as finite sums of rank-one updates.
Replace their empirical contractions temporarily by the deterministic
population contractions. This defines a finite oracle program.
Its coordinate operations are globally Lipschitz: \(\chi\) is
globally Lipschitz, the middle product has a bounded clipped factor,
and the top readout factor is deterministically bounded by \(aS\)
and can be clipped at that bound without changing oracle values.
The root tuple may include \((Z_0^{(1)},F(Z_0^{(1)}))\), which has
finite second moments.

Gaussian conditioning applies separately to each of the two initial
matrices and its reused transpose. At each new query its input is
measurable with respect to the preceding history. Conditional on old
forward and transpose answers, the residual of the queried matrix
is a fresh Gaussian matrix projected orthogonally to its old input
and output query spans. The other matrix's conditional residual is
unchanged. This sequential argument preserves the required
conditional residual independence even though the queries use both
matrices.

As in [§1.2](#l2-gaussian), add independent Gaussian noise of
size \(\epsilon\) to each of finitely many query inputs. Limiting
Gram matrices then have positive Schur complements. Conditioning,
the law of large numbers for the fresh Gaussian coordinates, and
vanishing normalized norms of finite-rank projections give joint
\(\mathcal W_2\) limits, including all contractions. Remove the
input noises using the initial operator bounds and Lipschitz
stability of this fixed finite program. Constants may depend on
its size and on \(R,\Delta\); no uniformity in the program length
is needed here.

For clarity, an oracle preactivation need not equal the action of
its stored finite matrix memory. Their exact difference is a finite
sum of earlier backward vectors multiplied by empirical-minus-
population activation contractions. The corresponding transpose
discrepancy uses activation vectors multiplied by backward
contraction errors. All these scalar errors tend to zero in
probability by the joint \(\mathcal W_2\) limit. Fixed-step
induction, using (C.6), then compares the oracle with empirical-feedback
clipped Euler and proves the same joint limits for the latter.
This argument is performed before sending \(\Delta\) to zero.

Taking a countable family of finite programs, closed under finite
unions, rational linear combinations, the two matrices and their
transposes, and bounded Lipschitz coordinate operations, constructs
common layer probability spaces. The initial operator bounds pass
to their dense probe classes and extend both initial actions and
adjoints to the generated \(L^2\) spaces. Finite adjunction identities
pass to the limit. This is the common action construction used
above. Lemma 6.1 identifies these clipped Euler coordinate laws with
the scalar laws satisfying (C.2).

Combining fixed-program convergence with (C.7), first at fixed
\(\Delta\) and then letting \(\Delta\to0\), proves fixed-\(R\)
finite-clipped-flow convergence of every finite joint list of the
globally Lipschitz forward/backward measurements, in \(\mathcal W_2\).
The elementary coupling bound used in every same-width comparison is
\[
\mathcal W_2\left(\frac1n\sum_i\delta_{v_i},
                  \frac1n\sum_i\delta_{\widetilde v_i}\right)
\le\frac{\|v-\widetilde v\|_2}{\sqrt n}.
\]
The vector-field bound in (C.4) supplies time equicontinuity.

In particular, write \(\Theta_{n,R}\) for the finite clipped flow
from zero readout and let
\[
a_{n,R}(s)=
\left(\frac1n\sum_i b_R(q_{n,R,i}^{(2)}(s))^2\right)^{1/2},
\qquad
a_R(s)=\|b_R(Q_R^{(2)}(s))\|_{L^2}.
\]
For every fixed \(R\),
\[
\sup_{s\le S}|a_{n,R}(s)-a_R(s)|
\longrightarrow0\quad\text{in probability}.            \tag{C.13}
\]
Indeed \(b_R\) is 1-Lipschitz, its squared measurement is continuous
with quadratic growth, and thus its norm converges at each fixed
time by \(\mathcal W_2\) convergence. Also (C.5) and the uniform state
velocity bound make \(q_{n,R}^{(2)}(s)\), and hence \(a_{n,R}(s)\),
Lipschitz in \(s\), with a common constant on the initial
operator-bound event. A finite time net upgrades the convergence
to (C.13). No finite-width exponential moment, nor a discontinuous
indicator measurement, is required.

### Finite uncut flow and the small prescribed readout

The prescribed finite initialization has
\[
W_{i,0}^{(4)}\sim N(0,n^{-2}),\qquad
\frac{\|W_0^{(4)}\|_2}{\sqrt n}=O_{\mathbb P}(n^{-1}).
\]
The two initial Gaussian operator norms are bounded by a fixed
\(M\) with probability tending to one. Couple the uncut finite flow
to \(\Theta_{n,R}\) using the same first-layer roots and matrices,
but keep the latter's readout initially zero. By (C.9),
\[
\sup_{s\le S}\rho_n(\Theta_n^{\rm flow}(s),\Theta_{n,R}(s))
\le e^{C(1+R)S}
\left[
\frac{\|W_0^{(4)}\|_2}{\sqrt n}
 +C\int_0^S a_{n,R}(u)\,du
\right].                                               \tag{C.14}
\]
The finite uncut flow exists on this interval by its polynomial
primal estimates; this step does not invoke an unproved uncut
stability theorem. The bounded-readout reference in (C.5) also means
that no coordinatewise-smallness assumption on the nonzero
readout is needed in (C.14).

At fixed \(R\), (C.11), (C.13), and (C.14) give an asymptotic bound
\(CS e^{C(1+R)S}\varepsilon_R\). This tends to zero as
\(R\to\infty\). Combining (C.14), fixed-\(R\) action-law convergence,
and (C.12) proves the local uncut finite-flow action-law limit.

The norm estimate is strong enough for additional gate-containing
measurements. Equation (C.8) first controls \(\delta^{(2)}\), then
operator bounds control \(Q^{(1)}=(W^{(2)})^*\delta^{(2)}\).
Finite joint laws of \(Z^{(1)},Q^{(1)}\) therefore converge in
\(\mathcal W_2\), uniformly in time. Their population \(L^2\) paths
are continuous and have compact time images. Their squared tails
are uniformly integrable. Clipping \(Q^{(1)}\) at an additional
fixed level and then removing that auxiliary clip proves the
corresponding statements for
\(\phi'(Z^{(1)})Q^{(1)}\) and
\(\phi'(Z^{(1)})^2Q^{(1)}\). The same argument treats subsequent
bounded gates and operator calls in the named network velocities.
This requires no Gaussian tail for \(Q^{(1)}\).

### Exact raw GD on its variable computational clock

Use the prescribed raw GD with \(\eta=n^{-2}\). For this local
comparison no global coercivity theorem is needed. Set
\[
\varepsilon=\frac{\|W_0^{(4)}\|_2}{\sqrt n},\qquad
\bar S=\min\{S_0,1/(4a^2)\},\qquad T_0=\bar S/4,
\qquad K_\eta=\lceil T_0/\eta\rceil.
\]
Work on the event \(\varepsilon\le1/(8a)\), whose probability
tends to one, and take \(\eta\le\bar S/24\). For any prefix
whose previous feature increments are positive and whose current
clock \(s_k\) is at most \(\bar S\), the exact readout updates give
\[
\frac{\|W_k^{(4)}\|_2}{\sqrt n}\le\varepsilon+as_k,
\qquad
|f_{n,k}|\le a\varepsilon+a^2s_k\le\frac38.
\]
It follows at the current node that
\[
\frac54\eta\le\alpha_k=2\eta(1-f_{n,k})
\le\frac{11}{4}\eta<3\eta.
\]
Starting from \(s_0=0\), induct on the physical steps. If
\(k\eta\le T_0\) and \(s_k\le3k\eta\), then
\[
s_{k+1}\le3k\eta+3\eta
\le3T_0+3\eta\le\frac78\bar S.
\]
This closes the positive-clock induction for every step needed
on \([0,T_0]\), including the last interpolation endpoint.
Consequently
\[
0<\alpha_k\le3\eta,\qquad
s_k=\sum_{j<k}\alpha_j\le3k\eta
\quad(0\le k\le K_\eta),
\]
where the increment assertion is used for \(k<K_\eta\).
The positive-step primal estimates (C.4), with the initial
readout added, now apply on this prefix independently of width.
For the rest of this section take \(S=\bar S\).
Define \(x_k^{(1)}=F(z_k^{(1)})\). Coordinatewise, its update is
exactly
\[
\begin{aligned}
x_{k+1}^{(1)}
={}&x_k^{(1)}+\alpha_k q_{n,k}^{(1)}\\
&+\alpha_k^2 z_k^{(1)}\phi'(z_k^{(1)})^2
                         (q_{n,k}^{(1)})^2
 +\frac{\alpha_k^3}{3}\phi'(z_k^{(1)})^3
                         (q_{n,k}^{(1)})^3.
\end{aligned}                                                        \tag{C.15}
\]
Products and powers in (C.15) are coordinatewise. The other three
blocks already are Euler updates for the uncut field (C.1).
Uniform operator and readout bounds give
\(\|q_{n,k}^{(1)}\|_2/\sqrt n\le C\).
Since \(\sup_z|z|\phi'(z)^2<\infty\), the additional vector in
(C.15) has normalized Euclidean norm at most
\[
C(\alpha_k^2\sqrt n+\alpha_k^3 n).
\]
Consequently, on every prefix certified by the local bootstrap,
its summed norm is at most
\[
CS\left((\max_k\alpha_k)\sqrt n
             +(\max_k\alpha_k)^2n\right)
\le C_S(\eta\sqrt n+\eta^2n)\longrightarrow0.            \tag{C.16}
\]

Compare this perturbed uncut Euler path with the exact finite
clipped reference \(\Theta_{n,R}(s_k)\). Subtracting one reference
step and using (C.9) gives
\[
d_{k+1}\le[1+C(1+R)\alpha_k]d_k
 +C\alpha_k a_{n,R}(s_k)
 +C_R\alpha_k^2
 +C(\alpha_k^2\sqrt n+\alpha_k^3n).                     \tag{C.17}
\]
Here \(d_k=\rho_n(\Theta_n^{\rm GD}(s_k),\Theta_{n,R}(s_k))\).
Its initial value is the small normalized readout norm.

The randomness of the partition \((s_k)\) causes no tail issue.
The Lipschitz bound for \(a_{n,R}\) used in (C.13) gives pathwise,
for every partition with maximum step \(A_n\),
\[
\sum_{k<K}\alpha_k a_{n,R}(s_k)
\le\int_0^{s_K} a_{n,R}(u)\,du+C S A_n
\le\int_0^S a_{n,R}(u)\,du+C S A_n                    \tag{C.18}
\]
for \(K\le K_\eta\). It applies also to partial final intervals.
Thus (C.13), discrete
Gronwall in the positive increments \(\alpha_k\), and (C.16) give
\[
\begin{aligned}
\max_{0\le k\le K_\eta}d_k\le e^{C(1+R)S}\Big[
&\frac{\|W_0^{(4)}\|_2}{\sqrt n}
 +C\int_0^S a_{n,R}(u)\,du\\
&+C_R\eta+C_S(\eta\sqrt n+\eta^2n)\Big],
\end{aligned}                                                        \tag{C.19}
\]
All relevant clocks, including the last interpolation endpoint,
are at most \(7S/8\) by the local bootstrap.
For fixed \(R\), take \(n\to\infty\); then let \(R\to\infty\).
The right side tends to zero in probability by (C.11).

For interpolation of the original raw parameters, apply the exact
cubic identity (C.15) with any fractional step
\(0\le\alpha\le\alpha_k\). It gives the same vanishing bound between
the transform of the raw linear interpolant and the transformed
Euler interpolant. Thus (C.19) also controls the specified
interpolation uniformly between its nodes.

### Return to physical time and the local conclusions

Use \(\bar S,T_0\) from the local bootstrap above.
All previous arguments apply with \(S=\bar S\).
The zero-readout reference and limiting population paths obey
\(|f_R(s)|,|f(s)|\le a^2s\le1/4\). Their physical clocks are the
unique solutions of
\[
\frac{ds_R}{dt}=2[1-f_R(s_R)],\qquad
\frac{ds}{dt}=2[1-f(s)],\qquad s_R(0)=s(0)=0.            \tag{C.20}
\]
The predictors are uniformly Lipschitz in feature time because
the output map is Lipschitz in (C.3) on the primal bounds and the
state velocities are uniformly bounded. Thus (C.20) is an ordinary
scalar Lipschitz initial-value problem.

For the actual finite feature flow, the readout equation gives
\(\|W^{(4)}(s)\|_2/\sqrt n\le\varepsilon+as\).
Hence \(|f_n(s)|\le3/8\) while \(s\le\bar S\), on the same
event \(\varepsilon\le1/(8a)\). Its physical clock therefore
has derivative in \([5/4,11/4]\subset(0,3)\) until any first
exit from this feature interval. Since \(3T_0<\bar S\), the
first exit cannot occur before \(T_0\). The local GD induction
gives the identical upper bound on its interpolated clock.
Thus all clocks under comparison stay strictly below \(\bar S\)
on this physical interval, without using predictor monotonicity
or a global optimization theorem.
The GD clock is linearly interpolated in physical time and has
slope \(2(1-f_{n,k})\) on its \(k\)-th physical step.

The output difference of two states is at most \(C\rho\). Comparing
the scalar clocks and using (C.14) or (C.19), scalar Gronwall gives
their uniform difference on \([0,T_0]\) bounded by a constant times
the corresponding feature-path error, plus the vanishing one-step
interpolation error for GD. Multiplying a clock discrepancy by
the uniform reference velocity bound controls its state effect.
Therefore the two exact finite-width algorithms satisfy
\[
\sup_{t\le T_0}
\rho_n\bigl(\Theta_n^{\rm GD}(t),\Theta_n^{\rm flow}(t)\bigr)
\longrightarrow0\quad\text{in probability}.            \tag{C.21}
\]
Both limits are compared to the same zero-readout clipped finite
reference before removing \(R\). Thus (C.21) does not require a
prior uncut Lipschitz bound.

Their finite joint measured laws converge uniformly on
\([0,T_0]\) to the unique local population solution reparametrized
by (C.20). Predictions and losses converge uniformly as well.
Since \(F^{-1}\) is 1-Lipschitz, these conclusions include the
original first-layer preactivation, not only its transform.
The limit operator statement is an action-law statement on the
generated population spaces, as explained after (C.3).

Uniqueness also applies to the raw physical equations. For a
competing raw integral solution with bounded primal norms, the
first-layer equation supplies absolutely continuous coordinate
paths with velocity \(2(1-f)\phi'(Z^{(1)})Q^{(1)}\).
The scalar chain rule on each such path gives
\[
 F(Z^{(1)}(t))
 =F(Z^{(1)}_0)+\int_0^t2(1-f(u))Q^{(1)}(u)\,du.
\]
The right side belongs to \(L^2\). Thus the transformed coordinate
belongs to the class in (C.3), even if not assumed at the outset.

Define its feature clock while \(1-f>0\). With zero initial
readout, \(|W^{(4)}|\le as\) and \(|f|\le a^2s\).
Before the clock reaches \(\bar S\), it obeys \(|f|\le1/4\)
and \(0<s'\le5/2\). It cannot reach \(\bar S\) by
\(T_0=\bar S/4\), nor can \(1-f\) vanish there. It therefore
defines a feature-time solution throughout its physical interval.
Feature-time uniqueness identifies it with the constructed
trajectory up to its clock endpoint, and scalar-clock uniqueness
in (C.20) identifies the physical trajectories. From a reached
state the same argument uses
\(|W^{(4)}(s_*)|\le as_*\), the restart comparison above, and
\(s(t)\le(5/2)t<\bar S\). This proves raw physical restart
uniqueness within the same local interval.

For the velocity conclusions below, at every GD mesh node use the
right-hand derivative of the raw linear interpolant and of its
recomputed preactivations. If \(T_0\) is itself a terminal mesh
node, use the left-hand derivative there. This convention does
not affect any integrated quantity.

The named uncut backward fields and kernel blocks follow by the
additional clipping/uniform-integrability argument after (C.14).
For hidden trajectory laws and integrated squared speeds, use
the exact feature-time preactivation velocities
\[
\frac{dZ^{(1)}}{ds}=\phi'(Z^{(1)})Q^{(1)},
\]
\[
\frac{dZ^{(2)}}{ds}
=\mathbb E_1[(H^{(1)})^2]\delta^{(2)}
 +W^{(2)}[\phi'(Z^{(1)})^2Q^{(1)}],
\]
\[
\frac{dZ^{(3)}}{ds}
=\mathbb E_2[(H^{(2)})^2]\delta^{(3)}
 +W^{(3)}\left[\phi'(Z^{(2)})\frac{dZ^{(2)}}{ds}\right].
                                                               \tag{C.22}
\]
All are continuous \(L^2\) paths by the same truncation argument.
To obtain physical velocities multiply (C.22) by \(-2r\).
Their finite laws and squared norms converge uniformly.

For completeness, on a GD interval let \(t_k=k\eta_n\) and let
\(\dot W_k^{(\ell)}\) be the constant raw matrix slope. Differentiating
the recomputed preactivations gives the exact product rule
\[
\partial_tz_n^{(\ell)}(t)
=\dot W_k^{(\ell)}h_n^{(\ell-1)}(t)
 +W_n^{(\ell)}(t)
   [\phi'(z_n^{(\ell-1)}(t))
      \odot\partial_tz_n^{(\ell-1)}(t)],
\qquad \ell=2,3.
\]
At \(t_k\), these are exactly the physical flow velocities evaluated
at the GD state. For layer 1 the raw interpolated slope is constant.
The matrix slopes, operator norms, and normalized vector slopes are
uniformly bounded by the primal estimates and the clock bound.
Consequently changes of a matrix or activation over one step have
size \(O(\eta_n)\) in their respective norms.

Proceeding from layer 1 to layer 3, the only term not covered directly
by these bounds is a changed gate multiplying a left-endpoint velocity
\(v_k\). Clip \(v_k\) coordinatewise at a fixed \(A\). The bounded
part has normalized error at most
\[
2A\,\frac{\|z_n^{(\ell-1)}(t)
                 -z_n^{(\ell-1)}(t_k)\|_2}{\sqrt n}
=O(A\eta_n).
\]
The remaining error is at most
\(2\|v_k\mathbf1_{\{|v_k|>A\}}\|_2/\sqrt n\).
The joint velocity laws already proved have uniformly integrable squared
tails, since their population \(L^2\) paths have compact time images.
Thus first \(n\to\infty\) at fixed \(A\), then \(A\to\infty\), shows
that the actual interpolated derivatives have the same joint laws and
squared norms as the endpoint velocities, uniformly in time.
The induction also accounts for the previous layer's derivative error.

It follows, for both GD and finite gradient flow, that
\[
\int_0^{T_0}\frac{\|\partial_tz_n^{(\ell)}(t)\|_2^2}{n}\,dt
\longrightarrow
\int_0^{T_0}\mathbb E_\ell[|\dot Z^{(\ell)}(t)|^2]\,dt,
\qquad \ell=1,2,3,
\]
in probability. Multiplication by the bounded gate
\(\phi'(z_n^{(\ell)})\), with the same truncation argument, proves
the corresponding statement for \(h_n^{(\ell)}\) and \(H^{(\ell)}\). Integrating a jointly measurable version of each
population velocity and applying Fubini supplies absolutely
continuous coordinate paths with the stated \(L^2\) values.
Finally, for an absolutely continuous scalar path,
\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^{T_0}|\dot z(t)|^2\,dt.
\]
Joint finite-grid laws and this estimate give each hidden-layer
trajectory law in \(\mathcal W_2(C([0,T_0]))\), with the supremum
path metric. Applying the 1-Lipschitz map
\(z(\cdot)\mapsto\phi(z(\cdot))\) also gives the hidden-feature path laws.

These conclusions establish the unconditional joint local limit.
The representation used throughout is proved in Lemma 6.1.
The tail estimate has been established only up to \(S_0\), so these
arguments assert no population continuation beyond the constructed interval
and no interchange with an infinite physical-time limit.


<a id="l3-gradient"></a>

## 7. Gradient structure of the local limit

The uncut local solution constructed in §6 is the gradient flow of
the original squared loss in the parameter geometry described below.

Use the three population spaces and matrix actions in
[§4](#l3-actions). Averages in a layer are denoted by
\(E_\ell\). Retain the forward equations
\[
 H^{(1)}=\phi(Z^{(1)}),\quad
 Z^{(2)}=W^{(2)}H^{(1)},\quad H^{(2)}=\phi(Z^{(2)}),\quad
 Z^{(3)}=W^{(3)}H^{(2)},\quad H^{(3)}=\phi(Z^{(3)}).
\]
Set
\[
 f=E_3[W^{(4)}H^{(3)}],\qquad r=f-1,\qquad \mathcal L=r^2,
\]
\[
 \delta^{(3)}=W^{(4)}\phi'(Z^{(3)}),\quad
 \delta^{(2)}=\phi'(Z^{(2)})(W^{(3)})^*\delta^{(3)},\quad
 \delta^{(1)}=\phi'(Z^{(1)})(W^{(2)})^*\delta^{(2)}.
 \tag{G.1}
\]
The derivatives exclude the residual. Each belongs to its layer's
mean-square space, since the gates are bounded and the matrix
actions are bounded.

The trained changes of \(W^{(2)},W^{(3)}\) are square-summable
operators, even though the initial Gaussian actions need not be.
Precisely, the size of a square-summable operator \(A\) is
\[
 \|A\|_{\rm HS}^2=\sum_j\|Ae_j\|_{L^2}^2,
\]
for any orthonormal basis of its input space; this sum does not
depend on the basis. This is the population counterpart of a
matrix's ordinary squared Frobenius norm. For the rank-one action
\((U\otimes V)B=U E[VB]\), the size is
\(\|U\otimes V\|_{\rm HS}=\|U\|_{L^2}\|V\|_{L^2}\).
An integral of the continuous rank-one velocities therefore has
finite HS size on a bounded time interval.

To justify this assertion for the cutoff limit as well, the
comparison estimate in [§6](#l3-bridge) proves uniform
mean-square convergence of \(\delta^{(2)}_R\) and
\(\delta^{(3)}_R\) to their uncut values, as well as convergence
of \(H^{(1)}_R,H^{(2)}_R\). The rank-one difference inequality
holds in HS norm just as in operator norm. Thus the integrals of
the matrix velocities converge in HS norm. Their limits are the
same matrix actions already obtained in operator norm.

Consider the raw parameter space with coordinates
\[
 (Z^{(1)},\,W^{(2)}-W^{(2)}_0,\,
 W^{(3)}-W^{(3)}_0,\,W^{(4)}).
\]
Its squared length for a variation is
\[
 E_1[(dZ^{(1)})^2]
 +\|dW^{(2)}\|_{\rm HS}^2
 +\|dW^{(3)}\|_{\rm HS}^2
 +E_3[(dW^{(4)})^2].                                   \tag{G.2}
\]
All affine states in this space have bounded matrix actions:
the HS size bounds the operator norm of each trained change.

The predictor is differentiable in the norm (G.2). Here is the
needed elementary remainder argument, avoiding an incorrect
claim that every pointwise nonlinearity is differentiable as a
map from all of \(L^2\) to \(L^2\). For any fixed \(B\in L^2\),
the bounded first and second derivatives of \(\phi\) give
\[
 \begin{aligned}
 &\left|E B[\phi(Z+e)-\phi(Z)-\phi'(Z)e]\right|\\
 &\quad\le C R\,E e^2
       +2\|B\,\mathbf1_{\{|B|>R\}}\|_{L^2}\|e\|_{L^2}.
 \end{aligned}                                         \tag{G.3}
\]
On \(|B|\le R\) use the quadratic Taylor remainder; on the
complement use its bound \(2|e|\). First fix \(R\) and send
\(\|e\|_{L^2}\) to zero, then send \(R\) to infinity. The
remainder in (G.3) is \(o(\|e\|_{L^2})\).

Successive forward differences are \(O(\|d\theta\|)\) in mean
square: use bounded activations, Lipschitz \(\phi\), bounded
matrix actions, and
\(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\).
Expand the scalar predictor from the top layer downward.
At each layer apply (G.3) with the fixed backward coefficient at
the original state. Terms containing both a matrix change and
an activation change are \(O(\|d\theta\|^2)\), by the operator
inequality and Cauchy--Schwarz. The same is true of the product
of a readout change and a top activation change. This proves
the norm derivative
\[
 \begin{aligned}
 df={}&E_1[\delta^{(1)}dZ^{(1)}]
 +E_2[\delta^{(2)}\,dW^{(2)}H^{(1)}]\\
 &+E_3[\delta^{(3)}\,dW^{(3)}H^{(2)}]
 +E_3[H^{(3)}dW^{(4)}].
 \end{aligned}                                         \tag{G.4}
\]
Equivalently its gradient in (G.2) is
\[
 \nabla f=
 \left(\delta^{(1)},\,
       \delta^{(2)}\otimes H^{(1)},\,
       \delta^{(3)}\otimes H^{(2)},\,
       H^{(3)}\right).                                 \tag{G.5}
\]
The rank-one entries follow from the identity
\(\langle U\otimes V,A\rangle_{\rm HS}=E[U\,AV]\).
The gradient is continuous. For example, bounded gates converging
in probability multiply a fixed \(L^2\) variable continuously
in \(L^2\), by truncating that fixed variable; combine this
observation with forward continuity and reverse operator bounds
in (G.1). Local Lipschitz continuity of the uncut gradient is
neither asserted nor needed for the differentiability claim.

The already constructed feature-time solution has
\(X^{(1)}=F(Z^{(1)})\) and
\(dX^{(1)}/ds=(W^{(2)})^*\delta^{(2)}\).
Since \((F^{-1})'(F(z))=\phi'(z)\), its raw first coordinate
satisfies \(dZ^{(1)}/ds=\delta^{(1)}\) in mean square.
One direct chain-rule justification uses coordinate absolute
continuity and the bound \(|(F^{-1})'|\le1\), then approximates
the mean-square velocity by bounded variables. This also gives
mean-square continuity of the resulting velocity.
Together with the other three integral equations, (G.5) yields
\[
 \frac{d\theta}{ds}=\nabla f(\theta).                    \tag{G.6}
\]

On the local interval chosen in [§6](#l3-bridge),
\(|f|<1\). Its physical clock solves
\(ds/dt=2(1-f)\). Hence the physical evolution is exactly
\[
 \frac{d\theta}{dt}=-2r\,\nabla f=-\nabla\mathcal L.             \tag{G.7}
\]
In particular, the derivative of its predictor is
\[
 \frac{df}{dt}=-2r\,K,\qquad
 \frac{d\mathcal L}{dt}=-4r^2K,
\]
where the four nonnegative kernel contributions are
\[
 \begin{aligned}
 K^{(1)}&=E_1[(\delta^{(1)})^2],\\
 K^{(2)}&=E_2[(\delta^{(2)})^2]\,E_1[(H^{(1)})^2],\\
 K^{(3)}&=E_3[(\delta^{(3)})^2]\,E_2[(H^{(2)})^2],\\
 K^{(4)}&=E_3[(H^{(3)})^2],\qquad
 K=K^{(1)}+K^{(2)}+K^{(3)}+K^{(4)}.
 \end{aligned}                                         \tag{G.8}
\]

This state is autonomous: the present four objects determine
every quantity in (G.1), then determine the four velocities.
The Gaussian response coefficients used to prove the limit are
not external inputs to (G.7). Both initial matrix actions and all
their trained changes are contained in the current matrix
operators. Local uniqueness and restartability on the constructed
interval are supplied by the cutoff comparison, not by a claim
that the uncut gradient is locally Lipschitz.

This gradient identity does not supply the tail and stability estimates
needed to continue the L3 population solution beyond the local interval.


<a id="l3-features"></a>

## 8. Feature learning in all three hidden layers

This section applies to the population flow established in §§3–7.
It proves nonzero feature motion in all three hidden layers using its
integral equations, strong mean-square continuity, and the initial
Gaussian action laws.

### Setup and the local statement

For layer \(\ell\), let \(\mathcal H_\ell=L^2(\Omega_\ell)\), with
inner product \(\langle u,v\rangle_{\mathcal H_\ell}=\mathbb E_\ell[uv]\)
and norm \(\|u\|_{L^2(\Omega_\ell)}\). Let
\(W^{(2)}(s):\mathcal H_1\to\mathcal H_2\) and
\(W^{(3)}(s):\mathcal H_2\to\mathcal H_3\) be the bounded operator
actions supplied by the local construction, and let a star denote their
Hilbert-space adjoints. For \(u\in\mathcal H_\ell\) and
\(v\in\mathcal H_{\ell-1}\), define the rank-one operator
\[
 (u\otimes v)x=u\,\mathbb E_{\ell-1}[vx].
\]
Its Hilbert--Schmidt norm is \(\|u\|_{L^2(\Omega_{\ell})}\|v\|_{L^2(\Omega_{\ell-1})}\).
This is the population version of \(uv^{T}/n\), whose finite contractions are written explicitly as \(u^{T}v/n\).

Set \(\phi(x)=\arctan x\), \(\phi'(x)=(1+x^2)^{-1}\),
and \(a=\pi/2\). The variable \(s\) is feature time. The local
canonical equations are
\[
 H^{(\ell)}=\phi(Z^{(\ell)}),\qquad
 Z^{(2)}=W^{(2)}H^{(1)},\qquad Z^{(3)}=W^{(3)}H^{(2)},
\]
\[
 \delta^{(3)}=\phi'(Z^{(3)})W^{(4)},\qquad
 Q^{(2)}=(W^{(3)})^*\delta^{(3)},\qquad
 \delta^{(2)}=\phi'(Z^{(2)})Q^{(2)},\qquad
 Q^{(1)}=(W^{(2)})^*\delta^{(2)},
\]
\[
 \frac{dZ^{(1)}}{ds}=\phi'(Z^{(1)})Q^{(1)},\quad
 \frac{dW^{(2)}}{ds}=\delta^{(2)}\otimes H^{(1)},\quad
 \frac{dW^{(3)}}{ds}=\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{ds}=H^{(3)}.                              \tag{F.1}
\]
These equations hold in integral form by §6. The
states are continuous in their \(L^2\) spaces; the weights are continuous
in operator norm, as also follows from their rank-one integral updates.
All limits below are in these \(L^2\) spaces unless otherwise stated.

Initially \(W^{(4)}_0=0\). The Gaussian initialization supplies
\(Z^{(1)}_0\sim N(0,1)\), the independent Gaussian initial actions
\(W^{(2)}_0,W^{(3)}_0\), and the forward laws
\[
 Z^{(2)}_0\sim N(0,\mu_1),\qquad Z^{(3)}_0\sim N(0,\mu_2),\qquad
 \mu_\ell=\|H^{(\ell)}_0\|_{L^2(\Omega_{\ell})}^2>0.                       \tag{F.2}
\]
Thus, for a standard Gaussian \(G\),
\[
 \mu_1=\mathbb E\phi(G)^2,\quad
 \mu_2=\mathbb E\phi(\sqrt{\mu_1}G)^2,\quad
 \mu_3=\mathbb E\phi(\sqrt{\mu_2}G)^2.
\]
Every displayed \(\phi'(Z^{(\ell)})\) acts by pointwise
multiplication on its own layer.

Define the initial backward fields, each on its indicated population,
\[
 \beta_3=H^{(3)}_0\phi'(Z^{(3)}_0)\in\mathcal H_3,\quad
 P_2=(W^{(3)}_0)^*\beta_3\in\mathcal H_2,\quad
 B_2=\phi'(Z^{(2)}_0)P_2\in\mathcal H_2,\quad
 P_1=(W^{(2)}_0)^*B_2\in\mathcal H_1.                    \tag{F.3}
\]
Define the bounded self-adjoint operators
\[
 \mathcal A^{(2)}_0 U
 =\mu_1 U+W^{(2)}_0\!\left[
 \phi'(Z^{(1)}_0)^2 (W^{(2)}_0)^*U\right],
 \qquad U\in\mathcal H_2,
\]
\[
 \mathcal A^{(3)}_0 U
 =\mu_2 U+W^{(3)}_0\!\left[
 \phi'(Z^{(2)}_0)\mathcal A^{(2)}_0
 \left(\phi'(Z^{(2)}_0)(W^{(3)}_0)^*U\right)\right],
 \qquad U\in\mathcal H_3.           \tag{F.4}
\]
Finally put
\[
 V^{(1)}=\phi'(Z^{(1)}_0)P_1,\qquad
 V^{(2)}=\mathcal A^{(2)}_0B_2,\qquad
 V^{(3)}=\mathcal A^{(3)}_0\beta_3.                           \tag{F.5}
\]

As \(s\downarrow0\), the local flow satisfies
\[
 W^{(4)}(s)=sH^{(3)}_0+o(s),\quad
 \delta^{(3)}(s)=s\beta_3+o(s),\quad
 Q^{(2)}(s)=sP_2+o(s),
\]
\[
 \delta^{(2)}(s)=sB_2+o(s),\qquad Q^{(1)}(s)=sP_1+o(s),  \tag{F.6}
\]
and, for all three hidden layers,
\[
 \frac{dZ^{(\ell)}}{ds}=sV^{(\ell)}+o(s),\qquad
 Z^{(\ell)}(s)-Z^{(\ell)}_0
       =\frac{s^2}{2}V^{(\ell)}+o(s^2),
\]
\[
 \frac{dH^{(\ell)}}{ds}=s\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s),\qquad
 H^{(\ell)}(s)-H^{(\ell)}_0
       =\frac{s^2}{2}\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s^2).            \tag{F.7}
\]
Every \(V^{(\ell)}\) and every \(\phi'(Z^{(\ell)}_0)V^{(\ell)}\) has strictly
positive \(L^2\) norm. Thus the second-order changes are genuine in
each preactivation and each hidden feature.

### Strong limits without differentiability assumptions on an \(L^2\) map

The following elementary multiplier fact is sufficient. If
\(x_s\to x_0\) in probability, \(v_s\to v_0\) in \(L^2\), and
\(g\) is bounded and continuous, then
\[
 g(x_s)v_s\longrightarrow g(x_0)v_0\quad\text{in }L^2.   \tag{F.8}
\]
Indeed, the part containing \(v_s-v_0\) is bounded by
\(\|g\|_\infty\|v_s-v_0\|_{L^2(\Omega_\ell)}\). For the other part, first restrict
to \(|v_0|\le K\), where bounded convergence in probability gives
convergence of its squared expectation, and then let \(K\to\infty\).
The remaining bound is
\(4\|g\|_\infty^2\mathbb E[|v_0|^2\mathbf1_{\{|v_0|>K\}}]\).
Only the fixed reference \(v_0\in L^2\) is used.

The same argument justifies the chain rule along a differentiable
\(L^2\) curve. If \(x(s+h)-x(s)=hv_h\) and \(v_h\to v\) in
\(L^2\), then
\[
 \frac{\phi(x(s+h))-\phi(x(s))}{h}
 =v_h\int_0^1 \phi'\bigl(x(s)+rh v_h\bigr)\,dr
 \longrightarrow \phi'(x(s))v\quad\text{in }L^2.
\]
The integral multiplier is bounded by one and converges in probability
to \(\phi'(x(s))\). This is a chain rule along the given curve, not an
assertion of Frechet differentiability of a Nemytskii map on \(L^2\).

The integral equation for \(W^{(4)}\) and continuity of \(H^{(3)}\)
give \(W^{(4)}(s)/s\to H^{(3)}_0\). Apply (F.8), then operator-norm
continuity of \(W^{(3)}\), then (F.8) again, and finally operator-norm
continuity of \(W^{(2)}\). This proves every limit in (F.6).

All right-hand sides of (F.1) are continuous by (F.8), so the integral
equations give strong derivatives. The chain rule above yields the
exact identities
\[
 \frac{dZ^{(2)}}{ds}=\mathcal A^{(2)}(s)\delta^{(2)},\qquad
 \mathcal A^{(2)}(s)U
 =\mathbb E_1[H^{(1)}(s)^2]U
 +W^{(2)}(s)\!\left[
 \phi'(Z^{(1)}(s))^2(W^{(2)}(s))^*U\right],
\]
\[
 \frac{dZ^{(3)}}{ds}=\mathcal A^{(3)}(s)\delta^{(3)},\qquad
 \mathcal A^{(3)}(s)U
 =\mathbb E_2[H^{(2)}(s)^2]U
 +W^{(3)}(s)\!\left[
 \phi'(Z^{(2)}(s))\mathcal A^{(2)}(s)
 \left(\phi'(Z^{(2)}(s))(W^{(3)}(s))^*U\right)\right].           \tag{F.9}
\]
For example, the first identity uses
\((\delta^{(2)}\otimes H^{(1)})H^{(1)}
=\|H^{(1)}\|_{L^2(\Omega_1)}^2\delta^{(2)}\) and
\(dH^{(1)}/ds=\phi'(Z^{(1)})^2(W^{(2)})^*\delta^{(2)}\).
The second follows from
\(dZ^{(3)}/ds=\|H^{(2)}\|_{L^2(\Omega_2)}^2\delta^{(3)}
 +W^{(3)}[\phi'(Z^{(2)})\,dZ^{(2)}/ds]\).

The operators in (F.9) are uniformly bounded near zero and converge
strongly on every fixed \(L^2\) vector to the operators in (F.4).
To verify this, apply (F.8) successively to the bounded gates and use
operator-norm continuity of the weights. No operator-norm convergence
of the gate multiplication operators is needed. Combining this strong
convergence with (F.6) proves the derivative expansions in (F.7).
Integration proves the state expansions; a further use of (F.8) and the
curve chain rule proves the feature expansions.

### Initial transpose conditioning and strict positivity

Here is the initial Gaussian conditioning calculation needed for (F.3).
For a finite Gaussian matrix \(W\) with entry variance \(1/n\), an
independent nonzero input \(h\), and \(y=Wh\), conditioning on \(h,y\)
gives
\[
 W=\frac{yh^{T}}{\|h\|_2^2}
        +\widetilde W P_{h^\perp}
 \quad\text{in conditional law},
\]
where \(\widetilde W\) is an independent matrix with the same entry
variance. If \(u\) is measurable from \(h,y\) and auxiliary randomness
independent of this conditional residual, then
\[
 W^{T}u
 =h\,\frac{y^{T}u/n}{\|h\|_2^2/n}
  +\sqrt{\|u\|_2^2/n}\,P_{h^\perp}g
 \quad\text{in conditional law},                       \tag{F.10}
\]
with a fresh standard Gaussian vector \(g\). The removed projection
has conditional normalized mean square \(1/n\). Thus, when the input
contractions have their canonical limits, its scalar transpose law is
\(c h+\sigma G\), with
\(c=\mathbb E[yu]/\mathbb E[h^2]\) and
\(\sigma^2=\mathbb E[u^2]\). The innovation \(G\) is independent
of the existing same-population initial data. Importantly, the
innovation variance is \(\mathbb E[u^2]\), without subtraction of
the response component.

First apply (F.10) to \(W^{(3)}_0\), input \(H^{(2)}_0\), output
\(Z^{(3)}_0\), and transpose input \(\beta_3\). It gives the joint
same-population law
\[
 P_2=c_3H^{(2)}_0+\sigma_3G^{\mathrm b}_2,\qquad
 c_3=\frac{\mathbb E_3[Z^{(3)}_0\beta_3]}{\mu_2}>0,\qquad
 \sigma_3^2=\mathbb E_3[\beta_3^2]>0,                      \tag{F.11}
\]
where \(G^{\mathrm b}_2\sim N(0,1)\) is independent of
\(Z^{(2)}_0\). Both inequalities follow because
\(z\phi(z)\phi'(z)>0\) for \(z\ne0\), and the Gaussian variance
\(\mu_2\) is positive. Consequently
\[
 B_2=\phi'(Z^{(2)}_0)
       \bigl(c_3\phi(Z^{(2)}_0)+\sigma_3G^{\mathrm b}_2\bigr),
\]
\[
 \sigma_2^2:=\mathbb E_2[B_2^2]
 =\mathbb E_2\left[\phi'(Z^{(2)}_0)^2
          \bigl(c_3^2\phi(Z^{(2)}_0)^2+\sigma_3^2\bigr)\right]>0.
                                                                    \tag{F.12}
\]

For the second application, condition on the bottom initialization,
\(Z^{(2)}_0=W^{(2)}_0H^{(1)}_0\), and the entire independent initial
matrix \(W^{(3)}_0\). The field \(B_2\) is then fixed and introduces
no further information about the conditional residual of
\(W^{(2)}_0\). Formula (F.10) therefore gives
\[
 P_1=c_2H^{(1)}_0+\sigma_2G^{\mathrm b}_1,\qquad
 c_2=\frac{\mathbb E_2[Z^{(2)}_0B_2]}{\mu_1}
 =\frac{c_3}{\mu_1}
       \mathbb E_2[Z^{(2)}_0\phi'(Z^{(2)}_0)\phi(Z^{(2)}_0)]>0. \tag{F.13}
\]
Here \(G^{\mathrm b}_1\) is standard Gaussian, independent of
\(Z^{(1)}_0\); the successive fresh innovations can be chosen as
independent groups in the canonical initial source construction.
The factor \(c_3\) in (F.13) retains the return through the third-layer
matrix. Treating \(B_2\) as an independent centered multiplier would
lose this term.

Only initial finite Gaussian queries are involved in (F.10)--(F.13).
Their contractions converge by conditional Gaussian averaging: the
forward activation averages are bounded; in the transpose step the
rank-one projection error vanishes in normalized \(L^2\); bounded
gates preserve that convergence. Pairwise contractions then converge
by Cauchy--Schwarz. This calculation uses no trained-state limit.

By (F.12)--(F.13), \(P_1\ne0\), \(B_2\ne0\), and \(\beta_3\ne0\)
in their \(L^2\) spaces. Moreover,
\[
 \mathcal A^{(2)}_0\succeq \mu_1I,\qquad
 \mathcal A^{(3)}_0\succeq \mu_2I.                         \tag{F.14}
\]
For any nonzero \(v\), the first inequality implies
\(\|\mathcal A^{(2)}_0v\|\ge \mu_1\|v\|\), by taking its inner
product with \(v\); the second gives the corresponding bound with
\(\mu_2\). Finally, multiplication by \(\phi'(Z^{(\ell)}_0)\) has zero
kernel because \(\phi'(z)>0\) for every finite \(z\). These observations
prove the strict positivity asserted after (F.7).

### Physical time, kernel blocks, and squared speeds

Let \(f(s)=\langle W^{(4)}(s),H^{(3)}(s)\rangle_{\mathcal H_3}\).
Equation (F.6) gives \(f(s)=\mu_3s+o(s)\). In a sufficiently small
neighborhood of zero, \(f(s)<1\), so define physical time by
\[
 \frac{ds}{dt}=2(1-f(s)),\qquad s(0)=0.
\]
Equivalently,
\(t(s)=\int_0^s[2(1-f(u))]^{-1}\,du\). It follows that
\[
 s(t)=2t+o(t),\qquad 1-f(s(t))=1+o(1).                  \tag{F.15}
\]
This is precisely the residual factor for squared loss \((f-1)^2\).
In particular, with the left-hand sides evaluated at feature time
\(s(t)\),
\[
 Z^{(\ell)}-Z^{(\ell)}_0=2t^2V^{(\ell)}+o(t^2),\qquad
 H^{(\ell)}-H^{(\ell)}_0=2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2).
\]

Define the four population kernel blocks at physical time \(t\) by
\[
 K^{(1)}(t)=\|\phi'(Z^{(1)})Q^{(1)}\|_{L^2(\Omega_1)}^2,\quad
 K^{(2)}(t)=\|H^{(1)}\|_{L^2(\Omega_1)}^2\|\delta^{(2)}\|_{L^2(\Omega_2)}^2,\quad
 K^{(3)}(t)=\|H^{(2)}\|_{L^2(\Omega_2)}^2\|\delta^{(3)}\|_{L^2(\Omega_3)}^2,\quad
 K^{(4)}(t)=\|H^{(3)}\|_{L^2(\Omega_3)}^2,
\]
where every right-hand side is evaluated at \(s=s(t)\). Put
\[
 \gamma_1=\|\phi'(Z^{(1)}_0)P_1\|_{L^2(\Omega_1)}^2>0,\qquad
 \gamma_2=\mu_1\|B_2\|_{L^2(\Omega_2)}^2>0,\qquad
 \gamma_3=\mu_2\|\beta_3\|_{L^2(\Omega_3)}^2>0.
\]
Then
\[
 K^{(\ell)}(t)=4\gamma_\ell t^2+o(t^2)\quad(\ell=1,2,3),
 \qquad K^{(4)}(t)=\mu_3+o(1).                           \tag{F.16}
\]
In particular all three hidden kernel blocks are strictly positive
at every sufficiently small positive time. These coefficients are
finite using only the second moments established above. For example,
\[
 \gamma_1=\mathbb E_1\left[\phi'(Z^{(1)}_0)^2
           \bigl(c_2^2\phi(Z^{(1)}_0)^2+\sigma_2^2\bigr)\right]>0.
\]

To state the squared-speed consequence precisely, use the \(L^2\)
norm for the vector blocks \(Z^{(1)},W^{(4)}\) and the
Hilbert--Schmidt norm for the two matrix velocities. Let
\(\mathcal J_\ell(T)\) be the integral from \(0\) to \(T\) of the
squared velocity of block \(\ell\). Equation (F.1) and the time change
give the exact identity
\[
 \mathcal J_\ell(T)
 =\int_0^T4(1-f(s(t)))^2K^{(\ell)}(t)\,dt.
\]
Therefore
\[
 \mathcal J_\ell(T)=\frac{16}{3}\gamma_\ell T^3+o(T^3)
       \quad(\ell=1,2,3),\qquad
 \mathcal J_4(T)=4\mu_3T+o(T).                            \tag{F.17}
\]
The initial matrix actions need not be Hilbert--Schmidt; only their
rank-one velocities and subsequent increments use that norm.

The hidden features themselves have positive squared-speed integrals
as well. Equations (F.7) and (F.15) give
\[
 \frac{dZ^{(\ell)}}{dt}=4tV^{(\ell)}+o(t),\qquad
 \frac{dH^{(\ell)}}{dt}=4t\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t),
\]
and hence
\[
 \int_0^T\left\|\frac{dZ^{(\ell)}}{dt}\right\|_{L^2(\Omega_{\ell})}^2dt
       =\frac{16}{3}\|V^{(\ell)}\|_{L^2(\Omega_{\ell})}^2T^3+o(T^3),
\]
\[
 \int_0^T\left\|\frac{dH^{(\ell)}}{dt}\right\|_{L^2(\Omega_{\ell})}^2dt
       =\frac{16}{3}\|\phi'(Z^{(\ell)}_0)V^{(\ell)}\|_{L^2(\Omega_{\ell})}^2T^3+o(T^3).
                                                                    \tag{F.18}
\]
All six leading coefficients in (F.18) are strictly positive. These are local consequences of the established flow and action
construction and hold within its interval.

### The kernel changes and the activation remains genuinely nonlinear

The expansions also prove nonconstancy of the total kernel.
Equations (F.4)--(F.5) and adjunction give
\[
 \langle\beta_3,\mathcal A^{(3)}_0\beta_3\rangle_{\mathcal H_3}
 =\mu_2\|\beta_3\|_{L^2(\Omega_3)}^2+\mu_1\|B_2\|_{L^2(\Omega_2)}^2+\|\phi'(Z^{(1)}_0)P_1\|_{L^2(\Omega_1)}^2
 =\gamma_1+\gamma_2+\gamma_3>0.
\]
Since \(H^{(3)}(s)=H^{(3)}_0+
(s^2/2)\phi'(Z^{(3)}_0)V^{(3)}+o(s^2)\), expanding its squared norm gives
\[
 K^{(4)}(s)=\mu_3+s^2(\gamma_1+\gamma_2+\gamma_3)+o(s^2).
\]
In feature time the sum of the three hidden kernel contributions
has the same positive \(s^2\) coefficient. In physical time,
\[
 K(t)
 =\mu_3+8(\gamma_1+\gamma_2+\gamma_3)t^2+o(t^2).           \tag{F.19}
\]
Hence \(K\) is not constant on any sufficiently small initial
interval. The gradient identity also gives
\(\mathcal L(t)=1-4\mu_3t+o(t)\), and \(\mathcal L(t)<1\) for small positive \(t\).

For each layer the initial preactivation is a nondegenerate
Gaussian. Its variance is positive. The mean-square error of the
best affine approximation to the activation is
\[
 \inf_{\alpha,\beta\in\mathbb R}
 E_\ell[(\phi(Z^{(\ell)})-\alpha Z^{(\ell)}-\beta)^2]
 =
 \operatorname{Var}(\phi(Z^{(\ell)}))
 -\frac{\operatorname{Cov}(Z^{(\ell)},\phi(Z^{(\ell)}))^2}
        {\operatorname{Var}(Z^{(\ell)})}.               \tag{F.20}
\]
Initially (F.20) is strictly positive. Otherwise \(\arctan z\)
would agree with an affine function with probability one under a
full-support Gaussian law; continuity would make them agree for
every real \(z\), which is false. The first and second moments
in (F.20) are continuous along the constructed mean-square paths,
because \(\phi\) is bounded and Lipschitz. Thus the variance and
(F.20) remain strictly positive on a common positive initial
interval for all three hidden layers.
