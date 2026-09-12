# C-H3 route E: effective dictionary construction by a universal finite circuit

Status: **first-route candidate and proved local lemmas; not a complete C-H3
theorem, not internally checked, not promoted**. No training trajectory was
executed, fitted, imported, or used to choose features. No Git mutation was made.

The main positive finding is that the fixed horizon `T=1/200` changes the
effective-error problem substantially. At `Y=1`, the absolute source-row bound
which fails at time 40 closes with elementary numerical slack. It supplies
effective tails on the short interval. A universal finite circuit, whose scalar
parameters range over predetermined boxes, can then replace the noneffective
compactness step in H2. This gives a plausible, deliberately enormous algorithm
for dictionary selection. It does not give plausible numerical usefulness.

The Gaussian-initialization part has a more complete resolution: an effective
compiler can avoid singular-rank decisions entirely by using full positive
covariance square roots. The H2 prototype's conditional QR/Schur procedure is
not an arbitrary-accuracy implementation of this construction.

## 1. Scope, provenance, and claim level

Scientific inputs read completely: `H2_proposed_section_v3.md`,
`H2_prototype_v3.py`, `H2_prototype_notes_v3.md`, `docs/NOTATION.md`;
`docs/special_data_limits.md` III.F.1–10; `docs/global_nonlinear.md`
C.4.7.1–2, C.4.7.3 statement and parts 1–2, C.4.7.4–5,
C.4.7.8 parts 1–3,5–6,8. The remaining long-horizon reference-transfer parts
of C.4.7.3 were not used. A metadata/headings search of `docs/README.md` was
also made to locate the named dependencies. No other studies, H3 reports,
study history, or prior verdicts were read.

Required process inputs: `RESEARCH_WORKFLOW.md`, the rigorous-math and
conjecture-investigation skills, and the latter's research-contract,
adversarial-audit, and proof-search references. The supervisor's scoped
assignment replaced ordinary author README startup. The source `N19` short-time
observation was reached locally before a supervisor message suggesting the
same calculation; that message arrived before freezing and is disclosed here.

The canonical model is precisely H2: two hidden tanh layers, no biases,
independent finite stored Gaussian variances `(1,1/n,1/n²)`, mobilities
`(n,1,n)`, unhalved squared-loss physical GF, `u=x/sqrt(2)` on the unit circle,
two separate population spaces, initial `w=g`, `K=c=0`, and the actual two
directions of `A0`. This route fixes `Y=1`, `T=.005`; extending the same cap to
arbitrary fixed larger Y is not asserted. Bounds below safely use `||A0||<=10`
from III.F instead of relying on the sharper bound 2 used in H2.

The proposed error is uniform in time, whole-circle prediction error, and
Euclidean W2 for any requested finite same-population tuple, evaluated with one
common coupling. The finite tuple and its effective real marks are fixed before
the accuracy is requested. Arbitrary noncomputable marks, arbitrary continuous
gates without supplied moduli, and arbitrary Borel laws without an effective
integration interface cannot be inputs to an effective algorithm.

The runtime witness remains the H2 autonomous system with finite quadrature
populations and its stored finite matrices. Universal circuits are used only
to prescribe the dictionary and certify its error. They are discarded before
runtime. They are not a saved sequence of earlier states or a Gaussian-action
service available to the runtime vector field.

## 2. An explicit short-time cap and tail bound

Use the constants of C.4.7.N9–N19, now with `Y=1,T=1/200`:

    C0=exp(.01)-1 < .0101,       R0=exp(.01) < 1.011,
    B=1,
    D0=B+2 R0 C0² T < 1.000002,
    d0=2 R0 T+2 C0 < .03031,
    L1(B)=4 R0 exp(6 R0 D0 T+8 R0² T² C0²) < 4.18,
    fB=L1(B)+2 R0 < 6.202.

These inequalities follow, for example, from the positive exponential series
and a geometric bound on its tail. In particular

    Psi_T(1)=d0 exp(d0 T fB) < .031 < 1.                 (E1)

This is a discrete causal induction, not an assumed bootstrap. At a new step
the lower-source estimates use only the already constructed earlier backward
rows; N15–N16 then bound the new row by `Psi_T(1)`. The first row also obeys
that bound (indeed its readout is initially zero). Thus all rows remain below 1,
for every finite law, every nonnegative step partition of total length at most
T, every support size, and every singular source covariance. The proof does
not need closeness to the reference law on this short interval.

Consequently every passive reverse query has the exact finite-program form

    Q=zeta+J,       |J|<=D0,       E zeta²<=C0².          (E2)

No independence of zeta and J is assumed. It follows by the triangle inequality
that `||Q||6 <= D0+C0*15^(1/6)<2`. Also

    E exp(4|Q|) <= 2 exp(4D0+8C0²) < 112.

For `x>=0`, `x²<=exp(2x)`. Therefore

    E[Q² 1_{|Q|>R}] <= 112 exp(-2R),
    tau_R(Q) <= 11 exp(-R),       R>=1.                 (E3)

The argument for affine interpolation times is the same finite program with
one shorter last increment. C.4.7.4's completion now applies with these
constants on the short interval for all bounded-label laws. Tails can pass
directly by Fatou along an almost surely convergent subsequence of each L2
query: the exponential moment bound remains 112. No assertion about a
coordinatewise supremum over all times or inputs is made. All quantities in
(E2)–(E3) are uniform with the supremum outside the expectation.

This provides a self-contained local ingredient for the requested family.
It does not by itself prove that every law in the entire bounded-label class
has hidden activity; a zero-label law is an immediate counterexample to that
stronger assertion.

## 3. A very conservative effective raw modulus

The raw Euler bounds NE, with `M0=10`, give through T

    ||c||infinity<.011, ||K||HS<.000103,
    ||A||<11, ||w||2<2, speed in the sum norm<3.         (E4)

For convenient comparison enlarge to `||c||infinity<=1`, `|r|<=2`,
`||A||<=11`, and `||w||2<=2`. At one input, if e is the raw sum error,
the usual subtractions give respectively

    ||H1-H1bar||2<=e, ||Z2-Z2bar||2<=12e,
    |f-fbar|<=13e, ||Delta2-Delta2bar||2<=25e,
    ||Q-Qbar||2<=276e.

For the lower gate use

    ||(phi'(w.u)-phi'(wbar.u)) Qbar||2
       <= 2 R e+2 tau_R(Qbar).

The row, middle, and readout velocity bounds are respectively
`1390e+8Re+8tau`, `130e`, and `74e`. For an input/label perturbation of
distance q, use `||wbar.(u-v)||2<=2q`, the same five subtractions, and
the final explicit vector u in the row gradient. Their sum is at most
`2824q+16Rq+8tau`. Coupling the training laws proves the safe bound

    velocity difference <=5000(1+R)(e+q)+16 tau_R(Qbar). (E5)

Only the reference has a tail premise. These deliberately inflated constants
are included to expose, rather than hide, the dependence in an effective
construction. They are not proposed numerical constants for useful computation.

For an Euler comparison replace e+q by `e+q+3h`, where h is the maximal
proof step. Together with (E3), choosing `R=1+log(1/v)` for
`v=e+q+3h<=1` yields the safe Osgood inequality

    v' <= 20000 v log(e/v).

Its direct integration gives the modulus

    Phi(s)=exp(1-alpha)*s^alpha,      alpha=exp(-100),   (E6)

whenever the right side is below one. The initial error s also includes any
uniform additive defect divided by a fixed enlarged constant. For larger s
use the raw-ball diameter. There is an explicit inverse on the small branch:
`Phi^{-1}(a)=(a*exp(alpha-1))^(1/alpha)`.

Even before dictionary enumeration, this exponent makes the present bound
prohibitively expensive. It nevertheless distinguishes a finite algorithm
with a modulus from a bare assertion of computability.

## 4. A bounded finite circuit can approximate every reached field

Use smooth saturation `T_R(x)=R tanh(x/R)` only in the **certificate circuit's**
bottom backward update. The runtime H2 equations remain unmodified. Since
`0<=x-tanh(x)<=x³/3` for x>=0 (integrate `tanh²(x)<=x²`),

    ||Q-T_R(Q)||2 <= ||Q||6³/(3R²) <= 8/(3R²).          (E7)

Compare a saturated Euler state to the true flow by writing

    T_R(Qapprox)-Qref
      =T_R(Qapprox)-T_R(Qref)+T_R(Qref)-Qref.

The first term uses the Lipschitz constant 1. A changed bottom gate multiplies
`T_R(Qref)`, whose absolute value is at most `|Qref|`; it therefore obeys
the same tail split as (E5), independent of saturation radius. The remaining
velocity defect is at most `11/R²` on the enlarged residual ball. Thus an
explicit error certificate is of the form

    sup_t raw error <= Phi(q+3h+R^(-2)),                (E8)

after increasing the harmless constant in (E6) if needed. The enlarged
constant must be retained literally in a finished implementation; (E8)'s
unit coefficient on `R^(-2)` is a normalization convention, not a sharp claim.

The importance of saturation is syntactic. Every coordinate increment of w
is now a bounded word. The row has form `g+bounded word`, c is bounded,
and K is a finite sum of ranks whose two factors are bounded words. Expanding
each K action into its finite rank list shows that every operation belongs
to H2's initialized bounded-word grammar, apart from real scalar contractions
and real marks. No unbounded product is fed through a Gaussian action.

Here is a finite construction independent of the target law or trajectory.

1. Given a tolerance s, choose rational R and an integer J so that the bound
   in (E8), with `h=T/J` and a chosen data grid error q, is at most s.
2. Choose a finite rational unit-circle net and rational label grid of mesh q.
   Rational circle points can be generated by `(1-a²,2a)/(1+a²)` plus the
   missing endpoint; use the elementary derivative bounds of this map to
   choose a covering mesh. The data grid is fixed before a law is supplied.
3. Write the J-step saturated Euler recursion as a symbolic finite circuit.
   Expand K into ranks. Replace every scalar residual, law weight, and
   population contraction used as a later coefficient by an independent
   parameter in a predetermined bounded interval containing its actual value.
   Product envelopes and the known readout/residual bounds supply such
   intervals recursively. Include each time node and the requested observation
   circuits, and a finite passive-input net.
4. Quantize **every** parameter box, without evaluating the physical feedback
   recursion for any law. Retain the resulting finite union of rational-word
   circuits. It covers the actual coefficient vector of every admitted law,
   whether or not that vector is ever computed.

The parameter mesh is effective on the canonical common carrier. Attach to
each circuit node its supremum envelope when bounded, its L2 bound otherwise,
and an L2 Lipschitz bound with respect to the finite parameter vector. Seeds
use `||g_i||2=1`; an action multiplies the input bound by 10; gates have
Lipschitz constant 1; an affine combination uses the sum of coefficient
magnitudes and parent norms; a bounded product uses
`B_v L_w+B_w L_v`. A parameter multiplying a node contributes that node's
L2 bound. All constants terminate with the finite circuit. A mesh of size
`s/(1+sum of the requested node constants)` therefore gives error at most s.
This avoids any inverse-covariance continuity argument during parameter
quantization.

This enumeration can be huge even at fixed J: allowing the coefficient
parameters independently deliberately includes many unrealizable circuits.
Those extra circuits are acceptable initialized observables. No coordinate of
the runtime state contains the parameter box or a target trajectory.

## 5. Turning the circuit cover into an explicit H2 order

For dynamics, cover the following families on the common carrier:

    H1(t,u), Delta2(t,u), A0 H1(t,u), A0* Delta2(t,u).

For a fixed requested observation graph also cover each bounded action
operand and its initialized action output, in both orientations. A time/input
net suffices: the raw speed is bounded by 3, and the finite graph's L2
continuity constants are obtained from the same bounded-operation induction.
For a bounded-gate pushforward of a named L2 field, supply the gate's effective
continuity modulus and truncate that named field before applying it.

The circuit cover consists of finite initialized words. An unbounded covered
word V is replaced by `T_S(V)`. Its error is at most
`||V||6³/(3S²)`. For each of the finitely many circuit words a sixth-moment
upper bound is computable from the finite Gaussian compiler: each action
output is one centered Gaussian plus a bounded response sum; the named
derivative envelopes bound that sum. Thus a rational S is selected before
dictionary construction. Bounded covered words are retained directly.

Let zeta be the desired total L2 error of this cover, including all previous
certificate errors. Every retained approximant is itself one H2 raw dictionary
word. Compute its natural-number code by the explicit pairing formulas in
H2. Select N at least the largest code and large enough that

    sqrt(2^(-N))/2 <= zeta.

No Gram eigenvalue lower bound appears. For a retained word psi, the exact
ridge identity in H2 gives

    ||(I-Q_N)psi||2 <= sqrt(2^(-N))/2.

Because I-Q is a contraction, a target within zeta of psi has filter error at
most `2 zeta`. The finite cover therefore supplies an explicit uniform source
bound replacing H2.10. For example, with filter error zeta on all four
displayed fields,

    ||(B_N-A0)H1||2 <= 11 zeta,
    ||(B_N*-A0*)Delta2||2 <= 11 zeta.

For the rank source, expand the two-sided filter of
`K'=-2 integral r Delta2 tensor H1` and use `integral |r|<=1`,
`||H1||2<=1`, `||Delta2||2<=.01`. Its defect is at most `2.02 zeta`.
Thus `eps_N<=25 zeta` is a safe production bound. H2's direct comparison
then gives a computable raw error via (E6), followed by finite observation
induction. This is the proposed constructive replacement for qualitative
strong convergence on unknown compact target sets.

The natural-number prefix is an especially costly indexing choice. It retains
many irrelevant words and sets a tiny ridge. A finite explicitly listed union
with a separately chosen rational ridge would be a much more sensible new
witness, but would be a change from the literal H2 prefix construction.

## 6. Gaussian compilation with no singular-rank oracle

For a finite initialized grammar program maintain its complete named centered
source covariance in each orientation, independent between orientations and
from g. Compute a new row from the required bounded-operand moments and frozen
named-source derivatives. At every stage represent the **whole** source prefix
as `C^(1/2) G`, with one standard Gaussian coordinate per named source, including
zero-variance and duplicate coordinates. Reevaluate old expressions after
changing this representation, keeping their already defined response
coefficients fixed. Their exact marginal laws are unchanged. Never replace
named derivatives by derivatives along a low-rank support.

A quantitative square-root bound can be proved without an external spectral
perturbation theorem. For PSD d-by-d matrices A,B and t>0, diagonalization gives
`||(A+tI)^(1/2)-A^(1/2)||F<=sqrt(d t)`. If
`X=(A+tI)^(1/2)-(B+tI)^(1/2)`, then

    (A+tI)^(1/2) X + X (B+tI)^(1/2) = A-B.

The integral of `exp(-s(A+tI)^(1/2))(A-B)exp(-s(B+tI)^(1/2))`
over s>=0 solves that equation, so

    ||A^(1/2)-B^(1/2)||F
      <= 2 sqrt(d t)+||A-B||F/(2 sqrt(t)).              (E9)

Given a desired square-root error, first choose t to make the first term
small, then choose a required covariance precision for the second. Positive
definiteness or a rank decision is unnecessary. Square roots themselves can be
evaluated by rational polynomial approximation to sqrt on a compact spectral
interval, with a uniform scalar remainder; add tI and a separate sqrt(t)
budget if convenient. A rational covariance approximation with entrywise
radius delta can be shifted by `d delta I` to be certified PSD; this numerical
shift is charged to (E9), not interpreted as a changed exact Gaussian law.

For a standard d-dimensional Gaussian G, quantize the cube `[-L,L]^d` with
coordinate error at most h and send the complement to zero. The same-G
coupling has

    E|G-Ghat|² <= d h²+2d(L+d/L) phi_normal(L), L>=1.   (E10)

Indeed use a union bound over coordinate tails, independence of the remaining
coordinates, `P(|G1|>L)<=2 phi_normal(L)/L`, and
`E[G1² 1_{|G1|>L}]<=2(L+1/L)phi_normal(L)`.
The rectangular cell probabilities are products of one-dimensional Gaussian
integrals. Taylor integration on bounded intervals plus the same tail bounds
gives rational enclosing weights to any requested precision. If their total
variation error is a, moving unmatched mass inside the cube costs at most
`4 d L² a` in squared transport distance. Normalize rational weights with an
explicit additional error budget.

On each fixed grammar circuit, all first and second named derivatives have
finite computable bounds: multiply bounded parent ranges, use bounded first
and second elementary derivatives, and retain all finite response terms.
Covariance integrands and derivative expectations therefore have effective
Lipschitz/growth bounds. Apply (E9)–(E10) and these bounds recursively to
choose tolerances at every source call. Near rank loss can force small
tolerances, but never creates an undecidable zero test. The finite recursion
terminates for every requested positive accuracy. Compile the full union
before extracting either population's joint marks or D.

For the ridge inverse square root, eta is fixed positive. One may use

    (G+eta I)^(-1/2)
       =(2/pi) integral_0^infinity (G+(eta+s²)I)^(-1) ds.

Diagonalization verifies the identity; the resolvent identity bounds changes
of G by an integrable multiple of `||delta G||/(eta+s²)²`. The integral is
`pi/(4 eta^(3/2))`. Thus the inverse-square-root sensitivity is at most
`||delta G||/(2 eta^(3/2))` on matrices whose eigenvalues are at least eta.
Truncate the integral with a rational tail bound and use bounded-interval
quadrature. This makes the conditioning cost explicit. The original prototype
uses float64 and rejects ridge underflow; it cannot implement this arbitrary-N
algorithm as written.

## 7. Population, law, time, rounding, and joint-law error budgets

For fixed N all frozen basis features have a computable bound L_N. Quantize
the **joint** Gaussian mark laws using section 6, producing rational positive
weights and rational marks. Compute D in the same compiled upper population.
Use extra precision until the quadrature feature operators have norms at most
2 and the D approximation is within one of its exact value; these are strict,
decidable certificates because the exact feature operators have norms at most
1. No resampling of reverse action is allowed.

The exact rational-mark finite-population ODE is still a negative gradient
flow in the weighted row/readout metric and Euclidean M metric. Hence its
loss is nonincreasing, its readout is bounded by `2t`, and its M increment is
bounded explicitly using the two feature-operator bounds. On this invariant
region the finite-population vector field is globally Lipschitz in the moving
coordinates with an explicit finite constant obtained from its displayed
sums/products and `|b|<=L_N`. Tanh has bounded derivatives; g is frozen.

Couple exact and quantized marks once and evolve both on this coupling. An
L2 comparison of w,c and a Frobenius comparison of M adds the static joint-mark
error, D error, and law-quadrature error as forcing. Every population pairing
is bounded by the two-factor Cauchy–Schwarz inequality. Thus, for explicitly
computed constants C_N,L_N' on the bounded region, the error is bounded by

    exp(L_N' T) [delta_initial
       + T C_N(delta_marks+delta_D+delta_law+delta_rhs)]. (E11)

There is no hidden approximation of independent marginals here. For a tuple
of k fields, evaluating all k on this same coupled population gives
`W2²<=sum_j ||V_j-Vhat_j||2²`. This also treats frozen/current pairs.
Quadratic contractions use their two L2 errors and bounded second moments.

An effective data interface supplies rational atomic approximants with a
certified W1 error. For the concrete arc families below, equal arc partitions
and their exact or rationally enclosed weights give this error directly.
For a fixed rational-mark population, its continuous input integrands have
explicit Lipschitz bounds from the finite arrays, so law quadrature is a
genuine numerical operation, not an arbitrary-action or integration oracle.

If a numerical trajectory is later authorized, a fixed-step Euler method for
this finite ODE has global defect bounded by
`T exp(L_N'T)(L_N' V_N h_num/2+delta_rhs)`, plus the interpolation error
`V_N h_num`. Enclose tanh and each arithmetic operation by rational intervals
to meet delta_rhs. Other validated solvers can improve this. Such a solver
saves the current finite populations, M,D, and fixed law data only; an elapsed
time list or growing Gaussian transcript is not a state coordinate. No solver
or trajectory was implemented or executed for this report.

The order of budgets is essential: select the closure tolerance, build the
dictionary and ridge, then bound fixed-N conditioning and finite-population
Lipschitz constants, and only then choose Gaussian, population, law, numerical
time, and rounding precision. A fixed quadrature rule as N grows is not covered.

## 8. Fixed effective nontrivial family: remaining proof obligation

An obvious effective candidate family consists of equal masses on the two
labeled arcs

    u=(cos a,sin a),       a in [-r,r],             y=+1,
    u=(cos a,sin a),       a in [pi/2+b-r,pi/2+b+r], y=-1,

with rational/effectively specified `(b,r)` in a fixed small compact rectangle,
including `r=0` as an atom. It includes nonorthogonal atomic and nonatomic laws
and has deterministic W1 quadratures. Its rectangle must be fixed independently
of epsilon. Choosing an arbitrary decimal rectangle and calling it active is
not justified by the present report.

H2's inherited activity radius and time are qualitative. A plausible effective
selection uses **initial** finite Gaussian expressions H15–H18 only. At the
reference, their strict positivity can be semidecided by certified Gaussian
integration and saturation of the one unbounded action operand. Choose a
dyadic parameter rectangle on which the positive initial acceleration and
nonaffinity margins remain separated from zero, using the finite-program
parameter moduli above. This search terminates by the proved strict initial
positivity and its continuity.

The remaining step is an explicitly persisted uniform remainder modulus for
the normalized hidden increments, not just existence of an o(t²) term. The
available bounds indicate how to obtain one: c/t approaches its initial
derivative at a linear rate; Delta2/t and Q/t inherit an explicit rate; the
lower gate uses (E3) to truncate its fixed initial backward coefficient; the
upper hidden coefficient is approximated through a bounded saturation and
`||A0||<=10`. Each is a finite error budget. However the complete uniform
remainder derivation and the resulting numerical/dyadic rectangle and time
have **not** been written or checked here. This is a real missing implication
for a full C-H3 claim over a fixed certified active family. The ordinary
all-bounded-label short-time approximation claim is not a substitute for it.

If the requested family is already supplied with an effective positive
activity certificate, the construction above does not need this step. The
qualitative H2 ball alone is not such an effective certificate.

## 9. Hostile audit and disposition

| Attack | Finding |
|---|---|
| Arbitrary-accuracy order chosen from an unknown target residual | The universal parameter-box circuit removes that dependence in principle; section 5 gives an explicit ridge-order rule. The full tolerance assembly remains a candidate, not implemented code. |
| Hidden trajectory or fitting | No law's feedback recursion is evaluated to select features. All predetermined parameter-grid circuits are included. If the contract forbids even this finite symbolic unrolling as a proof certificate, this route is unavailable; it is not being hidden in the runtime state. |
| Infinite precision stores inaccessible information | Inputs require effective marks/law quadratures. All compiled constants receive finite rational error budgets. |
| Source-rank discontinuity | Full covariance square roots and (E9) remove rank tests. Individual named derivative slots must survive. |
| Gaussian quadrature cannot certify arbitrary programs | (E10), finite derivative envelopes, and the causal covariance recursion give a terminating error algorithm, but its dimensions/cost are enormous. |
| Runtime arbitrary Gaussian action | Runtime uses only finite M and feature contractions. Gaussian compilation is initialization only. |
| Independent marginal coupling | Prohibited. Every tuple uses the same finite joint law and common mark coupling. |
| Input law excludes nonatomic/nonorthogonal data | The arc family supplies both and explicit W1 quadrature. A fixed active rectangle still needs its remainder certificate. |
| Finite population and time errors confused with closure | They are selected after N through (E11), independently of the proof mesh used in section 4. |
| Practical usefulness | Unsupported and strongly disfavored for this literal brute-force witness: alpha=exp(-100), parameter-box tensor enumeration, natural-number prefix inflation, eta=2^(-N), and Gaussian tensor quantization compound. This is not evidence that every effective witness is useless. |

Recommended route status: **promising for a nonuseful effective-existence
theorem; incomplete for C-H3 as a useful certified numerical system**. The
best independent reusable components are the short-time cap (E1)–(E3),
the full-covariance Gaussian compiler estimate (E9)–(E10), and the explicit
finite-cover/ridge source estimate in section 5. A finished proof must close
the uniform active-family remainder, instantiate all observation error
budgets, and check the entire compiled approximation pipeline. Replacing those
tasks by the word “computable” would be an invalid upgrade.

## 10. Source hashes and checks

HEAD at the pre-edit metadata check:
`117991a49487209a8859c9294369482b35825e58`. The shared index was empty;
concurrent modified/untracked files were preserved. Only this assigned report
was created by this route. No external source or theorem was imported.

| Input | SHA-256 |
|---|---|
| H2_proposed_section_v3.md | c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2 |
| H2_prototype_v3.py | f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137 |
| H2_prototype_notes_v3.md | bc3aac299026b8665cf6d69765d482692a40ff0cfb6f5d443837fc7d049a3f8e |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md | 947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |

Checks were mathematical substitutions, causal/singular-covariance attacks,
source reads, and metadata/hash verification. A static Python Decimal check at
50-digit precision, evaluating the displayed N9–N19 formulas without training,
returned `Psi_T(1)=0.030229053583260757880128705404389883350566390018742`
and the exponential-moment upper expression
`109.28501742708135790381287017307129725961469245599`; all seven displayed
coarse numerical inequalities passed assertions. This arithmetic sanity check
does not replace the positive-series enclosure argument or certify the full
route. No trajectory reproduction or independent mathematical review was
performed, so this artifact carries no internal PASS.
