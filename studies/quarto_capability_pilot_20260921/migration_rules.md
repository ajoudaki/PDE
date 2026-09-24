# Linear migration contract v4

Maintenance only. The frozen old book is the authority. Preserve all content,
order, heading levels, qualifiers, formulas and proof boundaries. Do not improve
wording, repair mathematics, promote research, or reorganize. Existing live
`docs/` and `code/` are read-only. The current roles and handoff gate are in `pilot_policy.md`: Luna performs
conversion AND reference discovery; Sol audits new content once and checks
corrections surgically. Root does not pre-author the target map.

## Frozen coordinates and one registry

`migration_sources.json` records book order, original paths, frozen copies,
SHA-256 hashes and the pinned Git revision. All ranges below are **1-based,
inclusive lines in those frozen files**, never current candidate line numbers.
The original contents can also be reconstructed from the pinned Git revision.
The linear prefix is tracked separately from references into future content.
`migration_progress.json` lists only accepted packets in order, with source
ranges and candidate paths/hashes; each packet's acceptance receipt links its
full audit. The next packet must start
immediately after that prefix; merely reserving a future target never advances it.

`migration_registry.json` is the accepted registry. A worker reads it, reuses
existing targets and proposes new targets in its packet's `_targets.json`.
Only the coordinator merges reviewed additions; workers never edit the shared
registry. Each target has exactly `id`, `kind`, `source`, `start`, `end`.
Packets retain immutable before-copies of the registry/progress so their checks
remain reproducible after later acceptance updates the shared versions. Query
the registry by source and interval; do not load its entire text into context.
The ID is `<kind>-<file-key>-l<start>`; file keys are fixed in the source manifest.
Quarto uses hyphens, not colons. Types use its spelling: `sec`, `thm`, `lem`,
`prp`, `cor`, `def`, `cnj`, `rem`, `exm`, `exr`, `sol`, `alg`, `eq`, `fig`, `tbl`;
ordinary anchors use `proof`, `assumption`, `part`, `eqpart` where appropriate.
Do not silently convert an unsupported type into a different environment.

Canonical ranges:

- `sec`: the ATX heading line only, including chapter titles.
- Formal statements: first statement/caption line through the last statement
  line, excluding proof and subsequent explanation. Statement text is unchanged.
- `proof`: first proof line through its final text/display/end marker, excluding
  the following commentary. Give it a separate ordinary anchor before the proof
  environment; never put a `proof-` ID on Quarto's proof div.
- `eq`: the whole display, opening through closing delimiter lines. Leave an
  unnumbered, unreferenced display unnumbered and without a registry entry.
- An explicitly referenced row/subpart uses `eqpart`/`part`, with the narrowest
  complete original line span containing that row/item; it must be contained in
  its parent object's range. Multiple targets on one source line, shared row
  delimiters, or unavailable portable syntax are exceptions: report, do not
  guess new identity conventions. They require a bounded contract amendment.
- Figures/tables: the whole original source block, including caption, excluding
  surrounding prose. Mathematical definitions can require semantic boundary
  review; range checks never establish that a boundary is scientifically right.

Search by source and overlapping interval before creating a label. Identical
source/kind/range means one object and one ID. Same-kind overlap is a conflict;
different mathematical statement kinds at the same span also conflict. Full
cross-kind containment (equation inside a theorem or proof) is legitimate;
crossing intervals are a conflict. Resolve ambiguity from the frozen source,
or flag it for audit. Never merge different kinds merely because they overlap.
Reserved targets in unmigrated content are binding future obligations. A target
is defined only if its accepted label actually occurs at its source location;
otherwise it remains reserved. Later packets must reuse/fulfil it. No fake
placeholder chapter, invented target or blanket unresolved-reference exemption.

## Edits and source correspondence

Each isolated packet receives a contiguous source range and returns:
`linear_NNN.qmd`, `linear_NNN_edits.json`, `linear_NNN_targets.json`, and a short
`linear_NNN_report.md`. Edits are a JSON list with `offset`, `old`, `new`, `kind`
and optional `target`. Offsets count Unicode characters from the start of the
exact source excerpt, zero-based. Edits are ordered and nonoverlapping; `old`
must match the original bytes after UTF-8 decoding. Do not edit line endings.
The candidate must equal applying exactly these edits. A raw old/new diff is
retained for review. No silent normalization of prose or mathematics is allowed.

For the first packet, allowed kinds are deliberately small:

- `label`: insert ` {#ID}` at the end of a section heading, `target: ID`.
  Use `old: ""` at the heading's ending offset; do not submit the whole heading
  as a replacement, even if its letters would remain unchanged.
- `math-delimiter`: `\[` / `\]` to `$$`, `\(` / `\)` to `$`, and nothing else.
- `whitespace`: adjust whitespace only to make valid paragraphs around displays;
  do not create blank paragraphs inside a display.
- `reference`: convert an existing reference to `@ID`, or a descriptive Markdown
  link whose caption is preserved exactly and destination is the manifest's
  `.qmd` file plus `#ID`. A numeric reference uses native `@ID`, not a hard-coded
  number disguised as link text. Preserve surrounding punctuation and emphasis.
  Quarto supplies the reference noun: avoid doubled “Section Section”.

Convert all code-form/plain mathematics faithfully under
`migration_transcription_rules.md`; actual code remains byte-identical. Existing
TeX display payloads remain byte-identical apart from permitted tag edits. Each conversion of a
reference carries its target ID and is audited against the full target context.
Before editing, inventory THREE reference classes across the whole packet:
existing internal Markdown links (including file-only links), raw numbered
references, and explicit named chapter/section references in prose. Resolve each
against the frozen book and registry. Numbered references are not the whole task.
Every existing link to a source file in the book manifest must become a link to
its reserved/defined stable target. Link explicit named chapter references while
preserving their exact caption/emphasis. Generic prose such as “these chapters”
or roadmap labels need not acquire an invented single destination. In the short
report list unresolved/ambiguous cases and why any candidate reference was left
as prose; do not report “none” from a numbered-reference-only scan.
Plain text and hyphenated names can identify chapters just as explicitly as
italicized titles. A mention is generic only if it does not identify a specific
book destination; typography alone is never a reason to leave it unlinked.
Plain planning labels (milestone A, C-H1, etc.) are not theorem/section numbers.
Generate the candidate by applying the declared edits to the exact excerpt,
including its final blank lines. Do not manually retype the candidate or trim it.

Later syntax classes are enabled only with an explicit reusable grammar/check,
not an unrestricted replacement kind. This is a small migration checker, not a
custom publisher. Use ordinary Quarto source and native rendering.

## Partial builds and acceptance

Check frozen hashes, prefix continuity, exact edit application, legal edits,
label inventory/position, registry collisions/intervals, all references, math
payload/counts and heading order. Negative tests must reject corruption,
duplicate/conflicting targets, bad ranges, reused IDs, unregistered links and
inconsistent fulfilled reservations; legitimate containment must pass.

Rendering is deferred by the user. During later integration only exact registered RESERVED
destinations may be unresolved; report every one explicitly. Other missing
links/citations/labels fail. A completed edition must have zero reservations.
Partial previews may display unresolved future reference numbers; this must
remain visible in their acceptance report, never presented as a finished book.

Sol reads each new packet's entire source/candidate, all edits, and each
target's actual source context, checks correspondence and references (including
ones never converted), and checks any changed mechanical safeguards with focused tests. Supply
complete frozen inputs, not worker/coordinator verdicts. Acceptance records the
exact reviewed hashes. Repairs follow `pilot_policy.md`: one consolidated list, worker preflight,
same-auditor surgical continuation. Check affected failure classes and retain
prior audit work. No duplicated full audit or speculative expansion.
