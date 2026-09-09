# Stopped independent-cavity trace approximation for simultaneous raw GD

Author derivation, 2026-09-06. This is a bounded extension to exact raw
gradient descent and its raw affine, recomputed-hidden interpolation.
It is not an audit of the gradient-flow candidate.

## Provenance and scope

The sole mathematical source read was the entire 864-line, 37,052-byte file
`/tmp/l2-two-sample-proof-0ywjpp/CAVITY_STOPPED_TRACE_LINEARIZATION_TEST.md`,
with SHA-256

`192a22168de5c560c3d8046f297e813dda1ca037065caa323a90eb9dd7a6bedb`.

That file was treated as an unverified candidate. The identities and
estimates used here are derived below; none of its theorem assertions is
an assumption. No other mathematical/project/history/review file was
consulted, and no experiments, external concentration results, or
subagents were used.

Established below: a finite-width stopped node theorem, an extension
uniform over every included raw interpolation cell, and vanishing errors
in the corresponding first-layer root equation. The response uses exact
ordered products of simultaneous-update Jacobians, with sources at the
old nodes. Conditioning precedes restriction to the actual stop. All
residual variations and both differentiated factors of trained outer
products are retained. Only a subpolynomial bound on the response trace
is obtained. Stop removal, a width-uniform trace estimate, and a limiting
closed law remain open here.

The proof constructs the response at the independent cavity, bounds all
its needed coordinate kernels by elementary Gaussian calculations, and
estimates the nonlinear defect of that response. A discrete stability
inequality transfers it to the actual bulk. Affinity of the raw
parameters, together with explicit cell moduli for the recomputed
fields, then gives the whole-cell result.

## 1. Model, exact algorithm, and interpolation conventions

Fix two deterministic samples with
\[
 \|x_a\|^2=d,\qquad x_1^Tx_2/d=\rho\in(-1,1),\qquad
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
 y_1=1,\quad y_2=-1.
 \tag{1}
\]
Here \(d\geq2\) may depend on \(n\). The result holds for every fixed
\(\rho\) in this interval; constants may depend on \(\rho\), but not on
\(d\). All vector norms are ordinary Euclidean or maximum norms as
indicated, and matrix norms are ordinary Frobenius or spectral norms.
Operator norms between product spaces use the sum-of-squares Euclidean
norm, with Frobenius norm on a matrix block. No normalized vector norm
is implicit in the notation.

There are two hidden layers of width \(n\). Use the canonical fields
\[
\begin{aligned}
 z^{(1)}_a&=W^{(1)}x_a,& h^{(1)}_a&=\phi_1(z^{(1)}_a),\\
 z^{(2)}_a&=A h^{(1)}_a,& h^{(2)}_a&=\phi_2(z^{(2)}_a),\\
 f_a&=n^{-1}w^Th^{(2)}_a,& c_a&=-2(f_a-y_a),\\
 \delta^{(2)}_a&=w\odot\phi_2'(z^{(2)}_a),&
 q^{(1)}_a&=A^T\delta^{(2)}_a.
\end{aligned}                                                    \tag{2}
\]
Throughout, \(\delta_a\) abbreviates \(\delta^{(2)}_a\) and \(q_a\)
abbreviates \(q^{(1)}_a\); neither abbreviation includes an extra
\(\phi_1'\) gate. Take \(\phi_2=\arctan\), and either
\(\phi_1=\arctan\) or
\(\phi_1(s)=\int_0^s p(u)\,du\), where \(p\) is a fixed, smooth,
compactly supported function not identically zero. Both activations
and their first three derivatives are bounded. No sign condition on
\(p\) is needed. Put \(B_1=\|\phi_1\|_\infty\).

Initialization has mutually independent entries and layers:
\[
 W^{(1)}_{il,0}\sim N(0,1/d),\qquad
 A_{li,0}\sim N(0,1/n),\qquad w_{l,0}\sim N(0,n^{-2}).
 \tag{3}
\]
Fix \(T>0\), \(K>0\), and a deterministic distinguished index \(j\).
Set \(\eta=n^{-2}\), \(t_k=k\eta\), and \(N=\lceil T/\eta\rceil\).
The extra endpoint satisfies \(N\eta\leq T+1\).
For \(0\leq k<N\), the algorithm is exactly
\[
\begin{aligned}
 W^{(1)}_{k+1}&=W^{(1)}_k+
   {\eta\over d}\sum_a c_{a,k}
       [\phi_1'(z^{(1)}_{a,k})\odot q_{a,k}]x_a^T,\\
 A_{k+1}&=A_k+{\eta\over n}\sum_a
              c_{a,k}\delta_{a,k}(h^{(1)}_{a,k})^T,\\
 w_{k+1}&=w_k+\eta\sum_a c_{a,k}h^{(2)}_{a,k}.
\end{aligned}                                                    \tag{4}
\]
Every right-hand side is evaluated at the old node \(k\), including
all residuals and hidden fields. These are simultaneous updates.

For \(t=t_k+\theta\eta\), \(0\leq\theta\leq1\), interpolate each
raw parameter by
\[
 (W^{(1)},A,w)(t)=(1-\theta)(W^{(1)},A,w)_k
                           +\theta(W^{(1)},A,w)_{k+1}.     \tag{5}
\]
All quantities in (2) at time \(t\) are recomputed from these raw
parameters. In particular hidden activations, \(z^{(2)}\), \(c\),
\(\delta^{(2)}\), and \(q^{(1)}\) are not interpolated between their
node values. The first preactivations are affine because
\(z^{(1)}=W^{(1)}x\).

Writing \(z_i=(z^{(1)}_{1,i},z^{(1)}_{2,i})^T\), multiplication of
the first line of (4) by the two inputs verifies
\[
 z_{i,k+1}=z_{i,k}+\eta C
       (c_{a,k}\phi_1'(z^{(1)}_{a,i,k})q_{a,i,k})_{a=1,2}.
 \tag{6}
\]
This includes \(i=j\). The distinguished root is always this actual
root, with \(z_{j,0}=\xi\); it is never replaced by an independent
root trajectory.

## 2. Independent cavity and node stops, including overshoot

Let \(I=\{1,\ldots,n\}\setminus\{j\}\), \(B=A_{:,I}\), and
\[
 g=A_{:,j,0}\sim N(0,I_n/n),\qquad
 \xi=(z^{(1)}_{1,j,0},z^{(1)}_{2,j,0})\sim N(0,C),\qquad
 R_n=K\sqrt{\log n}.
 \tag{7}
\]
Let \(\mathcal F_{-j}\) contain all initialization except \(g\),
including \(\xi\). Then \(g\) is independent of \(\mathcal F_{-j}\).

The unfrozen cavity deletes column \(j\), freezes row \(j\) of
\(W^{(1)}\), and applies (4) to the remaining variables, retaining
every denominator \(n\). Its upper preactivation is
\(B\phi_1(z^{(1)}_{a,I})\). Let \(s_c\) be its first node in
\(\{0,\ldots,N\}\) with
\(\max_{a,i\in I}|q_{a,i}|\geq R_n\), or \(N\) if no such node
exists. Freeze cavity parameters at node \(s_c\) and interpolate
these frozen-extended node parameters by (5). Hats always refer to
this extension, with fields recomputed from its parameters.

Let \(s_f\) be the corresponding first node of the full actual
algorithm with \(\max_{a,i}|q_{a,i}|\geq R_n\), or \(N\) if none
exists. In particular \(s_f=0\) if an initial actual field exceeds
the threshold. Set
\[
 s=\min(s_c,s_f),\qquad \tau=\min(T,s\eta),\qquad
 \mathcal C_n=\{\|B_0\|_{\rm op}\leq8,\ \|w_0\|_\infty\leq1,
                \ \max_{a,i\in I}|\widehat q_{a,i,0}|\leq R_n\}.
 \tag{8}
\]
The stopping nodes themselves are included in the node theorem.
Every incoming cell \([t_k,t_{k+1}]\), \(k<s\), is included, with
the last cell cut at \(T\) if necessary. These conventions permit
an interior crossing before the stopping node. Section 3 proves that
the overshoot throughout an incoming cell is at most
\(C_T\eta\sqrt n=C_Tn^{-3/2}\). Restricting the result to a first
continuous crossing is therefore also allowed, without changing any
kernel or probability estimate. No equality between a node stop and
a continuous stop is asserted.

Only \(\mathcal C_n\) is imposed when conditioning on
\(\mathcal F_{-j}\). The actual stop is used later in deterministic
comparison. It is never inserted into a matrix to which a Gaussian
law is applied.

## 3. Global deterministic GD bounds and exact column restoration

All bounds in this section hold on
\(\mathcal C_n\cap\{\|g\|\leq2\}\), without an actual stopping
assumption. Constants denoted by \(C_T\) can change from line to
line and depend only on \(T,\rho\), and fixed activation bounds.
They do not depend on \(d,n,K\). The same bounds hold for the cavity.

Put \(M_k=\|w_k\|_\infty\). Boundedness of \(\phi_2\) gives
\[
 |f_{a,k}|\leq\|\phi_2\|_\infty M_k,\qquad
 \sum_a|c_{a,k}|\leq C(1+M_k),\qquad
 M_{k+1}\leq M_k+C\eta(1+M_k).
 \tag{9}
\]
Iterating \(1+M_{k+1}\leq(1+C\eta)(1+M_k)\) bounds \(M_k\)
and the residuals by constants through \(N\). Since
\(\|\delta_{a,k}\|\leq C_T\sqrt n\) and
\(\|h^{(1)}_{a,k}\|\leq B_1\sqrt n\), (4) gives
\[
 \|A_{k+1}-A_k\|_F\leq C_T\eta.
\]
Also \(\|A_0\|_{\rm op}\leq\|B_0\|_{\rm op}+\|g\|\leq10\).
Summing the last bound and using affinity in each cell yields
\[
 \sum_a|c_a(t)|+\|w(t)\|_\infty+\|A(t)\|_{\rm op}\leq C_T,
 \qquad \|\delta_a(t)\|+\|q_a(t)\|\leq C_T\sqrt n.
 \tag{10}
\]
The bound on recomputed \(c_a(t)\) uses bounded \(\phi_2\) again.
Thus no gradient-flow energy identity or GD loss monotonicity is
needed for these finite-horizon bounds.

For a full or cavity cell, a dot denotes differentiation along its
raw affine segment, away from nodes. Equations (4), (6), and (10)
give
\[
 \|\dot z^{(1)}_a\|\leq C_T\sqrt n,\qquad
 \|\dot A\|_F+\|\dot w\|_\infty\leq C_T.
\]
Differentiating recomputed fields on this segment gives exactly
\[
\begin{aligned}
 \dot z^{(2)}_a&=\dot A h^{(1)}_a
                  +A[\phi_1'(z^{(1)}_a)\odot\dot z^{(1)}_a],\\
 \dot\delta_a&=\dot w\odot\phi_2'(z^{(2)}_a)
                +w\odot\phi_2''(z^{(2)}_a)\odot\dot z^{(2)}_a,\\
 \dot q_a&=\dot A^T\delta_a+A^T\dot\delta_a.
\end{aligned}
\]
Consequently, uniformly in all cells,
\[
 \|\dot z^{(2)}_a\|+\|\dot\delta_a\|+\|\dot q_a\|
       \leq C_T\sqrt n,\qquad |\dot c_a|\leq C_T.
 \tag{11}
\]
The last estimate follows from differentiating
\(f_a=n^{-1}w^Th^{(2)}_a\); each inner product is \(O(n)\).
For \(v=z^{(1)}_a,z^{(2)}_a,\delta_a,q_a,w\), in particular,
\[
 \sup_{t\in[t_k,t_{k+1}]}\|v(t)-v_k\|
           \leq C_T\eta\sqrt n.                         \tag{12}
\]
If the old node is before its node stop, (6) also gives
\(\|\dot z^{(1)}_a\|_\infty\leq C_TR_n\).
The stopped cavity therefore satisfies everywhere
\[
 \max_{a,i\in I}|\widehat q_{a,i}(t)|
       \leq R_n+C_T\eta\sqrt n.                         \tag{13}
\]
Its initial value is bounded by (8), and all later incoming cells
start below the threshold; freezing preserves the endpoint value.
Likewise the actual maximum on every cell \(k<s\) is at most the
right-hand side of (13). At \(s=0\) no positive cell is claimed.

The complete trained distinguished column is, exactly,
\[
\begin{aligned}
 A_{:,j,k}&=g+\ell_k,&
 \ell_k&={\eta\over n}\sum_{r<k}\sum_b
              c_{b,r}\delta_{b,r}h^{(1)}_{b,j,r},\\
 \ell(t)&=\ell_k+{\theta\eta\over n}\sum_b
              c_{b,k}\delta_{b,k}h^{(1)}_{b,j,k},&
 A_{:,j}(t)&=g+\ell(t).
\end{aligned}                                                    \tag{14}
\]
Here and below a sum over \(r<k\) starts at zero. In particular
\(\|\ell(t)\|\leq C_T/\sqrt n\). Let
\[
 h_a(t)=h^{(1)}_{a,j}(t),\quad
 e_a(t)=(g+\ell(t))h_a(t),\quad
 \delta_a^0(t)=w(t)\odot\phi_2'(B(t)h^{(1)}_{a,I}(t)).
\]
Then \(z^{(2)}_a=B h^{(1)}_{a,I}+e_a\), and the one-variable
fundamental theorem of calculus, coordinate by coordinate, gives
\[
\begin{aligned}
 \delta_a&=\delta_a^0+D_a^{\rm dir} e_a,\\
 D_a^{\rm dir}(t)&=\operatorname{diag}\left(
 w_l(t)\int_0^1\phi_2''((B h^{(1)}_{a,I})_l(t)
                                +u e_{a,l}(t))\,du\right).
\end{aligned}                                                    \tag{15}
\]
It follows by expanding \((g+\ell)^T\delta_a\) that
\[
\begin{aligned}
 q_{a,j}(t)&=G_a(t)+M_a(t)+S_a(t)
                         +g^T(\delta_a^0(t)-\widehat\delta_a(t)),\\
 G_a(t)&=g^T\widehat\delta_a(t),\qquad
 M_a(t)=\ell(t)^T\delta_a(t),\\
 S_a(t)&=h_a(t)g^TD_a^{\rm dir}(t)(g+\ell(t)).
\end{aligned}                                                    \tag{16}
\]
This identity holds at nodes and inside raw cells. Equations
(10), (14), (15) give \(|M_a(t)|+|S_a(t)|\leq C_T\).

## 4. Independent cavity derivatives in ordinary coordinates

Use the Euclidean bulk coordinate
\[
 X=\left((C^{-1/2}z_i/\sqrt n)_{i\in I},\ B,\ w/\sqrt n\right)
       \in\mathbb R^{m_n},\qquad m_n=n^2+2n-2.            \tag{17}
\]
For a moving first row, its displacement lies in the span of
\(x_1,x_2\). If \(\Delta W_i^{(1)}=\sum_a b_a x_a^T\), then
\(\Delta z_i=dCb\) and
\(d\|\Delta W_i^{(1)}\|^2=d^2b^TCb
 =\Delta z_i^TC^{-1}\Delta z_i\).
The orthogonal part of the row is fixed by (4). Thus squared
Euclidean displacement in (17) is precisely
\((d/n)\|\Delta W^{(1)}_I\|_F^2+\|\Delta B\|_F^2
 +(1/n)\|\Delta w\|^2\), with all factors explicit.

For an independent argument \(E=(E_1,E_2)\in\mathbb R^{2n}\), put
\[
 f_a(X,E)={1\over n}w^T\phi_2(B\phi_1(z^{(1)}_{a,I})+\sqrt n E_a),
 \qquad F(X,E)=-\nabla_X\sum_a(f_a(X,E)-y_a)^2.            \tag{18}
\]
Hold \(E\) fixed in derivatives. Direct differentiation gives the
three blocks
\[
\begin{aligned}
 F_{u,i}&={1\over\sqrt n}C^{1/2}
                    (c_a\phi_1'(z^{(1)}_{a,i})q_{a,i})_a,\\
 F_B&={1\over n}\sum_a c_a\delta_a(h^{(1)}_{a,I})^T,
       \qquad
 F_v={1\over\sqrt n}\sum_a c_a h^{(2)}_a.
\end{aligned}                                                    \tag{19}
\]
Here \(q_I=B^T\delta\) and the upper input is the one in (18).
This verifies the exact identities
\[
 X_{k+1}=X_k+\eta F(X_k,e_k/\sqrt n),\qquad
 \widehat X_{k+1}=\widehat X_k+\eta F(\widehat X_k,0)
                         \quad(k<s_c).                  \tag{20}
\]
In particular there is no differentiation of the actual function
\(e_k\) with respect to the bulk when obtaining (20).

At any frozen-extended cavity state, node or interpolated, define
\[
\begin{aligned}
 H_a&=\phi_1(\widehat z^{(1)}_{a,I}),&
 P_a&=\operatorname{diag}\phi_1'(\widehat z^{(1)}_{a,I}),\\
 V_a&=\operatorname{diag}\phi_2'(\widehat z^{(2)}_a),&
 D_a&=\operatorname{diag}(\widehat w\odot\phi_2''(\widehat z^{(2)}_a)).
\end{aligned}                                                    \tag{21}
\]
For \(Y=(u,V,v)\in\mathbb R^{m_n}\), the displacement \(Y/\sqrt n\)
in \(X\) gives physical increments
\(\zeta_i=C^{1/2}u_i\), \(\Delta B=V/\sqrt n\), and
\(\Delta w=v\). The matrix block \(V\) is distinct from the gate
matrix \(V_a\). Define
\[
\begin{aligned}
 Z_aY&=V H_a/\sqrt n+\widehat B P_a\zeta_a,\\
 L_aY&=V_a v+D_aZ_aY,\\
 Q_aY&=V^T\widehat\delta_a/\sqrt n+\widehat B^TL_aY.
\end{aligned}                                                    \tag{22}
\]
Thus \(Z_a,L_a:\mathbb R^{m_n}\to\mathbb R^n\),
\(Q_a:\mathbb R^{m_n}\to\mathbb R^{n-1}\), and
\(L_a=n^{-1/2}D_X\delta_a(X,0)|_{\widehat X}\).

For a physical upper input \(e=(e_1,e_2)\), the corresponding first
variations are
\[
\begin{aligned}
 \lambda_a&=Z_aY+e_a,& d\delta_a&=L_aY+D_ae_a,\\
 dq_a&=Q_aY+\widehat B^TD_ae_a,&
 \chi_a&=-{2\over n}
       [v^T\phi_2(\widehat z^{(2)}_a)+\widehat\delta_a^T\lambda_a].
\end{aligned}                                                    \tag{23}
\]
Differentiating the three products in (19) now gives the complete
linear map \(\mathscr L(Y,e)=JY+\sum_b\mathcal B_b e_b\):
\[
\begin{aligned}
 (\mathscr L_u)_i
 &=C^{1/2}\big(
    \widehat c_a\phi_1''(\widehat z^{(1)}_{a,i})\widehat q_{a,i}\zeta_{a,i}
   +\widehat c_a\phi_1'(\widehat z^{(1)}_{a,i})dq_{a,i}
   +\chi_a\phi_1'(\widehat z^{(1)}_{a,i})\widehat q_{a,i}
                      \big)_{a=1,2},\\
 \mathscr L_V
 &={1\over\sqrt n}\sum_a
     [\chi_a\widehat\delta_aH_a^T
      +\widehat c_a d\delta_aH_a^T
      +\widehat c_a\widehat\delta_a(P_a\zeta_a)^T],\\
 \mathscr L_v
 &=\sum_a[\chi_a\phi_2(\widehat z^{(2)}_a)
                           +\widehat c_aV_a\lambda_a].
\end{aligned}                                                    \tag{24}
\]
More precisely,
\[
 \mathscr L(Y,e)=\left.{d\over d\epsilon}ight|_{0}
      \sqrt n F(\widehat X+\epsilon Y/\sqrt n,
                                      \epsilon e/\sqrt n),
 \quad J=D_XF(\widehat X,0),\quad
 \mathcal B_b=D_{E_b}F(\widehat X,0).                     \tag{25}
\]
For example the variation of \(c\) is \(\chi\), including its
\(e\)-part, so it contributes in all three blocks. The variation of
\(B^T\delta\) includes \(V^T\widehat\delta/\sqrt n\), and both
factors of \(\delta H^T\) vary. The trained cavity values
\(\widehat B,\widehat w,\widehat c\) appear everywhere. Thus (24)
does not discard residual or trained-rank terms.

The following bounds follow directly from (10), (13), and (21)--(24):
\[
 \|Z_a\|_{\rm op}+\|L_a\|_{\rm op}+\|Q_a\|_{\rm op}
           +\sum_b\|\mathcal B_b\|_{\rm op}\leq C_T,
 \qquad \|J\|_{\rm op}\leq C_T(1+R_n),                  \tag{26}
\]
provided \(C_T\eta\sqrt n\leq1\). Indeed
\(\|H_a\|,\|\widehat\delta_a\|,\|\widehat q_a\|\leq C_T\sqrt n\),
and \(|\chi_a|\leq C_T(\|Y\|+\|e\|)/\sqrt n\). These cancel
the displayed \(1/\sqrt n\) factors. A rank-one matrix has
Frobenius norm equal to the product of the vector norms. Only
\(\widehat c\phi_1''\widehat q\zeta\) uses the coordinate maximum
of \(\widehat q\). It is absent when \(Y=0\), explaining the
bound for \(\mathcal B_b\) without a factor \(R_n\).

We also need cell moduli, for which (11)--(12) imply
\[
 \|O(t)-O(t_k)\|_{\rm op}\leq C_T\eta\sqrt n,
 \quad O=Z_a,L_a,Q_a,D_a,\ \widehat B^TD_a,
 \quad t\in[t_k,t_{k+1}].                                \tag{27}
\]
For completeness, \(\|\Delta H_a\|\leq C_T\eta\sqrt n\),
\(\|\Delta P_a\|_{\rm op}\leq C_T\eta\sqrt n\), and
\(\|\Delta V_a\|_{\rm op}+\|\Delta D_a\|_{\rm op}
\leq C_T\eta\sqrt n\). The last inequality uses the bounded third
derivative of \(\phi_2\) and \(\|\Delta w\|_\infty\leq C_T\eta\).
Substitute these and \(\|\Delta B\|_F\leq C_T\eta\) into (22).
In \(Q_a\), \(\|\Delta\widehat\delta_a\|/\sqrt n\leq C_T\eta\).
These facts prove (27), including on a frozen cell, where the maps
are constant. This proof does not assume affine interpolation of a
hidden field.

## 5. Exact ordered products and statement of the approximation

Let \(J_k,\mathcal B_{b,k},L_{a,k}\) denote the cavity maps at node
\(k\), and set
\[
 A^c_k=I_{m_n}+\eta J_k,\qquad
 U(k,l)=A^c_{k-1}A^c_{k-2}\cdots A^c_l\quad(k>l),\qquad
 U(l,l)=I_{m_n}.
 \tag{28}
\]
The later factor is on the left. All these are derivatives evaluated
at the frozen cavity state, even after \(s_c\); after freezing they
are not asserted to be derivatives of the frozen transition map.
This is an independent extension of the kernels to the deterministic
index range. It contains no actual-stop indicator. From (26),
\[
 \|U(k,l)\|_{\rm op}
    \leq\prod_{r=l}^{k-1}(1+C_T\eta(1+R_n))
    \leq e^{C_T(1+R_n)(k-l)\eta}.                        \tag{29}
\]
No exponential of a summed Jacobian replaces (28).

At nodes define, for \(0\leq r<k\leq N\),
\[
\begin{aligned}
 K_{ab}(k,r)&=L_{a,k}U(k,r+1)\mathcal B_{b,r},&
 \kappa_{ab}(k,r)&={1\over n}\operatorname{Tr}K_{ab}(k,r),\\
 d_{a,k}&={1\over n}\operatorname{Tr}D_{a,k},&
 m_{ab}(k,r)&={\widehat c_{b,r}\over n}
                    \widehat\delta_{b,r}^T\widehat\delta_{a,k}.
\end{aligned}                                                    \tag{30}
\]
The trace is over an \(n\)-by-\(n\) matrix. In particular a source
from step \(r\) is inserted at node \(r+1\); its subsequent
propagation begins with \(U(k,r+1)\), not \(U(k,r)\).

Here are the interpolation kernels. Write \(t=t_k+\theta\eta\)
with \(0\leq k<N\), \(0\leq\theta<1\), and use \(k=N,\theta=0\)
at \(N\eta\). Let
\[
 \omega_r(t)=
 \begin{cases}\eta,&r<k,\\\theta\eta,&r=k<N,\end{cases}
 \qquad
 P(t,r)=
 \begin{cases}
 (I+\theta\eta J_k)U(k,r+1),&r<k,\ k<N,\\
 U(N,r+1),&k=N,\ r<N,\\
 I_{m_n},&r=k<N.
 \end{cases}                                                \tag{31}
\]
All sums over \(r\) at time \(t\) mean \(0\leq r<k\), plus
\(r=k\) if \(k<N\). A zero weight contributes nothing. Put
\[
\begin{aligned}
 K_{ab}(t,r)&=L_a(t)P(t,r)\mathcal B_{b,r},&
 \kappa_{ab}(t,r)&={1\over n}\operatorname{Tr}K_{ab}(t,r),\\
 d_a(t)&={1\over n}\operatorname{Tr}D_a(t),&
 m_{ab}(t,r)&={\widehat c_{b,r}\over n}
                     \widehat\delta_{b,r}^T\widehat\delta_a(t).
\end{aligned}                                                    \tag{32}
\]
At \(t=t_k\), the positive-weight terms agree with (30). Values
from the left also agree at a cell endpoint, since
\(A^c_kU(k,r+1)=U(k+1,r+1)\). No new-node residual or source is
used in the fractional step. Only the readback map \(L_a(t)\) and
the direct/readout coefficients use recomputed fields at the query.

**Theorem.** For every fixed \(p_*>0\), constants \(A_*>0\) and
\(n_0\) can be chosen depending on \(T,\rho,p_*\), the activations,
and, for \(n_0\), \(K\), so the following holds. Define
\[
 H_n=e^{A_*(1+R_n)},\qquad a_n=\sqrt{\log n/n},\qquad
 b_n=\eta\sqrt n=n^{-3/2},
\]
\[
 \varepsilon_n^{\rm node}=H_n^{20}a_n,\qquad
 \varepsilon_n^{\rm cell}=H_n^{30}(a_n+b_n).              \tag{33}
\]
Take \(n\geq\max(3,n_0)\) and
\(H_n^{40}(a_n+b_n)\leq1/2\). These conditions hold eventually
for fixed \(T,K,\rho,p_*\).
For almost every \(\mathcal F_{-j}\) initialization in \(\mathcal C_n\),
there is an event of conditional probability at least
\(1-n^{-p_*}-e^{-n/2}\) with the following simultaneous conclusions.

At every node \(0\leq k\leq s\),
\[
\begin{aligned}
 q_{a,j,k}
   &=G_{a,k}+M_{a,k}+S_{a,k}
       +\eta\sum_{r<k,b}\kappa_{ab}(k,r)h_{b,r}
       +e^{\rm node}_{a,k},\\
 q_{a,j,k}
   &=G_{a,k}+d_{a,k}h_{a,k}
       +\eta\sum_{r<k,b}[m_{ab}(k,r)+\kappa_{ab}(k,r)]h_{b,r}
       +\widetilde e^{\rm node}_{a,k},
\end{aligned}                                                    \tag{34}
\]
where each error is at most \(\varepsilon_n^{\rm node}\) in
absolute value. At every \(0\leq t\leq\tau\),
\[
\begin{aligned}
 q_{a,j}(t)
   &=G_a(t)+M_a(t)+S_a(t)
       +\sum_{r,b}\omega_r(t)\kappa_{ab}(t,r)h_{b,r}+\mathfrak e_a(t),\\
 q_{a,j}(t)
   &=G_a(t)+d_a(t)h_a(t)
       +\sum_{r,b}\omega_r(t)[m_{ab}(t,r)+\kappa_{ab}(t,r)]h_{b,r}
       +\widetilde{\mathfrak e}_a(t),
\end{aligned}                                                    \tag{35}
\]
where each scalar readback error is at most
\(\varepsilon_n^{\rm cell}\) uniformly in \(a,t\).

The process \(G_a(t)=g^T\widehat\delta_a(t)\), defined on the whole
deterministic interval \([0,N\eta]\), is conditionally centered
Gaussian with
\[
 \mathbb E[G_a(t)G_b(u)\mid\mathcal F_{-j}]
       ={1\over n}\widehat\delta_a(t)^T\widehat\delta_b(u).
 \tag{36}
\]
This statement is under the original conditional Gaussian measure,
not under its further restriction to the good event or to survival.
The coefficients \(d,m,\kappa\) are \(\mathcal F_{-j}\)-measurable.
Uniformly over their full deterministic ranges,
\[
 |d_a(t)|+|m_{ab}(t,r)|\leq C_T,\qquad
 |\kappa_{ab}(t,r)|\leq C_Te^{C_T(1+R_n)(T+1)}.
 \tag{37}
\]
Both errors in (33) are \(n^{-1/2+o(1)}\to0\). The distinct
additional cell scale \(H_n^{30}b_n=n^{-3/2+o(1)}\) also vanishes.

## 6. Conditional Gaussian estimates on all node kernels first

Fix a cavity initialization in \(\mathcal C_n\). Its frozen
extension and every matrix above are now deterministic, independent
of \(g\). All conditional probability statements in this section
are made before introducing an actual stopping restriction.

For a deterministic row \(v\), completing the square in its Gaussian
moment-generating function gives
\(\mathbb E e^{t v^Tg}=e^{t^2\|v\|^2/(2n)}\). Optimizing
exponential Markov in \(t\) gives, for \(x>0\),
\[
 \Pr\{|v^Tg|>\|v\|\sqrt{2x/n}\}\leq2e^{-x}.             \tag{38}
\]
For a real square matrix \(K\), let
\(S=(K+K^T)/2\), \(v=\|S\|_F\), and \(b=\|S\|_{\rm op}\).
Then
\[
 \Pr\left\{\left|g^TKg-{\operatorname{Tr}K\over n}\right|
       >{2v\sqrt x\over n}+{2bx\over n}\right\}
          \leq2e^{-x}.                                  \tag{39}
\]
To prove this, the antisymmetric part contributes neither trace
nor quadratic form. Orthogonally diagonalizing \(S\) gives the
centered form \(n^{-1}\sum_i\lambda_i(Z_i^2-1)\), where the
\(Z_i\) are independent standard Gaussians. Direct Gaussian
integration gives \(\mathbb E e^{uZ_i^2}=(1-2u)^{-1/2}\).
For \(2|t|b<n\), the power series of the logarithm yields
\[
\begin{aligned}
 \log\mathbb E\exp\left({t\over n}\sum_i\lambda_i(Z_i^2-1)\right)
 &=\sum_i[-t\lambda_i/n-\tfrac12\log(1-2t\lambda_i/n)]\\
 &\leq {t^2v^2/n^2\over1-2|t|b/n}.
\end{aligned}
\]
Indeed \(\sum_{m\geq2}|u|^m/m\leq |u|^2/[2(1-|u|)]\).
If \(v>0\), choose \(t=n\sqrt x/(v+2b\sqrt x)\).
The product of this \(t\) with the threshold in (39), minus the
last moment bound, is \(x\). Markov proves the upper tail; replace
\(S\) by \(-S\) for the lower tail. If \(v=0\), the form is zero.
This proves (39), also for nonsymmetric ordered-product kernels.

Apply (38) to every row of
\[
 O_kU(k,r+1)\mathcal B_{b,r},\quad
 O_k\in\{I_{m_n},Z_{1,k},Z_{2,k},L_{1,k},L_{2,k},Q_{1,k},Q_{2,k}\},
 \quad 0\leq r<k\leq N,
 \tag{40}
\]
and to the rows of \(I_n\) and \(\widehat B_k^TD_{a,k}\).
Apply (39) to every \(K_{ab}(k,r)\) and \(D_{a,k}\).
There are at most \(C(T+1)^2n^6\) scalar tests in total:
\(O(n^2)\) rows and \(O(N^2)=O((T+1)^2n^4)\) pairs.
Choose \(x=\log(2M_n n^{p_*})\), where \(M_n\geq1\) is the
number of tests. Then the union of their exceptional events has
probability at most \(n^{-p_*}\), and \(x\leq C_{T,p_*}\log n\)
for \(n\geq3\).

Choose \(A_*\) large enough that (26), (29), their finite products,
and fixed constants needed below are absorbed in \(H_n\). In
particular all row norms in (40) and all tested matrix operator
norms are at most \(H_n\). The symmetric Frobenius norms in
(39) are at most \(\sqrt n H_n\). Also
\[
 \Pr(\|g\|>2)
    \leq e^{-n}\mathbb E e^{n\|g\|^2/4}
    =e^{-n}2^{n/2}\leq e^{-n/2}.                         \tag{41}
\]
Thus on one event of the probability claimed in the theorem,
all tested row actions and centered quadratic forms are bounded by
\(H_n^2 a_n\), and \(\|g\|\leq2\). In particular
\[
 \|g\|_\infty+\max_{k,a}\|\widehat B_k^TD_{a,k}g\|_\infty
    \leq H_n^2a_n,
 \qquad
 \max_{k,a}|g^TD_{a,k}g-\operatorname{Tr}D_{a,k}/n|
    \leq H_n^2a_n,                                     \tag{42}
\]
after enlarging \(A_*\) to absorb finite sums of constants.

Define, using the actual old-node features only as bounded scalars,
\[
\begin{aligned}
 Y_0^{\rm lin}&=0,\\
 Y_{k+1}^{\rm lin}&=(I+\eta J_k)Y_k^{\rm lin}
                       +\eta\sum_b\mathcal B_{b,k}g h_{b,k},\\
 Y_k^{\rm lin}&=\eta\sum_{r<k,b}U(k,r+1)\mathcal B_{b,r}g h_{b,r}.
\end{aligned}                                                    \tag{43}
\]
The last equality follows by induction from the middle line and
the product order in (28). Although \(h_{b,r}\) depends on \(g\),
every summand kernel in (40) has already been bounded, and
\(|h_{b,r}|\leq B_1\). No conditional Gaussian assertion is made
about \(Y^{\rm lin}\) itself. Equation (29) and
\(\eta\sum_{r<k}1\leq T+1\) give
\[
 1+\|Y_k^{\rm lin}\|+\|(g h_{a,k})_a\|\leq H_n.
 \tag{44}
\]
The row bounds similarly give
\[
\begin{split}
 \max_{k,a}\{&\|\zeta_a(Y_k^{\rm lin})\|_\infty,
       \|v_k^{\rm lin}\|_\infty,
       \|Z_{a,k}Y_k^{\rm lin}+g h_{a,k}\|_\infty,\\
       &\|L_{a,k}Y_k^{\rm lin}+D_{a,k}g h_{a,k}\|_\infty,
       \|Q_{a,k}Y_k^{\rm lin}+\widehat B_k^TD_{a,k}g h_{a,k}\|_\infty\}
       \leq H_n^3a_n.
\end{split}                                                      \tag{45}
\]
The \(Dg\) term uses bounded diagonal \(D\) and \(\|g\|_\infty\);
\(\zeta_i=C^{1/2}u_i\) uses at most two coordinates. The bounds
hold for every bounded sequence \(h\) simultaneously.

There is also a deterministic extension of this same event to all
cell kernels. For \(r<k\), (27), (29), and (31) give
\[
 \|K_{ab}(t,r)-K_{ab}(k,r)\|_{\rm op}\leq H_n^3 b_n.
 \tag{46}
\]
For \(r=k\), compare instead with
\(K_{ab}(k+1,k)=L_{a,k+1}\mathcal B_{b,k}\); (27) gives the same
bound. These comparisons also apply to the row families with
\(L_a\) replaced by \(I,Z_a,L_a,Q_a\). For any matrix difference
\(E\), on \(\|g\|\leq2\),
\[
 |g^TEg-\operatorname{Tr}E/n|
       \leq(\|g\|^2+1)\|E\|_{\rm op}\leq5\|E\|_{\rm op}.
\]
Consequently all continuous-cell centered quadratic forms and row
actions are bounded by \(H_n^4(a_n+b_n)\). This requires neither
a time grid nor Gaussian conditioning at a random query.

## 7. Nonlinear defect and deterministic stability at nodes

We prove the local estimate needed to transfer (43). Fix a cavity
node and set \(X'=\widehat X+Y/\sqrt n\). Use the physical
increments and variations in (22)--(23), and let
\[
 D_*=1+\|Y\|+\|e\|,\quad
 \alpha=\max_a\{\|\zeta_a\|_\infty,\|v\|_\infty,
                                     \|\lambda_a\|_\infty\},\quad
 r_*=D_*(\alpha+D_*/\sqrt n).
\]
If \(\alpha\leq1\), \(D_*/\sqrt n\leq1\), then
\[
 \left\|\sqrt n[F(X',e/\sqrt n)-F(\widehat X,0)]
                  -\mathscr L(Y,e)\right\|
          \leq C_T(1+R_n)r_* .                          \tag{47}
\]
This estimate concerns a derivative of the actual simultaneous
update vector field, without replacing that update by a flow.

Here is a product proof. Taylor's integral formula and the bounded
second and third derivatives give
\[
\begin{aligned}
 \Delta h^{(1)}_a&=P_a\zeta_a+r_{1a},&
       \|r_{1a}\|&\leq C\alpha D_*,\\
 \Delta\phi_1'&=\phi_1''(\widehat z^{(1)})\odot\zeta+r_p,&
       \|r_p\|&\leq C\alpha D_*.
\end{aligned}                                                    \tag{48}
\]
Each coordinate remainder is bounded by \(C|\zeta_i|^2\), and
\(\|\zeta^2\|_2\leq\|\zeta\|_\infty\|\zeta\|_2\).
The exact upper increment is
\[
 \Delta z^{(2)}_a=\lambda_a+\beta_a,\qquad
 \beta_a=\widehat B r_{1a}+(V/\sqrt n)\Delta h^{(1)}_a,
 \qquad \|\beta_a\|\leq C_T r_* .                      \tag{49}
\]
In particular \(\|\Delta z^{(2)}_a\|\leq C_T D_*\).
Expand first in \(\lambda_a\), and then use Lipschitz continuity
for the displacement \(\beta_a\). The bound
\(\|\lambda_a^2\|_2\leq\|\lambda_a\|_\infty\|\lambda_a\|_2\)
and \(\|v\|_\infty\leq\alpha\) give
\[
\begin{aligned}
 \Delta h^{(2)}_a&=V_a\lambda_a+r_{2a},&
 \Delta\delta_a&=d\delta_a+r_{\delta a},&
 \|r_{2a}\|+\|r_{\delta a}\|&\leq C_T r_*.
\end{aligned}                                                    \tag{50}
\]
The additional readout product in \(\Delta\delta\) is
\(v\odot[\phi_2'(\widehat z^{(2)}+\Delta z^{(2)})
 -\phi_2'(\widehat z^{(2)})]\), whose norm is at most
\(C\alpha D_*\). Continuing the products gives exactly
\[
\begin{aligned}
 \Delta q_a&=dq_a+r_{qa},&
 r_{qa}&=\widehat B^Tr_{\delta a}+(V/\sqrt n)^T\Delta\delta_a,\\
 \Delta c_a&=\chi_a+r_{ca},&
 r_{ca}&=-{2\over n}
          [\widehat w^Tr_{2a}+v^T\Delta h^{(2)}_a].
\end{aligned}                                                    \tag{51}
\]
Thus \(\|r_{qa}\|\leq C_Tr_*\), \(|r_{ca}|\leq C_Tr_*/\sqrt n\),
\(\|dq_a\|+\|\Delta q_a\|+\|\Delta\delta_a\|\leq C_TD_*\),
and \(|\chi_a|+|\Delta c_a|\leq C_TD_*/\sqrt n\).

To check every term in (47), suppress the sample index for one
sample and write
\(\Delta\phi_1'=\phi_1'(z^{(1)})-\phi_1'(\widehat z^{(1)})\).
The first-root remainders after (24) are exactly, with vector
products taken coordinatewise,
\[
 \begin{aligned}
 &\widehat c[\phi_1'(\widehat z^{(1)})r_q
                 +r_p\widehat q+(\Delta\phi_1')\Delta q]\\
 &\quad+r_c\phi_1'(\widehat z^{(1)})\widehat q
   +\Delta c[(\Delta\phi_1')\widehat q
                              +\phi_1'(z^{(1)})\Delta q].
 \end{aligned}                                                    \tag{52}
\]
Their Euclidean norms are bounded respectively by
\(C_Tr_*\), \(C_T(R_n+1)\alpha D_*\), \(C_T\alpha D_*\),
\(C_Tr_*\), \(C_T\alpha D_*\), and \(C_TD_*^2/\sqrt n\).
Here the curvature term uses (13); the residual terms use
\(\|\widehat q\|\leq C_T\sqrt n\). The matrix-block remainders,
with its explicit normalization, are
\[
 {\widehat c\over\sqrt n}
    [r_\delta H^T+\widehat\delta r_1^T
                            +\Delta\delta(\Delta h^{(1)})^T]
 +{1\over\sqrt n}
    [r_c\widehat\delta H^T
      +\Delta c(\Delta\delta H^T+\delta'(\Delta h^{(1)})^T)],
 \tag{53}
\]
where \(\delta'=\widehat\delta+\Delta\delta\) has norm at most
\(C_T\sqrt n\). Their Frobenius norms are bounded by
\(C_T(r_*+\alpha D_*+D_*^2/\sqrt n)\). The readout remainders are
\(\widehat c r_2+r_c\widehat h^{(2)}+\Delta c\Delta h^{(2)}\),
with the same bound. Summing the two samples and multiplying by
the fixed \(C^{1/2}\) in the first block proves (47).

We also need stability using only the actual maximum at an old
node. For two bulk states \(X,X'\) with bounded matrix spectral
norms and readout maximum norms, at the same physical input \(e\),
put \(W=\sqrt n(X-X')\). Exact product differences give
\[
 \|\Delta z^{(2)}\|+\|\Delta\delta\|+\|\Delta q_I\|
       \leq C_T\|W\|,
 \qquad |\Delta c_a|\leq C_T\|W\|/\sqrt n.              \tag{54}
\]
For example \(\Delta z^{(2)}=\Delta B h^{(1)}+B'\Delta h^{(1)}\)
and \(\Delta q=\Delta B^T\delta+(B')^T\Delta\delta\). The
\(1/\sqrt n\) in \(\Delta B\) cancels the ordinary \(\sqrt n\)
norm of the feature or backward vector. The same calculation for
\(n^{-1}w^Th^{(2)}\) gives the residual bound.

Suppose the first state is actual at an old node \(k<s\). Let
\(z^{(1)\prime}\) denote the first preactivation at the comparison
state \(X'\). For the first-root factor use the exact identity
\[
 \begin{aligned}
 c\phi_1'(z^{(1)})q-c'\phi_1'(z^{(1)\prime})q'
   &=(c-c')\phi_1'(z^{(1)})q\\
   &\quad+c'[\phi_1'(z^{(1)})-\phi_1'(z^{(1)\prime})]q
       +c'\phi_1'(z^{(1)\prime})(q-q').
 \end{aligned}                                                    \tag{55}
\]
Only the middle term needs a maximum, and it uses the actual
\(\max|q_I|<R_n\). The other terms use (54) and the ordinary
Euclidean bound on \(q\). Matrix and readout product differences
then imply
\[
 \sqrt n\|F(X,e/\sqrt n)-F(X',e/\sqrt n)\|
           \leq C_T(1+R_n)\|W\|.                       \tag{56}
\]
There is no requirement on the maximum at \(X'\), or at a parameter
secant. Finally, keeping \(X'\) fixed and varying its upper input,
the \(e\)-terms of (23)--(24), evaluated at any such input, give
\[
 \sqrt n\|F(X',e/\sqrt n)-F(X',e^0/\sqrt n)\|
           \leq C_T\|e-e^0\|.                          \tag{57}
\]
Only Euclidean \(q_I\) bounds enter this derivative; it has no
first-root curvature variation. These calculations justify (56)
and (57) directly, without a bound on a Hessian along a secant.

Apply these estimates with
\(X_k^{\rm app}=\widehat X_k+Y_k^{\rm lin}/\sqrt n\) and
\(e^0_{a,k}=g h_{a,k}\). Equations (44)--(45) put the assumptions
of (47) in force. The approximate matrix and coordinatewise readout
are bounded by \(C_T+1\). By (20), (24), and (43), at \(k<s\),
\[
 \left\|\sqrt n\left[
 {X_{k+1}^{\rm app}-X_k^{\rm app}\over\eta}
                      -F(X_k^{\rm app},e_k^0/\sqrt n)\right]\right\|
       \leq H_n^6a_n.                                  \tag{58}
\]
This is a nonlinear consistency defect, not a time discretization
error. The algorithm and its linear recurrence both use the exact
step \(\eta\). Also \(\|e_k-e_k^0\|\leq C_T/\sqrt n\) by (14).
Writing
\(E_k=\|\sqrt n(X_k-\widehat X_k)-Y_k^{\rm lin}\|\),
(56)--(58) yield
\[
 E_{k+1}\leq[1+C_T\eta(1+R_n)]E_k
                    +\eta[H_n^6a_n+C_T/\sqrt n],\quad E_0=0.
\]
Iterating this scalar inequality and using \(s\eta\leq T+1\)
proves
\[
 \max_{k\leq s}E_k\leq H_n^9a_n.                       \tag{59}
\]
The final application uses the safe old node \(s-1\), so the
possibly overshooting node \(s\) is included. If \(s=0\), (59)
is the equality \(0=0\).

The field expansions (48)--(51), their linear coordinate bounds
(45), and (54), (59) now give
\[
\begin{split}
 \max_{k\leq s,a}\{&\|z^{(1)}_{a,I,k}-\widehat z^{(1)}_{a,I,k}\|_\infty,
 \|w_k-\widehat w_k\|_\infty,
 \|z^{(2)}_{a,k}-\widehat z^{(2)}_{a,k}\|_\infty,\\
 &\|\delta_{a,k}-\widehat\delta_{a,k}\|_\infty,
 \|q_{a,I,k}-\widehat q_{a,I,k}\|_\infty\}
        \leq H_n^{12}a_n.                               \tag{60}
\end{split}
\]
For example the upper increment at the approximate state is
\(\lambda_a+\beta_a\); (45) controls \(\lambda_a\) coordinatewise
and (49) controls \(\beta_a\) in Euclidean norm. The change from
the approximate state to the actual state is bounded by (54) and
(59), plus the upper input error \(O(n^{-1/2})\). The linear
\(dq\) coordinate in (45) and the remainder in (51) give the
last bound. This also explains why first-root coordinates alone
would not suffice for the nonlinear upper-gate remainder.
In ordinary Euclidean norms the accompanying bounds are
\[
 \max_{k\leq s}\|\sqrt n(X_k-\widehat X_k)\|\leq2H_n,
 \quad \|\delta_{a,k}-\widehat\delta_{a,k}\|\leq C_TH_n,
 \quad |c_{a,k}-\widehat c_{a,k}|\leq C_TH_n/\sqrt n.
 \tag{61}
\]
No closeness of \(z_{j,k}\) to \(\xi\) is asserted or used.

## 8. Node readback and replacement of the complete learned terms

At zero upper input, apply (50) at \(X_k^{\rm app}\). The linear
upper coordinate \(Z_{a,k}Y_k^{\rm lin}\) is covered by (40), and
(54), (59) handle the actual-minus-approximate difference. Hence
\[
 \|\delta^0_{a,k}-\widehat\delta_{a,k}-L_{a,k}Y_k^{\rm lin}\|
           \leq H_n^{12}a_n.                           \tag{62}
\]
Multiplication by \(g\), whose norm is at most two, and (43) give
\[
 g^T(\delta^0_{a,k}-\widehat\delta_{a,k})
   =\eta\sum_{r<k,b}h_{b,r}g^TK_{ab}(k,r)g
                                      +O(H_n^{13}a_n).
\]
The already simultaneous bound (39)--(42) replaces every quadratic
form by \(\operatorname{Tr}K/n\). Since
\(\eta\sum_{r<k,b}|h_{b,r}|\leq2B_1(T+1)\), the scalar cost is
at most \(C_TH_n^2a_n\), including for the actual adaptive sequence
\(h\). Together with the exact split (16), this proves the first
node formula in (34).

For the learned column, (14) says exactly
\[
 M_{a,k}={\eta\over n}\sum_{r<k,b}
                  c_{b,r}h_{b,r}\delta_{b,r}^T\delta_{a,k}.
\]
Use
\[
 \delta_{b,r}^T\delta_{a,k}
      -\widehat\delta_{b,r}^T\widehat\delta_{a,k}
  =(\delta_{b,r}-\widehat\delta_{b,r})^T\delta_{a,k}
     +\widehat\delta_{b,r}^T(\delta_{a,k}-\widehat\delta_{a,k}).
\]
Equations (10), (61) bound this difference by \(C_TH_n\sqrt n\).
The residual replacement costs
\(|c_{b,r}-\widehat c_{b,r}|\,\|\delta_{b,r}\|\|\delta_{a,k}\|/n
\leq C_TH_n/\sqrt n\). Summing with \(\eta|h_{b,r}|\) gives
\[
 \left|M_{a,k}-\eta\sum_{r<k,b}m_{ab}(k,r)h_{b,r}\right|
              \leq C_TH_n/\sqrt n.                     \tag{63}
\]
This replaces all the actual residuals and trained column history
with quantified errors, rather than omitting their contributions.

By (42), (60), and \(\|\ell_k\|\leq C_T/\sqrt n\),
\(\|e_{a,k}\|_\infty\leq C_TH_n^2a_n\). The base argument
\(B_k h^{(1)}_{a,I,k}\) in (15) is
\(z^{(2)}_{a,k}-e_{a,k}\), so its maximum difference from the
cavity upper field is at most \(H_n^{13}a_n\). The bounded third
derivative in (15) and the readout bound therefore give
\[
 \|D_{a,k}^{\rm dir}-D_{a,k}\|_{\rm op}\leq H_n^{14}a_n.
\]
The term in \(S\) containing \(\ell\) costs \(C_T/\sqrt n\);
the quadratic bound for \(D\) in (42) handles the remaining term.
Thus
\[
 |S_{a,k}-d_{a,k}h_{a,k}|\leq H_n^{16}a_n.               \tag{64}
\]
All errors (62)--(64) fit within \(H_n^{20}a_n\), proving the
second node formula. Bounds (10), (21), and (29) prove (37).

At the initial node the bulk parameters agree, but the upper
fields have the exact mismatch
\[
 z^{(2)}_{a,0}-\widehat z^{(2)}_{a,0}=g\phi_1(\xi_a),
\]
\[
 c_{a,0}-\widehat c_{a,0}
 =-{2\over n}w_0^T[
       \phi_2(\widehat z^{(2)}_{a,0}+g\phi_1(\xi_a))
                           -\phi_2(\widehat z^{(2)}_{a,0})].
 \tag{65}
\]
Accordingly \(Y_0^{\rm lin}=0\), but the step-zero source
\(\mathcal B_{b,0}g\phi_1(\xi_b)\) is present, including its
residual variation through \(\chi\). The exact scalar at zero is
\(q_{a,j,0}=G_{a,0}+\phi_1(\xi_a)g^TD_{a,0}^{\rm dir}g\).
This proves the node statements even if \(s=0\); no Gaussian law
is assigned to the complete initial scalar.

## 9. Whole-cell proof for raw affine/recomputed-hidden queries

Define the affine response
\[
 Y^{\rm lin}(t)=(1-\theta)Y_k^{\rm lin}+\theta Y_{k+1}^{\rm lin}.
\]
Substituting the exact recurrence (43) gives, identically,
\[
 Y^{\rm lin}(t)
     =\sum_{r,b}\omega_r(t)P(t,r)\mathcal B_{b,r}g h_{b,r}.
 \tag{66}
\]
In particular \(h_{b,k}\), not \(h_b(t)\) or \(h_{b,k+1}\),
drives the fractional new source. Products such as
\((I+\theta\eta J_k)U(k,r+1)\) are exact in this identity.

The coordinate \(X\) in (17) is affine in the raw parameters.
On every included cell, both full and cavity bulk coordinates
are affine, so their discrepancy from (66) is exactly the affine
combination of the discrepancies at its endpoints. Thus (59)
implies the stronger, unchanged bound
\[
 \sup_{t\leq\tau}
       \|\sqrt n(X(t)-\widehat X(t))-Y^{\rm lin}(t)\|
                 \leq H_n^9a_n.                        \tag{67}
\]
This assertion concerns raw coordinates only. Nonlinear hidden
queries still require the estimates below.

From (43), (44), and (26),
\[
 \|Y^{\rm lin}(t)-Y_k^{\rm lin}\|
          \leq C_T\eta[(1+R_n)H_n+1]\leq H_n^2\eta.
 \tag{68}
\]
For \(k<s\), the actual distinguished-root increment satisfies
\[
 |z^{(1)}_{a,j}(t)-z^{(1)}_{a,j,k}|\leq C_T\eta R_n,
 \qquad |h_a(t)-h_{a,k}|\leq C_T\eta R_n.                \tag{69}
\]
Alternatively the coordinate bounds below need only \(|h_a(t)|\leq B_1\),
since its direct upper forcing is \(g h_a(t)\).
Equations (27), (42), (45), and (68) give, with
\(e_a^0(t)=g h_a(t)\),
\[
\begin{split}
 \sup_{t\leq\tau,a}\{&\|\zeta_a(Y^{\rm lin}(t))\|_\infty,
 \|v^{\rm lin}(t)\|_\infty,
 \|Z_a(t)Y^{\rm lin}(t)+e_a^0(t)\|_\infty,\\
 &\|L_a(t)Y^{\rm lin}(t)+D_a(t)e_a^0(t)\|_\infty,
 \|Q_a(t)Y^{\rm lin}(t)+\widehat B(t)^TD_a(t)e_a^0(t)\|_\infty\}
            \leq H_n^6(a_n+b_n).                       \tag{70}
\end{split}
\]
For example the change in \(Z_aY^{\rm lin}\) costs at most
\(C_Tb_n H_n+C_TH_n^2\eta\). The direct term uses
\(\|g\|_\infty B_1\). For the last term use (27) to extend
the bound on \(\widehat B_k^TD_{a,k}g\). These arguments establish
coordinate control at the actual query rather than supposing that
an interpolated hidden field is affine.

Apply the static expansions (48)--(51) at the cavity point
\(\widehat X(t)\), with \(Y=Y^{\rm lin}(t)\), first with upper
input \(e^0(t)\), and then with zero upper input when computing
\(\delta_a^0\). Their proof applies because (13) gives
\(R_n+O(b_n)\) throughout the cavity cell. Equations (44), (67),
(70), and \(\|e(t)-e^0(t)\|\leq C_T/\sqrt n\) give
\[
\begin{split}
 \sup_{t\leq\tau,a}\{&\|z^{(1)}_{a,I}-\widehat z^{(1)}_{a,I}\|_\infty,
 \|w-\widehat w\|_\infty,
 \|z^{(2)}_a-\widehat z^{(2)}_a\|_\infty,\\
 &\|\delta_a-\widehat\delta_a\|_\infty,
 \|q_{a,I}-\widehat q_{a,I}\|_\infty\}
           \leq H_n^{15}(a_n+b_n),                     \tag{71}
\end{split}
\]
\[
 \sup_{t\leq\tau,a}
 \|\delta_a^0(t)-\widehat\delta_a(t)-L_a(t)Y^{\rm lin}(t)\|
                 \leq H_n^{16}(a_n+b_n).               \tag{72}
\]
The ordinary Euclidean and residual bounds remain
\[
 \|\sqrt n(X(t)-\widehat X(t))\|\leq2H_n,
 \quad \|\delta_a(t)-\widehat\delta_a(t)\|\leq C_TH_n,
 \quad |c_a(t)-\widehat c_a(t)|\leq C_TH_n/\sqrt n.
 \tag{73}
\]
To verify the absence of a factor \(\sqrt n\) in the middle
bound, apply (54) to the actual and cavity bulk states and add
the physical forcing \(e\), whose Euclidean norm is \(O(1)\).
The residual difference then has its explicit additional
\(1/\sqrt n\) factor as in (23), (54).

Multiply (72) by \(g\) and insert (66). The centered quadratic
estimate extended in (46) gives
\[
 g^T(\delta_a^0(t)-\widehat\delta_a(t))
   =\sum_{r,b}\omega_r(t)\kappa_{ab}(t,r)h_{b,r}
                         +O(H_n^{18}(a_n+b_n)),         \tag{74}
\]
since \(\sum_r\omega_r(t)=t\leq T\). This proves the first
whole-cell formula by the exact split (16).

For the learned term, the exact affine column formula (14) is
\[
 M_a(t)={1\over n}\sum_{r,b}\omega_r(t)c_{b,r}h_{b,r}
                                             \delta_{b,r}^T\delta_a(t).
\]
Use the two-factor identity preceding (63), now with query \(t\),
and (61), (73). It gives uniformly
\[
 \left|M_a(t)-\sum_{r,b}\omega_r(t)m_{ab}(t,r)h_{b,r}\right|
                  \leq C_TH_n/\sqrt n.                 \tag{75}
\]
For the direct term, (71), (15), bounded \(\phi_2'''\), and
\(\|e_a(t)\|_\infty\leq C_T(\|g\|_\infty+n^{-1/2})\)
give \(\|D_a^{\rm dir}(t)-D_a(t)\|_{\rm op}
\leq H_n^{17}(a_n+b_n)\). Extend the quadratic estimate for
\(D_a\) using (27) just as in (46). Together with the
\(O(n^{-1/2})\) term involving \(\ell(t)\), this gives
\[
 |S_a(t)-d_a(t)h_a(t)|\leq H_n^{20}(a_n+b_n).             \tag{76}
\]
Equations (74)--(76) fit in the error \(H_n^{30}(a_n+b_n)\).
This completes the proof of (35). All steps are uniform over each
whole cell on the single event constructed before the actual stop;
there is no accumulation of a per-query error over \(N\) nodes.

## 10. Actual root queries and precise established/open boundary

Let \(\mathcal R_a(t)\) denote the entire right-hand side of the
second line of (35) without its scalar error. The exact first-root
interpolation satisfies, on cell interiors with \(k<s\),
\[
 \dot z_j(t)=C(c_{a,k}\phi_1'(z^{(1)}_{a,j,k})q_{a,j,k})_{a=1,2}.
 \tag{77}
\]
It can also be written with cavity residuals and the query-time
trace representation, with a quantified vanishing remainder:
\[
 \dot z_j(t)
   =C(\widehat c_a(t)\phi_1'(z^{(1)}_{a,j}(t))
                                      \mathcal R_a(t))_{a=1,2}
      +r_j(t),
 \tag{78}
\]
\[
 \|r_j(t)\|
   \leq C_T\left[
       \varepsilon_n^{\rm cell}
       +{H_n(1+R_n)\over\sqrt n}
       +\eta(1+R_n)^2+b_n\right]
   \leq H_n^{35}(a_n+b_n)\longrightarrow0.              \tag{79}
\]
Here is the product estimate. Replace \(c_{a,k}\) by
\(\widehat c_a(t)\); (11), (73) bound its change by
\(C_T(\eta+H_n/\sqrt n)\), which multiplies
\(|q_{a,j,k}|<R_n\). Replace the first gate using (69); the cost
is \(C_T\eta R_n^2\). Finally
\(|q_{a,j,k}-\mathcal R_a(t)|\leq C_Tb_n+
\varepsilon_n^{\rm cell}\) by (12), (35). Bounded residuals and
gates prove (79). The equation holds almost everywhere; at a node
the appropriate one-sided version uses its adjacent old node.
After integration the total root error is at most
\(T H_n^{35}(a_n+b_n)\). Equation (78) is an approximate identity
for the actual root, not a uniqueness or limit theorem for a new
closed stochastic equation.

To document that the conditioning event is only an initialization
restriction, its probability can be bounded without a dynamical
claim. A maximal \(1/4\)-separated subset of the unit sphere in
\(\mathbb R^k\) is a \(1/4\)-net with at most \(9^k\) points:
its disjoint radius-\(1/8\) balls fit in the radius-\(9/8\) ball.
Approximating each vector in a bilinear form by its net point
shows \(\|B_0\|_{\rm op}\leq2\max|u^TB_0v|\) on the two nets.
Each fixed form has variance \(1/n\), so (38) gives
\[
 \Pr(\|B_0\|_{\rm op}>8)
     \leq2\exp[-(8-2\log9)n].                           \tag{80}
\]
For any fixed \(q_*>0\), again from (38),
\[
 \Pr\{\|w_0\|_\infty>
              \sqrt{2(q_*+2)\log n}/n\}
       \leq2n^{-(q_*+1)}.                               \tag{81}
\]
On the complementary events,
\[
 \max_{a,i\in I}|\widehat q_{a,i,0}|
       \leq8\|\phi_2'\|_\infty
                         \sqrt{2(q_*+2)\log n/n}.
\]
For sufficiently large \(n\) this is below \(R_n\), and the
threshold in (81) is below one. Thus
\(\Pr(\mathcal C_n^c)\leq
2e^{-(8-2\log9)n}+2n^{-(q_*+1)}\) in that width regime.
No positive-time survival probability follows from (80)--(81).

The established conclusions are conditional stopped approximations
for one deterministic distinguished neuron, with an event uniform
over all algorithm nodes and all included raw cells. All actual
query and root-equation errors displayed above vanish at fixed
\(T,K,\rho\). The extra whole-cell scale is explicit; the algorithm
itself is exact, and no gradient-flow comparison is used. The
causal node sums retain the actual bounded root features.

What remains outside this extension is a width-uniform bound on
the independent trace, or on its action on the actual feature
history, and removal of the actual and cavity stops. The bound in
(37) is only \(n^{o(1)}\), which need not remain bounded. Neither
conditioning on survival, nor replacing the actual root path by an
independent one, has been used to turn it into a stronger assertion.
These independent trace/continuation questions are left to the
main work.
