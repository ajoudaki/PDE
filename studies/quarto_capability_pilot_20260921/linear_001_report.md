# linear_001 migration report

- Source: frozen `docs/README.md`, lines 1–211.
- Candidate: exact ordered replay of 19 declared edits, retaining the excerpt's final blank line.
- Labels: all eight source headings receive terminal insertion-only section labels (`old: ""` at the original heading-end offset).
- Mathematics: the single display changes only `\[` / `\]` to `$$`; its payload is byte-identical.
- References converted: the existing `shared notation` link; the named linear and residual-particle benchmark chapters; `The continuous-depth chapter`; the named *Global nonlinear learning* chapter; and numbered sections C.4.5–C.4.8.
- Proposed targets: 16 new targets against the empty before-registry; eight are defined in this packet and eight are reserved in future source files.
- Unresolved or ambiguous references: none. Generic mentions such as “each chapter,” “the chapters,” “the chapter's admissible joint scaling,” “chapters listed below,” and the category list “a local theorem, a special-data theorem and a benchmark for a different architecture” do not identify one stable book destination. Milestone A–F and C-H1–C-H4 are explicitly planning labels, not section references.
- Mechanical check: PASS. The final checker run reported 0 errors, 8 defined targets, 8 reserved targets, and 9 reference occurrences; its artifacts are in `data/generated/quarto_capability_pilot_20260921/linear001-sol-repair/final-pass/`.
