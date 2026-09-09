# A joint mean-field/gradient-flow limit for a nonlinear three-hidden-layer network

## The theorem

Fix integers \(p,d\ge 1\), pairwise distinct vectors \(x_1,\ldots,x_p\in\mathbb R^d\) with \(\|x_a\|^2=d\), and labels \(y_a\in\{-1,1\}\). Put
\[
R_{ab}=d^{-1}x_a^\top x_b,\qquad \phi(u)=\sin u+\cos u,
\qquad \gamma=2/p.
\]
For each width \(n\), consider
\[
\begin{aligned}
U_i^a&=w_i^\top x_a,&H_{1,i}^a&=\phi(U_i^a),\\
S_j^a&=\sum_iB_{ji}H_{1,i}^a,&H_{2,j}^a&=\phi(S_j^a),\\
T_k^a&=\sum_jA_{kj}H_{2,j}^a,&H_{3,k}^a&=\phi(T_k^a),\\
f_a&=\sum_kc_kH_{3,k}^a,&
\mathcal L_n&=p^{-1}\sum_a(f_a-y_a)^2.
\end{aligned}
\]
Initialize all entries independently by
\[
w_{ir}\sim N(0,d^{-1}),\qquad A_{kj},B_{ji}\sim N(0,n^{-1}),
\qquad c_k\sim N(0,n^{-4}).
\]
Use layer multipliers
\[
\lambda_{w,n}=n/d,\qquad \lambda_{B,n}=\lambda_{A,n}=1,
\qquad \lambda_{c,n}=1/n
\]
and exact full-batch GD with base step
\[
\eta_{0,n}=e^{-e^n}.
\]
Interpolate at time \(t=k\eta_{0,n}\).

Then there is \(T_*>0\) such that, for every \(T<T_*\), the exact interpolated GD dynamics converge in probability, along the full sequence \(n\to\infty\), to a unique autonomous action-law flow. The three empirical path laws of \(U,S,T\) converge in \(W_2(C([0,T];\mathbb R^p))\). Their sample marginals have finite positive variance; all three layers have positive integrated mean-square velocity and nonzero displacement; every one of the four scaled NTK blocks has a finite positive time integral; \(\phi\) remains non-affine in \(L^2\) on every hidden marginal; the total NTK is nonconstant; and \(\mathcal L(T)<\mathcal L(0)\). Constants and \(T_*\) may depend on the fixed dataset. No lower bound on pairwise separation is assumed.

The topology called the *action law* below is the countable-probe GNS topology. It records every fixed finite expression obtained from the current neuron marks by coordinate maps, normalized inner products, and applications of the two current matrices and their adjoints. It does not assert operator-norm convergence of the full random matrices.

## 1. Exact finite-width normalization

Write
\[
\langle u,v\rangle_n=n^{-1}u^\top v,
\qquad (u\otimes_n v)z=u\langle v,z\rangle_n,
\qquad C=nc.
\]
Then \(f_a=\langle C,H_3^a\rangle_n\). Define
\[
D_3^a=C\odot\phi'(T^a),\quad P_2^a=A^\top D_3^a,
\quad D_2^a=\phi'(S^a)\odot P_2^a,
\quad P_1^a=B^\top D_2^a.
\]
Direct differentiation, retaining every factor of \(n\), gives the layer-scaled gradient flow
\[
\begin{aligned}
\dot U^a&=-\gamma\sum_bR_{ab}e_b\,
 \phi'(U^b)\odot P_1^b,\\
\dot B&=-\gamma\sum_be_bD_2^b\otimes_nH_1^b,\\
\dot A&=-\gamma\sum_be_bD_3^b\otimes_nH_2^b,\\
\dot C&=-\gamma\sum_be_bH_3^b,
\end{aligned}\tag{1.1}
\]
where \(e_a=f_a-y_a\). For example,
\(\partial f_a/\partial B_{ji}=n^{-1}D_{2,j}^aH_{1,i}^a\), and
\(\partial f_a/\partial w_i=n^{-1}P_{1,i}^a\phi'(U_i^a)x_a\); multiplying by \(\lambda_B=1\) and \(\lambda_w=n/d\) yields (1.1).

The four scaled tangent kernels are
\[
\begin{aligned}
K^C_{ab}&=\langle H_3^a,H_3^b\rangle_n,\\
K^A_{ab}&=\langle H_2^a,H_2^b\rangle_n
             \langle D_3^a,D_3^b\rangle_n,\\
K^B_{ab}&=\langle H_1^a,H_1^b\rangle_n
             \langle D_2^a,D_2^b\rangle_n,\\
K^U_{ab}&=R_{ab}\langle\phi'(U^a)P_1^a,
                         \phi'(U^b)P_1^b\rangle_n.
\end{aligned}\tag{1.2}
\]
Thus, with \(K=K^C+K^A+K^B+K^U\),
\[
\dot f=-\gamma Ke,qquad
\dot{\mathcal L}_n=-\gamma^2e^\top Ke.
\tag{1.3}
\]
Exact GD in the normalized variables is exactly explicit Euler for (1.1), with step \(\eta_{0,n}\). Also \(\eta_{0,n}\lambda_{\ell,n}\to0\) for all four blocks.

## 2. The fixed finite Gaussian-program theorem used below

We use the following specialization of the parameterless NetsorT Master Theorem of G. Yang, *Tensor Programs III: Neural Matrix Laws*, arXiv:2009.10685v3.

**Tensor-program theorem.** Let \(W_1,\ldots,W_s\) be independent \(n\times n\) matrices with iid \(N(0,\sigma_r^2/n)\) entries. Let the coordinate slices of finitely many initial vectors be iid copies of a finite jointly Gaussian vector; its covariance may be singular. From these data form a fixed finite program by coordinatewise polynomially bounded maps and arbitrary finite applications of every \(W_r\) and \(W_r^\top\). For program vectors \(X_n^1,\ldots,X_n^m\) and a polynomially bounded test \(\Psi\),
\[
n^{-1}\sum_i\Psi(X_{n,i}^1,\ldots,X_{n,i}^m)
\longrightarrow \mathbb E\Psi(X^1,\ldots,X^m)
\quad\text{almost surely}.\tag{2.1}
\]
No rank-stability assumption is imposed. If all coordinate maps are linearly bounded and \(\Psi\) is quadratically bounded, the same convergence holds in \(L^1\).

For completeness, the essential conditional calculation in its proof is recorded. If previous uses of a Gaussian matrix \(W\) impose
\[
X=WY,qquad U=W^\top V,
\]
then, conditionally on the previous program,
\[
W\overset d=E+P_V^\perp\widetilde W P_Y^\perp,
\quad
E=XY^++V^{+\top}U^\top-V^{+\top}U^\top YY^+.
\tag{2.2}
\]
Consequently
\[
Wh\overset d=Eh+\sigma P_V^\perp z,qquad
\sigma^2=n^{-1}\|P_Y^\perp h\|^2,
\tag{2.3}
\]
with \(z\sim N(0,I_n)\) independent of the past. The proof maintains a full-support core set. When the limiting \(\sigma\) is positive, (2.3) adds a fresh Gaussian core coordinate. When it is zero, the zero-stability lemma proves that the limiting linear dependence is eventually an exact finite-width dependence. This proves rank stability, including at singular Grams, rather than assuming it. Conditional Gaussian concentration and moment induction prove (2.1). The mean version follows from Gaussian operator-norm tails and the fact that linearly bounded coordinate maps preserve normalized \(L^2\) bounds.

The limiting reused-matrix rule can be stated without derivatives. Suppose a new call is \(W^sX\), \(s\in\{+,-\}\), and the preceding opposite calls are \(W^{-s}Y_1,\ldots,W^{-s}Y_q\). Let
\[
G_{ij}=\mathbb E[Y_iY_j],qquad
b_i=\mathbb E[\widehat W^{-s}[Y_i]X].
\]
Then
\[
W^s[X]=\widehat W^s[X]+\sum_i(G^+b)_iY_i,
\tag{2.4}
\]
where same-orientation innovations have covariance
\(\mathbb E[\widehat W^s[X]\widehat W^s[X']]=\mathbb E[XX']\), and the two orientations and distinct matrices have independent innovation families. If \(G\) is singular, \(b\in\operatorname{ran}G\); the response in (2.4) is the unique element of \(\operatorname{span}\{Y_i\}\) with the prescribed covariances and is invariant under redundant calls. When symbolic derivatives are used, (2.4) is
\[
W^s[X]=\widehat W^s[X]
+\sum_{W^{-s}Y_i\prec X}Y_i
\mathbb E\frac{\partial X}{\partial\widehat W^{-s}[Y_i]}.
\tag{2.5}
\]
The innovation in (2.4) must not be omitted.

## 3. Fixed-mesh identification of the actual network

Choose \(\tau_R\in C^\infty(\mathbb R)\) so that
\[
\tau_R(x)=x\ (|x|\le R),\quad |\tau_R'|\le1,
\quad |\tau_R(x)|\le2R,\quad \tau_R(0)=0.
\tag{3.1}
\]
The clipped dynamics computes the preclip \(P_2=A^\top D_3\), sets
\(D_2=\phi'(S)\tau_R(P_2)\), computes the preclip
\(P_1=B^\top D_2\), and replaces \(P_1\) by \(\tau_R(P_1)\) only in the \(U\)-update. It does not clip \(D_3,A,B,C\).

Fix \(R,h>0\) and \(K_0=\lceil T/h\rceil<\infty\). Unrolling Euler gives the exact identities
\[
\begin{aligned}
B_kv&=B_0v-\gamma h\sum_{\ell<k,b}e_{\ell b}D_{2,\ell}^b
 \langle H_{1,\ell}^b,v\rangle_n,\\
B_k^\top v&=B_0^\top v-\gamma h\sum_{\ell<k,b}e_{\ell b}H_{1,\ell}^b
 \langle D_{2,\ell}^b,v\rangle_n,\\
A_kv&=A_0v-\gamma h\sum_{\ell<k,b}e_{\ell b}D_{3,\ell}^b
 \langle H_{2,\ell}^b,v\rangle_n,\\
A_k^\top v&=A_0^\top v-\gamma h\sum_{\ell<k,b}e_{\ell b}H_{2,\ell}^b
 \langle D_{3,\ell}^b,v\rangle_n.
\end{aligned}\tag{3.2}
\]

Construct a deterministic oracle recursively. Replace every error by
\[
\bar e_{k,a}=\mathbb E[C_kH_{3,k}^a]-y_a
\tag{3.3}
\]
and every overlap in (3.2) by the corresponding already-defined population expectation. Keep \(A_0,B_0\) as two separate independent Gaussian matrices. The causal order is
\[
U,H_1\to S,H_2\to T,H_3,e\to D_3,P_2,D_2,P_1
\to(U^+,C^+,A^+,B^+).
\tag{3.4}
\]
Thus every coefficient used by the oracle has already been defined. After substituting (3.2), this is a finite parameterless tensor program: its only matrices are \(A_0,B_0\) and their transposes, its initial vector is an iid-coordinate copy of \(N(0,R)\) together with zero, and every coordinate map is linearly bounded. The theorem of Section 2 identifies its limiting variables with the all-history rule (2.4), and gives all empirical inner products and quadratic kernel quantities.

It remains to restore empirical scalar feedback. Couple the actual and oracle programs with the same \(A_0,B_0,U_0\), and put the oracle readout equal to zero. The physical \(C_0=nc_0\) satisfies
\[
\mathbb E\|C_0\|_n^2=n^{-2},\qquad
\|C_0\|_n+\|C_0\|_\infty\longrightarrow0
\quad\text{in probability}.\tag{3.5}
\]
On the event \(\|A_0\|_{\rm op}+\|B_0\|_{\rm op}\le M\), whose probability tends to one, induct over the finite list (3.4). Coordinate maps are Lipschitz because of (3.1), \(C_k\) is coordinatewise bounded for fixed \(k\), and
\[
\|u\otimes_n v\|_{\rm op}=\|u\|_n\|v\|_n.
\]
For a learned action, add and subtract the oracle vector, coefficient, and overlap in (3.2), and use Cauchy--Schwarz. If \(\delta_k\) is the maximum normalized \(L^2\) error of constructed vectors together with the operator norm of the two learned rank memories, this gives
\[
\delta_{k+1}\le(1+C_Rh)\delta_k+C_Rh\zeta_{n,k},
\tag{3.6}
\]
where \(\zeta_{n,k}\to0\) collects only oracle empirical-minus-population errors. Fixed-step Gronwall and (2.1) give
\[
\max_{k\le K_0}\delta_k\longrightarrow0
\quad\text{in probability}.\tag{3.7}
\]
Hence the actual clipped Euler network has the asserted Gaussian operator DAG at every fixed \((R,h,K_0)\).

Enumerate a countable grammar of rational linear combinations, bounded coordinate maps, normalized inner products, and current applications of \(A,A^\top,B,B^\top\). Simultaneous convergence of every finite initial segment defines a positive kernel
\(\Gamma(q,q')=\mathbb E[Z_qZ_{q'}]\). Quotient its rational span by the zero seminorm and complete. The exact finite-width transpose identities pass to the limit, so \(A^\dagger,A\) and \(B^\dagger,B\) are adjoint bounded maps on the resulting layer Hilbert spaces. This GNS action state, with metric
\[
d_{\rm act}(s,s')=\sum_{m\ge1}2^{-m}
 \bigl(1\wedge|\Gamma_s(q_i,q_j)-\Gamma_{s'}(q_i,q_j)|\bigr)
\tag{3.8}
\]
under any enumeration of pairs, is the state topology used below. It contains all forward laws, adjoint laws, kernels, output, and loss, but does not claim full-matrix operator-norm convergence.

## 4. A uniform all-source estimate

This section supplies the estimate needed to let the auxiliary mesh tend to zero and then remove the cutoff. It is a statement about the limiting Gaussian DAG, not about individual finite-width coordinates.

For a compiled Euler DAG, retain every Gaussian innovation in (2.5), including redundant innovations at a singular covariance. For an action node \(q\), let \(b(q)\) be its cycle of birth. For a scalar node \(X\), let
\[
I_q(X)=\left\|\frac{\partial X}{\partial \widehat Z_q}\right\|_2,
\qquad
I(X)=\sum_q h^{\mathbf1_{\{b(q)<b(X)\}}}I_q(X).
\tag{4.1}
\]
The factor in (4.1) records the following exact property of the compiled network: every path from a source born in an earlier cycle to a node in the current cycle crosses either an Euler update or a learned-rank term in (3.2), and therefore contains a factor \(h\). Within one cycle the order (3.4) is acyclic. Define \(J_k\) as one plus the maximum, over nodes constructed through cycle \(k\), of the corresponding weighted derivative sum, and include in \(J_k\) the absolute sums of all response coefficients in (2.5).

**All-source lemma.** There are constants \(c_0,c_1<\infty\) and \(T_0>0\), depending only on \(p\) and the bounds \(\max_r\|\phi^{(r)}\|_\infty=\sqrt2\), such that, for \(0<h\le T\le T_0\), \(R\ge1\), and \(kh\le T\),
\[
\max_{a\le p}\bigl(\|P_{1,k}^a\|_{\psi_2}+
                         \|P_{2,k}^a\|_{\psi_2}\bigr)
\le c_0T,
\qquad
\mathbb EJ_k^2\le c_1.
\tag{4.2}
\]
Both constants are independent of \(h,R\) and of singularities of source covariances.

**Proof.** Since \(|H_3|\le\sqrt2\), the clipped Euler equations give, with \(c_k=\|C_k\|_\infty\),
\[
c_{k+1}\le(1+2\gamma ph)c_k+\gamma ph\sqrt2,
\]
because \(|e_a|\le1+\sqrt2c_k\). Hence, for \(kh\le T\le1\),
\[
\|C_k\|_\infty+\max_a\|D_{3,k}^a\|_\infty\le cT,
\qquad \max_a|e_{k,a}|\le c.\tag{4.3}
\]

Differentiate the compiled DAG. The only product rules containing an unbounded value are
\[
\begin{aligned}
d\{\phi'(U)\tau_R(P_1)\}
 &=\phi''(U)\tau_R(P_1)dU+\phi'(U)\tau_R'(P_1)dP_1,\\
dD_2
 &=\phi''(S)\tau_R(P_2)dS+\phi'(S)\tau_R'(P_2)dP_2,\\
dD_3&=\phi'(T)dC+C\phi''(T)dT.
\end{aligned}\tag{4.4}
\]
Here \(|\tau_R(x)|\le|x|\) and \(|\tau_R'|\le1\), so no factor \(R\) appears. All other same-cycle derivatives are bounded by a numerical constant times the sum of the derivatives of their parents. Every cross-cycle edge has the factor \(\gamma h\), as follows directly from (3.2) and the two Euler updates for \(U,C\). Induction in the order (3.4), followed by summation over source paths, therefore gives
\[
J_k\le c\left(1+h\sum_{\ell<k}X_\ell J_\ell\right),
\qquad
X_\ell=1+\sum_{a=1}^p(|P_{1,\ell}^a|+|P_{2,\ell}^a|).
\tag{4.5}
\]
This is a path-counting identity: a path contributing to the right side has a unique last cross-cycle edge; removing that edge leaves one of the source paths counted by \(J_\ell\). Conversely every such choice gives a path in the current DAG. Discrete Gronwall yields
\[
J_k\le c\exp\left(ch\sum_{\ell<k}X_\ell\right).
\tag{4.6}
\]

Suppose provisionally that
\[
q:=\max_{\ell\le k,a}\bigl(\|P_{1,\ell}^a\|_{\psi_2}
 +\|P_{2,\ell}^a\|_{\psi_2}\bigr)\le1.
\tag{4.7}
\]
Convexity gives, without independence,
\[
\mathbb E\exp\left(\lambda h\sum_{\ell<k}|P_{r,\ell}^a|\right)
\le\max_{\ell<k}\mathbb Ee^{\lambda T|P_{r,\ell}^a|}
\le2e^{c\lambda^2T^2q^2}.
\tag{4.8}
\]
Equations (4.6)--(4.8), with fixed \(\lambda\), imply
\(\mathbb EJ_k^2\le c\).

Let \(r_{3,k}\) be the sum of the absolute response coefficients in the call \(A_0^\top D_{3,k}^a\), maximized over \(a\), and let \(r_{2,k}\) be the analogous sum for \(B_0^\top D_{2,k}^a\). Tracing the factors in (4.4) gives
\[
r_{3,k}\le cT(\mathbb EJ_k^2)^{1/2},
\qquad
r_{2,k}\le c(q_{2,k}+T)(\mathbb EJ_k^2)^{1/2},
\tag{4.9}
\]
where \(q_{r,k}=\max_{\ell\le k,a}\|P_{r,\ell}^a\|_{\psi_2}\). For the first inequality, every derivative of \(D_3=C\phi'(T)\) contains either \(C=O(T)\), by (4.3), or a derivative of \(C\); the latter has crossed the update \(C_{j+1}-C_j=-\gamma h\sum eH_3\), and summing its weights gives at most \(T\). For the second inequality, the first term in \(dD_2\) is bounded in expectation by Cauchy--Schwarz as \(c q_{2,k}(\mathbb EJ_k^2)^{1/2}\); the derivative of \(P_2\) with respect to a \(B\)-forward source must first pass through \(D_3\), so (4.3) supplies the remaining \(T\). These account for the two terms of \(dD_2\) and hence exhaust all \(B\)-response paths.

Now decompose the two transpose calls using (2.5) and the learned terms in (3.2). The fresh innovation in \(P_2\) is centered Gaussian with standard deviation \(\|D_3\|_2\le cT\); its response is a linear combination of bounded \(H_2\)'s of total coefficient mass \(r_{3,k}\); and its learned term is bounded by
\(ch\sum_{\ell<k}\|D_{3,\ell}\|_2\|D_{3,k}\|_2\le cT^3\). Thus
\[
q_{2,k}\le cT+cr_{3,k}+cT^3.\tag{4.10}
\]
Likewise the fresh innovation in \(P_1\) has standard deviation at most
\(c\|D_2\|_2\le cq_{2,k}\), its response has size at most \(cr_{2,k}\), and its learned term is at most \(cTq_{2,k}^2\). Hence
\[
q_{1,k}\le cq_{2,k}+cr_{2,k}+cTq_{2,k}^2.\tag{4.11}
\]

Let \(k_*\) be the first index for which \(q_{1,k}+q_{2,k}>1\). Before and at the construction of that index, (4.7)--(4.9) apply. First (4.9)--(4.10) give \(q_{2,k_*}\le cT\). Only after this estimate, the second inequality in (4.9) and (4.11) give \(q_{1,k_*}\le cT\). Taking \(T_0\) so that \(2cT_0<1\) contradicts the definition of \(k_*\). This proves (4.2). The argument used the symbolic source graph and Gaussian integration by parts, not a covariance inverse, so singular covariances do not change it. \(\square\)

In particular, for \(r=1,2\), uniformly in \(h,R,k,a\),
\[
\mathbb E\bigl[|P_{r,k}^a|^2\mathbf1_{\{|P_{r,k}^a|>u\}}\bigr]
\le cT^2\left(1+u^2/T^2\right)e^{-cu^2/T^2}.
\tag{4.12}
\]

## 5. The compact-time limit

For fixed \(R\), eliminate the trained matrices using the integral form of (3.2). On the event \(\|A_0\|_{\rm op}+\|B_0\|_{\rm op}\le M\), the clipped signal map and vector field are Lipschitz in normalized \(L^2\), the two learned-rank operator norms, and the finitely many scalar overlaps. The Lipschitz constant \(L_R\) is independent of \(n\): the only otherwise problematic products contain \(\tau_R(P)\), bounded by \(2R\). Therefore the finite-width clipped ODE and its Euler scheme satisfy
\[
\sup_{kh\le T}d(X_{n,R}(kh),X_{n,R}^h(kh))
\le C_{R,T}h.\tag{5.1}
\]
The same estimate compares two meshes on the same initialization.

At fixed \((R,h)\), Section 3 gives the width limit. Apply (5.1) to two meshes, then take \(n\to\infty\). The limiting mesh action states are Cauchy as \(h\downarrow0\), and define a clipped continuous action state \(X_R(t)\), uniformly on \([0,T]\). The same estimate proves uniqueness for fixed \(R\).

We next transfer (4.12) to finite width. For fixed \((R,h)\), every oracle coordinate map is linearly bounded and
\[
\Psi_R(x)=|x-\tau_R(x)|^2
\]
is quadratically bounded. The mean form of the tensor-program theorem therefore gives convergence of its empirical average. Actual--oracle coupling transfers it because \(x\mapsto x-\tau_R(x)\) is \(2\)-Lipschitz. Finally (5.1) transfers the estimate from Euler paths to the clipped ODE and permits integration in time. Consequently
\[
\limsup_{n\to\infty}\mathbb E\int_0^T
\sum_{a,r}\|P_{r,n,R}^a(t)-\tau_R(P_{r,n,R}^a(t))\|_n^2dt
\le C_Te^{-cR^2/T^2}.\tag{5.2}
\]

Let \(X_n\) be the uncut finite-width ODE and \(X_{n,R}\) the clipped one. At either gate use
\[
\begin{aligned}
\phi'(u)p-\phi'(u_R)\tau_R(p_R)
={}&\phi'(u)(p-p_R)+\phi'(u)(p_R-\tau_R(p_R))\\
&+[\phi'(u)-\phi'(u_R)]\tau_R(p_R).
\end{aligned}\tag{5.3}
\]
The uncut field never appears in an \(L^\infty\) factor. Applying (5.3) at both adjoints and using (3.2) for both matrices gives, for the complete state distance \(D_{n,R}\),
\[
D_{n,R}'(t)\le C_T(1+R)D_{n,R}(t)+C_TS_{n,R}(t),\tag{5.4}
\]
where \(S_{n,R}\) is the sum of the clipped residual norms occurring in (5.2). Gronwall and Cauchy--Schwarz yield
\[
\limsup_{n\to\infty}\mathbb E\sup_{t\le T}D_{n,R}(t)
\le C_T\exp(C_TRT-cR^2/T^2)\longrightarrow0.\tag{5.5}
\]
The identical comparison between cutoffs \(R<R'\) shows that \(X_R\) is Cauchy as \(R\to\infty\). Its limit \(X\) solves the uncut equations, and (5.5) identifies the uncut finite-width ODE with \(X\). Uniqueness follows by comparing two candidate uncut solutions with the same cutoff solution and then sending \(R\to\infty\). Because the state is the current GNS action state, rather than a marginal list of fields, this comparison can be restarted from any \(t_0<T\); hence the evolution is autonomous and restartable on its existence interval.

For the three preactivation path laws, the inequality
\[
\frac1n\sum_i\sup_{s,t\in I}|Z_i(t)-Z_i(s)|^2
\le |I|\int_I\frac1n\sum_i|\dot Z_i(u)|^2du
\tag{5.6}
\]
gives tightness in \(C([0,T];\mathbb R^p)\). Fixed-grid action convergence, (4.12), and (5.6) give convergence of second moments and therefore \(W_2\) path convergence. The same uniform integrability passes every kernel block, output, loss, and squared velocity.

Finally compare exact GD with the finite-width uncut ODE. On the event that every underlying standard Gaussian initialization variable is at most \(n\) in absolute value, whose complement has probability at most \(Cn^2e^{-n^2/2}\), the triangular structure of (1.1) gives, for fixed \(T\), exponents \(q_0,q_1<\infty\) such that the ODE trajectory is contained in a ball of radius \(n^{q_0}\) and
\[
\sup_{\|\theta\|\le2n^{q_0}}
(\|F_n(\theta)\|+\|DF_n(\theta)\|)\le n^{q_1}.\tag{5.7}
\]
This follows successively: \(C\) obeys a scalar linear bound because \(H_3\) is bounded; \(A\) is then bounded by integrating \(D_3\); \(P_2,D_2,B\) follow; and finally \(P_1,U\) follow. Euler's error recursion gives
\[
\sup_{k\eta_{0,n}\le T}
\|X_{n,k}^{\rm GD}-X_n(k\eta_{0,n})\|
\le C_T\eta_{0,n}n^{q_1}e^{Tn^{q_1}}.\tag{5.8}
\]
With \(\eta_{0,n}=e^{-e^n}\), (5.8) tends to zero. Combining (5.5), fixed-\(R\) convergence, and (5.8) proves the claimed full diagonal joint limit.

## 6. The initialization law and its strict nondegeneracy

All random variables in this section are the one-coordinate variables of the limiting action state at time zero. Entrywise exponentials are denoted by \(\exp^{\circ}\). Since each \(U^a\) has variance one,
\[
 Q_1:=\mathbb E[H_1H_1^\top]=\exp^{\circ}(-\mathbf1\mathbf1^\top+R),
 \qquad (Q_1)_{ab}=e^{-1+R_{ab}}. \tag{6.1}
\]
Conditionally applying the Gaussian matrix theorem first to \(B_0\) and then to \(A_0\) gives centered Gaussian vectors
\[
 S\sim N(0,Q_1),\qquad T\sim N(0,Q_2), \tag{6.2}
\]
where
\[
 Q_2=\exp^{\circ}(-\mathbf1\mathbf1^\top+Q_1),
 \qquad Q_3:=\mathbb E[H_3H_3^\top]
 =\exp^{\circ}(-\mathbf1\mathbf1^\top+Q_2). \tag{6.3}
\]
The identity behind (6.1)--(6.3) is, for centered jointly Gaussian \((X,Y)\) with unit variances and covariance \(q\),
\[
 \mathbb E[(\sin X+\cos X)(\sin Y+\cos Y)]=e^{-1+q}. \tag{6.4}
\]

The three matrices \(Q_1,Q_2,Q_3\) are strictly positive definite. Indeed,
\[
 (Q_1)_{ab}=\exp\{-\|x_a-x_b\|^2/(2d)\}.
\]
For distinct \(x_a\), strict positive definiteness follows directly from the Fourier representation
\[
 \sum_{a,b}v_av_b e^{-\|x_a-x_b\|^2/(2d)}
 =c_d\int_{\mathbb R^d}e^{-d\|\xi\|^2/2}
 \left|\sum_av_ae^{i\xi\cdot x_a}\right|^2d\xi. \tag{6.5}
\]
If the integral vanishes, the exponential polynomial is zero on an open set, hence everywhere; restricting to a line whose projections of the finitely many distinct points are distinct gives a Vandermonde system and \(v=0\). If \(Q\) is strictly positive definite, then
\[
 e^{-1}\exp^{\circ}(Q)=e^{-1}\sum_{m\ge0}\frac{Q^{\circ m}}{m!} \tag{6.6}
\]
is strictly positive definite: every Schur power is positive semidefinite and the \(m=1\) summand is positive definite. Applying this twice proves the claim.

We next compute both reused adjoints, including their response terms. Put
\[
 g(T)=\sum_cy_c\phi(T_c),\qquad d_a^3=g(T)\phi'(T_a),\qquad G^3_{ab}=\mathbb E[d_a^3d_b^3]. \tag{6.7}
\]
The first adjoint rule (2.5) gives
\[
 p_a^2=\zeta_a^2+\sum_cM^3_{ac}\phi(S_c),
 \qquad \zeta^2\sim N(0,G^3),\quad \zeta^2\perp S, \tag{6.8}
\]
where
\[
 M^3_{ac}=y_cQ_{3,ac}-\delta_{ac}(Q_3y)_a. \tag{6.9}
\]
To verify (6.9), differentiate rather than guess:
\[
 \frac{\partial d_a^3}{\partial T_c}
 =y_c\phi'(T_c)\phi'(T_a)+\delta_{ac}g(T)\phi''(T_a). \tag{6.10}
\]
Here \(\phi''=-\phi\), \(\mathbb E[\phi'(T_c)\phi'(T_a)]=Q_{3,ac}\), and \(\mathbb E[g(T)\phi''(T_a)]=-(Q_3y)_a\), proving (6.9).

Set
\[
 d_a^2=\phi'(S_a)p_a^2,\qquad G^2_{ab}=\mathbb E[d_a^2d_b^2]. \tag{6.11}
\]
The second adjoint is
\[
 p_a^1=\zeta_a^1+\sum_cM^2_{ac}\phi(U_c),
 \qquad \zeta^1\sim N(0,G^2),\quad \zeta^1\perp U, \tag{6.12}
\]
with
\[
 M^2_{ac}=Q_{2,ac}M^3_{ac}-\delta_{ac}\sum_kQ_{2,ak}M^3_{ak}. \tag{6.13}
\]
Indeed, differentiating \(d_a^2=\phi'(S_a)(\zeta_a^2+\sum_kM^3_{ak}\phi(S_k))\) with respect to \(S_c\) and taking expectations yields exactly (6.13). Finally put
\[
 q_a^1=\phi'(U_a)p_a^1,\qquad G^1_{ab}=\mathbb E[q_a^1q_b^1]. \tag{6.14}
\]

Each of \(G^3,G^2,G^1\) is strictly positive definite. For \(G^3\), if \(v^\top d^3=0\) almost surely, the full-support Gaussian law of \(T\) and analyticity imply
\[
 \left(\sum_cy_c\phi(t_c)\right)\left(\sum_av_a\phi'(t_a)\right)=0
 \quad\hbox{for every }t\in\mathbb R^p. \tag{6.15}
\]
The first analytic factor is not identically zero. The ring of real-analytic functions on the connected set \(\mathbb R^p\) has no zero divisors, so the second factor is identically zero. Varying one coordinate at a time, and using that \(\phi'\) is nonconstant, gives \(v=0\). Given \(S\), the conditional variance of \(\sum_av_ad_a^2\) is
\[
 (v\odot\phi'(S))^\top G^3(v\odot\phi'(S)). \tag{6.16}
\]
The zeros of \(\phi'\) are discrete and \(S\) has a density, so (6.16) is positive almost surely for \(v\ne0\). This proves \(G^2>0\); the identical conditional-variance argument using (6.12) proves \(G^1>0\).

Consequently the three matrices
\[
 L_1=R\circ G^1,\qquad L_2=Q_1\circ G^2,\qquad L_3=Q_2\circ G^3 \tag{6.17}
\]
are strictly positive definite. For \(L_2,L_3\) this is the strict Schur product theorem. For \(L_1\), write \(R_{ab}=r_a\cdot r_b\). If \(v^\top(R\circ G^1)v=0\), then for every coordinate \(m\), \((v\odot r_{\cdot m})^\top G^1(v\odot r_{\cdot m})=0\). Thus \(v_ar_{am}=0\) for every \(a,m\). Since \(R_{aa}=1\), \(v=0\).

## 7. Small-time feature motion, active blocks, and a moving kernel

All expansions below are in the \(L^2\) spaces of the action state, uniformly over the finite sample index. They follow from the integral equations and the uniform integrability established in Sections 4--5; thus they are right-hand expansions of the already constructed width-first continuous flow, not finite-width Taylor expansions.

At time zero, \(C=0\), \(f=0\), and \(e=-y\). The equations first give
\[
\begin{aligned}
 C(t)&=\gamma t\,g+O_{L^2}(t^2),\\
 D_3^a(t)&=\gamma t\,d_a^3+o_{L^2}(t),
 &P_2^a(t)&=\gamma t\,p_a^2+o_{L^2}(t),\\
 D_2^a(t)&=\gamma t\,d_a^2+o_{L^2}(t),
 &P_1^a(t)&=\gamma t\,p_a^1+o_{L^2}(t). \tag{7.1}
\end{aligned}
\]
Define
\[
\begin{aligned}
 v_a^1={}&\sum_by_bR_{ab}q_b^1,\\
 v_a^2={}&\sum_by_bQ_{1,ab}d_b^2+B_0[\phi'(U_a)v_a^1],\\
 v_a^3={}&\sum_by_bQ_{2,ab}d_b^3+A_0[\phi'(S_a)v_a^2]. \tag{7.2}
\end{aligned}
\]
Differentiating the exact identities \(S=BH_1\), \(T=AH_2\), and using (1.1), yields
\[
 \dot U^a(t)=\gamma^2t v_a^1+o_{L^2}(t),\quad
 \dot S^a(t)=\gamma^2t v_a^2+o_{L^2}(t),\quad
 \dot T^a(t)=\gamma^2t v_a^3+o_{L^2}(t). \tag{7.3}
\]
For example, the first term in \(\dot S^a\) is \(\gamma^2t\sum_by_bQ_{1,ab}d_b^2\), from \(\dot B H_1^a\), and the second is \(\gamma^2tB_0[\phi'(U_a)v_a^1]\), from \(B\dot H_1^a\). This proves the middle identity; the last is identical with \(A,H_2,D_3\). Integration gives
\[
 Z^a(t)-Z^a(0)=\tfrac12\gamma^2t^2v_a^\ell+o_{L^2}(t^2),
 \quad (Z^a,\ell)=(U^a,1),(S^a,2),(T^a,3). \tag{7.4}
\]

Put \(E_\ell=y^\top L_\ell y>0\). The exact adjoint identities in the GNS state give
\[
\begin{aligned}
 \sum_ay_a\mathbb E[q_a^1v_a^1]&=E_1,\\
 \sum_ay_a\mathbb E[d_a^2v_a^2]&=E_2+E_1,\\
 \sum_ay_a\mathbb E[d_a^3v_a^3]&=E_3+E_2+E_1. \tag{7.5}
\end{aligned}
\]
For clarity, the extra term in the second line is
\[
 \sum_ay_a\mathbb E\{d_a^2B_0[\phi'(U_a)v_a^1]\}
 =\sum_ay_a\mathbb E\{(B_0^\top d_a^2)\phi'(U_a)v_a^1\}=E_1, \tag{7.6}
\]
and the third line follows in the same way. Hence none of the three vectors \((v_a^\ell)_{a\le p}\) is zero in \(L^2\). Equations (7.3)--(7.4) prove, for all sufficiently small \(T>0\), finite positive integrated squared velocity and nonzero mean-square displacement in every hidden layer.

The four kernel blocks have the expansions
\[
\begin{aligned}
 K^A(t)&=\gamma^2t^2L_3+o(t^2),\\
 K^B(t)&=\gamma^2t^2L_2+o(t^2),\\
 K^U(t)&=\gamma^2t^2L_1+o(t^2),\\
 K^C(t)&=Q_3+O(t^2). \tag{7.7}
\end{aligned}
\]
The remainders are entrywise. Thus every integrated block is strictly positive definite: for the first three this follows from (6.17), and for the readout block from \(Q_3>0\).

There is no cancellation hiding the kernel's motion. Since \(H_3^a(t)=\phi(T_a)+\frac12\gamma^2t^2\phi'(T_a)v_a^3+o_{L^2}(t^2)\), (7.5) gives
\[
 y^\top K^C(t)y=y^\top Q_3y+\gamma^2t^2(E_1+E_2+E_3)+o(t^2). \tag{7.8}
\]
Adding the other three blocks in (7.7),
\[
 y^\top K(t)y=y^\top Q_3y+2\gamma^2t^2(E_1+E_2+E_3)+o(t^2). \tag{7.9}
\]
The coefficient is strictly positive, so \(K(t)\ne K(0)\) for every sufficiently small positive \(t\).

## 8. Hidden variances, surviving nonlinearity, and decreasing loss

At zero, each scalar marginal \(U^a,S^a,T^a\) is \(N(0,1)\). The path-law \(W_2\) convergence and continuity of the limiting paths imply that their variances remain finite and at least \(1/2\) after reducing \(T_*\) if necessary.

For a probability law \(\mu\) of variance at least \(1/2\), define
\[
 \mathcal N(\mu)=\inf_{r,s\in\mathbb R}\int|\phi(z)-rz-s|^2d\mu(z). \tag{8.1}
\]
Writing this as the squared distance from \(\phi\) to \(\operatorname{span}\{1,z\}\), the normal equations give
\[
 \mathcal N(\mu)=\mathbb E\phi(Z)^2-b^\top M^{-1}b,
 \quad M=\begin{pmatrix}\mathbb EZ^2&\mathbb EZ\\\mathbb EZ&1\end{pmatrix},
 \quad b=\binom{\mathbb EZ\phi(Z)}{\mathbb E\phi(Z)}. \tag{8.2}
\]
The determinant of \(M\) is \(\operatorname{Var}Z\ge1/2\). Because \(\phi\) is bounded and Lipschitz, every entry in (8.2) is continuous under \(W_2\) convergence. For \(Z\sim N(0,1)\), \(\mathcal N(\mu)>0\): equality would make the analytic non-affine function \(\sin z+\cos z\) affine on a full-support measure and hence everywhere. Therefore, after reducing \(T_*\) again, (8.1) is bounded below by a positive constant for every sample and all three hidden layers. Its time integral is positive.

Finally \(f(0)=0\), hence \(e(0)=-y\), and (1.3), (6.3) give
\[
 \left.\frac d{dt}\mathcal L(t)\right|_{0+}=-\gamma^2y^\top Q_3y<0. \tag{8.3}
\]
Thus \(f(0)\ne y\) and \(\mathcal L(T)<\mathcal L(0)\) for every sufficiently small \(T>0\). Equations (3.7), (5.5), and (5.8) give full-sequence joint convergence in probability; (5.6) and uniform integrability give the three \(W_2\) path laws and pass all velocities and kernels; Sections 6--8 give strict nondegeneracy, feature motion, four active blocks, surviving nonlinearity, a moving kernel, and strict loss decrease. Taking \(T_*\) to be the minimum of the finitely many positive times chosen above completes the proof. \(\square\)
