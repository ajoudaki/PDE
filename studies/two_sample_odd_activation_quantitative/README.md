# Polynomial nonlinear mixing for two inputs

The assembled theorem in [PROOF.md](PROOF.md) gives the explicit sufficient
form theta_delta = c_poly delta^800 for the original odd two-input
population/GF/raw-GD theorem. The universal positive prefactor is defined
there using numerical constants. Three fresh independent complete-proof
reviews returned PASS at the unchanged mathematical hashes; see
[REVIEW_STATUS.md](REVIEW_STATUS.md) and
[REVIEW_CERTIFICATE.json](REVIEW_CERTIFICATE.json).

This is an asymptotic polynomial bound, not a practical or sharp
coefficient estimate. The proof does not establish theta of order delta^2.
The tracked prefactor satisfies log10(c_poly) approximately
-1004171.5712636513; its definition is exact in PROOF.md, and the
independent affine audit confirms this numerical evaluation. Thus the
improvement is in the asymptotic dependence on delta, not an established
usable coefficient for moderate separation.
The much milder restriction c delta^(7/4) already handles affine
comparison, endpoint fitting margin and nonaffinity; the conservative
exponent 800 includes the full nonlinear source-response proof.

Mathematical documents:

- [PROOF.md](PROOF.md): complete statement, coefficient formula,
  enlarged initialization and polynomial source-input certificate,
  assembly of the original global flow and finite-limit conclusions.
- [AFFINE_POLYNOMIAL_BOUNDS.md](AFFINE_POLYNOMIAL_BOUNDS.md): exact
  balance identities, logarithmic integrated curvature, polynomial
  comparison, absolute nonaffinity margin.
- [POLYNOMIAL_RESPONSE_LEMMA.md](POLYNOMIAL_RESPONSE_LEMMA.md):
  positive scaling of the coupled affine inverse, backward-row
  forcing conversion, and polynomial nonlinear response closure.
- [OLD_THRESHOLD_AND_NONAFFINITY.md](OLD_THRESHOLD_AND_NONAFFINITY.md):
  why the old chosen coefficient is superpolynomially small, plus
  independent regression and finite-array calculations.

[CONTRACT.md](CONTRACT.md) preserves the exact target and forbidden
substitutions. [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) distinguishes
the initial component results from the later assembled theorem.
[DEPENDENCY_HASHES.json](DEPENDENCY_HASHES.json) identifies the unchanged
previous proof and source files. Paths in that manifest are relative
to the parent mean_field_peeling directory.

The component notes preserve their original candidate and limited-scope
wording. Their review prerequisite has now been met for the assembled
theorem; the complete reports, rather than the preliminary reports,
record that assessment. The affine review also makes explicit the
backward-row duration and sample-basis factors already absorbed by C_B.

No experiment, optimizer change, external publication, or Git commit
was used. The older two-input proof remains unchanged.
