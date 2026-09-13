# An explicit short-time law domain for the exact two-hidden tanh flow

Status: new contained proof candidate, with exact scalar checks; not independently
reviewed or promoted. This closes the law-domain implication needed to apply the
C-H2 **outer convergence argument** at physical time `T=1/200`. It does not
certify a numerical closure, give an effective closure order, or assert a
quantified hidden-activity margin for every law below.

Author: scoped agent `/root/h3v2_scope`, 2026-09-13. No trajectory experiment and
no Git mutation were performed. The allowed research inputs were
`docs/NOTATION.md`, C.4–C.4.4 and C.4.7.1–5,8–9 of
`docs/global_nonlinear.md`, `H3_stability_proof.md`, `H3_stability.py`, and their
required maintained proof dependencies. Actual scientific reads used C.4's
model, complete C.4.1–2, complete C.4.7.1–5,8–9, A.1–4, and complete III.F.1–10
of `docs/special_data_limits.md`. No other study or route was read. Required
AGENTS/workflow and solve-math-rigorously/investigate-conjectures skills and
their research-contract/adversarial-audit references were read.

The proof imports the **proved finite-program/common-action construction** in
III.F.1–10, with its bounded-product extensions A.1–2 and sharp action bound
A.3. Its hypotheses are checked below. The uniform source estimate is reproved
from the exact finite source equations. No existential law radius or local
existence time is imported. The state completion, uniqueness, finite-GF bridge,
and the extension of C-H2's domain are provided explicitly.

## 1. Statement and the executable family

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

It has the exact energy identity, the explicit tails in section 3, and
law-continuity in the sum of row `L²`, increment HS, and readout `L²` norms.
Actual finite GF for each fixed Borel law converges to it in the C.4.7.5
observation sense, including whole-circle predictions and finite same-layer
joint observations with second moments. The same conclusion holds for any
deterministic laws `lambda_j→mu` in `W1` and any widths `n_j→∞`; actual laws
may be Borel and need not be atomic. For iid empirical laws the convergence
holds in joint probability for arbitrary sample-count/width growth.

The fixed C-H2 construction in C.4.7.9, at every integer order `N`, converges
to this flow for each such law on `[0,T]`, with precisely its stated raw,
whole-circle prediction, fixed-observation `W2`, and quadratic-contraction
conclusions. This is a direct extension of its convergence proof to this
short-time domain. It does not assert that these laws belong to its earlier
existential time-40 neighborhood.

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
 \tag{1}
\]

Only this mixture law is intended; no pairing between its two components is
used. Each nondegenerate component is nonatomic since `U` is injective on
these intervals. Both degenerate intervals give an explicit two-atom law.
Moreover `|U(s)-e1|=2|s|/sqrt(1+s²)≤1/10`; hence every cross-component pair
satisfies

\[
 2/5\le U(s)\cdot R_*U(v)\le4/5.                 \tag{2}
\]

Indeed its difference from `e1·R_*e1=3/5` is bounded by
`|U(s)-e1|+|U(v)-e1|≤1/5`. Thus this fixed family has nonorthogonal,
noncollinear inputs without invoking an unknown small radius.

The following exact rational interface returns normalized input directions,
labels, masses, and a proved transport error. It uses only Python's standard
`Fraction` type. It can be copied and run; it never queries a trajectory.

```python
from fractions import Fraction as F

def two_arc_rule(p, a, b, c, d, m):
    p, a, b, c, d = map(F, (p, a, b, c, d))
    if not isinstance(m, int) or isinstance(m, bool) or m < 1:
        raise ValueError("m must be a positive integer")
    if not (F(1,3) <= p <= F(2,3)
            and -F(1,20) <= a <= b <= F(1,20)
            and -F(1,20) <= c <= d <= F(1,20)):
        raise ValueError("outside the fixed rational two-arc family")
    atoms = []
    for mass, lo, hi, label, rotated in (
            (p, a, b, 1, False), (1-p, c, d, -1, True)):
        nodes = [(lo, mass)] if lo == hi else [
            (lo+(hi-lo)*F(2*j+1,2*m), mass/m) for j in range(m)]
        for s, weight in nodes:
            u1, u2 = (1-s*s)/(1+s*s), 2*s/(1+s*s)
            if rotated:
                u1, u2 = (3*u1-4*u2)/5, (4*u1+3*u2)/5
            atoms.append(((u1, u2), F(label), weight))
    error = (p*(b-a)+(1-p)*(d-c))/(2*m)
    return atoms, error
```

For a cell of length `ell=(b-a)/m`, uniform-to-midpoint coupling has
`E|S-midpoint|=ell/4`. Since `|U'(s)|=2/(1+s²)≤2`, its input transport cost
is at most `ell/2`; rotation preserves distance and labels are unchanged.
Mixture coupling proves the returned error, which is at most `1/(20m)`.
Every atom's normalized coordinates and mass are rational; the original
input is `sqrt(2)` times its normalized coordinate. Thus this is a certified
law representation, not an exact-integration oracle. For example
`p=1/2,a=c=-1/20,b=d=1/20` is a specific nonatomic admissible law, while
`a=b=c=d=0` gives the nonorthogonal two-atom law.

## 2. Finite Euler programs and an unconditional source cap

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
 \int rH^2(u)\,d\mu\right).                         \tag{3}
\]

Each rank has HS norm equal to the product of its two `L²` norms. No
Hilbert–Schmidt assumption is made on `A0`; its operator norm is at most two
by the proved A.3 Gaussian bound.

For a finite law `sum_a p_a delta_(u_a,y_a)` and any positive finite mesh
`h_k` of total length at most `T`, define Euler directly by (3). Bounded gates
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
 d_0=2RT+2C,\quad \Psi=d_0\exp\{d_0T(A_B+2R)\}.       \tag{4}
\]

The readout recurrence gives `||c_{k+1}||∞+1≤(1+2h_k)(||c_k||∞+1)`;
therefore `||c_k||∞≤e^(2T)-1<C`, `|r|≤R`. Summing rank and row updates gives

\[
 \|K_k\|_{\rm HS}\le2TRC<1/1000,\quad
 \|A_k\|_{\rm op}<201/100,\quad \|w_k\|_2<2,
 \quad\|\mathcal F_\mu(\theta_k)\|_{\rm sum}<3.        \tag{5}
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
                                                        \tag{6}
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
 Q_i=\zeta_i+J_i,\qquad |J_i|\le D,\qquad E\zeta_i^2\le C^2. \tag{7}
\]

For any nonnegative `lambda`, Jensen with the time/atom weights and the scalar
Gaussian exponential integral gives

\[
 E\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le2\exp(\lambda TD+\lambda^2T^2C^2/2).                    \tag{8}
\]

The sum of weights is at most `T`; add a zero term if it is smaller. This
estimate needs no independence among times or inputs.

For a past reverse pulse `p=(s,b)`, let `v_{k;p}=partial_(zeta_p) w_k` and
`M_{k;p}=max_{s<j≤k}|v_{j;p}|`. Differentiating (3),(6) gives a direct pulse
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

Applying (8) yields

\[
 E M_{k;p}/m_p\le A_B,
 \quad |\alpha_{ku,p}|\le A_Bm_p,
 \quad |F_{ku,p}|\le(A_B+2R)m_p.                           \tag{9}
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
 \sum_p|\beta_{ku,p}|\le\Psi.                             \tag{10}
\]

All right-hand memory terms are earlier ones. Lower pulses at the new node
use only previous beta rows; (9) then constructs its forward coefficients;
(10) constructs its current beta row. This is the causal induction which
makes a strict `Psi<B` sufficient without a circular current-row hypothesis.

Here is an elementary rational verification of that strict inequality.
For `0≤x<1`, `e^x≤1/(1-x)`. Also

\[
 e^{1/100}\le1+1/100+
 \frac{(1/100)^2}{2(1-(1/100)/3)}=60401/59800<R,
\]

because successive ratios after the quadratic term are at most `x/3`.
Direct rational substitutions in (4) give

\[
 D<1/31,\quad6RDT+8R^2T^2C^2<1/1000,
 \quad A_B<4R(1000/999)<41/10,
\]
\[
 A_B+2R<31/5,\quad d_0T(31/5)<1/1000,
 \quad\Psi<d_0(1000/999)<1/32=B.                         \tag{11}
\]

At initialization beta is zero. Equations (9)–(11) prove its cap for all
finite laws, all finite positive meshes of total length at most `T`, and all
passive directions. Zero atom masses may be discarded. There is no bound on
the number of atoms, covariance rank, or number of steps.

## 3. Individual tails, strong existence, and uniqueness

For `s≥D` define the explicit scalar majorant

\[
 \tau(s)=4(C+D)\exp\left(-\frac{(s-D)^2}{8C^2}\right).     \tag{12}
\]

Equation (7) implies `||Q 1_(|Q|>s)||2≤tau(s)`. To verify this without
assuming `zeta` and `J` independent, use `|Q|≤|zeta|+D` and put
`a=(s-D)/C`. Scalar Gaussian domination reduces to
`C|G|+D`, `G~N(0,1)`. On `|G|>a`, use
`1≤exp((G²-a²)/4)`. Completing the square gives
`E exp(G²/4)=sqrt(2)` and `E G² exp(G²/4)=2sqrt(2)`.
The squared tail is at most
`2 exp(-a²/4)(2sqrt(2) C²+sqrt(2)D²)`, below the square of (12).
The readout is bounded by `C`. These are uniform marginal estimates; they
make no assertion about the tail of a supremum over inputs or time.
An affine Euler state is an Euler prefix with one shorter final step, so the
same bounds hold for every recomputed interpolant query.

We give the completion rather than inferring existence from this cap. First,
the field (3) is jointly continuous in raw state and input. The only
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
For the Euler ball (5), and `s≥1`, let `e` be sum raw state distance and
`q=W1(mu,nu)`. Subtracting the fields yields

\[
 \|\mathcal F_\mu(\theta)-\mathcal F_\nu(\bar\theta)\|_{\rm sum}
 \le L_s(e+q)+16\int\tau_s(\bar Q(u))\,d\nu,
 \qquad L_s=3000(1+s),                                  \tag{13}
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
(13), after coupling and taking the infimum of transport costs. For the
middle field the HS rank-difference bound is used. This verifies (13)
without substituting operator norm for HS distance.

Take finite laws `mu_j`, meshes of maximal step `h_j`, and their affine
Euler paths, all on the fixed common carrier. A preceding-node state differs
from its interpolant by at most `3h_j`. For two such paths, (13), (12), and
scalar integration of `e'≤L_s e+b` give

\[
 \sup_{t\le T}e_{ij}(t)
 \le T e^{L_sT}\left[
 L_s\{W_1(\mu_i,\mu_j)+3h_i+3h_j\}+16\tau(s)\right].     \tag{14}
\]

For every Borel `mu`, finite laws with `W1(mu_j,mu)→0` exist by partitioning
the compact data space into cells of shrinking diameter and moving each
cell's exact mass to a representative. Choose any meshes `h_j→0`. For fixed
`s`, the first term in (14) vanishes as `i,j→∞`; then
`e^(L_sT)tau(s)→0` as `s→∞`, since its exponent has a negative quadratic
term in `s` and only a positive linear term. Thus the paths are Cauchy in
the complete space `C([0,T];E)`. The same calculation between two choices
proves independence of all approximations.

Let their limit be `theta_mu`. Their preceding-node paths converge to the
same limit. Joint field continuity just proved passes the integrated Euler
equations to

\[
 \theta_\mu(t)=(g,0,0)+\int_0^t\mathcal F_\mu(\theta_\mu(v))\,dv. \tag{15}
\]

The field convergence is uniform in time: any allegedly discrepant times
have a convergent subsequence, and uniform state convergence gives the
same limiting state there, contradicting joint continuity. Thus the integral
in (15) is strongly `C¹`, with one-sided endpoint derivatives. This constructs
the full state equation, including its HS increment, not just predictions.

The source decomposition itself passes to this limit. Fix a time and input,
and append that passive query to the convergent finite programs. For their
joint union, the source covariance rule gives

\[
 \|\zeta_i-\zeta_j\|_2^2
 =\|\Delta^2_i-\Delta^2_j\|_2^2\longrightarrow0.           \tag{16}
\]

This identity uses the cross contractions of their actual common-carrier
upper fields. The joint centered sources are Gaussian, so their `L²` limit
is centered Gaussian with variance at most `C²`. The corresponding `Q_i`
converge in `L²` by field continuity; hence `J_i=Q_i-zeta_i` converge in
`L²`. An almost-sure subsequence retains `|J|≤D`. A fixed real passive input
can also be obtained by a sequence of rational directions, using joint
continuity and the same covariance identity. Thus (7),(12) hold at every
time/input of (15), with the same constants. They hold separately at each
such pair, which suffices for the law-averaged tails in (13).

The strong chain rule along `C¹ L²` curves follows directly from the scalar
mean-value identity and the bounded-multiplier argument above. Apply it to
the two activations, and the action product rule, to differentiate `f(u)`.
The three gradient blocks are `phi'(w·u)Q(u)u`,
`Delta2(u) tensor H1(u)`, and `H2(u)`. Their joint continuity on the compact
input/time domain justifies differentiating the law integral. Pairing with
(3) proves

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta'_\mu(v)\|_{\rm raw}^2dv
 =\int y^2d\mu\le1.                                     \tag{17}
\]

The readout equation and `int|r|dmu≤sqrt(L)≤1` give `||c(t)||∞≤2t`.
Coordinatewise integration is justified by Fubini for the bounded readout
velocity. The remaining rank and row integrals then give

\[
 \|K(t)\|_{\rm HS}\le2t^2,\quad
 \|A(t)\|_{\rm op}\le2+2t^2,\quad
 \|w(t)\|_2\le\sqrt2+4t^2+2t^4.                         \tag{18}
\]

For law continuity, apply (13) to two constructed paths and integrate as in
(14), with the mesh terms absent. Its infimum over integer `s≥1` is a
deterministic common modulus tending to zero as `q→0` (first fix `s`, then
send `q→0`, then `s→∞`). In particular this controls the whole-circle
predictions and both forward hidden fields.

For uniqueness, any competing strong raw solution on `[0,T]` has bounded
raw and action norms by continuity on this compact interval. Repeat the
subtractions of (13) with their finite common bound, yielding
`C_*(1+s)e+C_*tau(s)`; its reference is the constructed solution, with
bounded readout and (12). There is no tail assumption on the competitor.
Zero initial error and Gronwall give
`sup e≤C_*T exp(C_*(1+s)T)tau(s)→0`. Applying the same argument on
`[b,T]` proves uniqueness from any reached state at time `b`. Its existence
is the restriction of (15); no statement about arbitrary ambient endpoints
or switched training laws is needed.

## 4. Identification with actual finite GF

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

The chain rule gives the finite counterpart of (17). On any finite maximal
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
and source hypotheses checked in section 2. They give all same-layer joint
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
enlargement of (5), with probability tending to one, and has bounded assigned
speed uniformly between its finitely many nodes.

For a fixed cutoff `s≥1`, second-moment convergence gives finite proxy tails.
The continuous map `v↦(|v|-s/2)_+` satisfies

\[
 \|v1_{|v|>s}\|_2\le2\|(|v|-s/2)_+\|_2\le2\tau_{s/2}(v).
\]

Since `s/2>D`, (12) and the finite-program limit therefore bound every
law-averaged proxy-node reverse tail by `2tau(s/2)+o_P(1)`. The proxy readout
has no tail at sufficiently large fixed `s`, since it is bounded by `C` plus
the vanishing initial-readout supremum. There are only finitely many such
nodes and training inputs for fixed `(nu,h)`. In particular this reasoning
does not claim finite tails uniform in a growing transcript.

Now let `lambda_j→mu` in `W1` and `n_j→∞`. The same finite-array subtractions
as in (13), with their common finite ball, compare actual GF for `lambda_j`
to the proxy, both on their common width-`n_j` carrier. The actual law may
be nonatomic; only the comparison law is finite. For a fixed cutoff `s` the
sum distance obeys, uniformly through `T`,

\[
 E_j\le C_*T e^{C_*(1+s)T}
 \left[(1+s)(W_1(\lambda_j,\nu)+h)
                    +2\tau(s/2)+o_{\mathbb P}(1)\right].  \tag{19}
\]

The mesh term comes from the proxy's bounded node/interpolant displacement;
the probability error includes the fixed-program velocity defects. Constants
are independent of the finite comparison law and its mesh. They need only
be finite, since the available tail is Gaussian in `s`.

For any desired error, first choose fixed `s` so that the amplified tail in
(19) is small. This is possible because its negative quadratic exponent
dominates the linear Gronwall exponent on the entire fixed interval. Next
choose finite `nu` close enough to `mu` and a small fixed mesh `h` so that
their amplified deterministic errors are small and their population Euler
path is close to (15). Only then let `j→∞`. Each random error in (19) concerns
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

## 5. Why the C-H2 outer convergence proof now applies

The C-H2 finite systems themselves are unchanged. Their rational initialized
word dictionaries, ridge `2^(-N)`, two joint mark/current-coordinate
populations and finite coefficient matrix depend only on order and the
specified Gaussian initialization. C.4.7.9 parts 2–4 prove their fixed-order
well-posedness for every bounded-label law, without restricting the law
radius. In particular their bounds are

\[
 \|c_N(t)\|_\infty\le2t,\quad
 \|M_N(t)-D_N\|_F\le2t^2,\quad
 \|B_N+K_N(t)\|_{\rm op}\le2+2t^2.                      \tag{20}
\]

Here `Q_(ell,N)` are their positive finite-rank contraction filters and
`B_N=Q_(2,N) A0 Q_(1,N)`. Their exact initialized Gaussian law construction
and fixed-order local characteristic contraction argument have no
training-law assumption beyond bounded labels. The energy identity prevents
finite-time escape, including in the bounded row-increment norm used by that
characteristic proof. Thus this is an already complete finite-system
existence result on the present explicit family.

The only domain-dependent premises in their outer comparison are existence
and identification of the target, its tails, and its invariance in the
initialized observable spaces. Sections 2–4 above prove the first two for
every bounded-label law on `[0,T]`. Here is the invariance proof without
applying a small-ball theorem outside its domain.

Let `H_ell^obs` be the `L²` spaces generated by the complete initialized
bounded-word algebra of C-H2. The sine/cosine cylinder density argument of
C-H1 part 5 is static: bounded words span these spaces, and both `A0` and
`A0*` take them into each other. Adjointness makes the pair reducing.
The initial `g`, zero `c`, and zero `K` lie in these spaces. Every finite-law
Euler step (3) preserves them: bounded coordinate operations preserve the
generated sigma-fields, actions preserve the spaces, and the increment is
a sum of ranks between them. The constructed limiting trajectory is a raw
limit of precisely those finite-law Euler paths. Closedness of `L²` and of
the HS operators supported between these spaces proves that its `w,c` stay
in them and its `K` has only that block. Thus C-H2's initialized dictionary
does approximate all dynamically needed target arguments for every law in
the proposition.

The remaining density/filter argument is also independent of the training
law. For a vector in a retained word span, diagonalization of its Gram gives
`||(I-Q_(ell,N))v||2≤sqrt(2^(-N))||a||/2`, where `a` is a fixed coefficient
vector representing that word-span vector (zero-pad at higher orders).
Density and `||I-Q||≤1` give strong convergence on `H_ell^obs`. Thus
`B_N→A0` and `B_N*→A0*` strongly there, uniformly on compact `L²` sets by
a finite net and their uniform operator norms.

In particular define the **proof error**, never supplied to the equations,

\[
 \epsilon_N=\sup_{t,u}\|(B_N-A_0)H^1(t,u)\|_2
 +\sup_{t,u}\|(B_N^*-A_0^*)\Delta^2(t,u)\|_2
 +\sup_t\|Q_{2,N}K'(t)Q_{1,N}-K'(t)\|_{\rm HS}.          \tag{21}
\]

It tends to zero. The first two argument families are compact by the proved
joint `L²` continuity on `[0,T]×S1`. The last curve is compact in HS;
finite-rank tensors are dense in HS, and the filters converge strongly on
each factor with uniform contraction norms. Approximate finitely many
points of that compact curve by finite ranks to obtain uniform convergence.

Let `e_N=||w_N-w||2+||K_N-K||HS+||c_N-c||2`. The exact subtractions in
C.4.7.9 (H2.11)–(H2.14) use (20), (18), actual adjoints, and only the
target's tail. They therefore give here, for every fixed `s≥1`,

\[
 e_N'\le C_*(1+s)(e_N+\epsilon_N)+C_*\tau(s),
 \qquad e_N(0)=0.                                      \tag{22}
\]

There is no attempt to bound `||B_N-A0||op` by `epsilon_N`. At forward and
reverse action nodes the omitted base is applied only to the **target**
argument in (21). At the middle velocity, the exact difference is a filtered
rank-field difference plus `Q2 K' Q1-K'`, so its omitted term is exactly
the third term of (21). This verifies both error production and propagation.

For fixed `s`, Gronwall gives

\[
 \sup_{t\le T}e_N(t)\le C_*T e^{C_*(1+s)T}
                [(1+s)\epsilon_N+\tau(s)].              \tag{23}
\]

First `N→∞`, then `s→∞`, proves convergence. This is equivalent to the
Osgood integration in H2 but uses the stronger short-time Gaussian tail.
The algorithm uses every integer `N`; the proof has not chosen its order
from an unknown target trajectory. Strong convergence of actions on compact
target graph-node curves and (23) prove all fixed observation claims by the
finite induction in H2 part 6. Coupling corresponding tuple values on the
same carrier gives `W2²≤sum_i ||V_(i,N)-V_i||2²`, and the two-factor
Cauchy–Schwarz bound gives convergence of quadratic contractions.

Consequently a C-H3 construction may use the explicit law interface (1)
without any uncomputed admissibility radius. This result supplies no
effective rate for (21), finite population quadrature, arithmetic tolerance,
or certified stopping rule for a numerical solver. Those are separate
remaining obligations. Nor does all-law existence imply all-law activity:
for example a zero-label law has a stationary zero-readout population flow.
For family (1), this note proves the exact dynamics and convergence domain,
not a numerical lower bound on hidden displacement at `T`.

## 6. Exact checks and provenance

The deterministic check at
`data/generated/observable_hierarchy/h3_v2_scope_exact_checks/checks.json`
contains eleven passing exact rational inequalities covering (5),(11), and
the existing `H3_stability.source_cap()` also passed. No Gaussian quadrature
or trajectory was evaluated. The new elementary exponential estimates above
are independent of the implementation's 80-term Taylor enclosure. Both Python
blocks in this note executed successfully. Three valid interface cases
(including degenerate and one-degenerate intervals) passed exact mass,
unit-direction, label, cross-arc geometry, and transport-majorant checks;
three invalid inputs were rejected. These results are recorded in the same
directory's `interface_checks.json`. Used dependency hashes were rechecked
and unchanged.

To reproduce the new scalar checks without generating any trajectory:

```python
from fractions import Fraction as F
T,C,R,B=F(1,200),F(101,10000),F(10101,10000),F(1,32)
D=B+2*R*C*C*T
x=2*T
assert 1+x+x*x/(2*(1-x/3)) < R
assert D < F(1,31)
assert 6*R*D*T+8*R*R*T*T*C*C < F(1,1000)
assert 4*R*F(1000,999) < F(41,10)
assert F(41,10)+2*R < F(31,5)
d0=2*R*T+2*C
assert d0*T*F(31,5) < F(1,1000)
assert d0*F(1000,999) < B
assert 2*T*R*C < F(1,1000)
assert 2+2*T*R*C < F(201,100)
assert F(3,2)+2*T*R*(2+2*T*R*C)*C < 2
assert 2*R*((2+2*T*R*C)*C+C+1) < 3
```

Source hashes at the check:

- `docs/NOTATION.md`: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`
- `docs/global_nonlinear.md`: `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161`
- `docs/special_data_limits.md`: `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489`
- `H3_stability_proof.md`: `a5a68240508b3601faddbc30005626c144190fe38d02d1291787ef3ebeb69735`
- `H3_stability.py`: `a59194db71e5b17fcd8a4884a0a5839a16c93007cd4e06dc65dbd1bb22bcf65d`

The status remains a candidate proof pending independent scrutiny. There is
no remaining existential-law-radius implication in this argument; the open
quantitative computation and activity questions are exactly the separate
ones stated above.
