# Frozen migration packet v1: linear chapter opening

This is publishing maintenance, not mathematical research or promotion. Preserve
all mathematics, claims, qualifiers, prose, emphasis, order and heading levels.
Do not correct, improve, summarize or reorganize the source. Do not consult other
studies or the rest of the book. Report ambiguity instead of inventing content.

## Inputs, outputs and isolation

Read this file, `pilot_source.md` and `pilot_manifest.json` completely. They are
the entire assignment and source contract. All three are in this directory.
`pilot_source.md` is exactly lines 1–907 of `docs/linear_dynamics.md`, ending before
Section 5. Read required shared process instructions, but no study history,
previous outputs, reviewer findings, or web sources are needed.

Write only `pilot_linear.qmd` and `pilot_worker_report.md` in this directory.
Temporary scripts may use `data/generated/quarto_capability_pilot_20260921/pilot-worker/`.
Do not alter inputs, other files, Git state, maintained book/code or configuration.
Do not render: Astra owns build and verification. One fresh worker context handles
this one packet, then stops. Model: gpt-5.6-terra, reasoning effort: medium.

## Conversion rules

1. Keep line wrapping and blank lines when practical. Add the six exact mapping
   comments `<!-- source-block: ID -->` before the corresponding blocks listed
   in the manifest. They must occur exactly once and in source order. Do not
   rearrange statements, proofs, paragraphs, equations or sections.
2. Keep the chapter title and every section title/heading level. Remove only
   their old numeric prefixes and add the exact `sec-` IDs in the manifest.
   Automatic rendered numbers can differ from old numbers. Never derive a
   reference's target from its future displayed number.
3. Convert inline `\(...\)` to `$...$`, displays `\[...\]` to `$$...$$`.
   Preserve every character inside math except existing `\tag{...}` commands
   and the two terminal proof squares identified below. Do not combine/split
   displays or change aligned, matrix or other mathematical environments.
   For each tagged display, remove its tag and put ` {#eq-linear-TAG}` after
   its closing `$$`; exact IDs are in the manifest. Untagged displays stay
   unnumbered. Tags on the same line as mathematics must not delete that math.
4. Replace every prose reference `(1.3)`, `(2.A.2)`, etc to an in-scope equation
   by its single native `@eq-linear-...` reference. Replace all prose occurrences
   of `Theorem 1`, `Lemma 2.A`, `Lemma 2`, and `Corollary 3` by their native IDs.
   This includes the introduction. Match the longer `Lemma 2.A` before `Lemma 2`.
   Replace the whole old reference, including any old type name or parentheses;
   Quarto supplies the type name and number. Do not write `Equation @eq-...`
   or `Theorem @thm-...`. Do not replace mathematical numbers or equation bodies.
5. Convert the four formal statements to native fenced divs using the exact IDs
   and boundaries in the manifest. Example:

   ```markdown
   ::: {#thm-linear-population}
   ## global population and joint limit

   There are ...
   :::
   ```

   Use the original parenthesized title, verbatim, as the first `##` heading.
   The untitled Lemma 2.A has no invented title. Remove only the old bold
   statement prefix; retain all body prose and equations. Do not absorb a proof
   or explanatory paragraph into the statement. Such title headings are inside
   the div and do not alter the document's section hierarchy.
6. Convert the three complete proof spans in the manifest to `::: {.proof}`
   divs. Remove their old opening bold proof prefix. For the named proof use
   `::: {.proof name="of the singular expansion"}`. Preserve its later internal
   bold paragraph headings verbatim. Remove only the terminal `\(\square\)` at
   original lines 341 and 733; the proof environment supplies the end marker.
   Close proofs exactly at the manifest boundaries. Do not wrap other explanatory
   prose in a new proof. No `#proof-` ID on a proof div (known Quarto issue).
7. Preserve the two out-of-scope introductory section ranges literally. They
   are explicitly pending in the manifest. Preserve `[NOTATION.md](NOTATION.md)`;
   Astra will supply that original resource for the partial edition. Do not
   create fake target sections or claim the partial chapter is a complete book.
8. No paper citations occur in this packet. Do not add any or fabricate metadata.
   In later packets use standard `.bib` keys and `@key` / `[@key, p. N]`, with
   missing bibliographic information reported explicitly. Unsupported constructs
   (custom theorem types, automatic subparts, subequations) must be escalated,
   not silently converted to weaker substitutes. None is required in this packet.

## Before returning

Read the complete result against the source once. Check especially theorem/proof
boundaries, trailing scope restrictions, equations with same-line tags, references
to Lemma 2.A, all six mapping comments, and every reference destination.
Report actual inputs, output paths, anything ambiguous or omitted, and which
self-checks you performed. Freeze your output and stop. Do not assert independent
verification or full-book readiness.
