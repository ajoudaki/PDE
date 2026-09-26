# Independent p4/p5 implementation check

**PASS: 130 checks, largest absolute discrepancy
`1.5543122344752192e-15`.** No implementation changes were needed. The tested
builder implements the frozen factors in P45_DERIVATION_ROUTE.md, including
the declared raw scales `24` and `120` and the population scalar contractions.

The checker is `p45_implementation_check.py`; complete observations,
tolerances and source hashes are saved in
`data/generated/gradient_flow_probe_dictionary_20260921/p45_implementation_check01/validation.json`.

This check used CPU float64, width 37 and initialization seeds 9 and 41.
It performed no training, trajectory integration or GPU work. The scope is
implementation correctness before the authorized GPU comparison, not
large-width conditioning, fitting success or approximation quality.

The expected new fields were evaluated directly from the independently
derived numerical-label equations (2), (7), (9), (14), and (17) of the route
report. The oracle does not call the builder's coefficient multiplication
or label-shifting helpers, and does not obtain its expected result by
rearranging the builder's returned columns. The actual initialized matrix
and its transpose enter every forward/adjoint query.

For each seed, tests used label pairs `(0,0)`, `(1,0)`, `(0,1)`, `(1,1)`,
`(1,-1)`, `(0.7,-1.3)`, `(-1.4,0.2)` and `(2.1,0.35)`. Contracting the
returned new columns against the corresponding homogeneous monomials,
then dividing by their declared factorial scales, reproduced both lower
quartic fields and both upper quintic fields.

Further checks verified:

- p4 raw tables are bit-for-bit identical to p3. p5 preserves every p3
  column unchanged and has the prescribed `(14,24)` dimensions.
- Population moments agree with an independent probabilists' Hermite
  calculation using explicit two-dimensional upper moment contractions.
  The builder's own 128/256-node discrepancy is
  `7.88385953742754e-11`, within its `1e-9` gate. As specified, this
  discrepancy is a quadrature diagnostic rather than a rigorous error bound.
- The initialized coefficient matrix equals `B2.T @ W0 @ B1 / n`; the
  represented dense matrix equals the corresponding two-sided filtered
  initialization. Read-in and the supplied nonzero finite random readout
  are retained exactly. The supplied initial arrays remain unchanged.
- Independent raw-Gram Cholesky normalization reproduces each returned
  basis at its prescribed p-dependent ridge, without column rescaling or
  rank deletion.
- At nontrivial perturbed states, a separately written predictor forms the
  represented dense middle matrix and agrees with engine predictions.
  Full-batch autograd agrees with the maintained gradient field in all
  three trainable blocks, using mobilities `(n,n,1)` for `(w,c,M)`.
  Eleven input samples and engine block size three exercise multiple blocks.

The finite carrier checks deliberately use the declared population
constants in the field formulas. Replacing them with empirical moments
would test a different construction. Passing does not assert that these
fields exactly reproduce finite-network Taylor coefficients, preserve the
initial dense function, or establish the unproved population regularity
needed to turn the formal higher-order expressions into strong-flow
Taylor expansions.

The independent route was completed before reading the new implementation.
After that, the specifically authorized inputs were `new_dictionary_p45.py`,
P45_PROTOCOL.md and the already assigned p3 builder/maintained engine.
No other study or p4/p5 implementation was consulted. Reproduction uses:

```text
/home/amir/miniconda3/bin/python studies/gradient_flow_probe_dictionary_20260921/p45_implementation_check.py --out <fresh-study-owned-output>
```
