# Exponential-potential search: current conclusions

2026-09-16. Continuation of the same flat study. All results below concern
the exact autonomous population closure, not a new approximation to its
trained network or a closure-order limit. Nothing has been promoted.

## Current answer and the scope boundary

For three generic unit-label inputs on the original two-dimensional
circle, unconditional convergence and an exponentially decreasing
current-state potential remain **open**. No nonconvergent initialized
generic example has been found. Failed estimates and ambient stationary
states must not be described as such an example.

There is now a complete restricted three-input theorem in **three input
dimensions**, using the established canonical general-d p=1 coefficient
construction. It has three nonredundant initialized hidden constraints,
correlated inputs, a mixed potential bounding the loss, and exponential
fitting with full-state convergence. It exploits an exact permutation
symmetry. It is separate from the original circle question; the user has
not explicitly accepted changing the dimension. The latest steering
keeps three inputs primary and permits alternatives only for a concrete
reason. The reason for this bounded alternative is the dictionary's
exact coordinate-permutation symmetry, not a claim that three circle
inputs cannot learn.

The complete candidate is [three_coordinate_candidate.md](three_coordinate_candidate.md).
Its author-side reconstruction is [three_coordinate_root_check.md](three_coordinate_root_check.md);
the fresh isolated complete check is [three_coordinate_audit.md](three_coordinate_audit.md).
Both checks passed for the stated d=3 theorem. The fresh review read
all 711 candidate lines and the complete assigned canonical dependencies;
it did not read the later many-input corollary.

## The explicit restricted potential

Choose a^2+2b^2=1 and a!=b. Set

    u1=(a,b,b), u2=(b,a,b), u3=-(b,b,a),
    labels=(+1,+1,-1), masses=(1/3,1/3,1/3).

For example a=2/sqrt(6), b=1/sqrt(6) gives three linearly independent
inputs with inner products 5/6,-5/6,-5/6. Retain the full d=3 canonical
marks and 4-by-7 moving M. If H_i is the current upper activation at the
ORIGINAL input u_i, define

    U=(H1+H2-H3)/3,   F=E[cU],   C0=E[U0^2]>0,
    Psi=(1+E[c^2])/(C0+F^2),
    Phi=L(1+C0 Psi).

The complete initialized dynamics obeys

    L <= Phi <= 2L,
    Phi_dot <= -4 C0 Phi,       Phi(0)=2,
    L(t) <= exp(-4 C0 t),
    E[U_t^2] >= C0,             E[c_t^2] <= F(t)^2/C0,
    remaining physical length <= sqrt(L(t)/C0).

C0 is a specified initialized Gaussian expectation. There is no unknown
endpoint, future supremum or trajectory integral in the potential.
The full derivative of its readout-dependent factor is included.

The key proof is exact symmetry followed by readout linearity. Permuting
the three coordinates is an isometry of the complete normalized closure
and preserves its initialization and signed data. The three signed
predictions are therefore equal to F. The full flow is
Xdot=2(1-F) grad F, not a frozen-hidden equation. In the auxiliary
gradient parameter, q_s=2F and F_s=K=||U||^2+||grad_(w,M)F||^2. Then

    (q/F^2)_s = -2(qK-F^2)/F^3 <= 0,
    qK-F^2 = (q||U||^2-F^2) + q||grad_(w,M)F||^2.

The first nonnegative term is readout misalignment with the useful
signed feature; the second is actual hidden-gradient activity. The
initial limit q/F^2=1/C0 proves that the feature cannot collapse and
that progress cannot stall. This supplies the loss rate and the mixed
potential derivative. The auxiliary parameter and endpoint are used
only in the proof.

The signed Gram combination is

    9 E[U^2] = sum_i E[H_i^2] + 2 E[H1 H2]
                               -2 E[H1 H3]-2 E[H2 H3].

Thus the theorem protects a combination of same-label and different-label
correlations while allowing its individual terms to increase or decrease.
It does not say pairwise distances are monotone, that U's norm increases
monotonically, or that all fitted states coincide. Three initialized
constraints are independent, but the exact symmetry restricts the
realized residual to one direction. Generic multiresidual dynamics is
not covered by this reduction.

The family also contains a problem that no bias-free linear predictor
can fit or even classify with strict correct signs. Choose
a=-2/sqrt(6), b=1/sqrt(6). Then the ORIGINAL inputs satisfy u3=u1+u2,
while their labels are (+1,+1,-1). A linear functional positive at both
u1 and u2 is positive at their sum, contradicting the third label.
The theorem nevertheless fits all three with the nonlinear closure.
These three directions lie in the plane orthogonal to (1,1,1); this
does not identify the d=3 coordinate dictionary with the canonical d=2
dictionary after a rotation or projection.

The same proof yields a restricted-family corollary for every fixed
m=d>=3: v_i=b*1+(a-b)e_i, a^2+(m-1)b^2=1, a!=b, u_i=y_i v_i,
and any prescribed signs y_i with equal masses. The complete proof is
[three_coordinate_many_inputs.md](three_coordinate_many_inputs.md).
Root read and checked all 348 lines against the frozen three-input
argument and general-d source. The only new rank exception has
p=-(m-1)q, where the remaining cubic coefficient is
-(m-1)m(m-2)q^3, nonzero for m>=3; a coordinate outside any selected
pair excludes antipodal duplicates. All metric probability factors,
dimension-dependent existence bounds and full potential derivatives
were checked. This is an author-side corollary check, outside the
fresh isolated review of the original three-input candidate. It gives
a path to larger data families without making a generic-input claim.

## What was proved for the original circle problem

### Conditional exponential potential with arbitrary monotone loss comparison

[three_exp_root.md](three_exp_root.md) and its complete bounded analytical
check [three_exp_reparam_check.md](three_exp_reparam_check.md) give a new
state-only potential on any declared region ||c||<=C and L<=ell<1/3.
Compactify the exact upper tanh family by its sign-field limits, impose
the exact common-readout Gram constraint, and minimize the readout speed
over this compact feasible set. A positive continuous dissipation modulus
d(s) is explicitly defined, without requiring a positive least Gram
eigenvalue. Then

    Phi(L)=exp(-integral_L^ell ds/d(s)),
    Phi_dot<=-Phi,       L=h(Phi),

where h is the continuous increasing inverse. This gives a defined finite
time to every positive loss tolerance. It does not prove entry into the
region or an a priori readout bound along a generic initialized path.
The unit exponential rate normalizes this transformed potential; any
slow convergence remains encoded in h.

### Geometry, stationary escape and bounded returns

[three_exp_escape.md](three_exp_escape.md), independently reviewed in
[three_exp_escape_audit.md](three_exp_escape_audit.md), proves that the
lower three-input coefficient map has surjective derivative whenever
w-g is bounded in essential supremum. It also proves that every
positive-loss stationary state in this bounded-increment odd chart with
M!=0 is a strict saddle, and constructs actual positive-loss stationary
states of the ambient closure. Neither saddle avoidance nor arrival at
one of those stationary states is proved for canonical initialization.

The separate post-freeze [three_exp_escape_second_pass.md](three_exp_escape_second_pass.md)
proves:

- After entry below L=1/3, bounded readout RETURNS suffice for fitting:
  liminf ||c||<infinity implies L->0. If a positive limiting loss persists
  below this level, ||c|| must tend to infinity, not merely be unbounded.
- Positive limiting loss forces a positive asymptotic time fraction near
  zero or opposite signed upper fields. This is a precise degeneration
  alternative, not proof that degeneration occurs.
- With bounded readout returns, possible limiting losses are restricted
  to {0,1/3,2/3,8/9}. This list is necessary, not an attainability claim.

These improve the preceding uniform-bounded-readout result while leaving
the decisive initialized escape exclusion open.

### Reached-state capture and the necessity of its qualification

[three_exp_openfamily.md](three_exp_openfamily.md) proves a quantitative
capture theorem: at an actually reached state, a sufficiently small
residual relative to the current three-feature Gram implies exponential
fitting, full-state convergence, and exponential decay of L(1+||c||^2).
The strict criterion is open in the input triple. No initialized generic
seed satisfying it was analytically established, so a nonempty open
initialized family is not thereby proved.

The same file contains a separately identified, root-supplied exact
obstruction: L(1+||c||^2) is NOT globally nonincreasing on all generic
initialized triples. Start from a limiting contradictory law at e1
and a compatible sample at e2; symmetry forces the first prediction to
zero while the second grows. The potential exceeds its initial value at
an explicit finite time. Finite-time data continuity transfers this
strict increase to an open set of distinct non-antipodal triples. This
disproves that specific global candidate, not fitting or another potential.

## Other failed routes and what they actually rule out

[three_exp_invariant.md](three_exp_invariant.md) gives the exact nonlinear
matrix/readout balance identity and its circulation defect. A natural
readout-only primitive cannot cancel it universally. It also constructs
ambient canonical-mark states with fixed positive loss and arbitrarily
small FULL gradient. Their readout norms diverge; they are not claimed
reachable. Thus a loss-only dissipation modulus on every ambient state
is false, but an initialized mixed potential remains possible.

[three_exp_product_check.md](three_exp_product_check.md) rules out a later
quantitative proposal even with positive margins and loss below 1/3:

    ||c_dot||^2 (1+||c||^2) >= k(epsilon,ell)>0.

Its explicit relaxed upper-feature sequence has pairwise nonparallel
tanh coefficients, loss in [epsilon,ell], readout squared norm of order
rho^(-2) and squared readout speed at most order rho^6. Root checked the
entire countersequence, moment factors, determinants, positive margins,
loss interval, cubic cancellation and remainder bounds. Hidden gradients
are uncontrolled in this construction. It defeats only that readout-only
bound, not full-state convergence.

## Numerical evidence and its failed validity gate

The one modest predeclared diagnostic was executed exactly to its terminal
stop: seven integrations, 3.7003 CPU seconds, peak 111372 KiB, with no
extra sweep or follow-up run. The canonical finite-rule vector field and
energy identity were independently checked. See
[three_exp_diagnostic_report.md](three_exp_diagnostic_report.md), the
source [three_exp_diagnostic.py](three_exp_diagnostic.py), and its original
preregistration [three_exp_contract.md](three_exp_contract.md).

The scalar-reference potential displayed positive derivatives in the
finite diagnostic. However its primary population-refinement discrepancy
was 0.61460, above the predeclared 0.02 threshold. The population
monotonicity test is **inconclusive**. All tested finite runs reduced
loss substantially; neither fact proves or refutes population fitting.
No numerical observation is used to fill any proof above.

## Claim ledger and exact remaining obligation

| Claim | Status | Boundary |
|---|---|---|
| Explicit exponentially decreasing mixed potential, restricted d=3 permutation family | Proved at stated scope | Changes dimension and uses exact symmetry |
| Original generic three-input circle theorem | Open | Needs an initialized multiresidual progress estimate |
| Nonconvergent generic initialized circle example | Not established | Ambient constructions are not trajectories |
| Bounded-readout sublevel exponential reparametrization | Proved conditionally | C and ell must be declared and maintained |
| Bounded returns plus entry below 1/3 imply fitting | Proved conditionally | Return/entry estimates remain missing |
| Strict saddles in the bounded-increment stationary chart | Proved | Does not establish initialized saddle avoidance |
| Capture theorem and openness | Proved conditionally | No initialized seed entry certificate |
| Global monotonicity of L(1+||c||^2) | Falsified | An open set of actual initialized generic triples |
| Positive ambient loss-only full-gradient modulus | Falsified | Explicit large-readout ambient states |
| Readout-speed/readout-norm product bound on relaxed features | Falsified | Does not control hidden velocities |
| Primary numerical monotonicity test | Inconclusive | Population-refinement gate failed |

The highest-leverage missing estimate for the original setting must
control the actual interaction of hidden motion and readout growth.
Initial Gram positivity alone is insufficient. A sufficient route is to
prove entry below 1/3 and bounded readout returns, then obtain a declared
bound or a stronger dissipation law for a rate. Another is to prove
initialized entry into the exact capture region. The current results do
not justify asserting that either must hold for every triple.

## Provenance and internal checks

The three original routes were fresh scoped agents and were frozen before
comparison. Post-freeze checks and root-supplied arguments are separately
identified. The escape reviewer read the original frozen 494-line file;
an accidental appended second-pass section was removed, the exact original
hash restored, and the additional work retained in its separate file.
The reviewer documented the incident and independently verified the
restored hash; no later section was used in that isolated verdict.

Root owns this synthesis, current notes, the conditional variational
construction, numerical source/report, scope update and manifests. The
three-coordinate author owns its frozen candidate; its reviewer is a
fresh context with only the neutral assignment and complete frozen inputs.
Shared instructions and canonical scientific sources were rechecked
unchanged. No other study was read and no shared docs/code or Git index
was modified. Historical manifests remain attached to their old README
versions rather than being rewritten.
