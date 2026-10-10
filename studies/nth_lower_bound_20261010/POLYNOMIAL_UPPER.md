# A polynomial retained-array upper bound for the same linear witness

This scoped proof concerns exactly the two-input, two-hidden-layer linear
witness of [RESULT.md](RESULT.md), with its Euclidean metric normalization and
frozen-top hierarchy. It proves a full-trajectory upper bound for that hierarchy
and compares it with the actual discrepancy of two independent dense networks.
A superpolynomial retained-array lower bound therefore cannot hold for this
witness. This is not an upper bound for arbitrary activations, label sizes,
depths or training-panel sizes.

The scientific inputs used were the complete current RESULT.md, the author's
complete [ANALYTIC_ROUTE.md](ANALYTIC_ROUTE.md), and the supervisor's scoped
assignment. No other scientific files or external sources were consulted.
This is an author-derived study result, not promoted material or an independent
promotion review.

## Statement

Let \(B\in\mathbb R^{n\times2}\), \(W\in\mathbb R^{n\times n}\),
\(c\in\mathbb R^n\), and
\[
f_a=c^\top WB e_a,\qquad
\mathcal L=\frac14\{(f_1-\eta)^2+f_2^2\},\qquad c_0=0.
\]
The flow uses the Euclidean/Frobenius metric in these coordinates. Assume
\[
\frac12I\preceq B_0^\top B_0\preceq2I,\qquad
\|W_0\|_{\mathrm{op}}\le4,\qquad
\sigma_{\min}(W_0B_0)\ge\frac34.                 \tag{1}
\]
For this upper bound it is enough that \(0<\eta\le10^{-8}\).
The current witness uses \(0<\eta\le10^{-62}\).

Simultaneously for every integer \(q\ge2\), the order-\(q\) frozen-top NTH
exists for all physical times, converges to the same fitted predictor as the
dense network, and satisfies
\[
E_n(q):=\sup_{t\ge0}\|f^{(q)}(t)-f(t)\|_2
\le24576\,\eta(128\eta)^{q-1}.                  \tag{2}
\]
This norm equals the whole normalized input-sphere error, since both
predictions are linear in the input.

For independent Gaussian initializations, put
\[
D_n=\sup_{t\ge0}\|f(t)-\widetilde f(t)\|_2,\quad
R=\frac1{8192},\quad c_\eta=\frac{\eta^2R^2}{128}.
\]
For \(n\ge2\), with the absolute constants \(c,C>0\) of the initialization
event in RESULT,
\[
\Pr\{D_n\ge c_\eta n^{-4}\}
\ge1-\frac{8+2e}{n}-C e^{-cn}.                 \tag{3}
\]
Put \(\rho=128\eta<1\) and choose
\[
q_n=\max\left\{2,\,
1+\left\lceil
\frac{5\log n+\log(3\cdot2^{46}/\eta)}
     {\log(1/\rho)}
\right\rceil\right\}.                         \tag{4}
\]
Then, on an event of probability at least
\(1-(8+2e)/n-Ce^{-cn}\),
\[
E_n(q_n)\le c_\eta n^{-5}\le D_n/n.            \tag{5}
\]
The explicit retained tensor arrays have
\[
2+\sum_{r=2}^{q_n}2^r=2^{q_n+1}-2
\le C_\eta n^\alpha,\qquad
\alpha=\frac{5\log2}{\log(1/(128\eta))}.         \tag{6}
\]
In the actual witness range \(\eta\le10^{-62}\), \(\alpha<1/20\).
This counts retained arrays after initialization, not the cost of generating
their coefficients or the original dense network's parameter storage.
The additive storage of the dense parameters is \(O(n^2)\), also polynomial;
no bound on the total setup memory or time for coefficient generation is claimed.

## 1. Kernel as a functional of a residual path

Write \(y=(\eta,0)\), \(r=f-y\), and \(u=-r/2\). Define
\[
K_{1,a}=f_a,\quad
K_{s+1,a_1\ldots a_s b}=D K_{s,a_1\ldots a_s}[V_b],
\quad
V_b=(W^\top c e_b^\top,\;c(Be_b)^\top,\;WBe_b).
\]
For a two-component control \(u\), define its action and ordered integrals by
\[
A_u(t)=\int_0^t\sum_b|u_b(s)|\,ds,\qquad
I_{b_1\ldots b_k}[u](t)=
\int_{0\le t_k\le\cdots\le t_1\le t}
\prod_{i=1}^k u_{b_i}(t_i)\,dt_k\cdots dt_1.
\]
The empty integral is one. After absolute values the scalar integrand is
symmetric, so
\[
\sum_{b_1,\ldots,b_k}|I_{b_1\ldots b_k}[u](t)|
\le A_u(t)^k/k!.                              \tag{7}
\]
ANALYTIC_ROUTE's dimension-free product-expression bound gives
\[
\max_{a,b,b_1,\ldots,b_k}
|K_{k+2,ab b_1\ldots b_k}(X_0)|
\le128\,4^k(k+3)!,\qquad k\ge0.               \tag{8}
\]
For \(q\ge2\), define
\[
\mathcal K_q[u]_{ab}(t)=
\sum_{k=0}^{q-2}\sum_{b_1,\ldots,b_k}
K_{k+2,ab b_1\ldots b_k}(X_0)
I_{b_1\ldots b_k}[u](t),                      \tag{9}
\]
and denote the infinite counterpart by \(\mathcal K_\infty[u]\).
Repeated integration of the finite hierarchy shows that its actual kernel
equals \(\mathcal K_q[u^{(q)}]\), using its own residual. The first index of
each driving sequence occurs at the latest integration time.

The first two tensor slots are symmetric: \(K_2\) is a symmetric Gram matrix
and further directional derivatives preserve that symmetry. Thus (9) is a
real symmetric matrix for every real path. No symmetry in later slots is used.

The operator norm of a two-by-two matrix is at most twice its largest entry.
Consequently (7)--(8), for \(A_u(t)\le A<1/4\), give
\[
\begin{aligned}
\|\mathcal K_q[u](t)-K_2(X_0)\|_{\mathrm{op}}
&\le256\sum_{k=1}^{\infty}(k+1)(k+2)(k+3)(4A)^k\\
&=1536\{(1-4A)^{-4}-1\}=:S(A).
\end{aligned}                                                   \tag{10}
\]
The same bound proves absolute convergence for \(q=\infty\).
Set \(A_*=10^{-6}\). On \(0\le A\le A_*\),
\[
S'(A)=24576(1-4A)^{-5}\le25000,
\qquad S(A_*)\le1/40<1/16.
\]
For instance \((1-4A_*)^5\ge1-20A_*\) verifies the derivative bound.

For two paths with action at most \(A_*\), every finite or infinite functional
also satisfies
\[
\|\mathcal K_q[u](t)-\mathcal K_q[v](t)\|_{\mathrm{op}}
\le25000\int_0^t\sum_b|u_b(s)-v_b(s)|\,ds.       \tag{11}
\]
To check this without losing a simplex factorial, interpolate
\(u_\theta=(1-\theta)u+\theta v\) and differentiate each ordered integral.
Sum the \(k\) possible insertion positions of \(v-u\). After taking absolute
values, the bound for their sum is
\[
\frac{A_*^{k-1}}{(k-1)!}
\int_0^t\sum_b|u_b(s)-v_b(s)|\,ds.
\]
Indeed the difference factor may appear anywhere in the ordering, while the
other \(k-1\) factors are the same scalar absolute-value function. Summing (8)
therefore gives \(S'(A_*)\). This convergent derivative majorant also justifies
the infinite version of (11).

## 2. The infinite functional equals the actual dense kernel

Use \(\|X\|=\max\{\|B\|_{\mathrm{op}},\|W\|_{\mathrm{op}},\|c\|_2\}\).
Since \(\|V_b(X)\|\le\|X\|^2\), a dense trajectory with \(A_u(t)\le A_*\)
obeys the scalar comparison
\[
\|X(t)\|\le4+\int_0^t\sum_b|u_b(s)|\,\|X(s)\|^2ds
\quad\Longrightarrow\quad
\|X(t)\|\le\frac4{1-4A_u(t)}<5.                \tag{12}
\]

Integrate its exact kernel hierarchy \(N+1\) times. The first terms are (9)
with \(k=0,\ldots,N\). The remainder contains
\(K_{N+3}(X(t_{N+1}))\), evaluated at a moving state. At states of norm at
most five, ANALYTIC_ROUTE bounds each entry of that remainder by
\[
\frac{(N+4)!}{2}\,5^{N+5}
\frac{A_u(t)^{N+1}}{(N+1)!}
=
\frac{625}{2}(N+2)(N+3)(N+4)(5A_u(t))^{N+1}.    \tag{13}
\]
This converges uniformly to zero when \(A_u(t)\le A_*\). Hence the actual dense
kernel equals \(\mathcal K_\infty[u]\) on every such interval. In particular
this identification holds before a possible first exit from the action bound;
no convergence of the infinite hierarchy has been assumed.

## 3. Both trajectories stay in the small-action region

At zero readout, (1) gives
\[
K_2(X_0)=(W_0B_0)^\top(W_0B_0)\succeq9I/16.
\]
As long as a dense or order-\(q\) trajectory has action at most \(A_*\), (10)
and the preceding identification imply
\(K(t)\succeq(9/16-1/16)I=I/2\).
Using the weaker gap \(K(t)\succeq I/4\), the residual equation
\(\dot r=-K(t)r/2\) yields
\[
\|r(t)\|_2\le\eta e^{-t/8},\qquad
A_u(t)\le\frac1{\sqrt2}\int_0^t\|r(s)\|_2\,ds
\le4\sqrt2\,\eta<A_*                         \tag{14}
\]
for \(\eta\le10^{-8}\). This excludes a first exit through \(A_*\).

A finite-time existence failure is excluded as well. For the dense trajectory,
(12) bounds every coordinate at fixed width. For the finite hierarchy, repeated
integration bounds each retained tensor by a finite sum of initialized
coefficients and powers of \(A_*\), just as in (9). There are finitely many
coordinates for each \(n,q\), so the polynomial ODEs continue at every finite
time. Both trajectories satisfy (14) globally and their predictions tend to
\(y\). All these statements are simultaneous in \(q\), on the single event (1).

## 4. Error bound for the entire trajectory

The inequality
\((k+1)(k+2)(k+3)\le6\cdot4^k\) holds for \(k\ge0\): it is equality at
zero and consecutive products have ratio \((k+4)/(k+1)\le4\).
Thus, for any path with action at most \(8\eta\),
\[
\begin{aligned}
\|\mathcal K_\infty[u](t)-\mathcal K_q[u](t)\|_{\mathrm{op}}
&\le1536\sum_{k=q-1}^{\infty}(16A_u(t))^k\\
&\le3072(128\eta)^{q-1}=:T_q.
\end{aligned}                                                   \tag{15}
\]
Here \(A_u(t)\le4\sqrt2\eta<8\eta\) by (14), and \(128\eta<1/2\).

Let \(e=f^{(q)}-f\), \(r=f-y\), and
\[
\Delta K=\mathcal K_q[u^{(q)}]-\mathcal K_\infty[u].
\]
The distinct residual controls differ by \(-e/2\), so (11) and (15) imply
\[
\|\Delta K(t)\|_{\mathrm{op}}
\le\frac{25000}{\sqrt2}\int_0^t\|e(s)\|_2\,ds+T_q.       \tag{16}
\]
Subtracting the output equations gives
\[
\dot e=-\tfrac12\mathcal K_q[u^{(q)}]e-\tfrac12\Delta K\,r,
\qquad e(0)=0.
\]
The homogeneous evolution contracts at least by \(e^{-(t-s)/8}\), from the
real symmetry and gap \(I/4\). Therefore
\[
\|e(t)\|_2\le\frac12\int_0^te^{-(t-s)/8}
\|\Delta K(s)\|_{\mathrm{op}}\eta e^{-s/8}\,ds.          \tag{17}
\]
For finite \(T\), write \(E_1(T)=\int_0^T\|e(t)\|_2dt\).
Integrating (17), interchanging nonnegative integrals, and using (16) yields
\[
\begin{aligned}
E_1(T)
&\le4\int_0^T\|\Delta K(s)\|_{\mathrm{op}}\|r(s)\|_2ds\\
&\le32\eta\left(\frac{25000}{\sqrt2}E_1(T)+T_q\right).
\end{aligned}
\]
Since \(32\eta\cdot25000/\sqrt2<1/2\), letting \(T\) increase gives
\(\int_0^\infty\|e(t)\|_2dt\le64\eta T_q\).
Equation (16) then gives \(\sup_t\|\Delta K(t)\|_{\mathrm{op}}\le2T_q\),
because \(64\eta\cdot25000/\sqrt2<1\).
Finally (17) and \(\int_0^\infty\|r(s)\|_2ds\le8\eta\) imply
\[
\sup_{t\ge0}\|e(t)\|_2\le8\eta T_q
\le24576\eta(128\eta)^{q-1}.
\]
This proves (2) on the full physical trajectory, including the fitted endpoint.

## 5. A polynomial lower bound for the actual independent dense pair

Initialize \(B,W\) independently with iid \(N(0,1/n)\) entries and take an
independent tilde copy. Both satisfy (1) with probability at least
\(1-Ce^{-cn}\), as proved in RESULT.
If \(a=B_0e_1\) and \(Z=\|W_0a\|_2^2\), then
\[
Z\overset{\mathrm{law}}=UV,\qquad
U,V\text{ independent with law }\chi_n^2/n.
\]
Indeed \(U=\|a\|_2^2\), and conditional on \(a\), \(W_0a\) has independent
Gaussian entries of variance \(\|a\|_2^2/n\). The conditional law of
\(V=\|W_0a\|_2^2/\|a\|_2^2\) does not depend on \(a\), giving independence.
The zero denominator has probability zero.

Here is a coarse density estimate without Stirling's formula.
With \(\alpha=n/2\ge1\), polar-coordinate integration of the Gaussian density
and scaling give
\[
p(v)=\frac{\alpha^\alpha}{\Gamma(\alpha)}
v^{\alpha-1}e^{-\alpha v},\qquad v>0.
\]
For \(\alpha>1\), the integrand \(t^{\alpha-1}e^{-t}\) is maximized at
\(t=\alpha-1\), whereas
\[
\Gamma(\alpha)\ge
\int_{\alpha-1}^{\alpha}t^{\alpha-1}e^{-t}dt
\ge e^{-1}(\alpha-1)^{\alpha-1}e^{-(\alpha-1)}.
\]
Therefore \(\sup_vp(v)\le e\alpha\); for \(\alpha=1\), this follows directly
from the exponential density. Conditional on any \(U\ge1/2\), the density of
\(UV\) is at most \(en\).

For an independent copy \(\widetilde Z\), condition on \(U,\widetilde Z\).
Since \(\operatorname{Var}(U)=2/n\), Chebyshev's inequality gives, for
\(\delta>0\),
\[
\Pr\{|Z-\widetilde Z|\le\delta\}
\le\Pr\{U<1/2\}+2en\delta
\le8/n+2en\delta.
\]
In particular,
\[
\Pr\{|Z-\widetilde Z|\ge n^{-2}\}\ge1-(8+2e)/n.         \tag{18}
\]

For \(g(t)=f_1(t)-\widetilde f_1(t)\),
\(g(0)=0\) and \(g'(0)=\eta(Z-\widetilde Z)/2\).
On (1) for both networks, ANALYTIC_ROUTE gives \(|g|\le2\) on the closed
complex disk of radius \(R=1/8192\), with holomorphy on a neighborhood.
For \(0\le t\le R/2\), the circle of radius \(R/2\) centered at \(t\) is in
that disk, so Cauchy's derivative estimate gives
\[
|g''(t)|\le H:=16/R^2.
\]
Choose \(t_n=\eta/(2Hn^2)<R/2\). On (18), Taylor's integral remainder gives
\[
|g(t_n)|\ge|g'(0)|t_n-\tfrac H2t_n^2
\ge\frac{\eta^2}{8Hn^4}
=\frac{\eta^2R^2}{128n^4}.
\]
The supremum \(D_n\) includes this time and input. Union-bounding the bad
events proves (3). This is not a lower bound at the fitted endpoint, where
the two dense predictors agree.

## 6. Array complexity and scope of the obstruction

Since \(24576\eta/c_\eta=3\cdot2^{46}/\eta\), (4) and (2) imply
\(E_n(q_n)\le c_\eta n^{-5}\). Combining with (3) proves (5), so
\(E_n(q_n)/D_n\to0\) in probability.

The positive numerator in (4) makes its inner integer at least two. The
ceiling adds at most one, and therefore
\[
2^{q_n+1}-2\le
8\left(\frac{3\cdot2^{46}}{\eta}\right)^{
\log2/\log(1/(128\eta))}
n^{5\log2/\log(1/(128\eta))}.
\]
For \(\eta\le10^{-62}\) the exponent is less than \(1/20\), proving (6).
The identity \(f(t,v)=\sum_av_af_a(t)\), \(\|v\|_2=1\), also holds for
the hierarchy: its initial tensors are linear in their first input slot,
and its evolution preserves this property. Thus the sphere norm requires no
extra continuum of stored query variables.

The supervisor's subsequent same-study result in
[STRONGER_SOURCE.md](STRONGER_SOURCE.md) gives a polynomial lower bound
\(n^{\alpha_{\mathrm{lower}}-o(1)}\), where
\(\alpha_{\mathrm{lower}}=\log2/(2C_\eta^{\mathrm{lower}})>0\) and
\(C_\eta^{\mathrm{lower}}\) is the constant of that separate lower bound.
This paragraph uses the result supplied by the supervisor and does not
rederive it. That polynomial lower bound and this polynomial upper bound
are compatible; the gap between their exponents remains unresolved.
A greater worst-case lower bound could still concern another activation,
label regime, depth, sample count or data configuration. No such example is
proved here. For this fixed, very small label and deep linear witness,
a superpolynomial retained-array lower bound, or even an \(\Omega(n)\)
lower bound under this array-count convention, is false.

## Check record

Author: agent \(\texttt{/root/nth\_lower\_analytic\_check}\), 2026-10-10.
The complete proof was derived from the scoped assignment and the two permitted
files. No experiments were run. The mathematical audit checked the integral
order, both simplex factorials, first-two-slot symmetry, the dense remainder
at moving states, finite-time continuation, and distinct residual paths.

At \(q=2\), (9) contains only its initial constant kernel and (15) starts
at \(k=1\), as required. The bootstrap uses one event for every order. The
density argument treats \(n=2\) directly via its exponential density and
does not use large-width density asymptotics. Its probability lower bound
may be negative at small width, which is valid and immaterial asymptotically.

The supervisor suggested a sharper dense-pair anti-concentration estimate;
the proof above instead derives the sufficient \(n^{-4}\) bound directly.
The scoped internal cross-check by agent
\(\texttt{/root/nth\_lower\_scalar}\) is complete in
[SAME_STUDY_CHECK.md](SAME_STUDY_CHECK.md); it found no blocking proof gap.
Root also read and reconstructed the complete proof. These are same-study
checks, not isolated promotion reviews.
Its model scope and preprocessing/storage distinction are part of its statement.

Direct arithmetic verification with \(\texttt{awk}\) at \(A_*=10^{-6}\)
and the maximal upper-bound label \(\eta=10^{-8}\) gave kernel displacement
\(0.0245762\), functional Lipschitz bound \(24576.5\), residual-action bound
\(5.65685\cdot10^{-8}\), absorption coefficient \(0.00565685\), and kernel
error amplification increment \(0.0113137\), all within the stated margins.
At \(\eta=10^{-62}\), the retained-array exponent is \(0.0251307<1/20\).
The explicit prefactor identity in Section 6 was also checked arithmetically.
These checks supplement the exact inequalities above; no empirical claim is made.
