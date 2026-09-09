# Evidence ledger: OMFP continuous-time control

Date: 25 August 2026.

| Claim | Level | Evidence | Remaining obligation |
|---|---|---|---|
| Dyadic scalar convergence follows from \(\sum_j b_{2^j}^*(\rho)/2^{5j}<\infty\) and \(|\kappa_m|\lesssim m^2\) | proved | direct estimate (1.7) in THEOREM_AND_AUDIT.md; independently derived in route_a.md and route_c.md | none |
| Any \(b_m^*=O(m^{5-\delta})\), \(\delta>0\), suffices | proved | geometric series | none |
| Fixed-\(m\) \(C^5\) plus a cubic coefficient does not imply dyadic summability | proved as a logical counterexample, not an OMFP counterexample | entire scalar family in route_c.md, Proposition 4.1 | network realizability is not claimed |
| Restartable Lipschitz split-defect sewing | proved | THEOREM_AND_AUDIT.md (1.1)--(1.3) | OMFP verification depends on activation |
| Depth-two Osgood sewing from the reachable moment bound \(\sup_{p\ge2}p^{-\alpha}\|Q\|_p<\infty\), \(\alpha\le1\) | proved conditional implication | route_b.md, Lemma 6.1 and Theorem 8.1; summarized in THEOREM_AND_AUDIT.md §1.1 | prove the reachable moment bound |
| The arctan natural coordinate directly identifies the actual discrete scheme | false | exact correction terms \(h^2Q^2+h^3Q^3/3\) in route_b.md §9 | needs uniform \(L^6\) control even to compare in \(L^2\) |
| The identity-activation \(t^4h^5\) bound at every fixed depth | proved; repaired assembly passed independent re-audit | fixed-width theorem WIDTH_DEPTH_TIME.md; exact temporal-DAG/fixed-operator intertwining and cubic law CUBIC_DEPTH_TIME.md; transported-defect theorem UNIFORM_BSERIES.md; explicit hypothesis check in THEOREM_AND_AUDIT.md §§2--4; independent route_d.md | none |
| Nonlinear \(L=2\) WRE\(_\alpha\), \(\alpha<1\) | open | exact ledger and implication in route_c.md §6 | mixed moving-query/aggregate-adjoint response resolvent |
| Nonlinear \(L=3\) connector transfer preserving exponent \(<1\) | open | route_c.md §7 | first close \(L=2\), then prove rank-independent connector transfer |
| General nonlinear OMFP IDE from width-first discrete steps | open | state sewing is conditional; raw-square supplies a separate no-go outside the bounded-derivative class | reachable tails, restart stability, state readout UI |

## Falsification checks

1. The identity activation has same-sign nonzero fifth coefficients of order
   \(t^4\) at depth two, so a martingale or cross-scale cancellation argument
   cannot be the general mechanism.
2. The fixed connector adjoint is not bounded on ambient \(L^p\), \(p>2\);
   any proof using such a bound is invalid.
3. A non-affine Nemytskii map is not \(C^2:L^2\to L^2\); scalar bounded
   derivatives do not justify the abstract Banach theorem.
4. Width is taken first at each fixed finite step list in every proved or
   conditional statement above.
