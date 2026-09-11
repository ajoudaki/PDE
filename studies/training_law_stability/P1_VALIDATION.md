# Standalone validation of proposed edition P1

The proof-only edition was assembled and checked from frozen inputs in
`data/generated/training_law_stability/promotion_validation_01/`, with no
repository imports or reads of live studies/book/code during execution.
The input snapshots, copied validator, exact command and complete result are
retained there. The source validator is `validate_promotion.py` in this study.

Executed from that run directory:

```text
python validate_promotion.py --inputs inputs --output edition
```

Python 3.10.12; exit code 0. The generated `edition/validation.json` records
the interpreter, all output hashes and each actual check. It verified all
seven frozen input hashes, exact assembly from the five declared scope edits
plus appended C.4, preservation of the remaining chapter text, balanced
mathematical environments, absence of study/runtime dependencies in the new
proof, all T/P/A equation references, and all newly introduced links/anchors.

The standalone edition includes the full proposed global-nonlinear chapter,
the proposed guide, unchanged notation, all necessary Gaussian and finite
dynamics excerpts, and `standalone_proof.md` combining the complete new proof
with every necessary dependency. The full proposed chapter SHA-256 is
`f48415a7017cd3b5bae48af29d3925263e139eda0b826ed95eb6ba546ac539d1`, matching
`P1_GLOBAL_EDITION.md`; the guide is
`95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e`.

There is no maintained API, executable guide example or empirical conclusion
in this addition. No training run, numerical parameter sweep or finite-width
rate test was performed. The unrelated book exporter has concurrent changes
and is outside this proof-only integration check. Unchanged guide links and
the remaining book chapters were not independently revalidated. The fresh
integration reviewer receives these precise limits and may independently
rerun the standalone validator.
