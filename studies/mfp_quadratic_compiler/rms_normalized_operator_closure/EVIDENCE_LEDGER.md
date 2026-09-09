# Evidence ledger

Status vocabulary: `proved`, `conditionally proved`, `formal`, `heuristic`,
`numerical`, `refuted`, `open`.

| ID | Claim | Status | Scope / assumptions | Audit obligation |
|---|---|---|---|---|
| E0 | Research contract in `PROTOCOL.md` is frozen after correcting the `G`-metric scaling before promoting any model claim. | proved | This study only. | Any later change must be logged explicitly. |
| E1 | `alpha,beta >= sqrt(epsilon)` at every finite width and time. | proved | Algebraic, `epsilon>0`. | Does not control coordinates or projection conditioning. |
| E2 | RMS normalization bounds empirical output norms but not coordinate maxima. | proved | Deterministic vectors. | Quantify consequences for products and the kernel. |
| E3 | Exact finite-width feature dynamics, reduced normalized-feature system, tangent kernel, and physical loss identities in `FINITE_WIDTH_THEOREM.md`. | proved | Model in protocol. | Certified by a second isolated hostile derivation. |
| E4 | Every trained layer has nonzero initial gradient almost surely. | proved | Finite width, iid Gaussian init, `epsilon>0`. | Certified; “projection” means positive contraction, not idempotent map. |
| E5 | Layerwise initial kernel limits are `27/D,36/D,48/D`; coherent hidden representations move at order one. | proved | Width tends to infinity; nonzero target for physical non-laziness. | Certified independently; no claim yet of order-one-time kernel convergence. |
| E6 | A finite admissible autonomous closure exists. | open | Full contract. | Construct and prove all convergence gates. |
| E7 | No finite admissible autonomous closure exists. | open | Full frozen class. | Must prove exhaustion, not an ansatz-specific failure. |
| E8 | Eliminating `G` exactly creates the two-time Grams `<H_s,H_t>` and `<R_s,R_t>`. | proved | Every finite width. | Retaining a current operator avoids this particular memory. |
| E9 | Any fixed finite scalar-overlap/Krylov-response cavity ansatz fails generically: the first alignment operator has an `n`-dimensional cyclic orbit almost surely. | proved | Gaussian initialization, fixed-finite response class. | Does not exclude a genuine operator field. |
| E10 | RMS identities and bounded naive Hilbert norms do not imply kernel uniform integrability; exact on-manifold spike sequences violate it. | proved | Ambient/restart states. | Reachability from iid initialization remains open. |
| E11 | A fixed sub-Gaussian or sub-exponential bootstrap propagates through the dynamics. | refuted | Already at initialization/first derivative: tails degrade from `psi_1` to about `psi_{2/3}`. | Try weighted moment/lognormal envelopes instead. |
| E12 | The naive single-Gaussian-extreme Riccati runaway is self-consistent in the exact flow. | refuted | The exact `-fY_i` normalization/readout feedback becomes leading parametrically before one row contributes order one to the RMS denominator, under an explicit diagonal/incoherence stop. | A simultaneous row/column concentration theorem or its probabilistic exclusion is still required. |
| E13 | Weighted tail uniform integrability follows from the exact loss/parameter-energy identities alone. | refuted | Deterministic multi-coordinate spike families obey the available low-norm bounds while concentrating the kernel. | Prove reachability-specific Gaussian estimates, not another low-energy inequality. |
| E14 | One current Malliavin response field closes recursive Gaussian integration by parts. | refuted | One-shot reduction closes, but reducing the response equation introduces `D_Gamma^2 X`, then all higher jets. | Retain the source action unreduced or prove a finite invariant response quotient. |
| E15 | A fixed-cutoff traffic flow already supplies an admissible source for the research contract. | open | A formal finite-generator cutoff flow was derived, but the proposed ultraproduct source is contractually forbidden and the continuous-time master-theorem passage is unaudited. | Replace it by a canonical source and independently prove Euler-to-flow convergence. |
| E16 | The preregistered early-spike diagnostic selects either the spike or barrier branch. | numerical, inconclusive | Ten of sixteen matched cases completed before the ten-minute cap; kernel peaks were tight but hitting ratios were mixed. | It changes no theorem claim and triggers no numerical branch. |
| E17 | The iid trajectory has no nonzero output-action layer on all vanishing time scales. | partially proved, otherwise open | `f(T_n)-f(0)->0` is proved for `T_n=o(n^-3/4)`, and fixed-mass simultaneous row/column packs are excluded before `o(n^-1/2)`; the remaining scales up to `o(1)` are open. Ambient packed states do not refute this iid-reachable claim. | Prove a stopped adaptive leave-one-pack estimate. |
| E18 | A de-la-Vallée-Poussin bound for `R_i^2` and `(u_i')^2` implies the full weighted-tail compactness condition. | proved and independently factor-audited | Every fixed feature-time interval; exact identities reduce the two dangerous densities to one quarter of these kinetic energies, with state-set tightness supplied by the action theorem. | Propagation of the superlinear kinetic entropy from iid initialization is open. |
| E19 | Fixed-interval loss action yields superlinear kinetic entropy. | refuted as a deterministic implication | Exact on-manifold states have bounded norms/action but order-one kinetic atoms; state entropies can have zero derivative there. | A reachability-specific probabilistic no-condensation theorem is necessary. |
| E20 | The iid flow keeps `h=<H^2>` uniformly away from zero on every fixed feature horizon. | proved | Fixed `epsilon>0`; use `m'=8 epsilon^2 f/(alpha^2 beta^2)`, monotonicity of `f`, iid concentration of `m(0)` and `f(0)`, and Jensen. | A late contrary audit used incomplete hypotheses and is superseded by this exact identity. |
| E21 | The row tangent action has an exact endpoint identity bounded by `sqrt(2)||A_0||+T/4`. | proved | Coupled exact feature flow; it controls total action, not spatial or temporal equi-integrability. | Combine with a kinetic no-condensation estimate rather than treating it as `(DV)`. |
| E22 | Natural strong-Hilbert, graphon, single Banach algebra, current-law, fixed-`Lp`, and finite-grade source constructions satisfy the full contract. | refuted for those named subclasses | Each obstruction was independently audited with normalization and scope corrections. | Infinite graded/closable traffic or Wiener source remains open; no universal no-go follows. |

## Supersessions

None yet.

The pre-freeze draft used `n^{-1} Tr(dG dG^T)`; it was superseded by the
canonical `Tr(dG dG^T)` metric.  No evidence item depended on the draft.

The exact finite-width results were independently derived once before being
entered as proved and were then certified by a second isolated hostile
referee, including the metric factors, layer limits, feature velocity, and
an exact on-manifold spike construction.

The exact unresolved compactness condition can be stated as trajectory-level
weighted uniform integrability of
`beta^-2 Z^2 C^2` and `alpha^-1 H T^2`.  Equivalently for output
equicontinuity, one may prove uniform absolute continuity in time of their
integrals.  Neither ambient spike examples nor the capped numerical panel
settle reachability from iid initialization.

The study was user-paused after every running isolated agent had returned.
`PAUSE_STATE.md` is the canonical resume packet and supersedes ad hoc terminal
summaries; neither E6 nor E7 has been promoted.
