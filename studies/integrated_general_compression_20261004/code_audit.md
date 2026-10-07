# Code audit: bounded integrated-result checks

2026-10-07. All code below was read statically before execution. It has
bounded local inputs, no credential/network use, and no intended file writes.
No dependency installation, training run or maintained API change was needed.

## Code map and scope

- `setup_integration_check.mjs`: read-only document validation; math-delimiter
  counts, environments, tags, anchors, local links and exact imported setup
  fragments. It is not a TeX parser or mathematical verifier.
- `cost_algebra_check.py`: deterministic small-array tests of jet actions,
  continuation compilation, harmonic normalization, selected metrics,
  Legendre prefix/factor execution, update-Gram action and inference cache.
- `../unseen_query_decoder_20261005/test_streamline_kernels.py`: exact-rational
  and integer tests of packed hashes, generator traversal, cached metric
  products, tiled sums and indexed pivot heaps. This is not a neural decoder
  implementation or fidelity experiment.

These checks have no train/test split or empirical baseline, so leakage,
hyperparameter fairness and statistical performance are not applicable.

## Executed evidence

Working directory for every command: `/home/amir/Codes/PDE`.

| Exact command | Exit | Result |
|---|---:|---|
| `node studies/integrated_general_compression_20261004/setup_integration_check.mjs` | 0 | No failures; 13,187 lines, 917 display pairs, 3,664 inline pairs, 443 tags, 342 anchors, 396 links. |
| `python3 -B studies/integrated_general_compression_20261004/cost_algebra_check.py` | 0 | PASS; maximum reported normalized error about `4.72e-15`, below `2e-11`. |
| `python3 -B studies/unseen_query_decoder_20261005/test_streamline_kernels.py` | 0 | All five tests pass. |

Environment: Node `v19.9.0`, Python `3.10.12`, NumPy `1.26.4`.
The numerical test seed is `20261006`; decoder-kernel cases are deterministic.

## Finding and interpretation

L8: The mechanical checker passes malformed `qquad` at RESULT lines 2659,
2673 and 2682 because its checks count delimiters and structures rather than
validating TeX commands. This is a coverage limitation, not evidence that the
checker fails its documented mechanical contract. Add a rendering/command
lint step if syntactic validity is to be claimed.

The executed tests support the finite execution identities only. They do
not establish concentration, cavity independence, finite-source coupling,
word-precision sufficiency, whole-trajectory approximation, floating-point
stability, practical runtime, or an optimal compression rate. Neither M1
nor M2 can be resolved by these tests.

## Version binding

- Checker SHA-256: `804017e24c0ed427c755687f53a83438bff00214a6040aa6f91962f1aa4680ea`.
- Cost algebra SHA-256: `d2cf4bdff31fb212c50c3dca30d1c2707f5e0b0594491eebb840f9d49b762128`.
- Decoder kernels SHA-256: `c3e7ae1f8567cb9872ee4ffeceb53dcac0b5d39add80a65df551525835e64619`.

The theorem and test files were not changed in this audit.
