# Selected-method compact module

Owned artifact: `paper/compact_selected.tex`. The original paper files are unchanged by this subtask. This is a theorem-only reconstruction, not an efficient-initialization or numerical-conditioning result.

## Implemented architecture

- `cp:selection`: direct 9r barrier construction, exact source metric, metric condition bounds, constant-vector mass, coordinate-product and activation bounds.
- `cp:selected-fitting`: prescribed corrected-readout dynamics, exact parameter-energy identity, independent fitting bootstrap, parameter convergence and endpoint tails.
- `cp:selected`: one source-to-runtime comparison for Harmonic and Logarithmic. The proof retains the source-energy inequality, signed residual damping, and exact cancellation through `zeta = z_w + V_C Q_C^{-1} e`; no ordinary ambient Gronwall estimate substitutes for that cancellation.
- `cp:jets`: explicit disk-to-rectangle continuation from finite initialized jets; finite approximation of later-anchor derivatives and integral coefficients; exact initialized-image pairing in Euclidean coefficient norm. It proves finite existence only.
- `cp:harmonic-approximation` and `cp:harmonic`: spherical-harmonic decay, Chebyshev time decay, weighted-simplex count, two-point d=1 case, selection, absolute Y/n error, and all retained state.
- `cp:panel`: adaptive-panel Taylor spaces using the shared analytic-domain lemma, exact input-span reduction, the common selected runtime, absolute Y/n error, and all retained state.

## Interfaces

The source module supplies `cp:src-coefficients`, `cp:src-powers`, `cp:source`, `cp:panel-source`, and `cp:src-panel-count`. Source coefficients H_j and tau_j are explicitly aliased as H_j^src and tau_j^src. The sphere event includes the passive backward family on the whole joint domain; without that stronger interface, a separate backward space for each training input would introduce an unwanted factor m into the harmonic coefficient count. The dense module supplies `cp:fit`.

The only comparison horizon is T = 32 log(en)/lambda. The tolerance is min(1,Y,S,Y/(2n A_n)); the independent tails are eventually below Y/(2n). No arbitrary-budget or arbitrary-horizon theorem is asserted.

The explicit comparison ledger is specialized to Y/lambda <= beta^(-30L). In particular B_n <= 1 + sqrt(log(en)), and A_n has only a polynomial sample/gap prefactor and exp(C sqrt(log(en))) with C depending on activations and depth. The full recurrence-defined label range is deliberately not claimed.

The exact temporal inverse radius is retained as 131072 (Y/lambda)^2 (U/a) log(en)^(3/2). It is squared only in the final retained-state count, preserving (Y/lambda)^4. The panel count preserves its separate (Y/lambda)^2 sqrt(log(en)) and lambda^(-1) log log(en) contributions before squaring; the displayed panel storage therefore retains two distinct sample/gap coefficients.

## Scope and verification status

Self-checks covered the sparse-metric identities, prescribed-velocity energy identity, source pairing errors, initial exactness, cancellation variables, origin-jet map and derivative recovery, d=1, harmonic dimension count, panel Euclidean coefficient tolerances, input-span coupling, and complete retained arrays. A complete control-character scan is clean after repairing one formfeed caused by a string escape. Parent integration/build and cross-review remain authoritative for the assembled draft.

No mathematical gap is being intentionally left in this module, but this is an internally assembled proof pending cross-review, not an independently certified or promoted result. The proof depends on the new source and dense interfaces being proved in the other compact modules. It makes no claim that their proofs follow from definitions alone.

No original decoder, experiments, efficient arithmetic/setup bounds, retained dense environment, or arbitrary-order extension is imported. The activation evaluator's nonprimitive description and scratch remain separately charged. Dense coefficient arrays, jets, quadrature tables, and adaptive partition schedules are discarded after initialization.
