# Packet009 user override: typeset all mathematics

The user requires automatic renumbering and no plain-text/code-form mathematics
after migration. This supersedes the earlier rule preserving pseudo-math as code.
Convert notation only: mathematical meaning, every qualifier, scope, operator,
index, constant and reference destination must stay identical. Actual program
code, commands and file paths remain code. No proof repair or prose rewriting.

Use native Quarto math, existing eq IDs and automatic @eq references. No custom
float types, manual-number links, raw HTML, filters or publisher extensions.

Two narrowly declared edit classes supplement exact replay:

- inline-transcription: a nonempty source expression within one paragraph (plain text or
  its complete code span; physical soft line breaks are allowed) becomes one nonempty $...$ expression. Permitted also
  within a heading; only its mathematical notation changes.
- display-transcription: one complete source indented mathematical block becomes
  one $$...$$ display, using native aligned/gathered notation where needed.
  Keep every formula and its order. Remove only its literal original equation
  annotation. If numbered/referenced, include the existing native closing label
  and target field; its eq target spans the complete original indented block.
  Unnumbered/unreferenced blocks stay unnumbered.

For these edits, exact symbol spelling necessarily changes. Record every old/new
expression in the edit list and checker inventory for full Sol equivalence review.
Do not claim the mechanical checker proves semantic equivalence. It checks exact
source spans/replay, constrained output shapes, source block boundaries, unique
labels and literal original annotation versus reference-target identity.

Keep existing byte-preservation checks on everything else: compare original
math/code/headings with a candidate projection that reverses ONLY the explicitly
declared transcriptions at their replay-derived positions. Do not globally strip
or exempt changed mathematical content. Check labels, refs and delimiter balance
on the actual candidate. Original TeX displays still obey exact payload checks.

A numbered indented block is an additional valid frozen eq-source shape; derive
its original identifier from its terminal annotation, not a nearby occurrence.
Retain complete-block/overlap checks. Allow symbolic TeX tags such as R10 with
the same exact target-tag matching rule. Unsupported multi-number blocks require
a precise report, not an arbitrary target or discarded annotation.

Sol is the sole final reviewer and verifies all transcriptions and omissions.
Rendering remains deferred. Earlier accepted packets retain their old receipts;
their remaining pseudo-math must be revisited before declaring the whole edition
fully migrated. This is an explicit outstanding obligation, not accepted omission.
