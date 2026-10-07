# Final bounded audit of the Harmonic setup integration

2026-10-06. Verdict: **PASS for integration within the scope below.** No
substantive integration blocker remains in the frozen version identified here.
This is not a fresh proof review of the inherited source theorem, a promotion
review, a numerical experiment, or a finite-precision certification.

## Frozen inputs and scope

The inspected final `RESULT.md` has SHA-256
`b827c064d22fb77c6d25e47c9b5741e51e9c7998deb6a64b3e3efaa14bb0e0b3`.
The complete integration fragments inspected have SHA-256:

- `SETUP_INTEGRATION_PROOFS.md`:
  `9b23d4bc765df0c8c0e1d19a53663a8d775246c73797c533935adfbbee13c5b1`.
- `SETUP_INTEGRATION_ORDERS.md`:
  `57ddd148ab2ae3c3b31fc50949f6045b22bb734a6e834aef9008ed1f698d511e`.

The review read both fragments completely and inspected the receiving
`RESULT.md` statements, original source recurrences, label allowances,
analytic-extension gates, coefficient-count interface and cost consequences.
For preservation checks it compared the imported mathematical displays with
their corresponding scientific sections in
`POLYNOMIAL_SETUP_ODE_ROUTE.md`,
`POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md`,
`LOCAL_CONTINUATION_SETUP.md`, `LOCAL_ACTIVATION_BACKEND.md`,
`LOCAL_CONTINUATION_ASSEMBLY.md`, `LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md`,
`IMPLICIT_GAUSSIAN_SAMPLER.md` and `IMPLICIT_HARMONIC_EXECUTION.md`.
A separately scoped read-only crosscheck compared the complete original and
integrated order recipes against `IMPLICIT_SETUP_ORDERS.md` and checked the
execution source's cost and coupling qualifications.

Only the assigned study inputs, `docs/notation.qmd` and required notation/math
skills were used. No other study, archived book, Git history, or previous audit
verdict supplied scientific evidence. The original analytic source and
comparison arguments are inherited inputs to this integration audit; they were
not independently reproved here.

## Findings

1. **Source hypotheses and labels are preserved.** The order recipe's internal
   references resolve to complete source recurrences (S.5)--(S.10), (S.22),
   (S.24)--(S.25) and (S.30), including the actual activity allowance
   \(S=16Ym/\gamma\). The exact common label interval and the Harmonic-only
   interval retain their separate definitions. The optional
   \(Y\le(\gamma/m)\beta^{-30L}\) cap does not replace the full interval.
   Both analytic-extension gates, the dimension-one counting gate and the
   source-radius gates remain present. The source probability threshold remains
   existential; no numerical confidence-to-width theorem is inferred.

2. **The deterministic proof chain is complete at its imported interface.**
   Signed defect stability bounds the parameter error using the integrable
   training residual. The restart argument constructs a holomorphic solution
   from each computed anchor, and the activation backend reserves separate
   defect and source-output allowances. The source-jet bridge uses
   \(\delta_{\rm node}/(32\sqrt n)\) as its backend target and proves the
   Euclidean base-source error needed by assembly. Multiplication by an
   initialized matrix of operator norm at most eight then supplies the image's
   separate coordinate bound. The paired coefficients are formed by the same
   linear operations, so their exact initialized-matrix relationship is kept.
   Positive quadrature is applied to the exact analytic sources before the
   finite nodal perturbation bound; the numerical path need not be globally
   analytic across its panels.

3. **The local coefficient conventions match.** Training recurrences initially
   use normalized Taylor coefficients in \(t-\tau_b\), where \(\tau_b\)
   is panel \(b\)'s left endpoint. The projection table instead uses
   \((t-\tau_b)/\Delta_b\), where \(\Delta_b>0\) is its length.
   The implicit execution explicitly supplies
   \[
   G_{b,c}^{\,g}(v_s)=\Delta_b^c[g(\tau_b+\cdot,v_s)]_c
   \]
   before applying that table. Its rescaling work is included in the projection
   bound. The bridge also expressly replaces the conditional assembly lemma's
   exact-activation jets by polynomial-backend jets while proving the required
   stronger source interface.

4. **The Gaussian claim has the correct joint scope.** The sampler maintains
   the conditional remainder for both directions of each initialized matrix
   and arbitrary global adaptive interleaving. The execution inventories exact
   initialized features, all panel actions, completed source-image coefficients,
   and final basis-image actions. Its stopping budget replaces the realized
   rank \(r\) by the deterministic upper bound \(\min(n,R)\).
   Consequently the joint-law claim concerns the explicit finite local
   initializer with the same scalar routines and deterministic conventions,
   together with its freshly sampled dense reference. It does not identify the
   output with the older initialization-jet program, exact source integrals, a
   supplied concrete matrix, or a prescribed entrywise random stream. There is
   no rejection on a good event and no added stochastic failure allowance.

5. **The complete costs and their specializations agree.** The explicit
   envelopes retain dense anchors, initialized image multiplication and final
   basis multiplication. The added initial Gram/solve-cache and final cache
   terms are conservative charges already justified by the execution
   inventory. The implicit envelopes charge Gaussian query spans, all retained
   increment factors and their repeated actions, projection, selection,
   geometry and final assembly. At fixed admissible structural parameters,
   \(T=32(m/\gamma)\log(en)\) and source tolerance \(1/n\), the stated
   explicit work/memory are
   \(O(n^2\log(en)^{3d/2+1})\) and \(O(n^2)\); the implicit
   work/memory are \(O(n\log(en)^{9d/2+3})\) and
   \(O(n\log(en)^{3d/2+1})\). These shorthand counts require the
   displayed bounded-cost primitive convention. General orders retain the
   finite envelopes and separate primitive charges. No finite-width timing
   superiority or first-order solver lower bound is asserted.

6. **The accuracy consequence uses a sufficient budget.** At
   \(n=\varepsilon^{-2+o(1)}\), the selected original
   \((T_0,1/n)\) source specialization gives
   \(n^{-1+o(1)}=\varepsilon^{2+o(1)}=o(\varepsilon)\) error.
   It has the advertised polylogarithmic retained storage and setup costs
   \(\varepsilon^{-4+o(1)}\) explicitly and
   \(\varepsilon^{-2+o(1)}\) implicitly. The text expressly permits a
   larger sufficient budget of the same storage order and does not claim the
   least inverse budget supports that stronger source tolerance. Full-width,
   baseline and zero-label branches preserve their separate constructions.

7. **The import preserves the mathematical formulas and local scopes.** The
   display comparison found no mathematical change in the imported signed
   stability, activation, assembly, bridge, sampler or implicit-execution
   formulas. Quadrature differences are the declared spherical-cutoff rename
   and exclusion of the superseded value-oracle cost passage. The local
   continuation difference is that same rename plus TeX spacing. Equation
   namespaces distinguish components, and the single order recipe gives the
   exact correspondence for the components' local names.

## Correction verified and limits

The first inspected version left two references to
\(\mathcal Y_J\) in (Setup-C.5) and its explanatory sentence after the
quadrature cutoff had been renamed \(\ell_*\). Both were corrected to
\(\mathcal Y_{\ell_*}\) in the fragment and `RESULT.md`; the hashes above
identify the corrected files. This resolves an undefined alias and preserves
the original formula. No other substantive integration correction was needed.

The audit does not certify floating-point stability, reliable numerical rank
tests, effective stochastic source thresholds, or measured performance at
practical widths. It does not authorize promotion or replace the complete
independent reviews required for promotion. Mechanical link/render validation
and any existing algebra checks are separate from this mathematical interface
audit.
