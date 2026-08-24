# Provisional asinh candidate: exact one-time operator contract

Status: exact C0--C1 candidate, not yet selected or promoted to a convergence
theorem, 22 August 2026.

The architecture, metrics, initialization, and training rule are exactly
those in `PROTOCOL.md`.  This file freezes the leading Phase-I witness so
that every remaining proof and audit attacks the same equations.

## 1. Activation and bottom natural coordinate

Choose the fixed activation

\[
 \phi(z)=\operatorname {arsinh}z,qquad
 d(z)=\phi'(z)=(1+z^2)^{-1/2}.                         \tag{1.1}
\]

Define

\[
 \Theta(u)=\frac12\{u\sqrt{1+u^2}+\operatorname {arsinh}u\},
 \qquad r=\Theta(u),                                  \tag{1.2}
\]

and let \(\iota=\Theta^{-1}\).  Then

\[
 \Theta'(u)=\sqrt{1+u^2}=d(u)^{-1}.                  \tag{1.3}
\]

Put

\[
 \Psi(r)=\operatorname {arsinh}\iota(r),\qquad
 c(r)=(1+\iota(r)^2)^{-1/2}.                          \tag{1.4}
\]

Both are globally Lipschitz and

\[
 \Psi'(r)=c(r)^2.                                     \tag{1.5}
\]

The transformed Gaussian seed is

\[
 r_0=\Theta(U_0),\qquad U_0\sim N(0,1),              \tag{1.6}
\]

and has every finite polynomial moment.  This is an exact invertible
coordinate change; the parameter metric and gradient rule are unchanged.

## 2. Exact finite causal fields

On the normalized spaces in `PROTOCOL.md`, set

\[
\begin{aligned}
 X_1&=\Psi(r),&Z_2&=G_1X_1,&X_2&=\operatorname {arsinh}Z_2,\\
 Z_3&=G_2X_2,&X_3&=\operatorname {arsinh}Z_3,&
 f_n&=\langle A,X_3\rangle_n,\\
 B_3&=A d(Z_3),&R_2&=G_2^*B_3,&B_2&=d(Z_2)R_2,\\
 Q_1&=G_1^*B_2.&&&&
\end{aligned}                                          \tag{2.1}
\]

With \((b\otimes x)v=b\langle x,v\rangle_n\), feature ascent is

\[
 \boxed{A'=X_3,\qquad r'=Q_1,\qquad
 G_1'=B_2\otimes X_1,\qquad G_2'=B_3\otimes X_2.}    \tag{2.2}
\]

The raw tangent kernel is exactly

\[
 \boxed{
 K_n=f_n'
 =\|X_3\|_2^2+\|B_3\|_2^2\|X_2\|_2^2
  +\|B_2\|_2^2\|X_1\|_2^2+\|c(r)Q_1\|_2^2.}       \tag{2.3}
\]

These identities are included in `test_finite_identities.py`.

## 3. Immutable source and current state

Use three probability Hilbert spaces \(H_j=L^2(\Omega_j)\), the endpoint
marks

\[
 a_0\in H_3,\qquad r_0\in H_1,
\]

and two independent jointly realized pointed Gaussian actions

\[
 \Gamma_1:H_1\to H_2,\qquad \Gamma_2:H_2\to H_3,     \tag{3.1}
\]

with their genuine Hilbert adjoints.  The source is the deterministic
projective master law of every fixed finite three-sorted program in these
marks, actions, adjoints, coordinate maps, and normalized moments.  The
Gaussian spectral-norm theorem extends the dense program actions to bounded
operators with \(\|\Gamma_j\|\le2\).

The current state is the fixed five-species tuple

\[
 (A,r,P_1,P_2,e)\in H_3\times H_1\times
 \mathfrak S_1(H_1,H_2)\times\mathfrak S_1(H_2,H_3)\times\mathbb R.
                                                               \tag{3.2}
\]

Set \(G_j=\Gamma_j+P_j\) and reconstruct (2.1) from the present state.

## 4. Exact autonomous physical IDE

The proposed physical system is

\[
 \boxed{
 \begin{aligned}
  \dot A&=2\eta eX_3,&\dot r&=2\eta eQ_1,\\
  \dot P_1&=2\eta eB_2\otimes X_1,&
  \dot P_2&=2\eta eB_3\otimes X_2,\\
  \dot e&=-2\eta eK,
 \end{aligned}}                                       \tag{4.1}
\]

initialized by

\[
 A(0)=a_0,\quad r(0)=r_0,\quad P_1(0)=P_2(0)=0,
 \quad e(0)=y_\star.                                  \tag{4.2}
\]

The current observations are

\[
 f=\langle A,X_3\rangle,qquad K\text{ from (2.3)},
 \qquad \mathcal L=e^2.                               \tag{4.3}
\]

Along any sufficiently regular solution,

\[
 f+e=y_\star,qquad \dot{\mathcal L}=-4\eta K\mathcal L. \tag{4.4}
\]

The tuple (3.2), with the fixed source (3.1), determines its own future.
The current operators are used extensionally; their rank-one creation times
are not retained.  There is no second training time, response kernel,
stored trajectory, delay, or growing list of state variables.

## 5. Exact critical phase/cotangent lift

For any preactivation \(z\), define

\[
 d_z=(1+z^2)^{-1/2},\qquad s_z=zd_z,qquad d_z^2+s_z^2=1. \tag{5.1}
\]

For the carriers

\[
 C_3=A,\qquad C_2=R_2,\qquad C_1=Q_1,                \tag{5.2}
\]

put

\[
 p_j=d_{Z_j}C_j,qquad q_j=s_{Z_j}C_j,qquad Z_1=\iota(r). \tag{5.3}
\]

Thus \(p_3=B_3,p_2=B_2,p_1=c(r)Q_1\), exactly the three
backward fields used by (2.2)--(2.3).  If \(V_j=Z_j'\), then

\[
 p_j'=-d_{Z_j}^2q_jV_j+d_{Z_j}C_j',\qquad
 q_j'=d_{Z_j}^2p_jV_j+s_{Z_j}C_j'.                   \tag{5.4}
\]

Consequently

\[
 p_j^2+q_j^2=C_j^2,qquad
 p_jp_j'+q_jq_j'=C_jC_j'.                            \tag{5.5}
\]

This lift is current-time and finite-species if adjoined, but it is not
being used to hide a missing estimate: (5.5) controls a single trajectory's
local rotation, not the separation of two trajectories with different
angles.

## 6. Exact tail advantages and unresolved bridge

The pointwise inequality

\[
 e^{\alpha|\operatorname {arsinh}z|}
 \le C_\alpha(1+z^2),\qquad 0<\alpha\le2,             \tag{6.1}
\]

turns every empirical \(L^2\) preactivation bound into an exponential
moment bound for its forward field.  The log derivative

\[
 \frac{d'(z)}{d(z)}=-\frac{z}{1+z^2}=-s_zd_z          \tag{6.2}
\]

is bounded.  These two identities and the skew cancellation (5.4) are why
asinh is the leading depth-three candidate.

They do not yet prove the required adaptive-adjoint estimate.  The precise
remaining statement is: for every compact physical horizon \(T\), there
exist \(c_T,C_T>0\) such that

\[
 \mathbb P\!\left\{
  \sup_{2\le p\le c_T\log n}\frac1p\sup_{t\le T}
  \bigl(\|R_{2,n}(t)\|_{p,n}+\|Q_{1,n}(t)\|_{p,n}\bigr)
  \le C_T
 \right\}\longrightarrow1.                          \tag{6.3}
\]

Estimate (6.3) yields the Osgood modulus

\[
 \omega(\delta)=C\delta\log(e/\delta),qquad
 \int_{0^+}\frac{d\delta}{\omega(\delta)}=\infty,   \tag{6.4}
\]

and would close uniqueness, mesh/cutoff removal, square-tail compactness,
and every raw term in (2.3).  Fixed-mesh moments and fixed
\(L^{2+\epsilon}\) bounds do not prove (6.3).  Until (6.3), or an
equivalent cancellation theorem, is proved, this file is an exact candidate
contract rather than a C2--C6 theorem.
