# Independent internal check of the width-2048 closure transfer

Date: 2026-09-25. Status: implementation and bounded execution checks pass;
scientific campaign endpoint replay and final scalar rescoring remain pending.
This is an internal implementation check, not a promotion review or a claim
that a closure fits, agrees with dense, or converges with order.

The assigned inputs were the complete closure-transfer protocol, the activation,
deep-moment and fast engines, the relevant factor helpers, the new complete
Euler runner, and newly generated closure-transfer data. No previous campaign
was re-audited. The checker used CPU only and launched no GPU work.

## Independent equations and implementation

The checker constructs actual physical matrices with NumPy:

\[
 W_\ell=W_{\ell0}-\frac{2}{Mn(1+s)}
 \sum_{p=0}^{P-1}(2p+1)A_{\ell,p}B_{\ell,p}^{T},\qquad \ell=2,3.
\]

It regenerates the original w,W20,W30,c arrays in NumPy's prescribed draw
order and scales, including readout standard deviation 1/n. Forward replay
uses explicit matrix products and independent ReLU, exact GELU, and SELU
formulas. Backward checks use the actual reconstructed matrix transposes.
Chronological transport is independently written as a degree-by-degree sum
over every lower degree. The prefix has A=0, B0 equal to the initial incoming
activation, higher B=0, and s=0. Zero residual is absorbing without a residual
division. A separate scoped algebra checker found no equation or prefix
discrepancy in the assigned engine sources.

Euler advances the seven stored blocks simultaneously. The reconstructed
matrix after a finite moment update is nonlinear in A,B,s, so it need not
equal an Euler update of the physical dense matrix. The check uses the correct
stored-variable Euler equations. The new runner captures only the RHS and
validity/loss fields; all borrowed velocities are consumed before graph replay.
The saved final loss is recomputed at the actual saved state, and the fixed
physical clock is updates times h.

## Evidence completed before final scientific results

- `closure_transfer_2048_checks01/algebra01.json`: 2,391 independent CPU
  comparisons passed, maximum absolute discrepancy 1.33227e-15. These cover all
  three activations and P=1,2,3, exact prefixes, noninitial moments/activity,
  explicit forward/transpose actions for training and passive query counts,
  chronological transport, zero residual, the initial dense tangent, original
  versus fast/cached RHS, simultaneous Euler, and pre/post-state loss.
- `closure_transfer_2048_checks01/bookkeeping01.json`: six tiny CPU output
  fixtures passed 260 recorded checks, plus rejection of an intentionally
  corrupted archive. Update, physical-time, wall, and immediate-target stops
  retain consistent states, clocks, losses and predictions. The 42 saved-block
  comparisons against independent Euler updates differ by at most 4.44090e-16.
  These are implementation fixtures, not scientific training runs.
- `closure_transfer_2048_checks01/pilot_replay01.json`: independent explicit
  matrix replay passed for all four saved pilot/opposite-GPU runs, with 140
  checks. Each replay uses eight training inputs and 32 fixed indices of the
  8192-angle circle. Maximum errors are 3.33067e-16 for training predictions
  and 1.66534e-16 for sampled circle predictions. Initializer, source, protocol,
  configuration and artifact hashes, archive CRCs, literal inputs, clocks,
  trace lengths, prefix loss and final MSE agree.
- Root's separate `closure_transfer_2048_execution01/receipt.json` records
  exact eager/captured agreement for all seven blocks over 100 updates on each
  of two fixtures, and exact opposite-GPU state/circle agreement over 400
  updates on each fixture. Its summed integration charge is 6.40367505699 s.
  This is externally executed evidence; this checker independently replayed
  the four saved states on CPU rather than launching GPU work.

One source-review ambiguity was raised before scientific launch: a nonfinite
terminal update does not retain a last-finite rollback state. Root clarified
the protocol before launch: preserve that raw failed endpoint, assign no
fabricated finite score, and preserve finite endpoint states for finite caps.
No runner-equation repair was needed. No numerical check failure was observed.
The deliberately corrupted archive is retained and labeled as a negative test.

## Reproduction and current provenance

Source: `closure_transfer_check.py`.
SHA256: `dc84b82d75d1512fadbc2e745de0d00272cc5ad962495925925c070b76d276dc`.
Runner checked: `03afd34771a131a1b816531768711f892944ded1a6dbe8579c06f7d439994bf5`.
The algebra receipt predates addition of the file-I/O checker and retains the
exact earlier checker hash. All receipts record their actual input/source
hashes; neither result nor source version is silently replaced.

Use `/home/amir/miniconda3/bin/python` with `PYTHONDONTWRITEBYTECODE=1` and
OMP/OPENBLAS/MKL/NUMEXPR thread counts set to 1. Commands accept fresh output
paths and never overwrite receipts:

```text
closure_transfer_check.py self-test --out NEW_RECEIPT.json
closure_transfer_check.py pipeline-test --scratch NEW_SCRATCH --out NEW_RECEIPT.json
closure_transfer_check.py replay --run RUN_DIRECTORY [RUN_DIRECTORY ...] --out NEW_RECEIPT.json
closure_transfer_check.py score --dense DENSE_PREDICTIONS.npz --closure CLOSURE_PREDICTIONS.npz --out NEW_RECEIPT.json
```

Replay and scoring do not import the producer. Scoring independently computes
circle RMS, maximum and relative error, and nested-grid sensitivity from raw
arrays. A raw-array score is labeled fitted only with compatible fitted run
summaries; a finite capped score is descriptive. Source/check receipts live
under this study's `closure_transfer_2048_checks01` generated namespace.

## First long-run fitted endpoint

An additional bounded check replayed the first scientific fit,
`selu__quadrant_alternating__P2__level0`, after 162121 updates at h=.00048828125
and physical time 79.16064453125. All 37 replay/metadata checks pass. Explicit
reconstruction gives MSE 9.999000555622815e-9 versus saved
9.999000636560610e-9, with maximum training prediction error 3.28304e-12 and
32-point circle error 5.49838e-13. The independent raw-array score against
the preserved finest dense endpoint is RMS .056970256245301956, maximum
.1099547676432211, relative RMS .014974295716488194, and nested-grid
sensitivity 1.792477725970354e-8. Receipts are `first_fit_replay01.json` and
`first_fit_score01.json` in the checker namespace. This detects no long-run
output inconsistency; closure step refinement and dense-reference sensitivity
remain separate requirements and are not certified by this first endpoint.

## Primary endpoint coverage

All 18 level-0 scientific runs subsequently fitted. The remaining 17 saved
states passed independent replay in `primary_replay01.json`; the earlier
SELU-quadrant P2 replay was reused rather than repeated. Together the 18 runs
pass 666 checks. Maximum explicit-matrix discrepancies are 8.64165e-12 on
training predictions and 7.43683e-13 on the 32 sampled circle inputs. All
independently recomputed losses satisfy the target.

`primary_scores01.json` independently compares all 18 raw closure endpoints
against both preserved dense endpoints. All 126 scalar comparisons agree
exactly with `closure_transfer_2048_preview02/analysis.json`; all 18 nested-grid
checks pass. Seven primary scores satisfy the descriptive RMS<=.1 threshold.
These primary scores do not yet pass a tested closure halving merely because
they fit. The first scoring driver stopped before writing a receipt after
looking for `descriptive_close` in `all_runs`; that field resides in the
selected `rows`. Joining by the saved run path fixed the schema lookup. The
receipt retains this checker-only history; no scoring formula or producer
changed.

## First refinement replay batch

`refinement_replay01.json` checks only the six newly completed level-1 ReLU
and SELU quadrant states, for P=1,2,3. All 222 checks pass and every replayed
loss satisfies the fitting target. Maximum prediction discrepancies are
4.35563e-12 on training inputs and 5.90694e-13 on sampled circle inputs.
Scientific-state replay coverage is now 24 unique endpoints: 18 primary plus
these six refinements. No earlier state was replayed again. Full-table
refinement rescoring and conditional-level checks remain pending.

## Complete half-step replay coverage

`refinement_replay02.json` checks the remaining 12 level-1 states and passes
all 444 checks. Maximum errors are 4.78107e-12 on training predictions and
5.11713e-13 on sampled circle predictions. The union of `first_fit_replay01`,
`primary_replay01`, `refinement_replay01`, and `refinement_replay02` contains
exactly 36 unique scientific states, with no repeated replay. All 18 primary
and all 18 half-step endpoints fit and pass all 1332 recorded checks. The six
conditional level-2 trajectories and final scoring/accounting are still
pending.

## Limits and remaining work

The bounded checks establish arithmetic and endpoint bookkeeping within their
tested scope. They do not establish scientific closure fidelity, long-run
numerical stability, continuous-time accuracy, or monotonic order improvement.
After the campaign finishes, replay only the newly saved refinement states
and independently rescore the final comparisons, preserving missing fits, numerical-screen failures,
the sensitivity-qualified SELU-quadrant dense reference, and all capped or
nonfinite attempts. Reconcile total GPU integration cost from actual runner
lifecycle/summary receipts plus the 6.40367505699 s execution checks; any
missing receipt must be flagged rather than replaced by the launcher's capped
fallback estimate.
