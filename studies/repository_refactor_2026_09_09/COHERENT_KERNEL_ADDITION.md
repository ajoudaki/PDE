## 15. Global training flow for a coherent dense residual kernel

This section treats a separate residual architecture: its dense, untied
trunk has the coherent normalization \(W/n\), and its input features and
readout are fixed and bounded. The continuum state is an actual kernel on
a neuron label space. It is not the Gaussian \(W/\sqrt n\) construction,
and it is not the scalar particle model. We prove existence and uniqueness
of the kernel training flow, including its exact gradient and energy
identity. No width or depth limit is assumed in this existence theorem.

### 15.1 Finite calculus and the metric being continued

Here \(L\) counts residual blocks, \(n\) is their common width, and
\(m\) is a fixed positive finite number of samples. Use the activation
and loss regularity specified in Section 15.3. Fix \(\alpha>0\). For fixed
input vectors \(x_a^{[n]}\in\mathbb R^n\) and a fixed readout
\(c^{[n]}\in\mathbb R^n\), set

\[
h_a^{(0)}=x_a^{[n]},\qquad
z_a^{(\ell)}=\frac{W_\ell h_a^{(\ell-1)}}n,\qquad
h_a^{(\ell)}=h_a^{(\ell-1)}+
\frac{\alpha}{L}\phi(z_a^{(\ell)}),\qquad
f_{n,a}=\frac{(c^{[n]})^T h_a^{(L)}}n.
\tag{15.1}
\]

All \(Ln^2\) trunk entries are independent parameter coordinates; no
diagonality, low rank, symmetry, or tying of different blocks is imposed.
Only these trunk matrices are trained. Let
\(\mathcal E_n=\mathcal R(f_{n,1},\ldots,f_{n,m})\), and write
\(q_a=\partial_a\mathcal R(f_n)\). For the library's mean full squared
loss, \(q_a=2r_{n,a}/m\), where \(r_{n,a}=f_{n,a}-y_a\). The mean half
squared loss instead has \(q_a=r_{n,a}/m\); at the same mobility it runs
at half the physical speed.

Use the residual-free adjoint

\[
p_a^{(L)}=c^{[n]},\qquad
b_a^{(\ell)}=p_a^{(\ell)}\odot\phi'(z_a^{(\ell)}),\qquad
p_a^{(\ell-1)}=p_a^{(\ell)}+
\frac{\alpha}{Ln}W_\ell^T b_a^{(\ell)}.
\tag{15.2}
\]

Indeed \(p_a^{(\ell)}=n\,\partial f_{n,a}/\partial h_a^{(\ell)}\),
so the transpose in (15.2) is that of the same forward matrix. Varying
one matrix gives

\[
\nabla_{W_\ell}f_{n,a}
=\frac{\alpha}{Ln^2}b_a^{(\ell)}(h_a^{(\ell-1)})^T,
\qquad
\nabla_{W_\ell}\mathcal E_n
=\frac{\alpha}{Ln^2}\sum_{a=1}^m
q_a b_a^{(\ell)}(h_a^{(\ell-1)})^T.
\tag{15.3}
\]

Thus mobility \(Ln^2\) for every raw matrix gives

\[
\dot W_\ell=-\alpha\sum_{a=1}^m
q_a b_a^{(\ell)}(h_a^{(\ell-1)})^T,
\qquad
\frac{d\mathcal E_n}{dt}
=-\frac1{Ln^2}\sum_{\ell=1}^L\|\dot W_\ell\|_F^2.
\tag{15.4}
\]

These are exact finite identities. In particular, full-batch dissipation
uses the squared norm of the sum in (15.4). If
\(\mathcal R\ge E_*\), integration and Cauchy--Schwarz give

\[
\left(\frac1{Ln^2}\sum_\ell
\|W_\ell(t)-W_\ell(0)\|_F^2\right)^{1/2}
\le\sqrt{t\,[\mathcal E_n(0)-E_*]}.
\tag{15.5}
\]

At fixed \(n,L\), the right side bounds every parameter displacement
on a finite time interval. The locally Lipschitz finite vector field
therefore extends globally. This observation makes no assertion uniform
in \(n,L\).

To identify the continuum metric, embed a matrix as a kernel constant on
the \(n^2\) equal neuron cells, and embed the blocks on the \(L\) equal
depth cells. Its squared \(L^2(ds\,du\,dv)\) norm is exactly
\((Ln^2)^{-1}\sum_\ell\|W_\ell\|_F^2\). The corresponding integral
operator acts as \(W_\ell/n\), and the integral readout as
\((c^{[n]})^Th/n\). This identifies the normalization and metric; it
does not prove that discretized training converges.

### 15.2 A strong kernel carrier

Put \(U=(0,1)\), with Lebesgue measure. For a measurable real kernel
\(k\) on \(U^2\), define its row and column bounds by

\[
\rho(k)=\operatorname*{ess\,sup}_{u\in U}
\left(\int_U|k(u,v)|^2\,dv\right)^{1/2},\qquad
\chi(k)=\operatorname*{ess\,sup}_{v\in U}
\left(\int_U|k(u,v)|^2\,du\right)^{1/2}.
\tag{15.6}
\]

Let \(\mathcal K\) be the space of such kernels, modulo almost-everywhere
equality, for which both bounds are finite, with norm

\[
\|k\|_{\mathcal K}=
\bigl(\rho(k)^2+\chi(k)^2\bigr)^{1/2}.
\]

This is a Banach space. To see completeness, a Cauchy sequence in this
norm converges in each of the Banach mixed spaces
\(L^\infty_u(L^2_v)\) and \(L^\infty_v(L^2_u)\). Both limits have the
same \(L^2(U^2)\) representative, since both embeddings into that space
are continuous. Hence they define one element of \(\mathcal K\), and
convergence holds in both components of its norm.

The depth carrier and the energy space are

\[
\mathbb K=L^2\bigl((0,1)_s;\mathcal K\bigr),\qquad
\mathbb H=L^2\bigl((0,1)_s\times U^2\bigr),\qquad
\|w\|_{\mathbb K}^2=
\int_0^1[\rho(w(s))^2+\chi(w(s))^2]\,ds.
\tag{15.7}
\]

The first space is the **Bochner** \(L^2\) space: its elements are
strongly measurable \(\mathcal K\)-valued depth profiles, represented
by almost-everywhere limits of simple profiles, with the displayed finite
norm. Joint scalar measurability of \(w(s,u,v)\) and the displayed norm
alone are not substituted for this requirement. Bochner \(L^2\) of a
Banach space is complete: for example, a subsequence of a Cauchy sequence
whose successive \(L^2\) differences have summable norms has an
almost-everywhere absolutely convergent series of differences, yielding
a strongly measurable limit and convergence in \(L^2\). There is a
continuous embedding \(\mathbb K\hookrightarrow\mathbb H\).

For \(g\in L^2(U)\), define

\[
(T_kg)(u)=\int_Uk(u,v)g(v)\,dv,\qquad
(T_k^*g)(v)=\int_Uk(u,v)g(u)\,du.
\]

Cauchy--Schwarz and Fubini give

\[
\|T_kg\|_\infty\le\rho(k)\|g\|_2,\qquad
\|T_k^*g\|_\infty\le\chi(k)\|g\|_2,\qquad
\|T_k\|_{2\to2}\le\|k\|_{L^2(U^2)}
\le\min\{\rho(k),\chi(k)\}.
\tag{15.8}
\]

Here \(T_k^*\) is the actual Hilbert-space adjoint of \(T_k\).
For bounded functions \(b,x\), the kernel
\((b\otimes x)(u,v)=b(u)x(v)\) satisfies

\[
\rho(b\otimes x)=\|b\|_\infty\|x\|_2,
\qquad
\chi(b\otimes x)=\|x\|_\infty\|b\|_2.
\tag{15.9}
\]

The actions \(\mathcal K\times L^\infty\to L^\infty\) in (15.8)
and the outer product \(L^\infty\times L^\infty\to\mathcal K\) in
(15.9) are continuous bilinear maps. They therefore preserve strong
measurability when applied to strongly measurable arguments: approximate
the arguments by simple functions and use continuity. These facts will
ensure that all depth and training integrals below are Bochner integrals.

### 15.3 The global theorem

Assume throughout this section that

* \(1\le m<\infty\), \(\alpha>0\), and the input profiles
  \(X_a^0\in L^\infty(U)\) and readout \(c\in L^\infty(U)\) are
  fixed and untrained;
* \(\phi\in C_b^2(\mathbb R)\): the function and its first two
  continuous derivatives are bounded; write
  \(M_j=\|\phi^{(j)}\|_\infty\), \(j=0,1,2\);
* \(\mathcal R\in C^2(\mathbb R^m)\) and
  \(\mathcal R\ge E_*\) for some finite real \(E_*\);
* \(w_0\in\mathbb K\).

The profiles \(X_a^0\) are the inputs of this kernel model. A fixed
bounded feature map applied to finite-dimensional data is one way to
specify them. No orthogonality, normalization, or nonsingularity of the
sample Gram matrix is assumed, and there is no population-of-data limit.
In particular, arbitrary fixed labels are allowed in squared loss.

At each training state \(w\), solve the depth equations

\[
\begin{aligned}
\partial_sX_a(s)&=\alpha\phi(Z_a(s)),&
Z_a(s)&=T_{w(s)}X_a(s),&X_a(0)&=X_a^0,\\
-\partial_sP_a(s)&=\alpha T_{w(s)}^*B_a(s),&
B_a(s)&=P_a(s)\phi'(Z_a(s)),&P_a(1)&=c.
\end{aligned}
\tag{15.10}
\]

Products and activations of functions on \(U\) are pointwise. Define

\[
f_a(w)=\int_Uc(u)X_a(1,u)\,du,\quad
q_a(w)=\partial_a\mathcal R(f(w)),\quad
\mathcal E(w)=\mathcal R(f(w)),
\]

\[
\mathcal G(w)(s)=\alpha\sum_{a=1}^m
q_a(w)B_a(s)\otimes X_a(s).
\tag{15.11}
\]

The adjoint \(P_a\) is residual-free: all loss factors occur in
\(q_a\). The training equation is

\[
\partial_tw(t)=-\mathcal G(w(t)),\qquad w(0)=w_0.
\tag{15.12}
\]

**Theorem 15.1 (global strong kernel flow).** Under the stated assumptions,
(15.10)--(15.12) have a unique solution
\(w\in C^1([0,\infty);\mathbb K)\). For each \(w\in\mathbb K\),
the forward and adjoint depth solutions in (15.10) are unique Bochner
absolutely continuous \(L^\infty(U)\)-valued curves, with derivatives
in \(L^1((0,1);L^\infty(U))\). The map
\(\mathcal G:\mathbb K\to\mathbb K\) is Lipschitz on each bounded
ball. The loss is Fréchet differentiable on \(\mathbb K\), with

\[
D\mathcal E(w)[v]=\langle\mathcal G(w),v\rangle_{\mathbb H}
\quad(v\in\mathbb K),\qquad
\frac{d}{dt}\mathcal E(w(t))
=-\|\partial_tw(t)\|_{\mathbb H}^2.
\tag{15.13}
\]

Consequently, for every finite \(T\),

\[
\int_0^T\|\partial_tw(t)\|_{\mathbb H}^2\,dt
=\mathcal E(w_0)-\mathcal E(w(T))
\le\mathcal E(w_0)-E_*,
\qquad
\|w(t)-w_0\|_{\mathbb H}
\le\sqrt{t\,[\mathcal E(w_0)-E_*]}.
\tag{15.14}
\]

The solution can restart uniquely from every point of \(\mathbb K\),
with the fixed data, readout, activation, and loss retained. Thus its
autonomous solution maps form a semigroup on this carrier. The theorem
does not assert well-posedness for arbitrary initial kernels in
\(\mathbb H\) alone.

**Proof: depth existence and estimates.** Write
\(C_X=\max_a\|X_a^0\|_\infty+\alpha M_0\). For any fixed
\(w\in\mathbb K\), the forward integral equation is a contraction
on a depth interval on which
\(\alpha M_1\int\rho(w(s))\,ds<1\), since \(U\) has measure one
and (15.8) applies. The integral of \(\rho(w)\) is finite, so finitely
many such intervals cover \([0,1]\). Boundedness of \(\phi\) gives,
at every depth,

\[
\|X_a(s)\|_\infty\le C_X.
\tag{15.15}
\]

The resulting curve is continuous into \(L^\infty\); its integrand is
strongly measurable by (15.8) and the Lipschitz Nemytskii map for
\(\phi\), and is bounded by \(\alpha M_0\). It is therefore a
Bochner absolutely continuous solution. The same local contraction
argument backwards in depth constructs \(P_a\), now with contraction
constant \(\alpha M_1\int\chi(w(s))\,ds\). It yields

\[
\sup_s\|P_a(s)\|_\infty
\le\|c\|_\infty
\exp\!\left(\alpha M_1\int_0^1\chi(w(s))\,ds\right).
\tag{15.16}
\]

Uniqueness follows from the same integral inequalities and Gronwall.
All arguments remain in \(L^\infty\); the adjoint integrand has an
integrable norm, so it too gives the asserted Bochner derivative.
In contrast to the bounded states and adjoints, the local field has only
the depth bound

\[
\|Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(w)\|_{L^2_s}.
\tag{15.17}
\]

An essential supremum of \(Z_a\) over depth is not required.

**Proof: local Lipschitzness in the strong carrier.** Fix \(A<\infty\)
and two kernels \(w,\widetilde w\) with carrier norms at most \(A\).
In this paragraph constants denoted \(C_A\) depend only on \(A\) and
the fixed problem data. Write \(d=w-\widetilde w\), and use a tilde
for the depth fields of \(\widetilde w\). Subtracting the forward
integral equations, applying (15.8), and then Gronwall gives

\[
\sup_s\|X_a(s)-\widetilde X_a(s)\|_\infty
\le C_A\|d\|_{\mathbb K}.
\tag{15.18}
\]

For completeness, the two terms in the integral inequality are
\(\alpha M_1\rho(w(s))\|X_a-\widetilde X_a\|_\infty\) and
\(\alpha M_1C_X\rho(d(s))\). Their depth integrals are controlled
by the \(L^2\) row bounds in (15.7). Hence

\[
\|Z_a-\widetilde Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(d)\|_{L^2_s}
+\|\rho(w)\|_{L^2_s}
\sup_s\|X_a-\widetilde X_a\|_\infty
\le C_A\|d\|_{\mathbb K}.
\tag{15.19}
\]

To compare adjoints, expand the difference of their integrands as

\[
\begin{split}
T_w^*B_a-T_{\widetilde w}^*\widetilde B_a
={}&T_w^*\bigl(\phi'(Z_a)(P_a-\widetilde P_a)\bigr)\\
&+T_w^*\bigl(\widetilde P_a
 [\phi'(Z_a)-\phi'(\widetilde Z_a)]\bigr)
+T_d^*\widetilde B_a.
\end{split}
\tag{15.20}
\]

The first term has \(L^\infty\) norm at most
\(M_1\chi(w)\|P_a-\widetilde P_a\|_\infty\). By (15.16), the
second term is bounded by
\(C_A M_2\chi(w)\|Z_a-\widetilde Z_a\|_\infty\), whose depth
integral is controlled by Cauchy--Schwarz and (15.19). The third term
is bounded by \(C_A M_1\chi(d)\). Backward Gronwall therefore gives

\[
\sup_s\|P_a-\widetilde P_a\|_\infty
+\|B_a-\widetilde B_a\|_{L^2_sL^\infty_u}
\le C_A\|d\|_{\mathbb K}.
\tag{15.21}
\]

For the second term in (15.21), use
\(B_a-\widetilde B_a
=\phi'(Z_a)(P_a-\widetilde P_a)
+\widetilde P_a[\phi'(Z_a)-\phi'(\widetilde Z_a)]\).
This estimate uses two square-integrable depth factors in (15.20),
not a bound on the maximum local field over depth.

All outputs lie in the fixed compact cube
\([-\|c\|_1C_X,\|c\|_1C_X]^m\). The gradient and Hessian of
\(\mathcal R\) are bounded there. Equation (15.18) thus also bounds
\(|q(w)-q(\widetilde w)|\) by \(C_A\|d\|_{\mathbb K}\).
For each sample, the outer-product difference in (15.11) expands as
\[
q_aB_a\otimes X_a-\widetilde q_a\widetilde B_a\otimes\widetilde X_a
=(q_a-\widetilde q_a)B_a\otimes X_a
+\widetilde q_a(B_a-\widetilde B_a)\otimes X_a
+\widetilde q_a\widetilde B_a\otimes(X_a-\widetilde X_a).
\]
By (15.9), \(\|b\otimes x\|_{\mathcal K}
\le\sqrt2\|b\|_\infty\|x\|_\infty\). Applying this inequality
pointwise in depth and then taking its \(L^2\) norm, using (15.15),
(15.16), (15.18), and (15.21), proves

\[
\|\mathcal G(w)\|_{\mathbb K}\le C_A,\qquad
\|\mathcal G(w)-\mathcal G(\widetilde w)\|_{\mathbb K}
\le C_A\|w-\widetilde w\|_{\mathbb K}.
\tag{15.22}
\]

Strong measurability of \(\mathcal G(w)(s)\) follows from the
continuous bilinear maps following (15.9) and from strong measurability
of \(X_a,P_a,Z_a\) as \(L^\infty\)-valued profiles. In particular
(15.22) concerns the Bochner carrier itself.

The training integral map
\(v(t)\mapsto w_0-\int_0^t\mathcal G(v(\tau))\,d\tau\)
is a contraction on a sufficiently short interval in a closed ball of
\(C([0,\varepsilon];\mathbb K)\): choose \(\varepsilon\) so that
the first bound in (15.22) keeps the image in the ball and the second
makes the contraction constant less than one. This constructs a unique
local \(C^1\) solution and, by successive restarts, a unique maximal
solution on \([0,T_*)\).

**Proof: differentiation and the exact gradient.** Fix \(w\in\mathbb K\)
and a variation \(v\in\mathbb K\). The proposed derivative of the
forward field is the unique solution of

\[
\partial_sY_a=\alpha\phi'(Z_a)
  (T_wY_a+T_vX_a),\qquad Y_a(0)=0.
\tag{15.23}
\]

The forward contraction argument, or its linear integral inequality,
shows that \(v\mapsto Y_a\) is bounded and linear from \(\mathbb K\)
to \(C([0,1];L^\infty(U))\). We verify that it is the Fréchet
derivative, since only a depth \(L^2\) bound for the local field is
available. Let \(e_a=X_a(w+v)-X_a(w)\) and
\(\zeta_a=Z_a(w+v)-Z_a(w)\). On a fixed ball, (15.18)--(15.19) give
\(\|e_a\|_{C_sL^\infty_u}=O(\|v\|_{\mathbb K})\) and
\(\|\zeta_a\|_{L^2_sL^\infty_u}=O(\|v\|_{\mathbb K})\).
Taylor's theorem gives the pointwise remainder

\[
|\phi(Z_a+\zeta_a)-\phi(Z_a)-\phi'(Z_a)\zeta_a|
\le\frac{M_2}{2}|\zeta_a|^2.
\]

Since
\(\zeta_a=T_we_a+T_vX_a+T_ve_a\), subtraction of (15.23)
shows that \(e_a-Y_a\) solves the same linear homogeneous integral
equation as \(Y_a\), with forcing equal to
\(\alpha\phi'(Z_a)T_ve_a\) plus the Taylor remainder. The integral
of the forcing norm is at most

\[
\alpha M_1\|\rho(v)\|_{L^1_s}\|e_a\|_{C_sL^\infty_u}
+\frac{\alpha M_2}{2}
\|\zeta_a\|_{L^2_sL^\infty_u}^2
=O(\|v\|_{\mathbb K}^2).
\]

Gronwall then proves
\(\|e_a-Y_a\|_{C_sL^\infty_u}=O(\|v\|_{\mathbb K}^2)\),
which establishes the asserted Fréchet derivative.

Both \(P_a\) and \(Y_a\) are absolutely continuous into \(L^2(U)\).
The product rule for their pairing is valid: their derivatives have
integrable \(L^2\) norms, and the curves have bounded \(L^2\) norms.
Using the adjoint of the same operator in (15.10), the homogeneous
terms cancel and leave

\[
\frac{d}{ds}\langle P_a,Y_a\rangle_{L^2(U)}
=\alpha\langle B_a,T_vX_a\rangle_{L^2(U)}.
\]

Integrating, using \(Y_a(0)=0\) and \(P_a(1)=c\), and applying
Fubini gives

\[
Df_a(w)[v]
=\alpha\int_0^1\langle B_a(s)\otimes X_a(s),v(s)\rangle_{L^2(U^2)}\,ds.
\tag{15.24}
\]

All terms are integrable by the preceding bounds. The finite-dimensional
chain rule for \(\mathcal R\) proves the first identity in (15.13).
The representer \(\mathcal G(w)\) belongs to \(\mathbb K\subset\mathbb H\),
and (15.22) makes the derivative continuous. Thus it is precisely the
gradient in the \(\mathbb H\) pairing, for the functional defined on
the strong carrier. This statement does not extend the functional or its
Fréchet differentiability to an open set of bare \(\mathbb H\).
Along the local \(C^1\) training curve, the chain rule and (15.12)
now yield the energy identity in (15.13). Its integral and
Cauchy--Schwarz give (15.14) on every interval of local existence.

**Proof: global continuation in the strong carrier.** Fix a finite
\(T>0\), and consider \(0\le t<\min\{T,T_*\}\). All constants in
this paragraph are independent of \(t\) in that interval. Define

\[
D=\mathcal E(w_0)-E_*\ge0,\qquad
H_T=\|w_0\|_{\mathbb H}+\sqrt{TD},\qquad
Q=\max_{z\in[-\|c\|_1C_X,\|c\|_1C_X]^m}\max_a|\partial_a\mathcal R(z)|.
\tag{15.25}
\]

Equations (15.14)--(15.15) give
\(\|w(t)\|_{\mathbb H}\le H_T\) and \(|q_a(t)|\le Q\).
Using the \(L^2\)-operator bound in (15.8) in the backward equation,
and then Gronwall and Cauchy--Schwarz in depth, gives

\[
\sup_s\|P_a(s,t)\|_2
\le\|c\|_2
\exp\!\left(\alpha M_1\int_0^1\|w(s,t)\|_{L^2(U^2)}\,ds\right)
\le\|c\|_2e^{\alpha M_1H_T}=:P_{2,T}.
\tag{15.26}
\]

Set
\(C_w(t)=\|\chi(w(\cdot,t))\|_{L^2_s}\) and
\(R_w(t)=\|\rho(w(\cdot,t))\|_{L^2_s}\). The column estimate
in (15.9) now closes without an \(L^\infty\) adjoint bound:

\[
\chi(\partial_tw(s,t))
\le\alpha\sum_a|q_a(t)|\|X_a(s,t)\|_\infty\|B_a(s,t)\|_2
\le\alpha mQ C_XM_1P_{2,T}=:A_T.
\]

Taking the depth \(L^2\) norm and integrating in training time, using
the triangle inequality for the column seminorm, yields

\[
C_w(t)\le C_w(0)+A_Tt.
\tag{15.27}
\]

Next integrate the backward equation directly in \(L^\infty\),
using its column operator bound and (15.26):

\[
\sup_s\|P_a(s,t)\|_\infty
\le\|c\|_\infty+
\alpha M_1P_{2,T}\int_0^1\chi(w(s,t))\,ds
\le\|c\|_\infty+
\alpha M_1P_{2,T}[C_w(0)+A_Tt].
\tag{15.28}
\]

Finally (15.9) gives

\[
\rho(\partial_tw(s,t))
\le\alpha mQM_1C_X
\bigl(\|c\|_\infty+\alpha M_1P_{2,T}[C_w(0)+A_Tt]\bigr)
=:B_{0,T}+B_{1,T}t.
\]

Consequently,

\[
R_w(t)\le R_w(0)+B_{0,T}t+\tfrac12B_{1,T}t^2.
\tag{15.29}
\]

Equations (15.27) and (15.29) bound the full \(\mathbb K\) norm on
every finite interval of existence. This separate argument is necessary:
the kernels \(k_N(u,v)=\sqrt N\,\mathbf1_{\{u<1/N\}}\) have
\(\|k_N\|_2=1\) but \(\rho(k_N)=\sqrt N\), so an energy bound
alone would not control the carrier.

If \(T_*<\infty\), take \(T=T_*\) in these bounds. The first estimate
in (15.22) then bounds \(\|\partial_tw\|_{\mathbb K}\) uniformly
on \([0,T_*)\). Hence \(w(t)\) is Cauchy in the Banach carrier as
\(t\uparrow T_*\), and has a limit there. Local existence from that
limit extends the solution past \(T_*\), a contradiction. Thus
\(T_*=\infty\). Local uniqueness at each restart proves global
uniqueness and the semigroup assertion. This completes the proof.

### 15.4 What the theorem supplies

The theorem applies, in particular, to \(\phi=\tanh\), to arbitrary
fixed bounded input profiles and readout, and to every initial coherent
kernel in the Bochner carrier (15.7). It supplies a global autonomous
training flow in physical time, an exact loss gradient, and the exact
energy law. The state remains an infinite-dimensional depth-indexed
kernel; no finite scalar closure or Gaussian initialization is imposed.

The bounded activation is material to the uniform forward bound, compact
output set, and ordered continuation proof. The result does not
automatically extend to ReLU, to trained endpoints, or to other metrics
and clocks. Nor does the energy identity by itself imply fitting,
nonzero feature motion, a training-time limit, or a finite-width
approximation theorem.

In particular, adding microscopic centered Gaussian matrices to a finite
coherent initialization raises a separate discrete-to-continuum problem.
The present proof asserts no noisy joint width/depth convergence rate,
no raw-kernel convergence for such noise, and no maximum-over-depth
control of local preactivations. It also makes no assertion about the
surviving Gaussian bulk at the different \(W/\sqrt n\) normalization.
