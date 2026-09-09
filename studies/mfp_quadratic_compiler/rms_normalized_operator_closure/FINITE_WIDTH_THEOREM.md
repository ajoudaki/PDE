# Exact finite-width theorem

This file uses the frozen convention in `PROTOCOL.md`.  A prime is unit
feature ascent and a dot is full-MSE physical time.

## 1. Normalization calculus

For

\[
N_\epsilon(v)=v/\sigma_v,\qquad
\sigma_v^2=\langle v,v\rangle_n+\epsilon,
\]

put

\[
\Pi_{N(v)}=I-N(v)\otimes N(v).
\]

Then, exactly,

\[
DN_\epsilon(v)[\delta v]
=\sigma_v^{-1}\Pi_{N(v)}\delta v.                 \tag{1.1}
\]

The symbol `Pi` is mnemonic, not a claim of idempotence.  It is symmetric
positive definite: it is the identity on `N(v)^perp` and has eigenvalue
`epsilon/sigma_v^2` on the span of `N(v)`.  Thus the derivative eigenvalues
are `1/sigma_v` tangentially and `epsilon/sigma_v^3` radially.

For the network define

\[
\Pi_H=I-H\otimes H,\qquad \Pi_Y=I-Y\otimes Y,
\]

and the row and column backpropagates

\[
C=\Pi_YA=A-fY,\qquad
R={2\over\beta}Z\odot C,\qquad
g=G^{\mathsf T}R,\qquad T=\Pi_Hg.                 \tag{1.2}
\]

## 2. Parameter dynamics and tangent kernel

For arbitrary perturbations,

\[
d\alpha=\langle H,dX\rangle_n,\qquad
dH=\alpha^{-1}\Pi_HdX,
\]
\[
d\beta=\langle Y,dV\rangle_n,\qquad
dY=\beta^{-1}\Pi_YdV.                             \tag{2.1}
\]

Consequently

\[
\boxed{
A'=Y,\qquad G'=R\otimes H,\qquad
u'={2\over\alpha}u\odot T.}                       \tag{2.2}
\]

Here `(R tensor H)_{ij}=R_iH_j/n`.  In particular,

\[
\|R\otimes H\|_F^2
=\langle R^2\rangle_n\langle H^2\rangle_n,        \tag{2.3}
\]

which is the decisive matrix-metric factor.

The exact tangent kernel is the sum of the three block-gradient norms:

\[
\boxed{
K=K_A+K_G+K_u
=\langle Y^2\rangle_n
\langle H^2\rangle_n\langle R^2\rangle_n
{4\over\alpha}\langle H\odot T^2\rangle_n.}       \tag{2.4}
\]

Equivalently, the last term is
`4 alpha^{-2}<X T^2>_n`.  Direct differentiation gives the exact identity

\[
f'=K.                                               \tag{2.5}
\]

For `e=y_*-f` and `L=e^2`, physical flow is

\[
\boxed{
\dot A=2\eta eY,\quad
\dot G=2\eta eR\otimes H,\quad
\dot u={4\eta e\over\alpha}u\odot T,\quad
\dot e=-2\eta eK,\quad
\dot L=-4\eta e^2K.}                               \tag{2.6}
\]

Thus

\[
e(t)=e(0)\exp\left(-2\eta\int_0^tK(s)\,ds\right), \tag{2.7}
\]

so the residual cannot cross zero.

## 3. Complete feature equations

Let `h=<H^2>_n`.  Then

\[
X'={4\over\alpha}X\odot T,\qquad
\alpha'=4\langle H^2\odot T\rangle_n,
\]
\[
H'={4\over\alpha}\Pi_H(H\odot T),                 \tag{3.1}
\]
\[
Z'=hR+{4\over\alpha}G\Pi_H(H\odot T),             \tag{3.2}
\]
\[
V'=2Z\odot Z',\qquad
\beta'={2\over\beta}\langle Z^3,Z'\rangle_n,
\qquad
Y'={2\over\beta}\Pi_Y(Z\odot Z').                \tag{3.3}
\]

Every right-hand side in physical time is multiplied by `2 eta e`.
Two exact alignment identities, including the radial leakage, are

\[
\boxed{
\langle H,g\rangle_n=\langle Z,R\rangle_n
={2\epsilon f\over\beta^2},\qquad
T=g-{2\epsilon f\over\beta^2}H.}                   \tag{3.4}
\]

They verify (2.5):

\[
\langle R,Z'\rangle_n
=h\langle R^2\rangle_n+{4\over\alpha}
 \langle H\odot T^2\rangle_n.
\]

With the raw initialized matrix `W=sqrt(n)G`, the exact row and column
balance laws are

\[
\boxed{
\left(\sum_jW_{ij}^2-2A_i^2\right)'
=-4fY_i^2,}                                         \tag{3.5}
\]

\[
\boxed{
\left(\sum_iW_{ij}^2-\frac12u_j^2\right)'
={4\epsilon f\over\beta^2}H_j^2.}                  \tag{3.6}
\]

They become the familiar exact balancedness invariants only at
`epsilon=0`.  At positive regularization the radial leakage gives the
displayed signed drifts; neither identity is a coordinate-spike bound.
Physical time again multiplies both right-hand sides by `2 eta e`.

## 4. Exact elimination of the raw first-layer coordinate

Since

\[
h=1-\epsilon/\alpha^2,
\qquad \alpha=\sqrt{\epsilon/(1-h)},                \tag{4.1}
\]

the output-relevant dynamics do not need `u` or its signs.  Define the
positive current-state operator

\[
\mathcal Q_H={4\over\alpha}\Pi_HM_H\Pi_H,           \tag{4.2}
\]

where `M_Hv=H odot v`.  Then `H'=Q_H g` and

\[
K_u=\langle g,\mathcal Q_Hg\rangle_n.               \tag{4.3}
\]

Writing the fixed pretrajectory Gaussian source as `Gamma=G(0)` and
`Q=G-Gamma`, the exact finite-width reduced system is

\[
\boxed{
\begin{aligned}
Z&=(\Gamma+Q)H,\quad Y=N_\epsilon(Z^2),\quad
f=\langle A,Y\rangle_n,\\
R&={2\over\beta}Z\odot(I-Y\otimes Y)A,\\
A'&=Y,\\
Q'&=R\otimes H,\\
H'&=\mathcal Q_H(\Gamma+Q)^{\mathsf T}R.
\end{aligned}}                                      \tag{4.4}
\]

It is autonomous and restartable at finite width.  It is not yet a
width-independent closure: constructing the adaptive forward and transpose
actions of `Gamma` after pointwise nonlinearities is the limiting problem.

## 5. Finite-width global existence

Both denominators are at least `sqrt(epsilon)`, so the finite-dimensional
vector field is smooth.  Gradient-flow dissipation gives

\[
\|\dot\theta\|_{\mu P}^2=4\eta^2e^2K=-\eta\dot L.
\]

Hence, for `0 <= s <= t`,

\[
\int_s^t\|\dot\theta\|_{\mu P}^2
=\eta(L(s)-L(t)),
\]
\[
\|\theta(t)-\theta(s)\|_{\mu P}
\le\sqrt{\eta(t-s)(L(s)-L(t))}.                     \tag{5.1}
\]

At fixed `n` this rules out escape to infinity on a finite interval, and
smooth local existence can therefore be continued globally.  The same bound
is dimension-free in the muP metric, but it controls neither coordinate
maxima nor the weighted products in `K`.

## 6. Almost-sure nondegeneracy and initialization limits

At every fixed width all three gradients in (2.2) are nonzero almost surely.
Indeed `u_i` and `Z_i` are all nonzero almost surely; `Pi_H` and `Pi_Y` are
invertible; `G` is invertible almost surely; and the remaining exceptional
conditions are proper Gaussian linear subspaces.  Therefore

\[
K_A>0,\qquad K_G>0,\qquad K_u>0                      \tag{6.1}
\]

almost surely.

Put

\[
a=3+\epsilon,\qquad s={3\over a},\qquad
b^2=3s^2+\epsilon,
\qquad D=a^2b^2=27+\epsilon(3+\epsilon)^2.           \tag{6.2}
\]

At iid Gaussian initialization, in probability,

\[
\alpha^2\to a,\quad \langle H^2\rangle_n\to s,
\quad\beta^2\to b^2,\quad f\to0,                   \tag{6.3}
\]

and conditional Gaussian laws plus Wick contraction give

\[
\boxed{
K_A\to{27\over D},\qquad
K_G\to{36\over D},\qquad
K_u\to{48\over D},\qquad
K\to{111\over D}.}                                 \tag{6.4}
\]

For the nontrivial last limit, one first proves

\[
\langle X\odot g^2\rangle_n\to{4s\over b^2},       \tag{6.5}
\]

by conditioning on `(u,W)`, taking the Gaussian quadratic form in `A`, and
using

\[
\mathbb E[Z_i^2\sum_jX_jG_{ij}^2\mid u]
=\langle H^2\rangle_n\langle X,1\rangle_n
{2\over n}\langle X\odot H^2,1\rangle_n.
\]

Equation (3.4) makes the `Pi_H` correction `o_P(1)` at initialization.

## 7. Genuine nonlinearity and feature learning

The parameter-to-output map is not affine.  For fixed nonzero `Z_0=G_0H`,
restriction to the line `G=cG_0` is

\[
f(c)={c^2\langle A,Z_0^2\rangle_n
\over\sqrt{c^4\langle Z_0^4\rangle_n+\epsilon}},    \tag{7.1}
\]

which is non-affine whenever its numerator is nonzero, an almost-sure event
at Gaussian initialization.

More importantly, the hidden blocks do not disappear in the width limit:
(6.4) assigns them the positive fractions `36/D` and `48/D` of the initial
output speed.  The coherent matrix update changes the preactivation at
order one:

\[
Z'_G=G'H=hR,
\qquad
\|Z'_G(0)\|_n^2\to{4s^3\over b^2}>0.                \tag{7.2}
\]

Indeed its induced normalized second-hidden representation also moves at
order one,

\[
\|(Y'_G)(0)\|_n^2\to{48s^4\over b^4}>0.             \tag{7.3}
\]

An independent contraction of the complete first normalized-feature
velocity gives

\[
\|H'(0)\|_n^2\to{64s^2\over ab^2}
={576\over aD}>0.                                   \tag{7.4}
\]

Physical velocities multiply these limits by `(2 eta e(0))^2`; they are
positive for the canonical nonzero target.  Thus individual matrix entries
move by `O(1/n)` but their coherent action moves features by `O(1)`.  This
rules out readout-only, frozen-feature, and instantaneous lazy/linearized
descriptions.  It does not by itself prove a compact-time kernel limit; that
is a separate gate.
