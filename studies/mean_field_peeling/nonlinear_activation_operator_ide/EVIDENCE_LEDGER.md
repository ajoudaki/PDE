# Evidence ledger: nonlinear activation selection

Status: resolved at C5 for arctangent, 21 August 2026.

| ID | Activation/family | Claim tested | Evidence type | Current verdict |
|---|---|---|---|---|
| E1 | identity | A compact operator/spectral IDE can be exact, restartable, and positively identified | existing theorem | positive comparator; excluded from nonlinear target |
| E2 | \(x^2\) | Finite pointed-traffic state \((A,u,q,e)\) and raw \(f,K\) formulas | exact finite algebra/formal lift | C0--C2 only |
| E3 | \(x^2\) | Natural \(L^2\oplus L^2\oplus\mathfrak S_1\) topology controls raw readouts | deterministic spike witnesses | refuted |
| E4 | \(x^2\) | Canonical Gaussian positive-time identification follows from average energy | tail/cavity audit | not established; dynamic LOO/UI gap |
| E5 | degree \(d\ge2\) polynomial | Superlinear coordinate growth avoids the quadratic tail mechanism | structural scaling comparison | disfavored; higher degree worsens the same mechanism |
| E6 | bounded smooth | Bounded forward fields remove superlinear raw-output tails | exact inequalities \(|\phi|,|\phi'|<\infty\) | promising but insufficient by itself |
| E7 | bounded smooth | Gaussian readout times \(\phi'(Z)\) is automatically a locally Lipschitz \(L^2\) map | multiplication audit | false on a generic \(L^2\) neighborhood; a canonical growth class or stronger argument is required |
| E8 | piecewise linear | Linear growth alone gives an easier proof | kink/switching audit | open; derivative discontinuities create a separate identification obligation |
| E9 | residual perturbation of identity | The proved linear theorem transfers for fixed nonzero perturbation | structural audit | open; must quantify the nonlinear multiplier and source functional calculus |
| E10 | leaky ReLU / hard-tanh / absolute value | A fixed derivative convention gives a unique finite-width flow through every kink | explicit two-neuron attracting/repelling switching construction | refuted; positive-probability regular states hit noncontinuable or nonunique switch states |
| E11 | \(x+\lambda\tanh x\) | Small fixed \(\lambda\ne0\) restores the identity theorem's bare-\(L^2\) local Lipschitz proof | unbounded Gaussian multiplier witness | refuted for that proof route; the Lipschitz quotient grows like \(|\lambda|M\) on \(|A|\sim M\) |
| E12 | strictly monotone \(\phi\) | The input-gradient multiplier is intrinsic | exact conjugacy \(r=\int^u1/\phi'\) | refuted: whenever the conjugacy is global, \(r'=G^*B\) exactly |
| E13 | tanh | Natural-coordinate contract plus bounded forward fields | exact algebra | viable, but \(r_0=(u+\sinh u\cosh u)/2\) has a transformed Gaussian tail |
| E14 | arctan | Natural-coordinate contract plus bounded forward fields and polynomial transformed seed | exact algebra and finite numerical identity test | selected winner; C0 passed |
| E15 | arctan | Finite identity \(f'=K\) in the transformed state | direct differentiation and random finite-width central differences | passed |
| E16 | arctan | One immutable two-sided Ginibre action exists and retains all \(G/G^*\) memory | \(\mathrm{NETSOR}^{\mathsf T+}\) finite-program theorem, countable program completion, Gaussian spectral-norm bound | C1 passed |
| E17 | arctan | The finite-field operator IDE is autonomous, global, and unique in a restart-stable class | cutoff Picard, Gaussian cutoff comparison, Osgood audit | C2--C3 passed |
| E18 | arctan | The raw kernel survives the width limit without coordinate condensation | fixed-mesh \(2+\varepsilon\) program moments, dimension-free Euler approximation, square-tail transfer in probability, then truncation for \(c(r)^2Q^2\) | passed after post-selection repair; the earlier direct Hölder mesh step is superseded |
| E19 | arctan | Canonical iid trajectories develop a quadratic-style tail boundary layer or adaptive-column spike | isolated extreme-coordinate/cavity attacks | no counterexample; mechanisms excluded on fixed horizons |
| E20 | arctan | Compact-time \(f,K\), residual, and loss are identified by the IDE | cutoff/mesh/source/clock theorem plus three fresh repair audits | C4--C5 passed |
| E21 | tanh / softsign | Arctan is the only viable nonlinear activation | structural comparison | false and not claimed; both are co-competitors, but neither has a cleaner combined contract/convergence proof |
| E22 | arctan source | A static two-sided Gaussian action is only an ultralimit or a hidden time-history | independent primary-source and projective-consistency audit of fixed `NETSOR^{T+}` programs | refuted; one countable pretrajectory source and its bounded adjoint action suffice |
| E23 | arctan kernel | A fixed-mesh high moment must remain uniform as the mesh shrinks | hostile quantifier audit | false; one auxiliary mesh proves continuous-trajectory square-tail tightness, after which a separate truncation argument removes the comparison mesh |
| E24 | arctan contract | A growing rank decomposition of \(q(t)\) is a forbidden growing-in-time state | independent extensional Markov audit | refuted; only the current trace-class operator is queried, on a phase space fixed at time zero |
| E25 | arctan tails | An adaptive rare row/column can produce an \(O(1)\) kernel layer despite bounded features | clean-room extreme-coordinate and square-tail audit | refuted on canonical-iid compact horizons by operator bounds, Gaussian cutoff stability, and fixed-mesh square-tail transfer |
| E26 | arctan theorem | The repaired ingredients leave a hidden circularity in source, mesh, cutoff, clock, or restart arguments | complete independent proof reconstruction | no; reconstruction passed with the ordered limits \(n\to\infty\), then mesh removal, then cutoff removal |

## Closed decision

Arctangent reaches C5.  The decisive mechanism is the combination of bounded
forward features, the cubic natural coordinate, a static two-sided action
source, Gaussian-tail cutoff removal, and fixed-program moment convergence.
The exchangeable/cavity route was retained only as an audit: by itself it
left an unproved low-influence estimate for Gaussian readouts and introduced
two-time response measures, so it is neither used nor needed in the final
theorem.
