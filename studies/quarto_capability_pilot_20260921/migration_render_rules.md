# Print-layout rules for the generated book

The frozen source, migrated Markdown, edit replay and registry rules remain
unchanged. This amendment concerns presentation in PDF and exported LaTeX only.

- Generated diagrams must fit the available page width and height without
  clipping; preserve their full source, aspect ratio, nodes and edges.
- Markdown tables remain tables in source and HTML. Where print tables contain
  cells too long to fit on a page, a small reusable format-only filter may emit
  page-breakable row blocks. Preserve every header, cell, caption, inline link,
  formula and row/column order, with each cell's column identity explicit. Do
  not shorten text, shrink it to unreadability or special-case scientific names.
- Unsupported table structures must remain unchanged and be reported for review,
  rather than silently lose spans, captions or identifiers. Inspect actual PDF
  pages, including the longest rows; a successful build alone is insufficient.

This is a narrow exception to the pilot's original no-custom-filter rule,
justified by observed clipping in the standard print renderer. It is not
reorganization or permission to rewrite source. The deterministic builder copies
the filter into `new_doc/` and records its hash. Earlier failed render probes and
their exact inputs remain generated evidence.

## Flat multi-relation displays (packets 005–006)

The first scientific packet exposed actual off-page loss in a long display.
For PDF and exported LaTeX only, a flat display with at least two top-level
comma-plus-`\quad` separators immediately followed by a source newline may
be laid out as `gathered` rows at those existing breaks. Retain every original
character, including separators and whitespace; insert only the row breaks
and the enclosing layout environment. Do not split inside braces. Displays
with existing environments, explicit row breaks, alignment or `\left`/`\right`
remain unchanged. No equation-specific IDs, algebra rewriting or font shrinking.

Freeze a mechanical inventory of affected displays across the assembled prefix.
Earlier accepted displays that do not match require no repeated visual audit;
inspect actual affected pages and the new packet. The source Markdown, HTML,
formula comparison and registry remain unchanged. This handles a bounded layout
pattern, not every possible overflowing equation; other content loss still blocks.

## Whole-book completion

The complete book exposed the same problem in a few additional structural forms.
For PDF and exported LaTeX only, the maintained filter may:

- break long flat displays at top-level commas, explicit spacing separators, or
  addition signs, never inside TeX groups or sized delimiters;
- place an already delimited long tuple or set-builder body in `gathered`, while
  preserving the enclosing delimiters and every mathematical token;
- replace an invisible `\right.`/`\left.` display join by one `gathered` row
  break, and split a long one-column row inside `aligned` at addition signs;
- add `\allowbreak` opportunities to long inline formulas at existing safe
  boundaries;
- use `scriptsize` for a wide six-or-more-column mathematical array and wrap a
  raw verbatim command line, without deleting or abbreviating content.

The filter treats nested matrix/alignment environments as opaque when finding an
outer break. It does not break between command arguments, inside braces, or at a
source newline. Unsupported structures remain unchanged. Acceptance requires an
independent XeLaTeX compile and visual inspection of representative affected
pages; renderer success alone is insufficient.
