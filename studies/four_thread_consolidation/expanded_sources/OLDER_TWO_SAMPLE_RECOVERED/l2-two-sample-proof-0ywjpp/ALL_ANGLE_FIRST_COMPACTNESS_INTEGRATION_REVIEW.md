# Independent integration audit: first-position and first-velocity compactness

Date: 2026-09-06.

## 1. Verdict, scope, and source identity

**The integration passes for the two actual finite schemes, with the proof supplements supplied below.** For each fixed finite horizon and each fixed \(|\rho|<1\), arctan gradient flow (GF) and exact simultaneous raw gradient descent (GD), with \(\eta_n=n^{-2}\) and the prescribed raw interpolation, satisfy every array premise in the compactness note. At \(\rho=-1\), with both activations odd and labels \((1,-1)\), the required invariant subspace is exact even with arbitrary nonzero readout. The first-position/velocity empirical laws, including both samples in the same neuron tuple, have quadratic-Wasserstein compact containment in probability in the product of uniform position topology and strong \(L^2\) velocity topology.

There is no unresolved dynamical premise for these conclusions under the stated initialization assumptions. This does not mean that deterministic uniform constants hold on every Gaussian outcome. The deterministic assertions require the stated initial norm and moment bounds; the Gaussian application discharges those bounds on explicit events of probability tending to one.

Two interface details merit an explicit supplement:

1. The compactness note states the antiparallel invariant identities without deriving them from the full finite model. Section 5 below derives them for arbitrary parameter values, the full GF vector field, the exact GD update, and the raw interpolation. This is a missing calculation, **not a failure of the invariant claim**.
2. The compactness note proves deterministic subsequential compactness, but does not state precise probability quantifiers. Its GD estimate with error \((h+\eta_n)^{2/3}\) directly supports a sequence argument with width tending to infinity. Passing to a single deterministic compact family that contains all good-event laws requires a little more explanation. Section 7 supplies a uniform translation estimate using the actual step structure of the GD preactivation velocity. Section 8 then gives the fixed-compact-set probability statement. This is a **proof-completion and quantifier supplement**, not a counterexample to the source's sequence conclusion.

Only the following three mathematical documents were read, in their entirety. No project material, prior review, history, external mathematical source, experiment, or agent was used. A procedural rigorous-math skill was read. Source files were not edited.

| Reference | File | Verified SHA-256 |
|---|---|---|
| F | `ALL_ANGLE_FIRST_LAYER_ACTION.md` | `9c0349c8aa76a6d7b260c34fd45a9e1d5dd8caf637a5ecbee0b16028bbd72ac9` |
| G | `ALL_ANGLE_RAW_GD_ACTION.md` | `95dd9f24b44245737bfd3cdcf4692383c24cacae84290d100deb2c21140a08e2` |
| V | `ALL_ANGLE_FIRST_VELOCITY_COMPACTNESS.md` | `a78c7439023d51e19e17b57e0105521a81fb09ccfc1920b32e97f376fdf6d742` |

All three files are in `/tmp/l2-two-sample-proof-0ywjpp/`. Source line references below refer to these verified versions.

The proof order is: verify the actual flow and update estimates; match every array premise with explicit constants; establish the singular-angle identities; check the relative-gate argument; prove joint strong compactness and its stochastic formulation. No population uniqueness, full mean-field identification, GF/GD comparison, or positive-time reverse-field tail claim is included.

## 2. Common setup and the exact metric factors

Fix \(T>0\). The case \(T=0\) reduces to initial-position laws, with a zero velocity space, and follows from the initial fourth-moment bound. Write

\[
\langle a_i\rangle_n=\frac1n\sum_{i=1}^n a_i,
\qquad
\|b\|_{n,2}=\langle |b_i|^2\rangle_n^{1/2}.
\]

A first-neuron field is a two-vector indexed by the two samples. Space-time norms use \(n^{-1}\sum_i dt\). Shifted norms always integrate over \([0,T-\tau]\), never outside the available trajectory.

To avoid conflating constants in the three notes, use \(A_{\rm op}\) for the middle-matrix norm bound, \(K_c\) for \(\sum_a|c_a|\), and \(K_z,J,A_{\rm kin},B_{\rm path},K_u\) for the five constants in V's array premises. Denote the first preactivation pair by \(z_i\), its actual time derivative by \(v_i\), the recomputed first activation pair by \(h_i\), and its derivative by \(w_i\). The controlled reverse pair and the gated pair are

\[
u_{a,i}=c_aq^{(1)}_{a,i},\qquad
d_i=\operatorname{diag}(p(z_i))u_i
\quad\hbox{in GF},\qquad p(s)=\frac1{1+s^2}.
\]

For GD, the definition of \(d\) uses the left-node values \(\bar z,u\). Here \(d_i\) is a two-vector; the ambient input dimension remains the scalar \(d\) in the original equations.

Arctan satisfies all activation assumptions in F and G: one can take

\[
B_1=B_2=\pi/2,\qquad P_1=P_2=1,\qquad L_1=L_2=1.
\]

Indeed \(\phi'=p\), \(\phi''(s)=-2s/(1+s^2)^2\), and \(|\phi''|\le1\). In addition, \(p>0\), arctan is odd, and \(p\) is even. The first two notes actually need only their weaker bounded-activation assumptions; V uses the additional relative-gate property.

The raw tangent norm is

\[
\|V\|_{\rm raw}^2
=\frac d n\|V^{(1)}\|_F^2+\|V^{(2)}\|_F^2
+\frac1n\|V^{(3)}\|^2.
\]

Direct differentiation of the finite prediction gives Euclidean gradients

\[
\nabla_{W^{(1)}}L=\frac2n\sum_a r_a\delta^{(1)}_a x_a^T,
\quad
\nabla_{W^{(2)}}L=\frac2n\sum_a r_a\delta^{(2)}_a(h^{(1)}_a)^T,
\quad
\nabla_{W^{(3)}}L=\frac2n\sum_a r_a h^{(2)}_a.
\]

Dividing by the metric weights shows that F's vector field is exactly \(-\operatorname{grad}_{\rm raw}L\), and G's update is exactly \(-\eta\operatorname{grad}_{\rm raw}L\). In particular, neither a sample-average factor nor a readout-rescaling factor is missing at the interface.

## 3. Verification of the action estimates for the actual schemes

### 3.1 GF: existence, reverse-field regularity, and pointwise work

F lines 62–79 correctly prove global finite-dimensional existence. The vector field is continuously differentiable and hence locally Lipschitz. Along its local solution,

\[
\frac{dL}{dt}=-\|\dot W\|_{\rm raw}^2.
\]

For any finite putative terminal time, the integrated squared raw speed is at most \(L(0)\). Cauchy–Schwarz bounds displacement over an interval of length \(s\) by \(\sqrt{sL(0)}\). At fixed \(n,d\), the raw metric is positive definite and equivalent to the usual finite-dimensional metric. Thus the trajectory is bounded, and its tail is Cauchy at a finite endpoint. Local existence at the endpoint extends it. This argument does not assume any limit dynamics.

Suppose \(\|W^{(2)}(0)\|_{\rm op}\le a\) and \(\|W^{(3)}(0)\|_\infty\le b\). F defines

\[
\begin{aligned}
R_0&=\sqrt2(B_2b+1),& K_c&=2\sqrt2R_0,\\
M&=b+B_2K_cT,&
A_{\rm op}&=a+B_1P_2\bigl(bK_cT+B_2K_c^2T^2/2\bigr),\\
Q&=A_{\rm op}P_2M.
\end{aligned}
\]

Loss decrease bounds the residual norm by \(R_0\), hence the sum of the absolute controls by \(K_c\). Integrating the readout equation bounds each readout coordinate by \(b+B_2K_ct\). A rank-one middle-layer update has operator norm equal to the product of its two Euclidean factor norms divided by \(n\); bounded activations and the readout bound then give the displayed \(A_{\rm op}\). Consequently, for each sample,

\[
\|\delta^{(2)}_a\|/\sqrt n\le P_2M,
\quad \|q^{(1)}_a\|/\sqrt n\le Q,
\quad \|\dot z^{(1)}_a\|/\sqrt n\le K_cP_1Q.
\]

The last inequality uses \(|C_{ab}|\le1\) in the exact projected first-layer equation. All are independent of the first-layer coordinate maximum.

The derivative estimates in F lines 100–123 also close without an unbounded product. In its notation,

\[
\begin{aligned}
D_A&=K_cP_2MB_1,&D_w&=K_cB_2,\\
D_Z&=D_AB_1+A_{\rm op}K_cP_1^2Q,\\
D_\delta&=D_wP_2+ML_2D_Z,\\
Q_1&=D_AP_2M+A_{\rm op}D_\delta.
\end{aligned}
\]

The product rules for \(z^{(2)}\) and \(\delta^{(2)}\) give RMS derivative bounds \(D_Z,D_\delta\). In the latter, multiplication by \(W^{(3)}\) is bounded coordinatewise by \(M\); no coordinate bound on \(q^{(1)}\) is used. Differentiating the actual transpose query gives

\[
\dot q^{(1)}_a=(\dot W^{(2)})^T\delta^{(2)}_a
+(W^{(2)})^T\dot\delta^{(2)}_a,
\qquad \|\dot q^{(1)}_a\|/\sqrt n\le Q_1.
\]

The three terms of F's kernel formula are exactly the three parameter contributions to \(\dot f\). Each entry is bounded by

\[
K_*=P_1^2Q^2+P_2^2M^2B_1^2+B_2^2.
\]

Thus \(\|K\|_{\rm op}\le2K_*\), \(\dot r=-2Kr\), and

\[
\sum_a|\dot c_a|\le8\sqrt2K_*R_0=:K'_c.
\]

In particular, the actual controlled field is differentiable and satisfies

\[
\|\dot u\|_{n,2}
\le\sum_a\bigl(|\dot c_a|\|q_a^{(1)}\|/\sqrt n
+|c_a|\|\dot q_a^{(1)}\|/\sqrt n\bigr)
\le K'_cQ+K_cQ_1=:K_u^{\rm F}.
\tag{R1}
\]

For

\[
U_i=\sum_a|u_{a,i}(0)|+\int_0^T\sum_a|\dot u_{a,i}(t)|\,dt,
\]

the triangle inequality in empirical \(L^2\), also applied inside the time integral, gives

\[
\|U\|_{n,2}\le K_cQ+TK_u^{\rm F}=:V_{\rm F}.
\tag{R2}
\]

For the first-layer row \(W^{(1)}_i\), put
\(E_i=\int_0^T d\|\dot W^{(1)}_i\|^2dt\). The exact equations give

\[
d\|\dot W^{(1)}_i\|^2=d_i^TCd_i
=\sum_a u_{a,i}\dot h_{a,i}.
\]

Integration by parts yields

\[
0\le E_i\le B_1\left(\sum_a|u_{a,i}(T)|+\sum_a|u_{a,i}(0)|
+\int_0^T\sum_a|\dot u_{a,i}|\right)\le2B_1U_i.
\tag{R3}
\]

Since the eigenvalues of \(C\) lie in \([0,2]\),

\[
|v_i|^2=|Cd_i|^2\le2d_i^TCd_i,
\qquad |v_i|\le2P_1U_i.
\]

Therefore

\[
\int_0^T|v_i|^2\le4B_1U_i,
\quad
\int_0^T|v_i|^3\le8B_1P_1U_i^2,
\quad
\sup_t|z_i(t)|^4\le8|z_i(0)|^4+128B_1^2T^2U_i^2.
\tag{R4}
\]

For the last inequality, the displacement is at most \(\sqrt{4B_1TU_i}\), and \((a+b)^4\le8(a^4+b^4)\). Also \(|w_i|\le P_1|v_i|\). These reproduce F's constants and provide its required per-neuron integrated-energy bound, including singular \(C\).

### 3.2 Exact GD: closing descent before using it

G lines 55–147 contain a valid first-exit argument. Put \(R=R_0+1\), \(K_c=2\sqrt2R\), \(H=T+1\), and

\[
M=b+B_2K_cH,\qquad
A_{\rm op}=a+HK_cP_2MB_1,\qquad Q=A_{\rm op}P_2M.
\]

Before the first residual-norm exit above \(R\), every old node used in an update has control sum at most \(K_c\). Summing those updates bounds the readout and middle matrix at both endpoints of each segment, including the candidate exit endpoint. Their norms remain bounded by \(M,A_{\rm op}\) throughout the segment by convexity. This inclusion of the candidate endpoint is what allows the descent proof to close.

Here is a check of the Hessian calculation, since assuming discrete descent would leave the application conditional. For a unit raw tangent \(V\), let

\[
\alpha_1=\sqrt{d/n}\|V^{(1)}\|_F,
\quad\alpha_2=\|V^{(2)}\|_F,
\quad\alpha_3=\|V^{(3)}\|/\sqrt n.
\]

Each is at most one. Then

\[
\|D_Vz^{(1)}_a\|/\sqrt n\le\alpha_1,
\quad
\|D_Vz^{(2)}_a\|/\sqrt n\le B_1\alpha_2+A_{\rm op}P_1\alpha_1.
\]

Set \(J_0=B_1+A_{\rm op}P_1\) and \(F_*=B_2+MP_2J_0\). Differentiating the prediction once gives \(|D_Vf_a|\le F_*\).

For another unit tangent \(U\), the mixed derivative of \(z^{(2)}\) has exactly the three terms displayed in G lines 104–107: two matrix/first-activation cross terms and the first-activation curvature term. The coordinatewise product bound

\[
\|s\odot t\|/\sqrt n
\le\sqrt n\,(\|s\|/\sqrt n)(\|t\|/\sqrt n)
\]

gives its RMS bound \(2P_1+A_{\rm op}L_1\sqrt n\). Differentiating the prediction twice adds two readout/hidden cross terms, bounded together by \(2P_2J_0\), a top-curvature term bounded by \(ML_2J_0^2\), and a term bounded by \(MP_2\) times the preceding RMS bound. Thus

\[
|D_UD_Vf_a|
\le2P_2J_0+ML_2J_0^2+MP_2(2P_1+A_{\rm op}L_1\sqrt n)
=F_{**}(n).
\]

In particular the width growth is at most \(\sqrt n\), not \(n\) or worse. The estimate for the top-curvature term uses the coordinate bound \(M\) and the Euclidean Cauchy–Schwarz inequality.

The raw update direction has norm at most \(K_cF_*\). Integrating the prediction differential along a raw segment gives a residual-norm increase of at most \(\sqrt2\eta K_cF_*^2\), so for sufficiently large \(n\) the entire segment has residual norm at most \(R+1\). The loss Hessian there is bounded by

\[
H_*(n)=4F_*^2+2\sqrt2(R+1)F_{**}(n).
\]

Taylor's integral formula along the actual update therefore gives

\[
L_{k+1}\le L_k-\eta\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2
+\tfrac12\eta^2H_*(n)\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2.
\]

Since \(\eta=n^{-2}\), both the segment-residual condition and \(\eta H_*(n)\le1\) hold beyond a deterministic threshold depending only on \(T,a,b\) and activation bounds. Descent then prevents the candidate exit. This proves actual node loss decrease and all preceding bounds through \(N=\lceil T/\eta\rceil\), without assuming them in advance.

### 3.3 Exact GD: the node variation and discrete work interfaces

The unspecified finite constants in G section 4 can be made explicit. Let

\[
\begin{aligned}
D_A&=K_cP_2MB_1,&D_w&=K_cB_2,&K_0&=K_cP_1Q,\\
D_Z&=D_AB_1+A_{\rm op}P_1K_0,\\
D_\delta&=D_wP_2+ML_2D_Z,\\
D_q&=D_AP_2M+A_{\rm op}D_\delta,\\
D_c&=4K_cF_*^2.
\end{aligned}
\]

The exact product differences, with the new middle matrix or readout placed next to the corresponding activation difference, prove

\[
\begin{gathered}
\|\Delta z^{(2)}_a\|/\sqrt n\le\eta D_Z,
\quad \|\Delta\delta^{(2)}_a\|/\sqrt n\le\eta D_\delta,
\quad \|\Delta q^{(1)}_a\|/\sqrt n\le\eta D_q,\\
\sum_a|\Delta c_a|\le\eta D_c.
\end{gathered}
\]

For the last estimate each prediction increment is bounded by \(\eta K_cF_*^2\), and \(c_a=-2(f_a-y_a)\). Expanding
\(\Delta(c_aq_a)=(\Delta c_a)q_{k,a}+c_{k+1,a}\Delta q_a\) gives

\[
\|u_{k+1}-u_k\|_{n,2}\le\eta(D_cQ+K_cD_q)=:\eta K_u^{\rm G}.
\tag{R5}
\]

It also gives the same bound with the empirical norm of the sum of the coordinatewise absolute sample increments, by the triangle inequality. Hence G's envelope satisfies

\[
\left\|\sum_a|u_{0,a,i}|+
\sum_{k=1}^{N-1}\sum_a|u_{k,a,i}-u_{k-1,a,i}|\right\|_{n,2}
\le K_cQ+(T+1)K_u^{\rm G}=:V_{\rm G}.
\tag{R6}
\]

This envelope uses nodes \(0,\ldots,N-1\), exactly the nodes generating the interpolated velocities. No control value at a nonexistent terminal cell is required. In particular \(\max_i U_i\le\sqrt nV_{\rm G}\) is available *before* the work argument.

At an old node let \(e_{k,i}=d_i^TCd_i\), so that

\[
\Delta z_i=\eta Cd_i,\qquad |\Delta z_i|^2\le2\eta^2e_{k,i}.
\]

Taylor expansion of the scalar first activation gives

\[
\sum_a u_{k,a,i}\Delta h_{a,i}=\eta e_{k,i}+R_{k,i},
\quad
|R_{k,i}|\le\tfrac12L_1U_i|\Delta z_i|^2
\le L_1\eta^2U_ie_{k,i}.
\]

For sufficiently large \(n\), \(\eta L_1\max_iU_i\le L_1V_{\rm G}n^{-3/2}\le1/2\). Discrete summation by parts bounds the sum on the left by \(2B_1U_i\), including both boundary terms. Thus, for the row action \(\mathcal A_i=\sum_{k=0}^{N-1}\eta e_{k,i}\),

\[
\mathcal A_i\le4B_1U_i.
\]

On the raw parameter interpolation the first preactivation is affine on each cell because \(z^{(1)}=W^{(1)}x\) is linear in \(W^{(1)}\). Its velocity is exactly the old-node value \(Cd_i\). Therefore, even on a partial final cell,

\[
\int_0^T|v_i|^2\le8B_1U_i,
\quad
\int_0^T|v_i|^3\le16B_1P_1U_i^2,
\quad
\sup_{t\le T}|z_i(t)|^4
\le8|z_i(0)|^4+512B_1^2(T+1)^2U_i^2.
\tag{R7}
\]

The recomputed activation obeys \(w_i=\operatorname{diag}(\phi'_1(z_i))v_i\) almost everywhere. No assertion that the activation is affine, or that hidden fields are interpolated from their nodes, enters this argument. The absorption threshold is independent of the empirical initial fourth moment and is not circular.

## 4. Every explicit premise of V, discharged

Let \(m_4=\langle|z_i(0)|^4\rangle_n\) be bounded by a fixed constant. The following table records valid choices for V lines 40–61. Constants \(K_c,Q,V_{\rm F},V_{\rm G}\) refer to the corresponding scheme above.

| Premise in V | Actual GF | Actual GD, for sufficiently large \(n\) |
|---|---|---|
| Correct arrays and regularity | \(z,u\) are differentiable; \(d=p(z)u\), \(\dot z=Cd\) | \(z\) is the raw affine interpolant; \(\bar z,u\) are left-node step fields; \(d=p(\bar z)u\), \(\dot z=Cd\) a.e. |
| Uniform RMS velocity \(K_z\) | \(\sqrt2K_cP_1Q\) | \(\sqrt2K_cP_1Q\) |
| Cubic space-time bound \(J^3\) | \(8B_1P_1V_{\rm F}^2\) | \(16B_1P_1V_{\rm G}^2\) |
| Integrated-energy bound \(A_{\rm kin}\) | \(4B_1V_{\rm F}\) | \(8B_1V_{\rm G}\) |
| Fourth position bound \(B_{\rm path}\) | \(8m_4+128B_1^2T^2V_{\rm F}^2\) | \(8m_4+512B_1^2(T+1)^2V_{\rm G}^2\) |
| RMS control derivative/increment | \(K_u^{\rm F}\) from (R1) | \(\lVert\Delta u_k\rVert_{n,2}\le\eta K_u^{\rm G}\) from (R5) |

In the fourth row, the precise premise is

\[
\left\langle\left(\int_0^T|v_i|^2dt\right)^2\right\rangle_n^{1/2}
\le A_{\rm kin}.
\]

It follows by squaring the pointwise estimates \(\int|v_i|^2\le4B_1U_i\) or \(8B_1U_i\) and using the empirical second moment of \(U\). It is not inferred merely from a mean kinetic-energy bound. The cubic bound would itself supply some quadratic tails of the \(L^2\) path norm, but does not by itself justify V's advertised fourth moment; the pointwise work estimate does.

At GD mesh nodes, derivatives are understood almost everywhere or with the right-interior/left-terminal convention in G. With that convention the uniform RMS bound holds as well. Neither a value at a single endpoint nor a partial final cell changes any norm used here.

For a time shift, integrating the GF derivative or summing crossed GD increments gives

\[
\|u(\cdot+\tau)-u\|_{L^2(n^{-1}\sum_i dt)}
\le\sqrt T K_u(\tau+e),\qquad e=0\text{ or }\eta.
\tag{R8}
\]

For GD the number of crossed increments is at most \(\tau/\eta+1\). The same reasoning gives

\[
\|\bar z(\cdot+\tau)-\bar z\|_{L^2}\le\sqrt T K_z(\tau+\eta),
\qquad
\|z(\cdot+\tau)-z\|_{L^2}\le\sqrt T K_z\tau.
\tag{R9}
\]

The latter estimate integrates the actual affine velocity. Thus every explicit array assumption, including temporal regularity of the correct controlled field and the distinction between node and recomputed quantities, is discharged for the actual schemes. Constants up to this point are independent of the angle. The next inverse estimate will depend on fixed \(\rho\).

## 5. Antiparallel invariance from the full finite model

This supplies the calculation omitted at V lines 84–90. Assume \(\rho=-1\), both activations are differentiable and odd, and \((y_1,y_2)=(1,-1)\). Input normalization gives

\[
\|x_1+x_2\|^2=2d+2d\rho=0,
\qquad x_2=-x_1.
\]

For **every** choice of the finite matrices and readout, before imposing any differential equation or initialization symmetry,

\[
z^{(1)}_2=-z^{(1)}_1,
\quad h^{(1)}_2=-h^{(1)}_1,
\quad z^{(2)}_2=-z^{(2)}_1,
\quad h^{(2)}_2=-h^{(2)}_1,
\quad f_2=-f_1.
\tag{R10}
\]

These follow successively from linearity of each matrix action, oddness of the two activations, and linearity of the readout. A differentiable odd function has even derivative: differentiating \(\phi(-s)=-\phi(s)\) gives \(\phi'(-s)=\phi'(s)\). Consequently

\[
\delta^{(2)}_2=\delta^{(2)}_1,
\quad q^{(1)}_2=q^{(1)}_1,
\quad \delta^{(1)}_2=\delta^{(1)}_1.
\tag{R11}
\]

In particular multiplication by the common readout in \(\delta^{(2)}\) preserves equality for an arbitrary nonzero vector. Also

\[
r_2=-f_1+1=-(f_1-1)=-r_1,
\qquad c_2=-c_1.
\tag{R12}
\]

No claim that \(f_1(0)=0\), or that the readout is initially zero, was used.

Substitution into the full GF equations reduces them to

\[
\dot W^{(1)}=\frac{2c_1}{d}\delta^{(1)}_1x_1^T,
\quad
\dot W^{(2)}=\frac{2c_1}{n}\delta^{(2)}_1(h^{(1)}_1)^T,
\quad
\dot W^{(3)}=2c_1h^{(2)}_1.
\tag{R13}
\]

Substitution into the exact simultaneous GD equations gives increments equal to \(\eta\) times precisely these expressions evaluated at the old node. Every new set of weights again satisfies the algebraic identities (R10)–(R12); so do all intermediate raw parameter interpolants. This is stronger than invariance of a specially initialized parameter submanifold: the paired identities are enforced by the input relation and architecture at every parameter value.

Specializing these identities to the arctan arrays audited here, \(z_i=(s_i,-s_i)\), \(u_i=(c_1q_{1,i},-c_1q_{1,i})\), and evenness of the first gate gives \(d_i=(a_i,-a_i)\). Since

\[
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}(a_i,-a_i)^T
=2(a_i,-a_i)^T,
\]

the exact GF velocity, and the exact GD cell velocity using old-node \(d\), obey

\[
v_i=2d_i,\qquad |d_i|=|v_i|/2.
\tag{R14}
\]

This proves exactly the substitute for \(C^{-1}\) required by V. The random readout distribution \(N(0,n^{-2})\) is fully compatible with it. Oddness of both activations and the opposite labels are hypotheses of this endpoint argument; the first two notes alone, with arbitrary bounded activations and labels, would not discharge that particular invariant claim. Both-arctan with the specified labels does discharge it. The aligned endpoint is outside this review.

## 6. Relative gates and strong velocity translations

For generic fixed \(|\rho|<1\), the eigenvalues of \(C\) are \(1+\rho\) and \(1-\rho\), so

\[
\|C^{-1}\|_{\rm op}=\frac1{1-|\rho|}.
\]

Set \(\kappa_\rho=(1-|\rho|)^{-1}\) in this case, and \(\kappa_{-1}=1/2\) in the invariant antiparallel case. Equations \(v=Cd\) and (R14), respectively, imply

\[
\|d\|_{L^3(n^{-1}\sum_i dt)}\le\kappa_\rho J=:D.
\tag{R15}
\]

This is a bound for the actual gated controlled pair. It makes no assertion about unrestricted multiplication by a reverse field.

The logarithmic derivative of \(p\) has absolute value at most one. For positive \(p(x),p(y)\),

\[
\theta(x,y):=\frac{|p(x)-p(y)|}{p(x)+p(y)}
=\tanh\!\left(\frac{|\log p(x)-\log p(y)|}{2}\right)
\le\min(1,|x-y|/2).
\]

If \(a=p(x)u\), \(b=p(y)v\), then

\[
\begin{aligned}
|a-b|&\le p(x)|u-v|+\theta(p(x)+p(y))|v|\\
&\le p(x)(1+\theta)|u-v|+\theta(|a|+|b|)\\
&\le2|u-v|+\theta(|a|+|b|).
\end{aligned}
\]

The middle step uses \(p(x)|v|\le|a|+p(x)|u-v|\). Applying this to both sample coordinates, taking their maximum \(\theta_i\), and using the Euclidean triangle inequality proves V's two-vector estimate with the same constants. There is no division by a residual or controlled field.

Take the two times \(t,t+\tau\), using \(z\) in GF and \(\bar z\) in GD. Since \(0\le\theta_i\le1\),

\[
\|\theta\|_{L^6}^6
\le\|\theta\|_{L^2}^2
\le\tfrac14\|\Delta_\tau z_{\rm gate}\|_{L^2}^2
\le\tfrac14TK_z^2(\tau+e)^2.
\]

Hölder's inequality, with \(1/2=1/6+1/3\), and the bounds for the two shifted copies of \(d\) give the explicit estimate

\[
\|\Delta_\tau d\|_{L^2}
\le2\sqrt T K_u(\tau+e)
+2D(TK_z^2/4)^{1/6}(\tau+e)^{1/3}.
\tag{R16}
\]

Multiplying by \(C\), whose norm is at most two, proves V's velocity translation estimate. The two shifted \(L^3\) norms are each bounded by the norm on the full interval, so there is no endpoint extension assumption. For \(\tau+e\le T+1\), the linear term can be absorbed into the one-third power with a constant depending on \(T\). Thus

\[
\|\Delta_\tau v\|_{L^2}^2\le C_{T,\rho}(\tau+e)^{2/3}.
\tag{R17}
\]

For the recomputed first activation, write

\[
\Delta_\tau w
=\operatorname{diag}(p(z(t+\tau)))\Delta_\tau v
+\operatorname{diag}(p(z(t+\tau))-p(z(t)))v(t).
\]

Let \(\beta_i\) be the maximum absolute gate difference over the two samples. Since \(0<p\le1\) and \(|p'|\le1\),

\[
\beta_i\le\min(1,|z_i(t+\tau)-z_i(t)|),
\quad
\|\beta\|_{L^6}\le(TK_z^2)^{1/6}\tau^{1/3}.
\]

Therefore

\[
\|\Delta_\tau w\|_{L^2}
\le\|\Delta_\tau v\|_{L^2}+J(TK_z^2)^{1/6}\tau^{1/3}.
\tag{R18}
\]

This verifies the activation-velocity claim for both schemes, including the distinction between \(p(\bar z)\) in the GD update and \(p(z)\) in the derivative of the recomputed activation. Constants may diverge as a generic fixed \(\rho\) approaches an endpoint. No conclusion for a sequence of such correlations is taken here.

## 7. Joint quadratic-Wasserstein compactness and the GD family supplement

### 7.1 Projection, fourth moments, and sequence compactness

Use the separable Banach space

\[
\mathcal E_T=C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)
\times C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2),
\]

with squared norm

\[
\|(z,v,h,w)\|_{\mathcal E_T}^2
=\|z\|_\infty^2+\|v\|_2^2+\|h\|_\infty^2+\|w\|_2^2.
\]

The empirical measure is

\[
\mu_n=\frac1n\sum_i\delta_{(z_i,v_i,h_i,w_i)}.
\]

The two sample coordinates remain paired in every component. Dropping \((h,w)\) gives exactly the product space in V's display (12). Here \(W_2\) is the infimum, over couplings, of the root mean square distance for the displayed norm.

For a uniform partition with mesh \(h=T/m\), let \(P_h\) be the cell-average operator on velocities and \(\Pi_h\) the polygon through the position values at partition nodes. Expansion of the square on one cell \(I\) gives

\[
\int_I|v-P_hv|^2
=\frac1{2h}\int_I\int_I|v(t)-v(s)|^2\,ds\,dt.
\]

Splitting the double integral into its two ordered halves and enlarging from within-cell pairs to all pairs separated by \(\tau<h\) proves

\[
\langle\|v_i-P_hv_i\|_2^2\rangle_n
\le\frac1h\int_0^h\|\Delta_\tau v\|_{L^2}^2\,d\tau
\le C_{T,\rho}(h+e)^{2/3}.
\tag{R19}
\]

The same proof applies to \(w\). Since positions are absolutely continuous, for a cell \([a,b]\) of length \(h\) and \(t\in[a,b]\),

\[
z(t)-\Pi_hz(t)=\int_a^t v(s)ds-\frac{t-a}{h}\int_a^b v(s)ds.
\]

Each integral is bounded by \(\sqrt h\|v\|_{L^2([a,b])}\), so

\[
\langle\|z_i-\Pi_hz_i\|_\infty^2\rangle_n
\le4h\langle\|v_i\|_2^2\rangle_n\le4hTK_z^2.
\tag{R20}
\]

The same holds for \(h_i\), since \(|w_i|\le|v_i|\). The notation \(h_i\) for the activation and \(h\) for the mesh has distinct roles in this formula.

The precise fourth-moment bounds are

\[
\langle\|z_i\|_\infty^4\rangle_n\le B_{\rm path},
\quad\langle\|v_i\|_2^4\rangle_n\le A_{\rm kin}^2,
\quad\|h_i\|_\infty^4\le4B_1^4,
\quad\|w_i\|_2^4\le\|v_i\|_2^4.
\]

Consequently

\[
\int\|X\|_{\mathcal E_T}^4d\mu_n(X)
\le4(B_{\rm path}+2A_{\rm kin}^2+4B_1^4)=:M_4.
\tag{R21}
\]

Both averaging and polygonal interpolation are contractions for the respective norms, so the same fourth-moment bound holds for the same-neuron projected law of
\((\Pi_hz_i,P_hv_i,\Pi_hh_i,P_hw_i)\). This law lives in a fixed finite-dimensional subspace for each fixed mesh.

For completeness, a uniform fourth moment proves finite-dimensional \(W_2\) precompactness as follows. Move all mass outside a ball of radius \(R\) to zero; this costs at most \(M_4/R^2\) in squared distance. Cover the remaining finite-dimensional ball by finitely many cells of diameter at most \(\epsilon\), and move their masses to cell representatives, at cost at most \(\epsilon^2\). On a fixed finite set the vectors of masses form a compact simplex, and convergence of masses gives \(W_2\) convergence: the common masses can be coupled identically and the unmatched mass costs at most the squared diameter times its total mass. Sending \(R\) to infinity and \(\epsilon\) to zero proves total boundedness.

The same-neuron coupling bounds the squared \(W_2\) error of projection by the sum of (R19) and (R20) for the four coordinates. For GF this goes uniformly to zero with \(h\). For a deterministic sequence of GD arrays with \(n\to\infty\),

\[
\lim_{h\downarrow0}\limsup_{n\to\infty}
W_2(\mu_n,(\Pi_h,P_h,\Pi_h,P_h)_\#\mu_n)=0.
\]

A diagonal subsequence on countably many finer meshes is \(W_2\)-Cauchy by the triangle inequality. The relevant metric space is complete. One can see the needed completeness directly by approximating a Cauchy subsequence by finite-support laws with summable \(W_2\) errors, coupling consecutive finite laws using transport matrices, and gluing the matrices using their common marginals. The resulting random points \(X_j\) have \(\sum_j\|X_{j+1}-X_j\|_{L^2}<\infty\). Thus their distances are summable almost surely and their tails tend to zero in \(L^2\), by the triangle inequality. Completeness of \(\mathcal E_T\) gives a limit with finite second moment, whose law is the required \(W_2\) limit. This justifies the passage from total boundedness or a Cauchy subsequence to a subsequential probability law.

These details verify V's deterministic compactness proof. Discarding finitely many terms is valid for a sequence containing one selected law per width. By itself, that sentence does not address the union of every possible random outcome at each of the finitely many widths. The next argument establishes a single compact family uniformly over all good outcomes.

### 7.2 Uniform GD translation estimate for compact containment

The actual GD preactivation velocity \(v\) is a step field on the uniform mesh \(\eta\), with \(\|v(t)\|_{n,2}\le K_z\). For \(0<\tau\le\eta\), the fields \(v(t+\tau)\) and \(v(t)\) differ only when an internal mesh point lies between the two times. There are at most \(T/\eta\) such points, and each occupies an interval of starting times of length at most \(\tau\). At every such time,
\(\|v(t+\tau)-v(t)\|_{n,2}^2\le4K_z^2\). Therefore

\[
\|\Delta_\tau v\|_{L^2}^2\le4TK_z^2\frac\tau\eta,
\qquad 0<\tau\le\eta.
\tag{R22}
\]

Fix \(0<\tau<\min(1,T)\) and split at \(\delta=\tau^{3/5}\). If \(\eta\le\delta\), (R17) bounds the squared norm by
\(C(\tau+\delta)^{2/3}\le C2^{2/3}\tau^{2/5}\). If \(\eta>\delta\), then \(\tau\le\eta\) and (R22) bounds it by \(4TK_z^2\tau^{2/5}\). Thus all these GD arrays satisfy

\[
\|\Delta_\tau v\|_{L^2}^2\le C_{T,\rho}\tau^{2/5},
\tag{R23}
\]

uniformly over widths and step sizes \(\eta\le1\) for which the already verified array bounds hold. For GF, (R17) with \(e=0\) implies this weaker exponent as well. Equation (R18) then gives (R23) for \(w\), because \(\tau^{2/3}\le\tau^{2/5}\) for \(\tau\le1\).

Inserting (R23) into the cell-average estimate gives a **uniform** squared projection error at most \(C_{T,\rho}h^{2/5}\). Together with (R20) and (R21), the preceding finite-dimensional covering argument proves total boundedness of the union of all the GF and GD empirical laws obeying the fixed constants. Its closure in \(\mathcal P_2(\mathcal E_T)\) is compact.

This supplement uses only the step structure already explicit in V's GD premise, its uniform RMS velocity bound, and its established relative-gate estimate. It introduces no new assumption on the optimizer, initialization, or model. The exponent is only used to obtain uniform compact containment; no optimal rate is claimed.

### 7.3 Derivative compatibility and absence of a first-layer energy defect

For the pair \((z,v)\), the set

\[
\mathcal S=\{(z,v):z(t)=z(0)+\int_0^t v(s)ds\ \text{for every }t\}
\]

is closed in uniform-position/strong-\(L^2\)-velocity topology, because

\[
\sup_{t\le T}\left|\int_0^t(v_j-v)\right|\le\sqrt T\|v_j-v\|_2.
\]

Each empirical law gives \(\mathcal S\) mass one, so any weak, hence any \(W_2\), limit does too. For example, this last assertion follows by applying weak convergence to the bounded continuous distance function \(\min(1,\operatorname{dist}(\cdot,\mathcal S))\), whose integrals are zero. The same reasoning preserves the activation derivative relation. More explicitly, uniform \(z_j\to z\) implies uniform \(p(z_j)\to p(z)\), and

\[
\|p(z_j)v_j-p(z)v\|_2
\le\|v_j-v\|_2+\|p(z_j)-p(z)\|_\infty\|v\|_2\to0.
\]

Hence limits are supported on \(h=\arctan z\), \(w=p(z)v\), and the appropriate integral identities.

If \(\mu_j\to\mu\) in \(W_2(\mathcal E_T)\), choose couplings with mean squared product distance tending to zero. Cauchy–Schwarz gives

\[
\left|\int\|v\|_2^2d\mu_j-\int\|v\|_2^2d\mu\right|
\le \bigl(\mathbb E\|v_j-v\|_2^2\bigr)^{1/2}
\left[\bigl(\mathbb E\|v_j\|_2^2\bigr)^{1/2}
+\bigl(\mathbb E\|v\|_2^2\bigr)^{1/2}\right]\to0.
\tag{R24}
\]

The bracket is bounded under \(W_2\) convergence, and also by the moment estimates here. The activation energy satisfies the same statement. This rules out a first-layer kinetic-energy defect along these strong joint-law convergences. It identifies the velocity as the path derivative; it does not identify the network equation generating the limiting velocity.

## 8. Gaussian application and precise probability quantifiers

Fix the correlation and normalized deterministic input pair, independently of initialization. The dimension may be any admissible dimension. In the antiparallel case impose the hypotheses of section 5. For each width define the actual initialization event

\[
E_n=\{\|W^{(2)}_0\|_{\rm op}\le8,\quad
\|W^{(3)}_0\|_\infty\le1,\quad
\langle|z_i(0)|^4\rangle_n\le13\}.
\]

The probability estimates in F and G are valid, including at \(\rho=-1\):

* Each initial first pair is Gaussian with covariance \(C\), and different rows are independent. Gaussian second/fourth moments give \(\mathbb E|z_i(0)|^4=8+4\rho^2\le12\). Also \((s+t)^4\le8(s^4+t^4)\) gives \(\mathbb E|z_i(0)|^8\le1680\) using the eighth moment \(105\) of each standard normal marginal. Chebyshev therefore bounds failure of the empirical fourth-moment event by \(1680/n\). A singular within-row covariance does not affect row independence or this calculation.
* A maximal \(1/4\)-separated sphere set has at most \(9^n\) points by the disjoint-ball volume bound. Approximation of both test vectors shows \(\|W^{(2)}_0\|_{\rm op}\le2\max_{u,v\text{ in net}}|u^TW^{(2)}_0v|\). Each fixed bilinear form is Gaussian of variance \(1/n\); its threshold-four tail is at most \(2e^{-8n}\). The union bound gives \(2\exp(-(8-2\log9)n)\).
* Each readout coordinate has variance \(n^{-2}\). The Gaussian exponential bound at threshold one, followed by the union bound, gives \(2n\exp(-n^2/2)\).

Thus, without needing independence between these three events,

\[
\mathbb P(E_n^c)\le b_n
:=\frac{1680}{n}+2e^{-(8-2\log9)n}+2ne^{-n^2/2}
\longrightarrow0.
\tag{R25}
\]

Take \(a=8,b=1,m_4=13\) in the preceding proofs. For every fixed \(T,\rho\) there are deterministic constants and a deterministic GD threshold \(n_0(T)\); generic-angle compactness constants may additionally depend on \(\rho\). By section 7 there is a deterministic compact set

\[
\mathcal K_{T,\rho}\subset\mathcal P_2(\mathcal E_T)
\]

containing every GF good-event law and every GD good-event law with \(n\ge n_0(T)\). It can be chosen to contain both schemes by taking the larger constants in their verified bounds. Consequently, for either scheme \(S\),

\[
\mathbb P\{\mu_n^S\notin\mathcal K_{T,\rho}\}\le b_n
\quad(n\ge n_0(T)),\qquad
\lim_{n\to\infty}\mathbb P\{\mu_n^S\in\mathcal K_{T,\rho}\}=1.
\tag{R26}
\]

If GF and GD use the same initialization, their joint containment in this compact set has failure probability at most \(b_n\), since the same \(E_n\) suffices. If they are initialized separately, a union bound gives at most \(2b_n\). Neither statement compares their trajectories or limits.

This is stronger than the usual asymptotic tightness formulation

\[
\forall\epsilon>0\ \exists\text{ compact }\mathcal K
\quad\limsup_{n\to\infty}\mathbb P(\mu_n^S\notin\mathcal K)\le\epsilon.
\]

It is a probability statement about a random empirical probability measure as a point of \(\mathcal P_2(\mathcal E_T)\). At finite width this random element is measurable: the finite equations and finite-step updates depend continuously on their initial data, with the interpolated paths and their \(L^2\) velocities continuous on bounded initial sets. In particular the compact-set events in (R26) have their usual meaning.

There are two useful tail formulations, with different objects being truncated. For the path-space tuple define

\[
F_n(R)=\int\|X\|_{\mathcal E_T}^2
\mathbf1_{\{\|X\|_{\mathcal E_T}>R\}}\,d\mu_n^S(X).
\]

On \(E_n\), (R21) gives \(F_n(R)\le M_4/R^2\). Hence, precisely,

\[
\forall\epsilon>0,\qquad
\lim_{R\to\infty}\limsup_{n\to\infty}
\mathbb P\{F_n(R)>\epsilon\}=0.
\tag{R27}
\]

For a pointwise-in-time velocity truncation, instead let

\[
G_n(R)=\left\langle\int_0^T|v_i(t)|^2
\mathbf1_{\{|v_i(t)|>R\}}dt\right\rangle_n.
\]

The cubic estimate gives \(G_n(R)\le J^3/R\) on \(E_n\), and the same ordered probability limits hold. The first expression controls quadratic tails of the norm of an entire path/velocity tuple; the second concerns a velocity value under empirical space-time measure. Both are valid here and should not be silently interchanged.

The resulting interpretation of subsequences is as follows:

* Deterministically, any selection of good-event laws at widths tending to infinity has a \(W_2\)-convergent subsequence. Limits satisfy the derivative compatibility and energy conclusion of section 7.3.
* For the original random laws, (R26) supplies compact containment in probability. It does **not** assert convergence in probability of \(\mu_n^S\), or that all subsequences have the same limit. No identification or uniqueness result has been used.
* If all widths are realized on one probability space, any deterministic width sequence admits a further subsequence with \(\sum_j b_{n_j}<\infty\). The union bound on the tail of this sum shows that only finitely many \(E_{n_j}\) fail almost surely. Along that further sequence, the random laws are almost surely relatively compact; a convergent subsubsequence can depend on the outcome. This is not an almost-sure statement along all widths, nor a deterministic subsequence converging in probability to an identified law.
* The good-event proof bounds no expectation of a tail functional on \(E_n^c\). In particular (R27) must not be promoted to expectation-level uniform integrability without additional estimates. Energy convergence in (R24) is along actual \(W_2\) convergence of laws and does not assert convergence of expectations over initialization.

The failure bound is uniform over deterministic normalized input pairs. The compactness statement above fixes \(\rho\); it does not assert a single initialization event controlling every input pair chosen after observing the weights. No sequence \(\rho_n\) approaching either endpoint is included. For each finite horizon the statements hold as written; a claim on an infinite horizon would require a specified local topology and a further diagonal formulation.

## 9. Final classification

| Item audited | Classification |
|---|---|
| Global actual finite GF and its action/variation bounds | Verified from F; no extra dynamical premise |
| Exact \(\eta_n=n^{-2}\) GD descent, variation, and work absorption | Verified from G for a deterministic sufficiently-large-width threshold; no assumed discrete stability |
| Every explicit array premise in V | Discharged by the table and calculations in section 4 |
| Generic fixed \(\lvert\rho\rvert<1\) relative-gate argument | Verified with \(\lVert C^{-1}\rVert=(1-\lvert\rho\rvert)^{-1}\) |
| Antiparallel case, including nonzero random readout | Correct; missing full-model calculation supplied in section 5; supplement, not failure |
| Joint uniform-position/strong-velocity \(W_2\) sequence compactness | Verified, including activation and derivative compatibility |
| A fixed compact family and precise in-probability claims | Supplied in sections 7.2–8 from existing array assumptions; quantifier supplement |
| Equality of GF/GD limits, limiting network-equation identification, population uniqueness, full MF conclusions, or reverse-field tails | Not established or asserted |

For the stated canonical Gaussian initialization, fixed generic correlation, and the separately specified antiparallel arctan case, the first-layer joint compactness conclusions are therefore actual probabilistic conclusions, not merely conclusions conditional on unverified array regularity.
