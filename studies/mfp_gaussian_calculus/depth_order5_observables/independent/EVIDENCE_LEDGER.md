# Independent `Gamma_04` evidence ledger

## C-S1: exact norm derivative identity

- Statement: finite-width `Q_l^(4)` is
  `2 Gamma_04 + 8 Gamma_13 + 6 Gamma_22`.
- Claim rung: exact identity.
- Status: proved by finite-width Leibniz differentiation; two independently
  implemented finite-width jet oracles agree in 30 layer-cases with maximum
  scaled error `1.38e-15`.
- Evidence: `FINITE_WIDTH_AND_WIDTH_AUDIT.md`,
  `POST_FREEZE_EXACT_AUDIT.json`.
- Falsifier: a product-rule coefficient mismatch.

## C-S2: one-pass scalar closure

- Statement: after the audited `R3` backbone, `Gamma_04` is produced by one
  nearest-neighbour forward pass of fixed scalar dimension using only
  one-dimensional `M` atoms.
- Claim rung: exact construction conditional on the population peel.
- Status: algebraically audited.  The public projection is one post-R3
  forward pass with two dynamic scalars `(gamma04,a41)`; no minimality claim.
- Evidence: frozen recurrence SHA
  `e97a3f6afda6ae17d1be498ac79b308b64fc71e7fd94a1f343e0e28844762122`.
- Cross-check: zero atom discrepancies against the response-aware population
  compiler at every layer of `H=2,3,4`; zero discrepancies between the
  three-state and two-state schedules at `H=1,2,3,4`.
- Falsifier: residual Gaussian/response object or exact map discrepancy.

## C-S3: existing-node dictionary

- Statement: `Gamma_11=w`, `Gamma_02=q02`, `Gamma_22=q22`, and
  `Gamma_13=q13`.
- Claim rung: semantic identification of frozen recurrence coordinates.
- Status: algebraically audited with zero discrepancies at every layer of
  `H=2,3,4` under two separate distributive canonicalizers.

## C-S4: annealed identification

- Statement: the scalar head equals the fixed-depth annealed large-width
  limit under the stated regularity and uniform-integrability hypotheses.
- Claim rung: theorem-level bridge.
- Status: exact under the stated fixed-depth polynomial-smooth tensor-program
  and finite-`L^p` hypotheses; otherwise open until convergence in probability
  and the displayed uniform-integrability condition are separately proved.

## C-S5: nonpolynomial regression

- Statement: the preregistered normalized-sine finite-width intercept agrees
  with the frozen head.
- Claim rung: empirical.
- Status: empirically supported over the preregistered `H=2`, layer-2,
  normalized-sine panel.  The 2,550-network fit passed with `z=-1.851` and
  chi-square p-value `0.211`.
- Evidence: `NORMALIZED_SINE_EXPERIMENT.json` and the four raw `.npy` cells.

## C-S6: competing producer comparison

- Statement: independently frozen Route A and Route S define the same local
  head.
- Claim rung: algebraic audit.
- Status: proved by exact sparse-map comparison: `83/20/1` terms and zero
  discrepancies.
- Evidence: `POST_FREEZE_ROUTE_COMPARISON.json`.

## C-S7: hostile 82-term candidate

- Statement: the independently frozen 82-term candidate is a valid competing
  contraction.
- Claim rung: proposed witness.
- Status: falsified.  It aliases the new moving-four forward innovation with
  the inherited moving-three slot.  Exact differences are 31 `Gamma04`
  monomials and four `a41` monomials.
- Evidence: `POST_FREEZE_ROUTE_COMPARISON.json`.
