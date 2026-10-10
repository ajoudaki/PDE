# Published NTH scope and the proposed width lower bound

Date: 2026-10-10. Scoped source assessment; no experiments, Git operations, other-study inputs, or maintained-book changes.

## Finding

The published Huang–Yau theorem provides a fixed-order upper bound in its native parameterization, with Gaussian initialization and its specified data and regularity hypotheses. For fixed data, depth, finite physical time, and fixed positive error tolerance, that bound makes order two sufficient as width grows. Thus, **at the level of the published theorem**, an exponential-in-width lower bound cannot hold for its same-realization training-prediction problem on the theorem's good initialization event. This addresses every fixed admissible problem satisfying the hypotheses, not merely an easy activation example.

That statement does **not** refute an existential hard-instance lower bound for zero-readout μP feature learning. It also does not cover arbitrary initializations, growing data/time/depth/regularity constants, or unrestricted test queries. The algebraic existence of an NTH is broader than the scope of this approximation theorem. A storage lower bound must specify which of these scopes it uses.

This report verifies the source statements and provides an elementary conditional finite-time consequence below. It does not certify the entire external proof or its heavy dependencies as a new internally checked theorem.

## Inputs and notation

I read the complete [ICML 2020 paper](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf), including its technique overview, discussion, and references, and the complete [arXiv v1 manuscript](https://arxiv.org/pdf/1909.08156v1), including Appendices A–C. The published paper's theorem uses separate \(p\) and \(p^*\); the arXiv proof version uses a single \(p\) for both roles. The [PMLR record](https://proceedings.mlr.press/v119/huang20l.html) links the paper but no separate supplement. Shared workflow and the canonical-notation, rigorous-math, and conjecture-audit instructions were also read. No current-book scientific material or other study was an input to this scoped assignment.

| Quantity | Huang–Yau | This report/user convention |
|---|---:|---:|
| Hidden width | \(m\) | \(n\) |
| Training sample count | \(n\) | \(m\) |
| Hidden depth | \(H\) | \(L\) |
| Truncation order | \(p\) | \(q\) |
| Fixed regularity/order ceiling | \(p^*\) | \(q_*\) |
| Activation | \(\sigma\) | \(\phi\) |
| Output weights | \(a\) | \(W^{(L+1)}\in\mathbb R^n\) |

For \(x_a\in\mathbb R^d\), define \(h_a^{(0)}=x_a\),

\[
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\frac1{\sqrt n}\phi(z_a^{(\ell)}),
\qquad
f_a=W^{(L+1)\top}h_a^{(L)},\quad 1\le\ell\le L.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\) and \(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\). This is the source's parameterization, not the μP forward pass. With parameter vector \(\theta\), residual \(r_a=f_a-y_a\), and loss

\[
\mathcal L(\theta)=\frac1{2m}\sum_{a=1}^m r_a^2,
\qquad \dot\theta=-\nabla_\theta\mathcal L,
\]

all source parameter blocks have unit mobility in this physical clock. Source initialization has independent Gaussian weight entries with fixed variances, including the random output vector. The proof treats the output vector as a nondegenerate Gaussian input. A degenerate zero-variance specialization is not separately established there; in any case, this does not supply μP's different parameter mobilities.

The exact kernels are defined recursively by

\[
K^{(2)}(x_a,x_b;\theta)
=\langle\nabla_\theta f_a,\nabla_\theta f_b\rangle,
\qquad
K^{(s+1)}(x_{a_1},\ldots,x_{a_s},x_b;\theta)
=\langle\nabla_\theta K^{(s)}(x_{a_1},\ldots,x_{a_s};\theta),
\nabla_\theta f_b\rangle.
\]

Consequently,

\[
\dot r_a=-\frac1m\sum_b K_t^{(2)}(x_a,x_b)r_b,
\qquad
\dot K_t^{(s)}(x_{a_1},\ldots,x_{a_s})
=-\frac1m\sum_b K_t^{(s+1)}(x_{a_1},\ldots,x_{a_s},x_b)r_b.
\]

These identities are exact by the chain rule. The truncated NTH evolves the analogous quantities through order \(q-1\), freezes \(\widetilde K_t^{(q)}=K_0^{(q)}\), and starts from the **same realized** initial \(f_0,K_0^{(2)},\ldots,K_0^{(q)}\).

## Exact published assumptions and bound

The source's Assumptions 2.1–2.2 require:

1. A smooth activation with \(\sup_{u\in\mathbb R}|\phi^{(s)}(u)|\le C_s\) for \(1\le s\le2q_*+1\). These are fixed finite-order derivative bounds. There is no bound on \(\phi\) itself and no complex analyticity requirement.
2. Fixed lower and upper bounds on \(\|x_a\|_2\). For every set of \(s\) distinct training inputs, \(1\le s\le2q_*+1\), the smallest singular value of their column matrix is at least \(c_s>0\). The constants are independent of width. In particular, the relevant subsets must be linearly independent; when all \(m\) inputs are among these subset sizes, this requires \(d\ge m\).
3. For Theorem 2.6, even \(2\le q\le q_*\), and \(\lambda_{\min}(K_0^{(2)})\ge\lambda>0\). Depth and the displayed derivative/data constants are treated as fixed, without explicit dependence tracking.

There is no separate numbered bounded-label assumption. The proof nevertheless uses \(\sum_a|f_a(0)-y_a|^2=O(m)\) in Appendix B.1. Fixed uniformly bounded labels, including \(y_a=\eta\) for fixed \(\eta\), are compatible with its intended scale. For an exact finite-confidence statement the initial residual bound should be retained explicitly; fixed-data Gaussian initial outputs are random variables with nonvanishing variance, not deterministically bounded numbers.

The published Theorem 2.6, equations (17)–(19), states the following bound after the notation translation above:

\[
t\le\min\left\{
\frac{c\sqrt{\lambda n/m}}{(\log n)^C},\quad
\frac{n^{q_*/[2(q_*+1)]}}{(\log n)^{C'}}
\right\},
\]

\[
\|f(t)-\widetilde f(t)\|_2
\lesssim
\frac{(1+t)t^{q-1}\sqrt m}{n^{q/2}}
\min\left\{t,\frac m\lambda\right\},
\]

\[
\|K_t^{(2)}-\widetilde K_t^{(2)}\|_{\max}
\lesssim
\frac{(1+t)t^{q-1}}{n^{q/2}}
\left[
1+\frac{(1+t)t(\log n)^C}{n}
\min\left\{t,\frac m\lambda\right\}
\right].
\]

Here \(\|A\|_{\max}=\max_{a,b}|A_{ab}|\). The paper displays no leading logarithm in these two errors; this report has preserved that display exactly rather than silently changing it. The estimates rely on the random-initialization event supporting Theorem 2.3. The source defines “high probability” as probability at least \(1-\exp(-n^c)\); the dependence of all constants and this confidence convention are part of the external result, not newly established here.

The literal tensor implementation stores at most

\[
m+\sum_{s=2}^{q}m^s
\]

real coordinates, counting the frozen top-order array as storage. For \(q=2\), it stores \(m\) evolving outputs and \(m^2\) fixed kernel entries. This is polynomial in the sample count for every fixed \(q\), independent of width after the realized initial coefficients have been computed. Forming those coefficients from the network has a separate cost and does not provide a free initialization algorithm.

For fixed \(m,L,T,\lambda\), fixed activation/data constants, and fixed error tolerance, the displayed \(q=2\) bound tends to zero as \(n\to\infty\), and the allowed horizon eventually includes \([0,T]\). An \(\exp(cn)\) necessary-storage assertion on this precise native problem would contradict that upper bound. An \(O(m^q)\) array count alone is not an exponential-in-width lower bound: such a claim needs a necessary order \(q(n)\), sample growth, a norm/tolerance, and the relevant initialization quantifier.

The theorem does not track constants as \(q\to\infty\). Its “arbitrary precision” discussion must not be promoted into uniform order convergence at fixed width without controlling \(C_s,c_s\), depth, and the theorem constants. Its main statement requires even \(q\), despite a subsequent illustrative paragraph mentioning \(p=3\).

## A complete finite-time implication, conditional only on kernel drift

This elementary implication avoids the positive-eigenvalue assumption and isolates the exact external input needed for the fixed-horizon storage conclusion.

Suppose a differentiable network follows the loss and flow above on \([0,T]\), its initial residual satisfies \(\|r(0)\|_2\le R\sqrt m\), and

\[
\|\dot K_t^{(2)}\|_{\max}\le\frac{B_n}{n}(1+t)
\quad(0\le t\le T).
\]

Let \(\widetilde r'=-K_0^{(2)}\widetilde r/m\) and \(\widetilde r(0)=r(0)\), the order-two truncated NTH. Then

\[
\sup_{0\le t\le T}
\frac{\|r(t)-\widetilde r(t)\|_2}{\sqrt m}
\le\frac{RB_n}{n}\left(\frac{T^2}{2}+\frac{T^3}{6}\right).
\]

Proof. The Gram matrix \(K_t^{(2)}\) is positive semidefinite. Hence

\[
\frac d{dt}\|r(t)\|_2^2=-\frac2m r(t)^\top K_t^{(2)}r(t)\le0.
\]

Integration of the assumed drift gives

\[
\|K_t^{(2)}-K_0^{(2)}\|_{\max}
\le\frac{B_n}{n}\left(t+\frac{t^2}{2}\right).
\]

For \(e=r-\widetilde r\), subtracting the two equations yields

\[
\dot e=-\frac1mK_0^{(2)}e
-\frac1m(K_t^{(2)}-K_0^{(2)})r,\qquad e(0)=0.
\]

Because \(K_0^{(2)}\) is positive semidefinite, its exponential has operator norm at most one. Variation of constants and \(\|A\|_{2\to2}\le m\|A\|_{\max}\) now give

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le R\int_0^t\|K_s^{(2)}-K_0^{(2)}\|_{\max}\,ds
\le\frac{RB_n}{n}\left(\frac{t^2}{2}+\frac{t^3}{6}\right).
\]

This proves the claim. Corollary 2.4 supplies a published drift input \(B_n\lesssim(\log n)^C\) on its event and horizon; accepting that input yields convergence for every fixed \(T\), even when the initial kernel is singular. The implication itself is fully derived here, whereas obtaining that drift from the random network remains the source-dependent step. It controls root-mean-square training prediction error; unnormalized \(\ell^2\) error has an extra factor \(\sqrt m\).

## Passive test queries

The paper describes a passive-query extension in equation (22), but its training theorem is not itself a stated uniform test-domain error theorem. For a fixed query \(x\), the truncated hierarchy adds kernels with one query argument and the remaining arguments among the training samples. Literal storage is \(1+\sum_{s=2}^q m^{s-1}\) per query. No query residual is added to the training loss.

A precise order-two extension follows from the same calculation. Set \(k_t=(K_t^{(2)}(x,x_a))_{a=1}^m\), and assume separately

\[
\|\dot k_t\|_\infty\le\frac{B_{x,n}}n(1+t),\qquad
\frac{\|k_0\|_2}{\sqrt m}\le\kappa_x.
\]

Initialize \(\widetilde f_x(0)=f_x(0)\) and evolve \(\dot{\widetilde f}_x=-k_0^\top\widetilde r/m\). Subtracting from \(\dot f_x=-k_t^\top r/m\) and integrating gives

\[
|f_x(t)-\widetilde f_x(t)|
\le\frac{R}{n}\left[
B_{x,n}\left(\frac{t^2}{2}+\frac{t^3}{6}\right)
+\kappa_x B_n\left(\frac{t^3}{6}+\frac{t^4}{24}\right)
\right].
\]

Indeed, the derivative difference is \(-(k_t-k_0)^\top r/m-k_0^\top e/m\); Cauchy–Schwarz, the residual bound, and the preceding training bound yield exactly these two integrals. Thus a finite predetermined query set is compatible with small storage **if its mixed-kernel drift is available**. The training theorem alone does not verify that additional estimate, especially for arbitrary or adaptive queries. Preserving the full initial network to produce coefficients for later queries also has its own polynomial-in-width storage cost.

## Random readout and dense-to-dense comparisons

Conditional on the initial hidden weights,

\[
f_a(0)\sim\mathcal N\!\left(0,\sigma_a^2\|h_a^{(L)}(0)\|_2^2\right).
\]

If two native networks share their hidden weights but have independent output vectors, their output difference has conditional variance

\[
2\sigma_a^2\|h_a^{(L)}(0)\|_2^2.
\]

On a nondegenerate activation/input instance this is order one. Native outputs therefore do not concentrate around one deterministic prediction at rate \(n^{-1/2}\). The source's \(n^{-1/2}\) scale concerns empirical kernel fluctuations around a deterministic limiting kernel, with other conditions as stated in Theorem 2.3. Its truncation theorem compares the **same initial realization**, with \(\widetilde f(0)=f(0)\); it does not compare independently initialized networks. Consequently, an observed order-one dense-to-dense discrepancy under independent random readouts is not a lower bound on truncation error. Zero readout sets \(f(0)=0\) exactly, but does not by itself prove any later dense-to-dense fluctuation rate.

## Activation and correlated-data admissibility

Smoothness with finitely many bounded positive-order derivatives is weaker than bounded holomorphic extension to a complex strip. If \(\phi\) is holomorphic and bounded by \(M\) on \(\{|\operatorname{Im}z|<\rho\}\), Cauchy's formula on each real-centered circle of radius \(\rho/2\) gives

\[
|\phi^{(s)}(u)|\le M s! (2/\rho)^s,
\]

so it supplies each required finite-order derivative bound. Holomorphy on a strip alone supplies no uniform bound over the entire real axis. Conversely, the source's smoothness assumptions do not imply analyticity or any controlled growth of derivative constants with order. The identity activation \(\phi(u)=u\) satisfies every source derivative condition: \(\phi'=1\) and all higher derivatives vanish. It is entire, but it is not bounded on an infinite strip. Thus its admission into a separate strip-analytic class depends on whether that class also requires bounded activation values.

For the proposed family in \(d=m+1\), let \(e_0,e_1,\ldots,e_m\) be the standard orthonormal basis and define

\[
x_a=\frac{e_0+e_a}{\sqrt2},\qquad y_a=\eta,
\quad 1\le a\le m,
\]

with fixed \(\eta\). Each input has norm one and distinct inputs have inner product \(1/2\). A matrix formed from any \(s\) distinct columns has Gram matrix

\[
\frac12(I_s+\mathbf1_s\mathbf1_s^\top).
\]

Its eigenvalues are \((s+1)/2\) in the all-ones direction and \(1/2\) on the orthogonal complement. The smallest singular value is therefore \(1\) for \(s=1\) and \(1/\sqrt2\) for \(s\ge2\). Assumption 2.2 is satisfied uniformly in sample count at every available subset size. This verifies the activation/data/label scale; it does not verify the separate initial-kernel eigenvalue condition for a different parameterization, nor does it move a μP construction into the native theorem.

Jointly growing \(m=m(n)\) changes the question. The native upper contains sample and spectral factors, and literal array storage is \(m(n)^q\). An asserted lower such as \(\exp(c\log m\log n)\) therefore requires its own order/error argument; neither admissibility of this dataset nor failure of a fixed-data argument establishes it.

## Proof-dependency status and limits of this assessment

The source's dependency chain is: initial Gaussian conditioning/concentration (Appendix A, with a conditioning lemma imported from Yang's tensor-program work); norm and higher-order-vector control (Appendix B, also using random-matrix bounds); then the kernel-drift and truncation comparisons (Appendix C). I read this entire chain in the arXiv manuscript, but did not retrieve or independently reconstruct Yang's full theorem or the random-matrix reference. Accordingly, the native neural-network upper is retained as a published result, not marked internally checked here.

There are visible steps requiring further work before using this manuscript as a complete self-contained imported proof. Appendix B.3 passes from first-derivative norm inequalities to higher derivatives of their maxima in (B.29); differentiation of inequalities and nonsmooth maxima needs a separate justification. Appendix C's top-order forcing estimate drops the logarithm present in (C.16), and using (C.14) at its top odd order calls for one more kernel estimate than the explicitly displayed range in the single-order arXiv statement. The published split between \(p\) and \(p^*\) can provide additional order room when \(p<p^*\), but is not itself a supplied revised appendix proof. These are narrowly identified audit obligations, not a conclusion that the theorem is false. The elementary conditional result above avoids these steps entirely.

For the requested lower-bound discussion, the reliable distinction is therefore:

- A published native fixed-order upper is directly relevant to a native, fixed-data, fixed-horizon, same-realization, high-probability lower claim.
- That upper does not refute a hard-instance claim quantified over a different μP/zero-readout flow, growing data, exceptional initializations, or additional test-query requirements.
- One hard activation/dataset can suffice for a worst-case lower, but an easy example cannot refute that existential claim. A refuting upper must cover every candidate in the exact asserted class, and its initialization and error quantifiers must match.

Source files retained in `data/generated/nth_lower_bound_20261010/native_scope_sources/`:

- `huang20l.pdf`, SHA-256 `2aaddce00cf459fab7408b28fbca555b951a5d1521ceabc205c7e05ac254ceeb`.
- `huang_yau_arxiv_v1.pdf`, SHA-256 `2036ab63a3e9ff20fa04c3f8d137dae385b9ba743b41a35aed1a92143e5fc91c`.

The corresponding layout-text extractions were used for complete reads. No numerical training or empirical validation was performed.
