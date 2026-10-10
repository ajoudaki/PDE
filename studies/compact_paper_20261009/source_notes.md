# Compact shared-source foundation

Scope: authoring `paper/compact_foundations.tex` only, with the current paper as the scientific input. The original paper files were not edited. The canonical-notation and rigorous-proof skills were applied; in particular, the first-layer matrix is written `W^(1)`, and passive backward fields are explicitly defined rather than silently identified with training derivatives.

## Public interfaces

- `cp:source`: whole-sphere forward and passive-backward holomorphy on the time rectangle through `T = 32 log(en)/lambda` times a complex-quadric tube; RMS, coordinate, response and angular bounds. All four source families share the time–sphere coefficient domain. This does not replace backward sphere sources by `m` separate training curves.
- `cp:panel-source`: the finite-input flaring domain, with `U_fin` independent of dimension and the number of passive inputs, the explicit radius `h(t)`, inscribed disks, and the adaptive-panel count. The proof includes the frozen-real-Gram unitary argument and the negative-time corner.
- `cp:finite-time`: radius `1/(lambda sqrt(log(en)))` for the finite-query lower-bound argument, with bounded prediction and initial-value difference on the enclosing rectangle.
- `cp:carrier`: all-real-time training carrier bound, including the endpoint. After the source horizon it follows from the physical parameter tail and a deterministic parameter derivative bound; no new late-time complex domain is assumed.
- `cp:src-powers`: the power ledger needed to deduce the master label cap, spatial and temporal coefficient orders, and dimension-free finite-panel constants.

The module takes the independently established real fitting result `cp:fit` as an internal dependency. It retains original-width normalization in rectangular fixed-deletion cavities. Its probabilistic width qualifications are existential and preserve confidence dependence without claiming an effective width threshold.

## Source correspondence and consolidation

- Current `integrated_appendix.tex`, lines 5991–9077: shared finite-deletion insertion, nonlinear remainders, Gaussian control entropy, same-root trace absorption, response recurrences, independent budget removal, rectangular/quadric continuation, and the activation-power ledger.
- Current `integrated_appendix.tex`, lines 12986–13974: finite-input Gaussian supremum and sample-RMS controls; fixed-deletion initialization and source transfer; the time-derivative estimate under provisional response stops. These are retained as shared ingredients, without the decoder-specific construction or seed apparatus that follows.
- Current `integrated_appendix.tex`, lines 10118–10228: finite-query radius and bounded-prediction specialization for the lower bound.
- Current `integrated_appendix.tex`, lines 12630–12739: the needed all-real-time carrier consequence is reproved from the fitting tail. The stronger all-finite-complex-horizon statement is not required by the compact selected proof.
- Current `panel_appendix.tex`, lines 1–458: the flaring-domain contract, derivative/propagator verification, and transfer of the shared source event. The later source compiler and runtime are owned by `compact_selected.tex`.

The compact proof uses a single local insertion argument and a single independent-moment removal argument for both domains. Domain-specific verification is deferred until after those common components. Activation values remain potentially unbounded: every size estimate uses `|phi(z)| <= b + s|z|` together with the slope and strip hypotheses. The finite-panel constants do not inherit the whole-sphere frame entropy factor.

## Validation state

The complete draft is ready for the assigned cross-review. The early whole-document build succeeded; reported source-module overfull displays have been reflowed. A mathematical cross-review and the final assembled-document build are separate integration checks and are not represented here as completed. No scientific obligation is intentionally delegated to the old paper or hidden behind an external proof citation. Any issue found by the assigned reviewer must be resolved explicitly before the parent marks the compact paper complete.
