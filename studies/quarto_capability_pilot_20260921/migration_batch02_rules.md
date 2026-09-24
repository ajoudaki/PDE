# Packets 002–003: narrow additions to the v3 contract

The unchanged preservation, registry and full-audit rules still apply. Packet
002 is README lines 212–496; packet 003 is lines 497–742. Together they finish
the introduction. Work is isolated per packet; acceptance remains sequential.

- Preserve Mermaid diagram source and tables verbatim, except allowed reference
  replacements inside table cells. The Mermaid opening fence may change from
  ` ```mermaid` to ` ```{mermaid}` (without the illustrative leading spaces):
  edit kind `mermaid-fence`, replacing exactly the fence-language token. No
  diagram nodes, edges, captions, styles or source order may change.
- A `reference` may replace a numeric section reference with native `@ID`, also
  consuming its immediately preceding `Section`/`Sections` noun so Quarto does
  not double it. Numeric references include C.4, C.5, 6, 7.2, etc. Existing links
  with numeric captions follow the same rule. A mixed descriptive/numeric link
  caption may become the unchanged descriptive prefix followed by `@ID` (e.g.
  `Global nonlinear learning, Section C.4` -> `Global nonlinear learning, @ID`).
  Preserve punctuation, qualifications and parts/ranges. Do not substitute
  one section for a range or broaden a reference to a chapter to avoid lookup.
- Other existing internal links retain their exact descriptive captions and
  use their actual registry targets. All external paper URLs and their captions
  remain unchanged in these packets; these are already functioning references.
- Preserve inline-math payloads exactly, including newlines; only delimiters
  change. Do not mistake repeated inline delimiters for display delimiters.
- Workers must use `migration_check.apply_edits` to write their candidate and
  run the existing checker before handoff. For 003's parallel preparation, a
  prefix-continuity error is expected until reviewed 002 is accepted; all other
  errors must be resolved. Do not fabricate an accepted 002 receipt. Coordinator
  rebases 003 onto the accepted registry, drops only identical duplicate target
  proposals, and runs its full check before audit/acceptance.

No new general framework or additional scientific investigation. New exceptions
are reported concretely. Fresh full Astra preservation audits are retained.
