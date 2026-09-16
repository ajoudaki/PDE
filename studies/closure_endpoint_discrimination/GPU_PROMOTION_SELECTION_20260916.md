# Independent selection: varying-order circle GPU closure

Date: 2026-09-16. Selector: `/root/select_circle`, a fresh scoped agent, not an
author or assembler of the engine or proposed candidate. This is the relevance
and placement gate in RESEARCH_WORKFLOW.md Part 2.1, not a complete scientific
review, correctness certification, incorporation approval, or new experiment.

## Decision

**Accept for assembly with narrowing.** Promote a compact optional Torch
implementation of the established finite circle closure, with public initialized
orders **1, 3, 5**, dimension **2**, and **float64** CPU/CUDA execution. The
smallest suitable destination is `code/pde/observable_torch_circle.py`, a matching
deterministic test module, and an API subsection beside the existing finite
numerical observable solver in `code/README.md`. Existing mathematics supplies
the equations; a new theorem or chapter is unnecessary. A short book pointer is
optional, provided it makes no additional convergence or performance claim.

Do not merge this extraction into a general-dimension initializer or common
tensor framework now. Its useful independent contract is already clear, and
the existing NumPy initializer and restart schema are the appropriate shared
infrastructure. I did not inspect a general-dimension study or implementation,
and this selection neither depends on nor judges one.

## Distinct value, duplication and maintenance

The maintained `observable_solver` already supplies the initialization,
two-population state, nonlinear vector field, physical Heun integration, circle
prediction, paired observables, and exact-value portable checkpoints. Its
float64, Decimal and rational backends and convergence scopes are documented
in the complete implementation guide. Therefore the candidate's value is
**optional GPU execution of that same bounded finite representation**, with a
CPU reference bridge and reusable interfaces. It is not a new closure or a
replacement initialization theory. No measured speedup is claimed here.

`CLOSURE.py` implements the needed tensor contractions in roughly its first
110 lines, but interleaves them with a campaign runner. The mathematical
duplication is small and justified by the different execution backend;
duplicating the dictionary producer, source compiler, ridge normalization or
portable schema would add unnecessary maintenance risk. Import Torch only
through the optional module, so ordinary package use retains its NumPy-only
dependency contract. Initialization may remain on CPU; document the copy and
initialization cost rather than implying end-to-end GPU initialization.

The additional maintenance obligation is backend parity: two devices,
state/data validation, owned arrays, numerical reduction differences and
checkpoint transfer. A deliberately small API and shared producer constrain
that obligation. The extraction should contain no study paths, campaign plan,
retained arrays, automatic stopping, logging policy, or hard-coded runtime cap.

## Selected scientific and numerical contract

| Item | Required retained scope |
|---|---|
| Model | Bias-free two-hidden-layer tanh; normalized directions `u=x/sqrt(2)` in `S^1`; canonical Gaussian variances `(1,1/n,1/n^2)` and mobilities `(n,1,n)` |
| Clock/loss | Physical time, residual `f-y`, unhalved weighted square loss; common factor `-2` in every moving block |
| State | Joint arrays `b1,g,w,p1,b2,c,p2,M,D`; initially `w=g,c=0,M=D`; population zero readout remains the limit of the finite random readout |
| Action | Forward `b2 M (b1^T diag(p1) values)`; reverse uses that same `M.T` and the other population weights |
| Initialization | Call maintained `initialize`; preserve joint marks, separate Q/P rules, reverse-to-forward response and all feature directions |
| Orders | `N=1,3,5`, feature dimensions `(5,3),(35,10),(128,21)`; reject unsupported public initialization orders rather than inheriting every integer accepted upstream |
| Ridge/dictionary | Exact existing schedule `eta_N=1/[1024(N+1)^2]`; inverse-lower-Cholesky normalization; N=5's two redundant constant tail features remain present |
| Time integration | Simultaneous explicit Heun for `w,c,M`; no clipping, fitted clock or sequential block update; clearly stated ownership/mutation semantics |
| Laws/observations | Valid finite weighted circle laws with finite labels; direct passive queries; loss, hidden Grams/RMS and initial/current same-mark paired observations |
| Arithmetic | Torch float64 only in this candidate; no silent down-conversion of Decimal/rational checkpoints or promise of a precision-removal sequence |
| Restart | Save the complete current/frozen state and finite law via the maintained portable schema; restore without invoking initialization or requiring old observation history |

By direct source comparison, the study's `fields`, `rhs` and `heun` use the
same contractions and simultaneous update as maintained `_fields`, `rhs` and
`evolve`. This supports extraction, but does not replace executed verification.
The only built-in small equation fixture explicitly initializes order 3.
Consequently its existence does not certify the advertised 1/3/5 range.

Closure order is an initialization-mark dictionary order, not angular Fourier
resolution. The GPU module must not describe arbitrary orders, arbitrary
dimension, float32/mixed precision, all-depth networks, arbitrary activations,
neural widths or general population integration as supported extensions.

The existing represented-family theorems retain their own stated horizons and
iterated limits. In particular fixed float64 CPU/GPU agreement does not prove
closure-order convergence, a GPU arithmetic-refinement theorem, accuracy at a
specified finite resolution, or validity of wider-law/long-time experiments.
Finite circle laws outside an applicable theorem remain exploratory. No
performance, endpoint, monotone-order improvement or generalization claim is
selected from the historical campaign.

## Required assembly corrections and verification

1. **Library boundary and validation.** Replace raw tensor dictionaries or wrap
   them in a validated owned state. Check finite values, shapes, nonnegative
   unit-mass probabilities, unit directions, common device/dtype and numeric
   arguments; reject booleans masquerading as order/step counts where relevant.
   Guard the float64 conversion boundary. Validate supported order metadata
   and expected dictionary dimensions for initialized/checkpoint imports, with
   a clearly documented supplied-state contract. The current low-level helpers
   rely on the campaign's caller checks and are not a complete public API.
2. **State ownership and bounded workspace.** Prefer fresh-state evolution,
   consistent with the maintained solver, or explicitly name an in-place API.
   Do not let frozen state/metadata alias caller-owned buffers accidentally.
   Suppress accidental autograd-history growth during ordinary integration.
   Add input blocking to the RHS and paired observations, as well as prediction;
   current study RHS materializes the complete training batch. Explicitly
   account for requested full Gram or pair arrays when those outputs are used.
3. **Autonomous observations.** Reconstruct initial first activations from `g`
   and initial second activations from `g,D` and the frozen feature tables.
   `training_observation(..., initial_h)` currently needs external initial
   arrays; the candidate's observations must work from its own saved state.
   Keep activation RMS distinct from paired displacement RMS. If full pairs
   are exposed, preserve their same-population coupling and return weights.
4. **All three orders.** At each selected order verify initializer identity,
   feature counts/tails/ridge, all fields, complete RHS and simultaneous Heun
   against the maintained implementation. Use reached or perturbed states with
   nonzero readout, since initialization alone hides backward-action errors.
   Include unequal input probabilities, correlations, duplicate/opposite
   inputs, and block-size consistency. Use independent gradient or directional
   checks of the physical metric and true transpose; small deterministic
   fixtures suffice, with no new training campaign.
5. **Observables and restart.** Check predictions, weighted loss, both hidden
   Grams, activation RMS, paired movement and any full pair arrays against
   independently reconstructed quantities. Save a noninitial own state, load
   it without initialization, and compare further identical steps with an
   uninterrupted run for every selected order. Preserve all nine arrays, data
   and metadata. Portable value equality is distinct from cross-device bitwise
   equality; state exact-repeat conditions explicitly and use justified
   tolerances for different reduction backends. Test CPU/CUDA transfer and
   actual CUDA execution when available; a skipped CUDA test must be disclosed.
6. **Reusable recipe.** Supply a small standalone initialization/evolution/
   observation/restart example and optional-dependency instructions. Report
   actual test environment and outcomes. Neither the example nor the tests may
   depend on this study or its campaign products. Device policy must be explicit
   without silently changing unrelated global Torch settings.

These are bounded implementation and validation obligations for the selected
engine, not new scientific research to rescue an empirical promotion. A full
paired adversarial review and integration review still follow assembly under
Part 2. The historical campaign remains closed; no experiment was run here.

## Read scope and provenance

Read completely: current `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`,
`docs/README.md`, `docs/NOTATION.md`, `code/README.md`, this study's `README.md`
and `CLOSURE.py`, and maintained `observable_solver.py`,
`observable_initialization.py`, `observable_words.py`. Initial truncated guide
reads were repaired with bounded reads. Read only the opening/model statement
and initial source-equation excerpt at `docs/global_nonlinear.md:12555-12760`
plus section-heading locations; the remainder of that chapter was not read
and no complete proof audit is claimed. No mathematical proof, conjecture
development, external-paper review or research-state synthesis was undertaken,
so the corresponding skills were not invoked.

No other study contents, old reports, generated campaign data, external sources
or the excluded `PROMOTION_SELECTION_20260916.md` were read. The permitted study
README mentions campaign outcomes and the separate selection's existence;
those mentions were not treated as an implementation correctness verdict.
Repository status/HEAD were checked only for coordination. Only this assigned
report was written; no code, shared guide or index was changed. No Git history
was inspected beyond the current HEAD identifier.

Source snapshots (SHA-256):

```text
AGENTS.md 7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747
RESEARCH_WORKFLOW.md 0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85
docs/README.md 0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e
docs/NOTATION.md 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
code/README.md b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e
studies/closure_endpoint_discrimination/README.md ec2d156149ae6d6a4d55ba4c1c2299e507bfc3991ac29deb237f0711a25c0fa2
studies/closure_endpoint_discrimination/CLOSURE.py 20d68cf906f031cde99ed74b225e1cdcad345f72d7ce2676ca62ee660cddf976
code/pde/observable_solver.py 711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605
code/pde/observable_initialization.py 6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2
code/pde/observable_words.py b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5
docs/global_nonlinear.md cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629
```

HEAD metadata at selection: `04b61a12795734cbfc93830bf0a164bab7d101c4`.
