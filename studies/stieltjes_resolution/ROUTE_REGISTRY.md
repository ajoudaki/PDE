# Resolution route registry

The common theorem contract is `PROOF_CONTRACT.md`.  Routes are separated by
mechanism, not by notation.  A route is promoted only by a proved lemma,
explicit construction, or exact counterexample mechanism.

| Route | Mechanism | Decisive result | Status |
|---|---|---|---|
| R-COMB | Nonlocal combinatorial total positivity and continued fractions | The exact Riordan production matrix has negative entries already at low order; Thorin positivity and its mass-one strengthening also have exact Hankel counterexamples | Closed as a canonical proof route |
| R-OPER | Analytic gradient geometry and positive resolvents | Exact Gauss--Newton/Ward identities were found, but the natural positive operators miss the moments; the trace-log candidate has a negative elementary coefficient | Blocked for canonical V1 |
| R-PROB | Probabilistic/free-probabilistic/Fock representation | A finite positive tree realizes the checked prefix, but the first primitive tree activity and third free cumulant are negative; the all-order construction is conditional on V1 | Blocked for canonical V1 |
| R-NEG | Exact canonical falsification and D13 certification | The exact Schur witness was isolated, but the best certified positive subtotal is only 38.7585% of the threshold and no admissible omitted-mass lemma closes the gap | Blocked for canonical V1 |
| R-GLOBAL | Extreme-Gaussian-tail/global identification | Candidate Gaussian population/DMFT equations exhibit tail and pole obstructions, but neither those equations nor a positive-time width-first bridge are proved for the canonical network | Blocked for canonical V3; no network-level no-closure theorem |
| R-AXIS | Theory-selected block-metric reduction | The boundary reduces exactly, and a full \(\beta=1\) Gaussian-program jet proves the same shifted determinant negative for every \(0\leq\alpha\leq1/100\); the unique six-moment transition is \(\alpha_*=0.017519225541486\ldots\) | **Complete interior disproof of U1; exact finite-prefix ray classification** |
| R-SHALLOW | Exact one-input boundary rescaling and characteristics | Positive scaling transfers the boundary witness to the conventional raw-square shallow model, while each neuron has an explicit Riccati characteristic | **Formal shallow Stieltjes claim disproved; characteristic compression retained** |

The decisive route is documented in `BLOCK_METRIC_RESOLUTION.md`; its exact
regenerating certificate is `block_metric_counterexample.py`.  The other
route failures are proof-mechanism obstructions, not evidence against the
still-open canonical sequence.
