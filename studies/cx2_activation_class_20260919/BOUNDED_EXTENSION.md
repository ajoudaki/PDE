# Bounded activations: smooth extension and the remaining C1,1 gap

Status: scoped author derivation, not independently reviewed or promoted.
The full bounded C1,1 claim remains open here. Sections 1–8 give a
source/continuation proof for the narrower class

\[
 \phi\in C^2(\mathbb R),\qquad
 M=\|\phi\|_\infty<\infty,\quad D=\|\phi'\|_\infty<\infty,\quad
 L=\|\phi''\|_\infty<\infty.                                      \tag{1}
\]

Nonaffinity is needed for fitting, not construction. Neither oddness,
monotonicity, nonvanishing derivative, bounded third derivative nor global
uniform continuity of the second derivative is assumed. Sections 9–10 give
a control-insertion lemma under the original C1,1 assumption and isolate
what it does not prove. The narrower theorem is not a solution for every
activation in the supervisor's assignment.

Scientific dependencies: the prescribed model notation; same-study
REFERENCE_PROOF.md (radial fitting); global_nonlinear.md B.1 (complete
clock construction), C.4.7.3 (complete causal source calculus), C.4.7.4–5
(completion and finite proxy comparison), C.4.7.10 D.2–3 (supported laws
and dense closure); special_data_limits.md III.F (fixed Gaussian programs,
actual adjoints, HS increments and strong chain rules); same-study
CLOSURE_PROOF.md and PARTIAL_RESULT.md §3. The changes to the tanh
source argument are proved below; its third-derivative estimates are not
assumed. No experiments, other-study inputs, Git actions or maintained
edits were used.

Constants may depend on M,D,L,T and the activation's local second-derivative
moduli. They do not depend on mesh length, support cardinality, minimum
atom mass, query rank, width or approximation order. A generic constant
may increase between displays.

## 1. Exact fallback theorem

Use u=x/sqrt(2) in S1, two hidden layers with the same phi, stored Gaussian
variances (1,1/n,1/n²), mobilities (n,1,n), and unhalved mean squared loss.
The full first row w belongs to L²(Omega1;R²), c to H2=L²(Omega2), and
A=A0+K:H1→H2, where only K is Hilbert–Schmidt. A0* is the actual adjoint
of the initialized action. The bound ||A0||≤10 suffices. Initially
(w,K,c)=(g,0,0), with g standard two-dimensional Gaussian. This population
zero readout is never substituted for the actual finite random readout.

For a law mu on S1×{+1,-1}, write

\[
 h(u)=\phi(w\cdot u),\ Z(u)=Ah(u),\ H(u)=\phi(Z(u)),\
 d(u)=c\phi'(Z(u)),\ Q(u)=A^*d(u),\
 f(u)=E_2[cH(u)],\ r(u,y)=f(u)-y.
\]

The full-row equation is

\[
 (w',K',c')=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,\
 \int r d(u)\otimes h(u)\,d\mu,\
 \int rH(u)\,d\mu\right).                                      \tag{2}
\]

Let mu*=(delta_(e1,+1)+delta_(e2,-1))/2. Under (1), for every fixed
T<infinity there is eps_T>0 such that every Borel law with mass one half
at each label and |u-e1|≤eps_T at label +1, |u-e2|≤eps_T at label -1
has a canonical strong C1 solution of (2) through T. It is unique among
strong raw solutions on the prescribed carrier and uniquely continues
from each reached state. For finite a,C>0,

\[
 \sup_{t\le T,u\in S^1}\tau_R(Q(t,u))\le Ce^{-aR^2},\qquad
 \tau_R(V)=\|V1_{|V|>R}\|_2,\quad R\ge1.                         \tag{3}
\]

The same bound holds uniformly for every sufficiently fine finite-supported
raw Euler program used in this construction. It bounds each time and
input with common constants, not a random maximum over them.

For nonaffine phi, define the initialization constants

\[
 q_0=\tfrac14E[\phi(Y_1)-\phi(Y_2)]^2>0,\qquad
 T_\phi=\frac{\log8}{4q_0},                                    \tag{4}
\]

where Cov(Y)=v I+mu0² 11^T, mu0=E phi(G), v=Var(phi(G)), and G is
standard normal. At T=T_phi, eps_T can be decreased once so every
law in this fixed supported family satisfies L_mu(T_phi)≤1/4.

## 2. Unconditional raw bounds and one-reference comparison

For a finite law with masses p_a>0 summing to one, use any positive
Euler mesh with total length ≤T. Put m_ka=h_kp_a and
gamma_ka=-2m_ka r_ka. Bounded activation gives

\[
 \|c_{k+1}\|_\infty\le(1+2M^2h_k)\|c_k\|_\infty+2Mh_k.
\]

For a nonconstant activation M>0. Therefore

\[
 C_T=(e^{2M^2T}-1)/M,\quad R_T=e^{2M^2T},\quad
 A_T=10+2TR_TDC_TM,\quad
 W_T=\sqrt2+2TR_TD^2C_TA_T                                    \tag{5}
\]

bound respectively ||c||infinity, |r|, ||A||op and ||w||2 at every node.
The middle bound sums the exact HS rank norm
||d⊗h||HS=||d||2||h||2≤DC_TM; the row bound uses
||Q||2≤A_TDC_T. These bounds also give a common raw speed V_T.
There is no mesh restriction, source cap or discrete energy assumption.

For two states on this ball, forward, upper backward and Q differences
are Lipschitz in raw sum distance d and input distance. For example,

\[
 \|h(u)-\bar h(v)\|_2\le D(d+W_T|u-v|),\quad
 \|Z-\bar Z\|_2\le A_T\|h-\bar h\|_2+M\|K-\bar K\|_{\rm HS},
\]
\[
 \|d-\bar d\|_2\le D\|c-\bar c\|_2+C_TL\|Z-\bar Z\|_2.
\]

The adjoint subtraction proves the corresponding Q estimate. Only the
lower gate needs a tail cutoff:

\[
 \|\phi'(z)q-\phi'(\bar z)\bar q\|_2
 \le D\|q-\bar q\|_2+LR\|z-\bar z\|_2+2D\tau_R(\bar q).        \tag{6}
\]

Subtract each residual and rank factor in (2), use the HS rank difference
inequality, and integrate a coupling of data laws. For data W1 distance q,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{(1)}
 \le C_T\{(1+R)(d+q)+\int\tau_R(\bar Q(u))\,d\nu\}.             \tag{7}
\]

For arbitrary strong competitors whose readout is only L2, localize also
the unchanged reference readout in the upper gate product. The constructed
reference readout is bounded, so this adds no tail above C_T.

## 3. Source calculus under one temporary cap

At a fixed smooth graph apply III.F.9–10. The independent orientation
Gaussian groups have full covariances E[xi_i xi_j]=E[h_i h_j] and
E[zeta_i zeta_j]=E[d_i d_j]. Define
alpha_i,p=E partial_(zeta_p)h_i and beta_i,p=E partial_(xi_p)d_i.
Each named derivative freezes covariance, residuals, contractions and
previously selected deterministic coefficients. The complete current
passive reverse row has one distinguished current source, even at rank
loss. The exact equations are

\[
 F_{i,p}=\alpha_{i,p}+\gamma_pE[h_i h_p]\quad(t(p)<t(i)),
\]
\[
 D_{i,p}=\beta_{i,p}+1_{t(p)<t(i)}\gamma_pE[d_i d_p],\quad
 Z_i=\xi_i+\sum_{p<i}F_{i,p}d_p,\quad
 Q_i=\zeta_i+\sum_{p\le i}D_{i,p}h_p.                           \tag{8}
\]

The current beta is E[c phi''(Z_i)] in its one current slot.
Under a temporary cap B on already constructed beta rows,

\[
 D_B=B+2R_TD^2C_T^2T,\quad
 \sum_p|D_{i,p}|\le D_B,\quad Q_i=\zeta_i+J_i,\quad
 |J_i|\le MD_B,\quad E\zeta_i^2\le D^2C_T^2.                   \tag{9}
\]

Jensen with the time/sample masses and the scalar Gaussian moment bound
gives, for lambda≥0,

\[
 E\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le2\exp\{\lambda TMD_B+\lambda^2T^2D^2C_T^2/2\}.             \tag{10}
\]

No independence in time is required.

For a past lower pulse p=(s,b), v_k,p=partial_(zeta_p)w_k has the exact
N7 recursion: differentiate the row update and (8), retaining phi'', Q,
and the complete D row. Its direct pulse is at most 2R_TD m_p.
The later propagation multiplier for its past maximum is at most

\[
 1+2R_Th_j\left(D^2D_B+L\sum_a p_a|Q_{ja}|\right).
\]

Iteration and (10) show, for every finite moment order p,

\[
 \|\max_{j\le k}|v_{j,p_0}|/m_{p_0}\|_{L^p}\le C_{B,p},
 \qquad |\alpha_{i,p_0}|+|F_{i,p_0}|\le C_Bm_{p_0}.            \tag{11}
\]

For upper derivatives U=partial_xi Z, C=partial_xi c,
V=partial_xi d, the exact equations are

\[
 U_{i;p}=1_{i=p}+\sum_{q<i}F_{i,q}V_{q;p},\qquad
 C_{k;p}=\sum_{q<k}\gamma_q\phi'(Z_q)U_{q;p},
\]
\[
 V_{i;p}=\phi'(Z_i)C_{k;p}+c_k\phi''(Z_i)U_{i;p}.              \tag{12}
\]

Sum absolute values over source slots. The C row is at most
2R_TD sum_(j<k)h_j max_a sum_p|U_ja;p|, so the V row is at most
(2R_TD²T+C_TL) times the largest U row. Insert (11) in the U equation
and iterate. This bounds all complete upper derivative rows pointwise by
a finite C_B. The current row uses only earlier lower updates and strictly
past upper-memory terms, not its own unknown beta cap. Formula (9) and
the row update also give every fixed-order moment of w,Q,Z under the cap.

## 4. Unconditional orthogonal clock source cap

Let J_s=phi'(J), J(0,z)=z. This scalar flow is global and |J_s|≤D.
Set w_a=J(X_a,g_a). The exact reference clocks satisfy

\[
 X_a'=-r_aQ_a,\qquad K'=-\sum_a r_a d_a\otimes h_a,\qquad
 c'=-\sum_a r_aH_a.                                          \tag{13}
\]

B.1 constructs their unique global flow and clock Euler approximations.
Its estimates hold in HS for K by III.F.30. No inverse of phi' is needed.

For two same-root clock states put x=sum_a||X_a-Xbar_a||2,
k=||K-Kbar||HS, z=||c-cbar||2. Active field differences obey

\[
 \sum_a\|h_a-\bar h_a\|_2\le D^2x,\quad
 V:=\sum_a\|Z_a-\bar Z_a\|_2\le A_TD^2x+2Mk,
\]
\[
 D_v:=\sum_a\|d_a-\bar d_a\|_2\le2Dz+C_TLV,\quad
 P:=\sum_a\|Q_a-\bar Q_a\|_2\le A_TD_v+2DC_Tk,
\quad S:=\sum_a|r_a-\bar r_a|\le2Mz+C_TDV.
\]

Subtracting (13) bounds its three velocity differences by

\[
 A_TDC_TS+R_TP,\quad
 DC_TMS+R_T(MD_v+DC_TD^2x),\quad MS+R_TDV.                    \tag{14}
\]

A fixed L0 makes their sum ≤L0(x+k+z), so later Euler differences
amplify by at most E0=exp(L0T). The bounds (5) remain valid after a fresh
root is inserted into one answer and all descendants are recomputed:
bounded activation and derivative preserve the readout/rank bounds.
No energy identity for a forced graph is used.

A reverse-answer forcing eps e at slot p changes its clock update by at
most 2R_Tm_p|eps|||e||2. A forward-answer forcing changes that node's
H,d,r,Q by at most D,C_TL,C_TD,A_TC_TL times |eps|||e||2.
Subtracting the three updates therefore bounds its immediate clock/HS/L2
change by P0m_p|eps|||e||2, where P0 is a finite polynomial in these
bounds. A passive later d is K0-Lipschitz in clock sum distance with
K0=D+C_TL(A_TD²+M). Its change is at most
P0K0E0m_p|eps|||e||2.

For source extraction keep the graph and nonzero eps fixed, take width
to infinity, then send eps to zero. The local new Gaussian root enters
as slot+eps e. Conditional Gaussian integration by parts gives

\[
 E[eV^\varepsilon]=\varepsilon E[\partial_{\rm slot}V^\varepsilon].
                                                                    \tag{15}
\]

At every fixed graph, named clock derivatives have a finite deterministic
bound, since |J_s|≤D, |partial_X phi(J)|≤D², |c|≤C_T and |phi''|≤L.
For the fixed-program theorem, first clip the clock and root arguments
smoothly. This bounds the otherwise possibly large root derivative of J;
its named clock derivative remains bounded by D independently of the
clipping levels. Remove these clips chronologically at a fixed graph:
its clock is a finite linear Gaussian expression plus a bounded expression,
so every needed root-derivative exponential is integrable. The named
derivatives have the preceding bounds independent of these clips.
Continuity of phi'' suffices for dominated convergence of the named
derivatives as eps→0. The complete III.F singular-source construction
applies; no derivative transverse to a singular value law is inferred
without this independent forcing. The unforced expression is independent
of e. Applying Cauchy–Schwarz in (15) proves

\[
 |\beta^{cl}_{i,p}|\le P0K0E0m_p\quad(p<i),\qquad
 |\beta^{cl}_{i,i}|\le C_TL.
\]

Hence B_cl=C_TL+TP0K0E0 bounds every reference clock row through T,
including passive inputs. Splitting reference atoms preserves the cap:
each past single-pulse coefficient splits proportionally to its mass,
whereas the current direct coefficient stays one distinguished slot.

Formula (9) gives clock Q Gaussian tails. Clock convergence and
tau_(2R)(Q)≤2||(|Q|-R)_+||2 pass these tails to the actual reference
flow. Thus reference tails have been established before raw-reference
source consistency and before any changed-law cap.

## 5. Differentiated consistency with zeros allowed

For R≥1 let
omega_R(a)=sup{|phi''(z)-phi''(zbar)|: |z|,|zbar|≤R, |z-zbar|≤a}.
Continuity implies omega_R(a)→0 for fixed R as a→0; no global modulus
is assumed.

The scalar clock defect relative to raw Euler is
e_h(z,b)=J(hb,z)-z-hb phi'(z). Put q=h|b|. Integration gives
|e_h|≤LDq²/2. Also
J_z(s,z)=exp(integral_0^s phi''(J(v,z))dv). If
omega_z(a)=sup_(|v-z|≤a)|phi''(v)-phi''(z)|, the same integral gives

\[
 |\partial_z e_h|
 \le q\{\omega_z(Dq)e^{Lq}+L(e^{Lq}-1)\},\qquad
 |\partial_b e_h|\le LDh^2|b|.                              \tag{16}
\]

Indeed |J(v,z)-z|≤D|v| and |J_z(v,z)|≤exp(L|v|). The b derivative
is h[phi'(J(hb,z))-phi'(z)]. These bounds use no inverse gate or third
derivative.

Apply (16) to the already capped clock program: z^+=J(hb,z),
b_a=-r_aQ_a. Under its cap, b has uniform Gaussian tails and z has
uniform fixed-order moments. Normalized past named derivatives of z,b
are bounded at every fixed moment order by (11), or directly by the
clock recursion. At the one direct pulse, partial_p z_s=0 and
|partial_p b_s|/m_p≤2R_T/h_s, so the b term costs O(h_s) after
normalization. At later steps, Holder and (16) imply

\[
 \sup_{p_0}\frac1{m_{p_0}}
    \sum_k\|\partial_{p_0}e_{h_k}\|_{L^p}
 \le\nu_p(h_{\max}),\qquad \nu_p(h)\longrightarrow0.           \tag{17}
\]

Here is the uniformity check for the only non-polynomial term. First
restrict |z|,|b|≤N. Then
omega_z(Dh|b|)≤omega_(N+DN+1)(Dh_max N) for h_max≤1, which tends
to zero. On the complement use omega_z≤2L, Holder, the Gaussian
exponential moments of b and fixed higher moments of z and the normalized
pulses. Their bounds make the complement uniformly small as N increases.
The factor exp(Lh|b|)-1 is handled identically; sum h_k²≤Th_max handles
the remaining terms. This also proves summed value consistency.
Only the known clock cap is used in (17).

## 6. Replacing the third derivative by a compact-set modulus

Suppose ||X-Xbar||2≤c delta and both second moments are ≤S².
Split the event |X|,|Xbar|≤R, |X-Xbar|≤a from its complement.
Bounded phi'' and Markov give, for finite p,

\[
 \|\phi''(X)-\phi''(\bar X)\|_p
 \le \omega_R(a)+2L\{c^2\delta^2/a^2+2S^2/R^2\}^{1/p}.       \tag{18}
\]

Consequently there is a deterministic nondecreasing modulus
Omega_B(delta)→0 that bounds all the L12 and L2 gate differences needed
below: take the infimum of the right side over R≥1, 0<a≤1, add
C_B delta^(1/16), and then a nondecreasing envelope if needed.
The limit follows by first fixing R large, then a small, then delta small.
This also works when phi'' oscillates increasingly fast at infinity.

Bounded phi' gives its L12 gate difference by interpolation with the
L2 difference. Under the cap, Q is bounded in L24 by (9); interpolation
of its L2 difference gives ||Q-Qbar||12≤C_B delta^(1/11).
These are the other terms absorbed in Omega_B.

Compare two programs on the same mesh and joint source carrier, with
matched masses/labels and uniformly paired inputs at distance≤eps.
Let eta bound raw state distances, delta=eta+eps≤1. Let E_k be the
supremum of complete beta-row differences over paired passive outputs
at distance≤eps; match past slots and the distinguished current slot.
Suppose earlier rows have a fixed cap B. The second program may be the
known clock reference, whose scalar defects are (17). Put nu=0 for
raw/raw comparison and nu=nu_p(h_max) for raw/clock comparison.

The full Gram source coupling gives exactly
||xi-xibar||p=||G||p||h-hbar||2 and
||zeta-zetabar||p=||G||p||d-dbar||2. Factor subtraction from Section 2
bounds h,Z,d,Q and residual differences in L2 by C_T delta. The learned
part of a D-row difference is therefore at most C_T delta:

\[
 \sum_q|D_{ka,q}-\bar D_{ka,q}|\le E_k+C_T\delta.              \tag{19}
\]

Subtract N7, putting changes of the evolving lower pulse into unbarred
propagation. The remaining terms are exactly: the changed direct pulse;
the product with factors r,u,phi'',Q,u and a reference pulse; and
the memory product with factors r,u,phi',D,phi',u and a reference pulse.
Three L12 factors put each forcing product in L4. Use (11),(18),(19)
for these factors. The propagation exponential is bounded in L4 by
(10). Minkowski over the time/sample masses followed by Holder gives

\[
 \|\max_{j\le k}|v_{j,p}-\bar v_{j,p}|\|_2/m_p
 \le C_B\{\Omega_B(\delta)+\nu+\sum_{j<k}h_jE_j\}.             \tag{20}
\]

All summands retain h_jp_a. No unbounded time/input maximum of Q or its
difference appears. Subtract alpha=E[phi'(w·u)u·v] and the learned
F term to obtain the same bound for the corresponding F-row density.

Subtract (12) and sum source indices. The unvaried upper derivative
row sums are pointwise bounded by Section 3. The U forcing is the F-row
difference just established; its propagated part is a time integral
of the V-row difference. C has only the past time integrator and bounded
phi'. V adds the changed phi', c, and phi'' factors. Formula (18) with
p=2 bounds the last, replacing exactly H40.E23's third-derivative use.
The two causal Gronwall iterations give

\[
 E_k\le C_B\{\Omega_B(\delta)+\nu+\sum_{j<k}h_jE_j\},\qquad
 E_k\le C_Be^{C_BT}\{\Omega_B(\delta)+\nu\}.                    \tag{21}
\]

No current unknown E_k appears in the first right side: the lower state
uses past updates and both upper memory sums are strictly past. Bound
the current diagonal directly by (18). This is the causal condition
needed at the first potentially failed row.

## 7. Noncircular cap closure and Borel completion

First compare raw reference Euler to the physical reference. Raw bounds
(5), estimate (7) and the already proved physical reference tails yield

\[
 \sup_k d(\theta^r_k,\theta_*(t_k))
 \le\inf_{R\ge1}C_Te^{C_T(1+R)T}
       \{(1+R)h_{\max}+Ce^{-aR^2}\}\longrightarrow0.           \tag{22}
\]

Clock Euler converges to the same target by (14). Its raw distance
eta_h to raw Euler thus tends to zero independently of a raw source cap.
At a first failed raw row apply (21) with B=B_cl+1, delta=eta_h
and nu from (17). For sufficiently small h_max the difference is
below 1/2, so the row is below B_cl+1/2. This contradicts failure.
Initialization beta=0 starts induction. Thus every sufficiently fine raw
reference program has cap B_*=B_cl+1.

Now compare any finite supported law with its split reference on the
same mesh. Splitting preserves B_*. Both programs have the crude bounds;
only reference tails are needed. The same-node version of (7) gives

\[
 \sup_kd(\theta_{\mu,k},\theta_{*,k})\le\Phi_T(\varepsilon),\quad
 \Phi_T(s)=\inf_{R\ge1}C_Te^{C_T(1+R)T}
                \{(1+R)s+Ce^{-aR^2}\}\longrightarrow0.       \tag{23}
\]

There is no mesh defect. Take B=B_*+1 and choose a fixed eps_T>0 with
delta=Phi_T(eps_T)+eps_T≤1 and
C_B exp(C_BT) Omega_B(delta)<1/2. At the first failed changed-law row,
(21) contradicts failure. These constants use initialization, activation,
its local moduli and T; they do not use a changed-law target path.
Thus all finite supported laws have a uniform cap, independent of masses,
rank and cardinality. Appending a shorter last step covers recomputed
fields on interpolation segments. Formula (9) proves their passive
Gaussian tails.

Approximate each Borel conditional law inside its own compact cap by
finite partitions, retaining the label masses. Two such Euler
interpolants satisfy

\[
 \sup_{t\le T}d(\theta^h_\mu,\theta^{h'}_\nu)
 \le\inf_{R\ge1}C_Te^{C_T(1+R)T}
 \{(1+R)(W_1(\mu,\nu)+h+h')+Ce^{-aR^2}\}.                    \tag{24}
\]

At fixed R send law/mesh errors to zero, then send R to infinity.
This proves Cauchy convergence in full-row L2+HS+readout L2, independently
of the approximations. The forward and upper backward fields are
continuous in u in L2; the lower product is continuous by III.F.34.
Compactness of S1 permits the Hilbert-valued integrals to pass through
law convergence. Compactness of the limiting state path makes the
integrand convergence uniform in time. Thus the limit is strong C1
and solves (2). Positive-part tails pass as in Section 4, proving (3).
The same estimate against any competing strong path, with the constructed
path as its sole tail-bearing endpoint, proves uniqueness and reached
continuation. The exact energy identity follows after this construction,
by the strong chain rule and actual HS adjunction.

## 8. Fitting, represented inputs, closure and the finite bridge

The signed radial theorem of REFERENCE_PROOF.md gives
L_*(t)≤exp(-4q0t). Its hypotheses hold by Section 4. The upper Gaussian
pair in (4) has full support because v>0; if q0=0, continuity and varying
one argument force phi constant. Thus q0>0 and L_*(T_phi)≤1/8.

Couple supported inputs to their axes. The state and input comparison
gives

\[
 \|r_\mu(T_\phi)-r_*(T_\phi)\|_{L^2(\mathrm{coupling})}
 \le C\{\Phi_{T_\phi}(\varepsilon)+\varepsilon\}.
\]

Decrease eps_T until the right side is at most
(1/2−1/sqrt(8))/2. Minkowski then gives
L_mu(T_phi)≤(1/4+1/(2sqrt(8)))²<1/4. This strict margin also
transfers the threshold 1/4 to actual finite training with probability
tending to one after the finite bridge below.

There is also an activation-dependent early observation time with positive
paired activity and visited-law nonaffinity. Apply maintained C.3 with its
weighted-loss correction to the reference: its coefficients are
p_a=omega_a y_a=y_a/2. The inputs are nonparallel, both labels nonzero,
both Gaussian variances and all mobilities positive, and the population
readout zero. Its complete proof therefore gives, in both layers and for
each anchor, an activation displacement
H_a^ell(t)-H_a^ell(0)=t²V_a^ell+o_L2(t²) with ||V_a^ell||2>0.
Choose a fixed t_act in (0,min(T_local,T_phi)) inside its sufficiently
short interval. The minimum j_* of the four paired RMS displacements at
that time is positive. On [0,t_act], all four reference preactivation
variances and best-affine-fit errors have a common positive lower bound.
The affine-fit assertion uses the exact moment expression

\[
 \operatorname{Var}(\phi(Z))-
 \operatorname{Cov}(Z,\phi(Z))^2/\operatorname{Var}(Z).
\]

Initial/current field convergence under the same-input coupling is uniform
in time and input by (23) and the forward estimates. It preserves the
initial and current coordinates on the same neuron population. Decrease
eps_T again until every supported query's paired RMS at t_act is at least
j_*/2. Then each layer's training-averaged squared paired displacement is
at least j_*²/4. Cauchy–Schwarz in time also makes its integrated squared
activation speed positive, with lower bound j_*²/(4t_act).
The same uniform L2 convergence preserves the reference variances and
all moments in the displayed affine-fit expression; after one more fixed
decrease of eps_T, those errors stay positive throughout [0,t_act] for
each supported input. These assertions concern this reduced supported
family. No activity claim is made for arbitrary Borel laws outside it,
or specifically at the later fitting endpoint.

Choose a fixed positive rational rho with 2rho≤eps_T. Put
U(s)=((1-s²)/(1+s²),2s/(1+s²)) and let R be the quarter-turn.
For four rational endpoints in [-1,1], let S,V be uniform on their
closed intervals, including degenerate intervals, and use

\[
 \tfrac12\operatorname{Law}(U(\rho S),+1)
 +\tfrac12\operatorname{Law}(R U(\rho V),-1).                  \tag{25}
\]

The identity |U(s)-U(t)|≤2|s-t| puts these laws in the proved class.
S=0,V=1 gives input inner product -2rho/(1+rho²), strictly nonzero.
Two nondegenerate intervals give a nonatomic law since U is injective.
The radius does not shrink with closure order or numerical refinement.
Raw inputs are sqrt(2) times these directions.

The fallback supplies the strong target and tails S/E of
CLOSURE_PROOF.md. Include its activation-independent smooth dictionary
in the common carrier. Each finite program stays in its reducing
completed spaces, and strong completion preserves them and their HS
block. For Borel mu, replace sums in that closure by integrals.
As in the complete D.3 proof, fixed order has bounded marks and a
locally Lipschitz finite-type field; its energy and bounded phi give
global finite-horizon bounds. The target sets {h(t,u)},{d(t,u)} are
compact in L2 and {K'(t)} compact in HS. Strong convergence of the
dictionary filters and both initialized action directions makes all
three omitted-source errors tend uniformly to zero. The one-reference
estimate (7), with these errors added, then proves uniform full-circle
prediction and fixed typed paired-observation convergence. No tail
premise for projected paths or cross-width operator norm is used.

For the finite bridge, fix a supported finite comparison law, a mesh
and cutoffs before width tends to infinity. III.F identifies this
finite program and its HS/Frobenius rank contractions. The proxy keeps
the actual finite initial readout additively. Its tails are (9).
The complete C.4.7.5 comparison uses only the actual finite energy ball,
bounded/Lipschitz gates and these proxy tails; those hypotheses have
now been supplied under (1). Removing the fixed law, mesh and cutoffs
therefore identifies actual finite GF through T_phi, including fixed
initialized/current pairs and quadratic contractions. PARTIAL_RESULT.md
§3's raw-GD stopping argument adds O(eta_n) to the preceding-node
error and admits every eta_n→0, with tails only on the reference proxy.
The actual finite data laws may be arbitrary circle/binary laws approaching
the fixed supported Borel target in W1; only the fixed comparison law
must satisfy the support condition. Indeed (5) and the actual finite
energy ball hold for all such labels/inputs, and (7) places tails only
on the supported comparison proxy. This includes deterministic empirical
laws and iid empirical laws converging in probability, with sample count
and width tending to infinity without a relation between them.

These are qualitative limits in the declared successive proof order,
not finite accuracy certificates or arbitrary diagonals with dictionary
order. Execution additionally needs consistent evaluators for phi and
phi'; effective selection of the radius by this proof needs local
modulus/bound information. Bare regularity does not imply computability.
The existential rational radius in (25) is a mathematical statement.

## 9. Positive control-insertion lemma under the original C1,1 assumption

Assume only |phi'|≤D and Lip(phi')≤L. For two unit directions set
gamma=|u1·u2| and V_i(w)=phi'(w·u_i)u_i. Let integrable controls b_i, db_i
drive w'=sum_i b_i V_i(w), with the same initial row for b and b+db.
Put v=integral sum_i|b_i| and d=integral sum_i|db_i|. Then

\[
 \left|w_{b+db}(t)-w_b(t)
       -\sum_iV_i(w_b(t))\int_0^t db_i(s)ds\right|
 \le LD e^{L(v+d)}\{2\gamma(v+d)d+d^2\}.                     \tag{26}
\]

For a smooth activation let Phi_b(t,s) be its control flow.
The insertion kernel is D Phi_b(t,s)V_i(w_b(s)). Differentiating the
transported field and integrating gives, up to bracket sign convention,

\[
 D\Phi_b(t,s)V_i(w_b(s))-V_i(w_b(t))
 =\int_s^tD\Phi_b(t,\tau)
               \sum_jb_j(\tau)[V_i,V_j](w_b(\tau))\,d\tau.
\]

Direct differentiation shows

\[
 [V_i,V_j]=(u_i\cdot u_j)
 [\phi''(w\cdot u_j)\phi'(w\cdot u_i)u_j
 -\phi''(w\cdot u_i)\phi'(w\cdot u_j)u_i].
\]

Cross brackets have norm ≤2gamma LD and self brackets vanish.
Also ||D Phi_b(t,s)||≤exp(Lv). For b+r db these facts bound
the insertion-kernel/endpoint difference by
2gamma LD(v+d)exp(L(v+d)). Integrate in r∈[0,1] and time.
The remaining endpoint change is bounded by
|V_i(w_(b+rdb)(t))-V_i(w_b(t))|≤LDd exp(L(v+d)).
This proves (26).

For C1,1 phi, mollify; smooth fields converge uniformly and retain D,L.
Their controlled flows converge uniformly by the integral difference
inequality. Pass every term in (26). Thus no classical spatial derivative
of the nonsmooth flow or derivative of a bracket is claimed. Under a
temporary neural source cap, the unforced control variation has all
exponential moments by (10). This is a genuine small-angle reduction for
two fixed inputs, but its right side also involves perturbed controls.

## 10. Exact remaining implications for the full bounded C1,1 claim

1. A full fresh Gaussian query changes b through A0,A0*, learned ranks
   and residual feedback. To turn (26) into a uniform L2 response bound,
   one must control products such as exp(Lv) integral|db| uniformly over
   meshes. An L2 action norm does not control those products. Bounds
   on one unforced named lower pulse are not a full fresh-query reinsertion
   estimate. A possible route is an auxiliary clock-form linear response
   on the actual background, leaving its actual upper gates unchanged;
   its identification with the needed source-row bound is still unproved.

2. Without that alternative representation, the upper term
   E[c phi''(Z)U] in (12) requires a reached-law weak derivative passage.
   For C2, (18) proves the needed stability. For C1,1 only, phi'' is an
   essentially bounded a.e. derivative and need not be continuous.
   Uniform bounds on mollified second derivatives do not furnish the
   common vanishing modulus used in (21). No such weak passage has been
   proved here.

3. Two fixed inputs do not cover two nonatomic arcs. Within one label
   class the directions are nearly parallel, and their C1,1 brackets
   need not be small. For an exact compact example take a smooth compactly
   supported chi equal to one near zero and
   phi(z)=chi(z)[z+(z_+)²/2]. This is bounded C1,1 with bounded derivative.
   Set u=e1, v=(cos(theta),sin(theta)), w=(-theta/4,1).
   For small theta>0, w·u<0<w·v, both inside chi=1. Thus
   phi'(w·u)=1, phi''(w·u)=0, phi''(w·v)=1. The bracket above equals
   (cos(theta))v, whose norm tends to one as |u-v| tends to zero.
   This refutes uniform smallness of within-arc brackets even on a
   bounded row set; it does not refute averaging or another construction.

The missing implication is a reached-source/tail estimate uniform over
a fixed positive supported two-arc family through T_phi for every bounded
C1,1 activation. Once supplied, Sections 2 and 7–8 give the continuation
and identification chain. Fixed positive proximity to an orthogonal flow
alone is not a Cauchy construction for a changed law.

The full C1,1 extension is not declared proved. The bounded C2 theorem
with bounded first and second derivatives is the strongest complete
fallback derived here; (26) is a separate structural result under the
original regularity.
