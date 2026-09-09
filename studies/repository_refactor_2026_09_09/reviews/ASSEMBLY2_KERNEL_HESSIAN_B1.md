**Overall verdict: CLEAN.**

Both candidates are independently **CLEAN**, including all of hessian Sections 14.6–14.7. I found no mathematical correction required under their stated assumptions. The substantive proofs are contained in the supplied files; neither candidate needs the other candidate, omitted chapter sections, or an unproved external heavy result.

This verdict covers the precise claims made in the files. In particular, it preserves the distinction between the deterministic Hessian obstruction and Gaussian expectation results, and between intrinsic tangent volume and projected volume.

**Read, integrity, and scope ledger.**

I personally read every line of all four permitted inputs. Initial hashes were recorded before reading their mathematical contents. Final hashes were recomputed after the audit and matched exactly. The three entries in `INPUTS.json` also matched their files’ hashes, byte counts, and line counts.

| Input | Lines read, inclusive | Bytes | SHA-256 before and after—identical |
|---|---:|---:|---|
| [coherent.md](/tmp/pde_assembly2_kernel_hessian_r2/coherent.md) | 1–589 | 20,170 | `19c267a56658d6980ed5bd4957d2db9fda5f7178c4eb7024dde961c285a8fd53` |
| [hessian.md](/tmp/pde_assembly2_kernel_hessian_r2/hessian.md) | 1–985 | 37,284 | `1dbf61698ef88e716a9bf1ef11b6d5ded2d21b321f5f50b9d1a4fba89fa9bbf1` |
| [NOTATION.md](/tmp/pde_assembly2_kernel_hessian_r2/NOTATION.md) | 1–98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| [INPUTS.json](/tmp/pde_assembly2_kernel_hessian_r2/INPUTS.json) | 1–17 | 429 | `728635dc5fd3b0e39ff2883945129493dafebf14cf0f35635a2fedd2860b192c` |

Total input coverage: **1,689 lines and 62,993 bytes**. `INPUTS.json` has no self-entry; its own before/after hash was checked separately.

I also personally read the complete required instruction files:

- [solve-math-rigorously/SKILL.md](/etc/codex/skills/solve-math-rigorously/SKILL.md).
- [investigate-conjectures/SKILL.md](/etc/codex/skills/investigate-conjectures/SKILL.md).
- [research-contract.md](/etc/codex/skills/investigate-conjectures/references/research-contract.md).
- [evidence-ledger.md](/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md).
- [adversarial-audit.md](/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md).

No delegation, external sources, checkout inspection, history, previous verdicts, other packets, or other tasks were used. No training or research experiments were run. The inputs were left unchanged.

**Notation contract: CLEAN.**

The candidates explicitly distinguish their architectures and therefore do not silently exchange normalizations.

In `hessian.md`, the stored hidden matrices act without an additional forward normalization; the \(1/\sqrt n\) factors in tangent formulas arise from differentiating the scaled coordinates \(\sqrt nW^{(\ell)}\). Its one-sample full squared loss and mobilities \((n,1,1,n)\) agree with `NOTATION.md`.

In `coherent.md`, \(L\) is explicitly retyped as the number of residual blocks. The forward \(W_\ell/n\), residual step \(\alpha/L\), fixed endpoints, and mobility \(Ln^2\) are explicitly specified for this separate model.

Both candidates keep residuals outside their residual-free adjoints and use the actual transpose or Hilbert adjoint of the forward operator. The full-loss versus half-loss factor is correct. The notation file’s arctangent primitives also have the stated derivatives:
\[
\frac{d}{dz}(z+z^3/3)=\frac1{\phi'(z)}
\quad\text{for }\phi(z)=\arctan z,
\]
and the derivative acquires the factor \(10\) for \(1+\arctan(z)/10\). Neither candidate uses these continuous-flow identities to identify raw GD with transformed Euler steps.

**Candidate `coherent.md`: CLEAN.**

**Section 15.1: finite metric, gradients, physical clock, and energy.**  
The raw finite model is exactly
\[
z_a^{(\ell)}=\frac{W_\ell h_a^{(\ell-1)}}n,\qquad
h_a^{(\ell)}=h_a^{(\ell-1)}+\frac{\alpha}{L}\phi(z_a^{(\ell)}),
\qquad
f_{n,a}=\frac{c^Th_a^{(L)}}n.
\]
Only the \(Ln^2\) untied trunk coordinates are trained.

Writing \(p_a^{(\ell)}=n\,\partial f_{n,a}/\partial h_a^{(\ell)}\), differentiation of one residual block gives
\[
p_a^{(\ell-1)}
=p_a^{(\ell)}
+\frac{\alpha}{Ln}W_\ell^T
 \bigl(p_a^{(\ell)}\odot\phi'(z_a^{(\ell)})\bigr).
\]
Thus (15.2) has the correct transpose and factor.

For a variation \(V_\ell\), the block contribution to \(Df_{n,a}\) is
\[
\frac1n(p_a^{(\ell)})^T
\frac{\alpha}{L}
\operatorname{diag}(\phi'(z_a^{(\ell)}))
\frac{V_\ell h_a^{(\ell-1)}}n.
\]
Consequently,
\[
\nabla_{W_\ell}f_{n,a}
=\frac{\alpha}{Ln^2}b_a^{(\ell)}(h_a^{(\ell-1)})^T,
\]
and the loss gradient in (15.3) follows by the finite-dimensional chain rule.

The parameter metric is
\[
\langle V,Z\rangle_{\rm metric}
=\frac1{Ln^2}\sum_\ell\operatorname{Tr}(V_\ell^TZ_\ell).
\]
Its inverse mobility is \(Ln^2\), producing precisely (15.4). The dissipation is
\[
\frac{d\mathcal E_n}{dt}
=-\frac1{Ln^2}\sum_\ell\|\dot W_\ell\|_F^2.
\]
The sum over samples occurs **inside** each matrix velocity and its squared norm. No missing cross-sample terms occur.

For mean full squared loss, \(q_a=2r_{n,a}/m\); for mean half squared loss, \(q_a=r_{n,a}/m\). The claimed factor-two physical-speed difference is correct.

Integrating dissipation and applying Cauchy–Schwarz in time proves (15.5). At fixed finite \(n,L\), this bounds every parameter coordinate on a finite time interval. The finite vector field is locally Lipschitz because the activation and loss are \(C^2\). Bounded parameters therefore permit continuation. No uniform-in-width conclusion is drawn from this finite-dimensional argument.

The cell embedding gives exactly
\[
\|W_{\rm embedded}\|_{L^2(ds\,du\,dv)}^2
=\frac1{Ln^2}\sum_\ell\|W_\ell\|_F^2,
\]
and its integral operator acts as \(W_\ell/n\). This establishes the metric identification, without asserting a discretization limit.

**Section 15.2: exact carrier, completeness, operators, and measurability.**  
The kernel space is
\[
\mathcal K=
L^\infty_u(L^2_v)\cap L^\infty_v(L^2_u),
\qquad
\|k\|_{\mathcal K}^2=\rho(k)^2+\chi(k)^2,
\]
with the two components identified through their common scalar \(L^2(U^2)\) representative.

The completeness proof is valid: a \(\mathcal K\)-Cauchy sequence converges in both complete mixed spaces, and both limits agree in \(L^2(U^2)\). The resulting common kernel belongs to their intersection and the convergence holds in the displayed norm.

The depth carrier is specifically
\[
\mathbb K=L^2((0,1);\mathcal K)
\]
in the **Bochner** sense. The file does not substitute joint scalar measurability for strong \(\mathcal K\)-valued measurability. Its summable-subsequence argument proves completeness of this carrier. The embedding into
\[
\mathbb H=L^2((0,1)\times U^2)
\]
is continuous.

All operator constants in (15.8) are correct:
\[
\|T_kg\|_\infty\le\rho(k)\|g\|_2,\qquad
\|T_k^*g\|_\infty\le\chi(k)\|g\|_2,
\]
and
\[
\|T_k\|_{2\to2}\le\|k\|_2\le\min\{\rho(k),\chi(k)\}.
\]
The first two follow by sectional Cauchy–Schwarz; the last uses that \(U\) has measure one. Fubini identifies the displayed reverse action as the actual Hilbert-space adjoint.

For rank-one kernels,
\[
\rho(b\otimes x)=\|b\|_\infty\|x\|_2,\qquad
\chi(b\otimes x)=\|x\|_\infty\|b\|_2.
\]
Hence
\[
\|b\otimes x\|_{\mathcal K}
\le\sqrt2\,\|b\|_\infty\|x\|_\infty.
\]
These continuous bilinear maps preserve strong measurability by simple-function approximation. The activation and derivative superposition maps needed later are Lipschitz on \(L^\infty\), with constants \(M_1\) and \(M_2\).

The constructed depth curves are explicitly Bochner integrals. Thus their asserted derivatives do not rely on treating an arbitrary Banach-valued absolutely continuous curve as automatically differentiable.

**Section 15.3: exact assumptions.**  
The theorem requires:

- A finite positive number \(m\) of samples and \(\alpha>0\).
- Fixed, untrained \(X_a^0,c\in L^\infty(U)\).
- \(\phi\in C_b^2(\mathbb R)\), with the function and its first two derivatives bounded.
- \(\mathcal R\in C^2(\mathbb R^m)\), bounded below by a finite \(E_*\).
- Initial state \(w_0\in\mathbb K\), including the strong-measurability requirement.

No Gram normalization, nonsingularity, orthogonality, label restriction, Gaussian initialization, or population-of-data limit is assumed. Arbitrary fixed finite data are represented through the stated bounded profiles and loss. Neither endpoint is trained.

**Depth existence and estimates.**  
For fixed \(w\in\mathbb K\), both \(\rho(w)\) and \(\chi(w)\) belong to \(L^1_s\). The forward integral map is a contraction on any interval where
\[
\alpha M_1\int\rho(w(s))\,ds<1.
\]
Integrability permits a finite subdivision satisfying this condition. The backward adjoint uses the corresponding condition with \(\chi(w)\). The complete-space contraction argument applies to continuous \(L^\infty\)-valued curves.

Bounded activation gives
\[
\sup_s\|X_a(s)\|_\infty
\le \max_a\|X_a^0\|_\infty+\alpha M_0=C_X.
\]
Backward Gronwall gives
\[
\sup_s\|P_a(s)\|_\infty
\le\|c\|_\infty
\exp\!\left(\alpha M_1\int_0^1\chi(w(s))\,ds\right).
\]
The forward integrand is bounded and strongly measurable; the adjoint integrand is strongly measurable with integrable norm. Their Bochner absolute continuity, \(L^1_sL^\infty_u\) derivatives, and uniqueness follow.

The local-field estimate is exactly
\[
\|Z_a\|_{L^2_sL^\infty_u}
\le C_X\|\rho(w)\|_{L^2_s}.
\]
No depth essential supremum is assumed or inferred.

**Lipschitz training field and local training existence.**  
On a carrier ball of radius \(A\), subtracting the forward equations gives an integral inequality with coefficient \(\alpha M_1\rho(w)\) and forcing \(\alpha M_1C_X\rho(w-\widetilde w)\). Thus (15.18) holds. Substitution into the forward operator difference gives (15.19).

The adjoint difference expansion (15.20) contains all three required terms: the adjoint difference, the activation-derivative difference, and the kernel difference. Its potentially delicate integral is controlled by
\[
\int_0^1\chi(w(s))
 \|Z_a(s)-\widetilde Z_a(s)\|_\infty\,ds
\le
\|\chi(w)\|_{L^2_s}
\|Z_a-\widetilde Z_a\|_{L^2_sL^\infty_u}.
\]
This is a legitimate product of two square-integrable depth factors. Backward Gronwall then gives the \(C_sL^\infty_u\) adjoint difference; the displayed decomposition of \(B_a-\widetilde B_a\) gives its \(L^2_sL^\infty_u\) bound.

Every output lies in the fixed compact cube
\[
[-\|c\|_1C_X,\|c\|_1C_X]^m.
\]
The loss gradient and Hessian are bounded there, so the loss factors are bounded and Lipschitz on the carrier ball. The three-term outer-product expansion, with the \(\sqrt2\) estimate above, proves both bounds in (15.22) in the actual Bochner carrier.

The local training contraction has both necessary properties: a sufficiently short interval keeps its image in the chosen ball and makes its Lipschitz constant less than one. Since \(\mathcal G\) is continuous, the resulting integral solution is \(C^1\) into \(\mathbb K\).

**Fréchet differentiation and gradient representation.**  
The linearized equation (15.23) defines a bounded linear map
\[
v\longmapsto Y_a\in C([0,1];L^\infty(U)).
\]
For the true increments \(e_a,\zeta_a\), the exact identity is
\[
\zeta_a=T_we_a+T_vX_a+T_ve_a.
\]
The Taylor remainder satisfies the global bound
\[
|\phi(Z+\zeta)-\phi(Z)-\phi'(Z)\zeta|
\le \frac{M_2}{2}|\zeta|^2.
\]
The forcing in the equation for \(e_a-Y_a\) therefore has integrated norm at most
\[
\alpha M_1\|\rho(v)\|_{L^1_s}\|e_a\|_{C_sL^\infty_u}
+\frac{\alpha M_2}{2}
 \|\zeta_a\|_{L^2_sL^\infty_u}^2
=O(\|v\|_{\mathbb K}^2).
\]
Gronwall gives the claimed quadratic remainder. This proves Fréchet differentiation, rather than only directional differentiation. It requires neither a depth-maximum bound nor a third activation derivative.

Both \(P_a\) and \(Y_a\) have integrable \(L^2\)-valued derivatives and bounded \(L^2\) norms. Their pairing therefore has the valid product rule
\[
\frac d{ds}\langle P_a,Y_a\rangle
=\alpha\langle B_a,T_vX_a\rangle.
\]
The homogeneous terms cancel using the same forward operator and its adjoint. The boundary conditions and Fubini give (15.24), and the finite-dimensional loss chain rule gives
\[
D\mathcal E(w)[v]
=\langle\mathcal G(w),v\rangle_{\mathbb H}.
\]

This is correctly described as an \(\mathbb H\)-pairing gradient for a functional defined on \(\mathbb K\). It does not assert Fréchet differentiability on an open subset of bare \(\mathbb H\).

**Energy identity.**  
Along the local \(C^1(\mathbb K)\) solution,
\[
\frac d{dt}\mathcal E(w(t))
=D\mathcal E(w(t))[-\mathcal G(w(t))]
=-\|\mathcal G(w(t))\|_{\mathbb H}^2.
\]
Integration and time Cauchy–Schwarz give precisely (15.14), including its constants.

**Ordered global continuation, uniqueness, and restart.**  
This proof closes in the required order, without using the desired strong bound prematurely.

First, with
\[
D=\mathcal E(w_0)-E_*,\qquad
H_T=\|w_0\|_{\mathbb H}+\sqrt{TD},
\]
energy gives \(\|w(t)\|_{\mathbb H}\le H_T\). The compact output cube gives the finite constant \(Q\) in (15.25).

Second, the Hilbert-space operator bound in the adjoint equation gives
\[
\sup_s\|P_a(s,t)\|_2
\le \|c\|_2 e^{\alpha M_1H_T}=P_{2,T}.
\]
Only the energy-space kernel norm is used here.

Third, the **column** estimate closes using this \(L^2\) adjoint bound:
\[
\chi(\partial_tw(s,t))
\le \alpha mQ C_XM_1P_{2,T}=A_T,
\]
and hence
\[
C_w(t)\le C_w(0)+A_Tt.
\]

Fourth, direct integration of the backward equation with the column operator estimate upgrades the adjoint:
\[
\sup_s\|P_a(s,t)\|_\infty
\le \|c\|_\infty+
\alpha M_1P_{2,T}\,[C_w(0)+A_Tt].
\]

Fifth, the **row** bound now follows:
\[
\rho(\partial_tw(s,t))
\le B_{0,T}+B_{1,T}t,
\]
where, writing \(F=\alpha mQM_1C_X\),
\[
B_{0,T}=F\bigl(\|c\|_\infty+\alpha M_1P_{2,T}C_w(0)\bigr),
\qquad
B_{1,T}=F\alpha M_1P_{2,T}A_T.
\]
Integration gives the exact factor \(1/2\) in
\[
R_w(t)\le R_w(0)+B_{0,T}t+\tfrac12 B_{1,T}t^2.
\]
The full carrier norm is \(\sqrt{C_w(t)^2+R_w(t)^2}\), so these are sufficient strong bounds.

The seminorm integration steps are valid consequences of the continuous mixed-space embeddings and Bochner integral inequalities; they do not require selecting pointwise representatives simultaneously for all training times.

If the maximal time were finite, these estimates would bound the carrier norm up to that time. The bounded-ball estimate for \(\mathcal G\) would then make \(w\) uniformly Lipschitz in \(\mathbb K\), giving a carrier limit at the endpoint. The local construction restarts there, contradicting maximality. Local uniqueness gives global uniqueness and the autonomous semigroup property.

The example
\[
k_N(u,v)=\sqrt N\,\mathbf1_{\{u<1/N\}}
\]
indeed has \(\|k_N\|_2=1\) and \(\rho(k_N)=\sqrt N\). It correctly shows why the separate strong continuation argument is necessary.

**Section 15.4: exact scope.**  
The result proves global forward training existence, uniqueness, restart, the exact gradient, and energy law for the stated coherent kernel model. It retains bounded fixed endpoints, \(C_b^2\) activation, lower-bounded \(C^2\) loss, arbitrary finite data, and the physical metric and clock.

It does not prove bare-\(\mathbb H\) well-posedness, trained-endpoint extensions, fitting, convergence as training time tends to infinity, a finite-dimensional closure, or any width/depth approximation theorem. No such conclusion is smuggled into the proof.

**Candidate `hessian.md`, Sections 14.1–14.5: CLEAN.**

**Exact assumptions and claim.**  
The obstruction uses three hidden layers, \(\phi=\arctan\), one datum \(d=m=1\), \(x_1=y_1=1\), full loss \((f_n-1)^2\), and stored mobilities \((n,1,1,n)\).

For each fixed \(\beta,\gamma>0\), sufficiently small fixed \(\varepsilon>0\), and every even \(n\ge4\), it constructs deterministic correlated hidden initial parameters with exactly zero readout. The conclusion concerns terminal signed material derivatives reached after a controlled trajectory segment. Four primal norms are bounded throughout that segment; the full Hessian operator norm is bounded at the terminal state only.

**Section 14.1: scaled-coordinate metric and exact feature field.**  
In raw coordinates, the inverse-mobility metric is
\[
\frac1n\|dz^{(1)}\|_2^2+
\|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2+
\frac1n\|dc\|_2^2.
\]
Under
\[
\Theta=(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)},c),
\]
this becomes \(\|d\Theta\|_2^2/n\). Thus the physical mobility is \(nI\) in these Euclidean coordinates.

Since \(\mathscr F=nf_n\),
\[
\nabla_\Theta\mathcal L_n=\frac{2r_n}{n}\nabla_\Theta\mathscr F,
\]
and physical GF is
\[
\dot\Theta=-2r_n b=2(1-f_n)b.
\]
This establishes the feature clock exactly.

The matrix derivative
\[
\nabla_{\sqrt nW^{(\ell)}}\mathscr F
=\frac{\delta^{(\ell)}(h^{(\ell-1)})^T}{\sqrt n}
\]
gives stored feature velocity \(\delta^{(\ell)}(h^{(\ell-1)})^T/n\), as stated. The first-weight and readout velocities are \(\delta^{(1)}\) and \(h^{(3)}\). Every block is trained.

The identities
\[
b=(J^Tc,h^{(3)}),\qquad
\mathsf B=\begin{pmatrix}A&J^T\\J&0\end{pmatrix},
\qquad
f_n'=\frac{\|b\|_2^2}{n}
\]
are exact in this metric.

**Section 14.2: complete Hessian.**  
For a fixed hidden tangent \(u=(u_1,E_2,E_3)\), the maps \(T_\ell u\) are exactly the first preactivation variations. A straight parameter line has second preactivation variation
\[
\partial_\lambda^2z^{(\ell)}
=\frac{2E_\ell D_{\ell-1}T_{\ell-1}u}{\sqrt n}
+W^{(\ell)}
\left[
\phi''(z^{(\ell-1)})\odot(T_{\ell-1}u)^{\odot2}
+D_{\ell-1}\partial_\lambda^2z^{(\ell-1)}
\right],
\]
with \(\partial_\lambda^2z^{(1)}=0\). This verifies both displayed second-variation formulas.

Pairing the resulting second output variation with \(c\) gives
\[
A=\sum_{\ell=1}^3T_\ell^TM_\ell T_\ell
+\operatorname{sym}(S_2^TD_1T_1)
+\operatorname{sym}(S_3^TD_2T_2),
\]
where \(\operatorname{sym}(H)=H+H^T\). This is exactly (14.8), including both mixed trained-matrix terms. The readout cross-blocks are \(J,J^T\); the readout–readout block vanishes because \(\mathscr F\) is linear in \(c\).

**Complete material differentiation.**  
Equations (14.9) correctly differentiate the forward and backward paths. In particular,
\[
\nu_\ell
=\frac{\|h^{(\ell-1)}\|_2^2}{n}\delta^{(\ell)}
+W^{(\ell)}D_{\ell-1}\nu_{\ell-1},
\qquad \ell=2,3,
\]
and
\[
D_\ell'=\operatorname{diag}(\phi''(z^{(\ell)})\nu_\ell).
\]
For the backward recurrence,
\[
(q^{(\ell)})'
=((W^{(\ell+1)})')^T\delta^{(\ell+1)}
+(W^{(\ell+1)})^T(\delta^{(\ell+1)})',
\]
and
\[
(\delta^{(\ell)})'=D_\ell'q^{(\ell)}+D_\ell(q^{(\ell)})'.
\]
At the top, \(q^{(3)}=c\) and \((q^{(3)})'=h^{(3)}\), producing the readout derivative in (14.9).

Differentiating \(T_\ell\) yields all four product-rule terms: the varying previous activation, varying matrix, varying activation derivative, and varying previous tangent. The terms involving \(T_1'\) vanish because \(T_1'=0\). Also,
\[
S_\ell'u=E_\ell^T(\delta^{(\ell)})'/\sqrt n,
\qquad
J'=D_3'T_3+D_3T_3'.
\]
These are precisely (14.10).

The diagonal derivatives have both required contributions:
\[
M_\ell'
=\operatorname{diag}\!\left(
\phi'''(z^{(\ell)})\nu_\ell q^{(\ell)}
+\phi''(z^{(\ell)})(q^{(\ell)})'
\right),
\]
with the top-layer convention just specified. Thus (14.11) includes \(c'=h^{(3)}\).

Differentiating the quadratic form gives (14.12): two tangent-derivative contributions for each diagonal quadratic term and all three factors’ derivatives for each mixed term. The absent \(T_1'\) contribution is identically zero. There is no frozen trained transpose or omitted readout term.

Finally,
\[
U^T\mathsf B^2U=\|\mathsf BU\|_2^2
=\|Au+J^T\xi\|_2^2+\|Ju\|_2^2,
\]
so (14.13) is exact for every real \(\kappa\).

**Section 14.3: terminal construction and every scalar factor.**  
For even \(n\ge4\), a balanced sign vector \(e\) exists and
\(\rho=(n-2)/n\in[1/2,1)\). The orthogonality claims used for \(W^{(2)}\) hold in both domain and range. They give
\[
\|W^{(2)}\|_{\rm op}
=\max\{2\sqrt2,\beta\sqrt\rho/a_0\}.
\]
For \(W^{(3)}=\mathbf1p^T\), the orthogonal vectors \(v,g\) give
\[
n\|p\|_2^2=5+\gamma^2\rho,
\]
and hence the stated third-matrix norm.

With \(a_0=\pi/4\), \(\mu=a_0^2\), the forward values are exactly
\[
h^{(1)}=a_0\mathbf1,\quad
z^{(2)}=\beta g,\quad h^{(2)}=t_\beta g,\quad
z^{(3)}=Z\mathbf1,\quad h^{(3)}=H\mathbf1.
\]
In particular \(Z=\gamma\rho t_\beta\), \(f_n=\varepsilon H\), and \(k=\varepsilon\phi'(Z)\).

Direct backward multiplication gives
\[
q^{(2)}=\sqrt n\,k\,v+\gamma k g,\qquad
\delta^{(2)}=\sqrt n\,k\,v+\gamma d_\beta k g,
\]
and
\[
q^{(1)}=-2\sqrt n\,k\,e+\Lambda k\mathbf1,
\qquad
\Lambda=\frac{\beta\gamma d_\beta\rho}{a_0}.
\]
Since \(D_1=I/2\), the displayed \(\nu_1\) follows.

For \(\nu_2\), the rare block is
\[
(\mu I+ww^T)(\sqrt n\,kv)
=\sqrt n\,k(\mu v-w),
\]
because \(w^Tv=-1\). The bulk coefficient is
\[
\mu\gamma d_\beta+\frac{\beta\Lambda}{4a_0}
=\gamma d_\beta\left(\mu+\frac{\beta^2\rho}{4a_0^2}\right)
=R_\beta.
\]
For \(\nu_3\),
\[
v^T(\mu v-w)=5\mu+1,
\]
so its coefficient is exactly
\[
Q_\beta=\rho t_\beta^2+5\mu+1+\gamma\rho d_\beta R_\beta.
\]
This verifies all of (14.15), including its factors \(1/2\), \(1/4\), and the bulk term.

The terminal diagonal Hessian estimates use
\[
\phi''(1)=-\tfrac12,\qquad \phi''(0)=0.
\]
They give exactly (14.16). The rare \(q^{(2)}\) coordinates grow like \(\sqrt n\), but their contributions to \(M_2\) vanish at \(z^{(2)}=0\); the \(q^{(1)}\) coordinates remain bounded because \(\sqrt n|e_i|=1\).

The bounds on \(T_\ell,J,S_\ell\), inserted into the full quadratic form, give a width-independent terminal bound on \(A\), hence on \(\mathsf B\). They also give
\[
\|b\|_2^2/n\le\|J\|_{\rm op}^2\varepsilon^2+P^2.
\]
No Hessian-history bound enters this argument.

The chosen tangent has unit norm:
\[
\|e_1\mathbf1^T/\sqrt n\|_F=1.
\]
Its responses and derivatives in (14.18) are correct. In particular, the differentiated \(W^{(3)}\) term vanishes because \(g^Te_1=0\); the differentiated \(D_2\) term vanishes because \(\phi''(0)=0\).

At the decisive coordinate,
\[
\nu_{2,1}=\sqrt n\,k(\mu-1),\qquad
q^{(2)}_1=\sqrt n\,k,
\]
so
\[
(M_2')_{11}
=\phi'''(0)\nu_{2,1}q^{(2)}_1
=2(1-\mu)nk^2.
\]
All other terms surviving for this tangent yield exactly
\[
U_n^T\mathsf B'U_n
=
2\mu(1-\mu)nk^2
+\mu\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}
+\frac{a_0\Lambda}{2}\varepsilon k\phi''(Z).
\]
Thus (14.19) is the full material derivative, with its complete bounded remainder.

Because
\[
D=\phi'(Z)\ge
D_*=\frac1{1+\{\gamma\phi(\beta)\}^2},
\]
the coefficient
\[
c_0=2\mu(1-\mu)D_*^2
\]
is positive and independent of width. The terminal Hessian bound controls
\(\|\mathsf BU_n\|^2\), and for either sign of \(\kappa\) its contribution is bounded below by \(-|\kappa|C^2\). This proves (14.6).

The scalar identity is also correct:
\[
\phi'''\phi'-\tfrac32(\phi'')^2=-2(\phi')^4.
\]
Its negative sign does not contradict the constructed positive term: the middle mobility has off-diagonal entries, and \(\nu_{2,1}q^{(2)}_1<0\).

**Section 14.4: explicit backward continuation to zero readout.**  
The equal-row/equal-readout subspace is invariant in both directions because its derivatives retain those forms. Smooth finite-dimensional uniqueness justifies using its restricted equations.

All inequalities in (14.22) follow from the rank-one norm formula, \(|\phi'|\le1\), and \(\|h^{(\ell)}\|/\sqrt n\le P\). In particular,
\[
\|\nu_2\|/\sqrt n\le(P^2+N_2^2)N_3\chi,
\]
and
\[
|y'|\le
\bigl[P^2+N_3^2(P^2+N_2^2)\bigr]\chi=K\chi.
\]
The constant \(K\) is therefore correct.

The stated \(\varepsilon_0\) ensures
\[
PN_3\varepsilon^2/h_*\le\tfrac14,\qquad
K\varepsilon^2/h_*\le y_*/4.
\]
Since \(N_3>1\), it also ensures
\(P\varepsilon^2/h_*\le1/4\). Thus every bound in (14.23) has the claimed constant.

During backward evolution,
\[
\frac{d\chi}{d\sigma}=-\phi(y)\le-h_*.
\]
The matrix norms remain strictly below their boundaries, and
\[
y(\sigma)\ge y(0)-y_*/4\ge3y_*/4>y_*/2.
\]
The first-weight RMS stays bounded by the displayed integral estimate. At each fixed width these bounds control every raw and scaled parameter coordinate, allowing continuation until \(\chi=0\).

If no zero occurred before \(\varepsilon/h_*\), integrating the preceding differential inequality would force \(\chi\le0\), a contradiction. Conversely, \(|d\chi/d\sigma|\le P\) gives the lower bound. Hence
\[
\varepsilon/P\le\tau_n\le\varepsilon/h_*.
\]
Reversing this same solution gives the asserted initialization and reached terminal state. This is an exact deterministic inverse-flow construction; no Gaussian distributional claim is used.

**Section 14.5: full physical clock and signed Jacobian.**  
Along the constructed segment, monotonicity of \(f_n\) gives
\[
0\le f_n\le\varepsilon H\le\varepsilon P\le\tfrac14.
\]
Therefore \(\alpha=2(1-f_n)\in[3/2,2]\), and
\[
\tau_n/2\le t_n\le2\tau_n/3.
\]

The complete physical Jacobian is
\[
\mathsf C=\alpha\mathsf B-\frac2n bb^T,
\]
because \(\nabla_\Theta\alpha=-2b/n\). Its derivative uses
\[
\dot\alpha=-2\alpha\|b\|^2/n,\quad
\dot b=\alpha\mathsf Bb,\quad
\dot{\mathsf B}=\alpha\mathsf B',
\]
giving exactly
\[
\dot{\mathsf C}
=\alpha^2\mathsf B'
-\frac{2\alpha}{n}\|b\|^2\mathsf B
-\frac{2\alpha}{n}\bigl[(\mathsf Bb)b^T+b(\mathsf Bb)^T\bigr].
\]
Both rank-one derivatives are present.

For completeness, the square also has all clock terms:
\[
\mathsf C^2
=\alpha^2\mathsf B^2
-\frac{2\alpha}{n}\bigl[(\mathsf Bb)b^T+b(\mathsf Bb)^T\bigr]
+\frac{4\|b\|^2}{n^2}bb^T.
\]
The terminal bounds on \(\|\mathsf B\|_{\rm op}\) and \(\|b\|/\sqrt n\) control every correction in these expressions independently of width. Since \(\alpha^2\ge9/4\), (14.25) follows with the stated leading coefficient.

The obstruction is pointwise at reached times that may depend on width. It does not establish a fixed-time Gaussian failure, an integrated signed-estimate failure, or a failure under an additional Hessian-history hypothesis. The file states these limitations correctly.

**Candidate `hessian.md`, Section 14.6: CLEAN.**

**Two-sided global feature flow and polynomial primal bounds.**  
This part permits arbitrary finite initial parameters and does not require the deterministic witness or even width parity.

The triangular bounds are valid in either time direction:
\[
R(u)=R_0+Pu,\qquad
K_3(u)=M+PR_0u+\tfrac12P^2u^2.
\]
Expanding the last polynomial in (14.29) gives
\[
K_2(u)=M+PMR_0u
+\frac{P^2}{2}(M+R_0^2)u^2
+\frac{P^3}{2}R_0u^3+\frac{P^4}{8}u^4.
\]
This confirms its explicit nonnegative coefficients.

The derivatives controlling these bounds are
\[
\|c'\|/\sqrt n\le P,\quad
\|(W^{(3)})'\|_{\rm op}\le PR,\quad
\|(W^{(2)})'\|_{\rm op}\le PK_3R.
\]
Similarly,
\[
\|z^{(1)}(s)\|/\sqrt n
\le\|z^{(1)}(0)\|/\sqrt n
+\int_0^{|s|}K_2(v)K_3(v)R(v)\,dv.
\]
The integral is polynomial; it is also bounded by the explicit polynomial
\(|s|K_2(|s|)K_3(|s|)R(|s|)\).

At fixed width these bounds prevent finite-time parameter escape in either feature-time direction. The local smooth field therefore produces a complete smooth flow \(\Phi_s\), with inverse \(\Phi_{-s}\).

The smooth-dependence argument is sufficient: on the compact finite-dimensional sets traversed locally, derivatives of the field are continuous and bounded, and difference quotients converge through the variational integral equation and Gronwall. Repeated differentiation is legitimate because arctangent is smooth.

The inverse fundamental-matrix argument is exact:
\[
Y'=\mathsf BY,\qquad Z'=-Z\mathsf B
\quad\Longrightarrow\quad
(ZY)'=0,\quad ZY=I.
\]
It requires only continuous coefficients on each finite interval.

**Nuclear inequalities and the complete Hessian bound.**  
The supplied SVD argument correctly proves nuclear/operator duality, the nuclear triangle inequality, and
\[
\|H\|_*\le\operatorname{rank}(H)\|H\|_{\rm op}.
\]
Decomposing the diagonal into rank-one terms gives
\[
\|T^T\operatorname{diag}(d)T\|_*
\le\|T\|_{\rm op}^2\sum_i|d_i|.
\]

Set
\[
t_2=P+K_2,\qquad t_3=P+K_3t_2.
\]
All map bounds preceding (14.33) are correct. In particular,
\[
\|S_2\|_{\rm op}\le K_3R,\qquad
\|S_3\|_{\rm op}\le R.
\]
Using \(|\phi''|\le2\) and \(\|v\|_1\le\sqrt n\|v\|_2\), the three diagonal sums are bounded by
\[
2nK_2K_3R,\qquad 2nK_3R,\qquad 2nR.
\]
This does not assume bounded maximum backward coordinates.

Each mixed symmetric operator has rank at most \(2n\). Their nuclear contributions are respectively at most
\[
4nK_3R,\qquad4nRt_2.
\]
The off-diagonal \(J\)-block contributes at most \(2nt_3\). Thus the full bound is exactly
\[
\|\mathsf B\|_*\le n\mathcal P_S(M,R_0),
\]
where
\[
\mathcal P_S
=2R(K_2K_3+t_2^2K_3+t_3^2)
+4R(K_3+t_2)+2t_3.
\]
Every factor in (14.33) is justified. This is a nonnegative polynomial in \(S,M,R_0\).

Likewise,
\[
\|b\|^2/n\le t_3^2R^2+P^2=\mathcal Q_S
\]
is correct.

**Every-plane tangent volume, Jacobi formula, and inverse argument.**  
For any full-rank initial \(q\)-frame,
\[
\mathcal T(s)=Y(s)\mathcal T(0)
\]
retains full column rank because \(Y(s)\) is invertible. Its Gram matrix remains positive definite.

The determinant expansion supplied in the file proves the required Jacobi identity. Since \(\mathsf B\) is symmetric,
\[
\frac d{ds}\log V_{\mathcal T}
=\operatorname{Tr}\!\left[
\mathcal T(\mathcal T^T\mathcal T)^{-1}\mathcal T^T\mathsf B
\right]
=\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B).
\]
The displayed \(\Pi_{\mathcal T}\) is indeed the orthogonal projector onto the current range. Its operator norm is one, so nuclear duality gives
\[
\left|\frac d{ds}\log V_{\mathcal T}\right|
\le n\mathcal P_S.
\]
Integration proves (14.28) in both time directions.

This proof is simultaneous over all initial tangent planes and all permitted dimensions. It supplies the pathwise intrinsic lower and upper bounds
\[
e^{-n|s|\mathcal P_S}V_{\mathcal T}(0)
\le V_{\mathcal T}(s)
\le e^{n|s|\mathcal P_S}V_{\mathcal T}(0).
\]
It does not supply a width-independent bound on individual response singular values.

**Exact Gaussian initialization and moments.**  
The law used here is exactly
\[
z_j^{(1)}(0)\sim N(0,1),\qquad
W_{ij}^{(2)}(0),W_{ij}^{(3)}(0)\sim N(0,1/n),\qquad
c_i(0)\sim N(0,n^{-2}),
\]
with the prescribed independence. In particular, the stored readout standard deviation is \(1/n\).

The net argument is valid with its stated constants:

- A maximal \(1/4\)-separated sphere set is a \(1/4\)-net with at most \(9^n\) points, by the radius-\(1/8\) disjoint-ball comparison.
- Approximating both unit vectors loses at most \(\frac12\|W\|_{\rm op}\), giving
  \(\|W\|_{\rm op}\le2\max_{\rm net}|y^TWx|\).
- The fixed bilinear form has variance \(1/n\); its moment-generating function gives the stated Gaussian tail.
- The pair-net union bound is therefore
  \[
  \Pr\{\|W\|_{\rm op}>u\}\le2\,81^ne^{-nu^2/8}.
  \]
- For \(u\ge10\), \(\log81<5\le u^2/16\), so this is at most \(2e^{-u^2/16}\).

Tail integration gives all fixed positive moments uniformly in width. A union bound gives the same property for the maximum \(M\) of the two hidden norms.

For \(R_n^{\rm std}=(n^{-1}\sum g_i^2)^{1/2}\), convexity for \(p\ge2\) and concavity for \(0<p<2\) give precisely the bounds stated in the file. Since
\[
R_0\stackrel{\rm law}=R_n^{\rm std}/n,
\]
the \(n^{-p}\) factor in (14.37) is correct. The first-weight RMS moments are also uniformly bounded.

Hölder controls every mixed monomial in \(\mathcal P_S(M,R_0)\). No exponential moment or Gaussian assumption on the evolved state is needed. Thus the expected supremum of absolute intrinsic log-volume change is bounded by \(C_Sn\).

Measurably chosen initial tangent planes cause no difficulty: the bound is pathwise and simultaneous, and continuity in time makes the compact-time supremum measurable.

**Forward physical time, including every clock correction.**  
For either sign of the initial residual,
\[
\dot r_n=-2r_n\|b\|^2/n.
\]
Solving this scalar equation along a local trajectory preserves its sign and gives
\[
|r_n(t)|\le|r_n(0)|\le1+PR_0.
\]
Therefore
\[
|\alpha(t)|\le2(1+PR_0),\qquad
\int_0^T|\alpha(t)|\,dt\le S_T=2T(1+PR_0).
\]
A positive initial residual corresponds to negative feature time, which is covered by the two-sided feature completeness already proved. The polynomial primal bounds prevent finite-time physical escape. A zero initial residual gives a stationary physical trajectory. No backward physical completeness is assumed.

At fixed physical time, the variational coefficient is the full
\[
\mathsf C=\alpha\mathsf B-\frac2n bb^T.
\]
The clock contribution has nuclear norm exactly \(2\|b\|^2/n\). Hence
\[
\|\mathsf C\|_*
\le2(1+PR_0)n\mathcal P_{S_T}+2\mathcal Q_{S_T}
\le n\widetilde{\mathcal P}_T.
\]
This verifies (14.39), including the use of \(n\ge1\) for the last term.

Substitution of the polynomial \(S_T\) preserves the polynomial form, so the previously proved Gaussian moments suffice. The physical fundamental matrix is invertible by its inverse linear equation, and the same projector/Jacobi calculation proves (14.40), including the supremum and expectation.

These are derivatives at fixed physical time. No feature-time derivative is substituted in place of the physical variational equation.

**Candidate `hessian.md`, Section 14.7: CLEAN.**

**Exact projection determinant, including singular cases.**  
The hidden-initial-plane response
\[
\mathcal T=\begin{pmatrix}\mathsf P\\\mathsf R\end{pmatrix}
\]
has full column rank even when its hidden projection \(\mathsf P\) is singular. Thus
\[
Q=\mathcal T(\mathcal T^T\mathcal T)^{-1/2}
=\begin{pmatrix}Q_H\\Q_C\end{pmatrix}
\]
is well-defined and has orthonormal columns.

Since
\[
Q_H^TQ_H=I-Q_C^TQ_C,
\]
the singular values \(a_j\) of \(Q_C\) lie in \([0,1]\). Factoring
\(\mathsf P=Q_H(\mathcal T^T\mathcal T)^{1/2}\) yields
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_{N_h}-Q_C^TQ_C)}.
\]
The nonzero spectra of \(Q_C^TQ_C\) and \(Q_CQ_C^T\) agree, with extra zeros contributing factors one. Therefore
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
=V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.
\]
This proves (14.41).

If \(\mathsf P\) is singular, \(Q_H^TQ_H\) is singular, so at least one \(a_j=1\); both sides vanish. No inverse of \(\mathsf P\) was used in this argument.

Thus there are at most \(n\) nontrivial angular factors, but they may be zero or arbitrarily small. The intrinsic bound alone gives no lower bound for this projected determinant.

**Slope and determinant identities on invertible branches.**  
Where \(\mathsf P\) is invertible,
\[
\mathsf K=\mathsf R\mathsf P^{-1},\qquad
\mathcal T=\begin{pmatrix}I\\\mathsf K\end{pmatrix}\mathsf P.
\]
Taking Gram determinants gives
\[
V_{\mathcal T}^2
=(\det\mathsf P)^2\det(I+\mathsf K^T\mathsf K),
\]
and the same singular-value argument changes the last determinant to
\(\det(I_n+\mathsf K\mathsf K^T)\). This proves (14.42), with the correct sign and factor \(1/2\).

The feature block equations are
\[
\mathsf P'=A\mathsf P+J^T\mathsf R,\qquad
\mathsf R'=J\mathsf P.
\]
Differentiating the inverse gives exactly
\[
\mathsf K'=J-\mathsf KA-\mathsf KJ^T\mathsf K.
\]
There is no assertion that this slope remains defined through a singular projection.

**Physical slope with all rank-one terms.**  
To display every block explicitly, write
\[
g_H=J^Tc,\qquad h=h^{(3)},\qquad b=(g_H,h).
\]
Then
\[
\begin{aligned}
\mathsf C_{HH}&=\alpha A-\frac2n g_Hg_H^T,\\
\mathsf C_{HC}&=\alpha J^T-\frac2n g_Hh^T,\\
\mathsf C_{CH}&=\alpha J-\frac2n hg_H^T,\\
\mathsf C_{CC}&=-\frac2n hh^T.
\end{aligned}
\]
Substitution into the file’s physical block Riccati equation gives
\[
\dot{\mathsf K}
=\alpha(J-\mathsf KA-\mathsf KJ^T\mathsf K)
+\frac2n(\mathsf Kg_H-h)(g_H^T+h^T\mathsf K).
\]
The factored correction contains all four rank-one clock contributions. Thus the physical equation stated in the file is complete.

The determinant identities are algebraic and apply equally to the response at fixed physical time. The derivative here fixes the initial readout while varying the hidden initial coordinate. It is not a conditional covariance or a derivative of a mean obtained after averaging over readouts.

**Required corrections and final scope.**

**Required corrections: none.** No actual proof gap was found in either candidate’s stated results.

The elementary dependencies are adequately supplied or applied with valid hypotheses: complete-space contraction, scalar integral inequalities, Bochner integration and Fubini, finite-dimensional differentiation, SVD/spectral facts, and Gaussian density calculations. There is no dependency on a width-limit theorem, an omitted population construction, an external random-matrix estimate, or the other candidate.

The accepted conclusions remain precisely:

- `coherent.md`: global forward, restartable strong-kernel training flow with the exact coherent metric, gradient, and energy law.
- `hessian.md` 14.1–14.5: a deterministic correlated, zero-readout-started, reached **pointwise** signed-Hessian obstruction, with segment primal bounds and a terminal-only Hessian bound.
- `hessian.md` 14.6: two-sided complete feature flow and pathwise/expected **intrinsic** tangent-volume bounds, plus forward physical-time counterparts under the exact Gaussian initialization.
- `hessian.md` 14.7: exact projection and branchwise slope identities, without projected nonsingularity, projected lower-volume or entropy bounds, response covariance estimates, or adaptive Gaussian-query control.

**Both candidates are CLEAN within these exact scopes.**