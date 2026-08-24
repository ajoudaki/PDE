# Fully trained three-hidden-layer tanh mean field: exact closure, conditional blueprint, and open bridge

**Audit date:** 22 August 2026
**Frozen model:** three hidden `tanh` layers, one scalar sample, fully trained
input feature, both hidden matrices, and readout
**Claim status:** the exact finite dynamics and the autonomous current-time
operator closure are proved algebraically; unconditional well-posedness and
the requested compact-time nonzero-label width theorem are still open.  The
target is neither proved nor disproved.

This report supersedes no earlier proved theorem.  It reconciles and extends the
following authoritative artifacts:

- the complete two-hidden-layer nonlinear theorem in
  `../nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md` and its
  `FINAL_AUDIT.md`;
- the complete fully trained depth-three linear operator theorem in
  `../identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md`;
- the frozen tanh contract in `FROZEN_CONTRACT.md`;
- the earlier tanh audits in `RESOLUTION_AUDIT.md`, `EVIDENCE_LEDGER.md`, and
  `PROOF_ROUTE_REGISTRY.md`.

The new rigorously established identities, criteria, and diagnostics recorded
here are:

1. exact current-time cotangent evolution identities in which the naked
   readout and raw cotangents cancel;
2. a quantitative no-focusing theorem on every deterministic vanishing
   physical-time window;
3. a corrected one-column cavity criterion with all measurability and width
   factors explicit;
4. a corrected Gaussian creation--response criterion for square uniform
   integrability; and
5. a rigorous obstruction to closing that criterion from the established
   normalized-`L2` and trace bounds by a Schatten-(4) Gronwall estimate.

None of these five facts proves the positive-time adaptive-transpose estimate.

## 1. Frozen research contract and claim levels

For every fixed physical horizon `T`, the requested theorem must prove

\[
 \sup_{0\le t\le T}
 \bigl(|f_n(t)-f(t)|+|K_n(t)-K(t)|
       +|\mathcal L_n(t)-\mathcal L(t)|\bigr)
 \xrightarrow{\mathbb P}0.                                      \tag{1.1}
\]

The label `y_*` is any fixed real number.  In particular, the theorem may not
use `y_*=0`, freeze any parameter, change the activation, or alter the
architecture.  The limiting state must have one current training time and a
number of field/operator species independent of width, elapsed time, mesh,
and proof order.  It must retain the actual adjoints of the initialized
matrices.  Two-time response or covariance kernels and trajectory-indexed
sources are excluded.

The admissible terminal claim levels are therefore:

- **complete positive theorem:** (1.1), all source/tail/mesh bridges, and
  well-posedness are unconditional;
- **complete negative theorem:** a reachable counterexample or impossibility
  theorem for this exact contract;
- **open:** anything weaker, including an exact IDE, a fixed-mesh theorem, or
  a conditional adaptive-Gaussian theorem.

The result of this audit is the third claim level.

## 2. Exact finite-width system

### 2.1 Spaces, initialization, and metrics

Let

\[
 H_n=(\mathbb R^n,\langle v,w\rangle_n),\qquad
 \langle v,w\rangle_n=\frac1n v^{\mathsf T}w,\qquad
 \|v\|_n^2=\langle v,v\rangle_n.                       \tag{2.1}
\]

For vectors `b,x`, define the normalized rank-one operator

\[
 (b\otimes x)h=b\langle x,h\rangle_n
 =\frac1n bx^{\mathsf T}h.                              \tag{2.2}
\]

The vector parameters `u,A` carry the `H_n` metric.  Each matrix parameter
has the ordinary Frobenius metric.  Initialize independently by

\[
 u_{0,i},A_{0,i}\stackrel{\mathrm{iid}}\sim N(0,1),
 \qquad
 (\Gamma_{\ell,n})_{ij}\stackrel{\mathrm{iid}}\sim N(0,1/n),
 \quad \ell=1,2,                                      \tag{2.3}
\]

and put `G_l(0)=Gamma_l`.  This is exactly the normalization inherited from
the accepted two-hidden-layer theorem.

### 2.2 Forward and backward fields

Suppress the subscript `n` when no ambiguity is possible and set

\[
\begin{aligned}
 x_1&=\tanh u,                 &D_1&=1-x_1^2,\\
 z_2&=G_1x_1, &x_2&=\tanh z_2, &D_2&=1-x_2^2,\\
 z_3&=G_2x_2, &x_3&=\tanh z_3, &D_3&=1-x_3^2,\\
 f_n&=\langle A,x_3\rangle_n.&&&
\end{aligned}                                                   \tag{2.4}
\]

All products with a `D_l` are coordinatewise.  Reverse differentiation gives

\[
\begin{aligned}
 B_3&=D_3A,& Q_2&=G_2^*B_3,&B_2&=D_2Q_2,\\
 Q_1&=G_1^*B_2,& B_1&=D_1Q_1.&&
\end{aligned}                                                   \tag{2.5}
\]

Because both matrix domain and codomain use the same normalized Hilbert
metric, `G_l^*` is its ordinary transpose.  It is not an independent
backward Gaussian matrix.

### 2.3 Riemannian gradients and physical time

For a variation of `G_2`,

\[
 \delta f_n
 =\frac1nB_3^{\mathsf T}(\delta G_2)x_2
 =\operatorname {Tr}\bigl[(B_3\otimes x_2)^{\mathsf T}
                            \delta G_2\bigr],           \tag{2.6}
\]

and similarly one layer lower.  The exact feature-ascent equations are

\[
 \boxed{
 A'=x_3,\qquad u'=B_1,\qquad
 G_2'=B_3\otimes x_2,\qquad
 G_1'=B_2\otimes x_1.}                                  \tag{2.7}
\]

Let

\[
 e_n=y_*-f_n,\qquad \mathcal L_n=e_n^2.                \tag{2.8}
\]

Gradient descent on the full MSE with learning-rate constant `eta` is

\[
 \dot\theta=2\eta e_n\nabla f_n.                        \tag{2.9}
\]

Thus every right-hand side in (2.7) is multiplied by

\[
 \alpha_n(t)=2\eta e_n(t).                              \tag{2.10}
\]

There is no additional width factor in physical time.

Equivalently, while the residual is nonzero, the signed feature coordinate

\[
 \varsigma_n(t)=2\eta\int_0^t e_n(r)\,dr                 \tag{2.10a}
\]

satisfies `d theta/d varsigma=grad f` and

\[
 \frac{d\varsigma_n}{dt}=2\eta e_n,
 \qquad
 \frac{dt}{d\varsigma_n}=\frac1{2\eta e_n}.            \tag{2.10b}
\]

Equation (2.12) below shows that a nonzero residual never changes sign.  If
it is zero, the physical trajectory is stationary, so the clock convention
extends by continuity.

### 2.4 Exact tangent kernel and energy law

The squared norm of the Riemannian gradient is

\[
 \boxed{
 K_n=\|x_3\|_n^2
 +\|B_3\|_n^2\|x_2\|_n^2
 +\|B_2\|_n^2\|x_1\|_n^2
 +\|B_1\|_n^2.}                                        \tag{2.11}
\]

Indeed, (2.2) gives
`||b \otimes x||_F=||b||_n ||x||_n`.  Consequently

\[
 \boxed{
 \dot f_n=2\eta e_nK_n,\qquad
 \dot e_n=-2\eta e_nK_n,\qquad
 \frac d{dt}e_n^2=-4\eta e_n^2K_n.}                   \tag{2.12}
\]

These identities are exact at every width and for every label.
In particular,

\[
 e_n(t)=e_n(0)\exp\!\left(-2\eta\int_0^tK_n(r)\,dr\right), \tag{2.12a}
\]

so a nonzero residual preserves its sign.
The same metric calculation gives

\[
 \|\dot\theta\|_{\rm par}^2=4\eta^2e_n^2K_n,
 \qquad
 \dot{\mathcal L}_n=-\eta^{-1}\|\dot\theta\|_{\rm par}^2. \tag{2.12b}
\]

### 2.5 Compact physical-time bounds

From (2.12), `|e_n(t)|<=|e_n(0)|`.  Since `|x_l|<=1`,

\[
 \sup_{t\le T}\|A(t)\|_n
 \le \|A_0\|_n+2\eta T|e_n(0)|.                         \tag{2.13}
\]

The rank-one trace norm identity

\[
 \|b\otimes x\|_{S_1}=\|b\|_n\|x\|_n                 \tag{2.14}
\]

then bounds `P_2=G_2-Gamma_2` in trace norm.  This bounds `G_2` in operator
norm, hence `B_2`; the same argument next bounds `P_1,G_1,B_1`.  On every
fixed `T`, all normalized vector norms, both learned trace norms, both matrix
operator norms, and `K_n` are therefore tight uniformly in `n`.  The finite
ODE has no compact-time explosion.

## 3. Immutable joint Gaussian source

The correct source has three sorts.  Start with independent endpoint marks
`u_0` in sort 1 and `a_0` in sort 3, two independent matrix letters from
sort 1 to 2 and sort 2 to 3, their transposes, scalar normalized inner
products, finite linear combinations, and coordinatewise pseudo-Lipschitz
maps.  A source program contains only finitely many such operations.

**Lemma 3.1 (fixed three-sort transpose-reusing programs).**  For any one
fixed program in this language and any finite list of same-sort output
fields, their empirical joint law converges almost surely against every fixed
pseudo-Lipschitz test of finite degree to a deterministic law.  Every program
scalar converges almost surely, and the empirical fields converge in every
fixed finite Wasserstein `W_p`.  The statement permits adaptive alternating
reuse of each `Gamma_l` and its transpose and permits singular limiting query
Gram matrices.

This is the two-matrix specialization of the transpose-aware master theorem.
Its hypotheses hold because the two Ginibre letters are independent, the
endpoint coordinate pairs are iid Gaussian and independent of them, and all
coordinate maps and moment scalars in a fixed clipped Euler program are
pseudo-Lipschitz of fixed finite degree.  The theorem supplies a deterministic
joint empirical law, including all fixed polynomial moments, for every fixed
finite program.

Taking one countable convergence-determining program language and
its projectively consistent laws yields probability Hilbert spaces

\[
 H_1=L^2(\Omega_1),\qquad H_2=L^2(\Omega_2),\qquad
 H_3=L^2(\Omega_3),                                    \tag{3.1}
\]

with their coordinatewise probability-algebra functional calculi.  On the
dense program fields define the two actions and transpose actions.  The
finite Gaussian spectral-norm theorem
`||Gamma_{ell,n}||_{op}->2` almost surely gives, on the completed limiting
source,

\[
 \|\Gamma_\ell v\|_2\le2\|v\|_2,\qquad
 \|\Gamma_\ell^*w\|_2\le2\|w\|_2.                     \tag{3.2}
\]

Passing the finite identity

\[
 \langle \Gamma_{\ell,n}v_n,w_n\rangle_n
 =\langle v_n,\Gamma_{\ell,n}^{\mathsf T}w_n\rangle_n \tag{3.3}
\]

through every program proves that the backward action is the genuine Hilbert
adjoint of the forward action.

The immutable source is therefore

\[
 \boxed{
 \mathfrak G_3=(H_1,H_2,H_3; u_0,a_0,
                 \Gamma_1,\Gamma_1^*,\Gamma_2,\Gamma_2^*;
                 \text{coordinate functional calculus}).}       \tag{3.4}
\]

It is determined by initialization alone.  It contains neither the label nor
the future trajectory.  Its finite-program convergence topology is the joint
pointed-action topology: every finite list of source expressions converges in
each fixed Wasserstein `W_p`, with its scalar moments.  No operator-norm
convergence of the finite matrices to the source operators across widths is
asserted; only the scalar norm limit used in (3.2) is invoked.

## 4. Exact autonomous one-time IDE

Let

\[
 P_1\in\mathfrak S_1(H_1,H_2),\qquad
 P_2\in\mathfrak S_1(H_2,H_3),\qquad
 G_\ell=\Gamma_\ell+P_\ell.                            \tag{4.1}
\]

Use the activated input coordinate `Y=tanh u`.  The present state is

\[
 \boxed{\mathcal X(t)=(Y(t),A(t),P_1(t),P_2(t),e(t)).} \tag{4.2}
\]

The vector field is not asserted on every point of the ambient `L2` product
space.  Its natural admissible domain is

\[
 \mathcal D_{\rm adm}=\{(Y,A,P_1,P_2,e):
   Y\in L^\infty(\Omega_1)\subset H_1,\ \|Y\|_\infty\le1,\ A\in H_3,
   \ P_1,P_2\in\mathfrak S_1,\ e\in\mathbb R\},       \tag{4.2a}
\]

and define the canonical coordinate domain

\[
 \mathcal D_{\rm can}=\{\mathcal X\in\mathcal D_{\rm adm}:
       |Y|<1\ \hbox{ a.s.},\ \operatorname {artanh}(Y)\in H_1\}. \tag{4.2b}
\]

All restartability statements mean restarting from a current
canonical/reachable state in `D_can`, with the same immutable
source.  Along such solutions `u=artanh(Y)`, and (4.4) gives
`dot u=2 eta e B_1`.  Thus using `Y` is a coordinate change, not a
frozen-input reduction.  No vector field on arbitrary `Y in H_1` is claimed.

From it and the immutable source, recompute all fields in the following
strictly current-time order:

\[
\begin{aligned}
 D_1&=1-Y^2,\\
 z_2&=G_1Y,&x_2&=\tanh z_2,&D_2&=1-x_2^2,\\
 z_3&=G_2x_2,&x_3&=\tanh z_3,&D_3&=1-x_3^2,\\
 B_3&=D_3A,&Q_2&=G_2^*B_3,&B_2&=D_2Q_2,\\
 Q_1&=G_1^*B_2,&B_1&=D_1Q_1.&&
\end{aligned}                                                   \tag{4.3}
\]

The candidate limiting IDE is

\[
 \boxed{
\begin{aligned}
 \dot Y&=2\eta eD_1B_1,&
 \dot A&=2\eta ex_3,\\
 \dot P_1&=2\eta eB_2\otimes Y,&
 \dot P_2&=2\eta eB_3\otimes x_2,\\
 \dot e&=-2\eta eK,
\end{aligned}}                                                   \tag{4.4}
\]

where

\[
 K=\|x_3\|_2^2+\|B_3\|_2^2\|x_2\|_2^2
   +\|B_2\|_2^2\|Y\|_2^2+\|B_1\|_2^2.                \tag{4.5}
\]

The remaining direct readouts are

\[
 f=\langle A,x_3\rangle_{H_3},\qquad
 \mathcal L=e^2.                                       \tag{4.5a}
\]

The initial state is

\[
 Y(0)=\tanh u_0,\quad A(0)=a_0,\quad
 P_1(0)=P_2(0)=0,\quad e(0)=y_*.                      \tag{4.6}
\]

The source law gives `f(0)=<a_0,x_3(0)>=0`.  Along any sufficiently regular
solution, direct differentiation yields `dot f=2 eta e K`, so
`e+f=y_*` is preserved.

Equation (4.4) is algebraically autonomous and restartable.  Although

\[
 P_\ell(t)=\int_0^t2\eta e(s)
 B_{\ell+1}(s)\otimes x_\ell(s)\,ds                  \tag{4.7}
\]

is useful in a proof, the state stores only the current extensional
trace-class operator `P_l(t)`, not its rank-one history.  The number of state
species is fixed.  The only time argument is `t`.

## 5. Exact cotangent evolution and what it cancels

Put `alpha=2 eta e` and define

\[
 H_2=\|Y\|_2^2B_2+G_1(D_1B_1),\qquad
 H_3=\|x_2\|_2^2B_3+G_2(D_2H_2).                       \tag{5.1}
\]

Then

\[
 \dot z_2=\alpha H_2,\quad \dot x_2=\alpha D_2H_2,
 \qquad
 \dot z_3=\alpha H_3,\quad \dot x_3=\alpha D_3H_3.   \tag{5.2}
\]

Set

\[
\begin{aligned}
 R_3&=D_3x_3-2x_3B_3H_3,\\
 S_2&=x_2\|B_3\|_2^2+G_2^*R_3,\\
 R_2&=D_2S_2-2x_2B_2H_2,\\
 S_1&=Y\|B_2\|_2^2+G_1^*R_2,\\
 R_1&=D_1S_1-2YB_1^2.
\end{aligned}                                                   \tag{5.3}
\]

Using `(b \otimes x)^*v=x<b,v>`, the product rule, and
`dot D_l=-2 alpha x_l D_l H_l`, one obtains the exact identities

\[
 \boxed{\dot B_3=\alpha R_3,\qquad
        \dot B_2=\alpha R_2,\qquad
        \dot B_1=\alpha R_1.}                          \tag{5.4}
\]

For example,

\[
 \dot Q_2=\dot G_2^*B_3+G_2^*\dot B_3
 =\alpha\{x_2\|B_3\|_2^2+G_2^*R_3\}.                \tag{5.5}
\]

The important cancellation is

\[
 D_\ell'(z_\ell)Q_\ell=-2x_\ell B_\ell,              \tag{5.6}
\]

and `D_3'(z_3)A=-2x_3B_3`.  Thus the first differentiated cotangent
equations contain neither a naked `A` nor a naked ungated `Q_l`.  This is a
real simplification, but (5.3) still contains adaptive transpose actions and
anisotropic products such as `B_l H_l`.

The differential identities (5.1)--(5.4) apply to the exact continuous
flow.  A clipped flow has the corresponding clipped inner products, and an
explicit Euler step has finite-difference tanh remainders; those variants may
not silently be assigned (5.4).

### 5.1 Positive Gram transport factorization

All primes in Sections 5.1--5.3 mean differentiation with respect to the
signed feature coordinate `varsigma` from (2.10a), and all identities in
those subsections are finite-width identities.  Physical-time versions gain
the common factor `alpha=2 eta e`.  Frobenius norms involving the immutable
matrices are not asserted at the source limit.

The forward velocities admit a sharper current factorization.  Define

\[
\begin{aligned}
 \mathcal K_2&=\|Y\|_2^2I+G_1D_1^2G_1^*\succeq0,\\
 \mathcal K_3&=\|x_2\|_2^2I+
     G_2D_2\mathcal K_2D_2G_2^*\succeq0.
\end{aligned}                                                   \tag{5.7}
\]

Since `B_1=D_1G_1^*B_2` and `B_2=D_2G_2^*B_3`,

\[
 H_2=\mathcal K_2B_2,\qquad H_3=\mathcal K_3B_3,       \tag{5.8}
\]

and the entire raw kernel factors as

\[
 K=\|x_3\|_2^2+\langle B_3,\mathcal K_3B_3\rangle.    \tag{5.9}
\]

This proves positivity without expanding the four squares.  It does not
make the coordinatewise transport `p`-dissipative for `p>2`.

The deep-linear adjacent balancedness invariants do not survive tanh.  With

\[
 c(r)=\tanh r-r\operatorname {sech}^2r,
\]

one instead has

\[
\begin{aligned}
 (\|A\|_2^2-\|G_2\|_F^2)'
   &=2\langle A,c(z_3)\rangle,\\
 (\|G_2\|_F^2-\|G_1\|_F^2)'
   &=2\langle Q_2,c(z_2)\rangle,\\
 (\|G_1\|_F^2-\|u\|_2^2)'
   &=2\langle Q_1,c(u)\rangle.
                                                               \tag{5.9a}
\end{aligned}
\]

Although `r c(r)>=0`, none of `A,Q_2,Q_1` has the matching coordinatewise
sign.  These balances therefore provide no monotone tail energy.

### 5.2 Exact input-column balance law

Let `g_j=G_{1,:,j}`, `gamma_j=Gamma_{1,:,j}`,
`delta_j=g_j-gamma_j`, and put

\[
 \Phi(r)=\frac12\sinh^2r,
 \qquad \Phi'(r)=\frac{\tanh r}{\operatorname {sech}^2r}.
                                                                  \tag{5.10}
\]

In feature time,

\[
 g_j'=\frac{Y_j}{n}B_2,qquad
 u_j'=D_{1,j}Q_{1,j}.                                  \tag{5.11}
\]

Therefore, coordinate by coordinate,

\[
 \boxed{
 \frac d{d\varsigma}\left\{\Phi(u_j)-\frac n2\|g_j\|_{\ell^2}^2\right\}=0,}
                                                                  \tag{5.12}
\]

and, after subtracting the immutable column,

\[
 \boxed{
 \frac d{d\varsigma}\left\{\Phi(u_j)-\frac n2\|\delta_j\|_{\ell^2}^2\right\}
 =Y_j(\Gamma_1^*B_2)_j.}                               \tag{5.13}
\]

The compact energy bounds give
`sqrt(n)||delta_j||_{ell^2}<=S sup_{|varsigma|<=S}||B_2(varsigma)||_n`,
uniformly in `j`.
Minkowski applied to (5.13), together with the ordinary `L2` operator bound
on `Gamma_1^*B_2`, yields

\[
 \sup_{|\varsigma|\le S}\|\Phi(u(\varsigma))\|_{2,n}=O_{\mathbb P,S}(1),
 \qquad
 \sup_{|\varsigma|\le S}\|D_1(\varsigma)^{-1}\|_{2,n}
 =O_{\mathbb P,S}(1).                                  \tag{5.14}
\]

Equivalently, the exact flow has a compact-time empirical fourth exponential
moment for `u`.  This is an unconditional nonlinear balance estimate not
contained in bare parameter energy.

It is also sharp.  The static fields

\[
 q=\sqrt n e_1,\qquad D_1=n^{-1/2}\text{ at coordinate }1,
 \qquad B_1=D_1q=e_1                                \tag{5.15}
\]

have bounded normalized `L2` norms for `q,B_1,Phi(u)`, but `q` has no
uniform `L^{2+epsilon}` or empirical `psi_1` bound.  Thus (5.14) does not
imply the missing square tails.

There is a scoped completeness statement for this balance strategy.  If a
separable column functional depends only on

\[
 r_j=\frac n2\|g_j\|_{\ell^2}^2
\]

and `u_j`, then along (5.11)

\[
 \frac d{d\varsigma}E(u_j,r_j)
 =Q_{1,j}\{D_{1,j}E_u+Y_jE_r\}.                        \tag{5.16}
\]

For it to be invariant for every current cotangent, the bracket must vanish.
The characteristic equation shows that every such invariant is

\[
 E(u,r)=F(r-\Phi(u)).                                   \tag{5.17}
\]

Hence no stronger separable input-column balance is waiting to be chosen.

### 5.3 Why positive Gram transport does not yield a tail entropy

In this subsection, `\langle H(Q)\rangle` denotes the normalized coordinate
average and all two-field brackets are normalized Hilbert inner products.
For any differentiable convex `H` and scalar `c`, exact differentiation gives

\[
\begin{aligned}
 \frac d{d\varsigma}\{\langle H(Q_2)\rangle-c\langle Q_2,x_2\rangle\}
={}&\|B_3\|_2^2\langle H'(Q_2),x_2\rangle\\
 &+\langle G_2H'(Q_2)-cz_3,B_3'\rangle
 -c\langle B_3,\mathcal K_3B_3\rangle,               \tag{5.18}\\
 \frac d{d\varsigma}\{\langle H(Q_1)\rangle-c\langle Q_1,Y\rangle\}
={}&\|B_2\|_2^2\langle H'(Q_1),Y\rangle\\
 &+\langle G_1H'(Q_1)-cz_2,B_2'\rangle
 -c\langle B_2,\mathcal K_2B_2\rangle.               \tag{5.19}
\end{aligned}
\]

The last terms have the favorable sign when `c>0`.  The preceding
cross-layer pairings are sign-indefinite.  For
`H(r)=|r|^p/p`, absolute control of one such term requires
`||Q||_{2p-2}^{p-1}` and therefore raises `p=2+epsilon` to
`2+2epsilon`; iteration does not close.

This is not cured by a different superquadratic Orlicz function.  Estimating
an `L2` forcing by Cauchy--Schwarz requires

\[
 |H'(r)|^2\le C\{1+H(r)\}.                              \tag{5.20}
\]

Then `sqrt(1+H)` is Lipschitz, so necessarily
`H(r)<=C(1+r^2)`.  Such an entropy is not superquadratic and cannot prove
square uniform integrability.

Nor does positivity of `mathcal K_l` give `p`-dissipation.  For
`c>1`, `v=(1,c)`, `b=(a,-1)`, `mathcal K=v \otimes v`, and
`c^{1/(p-1)}<a<c`,

\[
 \langle |b|^{p-2}b,\mathcal Kb\rangle
 =(a^{p-1}-c)(a-c)<0.                                  \tag{5.21}
\]

Finally, for `B=DQ`, `B'=DS-2xBH`, one has the exact weighted identity

\[
 \frac d{d\varsigma}\frac1p\langle D^{-\gamma}|B|^p\rangle
 =\langle D^{1-\gamma}|B|^{p-2}B,S\rangle
 -2\left(1-\frac\gamma p\right)
  \langle xH D^{-\gamma}|B|^p\rangle.                 \tag{5.22}
\]

The second term has no sign unless `gamma=p`; at that value the energy is
exactly `||Q||_p^p/p` and the response/moment jump is fully exposed.  These
facts rigorously block the absolute local-entropy architecture.  They do not
rule out a Gaussian-specific signed or reachable cancellation.

The balance law itself also fails to give a free Euler bridge.  One explicit
step has a positive Taylor remainder involving
`Phi''(u)=cosh(2u)` and a quadratic matrix-update term.  The critical bound
(5.14) does not control that remainder uniformly over width and mesh.

## 6. Conditional well-posedness and convergence reduction

### 6.1 The exact missing hypothesis

The learned adjoint pieces are current bounded-coordinate fields.  For
example,

\[
 P_2(t)^*B_3(t)=\int_0^t2\eta e(s)x_2(s)
       \langle B_3(s),B_3(t)\rangle_{H_3}\,ds,         \tag{6.0}
\]

and the analogous formula holds for `P_1^*B_2`.  The forward factor has
absolute value at most one and the scalar contraction is bounded by the
compact energy estimates.  Thus only the immutable pieces below can carry
the unresolved coordinate tail.

At width `n`, write only the immutable parts of the two middle transpose
queries:

\[
 q_{2,n}(t)=\Gamma_{2,n}^{\mathsf T}B_{3,n}(t),\qquad
 q_{1,n}(t)=\Gamma_{1,n}^{\mathsf T}B_{2,n}(t).        \tag{6.1}
\]

Here is the comparison family used in the conditional blueprint.  Let
`chi_R(r)=max(-R,min(r,R))`.  The `R`-clipped current vector field is obtained
by the exact forward reconstruction, followed by

\[
\begin{aligned}
 B_3^R&=D_3\chi_R(A),\\
 \widehat Q_2^R&=\chi_R(G_2^*B_3^R),&B_2^R&=D_2\widehat Q_2^R,\\
 \widehat Q_1^R&=\chi_R(G_1^*B_2^R),&B_1^R&=D_1\widehat Q_1^R,
\end{aligned}                                                   \tag{6.1a}
\]

and by using these clipped cotangents in (4.4) and (4.5).  This is a fixed
coordinatewise 1-Lipschitz program; `R=infinity` is the exact vector field.

Fix a deterministic `L_0` large enough for the Gaussian square-exponential
moment and define the initialization/energy event

\[
 \mathcal E_{n,M}=\left\{
 |e_n(0)|+\|A_0\|_n+\sum_{\ell=1}^2\|\Gamma_{\ell,n}\|_{\rm op}
 +\frac1n\sum_i e^{A_{0,i}^2/L_0^2}\le M\right\}.      \tag{6.1b}
\]

These events exhaust probability as `M->infinity`.  On `E_{n,M}`, the
a-priori estimates give a deterministic state ball on `[0,T]`.  Let
`K_{T,M,R}^{max}` be a deterministic upper bound for the clipped kernel on
that ball, and choose `L_{T,M,R}` to dominate a deterministic Lipschitz bound
for the clipped vector field, `2 eta K_{T,M,R}^{max}`, and
`(32/27)(2 eta M)R`.  Define `C_{n,T,M}` to contain:

1. the exact finite continuous flow;
2. every continuous `R`-clipped flow, `R` a positive integer; and
3. the piecewise-linear interpolation of explicit Euler for that clipped
   field on the uniform mesh `h=T/m`, for every integer `m` with
   `h L_{T,M,R}<=1/2`.

This family is fixed before seeing a trajectory.  Cutoff, mesh, and
interpolation conventions are therefore not selected after the proof.  The
extra mesh restriction preserves `|Y|<=1`: indeed
`Y^+=Y+h alpha(1-Y^2)^2 \widehat Q_1`, `|\widehat Q_1|<=R`, and
`max_{|y|<=1}(1-y)(1+y)^2=32/27` (with the symmetric lower-bound
calculation).  It also makes the Euler residual multiplier
`1-2 eta h K` lie in `[1/2,1]`.  Thus `|e|<=M`, and piecewise-linear
interpolation remains in `D_adm`.

For fixed `T`, let `(AG_T)` mean that there is one deterministic
`C_T<\infty` such that, for every localization level `M`,

\[
 \sup_{c\in\mathcal C_{n,T,M}}\sup_{t\le T}
 \frac1n\sum_{j=1}^n\sum_{\ell=1}^2
 e^{|q_{\ell,n,j}^{c}(t)|/C_T}
 =O_{\mathbb P,T,M}(1)\quad\hbox{on }\mathcal E_{n,M}. \tag{6.2}
\]

This is a reachable-trajectory statement, not a bound over every state in an
`L2` ball.  It is a hypothesis on the finite exact and comparison systems;
the source solution is then constructed as their limit, so the conditional
existence assertion is not assumed in the definition.

More explicitly, (6.2) means that for every fixed `M`,

\[
 \lim_{\Lambda\to\infty}\limsup_{n\to\infty}
 \mathbb P\!\left[
  \mathcal E_{n,M}\cap\left\{
  \sup_{c\in\mathcal C_{n,T,M}}\sup_{t\le T}
  \frac1n\sum_j\sum_{\ell=1}^2
       e^{|q^{c}_{\ell,n,j}(t)|/C_T}>\Lambda
       \right\}\right]=0.                              \tag{6.2a}
\]

A weaker sufficient condition uses deterministic localized square-tail
envelopes.  For every localization level `M`, require events `E_{n,T,M}` and
a deterministic function `bar tau_{T,M}(R) downarrow 0`, with
`E_{n,T,M}` measurable from the finite initialization and the fixed
comparison algorithms and contained in `mathcal E_{n,M}`, such that

\[
 \lim_{M\to\infty}\limsup_n\mathbb P(E_{n,T,M}^c)=0,   \tag{6.3}
\]

and, on `E_{n,T,M}`, every comparison path satisfies

\[
 \sup_{c,t,\ell}
 \|q_{\ell,n}^{c}(t)\mathbf1_{|q_{\ell,n}^{c}(t)|>R}\|_2
 \le\bar\tau_{T,M}(R).                                \tag{6.4}
\]

Define the deterministic modulus

\[
 \omega_{T,M}(\delta)=\inf_{R\ge1}
 \{R\delta+2\bar\tau_{T,M}(R)\}.                     \tag{6.5}
\]

It suffices that, for every fixed `M`,

\[
 \int_{0^+}\frac{d\delta}
 {\delta+\omega_{T,M}(\delta)}=\infty.                \tag{6.5a}
\]

Condition (6.2), localized jointly at an energy level `M` and an empirical
exponential-average threshold `Lambda`, supplies such a deterministic
envelope and gives an Osgood modulus of order
`delta log(e/delta)`.  The pair `(M,Lambda)` may be relabelled as the single
localization index in (6.3)--(6.5a).

### 6.2 Multiplier lemma

If a current field `q` satisfies an empirical/source `\psi_1` bound, then
`||q||_{2p}<=C p`.  If `w=h(z)-h(\widetilde z)` for a bounded Lipschitz
gate, then

\[
 \|w\|_2\le C\delta,\qquad \|w\|_\infty\le C.
\]

Hölder and interpolation give

\[
 \|qw\|_2
 \le \|q\|_{2p}\|w\|_{2p/(p-1)}
 \le Cp\,\delta^{1-1/p}.                               \tag{6.6}
\]

Choosing `p` comparable to `log(e/delta)` yields

\[
 \|qw\|_2\le C\delta\log(e/\delta).                   \tag{6.7}
\]

With the localized tail envelope (6.4), splitting at height `R` gives the
modulus (6.5) directly.  Equation (6.5a) is exactly the Bihari--Osgood
uniqueness condition.

### 6.3 Conditional convergence blueprint

The following is the exact intended conditional statement, but this report
does **not** promote it to a completed theorem: in addition to `(AG_T)`, four
uniform comparison lemmas listed below still require a fully written proof.

**Conditional target 6.1.**  Fix `T<\infty`, `eta>0`, and any `y_* in R`.
Assume `(AG_T)`, or the weaker uniform comparison-family condition
(6.3)--(6.5a), and assume comparison lemmas C1--C4 below.  Then:

1. (4.4) has a unique solution, among reachable comparison limits satisfying
   the stated `psi_1` or localized Osgood tail control, in
   \[
 C([0,T];H_1\oplus H_3\oplus\mathfrak S_1(H_1,H_2)
                  \oplus\mathfrak S_1(H_2,H_3)\oplus\mathbb R),
   \tag{6.8}
   \]
   where vectors have strong `L2` topology and learned operators have trace
   norm topology, with the limiting trajectory also lying in the canonical
   domain (4.2b).
2. `P_1,P_2` are trace-norm absolutely continuous; every reconstructed
   forward and backward field is strongly `L2` continuous; `f` is `C^1` and
   `dot f=2 eta e K`; and `K` is continuous.
3. The exact finite systems satisfy
   \[
   \sup_{0\le t\le T}
   \left(|f_n(t)-f(t)|+|K_n(t)-K(t)|
         +|e_n(t)-e(t)|+|\mathcal L_n(t)-e(t)^2|\right)
   \xrightarrow{\mathbb P}0.                           \tag{6.9}
   \]

#### Established reduction and remaining comparison lemmas

On a fixed cutoff and a fixed Euler mesh, every state and adjoint evaluation
is one finite two-matrix, transpose-reusing source program.  The source
theorem therefore identifies its full joint law and every fixed moment.  At
that fixed number of steps, each learned `P_l` has fixed finite rank; its
left/right Gram matrices converge entrywise, hence its nonzero singular
values and trace norm converge.  This verifies the operator/action passage
at a fixed mesh, not uniformly as the rank grows.

For two current states on an a-priori ball, all forward differences are
Lipschitz in the strong-vector/trace norm.  The `A D_3` multiplier has the
Gaussian-envelope modulus `delta sqrt(log(e/delta))`.  The two remaining
gate--cotangent products use (6.7).  Consequently the complete state
difference obeys

\[
 \Delta(t)\le \Delta(0)+C_T\int_0^t
 \{\Delta(s)+\Delta(s)\log(e/\Delta(s))\}\,ds.          \tag{6.10}
\]

The resulting formal state difference has the required deterministic
Bihari--Osgood form.  To turn this reduction into a theorem, the following
statements must be established for the explicit family (6.1a)--(6.1b):

- **C1 (reconstruction).** Every reconstructed field difference satisfies
  the asserted `delta log(e/delta)` modulus on each localization event,
  including both true-adjoint gate products and trace-norm rank-one updates.
- **C2 (uniform Euler consistency).** The clipped exact and piecewise-linear
  Euler paths have a deterministic local consistency modulus, are uniformly
  close by Bihari, and the source Euler paths are Cauchy as the mesh vanishes.
- **C3 (tail inheritance and cutoff removal).** The finite comparison-family
  tail envelope passes to each source Euler limit, and the `R`-clipped source
  and finite paths converge to their uncut reachable limits uniformly as
  `R->infinity`.
- **C4 (operator/state passage).** The learned rank-one sums converge in the
  trace-norm/action topology needed by every reconstruction, and one fixed
  auxiliary mesh gives the exact square-tail transfer below.

The pointwise multiplier calculation proves the core inequality behind C1;
it does not by itself prove C2--C4.  Once C1--C4 hold, Bihari--Osgood gives
reachable-class uniqueness and exact-versus-Euler stability, and letting the
localization probability tend to one removes the event.

For one fixed sufficiently fine auxiliary mesh, the source theorem supplies
all polynomial tails.  After exact/mesh `L2` stability, square tails transfer
by

\[
 q^2\mathbf1_{|q|>R}
 \le4(q-v)^2+2v^2\mathbf1_{|v|>R/2}.                   \tag{6.11}
\]

This would identify the raw squared norms in (4.5); weak convergence or
bounded tests alone would not.  The readout, residual equation, and loss
would then give (6.9).  Accordingly, `(AG_T)` is the central mathematical
tail lemma, while C1--C4 are additional proof-completeness obligations for
the conditional assembly.  Neither `(AG_T)` nor that complete assembly is
claimed here.

### 6.4 What is unconditional about well-posedness

At each finite width, global compact-physical-time well-posedness is
unconditional.  At the source level, fixed-cutoff equations and every fixed
Euler program are well-defined on the admissible domain (4.2a).
Unconditional uniqueness of the raw,
uncut source IDE in a restart-stable class is not currently proved: a
nonconstant gate multiplying an arbitrary `L2` cotangent has no uniform
Osgood modulus on `L2` balls.  The first assertion of Conditional target 6.1
must not be quoted as a theorem; it also depends on C1--C4.

The obstruction is quantitative.  Let `q_n=sqrt(n)e_1` and let two
preactivations equal `s e_1` and `r e_1`, where `D(s) != D(r)`.  Their
normalized `L2` distance tends to zero, while

\[
 \|q_n\{D(se_1)-D(re_1)\}\|_n=|D(s)-D(r)|.             \tag{6.12}
\]

This disproves uniform continuity on energy balls.  It does not prove that
the canonical Gaussian trajectory reaches such a pair.

## 7. Unconditional width results

### 7.1 Initialization

Let `G` be standard normal and define

\[
\begin{aligned}
 q_1^{\rm fwd}&=\mathbb E\tanh(G)^2,\\
 q_2^{\rm fwd}&=\mathbb E\tanh(\sqrt{q_1^{\rm fwd}}G)^2,\\
 q_3^{\rm fwd}&=\mathbb E\tanh(\sqrt{q_2^{\rm fwd}}G)^2,
\end{aligned}                                                   \tag{7.1}
\]

and

\[
\begin{aligned}
 s_3&=\mathbb E\operatorname {sech}^4
          (\sqrt{q_2^{\rm fwd}}G),\\
 s_2&=s_3\mathbb E\operatorname {sech}^4
          (\sqrt{q_1^{\rm fwd}}G),\\
 s_1&=s_2\mathbb E\operatorname {sech}^4(G).
\end{aligned}                                                   \tag{7.2}
\]

The fixed Gaussian program law and Gaussian regression give

\[
 K_n(0)\xrightarrow{\mathbb P}
 K_0=q_3^{\rm fwd}+s_3q_2^{\rm fwd}
                 +s_2q_1^{\rm fwd}+s_1
 \simeq0.7357209343.                                    \tag{7.3}
\]

The two immutable queries at time zero are, coordinatewise,

\[
\begin{aligned}
 q_{2,j}(0)&=A_0^{\mathsf T}D_3\Gamma_{2,:,j},\\
 q_{1,j}(0)&=A_0^{\mathsf T}D_3\Gamma_2D_2\Gamma_{1,:,j}.
\end{aligned}                                                   \tag{7.4}
\]

Conditionally on `(u_0,Gamma_1,Gamma_2)`, these are jointly centered Gaussian
in `A_0`.  Their variances are bounded by

\[
 \|\Gamma_{2,:,j}\|_{\ell^2}^2,\qquad
 \|\Gamma_2\|_{\rm op}^2\|\Gamma_{1,:,j}\|_{\ell^2}^2. \tag{7.5}
\]

The Gaussian operator- and maximum-column-norm bounds imply, for one
deterministic sufficiently large `L`,

\[
 \frac1n\sum_j
 \left[e^{q_{2,j}(0)^2/L^2}+e^{q_{1,j}(0)^2/L^2}\right]
 =O_{\mathbb P}(1).                                    \tag{7.6}
\]

No independence across `j` is required: conditional expectation followed by
Markov's inequality proves the empirical statement.  In particular, both
queries are square uniformly integrable at initialization.

### 7.2 Every fixed Euler program

For Euler step size `h` and a fixed number `m` of steps, eliminate each
trained matrix:

\[
\begin{aligned}
 G_\ell^kv&=\Gamma_\ell v+
 \sum_{r<k}h\alpha_r B_{\ell+1}^r
                    \langle x_\ell^r,v\rangle_n,\\
 (G_\ell^k)^*w&=\Gamma_\ell^*w+
 \sum_{r<k}h\alpha_r x_\ell^r
                    \langle B_{\ell+1}^r,w\rangle_n.
\end{aligned}                                                   \tag{7.7}
\]

For fixed `m`, (7.7) is one finite joint program with actual transpose reuse.
Its complete joint empirical law and every fixed polynomial moment converge
to the corresponding program in (3.4).  This proves fixed-cutoff,
fixed-mesh identification.  It supplies no estimate uniform as `m` tends to
infinity.

### 7.3 A quantitative canonical no-focusing theorem at vanishing time

**Theorem 7.1.**  For every deterministic sequence `h_n \downarrow 0`, along
the exact physical flow,

\[
 \sup_{\substack{0\le t\le h_n\\ \ell=1,2\\1\le j\le n}}
 |q_{\ell,j}(t)|
 =O_{\mathbb P}\!\left(
    \sqrt{\log n}+\sqrt{nh_n\log(e/h_n)}\right).        \tag{7.8}
\]

Consequently,

\[
 \frac1{\sqrt n}
 \sup_{t\le h_n,\ell,j}|q_{\ell,j}(t)|
 \xrightarrow{\mathbb P}0.                             \tag{7.9}
\]

#### Proof

The sign of `e_n` is constant.  Define the nonnegative signed feature clock

\[
 s(t)=2\eta\int_0^t|e_n(r)|\,dr,
 \qquad \sigma=\operatorname {sgn}e_n(0).              \tag{7.10}
\]

Then `dTheta/ds=sigma \nabla f` and
`d(sigma f)/ds=K`.  The path length in the exact product parameter metric
satisfies

\[
\begin{aligned}
 d_n(s)&=\int_0^s\sqrt{K(r)}\,dr\\
 &\le\sqrt{s\int_0^sK(r)\,dr}
 \le\sqrt{s\{2\|A_0\|_n+s\}}.                         \tag{7.11}
\end{aligned}
\]

Here `|f(s)|<=||A(s)||_n<=||A_0||_n+s`.  Moreover
`s(t)<=2 eta |e_n(0)|t`.  Since `||A_0||_n` and `e_n(0)` are tight, the
maximum parameter displacement on `[0,h_n]` is
`O_P(sqrt(h_n))`.

The following deterministic entropy multiplier estimate is used twice.  If
`|w_i|<=1`, `r=||w||_n^2`, and

\[
 M_v=\frac1n\sum_i e^{v_i^2/L^2},
\]

then

\[
 \|vw\|_n^2\le L^2r\left(\log M_v+\log\frac1r\right). \tag{7.12}
\]

To prove it, use the probability weights
`p_i=w_i^2/(nr)` in the entropy variational inequality; their relative
entropy against the uniform measure is at most `log(1/r)`.

The forward fields move by `O_P(sqrt(h_n))` in normalized `L2`.  Apply
(7.12) first with `v=A_0` to

\[
 B_3(t)-B_3(0)
 =D_3(t)(A(t)-A_0)+(D_3(t)-D_3(0))A_0                 \tag{7.13}
\]

and next with `v=Q_2(0)=q_2(0)` to the corresponding decomposition of
`B_2(t)-B_2(0)`.  Equations (7.6) and (7.11) give, uniformly on the interval,

\[
 \|B_3(t)-B_3(0)\|_n+
 \|B_2(t)-B_2(0)\|_n
 =O_{\mathbb P}\!\left(
 \sqrt{h_n\log(e/h_n)}\right).                         \tag{7.14}
\]

Also (7.6) implies
`max_{ell,j}|q_{ell,j}(0)|=O_P(sqrt(log n))`.  Finally,

\[
 \max_j|\Gamma_{\ell,:,j}^{\mathsf T}v|
 \le \left(\max_j\|\Gamma_{\ell,:,j}\|_2\right)
       \sqrt n\|v\|_n,                                 \tag{7.15}
\]

and the maximum column norm is `O_P(1)`.  Combining (7.14)--(7.15) proves
(7.8); `h log(e/h)->0` proves (7.9).

This theorem excludes the macroscopic `sqrt(n)` single-column selector of
Section 9 at every time `t_n->0`.  It does not exclude smaller focusing, such
as a `log n` coordinate capable of spoiling a fixed exponential moment.  It
does not give a fixed-positive-time tail estimate, and its crude uniform
coordinate perturbation does not imply (6.2).

### 7.4 Initialization equicontinuity and the zero-label theorem

For `sigma in {-1,+1}`, let `K_n^sigma(s)` denote the exact signed feature
flow `d theta/ds=sigma grad f`, started at initialization.  A sharper
layerwise square-tail transfer yields, uniformly in the two signs,

\[
 \lim_{\rho\downarrow0}\limsup_n
 \mathbb P\!\left[
   \sup_{0\le s\le\rho}
   |K_n^\sigma(s)-K_n(0)|>\varepsilon\right]=0.          \tag{7.16}
\]

To complete the layer transfer, use (7.6) first for `A_0` in the `B_3`
difference, next for `Q_2(0)` in the `B_2` difference, and finally for
`Q_1(0)` in

\[
\begin{aligned}
 Q_1(\varsigma)-Q_1(0)
  &=(G_1(\varsigma)-\Gamma_1)^*B_2(\varsigma)
    +\Gamma_1^*(B_2(\varsigma)-B_2(0)),\\
 B_1(\varsigma)-B_1(0)
  &=D_1(\varsigma)(Q_1(\varsigma)-Q_1(0))
    +(D_1(\varsigma)-D_1(0))Q_1(0).
                                                               \tag{7.16c}
\end{aligned}
\]

The forward fields are strongly `L2`
continuous by the path-length bound; matrix actions have tight operator
norms.  Each of the four squared terms in (2.11) therefore converges
uniformly as `rho downarrow 0`, which proves (7.16).

For a fixed label, the clock bound on a high-probability initialization event
also gives the physical-time consequence

\[
 \lim_{\delta\downarrow0}\limsup_n
 \mathbb P\!\left[
   \sup_{0\le t\le\delta}|K_n(t)-K_n(0)|>\varepsilon\right]=0. \tag{7.16a}
\]

These statements rule out a vanishing-time order-one raw-kernel boundary
layer, including concentration on `o(n)` coordinates if it carries
nonvanishing squared energy.  They do not exclude sublinear concentration
whose total normalized squared energy vanishes.

If `y_*=0`, then `e_n(0)=-f_n(0)=O_P(n^{-1/2})`, and (2.12) gives

\[
 s_n(T)=2\eta\int_0^T|e_n(t)|dt
 \le2\eta T|e_n(0)|=O_{\mathbb P}(n^{-1/2}).            \tag{7.16b}
\]

Combining this random feature-clock bound with the deterministic small-clock
equicontinuity (7.16) gives the claim: first fix `rho` using (7.16), then use
`P[s_n(T)>rho]->0`, and finally send `rho downarrow 0`.  Hence

\[
 \sup_{t\le T}|K_n(t)-K_0|\xrightarrow{\mathbb P}0.     \tag{7.17}
\]

Moreover, on the same event,

\[
 \sup_{t\le T}|f_n(t)-f_n(0)|
 \le2\eta T|e_n(0)|\sup_{t\le T}K_n(t)=o_{\mathbb P}(1). \tag{7.18}
\]

Since `f_n(0)->0`, `e_n=-f_n` for the zero label, and
`\mathcal L_n=e_n^2`, this proves the corresponding uniform convergence of
predictor, residual, and loss to the stationary zero-label source solution.
This is a complete theorem, but it does not resolve the requested
arbitrary-label problem.

## 8. Two exact sufficient formulations of the open bridge

### 8.1 Gaussian creation--response formulation

Fix column `j` of one immutable matrix and write

\[
 g=\sqrt n\,\Gamma_{:,j}\sim N(0,I_n),\qquad
 q_j=\frac1{\sqrt n}g^{\mathsf T}b,                    \tag{8.1}
\]

where `b=B_3` or `B_2`.  Let `J_b=D_gb`,
`\widehat J_b=\sqrt n J_b`, and

\[
 \|M\|_{S_p,n}=\left(\frac1n\operatorname {Tr}|M|^p\right)^{1/p}.
                                                                  \tag{8.2}
\]

For (8.3)--(8.4), assume
`b in D^{1,p}(R^n;R^n)`, `b/sqrt(n)` lies in the domain of the Gaussian
divergence, and the displayed field and derivative norms are `L^p`
integrable.  These hypotheses hold first for smooth cylindrical comparison
programs; a Lipschitz clipped flow uses the closed weak Gaussian-Sobolev
derivative.

Gaussian divergence gives the exact identity

\[
 \boxed{
 q_j=\delta_g(b/\sqrt n)+\frac1n\operatorname {Tr}\widehat J_b.}
                                                                  \tag{8.3}
\]

The finite-dimensional Meyer inequality and Schatten duality imply, for
fixed `p>=2`,

\[
 \|q_j\|_{L^p}
 \le C_p\left(
   \|b\|_{L^p(H_n)}+
   \|\widehat J_b\|_{L^p(S_p,n)}\right).               \tag{8.4}
\]

The divergence part in fact carries an additional `n^{-1/2}` in front of
the normalized Schatten term; the normalized trace in (8.3) is the dominant
response scale.

For an exact or clipped continuous path, additionally require absolute
continuity in the corresponding Malliavin-Sobolev space.  Apply (8.4) to
`b(0)` and `dot b(t)` and integrate in time.  A precise sufficient condition
is: for some `p>2`, uniformly in `n,j` and the continuous comparison family,

\[
\begin{aligned}
 &\left\|\|b(0)\|_n+\|\widehat J_b(0)\|_{S_p,n}\right\|_{L^p}\\
 &\quad+\int_0^T
 \left\|\|\dot b(t)\|_n+
       \|\sqrt nD_g\dot b(t)\|_{S_p,n}\right\|_{L^p}dt
 \le M_{p,T}.                                          \tag{8.5}
\end{aligned}
\]

For an Euler path, fix its piecewise-linear interpolation, or replace the
integral in (8.5) by the sum of the Malliavin-Sobolev norms of its increments.
Uniformity over Euler comparisons refers to that discrete version.

Then `sup_t |q_j(t)|` has a uniform `p`th moment, and

\[
 \mathbb E\sup_{t\le T}\frac1n\sum_j
 q_j(t)^2\mathbf1_{|q_j(t)|>R}
 \le C_{p,T}R^{2-p}.                                   \tag{8.6}
\]

Thus (8.5), even for `p=4`, supplies square uniform integrability.  For
(6.2), it is sufficient that the final bound on
`||sup_{t<=T}|q_j(t)||_{L^p}` be at most `C_Tp` for every integer `p>=2`.
It is also enough to have this uniformly for
`2<=p<=c_T log n`, followed by the explicit Markov/union and truncated
layer-cake argument: the top moment first gives
`max_j sup_t|q_j(t)|=O_P(log n)`, and optimizing the lower moments gives an
exponential tail up to that maximum.  Without this quantitative truncation,
fixed-`p` moment control alone does not imply (6.2).

At initialization, for a marked `Gamma_2` column,

\[
 \widehat J_{B_3}(0)
 =-2x_{2,j}\operatorname {diag}(x_3B_3),               \tag{8.7}
\]

so the response has exactly the required normalized Schatten scale.

The obstruction appears in its evolution.  Differentiating (5.4) creates

\[
 \operatorname {diag}(H_3)\widehat J_{B_3}             \tag{8.8}
\]

and analogous terms at layer 2.  Existing energy bounds control `||H_3||_n`
only.  A Schatten-(4) Gronwall would require a dimension-free inequality

\[
 \|\operatorname {diag}(h)M\|_{S_4,n}
 \le C\|h\|_n\|M\|_{S_4,n},                            \tag{8.9}
\]

which is false.  Take `h=sqrt(n)e_1` and `M=e_1e_1^T`.  The two sides scale
as `n^{1/4}` and `n^{-1/4}`, respectively.  In the derivative of the
Schatten-(4) energy, Hölder replaces `S_4` by `S_8`; iteration generates an
unclosed hierarchy.

Therefore (8.5) is a proved sufficient lemma, while its derivation from the
known energy bounds is falsified as an abstract proof step.  A reachable
row-delocalization or a signed weighted cancellation could still prove it.

### 8.2 Correct one-column cavity criterion

Let `g_j` be independent of a sigma-field `F_j`, and let the cavity paths
`V_a^{(j)}(t)` be `F_j`-measurable.  Put

\[
 Z_j=\sup_{a,t\le T}
 \left|n^{-1/2}g_j^{\mathsf T}V_a^{(j)}(t)\right|.      \tag{8.10}
\]

For the actual paths, define

\[
 q_{a,j}(t)=n^{-1/2}g_j^{\mathsf T}V_a(t),\qquad
 Q_j(t)=\max_a\sup_{0\le s\le t}|q_{a,j}(s)|.          \tag{8.10a}
\]

Suppose, for fixed constants, that

\[
 \sup_n\frac1n\sum_j\mathbb E e^{Z_j/c_0}<\infty,     \tag{8.11}
\]

and on one global event of probability tending to one the actual queries
obey (8.12), simultaneously for every column, both layers, and every member
of the designated exact/clipped/Euler comparison family:

\[
 Q_j(t)\le Z_j+A_T+
 \int_{[0,t)}Q_j(s)\,\mu_{n,j}(ds),qquad
 \mu_{n,j}([0,T])\le M_T.                              \tag{8.12}
\]

The strict interval prevents an uncontrolled same-step Euler atom.  The
measure-valued Gronwall lemma gives

\[
 Q_j(T)\le e^{M_T}(Z_j+A_T),                            \tag{8.13}
\]

so (8.11) implies the empirical exponential bound (6.2).

For the precise Gaussian-width check, let

\[
 m_j=\mathbb E[Z_j\mid\mathcal F_j],\qquad
 \sigma_j=\sup_{a,t}\|V_a^{(j)}(t)\|_n.               \tag{8.13a}
\]

Conditional Gaussian concentration gives

\[
 \mathbb E[e^{Z_j/c_0}\mid\mathcal F_j]
 \le\exp\!\left(\frac{m_j}{c_0}
             +\frac{\sigma_j^2}{2c_0^2}\right).       \tag{8.13b}
\]

Thus a cavity-measurable exponential bound on the normalized Hilbert norms
and total variations must be strong enough to control the averaged
right-hand side of (8.13b).  A localization event depending on `g_j` may not
be used inside this conditional concentration step; conditioning on it
truncates and biases the Gaussian law.

The model-specific missing estimate is (8.12).  Ordinary normalized-`L2`
cavity stability is too weak because

\[
 |n^{-1/2}g_j^{\mathsf T}\Delta V|
 \le\|g_j\|_2\|\Delta V\|_n\asymp\sqrt n\|\Delta V\|_n. \tag{8.14}
\]

It would suffice to prove an actual `n^{-1/2}` cavity gain in `H_n`, or to
control the scalar pairing in (8.12) directly.  No such estimate is presently
proved for both layers and all comparison flows.

## 9. Ambient tail obstruction, but no reachable counterexample

The tail issue is not removable by an abstract norm argument.  Fix a column
`j` of `Gamma_2`, let `g_i=sqrt(n) Gamma_{2,ij}`, keep the canonical
`A=A_0,u=u_0,G_1=Gamma_1`, and let
`x_2=tanh(Gamma_1 tanh u_0)`.  Choose `a>0` and

\[
 z_i=\begin{cases}
 0,&A_{0,i}g_i\ge0,\\
 a,&A_{0,i}g_i<0.
 \end{cases}                                            \tag{9.1}
\]

Put `r=z-Gamma_2x_2` and

\[
 P_2=\frac{r\otimes x_2}{\|x_2\|_n^2}.                \tag{9.2}
\]

Then `(Gamma_2+P_2)x_2=z` exactly, and

\[
 \|P_2\|_{S_1}=\|P_2\|_F
 =\frac{\|r\|_n}{\|x_2\|_n}=O_{\mathbb P}(1).         \tag{9.3}
\]

Here `||x_2||_n^2 -> q_2^{fwd}>0`, so the denominator is bounded away from
zero in probability.  Moreover

\[
 \|Q_2\|_n\le
 (\|\Gamma_2\|_{\rm op}+\|P_2\|_{\rm op})\|B_3\|_n,
 \qquad
 \|Q_1\|_n\le\|\Gamma_1\|_{\rm op}\|B_2\|_n.         \tag{9.3a}
\]

Thus the claimed backward and raw-kernel energy bounds follow from the
displayed operator, trace, and normalized-vector bounds; they are not being
inferred from the exceptional coordinate itself.

All normalized forward, backward, and kernel energies remain bounded.  But,
with `delta=sech^2(a)`,

\[
 \frac1{\sqrt n}(\Gamma_2^*B_3)_j
 =\frac1n\sum_i g_iA_{0,i}
 \left(\mathbf1_{g_iA_{0,i}\ge0}
       +\delta\mathbf1_{g_iA_{0,i}<0}\right)
 \xrightarrow{\mathbb P}\frac{1-\delta}{\pi}>0.       \tag{9.4}
\]

Thus one immutable transpose coordinate is of order `sqrt(n)`, despite all
the available energy and trace bounds.  This is a static, adapted algebraic
state.  It is not known to lie on the canonical training trajectory.  In
particular, (7.9) proves that it cannot be reached at any `t_n->0`.  No
positive-time reachable selector or other counterexample has been
constructed.

## 10. Proof-route registry

| Route | Precise target | Status | Cheapest decisive obstruction or next step | Scope of failure |
|---|---|---|---|---|
| Exact source/operator closure | Equations (3.4), (4.3)--(4.5) | **proved algebraically** | none | positive partial result |
| Fixed finite Euler program | Joint law with both true adjoints | **proved** | number of steps must remain fixed | does not remove mesh |
| Direct `L2`/operator/trace energy | Derive square tails from compact energy balls | **falsified** | selector (9.1)--(9.4) | refutes this proof route only |
| Dynamic column cavity | Prove (8.12), or an `n^{-1/2}` influence gain | **conditional/open** | anisotropic scalar pairing loses `sqrt(n)` | would prove `(AG_T)` |
| Moderate moments / Malliavin | Prove (8.5), initially at `p=4` | **conditional/open** | diagonal `L2` multiplier breaks `S_4` Gronwall | route needs delocalized response or cancellation |
| Finite-rank Picard/Fock | Approximate nonlinear response by fixed-rank words | **falsified as stated** | (8.7) is an extensive diagonal/noncompact response | not a no-go for a larger GNS field |
| Full current response operator | Close a tracial `L^p` tangent IDE | **algebraically possible, analytically open** | weighted response hierarchy; no strong width limit | no hidden time, but broadens state class |
| Gradient balance / local entropy | Use (5.7)--(5.22) to propagate `L^{2+epsilon}` | **critical gain proved; superquadratic closure falsified** | exact cross-layer pairing raises the moment order | Gaussian-specific signed route remains possible |
| Weak compactness plus MSE energy | Identify raw gradient from dissipation | **circular alone** | chain rule and nonlinear adjoint graph already require square tails | may help after a strong reference is built |
| Local Orlicz restart | Propagate initialization tails by short intervals | **blocked** | arbitrary adaptive transpose can focus the same column at each restart | reachability estimate still needed |
| Growing-mesh tensor program | Let program length grow with width | **conditional/open** | requires robust query-rank/no-amplification and uniform Euler stability | fixed mesh remains valid |
| Canonical focusing counterexample | Reach (9.4) in fixed positive time | **open** | vanishing-time route excluded by (7.9), simple power selection remains sub-Gaussian | no impossibility theorem |
| Zero-label physical clock | Use `e_n(0)=O_P(n^{-1/2})` | **proved** | does not apply to nonzero fixed label | exact special case only |

The complete depth-three linear theorem succeeds by a finite-rank
noncommutative Picard/Fock mechanism.  The nonlinear response (8.7) is an
extensive multiplication operator, so the linear finite-rank argument does
not transfer.  This contrast is a route diagnosis, not an autonomous-closure
impossibility theorem.

## 11. Typed claim/evidence ledger

| ID | Type | Claim | Status | Evidence or exact dependency |
|---|---|---|---|---|
| E1 | theorem | finite equations (2.4)--(2.12) | **proved** | direct metric differentiation |
| E2 | theorem | compact finite-width bounds (2.13)--(2.14) | **proved** | MSE dissipation and rank-one trace norm |
| E3 | construction | joint three-sort immutable source with actual adjoints | **proved for fixed programs** | projective two-sided Gaussian program law plus spectral norm |
| E4 | construction | (4.4) is one-time, restartable, `O(1)`-species on the canonical/reachable domain (4.2b) | **proved algebraically** | every field recomputed from present state/source; no arbitrary-`L2` domain claim |
| E5 | theorem | cotangent identities (5.1)--(5.6) | **proved** | product rule and normalized adjoints |
| E5a | theorem | positive Gram factorization (5.7)--(5.9) | **proved** | exact substitution of gated cotangents |
| E5b | theorem | input-column balance and `D_1^{-1}` estimate (5.12)--(5.14) | **proved for exact flow** | characteristic identity and compact `L2` bounds |
| E5c | negative lemma | separable invariants or an absolute Cauchy--Schwarz local entropy using only arbitrary `L2` forcing close a superquadratic tail | **falsified as a route** | (5.17)--(5.22), higher-moment cross-layer term |
| E6 | theorem | initialization kernel (7.3) and square tails (7.6) | **proved** | Gaussian regression |
| E7 | theorem | every fixed Euler mesh converges | **proved** | formula (7.7) and fixed-program theorem |
| E8 | theorem | vanishing-time max-query bound (7.8) | **proved for exact flow** | path length plus entropy multiplier |
| E9 | theorem | vanishing-time raw-kernel equicontinuity (7.16) | **proved** | square-tail-first layerwise transfer |
| E10 | theorem | zero-label compact-time convergence | **proved** | residual clock is `o_P(1)` |
| E11 | bridge | `(AG_T)` plus C1--C4 implies well-posedness and (6.9) | **conditional blueprint; not assembled** | Osgood reconstruction is derived; uniform Euler/source/cutoff lemmas remain |
| E12 | bridge | response estimate (8.5) implies square UI | **proved conditionally** | Gaussian divergence and Meyer inequality |
| E13 | negative lemma | `L2` diagonal multiplication closes normalized `S_4` | **falsified** | one-row example after (8.9) |
| E14 | bridge | corrected cavity assumptions (8.11)--(8.12) imply `(AG_T)` | **proved conditionally** | measurable Gaussian concentration and measure Gronwall |
| E15 | mechanism | learned adjoint pieces are the unresolved unbounded-coordinate tail source along the canonical update | **falsified** | formula (6.0), bounded forward factors |
| E16 | mechanism | immutable adaptive transpose can focus on energy balls | **proved ambiently** | selector (9.1)--(9.4) |
| E17 | counterexample | canonical `sqrt(n)` ambient-selector focusing occurs at `t_n->0` | **falsified** | (7.9); (7.16) also rules out an order-one kernel boundary layer |
| E18 | counterexample | canonical flow focuses at some fixed positive time | **open** | neither construction nor exclusion is known |
| E19 | theorem target | `(AG_T)` for arbitrary nonzero label | **open** | minimal unresolved reachable-state lemma |
| E20 | final claim | unconditional arbitrary-label convergence (1.1) | **open** | depends on E19 or an equivalent new representation, plus completion of C1--C4 |

No conditional row has been promoted to a theorem without retaining its
hypothesis.

## 12. Hostile audit

### 12.1 Hidden temporal memory

The source (3.4) is fixed before training and is label-independent.  The
operators `P_1(t),P_2(t)` are present spatial operators.  Neither a two-time
covariance, a response path, a trajectory law, an expanding word list, nor a
time-indexed rank-one decomposition is used as state.  Restarting (4.4)
from a current canonical/reachable state in (4.2b) requires only (3.4) and
(4.2).  This is an algebraic restart claim; unconditional raw-source
existence and uniqueness are not inferred from it.

### 12.2 Adjoint fidelity

The same matrix letter appears in each forward and backward query, and (3.3)
passes to the source.  Replacing `Gamma_l^*` by a fresh Gaussian would erase
the regression/Onsager mean and produce a different model.  No such
replacement occurs here.

### 12.3 Tail escape

The raw kernel contains `||B_2||_2^2` and `||B_1||_2^2`.  Empirical weak
convergence, bounded tests, exchangeability, and normalized `L2` bounds do
not identify these squares.  Equation (9.4) is an explicit order-one square
defect hidden in one coordinate.  Hence a square-UI or equivalent
weak--strong bridge is logically necessary for the current proof
architecture.

### 12.4 Topology

The limiting state topology is strong `L2` for vector fields and trace norm
for learned operators.  Fixed source programs converge in every fixed
finite `W_p`.  Raw-kernel convergence additionally needs square-tail
control.  No cross-width convergence of the initialized random matrices to
the source operators in operator norm, and no inference from a weak operator
limit, is claimed; the scalar norm limit used in (3.2) is separate.

### 12.5 Interchange of width, cutoff, and mesh

The proved order is: fix cutoff and mesh, take `n->infinity`.  The desired
order also removes cutoff and mesh uniformly in `n`.  Condition `(AG_T)`,
together with the still-unproved comparison lemmas C1--C4, is designed to do
that through (6.10)--(6.11).  Without this full bridge, choosing a diagonal
mesh `h_n->0` is unsupported: fixed-program convergence has constants and
query spans that grow with the number of steps.

### 12.6 Label and architecture

All exact and conditional formulas include trained `u,G_1,G_2,A` and any
fixed `y_*`.  The only unconditional compact-time convergence theorem beyond
initialization is the special `y_*=0` theorem, which is explicitly not the
requested result.  No readout is frozen, and tanh is not replaced by arctan,
a linear model, a residual model, or a normalized architecture.

### 12.7 Literature scope

The finite-program source step is consistent with the two-sided master
theorem used in [Tensor Programs IIb](https://proceedings.mlr.press/v139/yang21f.html)
and the feature-learning framework of
[Tensor Programs IV](https://proceedings.mlr.press/v139/yang21c.html).
Recent general-depth `muP` work such as
[Chen et al. (2025)](https://proceedings.mlr.press/v267/chen25cd.html)
describes a discrete-iteration infinite-width process with explicit
history-dependent variables.  Those results do not supply the uniform-width
continuous-time mesh removal, raw-kernel square-tail bridge, or restartable
one-time state required by this contract.

## 13. Layer-by-layer general-depth form

For any fixed number `L` of hidden tanh activations, use sorts
`H_1,...,H_L`, immutable actions
`Gamma_k:H_k->H_{k+1}` for `1<=k<L`, and current trace-class perturbations
`P_k`.  Reconstruct

\[
 x_1=\tanh u,\qquad
 z_{k+1}=(\Gamma_k+P_k)x_k,qquad
 x_{k+1}=\tanh z_{k+1}.                                \tag{13.1}
\]

Set `B_L=D_LA` and recursively

\[
 Q_k=(\Gamma_k+P_k)^*B_{k+1},\qquad B_k=D_kQ_k.        \tag{13.2}
\]

The exact one-time equations are

\[
\begin{aligned}
 \dot{\tanh u}&=2\eta eD_1B_1,\\
 \dot A&=2\eta ex_L,\\
 \dot P_k&=2\eta eB_{k+1}\otimes x_k,
             \qquad 1\le k<L,\\
 \dot e&=-2\eta eK,
\end{aligned}                                                   \tag{13.3}
\]

with

\[
 K=\|x_L\|_2^2+\sum_{k=1}^{L-1}
      \|B_{k+1}\|_2^2\|x_k\|_2^2+\|B_1\|_2^2.        \tag{13.4}
\]

This algebraic/source formulation uses `O(L)` genuine layer information and
no temporal memory.  It is proved as an exact finite identity and is the
natural conjectural source IDE for every fixed depth.  The compact-time width
theorem is **not** proved beyond the accepted two-hidden-layer nonlinear
case: each additional hidden matrix introduces another adaptive immutable
transpose whose gated cotangent requires a reachable square-tail estimate.
For fixed `L`, constants may depend on `L`; no depth-uniform theorem is
claimed.

## 14. Final exact theorem statement and verdict

**Theorem 14.1 (unconditional part).**  For the frozen fully trained
three-hidden-layer tanh network with the normalization (2.1)--(2.3) and any
fixed label, the finite dynamics are (2.4)--(2.12), satisfy the compact-time
bounds (2.13)--(2.14), obey the Gram/cotangent identities (5.1)--(5.14), and
have the algebraically exact candidate source closure (3.4), (4.3)--(4.6).
Its vector field is defined on the admissible domain (4.2a), and its
canonical restart claim is restricted to (4.2b), not arbitrary `L2` input
coordinates.
Every clipped Euler program whose cutoff and number of steps are fixed before
`n->infinity` converges through the actual adjoints.  Initialization satisfies
(7.3) and (7.6); the exact flow satisfies the feature-/physical-time
equicontinuity (7.16)--(7.16a) and the macroscopic no-focusing estimate (7.8).
If `y_*=0`, the full compact-physical-time observable convergence theorem
holds.

**Conditional target 14.2 (not promoted to a theorem).**  If `(AG_T)`, or the
weaker Osgood tail hypothesis (6.3)--(6.5a), holds uniformly for the required
comparison family on every compact horizon, and C1--C4 are proved, then the
source IDE is uniquely well posed in (6.8) within the reachable
comparison-limit class satisfying that tail control, and the fully trained
arbitrary-label finite networks satisfy (6.9).

**Open lemma.**  Prove `(AG_T)` for the canonical iid-initialized exact,
clipped, and Euler trajectories, or prove any equivalent reachable
composite-gate estimate that yields (6.3)--(6.5a).  Equivalently, a successful
route may prove the response bound (8.5), the scalar cavity inequality
(8.12), or a different one-time source continuity theorem that does not hide
history.  For the present comparison architecture, C1--C4 must then also be
proved; they are not consequences already established from `(AG_T)`.

**Verdict.**  The requested nonzero-label depth-three extension has not been
completed.  There is no rigorous impossibility theorem for it either.  The
central identified tail obstruction in the current proof architecture is
positive-time adaptive reuse of the two immutable Gaussian transposes;
C1--C4 are additional unresolved comparison lemmas.  Failure of
the energy, finite-rank response, or ordinary cavity estimates proves only
the failure of those proof routes.
No long-time claim \(\mathcal L(t)\to0\) is made; it is logically separate from
the compact-time width limit and no uniform positive kernel lower bound has
been established for this nonlinear depth-three system.
