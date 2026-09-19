# Artificial commuting tangent: parity and source identification

This is a fresh scoped mathematical check. Scientific inputs were the assignment,
`docs/NOTATION.md`, `docs/global_nonlinear.md` C.4.7.3, and
`docs/special_data_limits.md` III.F. No other study material, experiments, Git
history, or review findings were used. The solve-math-rigorously and
investigate-conjectures skills and their applicable contract/audit instructions
were read. This report concerns a research lemma, not an acceptance verdict.

**Conclusion.** The proposed identification can be made valid. One must construct
the artificial tangent as its own enlarged Gaussian value program, retain its
actual initialized action calls, and use the resulting **new** tangent response
arrays. Parity removes mixed base/tangent corrections; it does not remove the
tangent/tangent corrections. With a fixed complete list of named tangent calls,
the response arrays are independent of the selected probe and of the tangent
source covariance. A fresh upper probe therefore gives exactly the artificial
named beta coefficient. Width-uniform L2 stability bounds every past coefficient
with its time-step/atom mass, and hence bounds the complete row independently of
the actual base backward cap B.

The continuous lower comparison uses only the bounded second derivative. A raw
Euler comparison has an additional discretization defect; its uniformity over
activation approximations must not be inferred from M,D,L alone. A mesh limit at
each fixed smooth approximation separates this issue from the cap-independent
artificial anchor.

## 1. Fixed base and the artificial program

Use two inputs with G_ab=u_a.u_b, G_aa=1, half weights, and residual r=f-y.
Write h_ka=phi(w_k.u_a), Z_ka=A_k h_ka, d_ka=c_k phi'(Z_ka), and Q_ka=A_k* d_ka.
The activation bounds are

\[
 |\phi|\le M,\qquad |\phi'|\le D,\qquad |\phi''|\le L.
\]

The actual base has bounds |r_ka|<=R, ||c_k||infty<=C, and ||A_k||op<=A_* on
the horizon [0,T]. These constants are assumed available independently of B,
as in the question. For the mesh write lambda_ka=-h_k r_ka; with general atom
weights this becomes lambda_ka=-2 h_k p_a r_ka. Thus

\[
 K_k=\sum_{q<k}\lambda_q d_q\otimes h_q,
 \qquad A_k=A_0+K_k.
 \tag{1}
\]

The base is stored and is independent of the fresh centered Gaussian probe e.
Write eta_i, v_i, z_i, q_i for the artificial delta h_i, delta d_i, delta Z_i,
delta Q_i, and write a_k and B_k for delta c_k and delta K_k. The letter B_k
here is an operator increment, not the scalar backward row cap B.
Define

\[
 J_{ka,b}=G_{ab}\phi'(w_k\cdot u_a)\phi'(w_k\cdot u_b),
 \qquad \eta_{ka}=\sum_bJ_{ka,b}\chi_{k,b}.
 \tag{2}
\]

For passive u, use J_ku,b=(u.u_b) phi'(w_k.u) phi'(w_k.u_b).
The prescribed tangent dynamics, with the coefficients of the base frozen, are

\[
 \begin{split}
 z_i&=A_k\eta_i+B_k h_i+f_i,\\
 v_i&=\phi'(Z_i)a_k+c_k\phi''(Z_i)z_i,\\
 q_i&=A_k^*v_i+B_k^*d_i+g_i,\\
 \chi_{k+1,a}&=\chi_{k,a}+\lambda_{ka}q_{ka},\\
 a_{k+1}&=a_k+\sum_a\lambda_{ka}\phi'(Z_{ka})z_{ka},\\
 B_{k+1}&=B_k+\sum_a\lambda_{ka}
                   (v_{ka}\otimes h_{ka}+d_{ka}\otimes\eta_{ka}).
 \end{split}
 \tag{3}
\]

All tangent states start at zero. A single upper probe means f_p=e and every
other f_i and g_i is zero; a lower probe means g_p=e instead. Each f_i is added
to the complete forward answer, before every descendant at that slot is
evaluated. All descendants of (3) are recomputed. The base remains a stored
input to this new program. Equation (3) need not be the derivative of a nonlinear
feature-value system to be a legitimate Gaussian program in its own right.

At finite width, (3) is a linear map of the fresh probe vector with coefficients
depending on the actual base arrays. Ordinary finite derivatives of residuals
and empirical contractions can also be included. They are linear base/tangent
contractions; their population limits vanish by the argument below. Thus their
omission in (3) is justified at the population level, not by claiming that they
vanish for each finite sample of the probe.

## 2. What parity gives

At finite width, replacing the complete fresh probe vector e_n by -e_n leaves
the base arrays unchanged and negates every tangent array. The finite-program
limit is deterministic. Every limiting contraction of a base field with a
tangent field therefore vanishes. In particular,

\[
 E_1[h_i\eta_j]=0,\qquad E_2[d_i v_j]=0.
 \tag{4}
\]

Equivalently, conditional on the base arrays, a mixed empirical contraction is
a centered Gaussian linear functional of e_n. The operator bound in Section 5
bounds its variance by O(1/n) for fixed base fields with bounded normalized L2
norm. This provides a direct check on the parity-plus-deterministic-limit step.

In the scalar source representation, the symmetry is **not** e -> -e with all
other source coordinates held fixed. It flips e and every tangent Gaussian
source coordinate simultaneously. Base source coordinates remain fixed.
Tangent inputs have zero cross Gram with base inputs by (4). Consequently the
centered Gaussian source groups have block diagonal base/tangent covariance;
these two blocks are independent, including at singular covariance.

Every tangent scalar expression is homogeneous linear in its local tangent
sources and its local probe root, with coefficients depending on base sources.
Thus, after freezing all deterministic coefficients and covariance laws,

\[
 E[\partial_{\text{base source}}\text{(tangent field)}]=0.
 \tag{5}
\]

Indeed the differentiated expression remains odd in the independent centered
tangent block and probe root. Formula (5) uses the formal named-source
convention of III.F.4, not a derivative of a covariance matrix or a conditional
Gaussian representation. The tangent variance may depend on the base law;
that variance is a deterministic parameter, and (5) does not differentiate it.

## 3. Exact enlarged source equations

Keep a tangent forward call A_0 eta_i and a tangent reverse call A_0* v_i at
every named training slot, including calls that happen to have zero input.
All current forward calls precede all current reverse calls. Let xi_i^T and
zeta_i^T be their centered Gaussian sources. Their covariances are

\[
 E_2[\xi_i^T\xi_j^T]=E_1[\eta_i\eta_j],\qquad
 E_1[\zeta_i^T\zeta_j^T]=E_2[v_i v_j].
 \tag{6}
\]

The two orientations are independent groups, and their tangent blocks are
independent of the corresponding base blocks and of all roots. Define

\[
 \alpha^T_{i,q}=E_1[\partial_{\zeta_q^T}\eta_i],\qquad
 \beta^T_{i,q}=E_2[\partial_{\xi_q^T}v_i],
 \tag{7}
\]

with unavailable-source coefficients zero. The source rule III.F.9--III.F.10,
applied to the union of the base and tangent programs, gives

\[
 A_0\eta_i=\xi_i^T+\sum_{q<i}\alpha^T_{i,q}v_q,
 \qquad
 A_0^*v_i=\zeta_i^T+\sum_{q\le i}\beta^T_{i,q}\eta_q.
 \tag{8}
\]

Here q<i in a forward memory means a strictly earlier time. Terms onto base
reverse or forward inputs vanish by (5). The surviving coefficients in (8)
are new tangent coefficients, not the actual base alpha and beta arrays.

Expanding (1) and (3), and using (4), gives all learned-action terms explicitly:

\[
 \begin{split}
 K_k\eta_i&=0,&
 B_k h_i&=\sum_{q<k}\lambda_q E_1[h_qh_i]v_q,\\
 K_k^*v_i&=0,&
 B_k^*d_i&=\sum_{q<k}\lambda_q E_2[d_qd_i]\eta_q.
 \end{split}
 \tag{9}
\]

Consequently the exact frozen Gaussian tangent system is

\[
 \begin{split}
 F^T_{i,q}&=\alpha^T_{i,q}+\lambda_q E_1[h_i h_q],\quad q<i,\\
 D^T_{i,q}&=\beta^T_{i,q}
          +\mathbf1_{t(q)<t(i)}\lambda_q E_2[d_i d_q],\\
 z_i&=\xi_i^T+\sum_{q<i}F^T_{i,q}v_q+f_i,\\
 q_i&=\zeta_i^T+\sum_{q\le i}D^T_{i,q}\eta_q+g_i,
 \end{split}
 \tag{10}
\]

together with (2) and the chi/a recursions in (3). This derives, rather than
assumes, every surviving source response and learned Gram contribution.

The upper named pulses are precisely

\[
 \begin{split}
 U^T_{i;p}&=\mathbf1_{i=p}+\sum_{q<i}F^T_{i,q}V^T_{q;p},\\
 C^T_{k;p}&=\sum_{q<k}\lambda_q\phi'(Z_q)U^T_{q;p},\\
 V^T_{i;p}&=\phi'(Z_i)C^T_{k;p}
                    +c_k\phi''(Z_i)U^T_{i;p},\\
 \beta^T_{i,p}&=E_2 V^T_{i;p}.
 \end{split}
 \tag{11}
\]

For a lower pulse p, let X^T_ka;p=partial_zeta_p^T chi_ka. Then

\[
 \begin{split}
 X^T_{k+1,a;p}=X^T_{k,a;p}+\lambda_{ka}
 \left[\mathbf1_{(k,a)=p}+\sum_{q\le k}D^T_{ka,q}
                 \sum_bJ_{q,b}X^T_{t(q),b;p}\right],\\
 \alpha^T_{i,p}=E_1\sum_b J_{i,b}X^T_{t(i),b;p}.
 \end{split}
 \tag{12}
\]

These are the commuting lower source equations and the unchanged upper
source equations on the actual base.

## 4. The same beta row is extracted by all probe slots

A possible ambiguity is that each probe changes (6). It does not change the
coefficient arrays (7), provided the full named call list is retained.

To prove this, induct through the finite causal program. Every tangent node has
the form of a finite sum of tangent source/root coordinates multiplied by
functions of the base source coordinates. Differentiating in one tangent source
removes the tangent coordinate and leaves a function only of the base sources
and already computed deterministic response coefficients. Its expectation is
independent of the tangent covariance and the probe slot. Equations (11)--(12)
therefore construct one common alpha^T/beta^T array for every single-probe
realization of the same formal graph. This is a causal induction, not a
self-consistent choice among multiple coefficient arrays.

For an upper probe at p, e enters only through xi_p^T+e. In the scalar program,
all source groups are independent of e. Freezing deterministic objects gives

\[
 \partial_e v_i=\partial_{\xi_p^T}v_i,
 \qquad
 E_2[e v_i]=E_2[\partial_e v_i]=\beta^T_{i,p}.
 \tag{13}
\]

The middle equality is one-dimensional Gaussian integration by parts;
linearity and the L2 bound below guarantee integrability. It remains valid when
xi_p^T has variance zero. The probe identifies the specified formal slot rather
than trying to recover a derivative transverse to singular support from the
unforced value law. For a lower probe the same argument gives
E_1[e eta_i]=alpha^T_i,p.

Thus E[e v_i] bounds the right artificial beta. It does not directly bound the
actual base beta unless the lower tangent rule is the actual linearization.
The later coefficient comparison remains necessary.

## 5. Width-independent L2 stability and complete row bounds

Put x=sum_a ||chi_a||2, z=||a||2, kappa=||B||HS, and S=x+z+kappa. At finite
width these norms mean Euclidean RMS for vectors and ordinary Frobenius norm
for the learned matrix increment. For two inputs, direct subtraction of (3)
gives

\[
 \begin{split}
 H:=\sum_a\|\eta_a\|_2&\le2D^2x,\\
 Z_*:=\sum_a\|z_a\|_2&\le A_*H+2M\kappa+\sum_a\|f_a\|_2,\\
 V:=\sum_a\|v_a\|_2&\le2Dz+CLZ_*,\\
 Q_*:=\sum_a\|q_a\|_2&\le A_*V+2CD\kappa+\sum_a\|g_a\|_2.
 \end{split}
 \tag{14}
\]

Away from a forcing node the three Euler increments are bounded by

\[
 h_k RQ_*,\qquad h_k RDZ_*,\qquad h_k R(MV+CDH),
 \tag{15}
\]

respectively. Therefore S_{k+1}<=(1+h_k C_*)S_k, where C_* depends only on
M,D,L,R,C,A_*. In particular the amplification is at most exp(C_* T),
independently of width, mesh length, and B. A passive output satisfies
||v_i||2 <=C_out S_k, with C_out depending on the same constants.

For a single upper pulse at p=(s,b), all tangent states are zero before that
slot. Its current v_p equals c_s phi''(Z_p)e. Its immediate increments obey

\[
 S_{s+1}\le |\lambda_p|
     (A_*CL+D+CLM)\|e\|_2.
 \tag{16}
\]

The three terms come from chi, a, and B, respectively. Thus for i at a later
time,

\[
 |\beta^T_{i,p}|
 \le C_{\rm out}e^{C_*T}(A_*CL+D+CLM)|\lambda_p|.
 \tag{17}
\]

The unique distinguished current slot has

\[
 \beta^T_{ku,ku}=E_2[c_k\phi''(Z_{ku})],
 \qquad |\beta^T_{ku,ku}|\le CL;
 \tag{18}
\]

other current named slots have zero derivative for that output. Since
|lambda_sb|<=2R h_s p_b, (17)--(18) imply the complete passive row cap

\[
 |\beta^T_{ku,ku}|+\sum_{s<k,b}|\beta^T_{ku,sb}|
 \le CL+2RT C_{\rm out}e^{C_*T}(A_*CL+D+CLM).
 \tag{19}
\]

This cap is independent of B. It uses the common-row result of Section 4;
separate bounds for coefficients of unrelated probe-dependent rows would not
have justified (19). A reverse pulse similarly has S_{s+1}<=|lambda_p| ||e||2,
which yields an alpha^T bound with the same source mass.

If the ordinary finite first variation of residual feedback is included, then

\[
 \delta r_a=\langle a,H_a^{(2)}\rangle
                 +\langle c\phi'(Z_a),z_a\rangle,
 \qquad \sum_a|\delta r_a|\le2Mz+CDZ_*.
 \tag{20}
\]

Its extra velocity terms are delta r_a times the base Q_a, d_a tensor h_a,
and H_a^(2). Their norms use ||Q_a||2<=A_*CD and are bounded by another
constant times S. Thus they preserve cap-independent stability. Their
population coefficients are zero by (4) and independence of e in the direct
forcing slot. The same reasoning handles first variations of learned Grams.

## 6. Regularity: where third derivatives are unnecessary

For each fixed smooth approximation and fixed graph, one can first smooth and
truncate coordinate products to apply III.F literally. Choose odd clips for
tangent arguments; parity is exact at every truncation. A base-source derivative
of a coefficient c phi''(Z) can involve phi''', but its expected mixed correction
is exactly zero before any estimates. No uniform bound on that derivative is
needed for (10)--(19).

The surviving derivatives are in tangent slots. They never differentiate a
base multiplier, and their finite causal recursions use only the bounds D and
CL. Tangent clips with derivative bounded by one give finite deterministic
source-derivative bounds along a fixed graph. Those bounds and (14)--(15) allow
the clips to be removed in the value laws and in the surviving expected
derivatives. If the approximation is only C2, approximate its bounded continuous
second-derivative multiplier by smooth bounded multipliers. Strong multiplier
continuity (III.F.9), the finite causal recursions, and domination by those
finite derivative bounds pass to the original multiplier. Mixed corrections
remain identically zero. This supplies the needed extension without assuming a
uniform third derivative of the activation.

No assertion here extends the bounded action to arbitrary independent L2
random functions. Include the finite base/tangent/probe programs in the common
generated carrier of III.F.7. Its actual action/adjoint norm bound is the bound
used in (14).

## 7. Lower commutator and its discretization boundary

For continuous lower dynamics put X_a(w)=phi'(w.u_a)u_a and b_a=-r_a Q_a.
Then w'=sum_a b_a X_a(w). A named lower pulse v, with a variation delta b of
the controls, satisfies

\[
 v'=\sum_a b_a DX_a(w)v+\sum_aX_a(w)\delta b_a.
 \tag{21}
\]

Let chi'_a=delta b_a and v_bar=sum_a X_a(w)chi_a. Differentiating this explicit
expression and subtracting from (21), eta=v-v_bar obeys

\[
 \eta'=\sum_b b_bDX_b(w)\eta
 +\sum_{a,b}b_b\{DX_b(w)X_a(w)-DX_a(w)X_b(w)\}\chi_a.
 \tag{22}
\]

The bracket is exactly

\[
 DX_bX_a-DX_aX_b
 =G_{ab}\{\phi'(z_a)\phi''(z_b)u_b
                   -\phi'(z_b)\phi''(z_a)u_a\}.
 \tag{23}
\]

Its diagonal is zero and its off-diagonal norm is at most 2DL|G_12|.
Multiplying v_bar by the outside gate produces exactly (2). When comparing
actual and artificial pulses, the additional control difference is the
causal D-row difference, hence beta-beta^T plus the identical learned Grams.
The actual source multipliers Q and actual named pulses have the fixed Lp
bounds furnished by the temporary B cap in C.4.7.3. Thus the commutator forcing
can have a bound C_B |G_12| using M,D,L and the named-pulse estimates. No
comparison of phi'' at different upper trajectories occurs: the multiplier
c phi''(Z) in (11) is the actual base multiplier in both systems.

This establishes the structural cancellation needed for the comparison. It
does not label C_B as independent of B. A bootstrap may choose B from the
independent artificial cap (19), and then choose |G_12| sufficiently small
relative to that fixed C_B.

For raw Euler, (22) is not an exact discrete identity. The product
X_a(w_{k+1})chi_{k+1,a} produces both a chain-rule defect and a discrete product
defect. Bounded phi'' alone does not give a common vanishing mesh modulus across
all smooth approximations. The following scalar prescribed-control example
isolates the issue; it is not a counterexample to actual neural training.

On [0,1], take h=1/N and

\[
 \phi_h'(z)=1+\frac{h\ell}{2\pi}\sin(2\pi z/h).
 \tag{24}
\]

Multiply the primitive z-(h^2 ell/(4 pi^2))cos(2 pi z/h) by one fixed smooth
cutoff equal to one on [-1,2]. The resulting activations are bounded and smooth,
have common finite M,D,L bounds, and converge in C1 to the bounded cutoff of z.
The Euler base z_{k+1}=z_k+h phi_h'(z_k), z_0=0, has z_k=kh. At these nodes
phi_h'(z_k)=1 and phi_h''(z_k)=ell. A homogeneous Euler pulse therefore has
v_N=(1+h ell)^N v_0, whereas the commuting expression with constant chi is
v_bar_N=v_0. Their difference approaches (exp(ell)-1)v_0. Multiplying v_0 by
h realizes the same nonvanishing discrepancy after source-mass normalization.

The valid order is to fix a smooth approximation first, let its mesh tend to
zero, and keep only the constants in the continuous commutator estimate
uniform in the approximation. A schematic comparison

\[
 E_{\varepsilon,h}\le C_B|G_{12}|+\nu_{\varepsilon}(h),
 \qquad \nu_{\varepsilon}(h)\longrightarrow0
 \quad\text{for fixed }\varepsilon,
 \tag{25}
\]

is compatible with this check. Any third-derivative or modulus dependence may
enter nu_epsilon and the required mesh threshold, but must not enter the
cap-independent artificial anchor or the coefficient of |G_12|.

## 8. Exact logical outcome

Established by the displayed derivation: parity, block diagonal source groups,
the complete artificial equations (10)--(12), probe-independent response arrays,
fresh-probe extraction (13), and the cap-independent complete row bound (19),
under the stated cap-independent base bounds and fixed-program realization.

The artificial beta is not automatically the actual beta. The coefficient
comparison must use the small commutator (23), the actual named-source moment
estimates under a temporary cap, causal propagation of beta-beta^T, and a
properly ordered mesh limit. These remaining comparison steps do not require a
uniform comparison of upper second derivatives, because their base is common.

---

## Author-side follow-up: raw Euler implementation and C1,1 passage

This follow-up was separately authorized after the isolated lemma check above.
It read `COMMUTATOR_RESPONSE.md` completely and reread the current shared
`AGENTS.md`. It is an author-side error check, not a fresh independent acceptance
review. No other author proof, review, study, experiment, or Git material was
read. The original isolated analysis above is preserved.

**Finding.** I found no substantive error in the preferred raw-Euler argument
in Section 9, equations (32)--(38). Its discrete correction addresses the mesh
limitation identified in Section 7 above. The first-failed-row argument is
causal, and the common radius/tail constants do not require a uniform third
derivative. Below are the checks needed to support that finding.

### A. Exact discrete transport identity

Use the notation of the inspected proof: V_a=phi'(w.u_a)u_a,
b_ka=lambda_ka Q_ka, s_k=sum_a|b_ka|,
B_k=sum_a b_ka DV_a(w_k), J_k=I+h_k B_k, and
P_kj=J_(k-1)...J_j. (Here B_k is a row Jacobian, distinct from the tangent
operator denoted B_k earlier in this report.) For S=||phi'''||infty,
the Euler displacement has norm at most h_k D s_k, and

\[
 \begin{split}
 J_kV_a(w_k)-V_a(w_{k+1})
 &=h_k\sum_b b_{kb}(DV_bV_a-DV_aV_b)(w_k)
                  -\mathcal R_{k,a},\\
 |\mathcal R_{k,a}|&\le\tfrac12 S D^2 h_k^2s_k^2.
 \end{split}
 \tag{F1}
\]

This proves their (33). No derivative of Q or lambda enters this Taylor
remainder: both are frozen controls in the named row derivative.

The sum of P_(k,l+1)e_l,a telescopes to P_kj V_a(w_j)-V_a(w_k).
Since P_kj=P_(k,j+1)(I+h_j B_j), subtracting
h_j P_(k,j+1)B_j V_a(w_j) gives their exact (34). This last term is necessary;
the Euler forcing h_j lambda_ja V_a(w_j)nu_ja is inserted after multiplication
by J_j. Its norm is at most h_j L D s_j exp(L Lambda), proving (35).

### B. No maximum of Q and no hidden S dependence

Under the temporary actual beta cap, the Gaussian-plus-bounded decomposition
of Q bounds every fixed moment of s_j using only H,D,L,T and that cap. Jensen
bounds exp(eta Lambda) with the same dependence. Consequently

\[
 \Big\|\sum_jh_j^2s_j^2\Big\|_{L^p}
 \le h_{\max}\sum_jh_j\|s_j\|_{L^{2p}}^2
 \le C_{B,p}h_{\max}.
 \tag{F2}
\]

The total pulse mass divided by its source mass m_p is bounded by a constant
plus a constant times sup_j|v_j;p|/m_p. The latter has the exponential-in-Lambda
bound from their (11), also independent of S. Holder applied to these factors
therefore bounds the bracket and Taylor terms by
C_(B,p)[gamma+S h_max].

For the insertion-order term, its direct impulse contributes at most a constant
times h_s s_s exp(L Lambda) after division by m_p. Its memory part is bounded
by a constant times

\[
 h_{\max}\Lambda e^{L\Lambda}
                      \sup_j|v_{j;p}|/m_p.
 \tag{F3}
\]

Both have Lp norm at most C_(B,p)h_max. This verifies their (37), including the
supremum over the output node, because the right-hand bounds already sum all
forcing contributions on the capped prefix. All constants in this estimate
apart from the displayed S h_max can be fixed without S.

The other possible appearances of S are fixed-program justifications for
expected base-slot derivatives of c phi''(Z) times a tangent field. Those
expected corrections are identically zero by parity. Surviving tangent-slot
derivatives see c phi''(Z) only as a bounded multiplier. Neither the artificial
anchor nor the true/artificial upper comparison differentiates that multiplier.
Thus those fixed-program regularity constants do not enter the radius or tail
constants.

### C. First-failed-row causality

At a candidate failed row at node k, apply all capped estimates on the prefix
of updates j<k. Every Q_j, D_j, and control in that prefix uses a previously
bounded row. A lower named pulse v_k and its co-moving remainder R_k use only
those updates. The comparison of the accumulated controls X_k and chi_k uses
E_j only for j<k. It constructs alpha_k and F_k next. Finally the upper pulse
system at k uses F_k and upper memory at strictly earlier times. Its current
coefficient is the common E[c_k phi''(Z_ku)] and cancels exactly in the
discrepancy.

The crude pointwise upper derivative-row estimate also uses no current beta
cap: the density bound for F_k has already been obtained from preceding lower
updates. Therefore the C_B in their (38) can be fixed from B=B_cl+1 before
attempting the current row. There is no circular use of E_k or of a cap on the
row being constructed.

Choose gamma_* from this S-independent C_B, then fix a mollification and choose
h_* proportional to 1/(1+S). The two contributions in (38) can each be made at
most 1/4 after Gronwall. The current actual row is at most B_cl+1/2, closing the
induction. Passive outputs do not change this causal order: they append one
forward/reverse observation and never become lower driving controls. Their
outside gate and input-vector factors have the same uniform bounds.

### D. Independent check of the strong C1,1 value-law passage

The named source arrays need not converge as smoothing is removed. The value
comparison needed for the claimed strong flow uses only phi and phi'. Here is
a derivation of the relevant bridge using the assigned source conventions.

On the common raw ball, with both readouts bounded pointwise, forward fields,
upper d, Q, residuals, and rank-one updates are Lipschitz in raw distance,
except for the lower product phi'(w.u)Q. For that product put the difference
of Q on the bounded gate, and multiply the difference of the gate by the
reference Q. Splitting that reference Q at R gives

\[
 \|F(\theta)-F(\bar\theta)\|_{\rm raw}
 \le C(1+R)\|\theta-\bar\theta\|_{\rm raw}
                          +C\sum_a\tau_R(\bar Q_a).
 \tag{F4}
\]

For example, the exceptional term is at most
L R ||w-w_bar||2+2D tau_R(Q_bar). The upper difference uses
||d-d_bar||2 <=D||c-c_bar||2+CL||Z-Z_bar||2, so no upper localization and
no second cutoff factor are required. Constants depend only on the common
primal bounds and H,D,L.

For two raw-Euler interpolants, their raw speeds are uniformly bounded, and
each interpolant is O(h_max) from its preceding node. Apply (F4) to the two
preceding nodes and use their already proved uniform Gaussian Q tails. Gronwall
gives, with delta the sum of the two maximum mesh sizes,

\[
 \sup_{t\le T}\|\theta_h(t)-\theta_{\tilde h}(t)\|_{\rm raw}
 \le C_Te^{C_TR}\{(1+R)\delta+e^{-aR^2}\}.
 \tag{F5}
\]

Taking R to be a sufficiently large constant times sqrt(log(1/delta)) makes
the right side tend to zero. For each fixed mollification arbitrarily fine
meshes satisfy its h_*(S) threshold. Completeness gives a continuous raw limit;
strong multiplier continuity and the actual bounded action/adjoint pass its
integral equations. This proves a strong C1 path. L2 convergence of Q and
lower semicontinuity of x^2 1_(|x|>R) pass its Gaussian tail bound at every
time. The constants are uniform in the mollification and in the admitted
input geometry. No supremum of the random Q path is required.

For two mollifications replace delta in this argument by

\[
 \delta_{\rm act}
 =\|\phi_\varepsilon-\phi_\delta\|_\infty
  +\|\phi'_\varepsilon-\phi'_\delta\|_\infty.
 \tag{F6}
\]

Indeed all additional evaluation differences are bounded by C delta_act in
raw norm. In the lower product the gate evaluation error is at most
||phi'_epsilon-phi'_delta||infty ||Q_bar||2. The remaining localization is
exactly (F4). Bounded C1,1 activations have uniformly convergent mollifications
and first derivatives, so delta_act tends to zero. Equation (F5) then proves
Cauchy convergence of the smooth strong paths in C([0,T];raw).

Strong multiplier continuity passes phi'(w.u)Q in the limiting equation;
the other factors and rank operators pass by their L2/HS bounds. The limiting
velocity is continuous. The same lower-semicontinuity argument transfers
uniform active and passive Gaussian tails. Applying (F4) with this limiting
solution as the tail-bearing reference proves uniqueness against a bounded
strong competitor. A competitor with the same zero initial readout also has
the requisite pointwise readout bound by integrating its bounded activation
readout equation; no tail premise on that competitor is needed.

This independently supports the strong existence, reached uniqueness, and
Gaussian-tail part of the C1,1 conclusion. It does not require convergence of
phi'' or of its chosen pointwise representatives. The separate fitting horizon,
early-motion/nonaffinity, and finite-GF/raw-GD transfer statements cite other
study files that were not assigned for this follow-up; their internal proofs
were not re-audited here.

### E. Remaining presentation safeguard

The formal tangent graph should explicitly retain all named forward/reverse
calls, even zero-valued calls before a particular probe insertion. Section 4.2
already uses formal variance-zero slots and a probe-independent causal
recursion, so this is a clarification of its construction rather than a
missing algebraic term. Removing zero calls in different single-probe runs
would invalidate the common-row extraction argument.
