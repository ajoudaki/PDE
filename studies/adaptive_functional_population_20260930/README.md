# Adaptive functional population encoding

The user asks for a representation of deep response-memory populations that avoids high-dimensional polynomial/Fourier cutoffs and is accurate throughout training. This new study investigates nonlinear adaptive atoms, task symmetries and randomized data sketches. It does not import unpromoted findings from other studies.

## Contract

Keep canonical squared-loss training, nonlinear hidden feature learning, depth, and exact initialized Gaussian matrix/transpose reuse. Distinguish sample count m, input dimension d, width n, temporal order q and representation budget M. Count the descriptions of basis atoms as well as their scalar coefficients. A useful construction must be causal and restartable, and must control the feedback of its own approximation error. No dense trajectory or unlimited nonlinear integration oracle is admissible as an uncounted runtime input.

Scientific inputs: canonical equations in the task, maintained docs/index.qmd and docs/notation.qmd, and checked external primary sources. Fixed finite time, L² prediction and state norms are the initial target; uniform-in-width or all-time results require explicit additional proof. No experiment or manuscript edit is authorized by this theoretical investigation.

## Independent routes and ownership

- Root: synthesis and full source/proof verification.
- adaptive_atoms: prompt-only independent nonlinear atomic approximation and causal projection, ATOMS_ROUTE.md.
- task_symmetry: prompt-only independent symmetry quotient analysis, SYMMETRY_ROUTE.md.
- dynamic_sketch: prompt-only independent reference-trajectory empirical approximation, SKETCH_ROUTE.md.

Each route starts independently and sees no other route until its first concrete result is frozen. All proofs stay in this directory; generated products, if later authorized, belong to data/generated/adaptive_functional_population_20260930/.

## Results and current status

**Latest clarified target:** an autonomous trainer with population order p and temporal order q, O(Lnpq+nd) evolving learned state, and no concurrent dense trained driver. The earlier driven encoders below do not meet that target by themselves. The current synthesis is TWO_ORDER_POPULATION.md.

The new construction approximates the population-averaged hidden gradient by p current-state interaction directions, then stores q Legendre moments of their n-by-p factors. A smooth ridge range sketch obtains those factors through two streamed gradient products; no learned dense matrix or full input-response function is retained. Directions move with the current compressed network. Exact initialized matrices remain available. Counting temporary p-by-p algebra, the state is O(Lnpq+nd+Lp^2), which reduces to O(Lnpq+nd) for p<=n and q>=1. Population integration work and its numerical error are counted separately.

SOURCE_GEOMETRY.md proves a width-uniform **source** result at every hidden layer on a fixed finite horizon. If the normalized input law has p-center RMS distortion O(p^(-1/s)), then the best rank-p approximation of the current hidden gradient has Frobenius error at most C_(L,T) rho(t) p^(-1/2-1/s). The proof needs only forward input Lipschitz regularity and backward L2 energy: coarse geometric conditioning leaves a nuclear-norm residual, whose singular tail contributes an additional p^(-1/2). No teacher differentiability or finite sample count is required. A Lipschitz s-dimensional support supplies the data condition; a low-dimensional teacher on full-dimensional input does not automatically supply it.

SOURCE_GEOMETRY_CHECK.md internally verified the complete derivation and requested integrability and storage-accounting corrections, now incorporated. INTERACTION_BASIS_ROUTE.md contains the concrete autonomous equations, the randomized ridge-source estimate, exact Legendre evolution with O(npq) prefix sums, and a conditional finite-n trajectory comparison. Its outer-layer canonical scaling was corrected after the first frozen draft. INTERACTION_BASIS_CHECK.md records its completed internal check; it found no substantive defect and its positive-singular-value qualification and delimiter fixes were incorporated. None of these checks constitutes promotion.

**Unresolved:** the ridge choice needed for a small source error can enlarge temporal-factor derivatives and stability constants. The available comparison does not bound those constants independently of n,p and regularization. Consequently an O(p^(-beta)+q^(-2)) autonomous prediction theorem, and the requested matched-accuracy subquadratic advantage, remain unproved. The rate arithmetic in TWO_ORDER_POPULATION.md is explicitly conditional. No all-time or population-width convergence theorem was established in this continuation.

Three fresh prompt-only routes were independent until their first freezes: population_interaction (INTERACTION_BASIS_ROUTE.md), population_quadrature (QUADRATURE_ROUTE.md), and population_regular_task (REGULAR_TASK_ROUTE.md). The latter two supply, respectively, a sampled-input/history-panel witness with conditional deep stability, and exact population reductions for homogeneous finite-ray tasks or low-dimensional-support polynomial networks. They are alternatives, not extra broad unconditional theorems.

Primary sources checked in full in this continuation: Lubich and Oseledets, arXiv:1301.1058; Kieri, Lubich and Walach, DOI 10.1137/15M1026791. They establish low-rank-dynamics ingredient precedent, not the missing neural width-uniform/data-regularity theorem. Full links and specific distinctions are in TWO_ORDER_POPULATION.md. No new experiments, maintained-code edits, paper edits or Git changes were made.

### Earlier driven encoders

The sharpest encoding rate is in CENTROID_MEMORY.md and applies to the first layer. Normalize the first-layer forward history by the accumulated-activity length. Segment each neuron's weight curve by movement, and replace the history within a segment by a ridge function at its weighted centroid. The linear error cancels exactly. With bounded activation curvature K2 and normalized input radius R, every segment of diameter at most delta gives a uniform-in-input, uniform-in-time encoding error at most K2 R^2 delta^2/2. The source is the actual current weight curve, not a prescribed future path.

Canonical loss dissipation bounds the average weight-path length by rho0 sqrt(T). A shared pool of cells therefore gives O(nd[1+rho0 R sqrt(K2 T/epsilon)]) stored numbers for epsilon-accurate normalized first-layer forward history, on a prescribed finite horizon. This count has no training-sample factor and no input-dimensional accuracy exponent. The common error bound is independent of width when the stated quantities are fixed. It is **not** a width-uniform approximation theorem for the full dense versus closed network. The allocation is adaptive across neurons; the average path bound does not bound each individual path uniformly in width.

The construction is causal and restartable, with discrete cell births and continuous cell statistics. It is a hybrid system, not a single smooth ODE. A within-cell variance certificate makes approximation error observable without retaining the past. For higher temporal moments, local ridge jets give the same per-moment quadratic error with O(qd) state per cell. Reconstruction and feedback may add q-dependent constants. These are local expansions in learned parameter displacement, not temporal Taylor expansions at initialization.

Independent check: dynamic_sketch audited the centroid cancellation, input/time uniformity, canonical energy estimate and pooled capacity. Details are in CENTROID_CHECK.md. These are internal checks, not promotion reviews. No new training was run and no empirical accuracy claim is made.

Other routes are retained as alternatives with explicit limitations:

- ATOMS_ROUTE.md: bounded-variation neural source mixtures and an autonomous fixed-size reservoir. General deep source snapshots still cost a dense network each. This fails the desired learned-state economy.
- SKETCH_ROUTE.md: conditional fixed-reference coreset and functional Galerkin estimates. A coreset is not a functional population encoding; fixed-dictionary approximation requires a substantive source representation bound.
- SYMMETRY_ROUTE.md: exact task quotient under isotropic population inputs and a low-index teacher. Deep response kernels still require Gram/angle information. This does not provide a finite deep closure.

## Fixed-depth extension, 2026-09-30

The follow-up asks for an equivalent width-uniform result at every layer. ALL_LAYER_SYNTHESIS.md collects the proved extension and its remaining limits. For bounded C_b^2 activations, zero readout, bounded normalized inputs and finite label second moment, the exact canonical flow supplies:

- A width-independent nuclear-mass bound for each learned hidden matrix on every fixed finite horizon. Rank-s operator error is O(1/s), without assuming exact low rank or restricting the training-sample count.
- A causal driven encoder for every forward history, with O(1/M) error in neuron RMS uniformly in input and time, using O(ndM+LnM^2) learned descriptors plus one shared exact initialization.
- The same rate for the last backward layer in joint data-neuron L2, with O(M[n+q]) additional descriptors for q history modes. Physical-time moment coefficients avoid division by a small residual norm.

Constants depend on fixed depth, horizon, input and label bounds, activation bounds, and initial hidden operator norms. The Gaussian bounded-operator event is quantified directly. No small-label condition or feature-Gram gap is used. Fixed-width flow existence follows from local regularity and the exact loss dissipation identity. This is not a population-limit theorem.

The three independently scoped routes were all_layer_forward (ALL_LAYER_FORWARD.md), all_layer_operator (ALL_LAYER_OPERATOR.md), and all_layer_curvature (ALL_LAYER_CURVATURE.md). After the forward derivation was frozen, the curvature agent checked it and the separate last-backward extension in ALL_LAYER_FORWARD_CHECK.md. Its internal check passed after notation corrections; this is not a promotion review. The operator route also proves a finite-stream O(ns)-state sketch for signed rank-one updates, with the exact-flow source and driving-quadrature cost kept separate.

The remaining central obligation is a cheap description of **earlier backward histories**, a quadratic all-layer encoding rate, and autonomous feedback. A small preactivation error is multiplied by a correlated backward carrier; ordinary normalized L2 and Gaussian operator bounds do not control that product. Explicit arbitrary-state examples refute this norm inference but do not prove failure along canonical trained paths. Reachable-carrier tail estimates, or a different adaptive construction, remain needed. The requested full all-response theorem is therefore not established.

The encoders described above receive exact canonical trajectory data. Counting that driver restores its dense running state. Neither the representation counts nor the streaming-sketch bound alone prove a smaller autonomous trainer or a sample-independent per-step runtime. No new experiment or manuscript edit was made.

External source checked in full: Bruna, Peherstorfer and Vanden-Eijnden, Neural Galerkin, arXiv:2203.01360v3. It supplies precedent for projecting an evolution law onto a nonlinear functional family. It does not prove the missing deep-neural representation theorem. No priority claim is made for that general projection principle or for elementary centroid quadrature.
