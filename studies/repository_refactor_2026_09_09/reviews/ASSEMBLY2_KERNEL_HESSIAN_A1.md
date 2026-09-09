**CLEAN overall.** Both independent candidates are **CLEAN**, including hessian Sections 14.6–14.7. I found no mathematical correction required under their stated assumptions and scopes.

The coherent candidate contains a complete strong-carrier global-existence proof. The Hessian candidate contains both the reached deterministic obstruction and the intrinsic-volume results; its projection discussion correctly stops short of conclusions that those results do not establish.

**Read and hash ledger.** I read every line of the four permitted mathematical inputs, with this coverage:

| Input | Lines read | Bytes | Reading coverage |
|---|---:|---:|---|
| [coherent.md](/tmp/pde_assembly2_kernel_hessian_r2/coherent.md) | 589 | 20,170 | 1–220, 221–430, 431–589 |
| [hessian.md](/tmp/pde_assembly2_kernel_hessian_r2/hessian.md) | 985 | 37,284 | 1–250, 251–490, 491–740, 741–985 |
| [NOTATION.md](/tmp/pde_assembly2_kernel_hessian_r2/NOTATION.md) | 98 | 5,110 | 1–98 |
| [INPUTS.json](/tmp/pde_assembly2_kernel_hessian_r2/INPUTS.json) | 17 | 429 | 1–17 |

The following SHA-256 values were identical before and after the review:

```text
coherent.md
19c267a56658d6980ed5bd4957d2db9fda5f7178c4eb7024dde961c285a8fd53

hessian.md
1dbf61698ef88e716a9bf1ef11b6d5ded2d21b321f5f50b9d1a4fba89fa9bbf1

NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b

INPUTS.json
728635dc5fd3b0e39ff2883945129493dafebf14cf0f35635a2fedd2860b192c
```

All three manifest entries match their files’ hashes, byte counts, and line counts. `INPUTS.json` has no self-hash entry; its final hash matches the independently recorded initial hash.

I also personally read the complete required instruction files:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`
- `/etc/codex/skills/investigate-conjectures/SKILL.md`
- Its `references/research-contract.md`
- Its `references/evidence-ledger.md`
- Its `references/adversarial-audit.md`

No other mathematical source, checkout, history, prior verdict, packet, or task was inspected. No delegation, training, research experiment, or file modification occurred.

**Assumptions and notation contract.** The two architectures remain explicitly distinct.

For coherent.md, the assumptions are exactly: finite \(m\ge1\); \(\alpha>0\); fixed, untrained \(X_a^0,c\in L^\infty(0,1)\); \(\phi\in C_b^2(\mathbb R)\); a globally lower-bounded \(\mathcal R\in C^2(\mathbb R^m)\); and \(w_0\) in the specified strong Bochner carrier. The inputs need no Gram-matrix normalization or nondegeneracy. Arbitrary finite labels are allowed through the loss. The finite trunk retains \(W/n\), residual increments \(\alpha/L\), and fixed endpoints.

For hessian.md, the architecture has three hidden layers, one datum \(d=m=1\), \(x=y=1\), activation \(\arctan\), full squared loss \((f_n-1)^2\), and stored mobilities \((n,1,1,n)\). Its activation is smooth, so all third derivatives used in the material-Hessian calculation exist. The counterexample requires \(\beta,\gamma>0\), sufficiently small fixed \(\varepsilon>0\), and even \(n\ge4\). Section 14.6 first allows arbitrary finite deterministic parameters; its expectation statements then impose exactly the independent Gaussian initialization in (14.26).

These declarations are consistent with NOTATION.md. In particular, residuals remain outside backpropagated output derivatives; normalized pairings and matrix-coordinate factors remain explicit; the residual architecture expressly gives its own meaning to \(L\); and no result transfers initialization assumptions between the candidates.

**Coherent §15.1: finite calculus, metric, clock, and finite continuation — CLEAN.** Varying the \(\ell\)-th residual block gives
\[
dh_a^{(\ell)}
=\frac{\alpha}{Ln}\operatorname{diag}(\phi'(z_a^{(\ell)}))
\,dW_\ell h_a^{(\ell-1)}.
\]
Since the adjoint is \(p_a^{(\ell)}=n\,\partial f_{n,a}/\partial h_a^{(\ell)}\), pairing this variation with \(p_a^{(\ell)}/n\) gives
\[
\nabla_{W_\ell}f_{n,a}
=\frac{\alpha}{Ln^2}b_a^{(\ell)}(h_a^{(\ell-1)})^T.
\]
Both factors of \(n\), the depth factor \(L\), and the residual factor \(\alpha\) are correct.

The backward recurrence is the transpose derivative of the same residual block:
\[
p_a^{(\ell-1)}
=p_a^{(\ell)}
+\frac{\alpha}{Ln}W_\ell^Tb_a^{(\ell)}.
\]
Consequently, raw mobility \(Ln^2\) produces precisely (15.4). The loss factors occur only in \(q_a\); for mean full squared loss they are \(2r_a/m\).

The finite metric is
\[
g(\dot W,\dot W)=\frac1{Ln^2}\sum_\ell\|\dot W_\ell\|_F^2.
\]
Thus
\[
\dot{\mathcal E}_n
=\sum_\ell\langle\nabla_{W_\ell}\mathcal E_n,\dot W_\ell\rangle_F
=-\frac1{Ln^2}\sum_\ell\|\dot W_\ell\|_F^2.
\]
This retains the squared norm of the full sample sum, including its cross terms.

Integrating and applying Cauchy–Schwarz in this metric yields (15.5). At fixed \(n,L\), that bound controls every finite parameter coordinate. The field is locally Lipschitz under the stated \(C^2\) assumptions, so bounded finite-time trajectories extend. No width-uniform conclusion is needed for this finite argument.

The cell embedding has exactly the metric norm above, and its integral operator is \(W_\ell/n\). It identifies the continuum metric and scaling without claiming convergence of discretized training. Full versus half squared loss changes physical speed by exactly the stated factor two.

**Coherent §15.2: the exact carrier, completeness, and measurability — CLEAN.** The intersection
\[
\mathcal K=L^\infty_u(L^2_v)\cap L^\infty_v(L^2_u),
\qquad
\|k\|_{\mathcal K}^2=\rho(k)^2+\chi(k)^2
\]
is correctly interpreted as a space of common measurable kernels modulo almost-everywhere equality. A Cauchy sequence has limits in both mixed spaces; their continuous embeddings into \(L^2(U^2)\) identify the limits. This proves completeness of the intersection norm.

The depth space is genuinely
\[
\mathbb K=L^2((0,1);\mathcal K)
\]
in the **Bochner** sense. The text explicitly requires strong \(\mathcal K\)-valued measurability. It does not replace that requirement by joint scalar measurability plus an integrable norm. Its summable-subsequence argument supplies completeness of this Bochner space.

The operator estimates follow directly from rowwise or columnwise Cauchy–Schwarz:
\[
\|T_kg\|_\infty\le\rho(k)\|g\|_2,\qquad
\|T_k^*g\|_\infty\le\chi(k)\|g\|_2.
\]
Fubini identifies \(T_k^*\) as the actual Hilbert adjoint. Also
\[
\|T_k\|_{2\to2}\le\|k\|_2\le\min(\rho(k),\chi(k)).
\]
All normalizations use the unit measure of \(U\).

For \(b,x\in L^\infty(U)\), direct integration gives
\[
\rho(b\otimes x)=\|b\|_\infty\|x\|_2,\qquad
\chi(b\otimes x)=\|x\|_\infty\|b\|_2.
\]
The induced maps into \(L^\infty\) and \(\mathcal K\) are continuous bilinear maps. Applying them to simple approximations therefore preserves strong measurability. This addresses the nonseparability issue rather than bypassing it.

The embedding \(\mathbb K\hookrightarrow\mathbb H\) is continuous and injective. It supplies the common scalar-kernel interpretation needed for Fubini and the energy pairing.

**Coherent §15.3, depth existence and estimates — CLEAN.** For fixed \(w\), the forward integral map has Lipschitz coefficient
\[
\alpha M_1\rho(w(s))
\]
in \(L^\infty(U)\). This coefficient is integrable in depth. Absolute continuity of its integral permits a finite partition into contraction intervals. The same construction applies backward to the adjoint with coefficient \(\alpha M_1\chi(w(s))\).

The forward bound
\[
\sup_s\|X_a(s)\|_\infty
\le \|X_a^0\|_\infty+\alpha M_0
\le C_X
\]
uses boundedness of the activation, not any bound on \(Z_a\). The adjoint estimate
\[
\sup_s\|P_a(s)\|_\infty
\le\|c\|_\infty e^{\alpha M_1\|\chi(w)\|_{L^1_s}}
\]
follows from the backward integral inequality.

The integrands are strongly measurable and Bochner integrable. The constructed curves are therefore Bochner absolutely continuous with the asserted \(L^1_sL^\infty_u\) derivatives. Uniqueness follows from the same integral inequalities.

The local field satisfies only
\[
\|Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(w)\|_{L^2_s}.
\]
No depth-essential-supremum estimate is silently used later.

**Coherent §15.3, Lipschitz training field and local training existence — CLEAN.** On a carrier ball of radius \(A\), let
\[
d=w-\widetilde w,\qquad
P_A=\|c\|_\infty e^{\alpha M_1A}.
\]
The forward difference inequality gives, for example,
\[
\|X_a-\widetilde X_a\|_{C_sL^\infty}
\le \alpha M_1C_Xe^{\alpha M_1A}\|d\|_{\mathbb K}.
\]
Then
\[
\|Z_a-\widetilde Z_a\|_{L^2_sL^\infty}
\le C_X\|\rho(d)\|_2
+A\|X_a-\widetilde X_a\|_{C_sL^\infty}.
\]

The adjoint difference is expanded into exactly the three terms in (15.20). Their forcing integrals are controlled by
\[
M_2P_A\|\chi(w)\|_2
 \|Z_a-\widetilde Z_a\|_{L^2_sL^\infty}
\quad\text{and}\quad
M_1P_A\|\chi(d)\|_1.
\]
The remaining term supplies the integrable Gronwall coefficient. Hence (15.21) follows. The critical product has two \(L^2\)-depth factors and is used in \(L^1\); no unproved \(L^\infty\)-depth estimate enters.

All predictions lie in the fixed compact cube determined by \(C_X\) and \(\|c\|_1\). Continuity of the gradient and Hessian of \(\mathcal R\) bounds both there, so \(q\) is bounded and Lipschitz on the attained output set.

Expanding the three factors in
\[
q_aB_a\otimes X_a-\widetilde q_a\widetilde B_a\otimes\widetilde X_a
\]
and using
\[
\|b\otimes x\|_{\mathcal K}
\le\sqrt2\|b\|_\infty\|x\|_\infty
\]
proves both bounds in (15.22). The field is strongly measurable as a \(\mathcal K\)-valued depth profile, so these are bounds in the specified Bochner carrier.

The training-time contraction uses both requirements: its time interval keeps the image inside a chosen ball and makes the Lipschitz constant less than one. It therefore constructs a unique local \(C^1\)-curve in \(\mathbb K\), with successive restarts giving the maximal solution.

**Coherent §15.3, Fréchet derivative and gradient representation — CLEAN.** The linearized depth equation
\[
Y_a'=\alpha\phi'(Z_a)(T_wY_a+T_vX_a),\qquad Y_a(0)=0
\]
defines a bounded linear map \(v\mapsto Y_a\) into \(C_sL^\infty_u\).

For the actual increment \(e_a\) and field increment \(\zeta_a\),
\[
\zeta_a=T_we_a+T_vX_a+T_ve_a.
\]
After subtracting the linearized equation, the remainder has forcing
\[
\alpha\phi'(Z_a)T_ve_a
+\alpha\bigl[\phi(Z_a+\zeta_a)-\phi(Z_a)-\phi'(Z_a)\zeta_a\bigr].
\]
Its integrated norm is bounded by
\[
\alpha M_1\|\rho(v)\|_1\|e_a\|_{C_sL^\infty}
+\frac{\alpha M_2}{2}\|\zeta_a\|_{L^2_sL^\infty}^2
=O(\|v\|_{\mathbb K}^2).
\]
Gronwall therefore proves a quadratic remainder in \(C_sL^\infty\). This establishes Fréchet differentiability, rather than only directional differentiability.

The pairing product rule is legitimate because \(P_a,Y_a\) are absolutely continuous into \(L^2(U)\), with integrable derivatives and bounded curves. The homogeneous terms cancel using the genuine adjoint:
\[
\frac d{ds}\langle P_a,Y_a\rangle
=\alpha\langle B_a,T_vX_a\rangle.
\]
The endpoint conditions then give (15.24), and the finite-dimensional loss chain rule gives
\[
D\mathcal E(w)[v]
=\langle\mathcal G(w),v\rangle_{\mathbb H}.
\]

This is an \(\mathbb H\)-pairing representation for a functional defined on \(\mathbb K\). The text correctly avoids claiming Fréchet differentiability on an open subset of bare \(\mathbb H\), or treating the Banach carrier norm as a Hilbert gradient metric.

**Coherent §15.3, energy and ordered global continuation — CLEAN.** Along the local strong solution,
\[
\frac d{dt}\mathcal E(w(t))
=\langle\mathcal G(w),-\mathcal G(w)\rangle_{\mathbb H}
=-\|\partial_tw\|_{\mathbb H}^2.
\]
Integration and Cauchy–Schwarz give exactly (15.14).

The global argument has the necessary order, without circular dependence:

1. Energy gives
   \[
   \|w(t)\|_{\mathbb H}\le H_T
   =\|w_0\|_{\mathbb H}+\sqrt{T(\mathcal E(w_0)-E_*)}.
   \]
2. The \(L^2\)-operator estimate then gives
   \[
   \sup_s\|P_a(s,t)\|_2
   \le P_{2,T}:=\|c\|_2e^{\alpha M_1H_T}.
   \]
3. The column norm of the training field obeys
   \[
   \chi(\partial_tw(s,t))
   \le A_T:=\alpha mQC_XM_1P_{2,T},
   \]
   hence \(C_w(t)\le C_w(0)+A_Tt\).
4. Integrating the adjoint directly, now using column control and the already obtained \(L^2\)-adjoint bound, gives
   \[
   \sup_s\|P_a(s,t)\|_\infty
   \le\|c\|_\infty+
   \alpha M_1P_{2,T}[C_w(0)+A_Tt].
   \]
5. Only then is the row norm bounded:
   \[
   \rho(\partial_tw(s,t))\le B_{0,T}+B_{1,T}t,
   \]
   where valid explicit constants are
   \[
   \begin{aligned}
   B_{0,T}
   &=\alpha mQM_1C_X
     [\|c\|_\infty+\alpha M_1P_{2,T}C_w(0)],\\
   B_{1,T}
   &=\alpha mQM_1C_X\,\alpha M_1P_{2,T}A_T.
   \end{aligned}
   \]
   Integrating gives the factor \(1/2\) in (15.29).

The depth interval has measure one, so passing a depth-independent pointwise bound to its \(L^2_s\) norm introduces no extra constant. The time-integrated seminorm inequalities are valid through the corresponding continuous mixed-space embeddings and Bochner triangle inequalities.

The example \(k_N=\sqrt N\,1_{\{u<1/N\}}\) correctly has \(L^2\)-norm one and row norm \(\sqrt N\). Thus the text recognizes why energy alone cannot establish strong continuation.

If a maximal endpoint were finite, these bounds would keep the full carrier norm bounded. Equation (15.22) would then bound \(\partial_tw\) in \(\mathbb K\), making \(w(t)\) Cauchy at that endpoint. Completeness supplies a carrier-valued limit, and local existence extends it. This proves global existence.

Local uniqueness at every restart proves global uniqueness and the autonomous semigroup property on all of \(\mathbb K\).

**Coherent §15.4: exact scope — CLEAN.** The result is global strong well-posedness, gradient representation, and energy dissipation for the coherent kernel model. It proves no width/depth approximation theorem, Gaussian-noise limit, fitting result, long-time convergence, or finite-dimensional scalar closure. Bounded activation and fixed bounded endpoints are used materially. The proof neither substitutes a Gaussian normalization nor extends itself to ReLU or trained endpoints.

**Hessian §14.1: scaled metric and exact feature/physical fields — CLEAN.** In raw coordinates, the inverse-mobility metric is
\[
\frac1n\|dz^{(1)}\|_2^2
+\|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2
+\frac1n\|dc\|_2^2.
\]
After setting the matrix coordinates to \(\sqrt nW^{(\ell)}\), this becomes \(n^{-1}\|d\Theta\|_2^2\).

For \(\mathscr F=nf_n\), differentiation in these scaled coordinates gives
\[
\nabla_\Theta\mathscr F
=\left(\delta^{(1)},
 \frac{\delta^{(2)}(h^{(1)})^T}{\sqrt n},
 \frac{\delta^{(3)}(h^{(2)})^T}{\sqrt n},
 h^{(3)}\right).
\]
Thus Euclidean feature flow \(\Theta'=b\) gives exactly the stored equations (14.3). Moreover,
\[
f_n'=\frac1n\nabla\mathscr F\cdot b=\frac{\|b\|_2^2}{n}.
\]

Physical gradient flow in the scaled coordinates is
\[
-n\nabla_\Theta(f_n-1)^2
=-2(f_n-1)b=\alpha b.
\]
Therefore \(\alpha=2(1-f_n)\) is exactly the full-loss physical clock. The Hessian \(\mathsf B\) is the Euclidean Hessian of \(nf_n\), not the raw-coordinate Hessian or the loss Hessian.

Linearity in \(c\) gives the complete block structure
\[
\mathsf B=
\begin{pmatrix}A&J^T\\J&0\end{pmatrix}.
\]

**Hessian §14.2: full Hessian and material derivatives — CLEAN.** A straight hidden-coordinate variation has
\[
dz^{(1)}=u_1,\quad
dz^{(2)}=E_2h^{(1)}/\sqrt n+W^{(2)}D_1u_1,
\]
and
\[
dz^{(3)}=E_3h^{(2)}/\sqrt n+W^{(3)}D_2T_2u.
\]
These are exactly \(T_1u,T_2u,T_3u\).

Differentiating twice produces both bilinear matrix terms:
\[
\begin{aligned}
d^2z^{(2)}
&=2E_2D_1u_1/\sqrt n+
 W^{(2)}[\phi''(z^{(1)})u_1^{\odot2}],\\
d^2z^{(3)}
&=2E_3D_2T_2u/\sqrt n+
 W^{(3)}[\phi''(z^{(2)})(T_2u)^{\odot2}+D_2d^2z^{(2)}].
\end{aligned}
\]
Pairing the final second variation with \(c\) therefore gives
\[
u^TAu
=\sum_{\ell=1}^3(T_\ell u)^TM_\ell T_\ell u
+2(S_2u)^TD_1T_1u+2(S_3u)^TD_2T_2u.
\]
Polarization recovers the entire symmetric hidden Hessian. No trained block is omitted.

The material preactivation derivatives correctly include each matrix update:
\[
\nu_2=\frac{\|h^{(1)}\|^2}{n}\delta^{(2)}+W^{(2)}D_1\nu_1,
\quad
\nu_3=\frac{\|h^{(2)}\|^2}{n}\delta^{(3)}+W^{(3)}D_2\nu_2.
\]
The backward derivatives include both trained transposes:
\[
\begin{aligned}
(\delta^{(3)})'&=D_3'c+D_3h^{(3)},\\
(q^{(2)})'&=((W^{(3)})')^T\delta^{(3)}
 +(W^{(3)})^T(\delta^{(3)})',\\
(\delta^{(2)})'&=D_2'q^{(2)}+D_2(q^{(2)})',\\
(q^{(1)})'&=((W^{(2)})')^T\delta^{(2)}
 +(W^{(2)})^T(\delta^{(2)})'.
\end{aligned}
\]
Here \(D_\ell'=\operatorname{diag}(\phi''(z^{(\ell)})\nu_\ell)\).

For a fixed tangent, direct product differentiation gives all terms in (14.10): the moving activations in \(E_\ell h/\sqrt n\), each \(W^{(\ell)}{}'\), each \(D_\ell'\), and the lower \(T_2'\) contribution to \(T_3'\). Likewise,
\[
S_\ell'u=E_\ell^T(\delta^{(\ell)})'/\sqrt n,
\qquad J'=D_3'T_3+D_3T_3'.
\]
The formulas for \(M_\ell'\) include both the \(\phi'''\nu\) terms and the derivatives of their backward multipliers, including \(c'=h^{(3)}\).

Differentiating the quadratic form then gives exactly the diagonal terms
\[
2(T_\ell'u)^TM_\ell T_\ell u+(T_\ell u)^TM_\ell'T_\ell u
\]
and all five mixed-product derivatives listed in (14.12). Terms involving \(T_1'\) vanish because \(T_1\) is constant. Thus (14.12) is the full material derivative, not an activation-only calculation.

Finally,
\[
\mathsf BU=(Au+J^T\xi,Ju)
\]
proves the complete signed quadratic form (14.13), including the square and its sign for arbitrary real \(\kappa\).

**Hessian §14.3: terminal construction and positive Rayleigh quotient — CLEAN.** Balance of \(e\) gives \(e^T\mathbf1=0\), and \(w\perp g\). The two summands of \(W^{(2)}\) have orthogonal domains and ranges, yielding
\[
\|W^{(2)}\|_{\rm op}
=\max(2\sqrt2,\beta\sqrt\rho/a_0).
\]
Since \(W^{(3)}\) is rank one and \(v\perp g\),
\[
\|W^{(3)}\|_{\rm op}^2=5+\gamma^2\rho.
\]
Both expressions are exact.

Multiplication gives
\[
z^{(2)}=\beta g,\quad h^{(2)}=t_\beta g,\quad
z^{(3)}=\gamma\rho t_\beta\mathbf1.
\]
For the backward quantities,
\[
q^{(2)}=\sqrt n\,kv+\gamma kg,\qquad
\delta^{(2)}=\sqrt n\,kv+\gamma d_\beta kg,
\]
and
\[
q^{(1)}=-2\sqrt n\,ke+\Lambda k\mathbf1.
\]
Because \(D_1=I/2\),
\[
\nu_2=(\mu I+W^{(2)}D_1^2(W^{(2)})^T)\delta^{(2)}.
\]
Its rare-coordinate block is \(\mu I+ww^T\), so its rare part is
\(\sqrt n\,k(\mu v-w)\). The bulk coefficient is precisely
\[
R_\beta=\gamma d_\beta\left(\mu+\frac{\beta^2\rho}{4a_0^2}\right).
\]
Using \(v^T(\mu v-w)=5\mu+1\) then verifies \(Q_\beta\) and every entry of (14.15).

At the terminal point, the large rare entries of \(q^{(2)}\) multiply \(\phi''(0)=0\). Also \(\sqrt n|e_i|=1\). These facts establish all three bounds in (14.16). The \(T_\ell,S_\ell,J\) estimates then bound the complete Hessian, including its mixed terms and readout blocks.

The chosen tangent has Frobenius norm one and satisfies exactly
\[
T_2u=a_0e_1,\quad T_2'u=\Lambda k e_1/4,\quad
T_3u=a_0\mathbf1/\sqrt n,\quad
T_3'u=\Lambda k\mathbf1/(4\sqrt n).
\]
The differentiated third-matrix contribution vanishes because the first coordinate of \(h^{(2)}\) is zero; the \(D_2'\) contribution vanishes because \(\phi''(0)=0\). These are evaluated trained terms, not frozen blocks.

For this tangent, the lower-layer and mixed terms vanish for the reasons given in the text. At the selected middle coordinate,
\[
\nu_{2,1}q^{(2)}_1=(\mu-1)nk^2,
\]
and therefore
\[
(M_2')_{11}=2(1-\mu)nk^2.
\]
The surviving top-layer terms give exactly
\[
U_n^T\mathsf B'U_n
=2\mu(1-\mu)nk^2
+\mu[\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H]
+\frac{a_0\Lambda}{2}\varepsilon k\phi''(Z).
\]

The leading constant is positive because \(0<\mu<1\) and
\[
D\ge D_*=\frac1{1+\{\gamma\phi(\beta)\}^2}>0.
\]
Thus the stated
\[
c_0=2\mu(1-\mu)D_*^2
\]
is correct.

The unspecified width-independent remainders can be bounded explicitly. Put
\[
\overline\Lambda=\beta\gamma d_\beta/a_0,\quad
\overline R=\gamma d_\beta(\mu+\beta^2/(4a_0^2)),
\]
and
\[
\overline Q=t_\beta^2+5\mu+1+\gamma d_\beta\overline R.
\]
Using \(|\phi''|,|\phi'''|\le2\), the absolute value of the remaining terms is at most
\[
C_{\rm rem}
=2\mu\varepsilon^2\overline Q+2\mu P
+a_0\overline\Lambda\varepsilon^2.
\]
If \(C_B\) bounds the terminal full Hessian, one may take
\[
C_\kappa=C_{\rm rem}+|\kappa|C_B^2.
\]
This also verifies the assertion for negative \(\kappa\).

The scalar identity
\[
\phi'''\phi'-\tfrac32(\phi'')^2=-2(\phi')^4
\]
is correct, but it does not control the signed matrix expression: the off-diagonal middle mobility changes the sign of \(\nu_{2,1}q_1^{(2)}\). The proof identifies this mechanism explicitly.

**Hessian §14.4: backward continuation to exactly zero readout — CLEAN.** The subspace
\[
W^{(3)}=\mathbf1p^T,\qquad c=\chi\mathbf1
\]
is invariant under the full feature field. Its equations give \(\chi'=\phi(y)\) and the stated rank-one update for \(W^{(3)}\). Smooth local uniqueness justifies using the restricted system in either direction.

All constants in (14.21) are positive and independent of width. In particular, \(\beta,\gamma>0\) imply \(y_*>0\) and \(h_*=\phi(y_*/2)>0\).

Under the bootstrap bounds, the rank-one update formula gives
\[
\|(W^{(3)})'\|_{\rm op}\le P\chi,\qquad
\|(W^{(2)})'\|_{\rm op}\le PN_3\chi.
\]
The full preactivation derivative gives
\[
\|\nu_2\|/\sqrt n\le(P^2+N_2^2)N_3\chi,
\]
and hence
\[
|y'|\le[P^2+N_3^2(P^2+N_2^2)]\chi=K\chi.
\]
No Hessian estimate enters.

On backward elapsed time \(\sigma\le\varepsilon/h_*\), integration gives exactly (14.23). The condition
\[
\varepsilon^2\le h_*/(4PN_3)
\]
bounds the second-matrix displacement by \(1/4\); it also bounds the third-matrix displacement by \(1/(4N_3)\le1/4\). The other square-root condition bounds the \(y\)-displacement by \(y_*/4\). Thus \(y\ge3y_*/4>y_*/2\), and neither matrix boundary can be reached.

The first-coordinate RMS displacement is bounded as stated. At fixed width, these vector and operator bounds imply bounds on every parameter coordinate, so the supplied finite-dimensional continuation argument applies.

Before the first zero,
\[
\frac{d\chi}{d\sigma}=-\phi(y)\le-h_*.
\]
Therefore zero is reached by \(\varepsilon/h_*\), while \(|d\chi/d\sigma|\le P\) gives the lower bound \(\varepsilon/P\). Reversing this same solution constructs the claimed trajectory from exactly zero readout.

The whole-segment conclusion concerns primal RMS/operator norms. A uniform Hessian bound along that segment is neither assumed nor obtained. The inverse-flow initialization is deterministic and correlated; it is not identified with the independent Gaussian law.

**Hessian §14.5: physical material derivative and obstruction scope — CLEAN.** Along the constructed segment,
\[
0\le f_n\le\varepsilon P\le1/4,
\]
so \(\alpha\in[3/2,2]\). Integrating \(dt/ds=1/\alpha\) gives precisely
\[
\tau_n/2\le t_n\le2\tau_n/3.
\]

Since \(\nabla f_n=b/n\),
\[
\mathsf C=D(\alpha b)=\alpha\mathsf B-\frac2n bb^T.
\]
Differentiating along physical time gives
\[
\dot\alpha=-2\alpha\|b\|^2/n,\qquad
\dot b=\alpha\mathsf Bb,\qquad
\dot{\mathsf B}=\alpha\mathsf B',
\]
and therefore exactly (14.24):
\[
\dot{\mathsf C}
=\alpha^2\mathsf B'
-\frac{2\alpha}{n}\|b\|^2\mathsf B
-\frac{2\alpha}{n}
[(\mathsf Bb)b^T+b(\mathsf Bb)^T].
\]
Both differentiated rank-one terms and the derivative of the clock multiplier are present.

For an explicit remainder check, let \(Q_b\) bound \(\|b\|^2/n\) at the terminal point. The two correction terms together have operator norm at most \(12Q_bC_B\), and
\[
\|\mathsf C\|_{\rm op}\le2C_B+2Q_b.
\]
One valid constant in (14.25) is consequently
\[
C_\kappa'
=4C_{\rm rem}+12Q_bC_B
+|\kappa|(2C_B+2Q_b)^2.
\]
The leading coefficient is at least \((9/4)c_0\varepsilon^2n\), as claimed.

This is a reached, pointwise, deterministic counterexample to the specified width-independent signed upper bound under the stated norm controls. The terminal times may depend on width. It proves neither a Gaussian-typical obstruction nor an integrated-in-time obstruction, and it implies no fixed-time convergence failure.

**Hessian §14.6, two-sided feature flow and polynomial primal bounds — CLEAN.** Bounded activation gives the triangular inequalities
\[
|R_c'|\le P,\qquad
\|(W^{(3)})'\|_{\rm op}\le PR_c,\qquad
\|(W^{(2)})'\|_{\rm op}\le P\|W^{(3)}\|_{\rm op}R_c,
\]
where \(R_c=\|c\|/\sqrt n\). Integrating with absolute values proves (14.29)–(14.30) for either sign of feature time.

The last polynomial in (14.29) expands to
\[
K_2(u)=M+PMR_0u
+\frac{P^2}{2}(M+R_0^2)u^2
+\frac{P^3R_0}{2}u^3
+\frac{P^4}{8}u^4.
\]
Thus its coefficients and the integral factors are correct. The first-preactivation estimate follows from
\[
\|\delta^{(1)}\|/\sqrt n\le K_2K_3R.
\]
Its displayed integral is likewise an explicit finite polynomial envelope.

These bounds prevent escape at every fixed width on any bounded feature-time interval. They establish global existence in both directions for arbitrary finite initial parameters.

Smooth dependence is justified by the differentiated integral equation and a uniformly vanishing remainder on compact parameter sets. The inverse variational equation
\[
Y'=\mathsf BY,\qquad Z'=-Z\mathsf B
\]
gives \((ZY)'=0\), proving invertibility. Together with uniqueness, this supplies a complete smooth flow with inverse \(\Phi_{-s}\).

**Hessian §14.6, nuclear inequalities and full Hessian bound — CLEAN.** The SVD argument correctly proves the nuclear dual formula, triangle inequality, rank bound, and rank-one norm formula. Decomposing the diagonal into rank-one terms yields
\[
\|T^T\operatorname{diag}(d)T\|_*
\le\|T\|_{\rm op}^2\sum_i|d_i|.
\]

On \(|s|\le S\), the backward estimates imply the absolute diagonal sums
\[
2nK_2K_3R,\qquad2nK_3R,\qquad2nR
\]
for \(M_1,M_2,M_3\). These use \(\ell^1\le\sqrt n\,\ell^2\), not a width-independent coordinate maximum.

Each symmetric mixed term has rank at most \(2n\) and operator norm at most twice the product of its map norms. Their nuclear bounds are therefore
\[
4nK_3R,\qquad4nt_2R.
\]
The off-diagonal \(J\)-block has rank at most \(2n\) and operator norm at most \(t_3\), contributing \(2nt_3\).

Adding all pieces gives exactly
\[
\|\mathsf B\|_*
\le n\left[
2R(K_2K_3+t_2^2K_3+t_3^2)
+4R(K_3+t_2)+2t_3\right].
\]
This verifies every coefficient in \(\mathcal P_S\). The expression is a polynomial with nonnegative coefficients in \(S,M,R_0\). The extra bound
\[
\|b\|^2/n\le t_3^2R^2+P^2=\mathcal Q_S
\]
also follows exactly.

The argument supplies a nuclear bound of order \(n\), not a width-independent operator bound.

**Hessian §14.6, every-plane tangent volume, Jacobi formula, and inverse — CLEAN.** Every full-rank initial tangent matrix remains full rank because
\[
\mathcal T(s)=Y(s)\mathcal T(0)
\]
and \(Y(s)\) is invertible. Hence its Gram matrix stays positive definite.

Differentiating its determinant gives
\[
\begin{aligned}
(\log V_{\mathcal T})'
&=\tfrac12\operatorname{Tr}
[(\mathcal T^T\mathcal T)^{-1}(\mathcal T^T\mathcal T)']\\
&=\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B).
\end{aligned}
\]
The factor \(1/2\) cancels the two symmetric Gram-derivative terms. The stated \(\Pi_{\mathcal T}\) is an orthogonal projector, so its operator norm is one and
\[
|(\log V_{\mathcal T})'|\le\|\mathsf B\|_*.
\]
Integration in either direction proves (14.28), equivalently
\[
e^{-n|s|\mathcal P_S}
\le\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}
\le e^{n|s|\mathcal P_S}.
\]

The bound contains no tangent-dimension factor. It is pathwise and simultaneous over all initial planes, including planes chosen measurably from the initial parameters.

**Hessian §14.6, exact Gaussian initialization and moments — CLEAN.** The stored readout variance is \(n^{-2}\), as required by NOTATION.md. Consequently
\[
R_0=\|c(0)\|/\sqrt n
\quad\text{has law}\quad R_n^{\rm std}/n,
\]
not \(R_n^{\rm std}/\sqrt n\).

The sphere-net argument has the correct constants: radius-\(1/8\) packing inside a radius-\(9/8\) ball gives \(9^n\) points; two \(1/4\)-approximations incur at most \(\frac12\|W\|_{\rm op}\), giving the factor two in the net maximum. The Gaussian bilinear tail and union bound yield
\[
\Pr(\|W\|_{\rm op}>u)\le2\,81^n e^{-nu^2/8}.
\]
For \(u\ge10\), \(\log81<5\le u^2/16\) gives the final tail in (14.36). A union bound supplies the same uniform moment conclusion for the maximum of the two hidden norms.

Integrating the tail proves all positive operator-norm moments uniformly in width. Jensen’s inequality gives, for \(p\ge2\),
\[
\mathbb E(R_n^{\rm std})^p\le\mathbb E|g_1|^p,
\]
and for \(0<p<2\), the bound is one. Hence both estimates in (14.37) are correct.

Every polynomial monomial needed in \(\mathcal P_S\) and later physical envelopes is integrable by Hölder and these higher moments. No evolved Gaussian assumption or conditioning on a norm event is used. Therefore
\[
\mathbb E\sup_{|s|\le S}
\left|\log\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}\right|
\le C_Sn
\]
follows with width- and tangent-dimension-independent \(C_S\).

**Hessian §14.6, forward physical clock and tangent bounds — CLEAN.** Along a local physical trajectory,
\[
\dot r_n=-2r_n\|b\|^2/n.
\]
Its scalar solution preserves the residual sign and gives
\[
|r_n(t)|\le|r_n(0)|\le1+PR_0.
\]
Thus the total absolute feature-clock variation is at most
\[
S_T=2T(1+PR_0).
\]
This handles either sign of the initial residual. Two-sided feature completeness is precisely what permits the negative-clock case.

The complete feature flow and its polynomial bounds keep the physical parameters bounded on finite forward intervals, proving global forward physical existence. If the initial residual is zero, the state is stationary.

At fixed physical time, however, the variational field still includes
\[
\mathsf C=\alpha\mathsf B-\frac2n bb^T.
\]
In particular, a stationary zero-residual state need not have the identity tangent response: its Jacobian can be \(-2bb^T/n\).

The rank-one nuclear contribution is exactly \(2\|b\|^2/n\). Therefore
\[
\|\mathsf C\|_*
\le2(1+PR_0)n\mathcal P_{S_T}+2\mathcal Q_{S_T}
\le n\widetilde{\mathcal P}_T,
\]
which verifies (14.39), including the use of \(n\ge1\).

Substituting polynomial \(S_T\) preserves a polynomial envelope in \(M,R_0\). The inverse linear equation again proves full tangent invertibility, and the Gram/Jacobi argument proves (14.40). All required Gaussian moments have already been supplied.

These are compact-horizon bounds; the constants depend on \(S\) or \(T\). They are not uniform-in-time estimates.

**Hessian §14.7, projection determinant including singular cases — CLEAN.** For the hidden initial plane,
\[
\mathcal T=\binom{\mathsf P}{\mathsf R}
\]
has full column rank even when its upper block \(\mathsf P\) is singular. Orthogonalizing its columns gives
\[
Q=\mathcal T(\mathcal T^T\mathcal T)^{-1/2},
\qquad Q_H^TQ_H=I-Q_C^TQ_C.
\]
Since
\[
\mathsf P=Q_H(\mathcal T^T\mathcal T)^{1/2},
\]
taking Gram determinants yields
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_{N_h}-Q_C^TQ_C)}.
\]
The SVD of \(Q_C\) changes determinant dimension without any invertibility assumption, giving exactly
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
=V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.
\]

All \(a_j\) lie in \([0,1]\). The identity includes the singular case: \(\mathsf P\) is singular precisely when an angle factor vanishes, equivalently some \(a_j=1\). Both sides then equal zero.

The statement about at most \(n\) projection-loss directions is correct. It bounds their number, not their severity: even one factor can approach zero. Therefore intrinsic-volume control alone supplies no projected determinant lower bound.

**Hessian §14.7, feature and physical slope equations — CLEAN.** On an invertible branch,
\[
\mathsf K=\mathsf R\mathsf P^{-1},
\qquad
\mathcal T=\binom I{\mathsf K}\mathsf P.
\]
Taking determinants and using the same singular-value identity gives
\[
\log|\det\mathsf P|
=\log V_{\mathcal T}
-\tfrac12\log\det(I_n+\mathsf K\mathsf K^T).
\]
The subtracted quantity is nonnegative.

The full feature variational equations are
\[
\mathsf P'=A\mathsf P+J^T\mathsf R,\qquad
\mathsf R'=J\mathsf P.
\]
Differentiating the inverse proves
\[
\mathsf K'=J-\mathsf KA-\mathsf KJ^T\mathsf K.
\]
Its scope is exactly an interval where \(\mathsf P\) remains invertible. No global invertibility of this projection follows from full-flow invertibility.

For completeness, every physical-clock block can be displayed explicitly. Write \(a=J^Tc\) and \(h=h^{(3)}\). Then
\[
\begin{aligned}
\mathsf C_{HH}&=\alpha A-\tfrac2n aa^T,&
\mathsf C_{HC}&=\alpha J^T-\tfrac2n ah^T,\\
\mathsf C_{CH}&=\alpha J-\tfrac2n ha^T,&
\mathsf C_{CC}&=-\tfrac2n hh^T.
\end{aligned}
\]
Substitution into the stated physical block equation gives
\[
\dot{\mathsf K}
=\alpha(J-\mathsf KA-\mathsf KJ^T\mathsf K)
-\frac2n(h-\mathsf Ka)(a^T+h^T\mathsf K).
\]
This verifies all four rank-one block contributions. It is not merely the feature Riccati equation multiplied by \(\alpha\).

The derivative is taken at fixed initial readout. It is not a conditional covariance or a differentiated conditional mean.

**Proof containment and required corrections.** No required correction was found. Each candidate contains its own model-specific proof, including the necessary continuation, differentiation, and clock arguments. Neither depends mathematically on the other candidate or an omitted chapter.

The background tools are elementary integration and finite-dimensional linear algebra, contraction and integral inequalities, and the finite-dimensional ODE arguments supplied in the text. No heavy external population theorem, Gaussian matrix limit theorem, width-limit theorem, or unexplained compactness principle carries a missing proof step.

**Exact scope of the CLEAN verdict.**

| Result | Established scope | Not established |
|---|---|---|
| Coherent kernel flow | Global \(C^1\) flow and unique restart on the stated Bochner carrier; exact gradient pairing and energy identity | Bare-\(L^2\) well-posedness, width/depth limits, noisy-kernel convergence, fitting, or long-time convergence |
| Reached Hessian obstruction | Deterministic correlated initialization with zero initial readout; whole-segment primal bounds; terminal Hessian bound; pointwise signed divergence in feature and physical time | Gaussian-typical failure, common fixed terminal time, Hessian-history bound, or integrated signed obstruction |
| Full tangent volumes | Every-plane pathwise log-volume bounds; expected absolute log-volume change \(O(n)\) under the exact Gaussian law, on fixed horizons | Width-independent response operator bounds or projected lower-volume bounds |
| Hidden projection | Exact determinant identity, including singular projections; exact slope equations on invertible branches | Global projection nonsingularity, projected entropy bounds, response covariance estimates, or control of adaptive Gaussian queries |

The inputs remain unchanged.