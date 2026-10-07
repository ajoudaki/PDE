# Independent internal check of the ordinary-iid limitation

Check date: 2026-10-05. Verdict: **PASS for the explicitly stated zero-readout model and its stated independent-reference scope.** This is an independent internal proof check, not a promotion review or approval of established status.

The complete frozen input was `RANDOM_SMALL_LIMITATION.md`, SHA-256
`608ca4aa83134aa6559a101994fd32751bf64dfe76d4c6fa03999b8dc18e2d83`.
The only scientific input besides that document was `docs/notation.qmd`.
No study history, README, other route, previous verdict, other study,
experiment, or external scientific source was consulted.
The proof-check skill `solve-math-rigorously` was read. Reading
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned permission denied; the supervisor-authorized fallback was used:
explicit definitions, ordinary Euclidean/operator norms, visible width
factors, and the maintained notation contract. The supervisor clarified
that the frozen research contract explicitly specifies zero readout;
that clarification adds no scientific result to the proof.

## Claim and exact model

Fix one sample with input \(x_1\in\mathbb R^d\),
\(\|x_1\|_2=\sqrt d\), and label \(0<|y|\le1\). The width
\(q\) is any positive integer. With \(\phi=\tanh\), the model is

\[
u(x)=Ax/\sqrt d,\quad h(x)=\phi(u(x)),\quad
v(x)=Wh(x),\quad g(x)=\phi(v(x)),\quad
f_q(x)=w^Tg(x)/q.
\]

Here \(A\in\mathbb R^{q\times d}\),
\(W\in\mathbb R^{q\times q}\), and \(w\in\mathbb R^q\).
These are respectively the maintained convention's first matrix,
hidden matrix, and stored readout. Initially the entries of \(A\) are
independent \(\mathcal N(0,1)\), the entries of \(W\) are independent
\(\mathcal N(0,1/q)\), the matrices are independent, and \(w=0\).
The loss is \((f_q(x_1)-y)^2\), with block mobilities \((q,1,q)\).
This explicit readout initialization is essential to this proof. It does
not assert the corresponding result for the notation document's default
Gaussian small readout.

The claim is that absolute constants \(a,C,p_0>0\) exist such that two
independent copies satisfy

\[
\mathbb P\!\left(
 |f_q^{[1]}(t_q,x_1)-f_q^{[2]}(t_q,x_1)|
 \ge\frac{a^2|y|}{Cq}\right)\ge p_0,
\qquad t_q=\frac{a}{C\sqrt q}.
\]

The proof establishes this uniformly in \(q,d,x_1,y\) in the displayed
range. It then excludes an independent dense-reference comparison with
error \(K/\sqrt n\), fixed nonzero label and fixed finite \(K\), when
\(q(n)=o(\sqrt n)\) and the allowed fixed failure probability is
sufficiently small. Both conclusions reconstruct as follows.

## Conditional fluctuation and moments

Define \(\psi(z)=\tanh^2z\), let \(G\sim\mathcal N(0,1)\), and put

\[
v_*=\mathbb E\psi(G),\qquad
\mu(v)=\mathbb E\psi(\sqrt vG),\qquad
\nu(v)=\operatorname{Var}(\psi(\sqrt vG)).
\]

The normalization of \(x_1\) gives independent initial
\(u_i(x_1)\sim\mathcal N(0,1)\). Conditional on
\(h=\tanh u(x_1)\), independent rows of \(W\) give independent
\(v_j(x_1)\sim\mathcal N(0,V_q)\), where

\[
V_q=\frac1q\sum_i\psi(u_i),\qquad
\kappa_q=\frac1q\sum_j\psi(v_j).
\]

In particular, the conditional mean and variance of \(\kappa_q\)
are \(\mu(V_q)\) and \(\nu(V_q)/q\). The shared random variance
does create unconditional dependence between the second-layer
coordinates, and the proof correctly retains it.

For the source's constants

\[
r=\tfrac12\sqrt{v_*/2},\quad
\alpha=\mathbb P(|G|\le r),\quad
\beta=\mathbb P(|G|\ge1),\quad
b=\alpha\beta[\psi(2r)-\psi(r)]^2,
\]

we have \(0<v_*<1\) and \(b>0\). If \(v\in[v_*/2,1]\),
then \(\psi(\sqrt vG)\le\psi(r)\) on \(|G|\le r\), and
\(\psi(\sqrt vG)\ge\psi(2r)\) on \(|G|\ge1\). The two
opposite combinations in the independent-copy variance identity give
\(\nu(v)\ge b\), with no missing factor of two.
Since \(0\le V_q\le1\) and \(\mathbb EV_q=v_*\),

\[
v_*\le v_*/2+\mathbb P(V_q\ge v_*/2),
\quad
\operatorname{Var}(\kappa_q)
\ge\frac{\mathbb E\nu(V_q)}q
\ge\frac{bv_*}{2q}.
\]

These estimates include \(q=1\); no asymptotic concentration step is
being used.

For the upper fourth moment, direct differentiation yields
\(\psi''(z)=2(1-\tanh^2z)(1-3\tanh^2z)\), whose absolute value is
at most two. Gaussian integration by parts therefore gives
\(\mu'(v)=\mathbb E\psi''(\sqrt vG)/2\) for \(v>0\).
The source supplies integrable bounds for differentiation on every
compact positive interval; bounded \(\psi'\) removes the boundary
term in the integration by parts. Together with
\(0\le\mu(v)\le v\) at zero, this proves that \(\mu\) is
one-Lipschitz on \([0,1]\).

For independent centered variables bounded in absolute value by one,
the fourth-power expansion gives

\[
\mathbb E\left(q^{-1}\sum_iX_i\right)^4
=q^{-4}\left(\sum_i\mathbb EX_i^4
 +6\sum_{i<j}\mathbb EX_i^2\mathbb EX_j^2\right)
\le3q^{-2}.
\]

The required conditional centered variables and the first-layer
centered variables both satisfy this bound. Decomposing

\[
\kappa_q-\mu(v_*)
=[\kappa_q-\mu(V_q)]+[\mu(V_q)-\mu(v_*)]
\]

and using \(|x+z|^4\le8(|x|^4+|z|^4)\) gives the claimed
\(48/q^2\) bound. For the difference \(D_q\) of two independent
copies of \(\kappa_q\), it follows that

\[
\mathbb ED_q^2\ge bv_*/q,\qquad
\mathbb ED_q^4\le768/q^2.
\]

For a nonnegative variable \(Z\), splitting its expectation at
\(\mathbb EZ/2\) and applying Cauchy--Schwarz proves
\(\mathbb P(Z\ge\mathbb EZ/2)\ge
(\mathbb EZ)^2/(4\mathbb EZ^2)\).
The moments just established verify the hypotheses for \(Z=D_q^2\).
Thus the source's exact constants

\[
a=\sqrt{bv_*/2},\qquad p_*=(bv_*)^2/3072
\]

satisfy \(\mathbb P(|D_q|\ge a/\sqrt q)\ge p_*\).
The denominator 3072 and every preceding moment factor are correct.

## Operator-norm event and its intersection

A maximal one-quarter-separated subset of the unit sphere has at most
\(9^q\) points, by comparing disjoint radius-one-eighth balls with the
radius-nine-eighths enclosing ball. Maximality makes it a one-quarter
net. Approximating both arguments of a bilinear form by net points
costs at most \(\|W\|_{\mathrm{op}}/2\), so
\(\|W\|_{\mathrm{op}}\) is bounded by twice the maximal net
bilinear form in absolute value. Each fixed form is
\(\mathcal N(0,1/q)\). Its Gaussian exponential tail and a union
bound over the two nets give

\[
\mathbb P(\|W\|_{\mathrm{op}}>M)
\le2\exp[-(M^2/8-2\log9)q].
\]

For \(M^2=8[2\log9+\log(8/p_*)]\), this is at most
\(p_*/4\) for every \(q\ge1\). Subtracting the two matrix
failure probabilities from the fluctuation event gives

\[
\mathbb P\bigl(|D_q|\ge a/\sqrt q,
 \ \|W^{[1]}(0)\|_{\mathrm{op}}\le M,
 \ \|W^{[2]}(0)\|_{\mathrm{op}}\le M\bigr)
\ge p_*/2=:p_0.
\]

This argument does not assume independence between a network's
initial kernel and its initial matrix norm.

## Feature equation, physical clock, and curvature

All vectors in this section are evaluated at \(x_1\). Write primes
for derivatives with respect to feature time \(s\). Define

\[
z=w\odot\phi'(v),\quad
w'=g,\quad W'=zh^T/q,\quad
u'=\phi'(u)\odot W^Tz.
\]

The corresponding first-matrix derivative is
\(A'=u'x_1^T/\sqrt d\). Multiplication by \(x_1/\sqrt d\)
recovers \(u'\) precisely because \(\|x_1\|_2^2=d\).
The physical gradients are

\[
\nabla_wf_q=g/q,\quad \nabla_Wf_q=zh^T/q,\quad
\nabla_Af_q=q^{-1}
 [\phi'(u)\odot W^Tz]x_1^T/\sqrt d.
\]

Consequently the squared loss and mobilities \((q,1,q)\) give
exactly the displayed feature equation multiplied by
\(\dot s=2[y-F(s)]\), where \(F(s)=w(s)^Tg(s)/q\) and
\(s(0)=0\). There is no lost width factor or factor two. Allowing
negative \(s\) makes the construction valid for negative labels as
well.

On the matrix-norm event, integration from zero gives

\[
\|w(s)\|_\infty\le|s|,\qquad
\|W(s)\|_{\mathrm{op}}\le M+s^2/2.
\]

Indeed, \(\|g\|_\infty\le1\) and
\(\|W'\|_{\mathrm{op}}\le\|w\|_2\|h\|_2/q\le|s|\).
Also \(\|u'\|_2\le(M+s^2/2)\sqrt q\,|s|\).
These bounds prevent finite-\(s\) escape in the smooth
finite-dimensional feature equation, in either direction.

Set

\[
D=\operatorname{diag}(\phi'(u)^2),\qquad
B=\frac{\|h\|_2^2}{q}I+WDW^T.
\]

Differentiation gives \(h'=DW^Tz\), \(v'=Bz\), and

\[
F'=\frac{\|g\|_2^2}{q}+\frac{z^TBz}{q}\ge0.
\]

Here \(D\) and \(B\) are positive semidefinite. Along the physical
flow, the exact loss identity is
\(\frac d{dt}(F-y)^2=-4F'(F-y)^2\). Hence
\(|F-y|\le|y|\), \(|\dot s|\le2|y|\), and
\(|s(t)|\le2|y|t\). These bounds also continue the physical flow
for every finite time. For
\(0\le t\le1/(2\sqrt q)\), they imply \(|s(t)|\le q^{-1/2}\).

For \(|s|\le1\), put \(R=M+1\) and \(B_0=1+R^2\).
The bounds \(|\phi'|\le1\), \(|\phi''|\le2\) yield

\[
\frac{\|u'\|_2}{\sqrt q}\le R|s|,\quad
\frac{\|v'\|_2}{\sqrt q}\le B_0|s|,\quad
\frac{\|z\|_2}{\sqrt q}\le|s|,\quad
\frac{\|z'\|_2}{\sqrt q}\le1+2B_0s^2,\quad
\|B\|_{\mathrm{op}}\le B_0.
\]

The derivative of \(\|h\|_2^2/q\) costs at most \(2R|s|\);
the two differentiated \(W\) factors cost another \(2R|s|\).
Finally

\[
\|D'\|_{\mathrm{op}}\le4\|u'\|_\infty
\le4R\sqrt q\,|s|,
\quad
\|B'\|_{\mathrm{op}}
\le4R|s|+4R^3\sqrt q\,|s|.
\]

Applying Cauchy--Schwarz separately to
\(2g^Tg'/q\), \(2z'^TBz/q\), and \(z^TB'z/q\) gives

\[
|F''|
\le2B_0|s|+2B_0(1+2B_0)|s|
 +4R|s|^3+4R^3\sqrt q\,|s|^3.
\]

On \(|s|\le q^{-1/2}\), the last potentially growing expression
satisfies \(\sqrt q\,|s|^3\le1/q\le1\). All other displayed
powers of \(|s|\) are at most one. Therefore

\[
|F''|\le H:=4B_0+4B_0^2+4R+4R^3,
\qquad 0\le F'\le1+B_0.
\]

The chain rule gives the exact physical-time formula

\[
\partial_t^2f_q
=4F''(y-F)^2-4(F')^2(y-F).
\]

Using \(|y-F|\le|y|\le1\), the source's constant
\(C=4H+4(1+B_0)^2\) consequently satisfies

\[
|\partial_t^2f_q(t,x_1)|\le C|y|,
\qquad 0\le t\le1/(2\sqrt q).
\]

This is a width-uniform bound only on the claimed shrinking interval.
It requires no bound on the maximum initial first-layer coordinate.

## Separation and independent-reference consequence

Because \(w(0)=0\), the initial prediction is zero and
\(\partial_tf_q(0,x_1)=2y\kappa_q\). The integral Taylor
remainder is bounded by \(C|y|t^2/2\) per run. On the joint
fluctuation and norm event,

\[
|f_q^{[1]}(t,x_1)-f_q^{[2]}(t,x_1)|
\ge\frac{2a|y|t}{\sqrt q}-C|y|t^2.
\]

The source's constants satisfy \(a<1\), \(C>2\), so
\(t_q=a/(C\sqrt q)\) lies in the proved interval. Substitution
gives exactly \(a^2|y|/(Cq)\), with probability at least \(p_0\).
The time is deterministic and the lower bound already occurs at the
training input.

For the consequence, take two mutually independent compact runs and one
common dense reference, independent of both. For each compact run let
\(S_i\) be success of its entire claimed comparison with that dense
reference at tolerance \(K/\sqrt n\). The full-time, whole-sphere
success event in the source implies the same tolerance at
\((t_q,x_1)\). Thus on \(S_1\cap S_2\) the compact predictions
are within \(2K/\sqrt n\). For fixed \(y\ne0\), fixed finite
\(K\), and \(q(n)=o(\sqrt n)\), eventually

\[
\frac{a^2|y|}{Cq(n)}>\frac{2K}{\sqrt n}.
\]

The separation event is then contained in \(S_1^c\cup S_2^c\).
Each pair consisting of a compact run and the dense reference has the
same required independent joint law. Their marginal failure
probabilities are equal, so the union bound gives
\(\mathbb P(S_i^c)\ge p_0/2\). Independence of \(S_1\) and
\(S_2\) is unnecessary and was not used. The argument requires no
limit, concentration estimate, endpoint, or long-time convergence
theorem for the dense reference.

Consequently, every fixed \(\delta<p_0/2\) rules out such a
guarantee with any finite \(n\)-independent
\(K=C_{\mathrm{data},\delta}\), for all sufficiently large
\(n\). Every fixed polynomial in \(\log(en)\) is covered by
\(q(n)=o(\sqrt n)\).

## Issues and limitations

No substantive mathematical defect or required correction was found in
the frozen proof. All constants are finite, strictly positive, and
independent of width, dimension, normalized input, and permitted label.
The proof deliberately obtains a \(q^{-1}\) prediction discrepancy;
it does not establish an optimal \(q^{-1/2}\) lower bound.

The checked scope is essential: zero initial stored readout, the stated
two-hidden-layer tanh architecture, gradient flow with the stated
loss/mobilities, ordinary independent Gaussian hidden parameters, fixed
nonzero data label, and an independently initialized common reference.
The comparison event must control the early deterministic time used in
the proof. The argument does not address only an endpoint comparison,
labels tending to zero with \(n\), errors with an \(n\)-dependent
constant, other readout laws, raw discrete gradient descent, arbitrary
correlated couplings, or designed deterministic compact constructions.
In particular, it supplies a scoped obstruction to the ordinary iid
baseline and does not settle existence of the direct compact construction.
