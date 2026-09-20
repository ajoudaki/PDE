# Internal validation and claim ledger

Date: 2026-09-18. Primary agent owns the synthesis and this record. These
are internally checked study results, not promoted established material.

## Scope and sources

The user requested the original canonical p=1 closure, the specified
rotated equilateral family, singular states, and ideally an initialized
exponential loss-controlling potential. The model change required a new
study. No previous study's proof, report, numerical array, or unpromoted
finding was used as a scientific input. The equilateral data were specified
anew in this study's contract.

Startup HEAD was `019e3630237e33f58b9636c0aa67a039bebf0182`; index empty.
Shared instructions and workflow Part 1 were read, the complete scientific
reading guide and notation were read, and the exact initialized coefficient
source and complete relevant population-equation/well-posedness sections
were checked. The initialized p=1 dictionary is the Cholesky polynomial
core of C.4.7.10, with eta=1/4096, not the earlier pilot/symmetric-whitening
dictionary of C.4.7.9. The state, physical gradient equations and continuation
argument transfer with those exact features as the book specifies.

Relevant established source hashes:

| Source | SHA256 |
|---|---|
| docs/observable_p1.md | 0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba |
| docs/global_nonlinear.md | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/README.md | 60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad |

The exact main equations preserve both initialized matrix bands, the joint
lower correlations, the actual transpose, the unhalved loss and the original
physical metric. Constants are removed only on the proved canonical odd
parity class. No maintained code API or external mathematical theorem was
used to fill a proof gap.

## Independent routes and review record

Three fresh agents started from explicitly assigned established sources,
without inherited study discussion or each other's findings:

| Author route | Frozen report | Main outcome |
|---|---|---|
| p1_initial_geometry | initial_geometry.md | Exact monotone initialized code map, finite Gram positivity, initial-stall classification, rotation-symmetry scope. |
| p1_stationary_geometry | stationary_geometry.md | Lower submersion, exact finite singularity and stationary criteria, saddle classification and stationary-loss gap. |
| p1_positive_potential | positive_potential.md | Genuine three-input initial-rank result and a complete conditional trapping lemma; initialized unit-label convergence not proved. |

The primary agent read all complete route reports, checked their derivations
against the source equations, and synthesized them only after the candidates
were frozen. Two further fresh isolated agents separately reviewed the
initialization and stationary reports, with the complete coefficient source
and subsequently authorized characteristic-existence sections as dependencies.
They did not see the README, other reports or prior verdicts. Their full
reports are `audit_initial.md` and `audit_stationary.md`.

| Reviewed source | Final SHA256 | Verdict |
|---|---|---|
| initial_geometry.md | 6856fb3d2cca5d59d1b00c4bd3cf87dd74f87315999e244b42dd1662647f091d | PASS, complete stated scope. |
| stationary_geometry.md | 2fce30a3824d8bff4ecc9b04771f3986bc539735722f3434168103c464e7cfbc | PASS after explicit label/parity scope corrections. |
| positive_potential.md | 726fe88584b8c68608168bea54da59192e236770980d293b6b1d7b3e876bd2c5 | Primary-agent analytic check for its conditional statement only. |

The initial reviewer independently checked the combined regression
derivative rather than assuming either coefficient sign; conditional variance
and Gaussian integration by parts supply the proof. The all-finite-sample
ridge independence also covers collinear vectors of distinct magnitude.

The stationary reviewer checked the support/linear-form argument for arbitrary
measurable bounded displacement, every matrix-rank stratum, the confluent
ridge derivative argument, and both the negative-second-variation and cubic
descent constructions. Exact rational enumeration reproduced the thirteen
necessary stationary loss values for the specified weights.

The review prompted two scope corrections. Loss/saddle clauses now use the
specified nonzero binary labels, removing an overly broad arbitrary-label
sentence. Canonical bounded-displacement states explicitly have odd w,c;
nonodd active equations are labeled an auxiliary reduced extension, since
the full p=1 constants need not remain inactive outside parity. The reviewers
also requested and received the missing established uniqueness dependencies.
All identified objections were resolved in the final hashes.

## Synthesis checks

The primary agent checked all additional statements in `result.md` directly:

* The readout witness c_*=sum(G(0)^(-1)y)_j H_j(0) fits because its prediction
  vector is G(0)G(0)^(-1)y. It is bounded and odd, and uses only frozen
  initialized features and data. It is not asserted to be the trained endpoint.
* Completing the square in each input antipodal class proves equation (7).
  Combined with Gram independence, this shows that initial stalls coincide
  with the zero predictor being optimal among all odd predictors on finite
  data. It does not classify continuum laws or later failures.
* Nonstationary initialized trajectories cannot reach an equilibrium at any
  finite time by local backward uniqueness. This gives strict finite-time
  loss decrease, not convergence to zero.
* The full tangent expression (12) is the sum of the exact three gradient
  block Grams. Differentiating R^T Theta^(-1) R gives both terms of (13),
  including the changing metric; no favorable sign is omitted.
* The complete-collapse fitting construction uses three independent lower
  columns, maps them to z,z,-z and a fourth basis vector to an independent
  vector, and chooses c=H/EH^2. Its backward vector has positive pairing with
  z because s tanh(s) phi'(s)>0 away from s=0. Thus its full differential is
  nonsingular even though the upper Gram has rank one. This is a finite
  representation example, not an accessibility assertion.
* The conditional trapping lemma's norms, constants and first-exit argument
  were checked independently by the primary agent. Its gate Lipschitz
  estimates use the supplied population feature contractions and bounded
  increments; integrating exp(-kappa t) bounds the whole future displacement.
  The failure to prove its entrance from L(0)=1 remains explicit.

“Hessian” in the saddle statement denotes second variation along bounded
admissible perturbations. This suffices to rule out a local minimum in the
physical topology; no unnecessary C2 Frechet theorem on all of L2 is invoked.

## Numerical check and resource accounting

One diagnostic was planned before execution in `diagnostic_plan.md` and
implemented in `diagnostic.py`. All ten predeclared solves completed in
18.8292 seconds under the 120-second single-thread cap. Coefficient and time
refinement checks passed; population refinement and final-loss criteria did
not. `diagnostic_result.md` records the exact command, environment, all
outcomes and limitations. The main analytic theorems have no numerical
premise. No extra run or longer horizon was used after seeing the failures.

The final archive is under
`data/generated/p1_three_input_geometry_20260918/equilateral_01/`.
The primary agent additionally read every stored observation and every
endpoint array and verified finite values: ten completed solves, no NaN or
infinity. This check used JSON reads and NumPy load with allow_pickle=False;
it did not rerun training. All source and generated-product hashes are in
`manifest.sha256`.

## Current claims and unresolved target

**Exact, internally checked:** the complete finite-data initialization
classification; all-angle initialized equilateral nondegeneracy; exact
finite-state singularity/stationarity conditions in the three-input
canonical parity/bounded-displacement class; absence of positive-loss local
minima in that class; a positive stationary-loss gap; and the stated finite
representation constructions.

**Conditional, internally checked:** exponential loss decay and finite state
travel after the quantitative finite-state trapping test is reached.

**Empirical, unresolved under declared population refinement:** representative
equilateral finite rules reach losses near 3e-4 to 5e-4 by T=120. No population
or asymptotic fitting conclusion is inferred.

**Open:** whether every initialized equilateral rotation converges to zero;
deterministic avoidance of positive-loss stable sets; asymptotic escape or
loss of conditioning; classification outside canonical parity or for limits
at infinity; an unconditional exponential, loss-controlling potential from
the prescribed initialization on a general unit-label three-input family.

The next decisive mathematical obligation is a trajectory estimate closing
saddle avoidance/escape or proving entry into a regular fitting basin from
data alone. Neither initial full rank nor absence of bad local minima closes
that obligation. No such estimate is assumed in a theorem here. This bounded
pass is complete with that affirmative target unresolved; no promotion,
shared-source edit, Git write or expanded numerical campaign follows from
this record.

## Authorized positive-theorem continuation, 2026-09-18

The subsequent user request reopened the initialized positive convergence
question in this same study. The exact model and circle domain stayed fixed.
No new experiment, shared-source change, Git stage or commit was performed.
The synthesis is `positive_continuation.md`.

Three fresh routes independently read the established canonical equations
and the two complete checked mathematical reports of this study. Their
initial candidates were frozen before cross-pollination. The scalar
readout-radius mechanism was then supplied to the open-family route, and
the primary agent asked the energy route for a separate compatible-collision
interpolation lemma. Both follow-ups disclose that input in their reports.

Frozen candidate versions checked:

| Candidate | SHA256 | Actual check |
|---|---|---|
| `global_positive_route.md` | `36830e4ad5d89ce983c2c0144055dc6e52c82b6192f8b238bd5d41a4ac18b487` | Complete primary reconstruction and fresh isolated `audit_global_positive.md`, PASS within its stated scope. |
| `open_family_route.md` | `2e4c0208c9e94174001c0b12d11c8e8d3603064ed3008d0b5b943f2e8f79679a` | Primary agent read the complete 625-line report, checked reflection invariance, exact gradient factors, finite signal-clock bounds, endpoint transverse derivative, and local openness. The synthesis adds the explicit prefix-to-tail exponential inequality. |
| `energy_geometry_route.md` | `8c386feeae81bd2bbcf5a201f5cb3ba2a44fed92b29be16fe583146f38f0a391` | Its complete Section 8 was independently audited in `audit_collision_interpolation.md`, PASS. Primary agent reconstructed that proof and norm identities. Earlier diagnostic sections have author checks only. |

Both full isolated audit reports were read by the primary agent. Neither
reviewer read prior verdicts, other routes, study history or another study.
Their reports give exact source coverage and unchanged dependency hashes.
The global audit notes three scope conventions: uniform third-order input
remainders refer to bounded characteristic-displacement neighborhoods, the
axis jet reference is (e1,+1), and the weighted data space is L2(mu) after
null atoms are removed. These are the conventions used in the synthesis.
It also supplies a C2 argument that handles the small-correction obstruction
under strong L2 row convergence without assuming uniform third moments.
The frozen candidate was not silently changed after review.

The independent collision review checks both confluent independence lemmas,
the normalized third-feature remainder even at arbitrarily unequal scales,
compactness over every collision pattern, and the exact transformed target.
Its conditional loss consequence assumes the stated all-time geometric
protection; neither the candidate nor the review establishes that protection.

Additional root check: on the open two-input family the reference's scalar
residual coercivity is uniform on every chosen finite prefix. Finite-time
continuous dependence transfers it to neighboring data, while the proved
regular fitting basin controls the entire tail. Taking the minimum of these
two rates proves Phi=L and Phi'<=-lambda Phi from initialization, with no
assumed future bound. The neighborhood and rate exist by the proof but were
not numerically evaluated. This result still has only two inputs.

**Unchanged open target:** a genuine three-input circle configuration with
an unconditional exponentially decreasing loss-controlling potential from
the canonical initialization. The new scalar convexity proof loses a
residual-direction rotation term; the collision-compatible comparator proof
needs current upper codes protected from zero, incompatible antipodes and
escape; the reference-transfer proof needs a genuine regular fitting
reference. None of these bridges is assumed solved. No claimed all-time
result has been inferred from initial Gram positivity, absence of positive
local minima, or numerical monotonicity.
