# Proof-search approach registry

| Route | Core idea | Distinct bottleneck | Current state | Revisit trigger |
|---|---|---|---|---|
| A | Direct finite-width differential calculus and initialization law. | Projection and muP factors. | active | Independent factor audit. |
| B | Finite conditional-law / transport closure on fixed Gaussian marks. | First weighted-Wishart alignment has an almost-sure full Krylov orbit; tail class also degrades. | rejected for fixed finite response/overlap states | A non-scalar current operator that absorbs the whole action. |
| C | Fixed-source operator-valued closure. | Avoid encoding the full word hierarchy; prove compactness and readout continuity. | active, new canonical-source round | Concrete non-ultraproduct Gaussian row/column module. |
| D | Spike/alignment obstruction or canonical no-go. | A finite topology counterexample does not exhaust the closure class. | active, isolated | Formal exhaustion theorem. |
| E | Normalized-gradient energy and compactness route. | Kernel contains unbounded products despite bounded normalized features. | partial: Hilbert equicontinuity proved; fixed `psi_p` bootstrap refuted | Reachable weighted `L^{2+delta}` or lognormal envelope. |
| F | Conjugacy/invariant reduction induced by radial normalization. | `epsilon>0` breaks exact scale invariance and tangential motion remains. | queued | A finite invariant manifold or exact quotient. |
| G | Smooth cutoff, pointed diagonal-traffic limit, then cutoff removal. | The offered ultraproduct violates the contract; even at fixed cutoff the continuous-time passage needs an independent proof. Removal needs trajectory-level weighted UI. | conditional/formal, under audit | Canonical source plus uniform-in-cutoff reachable estimate. |
| H | Gaussian Fock/Malliavin source with current responses. | One response closes only one-shot integration by parts; recursive source reduction generates the full Gaussian jet. | first-response version rejected; canonical source round active | A finite invariant differential module or unreduced source action with a strong topology. |
| I | Reachable spike/barrier analysis from Gaussian extremes. | Exact feedback defeats the lone-row approximation under incoherence, but simultaneous adaptive packs remain uncontrolled. | active, new probability round | Prove weighted UI/temporal AC or positive-probability concentration. |
| J | Entropy/de-la-Vallée-Poussin Lyapunov control of weighted kernel tails. | Must close adaptive row/column commutators rather than only marginal moments. | active, isolated | A dimension-free superlinear tail functional. |

Routes that fail are not silently recycled: their valid lemmas are moved to the
ledger and any later reuse requires the listed trigger.

## Pause marker

User-paused on 21 August 2026 after all running agents closed normally.  No
route is currently executing.  Resume from routes J and C/G, using `(DV)` and
`(SRC)` as frozen gates in `PAUSE_STATE.md`; do not rerun rejected low-energy,
fresh-Gaussian, one-response, ultraproduct, or incomplete numerical routes.
