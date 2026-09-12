#### C.4.9. Nonlinear prediction selection during a finite added-data episode

This result concerns the whole-circle prediction selected by actual nonlinear
training after a fixed amount of learning from a component whose mixture weight
vanishes. The physical training law is unchanged throughout each run. The
limiting episode is a constrained gradient flow with evolving hidden features;
its initialization is the established fitted reference state, obtained from
the original initialization by a justified initial-layer limit.

##### Model, determining equation and theorem

Use the canonical bias-free network with two tanh hidden layers,

\[
 u=x/\sqrt2\in S^1,\quad h^1_n=\tanh(W^1_nu),\quad
 h^2_n=\tanh(W^2_nh^1_n),\quad f_n=(W^3_n)^Th^2_n/n.
\]

Initialize every entry and block independently, centered Gaussian with stored
variances \((1,1/n,1/n^2)\). Use mobilities \((n,1,n)\), the unhalved mean square,
and physical gradient flow. Keep the actual finite initial Gaussian readout.
Set

\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
             +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\epsilon,\alpha,y}=(1-\epsilon)\nu_*+\epsilon\nu_{\alpha,y},
\]
\[
 \nu_{\alpha,y}=\delta_{(\sqrt2u_\alpha,y)},\quad
 u_\alpha=(\cos\alpha,\sin\alpha),\quad
 |\alpha-\pi/4|\le1/1216,\quad 3/8\le y\le5/8.
 \tag{NS1}
\]

This fixed compact parameter rectangle has nonempty interior in location and
label. All its added inputs are nonorthogonal to both reference inputs. Its
labels are admitted for every fixed \(Y\ge1\). All actual mixture flows begin
at the original Gaussian initialization and use that same mixture throughout.

Let \(H_1=L^2(\Omega_1)\) and \(H_2=L^2(\Omega_2)\) be the canonical generated
Gaussian action spaces, with initialized action \(A_0:H_1\to H_2\) and its true
Hilbert adjoint. Their construction is by the joint Gaussian finite-program
law, including the response to every reused forward and transpose call.
The raw state is \(\theta=(w,K,c)\), where
\(w\in L^2(\Omega_1;\mathbb R^2)\), \(K:H_1\to H_2\) is Hilbert–Schmidt,
\(c\in H_2\), and \(A=A_0+K\). Only the increment is Hilbert–Schmidt.
Use the squared metric \(\|\Delta w\|_2^2+\|\Delta K\|_{HS}^2+\|\Delta c\|_2^2\).

The established reference endpoint \(\theta_\dagger\) is explicitly determined
from \((g,A_0,0)\), \(g\sim N(0,I_2)\), by the reference feature equation:
write \(\phi=\tanh\), \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\),
\(\delta(u)=c\phi'(AH^1(u))\), and \(Q(u)=A^*\delta(u)\). Starting at
\((w,K,c)=(g,0,0)\), solve

\[
 \partial_s w={1\over2}\sum_{a=1}^2 y_a\phi'(w\cdot e_a)Q(e_a)e_a,
 \quad \partial_sK={1\over2}\sum_{a=1}^2y_a\delta(e_a)\otimes H^1(e_a),
 \quad \partial_sc={1\over2}\sum_{a=1}^2y_aH^2(e_a),
\]

where \(y_1=1,y_2=-1\), and stop at the unique first \(s=s_\dagger\le10\)
with \(\langle c,(H^2(e_1)-H^2(e_2))/2\rangle=1\). The global clock construction
in C.4.5 proves well-posedness of this prescription and identifies it with the
physical reference endpoint. Put \(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\).
The zero readout in this population initialization is the limit of the actual
finite readout and imposes no finite-network reset.

For every state used below, define its current raw prediction gradient

\[
 g_\theta(u)=\left(
   \phi'(w\cdot u)Q(u)u,\quad \delta(u)\otimes H^1(u),\quad H^2(u)
                    \right),
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NS2}
\]

The inverse exists throughout the asserted episode. The determining evolution
and reconstruction are

\[
 {d\bar\theta_{\alpha,y}\over d\tau}
   =-2\big(f_{\bar\theta_{\alpha,y}}(u_\alpha)-y\big)
                  \Pi_{\bar\theta_{\alpha,y}}g_{\bar\theta_{\alpha,y}}(u_\alpha),
 \qquad \bar\theta_{\alpha,y}(0)=\theta_\dagger,
 \tag{NS3}
\]
\[
 P_{\alpha,y}(\tau,\sqrt2u)
   =\left\langle\bar c(\tau),
      \tanh\big((A_0+\bar K(\tau))\tanh(\bar w(\tau)\cdot u)\big)\right\rangle.
 \tag{NS4}
\]

Every coefficient in (NS3) is computed from the specified current state and
the established initialized action. In particular its projection and all
hidden features are recomputed along the evolution. There is no coefficient
supplied by an unknown changed-law trajectory.

**Theorem.** There exist \(\epsilon_0,\tau_0,a,j>0\), uniform over the parameter
rectangle (NS1), with these properties.

1. Equation (NS3) has a unique strong solution on \([0,\tau_0]\) in a fixed
   neighborhood of \(\theta_\dagger\). It is constructed on the canonical
   initialized carrier with its full retained reference history. It preserves
   the two reference predictions exactly. It determines (NS4) over the whole
   circle.

2. For every \(0<\epsilon<\epsilon_0\), the original-initialization mixture
   population GF exists and is unique through \(T_\epsilon=\tau_0/\epsilon\).
   For every \(0<\tau_-<\tau_0\),
   \[
    \sup_{(\alpha,y)}\sup_{\tau_-\le\tau\le\tau_0}
      \|\theta_{\mu_{\epsilon,\alpha,y}}(\tau/\epsilon)
                    -\bar\theta_{\alpha,y}(\tau)\|_{\rm raw}\longrightarrow0.
    \tag{NS5}
   \]
   The same convergence holds for predictions uniformly over the entire
   circle and for the finite named hidden observations stated below.
   The exclusion of \(\tau=0\) records the genuine initial layer; no pretraining
   stage is imposed on any actual run.

3. With \(R_\nu(f)=\int(f(x)-y)^2\,d\nu(x,y)\), the selected finite-episode
   prediction satisfies
   \[
      R_{\nu_{\alpha,y}}(F_*)
       -R_{\nu_{\alpha,y}}(P_{\alpha,y}(\tau_0))\ge a.
    \tag{NS6}
   \]
   This is risk on the added component itself, without its factor \(\epsilon\).
   For \((v_1,v_2,v_3)=(e_1,e_2,u_\alpha)\), its paired upper-hidden change is
   \[
    {1\over3}\sum_{i=1}^3
      \|H^2_{\bar\theta_{\alpha,y}(\tau_0)}(v_i)
                         -H^2_{\theta_\dagger}(v_i)\|_2^2\ge j.
    \tag{NS7}
   \]
   Both states use the same initialized primitives. The hidden displacement
   therefore measures adaptation caused by the added law after reference fitting.

4. For every separately fixed \(\epsilon\in(0,\epsilon_0)\) and law in (NS1),
   actual finite GF converges in probability to the mixture population
   prediction in \(C([0,T_\epsilon]\times\sqrt2S^1)\), with the joint
   same-layer internal observations needed for paired hidden measurements.
   Consequently, for every such fixed law and every \(\eta>0\),
   \[
    \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
     \Pr\!\left\{\sup_x|f_{n,\mu_\epsilon}(T_\epsilon,x)
                       -P_{\alpha,y}(\tau_0,x)|>\eta\right\}=0.
    \tag{NS8}
   \]
   Train a reference network with the same initial arrays, including readout,
   and define the directly paired finite observable
   \[
    J_{2,n,\epsilon}={1\over3n}\sum_{i=1}^3
      \|h^2_{n,\mu_\epsilon}(T_\epsilon,\sqrt2v_i)
                    -h^2_{n,\nu_*}(T_\epsilon,\sqrt2v_i)\|_2^2.
    \tag{NS9}
   \]
   In the same iterated order it converges in probability to (NS7)'s
   population quantity. In particular the probability that the added-risk
   gain is at least \(a/2\) and \(J_{2,n,\epsilon}\ge j/2\) tends to one.

The constants need not be numerically practical. The theorem asserts one fixed,
nonzero slow-time episode, not a final endpoint for the changed law. It gives
no simultaneous width/contamination rate and no raw-GD extension. The scale
\(\tau=\epsilon t\) follows from the stable reference-residual equations and
the remaining tangential force, as proved below.

##### Proof architecture

The proof first establishes a Gaussian source bound for a small perturbation
of the reference in integrated control mass, uniformly in physical horizon.
A protected Gaussian-row argument then proves strict endpoint conditioning.
Together these facts construct (NS3) and continue the actual mixture through
(NS5). An exact residual identity proves selection on the slow clock.
A fixed-readout hidden contrast and the exact risk derivative yield (NS6)–(NS7).
Finally a same-array, one-reference cutoff comparison identifies actual finite
GF and the paired observations in (NS8)–(NS9).

Equation labels and auxiliary constants are local to each proof unit below.
All finite vector norms are ordinary Euclidean norms; normalization factors
are displayed in the finite-state metric.


##### Proof unit A. Uniform source control in accumulated training force

###### A.1. Statement with the exact control and approximation conventions

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
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),
\]
\[
 g_u(\theta)=
 \bigl(\phi'(w\cdot u)Q(u)u,\,
       \Delta^{(2)}(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad\phi=\tanh.
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

The assertion here is a finite-program source bound. Proof unit C constructs
the required strong nonlinear trajectories from these bounds; proof unit D
identifies actual finite GF. No probability supremum over random finite-network
feedback controls is asserted by this source estimate.

###### A.2. Why control time is a legitimate common parameter

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

###### A.3. Exact named-source equations and inactive slots

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
 K_{k+1}&=K_k+\sum_j\gamma_{kj}\Delta^{(2)}_{kj}\otimes H^1_{kj},
 \end{aligned}                                                   \tag{CT12}
\]
\[
 \begin{aligned}
 Z^2_{ku}&=\xi_{ku}+\sum_{p<k}F_{ku,p}\Delta^{(2)}_p,&
 F_{ku,p}&=\alpha_{ku,p}
                  +\gamma_p\mathbb E_1[H^1_{ku}H^1_p],\\
 Q_{ku}&=\zeta_{ku}+\sum_{p\le k}D_{ku,p}H^1_p,&
 D_{ku,p}&=\beta_{ku,p}
          +{\bf1}_{p<k}\gamma_p\mathbb E_2[\Delta^{(2)}_{ku}\Delta^{(2)}_p],
 \end{aligned}                                                   \tag{CT13}
\]
where \(p<k\) means an earlier time index. At the passive current
time the sum has its one distinguished slot; at an active output
all other current beta coefficients are zero. Specifically
\[
 \alpha_{ku,p}=\mathbb E_1[\partial_{\zeta_p}H^1_{ku}],\qquad
 \beta_{ku,p}=\mathbb E_2[\partial_{\xi_p}\Delta^{(2)}_{ku}],\qquad
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
 =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.
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

###### A.4. A horizon-independent reference raw anchor

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
 K_{k+1}=K_k+\tfrac12h_k\sum_ay_a\Delta^{(2)}_{ka}\otimes H^1_{ka},
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

###### A.5. Temporary-cap moments and control transport

The estimates here are for arbitrary controlled raw programs,
not just the reference. Set \(M_0=\|A_0\|\le2\), \(L=L_*+1\), and restrict \(q\le1\).
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
(CT30), and \(|\Delta^{(2)}|\le L\).
No \(L^p\) operator estimate beyond \(p=2\) is invoked.

**Raw proximity before the source bootstrap**

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

**The weighted beta-row comparison**

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
 \|\mathrm d H^1\|_2+\|\mathrm d Z^2\|_2
 +\|\mathrm d\Delta^{(2)}\|_2+\|\mathrm d Q\|_2\le C\eta.
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
 \mathrm d D_{i,p}=\Delta\beta_{i,p}
 +{\bf1}_{p<i}\left[
   (\gamma_p-\bar\gamma_p)\mathbb E(\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p)
    +\gamma_p\Delta\mathbb E(\Delta^{(2)}_i\Delta^{(2)}_p)\right].
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
\((\mathrm d\phi'')\bar Q\bar v+\phi''(\mathrm d Q)\bar v\).
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
 \mathrm d U_{i;p}
 &=\sum_{q<i}(\mathrm d F_{i,q})\bar V_{q;p}
                 +\sum_{q<i}F_{i,q}\mathrm d V_{q;p},\\
 \mathrm d C_{k;p}
 &=\sum_{q<k}\bigl[
  (\gamma_q-\bar\gamma_q)\phi'(\bar Z_q^2)\bar U_{q;p}
  +\gamma_q\mathrm d\phi'(Z_q^2)\bar U_{q;p}
  +\gamma_q\phi'(Z_q^2)\mathrm d U_{q;p}\bigr],\\
 \mathrm d V_{i;p}
 &=\phi'(Z_i^2)\mathrm d C_{k;p}
       +\mathrm d\phi'(Z_i^2)\bar C_{k;p}
       +c_k\phi''(Z_i^2)\mathrm d U_{i;p}\\
 &\hspace{4mm}
       +\bigl[(c_k-\bar c_k)\phi''(\bar Z_i^2)
                    +c_k\mathrm d\phi''(Z_i^2)\bigr]\bar U_{i;p}.
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
\(\Delta^{(2)}\), not from a presumed current beta cap.
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

###### A.6. Closing the uniform cap

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

Here \(\mathrm d X=X-\bar X\) denotes a comparison difference;
\(\Delta^{(2)}\) is the typed upper backward field.


###### A-supplement.4. Named-coefficient continuity in the reference raw anchor

The reference anchor (CT21)–(CT25) uses three different limits.
Their order matters:

- At a fixed clock Euler graph and nonzero fresh forcing,
  width tends to infinity.
- At that fixed graph the forcing tends to zero, after
  establishing continuity of its named coefficient.
- Only after a mesh-uniform coefficient bound has been
  proved is the clock/raw Euler mesh refined.

There is no assertion that zero-forcing continuity is uniform
over a growing graph. The finite pulse norm bound is uniform
in the mesh, which is the property used to obtain the final cap.

For the first limit, smoothly clip the Gaussian first roots
and use an inactive smooth readout clip equal to identity on
a neighborhood of the deterministic readout interval.
The clock coordinate map \(J(X,g)\) obeys
\[
 J_X=\phi'(J),\qquad
 J_g=\frac{\phi'(J)}{\phi'(g)}.
 \tag{A9}
\]
After clipping g both derivatives are bounded at each fixed
clip level. The passive first feature is
\(\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), whose source-relevant
X derivatives are bounded independently of the root clip.
Thus the contained finite Gaussian program and its source rule
apply to the clipped forced and unforced graphs.

At any fixed graph, all named source derivatives have a finite
deterministic envelope while previous selected coefficients
remain in a compact set. This follows inductively:
the lower clock feature derivatives are bounded, the upper
tanh derivatives are bounded, the readout is bounded by total
feature length, and each action answer is its source plus a
finite linear combination with fixed coefficients.
Root derivatives are never taken in this induction.

Now remove the root clip chronologically. Earlier second
moments converge, so the next finite covariance matrix
converges. Its nonnegative square root converges even at rank
loss, by bounded subsequences and uniqueness of a nonnegative
square root. Couple on a common finite standard Gaussian list.
Node values and source derivatives converge in probability.
The deterministic derivative envelope gives uniform
integrability of derivatives, so their expectations converge.
The same argument is uniform over forcing amplitudes in a
fixed compact interval at this fixed graph. In particular it
proves coefficient continuity at zero forcing.
This is the complete continuity mechanism used by
C.4.5.2.R5–R7, not continuity of a pseudoinverse.

The fresh root z remains independent of all centered source
groups in the scalar construction. The latter's selected
covariances may depend on forcing amplitude q, but are
deterministic and frozen under differentiation. The only
local root insertion is \({\rm slot}+qz\), so
\[
 \partial_zV^q=q\,\partial_{\rm slot}V^q,\qquad
 \mathbb E[zV^q]=q\,\mathbb E[\partial_{\rm slot}V^q].
 \tag{A10}
\]
This validates the source extraction even for a zero-variance
or duplicated source slot. The unforced value law alone would
not determine such a transverse derivative.

For the raw-to-clock step, transformed raw variables
\(F(w)\) are an analysis device, not extra instructions to
which the at-most-linear value theorem is applied.
At a fixed raw graph each \(w\) has a linear envelope in the
finite Gaussian root/source list; its named derivatives have
polynomial envelopes. Multiplication by \(F'(w)=\cosh^2w\)
therefore has finite moments at that fixed graph.
The uniform defect estimate CT23 is stronger: after cancellation
its only exponential is \(e^{2h|b|}\), with a capped Gaussian
query b. CT28–CT29 give its required fixed moments uniformly
over all prefixes under the temporary cap.
The direct injection step has size \(h_s\), so dividing its
defect by \(|\bar\gamma_p|=h_s/2\) leaves \(O(h_s)\).
All later defect sums use
\(\sum_kh_k^2\le L_*h_{\max}\).

The source comparison CT24–CT25 then uses only:
bounded clock gates, the deterministic clock-pulse envelope,
the raw/clock raw-state difference, D-row coefficient
differences, and the summed normalized defect.
The current alpha is obtained before current beta; its
right side uses only old raw Q rows. Thus the cap bootstrap
does not assume its current conclusion.

The contained III.F source/regularization proof and C.4.5.2 clipping/forcing
argument supply these fixed-graph constructions. No all-orders jet theorem
or uniform derivative convergence of finite GF is needed for this anchor.

##### Proof unit B. Endpoint conditioning and finite nonlinear learning

For the activity implication in this unit, let \(\tau_{ex}>0\) be a common
existence interval for (NS3); proof unit C constructs it. The endpoint
conditioning and continuity estimates do not assume that existence.

###### B.2. Endpoint conditioning, with a complete proof

The supplied C.4.5–C.4.6 facts used here are

\[
 \|A_\dagger\|\le M:=2+\sqrt{10},\quad
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad
 \|c_\dagger\|_\infty\le H:=10,\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{2.1}
\]

The endpoint predictor is 76-Lipschitz, vanishes at
`(e1+e2)/sqrt(2)`, and fits `(1,-1)`. Thus, on (NS1),

\[
 |f_\dagger(u_\alpha)|\le76/1216=1/16,
 \qquad 5/16\le y-f_\dagger(u_\alpha)\le11/16.
 \tag{2.2}
\]

In particular the added-law endpoint risk is at least `25/256`, even though
its contribution to the mixture risk is only `epsilon` times that number.

C.4.6.S40–S44 supplies one nonnegative random envelope `N`, with finite
`C_*`, such that on the reference feature segment

\[
 \|N\|_p\le C_*\sqrt p\ (p\ge2),\quad
 \sup_s|X_a(s)|\le5N,\quad
 F(w_a(s))=F(g_a)+X_a(s),\quad F'(z)=\cosh^2z,
 \tag{2.3}
\]

where `g1,g2` are independent standard normals. It also gives
`||Q_dagger(u)||_4<=L4:=2C_*` uniformly over every deterministic circle
input. Its countable-source construction and Fubini supply the simultaneous
active-clock bounds in (2.3). Independence of `N` and `g` is not asserted.

Here is the endpoint first-feature independence argument in full. Fix
`v in R2` with nonzero coordinates. Markov's inequality with
`p=(R/(eC_*))^2>=2` gives

\[
 \Pr(N>R)\le\exp[-R^2/(e^2C_*^2)].
\]

The Gaussian density gives

\[
 \Pr\{|g-rv|_\infty\le1\}
    \ge {2\over\pi}\exp[-(r|v|+\sqrt2)^2/2].
\]

For all sufficiently large `r` this exceeds `Pr(N>r^2)`, so their box
intersected with `{N<=r^2}` has positive probability. On that event put
`rho=min(|v1|,|v2|)/2`; for large `r`, `|g_a|>=rho r`. The minimum of
`F'` on `[g_a-1,g_a+1]` is at least `exp(2(|g_a|-1))/4>5r^2`.
Monotonicity of `F` in (2.3) therefore gives

\[
 \sup_s|w_a(s)-g_a|
    \le20r^2e^{-2(|g_a|-1)}\le20e^2r^2e^{-2\rho r}\longrightarrow0.
 \tag{2.4}
\]

If a finite nonantipodal list `u1,...,um` satisfied
`sum a_j tanh(w_dagger.u_j)=0` almost surely, choose such a `v` also
avoiding all lines `v.u_j=0`. On the preceding positive-probability events,
the features tend uniformly to `sign(v.u_j)`. Hence

\[
                   \sum_j a_j\operatorname{sign}(v\cdot u_j)=0.
 \tag{2.5}
\]

Cross the line perpendicular to any `u_k` on the circle of `v` directions.
The nonantipodal condition means no other sign changes there. Choose points
on both sides with nonzero coordinates, also when the crossing is on an axis.
Subtracting (2.5) gives `2a_k=0` up to orientation. Thus all `a_k=0`.
The features are linearly independent.

At the endpoint define

\[
 H^1(u)=\tanh(w_\dagger\cdot u),\quad Z^2(u)=A_\dagger H^1(u),
 \quad H^2(u)=\tanh Z^2(u),\quad
 \delta(u)=c_\dagger\operatorname{sech}^2Z^2(u),\quad
 Q(u)=A_\dagger^*\delta(u).
\]

The readout is nonzero since `<c_dagger,H2(e1)>=1`. Because `Z2(u)`
is finite almost surely and its gate is strictly positive, every `delta(u)`
is nonzero in L2. The raw gradient, at this or any admissible state, is

\[
 g_\theta(u)=\big(u\operatorname{sech}^2(w\cdot u)Q(u),
                    \delta(u)\otimes H^1(u),\ H^2(u)\big).
 \tag{2.6}
\]

For a finite list, if `lambda_H` is its first-feature Gram minimum eigenvalue,
then

\[
 \left\|\sum_i a_i\delta_i\otimes H_i^1\right\|_{HS}^2
    \ge\lambda_H\sum_i a_i^2\|\delta_i\|_2^2.
 \tag{2.7}
\]

Indeed at each second-layer coordinate apply the first-feature Gram
inequality to `sum_i a_i delta_i(omega2)H_i^1` and integrate. This also
identifies the integral with the tensor's Hilbert–Schmidt norm. Thus the
middle gradient blocks, hidden gradient blocks and full gradients are
independent. No injectivity of the trained action is assumed.

The first-feature Gram is continuous in the input list by the L2 Lipschitz
bound for tanh. The fields `delta(u)` are L2-continuous: first pass input
continuity through `w_dagger`, tanh and the bounded action, then use the
bounded fixed readout in (2.1). Their nonzero L2 norms therefore have a
positive minimum on the present compact input set. Define

\[
 \kappa:=\min_{\alpha\in I}\lambda_{\min}
     \big(\langle H^1(v_i),H^1(v_j)\rangle\big)_{i,j=1}^3
       \ \min_{\alpha\in I,\,i\le3}\|\delta(v_i)\|_2^2>0.
 \tag{2.8}
\]

Continuity of the minimum eigenvalue follows from the Rayleigh formula,
`|lambda_min(B)-lambda_min(D)|<=||B-D||`; a continuous positive function
on a compact set has positive minimum. This proves every positivity step
in (2.8). It is a precisely defined endpoint constant, not an evaluated
numerical lower bound.

Consequently the endpoint three-input middle Gram is at least `kappa I`.
The full anchor Gram `M_dagger` is at least `kappa I`. Let

\[
 d_\alpha=\Pi_\dagger g_\dagger(u_\alpha),\quad
 \beta_\alpha=M_\dagger^{-1}G_\dagger^*g_\dagger(u_\alpha),\quad
 t_\alpha=(-\beta_{\alpha,1},-\beta_{\alpha,2},1).
 \tag{2.9}
\]

Since `d=sum_i t_i g_dagger(v_i)` and `|t|>=1`, (2.7) implies

\[
 \|d_\alpha\|^2\ge\|d_{\alpha,H}\|^2
       \ge\|d_{\alpha,K}\|_{HS}^2\ge\kappa.
 \tag{2.10}
\]

The hidden block `H` consists of the first row and middle increment; the
`K` subscript means only the middle increment. The upper gradient bound is

\[
 \|g_\dagger(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17.
\]

Therefore `||d_alpha||<=L0`, `||G_dagger||<=G0:=sqrt(2)L0`, and

\[
 |t_\alpha|\le T_0:=\sqrt{1+2L_0^4/\kappa^2}.
 \tag{2.11}
\]

###### B.3. Quantitative gradient continuity from raw distance and endpoint L4 tails

This paragraph verifies input continuity and state continuity together. Put
`d=||theta-theta_dagger||_raw`, `h=|u-v|`, `rho=d+h<=1`. Here `A-A_dagger`
is measured in HS norm, hence also bounded in operator norm. Use endpoint
quantities at `v` as fixed factors. Successive subtraction gives

\[
 \|Z^1_\theta(u)-Z^1_\dagger(v)\|_2\le a_1\rho,
 \quad\|H^1_\theta(u)-H^1_\dagger(v)\|_2\le a_1\rho,
 \quad a_1=1+W,
\]

\[
 \|Z^2_\theta(u)-Z^2_\dagger(v)\|_2,
 \ \|H^2_\theta(u)-H^2_\dagger(v)\|_2\le a_2\rho,
 \quad a_2=1+Ma_1,
\]

\[
 \|\delta_\theta(u)-\delta_\dagger(v)\|_2\le a_\delta\rho,
 \quad a_\delta=1+2Ha_2,
\]

\[
 \|Q_\theta(u)-Q_\dagger(v)\|_2\le a_Q\rho,
 \quad a_Q=C+1+Ma_\delta.
 \tag{3.1}
\]

For the backward product split it as
`(c-c_dagger)phi'(Ztheta)+c_dagger[phi'(Ztheta)-phi'(Zdagger)]`.
This uses the bounded endpoint readout, not an unproved L-infinity smallness
of the evolving readout difference. For the adjoint split use the current
backward field, whose L2 norm is at most `C+1`, in the changed-action term.

The only additional row product is a changed first gate times the fixed
endpoint `Q_dagger(v)`. For gates `b=phi'(z)-phi'(z0)`,
`|b|<=min(1,2|z-z0|)` implies

\[
 \|b\|_4\le\sqrt2\|z-z_0\|_2^{1/2},\qquad
 \|bQ_\dagger(v)\|_2\le\sqrt{2a_1}L_4\rho^{1/2}.
 \tag{3.2}
\]

This is Holder's inequality and the proved endpoint L4 bound. It does not
multiply two uncontrolled L2 increments. Also
`||Q_theta(u)||2<=(M+1)(C+1)=:Q1`. Subtracting the explicit input vector
in the row gradient, the middle rank factors and the final hidden value gives

\[
 \|g_\theta(u)-g_\dagger(v)\|\le C_g\rho^{1/2},
\]

\[
 C_g=Q_1+a_Q+a_\delta+Ca_1+a_2+\sqrt{2a_1}L_4.
 \tag{3.3}
\]

The raw Hilbert norm is bounded above here by the sum of its three component
norms. This proves uniform endpoint state/input continuity, including that
of `beta_alpha`, `t_alpha`, and `d_alpha` in (2.9). No input derivative of a
query is required.

At fixed `u`, prediction subtraction also gives

\[
 |f_\theta(u)-f_\dagger(u)|\le C_f d,
 \qquad C_f=1+Ca_2,
 \tag{3.4}
\]

uniformly on the circle. The scalar differentiation formula (2.6) along
strongly C1 raw curves follows from the strong L2 chain rule: for a fixed
direction the tanh difference quotient is dominated by its L2 direction,
and the error of replacing a C1 increment by that direction is controlled
by the one-Lipschitz activation. Differentiating the bounded action product
and the scalar readout pairing gives the three blocks in (2.6). Bounded
multiplier convergence against fixed L2 fields proves their continuity.
Explicitly, if bounded multipliers `b_k` converge in probability to `b`,
split a fixed `q in L2` at `|q|=R`. The bounded part of
`||(b_k-b)q||2` tends to zero by bounded convergence in probability; its
tail is at most `2 sup_k||b_k||infty ||q 1_(|q|>R)||2`. Let `k` grow
first and then `R` grow. Applying this fact successively to the fixed-state
backward and row factors proves continuity at any state, without requiring
an L4 bound at that state.
An ambient Frechet derivative of an L2-valued hidden map is not used.

For explicit projector estimates set

\[
 a_G=\sqrt2 C_g,\quad G_1=G_0+a_G,\quad
 a_M=(2G_0+a_G)a_G.
\]

Then `||G_theta-G_dagger||<=a_G sqrt(d)` and
`||M_theta-M_dagger||<=a_M sqrt(d)`. If
`a_M sqrt(d)<=kappa/2`, the Rayleigh formula gives
`M_theta>=kappa I/2`, and the inverse identity yields

\[
 \|M_\theta^{-1}-M_\dagger^{-1}\|
       \le(2a_M/\kappa^2)\sqrt d.
\]

Expanding the three changed factors in `G M^-1 G*` proves

\[
 \|\Pi_\theta-\Pi_\dagger\|\le C_\Pi\sqrt d,
 \quad C_\Pi={2a_GG_1\over\kappa}
       +{2G_0a_MG_1\over\kappa^2}+{G_0a_G\over\kappa}.
 \tag{3.5}
\]

Writing `d_theta,alpha=Pi_theta g_theta(u_alpha)`, it follows that

\[
 \|d_{\theta,\alpha}-d_\alpha\|\le C_d\sqrt d,
 \qquad C_d=C_g+C_\Pi L_0.
 \tag{3.6}
\]

All constants are uniform over (NS1).

###### B.4. The hidden contrast and its derivative along the reached path

Keep the endpoint readout and coefficients fixed during the episode:

\[
 O_\alpha(\theta)=\sum_{i=1}^3 t_{\alpha,i}
                 \langle c_\dagger,H^2_\theta(v_i)\rangle.
 \tag{4.1}
\]

This functional depends only on hidden parameters. Its raw gradient is
`o_alpha(theta)=(sum_i t_i h_i^fixed(theta),0)`, where `h_i^fixed` is the
first-row/middle portion of (2.6) with the readout set to `c_dagger`.
The proof is the strong curve chain rule just given, with a fixed bounded
readout in the scalar pairing. In particular

\[
 o_\alpha(\theta_\dagger)=(d_{\alpha,H},0),\qquad
 \|o_\alpha(\theta)-o_\alpha(\theta_\dagger)\|
       \le C_o\sqrt d,\quad C_o=\sqrt3T_0 C_g.
 \tag{4.2}
\]

For the last inequality apply (3.3) to the auxiliary state `(w,A,c_dagger)`
and sum its three hidden-gradient differences using
`sum|t_i|<=sqrt(3)|t|`. Thus derivative continuity of this hidden contrast
uses only raw distance and fixed endpoint L4 tails, even if the evolved
query field is known only through the constructed source-regular flow.

The field in (NS3) is continuous on the neighborhood under consideration:
(3.3) and its fixed-state bounded-multiplier proof give gradient continuity,
and (3.5) gives inverse/projector continuity. A raw-continuous solution of
the strong integral equation therefore has a continuous raw derivative.
Its two hidden maps are strongly C1 by the chain rule above. Consequently

\[
 {d\over d\tau}O_\alpha(\theta(\tau))
       =\langle o_\alpha(\theta(\tau)),V_{\alpha,y}(\theta(\tau))\rangle.
 \tag{4.3}
\]

At the endpoint, writing `r_dagger=f_dagger(u_alpha)-y`, (2.2) and (2.10)
give the uniform strictly positive value

\[
 O_\alpha'(0)=-2r_\dagger\|d_{\alpha,H}\|^2\ge5\kappa/8.
 \tag{4.4}
\]

This explicitly checks hidden representation motion. A nonzero hidden
parameter block is only the input to the identity, not its conclusion.

For a quantitative derivative modulus put

\[
 L_1=\sqrt{1+(C+1)^2(1+(M+1)^2)},\quad
 R_1=C+1+5/8,\quad V_1=2R_1L_1.
\]

On the unit raw ball and the invertible-Gram region, `||g_theta(u)||<=L1`,
`|f_theta(u_alpha)-y|<=R1`, and `||V_alpha,y(theta)||<=V1`, because
an orthogonal projector has norm at most one. Equations (3.4) and (3.6) give

\[
 \|V_{\alpha,y}(\theta)-V_{\alpha,y}(\theta_\dagger)\|
      \le C_V\sqrt d,
 \quad C_V=2C_fL_1+(11/8)C_d.
\]

Use (4.2), `||o_alpha(theta_dagger)||<=L0`, and the last bound in (4.3):

\[
 |O_\alpha'(\theta)-O_\alpha'(\theta_\dagger)|
       \le A_O\sqrt d,
 \qquad A_O=C_oV_1+L_0C_V.
 \tag{4.5}
\]

Here `O'(theta)` means its derivative in the actual field (NS3), not a
derivative of a frozen trajectory. This estimate supplies uniform
continuity along all the reached paths in the family.

###### B.5. A uniform, finite nonlinear episode

Choose the following positive raw radius:

\[
 \rho_0=\min\left\{1,\left({\kappa\over2a_M}\right)^2,
             {\kappa\over4C_d^2},\ {5\over32C_f},
             \left({5\kappa\over16A_O}\right)^2\right\}>0.
 \tag{5.1}
\]

Every denominator is finite and positive by its displayed definition. Let

\[
 \tau_0=\min\{\tau_{ex}/2,\rho_0/(2V_1)\}>0.
 \tag{5.2}
\]

Before a possible first exit from the raw ball of radius `rho0`, the
velocity bound `V1` gives `||theta(tau)-theta_dagger||<=V1 tau`.
If that first exit occurred by `tau0`, this distance would be at most
`rho0/2`, a contradiction. Thus all paths stay in the ball through `tau0`.
The Gram is at least `kappa I/2` there. This is a first-exit estimate for the
existing nonlinear equation, not a conclusion from the initial linear term.

Since `G_theta^*Pi_theta=0`, the chain rule applied to the two anchors proves
the anchor assertion. The choices in (5.1), (2.2), and (3.6) give throughout the interval

\[
 |r(\tau)|\ge5/32,\qquad r(\tau)<0,\qquad
 \|d_{\theta(\tau),\alpha}\|^2\ge\kappa/4.
 \tag{5.3}
\]

The exact added prediction and risk identities are

\[
 f_\theta(u_\alpha)'=-2r\|d_{\theta,\alpha}\|^2,\qquad
 (r^2)'=-4r^2\|d_{\theta,\alpha}\|^2.
 \tag{5.4}
\]

They retain every moving hidden field and the recomputed projector. Integrating
(5.3)–(5.4) gives (NS6) with

\[
 \eta_R={25\kappa\over1024}\tau_0>0,
 \qquad f_{\theta(\tau_0)}(u_\alpha)-f_\dagger(u_\alpha)
                        \ge {5\kappa\over64}\tau_0>0.
 \tag{5.5}
\]

By (4.4)–(4.5) and (5.1), `O_alpha'(theta(tau))>=gamma_O:=5kappa/16`.
Hence `Delta O_alpha>=gamma_O tau` for `0<=tau<=tau0`. Cauchy–Schwarz,
first in the second population and then in the three coefficients, yields

\[
 |\Delta O_\alpha|^2
 \le\|c_\dagger\|_2^2|t_\alpha|^2
             \sum_{i=1}^3\|\Delta H_i^2\|_2^2
 \le30T_0^2 J_{2,\alpha,y}(\tau).
 \tag{5.6}
\]

Thus (NS7) holds with the explicit positive constant

\[
 \eta_H={\gamma_O^2\tau_0^2\over30T_0^2}>0.
 \tag{5.7}
\]

This finite episode has actual upper hidden activation displacement. Its
proof uses derivative continuity of a scalar hidden contrast to retain a
strict sign over a finite interval; it does not extrapolate the initial
velocity as the finite trajectory. The interval and margins have no
`epsilon` dependence.

The whole-circle map is
`P_(alpha,y)(tau,sqrt(2)u)=<c(tau),tanh(A(tau)tanh(w(tau).u))>`.
It is jointly continuous in time and input and has a uniformly bounded input
Lipschitz constant on this episode, since it is bounded by
`||c||2 ||A||op ||w||2`. Equation (3.4) gives a uniform whole-circle
comparison to the endpoint on the local ball. This defines the prediction
to be captured; Its original-mixture identification is proved in proof unit C.

##### Proof unit C. Original-initialization continuation and slow selection

###### C.1. State and source interface

Use the state and initialized carrier in (NS2), and write its raw increment
space as \(\mathcal E\). Throughout this unit inputs in \(f_\theta(u)\)
are normalized; the reconstructed physical prediction is evaluated at
\(x=\sqrt2u\). For clarity the fields used in the comparisons are
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),
 \quad f_\theta(u)=\langle c,H^2(u)\rangle,
\]
\[
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),\quad
 g_u=(\phi'(w\cdot u)Q(u)u,\Delta^{(2)}(u)\otimes H^1(u),H^2(u)).\tag{1}
\]
The scalar prediction is continuously differentiable in the raw metric by
the contained scalar-gradient argument in A.4. Set
\[
 p=(\alpha,y)\in\mathcal P=I\times[3/8,5/8],\qquad
 I=[\pi/4-1/1216,\pi/4+1/1216].\tag{2}
\]
All constants below are uniform in this compact box. The reference feature
curve is exactly
\[
 \theta_s=\tfrac12g_{e_1}(\theta)-\tfrac12g_{e_2}(\theta),\tag{3}
\]
and C.4.5 proves the raw endpoint and residual bounds
\[
 \|\theta_*(t)-\theta_\dagger\|_{\rm raw}\le\sqrt{10}e^{-t/5},
 \qquad |r_*(t)|\le\sqrt2 e^{-t/5}.\tag{4}
\]
Its physical control is \(a_*=(e_*,-e_*,0)\), with total absolute mass
\(s_\dagger\le10\). For the three inputs \(e_1,e_2,u_\alpha\), raw Euler is
\[
 \theta_{k+1}=\theta_k+\sum_{j=1}^3\gamma_{kj}g_{u_j}(\theta_k).\tag{5}
\]
Let SCT denote the source estimate of proof unit A: there are uniform
\(\delta_{\rm src},h_{\rm src}>0\) and \(B_{\rm src}<\infty\) for all
such finite histories satisfying
\[
 \int|a(t)-a_*(t)|_1dt<\delta_{\rm src}.\tag{6}
\]
The mesh is measured by \((|a|_1+|a_*|_1)dt\). Every passive backward row,
including its distinguished current source and all old training sources,
then has the stated cap. Deterministic feedback coefficients are frozen
under named differentiation, just as in (CT12)–(CT16).

The physical reference keeps running after every finite prefix. A prefix
through \(b\) followed by appended controls has distance at most the
appended absolute mass plus \(s_\dagger-s_*(b)\), including a zero extension
after the episode. This supplies the endpoint interface without a source
reset. All subsequent constructions use this exact full-history condition.

###### C.2. Consequences of SCT and the one-reference modulus

Write \(L=\sum_{k,j}|\gamma_{kj}|\). Under (6),
\(L\le10+\delta_{\rm src}\). The elementary controlled updates give

\[
 \|c\|_\infty\le L,\quad \|K\|_{\rm HS}\le L^2/2,\quad
 \|A\|_{\rm op}\le2+L^2/2,\quad
 \|w\|_2\le\sqrt2+L^2+L^4/8.
 \tag{7}
\]

Indeed the readout increases by at most the current control mass, the middle
increment by at most that mass times the preceding readout bound, and the
row increment by at most that mass times the action/readout bounds.
Summing is bounded by the corresponding integrals in accumulated mass.
Harmless enlarged constants also cover affine interpolants and unequal
simultaneous updates. None depends on physical elapsed time.

The exact source identity C.4.7.N5 is
\(Q_{kv}=\zeta_{kv}+\sum_qD_{kv,q}H^1_q\). Its learned coefficient row has
absolute sum at most \(L\sup\|c\|_\infty^2\); its response row is bounded by
SCT. Also \(\mathbb E\zeta_{kv}^2\le\sup\|c\|_\infty^2\). Thus

\[
 Q_{kv}=\zeta_{kv}+J_{kv},\quad |J_{kv}|\le C,\quad
 \operatorname{Var}(\zeta_{kv})\le C^2,
 \qquad \tau_R(Q_{kv})\le C e^{-cR^2}\quad(R\ge1).
 \tag{8}
\]

The last estimate follows by splitting at \(R>2C\), using
\(\{|Q|>R\}\subset\{|\zeta|>R-C\}\), and integrating the scalar Gaussian
tail; enlarging the constant covers the remaining \(R\). It requires no
independence of \(J\) and \(\zeta\). In particular

\[
 \sup_{k,v}\|Q_{kv}\|_p\le C_p<\infty\qquad(2\le p<\infty).
 \tag{9}
\]

These are separate deterministic input/time bounds, not a moment bound for
an uncountable coordinate supremum.

For two raw states \(\theta,\bar\theta\) on a common bounded raw/action region,
use the equivalent sum distance \(d\). Suppose only the comparison endpoint
\(\bar\theta\) has \(\|\bar c\|_\infty\le C\) and the tails (8).
Subtract the factors in (1). The upper subtraction is

\[
 \Delta^{(2)}-\bar\Delta^{(2)}=(c-\bar c)\phi'(Z^2)
                +\bar c[\phi'(Z^2)-\phi'(\bar Z^2)].
\]

It costs \(Cd\), as do \(Q-\bar Q\) and the middle/readout blocks.
The remaining lower product is bounded by

\[
 \|[\phi'(w\cdot v)-\phi'(\bar w\cdot v)]\bar Q(v)\|_2
 \le 2R\|w-\bar w\|_2+2\tau_R(\bar Q(v)).
 \tag{10}
\]

Changing the input adds \(C|v-\bar v|\) to the forward and upper differences;
apply (10) also to the lower gate with
\(\|w\cdot v-\bar w\cdot\bar v\|_2\le
\|w-\bar w\|_2+\|\bar w\|_2|v-\bar v|\).
Consequently

\[
 \|g_v(\theta)-g_{\bar v}(\bar\theta)\|_{\rm raw}
 \le C(1+R)(d+|v-\bar v|)+C e^{-cR^2}.
 \tag{11}
\]

Only the comparison state's tails appear. Its readout supremum is likewise
the only readout supremum used in this subtraction. An arbitrary competing
strong raw solution therefore need not satisfy a new tail assumption.

For \(0<z\le1\), set
\(\omega(z)=z\sqrt{\log(e/z)}\), and extend it increasingly at larger \(z\).
Choosing \(R\) proportional to \(\sqrt{\log(e/z)}\) in (11) gives the
one-reference bound \(C\omega(z)\). The function is increasing on \((0,1]\),
and

\[
 \int_{0+}\frac{dz}{\omega(z)}=\infty.
 \tag{12}
\]

The following explicit comparison will be used repeatedly. If
\(D(t)\le\eta+C\int_0^t\omega(D(s))ds\), then, while the right side stays
below one,

\[
 D(t)\le {\cal O}_t(\eta):=
 e\exp\!\left[-\left(\sqrt{\log(e/\eta)}-Ct/2\right)^2\right].
 \tag{13}
\]

To prove it, put \(Z(t)=\eta+C\int_0^t\omega(D(s))ds\). Monotonicity gives
\(Z'\le C\omega(Z)\), and
\((\sqrt{\log(e/Z)})'\ge-C/2\). Integrate. For \(\eta=0\), replace it by a
positive number and let that number decrease to zero. For every fixed
bounded interval, \({\cal O}_t(\eta)\to0\) uniformly as \(\eta\to0\).
A first-exit argument validates staying below one when the initial error
is sufficiently small.

###### C.3. Endpoint conditioning and constrained coefficients

Let \(G(\theta):\mathbb R^2\to\mathcal E\) have columns \(g_{e_1},g_{e_2}\).
The endpoint Gram \(M_\dagger=G(\theta_\dagger)^*G(\theta_\dagger)\) is strictly
positive. This follows from proof unit B.

By joint raw gradient continuity there are \(\rho>0,\kappa>0\) such that on

\[
 {\cal N}=\{\|\theta-\theta_\dagger\|_{\rm raw}<\rho\}
 \quad\text{one has}\quad M(\theta):=G^*G\ge4\kappa I_2.
 \tag{14}
\]

Shrink \(\rho\) once and retain an interior ball for all constructed paths.
The neighborhood has bounded raw/action norms, although it need not have
bounded readout supremum. The latter bound comes from controls, not (14).
Put

\[
 B(\theta)=G(\theta)M(\theta)^{-1},\quad
 \Pi(\theta)=I-G(\theta)M(\theta)^{-1}G(\theta)^*,
\]
\[
 r_p(\theta)=f_\theta(u_\alpha)-y,\quad
 v_p(\theta)=r_p(\theta)g_{u_\alpha}(\theta),\quad
 V_p(\theta)=-2\Pi(\theta)v_p(\theta).
 \tag{15}
\]

The inverse in (15) is an ordinary two-by-two matrix inverse. The coefficients
are bounded and continuous on a slightly smaller raw neighborhood, uniformly
in \(p\). In particular

\[
 V_p(\theta)=\sum_{j=1}^3a_j(\theta,p)g_{u_j}(\theta),
 \quad (a_1,a_2)^T=2r_p M^{-1}G^*g_{u_\alpha},\quad a_3=-2r_p,
 \quad |a|_1\le A.
 \tag{16}
\]

The scalar prediction is Lipschitz on bounded raw/action sets. Equations
(11), the identity
\(M^{-1}-\bar M^{-1}=M^{-1}(\bar M-M)\bar M^{-1}\), and the bounded Gram
factors therefore give

\[
 \|V_p(\theta)-V_{\bar p}(\bar\theta)\|_{\rm raw}
 \le C\omega(d(\theta,\bar\theta)+|p-\bar p|)
 \tag{17}
\]

when \(\bar\theta\) is a tail-bearing constructed state. The same estimate
holds for the coefficient vector in (16). It does not assert an ambient
locally Lipschitz field.

###### C.4. Construction from reference prefixes, tails, and uniqueness

Choose reference physical prefixes ending at \(b_m\uparrow\infty\), with
sufficiently fine finite raw Euler approximations using exact integrated
reference controls. Their terminal states
\(\theta_m^0\) converge in raw norm to \(\theta_\dagger\), by the established
reference construction, or by (11)--(13) and SCT. Their controls approximate
the fixed reference controls on that prefix. Immediately after \(b_m\),
append the explicit Euler recursion on an interval of length \(\tau_0\)

\[
 \theta^{m,h}_{k+1}=\theta^{m,h}_k+h_k V_p(\theta^{m,h}_k).
 \tag{18}
\]

Choose once a positive \(\tau_0\) so small that

\[
 A\tau_0<\delta_{\rm src}/8,\qquad
 \tau_0\sup_{{\cal N},p}\|V_p\|_{\rm raw}<\rho/8.
 \tag{19}
\]

Take \(m\) large enough that the prefix state error is below \(\rho/8\),
its control approximation error is below \(\delta_{\rm src}/8\), and the
omitted suffix has mass below \(\delta_{\rm src}/8\). The bound on (18)'s
accumulated speed keeps all its nodes strictly inside \({\cal N}\); the
controls (16) are legitimate throughout. Equations (19) keep the entire
history strictly inside the SCT tube. Decrease its maximal control mesh
as necessary. This proves admissibility before using the tail conclusion.

Compare two appended Euler interpolants. Their preceding-node distance is
at most their current distance plus \(C(h+h')\). Equation (17), with (8)
at the comparison nodes, bounds their velocity difference by the Osgood
modulus of that quantity, plus the parameter discrepancy. Integrating and
using (13) shows they are Cauchy in \(C([0,\tau_0];\mathcal E)\), uniformly in
\(p\), as their prefix errors and meshes tend to zero. The limit is independent
of those choices. One may first use a countable dense parameter/mesh family
and its finite unions on the prescribed carrier, then extend by the same
uniform estimate; no uncountable family of independent carriers is chosen.

The joint continuity of (1) and (15) passes (18)'s integral equation to

\[
 \bar\theta_p(\tau)=\theta_\dagger+
             \int_0^\tau V_p(\bar\theta_p(s))\,ds.
 \tag{20}
\]

The convergence of the integrands is uniform: otherwise choose discrepant
times and parameters, extract a convergent parameter/time subsequence, and
apply continuity at the limiting state. Thus (20) is strongly \(C^1\), jointly
continuous in \(p,\tau\), and has one-sided derivatives at the endpoints.
All coefficients are computed from the current full state, the fixed atom,
and the retained initialized action. The reference prefix is an approximation
of its already specified initial state, not a pretraining stage imposed on
the changed-law optimizer.

The Gaussian tails survive this construction. Raw convergence gives
\(Q_m(v)\to Q(v)\) in \(L^2\), uniformly over compact parameter/time/input sets,
by bounded-multiplier continuity and compactness. For fixed \(R\),
\(q\mapsto(|q|-R)_+\) is \(L^2\)-Lipschitz and

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2.
 \tag{21}
\]

Pass (8) through this continuous positive-part norm; (21) gives
\(\tau_R(Q)\le C e^{-c'R^2}\) with enlarged constants. Similarly
\(\|c\|_\infty\le10+\delta_{\rm src}\) passes through an almost-everywhere
subsequence. All moments (9), particularly \(L^4\) and \(L^8\), follow.
Interpolation between \(L^2\) convergence and the uniform \(L^8\) bounds
makes the query maps jointly continuous into \(L^4\).

Uniqueness requires tails only on this constructed path. If another strong
solution of (20) on the same carrier starts at \(\theta_\dagger\), compare it
with \(\bar\theta_p\) using (17) and (13). On their initial common
neighborhood the initial error is zero, so they coincide. Repeating at the
end of a common subinterval proves equality through \(\tau_0\); an earlier
exit would contradict the constructed path's strict interior bound.
The same argument proves uniqueness from every reached state on the remaining
interval. No arbitrary-state existence assertion is made.

Since the scalar predictions are \(C^1\), (20) gives
\(\partial_\tau(f(e_1),f(e_2))=G^*V_p=0\). Both anchors are fitted exactly
throughout. The whole-circle determining prediction is

\[
 P_p(\tau,\sqrt2v)=
 \langle\bar c_p(\tau),
  \phi((A_0+\bar K_p(\tau))\phi(\bar w_p(\tau)\cdot v))\rangle.
 \tag{22}
\]

The full hidden state evolves in (20). Formula (22) is not a prediction-only
closure or a frozen kernel.

###### C.5. Strong activation derivatives and absolute continuity of B

These derivative statements concern controlled reached curves, not arbitrary
ambient directions. Let a reached raw curve solve

\[
 \theta'(t)=\sum_{j=1}^3a_j(t)g_{u_j}(\theta(t)),\qquad
 m(t)=\sum_j|a_j(t)|\in L^1,
 \tag{23}
\]

and assume the uniform query tails and readout bounds just proved. All constants
below depend only on those reached bounds and the anchor gap.
The first component of (1) gives
\(\|w'(t)\|_4\le C m(t)\). Also
\(\|K'(t)\|_{\rm HS}+\|c'(t)\|_2\le C m(t)\) and the pointwise readout
formula gives \(|c'(t,\omega_2)|\le m(t)\).
Hence, for every deterministic passive input \(v\),

\[
 (H^1(v))'=\phi'(w\cdot v)\,w'\cdot v,\qquad
 (Z^2(v))'=K'H^1(v)+A[\phi'(w\cdot v)\,w'\cdot v],
\]
\[
 (H^2(v))'=\phi'(Z^2(v))(Z^2(v))',\qquad
 \Delta^{(2)}(v)'=c'\phi'(Z^2(v))+c\phi''(Z^2(v))(Z^2(v))',
\]
\[
 Q(v)'=K'^*\Delta^{(2)}(v)+A^*\Delta^{(2)}(v)'.
 \tag{24}
\]

These are strong \(L^2\) absolutely continuous identities and
\(\|Q(v)'\|_2+\|\Delta^{(2)}(v)'\|_2\le Cm(t)\). A direct justification, which
also covers merely integrable controls, is to choose the coordinatewise
absolutely continuous representatives supplied by Fubini, apply the scalar
chain rule almost everywhere, and integrate the displayed \(L^2\)-integrable
derivatives. The uniform pointwise bound on \(c\) handles its product with
\((Z^2)'\). This argument needs no \(L^\infty\) Banach-space derivative of c.

Differentiate the three blocks of (1) along (23):

\[
 (g_v)'_w=
 \{\phi''(w\cdot v)(w'\cdot v)Q(v)+\phi'(w\cdot v)Q(v)'\}\,v,
\]
\[
 (g_v)'_K=\Delta^{(2)}(v)'\otimes H^1(v)+\Delta^{(2)}(v)\otimes(H^1(v))',
 \qquad (g_v)'_c=(H^2(v))'.
 \tag{25}
\]

The only additional unbounded product is the first term in (25). Hölder gives

\[
 \|(w'\cdot v)Q(v)\|_2\le\|w'\|_4\|Q(v)\|_4\le Cm(t).
 \tag{26}
\]

All other terms are controlled by (24), bounded gates, and the rank norm
identity. Thus each anchor gradient is absolutely continuous in raw norm and
\(\|G'(t)\|_{\mathrm{op}}\le Cm(t)\).
The same coordinatewise argument, now using (26), proves the fundamental
theorem for (25); it is not a formal ambient Hessian calculation.

Ordinary finite-matrix absolute continuity and (14) now yield

\[
 M'=G'^*G+G^*G',\qquad
 B'=G'M^{-1}-GM^{-1}M'M^{-1},\qquad
 \|B'\|_{\mathrm{op}}\le Cm(t).
 \tag{27}
\]

Along (20), the coefficients (16), the query \(L^4\) continuity, and bounded
multiplier continuity show that its row velocity is jointly \(L^4\)-continuous
in \((p,\tau)\). Equations (24) show that the strong activation derivatives
are jointly \(L^2\)-continuous in \((p,\tau,v)\), including \(\tau=0\).
For example the multiplier difference is applied to one fixed limiting
velocity, and its varying velocity is subtracted first; compactness makes
this argument uniform. Consequently

\[
 H^2_{\bar\theta_p(\tau)}(v)
 =H^2_{\theta_\dagger}(v)+
   \tau\,D H^2_{\theta_\dagger}(v)[V_p(\theta_\dagger)_h]
   +o_{L^2}(\tau)
 \tag{28}
\]

uniformly on compact parameter/input sets. The derivative is the strong
curve derivative in (24). This is the uniform derivative fact needed for the
paired hidden-activation margin in proof unit B.

###### C.6. Actual original-mixture continuation in the control tube

For an existing reached mixture segment set
\(r=(f(e_1)-1,f(e_2)+1)\). The exact equations, with the two anchor weights
included, are

\[
 \theta'=-(1-\varepsilon)Gr-2\varepsilon v_p,\qquad
 r'=-(1-\varepsilon)Mr-2\varepsilon G^*v_p.
 \tag{29}
\]

The controls in (23) are
\((-(1-\varepsilon)r_1,-(1-\varepsilon)r_2,-2\varepsilon r_p)\).
On the bounded conditioned region, for \(0<\varepsilon\le1/2\),

\[
 |r(t)|\le e^{-2\kappa(t-b)}|r(b)|+C\varepsilon,\qquad
 \int_b^t|r(s)|ds\le C|r(b)|+C\varepsilon(t-b).
 \tag{30}
\]

Indeed pair the residual equation with \(r/|r|\) away from zero, use
\(M\ge4\kappa I\), and bound \(G^*v_p\). Regularization by
\(\sqrt{|r|^2+\eta^2}\) and \(\eta\downarrow0\) covers zero residuals.
In particular the post-b control mass and raw displacement are at most

\[
 \int_b^t m(s)ds+
 C^{-1}\|\theta(t)-\theta(b)\|_{\rm raw}
 \le C|r(b)|+C\varepsilon(t-b).
 \tag{31}
\]

Here and below constants may be enlarged; the sum form of (31) is only an
upper bound, not an equality.

The next two discrete steps construct that existing segment before using
its continuous estimates. In particular (30) is not used to assume the
existence it is meant to control.

**Fixed b prefix, before any changed-program cap**

Every finite raw Euler program for the three-atom mixture exists by finite
recursion. Through a separately fixed b, its elementary readout recurrence
gives \(\|c_k\|_\infty\le e^{2b}-1\); summing its bounded-gate updates gives
finite constants for its raw norm, action norm, and interpolation speed,
depending on b but not on p, \(\varepsilon\), or the mesh. This is the direct
calculation of C.4.7.NE with T replaced by this fixed b, not an extension of
that theorem's source cap.

Compare this arbitrary mixture Euler interpolant with the already existing
actual reference on \([0,b]\), using the latter as the sole tail-bearing
endpoint. Its passive Gaussian tails follow from C.4.6.S43 or SCT. The
cutoff subtraction (11), residual differences, and the preceding-node
error give, for physical maximal mesh h,

\[
 \sup_{t\le b}d(\theta_{\varepsilon,p}^{h}(t),\theta_*(t))
 \le C_b e^{C_b(1+R)b}
       \{(1+R)(\varepsilon+h)+e^{-cR^2}\}.
 \tag{32a}
\]

The law difference at the reference is \(O(\varepsilon)\), uniformly in p;
the proxy's preceding-node error is \(O(h)\). These are the two sources
inside the first brace. No tails of the mixture Euler program enter.
Choose R proportional to \(\sqrt{\log(e/(\varepsilon+h))}\), with its
constant large enough to make the Gaussian term smaller than a fixed power
of \(\varepsilon+h\). The linear-in-R amplification is sub-power.
Thus the right side defines a modulus \(\omega_b(\varepsilon+h)\to0\).

Let \(a^h_{\varepsilon,p}\) be the piecewise constant controls of this
Euler program. Uniform scalar prediction continuity and its node error imply

\[
 D_{\varepsilon,b}^{h}:=
 \int_0^b|a^h_{\varepsilon,p}(t)-a_*(t)|_1dt
 \le C_b\{\varepsilon+h+\omega_b(\varepsilon+h)\}\longrightarrow0.
 \tag{32b}
\]

Thus actual integrated coefficient closeness, not merely a raw norm
comparison, is established before applying SCT. For fixed sufficiently small
\(\varepsilon\) and all sufficiently fine meshes these prefixes lie in a
strict SCT tube. Their subsequent Euler Cauchy completion uses the now
available mixture-program tails. This proves uniform-in-p convergence of
the completed prefix to the reference as \(\varepsilon\to0\), for every
separately fixed b, however large.

**Post-b discrete residual contraction and cap first exit**

Include b as a mesh node. Continue actual-mixture Euler with its own
population residuals. Use inner stopping thresholds \(\rho/2\) for distance
from \(\theta_\dagger\) and \(\delta_{\rm src}/2\) for the integrated control
distance; the outer raw ball and source tube have radii \(\rho\) and
\(\delta_{\rm src}\). Choose the step small enough that one update from an
inner stopped node, and its full affine segment, remains in the outer
regions. Its coefficient size is uniformly bounded there by
\(C(|r_k|+\varepsilon)\); its physical step can also be made small enough
to satisfy the dominating control-mesh threshold.

The whole finite history through each such affine segment is source
admissible, so its recomputed passive queries have uniform \(L^4\) bounds.
Along that segment the constant velocity is
\(V_k=-(1-\varepsilon)G_k r_k-2\varepsilon v_{p,k}\).
Its row \(L^4\) norm, middle HS norm, and pointwise readout derivative
are bounded by \(C(|r_k|+\varepsilon)\). Apply the proof of (24)--(26) along
this affine curve, using its fixed node velocity and its current queried
fields. It gives
\(\|(g_{e_a})'\|_{\rm raw}\le C(|r_k|+\varepsilon)\).
The scalar chain rule and a second integration therefore give the exact
Euler residual expansion

\[
 r_{k+1}=[I-h_k(1-\varepsilon)M_k]r_k
       -2h_k\varepsilon G_k^*v_{p,k}+R_k,\qquad
 |R_k|\le C h_k^2(|r_k|+\varepsilon)^2.
 \tag{32c}
\]

This is a derivative along a controlled affine step; it does not assert
ambient \(C^2\) regularity. Since \(4\kappa I\le M_k\le M_{\max}I\),
choose \(h_kM_{\max}\le1\). Then
\(\|I-h_k(1-\varepsilon)M_k\|\le1-2\kappa h_k\).
The residuals are bounded on the outer region, say by \(R_{\max}\).
Use \((|r_k|+\varepsilon)^2\le(R_{\max}+1)(|r_k|+\varepsilon)\), and
decrease the maximal step so that
\(Ch_k(R_{\max}+1)\le\kappa\). Absorbing the remainder yields

\[
 |r_{k+1}|\le(1-\kappa h_k)|r_k|+C h_k\varepsilon,\qquad
 \sum_{k:\ b\le t_k<t_N}h_k|r_k|
 \le C|r_b|+C\varepsilon(t_N-b).
 \tag{32d}
\]

The sum follows by telescoping the first inequality, not by accumulating
an \(O(hT)\) error. The post-b control mass and raw displacement obey the
same right-hand bound. These estimates are uniform in mesh and horizon
while the stopped construction is in the outer regions.

On the original physical schedule, keep the reference running throughout.
The triangle inequality after b gives, through
\(T=b+\tau_0/\varepsilon\),

\[
 \int_0^T|a^h_{\varepsilon,p}-a_*|_1dt
 \le D_{\varepsilon,b}^{h}+(s_\dagger-s_*(b))
             +C|r_b|+C\tau_0.
 \tag{33}
\]

One may pad the actual program with zero controls after T; the untruncated
reference tail is still bounded by \(s_\dagger-s_*(b)\).
No independent time change of that reference is needed.

Choose b large so that the reference endpoint error, its residual, and its
remaining control mass are much smaller than the inner margins. Then choose
\(\varepsilon+h\) small in (32a)--(32b) so that the mixture prefix has the
same properties. Finally decrease \(\tau_0>0\), uniformly in p, so that
\(C\tau_0\) and its associated raw displacement use less than one quarter of
the inner margins. Equations (32d)--(33) keep a potential first exiting node
strictly inside both inner regions. This contradicts first exit.
Thus all the Euler programs continue through \(b+\tau_0/\varepsilon\) with
uniform source caps and raw bounds.

For each fixed positive \(\varepsilon\) this is a finite physical horizon.
The one-reference Osgood comparison, now with the capped Euler paths,
makes the actual-mixture Euler programs Cauchy as their physical meshes
vanish. The argument of Section 4 passes their equations, Gaussian tails,
and scalar controls to a unique strong solution of (29).
It starts from the original initial state. The physical mesh may depend on
\(\varepsilon\); no simultaneous step/perturbation limit is claimed.
The integrated bounds pass to the limit, and the exact continuous
calculation gives (30)--(31).

The choice of \(\tau_0\) works for every sufficiently large b; only the
required smallness of \(\varepsilon\) and the proof mesh depends on b.
This proves the needed original-mixture continuation rather than assuming
it, and permits the successive limits in the next section.

###### C.7. Residual identity and singular selection

Equations (29) give the exact identity

\[
 \theta'=\varepsilon V_p(\theta)+B(\theta)r'.
 \tag{34}
\]

Indeed multiplying the residual equation by \(B=GM^{-1}\) recovers the
anchor force and subtracts precisely the normal component of the added
force. By (27), on the reached segment,

\[
 \|B'(t)\|_{\mathrm{op}}\le C(|r(t)|+\varepsilon).
\]

Combining with (30) and integrating gives

\[
 \int_b^t\|B'(s)r(s)\|_{\rm raw}ds
 \le C\{|r(b)|^2+\varepsilon|r(b)|+\varepsilon^2(t-b)\}.
 \tag{35}
\]

For example \(|r|\le a e^{-2\kappa(s-b)}+C\varepsilon\); squaring and
integrating bounds \(\int|r|^2\) by
\(Ca^2+C\varepsilon a+C\varepsilon^2(t-b)\), and the additional
\(\varepsilon\int|r|\) has the same bound.

The Hilbert-space absolutely continuous product rule now legitimately yields

\[
 \theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
       +\varepsilon\int_b^t V_p(\theta(s))ds
       -\int_b^t B'(s)r(s)ds.
 \tag{36}
\]

Set \(\widetilde\theta_{\varepsilon,b,p}(\tau)
=\theta_{\varepsilon,p}(b+\tau/\varepsilon)\).
Uniformly for \(0\le\tau\le\tau_0\), (30), (35), and (36) give

\[
 \widetilde\theta_{\varepsilon,b,p}(\tau)
 =\theta_\dagger+
       \int_0^\tau V_p(\widetilde\theta_{\varepsilon,b,p}(s))ds
       +E_{\varepsilon,b,p}(\tau),
\]
\[
 \sup_{\tau,p}\|E_{\varepsilon,b,p}(\tau)\|_{\rm raw}
 \le C\{\sup_p\|\theta_{\varepsilon,p}(b)-\theta_\dagger\|_{\rm raw}
       +\sup_p|r_{\varepsilon,p}(b)|
       +\sup_p|r_{\varepsilon,p}(b)|^2+\varepsilon\}.
 \tag{37}
\]

At fixed b the right side has limit superior at most \(Ce^{-b/5}\), by
(4) and the completed-prefix consequence of (32a)--(32b). Compare (37) with
(20), putting the constructed constrained
path on the tail-bearing side of (17). Formula (13) then gives

\[
 \limsup_{\varepsilon\downarrow0}
 \sup_{p,\tau\le\tau_0}
 \|\widetilde\theta_{\varepsilon,b,p}(\tau)-\bar\theta_p(\tau)\|_{\rm raw}
 \le {\cal O}_{\tau_0}(Ce^{-b/5}).
 \tag{38}
\]

Send b to infinity. For original, unshifted slow time and any fixed
\(0<\tau_{\min}<\tau_0\), write
\(\sigma=\tau-\varepsilon b\ge0\) for small \(\varepsilon\).
Then
\(\theta_{\varepsilon,p}(\tau/\varepsilon)
=\widetilde\theta_{\varepsilon,b,p}(\sigma)\), while
\(\|\bar\theta_p(\tau)-\bar\theta_p(\sigma)\|\le C\varepsilon b\).
Equation (38) proves

\[
 \lim_{\varepsilon\downarrow0}
 \sup_{p\in\mathcal P}\sup_{\tau_{\min}\le\tau\le\tau_0}
 \|\theta_{\varepsilon,p}(\tau/\varepsilon)-\bar\theta_p(\tau)\|_{\rm raw}=0.
 \tag{39}
\]

The reference path is compared at the same physical times and tends to
\(\theta_\dagger\) uniformly on this interval. The exclusion of \(\tau=0\)
in (39) is necessary: the actual original state at physical zero is not the
fitted endpoint. The reference-prefix decomposition proves the limit and
does not change the optimizer.

The bounds for forward actions and the scalar prediction on bounded raw sets
are uniform in the circle input. They therefore turn (39) into whole-circle
prediction convergence and uniform \(L^2\) activation convergence.
The physical scale is \(t=\tau/\varepsilon\), obtained from the exact
projected force in (34). No finite-order law-response expansion has been
extended to this scale.

##### Proof unit D. Actual finite gradient flow and paired observations

###### D.1. Fixed-horizon population-to-finite bridge

Fix one positive epsilon and one admitted added law, and a finite physical
horizon T (which may equal tau0/epsilon). Suppose controlled population Euler
programs for its actual mixture GF converge strongly on [0,T] to a unique
population path theta, with the following bounds uniform in sufficiently fine
Euler partitions: ordinary raw state ball; readout essential supremum;
passive-query second-moment tails

    tau_R(Q(u)) + tau_R(c) <= C exp(-a R^2),  R>=1,

for every training and finitely named observation input. Constants may depend
on the fixed epsilon and T. Here tau_R(v)=||v 1_{|v|>R}||_2; any equivalent
soft cutoff can be used in intermediate convergence arguments. Assume all these
Euler programs live on the same initialized Gaussian carrier and use its actual
forward action and actual adjoint. Their strong limit determines predictions
by f_theta(u)=<c,tanh((A0+K)tanh(w.u))>.

Then the actual width-n mixture GF, starting at the prescribed independent
Gaussian arrays with their actual nonzero readout, converges in probability to
this prediction in C([0,T]xS1). For every finite list of times and inputs, its
first-row, forward hidden, upper gate, readout, and actual forward/adjoint-query
fields have the joint same-layer observation limits supported by the maintained
finite-program theorem and its second-moment extension. This includes paired
second-hidden activation distances between mixture and reference flows using
the same initialized arrays. No unknown finite-width endpoint is introduced.

###### D.2. Proof

At width n all vector and matrix norms are ordinary Euclidean, Frobenius or
operator norms. The raw state-increment metric is

    d_n^2=||W1-W1bar||_F^2/n+||W2-W2bar||_F^2+||c-cbar||_2^2/n.

The initialized middle action itself is bounded in operator norm, rather than
Frobenius norm; only its increments enter d_n. Work on initial events on which
its operator norm, the first-row second moment and initial loss are bounded.
Their probabilities tend to one by the established Gaussian initialization
bounds and laws of large numbers. The actual initial readout has entries of
standard deviation 1/n. Its maximum tends to zero in probability, because
Pr(max_j |c0,j|>eta)<=2n exp(-n^2 eta^2/2). Its normalized second moment also
tends to zero. It is retained in every finite array and proxy, never set to zero.

The finite GF is global at every n. Its smooth vector field is locally
Lipschitz in finite dimensions; unhalved loss dissipation gives
integral_0^T ||theta_n'||_raw^2 <= L_n(0). Hence its raw displacement is at most
sqrt(T L_n(0)). This bounds the action norm by its initialized norm plus the
Frobenius increment. Also |c_n'(j)|<=2 integral |f_n-y| dmu <=2 sqrt(L_n(0)),
so ||c_n(t)||_infty<=||c_n(0)||_infty+2T sqrt(L_n(0)). These bounds imply a
finite raw velocity bound on [0,T], uniform on the preceding initial events.
They justify continuation and every subsequent comparison; they do not provide
the decisive population query tails.

Fix a finite Euler partition h and freeze the *population Euler program's*
scalar training coefficients. Run that exact finite program on the actual
Gaussian arrays, including their initial readout. Call it the finite proxy.
It uses every actual middle multiplication and its actual transpose; no
independent replacement is made. The fixed-program neural law and its
at-most-quadratic observation extension show convergence of all its finitely
named fields, scalar contractions and second moments to their population
program values. The small initial readout passes by a fixed-oracle cutoff induction, rather
than a dimension-dependent finite-dimensional Lipschitz bound. First construct
the finite oracle with zero limiting readout instructions and the same actual
first/middle arrays. Its fixed nodes have the proved joint second-moment laws.
Compare the actual-readout proxy to that oracle, keeping its Gaussian readout
additively in the former. The initial raw error tends to zero. At a coordinate
update, every changed bounded gate multiplying an oracle L2 field is split at
a fixed cutoff R: its bounded part is controlled by the preceding raw error,
and its remaining normalized error by that oracle field's empirical L2 tail.
At fixed program and R the latter converges by the node's second-moment law;
then R tends to infinity. Direct action and rank subtractions handle the other
terms. Induction through the finite number of nodes therefore gives raw error
tending to zero at every node. Readout suprema stay bounded on the initial
events because the update is a sum of bounded tanh values and the actual
initial maximum vanishes. No uniform Lipschitz constant on arbitrary
width-dependent parameter balls is assumed. This is the fixed-program
extension used by C.4.7; the zero-readout object is only a comparison oracle,
never a replacement for an actual finite run or its actual-readout proxy.
In particular, the discrepancy between a proxy prediction at an update input
and its population coefficient's prediction tends to zero. Denote the maximum
of these finitely many discrepancies by zeta_(n,h); then zeta_(n,h)->0 in
probability for fixed h.

For clarity, the comparison can be made at every left Euler endpoint and its
affine interpolation. The interpolation stays on a common raw ball. Its
recomputed c and Q tails converge at a fixed cutoff to the corresponding
population tails. One may first name a finite additional interpolation grid;
the forward/action maps are L2 Lipschitz on this ball with bounded readout,
and the proxy raw interpolation speed is bounded. Soft tails
||(|Q|-R)_+||_2 are one-Lipschitz in Q and pass to the fixed-program limit.
A finer interpolation grid and the elementary inequalities relating hard tails
at R to soft tails at R/2 give the asserted bound uniformly over interpolation
time, with enlarged constants. No growing transcript is taken before width.

Subtract actual GF from the affine proxy. The one-reference product inequality
is elementary: for a bounded Lipschitz gate b and an arbitrary comparison
vector qbar,

    ||(b(z)-b(zbar))qbar||_2
                <= C R ||z-zbar||_2 + C tau_R(qbar).

Apply it to the lower gate multiplier with the proxy Q as qbar and to the
upper multiplier with proxy c. Direct bounded-operator subtraction handles Q
itself. The middle rank subtraction uses
||a tensor b||_HS=||a||_2||b||_2. Prediction residual subtraction is bounded by
the raw distance on the common ball. The frozen coefficient error contributes
zeta_(n,h), and the interpolation defect contributes O(h_max). Thus, for each
fixed cutoff R and the fixed T,

    sup_[0,T] d_n <= C_T exp(C_T R) [
       (1+R)(h_max+zeta_(n,h))
       + sup_proxy_time (tau_R(c_proxy)+sum_j p_j tau_R(Q_proxy(u_j))) ].

The two finite states have identical initial arrays, so there is no initial
state error in this inequality. The actual initial Gaussian readout remains
inside both states and the harmless uniform initial bounds above.

Take n->infinity with the partition and cutoff fixed. The proxy tails tend to
bounded Gaussian population tails, and zeta_(n,h) vanishes. For any desired
comparison error, first choose R large enough that
C_T exp(C_T R-a'R^2) is smaller than that error, then choose h_max small enough
that its amplified interpolation defect is smaller still. Both choices are
finite at every fixed positive epsilon. This proves proximity of finite GF to
the finite proxy in probability, with arbitrarily small prescribed error.
Strong population Euler completion then identifies the unique population path.
One does not send R to infinity at a fixed positive mesh, or claim uniform
width rates as epsilon tends to zero.

On each common raw ball,

    sup_u |f_theta(u)-f_thetabar(u)| <= C_T d(theta,thetabar),
    ||H2_theta(u)-H2_thetabar(u)||_2 <= C_T d(theta,thetabar).

The input Lipschitz constants are bounded by products of the readout, action
and first-row norms; H1 and H2 satisfy the corresponding L2 input estimates.
Consequently finite input nets upgrade proxy prediction convergence to the
whole circle, uniformly in physical time using the same velocity bounds.
This proves the claimed C([0,T]xS1) convergence.

For joint reference/mixture observations, use the union of their finite proxy
programs on the SAME Gaussian arrays and the finite-program joint law. Paired
bounded activation products are permitted second-moment observations. Both
finite flows are close to their proxies in the normalized hidden norms, so
Cauchy–Schwarz passes each mixed inner product and squared distance. Reference
capture is required only on this fixed finite T, where the established result
applies. The endpoint appears only afterwards, through the proved population
reference convergence as epsilon tends to zero and T=tau/epsilon tends to
infinity. Thus the paired finite statistic at time T converges to

    (1/m) sum_i ||H2_theta_mu(T)(u_i)-H2_theta_*(T)(u_i)||_2^2.

Combining the population selection theorem of proof unit C with the already
proved reference endpoint convergence gives its constrained-path versus latent
endpoint limit. This order keeps the actual common initialization intact.

##### Completion of the theorem

Take the common constrained existence time from proof unit C as the
\(\tau_{ex}\) used in proof unit B, and use B's smaller positive time as
our final \(\tau_0\). Decreasing a time already constructed preserves every
source bound, uniqueness statement and mixture continuation estimate. Set
\(a=\eta_R\) from (5.5) and \(j=\eta_H\) from (5.7), both in proof unit B.
They depend only on the fixed reference and parameter rectangle.

Proof unit C proves (NS5) uniformly over that rectangle, in the original
unshifted physical times \(t=\tau/\epsilon\). Its original-mixture Euler
programs verify all the population hypotheses of proof unit D for each fixed
positive \(\epsilon\). Thus D proves (NS8) and the joint same-array
observation contract. At \(T_\epsilon\), the population reference tends
strongly to \(\theta_\dagger\). The forward field inequalities therefore
identify (NS9)'s limit with (NS7), using paired programs on the same initialized
arrays, followed only then by \(\epsilon\downarrow0\).

On the common bounded prediction region, squared loss at the one added atom
is continuous. Hence the probability that
\(R_{\nu}(F_*)-R_{\nu}(f_{n,\mu_\epsilon}(T_\epsilon))\ge a/2\)
and \(J_{2,n,\epsilon}\ge j/2\) tends to one in the displayed iterated order.
This verifies every assertion of the theorem. The state reconstruction retains
the evolving hidden features and actual adjoint throughout the episode.

