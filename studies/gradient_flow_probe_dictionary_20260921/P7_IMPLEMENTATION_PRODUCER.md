# p7 implementation producer record

The frozen builder `new_dictionary_p7.py` implements the independently
derived full-time candidate in `P7_DERIVATION.md`. Its SHA256 is
`f4709f9c5287f125f17a637ed4e0c88cbad7125cd84fca3a54ad830afcf52a19`.
The candidate derivation was not modified after the independent oracle
froze its input hash.

The callable API is `raw_features(initial,p)` and
`build(initial,p,block_size=512,forward_mode='auto')`, for p=6 or p=7.
The old p5 builder supplies the unchanged raw prefix. The p6 list appends
four upper M columns. The p7 list then appends twelve lower T6 columns,
two upper tau P columns, and sixteen upper K7 columns, giving `(26,46)`.
All six feedback columns are retained in addition to the highest label
degree fields. The prescribed ridge is `1/[1024(p+1)^2]`; the initial
middle projection and all maintained engine calls follow the old builder.

Population contractions come from the frozen `p7_gaussian_check.py` API.
The builder checks the 192/256-node discrepancy and the beta symmetry
identities, then projects beta onto its exact population parity/swap
structure by averaging the two equivalent entries of each type. No
empirical task contractions or task labels enter the feature construction.
The actual finite initialized matrix and its transpose evaluate every
required query. Initial random readout is retained by `build`.

Producer smoke evidence is
`data/generated/gradient_flow_probe_dictionary_20260921/p7_derivation01/builder_cpu_smoke.json`.
At CPU float64 width64, seed7321, raw shapes were `(64,26)` and `(64,46)`;
both p5 and p6 prefixes were bitwise equal, lower composition discrepancy
was `3.47e-17`, and sextic divisibility error was exactly zero. The maximum
Gaussian quadrature discrepancy was `4.92257e-12`. The lower/upper ridge
conditions were approximately `3.25e5` and `1.52e9`, below the existing
`1e10` gate. This producer check does not replace independent validation.

The exact symbolic producer check `p7_symbolic_check.py` separately
verified the formal K3/M/P ranks `8,12,14`, the fixed pivots and exact
reconstruction identities. Its result is
`data/generated/gradient_flow_probe_dictionary_20260921/p7_derivation01/symbolic_check.json`.
It uses exact rational arithmetic, with no numerical label fitting.

The independent finite oracle reported complete bivariate-coefficient
agreement through the eighth middle-weight power with maximum discrepancy
`1.94e-16`. The separate implementation checker reported 463 CPU checks
passing, with maximum scaled discrepancy `1.654e-11`, including scalar
formula evaluation, independent coefficient extraction, exact prefixes,
basis normalization, predictions and all three parameter velocities.
Those checks retain their independently owned reports and raw evidence.
No builder change followed either validation.

This is study-only implementation and internal validation. There is no
promotion, population regularity theorem, minimal Gaussian-span theorem,
or training-performance conclusion in this producer record.
