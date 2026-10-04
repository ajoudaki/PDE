# Functional and adaptive-basis route

Scoped theoretical report, 2026-09-29. Scientific inputs were the supervisor's prompt only. No other study, book passage, manuscript, code, or experimental result was inspected. The research-contract and adversarial-audit procedures of `investigate-conjectures`, and the `solve-math-rigorously` skill, were used. No computation or experiment was performed.

## Conclusion and contract

A shared functional basis has a precise optimization interpretation, but basis sparsity alone does not give a causal compressed training flow. Three positive statements survive:

1. Optimizing an orthonormal sample basis turns column support into rank, columnwise l1 into the nuclear norm, and columnwise l2 into invariant Frobenius energy. This is an exact snapshot statement.
2. Polynomial activations admit exact, autonomous, sample-count-independent training through finitely many empirical input/target moments. The same polynomial representation replaces sample-indexed temporal history slots, without changing whatever temporal truncation was already used. Its degree grows exponentially with depth and its monomial count can be prohibitive.
3. On a bounded data class and finite horizon, uniform approximation of the per-sample gradient gives a genuine trajectory theorem. A fixed weighted subset obtained from an input-space partition supplies a constructive autonomous approximation whose retained size is independent of sample count. It requires initial access to the complete dataset and has a dimension-dependent accuracy cost.

None of these facts implies that a generic smooth deep network has a small exactly closed harmonic basis. The important unresolved implication is from bounded response/atomic norms to a *computable causal generator* with controlled defect; an optimal snapshot expansion does not supply that implication.

The canonical object here is the initialized network with its original dense initialized matrices, original samples, and feature-learning gradient flow. Write the number of samples as m and the relevant width normalization as n. At a hidden layer,

\[
\dot W=-\frac{2}{n}\mathbb E_m[a b^\top],\qquad
a(x,y,t)=r(x,y,t)\delta(x,t),\quad b(x,t)=h(x,t),
\]

where \(\mathbb E_m=m^{-1}\sum_{a=1}^m\). All trainable layers remain trainable. The target is the trajectory on \([0,T]\), not just its endpoint or a low-dimensional observable selected after seeing the answer. State, coefficients, basis descriptions, and online access to the original data must all be counted. Initial preprocessing may read all m samples; that cost is explicitly retained below. No future target trajectory is available for choosing coefficients.

## 1. Exact shared-basis identity and its residual

Equip functions on the m sample indices with
\(\langle f,g\rangle_m=\mathbb E_m[fg]\). Let
\(\phi_1,\ldots,\phi_m\) be an orthonormal basis, and put

\[
A_j=\mathbb E_m[a\phi_j],\qquad B_j=\mathbb E_m[b\phi_j].
\]

Expansion in this finite orthonormal basis gives the exact identity

\[
\mathbb E_m[ab^\top]=\sum_{j=1}^m A_jB_j^\top.
\]

For the projector P onto any K selected modes, the discarded part is exactly

\[
\mathbb E_m[ab^\top]-\sum_{j\leq K}A_jB_j^\top
=\mathbb E_m[((I-P)a)((I-P)b)^\top].
\]

The two mixed terms vanish by orthogonality. Consequently,

\[
\left\|\mathbb E_m[ab^\top]-\sum_{j\leq K}A_jB_j^\top\right\|_*
\leq \|(I-P)a\|_{L^2_m}\,\|(I-P)b\|_{L^2_m}.
\tag{1}
\]

Indeed, a rank-one matrix uv^T has nuclear norm \(\|u\|_2\|v\|_2\); the triangle inequality and scalar Cauchy–Schwarz give (1). The Frobenius and operator norms are bounded by this nuclear-norm bound. Exactness of the update only requires one of a or b to lie in the retained space; it does not require both response fields to be reconstructed exactly.

For a nonorthonormal set of functions collected into \(\phi\in\mathbb R^K\), let \(G=\mathbb E_m[\phi\phi^\top]\) be invertible. The corresponding projected update is

\[
\mathbb E_m[a\phi^\top]G^{-1}\mathbb E_m[\phi b^\top].
\]

Thus a chosen input basis generally introduces empirical Gram and multiplication coefficients; declaring the basis shared does not eliminate these data-dependent objects.

## 2. What adaptive l0, l1, and l2 optimization actually means

Let \(R\in\mathbb R^{d\times m}\) be a normalized response matrix: for example, its a-th column is the concatenation of a_a and b_a divided by \(\sqrt m\). A change of orthonormal sample basis is right multiplication by an orthogonal matrix Q. Its columns are the vector-valued coefficients in the new basis.

Three exact variational identities are

\[
\begin{aligned}
\min_{Q\in O(m)}\#\{j:(RQ)_{:j}\ne0\}&=\operatorname{rank}R,\\
\min_{Q\in O(m)}\sum_j\|(RQ)_{:j}\|_2&=\|R\|_*,\\
\sum_j\|(RQ)_{:j}\|_2^2&=\|R\|_F^2\quad\text{for every }Q.
\end{aligned}
\tag{2}
\]

For the first identity, any k nonzero columns give a rank-at-most-k matrix, while choosing Q to contain the right singular vectors attains rank R columns. For the second, write
\(R=\sum_j(RQ)_{:j}q_j^\top\). Each q_j has unit norm, so the nuclear triangle inequality gives the lower bound; the same singular-vector choice attains the sum of singular values. The final identity follows from \(QQ^\top=I\).

There is also an exact least-squares basis optimization:

\[
\min_{P=P^\top=P^2,\;\operatorname{rank}P=K}
\|R(I-P)\|_F^2=\sum_{j>K}\sigma_j(R)^2.
\tag{3}
\]

To verify (3), diagonalize \(R^\top R\), with eigenvalues \(\lambda_j=\sigma_j^2\) in decreasing order. Then
\(\|R(I-P)\|_F^2=\sum_j\lambda_j-\sum_j\lambda_j p_j\),
where the diagonal entries of P in that eigenbasis obey \(0\leq p_j\leq1\) and \(\sum_jp_j=K\). Moving mass toward larger eigenvalues shows that the largest possible retained sum is \(\sum_{j\leq K}\lambda_j\). The corresponding eigenvector projector attains it.

These identities resolve part of the proposed optimization interpretation:

- A learned orthonormal sample basis with a column-support constraint is a rank constraint.
- Its columnwise l1 cost is a nuclear-norm cost after optimizing the basis.
- Its columnwise l2 energy cannot select a basis; it is invariant.

They do not resolve causal closure. A column of Q contains m entries. Keeping K coefficient vectors while omitting the cost of the K sample-space basis vectors hides mK numbers. A function representation \(\phi_j(x,y)\) can avoid that storage only if its parameters, evaluation cost, and evolution are themselves bounded independently of m.

An especially sharp degeneracy occurs for one scalar response f: choosing the first basis vector to be \(f/\|f\|\) makes f one-sparse. The first basis vector now contains the original response. Consequently, unconstrained adaptive orthonormal l1 minimization for a single vector reduces to its l2 norm, not a compression theorem.

Normalization and nonredundancy of atoms also matter. With unit rank-one matrix atoms, minimal l0 is rank and minimal l1 is nuclear norm. In contrast, an unrestricted coefficient l2 cost is degenerate even for normalized atoms: replace one coefficient c by J repeated copies c/J, decreasing its squared coefficient cost from c^2 to c^2/J without changing the represented object. Schatten-p statements concern singular-value coefficients, or a sufficiently specified equivalent variational problem, not arbitrary learned coefficients.

## 3. Norm control, frequency control, and matrix control differ

For a fixed orthonormal basis, an l1 coefficient bound \(\sum_j|c_j|\leq B\) gives the best-K-term error

\[
\left(\sum_{j>K}|c_j^*|^2\right)^{1/2}\leq\frac{B}{\sqrt{K+1}},
\]

where \(|c_j^*|\) are in decreasing order. This follows from
\(|c_{K+1}^*|\leq B/(K+1)\) and
\(\sum_{j>K}|c_j^*|^2\leq |c_{K+1}^*|\sum_{j>K}|c_j^*|\).
More generally an lp bound for \(0<p<2\) gives a best-K rate proportional to \(K^{1/2-1/p}\), by bounding \(|c_j^*|\leq B j^{-1/p}\) and summing the squared tail.

This is not a low-frequency cutoff guarantee. A unit coefficient at arbitrarily high frequency has l1=l2=1 and is missed by every fixed cutoff. The selected frequency or atom must also have an admissible description. A weighted spectral condition such as

\[
\sum_{k\in\mathbb Z^{d_x}}(1+|k|^2)^s|c_k|^2\leq B^2
\]

does imply cutoff error at radius R at most \(BR^{-s}\). The number of lattice modes then scales as \(R^{d_x}\), making the input-dimension dependence explicit. Unweighted l2 control does not imply any such uniform tail estimate.

Multiplication exposes a second distinction. On a circle, let \(a=b=\sin(Nx)\). Every fixed Fourier cutoff below N discards both fields, but
\(\mathbb E[ab]=1/2\). High frequencies can generate a constant update. This is an algebraic counterexample to a low-mode closure argument, not a claim that an arbitrary prescribed initialized network must realize this particular pair of fields.

There is a useful stronger matrix fact for the hidden update. Define

\[
\alpha(t)=\big(\mathbb E_m[r^2\|\delta\|_2^2]\big)^{1/2},\qquad
\beta(t)=\big(\mathbb E_m[\|h\|_2^2]\big)^{1/2}.
\]

The canonical outer-product representation implies

\[
\|\dot W(t)\|_*\leq\frac2n\alpha(t)\beta(t),\qquad
\|W(t)-W_0\|_*\leq V_T:=\frac2n\int_0^T\alpha(s)\beta(s)\,ds.
\tag{4}
\]

Hence at every time t there exists a rank-K matrix M_K(t) with

\[
\|W(t)-W_0-M_K(t)\|_F\leq\frac{V_T}{\sqrt{K+1}},\qquad
\|W(t)-W_0-M_K(t)\|_{\rm op}\leq\frac{V_T}{K+1}.
\tag{5}
\]

The proof uses the singular-value tail and the same l1 argument above. This bound is independent of m only if V_T is bounded independently of m in the stated network normalization. It need not be independent of width, depth, initialized operator norms, input norms, labels, or horizon.

Equation (4) contains more information than an arbitrary Frobenius-energy bound on the response matrix: bounded response energies produce a nuclear bound on their averaged bilinear update. Thus failure of l2 response compression does not refute update-matrix compression.

Equation (5) is still an existence statement for snapshots. It gives no equations for M_K. Even rank-one instantaneous updates can accumulate full exact rank: with
\(v(t)=(1,t,\ldots,t^{d-1})^\top\), the matrix
\(\int_0^t v(s)v(s)^\top ds\) is positive definite for every t>0, since its quadratic form is the integral of the square of a nonzero polynomial. This example does not contradict approximate low-rank bounds; it rules out inferring exact cumulative rank from instantaneous rank.

## 4. Why adaptive snapshots do not automatically give closed dynamics

If the basis varies with time, its coefficients satisfy

\[
\frac{d}{dt}\langle a,\phi_j\rangle_m
=\langle\dot a,\phi_j\rangle_m+\langle a,\dot\phi_j\rangle_m.
\tag{6}
\]

The second term must be computed. Selecting a singular basis at each time requires the current response matrix, and differentiating that selection may encounter repeated singular values or vanishing gaps. Neither operation is accounted for by retaining just the coefficient vectors.

A rank-constrained differential approximation does have an exact optimization interpretation. On a smooth fixed-rank matrix manifold \(\mathcal M_K\), choose

\[
\dot{\widetilde W}
=\arg\min_{V\in T_{\widetilde W}\mathcal M_K}
\|V-F(\widetilde W)\|_F^2.
\tag{7}
\]

The minimizer is the orthogonal tangent projection of F. If \(F=-\nabla L\), this is gradient flow of the restriction of L to that manifold under the induced Euclidean metric. It remains a different flow from the unconstrained canonical training flow.

Nuclear bounds alone do not make its normal defect small. At
\(X=\operatorname{diag}(1,\ldots,1,0)\) of rank K, the unit-nuclear-norm direction \(F=e_{K+1}e_{K+1}^\top\) is entirely normal to the rank-K tangent space. For the smooth quadratic loss
\(L(Y)=\tfrac12\|Y-(X+F)\|_F^2\), the constrained flow starts with zero velocity, while the unconstrained flow starts with velocity F. This is a counterexample to the claimed implication from nuclear control to small tangent defect, not to every possible causal rank-compression rule.

There is a general exact error statement. If the original state obeys \(\dot\theta=F(\theta)\), the compressed state reconstructs \(\widetilde\theta\) with
\(\dot{\widetilde\theta}=F(\widetilde\theta)+e(t)\), and F is \(\Lambda\)-Lipschitz on both paths, then

\[
\|\theta(t)-\widetilde\theta(t)\|
\leq e^{\Lambda t}\|\theta(0)-\widetilde\theta(0)\|
+\int_0^t e^{\Lambda(t-s)}\|e(s)\|\,ds.
\tag{8}
\]

To prove it, subtract the integral equations, use the Lipschitz inequality, and multiply the associated scalar integral inequality by the integrating factor \(e^{-\Lambda t}\). This controls propagation; the substantive missing estimate for any proposed adaptive basis is a bound on the produced defect e, obtained without the inaccessible full trajectory.

There is also a precise algebraic closure obstruction. A finite-dimensional unital subalgebra A of real functions on m samples, closed under pointwise multiplication, consists of functions constant on the classes of some partition, and its dimension equals the number of classes it distinguishes. To see this, declare two samples equivalent if every f in A takes the same value on both. A generic linear combination of a basis of A has distinct values on all distinct classes: only finitely many hyperplanes of coefficients are forbidden. Lagrange interpolation polynomials in that one function then belong to A and give the indicator of each class. These indicators are independent and span all class-constant functions. Consequently, if A distinguishes all m samples, its dimension is m.

This obstructs universal exact closure by a small response-function algebra. It does not exclude closure on a special reachable family, nor does it exclude the finite *data-moment* representation below, which evaluates the full fixed-depth network algebraically rather than requiring the response space itself to be invariant under every multiplication.

## 5. Exact polynomial-activation compression, including temporal histories

Assume input dimension d_x, scalar output, L nonlinear hidden layers, and a fixed polynomial activation of degree p>=1. Affine biases are allowed. Let

\[
h_0=x,\quad z_l=W_lh_{l-1}+b_l,\quad h_l=\sigma(z_l),\quad
f_\theta(x)=c^\top h_L+b_{\rm out},\quad D=p^L.
\]

For every parameter value, \(h_l(x)\) is a vector of polynomials of degree at most \(p^l\). Put \(\delta_l=\partial f_\theta/\partial z_l\). Backpropagation gives

\[
\deg_x\delta_l
\leq\sum_{j=l}^L(p-1)p^{j-1}
=D-p^{l-1}.
\tag{9}
\]

Indeed, \(\sigma'(z_j)\) has degree at most \((p-1)p^{j-1}\), matrix multiplication does not raise input degree, and products add degrees. Thus

\[
r\delta_l=A_l^0(x)-yA_l^1(x),
\]

with

\[
\deg A_l^0\leq2D-p^{l-1},\qquad
\deg A_l^1\leq D-p^{l-1},\qquad
\deg h_{l-1}\leq p^{l-1}.
\tag{10}
\]

Every weight-gradient entry \(\mathbb E_m[r\delta_lh_{l-1}^\top]\) is therefore determined by the finite data statistics

\[
M_\alpha=\mathbb E_m[x^\alpha],\quad |\alpha|\leq2D,
\qquad
b_\alpha=\mathbb E_m[yx^\alpha],\quad |\alpha|\leq D.
\tag{11}
\]

The same bounds cover the output and bias gradients. The number of retained scalar data moments is at most

\[
\binom{d_x+2D}{2D}+\binom{d_x+D}{D}.
\tag{12}
\]

The statistic \(\mathbb E_m[y^2]\) does not affect the gradient, but it is required as one additional scalar whenever the original dynamics or temporal representation uses the residual-RMS clock \(\rho(t)^2=\mathbb E_m[(f_t(x)-y)^2]\). With that clock, retaining it is mandatory, not merely optional loss reporting: the other terms in rho squared use (11), while its final constant term is \(\mathbb E_m[y^2]\). Thus (12) becomes that displayed count plus one for the clocked representation. For several output coordinates, retain the corresponding target moment vector for each monomial and the required target second-moment statistic.

Expanding the network and its derivatives in monomials expresses its empirical gradient as a polynomial function of the trainable parameters and the fixed numbers (11). The resulting ODE is exactly the original empirical feature-learning ODE, initialized at the original dense W0. Its online data dependence is independent of m. This is exact finite sufficient-statistic closure, not frozen-feature training.

It also addresses sample-indexed temporal moments directly. Let \(P_k(s)\) be any prescribed scalar temporal basis function, including a Legendre basis on the relevant interval. Integrating \(h_{l-1}(s,x)P_k(s)\) in s leaves its degree in x at most \(p^{l-1}\). Integrating \(r(s,x,y)\delta_l(s,x)P_k(s)\) leaves the decomposition and degrees in (10) unchanged. Time integration acts only on finitely many scalar coefficient functions.

If q temporal coefficients per response are retained, their sample-indexed arrays can therefore be replaced by polynomial coefficient arrays. Writing
\(N(d,s)=\binom{d+s}{s}\), and assuming the hidden widths are at most n, an upper bound for their scalar storage is

\[
O\!\left(nq\sum_{l=1}^L
\left[N(d_x,p^{l-1})
+N(d_x,2D-p^{l-1})
+N(d_x,D-p^{l-1})\right]\right),
\tag{13}
\]

plus the fixed empirical moments (11) and whatever initialized-matrix storage was already present. The known input h0=x need not be stored as a response history, so this bound does not require input dimension at most n. Pairing these histories over the samples uses only monomial products:

\[
\mathbb E_m[x^\alpha x^\beta]=M_{\alpha+\beta},\qquad
\mathbb E_m[yx^\alpha x^\beta]=b_{\alpha+\beta}.
\]

The maximal required degrees are exactly 2D and D, respectively. This replacement is exact for every retained temporal coefficient; it does not improve or prove convergence in q. It removes the explicit m history slots from an existing temporal approximation while preserving that approximation's equations, provided all pointwise network operations and sample contractions are evaluated through the polynomial coefficients.

This is a mathematical construction, not a general efficient algorithm. For p>=2, D=p^L grows exponentially with depth. The counts in (12)-(13) and the associated polynomial multiplications can be enormous. They depend on input dimension, width, depth, and q even though they do not depend on m. A nonpolynomial smooth activation does not satisfy this exact degree bound. Replacing it by a polynomial changes the model; matching the original trajectory then requires an explicit uniform gradient error bound, including activation-derivative errors, followed by (8).

## 6. Why finite moments fail in a generic smooth model

An elementary smooth-network example separates polynomial moment closure from generic smoothness. Consider a scalar feature \(f_\theta(x)=e^{\theta x/2}\), target zero, and squared loss \(f_\theta(x)^2=e^{\theta x}\). Its gradient is \(x e^{\theta x}\).

For any integer Q>=0, take points \(x_j=1+j/(Q+1)\), j=0,...,Q+1, and signed multiplicities
\(c_j=(-1)^j\binom{Q+1}{j}\). The Q+1 finite difference of a degree-at-most-Q polynomial vanishes, so

\[
\sum_j c_jx_j^k=0\quad (0\leq k\leq Q).
\]

The positive and negative multiplicities each sum to \(2^Q\), hence define two uniform empirical datasets of equal size by replicating the corresponding points. Their moments through degree Q are identical. In contrast,

\[
\sum_jc_j e^{\theta x_j}
=e^\theta(1-e^{\theta/(Q+1)})^{Q+1}.
\]

For every \(\theta>0\), its derivative is nonzero: the absolute value is the product of two strictly positive, strictly increasing functions. Therefore the two datasets have different initial training velocities at the same \(\theta_0>0\). A simulator initialized only from those Q moments cannot reproduce both trajectories even locally.

This refutes the inference that arbitrary smooth activation has exact finite polynomial-moment closure. It is not a no-go theorem for the specific activation or initialization of an unspecified deeper canonical network, and it does not refute approximate compression.

A broader exact-statistic obstruction can be proved under regularity assumptions on encoding. Suppose a C1 statistic S of m distinct points x_a in (1,2), valued in \(\mathbb R^q\), determines \(\mathbb E_m[xe^{\theta x}]\) for all theta in [0,1] via a reconstruction whose derivative in S is continuous jointly in theta and S. Integrating from zero in theta, and using \(\mathbb E_m[e^{0x}]=1\), then reconstructs \(\mathbb E_m[e^{\theta x}]\) by a C1 function of S. Choose \(\theta_j=j/(m+1)\), j=1,...,m. The Jacobian of these m reconstructed values with respect to the m input points has entries
\(m^{-1}\theta_j e^{\theta_jx_a}\). After row and column scaling this is a Vandermonde matrix in the distinct numbers \(e^{x_a/(m+1)}\), and has rank m. Factoring the same map through S gives Jacobian rank at most q. Thus q>=m.

The assumptions matter: this is a lower bound for a regular exact sufficient statistic for the vector field on a parameter interval. It is not asserted for an arbitrary discontinuous real-number encoding, nor for every approximate trajectory model from one initial condition.

## 7. A constructive finite-horizon trajectory theorem independent of m

Here is a fully causal alternative that applies to smooth nonlinear feature learning and does not assume response closure.

Let z=(x,y) range over a bounded set Z in \(\mathbb R^{d_z}\), and let \(\ell(\theta,z)\geq0\) be C2 in the P trainable coordinates theta. Fixed positive learning-rate factors can be absorbed into a fixed linear rescaling of these coordinates; all norms and constants below are in those coordinates. Frozen initialized parameters remain fixed. Write

\[
F_z(\theta)=-\nabla_\theta\ell(\theta,z),\qquad
F_m(\theta)=\mathbb E_m[F_z(\theta)].
\]

Assume
\(B_0=\sup_{z\in Z}\ell(\theta_0,z)<\infty\), and fix T. Both the original empirical flow and any positive probability reweighting of data from Z remain in the radius
\(R=\sqrt{TB_0}\) ball around theta0. Indeed, for any such empirical measure nu,

\[
\int_0^t\|\dot\theta_\nu(s)\|^2ds
=L_\nu(\theta_0)-L_\nu(\theta_\nu(t))\leq B_0,
\]

and Cauchy–Schwarz bounds displacement by \(\sqrt{tB_0}\). Smoothness on a neighborhood of this compact ball also gives existence through T: a finite maximal time would have a bounded path and bounded locally Lipschitz vector field, which permits continuation.

Assume on that ball and all z in Z that

\[
\|F_z(\theta)-F_z(\theta')\|\leq\Lambda\|\theta-\theta'\|,
\qquad
\|F_z(\theta)-F_{z'}(\theta)\|\leq\Gamma\|z-z'\|.
\tag{14}
\]

Cover Z by K cells of diameter at most rho. In each occupied cell select one original sample z_j and assign it weight w_j equal to the fraction of samples in that cell. Define the fixed surrogate vector field

\[
\widetilde F(\theta)=\sum_{j=1}^K w_jF_{z_j}(\theta),
\qquad w_j>0,\quad\sum_jw_j=1.
\]

This weighted dataset is chosen using the initial dataset only. Pairing every sample with its cell representative and applying (14) gives, uniformly on the reachable ball,

\[
\|F_m(\theta)-\widetilde F(\theta)\|\leq\Gamma\rho.
\]

Start the autonomous weighted training flow from the same theta0. Applying (8) yields

\[
\sup_{0\leq t\leq T}\|\theta(t)-\widetilde\theta(t)\|
\leq\Gamma\rho\,\Psi_\Lambda(T),\qquad
\Psi_\Lambda(T)=
\begin{cases}(e^{\Lambda T}-1)/\Lambda,&\Lambda>0,\\T,&\Lambda=0.
\end{cases}
\tag{15}
\]

If Z is contained in a cube of side A, a grid gives for example
\(K\leq(1+\lceil A\sqrt{d_z}/\rho\rceil)^{d_z}\).
Taking \(\rho=\varepsilon/(\Gamma\Psi_\Lambda(T))\) supplies a size bound independent of m with all structural and regularity dependencies displayed. Empty cells are not stored. Cases \(\Gamma=0\) or \(B_0=0\) reduce directly to a single representative or a stationary flow.

The state has P trainable coordinates and at most K stored examples/weights. It is autonomous and restartable. Dense initialized matrices are retained exactly. Every layer is trained on the current nonlinear responses, so feature learning is preserved. The theorem compares the original full empirical trajectory, not a population trajectory. The original dataset is inspected during preprocessing, costing at least O(m) input access; subsequent dynamics use no original sample oracle. Producing all m individual predictions still costs at least the output size, while predictions at any requested input can be computed from the retained parameters.

This theorem is mathematically sample-count-independent, but it is not uniformly cheap in input dimension or network width. P is the original parameter count, the covering exponent is d_z, and B0, Lambda, Gamma may deteriorate with depth, width, W0, and horizon. Claiming a compact practical neural-state compression from (15) alone would hide these costs.

### An optimization formulation and a second construction

The fixed weighted-subset problem is naturally

\[
\min \#\operatorname{supp}(w)
\quad\text{subject to}\quad
w_a\geq0,\ \sum_aw_a=1,\quad
\sup_{\theta\in B_R}
\left\|\mathbb E_m F_z(\theta)-\sum_aw_aF_{z_a}(\theta)\right\|\leq\delta.
\tag{16}
\]

This is a genuine l0 support constraint in a dictionary of gradient *functions of theta*. It directly controls the defect needed in (15), rather than merely a snapshot response. Because the weights are probabilities, their l1 norm is exactly one for every feasible solution; l1 alone cannot distinguish supports in (16). An l2 penalty favors spread in simple duplicate-atom cases, not sparsity.

There is a deterministic construction even without data-space Lipschitz regularity. Choose an eta-net \(\theta_1,\ldots,\theta_J\) of B_R and form each sample's vector

\[
v_a=(F_{z_a}(\theta_1),\ldots,F_{z_a}(\theta_J))\in\mathbb R^{PJ}.
\]

The empirical mean of the v_a admits a positive convex representation using at most PJ+1 of them. A direct proof starts with the uniform weights: if more than PJ+1 weights are positive, the augmented vectors \((v_a,1)\) are linearly dependent. Move the weights along that dependence until at least one reaches zero, preserving nonnegativity, total mass, and the vector mean. Iterate until at most PJ+1 remain. Thus no external existence oracle is needed for this finite construction.

The resulting weighted subset matches F_m at every net point. At any theta, choose a net point within eta; the two Lipschitz deviations contribute at most \(2\Lambda\eta\). Equation (15) therefore holds with \(\Gamma\rho\) replaced by \(2\Lambda\eta\). A grid of the parameter ball gives finite J depending on P, R, and eta, but not m. This route may be exponentially expensive in P and its preprocessing evaluates the gradient at all J net points for all m samples. Those costs are part of the statement, not omitted implementation details.

## 8. Claim ledger and decisive remaining question

| Claim | Status | Main condition or limitation |
|---|---|---|
| Shared sample basis rewrites the hidden update as paired response coefficients | Exact | Full basis, or explicit residual (1) |
| Adaptive orthonormal l0/l1/l2 correspond to rank/nuclear/invariant energy | Proved | Columnwise coefficient costs and counted basis descriptions |
| Unweighted l2 guarantees a useful fixed harmonic cutoff | False | High-frequency one-mode counterexample |
| Nuclear response-update variation gives low-rank snapshots | Proved | Uniform V_T in the intended normalization |
| Nuclear control makes ordinary fixed-rank tangent flow accurate | False in general | Unit normal-direction counterexample |
| A small universally product-closed sample basis distinguishes arbitrary samples | False | Finite function-algebra argument |
| Polynomial activations admit exact finite empirical-moment training | Proved | Counts (12)-(13), no generic efficiency claim |
| The polynomial representation removes m temporal-history slots | Exact at each retained temporal order | Does not establish temporal-order convergence |
| Generic smoothness implies finite exact polynomial-moment closure | False | Smooth exponential-feature example |
| Uniform gradient quadrature produces a causal trajectory approximation | Proved | Bounded reachable region and explicit regularity constants |
| Positive fixed coresets can make retained data size independent of m | Proved under (14), or via a parameter net | Upfront complete-data processing; dimension dependence retained |
| l0/l1/l2 basis selection alone yields the desired efficient full-network generator | Open/unsupported | Missing causal defect bound and complexity audit |

The highest-leverage obligation for a practical shared-basis claim is to state and prove a bound of the form

\[
\|F_m(\widetilde\theta)-F_{\rm compressed}(\widetilde\theta,\text{retained state})\|
\leq\delta(K,T,\text{declared regularity}),
\]

or the appropriate integrated/increment analogue, with no future trajectory and no m-dependent hidden coefficients or online data oracle. Once this source bound and the state norm are specified, (8) gives the finite-horizon propagation argument. The polynomial construction and fixed coresets give two rigorous ways to close that obligation in narrower or expensive regimes. Snapshot basis optimality supplies neither the source estimate nor its computational provenance by itself.
