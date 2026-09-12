# Deterministic Gaussian-tree spectral route — frozen first-round report

This route produces a finite causal recurrence with initialization-derived coefficients, exact reuse of the initialized Gaussian action and its transpose in the coefficient algebra, explicit retained training history, and a finite joint observation representation. It does **not** establish an economical approximation through time 40. The missing bridge is quantitative approximation of the reachable nonlinear multiplication operators by the tree basis. A generic basis becomes expensive even before training, and force or temporal bounds alone do not repair that problem.

Status: independent first-round analysis; no simulations; not a convergence or feasibility claim. Scientific input was only the supervisor's self-contained assignment. Required process skills were read. No other study, book, code, history, or reviewer material was used. This report is frozen before cross-comparison.

## Contract and proposed distinction

The target is exactly the assigned two-hidden-layer population gradient flow on (H_i=L^2(\Omega_i)), with (w_0=g\sim N(0,I_2)), (c_0=K_0=0), (A=A_0+K), the assigned unhalved square loss, and (T=40). At finite width the initialized dense entries have variance (1/n), the stored output entries have variance (1/n^2), output normalization is (1/n), and the assigned mobilities are retained. The initialized action is never replaced by a fresh independent action when it is used backward.

The construction uses deterministic finite matrices representing multiplication of random variables, rather than particles or a fitted statistical closure. Their entries are evaluated by finite Gaussian contraction combinatorics. The trained correction is kept as a list of past rank-one sources. Its growing cost is counted. The construction therefore retains history explicitly; it does not assert an economical history compression.

The certification sought would concern a fixed sufficiently small law neighborhood of the assigned orthogonal opposite-label reference. The recurrence itself also makes sense for broader same-model laws. No law is selected as a function of requested accuracy. The quantitative neighborhood, source-tail constants, and temporal constants are not supplied in the assignment; none is invented here.

One explicit admissible family includes a fixed finite atomic part and a nonatomic angle density (p(\theta)), together with a first-label-moment density (m(\theta)), where (p,m) are finitely specified trigonometric polynomials, (p\geq0), and

\[
 |m(\theta)|\leq Yp(\theta),\qquad
 \sum_a \alpha_a+\int_0^{2\pi}p(\theta)d\theta=1.
\]

For (Y>0), realize the nonatomic component by labels (\pm Y) with densities ((p\pm m/Y)/2). A nonconstant (m/p) gives correlated input and label. A fixed small mixture of such a component with the reference is an example near the reference in mixture-sensitive topologies; membership in the assignment's unspecified neighborhood is an additional condition. For (Y=0), labels are zero. Only the marginal input measure and first-label-moment measure enter this flow, because its residual enters linearly in every update. Thus no conditional-label quadrature is needed.

## 1. An initialization algebra with fully available coefficients

Use two types of rooted expressions. Type 1 starts with (1,g_1,g_2); type 2 starts with (1). Permitted operations are real linear combinations, multiplication within a type, (A_0:1\to2), and (A_0^*:2\to1). A rooted expression contains finitely many operations. Fix nested finite syntax lists (B_i(L)) containing every expression up to a specified operation/degree budget (L). Repeated expressions and zero-norm combinations are removed by the Gram matrix. The particular budget convention affects cost, not the argument.

At finite width, interpret (g_k) as an iid Gaussian coordinate at each first-layer vertex, (A_{ij}=\xi_{ij}/\sqrt n), and all inner products as (n^{-1}\sum). The transpose is the actual transpose of this same matrix. Products are coordinatewise. Consequently each expression and each scalar inner product is a finite polynomial in the actual initialized Gaussian variables. This is a device for calculating limiting coefficients, not a finite neural-training procedure.

For any fixed expressions (X,Y,Z), the following limits are finite and explicitly computable:

\[
 \langle X,Y\rangle_i,\qquad
 \langle X,YZ\rangle_i,\qquad
 \langle X,A_0Y\rangle_2.
\]

Here and below an identification with the assigned population action means the action realizes these polynomial initialization limits. The finite-width coefficient statement itself does not require a nonlinear population-limit theorem.

**Proof of coefficient availability.** Expand an expression into rooted decorated graphs. An action contributes a bipartite edge and a factor (n^{-1/2}\xi_{ij}); a normalized average contributes (n^{-1}). Gaussian (g) factors decorate first-layer vertices. For a scalar product of (r) normalized averages, write (E) for the number of action edges. Partition vertex slots according to which first-layer and which second-layer indices coincide. If the partition leaves (v_1,v_2) distinct indices, the exact number of assignments is ((n)_{v_1}(n)_{v_2}), where ((n)_v=n(n-1)\cdots(n-v+1)).

For each partition, independence gives zero unless each distinct Gaussian matrix entry occurs an even number of times. Its contribution is its even Gaussian moment, multiplied by the even Gaussian moments of the (g) decorations at each first-layer vertex. These moments are integers: (E[G^{2k}]=(2k-1)!!), proved by integration by parts from the Gaussian density; odd moments vanish. For two coordinates use their independence. Thus each contribution is an explicitly known constant times

\[
 (n)_{v_1}(n)_{v_2}\,n^{-E/2-r}.
\]

There are at most (E/2) distinct matrix edges after a nonzero contraction. Every connected component comes from at least one of the (r) rooted averages, so its number (c\leq r). In each graph, vertices are at most distinct edges plus components. Therefore

\[
 v_1+v_2\leq E/2+r.
\]

Terms with strict inequality vanish; terms with equality converge to the calculated Gaussian-moment constant. Summing the finitely many partitions proves the assertion. The same argument handles any fixed product of scalar averages and hence supplies the moments needed to control their fluctuations.

For concentration of one normalized polynomial average, apply this expansion to its second moment. Leading partitions joining its two initially separate rooted components have at most one component, hence lose at least one power of (n). Leading partitions keeping the components separate factor into the two individual leading sums. Thus variance tends to zero. Linear combinations give joint convergence in probability of every finite list of these coefficients. This is concentration of polynomial observables, not a claim that arbitrary nonlinear laws are determined by their moments.

The actual finite initialization of the output can also be included: write its entries as (\eta_i/n), with fresh standard Gaussian (\eta_i), and add its decorations and explicit factors (n^{-1}) to the preceding expansion. Every term containing such an initial-output factor has the extra negative power; it contributes zero to a fixed limiting polynomial coefficient. This explains (c_0=0) in this coefficient calculation without resetting the finite output initialization. It does not independently prove capture of the finite nonlinear trajectory; capture is an assigned assumption.

After Gram quotienting and orthonormalizing, let (V_i(L)\subset H_i) be the finite expression spaces and (P_i) their orthogonal projections. All multiplication coefficients

\[
 T^{(i)}_{abc}=\langle e_a,e_be_c\rangle_i
\]

and the projected initialized action (A_L=P_2A_0|_{V_1}) are available by the calculation above. Singular Gram matrices are quotiented, rather than inverted. Before numerical rounding their entries are algebraic combinations of explicitly calculated integers. Numerical precision and conditioning are additional counted approximation parameters.

**A transpose check.** For any first-layer polynomial (h(g)),

\[
 \langle h,A_0^*A_0h\rangle_1
 =\langle A_0h,A_0h\rangle_2
 =E[h(g)^2].
\]

At finite width, conditional on (g), the coordinates of (A_0h) are independent centered Gaussians with variance (n^{-1}\sum_jh(g_j)^2). The displayed limit follows from the Gaussian second and fourth moments and the ordinary iid second-moment estimate. Replacing the backward action by an independent centered Gaussian action would give zero for the corresponding mixed contraction. Thus forward covariance matching alone misses an order-one return term. The proposed Gram algebra preserves this term and all its finite polynomial analogues.

## 2. Nonlinear coefficients without latent Gaussian quadrature

For (x\in V_i), form the real symmetric multiplication matrix

\[
 M_i(x)_{ab}=\langle e_a,xe_b\rangle_i.
\]

Let (\mathbf1_i\) be the coefficient vector of the constant function. Define finite coefficient vectors

\[
 S_i(x)=\tanh(M_i(x))\mathbf1_i,
 \qquad U_i(x)=\operatorname{sech}^2(M_i(x))\mathbf1_i.
\]

These are obtained by diagonalizing a finite real symmetric matrix and applying the scalar functions to its eigenvalues. All matrix entries come from the Gaussian contraction tensors and current coefficients. There is no expectation over a growing list of latent Gaussians hidden in this definition.

Define the projected product (B_i(x,y)=P_i(xy)) by the tensor (T^{(i)}). The matrices (M_i(x)) represent multiplication by a random variable, not hidden-neuron coupling parameters. (A_L) is fixed initialization data. No dense learned correction matrix is stored. Dense Gram and multiplication tensors can nevertheless be prohibitively large; renaming them does not eliminate that cost.

For every finite (L), these maps are defined at every real coefficient vector, and

\[
 \|S_i(x)\|_2\leq1,\qquad \|U_i(x)\|_2\leq1,
\]

because the matrix functions have operator norm at most one and (\|\mathbf1_i\|_2=1). They need not satisfy a pointwise range bound as functions on (\Omega_i). Nor is (U_i(x)) automatically the derivative of the finite map (S_i). The finite recurrence below is therefore an approximation of the specified equations, not a claimed exact gradient flow of a surrogate loss.

## 3. Complete causal recurrence and restart

Partition the angle circle into (J) intervals, retaining any atoms separately, and choose representative inputs (u_j). Set

\[
 a_j=\mu_\theta(I_j),\qquad b_j=\int_{I_j}y\,d\mu.
\]

For the explicit law family above these weights use only integrals of trigonometric polynomials and finite sums, with elementary antiderivatives. They obey (a_j\geq0), (\sum_ja_j=1), and ( |b_j|\leq Ya_j). Refinement changes the numerical representation of one fixed law. General computable same-model laws can be supplied with certified one-dimensional weight routines; no general oracle for arbitrary measures is assumed.

Fix (N), (h=40/N), (L), and numerical precision. The state at step (m) consists of two first-layer vectors (w_{m,1},w_{m,2}\in V_1), a second-layer vector (c_m\in V_2), and the full list

\[
 \mathcal H_m=\{(\beta_{\ell j},d_{\ell j},h_{\ell j}):0\leq\ell<m,\ 1\leq j\leq J\}.
\]

Initialize (w_{0,k}=g_k), (c_0=0), and the list empty. Each list entry acts as the operator (\beta d\otimes h:x\mapsto\beta d\langle h,x\rangle_1). To advance, evaluate synchronously from the old state:

\[
\begin{aligned}
 x_j&=w_m\cdot u_j,& H_j&=S_1(x_j),& R_j&=U_1(x_j),\\
 Z_j&=A_LH_j+\sum_{(\beta,d,h')\in\mathcal H_m}
       \beta d\langle h',H_j\rangle_1,\\
 V_j&=S_2(Z_j),& f_j&=\langle c_m,V_j\rangle_2,&
 D_j&=B_2(c_m,U_2(Z_j)),\\
 Q_j&=A_L^*D_j+\sum_{(\beta,d,h')\in\mathcal H_m}
       \beta h'\langle d,D_j\rangle_2,&
 \rho_j&=a_jf_j-b_j.
\end{aligned}
\]

Then set

\[
\begin{aligned}
 c_{m+1}&=c_m-2h\sum_j\rho_j V_j,\\
 w_{m+1,k}&=w_{m,k}-2h\sum_j\rho_j u_{j,k}B_1(R_j,Q_j),\quad k=1,2,
\end{aligned}
\]

and append ((-2h\rho_j,D_j,H_j)) for every (j). This is exactly the Euler update of the rank-one source in the specified (K) equation after the displayed finite approximations. In particular, its transpose uses the same retained source factors in reverse order. The normalizations and factor 2 agree with the assigned model.

Every step requires finitely many algebraic operations and finite matrix functions and returns finite real coefficients. Induction proves that the recurrence is defined for every finite (N). This does not imply numerical stability at a prescribed step size. For example, its elementary bound

\[
 \|c_m\|_2\leq Y((1+2h)^m-1)\leq Y(e^{2t_m}-1)
\]

follows from ( |f_j|\leq\|c_m\|_2) and (\|V_j\|_2\leq1), and is far too large to justify practical time-40 accuracy.

A checkpoint must retain the current coefficients, complete list, current time, basis description and Gram quotient, law weights, and precision. This state determines the continuation, including the frozen action and its adjoint. Keeping only (w,c), or only forward covariances, is not a restart. The list length is at most (NJ). It is finite because the requested horizon and discretization are finite; it is not asserted to remain bounded under refinement.

At an arbitrary probe input (u), repeat the same finite forward/backward evaluation using the saved state. The prediction is (\widehat f_m(u)=\langle c_m,S_2(Z_m(u))\rangle_2). Saved past times needed for an observation contract require saving their coefficient vectors or re-evolving the finite recurrence from a checkpoint. A future trajectory is never part of the initial data.

## 4. A genuine finite joint observation representation

A covariance-only contract would miss the problem's requested mechanism. For any fixed finite set of probe inputs and times, form coefficient vectors for the following variables at a common neuron:

* First layer: (g,w_t,H_0(u),H_t(u),Q_t(u),U_1(w_t\cdot u)Q_t(u)), with products interpreted through (B_1).
* Second layer: (Z_0(u),Z_t(u),V_0(u),V_t(u),c_t,D_t(u)).

These lists include paired initialized/current variables and same-layer forward/backward joint information. In addition report link contractions such as (\langle D_t,A_LH_s\rangle_2=\langle A_L^*D_t,H_s\rangle_1), and their history-corrected counterparts. There is no asserted canonical joint random neuron obtained by pairing an arbitrary index in layer 1 with an arbitrary index in layer 2.

For a list (X_1,\ldots,X_r\in V_i), diagonalize each symmetric matrix (M_i(X_j)). Write its spectral values and orthogonal projectors as (\lambda_{jk},E_{jk}). The following finite probability law is explicit:

\[
 \nu_{i,L}\{(\lambda_{1k_1},\ldots,\lambda_{rk_r})\}
 =\|E_{rk_r}\cdots E_{1k_1}\mathbf1_i\|_2^2.
\]

It is nonnegative. Summing over (k_r) preserves the squared norm because mutually orthogonal projectors sum to the identity; repeat for all coordinates to obtain total mass one. Thus this is an actual finite joint law, rather than a possibly non-positive multivariate matrix-exponential formula. The coordinate order is fixed and is part of the observation definition. Finite compressed multiplication matrices need not commute, so changing the order can change this law. That discrepancy is another approximation effect requiring convergence proof.

The law need not be enumerated. For a joint characteristic function, start with (\varrho_0=\mathbf1_i\mathbf1_i^T) and recursively compute

\[
 \varrho_j=\sum_k e^{iq_j\lambda_{jk}}E_{jk}\varrho_{j-1}E_{jk};
 \qquad \widehat\chi(q)=\operatorname{tr}\varrho_r.
\]

This formula evaluates the characteristic function of the displayed positive law by finite matrix operations. In each eigencoordinate basis the map deletes off-block entries and applies the scalar phase to each block; dense implementations cost order (r m_i^3) after eigendecomposition. Degenerate eigenspaces are retained as whole projectors, making the definition independent of an arbitrary eigenbasis. Arbitrary black-box joint test functions can require up to (m_i^r) atom evaluations; that cost is explicit and is not hidden as an expectation or quadrature routine.

A prospective convergence contract is weak convergence of these laws, uniformly on the stipulated compact time set and controlled probe/test class, together with uniform prediction error and any named mixed moments for which uniform integrability is established. The finite construction supplies the observation maps. It has not proved that prospective contract.

## 5. The precise spectral bridge

The following elementary conditional result explains why the construction is more than a formal moment replacement.

**Conditional multiplication theorem.** Let (x) be a real random variable on a fixed probability space. Multiplication (M_x\psi=x\psi) has its maximal domain (D(M_x)=\{\psi:x\psi\in L^2\}). Let (V_L\) be nested finite-dimensional subspaces containing (1), with union dense in (L^2). Assume the union is a core for (M_x): it is dense in the norm (\|\psi\|_2+\|x\psi\|_2). Let (M_L=P_LM_xP_L), extended as zero on (V_L^\perp). Then

\[
 \tanh(M_L)1\longrightarrow\tanh(x),\qquad
 \operatorname{sech}^2(M_L)1\longrightarrow\operatorname{sech}^2(x)
\]

in (L^2). For finitely many multiplication variables satisfying a common-core condition, their ordered spectral joint laws converge weakly to their ordinary joint law, provided the finite variables also converge on that core as described below.

**Proof of the resolvent step.** Multiplication by real (x) is self-adjoint on its maximal domain: solving ((M_x-i)\psi=\eta) gives (\psi=\eta/(x-i)), for which both (\psi) and (x\psi) are square integrable. The inverse has norm at most one. The same bound holds for each real symmetric (M_L). For (\psi) in the union, eventually (P_L\psi=\psi), and

\[
 (M_L-i)\psi=P_L(x\psi)-i\psi\longrightarrow (M_x-i)\psi.
\]

Consequently the resolvents converge on the dense set of vectors ((M_x-i)\psi) with (\psi) in the core. Their uniform norm bound extends convergence to every vector. The same proof works at every nonreal spectral parameter.

For completeness, a useful explicit rational expansion is

\[
 \tanh z=2z\sum_{k=1}^{\infty}
       \frac1{\pi^2(k-1/2)^2+z^2},\qquad z\in\mathbb R.
\]

One way to derive it is to solve (-v''+z^2v=0) on ((0,1)) with (v(0)=0,v'(1)=1), giving (v(1)=\tanh(z)/z), interpreted continuously at zero. Expand in the orthonormal functions (\sqrt2\sin(\pi(k-1/2)s)). Integration by parts against each function gives coefficient (\sqrt2(-1)^{k-1}/(\pi^2(k-1/2)^2+z^2)). These coefficients have summable absolute values; evaluating their sine series at 1 gives the formula. Completeness of this sine family follows by odd extension at 0 and even extension at 1 to the ordinary Fourier basis.

The tail after (K) terms is bounded in absolute value by

\[
 2|z|\sum_{k>K}\frac1{\pi^2(k-1/2)^2}
 \leq \frac{2|z|}{\pi^2(K-1/2)}.
\]

Resolvent convergence gives convergence of each finite rational sum. Also (\|M_L1\|_2=\|P_Lx\|_2\leq\|x\|_2), so the displayed tail is uniformly small when applied to (1). This proves the tanh assertion. The same argument first proves strong convergence on any vector in the common core, then on all vectors using the uniform operator bound (\|\tanh(M_L)\|\leq1). Squaring strongly convergent uniformly bounded operators proves the sech-squared assertion.

For spectral projections onto intervals whose boundaries have zero spectral mass at the vectors under consideration, approximate their indicators above and below by bounded continuous functions, use resolvent approximation and the boundary-mass condition, and obtain strong projection convergence. Products of finitely many uniformly bounded strongly convergent projectors also converge strongly, by telescoping the product. The limiting multiplication projections commute, and

\[
 \|1_{X_r\in I_r}\cdots1_{X_1\in I_1}1\|_2^2
 =P(X_1\in I_1,\ldots,X_r\in I_r).
\]

Approximate joint bounded continuous tests by step functions on a sufficiently large compact cube and choose continuity boundaries; probability outside the cube is controlled by the convergent marginal projections. This proves weak convergence of the ordered joint laws. It does not assert a uniform quantitative rate.

If (x_L\) itself varies with the approximation, a sufficient replacement assumption is

\[
 \|(x_L-x)\psi\|_2\to0
 \quad\text{for every }\psi\text{ in a common core}.
\]

Together with core approximation, this gives the same resolvent proof. Plain (L^2) convergence of (x_L) is not enough to imply this weighted multiplication convergence. This distinction matters directly for trained preactivations and backward products.

**A sufficient Gaussian-core criterion.** If all variables under consideration are polynomials in finitely many *available* independent Gaussian primitives and the basis includes all polynomials in those primitives, it is a core for multiplication by each such variable. Indeed, for a polynomial (p), polynomials are dense in (L^2((1+p^2)d\gamma)). To prove density, let (f) be orthogonal to them. Cauchy–Schwarz and Gaussian exponential integrability show that

\[
 F(z)=\int f(s)(1+p(s)^2)e^{z\cdot s}\,d\gamma(s)
\]

is an entire function of the finite-dimensional complex vector (z), with differentiation under the integral justified on every compact set by the same integrable bound. All its derivatives at zero vanish. Its power series, obtained by dominated expansion of the exponential on compact (z)-sets, is therefore zero. The Fourier transform of the finite signed measure (f(1+p^2)d\gamma) vanishes. Convolution with a Gaussian then vanishes by Fourier inversion for its integrable smooth convolution; as the Gaussian kernels form an approximate identity, the signed measure is zero. Thus (f=0), proving density and the criterion.

This criterion does **not** establish that a small tree basis exposes all Gaussian primitives generated by repeated adaptive forward and transpose actions. Deriving such primitives, proving that they lie in the accessible completed algebra, and bounding their number and chaos degree is a missing bridge. The finite polynomial Wick calculation alone does not settle it: high-degree polynomial Gaussian variables can fail the elementary moment-determinacy criteria, so replacing this issue by an unproved method-of-moments assertion would be invalid.

## 6. Generation is separate from propagation

The assumptions of unique population flow, finite-flow capture, and force-controlled source and temporal estimates identify the target and can help propagate a specified error. They do not, as stated, bound the error **generated** by this basis.

For a projection-based comparison with the exact flow, the missing source bounds include at least:

\[
\begin{aligned}
 &\|(I-P_i)\,\hbox{reachable state/source}\|_2,\\
 &\|S_i(P_ix)-P_i\tanh(x)\|_2,
 \quad\|U_i(P_ix)-P_i\operatorname{sech}^2(x)\|_2,\\
 &\|B_i(P_ix,P_iy)-P_i(xy)\|_2,\\
 &\|P_2A_0(I-P_1)H\|_2,
 \quad\|P_1A_0^*(I-P_2)D\|_2,
\end{aligned}
\]

and the analogous errors in the stored history sources. All are along reachable states and uniformly over the fixed law class. A norm bound on a source is not a small bound on its omitted tree modes.

If, in an appropriate state/history norm, these sources give a computable one-step defect (h\eta_L+h\eta_J+Ch^2), and the propagation estimate gives

\[
 e_{m+1}\leq(1+h\Lambda_m)e_m
       +h(\eta_L+\eta_J)+Ch^2,
\]

then iteration proves

\[
 e_N\leq
 \exp\!\Big(\sum_mh\Lambda_m\Big)
 \{e_0+40(\eta_L+\eta_J+Ch)\}.
\]

The proof is multiplication of the recurrence by the inverse accumulated products, summation, and (1+x\leq e^x) for nonnegative (x). This is a conditional propagation statement. It provides no estimate of (\eta_L), no useful value of (L), and no license to identify the finite recurrence with the population flow.

For the one-dimensional law approximation, if its exact relevant integrands are Lipschitz with constant (C_t) in angle, moving each interval's input to its representative gives error at most its mesh width times (C_t); this follows by integrating the pointwise Lipschitz bound against the input measure and the signed first-label-moment measure, whose variation is bounded by (Y\mu_\theta). The assignment's temporal/source assumptions may help bound (C_t), but no numerical bound through 40 was supplied.

The exact population energy identity, whenever the assigned differentiations are justified, is

\[
 \frac d{dt}\int(f-y)^2d\mu
 =-\|\dot c\|_2^2-\|\dot w\|_2^2-\|\dot K\|_{HS}^2.
\]

It follows by differentiating the loss and substituting each of the three given negative-gradient equations. Since the initial loss is at most (Y^2), Cauchy–Schwarz bounds total state-space path length up to (T) by (Y\sqrt T). This does not bound the tree degree of that path. Small displacement can lie in an arbitrarily high orthogonal mode; energy control alone is not a spectral source theorem.

## 7. Total cost and time-40 feasibility

Let (m=\max(\dim V_1,\dim V_2)). A direct implementation stores order (m^3) multiplication coefficients, order (m^2) Gram/action coefficients, and order (NJm) history coordinates. An orthonormal basis may make the initially combinatorial tensors dense. Sparse formats can improve these upper bounds only if their sparsity survives the chosen basis and updates.

At step (\ell), direct source-list application costs order (\ell J^2m); multiplication tensor contractions and matrix functions cost order (Jm^3). Total evolution cost is therefore bounded at the direct-implementation level by

\[
 O(NJm^3+N^2J^2m),\qquad
 \text{memory }O(m^3+NJm).
\]

This excludes coefficient construction, which is itself substantial. For expression size (O(L)), direct set-partition/Gaussian-contraction enumeration has a bound of the form ((CL)^{CL}) per coefficient. There are order (m^3) multiplication coefficients. This is an explicit combinatorial calculation, not a claim of polynomial preprocessing cost. Graph memoization and symmetry reduction are possible unproved improvements.

As an arithmetic illustration only, (N=4000,J=64,m=100) yields approximately (2.56\times10^{11}) operations in the first evolution term and (6.55\times10^{12}) in the history term. The two history-factor arrays alone require roughly 410 MB at eight bytes per coefficient. No accuracy is claimed for those values. Raising (m) to 1000 multiplies the cubic term by 1000. The generic construction currently offers no certified choice of (m,N,J) delivering useful accuracy through 40.

There is already a dimensional warning at initialization. Choose (q) linearly independent first-layer polynomials and orthonormalize them in Gaussian (L^2\). Their (q) forward images under the actual initialized matrix have a limiting row law of (q) independent standard Gaussians. To verify this, condition on first-layer Gaussian samples: the row law is exactly Gaussian with the empirical source Gram covariance, and this covariance converges entrywise by the finite iid moment bound. Different rows are conditionally independent. Gaussian characteristic functions then identify the limit directly, without a moment-determinacy assumption.

A basis containing all degree-at-most-(p) polynomials in these (q) independent Gaussian coordinates has dimension

\[
 \binom{q+p}{p}.
\]

Independence of the monomials follows because a polynomial zero in Gaussian (L^2) vanishes almost everywhere under a strictly positive density and hence is the zero polynomial. For example, (q=15,p=6) gives 54,264 coordinates. Dense multiplication tensors at that size are out of scope for an economical method. This attacks the generic tensor basis, not all reachable-state bases: the actual flow might need a much smaller structured subspace, but that is precisely the unproved compression claim. The assigned force estimates do not establish it.

## 8. Hostile audit and frozen claim ledger

| Claim or attack | Status and consequence |
|---|---|
| Every fixed polynomial coefficient is obtained from actual dense Gaussian initialization | Proved by the finite graph expansion; no fitted coefficient or future trajectory. |
| The initialized transpose can be replaced by an independent backward Gaussian map | False even for the displayed (A_0^*A_0h) contraction. The candidate does not make that substitution. |
| Finite recurrence, prediction, and full-history restart are specified | Proved as a finite construction. No numerical stability or target convergence is implied. |
| Nonlinear coefficients hide high-dimensional Gaussian quadrature | Avoided: finite symmetric matrix functions are the operations. Their matrix sizes and cubic costs are counted. |
| Joint observations are merely marginal covariance data | Avoided by the explicit positive ordered spectral law and link contractions. Finite-order dependence and its convergence remain visible. |
| A common multiplication core gives spectral and joint-law convergence for fixed variables | Proved conditionally above, with the needed weighted convergence condition stated for varying variables. |
| The available adaptive tree algebra is a sufficiently small common core throughout training | Open and major. Gaussian moments do not prove this. |
| Force/energy bounds provide the missing spectral approximation rate | Unsupported. They control size/path length, not generated tree or chaos degree. |
| Generic Galerkin plus source-history storage is already practical through 40 | Unsupported and disfavored by the explicit cost. This witness has no demonstrated useful accuracy/cost pair. |
| Failure of this witness disproves an economical deterministic representation | Not claimed; no broader impossibility follows. |

Additional failure modes are Gram ill-conditioning; loss of pointwise bounds after projection; high-to-low feedback through products and (A_0^*); fixed-basis spectral approximation of changing variables; long-history accumulation; absence of a uniform law-neighborhood rate; and the noncommutation of finite multiplication matrices. A practical implementation must control all of these, not only time-step refinement.

The highest-leverage next theoretical obligation for this route is a constructive, quantitative reachable-subspace theorem: from initialization and the law alone, expose a small family of Gaussian/tree coordinates forming a common multiplication core to the required tolerance, bound the discarded source in the weighted norms above by an explicit function of accumulated force, and count both coordinate generation and retained history. Without such a theorem, this route is an honest finite spectral construction and a possible testing framework, but it does not meet the requested economical time-40 milestone.
