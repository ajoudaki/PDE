# Standalone validation of proposed edition P2

The proof-only edition was assembled from frozen inputs in
`data/generated/training_law_stability/promotion_validation_02/`, without
repository imports or live study/book/code reads during execution. The input
snapshots, copied validator, exact command and full result are retained there.
The source validator is `validate_promotion_p2.py` in this study.

Executed from that run directory:

```text
python validate_promotion_p2.py --inputs inputs --output edition
```

Python 3.10.12; exit code 0. The final `edition/validation.json` records the
interpreter, output hashes and actual checks. These cover the seven frozen
input hashes, exact assembly of five scope edits plus C.4, preservation of the
remaining chapter, mathematical environments, T/P/A reference membership,
new links/anchors and absence of study/runtime dependencies in the addition.
They do not mechanically verify mathematical correctness or the notation
contract; those require complete reading.

The output includes the complete proposed chapter and guide, unchanged
notation, every necessary Gaussian/finite-dynamics dependency excerpt, and
`standalone_proof.md` containing the new proof and all its dependencies.
The chapter SHA-256 is
`1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9`;
the guide is
`95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e`;
the standalone proof is
`3ed9a24257bb4af2106dec9f1e52ac46483b8e02f0c2b05dfd06756c0a7d3682`.

No maintained API, executable guide example or empirical conclusion is added.
No training, parameter sweep or finite-width rate test was run. Unchanged
guide links, the remaining book complement and the concurrently edited book
exporter are outside this proof-only check. A fresh independent integration
reviewer receives the complete new scientific material, necessary older scope,
frozen baselines and validator, and independently reruns into fresh scratch.
