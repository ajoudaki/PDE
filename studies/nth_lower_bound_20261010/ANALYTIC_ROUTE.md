# Uniform analytic bounds for the frozen-top linear hierarchy

This is a scoped, author-derived proof for the study
`nth_lower_bound_20261010`. Its scientific inputs are the supervisor's
self-contained assignment and the additional derivative lower bound stated in
the final conditional application below. No other study files or established
book/code sources were used. The required proof, notation and repository process
instructions were read. A fresh scoped helper derived the polynomial endpoint
estimate used below. These are study results, not promoted material or an
independent promotion review.

The proof first bounds every ordered Lie derivative without a width factor.
Ordered time integrals then give a contraction for the prediction component of
every finite hierarchy on the same complex disk. Finally a Taylor truncation and
an elementary Chebyshev endpoint estimate convert a nonzero derivative into a
real-interval discrepancy. Retaining the factorial in that endpoint estimate
gives a stronger conclusion than the originally requested estimate.

## Model and the precise frozen-top convention

Fix a width \(n\ge1\). The parameter state is

\[
X=(B,W,c)\in
\mathbb R^{n\times2}\times\mathbb R^{n\times n}\times\mathbb R^n,
\qquad f_a(X)=c^\top WB e_a,\quad a\in\{1,2\},
\]

where \(e_a\in\mathbb R^2\) is the \(a\)-th coordinate vector. Both hidden
layers are linear. The loss and residuals are

\[
\mathcal L(X)=\frac14\sum_{a=1}^2(f_a(X)-y_a)^2,
\qquad r_a=f_a-y_a,
\qquad y=(y_0,0),\quad 0<y_0\le1.
\]

All parameter blocks use their Euclidean/Frobenius metric, and the dot denotes
the physical training time of this normalized metric. Thus, with

\[
V_a(X)=\nabla f_a(X)
 =\bigl(W^\top c e_a^\top,\;c(Be_a)^\top,\;WBe_a\bigr),
\]

the dense flow is

\[
\dot X=\frac12\sum_{b=1}^2(y_b-f_b(X))V_b(X).
\tag{1}
\]

Define the ordered hierarchy coefficients by

\[
K_{1,a}=f_a,\qquad
K_{s+1,a_1\ldots a_s b}=D K_{s,a_1\ldots a_s}[V_b],\qquad s\ge1.
\tag{2}
\]

In particular \(K_{2,ab}=\langle V_a,V_b\rangle\). No permutation symmetry
of the later indices is assumed. The order-\(q\) frozen-top hierarchy, for an
integer \(q\ge2\), stores \(f^{(q)}=K^{(q)}_1\) and tensors \(K^{(q)}_2,
\ldots,K^{(q)}_q\), initialized by their values at a common state \(X_0\).
Its equations are

\[
\begin{aligned}
\dot K^{(q)}_{s,a_1\ldots a_s}
 &=\sum_{b=1}^2K^{(q)}_{s+1,a_1\ldots a_s b}u^{(q)}_b,
 &&1\le s<q,\\
\dot K^{(q)}_q&=0,
&u^{(q)}_b&=\frac{y_b-f^{(q)}_b}{2}.
\end{aligned}
\tag{3}
\]

Assume throughout that

\[
c_0=0,\qquad \max\{\|B_0\|_{\mathrm{op}},\|W_0\|_{\mathrm{op}}\}\le4.
\tag{4}
\]

The proof is deterministic. Gaussian initialization is relevant only to the
separate probability of (4).

## Ordered derivatives have a dimension-free factorial bound

Complexify all parameter entries and all the preceding polynomial formulas.
The transpose in those formulas remains a transpose, not a conjugate transpose.
For estimates only, use Hermitian Euclidean norms and set

\[
\|X\|=\max\{\|B\|_{\mathrm{op}},\|W\|_{\mathrm{op}},\|c\|_2\}.
\]

Matrix multiplication, a transpose, a vector pairing and an outer product all
obey their usual product bounds in these norms, over the complex numbers as
well. In particular, for \(\|X\|\le s\),

\[
|f_a(X)|\le s^3,\quad
\|V_a(X)\|\le s^2,\quad
\|Df_a(X)\|\le3s^2,\quad
\|DV_a(X)\|\le2s.
\tag{5}
\]

For every integer \(k\ge0\) and every ordered sample sequence,

\[
\left|K_{k+1,a b_1\ldots b_k}(X)\right|
\le\frac{(k+2)!}{2}\,s^{k+3},\qquad \|X\|\le s.
\tag{6}
\]

To see this without dimension-dependent coordinate estimates, represent the
cubic scalar expression \(c^\top WB e_a\) as a product expression with three
variable leaves. Applying \(D[\,\cdot\,][V_b]\) to any expression of degree
\(d\) differentiates one of its \(d\) leaves. Replacing a \(B\), \(W\) or \(c\)
leaf by the corresponding component of \(V_b\) replaces that leaf with exactly
one product expression containing two variable leaves. Fixed coordinate
vectors, multiplication and transposes add no sum and have norm at most one.
The differentiated expression is therefore a sum of at most \(d\) expressions
of degree \(d+1\), each bounded by \(s^{d+1}\). Iteration from degree three gives
at most \(3\cdot4\cdots(k+2)=(k+2)!/2\) expressions of degree \(k+3\).
This also covers repeated terms: they may be counted separately. It proves
(6) with no dependence on \(n\).

At the initial state, (4) and (6) give

\[
\max_{a,b_1,\ldots,b_k}
|K_{k+1,a b_1\ldots b_k}(X_0)|
\le H_k:=32\,4^k(k+2)!,\qquad k\ge0.
\tag{7}
\]

The separate identity \(f_a(X_0)=0\) will remove the \(k=0\) term below.

## Exact integral representation of each finite hierarchy

For any analytic two-component function \(f\), put \(u_b=(y_b-f_b)/2\).
For a sample sequence \(b_1,\ldots,b_k\), define its ordered integral by

\[
I_{b_1\ldots b_k}[u](t)
=\int_0^t u_{b_1}(t_1)
  \int_0^{t_1}u_{b_2}(t_2)\cdots
  \int_0^{t_{k-1}}u_{b_k}(t_k)\,dt_k\cdots dt_2dt_1,
\tag{8}
\]

and set the empty integral to one. For complex \(t\), the nested integrals
may be taken along the straight segment from zero to \(t\); equivalently set
\(t_i=t\theta_i\) and integrate over
\(0\le\theta_k\le\cdots\le\theta_1\le1\). This produces an analytic
function. Repeated integration of (3) gives exactly

\[
f^{(q)}_a(t)
=\sum_{k=1}^{q-1}\sum_{b_1,\ldots,b_k=1}^2
K_{k+1,a b_1\ldots b_k}(X_0)
I_{b_1\ldots b_k}[u^{(q)}](t).
\tag{9}
\]

Conversely, if \(f\) satisfies (9) with its own \(u=(y-f)/2\), define

\[
K^{(q)}_{s,a_1\ldots a_s}(t)
=\sum_{k=0}^{q-s}\sum_{b_1,\ldots,b_k=1}^2
K_{s+k,a_1\ldots a_s b_1\ldots b_k}(X_0)
I_{b_1\ldots b_k}[u](t),\qquad 1\le s\le q.
\tag{10}
\]

Differentiating the outermost integral in (8) removes its first index and
produces \(u_{b_1}(t)\). Consequently (10) satisfies every equation in (3),
has the required initial conditions, and has \(K^{(q)}_1=f\). This establishes
the exact equivalence between (9) and the full finite hierarchy.

The first driving index in (8) occurs at the latest integration time. Reversing
the order of the indices in (9) without also reversing the coefficient
convention (2) would generally be incorrect. Every function in (9) uses the
closure's own residual in physical time; there is no replacement by a dense
residual clock or by a common endpoint in a different clock.

## A common complex disk for every hierarchy order

Let

\[
R_0=\frac1{4096},\qquad R=\frac{R_0}{2}=\frac1{8192}.
\tag{11}
\]

Use the Banach space of two-component functions continuous on the closed disk
\(|t|\le R_0\) and analytic on its interior, with norm
\(\|f\|_\infty=\max_a\sup_{|t|\le R_0}|f_a(t)|\). On its closed unit
ball, the residual vector obeys

\[
\sum_{b=1}^2|u_b(t)|
\le\frac12\sum_b(|y_b|+|f_b(t)|)\le2.
\tag{12}
\]

The actual bound is at most \(3/2\), but two is convenient. Let
\(\Phi_q(f)\) denote the right-hand side of (9). By the ordered simplex's
volume \(1/k!\), (7), (8) and (12),

\[
\begin{aligned}
\|\Phi_q(f)\|_\infty
&\le32\sum_{k=1}^{q-1}(k+1)(k+2)(8R_0)^k\\
&\le64\bigl[(1-8R_0)^{-3}-1\bigr]<0.38.
\end{aligned}
\tag{13}
\]

For two functions in this unit ball, their residual vectors satisfy
\(\sum_b|u_b-v_b|\le\|f-g\|_\infty\). Expanding a difference of \(k\)
factors into \(k\) terms in (8) therefore gives

\[
\begin{aligned}
\|\Phi_q(f)-\Phi_q(g)\|_\infty
&\le16\sum_{k=1}^{\infty}k(k+1)(k+2)(8R_0)^k
     \|f-g\|_\infty\\
&=\frac{96(8R_0)}{(1-8R_0)^4}\|f-g\|_\infty
<0.2\|f-g\|_\infty.
\end{aligned}
\tag{14}
\]

Here \(8R_0=1/512\), and the series identities follow by differentiating the
geometric series. Thus the contraction theorem gives one fixed point in the
unit ball for every \(n\ge1\) and every \(q\ge2\). Formula (10) supplies its
full hierarchy state. A polynomial finite-dimensional ODE has unique local
solutions, which can also be seen directly by the local Lipschitz bound for
its vector field, so this fixed point is the analytic continuation of the
specified frozen-top trajectory. In particular,

\[
\max_a|f^{(q)}_a(t)|\le1\qquad(|t|\le R_0),
\tag{15}
\]

uniformly in \(n,q,X_0,y_0\) under (4) and \(0<y_0\le1\). The statement on
the smaller closed disk \(|t|\le R\) has an open neighborhood of analyticity.
No uniform bound on the individual high-order stored tensors is claimed or
needed.

## The dense trajectory on the same disk

Let \(G(X)\) be the right-hand side of (1). On the unit ball about \(X_0\)
in the parameter norm, \(\|X\|\le5\). Formula (5) gives

\[
\|G(X)\|\le(1+5^3)5^2=3150,
\qquad \|DG(X)\|\le3\cdot5^4+2\cdot5(1+5^3)=3135.
\tag{16}
\]

The Picard map \(X(t)\mapsto X_0+\int_0^tG(X(z))\,dz\), on continuous
closed-disk functions analytic in the interior and within distance one of
\(X_0\), maps that ball into itself and has Lipschitz constant at most
\(3135R_0<1\), since \(3150R_0<1\). It therefore supplies the dense
trajectory on \(|t|\le R_0\), with \(\|X(t)\|\le5\).

To bound its outputs by one as well, observe from (6) with \(k=1\) that

\[
|K_{2,ab}(X(t))|\le3\cdot5^4=1875.
\]

Fix any ray \(t=\rho e^{i\theta}\), \(0\le\rho\le R_0\), and set
\(F(\rho)=\max_a|f_a(X(\rho e^{i\theta}))|\). The output equation from
(1) and \(f_a(X_0)=0\) gives

\[
F(\rho)\le1875\int_0^\rho(1+F(s))\,ds.
\]

Iteration of this integral inequality, or the scalar differential inequality
for its right-hand side, gives

\[
F(\rho)\le e^{1875\rho}-1\le e^{1875/4096}-1<1.
\tag{17}
\]

The factor \(e^{i\theta}\) in the differentiated ray parameter has modulus
one and hence introduces no change. Equations (15) and (17) prove the promised
uniform statement: every dense and frozen-top output is holomorphic on
\(|t|<R_0\), and bounded by one on the closed disk \(|t|\le R\), independently
of both \(n\) and \(q\). Each component of their difference is bounded by two.

## Derivatives force a real-interval discrepancy

Here is a scalar analytic estimate with explicit dependence. Suppose \(g\) is
holomorphic on a neighborhood of \(|z|\le R\), is bounded there by \(M>0\),
and for an integer \(j\ge1\) satisfies

\[
|g^{(j)}(0)|\ge a^j,\qquad a>0.
\tag{18}
\]

There is a constant \(C=C(R,M,a)\), independent of \(j\) and \(g\), such that

\[
\sup_{0\le t\le R/4}|g(t)|
\ge\exp\{-j\log j-2j\log\log(ej)-Cj\}.
\tag{19}
\]

This implies the requested weaker estimate with \(-2j\log j\). No sign
condition on \(g\) or on its derivative is required.

For completeness, we derive the polynomial endpoint estimate used to prove
(19). For a complex polynomial \(P\) of degree at most \(N\ge j\), set
\(p(x)=P(R(x+1)/8)\). Expand it in the Chebyshev polynomials,

\[
p(x)=\sum_{k=0}^N\alpha_kT_k(x),\qquad
T_k(\cos\theta)=\cos(k\theta).
\]

Cosine orthogonality gives

\[
\alpha_k=\frac2\pi\int_0^\pi
p(\cos\theta)\cos(k\theta)\,d\theta,
\qquad |\alpha_k|\le2\|p\|_{[-1,1]},\quad k\ge1.
\tag{20}
\]

Differentiating the defining cosine identity gives the differential equation
\((1-x^2)T_k''-xT_k'+k^2T_k=0\). Differentiating that equation \(r\) times
and evaluating at one yields

\[
T_k^{(r+1)}(1)=\frac{k^2-r^2}{2r+1}T_k^{(r)}(1).
\]

Starting from \(T_k(1)=1\), and using parity for the other endpoint, gives

\[
|T_k^{(j)}(-1)|
=\prod_{r=0}^{j-1}\frac{k^2-r^2}{2r+1}
\le\frac{k^{2j}}{j!},\qquad 1\le j\le k,
\tag{21}
\]

because \(2r+1\ge r+1\). The derivative is zero for \(j>k\). Therefore
(20), (21) and the affine change of variables imply

\[
|P^{(j)}(0)|
\le\frac{2N}{j!}\left(\frac{8N^2}{R}\right)^j
\|P\|_{[0,R/4]}.
\tag{22}
\]

This proof works for complex coefficients; it does not use a real-valued
polynomial Markov inequality without checking its complex extension.

Now put

\[
A=\frac{aR}{8},\quad b=\max\{0,\log(1/A)\},\quad
d=\max\{0,\log(4M/3)\},\quad K=32(1+b+d),
\]

and, for the given \(j\), set

\[
L=\log(ej),\qquad N=\lceil KjL\rceil.
\]

Let \(P_N\) be the Taylor polynomial of \(g\) at zero of degree \(N\).
Cauchy's coefficient bound yields

\[
\|g-P_N\|_{[0,R/4]}
\le M\sum_{k=N+1}^{\infty}4^{-k}
=\frac M3\,4^{-N}.
\tag{23}
\]

Since \(N\ge j\), \(P_N^{(j)}(0)=g^{(j)}(0)\) exactly. If
\(S=\|g\|_{[0,R/4]}\), (18), (22) and (23) give

\[
S\ge\frac{A^j j!}{2N^{2j+1}}-\frac M3\,4^{-N}.
\tag{24}
\]

We check that the remainder is small enough uniformly down to \(j=1\).
Since \(N\le2KjL\) and \(L\le j\),

\[
\begin{aligned}
j\log(1/A)+(2j+1)\log N+\log(4M/3)
&\le j\{b+d+3\log(2K)+6\log j\}\\
&\le jL\{b+d+3\log(2K)+6\}\\
&\le KjL\log4\le N\log4.
\end{aligned}
\tag{25}
\]

For the penultimate inequality, set \(D=1+b+d\ge1\). Its bracket is
\(D+5+3\log(64D)\le4D+20\le24D<32D\log4=K\log4\), using
\(\log64<6\) and \(\log D\le D-1\). Exponentiating (25) gives

\[
\frac M3\,4^{-N}\le\frac{A^j}{4N^{2j+1}}
\le\frac{A^j j!}{4N^{2j+1}}.
\]

Consequently (24) implies

\[
S\ge\frac{A^j j!}{4N^{2j+1}}
\ge\frac{A^j j!}{4(2KjL)^{2j+1}}.
\tag{26}
\]

Finally, \(\log(j!)\ge\int_1^j\log x\,dx\ge j\log j-j\), and
\(\log j+\log L\le2j\). Taking logarithms in (26) proves (19), for
example with

\[
C=b+3\log(2K)+3+\log4.
\tag{27}
\]

Thus (19) is uniform over any family sharing \(R,M,a\), even if both the
analytic function and the differentiated order depend on width.

## Conditional application to a first unmatched derivative

The following paragraph uses a derivative estimate supplied by the supervisor;
its algebraic derivation is outside this scoped analytic proof. Suppose that,
on an initialization event contained in (4), the discrepancy

\[
g_{n,q}(t)=f^{\mathrm{dense}}_{n,1}(t)-f^{(q)}_{n,1}(t)
\]

satisfies, at an order \(j=j(q)\ge1\),

\[
|g_{n,q}^{(j)}(0)|\ge\frac18\left(\frac{y_0}{2}\right)^j.
\tag{28}
\]

For a fixed target \(y_0>0\), (28) implies (18) with \(a=y_0/16\), since
\(8^{-1}\ge8^{-j}\). The analytic bound above supplies \(R=1/8192\) and
\(M=2\). Hence, on the same event and simultaneously for all applicable
orders,

\[
\sup_{0\le t\le1/32768}|g_{n,q}(t)|
\ge\exp\{-j\log j-2j\log\log(ej)-C(y_0)j\}.
\tag{29}
\]

If that event has probability tending to one, \(j(q)=q+O(1)\), and a
deterministic sequence \(q_n\) achieves

\[
\sup_{0\le t\le1/32768}|g_{n,q_n}(t)|=O_{\mathbb P}(n^{-1/2}),
\]

then necessarily

\[
\liminf_{n\to\infty}\frac{q_n\log q_n}{\log n}\ge\frac12.
\tag{30}
\]

Indeed, bounded \(q_n\) along a subsequence contradicts the positive constant
lower bound (29). Along any subsequence with \(q_n\to\infty\) and
\(q_n\log q_n\le(1/2-\varepsilon)\log n\), the additional terms
\(2j\log\log(ej)+Cj\) are \(o(j\log j)\). Thus (29) times \(\sqrt n\)
diverges on events of probability tending to one, contradicting tightness.

The target must be fixed, or bounded below by a positive constant, for this
uniform constant. A vanishing target \(y_0=y_0(n)\) changes the bound through
\(C(y_0)\). Equation (29) is a supremum on a physical-time interval; it does
not identify the discrepancy at a prescribed final time, prove a matching
upper bound, establish a nonlinear-activation result, or constrain other
possible reduced models.

## Contributor and check record

The analytic author was agent \(\texttt{/root/nth\_lower\_analytic\_check}\).
Its assigned scientific input was the prompt defining (1)--(4), the requested
ordered-derivative and analytic estimates, and the supervisor's later statement
of (28). The author inspected no other scientific files. A metadata-only agent
listing incidentally displayed a completed scalar-route summary from the same
study; none of that summary is used in this proof. Thus this is not represented
as an isolated blind review of the scalar route or of the complete study.

Agent \(\texttt{/root/nth\_lower\_analytic\_check/sup\_lemma}\) was created with
no inherited conversation. Its complete scientific assignment was to prove the
analytic derivative-to-real-supremum implication from fixed \(R,M,a\), first
targeting the weaker coefficient two in front of \(j\log j\). It derived the
Chebyshev expansion, endpoint derivative product and explicit tail comparison
(20)--(25) without scientific retrieval. The analytic author then proposed
retaining the denominator bound \(\prod_{r=0}^{j-1}(2r+1)\ge j!\); the helper
independently checked the strengthened polynomial estimate, the unchanged tail
comparison and the \(j=1\) case. It also checked the monomial family
\(g_j(z)=a^jz^j/j!\), whose real supremum is
\(\exp\{-j\log j+O(j)\}\), so coefficient one is asymptotically sharp under
the scalar analytic assumptions, apart from the lower-order logarithmic term.
This helper check covers the analytic scalar lemma, not the dense or hierarchy
construction and not the supervisor-supplied derivative estimate (28).

The analytic author checked the finite hierarchy's \(q=2\) case directly:
(9) reduces to
\(f_a(t)=\sum_bK_{2,ab}(X_0)\int_0^tu_b(s)\,ds\), whose derivative is
precisely (3) with constant \(K_2\). The same outer-integral differentiation
proves (10) for arbitrary \(q\), with the displayed order of indices.

On 2026-10-10, direct arithmetic verification used
\(\texttt{awk}\) to evaluate (13), (14), (16) and (17) at \(R_0=1/4096\).
The values were respectively \(0.376470\), \(0.188972\), dense displacement
\(0.769043\), dense Lipschitz constant \(0.765381\), and dense output bound
\(0.580535\), all within their stated thresholds. The symbolic formulas in
the proof, rather than these rounded numbers, establish the inequalities.

For the supervisor's explicit specialization \(\eta=y_0\), arithmetic gives
\[
A=\frac{aR}{8}=\frac{\eta}{2^{20}},\qquad
K=32\left[1+\log\!\left(\frac{2^{20}}{\eta}\right)+\log(8/3)\right],
\quad N=\lceil Kj\log(ej)\rceil.
\]
Equation (26) therefore gives the completely explicit lower bound
\[
\sup_{0\le t\le1/32768}|g_{n,q}(t)|
\ge\frac{j!(\eta/2^{20})^j}{4N^{2j+1}},
\]
conditional only on (4) and (28). The state assumptions, residual factors,
complex transposes, simplex factorials and endpoint time interval were checked
in the author's final mathematical audit. The stronger claim that (28) holds
for the network remains assigned to its algebraic derivation elsewhere.
