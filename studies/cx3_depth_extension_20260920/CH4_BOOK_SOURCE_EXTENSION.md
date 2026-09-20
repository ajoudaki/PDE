# Three-layer tanh: a direct attempt to extend the book's source anchor

Scoped author derivation, 2026-09-20. This is a partial proof attempt, not a
completed C-H4 extension or an independent review. No numerical experiment,
code execution for scientific evidence, or Git mutation was performed.

## 1. Inputs, independence and outcome

I previously performed a read-only theorem-scope search of maintained
`docs/`, principally `special_data_limits.md`. That work established model
mismatches; it was not a proof audit. For this attempt I read the complete
`CONTRACT.md`, `CH3_LOCAL_PROOF.md`, and maintained
`global_nonlinear.md` B.1 (1903–2453), C.4.5.1 (5475–6103), and
C.4.7.1–4 (8989–10424), including the full chronological source-cap proof.
No other study or parallel route report was read. Required mathematical and
research skills were applied. The prior book search is disclosed rather
than described as a fresh context.

The derivation below preserves three tanh layers, both independently
initialized Gaussian actions and their actual adjoints, all trained raw
blocks, and the zero population limit of the prescribed finite readout.
It proves three useful statements:

1. Explicit three-layer coefficient inequalities under temporary caps,
   with the exact middle current-return term retained.
2. A single, precise top-source cap lemma sufficient for the orthogonal
   reference's strong continuation through fitting; the lemma is **open**.
3. A sign test on the actual local reference: the new middle multiplier
   has both signs already at first nonzero order. A pointwise dissipative
   replacement for it is false.

The inequalities do not select their caps through a guaranteed fitting
interval. The book's fresh-root anchor is not completed at depth three.

## 2. Exact orthogonal clock system and unconditional primal bounds

Write A=A20+K2:H1->H2 and B=A30+K3:H2->H3. Use phi=tanh and
d(z)=phi'(z). At the reference inputs e1,e2 with labels y1=1,y2=-1,

    z1a=wa, h1a=phi(wa), z2a=A h1a, h2a=phi(z2a),
    z3a=B h2a, h3a=phi(z3a), delta3a=c d(z3a),
    q2a=B* delta3a, delta2a=d(z2a)q2a, q1a=A* delta2a.

The feature equation associated with b=<c,(h31-h32)/2> is exactly

\[
 c_s=\tfrac12\sum_a y_a h_{3a},\quad
 (K_3)_s=\tfrac12\sum_a y_a\delta_{3a}\otimes h_{2a},\quad
 (K_2)_s=\tfrac12\sum_a y_a\delta_{2a}\otimes h_{1a},\quad
 (w_a)_s=\tfrac12 y_a d(w_a)q_{1a}.                         \tag{1}
\]

All tensors are layer typed and use HS norm. Let j_X=d(j), j(0,g)=g.
Its global scalar solution satisfies |j(X,g)-j(Y,g)|<=|X-Y|. Set
w_a=j(X_a,g_a). The last equation becomes

\[
 (X_a)_s=\tfrac12y_aq_{1a}.                                \tag{2}
\]

This is an exact coordinate representation of existing solutions; it
does not already give a Lipschitz Banach-space field.

Fix a feature horizon S>0 and M0>=max(||A20||op,||A30||op), for example
M0=10. Every finite clock-Euler program from c0=0, with nonnegative
steps totaling at most S, satisfies

\[
 \|c_k\|_\infty\le s_k,\quad
 \|K_{3,k}\|_{HS}\le S^2/2,\quad B_S:=M_0+S^2/2,
\]
\[
 \|\delta_{3a,k}\|_2\le S=:R_3,\quad
 \|q_{2a,k}\|_2,\|\delta_{2a,k}\|_2\le B_SS=:R_2,
\]
\[
 \|K_{2,k}\|_{HS}\le B_SS^2/2,\quad A_S:=M_0+B_SS^2/2,
 \sum_a\|X_{a,k}\|_2\le A_SB_SS^2/2.                       \tag{3}
\]

Indeed each feature is bounded by one, each gate by one, and
sum_a |y_a|/2=1. Sum the readout increments, then the top rank increments,
then bound q2 by B*delta3, then sum the lower rank and clock increments.
The inequality sum_k h_k s_k<=S^2/2 gives the displayed constants.
No source cap, discrete energy identity, or population continuation is
used. The same argument applies to an existing continuous feature path.

These bounds eliminate finite-dimensional blowup on a fixed feature
horizon. They do not bound multiplication by q2 in the population norm.

## 3. The complete new middle-population derivative system

This section concerns each separately fixed finite clock-Euler graph.
The source construction is the same fixed-program construction as in
CH3 §5 and maintained C.4.7.3, with a separate label for each edge.
Index a training slot by i=(k,a); q<i means a strictly earlier time.
Put m_i=h_k/2 and gamma_i=y_a m_i. All covariances, deterministic
contractions, gamma, and response coefficients are frozen in a named
derivative. A current passive query, if appended, has its own direct
slot. The estimates below require only the two active queries.

For edge l=2,3, the exact source representations are

\[
 z_{l,i}=\xi_{l,i}+\sum_{q<i}F_{l,iq}\delta_{l,q},\qquad
 q_{l-1,i}=\zeta_{l,i}+\sum_{q\le i}D_{l,iq}h_{l-1,q},       \tag{4}
\]
\[
 F_{l,iq}=\alpha_{l,iq}+\gamma_q E[h_{l-1,i}h_{l-1,q}],
\quad
 D_{l,iq}=\beta_{l,iq}+\mathbf1_{q<i}\gamma_q
                                      E[\delta_{l,i}\delta_{l,q}],\tag{5}
\]
\[
 \alpha_{l,iq}=E[\partial_{\zeta_{l,q}}h_{l-1,i}],\qquad
 \beta_{l,iq}=E[\partial_{\xi_{l,q}}\delta_{l,i}].            \tag{6}
\]

The centered Gaussian source variances are E h_(l-1,i)^2 and
E delta_(l,i)^2, respectively. Population 2 contains the independent
orientation families xi2 and zeta3; population 1 contains g,zeta2;
population 3 contains xi3. Correlations within each history are retained.

At the top, define U3_i;p=partial_xi3p z3_i,
C_k;p=partial_xi3p c_k, and V3_i;p=partial_xi3p delta3_i. Exactly,

\[
 U_{3,i;p}=\mathbf1_{i=p}+\sum_{q<i}F_{3,iq}V_{3,q;p},\quad
 C_{k;p}=\sum_{q<k}\gamma_qd(z_{3,q})U_{3,q;p},
\]
\[
 V_{3,i;p}=d(z_{3,i})C_{k;p}+c_k\phi''(z_{3,i})U_{3,i;p}.
                                                               \tag{7}
\]

In particular beta3_i,i=E[c_k phi''(z3_i)], and other current top
forward slots have zero coefficient. Thus the current part of D3 is
its one distinguished diagonal, not an unweighted sum over samples.

For a middle forward pulse xi2_p put U_i;p=partial z2_i,
V_i;p=partial delta2_i, and Q_i;p=partial q2_i. The exact equations are

\[
 U_{i;p}=\mathbf1_{i=p}+\sum_{q<i}F_{2,iq}V_{q;p},\qquad
 Q_{i;p}=\sum_{q\le i}D_{3,iq}d(z_{2,q})U_{q;p},
\]
\[
 V_{i;p}=d(z_{2,i})Q_{i;p}
                    +\phi''(z_{2,i})q_{2,i}U_{i;p}.        \tag{8}
\]

Separating the current return gives

\[
 V_{i;p}=M_iU_{i;p}
       +d(z_{2,i})\sum_{q<i}D_{3,iq}d(z_{2,q})U_{q;p},
\quad
 M_i=\phi''(z_{2,i})q_{2,i}
                  +\beta_{3,ii}d(z_{2,i})^2.              \tag{9}
\]

For a reverse pulse zeta3_p the same equations hold except that U has
no direct impulse and Q has the direct impulse 1_(i=p). This yields
alpha3_i,p=E[d(z2_i)U_i;p] for that reverse-pulse solution.
Equations (8)–(9) retain every middle term, including the current return.

The bottom clock derivative chi_(a,k;p)=partial_zeta2p X_(a,k) obeys

\[
 \chi_{a,k+1;p}=\chi_{a,k;p}+\gamma_{ka}
 \left[\mathbf1_{(k,a)=p}
       +\sum_{q\le(k,a)}D_{2,(k,a)q}d(w_q)^2\chi_{a(q),k(q);p}\right].
                                                               \tag{10}
\]

Here the notation in the sum includes all preceding slots and the one
possible current slot of its query. Since w_a=j(X_a,g_a), its feature
clock derivative is d(w_a)^2. The q1 phi''(w) multiplier has disappeared
from (10). The q2 phi''(z2) multiplier in (9) has not disappeared.

## 4. Explicit temporary-cap inequalities

Suppose a prefix has response-row caps

\[
 \sum_q|\beta_{2,iq}|\le B_2,\qquad
 \sum_q|\beta_{3,iq}|\le B_3.                               \tag{11}
\]

Define d2=B2+S R2^2 and d3=B3+S R3^2=B3+S^3. By (3)–(5), the
D2,D3 row sums are at most d2,d3. Hence

\[
 q_{2,i}=G_i+J_i,\quad E G_i^2\le S^2,\quad |J_i|\le d_3.   \tag{12}
\]

The source Gaussian G_i need not be independent of J_i. Only its
marginal Gaussian law is used. Likewise q1 is a Gaussian of variance
at most R2^2 plus a bounded correction of magnitude d2.

Equation (10) gives max_a,j |chi_(a,j;p)|<=m_p exp(S d2). The direct
pulse has size m_p, and every subsequent increment is bounded by
h_k d2 times the preceding maximum. Therefore

\[
 |\alpha_{2,ip}|\le m_p e^{Sd_2},\qquad
 |F_{2,ip}|\le f_2m_p,\quad f_2:=1+e^{Sd_2}.               \tag{13}
\]

For (8), sum absolute derivatives over all source slots. Let Ubar_k be
the maximum such U row sum through time k. Since the Q row sum is at
most d3 Ubar_k, the V row sum is at most
(2|q2_i|+d3)Ubar_k. Causal substitution in U yields

\[
 \overline U_k\le
 \exp\left(f_2Sd_3+2f_2\sum_{q<k}m_q|q_{2,q}|\right).       \tag{14}
\]

This estimate does not introduce a supremum of the Gaussian history
inside an expectation. From (12) and Jensen with normalized masses,

\[
 E\exp\left(\lambda\sum_{q<k}m_q|G_q|\right)
               \le2\exp(\lambda^2S^4/2).
\]

Consequently, for p>=1,

\[
 \|\overline U_k\|_p
       \le2^{1/p}\exp(3f_2Sd_3+2pf_2^2S^4).               \tag{15}
\]

Cauchy–Schwarz, ||q2_i||2<=S+d3, and (15) give the explicit improvement
candidate

\[
 \sum_q|\beta_{2,iq}|\le\Psi_2(B_2,B_3):=
 \sqrt2(2S+3d_3)\exp(3f_2Sd_3+4f_2^2S^4).                 \tag{16}
\]

For one zeta3 pulse, its first V equals d(z2_p), while U at that
injection time is zero. Its first subsequent U is bounded by f2 m_p.
The same causal iteration as (14) therefore gives

\[
 |\alpha_{3,ip}|\le c_3m_p,\quad
 c_3:=2f_2\exp(3f_2Sd_3+2f_2^2S^4),\quad f_3:=1+c_3.       \tag{17}
\]

At the top, (7) gives a C row sum at most S times the maximum U3 row
sum and a V3 row sum at most 3S times that maximum. Thus

\[
 \sum_q|\beta_{3,iq}|\le\Psi_3(B_2,B_3):=
                  3S\exp(3f_3S^2).                        \tag{18}
\]

All constants are independent of mesh cardinality. These are estimates
on prefixes with the assumed caps, in the chronological order bottom
responses, middle responses, then top responses. They are not cap removal.

In fact this particular absolute bootstrap cannot close for S>=1.
Since f2>=2 and d3>=B3, (17) implies f3>=4 exp(6B3), and hence

\[
 \Psi_3(B_2,B_3)\ge3\exp(12e^{6B_3})>B_3
                  \quad(B_2,B_3\ge0,\ S\ge1).             \tag{19}
\]

For example use exp(6B3)>=1+6B3 and exp(x)>=1+x to verify the final
strict inequality. Thus B3>=Psi3 is impossible. This refutes a cap
selection from these overestimates, not boundedness of the true rows.
The analogous warning in the book is C.4.7.N19; its remedy is a separate
Lipschitz clock anchor, whose three-layer version is precisely missing.

## 5. An exact sufficient new lemma for the reference

Let q0=1 and q_l=E tanh(sqrt(q_(l-1))G)^2, l=1,2,3, with G standard
normal. Put m3=q3/2>0 and S0=1/m3. These are fixed, computable Gaussian
integrals and S0 is independent of width. The following is a concrete
sufficient lemma; it is **not proved by this report**.

**Top-source cap lemma.** There are h0>0 and Btop<infinity such that
every reference clock-Euler program (1)–(2) of total feature time at most
S0, with hmax<=h0, satisfies

\[
 \sup_{k,a}\sum_{p\le(k,a)}
   |E_3[\partial_{\xi_{3,p}}\delta_{3,ka}]|\le B_{\rm top}. \tag{20}
\]

The derivatives freeze the deterministic objects specified in §3.
Both initialized matrix labels and actual transpose reuse are mandatory.
No population path through S0 is an input to (20).

Why this one cap suffices for reference continuation: (3) and (4) give
q2=G+J with variance<=S0^2 and |J|<=Btop+S0^3. Thus q2 has uniform
Gaussian marginal tails over all admitted clock programs. In clock
distance sum_a||X_a-Xbar_a||2+||K2-K2bar||HS+
||K3-K3bar||HS+||c-cbar||2, all forward differences and the top
delta3,q2 differences are Lipschitz on (3). The only remaining backward
gate subtraction is

\[
 \|[d(z_2)-d(\bar z_2)]\bar q_2\|_2
       \le2R\|z_2-\bar z_2\|_2+2\tau_R(\bar q_2).          \tag{21}
\]

No bottom gate is differentiated in the clock equations. The remaining
adjoint and rank differences use bounded action norms and the HS rank
inequality. Therefore their vector fields satisfy

\[
 \|F(X,K_2,K_3,c)-F(\bar X,\bar K_2,\bar K_3,\bar c)\|_{sum}
          \le C(1+R)d+C\sum_a\tau_R(\bar q_{2a}).            \tag{22}
\]

Uniform speed bounds follow from (3). Comparing two clock-Euler
interpolants gives C exp(CRS0)[(1+R)(h+h')+exp(-cR^2)]. Send their
meshes to zero at fixed R, then R to infinity. Completeness of the clock
L2/HS state yields a strong solution, and bounded-multiplier continuity
passes its integral equation to the limit. The same one-reference
comparison proves uniqueness without imposing tails on a competitor.
The scalar representation j converts back to the raw equations. Raw
competitors also have that representation by Fubini and uniqueness of
the scalar equation w'=d(w)b with integrable b.

This conditional construction would already imply the full reference
fitting mechanism. Let J be the directional differential of
h=(h31-h32)/2 with respect to all three hidden blocks. Then (1) is
c_s=h, hidden_s=J*c, so the strong chain rule gives

\[
 b_s=\|h\|_2^2+\|J^*c\|_{hidden}^2,\qquad c_{ss}=JJ^*c.
\]

As in C.4.5.1 R12, ||c|| is convex while nonzero and starts with
right derivative sqrt(m3). Cauchy–Schwarz then gives b_s>=m3.
Exchange/readout-sign symmetry of the initialized canonical source law
and uniqueness give f1=b=-f2. Hence b reaches one at a first
s_dagger<=S0. Since b_s is bounded on the constructed compact interval,
integral_0^s [2(1-b)]^-1 diverges at s_dagger. The physical clock
ds/dt=2(1-b) defines the reference for every finite physical time and

\[
 \mathcal L_*(t)\le e^{-4m_3t},\qquad
 T_{fit}=\log(8)/(4m_3)\ \Longrightarrow\ \mathcal L_*(T_{fit})\le1/8.
                                                               \tag{23}
\]

The state at s_dagger is a strong learned endpoint. These are consequences
of (20), not unconditional theorems here. A finite-network bridge can
then use a fixed clock reference oracle and (22), retaining the actual
finite readout additively; bottom raw-GD lifting has the sufficient
eta_n sqrt(n)->0 condition of B.1. That bridge and a supported-law
source-cap transfer have not been completed or claimed in this report.

Only beta3 is needed for (22). A neighborhood theorem in raw coordinates
also needs q1 tails or a substitute stability estimate. Requiring both
caps in §4 was one attempted way to obtain the top cap, not an assertion
that both caps are logically necessary for the orthogonal reference.

## 6. Why pointwise signed middle feedback does not supply the cap

There is a direct local sign test, using only initialization and the
already supplied local strong path. At initialization put U_a=z2a(0)
and V_a=z3a(0). Each pair consists of independent centered Gaussians,
of variances q1 and q2 respectively. On population 3 define

\[
 h_0=(\phi(V_1)-\phi(V_2))/2,\quad T_a=h_0d(V_a),\quad
 C_{ab}=E[T_aT_b],\quad k_a=E[h_0\phi''(V_a)].
\]

The exact initial transpose law for B0 gives, on population 2,

\[
 P_a:=B_0^*T_a=\sum_b p_{ab}\phi(U_b)+\Gamma_a,\qquad
 p_{ab}=E[V_bT_a]/q_2,
\quad\Gamma\sim N(0,C),                                   \tag{24}
\]

where Gamma is independent of the initial lower-population variables.
This is the same finite Gaussian conditioning used in C.4.5.1 R25:
condition B0 on its two independent forward queries, retain its forced
mean on their span, and apply the remaining independent Gaussian matrix
to T. The finitely many removed lower projections have vanishing RMS.
It is the actual reused transpose law, not replacement by an independent
matrix. Here Caa>0 because h0 d(Va) is not almost surely zero.

Along the local feature path, c(s)/s->h0 and the hidden state tends
strongly to its initialization. Bounded multiplier continuity gives

\[
 q_{2a}(s)/s\longrightarrow P_a,\qquad
 \beta_{3,aa}^{diag}(s)/s\longrightarrow k_a,
\]
\[
 M_a(s)/s\longrightarrow
 M_a^0:=\phi''(U_a)P_a+k_a d(U_a)^2\quad\hbox{in }L^2.     \tag{25}
\]

Here beta3_diag(s) means the exact current coefficient E[c(s)phi''(z3a(s))].
The physical local path from CH3 supplies a local feature path because
b(0)=0 and the positive clock is invertible on a sufficiently short
interval; only that onset interval is used in (25).

Conditional on U1,U2, the random variable M_a^0 is Gaussian with variance
phi''(Ua)^2 Caa>0 almost surely: q1>0 and tanh'' vanishes only at zero.
It therefore has strictly positive probabilities above any finite
positive threshold and below its negative. In particular there are
epsilon,p>0 for which both events M_a^0>epsilon and M_a^0<-epsilon
have probability at least p. L2 convergence in (25) shows that, for
all sufficiently small s>0, both M_a(s)>s epsilon/2 and
M_a(s)<-s epsilon/2 have positive probability.

Thus M_i<=0 cannot be imposed as a reached-state pointwise property.
This does not refute an averaged signed response bound or the desired
population theorem. It tests the strongest immediate simplification of
(9), rather than asserting that all signed methods are impossible.

### 6.1. A favorable signed expectation at onset

There is nevertheless a strict favorable sign in the *expected* current
coefficient. Oddness, independence of V1,V2, and phi''=-2 phi d give

\[
 y_a k_a=-E[\phi(V)^2d(V)]<0,\qquad
 y_a p_{aa}=\frac{E[V\phi(V)d(V)]}{2q_2}>0,
                   \quad V\sim N(0,q_2).                    \tag{27}
\]

The second integrand is positive except at zero. Averaging (25), the
cross b!=a term vanishes by independence and oddness, and Gamma has zero
conditional mean. Consequently

\[
 E M_a^0=p_{aa}E[\phi''(U)\phi(U)]+k_aE[d(U)^2],
                         \quad U\sim N(0,q_1),
\]
\[
                         y_a E M_a^0<0.                     \tag{28}
\]

Both summands have the asserted strict sign. The L2 convergence in (25)
therefore proves y_a E M_a(s)<0 for every sufficiently small positive s.
Likewise y_a E[c(s)phi''(z3a(s))]<0 there. These are reached local
expectations, not pointwise claims and not a sign assumption at later
feature times.

The complementary past-source signs can be checked exactly at the first
positive clock-Euler node. Let its first step have length h>0. All hidden
raw blocks remain at initialization, while c1=h h0. At output i=(1,a)
and earlier source p=(0,b), formulas (7)–(8) give

\[
 \beta_{3,(1,a),(0,b)}=
       \frac{hy_b}{2}E_3[d(V_a)d(V_b)],
\]
\[
 \beta_{2,(1,a),(0,b)}=
       \frac{hy_b}{2}E_3[d(V_a)d(V_b)]
                              E_2[d(U_a)d(U_b)].            \tag{29}
\]

For the first equation, only the c derivative contributes: the old top
delta is identically zero and its forward-source derivative is zero.
For the second, only the old H2 term of the D3 memory contributes; old
delta2 and its forward-source derivative vanish because c0=0. Distinct
named sources remain distinct even when their covariance is singular.
The exact current coefficients at this node are h k_a and h E M_a^0.
All contractions in (29) are strictly positive.

Thus after the exact odd label folding u_a->y_a u_a, which makes both
labels positive and multiplies beta_(l,i,p) by y_(sample(p)), current
coefficients are negative and the first past coefficients are positive.
This is a viable onset pattern for a signed Volterra argument. Neither
preservation of these signs nor a cap following from them is proved.
In particular the pointwise random term in (9) still has both signs;
replacing its expectation by a coefficient times an independently
averaged pulse would discard its correlation with that pulse.

## 7. Exact unresolved term in the fresh-root argument

The book extracts source coefficients by injecting one independent
Gaussian answer root, proving an L2 post-pulse stability bound, taking
width first, and then letting its amplitude tend to zero. At depth two
the needed stability is N39–N44. At depth three, the linearized fields
necessarily contain

\[
 \dot\delta_2=d(z_2)\dot q_2+
                  \phi''(z_2)q_2\dot z_2,\qquad
 \dot z_2=\dot A h_1+A[d(w)^2\dot X],                    \tag{26}
\]

where the dot here denotes the fresh-pulse variation, not time.
Every other backward term is an action, adjoint, or bounded gate on a
controlled variation, with c bounded by S. At the initial injection the
fresh root is independent of the old fields, and its weighted second
moment can be bounded. At later steps dot z2 is a descendant of the
same reused actions. Independence cannot be reused. The missing
estimate is a causal bound for

\[
 E[|q_2|^2|\phi''(z_2)\dot z_2|^2]
\]

or a signed integrated substitute controlling the resulting pulse
propagator. Bounds on ||q2||2 and ||dot z2||2 alone do not control that
product. Temporary beta3 caps control q2 tails and lead to (14)–(18),
but those caps are the premise to be established. Inserting that premise
into the fresh-root estimate would make the reference anchor circular.

Current status: exact equations and the stated temporary-cap and sign
lemmas are proved in this author derivation; (20), the fitting-horizon
continuation, the supported neighborhood, and all associated long-time
finite-algorithm conclusions remain open in this route. Reopen this route
with a causal pulse estimate for (26), or a direct signed bound on the
middle recursion (8)–(9), rather than with primal energy alone.
