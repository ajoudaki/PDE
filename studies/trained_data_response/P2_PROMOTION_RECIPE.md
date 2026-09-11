# Proposed C.4.7: standalone validation recipe

This packet proposes one appended section in docs/global_nonlinear.md and
seven exact navigation replacements across that chapter and docs/README.md.
P2_SECTION.md is the complete new scientific text. P2_PROPOSED_GUIDE.md
is the complete proposed guide. P2_EDITION_ANCILLARY.json specifies every
old/new replacement and all base hashes. The complete invoked established
proof units, notation and current guide are P2_PROMOTION_DEPENDENCIES.md.
P2_PROMOTION_MANIFEST.json freezes every applicable input. No verdict or
history is a scientific dependency.

From /home/amir/Codes/PDE, choose a fresh generated output path and run:

```sh
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/NEW_RUN
```

The runner verifies all frozen input hashes and seven exact dependency
excerpts. It invokes P2_EDITION_BUILD.py to make a docs-only edition under
NEW_RUN/edition/standalone/docs. The builder copies ten frozen established
Markdown documents, applies exactly the seven navigation replacements and
appends the frozen section. It verifies that reversing those operations
recovers every base byte, that the other eight documents are unchanged,
and that the affected and complete guide links/fragments resolve. Its
one explicit preexisting exclusion is the guide's ../code/README.md link,
because no maintained code is added or required by this proof-only edition.
External web URLs are preserved without retrieval; older chapter links are
outside this affected-link check.

The runner verifies that the assembled guide equals P2_PROPOSED_GUIDE.md.
It copies the three supplied deterministic scripts to standalone/validation,
and executes them there with empty PYTHONPATH, bytecode disabled and one
BLAS/OpenMP thread. They read no study, history, retained output or Git
file. Their fresh outputs go under the standalone data namespace. The
standalone artifact has no studies or .git directory.

The three checks are:

- P2_PROMOTION_TANGENT_CHECK.py: supplied nonzero-readout tangent identities,
  normalized unhalved loss metric, singular compatible semigroup identity,
  and an incompatible nilpotent negative control. It is byte-identical to
  the existing deterministic source used for the C.4.6 identities.
- P2_PROMOTION_REFERENCE_CHECK.py: exact rational outward bounds for the
  reference certificate contained in C.4.5.1. It is the same complete
  arithmetic algorithm, with no training integration.
- P2_PROMOTION_RADIAL_CHECK.py: one fixed supplied state with correlated and
  repeated inputs and conflicting labels. It checks the exact row-radial
  identity, saturation inequality, and loss dissipation independently by
  complex-step differentiation. The calculation is identical to the study
  radial check; only its output-path policy is delegated to this runner so
  it runs inside the standalone validation directory.

All scripts fail on a violated numerical or exact assertion and require
fresh output directories. The runner retains every command, working
directory, exit code, complete log and log hash in NEW_RUN/validation.json
and the named logs, including a failure record if a subprocess fails.
The edition report includes all original and final document hashes and
the exact inverse-preservation recipe. The final checks verify inputs
again. Python, NumPy and SciPy versions appear in the output records.

No optimizer trajectory, parameter sweep or empirical training claim is
part of this recipe. Algebra and document correspondence support the
scientific audit; these scripts do not verify the uniform source estimates
or certify a mathematical theorem by themselves. No established file is
changed. Promotion requires the independent gates and approval specified
by RESEARCH_WORKFLOW.md.
