# Working-paper integration and rendering check — 2026-10-07

## Scope and status

The user authorized replacing the working paper under `paper/` with this
study's integrated results, keeping canonical neural notation, short main-text
headlines, detailed appendix proofs, and a compiled, visually inspected PDF.
This revision is complete. It is not promotion into `docs/` or `code/`, formal
verification, or a new independent review of every scientific argument.
The preceding reconstruction and its scoped proof checks remain recorded in
[PROOF_COMPLETION_CHECK.md](PROOF_COMPLETION_CHECK.md).

The manuscript now has 14 main-text pages including references, a one-page
linked appendix guide, and 174 pages of detailed statements and proofs:
189 pages total. It is [paper/main.pdf](../../paper/main.pdf).

## Sources and presentation contract

The scientific source is the integrated `RESULT.md`, SHA256
`9c7b10dda810c13384ba9c85ffa70ca72b2be2475a7400377db028cf169f77f4`.
The old manuscript supplied its title, author, neural notation and existing
figure editions. The maintained book's index and notation contract, root
instructions, research workflow, and canonical-notation/neural-reference
instructions were applied. No other study's science was newly imported.

The only scientific-source edit during this paper conversion was a TeX
delimiter correction in FC.60: its final literal set brace now uses `\}`.
The same correction was made in `DECODER_FINITE_CONSTRUCTION.md`. No coefficient,
hypothesis or argument changed. Earlier frozen audit hashes are not rewritten
to imply a review of this new byte version.

The main text:

- Uses the paper's `W`, `z`, `h`, backward-response and readout notation.
  The appendix states the exact correspondence `A = W^(1)`.
- Keeps structural sample, width, dimension and Gram-gap parameters distinct.
  Main-text `c,C` depend only on activation and fixed depth.
- Normalizes errors by fixed nonzero label RMS and fixes confidence at 99%.
  Its normalized tolerance corresponds to absolute tolerance `Y epsilon` in
  the appendix. The full label allowance and arbitrary confidence remain there.
- Preserves cubic Legendre and quartic Harmonic sample/gap storage powers;
  it does not spend small labels to claim an improvement in those powers.
- Distinguishes coupled-reference compression from the Logarithmic decoder's
  independent-reference, dense-upper-certificate guarantee. Its particular
  dense certificate's unquantified structural coefficients are not hidden in
  activation/depth-only `C`.
- Separates moving state, fixed mixers, all retained storage, setup peak,
  training-stage versus complete-training work, and query workspace conventions.
- Retains eventual stochastic width qualifications for the first three models,
  the decoder's explicit gate and spanning assumption, finite-word evaluator
  and external-description/access costs, and the transient nature of the lower bound.
- States constructive mechanism and proof insights without treating them as
  substitute proofs. All detailed certificates and arguments are in the paper.

No `ell_n` abbreviation, boxed equations, missing-appendix fallback, old
conditional-paper theorem, or unsourced-note input remains in the new build.
The two old figures are explicitly illustrations. No training was rerun and
no empirical claim for Harmonic, Logarithmic, or practical setup speedup was added.

## Appendix coverage and conversion checks

The deterministic [converter](paper_appendix_build.mjs) builds a static
`paper/integrated_appendix.tex`. LaTeX never reads a study file. Scientific
Parts I–III, source lines 275–16128 inclusive, are retained. The separate
top-level summary is superseded by the new main text; Part IV's audit/provenance
records are not scientific premises.

Final conversion manifest:
`data/generated/integrated_general_compression_20261004/paper_rewrite_appendix_HOEdmj/conversion_manifest.json`.

Coverage inventory:

- 15,854 selected lines: 15,811 retained/accounted lines and 43 explicitly
  excluded HTML conversion comments or historical source-access lines.
- 1,099 displays, 5,085 inline math spans, 593 tagged equations.
- 16 tables with 106 data rows; all original row/column mappings retained.
- 344 source anchors, 937 emitted labels, 1,048 emitted references.
- Zero uncovered lines, unsupported markup, dangling references or duplicate labels.
- All IC/FC/WB material retained, including 91 IC, 62 FC and 17 WB named tags.

The converter modernizes 47 brace-delimited infix fractions and 20 binomials,
removes five equation boxes while preserving their argument groups, wraps
selected long definition chains, and stacks one wide complete-cost array
without losing entries. Long descriptive equation tags become numbered labels
with correspondingly rewritten references. Short named proof tags are retained.
These are formatting transformations, not new mathematics.

The standalone appendix compile also passed. Its separate 11pt wrapper has a
0.742pt prose overflow; that overflow is absent in the final combined manuscript.

## Bounded mathematical cross-checks

The source coauthor prepared the result interface and checked the construction
and abstract against the authorized integrated source. The construction
coauthor prepared the methods and cross-checked all main/results/cost text for
normalization, inverse powers, confidence, state inventories and execution costs.
The decoder coauthor assembled and checked the static appendix. Root reconciled
their findings and final presentation. These are collaborating, scoped checks,
not blind independent promotion reviews.

Concrete corrections included the abstract's `m >= 2` qualification, replacing
main-text depth factors by the declared constants, an explicit external retained
description cost for the decoder, normalized-versus-absolute tolerance mapping,
and removing repeated setup declarations. Source-backed paragraphs explain the
conditional Gram fluctuation mechanism and readout–residual cancellation.
The last editorial changes after cross-check were redundancy removal, those
checked insight paragraphs, the appendix guide, and typesetting-only changes.

## Build and visual checks

From `paper/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/home/amir/Codes/PDE/data/generated/integrated_general_compression_20261004/paper_rewrite_KFCZPBuv \
  main.tex
```

Final status: exit 0; 189-page PDF; zero LaTeX warnings, undefined references,
undefined citations, duplicate destinations, missing-character messages or
overfull boxes. There are 33 underfull diagnostics, chiefly ragged comparison
table alignments. The narrowest automatically fitted display is at scale 0.8762,
corresponding to approximately 8.76pt main math in the 10pt appendix, rather
than a half-size unreadable equation. Wide chains were broken before scaling.

Root rendered and inspected main pages 1–16 and representative appendix pages
26, 48, 63, 84, 94, 100, 113, 122, 126, 127, 147, 171, 174 and 189. These cover
headlines, inverse orders, storage/cost tables, both figures, navigation,
detailed certificates, the formerly wide cost display, each proof family,
the narrowest fitted FC display, initialization and the final page. Final
box-free page 84 and revised insight page 9 were inspected separately.
No clipped or overlapping content was observed. This is targeted visual
inspection plus whole-document compile diagnostics, not visual review of all
189 pages at full resolution.

All logs, manifests and rendered contact sheets are under the study's generated
namespace, principally `paper_rewrite_KFCZPBuv/`. The old unchanged compiled PDF
was moved recoverably to that directory as `previous-main.pdf` before installing
the replacement; its inherited file ownership prevented overwriting it in place.
Old proof modules, trial manuscripts and unused figures remain intact but are
not inputs to the revised paper.

The study structural checker also passes: 16,396 lines, 1,114 display pairs,
4,860 inline pairs, 606 tags, 345 anchors, 401 local links, zero failures.
`git diff --check` passes on the owned paper/study paths. No commit or staging
operation was requested or performed; unrelated work is preserved.

## Final artifact hashes

| Artifact | SHA256 |
|---|---|
| `paper/main.tex` | `249767c91cceeceee32dd9134f8c0c65fe069d1c6a8cca045bc4b89fa4e054a8` |
| `paper/results.tex` | `2a83b6f32b015f094b3b5773f6d970206e0be7d8af343fef0c5c61b361af8f5d` |
| `paper/methods.tex` | `3b67373412f2277b5613ccb2fa691b44552762f0e344e80e1716dc51b7ac0d1b` |
| `paper/costs.tex` | `ed1d981f46434ff310a634253f9afc3a3a2a1254238661f4912e37ab514f01e2` |
| `paper/integrated_appendix.tex` | `8893e63d99a4b072ea093ef34386653a33045ded9b472fa5a5c47e6d3261ede8` |
| `paper_appendix_build.mjs` | `3554e55e79d10e506fede64d6b0fc9d65b5a332f563e0143250e08757eb8ee6a` |
| `paper/main.pdf` | `065e01079006026957b1ddf99baed1bc021b5dffdd487d412b2b3f448d2d626b` |
