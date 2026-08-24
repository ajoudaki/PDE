# Provisional Gudermannian candidate: exact depth-three operator contract

Status: exact C0--C1 candidate under Phase-I audit; it is not a convergence
theorem, 22 August 2026.

## 1. Activation and exact bottom coordinate

Take the fixed genuinely nonlinear activation

\[
 \phi(z)=\operatorname {gd}(z)
 =\arctan(\sinh z)=\arcsin(\tanh z),\qquad
 d(z)=\phi'(z)=\operatorname {sech}z.                 \tag{1.1}
\]

It is smooth, odd, bounded by \(a=\pi/2\), and has bounded derivatives of
every order.  Its phase identities are

\[
 \cos\phi(z)=d(z),\qquad \sin\phi(z)=\tanh z,qquad
 d(z)^2+\tanh^2z=1.                                   \tag{1.2}
\]

The natural bottom coordinate is particularly simple:

\[
 r=\Theta(u)=\sinh u,qquad u=\operatorname {arsinh}r,qquad
 X_1=\phi(u)=\arctan r.                               \tag{1.3}
\]

Writing

\[
 c(r)=(1+r^2)^{-1/2},\qquad \Psi(r)=\arctan r,
\]

one has \(r'=Q_1\) and \(\Psi'(r)=c(r)^2\).  The transformed
initial mark \(r_0=\sinh U_0\) lies in every finite \(L^p\), although it
is not polynomially bounded as a function of the Gaussian mark.  Source
identification therefore uses Gaussian truncation of \(U_0\), followed by
cutoff removal; it must not silently invoke a polynomial-growth tensor
program theorem on the untruncated map.

## 2. Exact finite current fields

On the normalized spaces fixed in `PROTOCOL.md`, set

\[
\begin{aligned}
 X_1&=\arctan r,&Z_2&=G_1X_1,&X_2&=\operatorname {gd}(Z_2),\\
 Z_3&=G_2X_2,&X_3&=\operatorname {gd}(Z_3),&
 f_n&=\langle A,X_3\rangle_n,\\
 B_3&=A\operatorname {sech}(Z_3),&R_2&=G_2^*B_3,&
 B_2&=\operatorname {sech}(Z_2)R_2,\\
 Q_1&=G_1^*B_2.&&&&
\end{aligned}                                         \tag{2.1}
\]

Feature ascent is exactly

\[
 \boxed{A'=X_3,\quad r'=Q_1,\quad
 G_1'=B_2\otimes X_1,\quad G_2'=B_3\otimes X_2.}     \tag{2.2}
\]

The raw tangent kernel is

\[
 \boxed{
 K_n=\|X_3\|_2^2+\|B_3\|_2^2\|X_2\|_2^2
 +\|B_2\|_2^2\|X_1\|_2^2+\|c(r)Q_1\|_2^2.}        \tag{2.3}
\]

These are the original mixed-metric parameter gradients, not a modified
flow in the \(r\) metric.

## 3. Fixed-species autonomous IDE

Let \(\Gamma_1,\Gamma_2\) be the two immutable jointly realized pointed
Gaussian actions, including their genuine adjoints, and let

\[
 G_1=\Gamma_1+P_1,\qquad G_2=\Gamma_2+P_2.             \tag{3.1}
\]

The proposed state has the fixed five species

\[
 (A,r,P_1,P_2,e).                                     \tag{3.2}
\]

Every field in (2.1) is reconstructed from the current state and the fixed
source.  Physical MSE time is

\[
 \boxed{
 \begin{aligned}
  \dot A&=2\eta eX_3,&\dot r&=2\eta eQ_1,\\
  \dot P_1&=2\eta eB_2\otimes X_1,&
  \dot P_2&=2\eta eB_3\otimes X_2,\\
  \dot e&=-2\eta eK,
 \end{aligned}}                                      \tag{3.3}
\]

with

\[
 A(0)=a_0,\quad r(0)=\sinh u_0,\quad P_1(0)=P_2(0)=0,
 \quad e(0)=y_\star.                                  \tag{3.4}
\]

The observations are

\[
 f=\langle A,X_3\rangle,\qquad K\text{ from (2.3)},
 \qquad \mathcal L=e^2.                               \tag{3.5}
\]

This contract is autonomous and restartable with the same immutable
source.  It contains no time-pair index, response kernel, delay, stored
trajectory, or list whose length grows with time.

## 4. Global single-trajectory bounds

On a feature-time interval \([-S,S]\), boundedness of every \(X_j\) gives

\[
 |A_i(s)-A_i(0)|\le aS,qquad
 \|A(s)\|_2\le\|A_0\|_2+aS.                          \tag{4.1}
\]

Since \(|B_3|\le|A|\), both current operator perturbations have bounded
trace-norm variation.  The operator norms of \(G_1,G_2\), followed by the
successive bounds on \(B_3,R_2,B_2,Q_1\), then bound \(r\) in \(L^2\).
Thus neither the finite system nor a sufficiently regular candidate IDE
can escape on a compact feature interval.  In physical time the signed
residual clock satisfies \(|s(t)|\le2\eta|y_\star|t+o_n(1)\).

The learned adjoint terms are pointwise tail-safe.  For example,

\[
 P_2(t)^*B_3(t)
 =\int_0^tX_2(s)\langle B_3(s),B_3(t)\rangle\,ds,     \tag{4.2}
\]

and \(|X_2|\le a\); the same statement holds at the lower matrix.

## 5. Exact phase lift

For a preactivation \(z\), let

\[
 h(z)=d(z)+i\tanh z=e^{i\phi(z)}.                     \tag{5.1}
\]

For any real cotangent carrier \(C\), define

\[
 p=d(z)C,\qquad q=\tanh(z)C,\qquad W=p+iq=h(z)C.      \tag{5.2}
\]

Then

\[
 p^2+q^2=C^2.                                         \tag{5.3}
\]

If \(V=z'\), the exact current-time equations are

\[
 p'=dC'-dqV,\qquad q'=\tanh(z)C'+dpV,qquad
 W'=hC'+idVW.                                         \tag{5.4}
\]

The velocity contribution is a pointwise skew rotation.  At the three
layers take \(C_3=A,C_2=R_2,C_1=Q_1\); the real components are precisely
\(B_3,B_2,c(r)Q_1\), the three derivative-weighted fields in (2.2)--(2.3).

The lift is finite-species and current-time, but (5.3) is a
single-trajectory identity.  For two different phase velocities the
relative-energy equation retains a multiplier by the comparison carrier;
phase rotation alone does not prove stability.

## 6. Why this candidate supersedes asinh provisionally

Gudermannian combines three mechanisms that the earlier candidates did not
simultaneously possess:

1. all forward features are uniformly bounded;
2. the readout remains a Gaussian mark plus a bounded coordinatewise shift;
3. the derivative and its complementary coordinate form the exact unit
   phase (5.1), while the bottom natural coordinate reduces to arctangent.

This makes every learned-adjoint contribution pointwise safe and leaves
only the immutable adaptive actions

\[
 \Gamma_2^*B_3,\qquad \Gamma_1^*B_2                 \tag{6.1}
\]

as stochastic tail obligations.  The finite-width stress experiment in
`audit_activation_tails.py` shows stable \(L^2,L^4,L^8\) diagnostics at
widths 128, 256, and 512 through feature time 1.5.  This is selection
evidence, not a convergence theorem.

## 7. Exact unresolved bridge

A natural strongest target is a moderate empirical sub-Gaussian estimate

\[
 \mathbb P\!\left\{
 \sup_{2\le p\le c_T\log n}p^{-1/2}\sup_{t\le T}
 \bigl(\|R_{2,n}(t)\|_{p,n}+\|Q_{1,n}(t)\|_{p,n}\bigr)
 \le C_T\right\}\longrightarrow1.                    \tag{7.1}
\]

A subexponential version with \(p^{-1}\) would still give the needed
Osgood modulus and square uniform integrability.  Neither has yet been
proved.

The row cavity has an exact scalar current Onsager coefficient, but a whole
column perturbation also changes the trainable readout and returns through
the same column at order one.  Hence replacing the true adjoint by a fresh
Gaussian plus an \(o(1)\) error is false.  A correct proof must control the
full order-one phase/carrier finite difference.  Its relative energy has an
uncancelled term of the form

\[
 \operatorname {Re}\langle\delta W,
 i\,\delta(dZ')\,W\rangle,                             \tag{7.2}
\]

which bare \(L^2\) bounds estimate using a carrier maximum and therefore
lose \(\sqrt{\log n}\).  Calling (7.1) a consequence of (5.3), operator
norms, or loss energy would be circular.

Accordingly this file freezes only the exact algebraic candidate.  It is
not promoted to C2--C6 unless (7.1), or an equivalent mesh-free
identification theorem, is proved without a delocalization assumption of
the same strength.
