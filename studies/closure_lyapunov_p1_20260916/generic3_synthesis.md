# Generic three-input continuation: results and exact remaining gap

2026-09-16. Research only. The requested unconditional mixed-potential
theorem is **unresolved**. No counterexample to convergence of the prescribed
initialized dynamics has been constructed. Failure of a candidate potential
is not evidence that no such potential exists or that training fails.

## Target retained

The model is the canonical p=1 population closure, with all evolving
blocks (Gamma_1,Gamma_2,M), complete joint initialization, frozen dictionary
marks, actual transpose, and the physical unhalved probability-weighted
square-loss metric. The data are three equally weighted, distinct,
non-antipodal circle inputs with labels (+1,+1,-1), without imposing a
dictionary symmetry. This is the target in generic3_contract.md.

The user's clarification is adopted: a mixed potential may decrease
while any individual within-class or between-class distance increases
or decreases. The short-time same-class expansion result below is only
a stress test for candidates. It does not refute the requested mechanism.
Reaching every positive loss tolerance in finite time is the fitting
target; exact zero loss need not occur at a finite time.

## Strongest new convergence statement

For the exact initialized trajectory, if

\[
  \mathcal L(t_0)<1/3\quad\text{for some finite }t_0,
  \qquad \sup_{t\ge t_0}\|c(t)\|_{L^2}<\infty,
\]

then \(\mathcal L(t)\to0\). This result allows arbitrary fluctuations
of individual hidden distances and does not assume a bound on w or M,
or uniform positivity of the complete hidden Gram matrix. It does not
prove a rate, convergence of the full state, or either displayed hypothesis
for every generic initialized triple.

The full proof is in generic3_stationary_geometry.md; the separate
post-freeze analytical check is generic3_compactness_check.md. The exact
upper fields have the form tanh(Z dot v_i), where the fixed two-dimensional
mark Z has positive density on a square. Their L2 closure is compact and
adds only sign(Z dot d) boundary fields. At most three distinct nonzero
fields in this closure are independent after grouping equal/opposite
fields. This follows from the first three odd tanh coefficients and a
Vandermonde determinant, and from the jumps of the sign fields.

Loss below 1/3 makes every signed prediction strictly positive. With a
bounded readout, an asymptotically stationary sequence cannot have a zero
signed feature or an opposite signed feature pair. Identical limiting
fields have identical limiting signed predictions. The exact readout
equation and independence then force every signed prediction to be one.
Finite energy supplies the stationary sequence; monotone loss converts
subsequential fitting into fitting along the entire trajectory.

This identifies a class-compatible geometry without selecting a unique
representation. Equal same-class features are allowed, as are distinct
same-class features. Opposite classes cannot have identical limiting
features when the readout is bounded and both are fitted. Other neutral
directions remain uncontrolled.

## Claim ledger

| Claim | Type and actual check | Scope or unresolved issue |
|---|---|---|
| Upper-feature compactness, independence including sign limits, and bounded-readout convergence below loss 1/3 | Proved conditional theorem; root derivation and complete bounded post-freeze analytical check | Neither threshold entry nor readout boundedness is proved generically. |
| A nonglobal readout-stationary state must have a zero signed feature or an opposite signed pair | Exact geometry; proved in the same root argument | Does not establish avoidance or instability along the initialized trajectory. |
| A reached-state capture inequality implies exponential fitting and full-state convergence | Conditional theorem in generic3_metric_route.md; author derivation and root algebra check | The criterion provably fails at canonical initialization; later entry remains open. |
| Normalized margin acquires an indefinite residual coupling term | Exact identity in generic3_metric_route.md | An unsigned term in the proof is not a counterexample along the canonical trajectory. |
| Mixed feature/readout barriers below loss 1/3 | Exact inequalities in generic3_metric_second_pass.md; author derivation and root check | They constrain a product; unbounded readout is not excluded. |
| Nonlinear balance defects and o(sqrt(t)) raw-state growth | Exact identities and energy consequence in generic3_metric_second_pass.md | Neither gives a uniform state bound or supplies deep-linear balancedness. |
| Both layers' same-class squared distance initially increases on an open set of admissible triples | Proved in generic3_geometry_route.md; fresh complete isolated audit PASS | Refutes separate attraction monotonicity only; not a mixed potential or fitting. |
| Generic initialized unit-label fitting and a mixed current-state potential | OPEN | No complete proof and no convergence counterexample. |

The capture route's comparison quantity uses accumulated residual along
the trajectory. Its second pass explicitly corrects its interpretation:
it is **not** a potential determined by the saved closure state. The
historical first-pass artifact is preserved unchanged.

## The missing estimate

A sufficient route to unconditional fitting would establish both finite-time
entry below loss 1/3 and an all-time readout bound. More generally, a mixed
current-state potential could replace those separate bounds by excluding
loss-persisting degeneration compensated by readout growth. These are
sufficient proof routes, not claimed necessary conditions for convergence.

Initial Gram positivity already guarantees representability. It does not
guarantee that training preserves that Gram. Energy gives only time-integrated
squared speed; the exact readout identity gives ||c(t)||^2 <= t. These
bounds do not prevent unbounded readout over infinite time. The nonlinear
balance defects have uncontrolled signs, so a bound from a linear network
cannot be transferred to this tanh closure.

The scalar-residual potential from all_angles_result.md remains valid for
its proved pair and symmetry-reduced four-point families. Its proof does
not extend by dropping the extra residual coupling in a generic triple.
No new state-only potential with the requested unconditional consequence
has been established in this continuation.

## Provenance, verification and close status

Two fresh scoped routes were frozen before comparison. Root checked their
complete arguments against the canonical equations and normalization.
generic3_audit independently read the complete geometry candidate and
its specified canonical dependencies; the unchanged candidate passed.
generic3_geometry subsequently checked the root compactness argument,
with exposure and limited scope recorded. That check is not an isolated
review of the complete study. No promotion review is claimed.

No numerical experiments, external scientific inputs, shared book/code
edits, or Git-index changes were used. Canonical sources and the frozen
geometry candidate were checked unchanged; generic3_manifest.sha256
records the final continuation artifacts and source versions. Previous
manifests remain historical snapshots, including older README versions.

Final deterministic checks: `sha256sum` reproduced the contract's five
instruction/canonical hashes and the audited geometry-candidate hash
536726d952eb3fb3487a799903c028c4b9f98a4be54df854a3b2075dc59eb0fb.
A Python pathlib/re link check covered README and all eight generic3
Markdown artifacts: 41 local links, with no missing target other than
the manifest awaiting generation at that check. The manifest is generated
after this text and checked against every listed file. These are source
and artifact checks, not numerical evidence or machine-checked proofs.

The bounded analytical routes and their checks are complete. The primary
research question remains open. The next useful mathematical obligation
is a joint geometric/readout estimate controlling possible escape, not
another proof of separate pairwise monotonicity or initialized rank.
