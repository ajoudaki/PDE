# A weak nonlinear reinsertion remainder from an ordinary energy estimate

2026-10-01. Scoped theoretical continuation. Scientific inputs are the complete
`BIAS_CAVITY_ROUTE.md`, `RESOLUTION_UPPER_ROUTE.md`,
`FITTING_AND_THRESHOLD.md`, and `CONCENTRATION_ROUTE.md` in this study. The
solve-math-rigorously and investigate-conjectures skills and their contract/audit
references were applied. No other study, sibling route, experiment, Git
operation, or manuscript edit was used.

**Result.** Assuming the actual row-cavity near-cap estimate stated in
`RESOLUTION_UPPER_ROUTE.md`, the first-moment weighted nonlinear reinsertion
estimate (20) of that report follows. The estimate is uniform over every
measurable removed-row path bounded by a fixed multiple of cavity activity.
On a simultaneous fitting event this includes the actual causal row path
through comparability of full and cavity activities. Its proof
keeps the same matrix and transpose and the hard clip. It does not make a
nonlinear propagator independent of the removed Gaussian row.

The key is to use the ordinary remainder estimate
\(\mathbb E\sup_t\|R(t)\|_2^2=O(n^{-1/2})\) as an **energy** estimate. Its
square root is only \(O(n^{-1/4})\), but the weak Taylor argument needs the
energy itself. A scalar inequality puts the nonlinear input error into this
quadratic term and puts every remaining cap event on a cavity Gaussian
adjoint or a tangent envelope.

This proves a frozen-coefficient weak response estimate, not the requested
population theorem. Restoring empirical scalar histories and comparing the
resulting response/covariance laws with the own clipped population remain
separate obligations. An RMS version of this intermediate row estimate is not
proved and is not needed merely to bound a deterministic prediction bias.

## 1. Exact object, event, and statement

Fix the deleted upper row i, put \(W=W_0^{(i)}\), and write the independent
removed row as \(\omega\sim N(0,I_n/n)\). The cavity sigma-field \(\mathcal A\)
contains \(A_0,W\). Freeze the scalar histories
\(r_a,\rho,\tau,K_{ba},V_{ba}\) at their actual row-cavity values. In particular,
\(s(t)=\int_0^t\rho\), \(\tau=1+s\), \(|K_{ba}|\le1\), and
\(|V_{ba}|\le Cs^3\). The forced equations are exactly those of Section 4 of
`BIAS_CAVITY_ROUTE.md`:

\[
\begin{aligned}
 \alpha_a&=Au_a,& h_a&=\tanh\alpha_a,\\
 z_a&=Wh_a+m^{-1}\sum_bv_bK_{ba},&
 d_a&=C_M(w\odot\psi(z_a)),\\
 p_a&=W^Td_a+\omega\eta_a+m^{-1}\sum_bk_bV_{ba},&
 \ell_a&=C_M(\psi(\alpha_a)\odot p_a),
\end{aligned}
\tag{1}
\]

with the absent upper coordinate omitted in the W action, and

\[
 \dot A=-\frac2m\sum_a r_a\ell_a u_a^T,
 \quad \dot w=-\frac2m\sum_a r_a\tanh z_a,
 \quad \dot v_a=-2r_ad_a,
 \quad \dot k_a=\frac\rho\tau(h_a-k_a).
\tag{2}
\]

Here \(\psi=\operatorname{sech}^2\), M is a fixed positive cap, and all norms on
these vector states are ordinary, unnormalized Euclidean/Frobenius norms.
The dimensions d and m are fixed. Write \(U=(A,w,(v_a),(k_a))\), as a vector
in \(\mathbb R^{N_n}\), where \(N_n\le Cn\). At \(\omega=0\), (1)–(2) are
the actual cavity trajectory \(U^c\), independently of eta.

Use a common cavity event \(\mathcal C\in\mathcal A\) on which

\[
 \|W\|_{op}\le K,\qquad
 \rho(t)\le\bar\rho(t):=Y e^{-\kappa t},\qquad
 s(\infty)\le S_*<M/4.
\tag{3}
\]

For every lower gate carrier of the cavity, write
\(X_{aj}^c(t)=\psi(\alpha_{aj}^c(t))p_{aj}^c(t)\). The probabilistic input is

\[
 \mathbb P\bigl(\mathcal C\cap
 \{\operatorname{dist}(X_{aj}^c(t),\{-M,M\})\le u\}\bigr)
 \le C_0u
 \quad (u>0),
\tag{4}
\]

uniformly in a,j,t,n. The upper-route proposition, with one upper row already
deleted and its common good event, supplies (4) for M=1. The same proof below
applies to another fixed M whenever (4) has been established at that cap.
The event is independent of omega. No conditional independence after
conditioning on a full, non-cavity good event is assumed. The initial Gram
margin and the fixed small-label hypothesis are those needed for (3) and (4).

An expectation with subscript \(\mathcal C\) means
\(\mathbb E_{\mathcal C}Z=\mathbb E[\mathbf1_{\mathcal C}Z]\); it is not a
conditional expectation. If \(\mathbb P(\mathcal C)\) is bounded below, the
same bounds hold conditionally on \(\mathcal C\), after changing constants.

Fix \(0<C_\eta<\infty\). Allow eta to be **any** jointly measurable function of
cavity roots, omega, and time satisfying
\(|\eta_a(t)|\le C_\eta s(t)\), where s is the **cavity** activity. Causality
is not needed for the estimate. The frozen-coefficient single-row histories
satisfy this with \(C_\eta=2\). When constructing
the first tangent \(T[\eta](t)\), hold this realized history fixed and
differentiate the forced solution at zero row. Thus the notation does not
differentiate the map \(\omega\mapsto\eta(\omega)\).

For \(H_a(U)=\tanh(Au_a)\), the conclusion is

\[
 \mathbb E_{\mathcal C}\sup_{t\ge0}
 \left|\omega^T\left[
 H_a(U(t;\omega,\eta(\omega)))-H_a(U^c(t))
       -D H_a(U^c(t))T[\eta(\omega)](t)\right]\right|
 \le\frac C{\sqrt n}.
\tag{5}
\]

The constant is uniform over these measurable choices of eta and over
physical time. It can depend on \(C_\eta\), fixed data, cap, activity bound,
gap, and operator cutoff. Labels are fixed independently of width.

For the full actual row, the direct bound is
\(|d_{ai}^{\rm full}(t)|\le2s_{\rm full}(t)\), which need not be at most
\(2s(t)\). On a simultaneous full/cavity fitting event, the residual speed
bound \(\|\dot r\|_m\le C\rho\) and exponential fitting give
\(cY\min(t,1)\le s(t)\) and
\(s_{\rm full}(t)\le CY\min(t,1)\). Thus
\(s_{\rm full}(t)\le C_{\rm act}s(t)\), with a fixed constant, and the full
actual path qualifies with \(C_\eta=2C_{\rm act}\). For Y=0 both paths vanish.
If needed, extend this path off the simultaneous event by clipping it to
\([-C_\eta s(t),C_\eta s(t)]\). The extension obeys the theorem everywhere
on \(\mathcal C\) and agrees with the actual path on that event; restricting
the nonnegative estimate (5) to the event is then legitimate without any
Gaussian conditioning on it. Throughout this substitution **the scalar
coefficient histories in (1)–(2) remain frozen at cavity values**. Restoring
their full actual values is not part of (5).

## 2. A local inequality for the actual clipped gate

Both scalar nonlinearities used in (1) have the following useful structure.
For tanh, its Taylor defect at an increment u obeys

\[
 |\tanh(x+u)-\tanh x-\psi(x)u|
 \le C\min(u^2,|u|).
\tag{6}
\]

This follows from its bounded first and second derivatives: the two separate
bounds are \(2|u|\) and \(u^2\).

For the exact post-gate clip set
\(F(x,p)=C_M(p\psi(x))\), \(X=p\psi(x)\),
\(d_X=\operatorname{dist}(X,\{-M,M\})\), and \(D=|u|+|v|\). At a base
point off the two corners, let

\[
 q_F=F(x+u,p+v)-F(x,p)-D F(x,p)(u,v).
\]

Then, with constants depending only on fixed M,

\[
 |q_F|\le C_M\left[
       \min(D^2,D)+D\mathbf1_{\{d_X\le C_MD\}}\right].
\tag{7}
\]

Here is a proof that does not assume a bound on the uncut carrier p. The
global inequality \(|F(x+u,p+v)-F(x,p)|\le2M|u|+|v|\) also bounds its weak
first derivatives; hence \(|q_F|\le C_MD\). Choose a sufficiently small
fixed \(\delta_M>0\). For \(D\ge\delta_M\), this global bound is at most
\(C_M\min(D^2,D)\). Suppose \(D<\delta_M\). Since

\[
 |\log\psi(x+u)-\log\psi(x)|\le2|u|,
\tag{8}
\]

if \(|X|>2M\), decreasing \(\delta_M\) ensures that both carriers stay
saturated on the same side. In that case the defect is zero. If
\(|X|\le2M\), relative derivative bounds
\(|\psi'|\le2\psi\), \(|\psi''|\le C\psi\), and (8) give

\[
 \psi(x+u)(p+v)-X
 =p\psi'(x)u+\psi(x)v+e,
 \qquad |e|\le C_MD^2,
\]

and the entire carrier increment has magnitude at most \(C_MD\).
The scalar clip defect for an increment q is bounded by
\(|q|\mathbf1_{\{d_X\le|q|\}}\), by integrating its piecewise constant
slope along the increment. Adding the error e proves (7).

The estimate remains valid with either bounded one-sided derivative at a
corner. More importantly, (4), Fubini on each finite time interval, and a
countable union show that almost every cavity realization encounters a
corner on a time set of measure zero. Thus its ordinary variational equation
can use the actual derivative almost everywhere in time.

## 3. Gaussian moment envelopes do survive adaptive eta

The vector field in (2), after inserting (1), is globally Lipschitz in U,
with Lipschitz coefficient at most \(C\rho(t)\), uniformly in omega and eta.
To check this, the linear maps use only bounded W,K,V and fixed u; tanh is
globally Lipschitz; and the two clipped gates obey the global inequality used
above. This estimate does not require the shifted state to stay inside the
actual small-activity tube. The row forcing changes p additively by
\(\omega\eta_a\), and introduces no state derivative depending on omega.
Consequently measurable eta defines a global Caratheodory solution with
integrable difference bounds.

In particular, comparison with zero forcing gives
\(\sup_t\|U(t)-U^c(t)\|_2\le C\|\omega\|_2\); the same bound holds for the
linear tangent below. Hence all scalar weighted remainders considered here
are dominated by a constant times \(\|\omega\|_2^2\). The uses of Tonelli,
Minkowski, and integral variation of constants are therefore legitimate;
stronger moment estimates below improve this initial integrable domination.

Linearize the complete finite directed graph of operations in (1)–(2) about
the cavity. Its state tangent solves

\[
 \dot T=L(t)T+\sum_b r_b(t)B_b(t)\omega\eta_b(t),
 \qquad T(0)=0,
 \qquad \|L(t)\|_{op}\le C\rho(t),\quad\|B_b(t)\|_{op}\le C.
\tag{9}
\]

All matrices are cavity measurable. Clip selectors occur in L and B but
their time derivatives are not taken. If P is the evolution of L, then

\[
 T(t)=\sum_b\int_0^t
 P(t,s)B_b(s)\omega\eta_b(s)r_b(s)\,ds,
 \quad\|P(t,s)\|_{op}\le e^{C S_*}.
\tag{10}
\]

This is the first tangent of the nonlinear solution, rather than only a
formal linear equation. For fixed realized eta, compare the solution forced
by \(\lambda\omega\eta\) with the cavity. Its difference divided by lambda
is bounded uniformly in time by \(C\|\omega\|_2\). At almost every time the
base graph is differentiable, by the corner-null statement after (8), so its
linearization error divided by lambda tends to zero. It is dominated by
\(C\rho(t)\|\omega\|_2\), an integrable function. Dominated convergence in
the integral equation and Gronwall therefore identify the limit with (9).

For any deterministic row vector q, conditional Gaussian integration gives
\(\|q\omega\|_{L^p_\omega}\le C\sqrt p\|q\|_2/\sqrt n\) for \(p\ge1\).
Take absolute values inside (10) before using \(|\eta_b|\le C_\eta s\), and apply
Minkowski. Thus every coordinate of T is bounded in magnitude by a
nonnegative, cavity-dependent random envelope with conditional moments
\(C\sqrt p/\sqrt n\), **uniformly over all allowed eta**.

The same bound holds for the supremum over terminal time of each state
coordinate. In fact, for a source time s,

\[
 \sup_{t\ge s}|e_j^TP(t,s)B_b(s)\omega|
 \le |e_j^TB_b(s)\omega|
 +\int_s^\infty|e_j^TL(t)P(t,s)B_b(s)\omega|\,dt.
\tag{11}
\]

The conditional \(L^p\) norm of the right side is at most
\(C\sqrt p/\sqrt n\), because \(\int\|L(t)\|_{op}dt\le CS_*\).
Insert (11) into the absolute integral in (10). This gives a common envelope
\(\mathcal T_j\) with

\[
 \sup_t|T_j(t)|\le\mathcal T_j,
 \qquad
 \|\mathcal T_j\|_{L^p_\omega}\le C\sqrt p/\sqrt n.
\tag{12}
\]

For every algebraic node in (1), its linearized input at a fixed time is a
bounded cavity linear map of T plus bounded multiples of omega. To obtain
the coordinate moment bound for such a map Q(t), insert (10) directly:
the j-th coordinate has kernels
\(e_j^TQ(t)P(t,s)B_b(s)\), whose Euclidean row norms are bounded uniformly.
Take absolute values before eta and apply the Gaussian projection bound and
Minkowski to these kernels. This gives the same conditional moment envelope;
it does **not** follow by summing individual coordinate envelopes through an
operator norm. The term \(\eta_a(t)\omega_j\) is bounded directly by
\(C_\eta S_*|\omega_j|\).
No time variation of eta or of a source-time selector is required. For these
algebraic nodes only the fixed-time estimate is used; bounded variation of
every algebraic tangent coefficient is not asserted.

The moments in (12) imply conditional sub-Gaussian tail bounds for the
envelopes. For example, Markov with integer \(p\) proportional to \(n u^2\)
gives \(\mathbb P_\omega(\mathcal T_j>u)\le C e^{-cnu^2}\), with the bound
made trivial when u is below a fixed multiple of \(n^{-1/2}\).

## 4. The ordinary energy estimate

Write \(\Delta=U-U^c\) and \(R=\Delta-T\). First consider a local activation
defect evaluated at its *pure linearized input*, rather than its actual input.
Let V be the sum of the absolute values of the at most two tangent input
coordinates of that activation. It has the conditional moment envelope just
proved. Equation (7) gives

\[
 |q^{\rm tan}|^2\le C[V^4+V^2\mathbf1_{\{d_X\le CV\}}].
\tag{13}
\]

Conditional Cauchy–Schwarz and the envelope tail give

\[
 \mathbb E_\omega[V^2\mathbf1_{\{d_X\le CV\}}\mid\mathcal A]
 \le\frac Cn e^{-cn d_X^2}.
\tag{14}
\]

For a lower gate, (4) implies

\[
 \mathbb E_{\mathcal C}e^{-cn d_X^2}
 =\mathbb E_{\mathcal C}\int_{d_X}^{\infty}
                 2cn u e^{-cnu^2}\,du
 \le C\int_0^\infty n u^2e^{-cnu^2}\,du
 \le Cn^{-1/2}.
\tag{15}
\]

Thus each squared lower-gate defect has expectation at most \(Cn^{-3/2}\).
For an upper gate, its base carrier has magnitude at most \(2S_*<M/2\), so
its distance to the caps is at least M/2. Equation (14) then gives an
exponentially small corner term and the smooth term is \(O(n^{-2})\).
For tanh, the squared defect is also \(O(n^{-2})\) by (6). There are at most
Cn scalar activation nodes, so for each finite list of vector activation
defects,

\[
 \mathbb E_{\mathcal C}\|q^{\rm tan}(t)\|_2^2
 \le Cn^{-1/2}
\tag{16}
\]

uniformly in time and in the selected adaptive eta.

To transfer this to the whole vector field, evaluate its nonlinear graph at
the shifted state \(U^c+T\) and the same forced input \(\omega\eta\). Compare
this evaluation with the graph obtained by linearizing every node. At a
linear node the difference is a bounded linear map of preceding errors. At
an activation node, add and subtract the activation evaluated at its pure
tangent input: its global Lipschitz bound propagates preceding errors, while
the new source is precisely the defect in (13). Induction over the fixed
finite graph gives

\[
 \|F_t(U^c+T,\omega\eta)-F_t(U^c,0)
                   -L(t)T-\text{row tangent forcing}\|_2
 \le C\rho(t)\sum_v\|q_v^{\rm tan}(t)\|_2.
\tag{17}
\]

Here \(F_t\) denotes the actual right side of (2), and v runs over a fixed
number of vector activation types. The number of graph operations is
independent of n. The global Lipschitz bound for \(F_t\) now gives

\[
 \sup_{t\ge0}\|R(t)\|_2
 \le C\int_0^\infty\rho(s)
                         \sum_v\|q_v^{\rm tan}(s)\|_2\,ds.
\tag{18}
\]

Use the deterministic envelope \(\rho\le\bar\rho\) in (3), Minkowski in
\(L^2\), and (16). Since \(\int\bar\rho<\infty\),

\[
 \mathbb E_{\mathcal C}\sup_{t\ge0}\|R(t)\|_2^2
 \le Cn^{-1/2}.
\tag{19}
\]

The same graph comparison implies a fixed-time version for every algebraic
input: if its actual increment is its tangent increment plus E, then

\[
 \mathbb E_{\mathcal C}\|E(t)\|_2^2\le Cn^{-1/2}.
\tag{20}
\]

Indeed its error is bounded by \(C\|R(t)\|_2\) plus a fixed sum of
\(\|q_v^{\rm tan}(t)\|_2\), by the preceding graph induction. This proves
(20) from (16) and (19); it does not assume coordinate delocalization of the
nonlinear error.

## 5. The scalar inequality that converts energy to a weak bound

Let a be a nonnegative weight, let t be the sum of the absolute tangent input
coordinates, and let e be the corresponding sum for the nonlinear input
error. Thus the total input size D is at most \(t+e\). Applied to (7), the
following completely deterministic bound is sufficient:

\[
 a|q_F|\le C\left[
 e^2+a t^2+a^3
 +a t\mathbf1_{\{d_X\le Ct\}}
 +a^2\mathbf1_{\{d_X\le Ca\}}\right].
\tag{21}
\]

For tanh, the same bound holds without either cap term. To verify (21), put
\(h(u)=\min(u^2,u)\). Then
\(h(t+e)\le2h(t)+2h(e)\),
\(a h(t)\le a t^2\), and

\[
 a h(e)\le e^2+a^3.
\tag{22}
\]

For (22), if \(a\le1\), use \(ah(e)\le e^2\). If \(a>1\) and \(e\ge a\),
use \(ah(e)=ae\le e^2\). If \(a>1\) and \(e<a\), use \(ah(e)\le ae^2<a^3\).
For the corner term, the larger of t,e gives

\[
 (t+e)\mathbf1_{\{d_X\le C(t+e)\}}
 \le2t\mathbf1_{\{d_X\le2Ct\}}
       +2e\mathbf1_{\{d_X\le2Ce\}}.
\]

Split the last term according to \(e\ge a\) or \(e<a\):

\[
 ae\mathbf1_{\{d_X\le2Ce\}}
 \le e^2+a^2\mathbf1_{\{d_X\le2Ca\}}.
\tag{23}
\]

Combining these inequalities proves (21). No independence, smallness, or
Gaussianity of e is required.

Suppose now that a and t have conditional moment bounds
\(\|a\|_{L^p_\omega}+\|t\|_{L^p_\omega}\le C\sqrt p/\sqrt n\), and that
the base carrier satisfies (4). Their dependence on each other is arbitrary.
Conditional Hölder gives
\(\mathbb E_\omega(at^2+a^3)\le Cn^{-3/2}\).
Conditional Cauchy–Schwarz and their tail bounds give

\[
 \mathbb E_\omega[
 at\mathbf1_{\{d_X\le Ct\}}+
 a^2\mathbf1_{\{d_X\le Ca\}}\mid\mathcal A]
 \le Cn^{-1}e^{-cn d_X^2}.
\tag{24}
\]

Using (15), summing over at most Cn coordinates, and using (20), equation
(21) therefore yields

\[
 \mathbb E_{\mathcal C}\sum_j a_j|q_{F,j}(t)|
 \le Cn^{-1/2}.
\tag{25}
\]

Upper-gate corner terms again have a fixed base separation from the caps;
their contribution in (24) is exponentially small. Thus (25) holds for all
activation types in the exact graph. This is where the ordinary
\(n^{-1/4}\) remainder norm becomes useful: its squared norm appears in
(21), with exactly the required \(n^{-1/2}\) scale.

## 6. Cavity adjoints and the actual nonlinear remainder

There is an exact alternative expansion of the graph using local defects at
the **actual** input increments. At every activation write its increment as
its base derivative times its input increment plus its local Taylor defect
q. Propagate these identities through the finite graph, using the base
derivatives for the linear part. This gives the exact state identity

\[
 \dot R=L(t)R+\rho(t)\sum_v M_v(t)q_v(t),
 \qquad R(0)=0,
 \qquad\|M_v(t)\|_{op}\le C.
\tag{26}
\]

Every \(M_v\) is cavity measurable: products of base derivatives, W or
\(W^T\), and the frozen scalar coefficients. Ratios \(r_a/\rho\) are bounded
by \(\sqrt m\); at \(\rho=0\) define the unused M to be zero. The local q
are the only nonlinear row-dependent factors. Formula (26) is algebraic
variation of constants about the cavity, not a declaration that an actual
nonlinear propagator is independent of omega.

For the feature output write

\[
 H_a(U)-H_a(U^c)-D H_a(U^c)T
 =D H_a(U^c)R+q_{H_a}.
\tag{27}
\]

The propagated part of its weighted scalar remainder is

\[
 \omega^TD H_a(U^c(t))R(t)
 =\sum_v\int_0^t\rho(s)
   a_v(t,s)^Tq_v(s)\,ds,
 \quad
 a_v(t,s)=M_v(s)^TP(t,s)^TD H_a(U^c(t))^T\omega.
\tag{28}
\]

For each source coordinate j define
\(A_{v,j}(s)=\sup_{t\ge s}|a_{v,j}(t,s)|\).
Conditional on the cavity, the integrand in (28) is linear in omega before
taking its absolute supremum. Moreover its matrix coefficient has bounded
initial operator norm and integrable terminal-time variation. Indeed,
\(\partial_tP=L(t)P\) with \(\|L(t)\|_{op}\le C\rho(t)\), while
\(D H_a\) is a diagonal gate followed by the fixed input map and

\[
 \left\|\frac d{dt}D H_a(U^c(t))\right\|_{op}\le C\rho(t).
\tag{29}
\]

To check (29), each row of \(\dot A^c\) is bounded by \(C\rho\), because the
lower signal is clipped by fixed M. Since \(\psi'\) is bounded, the claimed
operator estimate follows coordinatewise. No derivative of \(M_v(s)\), or
of its source-time selectors, is taken. The argument of (11) now proves

\[
 \|A_{v,j}(s)\|_{L^p_\omega}\le C\sqrt p/\sqrt n.
\tag{30}
\]

Use (25) with the weights (30), take the temporal supremum in (28) by an
absolute integral, and bound \(\rho\le\bar\rho\). This yields

\[
 \mathbb E_{\mathcal C}\sup_t
 |\omega^TD H_a(U^c(t))R(t)|
 \le C\int_0^\infty\bar\rho(s)n^{-1/2}\,ds
 \le Cn^{-1/2}.
\tag{31}
\]

Finally, \(q_{H_a}\) is the direct tanh defect with input
\(\Delta A u_a=T_Au_a+R_Au_a\). Apply the cap-free form of (21) with
\(a_j=|\omega_j|\), using the state tangent supremum envelopes (12), and
then take the supremum in time. The error term is bounded by
\(C\sup_t\|R_A(t)\|_F^2\); the other terms have expectation

\[
 \sum_j\mathbb E_\omega\left[
 |\omega_j|\Big(\sup_t|(T_A(t)u_a)_j|\Big)^2+|\omega_j|^3
 \mid\mathcal A\right]\le Cn^{-1/2}.
\]

Thus (19) gives
\(\mathbb E_{\mathcal C}\sup_t|\omega^Tq_{H_a}(t)|\le Cn^{-1/2}\).
Together with (27) and (31), this proves (5).

## 7. The adaptive linear term, for completeness

The first-order scalar response has the cavity-kernel representation

\[
 \omega^TD H_a(U^c(t))T(t)
 =\sum_b\int_0^t\eta_b(s)r_b(s)\omega^TK_b(t,s)\omega\,ds.
\]

The same evolution/output argument gives
\(\|K_b(s,s)\|_{op}+\int_s^\infty\|\partial_tK_b(t,s)\|_{op}dt\le C\).
For a fixed real matrix K, direct Gaussian second/fourth moment expansion
gives

\[
 \mathbb E_\omega\left|\omega^TK\omega-\frac{\operatorname{tr}K}{n}\right|^2
 =\frac{\operatorname{tr}(KK^T)+\operatorname{tr}(K^2)}{n^2}
 \le\frac{2\|K\|_{op}^2}{n}.
\]

Apply this at terminal time s and to its terminal-time derivative, and use
Minkowski. Then take absolute values before bounding eta. Uniformly over
the same adaptive choices,

\[
 \left\|\sup_t\left|
 \omega^TD H_a(U^c(t))T(t)
 -\sum_b\int_0^t\eta_b(s)r_b(s)
              \frac{\operatorname{tr}K_b(t,s)}n\,ds
 \right|\right\|_{L^2_\omega}
 \le\frac{CS_*^2}{\sqrt n}
\tag{32}
\]

on every good cavity realization. Thus the adaptive linear term and the
weak nonlinear estimate (5) can both be used without conditioning on the
realized eta as though that conditioning preserved the Gaussian law.

## 8. Why no RMS upgrade is claimed from one-point density alone

Here is a complete counterexample to that particular inference, using the
same scalar hard clip. It is **not** a reachable-state example for the neural
closure and is not a prediction lower bound.

Take M=1, independent \(U\sim\operatorname{Unif}[0,1/4]\), and
\(\omega_j=G_j/\sqrt n\) with iid standard Gaussian G. Let every base carrier
be \(X_j=1+U\) and every tangent increment be \(\delta_j=\omega_j\). The
base clip derivative is zero almost surely. Every marginal obeys
\(\mathbb P(\operatorname{dist}(X_j,\{-1,1\})\le u)\le4u\); the tangent
and weight are jointly Gaussian conditional on U. Set

\[
 Z_n=\sum_{j=1}^n\omega_j[C_1(1+U+\omega_j)-1].
\tag{33}
\]

Every summand is nonnegative: a positive row entry leaves the clip at 1;
a negative row entry multiplies a nonpositive clip change. For n sufficiently
large, on \(0<U\le(2\sqrt n)^{-1}\) and \(-2\le G_j\le-1\), the lower cap
is not reached and

\[
 \omega_j[C_1(1+U+\omega_j)-1]
 =\frac{G_j(G_j+\sqrt n U)}n\ge\frac1{2n}.
\]

Let \(p_0=\mathbb P(-2\le G\le-1)>0\). The number N of such coordinates has
mean \(np_0\) and variance \(np_0(1-p_0)\), so Chebyshev gives
\(\mathbb P(N\ge np_0/2)\ge1/2\) for all sufficiently large n. It is
independent of U. Since
\(\mathbb P(0<U\le(2\sqrt n)^{-1})=2/\sqrt n\), equation (33) yields

\[
 \mathbb E Z_n^2\ge\frac{c}{\sqrt n},
 \qquad \|Z_n\|_{L^2}\ge c n^{-1/4}.
\tag{34}
\]

Nevertheless its first moment is root width. The scalar clip remainder bound
gives
\(Z_n\le\sum_j\omega_j^2\mathbf1_{\{U\le|\omega_j|\}}\), hence independence
of U and omega implies

\[
 \mathbb E Z_n\le4\sum_j\mathbb E|\omega_j|^3
 \le Cn^{-1/2}.
\tag{35}
\]

The shared random distance U allows all coordinates to approach a cap
together. Pair near-cap control or a separate response-mean concentration
argument could exclude this in the actual system, but one-point density
does not. This only limits an unnecessary strengthening of (5). The actual
deterministic prediction-bias route may use the L1 estimate proved above,
combined with its separately established centered prediction concentration.

## 9. Status and remaining boundary

- **Proved from the stated cavity near-cap input:** (5), the all-time weak
  nonlinear reinsertion estimate, uniformly over bounded adaptive eta;
  (19), the ordinary remainder energy estimate; and (32), adaptive linear
  response concentration.
- **Scientific dependency:** the exact common-event near-cap estimate (4)
  for the actual row cavity, as supplied by `RESOLUTION_UPPER_ROUTE.md`.
  This report does not independently reprove that proposition.
- **Not assumed:** Gaussianity of actual nonlinear increments, independence
  of a nonlinear propagator, a fresh backward matrix, differentiable hard
  clipping, a history-Gram inverse, or labels that shrink with width.
- **Still open here:** quantitative restoration of actual empirical scalar
  histories and identification/bias of the retained joint response/covariance
  law relative to the own clipped population.
- **Not concluded:** an RMS bound for this individual nonlinear row remainder,
  or the full population prediction theorem. Equation (34) is solely a
  counterexample to an inference from one-point near-cap assumptions.

The result advances one necessary weak source estimate. It should not be
promoted to a population rate until the remaining source-law comparison is
proved for the original clipped dynamics.
