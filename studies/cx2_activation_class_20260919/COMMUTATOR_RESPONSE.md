# A commutator response candidate for bounded C1,1 activations

Status: **candidate proof, pending independent audit**. This is a scoped
author derivation, not established material or a promotion proposal. Its
central new claim is the artificial tangent/source identification in §4.
Every downstream conclusion depends on that claim. No experiment was run.

The proposed conclusion is: for each bounded nonaffine
`phi in C1,1(R)`, with bounded derivative and globally Lipschitz derivative,
and each fixed finite T, there is a positive gamma_*(phi,T) such that the
exact two-hidden-layer Gaussian-action flow exists strongly through T for
two unit normalized inputs with `|u1.u2|<gamma_*`, equal masses and labels
`(+1,-1)`. It has uniform exponential (indeed Gaussian) reverse-field
tails in that family. At the reference fitting horizon, shrinking the
radius gives loss below 1/4. The architecture, stored variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved mean loss, actual Gaussian
action/adjoint, full first row and HS learned increment are unchanged.

Only the four assigned study proofs, maintained NOTATION, the pertinent
global_nonlinear source/query sections and Gaussian master-theorem
dependencies were used. The solve-math-rigorously and
investigate-conjectures skills and required theory/audit references were
read. No other study, active route, review or Git history was consulted.

Sections 1--7 first describe an exact frozen-control lower-flow
discretization as an auxiliary construction. Section 9 gives a preferable
raw-Euler implementation of the same argument, using only the already
established fixed-program source extension. Its mesh threshold may depend
on the smooth mollification; its radius and tail constants do not.
Section 9 therefore removes any need to rely on the new controlled-flow
instruction extension in §3. Both implementations retain the same
artificial tangent/source identification as their central audit target.

## 1. Base program and unconditional bounds

Use the notation

\[
 h_a=\phi(w\cdot u_a),\quad Z_a=Ah_a,\quad H_a=\phi(Z_a),
 \quad d_a=c\phi'(Z_a),\quad Q_a=A^*d_a,\quad
 f_a=E_2[cH_a],\quad r_a=f_a-y_a,\quad A=A_0+K.
 \tag{1}
\]

Both `u_a` are unit vectors, their absolute inner product is gamma,
`p_a=1/2`, and `lambda_ka=-2 p_a r_ka`. Let

\[
 H=\|\phi\|_\infty>0,\quad D=\|\phi'\|_\infty,
 \quad L=\operatorname{Lip}(\phi').
\]

Initially work with a smooth mollification of phi, retaining the same
bounds H,D,L. Dependence on higher derivatives is permitted in the
fixed-program justification but nowhere in a uniform estimate below.
Fix an arbitrary finite positive mesh with total length at most T.
At a node compute all fields (1) using the actual action and adjoint.
Update c and K by

\[
 c_{k+1}=c_k+h_k\sum_a\lambda_{ka}H_{ka},\qquad
 K_{k+1}=K_k+h_k\sum_a\lambda_{ka}d_{ka}\otimes h_{ka}.
 \tag{2}
\]

For the lower row solve, on this step only,

\[
 \partial_s w(s)=\sum_a\lambda_{ka}Q_{ka}V_a(w(s)),\quad
 V_a(v)=\phi'(v\cdot u_a)u_a,\quad w(0)=w_k,
 \quad w_{k+1}=w(h_k).
 \tag{3}
\]

Thus Q and lambda are fixed during the lower substep. For each row this
is an ordinary globally Lipschitz controlled ODE. Its value map is
continuous and has the linear envelope
`|w(h)-w(0)|<=h D sum_a |lambda_a Q_a|`.

Starting with population c=0, the scalar recurrence

\[
 \|c_{k+1}\|_\infty\le(1+2H^2h_k)\|c_k\|_\infty+2Hh_k
\]

gives actual population residuals `|r_ka|<=R:=exp(2H²T)`.
The looser bound `C:=2RHT` on c also holds for every finite oracle base
program whose residuals are frozen at these deterministic values.
On the event `||A0,n||op<=10`, which has probability tending to one,
the following bounds therefore hold for those finite oracle programs
and their population limit, without any source cap:

\[
 \|c_k\|_\infty\le C,\quad \|d_{ka}\|_2\le CD,
 \quad\|K_k\|_{HS}\le2RTCDH,\quad
 \|A_k\|_{op}\le M:=10+2RTCDH,
 \tag{4}
\]

and `||Q_ka||2<=MCD`, `||w_k||2<=sqrt(2)+2RTD MCD`.
Finite norms here mean vector RMS and ordinary Frobenius increment
norm, exactly as in the maintained normalization. No energy identity
is assigned to this auxiliary program.

The finite base oracle can replace each residual by its selected
population value, as in A.1--A.2. This is an auxiliary source extraction,
not a claim that the original finite network uses deterministic feedback
or zero initial readout.
Only those residual scalars are frozen: every finite h, Z, d and Q is
recomputed using the current actual matrix and its transpose, and K is
updated by the actual finite rank operations in (2), so the base used in
the L2 estimate (14) is a genuine finite action program rather than a
substitution of scalar Gaussian-source expressions for matrix answers.

## 2. The controlled commutator identity

For smooth phi, `||DV_a||<=L` and

\[
 DV_b(v)V_a(v)-DV_a(v)V_b(v)
 =(u_a\cdot u_b)\{
 \phi''(v\cdot u_b)\phi'(v\cdot u_a)u_b
 -\phi''(v\cdot u_a)\phi'(v\cdot u_b)u_a\}.
 \tag{5}
\]

It is zero for a=b and has norm at most `2 gamma L D` otherwise.
Let `w'=sum_a b_a(t)V_a(w)` for arbitrary integrable scalar controls,
and write
`Lambda(s,t)=integral_s^t sum_a |b_a(v)|dv`.
If P(t,s) is the derivative of the controlled flow in its starting row,
then

\[
 \|P(t,s)\|\le e^{L\Lambda(s,t)},\qquad
 |P(t,s)V_a(w_s)-V_a(w_t)|
 \le2\gamma LD\Lambda(s,t)e^{L\Lambda(s,t)}.
 \tag{6}
\]

For the second inequality set `E=P(t,s)V_a(w_s)-V_a(w_t)`.
Its initial value is zero and its derivative is
`DF(t,w_t)E+sum_b b_b(DV_b V_a-DV_a V_b)(w_t)`.
Variation of constants and (5) prove (6). This proof never divides by
a gate. It handles sign-changing controls and flat gates.

The C1,1 form needed here is the family of estimates (6) for smooth
mollifications with uniform H,D,L. They are also finite-difference
impulse estimates after integration in the impulse amplitude and
passage to the limiting Lipschitz flows. No value of phi'' on a
nondifferentiability set and no convergence of phi'' is required.

## 3. Exact base sources and consequences of a temporary cap

For the base program (2)--(3), the action skeleton of maintained N3--N8
still holds: it only uses the rank expansion in (2), not the particular
lower update. Put `gamma_ka=h_k lambda_ka`, `m_ka=h_k p_a`, and define

\[
 \begin{split}
 \alpha_{i,q}&=E_1\partial_{\zeta_q}h_i,\qquad
 \beta_{i,q}=E_2\partial_{\xi_q}d_i,\\
 F_{i,q}&=\alpha_{i,q}+\gamma_q E_1[h_i h_q]\quad(q<i),\\
 D_{i,q}&=\beta_{i,q}+\mathbf1_{q<i}\gamma_qE_2[d_i d_q],\\
 Z_i&=\xi_i+\sum_{q<i}F_{i,q}d_q,\qquad
 Q_i=\zeta_i+\sum_{q\le i}D_{i,q}h_q.
 \end{split}\tag{7}
\]

Time, rather than lexicographic order among samples, is intended by q<i
in learned terms. At a current reverse row only its own current forward
slot contributes, with coefficient `E[c phi''(Z_i)]`. All deterministic
coefficients, residuals, contractions and covariances are frozen when
taking named derivatives. Source slots remain separate at singularity.

At a fixed graph, (7) is justified by the source theorem III.F.1--6
and the following extension of A.2's clipping argument. The map (3)
has a linear value envelope and its derivatives in w and Q are bounded
by a fixed polynomial times `exp(Lh sum |lambda Q|)`. Base Q is a Gaussian
source plus finitely many bounded h's with already finite coefficients.
Inducting over the fixed graph bounds every first named derivative by
a polynomial times `exp(C sum |G_j|)` in a finite Gaussian list. Higher
derivatives of a fixed smooth mollification are finite and only change
this fixed-graph constant. These envelopes have every finite moment.
Smooth root/product clipping and local C1 convergence therefore give
uniform integrability of the first derivatives. Covariance square-root
coupling works also at rank loss. Chronological removal of clips proves
(7); the same values are the A.1 continuous-action values. This is a
fixed-graph assertion and does not presuppose a mesh-uniform cap.

Suppose every preceding beta row has absolute row sum at most B. Define

\[
 D_B=B+2RT C^2D^2.
\]

Then `sum_q |D_iq|<=D_B` and

\[
 Q_i=\zeta_i+J_i,\qquad |J_i|\le H D_B,
 \qquad E\zeta_i^2\le C^2D^2.
 \tag{8}
\]

Along the concatenated lower controlled path let
`Lambda=integral_0^T sum_a |lambda_a Q_a|dt`.
Jensen with the time/atom masses, followed by the scalar Gaussian
exponential bound, gives for every nonnegative eta

\[
 E e^{\eta\Lambda}
 \le2\exp\{2\eta RT H D_B+2\eta^2R^2T^2C^2D^2\}.
 \tag{9}
\]

There is no independence assumption across times and no maximum of
Gaussian queries in this bound.

For a named reverse pulse p=(s,b), let `v(t)=partial_(zeta_p) w(t)`.
Its control derivative at node j is

\[
 \nu_{ja}=\mathbf1_{(j,a)=p}
       +\sum_qD_{ja,q}\phi'(w_{t(q)}\cdot u_q)
                                  u_q\cdot v(t(q)).
 \tag{10}
\]

Within the lower substep,
`v'=sum_a lambda_a[Q_a DV_a(w)v+V_a(w)nu_a]`.
The direct forcing integrates to at most `2RD m_p`. Gronwall gives

\[
 {\sup_{t\le T}|v(t)|\over m_p}
 \le2RD\exp\{L\Lambda+2RD^2D_BT\}.
 \tag{11}
\]

Thus normalized lower pulses have every fixed finite moment, uniformly
over capped prefixes and meshes. In particular
`|alpha_i,p|<=A_B m_p`, hence `|F_i,p|<=f_B m_p` for finite constants
A_B,f_B. The upper named equations remain exactly

\[
 U_{i;p}=\mathbf1_{i=p}+\sum_{q<i}F_{i,q}V_{q;p},\quad
 C_{k;p}=\sum_{q<k}\gamma_q\phi'(Z_q)U_{q;p},\quad
 V_{i;p}=\phi'(Z_i)C_{k;p}+a_iU_{i;p},\quad
 a_i=c_k\phi''(Z_i),\quad\beta_{i,p}=EV_{i;p}.
 \tag{12}
\]

Because `|a_i|<=CL`, their complete absolute derivative rows have a
pointwise finite bound depending on B,H,D,L,R,C,T, by the deterministic
Volterra Gronwall argument N15. In particular, for
`d_0=2RTD²+CL`, the row sum of U is at most `exp(f_B d_0 T)` and the
row sum of V is at most `d_0 exp(f_B d_0 T)`.
These estimates alone do not select B.

## 4. An artificial tangent program on this same base

This section is the proposed new source anchor. It is not the full
raw tangent equation. It is an explicitly defined linear auxiliary
program with the actual base trajectory and all its gates held fixed.
Its deterministic residuals are frozen, as required for named-source
derivatives. Consequently no tangent residual is inserted below.

Put

\[
 M_{ba,k}=(u_b\cdot u_a)\phi'(w_k\cdot u_b)\phi'(w_k\cdot u_a).
\]

The auxiliary states are two lower fields `chi_a`, an HS operator B_tan,
and an upper field c_tan, initialized at zero. At every base node set

\[
 \begin{split}
 h^{\rm tan}_{kb}&=\sum_a M_{ba,k}\chi_{ka},\\
 Z^{\rm tan}_{kb}&=A_kh^{\rm tan}_{kb}+B_{{\rm tan},k}h_{kb},\\
 d^{\rm tan}_{kb}&=\phi'(Z_{kb})c_{{\rm tan},k}
                                  +a_{kb}Z^{\rm tan}_{kb},\\
 Q^{\rm tan}_{kb}&=A_k^*d^{\rm tan}_{kb}
                                  +B_{{\rm tan},k}^*d_{kb},\\
 \chi_{k+1,a}&=\chi_{ka}+\gamma_{ka}Q^{\rm tan}_{ka},\\
 c_{{\rm tan},k+1}&=c_{{\rm tan},k}
                       +\sum_a\gamma_{ka}\phi'(Z_{ka})Z^{\rm tan}_{ka},\\
 B_{{\rm tan},k+1}&=B_{{\rm tan},k}+\sum_a\gamma_{ka}
       [d^{\rm tan}_{ka}\otimes h_{ka}+d_{ka}\otimes h^{\rm tan}_{ka}].
 \end{split}\tag{13}
\]

One fresh independent standard Gaussian upper root e is inserted
additively into one complete answer `Z_tan,sb`. Later descendants are
recomputed. The base is unaffected. The same linear module can instead
receive a lower root in a Q_tan answer. None of these operations changes
the initialized action; all uses of A and A* in (13) are actual adjoints.

### 4.1 A width-uniform L2 estimate

Set `x=sum_a ||chi_a||2`, `kappa=||B_tan||HS`, `z=||c_tan||2`,
and `d=x+kappa+z`. With sums over the two inputs, the following estimates
hold at finite width and in the population:

\[
 \begin{array}{ll}
 \sum_b\|h_b^{\rm tan}\|_2\le2D^2x,&
 Z_{\rm sum}:=\sum_b\|Z_b^{\rm tan}\|_2\le2MD^2x+2H\kappa,\\
 d_{\rm sum}:=\sum_b\|d_b^{\rm tan}\|_2\le2Dz+CL Z_{\rm sum},&
 Q_{\rm sum}:=\sum_b\|Q_b^{\rm tan}\|_2\le M d_{\rm sum}+2CD\kappa.
 \end{array}\tag{14}
\]

The sums of the state increment norms divided by h are at most,
respectively,
`R Q_sum`, `R(H d_sum+2CD³x)`, and `RD Z_sum`.
Thus `d_(k+1)<=(1+K h_k)d_k` for a finite K depending only on
H,D,L,R,C,M. For example
`K=100(1+H+D+L+R+C+M)^8` is an overestimate.

At the forward insertion step the total state increment is at most

\[
 P m_p\|e\|_2,\qquad P=2R\{CL(M+H)+D\}.
 \tag{15}
\]

Indeed the three immediate changes are at most
`|gamma_p|MCL||e||2`, `|gamma_p|CLH||e||2`, and
`|gamma_p|D||e||2`. Later upper outputs satisfy

\[
 \|d_i^{\rm tan}\|_2\le K_0P e^{KT}m_p\|e\|_2,
 \quad K_0=D+CL(MD^2+H),\qquad t(i)>s.
 \tag{16}
\]

This estimate has no source cap. No Lp action estimate is used: every
action and adjoint in (14) is used only on L2. The coefficients M and a
are bounded multiplication operators even though the base Q may be
unbounded. The random multiplier Q DV from the true lower tangent is
precisely the part excluded in (13).

### 4.2 Source identification by even/odd parity

Here is the full identification proposed for (13); parity is used only
where justified by a finite Gaussian program.

Construct the joint base/tangent fixed program with the same initialized
matrix and a fresh root e. Unroll B_tan into its finitely many ranks.
All coordinate values have linear envelopes because M,a and the other
gate factors are bounded. With fixed smooth phi, derivatives in base
slots have at most a polynomial times `exp(C sum |G_j|)` envelope,
by the same fixed-graph induction as §3. Derivatives in tangent slots
have a deterministic finite bound, since (13) is linear with bounded
base multipliers and finitely many deterministic source coefficients.
The clipping/value/source extension proved in §3 therefore applies.

Every finite tangent variable is linear in e conditional on the base
arrays; every base variable is independent of e. Hence the finite joint
law is invariant under changing the signs of all tangent variables and
leaving all base variables fixed. The deterministic fixed-program limit
inherits this symmetry. Every base/tangent scalar contraction is zero:
the product is odd and integrable. Equivalently, a finite conditional
variance proof uses (14)--(16): for a bounded-RMS base vector b and
tangent vector T_n e_n, the normalized pairing has conditional variance
`||T_n^T b||²/n²=O(1/n)` on the action event. This is an additional direct
check for the mixed contractions used here.

Consequently the covariance between a base source and a tangent source
of the same orientation is zero. Their joint Gaussian law makes the
base and tangent source blocks independent; both are independent of
the external root e by III.F.4. Within each block there can be arbitrary
time correlations and singularity.

Chronologically, a tangent coordinate expression is odd and linear in
the tangent sources and e, with coefficients depending on base sources.
Differentiating it in a **base** slot preserves that oddness. Its
expected derivative in that base slot is therefore zero. Differentiating
a base expression in a tangent slot gives zero. The action rule thus has
no base/tangent response correction in either direction. Only expected
derivatives in tangent slots survive.

The learned operator terms can now be expanded exactly. For example

\[
 K h_i^{\rm tan}=0,\quad
 B_{\rm tan}h_i=\sum_{q<i}\gamma_q d_q^{\rm tan}E[h_qh_i],
 \quad
 B_{\rm tan}^*d_i=\sum_{q<i}\gamma_q h_q^{\rm tan}E[d_qd_i].
 \tag{17}
\]

The omitted terms in these equalities are exactly mixed contractions
such as `E[h_q h_i^tan]` and `E[d_q d_i^tan]`, just proved zero.
Likewise `K* d_i^tan=0`. It follows that the tangent scalar action
expressions have precisely the skeleton

\[
 Z_i^{\rm tan}=\xi_i^{\rm tan}
                +\sum_{q<i}\bar F_{i,q}d_q^{\rm tan}+\mathbf1_{i=p}e,
 \qquad
 Q_i^{\rm tan}=\zeta_i^{\rm tan}
                +\sum_{q\le i}\bar D_{i,q}h_q^{\rm tan},
 \tag{18}
\]

where

\[
 \bar F_{i,q}=\bar\alpha_{i,q}+\gamma_qE[h_i h_q],\quad
 \bar D_{i,q}=\bar\beta_{i,q}+\mathbf1_{q<i}\gamma_qE[d_i d_q].
 \tag{19}
\]

For these formulas bar-alpha and bar-beta are the expected derivatives
of tangent operands in tangent source slots. Their derivative recursions
use only the base law and coefficients, not the tangent covariance.
In particular, for a tangent reverse pulse p,

\[
 \chi_{k+1,a;p}=\chi_{ka;p}+\gamma_{ka}
  \left[\mathbf1_{(k,a)=p}+\sum_q\bar D_{ka,q}
                              \sum_bM_{qb,t(q)}\chi_{t(q),b;p}\right],
 \qquad
 \bar\alpha_{i,p}=E\sum_bM_{ib,t(i)}\chi_{t(i),b;p}.
 \tag{20}
\]

The upper recursion is exactly (12) with F replaced by bar-F and
the same **actual base** factors phi'(Z), a and gamma. Causal induction
therefore defines the same bar-alpha/bar-beta for every location of the
fresh probe, including locations whose unforced tangent source variance
is zero. No derivative is inferred from a value law on a singular
support: these are the formal derivatives supplied by III.F.4--5 for
the explicit module (13).

The coefficient of the external e in (18) and its descendants obeys
that same upper source pulse recursion. Conditional on all base and
tangent Gaussian sources, e is independent standard normal; tangent
outputs are linear in e. Thus

\[
 E_2[e d_i^{\rm tan}]=E_2[\partial_e d_i^{\rm tan}]
                          =\bar\beta_{i,p}.
 \tag{21}
\]

For fixed mesh first let width tend to infinity in the augmented program
and its pairing with e. The high-probability action bound and
`||e_n||2/sqrt(n)->1` transfer (16); Cauchy--Schwarz and (21) prove

\[
 |\bar\beta_{i,p}|\le K_0P e^{KT}m_p\quad(t(p)<t(i)),\qquad
 |\bar\beta_{i,i}|\le CL.
\]

Therefore the artificial source rows have the mesh-uniform anchor

\[
 B_{\rm cl}:=CL+T K_0P e^{KT}.\tag{22}
\]

This is a tangent Gaussian program argument, not the assertion that a
custom tangent is a derivative of the original nonlinear flow.
Full residual differentiation is unnecessary and was not used. In the
population odd sector its first-order residual contractions would
vanish; (13) instead freezes them explicitly from the outset.

## 5. Comparing the true and artificial source recursions

Both are now on the **same actual base**. Consequently all learned
Grams in (7),(19), the controls, gates, readout and a=c phi''(Z) coincide.
In particular `D-barD=beta-barbeta` and `F-barF=alpha-baralpha`.
No difference of phi'' values occurs.

For a true reverse pulse p define

\[
 X_{a,k;p}=\sum_{j<k}\gamma_{ja}\nu_{ja;p},\qquad
 R_{k;p}=v_{k;p}-\sum_aV_a(w_k)X_{a,k;p}.
\]

Variation of constants in the controlled equation and (6) give

\[
 |R_{k;p}|\le2\gamma LD\Lambda e^{L\Lambda}
       \sum_{j<k,a}h_j|\lambda_{ja}|\,|\nu_{ja;p}|.
 \tag{23}
\]

By (10), the last sum is at most
`2R m_p+2RD D_B T sup|v_p|`. Combining (9),(11) proves, for every fixed
finite moment order l,

\[
 \|\sup_k|R_{k;p}|\|_{L^l}\le\gamma C_{B,l}m_p.
 \tag{24}
\]

This is the only commutator error estimate needed. It is proved in
the lower source coordinates; it is never sent through A0* in Lp.

The artificial pulse (20) satisfies the pointwise bound

\[
 \sup_{k,a}|\chi_{ka;p}|/m_p
 \le2R\exp\{2RD^2D_{\rm cl}T\},\quad
 D_{\rm cl}=B_{\rm cl}+2RTC^2D^2.
 \tag{25}
\]

Indeed only bounded M entries and a deterministic bar-D row occur.
For the real pulse, its lower feature derivative is exactly

\[
 \partial_{\zeta_p}h_i
 =\sum_aM_{ia,t(i)}X_{a,t(i);p}
                 +\phi'(w_{t(i)}\cdot u_i)u_i\cdot R_{t(i);p}.
 \tag{26}
\]

Let `E_k=max_a sum_p |beta_ka,p-barbeta_ka,p|`.
Subtract (20) from the X recursion and use (26). The three terms are:

* D times bounded M times the earlier X-chi difference;
* D times the last, R-containing term of (26);
* (D-barD) times the unchanged artificial feature pulse.

Under the real cap B the first has a deterministic Gronwall coefficient,
the second is bounded in L2 by (24), and the third by (25) times E_j.
All outside update masses remain h_j p_a. Taking L2, summing these
forcing norms and applying discrete Gronwall yields

\[
 \max_{l\le k,a}\|X_{a,l;p}-\chi_{a,l;p}\|_2
 \le C_Bm_p\left(\gamma+\sum_{j<k}h_jE_j\right).
 \tag{27}
\]

Applying the bounded outside factors in (26) and taking expectations
therefore gives the entrywise bound

\[
 |F_{i,p}-\bar F_{i,p}|
 =|\alpha_{i,p}-\bar\alpha_{i,p}|
 \le C_Bm_p\left(\gamma+\sum_{j<t(i)}h_jE_j\right).
 \tag{28}
\]

The source row mass sum is at most T. Both true and artificial upper
derivative rows have pointwise bounds from (12), the actual temporary
cap, and the artificial anchor (22). Subtract the two upper systems.
Only their F arrays differ. The U difference is
`sum_q (F-barF)_iq barV_q,p+sum_q F_iq(V-barV)_q,p`;
the C and V differences have only their unchanged bounded factors.
Summing absolute values in p and using (28) gives a causal Volterra
inequality. Discrete Gronwall yields

\[
 E_k\le C_B\left(\gamma+\sum_{j<k}h_jE_j\right).
 \tag{29}
\]

The current diagonal beta terms coincide exactly, since a_i is the same.
No current E_k is hidden in the right side: lower h_k uses only steps
j<k; F_k then uses those lower derivatives; upper memory is also earlier.

Set `B=B_cl+1`. Choose a positive
`gamma_*<min(1/2,1/[2 C_B exp(C_B T)])`, with the fixed constants in
(29) enlarged as necessary. At a first potentially failed actual row,
every needed earlier row obeys B. Equation (29) bounds its discrepancy
from the artificial row by at most 1/2. Its actual row sum is therefore
at most `B_cl+1/2<B`, a contradiction. Initialization has beta=0.
This closes the source cap for every mesh of (2)--(3), uniformly over
smooth mollifications and all `|u1.u2|<=gamma_*`.

Equation (8) now gives common Gaussian reverse-field tails at all
construction nodes. The constants may be extremely large but are
finite and independent of width, mesh and mollification.

## 6. Removing the auxiliary mesh and activation smoothing

Here are the bridges required to turn the source claim into a theorem
about the actual model. They use exactly the raw comparison framework
already proved in CLOSURE_PROOF §6 and PARTIAL_RESULT §3.

Interpolate K and c affinely and interpolate w by its controlled path
(3). Their raw speeds are uniformly bounded in L2 by (4). The only
discrepancy from the raw node velocity is in the lower gate. On one
step, pointwise,

\[
 |w(s)-w_k|\le sD\sum_a|\lambda_{ka}Q_{ka}|,
\quad
 |\dot w(s)-F_w(\theta_k)|
 \le LD s\left(\sum_a|\lambda_{ka}Q_{ka}|\right)^2.
 \tag{30}
\]

The now-uniform fourth moments of node Q from (8) bound the L2 defect
by `C_B h_k`. Thus the integrated raw consistency defect tends to zero
with h_max. This estimate needs only Lipschitz phi', not continuity
of phi''. Comparisons can be made at the preceding nodes; their distance
to the interpolants is O(h_max) in raw norm.

The one-reference raw difference bound on this common ball is

\[
 \|F(\theta)-F(\bar\theta)\|_{\rm raw}
 \le C(1+R_{\rm cut})\|\theta-\bar\theta\|_{\rm raw}
                +C\sum_a p_a\tau_{R_{\rm cut}}(\bar Q_a).
 \tag{31}
\]

Readout is bounded here. The two lower-gate and upper-gate localization
errors add exactly as in CLOSURE_PROOF (15)--(18); no square cutoff
factor is introduced. Applying (31) at the nodes, with (30) and the
uniform Gaussian tail, proves Cauchy convergence of two interpolants
by the logarithmic-cutoff/Osgood argument. Completeness in full-row
L2 + HS + readout L2 gives a strong solution of the raw equations.
Bounded continuous multiplier convergence and the actual bounded
action/adjoint pass the integral equations. Their velocity is continuous,
so the path is C1. Fatou transfers the tails. The same one-reference
argument proves uniqueness against any bounded strong competitor.

For two smooth mollifications the raw comparison has in addition the
uniform activation and derivative evaluation errors
`||phi_epsilon-phi_delta||infty` and
`||phi_epsilon'-phi_delta'||infty`, times the common raw bounds.
They tend to zero by the elementary mollification estimates in
REFERENCE_PROOF (30). Applying the same Osgood comparison proves
Cauchy convergence of the smooth strong paths. It passes the original
C1,1 equations and their uniform tails, without taking a limit of a_i
or any source derivative coefficient. This proves the claimed strong
C1,1 construction, conditional only on the source anchor in §4.

The limit order is: fix smooth activation and finite mesh, take width
for the auxiliary value/source statements, remove the auxiliary mesh,
then remove activation smoothing using uniform tails. The finite-GF
and arbitrary `eta_n->0` raw-GD identification follows separately from
the complete conditional bridge in PARTIAL_RESULT §3, since S and E
are now supplied on this horizon. Its actual finite random readout is
retained. This does not identify finite raw GD with the auxiliary scheme.

## 7. Fitting and exact claim limits

For the fixed original bounded activation let T be the orthogonal
reference fitting horizon `log(8)/(4q0)` of REFERENCE_PROOF. That proof
gives loss at most 1/8 for the reference.
An orthogonal change of coordinates makes the first perturbed input
e1 and the second `(kappa,sqrt(1-kappa²))`, after choosing the reference
second axis with the appropriate sign. For `|kappa|<1/2`, its distance
from e2 is at most `2|kappa|`. Rotational invariance of the full initial
Gaussian row makes this a legitimate comparison on the same action
carrier.

The source tails in §5 are uniform over that positive input radius.
The same raw comparison (31), with the data perturbation included as
in maintained NC or CLOSURE_PROOF §6, gives uniform-in-time continuity
of the constructed state and hence predictions as kappa tends to zero.
Shrinking gamma_* therefore makes the time-T loss less than 1/4.
No continuity of phi'' is used in this value-law comparison. The early
hidden activity and nonaffinity conclusions are already supplied by
PARTIAL_RESULT's local theorem and are not endpoint claims here.

This candidate does not cover unbounded phi, arcs or arbitrary
nonatomic laws. Its constants are not a useful numerical resolution
rule, and this file does not implement a general-activation solver.
The nonlinear surrogate in (13) is not offered as a replacement model
or a restartable closure: it is only a finite source-bound witness.

## 8. Audit ledger and reopening condition

| Claim | Status within this candidate | Dependency / attack |
|---|---|---|
| Controlled commutator estimate (6) | Direct proof | Only H,D,L; no inverse gate |
| Capped real-pulse moments (9)--(11) | Direct proof | Gaussian source rule and temporary B |
| Artificial finite L2 estimate (14)--(16) | Direct proof | Only actual L2 operator/HS norms |
| Artificial source identification (18)--(21) | New candidate lemma; independent audit required | Joint base/tangent parity, expected derivatives in base slots, singular source handling |
| Uniform artificial anchor (22) | Follows if that lemma is valid | Fresh root paired with a genuine finite linear program |
| True/artificial source comparison (23)--(29) | Direct conditional argument | Same actual base; no gate differences or Lp matrix action |
| C1,1 near-orthogonal strong flow and tails | Candidate conclusion | Anchor plus raw consistency and Osgood passage |
| Fixed-horizon fitting | Candidate conclusion | Supplied reference and data continuity |

The principal hostile check is whether the linear module source law
really has exactly (18), with no additional response term from its
base-dependent multiplication coefficients. The proposed proof does
not simply ignore those derivatives: it claims their **expectations**
vanish by the independent odd tangent sector, while the within-tangent
derivatives are retained. If an audit finds a surviving base/tangent
response term, (22) is not established and the route returns to the
original source-cap gap. Failure there would not disprove the desired
near-orthogonal theorem. Until that audit is complete this file should
remain a candidate rather than upgrade the study's result.

## 9. Preferred implementation: raw Euler before removing smoothing

This section replaces the lower construction (3) by ordinary raw Euler
and replaces (23)--(24) by a quantified mesh-defect estimate. Everything
in §§4--5 involving the artificial tangent/source anchor is unchanged.
It has two benefits: fixed-program source legitimacy is exactly A.2,
and no differentiated consistency bound uniform in the mollifier is
needed. This is the preferred complete implementation of the candidate.

Fix a smooth bounded mollification, with the same H,D,L and finite
`S=||phi'''||infty`. The actual base lower update is now

\[
 w_{k+1}=w_k+h_k\sum_a\lambda_{ka}Q_{ka}V_a(w_k).
 \tag{32}
\]

The c,K updates, unconditional bounds (4), source skeleton (7),
cap-dependent Gaussian decomposition (8), and upper system (12) remain
identical. The base program uses only continuous linear-envelope
instructions and bounded smooth gate times one unbounded factor.
Thus its named-source formulas follow literally from A.1--A.2.

For the augmented tangent program (13), the bounded base coefficient
a=c phi''(Z) has bounded first derivative at fixed mollification, with
a constant allowed to depend on S; its product with one tangent field
again fits the A.2 clipping proof. More explicitly, after unfolding all
rank updates, values have a linear envelope in the finite base and
tangent Gaussian lists. Differentiation in a base slot adds only finitely
many factors of the unbounded base Q or tangent variables, so first named
derivatives have a polynomial Gaussian envelope. This is exactly the
induction in A.2. Tangent source derivatives retain their bounded
coefficients. The parity/source proof (17)--(21) therefore requires no
new coordinate-flow theorem in this implementation.

For the global coordinate-map hypotheses, replace the c argument of
a by a smooth bounded clip equal to the identity on a neighborhood of
[-C,C]. This clip is inactive on every finite oracle and population base
node by (4), including in a neighborhood needed for each formal
derivative. It makes the stated bounded coefficient and derivative
bounds literal on the whole coordinate domain.

To prove the discrete version of (6), set

\[
 b_{ka}=\lambda_{ka}Q_{ka},\quad s_k=\sum_a|b_{ka}|,\quad
 B_k=\sum_a b_{ka}DV_a(w_k),\quad J_k=I+h_kB_k,
 \quad P_{k,j}=J_{k-1}\cdots J_j.
\]

All these matrices act on a single finite-dimensional row, not on a
population Lp space. Put `Lambda=sum_k h_k s_k`. Then
`||P_kj||<=exp(L Lambda)`. Taylor's integral formula for V_a along the
one Euler displacement and `||D²V_a||<=S` give

\[
 e_{k,a}:=J_kV_a(w_k)-V_a(w_{k+1}),\qquad
 |e_{k,a}|\le2\gamma LD h_ks_k
                         +\tfrac12 SD^2h_k^2s_k^2.
 \tag{33}
\]

The first term is exactly the bracket (5), with the self bracket zero;
the second is the ordinary second-order Taylor remainder for V_a.
Telescoping the transported errors and accounting for the fact that
the Euler control pulse is inserted after J_j rather than before it,
one obtains the exact decomposition

\[
 P_{k,j+1}V_a(w_j)-V_a(w_k)
 =\sum_{l=j}^{k-1}P_{k,l+1}e_{l,a}
                       -h_jP_{k,j+1}B_jV_a(w_j).
 \tag{34}
\]

Indeed the telescoping sum equals
`P_kj V_a(w_j)-V_a(w_k)`, and
`P_kj=P_k,j+1(I+h_jB_j)`. Consequently

\[
 |P_{k,j+1}V_a(w_j)-V_a(w_k)|
 \le e^{L\Lambda}\left[
 2\gamma LD\Lambda+\tfrac12 SD^2\sum_lh_l^2s_l^2
                                     +h_jLDs_j\right].
 \tag{35}
\]

The exact real named pulse solves
`v_(k+1)=J_kv_k+h_k sum_a lambda_ka V_a(w_k)nu_ka`, with nu as in
(10). Discrete Gronwall proves the same bound (11). Its co-moving
remainder from §5 is exactly the sum of (34) multiplied by
`h_j lambda_ja nu_ja`. We now estimate that sum without taking a
maximum of s_j or of Q_j.

First, under cap B all s_j have uniformly bounded moments of every
fixed order by (8), and (9) controls every exponential moment of
Lambda. For every fixed l,

\[
 \left\|\sum_jh_j^2s_j^2\right\|_{L^l}
 \le h_{\max}\sum_jh_j\|s_j\|_{L^{2l}}^2
 \le C_{B,l}h_{\max}.
 \tag{36}
\]

The total pulse mass obeys
`sum_ja h_j |lambda_ja nu_ja|<=2R m_p+2RD D_B T sup|v_p|`.
Holder, (9), (11) and (36) bound the first two terms of (35), after
summation and division by m_p, by `C_(B,l)[gamma+S h_max]`.

For the final term in (35), split nu into its direct impulse and
the D row in (10). The direct contribution occurs only at p=(s,b);
after division by m_p it is bounded by `2R h_s s_s` times the common
exponential factor. Its Lp norm is O(h_max) by Holder, (9), and the
single-node moment bound. The remaining contribution is at most

\[
 2RD D_B\,h_{\max}\Lambda\sup_j|v_{j;p}|/m_p
\]

times the same fixed exponential factor. Equations (9),(11) bound its
Lp norm by `C_(B,l) h_max`. Thus the discrete replacement for (24) is

\[
 \|\sup_k|R_{k;p}|\|_{L^l}/m_p
 \le C_{B,l}\{\gamma+(1+S)h_{\max}\}.
 \tag{37}
\]

Only S multiplies a vanishing mesh error. Every C_(B,l) in (37) depends
on H,D,L,T and the cap, and can be chosen independently of S.

Substitute (37) for (24) in (26)--(29). All other factors use only
H,D,L and the common base fields. The resulting cap discrepancy is

\[
 E_k\le C_B\left[\gamma+(1+S)h_{\max}
                                  +\sum_{j<k}h_jE_j\right].
 \tag{38}
\]

Fix `B=B_cl+1` and choose gamma_* using only the S-independent
constant C_B, so that `C_B exp(C_BT) gamma_*<=1/4`.
For each separately fixed smooth activation choose its mesh threshold
so that `C_B exp(C_BT)(1+S)h_*<=1/4`. The same first-failure argument
then gives the B cap on all meshes with h_max<=h_*. The cap, its Q
Gaussian-tail constants and the positive gamma_* are independent of S.
The threshold h_* is allowed to depend on S.

Ordinary raw-Euler interpolants now converge by (31) and those uniform
incoming tails, precisely as in CLOSURE_PROOF's Osgood construction;
there is no new splitting consistency step. This constructs the strong
flow for each fixed mollification. Only afterwards are mollifications
compared and removed using phi/phi' convergence and their common tails,
as in §6. This establishes the same candidate C1,1 result without any
uniform continuity assumption on phi'' and without the extra source
extension for (3).

This limit-order distinction is essential. The statement is not that
one mesh threshold works for all mollifications, or that raw source
coefficients themselves converge as smoothing is removed. The statement
needed for the original flow is a uniform radius and uniform tails of
the already constructed smooth strong flows, and those are the quantities
provided by (38).

### 9.1 Passive queries

The same anchor and comparison extend to each passive unit input u,
uniformly in u, without training it. Define

\[
 h^{\rm tan}(u)=\phi'(w\cdot u)\,
                     u\cdot\sum_{a=1}^2V_a(w)\chi_a.
 \tag{39}
\]

Its L2 norm is at most D² x. Its source derivatives have the same
bounded outside coefficients as (26), with the lower error
`phi'(w.u) u.R`. The commutators still concern only the two active
driving vector fields V_1,V_2; no bracket with a passive vector field
is required. The upper tangent output for this appended query obeys
(14)--(16) with h(u),d(u) and the same H,D,L,C,M bounds. Its current
beta has only its one distinguished source, bounded by CL. This proves
the same B_cl anchor for passive rows, after enlarging K0 if needed.

Define E_k in (38) as the supremum over these passive rows. The forcing
rows in (20),(27) remain the two active rows, which are included in that
supremum. Equation (39) bounds every passive outside factor uniformly,
so all estimates are unchanged. Hence (8) gives uniform marginal
Gaussian tails for passive reverse queries as well. During smoothing
removal those tails pass for each u by positive-part truncations, with
constants independent of u; no continuity of beta(u) is needed.
