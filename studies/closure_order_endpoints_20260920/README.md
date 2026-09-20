# Closure order and fitted predictor stability

Started 2026-09-20. New research direction: compare the canonical population
closures at orders p and p+1, particularly their limiting whole-circle
predictors after training. Preserve canonical dictionaries, ridge schedule,
joint initialization, actual adjoint, unhalved weighted square loss and physical
gradient metric unless a modified optimizer is explicitly declared.

## Contract and initial scope

Primary target: canonical gradient flow on finite compatible circle datasets;
secondary target: an explicitly specified modified optimizer with a proved
order-consistent selection rule. Compare outputs in the uniform circle norm,
and distinguish fixed-horizon convergence, endpoint existence, endpoint
stability, quantitative order rates, and identification with the full model.
Fitting alone must not be treated as selection of a unique predictor.

Scientific inputs are established docs/ and code/ and this study's own work.
Other studies and their unpromoted findings are not inputs, including earlier
optimizer proofs discussed in the conversation. Any necessary mechanism must
be derived here from the allowed sources. No experiments have been launched.

## Results and limits

Start with [RESULTS.md](RESULTS.md), the integrated mathematical account with
physical inputs denoted by `x`, and separate scopes for each theorem.

| Result | Status and precise scope |
|---|---|
| Consecutive fitted predictors and whole-circle order limit after nonlinear burn-in | Proved for every fixed finite compatible circle dataset with labels in `[-1,1]`, for all sufficiently large canonical orders. Both hidden blocks are frozen after an explicit positive time; readout GF then fits exactly. |
| Noisy readout selector | Proved for the same data and burn-in. Bounded projected random forcing plus nullspace damping selects the minimum-readout-norm interpolant independently of noise. Exponential physical-time convergence and quantitative order comparison; hidden blocks remain frozen. |
| Uninterrupted canonical GF, including its endpoint | Proved for the orthogonal two-atom family with opposite labels `±alpha`, `0<alpha<=10^-3`. All sufficiently large orders converge uniformly on all physical times and circle inputs; both hidden layers and all trainable blocks move. |
| Current-state certificate for unchanged GF | Proved at any order and finite law whose reached state passes the explicit small-loss/positive-Gram inequality. Gives fitting, finite remaining physical travel and an endpoint-comparison bound. Eventual passage is not assumed or proved for arbitrary data. |
| Geometry of the canonical filters | Proved: a ridge approximation defect decreases with order; positive filters and lifted middle mobilities increase in quadratic-form order. Consecutive filter actions have a square-summable bound on each fixed field. |
| Fitting alone fails to select an order limit | Proved using bounded exactly fitted equilibria in the actual closure spaces with alternating prediction at an extra input. Canonical-initialization reachability is not asserted. |
| Rapid error rate as a function of order alone | Open. The exact missing input is an approximation/coefficient-cost bound on the particular reachable forward/backward fields. Density alone cannot supply a rate for arbitrary fields. |
| General uninterrupted-GF endpoints | Open beyond the stated restricted family and a posteriori certificate. Modified-optimizer results do not settle it. |

All hierarchy results retain the full initialized-word enrichment. None replaces
that hierarchy by the polynomial core, changes its ridge, assumes whitening
coordinates are nested, or compares differently sized coefficient matrices
using a fictitious common Frobenius metric. The small-order fitting threshold
is qualitative; a low order can instead be checked by its actual Gram.

## Artifact map

- [SELECTION_ROUTE.md](SELECTION_ROUTE.md): broad modified-optimizer theorem,
  exact readout endpoint, preserved nullspace, noisy minimum-norm selector,
  learned-feature comparison, and the all-law short-horizon extension.
- [ENDPOINT_ROUTE.md](ENDPOINT_ROUTE.md): uninterrupted-GF small-label
  theorem, all-time comparison, uniform tails, hidden activity and a separate
  elementary GF example showing why finite-horizon convergence is insufficient.
- [OPERATOR_ROUTE.md](OPERATOR_ROUTE.md): exact hierarchy filters, lifted
  mobility, induced metric, finite-time defects and quantitative transfer bounds.
- [LEAD_COMPARISON.md](LEAD_COMPARISON.md): monotone ridge approximation
  functional, checkable unchanged-GF certificate, adjacent-endpoint bound,
  and the proof that abstract density alone supplies no order rate.
- [FITTING_ALONE.md](FITTING_ALONE.md): actual-closure interpolating equilibrium
  counterexample; no canonical reachability claim.
- [SELECTION_REVIEW.md](SELECTION_REVIEW.md),
  [ENDPOINT_REVIEW.md](ENDPOINT_REVIEW.md), and
  [LEAD_REVIEW.md](LEAD_REVIEW.md): informed internal checks, exact source
  scope, candidate hashes and correction closure. These are not isolated
  promotion reviews.

## Inputs, process and verification

Startup HEAD: `8a15e0f196ed31af54160c651bdfbf2f109eecf7`; tracked worktree
and index were clean. Shared AGENTS/workflow, docs README/notation and the
research/rigorous-mathematics skills were read. No other study, earlier
conversation's unpromoted optimizer proof, or external reference supplied a
scientific premise.

The lead read the complete relevant units of `docs/global_nonlinear.md`:
C.4.7.9, C.4.7.10.A and B, C.1 through its explicit low-order dynamics and
limit qualifications, D.3, and C.4.5.1–C.4.5.2. Agents' exact complete source
coverage is recorded in their route and review reports. The broader all-law
short-horizon hierarchy claim was rederived from A's all-Borel-law construction;
it is not falsely attributed to the narrower statement of B. No maintained
numerical-interface extension is claimed.

Three fresh scoped routes were developed before candidates were frozen and
compared: operator geometry, uninterrupted-GF endpoints, and selected
optimization. The lead developed separate certificates and the fitting
obstruction. Subsequent internal reviewers were explicitly allowed the other
named candidate and needed established sources. They disclose their author
involvement. The lead also checked all complete candidates and review reports.

Actual checks included rederivation of probability-weighted loss factors,
physical path-length constants, feature/Gram drift, the two filtered middle
actions, exact readout solutions, resolvent bounds, short-time source
comparison, Gaussian-tail removal, and time/order limits. A few deterministic
arithmetic/hash checks were used. No training simulation, quadrature experiment,
or numerical monotonicity was used as a proof. No generated dataset or maintained
code change was needed.

Two minor issues were corrected and checked: the abstract slow-approximation
example now makes the error/rate ratio unbounded, and positive noise amplitude
is no longer described as guaranteeing nonzero projected forcing. The synthesis
also uses canonical `m` for sample count, distinguishes the evolving feature
Gram from the constant physical metric, and states the observable-space domain
of dictionary density explicitly. No mathematical objection remains
within the recorded theorem scopes.

Canonical source snapshots:

- `docs/global_nonlinear.md` SHA256:
  `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
- `docs/NOTATION.md` SHA256:
  `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.

Final internally reviewed candidate snapshots:

| Candidate | SHA256 |
|---|---|
| `ENDPOINT_ROUTE.md` | `430c86712686cf7c0d059d6a7a1032d21e637efa3606255f9628387ded34a17e` |
| `SELECTION_ROUTE.md` | `a076b9a3826c9abe9408ec2f1c3b46856b0d3e82eeb4ce50ec2574f92ff969e7` |
| `LEAD_COMPARISON.md` | `161a0826011641a1dfa37838adc818d0e3576bfddbe0ad6866d19eb8b6a53189` |
| `FITTING_ALONE.md` | `e87dfd13f6cdf806c42479dc3e136474ff9b2ab2142cb56585bcbeac4754f12a` |

The operator candidate was separately checked by the lead and has SHA256
`76abf53ae00c6d4b8b6e50f6e5b60031f9e0c83233914cad7e27a4db3572c057`.
Final review hashes and correction provenance are in the review files.

No established material has been modified or promoted; no Git mutation was
performed. Promotion is a separate process requiring fresh isolated review and
user approval of a concrete addition.

Final artifact check passed for all ten study Markdown files: local links,
final newlines and whitespace, plus seven source/candidate snapshot hashes.
Both tracked-worktree and index diffs remained empty. Final synthesis SHA256:
`8298b8882ed1ceb1bd21be412a9ebef3096cb2628ef69a59ccc5286d3f0edcc1`.

## Next discriminating mathematical target

Prove a quantitative raw-dictionary approximation bound, including coefficient
cost, for the reachable lower forward field, upper backward field, their
initialized actions and the learned rank force on a fixed horizon. This would
turn the proved endpoint comparison into an actual rate in `p`. For general
uninterrupted GF one additionally needs uniform tail control or eventual entry
into the proved current-state certificate. Reproving density or merely finding
more fitted equilibria does not supply either estimate.
