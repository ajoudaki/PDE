# Scoped internal check of the finite-horizon closure theorem

Date: 2026-09-25. Status: **PASS for the original-clock finite-horizon
theorem and its explicit constants.** No correction blocking that theorem
was found. The adaptive-clock and book-specific source attributions have
the coverage limitations stated below.

This is a collaborative internal mathematical check, not an isolated
promotion review. The checker first derived the original-clock bounds
from the supervisor's prompt and the two permitted closure notes, then
read every line of the complete frozen candidate. The checker received
the proposed proof architecture before that derivation. This report does
not claim blindness to the author's intended result or independence from
the collaborative discussion.

## Frozen inputs and actual coverage

The following are the complete scientific files read within the assigned
scope. Line counts refer to the files checked, including blank lines.

| File | Coverage | SHA256 |
| --- | --- | --- |
| `ORACLE_FINITE_HORIZON_BOUND.md` | All 363 lines, sections 1--8 | `bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1` |
| `MOMENT_CONSTRUCTION.md` | All 207 lines | `5d8bf7fb354fbdef138676ca0ee5d59799a9032e6f6f531ca4650c8e0e5a9025` |
| `RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md` | All 268 lines | `677b4d4f7abd5239e1894411c127cf87230ddbde27ec447c2ae56836b7629f23` |

The supervisor's mathematical assignment and clarifications were also
inputs. The required `solve-math-rigorously` skill was read and applied.
No other study artifacts, study histories, established chapters, source
reports, or maintained code were read. In particular, the checker did not
read `RESPONSE_CLOCK_FULL_CLOSURE.md`, `docs/arctan_limits.md`, or
`docs/global_nonlinear.md`. Their content was not obtained indirectly
through another agent. The claims concerning those sources below are
therefore checked only as conditional statements using the assumptions
displayed in the candidate; their source attribution is not certified.

No experiments, numerical solvers, symbolic packages, or maintained-code
checks were run. The only new artifact written by the checker is this
report. The candidate was not edited.

## Claim level and quantifiers

The main statement is valid for finite positive n,d,M, finite real data
and initialization, the specified tanh network, consistent raw moments,
and every integer P>=1. Time is forward physical time, so the finite
horizon is 0<=T<infinity. The same initial physical arrays are used in
the dense and closure systems.

For each such T, the displayed C_T and K_T are finite and independent of
P. Both systems exist uniquely for all finite physical times, and the
physical block-sum error satisfies (1). The rate is O_T(1/P) because
sqrt(P(P+1)) is comparable to P. The statement is about exact
continuous-time equations at fixed width and data. No successful fitting,
source variation bound, task geometry condition, or closure descent
property has been smuggled into the proof.

The distinction between global existence and convergence uniformly over
all physical time is maintained correctly. The former is proved; the
latter is not claimed. Nor does the proof give width-uniform constants.

## Canonical equations and exact moment identities: (2)--(5)

With unhalved mean squared loss and readout W3^T b/n, applying mobilities
(n,1,n) to the three parameter blocks gives exactly (2), including its
middle-layer factor 1/n. The definitions of delta and gamma have the
correct orientation and normalization.

The raw equations (3) match the permitted original construction. On an
existing solution segment the moment integrals in (4) differentiate to
(3) by the displayed dilation identity. Their initial values match the
constant forward prefix and zero backward prefix. Linear uniqueness
along the fixed history then establishes (4); no trajectory from the
dense system is involved.

Legendre orthogonality gives the reconstruction (5), with normalization
(2k+1)/tau for each coefficient product. The fixed prefix contributes
zero to the unprojected forward/backward product. Neither (4) nor (5)
requires differentiating the backward history.

## A priori bounds and continuation: (6)--(12)

The readout identity (7) is exact:

    d||W3||^2/dt = -4n mean (f-y)f
                 = nY^2 - 4n mean(f-y/2)^2.

It applies to both systems because the readout equation is unchanged,
regardless of whether the closure loss is decreasing. Since ||b_a||<=sqrt(n),
the estimate |f_a|<=B_T/sqrt(n), followed by the triangle inequality in
sample RMS, gives rho<=q_T. Thus tau<=ell_T and tau-1<=S_T on every
local interval contained in [0,T].

For positive rho, mean(r_a/rho)^2=1 and ||delta_a||<=B_T, so
mean||u_a||^2<=B_T^2. Integrating in activity yields the two history
energy bounds (8); the source energy only uses length tau-1 because
its prefix is zero. Projection contractivity and Cauchy--Schwarz over
both samples and history give exactly

    ||W2hat-W0||_F <= 2 B_T sqrt(tau(tau-1))/sqrt(n).

The looser D_T in (6) is valid. For the dense flow the direct bound
||F2||_F<=2rho B_T/sqrt(n) gives its stated middle-matrix estimate,
which is also bounded by D_T.

The derivative estimates (10)--(11) follow from

    ||gamma_a|| <= ||W2||_op ||delta_a|| <= D_T B_T,
    mean |r_a| ||z_a|| <= rho X,
    ||diag(1-h_a^2)||_op <= 1.

Consequently H_T=2D_TB_TX^2 is the correct Euclidean-vector Lipschitz
constant in activity. This argument needs no estimate of W2hat_dot and
no derivative of the residual direction. Integrating the inequality
||h_a_dot||<=rho H_T also proves constancy on any zero-activity segment,
so defining a history on the activity coordinate is justified. The
constant prefix creates no jump in the forward history.

For fixed P, the raw system is locally Lipschitz in its finite state on
tau>0. Taking the residual RMS algebraically introduces a Lipschitz norm,
not a singular division. Consistent forward responses are smooth functions
of the weights and moments there. Bessel's inequality yields (12) with
the stated factors M, n, ell_T, and S_T. In fact these inequalities bound
even the unweighted Euclidean norm of the full retained moment stack
independently of P, since every weight 2k+1 is at least one.

For any putative finite maximal existence time, choose a finite T at
least that time and apply these bounds on the existing segment. All
coordinates stay in a compact subset of tau>0 with tau>=1. The vector
field is bounded on that compact set, which gives a limit at the
endpoint; local existence there continues the solution. This rules out
finite-time blowup without assuming the result in advance. The dense
system continues by its physical parameter bounds. The local Lipschitz
property gives uniqueness for both systems.

At a state with zero residual vector all raw right-hand sides vanish,
including clock and moment transport. It is a full equilibrium.
Uniqueness for the locally Lipschitz ODE, also applied to the reversed
local time direction, prevents a nonstationary solution from first
reaching such an equilibrium at finite time. Hence an initially positive
rho remains positive at every finite time. No positive lower bound
uniform in P is needed.

The rational response lift is covered only with consistent initialization
and identification with this raw solution. If initially rho=0, its
displayed rational rho equation is undefined; the separate stationary
extension described in the candidate is the appropriate interpretation.
The proof is not a claim that that rational expression is nonsingular at
zero, or that inconsistent lifted states have the same bounds.

## Forward-only projection and accumulator error: (13)--(17)

The weighted Legendre inequality (13) has the correct eigenvalue
P(P+1) and interval factor tau^2/4. One direct verification is to use
the eigenvalue equation and weighted derivative orthogonality on [0,1]:

    integral x(1-x) p_k' p_j'
      = [k(k+1)/(2k+1)] delta_kj.

Integration by parts identifies the derivative pairing with the ordinary
Legendre coefficient. Weighted Bessel's inequality therefore controls
the coefficient energy multiplied by k(k+1). Polynomial completeness
gives Parseval for the L2 tail. Rescaling to [0,tau] gives (13).
All these steps apply componentwise to the Lipschitz forward histories,
which belong to H1. There is no derivative atom at the prefix join.

The derivative is zero on the prefix, so its L2 norm is at most
H_T sqrt(tau-1). This gives (14). Orthogonality proves (16) for a
vector outer product component by component: each retained component
of the forward projection is a polynomial to which the discarded source
is orthogonal.

Thus, writing s=tau-1 and lambda=P(P+1), the constants combine as

    ||R_P||_F
      <= (2/n) [B_T sqrt(s)]
                  [H_T tau sqrt(s)/(2sqrt(lambda))]
       = B_T H_T tau s/(n sqrt(lambda)).

This verifies (17), its sign convention relative to (15), and
C_T=B_T H_T ell_T S_T/n. P=1 is included. T=0 and stationary zero-loss
data introduce no exception. The zero backward prefix is important in
the sharper factor S_T but its jump creates no problem for this argument.

R_P is the signed matrix-valued accumulated defect. Its small supremum
does not imply a small instantaneous E, nor a small integral of ||E||.
The candidate explicitly preserves this distinction. A bound on the
total variation of u is not needed for the accumulated estimate.

## Explicit stability constant and comparison: (18)--(22)

Every term in K_T was checked in the stated block-sum norm. For two
states in the region ||W2||_F<=D, ||W3||<=B, write their distance as e.
Successive product splittings give:

    ||Delta h|| <= X e,
    ||Delta b|| <= (D X + sqrt(n)) e = a2 e,
    |Delta f| <= (B a2 + sqrt(n)) e/n = af e,
    ||Delta delta|| <= (1 + 2 B a2) e = ad e,
    ||Delta gamma|| <= (2 D B X + B + D ad) e = ag e.

For delta, the gate difference is bounded by 2||Delta b|| and the
readout vector contributes at most B. For gamma, the first gate,
middle matrix, and delta differences contribute respectively
2DBX, B, and D ad. Frobenius norm dominates operator norm throughout.

For each of the two states mean|r_a|<=q, while
max_a|Delta r_a|<=af e. Splitting the products in the canonical fields
therefore gives exactly the following three constants:

    F1: 2X(DB af + q ag),
    F2: (2/n)(B sqrt(n) af + q sqrt(n) ad + q B X),
    F3: 2(sqrt(n) af + q a2).

Their sum is (18). The estimate is valid for arbitrary W1 and does
not depend on P or a bound on its retained moments. There is no missing
sample factor, width factor, or residual-derivative term.

The physical integral identity (20) follows directly from the exact
outer equations and the accumulator definition. Since both trajectories
lie in the region just checked, subtraction gives (21). Integral
Gronwall (or iteration of the nonnegative integral inequality) gives
(1) and (22) with exp(K_T T). A small derivative defect is not required
for this integral argument. Prediction and passive-input response
consequences follow by the same response difference estimates, using
the appropriate passive input norm bound. The order rule is a valid
sufficient mathematical condition, without an efficiency guarantee.

## Adaptive clock and all-time claims: coverage and limitations

Section 6 is correctly segregated from the unconditional original-clock
theorem. Under its displayed assumptions of regular adaptive solutions,
the accumulated bound (23), a suitable physical bound (24), and a
P-uniform finite response length, substitution into the same integral
stability argument gives (25). The use of max(1,P-1) includes small P.
Finite positive Gram matrices alone do not imply a uniform inverse
bound or uniform regularity; the candidate correctly leaves those
obligations open.

The stated contraction reasoning for (24) is compatible with an
orthogonal projection in a measure of total mass A_P, a source bounded
in sample RMS by B_T, forward norm at most sqrt(n), and the stated
fixed prefix subtraction. However, the actual weighted-clock equations
and the original proof of (23) were outside the checker's input scope.
This report does not certify that those hypotheses and representations
hold for the cited adaptive source file. This coverage limit does not
affect (1), whose proof is self-contained in sections 1--5.

The scalar example in section 7 is correct. The unforced equation
z'=z-z^3 is negative gradient flow of (z^2-1)^2/4. From z(0)=0 a
nonnegative continuous forcing of positive total mass makes z(1)>0;
after forcing stops its trajectory tends to 1. Its forcing primitive
has supremum epsilon. Thus small accumulated forcing need not yield
small all-time trajectory error even for a smooth squared-loss gradient
flow with bounded trajectories. The candidate appropriately does not
present this as a counterexample to the neural closure itself.

The bounded-primitive linear corollary is valid under the displayed
operator assumptions. If M_V=sup_t||V(t)||,
J_V=integral_0^infinity||V'(t)||dt, and
B_1=integral_0^infinity||B(t)||dt are finite, its equations imply

    sup_t||z(t)|| <= (1+J_V) sup_t||R(t)||,
    sup_t||v(t)|| <= (1+J_V) exp(M_V B_1) sup_t||R(t)||.

This follows by variation of constants for the constant generator,
then integration by parts against R, then integral Gronwall. It does
not require differentiability of a continuous R once the integral
formulation is used. Boundedness of a homogeneous propagator alone
does not supply the integrable derivative condition. Applying this
linear corollary to the nonlinear neural closure would require the
additional matching, nonlinear, neutral-direction, and uniform-source
controls listed by the candidate.

The assertions that the cited book proof actually supplies those
operator hypotheses, the exact source equation labels, and the
descriptions of book population limits are not independently verified
here. They require the separate source check identified by the author.
They are not premises of the finite-dimensional theorem checked above.

## Corrections, unresolved issues, and conclusion

No mathematical correction to (1)--(22) is required by this audit. The
usual forward-time convention 0<=T<infinity is understood. No candidate
edits were requested or performed.

Unresolved claims remain exactly outside the proven scope: all-time
uniform nonlinear tracking; width-uniform limits or efficiency; a
finite-step solver certificate; instantaneous or absolute integrated
defect convergence from these estimates alone; unconditional regularity
and uniform length for the adaptive clock; and direct verification of
the external source attributions excluded from this checker's scope.

Within its stated finite-dimensional, finite-horizon scope, the original
activity-clock theorem is complete, its bounds are noncircular, and its
explicit constants and zero-residual handling are correct.
