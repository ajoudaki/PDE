Message Type: FINAL_ANSWER
Task name: /root
Sender: /root/resnet_matrix_route
Payload:
The functional-analytic argument can be repaired for bounded activations such as \(\tanh\), but the earlier claim of local Lipschitzness in bare \(L^2\) was false. The correct phase space must control both row and column \(L^2\) norms uniformly.

## 1. Correct kernel space

Let \(U=(0,1)\). For a kernel \(k(u,v)\), define
\[
r(k)=\operatorname*{ess\,sup}_{u\in U}\|k(u,\cdot)\|_{L^2_v},
\qquad
c(k)=\operatorname*{ess\,sup}_{v\in U}\|k(\cdot,v)\|_{L^2_u}.
\]
Set
\[
\mathcal K
=L^\infty_uL^2_v\cap L^\infty_vL^2_u,
\qquad
\|k\|_{\mathcal K}=r(k)+c(k),
\]
and, including depth,
\[
\mathbb K
=L^2_sL^\infty_uL^2_v
 \cap L^2_sL^\infty_vL^2_u,
\]
\[
\|w\|_{\mathbb K}^2
=\int_0^1\big(r(w(s))^2+c(w(s))^2\big)\,ds.
\tag{1}
\]
This is a Banach space. It embeds continuously into
\[
\mathbb H=L^2((0,1)^3_{s,u,v}).
\]

The useful operator estimates are
\[
\|T_kx\|_\infty\le r(k)\|x\|_2,
\qquad
\|T_k^*x\|_\infty\le c(k)\|x\|_2,
\tag{2}
\]
and
\[
\|T_k\|_{2\to2}\le \|k\|_{L^2(U^2)}
\le \min\{r(k),c(k)\}.
\tag{3}
\]

## 2. Why bare \(L^2\) fails

In the adjoint and gradient one encounters
\[
R=P\,\phi'(Z),\qquad Z=T_wX.
\]
If only \(P,Z\in L^2\), then
\[
P\big(\phi'(Z)-\phi'(\widetilde Z)\big)
\]
need only lie in \(L^1\), not \(L^2\).

This is a genuine failure of local Lipschitzness. Take a fixed unbounded
\[
P(u)=u^{-1/4}\in L^2(0,1),
\]
let \(E_\varepsilon=(0,\varepsilon)\), and set
\[
Z_\varepsilon=a\,1_{E_\varepsilon},\qquad Z_0=0,
\]
where \(\phi'(a)\ne\phi'(0)\). Then
\[
\|Z_\varepsilon-Z_0\|_2=|a|\varepsilon^{1/2},
\]
whereas
\[
\left\|
P\big(\phi'(Z_\varepsilon)-\phi'(0)\big)
\right\|_2
=
|\phi'(a)-\phi'(0)|\sqrt2\,\varepsilon^{1/4}.
\]
The ratio diverges like \(\varepsilon^{-1/4}\). Thus the graphon training vector field is not locally Lipschitz on bare \(L^2\) balls. The earlier \(L^2\)-Picard argument and its unqualified uniqueness claim were invalid.

## 3. Local well-posedness in \(\mathbb K\)

Consider
\[
\partial_sX_a=\phi(T_wX_a),\qquad X_a(0)=x_0^a,
\tag{4}
\]
\[
-\partial_sP_a=T_w^*R_a,\qquad
R_a=P_a\phi'(T_wX_a),\qquad P_a(1)=c,
\tag{5}
\]
and
\[
\partial_tw
=-\sum_{a=1}^Mq_aR_a\otimes X_a.
\tag{6}
\]

Assume

- \(\phi\in C_b^2(\mathbb R)\);
- \(x_0^a,c\in L^\infty(U)\);
- \(\mathcal R\in C^2(\mathbb R^M)\);
- \(w_0\in\mathbb K\).

Then:

1. For each \(w\in\mathbb K\), (4) has a unique
   \[
   X_a\in W^{1,1}_sL^\infty_u.
   \]

2. Equation (5) has a unique
   \[
   P_a\in W^{1,1}_sL^\infty_u.
   \]

3. The map
   \[
   w\longmapsto
   -\sum_a q_aR_a\otimes X_a
   \]
   is locally Lipschitz from \(\mathbb K\) to \(\mathbb K\).

The key outer-product estimates are
\[
r(R\otimes X)\le \|R\|_\infty\|X\|_2,
\qquad
c(R\otimes X)\le \|X\|_\infty\|R\|_2.
\tag{7}
\]
The mixed norm also gives \(Z=T_wX\in L^\infty\), so
\[
\|P(\phi'(Z)-\phi'(\widetilde Z))\|_2
\le
\|P\|_\infty\|\phi''\|_\infty
\|Z-\widetilde Z\|_2.
\tag{8}
\]
This is precisely the estimate unavailable in bare \(L^2\).

Picard–Lindelöf in \(\mathbb K\) therefore gives a unique maximal solution
\[
w\in C^1([0,T_*);\mathbb K).
\]

## 4. Energy identity

Let
\[
F(w)=\mathcal R(f_1(w),\dots,f_M(w)).
\]
On \(\mathbb K\), the forward solution map is Fréchet differentiable. Its derivative is represented in the \(\mathbb H\) pairing by
\[
\nabla_{\mathbb H}F(w)
=\sum_aq_aR_a\otimes X_a.
\tag{9}
\]
Thus (6) is the \(L^2(ds\,du\,dv)\) gradient flow, even though it is solved in the stronger space \(\mathbb K\). Along every local solution,
\[
\frac d{dt}F(w(t))
=-\|\partial_tw(t)\|_{\mathbb H}^2.
\tag{10}
\]
If \(F\ge F_*\), then
\[
\int_0^T\|\partial_tw(t)\|_{\mathbb H}^2dt
\le F(w_0)-F_*,
\tag{11}
\]
and
\[
\|w(t)-w_0\|_{\mathbb H}
\le\sqrt{t\,[F(w_0)-F_*]}.
\tag{12}
\]

Energy alone does not control \(\mathbb K\): kernels
\[
k_N(u,v)=\sqrt N\,1_{\{u<1/N\}}
\]
have bounded \(L^2(U^2)\) norm but \(r(k_N)=\sqrt N\). A separate mixed-norm estimate is therefore necessary.

## 5. Global existence for bounded \(\phi\)

For this architecture, such an estimate is available.

First,
\[
\sup_{s,t}\|X_a(s,t)\|_\infty
\le \|x_0^a\|_\infty+\|\phi\|_\infty
=:C_X,
\tag{13}
\]
independently of \(w\). Hence all outputs remain in a fixed compact set, so
\[
\sup_t|q_a(t)|\le C_q.
\tag{14}
\]

Energy gives, on every finite interval,
\[
\sup_{t\le T}\|w(t)\|_{\mathbb H}\le C_T.
\]
Consequently, the \(L^2\) adjoint satisfies
\[
\sup_{s,t\le T}\|P_a(s,t)\|_2
\le
\|c\|_2
\exp\!\left(
 \|\phi'\|_\infty\|w(t)\|_{\mathbb H}
\right)
\le C_T.
\tag{15}
\]

Let
\[
C_w(t)=
\left(\int_0^1c(w(s,t))^2ds\right)^{1/2},
\qquad
R_w(t)=
\left(\int_0^1r(w(s,t))^2ds\right)^{1/2}.
\]
From the adjoint equation and (2),
\[
\|P_a\|_{L^\infty_{s,u}}
\le
\|c\|_\infty
+\|\phi'\|_\infty
\int_0^1c(w(s,t))\|P_a(s,t)\|_2ds
\le \|c\|_\infty+C_TC_w(t).
\tag{16}
\]

Using (7), (13)–(16),
\[
c(\partial_tw(s,t))
\le
\sum_a|q_a|
\|X_a(s,t)\|_\infty\|R_a(s,t)\|_2
\le C_T.
\]
Therefore
\[
C_w(t)\le C_w(0)+C_Tt.
\tag{17}
\]

Similarly,
\[
r(\partial_tw(s,t))
\le
\sum_a|q_a|
\|R_a(s,t)\|_\infty\|X_a(s,t)\|_2
\le C_T\bigl(1+C_w(t)\bigr),
\]
and hence
\[
R_w(t)
\le R_w(0)+C_T(t+t^2).
\tag{18}
\]

Thus \(\|w(t)\|_{\mathbb K}\) cannot blow up in finite time. Since the vector field is Lipschitz on bounded \(\mathbb K\)-balls, the maximal time is \(T_*=\infty\).

Therefore the corrected result is:

> For \(\phi\in C_b^2\), bounded initial features/readout, \(w_0\in\mathbb K\), and a lower-bounded \(C^2\) loss, the graphon forward–adjoint–training system has a unique global solution \(w\in C^1([0,\infty);\mathbb K)\), and it satisfies the exact \(L^2\) energy identity (10).

This global argument does not automatically extend to ReLU or other unbounded activations.

## 6. Consequence for the width proof

The discrete analogue is
\[
\|A\|_{\mathcal K_n}
=
\max\left\{
 \max_i\left(\frac1n\sum_jA_{ij}^2\right)^{1/2},
 \max_j\left(\frac1n\sum_iA_{ij}^2\right)^{1/2}
\right\}.
\tag{19}
\]
Gaussian matrices satisfy
\[
\frac1L\sum_{\ell=1}^L
\|G_\ell\|_{\mathcal K_n}^2=O_{\mathbb P}(1)
\]
uniformly in \(L\), providing uniform \(p_\ell^\infty\) bounds. Their effect on \(L^2\) state errors is nevertheless small because
\[
\left\|G_\ell/n\right\|_{2\to2}
=O_{\mathbb P}(n^{-1/2}).
\]

The gate estimate needed in the convergence Gronwall is now valid:
\[
\|p\odot[\phi'(z)-\phi'(\bar z)]\|_{2,n}
\le
\|p\|_{\infty,n}\|\phi''\|_\infty
\|z-\bar z\|_{2,n}.
\tag{20}
\]

So the previous width theorem is repairable, but its proof must explicitly carry the mixed row/column norm. A bare normalized-Frobenius/\(L^2\) argument is insufficient.
