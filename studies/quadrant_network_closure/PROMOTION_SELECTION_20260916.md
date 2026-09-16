# Independent promotion selection — 2026-09-16

Decision: **NARROW for candidate assembly** to the exact factored Heun implementation for the canonical finite two-hidden-layer tanh network. **DEFER empirical promotion** of this study's network/closure and matched-loss NTK comparisons. Do not promote a new closure theorem, a population-accuracy claim, or the campaign drivers.

This is workflow Part 2, step 1 relevance/placement screening. It is neither a complete scientific review nor user approval. The selector is the fresh scoped agent `/root/screen_quadrant`, which did not author or assemble this study. It received the neutral selection assignment and permitted study/established inputs, without another study's scientific findings. No new training, trajectory reproduction, implementation, or canonical modification was performed.

## Smallest selected contribution

Extract the numerical core of `NETWORK.py`: `State`, stable tanh derivative, stream-compatible blocked initialization, forward evaluation, factored physical RHS, and simultaneous Heun step. The scientific contract should stay narrow:

- Exactly two equal-width hidden layers, bias-free tanh, scalar readout, two-dimensional normalized directions `u=x/sqrt(2)`; finite nonempty training batches with uniform unhalved MSE and mobilities `(n,1,n)`.
- Full dense stored middle matrix; independent Gaussian initialization in maintained PCG64 layer order with variances `(1,1/n,1/n²)` and actual finite random readout retained. A supplied finite nonzero state is also meaningful for stepping and deterministic tests.
- Explicit float32/float64 and device contract. PyTorch is an optional dependency for this backend. Do not make ordinary `pde` imports require PyTorch/CUDA.
- Explicit Heun is an approximation to physical GF. It is neither an exact finite-time GF solution nor the maintained raw-GD update. No arbitrary-step stability, loss-monotonicity, long-time accuracy, GPU speedup, or population-convergence guarantee is selected.

The distinct implementation idea is evaluation of the *exact Heun predictor* without constructing a second dense middle matrix. If `H` is the first activation matrix and `L=-(2/(mn))*Delta2*residual` (residual broadcast over columns), then the existing finite equations give `B_dot=L H^T`. At step size `h`, the predictor action on its current first activation `H_plus` is

    (B+h L H^T) H_plus = B H_plus + h L (H^T H_plus).

Its actual transpose on the predictor's backward field is

    (B+h L H^T)^T Delta_plus = B^T Delta_plus + h H (L^T Delta_plus).

The second stage recomputes its residual, gates, activations and endpoint block values; the final middle update is the sum of the two rank-at-most-m stage updates. This uses ordinary distributivity, retains both directions of the same matrix, and deletes no matrix component. These identities explain the selection; a finished candidate must contain their complete canonical derivation and its implementation correspondence.

The full network still has quadratic middle storage and matrix-multiplication work. The optimization avoids dense predictor/velocity materialization: stage factors use order `nm` storage, with order `m²` contractions, in addition to full parameter storage. It is attractive when batch size is small relative to width; it is not a finite-population closure or an efficiency theorem in requested prediction accuracy.

### Destination and boundaries

The smallest suitable destination is one optional backend module, provisionally `code/pde/finite_network_torch.py`, with focused tests and a short subsection of `code/README.md`. A short implementation identity adjoining `docs/finite_dynamics.md` Sections 1–2 is optional if the code guide contains the full derivation. There is no justification for a new theory chapter or changing the global-nonlinear convergence statements.

Keep campaign preparation, hard-coded 16/144-point shapes, seeds, supervisor, GPU assignments, plotting, serialization of this campaign, and performance tables in this study. Do not copy `NETWORK.py` wholesale into the library. The normalized direction convention must be visibly distinguished from the general finite library's physical-input convention; an adapter, if included, must be tested explicitly.

Raw activation Grams `H^T H/n` and weighted closure Grams `H^T diag(p) H` may accompany an example or a small observation helper if the assembled interface needs them. They are not a second substantial scientific result. The existing paired-observation API already supplies the underlying same-population hidden arrays and weights; a separate large diagnostics module would add unnecessary maintenance.

## Duplication and value against the current edition

| Study component | Current established coverage | Selection |
|---|---|---|
| Canonical gradients, mobilities, raw tangent kernel and energy | `docs/finite_dynamics.md` Sections 1–2; `code/pde/finite_network.py` and its guide | Existing mathematics. Reuse these identities and the NumPy oracle; do not claim a new model or theorem. |
| Exact factored finite-network Heun predictor and PyTorch execution | Maintained finite API has NumPy forward/RHS/raw GD/kernel; maintained Heun is for the different observable-closure state | Distinct reusable finite-network implementation; narrow selection as above. No current PyTorch/CUDA backend was found in `code/pde` or its guide. |
| Nonlinear closure initialization/evolution, complete joint populations, transpose, paired motion and restart | `pde.observable_solver`, the full code guide, and C.4.7.10 | `CLOSURE.py` delegates these operations to the maintained solver. No second solver or restart implementation should be promoted. |
| Full activation Gram diagnostics | Existing finite forward fields and closure paired arrays expose the needed fields/weights | Small convenience only; no new closure or identification result. |
| Initial tangent-kernel blocks and spectral frozen flow | Finite dynamics Section 2; C.5 equation C5.11 and finite-clock discussion already supply kernel/exponential/matched-loss principles | The script adds useful finite-kernel arithmetic and a specific comparison, but no distinct theorem. Do not add a second kernel framework to the selected package. |
| Loss explorer and plot packet | Study-specific output interpolation and presentation, described in README | Retain as study artifacts; no scientific promotion selected. |

C.4.7.10's numerical/closure limits have stated represented families and iterated limit orders. Its short-time domain is `[0,1/200]`; its separate time-40 construction uses the explicit extremely small law neighborhood. The quadrant law through `T=100` is outside those declared numerical convergence guarantees. Merely calling the maintained solver on it does not extend them.

This assessment compares the study only with the current established edition. It makes no assertion about overlap with any other unpromoted study; their sources and findings were not read. The coordinator may resolve overlap among independently proposed additions without treating this report as such a comparison.

## Empirical findings retained but deferred

The README reports a completed fixed menu, independent saved-data/checkpoint checks, and passing step/precision controls. It also reports the decisive unresolved control explicitly. The saved `analysis.json` control entries confirm that all three *joint* `(Q,P)` quadrature refinements fail their predeclared tolerances:

| Order | Maximum saved-panel prediction change | Maximum relative Gram change across reported panels/layers |
|---|---:|---:|
| 1 | 0.0224135 | 0.0372929 |
| 3 | 0.116576 | 0.139225 |
| 5 | 0.147523 | 0.211579 |

The corresponding gates are 0.02 and 0.03. Refining both quadratures jointly does not separate initializer error from population integration error, and two finite rules supply no remaining-error bound. Smaller endpoint differences do not discharge the trajectory gate. This blocks a population-accuracy or accurate-internal-evolution conclusion. It does not invalidate the existence of the retained finite computations or the exact Heun implementation identity.

The main finite-resolution example remains potentially useful: close final outputs coexist with large second-layer Gram disagreement, and increasing order does not uniformly improve observables. Its promotion would require an explicit finite-resolution scope and maintained generation/analysis of the full example. No empirical number is selected for the present method-only package.

The NTK extension uses the **full finite initial** mobility-weighted tangent kernel and matches each seed's final network training loss. C.5 explicitly distinguishes that finite kernel from the frozen-readout block, even though their limiting initialized population kernels coincide. The recorded extension has positive small eigenvalues, cross-kernel/oracle checks, singular-case exponential tests and high-precision propagation checks. These support its internal arithmetic account; they are not fresh promotion reproduction of the upstream trained networks. Its very long matched physical times do not make it a common-time comparison. The interactive explorer uses the different loss-of-mean/shared-ensemble-time convention and must not silently replace the endpoint per-seed convention.

No test-label law exists on the passive circle in this study. The reported output RMSE against the network is disagreement/extrapolation, not test-risk accuracy or a generalization advantage. Reproduction would not repair this missing target for a generalization claim. The closure quadrature issue does not logically invalidate a separately reproduced finite network-versus-NTK extrapolation example, but that example still has its own substantial upstream reproduction obligation and is not necessary for the selected small method addition.

The old verifier re-evaluates retained final states and recomputes saved-data identities/metrics. It does not restart all network training and closure production from initialization in a new directory. Reading that report, or replotting retained arrays, cannot satisfy the fresh end-to-end empirical promotion requirement. No new campaign was launched to rescue this gap.

## Maintenance cost and gates still required

The selected core has moderate, bounded maintenance cost: a second numerical backend, optional PyTorch dependency, device/dtype handling, deterministic initialization, and cross-backend tolerances. The mathematical equations remain those of the existing NumPy oracle. The present study functions are not yet a general library contract: tensor shape/device/dtype/finiteness validation, ownership and in-place mutation semantics, finite step validation, supported numerical range, and a clear no-autograd or explicit-autograd policy must be supplied in the candidate. The maintained NumPy core's scaled extreme-range arithmetic protections are not inherited by ordinary tensor products.

Required assembly/review work, without a new research campaign:

1. Separate the selected core from campaign I/O and global runtime settings. Specify the exact supported model, input orientation, update ownership, dependencies and numerical limitations. Keep the optional backend import isolated.
2. Include a complete derivation tying both corrected predictor actions and all final blocks to simultaneous ordinary Heun of the maintained physical RHS. State what memory allocation is avoided without promising measured speedup.
3. Supply meaningful tests against independently formed dense predictor stages from the maintained oracle, with nonzero readout, nonzero residual and changing hidden features. Include forward and transpose corrections, block initialization boundary, repeated steps, declared dtype/device behavior, zero or duplicated inputs where supported, zero residual, and the chosen mutation/rejection contract. Existing single nonzero-state checks are a useful starting point, not a complete final suite.
4. Freeze the actual standalone module, tests, guide and full dependencies. Obtain the two fresh complete adversarial reviews required by Part 2; neither the selector nor an author/assembler can fill those roles. Resolve objections with new complete reviews as prescribed.
5. Run standalone integration checks without study imports/history/retained outputs, obtain the independent integration review, and present the concrete final addition for user approval before editing live established files.

If any empirical campaign conclusion or timing/memory measurement is added later, it reopens the producer-and-analysis reproduction gate. A CPU-only algebra check cannot by itself certify CUDA behavior; unavailable GPU validation must be declared and the supported scope narrowed or held. Nothing in this selection authorizes an additional training campaign.

## Exact reading and action coverage

Required instructions read completely: repository `AGENTS.md`; all of `RESEARCH_WORKFLOW.md`; `docs/README.md`; `docs/NOTATION.md`; `code/README.md`. Long guide reads were split into ranges and the truncated overlap was reread. Skill files read completely: `/etc/codex/skills/investigate-conjectures/SKILL.md`, its `references/evidence-ledger.md` and `references/adversarial-audit.md`; `/etc/codex/skills/solve-math-rigorously/SKILL.md`. The research-assessment discipline was applied. No external mathematical theorem or proof search was needed.

Study files read completely: `README.md` (before this administrative append), `EXPERIMENT_PLAN.md`, `NTK_PLAN.md`, `NETWORK.py`, `CLOSURE.py`, `NTK_COMPARE.py`, `PREPARE.py`, `SUPERVISE.py`, `VERIFY.py`.

Established implementations read completely: `code/pde/finite_network.py`, `code/pde/observable_solver.py`.

Established chapter body ranges read for placement, **not** as a fresh proof audit:

- `docs/finite_dynamics.md` lines 1–122 (complete opening and Sections 1–2).
- `docs/global_nonlinear.md` lines 12555–12735 (C.4.7.10 opening, complete A.1, initial A.2 portion), 13982–14059 (complete D.1), 21314–21395 (C.5 opening/model portion), 21469–21575 (complete passive-input and unique-matching subsection, ending at the next heading), 21913–21968 (complete finite-clock/limitations subsection, ending at the next heading).
- Additional heading/search matches in the named established chapter/API files were inspected only for navigation. Search output was not counted as complete proof or test-body reading. No other chapter proofs or solver dependencies were audited.

Generated evidence read completely as text: `run_001/checks/network_check/check.json`, `run_001/checks/closure_check/check.json`, `network_cpu_check_001/check.json`, `network_cpu_check_002/check.json`, and `ntk_001/ntk_comparison.json` (parsed and displayed in full). Selected JSON fields only: all `run_001/analysis.json` control entries and its top-level keys; `run_001/verification.json` top-level keys and `passed`, `errors`, `changed_frozen_sources`, `elapsed_seconds`. The latter fields report a historical pass and no then-changed frozen sources; they were not independently rerun here.

Unread scientific complement: plot implementations `PLOTS.py` and `NTK_PLOTS.py`, `LOSS_EXPLORER_DATA.py`, rendered figures, raw trajectory arrays, network checkpoints, closure restart payloads, other generated records, the unlisted maintained proofs and test bodies. These are not required to defer their empirical claims and no complete empirical or producer-validation verdict is claimed. Directory/file listings in the permitted study/generated namespace and established trees were used for inventory; no other study was opened or searched. Global Git status exposed only pathname metadata for concurrent work.

Actions were read-only inspection, metadata/hash checks, and creation of this report plus the administrative README append. No deterministic test or experiment was executed. No canonical file, prior artifact, generated product, Git index, branch or commit was modified. HEAD at the check was `04b61a12795734cbfc93830bf0a164bab7d101c4`; the index was empty. Existing unrelated working-tree changes were preserved.

### Input fingerprints

SHA256 of the principal read inputs (before this report and README append):

| Input | SHA256 |
|---|---|
| `AGENTS.md` | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `docs/README.md` | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `studies/quadrant_network_closure/README.md` | `fd66f467b6674b36104e7ea78e8251ab0f99284ec9f38677a6748b0559c54bef` |
| `studies/quadrant_network_closure/NETWORK.py` | `c62090dfc7d43565ed4b3046a2a7eb97b654e204f9149721f5f25ecaa2479679` |
| `studies/quadrant_network_closure/CLOSURE.py` | `8345083495ccd8562ab6f55d30e68398f72059a23acf157db0e9bda102c68611` |
| `studies/quadrant_network_closure/NTK_COMPARE.py` | `a5644125c4b61b3cccab02f0d5f6cc1569b3eee11f3cc2bb160c28d36f723982` |
| `studies/quadrant_network_closure/EXPERIMENT_PLAN.md` | `a77aa2aecbf5cabd126076424cde61e6cfcf02baa5f09fce229376f1271ab706` |
| `studies/quadrant_network_closure/NTK_PLAN.md` | `6a5e5edf447613d642124762835c2d034e05e6807e6e4954427a6aa5f8fa1d66` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/observable_solver.py` | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/global_nonlinear.md` | `cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629` |

The first CPU check belongs to an older `NETWORK.py` hash; the second CPU and recorded GPU checks carry the current selected source hash. Neither is represented as a new selection-time test.
