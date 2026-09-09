# Bounded positive-metric and formal Taylor assembly

Date: 2026-09-09.

Candidate: ../POSITIVE_METRIC_TAYLOR_ADDITION.md, intended as Section 10
of the maintained Gaussian-calculus chapter after the separate pullback
addition. This is an assembly record, not independent acceptance.

## Authorized scope and files

The parent authorized this proof-only candidate and this audit file. No
main chapter, package code, test, historical artifact, or Git state was
edited. No high-order generator, simulation, or campaign was run. Existing
small exact certificate evaluation was authorized and used as described
below. The mathematical work preserves the raw-square one-input,
two-hidden-layer model, independent standard Gaussian primitive variables,
order-one stored readout, and the explicitly stated block mobilities.

Both solve-math-rigorously and investigate-conjectures skills were read in
full, together with the latter's evidence-ledger and adversarial-audit
references. Their paths and hashes appear in the manifest below.

## Exact claim changes proposed

| Claim | Proposed status and scope | Proof in candidate |
|---|---|---|
| Every fixed derivative has a finite annealed limit polynomial in the block multipliers | Proved by explicit primitive rewrites and normalized finite-forest expectation counting for this model | Section 10.1 |
| A strictly positive block metric violates the formal Stieltjes representation | Existential interval \(0<\alpha<\varepsilon\), \(\beta=1\); no numerical endpoint | Section 10.2 |
| Canonical formal coefficients have factorial lower growth | Direct raw-square bound \(c_k\ge m!4^{-m}6^{k+1}\binom{k+2}{2}\), odd \(k\), \(m=(k+3)/2\) | Section 10.3 |
| Prescribed positive Taylor residual-clock losses are uniformly Cauchy near initialization | False; their pointwise limit is discontinuous at zero | Section 10.4 |
| Typical derivative concentration | Not claimed or imported | Explicit boundary in Section 10.1 |
| Actual positive-time network trajectory or its discontinuous step loss | Not constructed or identified | Explicit boundaries throughout |
| Every signed/nonanalytic/non-Taylor finite description fails | Not claimed | End of Section 10.4 |

The new local bridge is the normalized derivative-to-forest identity. At
each hit the primitive vector field contributes \(1/n\). A row or column
hit increases the edge count by two; a middle-edge hit preserves the edge
count and increases the component count by one. Both changes increase
\(e/2+r\) by one. The candidate gives the exact decorations, multiplicities,
unrestricted labeling convention, and expectation proof rather than
invoking correctness of a historical executable.

The positivity comparison for factorial growth is at the primitive
polynomial/expectation level. It does not make a componentwise comparison
of trained network trajectories. The scalar branch is obtained by taking
only the readout and middle-block derivations inside the same full model.
The conditional branch expectation is a fixed polynomial in
\(q_n=n^{-1}\sum u_j^4\); its limit is proved with explicit moment bounds.

The lower bound is derived directly with raw-square coordinates:
\(a'=z^2,\ z'=2qaz\), invariant ray \(z=\sqrt{2q}a\), and
\(az^2=2q(1-2qs)^{-3}\). Thus no historical \(\phi(u)=u^2/2\)
or variance-parameter conversion is silently used.

## Dependencies for isolated reviewers

Read the candidate in full. The sole finite numerical theorem input is
the maintained docs/gaussian_calculus.md, Section 7.2:

1. “A fully specified quadratic initialization-jet obstruction,” equations
   (7.C1)--(7.C11): model and metric, frozen-row identity, conditional
   Gaussian moment limit, monomial recurrence, formal inverse, six
   moments, and exact negative quadratic witness.
2. “Implementation and independent checking routes,” especially
   quadratic_axis_certificate(), explains how that witness is regenerated.

The candidate repeats the finite-forest expectation proof and the formal
inverse continuity recurrence in full. Section 4's Gaussian integration
by parts/Wick formula and Section 7.2's forest proof can additionally be
supplied as established corroborating dependencies; the candidate states
the needed integration-by-parts induction itself.

No result from the forthcoming review process is a proof input. Historical
searches were used as locators; no later review verdict is used to establish
a mathematical claim.

## Correction and adversarial reconciliation

The corrected leading notes in both quadratic primary manuscripts retract
inherited concentration and positive-time identification. The candidate
preserves that scope. It uses the formal averaged coefficients and proves
non-Cauchy behavior only for the prescribed Taylor family. The bounded
metric triangle argument gives failure of its iterated common-target
shadowing claim without requiring any actual network limit.

The full adversarial manuscript separates positive coefficient compilers,
analytic/Banach realizations, Gaussian tail truncation, and general
non-oracular real-axis closure. Those larger no-go claims are not added.
In particular, positive semidefiniteness of the full trained message is
never used as componentwise positivity.

The complete matroid correction rejects its unrestricted rank gate and
the singleton-row benchmark that omitted even-readout parity. The complete
two-hit charging correction rejects prefixwise factor-nine contraction
bounds and leaves its aggregate upper bound unsupported. Neither shortcut
is used: the candidate sums ordinary Gaussian edge pairings directly for
existence and uses a positive scalar subfamily for a lower bound.

The positive-alpha primary derivation asserts a generic finite Gaussian
program/concentration lemma. That stronger lemma and its order-thirteen
coefficient table are not imported. The connected-compiler source explicitly
reports only a partial independent order-thirteen overlap. The candidate
instead proves finite-order polynomial dependence from the forest grammar,
then applies continuity to the already specified boundary witness. The
reported interval \(1/100\), sharp root, determinant polynomial, and
canonical high-order positive gates are not conclusions of this candidate.

## Bounded checks performed

A single deterministic Python call imported the existing
pde.exact_calculus.quadratic_axis_certificate() with bytecode writes
disabled. It regenerated the fixed scalar boundary certificate, without
reading retained tables, and checked:

- the three witness coefficients against (10.9);
- the exact negative witness value against (10.10);
- the frozen first derivative \(63\);
- the illustrative scalar lower bounds in (10.13) at \(k=1,3,5\).

All checks passed. Wall time was approximately 0.067 seconds. The illustrative
low-order comparisons are sanity checks, not evidence replacing the all-order
proof. Delimiter counts were balanced and the candidate had no unexpected
control characters. No positive-alpha jet was generated; no numerical
trajectory or empirical concentration claim was tested.

## Source reading and SHA-256 manifest

Ranges refer to the source versions read during assembly. Whole-file hashes
identify those versions; mutable maintained files should be frozen again by
the coordinator with the final review input.

| Source | Read coverage | SHA-256 |
|---|---|---|
| studies/stieltjes_resolution/POSITIVE_ALPHA_JET_DERIVATION.md | Full, 1–387 | a6107b798bea3e1cf4331bafbbc1163a56996abdf5ef5cca4dff1adf833db9a2 |
| studies/stieltjes_resolution/BLOCK_METRIC_RESOLUTION.md | Full, 1–472 | 4b441a69d643e30adebddc143b204b6363e2b2a6a71d186c7b679fe03efc6289 |
| studies/stieltjes_resolution/ALPHA_CONNECTED_COMPILER_AUDIT.md | Full, 1–100 | beb7897cfa0cf56a84b9d9c93a9c7de4559b7f547f267431a2bd4bbec8aa5d4a |
| studies/stieltjes_resolution/PROOF_CONTRACT.md | 1–180 | cd9d2b33eb284199011914cbb729e6dc2c45b9d84f45865fe740e79a7b28baf6 |
| studies/quadratic_nonclosure/approximate_single_source_conjecture_resolution.md | Full, 1–838 | fa58d9683eca82395df58aa0ecc1dc5187e9adb197138535a599f1abf259fe6b |
| studies/quadratic_nonclosure/adversarial_audit_report.md | Full, 1–806 | 51d2c7ed76f7625ca00d93d55715356e111e597e4c82fbb28a2743ccbd1afa72 |
| studies/quadratic_nonclosure/QUADRATIC_MUP_NONCLOSURE_MASTER_REPORT.md | 1–70, 384–447, 544–610, 2848–2916; locator searches elsewhere | 6e829d494150f773221edb1b51861c47c1b904709d9ee32eb33253e05169d6a3 |
| studies/quadratic_nonclosure/README.md | Full, 1–60 | 5fe16e9ba2f6198b3e4a47e0032591fdd167f2123e6f895fcbed4d82aeda6020 |
| studies/mfp_quadratic_compiler/README.md | Full, 1–226 | 65440716fc82d88bce06f9cb59e5c577bf5d37b6dbac2301bdced4f2c9b23683 |
| studies/mfp_quadratic_compiler/graph_compiler_reference.py | Full, 1–600, across two reading passes | 21056f8dd8a02bf5a2b0bfccd5e71c53a0c0ffe10ab377673d675896b11db4d6 |
| studies/mfp_quadratic_compiler/archive/MATROID_WICK_AUDIT.md | Full, 1–91 | efb72441f91dfc718616f24a608c7f2cd2ae43abcb0ad83e3523f974af7500ce |
| studies/mfp_quadratic_compiler/TWO_HIT_CHARGING_AUDIT.md | Full, 1–124 | fa76036b49c060b92f3b8309adb9ca82cc4f88ace10048ac89b384bcff28f085 |
| studies/mfp_quadratic_compiler/SECTOR_ENGINE.md | Full, 1–78 | 6ab51299604155b4c79fade2c45d1f372445e6860320ea77c6a65c41ec962a78 |
| studies/mfp_program_history/CURRENT_RESEARCH_STATE.md | 505–595, 605–887; locator searches | 9cb4794c4cda01a012a17892d2e8df0c2a6c9cc98f3a6eb4257b0b86f3076b15 |
| studies/stieltjes_program_history/CURRENT_RESEARCH_STATE.md | 270–307, 909–956, 1321–1407; locator searches | 35c5a48c68fbbebe29036f0363fa852c98d47a816a49aa8a15b87b80a39a3783 |
| docs/gaussian_calculus.md | 2050–2433, including full Section 7.2; heading locators elsewhere | 9676106aa203f8f3939b794429a945ac1c55a127fa230c94fde0672268eee56d |
| code/pde/exact_calculus.py | 1–115, 200–249 and symbol locators; only the existing axis function called | d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3 |
| /etc/codex/skills/solve-math-rigorously/SKILL.md | Full | 9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7 |
| /etc/codex/skills/investigate-conjectures/SKILL.md | Full | a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de |
| /etc/codex/skills/investigate-conjectures/references/evidence-ledger.md | Full | 9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e |
| /etc/codex/skills/investigate-conjectures/references/adversarial-audit.md | Full | 8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501 |
