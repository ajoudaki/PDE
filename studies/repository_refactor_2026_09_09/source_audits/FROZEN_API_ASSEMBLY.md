# Frozen quadratic API assembly and correction

The coordinator implemented the exact finite reduction proved in finite-dynamics Section 8.1 inside the existing finite_reductions module. The supplied feature second moment is fixed; the trained connector/readout mobilities are one and n; the physical loss is half the squared residual. No initialization, trajectory loop, experiment or population solver was added. Every evaluated formula follows from the unreduced raw connector/readout derivative, and simultaneous Euler preactivations follow by multiplication with the unchanged bottom feature.

Four new deterministic test methods check the raw coordinate gradients, both independent kernel blocks, metric energy, one simultaneous step and recomputed raw interpolation, degenerate states, array ownership, validation and representable ranges. All thirteen finite-reduction tests pass. Each earlier module definition and earlier test class remains AST-identical to caf975a; only the module introductory prose was extended. The previous finite-dynamics proof body remains byte-identical and the complete 613-line candidate occurs exactly once.

Both first-round full independent reviews A1 and B1 independently found a mixed-boolean validation discrepancy: NumPy coercion could turn a supplied bool into an ordinary integer or float before checking dtype. The original full code, tests and chapter are retained unchanged under reviews/ASSEMBLY2_FROZEN_R1_*. The corrected validator inspects the supplied elements through an object view and rejects Python/NumPy booleans before accepting the numeric conversion; provenance erased before the API receives an already numeric array is not reconstructed. Regression cases cover list/tuple inputs, both vector arguments, and both public functions. The thirteen tests pass after correction. A new complete nine-file packet, with no prior verdicts, was frozen for two fresh independent reviews.

The previous finite-dynamics introduction was clarified before the new freeze: the C2 global finite-GF proof is in Sections 1–4, while the separately scoped ReLU results in Section 9 keep their own solution convention and compactness claim. No proof statement was changed by this introductory clarification.

The new guide fragment supplies a runnable state/step example and the full argument/return contract. The numerical functions retain ordinary float64 rounding, underflow and intermediate-range restrictions; their finite evaluations do not certify a limit theorem. No generated scientific data is required.

```json
{
  "code/pde/finite_reductions.py": {
    "preserved_definitions": [
      "ReductionEvaluation",
      "LaxEvaluation",
      "_scalar",
      "_state",
      "_finite",
      "_field_copies",
      "_evaluation",
      "mixed_quadratic",
      "mixed_lax",
      "rms_quadratic"
    ],
    "new_definitions": [
      "FrozenQuadraticEvaluation",
      "_frozen_state",
      "frozen_quadratic",
      "frozen_quadratic_step"
    ]
  },
  "code/tests/test_finite_reductions.py": {
    "preserved_definitions": [
      "arrays",
      "shifted",
      "coordinate_shift",
      "finite_state",
      "normalized_output",
      "MixedReductionTests",
      "RMSReductionTests",
      "ReductionContractTests"
    ],
    "new_definitions": [
      "FrozenQuadraticTests"
    ]
  }
}
```
