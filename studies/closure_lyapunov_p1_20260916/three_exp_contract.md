# Exponential-potential continuation for three generic inputs

2026-09-16. Explicitly reopened by the user's request to work harder until
the three-input exponential-potential question is resolved. This is a
continuation of the same study, not permission to use another study.

## Exact primary claim

For each three distinct non-antipodal normalized circle inputs with masses
1/3 and labels (+1,+1,-1), seek an explicitly defined nonnegative function
Phi of the complete current canonical p=1 closure state and declared fixed
data, such that along the prescribed initialized physical flow

    Phi(S_t) <= exp(-lambda t) Phi(S_0), lambda>0,
    L(S_t) <= h(Phi(S_t)),

where h is increasing, h(s)->0 as s->0, and its constants and lambda may
depend on the input geometry. No unknown future path, supplied endpoint,+trajectory clock, arbitrary rotation of the dictionary, frozen-hidden
substitute, small labels, or changed gradient metric is allowed. A general
h permits slower-than-exponential loss decay; this is recorded explicitly
and is not a loophole for assuming fitting.

The target retains all three independent residuals. A genuine open generic
unit-label family is useful partial progress, but does not resolve all
permitted triples. Conditional capture, stationary classification and
initial representability also do not resolve the primary target.

## Work registry and resources

Three fresh independent agents receive separate explicit input scopes and
own only the listed flat artifacts. Candidates are frozen before comparison.
The required research and rigorous-mathematics skills apply to every route.

| Route | Mechanism | Artifact |
|---|---|---|
| three_exp_invariant | Multiresidual invariant or mixed geometric potential | three_exp_invariant.md |
| three_exp_escape | Mark transport, reachable-state rank, stationary escape | three_exp_escape.md |
| three_exp_openfamily | Structural stability and an initialized genuine open family | three_exp_openfamily.md |
| root | Nonlinear dissipation reparametrization and targeted candidate stress | three_exp_root.md |

Initial route round: approximately 15–20 minutes of substantive reasoning,
then freeze and compare concrete claims. Follow-up rounds require a new
lemma or mechanism, rather than repeated statements of the same gap.
Reserve capacity for reconstruction and an independent check if a complete
candidate emerges. No fixed global proof-search deadline was supplied by
the user. This instruction does not authorize an unsupported positive
conclusion if the mathematical obstruction remains unresolved.

No shared book/code or Git-index writes. Current instructions, source hashes
and HEAD match the preceding generic3 snapshot. Established docs/code and
this study are the only repository scientific inputs. A narrow external
literature search screened for matching convergence mechanisms; no external
theorem has been imported at contract creation.

## Small diagnostic: preregistration

Decision question: does the earlier scalar regular potential remain
monotone on genuine three-residual initialized trajectories, or does the
exact additional residual coupling produce a visible violation?

Candidate: (1+||c||^2)/(C_0+F^2), F=(f_1+f_2-f_3)/3 and
C_0=||(H_1(0)+H_2(0)-H_3(0))/3||^2. Its physical derivative is evaluated
from the full finite-quadrature velocity, including moving features.

Three predeclared angle triples in radians, all with labels (+1,+1,-1):
(0.1,1.4,0.75), (0.15,2.5,4.3), (0,pi-0.2,pi+0.4).
These respectively stress an intervening opposite label, a nonsymmetric
spread, and nearly antipodal same labels. No angle sweep or post-selection.

Use the maintained canonical correlated initializer and full w,c,M
equations. Deterministic population quadrature is a diagnostic approximation,
not the population theorem. Baseline Q=2048,P=512; refinement Q=4096,P=1024.
Integrate with float64 DOP853, rtol=1e-8, atol=1e-10, at most physical T=400,
stopping earlier at L<=1e-8. One tighter baseline integration (rtol=1e-10,
atol=1e-12) is authorized for the first apparent violation, or the first
case if none. At most seven integrations, one numerical thread, 180 CPU
seconds total integration/initialization budget, 1 GiB working arrays and
250000 RHS calls per integration. Stop at the first exceeded resource
limit; retain incomplete results without changing parameters.

Sample 401 fixed times on [0,400] and the stopping endpoint. Record loss,
readout norm, readout Gram eigenvalues, total residual-direction curvature,
candidate value and its exact finite-system derivative. A candidate violation
requires a positive derivative above 1e-4*max(1,initial candidate value),
with the same sign at both quadratures and at least 100 times the matching
time-refinement discrepancy. Population refinement must change predictions
by at most 0.02 on the compared panel; otherwise classify inconclusive.
No observed violation only retains the candidate; it is not a proof.
Fitting, spectral growth and norm traces are descriptive secondary outputs.

Reproducibility: preserve script, source hashes, exact configurations,
software/thread settings and raw time panels in a fresh study-owned
generated directory. Deterministic quadrature uses no random seed. No
further numerical branch is authorized by this diagnostic's outcome.
