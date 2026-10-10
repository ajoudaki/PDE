# Candidate v1 layout findings

Root inspection of the rendered complete candidate PDF on 2026-10-10 found
two integration corrections. No frozen v1 source or review packet was changed.

1. The book deliberately disables section numbering. New `@sec-...` references
   therefore render as empty `Section` references in PDF, despite resolved
   targets and no build warning. Examples occur on pages 120 and 127 and in
   the updated chapter route. Use descriptive links to the existing section
   identifiers, following nearby maintained prose. Keep equation/theorem/
   lemma/proposition references native and preserve every anchor.
2. The new native definition environment renders as `Definition 0.0.1`.
   Existing PDF/LaTeX header configuration detaches theorem, lemma, proposition
   and corollary counters from unnumbered sections, but does not yet handle
   definitions (there are no prior native definitions). Add the analogous
   `counterwithout{definition}{section}` configuration in both formats.
   This changes no chapter/part list or mathematical claim.

The five inspected pages (118, 120, 127, 134, 136) otherwise show intact math,
proofs, code and the transition to the existing forest material. This bounded
inspection is not a whole-book typography audit. The final corrected edition
must be rendered and reviewed again; v1 structural success is insufficient.

The scientific reviewers are independently completing their original neutral
assignments. Their reports and inputs will remain retained. These author layout
findings have not been sent as guidance to either reviewer.

The format-only v2 full PDF rebuilt successfully. Root inspection of pages
118 and 120 verifies the corrected definition number and descriptive links.
It also shows the global table-to-card filter separating an instruction label
from its formula across a page break. Before freezing v3, the two new rule
tables were therefore recast as a compact instruction list and displayed
adjoint rules. The formulas are unchanged; the four adjoint displays gain
descriptive equation identifiers. These presentation changes join the fixed-seed
compiler correction in the next complete candidate; they are not applied to
either retained frozen edition.
