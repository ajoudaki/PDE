# Neural tangent hierarchy as quantitative compression

## Scope

Started 2026-10-10 in response to a request for a theorem, rather than a
heuristic, quantifying NTH retained storage at dense-run variability accuracy.
Width is `n`, training sample count `m`, input dimension `d`, and hidden depth
`L`. Distinguish the published NTK-parameterized construction from the
project's feature-learning parameterization. Do not transfer bounds between
them or identify an accuracy upper bound with dense-run variability.

Permitted scientific inputs: the maintained `docs/` and directly relevant
published NTH sources and their proofs. No other study is being imported.
This work does not edit the paper, maintained book, code, or experiments.

## Current result

- [RESULT.md](RESULT.md): exact online state counts, literal source theorem's
  width/accuracy consequences, a fully proved conditional finite-panel
  order-two comparison, and proved qualifications concerning data
  conditioning and the native dense-pair benchmark.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): full primary-source scope/proof audit by
  the scoped `nth_explicit_source` agent.

The requested unconditional same-scope theorem is **not closed**. The source
uses another parameterization and readout, extra raw-input conditioning,
unquantified fixed-background constants, and finite-horizon training RMS.
Its inspected proof also has unresolved steps listed in the audit. The
previous conversational geometric hierarchy-tail forecast is withdrawn as
a theorem claim; no `m^{O(log n)}` feature-learning guarantee was proved.

## Sources

- Huang and Yau, *Dynamics of Deep Neural Networks and Neural Tangent
  Hierarchy*, ICML 2020, main paper and full arXiv appendix:
  https://proceedings.mlr.press/v119/huang20l/huang20l.pdf
  https://arxiv.org/pdf/1909.08156
- `docs/index.qmd` and `docs/notation.qmd` for the maintained target and
  notation; `docs/08b-trajectory-compression.qmd`, setup and headline section,
  for the exact canonical model and comparison contract. No compression
  theorem from that chapter was imported as a proof dependency.

## Check status

Root authored the result and read the relevant full source statements and
Appendices A–C; the scoped agent read both source PDFs completely. A bounded
second check by that agent verified the new deterministic statements and
proofs, with three clarifications incorporated. See the result's check
record. This is not a promotion audit and does not certify the source's
unresolved stochastic estimates. No experiments, commits, paper changes,
maintained-book changes, or broad repository changes were made.

Next meaningful proof obligation, if continued: establish mixed-kernel source
bounds with explicit depth, activation, data and confidence dependence in a
precisely chosen network parameterization. Do not claim the existing
conditional transfer has supplied those hypotheses.
