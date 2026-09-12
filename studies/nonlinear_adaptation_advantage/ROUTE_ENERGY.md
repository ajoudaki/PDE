# Route E: finite-episode energy and semigroup comparison

Frozen independent candidate, 2026-09-12. Author: `/root/energy_route`.
Status: **partial mathematical results; E₀ unresolved; no promotion claim**.

The exact selected nonlinear episode admits a signed risk-difference formula,
an explicit quadratic-in-time bound on any advantage, and a finite scalar-clock
separation criterion. None proves a positive advantage. The missing assertion
is a uniform positive signed interaction between actual kernel deformation and
the propagated residual. Endpoint conditioning and energy dissipation do not
supply its sign. Complete counterexamples below invalidate generic substitutes
for that missing structural property.

## 1. Contract and established inputs

The assignment was the neutral RESEARCH_CONTRACT.md plus a finite-episode
variational/energy/semigroup approach. No experiments, subagents, other routes,
other studies, or scientific discussion from another route were used. Only
this file is written; no Git/index mutation is made.

Retain the contract's bias-free two-hidden-layer tanh network, physical input
x=sqrt(2)u, stored Gaussian variances (1,1/n,1/n²), mobilities (n,1,n), output
division by n, unhalved squared loss, and actual GF. Every actual network uses
its original arrays, including its random finite readout, and its original fixed
mixture (1-epsilon)nu_*+epsilon nu throughout. The known anchors have their exact
weights. The canonical slow clock is tau=epsilon t; no network is restarted.

The selected full raw state is theta=(w,K,c), with action A=A_0+K and its actual
adjoint. Only K is Hilbert–Schmidt. The raw norm is the sum of squared row-L²,
middle-Hilbert–Schmidt and readout-L² norms. The gradient g_theta, anchor map
G_theta and projection Pi_theta=I-G_theta(G_theta^*G_theta)^(-1)G_theta^*
are NSC1 exactly. Write d_theta(u)=Pi_theta g_theta(u), retaining all blocks.

The following are imported established results from C.4.10.2:

* There is one T_c>0 for all bounded-label added laws. The selected state solves
  theta'=-2 integral (f_theta-y)d_theta dnu, starts at the specified fitted
  endpoint, preserves its anchors, and is strongly C¹.
* Its common neighborhood satisfies |f|<=c_b, ||g(u)||<=L and
  M_theta>=k I/2. Scalar prediction has raw Lipschitz constant L.
* Control mass per unit slow time is at most A_s. The reached derivative
  calculation NSC25–NSC28 gives ||g_theta(u)'||<=T_g m(tau), m<=A_s,
  uniformly in input. This uses bounded readout and two L⁴ factors for the
  first-row product, not an ambient activation Hessian.
* NSC8 and NSC44–NSC51 capture the selection by actual original-mixture finite
  GF, width first at fixed positive contamination, contamination second.
  They provide no uniform finite-width rate over the task class.

Constants above are NSC3–NSC4 with label bound Y_0=1. At the endpoint
||d_dagger(u)||<=L_0. For E_N in NSS17, the endpoint force satisfies
||T_p a||²>=lambda_N||a||_p², with lambda_N>0 uniform over the declared
density class. Numerical lower bounds for these eigenvalues are not supplied.
The contained source proof already includes 225400 exp(2880)+180; no
practical conditioning or useful-sized episode is inferred from finiteness.

## 2. Ordinary four-coefficient family and quantitative nonstationarity

Fix 0<R<=1/8, s>=1 and cap N=1. Put A=R/32, B=R/(32·3^s), and r_v=R/256.
Use q_0=cos³(alpha)-sin³(alpha), h=sin²(2alpha), and

\[
q=q_0+h(v+w),\qquad
v=a_0\cos\alpha+b_0\sin\alpha+a_1\cos3\alpha+b_1\sin3\alpha,
\]
\[
a_0,b_0\in[A,2A],\quad a_1\in[B,2B],\quad b_1\in[-2B,-B],
\]
\[
\|w\|_{s,1}:=|w_{c,0}|+|w_{s,0}|
 +3^s(|w_{c,1}|+|w_{s,1}|)\le r_v,
\tag{E1}
\]

where w has the same cap. Four coefficients vary independently on intervals
of widths A,A,B,B. After perturbation each fundamental coefficient has
magnitude at least 7A/8, and each third-harmonic coefficient at least 7B/8.
The weighted budget is at most R/4+R/256<R. These are quantitatively active
components at the declared weighted scale, not merely optional directions
near a single witness.

For density use

\[
p=1+b,\quad \int b\,d\rho=0,\quad
\|b\|_\infty+\operatorname{Lip}_{circle}(b)\le1/4.
\tag{E2}
\]

Thus 3/4<=p<=5/4 and support is the full circle. The class lies in P_(1/4).
A center with Lipschitz norm at most 1/8 admits every zero-integral density
perturbation of that norm at most 1/8. Target robustness is relative to R.
In the four-dimensional anchored target space, every C¹ target perturbation
of norm at most

\[
r_q=\frac{R}{1024\sqrt{2+2\,3^{2s}}}
\tag{E3}
\]

is admitted by (E1). To verify this, the uniform-measure Gram of
h cos alpha,h sin alpha,h cos3alpha,h sin3alpha has diagonal 3/16,
cosine cross entry -1/8, sine cross entry +1/8, and other entries zero.
Its least eigenvalue is 1/16. Hence the Euclidean coefficient norm is
at most 4||delta q||_rho; Cauchy–Schwarz with weights proves (E3).
The topology is C¹ relative to this fixed-cap anchored subspace; robustness
to arbitrary targets outside it is not claimed.

Nonstationarity has an explicit margin. Let
psi_1=h(cos alpha+sin alpha), psi_3=h(cos3alpha-sin3alpha).
Both are symmetric under coordinate swap, whereas F_*-q_0 is antisymmetric.
Direct trigonometric integration gives

\[
(\langle\psi_i,\psi_j\rangle_\rho)_{i,j=1,3}
=\begin{pmatrix}3/8&-1/4\\-1/4&3/8\end{pmatrix}\ge\tfrac18 I.
\]

The symmetric coefficients of v are at least A and B. Orthogonal projection
onto swap-symmetric functions in L²(rho), followed by the reverse triangle
inequality and ||hw||_rho<=r_v, gives for r_0=F_*-q

\[
\|r_0\|_p^2\ge e_0:=\frac34(A/\sqrt8-r_v)^2>0.
\tag{E4}
\]

Here r_v=A/8<A/sqrt(8). Also r_0 belongs to E_1, so its endpoint projected
force has squared norm at least lambda_1 e_0>0. This excludes stationarity
without inspecting any nonlinear trained prediction. Label noise NG6 remains
admissible: |q_0|<=1-h/4, ||v+w||_infty<R<=1/8, and |xi|<=h/8 imply
|q+xi|<=1. Centering removes noise from the population equation.

This family is a nonvacuous domain for the following identities. A positive
nonlinear-versus-frozen sign on it remains unproved.

## 3. Exact prediction dynamics and a finite kernel-motion bound

Fix a task. All following unmarked inner products are in H=L²(p rho).
Let E denote the raw increment Hilbert space. Define

\[
T_\tau:H\to E,\quad T_\tau a=\int a(u)d_{\theta(\tau)}(u)p(u)d\rho(u),
\qquad \mathsf K_\tau=T_\tau^*T_\tau.
\tag{E5}
\]

The adjoint is (T_tau^*v)(u)=<d_theta(tau)(u),v>_raw. Continuous bounded
raw-valued input maps are Bochner integrable; Cauchy–Schwarz gives
||T_tau||<=L and ||K_tau||<=L². Each K_tau is self-adjoint and nonnegative.
At the endpoint ||K_0||<=L_0². This is the full projected endpoint kernel,
not readout-only and not the original-initialization NTK.

The scalar chain rule and Pi*=Pi²=Pi give, exactly,

\[
r_\tau=P_\nu(\tau)-q,\qquad r_\tau'=-2\mathsf K_\tau r_\tau,
\qquad (\|r_\tau\|^2)'=-4\|T_\tau r_\tau\|_{raw}^2.
\tag{E6}
\]

Thus ||r_tau||<=R_0:=||r_0||<=B_0:=sqrt(10)+1.

There is a true Lipschitz bound in episode time. With B_G=GM^(-1),
differentiate the projection onto the range of G and group its terms:

\[
\Pi'=-\Pi G'B_G^*-B_GG'^*\Pi.
\]

The gap gives ||B_G||<=sqrt(2/k), while NSC28 gives
||G'||<=sqrt(2)T_g m. Therefore

\[
\|\Pi'\|\le4T_gm/\sqrt k,\quad
\|d_\tau'(u)\|\le T_gm(1+4L/\sqrt k)\le J,
\]
\[
J=A_sT_g(1+4L/\sqrt k),\qquad \Gamma=2LJ,\qquad
\|\mathsf K_\tau-\mathsf K_\sigma\|\le\Gamma|\tau-\sigma|.
\tag{E7}
\]

Indeed integration at each input gives ||T_tau-T_sigma||<=J|tau-sigma|;
subtracting the two factors of T* T proves the last inequality. These
derivatives are only along the reached controlled curves covered by
NSC25–NSC28. No neural time-analyticity or Taylor radius is assumed.

## 4. The exact signed finite-time comparison

The frozen residual is

\[
z_\tau=F_{fr}(\tau)-q=S(\tau)r_0,\qquad
S(t)=\exp(-2t\mathsf K_0).
\tag{E8}
\]

This bounded linear operator exponential has an absolutely norm-convergent
series, dominated by exp(2t||K_0||). Differentiating it proves the equation.
Differentiating ||S(t)a||² and using K_0>=0 proves contraction. This
elementary linear exponential is not a neural Taylor convergence assumption.

Set

\[
W_T=\int_0^T S(T-s)(\mathsf K_s-\mathsf K_0)r_s\,ds.
\tag{E9}
\]

Subtract (E6) from the frozen equation and differentiate the continuous
variation-of-constants integral. Its initial difference is zero, hence

\[
r_T=z_T-2W_T,\qquad
\mathcal E_\nu(F_{fr}(T))-\mathcal E_\nu(P_\nu(T))
=4\langle z_T,W_T\rangle-4\|W_T\|^2.
\tag{E10}
\]

Self-adjointness supplies the equivalent cross interaction

\[
\langle z_T,W_T\rangle
=\int_0^T\langle S(T-s)z_T,
                    (\mathsf K_s-\mathsf K_0)r_s\rangle\,ds.
\tag{E11}
\]

Thus strict advantage holds exactly when <z_T,W_T> > ||W_T||².
A uniform a requires a signed lower bound in (E11) exceeding the quadratic
penalty. Rephrasing that missing condition is not, by itself, progress:
without an independent sign estimate it retains theorem-level strength.

There is useful unsigned control:

\[
\|W_T\|\le\Gamma R_0T^2/2,\quad
\|r_T-z_T\|\le\Gamma R_0T^2,\quad
|\mathcal E_\nu(F_{fr}(T))-\mathcal E_\nu(P_\nu(T))|
\le2\Gamma R_0^2T^2.
\tag{E12}
\]

The first inequality integrates Gamma s R_0. The last uses both residual
contractions and the difference-of-squares inequality. An independent
bound <z_T,W_T> >= beta R_0²T² would prove advantage at least
(4 beta-Gamma²T²)R_0²T². No beta>0 is established here.

The size of any advantage can also be compared to total learning. Put
D=4L^4+Gamma and lambda=lambda_1. Equation (E6) gives
||r_t-r_0||<=2L²R_0t. Subtract the two residual factors and the kernel to get

\[
|\langle r_t,\mathsf K_t r_t\rangle
       -\langle r_0,\mathsf K_0r_0\rangle|\le D R_0^2t.
\]

The residual terms cost L²(2R_0)(2L²R_0t), and kernel change costs
Gamma t R_0². Since r_0 in E_1, integrate (E6) to obtain, for
0<T<=min(T_c,lambda/D),

\[
\mathcal E_\nu(F_*)-\mathcal E_\nu(P_\nu(T))
\ge4\lambda R_0^2T-2DR_0^2T^2\ge2\lambda R_0^2T>0,
\]
\[
\frac{|\mathcal E_\nu(F_{fr}(T))-\mathcal E_\nu(P_\nu(T))|}
     {\mathcal E_\nu(F_*)-\mathcal E_\nu(P_\nu(T))}
\le\frac{\Gamma T}{\lambda}.
\tag{E13}
\]

Arbitrarily shrinking the episode therefore cannot itself establish an
advantage comparable to total learning. The constants remain ill-conditioned.

## 5. Hostile checks of generic dominance arguments

### Variational descent supplies no comparison order

At a current anchor-fitted state, the selected velocity minimizes
||v||_raw²/2+2 integral r(u)<g_theta(u),v> p d rho over the closed subspace
G_theta^*v=0. Completing the square gives
v=-2Pi_theta integral r g_theta p, exactly the constrained GF.
The frozen learner has the analogous minimization using its endpoint tangent
and its own residual. At later times neither tangent-space nesting nor equal
residuals holds. These separate minimization principles and dissipation
identities do not order their risks.

### Scalar saturation can make nonlinear GF strictly slower

This is a proof-rule counterexample, not a counterexample to E₀'s specified
deep architecture. Let f(theta)=tanh(theta), f(theta_0)=1/2, and target 3/4,
with Euclidean parameter GF of the unhalved square. Writing y=f(theta),

\[
y'=2(3/4-y)(1-y^2)^2.
\]

Smooth scalar uniqueness keeps 1/2<y(t)<3/4 for finite t>0: the vector
field is positive in the interval, and reaching its equilibrium in finite
time would contradict uniqueness. For u=3/4-y,

\[
u(t)=\tfrac14\exp[-2\int_0^t(1-y(s)^2)^2ds].
\]

The moving kernel is strictly below its initial value 9/16 at positive time.
Hence u(t)>(1/4)exp(-9t/8), the frozen residual, for every finite t>0.
The nonlinear learner strictly learns, yet is strictly worse than its full
frozen tangent. Nonlinearity and risk descent cannot determine advantage.

### Even Loewner enlargement need not order finite-time risks

This also falsifies a generic implication, not the specific neural theorem.
Let

\[
B=\begin{pmatrix}1&0\\0&2\end{pmatrix},\quad
C=\begin{pmatrix}1&1\\1&1\end{pmatrix}\ge0,\quad A=B+C.
\]

Start residual e_2; use kernel B until a positive t_1 and A thereafter.
The frozen learner uses B throughout. At t_1+1 both risks have common
factor exp(-8t_1). The frozen remaining factor is exp(-8). The smaller
eigenvalue of A is lambda_-=(5-sqrt(5))/2, and the squared e_2 overlap
with its eigenspace is c_-=(1-1/sqrt(5))/2>1/4. Thus

\[
\langle e_2,e^{-4A}e_2\rangle
\ge c_-e^{-4\lambda_-}>e^{-8}.
\]

The last ratio is c_- exp(2sqrt(5)-2)>(1/4)e²>1, since e²>1+2+2=5.
Although every changed kernel is at least B, its finite-time risk is larger:
the off-diagonal motion introduces residual in its slower eigendirection.

A smooth switch B+chi_delta(t)C, rising from zero to one over an interval
of length delta after t_1, preserves both Loewner enlargement and the same
initial kernel. Comparing its contractive evolution to the switched one by
Duhamel bounds the residual discrepancy by 2||C||delta. The strict preceding
margin survives for sufficiently small delta. Continuity cannot repair the
invalid dominance inference. Additional structure, such as suitable
commutation, would be needed and is not proved for the deep tanh flow.

## 6. Components and a finite scalar-clock exclusion criterion

Let Q_j be mutually orthogonal fixed projections in H summing to identity.
For task interpretation one can first use span{h cos alpha,h sin alpha},
then the part of the third-harmonic anchored space orthogonal to it, then
their orthogonal complement. Orthogonalization uses p rho before the episode.
The complement must remain: neither learner is asserted to preserve the finite
task space. For every component (E10) gives exactly

\[
\|Q_jz_T\|^2-\|Q_jr_T\|^2
=4\langle Q_jz_T,Q_jW_T\rangle-4\|Q_jW_T\|^2.
\tag{E14}
\]

Summing recovers the total risk gap. Component differentiation instead gives
-4<Q_jr,K_tau r>, including all off-component interactions; it need not be
negative. Normalize by a fixed positive task scale if desired. Normalizing
by initial component error requires its own positive denominator bound.
No favorable uniform component sign in (E14) has been proved.

A nonnegative frozen learning-rate schedule with cumulative clock s produces
z_s, regardless of its timing. Specify a common budget

\[
0<T\le S\le\lambda/(8L_0^4),\qquad T\le T_c.
\tag{E15}
\]

For interpretation only, give the scalar competitor every s in [0,S], including
task-specific oracle selection inside this declared budget. The base comparison
still uses matched T. Let v_T=K_0z_T, and Q_perp project orthogonally to its
one-dimensional span in the common prediction metric. This direction is
computed from endpoint kernel, target and frozen evolution, without nonlinear
trained output; its purpose is to remove scalar clock motion. Then

\[
\inf_{0\le s\le S}\|r_T-z_s\|
\ge\|Q_\perp(r_T-z_T)\|
 -\frac{8L_0^4R_0\Gamma^2T^4}{\lambda^2}.
\tag{E16}
\]

Proof: q_f(s)=<z_s,K_0z_s> obeys
q_f'=-4||K_0z_s||²>=-4L_0^4R_0², so (E15) and endpoint conditioning
give q_f(s)>=lambda R_0²/2. In particular v_T is nonzero and
-(||z_s||)'=2q_f(s)/||z_s||>=lambda R_0.
A distance minimizer s_* exists on [0,S]; since T is admitted, (E12) gives
||r_T-z_(s_*)||<=Gamma R_0T². The triangle inequality for norms yields
| ||z_(s_*)||-||z_T|| |<=2Gamma R_0T², hence
|s_*-T|<=2Gamma T²/lambda. Finally z_s''=4K_0²z_s has norm at most
4L_0^4R_0. Integrating it twice around T and using Q_perp z_T'=0 gives
||Q_perp(z_s-z_T)||<=2L_0^4R_0|s-T|². The projected triangle inequality
at s_* proves (E16).

This is a finite-horizon estimate with a verified remainder; no neural Taylor
radius appears. A transverse displacement larger than that remainder would
exclude every scalar clock in the budget. Such a displacement remains
unproved. Scalar separation alone is also insufficient: beneficial relative
learning needs a signed task-component statement such as (E14).

## 7. Sampling and finite-network scope

A population margin has not been obtained, so no unconditional sample threshold
for E₀ can be reported. Here is a bounded check of the frozen sampling input,
retained to identify whether sampling adds a new sign obstacle.

Use the same iid observations and bounded centered noise as the nonlinear
empirical learner. On the fixed full endpoint tangent space let

\[
v_m'=-2m^{-1}\sum_i
 [F_*(X_i)+\langle d_\dagger(X_i),v_m\rangle-Y_i]d_\dagger(X_i),
\quad v_m(0)=0,
\]
\[
F_{fr,m}(t,u)=F_*(u)+\langle d_\dagger(u),v_m(t)\rangle.
\tag{E17}
\]

This is a bounded linear ODE with a nonnegative empirical covariance, even
for singular or repeated samples. Its population counterpart represents (E8).
Evaluate the empirical force discrepancy on that deterministic population
path: I_m(t)=m^(-1)sum z_t(X_i)d(X_i)-E[z_t(X)d(X)], and
N_m=m^(-1)sum xi_i d(X_i). Independence and centering give
E||I_m(t)||²<=L_0²B_0²/m and E||N_m||²<=L_0²sigma²/m.
The difference equation has homogeneous generator minus twice the empirical
nonnegative covariance, so its propagator is a contraction. Integration,
Cauchy–Schwarz in time, Markov and a union bound prove, with failure at most
delta_I+delta_xi,

\[
\sup_{t\le T}\|F_{fr,m}(t)-F_{fr}(t)\|_\infty
\le\frac{2TL_0^2}{\sqrt m}
 \left(\frac{B_0}{\sqrt{\delta_I}}+
                       \frac{\sigma}{\sqrt{\delta_\xi}}\right).
\tag{E18}
\]

Omit the noise term and allowance when sigma=0. The proof never uses
independence of trained features and their own labels.

The established nonlinear sampling modulus NGL8–NGL13 applies on the same
observations. A union bound combines it with (E18), without requiring
independent events. Therefore any independently proved uniform population
margin would transfer using prediction error tolerances smaller than that
margin divided by bounded residual scales. The supervisor has a separate
transfer task; this route does not duplicate a complete conditional threshold.

Known anchors retain their exact weights in the nonlinear empirical law.
All projected endpoint directions vanish at the anchors, so (E17) preserves
them exactly. For each fixed sample the nonlinear term is captured by actual
finite original-mixture GF, width first and contamination second; the sampling
limit is last. A finite neural realization of the frozen kernel still needs
its own full-gradient/kernel approximation. Hidden/output convergence alone
is not silently substituted for that argument.

## 8. Status and exact reopening condition

| Claim | Status | Evidence or limitation |
|---|---|---|
| Full selected prediction dynamics | Exact using established continuation | (E5)–(E6) |
| Robust active four-coefficient family | Proved | (E1)–(E4), explicit Gram and symmetry |
| Finite-time kernel-motion bound | Proved from reached derivative estimates | (E7) |
| Signed risk comparison | Exact | (E9)–(E11) |
| Size and learning-fraction bounds | Proved | (E12)–(E13) |
| Generic descent implies superiority | False proof rule | Scalar tanh example |
| Loewner kernel enlargement orders finite-time risks | False proof rule | Explicit noncommuting 2D example |
| Scalar-clock exclusion | Conditional quantitative criterion | (E16); transverse size unproved |
| Beneficial component reweighting | Open | No sign established in (E14) |
| Uniform positive E₀ margin | Open | Missing signed interaction (E11) |
| Frozen shared-sample control | Proved | (E17)–(E18) |
| Finite frozen neural realization | Not claimed | Separate gradient/kernel limit needed |

The single decisive scientific obligation is a uniform positive lower bound
for the *actual-neural* interaction (E11), with sufficient margin over (E10)'s
quadratic penalty, accompanied by a beneficial signed component inequality.
Neither endpoint conditioning nor any unsigned source/continuity estimate
controls this. Assuming the desired sign on an unknown reached path would
merely rename the theorem.

The remaining ordinary alternative is scalar clock change; (E16) identifies
the finite prediction evidence that could rule it out under a declared budget.
The strongest generic obstruction is residual transfer between directions:
decreasing each learner's own loss cannot compare their risks. No numerical
artifact is implicated because no experiment ran. A failed sign proof here
does not establish impossibility of E₀. Attribution is only to the full
nonlinear constrained evolution, not the middle layer alone, initialization
NTK, another architecture, or resource efficiency.

Boundary audit: e_0 excludes zero residual; k/2 protects the projection inverse;
lambda_1 is used only on the finite initial target space; singular empirical
covariances are harmless for contraction; non-even densities use their actual
common metric; all component complements remain; the scalar denominator is
positive by (E15); no all-time nonlinear result, limit interchange, or finite
endpoint restart is used.

Registry recommendation: **blocked at the structural sign comparison, with
reusable exact lemmas retained**. Reopen upon a new signed geometric estimate
or a complete finite prediction-space construction with controlled remainders.

## 9. Actual reads, checks and provenance

Read completely:

* Neutral contract (92 lines), docs/NOTATION.md (98 lines), both required skills,
  and research-contract, adversarial-audit and proof-search-orchestration
  references. Initially truncated combined reference outputs were repaired
  with complete separate reads.
* RESEARCH_WORKFLOW.md Part 1 including shared-write instructions. The initial
  full-file output was partly truncated; lines 1–125 were reread. The
  shared-write paragraph was visible completely in the original output.
  Part 2 was incidentally visible; no promotion was performed.
* docs/global_nonlinear.md lines 12994–17016, complete C.4.9–C.4.10.
  The truncated C.4.10.3 portion was repaired by reads of 16352–16558 and
  16558–16645; preceding definitions 16297–16351 were visible completely.
* Contained dependencies in that file: 1840–1902 (A.1–A.4), 5475–5782
  (C.4.5.1 §§1–3), 5999–6103 (complete rational certificate supporting
  m>=1/10), 6104–6521 (C.4.5.2 §§1–4).
* By the supervisor's explicit input-scope expansion,
  docs/special_data_limits.md 3785–4326, complete III.F, including all proof
  bodies for Gaussian-program convergence, singular queries, common generated
  actions, actual adjoints, raw Hilbert increments and scalar/strong chain rules.

The unread complement of the two book files was not audited. The dependency
path used here is the contained source-tube proof with the listed reference,
Gaussian-program and chain-rule inputs. Additional historical references in
C.4.9 to C.4.6/C.4.7 were not independently re-audited: needed identities and
source facts are supplied on the contained path read above. No external source,
other study, other route, history or another agent's scientific findings was
used. Git status exposed only coordination metadata/filenames; contents of
other studies were not read.

Before writing, HEAD was 1bed52ef4a190589659fccce96acf50bb7a2e8c5 and the index
was empty. Concurrent changes were present and left untouched. No training,
symbolic experiment, numerical quadrature or source-certificate execution was
performed. Checks were hand reconstruction of all displayed derivations,
finite Gram calculations, the 2D example, Duhamel signs, the projection
derivative, and the scalar-clock remainder. This is a checked derivation
candidate, not an independent promotion review.

Input SHA-256 values are appended below. They identify full files; read scope
is the selected coverage above, not a claim to have read every hashed line.


| Input | SHA-256 |
|---|---|
| `studies/nonlinear_adaptation_advantage/RESEARCH_CONTRACT.md` | `0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `/etc/codex/skills/investigate-conjectures/references/proof-search-orchestration.md` | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
