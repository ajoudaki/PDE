# Independent CPU implementation check for new p6 and p7

The checker is `p7_implementation_check.py`. It evaluates the prescribed
frozen population formulas on two finite Gaussian matrix carriers. Its
scalar contractions remain deterministic population constants from the
independently checked Gaussian quadrature; finite matrix row averages
are used only for basis normalization and the finite compressed model.
No training or GPU computation is part of this check.

## Frozen check specification

The two CPU float64 cases have `(seed,width)=(19,61),(53,79)`. Both retain
a nonzero finite initialized readout. Scalar algebra-label inputs are
`(0,0),(1,0),(0,1),(1,1),(1,-1),(.7,-1.3),(-1.4,.2),(2.1,.35)`.
These inputs evaluate polynomial identities after the dictionary has
been constructed; they do not fit or select dictionary fields.

The direct evaluator independently implements the scalar formulas for
`P4,T,E,K5,T6,E6,K7,M,P` from P7_DERIVATION.md. It does not call the
builder's homogeneous-polynomial arithmetic. It expands every learned
operator action as a sum of scalar population pairings, uses the actual
matrix and transpose for initialized actions, and computes beta from a
separate one-dimensional Gaussian formula.

The complete T6 and K7 polynomials are compared directly against the
retained coefficient columns at each scalar-label pair. The p5 T and K5
polynomials are checked at the same inputs to audit the direct evaluator's
inherited pieces. The selected M and tau-P columns are checked using
independent eight-point complex Fourier extraction: for a homogeneous
polynomial of degree below eight, evaluation at `(1,exp(2*pi*i*k/8))`
and the discrete Fourier identity recover every coefficient without
aliasing. This is an algebra oracle only. The recovered M/P/T6/K7
coefficients are independently evaluated at the real scalar-label pairs
as a numerical validity check. The builder's complete internal M/P/T6/K7
coefficient arrays are also evaluated at every real scalar-label pair and
compared with the direct formulas.

The implementation checks also require:

- Exact dimensions `(14,28)` for p6 and `(26,46)` for p7.
- Every inherited p5 and p6 raw column preserved bit for bit.
- Prescribed `6!` and `7!` scales on the newly retained columns.
- Initial readin and nonzero readout preserved bit for bit, and the
  projected middle initialization evaluated independently.
- Raw Gram plus ridge normalized using independent NumPy Cholesky and
  linear solves.
- Predictions and all three moving-state gradient blocks compared with
  a separately constructed dense compressed model and automatic
  differentiation, on eleven inputs in blocks of three.
- Supplied initial arrays left untouched.

For arrays the default error is
`max(abs(actual-expected))/max(1,max(abs(expected)))`. Field and prediction
checks have gate `3e-11`; independent beta uses `2e-13`; realness of
Fourier coefficients uses `3e-12`; basis normalization uses `3e-8`; and
gradient checks use `3e-10`. Prefix and preserved-array tests require
zero error. These thresholds are frozen before running the complete
candidate. A failed check requires diagnosis, not threshold adjustment.

## Results

**PASS: 463 checks.** No candidate correction, failed scientific gate, or
threshold change was needed. The validation record is
`data/generated/gradient_flow_probe_dictionary_20260921/p7_implementation01/validation.json`.

| Check group | Maximum scaled error |
|---|---:|
| T6 direct/Fourier/internal coefficients | `3.079e-15` |
| K7 direct/Fourier/internal coefficients | `9.767e-15` |
| Complete M polynomial | `2.221e-15` |
| Complete P polynomial | `5.441e-15` |
| Selected M and tau-P raw coefficients | `3.401e-16` |
| Inherited p5/p6 prefixes | exactly zero |
| Independent ridge normalization | `1.654e-11` |
| All three gradient blocks | `4.441e-16` |
| Dense compressed predictions | `3.817e-17` |

The largest discrepancy came from the independently computed p7 upper
basis at seed 19: absolute error `6.762e-11`, scaled error `1.654e-11`,
against its frozen `3e-8` gate. The p7 upper regularized Gram condition
numbers were `6.948e9` and `2.560e9`; these relatively large numbers
reflect the prescribed raw derivative scales and were retained unchanged.
All computations used float64.

The frozen builder SHA256 is
`f4709f9c5287f125f17a637ed4e0c88cbad7125cd84fca3a54ad830afcf52a19`.
The producer confirmed that this source remained unchanged after the
independent check. The result records hashes of the checker, builder,
inherited builders, Gaussian contraction code, and derivation.

Runtime was `/home/amir/miniconda3/bin/python`, with PyTorch `2.9.0+cu130`
and NumPy `1.26.4`. The command was:

```
OPENBLAS_NUM_THREADS=1 /home/amir/miniconda3/bin/python \
  studies/gradient_flow_probe_dictionary_20260921/p7_implementation_check.py \
  --out data/generated/gradient_flow_probe_dictionary_20260921/p7_implementation01
```

The execution device was CPU despite the CUDA-capable PyTorch package.
There were no GPU operations or training runs. A prior import-only check
found that the default system Python did not contain PyTorch; the existing
Miniconda runtime was used without installing or modifying packages.

## Scope

This validates evaluation of the prescribed frozen fields and their
compressed CPU dynamics. It does not make population moments into
empirical finite-network identities, establish exact finite-network
Taylor matching, prove minimal Gaussian span dimensions, or test
training performance. Strict population regularity through time power
eight remains the separate limitation stated in P7_DERIVATION.md.
