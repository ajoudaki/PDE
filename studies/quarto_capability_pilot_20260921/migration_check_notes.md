# Linear migration checker notes

`migration_check.py` is a bounded standard-library checker for the current linear
migration contract. Run it from any directory as

```text
python studies/quarto_capability_pilot_20260921/migration_check.py \
  studies/quarto_capability_pilot_20260921/linear_001_packet.json
```

Add `--output NEW_DIRECTORY` to retain `raw.diff` and `verification.json`.
The output directory must not already exist. The command prints JSON and exits
nonzero on any failure.

The checker verifies frozen source hashes and line counts, accepted-prefix
continuity and receipts, packet/target/edit schemas, deterministic IDs and
interval conflicts, exact edit replay, the first-packet edit grammars, frozen
heading coordinates and labels, math payload/order, reference IDs and link
destinations, remaining raw numbered references or internal `.md` links, and
the defined/reserved target inventory. Covered targets and headings cannot
remain unfulfilled. Label coordinates come from original edit offsets, so an
allowed blank-line insertion does not change their frozen coordinates.

The supported edit kinds remain deliberately limited to `label`,
`math-delimiter`, display-adjacent LF-only `whitespace`, and `reference`.
Single-line existing Markdown links and single-line plain captions can become
descriptive `.qmd#ID` links. Multiline captions and later migration syntax
classes are unsupported and fail closed.

These checks establish mechanical source correspondence. They do not establish
that a mechanically valid reference points to the scientifically correct
object, or that a target boundary is mathematically appropriate. The required
complete preservation audit remains responsible for those judgments.

Validation command:

```text
cd studies/quarto_capability_pilot_20260921
python -m unittest -v migration_check_tests.py
```

The 14 deterministic tests cover a valid packet, content corruption, wrong IDs
and destinations, same-kind collisions and crossing intervals, legitimate
cross-kind containment, a changed accepted registry, invalid heading placement,
unknown references, missing covered labels, shifted candidate lines after a
blank-line insertion, caption preservation for an existing Markdown link,
single-line section ranges, and normalized relative old-book link paths.

The first submitted `linear_001` packet was checked before acceptance and
correctly failed for an exact replay mismatch and the unconverted internal-book
link `NOTATION.md`. Evidence is retained under
`data/generated/quarto_capability_pilot_20260921/linear-checks/initial-submission/`.
