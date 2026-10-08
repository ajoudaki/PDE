# Width-uniform short-time estimate for the exact dense flow

This is a scoped proof contribution to `bounded_packet_logarithmic_theory_20261008`.
Its scientific inputs are the supervisor's self-contained assignment and exactly
`dense_fields`, `dense_rhs`, and `BoundedGaussianPackets` in
`paper/figures/capture_trajectory.py`. No other study, archived book, or external
scientific source was used. The source file SHA-256 at inspection was
`bbb53b4e473be7efa079bc7d46fe5a4564e0625630c701fa7a3dd5152e8f69b2`;
repository HEAD was `1695447b4384c9b53df3dc051eb88c5f1fbb234c`.
Required proof and canonical-notation skills, including the neural-network
reference, were read. This is a proved candidate with an author algebraic check;
it has not received an independent review or been promoted.

## Exact model and statement

Let the width be an integer \(p\geq1\), the input dimension be \(d\geq1\),
and the training data be \((v_a,y_a)\in\mathbb R^d\times\mathbb R\),
\(1\leq a\leq m\), with \(m\geq1\) and \(\|v_a\|_2\leq1\).
The input convention in the assignment is \(v=x/\sqrt d\).
For evolving parameters
\(A(t)\in\mathbb R^{p\times d}\),
\(B(t)\in\mathbb R^{p\times p}\), and \(w(t)\in\mathbb R^p\), define

\[
h^{(1)}(t,v)=\tanh(A(t)v),\qquad
h^{(2)}(t,v)=\tanh(B(t)h^{(1)}(t,v)),\qquad
f(t,v)=\frac1p w(t)^\top h^{(2)}(t,v).
\]

The activation acts coordinatewise. Set

\[
r_a(t)=f(t,v_a)-y_a,\qquad
\mathcal L(t)=\frac1m\sum_{a=1}^m r_a(t)^2,\qquad
Y=\left(\frac1m\sum_{a=1}^m y_a^2\right)^{1/2}.
\]

Training is gradient flow with mobilities \((p,1,p)\) for \((A,B,w)\):

\[
\dot A=-p\nabla_A\mathcal L,\qquad
\dot B=-\nabla_B\mathcal L,\qquad
\dot w=-p\nabla_w\mathcal L.
\]

In the inspected Python source the state is `(w, c, matrix)`; its exact
correspondence with the present notation is `(A, w, B)`. The code's `inputs`
already contain \(v_a\); there is no additional input normalization in the RHS.

Assume finite initial parameters, \(w(0)=0\), and
\(\|B(0)\|_{\mathrm{op}}\leq M\), where \(M\geq0\).
There is no bound on \(A(0)\). The solution exists uniquely for every finite
\(t\geq0\). For any fixed finite \(T>0\), put

\[
S_T=1+(M+2Y^2T^2)^2.
\]

Then, simultaneously for every \(\|v\|_2\leq1\) and \(0\leq t\leq T\),

\[
\left|f(t,v)-t\dot f(0,v)\right|
\leq 2Yt^2+\frac{16}{3}Y^3 S_Tt^3,
\tag{1}
\]

where the initial velocity is exactly

\[
\dot f(0,v)
=\frac2m\sum_{a=1}^m y_a
\frac{h^{(2)}(0,v_a)^\top h^{(2)}(0,v)}p.
\tag{2}
\]

In particular, on \([0,1]\) the requested quadratic constant is

\[
C(M,Y)=2Y+\frac{16}{3}Y^3\bigl[1+(M+2Y^2)^2\bigr].
\tag{3}
\]

All these constants are independent of width, sample count, input dimension,
and the initial first-layer norm. The estimate is for the full evolving network.
The proof first controls the readout and hidden weights by loss dissipation,
then controls both hidden activations, and finally integrates the readout
equation while retaining the feature motion.

## Proof of the flow estimate

Write \(h_a^{(\ell)}=h^{(\ell)}(t,v_a)\) and define the diagonal matrices

\[
D_a^{(\ell)}=\operatorname{diag}(1-(h_a^{(\ell)})^2),
\qquad \ell=1,2.
\]

Each has operator norm at most one. Direct differentiation of the stated loss
gives the exact equations

\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(2)},\\
\dot B&=-\frac{2}{pm}\sum_a r_a(D_a^{(2)}w)h_a^{(1)\top},\\
\dot A&=-\frac2m\sum_a r_a
 D_a^{(1)}B^\top D_a^{(2)}w\,v_a^\top.
\end{aligned}
\tag{4}
\]

These equations match `dense_rhs`, including its factor two and all width
factors. Vector norms below are Euclidean; matrix norms are the usual operator
and Frobenius norms. Since \(|\tanh|\leq1\), both activations have
\(\|h^{(\ell)}(t,v)\|_2/\sqrt p\leq1\).

The RHS in (4) is smooth in the finite-dimensional parameter vector, so a
unique local solution exists. Along that solution, the chain rule and the
positive mobilities give

\[
\frac{d}{dt}\mathcal L
=-\frac1p\|\dot A\|_F^2-\|\dot B\|_F^2
 -\frac1p\|\dot w\|_2^2\leq0.
\tag{5}
\]

Initially \(f=0\), hence \(\mathcal L(0)=Y^2\). Cauchy--Schwarz therefore
yields \(m^{-1}\sum_a |r_a(t)|\leq\sqrt{\mathcal L(t)}\leq Y\).
Let \(s(t)=\|w(t)\|_2/\sqrt p\) and \(b(t)=\|B(t)\|_{\mathrm{op}}\).
The first equation in (4) implies

\[
\frac{\|\dot w(t)\|_2}{\sqrt p}\leq2Y,\qquad s(t)\leq2Yt.
\tag{6}
\]

For an outer product, \(\|uz^\top\|_F=\|u\|_2\|z\|_2\).
Consequently the second equation in (4) gives

\[
\|\dot B(t)\|_F
\leq\frac2{pm}\sum_a |r_a|\|w\|_2\|h_a^{(1)}\|_2
\leq2Ys(t)\leq4Y^2t.
\]

Integration, followed by \(\|\cdot\|_{\mathrm{op}}\leq\|\cdot\|_F\), gives

\[
\|B(t)-B(0)\|_F\leq2Y^2t^2,
\qquad b(t)\leq M+2Y^2t^2.
\tag{7}
\]

The third equation in (4), the contraction bounds for the diagonal matrices,
and \(\|v_a\|_2\leq1\) imply

\[
\frac{\|\dot A(t)\|_F}{\sqrt p}
\leq2Yb(t)s(t)
\leq4Y^2t(M+2Y^2t^2).
\tag{8}
\]

In particular,
\(\|A(t)-A(0)\|_F/\sqrt p\leq2MY^2t^2+2Y^4t^4\).
Equations (6)--(8) bound every parameter on any finite interval on which the
local solution exists. The continuation property for a locally Lipschitz ODE
states that a maximal solution with a finite terminal time must leave every
compact subset of its finite-dimensional state space. Here these bounds keep
the parameters in a closed bounded, hence compact, ball up to any proposed
finite terminal time. The vector field is smooth on all of that space.
Thus no finite terminal time is possible, proving global existence.

For a fixed query \(\|v\|_2\leq1\), differentiate its forward pass. Because
\(|\tanh'|\leq1\), (8) gives

\[
\frac{\|\dot h^{(1)}(t,v)\|_2}{\sqrt p}
\leq\frac{\|\dot A(t)v\|_2}{\sqrt p}
\leq2Yb(t)s(t).
\]

Differentiating the second preactivation then gives

\[
\begin{aligned}
\frac{\|\dot h^{(2)}(t,v)\|_2}{\sqrt p}
&\leq\|\dot B(t)\|_{\mathrm{op}}
       \frac{\|h^{(1)}(t,v)\|_2}{\sqrt p}
   +b(t)\frac{\|\dot h^{(1)}(t,v)\|_2}{\sqrt p}\\
&\leq2Ys(t)(1+b(t)^2)
\leq4Y^2 S_Tt\qquad(0\leq t\leq T).
\end{aligned}
\]

This estimate is uniform over the entire query unit ball; integrating gives

\[
\frac{\|h^{(2)}(t,v)-h^{(2)}(0,v)\|_2}{\sqrt p}
\leq2Y^2S_Tt^2.
\tag{9}
\]

No coordinate supremum of a backward signal is needed. In particular the
only bound on the backward action in (8) is
\(\|D_a^{(1)}B^\top D_a^{(2)}w\|_2\leq b(t)\|w\|_2\).

At time zero, (4) gives
\(\dot w(0)=2m^{-1}\sum_a y_a h^{(2)}(0,v_a)\),
so \(\|\dot w(0)\|_2/\sqrt p\leq2Y\). Since \(w(0)=0\), differentiating
\(f=w^\top h^{(2)}/p\) proves (2).
Subtracting the initial readout velocity in the first equation of (4) gives
the exact identity

\[
\dot w(t)-\dot w(0)
=-\frac2m\sum_a f(t,v_a)h^{(2)}(t,v_a)
 +\frac2m\sum_a y_a
   [h^{(2)}(t,v_a)-h^{(2)}(0,v_a)].
\]

Here \(|f(t,v_a)|\leq s(t)\), and
\(m^{-1}\sum_a|y_a|\leq Y\). Using (6) and (9),

\[
\frac{\|\dot w(t)-\dot w(0)\|_2}{\sqrt p}
\leq4Yt+4Y^3S_Tt^2,
\]

and hence

\[
\frac{\|w(t)-t\dot w(0)\|_2}{\sqrt p}
\leq2Yt^2+\frac43Y^3S_Tt^3.
\tag{10}
\]

Finally, decompose the error without freezing the evolving feature:

\[
\begin{aligned}
f(t,v)-t\dot f(0,v)
&=\frac{[w(t)-t\dot w(0)]^\top h^{(2)}(t,v)}p\\
&\quad+\frac{t\dot w(0)^\top
 [h^{(2)}(t,v)-h^{(2)}(0,v)]}p.
\end{aligned}
\]

The first term is bounded by (10); the second is bounded by
\(t(2Y)(2Y^2S_Tt^2)=4Y^3S_Tt^3\). Their sum proves (1).
Taking \(T=1\) and \(t^3\leq t^2\) proves (3).
If \(Y=0\), (5) gives zero loss and (4) gives a stationary solution, so the
same statements hold with zero remainder. This also checks the degenerate case.

## Operator-norm bound for the packet initialization

This part treats the random construction in exact arithmetic. Set the packet
width to \(q\geq2\), the source width to \(N\geq2\), and take the two
training vectors \(v_1=e_1,v_2=e_2\in\mathbb R^2\). Let

\[
H_{ia}=\tanh(A_{ia}),\qquad
K_H=H^\top H/q,\qquad
K_{\rm source}=H_{\rm source}^\top H_{\rm source}/N,
\]

where the entries of each first-layer Gaussian matrix are independent standard
normals, as in the initializer. The packet matrix \(Z\in\mathbb R^{q\times2}\)
satisfies \(Z^\top Z/q=K_{\rm source}\). The Gaussian matrix
\(G\in\mathbb R^{q\times q}\) has independent \(N(0,1/q)\) entries.
The argument needs no independence between \(Z\) and any of the other matrices.

For full-column-rank \(H\), define
\(H^\dagger=(H^\top H)^{-1}H^\top\) and the orthogonal projection
\(P=HH^\dagger\). The source code's reduced QR decomposition \(H=UR\)
and triangular solve give precisely

\[
B_0=G+(Z-GH)R^{-1}U^\top
   =G(I-P)+ZH^\dagger.
\tag{11}
\]

Because \((I-P)H=0\), its two summands have orthogonal input subspaces and

\[
B_0B_0^\top
=G(I-P)G^\top+Z(H^\top H)^{-1}Z^\top.
\]

Therefore

\[
\|B_0\|_{\mathrm{op}}^2
\leq\|G\|_{\mathrm{op}}^2
 +\frac{\|K_{\rm source}\|_{\mathrm{op}}}{\lambda_{\min}(K_H)}.
\tag{12}
\]

There is no Frobenius-norm penalty in this inequality. Bounded tanh features
give \(\operatorname{tr}(K_{\rm source})\leq2\), hence
\(\|K_{\rm source}\|_{\mathrm{op}}\leq2\), deterministically and uniformly
in the source width. The Gaussian-derived entries of \(H\) and
\(H_{\rm source}\) have continuous densities on \((-1,1)\). The determinant
of their first two rows is zero only on a Lebesgue-null subset, so both have
column rank two almost surely. The packet Gaussian QR factor also has rank
two almost surely. Thus the inverses and source Cholesky factor used in (11)
exist almost surely in the mathematical construction.

Here are explicit elementary probability bounds for (12). Define the positive
constant

\[
a=\mathbb E[\tanh(g)^2]
  =\frac1{\sqrt{2\pi}}\int_{\mathbb R}\tanh(u)^2e^{-u^2/2}\,du,
\qquad g\sim N(0,1).
\]

It satisfies \(0<a<1\), and for a fully elementary positive lower bound,

\[
a\geq\frac{2e^{-2}}{\sqrt{2\pi}}\tanh(1)^2>0,
\tag{13}
\]

by restricting the Gaussian integral to \([1,2]\cup[-2,-1]\).
The independence and oddness of the two tanh Gaussian coordinates show that
\(\mathbb E K_H=aI_2\).

For completeness, if an independent scalar sample \(X_i\) lies in an interval
of length \(L\), then
\(\mathbb E e^{\lambda(X_i-\mathbb EX_i)}\leq e^{\lambda^2L^2/8}\).
Indeed, the second derivative of its log moment-generating function is the
variance under exponential tilting. That tilted distribution has the same
support interval, and its variance is at most \(L^2/4\): subtracting the
interval midpoint bounds the second moment by \(L^2/4\), and variance is the
minimum second moment over choices of center. Integrating the second derivative
twice proves the displayed moment-generating-function bound. Independence,
Markov's inequality, and optimization over positive and negative \(\lambda\)
then give

\[
\mathbb P\left(\left|q^{-1}\sum_i(X_i-\mathbb EX_i)\right|>\varepsilon\right)
\leq2e^{-2q\varepsilon^2/L^2}.
\]

Apply this to the three distinct entries of \(K_H\), all with support
interval length at most two. A union bound and the fact that a \(2\times2\)
matrix whose entries are bounded by \(\varepsilon\) has operator norm at
most \(2\varepsilon\) yield

\[
\mathbb P\{\lambda_{\min}(K_H)<a/2\}
\leq6e^{-qa^2/32}.
\tag{14}
\]

This also directly proves convergence in probability of \(K_H\) to \(aI_2\).

To bound \(G\), choose a \(1/4\)-net \(\mathcal N\) of the unit sphere in
\(\mathbb R^q\) with at most \(9^q\) points. Such a net follows by taking
a maximal \(1/4\)-separated set: the disjoint radius-\(1/8\) balls around
its points lie in the radius-\(9/8\) ball, so comparison of volumes bounds
its size by \(9^q\); maximality supplies the covering property.
For any matrix, approximating each of its two unit test vectors by this net
gives

\[
\|G\|_{\mathrm{op}}
\leq2\max_{u,z\in\mathcal N}|u^\top Gz|.
\]

For fixed unit \(u,z\), the scalar \(u^\top Gz\) is centered Gaussian with
variance \(1/q\). Its moment-generating function and Markov's inequality give
\(\mathbb P\{|u^\top Gz|>r\}\leq2e^{-qr^2/2}\).
Taking a union bound with \(r=4\), and writing
\(c_G=8-2\log9>0\), proves

\[
\mathbb P\{\|G\|_{\mathrm{op}}>8\}\leq2e^{-c_Gq}.
\tag{15}
\]

Combining (12), (14), and (15) gives the explicit uniform bound

\[
\mathbb P\left\{\|B_0\|_{\mathrm{op}}
 >M_{\rm packet}\right\}
\leq6e^{-qa^2/32}+2e^{-c_Gq},
\qquad
M_{\rm packet}=\sqrt{64+4/a}.
\tag{16}
\]

For \(0<\delta<1\), the probability is at most \(\delta\) whenever

\[
q\geq\max\left\{2,\frac{32}{a^2}\log\frac{12}{\delta},
                     \frac1{c_G}\log\frac4\delta\right\}.
\tag{17}
\]

The bound is uniform in every \(N\geq2\). In particular,
\(\|B_0\|_{\mathrm{op}}=O_{\mathbb P}(1)\) as \(q\to\infty\), and the
flow estimate (1) holds with \(p=q\) and \(M=M_{\rm packet}\) on the event
in (16). In fact the family over all integers \(q\geq2,N\geq2\) is tight:
(16) controls all sufficiently large \(q\) uniformly; for each of the finitely
many smaller \(q\), (12), \(\|K_{\rm source}\|_{\mathrm{op}}\leq2\), and
the almost-sure positivity of \(\lambda_{\min}(K_H)\) give finite random
upper bounds whose tails vanish uniformly in \(N\).

## Check scope and remaining limitations

The author check rederived all three parameter velocities from the stated MSE
and mobilities, checked the dissipative identity, verified every normalized
norm cancellation, and expanded the QR initializer to (11). The two potentially
width-sensitive steps are the outer-product bound for \(\dot B\) and the
backward action for \(\dot A\); their cancellations are shown explicitly.
The proofs of the only concentration bounds used are included above.
No experiment or numerical approximation was used.

There is no remaining mathematical gap in the stated deterministic estimate or
the ideal random-initializer bound. These results do not establish any
comparison of two independently initialized networks, decoder approximation,
or trajectory agreement beyond the explicitly bounded Taylor remainder.
The source implementation uses floating-point QR, Cholesky, triangular solves,
and rank checks; rounding-error guarantees and probabilities of numerical
rejection are outside the exact-arithmetic result (16).
