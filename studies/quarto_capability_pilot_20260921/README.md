# Quarto capability pilot

Repository-maintenance publishing pilot, 2026-09-21. The artificial capability
tests were followed by the authorized real-text pilot described below. The
existing book and publishing code remain unchanged. Source order and structure
are preserved in the candidate; reorganization is a separate phase.

**Current phase (2026-09-25): deterministic migration finalized.**
`migration.py` now reads the eleven maintained theory chapters under `docs/`
and writes the separate candidate under `new_doc/`. The implementation guide
under `code/` is not a book chapter and is not migrated. The program itself
invokes no model or renderer. The old book and code documentation are unchanged.

The structural pass defined 4,629 stable targets and reserved 300 more for
labelled raw formulas. The initial four Terra 5.6/medium responses supplied
structured replacements for 6,508 exact candidates. The completed source-aware
scan added 949 previously unflagged records, giving 7,457 records: 3,667
inline-code spans, 611 indented formula blocks, and 3,179 plain-text formula
lines. The compact review covered 10,094 atomic replacements, corrected the
recorded mathematical transcription errors, and rechecked every affected syntax
class. Its final notation pass corrected 154 mappings in 147 records, including
indexed symbols, indicator functions, and legacy transpose markers.

The candidate now defines all 4,929 targets. It converts all 3,360 original
tagged displays to automatic Quarto equation labels without changing their
mathematical payloads, converts
legacy inline TeX delimiters, recognizes 130 formal environments, anchors three
named symbolic statements, and maps the old HTML anchors and bold numbered
subsections, including the six plain-numbered bold subunits.

The index renders 5,728 target references and preserves all six repository-local
links. The 27 originally ambiguous references and five additional equation
ranges have reviewed exact mappings. A reference/math separation check recovered
35 references that earlier formula spans had hidden and now rejects any such
overlap. The six literature links retain their original destinations and also
carry verified citation keys backed by six entries in `new_doc/references.bib`.

The build reports zero unresolved math, references, links, or equations. Checks
cover all 7,457 exact applications, every target and reference, source hashes,
fenced code, display payloads, repository links, bibliography decisions, and
math/reference separation. Independent residual scans find no legacy delimiters,
raw mathematical signals, or pseudo-symbol syntax in replacement payloads.

The final publishing run is `data/generated/quarto_capability_pilot_20260921/
finalization08/`. All 56 migration tests, the synthetic self-test, the complete
formula preflight, and the whole-book integrity checks pass. All 14 generated
source/support files reproduce byte-for-byte from frozen inputs. HTML, PDF and
editable LaTeX render successfully; all 4,929 expected HTML targets occur exactly
once, with no broken internal links or unresolved citations. The PDF is 1,614
pages and passes `qpdf`; compiling the exported LaTeX independently produces the
same PDF byte-for-byte. Eight representative pages covering front matter, long
and split mathematics, recovered headings, a formal statement and the bibliography
were inspected visually and pass. The two remaining TeX diagnostics are inherited
legacy `amsmath` syntax warnings; there are no missing glyphs, undefined references,
duplicate PDF destinations, or overfull boxes wider than 50 pt.

The first attempted call set was rejected atomically: one prompt exceeded the
hard character limit, one response stopped after 30 display items, and two
responses returned empty arrays. No part reached `new_doc/`. The corrected
schemas required the exact full array lengths; their four responses are the only
ones represented in `migration_decisions.json`.

The active workflow is [the deterministic migration contract](LIGHTWEIGHT_MIGRATION.md).
The former packet-by-packet model workflow, including packets 001–010 and their
audits, is historical evidence only and is not an active instruction.

## Scope and decision

Use a tiny artificial book to test standard mathematical environments, labelled
equations, cross-file/chapter references, includes, bibliography, HTML/PDF output,
and editable standalone LaTeX export. Test re-numbering after insertion and confirm
that missing references are detectable. Native limitations are recorded rather than
hidden behind custom filters. No custom compiler implementation in this toy.

Success: standard configuration produces correct linked HTML and PDF, and exported
LaTeX can be compiled independently with live references/citations. Core failures
stop real migration. Advanced features may be reported as explicit limitations.

## Ownership

Astra/root: test contract, runtime, builds and verification, this README.
Sol/medium subagent: artificial fixture sources only, no maintained edits.
Real-text pilot: fresh Terra 5.6/medium migration worker; fresh Astra preservation
reviewer. Root alone owns instructions, checker, configuration and this README.
All generated files, runtime downloads and logs: `data/generated/quarto_capability_pilot_20260921/`.
No Git staging or commit is part of this test.

## Baseline results and decision

Completed the bounded toy on Quarto **1.10.18**, with system XeLaTeX (TeX Live
2022/dev/Debian), latexmk 4.76 and biber 2.17. A portable official release was
downloaded into the study's generated runtime directory, verified against its
GitHub release asset SHA-256 (`afad071b5bd22c02f2d300695743189d3650e0537a53073e654b630cff2b0c73`).
No system installation, custom filters or publisher patches were used.

**Core functionality passes; this supports proceeding to the bounded real-text
pilot, not approval to migrate the full book.** The current book is unchanged.

- HTML, PDF and LaTeX export render successfully. The PDF has nine pages because
  the deliberately small fixture includes a title, contents, preface and two part
  title pages. The actual prose/math source is about 140 lines.
- Theorem, lemma, proposition, definition, corollary, remark, conjecture, example
  and proof display; inline math, an aligned display, matrix/cases notation,
  included Markdown, a table and footnote are exercised.
- Forward/back references across two chapters and an included `.md` resolve.
  The four generated HTML pages have no missing local HTML link targets or
  duplicate IDs under `check_toy.py`'s explicit scope.
- A fictitious, clearly marked bibliography record renders normally and with a
  page citation. Export retains `\\textcite`/`\\autocite`, `\\label`/`\\ref` and
  `\\printbibliography`. Exported `.tex` plus the standard `.bib` compile using
  latexmk without invoking Quarto. The bibliography must accompany the TeX;
  this release's LaTeX output directory did not copy it automatically.
- Inserting a theorem and equation into the exported LaTeX changes the original
  theorem/equation from 1.1 to 1.2, and the following included theorem from 1.2
  to 1.3. The references in the resulting PDF update accordingly.
- `qpdf --check` succeeds; Astra inspected the extracted PDF text and page 5
  visually. The standalone logs contain a nonfatal KOMA-Script float-package
  compatibility warning, not an undefined-reference error.

### Problems exposed and conventions needed

1. In run01, `::: {#proof-seed .proof}` crashed Quarto's filter in all formats.
   Inspection of the runtime traced this to treatment of the ID's prefix as a
   cross-reference category. A separate ordinary anchor `[]{#proof-seed}` before
   `::: {.proof}` works in HTML and LaTeX. The failed source/logs remain in run01.
2. A missing `@thm-does-not-exist` emits a warning but returns **exit code 0**.
   Adding `--fail-if-warnings` still returns 0 for this Quarto cross-reference
   warning. Migration therefore needs a small explicit unresolved-reference
   check/build gate; success of the rendering command alone is insufficient.
3. Proof and Assumption links are ordinary named anchors in this fixture, not
   automatically numbered cross-references. Standard theorem types have separate
   counters by default. No claim is made that numbered custom assumptions or a
   common theorem/lemma counter have been validated.
4. Sequential format renders can replace the common output directory. The runner
   uses standard separate output directories for HTML, PDF and LaTeX.

At the baseline stage, grouped subequations, automatically referenced theorem
subparts, figures, algorithms, and bibliography-style matching were not tested.
The bounded extension below supersedes that status where explicitly stated.
The ordinary item-(a) link has manual display text and does not track item reordering.

## Bounded capability extension

Completed on 2026-09-21, using the same Quarto runtime. Sources are
`extra_advanced.qmd`, `extra_appendix.qmd`, `extra_references.bib`, and
`extra_figure.tex`; the two added QMD files total 102 lines. `run_extension.py`
builds a generated copy of the artificial book. No maintained book content is
copied into it, moved, reformatted or promoted.

**The extension passes its explicit core checks; it also exposes native feature
limits. This is not an all-features or full-migration approval.**

| Capability | Observed result |
|---|---|
| Chapter/section/subsection/subsubsection references; appendix and cross-links | Pass in generated HTML and PDF, including `3.1.1.1` and Appendix A. |
| Grouped theorem/section references | Pass as lists of references; automatic range compression was not tested. |
| Algorithm, exercise and solution | Native numbered environments and references pass. This is an ordinary ordered-list algorithm, not a pseudocode language with line references. |
| Figure, longer aligned display, simple math macro | PDF inspected visually; HTML contains the expected figure, math and reference targets. No browser-based MathJax rendering audit was performed. |
| Proof ending in a display | PDF inspected: proof and end marker both render, with the marker on a separate line. |
| Two bibliography files; grouped and page-specific citations | Pass. HTML and PDF both use author–year citations; punctuation and bibliography formatting are not identical. |
| Standalone LaTeX export with macro, figure and bibliography | Compiles independently with live references and citations when both `.bib` files and the image are supplied. |
| Insertion/movement in Quarto source | HTML references update: original theorem/equation `1.1` to `1.2`; included theorem moves from first chapter `1.2` to second chapter `2.1`, with its link destination updated. |
| Deliberately broken references | The new gate rejects all six injected cases: missing theorem, equation, section, citation, duplicate HTML ID and missing local fragment. Quarto itself still returns zero. |
| Theorem subparts and proof links | Ordinary anchors work; item letters and link text remain manual. No automatic subpart/step numbering solution was established. |
| Subequations and separately numbered aligned rows | Raw LaTeX works in PDF. The same source lacks the corresponding automatic numbering/reference behavior in default HTML; see `edge_notes.md`. |
| Numbered Assumption alongside Theorem | Global theorem relabelling works, but it changes every theorem. No independent theorem-style Assumption type was found in standard configuration. Custom cross-reference types are floats. |
| Shared theorem/lemma counter | No standard configuration found; native counters are separate. |

The additional edge probes are in `edge_features.qmd` and `edge_notes.md`, with
runtime/schema inspection and primary-documentation links. Their generated
evidence is in `edge01/`. Subequation HTML limitations are based on the emitted
configuration and MathJax's documented support, not a browser execution test.
They do not establish impossibility with extensions or custom configuration.

Astra read the final PDF text, inspected pages 9 and 10, checked native LaTeX
commands, reviewed the positive/negative gate results and the changed reference
numbers/destinations, and verified the edge-probe evidence. Visual inspection
also caught a wording error in the frozen toy: `Equation @eq-representative-long` renders
as “Equation Equation 3.1”. Quarto supplies the noun in its reference text;
migration must avoid preserving a redundant raw prefix. This is a useful example
of a semantic/presentation error that a valid-link check cannot detect.

### Reference gate scope

`reference_gate.py` returns nonzero for known unresolved-reference/citation
diagnostics, duplicate IDs within a generated HTML page, and broken local HTML
destinations. The valid six-page book passes; all six injected failures are
detected. It is intentionally small, with no publishing filter or runtime patch.
It is a tested toy gate, not yet a complete production migration checker.

It cannot recognize a scientifically wrong but existing destination, an
unconverted raw-text reference, or arbitrary MathJax failures. Duplicate source
labels across chapters need a global source-label check in a real migration.
Old/new block mapping, candidate reference searches and semantic review remain
necessary. Pending references to material outside a partial pilot must be listed
explicitly; a partial pilot is not a fully resolved book.

### Remaining decisions

Before broad migration, choose whether separate theorem counters, named
Assumptions, manual subparts, and one native equation label per display are
acceptable. If automatic custom environments, shared counters or portable
subequations are requirements, they need their own bounded solution test first.
Do not silently simplify required mathematical structure during migration.

Full-book performance, long real proofs/displays, shared macros across files,
automatic reference ranges and precise cross-format bibliography style matching
remain outside this quick extension. The bounded real-text pilot remains the
next preservation test; its authorization and actual execution are separate.

Extension evidence:

- `extension01/commands.json`, `extension01/source_hashes.json`: execution and source snapshot.
- `extension01/verification.json`: explicit results, negative cases and before/after references.
- `extension01/book/_out-pdf/Artificial-Quarto-Mathematics-Fixture.pdf`: extended 12-page PDF.
- `extension01/book/_out-html/index.html`: extended HTML book.
- `extension01/standalone/`: independent LaTeX build with ordinary assets.
- `extension01/page-09.png`, `extension01/page-10.png`: inspected PDF pages.
- `extension01/final_receipt.json`: maintained-source preservation and final source hashes.

Reproduce into a fresh generated directory:

```sh
python studies/quarto_capability_pilot_20260921/run_extension.py \
  --quarto data/generated/quarto_capability_pilot_20260921/runtime/quarto-1.10.18/bin/quarto \
  --run-directory data/generated/quarto_capability_pilot_20260921/extension-reproduction01
```

## Evidence

Generated paths below are relative to `data/generated/quarto_capability_pilot_20260921/`:

- `runtime/release.json`: official release metadata and download provenance.
- `run01/`: first source snapshot and retained proof-anchor failure.
- `run02/`: successful render/export before separating output directories.
- `run03/commands.json`, `run03/source_hashes.json`: successful baseline provenance.
- `run03/verification.json`, `run03/verification_commands.json`: link, standalone,
  renumbering and deliberately broken-reference results.
- `run03/book/_out-pdf/Artificial-Quarto-Mathematics-Fixture.pdf`: Quarto PDF.
- `run03/book/_out-html/index.html`: HTML entry point.
- `run03/book/_out-latex/book-latex/Artificial-Quarto-Mathematics-Fixture.tex`: export.
- `run03/standalone/` and `run03/standalone_inserted/`: independent TeX builds.
- `run03/page5.png`: inspected page; `run03/rendered.txt`: extracted PDF text.
- `run03/final_receipt.json`: final source hashes and maintained-file preservation.

## Reproduction

From the repository root, select a **fresh** run directory:

```sh
python studies/quarto_capability_pilot_20260921/run_toy.py \
  --quarto data/generated/quarto_capability_pilot_20260921/runtime/quarto-1.10.18/bin/quarto \
  --run-directory data/generated/quarto_capability_pilot_20260921/reproduction01
python studies/quarto_capability_pilot_20260921/check_toy.py \
  --quarto data/generated/quarto_capability_pilot_20260921/runtime/quarto-1.10.18/bin/quarto \
  --run-directory data/generated/quarto_capability_pilot_20260921/reproduction01
```

The first script records all build commands and source hashes. The second records
its command results, checks native cross-references and compiles exported TeX in
two fresh directories. Its core success status does not assert that the deliberately
missing-reference test is fatal: that limitation is explicitly recorded in JSON.
Original runs preceded the scripts' final nonzero-exit-on-core-failure checks;
those checks change reporting only, not rendering or verification commands.

## Real-text pilot: linear chapter opening

The user authorized a separate candidate edition with Terra 5.6 as the base
migration worker and Astra design/verification. This continues the same publishing
investigation. Scope is the existing chapter's first 907 lines, through original
Section 4. The maintained source stays in `docs/linear_dynamics.md`; the candidate
is `pilot_linear.qmd` in this study, not in the established book.

- `pilot_policy.md`: minimal isolated-packet and fault-recovery policy; complete
  pilot review, later 10% random section sampling plus targeted checks.
- `pilot_instructions_v1.md`: original worker instructions; `pilot_instructions.md`:
  revised v2 rules for the next isolated packet, retaining the same permitted content changes.
- `pilot_source.md`, `pilot_manifest.json`: exact original excerpt, hashes,
  contiguous six-block map, target identities and explicit pending references.
- `pilot_quarto.yml`, `pilot_index.qmd`, `pilot_notation_resource.md`: candidate
  publication configuration, scope note and unchanged notation resource.
- `check_pilot.py`: packet-specific content, equation, boundary and reference
  checks. `render_pilot.py`: isolated builds into fresh generated directories.
- `pilot_audit_assignment.md`: neutral full-preservation audit assignment.

The fresh worker reads only the assignment, excerpt and manifest; it has no prior
migration context. The fresh reviewer receives a frozen complete packet without
the worker self-report or root's preliminary verdicts. This is preservation
maintenance, not a mathematical reproof or a new scientific promotion.

### Outcome

**The corrected excerpt passes preservation and publishing checks. Terra's first
submission needed a small repair; this is not a flawless first-pass result.**
One isolated Terra 5.6/medium worker produced the candidate. Astra/root performed
design, deterministic checking, bounded repair and rendering. A fresh Astra/high
reviewer read 100% of the frozen original and candidate, then verified the complete
correction diff and reran its independent full comparisons. No second worker,
model escalation or restart was needed.

The first candidate preserved all prose and mathematical payload, but its main
theorem fence absorbed the following explanatory paragraph. Both the mechanical
boundary check and independent reviewer caught this. Separately, display syntax
needed blank lines around equations and removal of the whitespace-only line left
by an indented tag-only line. The missing blank-paragraph rule was a design gap;
the misplaced theorem fence violated an explicit original rule. The worker's
self-report did not catch that boundary defect and is not acceptance evidence.

The bounded Astra repair moved one fence, inserted 18 blank lines around nine
displays, and removed one internal whitespace-only line. All scientific tokens
and their order remain preserved. Initial and intermediate failures remain in
`pilot01/` and `pilot02/`; the accepted candidate and complete output are frozen
in `pilot03/`. The active v2 instructions make both rules explicit and the checker
enforces them. There has not yet been a new Terra run under v2; retain full review
for the next calibration packet before switching to the later sampling policy.

Checks passed:

- Six contiguous source blocks, all 907 original lines, preserved under the exact
  allowed transformations; four formal statements and three proof scopes correct.
- All 316 substantive inline expressions and 49 displays preserved; 45 equation
  labels, 55 native IDs and 63 reference occurrences independently checked.
- Nine injected defects rejected, including a changed qualifier, a valid but
  wrong destination, an altered constant, dropped text, and an expanded theorem.
- HTML/PDF/LaTeX builds pass. HTML has the expected 316 inline/49 display math
  nodes and no broken local HTML references or unresolved-reference diagnostics.
- Exported LaTeX compiles independently; all 55 labels remain live. The original
  notation resource is bundled alongside each format, including PDF explicitly.
- The candidate file, independently reviewed snapshot and rendered source agree
  byte-for-byte. All 17 monitored maintained files remain unchanged.

Root inspected PDF pages 4, 6, 9 and 10. One originally long equation (original
1.1) extends 60.99 pt beyond the text margin but remains visible on the page. This
is a recorded typography limitation; no mathematical reflow was smuggled into the
preservation conversion. A nonfatal KOMA-Script/float warning also remains. Full
browser/MathJax visual review and whole-book layout/performance are outside this
pilot. Native named-proof captions also differ: HTML prints “Proof (of the
singular expansion)”, whereas PDF uses “of the singular expansion” alone as the
proof heading. The proof environment, body and end marker survive; the caption
needs a publication convention before full migration. These two typography issues
are explicitly open, not a claim of publication-ready layout. The two introductory
section-range references remain explicitly pending.

Reports: `pilot_worker_report.md` (untrusted self-check), `pilot_astra_review.md`
(initial NEEDS CORRECTION), `pilot_astra_followup.md` (bounded correction PASS).
The latter documents its initial full read plus complete correction diff and
full independent mechanical rerun; it does not claim a second complete manual
read or scientific reproof.

Generated evidence under `data/generated/quarto_capability_pilot_20260921/`:

- `pilot01/audit_inputs/`: original complete frozen packet; failed first build.
- `pilot02/`: first spacing repair, retaining the indented tag-line parsing failure.
- `pilot03/audit_inputs/`: final frozen candidate, original contract and v2 amendment.
- `pilot03/preservation_and_faults.json`: complete mapping and nine negative controls.
- `pilot03/parser_check.json`, `reference_gate.json`, `commands.json`, `final_receipt.json`:
  parser, reference, build, correspondence, output and maintained-source checks.
- `pilot03/book/_out-pdf/PDE-book-—-isolated-migration-pilot.pdf`: readable pilot PDF.
- `pilot03/book/_out-html/index.html`: pilot HTML book.
- `pilot03/standalone/`: independently compiled editable LaTeX and notation resource.
- `pilot-audit/`, `pilot-audit-followup/`: independently written complete comparison
  scripts, full reference/display ledgers and correction evidence.

### Real-text reproduction

Use a fresh generated directory. These commands do not edit the existing book:

```sh
python studies/quarto_capability_pilot_20260921/check_pilot.py \
  studies/quarto_capability_pilot_20260921/pilot_linear.qmd --fault-tests
python studies/quarto_capability_pilot_20260921/render_pilot.py \
  --quarto data/generated/quarto_capability_pilot_20260921/runtime/quarto-1.10.18/bin/quarto \
  --run-directory data/generated/quarto_capability_pilot_20260921/pilot-reproduction01
python studies/quarto_capability_pilot_20260921/reference_gate.py \
  data/generated/quarto_capability_pilot_20260921/pilot-reproduction01/book/_out-html \
  data/generated/quarto_capability_pilot_20260921/pilot-reproduction01/html.log \
  data/generated/quarto_capability_pilot_20260921/pilot-reproduction01/pdf.log \
  data/generated/quarto_capability_pilot_20260921/pilot-reproduction01/latex.log
```

For standalone compilation, copy the exported `.tex` and `NOTATION.md` into a fresh
directory, name the TeX file `pilot.tex`, and run
`latexmk -xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape pilot.tex`.
The complete executed command and output are recorded in `pilot03/final_receipt.json`
and `pilot03/standalone.log`.

This accepts only the opening prefix of the selected chapter as a candidate
conversion, not a first-chapter prefix of the entire book. No subsequent chapter
has been started, no established material replaced, and no Git changes staged or
committed. The next step is a separate user-authorized calibration packet under
the tightened rules; reorganization remains deferred.

Subsequent user clarification: repairs must address the widest justified failure
class through reusable instructions/checks and a scan of prior candidates, rather
than only fixing the reported occurrence. `pilot_policy.md` now states that rule
explicitly. Full Astra review remains mandatory for every packet in the current
phase; sampling is only a later separately agreed option. No additional conversion
packet was launched by this policy clarification.


## Linear migration: packet 001 checkpoint (historical)

The first linear packet is **accepted as a separate formatting candidate**:
`docs/README.md` original lines 1–211, preserved in `linear_001.qmd`. The existing
book is still authoritative and byte-identical to the frozen version. Nothing
has been reorganized or scientifically promoted. The earlier 907-line linear
chapter pilot is out of order and is not part of this accepted prefix.

The frozen book contains 12 source files, in the existing publisher's order,
at Git revision `ab6dd76987007b925b4d9559a936234e224ef6e9`. The manifest records
complete hashes, line counts, source paths and future output filenames. Frozen
copies are under `linear_frozen/snapshot/` in this study's generated namespace;
source bytes can also be reconstructed from that pinned revision. Do not replace
these snapshots with newer concurrent versions of the maintained book.

The small operational contract is:

- `migration_rules.md`: canonical source ranges, Quarto-compatible typed IDs,
  permitted edits, reference inventory and pending-target rules (current v3).
- `migration_sources.json`: immutable source identities and order.
- `migration_registry.json`: 16 accepted target entries, eight currently defined
  and eight binding future reservations. State is determined from accepted
  candidate labels; a reservation never advances the migrated prefix.
- `migration_progress.json`: accepted contiguous ranges and candidate/registry
  hashes; `linear_001_acceptance.json` binds this acceptance to the complete audit.
- `linear_001_packet.json`, its before-registry/progress copies, edit list and
  target proposal: reproducible correspondence independent of later state updates.
- `migration_check.py`: exact edit replay, typed interval/identity checks,
  original-coordinate validation, preservation and reference inventory.
  `check_linear_render.py` checks the partial HTML/Quarto driver logs.

The checker remains deliberately scoped to this packet's syntax: section
labels, references, delimiter conversion and display-adjacent whitespace. New
syntax needs its own explicit rules/checks before it is used. It is not a custom
publisher or a semantic proof checker. Source offset mapping remains valid when
formatting changes the candidate's line count.

### Outcome and calibration

A fresh Astra audit read all 211 original and candidate lines, every edit and
all 16 actual target identities. Its verdict is **PASS for this exact partial
packet**, with no candidate correction required. See
`linear_001_astra_review.md` for full coverage, hashes and evidence. Root verified
all 47 hashes in that report against the final files before merging the registry
and advancing the prefix. All 12 maintained source files still match the frozen
hashes. No Git staging/commit or other study changes were performed by this task.

The candidate has eight heading labels, nine reference conversions and one
unnumbered display whose mathematical payload is byte-identical. Six backtick
spans remain unchanged. The continuous-depth destination is reused for two
references. Eight future destinations remain explicitly pending; the partial
preview therefore contains unfinished links and reference-number placeholders.
It must not be presented as a finished book. Current targets resolve in HTML
and TeX; HTML/PDF/LaTeX render, and exported TeX compiles independently. All seven
PDF pages were independently inspected. Browser/MathJax visual execution was not
performed. The independent audit ran 25 supplied tests and 25 further challenges;
two deliberate semantic errors passed mechanical checks, demonstrating why full
human-level source/reference review remains necessary.

This was **not a clean Terra calibration pass**. Two fresh Terra/medium workers
left reference omissions, and the second used disallowed whole-heading edit
records. One fresh Sol/medium worker repaired the bounded packet; the coordinator
did not rewrite its scientific content. Original submissions, self-reports,
rejections and local failed checks are retained. See
`linear_001_submission01_review.md`, `linear_001_submission02_review.md`,
`linear_001_report_v1.md`, `linear_001_report_v2.md`, and the final
`linear_001_report.md`. A separate Sol/medium task implemented the checker to the
coordinator's specification; Astra reviewed and refined its original-coordinate,
range and link checks before the independent full audit.

The failure-class fixes are reference discovery across existing links, numbers
AND plain/italicized named destinations; insertion-only label edits; exact replay
including final blank lines; and mandatory worker access to the checker before
handoff. The first workers' restricted input scope had excluded that checker,
which was an avoidable coordination inefficiency. Full review stays mandatory;
this run does not establish token savings or justify unattended bulk migration.
The previous out-of-order pilot's bundled notation link and two pending range
references remain known obligations when that source is reached later.

Generated evidence (relative to this study's generated-data directory):

- `linear001-submission01/`, `linear001-submission02/`: retained Terra submissions.
- `linear-checks/`, `linear001-checked01/`, `linear001-sol-repair/`: failures,
  bounded repairs and their checks; `linear001-checked02/`: final root diff/check.
- `linear001-audit-inputs/`: complete frozen review packet and hash manifest.
- `linear001-astra-audit/`: independent comparisons, fault challenges and all PDF pages.
- `linear001-render01/`: three-format builds, commands, hashes, reference report,
  standalone TeX build, and final source/label correspondence evidence.

### Reproduction and next packet

From the repository root, the packet's immutable before-copies let its original
check run even after the shared registry has advanced:

```sh
python studies/quarto_capability_pilot_20260921/migration_check.py \
  studies/quarto_capability_pilot_20260921/linear_001_packet.json
python studies/quarto_capability_pilot_20260921/render_linear.py \
  studies/quarto_capability_pilot_20260921/linear_001_packet.json \
  --quarto data/generated/quarto_capability_pilot_20260921/runtime/quarto-1.10.18/bin/quarto \
  --run-directory data/generated/quarto_capability_pilot_20260921/linear001-reproduction01
python studies/quarto_capability_pilot_20260921/check_linear_render.py \
  data/generated/quarto_capability_pilot_20260921/linear001-reproduction01
```

Select a fresh run directory. The standalone export and exact independent
`latexmk` command are recorded in `linear001-render01/standalone_command.json`;
copy the exported directory to fresh generated scratch before compiling it.
The render gate checks HTML and Quarto logs; the full audit separately verifies
PDF/TeX contents, actual labels and final engine warnings against reservations.

At this checkpoint the next source was **`docs/README.md:212`**, beginning with the existing Mermaid diagram.
Do not skip it, migrate a later chapter first, or silently replace the diagram.
Use a fresh isolated worker with the v3 contract, current registry/progress
snapshots and access to the checker. Preserve its source while qualifying any
new rendering case; then assemble the contiguous prefix and obtain the required
fresh full Astra audit. The present rendering runner supports only a prefix of
the introduction starting at line 1; ordered multi-packet assembly must be added
explicitly when that next packet is ready. Continue the book's existing order;
reorganization, scientific promotion and maintained-code changes remain separate.

## Linear migration: packets 002–003 checkpoint

**Packets 002 and 003 are accepted as formatting candidates**, adding 531 source
lines and completing the introduction in its original order:

| Packet | Frozen source interval | Independent full audit | Acceptance |
|---|---|---|---|
| 002 | `docs/README.md:212–496` | [PASS](linear_002_astra_review.md) | [Receipt](linear_002_acceptance.json) |
| 003 | `docs/README.md:497–742` | [PASS](linear_003_astra_review.md) | [Receipt](linear_003_acceptance.json) |

Two fresh isolated Sol/medium workers prepared the packages in parallel; two
fresh Astra reviewers audited all source content, edits and reference identities
in parallel. Both candidates passed without content correction. Acceptance was
sequential: 003's before-state was updated only after actual 002 acceptance, and
two identical reference proposals were reused. Its candidate and edit list did
not change. Root checked all 36 artifact hashes in each final review inventory
before acceptance. Immutable initial/final inputs preserve the correspondence.

The live registry now contains **47 targets: 21 defined and 26 reserved for later
chapters**. The prefix is exactly 001 + 002 + 003, with no reordering. All twelve
maintained source files still match their frozen hashes; maintained book/code
and Git index were not changed by this task. External paper URLs remain intact.
This remains a partial edition with visible pending references.

The source-check suite passes 17 tests and the assembly/render suite passes 14.
Final HTML, PDF and LaTeX builds and the exact-reservation gate pass. Full audits
also inspected rendered content: the complete diagram and every chapter-table
cell survive. Standard PDF rendering initially clipped the diagram and long
rows. The [bounded print amendment](migration_render_rules.md) now uses native
page bounds and a small filter for breakable simple two-column tables; source
and HTML tables remain unchanged. A two-line browser launcher corrects the
observed raster-outline crop. Unsupported table shapes and new diagrams still
require review; field labels can precede a page break. Exact reproduction details
and retained failed attempts are in [render notes](batch02_render_notes.md).

Final generated runs, relative to this study's generated-data directory:

- 002: `batch02-render-tooling/linear002-render-repaired-v5/`.
- 003 and the full accepted introduction: `linear003-render-final02/`.
- Frozen final audit inputs: `linear_002-audit-final-v5/`, `linear_003-audit-final/`.
- Independent review evidence: `batch02-astra002/`, `batch02-astra003/`.

Reproduction uses the existing commands above with `linear_003_packet.json` and
a fresh run directory; its immutable before-copies remain reproducible after
acceptance. Permit the browser's local debugging port during rendering.

**Next source: `docs/NOTATION.md:1`.** Use the same frozen manifest, registry and
full-review contract. The current runner assembles an introduction prefix;
crossing into the next file needs ordinary multi-chapter Quarto assembly while
retaining verified component hashes. Reorganization remains deferred. No third
package or additional scientific work was started in this two-package batch.

## Linear migration: packet 004 checkpoint

Packet **004**, all 98 lines of frozen `docs/NOTATION.md`, is accepted:
[full Astra review](linear_004_astra_review.md), [receipt](linear_004_acceptance.json).
One fresh Sol/medium worker, one fresh complete Astra preservation audit, and one
HTML/PDF/LaTeX build; no candidate corrections. Nine surgical edits preserve all
prose, backticks and both formula payloads. The existing title reservation is
fulfilled; four new headings bring the registry to 51 targets (26 defined,
25 future reservations).

The only tooling change groups verified source packets into ordinary Quarto
chapters in manifest order. Sixteen render tests passed; the reviewer separately
checked all five assembly tests, one broken-anchor challenge, the complete new
chapter and its rendered formulas. Earlier content received hash/assembly checks,
not repeated content audits. Root verified all 56 reviewed hashes before accepting.
All maintained source hashes remain unchanged. No Git operations were performed.

Inputs: `linear004-audit-inputs/`; audit evidence: `packet004-audit/`; final build:
`linear004-render/`, all under this study's generated directory. Reproduce with
the existing renderer command, `linear_004_packet.json` and a fresh run directory.
The current runner now supports subsequent source files. The explicit
[cost discipline](pilot_policy.md#cost-discipline-from-packet-004) retains full
new-content review while removing repeated audits and cosmetic print work.

Next source: **`docs/global_nonlinear.md:1`**. Accepted total: **840/77,711 lines
(1.08%)**. Reorganization and scientific promotion remain separate.

## Linear migration: packets 005–006 checkpoint

Packets **005–006** are accepted as formatting candidates, adding **999 lines**
of frozen `docs/global_nonlinear.md` without reordering or scientific changes:

| Packet | Source lines | Complete preservation review | Acceptance |
|---|---|---|---|
| 005 | 1–504 | [Astra PASS](linear_005_astra_review.md) | [Receipt](linear_005_acceptance.json) |
| 006 | 505–999 | [Astra PASS](linear_006_astra_review.md) | [Receipt](linear_006_acceptance.json) |

Each packet used an isolated Sol conversion and a fresh full Astra preservation
review. Root checked all 176 and 108 artifact hashes in the respective inventories.
Packet 006 was rebased only after actual 005 acceptance: eight identical proposals
were removed; candidate and edits stayed byte-identical. The registry now has
**107 targets: 80 defined and 27 future reservations**.

This batch introduces 42 native numbered equations and one theorem environment.
The [math rules](migration_math_rules.md) and checker preserve formula payloads,
theorem boundaries, numeric reference destinations and composite section locators.
The 25 source-check tests passed. Tag-only lines use a TeX comment to avoid a
Pandoc paragraph break; the native class option preserves existing `\rm` notation.
Initial failed builds remain retained as evidence.

Final HTML, PDF and LaTeX builds and exact-reservation checks pass. Reviewers read
all new source content and inspected all new PDF pages. One clipped equation
required the bounded [print amendment](migration_render_rules.md): six displays
across this batch gain only layout wrappers/row breaks; earlier packets have no
matching displays. The [focused fixture](print_filter_cases.md) is retained;
commands, hashes and match inventory are in generated
`math-check-extension/print_filter_focused_results.json`. Cosmetic duplicate heading
numbers and one readable equation extending into the margin are deferred. HTML
math was checked statically; browser MathJax runtime was not tested this round.

Final runs: `linear005-render-wrapped/` and `linear006-render-final/`; frozen inputs:
`linear005-audit-final/` and `linear006-audit-final/`; independent evidence:
`packet005-audit/` and `packet006-audit/`, all under this study's generated directory.
Use the existing reproduction commands with the corresponding packet descriptor.
Earlier failed attempts and initial inputs remain untouched.

All maintained source hashes remain unchanged. No Git writes, maintained implementation changes,
reorganization or scientific promotion occurred. The accepted prefix is now
**1,839/77,711 lines (2.37%)**. Next source: **`docs/global_nonlinear.md:1000`**.
No further packet has been started.

## Linear migration: packet 007 checkpoint

Packet **007**, frozen `docs/global_nonlinear.md:1000–1898` (**899 lines**),
is accepted: [full Astra audit](linear_007_astra_review.md),
[receipt](linear_007_acceptance.json). One isolated Terra conversion, one full
Astra content/reference audit, and a two-link correction checked only as a delta.
All words, formulas, qualifiers and source order are preserved. The existing
checker passes; its small heading-versus-prose correction has a focused regression.
No renderer, visual review, new test campaign or publishing machinery was used.

The audit caught coordinated named chapter references sharing a suffix
(“global nonlinear and special-data chapters”); both now link to existing IDs.
Future workers should explicitly include such coordinated names in their existing
all-reference scan. This is an application of the current rule, not a new target type.

Root verified all 70 reviewed hashes. Registry: 162 targets,
131 defined and 31 future reservations. Frozen initial/final inputs:
`packet007-audit-inputs/`, `packet007-audit-final/`; evidence: `packet007-audit/`,
under the study's generated directory. Rendering is explicitly deferred to
integration, so this acceptance does not certify publishing presentation.

All maintained sources remain unchanged; no Git writes or scientific promotion.
Total: **2,738/77,711 lines (3.52%)**. Next: **`docs/global_nonlinear.md:1899`**.

## Linear migration: packet008 (historical)

Packet **008**, `docs/global_nonlinear.md:1899–2453` (**555 lines**, complete B),
is accepted: [Astra audit](linear_008_astra_review.md),
[receipt](linear_008_acceptance.json). User-selected **Luna5.6** performed conversion;
one fresh Astra preservation audit passed without corrections. Existing checker
passed; root verified 36 reviewed hashes. No new tooling, rendering or test
campaign. Original book/code and Git index were not changed.

The initially larger 1,542-line attempt reached C.1's numbered indented plain-text
formulas. Current rules preserve such text verbatim but do not yet support native
equation labels/references for it. Do not invent TeX or waive reference checks.
The larger conversion remains **unaccepted**, retained as
`linear_008_extended_unaccepted*`; its descriptor points to those retained files.
It does not advance the prefix or merge its target proposals. A.1 references in
the accepted B section were resolved using the existing registry.

Current source/reference-audited total: **3,293/77,711 lines (4.24%)**.
Registry: 195 targets, 164 defined and 31 future reservations.
Frozen input/evidence: `packet008-audit-inputs/`, `packet008-audit/` under the
study's generated directory. Next source: **`docs/global_nonlinear.md:2454`**.
Before accepting C.1, settle the precise treatment of its code-form equations;
no further conversion or publishing work is underway.

## Linear migration: current

Packet **009**, `docs/global_nonlinear.md:2454–6341`, is accepted: **3,888
source lines (5.003% of the frozen book)**. User-selected Luna5.6 workers
performed conversion and corrections; Sol5.6 was the sole final reviewer.
See the [PASS review](linear_009_sol_review.md),
[acceptance receipt](linear_009_acceptance.json), and complete
[correction record](linear_009_sol_corrections.md).

All mathematics in this packet is typeset; numbered equations and references
use automatic targets. The strict checker passes. Sol reports 31/31 focused
tests passed. Root verified 27 review-inventory entries and all 124 entries
in the four immutable audit manifests, exact candidate correspondence, prior
accepted-file hashes, and unchanged established/frozen source hashes. The
registry now has **450 targets: 417 defined, 33 reserved** for future migration.

One initial full audit was retained throughout; corrections returned to the
same Sol auditor for changed-only checks until PASS. Root applied the final
two literal prime-notation substitutions exactly as Sol requested. No fresh
auditor, scientific reproof, rendering campaign, Git write, or established
book/code edit was performed. Rendering remains deferred to integration.
Frozen initial/correction inputs are `packet009-audit-inputs/`,
`packet009-audit-corrected/`, `packet009-audit-final/`, and
`packet009-audit-final2/` under this study's generated namespace.

Current source/reference-audited total: **7,181/77,711 lines (9.24%)**.
Next source: **`docs/global_nonlinear.md:6342`**. This completes the authorized
5% batch; no additional batch is running.

**Outstanding earlier-packet obligation:** the newer no-plain-math requirement
supersedes the earlier pseudo-math-preservation policy. Packets001–008 retain
their original receipts, but their remaining ASCII/code-form math needs a
targeted transcription pass before the entire edition is called fully migrated.
This batch did not authorize or perform that separate cleanup.

General worker safeguards from this batch are recorded in
[pilot_policy.md](pilot_policy.md): cover abbreviated reference-range endpoints,
bare symbols, and complete word boundaries. Derivative primes must be attached
superscripts (`f'` or `f^{\prime}`), never detached `f\prime`.

## Packet010 pause after budget overrun

Coordinator paused further model work after the user's budget complaint.
The accepted prefix remains001–009 (7,181/77,711 lines,9.24%). Packet010
6342–7909 is preserved but unaccepted. Its worker reports the prescribed late
corrections applied to `linear_010_edits.json` / `linear_010.qmd` and a strict
checker PASS (1049 edits). The same Sol auditor has not yet checked that final
late delta; no acceptance receipt or registry/progress advancement was made.
Resume only on user direction, retaining Sol's prior accepted review and checking
only the late delta against `packet010-audit-corrected/`. The initial round
failed its efficiency target; no token-savings claim is justified. Workers have
finished their current actions; no new review was launched at this pause.

## Lightweight workflow reset (2026-09-24)

The earlier operational workflow is superseded by
[`LIGHTWEIGHT_MIGRATION.md`](LIGHTWEIGHT_MIGRATION.md). Future conversion uses
one tool-free Terra call and one tool-free isolated Sol audit per block, with
local mechanical checks between them. The coordinating thread never rereads or
reproduces complete book blocks and performs no duplicate semantic audit.
Historical packets and packet010 remain frozen evidence and are not active
workflow inputs. No migration call or book-content read occurred in this reset.
