# Population slow selection from the original mixture initialization

Author: geometric-route agent, second-round synthesis. Date: 2026-09-12.
Status: theorem module using the frozen controlled source theorem in
CONTINUATION_CONTROL_TUBE.md, SHA-256
175492fdd14a51395187cb586f2aa63b634bd688a01cbd84f3a9a043efd06cbc.
That module was read completely after its freeze. The assembled proof still
requires its independent review; this document is not a target-completion claim.
The first-round ROUTE_GEOMETRIC.md remains frozen and is not used as a
population result. No experiment, finite-width endpoint assumption, staged
training procedure, or Git write is used here.

## 1. Model, carrier, and precise source-theorem dependency

Use the canonical Gaussian carrier and notation of C.4.7. The raw increment
space is

\[
 \mathcal E=L^2(\Omega_1;\mathbb R^2)
 \oplus\mathcal S_2(H_1,H_2)\oplus H_2,\qquad
 H_\ell=L^2(\Omega_\ell),\qquad \theta=(w,K,c),\quad A=A_0+K.
\]

The fixed initialized action has \(\|A_0\|_{\mathrm{op}}\le2\), and its
actual adjoint is retained. Initially \(\theta=(g,0,0)\), where the two
coordinates of \(g\) are independent standard normals. For \(\phi=\tanh\),

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad f_\theta(u)=\langle c,H^2(u)\rangle,
\]
\[
 \Delta(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta(u),\qquad
 g_u(\theta)=\big(\phi'(w\cdot u)Q(u)u,\,
                   \Delta(u)\otimes H^1(u),\,H^2(u)\big).
 \tag{1}
\]

Here \(g_u\) is the raw scalar prediction gradient, and
\((a\otimes b)v=a\langle b,v\rangle\). The scalar prediction is \(C^1\)
in the raw metric, with jointly continuous gradient. This is the scalar
statement of A.4 and C.4.7.2, not an ambient \(C^2\) assertion or a
Fréchet derivative assertion for an \(L^2\)-valued activation map.

Let

\[
 \mathcal P=I\times[3/8,5/8],\qquad
 I=[\pi/4-a,\pi/4+a],\quad 0<a<\pi/8,
 \quad u_\alpha=(\cos\alpha,\sin\alpha).
 \tag{2}
\]

The coordinator may decrease \(a>0\) to obtain its learning margins. Every
constant and time below is uniform on this compact parameter box. Its
relative interior gives an open single-added-atom family. Write \(p=(\alpha,y)\)
and \(\nu_p=\delta_{(u_\alpha,y)}\). Training is always from the original
initialization under

\[
 \mu_{\varepsilon,p}=(1-\varepsilon)\nu_*+\varepsilon\nu_p,\qquad
 \nu_*=\tfrac12\delta_{(e_1,1)}+\tfrac12\delta_{(e_2,-1)}.
\]

Physical inputs are \(x=\sqrt2u\). Finite stored variances are
\((1,1/n,1/n^2)\), mobilities are \((n,1,n)\), the output is divided by \(n\),
and loss is unhalved. The actual finite initial Gaussian readout is retained.

C.4.5.1 constructs the reference feature path \(\theta_*(s)\),
\(0\le s\le s_\dagger\le10\). It is exactly the controlled equation

\[
 \theta_s=\tfrac12g_{e_1}(\theta)-\tfrac12g_{e_2}(\theta).
 \tag{3}
\]

Its endpoint is denoted \(\theta_\dagger\). Its physical reference path
converges to this state with

\[
 \|\theta_*(t)-\theta_\dagger\|_{\rm raw}
 \le\sqrt{10}e^{-t/5},\qquad
 |r_*(t)|\le\sqrt2e^{-t/5}.
 \tag{4}
\]

In physical time its controls are \((-r_{*,1},-r_{*,2},0)\); their total
absolute mass is \(s_\dagger\), not an unbounded physical time horizon.

### SCT: exact interface supplied by the frozen controlled source theorem

Consider finite raw Euler programs from the prescribed initial carrier,
using the three inputs \(e_1,e_2,u_\alpha\) and signed scalar increments
\(\gamma_{kj}\):

\[
 \theta_{k+1}=\theta_k+\sum_{j=1}^3\gamma_{kj}g_{u_j}(\theta_k).
 \tag{5}
\]

The coefficients are deterministic population quantities at each already
constructed node. They may be feedback values computed from scalar
contractions, but are frozen when differentiating named source expressions,
exactly as in C.4.7.N2--N8. Both action orientations and all source corrections
remain those of the prescribed carrier.

Use deterministic signed controls on their original physical interval, and
compare with the physical reference controls
\(\bar a=(e_*(t),-e_*(t),0)\). The control distance is

\[
 \int |a-\bar a|_1\,dt\le\delta.
 \tag{6}
\]

One may equivalently use their exact integrated signed increments on a
common refinement. Mesh size means maximal mass of the dominating measure
\((|a|_1+|\bar a|_1)dt\), not physical time. A cell of
zero dominating mass causes no update. Nonzero added controls on a cell where
the reference control is zero keep their full mass in (6).

**SCT consequence of CT4--CT7.** There are \(\delta_{\rm src}>0\), \(h_{\rm src}>0\), and
\(B_{\rm src}<\infty\), uniform over \(\alpha\in I\), such that every finite
program (5) whose exhibited control distance to the physical reference
history is less than
\(\delta_{\rm src}\), and whose dominating control mesh is at most
\(h_{\rm src}\), has every named passive backward coefficient row bounded by
\(B_{\rm src}\). The bound holds at every node and every deterministic passive
input \(v\in S^1\), after appending its distinguished current query.
It is uniform over the number of instructions, the physical duration of the
schedule, covariance ranks, and reference-prefix length. The same bound, or
a fixed enlargement, applies to recomputed affine-interpolation queries.

The coefficient is exactly
\(\beta_{kv,q}=\mathbb E_2[\partial_{\xi_q}\Delta_k(v)]\) with the freezing
convention above, and the row includes its distinguished current slot and
all preceding training slots. It is not a derivative reconstructed from
values on a singular Gaussian support.

The endpoint interface is applied without independently reparameterizing the
reference. Follow its original control history through physical b, then append
arbitrary controls on \([b,b+\ell]\). On the latter interval compare them with
the still-running physical reference, using the triangle inequality:
their control distance is at most the reference tail mass after b plus the
appended absolute control mass. This also holds if controls are set to zero
after \(b+\ell\) and CT4 is evaluated on the full infinite physical interval.
Approximation errors of the reference prefix are included in (6), not dropped.

This is a control-history statement, not a claim that every point in an
ambient raw ball has Gaussian query tails. Its proof is CT10--CT45 of the
frozen continuation module, with its control-clock interpolation passage
CT46--CT47. This supplies uniformity in the three directions, zero-reference
added slots, and passive inputs. C.4.7.N-cap through physical time 40 is not
itself substituted for this proof.

The remaining infrastructure used below is already the fixed finite-program
construction, common-carrier realization, bounded initialized action,
one-reference comparison, and observation passage stated and proved in
A.1--A.4 and C.4.7.2, C.4.7.4--5. No long-time conclusion of those local
theorems is assumed.

## 2. Consequences of SCT and the one-reference modulus

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
 \Delta-\bar\Delta=(c-\bar c)\phi'(Z^2)
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

## 3. Endpoint conditioning and constrained coefficients

Let \(G(\theta):\mathbb R^2\to\mathcal E\) have columns \(g_{e_1},g_{e_2}\).
The endpoint Gram \(M_\dagger=G(\theta_\dagger)^*G(\theta_\dagger)\) is strictly
positive. This is the conditioning route's Lemma 4.1; the needed two-input
argument is short enough to record.

C.4.6.S43--44 give a common subGaussian envelope \(N\) and
\(|X_a|\le5N\) for the reference clocks
\(\mathcal F(w_a)=\mathcal F(g_a)+X_a\), \(\mathcal F'(z)=\cosh^2z\).
For \(v=(1,1)\) and \(v=(1,-1)\), the event
\(\{|g-rv|_\infty\le1,\ N\le r^2\}\) has positive probability for all large
\(r\): its Gaussian box probability is \(\exp[-O(r^2)]\), whereas
\(\Pr(N>r^2)\le C\exp(-cr^4)\). On that event the clock equation and the
mean-value formula give \(|w_a-g_a|\le C r^2e^{-cr}\). Hence a linear relation
\(\lambda_1H^1(e_1)+\lambda_2H^1(e_2)=0\) would imply both
\(\lambda_1+\lambda_2=0\) and \(\lambda_1-\lambda_2=0\). The two lower
features are independent in \(L^2\). Since \(f_\dagger(e_1)=1\),
\(c_\dagger\ne0\); strict positivity of the tanh gate makes each
\(\Delta_\dagger(e_a)\ne0\). Apply a supposed linear relation between the
middle ranks \(\Delta_a\otimes H^1_a\) to dual vectors in the span of the
two independent \(H^1_a\). Each coefficient must vanish. Thus the middle
gradient blocks, and therefore the full gradients, are independent.

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

## 4. Construction from reference prefixes, tails, and uniqueness

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

## 5. Strong activation derivatives and absolute continuity of B

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
 \Delta(v)'=c'\phi'(Z^2(v))+c\phi''(Z^2(v))(Z^2(v))',
\]
\[
 Q(v)'=K'^*\Delta(v)+A^*\Delta(v)'.
 \tag{24}
\]

These are strong \(L^2\) absolutely continuous identities and
\(\|Q(v)'\|_2+\|\Delta(v)'\|_2\le Cm(t)\). A direct justification, which
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
 (g_v)'_K=\Delta(v)'\otimes H^1(v)+\Delta(v)\otimes(H^1(v))',
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
coordinator's paired hidden-activation margin.

## 6. Actual original-mixture continuation in the control tube

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

### Fixed b prefix, before any changed-program cap

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

### Post-b discrete residual contraction and cap first exit

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

## 7. Residual identity and singular selection

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

## 8. Actual finite GF and joint hidden observations: width first

Here is the finite bridge required for (39). Fix p, then a sufficiently small
positive \(\varepsilon\). Its horizon \(T_\varepsilon=\tau_0/\varepsilon\)
is now a fixed finite number. The population construction above is completed
by finite raw Euler programs with deterministic population coefficients,
all in the SCT tube. For any target accuracy choose one such finite program
before sending width to infinity.

Realize it on the actual initialized arrays, expand each learned middle
increment as the finite sum of its assigned ranks, and add the actual finite
initial readout to the proxy readout. Both the proxy and actual finite GF
therefore begin from exactly the same arrays. C.4.7.5's fixed-program argument
and A.1 apply: bounded gates multiply named \(L^2\) fields, both orientations
use the same initialized matrix, and every learned contraction is a finite
sum of same-layer pairings. The initial readout RMS and supremum vanish in
probability; they are propagated as an additive proxy discrepancy, not set
to zero in the actual network.

At each fixed program and cutoff R, node fields and positive-part second
moments converge jointly. Equations (8) and (21) give proxy tails bounded by
\(Ce^{-cR^2}+o_{\mathbb P}(1)\). Actual finite GF has global existence by its
finite energy identity. At this fixed \(T_\varepsilon\), that identity gives
deterministic raw/action bounds on an initialization event with probability
tending to one. Those finite bounds may depend on \(\varepsilon\); no
width-uniform finite endpoint or all-time bound is needed.

Use the normalized same-carrier finite comparison of C.4.7.2, with the proxy
as the sole tail-bearing endpoint. Its raw distance to actual GF satisfies
the integrated estimate

\[
 \sup_{t\le T_\varepsilon}d_n(t)
 \le C_\varepsilon e^{C_\varepsilon(1+R)T_\varepsilon}
       \{(1+R)h+C e^{-cR^2}+o_{\mathbb P}(1)\}.
 \tag{40}
\]

The \(h\) term includes the proxy node/interpolation defect; any fixed-program
feedback consistency error is included in \(o_{\mathbb P}(1)\).
For required accuracy, first choose R so large that its Gaussian tail
dominates the linear-in-R exponent, then choose the finite mesh sufficiently
fine, and only then let \(n\to\infty\). This is legitimate for every fixed
\(\varepsilon\), however large its fixed \(T_\varepsilon\). No increasing
transcript is submitted to a fixed-program theorem.

The population proxy approximates its completed path in raw norm.
Uniform forward/prediction bounds and finite time/input nets therefore give

\[
 \sup_{t\le T_\varepsilon,v\in S^1}
 |f_{n,\mu_{\varepsilon,p}}(t,\sqrt2v)
               -f_{\theta_{\varepsilon,p}(t)}(v)|
 \longrightarrow0\quad\text{in probability}.
 \tag{41}
\]

The state assertion has exactly C.4.7's finite-proxy meaning: a finite matrix
is never subtracted from a population operator on another carrier.
At each fixed program, Hilbert--Schmidt pairings use
\(\langle a\otimes b,\tilde a\otimes\tilde b\rangle
=\langle a,\tilde a\rangle\langle b,\tilde b\rangle\), and finite Frobenius
pairings have the same normalized two-population contraction.

For any fixed finite observation list, include the reference history and
the mixture history on the same initialized arrays and in one finite union
of their fixed programs. C.4.7.5's observation induction then captures their
joint within-layer empirical laws with second moments. Applying bounded
actions, bounded continuous gates to named \(L^2\) fields, and the correctly
typed quadratic contractions preserves the comparison. In particular it
captures

\[
 {1\over n}\|h^\ell_{n,\mu_{\varepsilon,p}}(t,\sqrt2v)
                -h^\ell_{n,\nu_*}(t,\sqrt2v)\|_2^2
\]

with the same neuron indices and initialization. For these activation
observables, forward Lipschitz and state-speed bounds extend the convergence
uniformly over compact time/input sets at each fixed \(\varepsilon\).
This requires joint programs, not a coupling chosen between two marginal
limits. No arbitrary unbounded product is admitted by this observation step.

Combining (39) and (41), for each fixed p and every \(\eta>0\),

\[
 \lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}
 \Pr\left\{\sup_{\tau_{\min}\le\tau\le\tau_0,\ v\in S^1}
 |f_{n,\mu_{\varepsilon,p}}(\tau/\varepsilon,\sqrt2v)
                      -P_p(\tau,\sqrt2v)|>\eta\right\}=0.
 \tag{42}
\]

The analogous iterated conclusion holds for the paired hidden activations
against the actual reference at the same physical times, with limiting
displacement from \(H^\ell_{\theta_\dagger}\) to
\(H^\ell_{\bar\theta_p(\tau)}\).
The population statement (39) is uniform over p. Equation (42) is a
separately fixed-law probability statement; no supremum of failure
probabilities over all p and no simultaneous \(n,\varepsilon\) rate is claimed.

This also gives finite-program capture in the established
approximation sense: for a fixed episode, law, and requested accuracy,
choose a finite reference-prefix program and a finite constrained Euler
program before the width limit. It is not an exact finite-dimensional
scalar closure of the complete latent state.

## 9. Scope, remaining check, and source record

Using SCT as supplied by the frozen continuation module, this module proves
a unique, determining constrained population trajectory, construction from
the actual reference endpoint,
the original-mixture singular limit, and the width-first finite-GF bridge,
with joint hidden observations and no finite-width endpoint assumption.
Its risk identity is

\[
 {d\over d\tau}R_{\nu_p}(\bar\theta_p(\tau))
       =-4\|\Pi(\bar\theta_p(\tau))v_p(\bar\theta_p(\tau))\|_{\rm raw}^2.
\]

The coordinator separately supplies the uniform nonzero learning and hidden
activation margins for the single-added-atom family. This module supplies
their needed joint derivative continuity, but does not claim completion of
the target before the assembled proof and its dependencies pass the required
independent checks.

There is no additional source estimate assumed in this module: CT4--CT7 and
CT46--CT47 give the interface used here, and (32a)--(33) verify it for the
actual-feedback Euler programs before completion. The physical reference
continues after each prefix; its full remaining control mass is included.
The derivative argument needs only the resulting fourth moments and bounded
readout. A cap only through physical time 40, or only for already existing
changed trajectories, would not have sufficed. Gaussian tails have not been
inferred from bounded raw norms alone.

Scientific sources read for this second-round module:

* ROUTE_RESIDUAL_CLOCK.md and ROUTE_CONDITIONING.md completely; truncated
  portions of the latter were repaired by focused reads.
* CONTINUATION_CONTROL_TUBE.md completely after its freeze, at the hash
  recorded at the start of this module. The endpoint application was checked
  against its actual physical-reference condition CT4.
* docs/NOTATION.md completely.
* docs/global_nonlinear.md lines 1840--1898 (A.1--A.4);
  5269--5781 (C.4.5 statement and complete reference construction through
  endpoint/prediction); 7651--7818 and 8141--8425 (C.4.6 source statement,
  deterministic equations, full bounded-feature source completion,
  continuity, and observation identification); 8977--9611,
  10027--10553 (C.4.7 model, comparison, source equations and conditional-cap
  consequences, reference anchor, complete strong completion and finite
  observation bridge); 11440--11823 (C.4.8 model and finite-source recursion,
  including the full fixed-order frozen-source argument).

The omitted C.4.7 coefficient-transport/mesh-defect proof is not independently
claimed here as a proof of SCT; the frozen continuation module supplies the
complete new control argument, and the coordinator audits its established
dependencies. C.4.8's statistical theorem and mass-response calculus are
not used to extend any time horizon. The foundational fixed-program inputs
are consumed through the complete stated bridge and its supplied argument;
their separate full book audit is the coordinator's responsibility.
No other study, prior task, external scientific source, maintained API, or
unlisted author artifact was used. Required math/research skills and their
applicable process references were already read in the first round.
