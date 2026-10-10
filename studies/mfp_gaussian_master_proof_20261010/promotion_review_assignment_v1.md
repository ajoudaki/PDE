# Neutral complete scientific promotion review, candidate v1

Review the actual proposed finite Gaussian calculus theory, implementation,
examples and tests for mathematical and software correctness. Seek concrete
gaps and counterexamples. No outcome is presumed. This is one of two separate
complete adversarial reviews, not a divided math/code review.

Frozen run:
`/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v1/`.
The `edition/` contains the proposed standalone docs/code edition, while
`review_packet/` supplies the new theory and exact dependency excerpts. Check
`candidate_manifest.json`, `changed_manifest.json` and
`review_packet/manifest.json` before and after work. The manifest records the
authors/assemblers and selector; none may act as this reviewer.

Read AGENTS.md, the complete RESEARCH_WORKFLOW.md, the canonical-notation skill
and neural reference, and solve-math-rigorously. These are process instructions;
ordinary author startup does not apply to this isolated review. Do not read the
study README, author reports, selection report, internal or other review reports,
other studies, archived book, task history or author discussion. No inherited
conversation is supplied. Do not communicate with the other reviewer.

Read every line of:

- `review_packet/promotion_theory.qmd`, all four `dependency_*.qmd` excerpts,
  exact book/README patches, and bibliography addition. The excerpts contain
  complete relevant sections: Chapter 2 opening through exact polynomial
  Gaussian expectations, finite-jet comparison section, contained A.1–A.4
  scope, and Chapter 13 III.F.1–III.F.6. Their origin metadata records ranges
  and hashes. The bounded Gaussian law is an actual proof dependency; the
  old finite-jet and contained-scope passages also provide interface context.
- Every `required_edition_reads` file listed in the packet manifest, in full:
  all new implementation, tests, examples/producer and API guide; the complete
  code README, book index and notation contract; Quarto configuration,
  bibliography, package initialization and the existing rational Gaussian
  moment module. Existing `finite_network.py` is only a parent-package import
  dependency, not a claimed new numerical algorithm; it is available in the
  edition if needed to investigate import behavior.
- The primary-source attribution inputs `provenance_non_gaussian_tp_main.txt`
  and `provenance_appendices_H_I_J.txt`, with source hashes/URLs in
  `provenance_sources.json`. The candidate's moment argument is self-contained;
  it does not assume the external main theorem. Audit attribution and avoid
  imputing a priority claim absent from the candidate.
- The candidate mapping and assembly script, to check what bytes are proposed.
  The assembled Chapter 2 contains exactly the inserted theory and three
  scoped replacements; inspect their placement/context. The unread complement
  of the book is not assigned for a fresh whole-book proof audit.

Repair truncated reads. If a necessary scientific input is missing, report it
explicitly; do not fetch research from elsewhere. Required corrections block
acceptance. Record an objection even if you think the author can easily fix it.

Reconstruct the complete language and proof, including arbitrary named typed
matrix edges, Gaussian source identity, singular queries, uniform raw-entry
moments, zero-singleton cancellation, cutoff-uniform derivative profiles,
correlated matrix errors, causal scalar feedback, probability-to-expectation
passage, exact normalized gradients/updates and moving jets, and restricted
activation normal form. Check all worked formulas, labels, input geometry,
readout law and physical clock. Check that claims cover exactly admitted
operations and preserve the older broader-root/lower-regularity theorem.

Independently audit the complete code, producer, numerical semantics and tests.
Probe boundaries and errors, shared matrices, singular slots, physical versus
formal derivatives, frozen seeds, current ambient gradients versus pullbacks,
and symbolic covariance versus explicit geometry. The long quadratic kernel
polynomial in the guide is a produced formula, with disclosed shared-compiler
checks and independent finite AD checks; assess whether its evidence and the
algorithmic proof actually support it. Do not treat test success as a theorem.

Run relevant deterministic commands from the standalone edition with only its
`code/` on PYTHONPATH and bytecode disabled. Guide commands must not depend on
the live checkout, study outputs or history. Redirect your generated outputs
to your assigned fresh scratch directory beneath this run (or its own copied
standalone edition). Do not mutate frozen source files. No stochastic training
experiments, external writes, Git changes or live maintained edits are assigned.

Save a complete report to the separately assigned flat study-owned filename.
Include exact read coverage and unread complement, initial/final input hashes,
actual attacks/commands/results, separate theory/code/example verdicts,
unresolved objections, independence disclosure and completion evidence. Retain
your scripts/logs in your assigned scratch directory. Give a clear PASS only
if no required correction or missing input remains; otherwise report all
blocking issues. This scientific review does not replace integration review
or the final user approval gate.
