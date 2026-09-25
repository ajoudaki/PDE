# Deterministic whole-book migration contract

This contract supersedes the packet, worker and auditor workflows previously
used in this study. Those runs remain historical evidence only.

## Principle

The maintained Markdown book is frozen input. One standard-library Python
program performs every transformation that follows from syntax or from a unique
book target. It processes complete chapters in source order and writes a
separate Quarto candidate. It never edits the old book, invokes a model, calls a
renderer, or guesses an ambiguous mathematical meaning.

Corrections belong in general rules in `migration.py`. Do not patch an isolated
generated occurrence. Rebuilding must reproduce the entire candidate from the
same source hashes.

## Active artifacts

There are four durable auxiliary artifacts:

- `migration.py`: discovery, indexing, transformation, validation and a
  synthetic self-test;
- `migration_state.json`: source hashes and order, targets, references,
  literature links, output hashes, unresolved spans and check results;
- `migration_decisions.json`: exact source-coordinate math replacements, model
  provenance, reviewed reference overrides, verified bibliography entries, and
  compact-review results;
- `pdf_breakable_tables.lua`: the print-only layout filter copied verbatim into
  the generated book and hashed in the migration state.

The four compact prompts, schemas, raw responses and call receipts are generated
scratch under `data/generated/quarto_capability_pilot_20260921/math-transcription01/`.
They are not book sources. `migration.py` prepares and ingests them but never
invokes a model.

The candidate book, including `_quarto.yml`, is generated under the repository's
top-level `new_doc/` directory. This keeps the same relative position to `code/`
as the original `docs/` directory. The maintained `code/README.md` is not a book
chapter and remains outside the migration.

## Deterministic responsibilities

The program:

1. discovers the maintained theory chapters from `docs/`, beginning with the
   reading guide and notation chapter; it does not ingest code documentation;
2. assigns stable typed IDs from object kind, source path and frozen source line;
3. labels Markdown headings, old HTML anchors and explicitly numbered bold
   subsections, including nested plain-numbered bold units, without changing
   their order;
4. converts `\[...\]` displays to Quarto `$$...$$` blocks, removes each old
   `\tag{...}`, and attaches one automatic `eq-` target while checking the
   mathematical payload byte-for-byte;
5. converts legacy `\(...\)` delimiters, including multiline inline math, while
   leaving the TeX payload unchanged;
6. converts explicit theorem, lemma, proposition, corollary and proof markers to
   native Quarto environments, including the book's named and prefixed caption
   variants and literal `Proof.` markers; named symbolic statements such as
   `(F)` receive ordinary stable anchors in their actual local outline scope;
7. resolves explicit links and numbered references only when the destination is
   unique globally, unique in local outline scope, or has a uniquely dominant
   nearby target; section wording is preserved in an ordinary stable link.
   Explicit chapter scope can continue across lines in one paragraph; local
   proof-unit abbreviations, restarted coordinate runs and relative descendants
   such as `III.V` followed by `V.3` are resolved only within their common
   outline parent. Qualified local equation tokens such as
   `C.4.5.2.R5` use the equation tag only inside the named section. Local
   abbreviations such as `E21` may resolve a target ending in `.E21` only in a
   unique shared outline scope; only a globally unique fully qualified tag may
   cross chapters. Parenthesized equation ranges use the same endpoint rules;
   every endpoint in a range activates together only after all are defined;
8. preserves external literature links. Bibliography records and citation keys
   are added only through reviewed exact-source decisions with verified metadata;
9. preserves fenced code byte-for-byte and distinguishes clear code paths,
   modules and calls from candidate mathematics;
10. without a decision file, inventories every remaining legacy mathematical transcription by frozen
    coordinates as an inline code span, indented formula block or plain-text
    formula line;
11. reserves, without rendering, one stable future equation target for every
    high-confidence aligned label in those raw formula spans. Multiple numbered
    formulas in one indented Markdown block receive separate reservations;
12. with the frozen decision file, verifies every exact source span, preserves
    prose outside selected spans, activates every reserved target and reference,
    and refuses incomplete, stale, overlapping or structurally invalid decisions.
    A math span may not overlap any automatically resolved or reviewed reference.

Manual section numbers remain visible during this no-reorganization phase, so
automatic Quarto section numbering is disabled. Equation and formal-environment
numbering remains automatic and global. The generated LaTeX configuration
removes hidden chapter/section resets so unnumbered source headings cannot
create duplicate PDF destinations.

## Refusal rules

The program leaves an occurrence unchanged and records it when several plausible
destinations remain. Proximity alone is accepted only when the nearest target is
strictly less than half the distance to the runner-up. No source-specific line
exception may be added merely to eliminate an unresolved count.

The model's only content-editing input is the recorded mathematical transcription
inventory with bounded local context. It does not receive whole chapters and has
no role in choosing labels or references. Its output is data, never a file edit.
The ingester discards spans copied from context or overlapping protected code or
references. A deterministic lexer may supply only residual pseudo-LaTeX tokens
whose exact boundaries and translation are syntactically fixed. Ambiguous prose
references require an explicit destination mapping; they do not justify a
whole-block model rewrite.

A simple parenthesized tag such as `(2)` or `(F)` is local: it must share a
non-root outline ancestor with one uniquely selected formula target. Compound
tags carry their own scope. Parentheses inside raw subscripts or superscripts,
formula-label occurrences themselves, and endpoints of a parenthesized range
are never rewritten as independent references.

Closed inline formulas mask only their own delimiters and payload. They may not
hide later prose on the same line. A prime followed by a parenthesized number,
as in `m'(1)`, is a function argument rather than an equation citation. Reviewed
LaTeX payloads must also eliminate pseudo-indices such as `H1_N`, distinguish
indices from indicator functions, and retain the exact source mathematics.

A theorem-, lemma-, proposition- or corollary-style phrase may fall back to a
numbered section only when the section shares its local unit, names that formal
kind, or opens with that formal environment. A coincidentally numbered remote
section is not enough.

## Checks

Every build requires:

- unchanged source hashes throughout the run;
- unique target definitions and no undefined generated references;
- exact preservation of fenced code;
- exact display payload and label correspondence;
- without decisions, reserved raw-formula targets remain undefined and their
  references remain unrendered; with decisions, every reservation is defined
  exactly once and every formerly reserved reference activates;
- no remaining legacy TeX delimiters or equation tags outside code;
- no residual raw-math signals in generated prose and no reviewed pseudo-symbol
  syntax in LaTeX payloads;
- no mathematical decision overlapping a resolvable reference;
- balanced and complete formal environments;
- every repository-local link still resolves from its generated chapter to the
  same existing repository file;
- every reviewed citation key appears in the generated bibliography and at its
  exact frozen source link;
- a successful synthetic self-test and Python compilation.

The one final publishing check additionally requires byte-identical regeneration
in a fresh directory, successful HTML/PDF/LaTeX renders, an independent compile
of the exported LaTeX, no missing targets/citations/glyphs or duplicate PDF
destinations, and representative visual inspection. Print-only line wrapping
must follow `migration_render_rules.md`; it may add layout breaks but may not
rewrite a mathematical expression.

Mechanical fixtures cover equations, formal environments, sections, resolved
references and each unresolved-math form. Final inspection also uses fresh
uniform samples over reference records, reservations, unresolved math and
generated character positions. A discovered fault changes a reusable rule and
triggers one whole-book rebuild. Repeated ad hoc review rounds and packet-by-packet
model audits are not part of this workflow.

## Commands

From the repository root:

```sh
python studies/quarto_capability_pilot_20260921/migration.py self-test
python studies/quarto_capability_pilot_20260921/migration.py prepare-math
python studies/quarto_capability_pilot_20260921/migration.py ingest-math
python studies/quarto_capability_pilot_20260921/migration.py build \
  --decisions studies/quarto_capability_pilot_20260921/migration_decisions.json
```

The build prints only compact counts. Detailed coordinates remain in the single
state file and the generated chapter files.
