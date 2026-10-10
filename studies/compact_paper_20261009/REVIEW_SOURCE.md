# Bounded source-module cross-review

Date: 2026-10-09. Review target: the frozen 1,356-line `paper/compact_foundations.tex`, together with the complete `paper/compact.tex` and `paper/compact_fitting.tex` interfaces. No TeX was edited. No author notes, previous review reports, other studies, empirical code, or other compression-method proofs were read for this review. The original long appendices were not needed to supply a missing proof.

Source-module SHA-256 at review: `25847cf8a19e5af600a836159b32741d431f3b4c2455c8a1aab1b1c0cab7548a`.

## Outcome

I found two localized corrections to the written proof, described below. Neither requires changing the source propositions, their label allowance, their query domains, or their probability qualifications. The relevant bounds and the uniform-control argument already supply the needed repair. Subject to making these corrections explicit, I found no additional material gap in the checked dependency chain for `cp:source`, `cp:panel-source`, `cp:finite-time`, or `cp:carrier`.

This is a bounded mathematical cross-review, not a formal verification or a review of the selected-model implementations, all headline conclusions, novelty, empirical claims, or preprocessing complexity. The canonical-notation and rigorous-proof instructions governed the mathematical checks; the paper-review severity rubric distinguishes the localized flaws below from a missing source argument. The requested single-report format takes precedence over the general review skill's multi-file template.

## L1 — Qualify Gaussianity and conditional means before adaptive substitution

Locations: `paper/compact_foundations.tex:657–660`, and the corresponding wording at `:689–700`.

The sentence saying that the retained-coordinate variations “are linear Gaussian images, hence centered” follows the substitution of actual adaptive controls at lines 637–638. After that substitution, the variations need not be Gaussian or centered: the controls depend on the omitted roots. Likewise, the trace formulas are conditional means of the *frozen deterministic-control forms*, not necessarily conditional means of the expressions with actual adaptive controls inserted.

The proof does not need adaptive Gaussianity. Lines 585–640 establish a single event uniform over deterministic control histories and then substitute actual controls. On that event, the frozen-control quadratic forms minus their traces are bounded uniformly, so the trace formulas remain valid pointwise bounds after substitution. This is a localized wording error rather than a missing independence argument.

Recommended replacement for the final sentences at lines 657–660:

```tex
For every deterministic frozen control history, the retained linear
variations are centered Gaussian images conditional on the cavity.
After substituting adaptive controls, we use only the uniform bounds
already proved; we assert neither Gaussianity nor centering of the
resulting variations. Pairing a frozen-control variation again with
an omitted root produces a quadratic form. Its nonzero trace is
retained before adaptive substitution, as treated next.
```

At the beginning of “Every noncentered contraction,” add:

```tex
Throughout this paragraph, conditional means and centered forms refer
to deterministic frozen controls, conditional on the cavity. The
resulting trace bounds hold uniformly over those controls and are
then evaluated at the actual adaptive controls.
```

Dependency impact: this correction makes the use of the local comparison in trace absorption and budget removal precise. It does not alter the uniform-event construction, scalar-feedback coefficients, moment order, or source conclusions. Severity: **Minor Flaw**.

## L2 — Scope the learned-row estimate and define its common envelope

Locations: `paper/compact_foundations.tex:453–455` and `:519–527`.

The displayed incoming-row estimate at line 522 is valid for hidden-layer incoming rows, whose flow contains the factor `1/n`. It is not valid for the first-layer incoming row. From the actual first-layer equation in `compact.tex:84`, the provisional carrier bound and `2\int\rho|dt|\le S` give instead

\[
 \|\Delta W^{(1)}_{i,:}\|_2\le sS^2M,
\]

with no `n^{-1/2}`. This does not create a large retained forcing term: deleting a first-layer neuron creates no lower retained reverse port. Its initialized incoming row and its learned motion affect its own activation and response controls, which are already among the controls covered uniformly. Only its existing outgoing column contributes a learned retained forward port. The separate first-layer term at line 751 is also consistent with the unsuppressed row motion.

There are two notation issues in the same estimate. `\tau_*` occurs only at line 521 and is not defined; the intended quantity is `\max_j\tau_j`. Also, the definition of `M` at lines 454–455 mentions only reference scaled carriers, whereas `b+sM` in line 521 requires a preactivation envelope and the control estimates use deleted-neuron amplitudes. All of these quantities have provisional polynomial-logarithmic bounds, so taking a common envelope is available without changing the local argument.

Recommended replacement for the definition of `M` at lines 454–455:

```tex
\(J_b=\beta^{20L}(1+M)\), where \(M\ge1\) is a common
provisional bound for the absolute preactivations and scaled carriers
of the reference and full paths, including the deleted-neuron values
that define the scalar controls. Such an envelope is
\(\operatorname{poly}(\ell)\) under the stated stops.
```

Recommended replacement for lines 519–525:

```tex
For every existing outgoing column, and for an incoming row at a
layer \(j\ge2\), integrating the omitted-parameter equations gives
\[
 \|\Delta W^{(j+1)}_{:,i}\|
       \le S^2(\max_r\tau_r)(b+sM)/\sqrt n,
 \qquad
 \|\Delta W^{(j)}_{i,:}\|
       \le S^2H_{\max}sM/\sqrt n.
\]
At the first layer the incoming-row estimate is instead
\(\|\Delta W^{(1)}_{i,:}\|\le sS^2M\).
There is no retained reverse port below that layer: this row's
motion is included in the deleted neuron's scalar controls, rather
than in the learned retained-port remainder. Thus every existing
learned port entering the retained equation still induces a force
at most
\(S^2\beta^{260L}(1+u)^2(1+M)^3(1+\bar\rho)/\sqrt n\).
```

The top-layer residual-offset sentence can then remain unchanged. If `M` is enlarged for passive controls as well, that only enlarges an allowed polynomial-logarithmic envelope; no displayed structural source constant is changed.

Dependency impact: the retained local remainder closure needs the `n^{-1/2}` bound only for actual learned retained ports. The omitted first-layer row is not such a port, so the repair preserves the `n^{-1/25}` first-exit estimate, the `n^{-1/30}` coordinate comparison, and the source event. Severity: **Minor Flaw**.

## Checked dependency chain

### Independence, stops, and local insertion

- Lines 254–298 define cavity initial tests, stops, and extensions using retained initialization only. Failed initial tests produce globally defined zero reference paths. Rectangle and expanding-domain retractions commute with real anchoring, so the later complex-minus-real decomposition does not silently condition a root on full-network survival.
- The retained equation at lines 300–319 includes the changed forward residual, the lower reverse port, and the top residual offset. The parameter scaling matches the mobility coordinates in the setup and fitting module.
- The Hessian decomposition at lines 332–358 separates bounded low-rank factors from the carrier diagonal. The Schatten normalization is by the original width `n`, not by the parameter-space dimension.
- The control-net calculation at lines 591–640 has logarithmic size `n^{5/8} poly(log n)`, whereas the Gaussian tail exponent is eventually `n^{.78}`. Its interpolation error is `n^{-1/8+1/200} poly(log n)=o(n^{-1/10})`. This leaves the claimed entropy margin before adaptive substitution.
- The nonlinear closure at lines 430–580 lists forward/backward, gradient/residual, reverse-probe, passive-response, and angular terms. With `N=n^{.01}`, `d_0=n^{-.1}`, and `u_0=n^{-.04}`, the terms in line 648 are indeed `o(u_0)` after the `n^{1/4000}` propagator factor. The joining-strip gate is strict at these scales. L2 makes the first-layer endpoint treatment explicit.

### Nonzero traces and moment removal

- Lines 668–739 retain the same-root traces, including the direct port Hessian and the smaller changed-residual contraction. The Dyson/Schatten argument assigns reciprocal exponents summing to one, which yields exactly the required `1/n` trace normalization. The domain proofs supply bounds on the product of the norms of the base propagators on disjoint contour pieces, as needed in the inserted-Hessian products.
- Lines 743–781 keep evaluated-sample amplitudes separate from driving-sample RMS amplitudes, then close the two scalar inequalities using `4D_0 C_F S^2\le1/2`. There is no sample-count factor in the absorption coefficient.
- Lines 784–837 obtain real Gaussian-reference moments through normalized residual activity and the carrier tail split, not a raw-time net. The square-root activity modulus and the Gaussian moment estimate are supplied, including the sample-RMS Jensen step without sample independence.
- Lines 1002–1059 use complete independently stopped paths. Singleton/common-cavity differences remain independent of the paired root even though the two coefficient paths need not be independent of each other. Fixed-order correction moments tend to one; distinct roots are independent given their common cavity. Collision tuples have vanishing normalized multiplicity after the `n^{o(1)}` maximum bound.
- The order of limits is correct: fix the deletion/moment order, take `n\to\infty`, then increase that order. Consequently the label allowance is fixed before the confidence and moment arguments. The final `mL(16L/\mathcal B)^u` bound tends to zero because `\mathcal B=1024e^2L`.

### Derivatives and analytic domains

- The time-derivative argument at lines 966–998 uses the provisional response caps, not already improved caps, and uses a growing deterministic Hölder exponent only inside the existing exponential budget. It does not require growing deletion sets. This distinction is important for the later domain argument.
- For the fixed rectangle, lines 1063–1122 obtain residual growth and the base-propagator factor from the operator/RMS bounds before invoking Gaussian insertion. The response and angular bounds then give strict activation-strip margins, followed by budget removal and local holomorphic continuation. This ordering does not assume complex Gram positivity.
- For the expanding panel domain, lines 1247–1304 freeze the real symmetric generator `2G(t)G(t)^\top` along a vertical segment. Its imaginary-time flow is unitary. The perturbation is controlled by the differentiated-gradient bound and the weighted residual integral, giving growth `exp((2C_g/sqrt(K)) B_n Y r_n)`. Since `B_n r_n\to0`, the factor-two base premise is eventually valid even though the domain's height grows. The norm-growth integrals add on ordered disjoint pieces.
- The expanding-domain retraction is uniformly Lipschitz, its real anchoring commutes, and its bounding rectangle has side `O(log n)`. The complex-minus-real radius is `O(log log n/sqrt(log n))`, sufficient for the stated vanishing Gaussian correction moments. The disk inclusion and the integral bound for the adaptive panel count were checked directly from `0\le h'\le d_h\le1/8`.
- Strict strip separation and bounded finite-width parameters support local analytic continuation across the compact stopped boundary. The query extension is by finite forward composition; passive backward fields use finite backward recursion and do not need another probabilistic budget.

### Finite-time and all-time interfaces

- Lines 1145–1159 justify the exact finite-query time radius `1/(lambda sqrt(log(en)))`. Using `S\le16 beta^{-30L}` and `U_fin\le beta^{26L}` gives `a/(4S^2U_fin)\ge beta^{34L-1}/64>1`; the coefficient is not an unspecified structural multiple. The prediction and independent-difference bounds follow from the given RMS caps.
- Lines 1161–1183 extend the carrier maximum by the real parameter tail after `T=32 log(en)/lambda`. The polynomial width factor from backward subtraction is dominated by `exp(-16 log(en))`. This includes the fitted endpoint and does not require a complex late-time extension.
- The fixed-data/eventual-width qualification in `compact.tex:119–146` is essential and is preserved. The proof does not supply a practical or polynomial width threshold, a simultaneous all-width event, a growing-data limit, or a uniform small-label limit.

## Final assessment

The compact source proof retains the essential arguments needed for its strong probability and domain claims: independent stopped references, uniform control nets, explicit same-root traces, fixed-order moment removal, provisional derivative estimates, and a separate expanding-domain propagator calculation. L1 and L2 should be corrected before calling the written module complete. Their proposed repairs are local and leave the statements and quantitative source interfaces unchanged. I found no basis in this bounded review for demanding a weaker label cap, a narrower query domain, a confidence-dependent allowance, or an additional factor in the analytic time radius.

## Resolution addendum — local corrections checked

Date: 2026-10-09. This addendum checks only the requested local revisions, not a second full-module review. Revised source SHA-256: `8de151e32734ee2c9116a91a1cccb7c5ecee7ec1369ff4784e88fb4d79a6148a`.

- **L1 closed.** Revised `paper/compact_foundations.tex:671–677` explicitly limits Gaussianity and centering to deterministic frozen controls, conditional on the cavity, and retains only the uniform bounds after adaptive substitution. Lines 684–687 apply that qualification throughout the trace paragraph. Thus the later conditional-mean language at lines 710–723 no longer asserts a distributional property of the adaptive expressions.
- **L2 closed.** Revised lines 454–458 define the common provisional envelope needed by the local preactivation, carrier, and deleted-neuron control estimates. Lines 523–530 distinguish every existing outgoing column from incoming rows at layers `j>=2`, and replace the undefined coefficient by `max_r tau_r`. The outgoing-column statement still includes `j=1`, namely the column of `W^(2)` issuing from a deleted first-layer neuron; the `j>=2` restriction grammatically and mathematically applies only to the incoming-row statement. Lines 532–539 give the unsuppressed first-layer incoming-row estimate and explicitly keep its motion in the deleted neuron's scalar controls, not in the retained-port remainder. The retained `n^{-1/2}` forcing bound therefore has exactly the scope used in the local closure.

Both reported findings are resolved without changing the source statements, their constants or powers, or their probability and query-domain qualifications. No TeX was edited during either review pass. There are no unresolved findings from this bounded source-module review.
