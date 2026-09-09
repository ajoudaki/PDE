# Evidence ledger: near-identity OMFP

Date: 25 August 2026.

| ID | Claim | Status | Evidence | Remaining bridge |
|---|---|---|---|---|
| NI1 | RMS normalization is explicit and stays in \([3/4,5/4]\) when \(|\alpha|R\le1/4\) | proved | `CUBIC_OPENNESS.md` §1; `route_audit.md` §2 | none |
| NI2 | The exact cubic invariant is Lipschitz in amplitude with a terminating activation-only constant | proved and independently audited | `CUBIC_OPENNESS.md`; cubic theorem cited there; independent numeric/algebra audit | none |
| NI3 | The nonlinear class is genuine at every nonzero amplitude if \(\varphi''\not\equiv0\) | proved | \(\psi''=\alpha\varphi''/s_\alpha\) | none |
| NI4 | The ambient \(C^2(L^2,L^2)\) Nemytskii/Frechet seminorm is unavailable and jumps at identity | proved | spike theorem in `route_audit.md` §4 and `AUDITED_SYNTHESIS.md` §4.1 | none |
| NI5 | Fixed-horizon continuity/analyticity does not imply a common nonlinear radius | proved as a logical no-go | `route_audit.md` §3; `AUDITED_SYNTHESIS.md` §4.2 | none |
| NI5a | The analytic curvature energy \(\mathcal E_\rho(\psi)=\sum_{r\ge2}\rho^r\|\psi^{(r)}\|_\infty/r!\) is explicitly \(O(|\alpha|)\) for Bernstein residuals | proved | `AUDITED_SYNTHESIS.md` (5.1a)--(5.1b) | it controls local vertices, not yet aggregate response trees |
| NI6 | Amplitude order \(k\) is algebraically triangular around identity | proved coefficientwise at each fixed finite schedule and fixed finite marked cylindrical expression; finite order under finite smoothness, all formal orders under a Bernstein envelope | `route_analytic.md` §3; `AUDITED_SYNTHESIS.md` §5 | all-source marked-resolvent norm |
| NI7 | Graded Gaussian product norm closes Holder products | proved | `route_analytic.md` Lemma 4.1 | degree-collapse expectations |
| NI8 | A finite-chaos, continuous, at-most-linear activation must be affine | proved | `FOURIER_SUBCLASS_SUPPLEMENT.md` Theorem 3.1 | none |
| NI9 | Finite Fourier regularity gives an exact finite response closure | falsified | `FOURIER_SUBCLASS_SUPPLEMENT.md` §§4--7 | requires all-source-order scale |
| NI10 | `route_volterra.md` Lemma 7.1 proves the fixed-order marked resolvent | rejected by two independent audits | `FOURIER_SUBCLASS_SUPPLEMENT.md` §12; analytic-agent audit | second and higher source marks; source-row bound |
| NI11 | A fixed nonlinear \(L=2\) interval satisfies the uniform \(t^4h^5\) remainder | open | `AUDITED_SYNTHESIS.md` §8 gives FRC2 plus a domination compiler as a sufficient conjectural proof program | factorial response-contraction and domination theorems |
| NI12 | The same uniform nonlinear result holds at \(L=3\) | open | `route_analytic.md` §9; `AUDITED_SYNTHESIS.md` §9 | \(\mathrm{FRC}_2\), then alternating-connector transfer |
| NI13 | The exact local fifth coefficient \([h^5]\{F_{2t,L}(h)-F_{t,L}(2h)\}\) is degree at most four in \(t\), for every admissible activation and fixed depth | proved and independently audited | `FIFTH_JET_POLYNOMIAL_THEOREM.md`; `FIFTH_JET_POLYNOMIAL_INDEPENDENT_AUDIT.md`; `ORDER5_WIDTH_FIRST_ARTIFACT_AUDIT.md` | none at the jet level; does not imply NI11 or NI12 |
| NI14 | The normalized genuine nonlinear class \(0<|\alpha|R\le1/4\) has the shared bound \(|[h^5]\Delta_{t,L}|\le(227/180)4^{E_{L,5}}t^4\) | proved | fifth-jet theorem §6 and Newton-envelope audit | none at the jet level |

## Supersession note

The positive fixed-amplitude-order closure claimed in `route_volterra.md`
is superseded by the audit in
`FOURIER_SUBCLASS_SUPPLEMENT.md` §12.  In particular, equations
(7.17)--(7.18) of that route do not establish their claimed response-row
estimate, and its one-source ledger is not closed under another aggregate
adjoint action.
