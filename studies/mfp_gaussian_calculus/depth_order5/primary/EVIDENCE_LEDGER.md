# Route S evidence ledger

### S-1: chronological fixed-depth compiler

- Statement: the order-five forward/backward chronology in
  `depth_population_jet.py` specializes at `H=2` to the audited primary
  order-five compiler.
- Claim-ladder rung: exact finite construction / algebraic audit.
- Status: exact-under-assumptions, atomwise tested.
- Scope and assumptions: arbitrary symbolic `Q0`; derivatives through five.
- Supporting evidence: exact expanded-map differences are zero for
  `(A,B,C)`, with tagged term counts `(3,50,1045)` and unit-quotient counts
  `(3,46,974)`.
- Contrary evidence: none observed.
- Dependencies: correctness of the frozen `H=2` reference map.
- Cheapest decisive resolver: repeat the literal exact-rational map diff.
- Concrete falsifier: any nonzero coefficient difference.
- Authoritative sources: `depth_population_jet.py` and the eventual frozen
  test report.

### S-2: explicit H=3 and H=4 normal forms

- Statement: Route S emits finite tagged and unit-Gram arithmetic formulas for
  `A,B,C` at depths three and four.
- Claim-ladder rung: exact finite construction.
- Status: open until artifacts are frozen.
- Dependencies: S-1 and feasible DAG construction/canonicalization.
- Cheapest decisive resolver: compile, canonicalize, hash, and replay-evaluate
  the artifacts.
- Concrete falsifier: an unresolved auxiliary Gaussian or failure to emit a
  finite formula.

### S-3: algebraic controls

- Statement: parity, derivative-order, constant, affine, linear, and quadratic
  controls pass for the frozen depth formulas.
- Claim-ladder rung: algebraic audit.
- Status: open.
- Dependencies: S-2 and an exact polynomial moment evaluator.
- Concrete falsifier: any exact mismatch with an independently derived control.

### S-4: smooth finite-width diagnostic

- Statement: a preregistered nonpolynomial finite-width experiment is
  statistically consistent with the population `A,B,C` values at `H=3,4`.
- Claim-ladder rung: empirical diagnostic only.
- Status: open; it cannot establish the annealed theorem.
- Dependencies: frozen experiment contract, independent finite-width Taylor
  differentiator, sampling validity gates.
- Concrete falsifier: a replicated discrepancy outside the frozen tolerance
  with all validity gates passing.

### S-5: annealed large-width identification

- Statement: the compiler output equals
  `lim_n E[D_n^k f_n]` under explicit activation regularity and UI hypotheses.
- Claim-ladder rung: theorem-level identification.
- Status: open until the exact theorem bridge and its hypotheses are audited
  for arbitrary fixed depth.
- Dependencies: fixed-order tensor-program convergence and expectation
  convergence via all-Lp convergence or a separate UI bound.
- Concrete falsifier: failure of a required theorem hypothesis or an
  unaccounted non-negligible equality partition.

