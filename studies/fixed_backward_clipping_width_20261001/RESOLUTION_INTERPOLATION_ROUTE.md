# Interpolation resolution attempt: exact tree cancellation and the unsummed nonlinear response

2026-10-01. Scoped theoretical continuation. **The actual all-time root-width bias remains open in this attempt.** There is no counterexample to the specified neural flow here. The new positive result is an inverse-free, uniform \(O(n^{-1})\) comparison for every fixed polynomial matrix-action program under the block variance interpolation. Its proof identifies precisely which tree contributions cancel. The new negative result is an explicit counterexample to obtaining the interpolation estimate from stochastic row sums, permutation symmetry, and initialization Lipschitz bounds alone. Hard clipping leaves a further obstruction to replacing the whole trajectory by its small-label Taylor series.

The complete assigned inputs were FITTING_AND_THRESHOLD.md, CONCENTRATION_ROUTE.md, CLIPPED_POPULATION_ROUTE.md, and BIAS_DIMENSION_ROUTE.md. The rigorous-math and conjecture-investigation skills and their relevant contract, evidence, proof-search, and audit references were read. No other study, new sibling report, experiment, code, paper edit, or Git operation was used. The only written artifact is this report. All new calculations below are contained proofs; no external theorem is imported.

## 1. Contract and the remaining implication

The target retains the actual order-one, two-hidden-layer tanh system, recursive post-gate hard clipping at \(M=1\), independent canonical Gaussian \(A_0,W_0\), the true reused transpose, zero readout and value initialization, fixed finite training data with a positive initial population readout-Gram gap, and sufficiently small but fixed positive label RMS \(Y\). The reference is the own clipped population flow already identified in the assigned population input. Queries range over a fixed bounded set, with the supremum in physical time inside the query integral when a test law is used. The probabilistic target is conditional on the good initialization event, followed by the existing high-probability transfer. Bad-initialization all-time moments are a separate question.

Write \(N=2n\), and let \(s_i,t_j\) be balanced signs on the two physical layers. The interpolation is

\[
 W_{ij}^{\theta}\text{ independent},\qquad
 W_{ij}^{\theta}\sim N(0,S_{ij}^{\theta}),\qquad
 S_{ij}^{\theta}=\frac{1+\theta s_it_j}{N},\quad 0\le\theta\le1.
 \tag{1}
\]

It obeys

\[
 \sum_jS_{ij}^{\theta}=\sum_iS_{ij}^{\theta}=1,
 \qquad 0\le S_{ij}^{\theta}\le 2/N.
 \tag{2}
\]

The endpoints are the fully connected width-\(N\) initialization and two independent width-\(n\) diagonal blocks. All matrix calls retain the same matrix and its transpose. The joining lemma in the assigned bias input already compares the block endpoint with two separate width-\(n\) flows in expected all-time error \(O(n^{-1/2})\).

Let \(a_N^{\rm ext}(t,x,A_0,W)\) be the bounded prediction-velocity extension from that input. The outstanding bridge is

\[
 \sup_{T\ge0}\left|
 \int_0^T
 \bigl(\mathbb E a_N^{\rm ext}(t,x,A_0,W^1)
       -\mathbb E a_N^{\rm ext}(t,x,A_0,W^0)\bigr)\,dt
 \right|\le C_xN^{-1/2}.
 \tag{3}
\]

The counting argument below proves the corresponding mean comparison for a fixed polynomial program, but not (3). The hard-clip discussion explains why a formal expansion cannot be silently identified with the exact velocity.

## 2. Exact cancellation for variance-weighted trees

Consider any \(N\times N\) nonnegative matrix \(S\) satisfying (2). A finite bipartite graph has row-type vertices and column-type vertices; an edge joins opposite types. Parallel edges are allowed. For a graph \(H\) with \(v\) vertices, \(e\) edges, and \(c\) connected components, put

\[
 Z_H(S)=\sum_{\ell:V(H)\to[N]}
                  \prod_{(u,v)\in E(H)}S_{\ell(u),\ell(v)}.
 \tag{4}
\]

Row and column labels belong to different index sets. Distinct vertices of the same type may receive the same label in (4).

**Tree identity.** If \(H\) is a forest, then \(Z_H(S)=N^c\).

For each component choose a root. Sum the label of a leaf first. If its parent is row-type, the relevant sum is a row sum of \(S\), equal to one; if the parent is column-type, it is a column sum, also one. Remove the leaf and repeat. The last root label contributes \(N\). Multiplication over components proves the identity, including isolated vertices.

**Collision estimate.** If \(H\) is a forest, imposing distinct labels on every pair of vertices of the same type changes \(N^{-c}Z_H(S)\) by at most \(v(v-1)/N\).

Choose each root uniformly on \([N]\), independently across components, and sample each child from the transition probabilities \(S\) or \(S^T\) specified by its parent type. The probability of a labeling is exactly \(N^{-c}\prod_ES\). Every vertex is uniform, because both transition matrices preserve the uniform law. Vertices in different components collide with probability \(1/N\). For two distinct vertices of the same type in one component, orient the tree at the first vertex. The conditional transition to the second is a positive-length product of \(S,S^T\). Every entry of such a product is at most \(2/N\): multiplication on the right by a doubly stochastic matrix preserves this entrywise bound. Their collision probability is therefore at most \(2/N\). A union bound over at most \(v(v-1)/2\) pairs proves the claim. Re-rooting is legitimate because the root is uniform and reversing an edge replaces \(S\) by \(S^T\), leaving the labeling weight unchanged.

**Cycle estimate.** For general \(H\), let \(R=e-v+c\ge0\) be its number of edges outside a spanning forest. Then

\[
 Z_H(S)\le N^c(2/N)^R.
 \tag{5}
\]

Choose a spanning forest, bound every remaining edge weight by \(2/N\), and sum the forest weights with the tree identity. This also bounds the sum restricted to injective labelings. All three statements are uniform in \(\theta\), including \(\theta=1\).

## 3. Fixed polynomial matrix-action programs

A polynomial matrix-action program here means a fixed finite expression built from:

- iid first-layer row roots with moments of every required finite order, independent of \(W\);
- deterministic coordinatewise polynomials and deterministic linear combinations;
- repeated actions of \(W\) and its actual transpose;
- normalized empirical averages and pairings, using \(1/N\);
- products of the resulting scalar contractions.

Its coefficients and instruction list are independent of \(N,\theta\). Independent roots on the second layer could also be included. This class does not allow reading individual matrix entries as a separate coordinatewise array.

**Proposition.** For every scalar program \(P_N\) in this class there is a finite, explicitly computable constant \(\mathfrak C(P)\), depending on its expression and root moments but not on \(N,\theta,\eta\), such that

\[
 \sup_{\theta,\eta\in[0,1]}
 \left|\mathbb EP_N(A_0,W^\theta)
       -\mathbb EP_N(A_0,W^\eta)\right|
 \le \mathfrak C(P)/N.
 \tag{6}
\]

Here is the counting proof. Expanding the finitely many polynomials gives a finite sum of terms

\[
 N^{-c_0}\sum_{\ell:V(H_0)\to[N]}
 \left(\prod_{e\in E(H_0)}W_{\ell(e)}\right)
 \left(\prod_{v\in V(H_0)}q_v(\xi_{\ell(v)})\right),
 \tag{7}
\]

where \(H_0\) is bipartite with \(c_0\) components and \(q_v\) is a fixed root polynomial, possibly one. A coordinatewise product joins expression trees at their common output vertex; a matrix action adds an edge and sums the previous output index; an empirical average closes the remaining root and contributes \(1/N\). Products of scalar averages give disjoint unions. Repeating these operations constructs (7). Matrix reuse has introduced no independence assumption.

If the number \(L\) of matrix occurrences is odd, their Gaussian expectation is zero. For even \(L\), repeated Gaussian integration by parts gives the pairing formula: sum over pairings of the \(L\) occurrences, identify both endpoints of each paired pair, and replace the pair by its variance \(S_{ij}\). For completeness, integration by parts in one Gaussian coordinate replaces one occurrence by its variance times the derivative of the remaining product; that derivative chooses each possible partner once. Induction on \(L\) gives the formula, including repeated entries and their pairing multiplicities.

For each pairing, let \(H_1\) be the quotient multigraph. It has \(e=L/2\) variance edges and at most \(c_0\) components. Partition its row vertices and column vertices according to which labels coincide. After identifying each partition block, sum only over injective labels on the resulting graph \(H\). The expected root decoration is a constant \(\mu_H\): roots at different labels are independent, and decorations at an identified vertex are multiplied before expectation. This constant is finite by the assumed polynomial root moments. There are finitely many partitions, independently of \(N\).

Let \(v,c,R=e-v+c\) be the parameters of \(H\). Identifications cannot increase the number of components, so \(c\le c_0\). Equation (5) bounds its contribution, excluding fixed coefficients and \(\mu_H\), by

\[
 N^{-c_0}N^c(2/N)^R
   =2^R N^{c-c_0-R}.
 \tag{8}
\]

If \(c<c_0\) or \(R\ge1\), this is at most \(2^R/N\). If \(c=c_0\) and \(R=0\), the graph is a forest with all original components retained. The tree identity and collision estimate give its normalized contribution as

\[
 \mu_H+\varepsilon_H(S),\qquad
 |\varepsilon_H(S)|\le |\mu_H|v(v-1)/N.
 \tag{9}
\]

The only order-one contributions are therefore the profile-independent forest constants \(\mu_H\). Every other contribution and every injectivity correction is \(O(1/N)\). Sum (8)–(9) over the finite monomials, pairings, and partitions, and double the resulting error constant to compare two profiles. This defines an explicit admissible \(\mathfrak C(P)\) and proves (6).

The result permits arbitrary finite reuse of the transpose and never inverts a history Gram. It closes a finite-program version of the signed cancellation. It does not give constants uniform in program length or polynomial degree.

## 4. A precise approximation estimate that would complete the route

Suppose that for every \(0<\varepsilon<1\) there is a polynomial matrix-action program \(P_{N,\varepsilon}(t,x)\), with deterministic time-dependent coefficients, such that

\[
 \sup_{\theta\in[0,1]}\int_0^\infty
 \mathbb E\left|a_N^{\rm ext}(t,x,A_0,W^\theta)
                   -P_{N,\varepsilon}(t,x)\right|dt
 \le C_x\varepsilon,
 \tag{10}
\]

and the explicit counting constants from the preceding proof obey

\[
 \int_0^\infty\mathfrak C(P_{\varepsilon}(t,x))dt
 \le C_x\varepsilon^{-1}.
 \tag{11}
\]

Measurability and integrability are part of this sufficient condition. The programs must approximate the actual extension, or the actual flow on profile-uniform good events with a controlled complement, rather than a different surrogate.

The triangle inequality and (6) bound the integral of the absolute endpoint mean-velocity difference by

\[
 2C_x\varepsilon+\frac{C_x}{N\varepsilon}.
 \tag{12}
\]

Taking \(\varepsilon=N^{-1/2}\) proves (3). The existing joining estimate and dyadic telescoping then give the own-population bias. If the constants are uniform on the prescribed bounded query set, Minkowski's inequality gives the query \(L^2\) bias. Combining it with the supplied conditional centered-fluctuation estimate yields the conditional root-mean-square bound for the entire time path; adding \(\Pr(\mathcal G_n^c)=O(n^{-1})\) yields the high-probability transfer.

Neither (10) with this quantitative cost nor (11) is proved here. Fixed-tolerance polynomial approximation would give only an unspecified finite \(\mathfrak C(P_\varepsilon)\). Letting \(N\to\infty\) first and then \(\varepsilon\to0\) would give qualitative convergence but no root-width rate. More generally a proved cost \(C\varepsilon^{-p}\) would give \(N^{-1/(p+1)}\) by the same optimization.

Small activity alone does not establish (11). The absolute counting bound includes all Gaussian pairings, whose number for \(2k\) occurrences is \((2k-1)!!\), as well as index partitions and root moments. A geometric factor \(q^k\), with fixed \(q>0\), does not by itself bound \(q^k(2k-1)!!\). This diagnoses the present absolute-sum estimate; it does not prove that a sharper expansion with cancellations cannot converge. An adequate response norm must exploit such cancellations or sum nonlinear node functions before taking absolute values.

There is a further distinction between small state motion and small response. Normalizing \(w\) by \(Y\) gives hidden displacement \(O(Y^2)\), but the supplied deterministic tube does not give an \(O(Y)\) Lipschitz constant for the lower gate with respect to its preactivation. To check this exactly, fix \(a\ne0\) and \(0<\delta<1\). On a subset of \(k\) coordinates take

\[
 \alpha_j=a,\qquad
 p_j=(1-\delta)/\operatorname{sech}^2a,
\]

and put \(p_j=0\) elsewhere. Choosing \(k/N\le Y^2\operatorname{sech}^4a\) makes \(\|p\|_2/\sqrt N\le Y\). For an infinitesimal preactivation change supported on this subset, all active arguments remain strictly unsaturated and

\[
 \frac{\|\Delta C_1(p\operatorname{sech}^2\alpha)\|_2}
      {\|\Delta\alpha\|_2}
 \longrightarrow 2(1-\delta)|\tanh a|.
\]

This ratio is independent of \(Y\). It refutes only an improved deterministic Lipschitz estimate on the whole stated RMS tube; it is not an assertion that these arrays are reached by the actual Gaussian flow. Multiplication by the residual and integration of activity therefore supply an \(O(Y)\), rather than automatically \(O(Y^2)\), coefficient for this part of a deterministic iteration. A contraction for sufficiently small \(Y\) may still be possible. But even a proved contraction in the state norm would not be a contraction in the explicit graph-error norm \(\mathfrak C\). Obtaining geometric loop-defect constants per genuine forward/transpose feedback cycle requires a new response estimate. The report contains no such estimate and does not infer it from \(h-h_0=O(Y^2)\).

## 5. Symmetry and regularity alone are insufficient

Define

\[
 H_N(W)=N^{-3/2}\sum_{i,j}|W_{ij}|,\qquad
 \widetilde H_N(W)=\min\{H_N(W),2\}.
 \tag{13}
\]

Both are invariant under independent permutations of the two physical layers. Cauchy–Schwarz and the singular-value bound give

\[
 |H_N(W)-H_N(V)|
 \le N^{-1/2}\|W-V\|_F
 \le\|W-V\|_{\rm op}.
 \tag{14}
\]

The capped observable is thus bounded and operator-Lipschitz with constant one. At \(W=G/\sqrt N\), it is Lipschitz in the standard Gaussian roots with constant \(1/N\). These bounds are stronger than the corresponding generic regularity used for prediction velocity.

Nevertheless direct Gaussian integration gives, with \(c=\sqrt{2/\pi}\),

\[
 \mathbb EH_N(W^\theta)
 =\frac c2\bigl(\sqrt{1+\theta}+\sqrt{1-\theta}\bigr).
 \tag{15}
\]

There are \(N^2/2\) entries of each variance. Its endpoint difference is \(c(1-1/\sqrt2)>0\), independently of width, although its first derivative at \(\theta=0\) is zero.

The cap changes each expectation by only \(O(N^{-2})\). Independence gives

\[
 \operatorname{Var}H_N
 =N^{-3}\sum_{ij}\operatorname{Var}|W_{ij}|
 \le N^{-3}\sum_{ij}S_{ij}=N^{-2}.
\]

Write \(\mu_\theta=\mathbb EH_N\le c<1\). On \(H_N>2\),

\[
 0\le H_N-\widetilde H_N
 \le\frac{(H_N-\mu_\theta)^2}{2-\mu_\theta}.
\]

Taking expectations proves the assertion. Multiplying \(\widetilde H_N\) by a nonnegative integrable time envelope also gives a bounded velocity-like observable with an integrable Lipschitz constant and order-one integrated endpoint mean difference.

This is **not** an actual-network counterexample. It uses entrywise access to \(W\), absent from the matrix-action program class and the neural flow. Its exact implication is that row sums, permutation invariance, boundedness, a zero first interpolation derivative, and Gaussian concentration cannot establish (3) without exploiting the flow's specific matrix-action structure. The tree proof captures part of that structure; a uniform nonlinear extension is still needed.

## 6. The actual first transpose response has unbounded support

A direct calculation in the actual equations sharpens why lower clipping cannot simply be discarded. Take \(m=d=1,x=1\), and \(y>0\) within the small-label restriction. Put

\[
 \alpha_j=(A_0)_j,\quad h_j=\tanh\alpha_j,\quad
 z=W_0h,\quad b(z)=\tanh z\,\operatorname{sech}^2z.
\]

The argument of the lower clip is

\[
 c_j(t)=\operatorname{sech}^2(A_j(t))\,[B(t)^Td(t)]_j.
\]

Initially \(w=v=0,k=h\), so \(\dot A(0)=\dot v(0)=\dot k(0)=0\), \(\dot B(0)=0\), and \(\dot w(0)=2y\tanh z\). Both clips are differentiable at their zero arguments. Consequently

\[
 \dot c_j(0)=2y\operatorname{sech}^2\alpha_j\,T_j,
 \qquad T=W_0^Tb(z).
 \tag{16}
\]

Condition on \(h,z\). Each Gaussian row of \(W_0\), conditioned on its inner product with \(h\), has mean \(z_i h/\|h\|^2\) and covariance \(N^{-1}(I-hh^T/\|h\|^2)\). This follows by decomposing the isotropic row into its projection on \(h\) and its orthogonal complement; their joint Gaussian covariance is zero, so the two projections are independent. The rows remain conditionally independent. Since \(h\ne0\) almost surely,

\[
 T\ \stackrel{\rm law}{=}\
 \kappa_Nh+\sqrt{\nu_N}
 \left(I-\frac{hh^T}{\|h\|^2}\right)\xi,
 \tag{17}
\]

where \(\xi\) is an independent standard Gaussian vector and

\[
 q_N=\|h\|^2/N,\qquad
 \kappa_N=\frac{N^{-1}\sum_i z_i b(z_i)}{q_N},
 \qquad \nu_N=N^{-1}\sum_i b(z_i)^2.
\]

Put \(q=\mathbb E\tanh^2G>0\), let \(Z\sim N(0,q)\), and define

\[
 \kappa=\mathbb E[Zb(Z)]/q,\qquad
 \nu=\mathbb E[b(Z)^2]>0.
\]

The iid mean-square law gives \(q_N\to q\) in probability. Conditional on \(h\), the \(z_i\) are iid \(N(0,q_N)\). Both \(b^2\) and \(z\mapsto zb(z)\) are bounded continuous. Their empirical mean errors have conditional variance \(O(N^{-1})\), and their Gaussian expectations converge by bounded convergence as \(q_N\to q\). Thus \(\kappa_N\to\kappa\) and \(\nu_N\to\nu\) in probability. For fixed \(j\), the subtracted projection in (17) has conditional variance \(h_j^2/\|h\|^2\to0\). It follows that

\[
 \frac{\dot c_j(0)}{2y}
 \ \Longrightarrow\
 \operatorname{sech}^2G
       \bigl(\kappa\tanh G+\sqrt\nu\,G'\bigr),
 \tag{18}
\]

where \(G,G'\) are independent standard Gaussians. Conditioning on the good event preserves this limit because that event has probability tending to one.

The right-hand law has unbounded support in both directions: conditional on finite \(G\), its Gaussian variance is \(\nu\operatorname{sech}^4G>0\). There can therefore be no width-uniform coordinatewise bound \(|\dot c_j(0)|\le Cy\) on good initializations for a fixed \(C\). This calculation uses the actual reused transpose and the actual initial trajectory derivative.

Equation (18) alone does **not** prove a threshold crossing before a prescribed positive time; that would also require control of the time remainder. Its valid conclusion rules out an alleged uniform coordinatewise smallness of the lower carriers from the RMS label and operator bound alone. A response expansion must retain threshold effects.

## 7. A Taylor series need not include the clipping corners

An exact scalar diagnostic is

\[
 F(\varepsilon)=\mathbb E[C_1(\varepsilon G)^2],\qquad F(0)=0,
\]

with \(G\) standard Gaussian. For \(\varepsilon>0\), write \(\varphi\) for its density and \(Q(a)=\int_a^\infty\varphi(u)du\). Integrating \(u^2\varphi(u)\) once by parts gives

\[
 F(\varepsilon)=\varepsilon^2
 -2\varepsilon\varphi(1/\varepsilon)
 +2(1-\varepsilon^2)Q(1/\varepsilon).
 \tag{19}
\]

The difference \(\varepsilon^2-F(\varepsilon)\) is strictly positive for every nonzero \(\varepsilon\): clipping removes a positive amount on \(|G|>1/|\varepsilon|\). Near zero its magnitude is at most \(C|\varepsilon|\exp[-1/(2\varepsilon^2)]\), using \(Q(a)\le\varphi(a)/a\). The latter follows by bounding \(1\le u/a\) in the tail integral. Differentiating (19) any fixed number of times produces a finite sum of rational powers of \(\varepsilon\) times \(\varphi(1/\varepsilon)\), together with the tail term. The same tail bound makes every derivative of the difference tend to zero at zero. The even extension is smooth, with Taylor series exactly \(\varepsilon^2\), but differs from that series at every nonzero \(\varepsilon\).

This scalar function is not asserted to equal the network prediction. It proves that correct perturbative coefficients of Gaussian clipped responses need not sum to the exact expectation, even at arbitrarily small fixed activity. Equation (18) establishes that unbounded Gaussian carrier responses occur in the actual model. A label-series proof must control the nonperturbative clipping remainder at width-dependent accuracy; a remainder exponentially small in \(1/Y^2\) is still fixed as \(N\to\infty\).

The weak covariance-interpolation formula in the assigned bias input remains valid and retains the corners. A classical second-response equation instead differentiates \(C_1'\), producing signed boundary measures at \(\pm1\). Their contribution requires joint estimates for carrier density at the boundary and the matrix-entry response fields. A bound on the scalar carrier density alone does not bound a density weighted by products of those fields. No joint estimate for the evolving trajectory follows from (16)–(18).

## 8. Result and exact remaining gap

| Claim | Status in this attempt |
|---|---|
| Collision-free Wick forests have profile-independent leading weight | Proved uniformly through the block endpoint |
| Every fixed polynomial matrix-action program has endpoint mean difference \(O(N^{-1})\) | Proved, including arbitrary finite transpose reuse |
| Symmetry, row sums, and generic bounded operator-Lipschitz regularity suffice | Falsified by (13)–(15), only as a proof-route claim |
| The actual initial lower-carrier response has bounded support after division by the label | Falsified by (18) |
| A small-label Taylor expansion automatically retains all hard-clip effects | Invalid as a general principle, by (19) |
| Approximation with the explicit diagram cost (10)–(11), or a corresponding nonlinear response estimate | Open |
| Actual all-time dyadic mean estimate and own-population root-width bias | Open |
| Unconditional all-time bad-initialization moment bound | Not established; separate from the stated conditional-to-probability transfer |

The concrete new unresolved implication is (10)–(11): sum the profile-independent tree structure and the \(1/N\) loop source for the **full clipped nonlinear trajectory** at accuracy \(N^{-1/2}\), with integrable time cost. A direct weak signed-trace proof could avoid polynomial approximation, but it still needs structural control of nonlinear node responses and threshold boundary terms. No extra fitting or centered-concentration estimate supplies that control. The route remains blocked at quantitative nonlinear summation, rather than finite-program identification or long-time propagation.
