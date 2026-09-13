##### C.4.7.10. Finite numerical autonomous observable closure

This section gives a finite numerical implementation of the same nonlinear
population physical gradient flow. Its exact model is C.4.7.8: no biases,
two tanh hidden layers, stored Gaussian variances (1,1/n,1/n²), mobilities
(n,1,n), unhalved squared loss, and both orientations of one reused initialized
Gaussian action. The finite-network interpretation retains its actual random
initial readout.

Fix T=1/200 and one rational two-arc law defined in part A. Part B specifies
a compatible dense closure, with exact prediction f_N at order N. Write
\(\mathfrak j=(\varepsilon,Q,P,m,J,p)\) for the numerical resolution
of part C: source regularization, initializer and population cubature, input
quadrature, number of time steps and arithmetic precision. Its finite
prediction is \(\widehat f_{N,\mathfrak j}\). Then

\[
 \widehat f_{N,\mathfrak j}\longrightarrow f_N,
 \qquad f_N\longrightarrow f_\mu
 \quad\hbox{in }C([0,T]\times S^1),
\]

with the iterated numerical order in part C.1. The same limits preserve
training-averaged initial/current activation pair laws in W2 and their RMS
displacements in both layers. Neither horizon nor law family shrinks. The
numerical state restarts from its own complete finite marks and coefficients;
at fixed resolution its working storage is independent of elapsed step count.

Part A proves the required explicit short-time population domain; it is not
an assertion that the represented laws belong to the older time-40 neighborhood.
Part B verifies density, both action directions and nonredundant odd-degree
enrichment. Part C proves every numerical limit and accounts for initialization,
evolution, precision and workspace. No rate, per-run error certificate, arbitrary
diagonal refinement or tolerance-to-resolution rule is asserted. Feasible
declared computations are a separate reproducible library validation.

Unqualified equation references within parts A and C carry their displayed
H3.S and H3.N prefixes. Part B uses H3.1–H3.3.

###### A.1. Statement and the executable family

Let `Z = sqrt(2) S^1 × [-1,1]`, write `u=x/sqrt(2)`, and use the transport cost
`|u-v|+|y-z|`. Set `T=1/200`. Use precisely the C.4 finite model

\[
 f_n(x)=n^{-1}(W^{(3)})^T\tanh(W^{(2)}\tanh(W^{(1)}u)),
\]

with no biases, independent stored centered Gaussian variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, and unhalved mean squared loss. All
times here are physical GF times. The finite initial readout is retained.

**Proposition.** Every Borel probability law `mu` on `Z` has a canonical
strong `C¹` population GF on `[0,T]`, unique among strong raw solutions on
the same canonical initialized action carrier. It is uniquely restartable
from each reached state for the remaining interval. The initial state is
`(w,K,c)=(g,0,0)`, with `g~N(0,I₂)`, retained initialized Gaussian action
`A0`, and its actual adjoint. The state space is

\[
 \mathcal E=L^2(\Omega_1;\mathbb R^2)\oplus
 \mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))\oplus L^2(\Omega_2),
 \qquad A=A_0+K.
\]

It has the exact energy identity, the explicit tails in part A.3, and
law-continuity in the sum of row `L²`, increment HS, and readout `L²` norms.
Actual finite GF for each fixed Borel law converges to it in the C.4.7.5
observation sense, including whole-circle predictions and finite same-layer
joint observations with second moments. The same conclusion holds for any
deterministic laws `lambda_j→mu` in `W1` and any widths `n_j→∞`; actual laws
may be Borel and need not be atomic. For iid empirical laws the convergence
holds in joint probability for arbitrary sample-count/width growth.

Here is a fixed finite-input subfamily, independent of order or accuracy.
Define

\[
 U(s)=\left(\frac{1-s^2}{1+s^2},\frac{2s}{1+s^2}\right),\qquad
 R_* =\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}.
\]

The input consists of five rational numbers `(p,a,b,c,d)` satisfying

\[
 1/3\le p\le2/3,\qquad
 -1/20\le a\le b\le1/20,\qquad -1/20\le c\le d\le1/20.
\]

Let `V_[a,b]` be uniform probability on `[a,b]` when `a<b` and `delta_a`
when `a=b`. Define

\[
 \mu=p\,\operatorname{Law}(\sqrt2 U(S),+1)
 +(1-p)\,\operatorname{Law}(\sqrt2 R_*U(V),-1),
 \quad S\sim V_{[a,b]},\ V\sim V_{[c,d]}.
 \tag{H3.S1}
\]

Only this mixture law is intended; no pairing between its two components is
used. Each nondegenerate component is nonatomic since `U` is injective on
these intervals. Both degenerate intervals give an explicit two-atom law.
Moreover `|U(s)-e1|=2|s|/sqrt(1+s²)≤1/10`; hence every cross-component pair
satisfies

\[
 2/5\le U(s)\cdot R_*U(v)\le4/5.                 \tag{H3.S2}
\]

Indeed its difference from `e1·R_*e1=3/5` is bounded by
`|U(s)-e1|+|U(v)-e1|≤1/5`. Thus this fixed family has nonorthogonal,
noncollinear inputs without invoking an unknown small radius.



For a cell of length `ell=(b-a)/m`, uniform-to-midpoint coupling has
`E|S-midpoint|=ell/4`. Since `|U'(s)|=2/(1+s²)≤2`, its input transport cost
is at most `ell/2`; rotation preserves distance and labels are unchanged.
Mixture coupling proves the returned error, which is at most `1/(20m)`.
Every atom's normalized coordinates and mass are rational; the original
input is `sqrt(2)` times its normalized coordinate. Thus this is a certified
law representation, not an exact-integration oracle. For example
`p=1/2,a=c=-1/20,b=d=1/20` is a specific nonatomic admissible law, while
`a=b=c=d=0` gives the nonorthogonal two-atom law.

###### A.2. Finite Euler programs and an unconditional source cap

Put `phi=tanh`. For every state define the typed fields

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),
 \quad f(u)=\langle c,H^2(u)\rangle_2,
\]
\[
 \Delta^2(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^2(u),
 \quad r(u,y)=f(u)-y.
\]

The exact vector field is

\[
 \mathcal F_\mu(w,K,c)=-2\left(
 \int r\phi'(w\cdot u)Q(u)u\,d\mu,
 \int r\Delta^2(u)\otimes H^1(u)\,d\mu,
 \int rH^2(u)\,d\mu\right).                         \tag{H3.S3}
\]

Each rank has HS norm equal to the product of its two `L²` norms. No
Hilbert–Schmidt assumption is made on `A0`; its operator norm is at most two
by the proved A.3 Gaussian bound.

For a finite law `sum_a p_a delta_(u_a,y_a)` and any positive finite mesh
`h_k` of total length at most `T`, define Euler directly by (H3.S3). Bounded gates
and bounded actions make every step a legitimate raw state. The fixed-program
theorem applies after expanding the learned increment into its finite sum
of ranks: the roots are Gaussian, both action orientations are of the same
initialized matrix, gates are smooth with bounded derivatives, and the only
unbounded products are bounded gates times named `L²` fields. A.1–2 supplies
their fixed-program value and named-source extension, with finite polynomial
derivative envelopes. Causal contractions use their earlier deterministic
population values. The program is finite before any width limit is used.
Zero or duplicated query covariances are covered by III.F.5. Thus neither an
inverse-Gram lower bound nor a minimum atom mass is required.

Fix the exact constants

\[
 T=1/200,\quad C=101/10000,\quad R=10101/10000=1+C,
 \quad B=1/32,
\]
\[
 D=B+2RC^2T,\quad
 A_B=4R\exp(6RDT+8R^2T^2C^2),\quad
 d_0=2RT+2C,\quad \Psi=d_0\exp\{d_0T(A_B+2R)\}.       \tag{H3.S4}
\]

The readout recurrence gives `||c_{k+1}||∞+1≤(1+2h_k)(||c_k||∞+1)`;
therefore `||c_k||∞≤e^(2T)-1<C`, `|r|≤R`. Summing rank and row updates gives

\[
 \|K_k\|_{\rm HS}\le2TRC<1/1000,\quad
 \|A_k\|_{\rm op}<201/100,\quad \|w_k\|_2<2,
 \quad\|\mathcal F_\mu(\theta_k)\|_{\rm sum}<3.        \tag{H3.S5}
\]

The row estimate uses `sqrt(2)+2TR(2+2TRC)C<2`; the speed bound uses
`2R((2+2TRC)C+C+1)<3`. All affine interpolants obey these bounds.

For completeness, the exact source calculation giving the cap is as follows.
At a training slot `(k,a)` put `m_ka=h_k p_a`, `gamma_ka=-2m_ka r_ka`.
Forward centered sources `xi` have covariance `E1[H1_i H1_j]`; reverse
centered sources `zeta` have covariance `E2[Delta2_i Delta2_j]`. Distinct
orientations are independent source groups. Answers include their response
terms, so this does not make the action and its adjoint independent.
For frozen deterministic contractions, residuals, covariances and previously
computed response coefficients, let

\[
 \alpha_{i,p}=E_1[\partial_{\zeta_p}H^1_i],\qquad
 \beta_{i,p}=E_2[\partial_{\xi_p}\Delta^2_i].
\]

III.F.4's source rule plus the finite learned-rank sum gives exactly

\[
 Z^2_i=\xi_i+\sum_{p<i}F_{i,p}\Delta^2_p,
 \quad F_{i,p}=\alpha_{i,p}+\gamma_p E_1[H^1_iH^1_p],
\]
\[
 Q_i=\zeta_i+\sum_{p\le i}D_{i,p}H^1_p,
 \quad D_{i,p}=\beta_{i,p}+\mathbf1_{p<i}\gamma_p E_2[\Delta^2_i\Delta^2_p].
                                                        \tag{H3.S6}
\]

Here `p<i` means a strictly earlier time for a memory term. There is only
one distinguished current forward source for each new output query. Its
current coefficient is `E2[c_k phi''(Z2_i)]`; all other current coefficients
are zero. Append a passive query after the active calls; unused previous
queries have zero derivatives. Formal sources remain separate names even
when covariance is singular.

Assume previous beta-row absolute sums are at most `B`. Then the corresponding
`D`-row sums are at most `D`, and

\[
 Q_i=\zeta_i+J_i,\qquad |J_i|\le D,\qquad E\zeta_i^2\le C^2. \tag{H3.S7}
\]

For any nonnegative `lambda`, Jensen with the time/atom weights and the scalar
Gaussian exponential integral gives

\[
 E\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le2\exp(\lambda TD+\lambda^2T^2C^2/2).                    \tag{H3.S8}
\]

The sum of weights is at most `T`; add a zero term if it is smaller. This
estimate needs no independence among times or inputs.

For a past reverse pulse `p=(s,b)`, let `v_{k;p}=partial_(zeta_p) w_k` and
`M_{k;p}=max_{s<j≤k}|v_{j;p}|`. Differentiating (H3.S3),(H3.S6) gives a direct pulse
of magnitude at most `2R m_p`, followed by a multiplicative increment bounded
by

\[
 2Rh_j\left(D+2\sum_a p_a|Q_{ja}|\right)M_{j;p}.
\]

Indeed the derivative of the lower gate contributes `2|Q||v|`, while each
old first-feature derivative in the `D` sum is bounded by the past pulse
maximum. The current feature derivative uses `w_j`, which is already fixed
before that update. Iteration with `1+x≤exp(x)` therefore gives

\[
 M_{k;p}/m_p\le2R\exp\left(2RDT+4R\sum_{j<k,a}h_jp_a|Q_{ja}|\right).
\]

Applying (H3.S8) yields

\[
 E M_{k;p}/m_p\le A_B,
 \quad |\alpha_{ku,p}|\le A_Bm_p,
 \quad |F_{ku,p}|\le(A_B+2R)m_p.                           \tag{H3.S9}
\]

For forward pulses write `U_i;p=partial_(xi_p) Z2_i`,
`C_k;p=partial_(xi_p)c_k`, `V_i;p=partial_(xi_p)Delta2_i`. Their exact
finite equations are

\[
 C_{k;p}=\sum_{q<k}\gamma_q\phi'(Z^2_q)U_{q;p},\quad
 U_{ku;p}=\mathbf1_{(k,u)=p}+\sum_{q<k}F_{ku,q}V_{q;p},
\]
\[
 V_{ku;p}=\phi'(Z^2_{ku})C_{k;p}+c_k\phi''(Z^2_{ku})U_{ku;p}.
\]

Let `mathcal U_k` be the largest absolute `U` derivative-row sum through
step `k`. Then the absolute `C` row is at most `2RT mathcal U_k`, and the
absolute `V` row is at most `d0 mathcal U_k`. Consequently

\[
 \mathcal U_k\le1+(A_B+2R)d_0\sum_{j<k}h_j\mathcal U_j
 \le\exp((A_B+2R)d_0T),\quad
 \sum_p|\beta_{ku,p}|\le\Psi.                             \tag{H3.S10}
\]

All right-hand memory terms are earlier ones. Lower pulses at the new node
use only previous beta rows; (H3.S9) then constructs its forward coefficients;
(H3.S10) constructs its current beta row. This is the causal induction which
makes a strict `Psi<B` sufficient without a circular current-row hypothesis.

Here is an elementary rational verification of that strict inequality.
For `0≤x<1`, `e^x≤1/(1-x)`. Also

\[
 e^{1/100}\le1+1/100+
 \frac{(1/100)^2}{2(1-(1/100)/3)}=60401/59800<R,
\]

because successive ratios after the quadratic term are at most `x/3`.
Direct rational substitutions in (H3.S4) give

\[
 D<1/31,\quad6RDT+8R^2T^2C^2<1/1000,
 \quad A_B<4R(1000/999)<41/10,
\]
\[
 A_B+2R<31/5,\quad d_0T(31/5)<1/1000,
 \quad\Psi<d_0(1000/999)<1/32=B.                         \tag{H3.S11}
\]

At initialization beta is zero. Equations (H3.S9)–(H3.S11) prove its cap for all
finite laws, all finite positive meshes of total length at most `T`, and all
passive directions. Zero atom masses may be discarded. There is no bound on
the number of atoms, covariance rank, or number of steps.

###### A.3. Individual tails, strong existence, and uniqueness

For `s≥D` define the explicit scalar majorant

\[
 \tau(s)=4(C+D)\exp\left(-\frac{(s-D)^2}{8C^2}\right).     \tag{H3.S12}
\]

Equation (H3.S7) implies `||Q 1_(|Q|>s)||2≤tau(s)`. To verify this without
assuming `zeta` and `J` independent, use `|Q|≤|zeta|+D` and put
`a=(s-D)/C`. Scalar Gaussian domination reduces to
`C|G|+D`, `G~N(0,1)`. On `|G|>a`, use
`1≤exp((G²-a²)/4)`. Completing the square gives
`E exp(G²/4)=sqrt(2)` and `E G² exp(G²/4)=2sqrt(2)`.
The squared tail is at most
`2 exp(-a²/4)(2sqrt(2) C²+sqrt(2)D²)`, below the square of (H3.S12).
The readout is bounded by `C`. These are uniform marginal estimates; they
make no assertion about the tail of a supremum over inputs or time.
An affine Euler state is an Euler prefix with one shorter final step, so the
same bounds hold for every recomputed interpolant query.

We give the completion rather than inferring existence from this cap. First,
the field (H3.S3) is jointly continuous in raw state and input. The only
non-Lipschitz-looking operation needed is a bounded continuous multiplier
times an `L²` field. If `z_j→z` in probability and `v_j→v` in `L²`, subtract
the varying vector first. For the remaining term, truncate fixed `v` at
`|v|≤M`, use bounded convergence in probability there, and control the
complement by `2||b||∞ ||v 1_(|v|>M)||2`. This proves
`b(z_j)v_j→b(z)v` in `L²`. Apply it at both backward gates; bounded actions
and the rank norm identity handle the other operations. Compactness of the
data domain makes convergence uniform in the input. Each integrand has
compact separable range and is bounded, hence is Bochner integrable in the
raw spaces. For fixed continuous Banach-valued `G`, coupling laws at mean
distance `q` bounds its integral difference by
`omega_G(a)+2||G||∞q/a`. First `q→0`, then `a→0`, proves joint field/law
continuity. No ambient `L²` algebra or locally Lipschitz population-ODE
assertion has been used.

Here is a quantitative one-reference comparison adequate for completion.
For the Euler ball (H3.S5), and `s≥1`, let `e` be sum raw state distance and
`q=W1(mu,nu)`. Subtracting the fields yields

\[
 \|\mathcal F_\mu(\theta)-\mathcal F_\nu(\bar\theta)\|_{\rm sum}
 \le L_s(e+q)+16\int\tau_s(\bar Q(u))\,d\nu,
 \qquad L_s=3000(1+s),                                  \tag{H3.S13}
\]

where `tau_s(v)=||v 1_(|v|>s)||2`; only the reference needs tails. One can
check the constant with bounds three on row norm, action norm, both readout
`L²` norms and the reference readout supremum, and residual bound four.
For a coupled input pair at distance `h=|u-v|`, the first preactivation,
second preactivation, prediction, upper backward field, and reverse query
differences are bounded respectively by
`3(e+h),9(e+h),28(e+h),55(e+h),168(e+h)`. Add `|y-z|` to the residual
difference. The lower gate difference is at most
`(168+6s)(e+h)+2 tau_s(Qbar)`, by splitting its reference factor at `s`.
The row, middle, and readout velocity differences are consequently bounded
by `(1920+48s)(e+h+|y-z|)+16 tau_s(Qbar)`,
`680(e+h+|y-z|)`, and `128(e+h+|y-z|)`, respectively. Their sum is below
(H3.S13), after coupling and taking the infimum of transport costs. For the
middle field the HS rank-difference bound is used. This verifies (H3.S13)
without substituting operator norm for HS distance.

Take finite laws `mu_j`, meshes of maximal step `h_j`, and their affine
Euler paths, all on the fixed common carrier. A preceding-node state differs
from its interpolant by at most `3h_j`. For two such paths, (H3.S13), (H3.S12), and
scalar integration of `e'≤L_s e+b` give

\[
 \sup_{t\le T}e_{ij}(t)
 \le T e^{L_sT}\left[
 L_s\{W_1(\mu_i,\mu_j)+3h_i+3h_j\}+16\tau(s)\right].     \tag{H3.S14}
\]

For every Borel `mu`, finite laws with `W1(mu_j,mu)→0` exist by partitioning
the compact data space into cells of shrinking diameter and moving each
cell's exact mass to a representative. Choose any meshes `h_j→0`. For fixed
`s`, the first term in (H3.S14) vanishes as `i,j→∞`; then
`e^(L_sT)tau(s)→0` as `s→∞`, since its exponent has a negative quadratic
term in `s` and only a positive linear term. Thus the paths are Cauchy in
the complete space `C([0,T];E)`. The same calculation between two choices
proves independence of all approximations.

Let their limit be `theta_mu`. Their preceding-node paths converge to the
same limit. Joint field continuity just proved passes the integrated Euler
equations to

\[
 \theta_\mu(t)=(g,0,0)+\int_0^t\mathcal F_\mu(\theta_\mu(v))\,dv. \tag{H3.S15}
\]

The field convergence is uniform in time: any allegedly discrepant times
have a convergent subsequence, and uniform state convergence gives the
same limiting state there, contradicting joint continuity. Thus the integral
in (H3.S15) is strongly `C¹`, with one-sided endpoint derivatives. This constructs
the full state equation, including its HS increment, not just predictions.

The source decomposition itself passes to this limit. Fix a time and input,
and append that passive query to the convergent finite programs. For their
joint union, the source covariance rule gives

\[
 \|\zeta_i-\zeta_j\|_2^2
 =\|\Delta^2_i-\Delta^2_j\|_2^2\longrightarrow0.           \tag{H3.S16}
\]

This identity uses the cross contractions of their actual common-carrier
upper fields. The joint centered sources are Gaussian, so their `L²` limit
is centered Gaussian with variance at most `C²`. The corresponding `Q_i`
converge in `L²` by field continuity; hence `J_i=Q_i-zeta_i` converge in
`L²`. An almost-sure subsequence retains `|J|≤D`. A fixed real passive input
can also be obtained by a sequence of rational directions, using joint
continuity and the same covariance identity. Thus (H3.S7),(H3.S12) hold at every
time/input of (H3.S15), with the same constants. They hold separately at each
such pair, which suffices for the law-averaged tails in (H3.S13).

The strong chain rule along `C¹ L²` curves follows directly from the scalar
mean-value identity and the bounded-multiplier argument above. Apply it to
the two activations, and the action product rule, to differentiate `f(u)`.
The three gradient blocks are `phi'(w·u)Q(u)u`,
`Delta2(u) tensor H1(u)`, and `H2(u)`. Their joint continuity on the compact
input/time domain justifies differentiating the law integral. Pairing with
(H3.S3) proves

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta'_\mu(v)\|_{\rm raw}^2dv
 =\int y^2d\mu\le1.                                     \tag{H3.S17}
\]

The readout equation and `int|r|dmu≤sqrt(L)≤1` give `||c(t)||∞≤2t`.
Coordinatewise integration is justified by Fubini for the bounded readout
velocity. The remaining rank and row integrals then give

\[
 \|K(t)\|_{\rm HS}\le2t^2,\quad
 \|A(t)\|_{\rm op}\le2+2t^2,\quad
 \|w(t)\|_2\le\sqrt2+4t^2+2t^4.                         \tag{H3.S18}
\]

For law continuity, apply (H3.S13) to two constructed paths and integrate as in
(H3.S14), with the mesh terms absent. Its infimum over integer `s≥1` is a
deterministic common modulus tending to zero as `q→0` (first fix `s`, then
send `q→0`, then `s→∞`). In particular this controls the whole-circle
predictions and both forward hidden fields.

For uniqueness, any competing strong raw solution on `[0,T]` has bounded
raw and action norms by continuity on this compact interval. Repeat the
subtractions of (H3.S13) with their finite common bound, yielding
`C_*(1+s)e+C_*tau(s)`; its reference is the constructed solution, with
bounded readout and (H3.S12). There is no tail assumption on the competitor.
Zero initial error and Gronwall give
`sup e≤C_*T exp(C_*(1+s)T)tau(s)→0`. Applying the same argument on
`[b,T]` proves uniqueness from any reached state at time `b`. Its existence
is the restriction of (H3.S15); no statement about arbitrary ambient endpoints
or switched training laws is needed.

###### A.4. Identification with actual finite GF

This step requires finite-program identification in addition to population
tails. At finite width, compactness of the data domain makes the exact
Borel-law vector field smooth on every bounded parameter set: all derivatives
of its integrand are uniformly bounded there, so difference quotients pass
under the integral. Local existence needs only the following contraction:
on a closed parameter ball, fix bounds for the field and its derivative;
choose a time interval so that integrating the speed stays inside the ball
and its length times the derivative bound is below one. Integration maps
continuous paths into that ball contractively. Its successive iterates
converge uniformly to the integral solution, and the contraction proves
uniqueness. The field is the negative loss gradient for squared metric

\[
 \|\dot w_n\|_F^2/n+\|\dot K_n\|_F^2+\|\dot c_n\|_2^2/n.
\]

The chain rule gives the finite counterpart of (H3.S17). On any finite maximal
interval, displacement is at most `sqrt(t L_n(0))`, and a terminal increment
is at most `sqrt(|t-s| L_n(0))`. Thus a finite endpoint exists, and local
smooth finite-dimensional existence extends the solution. This proves global
finite GF existence and uniqueness for every fixed Borel law.

The event `||A0,n||op≤10`, `||w0,n||F/sqrt(n)≤2`,
`||c0,n||∞≤1` has probability tending to one, independently of the law.
Here the Gaussian readout satisfies
`P(max_i|W3_i|>epsilon)≤2n exp(-n²epsilon²/2)`. On this event
`L_n(0)≤4`; energy gives law-independent raw/action bounds through `T` and
`||c_n(t)||∞≤1+4t`. This supplies a common deterministic comparison ball.

Fix a finite comparison law `nu` and a finite mesh `h`, before taking width
to infinity. Its population Euler program has a finite number of instructions.
Realize those instructions on the actual finite initialized arrays, retaining
the deterministic population residuals and contractions in its assigned
increments. Expand `K` into its finite rank sum. Include the actual finite
initial readout **additively in the proxy parameters**. Thus GF and proxy
start at exactly the same arrays. The proxy's assigned increments come from
the zero-population-readout program; its recomputed feedback is compared to
those assigned increments next.

III.F.1–7 and A.1–2 apply to that fixed graph with precisely the root, gate,
and source hypotheses checked in part A.2. They give all same-layer joint
second moments and hence scalar-contraction convergence. A finite induction
recovers the proxy's recomputed feedback: for a gate times an unbounded named
field, subtract the field error first and split the fixed reference field at
a cutoff in the gate error. Its joint second-moment convergence controls the
tail; let width increase at fixed cutoff, then remove the cutoff. Bounded
actions propagate the field errors. Additive initial-readout error tends to
zero in both RMS and supremum, so the same induction covers it. Hence all
recomputed proxy velocity defects at its finitely many nodes are `o_P(1)`.

The middle metric is identified exactly, not by a cross-carrier operator
comparison. If `K=sum_i a_i tensor b_i`, then

\[
 \|K\|_{\rm HS}^2=\sum_{i,j}\langle a_i,a_j\rangle_2
                                      \langle b_i,b_j\rangle_1.
\]

For finite ranks `a_i b_i^T/n` their ordinary Frobenius contraction is the
same finite double sum of normalized pairings, which converges by the
fixed-program theorem. The proxy consequently stays on a deterministic
enlargement of (H3.S5), with probability tending to one, and has bounded assigned
speed uniformly between its finitely many nodes.

For a fixed cutoff `s≥1`, second-moment convergence gives finite proxy tails.
The continuous map `v↦(|v|-s/2)_+` satisfies

\[
 \|v1_{|v|>s}\|_2\le2\|(|v|-s/2)_+\|_2\le2\tau_{s/2}(v).
\]

Since `s/2>D`, (H3.S12) and the finite-program limit therefore bound every
law-averaged proxy-node reverse tail by `2tau(s/2)+o_P(1)`. The proxy readout
has no tail at sufficiently large fixed `s`, since it is bounded by `C` plus
the vanishing initial-readout supremum. There are only finitely many such
nodes and training inputs for fixed `(nu,h)`. In particular this reasoning
does not claim finite tails uniform in a growing transcript.

Now let `lambda_j→mu` in `W1` and `n_j→∞`. The same finite-array subtractions
as in (H3.S13), with their common finite ball, compare actual GF for `lambda_j`
to the proxy, both on their common width-`n_j` carrier. The actual law may
be nonatomic; only the comparison law is finite. For a fixed cutoff `s` the
sum distance obeys, uniformly through `T`,

\[
 E_j\le C_*T e^{C_*(1+s)T}
 \left[(1+s)(W_1(\lambda_j,\nu)+h)
                    +2\tau(s/2)+o_{\mathbb P}(1)\right].  \tag{H3.S19}
\]

The mesh term comes from the proxy's bounded node/interpolant displacement;
the probability error includes the fixed-program velocity defects. Constants
are independent of the finite comparison law and its mesh. They need only
be finite, since the available tail is Gaussian in `s`.

For any desired error, first choose fixed `s` so that the amplified tail in
(H3.S19) is small. This is possible because its negative quadratic exponent
dominates the linear Gronwall exponent on the entire fixed interval. Next
choose finite `nu` close enough to `mu` and a small fixed mesh `h` so that
their amplified deterministic errors are small and their population Euler
path is close to (H3.S15). Only then let `j→∞`. Each random error in (H3.S19) concerns
this fixed finite graph and fixed cutoff; `W1(lambda_j,mu)→0`. This proves
arbitrarily accurate same-carrier proxy approximation to actual finite GF.
Taking `lambda_j=mu` gives the assertion for each exact Borel-law loss.

Forward/prediction formulas are Lipschitz on these balls, uniformly in input.
Fixed time/input nets, the finite-program limits on their nodes, the full-row
input Lipschitz bounds, and the bounded raw speeds give convergence uniform
in `t∈[0,T]` and `u∈S1` for predictions and the declared forward observations.
For a further fixed observation graph, each bounded action costs its operator
bound times the input error, plus HS increment error times the target input
norm. Globally Lipschitz gates preserve `L²` approximation. For a bounded
continuous gate times a fixed named `L²` field, use its cutoff, bounded
uniform continuity on a compact box, and the fixed-program second-moment
tails before removing the cutoff. Induction proves same-layer joint `W2`
convergence and quadratic contractions. Initial/current observations use a
single same-neuron tuple. No arbitrary unbounded products or cross-carrier
operator-norm convergence have been asserted.

For iid empirical laws, move the empirical and true law to a common finite
partition of diameter `b`. These moves cost at most `2b`. On that fixed
partition, the expected sum of cell-frequency errors tends to zero, since
each has variance at most `1/(4m)`. The remaining transport cost is bounded
by the data diameter times the total mass error. First `m→∞`, then `b→0`,
proves `W1` convergence in probability. The finitely many proxy events
depend only on initialization and its fixed comparison law; combine their
probability bounds with the data-distance event. No relative growth rate
between width and sample count is required.


###### B. Dense compatible hierarchy and relevant enrichments

Use the exact bias-free tanh model of C.4.7.8. Part C proves its finite numerical realization. Set T=1/200 and fix
one represented two-arc law from the short-time proposition. The proposition
constructs its canonical population GF (w,K,c), with A=A0+K, by finite common
Gaussian programs, proves its individual reverse-query tails and identifies
it with the actual finite-network GF retaining its random initial readout.
No finite-network approximation is used to run the closure.

The bounded initialized-word grammar consists of the constants on both
populations, first-population Gaussian seeds g1,g2, rational linear
combinations, sin/cos/tanh of permitted words, products of bounded words on
one population, and A0 or its actual adjoint on bounded operands. The
population type determines the orientation. Let the natural-number coding
be exactly C.4.7.9's coding: 0,1 are the two constants; 2,3 are g1,g2; for
n=4+8k+j, j=0,1,2,3 applies sin,cos,tanh,action to code k; for j=4,5,7,
unpair k by Cantor pairing and use addition, bounded product, addition;
for j=6, the first unpaired integer specifies a rational coefficient and the
second its operand. Type-invalid expressions are rejected. If the rational
index unpairs as (a,b), its numerator is 0 for a=0, (a+1)/2 for odd a,
and -a/2 for even positive a, and its denominator is b+1. This enumerates
every permitted finite word. Envelopes are exact rational metadata, never
rounded to float to decide boundedness. Literal syntax duplicates are shared;
no numerical or algebraic rank deletion is used.

Use h_i=tanh(g_i), xi_i=A0 h_i, H_i=tanh(xi_i), p_i=A0* H_i, for i=1,2.
With G a standard scalar Gaussian, set

\[
 v=E\tanh^2G,\quad \alpha=E[1-\tanh^2(\sqrt vG)],
 \quad \tau_0=E\tanh^2(\sqrt vG).
\]

All three constants are strictly positive. Oddness and independence give
E[h_i h_j]=v delta_ij. The complete finite-source rule of C.4.7.8 therefore
realizes the forward sources as independent N(0,v) variables and gives

\[
 p_i=\zeta_i+\alpha\tanh g_i,
 \qquad (\zeta_1,\zeta_2)\sim N(0,\tau_0 I_2),
\]

independently of g. Here E[partial_(xi_j)H_i]=alpha delta_ij; this is the
response term from the same reused action. The two population measures are
separate, and their quadrature indices are not paired across populations.

Put X1=(tanh g1,tanh g2,tanh p1,tanh p2) and X2=(tanh xi1,tanh xi2).
For order N>=1 retain all products of Chebyshev polynomials

\[
 \prod_{j=1}^{d_\ell}T_{a_j}(X_{\ell,j}),\quad
 a_j\ge0,\quad\sum_j a_j\le N,\qquad d_1=4,\ d_2=2,
\]

and append every bounded valid code through N not already present literally.
Use total degree followed by descending lexicographic exponent order for the
polynomial list, then increasing code order. Compiling a dependency does not
make it a retained feature. The recurrence T0=1,T1=x,T_(k+1)=2xT_k-T_(k-1)
expresses each polynomial as a bounded word. The identity T_k(cos theta)=
cos(k theta), obtained by induction from the cosine addition formula, proves
its absolute bound one on [-1,1].

The conditional Gaussian density of (g,p) is positive everywhere on R4.
The coordinatewise tanh diffeomorphism gives X1 a positive density on the
open four-cube; X2 similarly has a positive density on the open two-cube.
A polynomial zero almost surely is zero on that cube by continuity, and
is the zero polynomial by successively applying the one-variable root
property to every variable. The listed products have distinct leading
monomials and span all polynomials of total degree at most N. Their exact
span dimensions are binomial(N+4,4) and binomial(N+2,2). At N=1,2,3 the
appended code prefix contributes no new bounded word. The dimensions are
therefore (5,3), (15,6), (35,10), with strict enrichment in both populations.

Strict raw-span enrichment alone need not add a direction used by a particular
trajectory. For example, the new quadratic core features are even under the
joint core sign reversal, whereas the initialized hidden fields are odd.
Operational comparisons can therefore use the odd degrees N=1,3,5. Their
full retained counts are (5,3), (35,10), (128,21): the last first-population
list has 126 polynomial features and also the two syntactically distinct
constant tail words sin(1),cos(1). Those harmless duplicate functions are
retained according to the declared rule, rather than deleted by rank.

These odd degrees add initialized action information beyond the previous
upper span. To verify this exactly, let H=tanh(xi_1) and, for k=3 or 5,
let P_k be the monic degree-k polynomial orthogonal to lower-degree
polynomials for the law of H. The positive density on (-1,1) makes its
moment Gram positive definite, so it exists uniquely. Symmetry makes P_k
odd. It has k distinct roots in (-1,1): otherwise multiply it by the
product of its fewer-than-k sign-changing interior roots. The resulting
function has a fixed nonzero sign off finitely many points, contradicting
orthogonality to that lower-degree product. Interpolate artanh at those
k roots by a polynomial L of degree at most k-1. Repeated Rolle's theorem
gives, at every other x in (-1,1),

\[
 P_k(x)[\operatorname{artanh}(x)-L(x)]
 =\frac{\operatorname{artanh}^{(k)}(\xi_x)}{k!}P_k(x)^2>0,
\]

because for odd k,
artanh^(k)(x)=(k-1)![(1-x)^(-k)+(1+x)^(-k)]/2>0.
The product is integrable, since artanh(H)=xi_1 is Gaussian and P_k is
bounded. Orthogonality to L therefore gives E[P_k(H)xi_1]>0. Independence
of H1,H2 also makes P_k(H1) orthogonal to every previous upper polynomial
of total degree at most k-2. Nevertheless

\[
 E_2[P_k(H_1)A_0h_1]=E[P_k(H_1)\xi_1]>0.
\]

The same quantity is E1[(A0*P_k(H1))h1] by actual adjunction. Thus the
newly retained directions carry nonzero action information in the very
coupling used by the closure. This is a structural enrichment claim; it
does not assert an accuracy ordering between two finite degrees.

For polynomial-core features F(X1),B(X2), all initialized action contractions
reduce to bounded integrals in four and two independent scalar Gaussians:

\[
 E_2[B A_0F]=\sum_{i=1}^2
 E_1[Fh_i]E_2[\partial_{\xi_i}B]
 +\sum_{i=1}^2 E_1[\partial_{\zeta_i}F]E_2[BH_i].       \tag{H3.1}
\]

Indeed append A0F after the two reverse probes. Its source response is
sum_i E1[partial_(zeta_i)F]H_i, and its centered source has covariance
E1[Fh_i] with xi_i. Subtracting sum_i(E1[Fh_i]/v)xi_i leaves a centered
Gaussian independent of the old forward pair, including when its variance
is zero. Its product with B has expectation zero. Finally Gaussian
integration by parts gives E[B xi_i]=v E[partial_(xi_i)B]: the Gaussian
density derivative is -xi_i/v, the bounded B makes the boundary term zero,
and its derivative is bounded at fixed degree. Fubini applies. These steps
prove (H3.1). An innovation is integrated out of this contraction, not
deleted from a joint action law. The formula also applies to a retained
bounded smooth tail depending only on the same core coordinates. A new
action requires the full finite-source compiler, as in the numerical proof.

Let psi_l,N be the entire raw feature column, G_l,N=E[psi psi^T], and set
eta_N=1/[1024(N+1)^2]. Define lower Cholesky L_l,N by
G_l,N+eta_N I=L_l,N L_l,N^T, and b_l,N=L_l,N^-1 psi_l,N. If U_l,N
maps a coefficient vector to b_l,N^T times that vector, then

\[
 U_{\ell,N}^*U_{\ell,N}
 =I-\eta_N L_{\ell,N}^{-1}L_{\ell,N}^{-T}\le I,
 \qquad
 Q_{\ell,N}=U_{\ell,N}U_{\ell,N}^*
 =S_{\ell,N}(G_{\ell,N}+\eta_NI)^{-1}S_{\ell,N}^*,      \tag{H3.2}
\]

where S maps raw coefficients to psi^T times the vector. In particular Q is
a positive contraction. Its raw spans are nested and dense in the initialized
observable spaces: every bounded code eventually appears, and the rational
word/Fourier-cylinder density argument of C.4.7.9 applies without alteration.
For completeness the only filter estimate needed is, for a fixed raw-span
vector S a embedded at all later orders,

\[
 \|(I-Q_N)S_N a\|^2
 =\sum_j\frac{\eta_N^2\lambda_j}{(\lambda_j+\eta_N)^2}|a_j|^2
 \le\frac{\eta_N}{4}|a|^2.
\]

Here diagonalize the positive raw Gram and use
lambda/(lambda+eta)^2<=1/(4eta). Approximate any initialized observable-space
vector by a fixed raw-span vector and use ||I-Q_N||<=1. This proves Q_N→I
strongly. The initialized observable spaces contain the exact trajectory.
The sine/cosine cylinder argument of C.4.7.8 makes the bounded initialized
words dense in their generated L2 spaces. Both A0 and its adjoint take these
spaces into each other; adjointness makes the pair reducing. The initial
Gaussian coordinates belong to them by bounded truncation. Every finite-law
Euler step in part A preserves the generated sigma fields, and its learned
increment is a finite sum of ranks between the two spaces. Closedness in L2
and in the corresponding HS operator block passes this property to the strong
completion in part A. No assumption that the finite Gaussian core alone
generates these full spaces is made.

Set D_N=U_2,N* A0 U_1,N. The raw contraction C from (H3.1) or the full
source program gives D_N=L_2,N^-1 C L_1,N^-T; the right transpose is required.
Use the complete nonlinear equations of C.4.7.9 with these features and D_N.
This inverse-Cholesky choice is equivalent to symmetric whitening: if
R=G+eta I and O=L^-1 R^(1/2), then OO^T=I and b=O b^s. Transform
M=O2 M^s O1^T, a=O1 a^s, d=O2 d^s. Predictions, both action orientations,
row/readout equations and the Frobenius middle gradient all agree.

Here is the compatibility with the identical population GF, including the
change in dictionary and ridge. Lift the exact finite-order equations to the
fixed canonical carrier and put

\[
 B_N=Q_{2,N}A_0Q_{1,N},\qquad
 K_N=U_{2,N}(M_N-D_N)U_{1,N}^*.
\]

Their current action is B_N+K_N. The middle equation is exactly the rank
equation with Q2 and Q1 on its two factors. Energy differentiation uses the
same population pairings as the dynamics, so the unhalved loss is at most
one, ||c_N||_infty<=2t, ||M_N-D_N||_F<=2t^2, and ||K_N||_HS<=2t^2.
The operator bound on A0 and (H3.2) give ||B_N||<=2, uniformly in N.

Both B_N and its adjoint converge strongly to A0 and its adjoint. For example,
subtract Q2 A0(Q1 v-v)+(Q2-I)A0v and use boundedness and strong convergence.
Strong convergence of uniformly bounded operators is uniform on a compact
set, by a finite epsilon-net and the triangle inequality. Applied to the
continuous exact trajectory's compact (t,u) images h1 and delta2, this gives
the first two vanishing terms in

\[
 \epsilon_N=\sup_{t,u}\|(B_N-A_0)h^1(t,u)\|_2
 +\sup_{t,u}\|(B_N^*-A_0^*)\delta^2(t,u)\|_2
 +\sup_t\|Q_{2,N}\dot K(t)Q_{1,N}-\dot K(t)\|_{\rm HS}\to0. \tag{H3.3}
\]

For the last term approximate each HS operator by a finite sum of rank-one
operators. Strong convergence handles their finitely many factors; contractions
bound the discarded HS remainder. The same finite-net argument makes this
uniform on the compact image of the continuous exact derivative dot K.

Let e_N be the sum of row L2, middle HS and readout L2 distances. The
one-reference comparison in C.4.7.9 applies: its derivation uses precisely
the uniform bounds just checked, both strong action directions, and the
HS projection source in (H3.3). Splitting the exact reference reverse query
at magnitude s controls its multiplier, giving

\[
 D^+e_N(t)\le C(1+s)(e_N(t)+\epsilon_N)+C\tau(s),\qquad e_N(0)=0,
\]

where C is independent of N,s and the short-time proposition gives
tau(s)<=C0 exp[-c0(s-D0)^2]. This is the same estimate proved there for the
filtered closure; no tail bound on numerical or projected trajectories is
inserted as an assumption. Integrating the scalar inequality yields
sup_t e_N<=CT exp[C(1+s)T]((1+s)epsilon_N+tau(s)). First N→infinity at
fixed s and then s→infinity proves raw convergence, since a negative
quadratic dominates the positive linear exponent.

Direct subtraction of f=E[c tanh(A tanh(w·u))], using the action/row/readout
bounds and |tanh'|<=1, now proves sup_(t,u)|f_N-f_mu|→0. The same
subtraction for the initial and current hidden activations gives uniform
(t,u) L2 convergence in each population; initial upper activations use
B_N tanh(g·u) and converge by compact-target strong convergence. Keeping
initial and current values on the same carrier gives joint-pair W2 convergence.
Integrating against the fixed training law preserves it. RMS displacement
converges because it is the L2 norm of the difference of the two paired
activations and the reverse triangle inequality bounds changes of that norm.
The supported family and T have remained fixed throughout all limits.

Fix \(T=1/200\), write \(u=x/\sqrt2\in S^1\), and fix one represented
law \(\mu=\mathrm{ArcLaw}(\omega,a,b,c,d)\). Its rational parameters satisfy
\(1/3\le\omega\le2/3\), \(-1/20\le a\le b\le1/20\), and
\(-1/20\le c\le d\le1/20\). The first component has mass \(\omega\),
label \(+1\), and direction
\[
 U(s)=((1-s^2)/(1+s^2),2s/(1+s^2)),\qquad s\sim\mathrm{Unif}[a,b].
\]
The second has mass \(1-\omega\), label \(-1\), and direction \(RU(s)\)
with \(s\sim\mathrm{Unif}[c,d]\), where
\(R=\left(\begin{smallmatrix}3/5&-4/5\\4/5&3/5\end{smallmatrix}\right)\).
A degenerate interval denotes an atom. The family contains nonorthogonal
atomic and nonatomic laws, with exact finite input descriptions.

Part A supplies its unique canonical strong
Gaussian population gradient flow through \(T\), and identifies that flow
with the actual finite-network gradient-flow limit. The fixed conventions
are the bias-free two-hidden-layer tanh model, mobilities \((n,1,n)\),
unhalved squared loss, and physical time.

###### C.1. Finite equations and assertion

At order \(N\ge1\), retain all total-degree-at-most-\(N\) Chebyshev products
in the lower coordinates
\[
 (\tanh g_1,\tanh g_2,\tanh p_1,\tanh p_2),\qquad
 p_i=A_0^*\tanh(A_0\tanh g_i),
\]
and the upper coordinates \((\tanh\xi_1,\tanh\xi_2)\),
\(\xi_i=A_0\tanh g_i\). Append every bounded valid initialized-word code
through \(N\) not already present literally, in the exact coding and order
of part B. Word scalars and envelopes are exact
rationals; there is no empirical-rank test. Denote the raw columns by
\(\psi_\ell\), their lengths by \(d_\ell\), and set
\[
 \eta_N=\frac1{1024(N+1)^2},\quad G_\ell=E[\psi_\ell\psi_\ell^T],
 \quad L_\ell L_\ell^T=G_\ell+\eta_NI,\quad
 b_\ell=L_\ell^{-1}\psi_\ell,\quad
 D=L_2^{-1}CL_1^{-T},\quad C=E_2[\psi_2(A_0\psi_1)^T].       \tag{H3.N1}
\]
The joint marks are \(\lambda_1=\operatorname{Law}(b_1,g)\) and
\(\lambda_2=\operatorname{Law}(b_2)\). With \(w(0)=g,c(0)=0,M(0)=D\), put
\[
\begin{aligned}
 h_1(u)&=\tanh(w\cdot u),&a(u)&=E_1[b_1h_1(u)],\\
 h_2(u)&=\tanh(b_2^TMa(u)),&f(u)&=E_2[ch_2(u)],\\
 d(u)&=E_2[b_2c(1-h_2(u)^2)],&q(u)&=b_1^TM^Td(u).
\end{aligned}
\]
For \(r(u,y)=f(u)-y\), the finite equations are
\[
 \dot w=-2\int r(1-h_1^2)q\,u\,d\mu,\qquad
 \dot c=-2\int rh_2\,d\mu,\qquad
 \dot M=-2\int rda^T\,d\mu.                                \tag{H3.N2}
\]
These are exactly the contractions in the implementation. Both action
orientations use the one evolving \(M\) and its actual transpose.

The independent numerical parameters are as follows. A positive rational
\(\varepsilon\) adds \(\varepsilon I\) to generic source Grams; \(Q\)
Halton points compute initializer coefficients, Grams and \(C\); \(P\)
points replay the resulting complete joint mark laws with those coefficients
frozen. The two-arc midpoint rule has at most \(A=2m\) data points. Explicit
Heun uses \(J\) steps of intended length \(h=T/J\). Linear interpolation
of successive states defines all intermediate times; nonlinear activations
are evaluated on that state. The rational backend has precision \(p\ge20\)
and grid \(10^{-p}\mathbb Z\). All law parameters, \(\varepsilon\), and
the intended step are declared exactly. Resource allowances are adjustable
and must admit each requested finite computation.

**Theorem.** For every fixed represented law, \(N,\varepsilon,Q,P,m,J\),
the rational implementation, with adequate resource allowances, succeeds
for all sufficiently large \(p\) and converges to the corresponding exact
finite computation. Successive limits
\[
 p\to\infty,\quad J\to\infty,\quad m\to\infty,\quad
 P\to\infty,\quad Q\to\infty,\quad\varepsilon\downarrow0       \tag{H3.N3}
\]
give (H3.N1)–(H3.N2). The outer limit \(N\to\infty\) gives the canonical flow
through the same fixed \(T\). Convergence includes predictions uniformly
in \(t\in[0,T]\) and \(u\in S^1\), and, uniformly in time, the laws
\[
 \mathcal P_\ell(t)
 =\operatorname{Law}_{\lambda_\ell\otimes\mu}
       (h_\ell(0,u),h_\ell(t,u))                            \tag{H3.N4}
\]
in \(W_2\), and their RMS displacements
\[
 R_\ell(t)=\left(\int|z_2-z_1|^2\,d\mathcal P_\ell(t)(z)\right)^{1/2}.
                                                                  \tag{H3.N5}
\]
The upper initial coordinate uses the same \(g,b_1,b_2,D\) as the current
coordinate. At finite precision, normalize returned nonnegative product
weights only when interpreting (H3.N4) as a probability law; their total
mass tends to one in the first limit. The reported RMS, which uses the
actual returned weights, has the same limit. No vector-field weights
are changed by this convention.

Thus the limiting error is zero in the nested order
\[
 \lim_{N\to\infty}\lim_{\varepsilon\downarrow0}\lim_{Q\to\infty}
 \lim_{P\to\infty}\lim_{m\to\infty}\lim_{J\to\infty}\lim_{p\to\infty}.
                                                                  \tag{H3.N6}
\]
Each intermediate target exists in the stated observation metrics. The
\(\varepsilon\) limit is vacuous for the core implementation. This is
an iterated assertion: it gives neither an arbitrary diagonal nor a
universal computable tolerance schedule, affordable computation at every
order, or a broader family/horizon. The unbounded precision statement
uses the integer/rational backend; float64 and Decimal are additional
executable options.

###### C.2. Gaussian integration and adaptive initialization

We include the integration facts needed for adaptively chosen finite
coefficients. For the base-\(b\) radical inverse \(U_{k,b}\) of
\(1\le k\le Q\),
\[
 \frac1{bQ}\le U_{k,b}\le1-\frac1{bQ},\qquad
 D_{Q,b}\le\frac{1+(b-1)(\lfloor\log_bQ\rfloor+1)}Q.         \tag{H3.N7}
\]
An index has at most \(\lfloor\log_bQ\rfloor+1\) digits, giving the endpoint
bounds. Split \(0\le k<Q\) into base-\(b\) aligned blocks: there are
at most \((b-1)(\lfloor\log_bQ\rfloor+1)\) blocks, and a block of length
\(b^j\) has one point in each interval of length \(b^{-j}\), with
unnormalized interval discrepancy at most one. Replacing its index zero
by index \(Q\) changes any interval count by at most one, proving (H3.N7).
For distinct prime bases, fixing leading digit strings fixes residues
modulo coprime prime powers. The Chinese remainder bijection gives one
residue modulo their product and frequency error at most \(1/Q\).
Approximating rectangles by digit cylinders proves joint equidistribution.

Write \(X_k=-\log U_{k,b}\), \(M_Q=\log(bQ)\). Layer cake gives, for \(r>0\),
\[
 Q^{-1}\sum_{k\le Q}X_k^r1_{X_k>L}
 \le I_r(L)+D_{Q,b}M_Q^r,\quad
 I_r(L)=L^re^{-L}+\int_L^\infty rt^{r-1}e^{-t}\,dt.          \tag{H3.N8}
\]
When \(M_Q\le L\) the left side is zero. Otherwise, using
\(D_{Q,b}\le b\log(bQ)/(Q\log b)\), it is at most
\[
 I_r(L)+(b^2/\log b)L^{r+1}e^{-L}\quad(L\ge r+1),
\]
because \(z^{r+1}e^{-z}\) decreases there. This is uniform in \(Q\).
Pairwise Box–Muller pushes uniform Lebesgue measure to the joint standard
Gaussian, by the polar change of variables. Its singular endpoints have
measure zero, so truncation away from them proves weak convergence of
its Halton rules. With \(s\) pairs, their output satisfies
\[
 |z|^r1_{|z|>R}\le(2s)^{r/2}
       \sum_{j=1}^s X_j^{r/2}1_{X_j>R^2/(2s)},             \tag{H3.N9}
\]
since \(|z|^2\le2s\max_jX_j\). Hence all polynomial moments and their
uniform tails converge. Weak convergence and these tails imply \(W_r\)
convergence for every finite \(r\ge1\): couple common masses in small
cells of a bounded box with Gaussian-null boundaries; bound the remaining
transport by tail \(r\)-moments; enlarge the box and shrink the cells.

If \(\theta_Q\to\theta\) is a finite coefficient vector, and
\(F(\theta,z)\) is continuous with a common bound \(C(1+|z|^k)\) for
\(\theta\) near its limit, then
\[
 Q^{-1}\sum_{j\le Q}F(\theta_Q,z_j)\longrightarrow EF(\theta,Z). \tag{H3.N10}
\]
On a ball this follows from uniform continuity and weak convergence;
off it use a moment larger than \(k\) in (H3.N9). Applied to joint maps,
the same argument gives their \(W_r\) convergence when the required
moments are bounded. Crucially, \(\theta_Q\) may have been computed using
earlier integrals on the same cloud.

The generic compiler processes the complete typed union of retained words,
forward actions on each lower word, reverse actions on each upper word,
and their dependencies. Each literal action has a named source. Literal
duplicates share a node; empirical equality never identifies nodes. Each
population uses one joint Gaussian cloud, on separate probability spaces.
When a new action operand is \(v\), its source cross covariance with an
older operand \(v_j\) is \(E_Q[vv_j]\), and its variance is
\(E_Q[v^2]+\varepsilon\). Every older operand table and old Cholesky row
is preserved. Thus the entire covariance prefix is exactly its empirical
operand Gram plus \(\varepsilon I\), which is positive definite even
for dependent or zero operands. Appending one Cholesky row realizes the
new joint Gaussian without replacing old values.

An action equals its named Gaussian source plus
\(\sum_j E_Q[\partial_jv]v_j\) over old opposite-orientation actions.
The derivative is that of the explicit expression in named sources,
with covariance and response coefficients frozen. At an action the
reverse traversal adds its direct source derivative and propagates
through frozen response links. It does not differentiate the
opposite-population graph operand, Gaussian roots or estimated coefficients.
Coordinate nodes obey the usual chain/product rules. This is the formal
AD rule of the canonical finite Gaussian program, including nested responses.

Induct over the finite causal ordering. Each value and formal derivative
is continuous in finitely many Gaussian coordinates and earlier
coefficients, with a uniform polynomial Gaussian envelope on compact
coefficient sets. Bounded gates and derivatives, finite products and
response sums preserve these properties. Equation (H3.N10) applies to every
new coefficient/covariance. For fixed positive \(\varepsilon\), Cholesky
is continuous at every positive definite prefix. This proves convergence
as \(Q\to\infty\) of all coefficients, joint outputs, raw Grams and
the forward contraction \(C\). The reverse contraction is a diagnostic
from the same full program; it is not substituted into the dynamics.

For fixed \(Q,\varepsilon\), replay on \(P\) points uses exactly these
frozen factors and coefficients. It refits none of them. Equation (H3.N10)
therefore gives joint \(W_2\) convergence as \(P\to\infty\), including
the retained \(g\) coordinate. Reusing the existing cloud at \(P=Q\)
is the same rule and changes no limit.

After \(Q\to\infty\), remove \(\varepsilon\). Induct over the sources
again. New coefficients and covariances are expectations of continuous,
polynomially bounded functions of preceding jointly Gaussian sources.
Represent each complete source vector by its covariance's positive
semidefinite square root times a standard Gaussian. Such square roots
are continuous: every subsequence has a convergent subsubsequence of
bounded positive square roots; its limit squares to the limiting matrix,
and uniqueness identifies that limit. The uniform moment argument proves
continuity of all new expectations. This coupling is for the proof only;
it leaves all named sources and formal derivatives intact. Consequently
the limit is the canonical source recursion even for singular covariances.
Neither continuity of singular Cholesky factors nor deletion of a
zero-variance derivative slot is assumed.

The core calculation has the same limiting contractions. Set
\[
 v=E\tanh^2G>0,\quad \tau=E\tanh^2(\sqrt vG)>0,\quad
 \alpha=E[1-\tanh^2(\sqrt vG)]>0.
\]
Its lower joint law is \(g\sim N(0,I_2)\),
\(p=\sqrt\tau Z+\alpha\tanh g\), with \(Z\) independent, and its upper
law is \(\xi\sim N(0,vI_2)\). For bounded retained smooth functions
\(F(g,p),B(\xi)\),
\[
 E_2[BA_0F]=
 \sum_i E_1[F\tanh g_i]E_2[\partial_{\xi_i}B]
 +\sum_i E_1[\partial_{\zeta_i}F]E_2[B\tanh\xi_i],\quad
 \zeta=\sqrt\tau Z.                                      \tag{H3.N11}
\]
Append \(A_0F\) in the full source rule: its response gives the second
term, while its centered source has covariance \(E_1[F\tanh g_i]\)
with \(\xi_i\). Subtract Gaussian regression on \(\xi\); the remainder
is centered and independent of \(B\). Integration by parts
\(E[B\xi_i]=vE[\partial_{\xi_i}B]\) proves the first term. Boundedness
of \(B\) and its fixed-word derivatives justifies the Gaussian boundary
limit. This integrates out an innovation in one contraction without
replacing a joint action law.

The code computes both terms of (H3.N11), with the chain factors
\(1-\tanh^2p_i\) and \(1-\tanh^2\xi_i\). Its finite \(Q\) versions of
\(v,\tau,\alpha\) are strictly positive: the first Halton Gaussian
coordinate is nonzero, and exact finite \(\operatorname{sech}^2\) is
positive. Equation (H3.N10) proves their convergence, that of (H3.N11), and
that of the raw Grams. A tail using only these core actions uses the
same coordinates and derivatives; any new action triggers the generic
compiler. Source regularization is unused in the core calculation.

Each raw retained coordinate has a deterministic finite bound \(B_{\ell,j}\).
Chebyshev products have bound one, from \(T_k(\cos\theta)=\cos(k\theta)\).
Let \(B_\ell^2=\sum_jB_{\ell,j}^2\). For exact or empirical raw Grams,
\[
 |b_\ell|\le B_\ell/\sqrt{\eta_N}=:K_\ell,                 \tag{H3.N12}
\]
since \(L_\ell L_\ell^T\ge\eta_NI\). Ridge normalization is continuous
at fixed \(N\). The three transposes in (H3.N1) agree with inverse-lower
Cholesky normalization in the code. Every successive joint mark law
therefore converges in \(W_2\), and \(D\) converges in Frobenius norm.
The relevant \(D\)'s and second moments of \(g\) are bounded along
each such convergence. No contraction property of empirical marks
is needed for the next argument.

###### C.3. Fixed-dimensional existence and stability

Consider any probability mark laws with \(|b_\ell|\le K_\ell\),
\(E|g|^2<\infty\), and finite \(D\), and data with \(|y|\le1\).
On the Banach space of bounded increments \(w-g\), bounded \(c\), and
finite \(M\), (H3.N2) is locally Lipschitz: gates have bounded derivatives,
input norms are one, and other operations are bounded integrals and
finite products. The unbounded fixed \(g\) appears only inside gates.
Picard iteration is therefore a contraction on a sufficiently small
closed time-space ball and gives a unique local solution.

For \(\mathcal L=\int(f-y)^2d\mu\), differentiation under the bounded
integrals gives
\[
 \dot{\mathcal L}=-\|\dot w\|_2^2-\|\dot c\|_2^2-\|\dot M\|_F^2,
 \qquad\mathcal L(0)\le1.
\]
Indeed the negatives of (H3.N2) are respectively its population \(L^2\),
population \(L^2\), and Frobenius gradients. Thus \(\int|r|d\mu\le1\),
and
\[
 \|c(t)\|_\infty\le2t,\quad |a|\le K_1,\quad |d|\le2K_2t,\quad
 \|M(t)-D\|_F\le2K_1K_2t^2,\quad
 \|\dot w(t)\|_\infty\le4K_1K_2t\|M(t)\|_F.                \tag{H3.N13}
\]
These bounds prevent escape from a bounded Banach ball on \([0,T]\).
Local continuation gives existence and uniqueness there for general
or atomic mark laws, and an autonomous solution map.

Couple two lower joint laws and two upper mark laws. On these couplings,
define
\[
 e=\|w-\widetilde w\|_2+\|c-\widetilde c\|_2
                         +\|M-\widetilde M\|_F,\qquad
 \rho_b=\|b_1-\widetilde b_1\|_2+\|b_2-\widetilde b_2\|_2.
\]
For the same \(u\),
\[
 |a-\widetilde a|\le\|b_1-\widetilde b_1\|_2+
                                      K_1\|w-\widetilde w\|_2.
\]
Splitting the three factors of \(b_2^TMa\), then the factors of \(f,d,q\),
and using (H3.N13), bounds
\(\|h_2-\widetilde h_2\|_2,|f-\widetilde f|,|d-\widetilde d|,
\|q-\widetilde q\|_2\) by \(C(e+\rho_b)\). In particular the lower
gate product is controlled by
\[
 \|(h_1^2-\widetilde h_1^2)\widetilde q\|_2
 \le2\|\widetilde q\|_\infty\|w-\widetilde w\|_2,
\]
and the multiplier is bounded by (H3.N12)–(H3.N13).
For distinct directions,
\(\|h_1(u)-h_1(v)\|_2\le\|w\|_2|u-v|\); all other fields inherit a
bound \(C|u-v|\). Labels enter affinely, and the explicit \(u\) factor
is Lipschitz. Integrating a coupling of the data therefore bounds
the drift change by \(CW_1(\mu,\widetilde\mu)\). All constants use
only common \(K_\ell,\|D\|_F,\|g\|_2,T\) bounds. Subtracting (H3.N2),
integrating and summing the geometric series for its integral
inequality gives
\[
 \sup_{t\le T}e(t)\le e^{CT}
 \bigl(\|g-\widetilde g\|_2+\|D-\widetilde D\|_F+
              CT[\rho_b+W_1(\mu,\widetilde\mu)]\bigr).      \tag{H3.N14}
\]
This verifies both the existence and the stability hypotheses needed
by every numerical mark-law limit.

For the arc midpoint rule, mean parameter error is at most interval
length divided by \(4m\). Since \(|U'(s)|=2/(1+s^2)\le2\), mean direction
error is at most \(1/(20m)\). Couple mixture components identically;
labels then agree, and degenerate intervals have zero error.
The data rules converge in \(W_1\). Equation (H3.N14) first removes \(m\),
then \(P\), then the initializer errors \(Q,\varepsilon\) proved above.

###### C.4. Time and arithmetic limits

Fix \(N,\varepsilon,Q,P,m\) and first use exact arithmetic. The finite
ODE is smooth. Its Heun nodes and stages are bounded independently of
\(J\), without assuming a discrete energy inequality. Set
\(B_k=1+\|c_k\|_\infty\). Since \(|f-y|\le B_k\), its first stage
satisfies \(B_k^*\le(1+2h)B_k\), and
\[
 B_{k+1}\le(1+2h+2h^2)B_k\le e^{(2+2T)h}B_k.
\]
Thus all stages have bound \(B_*=(1+2T)e^{(2+2T)T}\). Their matrix
velocity is at most \(V_M=2B_*K_1K_2(B_*-1)\), hence
\(\|M\|_F\le\|D\|_F+2TV_M\). Their row velocity is then at most
\(2B_*K_1K_2(\|D\|_F+2TV_M)(B_*-1)\), also bounding \(w-g\).
On a slightly larger bounded set the vector field is Lipschitz.
The exact solution has one-step Euler defect \(O(h^2)\), since its
velocity is Lipschitz in time; Heun differs from Euler by \(O(h^2)\).
Consequently \(e_{k+1}\le(1+Ch)e_k+Ch^2\), and summing gives
\(\max_ke_k\le C_Th\). Linear interpolation adds \(O(h)\).
This proves uniform-time consistency; a stronger order is unnecessary.

Now fix all finite parameters including \(J\) and let \(p\to\infty\).
Put \(\delta=10^{-p}\). The rational backend retains integer units
over scale \(10^p\). Nearest rounding, including negative ties, has
error at most \(\delta/2\). Addition/subtraction of represented
values are exact; multiplication and division round once. These
operations are locally uniformly consistent, with a nonzero
denominator margin for division. Integer powers terminate by repeated
squaring. Integer square root has error less than \(\delta\);
consistency at zero uses
\(|\sqrt x-\sqrt y|\le\sqrt{|x-y|}\).

The elementary functions are finite algorithms. Exact power-of-two
reduction puts a positive logarithm argument in \([1,2)\). Its series
\(2\sum_{k\ge0}z^{2k+1}/(2k+1)\), \(0\le z\le1/3\), has a geometric
tail; the implemented tolerances give total log error at most
\(\delta/2+\delta/(4\cdot10^5)\), including the multiple of \(\log2\).
For exponential, reduce \(|x|/2^s\le1/2\), sum Taylor terms, and square
exactly. The amplification of the omitted tail is at most
\(2^se^{2|x|}\); the guard \(\lceil2|x|\rceil+s+5\) decimal places
dominates it. The pre-rounding error is at most \(10^{-5}\delta\).
Reciprocation for negative arguments cannot amplify the discrepancy
because both positive exponentials are at least one.

Pi is computed by the alternating series for
\(16\arctan(1/5)-4\arctan(1/239)\); the tangent addition identity
identifies pi, and the error is at most \(20\,10^{-p-5}\).
Exact rational reduction modulo its computed \(2\pi\) places trig
arguments inside \((-16/5,16/5)\). After the first generated term,
Taylor terms decrease absolutely, so the alternating tail at stopping
is at most \(10^{-p-5}\). With pi computed at precision \(p+5\),
the sine/cosine error on \(|x|\le M\) is at most
\[
 \delta/2+10^{-p-5}+40(M/6+1)10^{-p-10}.                  \tag{H3.N15}
\]
Periodicity handles changes in the reduction quotient. Tanh uses
\(e=e^{-2|x|}\), \(\pm(1-e)/(1+e)\), with denominator at least one.
Thus every elementary routine terminates and is locally uniformly
consistent on its continuous domain.

For fixed finite Gaussian clouds, exact Halton uniforms are strictly
between zero and one and eventually round positive. If the rounded
uniform is below one, it is at most \(1-\delta\); the log bound above
ensures a negative computed logarithm. If it rounds to one, its
radius is zero. All Box–Muller points eventually exist and converge.
Every exact source Gram plus \(\varepsilon I\) and feature Gram plus
\(\eta_N I\) is positive definite. Induction over finite Cholesky
operations proves convergence, and each exact positive pivot supplies
a margin ensuring eventual success. The core variances/response
have the same strict-margin property. Matrix inputs in this pipeline
are already converted to the chosen arithmetic, as required by the
Cholesky helper.

Dictionary decisions use exact words/rationals. Skipping a numerically
zero response coefficient is equivalent to multiplying by zero, so
it preserves consistency even at a limiting zero. Weight rounding
has total error at most the number of weights times \(\delta/2\);
validators permit that number times \(10^5\delta\). Each exact arc
coordinate rounds with error at most \(\delta/2\), so two squarings
and addition perturb its unit squared norm by less than \(4\delta\),
inside the \(10^5\delta\) allowance. Repeated validation does not
renormalize the data. Thus the shrinking-tolerance validation checks
also eventually pass; continuity alone would not establish this.

All remaining fixed computations are finite compositions of these
consistent operations. Induction proves convergence of the state
and observations at each of the finitely many steps. It is uniform
over input direction and interpolation fraction: their domains
are compact, intermediate values bounded, and primitive convergence
locally uniform. For evaluating all \(u\in S^1\), take their directly
rounded coordinates; the same unit-norm bound applies. Intended
time \(J(T/J)\) and represented time differ by at most \(J\delta/2\).
This proves the first limit of (H3.N3), including eventual precision
success, before removing the time step. It does not cover a diagonal
with positive pivots shrinking faster than precision resolves.

###### C.5. Observations, composition and own-state restart

part C.3 bounds prediction errors and both current activation errors
in \(L^2\), uniformly in \(u,t\), by \(C(e+\rho_b)\).
Initial lower error is at most \(\|g-\widetilde g\|_2\), and initial
upper error has the same product bound with \(M=D,w=g\).
Keeping both coordinates on the same mark coupling therefore proves
joint-pair \(W_2\) convergence. For data-law changes the additional
squared transport cost is at most \(CE|u-v|^2\le C'E|u-v|\), by the
input estimates and bounded circle diameter. This proves convergence
of the training averages in (H3.N4); \(u,y\) may also be retained in the
coupled law. The reverse triangle inequality in \(L^2\) bounds the
change of (H3.N5) by the \(L^2\) error of its displacement coordinate.
Rounded RMS converges too, by square-root continuity including zero.

Parts C.2–C.4 remove every inner error in (H3.N6). Part B supplies the final outer limit for exactly (H3.N1): its
positive filters converge strongly to identity, both directions of
\(Q_{2,N}A_0Q_{1,N}\) converge strongly, and projected middle
Hilbert–Schmidt sources converge on the exact trajectory's compact
targets. Part A supplies the strong reference
and Gaussian reverse-query tails. Their one-reference comparison
therefore gives strong trajectory convergence and precisely these
uniform-circle, pair-law and RMS observations. The family, horizon,
dictionary, ridge and GF conventions agree, proving (H3.N6).

The equations are autonomous. A checkpoint stores
\(b_1,g,w,p_1,b_2,c,p_2,M,D\), finite data and arithmetic metadata.
Rational values use hexadecimal integer units and precision;
Decimal uses exact strings and float64 hexadecimal values. Loading
recovers the same working values and validates without changing
weights. Thus, at a step endpoint, identical arithmetic, data,
step sizes and block size reproduce the same subsequent working
states. No source tape, clock, previous velocity or growing history
enters the step map. The limiting population solution has its own
restart property by uniqueness in part C.3; (H3.N14), with restart
state error included in \(e(0)\), proves convergence to that restart.
Interpolating an interior observation does not assert that a fresh
Heun mesh from that time equals the previous finite mesh.

###### C.6. Work, storage and scalar bits

The following bounds count scalar operations; scalar bit cost is
additional. With equal population counts \(P\), the retained state
contains
\[
 S=P(d_1+d_2+7)+2d_1d_2                                  \tag{H3.N16}
\]
scalars, and data contain \(4A\). Metadata and exact input/syntax
descriptions have additional finite bit size. Each retained pair
array has \(2PA\) scalars; the streamed RMS option avoids those arrays.
The coefficient-first products \(b_2(Ma)\), \(b_1(M^Td)\), and
\(b_2(Da_0)\) give right-side work
\[
 O\bigl(A[P(d_1+d_2+1)+d_1d_2]+S+A\bigr).                 \tag{H3.N17}
\]
Heun multiplies this by \(O(J)\). At block size \(B\le A\), workspace is
\[
 O(S+A+PB+B(d_1+d_2)+d_1d_2).                             \tag{H3.N18}
\]
A constant number of stages or endpoints changes only the constant;
memory need not grow with elapsed steps. Forward prediction on \(V\)
directions has the corresponding forward-only cost with \(A=V\).
A finite panel is not a certificate for a continuum supremum.

Let \(K\) be the full typed compiler DAG node count, \(s\) its number
of named sources, and \(d=d_1+d_2\). At most \(E=2K+s^2\) coordinate
and response edges occur. A conservative generic initializer work bound is
\[
 O\bigl(QsE+Qs^2+s^3+(Q+P)E+(Q+P)d^2+d^3\bigr),           \tag{H3.N19}
\]
plus generation of finitely many prime bases and
\(O((Q+P)(s+2)\log(Q+P+1))\) digit operations and elementary Gaussian
transforms. Each AD walk visits at most \(E\) edges on \(Q\) entries,
at most \(s\) times; pair covariances, new Cholesky rows, replay,
Grams, contractions and normalization give the other terms.
Its workspace is \(O((Q+P)(K+s+d)+s^2+d^2)\) scalars.
The core has fixed Gaussian dimensions four and two, work
\(O((Q+P)(N+1)d+(Q+P)d^2+d^3)\), and workspace
\(O((Q+P)(d+N+1)+d^2)\). Releasing coefficient tables before replay
improves constants.

Exact word construction adds finite integer/DAG work. Every natural
code has strictly smaller dependency codes, so the iterative decoder
terminates. Cached child hashes and iterative syntax equality avoid
expanding shared polynomial trees. Prefix memoization uses
\(O(N+K)\) syntax nodes, with exact scalar/envelope bit sizes counted.
Syntax caches can persist between initializer calls; they are not
source coefficient tables or training history. The small recursive
core-tail evaluator does not impose an order ceiling: code
\(62=\tanh(A_0 1)\) already introduces a non-core action, after
which the dispatch uses the iterative full compiler.

For a retained rational scalar bounded by \(M_*\), the maximum units
and scale bit size is
\[
 \beta=O(p+\log(1+M_*)).                                 \tag{H3.N20}
\]
Thus retained numerical storage is \(O((S+A)\beta)\) bits plus
metadata. Workspace scalar counts above likewise require their
maximum scalar bit size. Gaussian endpoint bounds give
\(|z|\le C_s\sqrt{\log(b_{\max}\max(P,Q))}\); finite coefficient
induction, bounded marks and (H3.N13) bound remaining magnitudes.
At fixed outer parameters they are uniform for sufficiently large
precision. The retained-byte diagnostic includes rational units
and scales; it is not a process-wide peak memory measurement.

Basic-operation work must be weighted by integer arithmetic cost.
Elementary calls additionally hold exact temporary Fractions. On
fixed bounded operand sets, away from zero for logarithm/division,
a conservative bound is \(O(p^2\log(p+2))\) bits per temporary rational
and \(O(p)\) series iterations, with operand-dependent constants.
For log/exp, term denominators divide a power of one \(O(p)\)-bit
base denominator times the product of \(O(p)\) small integer factors;
the common denominator therefore has \(O(p^2+p\log(p+2))\) bits.
The computed pi has \(O(p\log(p+2))\) denominator bits; reduction
and \(O(p)\) trig powers enlarge this to \(O(p^2\log(p+2))\).
Geometric and Taylor tails give \(O(p)\) iterations.
Exact squaring has a fixed operand-dependent
number of stages. Weighting (H3.N17)–(H3.N19) by these integer costs and
adding temporary Fraction storage yields finite bit-work/space
bounds. Large operands can make the constants large.
API byte/work estimates are adjustable resource guards, not certified
peak-bit bounds, and must grow as required along all refinements,
including precision. There is no fixed precision ceiling in the
integer/rational algorithm under the usual unbounded-resource
interpretation of these finite computations.

This proves all stated numerical limits and resource assertions.

