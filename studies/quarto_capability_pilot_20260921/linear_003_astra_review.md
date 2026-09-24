# Packet 003 independent preservation audit

**PASS — formatting preservation, partial edition.** Reviewed 2026-09-21.
This verdict applies to the final frozen packet and the actual
`linear003-render-final02` output, not either provisional preview.

Coverage was 100% of frozen `docs/README.md:497–742`, the complete candidate,
all 39 edits (10 labels, 29 references), all 21 initial target proposals,
and the original heading/opening context of all 18 distinct reference
destinations. Prose, qualifications, heading levels/order, code-form mathematics,
the eight-row/two-column chapter table, and all four external paper captions
and URLs survive. Existing links, raw numbered references and explicit named
chapter references were reviewed for omissions. The named linear,
continuous-depth and finite-controls chapters are linked; generic chapter
language and roadmap milestone labels appropriately remain prose. No
mathematical reproof or literature-claim audit was performed.

The initial check had only the declared prefix-continuity error. I subsequently
verified the actual packet-002 acceptance receipt against the final before-state,
not a predicted acceptance. The rebase changed only registry/progress and
removed two proposals identical to accepted objects:
`sec-docs-gaussian-calculus-l1` and `sec-docs-global-nonlinear-l19884`.
The candidate and edits are byte-identical to those fully reviewed. The final
copied `validate_packet(..., repo_root=Path('/home/amir/Codes/PDE'))` passes,
with 19 proposals, 21 defined labels and 26 reservations. All 24 final input
manifest hashes and 15 actual-render input hashes match. Assembly is exactly
the accepted 001 and 002 bytes followed by this candidate, covering lines 1–742.

The copied checker’s 17 tests pass. Three bounded packet mutations—deleting a
table qualification, changing an external paper version, and dropping a named
chapter link—were independently rejected. These checks supplement the full
source/reference reading; they do not establish semantic correctness alone.

HTML, PDF and exported LaTeX completed successfully. I read the renderer,
configuration, format-only filter, its explicit print-layout amendment, the
actual three logs and packet-003 LaTeX output. All 37 non-table content blocks
survive in HTML/PDF; all 16 table body cells survive fully and in order within
the table section. HTML remains a table. The amended print form preserves both
column identities and all cells as page-breakable blocks. The provisional PDF
clipped the longest cell; the repaired longest rows were visually inspected,
and final PDF pages 17–18 are pixel-identical to that inspected repair. There is
no clipping or footer overlap there. A few field labels precede a page break,
which is a minor presentation limitation. All four paper URLs remain actual
PDF link annotations. All 21 defined labels occur uniquely in HTML and TeX;
TeX native-reference counts match the exact reservation inventory.

The partial reference gate passes. Only the 26 exact registered future targets
remain unresolved, individually listed with native-reference counts, pending
links and accepted diagnostics in the evidence below. Visible unresolved
numbers and absent future chapters mean this is **not a complete edition**.
Earlier accepted pieces were checked for identity/assembly, not independently
reaudited scientifically. The review used the neutral assignment, frozen inputs,
original target contexts, rendering amendment/tools/artifacts and the acceptance
receipt; no worker reports, prior review reports or study history were used.

Evidence: [exact reviewed hashes](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/reviewed_hashes.json),
[final input manifest](../../data/generated/quarto_capability_pilot_20260921/linear_003-audit-final/hashes.json),
[rebase checks](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/final_rebase_checks.json),
[source check](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/final_source_check.json),
[render check and explicit reservations](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/final_render_check.json),
[artifact checks](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/final_artifact_checks.json),
[table checks](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/repaired_provisional_table_checks.json),
[negative challenges](../../data/generated/quarto_capability_pilot_20260921/batch02-astra003/challenges.json).
