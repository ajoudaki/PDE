# Revision v2 and review disposition

The original full v1 reports are preserved unchanged:

- [Scientific A](scientific_review_v1_a.md), SHA-256
  `bf9101c05ee509de7faf2851db55f738e21eeef6a34861207a73154ed2043b90`:
  NOT ACCEPTABLE AS WRITTEN; required correction R1.
- [Scientific B](scientific_review_v1_b.md), SHA-256
  `35c16b392928ced4b07d15ffb02163fb9cb381c284189fc536d33cec3e7a40b5`:
  PASS for its interpreted finite-cap scope.
- [Integration](integration_review_v1.md), SHA-256
  `784cdb2d937293f76047ef01481178726b2c616ffe486e518d4c81710194ae25`:
  PASS within its stated exact older read scope. Its disclosed reading overrun
  and authorized extension are retained in the original report and supplement.

Root read all three original reports completely, verified their hashes and
retained check evidence. The pair does not pass: one required correction
blocks acceptance regardless of the other reports.

R1 is a missing explicit hypothesis in the robust subfamily. NGL14 bounded
only the first N+1 coefficients of w while NG5 allowed infinite series. Thus
the displayed condition did not force the zero tail and membership of the
initial residual in E_N used later. Review A's N=0 example adds a nonzero
third harmonic within the global coefficient budget. This refutes those proof
premises for the literal larger set; it does not show the intended finite-cap
learning theorem false.

The only scientific difference in v2 is six lines after NGL14, explicitly
defining w as its sum from k=0 to N and setting every higher coefficient to
zero. This is the finite-cap robust family intended by the frozen study
contract and relevance disposition. The wider infinite-series approximation
and sampling theorems remain unchanged. All other proof text, constants,
source dependencies and reading-guide content are unchanged. No source or
review file in v1 was edited.

The corrected complete candidate is [candidate_addition_v2.md](candidate_addition_v2.md),
SHA-256 `b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d`.
Its [complete scientific manifest](scientific_manifest_v2.json) has SHA-256
`cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7`.
The proposed full guide remains
`d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c`.

Two new fresh isolated reviewers, scientific_review_v2_c and
scientific_review_v2_d, received the full v2 packet and neutral assignment,
without old packets, findings, verdicts or author discussion. They must each
read every scientific/dependency line again. A new fresh integration_review_v2
received the complete assembled edition and exact older interface ranges,
without any prior review. Old PASS reports are not reused for these gates.

Deterministic edition validation was rerun from the corrected frozen inputs:

```text
python3 studies/nonlinear_selection_generalization/validate_edition_v2.py data/generated/nonlinear_selection_generalization/edition_validation_v2_20260912_01
```

Exit zero, Python 3.10.12. Exact reference assertions, elementary algebra,
inverse-modulus checks, all 103 labels, new fragment and original-chapter-byte
preservation passed. Full generated record is `validation.json` in that run.
The assembled chapter hash is
`5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483`.
The [integration manifest](integration_manifest_v2.json) identifies the full
selected-file edition and its hashes. These deterministic checks do not
replace the new scientific or integration reviews. No training experiment
was run and no established file changed.
