# Internal check: almost-sure feature rank at each fixed finite time

Checked 2026-10-11 by the scoped `intrinsic_geometry_check` agent. Input was
the supervisor's new proposition and the already-read canonical model in
`INTRINSIC_GEOMETRY_ROUTE.md`, SHA-256
`33626db7dba86ff58b5bbbcdd0bcadb06766a6802dc47ab50d992a598709d327`.
No additional scientific sources, prior arguments for this proposition,
external references, or experiments were used. Required proof and canonical
notation skills were applied. This is an internal check, not promotion.

**Verdict:** the proposition is valid, for every fixed label vector, including
zero labels. The proof below supplies ridge independence, global existence,
analytic dependence, and the analytic zero-set argument. The conclusion is
pointwise in deterministic finite time, with no intrinsic-rank restriction.
It is not simultaneous full rank at every time and is not an all-time fitting
theorem.

## Statement and model

Let \(m\ge1\), \(n\ge m\), and let the columns \(x_a\in\mathbb R^D\)
of \(X\in\mathbb R^{D\times m}\) be distinct unit vectors with
\(x_a\ne-x_b\) for distinct indices. Fix any \(y\in\mathbb R^m\).
For parameters \(A\in\mathbb R^{n\times D}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\), define
\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|^2/m.
\]
The physical gradient flow is
\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L.
\]
Initially, \(A\) has independent \(N(0,1)\) entries, \(W\) has
independent \(N(0,1/n)\) entries, the two matrices are independent,
and \(w=0\).

For each deterministic \(T\in[0,\infty)\),
\[
\mathbb P\!\left(\operatorname{rank}U(T)=m\right)=1.
\tag{1}
\]
In addition, with probability one, the determinant of the submatrix formed
by the first \(m\) rows of \(U(t)\) has only finitely many zeros on each
compact time interval. All rank-deficient times are contained in this locally
finite random set. These statements require no condition
\(m\le\operatorname{rank}X\).

## 1. A nonsingular feature evaluation exists

The ridge functions \(a\mapsto\tanh(a^\top x_b)\), indexed by samples
\(b=1,\ldots,m\), are linearly independent. Here is a direct proof.

Choose \(\xi\in\mathbb R^D\) outside the finitely many hyperplanes
orthogonal to \(x_a\) and \(x_a\pm x_b\). Each is a proper hyperplane
by the sample assumptions, so their union cannot cover \(\mathbb R^D\).
Then \(\beta_a=\xi^\top x_a\) are nonzero and have pairwise distinct
absolute values. Write \(\alpha_a=|\beta_a|>0\).

Suppose fixed coefficients satisfy
\(\sum_b c_b\tanh(\theta^\top x_b)=0\) for every
\(\theta\in\mathbb R^D\). Restricting to \(\theta=t\xi\) and
absorbing \(\operatorname{sign}(\beta_b)\) into the coefficients gives
\[
\sum_b d_b\tanh(\alpha_b t)=0\qquad\text{for every }t\in\mathbb R.
\]
Letting \(t\to\infty\) first gives \(\sum_bd_b=0\). Subtract this
constant identity and use
\[
\tanh(\alpha t)-1
=-\frac{2e^{-2\alpha t}}{1+e^{-2\alpha t}}.
\]
Multiplication by \(e^{2\alpha_{\min}t}\) and passage to infinity force
the coefficient corresponding to the unique smallest \(\alpha_b\) to
vanish. Repeating with the remaining terms forces every coefficient to
vanish. Thus the functions are independent.

Consequently the feature vectors
\(\bigl(\tanh(\theta^\top x_b)\bigr)_{b=1}^m\), as \(\theta\)
ranges over \(\mathbb R^D\), span \(\mathbb R^m\). Otherwise a nonzero
vector orthogonal to their span would give a nontrivial functional relation.
Choose \(m\) such evaluation vectors forming a basis, and use their
arguments as the first \(m\) rows of a matrix \(A_*\). Then
\[
\det\bigl(\tanh(A_*X)_{1:m,:}\bigr)\ne0.
\tag{2}
\]
The remaining rows may be arbitrary. This existence argument uses the
nonlinearity, not the linear rank of \(X\).

## 2. Global existence and analytic dependence

Identify all parameters with a vector \(p=(A,W,w)\) in finite-dimensional
Euclidean space. The vector field is real analytic on this entire real
space: matrix multiplication is polynomial, \(\tanh\) is real analytic
at every real argument, and differentiation preserves real analyticity.

For arbitrary finite initial parameters, the loss is finite and
\[
-\dot{\mathcal L}
=\|\dot A\|_F^2/n+\|\dot W\|_F^2+\|\dot w\|^2/n.
\]
Define the weighted parameter norm
\(\|p\|_*^2=\|A\|_F^2/n+\|W\|_F^2+\|w\|^2/n\). Integration
and Cauchy--Schwarz give, for every interval within the existence domain,
\[
\|p(t)-p(0)\|_*
\le\int_0^t\|\dot p(s)\|_*\,ds
\le\sqrt{t\mathcal L(0)}.
\tag{3}
\]
If the maximal forward time were finite, this would keep the trajectory
inside a compact set. The smooth vector field is bounded and locally
Lipschitz there; bounded velocity gives a limiting state at that time and
local existence from this state extends the trajectory. This contradicts
maximality. Thus every real initial state has a global forward solution.
On the slice \(w(0)=0\), one has simply
\(\mathcal L(0)=\|y\|^2/m\).

For clarity, the analytic-dependence step is local in the initial state;
it does not require one common complex neighborhood for all initial states
or all times. Near any finite real state, the vector field extends
holomorphically to a complex neighborhood: the finitely many tanh arguments
avoid the complex poles after shrinking that neighborhood. On a smaller
closed polydisc the field and its derivative are bounded. Picard iteration
for sufficiently short complex time is then a uniform contraction. Each
iterate is holomorphic in time and initial state, and the uniform limit is
holomorphic, proving the local analytic flow assertion.

Fix a real trajectory and a finite \(T\). Its image on \([0,T]\) is
compact by (3). Cover it by finitely many of the above local flow
neighborhoods and subdivide the time interval so that successive solution
segments remain in such neighborhoods. Shrinking the initial neighborhood
at each step ensures the same compositions are defined for nearby initial
states. A finite composition of analytic maps is analytic. Hence the
time-\(T\) solution map is real analytic near every real initial state,
and therefore on all real parameter space. Restricting to \(w(0)=0\)
preserves analyticity in \((A(0),W(0))\).

The same local argument proves that each trajectory is real analytic in
time. At time zero a short backward solution exists by local existence;
at every finite forward time there is a later solution by global existence.
Thus the trajectory is analytic on an open interval containing every
compact interval \([0,T]\).

## 3. Analytic nonidentity and the Gaussian probability statement

For fixed \(T\), define the scalar function of the initial matrices
\[
g_T(A_0,W_0)
=\det\bigl(U(T;A_0,W_0,w_0=0)_{1:m,:}\bigr).
\]
It is real analytic by the preceding section. It is not identically zero:
take \(A_0=A_*\) from (2) and \(W_0=0\). Since \(w_0=0\), at this
state \(H=0\), \(f=0\), and all parameter velocities vanish. In detail,
the readout gradient vanishes because \(H=0\); both lower-layer gradients
vanish because they contain a factor \(w\). This remains true for every
residual \(r=-y\). The solution is therefore stationary, and
\[
g_T(A_*,0)=\det\bigl(\tanh(A_*X)_{1:m,:}\bigr)\ne0.
\]
The zero matrix \(W_0=0\) is used solely as an analytic nonidentity
witness; no positive probability is assigned to that exact initialization.

A nonzero real-analytic scalar function on \(\mathbb R^N\) has a
Lebesgue-null zero set. One self-contained proof is induction on \(N\).
For \(N=1\), zeros of a nonzero analytic function are isolated, hence
countable. In higher dimension write the argument as \((x',t)\).
At least one analytic coefficient
\(h_k(x')=\partial_t^k g(x',0)\) is not identically zero; otherwise each
one-variable function \(t\mapsto g(x',t)\) has all derivatives zero at
zero and is identically zero on the connected real line. The exceptional
set on which the entire one-variable function vanishes is contained in
\(\{h_k=0\}\), a null set by induction. Every other vertical section
has a null zero set by the one-variable case. Fubini on bounded boxes,
followed by a countable union, proves the assertion.

The joint Gaussian law of all entries of \((A_0,W_0)\) has a density
on its full finite-dimensional real parameter space. It therefore assigns
probability zero to \(\{g_T=0\}\). A nonzero first-\(m\)-row minor
implies full column rank, proving (1). The proof works for every fixed
\(y\), with no size or sign restriction. For \(y=0\), the actual
initialized flow is stationary for every \((A_0,W_0)\), which is fully
consistent with the same rank conclusion.

## 4. Time quantifiers and limits

Applying (1) at \(T=0\) shows that almost surely the specified initial
minor is nonzero. For any realization with this property, let
\(g(t)=\det(U(t)_{1:m,:})\). This is an analytic function on an open
interval containing \([0,\infty)\), and \(g(0)\ne0\), so it is not
identically zero. Its zeros cannot accumulate at any finite time. Compactness
then gives finitely many zeros on each \([0,T]\). Every time at which
\(U(t)\) loses full column rank is among these zeros, although a zero of
this particular minor need not imply loss of full column rank.

It would be invalid to take an uncountable intersection of the probability-one
events in (1) and conclude full rank at every time. The analyticity argument
only reduces the possible exceptional set to locally finitely many random
times; it does not rule them out. It also supplies no uniform lower bound on
the least singular value, no quantitative width requirement beyond \(n\ge m\),
and no positive spectral gap as \(t\to\infty\). In particular it does not
prove any all-time residual-convergence or fitting claim for the nonlinear
Gaussian-initialized network.

Only this assigned report was written. No source edits, experiments, Git
staging, or commits were performed.
