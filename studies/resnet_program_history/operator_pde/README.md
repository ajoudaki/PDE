# Operator–Galerkin PDE program

This phase contains an explicit finite-cutoff operator–Liouville PDE, whose
mathematical state contains no network-width coordinate at each fixed \(P\),
and a sequence of empirical consistency tests against finite networks.

## Phases

1. [`core`](core/) contains the direct PDE construction, dense comparison,
   mathematical checks, processed evidence, and independent audits. Start
   with [`core/CONJECTURE_REPORT.md`](core/CONJECTURE_REPORT.md) and
   [`core/REPORT.md`](core/REPORT.md).
2. [`generalization`](generalization/) contains the fixed-\(P=5\) transfer
   study. The authoritative interpretation is
   [`generalization/FINAL_REPORT.md`](generalization/FINAL_REPORT.md); its
   source, protocol, results, and checks now sit directly in the phase root.
3. [`activation_controls`](activation_controls/) is the self-contained
   activation-linearity falsification experiment. Its original source lineage
   and evidence seals are intentionally retained because the protocol checks
   them during reproduction.
4. [`rerun_2026-07-31`](rerun_2026-07-31/) contains the later smoke and
   canonical reproductions.

The three scientific source trees are deliberately phase-local. The core is
tanh-only, the transfer phase uses the normalized tanh/erf/atan registry, and
the activation-control phase extends that registry with identity and gain
controls. Their frozen protocols bind these differences by hash, so merging
them would be a scientific refactor rather than a cleanup.

Current reading: at fixed \(P\), the candidate PDE has exact internal
shared-transpose and projected-gradient identities and strong low-order
empirical performance against finite-network ensembles. Neither identification
with the ordered \(n\to\infty\), then \(L\to\infty\) limit nor
arbitrary-accuracy \(P\to\infty\) convergence is established.
