# Positive-time run integrity and audit

## Frozen source hashes

The following hashes were recorded before the first trajectory step and are
unchanged after the run:

```text
963eda26c32e7edac1990c9c4b9852c75c745d522aae9d7287e288ddd320cb94  empirical_redesign/POSITIVE_TIME_PROTOCOL.md
7986d92af29461f0939583cab1884ea7f34e06afe2dc7b2610a84dd68f505c46  empirical_redesign/run_positive_time_pair_median.py
84e3ffb8df31175caca4758fd3dd09602ef2a35bb77ba1cf12ee116b87d6602a  direct_loewner_prespecified/simulate_loewner.py
bc6d901c2ab55a09498675866ec9de342793949ed3010e3d190c95cd37b02ecc  direct_loewner_prespecified/corrected_clock_core.py
7a81b7a0aa6d43f11960fb38c7a67da1308c8f26a94ab4bb2eab4af1d2d06990  empirical_redesign/jet_control_variate.py
```

The same hashes are embedded in `results.json`.

## Primary output hashes

```text
8ea34d6747e16a4a012464de761103c0e462f45170c2422cc4eb29c00fd5be64  results.json
b58682f16abb815ed4d663d1a395d3053180b34cb6f5b5050dac9a4961f9565b  raw_width_128.npz
9b0c7cdcc84aa267879a7bb44885a0a6f5f0e9ca63e6cf0fc524d21599350a83  raw_width_256.npz
9c4ebcb05bc1b513cb70cd813040822acf1301cc5fe7e7cb3448722c9d0dcf2f  half_step_width_128.npz
7420c13c11b0ca997e6638894340b5868c8880ae9532ae764e56b4c502f65c3d  half_step_width_256.npz
32297d5fb91122be8e193c18b49ea0c3b104f25fe2626f33001d019565eaeb52  bootstrap_width_128.npz
58dee0f208572c8bd8ecbaca08838a9fcbd62bcce3c1999e042a35996ad8772a  bootstrap_width_256.npz
24f3added403f77d9118e208e6cb315fef119921856df82ee10cae3100d55eca  console.log
```

## Reproducibility and resource checks

- Both widths contain all 224 preregistered pairs and 61 primary time points.
- Both step-halving archives contain the first 16 pairs and 121 points.
- Regenerated fifth-order jets agree bit-for-bit with the frozen local-test
  archives (`max relative error = 0` at both widths).
- There were zero stopped trajectories at either width.
- Recorded peak resident memory was `159216 KiB` (about 155.5 MiB), below the
  frozen 8-GiB address-space cap.

## Interpretation audit

Every numerical and local gate passed.  The primary degree-three confirmation
score for matrix `A` was negative at both widths and its adjusted upper
bootstrap bound was negative.  It is **not** a protocol-level negative signal:
the degree-two and degree-four sensitivity scores are positive at both widths.
Matrix `B` is of order `1e-12`, with bootstrap intervals crossing zero and
mixed sensitivity signs.  Therefore the frozen classification
`loewner_inconclusive` is correct.
