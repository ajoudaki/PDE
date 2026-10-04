# Two-sample population symmetry, mandatory boundary, and two active memory channels

Status: frozen scoped theory candidate, 2026-09-30. The arguments below are exact under the explicitly stated population-existence and symmetry hypotheses. They are author-checked, not independently reviewed or promoted. This route does not prove population existence, global fitting, endpoint existence, or a global query sign law.

## Scope, sources, and indispensable hypotheses

The scientific input is only the supervisor's supplied two-sample, infinite-width population system. Required process sources read were root `AGENTS.md`, `RESEARCH_WORKFLOW.md` Part 1, the `solve-math-rigorously` and `investigate-conjectures` skills, and the latter's research-contract, adversarial-audit, and proof-search-orchestration references. No study history, manuscript, established book, external scientific source, finite-width reference, or experiment was used.

Exposure disclosure: a `collaboration.list_agents` call intended to inspect concurrency returned completed agents' scientific summaries from earlier finite-dimensional routes. This was reported to the supervisor. Those summaries are not inputs to any argument here, but this route must not be called a blind independent attempt. An independent candidate-only check remains available to the supervisor.

All query arguments below are normalized coordinates \(q=x/\sqrt d\). Thus (F_t(q)) means the supplied predictor evaluated at raw input \(x=\sqrt d\,q\). The two training vectors satisfy \(\|u_1\|=\|u_2\|=1\), and \(y_a\in\{-1,1\}\). Write

\[
B_t f=T f+\frac12\sum_{a=1}^2 V_a(t)\langle K_a(t),f\rangle_1,
\quad H_t(q)=\tanh(A_t\cdot q),\quad
G_t(q)=\tanh(B_tH_t(q)),\quad F_t(q)=\langle W_t,G_t(q)\rangle_2.
\]

Inner products are real population \(L^2\) inner products. The physical-time equations are exactly those in the assignment:

\[
\begin{split}
D_a&=W(1-G_a^2),\qquad
L_a=(1-H_a^2)B^*D_a,\\
\dot W&=-\sum_a r_aG_a,\qquad
\dot A=-\sum_a r_aL_au_a,\qquad
\dot V_a=-2r_aD_a,\\
\dot K_a&=\frac{\rho}{\tau}(H_a-K_a),\qquad
\dot\tau=\rho,\qquad
r_a=F(u_a)-y_a,\qquad
\rho^2=\frac{r_1^2+r_2^2}{2}.
\end{split}
\]

Initially \(A_0\) is standard isotropic Gaussian, \(W_0=V_{a,0}=0\), \(K_{a,0}=H_0(u_a)\), and \(\tau_0=1\). The initialized mixing and its true adjoint are reused throughout.

The following hypotheses isolate the missing foundation rather than replace it by an arbitrary operator model.

1. **Population flow and integrability.** The canonical Gaussian population construction has a unique solution on the interval under discussion. Every displayed pairing and derivative used below exists; training/query features and keys are continuous in their population \(L^2\) spaces. Readout and memory derivatives hold in \(L^2\). The predictor and the scalar population inner products used below are deterministic. These conditions are assumed, not proved here.
2. **Joint initialization symmetry and equivariance.** The complete initialized population law, including mixing/adjoint reuse, is invariant under \(A_0\mapsto R A_0\) for every input-space \(R\in O(d)\). Rotating the data and first-layer vectors together, or permuting sample indices together, transports the unique flow accordingly. The law of the full state, and hence its deterministic scalar observables, has this covariance. A pathwise equality of individual neurons before and after a rotation is not assumed.
3. **Initial forward Gaussian law, used only for the initial-sign and rank-two conclusions.** For every finite query set, \(Z_0(q)=T H_0(q)\) is a centered jointly Gaussian field on population 2 with
   \[
   \mathbb E_2[Z_0(q)Z_0(q')]
   =\mathbb E_{a\sim N(0,I_d)}[\tanh(a\cdot q)\tanh(a\cdot q')].
   \]
   This fixes unit mixing variance; a fixed positive mixing variance only changes the covariance by a positive factor and leaves every sign/rank conclusion unchanged.

Hypothesis 2 is the relevant symmetry consequence expected of the canonical iid-Gaussian initialization; Hypothesis 3 specifies its initial forward law. Neither follows from merely declaring \(T\) to be a bounded map between two \(L^2\) spaces. In particular, this note does not identify an arbitrary bounded \(T\), or an isonormal forward map with a conveniently chosen adjoint, with the required trained Gaussian population limit. No independence of trained neuronwise quantities is used.

The main result is a complete symmetry normal form and its sharp mandatory zero set. A second result shows that synchronized residuals nevertheless activate both population memory channels at order \(t^2\).

## 1. Exact sign gauge and synchronized residuals

Set the signed inputs

\[
p_a=y_au_a,\qquad \kappa=p_1\cdot p_2=y_1y_2(u_1\cdot u_2).
\]

Replace the two labels by \(+1\), and replace \(K_a,V_a\) by \(y_aK_a,y_aV_a\). This is an exact gauge transformation of the entire physical trajectory, with \(A,W,T,\tau\), and the query predictor unchanged.

To verify it, oddness gives \(H(p_a)=y_aH(u_a)\), \(G(p_a)=y_aG(u_a)\), and \(F(p_a)=y_aF(u_a)\). Each memory summand remains unchanged because

\[
(y_aV_a)\langle y_aK_a,H(q)\rangle_1
=V_a\langle K_a,H(q)\rangle_1.
\]

The signed residual is \(e_a=F(p_a)-1=y_ar_a\). The fields \(D_a\) and \(L_a\) are unchanged at the corresponding signed training point because the activation derivatives are even. Thus

\[
-r_aG(u_a)=-e_aG(p_a),\qquad
-r_aL_au_a=-e_aL_ap_a,
\]

and multiplication of the \(V_a,K_a\) equations by \(y_a\) gives their all-positive-label equations. The clock is unchanged since \(e_a^2=r_a^2\). The transformed initial keys are exactly \(H_0(p_a)\).

For the rest of the proof, \(H_a,G_a,K_a,V_a,D_a,L_a\) refer to these signed coordinates, and both labels are \(+1\).

For any \(R\in O(d)\), the transformation \(A\mapsto R A\), \(p_a\mapsto Rp_a\), with \(W,K,V,T\) unchanged, transports every equation and satisfies

\[
F^{R\mathcal D}_t(Rq)=F^{\mathcal D}_t(q),
\]

where the superscript records the signed dataset. This identity follows first for the transformed initialized state by substitution and then for the canonical deterministic population predictor by Hypotheses 1–2. A sample permutation similarly preserves the predictor. There is an orthogonal map exchanging any two equal-norm vectors. Therefore

\[
F_t(p_1)=F_t(p_2)=:f(t),\qquad
e_1(t)=e_2(t)=:e(t)=f(t)-1.
\]

Returning to the original labels gives the exact synchronization law

\[
r_a(t)=y_ae(t),\qquad
F_t(u_a)=y_af(t),\qquad \rho(t)=|e(t)|.
\]

Equal residuals in signed coordinates do not assert equality of the two feature fields or either pair of memory fields.

## 2. Whole-query normal form and the sharp mandatory boundary

Assume first that \(-1<\kappa<1\). Define

\[
e_+=\frac{p_1+p_2}{\sqrt{2(1+\kappa)}},\qquad
e_-=\frac{p_1-p_2}{\sqrt{2(1-\kappa)}},\qquad
a=\sqrt{\frac{1+\kappa}{2}},\qquad
b=\sqrt{\frac{1-\kappa}{2}}.
\]

Then \(e_+,e_-\) are orthonormal and \(p_1=ae_++be_-\), \(p_2=ae_+-be_-\). For a query write

\[
q=\alpha e_++\beta e_-+z,\qquad z\perp e_+,e_-,\qquad s=\|z\|.
\]

**Theorem 1 (exact query normal form).** At every time in the existence interval,

\[
F_t(q)=\Phi_t(\alpha,\beta,s),\qquad
\Phi_t(-\alpha,\beta,s)=-\Phi_t(\alpha,\beta,s),\qquad
\Phi_t(\alpha,-\beta,s)=\Phi_t(\alpha,\beta,s).
\]

The radius coordinate is restricted to \(s=0\) when \(d=2\). In particular,

\[
(p_1+p_2)\cdot q=0\quad\Longrightarrow\quad F_t(q)=0.
\tag{1}
\]

If \(F_t\) is \(C^1\) in \(q\), it has the more explicit form

\[
F_t(q)=\alpha\,\Psi_t(\alpha^2,\beta^2,s^2)
\tag{2}
\]

with a continuous scalar function \(\Psi_t\) on the applicable domain. On the mandatory plane, \(\nabla_qF_t\), when defined, is parallel to \(e_+\); its signed magnitude need not be constant or positive.

**Proof.** All orthogonal maps acting on \(\operatorname{span}\{p_1,p_2\}^{\perp}\) and fixing the training span preserve the dataset. They act transitively on perpendicular vectors of a fixed length, so equivariance makes the query dependence on \(z\) radial. The reflection \(S=I-2e_-e_-^\top\) exchanges \(p_1,p_2\); therefore \(F_t(Sq)=F_t(q)\), giving evenness in \(\beta\).

For every state, regardless of initialization, \(H_t(-q)=-H_t(q)\). Linearity of \(B_t\), oddness of the second tanh, and the linear readout then give \(F_t(-q)=-F_t(q)\). Combining this oddness with the evenness in \(\beta\) and the perpendicular reflection \(z\mapsto-z\) gives oddness in \(\alpha\). Evaluation at \(\alpha=0\) proves (1).

For the \(C^1\) claim, define \(\Psi_t(A,B,S)=\Phi_t(\sqrt A,\sqrt B,\sqrt S)/\sqrt A\) when \(A>0\), and use \(\partial_\alpha\Phi_t(0,\sqrt B,\sqrt S)\) at \(A=0\). The identity

\[
\frac{\Phi_t(\alpha,\beta,s)}{\alpha}
=\int_0^1\partial_\alpha\Phi_t(\theta\alpha,\beta,s)\,d\theta
\]

proves continuity at \(A=0\); parity supplies (2). Since the restriction to the plane is identically zero, every derivative tangent to it vanishes. This proves the gradient assertion. ∎

In raw input coordinates, the mandatory plane is

\[
\{x:(y_1x_1+y_2x_2)\cdot x=0\}.
\]

For opposite labels this is the equal-distance plane of the two equal-norm training inputs, with orientation fixed by the labels. For equal labels its normal is their sum. Equation (1) identifies a zero set, not by itself a sign-changing decision boundary.

These statements pass to every pointwise limit \(F_\infty(q)=\lim_{j\to\infty}F_{t_j}(q)\), provided that limit exists on the query domain. No convergence of fields is needed to pass the exact equalities. Formula (2) at the limit additionally requires \(C^1\) regularity of the limit; it is not inferred from pointwise convergence.

**Sharpness of what symmetry forces.** For \(\kappa>-1\), the bounded smooth function

\[
F_{\rm base}(q)=\frac{\tanh\alpha}{\tanh a}
\]

satisfies every displayed predictor symmetry, interpolates \(F(p_1)=F(p_2)=1\), and vanishes only on \(\alpha=0\). Thus symmetry and interpolation force no additional zero points.

They also do not rule out additional zeros. With \(c=\tanh a>0\), the bounded smooth functions

\[
F_\lambda(q)=\frac{\tanh\alpha}{c}
\left[1+\lambda\bigl(\tanh^2\alpha-c^2\bigr)\right]
\tag{3}
\]

have the same symmetries and interpolation values. If \(\lambda>c^{-2}\), they vanish on two additional planes

\[
\alpha=\pm\operatorname{artanh}\sqrt{c^2-\lambda^{-1}}
\]

and have the opposite sign to \(\alpha\) between the central and these additional planes. This is a counterexample to an inference from symmetry plus fitting, not a claimed reachable \(q=1\) trajectory or a finite-width witness. An all-time or endpoint sign theorem must use a further property of the population dynamics.

### Degenerate geometries

If \(\kappa=1\), the signed samples coincide. Their fields and memories coincide by uniqueness, and the predictor is of the form \(\Phi_t(\alpha,\|q-\alpha p_1\|)\), odd in \(\alpha=q\cdot p_1\). Its mandatory plane is \(p_1^\perp\). All conclusions about normal-form insufficiency remain valid, with \(a=1\); there is no antisymmetric channel.

If \(\kappa=-1\), the signed samples are antipodal with equal target \(+1\). The supplied zero-readout initialization yields the exact arrested trajectory

\[
A_t=A_0,\quad W_t=V_{1,t}=V_{2,t}=0,\quad
K_{a,t}=H_0(p_a),\quad \tau_t=1+t,\quad F_t(q)=0.
\]

Indeed \(G_2=-G_1\), so \(\dot W=G_1+G_2=0\); \(D_a=L_a=0\), and the key differences vanish. All equations are satisfied, and uniqueness selects this trajectory. This includes equal labels at opposite original inputs and opposite labels at identical original inputs. No fitting or nonzero normal direction is possible in this case. For \(d=1\), the signed data necessarily fall into one of these two degenerate cases.

## 3. Exact two-channel population equations

For \(-1<\kappa<1\), define \(h_\pm=(H_1\pm H_2)/2\), and use the same half-sum and half-difference convention for \(g,k,v,D,L\). The signed memory representation is exactly

\[
B=T+v_+\otimes k_+ +v_-\otimes k_-,\qquad
(v\otimes k)f=v\langle k,f\rangle_1.
\tag{4}
\]

Synchronization reduces the equations to

\[
\begin{split}
\dot W&=-2e\,g_+,\\
\dot A&=-2e\,(aL_+e_++bL_-e_-),\\
\dot v_\pm&=-2e\,D_\pm,\\
\dot k_\pm&=\frac{|e|}{\tau}(h_\pm-k_\pm),\qquad
\dot\tau=|e|.
\end{split}
\tag{5}
\]

All components of \(A\) perpendicular to the training span are therefore exactly constant, but that statement alone does not make them independent of the trained population state.

Sample-swap symmetry makes every deterministic scalar inner product of an even and an odd sample channel zero. Here is the full justification, without a neuronwise equality: transform a trajectory by \(A\mapsto SA\), \(K_a\mapsto K_{\sigma(a)}\), \(V_a\mapsto V_{\sigma(a)}\), \(W\mapsto W\), where \(\sigma\) swaps the samples and \(T\) is unchanged. Direct substitution gives the trajectory with first-layer initialization \(SA_0\), whose complete initialized law is the same by Hypothesis 2. Every plus channel is unchanged and every minus channel is negated. A deterministic scalar population observable that changes sign must consequently be zero. In particular,

\[
\begin{gathered}
\langle k_+,h_-\rangle_1=\langle k_-,h_+\rangle_1=0,
\qquad \langle k_+,k_-\rangle_1=0,\\
\langle v_+,D_-\rangle_2=\langle v_-,D_+\rangle_2=0,
\qquad \langle v_+,v_-\rangle_2=0,
\qquad\langle W,g_-\rangle_2=0.
\end{gathered}
\tag{6}
\]

If only predictor-level equivariance were available, rather than the full scalar-state equivariance in Hypothesis 2, (6) would require that extra hypothesis. The normal-form theorem itself needs only predictor-level equivariance.

Let \(z_\pm=(Z_1\pm Z_2)/2\). Equations (4) and (6) give

\[
z_+=Th_++v_+\langle k_+,h_+\rangle_1,\qquad
z_-=Th_-+v_-\langle k_-,h_-\rangle_1.
\tag{7}
\]

The nonlinearity couples these channels:

\[
g_+=\frac{\sinh(2z_+)}{\cosh(2z_+)+\cosh(2z_-)},\qquad
g_-=\frac{\sinh(2z_-)}{\cosh(2z_+)+\cosh(2z_-)},
\tag{8}
\]

and

\[
D_+=W(1-g_+^2-g_-^2),\qquad D_-=-2Wg_+g_-.
\tag{9}
\]

For completeness, set \(P_\pm=B^*D_\pm\). Then

\[
\begin{split}
P_+&=T^*D_++k_+\langle v_+,D_+\rangle_2,\\
P_-&=T^*D_-+k_-\langle v_-,D_-\rangle_2,\\
L_+&=(1-h_+^2-h_-^2)P_+-2h_+h_-P_-,\\
L_-&=(1-h_+^2-h_-^2)P_--2h_+h_-P_+.
\end{split}
\tag{10}
\]

These formulas use the actual adjoint of the same \(T\); they make no Gaussian resampling or independence replacement. Equations (8)–(10) show why the scalar residual does not close the dynamics into one feature channel.

### A sharp initial consequence: the memory correction has rank two

**Theorem 2 (intrinsic activation of both memory channels).** Under Hypotheses 1–3 and \(-1<\kappa<1\), as physical time \(t\downarrow0\),

\[
\begin{split}
v_+(t)&=2t^2g_{+,0}(1-g_{+,0}^2-g_{-,0}^2)+o_{L^2}(t^2),\\
v_-(t)&=-4t^2g_{+,0}^2g_{-,0}+o_{L^2}(t^2).
\end{split}
\tag{11}
\]

Both leading coefficients are nonzero in \(L^2(\Omega_2)\). Both keys \(k_\pm(t)\) are nonzero for all sufficiently small positive \(t\). Consequently the memory correction \(B_t-T\), as a map from population 1 to population 2, has rank exactly two for every sufficiently small positive \(t\).

**Proof.** Initially \(e=-1\), \(W=0\), and (5) gives

\[
W(t)/t\longrightarrow2g_{+,0}\quad\hbox{in }L^2.
\]

Since training activations are bounded and continuous in \(L^2\), products in (9) give

\[
D_+(t)/t\to2g_{+,0}(1-g_{+,0}^2-g_{-,0}^2),\qquad
D_-(t)/t\to-4g_{+,0}^2g_{-,0}
\]

in \(L^2\). For example, replace \(W(t)/t\) by its bounded limiting function and use \(L^2\) convergence of the bounded activation factors; the remaining error is bounded by a constant times the \(L^2\) readout error. Integrating \(\dot v_\pm=-2eD_\pm\), with \(e(t)\to-1\), proves (11).

Let \(v_0=\mathbb E[\tanh(N)^2]>0\) and \(c_0=\langle H_{1,0},H_{2,0}\rangle_1\). Because the first-layer Gaussian pair has correlation \(-1<\kappa<1\), neither \(H_{1,0}-H_{2,0}\) nor \(H_{1,0}+H_{2,0}\) vanishes almost surely. Their squared norms are \(2(v_0-c_0)\) and \(2(v_0+c_0)\), respectively. Hence \(-v_0<c_0<v_0\), and Hypothesis 3 makes \((Z_{1,0},Z_{2,0})\) a nondegenerate Gaussian pair.

Since tanh is injective and odd, \(g_{+,0}=0\) precisely when \(Z_{1,0}+Z_{2,0}=0\), and \(g_{-,0}=0\) precisely when \(Z_{1,0}-Z_{2,0}=0\). Both events have probability zero. Also

\[
1-g_{+,0}^2-g_{-,0}^2
=\tfrac12[(1-G_{1,0}^2)+(1-G_{2,0}^2)]>0.
\]

Therefore both coefficients in (11) have positive \(L^2\) norm. The same first-layer argument shows \(k_{\pm,0}=h_{\pm,0}\ne0\), and continuity preserves nonzeroness for small time. By (6), \(k_+,k_-\) are orthogonal and so are \(v_+,v_-\). Equation (4) maps each nonzero key direction to its corresponding nonzero, orthogonal value direction; its rank is exactly two. ∎

This is a population statement about the actual \(q=1\) memory perturbation. It does not depend on a finite-width witness, a dense trained reference, or a claim that the trajectory eventually fits.

## 4. Strict initial query sign from the initialized Gaussian law

The mandatory plane is also the complete zero set of the *initial predictor velocity*. This needs only the initialized forward covariance law in addition to the flow assumptions.

For centered Gaussian \(X,Y\) with variances \(v,w>0\) and covariance \(c\in(-\sqrt{vw},\sqrt{vw})\), define

\[
J_{v,w}(c)=\mathbb E[\tanh X\,\tanh Y].
\]

It is odd in \(c\), and

\[
\frac{d}{dc}J_{v,w}(c)
=\mathbb E[\operatorname{sech}^2X\,\operatorname{sech}^2Y]>0.
\tag{12}
\]

Here is the required covariance identity rather than an external theorem citation. Write the Gaussian density

\[
\varphi_c(x,y)=\frac1{2\pi\sqrt{vw-c^2}}
\exp\left[-\frac{wx^2-2cxy+vy^2}{2(vw-c^2)}\right].
\]

Direct differentiation gives \(\partial_c\varphi_c=\partial_x\partial_y\varphi_c\). For a fixed interior covariance, differentiation under the integral is justified on a small covariance neighborhood by a Gaussian integrable bound for the density derivatives. Integrating twice by parts moves the two spatial derivatives onto the tanh factors; bounded derivatives and Gaussian decay remove the boundary terms. This proves (12). Sending \(Y\mapsto-Y\) proves oddness. A representation by two independent standard normals proves continuity at the two covariance endpoints by bounded convergence. Positivity of (12) on every interior interval therefore gives strict monotonicity on the closed covariance interval as well.

For a query of norm \(R>0\), let

\[
C_R(s)=J_{1,R^2}(s),\qquad
v(R)=\mathbb E[\tanh(RN)^2],\qquad
k_R(s)=J_{v(1),v(R)}(C_R(s)),\qquad |s|\le R.
\]

Both maps being composed are odd and strictly increasing. Thus \(k_R\) is odd and strictly increasing. By Hypothesis 3,

\[
\langle G_0(p_a),G_0(q)\rangle_2=k_R(p_a\cdot q).
\]

Because \(W_0=0\) and \(\dot W_0=G_{1,0}+G_{2,0}\), differentiation of the readout at time zero gives

\[
\dot F_0(q)=k_R(p_1\cdot q)+k_R(p_2\cdot q).
\tag{13}
\]

For \(-1<\kappa<1\), the arguments are \(a\alpha+b\beta\) and \(a\alpha-b\beta\). If \(\alpha>0\), the first is greater than the negative of the second, so strict monotonicity and oddness give

\[
k_R(a\alpha+b\beta)>-k_R(a\alpha-b\beta).
\]

The reversed inequality holds for \(\alpha<0\); at \(\alpha=0\) the sum is zero. At \(q=0\), it is also zero. Therefore

\[
\operatorname{sign}\dot F_0(q)
=\operatorname{sign}\bigl((p_1+p_2)\cdot q\bigr),\qquad \kappa>-1.
\tag{14}
\]

For \(\kappa=1\), (13) is twice one strictly increasing odd kernel, proving the same conclusion. For \(\kappa=-1\), (13) vanishes identically, as required by the arrested trajectory.

In particular, for each fixed query off the mandatory plane there exists a positive time interval, potentially depending on the query, on which \(F_t(q)\) has the sign in (14). The statement follows from \(F_t(q)=t\dot F_0(q)+o(t)\). It does not assert one common interval for all unbounded queries or all queries arbitrarily near the plane. At the training points it also proves

\[
\dot f(0)=\langle G_{1,0}+G_{2,0},G_{1,0}\rangle_2
=2\|g_{+,0}\|_2^2>0\qquad(\kappa>-1),
\]

where the equality uses the vanishing even/odd cross inner product. This initial strict sign is not propagated to later time by a new Gaussian-independence assumption; the needed later-time positivity theorem remains open.

## 5. Claim separation and remaining bottleneck

| Claim | Result and indispensable qualifications |
|---|---|
| Binary sign gauge | Exact algebra for the supplied equations; no Gaussian-law assumption needed. |
| Signed residual synchronization | Exact under unique deterministic population equivariance. |
| Full-query normal form and mandatory plane | Exact on every existence interval; inherited by pointwise endpoint limits. |
| Largest symmetry-forced zero set | Precisely the stated plane for \(\kappa>-1\); the whole predictor is zero for the initialized \(\kappa=-1\) case. |
| Two-channel equations and orthogonality | Exact under full scalar-state equivariance and true adjoint reuse. |
| Rank-two \(q=1\) memory near initialization | Proved under initial joint Gaussian forward law and the stated \(L^2\) continuity. |
| Initial query sign law | Proved under that initial Gaussian law, with no trained Gaussian or independence assumption. |
| No additional zeros for every positive time or at a fitted endpoint | Open; neither symmetry nor interpolation implies it. |
| Existence and identification of the canonical Gaussian population flow | Assumed foundation, not replaced by the abstract operator notation. |
| Global fitting and endpoint existence | Not established by this route. |

The strongest surviving obstruction to the full boundary claim is a sign change of the amplitude \(\Psi_t\) away from the training orbit. Equation (3) proves that symmetry, smoothness, boundedness, and exact interpolation alone do not exclude it. The coupled equations (8)–(10), together with the nonzero antisymmetric memory in (11), prevent discarding the minus channel as a shortcut. A further sign-preserving or comparison property for the actual reused-mixing population dynamics is the precise missing bridge.

The author check reconstructed the gauge transformation, orthogonal covariance, all parity identities, endpoint passage, all coefficients in (11), the Gaussian covariance derivative, and both degenerate geometries directly from the supplied equations. No external theorem, numerical test, experiment, fitted dense reference, finite-width trajectory, or trained-neuron independence argument was used. These checks support the conditional statements above, not the unresolved stronger endpoint claim.
