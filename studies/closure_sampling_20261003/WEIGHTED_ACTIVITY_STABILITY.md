# Weighted activity stability with two-sided source defects

2026-10-03. Scoped deterministic lemma supporting
CANONICAL_NEURON_COMPRESSION.md. This note proves real stability, fitting,
and transfer to the original physical clock. It assumes the stated
source defects; it does not prove their initialization-only construction
or a complex-analytic source theorem. No experiments or Git operations
were used. The canonical-notation and rigorous-proof skills apply.

## 1. Weighted model and uniform real tube

Let D_1,D_2 be positive diagonal matrices on the retained lower and upper
neurons, with tr(D_1)=tr(D_2)=1. Use the norms and adjoint

\[
 \|v\|_{D_i}=(v^\top D_iv)^{1/2},\quad
 B^*=D_1^{-1}B^\top D_2,\quad
 \|B\|_{\rm HS}=\|D_2^{1/2}BD_1^{-1/2}\|_F.
\]

The operator norm is from the D_1 space to the D_2 space. It is at
most the displayed Hilbert--Schmidt norm, and
\[
 \|xy^\top D_1\|_{\rm HS}=\|x\|_{D_2}\|y\|_{D_1}.             \tag{1}
\]
These are identities after conjugating by the square roots of D_i.
Consequently none of the estimates below depends on the smallest mass.

Train on x_1=sqrt(2)e_1. The two first-layer columns are a and beta,
with beta fixed during training. Define the globally increasing function
\[
 \Psi(a)=a/2+\sinh(2a)/4,\quad u=\Psi(a),\quad
 \sigma(u)=\tanh(\Psi^{-1}(u)).
\]
It has derivative cosh^2(a), tends to both infinities, and hence has a
real inverse on all of R. Its inverse and sigma satisfy
\[
 (\Psi^{-1})'(u)=\operatorname{sech}^2a\le1,\qquad
 \sigma'(u)=\operatorname{sech}^4a\le1.                    \tag{2}
\]
Both are globally 1-Lipschitz on the real line, coordinatewise.

Primes below denote activity derivatives. The weighted dense equations are
\[
 h=\sigma(u),\ z=Bh,\ g=\tanh z,\ 
 \delta=w\odot\operatorname{sech}^2z,\quad
 u'=B^*\delta,\quad B'=\delta h^\top D_1,\quad w'=g.        \tag{3}
\]
In the ordinary coordinate, a'=sech^2(a) odot B^*delta.
Thus (3) is an exact coordinate change, not a different training flow.
Assume w(0)=0, ||B(0)||_op<=K and ||g(0)||_{D_2}^2>=gamma>0.

Since each real tanh has absolute value at most one, on 0<=s<=S,
\[
 \|w(s)\|_\infty\le s,\quad \|\delta(s)\|_{D_2}\le s,\quad
 \|B(s)-B(0)\|_{\rm HS}\le s^2/2,\quad
 \|B(s)\|_{\rm op}\le K_S:=K+S^2/2.                     \tag{4}
\]
In particular, ||u(s)-u(0)||_{D_1}<=K s^2/2+s^4/8.
Using (2), then subtracting Bh-B(0)h(0), yields
\[
 \|h(s)-h(0)\|_{D_1}+\|g(s)-g(0)\|_{D_2}\le C_Ks^2
                                                               \tag{5}
\]
for S<=1. All bounds are independent of the absolute size of u(0).
The equations are locally smooth on real finite-dimensional space; (4)
and the finite u increment prevent escape on [0,S], proving existence.

The training prediction F(s)=w(s)^TD_2g(s) has derivative
\[
 F'(s)=\|g\|_{D_2}^2+\|\delta\|_{D_2}^2\|h\|_{D_1}^2
       +\|\operatorname{sech}^2a\odot B^*\delta\|_{D_1}^2. \tag{6}
\]
Indeed differentiating F gives ||g||^2+<delta,z'>; then
z'=B'h+B diag(sech^2a)a', and the adjoint identity gives the
last two nonnegative terms. Choose a fixed S>0 so (5) changes the
initial g norm by at most sqrt(gamma)/2. Then, throughout [0,S],
\[
 \kappa:=\gamma/4\le F'(s)\le
 \Lambda:=1+S^2+K_S^2S^2.                              \tag{7}
\]
This proves the same tube and gap for every weighted model satisfying
the same two initialized bounds, without a carrier maximum.

## 2. Reference restrictions and source assumptions

Let the full width-n dense reference satisfy the same initialization
bounds, with normalized Euclidean norms and its ordinary mixer W.
Write its activity solution as u(s), h(s,theta), z(s,theta), g(s,theta),
w(s), delta(s), where theta denotes the passive circle input
x_theta=sqrt(2)(cos(theta),sin(theta)). Training means theta=0.
The first-layer query preactivation is a cos(theta)+beta sin(theta).

Fix retained indices I,J and a matrix B_0 of weighted operator norm <=K.
Define the following matrix only for comparison:
\[
 B_R(s)=B_0+\int_0^s
             \delta(v)_J h(v,0)_I^\top D_1\,dv.          \tag{8}
\]
It has norm <=K_S by the same rank-one bound, because the original
reference satisfies |w_j(s)|<=s. Put u_R=u_I, w_R=w_J,
h_R=h(s,0)_I, delta_R=delta_J and z_R=z(s,0)_J.

Assume, uniformly for s in [0,S] and every real theta,
\[
 \|B_R(s)h(s,\theta)_I-z(s,\theta)_J\|_{D_2}
       \le\epsilon_f,\qquad
 \|B_R(s)^*\delta_R(s)-u_R'(s)\|_{D_1}
       \le\epsilon_b,                                  \tag{9}
\]
\[
 |w_R(s)^\top D_2g(s,\theta)_J-f_n(s,x_\theta)|
       \le\epsilon_p.                                  \tag{10}
\]
The reverse derivative in (9) is exactly
u_R'=(W(s)^Tdelta(s))_I, by the original coordinate change.
The analytic cubature construction must prove (9)--(10); the present
lemma does not assume that a small forward defect implies a reverse one.

Initialize the compressed system (3) by u_C(0)=u_R(0),
B_C(0)=B_0, w_C(0)=0, beta_C=beta_I. Assume its initialized training
Gram also has lower bound gamma. This holds in the cited construction
by exact initial matching. Both systems consequently satisfy (4)--(7).

## 3. Stability with constants independent of neuron weights

Set U=||u_C-u_R||_{D_1}, M=||B_C-B_R||_HS,
V=||w_C-w_R||_{D_2}, and d=U+M+V. By (2),
||h_C-h_R||_{D_1}<=U. Subtracting the forward products gives
\[
 Z:=\|B_Ch_C-z_R\|_{D_2}\le K_SU+M+\epsilon_f.            \tag{11}
\]
The function sech^2 has derivative of absolute value at most two.
Subtract its product with w using the bounded reference w_R to obtain
\[
 Q:=\|\delta_C-\delta_R\|_{D_2}\le V+2SZ.                 \tag{12}
\]
Only the coordinate bound |w_R|<=S appears. There is no bound on
individual reference reverse carriers in (11)--(12).

Subtract the three evolution equations. The u equation uses the second
defect in (9); the B_R derivative in (8) is exact. Equation (1) yields
\[
 D^+U\le K_SQ+SM+\epsilon_b,\quad
 D^+M\le Q+SU,\quad D^+V\le Z.                          \tag{13}
\]
For example, the u difference is
B_C^*(delta_C-delta_R)+(B_C-B_R)^*delta_R
+(B_R^*delta_R-u_R'); the first two terms have the stated operator
bounds. The matrix difference is
(delta_C-delta_R)h_C^TD_1+delta_R(h_C-h_R)^TD_1.
Norm Dini derivatives at zero follow by regularizing the norm.

Substituting (11)--(12) into (13) gives, for a constant L depending
only on K,S,
\[
 D^+d\le Ld+L\epsilon_f+\epsilon_b,\qquad d(0)=0.
\]
The elementary integrating-factor inequality therefore proves
\[
 \sup_{0\le s\le S}d(s)
       \le S e^{LS}(L\epsilon_f+\epsilon_b).             \tag{14}
\]
This is a fixed-activity estimate. Its constants involve neither a
minimum mass, a population size, an initial u norm, nor a reference
carrier maximum. The physical time interval will be unbounded.

For any real theta, (2) and the equality of retained beta imply
||h_C(s,theta)-h(s,theta)_I||_{D_1}<=U. Repeating (11) for this
query, subtracting the readout pairing, and applying (10) proves
\[
 \eta:=\sup_{s\in[0,S],\,\theta\in\mathbb R}
 |f_C(s,x_\theta)-f_n(s,x_\theta)|
       \le C(\epsilon_f+\epsilon_b+\epsilon_p).         \tag{15}
\]
Indeed the error before (10) is at most
V+S(K_SU+M+epsilon_f). This controls all queries simultaneously.

## 4. Physical clocks and fitted endpoints

Choose 0<y<=kappa S/2. For either model, (7) and F(0)=0 give
a unique activity s_* in (0,S/2] with F(s_*)=y. Define its own
physical clock by
\[
 \dot s(t)=2[y-F(s(t))],\qquad s(0)=0.                   \tag{16}
\]
Uniqueness and the sign show 0<=s(t)<s_* at finite t and monotone
convergence to s_*. More explicitly, y-F(s(t)) has derivative
-2F'(s(t))[y-F(s(t))], so it lies between
y exp(-2Lambda t) and y exp(-2kappa t). The parameter path therefore
has the fitted endpoint given by its continuous activity solution at s_*.

Let s_C(t),s_n(t) denote these distinct physical clocks. Monotonicity
of F_C with derivative at least kappa gives
\[
 D^+|s_C-s_n|\le-2\kappa|s_C-s_n|+2\eta,
 \qquad |s_C(t)-s_n(t)|\le\eta/\kappa.                  \tag{17}
\]
To verify the first inequality, insert and subtract F_C(s_n) in the
difference of (16). The first term has the dissipative sign by (7);
the remaining F_C(s_n)-F_n(s_n) is bounded by (15).

For the original reference, the derivative of every circle-query
prediction in activity is uniformly bounded by a constant C_K.
Indeed ||a'||_2/sqrt(n)<=K_Ss, ||h_theta'||_2/sqrt(n)<=K_Ss,
||W'||_op<=s, and ||z_theta'||_2/sqrt(n)<=s+K_S^2s.
Differentiating w^Tg_theta/n, using ||w'||_2/sqrt(n)<=1 and
||w||_2/sqrt(n)<=s, gives the asserted bound. These estimates also
hold for the weighted model but only the original one is needed.
Combining this query derivative with (15) and (17) proves
\[
 \sup_{t\in[0,\infty],\,\theta\in\mathbb R}
 |f_C(t,x_\theta)-f_n(t,x_\theta)|
       \le C(1+\kappa^{-1})
                 (\epsilon_f+\epsilon_b+\epsilon_p).   \tag{18}
\]
The value at infinity is justified by the already proved convergence
of both activity clocks and continuous query predictors. This completes
the source-to-trajectory comparison, including fitting and the endpoint,
without changing either model's physical clock.
