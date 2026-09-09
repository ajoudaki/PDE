# Compactness, Weak Identification, and Uniqueness Audit

## Verdict

The exact gradient structure gives real width-uniform compactness for the
predictor and weak compactness for several state components. It does not
identify the adaptive Gaussian source actions, give a compact-time modulus
for the raw kernel, or define a single-valued restartable evolution on the
ordinary one-time node state.

An explicit depth-two pair has identical current forward/backward fields,
predictor, raw kernel, and all scalar overlaps among those fields, but
different next forward derivative and different derivative of the raw
kernel. Thus compactness plus nodewise Young measures cannot yield
uniqueness. Restoring predictivity requires transverse source-action data,
whose closure is the operator-word/response hierarchy.

This kills compactness--identification--uniqueness as an easier completion.
The finite-state witness does not by itself exclude every richer state
restricted to the actual reachable manifold; it proves that any such state
must retain more than ordinary current node laws and overlaps.

## 1. Exact energy geometry and scaling

Let

\[
|v|_n^2=\langle v,v\rangle_n,\qquad
p_n=\langle A,x_D\rangle_n.
\]

For the parameter metric

\[
\|\delta\theta\|_{g,n}^2
=|\delta A|_n^2+|\delta u|_n^2
+\sum_{l=1}^{D-1}\|\delta G_l\|_F^2,
\]

the finite flow is exactly

\[
\dot\theta=\nabla_g p_n.
\]

Therefore

\[
\boxed{
\dot p_n=K_n
=|x_D|_n^2+|b_1|_n^2+
\sum_{l=1}^{D-1}|b_{l+1}|_n^2|x_l|_n^2
=\|\dot\theta\|_{g,n}^2\ge0 .
}                                                                  \tag{1}
\]

Let \(c_\phi=\pi/2\), \(a=|A|_n\), \(B_l=|b_l|_n\), and
\(M_l=\|G_l\|_{\rm op}\). Boundedness of arctangent and its derivative gives

\[
|x_l|_n\le c_\phi,\qquad
B_D\le a,\qquad B_l\le M_lB_{l+1},
\]

\[
a(t)\le a(0)+c_\phi t,
\]

and

\[
M_l(t)\le M_l(0)+c_\phi\int_0^tB_{l+1}(s)\,ds.                    \tag{2}
\]

The inequalities are triangular from the last layer downward. Hence for
fixed \(D,T\), on the usual Gaussian initial localization,

\[
\sup_{t\le T}\left(
a(t)+|u(t)|_n+\sum_l(M_l(t)+B_l(t))
\right)\le C_{D,T}.                                                \tag{3}
\]

The scales are consequently:

- vectors have Euclidean norm \(O(\sqrt n)\) and normalized norm \(O(1)\);
- Gaussian source matrices have operator norm \(O(1)\) and Frobenius norm
  \(O(\sqrt n)\);
- each entry of \(\dot G_l\) is typically \(O(n^{-1})\);
- \(\|\dot G_l\|_F=\|\dot G_l\|_{\rm op}=O(1)\), since it is rank one;
- \(G_l(t)-\Gamma_l\) has \(O_T(1)\) operator and Frobenius norm;
- \(p_n\) and \(K_n\) have order one.

For forward fields,

\[
\dot z_1=b_1,\qquad
\dot z_{l+1}=b_{l+1}|x_l|_n^2+G_l\dot x_l,\qquad
|\dot x_l|_n\le|\dot z_l|_n.
\]

Induction using (3) gives

\[
\sup_{t\le T}\bigl(|\dot z_l(t)|_n+|\dot x_l(t)|_n\bigr)
\le C_{D,T}.                                                       \tag{4}
\]

After step-function embedding, this supplies compactness in
\(C([0,T];L^2_{\rm weak})\) for the forward vectors and weak Hilbert--Schmidt
compactness for the learned matrix increments. Coordinate nonlinearities
need joint Young measures.

For the top backward field, the exact arctangent grouping is

\[
\dot b_D=x_D\phi'(z_D)
+b_D\frac{\phi''(z_D)}{\phi'(z_D)}\dot z_D,\qquad
\left|\frac{\phi''}{\phi'}\right|\le1.                             \tag{5}
\]

The product in (5) gives only an averaged \(L^1\)-in-time derivative bound
from energy-level information. Lower backward fields require still more
products. Thus energy alone does not make \(b_l,r_l\), or \(K_n\)
equicontinuous.

A precise positive consequence is:

\[
p_n\ \text{is tight in }C([0,T]),\qquad
K_n\ \text{is only weak-* tight in }L^\infty(0,T),                \tag{6}
\]

and every subsequential pair satisfies \(K=\dot p\) distributionally.
Equation (6) is weaker than uniform raw-kernel convergence.

There is also a topology mismatch. For deterministic bounded normalized
vectors \(f_n,g_n\),

\[
\langle f_n,\Gamma_lg_n\rangle_n\longrightarrow0,
\]

so the Gaussian matrix vanishes in weak operator topology. Yet for an
independent normalized \(g_n\),

\[
|\Gamma_lg_n|_n^2-|g_n|_n^2\longrightarrow0.
\]

Every compact operator topology supplied by the energy therefore erases a
leading random action.

## 2. Exact weak formulation and its missing term

Put

\[
C_l(s,t)=\langle x_l(s),x_l(t)\rangle_n,\qquad
R_{l+1}(s,t)=\langle b_{l+1}(s),b_{l+1}(t)\rangle_n.
\]

For test paths \(h,k\), the integrated source identities give

\[
\begin{aligned}
\int_0^T\langle h(t),z_{l+1}(t)\rangle_n\,dt
={}&\int_0^T\langle h(t),\Gamma_lx_l(t)\rangle_n\,dt\\
&+\int_{0\le s\le t\le T}
\langle h(t),b_{l+1}(s)\rangle_nC_l(s,t)\,ds\,dt,
\end{aligned}                                                      \tag{7}
\]

and

\[
\begin{aligned}
\int_0^T\langle k(t),r_l(t)\rangle_n\,dt
={}&\int_0^T\langle k(t),\Gamma_l^Tb_{l+1}(t)\rangle_n\,dt\\
&+\int_{0\le s\le t\le T}
\langle k(t),x_l(s)\rangle_nR_{l+1}(s,t)\,ds\,dt.
\end{aligned}                                                      \tag{8}
\]

At positive time, the vectors in the first terms depend on the same source.
For a generic empirical test, Gaussian integration by parts gives

\[
\mathbb E\!\left[\frac1n\sum_{i,j}\psi_i\Gamma_{ij}x_j\right]
=\frac1{n^2}\sum_{i,j}
\mathbb E\!\left[\partial_{\Gamma_{ij}}(\psi_ix_j)\right].         \tag{9}
\]

The right side contains the source derivatives of the current flow. They
obey the tangent dynamics; iterating (9) generates the response hierarchy.
Weak compactness does not identify this term.

Rank-one integration merely rewrites the missing data as the two-time
quantities in (7)--(8). Arctangent bounds coefficients but does not express
those cross-time couplings from a current node marginal. Classical
compensated compactness has no complementary spatial differential
constraints here.

## 3. Exact depth-two nonclosure witness

Let

\[
\alpha=\arctan 1=\frac\pi4,\qquad
u=(0,1),\qquad x_1=(0,\alpha),
\]

\[
z_2=(1,0),\qquad A=(0,1),\qquad b_2=(0,1),
\]

and, for \(c\in\mathbb R\),

\[
G_c=
\begin{pmatrix}
c&1/\alpha\\
1&0
\end{pmatrix}.
\]

Then

\[
G_cx_1=z_2,\qquad G_c^Tb_2=(1,0)=r_1,\qquad
b_1=\phi'(u)\odot r_1=(1,0),
\]

independently of \(c\). Hence every displayed forward/backward node field,
the predictor, the raw kernel, and every scalar overlap among these fields
agree for all \(c\).

Nevertheless,

\[
\dot x_1=(1,0),\qquad
\dot G_c=\frac12b_2x_1^T,
\]

and therefore

\[
\dot z_2=\dot G_cx_1+G_c\dot x_1
=\left(c,1+\frac{\alpha^2}{2}\right).                              \tag{10}
\]

For

\[
K=|x_2|_n^2+|b_1|_n^2+|b_2|_n^2|x_1|_n^2,
\]

direct differentiation gives

\[
\dot K=\alpha c.                                                    \tag{11}
\]

The choices \(c\) and \(-c\) even have identical Frobenius norm and singular
values, while reversing \(\dot K\).

The general hidden direction is:

\[
\Delta G\,x=0,\qquad \Delta G^Tb=0,\qquad
\Delta G\,\dot x\ne0.                                              \tag{12}
\]

For example, take

\[
\Delta G=\lambda ae^T,\qquad
a\perp b,\quad e\perp x,\quad e^T\dot x\ne0.
\]

In high dimension, delocalized \(a,e\) make the entries of \(\Delta G\)
small and its normalized spectral mass vanish, while its next action remains
order one. Thus entry distributions and leading spectral laws do not repair
the state.

One derivative can be repaired by retaining the transverse action of \(G\)
on \(\dot x\) and its adjoint analogue. The next derivative needs the action
on \(\ddot x\), and so on. Exact restarting therefore needs the operator on
the complete forward/backward cyclic subspaces, or a proved finite
compression of those operator words.

Claim-level caveat: (10)--(12) prove nonsufficiency on a state space that
admits these microstates. A closure defined only on the actual
infinite-width reachable manifold could in principle impose extra relations.
It must prove those relations and show that its finite state distinguishes
all reachable transverse actions; the counterexample cannot simply be
ignored.

## 4. Why standard uniqueness theories do not repair the state

The reduced node state has no single-valued vector field by (10), so an
Osgood or one-sided Lipschitz theorem cannot even be formulated there.

Nor is the full flow monotone. The scalar restriction

\[
f(A,u)=A\arctan u
\]

has Hessian at the origin

\[
\nabla^2f(0,0)=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

with eigenvalues \(1,-1\). Neither sign of its gradient is monotone.
Lasry--Lions and maximal-monotone uniqueness therefore have no applicable
global sign.

A relative-energy comparison of full states reads

\[
\frac12\frac d{dt}\|\theta-\widetilde\theta\|_{g,n}^2
=\langle\theta-\widetilde\theta,
\nabla_gp_n(\theta)-\nabla_gp_n(\widetilde\theta)\rangle_{g,n}.     \tag{13}
\]

Closing (13) on every difference direction needs an ambient one-sided
Hessian bound, which is stronger than the target. Restricting to actual
reachable differences recovers the original reachable-stability problem.

## 5. Sufficient abstract theorem and leaf audit

A compactness route would need a Polish one-time state \(\mathcal S\) such
that:

1. the state, predictor, and kernel are compact in their required
   compact-time topologies;
2. a countable separating test algebra has a closed limiting generator;
3. the weak limiting equation is unique for every admissible restart state;
4. predictor and kernel are continuous state observables;
5. finite autonomous truncations approximate the state with a computable
   error tending to zero.

Then standard subsequence identification and uniqueness would imply the full
limit. The actual leaves are:

- **Energy compactness:** established for the predictor, forward weak paths,
  and learned increments.
- **Kernel time modulus:** open; differentiating the kernel evaluates the
  Hessian on the flow direction.
- **Source identification:** open; (9) gives the response hierarchy.
- **Ordinary one-time node generator:** falsified by (10)--(12).
- **Weak--strong uniqueness:** unavailable before closure and otherwise
  needs the same or a stronger stability estimate.
- **Finite truncation tail:** open for the cyclic source-action hierarchy.

Measure-valued solutions, nonlinear martingale problems, modulated energy,
ordinary graphons, and hydrodynamic relative entropy do not alter these
leaves. A full causal two-time covariance/response state is a plausible
Volterra closure, but violates the stipulated one-time contract.

The genuine positive result is subsequential compactness of the predictor
and weak state pieces. It is not convergence of the raw kernel or a
computable autonomous limit. The route is therefore rejected as a
standalone completion.
