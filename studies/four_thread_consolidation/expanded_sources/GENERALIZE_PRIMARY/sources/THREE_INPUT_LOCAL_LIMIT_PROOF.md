# Three inputs: a rigorous local-time joint width and gradient-flow limit

## Result and scope

Fix three inputs \(x_1,x_2,x_3\in\mathbb R^d\), with
\[
\frac{\|x_a\|_2^2}{d}=1,\qquad
x_a\ne x_b,\quad x_a\ne -x_b\quad(a\ne b),\qquad
G_{ab}=\frac{x_a^\top x_b}{d}.
\]
Because the norms agree, the conditions on \(x_a,x_b\) are exactly pairwise nonparallelity. The \(3\times3\) matrix \(G\) is positive semidefinite with diagonal one. It may be singular. All input indices and input sums below range over \(1,2,3\).
Let \(y_1,y_2,y_3\in\{-1,1\}\). There is \(T_0>0\) such that the ordinary, layer-scaled full-batch GD specified below has a unique autonomous population limit on \([0,T_0]\), for every sequence of positive steps \(\eta_n\to0\). In particular this includes the earlier regime \(\eta_n\sqrt n\to0\) and the original choice \(n^{-2}\). The proof works for all such triples and all eight label sign patterns. Moreover, the existence time \(T_0\) can be chosen uniformly over these triples and labels: its construction uses only three inputs, \(|G_{ab}|\le1\), and the fixed activation and initialization scales. It does not depend on width, step size, input dimension, or a lower bound on a Gram eigenvalue.

Predictions, residuals, loss, and all entries of all three kernel blocks converge in probability uniformly on this interval. The joint three-input hidden path laws converge with their second moments in the uniform path norm. Integrated squared hidden velocities converge. The joint empirical averages of any fixed finite collection of continuous, globally Lipschitz forward/adjoint probes, with bounded products when a product instruction is used, converge to their corresponding population expectations, uniformly in time. Unbounded first-layer backward fields and their quadratic contractions are included by the tail argument below.

Here a fixed action probe is a finite calculation from the current fields and constants using fixed globally Lipschitz coordinate functions, linear combinations, and appropriately typed calls to \(W^{(2)}\) and its adjoint. A product instruction is allowed when both varying factors are uniformly bounded, for example after clipping. Final same-layer joint measurements can be continuous with at most quadratic growth. Probe length and functions do not grow with width or depend on the learning rate.

On a possibly smaller interval \((0,T_*]\), each input's preactivations move in both hidden layers, all three \(3\times3\) kernel blocks are positive definite, the total kernel is nonconstant, loss strictly decreases, and \(\arctan\) has positive best-affine-fit error on each hidden preactivation distribution.

**Scope:** this is a local-time theorem. A convergence theorem on every finite horizon is not claimed for arbitrary input geometry. \(T_0>0\) is chosen before taking width and learning-rate limits and does not shrink in those limits. The strictly positive feature-learning coefficients and the possibly smaller activity interval \(T_*\) may depend on the fixed input geometry and labels.

The inputs are fixed while taking the width and learning-rate limits. A common existence interval across configurations is not a claim of a convergence rate uniform over configurations that themselves change with width.

## The finite network and its exact updates

The dimensions are \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(2)}\in\mathbb R^{n\times n}\), and \(W^{(3)}\in\mathbb R^n\). For input \(a=1,2,3\), use
\[
z_a^{(1)}=\frac{W^{(1)}x_a}{\sqrt d},\quad
h_a^{(1)}=\phi(z_a^{(1)}),\quad
z_a^{(2)}=W^{(2)}h_a^{(1)},\quad
h_a^{(2)}=\phi(z_a^{(2)}),\qquad \phi=\arctan,
\]
\[
f_{n,a}=\frac{(W^{(3)})^\top h_a^{(2)}}n,\qquad
r_{n,a}=f_{n,a}-y_a,\qquad L_n=\sum_{a=1}^3r_{n,a}^2.
\]
The summed loss retains the earlier factors of two; using the average of the three losses divides the speed by three.

All initialization entries are independent:
\[
W_{0,ij}^{(1)}\sim N(0,1),\quad
W_{0,ji}^{(2)}\sim N(0,1/n),\quad
W_{0,j}^{(3)}\sim N(0,1/n^2).
\]
Consequently each first-layer root triple is \(N(0,G)\), independently over neuron index \(i\). The three preactivations for one neuron may be correlated and may satisfy an exact linear relation. This is permitted.

Set
\[
\delta_a^{(2)}=W^{(3)}\odot\phi'(z_a^{(2)}),\qquad
\delta_a^{(1)}=\phi'(z_a^{(1)})\odot(W^{(2)})^\top\delta_a^{(2)}.
\]
Thus \(\delta_a^{(\ell)}=n\,\partial f_{n,a}/\partial z_a^{(\ell)}\).
In the displayed rescaled parameterization the layer learning-rate multipliers are \(n,1,n\). The exact first-weight update is
\[
W_{k+1}^{(1)}
=W_k^{(1)}-\frac{2\eta_n}{\sqrt d}
\sum_{b=1}^3r_{n,b,k}\delta_{b,k}^{(1)}x_b^\top.
\]
Multiplication by \(x_a/\sqrt d\) gives
\[
\begin{aligned}
z_{a,k+1}^{(1)}
&=z_{a,k}^{(1)}
-2\eta_n\sum_bG_{ab}r_{n,b,k}\delta_{b,k}^{(1)},\\
W_{k+1}^{(2)}
&=W_k^{(2)}-\frac{2\eta_n}{n}
\sum_b r_{n,b,k}\delta_{b,k}^{(2)}(h_{b,k}^{(1)})^\top,\\
W_{k+1}^{(3)}
&=W_k^{(3)}-2\eta_n\sum_b r_{n,b,k}h_{b,k}^{(2)} .
\end{aligned}\tag{M1}
\]
Use physical time \(t=k\eta_n\), linearly interpolate these parameters, and recompute the forward pass at intermediate times.

The whole effect of input geometry on first-layer training is \(G\): training on input \(b\) moves input \(a\)'s preactivation with coefficient \(G_{ab}\). If \(Gc=0\), then \(\sum_a c_a z_a^{(1)}=0\) initially and every update preserves this relation. No inverse of \(G\) is used.

The finite continuous flow has the kernel blocks
\[
K^{(1)}_{n,ab}
=G_{ab}\frac{(\delta_a^{(1)})^\top\delta_b^{(1)}}n,\quad
K^{(2)}_{n,ab}
=\frac{(h_a^{(1)})^\top h_b^{(1)}}n
 \frac{(\delta_a^{(2)})^\top\delta_b^{(2)}}n,\quad
K^{(3)}_{n,ab}
=\frac{(h_a^{(2)})^\top h_b^{(2)}}n .
\tag{M2}
\]
Differentiation gives \(\dot f_n=-2K_n r_n\) and \(\dot L_n=-4r_n^\top K_n r_n\), where \(K_n\) is the sum of the blocks. Each block is positive semidefinite: it is the Gram matrix of the corresponding scaled parameter gradients. Individual residual magnitudes need not decrease; their squared sum does.

## Why a new stability estimate is needed

With \(F(s)=s+s^3/3\), the componentwise transformation \(X_a^{(1)}=F(Z_a^{(1)})\) gives
\[
\dot X_a^{(1)}
=-2\sum_bG_{ab}r_b
\frac{1+(Z_a^{(1)})^2}{1+(Z_b^{(1)})^2}
(W^{(2)})^*\delta_b^{(2)}.
\tag{M3}
\]
If the inputs are mutually orthogonal, only diagonal terms occur and the ratios cancel. Otherwise nonzero cross-input terms remain and their ratios are unbounded. We therefore work with the original preactivations and prove a uniform tail estimate for the backward fields.

The exact limiting equations will be
\[
H_a^{(1)}=\phi(Z_a^{(1)}),\quad
Z_a^{(2)}=W^{(2)}H_a^{(1)},\quad
H_a^{(2)}=\phi(Z_a^{(2)}),\quad
f_a=\mathbb E[W^{(3)}H_a^{(2)}],\quad r_a=f_a-y_a,
\]
\[
\delta_a^{(2)}=W^{(3)}\phi'(Z_a^{(2)}),\qquad
\delta_a^{(1)}=\phi'(Z_a^{(1)})(W^{(2)})^*\delta_a^{(2)},
\]
\[
\begin{aligned}
\dot Z_a^{(1)}&=-2\sum_bG_{ab}r_b\delta_b^{(1)},\\
\dot W^{(2)}&=-2\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},\\
\dot W^{(3)}&=-2\sum_b r_bH_b^{(2)}.
\end{aligned}\tag{M4}
\]
Here \((u\otimes v)V=u\,\mathbb E[vV]\). This definition displays the normalization that replaces the finite factor \(1/n\). First-layer and second-layer coordinates belong to separate populations. \(W^{(2)}\) acts from the former to the latter, and its adjoint acts in reverse. Every expectation pairs coordinates of the same population.

The initial root triple is \(N(0,G)\), the population readout is zero, and the initial action \(W_0^{(2)}\) is the joint forward-and-transpose limit of the initial Gaussian matrix, constructed next. The state consists of three first-layer fields and the shared matrix action and readout field. It has finitely many kinds of state objects, not finitely many scalar degrees of freedom.

## The fixed-mesh construction and the new tail lemma

We use the following finite Gaussian fact. For a fixed finite calculation from iid jointly Gaussian coordinate tuples, independent of a Gaussian matrix of entry variance \(1/n\), with polynomially bounded coordinate functions and finitely many calls to that matrix and its transpose, every same-layer joint empirical average of a continuous polynomially bounded measurement has a deterministic limit. The limiting action is Gaussian randomness plus the responses forced by earlier opposite-direction calls. The precise response coefficients and their derivative convention are given and used in the appendix below. This is the specialization of Theorem 2.10 and Box 1 of [Tensor Programs III](https://arxiv.org/pdf/2009.10685). Its hypotheses hold here: after fixing population scalar coefficients, each instruction is polynomially bounded, and the training instructions whose derivatives are used below are smooth with polynomially bounded derivatives, as functions of finitely many Gaussian variables. The initial tuple covariance may be singular; represent it as a fixed linear image of independent Gaussian roots. No claim of iid finite coordinates after matrix reuse is used.

For completeness, the underlying conditioning mechanism is as follows. If previous calls have revealed \(W_0^{(2)}V=Y\) and \((W_0^{(2)})^\top U=R\), then the remaining Gaussian matrix is an independent Gaussian projected onto the directions orthogonal to the columns of \(U\) and \(V\). Its conditional mean obeys both recorded equations. A new product is the response fixed by these equations plus that projected Gaussian applied to the unexplored part of the new input. Gaussian integration by parts identifies the response coefficients. The finite Gaussian theorem makes this induction valid also with dependent query directions. We explicitly rely on this stated finite-program result, not on a claim that the infinite-time or growing-program-length theorem already follows from it.

These finite limits can be realized on two common population coordinate spaces. Here are the details relevant to the subsequent continuous-time argument. Take all the programs needed for rational meshes, their finite unions, and a countable closure under rational linear combinations, the coordinate operations in the proof, and bounded Lipschitz approximations. Their finite joint laws are consistent, so they can be realized jointly. Take the mean-square closure of their linear spans on each layer. Exact finite linear identities pass to these laws.

A fixed sufficiently large \(M\) satisfies
\[
\mathbb P(\|W_0^{(2)}\|_{\rm op}>M)
\le2\,9^{2n}e^{-nM^2/8}\longrightarrow0.
\tag{M5}
\]
Indeed two \(1/4\)-nets of the unit sphere each have at most \(9^n\) points, and every fixed bilinear form of the matrix is \(N(0,1/n)\). This finite operator inequality and joint second-moment convergence imply
\[
\mathbb E[(W_0^{(2)}V)^2]\le M^2\mathbb E[V^2]
\]
for every generated \(V\). Thus the action is well-defined on equal-in-mean-square variables and extends to the closure. The same reasoning applies to the transpose. The exact finite identity
\[
\frac{u^\top W_0^{(2)}v}{n}
=\frac{((W_0^{(2)})^\top u)^\top v}{n}
\]
passes to the limit and identifies the two actions as adjoints. Bounded coordinate multipliers and their required products belong to these spaces by clipping and mean-square approximation. This constructs the common bounded-operator realization used below; it is not an additional assumption.

Define population Euler for (M4) in this common realization, starting from the stated initialization. Its rank expansion is
\[
W_k^{(2)}=W_0^{(2)}
-2\Delta\sum_{s<k}\sum_b
r_{b,s}\delta_{b,s}^{(2)}\otimes H_{b,s}^{(1)}.
\tag{M6}
\]
Thus each fixed mesh is a finite Gaussian calculation with deterministic population residuals and contractions. Iterative construction is causal: the current fields determine their expectations and then the next fields. Its realization agrees with the finite Gaussian law, because applying the same rank expansion reduces each action to an initial-matrix call and those deterministic contractions.

The appendix proves the essential new estimate:
\[
\sup_{\Delta:\,\Delta\le T_0}\ 
\max_{a,k:\,k\Delta\le T_0}
\mathbb E\exp\!\left(
c\left|(W_k^{(2)})^*\delta_{a,k}^{(2)}\right|^2
\right)\le C .
\tag{M7}
\]
Here \(T_0,c,C>0\) do not depend on the mesh. In particular the squared tail beyond \(R\) is at most \(C e^{-c'R^2}\), after reducing \(c'\).

The appendix is a derivation, not an assumed light-tail condition. It controls the accumulated deterministic response coefficients on both layers. The second-layer derivatives stay bounded; the first-layer derivatives have a Gaussian exponential bound. A short-time induction closes these bounds uniformly in the number of Euler steps.

## Population Euler converges to a unique flow

For comparing two population states use
\[
d=\sum_{a=1}^3
\bigl(\mathbb E|Z_a^{(1)}-\widetilde Z_a^{(1)}|^2\bigr)^{1/2}
+\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
+\bigl(\mathbb E|W^{(3)}-\widetilde W^{(3)}|^2\bigr)^{1/2}.
\tag{M8}
\]
At finite width replace each mean-square norm by the Euclidean norm divided by \(\sqrt n\).

All Euler trajectories, and all the actual discrete trajectories with \(\eta_n\le1\), have bounds independent of width on a fixed bounded time interval, whenever the initial readout supremum and matrix operator norm are bounded. To see this, boundedness of \(\phi\) gives
\[
|r_a|\le 1+\frac{\pi}{2}\|W^{(3)}\|_\infty,\qquad
\|W^{(3)}_{k+1}\|_\infty
\le\|W^{(3)}_k\|_\infty+
C\eta_n(1+\|W^{(3)}_k\|_\infty).
\]
The geometric sum bounds the readout supremum. The rank-one update then bounds the matrix operator norm, and the first-layer update bounds the root-mean-square velocity and displacement. The same calculation applies to population Euler with \(\Delta\). All initial bounds hold with probability tending to one for the finite initialization.

On these bounded sets, the forward quantities, residuals, second-layer backward fields, and the maps
\[
(Z_1^{(1)},Z_2^{(1)},Z_3^{(1)},W^{(2)},W^{(3)})
\longmapsto (W^{(2)})^*\delta_a^{(2)}
\]
are Lipschitz in (M8). This follows by adding and subtracting one factor at a time, using boundedness and Lipschitz continuity of \(\phi,\phi'\), the readout supremum bound, and the operator bound.

Only the first-layer multiplication needs a separate estimate. Write
\[
P_a=(W^{(2)})^*\delta_a^{(2)},\qquad
\widetilde P_a=(\widetilde W^{(2)})^*\widetilde\delta_a^{(2)}.
\]
Then
\[
\phi'(Z_a^{(1)})P_a-\phi'(\widetilde Z_a^{(1)})\widetilde P_a
=\phi'(Z_a^{(1)})(P_a-\widetilde P_a)
+[\phi'(Z_a^{(1)})-\phi'(\widetilde Z_a^{(1)})]\widetilde P_a.
\]
Split the last term at \(|\widetilde P_a|=R\). Since \(\phi'\) is bounded and Lipschitz,
\[
\|[\phi'(Z)-\phi'(\widetilde Z)]\widetilde P\|_{L^2}
\le C R\|Z-\widetilde Z\|_{L^2}
+C\|\widetilde P\,1_{\{|\widetilde P|>R\}}\|_{L^2}.
\tag{M9}
\]
Here \(\|V\|_{L^2}=(\mathbb E V^2)^{1/2}\). Only the reference field needs a tail bound. For a reference Euler grid point, (M7) bounds the final term by \(C e^{-cR^2}\).

An Euler interpolant moves by at most \(C\Delta\) in (M8) between grid points. Its backward field therefore differs from the grid field by at most \(C\Delta\) in mean square, using the Lipschitz map above. Thus, at any intermediate time, the vector field differs from the interpolant's assigned grid velocity by at most
\[
C(1+R)\Delta+C e^{-cR^2}.
\tag{M10}
\]
The same localization gives the comparison inequality for two meshes. Integration and the elementary Gronwall inequality yield, for \(0<T\le T_0\),
\[
\sup_{t\le T}d(\theta^\Delta(t),\theta^{\Delta'}(t))
\le
C e^{C(1+R)T}
\left((1+R)(\Delta+\Delta')+e^{-cR^2}\right).
\tag{M11}
\]
First send both meshes to zero with \(R\) fixed. Then send \(R\) to infinity. The term \(e^{C(1+R)T-cR^2}\) vanishes, so the Euler paths are Cauchy uniformly in time in (M8).

The state spaces are complete, and the limit keeps the readout supremum and operator bounds. The coordinate product \((Z,P)\mapsto\phi'(Z)P\) is continuous from \(L^2\times L^2\) to \(L^2\): split off the change of \(P\), then use boundedness of \(\phi'\) and dominated convergence against the fixed limiting \(P^2\). This allows passage to the integral form of (M4). The limit is therefore a solution, not just a limit of observables. It inherits (M7) by convergence in probability and Fatou's inequality; at intermediate grid times use the \(O(\Delta)\) backward-field difference.

The same estimate compares this solution with any other solution of (M4) in the bounded state class with the same initial state. Only the constructed reference solution requires (M7). Their error is bounded by \(C e^{C(1+R)T-cR^2}\) for every \(R\), hence is zero. This proves uniqueness.

The equations use only the current fields and the current action and adjoint. In particular, their future evolution does not require the stored Euler history. More formally, the closed spaces generated by current fields, bounded coordinate operations, and current forward/adjoint actions contain the future: clipped vector fields and their Euler approximations remain there, and (M9) removes the clipping. Equal current joint action laws identify these generated spaces by a mean-square isometry, which intertwines their actions. Uniqueness therefore identifies their future action laws. This proves autonomy and restartability along the constructed interval.

## From the population flow to the actual fine-step GD

Fix a coarse mesh \(\Delta\), independently of the actual step \(\eta_n\). Build a finite oracle by expanding (M6), supplying it with the population residuals and every population contraction in these expansions. It starts from the same finite first-layer initialization and the same \(W_0^{(2)}\) as GD, but has \(W_0^{(3)}=0\). Every oracle instruction now has deterministic scalar coefficients. The fixed finite Gaussian theorem applies jointly to all its nodes and proves convergence of all the needed empirical contractions and second moments.

There is a useful distinction between oracle nodes and an actual finite network state. Construct proxy parameter arrays using its first-layer nodes and readout, and the matrix
\[
W_{k,\mathrm{proxy}}^{(2)}
=W_0^{(2)}-\frac{2\Delta}{n}
\sum_{s<k,b}r_{b,s}\delta_{b,s,\mathrm{oracle}}^{(2)}
(h_{b,s,\mathrm{oracle}}^{(1)})^\top.
\tag{M12}
\]
Applying this proxy matrix to a current oracle activation differs from its prescribed oracle preactivation only by sums of empirical-minus-population contractions. For example each forward discrepancy has the form
\[
-2\Delta r_{b,s}\delta_{b,s,\mathrm{oracle}}^{(2)}
\left(
\frac{(h_{b,s,\mathrm{oracle}}^{(1)})^\top
h_{a,k,\mathrm{oracle}}^{(1)}}{n}
-\mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}]
\right).
\tag{M13}
\]
The transpose discrepancy has the corresponding contraction of two \(\delta^{(2)}\) fields. At a fixed mesh there are finitely many such terms. Their scalar errors tend to zero, and their vector norms stay bounded. The actual network quantities recomputed from the proxy arrays therefore differ from the oracle nodes by \(o_{\mathbb P}(1)\) in root mean square. Bounded readout and the operator bound justify each subsequent forward/backward comparison. In particular its recomputed vector field differs from its prescribed oracle grid velocity by \(o_{\mathbb P}(1)\).

For each fixed threshold \(R\), the oracle's empirical squared tails converge to their population counterparts. One may use continuous upper cutoffs, equal to one beyond \(R\) and zero below \(R-1\), to avoid discontinuities. The fixed finite Gaussian theorem applies to these quadratic-growth measurements. Consequently the root-mean-square tail of the recomputed proxy backward field has limit superior at most \(C e^{-cR^2}\), after modifying constants. This is proved for the reference oracle, not assumed for actual GD.

Linearly interpolate the proxy parameters. Their metric speed is bounded in probability, with limiting bound independent of the mesh, by (M4) and the node consistency just proved. Their between-grid vector-field defect is bounded by (M10), plus a fixed-mesh \(o_{\mathbb P}(1)\). Compare the actual GD interpolant to this proxy. Actual GD's derivative is its vector field at the preceding fine grid point; its state changes by \(O(\eta_n)\) inside a fine step. Apply (M9) with the proxy as reference. No tail bound for the actual GD is needed. Gronwall gives
\[
\begin{aligned}
\sup_{t\le T}d_n(\theta_n^{\mathrm{GD}}(t),\theta_n^{\mathrm{proxy},\Delta}(t))
\le C e^{C(1+R)T}
\bigg(
&\frac{\|W_{n,0}^{(3)}\|_2}{\sqrt n}
+(1+R)(\eta_n+\Delta)\\
&+e^{-cR^2}+o_{\mathbb P}(1)
\bigg).
\end{aligned}\tag{M14}
\]
The \(o_{\mathbb P}(1)\) here is at fixed \(R,\Delta\). Bounds on the actual readout supremum are obtained from its update, not from root-mean-square closeness.

The initialization discrepancy vanishes, and \(\eta_n\to0\). First take \(n\to\infty\) at fixed \(R,\Delta\); next take \(\Delta\to0\); finally take \(R\to\infty\). Together with (M11), the fixed-mesh oracle empirical convergence, and the triangle inequality for observables, this proves the claimed joint limit. Thus this local proof needs no width-dependent learning-rate restriction beyond \(\eta_n\to0\).

For the first kernel block, use (M9) once more to transfer the first-layer \(\delta^{(1)}\) fields in mean square; the other blocks follow directly from the bounded/Lipschitz maps. Products and contractions then converge by Cauchy–Schwarz. For hidden velocities,
\[
\dot z_a^{(2)}
=\dot W^{(2)}h_a^{(1)}
+W^{(2)}\bigl[\phi'(z_a^{(1)})\odot\dot z_a^{(1)}\bigr].
\]
The reference first-layer velocity is a finite linear combination of bounded multiples of the backward fields, hence has the same tail control. Applying the same comparison proves convergence of both hidden velocities in integrated mean square and hence of their integrated squared norms.

To obtain path-law convergence, first use the finite Gaussian theorem on any fixed finite time grid. Between two times separated by at most \(\varepsilon\), any absolutely continuous coordinate path satisfies
\[
\sup_{s,t\ \mathrm{in\ one\ grid\ cell}}|z(t)-z(s)|^2
\le\varepsilon\int_{\mathrm{cell}}|\dot z(u)|^2\,du.
\]
The proved mean-energy bounds therefore approximate empirical and population path laws, in squared uniform-path distance, by their piecewise linear grid reconstructions with error at most \(C\varepsilon\). Letting the grid become fine gives the joint three-input path-law assertion. The same finite-grid approximation and (M9) give uniform-in-time convergence of the stated fixed action probes.

## Strict feature learning without assuming that G is invertible

We have proved existence, uniqueness, and convergence without needing \(G\) positive definite. For strict feature learning, two additional arguments replace the two-input proof's full-support and exchange-symmetry shortcuts.

Write
\[
Z_{0,a}^{(1)}=\frac{w^\top x_a}{\sqrt d},\qquad w\sim N(0,I_d),\qquad
Q_{ab}=\mathbb E[H_{0,a}^{(1)}H_{0,b}^{(1)}].
\]
We first prove \(Q\) positive definite even if \(G\) has rank two. If \(c^\top Qc=0\), then
\[
\sum_{a=1}^3c_a\arctan(w^\top x_a/\sqrt d)=0
\]
almost surely. Continuity and the full support of \(w\) make this identity hold for every \(w\in\mathbb R^d\).

Choose \(v\in\mathbb R^d\) outside the finitely many hyperplanes
\[
v^\top x_a=0,\qquad v^\top(x_a-x_b)=0,\qquad
v^\top(x_a+x_b)=0.
\]
Each is a proper hyperplane because the inputs are nonzero and no two equal up to sign. A finite union of proper hyperplanes cannot cover \(\mathbb R^d\). Hence the numbers \(b_a=v^\top x_a/\sqrt d\) are nonzero and their squares are distinct. Restrict the identity to \(w=tv\). The coefficients of \(t,t^3,t^5\) in
\(\arctan(tb)=tb-(tb)^3/3+(tb)^5/5+O(t^7)\) give
\[
\sum_a c_a b_a(b_a^2)^k=0,\qquad k=0,1,2.
\]
The determinant of the matrix with columns \((1,b_a^2,b_a^4)^\top\) is
\(\prod_{a<b}(b_b^2-b_a^2)\ne0\). Thus \(c_a b_a=0\) for every \(a\), hence \(c=0\). This proves \(Q\succ0\).

The first forward calls now give a full-support Gaussian triple
\[
(Z_{0,1}^{(2)},Z_{0,2}^{(2)},Z_{0,3}^{(2)})\sim N(0,Q).
\]
Define the repeated coefficients
\[
S=\sum_a y_aH_{0,a}^{(2)},\quad
U_a=S\phi'(Z_{0,a}^{(2)}),\quad
P_a=(W_0^{(2)})^*U_a,\quad
B_a=\phi'(Z_{0,a}^{(1)})P_a,
\]
\[
V_{ab}=\mathbb E[U_aU_b],\qquad D_{ab}=\mathbb E[B_aB_b].
\tag{M15}
\]
Conditional on the last two second-layer coordinates, \(S\) is a strictly monotone function of the first coordinate. That first coordinate has a continuous conditional Gaussian density, so \(\mathbb P(S=0)=0\). If \(\sum_ac_aU_a=0\), division by \(S\), full support, and continuity imply
\(\sum_ac_a\phi'(s_a)=0\) for every \(s\in\mathbb R^3\). Varying one coordinate while fixing the other two forces each \(c_a=0\). Therefore \(V\succ0\).

The simultaneous initial transpose responses satisfy
\[
P_a=\sum_{c=1}^3H_{0,c}^{(1)}
\left[
Q^{-1}
\begin{pmatrix}
\mathbb E[Z_{0,1}^{(2)}U_a]\\
\mathbb E[Z_{0,2}^{(2)}U_a]\\
\mathbb E[Z_{0,3}^{(2)}U_a]
\end{pmatrix}
\right]_c+\Gamma_a,
\tag{M16}
\]
where \(\Gamma\sim N(0,V)\) is independent of the first-layer roots. This follows by conditioning the initial Gaussian matrix on its three forward calls. Its fresh transpose part has source covariance \(V\); the finite-rank projection onto the initial forward directions disappears in normalized mean square. Equivalently, Gaussian integration by parts gives this instance of the appendix response rule.

Since every \(\phi'(Z_{0,a}^{(1)})>0\), the conditional covariance of \((B_1,B_2,B_3)\), given the first-layer roots, is positive definite. Hence \(D\succ0\).

Define the first- and second-layer displacement coefficients by
\[
T_a=\sum_bG_{ab}y_bB_b,\qquad
R_a=\sum_b y_bQ_{ab}U_b+
W_0^{(2)}[\phi'(Z_{0,a}^{(1)})T_a].
\tag{M17}
\]
Each \(T_a\) has strictly positive conditional variance. In fact its coefficient of \(\Gamma_a\) in (M16) is \(G_{aa}y_a\phi'(Z_{0,a}^{(1)})\ne0\), and \(V\) is positive definite. Thus \(\mathbb E[T_a^2]>0\).

To prove every \(R_a\) nonzero we cannot use input-exchange symmetry: a general triple has none. Instead examine the next forward call. Denote its input, which recurs in this calculation, by
\[
J_a=\phi'(Z_{0,a}^{(1)})T_a.
\]
Let \(\alpha_a\in\mathbb R^3\) solve
\[
\sum_c Q_{bc}\alpha_{a,c}=\mathbb E[H_{0,b}^{(1)}J_a],
\qquad b=1,2,3,
\]
and subtract the component explained by the previous forward inputs:
\[
J_a^\perp=J_a-\sum_c\alpha_{a,c}H_{0,c}^{(1)},\qquad
\sigma_a^2=\mathbb E[(J_a^\perp)^2].
\]
This is ordinary least-squares projection onto the three old \(H\) fields.

Given the first-layer roots, \(J_a\) is a linear function of the Gaussian vector \(\Gamma\), with coefficients
\[
c_b=\phi'(Z_{0,a}^{(1)})G_{ab}y_b\phi'(Z_{0,b}^{(1)}).
\]
In particular \(c_a=y_a\phi'(Z_{0,a}^{(1)})^2\ne0\). Subtracting a function of the roots cannot remove this conditional randomness, so
\[
\sigma_a^2
\ge\mathbb E[\operatorname{Var}(J_a\mid Z_{0,1}^{(1)},Z_{0,2}^{(1)},Z_{0,3}^{(1)})]
=\mathbb E[c^\top Vc]>0.
\tag{M18a}
\]

Condition on the already revealed forward calls
\(W_0^{(2)}H_{0,c}^{(1)}=Z_{0,c}^{(2)}\) and transpose calls
\((W_0^{(2)})^*U_b=P_b\). The new forward call has the population law
\[
W_0^{(2)}J_a
=\sum_c\alpha_{a,c}Z_{0,c}^{(2)}
+\sum_b\beta_{a,b}U_b+\sigma_a\gamma_a,
\qquad
\sum_c V_{bc}\beta_{a,c}=\mathbb E[P_bJ_a^\perp].
\tag{M18b}
\]
Here \(\gamma_a\sim N(0,1)\) is independent of the previous second-layer history. To see the variance, the remaining finite Gaussian matrix is projected orthogonally to the three observed input directions on each side. Applying it to the part of \(J_a\) perpendicular to the old \(H\) inputs gives variance \(\|J_a^\perp\|_2^2/n\). The output projection has fixed rank three, so its removal changes normalized mean square by \(O(1/n)\). Joint empirical convergence then gives (M18b). The response coefficients follow from the two recorded matrix identities. Both Gram inverses are legitimate because \(Q,V\succ0\). One such calculation is made for each \(a\); independence of the three \(\gamma_a\) from one another is neither claimed nor needed.

The learned-matrix contribution \(\sum_b y_bQ_{ab}U_b\) in \(R_a\) depends only on the previous second-layer coordinates. It cannot cancel the independent new Gaussian term. Thus
\[
\mathbb E[R_a^2]\ge\sigma_a^2>0,\qquad a=1,2,3.
\tag{M18c}
\]

Substitution in the integral equations, beginning with \(W^{(3)}(0)=0\) and \(r_a(0)=-y_a\), gives
\[
W^{(3)}(t)=2tS+o_{L^2}(t),\qquad
\delta_a^{(2)}(t)=2tU_a+o_{L^2}(t),
\]
\[
Z_a^{(1)}(t)-Z_{0,a}^{(1)}=2t^2T_a+o_{L^2}(t^2),
\]
\[
W^{(2)}(t)-W_0^{(2)}
=2t^2\sum_b y_bU_b\otimes H_{0,b}^{(1)}+o_{\rm op}(t^2),
\]
\[
Z_a^{(2)}(t)-Z_{0,a}^{(2)}=2t^2R_a+o_{L^2}(t^2).
\tag{M19}
\]
For example the readout integral divided by \(t\) converges to \(2S\), then the second-layer backward field divided by \(t\) converges to \(2U_a\). Integrating the first-layer and matrix velocities therefore gives the factors \(2t^2\). Expanding \(W^{(2)}H_a^{(1)}\) gives the two terms in \(R_a\). Each passage uses bounded \(\phi,\phi'\), the bounded matrix action, and strong mean-square continuity. Differentiating the activation along these strongly convergent mean-square increments is justified by dominated convergence against their fixed limiting direction; no global differentiability claim for nonlinear maps on the whole mean-square space is used.

The corresponding hidden velocities are \(4tT_a+o_{L^2}(t)\) and \(4tR_a+o_{L^2}(t)\). Consequently each input's squared displacement has positive coefficient \(4\mathbb E[T_a^2]\) or \(4\mathbb E[R_a^2]\) times \(t^4\), and its integrated squared speed has positive coefficient \((16/3)\mathbb E[T_a^2]\) or \((16/3)\mathbb E[R_a^2]\) times \(t^3\).

It remains to check that singular \(G\) does not make a kernel block singular. Let \(\lambda>0\) be the smallest eigenvalue of \(D\). For every \(c\in\mathbb R^3\),
\[
\begin{aligned}
\sum_{a,b}c_ac_bG_{ab}D_{ab}
&=\frac1d\sum_{j=1}^d
\mathbb E\left[\left(\sum_a c_a x_{a,j}B_a\right)^2\right]\\
&\ge\frac{\lambda}{d}\sum_{j=1}^d\sum_a c_a^2x_{a,j}^2
=\lambda\sum_a c_a^2 .
\end{aligned}
\tag{M20}
\]
This uses normalization, not invertibility of \(G\). Thus the matrix with entries \(G_{ab}D_{ab}\) is positive definite. Likewise the matrix with entries \(Q_{ab}V_{ab}\) is positive definite: if \(\lambda_V>0\) is the smallest eigenvalue of \(V\), its quadratic form is at least \(\lambda_V\sum_aQ_{aa}c_a^2>0\) for \(c\ne0\).

Put
\[
A_1=\sum_{a,b}y_ay_bG_{ab}D_{ab}>0,\qquad
A_2=\sum_{a,b}y_ay_bQ_{ab}V_{ab}>0.
\]
Adjunction and (M17) give
\[
\sum_a y_a\mathbb E[U_aR_a]=A_1+A_2.
\]
The kernel expansions are
\[
K^{(1)}_{ab}(t)=4t^2G_{ab}D_{ab}+o(t^2),\qquad
K^{(2)}_{ab}(t)=4t^2Q_{ab}V_{ab}+o(t^2).
\]
Expanding \(H_a^{(2)}(t)\) using (M19) shows that the readout block contributes \(4(A_1+A_2)t^2\) to its quadratic form in direction \(y\). The other two blocks contribute the same amount. Therefore
\[
y^\top K(t)y
=y^\top K^{(3)}(0)y+8(A_1+A_2)t^2+o(t^2).
\tag{M21}
\]
The total kernel is nonconstant. The first two blocks are positive definite at sufficiently small positive times by (M20). The initial readout block is positive definite because the second-layer Gaussian triple has full support, and the three coordinate arctangents have no linear relation. It remains positive definite by continuity.

Finally,
\[
L(0)=3,\qquad \dot L(0)=-4y^\top K^{(3)}(0)y<0.
\]
The loss strictly decreases on a sufficiently small interval. Every initial hidden marginal is a nondegenerate Gaussian, so it has positive variance and positive best-affine-fit error for \(\arctan\). The variance/covariance formula for that fit and mean-square continuity preserve positivity for small time.

All strict conclusions hold on some \((0,T_*]\) with \(0<T_*\le T_0\). These time constants do not depend on \(n\), \(\eta_n\), or \(\Delta\). The existence time \(T_0\) is uniform over normalized triples; the activity interval and positive activity coefficients may depend on the fixed triple and labels. No lower bound uniform near parallel configurations is claimed for those coefficients.

## Appendix: the mesh-uniform response calculation

The following calculation supplies (M7). Its equation numbers are local to the appendix.

Let the input Gram matrix be
\[
G_{ab}=x_a^\top x_b/d,\qquad G\succeq0,\quad G_{aa}=1,\quad |G_{ab}|\le1,
\]
and labels be \(y_1,y_2,y_3\in\{-1,1\}\). Use the summed loss \(\sum_{a=1}^3r_a^2\); averaging the loss only rescales time. The first-layer population root \((Z_{1,0}^{(1)},Z_{2,0}^{(1)},Z_{3,0}^{(1)})\) is centered Gaussian with covariance \(G\). The shared readout starts at \(W_0^{(3)}=0\).

For fixed mesh \(\Delta>0\), population Euler obeys
\[
H_{a,k}^{(1)}=\phi(Z_{a,k}^{(1)}),\quad
Z_{a,k}^{(2)}=W_k^{(2)}H_{a,k}^{(1)},\quad
H_{a,k}^{(2)}=\phi(Z_{a,k}^{(2)}),\quad
\delta_{a,k}^{(2)}=W_k^{(3)}\phi'(Z_{a,k}^{(2)}),
\]
\[
r_{a,k}=\mathbb E[W_k^{(3)}H_{a,k}^{(2)}]-y_a,
\]
\[
Z_{a,k+1}^{(1)}=Z_{a,k}^{(1)}-2\Delta\sum_{b=1}^3G_{ab}r_{b,k}\phi'(Z_{b,k}^{(1)})P_{b,k},
\qquad P_{b,k}:=(W_k^{(2)})^*\delta_{b,k}^{(2)},
\tag{1}
\]
\[
W_{k+1}^{(2)}=W_k^{(2)}-2\Delta\sum_{b=1}^3r_{b,k}\delta_{b,k}^{(2)}\otimes H_{b,k}^{(1)},
\qquad
W_{k+1}^{(3)}=W_k^{(3)}-2\Delta\sum_{b=1}^3r_{b,k}H_{b,k}^{(2)}.
\tag{2}
\]
Here \(\phi=\arctan\). All response derivatives below hold every deterministic coefficient in these finite recursions fixed, including residuals, contractions, and response coefficients. They do not differentiate through expectations or through the covariance law.

## Exact finite-mesh Gaussian response representation

Introduce two centered jointly Gaussian collections \(\xi_{a,k}\) and \(\eta_{a,k}\), independent of one another. The first-layer root is independent of both. Their covariances are
\[
\mathbb E[\xi_{a,k}\xi_{b,s}]=\mathbb E[H_{a,k}^{(1)}H_{b,s}^{(1)}],
\qquad
\mathbb E[\eta_{a,k}\eta_{b,s}]=\mathbb E[\delta_{a,k}^{(2)}\delta_{b,s}^{(2)}].
\tag{3}
\]
These are separate-layer probability spaces; taking them independent on a product space is only a convenient representation, not an assertion of a natural pairing of neurons across layers.

Define the deterministic coefficients
\[
A_{ak,bs}:=\mathbb E\left[\frac{\partial\delta_{a,k}^{(2)}}{\partial\xi_{b,s}}\right],\quad s\le k,
\qquad
C_{ak,bs}:=\mathbb E\left[\frac{\partial H_{a,k}^{(1)}}{\partial\eta_{b,s}}\right],\quad s<k.
\tag{4}
\]
The derivatives are symbolic derivatives of the displayed causal recursions, treating Gaussian slots as separate real arguments even when their realized joint covariance is singular. Then the exact limiting initial-matrix actions are
\[
W_0^{(2)}H_{a,k}^{(1)}=
\xi_{a,k}+\sum_{b=1}^3\sum_{s<k}C_{ak,bs}\delta_{b,s}^{(2)},
\tag{5}
\]
\[
(W_0^{(2)})^*\delta_{a,k}^{(2)}=
\eta_{a,k}+\sum_{b=1}^3\sum_{s\le k}A_{ak,bs}H_{b,s}^{(1)}.
\tag{6}
\]
Expanding the learned matrix gives the full equations
\[
Z_{a,k}^{(2)}=
\xi_{a,k}+\sum_{b=1}^3\sum_{s<k}
\left(C_{ak,bs}-2\Delta r_{b,s}\mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}]\right)
\delta_{b,s}^{(2)},
\tag{7}
\]
\[
P_{a,k}=
\eta_{a,k}+\sum_{b=1}^3\sum_{s\le k}
\left(A_{ak,bs}-\mathbf1_{s<k}2\Delta r_{b,s}\mathbb E[\delta_{b,s}^{(2)}\delta_{a,k}^{(2)}]\right)
H_{b,s}^{(1)}.
\tag{8}
\]
Together with (1), the readout update in (2), and \(\delta=W^{(3)}\phi'(Z^{(2)})\), these are causal finite recursions. To construct step \(k\): first construct \(H_{a,k}^{(1)}\) and its derivatives using \(\eta\)-slots through \(k-1\); next construct \(Z_{a,k}^{(2)},\delta_{a,k}^{(2)}\) using \(\xi\)-slots through \(k\); finally construct \(P_{a,k}\) and update first-layer coordinates and readout. The Gaussian covariance matrices extend consistently because they are Gram matrices of the constructed source variables.

Why the Gaussian response rule has this form: conditioning on previous forward and transpose products gives the Gaussian matrix regression formula with a projected fresh Gaussian matrix. In the limit, its Gaussian parts in each orientation have covariance equal to the Gram matrix of the sources. Its non-Gaussian part lies in the span of the previous sources in the opposite orientation. Gaussian integration by parts identifies the coefficients of this response as the expectations in (4). The elementary identity used is, for a centered Gaussian vector \(g\) with covariance \(\Sigma\),
\[
\mathbb E[g_i f(g)]=\sum_j\Sigma_{ij}\mathbb E[\partial_j f(g)].
\tag{9}
\]
It is valid even for singular \(\Sigma\), by writing \(g=B\gamma\) and integrating by parts in independent standard Gaussian coordinates \(\gamma\). If the conditional regression uses a pseudoinverse, the symbolic derivative coefficients and the pseudoinverse coefficients can differ only by a vector in the covariance nullspace; the corresponding combination of source variables has zero squared norm, so the response itself is unchanged. This is the singular-covariance issue that must be retained in a complete proof.

For a rigorous external formulation of this finite-program identity, see [Tensor Programs III](https://arxiv.org/pdf/2009.10685), Box 1, Remarks 2.11–2.12 and Theorem 2.10. The algebraic recursions here are smooth, polynomially bounded functions of finitely many Gaussian slots, and their symbolic derivatives are polynomially bounded for fixed program length. Thus all expectations in (4) exist. The finite-query theorem handles fixed program length; the estimates below are the additional ingredient needed uniformly as length increases. This note does not purport to reprove the entire master theorem in the preceding paragraph.

## Uniform short-time response bounds

Fix \(T\le1\) and \(k\Delta\le T\). Constants in this section depend only on bounds for \(\phi,\phi',\phi''\), on the bounds \(|G_{ab}|\le1\) and the fixed number three of inputs; they do not depend on \(\Delta\), \(k\), or the Gaussian covariance ranks.

Put \(B_k=\|W_k^{(3)}\|_\infty\). Since \(|r_{a,k}|\le1+\|\phi\|_\infty B_k\), (2) gives
\[
B_{k+1}\le B_k+6\Delta\|\phi\|_\infty(1+\|\phi\|_\infty B_k).
\]
The resulting geometric sum gives, for a fixed \(C_0\),
\[
B_k\le C_0T,\qquad |r_{a,k}|\le C_0,\qquad |\delta_{a,k}^{(2)}|\le C_0T.
\tag{10}
\]
The absolute row sums of the training-memory coefficients in (7) and (8) are therefore at most \(C_0T\) and \(C_0T^3\), respectively.

Define
\[
\mathcal A_k=\max_{a,\,r\le k}\sum_{b=1}^3\sum_{s\le r}|A_{ar,bs}|,
\qquad
\mathcal C_k=\max_{a,\,r\le k}\sum_{b=1}^3\sum_{s<r}|C_{ar,bs}|.
\tag{11}
\]
Equation (8) already gives the pathwise bound
\[
|P_{a,k}-\eta_{a,k}|\le C_0(\mathcal A_k+T^3),
\qquad
\mathbb E[\eta_{a,k}^2]\le C_0^2T^2.
\tag{12}
\]

First estimate \(\mathcal C_k\) in terms of \(\mathcal A_{k-1}\). Let \(J_k\) be the maximum, over the first-layer coordinates at times through \(k\), of the sum of absolute derivatives with respect to all backward Gaussian slots \(\eta_{b,s}\). Initially \(J_0=0\). In (8), the derivative of \(P_{a,k}\) has absolute sum at most
\[
1+(\mathcal A_k+C_0T^3)J_k,
\]
because \(|\phi'|\le1\). Differentiating (1) and using bounded \(G,r,\phi',\phi''\) gives
\[
J_{k+1}\le
\left(1+C\Delta\left[1+\mathcal A_k+\sum_{b=1}^3|\eta_{b,k}|\right]\right)J_k+C\Delta.
\tag{13}
\]
Consequently,
\[
J_k\le CT\exp\left(CT(1+\mathcal A_{k-1})+C\Delta\sum_{r<k}\sum_{b=1}^3|\eta_{b,r}|\right).
\tag{14}
\]
No independence over time is used. Jensen's inequality applied to the average of the \(3k\) terms, followed by the scalar Gaussian exponential bound, gives
\[
\mathbb E\exp\left(C\Delta\sum_{r<k}\sum_{b=1}^3|\eta_{b,r}|\right)
\le 2\exp\left(\frac92 C^2C_0^2T^4\right).
\tag{15}
\]
Since absolute expectation is bounded by expectation of absolute value, (4), (14), and (15) imply
\[
\mathcal C_k\le CT\exp\left(CT(1+\mathcal A_{k-1})+CT^4\right),
\tag{16}
\]
after increasing \(C\).

Now estimate \(\mathcal A_k\) through the second-layer recursion. Let \(V_k\) be the maximum, over \(Z_{a,r}^{(2)}\) for \(r\le k\), of the sum of absolute derivatives with respect to all forward Gaussian slots \(\xi_{b,s}\). It is a nonnegative random variable, but the bound below is deterministic.

The readout is
\[
W_k^{(3)}=-2\Delta\sum_{r<k}\sum_{a=1}^3r_{a,r}\phi(Z_{a,r}^{(2)}).
\]
Therefore its derivative absolute sum is at most \(C_0T V_k\). Differentiating \(\delta_{a,k}^{(2)}=W_k^{(3)}\phi'(Z_{a,k}^{(2)})\), using (10), yields
\[
\sum_{b,s}\left|\frac{\partial\delta_{a,k}^{(2)}}{\partial\xi_{b,s}}\right|\le C_1T V_k.
\tag{17}
\]
Equation (7), whose memory uses only \(s<k\), yields
\[
V_k\le \max\{V_{k-1},\,1+C_1T(\mathcal C_k+C_0T)V_{k-1}\}.
\tag{18}
\]
Initially \(V_0=1\) and \(\mathcal A_0=0\).

Choose fixed constants \(M_A=2C_1\) and \(M_C\) large enough that the right side of (16) is at most \(M_CT\) whenever \(\mathcal A_{k-1}\le M_AT\) and \(T\le T_0\). All these constants can be chosen independently of the input geometry because only \(|G_{ab}|\le1\) was used. Then choose \(T_0>0\) small enough that
\[
C_1T_0^2(M_C+C_0)\le\tfrac12.
\tag{19}
\]
An induction over \(k\) now proves
\[
\mathcal A_k\le M_AT,\qquad \mathcal C_k\le M_CT,\qquad V_k\le2,
\qquad k\Delta\le T\le T_0.
\tag{20}
\]
Indeed the bound for \(\mathcal A_{k-1}\) supplies the bound for \(\mathcal C_k\) in (16); (18)-(19) then give \(V_k\le2\); (17) gives \(\mathcal A_k\le2C_1T\).

Combining (12) and (20), every backward coordinate is a centered Gaussian of variance at most \(C T^2\), plus a bounded (possibly dependent) remainder of absolute value at most \(CT\). Thus there are fixed \(c,C>0\) such that
\[
\sup_{\Delta>0}\sup_{k\Delta\le T_0}\max_a
\mathbb E\exp\left(c|P_{a,k}|^2/T_0^2\right)\le C.
\tag{21}
\]
This is the desired mesh-uniform Gaussian-tail bound. It was proved from bounded second-layer coordinate derivatives and a short-time response bootstrap. It was not assumed merely from fixed-program moment convergence.
