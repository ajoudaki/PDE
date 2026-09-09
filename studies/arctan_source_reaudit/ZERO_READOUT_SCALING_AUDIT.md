# Audit of the zero-readout arctangent scaling

## Verdict

With raw mobilities

\[
 \lambda_1=n,\qquad \lambda_2=1,\qquad \lambda_3=n^{-1},
\]

the displayed finite gradient equations are correctly normalized.  However,
if \(W^{(3)}_{0,i}\sim N(0,n^{-4})\) and \(C=nW^{(3)}\), then

\[
 \operatorname{Var}(C_{0,i})=n^{-2},
\]

so the width-limit initialization is \(C_0=0\), not a nondegenerate
Gaussian readout.  Consequently only the top/readout tangent-kernel block is
nonzero at time zero.  Both hidden blocks become strictly active at order
\(t^2\).

## Exact finite scaling

Let

\[
 H=\phi(A),\quad Z=BH,\quad G=\phi(Z),\quad
 f=\sum_iW^{(3)}_iG_i=\langle C,G\rangle_n,
 \quad e=f-1,
\]

where \(\phi=\arctan\), \(q=\phi'\), and
\(D=C\odot q(Z)\).  Ordinary differentiation in the raw variables gives

\[
 \frac{\partial f}{\partial W^{(3)}}=G,
 \qquad
 \frac{\partial f}{\partial B}=n^{-1}DH^{\mathsf T},
 \qquad
 \frac{\partial f}{\partial A}=n^{-1}q(A)\odot B^{\mathsf T}D.
\]

Gradient descent on \(e^2\), with the three mobilities above, therefore is

\[
 \dot C=-2eG,
 \qquad
 \dot B=-2e(D\otimes H),
 \qquad
 \dot A=-2e q(A)\odot B^{\mathsf T}D,
\]

where \(D\otimes H=n^{-1}DH^{\mathsf T}\).  The corresponding tangent
kernel decomposes as

\[
 K=K_3+K_2+K_1,
\]

\[
 K_3=\langle G^2\rangle_n,qquad
 K_2=\langle D^2\rangle_n\langle H^2\rangle_n,qquad
 K_1=\langle q(A)^2(B^{\mathsf T}D)^2\rangle_n.
\]

The raw mobility \(n^{-1}\) in the third layer is essential.  Merely
defining \(C=nW^{(3)}\) would instead give
\(\dot C=-2neG\) under unit raw mobility.

## Initialization

The rescaled readout satisfies

\[
 \mathbb E\|C_0\|_n^2=n^{-2},\qquad
 \mathbb E\|C_0\|_{\ell^2}^2=n^{-1},
\]

and \(\|C_0\|_\infty\to0\) in probability.  Thus
\(C_0,D_0,f_0\to0\).  In contrast, if \(A_i\sim N(0,1)\),
\(B_{ij}\sim N(0,n^{-1})\), and

\[
 h_2=\mathbb E\arctan(N)^2>0,
\]

then \(Z_0=BH_0\) has limiting law \(N(0,h_2)\).  Hence

\[
 K_3(0)\longrightarrow
 g_2:=\mathbb E_{Z\sim N(0,h_2)}\arctan(Z)^2>0,
\]

whereas \(K_2(0),K_1(0)\to0\).

## Width-first small-time expansion

At finite width the correct first expansion is

\[
 C_n(t)=C_{0,n}+2(1-f_{0,n})tG_{0,n}+O_n(t^2),
\]

and \(D_{0,n}\ne0\) almost surely.  The cleaner formulas below hold only
after taking the width limit, where \(C_0=D_0=f_0=0\) and \(e_0=-1\).

Put

\[
 U=G_0q(Z_0),\qquad \Xi=B_0^{\mathsf T}U.
\]

Direct differentiation then gives

\[
 C(t)=2tG_0+O(t^2),
 \qquad
 D(t)=2tU+O(t^2),
\]

\[
 B(t)=B_0+2t^2(U\otimes H_0)+o(t^2),
\]

and

\[
 A(t)=A_0+2t^2q(A_0)\Xi+o(t^2).
\]

Thus the signs and numerical factors in these post-width formulas are
correct.

## Reused-adjoint nondegeneracy

Let \(v=h_2\), \(Z\sim N(0,v)\),

\[
 u(z)=\frac{\arctan z}{1+z^2},qquad
 u_2=\mathbb E u(Z)^2>0,qquad
 \mu=\mathbb E u'(Z).
\]

Gaussian row conditioning for the same reused \(B_0\) gives the column
field law

\[
 \Xi=\mu H+\sqrt{u_2}\,\zeta,
\]

where \(H=\arctan(A)\) and \(\zeta\sim N(0,1)\) is independent of \(A\).
Indeed, conditional on \(H\), decompose every row into its projection along
\(H\) and an independent orthogonal Gaussian row.  The projection
coefficient converges to

\[
 \frac{\mathbb E[Zu(Z)]}{v}=\mathbb E u'(Z)=\mu
\]

by Stein's identity, while the orthogonal innovation has coordinate
variance \(u_2\).

Consequently

\[
 K_2(t)=4t^2h_2u_2+o(t^2),
\]

and

\[
\begin{aligned}
 K_1(t)
 &=4t^2\mathbb E\{q(A)^2\Xi^2\}+o(t^2)\\
 &=4t^2\left[
 \mu^2\mathbb E\{q(A)^2H^2\}
 +u_2\mathbb E q(A)^2\right]+o(t^2).
\end{aligned}
\]

Both displayed quadratic coefficients are strictly positive.  The precise
statement is therefore: the top block is active at \(t=0\), and both hidden
blocks become active immediately for positive time, with kernel magnitude
of order \(t^2\).  Calling all three blocks active at initialization is
incorrect.

The stronger remainder \(O(t^3)\) is available only after separately
establishing the required reachable \(L^4/L^6\) differentiability bounds.
It does not follow from local Lipschitzness of the ambient \(L^2\)-valued
ODE alone.  The \(o(t^2)\) form above is sufficient for strict activation.

## OMFP regularity correction

The raw \(A\)-equation is an exact finite identity, but it is not an
ordinary locally Lipschitz vector field on an ambient \(L^2\) ball: the
difference term
\((q(A)-q(\widetilde A))B^{\mathsf T}D\) is a product of two merely
\(L^2\) fields.  Use the arctangent natural coordinate

\[
 R=A+A^3/3.
\]

Then

\[
 \dot R=-2eB^{\mathsf T}D,
 \qquad H=\arctan\Theta^{-1}(R),
\]

and the latter coordinate map is globally Lipschitz.  Since the limiting
readout starts from zero and \(|G|\le\pi/2\), the target-one loss identity
\(\dot e=-2eK\) gives \(|e|\le1\) and hence

\[
 \|C(t)\|_\infty\le\pi t.
\]

This bounded current readout makes \(D=Cq(Z)\) locally Lipschitz in the
transformed OMFP state.  Thus the natural-coordinate IDE supplies the
correct continuum proof; an unqualified ambient-\(L^2\) Picard argument in
the raw \(A\) coordinate does not.
