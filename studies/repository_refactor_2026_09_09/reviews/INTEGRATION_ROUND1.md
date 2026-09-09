# Isolated whole-library integration audit

Verdict: **NOT CLEAN**

Audit date: 2026-09-09. Snapshot root: `/tmp/pde-library-integration.J6HkSP`.

## 1. Scope, isolation, and meaning of the verdict

The only substantive inputs were this root's `docs/`, `code/`, `Makefile`, and `requirements.txt`. No original repository, studies, data, history, other reviews, web sources, or agents were consulted. No previous verdict was used. The supplied implementation and tests were inspected before running the supplied `make check`. No new scientific experiment was performed. No input was edited; this report is a separate output in the private root.

This is a whole-library **integration audit**, with full mathematical proof audits of `gaussian_calculus.md` and `linear_dynamics.md`, and a full audit of the necessary finite identities in `finite_dynamics.md`. The other five mathematical chapters received theorem/convention/dependency-interface audits, including substantial reads of the actual supporting arguments. Their full text was inspected over the course of the audit, but that is **not** a claim to have independently verified every proof step in all 17,223 lines of mathematical chapters. Section 7 makes this distinction explicit.

Two required findings remain:

1. The equal-label chapter uses the reserved sample count `m=2` where it needs the activation floor `c_-=5/6`. This produces false displayed inequalities as written.
2. Two proof displays contain undefined replacement symbols for already defined objects.

These are localized integration/notation defects. The first is more than a cosmetic spelling issue because its literal inequalities are impossible. I found no evidence that the intended principal theorems are false; the indicated repairs do not appear to need new hypotheses. Nevertheless, under the requested shared-canonical-notation and self-contained-proof standard, this exact snapshot is NOT CLEAN. The proposed corrections have not been applied or treated as part of the audited inputs.

Within the coverage below, I found no additional required mathematical or implementation issue, no hidden document/figure dependency, and no improper promotion of a fixed-program result to a continuous-training theorem. Passing implementation tests does not override the findings.

## 2. Required issues

### R1 — Sample count silently replaces the activation floor

Location: [special_data_limits.md:3204](/tmp/pde-library-integration.J6HkSP/docs/special_data_limits.md:3204), with related occurrences at lines 3221, 3233, and [3282](/tmp/pde-library-integration.J6HkSP/docs/special_data_limits.md:3282).

The shared contract reserves `m` for sample count. Part II expressly reiterates at [lines 2138–2139](/tmp/pde-library-integration.J6HkSP/docs/special_data_limits.md:2138) that `c_-=5/6` is the lower activation bound and `m=2` remains the sample count. Section II.D also starts with `c_-=5/6`, `a=7/6`.

But II.D.1 states

\[
\frac12 E(H^{(1)}_1+H^{(1)}_2)^2\ge 2m^2.
\]

With the chapter's `m=2`, the claimed lower bound is 8. Since both features are bounded above by `a=7/6`, the left side is at most

\[
2a^2=49/18<8.
\]

The same incorrect symbol appears in the lower covariance constants `c_1=min(2m^2,d_1/2)` and `c_2=min(2m^2,d_2/2)`. Section II.D.3 then asserts `W^(4)(s)>=ms`. Its zero-readout feature equation is

\[
(W^{(4)})_s=(H^{(3)}_1+H^{(3)}_2)/2,
\]

so `W^(4)(s)<=as<2s` for every positive feature time. The asserted bound with `m=2` is again impossible. This equation and inequality use feature time; changing the physical loss clock does not fix the collision.

Required repair: replace the activation-floor occurrences of `m` by `c_-` at all four locations: `2c_-^2`, `min(2c_-^2,d_1/2)`, `min(2c_-^2,d_2/2)`, and `W^(4)(s)>=c_-s`. Keep `m=2` elsewhere. The lower bound `b_0` at line 3293 already uses `c_-` correctly.

Dependency impact: these bounds feed forward-pair separation, Gaussian density lower bounds, and positive reverse-query covariance in II.D.1–4, hence the every-positive-time motion part of Theorem II.1. With the stated activation floor substituted, the intended positivity arguments have the necessary positive constants. This is not an identified failure of the separately established fitting estimate or of the off-mode finite-algorithm comparison.

### R2 — Resolve two unbound proof symbols to their canonical objects

Locations:

- [special_data_limits.md:2231](/tmp/pde-library-integration.J6HkSP/docs/special_data_limits.md:2231): `X^T X=dC`. The input Gram is `G`; no corresponding matrix `C` is defined. The preceding and following metric formulas use `G^(-1)`. Write `X^T X=dG`.
- [special_data_limits.md:5692](/tmp/pde-library-integration.J6HkSP/docs/special_data_limits.md:5692): `A_2 T_j^1` in the initial forward-response base case. `A_2` is not defined. The action in the surrounding recursion is the initialized `W^(2)`, mapping population 1 to population 2. Use that existing symbol, with its initialization understood as throughout III.N, or explicitly define a typed alias before use.

These are minor repairs, but required by the requested canonical and self-contained notation contract. Neither should be repaired by importing a definition from another document. The intended first-row metric calculation and the same-matrix response identity can be reconstructed from the surrounding in-book definitions, so no new mathematical premise appears necessary.

## 3. Full proof-audit acceptances

These are fresh acceptances of the current text within its own quantifiers, not endorsements based on an earlier review.

### Gaussian calculus — full mathematical read, lines 1–1812

No required issue found.

- Sections 1–2 use Gaussian conditioning with the correct reused-transpose response. The fresh reverse variance is the full input second moment, not a response-subtracted variance. Predictability is essential and is supplied by the chronological query order.
- Finite gradient-direction derivatives and Wick recursion are finite-order statements. The rational Schur-complement PSD test treats a zero diagonal pivot by requiring its row to vanish; singular covariance does not justify an inverse.
- Section 5 explicitly changes to **order-one stored readout**. It concerns each fixed finite depth, fixed number of feature-ascent steps, and fixed nonzero step `h`, including negative `h`. It is not loss GD, and contains no uniform-in-program-length or `h -> 0` assertion.
- The multi-matrix conditional-kernel argument preserves the product conditional law of residual matrix randomness under adaptive interleaving. Every input is known before its answer is sampled. Forward and transpose actions of a matrix are not independently resampled.
- The inverse-free source recursion uses full uncentered Grams and named-source derivatives with selected coefficients and covariance parameters frozen. Distinct formal slots are retained at degeneracy.
- The strict-rank proof was read through its nonconstant, affine, and endpoint cases. Constant normalized activations and the one-hidden-layer branch are handled separately; neither is silently passed through a positive-rank inverse argument.
- The joint coupling, predictable stopping, Gram/Schur controls, and high-moment removal of exceptional events were read as one proof chain. The raw program is defined on the exceptional events as well; stopped estimates alone are not substituted for raw moment convergence.
- Section 6's same-space multiplication obstruction requires the stated unbounded variable and norm/embedding hypotheses. Its divergent-Taylor example is smooth, and the text explicitly constructs a smooth autonomous ODE realizing it. Thus it correctly does **not** infer smooth scalar-ODE impossibility from Taylor divergence.

### Linear dynamics — full mathematical read, lines 1–1166

No required issue found.

- Stored endpoint weights have variance one. The proof vectors `u=W^(1)/sqrt(n)` and `v=W^(4)/sqrt(n)` are embeddings, not a change to tiny stored readout. The common mobility `kappa` is deliberately outside the chapter's unit-mobility kernel.
- Cyclic block multiplication verifies `D C=(C*)^3`, `rank(C^3)<=4`, `f=Tr(C^4)/4`, and the kernel/dissipation identities. These facts also make the traces meaningful on the population space.
- The explicit colored-word source is supported by the chapter's Wick/quotient-graph calculation, including rooted Gram convergence and the variance estimate. No external free-probability representation theorem is a hidden premise.
- The trace-class increment equation is locally Lipschitz on bounded affine-state balls. The rank-four and energy estimates give the required finite-horizon trace-norm bound and continuation. Restart is in the specified cyclic trace-class affine space.
- Fitting uses the proved endpoint-norm/kernel inequalities. The initialized `y=0` population is separately stationary. Neither this fact nor compact-time width convergence proves convergence of finite optimizer endpoints.
- Finite-word Picard approximations, rooted contractions, and finite-rank Schatten readouts are compatible with the source lemma. No operator-norm comparison across different width spaces or empirical neuron-coordinate law is claimed.
- The exact GD argument recomputes the residual from each updated raw state; it is not Euler for a separately stored residual equation. Its dimension-independent estimate supports every deterministic `eta_n -> 0` on each fixed finite physical horizon.
- The nonclosure theorem's connected-contraction growth and stable-independence argument apply to the specified width-uniform bounded-contraction encoders: polynomial identities on open state sets, or analytic identities near zero, including finitely many spatial fields with finite-jet local evolution/readout. They do not exclude arbitrary smooth encoders, a closure along only the initialized Gaussian trajectory, or a field encoding an entire future trajectory. The explicit transport-field and width-one examples delimit that scope correctly.

### Finite dynamics — full dependency proof audit, lines 1–214

No required issue found.

The canonical mean-loss factors are

\[
\dot f=-(2/m)Kr,\qquad
\dot{\mathcal L}=-(4/m^2)r^TKr.
\]

Here the raw kernel includes the block mobilities but not residuals or the loss factor. The first-layer `1/sqrt(d)`, hidden `1/n`, and stored-readout normalizations agree with the implementation. For positive fixed mobilities and `C^2` activations, local finite-dimensional regularity and weighted energy give finite length on each finite time interval; the resulting Cauchy endpoint permits continuation. This is finite-time nonescape, not a claim of bounded parameters as time tends to infinity. Width-uniform finite-horizon norm bounds use the separately stated bounded-slope assumptions.

## 4. Cross-chapter contract and theorem-reuse audit

The following records the accepted interfaces, subject to R1–R2 where indicated. “Global” means a solution exists for every finite physical time; width approximations remain compact-time statements unless expressly stated otherwise.

| Result | Initialization and loss/clock | Actual approximation scope and dependency boundary |
|---|---|---|
| Arctangent, L=2 | One datum; tiny stored readout; `(f-1)^2` | Global finite-horizon joint GF/raw-GD limit, with `eta_n sqrt(n) -> 0`; its own fixed-program source law, transformed-flow stability, cubic raw-GD defect, and observation-tail bridge. |
| Arctangent, L=3 | Same one-datum tiny-readout model; `(f-1)^2`; `eta_n=n^-2` | Uncut population/algorithm theorem only on its explicit positive local interval. Fixed-cap auxiliary flows exist on every finite feature horizon, but are not the uncut optimizer. Sections 3–6 establish the representation and tail premises before cap removal. |
| Shifted arctangent, fixed L>=3 | `1+arctan/10`; one datum; tiny readout; `(f-1)^2`; `eta_n=n^-2` | Own arbitrary-fixed-depth source theorem and chronological response bootstrap. Cap error has Gaussian tails overcoming comparison growth linear in the cap. The positive activation floor places every finite physical horizon inside the constructed feature interval. |
| Special data I | L=2 arctangent, opposite labels, Gram correlation 0 or -1; tiny readout; sum loss | `eta_n=n^-2`; mean-loss clock/step is twice the chapter clock/step. Its own all-moment source/probe/path argument is stronger than the generic W2 theorem. The special-angle transform is not exported to arbitrary correlations. Strict progress and persistent activity, not asymptotic fitting. |
| Special data II | L=3 shifted arctangent, equal labels, fixed correlation in [-1,1); tiny readout; sum loss | `eta_n=n^-2`; mean-loss speed factor 2. Population label-mode clock is established after symmetry; finite off-mode residuals are controlled directly in II.C.4. III.F.1–7 is genuinely a generic fixed-program theorem, allowing these two samples and two matrices. R1 affects the written motion proof. |
| Special data III | Three distinct unit-norm samples under the stated separation, binary labels, each fixed L>=2; tiny readout; half-sum loss | `eta_n=n^-2`; mean-loss speed factor 3/2. Hidden-field normalization does not rescale stored weights, raw metric, or GD. The gain is chosen independently of depth, but finite-width convergence fixes depth and activation first. The broad nonaffinity bound is absolute and depth-dependent; the stronger uniform-margin activation class is separately proved. R2 affects one initial-motion display. |
| Linear L=3 | One datum, arbitrary label; order-one stored readout; squared loss, common mobility kappa | Every `eta_n -> 0`; rooted operator geometry, not nonlinear coordinate-law claims. Its independent word-source proof supplies the needed Gaussian limit. Restricted nonclosure is compatible with its operator closure. |
| Continuous depth | A different scalar-particle residual architecture; initial law in P1; half-mean loss; mobility kappa nL | GF, joint width/depth convergence on fixed physical horizons, using depth-averaged W1. No GD-step theorem and no dense-Gaussian-architecture substitution. Constant initial depth profile supplies the continuous representative used for sampling depth nodes. |
| Finite optimization/controls | Canonical one-datum L=3 arctangent; tiny readout; squared loss | Deterministic event hypotheses and explicit width thresholds give finite GF and exact-GD fitting/endpoints. The projection is a separate finite system; its L1 defect and sufficient cap of order sqrt(n) do not supply a population or GD theorem for that projection. |

### Specific dependency checks

- **Loss normalization.** For `L_c=c sum r_a^2`, the canonical mean-loss vector field is multiplied by `cm`. Therefore `theta_c(t)=theta_mean(cm t)` and `eta_mean=cm eta_c`. Parts I/II use `c=1,m=2`; Part III uses `c=1/2,m=3`. The reference code uses the mean convention. Its default step must not simply be called the same step as a sum-loss theorem. R1 is a different misuse of `m`, not an unresolved loss factor.
- **First-weight storage.** Special-data `V^(1)=W^(1)/sqrt(d)` has row metric `d E|dV|^2`, equal to the canonical metric for `W^(1)`. The corresponding finite factor is `d/n`. Input-span reconstruction preserves frozen orthogonal components and handles antiparallel inputs without an inverse of their singular Gram. R2 is the stray `C` in this otherwise compatible calculation.
- **Feature clocks and actual GD.** The cubic transforms in the arctangent chapters cancel gates only in the continuous equations. Their exact raw-GD expansion retains quadratic/cubic defects, with accumulated terms involving `eta sqrt(n)` and `eta^2 n`. Positive computational clock increments are established on the required interval; auxiliary proof meshes are held fixed in Gaussian width limits. The equal-label two-sample comparison does not impose residual symmetry on the actual finite algorithm.
- **Source laws versus growing transcripts.** The nonlinear chapters prove their own fixed-program conditioning/source statements. In-book reuse by Part II invokes III.F's generic root/matrix scope, not the three-sample training theorem and not Gaussian calculus Section 5's different order-one-readout model. Each training bridge adds a same-width approximation argument and then removes the auxiliary mesh/caps. No growing-transcript estimate is silently imported.
- **Unbounded query products.** The generic bounded-derivative theorem is not applied directly to a product such as `phi'(Z)Q` with unbounded `Q`. The relevant bridges use nested observation truncations, incoming W2 tails, and bounded action norms. Where expected source derivatives are needed, III.V and III.N provide derivative envelopes and an ordered removal of inner/outer caps. W2 convergence alone is not used to infer derivative convergence. The III.N recurrence requires only the stated C2 regularity, not an unstated third derivative.
- **Cap removal and continuation.** I checked the hypotheses feeding the asymmetric comparisons: source-tail estimates precede their use; comparison growth has one cap factor rather than a power of the cap per layer; only the reference needs the tail bound. In Part III, controlled primal/Gram estimates establish capped physical continuation and bounded total control time before the controlled source estimate is transferred to those paths. This avoids a circular appeal to an already constructed uncut population solution.
- **Topology.** Finite vector RMS is explicit, matrix increments use ordinary Frobenius/HS norms, and population contractions stay within a layer. Common-space comparisons do not identify matrix entries across widths. W2 laws include second moments; path W2 uses the supremum path metric and the bound `||z-I_pi z||_infty^2 <= 4|pi| integral |z'|^2`, not just fixed-time weak convergence. Bounded multiplier continuity and scalar prediction differentiability are distinguished from generally false L2-to-L2 Frechet differentiability of pointwise nonlinearities.
- **Finite T versus endpoints.** The guide makes the valid sequential consequence explicit: choose a finite population fitting time for a desired accuracy, then take width/step limits. Neither it nor the theorem interfaces identifies finite GF/GD endpoints with population endpoints. Finite optimization proves its own endpoint result at each eligible width and does not upgrade the local L=3 population arctangent theorem. The finite metric projection clips a different object from the coordinate-query clips in that theorem; the former's L1 defect is not treated as RMS state stability.
- **Nonclosure.** Gaussian calculus's norm/Taylor obstructions, linear dynamics's restricted contraction obstruction, and continuous depth's fixed-linear-moment obstruction have different hypotheses. None implies an unrestricted impossibility theorem for smooth scalar ODEs or finite function-valued states.

### Classical background accepted, with hypotheses checked

No external specialized probability, tensor-program, mean-field, free-probability, or optimization theorem was accepted as a missing proof premise. The relevant constructions are in the snapshot. The ordinary background used in the audited interfaces consists of finite-dimensional Gaussian projection/integration by parts; elementary inequalities and laws of large numbers; dominated convergence, Fatou and Fubini; finite-dimensional spectral/least-squares facts; Hilbert-space adjunction and trace-ideal inequalities; contraction/ODE continuation; and elementary weak-plus-moment transport facts.

In particular, Gaussian integration by parts has the required bounded derivative or explicit integrable envelope, Gaussian square roots are finite-dimensional PSD square roots even at singularity, and continuation uses complete spaces and actual bounded/integrable velocities. Continuous depth Section 7 additionally uses classical disintegration of Borel probabilities on Euclidean product spaces and countable probability-kernel extension: its variables are indeed Euclidean/Borel probabilities with finite first moment where W1 is used. It does not assume a measurable family of optimal couplings over depth. These are classical measure-theoretic background, not hidden study-specific premises.

## 5. Implementation and portability

The complete public code, structural checker, all four test files, and code README were inspected. The implementation's mean loss, residual-free backpropagation, mobilities, raw simultaneous updates, and kernel blocks match finite dynamics. The initializer uses the tiny stored-readout convention; the order-one-readout mathematical chapters are not claimed to be its default initialization. Arbitrary finite correlated, repeated, opposite, or singular-input batches do not trigger whitening or Gram inversion.

The exact Gaussian-moment module matches the finite Wick recurrence and rational PSD domain. It validates covariance even for odd/constant moments. Numerical arithmetic is honestly described as float64, with selected scale-order protections rather than general correct rounding or immunity from intermediate matrix-product overflow. Custom activation regularity and consistency remain the caller's stated responsibility.

Executed from `/tmp/pde-library-integration.J6HkSP`, after inspection:

```text
make check
Library boundary and local links checked: 19 files.
Ran 52 tests in 0.154s
OK
Exit status: 0
```

Runtime check: Python **3.10.12**, NumPy **1.26.4**, matching the pinned requirement. The imported public package was `/tmp/pde-library-integration.J6HkSP/code/pde/__init__.py`. No package installation was performed. The supplied command suppresses Python bytecode and uses the copied code's import path for the tests.

The snapshot contains 19 Markdown/Python files plus the two root build/dependency files. The structural check found no symlink, missing local file link, unresolved declared local module, or undeclared import in its supported syntax. Manual inspection of the actual dependency prose, code imports, file-access sites, and navigation anchors found no out-of-snapshot mathematical source, study figure, generated table, data file, or runtime research dependency. The code README's example does not read external data or write output files. NumPy and the Python runtime are explicit software prerequisites, not vendored contents or mathematical proof premises.

This was a run in the copied root with its installed declared runtime, not a network-disabled fresh-container installation test. There was no new simulation, parameter search, or numerical theorem validation.

## 6. Optional improvement

**O1 — Strengthen navigation checks, without calling them proof verification.** In [check_library.py:47](/tmp/pde-library-integration.J6HkSP/code/tools/check_library.py:47), same-document fragments are skipped, and fragments of other file links are stripped. The current explicit arctangent anchors and their incoming dependency links were checked manually and are present. A future fragment-target check would guard against broken section navigation. This is optional: no broken current anchor was found, and it would not detect R1 or certify theorem assumptions.

## 7. Exact read coverage

Coverage labels:

- **F:** full mathematical read and proof audit, including the displayed supporting argument and exceptional/degenerate cases.
- **I:** theorem, conventions, dependency links, and actual dependency-assumption/interface audit; supporting calculations were inspected as needed. Even when every line was read, this is **not** a full independent proof audit of that chapter.
- **C:** full prose/code/test inspection; not a mathematical proof certification.

| Input | Lines read/inspected | Audit level and focus |
|---|---:|---|
| `docs/NOTATION.md` | 1–98, complete | C; canonical meanings, norms, readout, losses and clocks |
| `docs/README.md` | 1–85, complete | C; every chapter's advertised scope and explicit exclusions |
| `code/README.md` | 1–165, complete | C; API/model mapping, arithmetic and test claims |
| `docs/gaussian_calculus.md` | 1–1812, complete | F; all six sections, including the full fixed-program proof and obstruction boundaries |
| `docs/linear_dynamics.md` | 1–1166, complete | F; operator source, global flow, fitting, width/GD bridge and both restricted nonclosure classes |
| `docs/finite_dynamics.md` | 1–214, complete | F; shared finite gradients, kernels, energy and continuation hypotheses |
| `docs/arctan_limits.md` | 1–3117, complete text inspection | I; L2/global versus L3/local, Sections 3–7 source/cap/GD/gradient dependencies, Section 8 motion premises |
| `docs/global_nonlinear.md` | 1–1796, complete text inspection | I; arbitrary-fixed-depth source bootstrap, tails, feature interval, clock, GD and observations |
| `docs/special_data_limits.md` | 1–6397, complete text inspection | I; all three theorem/convention blocks; I.2–5; II.A–D; III.F/S/G/V/N/A dependency compatibility and observation/motion hypotheses |
| `docs/continuous_depth.md` | 1–1490, complete text inspection | I; A1–A2, characteristic-class theorem, complete profile space, joint width/depth bound, moment-obstruction scope |
| `docs/finite_optimization_and_controls.md` | 1–1231, complete text inspection | I; deterministic event hypotheses, exact-GD width threshold, endpoint versus compact-time scope, projection/defect boundary |
| `code/pde/__init__.py` | 1–26, complete | C; public exports and local import boundary |
| `code/pde/finite_network.py` | 1–363, complete | C; finite equations, initialization, validation, numerical contract |
| `code/pde/gaussian_moments.py` | 1–114, complete | C; rational validation and Wick recurrence |
| `code/tools/check_library.py` | 1–100, complete | C; check scope and limitations |
| `code/tests/test_finite_network.py` | 1–297, complete | C; finite-difference/normalization/algorithm tests |
| `code/tests/test_gaussian_moments.py` | 1–110, complete | C; exact formulas and domain tests |
| `code/tests/test_library_boundary.py` | 1–58, complete | C; temporary-fixture structural tests |
| `code/tests/test_numerical_contract.py` | 1–202, complete | C; arithmetic/callback regression tests |
| `Makefile` | 1–9, complete | C; only the supplied check/test workflow executed |
| `requirements.txt` | 1–2, complete | C; explicit NumPy pin |

The eight mathematical chapters total **17,223 lines**; all 21 inputs total **18,852 lines**. Full proof-audit coverage is the three F rows, not that total. The interface-only designation on the other five chapters remains in force despite the broader text coverage. Searches alone were not counted as full reads; truncated read outputs were followed by reads of the omitted intervals.

## 8. SHA-256 provenance and preservation

The following paths are relative to the private snapshot root, not to any original repository. These exact SHA-256 values match the initial inventory and the post-check inventory. The same 21-file manifest was rechecked after writing the report; no input changed. `REVIEW.md` is not an input and is deliberately excluded from this manifest.

```text
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
f7d3d22e48aac6ed90d4b041c317b10ecf99a538e02e09cf5183fd46d25af95a  docs/README.md
19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  docs/arctan_limits.md
0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362  docs/continuous_depth.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
a12a4f2541dd989a01920541f07ce8f80058b88d3e19db65c4b376c1fcf6653e  docs/finite_optimization_and_controls.md
cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95  docs/global_nonlinear.md
36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b  docs/linear_dynamics.md
94ad0b6a9ba39e937e1f90626c74c6b9d1f652fe20523dcdf1cdbf780bdfeda0  docs/special_data_limits.md
0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
```

## 9. Disposition

The whole-library integration verdict for these hashes is **NOT CLEAN**. Required next work is R1 and R2, followed by a focused recheck of their dependent displays and the canonical notation contract. The optional checker improvement is not a condition of mathematical acceptance. No input repairs, refactor, external coordination, or new experiment were authorized or performed in this audit.
