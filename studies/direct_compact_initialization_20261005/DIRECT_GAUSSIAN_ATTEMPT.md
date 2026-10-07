# Direct Gaussian initialization: constructive finite compiler and an exposed missing innovation

Status: bounded author investigation, frozen candidate calculations, not independently reviewed or promoted. No experiment or Git write was performed. The strict all-time, whole-sphere root-width comparison remains open.

The positive finding is concrete: the maintained book already supplies a direct Gaussian-law initializer for every fixed finite retained dictionary. It computes the forward/adjoint mixer and both activation quadratures without realizing a width-\(n\) matrix or its trajectory. Its proved scope is an ordered, fixed-dictionary numerical limit. It does not calibrate dictionary size, source count, or quadrature work to the tolerance \(n^{-1/2}\).

The calculation below gives a model-specific version of that initializer and identifies the first unrepresented Gaussian innovation. This shows exactly why initializing a contraction matrix from Gaussian expectations is insufficient by itself to close future nonlinear matrix actions. It is a limitation of the specified initial core, not a no-go theorem for richer direct constructions.

## 1. Model and the finite-dimensional objects being synthesized

Write \(u=x/\sqrt d\) for normalized inputs, so \(\|u\|_2=1\). The training directions \(u_a\), \(1\le a\le m\), are orthonormal. The canonical width-\(n\) model is

\[
f_n(u)=\frac1n w_n^T\phi\big(W_n\phi(A_nu)\big),
\qquad \phi=\tanh,
\]

with independent initialized entries \(A_{n,ij}\sim N(0,1)\), \(W_{n,ij}\sim N(0,1/n)\), and \(w_n(0)=0\). It trains by gradient flow of \(m^{-1}\sum_a(f_n(u_a)-y_a)^2\) with mobilities \((n,1,n)\). Labels are fixed and sufficiently small for the intended all-time fitting target, but the finite initialization identities below do not need smallness.

The book's generic finite closure uses a lower population of fixed marks \(b_i\in\mathbb R^{r_1}\), an upper population of fixed marks \(\beta_j\in\mathbb R^{r_2}\), positive quadrature weights \(\pi_i,\rho_j\) summing to one in each population, and moving variables

\[
v_i(t)\in\mathbb R^d,\qquad c_j(t)\in\mathbb R,
\qquad M(t)\in\mathbb R^{r_2\times r_1}.
\]

The input dimension is \(d\); the dictionary lengths \(r_1,r_2\), quadrature sizes \(P_1,P_2\), Gaussian source count \(s\), and dense neural width \(n\) are distinct quantities. With \(E_1,E_2\) denoting the finite weighted sums, define

\[
\begin{aligned}
h_i(u)&=\phi(v_i\cdot u),&a(u)&=E_1[bh(u)],\\
H_j(u)&=\phi(\beta_j^TMa(u)),&\widetilde f(u)&=E_2[cH(u)],\\
\mathbf d(u)&=E_2[\beta c\phi'(\beta^TMa(u))],&
p_i(u)&=b_i^TM^T\mathbf d(u).
\end{aligned}
\]

Its exact finite equations are

\[
\dot v_i=-\frac2m\sum_a(\widetilde f(u_a)-y_a)
  \phi'(v_i\cdot u_a)p_i(u_a)u_a,
\]

\[
\dot c_j=-\frac2m\sum_a(\widetilde f(u_a)-y_a)H_j(u_a),
\qquad
\dot M=-\frac2m\sum_a(\widetilde f(u_a)-y_a)\mathbf d(u_a)a(u_a)^T.
\tag{1}
\]

These are the book C.1 equations with its probability law specialized to the empirical training law. Replacing its two input coordinates by \(d\) coordinates changes only Euclidean dot products and the lower row shape; direct differentiation verifies (1). The state metric is

\[
\sum_i\pi_i|\delta v_i|^2+\sum_j\rho_j|\delta c_j|^2+\|\delta M\|_F^2.
\]

Thus both action orientations use the same \(M\) and its actual transpose, and physical time has the canonical factor \(2/m\). This algebraic extension does not import the book's continuum-convergence theorem to arbitrary \(d,m\) or all times.

For fixed dictionaries and nodes, the total moving and fixed state is

\[
O\big(P_1(d+r_1)+P_2(1+r_2)+r_1r_2+md\big)
\]

scalars. A training vector-field evaluation costs
\(O(m[P_1(d+r_1)+P_2r_2+r_1r_2])\) scalar operations. The question is therefore how to synthesize the joint marks and initial mixer \(M(0)\), and how large these quantities must be for the target accuracy.

## 2. A direct Gaussian core, with no population oracle

Use \(g\sim N(0,I_d)\) in the lower population and let \(g_a=g\cdot u_a\). Put

\[
h_a=\phi(g_a),\qquad q=E_1[h_a^2]=E\phi(G)^2>0.
\]

The upper initial forward fields \(\xi_a=W_0^{(2)}h_a\) have the law \(N(0,qI_m)\). Define upper fields

\[
S(\xi)=\frac2m\sum_b y_b\phi(\xi_b),
\qquad U_a(\xi)=S(\xi)\phi'(\xi_a).
\tag{2}
\]

These are respectively the initial readout velocity and the leading second-layer backward fields of the canonical model. Their covariance and response coefficients are explicit finite Gaussian integrals:

\[
C_{ab}=E_2[U_aU_b],\qquad D_{ba}=E_2[\partial_{\xi_b}U_a].
\tag{3}
\]

Let \(\zeta\sim N(0,C)\) be independent of \(g\). The exact initialized population reverse fields are

\[
R_a=(W_0^{(2)})^*U_a
=\zeta_a+\sum_bD_{ba}h_b.
\tag{4}
\]

Equation (4) is the source-response identity of III.F.4 for the finite program consisting of the initial forward calls and these reverse calls. The response term in (4) must be retained. It is not an independent-Gaussian replacement of the transpose action.

Choose bounded lower dictionary functions \(F_i(g,\zeta)\), \(1\le i\le r_1\), and bounded upper functions \(B_j(\xi)\), \(1\le j\le r_2\), each given by a valid finite smooth initialized-word expression. Require polynomial Gaussian envelopes for the values and every named-source derivative used below, uniformly on compact sets of the earlier coefficients, as in the contained source compiler. No extension to arbitrary bounded smooth functions with merely integrable derivatives is claimed. The initialized cross-contraction matrix has the exact formula

\[
\begin{aligned}
C^{\mathrm{mix}}_{ji}
&=E_2[B_jW_0^{(2)}F_i]\\
&=\sum_bE_1[F_i h_b]E_2[\partial_{\xi_b}B_j]
 +\sum_aE_1[\partial_{\zeta_a}F_i]E_2[B_jU_a].
\end{aligned}
\tag{5}
\]

To prove this, append the action \(W_0^{(2)}F_i\) to the source program. Its response is \(\sum_aU_aE_1[\partial_{\zeta_a}F_i]\). Its centered forward source has covariance \(E_1[F_ih_b]\) with \(\xi_b\). Gaussian regression on \(\xi\), whose covariance is \(qI_m\), and scalar Gaussian integration by parts give

\[
E_2[B_j\xi_{F_i}]
=\sum_b\frac{E_1[F_ih_b]}q E_2[B_j\xi_b]
=\sum_bE_1[F_ih_b]E_2[\partial_{\xi_b}B_j].
\]

The source remainder is independent of \(\xi\), centered, and hence has zero contraction with \(B_j\). This proves (5), including singular \(C\); \(\zeta=C^{1/2}Z\) is sufficient to define all Gaussian integrals. The formula integrates an innovation out of one **linear contraction**. It does not assert that the joint action law lacks that innovation.

Let \(G_1=E_1[FF^T]\), \(G_2=E_2[BB^T]\), choose a positive ridge \(\eta\), and form positive-diagonal Cholesky factors

\[
L_\ell L_\ell^T=G_\ell+\eta I,
\quad b=L_1^{-1}F,\quad\beta=L_2^{-1}B,
\quad M(0)=L_2^{-1}C^{\mathrm{mix}}L_1^{-T}.
\tag{6}
\]

Initialize lower moving rows from the same lower Gaussian nodes as their marks, \(v_i(0)=g_i\), and set \(c_j(0)=0\). Equations (2)–(6) specify a direct-law initializer. They use Gaussian dimensions \(d+m\) and \(m\), independent of dense width. They require no dense-trained object and no fitted population coefficients as input. Every expectation is an integral of an explicitly given finite-dimensional function.

For example, take a Gaussian quadrature cloud constructed by the Halton/Box–Muller rule proved in book C.2. First compute (3), then evaluate the lower functions at \((g,C^{1/2}Z)\), evaluate the upper functions at \(\sqrt q Z'\), and form the finite sums in (5)–(6). At fixed dictionaries and positive ridge, their convergence follows from C.2's joint Gaussian quadrature lemma and continuity of positive square roots and positive-definite Cholesky factors. That lemma permits earlier coefficients to have been computed on the same cloud. No unknown population integral has to be supplied by an oracle.

For the book's original core, \(U_a=\phi(\xi_a)\), (5) is exactly its equation `eq-docs-global-nonlinear-l13908`. Equations (2)–(5) instead use the canonical model's initial backward fields; their proof uses the same contained III.F source rule. The book's general initialized-word dictionary, rather than its particular core coordinates alone, is the mechanism for enriching the retained source space.

## 3. The complete direct finite-program compiler

The following is the constructive content of book C.2, not a new width theorem. Fix a finite typed directed acyclic graph of initialized words, their requested forward and reverse actions, and all dependencies. Each layer has its own Gaussian population cloud. Every literal action has a distinct named source unless it is literally the same graph node.

At a new oriented action with operand \(v\):

1. Estimate its covariance with every previous operand of the same orientation by the quadrature sums \(E_Q[vv_j]\), and its variance by \(E_Q[v^2]+\varepsilon\), for a fixed \(\varepsilon>0\). Preserve earlier operand tables and coefficients. The covariance prefix is its empirical operand Gram plus \(\varepsilon I\).
2. Append one Cholesky row and generate the new Gaussian source from the corresponding coordinates of the cloud. Previous source values are unchanged.
3. Set the action value to that source plus the causal response sum \(\sum_jE_Q[\partial_jv]v_j\) over earlier opposite-orientation actions. The derivative is of the explicit operand expression in named sources. Earlier covariance/response coefficients, roots, and opposite-population graph operands are held fixed.
4. Continue coordinate operations and contractions in dependency order. A new action caused by a new nonlinear operand is a new source, not a relabeling of an old one.

Formal automatic differentiation is important here: differentiating estimated coefficients as functions of the cloud would implement a different recursion. The source rule differentiates the current symbolic expression with those coefficients fixed.

For every fixed graph and \(\varepsilon>0\), C.2 proves convergence as coefficient-node count \(Q\to\infty\). Replay on \(P\) nodes uses those frozen coefficients and factors, with no refitting. The limit \(P\to\infty\) recovers the corresponding joint marks. Only after the coefficient limit does \(\varepsilon\downarrow0\) remove source regularization. Continuity of positive semidefinite square roots, rather than continuity of singular Cholesky factors, identifies this last limit.

Thus the book provides an executable route from a finite syntax description to approximate initialized marks and mixers, including both orientations of the same Gaussian action. It is stronger than prescribing inaccessible coefficients. It is still weaker than a width-dependent root-error construction.

For exact resource bookkeeping, let \(K\) be the complete graph-node count, \(s\) the named-source count, \(r=r_1+r_2\), and \(E=2K+s^2\). C.6 gives the conservative initializer work

\[
O\big(QsE+Qs^2+s^3+(Q+P)E+(Q+P)r^2+r^3\big)
\tag{7}
\]

and workspace

\[
O\big((Q+P)(K+s+r)+s^2+r^2\big).
\tag{8}
\]

These are scalar counts, with Gaussian digit generation and precision costs additional. For arbitrary \(d\), storing/replaying the first-root coordinates adds the corresponding \(O((Q+P)d)\) term. There is no dense-width factor in (7) or (8). The required polylogarithmic bound concerns the retained compact state, whose count is given in Section 1. Initializer work and temporary workspace in (7)–(8) must be explicit and must avoid constructing or querying the dense network, but they may exceed the retained-state bound. A quantitative accuracy schedule must therefore control retained \(P_1,P_2,r_1,r_2\) within the old size bound and report the potentially larger setup work and workspace separately.

C.1's full neural comparison theorem is narrower than the present target: its initial neural readout is iid \(N(0,n^{-2})\), its prescribed population/closure readout is zero, its input domain is the circle, its inherited represented-law class is the rational two-arc family at \(T=1/200\), and all numerical/order limits are explicitly nested. The algebraic initializer itself is unaffected by replacing the vanishing neural readout by exact zero, but the full convergence theorem is not silently extended here to arbitrary orthogonal \(m\)-sample data, general dimension, or all-time endpoints. Only its contained finite Gaussian-integration construction and finite equations are used.

## 4. The first fresh innovation: an exact three-query calculation

Consider the canonical one-sample case, which lies within the orthogonal-data benchmark, with fixed \(y\ne0\). This calculation concerns two exact raw Euler updates of step \(h>0\) and the following forward evaluation; it isolates an initialization-closure issue and is not a claimed GF discretization rate.

Let \(g\sim N(0,1)\), \(H=\phi(g)\), \(q=EH^2\), and \(\xi\sim N(0,q)\) in the upper population. Set

\[
\lambda=E\phi(\xi)^2,\qquad
U=2y\phi(\xi)\phi'(\xi),\qquad
C=EU^2>0,\qquad D=EU'(\xi).
\]

Let \(\zeta\sim N(0,C)\) independently of \(g\), so the initial reverse field is

\[
R=W_0^*U=\zeta+DH.
\tag{9}
\]

The first Euler update changes only the readout, to \(c_1=2hy\phi(\xi)\). Its training residual is \(r_1=y(2h\lambda-1)\). The second update changes the first preactivation and connector to

\[
g_2=g+\epsilon\phi'(g)R,
\qquad W_2=W_0+\epsilon U\otimes H,
\qquad \epsilon=-2h^2r_1.
\tag{10}
\]

It changes the readout to \(c_2=4hy(1-h\lambda)\phi(\xi)\). These identities follow directly from the canonical mean-loss gradient equations at the two nodes; no continuous-time Taylor expansion is used.

Define the new lower activation and three scalar coefficients by

\[
F_\epsilon=\phi\big(g+\epsilon\phi'(g)(\zeta+DH)\big),
\quad a_\epsilon=\frac{E[HF_\epsilon]}q,
\quad b_\epsilon=E[\partial_\zeta F_\epsilon],
\]

\[
v_\epsilon=E[F_\epsilon^2]-\frac{E[HF_\epsilon]^2}q.
\tag{11}
\]

Applying the same source rule to the third call gives the exact scalar law

\[
W_0F_\epsilon
=a_\epsilon\xi+b_\epsilon U+\sqrt{v_\epsilon}\,G_{\mathrm{new}},
\tag{12}
\]

where \(G_{\mathrm{new}}\sim N(0,1)\) is independent of the old upper source \(\xi\). The trained rank-one part is retained exactly:

\[
W_2F_\epsilon
=\underbrace{a_\epsilon\xi+
 (b_\epsilon+\epsilon E[HF_\epsilon])U}_{\mu_\epsilon(\xi)}
 +\sqrt{v_\epsilon}\,G_{\mathrm{new}}.
\tag{13}
\]

For every \(\epsilon\ne0\), \(v_\epsilon>0\). Indeed, conditional on \(g\), the variable \(F_\epsilon\) is a strictly monotone nonconstant function of the nondegenerate Gaussian \(\zeta\), because \(\phi'\) is positive everywhere. Hence its conditional variance is positive. Since projection on the span of \(H\) is no better than conditioning on the entire \(g\),

\[
v_\epsilon=\inf_a E(F_\epsilon-aH)^2
\ge E\operatorname{Var}(F_\epsilon\mid g)>0.
\]

The size is explicit to leading order. Dominated convergence, using
\(|(F_\epsilon-H)/\epsilon|\le|R|\), gives

\[
\frac{F_\epsilon-H}{\epsilon}\to\phi'(g)^2R
\quad\text{in }L^2.
\]

After orthogonal projection away from \(H\),

\[
\frac{v_\epsilon}{\epsilon^2}\to
\big\|\phi'(g)^2R-\frac{E[H\phi'(g)^2R]}qH\big\|_{L^2}^2
\ge C E\phi'(g)^4>0.
\tag{14}
\]

The inequality isolates the independent, centered \(\phi'(g)^2\zeta\) component, which is orthogonal to every function of \(g\).

Equation (13) has two consequences. First, an upper dictionary consisting only of functions of the original \(\xi\) cannot represent this action exactly, regardless of how many such functions it contains: its best conditional-mean approximation has RMS error \(\sqrt{v_\epsilon}\). Second, knowing all the linear contractions (5) does not remove this residual. Those contractions integrate out \(G_{\mathrm{new}}\), but the next tanh does not commute with that integration.

The latter issue affects a predictor, not only a hidden field. If one retained the exact means and rank-one memory in (13) but omitted the new innovation, the true two-step output and this projected-core output would differ by

\[
4hy(1-h\lambda)E\left[\phi(\xi)
 \left(E_G\phi(\mu_\epsilon(\xi)+\sqrt{v_\epsilon}G)
                   -\phi(\mu_\epsilon(\xi))\right)\right].
\tag{15}
\]

Because tanh has bounded fourth derivative, Taylor's formula and
\(EG=EG^3=0\), \(EG^2=1\), \(EG^4=3\) give uniformly in real \(z\)

\[
E_G\phi(z+\sqrt vG)-\phi(z)
=\tfrac v2\phi''(z)+O(v^2).
\]

As \(h\downarrow0\) at fixed \(y\ne0\), \(\epsilon\to0\),
\(\mu_\epsilon(\xi)\to\xi\) in \(L^2\), and (14) shows \(v_\epsilon>0\). Dividing (15) by \(4hy(1-h\lambda)v_\epsilon\), its limit is

\[
\tfrac12E[\phi(\xi)\phi''(\xi)]
=-E[\tanh^2(\xi)\operatorname{sech}^2(\xi)]<0.
\tag{16}
\]

Thus the omitted source produces a nonzero nonlinear predictor discrepancy for all sufficiently small fixed nonzero steps. This discrepancy is independent of the dense width after its fixed-program limit. It can be removed by adding the new source or integrating its conditional law inside this one activation, but future reverse actions then require the corresponding joint source and derivative information as well. Scalar smoothing of one forward value alone is not the full response-preserving update.

This calculation does not disprove a growing dictionary, an adaptive source compiler, or a GF approximation with shrinking time mesh. It identifies the exact information that such a construction must retain or control.

## 5. What a virtual finite-width reference supplies—and what it does not

The analogous finite-width identity makes the remaining dependence visible without invoking any asymptotic law. In the preceding one-sample setup, let \(g,H,Y,U,R\) be length-\(n\) arrays, with \(Y=W_0H\), \(U=2y\phi(Y)\phi'(Y)\), and \(R=W_0^TU\). Define

\[
q_n=\|H\|_2^2/n,\quad b_n=Y^TU/n,
\quad c_n=\|U\|_2^2/n,
\quad P_H=HH^T/\|H\|_2^2.
\]

Conditional on \((g,Y)\), Gaussian row conditioning gives exactly

\[
R\ \overset d=\frac{b_n}{q_n}H+
             \sqrt{c_n}(I-P_H)Z,
\qquad Z\sim N(0,I_n)
\tag{17}
\]

with \(Z\) independent of the conditioned variables. For any subsequent lower query \(F\) measurable from this transcript, write

\[
F_\perp=(I-P_H)F,\qquad
a_n=H^TF/(nq_n),\qquad P_U=UU^T/\|U\|_2^2.
\]

Conditioning on the complete two-direction transcript gives exactly

\[
W_0F\ \overset d=
a_nY+
U\frac{R^TF_\perp/n}{c_n}
 +\frac{\|F_\perp\|_2}{\sqrt n}(I-P_U)\Gamma,
\quad\Gamma\sim N(0,I_n),
\tag{18}
\]

where \(\Gamma\) is independent of that transcript. The denominators are positive almost surely for this nonzero-label Gaussian initialization. These formulas are direct specializations of book III.F.3; they keep the empirical coefficients and both finite-rank projections.

Equations (17)–(18) eliminate the need to store \(n^2\) matrix entries. They do not eliminate the \(n\)-coordinate nonlinear empirical contractions or the \(n\)-dimensional innovations. A literal exact simulator with \(s\) retained calls uses \(O(ns+s^2+nd)\) scalar storage and \(O(ns^2+s^3)\) transcript work, up to root and coordinate-operation costs. Streaming/regeneration may alter storage, but computing these empirical contractions still constructs or evaluates the virtual width-\(n\) state. That is the scope violation for the requested law-only initializer; width-dependent setup work by itself is not forbidden.

Replacing those contractions by Gaussian-law quadrature is precisely the additional approximation accomplished at fixed program length by III.F and C.2. It is not an exact finite-width sufficient-statistic identity of dimension \(s\). A virtual dense reference may be used in a proof coupling, but its actual \(n\)-row empirical data cannot be passed into the claimed compact construction.

The separate exact replacement law in book Gaussian-reuse G.1–3 also illustrates this distinction: it replaces a matrix with Gaussian source arrays and response coefficients while preserving adaptive transcript law. Its source arrays remain \(n\times s\), and its fixed-history covariance proof is followed by sequential conditioning. It does not license treating adapted coefficients as independent of already used Gaussian primitives. No result for its different clipped three-hidden-layer application is imported here.

## 6. Remaining obligation and verdict

A usable direct synthesis route is therefore:

\[
\text{finite initialized-word dictionary}
\longrightarrow
\text{causal Gaussian source compiler and quadrature}
\longrightarrow
\text{joint marks and one forward/adjoint mixer}
\longrightarrow
\text{autonomous finite equations (1)}.
\]

The first two arrows have a contained fixed-dictionary construction. The last arrow is a well-defined finite smooth ODE with the correct shared transpose and mean-loss clock. Equations (12)–(16) show why dictionary enrichment must account for fresh action innovations and their later responses, rather than merely fit more functions of an unchanged initial source list.

To prove the requested compact theorem one still needs a quantitative bound that links the reachable action-source tail to dictionary/source order and propagates its error through actual nonlinear training. Simultaneously, one needs finite-width fluctuation and weak-bias control against the same deterministic evolution, and a quadrature/regularization schedule that reaches the required accuracy while preserving the old polylogarithmic retained-state bound. The initializer's work and temporary workspace in (7)–(8) must be reported explicitly and remain independent of any realized dense reference, but may be larger than the retained compact state. C.1 explicitly states that its nested limits give neither an arbitrary diagonal nor a universal computable tolerance schedule. The present calculation supplies no replacement for those missing estimates.

An error description such as \(O_{\mathbb P}(n^{-1/2})+e_{r,Q,P,s}\), with a separately proved \(e_{r,Q,P,s}\to0\), would be a useful intermediate theorem. It is weaker than the strict target unless \(e_{r,Q,P,s}\le C/\sqrt n\) is established with the admissible resources. Even that decomposition is not proved for the full all-time GF here; fixed-program source laws are not a quantitative theorem for a growing training transcript.

Verdict: retain the direct C.2 compiler as a substantive positive construction, and retain (13) as the precise unresolved innovation term. The obstacle is no longer that reduced mixers cannot be initialized without dense training. It is controlling the number, tail, and quadrature accuracy of the response-preserving sources required by the trained nonlinear flow.

## Scope, sources, and checks

This scoped author task read no other study or route output. Its scientific inputs were the assignment and maintained book. Required research/proof skills had already been read. The canonical-notation skill remained unavailable as previously disclosed; the explicit repository notation requirements and `docs/notation.qmd` were followed.

Complete relevant source units read:

- `docs/08-autonomous-computation.qmd`, C.1, physical lines 3394–3795: finite equations, metric, initialized marks, complete numerical statement, and explicit scope limitations. No outer convergence theorem is imported here.
- Same file, C.2, physical lines 3796–3970: complete Gaussian quadrature and adaptive-source initialization proof, including the core mixer identity.
- Same file, C.6, physical lines 4195–4295: complete resource counts and precision qualifications.
- `docs/12-three-sample-learning.qmd`, III.F.1–7, physical lines 316–728: complete fixed-program law, adaptive conditioning, response formulas, singular queries, feedback and joint action construction; read during this route's prior authorized task and reused.
- `docs/02-gaussian-reuse.qmd`, G.1–6, physical lines 4748–end: complete exact Gaussian replacement theorem and its stated application limits. Only the universal conditional-law distinction of G.1–3 is used here.
- `docs/index.qmd`, `docs/notation.qmd`, and the complete B.1/A.1 passages from the prior task remain the model and notation context.

Hashes at freeze:

| Source | SHA-256 |
| --- | --- |
| `docs/08-autonomous-computation.qmd` | `72224d6c545531a768e090ac24b681c58046de0a42b37105a9a6ad51316c8b54` |
| `docs/02-gaussian-reuse.qmd` | `a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92` |
| `docs/12-three-sample-learning.qmd` | `06d6e45f1d7d6c280fb0c5dcac3303b49d56bec4d4a7df632cd73af5091d1d15` |

HEAD: `3834145d910202a84824d943fe7d7f65714d96f2`; shared index empty on the metadata check. Author checks covered layer types, mean-loss factors, Gaussian covariance normalization, conditional rather than fresh independence, both trained and initialized connector parts, strict positivity of the new innovation, the bounded-fourth-derivative Taylor remainder, and the scope difference between two Euler steps and all-time GF. No machine verification or independent review is claimed.
