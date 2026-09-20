# Loss gradient plus projected selection: lead derivation

2026-09-19. Candidate derived independently by the lead before reading the
parallel constrained route. Inputs: this study's complete canonical-feature,
model/geometry and selected-target proofs. No other studies or experiments.
The model, data, canonical marks, unhalved loss and physical norms are unchanged.
The optimizer changes the relative hidden learning rate and adds a secondary
direction in the kernel of the full training Jacobian. The noise is a random
ODE, not an Itô equation. Internal review is required before acceptance.

## 1. Explicit constants and fixed coordinates

Use h=(w,M), h0=(g,D), A_h, Y, sigma=lambda_min(A_h0 A_h0*)>0,
r, a1, a3, C_J from MODEL_AND_GEOMETRY.md; |Y|=1 and sigma<=1.
All compatible observations have already been merged into m representatives.
Let

\[
 b=\sqrt{2/\sigma},\qquad R=12/\sigma,
 \qquad \epsilon=\sigma/8,\qquad
 0<\eta\le\sqrt{\epsilon/4}.
\]

Choose a finite rho>=1 so large that

\[
\begin{split}
\rho&\ge C_J+1+4J(h_0)/r^2,\qquad R/\sqrt\rho\le r,\qquad
 2a_1/(\sigma\sqrt\rho)\le1,\\
\ell:=2a_1/\sqrt\rho+a_3R/\rho
&\le\min\{\epsilon/8,\sigma/16,1/(4bR)\}.
\end{split}\tag{1}
\]

Every right-hand side is a strictly positive data-defined number. Thus these
inequalities give an explicit finite prescription: put d equal to the minimum
on the second line and take rho at least all first-line bounds, (4a1/d)^2,
and 2a3 R/d. No future state or optimization outcome is used.

Define fixed Hilbert coordinates

\[
 z=(\sqrt\rho(h-h_0),c),\qquad
 f(z)=A_{h_0+z_h/\sqrt\rho}c,\qquad e=f(z)-Y,
 \quad T_z=Df(z).
\]

The finite vector f is weighted training prediction, not a passive predictor.
For ||z||<=R, h lies in the certified radius-r hidden ball. Then

\[
 T_zT_z^*\succeq A_hA_h^*\succeq(\sigma/2)I,
 \quad \|T_z\|\le\sqrt{1+a_1^2\|z\|^2/\rho},
 \quad \operatorname{Lip}(T)\le\ell.                 \tag{2}
\]

Indeed T[v]=(DA_h[v_h/sqrt(rho)])c+A_h v_c. For the derivative difference,
changing c and A contributes at most a1/sqrt(rho) times each corresponding
coordinate difference, and changing DA contributes a3 R/rho times the hidden
coordinate difference. Their sum is bounded by ell ||delta z||||v||.
These are C1,1 estimates, not an assumed Hilbert C2 property.

The current orthogonal projection onto variations invisible to all training
predictions to first order is

\[
 P_z=I-T_z^*(T_zT_z^*)^{-1}T_z.                       \tag{3}
\]

Only the current full Jacobian and an m-by-m matrix inverse are used. P includes
the true first-layer and middle-layer adjoints of the closure. Its bounded local
Lipschitz regularity follows from (2) and the finite inverse identity.

## 2. The rule

At fixed positive refresh intervals draw a unit-bounded vector U_t in the fixed
Hilbert z space, and hold it between refreshes. Define

\[
 \dot z=-2T_z^*e-\epsilon P_z z+\eta |e|P_z U_t,
 \qquad z(0)=0.                                      \tag{4}
\]

This is the ordinary gradient of the unhalved training loss in z coordinates,
plus projected quadratic regularization and projected vanishing noise. Both
extra terms are annihilated by T_z. There are no derivatives of P, no reduced
objective J in the update, no separate readout transport, and no auxiliary dual
variables. In physical coordinates the loss term is

 (dot h,dot c)=(-rho^{-1} grad_h L,-grad_c L).

Thus a smaller positive hidden learning rate is a real restriction, not an
unmodified physical-gradient claim. Multiplying the entire vector field by rho
gives an equivalent path formulation with the original hidden loss-gradient
coefficient and a rho-times faster readout rate, provided the forcing is also
reparameterized from U_t to U_(rho t), with refresh interval divided by rho.
This is an explicitly changed clock/rate prescription, not an equality in the
original clock with an unchanged noise schedule.

Noise directions may be fixed functions of the existing marks. To ensure a
nontrivial process for every m, choose m+1 linearly independent bounded readout
fields (e.g. odd powers Z1,Z1^3,...,Z1^(2m+1), individually normalized), and draw
U uniformly from their signed pairs, with zero hidden components. At z=0 the
normal space has dimension m. At least one of these directions has P0 U!=0,
so positive eta gives distinct initial velocities with positive probability.
All conclusions below hold for every permitted bounded direction sequence.

## 3. Confinement and exact loss dissipation

Because TP=0, the actual residual satisfies

\[
 \dot e=-2T_zT_z^*e,\qquad
 \dot L=-4\|T_z^*e\|^2\le-2\sigma L.                \tag{5}
\]

Before a possible exit from ||z||<R, |e(t)|<=exp(-sigma t).
Let s=||z||. Since <z,Pz>=||Pz||², Cauchy--Schwarz gives

\[
 D^+s\le[2+\eta+(2a_1/\sqrt\rho)s]|e|.             \tag{6}
\]

The bound uses sqrt(1+u²)<=1+u and remains valid at s=0 by the upper
one-sided derivative. Integrating (6) and using integral |e|<=1/sigma yields

\[
 s(t)\le\frac{2+\eta}{\sigma}
          \exp(2a_1/(\sigma\sqrt\rho))
       <9/\sigma< R.                                \tag{7}
\]

Here eta<1 and exp(1)<3. The strict margin excludes any first exit. All
coefficients in (4) are locally Lipschitz on an open neighborhood of this
reached set and bounded there. A finite maximal time would have a strong
Cauchy endpoint by bounded velocity; local continuation from that endpoint
contradicts maximality. This proves global existence and uniqueness for each
noise sequence without invoking compactness of a Hilbert ball.

## 4. Unique selected endpoint

The selected-target proof applies with any rho satisfying its displayed lower
bound, hence with (1). It gives a unique interior minimizer h_* of

 J(h)+rho ||h-h0||²/2,   ||h-h0||<=r,

and the readout
\[
c_*=A_{h_*}^*K_{h_*}^{-1}Y.
\]
Define z_*=(sqrt(rho)(h_*-h0),c_*).
Equivalently z_* uniquely minimizes ||z||²/2 among fitted states in that hidden
ball. Since the initialized-hidden minimum readout is feasible,

\[
 \|z_*\|^2\le2J(h_0)\le1/\sigma,\qquad
 z_*=-T_{z_*}^*\lambda_*,\quad
 \lambda_*=-K_{h_*}^{-1}Y,\quad |\lambda_*|\le2/\sigma.
                                                               \tag{8}
\]

The readout stationarity identity is c_*=-A_{h_*}^* lambda_*. For every
hidden variation v, the derivative identity for J gives
rho<h_*-h0,v>+<lambda_*,(DA_{h_*}[v])c_*>=0.
Thus P_{z_*} z_*=0 and z_* is an equilibrium of (4). Its definition is fixed
by data, initialization and rho; it is not an input to (4).

## 5. Global exponential attraction inside the proved region

Write delta=z-z_*, d=||delta||, P=P_z, and N=I-P. Both endpoints of the
connecting segment lie in the convex radius-R ball. C1,1 Taylor integration
at z gives

\[
 T_z\delta=e+v,\qquad |v|\le\ell d^2/2.
\]

The normal projector and (2) imply

\[
 \|N\delta\|\le b(|e|+\ell d^2/2)
              \le b|e|+b\ell R d,
\]

because d<=2R. Since b ell R<=1/4,

\[
 \|P\delta\|^2\ge(7/8)d^2-2b^2|e|^2.             \tag{9}
\]

By (8), Pz_*=-P(T_{z_*}-T_z)^*lambda_*, hence
||Pz_*||<=ell |lambda_*| d. Therefore

\[
 \langle\delta,Pz\rangle
 \ge(3/4)d^2-2b^2|e|^2,                             \tag{10}
\]

using ell |lambda_*|<=1/8. The loss-gradient term satisfies

 -2<delta,T_z* e> <= -2|e|²+ell |e| d² <= -2|e|²+ell d².

The noise obeys the pointwise Young bound

 eta |e| <delta,P U> <= (epsilon/8)d²+(2eta²/epsilon)|e|².

Insert these and (10) into (4). Since ell<=epsilon/8,
2epsilon b²=1/2 (epsilon=sigma/8), and 2eta²/epsilon<=1/2,

\[
 \frac12\frac d{dt}d^2
 \le-\frac\epsilon2d^2-|e|^2.                       \tag{11}
\]

In particular the legitimate fixed-target potential

\[
 \Psi(S)=\tfrac12\{\rho\|h-h_*\|^2+\|c-c_*\|^2\}
\]

obeys dot Psi<=-epsilon Psi. Its target is the proved unique solution of
the explicit fixed variational problem, not an endpoint oracle. On the reached
ball, (2) and f(z_*)=Y give L<=2D² Psi, with
D=sqrt(1+a1²R²/rho). Therefore

\[
 L(t)\le e^{-2\sigma t}L(0),\quad
 \|z(t)-z_*\|\le e^{-\epsilon t/2}\|z_*\|.         \tag{12}
\]

Since rho>=1, this controls the original physical state norm as well. All
constants are independent of the noise realization. The established direct
state-to-predictor inequality in PASSIVE_LIMITS.md implies uniform exponential
convergence on the circle and locally uniform convergence on R² to the same
fitted predictor f_*. Finite physical travel follows too: the complete vector
field vanishes at z_*, its deterministic part is locally Lipschitz, and its
noise magnitude is <=eta |e|, all bounded by integrable exponentials.

## 6. What was simplified, and what remains a restriction

The update uses the original loss gradient in a fixed layer metric, a projected
quadratic preference and bounded projected noise of size sqrt(L). It does not
use grad J, current minimum-norm fitted readouts, readout-reset phases, candidate
acceptance/rejection, projector derivatives or a supplied selected endpoint.
The preferred endpoint is the same minimum-hidden-displacement/readout-norm
interpolant as in the previous construction for this rho. It permits data-
dependent changes in both hidden blocks, rather than returning h to h0.

The fixed hidden/readout learning-rate ratio can be very unequal for difficult
geometry. The full Jacobian projection still requires an m-by-m inverse and is
not ordinary minibatch noise. The selection correction persists on the zero-loss
manifold until its unique preferred state is reached; pure noise alone would
not impose that preference. No near-original-GF limit, uniform computational
cost, unbounded hidden motion or higher-p theorem is claimed.
