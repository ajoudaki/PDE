# C-H1: weak current-observable construction

Status: **frozen independent candidate, with initialization and restart bridges explicitly open**. This note uses only the supervisor's mathematical prompt and the required mathematical/research skills. It does not use another route, study history, or the canonical Gaussian-initialization sources. It is an internal research result, not established repository theory.

The construction below proves exact weak identities with finite level dependence and reconstruction of the currently observable-generated operator action. It does **not**, from the supplied assumptions alone, prove canonical Gaussian initialization or predictive sufficiency of the established continuation. The latter follows from the separately stated uniqueness/invariance bridge. No high temporal derivatives or moment-determinacy assumption are used.

## 1. Contract and domain

Let real probability Hilbert spaces be
\(H_i=L^2(\Omega_i,\mathbb P_i)\). At a current state,
\[
Q=(Q_1,Q_2)\in H_1^2,\qquad A\in L^\infty(\Omega_2),\qquad
W\in\mathcal B(H_1,H_2),
\]
and \(W^*\) is the actual Hilbert-space adjoint. The instantaneous construction is defined on **every** such triple, not only reached states. On a time interval, assume the supplied strong flow means
\[
Q\in C^1(H_1^2),\quad A\in C^1(H_2),\quad
W\in C^1(\mathcal B(H_1,H_2)),\quad
\sup_t\|A_t\|_\infty<\infty,
\]
locally in time. The identities also admit absolutely continuous variants, but that extension is not needed here. The flow integrals are assumed meaningful; a sufficient explicit condition is that \(\nu\) is finite and \(y\in L^1(\nu)\). For usual MSE data with finite \(\nu\) and \(y\in L^2(\nu)\), this condition holds.

For \(s\in\sqrt2S^1\), abbreviate
\[
h_s=\tanh(Qs/\sqrt2),\quad z_s=Wh_s,\quad k_s=\tanh z_s,
\]
\[
d_s=A\operatorname{sech}^2z_s,\qquad
B_s=W^*d_s,\qquad b_s=\operatorname{sech}^2(Qs/\sqrt2),
\]
\[
f_s=\langle A,k_s\rangle_2,\qquad r_s=f_s-y_s.
\]
The physical flow is
\[
\dot A=-2\int r_sk_s\,d\nu(s),\quad
\dot W=-2\int r_s(d_s\otimes h_s)\,d\nu(s),\quad
\dot Q_j=-2\int r_s\frac{s_j}{\sqrt2}b_sB_s\,d\nu(s).
\tag{1}
\]
Here \((d\otimes h)u=d\langle h,u\rangle_1\). In particular,
\(\|d_s\|_2\leq\|A\|_\infty\),
\(\|B_s\|_2\leq\|W\|\|A\|_\infty\), and
\(\|b_sB_s\|_2\leq\|W\|\|A\|_\infty\), uniformly in \(s\).

The hierarchy is an infinite family of weak laws, with finitely many expression **shapes and field occurrences** at each level. It is not a finite-dimensional state or a proved convergent finite closure. Test labels may range over smooth bounded functions; this richness is part of the candidate's explicit admissible class. Each state variable is a current observable. The evolution formula uses only other current observables, \(\nu\), and \(y\), and uses neither parameter history nor future values nor direct operator access.

## 2. Safe expression fields and finite levels

Write \(\mathcal C_m\) for the real \(C^\infty\) functions on \(\mathbb R^m\) that are bounded and have bounded derivatives of every positive order. Bounds may depend on the particular test label. Constants are included.

Construct typed finite expression trees as follows.

* The layer-1 leaves are \(Q_1,Q_2,1\); the layer-2 leaves are \(A,1\).
* If \(v_1,\ldots,v_m\) are fields on one layer and \(g\in\mathcal C_m\), then \(g(v_1,\ldots,v_m)\) is a field on that layer.
* Also allow \(Wg(v_1,\ldots,v_m)\) for layer-1 children, and \(W^*g(v_1,\ldots,v_m)\) for layer-2 children.

An operator is therefore applied only to a **bounded** smooth function of previously constructed fields. A node \(Tg(v_1,\ldots,v_m)\), where \(T\in\{I,W,W^*\}\) has the appropriate type, has size
\[
c\big(Tg(v_1,\ldots,v_m)\big)=1+\sum_jc(v_j),
\]
and a leaf has size one. Repeated subexpressions are counted repeatedly: this is a tree count, so no hidden unbounded directed-graph input is present.

Level \(S_n\) consists of the joint laws of every same-layer tuple
\((v_1,\ldots,v_m)\) with \(\sum_jc(v_j)\leq n\), retaining all expression labels and all input labels jointly. Equivalently, one may retain
\[
\mathbb E_i\Phi(v_1,\ldots,v_m),\qquad \Phi\in\mathcal C_m,
\tag{2}
\]
for these tuples. Smooth bounded tests determine the joint law: in particular real and imaginary parts of every characteristic function are among the tests. This observation uses characteristic functions, **not moments or moment determinacy**.

There are finitely many typed rooted tree shapes of size at most \(n\), and at most \(n\) field occurrences in each retained tuple. The parameter labels \(g,\Phi,s\) are continuous/infinite test families. Products of scalar expectations, needed below, use at most two independent probability-space replicas per summand. They are computed from the corresponding same-layer joint laws; no marginal-only replacement loses shared-input information.

Fix a bound \(M\) exceeding \(\|A\|_\infty\) on the interval being considered. Choose a smooth bounded function \(a_M\), with bounded derivatives, equal to the identity on \([-M,M]\). Then
\[
h_s=\tanh((s_1Q_1+s_2Q_2)/\sqrt2),\quad
z_s=Wh_s,\quad B_s=W^*[a_M(A)\operatorname{sech}^2z_s]
\]
are safe expressions. The value
\[
f_s=\mathbb E_2[a_M(A)\tanh z_s]
\tag{3}
\]
is a fixed finite-level bounded weak observable. The bound \(M\) is a declared class/local-interval bound, not information about the future trajectory. If only a current bound is known, the same statements hold on any established neighborhood with a declared common bound.

## 3. First-derivative legitimacy

The safe grammar deliberately excludes arbitrary multiplication of two unbounded \(L^2\) fields before applying an operator.

**Pathwise chain lemma.** If \(u_j(t)\in C^1(L^2)\), and \(g\) is continuously differentiable with bounded first derivatives, then
\[
\frac d{dt}g(u_1(t),\ldots,u_m(t))
=\sum_j(\partial_jg)(u_1(t),\ldots,u_m(t))\dot u_j(t)
\quad\text{in }L^2.
\tag{4}
\]
To verify this without claiming Fréchet smoothness of the Nemytskii map on \(L^2\), write the scalar fundamental-theorem-of-calculus difference quotient along the line segment from \(u(t)\) to \(u(t+h)\). Terms multiplying
\((u(t+h)-u(t))/h-\dot u(t)\) tend to zero in \(L^2\), because the derivatives of \(g\) are bounded. The remaining multiplier differences tend to zero in probability, are uniformly bounded, and multiply a fixed \(L^2\) function. Their products tend to zero in \(L^2\): truncate that fixed function at height \(K\), use bounded convergence in probability on the truncated part, and then let its \(L^2\) tail tend to zero. This argument also proves continuity of the derivative.

If \(V(t)\in C^1(\mathcal B(H_i,H_j))\) and \(u(t)\in C^1(H_i)\), the bounded bilinear product rule gives
\((Vu)'=\dot Vu+V\dot u\) in \(H_j\). Induction through the safe tree proves that every retained field is \(C^1(L^2)\). Applying (4) to the bounded outer test and then the continuous expectation functional proves that every observable (2) is \(C^1\).

This establishes first derivatives separately for every safe observable. It makes no assertion that a field such as \(b_sB_s\) has an \(L^2\) time derivative, or that observables have arbitrary temporal derivatives. Indeed, differentiation of \(b_sB_s\) would expose a product of two unbounded \(L^2\) fields, so that stronger assertion is not justified here.

## 4. Exact weak derivative by reverse adjoints

Let
\[
F=\mathbb E_i\Phi(v_1,\ldots,v_m)
\]
have total tree size, including its outer test, at most \(n\). Treat each repeated occurrence as a separate node. Initialize the covector at root \(v_j\) to
\(\lambda_{v_j}=\partial_j\Phi(v_1,\ldots,v_m)\), a bounded field. Along a node
\[
v=Tg(u_1,\ldots,u_a),\qquad T\in\{I,W,W^*\},
\]
put
\[
\eta_v=T^*\lambda_v,\qquad
\lambda_{u_j}=(\partial_jg)(u_1,\ldots,u_a)\eta_v,
\tag{5}
\]
where \(I^*=I\), \((W^*)^*=W\). Every covector lies in \(L^2\): each step uses a bounded operator or multiplication by a bounded function. One may sum covectors at shared leaves, or keep the finitely many occurrences separate. Keeping them separate gives the simpler complexity bound below.

Differentiating the tree once, and using
\(\langle\lambda,T\dot u\rangle=\langle T^*\lambda,\dot u\rangle\), gives exactly the sum of leaf and operator-variation terms. After substituting (1), each leaf occurrence contributes one of
\[
-2\int r_s\frac{s_j}{\sqrt2}
  \langle\lambda_{Q_j},b_sB_s\rangle_1\,d\nu(s),
\tag{6}
\]
\[
-2\int r_s\langle\lambda_A,k_s\rangle_2\,d\nu(s).
\tag{7}
\]
Constant leaves contribute zero. Each \(W\)-node \(v=Wg(u)\) contributes
\[
-2\int r_s
 \langle\lambda_v,d_s\rangle_2
 \langle h_s,g(u)\rangle_1\,d\nu(s),
\tag{8}
\]
and each \(W^*\)-node \(v=W^*g(u)\) contributes
\[
-2\int r_s
 \langle\lambda_v,h_s\rangle_1
 \langle d_s,g(u)\rangle_2\,d\nu(s).
\tag{9}
\]
Equations (6)–(9), summed over the finite tree, are the exact weak derivative.

All same-space unbounded products in these formulas consist of **at most two \(L^2\) factors**, possibly times a bounded factor. For example,
\[
|\langle\lambda_{Q_j},b_sB_s\rangle_1|
\leq\|\lambda_{Q_j}\|_2\|W\|\|A\|_\infty.
\]
No \(L^2\cdot L^2\to L^2\) multiplication estimate occurs. The integrands are dominated by a constant times \(|r_s|\), uniformly in \(s\), since \(\|h_s\|_2,\|k_s\|_2\leq1\) and the finite covector norms are bounded by products of operator norms and test-derivative bounds.

The expressions (5) contain operator actions on unbounded \(L^2\) arguments. They are used to **prove** the derivative, not supplied as raw operator queries in the hierarchy evolution. The following bounded-cutoff construction removes those queries from the right-hand side.

## 5. Reverse cutoff and an explicit finite dependency level

Choose smooth functions \(\chi_R:\mathbb R\to\mathbb R\), \(R\geq1\), such that
\[
\chi_R(u)=u\ (|u|\leq R),\qquad
|\chi_R(u)|\leq|u|,\qquad
\operatorname{Lip}(\chi_R)\leq1,
\]
and \(\chi_R\) is bounded and has bounded derivatives of every order. For example, integrate a smooth even cutoff of the derivative, equal to one on \([-R,R]\), valued in \([0,1]\), and zero outside \([-2R,2R]\).

Define a safe approximation of each reverse covector. Root covectors are left exact. At a reverse step across \(v=Tg(u)\), set
\[
\eta_v^{R}=\begin{cases}
\lambda_v^{R},&T=I,\\
T^*\chi_R(\lambda_v^{R}),&T=W\text{ or }W^*,
\end{cases}
\]
\[
\lambda_{u_j}^{R}
=(\partial_jg)(u_1,\ldots,u_a)\chi_R(\eta_v^{R}).
\tag{10}
\]
The last expression is a single bounded smooth function of the original children and \(\eta_v^R\). Every field in (10) is thus a safe expression. There are no unbounded operator arguments.

For any \(v_R\to v\) in \(L^2\),
\[
\|\chi_R(v_R)-v\|_2
\leq\|v_R-v\|_2+\|\chi_R(v)-v\|_2\longrightarrow0.
\tag{11}
\]
The last limit is dominated convergence, since \(\chi_R(v)\to v\) pointwise and \(|\chi_R(v)-v|\leq2|v|\). Applying (11), the boundedness of \(W,W^*\), and bounded multiplication at each finite reverse step proves
\[
\lambda_v^R\longrightarrow\lambda_v\quad\text{in }L^2
\tag{12}
\]
for every occurrence. Their \(L^2\) norms are bounded independently of \(R\), by the same finite products of test-derivative bounds and operator norms.

Here is an explicit conservative size bound. A root covector has size at most \(n\). At one step of a reverse path, the operator cutoff adds at most one node, and the bounded multiplication introduces one node and copies the children of one forward node, of combined size at most \(n-1\). Thus each step adds at most \(n+1\) nodes. Every path has at most \(n\) steps, giving
\[
c(\lambda_v^R)\leq n^2+2n.
\tag{13}
\]
This bound is independent of \(R\). It also allows harmless redundant cutoffs when \(T=I\).

In (6)–(9), replace covectors by (10) and replace each unbounded scalar factor in an expectation by its \(\chi_R\) cutoff. For instance use
\[
\mathbb E_1\!left[
\chi_R(\lambda_{Q_j}^R),
\chi_R(B_s),
\operatorname{sech}^2((s_1Q_1+s_2Q_2)/\sqrt2)
\right]
\tag{14}
\]
in (6). The integrand in (14) is a bounded smooth test of a finite safe tuple. By (11)–(12) and Cauchy–Schwarz, it converges to the pairing in (6). The other pairings converge by the same two-factor argument. Uniform covector norm bounds permit the limit under the \(s\)-integral, by the domination established after (9).

The elementary physical fields \(h_s,z_s,k_s,d_s,B_s\) have fixed tree sizes. Equations (13)–(14) therefore give, for example, the explicit sufficient level
\[
N(n)=4(n+10)^2
\tag{15}
\]
for every bounded-cutoff observable used in the weak derivative of a size-\(n\) observable. This deliberately loose bound also covers the prediction (3), the extra \(Q\) leaves, and both factors of every product of expectations.

Consequently there is a defined functional \(\mathcal D_F\) such that, on every strong trajectory in Section 1,
\[
\frac d{dt}F_t=\mathcal D_F(S_{N(n)}(t);\nu,y),
\tag{16}
\]
where \(\mathcal D_F\) is the explicitly specified common-cutoff limit of (6)–(10), (14). Computing its approximands requires only current weak observables at level \(N(n)\), the known residual from (3), finite algebra, and integration over training input. It requires no call to \(W_t\) or \(W_t^*\).

**What “finite” does and does not mean here.** Formula (16) has exact dependence on a finite hierarchy level, and every cutoff approximand has a finite expression construction with a size bound independent of the cutoff. The exact right-hand side is a convergent cutoff **limit within that fixed level**. No uniform truncation error or finite numerical evaluation budget is proved. If C-H1 requires a finite number of weak-test evaluations with no limiting operation, this candidate does not establish that stronger requirement. Also, the level is a test-indexed weak-law family, not finitely many scalar coordinates.

## 6. What the full hierarchy reconstructs at a current state

Let \(\mathcal E_i\) denote all safe expression fields on layer \(i\). Let
\[
\Sigma_i=\sigma(\mathcal E_i)\quad\text{(completed)},\qquad
K_i=L^2(\Omega_i,\Sigma_i,\mathbb P_i).
\]
These are current-state constructions, not histories. Let \(D_i\) be the bounded algebra of smooth bounded functions of finite tuples of safe fields. It contains constants, is closed under finite sums and products, and generates \(\Sigma_i\): for every \(v\in\mathcal E_i\), the bounded functions \(\chi_R(v)\in D_i\) converge pointwise to \(v\).

The bounded-function monotone-class argument gives density of \(D_i\) in \(K_i\). In the precise form needed, a unital bounded algebra that generates a sigma algebra has dense linear span in \(L^2\) of that sigma algebra: the closure contains bounded monotone limits by dominated convergence, so the monotone class generated by the algebra contains all bounded measurable functions; truncation then handles every \(L^2\) function. This verifies the density hypothesis rather than presuming coordinate moments determine the law.

By definition of the grammar,
\(WD_1\subset K_2\) and \(W^*D_2\subset K_1\). Boundedness and density imply
\[
WK_1\subset K_2,\qquad W^*K_2\subset K_1.
\tag{17}
\]
The complementary inclusions also follow by adjointness, e.g.
\(\langle Wu,v\rangle_2=\langle u,W^*v\rangle_1=0\)
for \(u\in K_1^\perp,v\in K_2\). Thus the pair \((K_1,K_2)\) reduces the two-layer operator: \(W\) has no cross blocks between these subspaces and their orthogonal complements.

Now consider another current triple \((\widetilde Q,\widetilde A,\widetilde W)\), possibly on different probability spaces, with the **same labeled joint hierarchy at every level**. Send any \(g(v_1,\ldots,v_m)\in D_i\) to the identical labeled expression in the second triple. Equality of finite joint laws makes this map well defined: a difference that is zero almost surely in the first state has the same zero squared norm in the second. The same equality gives preservation of inner products, constants, products, and bounded functional calculus. It extends by density to a surjective isometry
\[
U_i:K_i\longrightarrow\widetilde K_i.
\tag{18}
\]
It preserves expectation since \(U_i1=1\). Bounded measurable functional calculus follows by bounded approximation and the monotone-class argument; \(L^2\) limits extend it to the operations used here. In particular, \(U_i\) preserves multiplication by a bounded field. For unbounded base leaves, apply the map to \(\chi_R(Q_j)\) or \(\chi_R(A)\) and use \(L^2\) convergence to obtain
\[
U_1Q_j=\widetilde Q_j,\qquad U_2A=\widetilde A.
\tag{19}
\]
On \(D_1\), the identical-expression rule directly gives
\(U_2Wd=\widetilde WU_1d\). Density extends this to
\[
U_2W|_{K_1}=\widetilde W|_{\widetilde K_1}U_1,
\qquad
U_1W^*|_{K_2}=\widetilde W^*|_{\widetilde K_2}U_2.
\tag{20}
\]

Therefore equality of the full current hierarchy reconstructs, up to a probability-algebra isometry, the base fields and the **entire operator action on the observable-generated reducing subspaces**. It need not determine the orthogonal blocks. This is an exact reconstruction statement, and it is stronger than equality of present predictions.

This richness does not establish finite-dimensional compression. If arbitrary internal bounded-test labels are outside the intended admissible observable class, the candidate must be restricted and (17)–(20) do not automatically survive that restriction. The grammar must not be described as a fixed finite list of prescribed activations when it actually admits arbitrary test labels.

## 7. Restart implication and its exact missing bridge

For a fixed current state and the subspaces \(K_i\) above, the vector field (1) is tangent to the following invariant candidate class:
\[
Q(t)\in K_1^2,\quad A(t)\in K_2,\quad
W(t)=W(0)+C(t),
\]
where \(C(t)\) vanishes on \(K_1^\perp\) and maps \(K_1\) into \(K_2\). Indeed, bounded functional calculus preserves the \(K_i\), (17) preserves forward and backward fields, bounded multiplication preserves \(K_1\), and the rank-one updates \(d_s\otimes h_s\) have exactly the stated support. This is a checked **tangency** statement.

Tangency alone does not prove that a specified infinite-dimensional strong continuation remains in this class. Nor does the prompt's existence statement, by itself, provide the requisite uniqueness. An ambient \(L^2\) Picard theorem must not be invoked without a valid local Lipschitz estimate: the troublesome term
\((b(Q)-b(\widehat Q))B\) generally has no estimate by a universal constant times \(\|Q-\widehat Q\|_2\) when only \(B\in L^2\) is known.

The missing bridge can be supplied by the following precise property of the **established reached flow**, if proved separately:

> From each reached state under comparison, the established continuation stays in its frozen observable-generated class above; and a continuation transported by the probability-algebra isometries (18)–(20) agrees with the established continuation of the transported reached state on the common positive time/law neighborhood.

For example, existence of the restricted continuation plus uniqueness in a class covering both it and the established continuation suffices. An independently proved one-reference tail comparison may also supply this property. Neither assertion is proved from the prompt-only inputs here.

**Conditional restart theorem.** Under that bridge, equality of the full current hierarchy for two reached states implies equality of their future prediction functions, and in fact of their full future labeled hierarchies, throughout the common continuation neighborhood.

Proof: transport the restricted fields by \(U_1,U_2\), and the restricted operator by \(U_2W(t)U_1^{-1}\). Equations (19)–(20), preservation of bounded multiplication and expectations, and the rank-one identity
\[
U_2(d\otimes h)U_1^{-1}=(U_2d)\otimes(U_1h)
\]
show term by term that the transported fields solve (1), with identical \(f_s\), \(r_s\), \(\nu\), and \(y\). The stated bridge identifies this continuation with the second established flow. Induction through the expression grammar then proves equality of all future labeled joint laws. This proof starts from the current state and uses no retained history.

Without the bridge, the unconditional result is (17)–(20) and equality of every weak derivative (16) at matching current hierarchies. Neither fact alone proves uniqueness of solutions of the infinite hierarchy or predictive sufficiency.

## 8. Finite evaluation and canonical initialization

For any fixed current parameter triple, each hierarchy entry has a finite semantic expression tree: finite pointwise smooth operations, finitely many **shared** \(W,W^*\) applications, and a final finite-dimensional joint weak test. This makes the observable itself well defined. It is not an evolution algorithm with access to the current operator; evolution is instead (16).

The finite tree also identifies exactly what an initialization theorem must provide: the joint initialization law of a finite alternating forward/adjoint program, with all repeated uses of the same initial operator correlated. A fresh independent Gaussian draw at each invocation is not such a theorem.

**Initialization remains missing in this scoped candidate.** The supplied phrase “reused Gaussian action” does not include its complete alternating-adjoint evaluation rules. I have not read or inferred those rules. In particular, replacing the canonical initialization by a bounded isonormal embedding and using its first-chaos adjoint would eliminate a potentially surviving reverse Gaussian bulk and is not an admissible substitution. The supervisor is to supply the canonical finite initialization from the complete designated sources. It must cover the safe expression class in Section 2, including arbitrary bounded smooth internal tests, or explicitly state any smaller covered class and revisit reconstruction.

Even once a joint law for each finite program is supplied, the initialization proof must verify consistency for repeated labels and all finite collections. Initialization of each retained finite tree is separate from any claim that infinitely many initial laws are computable in one finite operation.

## 9. Claim ledger, audit, and route recommendation

| Claim | Status | Exact dependency or limitation |
|---|---|---|
| Safe fields and weak observables exist at every level | Proved on Section 1 instantaneous domain | Bounded \(W\), \(Q\in L^2\), \(A\in L^\infty\); finite safe grammar |
| Every retained weak observable has a first derivative along the supplied strong flow | Proved under stated path regularity | Pathwise \(L^2\) chain lemma; no high derivatives |
| Exact weak evolution depends on a finite higher level | Proved as the cutoff-limit formula (16) | Arbitrary smooth bounded test labels; level bound (15); no finite cutoff-error rate |
| No illegal same-norm multiplication | Checked | Reverse factors stay \(L^2\); scalar products use at most two such factors |
| Full hierarchy reconstructs dynamically relevant current action | Proved, (17)–(20) | Equality of all labeled joint laws, not marginal laws |
| Actual reached continuations stay in reconstructed subspaces and transport uniquely | Open in supplied scope | Requires the separate uniqueness/invariance bridge of Section 7 |
| Predictive sufficiency/restartability | Conditional theorem | Follows from that bridge, not from formal weak identities alone |
| Canonical finite Gaussian initialization | Open in supplied scope | Must preserve actual-adjoint reuse and any reverse Gaussian bulk |
| Closed finite truncations, hierarchy uniqueness, convergence rates, arbitrary-accuracy finite surrogates | Not claimed | No theorem here bridges exact weak identities to these stronger assertions |

The strongest remaining structural objections are explicit: the admissibility of the test-indexed internal grammar; the cutoff limit if a finite-evaluation requirement forbids it; the canonical alternating Gaussian initialization; and the reached-flow uniqueness/invariance bridge. None is disguised as an automatic consequence of boundedness or formal tangency. Moment indeterminacy and high temporal differentiability are avoided rather than assumed away.

**Registry recommendation:** retain this route as a concrete candidate/reconstruction mechanism, frozen pending the canonical initialization and reached-flow comparison supplied by the supervisor. It provides an exact current-observable weak hierarchy under a stated broad test class, but the supplied prompt alone does not complete C-H1.
