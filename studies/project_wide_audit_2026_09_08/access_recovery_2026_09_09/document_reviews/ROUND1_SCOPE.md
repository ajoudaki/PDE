# ROUND1 scientific/model scope review

Verdict: **CLEAN**

No required correction found in the assigned document's internal deductions, quantifiers, negative-claim logic, or scientific recommendations. This verdict accepts the document's explicit distinction between checked arguments, dependency-qualified results, and open claims; it does not recertify the underlying sources.

## Input integrity and complete-read record

- Sole mathematical/evidential input: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/access_recovery_2026_09_09/document_reviews/ROUND1_INPUT.md`.
- SHA256 before reading: `0629b35cbc044747233fe10788fb18158b269c56d0b73778708971e56fc61d06`.
- SHA256 after the complete read: `0629b35cbc044747233fe10788fb18158b269c56d0b73778708971e56fc61d06`.
- Full, line-numbered reads: **1–110, 111–220, 221–330, 331–440, 441–550, 551–649**, including every section, equation, table, and the final paragraph at line 649.
- The initial combined output for lines 1–330 was truncated. All three affected ranges were reread individually with complete output; no omitted text was inferred from the truncated batch.

## Scope and deduction checks

1. **Model, initialization, optimizer, and nonlazy behavior — lines 7–19, 39–68, 261–265, 295–331, 335–355.** The intended independently Gaussian initialized, all-block-trained model is distinguished from affine-first, small-perturbation, large-gain, and order-one-readout variants. Equal limiting initial predictions are explicitly not used to identify the small-readout and order-one-readout dynamics. Existence is not promoted to hidden activity; initial motion, persistent nonaffinity, changing kernels, and predictor separation remain separate properties. The relative-nonlinearity bound at lines 323–331 follows from the independent-copy variance identity and the lower increment bound with slope (a-e). Its stated exception for equal-coefficient odd overall gain is correct.

2. **Time and limit quantifiers, including recovered results — lines 59–66, 96–135, 208–230, 276–291, 351–395.** Fixed-order germs and fixed-program limits are not promoted to positive-time nonlinear dynamics. Every separately fixed linear depth is distinguished from depth-uniform or joint width/depth conclusions, and the recovered general linear GF result is not credited with the separate three-hidden-layer GD bundle. The finite-GF diagonal corollary is internally valid: fixed-width nonnegative-loss dissipation prevents finite-time escape; deterministic sufficiently small steps can be chosen in probability at each width; the theorem for every deterministic vanishing step sequence and the triangle inequality then transfer exactly the stated local observables. This supplies no global population continuation. Recovered same-array, capped-flow, strong-endpoint, plateau, and fast/slow statements retain their unproved response and identification premises.

3. **Finite optimization versus population identification — lines 299–312, 341–355, 373–381, 562–579.** Positive-time prediction inequalities and unsaturated gates are not misreported as asymptotic fitting or perpetual motion. High-probability finite fitting remains distinct from almost-sure fitting at each width and from global population convergence. The residual-direction coercivity argument has the correct mean-square normalization: it gives loss decay at rate at least (4\kappa/m). The prescribed-accuracy probability bound correctly chooses a finite horizon first and does not exchange width and infinite time or claim endpoint convergence.

4. **Negative results and their domains — lines 112–135, 141–202, 232–255, 460–483.** Changed-metric, changed-activation, and finite-prefix Stieltjes results do not settle the canonical all-order question. A failed deterministic stability estimate is not treated as a Gaussian-typical counterexample. Formal zero Taylor radius excludes the stated analytic/positive-compiler routes, while the displayed smooth autonomous ODE correctly defeats the broader smooth-ODE inference. The covariant-Schur and tagged-DMFT conclusions retain their proof-gap or conditional status. Ambient, generated-action, deterministic-reachable, fixed-mesh-neighborhood, and actual-positive-time witnesses are distinguished; failure of ordinary local Lipschitzness is not used to deny an independently constructed unique flow.

5. **Spectral, polynomial/PDE, and graphon distinctions — lines 204–255, 481, 485–537.** Restricted finite-contraction closure barriers coexist consistently with infinite-dimensional operator evolution. Spectra-only insufficiency concerns loss of orientation/mixed-word information, not impossibility of all spectral or operator descriptions. Scalar-particle residual, coherent dense graphon, and Gaussian-source/Hermite architectures remain separate. The recovered graphon strong-flow result is not promoted to its withdrawn noisy width/depth approximation rate or to the independently Gaussian initialized dense model. Source-Hermite truncation and empirical prediction comparisons are not presented as trained cutoff removal or generalization theorems. Prior-art statements remain model-specific and novelty is not certified as exhaustive.

6. **Clipping and preservation of the final optimizer — lines 393, 397–449.** Fixed coordinate-query clipping, varying-cap transcript comparison, and energy-compatible metric projection are not concatenated into an uncut population theorem. The metric projection identity follows from box optimality: nonzero components of (e_R) occur on the corresponding signed active faces, giving (e_R^T u_R=R\|e_R\|_1). An integrated weak defect is not promoted to RMS control. The all-physical-time inactivity statement retains both the fitting event and the necessary constant multiplying (\sqrt n). The practical dissipative cap is also explicitly a separate construction.

7. **Scientific strategy and fitting obstructions — lines 539–581.** Duplicate-input and parity restrictions are fitting obstructions, not obstructions to evolution. The bounded-feature contrast inequality correctly yields a necessary readout cost ((1-\varepsilon)/a), without declaring fitting impossible for fixed positive amplitude. The recommended reachable-response estimate preserves the chosen optimizer and correlated-data target; it is identified as missing, not assumed solved by initialization conditioning, forward compactness, a changed architecture, or a clipping result. Passive test-input and representation/risk analysis remain future obligations.

The contribution tables and closing corrections at lines 583–649 preserve these qualifications rather than restoring stronger claims in their summaries.

## Required corrections and optional improvements

- Required corrections: **none**.
- Optional improvements: **none requested**. The document already provides the qualifications needed for this scope review.

## Isolation compliance

I read only the assigned input and the operational instructions in `/etc/codex/skills/solve-math-rigorously/SKILL.md`. The skill informed the internal quantifier and implication checks; the user's document-only restriction governed the evidence boundary. I did not open linked/source/project files, previous reviews, historical rollouts, source audits, other agents' material, web pages, or external papers. No agents, experiments, or task contacts were used. No master or source was edited. The only file written was this assigned report, using `apply_patch`.
