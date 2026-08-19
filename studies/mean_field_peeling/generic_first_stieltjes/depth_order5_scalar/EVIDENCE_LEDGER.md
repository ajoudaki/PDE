# Evidence ledger: scalar unit-Gram order-five depth recursion

This ledger separates full algebraic closure from the still-open strict
two-sweep representation requested in the research contract.

### S5-1: finite \(M\)-only state

- Statement: a fixed-dimensional deterministic scalar state, independent of
  \(H\), closes the unit-Gram order-five peel.
- Status: **proved with six chronological sweeps**.
- Evidence: 29 dynamic scalar coordinate types with dimensions
  `7/8/4/4/3/3`; all local maps are explicit \(M_\nu\)-polynomials.
- Qualification: a single-forward/single-backward compression is **open**.
  The exact dependency chain is F1/R1/F2/R2/F3/R3.  No minimality or no-go
  theorem is claimed.

### S5-2: explicit transitions

- Statement: every initialization, local transition, source, accumulator,
  and terminal expression is displayed in the contract alphabet.
- Status: **proved**.
- Evidence: `ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md` embeds all 38
  frozen local transition formulas.  `verify_canonical_report.py` compares
  them literally with the three frozen transition JSONs.

### S5-3: exact frozen-map equality

- Statement: exact distribution reproduces the frozen \(H=2,3,4\) unit maps.
- Status: **proved**.
- Evidence:

  | \(H\) | \(A\) terms/diffs | \(B\) terms/diffs | \(C\) terms/diffs |
  |---:|---:|---:|---:|
  | 2 | 3 / 0 | 46 / 0 | 974 / 0 |
  | 3 | 4 / 0 | 160 / 0 | 6,519 / 0 |
  | 4 | 5 / 0 | 350 / 0 | 17,641 / 0 |

- Post-freeze cross-route evidence: zero discrepancies for
  \(A,B,C,S_5,AC,Bm2,M2,Am3\) at \(H=1,2,3,4\).
- Provenance qualification: the two assemblers were independently written,
  but share the independently frozen Route-A moving local tables.  The main
  completion chain is one analytic derivation plus an independent exact map
  canonicalizer and hostile audit, not two independent local derivations.

### S5-4: lower-order projection and controls

- Statement: the same state gives \(A_H=\tau_H\), the Section 7.1 compact
  order-three recurrence, parity, and the required controls.
- Status: **proved in the stated scopes**.
- Evidence: exact transition projections; constant, normalized affine,
  normalized quadratic, and deep-linear substitutions; companion tagged
  unnormalized-quadratic audit; normalized-sine regression.
- Scope correction: \(x^2\) does not preserve unit forward Grams.  Its
  accepted unnormalized controls come from the companion layer-tagged map,
  not formal substitution into this unit quotient.

### S5-5: terminal derivative ceiling

- Statement: every terminal atom contains derivatives only through
  \(\phi^{(5)}\).
- Status: **proved**.
- Evidence: fail-fast Wick--Stein constructors, literal transition scan, and
  expanded \(H=2,3,4\) atom scan all report maximum derivative five.

### S5-6: annealed limit

- Statement: the algebraic recurrence equals
  \(\lim_n\mathbb E[D_n^k f_n]\), \(k=1,3,5\), at each fixed \(H\).
- Status: **theorem-level conditional**.
- Sufficient bridge: \(\phi\in C^\infty\), all derivatives of polynomial
  growth, and finite Tensor Program convergence in every finite \(L^p\); or
  convergence in probability plus
  \(\sup_n\mathbb E|D_n^k f_n|^{1+\epsilon}<\infty\) for \(k=1,3,5\).
- Excluded: growing depth/batch, positive-time convergence, all-orders series,
  and depth-uniform flattened-size bounds.

### S5-7: audit verdict

- Algebraic/full-contraction verdict: **pass**.
- Literal strict one-forward/one-backward schematic: **not achieved; open**.
- Exact artifacts: `primary/FULL_SCALAR_AUDIT.json`,
  `primary/FULL_INDEPENDENT_COMPARISON.json`, and the hostile audit ledger.
