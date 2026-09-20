# Fixed-depth tanh foundations assessment

This is a bounded author assessment for C-X3, not an independent review or a completed depth-extension theorem. The intended target is the maintained two-hidden-layer tanh C-H3/C-H4 program at three hidden layers first and then every separately fixed finite depth. No training, numerical integration, certificate execution, or Git write was performed.

The strongest defensible conclusion is that the maintained library already supplies the exact local finite-dataset population system at every fixed depth. It does not supply an all-depth tanh opposite-label reference through substantial training. The reference's signed symmetry and radial-readout fitting argument have an architecture-independent algebraic extension, but their required strong-flow continuation and finite-network bridge remain missing. Strict activity of each sample in every layer is a separate missing bridge; aggregate gradient energy does not prove it.

## 1. Read coverage and scope

All source reads used the unchanged maintained files at HEAD `bcee9782651c34ae1204d37186e5c57e9282b273`; `git diff --stat` was empty for the three scientific files below.

- `docs/NOTATION.md`: complete.
- `docs/global_nonlinear.md`, lines 2454–3835: complete C introduction and C.1–C.3, including the weighted-loss correction at the end of C.3.
- `docs/global_nonlinear.md`, lines 1840–2453: complete A.1–A.4 and B/B.1, including the exact-GD restriction and affine-first exception.
- `docs/global_nonlinear.md`, lines 5475–6103: complete C.4.5.1, read after the supervisor explicitly added it to this assignment. This includes all five subunits and the printed rational certificate; the certificate was read, not executed.
- `docs/global_nonlinear.md`, lines 1–184: complete introduction and Section 1 theorem statement/architecture. Its later proof was not read and is not being newly audited here.
- `docs/special_data_limits.md`, lines 1–24, 2095–2152, and 3507–3784: family map, complete Theorem II.1 statement/architecture, and complete III.M model/theorem unit. These establish model boundaries only; their global proofs were not audited.
- Heading/keyword searches in maintained `docs/` identified those units. No other study, study history, another agent's report, research chat, or unpromoted result was read.
- Skills: complete `solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and its `research-contract.md` and `adversarial-audit.md`. No experiment reference was needed because computation was not authorized for this subtask.

The full fixed-Gaussian-program proof underlying A.1–A.2 was not reread. It is an explicit maintained dependency through those specializations, not a new theorem proved by this assessment. C-H3/C-H4's closure proofs are assigned to the supervisor and are not assessed here.

## 2. What is already maintained

| Source | Available conclusion | Boundary for C-X3 |
|---|---|---|
| C.1–C.2 | Every separately fixed `L≥2`, fixed finite weighted dataset, tanh allowed; unique autonomous strong local population flow; actual finite GF and every deterministic `eta_n→0` raw-GD sequence converge in the stated prediction, kernel, same-layer path-Wasserstein-2, probe and integrated-speed topologies. | Local time only. Fixed-dataset convergence, even though its constants are uniform in dataset size under the stated bounds. No continuum-law/growing-data limit or numerical finite closure follows from those constants alone. |
| C.3 | Two hidden layers, Gaussian initialization, positive variances/mobilities, zero limiting readout, nonzero labels and pairwise nonparallel normalized inputs: each input moves in both layers, each block is positive definite/nonconstant at small positive times, strict loss descent and nonaffinity. | Its reuse/noncancellation proof is explicitly two-layer. C.2 explicitly disclaims arbitrary-depth strict activity. |
| B.1 | Two hidden layers; orthogonal data; bounded top activation and bounded limiting readout, including zero. Tanh qualifies. Global strong population flow and finite GF/raw GD on every compact horizon. | B.1 uses `eta_n sqrt(n)→0` for its global raw-GD bridge. The nonlinear first-layer proof does not cover arbitrary Gram geometry. Its affine-first exception changes the target model. |
| C.4.5.1 | Actual two-layer tanh orthogonal opposite-label reference, global feature flow, fitting endpoint, whole-circle endpoint convergence, explicit `T=40` margins, and paired hidden activity at `t=1/200`. | The feature-flow existence argument and explicit margins were proved at `L=2`; its early activity result is not a displacement assertion at `T=40`. |
| Global nonlinear Section 1 | Every fixed `L≥3`, global fitting and every-layer activity for **one datum and `1+arctan(z)/10`**. | This is not an all-depth tanh theorem. Its positive activation floor and one-input setting cannot be silently substituted. |
| Special-data II / III.M | Three-layer shifted-arctan equal-label theorem; separately fixed-depth theorem for `a(1+z)+e psi(z)` with a large affine gain. | Neither is the two-opposite-label tanh reference. The nonzero affine part in III.M cannot be set to zero while retaining its theorem. |

At zero limiting readout C.1 admits the specified finite stored Gaussian readout of standard deviation `1/n`, by its vanishing RMS perturbation argument. The limit's zero readout does not authorize setting the actual finite initialization to zero. No arbitrary-depth result here asserts `L=L(n)→∞`.

## 3. Exact state and causal skeleton

Let `u_a=x_a/sqrt(d)`, `G_ab=u_a·u_b`, and use the probability-weighted loss

\[
\mathcal L=\sum_a\omega_a(f_a-y_a)^2,\qquad \omega_a>0,\quad\sum_a\omega_a=1.
\]

There are **L separate populations** \(\mathcal H_\ell=L^2(\Omega_\ell)\) and **L−1 initialized actions**
\(A_\ell:\mathcal H_{\ell-1}\to\mathcal H_\ell\), \(2\le\ell\le L\), each with its actual adjoint. Write \(W^{(\ell)}=A_\ell+B_\ell\); only \(B_\ell\) is a Hilbert–Schmidt trained increment. A full-row formulation retains \(w\in L^2(\Omega_1;\mathbb R^d)\), \(Z_a^{(1)}=w\cdot u_a\), and \(c=W^{(L+1)}\in\mathcal H_L\). With \(\phi=\tanh\),

\[
H_a^{(\ell)}=\phi(Z_a^{(\ell)}),\quad
Z_a^{(\ell)}=W^{(\ell)}H_a^{(\ell-1)}\ (\ell\ge2),\quad
f_a=E_L[cH_a^{(L)}],\quad r_a=f_a-y_a,
\]
\[
\Delta_a^{(L)}=c\phi'(Z_a^{(L)}),\qquad
\Delta_a^{(\ell)}=\phi'(Z_a^{(\ell)})(W^{(\ell+1)})^*\Delta_a^{(\ell+1)}.
\]
\[
\begin{aligned}
\dot w&=-2\kappa_1\sum_b\omega_b r_b\Delta_b^{(1)}u_b,\\
\dot B_\ell&=-2\kappa_\ell\sum_b\omega_b r_b\Delta_b^{(\ell)}\otimes H_b^{(\ell-1)},\quad 2\le\ell\le L,\\
\dot c&=-2\kappa_{L+1}\sum_b\omega_b r_bH_b^{(L)}.
\end{aligned}
\tag{F1}
\]

The full-row equation is the direct raw finite update's population form; its projection gives C.1's proved finite-dataset equation. Constructing it on a common full-input space and integrating arbitrary laws remains part of the requested continuum extension. The finite rank-one representative is `uv^T/n`; initialization variances never multiply the trained terms. For unit mobilities the raw increment metric is

\[
\|\delta\theta\|_{\rm raw}^2
=\|\delta w\|_2^2+\sum_{\ell=2}^L\|\delta B_\ell\|_{\rm HS}^2+\|\delta c\|_2^2.
\tag{F2}
\]

The original finite stored-block mobilities remain `n kappa_1,kappa_2,...,kappa_L,n kappa_(L+1)`. For nonunit mobilities, divide each squared block norm in (F2) by its mobility multiplier when invoking gradient identities.

The kernel blocks and identities are

\[
K^{(1)}_{ab}=G_{ab}E_1[\Delta_a^{(1)}\Delta_b^{(1)}],\quad
K^{(\ell)}_{ab}=E_{\ell-1}[H_a^{(\ell-1)}H_b^{(\ell-1)}]E_\ell[\Delta_a^{(\ell)}\Delta_b^{(\ell)}],
\]
\[
K^{(L+1)}_{ab}=E_L[H_a^{(L)}H_b^{(L)}],\qquad
K=\sum_{\ell=1}^{L+1}\kappa_\ell K^{(\ell)},\qquad
\dot f=-2K\operatorname{diag}(\omega)r,
\]
\[
\dot{\mathcal L}=-4(\operatorname{diag}(\omega)r)^TK(\operatorname{diag}(\omega)r).
\tag{F3}
\]

At `L=3`, the distinct state is `w,B_2,B_3,c`, on three populations; replacing `A_3 A_2` by a single action loses the intermediate tanh gate and both backward reuse structures.

### Reuse obligations that a depth proof must retain

C.2 gives a separate response system for each initial matrix, with named forward slots \(\xi^{(\ell)}\), reverse slots \(\eta^{(\ell)}\), and covariance laws

\[
E[\xi_{ak}^{(\ell)}\xi_{bs}^{(\ell)}]
=\sigma_\ell^2E_{\ell-1}[H_{ak}^{(\ell-1)}H_{bs}^{(\ell-1)}],\quad
E[\eta_{ak}^{(\ell)}\eta_{bs}^{(\ell)}]
=\sigma_\ell^2E_\ell[\Delta_{ak}^{(\ell)}\Delta_{bs}^{(\ell)}].
\]

The orientation innovation families can be independent while the *actual actions* retain their deterministic response terms. They cannot be replaced by independent forward/backward matrices. Named-source differentiation freezes deterministic coefficients, contractions and covariance laws, and does not differentiate through an expectation. C.2's single reverse pulse retains the factor `Delta omega_b`. Its forward response caps are chosen bottom-up and reverse caps top-down, before selecting a positive interval. This is the maintained noncircular local construction, with constants depending on depth.

All expectations and products in these recursions are typed to one population. Identifying neuron indices across layers, treating `A_ell` as an iid continuum integral kernel, or approximating all its relevant action by an unproved Hilbert–Schmidt tail are forbidden substitutions. A numerical hierarchy must preserve the same adjunction under its actual discrete inner products and control both orientations on generated reachable fields. Merely storing finitely many operator symbols is not finite-dimensional closure.

## 4. Local consequences that extend without a new global theorem

The following are deductions from C.1 and the elementary C.3 arguments, not a claim that C.3 already states an all-depth theorem. Assume positive variances/mobilities, Gaussian first roots, normalized pairwise nonparallel inputs, and every label nonzero. Put \(p_a=\omega_a y_a\), \(Q^{(\ell)}_{ab}=E_\ell[H_{0,a}^{(\ell)}H_{0,b}^{(\ell)}]\).

1. C.3's ridge independence proves \(Q^{(1)}\succ0\), even when \(G\) is singular. If \(Q^{(\ell-1)}\succ0\), the initialized \(Z_0^{(\ell)}\) is a full-support Gaussian tuple. A dependence \(\sum_a v_a\tanh Z_{0,a}^{(\ell)}=0\) therefore holds everywhere; varying one coordinate forces its coefficient to vanish. Hence every \(Q^{(\ell)}\succ0\).
2. Set \(S=\sum_a p_aH_{0,a}^{(L)}\). Then \(\|S\|_2^2=p^TQ^{(L)}p>0\), and (F3) gives \(-\dot{\mathcal L}(0)=4\kappa_{L+1}\|S\|_2^2>0\). Continuity preserves strict loss descent for a sufficiently short interval.
3. Every initialized hidden marginal is a nondegenerate Gaussian. Its variance and tanh best-affine-fit error are positive. C.1's mean-square continuity preserves common positive lower bounds for the finitely many sample/layer marginals on a shorter interval.

The exact onset recursion also extends. Use \(U_a^{(\ell)}\) for the initial backward coefficients (not a new random matrix):

\[
U_a^{(L)}=\phi'(Z_{0,a}^{(L)})S,\qquad
U_a^{(\ell)}=\phi'(Z_{0,a}^{(\ell)})A_{\ell+1}^*U_a^{(\ell+1)}.
\]
\[
M_\ell=\kappa_\ell\sum_b p_bU_b^{(\ell)}\otimes H_{0,b}^{(\ell-1)},\quad
V_a^{(1)}=\kappa_1\sum_bG_{ab}p_bU_b^{(1)},
\]
\[
V_a^{(\ell)}=M_\ell H_{0,a}^{(\ell-1)}
+A_\ell\{\phi'(Z_{0,a}^{(\ell-1)})V_a^{(\ell-1)}\},\quad 2\le\ell\le L.
\tag{F4}
\]

Successive division of the integral equations by `t` and `t²`, using strong bounded-multiplier continuity, gives

\[
c(t)=2\kappa_{L+1}tS+o_{L^2}(t),\quad
\Delta_a^{(\ell)}(t)=2\kappa_{L+1}tU_a^{(\ell)}+o_{L^2}(t),
\]
\[
B_\ell(t)=2\kappa_{L+1}t^2M_\ell+o_{\rm op}(t^2),\quad
Z_a^{(\ell)}(t)-Z_{0,a}^{(\ell)}
=2\kappa_{L+1}t^2V_a^{(\ell)}+o_{L^2}(t^2),
\]
\[
\dot Z_a^{(\ell)}(t)/t\to4\kappa_{L+1}V_a^{(\ell)},\quad
[H_a^{(\ell)}(t)-H_{0,a}^{(\ell)}]/t^2
\to2\kappa_{L+1}\phi'(Z_{0,a}^{(\ell)})V_a^{(\ell)}.
\tag{F5}
\]

Thus every-layer per-input onset reduces to proving \(V_a^{(\ell)}\ne0\) in mean square. Since tanh's derivative is everywhere positive, this also gives activation motion; its derivative need not have a uniform positive lower bound. The two terms in (F4) cannot be declared noncancelling from their separate norms.

There is a further aggregate consequence. Put \(D^{(\ell)}_{ab}=E_\ell[U_a^{(\ell)}U_b^{(\ell)}]\) and

\[
E_* =\kappa_1p^T(G\circ D^{(1)})p
+\sum_{\ell=2}^L\kappa_\ell p^T(Q^{(\ell-1)}\circ D^{(\ell)})p.
\]

All terms are nonnegative Gram energies. C.3's full-support proof, applied to the top initialized tuple and nonzero `p_a`, proves \(D^{(L)}\succ0\); therefore \(E_*>0\). Repeated adjunction in (F4) gives
\(\sum_ap_aE_L[U_a^{(L)}V_a^{(L)}]=E_*\): the terminal learned-action term gives the `ell=L` summand, and each preceding adjunction gives the next summand until the first-layer term remains. Expanding the hidden and readout kernel blocks in (F5) then yields

\[
p^TK(t)p=\kappa_{L+1}\|S\|_2^2
+8\kappa_{L+1}^2E_*t^2+o(t^2).
\tag{F6}
\]

Consequently the total kernel is locally nonconstant at every fixed depth. The top hidden learned action also has nonzero onset on each `H0_a^(L−1)`: its coefficient against the positive-definite tuple `U_b^L` has nonzero `a` entry `kappa_L p_a Q^(L−1)_aa`. These facts do **not** prove positivity of every lower backward covariance, nonzero `V_a^ell` for all layers, or every block's strict positivity. The missing activity lemma should prove the recursive unused-Gaussian variance after **all** relevant adjacent forward/adjoint calls, or provide an alternative per-input noncancellation proof. C.3's one-matrix calculation is a guide, not an induction already carried out.

## 5. Conditional all-depth opposite-label fitting route

Fix unit mobilities, unit initialization variances, two orthogonal normalized inputs `e1,e2`, equal weights `1/2`, labels `+1,−1`, and zero population readout. Let \(\vartheta=(w,B_2,\ldots,B_L)\) contain all hidden blocks and define

\[
h(\vartheta)=\tfrac12(H_1^{(L)}-H_2^{(L)}),\quad
b=E_L[ch],\qquad J_\vartheta=D h.
\]

Here `J` is the bounded directional differential from the hidden raw Hilbert space to \(\mathcal H_L\), obtained by the full forward differential recursion; its adjoint uses every actual \(W^{(\ell)*}\). No unrestricted Fréchet claim for the L2-valued tanh map is needed. On any strong feature solution,

\[
c_s=h,\qquad\vartheta_s=J_\vartheta^*c,
\qquad c_{ss}=J_\vartheta J_\vartheta^*c,
\qquad b_s=\|h\|_2^2+\|J_\vartheta^*c\|_{\rm hidden}^2
=\|\theta_s\|_{\rm raw}^2.
\tag{F7}
\]

The chain/product rules of A.4 justify these identities at any finite depth. For the norm `g=||c||2>0`,

\[
g_s=b/g,\qquad
g_{ss}=\{\|h\|_2^2-(g_s)^2+\|J_\vartheta^*c\|^2\}/g\ge0.
\tag{F8}
\]

At initialization, the two forward coordinates remain independent centered Gaussians at each layer because oddness makes every preceding cross covariance zero. Define

\[
q_1=E\tanh^2G,\qquad q_\ell=E\tanh^2(\sqrt{q_{\ell-1}}G),
\qquad m_L=\|h(0)\|_2^2=q_L/2>0.
\tag{F9}
\]

Since `c(s)=s h(0)+o(s)`, (F8) gives `g_s(0+)=sqrt(m_L)` and hence
\(b_s\ge m_L\) throughout the strong solution's positive interval. A first positive zero of `g` is impossible because `g≥s sqrt(m_L)`.

The exchange/readout-sign transformation from C.4.5.1 extends algebraically: swap the two input coordinates of `w`, leave all hidden actions unchanged, and send `c` to `−c`. Adjoining the transformed programs to the canonical construction preserves initialization law. **Provided uniqueness is available on the interval**, it gives deterministic population predictions `f1=b=−f2`. This is law symmetry, not exact symmetry of a finite initialized network. The physical mean-loss equation is then the feature equation with

\[
ds/dt=2(1-b),\qquad e(t)=1-b(s(t)),\qquad e_t=-2b_s e.
\tag{F10}
\]

If a unique strong feature flow is constructed through its first level `b=1`, that level occurs at `s_dagger≤1/m_L`; the same bounded-derivative clock argument as C.4.5.1 gives all physical times and

\[
0<e(t)\le e^{-2m_Lt},\qquad R_{\nu_*}(f(t))\le e^{-4m_Lt}.
\tag{F11}
\]

Also, for `s1≤s2≤s_dagger`, Cauchy–Schwarz in (F7) gives

\[
\|\theta(s_2)-\theta(s_1)\|_{\rm raw}
\le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))},\quad
\|\theta(s(t))-\theta(s_\dagger)\|_{\rm raw}\le e(t)/\sqrt{m_L}.
\tag{F12}
\]

These imply, conditionally, `||c||2≤m_L^(−1/2)` and every action norm at most \(B_L=2+m_L^{-1/2}\). The whole-circle prediction gradient has squared raw norm bounded by

\[
C_L^2=1+m_L^{-1}\sum_{j=0}^{L-1}B_L^{2j}.
\]

The first-row block contributes the last power, the successive matrix blocks contribute the remaining powers, and the readout contributes one. The straight segment between endpoint/reference states retains these bounds, so

\[
\sup_{|u|=1}|f(t,u)-f(\infty,u)|
\le C_Lm_L^{-1/2}e^{-2m_Lt}.
\tag{F13}
\]

This supplies a possible depth-dependent useful horizon once the missing strong construction is proved. It does not inherit the two-layer numerical constants or `T=40`.

### The exact missing bridge

At `L=2`, C.4.5.1's transformed equation is locally Lipschitz because the only remaining varying gate multiplies the bounded readout `c`; its first gate is absorbed into scalar first-row clocks. Its explicit polynomial bounds then give global feature continuation.

At `L=3`, even with the first gate removed, differentiating the second-layer gate produces

\[
[\phi'(Z^{(2)})-\phi'(\widetilde Z^{(2)})]\,
(W^{(3)})^*\Delta^{(3)}.
\]

The reused backward factor is generally unbounded. Bounded actions and bounded `c` do not give its coordinate supremum. This is precisely the term for which C.1–C.2 obtain local source-tail localization. The required all-depth fitting theorem must provide continuation and uniqueness through the necessary feature interval—e.g. by controlling those source tails/response coefficients on the reached orbit—and identify actual finite GF/raw GD there.

The raw length estimate (F12) prevents norm escape and gives a Cauchy endpoint while `b≤1`; it does **not** itself prove local existence or uniqueness at that trained endpoint. C.1 is an original-initialization theorem, not an arbitrary-trained-state theorem. The raw vector field is continuous, but a finite-dimensional Peano/Picard continuation conclusion cannot be imported into this Hilbert setting without its hypotheses. This is a major missing bridge, not a counterexample to the route.

## 6. Remaining obligations and counterchecks

The smallest decisive foundations problem is: construct and uniquely continue the **three-layer tanh orthogonal opposite-label reference** until its first feature level `b=1`, with its two reused initialized actions and actual finite-GF identification. Equations (F7)–(F13) then supply fitting and endpoint control. The same proof should explicitly state which bounds can be iterated at every separately fixed depth before any all-depth claim is made.

Further independent obligations are:

- Extend C.1's finite-dataset result to a compatible full-row/action model over the entire input circle and obtain quantitative law stability on a genuinely nonorthogonal/nonatomic class. Uniform-in-`m` local bounds do not prove this completion.
- Prove the per-input, every-layer noncancellation lemma for (F4), with positive margins on the specified law family. Early activity suffices if that is the contract; activity at the substantial-training endpoint is stronger and is not inherited.
- Carry the neighborhood evolution, paired observables, numerical closure, source-error control, quadrature adjunction, and autonomous restart property through the useful horizon. Stability without a vanishing closure source error is insufficient. These closure-specific units are outside this subtask's read scope.
- State which actual finite algorithm is captured. C.1's every-vanishing-step result is local; B.1's global sufficient step condition is stronger. Neither supplies an unspecified all-depth global-GD claim.

Concrete boundary checks:

1. Identical inputs with opposite labels give `S=0` and a frozen zero-readout population; antiparallel inputs with odd tanh and equal labels do likewise. Data/label nondegeneracy cannot be dropped from strict-onset claims.
2. Zero labels, zero mobility, or zero variance can destroy layerwise strictness although C.1's existence theorem still applies. The nonzero `p_a` requirement is separate from existence.
3. All hidden initial speeds are zero at zero readout. Positive onset means order-`t` RMS speed and order-`t²` displacement at small positive times, not a speed lower bound at `t=0`.
4. For unit-variance tanh, `0<q_(ell+1)<q_ell` because `|tanh z|<|z|` off zero. Continuity of the recursion forces `q_ell→0`. Hence (F9) supplies no depth-uniform positive fitting margin, and no depth-uniform nonaffinity margin is justified. This does not obstruct a separate theorem for every fixed depth.
5. Symmetry and the feature clock belong to the canonical population reference. Actual finite residuals need not remain exactly in the signed mode, and nearby nonorthogonal laws need not obey that scalar clock.
6. Paired initial/current activation displacement is not distance between separate marginals. It must remain paired in the observation family and finite approximation.
7. A radial-readout energy inequality proves progress of one signed mode; a positive aggregate kernel coefficient proves some hidden learning. Neither proves nonzero motion for every sample in every layer.
8. The two-layer explicit Gaussian certificate supplies only its printed constants. No three-layer or all-depth numerical margin has been evaluated here.

There is no fatal obstruction established by this assessment. There is also no maintained theorem that closes these bridges for the requested all-depth tanh model.
