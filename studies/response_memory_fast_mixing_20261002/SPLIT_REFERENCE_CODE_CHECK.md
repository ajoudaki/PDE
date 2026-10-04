# Split reference kernel: scoped code check

**Verdict: PASS for the source-level split, normalization, indexing, mixer transpose, and reference-only dispatch.** The numerical verification is meaningfully discriminating. This verdict does not certify GPU execution, resource feasibility, campaign completion, or external launch controls.

Reviewed on 2026-10-02 under a narrow isolated assignment. Scientific inputs were only `fast_training.py`, `fast_training_split_reference.py`, `verify_split_reference.py`, and `POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md`. Required shared instructions and the canonical-notation and rigorous-math skills were applied. No study history, campaign outputs, other studies, or GPU were read or used. The producer was not edited.

## Exact operator and operation order

For a sample vector of length $n=32768=2m$, with $m=16384$, write $x=(a,b)$. Define the unnormalized Sylvester transform recursively by $S_1=(1)$ and

\[
S_{2m}=\begin{pmatrix}S_m&S_m\\S_m&-S_m\end{pmatrix},
\qquad H_n=n^{-1/2}S_n.
\]

The original kernel processes butterfly levels $0,\ldots,14$ in increasing order. At a level with `step = 1 << level`, a low-index coordinate becomes its old value plus its partner; a high-index coordinate becomes its partner minus its old value. Levels $0,\ldots,13$ never cross the two halves. Therefore the new first kernel computes precisely $S_m a$ and $S_m b$, without normalization. The second computes

\[
H_nx=n^{-1/2}(S_ma+S_mb,\;S_ma-S_mb).
\]

The high-half subtraction has the correct order. The final factor remains $n^{-1/2}$; neither half is normalized early. For the authorized float32 inputs, the intermediate buffer is float32 and introduces no new precision conversion. The arithmetic dependency order matches the original source. Actual compiled-GPU equality remains an execution check, which the supplied verifier explicitly performs against the direct butterfly.

The first launch has one program per contiguous half, giving two half-programs per sample. The second uses `j < x.numel() // 2`, `row = j // m`, and `col = j % m`. Each valid `j` writes precisely the low and high coordinates of the corresponding sample. These pairs are disjoint and cover the output. `contiguous()` makes the flattening valid for arbitrary leading batch dimensions in the exercised nonempty inputs.

The dispatcher selects the split only when `n == 32768`. The other branch and its kernel are textually unchanged from the original. The training entry point additionally requires the exact width, kind, seed list, compact output, TF32 setting, and step size specified in the amendment. The source diff contains no changes to mixer construction, its actions, the training equations, data selection, or trajectory observables.

## Signs, permutations, and adjoint

For a permutation array $p$, define $P_p x=x[p]$ on a sample column vector; its transpose is indexing by the inverse permutation. Let $D_{\rm left}$, $D_{\rm right}$, and $D_{\rm middle}$ denote the real diagonal matrices formed from the correspondingly named stored arrays. The unchanged forward method implements

\[
F=P_{\rm lp}D_{\rm left}H_nD_{\rm middle}P_{\rm perm}H_nD_{\rm right}P_{\rm rp}.
\]

Since $H_n^\top=H_n$, reversing the factors gives

\[
F^\top=P_{\rm rp}^\top D_{\rm right}H_nP_{\rm perm}^\top D_{\rm middle}H_nD_{\rm left}P_{\rm lp}^\top.
\]

This is exactly the supplied transpose method, using `li`, `inverse`, and `ri` in the required positions. In particular, `middle` stays before inverse indexing when reading the transpose code from input to output. The split does not move any sign, diagonal, or permutation operation.

## What the verifier distinguishes

The five random full-width samples are checked against a direct, increasing-level PyTorch butterfly using both `torch.equal` and a relative norm. This detects cross-half sign reversal, missing or extra normalization, swapped coordinates, and cross-row indexing defects. The involution check alone would not establish the intended transform, but it is supplemented by this direct action oracle.

The exact basis check includes the first coordinate, a low bit, the final low-half coordinate, the first high-half coordinate, and the final coordinate. Its independent parity formula tests boundary signs and scaling. These five basis vectors alone would not detect every permutation of middle bit positions; the full random-input direct comparison addresses that weakness. The lower-width check exercises a noncontiguous 16384-wide slice, with identical original/new kernels covering the remaining non-reference widths by source inspection.

Full mixer forward and transpose comparisons use the actual stored arrays. Their reference expressions mirror the intended factor ordering, while the separate bilinear adjoint identity detects an inconsistent inverse or backward ordering. TF32 is disabled for these checks. Every metric whose name contains `error` is required to be strictly below `3e-6`; the three exact comparisons must also be true. A NaN error fails the `<` gate.

## Independent CPU checks performed

Executed the actual three kernel bodies after AST extraction, removing only Triton decorators/type annotations and supplying NumPy implementations of their load/store, gather, indexing, and elementwise primitives. No study module or unassigned dependency was imported. Used NumPy RNG seed 912701, five float32 rows of width 32768, the verifier's five basis vectors, and additional shapes `(32768,)` and `(2, 3, 32768)`. Compared against an independently coded reshape-based butterfly. Also executed the actual mixer method bodies on an independent 32-dimensional real diagonal/permutation example and compared its transpose to a dense matrix.

| Check | Observed result |
| --- | --- |
| Split versus original kernel-body emulation | Bitwise equal |
| Split versus independent direct float32 butterfly | Bitwise equal |
| Explicit basis signs and magnitudes | Exact agreement |
| Additional leading-dimension shapes | Bitwise equal |
| Relative float64 transform discrepancy | `1.09984143100943e-7` |
| Relative involution discrepancy | `1.5796952368418715e-7` |
| Mixer transpose versus dense action, maximum absolute error | `8.881784197001252e-16` |
| Bilinear adjoint absolute error | `8.881784197001252e-16` |

Negative controls gave relative action errors `1.4127` for reversed cross-half subtraction, `0.99219` for an extra half normalization, and `1.2643` for reusing the first row. Replacing the inverse permutation by the forward permutation gave an absolute adjoint discrepancy `15.7436`. These checks validate the relevant error sensitivities, without claiming GPU compiler or performance validation.

## Explicit limits and dependencies

- `reuse_check.py` was outside the allowed input scope. Consequently its claimed float64 implementation and the provenance of its mixer arrays were not audited. The independent direct action and CPU checks above do not depend on it; certification of the verifier's specifically named NumPy-float64 oracle requires inspection of that dependency.
- GPU execution and verification outputs were outside scope. This report cannot assert that the frozen GPU verifier passed or that the new kernel fits the device resource limit.
- The producer does not itself consume the verifier's pass record. It retains a 1800-second campaign guard and accepts a device argument, whereas the amendment imposes tighter combined budgets and physical GPU1. Enforcement of preverification ordering, combined budgets, and device isolation therefore depends on external launch controls, which were not assigned for inspection. This is a concrete orchestration dependency, not a defect in the split transform.

## Reviewed source identities

Repository HEAD at check time: `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`. The reviewed files were untracked, so these SHA-256 values identify the checked versions:

| File | SHA-256 |
| --- | --- |
| `fast_training.py` | `7356bce354297abedd38c1db7b433d882d283885657ea2e39bfe521c238142a2` |
| `fast_training_split_reference.py` | `24265e260e1741b6771df2d551a16d834667d277a070539151cbbea37c12d4c1` |
| `verify_split_reference.py` | `24cf6eeab32c6afef0d372241720c22bcdc12771cffc957e21ce2468c5ae7b27` |
| `POPULATION_COST_SPLIT_REFERENCE_AMENDMENT.md` | `6aeeee9a296156aeb5bc5d34f969bbf2847aef1aff05dee5f2911c86356dbe09` |
