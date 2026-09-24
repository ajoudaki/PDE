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

There are only two auxiliary artifacts:

- `migration.py`: discovery, indexing, transformation, validation and a
  synthetic self-test;
- `migration_state.json`: source hashes and order, targets, references,
  literature links, output hashes, unresolved spans and check results.

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
   `C.4.5.2.R5` use the equation tag only inside the named section;
8. preserves external literature links and inventories them. It does not invent
   authors, dates or citation keys when the old source supplies no bibliography
   metadata;
9. preserves fenced code byte-for-byte and distinguishes clear code paths,
   modules and calls from candidate mathematics;
10. inventories every remaining legacy mathematical transcription by frozen
    coordinates as an inline code span, indented formula block or plain-text
    formula line;
11. reserves, without rendering, one stable future equation target for every
    high-confidence aligned label in those raw formula spans. Multiple numbered
    formulas in one indented Markdown block receive separate reservations.

Manual section numbers remain visible during this no-reorganization phase, so
automatic Quarto section numbering is disabled. Equation and formal-environment
numbering remains automatic.

## Refusal rules

The program leaves an occurrence unchanged and records it when several plausible
destinations remain. Proximity alone is accepted only when the nearest target is
strictly less than half the distance to the runner-up. No source-specific line
exception may be added merely to eliminate an unresolved count.

Plain/code-form mathematics is not rewritten by heuristics that could change an
operator, norm, derivative, index, quantifier or grouping. If a later model pass
is authorized, its only content-editing input is the recorded mathematical
transcription inventory with minimal local context. It does not receive whole
chapters and has no role in choosing labels or routine references. Ambiguous
prose references require an explicit destination mapping; they do not justify a
whole-block model rewrite.

A simple parenthesized tag such as `(2)` or `(F)` is local: it must share a
non-root outline ancestor with one uniquely selected formula target. Compound
tags carry their own scope. Parentheses inside raw subscripts or superscripts,
formula-label occurrences themselves, and endpoints of a parenthesized range
are never rewritten as independent references.

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
- reserved raw-formula targets remain undefined, and references to them remain
  unrendered until transcription;
- no remaining legacy TeX delimiters or equation tags outside code;
- balanced and complete formal environments;
- every repository-local link still resolves from its generated chapter to the
  same existing repository file;
- a successful synthetic self-test and Python compilation.

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
python studies/quarto_capability_pilot_20260921/migration.py build
```

The build prints only compact counts. Detailed coordinates remain in the single
state file and the generated chapter files.
