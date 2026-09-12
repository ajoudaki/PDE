# A source cap in an integrated-control neighborhood of the full reference

Second-round candidate, 2026-09-12. Author: continuation route.
The first-round ROUTE_CONTINUATION.md is frozen and unchanged.
Cross-pollination with the coordinator's ROUTE_RESIDUAL_CLOCK.md was
explicitly authorized. This file supplies a controlled continuation
lemma; it does not assume a source estimate or endpoint Gram gap.
The proof has been checked by its author, not independently reviewed.

## 1. Statement with the exact control and approximation conventions

Keep the canonical two-hidden tanh carrier, Gaussian action \(A_0\)
with its actual adjoint, \(w(0)=g\sim N(0,I_2)\), \(K(0)=0,c(0)=0\),
and \(A=A_0+K\). The raw Hilbert metric is
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\|\Delta K\|_{\rm HS}^2+\|\Delta c\|_2^2.
\]
For each \(u\in S^1\), define
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad
 \Delta^2(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^2(u),
\]
\[
 g_u(\theta)=
 \bigl(\phi'(w\cdot u)Q(u)u,\,
       \Delta^2(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad\phi=\tanh.
 \tag{CT1}
\]
This is the actual raw gradient of the scalar prediction. It retains
the original architecture and both orientations of the reused matrix.

Fix finitely many directions \(u_1=e_1,u_2=e_2,u_3,\ldots,u_J\)
on the circle. They need not be distinct, separated, or orthogonal.
For a physical interval \(I=[0,T]\), where \(T\) is arbitrary and may
also be infinite, let \(a_j(t)\) be deterministic integrable controls.
The comparison controls are the complete reference history
\[
 a_{*,1}(t)=e_*(t),\qquad a_{*,2}(t)=-e_*(t),\qquad
 a_{*,j}(t)=0\quad(j\ge3),
 \qquad e_*=1-f_*(e_1)>0.
 \tag{CT2}
\]
Its total absolute mass is the reference feature length, at most
\(s_\dagger\le10\). Only finiteness of this bound is necessary below.
The controlled equation is
\[
 \theta'(t)=\sum_{j=1}^J a_j(t)g_{u_j}(\theta(t)).
 \tag{CT3}
\]

**Controlled source-tube theorem.** There are \(\delta>0\), \(h_0>0\),
\(B<\infty\), \(M<\infty\), and \(c>0\), depending only on the
reference feature segment and the canonical model, with the following
properties. They are independent of \(T\), the number of time steps,
and the minimum nonzero control coefficient.

Assume
\[
 q:=\int_I\sum_j|a_j(t)-a_{*,j}(t)|\,dt\le\delta.
 \tag{CT4}
\]
Use the common dominating measure
\[
 ds=\sum_j(|a_j(t)|+|a_{*,j}(t)|)\,dt.
 \tag{CT5}
\]
On a finite partition in this control clock with maximal interval
length at most \(h_0\), take exact integrated coefficients
\[
 \gamma_{kj}=\int_{I_k}a_j(t)\,dt,\qquad
 \bar\gamma_{kj}=\int_{I_k}a_{*,j}(t)\,dt
 \tag{CT6}
\]
and run raw Euler with these coefficients and the same initialization.
Every passive backward-source row at every node satisfies
\[
 |\beta_{ku,ku}|+\sum_{s<k,j}|\beta_{ku,sj}|\le B,\qquad
 \sup_{u\in S^1}\tau_R(Q_k(u))\le M e^{-cR^2},\quad R\ge1.
 \tag{CT7}
\]
The corresponding readout tails have the same bound after enlarging
\(M\). Current passive slots are distinguished as described below.
Zero controls and padding are permitted. The estimate retains all
source slots from the entire reference history.

The raw Euler approximations converge strongly to a unique solution
of (CT3), absolutely continuous in the control clock and in physical
time on every finite interval. The solution is unique among strong
solutions on the prescribed carrier with the same controls. It has
the tails in (CT7), with adjusted constants. Its restrictions give
unique reached continuations. For fixed controls, actual finite
controlled networks with the specified Gaussian initialization are
captured in probability, uniformly over \(I\), for whole-circle
predictions and the finite observation contract of C.4.7.1.
The proxy and approximation order is the same as in C.4.7.5:
fix accuracy, a finite control partition and its finite program,
then take width to infinity, then remove the fixed approximation.
No finite matrix is subtracted from a population operator.

The theorem permits constants uniform in physical horizon. It does
not assert a probability supremum over a class of controls or
identification for finite-width-dependent feedback controls.
Those feedback passages require the application described in section 8.

## 2. Why control time is a legitimate common parameter

Set \(L_*=10\), reducing it to the actual reference bound if desired.
From (CT4),
\[
 \int_I\sum_j|a_j|\le L_*+q,\qquad
 S:=\int_I\sum_j(|a_j|+|a_{*,j}|)\le2L_*+q.
 \tag{CT8}
\]
The increasing cumulative distribution of (CT5) is continuous.
Where its density is positive, divide each control by that density;
the resulting coefficients \(b_j(s),\bar b_j(s)\) satisfy
\[
 \sum_j(|b_j(s)|+|\bar b_j(s)|)=1
 \quad\hbox{for almost every }s.
 \tag{CT9}
\]
Flat parts carry zero control and zero state change. A generalized
inverse gives the control-clock integral equations, and substitution
in the Lebesgue integral recovers physical time. Equivalently all
formulas can first be proved for step functions and passed in \(L^1\).
This change introduces no optimizer or future state information:
the controls in this theorem are prescribed deterministic functions.

For coefficient arrays define
\[
 m_{kj}=|\gamma_{kj}|+|\bar\gamma_{kj}|,\quad
 m_k=\sum_jm_{kj},\quad
 q_{\rm disc}=\sum_{k,j}|\gamma_{kj}-\bar\gamma_{kj}|.
 \tag{CT10}
\]
Then \(\sum_km_k\le2L_*+q\), \(q_{\rm disc}\le q\), and
\(m_k\le h_0\). A slot with \(m_{kj}=0\) can be omitted or retained
with zero coefficient. For a nonzero slot \(p=(s,j)\), put
\[
 e_p=\frac{|\gamma_p-\bar\gamma_p|}{m_p}\in[0,1],
 \qquad \sum_pm_pe_p=q_{\rm disc}.
 \tag{CT11}
\]
There is no division by a reference coefficient. In particular
(CT11) handles a genuinely new direction, whose reference control
is zero, and vanishing actual controls.

## 3. Exact named-source equations and inactive slots

At each node all active forward calls precede its reverse calls.
Both compared programs use the same training-slot index set.
For a passive current query append one otherwise unused forward and
reverse pair; call its one direct forward slot \(ku\).
Old unused passive queries may be discarded because their values
were never used by an update. Their formal derivatives in every
later state are zero. They do not accumulate a diagonal response
at subsequent times.

With the deterministic controls, contractions, covariances and
response coefficients frozen under named differentiation, the
source equations are
\[
 \begin{aligned}
 w_{k+1}&=w_k+\sum_j\gamma_{kj}
             \phi'(w_k\cdot u_j)Q_{kj}u_j,\\
 c_{k+1}&=c_k+\sum_j\gamma_{kj}\phi(Z^2_{kj}),\\
 K_{k+1}&=K_k+\sum_j\gamma_{kj}\Delta^2_{kj}\otimes H^1_{kj},
 \end{aligned}                                                   \tag{CT12}
\]
\[
 \begin{aligned}
 Z^2_{ku}&=\xi_{ku}+\sum_{p<k}F_{ku,p}\Delta^2_p,&
 F_{ku,p}&=\alpha_{ku,p}
                  +\gamma_p\mathbb E_1[H^1_{ku}H^1_p],\\
 Q_{ku}&=\zeta_{ku}+\sum_{p\le k}D_{ku,p}H^1_p,&
 D_{ku,p}&=\beta_{ku,p}
          +{\bf1}_{p<k}\gamma_p\mathbb E_2[\Delta^2_{ku}\Delta^2_p],
 \end{aligned}                                                   \tag{CT13}
\]
where \(p<k\) means an earlier time index. At the passive current
time the sum has its one distinguished slot; at an active output
all other current beta coefficients are zero. Specifically
\[
 \alpha_{ku,p}=\mathbb E_1[\partial_{\zeta_p}H^1_{ku}],\qquad
 \beta_{ku,p}=\mathbb E_2[\partial_{\xi_p}\Delta^2_{ku}],\qquad
 \beta_{ku,ku}=\mathbb E_2[c_k\phi''(Z^2_{ku})].
 \tag{CT14}
\]
An identical input does not merge its formal current name with an
earlier source. A singular covariance also does not merge those
names.

For lower pulses \(v_{k;p}=\partial_{\zeta_p}w_k\),
\[
 \begin{aligned}
 v_{k+1;p}=v_{k;p}+\sum_j\gamma_{kj}u_j\bigg[
 &\phi''(w_k\cdot u_j)Q_{kj}(u_j\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_j)
 \left({\bf1}_{(k,j)=p}
   +\sum_{q\le k}D_{kj,q}\phi'(w_{t(q)}\cdot u_q)
                                    (u_q\cdot v_{t(q);p})\right)
 \bigg].
 \end{aligned}                                                   \tag{CT15}
\]
For upper pulses,
\[
 \begin{aligned}
 C_{k;p}&=\sum_{q<k}\gamma_q\phi'(Z^2_q)U_{q;p},\\
 U_{ku;p}&={\bf1}_{ku=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^2_{ku})C_{k;p}
                   +c_k\phi''(Z^2_{ku})U_{ku;p}.
 \end{aligned}                                                   \tag{CT16}
\]
These formulas follow directly by differentiating (CT12)–(CT13);
they are also C.4.7.N7–N8 without its residual specialization.
They do not differentiate a residual or any covariance.

If \(\gamma_p=0\), a lower pulse has no injection and remains zero.
An upper pulse at that time can affect its own current \(V\), but
its influence on later states is zero: the update coefficient is
zero and its lower F coefficient into all later queries is zero.
Chronological induction in (CT15)–(CT16) proves this assertion.
Thus retaining arbitrarily many zero slots changes neither the cap
nor the later coefficient rows.

The two programs are realized jointly using the same initialized
arrays and the common source construction III.F. The source
covariances, including cross-program entries, satisfy
\[
 \|\xi_i-\bar\xi_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|H^1_i-\bar H^1_i\|_2,\qquad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|\Delta^2_i-\bar\Delta^2_i\|_2.
 \tag{CT17}
\]
This is subtraction of the two uncentered-input Gram covariances,
not a Lipschitz assertion about matrix square roots. To construct the
joint law one takes the finite union of the two programs.
The scalar expression of either branch depends only on its own
named slots and shared roots; extra calls in the other branch have
zero formal derivatives there. The cross covariances nevertheless
couple the two Gaussian lists. Their entire old source history is
present in (CT13)–(CT17). No source is refreshed at a splice or restart.

## 4. A horizon-independent reference raw anchor

The reference coefficients obey
\(\bar\gamma_{k1}=-\bar\gamma_{k2}\ge0\) and have total mass at most
\(L_*\). Remove zero steps and put \(h_k=2\bar\gamma_{k1}\).
The reference raw program is exactly feature Euler with total
feature length at most \(L_*\); physical pauses have disappeared.

Here is a proof of its uniform raw source cap. This also isolates
the anchor needed below; no nearby-law source estimate enters.
Let \(F'(w)=1/\phi'(w)\), and \(J_X=\phi'(J)\), \(J(0,g)=g\).
Feature clock Euler is
\[
 X_{a,k+1}=X_{a,k}+\tfrac12h_ky_aQ_{ka},\quad
 K_{k+1}=K_k+\tfrac12h_k\sum_ay_a\Delta^2_{ka}\otimes H^1_{ka},
 \quad c_{k+1}=c_k+\tfrac12h_k(H^2_{k1}-H^2_{k2}),
 \tag{CT18}
\]
with \(w_a=J(X_a,g_a)\), \(y_1=1,y_2=-1\).
Direct sums give \(\|c_k\|_\infty\le L_*\) and
\(\|K_k\|_{\rm HS}\le L_*^2/2\), hence a bounded action.
The lower-feature map has clock derivative norm at most one,
including a passive direction:
\[
 H^1(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2)).
 \tag{CT19}
\]
Its derivative in \(X\) has components bounded by \(|u_j|\).

Subtract two clock programs after one fresh pulse.
The forward differences are bounded by the clock difference plus
the HS increment difference. The upper gate subtraction obeys
\[
 \|c\phi'(Z)-\bar c\phi'(\bar Z)\|_2
 \le\|c-\bar c\|_2+2L_*\|Z-\bar Z\|_2.
 \tag{CT20}
\]
Actual adjunction and the rank difference identity give a fixed
Lipschitz constant \(L_{\rm cl}<\infty\) for all three clock
velocities. Thus the post-pulse amplification is at most
\(E_{\rm cl}=e^{L_{\rm cl}L_*}\), uniformly in the mesh.
A reverse-answer pulse at old slot \(p\) changes the clock by at
most \(|\bar\gamma_p|\) times its RMS. A forward-answer pulse
changes its activation and gate, and hence all immediate updates,
by at most \(C|\bar\gamma_p|\) times its RMS. The readout supremum
and action bounds survive the forcing: the readout still updates
by bounded tanh functions and the middle updates have norm bounded
by their control mass times \(L_*\).
Consequently the later passive first-feature response and upper
backward response are at most \(C|\bar\gamma_p|\).

At each fixed graph, add a fresh standard Gaussian \(z\) at that
complete answer with amplitude \(q\), take the fixed-program width
limit first, and pair the observed difference with \(z\).
In its source expression, \(z\) occurs only as
\({\rm slot}+qz\); conditional Gaussian integration by parts yields
\(\mathbb E[zV^q]=q\mathbb E[\partial_{\rm slot}V^q]\).
The unforced output is independent of \(z\).
The fixed-graph source coefficients are continuous at zero forcing:
clip the root, use the bounded clock derivatives, retain the
bounded readout, and remove the clip by the finite causal
covariance-square-root argument in C.4.5.2.R5–R7.
Each fixed graph has a deterministic source-derivative bound
independent of the root clip. Hence its derivative expectations
converge. Taking \(q\to0\) after width gives
\[
 |\alpha^{\rm cl}_{ku,p}|+|\beta^{\rm cl}_{ku,p}|
 \le C|\bar\gamma_p|\quad(p<k),\qquad
 |\beta^{\rm cl}_{ku,ku}|\le2L_*.
 \tag{CT21}
\]
This proves a finite \(B_{\rm cl}\) for all prefixes through \(L_*\),
uniformly over passive queries and covariance rank.

Clock Euler converges to the globally existing reference feature
clock equation on \([0,L_*]\), by its bounded-set Lipschitz
comparison and the direct integral equation. The Gaussian source
isometry and (CT21) pass Gaussian-plus-bounded reverse-query
decompositions to this flow. Thus the actual reference feature flow
has active Gaussian tails on this compact feature segment, even
if its length exceeds the fitting endpoint.

Compare reference raw Euler with that existing flow using the
one-reference gradient cutoff estimate. Their discrepancy is
\(\eta_h\to0\) as the largest feature step tends to zero; only
reference-flow tails enter. Clock Euler has the same property.
Under a temporary cap on preceding raw source rows, transform a
raw first-coordinate step to its clock. Its exact defect is
\[
 R_h(w,b)=F(w+hb\phi'(w))-F(w)-hb
 =h^2b^2\phi'(w)^2
       \int_0^1(1-v)F''(w+vhb\phi'(w))\,dv,
 \tag{CT22}
\]
with \(b=y_aQ_a/2\). The elementary hyperbolic bounds give
\[
 |R_h|\le Ch^2b^2e^{2h|b|},\quad
 |\partial_pR_h|
 \le Ch^2e^{2h|b|}(1+h|b|)
       \{b^2|\partial_pw|+|b||\partial_pb|\}.
 \tag{CT23}
\]
The temporary-cap Gaussian decomposition and pulse estimates in
section 5 give all fixed moments of these factors. At the direct
injection step, division by its mass
\(|\bar\gamma_p|=h_s/2\) leaves a bound \(Ch_s\).
At later steps the normalized pulse is bounded in every fixed
moment. Since \(\sum_kh_k^2\le L_*h_{\max}\), the summed
normalized defect is at most \(C_Bh_{\max}\) in \(L^2\).
The summed undifferentiated defect has the same bound.

For completeness the transformed lower pulse recursion has
deterministic propagation
\[
 \chi_{k+1;p}
 =\chi_{k;p}+\sum_a\bar\gamma_{ka}e_a
 \left({\bf1}_{(k,a)=p}
    +\sum_{q\le k}D_{ka,q}J_q\chi_{t(q);p}\right)
    +\partial_pR_k,
 \tag{CT24}
\]
where \(J_q\) is the bounded clock derivative of its first feature.
Clock Euler has the same equation with the last term zero.
Its normalized pulses are pointwise bounded by
\(C\exp(CB_{\rm cl}L_*)\).
Differences of clock gates are \(O(\eta_h)\) in \(L^2\);
the D-row difference is the beta-row difference plus \(C\eta_h\).
Subtract (CT24), divide by \(|\bar\gamma_p|\), sum its defects,
and apply deterministic discrete Gronwall. Summing the resulting
alpha differences over source masses, and then subtracting the
upper equations (CT16), gives
\[
 E_k\le C_B\left(\eta_h+h_{\max}
                   +\sum_{j<k}h_jE_j\right).
 \tag{CT25}
\]
There is no current unknown on the right. Put \(B=B_{\rm cl}+1\);
choose \(h_{\max}\) so that Gronwall makes \(E_k\le1/2\).
At the first potentially failed raw row the past cap suffices
for (CT23)–(CT25), so that row cannot fail.
This proves a reference raw cap \(B_*<\infty\).
Because this argument is on feature length \(\le L_*\), its
constants do not depend on physical horizon or on pauses.
Extra zero-control directions have no past response, by section 3.

## 5. Temporary-cap moments and control transport

The estimates here are for arbitrary controlled raw programs,
not just the reference. Set \(L=L_*+1\) and restrict \(q\le1\).
The total absolute coefficient mass is at most \(L\).
Directly from (CT12),
\[
 \|c_k\|_\infty\le L,\quad
 \|K_k\|_{\rm HS}\le L^2/2,\quad
 \|A_k\|\le M_0+L^2/2,\quad
 \|w_k\|_2\le\sqrt2+(M_0+L^2/2)L^2/2.
 \tag{CT26}
\]
These bounds do not assume a cap. Under a temporary cap \(B\),
(CT13) gives
\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad
 \mathbb E\zeta_{ku}^2\le L^2,\qquad
 |J_{ku}|\le D_B:=B+L^3.
 \tag{CT27}
\]
For \(Z=\sum_p|\gamma_p||Q_p|\), Jensen and the scalar Gaussian
exponential moment imply
\[
 \mathbb E e^{\lambda Z}
 \le2e^{\lambda LD_B+\lambda^2L^4/2},\qquad\lambda\ge0.
 \tag{CT28}
\]
It follows from (CT15) and \(1+x\le e^x\) that
\[
 \max_{j\le k}|v_{j;p}|
 \le|\gamma_p|\exp(D_BL+2Z).
 \tag{CT29}
\]
Thus all normalized pulses \(v_{\cdot;p}/m_p\) have all fixed
moments, with one common bound. The same holds for the barred
program. In particular
\[
 |\alpha_{ku,p}|\le C_B|\gamma_p|,\qquad
 |F_{ku,p}|\le C_B|\gamma_p|.
 \tag{CT30}
\]
From (CT16), the pointwise sum of the absolute U derivatives is
at most \(e^{C_BL^2}\); the corresponding C and V row sums are
bounded by \(C_B\). For a single old upper pulse, the direct
current V value has size at most \(2L\). Its first later C/F
terms have the factor \(|\gamma_p|\), and the remaining
propagation has total coefficient mass at most \(L\).
Consequently
\[
 |\beta_{ku,p}|\le C_B|\gamma_p|\quad(p<k),\qquad
 \sum_p|V_{ku;p}|+\sum_p|C_{k;p}|+\sum_p|U_{ku;p}|\le C_B.
 \tag{CT31}
\]
The last three bounds are pointwise. The first is deterministic.
These are the single-pulse and row-sum inductions of (CT16);
they do not require a positive lower bound for \(|\gamma_p|\).

Equations (CT27), (CT30), and (CT12) also give all fixed marginal
moments of \(Q,Z^2\) and the time maximum of \(|w|\).
For the latter, use
\(\sup_k|w_k|\le|g|+\sum_p|\gamma_p||Q_p|\).
For \(Z^2\), use its Gaussian source of variance at most one,
(CT30), and \(|\Delta^2|\le L\).
No \(L^p\) operator estimate beyond \(p=2\) is invoked.

### Raw proximity before the source bootstrap

For the two programs on the same mesh let
\(d_k=\|\theta_k-\bar\theta_k\|_{(1)}\), the raw sum norm.
Every \(g_u\) has a common raw norm bound by (CT26).
The same-input gradient comparison is
\[
 \|g_u(\theta)-g_u(\bar\theta)\|_{(1)}
 \le C(1+R)d+C\tau_R(\bar Q(u))
 \tag{CT32}
\]
for \(R\ge L\). The upper gate uses bounded \(\bar c\), and
the only unbounded lower gate multiplier is \(\bar Q\).
This is the explicit split on \(|\bar Q|\le R\) and its
complement, followed by the rank difference identity.

Subtract updates as
\[
 \sum_j(\gamma_{kj}-\bar\gamma_{kj})g_{u_j}(\theta_k)
 +\sum_j\bar\gamma_{kj}
                  [g_{u_j}(\theta_k)-g_{u_j}(\bar\theta_k)].
 \tag{CT33}
\]
Only the second term needs tails, and only its two reference axes
occur. Section 4 therefore gives
\[
 \eta:=\max_kd_k\le\Phi(q_{\rm disc}),\qquad
 \Phi(q)\longrightarrow0\quad(q\downarrow0),
 \tag{CT34}
\]
uniformly in admitted meshes. Explicitly before cutoff choice the
bound is \(Ce^{C(1+R)L_*}(q_{\rm disc}+L_*e^{-cR^2})\).
Choose \(R\) proportional to \(\sqrt{\log(e/q_{\rm disc})}\);
at zero discrepancy both recursions are identical.
This proof uses no nearby-program source cap.

### The weighted beta-row comparison

Define at the same passive output input
\[
 E_k=\sup_u\left(
 |\beta_{ku,ku}-\bar\beta_{ku,ku}|
 +\sum_{p<k}|\beta_{ku,p}-\bar\beta_{ku,p}|\right).
 \tag{CT35}
\]
We prove, under a cap on the preceding rows,
\[
 E_k\le C_B\left(
    \eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\right).
 \tag{CT36}
\]
Every constant in this estimate depends on \(B,L\), not on
physical horizon or the number of source slots.

Here are the complete product and mass estimates. Direct
forward/action subtractions and bounded readouts imply uniformly
at matched inputs
\[
 \|\Delta H^1\|_2+\|\Delta Z^2\|_2
 +\|\Delta\Delta^2\|_2+\|\Delta Q\|_2\le C\eta.
 \tag{CT37}
\]
The \(L^{24}\) bounds just proved, interpolated with (CT37), give
an \(L^{12}\) difference bound \(C_B\eta^{1/11}\) for \(w,Q,Z^2\).
For bounded gates their \(L^2\) difference and pointwise bound give
at least \(C_B\eta^{1/6}\). On \(\eta\le1\) each is bounded by
\(C_B\eta^{1/16}\). The explicit products below require at most
three \(L^{12}\) factors, followed by multiplication by an \(L^4\)
integrating factor. No bound on a maximum of query differences
or a larger-moment interpolation exponent is needed.

The D-row difference has the exact decomposition
\[
 \Delta D_{i,p}=\Delta\beta_{i,p}
 +{\bf1}_{p<i}\left[
   (\gamma_p-\bar\gamma_p)\mathbb E(\bar\Delta^2_i\bar\Delta^2_p)
    +\gamma_p\Delta\mathbb E(\Delta^2_i\Delta^2_p)\right].
 \tag{CT38}
\]
Thus its deterministic row sum is at most
\(E_k+C(q_{\rm disc}+\eta)\).

Subtract (CT15). Its linear propagation of the pulse difference
has coefficient at step \(j\) at most
\[
 D_B\sum_a|\gamma_{ja}|
      +2\sum_a|\gamma_{ja}||Q_{ja}|.
 \tag{CT39}
\]
The product of the resulting amplification factors has all fixed
moments by (CT28). Its forcing consists of exactly:
the direct injection difference \(\gamma_p-\bar\gamma_p\);
update coefficient differences; outside gate differences;
the difference of \(Q\); D-row differences (CT38); and the
inside past-gate differences.
An unchanged normalized barred pulse is bounded by the common
random envelope in (CT29). In the first-gate term, subtract
\(\phi''Qv\) as propagation plus
\((\Delta\phi'')\bar Q\bar v+\phi''(\Delta Q)\bar v\).
In its memory term subtract
\(\phi'\sum D\phi'_qv_q\) into propagation and the three
differences of its outside gate, D, and inside gate.
These exhaust every term.

After division by \(m_p\), the injection cost is \(e_p\).
Coefficient-change costs sum to \(C_Bq_{\rm disc}\), since
every such term is multiplied by \(|\gamma-\bar\gamma|\).
Field/gate costs are bounded by \(C_B\eta^{1/16}\) after
Hölder. For an inside-gate sum, take its \(L^p\) norm by
Minkowski before summing its deterministic D coefficients;
the D-row sum is bounded by \(D_B\).
No maximum of a gate difference over old source slots is taken.
The beta discrepancy cost is
\(C_B\sum_{j<k}m_jE_j\).
Multiplying by the random amplification (CT39) and using
Cauchy–Schwarz proves
\[
 \left\|\frac{\max_{i\le k}|v_{i;p}-\bar v_{i;p}|}{m_p}\right\|_2
 \le C_B\left(e_p+\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT40}
\]
The required product norms use at most a gate difference, a query,
and a normalized pulse. Their \(L^{12}\) bounds give \(L^4\)
forcing; (CT39) has an \(L^4\) bound, giving the asserted \(L^2\)
product. Coefficient-only and D-row terms require fewer factors.

Taking expected first-feature derivatives in (CT40), subtracting
the outside bounded gate, and summing over \(p\), gives
\[
 \sup_u\sum_{p<k}|\alpha_{ku,p}-\bar\alpha_{ku,p}|
 \le C_B\left(\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT41}
\]
Here \(\sum_pm_pe_p=q_{\rm disc}\) and
\(\sum_pm_p\le2L_*+1\). This is precisely where normalization by
the common source mass matters. The F-row difference has the same
bound, by (CT13), (CT37), and coefficient variation.

Set \(G_k=\eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\) and
\[
 W_k=\max_j\left\|\sum_p|V_{kj;p}-\bar V_{kj;p}|\right\|_2.
 \tag{CT42}
\]
The maximum is over output fields only; there is no random
maximum over Gaussian source history. Subtract (CT16):
\[
 \begin{aligned}
 \Delta U_{i;p}
 &=\sum_{q<i}(\Delta F_{i,q})\bar V_{q;p}
                 +\sum_{q<i}F_{i,q}\Delta V_{q;p},\\
 \Delta C_{k;p}
 &=\sum_{q<k}\bigl[
  (\gamma_q-\bar\gamma_q)\phi'(\bar Z_q^2)\bar U_{q;p}
  +\gamma_q\Delta\phi'(Z_q^2)\bar U_{q;p}
  +\gamma_q\phi'(Z_q^2)\Delta U_{q;p}\bigr],\\
 \Delta V_{i;p}
 &=\phi'(Z_i^2)\Delta C_{k;p}
       +\Delta\phi'(Z_i^2)\bar C_{k;p}
       +c_k\phi''(Z_i^2)\Delta U_{i;p}\\
 &\hspace{4mm}
       +\bigl[(c_k-\bar c_k)\phi''(\bar Z_i^2)
                    +c_k\Delta\phi''(Z_i^2)\bigr]\bar U_{i;p}.
 \end{aligned}                                                   \tag{CT43}
\]
The direct current U impulses cancel after pairing the distinguished
slots. Use (CT31)'s pointwise barred row bounds, (CT30)'s density
\(|F_{i,q}|\le C_Bm_q\), the coefficient mass bound, and
(CT37), then sum (CT43) over \(p\) and take \(L^2\).
The first line contributes \(C_BG_k+C_B\sum_{q<i}m_qW_{t(q)}\).
The second contributes its coefficient variation \(C_Bq_{\rm disc}\),
its gate variation \(C_B\eta\), and the same integrated U-row
discrepancy; exchanging two finite sums costs at most the total
mass \(2L_*+1\). The third line contributes \(C_B\eta\) and the
same two row errors. Therefore
\[
 W_k\le C_BG_k+C_B\sum_{j<k}m_jW_j.
 \tag{CT44}
\]
Discrete Gronwall in total mass, and monotonicity of \(G_k\), give
\(W_k\le C_BG_k\). A passive output obeys the same (CT43);
its past terms use the active \(W_j\), so its row difference has
the same bound. Taking expectations proves (CT36).
Its diagonal can also be checked directly from (CT14), with
an \(L^2\) difference at most \(C\eta\).

Everything used for the lower estimates at node \(k\) concerns
earlier Q rows. Its current alpha is then constructed; the upper
equations use only earlier V rows and that alpha.
Current \(Z^2\) moments follow from this new F-row and bounded
\(\Delta^2\), not from a presumed current beta cap.
Thus (CT36) is causal and is valid at the first potentially failed
current beta row.

The row functions extend continuously to all passive directions.
Indeed \(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|
\le C(1+|w|)|u-v|\). Taking expectations against a normalized
lower pulse and using its \(L^2\) bound gives an alpha difference
at most \(C_B|\gamma_p||u-v|\). The contraction term has the
same bound, so the F-row has a summed Lipschitz bound.
In (CT16) the old V rows are unchanged when only the current
passive input varies; the changed F-row and the \(L^2\)-Lipschitz
current upper gates, multiplied by the pointwise old derivative
row bounds, give a beta-row Lipschitz estimate.
Thus a dense countable set of passive inputs suffices for the
common construction, with the asserted supremum supplied by
continuity. This makes no continuity claim for a random
supremum of Gaussian queries.

## 6. Closing the uniform cap

Choose \(B=B_*+1\), where section 4 supplied the reference raw cap.
At every preceding prefix satisfying that cap, (CT34) and (CT36)
give
\[
 E_k\le C_B e^{C_B(2L_*+1)}
                      \bigl(\Phi(q)^{1/16}+q\bigr).
 \tag{CT45}
\]
Choose \(\delta>0\) small enough that this is at most \(1/2\)
for \(q\le\delta\). The zero initial readout gives zero initial
beta rows. At the first potential failure the current row is
at most \(B_*+1/2<B\), a contradiction. This proves the
coefficient assertion of (CT7), including every old source slot.

Equation (CT27) then gives Gaussian tails: for \(R\ge2D_B\),
\(|Q|>R\) implies \(|\zeta|>R/2\), and integrating the scalar
Gaussian tail bounds
\(\mathbb E[(|\zeta|+D_B)^2{\bf1}_{|\zeta|>R/2}]\)
by \(Ce^{-cR^2}\). Taking a square root and reducing \(c\)
gives (CT7); enlarge \(M\) for \(1\le R<2D_B\) and for the
bounded readout. No independence of the bounded remainder and
the Gaussian part is needed.

## 7. Strong completion and finite controlled capture

For one fixed pair of controls, work on its compact control interval
\([0,S]\). At a partition node use the exact integrated coefficients.
Between nodes use the integral interpolation
\[
 \theta^\pi(s)=\theta^\pi(s_k)+
      \int_{s_k}^s\sum_j b_j(v)g_{u_j}(\theta^\pi(s_k))\,dv.
 \tag{CT46}
\]
Its speed is bounded uniformly by (CT9), (CT26), and (CT1).
It differs from its preceding node by at most \(C|\pi|\).
An intermediate state is also one more raw Euler update using the
partial integrated coefficients, so the same source cap applies.

For two partitions, compare their assigned velocities using
(CT32), the common controls, and the reference tails of either
controlled Euler path now proved in (CT7).
The integrated discrepancy on \([0,S]\) is bounded by
\[
 Ce^{C(1+R)S}
      \{(1+R)(|\pi|+|\pi'|)+e^{-cR^2}\}.
 \tag{CT47}
\]
Take the mesh sizes to zero at fixed \(R\), then take
\(R\to\infty\). The paths are Cauchy in the complete raw path
space. The gradient maps \(g_u\) are continuous in raw state,
uniformly over the compact circle, by bounded multiplier
continuity and rank subtractions. Dominated convergence using
(CT9) passes (CT46) to (CT3)'s integral equation.
This gives a strong absolutely continuous solution.

Positive-part cutoff convergence transfers (CT7) to that solution.
For uniqueness against an arbitrary strong solution, the path
range on the compact control interval is bounded. Apply (CT32)
with the constructed solution as the only tail-bearing endpoint.
At zero initial discrepancy (CT47) with zero mesh term gives
zero after sending \(R\to\infty\). The same argument on any
remaining subinterval gives reached uniqueness. Reached
existence is the restriction of the constructed path, retaining
its actual current state and all initialized primitives.
For \(T=\infty\), compact control time supplies the endpoint;
no new existence theorem at an arbitrary raw state is inferred.

At finite width, the controlled equation is a Carathéodory ODE:
the coefficients are measurable and integrable, while its
parameter vector fields are smooth. Contraction in control time
gives local existence and uniqueness. On the initialization event
\(\|A_{0,n}\|\le10\), first-row RMS at most 2, and initial
readout supremum at most 1, the elementary controlled bounds are
\[
 \|c_n\|_\infty\le1+L,\qquad
 \|K_n\|_F\le L+L^2/2.
 \tag{CT48}
\]
The first-row displacement is bounded by the same finite action
bound times \(L+L^2/2\). Thus no finite control-time blowup occurs.
For each individual initialized finite network the same reasoning
uses its finite initial norms and proves existence.

Fix a finite control partition. Its population program has
finitely many instructions and deterministic integrated controls.
Realize it on the actual finite initialized arrays, expanding K
into its finite ranks. Keep the actual initial readout additively
in the proxy parameters. III.F.1–7 and A.1–A.2 identify the joint
node laws, second moments and both action orientations.
The rank Gram contractions identify the HS/Frobenius increment
metric. Recomputed proxy gradients differ from assigned oracle
gradients by \(o_{\mathbb P}(1)\); bounded gates times fixed
oracle \(L^2\) fields are handled by cutoff and then second-moment
convergence. Positive-part cutoffs transfer (CT7) at its finitely
many nodes to finite RMS tails, up to \(o_{\mathbb P}(1)\).

Compare actual controlled finite flow to the proxy using the
same controls. Equations (CT32), (CT48), and the interpolation
speed give the bound (CT47), with one additional
\(o_{\mathbb P}(1)\), at fixed partition and cutoff.
Because total control time is bounded independently of \(T\),
the constants in this comparison are uniform in physical
horizon. Choose the Gaussian cutoff first, then a fine fixed
partition, then take width to infinity. This yields arbitrarily
small same-carrier raw error to a fixed population proxy.
Passive input and control-time nets give whole-circle uniform
prediction capture. Bounded actions, Lipschitz coordinate
operations, and fixed bounded gates applied to named \(L^2\)
fields preserve the approximation by the finite induction of
C.4.7.5. This supplies its stated observation contract and paired
hidden measurements. There is no assertion about arbitrary
unbounded observation products.

This completes the controlled source-tube theorem.

## 8. Scope of the application to the mixture

The source estimate itself now has a horizon-independent radius.
It is conditional only on the explicit deterministic integrated
control neighborhood (CT4), not on a tail or Gram hypothesis.
It is strong enough to anchor prefixes arbitrarily near the
fitted endpoint while retaining their entire Gaussian history.

For an already constructed deterministic population mixture flow,
its actual residual controls are deterministic, so the theorem
can be applied to their realized scalar functions after proving
(CT4). For example the coordinator's proposed Gram estimate
\(M\ge\kappa I\) gives, on a bounded stopped segment,
\[
 \int_b^t|r(s)|\,ds\le C|r(b)|+C\epsilon(t-b).
 \tag{CT49}
\]
The actual added control mass is at most
\(C\epsilon(t-b)\). The reference tail after b has mass tending
to zero as \(b\to\infty\). A fixed large b followed by a fixed
small slow-time interval \(\epsilon(t-b)\le\tau_0\) is therefore
consistent with (CT4). But (CT49), the stopping argument that
keeps the Gram positive, and existence of the endogenous-control
flow must be proved together; this file does not assume them.

There is also a finite-network distinction. Finite GF residual
controls are random and width dependent. The fixed deterministic
control theorem cannot simply be applied as a uniform probability
statement to those controls. A legitimate GF identification uses
the deterministic population Euler proxy, retains finite GF's
own residuals in the actual vector field, and compares them
directly. That comparison must exploit control-time estimates
or the stabilized reference residual equations so that its
constants do not reintroduce an uncontrolled physical factor
\(\exp(CT_\epsilon)\). For each fixed positive epsilon the horizon
is finite, so ordinary one-reference comparison with the
constructed population path and its now proved Gaussian tails
does give width-first capture; no uniform epsilon-width rate
follows. The remaining population-feedback construction is an
application obligation, separate from the proved source cap.

No endpoint Gram positivity, constrained slow-flow existence,
positive added-risk gain, or hidden-activity margin is asserted
in this file. Those are independent tasks. The theorem closes
the proposed deterministic integrated-control source estimate,
including its complete-history, zero-slot and passive-query issues.

## 9. Checks, provenance, and frozen inputs

The main attacks checked were:

- New controls with zero reference mass: handled by \(m_p\) and
  the identity \(\sum m_pe_p=q_{\rm disc}\), never a reference
  mass inverse.
- Arbitrarily many old or zero slots: all old sums retain their
  injection masses; inactive passive evaluations have no
  descendants. Only one distinguished current diagonal occurs.
- Singular cross-program covariance: handled by the covariance
  isometry (CT17) on the joint fixed-program realization.
- Circular current-query assumptions: the cap argument constructs
  lower derivatives and current alpha before current beta.
- Physical-time blowup of constants: all amplification sums use
  total coefficient mass bounded by \(2L_*+1\).
- Missing higher-moment action bounds: moments come from named
  source decompositions and finite pulse equations.
- Random finite feedback: explicitly excluded from a probability
  supremum and separated in section 8.
- A mere endpoint replacing existence: strong completion is by
  uniform Euler source tails and (CT47), not energy alone.

Scientific inputs read in the first round remain available with
their exact coverage recorded in ROUTE_CONTINUATION.md.
The second round additionally read the complete coordinator
ROUTE_RESIDUAL_CLOCK.md. No other study, other route, or task
history was read. No training experiment or Git mutation occurred.
Only this assigned new report was edited. Shared HEAD/index were
checked as metadata before writing.

SHA-256 values checked before this derivation:

| Input | SHA-256 |
|---|---|
| Frozen ROUTE_CONTINUATION.md | 7f33067ed4715f53fb1f14d39a9a7b07865178519c4bdef0a344048104225a13 |
| ROUTE_RESIDUAL_CLOCK.md | 6cb2b1dfb815aa2c579a4e85f4ece77c713e2bcacfa19ee5bf9c7133455a0c9d |
| docs/global_nonlinear.md | bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |

Observed HEAD: abab5537b4a248ada7fde7164c60a56fb864e881.
This is a theoretical candidate with no numerical training claim.
