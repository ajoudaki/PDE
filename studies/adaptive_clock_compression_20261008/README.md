# Adaptive clocks for finite-panel response compression

## Contract

New research direction requested 2026-10-08: investigate whether loss-,
residual- or feature-motion time coordinates improve the existing temporal
source rank sufficiently to reduce retained finite-panel model storage from
log(en)^5 toward log(en)^2. Preserve the canonical Gaussian, zero-readout,
fixed-depth, nonlinear neural gradient flow, analytic activation class
(bounded derivative, possibly unbounded values), finite training/passive
panel, existing label allowance and positive feature-Gram gap. Comparisons
must remain at the same physical time, through the fitted endpoint.

Distinguish a clock used only to construct an approximation basis from a
change of the deployed optimizer. The latter must retain the inverse clock
and its costs to preserve physical-time predictions. Do not trade a uniform
panel error for a weighted temporal average, treat stable toy ODEs as neural
counterexamples, or assume endpoint analyticity from exponential real decay.
No new empirical training campaign, paper rewrite or promotion is requested.

## Sources and authority

The user explicitly approved directly relevant proofs in
initialization_panel_compression_20261008,
finite_panel_absolute_compression_20261005, and
integrated_general_compression_20261004. The paper and established docs/code
are also in scope. Read only the relevant source/proof dependencies; earlier
experiments do not prove the proposed exponent improvement. The current
paper and existing studies remain unchanged. Required research, rigorous
proof and canonical-notation skills are used.

## Bounded initial investigation

1. Lead: reconstruct the exact temporal rank ledger and locate each width
   logarithm; synthesize checked clock identities, a candidate improved
   approximation route, and the exact remaining proof obligations.
2. Clock-geometry route: finite-interval clocks, endpoint regularity,
   representational invariance, physical-time accounting and simple exact
   stress examples. Own CLOCK_GEOMETRY.md only.
3. Approximation route: investigate adaptive intervals / decay-adapted source
   approximation from precisely stated existing analytic and tail estimates;
   derive a stronger bound if possible, otherwise isolate what additional
   analytic estimate is required. Own ADAPTIVE_APPROXIMATION.md only.

Routes start independently with bounded assigned inputs, then outputs are
reconstructed before synthesis. One initial round and one focused check;
no open-ended proof campaign or numerical sweep. A log^2 n claim requires a
complete rank O(log n) bound for all necessary forward/backward/initialized
source families, unchanged accuracy/stability/provenance hypotheses, and
fully counted squared metric/mixer storage. A conditional theorem or a
generic ODE obstruction is reported as such, not as resolution of the neural
question. No assumption that the requested improvement must exist.

## Current results

The continued investigation's synthesis is [RESULT.md](RESULT.md).
The residual-adapted domain now proves sufficient neural retained storage
of third logarithmic power, with the same finite-panel scope and full
label allowance. The exact bound retains both its fourth-power label/gap
coefficient and a lower-logarithm term with a different gap coefficient.
The paper and previous integrated compression document are unchanged;
this result has not been promoted. Near-second-power storage remains open.

| Claim | Status and evidence |
|---|---|
| Existing source-rank exponent is \(1+1/2+1=5/2\); quadratic retained interactions give 5 | Reconstructed from the authorized source interface in [SOURCE_RANK_LEDGER.md](SOURCE_RANK_LEDGER.md) |
| Onto time reparameterization preserves optimal uniform linear-source rank | Exact; independent derivations in the ledger and [CLOCK_GEOMETRY.md](CLOCK_GEOMETRY.md) |
| Finite real motion and exponential loss decay force analytic compactification of every response | False for generic analytic gradient systems; exact two-mode example in the geometry note, explicitly not a neural counterexample |
| A scalar residual can be cancelled by a feature clock, giving analytic continuation through fitting at fixed width | Proved under the stated analytic and positive-Gram hypotheses in the geometry note; width-uniform constants remain open |
| Current strip, tail and speed estimates alone imply improved rank | False for generic source curves; explicit \(\Omega((\log n)^{5/2})\) rank example with uniformly bounded coordinates, independently reconstructed in [RANK_CHECK.md](RANK_CHECK.md) |
| Enlarged complex domains yield lower logarithmic storage powers | Approximation theorems in [ADAPTIVE_APPROXIMATION.md](ADAPTIVE_APPROXIMATION.md), with full rank/storage and initialized-image pairing; stronger second-power hypotheses remain conditional |
| The actual neural sources possess the residual-adapted flaring domain with unchanged label qualification | Proved in [FLARING_ROUTE.md](FLARING_ROUTE.md), internally reconstructed in [FLARING_CHECK.md](FLARING_CHECK.md); yields third-power retained storage |
| A complex sector can be obtained at late times without a new label restriction | Proved in [SECTOR_ROUTE.md](SECTOR_ROUTE.md); onset of order log n is too late to improve early rank |
| Near-second-power retained storage | Open; early source cost remains unresolved |
| A switch from Chebyshev to Legendre alone improves the best uniform polynomial approximation space | False; the degree spaces coincide |

These new deterministic claims and conditional implications are internally
checked, not promoted results. They do not freshly audit every dependency
of the old compression theorem. The exact-real coordinate convention,
finite-panel scope, full label allowance, fixed-problem width asymptotics,
initialization-only information and all-time physical-clock comparison
remain explicit.

## Checks and provenance

The two initial routes were fresh and independent until each froze its
first candidate. Their permitted inputs and actual read coverage are
recorded in their notes. The lead read both complete candidates and
reconstructed the equations, approximation tails, panel counts, exact
forward/transpose image pairing and scope distinctions.

A third fresh prompt-only checker reconstructed the source-rank example,
including its strengthened discrete-cosine version. The complete
derivation is retained in RANK_CHECK.md; it checks the complex Hermitian
norm, derivative bound, amplitude/error ratio, projection trace,
coordinate envelope and restriction to generic curves. The geometry
route subsequently checked the frozen rank and approximation synthesis;
its checked hashes and narrower read scope appear in its final section.

The original 533-line approximation candidate, before the final focused
neural-domain investigation, has SHA-256
671fcb7f0e9863d3939eb9b5bbc0fabc3f0a75a14a772ea0fe3615544247a235.
The checked root rank ledger has SHA-256
98387ad80255c1452562dc0d0e78b00e9ceca690ecf67024c3bb77c0fc102edd;
the separate rank reconstruction has SHA-256
468b918fb3d98fbf45b5bdf506037bf26862e2dc237000d1fc219c43cc78e7c9.
Any further exploratory appendix in the approximation route is separate
from that frozen cross-check and must keep its assumptions explicit.

The final approximation note including Section 6 has SHA-256
fd6daf74a3c95678bcfe8bd29aafedd9e9b22d6d3afe14dc8c829c96065f7b44.
The lead read all of that section and reconstructed its conditional
deterministic algebra: mobility normalization, product derivatives,
complex transpose norms, vertical frozen-Gram unitarity, the double
residual integral and radius substitution. This checks the implication
under its displayed contour hypotheses, not those hypotheses on an
enlarged stochastic neural domain. The additional source attribution
and uncompleted independent-cavity bridge are documented there; they
were not an accepted new probability theorem at that initial stopping
point. The authorized continuation below closes that particular source
bridge on the flaring domain; it does not prove the stronger domains.

Primary input snapshots:

- initialization_panel_compression_20261008/PANEL_BOUND.md:
  9622e6938eb19eb31965f004fab9b3f20b3ce544e135eb9f2fd72631a86051d9.
- finite_panel_absolute_compression_20261005/PANEL_SOURCE.md:
  ca1066cf168829bea642db013a4fbc24166b224df0731783a51b4c85e4fdbaed.
- paper/integrated_appendix.tex, relevant sections only:
  5d5c0c6ebe61d594f516eccc90360a7ca40cfa030656fa5af8452bcea5b7f137.

No experiment was run and no empirical result is upgraded. This study
contains proofs and source analysis only. No existing tracked document,
code or paper file was edited. The final read-only unsandboxed Git status
showed only this new study untracked; sandbox-only apparent changes to
two unreadable migration files were not acted upon.

## Initial stopping point, before the authorized continuation

The neural \((\log n)^2\) question remains open. The decisive missing
step is stronger regularity for the entire actual neural response family,
including backward responses and both initialized mixer directions—not
just a faster scalar clock or real loss decay. Conditional enlarged-domain
counts do not supply that step.

The initial route round, bounded synthesis checks and focused inspection
of the enlarged-domain dependency are complete. That final inspection
supplied a conditional stopped-propagator estimate, but did not close
the stochastic source-domain extension. The investigation stops with
that precise remaining obligation. Further development requires a new
request; these notes do not reopen the empirical campaign or alter the
existing headline.

## Authorized continuation: near-second power, then third power

The user's next request explicitly reopens this proof direction. First
seek retained storage of order log(en)^2 times iterated logarithms under
the unchanged scope; if that does not close after a serious attempt,
pursue the log(en)^3 expanding-domain route. A conditional approximation
count alone is not completion. No neural exponent is upgraded until the
source event, finite initialization provenance, rank selection and
all-time comparison have all been checked.

The bounded continuation has two independent initial routes: a
sector/analytic-flow route (SECTOR_ROUTE.md), and a residual-adapted
stopped-domain route (FLARING_ROUTE.md). The lead works on the source
dependencies and synthesis. Each must produce an actual proved lemma
or identify the exact unclosed implication. Two proof rounds and one
focused reconstruction are the initial stopping budget; no training
campaign or paper edit is authorized. Study-scoped results retain the
existing sample/depth/label qualifications and do not use a smaller label
cap to manufacture a better exponent.

The separate request for a more intrinsic alternative to coordinate
selection is kept in selector_free_response_compression_20261008.
The user allows the questions to interact if there is a genuine shared
construction. Only the explicitly relevant prior source/proof interfaces
and this continuation's identified mathematical results may cross those
two contexts; unrelated studies remain out of scope.

## Completed continuation and checks

The two fresh routes froze their candidates independently. The sector
route proved a late-sector lemma, but did not reach the desired exponent.
The flaring route repaired the causal order of the source bootstrap:
provisional response stops imply sharp derivatives, which bound the
negative-Gram products before insertion. Its independently clipped
domains then permit the original common-cavity moment removal.

The lead read both complete candidates. It reconstructed the sector
specialization against the complete relevant real-fitting proof, and
checked the flaring derivative, imaginary-time propagation, independent
clipping, Gaussian moment transfer, adaptive panel count, inventory and
all-time comparison. It read the complete relevant unbounded-source and
finite-query bridge files, the original complete insertion proof's
relevant paper section, and the authorized rank/runtime interfaces.

The scoped checker reconstructed the full flaring candidate and its
named dependency files; its exact scope and hashes are recorded in
FLARING_CHECK.md. A further scoped check verified the selection and
finite-anchor interfaces. The checker reused an existing context, so
this is internal reconstruction, not a fresh isolated promotion review.
Its conclusion is a scoped PASS, with qualitative width onset,
fixed-parameter asymptotics and unrestricted preprocessing cost explicit.

The frozen flaring candidate checked there had SHA-256
994a60c55b65b2a1518e8317e6f5550bbb6202f0ed205a014338e33f5dc8a0eb.
The lead then incorporated the report's finite-derivative compiler lemma,
made its scaled-coefficient error allocation explicit, corrected one
doubled comma and updated the status language. The resulting proof has
SHA-256 688efd057daee248d16ef9ddb78c080f815ef6cd5cc6e0ef0b3eeac505886ca7.
The check report has SHA-256
c41e1678978803d2f875d4e1e41e1c01342b2f39f4f3c141c1b51e538d1fd7da.
The sector candidate checked by the lead has SHA-256
332fe2e4e0a01f6272e93952fb5f0b7b5504326d3fbf7d1bcbd1b4cc2aff7af6.

The current result and explicit beta-envelope are in RESULT.md; its
algebra keeps the new gap-dependent term and does not trade the small
label cap for a lower displayed sample power. Target error Y/n is
available at the same third logarithmic power and is negligible relative
to the inherited dense-pair panel lower bound for m>=2.

No experiment, implementation, paper edit or Git write was made. The
final read-only Git status showed only this study and the new
selector_free_response_compression_20261008 study as untracked. The
bounded requested investigation ends here: third power is closed within
the inherited interfaces, near-second power and an efficient intrinsic
nonlinear evaluator remain open. No further campaign is silently started.
