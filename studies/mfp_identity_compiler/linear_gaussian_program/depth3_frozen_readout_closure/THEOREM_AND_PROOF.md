# Frozen-readout depth three collapses to the depth-two IDE

Status: exact finite-width reduction and inherited positive-time theorem,
20 August 2026.

## 1. Result

Consider

\[
X=u,\qquad Z=n^{-1/2}WX,\qquad
T=n^{-1/2}VZ,\qquad f_n=n^{-1}A^TT,
\tag{1.1}
\]

where \(A,V,W,u\) are independently standard Gaussian at initialization.
Freeze \(A\), train \(V,W,u\), and use the feature generator \(n\nabla f_n\).

Put

\[
a=A/\sqrt n,\qquad R=V/\sqrt n,\qquad
B=W/\sqrt n,\qquad x=u/\sqrt n.
\tag{1.2}
\]

Then

\[
f_n=a^TRBx.
\tag{1.3}
\]

Define the frozen scalar

\[
\alpha_n=\|a\|^2=\frac{\|A\|^2}{n}
\tag{1.4}
\]

and the contracted trainable readout

\[
p=R^Ta,\qquad q=p/\sqrt{\alpha_n},
\qquad \tau=\sqrt{\alpha_n}\,s.
\tag{1.5}
\]

Conditional on the frozen readout, the complete output-relevant finite-width
dynamics are exactly

\[
\boxed{
q_\tau=Bx,\qquad x_\tau=B^Tq,\qquad B_\tau=qx^T,}
\tag{1.6}
\]

and

\[
\boxed{
f_n(s)=\sqrt{\alpha_n}\,F_n(\tau),\qquad
K_{3,\mathrm{fr},n}(s)=\alpha_n K_{2,n}(\tau),}
\tag{1.7}
\]

where \(F_n=q^TBx\) and \(K_{2,n}=(F_n)_\tau\) are precisely the
two-hidden-layer scalar-output feature and kernel.

More generally, every feature derivative obeys the exact finite-width
scaling

\[
\frac{d^k f_n}{ds^k}(0)
=\alpha_n^{(k+1)/2}F_{2,n}^{(k)}(0).
\tag{1.7a}
\]

Thus the width-limit jet begins
\((0,3,0,48,0,1464,\ldots)\), not the fully trainable depth-three jet
\((0,4,0,160,0,13888,\ldots)\).  This is a normalization check and makes the
scope difference visible already at first order.

At initialization, conditional on \(a\),

\[
q_j(0)\overset{\mathrm{iid}}{\sim}N(0,1/n),
\tag{1.8}
\]

independently of \(B(0),x(0)\), while

\[
\alpha_n\longrightarrow1
\quad\text{almost surely}.
\tag{1.9}
\]

Thus the frozen-readout depth-three model has the same deterministic
single-source mean-field IDE as the established depth-two model.

## 2. Exact finite-width derivation

Differentiating (1.3) with respect to the raw trainable blocks under the
generator \(n\nabla f_n\), and then returning to normalized variables, gives

\[
a_s=0,\qquad
R_s=a(Bx)^T,\qquad
B_s=(R^Ta)x^T,\qquad
x_s=B^TR^Ta.
\tag{2.1}
\]

Since \(p=R^Ta\) and \(a\) is frozen,

\[
p_s=R_s^Ta=\|a\|^2Bx=\alpha_nBx.
\tag{2.2}
\]

Consequently the closed active subsystem is

\[
p_s=\alpha_nBx,\qquad
x_s=B^Tp,\qquad
B_s=px^T.
\tag{2.3}
\]

Substituting (1.5) and using \(d/d\tau=\alpha_n^{-1/2}d/ds\)
gives (1.6).  Equation (1.7) follows from

\[
f_n=p^TBx=\sqrt{\alpha_n}\,q^TBx
\]

and one further differentiation with respect to \(s\).

The corresponding exact invariants are

\[
\boxed{
C_n=BB^T-qq^T
=BB^T-\alpha_n^{-1}pp^T,\qquad
\|q\|^2-\|x\|^2.}
\tag{2.4}
\]

The component of \(R\) orthogonal to the frozen vector \(a\) is a spectator:
\(R_s\) has column-space direction \(a\), while both the output and the lower
blocks depend on \(R\) only through \(R^Ta=p\).  Hence no untracked
\(n\)-dimensional orientation feeds back into (2.3).

For (1.8), condition on \(a\).  Since the entries of \(R(0)\) are iid
\(N(0,1/n)\),

\[
\operatorname{Var}[p_j(0)\mid a]
=\frac{\|a\|^2}{n}=\frac{\alpha_n}{n},
\]

with zero conditional cross-covariances.  Division by
\(\sqrt{\alpha_n}\) proves (1.8).  The conditional law is independent of
\(a\), so \(q(0)\) is also independent of \(\alpha_n\).  Equation (1.9) is
the Gaussian law of large numbers.

## 3. Autonomous physical-time IDE

Use the same spectral domain, source measure, and initial profiles as at
depth two:

\[
\Lambda=\{-\tfrac12\}\cup(0,4),
\]

\[
d\nu(\lambda)=\frac34\delta_{-1/2}(d\lambda)
+\frac{(1+\lambda)\sqrt{\lambda(4-\lambda)}}
{\pi(1+2\lambda)}\mathbf1_{(0,4)}(\lambda)d\lambda,
\tag{3.1}
\]

\[
(\alpha_0,\beta_0)=
\begin{cases}
(1,0),&\lambda=-\tfrac12,\\[1mm]
\left([2(1+\lambda)]^{-1/2},
\sqrt{\dfrac{1+2\lambda}{2(1+\lambda)}}\right),
&0<\lambda<4.
\end{cases}
\tag{3.2}
\]

The subscripts on \(\alpha_0,\beta_0\) distinguish these profiles from the
finite-width readout norm \(\alpha_n\).  Set

\[
r=\int_\Lambda|\psi|^2d\nu,\qquad
K=\int_\Lambda
\bigl(|\pi|^2+(\lambda+2r)|\psi|^2\bigr)d\nu.
\tag{3.3}
\]

For full-MSE gradient flow over the trainable blocks,

\[
\dot\theta=-\eta n\nabla_\theta(y_\star-f_n)^2,
\]

let \(e=y_\star-f\).  Before taking width to infinity, the corresponding
finite-atomic spectral equations have the scalar readout-norm factors

\[
\partial_t\psi=2\eta\sqrt{\alpha_n}\,e\,\pi,\qquad
\partial_t\pi=2\eta\sqrt{\alpha_n}\,e(\lambda+2r)\psi,\qquad
\dot e=-2\eta\alpha_n eK.
\tag{3.4}
\]

Since \(\alpha_n\to1\), the deterministic limiting IDE is exactly

\[
\boxed{
\begin{aligned}
\partial_t\psi&=2\eta e\pi,\\
\partial_t\pi&=2\eta e(\lambda+2r)\psi,\\
\dot e&=-2\eta eK,
\end{aligned}}
\tag{3.5}
\]

with

\[
\psi(\lambda,0)=\alpha_0(\lambda),\qquad
\pi(\lambda,0)=i\beta_0(\lambda),\qquad e(0)=y_\star.
\tag{3.6}
\]

The output and loss are

\[
\boxed{
f(t)=y_\star-e(t)
=\operatorname{Re}\int_\Lambda\overline\psi\pi\,d\nu,
\qquad L(t)=e(t)^2,}
\tag{3.7}
\]

and

\[
\dot L=-4\eta K L.
\tag{3.8}
\]

Conditional finite-width equivalence (1.6), the independence in (1.8), and
\(\alpha_n\to1\) transfer the established compact-time convergence theorem:
for every finite \(T\),

\[
\sup_{0\le t\le T}
\left(|f_n(t)-f(t)|
+|(y_\star-f_n(t))^2-L(t)|\right)
\xrightarrow{\mathbb P}0.
\tag{3.9}
\]

The limiting physical solution is global and \(L(t)\to0\), by the same
feature-output bijection and scalar residual-clock argument as at depth two.

## 4. Why randomization does not change the source

The frozen Gaussian readout is a random fixed aggregate over the coordinates
of the third hidden layer.  Its orientation is immaterial for two exact
reasons:

1. the adjacent matrix evolves only in the readout direction, and the rest
   of that matrix never enters the output or lower-block gradients;
2. Gaussian rotational invariance makes the normalized contraction
   \(R(0)^Ta/\|a\|\) a fresh standard isotropic vector, independently of the
   lower network.

Only \(\|a\|\) survives at finite width, and it self-averages to one.  A
deterministic unit-norm averaging vector and a frozen Gaussian unit-norm
readout therefore belong to the same exact reduced dynamics and the same
mean-field universality class.

## 5. Exact boundary with fully trainable depth three

This result does not solve the usual fully trainable depth-three network.
If the readout is trained, then

\[
a_s=RBx.
\]

The contracted variable \(p=R^Ta\) instead obeys

\[
\boxed{
p_s=\|a\|^2Bx+R^TR\,Bx,}
\tag{5.1}
\]

because both \(R\) and \(a\) now move.  Also

\[
(\|a\|^2)_s=2f.
\tag{5.2}
\]

The additional evolving operator \(R^TR\) is precisely absent in the frozen
case and is not summarized by the scalar norm.  Therefore the frozen-readout
theorem is a genuine stepping stone, but not a proof that the fully trainable
depth-three model has the same one-source IDE.  The next bottleneck is to find
an invariant or a fixed-size operator-valued spectral closure for the extra
term in (5.1).
