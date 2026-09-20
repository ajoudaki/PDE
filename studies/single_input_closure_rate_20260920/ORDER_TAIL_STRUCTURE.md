# Factorial fading of action-generation tails

Research derivation, 2026-09-20; internally derived, not independently checked
or promoted. Scientific inputs are this study's README, ROUTE_DYNAMICS.md and
CORE_OBSTRUCTION.md, and the assigned maintained hierarchy and notation.
No experiment, other study, or future-trajectory coefficient is used.

There is a structural factorial upper bound in **action-generation depth**
for the exact source omitted by an auxiliary observable-space projection.
It applies to the canonical single-input flow, including all physical times
and the whole passive circle. It is not yet a factorial bound in maintained
H3 order `p`: each auxiliary generation retains an entire sigma-field and
therefore infinitely many scalar degrees of freedom. Its value is to separate
the dynamical cost of additional action generations from the finite dictionary's
cost of resolving functions inside those generations.

## 1. The auxiliary depth and the precise statement

Retain all conventions of ROUTE_DYNAMICS.md: `A0` and its actual adjoint,
`||A0||<=2`, first-row roots `(g1,g2)`, sole normalized training input `e1`
with label `+1`, zero population initial readout, and original gradient flow.
Set `h_i=tanh(g_i)`, `Y_i=A0 h_i`, `H_i=tanh(Y_i)` and `p_i=A0*H_i`.
The fixed H3 cores generate

    G1^0 = sigma(g1,g2,p1,p2),       G2^0 = sigma(Y1,Y2).

Complete all sigma-fields under their population probability measures. Define
one action generation by a forward and then a reverse expansion:

    G2^(r+1) = sigma(G2^r, {A0 v : v in L-infinity(G1^r)}),
    G1^(r+1) = sigma(G1^r, {A0* z : z in L-infinity(G2^(r+1))}).    (1)

The new action answers are L2 random variables. In particular these are
well-defined sigma-fields, even though their generators need not be bounded.
Only bounded operands are queried, as in the maintained grammar. There is no
claim that a generation has finitely many roots or features.

Let `P_l^r` be conditional expectation onto `L2(G_l^r)` and put

    A_r = P2^r A0 P1^r.                                      (2)

For the **exact** feature-time solution `(X,K,c)`, put
`w=(j(X,g1),g2)`, `H(s,u)=tanh(w(s) dot u)`, and
`delta(s)=c(s) sech²((A0+K(s))H(s,e1))`. Define its three omitted sources by

    rho_r(S) = sup_(s<=S,u in S1) ||(A_r-A0)H(s,u)||_2
             + sup_(s<=S) ||(A_r*-A0*)delta(s)||_2
             + sup_(s<=S) ||P2^r K_s(s) P1^r-K_s(s)||_HS.       (3)

For every `S>0` and integer `r>=1`, set

    B = 2+S²/2,
    L = 2B+1+2S(B²+B+1),
    M = 1+3S/2+S³/8.

Then the following source bound has no unproved projection-tail hypothesis:

    rho_r(S) <= (9+10SB+S) M L^(r-1) S^r/r!.                  (4)

Let `f^[r]` be the autonomous projected flow with initial action `A_r` and
the two-sided projected middle update, using the same original gradient
metric. There is an explicit constant `C`, independent of `r`, such that

    sup_(t>=0,u in S1) |f^[r](t,u)-f(t,u)|
                   <= C (5L_5)^(r-1)/r!,                    (5)

where `L_5=4575/2`. Equation (5) is an upper bound, not an assertion of sharp
factorial asymptotics or a matching lower bound. All physical times are
compared at identical physical time in the two flows.

## 2. Global Picard iterates and their preserved bounds

Use only the transformed integral equations, not a Taylor expansion. Start
with `X_0=K_0=c_0=0`. Given iterate `k`, write

    w_k=(j(X_k,g1),g2),     H_k(u)=tanh(w_k dot u),
    Z_k=(A0+K_k)H_k(e1),   delta_k=c_k sech²(Z_k),

and define, on the entire interval `[0,S]`,

    X_(k+1)(s) = integral_0^s (A0+K_k(v))*delta_k(v) dv,
    K_(k+1)(s) = integral_0^s delta_k(v) tensor H_k(v,e1) dv,
    c_(k+1)(s) = integral_0^s tanh(Z_k(v)) dv.                (6)

These iterates use the initialized action, never the unknown target path.
They remain in the same bounded domain as the exact solution. In fact,
induction using `|tanh|<=1`, `0<=sech²<=1`, and the rank-one norm gives

    ||c_k(s)||_infinity <= s,
    ||K_k(s)||_HS <= s²/2,
    ||X_k(s)||_2 <= s²+s⁴/8.                               (7)

For the last bound integrate `(2+v²/2)v`; for the middle bound integrate
`v`. The bound on `c_(k+1)` follows directly from (6), independent of `k`.
The integral equations produce continuous L2/HS curves. Bounded-multiplier
continuity justifies the nonlinear compositions, and `j` is 1-Lipschitz in
its displacement argument, as proved in ROUTE_DYNAMICS.md.

For two states in this domain use the sum distance

    D = ||X-Xtilde||_2+||K-Ktilde||_HS+||c-ctilde||_2.

Their lower features differ by at most `||X-Xtilde||_2`, uniformly over the
passive circle. At the training input,

    ||Z-Ztilde||_2 <= B||X-Xtilde||_2+||K-Ktilde||_HS,
    ||delta-deltatilde||_2
        <= ||c-ctilde||_2+2S||Z-Ztilde||_2.                 (8)

Here the second inequality uses the supremum bound on the reference readout
and the global Lipschitz constant two for `sech²`. Subtract the three vector
fields in (6), using actual adjunction and the two-factor rank-one identity.
The coefficients of the three component distances in their summed norm are
at most

    2SB²+2SB+S+B,       2SB+3S+1,       B+1,

respectively. Each is at most the displayed `L`, since `B>=2`. Thus the
vector field is `L`-Lipschitz on the domain traversed by all these curves.
This verification is needed: unconstrained global Lipschitz continuity on
the entire L2 product space is neither used nor asserted.

Let `E_k(s)` be the sum distance from iterate `k` to the exact solution.
Equation (7), also valid for the exact solution, gives `E_0(s)<=Ms`.
Subtracting its integral equation from (6) gives

    E_(k+1)(s) <= L integral_0^s E_k(v) dv.

Induction therefore proves, without a smallness restriction on `LS`,

    E_k(s) <= M L^k s^(k+1)/(k+1)!.                        (9)

These are globally defined Picard iterates on the fixed bounded feature
interval. The factorial controls the large-horizon iteration error; no
analyticity in time or convergent Taylor series is required.

## 3. Picard depth really bounds action-generation depth

For every `k` and `s`,

    X_k(s) in L2(G1^k),       c_k(s) in L2(G2^k),
    K_k(s) = P2^k K_k(s) P1^k.                             (10)

The assertion is true at `k=0`. Suppose it holds at `k`. For each passive
input `u`, `H_k(s,u)` is bounded and `G1^k`-measurable. Thus `A0H_k(s,u)`
is `G2^(k+1)`-measurable by (1), and `K_kH_k(s,u)` already lies in
`L2(G2^k)`. Consequently `tanh Z_k` and `delta_k` belong to
`L-infinity(G2^(k+1))`; specifically `|delta_k(s)|<=s`.
The reverse query `A0*delta_k` is then `G1^(k+1)`-measurable.
The remaining part `K_k*delta_k` lies in `L2(G1^k)`.

The rank in (6) connects `L2(G1^k)` to `L2(G2^(k+1))`. Each of the
three closed subspaces just described is preserved under its Bochner
integral, establishing (10) for `k+1`. This also shows why one generation
in (1) includes a forward and a reverse action.

Fix `r>=1` and put `k=r-1`. From (10) and (1),

    (A_r-A0)H_k(s,u)=0,
    (A_r*-A0*)delta_k(s)=0,
    P2^r(delta_k tensor H_k)P1^r=delta_k tensor H_k.        (11)

These are exact cancellations. Since `||A_r-A0||<=4`, (8)--(9) give

    ||(A_r-A0)H(s,u)||_2 <= 4E_k(s),
    ||(A_r*-A0*)delta(s)||_2 <= 4(1+2SB)E_k(s).           (12)

On Hilbert--Schmidt operators, `T -> P2^r T P1^r` is an orthogonal
projection: adjointness follows from the HS pairing and idempotence from
that of the two population projections. Its complementary operator has
norm at most one. Since `K_s=delta tensor H(e1)`, the last cancellation
in (11) and the rank-one difference identity yield

    ||P2^r K_s P1^r-K_s||_HS
       <= ||delta tensor H-delta_k tensor H_k||_HS
       <= (1+2SB+S)E_k(s).                                (13)

Summing (12)--(13), taking the indicated suprema, and using (9) proves
(4). In particular this is a proof of a projection-source rate, not merely
a state convergence statement followed by an assumed source estimate.

## 4. Uniform physical-time consequence and its limit of scope

For the auxiliary projected flow use initial action `A_r`, the same row and
readout equations, and middle equation

    (K^[r])_s = P2^r(delta^[r] tensor H^[r])P1^r.           (14)

All its states remain in the population subspaces in (10) with index `r`.
Thus (14) is its gradient equation in the ordinary HS norm on that closed
subspace. The row and readout gradients are already in their respective
subspaces. It is a well-defined autonomous, restartable infinite-dimensional
projection, retaining the actual transpose through `A_r*`.

At the training input, even generation zero satisfies

    A_r tanh(g1)=A0 tanh(g1)=Y1.

Indeed both its input and its output belong to the initial cores. Hence its
initial upper-feature norm is exactly the canonical
`m_*=E tanh²(Y1)>1/5`, independently of `r`. The gradient norm-convexity
argument in ROUTE_DYNAMICS.md applies in the projected raw metric: both
training predictions increase at feature speed at least `m_*`, and both
fitting endpoints lie strictly below feature time five. There is no
small-source prerequisite for this fitting assertion.

Use `S=5` in the stability and scalar-clock comparison in that route.
That proof uses only the two-sided contraction properties, the three
sources (3), and the indicated gradient fitting estimate, all verified here.
For an entirely specified constant put

    E = [2S(B+1)+3](exp(LS)-1)/L,
    P = (1+SB)E+S,
    V² = 1+S²(B²+1),
    C = (1+5V²) P (9+10SB+S) M S,             S=5.        (15)

Its feature-time error is at most `P rho_r(5)`. The two physical clocks
differ by at most that number divided by `m_*`; the exact passive
prediction has feature derivative at most `V²`. Equations (4) and (15)
give (5), including the endpoint by passage to the physical-time limit.
All constants are deliberately conservative.

For fixed `S`, the factorial inequality `r! >= (r/e)^r` follows by bounding
`sum_(j=1)^r log j` below by `integral_1^r log x dx`.
Thus the proved source bound, and the all-time prediction bound, have

    log(error upper bound) <= -r log r+O(r),               (16)

where the constants depend on the fixed feature horizon. In this auxiliary
generation depth, an accuracy `epsilon` is sufficient at depth
`O(log(1/epsilon)/log log(1/epsilon))` as `epsilon -> 0`.

The maintained H3 order `p` has two different approximation burdens: it must
reach these action generations through its literal-code prefix and also
resolve their functions with finitely many retained features and positive
ridge. The spaces in (1) discharge neither finite-resolution burden.
Consequently substituting `p` for `r` in (4)--(16) is invalid. A quantitative
finite-word compilation bound is still needed to convert this structural
fact into a rate for the unchanged maintained closure. No unidentified tail
is left in the depth theorem; the remaining distinction is between its
infinite-resolution approximation family and the prescribed finite family.

There is no lower bound here, no claim of monotone prediction accuracy as
either index increases, and no conclusion that factorial fading alone makes
small practical H3 orders accurate. The result establishes that indefinite
feature evolution is not a necessary obstruction: bounded feature time and
the exact transformed dynamics force high action-generation sources to fade.
