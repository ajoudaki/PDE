# Compact first saturation and a linear-tail top activation: exact simultaneous RawGD

This is an independent discrete proof for the model and initialization in
`COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md`. That candidate was the only mathematical
source read. No assertion of its proof is assumed here. There are no experiments,
external imports, auxiliary mathematical sources, or other agents.

**Conclusion.** The proposed discrete strategy works. For every fixed interior
input correlation, the prescribed canonical Gaussian initialization has an
explicit event of probability tending to one on which simultaneous RawGD with
the single fixed step size \(\eta=n^{-2}\) optimizes to zero loss, has finite total
residual clock, and converges in all its finite-dimensional parameters. The width
threshold and all bounds below are independent of the number of steps. The
initial loss margin is attained by the actual GD iterates. No comparison with
gradient flow is used.

The proof first certifies individual update segments by a full raw-coordinate
Hessian bound. Discrete action then supplies a short-time loss margin. An exact
centered balance, including its quadratic Euler error, bounds the weighted
residual clock and closes a separate all-time induction.

## 1. Canonical model, exact updates, and the frozen rows

Fix \(d\ge2\), \(\rho\in(-1,1)\), and two inputs and labels satisfying
\[
 \|x_1\|_2^2=\|x_2\|_2^2=d,\qquad x_1^Tx_2=d\rho,
 \qquad y=(1,-1)^T.
 \tag{1}
\]
Let \(p\) be even, nonnegative, smooth, supported on \([-R,R]\), and positive
on \((-R,R)\). The fixed activations are
\[
 \phi_1(z)=\int_0^z p(u)\,du,\qquad
 \phi_2(z)=z+\varepsilon\arctan z,\qquad \varepsilon>0.
\]
Set the finite constants
\[
 A=\int_0^R p(u)\,du>0,\quad
 P=\|\phi_1'\|_\infty,\quad P_2=\|\phi_1''\|_\infty,
 \quad M=1+\varepsilon,\quad Q_2=2\varepsilon.
 \tag{2}
\]
Then
\[
 |\phi_1|\le A,\qquad 1\le\phi_2'\le M,\qquad
 |\phi_2(z)|\le M|z|,\qquad |\phi_2''(z)|\le Q_2.
 \tag{3}
\]
All vector norms are ordinary Euclidean norms; all Frobenius and operator norms
are ordinary, unnormalized norms. Every normalizing factor is displayed.

Both hidden widths are \(n\). The canonical parameters are
\[
 W^{(1)}\in\mathbb R^{n\times d},\qquad
 W^{(2)}\in\mathbb R^{n\times n},\qquad W^{(3)}\in\mathbb R^n.
\]
For \(a\in\{1,2\}\), define
\[
 z^{(1)}_a=W^{(1)}x_a,\quad h^{(1)}_a=\phi_1(z^{(1)}_a),\quad
 z^{(2)}_a=W^{(2)}h^{(1)}_a,\quad h^{(2)}_a=\phi_2(z^{(2)}_a),
\]
\[
 f_a=\frac1n(W^{(3)})^Th^{(2)}_a,\qquad
 r=f-y,\qquad L=\|r\|_2^2,\qquad s=\|r\|_2,
 \qquad H^{(\ell)}=(h^{(\ell)}_1,h^{(\ell)}_2).
 \tag{4}
\]
Activations and derivatives act coordinatewise. At node \(k\), compute all three
right-hand sides from that same node:
\[
\begin{split}
 F^{(1)}_k={}&-\frac2d\sum_{a=1}^2 r_{a,k}
 \left[\phi_1'(z^{(1)}_{a,k})\odot
 (W^{(2)}_k)^T
       \bigl(W^{(3)}_k\odot\phi_2'(z^{(2)}_{a,k})\bigr)\right]x_a^T,\\
 F^{(2)}_k={}&-\frac2n\sum_{a=1}^2 r_{a,k}
       \bigl(W^{(3)}_k\odot\phi_2'(z^{(2)}_{a,k})\bigr)
       (h^{(1)}_{a,k})^T,\\
 F^{(3)}_k={}&-2\sum_{a=1}^2r_{a,k}\phi_2(z^{(2)}_{a,k}).
\end{split}
\]
The algorithm throughout this document is exactly
\[
 W^{(\ell)}_{k+1}=W^{(\ell)}_k+\eta F^{(\ell)}_k,
 \qquad \ell=1,2,3,\qquad \eta=n^{-2}.
 \tag{5}
\]
There is no sequential layer update, fresh-node evaluation, projection, clipping,
or step-size adaptation. Every finite iterate is well-defined: a finite parameter
vector has a finite right-hand side in (5).

An initially saturated first row, meaning both of its first preactivations lie
outside \((-R,R)\), is exactly unchanged at every step. Indeed both factors
\(\phi_1'\) in its row update are zero. If the row has remained unchanged through
node \(k\), those two factors are still zero at node \(k\), proving the assertion
by induction. Its row is also unchanged on every straight update segment.

Let \(N_s,N_o\) count initially saturated same-sign and opposite-sign rows. Their
fixed contribution implies, at all nodes and throughout all update segments,
\[
 \Gamma:=\frac1n(H^{(1)})^TH^{(1)}
 \succeq \frac{A^2}{n}
 \begin{pmatrix}N_s+N_o&N_s-N_o\\N_s-N_o&N_s+N_o\end{pmatrix}
 \succeq\gamma_n I_2,
 \qquad \gamma_n=\frac{2A^2}{n}\min(N_s,N_o).
 \tag{6}
\]
Every remaining row contributes a positive semidefinite outer product. No other
first row is frozen by the algorithm. Until the initialization calculation,
assume \(\gamma_n\ge\gamma>0\).

## 2. The raw gradient, all mixed Hessian terms, and a one-step certificate

For purposes of differentiation only, identify the raw Euclidean coordinates as
\[
 \theta=\left(\sqrt{\frac dn}W^{(1)},\ W^{(2)},\
                  \frac{W^{(3)}}{\sqrt n}\right).
 \tag{7}
\]
The Euclidean product norm on these coordinates is therefore explicitly
\[
 \|\Delta\theta\|_2^2
 =\frac dn\|\Delta W^{(1)}\|_F^2
       +\|\Delta W^{(2)}\|_F^2
       +\frac1n\|\Delta W^{(3)}\|_2^2.
\]
Direct differentiation of (4) gives
\[
 \theta_{k+1}=\theta_k-\eta\nabla_\theta L(\theta_k),\qquad
 \|\nabla_\theta L\|_2^2
 =\frac dn\|F^{(1)}\|_F^2+\|F^{(2)}\|_F^2
                          +\frac1n\|F^{(3)}\|_2^2
 =4r^TKr.
 \tag{8}
\]
Here \(K\) is the Gram matrix of the two raw prediction gradients. It splits
into the three positive semidefinite layer contributions \(K_1+K_2+K_3\), with
\[
 K_3=\frac1n(H^{(2)})^TH^{(2)},
\]
\[
 (K_2)_{ab}=\frac{(h^{(1)}_a)^Th^{(1)}_b}{n^2}
 \left\langle W^{(3)}\odot\phi_2'(z^{(2)}_a),
                 W^{(3)}\odot\phi_2'(z^{(2)}_b)\right\rangle.
 \tag{9}
\]
The first-layer contribution is the Gram of the matrices
\[
 \frac1{\sqrt{nd}}
 \left[\phi_1'(z^{(1)}_a)\odot(W^{(2)})^T
           \bigl(W^{(3)}\odot\phi_2'(z^{(2)}_a)\bigr)\right]x_a^T.
\]
Writing \(b=\|W^{(3)}\|_2/\sqrt n\), the exact second-layer kernel satisfies
\[
 K_2=\frac1n\sum_i(W^{(3)}_i)^2
 \operatorname{diag}\bigl(\phi_2'(z^{(2)}_{i1}),\phi_2'(z^{(2)}_{i2})\bigr)
 \Gamma
 \operatorname{diag}\bigl(\phi_2'(z^{(2)}_{i1}),\phi_2'(z^{(2)}_{i2})\bigr)
 \succeq\gamma b^2I_2.
 \tag{10}
\]
This is a congruence argument using (6) and \(\phi_2'\ge1\), not an entrywise
comparison.

We next prove bounds on the **full** raw Hessian, including all layer-mixed terms.
Suppose a parameter state satisfies
\[
 \|W^{(2)}\|_{\rm op}\le U,\qquad
 \frac{\|W^{(3)}\|_2}{\sqrt n}\le V.
 \tag{11}
\]
No bound on \(W^{(1)}\), on an individual preactivation, or on an individual
readout beyond \(\|W^{(3)}\|_\infty\le\sqrt n V\) is imposed. Define
\[
 T(U)=A+UP,
\]
\[
 \mathcal G(U,V)=M\bigl(AU+VT(U)\bigr),
\]
\[
 \mathcal J(U,V)=2MT(U)+2MPV+Q_2V T(U)^2+MVUP_2,
\]
\[
 \mathcal H(U,V)=4\mathcal G(U,V)^2
                    +4(1+MAUV)\mathcal J(U,V).
 \tag{12}
\]
Then, for each sample,
\[
 \|\nabla_\theta f_a\|_2\le\mathcal G(U,V),\qquad
 \|\nabla_\theta^2 f_a\|_{\rm op}\le\sqrt n\,\mathcal J(U,V),
 \qquad
 \|\nabla_\theta^2 L\|_{\rm op}\le\sqrt n\,\mathcal H(U,V).
 \tag{13}
\]

Here is a derivation. For a raw direction \(u=(u_1,u_2,u_3)\), the corresponding
canonical variations are
\(\sqrt{n/d}\,u_1,u_2,\sqrt n\,u_3\). Suppressing the sample index,
\[
 \|Dz^{(1)}[u]\|_2\le\sqrt n\|u_1\|_F,\qquad
 \|Dh^{(1)}[u]\|_2\le P\sqrt n\|u_1\|_F,
\]
\[
 Dz^{(2)}[u]=u_2h^{(1)}+W^{(2)}Dh^{(1)}[u],\qquad
 \|Dz^{(2)}[u]\|_2
 \le\sqrt n\bigl(A\|u_2\|_F+UP\|u_1\|_F\bigr)
 \le\sqrt n T(U)\|u\|_2.
 \tag{14}
\]
The unbounded top activation is controlled by its ordinary second moment:
\[
 \frac{\|h^{(2)}_a\|_2}{\sqrt n}\le MAU,
 \qquad \frac{\|H^{(2)}\|_F}{\sqrt n}\le\sqrt2 MAU.
 \tag{15}
\]
The two terms in
\[
 Df_a[u]=\frac1n\left[
 \sqrt n\,u_3^T\phi_2(z^{(2)})
 +(W^{(3)})^T\bigl(\phi_2'(z^{(2)})\odot Dz^{(2)}[u]\bigr)\right]
\]
are bounded by \(MAU\|u_3\|_2\) and
\(MV(A\|u_2\|_F+UP\|u_1\|_F)\). This proves the gradient bound.

For a second raw direction \(v\), the second differential of the second
preactivation is exactly
\[
 D^2z^{(2)}[u,v]
 =u_2Dh^{(1)}[v]+v_2Dh^{(1)}[u]
 +W^{(2)}\left[\phi_1''(z^{(1)})\odot
                  Dz^{(1)}[u]\odot Dz^{(1)}[v]\right].
 \tag{16}
\]
The second differential of the prediction is exactly
\[
\begin{split}
 D^2f_a[u,v]=\frac1n\Big[&
 \sqrt n\,u_3^T\bigl(\phi_2'(z^{(2)})\odot Dz^{(2)}[v]\bigr)
 +\sqrt n\,v_3^T\bigl(\phi_2'(z^{(2)})\odot Dz^{(2)}[u]\bigr)\\
 &+(W^{(3)})^T\bigl(\phi_2''(z^{(2)})\odot
                           Dz^{(2)}[u]\odot Dz^{(2)}[v]\bigr)\\
 &+(W^{(3)})^T\bigl(\phi_2'(z^{(2)})\odot D^2z^{(2)}[u,v]\bigr)
 \Big].
\end{split}
 \tag{17}
\]
For \(\|u\|_2=\|v\|_2=1\), its readout-mixed terms total at most \(2MT(U)\).
The top-curvature term is at most \(\sqrt n Q_2VT(U)^2\), using
\(\|W^{(3)}\|_\infty\le\sqrt n V\) and
\(\sum_i|\alpha_i\beta_i|\le\|\alpha\|_2\|\beta\|_2\).
The first two terms of (16), after contraction in (17), total at most \(2MPV\).
Its last term contributes at most \(\sqrt n MVUP_2\), using
\(\|\alpha\odot\beta\|_2\le\|\alpha\|_2\|\beta\|_2\).
Since \(n\ge1\), these estimates give the second bound in (13).

Finally,
\[
 \nabla_\theta^2L
 =2\sum_{a=1}^2\left(
     \nabla_\theta f_a(\nabla_\theta f_a)^T
                         +r_a\nabla_\theta^2f_a\right),
 \qquad \|r\|_2\le\sqrt2(1+MAUV),
\]
which gives the last bound in (13). In particular, (13) applies throughout a
bounded upper-parameter region without assuming that its loss is small.

**One-step certificate.** Fix finite \(U_g,V_g>0\) and \(\overline L=4\). Suppose
the current node satisfies (11) with \(U_g,V_g\) and \(L_k\le\overline L\). Put
\[
 J_g=2\sqrt2\sqrt{\overline L}\,\mathcal G(U_g,V_g),\qquad
 H_g=\mathcal H(U_g+1,V_g+1).
\]
If
\[
 \eta J_g\le1,\qquad \eta\sqrt n H_g\le1,
 \tag{18}
\]
then the complete proposed update segment lies in the region
\(\|W^{(2)}\|_{\rm op}\le U_g+1\), \(\|W^{(3)}\|_2/\sqrt n\le V_g+1\).
Indeed \(\|\nabla_\theta L(\theta_k)\|_2\le J_g\), and each of these two norms
can increase by at most the raw displacement \(\eta J_g\). This segment
containment is proved **before** applying a descent estimate.

Let \(g_k=\nabla_\theta L(\theta_k)\). Twice integrating the second derivative
of \(u\mapsto L(\theta_k-ug_k)\) on the already contained segment gives
\[
 L(\theta_k-ug_k)
 \le L_k-u\left(1-\frac{u\sqrt nH_g}{2}\right)\|g_k\|_2^2
 \le L_k-\frac u2\|g_k\|_2^2,
 \qquad 0\le u\le\eta.
 \tag{19}
\]
Consequently the actual next node satisfies
\[
 L_k-L_{k+1}\ge\frac\eta2\|g_k\|_2^2
                 =2\eta r_k^TK_kr_k
                 \ge2\eta\gamma b_k^2 L_k.
 \tag{20}
\]
The loss is also nonincreasing within the segment: its derivative is at most
\(-(1-u\sqrt nH_g)\|g_k\|_2^2\le0\), by integrating the Hessian once.
Whenever \(s_k>0\), division by \(s_k+s_{k+1}\le2s_k\) gives the precise factor
\[
 s_k-s_{k+1}\ge\eta\gamma b_k^2s_k.
 \tag{21}
\]
If \(s_k=0\), every update is zero and these inequalities continue to hold.

## 3. Consequences on a certified finite prefix: action and short-time coercivity

For now, consider only a finite prefix on which the one-step certificate has
actually been verified. Summing (20) in its gradient form gives
\[
 \sum_{j<k}\eta\|g_j\|_2^2\le2(L_0-L_k)\le2L_0.
 \tag{22}
\]
Let \(t_k=k\eta\), and interpolate the canonical parameters affinely on every
cell \([t_j,t_{j+1}]\), with slope \(F^{(\ell)}_j\). Equivalently,
\(\theta(t)=\theta_j-(t-t_j)g_j\). A partial-cell action is bounded by the
action of its complete, certified cell. Cauchy--Schwarz therefore gives, at nodes
and everywhere in the certified cells,
\[
 \|\theta(t)-\theta(0)\|_2\le\sqrt{2tL_0},
\]
\[
 \|W^{(2)}(t)-W^{(2)}_0\|_F\le\sqrt{2tL_0},\quad
 \frac{\|W^{(3)}(t)-W^{(3)}_0\|_2}{\sqrt n}\le\sqrt{2tL_0},\quad
 \sqrt{\frac dn}\|W^{(1)}(t)-W^{(1)}_0\|_F\le\sqrt{2tL_0}.
 \tag{23}
\]
These are action estimates for the actual Euler polygon, not a gradient-flow
energy identity.

Write \(A_0=W^{(2)}_0\) and assume \(\|A_0\|_{\rm op}\le\alpha_0\). Let
\(e(t)=\sqrt{2tL_0}\). The input norms and the Lipschitz constant \(P\) give
\[
 \frac{\|H^{(1)}(t)-H^{(1)}(0)\|_F}{\sqrt n}
 \le\sqrt2P e(t).
\]
Expanding the product as
\[
 W^{(2)}(t)H^{(1)}(t)-A_0H^{(1)}(0)
 =[W^{(2)}(t)-A_0]H^{(1)}(0)
       +W^{(2)}(t)[H^{(1)}(t)-H^{(1)}(0)]
\]
and using \(\phi_2\)'s Lipschitz bound proves
\[
 \frac{\|H^{(2)}(t)-H^{(2)}(0)\|_F}{\sqrt n}
 \le M\sqrt2 e(t)\,[A+P(\alpha_0+e(t))].
 \tag{24}
\]
Fix \(\kappa>0\), \(\overline L=4\), and the positive time
\[
 \tau=\min\left\{\frac1{4\overline L},\
 \frac{\kappa}{32M^2\overline L[A+P(\alpha_0+1)]^2}\right\}.
 \tag{25}
\]
If \(L_0\le\overline L\), then for \(t\le2\tau\) the right side of (24) is
at most \(\sqrt\kappa/2\), and \(e(t)\le1\). Thus, if
\(K_{3,0}\succeq\kappa I_2\), then for any unit \(v\in\mathbb R^2\),
\[
 \left\|\frac{H^{(2)}(t)v}{\sqrt n}\right\|_2
 \ge \left\|\frac{H^{(2)}(0)v}{\sqrt n}\right\|_2
       -\frac{\|H^{(2)}(t)-H^{(2)}(0)\|_F}{\sqrt n}
 \ge\frac{\sqrt\kappa}{2}.
\]
Consequently,
\[
 K_3(t)\succeq\frac\kappa4 I_2
 \quad\text{on the certified portion of }[0,2\tau].
 \tag{26}
\]
At every such old node, (20) yields
\[
 L_{j+1}\le(1-\eta\kappa/2)L_j.
 \tag{27}
\]
Section 5 below certifies this entire initial interval by induction; neither
(22) nor (26) is assumed on an uncertified cell.

## 4. Exact discrete centered balance and the clock on a finite prefix

Use the quantities
\[
 B_k=W^{(2)}_k-A_0,\quad a_k=\|B_k\|_F,\quad
 b_k=\frac{\|W^{(3)}_k\|_2}{\sqrt n},\quad
 b_0=\frac{\|W^{(3)}_0\|_2}{\sqrt n},\quad
 X_k=\sum_{j<k}\eta s_jb_j.
 \tag{28}
\]
Thus \(X_0=a_0=0\). The separately denoted constant \(\alpha_0\) bounds
\(\|A_0\|_{\rm op}\), not its Frobenius norm or the centered displacement.

The bounded homogeneity defect and the constants used in the clock argument are
\[
 D(z)=z\phi_2'(z)-\phi_2(z)
      =\varepsilon\left(\frac z{1+z^2}-\arctan z\right),\qquad
 D_*:=\|D\|_\infty=\frac{\varepsilon\pi}{2},
\]
\[
 C_B=2\sqrt2 MA,\qquad C_f=\sqrt2 MA,\qquad
 C_D=4\sqrt2(D_*+M\alpha_0A).
 \tag{29}
\]
For the equality defining \(D_*\), its derivative is
\(-2\varepsilon z^2/(1+z^2)^2\) and its two limits are
\(\mp\varepsilon\pi/2\).

Equation (5) gives, without any descent assumption,
\[
 \|F^{(2)}_k\|_F\le C_Bs_kb_k,\qquad
 a_k\le C_BX_k.
 \tag{30}
\]
Expanding the two squared norms in a single simultaneous step gives exactly
\[
\begin{split}
 &(\|B_{k+1}\|_F^2-b_{k+1}^2)-(\|B_k\|_F^2-b_k^2)\\
 &=-\frac{4\eta}{n}\sum_{a=1}^2r_{a,k}
 \left\langle W^{(3)}_k,
 D(z^{(2)}_{a,k})
   -\phi_2'(z^{(2)}_{a,k})\odot A_0h^{(1)}_{a,k}\right\rangle\\
 &\hspace{1em}+\eta^2\left(\|F^{(2)}_k\|_F^2
                            -\frac{\|F^{(3)}_k\|_2^2}{n}\right).
\end{split}
 \tag{31}
\]
Indeed the two linear cross terms are respectively
\(-4\eta n^{-1}\sum_a r_{a,k}
 \langle W^{(3)}_k,\phi_2'(z^{(2)}_{a,k})\odot B_kh^{(1)}_{a,k}\rangle\)
and \(-4\eta\langle r_k,f_k\rangle\). Substituting
\(B_kh^{(1)}_{a,k}=z^{(2)}_{a,k}-A_0h^{(1)}_{a,k}\) proves (31).
All its features and derivatives are evaluated at the old node. No transported
feature derivative or new-node term is present in this norm expansion.

The absolute value of the first part of (31) is at most
\(\eta C_Ds_kb_k\). On a certified prefix, the sum of absolute quadratic
corrections is bounded by
\[
 \sum_{j<k}\eta^2
 \left|\|F^{(2)}_j\|_F^2-\frac{\|F^{(3)}_j\|_2^2}{n}\right|
 \le\eta\sum_{j<k}\eta\|g_j\|_2^2
 \le2\eta L_0.
 \tag{32}
\]
Using \(\|B_0\|_F=0\), we obtain
\[
 |a_k^2-b_k^2+b_0^2|\le C_DX_k+2\eta L_0.
 \tag{33}
\]
In particular, if \(\eta\le1\) and \(L_0\le4\), put \(E_*=8\). Then
\[
 a_k\le b_k+\sqrt{C_D}\sqrt{X_k}+\sqrt{E_*},\qquad
 b_k^2\le C_B^2X_k^2+b_0^2+C_DX_k+E_*.
 \tag{34}
\]
The prediction bound, with its explicit width factors, is
\[
 \|f_k\|_2
 \le\frac{\|H^{(2)}_k\|_F\|W^{(3)}_k\|_2}{n}
 \le C_fb_k\|W^{(2)}_k\|_{\rm op}
 \le C_fb_k(\alpha_0+a_k).
 \tag{35}
\]

Suppose a certified node \(m\) has \(s_m\le s_*<\sqrt2\). At any later certified
node, monotonicity gives \(\|f_k\|_2\ge\sqrt2-s_*\). Combining (34)--(35), first
for \(b_k\le1\) and then trivially for \(b_k\ge1\), proves
\[
 b_k\ge\frac{c_*}{1+\sqrt{X_k}},\qquad
 c_*:=\min\left\{1,
 \frac{\sqrt2-s_*}{C_f(\alpha_0+1+\sqrt{E_*}+\sqrt{C_D})}\right\}>0.
 \tag{36}
\]
Thus the bounded Euler balance error only enlarges a finite constant.

Use the elementary increasing function
\[
 F(x)=\int_0^x\frac{du}{1+\sqrt u}
      =2\bigl(\sqrt x-\log(1+\sqrt x)\bigr),\qquad x\ge0.
 \tag{37}
\]
Its integrand decreases, so for \(v\ge u\ge0\),
\[
 F(v)-F(u)\le\frac{v-u}{1+\sqrt u}.
 \tag{38}
\]
Also \(F(x)\ge\sqrt x-2\log2\): the function
\(\log(1+u)-u/2\) has its maximum at \(u=1\), as its derivative shows, so
\(\log(1+u)\le u/2+\log2\). In particular, \(F\) is unbounded.

The exact clock increment is \(X_{k+1}-X_k=\eta s_kb_k\). Equations
(21), (36), and (38) give
\[
 s_k-s_{k+1}\ge\gamma b_k(X_{k+1}-X_k)
 \ge\gamma c_*\frac{X_{k+1}-X_k}{1+\sqrt{X_k}}
 \ge\gamma c_*\bigl(F(X_{k+1})-F(X_k)\bigr).
 \tag{39}
\]
The concavity inequality has the required direction. Telescoping on any such
finite prefix yields
\[
 s_k+\gamma c_*\bigl(F(X_k)-F(X_m)\bigr)\le s_m,
 \qquad k\ge m.
 \tag{40}
\]
Only lower bounds at the old nodes enter (39). This fact is what lets (40)
bound a candidate next node before knowing that the next node remains in the
bounded region.

## 5. Independently fixed constants and the noncircular all-time induction

Here is a deterministic theorem with a finite width threshold. Fix
\(\alpha_0\ge0\), \(\gamma>0\), and \(\kappa>0\), and keep
\(\overline L=4\), \(E_*=8\). Define \(\tau\) by (25), and define in this order
\[
 s_*=\sqrt2e^{-\kappa\tau/8}<\sqrt2,\qquad X_{\rm pre}=8\tau,
\]
\[
 c_* =\min\left\{1,
 \frac{\sqrt2-s_*}{C_f(\alpha_0+1+\sqrt{E_*}+\sqrt{C_D})}\right\},
\]
\[
 X_* =\left(F(X_{\rm pre})+\frac{s_*}{\gamma c_*}+2\log2\right)^2,
 \qquad U_*=\alpha_0+C_BX_*,
\]
\[
 b_* =\sqrt{C_B^2X_*^2+1+C_DX_*+E_*},\qquad
 \beta_* =\frac{c_*}{1+\sqrt{X_*}}>0,\qquad
 S_*=4\tau+\frac{s_*}{\gamma\beta_*^2}.
 \tag{41}
\]
The inequality following (38) shows \(X_{\rm pre}\le X_*\). Choose guard bounds
and the one-step constants by
\[
 U_g=\max\{\alpha_0+1,U_*\}+1,\qquad
 V_g=\max\{2,b_*\}+1,
\]
\[
 J_g=2\sqrt2\sqrt{\overline L}\,\mathcal G(U_g,V_g),\qquad
 H_g=\mathcal H(U_g+1,V_g+1).
 \tag{42}
\]
Finally set
\[
 N_{\rm det}=\left\lceil\max\left\{
 2,\ \tau^{-1/2},\ J_g^{1/2},\ H_g^{2/3},\ \kappa^{1/2},\
 \sqrt{2\gamma}\,V_g,\
 \left(\frac{2C_BU_*\sqrt{\overline L}}{\beta_*}\right)^{1/2}
 \right\}\right\rceil.
 \tag{43}
\]
Every constant in (41)--(43) is finite and is defined using only fixed initial
bounds, activations, and coercivity constants. None uses a trajectory supremum,
a terminal step count, an unknown clock, or a limiting parameter. For
\(n\ge N_{\rm det}\), \(\eta=n^{-2}\) satisfies
\[
 \eta\le\tau,\quad \eta J_g\le1,\quad
 \eta\sqrt nH_g\le1,\quad \eta\kappa\le1,\quad
 2\eta\gamma V_g^2\le1,\quad
 \eta C_BU_*\sqrt{\overline L}\le\beta_*/2.
 \tag{44}
\]
In particular, the Hessian condition is \(n^{-3/2}H_g\le1\), which is a single
width condition, independent of time.

**Deterministic theorem.** Suppose the exact initial canonical parameters satisfy
\[
 \gamma_n\ge\gamma,\qquad \|W^{(2)}_0\|_{\rm op}\le\alpha_0,\qquad
 \frac{\|W^{(3)}_0\|_2}{\sqrt n}\le1,\qquad K_{3,0}\succeq\kappa I_2,
\]
\[
 L_0\le4,\qquad L_0\le2e^{\kappa\tau/4}.
 \tag{45}
\]
For every fixed \(n\ge N_{\rm det}\), all simultaneous updates (5) satisfy the
descent certificate. With
\[
 m=\lceil\tau/\eta\rceil,\qquad t_m=m\eta\in[\tau,2\tau],
\]
the actual node \(m\) has the strict margin
\[
 L_m\le2e^{-\kappa\tau/4}=s_*^2=2-\delta_*,\qquad
 \delta_*=2(1-e^{-\kappa\tau/4})>0.
 \tag{46}
\]
At every node,
\[
 X_k\le X_*,\qquad
 \|W^{(2)}_k-W^{(2)}_0\|_F\le C_BX_*,\qquad
 \|W^{(2)}_k\|_{\rm op}\le U_*,\qquad
 \frac{\|W^{(3)}_k\|_2}{\sqrt n}\le b_*.
 \tag{47}
\]
For \(k\ge m\), the readout norm is at least \(\beta_*\), and
\[
 L_k\le s_*^2(1-2\eta\gamma\beta_*^2)^{k-m}
       \le s_*^2e^{-2\gamma\beta_*^2(t_k-t_m)},
\]
\[
 \sum_{k=0}^\infty\eta\sqrt{L_k}\le S_*,\qquad
 \sum_{k=0}^\infty\eta\sqrt{L_k}
                      \frac{\|W^{(3)}_k\|_2}{\sqrt n}\le X_*.
 \tag{48}
\]
All canonical parameters converge, with zero limiting loss. Section 6 gives
their ordinary-norm total variations and the whole-cell conclusions.

**Proof of the finite initial induction.** At node zero, the guard bounds and
\(L_0\le4\) hold. Suppose the cells ending at node \(k<m\) have been certified.
If \(k>0\), (23), \(t_k\le2\tau\), and (25) give
\[
 \|W^{(2)}_k\|_{\rm op}\le\alpha_0+1<U_g,\qquad b_k\le2<V_g.
\]
These bounds also hold at node zero directly. The old-node gradient bound
therefore places the entire next segment in the larger region of Section 2.
Equations (18)--(20) certify its descent. Only now is its action added to (22).
Since \(t_{k+1}\le t_m\le2\tau\), (23)--(26) apply to the newly certified cell,
including its endpoint. At its old node, \(K_{3,k}\succeq\kappa I_2/4\), so
(27) applies. This proves the induction through cell \(m-1\).

The result is
\[
 L_m\le L_0(1-\eta\kappa/2)^m
      \le L_0e^{-\kappa t_m/2}
      \le2e^{-\kappa\tau/4},
\]
where (44) makes the geometric factor positive. Also \(s_j\le2\), \(b_j\le2\)
for \(j<m\), and hence
\[
 X_m\le4t_m\le8\tau=X_{\rm pre}.
 \tag{49}
\]
No GF trajectory or approximation error was introduced.

**Proof of the all-time induction.** On the certified initial prefix, (30),
(33), \(b_0\le1\), and (49) imply all upper bounds in (47), since
\(X_j\le X_m\le X_{\rm pre}\le X_*\). At node \(m\), the loss margin has been
established; (36) gives \(b_m\ge\beta_*\). This is the base of the second
induction.

Suppose every cell ending at node \(k\ge m\) has been certified and (47) holds
through node \(k\). These upper bounds lie strictly inside the guard bounds.
The current node has loss at most four. Thus the one-step certificate applies
to the entire next segment, proving descent for the actual next node before
any estimate at that new node is assumed. We can now extend the energy sum and
the exact balance through that step.

For each old node \(j=m,\ldots,k\), (36) is already available from the
certified balance and the loss margin. Thus (39) telescopes through the new
increment \(X_{k+1}-X_k\), to give
\[
 F(X_{k+1})\le F(X_m)+\frac{s_m}{\gamma c_*}
             \le F(X_{\rm pre})+\frac{s_*}{\gamma c_*}.
\]
Using \(F(x)\ge\sqrt x-2\log2\) proves \(X_{k+1}\le X_*\). Equations
(30), (33), and (34) then prove the same upper bounds (47) at node \(k+1\),
strictly inside the guard region. Its loss is still at most \(s_*^2\), so (36)
also gives \(b_{k+1}\ge\beta_*\). This closes the induction.

Equivalently, a putative first failing node cannot fail: its old node certifies
its full update segment, after which the clock and balance restore the strict
guard bounds at the candidate node. The short induction was separate and used
only action before the loss margin existed. The width requirement (43) has no
dependence on how far either induction is continued.

For \(k\ge m\), (20) and \(b_k\ge\beta_*\) give the first bound in (48).
The factor \(1-2\eta\gamma\beta_*^2\) lies in \((0,1)\), since (44) holds
and \(\beta_*<V_g\). Summing (21) gives
\[
 \sum_{k=m}^N\eta s_k\le\frac{s_m-s_{N+1}}{\gamma\beta_*^2}
                          \le\frac{s_*}{\gamma\beta_*^2}.
\]
The pre-entry sum is at most \(2t_m\le4\tau\). Taking increasing finite sums
proves the unweighted residual bound in (48). The weighted bound follows from
\(X_k\le X_*\) and monotonicity of \(X_k\). This proves (47)--(48) without
an exchange involving an unproved infinite-time bound.

## 6. Parameter convergence, integrable controls, and complete update cells

The exact equations and the bounds already proved give, at every node,
\[
 \|F^{(2)}_k\|_F\le C_Bs_kb_k,\qquad
 \frac{\|F^{(3)}_k\|_2}{\sqrt n}\le C_BU_*s_k,
\]
\[
 \sqrt{\frac dn}\|F^{(1)}_k\|_F
 \le2\sqrt2 PMU_*s_kb_k.
 \tag{50}
\]
For the last inequality use
\[
 \left\|\phi_1'(z^{(1)}_{a,k})\odot(W^{(2)}_k)^T
       \bigl(W^{(3)}_k\odot\phi_2'(z^{(2)}_{a,k})\bigr)\right\|_2
 \le PMU_*\sqrt n\,b_k
\]
in (5), along with \(\|x_a\|_2=\sqrt d\) and
\(\sum_a|r_{a,k}|\le\sqrt2s_k\). Hence the ordinary-norm total variations obey
\[
 \sum_{k\ge0}\|W^{(2)}_{k+1}-W^{(2)}_k\|_F\le C_BX_*,
\]
\[
 \sum_{k\ge0}\|W^{(3)}_{k+1}-W^{(3)}_k\|_2
                  \le\sqrt n\,C_BU_*S_*,
\]
\[
 \sum_{k\ge0}\|W^{(1)}_{k+1}-W^{(1)}_k\|_F
                  \le\sqrt{\frac nd}\,2\sqrt2 PMU_*X_*.
 \tag{51}
\]
At fixed finite \(n,d\), tails of these convergent nonnegative sums bound
distances between any two late parameter vectors. The coordinates are Cauchy
and have finite limits in Euclidean space. Formula (4) is continuous, and (48)
gives \(L_k\to0\), so the limiting canonical parameters predict exactly
\((1,-1)\).

For each sample, the actual nodal first-coordinate control
\[
 q_{:,a,k}=-2r_{a,k}(W^{(2)}_k)^T
             \bigl(W^{(3)}_k\odot\phi_2'(z^{(2)}_{a,k})\bigr)
\]
satisfies
\[
 \sum_{k\ge0}\eta\frac{\|q_{:,a,k}\|_2}{\sqrt n}
 \le2MU_*X_*.
 \tag{52}
\]
The first-coordinate update is exactly
\[
 z^{(1)}_{j,a,k+1}-z^{(1)}_{j,a,k}
 =\eta\sum_{b=1}^2\frac{x_b^Tx_a}{d}
                 q_{j,b,k}\phi_1'(z^{(1)}_{j,b,k}).
\]
Thus (52) is a discrete integrable-control statement with the old-node
derivative factors that the actual algorithm uses.

For clarity, define \(W^{(\ell)}(t)\) only as the straight interpolation of (5).
This polygon is not asserted to solve an ODE. Its complete-cell bounds are:

* By convexity of the norms, the bounds on \(W^{(2)}-W^{(2)}_0\),
  \(\|W^{(2)}\|_{\rm op}\), and \(\|W^{(3)}\|_2/\sqrt n\) in (47) hold for
  every real \(t\ge0\). The frozen-row inequality (6) holds there exactly.
* For either sample and every real \(t\ge0\),
  \[
  \frac{\|z^{(2)}_a(t)\|_2}{\sqrt n}\le AU_*,\qquad
  \frac{\|\phi_2(z^{(2)}_a(t))\|_2}{\sqrt n}\le MAU_*.
  \tag{53}
  \]
* On \([t_k,t_{k+1}]\), the loss of the interpolated parameters is
  nonincreasing and at most \(L_k\), by (19) and its derivative estimate.
  Therefore
  \[
  \int_0^\infty\sqrt{L(W(t))}\,dt\le S_*.
  \tag{54}
  \]
  It also tends to zero, since the nodal upper bound in (48) tends to zero.
* For \(t\in[t_k,t_{k+1}]\) with \(k\ge m\), the reverse triangle inequality,
  (50), and (44) give
  \[
  \frac{\|W^{(3)}(t)\|_2}{\sqrt n}
  \ge b_k-\eta C_BU_*s_k\ge\beta_*/2.
  \tag{55}
  \]
  This lower bound is established separately; it is not inferred from convexity
  or from lower bounds at the two endpoints.

The continuous weighted clock of this interpolation is not identified with
\(X_k\). Its finite bound, with the interpolation error shown, is
\[
 \int_0^\infty\sqrt{L(W(t))}
                 \frac{\|W^{(3)}(t)\|_2}{\sqrt n}\,dt
 \le X_*+\frac{\eta C_BU_*\sqrt{\overline L}}2 S_*.
 \tag{56}
\]
Indeed, within cell \(k\), its two factors are at most \(s_k\) and
\(b_k+(t-t_k)C_BU_*s_k\). Integrating their product gives
\(\eta s_kb_k+\eta^2C_BU_*s_k^2/2\). Sum these bounds and use
\(\sum_k\eta s_k^2\le\sqrt{\overline L}\sum_k\eta s_k\).

The action bound (23) now holds for all real \(t\ge0\); explicitly,
\[
 \int_0^\infty\left(
 \frac dn\|\dot W^{(1)}(t)\|_F^2
 +\|\dot W^{(2)}(t)\|_F^2
 +\frac{\|\dot W^{(3)}(t)\|_2^2}{n}\right)dt\le2L_0.
 \tag{57}
\]
Derivatives here are the piecewise constant old-node slopes, defined off the
cell endpoints. For an explicit within-cell displacement bound, (50) gives
\[
 \|W^{(2)}(t)-W^{(2)}_k\|_F
       \le\eta C_B\sqrt{\overline L}\,b_*,
\]
\[
 \|W^{(3)}(t)-W^{(3)}_k\|_2
       \le\eta\sqrt n\, C_BU_*\sqrt{\overline L},
\]
\[
 \|W^{(1)}(t)-W^{(1)}_k\|_F
       \le\eta\sqrt{\frac nd}\,2\sqrt2 PMU_*\sqrt{\overline L}\,b_*.
 \tag{58}
\]
Thus the displayed ordinary norms have their actual width factors; the combined
raw displacement is at most
\(2\sqrt2\eta\sqrt{\overline L}\,\mathcal G(U_*,b_*)\).
The total variations of the polygon are exactly the sums in (51). Its parameters
therefore converge to the same limits as the nodes.

## 7. Discharging the assumptions for the prescribed independent initialization

Now use precisely the independent canonical Gaussian initialization
\[
 W^{(1)}_{ij,0}\sim N(0,1/d),\qquad
 W^{(2)}_{ij,0}\sim N(0,1/n),\qquad
 W^{(3)}_{i,0}\sim N(0,n^{-2}),
 \tag{59}
\]
with all entries in all layers independent. In particular the actual random
readout is retained, not replaced by zero.

Let \((Z_1,Z_2)\) be centered Gaussian with covariance
\(\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\). Define
\[
 m_s=\Pr(Z_1\ge R,Z_2\ge R)+\Pr(Z_1\le-R,Z_2\le-R),
\]
\[
 m_o=\Pr(Z_1\ge R,Z_2\le-R)+\Pr(Z_1\le-R,Z_2\ge R),
 \qquad \gamma=A^2\min(m_s,m_o),\qquad \kappa=\gamma/2.
 \tag{60}
\]
Both corner probabilities are positive because \(|\rho|<1\) gives a strictly
positive Gaussian density on every open corner. Thus \(\gamma,\kappa>0\).
Use \(\alpha_0=8\) in all constants (25), (29), and (41)--(43).

Consider the explicit event
\[
 E_n=\left\{
 \frac{N_s}{n}\ge\frac{m_s}{2},\quad
 \frac{N_o}{n}\ge\frac{m_o}{2},\quad
 K_{3,0}\succeq\kappa I_2,\quad
 \|W^{(2)}_0\|_{\rm op}\le8,\quad
 \frac{\|W^{(3)}_0\|_2}{\sqrt n}\le\frac2n
 \right\}.
 \tag{61}
\]
We prove its probability bound rather than assuming an initialization theorem.

**Frozen-row counts.** For each initial first row, its preactivation pair has
exactly the law used in (60), by (1) and (59). Rows are independent. A Bernoulli
count with mean \(nm\) has variance \(nm(1-m)\), and Markov's inequality applied
to its squared centered value gives
\[
 \Pr\left(\frac{N_s}{n}<\frac{m_s}{2}
           \ \text{or}\ \frac{N_o}{n}<\frac{m_o}{2}\right)
 \le\frac4n\left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right).
 \tag{62}
\]
On the complementary event, (6) has \(\gamma_n\ge\gamma\).

**Initial top-feature Gram.** Condition on the entire first-layer realization
and let \(H=H^{(1)}_0\), \(G=H^TH/n\). The row pairs of
\(W^{(2)}_0H\) are then independent centered Gaussians with covariance \(G\).
On the count event, \(G\succeq\gamma I_2\) and \(G_{aa}\le A^2\).
For one row pair \(Z\), write
\(Z=U+\sqrt\gamma\,\xi\), with \(U\) centered Gaussian of covariance
\(G-\gamma I_2\) and \(\xi\) having independent standard normal coordinates,
independently of \(U\). The positive semidefinite covariance permits this
construction by diagonalizing its two-dimensional symmetric matrix.

For any scalar random variable \(T\) of finite variance and an independent copy
\(T'\), the lower derivative bound in (3) gives
\[
 \operatorname{Var}(\phi_2(T))
 =\tfrac12\mathbb E(\phi_2(T)-\phi_2(T'))^2
 \ge\tfrac12\mathbb E(T-T')^2=\operatorname{Var}(T).
\]
Conditional on \(U\), the coordinates of \(V=\phi_2(Z)\) are independent and
each has variance at least \(\gamma\). For any \(v\in\mathbb R^2\), therefore,
\[
 \mathbb E[(v^TV)^2\mid H]
 \ge\mathbb E[\operatorname{Var}(v^TV\mid U,H)\mid H]
 \ge\gamma\|v\|_2^2.
 \tag{63}
\]
This argument does not require nonnegative \(\rho\).

A scalar centered Gaussian of variance \(\sigma^2\) has fourth moment
\(3\sigma^4\), obtained by two integrations by parts in its density (and also
valid at zero variance). Cauchy--Schwarz and (3) then yield
\[
 \mathbb E[V_a^2V_b^2\mid H]
 \le M^4\sqrt{\mathbb E[Z_a^4\mid H]\mathbb E[Z_b^4\mid H]}
 \le3M^4A^4.
\]
Using independence of the \(n\) rows in the empirical Gram,
\[
 \mathbb E\left[
 \left\|K_{3,0}-\mathbb E[VV^T\mid H]\right\|_F^2\mid H\right]
 \le\frac{12M^4A^4}{n}.
\]
If the norm inside this expectation is at most \(\gamma/2\), (63) implies
\(K_{3,0}\succeq\gamma I_2/2\). Markov's inequality therefore gives
\[
 \Pr(K_{3,0}\not\succeq\kappa I_2\mid W^{(1)}_0)
 \le\frac{48M^4A^4}{n\gamma^2}
 \quad\text{on the count event}.
 \tag{64}
\]

**Initial second-layer operator norm.** A Euclidean \(1/4\)-net of the unit
sphere can have at most \(9^n\) points: choose a maximal separated set, and
compare the volumes of its disjoint radius-\(1/8\) balls with the containing
radius-\(9/8\) ball. Maximality makes it a net. Approximating both unit vectors
in a bilinear form gives
\[
 \|W^{(2)}_0\|_{\rm op}
 \le2\max_{u,v\text{ in the net}}|u^TW^{(2)}_0v|.
\]
For each fixed pair, the bilinear form is \(N(0,1/n)\). Completing the square
gives its exponential moment \(e^{t^2/(2n)}\); Markov's inequality with the
optimizing \(t\), and the two tails, bound the probability of absolute value
exceeding 4 by \(2e^{-8n}\). A union bound over the net pairs proves
\[
 \Pr(\|W^{(2)}_0\|_{\rm op}>8)
 \le2e^{-(8-2\log9)n}.
 \tag{65}
\]

**Initial readout norm.** Write \(W^{(3)}_{i,0}=\xi_i/n\). Then
\(b_0^2=n^{-3}\sum_i\xi_i^2\). Direct Gaussian integration gives
\(\mathbb E e^{\xi_i^2/4}=\sqrt2\), so Markov's inequality yields
\[
 \Pr(b_0>2/n)
 =\Pr\left(\sum_i\xi_i^2>4n\right)
 \le e^{-(1-\frac12\log2)n}.
 \tag{66}
\]

Integrate (64) only over the count event, and combine (62), (65), and (66)
by a union bound. This proves
\[
 \Pr(E_n)\ge\max\{0,1-p_n\},
\]
\[
 p_n=\frac4n\left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right)
       +\frac{48M^4A^4}{n\gamma^2}
       +2e^{-(8-2\log9)n}
       +e^{-(1-\frac12\log2)n}.
 \tag{67}
\]
No independence between the two second-layer events in (61) was assumed.

**Initial loss and the final width threshold.** Put
\[
 q_0=2MA\alpha_0=16MA,
\]
\[
 N_*=\left\lceil\max\left\{
 N_{\rm det},\quad \frac{q_0}{\sqrt2-1},\quad
 \frac{q_0}{e^{\kappa\tau/8}-1}
 \right\}\right\rceil.
 \tag{68}
\]
This is finite. On \(E_n\), (35) at node zero gives
\[
 \|f_0\|_2\le\frac{2\sqrt2 MA\alpha_0}{n}
                   =\frac{\sqrt2 q_0}{n},\qquad
 L_0\le2(1+q_0/n)^2,
\]
\[
 |L_0-2|\le\frac{4q_0}{n}+\frac{2q_0^2}{n^2}.
 \tag{69}
\]
For \(n\ge N_*\), these bounds imply both \(L_0\le4\) and
\(L_0\le2e^{\kappa\tau/4}\); also \(b_0\le2/n\le1\). Thus all hypotheses
(45) of the deterministic theorem hold on \(E_n\).

**Canonical all-time theorem.** For every fixed \(\rho\in(-1,1)\), the fixed
activations above, and any fixed integer \(n\ge N_*\), the simultaneous
canonical RawGD updates (5) with initialization (59) satisfy (46)--(58) on the
event (61), of probability at least \(\max\{0,1-p_n\}\). In particular they
reach a fixed strict loss margin by the actual node time
\(t_m\in[\tau,\tau+\eta]\), have finite weighted and unweighted residual sums,
and converge in all parameters to zero loss.

The constants \(\tau,\delta_*,X_*,U_*,b_*,\beta_*,S_*,N_*\) depend only on
the fixed activations and the fixed interior correlation. They do not depend on
the Gaussian realization inside the event, the width beyond its threshold,
the input dimension, or the number of GD steps. The probability bound tends to
one as \(n\to\infty\); the optimization and convergence assertions themselves
hold at each qualifying finite width.

## 8. Scope of the result

The proof supplies actual descent, actual entry below loss 2, exact preservation
of the frozen rows, a summed Euler balance error, time-uniform upper parameter
bounds, finite residual sums, and parameter convergence for the stated event.
The raw-coordinate Hessian bound is of order \(\sqrt n\), not order one.
The top activation and readout coordinates are controlled through the explicit
ordinary-norm factors above; no width-independent maximum-readout bound is used.

No optimization conclusion is claimed for draws outside (61), although every
finite algebraic update remains defined. There is no assertion of almost-sure
optimization for every fixed width. The constants need not stay bounded as
\(\rho\) approaches an endpoint, and neither endpoint is included. No
mean-field limit, mean-field uniqueness, propagation theorem, nonlazy behavior,
or persistent nonlinear-learning conclusion is inferred.
