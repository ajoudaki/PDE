# Final extension receipt — connected frozen-reference loader

**Complete; frozen for independent acceptance.** Exact freeze time, source hashes, and protected-file checks are in `FINAL_HASHES.json`. This receipt adds the explicitly authorized connected-reader fix to the completed three-consumer extension. Earlier receipts, including slice 1, remain unchanged.

## Bounded repository change

Only `studies/mfp_gaussian_calculus/depth_order5_scalar/audit/reference_maps.py` changed in this increment:

- **Line 19:** explicit retained root `data/historical/studies/mfp_gaussian_calculus`.
- **Lines 65–68:** `historical_reference_path(depth)` maps the original logical reference label into that retained root.
- **Lines 71–75:** the existing `load_reference(depth)` reads the resolved historical path. It has no source/fresh fallback and no output/write interface.

`REFERENCE` at lines 21–34 remains unchanged, including its source-relative logical labels and exact expected digests. `EXPECTED_COUNTS`, both accepted schemas, canonicalization, all validation after reading, and formula helpers are unchanged. The scalar audit's separate `selected_reference` therefore remains compatible.

The existing callers—`test_reference_maps`, `audit_primary_sector_independent`, `exact_controls`, and `audit_frozen_sector`—inherit the corrected location through the same loader API. None of these callers was edited. This is an immutable-artifact audit, not a fresh producer.

## Verification

**32/32 tiny tests pass: 15 original + 13 extension + 4 connected-loader tests.** Transcripts: `original-15.txt` and `extension-and-loader-17.txt`.

The new tests exercised the actual loader on all three retained maps, checked the exact physical read paths and pinned hashes/counts, and confirmed no file mutation. Synthetic tiny fixtures verify digest/schema/count refusal and missing-history failure without fallback. AST comparisons confirm unchanged logical labels, expected hashes/counts, formula helpers, and the complete validation body after the read.

The prior extension protection test now treats this one loader as the newly authorized change; its contract is tested separately. All **10 remaining protected files** and the **three consumers plus stable helper** remain byte-identical to the prior freeze. Original slice-1 receipts remain unchanged.

No coefficient generation, campaign, symbolic production audit, installation, seal refresh, historical-data write, Git operation, report reconstruction, or unrelated repository edit was performed. Reading and canonicalizing already-retained maps is the only real-map work; no coefficients were generated. Synthetic fixtures were confined to `/tmp` and removed automatically.

## Final boundary

No remaining blocker in this bounded connected-reader repair. The two retired consumer interfaces still refuse before imports; the scalar audit still exposes fresh/explicit/historical input selection; Hegel's hostile-audit guard and original seals remain unchanged. Earlier statements that the reference-loader source was unchanged are superseded only by this explicitly authorized one-file delta, not by an in-place edit to earlier receipts.
