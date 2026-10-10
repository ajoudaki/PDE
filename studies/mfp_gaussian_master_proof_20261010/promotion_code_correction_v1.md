# Fixed-seed substitution correction

Author: `/root/promotion_code_author`, 2026-10-10. Scoped author helper:
`/root/promotion_code_author/fixed_seed_semantics` (read-only semantics check;
no edits). Neither role is an independent promotion review. This correction
addresses R1 in the complete `promotion_review_one_v1.md`, which was read in
full. No other review report was opened for this correction.

## Defect and corrected convention

The reported exact rational reproducer was confirmed before editing. With
`seed=freeze(x)`, `loss=mean(x*seed)`, two steps of size `1/10`, and initial
array `[1,2]`, the old candidate returned `(81/100,81/50)`. The declared
fixed-seed result is `(4/5,8/5)`.

`Program.at` now preserves an existing `freeze` node and its original defining
expression. Its existing simultaneous replacement rule is unchanged elsewhere.
In the enlarged parameter/seed space, for seed `b=x_initial` and loss
`mean(x*b)`, the vector gradient with mobility `n` is `b`. Thus every step is
`x_next=x-eta*b`, giving `x_after=x_initial-steps*eta*b`. Neither current-state
substitution nor a history pullback silently refreshes `b`.

The finite evaluator and Gaussian compiler remain unchanged. They follow the
original seed expression to obtain its value and initialization dependence.
Consequently the seed can be correlated with the initial parameters even though
physical derivatives treat it as an independent fixed coordinate. For example,
a frozen `W@one` still supplies the response coefficient one when subsequently
used in a call to the original `W.T`; that source dependence is preserved.

To request a new seed at an updated state, explicitly construct
`freeze(at(value,state))` from the ordinary unfrozen expression `value`.
`at(freeze(value),state)` retains the original seed instead. Existing seeds
cannot depend on the private time parameter newly created by `curve_jets`, so
preserving them also respects its fixed-coefficient path convention.

## Exact edited paths

Only these three candidate files changed:

- `promotion_code__mfp_compiler.py`: add `freeze` to the operations preserved
  verbatim by `at`; clarify the `freeze` and `at` docstrings.
- `promotion_code__test_mfp_compiler.py`: add the five `FrozenSeedTests` below.
- `promotion_code__MFP_CALCULUS.md`: explain fixed seed lifecycle under state
  substitution, explicit new snapshots, represented direction factors,
  physical versus statistical independence, and fixed seeds in history pullbacks.

No original prototype, master proof, study README, book file, maintained file,
Git/index state, or frozen v1/v2 candidate was edited. Existing mapped candidate
files outside those three are byte-identical to the correction's starting copy.
The full mapping and README patch files are unchanged.

## Tests and evidence

Fresh scratch is
`data/generated/mfp_gaussian_master_proof_20261010/promotion_seed_fix/`.
`before/` retains the complete starting candidate code and its three existing
package import dependencies. `after/` contains the corrected candidate; no
study imports or retained outputs are required. The live flat sources match
the final `after/` bytes. `input_hashes.json`, `validation.json`, and the three
unified diffs retain the exact inputs, final hashes and change correspondence.

The new tests use independent rational formulas and dense arithmetic:

1. Vector GD at zero through three steps preserves the initial seed, including
   direct `at(seed,state)`. The physical derivative of the updated vector with
   respect to its live initial coordinate remains one with the seed fixed.
   Gaussian compilation separately retains the shared initialization value.
2. Scalar and nested seeds survive simultaneous vector/scalar substitution;
   explicit `freeze(at(value,state))` makes the new requested snapshot.
3. Matrix GD at zero through three steps preserves a frozen scalar coefficient
   and both frozen rank factors derived from the original matrix/vector. The
   independent dense gradient is `c*u*v.T/n`. All columns, a transpose action,
   and the updated loss agree with `W_initial-steps*eta*c*u*v.T/n`.
4. Moving and prescribed-curve jets of `mean(x**2)` along `-freeze(x)` agree
   with the exact fixed-seed path `x_initial-t*b`, including the zero cubic
   coefficient. Their Gaussian values are `(1,-2,1,0)`.
5. A frozen matrix action remains physically fixed under substitution and
   differentiation while preserving its original Gaussian source response.

Commands below run from the scratch `after/` directory:

```sh
PYTHONPATH=../before/code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_mfp_compiler.py' -k FrozenSeedTests -v
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_mfp_compiler.py' -k FrozenSeedTests -v
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v
```

The first command deliberately imports the old compiler while running the new
regressions: it fails with **8 failed subcases across 5 tests**, exit 1
(`regressions_before.log`). The corrected focused run passes **5 tests**, exit 0
(`regressions_after.log`). The full corrected suite passes **72 tests in
19.708 seconds**, exit 0 (`suite_after.log`). All five executable Python guide
blocks were extracted verbatim and executed separately; all passed
(`guide_after.log`). The exact original mismatch is in `reproducer_before.log`.
Python is 3.10.12; detailed platform and source hashes are in `validation.json`.
No stochastic experiment or training campaign was run.

## Wider inspection and remaining gate

The author helper inspected only the allowed compiler/guide plus required
instructions. Its semantic check agreed on moving/frozen derivatives, private
curve time, represented factors, nested seeds and explicit new snapshots. It
also ran small in-memory examples with an independent minimal interpreter;
these were auxiliary author checks, not a replacement for the real package
regression and full-suite commands above.

No further correctness defect was found within this bounded correction.
`at` still visits/rebuilds descendants below a preserved freeze node before
ignoring those replacements at the seed boundary; this can create unused nodes
and traces, but does not change the returned expression or compiled reachable
graph. That preexisting traversal is left alone to keep the correction minimal.

This is author validation of corrected source bytes. It does not waive the
adverse v1 report or satisfy the two fresh complete scientific reviews required
for the corrected promotion packet. Full integration review and user approval
remain the coordinator's later gates.
