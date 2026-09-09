# Three-input threshold evidence ledger

2026-09-08. Main research claim: find a positive activation coefficient
depending only on delta for the complete three-input odd-mixture L3
theorem. Status: **open**. No sufficient asymptotic has been established.

| Claim | Status | Scope and evidence |
|---|---|---|
| Two-input theta<=c_poly delta^2 theorem | Previously proved; unchanged | Earlier four-file proof and its original source chain |
| Three-input initialization infimum is comparable to theta^2 delta^2 | Proved | Fixed d>=2, 0<delta<=1/4, 0<theta<=1/2; primary geometry proof |
| Pairwise separation plus full input rank gives a delta-only input spectral gap | Falsified | REPORT §2: full-rank Gram Rayleigh quotient eta^2/(3+eta^2) at fixed pairwise separation |
| Near-collinear low-loss state requires R>(10 theta sqrt(delta))^(-1/4)-11 | Proved necessary state bound | REPORT §3 and routes/GEOMETRY.md; no existence or fitting assertion |
| Corresponding fitting-time lower bound | Exact under assumptions | Existing true strong GF with energy identity reaching loss<=3/8 |
| Initial O(delta) Gram-null arctangent remainder persists on every bounded raw L2 ball | Falsified | Rare-event first-layer change yields Omega(sqrt(delta)); not a reachable-GF example |
| Full raw kernel null projection <=256 theta^2 ||v||_1^2 (11+R)^6 | Proved | Any v in ker(Gamma), original raw state and four kernel blocks |
| Readout linearity, zero initial readout and GF imply monotone feature Gram | Falsified as a general inference | Explicit smooth finite-dimensional readout-linear example; no counterexample asserted for actual L3 flow |
| Combined Gaussian response has inverse-free L2 variance bound | Proved under explicit IBP hypotheses | Includes singular covariance and independent extra random arguments |
| L2 regression plus bounded individual queries gives uniform Lp response | Falsified as a general inference | Walsh example at identity covariance; actual neural family needs additional structure |
| Positive polynomial, exponential or constant cutoff for complete three-input theorem | Open | Neither interval nor single successful witness obtained |
| Such a cutoff or witness cannot exist | Not established | No positive-theta counterexample to original theorem found |

## Route registry

| Route | Mechanism and strongest result | Exact remaining gap | Reopen condition |
|---|---|---|---|
| Direct energy/source | Conditional finite-time raw energy control; inverse-free L2 combined response | L2 control does not supply reachable tails or strong compactness/continuation | A neural-query-specific moment/tail theorem or alternate strong construction |
| Nonlinear reference | Exact residual-direction and Gram identities; full-kernel null upper bound | No suitable nonlinear reference with controlled responses and trained nondegeneracy | A reference retaining Gram-null nonlinear signal with a noncircular source bound |
| Geometry | Sharp initialization scale; separation-dependent necessary fitting excursion | Geometry does not propagate source laws through training | A reachable-state law/moment estimate linking initialization to dynamics |

These routes have reached explicit unresolved implications. No route is
declared impossible. The old affine sufficient clock estimate becomes
circular at the symmetric nonlinear theta^(-2) certificate scale; this
is a failure of that estimate, not of all possible proofs.

## Supersession and audit corrections

The previous three-input open status is unchanged. The new partial
bounds sharpen its explanation without upgrading the global theorem.
The root report initially overstated absence of a PSD Gram-derivative
argument as an actual sign assertion for this architecture. Review
corrected that sentence. The direct-source variance claim was restricted
to the bounded primal query inputs, excluding arbitrary product and
derivative probes. The nonlinear-reference note now expressly allows
a direct construction with T-dependent constants and a T-independent
activation. Final review records identify those corrected files.

No experiments were run. No earlier mathematical source files were
edited. Sharpness is claimed only for the initialization scale, not
for the new excursion/kernel estimates or a sufficient activation law.
