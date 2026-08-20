# A directly simulable neural PDE for the dense Euclidean \(\mu\)P ResNet

## 1. Status

This note defines the equation that is actually simulated in this bundle.
It is a new, explicit operator-Galerkin candidate for the ordered
width-then-depth limit. It is not a relabeling of the finite-matrix \(q/r\)
surrogate, and it is not the un-emitted \(K/J/N\) response-word compiler in
the earlier conjecture note.

For every finite Galerkin order \(P\), the equation below is a genuine,
autonomous, width-independent conditional Liouville PDE. Its remaining
conjectural step is identification with the canonical fully dense network as
\(n\to\infty\), then \(L\to\infty\), and finally \(P\to\infty\).

## 2. Canonical dense model

For fixed training samples \(u_1,\ldots,u_m\in\mathbb R^d\), let
\(\Delta=L^{-1}\) and

\[
h_r^0=Bu_r,\qquad
z_r^\ell=W_\ell h_r^\ell,\qquad
h_r^{\ell+1}
=h_r^\ell+\gamma\Delta\sigma(z_r^\ell),
\]

\[
f_r=\frac1n a^\top h_r^L,\qquad
\mathcal L=\frac12\sum_r(f_r-y_r)^2.
\]

All matrices are dense and unconstrained. The initialization and standard
Euclidean \(\mu\)P multipliers are

\[
(W_\ell)_{ij}\sim N(0,\sigma_w^2/n),\qquad
B_{ij}\sim N(0,1),\qquad
a_i\sim N(0,A^2),
\]

\[
\eta_{W_\ell}=L,\qquad \eta_B=\eta_a=n.
\]

Writing \(e=f-y\), \(p_r^L=a\),
\(D_r^\ell=\operatorname{diag}\sigma'(z_r^\ell)\), and
\(\beta_r^\ell=D_r^\ell p_r^{\ell+1}\), the exact parameter flow is

\[
\dot W_\ell=-\frac{\gamma}{n}\sum_qe_q\beta_q^\ell(h_q^\ell)^\top,
\qquad
\dot a=-\sum_qe_qh_q^L,
\qquad
\dot B=-\sum_qe_qp_q^0u_q^\top.
\]

The target order is

\[
n\to\infty\quad\text{at fixed }L,
\qquad L\to\infty\quad\text{second}.
\]

The present transfer experiment keeps the derivation fixed and tests three
smooth, bounded, odd activations with \(\sigma'(0)=1\): tanh,
\(\operatorname{erf}(\sqrt{\pi}z/2)\), and
\((2/\pi)\arctan(\pi z/2)\). The original narrow conjecture is for tanh;
the other two are explicit extension tests.

## 3. Isonormal row projection after the width limit

Let

\[
\theta=(B_i(0),a_i(0)/A)\sim\mu=N(0,I_{d+1})
\]

be the immutable base-neuron label. Fix the first \(P\) normalized
multivariate Hermite functions
\(\phi_1,\ldots,\phi_P\in L^2(\mu)\), ordered by total degree.

For a slow neuron field \(v(\theta)\), define

\[
\langle\phi_j,v\rangle_\mu
=\int\phi_j(\theta)v(\theta)\,d\mu(\theta).
\]

The projection of one iid dense row is the isonormal action

\[
(W^0_Pv)(\theta,\varepsilon)
=\sigma_w\sum_{j=1}^P
\varepsilon_j\langle\phi_j,v\rangle_\mu,
\qquad
\varepsilon\sim N(0,I_P).
\]

This is applied after the dense width limit. It is not a rank-\(P\)
parameterization of any reference network. It is exactly the cylindrical
projection of a Gaussian row operator onto the queried function subspace.
It obeys

\[
\mathbb E_\varepsilon[(W^0_Pv)(W^0_Pv')]
=\sigma_w^2
\langle\Pi_Pv,\Pi_Pv'\rangle_\mu.
\]

Most importantly, the same row coefficients are reused for the transpose.
If \(w=(w_1,\ldots,w_P)\) is the current total row coefficient, then

\[
(W_Pv)(\theta,w)
=\sum_jw_j\langle\phi_j,v\rangle_\mu,
\]

\[
(W_P^*\psi)(\theta)
=\sum_j\phi_j(\theta)
\int d\mu(\theta')\int w_j\psi(\theta',w)
\,d\rho_{s,t}^{\theta'}(w).
\]

Therefore

\[
\langle W_Pv,\psi\rangle_{\mu\otimes\rho}
=\langle v,W_P^*\psi\rangle_\mu
\]

exactly at every finite \(P\). No independent backward Gaussian is used.
The usual Onsager term is the Gaussian integration-by-parts component of
this same identity.

## 4. Conditional Liouville PDE

For each depth \(s\), base label \(\theta\), and training time \(t\), let
\(\rho_{s,t}^{\theta}\) be the conditional law of the current total row
coefficient \(w\in\mathbb R^P\). Initially,

\[
\rho_{s,0}^{\theta}=N(0,\sigma_w^2I_P),
\]

independently of \((s,\theta)\).

Define

\[
H_{jr}(s,t)
:=\int\phi_j(\theta)h_r(s,\theta,t)\,d\mu(\theta),
\]

\[
z_r(s,\theta,w,t)
:=\sum_jw_jH_{jr}(s,t),
\]

\[
\beta_r(s,\theta,w,t)
:=\sigma'(z_r(s,\theta,w,t))p_r(s,\theta,t).
\]

The row-law characteristic velocity is the projected ordinary Euclidean
\(\mu\)P gradient:

\[
\boxed{
V_j(s,\theta,w,t)
=-\gamma\sum_{q=1}^m e_q(t)\,
\beta_q(s,\theta,w,t)H_{jq}(s,t).
}
\]

The finite-dimensional transport PDE is

\[
\boxed{
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\cdot\left(\rho_{s,t}^{\theta}V\right)=0.
}
\tag{OG-PDE}
\]

The coupled slow forward and adjoint depth equations are

\[
\boxed{
\partial_sh_r(s,\theta,t)
=\gamma\int
\sigma(z_r(s,\theta,w,t))
\,d\rho_{s,t}^{\theta}(w),
}
\]

\[
h_r(0,\theta,t)=B(\theta,t)u_r,
\]

\[
\boxed{
-\partial_sp_r(s,\theta,t)
=\gamma\sum_{j=1}^P\phi_j(\theta)
\int d\mu(\theta')\int
w_j\beta_r(s,\theta',w,t)
\,d\rho_{s,t}^{\theta'}(w),
}
\]

\[
p_r(1,\theta,t)=a(\theta,t).
\]

The remaining characteristic equations are

\[
\boxed{
\dot B(\theta,t)
=-\sum_qe_q(t)p_q(0,\theta,t)u_q^\top,
\qquad
\dot a(\theta,t)
=-\sum_qe_q(t)h_q(1,\theta,t).
}
\]

The readout is

\[
f_r(t)=\int a(\theta,t)h_r(1,\theta,t)\,d\mu(\theta).
\]

These equations are autonomous and restartable from
\((B,a,\{\rho_s^\theta\}_{s\in[0,1]})\).

## 5. Exact finite-\(P\) gradient identity

Let

\[
G^h_{rq}(s)
=\langle h_r(s),h_q(s)\rangle_\mu,
\qquad
G^p_{rq}(0)
=\langle p_r(0),p_q(0)\rangle_\mu,
\]

\[
G^\beta_{rq}(s)
=\int d\mu(\theta)\int
\beta_r(s,\theta,w)\beta_q(s,\theta,w)
\,d\rho_s^\theta(w),
\]

\[
G^{h,P}_{rq}(s)
=\sum_{j=1}^P H_{jr}(s)H_{jq}(s).
\]

Then the PDE predictor obeys

\[
\boxed{\dot f=-\Theta_Pe,}
\]

\[
\boxed{
(\Theta_P)_{rq}
=G^h_{rq}(1)
+(u_r^\top u_q)G^p_{rq}(0)
+\gamma^2\int_0^1
G^{h,P}_{rq}(s)G^\beta_{rq}(s)\,ds.
}
\]

Every term is positive semidefinite, so

\[
\dot{\mathcal L}=-e^\top\Theta_Pe\le0.
\]

The implementation verifies the transpose pairing, finite-difference
Euclidean gradients, positive semidefiniteness, and
\(\dot f=-\Theta_Pe\) independently.

## 6. Numerical realization

The main solver writes

\[
w=\sigma_w\varepsilon+c,
\qquad
\dot c_j=V_j,
\]

with fixed Gaussian cubature labels \((\theta,\varepsilon)\). This is the
method of characteristics for (OG-PDE), not a finite network: there is no
original width \(n\), no \(n\times n\) matrix, and no target trajectory in
the velocity.

The three numerical axes are:

- \(P\): Hermite/operator order;
- \(N\): deterministic depth discretization;
- \(M,R\): base-label and Gaussian-row cubature resolution.

The primary run uses

\[
P=5,\qquad N=16,\qquad M=81,\qquad R=128.
\]

Here \(M=3^{d+1}=81\) is order-three tensor Gauss--Hermite cubature in
the immutable base label, while \(R=128\) is scrambled-Sobol cubature in
the row innovation. For fixed \(d=3\), independently of whether
\(m=2,3,4,\) or \(5\), \(P=5\) contains the constant, three input-map
coordinates, and the readout coordinate. The augmented characteristic representation
has \(d+1+2P=14\) scalar coordinates per depth location; the equivalent
conditional law in total \(w\) has \(d+1+P=9\).

## 7. Remaining mathematical identification gap

At fixed finite \(L\), \(W_\ell^\top\beta_\ell\) contains a centered
column-cavity Gaussian component with \(O(1)\) coordinate variance. The
PDE retains its conditional/Onsager mean. In the \(1/L\) residual
backward recurrence, independent depth slices should average the centered
part to RMS size \(O(L^{-1/2})\).

The dense-to-PDE identification therefore requires:

1. trained iid-depth propagation of chaos and cancellation of centered
   row/column innovations as \(L\to\infty\);
2. survival of the conditional Onsager mean represented by the shared
   transpose above;
3. convergence of the Hermite projection as \(P\to\infty\);
4. stability sufficient to pass these limits through the full training
   trajectory.

Earlier experiments provide consistency evidence for the global curves,
the \(N,M,R\) discretization, and increasing dense width/depth. They did
not show monotone improvement with Hermite order \(P\): valid
\(P=15\) and \(P=35\) runs were farther from the finite-network references
than \(P=5\). The present experiment therefore freezes \(P=5\) and tests
transfer across data and activation configurations; it does not claim
\(P\)-convergence or close the ordered-limit theorem.
