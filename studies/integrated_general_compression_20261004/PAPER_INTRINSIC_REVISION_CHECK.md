# Intrinsic-variability paper revision: completion and checks

2026-10-07. This records a working-paper revision, not promotion to the
maintained Quarto book, formal verification, or a new independent review
of every source proof.

## Rollback checkpoint and scope

Before changing the scientific statements or exposition, commit
2c27cbc68c0da734a921679ed3097bfaa2b44179 saved the complete current paper,
PDF, integrated result and study-owned proof sources. The common Git-writer
lock was held. Unrelated changes in the shared checkout were excluded.
The checkpoint intentionally preserved the then-current generated
appendix's harmless extra EOF blank line; this revision removes it in the
deterministic converter.

This revision changes the main accuracy contract, theorem organization,
mechanism exposition, cost presentation and the corresponding appendix.
It does not change the dense architecture, label allowance, activation
class, original Legendre/Harmonic certificates, or finite decoder algorithm.
No new training experiment was run. The maintained book and code were
not changed.

## Mathematical change

The common benchmark is the 99.99% quantile of the actual complete
independent-dense discrepancy; each model's headline confidence is at
least 99%. This is neither an analytic upper envelope nor the discrepancy
of a particular realized pair.

The complete new decoder proof selects a regular deterministic center
from the pairwise law, transfers fixed-code interval tests using the
existing scalar transcript law, amplifies complete members, and extends
through the existing input/time codes and fitted tail. At general failure
\(\delta\), the certified error is
\(2b_n(\delta)+A_{\rm num}Yn^{-10}\), where the actual pairwise
quantile has tail \(\delta/32\). Its failure is at most \(3\delta/16\).
At the paper's fixed quantile, the exact bound is
\(1/5000+1/800=0.00145<0.01\). No algorithm computes the center or quantile.

For \(m\ge2\) and fixed nonzero labels, the proved dense lower bound
eventually absorbs the numerical term and gives factor three. This
consequence inherits the unquantified lower-bound onset. The original
explicit finite-width gates still certify the additive intrinsic bound
and the analytic absolute bound. The one-sample zero-variability example
is included, so the additive term is not silently erased over the original
scope. Zero labels retain their exact zero branch.

The analytic decoder envelope was renamed from \(b_n\) to \(B_n\)
only in the relevant decoder sections and mirrored source fragments.
Unrelated proof-local Harmonic tube radii were not globally renamed.
All three prescribed sizes appear in one main theorem, with their internal
orders confined to the appendix's proof and mechanism descriptions.
Legendre remains \(n^{5/4+o(1)}\) learned coordinates plus fixed dense
mixers; it is not relabeled linear. The cubic/quartic gap powers remain.
The Logarithmic word power remains six, with an extra logarithm in bits.

## Scoped proof and presentation checks

- The complete candidate proof is preserved in
  [VARIABILITY_DECODER_REFINEMENT.md](VARIABILITY_DECODER_REFINEMENT.md).
- [VARIABILITY_DECODER_REFINEMENT_CHECK.md](VARIABILITY_DECODER_REFINEMENT_CHECK.md)
  checks the regular center, per-code law transfer, exact failure budgets,
  numerical remainder, and eventual absorption against the embedded finite
  source/decoder interfaces. It reports no substantive gap in this refinement.
- [PAPER_HEADLINE_REFINEMENT_CHECK.md](PAPER_HEADLINE_REFINEMENT_CHECK.md)
  checks the three size substitutions, label handling, confidence conventions,
  inventories, training/query substitutions and Harmonic setup specialization.
- The lead incorporated both nonblocking recommendations: the cost table
  explicitly retains the eventual threshold, and the theorem says
  prescribed state bounds instead of suggesting a proved minimum.
- A final read-only consistency pass confirmed the integrated candidate
  and joint proof. The realized-pair upper/lower statement now explicitly
  allocates failure \(10^{-4}\) and \(1/200\), respectively.

The canonical-notation and rigorous-proof workflows guided the minimal
main notation, absolute-error convention, explicit confidence relation and
separation of quantile from realized discrepancy. The bounded research
workflow separated the actual new lemma from unchanged source premises.
The appendix contains the complete new proof and all inherited scientific
dependencies; the audit reports are records, not mathematical premises.

## Mechanical and rendered checks

The study integration checker verifies balanced mathematics, unique tags
and anchors, all local links, matching source fragments, and exact inclusion
of the audited variability proof (apart from deeper headings and the
uncentered-second-moment terminology clarification).

The deterministic converter includes every scientific line of Parts I–III,
omitting only conversion/history comments. The resulting static appendix
does not read a study file during LaTeX compilation. Its coverage manifest
records all displays, inline formulas, tags, tables, anchors and references.
The complete manuscript is compiled with latexmk and the included bibliography.

Build and rendering directory:

data/generated/integrated_general_compression_20261004/paper_intrinsic_D3pc1mpR/

Final checks passed:

- Integration checker: 16,979 source lines, 1,143 display pairs, 5,055 inline
  pairs, 621 unique equation tags, 347 explicit anchors, 407 local links;
  no failures. The full audited candidate is mechanically matched.
- Static conversion: scientific lines 350–16,700; 16,308 covered content
  lines and 43 explicitly recorded conversion/history-comment lines;
  1,125 displays, 5,250 inline expressions, 606 equation tags, 16 tables
  with 106 rows, 346 anchors, 952 emitted labels and 1,071 references.
  No missing or dangling reference, uncovered line or unsupported markup.
- The isolated appendix compiled successfully before the final cosmetic
  split of its two-definition (VD.1) display. The combined paper compiled
  successfully afterward with all cross-references and bibliography resolved.
- Final PDF: 194 pages; 13 main-text/reference pages, one appendix guide,
  then the complete scientific appendix. No LaTeX warnings or overfull
  boxes; 33 underfull alignment diagnostics remain in intentionally
  ragged tables, without clipped content.
- Rendered inspection covered the title/setup, joint theorem, intrinsic
  comparison, all three mechanism explanations, both cost tables,
  discussion/references and appendix guide. The new proof and order
  derivations were inspected on pages 141–147. The longest new display
  was split into two preserved definitions for legibility.
- Scoped Git whitespace checks passed. The final generated PDF was installed
  at paper/main.pdf and its bytes match the checked build. The earlier
  checkpoint remains untouched. This revision was initially left uncommitted
  for review; the user subsequently authorized its commit and push.

The final conversion manifest is under
data/generated/integrated_general_compression_20261004/paper_rewrite_appendix_TLim3K/.
The main build, auxiliary files and rendered images are in the directory above.
No compiled artifact is needed to reconstruct the mathematical argument:
the static source, bibliography and included figures compile directly.

## Final source and artifact hashes

| File | SHA-256 |
|---|---|
| paper/main.tex | a7c09bbbfaa5214520f1c9316ec61536f5e74b6b1685de9e2c7c0316cf8a00f8 |
| paper/results.tex | 348e8e44777944557bb161aebbce3de9cbfdca4e8e1331f0fab072e881de8606 |
| paper/methods.tex | 9eeec414767eaa02c454530be5e8d42ba6b64cb7576dbaee01f973b5097de7af |
| paper/costs.tex | 22e3b316395a06042481b3686b1d94eb323a6f80be275d14aec998e13bbca543 |
| paper/integrated_appendix.tex | 5d5c0c6ebe61d594f516eccc90360a7ca40cfa030656fa5af8452bcea5b7f137 |
| paper/main.pdf | 54e4dcd4e8eacf486b60b55ffe5905825dbb8b2a92ac692c8de3d2e7e839c173 |
| RESULT.md | 5750d944b25629874764e333cfec5ff0d4294fbf4734ad4d9107bfc7b23af5c9 |
| paper_appendix_build.mjs | c169b61fa946f872168d722fc005b96ff9a099d6cd699a9ce776cc8bdc4b05e0 |
