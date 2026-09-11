# Review provenance and resolution

The coordinator has read the complete version-1 paired proof reports and
integration report, repaired truncated tool reads, and verified the frozen
scientific inputs and recorded check products. Reviewers were fresh isolated
agents, distinct from authors, assembler and selector; neither proof reviewer
received the other's findings or study history. The integration reviewer was
a separate fresh agent. Original packets and reports remain unchanged.

## Version 1

Candidate SHA256:
`53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456`.

| Full report | SHA256 | Verdict |
|---|---|---|
| review_v1_A.md | 099f635975af7537f8e8c6df2a99ba079325b7736d34a219f5ab6efa2580db8a | Proof PASS; optional TeX correction |
| review_v1_B.md | c2cdb4c157709bb01ac05fa47dab59c0b9d898b721586c2c7ca1ac660aa0f53e | Proof PASS; optional TeX and stale heading corrections |
| integration_v1.md | 357fbd494ad244eced8229a1bd9ad42688775db6487478e435406f4e6e9c2fb6 | BLOCKED, four required corrections |

The integration objections prevent version-1 acceptance, regardless of its
proof PASS reports. The following exact corrections are incorporated in a new
frozen candidate through `assemble_proposal_v2.py`:

| Objection | Resolution in version 2 |
|---|---|
| R1: invalid TeX control word `\\ler` | Restore `\\le r` in the local-radius inequality. |
| R2: hidden finite norm normalizations conflict with `docs/NOTATION.md` | Use ordinary Euclidean/Frobenius norms and explicit factors of `1/sqrt(n)` throughout the finite-existence argument. |
| R3: subsection depth, stale local numbering and cross-reference | Make C.4.8 a fourth-level heading, matching C.4.5--7; remove inherited local numbering and identify C.4.8.2 explicitly. |
| R4: middle-update explanation omitted residual and factor 2 | State the exact rank-one Frobenius identity separately, then bound the full update by `2 integral |r| (||Delta||_2/sqrt(n)) (||h||_2/sqrt(n))`. |

The coordinator checked the corrected inequalities directly from finite GF,
including `||h||_2/sqrt(n)<=1`, `||Delta||_2<=||c||_2`, the operator bound for
the first-layer update, and finite-time integration of the readout inequality.
The theorem, source-response estimate, statistical proof, limit order and
exceptional-event handling were not altered. The complete corrected inputs
nonetheless receive fresh paired reviews as well as a fresh integration review.

## Version 2

| Frozen input | SHA256 |
|---|---|
| proposal_C4_8_v2.md | 98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928 |
| promotion_edits_v2.json | 50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c |
| review_packet_v2.md | 4eb8fb821a7e87d6819afc1c2fd7e1716e09b7bd2333d83509ca5a02802fb996 |
| integration_packet_v2.md | b6ede822df001807c55ac017c7986de4f541a8fcb1e1fb1f7292d601fa477a4c |
| validate_proposal_v2.py | e54689af496ce014ec2cc793f34fbefe370f1571122b3f6447863f3b73c81940 |

Fresh reviewers `/root/review_v2_a`, `/root/review_v2_b` and
`/root/integration_v2` receive only their neutral assignments, frozen complete
inputs and required skills. No version-1 verdicts or corrections, author reports,
study README or each other's findings are supplied. Their complete reports
are pending. The neutral assignments record exact read coverage, author/selector
identities, all source hashes and separate owned scratch/output paths.

Standalone version-2 validation passed with Python 3.10.12. Report:
`data/generated/trained_prediction_sampling/standalone_v2/validation_report.json`,
SHA256 `a43fbd60d00c8891c62d289d1f3c1846722192781c1dde3118b40c7cf2483ec9`.
It verifies the exact unchanged dependency bytes, proposed edits and their inverse,
88 new equation tags, 67 explicit tag references, the new navigation anchor,
TeX control words, and independent isolated execution of the six Gaussian
identities and 748 exact Hoeffding assertions. This is not a whole-book proof,
old-link, exporter or unrelated-code audit. No training experiment was run.

The standalone proposed chapter has SHA256
`bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05`;
the proposed guide has SHA256
`5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f`.
Established book/code files remain unchanged. Explicit user approval of the
final reviewed package remains required before integration.
