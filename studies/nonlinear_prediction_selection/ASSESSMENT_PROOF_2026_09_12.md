# Additional independent mathematical assessment — 2026-09-12

No major or fatal mathematical blocker was identified in the inspected proof chain of `CANONICAL_ADDITION_v3.md`. This is an additional mathematical assessment, not a complete promotion audit or a promotion approval. It does not assert that an uninspected dependency or a separate repository integration obligation has been checked.

The assessment was conducted from the supervisor's neutral assignment and the permitted frozen inputs. No study README, history, existing review, other reviewer's findings, other study, or external scientific source was read. The required `solve-math-rigorously` and `investigate-conjectures` skills were read, together with the latter's research-contract, adversarial-audit, and decisive-experiments references. Only this assigned report was written; no Git operation was performed.

## Scope and exact reading coverage

Line numbers below refer to the frozen files as read, rather than the source-document line numbers printed inside the excerpts.

| Scientific input | Complete read coverage | Unread complement |
|---|---|---|
| `CANONICAL_ADDITION_v3.md` | 1–2329, entire candidate | None |
| `DEPENDENCIES_GAUSSIAN_v1.md` | 1–550, entire frozen excerpt, including III.F.1–11 | None |
| `DEPENDENCY_NOTATION_v1.md` | 1–98, entire file | None |
| `verify_reference_certificate.py` | 1–58, entire file before execution | None |
| `DEPENDENCIES_GLOBAL_v1.md` | 1–622; 2936–3243; 3460–4056; 5113–5719 | 623–2935; 3244–3459; 4057–5112; 5720–8901 |

The global-dependency coverage contains complete A.1–4 and B.1; the complete reference construction, symmetry/fitting, and endpoint proof subsections C.4.5.1 §§1–3; its complete rational-certificate subsection §5; complete C.4.5.2; and complete C.4.6.3 §§1–6, including the cavity comparison, Gaussian maximum estimate, finite-feature transfer, and simultaneous reference envelope. In particular, the envelope used for the candidate's endpoint independence was checked back through its proof rather than accepted from its label. The other hidden-motion calculation in C.4.5.1 §4, the rest of C.4.6, and C.4.7 were not read. The candidate's new control-mass recursions and finite-GF argument were assessed directly using the inspected Gaussian/value/continuity foundations; this report does not independently certify all of C.4.7. No missing scientific input prevented the bounded assessment, but the listed unread complement remains outside its assurance.

Frozen input SHA-256 values:

```text
CANONICAL_ADDITION_v3.md
c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879
DEPENDENCIES_GLOBAL_v1.md
6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942
DEPENDENCIES_GAUSSIAN_v1.md
c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77
DEPENDENCY_NOTATION_v1.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
verify_reference_certificate.py
07c51c139ebf66912ef7b730201dcc71581b11355dd29dbee6140bf2bba63118
```

## Substantive mathematical checks

### 1. Integrated control mass supplies the asserted horizon independence

The object proved in A is a deterministic finite-program statement, with total variation of controls close to the entire physical reference history (candidate 217–274). It does not quantify over arbitrary random finite-network feedback. This distinction is necessary and is observed in the later finite-width passage.

The key bounds are expressed in total coefficient mass, not the number of nodes or elapsed physical time. Exact interval integrals give `q_disc <= q` and total common mass at most `2 L_* + q` (300–317). Normalizing a pulse by `m_p = |gamma_p| + |bar gamma_p|` makes its direct mismatch cost `e_p`, with `sum m_p e_p = q_disc`. Thus genuinely new inputs and vanishing reference coefficients cause no inverse-small-mass singularity.

I checked the causal dependence in CT13–CT16 (341–387). A current forward answer uses earlier reverse responses; a current backward response then uses that newly constructed forward row and previous upper derivative rows. The current diagonal is the derivative of its own forward slot, not a cumulative contribution from every previously unused passive query. Zero-control slots consequently have no later influence (389–395). These are substantive protections against row growth from padding.

The reference anchor separates fixed-graph width passage, zero-forcing coefficient continuity, and later mesh refinement (416–558, 866–961). The fresh-root integration-by-parts extraction is justified by the full forced expression and continuity of its named coefficients, including singular covariance supports. The inspected dependency supplies the same construction explicitly (global 3651–3900). The clock/raw distinction is respected: CT22 is a nonzero raw-to-clock defect. Its differentiated bound involves `exp(2h|b|)`, and its normalized summed error is controlled by `sum h_k^2 <= L_* h_max`; it is not treated as an exact discrete coordinate equivalence.

Under a temporary past-row cap, CT27 is Gaussian plus a bounded remainder. Jensen's inequality applied to the weighted sum of absolute queries gives CT28 without taking a maximum over a Gaussian history. This supplies every fixed moment of the pulse amplification. The interpolation exponent `1/11` from L2 and L24 to L12 is correct; weakening to `1/16` is harmless. The products in CT40 use at most three L12 factors and one L4 amplification factor, giving L2 control. The upper-row comparison uses pointwise sums of source derivatives and deterministic coefficient masses, not a random maximum of their differences (663–835). Its right side involves only earlier beta errors. Consequently the strict first-failure argument in CT45 closes with constants independent of physical horizon (837–860).

No unproved Lp operator bound for the initialized action is needed in this chain. The action estimates use L2; higher moments come from the source expressions.

### 2. The full row and the actual adjoint live on a compatible carrier

The frozen Gaussian construction includes the complete first-row root, both orientations of each initialized matrix, and finite unions of programs. Its source rule retains separate names on singular supports (Gaussian 170–276). A transpose answer is correlated with a forward answer through its response correction; independence of the centered orientation-source groups does not replace the transpose by an independent operator.

The countable generated language is dense in the generated L2 spaces, finite operator bounds pass to that dense span, and finite transpose pairings pass to the true Hilbert adjoint (Gaussian 296–391). The global A.3 proof supplies the sharper norm bound two. Only increments are Hilbert–Schmidt, with finite representative `uv^T/n`, consistent with the candidate's raw metric and mobilities.

This construction supports the common cross-program source isometry CT17 and the full-history prefix approximation in C.4. The countable dense parameter construction plus the proved uniform comparison extends to the compact parameter rectangle; it does not choose unrelated carriers for different parameters (candidate 1646–1728). No finite-dimensional compression claim is being made.

### 3. Endpoint conditioning has a checked source mechanism

The inspected reference proof supplies the unique first fitting feature time, exponential physical approach, and endpoint raw/readout bounds (global 2936–3243). Its global-in-physical-time query envelope is obtained on the bounded feature segment using a full learned cavity comparison and finite-list passage to the canonical space (global 5113–5719), rather than by assuming independence of trained queries and initialized columns.

The candidate uses that envelope correctly in 993–1049. The Gaussian box probability decays as `exp(-O(r^2))`, whereas the envelope event `N > r^2` has probability `exp(-Omega(r^4))`. Their positive-probability intersection needs no independence. On it, the integrated clock perturbation is polynomial while the inverse-gate derivative near a large Gaussian root is exponential. Hence `w_dagger` approaches the original root on those boxes, and the limiting tanh signs separate every finite nonantipodal direction list. Crossing one perpendicular line isolates one coefficient in a putative feature dependence.

The middle-block Gram lower bound (1070–1102) then follows by applying the first-feature Gram inequality at each upper coordinate and integrating. Since the fitted readout is nonzero and each upper tanh derivative is strictly positive almost surely, each upper backward factor is nonzero. Compactness and continuity give a positive uniform lower bound on the specific three-input rectangle. This does not require injectivity of the trained action or an evaluated numerical eigenvalue.

### 4. Construction and slow selection respect the initial layer

The one-reference cutoff estimate leads to the modulus `omega(z) = z sqrt(log(e/z))`. Its reciprocal is nonintegrable at zero, and the explicit integral comparison in C.2 proves uniqueness as well as Euler completion (1526–1588). Thus the merely continuous ambient gradient is not used as though it were locally Lipschitz, and existence is not inferred from continuity in an infinite-dimensional space.

The constrained Euler histories first satisfy the full-history source-tube condition by their bounded appended mass and the small omitted reference suffix. Only then are source tails used to complete them (1646–1719). The two fitted predictions are preserved by `G* Pi = 0` and the legitimate scalar chain rule.

For actual mixtures, C.6 establishes fixed-prefix control closeness before applying the new source cap (1879–1926). A partial last Euler step is itself a finite program with proportionally shortened last coefficients. Its recomputed queries therefore receive the source bound while that affine segment remains inside the outer stopped regions. Its fixed row velocity is L4-bounded, so the derivative argument in C.5 applies to the segment. This justifies the residual remainder

`|R_k| <= C h_k^2 (|r_k| + epsilon)^2`

at 1928–1978. Absorption and telescoping yield the integrated residual estimate without an accumulating `h T` term. It is then the sum of the reference suffix, fixed-prefix discrepancy, residual transient, and `C tau_0` that closes the continuation through order `1/epsilon` physical time (1980–2018).

The exact identity `theta' = epsilon V_p(theta) + B(theta) r'` is algebraically correct (2020–2057). Along reached curves, L4 query bounds control the otherwise problematic product `w' Q`; this gives absolute continuity of the anchor gradients and `|B'| <= C(|r| + epsilon)` without assuming an ambient Hessian. Integration by parts leaves an error bounded by the prefix error, its residual, its residual squared, and `epsilon`. Taking `epsilon` to zero at fixed prefix time and only then sending the prefix time to infinity proves selection. The final change from shifted to unshifted slow time excludes `tau = 0` and pays only `C epsilon b` (2059–2117). No response expansion is extrapolated to a diverging horizon.

The risk and hidden-activation conclusions also have separate proofs. The fixed-readout hidden contrast has initial derivative `-2 r_dagger ||d_H||^2 > 0`; its uniform derivative continuity retains a positive sign over a fixed short episode. Cauchy–Schwarz converts its increase to the claimed upper-hidden displacement (1261–1418). The displayed risk and displacement constants have the correct factors.

### 5. Actual finite GF is recovered in the stated iterated order

D keeps epsilon and the physical horizon fixed during each width limit. Finite loss dissipation gives the required bounded raw displacement and readout supremum; it is not substituted for query-tail control. The actual small Gaussian readout is retained and compared to a zero-limit-readout oracle only through a fixed-program cutoff induction (2166–2214).

The source tails belong to fixed proxies with population coefficients. Hard tails are bounded through continuous soft-tail second moments, so their empirical passage uses the actual fixed-program observation theorem. Cutoff amplification grows exponentially in R, while the population tail decays as `exp(-a R^2)`; choosing R and then a sufficiently small finite mesh yields the needed comparison (2216–2268). This is compatible with every separately fixed positive epsilon and claims no joint width/epsilon rate.

Finite input nets and bounded raw/input velocities give the full-circle prediction conclusion. The union of reference and mixture proxy programs on the same arrays retains the mixed activation products needed for the paired statistic (2270–2303). The reference endpoint is taken after the fixed-horizon width passage. I found no optimizer change, finite-readout reset, independent-transpose substitution, or exchange of these limits in this bridge.

## Bounded deterministic check

Before execution, the check was fixed as one unchanged run of the supplied certificate, with a 60-second timeout and no replication or follow-up experiment. Passing required exit zero and every exact rational assertion. Failure of an assertion would invalidate the corresponding constant margin; timeout or environment failure would have been inconclusive. This checks constants, not trained trajectories.

Executed with Python 3.10.12:

```text
timeout 60s python3 studies/nonlinear_prediction_selection/verify_reference_certificate.py
exit status: 0
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

The code was inspected before execution. It uses exact rational Taylor bounds and outward rounding; decimal output is only a summary. Its stated assertions, including `q > .39`, `q < .4`, and the lower margin yielding `m >= .1`, passed. No stochastic or training computation was run.

## Remaining limits of this assessment

The conclusion is absence of an identified central blocker within the stated coverage, not a claim that independent checking is infallible. The numerous unnamed enlarged constants in the source bootstrap were assessed for finite, causal, horizon-independent dependence; they were not converted into useful numerical episode lengths or a machine-checked proof. Neither practical effect size nor a simultaneous width/contamination rate is established. The theorem's scope is one small but nonzero slow-time episode near the fitted reference, not changed-law endpoint convergence, arbitrary-law global existence, or a raw-GD extension. Promotion requirements, repository integration, and the explicitly unread dependency complement are outside this report.
