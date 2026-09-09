# Gradient-Geometry Machinery Audit

## Verdict

The one-sample gradient geometry supplies exact identities at every fixed
depth, a useful intrinsic mobility metric, compact-time size bounds, and a
quantitative low-rank approximation of each *learned matrix increment*.  It
does **not** produce an admissible autonomous closure at depth three.

The decisive obstruction is compression rather than blow-up.  The internal
pullback cometric already has a non-scalar generalized-Wishart bulk at
initialization, and coordinatewise activation motion changes that bulk in
full rank.  Retaining the cometric is a forbidden full-matrix state; retaining
only finitely many of its actions generates a Krylov/response hierarchy; and
postulating that omitted actions are small on future causal directions is the
unproved reachable-tangent theorem.

Accordingly:

- the identities and bounds below are **proved**;
- gradient geometry as an easier completion machinery is **killed**;
- the existence of a different admissible arbitrary-depth closure remains
  **open**.

Throughout this note the trainable matrices are denoted by \(G_\ell(t)\), and
\(\Gamma_\ell=G_\ell(0)\) denotes the immutable Gaussian initialization.

## 1. Exact pullback cometric and kernel collapse

Put

\[
D_\ell=\operatorname{diag}\phi'(z_\ell),\qquad
\alpha_\ell=\|x_\ell\|_n^2.
\]

On parameter space use normalized Euclidean metrics for vectors and the
ordinary Frobenius metric for matrices.  The finite flow in the program
contract is exactly gradient ascent for the predictor, so

\[
\dot p=\|\nabla_g p\|_g^2=\Theta_n.
\tag{1}
\]

Define the upstream pullback cometrics recursively by

\[
P_1=I,
\qquad
P_{\ell+1}
=\alpha_\ell I+G_\ell D_\ell P_\ell D_\ell G_\ell^T.
\tag{2}
\]

Then at every finite width and depth,

\[
\boxed{\dot z_\ell=P_\ell b_\ell},
\qquad
\boxed{\Theta_n=\alpha_D+\langle b_D,P_D b_D\rangle_n}.
\tag{3}
\]

Indeed, if (3) holds at layer \(\ell\), then

\[
\begin{aligned}
\dot z_{\ell+1}
&=\dot G_\ell x_\ell+G_\ell D_\ell\dot z_\ell\\
&=\alpha_\ell b_{\ell+1}
 +G_\ell D_\ell P_\ell D_\ell G_\ell^Tb_{\ell+1}.
\end{aligned}
\]

Thus \(P_\ell=J_\ell J_\ell^*\) is precisely the pullback Gram operator of
the preactivation \(z_\ell\) with respect to all upstream parameters.

For arctangent, \(|\phi|\le a=\pi/2\) and \(\|D_\ell\|_{\rm op}\le1\), so

\[
\|P_{\ell+1}\|_{\rm op}
\le a^2+\|G_\ell\|_{\rm op}^2\|P_\ell\|_{\rm op}.
\tag{4}
\]

Moreover,

\[
\|A(t)\|_n\le\|A(0)\|_n+at,
\qquad
\frac d{dt}\|G_\ell\|_{\rm op}
\le a\|A\|_n\prod_{j>\ell}\|G_j\|_{\rm op}.
\tag{5}
\]

The triangular system (5), starting at the top layer, gives
width-independent compact-time bounds on the high-probability initialization
event where the source operator norms are bounded.  It controls all
\(\|G_\ell\|_{\rm op}\), \(\|b_\ell\|_n\), \(P_\ell\), and \(\Theta_n\).
This is compact containment, not stability of two nearby trajectories.

## 2. Flux identities and the exact nonlinear bottom invariant

Let

\[
S(z)=\frac{\phi(z)}{\phi'(z)},
\qquad h(z)=z\phi'(z)-\phi(z).
\]

Every edge obeys the exact flux identity

\[
\langle b_{\ell+1},z_{\ell+1}\rangle_n
=\langle r_\ell,x_\ell\rangle_n
=\langle b_\ell,S(z_\ell)\rangle_n.
\tag{6}
\]

At an internal layer,

\[
\frac d{dt}
\left(G_{\ell-1}G_{\ell-1}^T-G_\ell^TG_\ell\right)
=\frac1n\left[
b_\ell z_\ell^T+z_\ell b_\ell^T
-x_\ell r_\ell^T-r_\ell x_\ell^T
\right].
\tag{7}
\]

Taking traces shows that the deep-linear balancedness defect is

\[
\frac d{dt}(E_{\ell-1}-E_\ell)
=2\langle h(z_\ell),r_\ell\rangle_n.
\tag{8}
\]

For arctangent, \(h'(z)=-2z^2/(1+z^2)^2\), so this does not vanish.
Ordinary layer balancing therefore does not survive the nonlinearity.

There is an exact bottom invariant.  Define \(\Psi(0)=0\) and

\[
\Psi'(z)=2\frac{\phi(z)}{\phi'(z)}.
\tag{9}
\]

For \(\phi=\arctan\),

\[
\Psi(z)=2\left(z+\frac{z^3}{3}\right)\arctan z
-\frac{z^2}{3}-\frac23\log(1+z^2).
\tag{10}
\]

Then

\[
\boxed{
\|G_1(t)\|_F^2-\langle\Psi(u(t)),1\rangle_n
=\text{constant}.}
\tag{11}
\]

In fact the identity holds columnwise:

\[
\boxed{
(G_1^TG_1)_{jj}-\frac1n\Psi(u_j)=\text{constant}.}
\tag{12}
\]

This follows from

\[
\frac d{dt}(G_1^TG_1)_{jj}
=\frac2n\phi(u_j)r_{1j},
\qquad
\dot u_j=\phi'(u_j)r_{1j}.
\]

Here \(\Psi''(z)=2(1+2z\arctan z)\ge2\) and
\(\Psi(z)\asymp |z|^3\), so (12) supplies real bottom-layer moment control.
It does not control the internal pullback operators below.

## 3. Mobility and the intrinsic cap connection

For arctangent set

\[
R(z)=z+\frac{z^3}{3},qquad
R'(z)=\frac1{\phi'(z)},qquad
\kappa(z)=\frac{\phi''(z)}{\phi'(z)},\quad |\kappa|\le1.
\]

In mobility coordinates \(y_\ell=R(z_\ell)\), (3) becomes

\[
\dot y_\ell=C_\ell r_\ell,
\qquad
C_\ell=D_\ell^{-1}P_\ell D_\ell.
\tag{13}
\]

Although \(C_\ell\) can have a large Euclidean norm, it is self-adjoint and
positive in

\[
\langle v,w\rangle_{D_\ell^2}
=\langle D_\ell v,D_\ell w\rangle_n,
\]

and its intrinsic operator norm is exactly \(\|P_\ell\|_{\rm op}\).

Let

\[
L_\ell=D_\ell^{-1}\dot D_\ell
=\operatorname{diag}(\kappa(z_\ell)\dot z_\ell).
\]

The induced covariant derivative on vectors is
\(\nabla_t v=\dot v+L_\ell v\), and on endomorphisms it is

\[
\nabla_t C=\dot C+L_\ell C-CL_\ell.
\]

Consequently,

\[
\boxed{
\nabla_tC_\ell=D_\ell^{-1}\dot P_\ell D_\ell.}
\tag{14}
\]

Thus the apparent ratios of small activation derivatives and their
commutator are coordinate artifacts *along one trajectory*.  A
two-trajectory comparison has different connections, and the resulting
defect products again require forced reachable-tangent control.

At depth one, this chart is a genuine complete reduction:

\[
\dot y=A,qquad \dot A=f(y),qquad
f(y)=\phi(R^{-1}y),qquad 0\le f'(y)=\phi'(u)^2\le1.
\tag{15}
\]

It gives a globally Lipschitz coordinate flow, the invariant
\(A_i^2-\Psi(u_i)\), and a closed restartable Liouville equation for the
empirical law.  At depth two, even freezing a generic non-diagonal \(P_2\)
destroys this quadrature.  An invariant \(\|A\|^2-U(z_2)\) would require

\[
\nabla U(z)=2P_2^{-1}S(z).
\]

For \(i\ne j\), curl-freeness demands

\[
(P_2^{-1})_{ij}\bigl(S'(z_j)-S'(z_i)\bigr)=0,
\tag{16}
\]

which fails generically because \(S'\) is nonconstant.

## 4. Trace-class learned motion

Each matrix increment has the exact representation

\[
\Delta G_\ell(t)
=\int_0^t\frac1n b_{\ell+1}(s)x_\ell(s)^T\,ds.
\tag{17}
\]

Therefore

\[
\|\Delta G_\ell(t)\|_*
\le V_\ell(t)
:=\int_0^t\|b_{\ell+1}(s)\|_n\|x_\ell(s)\|_n\,ds.
\tag{18}
\]

If \(\sigma_k\) are its singular values, then

\[
\boxed{
\inf_{\operatorname{rank}Q\le m}
\|\Delta G_\ell-Q\|_F
\le\frac{V_\ell(t)}{\sqrt{m+1}}.}
\tag{19}
\]

Indeed \(\sum_k\sigma_k\le V\),
\(\sigma_{m+1}\le V/(m+1)\), and
\(\sum_{k>m}\sigma_k^2\le\sigma_{m+1}\sum_{k>m}\sigma_k\).

This is a useful, effective compactness theorem for the *learned update*.
Eliminating that update exactly, however, gives

\[
z_{\ell+1}(t)=\Gamma_\ell x_\ell(t)
+\int_0^t b_{\ell+1}(s)
 \langle x_\ell(s),x_\ell(t)\rangle_n\,ds,
\tag{20}
\]

\[
r_\ell(t)=\Gamma_\ell^Tb_{\ell+1}(t)
+\int_0^t x_\ell(s)
 \langle b_{\ell+1}(s),b_{\ell+1}(t)\rangle_n\,ds.
\tag{21}
\]

Equations (20)--(21) expose the forbidden two-time kernels.  Low-rank
approximability of \(\Delta G_\ell\) therefore does not itself give a
one-time autonomous state.

## 5. Fatal depth-three compression obstruction

At depth three,

\[
P_3=\alpha_2I+G_2D_2P_2D_2G_2^T.
\tag{22}
\]

The inner operator \(P_2\) is already irreducibly non-scalar at time zero:

\[
P_2=\alpha_1I+W,\qquad
W=\Gamma_1D_1^2\Gamma_1^T
=\frac1nX\operatorname{diag}(q_j)X^T,\quad
q_j=\phi'(u_j)^2.
\tag{23}
\]

Writing \(\tau=n^{-1}\operatorname{Tr}\), Wick contraction gives

\[
\tau(W)\longrightarrow m_1=\mathbb E q,
\qquad
\tau(W^2)\longrightarrow m_1^2+m_2,\quad
m_2=\mathbb E q^2>0.
\tag{24}
\]

Hence

\[
\inf_c\tau((W-cI)^2)\longrightarrow m_2>0.
\tag{25}
\]

Thus \(P_2\) is not a scalar plus a fixed-rank correction.  It has a genuine
spectral bulk before training.  Activation motion also generates the term

\[
\frac d{dt}(G_1D_1^2G_1^T)
\supset
G_1\operatorname{diag}
\bigl(2\phi'(z_1)\phi''(z_1)\dot z_1\bigr)G_1^T,
\tag{26}
\]

which is generically full rank.  Rank-one updates of \(G_1\) therefore do not
make the internal cometric evolution low rank.

If an approximation omits \(\delta P_2\), the next layer sees

\[
G_2D_2\,\delta P_2\,D_2G_2^Tb_3.
\tag{27}
\]

There are three evident representations:

1. retain \(P_2\), which violates the no-full-matrix state contract;
2. retain finitely many actions \(P_2v_j\), whose differentiation generates
   new source directions and hence an unclosed Krylov/response hierarchy;
3. assert that the omitted operator is small on every newly reachable
   direction, which is precisely the unresolved reachable-tangent theorem.

This is the machinery's fatal gate.  It does not prove that no clever
compression can exist, but it proves that pullback geometry and low-rank
learned motion do not supply one.

## 6. Time changes do not remove the obstruction

Let \(g=\nabla_gp\), \(K=\|g\|_g^2\), and \(H=Dg\).  Predictor time gives

\[
D\left(\frac gK\right)
=\frac{(I-2\Pi_g)H}{K},
\tag{28}
\]

while arc-length time gives

\[
D\left(\frac g{\sqrt K}\right)
=\frac{(I-\Pi_g)H}{\sqrt K}.
\tag{29}
\]

The first prefactor is a reflection and the second removes only the
longitudinal component.  Neither changes the trajectory image, source-action
memory, or rank obstruction.  Kernel time is just \(p-p(0)\).

Nor is the raw kernel monotone.  In the scalar depth-one model,

\[
K=\phi(u)^2+\phi'(u)^2A^2,
\qquad
\dot K=2\phi'(u)^2A
\bigl(2\phi(u)+\phi''(u)A^2\bigr),
\tag{30}
\]

which is negative, for example, at \(u=1,A=2\) for arctangent.  The clocks
therefore add no uniform restart certificate near critical behavior.

## 7. Exact remaining leaf

A gradient-geometric completion would still need an autonomous one-time
compressed state that reconstructs every required action \(P_\ell b_\ell\)
with residual \(\varepsilon_m\to0\), and a derived Osgood estimate

\[
D^+d(S,\widetilde S)
\le\omega_T(d(S,\widetilde S))+\varepsilon_m,
\qquad
\int_{0^+}\frac{dr}{\omega_T(r)}=\infty.
\tag{31}
\]

At depth three, constructing that state is not a small lemma: it is the
source-action/forced-tangent completion problem.  Replacing it by all vector
spectral measures or mixed source moments is merely a full response closure.

The resulting claim-level verdict is therefore:

| Claim | Status |
|---|---|
| Pullback recursion, kernel collapse, flux, and balance-defect identities | Proved |
| Arctangent bottom invariant | Proved |
| Depth-one mobility/Liouville closure | Proved |
| Intrinsic cap symmetrization | Proved algebraically |
| Trace-class learned increments and effective rank tail | Proved |
| Generic depth-two quadrature integrability | Falsified by curl obstruction |
| Permitted depth-three closure from this geometry | Killed by the full-bulk cometric obstruction |
| A wholly different arbitrary-depth closure | Open |
