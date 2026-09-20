# C-X3: reference geometry, a continuation criterion, and its remaining gap

Scoped alternative proof route, 2026-09-20. This is a theoretical author
analysis, not a completed C-X3 theorem or an independent review. No experiment,
code execution, or Git mutation was performed.

The result of this route is conditional. At every fixed depth, the signed
reference dynamics have polynomial raw bounds on every finite feature-time
interval, and they have a strong endpoint at any finite proposed obstruction
below the fitting level. Uniform exponential backward-field tails for a
specified autonomous cutoff construction would close existence, uniqueness,
and global physical reference fitting. Those tails are **not proved here**.
An explicit calculation also rules out an ambient one-sided Lipschitz
replacement, even within the reference symmetry class and after the
first-layer clock change.

## 1. Read scope and exact object

The scientific inputs were only this study's `CONTRACT.md` and
`CH3_LOCAL_PROOF.md`, `docs/NOTATION.md`, and the following portions of
`docs/global_nonlinear.md`: B.1 lines 2100–2453, C.1–C.2 lines 2454–3440,
and C.4.5.1 lines 5475–6103. No other study, route output, or unpromoted
finding was read. The solve-math-rigorously and investigate-conjectures
skills, including the latter's contract and adversarial-audit references,
were applied. The proof below derives its new statements; cited local
existence and common-carrier facts retain the status of the assigned CH3
candidate.

Fix L>=3 and the contract's independent initialized Gaussian actions
A_l,0:H_(l-1)->H_l, with their actual adjoints, where H_l=L2(Omega_l).
Use their canonical common carrier from CH3. All action norms are finite;
the bound 10 from CH3 is enough. No action A_l,0 is declared HS. Set

\[
 E=H_1^2\oplus\bigoplus_{l=2}^L S_2(H_{l-1},H_l)\oplus H_L,
 \qquad \theta=(w,K_2,\ldots,K_L,c),\quad A_l=A_{l,0}+K_l.
\]

The norm on E is the raw square-sum norm. A sum of component norms will
occasionally be used for estimates; its equivalence constants depend only
on L. Initially w=(g_+,g_-) has independent standard normal components,
every K_l is zero, and c=0. The two normalized inputs are e_1,e_2 with
labels y_+=1,y_-=-1. Write H_(l,a), Z_(l,a), P_(l,a), Delta_(l,a) for the
contract's exact forward/backward fields. Put

\[
 h=(H_{L,+}-H_{L,-})/2,\qquad b=\langle c,h\rangle.
\]

For a hidden increment v=(v_w,B_2,...,B_L), define recursively

\[
 V_{1,a}=v_{w,a},\qquad
 V_{l,a}=B_lH_{l-1,a}+A_l[\phi'(Z_{l-1,a})V_{l-1,a}],
 \qquad Jv=\tfrac12\sum_a y_a\phi'(Z_{L,a})V_{L,a},
 \quad\phi=\tanh.
\]

This bounded linear map is a directional differential into H_L. Scalar
pairing with c and actual adjunction give

\[
 J^*c=\left(
 (y_a\Delta_{1,a}/2)_a,
 \left(\tfrac12\sum_a y_a\Delta_{l,a}\otimes H_{l-1,a}\right)_{l=2}^L
 \right).
\tag{1}
\]

Thus the exact signed feature equation is

\[
 \theta_s=G(\theta),\qquad
 c_s=h,\qquad (w,K_2,...,K_L)_s=J^*c.
\tag{2}
\]

It trains every block. Formula (1) uses the HS identity
<q tensor v,B>_HS=<q,Bv>; it does not replace HS by operator norm.
The scalar functional b has continuous raw gradient G, by the scalar
chain-rule argument of CH3. No L2-valued Frechet derivative of tanh is
asserted. CH3 and C.2 apply locally also to the bounded deterministic signed
coefficients in (2), as explicitly permitted in C.2's final paragraphs.

## 2. Global raw bounds are available before any tail estimate

Let a_l,0=||A_l,0||op. Define, from the top downward, the nonnegative
polynomials

\[
 a_L(s)=a_{L,0}+s^2/2,
 \qquad
 a_l(s)=a_{l,0}+\int_0^s v\prod_{j=l+1}^L a_j(v)\,dv
 \quad(l=L-1,...,2).
\tag{3}
\]

Empty products are one. On every existing strong solution of (2),

\[
 \|c(s)\|_\infty\le s,\quad
 \|A_l(s)\|op\le a_l(s),\quad
 \|K_l(s)\|HS\le a_l(s)-a_{l,0},
\tag{4}
\]
\[
 \|w(s)-w(0)\|_{H_1^2}
 \le 2^{-1/2}\int_0^s v\prod_{j=2}^L a_j(v)\,dv.
\tag{5}
\]

Indeed |h|<=1 gives the readout bound. Since 0<phi'<=1 and
||H_(l,a)||2<=1, downward backpropagation gives

\[
 \|\Delta_{l,a}(s)\|_2
 \le s\prod_{j=l+1}^L\|A_j(s)\|op.
\]

The l-th rank velocity in (1) has HS norm at most the right side.
Starting at l=L and integrating proves (3)–(4). The two row velocities
have norms at most half the l=1 bound; their square sum proves (5).
Every polynomial is finite at every finite s. These estimates are stronger
than a small-ball estimate, but they do not give infinite-dimensional
existence or uniqueness.

They also hold for the cutoff equations in §4 because scalar clipping
does not increase absolute values. In particular, none of those auxiliary
flows can escape the raw bounded sets at a finite time.

## 3. The exact geometric gain and what an endpoint does not prove

On every strong solution of (2), the strong curve chain rule gives

\[
 h_s=JJ^*c,\quad
 b_s=\|h\|_2^2+\|J^*c\|_{hidden}^2
     =\|\theta_s\|_{raw}^2.
\tag{6}
\]

To justify the chain rule, approximate a fixed L2 velocity by bounded
variables, use scalar differentiation with bounded phi', and remove the
approximation by the bound |phi'|<=1. Multiplication by a bounded
continuous gate is strongly continuous against a fixed L2 factor. Apply
the operator product rule and this argument successively through the
finitely many layers. No derivative of J is used in (6).

Let q_0=1 and q_l=E[tanh(sqrt(q_(l-1))G)^2] for a standard normal G.
Each q_l is strictly positive: its integrand is positive except at G=0.
At initialization the two inputs have orthogonal forward Gram matrices
q_l I at every layer, by independent Gaussian action and oddness. Hence

\[
 m=\|h(0)\|_2^2=q_L/2>0.
\tag{7}
\]

For g(s)=||c(s)||2>0, differentiating the scalar norm gives

\[
 g_s=b/g,\qquad
 g_{ss}=\{\|h\|_2^2-g_s^2+\|J^*c\|_{hidden}^2\}/g\ge0.
\]

The inequality is Cauchy–Schwarz applied to <c,h>. Since
c(s)=s h(0)+o_L2(s), g_s(0+)=sqrt(m). Therefore g_s>=sqrt(m),
g>=s sqrt(m), and ||h||2>=g_s on the first positive interval. The lower
bound on g prevents that interval from ending at a positive zero. Thus

\[
                         b_s\ge m
\tag{8}
\]

throughout any existing positive feature interval.

Suppose an existing solution is defined on [0,S) with S<infinity and
b(s)<=1. Integrating (6) and applying Cauchy–Schwarz gives

\[
 \|\theta(v)-\theta(u)\|raw
 \le\sqrt{(v-u)(b(v)-b(u))}\le\sqrt{v-u}
 \quad(0<=u<=v<S).
\tag{9}
\]

Completeness of E gives a strong endpoint theta(S). Continuity of G,
proved by the bounded-gate truncation argument in CH3, extends the
integral equation and its derivative to this closed interval. Moreover
S<=1/m by (8), and
||theta(S)-theta(0)||raw<=1/sqrt(m).

This does not construct the solution to the right of S. A continuous
vector field on an infinite-dimensional Hilbert space is not covered by
the contraction argument used in B.1. Compactness of the one reached
curve gives uniform L2 tail disappearance, but gives no required rate.
For example on (0,1), P(x)=x^(-1/4) belongs to L2 and has
||P 1_(P>R)||2=sqrt(2)/R for R>=1. Its bounded truncations converge in
L2. Thus even strong convergence of fields each having every exponential
moment does not preserve a uniform exponential tail estimate. This
example only diagnoses the invalid topological inference; it is not
claimed to be a reached neural field.

## 4. A precise, weaker-than-Gaussian sufficient continuation criterion

For N>=1 let chi_N(r)=max(-N,min(N,r)). Keep all forward equations exact.
At a state theta define clipped backward fields by

\[
 P^N_{L,a}=c,\quad \Delta^N_{L,a}=\phi'(Z_{L,a})\chi_N(c),
\]
\[
 P^N_{l,a}=A_{l+1}^*\Delta^N_{l+1,a},\quad
 \Delta^N_{l,a}=\phi'(Z_{l,a})\chi_N(P^N_{l,a})\quad(l<L).
\tag{10}
\]

Replace Delta by Delta^N in (1), retaining c_s=h, to define G_N.
These are autonomous auxiliary equations, determined by initialization
and current state. They are not the optimizer asserted in the contract.
Only convergence of their removal limit could make them a construction
of that optimizer.

On any fixed raw bounded set, G_N is Lipschitz with constant C(1+N),
where C is independent of N. For example

\[
 \|\phi'(z)\chi_N(p)-\phi'(\bar z)\chi_N(\bar p)\|_2
 \le\|p-\bar p\|_2+2N\|z-\bar z\|_2.
\]

Forward differences are Lipschitz. Downward backpropagation multiplies
an already formed error only by bounded actions and gates, then adds a
term proportional to N. Therefore no power N^L is introduced. The HS
rank difference inequality finishes the estimate for every raw block.
The integrated map on a small continuous-path ball is a contraction if
the interval length times C(1+N) is less than one; its bounded velocity
keeps that ball invariant after shortening the interval. This constructs
a unique local solution. Bounds (3)–(5), also valid for G_N, give bounded
velocities on every finite horizon, hence a strong endpoint at any
proposed finite terminal time. The same local contraction restarts there.
Consequently the solution theta^N exists uniquely for all s>=0.

In the next hypothesis P_(l,a)(theta^N(s)) means the **unclipped** exact
backward field recomputed at this clipped-flow state. Define
tau_R(P)=||P 1_(|P|>R)||2.

**Conditional continuation theorem.** Fix S<infinity. Suppose there are
D<infinity and alpha>0, independent of N, such that

\[
 \sup_{N>=1}\sup_{0<=s<=S}
 \sum_{a=+,-}\sum_{l=1}^L
 \tau_R(P_{l,a}(\theta^N(s)))\le D e^{-\alpha R}
 \quad(R>=0).
\tag{11}
\]

Then theta^N converges uniformly in raw norm on [0,S] to a strong C1
solution of the exact equation (2). It is unique among continuous strong
raw solutions on its initialized carrier, with no tail assumption on a
competitor. It has unique same-equation reached-state restart. Hypothesis
(11) is not established in this document.

Here is the proof. At a fixed state, compare exact and clipped
backpropagation, using the one-Lipschitz property of chi_N. Starting from
the top gives

\[
 \|\Delta_{l,a}-\Delta^N_{l,a}\|_2
 \le\|A_{l+1}\|op\|\Delta_{l+1,a}-\Delta^N_{l+1,a}\|_2
       +\tau_N(P_{l,a}),
\]

with the top bound tau_N(c). Downward substitution and the raw rank
identity prove, on the common polynomial ball,

\[
 \|G_N(\theta)-G(\theta)\|sum
 \le C\sum_{a,l}\tau_N(P_{l,a}(\theta)).
\tag{12}
\]

The raw one-reference estimate from CH3, with the fixed signed
coefficients of (2), is

\[
 \|G(\theta)-G(\bar\theta)\|sum
 \le C(1+R)e(\theta,\bar\theta)
        +C\sum_{a,l}\tau_R(P_{l,a}(\bar\theta)).
\tag{13}
\]

Its proof is the same gate truncation and finite downward substitution;
the loss-residual difference term is absent. Combining (11)–(13) on
any time slab I=[u,u+delta] gives

\[
 \sup_{s\in I}e(\theta^N(s),\theta^M(s))
 \le e^{C(1+R)\delta}
 \left[e(\theta^N(u),\theta^M(u))
       +CD\delta\{e^{-\alpha R}+e^{-\alpha N}+e^{-\alpha M}\}\right].
\tag{14}
\]

Choose delta>0 with C delta<alpha/2 and partition [0,S] into finitely
many such slabs. On the first slab the starting distance is zero. First
send N,M to infinity at fixed R, then R to infinity; the remaining bound
has exponent at most -alpha R/2. Thus the sequence is Cauchy there.
On the next slab the starting distance already tends to zero, so the
same ordered limits apply. Finite induction proves uniform Cauchy
convergence on [0,S]. Completeness gives theta. Continuity of G makes
G(theta^N) converge uniformly along these convergent paths: otherwise
a contrary sequence of times would have a convergent subsequence and
contradict joint continuity. The defect (12) tends to zero uniformly.
Passing to the integral equation proves theta_s=G(theta), strongly.

Exact backward fields also converge uniformly in L2. The elementary
bound
tau_R(P)<=2||P-Q||2+2 tau_(R/2)(Q)
therefore transfers an exponential bound with exponent alpha/2 to the
limit. Compare any competing raw strong solution against this reference
in (13). Its compact raw path and the reference have a common bounded
ball. On sufficiently short slabs the argument of (14), without cutoff
defects, forces zero distance; finite induction proves uniqueness.

For reached-state restart, the existing restriction provides existence
and the preceding estimate gives uniqueness. It is also constructible
from that current state alone: start G_N there and compare it with the
reference using the Lipschitz bound C(1+N) for G_N and (12) on the
reference only. On a sufficiently short slab the error is bounded by
C exp(CN delta-alpha N/2), which vanishes. Repeat over finitely many
slabs. Every cutoff construction uses only current actions, actual
adjoints, coordinate operations, and current fields. Their generated
closed spaces contain the limit. Equal current joint action laws thus
identify the continuations by the corresponding L2 isometry.

The same proof works if the left side of (11) is replaced by its time
integral over [0,S]; (14) uses only integrated tails. For the uniqueness
part alone, it suffices that the already existing reference has such an
integrated exponential tail, without a cutoff-family assumption.

Why exponential tails are a useful threshold for this argument can be
seen directly. With tau_R<=D exp(-alpha R^beta), optimization of (13)
gives a modulus bounded by
C e[1+(log(1/e))^(1/beta)] for small state distance e. The reciprocal
integral near zero diverges for beta>=1. This scalar uniqueness fact
follows by integrating d'(s)<=omega(d(s)): starting at distance epsilon,
the time needed to reach a fixed positive distance is at least
integral_epsilon^a dx/omega(x), which tends to infinity. If beta<1 the
displayed reciprocal integral is finite, so this bound supplies no such
uniqueness conclusion. This is a limit of the estimate, not a
nonuniqueness theorem for the neural flow.

## 5. What that criterion would imply for the unperturbed reference

It is enough to prove (11) at the single explicit feature horizon
S=1/m, where m=q_L/2 from (7). Conditional on that hypothesis, (8) makes
b reach 1 at a unique first s_dagger<=1/m. The canonical initialization
has a measure-preserving swap involution at each population, exchanging
the two input queries and intertwining every A_l,0 with its actual
adjoint. It is obtained by adjoining swapped copies of each finite
initialized program, exactly as in C.4.5.1. Odd chi_N makes every cutoff
construction equivariant under that swap and c->-c. Its limit therefore
has f(e_1)=b=-f(e_2). This is population symmetry; finite initialized
networks are not assumed to be symmetric.

The physical reference vector field is consequently 2(1-b)G. On
0<=s<s_dagger define

\[
 t(s)=\int_0^s\frac{dv}{2(1-b(v))}.
\]

Since b_s is continuous and bounded up to s_dagger,
1-b(s)<=C(s_dagger-s); hence t(s) diverges at s_dagger. Its inverse
exists for every physical t>=0 and satisfies s_t=2(1-b). Thus the
conditional reference is global in physical time and

\[
 0<1-b(s(t))\le e^{-2mt},\qquad
 \mathcal L_*(t)\le e^{-4mt}.
\tag{15}
\]

In particular T_fit=log(8)/(4m) gives reference loss at most 1/8.
The strong endpoint theta_dagger=theta(s_dagger) exists, and (8)–(9)
give

\[
 \|\theta(s(t))-\theta_\dagger\|raw
 \le(1-b(s(t)))/\sqrt m.
\tag{16}
\]

For an explicit whole-input consequence let
B=max_(2<=l<=L)(a_l,0+1/sqrt(m)) and
Q^2=1+m^(-1) sum_(r=0)^(L-1) B^(2r).
Every state before the endpoint is within 1/sqrt(m) of initialization
by (9), so its action norms are at most B and its readout L2 norm is at
most 1/sqrt(m). The same holds on a straight segment between any two
such states. The raw gradient of a passive prediction f(u), |u|=1,
has readout norm at most one and hidden-block norms at most
m^(-1/2) B^(L-l), l=1,...,L. Scalar integration along that segment gives
sup_u|f_theta(u)-f_tilde_theta(u)|<=Q||theta-tilde_theta||raw. Hence

\[
 \sup_{|u|=1}|f_*(t,u)-f_\dagger(u)|
 \le Qm^{-1/2}e^{-2mt}.
\tag{17}
\]

These are consequences **conditional on (11)**. No positive supported-law
neighborhood, actual finite-network capture through this horizon, closure
convergence, or numerical realization follows merely from (15)–(17).

## 6. Exact obstruction to an ambient monotonicity replacement

The following calculation retains the actual Gaussian initialization and
its reused transpose action. It is stronger than an abstract warning
that a product of L2 fields may be troublesome.

For every L>=3, on every raw neighborhood of initialization, the vector
field G fails a finite one-sided Lipschitz bound

\[
 \langle G(\theta)-G(\bar\theta),\theta-\bar\theta\rangle
 \le C\|\theta-\bar\theta\|raw^2.
\tag{18}
\]

The failure persists after restricting to the reference swap symmetry
and after transforming only the first-layer rows by B.1's scalar clocks.
It is not a claim of nonuniqueness along the actually reached solution.

Keep all hidden parameters at initialization. Set c=epsilon h_0, where
h_0=(H_(L,+)(0)-H_(L,-)(0))/2 and epsilon>0 can be arbitrarily small.
This state is within epsilon sqrt(m) of initialization and has
||c||infinity<=epsilon. It respects the reference swap symmetry because
h_0 changes sign under the swap.

Write X_a=Z_(L-1,a)(0), Y_a=Z_(L,a)(0), and
U_a=h_0 phi'(Y_a). The initialized top forward Gram is q_(L-1) I.
The first actual reverse call of A_L,0 obeys the Gaussian conditioning
identity

\[
 A_{L,0}^*U_+
   =p_+H_{L-1,+}(0)+p_-H_{L-1,-}(0)+\Gamma,
 \quad p_a=E[Y_aU_+]/q_{L-1},
\tag{19}
\]

where Gamma is centered Gaussian of variance E[U_+^2]>0, independent of
the old lower-population fields. This is precisely the conditioning
calculation of C.4.5.1 (R25) applied to the top edge: condition the
initialized Gaussian matrix on its two forward queries; its conditional
mean gives the two displayed projections, and its independent residual
matrix gives the reverse Gaussian term. The finite projections onto the
two old lower query directions have vanishing RMS. The source U_+ is a
bounded smooth function of the two Gaussian outputs, so this fixed
program is admissible. Positivity of its variance follows from full
support of (Y_+,Y_-) and the fact that
(tanh Y_+-tanh Y_-)phi'(Y_+) is not identically zero.

Let P=A_L,0^*[c phi'(Y_+)]=epsilon A_L,0^*U_+.
The deterministic part in (19) is bounded. Since X_+ is a nondegenerate
Gaussian, phi''(X_+) is nonzero with probability one. Independence of
Gamma from the lower fields implies

\[
             \Pr(P\phi''(X_+)>M)>0\quad\text{for every }M>0.
\tag{20}
\]

Indeed condition on the lower fields where |phi''(X_+)|>0: a
nondegenerate normal with either nonzero multiplier has an unbounded
upper tail, regardless of its finite conditional mean.

Let S_l be the initialized swap involution on H_l. It is a unitary
map preserving coordinate multiplication, S_l^2=I,
S_l A_l,0=A_l,0 S_(l-1), and S_l H_(l,+)=H_(l,-).
Choose the bounded field

\[
 q_M=\sqrt{\frac{q_{L-2}}{2\Pr(E_M)}}\,1_{E_M},
 \qquad E_M=\{P\phi''(X_+)>M\},
\]

in H_(L-1). Indicators are L2 limits of bounded continuous functions
of the displayed finite-program variables, hence belong to the common
generated carrier. Define the HS perturbation only in block L-1 by

\[
 B_M=\frac{q_M\otimes H_{L-2,+}(0)
              +(S_{L-1}q_M)\otimes H_{L-2,-}(0)}{q_{L-2}}.
\tag{21}
\]

The two lower input features have Gram q_(L-2)I, so
B_M H_(L-2,+)=q_M, B_M H_(L-2,-)=S_(L-1)q_M, and
||B_M||HS^2=2||q_M||2^2/q_(L-2)=1. Also
S_(L-1) B_M S_(L-2)=B_M, so this direction preserves the swap symmetry.
At L=3 this is exactly a K_2 direction, leaving both first-row clocks
fixed.

Differentiate b twice along K_(L-1)(t)=t B_M while keeping the other
blocks and c=epsilon h_0 fixed. All variations q_M are bounded at each
fixed M. Operator differentiation is in L2; scalar differentiation at
the top uses bounded phi'' and products of two L2 first derivatives,
which are integrable. Thus the differentiation is justified without an
unbounded L2 Hessian assumption. The plus and minus contributions become
equal by swap invariance and S_L c=-c. The result is

\[
 \frac{d^2 b}{dt^2}(0)
 =E_L[c\phi''(Y_+)\{A_{L,0}(\phi'(X_+)q_M)\}^2]
       +E_{L-1}[P\phi''(X_+)q_M^2].
\tag{22}
\]

The first term has absolute value at most
2 epsilon ||A_L,0||op^2 ||q_M||2^2, because |phi''|<=2 and
||c||infinity<=epsilon. By (20) the second is at least
M||q_M||2^2. Since ||q_M||2^2=q_(L-2)/2, (22) yields

\[
 \frac{d^2 b}{dt^2}(0)
 \ge\frac{q_{L-2}}2
       \{M-2\epsilon\|A_{L,0}\|op^2\}\longrightarrow\infty.
\tag{23}
\]

If (18) held on a raw neighborhood, apply it between this state and
its tB_M perturbation, divide by t^2, and send t to zero. Since G is
the scalar gradient of b, the result would bound (22) by C for every M,
contradicting (23). Taking epsilon small places the base state in any
chosen neighborhood. Because the perturbation fixes w, the same
contradiction survives changing only the first-row coordinates to the
B.1 clocks. In particular, convexity of the single scalar ||c|| does
not supply the missing monotonicity estimate for the full raw system.

The calculation does not say that every useful metric change fails.
It specifically excludes a finite one-sided Lipschitz constant in the
raw metric, or the inherited metric that changes only first-row clocks,
even on the reference-symmetric state class.

## 7. Why a direct second-layer scalar clock is not supplied by B.1

Already at L=3, differentiation of the exact feature equations gives

\[
 (Z_{2,a})_s
  =\tfrac12\sum_b y_b\langle H_{1,b},H_{1,a}\rangle
                      \phi'(Z_{2,b})P_{2,b}
    +\tfrac12 y_a A_2[\phi'(w_a)^2 P_{1,a}].
\tag{24}
\]

The last term has no factor phi'(Z_(2,a)); it comes from motion of the
lower features through the same actual action A_2. The current feature
Gram also need not be diagonal. Consequently the B.1 transform with
F'(z)=1/phi'(z) divides these terms by phi'(Z_(2,a)) instead of removing
all varying gates. The factor 1/phi'(z)=cosh(z)^2 is unbounded. Bounds
(3)–(5) do not control that multiplication on L2. This identifies the
missing estimate for this scalar-clock proposal; it is not a proof
that every joint nonlinear coordinate transformation is impossible.

## 8. Claim status and next exact obligation

| Claim | Status | Reason |
|---|---|---|
| Exact all-block signed feature system in the raw HS metric | Proved algebraically | (1)–(2), actual adjoints |
| Polynomial raw bounds at every finite feature horizon | Proved on existing/cutoff solutions | Top-down induction (3)–(5) |
| Radial convexity and b_s>=q_L/2 | Proved on strong solutions | (6)–(8) |
| Strong endpoint at a finite boundary with b<=1 | Proved | (9), completeness and field continuity |
| Autonomous cutoff construction globally in feature time | Proved | Local contraction plus (3)–(5) |
| Exact reference continuation from cutoff removal | Conditional | Requires (11), which is unproved |
| Global physical reference, fitting, strong endpoint, whole-input endpoint approximation | Conditional | §5 depends on (11) at S=1/m |
| Ambient monotonicity or first-clock Lipschitz shortcut | Ruled out in the stated metrics | Symmetry-preserving Gaussian calculation (19)–(23) |
| Actual strong continuation, supported perturbations, finite GF/GD capture and common closure through fitting | Open in this route | No tail/removal/transfer proof through S=1/m |

The highest-leverage remaining input for this route is a proof of (11),
or its integrated version, on the explicit finite horizon 1/m. It must
control the exact backward fields along the current-state cutoff family,
uniformly as N grows, while retaining both orientations of every
initialized Gaussian action. Polynomial raw bounds, bounded readout,
the radial fitting identity, and individual-time L2 compactness do not
supply that estimate. Failure of this route to prove it is not evidence
that the contract's depth extension is false.

## 9. Second-round check: cutoff energy and integrated tails

Added 2026-09-20 after freezing §§1–8. This section records the requested
focused attempt to use signed energy for the time-integrated version of
(11). It leaves the first-round claims unchanged. The separately checked
`CH4_FITTING_CONSTANTS.md` was read only after the freeze; its exact hash
and scoped check are in `CH4_FITTING_CHECK.md`. Its new initialization
bound is not needed below.

### 9.1 The cutoff energy identity has a genuine error term

Write b_N(s)=b(theta^N(s)) and D_N(theta)=G(theta)-G_N(theta).
Since G is the scalar raw gradient of b and theta^N_s=G_N(theta^N),
the exact identity is

\[
 (b_N)_s
 =\langle G(\theta^N),G_N(\theta^N)\rangle_{raw}
 =\|G_N(\theta^N)\|_{raw}^2
       +\langle D_N(\theta^N),G_N(\theta^N)\rangle_{raw}.
\tag{25}
\]

This follows from the scalar chain rule and does not assume cutoff
convergence. By (3)–(5), G_N has a bound V_S on [0,S] independent of N.
The exact estimate (12) therefore gives the valid substitute

\[
 \left|(b_N)_s-\|\theta^N_s\|_{raw}^2\right|
 \le C_S\sum_{a,l}\tau_N(P_{l,a}(\theta^N(s))).
\tag{26}
\]

In particular, b_N(0)=0 and |b_N(s)|<=||c(s)||2||h(s)||2<=s imply

\[
 \int_0^S\|\theta^N_s\|_{raw}^2ds
 \le S+C_S\int_0^S\sum_{a,l}
              \tau_N(P_{l,a}(\theta^N(s)))\,ds.
\tag{27}
\]

Thus this substitution introduces the very integrated tail quantity
whose decay is missing. No sign of the error in (25) is claimed.

Here is an exact check that the error term cannot simply be deleted as
an algebraic identity, even in the reference-symmetric class. Keep every
hidden block at initialization, put sigma=sign(h_0), and set c=lambda
sigma for lambda>N. The zero set of h_0 has probability zero. All fields
are on the original canonical carrier; sigma is obtained by bounded L2
approximation, and it changes sign under the reference swap.

Because chi_N(c)=N sigma, the hidden part v_N of G_N is independent of
lambda. The exact hidden gradient is lambda v_1 by linearity in c,
where v_1 denotes that gradient at c=sigma. The readout derivative is
h_0 in both fields. Let a=<v_1,v_N> and d=||v_N||hidden². Then at this
state

\[
 db[G_N]=m+\lambda a,\qquad \|G_N\|raw^2=m+d.
\tag{28}
\]

Moreover d>0. Indeed the top hidden-block update is
(N/2) sum_a y_a(sigma phi'(Y_a)) tensor H_(L-1,a)(0), whose HS norm
squared equals
N² q_(L-1) sum_a E[phi'(Y_a)²]/4>0 by the orthogonal initialized
feature Gram. If the two expressions in (28) were equal both at
lambda=2N and at lambda=3N, subtraction would force a=0 and then d=0.
They therefore differ at at least one of these two symmetric states.
This is a counterexample to a structural identity for the cutoff vector
field; it does not assert that these two states lie on its canonical
initial trajectory.

### 9.2 An actual-Gaussian state obstruction to energy-only tail bounds

There are reference-symmetric raw states arbitrarily close to
initialization with all of the following properties: bounded readout,
bounded raw/action norms, b<1, bounded exact and clipped raw velocities,
the **unchanged initialized forward fields at both anchors**, and no
exponential backward tail. This makes the obstruction more specific
than an abstract L2 counterexample.

Keep the initialized notation X_a=Z_(L-1,a)(0),
Y_a=Z_(L,a)(0), U_+=h_0 phi'(Y_+), and the swap involutions S_l.
The standardized variables
G_a=X_a/sqrt(q_(L-2)) are independent standard normals. Define

\[
 v_a=\frac{e^{G_a^2/8}-E e^{G^2/8}}
            {\{\operatorname{Var}(e^{G^2/8})\}^{1/2}}.
\tag{29}
\]

The denominator is finite and strictly positive: Gaussian integration
gives E exp(G²/8)=(3/4)^(-1/2) and E exp(G²/4)=sqrt(2).
Thus ||v_a||2=1. These fields belong to the canonical generated L2
carrier by truncating the continuous functions in (29). They are even
in their own G coordinate and centered. Consequently

\[
 \langle v_a,H_{L-1,b}(0)\rangle=0
 \quad(a,b=+,-),\qquad S_{L-1}v_+=v_-.
\tag{30}
\]

For a=b this is oddness of tanh times an even integrable function;
for a!=b it is independence and the zero mean of tanh.

For arbitrary small epsilon,kappa>0, set c=epsilon h_0, keep all hidden
blocks but the top one at initialization, and put

\[
 K_L=\frac\kappa2
       \{U_+\otimes v_+ +(S_LU_+)\otimes v_-\}.
\tag{31}
\]

This is a genuine HS learned increment, of norm at most kappa||U_+||2.
It commutes with the swap involutions, and c has the required odd swap
parity. Equations (30) imply K_L H_(L-1,a)(0)=0. Hence every anchor
forward field remains exactly its initialized value, h=h_0, and
b=epsilon m<1 if epsilon is sufficiently small. The full raw distance
to initialization is at most kappa+epsilon sqrt(m). In particular the
construction does not obtain large backward tails by making any raw
norm or readout supremum diverge.

Use (19) for the actual initialized reverse action. Recomputed at this
state, the plus backward field one layer below the top is

\[
 P_{L-1,+}
 =\epsilon\{p_+H_{L-1,+}(0)+p_-H_{L-1,-}(0)+\Gamma\}
       +a v_+ +d v_-,
\tag{32}
\]

where

\[
 a=\frac{\kappa\epsilon}{2}\|U_+\|_2^2>0,\qquad
 d=\frac{\kappa\epsilon}{2}\langle S_LU_+,U_+\rangle.
\]

Here Gamma is a nondegenerate Gaussian independent of G_+,G_-.
The two response terms involving H are bounded. Restrict to an event
where |v_-| and |Gamma| are at most a sufficiently large fixed M_0;
this event has strictly positive probability and is independent of v_+.
On it, (32) is at least a v_+-C for a fixed finite C.

For completeness, v_+ has a quantitative polynomial lower tail. If
z=sqrt(8 log(C_1 R)) with C_1 sufficiently large and R sufficiently
large, then G_+ in [z,z+1/z] implies v_+>C_2 R, where C_2 can be any
fixed positive constant after increasing C_1. On that interval the
Gaussian density is at least its value at z+1/z. Therefore

\[
 \Pr(v_+>C_2 R)
 \ge c R^{-4}(\log R)^{-1/2}
\tag{33}
\]

for some c>0. Choose C_2 so that a C_2 R-C>2R for large R. The
independent event just specified and (32)–(33) give

\[
 \tau_R(P_{L-1,+})
 \ge c' R^{-1}(\log R)^{-1/4}
\tag{34}
\]

for all sufficiently large R, with c'>0 depending on the fixed small
epsilon,kappa. In particular E exp(alpha|P_(L-1,+)|)=infinity for every
alpha>0, and no bound D exp(-alpha R) can hold.

Nevertheless every exact raw gradient block is finite and uniformly
bounded on this small raw ball. This follows directly from bounded
actions and gates, bounded hidden activations, and ||c||2<=epsilon:
the exact backward L2 norms and all HS ranks are bounded by the same
finite products used in §2. The clipped velocities satisfy those bounds
as well. Thus the instantaneous quantities entering the signed energy
identity, including ||G||raw², provide no exponential-tail estimate,
even with actual initialized actions, HS increments, small raw distance,
the reference symmetry, and unchanged anchor forward features all
retained.

The states (31) are not asserted to be reached by theta^N. Therefore
this construction does not disprove the required integrated estimate
along that family. It does rule out obtaining it from the available
raw bounds and signed energy values by a pointwise tail inequality and
then integrating. The focused attempt yields (25)–(27) and the exact
obstruction (29)–(34), but no path-specific integrated exponential-tail
bound for the canonical cutoff family.
