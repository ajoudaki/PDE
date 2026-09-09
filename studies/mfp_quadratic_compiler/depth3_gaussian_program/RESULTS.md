# Depth-3 raw-quadratic jet through order nine

## Outcome

The nested detransposition method remains efficient after adding a third
hidden layer.  For the model and scaling frozen in `PROTOCOL.md`, the exact
width-first feature jet is

| (r) | (F^{(r)}(0)) |
|---:|---:|
| 0 | 0 |
| 1 | 14,175 |
| 2 | 0 |
| 3 | 139,445,032,896 |
| 4 | 0 |
| 5 | 4,298,284,752,832,899,360 |
| 6 | 0 |
| 7 | 272,967,464,957,028,310,013,451,264 |
| 8 | 0 |
| 9 | 29,466,555,372,596,241,677,766,026,853,605,376 |

The seventh- and ninth-order values are new relative to the frozen controls.

## Validation outcome

All prospective gates passed:

1. The accepted raw-quadratic depth-3 values at orders one, three, and five
   were reproduced exactly.
2. Orders (0,2,4,6,8) vanished exactly, not numerically.
3. The ordinary-Taylor assembler and the separately written
   derivative-normalized/binomial assembler agreed on every output through
   order nine.
4. Every output rational had denominator one.
5. The first-order block decomposition is
   (2187+2916+3888+5184=14,175) for the (A,V,W,u) blocks.

The second assembler is an independent check of coefficient normalization,
Volterra integration weights, and product combinatorics.  It shares the same
derived Gaussian-program/detransposition identities, so this is not described
as a second independent proof of the width-limit theorem.

## Efficiency evidence

The timed dual-route command was

```text
/usr/bin/time -v python3 depth3_exact_jet.py --max-order 9 --route both --json
```

On the recorded run:

| route | wall time inside engine |
|---|---:|
| ordinary Taylor coefficients | 16.626 s |
| derivative-normalized coefficients | 16.434 s |

The combined process took 33.11 s and had maximum resident memory 30,848 KiB.
At order nine, the largest stored scalar polynomial was (B_{2,9}), with 579
monomials.  The middle-law Wick cache held 37,219 moments.  This is comfortably
inside the prospective 10-minute/4-GiB per-route boundary and is several
orders of magnitude smaller than an explicit derivative-forest expansion.

This establishes practical efficiency for this depth and order.  It is not
an asymptotic complexity guarantee for arbitrary depth or arbitrary order.

## Reproducibility and provenance

- Prospective protocol SHA-256:
  `f24009b2c122737d6f671b8f065d114d3dad49c32404e08db2ec2300246868c6`
- Derivation SHA-256:
  `3728caf148de328b0a5e2b725faca6bfaaf27a61e04b465e4f5352759505659d`
- Exact engine SHA-256:
  `2f053874429f02c4c2830fceadc13d688e5962d85503741f76c40a98ef380f0e`
- Fast-test SHA-256:
  `3789f00a02f117733fcf6490b787ee2012377cfe679f6adf4d3a2f69d7d40d65`

The protocol hash was recorded before the new seventh- and ninth-order
coefficients were computed.  Machine-readable results are in
`results_order9.json`.

The fast regression suite runs both exact routes through the accepted
order-five controls:

```text
python3 test_depth3_exact_jet.py
...
Ran 3 tests in 0.365s
OK
```

## Claim boundary

These are exact formal derivatives of the stated width-first mean-field
feature trajectory at (t=0).  The computation does not prove a positive-time
limit, an all-order formula, an all-depth bound, or a Stieltjes property.
