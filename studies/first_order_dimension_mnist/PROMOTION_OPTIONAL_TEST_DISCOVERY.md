# Integration-only optional dependency correction

The complete integration04 review found unconditional Torch imports break the
maintained NumPy-only test-discovery contract. Its original report and failure
are retained in the coordinating origin; no scientific objection was raised.

`PROMOTION_test_general_p1_optional.py` is the actual corrected test module for
integration. It guards only missing-Torch imports/setup, skips the two tensor
classes explicitly, lets all initialization/comparison tests run with NumPy,
and defers the helper's default dtype until invocation. Installed but broken
Torch imports still fail. All 16 test method bodies are literally unchanged;
the assembler verifies this with parsed source segments. All scientific modules,
proofs, test assertions/oracles, recipe sources and frozen_v4 remain unchanged.

Original test SHA256: `99de6d99818d022002e432021f0e86f14b263c382ea6caedb2f4c7351ecafb03`.
Adapter SHA256: `895ff58b2e348ec7733534c9e969d2cd1579e25b33cc3f3d08525d32aff37215`.

This is an interface/test-discovery repair under workflow Part 2.4, not a change
in scientific content or a substitute scientific review. The accepted frozen_v4
scientific pair remains attached to that identical scientific content; a new
complete independent integration review must verify the exact adapter and final
edition. The prior integration report cannot clear the corrected edition.
