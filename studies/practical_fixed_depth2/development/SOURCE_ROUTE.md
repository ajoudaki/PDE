# Direct single-matrix source route: covariance contractions and energy controls

Status: partial rigorous progress, not a resolution of CONTRACT.md. No experiment is used. The exact activation throughout is

\[
\phi(z)=a(1+z)+e\tanh z,\qquad a=3/4,\quad e=1/4.
\]

The central new observation is that an entire initialized response row, after contraction against the true opposite-layer inputs, is an isometric transfer of a first Gaussian-chaos projection. Its norm and time energy admit contraction estimates independent of coefficient condition numbers. This does not bound its spatial tails: an explicit, exact repeated-matrix program below shows why.

## 1. Model, convention, and level of assertions

Write \(c_i=y_i-f_i\), \(u_i=x_i/\sqrt d\), \(\Gamma_{ij}=u_i^Tu_j\), and

\[
z_i=u_i^Tw,\quad h_i=\phi(z_i),\quad v_i=(A_0+U)h_i,
\quad k_i=\phi(v_i),\quad b_i=\phi'(v_i)C,
\quad q_i=(A_0+U)^*b_i,\quad d_i=\phi'(z_i)q_i.
\]

The actual raw field is

\[
\dot w=\sum_i c_i d_i u_i,\qquad
\dot U=\sum_i c_i b_i\otimes h_i,\qquad
\dot C=\sum_i c_i k_i.
\tag{1}
\]

All initialized calls below use the same genuine \(A_0\) and its adjoint. Expectations in source derivatives freeze previously generated deterministic coefficients and the physical residual controls. They do not differentiate these expectations or replace physical controls by ascent controls.

The finite-program source assertions are exact for finite smooth programs whose coordinate derivatives satisfy the fixed-program hypotheses, in particular at fixed incoming-field cap and fixed mesh. Extensions to an already-existing strong uncapped source path are conditional on its justified source identification. They are not an independent construction of that path.

For a genuine existing flow the energy identity gives, with \(E_0=E(0)\),

\[
\int_0^T\|\dot\Theta\|_{\rm raw}^2\,dt\le E_0,
\quad \|\Theta(t)-\Theta(0)\|_{\rm raw}\le\sqrt{tE_0}.
\tag{2}
\]

At population initialization \(C_0=0\) and binary \(\{-1,1\}\) labels give \(E_0=3/2\). The finite small Gaussian readout is not discarded in any finite-width claim; the estimates below with zero initial readout are explicitly population estimates. Put

\[
R=\sqrt{TE_0},\qquad H=a+1+R,\qquad L=\sqrt{6E_0}.
\]

Then \(\|c(t)\|_1\le L\), \(\|C(t)\|_2\le R\), \(\|h_i(t)\|_2\le H\). No inverse of \(\Gamma\) is used.

## 2. Entire responses are Gaussian-chaos contractions

Consider one finite source program, and pad its source lists by unavailable coordinates. Let \(\zeta=(\zeta_1,\ldots,\zeta_m)\) be the reverse source group, with covariance

\[
K_{st}=E[b_s b_t],
\]

where each index includes its time and sample. Let \(h\) be any forward input in the program. Set \(\alpha_s=E[\partial_{\zeta_s}h]\). The exact initialized forward response is

\[
\mathcal R_h=\sum_s\alpha_s b_s.
\tag{3}
\]

**Lemma 1 (basis-free response contraction).** Let \(P_\zeta\) denote orthogonal projection in the bottom \(L^2\) space onto the linear span of the centered Gaussian variables \(\zeta_s\). The linear map \(J_b\zeta_s=b_s\) is well-defined and isometric on that span, and

\[
P_\zeta h=\sum_s\alpha_s\zeta_s,
\qquad \mathcal R_h=J_bP_\zeta h,
\qquad \|\mathcal R_h\|_2\le\|h\|_2.
\tag{4}
\]

This holds for singular covariance matrices, and the result is independent of the chosen formal coefficient vector. For two inputs from one common finite program,

\[
\|\mathcal R_h-\mathcal R_{\tilde h}\|_2
\le\|h-\tilde h\|_2.
\tag{5}
\]

**Proof.** The two families \((\zeta_s)\) and \((b_s)\) have the same Gram matrix \(K\). Thus a linear relation of zero \(L^2\) norm in either family has zero norm in the other; this proves the well-defined isometry. Gaussian integration by parts, conditional on the independent roots and other source groups, gives

\[
E[\zeta_t h]=\sum_s K_{ts}\alpha_s.
\]

Consequently \(h-\sum_s\alpha_s\zeta_s\) is orthogonal to every \(\zeta_t\), proving the first identity. The second is (3). Orthogonal projection and isometry give (4) and (5). No nonsingularity or inverse covariance estimate appears. The integration-by-parts identity can be checked by writing \(\zeta=TG\) and integrating each independent standard Gaussian coordinate of \(G\); fixed capped finite programs have integrable derivatives, so that calculation is justified. ∎

Exactly the same argument for the forward Gaussian source group \(\xi\), whose covariance is \(E[h_s h_t]\), gives the reverse response

\[
\mathcal S_b=J_hP_\xi b,
\qquad \|\mathcal S_b\|_2\le\|b\|_2.
\tag{6}
\]

The full initialized identities are

\[
A_0h=\xi_h+\mathcal R_h,
\qquad A_0^*b=\zeta_b+\mathcal S_b.
\tag{7}
\]

The two summands within either identity need not be independent or orthogonal. In particular (4) does not imply an initialized action norm of \(\sqrt2\). All current and past returns remain inside the projection. At a top current call the diagonal source derivative remains

\[
E[C\phi''(v_i)],\qquad
\phi''(v)=-\tfrac12\operatorname{sech}^2(v)\tanh(v),
\]

and its absolute value is at most \(\tfrac12\|C\|_2\).

**Corollary 1 (time energy of the forward response).** On a common source realization, suppose \(h:[0,T]\to L^2\) is strongly absolutely continuous with square-integrable speed and (7) has already been justified along the path. Then

\[
\mathcal R_h(t)=J_bP_\zeta h(t),\qquad
\int_0^T\|\partial_t\mathcal R_h(t)\|_2^2dt
\le\int_0^T\|\dot h(t)\|_2^2dt.
\tag{8}
\]

**Proof.** Use the closed linear span of the complete source family. The Gram isometry extends by continuity to its completion. The projection and isometry are fixed bounded linear maps on that common space, so they commute with Bochner integration. Apply their norm bound to the derivative. Future correlated source coordinates cause no problem: Gaussian integration by parts shows that the finite chronological expression is the projection onto the complete finite group, even though its formal derivatives in unavailable coordinates are zero. A countable approximation then gives the same assertion on the closed span. ∎

This replaces coefficient-row control by invariant contraction estimates. It is strictly weaker than an estimate on an \(L^1\) row of source coefficients.

## 3. Energy alone already gives Gaussian tails for the primitive path drivers

The following simple Gaussian fact is useful. If \(X\) is a centered Gaussian random element in a real separable Hilbert space and \(S=E\|X\|^2<\infty\), then, for \(S>0\),

\[
E\exp\bigl(\|X\|^2/(4S)\bigr)\le e^{1/2}.
\tag{9}
\]

To prove this, diagonalize each finite-dimensional covariance compression with eigenvalues \(\lambda_j\ge0\). Its exponential moment equals \(\prod_j(1-\lambda_j/(2S))^{-1/2}\). Since \(\lambda_j/(2S)\le1/2\) and \(-\log(1-x)\le2x\) there, the product is at most \(\exp(\sum_j\lambda_j/(2S))\le e^{1/2}\). Increasing orthogonal projections and monotone convergence prove (9). A Hilbert-valued Gaussian with finite covariance trace is constructed by the convergent series of independent normal coordinates with square-summable variances; the same finite-dimensional argument applies. The zero-trace case is deterministic zero.

**Lemma 2 (primitive Gaussian drivers on a physical energy path).** Suppose a common source realization has been justified for an existing true flow on \([0,T]\). The three forward primitive sources \(\xi_i(t)\), with covariance \(\langle h_i(t),h_j(s)\rangle\), have jointly Gaussian versions with absolutely continuous paths. With

\[
S_f=\sum_i\left(\|h_i(0)\|_2^2+\int_0^T\|\dot h_i(t)\|_2^2dt\right)
\le3(a+1)^2+3E_0,
\]

they satisfy

\[
E\exp\left(\frac{\sum_i\sup_{t\le T}|\xi_i(t)|^2}
{4(1+T)S_f}\right)\le e^{1/2}.
\tag{10}
\]

The reverse primitive group can be realized as a jointly Gaussian \(L^2([0,T];\mathbb R^3)\) random element \(\zeta\). Its trace satisfies

\[
S_r=\sum_i\int_0^T\|b_i(t)\|_2^2dt
\le\frac32E_0T^2,
\]

and

\[
E\exp\bigl(\|\zeta\|_{L^2_t}^2/(4S_r)\bigr)\le e^{1/2}.
\tag{11}
\]

In particular its time integral has a Gaussian supremum tail, using \(\sup_t|\int_0^t\zeta_i|\le\sqrt T\|\zeta_i\|_{L^2_t}\).

**Proof.** Regard the vector-valued function \(h_i(t)\) as a deterministic path in the bottom Hilbert space and apply an isonormal Gaussian map \(G_f\) to \(h_i(0)\) and \(\dot h_i(t)\). The resulting Gaussian element in \(\mathbb R^3\oplus L^2_t(\mathbb R^3)\) has trace \(S_f\). Its integrated version has covariance \(\langle h_i(t),h_j(s)\rangle\), so it is the required forward source law. For every scalar absolutely continuous path, \(\sup_t|x(t)|^2\le(1+T)(|x(0)|^2+\int|\dot x|^2)\). Equation (9) proves (10). Since \(\dot h_i=\phi'(z_i)u_i^T\dot w\), its integrated squared norm is at most that of \(\dot w\), proving the stated trace bound. The offset is retained through \(\|h_i(0)\|_2\le a+1\).

For the reverse group apply an independent isonormal Gaussian map \(G_r\) to the deterministic Hilbert-valued map \(b_i(t)\). The covariance trace in \(L^2_t\) is \(S_r\). Since \(|\phi'|\le1\), \(\|b_i(t)\|_2^2\le\|C(t)\|_2^2\le tE_0\). Integrating and summing proves its trace bound; (9) proves (11). No reverse-source time derivative or independence of different times is required. ∎

These estimates need no bounded source coefficient row. They cannot be assigned directly to non-energy-preserving capped training curves: the required energy premise must be proved for the approximation being used.

**Corollary 2 (application to the energy-preserving caps).** Consider the root route's approximants which multiply the entire true first-row raw gradient by a common nonnegative cap factor at most one, cap the entire readout velocity in the same dissipative fashion, and leave the true learned-operator gradient unchanged. Suppose their extra ambient readout cap is inactive, as follows from the bounded readout rate. Their proved dissipation inequality supplies (2) uniformly in the cap. Therefore Lemma 2, and the return contraction and time-energy estimates, apply uniformly to their fixed-cap canonical source constructions. The proof uses only the query source law, the bounded derivative of \(\phi\), \(|b_i|\le|C|\), and the energy bound. It does not require uncapped dynamics or derivatives of the cap to be uniform. Equations (12)--(15) also remain exact because the operator update is unchanged.

## 4. What remains after separating the controlled terms

Write \(R_i(t)=\mathcal R_{h_i(t)}\), \(S_i(t)=\mathcal S_{b_i(t)}\). The exact uncut identities, whenever identified, are

\[
v_i(t)=\xi_i(t)+R_i(t)
+\int_0^t\sum_j c_j(s)b_j(s)\langle h_j(s),h_i(t)\rangle ds,
\tag{12}
\]

\[
q_i(t)=\zeta_i(t)+S_i(t)
+\int_0^t\sum_jc_j(s)h_j(s)\langle b_j(s),b_i(t)\rangle ds.
\tag{13}
\]

The learned terms have the pointwise bounds

\[
|(Uh_i)(t,\omega_2)|\le LH^2\int_0^t|C(s,\omega_2)|ds,
\tag{14}
\]

\[
|(U^*b_i)(t,\omega_1)|\le LR^2\int_0^t\max_j|h_j(s,\omega_1)|ds.
\tag{15}
\]

These follow directly from the rank-one raw update, \(|b_j|\le|C|\), and Cauchy--Schwarz for the deterministic contractions. Thus the primitive drivers and learned operator pieces have explicit energy-based bounds. The remaining issue is the spatial tail of the two aggregate initialized returns \(R,S\), or a direct comparison estimate avoiding those tails.

For example (4), (6), and (8) yield

\[
\sup_t\|R_i(t)\|_2\le H,\quad
\sup_t\|S_i(t)\|_2\le R,\quad
\int_0^T\|\dot R_i(t)\|_2^2dt\le E_0.
\]

These are useful, rank-invariant bounds but do not imply uniform integrability of squared returns across approximation levels.

## 5. An exact obstruction to upgrading covariance contraction to tails

The following does not disprove the requested physical-flow theorem. It rules out a tempting but invalid bridge: a general bound of the initialized action on subGaussian variables, or a general transfer of uniform subGaussian bounds by the response isometry.

Let \(1\) be the constant bottom input, \(Z=A_0 1\sim N(0,1)\), and let \(g_M=g_M(Z)\) be a smooth function valued in \([0,1]\) which is zero on \(( -\infty,M]\) and one on \([M+1,\infty)\). Such a function can be chosen with a derivative bound independent of \(M\). Put

\[
p_M=E[g_M(Z)^2],\qquad \mu_M=E[g_M'(Z)]=E[Zg_M(Z)].
\]

Query the genuine transpose and then the genuine forward action:

\[
q_M=A_0^*g_M=\zeta_M+\mu_M1,
\qquad E\zeta_M^2=p_M,
\]

\[
A_0q_M=\xi_M+g_M,
\qquad E\xi_M^2=p_M+\mu_M^2,
\qquad E[\xi_M Z]=\mu_M.
\tag{16}
\]

These identities follow from the exact two-orientation rule: the first reverse response is \(\mu_M1\), and the final forward input has derivative one with respect to \(\zeta_M\), producing the complete return \(g_M\). Thus

\[
A_0q_M=g_M(Z)+\mu_MZ+\sqrt{p_M}\,G,
\tag{17}
\]

where \(G\) is independent standard Gaussian. Each program is fixed and smooth, so this is within the finite-program theorem, without a trajectory continuation assertion.

The normalized inputs \(q_M/\sqrt{p_M}\) have uniformly bounded Gaussian-plus-constant subGaussian norms because \(|\mu_M|\le\sqrt{p_M}\). Their output tails are not uniformly square-integrable. Indeed

\[
E\left[\left(\frac{g_M(Z)}{\sqrt{p_M}}\right)^2\right]=1,
\]

and this variable is supported on \(\{Z>M\}\), whose probability tends to zero. The other terms \((\mu_M/\sqrt{p_M})Z+G\) are uniformly square-integrable; therefore their sum with \(g_M/\sqrt{p_M}\) cannot be uniformly square-integrable. To justify the last step, uniform integrability of both squared sums and squared Gaussian remainders would imply uniform integrability of their squared difference by \(|x-y|^2\le2|x|^2+2|y|^2\), a contradiction.

The input/output operation is precisely the same initialized matrix reused in both directions. Nothing here permits dropping return terms. It shows that covariance contraction and a bounded initialized \(L^2\) action, even together with uniformly Gaussian input tails, do not supply the spatial tail estimate needed for cap removal.

## 6. Claim registry and the exact open implication

| Claim | Status | Scope |
|---|---|---|
| Entire forward and reverse returns are isometric transfers of first Gaussian-chaos projections | Proved | Fixed admissible finite programs; singular covariance allowed |
| Aggregate return norm contraction, including differences on one common source program | Proved | Same source group and transfer map |
| Forward-return time-energy contraction | Proved conditionally | An already identified strong source path |
| Primitive forward-source supremum and integrated reverse-source Gaussian tails from physical energy | Proved conditionally | Existing genuine flow with source identification |
| Learned-return Volterra bounds retaining physical controls and offset | Proved conditionally | Existing genuine flow |
| Generic initialized action preserves subGaussian bounds/UI | False | Exact repeated-matrix counterexample (16)--(17) |
| Actual energy-stopped approximation returns have uniform spatial tails or strong Cauchy control | Open | This is the remaining implication |
| Global strong population flow, canonical uniqueness, and full GF/GD joint limit for the fixed activation | Not proved here | The open implication remains necessary for this route |

The concrete unresolved implication is: do actual energy-stopped physical approximations, started from the given Gaussian initialization, satisfy a cap-independent uniform-integrability or stronger tail estimate for the two transferred Gaussian-chaos projections in (12)--(13), sufficient for strong cap removal and uniqueness? Proving coefficient boxes is sufficient but not necessary; the contraction identities expose a weaker invariant target. The rare-event probe above is not physically reachable by construction, so it neither resolves that implication negatively nor excuses replacing it by an ambient-space theorem.

## 7. Finite endpoints of an established cap-removal interval

**Lemma 3 (strong endpoint for a uniformly dissipative approximation family).** Let \(\Theta_R:[0,\tau]\to\mathcal P\) satisfy

\[
\int_0^\tau\|\dot\Theta_R(t)\|_{\rm raw}^2dt\le E_0
\]

uniformly in \(R\), and suppose the family is Cauchy in \(C([0,t];\mathcal P)\) for every \(t<\tau<\infty\). Then it is Cauchy in \(C([0,\tau];\mathcal P)\).

**Proof.** For \(s\in[t,\tau]\),

\[
\|\Theta_R(s)-\Theta_S(s)\|_{\rm raw}
\le\|\Theta_R(t)-\Theta_S(t)\|_{\rm raw}
+2\sqrt{(\tau-t)E_0}.
\]

First choose \(t\) near \(\tau\), then choose \(R,S\) large enough for the preceding compact interval. Completeness gives the uniform strong limit through \(\tau\). Continuous forward propagation, bounded-multiplier continuity, and continuity of the genuine operator action give strong convergence of every actual field at the endpoint. In particular their squared magnitudes are uniformly integrable there. ∎

This does not by itself restart the flow beyond \(\tau\). Endpoint strong compactness gives vanishing tails without a quantitative decay rate; those tails need not dominate the exponential-in-cap propagation factor in a usual capped comparison. Thus a reached-state restart result exploiting strong endpoint compactness would be an alternative to a global subGaussian estimate, but it remains an additional theorem.
