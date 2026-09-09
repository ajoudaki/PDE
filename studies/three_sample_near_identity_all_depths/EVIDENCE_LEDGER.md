# Evidence and claim ledger

2026-09-08. User's final activation constraint is controlling.

| Claim | Status | Evidence and limitation |
|---|---|---|
| Large overall gain answers the requested theorem | Rejected as a substitution | User explicitly requires a perturbation of identity. Separate gain proofs are outside the target. |
| Excluding antipodal pairs rules out the forced oddness contradiction | Exact | Oddness forces opposite outputs only at an antipodal pair; no such pair is admitted. This does not prove training convergence. |
| Pairwise absolute separation forces a positive three-input linear Gram | False | Three unit vectors at 120-degree angles have pairwise correlation -1/2 and sum to zero. |
| Positive theta gives independent initialized features | Proved | Cubic Gaussian tensor lifting, including singular input Grams, in INITIALIZATION.md. |
| Normalized initialized conditioning worsens exponentially with depth | Superseded | INITIALIZATION.md proves exact improvement of the extremal normalized eigenvalues. The earlier e^-9 propagation loss is removed. |
| Initial feature energy and least eigenvalue have order 1/L at fixed theta,delta | Proved | Explicit reciprocal-variance bounds and the positive normalized Gram floor. No claim of uniformity as theta,delta also tend to zero. |
| A positive absolute nonaffinity gap can be uniform over every initialized depth for this exact unit-sum mixture | False | Its Gaussian affine-regression error has order L^-3 at fixed theta. A fixed-depth time-uniform gap remains possible. |
| Near-identity fitting can retain a theta-independent rate on all admitted triples | False | Conditional necessary state/time bounds in NECESSARY_FITTING_SCALE.md; finite fitting times diverge as theta decreases. |
| A strictly positive theta-dependent global theorem is false | Not established | None of the route failures or necessary bounds is a counterexample to that theorem. |
| Covariance-weighted response control yields L2 returns | Exact under stated Gaussian integration-by-parts hypotheses | SOURCE_ROUTE.md includes singular covariance. |
| That L2 bound supplies the required higher-moment tails | Unproved; generic inference invalid | Smooth translated-bump feature-span example in SOURCE_ROUTE.md. It is not a neural trajectory counterexample. |
| True-gradient finite-partition approximants are global with uniform compact-time energy bounds | Proved construction | ENERGY_GALERKIN_ROUTE.md. These are auxiliary population approximations, not the original finite-width algorithms. |
| Those approximants converge strongly to the canonical population flow | Conditional only | The explicit unresolved-coordinate compactness condition remains unproved. |
| A small offset repairs initialized affine rank deficiency | Proved | Both route notes. Global unit-slope affine fitting and a usable response budget remain missing. |
| Complete global near-identity population/GF/GD theorem for three inputs at general depth | Open in this analysis | No theta_(delta,L) cutoff claimed. The missing trajectory and identification implications are explicit in REPORT.md. |

No experiments were used. The final reviews certify exact partial
statements at recorded hashes, not the unproved final row.
