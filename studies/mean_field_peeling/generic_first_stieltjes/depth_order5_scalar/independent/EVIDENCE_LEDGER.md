# Evidence ledger: independent analytic route

### A-1: seven-scalar frozen-forward contraction

- Statement: the unit-Gram frozen forward jet through order five contracts to
  the seven deterministic scalars ((u,v,w,x,y,j,k)).
- Status: **exact-under-assumptions**.
- Evidence: literal Bell polynomials plus inverse-free one-coordinate
  Wick--Stein elimination in `forward_contraction.py`; frozen exact table
  `FROZEN_FORWARD_RECURRENCE.json`.
- Scope: the straight tensor family (V[p^5]), not the full (D^5f).
- Falsifier: a coefficient mismatch in an independently reconstructed local
  Gaussian contraction.

### A-2: eight-scalar frozen-gradient contraction

- Statement: four reverse innovation pairings and four feature coefficients,
  plus two terminal accumulators, close
  (U[Hp,p^3]) and (|T[p,p]|^2).
- Status: **algebraically audited**.
- Evidence: `reverse_contraction.py`,
  `FROZEN_REVERSE_RECURRENCE.json`, and
  `FROZEN_REVERSE_TRANSITIONS.md`.
- Exact liveness result: (e_{33}) is not needed.
- Post-freeze evidence: a second implementation reconstructed all exported
  sector roots through H=4 with zero exact discrepancies.
- Falsifier: a missed response branch in source13/source22 or a nonzero
  discrepancy under an independent local reconstruction.

### A-3: lower-order projection

- Statement: ((w,u,j)) and ((e_{11},c_{10})) reproduce the audited
  order-three forward and reverse recurrences.
- Status: **algebraically audited**.
- Evidence: exact sparse-polynomial equalities in
  `test_analytic_route.py`.

### A-4: derivative ceiling

- Statement: all emitted atoms use only derivatives through
  (phi^{(5)}).
- Status: **algebraically audited**.
- Evidence: construction rejects a generated sixth derivative; terminal
  atom-name scan passes.

### A-5: full (C_H) scalar recurrence

- Statement: the frozen moving-gradient passes close the former residual and
  hence all six families in the full (C_H).
- Status: **algebraically audited; exact fixed-depth scalar normal form**.
- Evidence: `FROZEN_MOVING_RECURRENCE.json`, `moving_contraction.py`, and
  `depth_assembler.py`, all frozen under `FROZEN_MANIFEST.json` before map
  comparison.  Exact rational comparisons give:

  | H | A terms/diffs | B terms/diffs | C terms/diffs |
  |---:|---:|---:|---:|
  | 2 | 3 / 0 | 46 / 0 | 974 / 0 |
  | 3 | 4 / 0 | 160 / 0 | 6519 / 0 |
  | 4 | 5 / 0 | 350 / 0 | 17641 / 0 |

- Exact terminal regrouping:

  \[
  C_H=2S_{5,H}+10AC+10Bm2+4M2+12Am3.
  \]

- Structural scope: the realization requires the chronological passes
  F1/R1/F2/R2/F3/R3.  The secondary forward tangent depends on an already
  differentiated reverse carrier, so this realization cannot be reordered
  into the requested single-forward/single-backward schematic.  This is not
  a universal minimality or no-go theorem.

### A-6: fixed-depth annealed identification

- Statement: a complete algebraic recurrence equals the annealed width
  limit at each separately fixed depth.
- Status: **theorem-level conditional**.
- Sufficient assumptions: fixed H; φ is C^5 with derivatives through order
  five of polynomial growth; the finite tensor program converges in
  probability; and, for some ε>0,
  `sup_n E|D_n^k f_n|^(1+ε)<∞` for k=1,3,5.  The latter is the explicit
  uniform-integrability bridge.  The stronger C-infinity/all-derivatives
  polynomial-growth package plus convergence in all finite Lp also suffices.

### A-7: controls and regression

- Statement: constant, affine, linear, normalized quadratic, and smooth
  nonpolynomial gates agree with the frozen unit maps.
- Status: **exact** for the first four classes; **empirical** for normalized
  sine.
- Evidence: exact moment substitutions in `FULL_SCALAR_RECURRENCE.md`; the
  normalized-sine preregistered finite-width regression used 7,700 networks
  and passes at H=3 and H=4.
- Scope correction: canonical unnormalized x^2 belongs to the companion
  layer-tagged/arbitrary-Gram recurrence.  It is not a specialization of the
  shared unit-Gram quotient.
