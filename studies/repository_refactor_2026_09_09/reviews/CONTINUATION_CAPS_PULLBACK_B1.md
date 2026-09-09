# Independent isolated proof and code audit B1

Verdict: **CORRECTIONS REQUIRED** (one minor mathematical-domain correction, P3). Not CLEAN.

The required correction is confined to the regularity stated for the predictor-based cubic specialization. I found no required correction in Theorems 12.1–12.2, the generic finite Euler pullback formula, or the two rational pullback APIs. Passing tests do not remove the issue below.

## Required correction

### B1-F1 — The predictor's third derivative need not exist under the stated hypotheses (P3 / minor)

**Locations:** `docs/loss_pullback.md:44–56`, `219–250`, especially the definition in (9.P18) at lines 222–224 and the claimed product rule (9.P20) at lines 237–244. The inherited finite-network activation hypothesis is only C2 (`docs/finite_dynamics.md:20`; `code/NUMERICAL_CONTRACT.md:63–68`).

The generic pullback theorem assumes that `u,v` are C6, and explicitly supplies `P in C7` as sufficient when `u=-P`, `v=grad P`. These conditions do not ensure that the underlying predictor `f` is C3 at a zero-residual state. Nevertheless (9.P18) defines the full third derivative tensor `D^3 f` at the same arbitrary supplied state, and (9.P20) invokes the third-order product rule for arbitrary directions without a separate predictor-regularity hypothesis.

A permitted finite-network example is width, input dimension, hidden depth and sample count all one, mobilities one, input one, label zero, scalar hidden activation `phi(w)=|w|^3`, stored first weight `w`, and stored readout `a`. The activation is C2, as required by the finite model. In mobility coordinates, which here are the original coordinates,

\[
f(w,a)=a|w|^3,\qquad \mathcal L(w,a)=a^2w^6,\qquad P(w,a)=-a^2w^6,
\]
\[
v(w,a)=(-6a^2w^5,-2aw^6).
\]

Thus both `u=mathcal L` and `v` are C-infinity, and `P` is C-infinity: every stated regularity hypothesis for the loss pullback is satisfied. At the supplied state `(w,a)=(0,1)`, however, the third derivative of `f` does not exist, since its restriction to `a=1` is `|w|^3`, whose second derivative is `6|w|`. Consequently `D^3f` in (9.P18) and (9.P20) is undefined. Multiplying that undefined tensor by a zero residual does not make the displayed derivative identity valid.

**Required repair:** Explicitly add `f in C3` near the supplied state for (9.P18)–(9.P21), while retaining the separately stated C6/C7 loss-field regularity for the Taylor remainder. Alternatively, place stationary states before the derivative-based specialization and restrict the displayed tensor definitions/product rule to states where the needed predictor derivatives exist, with a proof of any regularity inferred from `P`. The former is a short sufficient repair.

The stationary example has exactly zero Euler defect, as the later stationary-state argument correctly states. This finding concerns the domain and justification of the predictor-tensor formulas; it does not contradict the generic formula (9.P15), the exact zero-defect conclusion, or either capped-flow theorem. It remains a required correction under a criterion that all displayed mathematical claims must be well-defined under their advertised hypotheses.

## Proof audit

All supplied mathematical input was read completely and checked independently.

- **Finite model and metric:** Re-derived the residual-free backward recursion; Euclidean/Frobenius gradients; endpoint mobilities `n*kappa`; middle mobilities `kappa`; kernel normalization; mean-square factors `2/m` and `4/m^2`; and the weighted energy identity. The finite-time energy continuation argument works for arbitrary C2 activations. The width-uniform estimates correctly add bounded first derivatives and the initial norm/loss bounds. The sphere-net bound has the stated `2*9^(2n)*exp(-n*M^2/8)` constants.
- **Given-space capped theorem:** Checked the first/readout L2 norms and middle Hilbert–Schmidt norm against the normalized finite learning metric, genuine adjoint use, rank-one operator identities, bounded activation derivatives, continuity of the gate products, and the chain rule along C1 Hilbert-space curves. The temporary readout cap produces a locally Lipschitz extension with growth linear in the cap radius. The common first-row scalar cap preserves dissipation even with cancellation among sample directions. Its energy bound is `E0=3/2`; the readout bound is `2Rt`. Completeness, bounded field norms, and the inactive auxiliary cap justify global strong existence and uniqueness.
- **Conditional continuation:** Checked moment extraction from the exponential L2 tail, readout tails via the integral equation and Minkowski, the reference-state splitting estimate, and the single rather than squared cutoff factor. Optimizing the cutoff gives the stated logarithmic modulus. The defect has the stated `sqrt(3)` factor and no matrix defect. The positive scalar comparison and first-exit argument yield full real-indexed cap convergence. Continuity on the convergent paths justifies uniform field and kernel convergence without compactness of Hilbert balls. Tail passage by Fatou gives enough reference-state control for uniqueness against all strong competitors and for restarting along the reached curve. The exact loss energy identity follows from the proved chain rule.
- **Clock and scope:** `mathcal L=2E/3` for the three-sample capped model, so evaluating an E-flow at `2t/3` correctly supplies mean-loss time. No raw-GD identity follows from that observation. The spaces and bounded initial middle operator are assumptions. Exponential tails remain an explicit unproved premise. No finite-width Gaussian identification, population GF/GD approximation, fitting claim, or feature-motion conclusion is silently asserted.
- **Finite Euler calculus:** Checked the mobility coordinate change, moving residual, finite noncommuting word recursion, binomial pullback identity, degree cancellation, all displayed temporal polynomials, the sixth-order integral remainder and its fixed-N scope, the independent cubic trajectory expansion, and the generic gradient-potential cubic formula. The algebra of the predictor specialization is correct where its derivatives exist; B1-F1 concerns the missing hypothesis. The convex hybrid-path condition is sufficient for the local defect, telescoping, and stated dyadic bounds; the fixed-order coefficient bound alone is correctly distinguished from a remainder estimate.
- **Gaussian and exact dependencies:** Checked the singular-covariance integration-by-parts recurrence and rational Schur-complement validator. Checked the forest quotient-graph exponent bound, component factorization, isolated vertices and odd-edge cases, and the colored-forest canonical-key proof. The frozen-first-block quadratic certificate has the stated different initialization/metric; its coefficient recurrence, formal reversion, moment interpretation, determinant and polynomial witness require no infinite-series convergence or positive-time population theorem. No missing specialized external theorem was needed for these conclusions.

## Code and tests

Read all supplied production and test code. Checked input validation, exact integer/Fraction restrictions, zero order/zero steps, omitted zero weights, returned ownership, operator-word enumeration, polynomial coefficient generation, rational reversion, determinant pivots, forest validation and keys, and the certificate construction. Inspected the finite-network normalization, scalar scaling arithmetic, activation-copy discipline, zero-step behavior, and declared float64 limitations. Found no additional advertised-interface correction.

Required test command, executed inside the isolated candidate with bytecode disabled:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code python -B -m unittest discover -s code/tests -p test_exact_calculus.py -v
```

Result: **11 tests passed**, 0 failures, 0 errors.

Small independent deterministic checks (no training, random sampling, or high-order campaign):

1. Paired rational coefficients for orders 1–8 and N=0–8 against the direct binomial definition.
2. Twenty-seven exact cubic-loss comparisons using a nonlinear scalar polynomial predictor, three supplied states, three labels including zero residual, and N=1,2,4. Direct truncated Euler composition agrees with (9.P21) in its smooth domain.
3. Fifty singular-Gaussian moment checks for `X=(G,2G,0)` against one-dimensional normal moments and the zero-coordinate identity.
4. Fixed two-neuron finite networks of depths 1–3 with zero, duplicate and opposite samples and unequal positive mobilities: coordinate finite differences of loss, velocity versus mobility-scaled gradients, kernel dissipation, simultaneous GD update, and independent output ownership.
5. Zero-step GD with callbacks that would fail if evaluated: no callback evaluation and independent output ownership verified.

All independent checks passed. They are evidence about the exercised finite operations, not substitutes for the proof or the missing regularity condition.

## Isolation, read coverage, and integrity

Candidate mathematical/code input was restricted to `/tmp/pde_continuation_review_a1` and its `INPUTS.json`. I did not read the project checkout, histories, studies, prior reports, chats, or other agents' work, and did not delegate. I separately read `/etc/codex/skills/solve-math-rigorously/SKILL.md` as instructed. No candidate input was edited. The review artifact is outside the candidate directory.

Every listed file was read from its first through its final line: **11 files, 2498 lines total**. Byte counts, line counts and SHA-256 hashes were checked against the manifest before reading the listed files and again after the complete reading/testing audit. Every pre- and post-audit check matched. The following digests are the identical before/after digests; coverage ranges are inclusive.

| File | Bytes | Lines read | SHA-256 before = after |
|---|---:|---:|---|
| `code/NUMERICAL_CONTRACT.md` | 4890 | 1–91 | `3791adea2ec3a4713a265ab1aa2b00e9993b51a957415060bebc88fe2399de22` |
| `code/pde/__init__.py` | 611 | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | 10108 | 1–249 | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_network.py` | 15525 | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 4464 | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | 10214 | 1–217 | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `docs/NOTATION.md` | 5110 | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 8355 | 1–214 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/gaussian_dependencies.md` | 17119 | 1–346 | `e52365e7ed2afaf3d48272b913caf60e1aa59f55d846019527f84ae15592cf84` |
| `docs/given_space_caps.md` | 18663 | 1–417 | `cdda914e481b46d51366a5d80661cd192b0f319d6507bc8b29eba69d87f9f95d` |
| `docs/loss_pullback.md` | 15809 | 1–363 | `3e14b0633a891b98c2ed25f3e1147e7d5e90b193a021b18e9d2875acb502575f` |
