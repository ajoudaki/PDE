# Frozen contract: depth-three tanh operator IDE

Status: activation and algebra frozen; continuous-width identification is a
proof target, not yet a theorem.

## Canonical finite system

Use `H_n=(R^n,<.,.>_n)` with

\[
 \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w,
 \qquad (v\otimes w)h=v\langle w,h\rangle_n.
\]

The independent initialization is

\[
 u_{0,i},A_{0,i}\sim N(0,1),\qquad
 (G_{\ell,0})_{ij}\sim N(0,1/n),\quad \ell=1,2.
\]

Set `phi=tanh`, and write

\[
\begin{aligned}
 X_1&=\tanh u,& Z_2&=G_1X_1,&X_2&=\tanh Z_2,\\
 Z_3&=G_2X_2,&X_3&=\tanh Z_3,&f_n&=\langle A,X_3\rangle_n.
\end{aligned}
\]

Let `d(z)=sech^2(z)`.  The current cotangents are

\[
 B_3=A d(Z_3),\quad Q_2=G_2^*B_3,\quad B_2=d(Z_2)Q_2,
 \quad Q_1=G_1^*B_2,\quad B_1=d(u)Q_1.
\]

In feature time,

\[
 A'=X_3,\qquad u'=B_1,\qquad
 G_2'=B_3\otimes X_2,\qquad G_1'=B_2\otimes X_1.
\tag{1}
\]

For MSE residual `e=y-f_n`, physical time multiplies every right-hand side
in (1) by `2 eta e`.

## Activated-coordinate Markov state

Put `Y=X_1=tanh(u)`, `G_l=Gamma_l+P_l`, and
`D_1=1-Y^2`.  Recompute at the current time

\[
 Z_2=G_1Y,\quad X_2=\tanh Z_2,\quad D_2=1-X_2^2,
\]

\[
 Z_3=G_2X_2,\quad X_3=\tanh Z_3,\quad D_3=1-X_3^2,
\]

\[
 B_3=D_3A,\quad Q_2=G_2^*B_3,\quad B_2=D_2Q_2,
 \quad Q_1=G_1^*B_2,\quad B_1=D_1Q_1.
\]

The frozen candidate IDE is

\[
\boxed{
\begin{aligned}
 \dot Y&=2\eta e\,D_1B_1,\\
 \dot A&=2\eta e\,X_3,\\
 \dot P_1&=2\eta e\,B_2\otimes Y,\\
 \dot P_2&=2\eta e\,B_3\otimes X_2,
\end{aligned}}
\tag{2}
\]

with `P_1(0)=P_2(0)=0` and immutable Gaussian-program actions
`Gamma_1,Gamma_2` together with their genuine Hilbert adjoints.  Equation
(2) is autonomous and restartable from

\[
 (\Gamma_1,\Gamma_2;Y,A,P_1,P_2).
\]

It has one training-time coordinate and a constant number of vector/operator
species.  No covariance indexed by two training times, stored response path,
or time-labelled rank-one list is part of the state.

## Direct observables and exact energy identities

The raw tangent kernel is

\[
\boxed{
 K=\|X_3\|_n^2
  +\|B_3\|_n^2\|X_2\|_n^2
  +\|B_2\|_n^2\|Y\|_n^2
  +\|B_1\|_n^2.}
\tag{3}
\]

Direct differentiation gives

\[
 \dot f=2\eta eK,\qquad
 \dot e=-2\eta eK,\qquad
 \frac d{dt}e^2=-4\eta e^2K.
\tag{4}
\]

The parameter-speed identity and Cauchy--Schwarz imply compact-time
dimension-free normalized-vector displacement bounds and

\[
 \sup_{t\le T}\|P_\ell(t)\|_{S_1}=O_{\mathbb P,T}(1).
\tag{5}
\]

Hence `G_l` are bounded in operator norm and every displayed field is bounded
in normalized `L2`, uniformly on compact physical time with high probability.

At canonical initialization, let `G` be standard normal and set

\[
 q_1=\mathbb E\tanh(G)^2,\quad
 q_2=\mathbb E\tanh(\sqrt{q_1}G)^2,\quad
 q_3=\mathbb E\tanh(\sqrt{q_2}G)^2,
\]

\[
 s_3=\mathbb E d(\sqrt{q_2}G)^2,\quad
 s_2=s_3\mathbb E d(\sqrt{q_1}G)^2,\quad
 s_1=s_2\mathbb E d(G)^2.
\]

Exact Gaussian regression then gives

\[
 K_n(0)\longrightarrow K_0=q_3+s_3q_2+s_2q_1+s_1
 \simeq0.7357209343.
\tag{5a}
\]

It also gives square-uniform integrability of both immutable-adjoint fields
at time zero.  A layerwise truncation proof consequently yields

\[
 \lim_{\delta\downarrow0}\limsup_n
 \Pr\!\left[\sup_{t\le\delta}|K_n(t)-K_n(0)|>\epsilon\right]=0.
\tag{5b}
\]

Thus the open compact-time obligation below cannot fail through an
initialization-scale or any other vanishing-time concentration layer.

## Why tanh was selected

All `X_l` are coordinatewise bounded by one.  Consequently

\[
 A(t)=A_0+\int_0^t2\eta e(s)X_3(s)\,ds
\]

is an empirical sub-Gaussian field plus a bounded shift, and `B_3=D_3A`
has the same tail quality.  Moreover

\[
 P_2(t)^*B_3(t)
 =\int_0^t2\eta e(s)X_2(s)
   \langle B_3(s),B_3(t)\rangle_n\,ds,
\tag{6}
\]

and analogously for `P_1^*B_2`.  Since the forward factor is bounded and the
scalar contractions have compact-time bounds, every learned-adjoint term is
coordinatewise bounded.  Thus the only possible tail defect is in

\[
 \Gamma_2^*B_3,\qquad \Gamma_1^*B_2.
\tag{7}
\]

Leaky arctangent preserves arbitrary `L2` spikes through its linear tail.
Asinh deterministically improves them only to `psi_1`.  Tanh gives bounded
forward fields and bounded learned-adjoint pieces.  Faster Gaussian gates do
not improve the required supremum-in-time raw-kernel control and have an
unbounded logarithmic gate derivative.

## Frozen proof obligation

For every `T<infinity`, prove that there is a deterministic `C_T<infinity`
such that, in probability, along the exact trajectory and uniformly along
the clipped/Euler comparison trajectories used in mesh removal,

\[
 \sup_{t\le T}\frac1n\sum_{j=1}^n
 \left[
 e^{| (\Gamma_2^*B_3(t))_j|/C_T}
 +e^{| (\Gamma_1^*B_2(t))_j|/C_T}
 \right]=O_{\mathbb P,T}(1).
\tag{AG_T}
\]

The bound must use reachability from the canonical iid initialization.  It
does not follow from operator norm, exchangeability, bounded forward fields,
or `L2` energy alone.

Conditional on `(AG_T)`, tail truncation gives the Osgood modulus

\[
 \omega(r)=C_T r\{1+\log_+(1/r)\},\qquad
 \int_{0^+}\frac{dr}{\omega(r)}=\infty.
\tag{8}
\]

This yields current-state uniqueness, exact-versus-Euler stability, cutoff
removal, raw-kernel continuity, and uniform compact-time finite-width
convergence.  Proving `(AG_T)` or an equivalent reachable composite-gate
estimate is the sole remaining unconditional step.

## Closed zero-label corollary

For the special target `y=0`, canonical initialization has
`f_n(0)=O_P(n^{-1/2})`, so the physical residual clock travels only
`O_P(n^{-1/2})` on every fixed physical horizon.  Combining this with
(5b) gives

\[
 \sup_{t\le T}|K_n(t)-K_0|\longrightarrow0
 \quad\hbox{in probability}.
\]

Thus the full compact-physical-time statement closes for the zero target.
This does not address the intended fixed nonzero label: there the feature
clock moves an order-one distance, and `(AG_T)` remains necessary.
