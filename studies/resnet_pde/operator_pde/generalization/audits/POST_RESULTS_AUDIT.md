# Independent post-results audits

Three independent audit tracks were run after the processed summary existed.

## Statistical and decision audit

Using only the frozen protocol, analysis plan, processed summary, and CSVs,
the auditor recomputed:

- the 14-case inventory and preregistered final-reference tier;
- every UCB and LCB from the joint critical values;
- every Gram-only UCB;
- strong-transfer, near-original, and material-counterexample decisions;
- numerical-gate and plateau aggregation.

There were zero inconsistencies. The correct broad verdict is
`boundary_or_unresolved`.

The central reason is statistical: the simultaneous upper critical increment,
0.0594006, already exceeds the 0.05 equivalence margin. Every observed error is
below 0.05, but no case can be certified under the global UCB rule. No material
counterexample is established.

## Scientific-interpretation audit

The auditor found strong descriptive transfer but rejected a blanket claim.

- Observed errors across all 14 cases are 0.95–4.14% for Gram motion,
  0.74–1.83% for outputs, and 0.31–1.97% for loss.
- All cases are nonlazy, and PDE/dense feature-motion ratios are 0.977–1.023.
- Labels and standalone activation changes are the cleanest no-retuning
  evidence.
- Six cases remain numerically unresolved and four fail the frozen
  two-window plateau rule.
- Only B0 and Y1 directly test the current narrow conjecture; the remaining
  cases are extension evidence.

## Release and provenance audit

The auditor reran full evidence verification. All 50 tests, all 32 frozen
source hashes, 56 PDE-seal entries, 46 dense archive hashes, and eight
processed-output hashes passed.

The original frozen README and reproduction driver predated two execution-only
compatibility wrappers and therefore did not provide a working clean rerun.
The compact release addresses this without rewriting frozen science:

- `RELEASE_README.md` becomes the archive's opening README;
- `protocol/reproduce_generalization_postfreeze.py` is the supported driver;
- `protocol/seal_dense_verified.py` verifies the historical execution wrapper
  before invoking it;
- `RELEASE_PROVENANCE.json` binds both amendment pairs, all three stage seals,
  the frozen manifest, processed summary, final report, and reproduction
  entrypoint;
- the archive-wide `SHA256SUMS.txt` and `verify_release.py` validate every
  included file.

Code inspection found no scientific effect from either amendment. They provide
redundant metadata/seed aliases and Python 3.12 module registration while
retaining exact case, array-shape, stored-seed, schedule, configuration-hash,
archive-seal, metric, bootstrap, and decision validation.

## Limits of the audits

- Processed-result audits do not independently recreate the raw trajectories.
- A release-level provenance record cannot retroactively prove chronology; it
  binds the records and code that assert and implement it.
- Requirements pin Python and the three numerical packages used by the study,
  but the release is not a hermetic container or byte-identical BLAS image.
- Finite-network bootstrap uncertainty does not include PDE truncation bias or
  finite width/depth bias.
