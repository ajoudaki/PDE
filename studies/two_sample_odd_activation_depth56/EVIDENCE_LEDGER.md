# Claim ledger and supersession

2026-09-07. Research scope: new theory with adversarial proof review.
No empirical claims or trajectory experiments enter this proof.

| Claim | Rung | Status | Supporting artifact | Scope / falsifier |
|---|---|---|---|---|
| C1: Same old c_poly works with power ten at L5 and L6 | Complete global population and compact-horizon width theorem | Proved | PROOF Sections 1-6, all companions | Original two-input model; failure of source closure or a required limit bridge blocks the claim |
| C2: Same prefactor permits powers31/8,9/2,21/4,83/14 at L3,L4,L5,L6 | Same full theorem | Proved | PROOF(1),(25)-(27) | One common coefficient on this finite depth range, all separated configurations |
| C3: Every fixed L>=6 permits explicit c_L delta^(9-43/[2(L+1)]) | Same full theorem, L fixed before width limit | Proved | PROOF(1)-(7), affine Section7, source Sections4-5 | c_L depends on L; no L(n) result |
| C4: One positive common prefactor works for all finite depths | Stronger uniform existence claim | Open | No complete bridge | Current depth-dependent estimate does not prove or disprove this |
| C5: The convex activation admits depth-uniform positive initialization rate and nonaffinity constants in the earlier stated sense | Stronger numerical uniformity | Falsified in that scope | Immutable depth4/DEPTH_UNIFORMITY.md | Initialization variance tends to zero; does not falsify C4 |
| C6: A common exponent eight follows merely by replacing every incoming-field power with its new Gaussian-part scale | Proposed source estimate | Rejected | SOURCE_RESPONSE Section6 | Omits deterministic B-gate errors; not an impossibility theorem for power eight |

## Dependencies and adversarial checks

All four new mathematical files are frozen at CANDIDATE_HASHES.json;
28 older mathematical files are frozen at DEPENDENCY_HASHES.json.
Review outcomes belong to REVIEW_STATUS.md and reviews/, with exact hashes.
The proof depends on the actual older finite Gaussian-conditioning and
strong-limit derivations, never on a review's PASS label.

The root and author checks identified and retained two necessary controls:
1. The full derivative perturbation contains a DeltaV B and B DeltaG;
   their powers cannot be replaced by the incoming q moment power.
2. The enlarged active backward box must explicitly bound its positive
   transfer, while the inactive sector needs a separate small box.

The Gaussian-part moment lemma uses actual same-array L2 bounds and
triangle inequalities, followed by Gaussian moment estimates and a small
feedback absorption. It assumes no independence of Gaussian and nonlinear
remainders. Strict factors on both sides of each backward defect preserve
source-step densities during positive-chain compression.

## Supersession

Three independent full-proof reviews passed at the final hashes. C1-C3
extend rather than invalidate the old
L3/L4 power-ten results. The new smaller sufficient powers supersede their
quantitative strength, while all old model, topology, limit-order, motion
and nonaffinity requirements remain. The rejected exponent-eight ledger
is not used. Optimal exponents, useful-size prefactors, and one common
activation for every finite depth remain unresolved.

## Final update

C1-C3 are promoted to proved under the frozen contract following the
completed argument and three independent complete-proof checks of the
exact final files. No unresolved gap was reported. The review outcomes
and their scope are recorded in REVIEW_STATUS.md. C4 remains open, C5
retains its narrower obstruction, and the rejected C6 ledger remains unused.
All 28 old dependency hashes were reverified after final assembly.
