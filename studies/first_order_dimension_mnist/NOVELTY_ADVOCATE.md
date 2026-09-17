# Advocate: independently frozen opening

Date: 2026-09-16. Role: advocate in the authorized retrospective scientific assessment. This opening was composed without access to the critic's opening, earlier debates, earlier agents' verdicts, or unlisted studies. The investigate-conjectures skill and its four assigned references were read and applied. No experiment, new proof search, source modification, or promotion is undertaken.

## Strongest supportable positive case

The work deserves to be treated as a substantive constructive contribution to nonlinear wide-network dynamics, and as a credible candidate for an important numerical method. Calling it merely a rephrasing of low rank, mean field, backpropagation or Galerkin misses the scientific object: an explicitly initialized, current-state, autonomous approximation family that preserves the forward and reverse uses of a dense Gaussian matrix, learns nonlinear hidden representations, and is proved to converge to the original network's population gradient flow in stated domains. The valuable combination is the representation plus its identification and convergence theorem, not a new name for a familiar projection.

The maximal defensible significance case is that it offers a bridge between rigorous feature-learning limits and practical reduced simulation. Dense Gaussian initialization is retained at the target level; the low-order surrogate approximates its action on a generated observable space instead of simply declaring the Gaussian bulk absent. Initial coefficients are computed without a teacher trajectory. The numerical state has fixed size during evolution and restart. Both population coordinates and the middle coefficient matrix learn. Qualitative theory includes joint initial/current hidden observations and both action directions, not only loss. Existing sparse-circle and MNIST evidence shows this is more than a formal construction whose first useful order is inaccessible.

I provisionally rate the mathematics **3/4, substantial specialist advance**, the numerical method **2/4, credible useful scoped method**, and wider ML **1/4, promising proof of concept**. Here 0 means no supported contribution, 1 means a sound useful construction or restricted proof of concept, 2 means substantive validated result in a limited class, 3 means an important advance across a nontrivial specialist problem class, and 4 means a foundational or broadly enabling advance under explicitly demanding evidence. These are scientific assessments, not priority certifications or predictions of community adoption. I will defend raising numerical significance to 3 if matched cost/fidelity comparisons against strong ordinary alternatives succeed; a practical error-controlled approximation to a broad genuinely trained Gaussian regime could earn 4 in the specialist mathematical/numerical field even before broad ML adoption.

## What the closure actually is

At fixed order N=p, retain two populations with frozen initialized feature marks b1,b2 and moving lower vectors w and upper readouts c, plus an unrestricted feature coefficient matrix M. For input u, form a=E[b1 tanh(w·u)], then h2=tanh(b2^T M a), f=E[c h2]. The reverse signal uses M^T and the same marks. Their exact velocities are the gradients of squared loss for the population L2 metric on w,c and Frobenius metric on M. Backpropagation remains, represented by these contractions.

With quadrature arrays, the effective middle matrix is B2 M B1^T diag(p1). Consequently the finite computation is algebraically a trainable structured bottleneck network with fixed outer factors and a particular weighted parameter metric. This is not a defect: numerical discretizations often admit a familiar finite architecture. Its value is why those frozen factors/initial coefficients were chosen and what increasing the hierarchy approximates. Arbitrary low-rank factor training or a post hoc fit to a trained network is a different algorithm. The continuum fixed-order state still contains two full probability laws on finite-dimensional spaces; it is not finitely many scalar moments. Particle resolution and dictionary order are independent.

N is initialized-mark resolution, not Taylor time order, Fourier cutoff, neuron count, or a depth index. Nonlinear tanh remains intact at N=1. Fixed w,c are not polynomially truncated. The maintained theorem's exhaustive bounded-word tail is essential to density; a polynomial core by itself has not been shown to generate the full required action space. N=0 is not a maintained NTK. Degree dimensions and integration cost can grow sharply; the general-d N=1 moving-state count O(Pd+d²), versus O(nd+n²), is useful at d much smaller than n, not uniformly across growing dimensions.

## Exact theory and limitations

I read complete docs/README.md, docs/NOTATION.md and code/README.md, C.4.7.9 and C.4.7.10 through the time-40 construction, and the relevant study initializer derivation/equations. C-H2 is a regularized two-sided Galerkin-type action approximation with Q_l=U_l U_l*, positive contractions rather than orthogonal projectors. Strong convergence in both orientations, compactness of the reachable query sets and Hilbert–Schmidt learned-increment sources make the omitted source vanish; one-reference backward-tail estimates then propagate the error. This is a nontrivial bridge beyond formal hierarchy identities. The scheme does not use the proof's target-dependent error to initialize or evolve.

The strongest current theorem is nevertheless scoped. The practical represented nonorthogonal two-arc family has T=1/200. The time-40 family has rho=2^{-E10}, E0=8192, E(j+1)=2^{Ej}; at recorded precision its supported perturbations collapse to the orthogonal reference. The positive radius is a real mathematical neighborhood and independent of resolution, but cannot honestly be sold as practically resolved diverse geometry. Fixed-order well-posedness for larger domains is not convergence there. No theorem covers the high-dimensional MNIST run, arbitrary long horizons, monotonic improvement in N, an arbitrary joint refinement, or a useful cost-to-accuracy rate. Numerical limits remove arithmetic, time mesh, input quadrature, population quadrature, initialization quadrature and source regularization before outer order. Finite-width identification is separate.

## Empirical argument, including contrary evidence

The MNIST study sources required by the assignment were read, including README, REPORT, PCA_REPORT, INITIALIZATION_THEORY, MODEL_SCOPE_CHECK, COMPUTE_REPORT, FULL_4096_CHECK, PCA_RUN_CHECK and producer equations. Nominal P4096 means 2048 antithetic base draws, not 4096 iid particles. The learned matrix is unrestricted inside the dictionary. At approximately common MSE0.011080311898, original same-representation mean validation RMS is0.0431777, PCA same-representation0.0416288. PCA relative error is4.09–4.62%; within-digit correlations around.98 show nontrivial sample detail beyond class signs. Same-device fixed-T100 integration gives3.75–3.96× speedup and80.20% lower live allocated memory for PCA closure versus PCA network. Independent replay, half-step controls and5,607 analysis checks make these unusually well-supported internal finite results.

PCA centered the data, retained only53.05% of original uncentered energy, and changed the coordinate dictionary; it is not a test of discarding merely2% of input information. PCA closure/original-network RMS0.1053142 and PCA-network/original-network0.0975023 show a genuine representation effect. Runtime is not time to matched loss or fidelity. Three seeds, one digit pair and no smaller-network/general-bottleneck comparator leave economic superiority open.

The authorized circle evidence strengthens the positive case. In closure_circle_spectral_mechanism, actual 4096-network pair functions are approximated at roughly0.66–3.99% circle RMS by N1/3/5; all nine widest-width individual pair functions fit a tanh–sine family within5%. N3 improves on N1 across all three pair geometries and all six multiple-point geometries descriptively. Quad30 passes the complete available order-improvement gates:7.46→3.89→2.08% error. Closures differ from their own frozen kernels by53–55% at the controlled30-degree pair, far beyond measured numerical differences. Thus ordinary frozen-kernel dynamics is an inadequate explanation of that result.

The adverse circle record is equally important. Triple40 quadrature controls fail; four of six multiple-point cases lack matching closure controls; N5 sometimes worsens the observed error. Quadrant second-layer Gram error remains~.65 even when output is close. XOR and quadrant initial-kernel predictions remain very different at matched training loss, but no external teacher is specified off support. Endpoint-discrimination T1000 is not settled, fails two numerical gates, and N5's improved prediction does not uniformly improve hidden Grams. Wider-arc/long-circle quadrature remains unresolved. closure_feature_geometry currently has only its initial README, no completed result to add. None of these is promoted or an external replication.

## Independently inspected primary prior art

The search is non-exhaustive. I searched current and older combinations of Galerkin, closure, low rank, mean field, feature learning and infinite width, including2025/2026. Exact access coverage is stated, not inflated to reading entire long papers.

- Yang–Hu, Tensor Programs IV, [main paper](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf), §§2–5; [supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), Appendix A and G, especially DefinitionG.3/TheoremG.4. Inspected model scaling, discrete feature-learning classification, Gaussian source/transpose response rule and fixed-program theorem. Strong direct precedent for feature learning, Gaussian reuse and initialized contractions. Additional GF uniformity and fixed-current-state hierarchy convergence are not supplied by the cited fixed-program statement.
- Bordelon–Pehlevan, [DMFT](https://arxiv.org/pdf/2205.09653), §§1–3, computational discussion/table and AppendixB Algorithm1. Inspected nonlinear feature-learning stochastic process, kernels indexed by two times and alternating Gaussian-process simulation. It is a direct conceptual and computational predecessor, including non-NTK behavior. The reported kernel memory scales with the time grid; the present fixed-resolution current-state storage is a concrete distinction. Different initialization/scaling must be mapped before asserting the target flows coincide.
- Yang–Santacroce–Hu, [pi-limit](https://openreview.net/pdf?id=tUMr0Iox8XW), indexed primary abstract/introduction and author [publication page](https://www.microsoft.com/en-us/research/publication/efficient-computation-of-deep-nonlinear-infinite-width-neural-networks-that-learn-features/). PDF access hit a browser challenge. It proves/implements an efficient feature-learning limit of projected GD with appended gradients; cannot be ignored as a prior computational route. It changes the target optimizer; full exact equivalence remains unverified here.
- Huang–Yau, [Neural Tangent Hierarchy](https://arxiv.org/pdf/1909.08156), §2, Theorems2.3/2.6 and equations2.7–2.10. Direct prior for a truncated evolving neural hierarchy and error theorem. Its kernel/width expansion and initialization assumptions differ from the current order hierarchy approximating an already nonlinear population GF.
- Nguyen–Pham, [multilayer mean field](https://arxiv.org/pdf/2001.11443v3), abstract, setup and theorem/initialization passages in §§4–5; Celentano–Cheng–Montanari, [rigorous DMFT](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf), abstract/setup/applications/theorem passages; Chizat–Bach, [particle transport](https://arxiv.org/pdf/1805.09545v2), §2.4 Theorem2.6. These establish rigorous prior nonlinear population/particle or DMFT theories; broad claims that such mathematics did not exist are false. They do not, in the inspected passages, establish this exact closure contract.
- Koch–Lubich, [dynamical low rank](https://epubs.siam.org/doi/pdf/10.1137/050639703), primary abstract only. Tangent-space projection onto moving rank-r manifolds is a longstanding numerical idea; this construction instead fixes initialized action spaces and evolves an unrestricted core. A familiar low-rank ancestor does not establish equation-level identity.
- Göring et al., [2026 mean-field feature learning](https://arxiv.org/pdf/2510.15174), abstract and introduction inspected. Bayesian/SGLD posterior closure is current related work, a different target from deterministic physical GF. This search hit reinforces that broad novelty slogans are unsafe.

The smallest surviving novelty candidate is therefore the exact combination: a constructive initialized observable dictionary retaining response-aware Gaussian actions, finite autonomous current populations and matrix coefficients, proved convergent in prediction plus joint hidden/action observations to the stated unmodified nonlinear Gaussian GF, with a finite numerical realization and explicit restart/storage contract. I have not found a matching theorem in the inspected passages; that is not a proof of priority. The present numerical evidence makes the candidate scientifically consequential enough to investigate seriously.

## Opening demands for the debate

I will object to collapsing contribution-level novelty into novelty of primitive operations; to requiring broad ML superiority before recognizing a mathematical advance; to treating unresolved quadrature as disproof of all finite empirical information; and to treating a positive but tiny theorem domain as no theorem. In return I accept that no-breakthrough verdict for wider ML is currently justified, that a structured-network comparator is mandatory for numerical superiority, and that priority and practical high-order convergence remain open. The final agreement must specify thresholds which, if passed, commit both sides to actual significance upgrades rather than merely inviting reconsideration.

Opening status: FROZEN. Subsequent debate/concessions will be appended below without changing the opening.

## Direct debate record (after frozen opening)

The opening above was frozen before reading the critic, with SHA256
`e4358e200ddc4cc6b1f55f18084d5e238c830a49f835e817046ce2f0cf76a96f`.
Everything below is later debate material; the opening is preserved verbatim.

### Exchange 1: objections, attribution and proposed tests

- **C01 (critic):** finite architecture/backprop are familiar. **Evidence:**
  canonical H2.4–H2.7 and the finite weighted forward map. **Response:** accepted
  as already acknowledged by my opening; construction provenance and unchanged
  target approximation carry the proposed contribution. **Disposition:** closed
  on this scope, subject to final exact wording.
- **C02 (critic):** low-rank/Galerkin/ridge/autonomous-ODE primitives are classical.
  **Response:** accepted. The difficult coupled obligations are initialized joint
  law, actual adjoint, target identification, and convergent two-sided action
  approximation. Familiar tools neither certify nor negate the combined result.
  **Disposition:** factual agreement; degree of significance remains open as A01.
- **C03 (critic):** TP/DMFT/pi-limit precede nonlinear infinite-width computation.
  **Response:** accepted. The prior scalings/training laws must be compared
  explicitly. I do not claim first feature-learning limit, first deep limit, or
  first computable nonlinear infinite model. **Disposition:** closed, priority
  of the whole present contract jointly remains unverified.
- **C04–C05 (critic):** theorem domain and convergences/cost must remain scoped.
  **Response:** accepted, including the extraordinarily small time40 family,
  no MNIST theorem, distributions versus finitely many numbers, distinct limits,
  and no dimension-free or fixed-order arbitrary-accuracy claim. **Disposition:**
  closed on facts; domain's grading implication debated as A01.
- **C06–C08 (critic):** measured savings are not a cost/fidelity frontier; good
  output can coexist with poor hidden geometry; network-shaped extrapolation is
  not ground-truth generalization. **Response:** accepted in full. Existing
  controlled nonlinear signals and measured savings still support a significant
  simulation proof of concept (A02). **Disposition:** closed factual scope;
  grade and future controls negotiated below.
- **C09 (critic, later):** finite coordinate-anchored order need not be rotationally
  invariant. **Evidence:** spectral INSIGHT.md reports roughly 2.6–2.8% N1 and
  0.7–1% N3/N5 rotation differences, with stated control qualifications.
  **Response:** accepted; PCA changes coordinates, centering and scaling as well
  as dimension. Rotation and same-target preprocessing controls enter the
  numerical milestone. **Disposition:** closed.
- **A01 (advocate):** the combined constructive theorem could merit *highly
  significant within rigorous approximation of deep Gaussian feature-learning
  dynamics*, while merely *significant* across wider deep-learning theory.
  **Evidence:** complete initialized-word law, both operator orientations,
  unchanged target, autonomous restart, declared-observable convergence; none
  is supplied just by calling a network low rank. **Critic response:** pending.
  **Disposition:** open; no agreed grade yet.
- **A02 (advocate):** denying any numerical significance until competitive
  frontier tests confuses a meaningful proof of concept with a validated superior
  method. **Evidence:** internally controlled current MNIST/PCA differences,
  real allocation/runtime savings and resolved quad30 order transitions.
  **Critic response:** already offers “significant proof of concept for
  simulation; superiority unestablished.” **Disposition:** compatible wording,
  final rubric pending.

Independent primary-source checks after freezing further constrain novelty:
Denil et al. (2013), [sections2–3](https://proceedings.neurips.cc/paper/2013/file/7fec306d1e665bc9c748b5d2b99a6e97-Paper.pdf),
explicitly use W=UV with fixed dictionary U, learned V, ridge-derived bases and
a fixed-pooling interpretation. [LoRA-XS](https://arxiv.org/pdf/2405.17604),
sections3.1–3.3, gives two frozen factors with a learned inner matrix and
Frobenius projection. [LoRA-SB](https://arxiv.org/pdf/2411.19557), section2 and
Theorem3, explicitly corrects coefficient gradients using both factor Gram
inverses; its actual chosen orthonormal bases simplify that correction.
I directly read those model/method passages, not their complete proof appendices
or experiments. These are direct antecedents for even the two-sided/core and
metric ingredients. Their pretrained additive-update targets do not by these
passages identify the present initialized Gaussian population theorem. No
architectural-priority or metric-priority claim survives this comparison.

### Exchange 2: resolved grades and concrete upgrades

- **A01 resolution.** The critic agreed that the law/adjoint/target/autonomous
  approximation package is substantive and not dismissed by primitive
  familiarity. The missing consequence for *highly significant* is a robust
  nondegenerate long-time family or useful quantitative approximation control.
  The present T=.005 guarantee and practically microscopic time40 family do
  not supply that consequence. I accept this bottleneck-based rubric and
  withdraw my higher present mathematical grade. **Disposition:** closed with
  one common grade, significant substantive specialist mathematics. No broad
  ML-success requirement was imposed on the mathematical upgrade.
- **A02 resolution.** The critic accepted significant numerical simulation proof
  of concept now, while frontier superiority remains unestablished. Both accept
  wider ML as promising proof of concept below an established significant
  methodological advance. **Disposition:** closed. The final rubric replaces
  both openings' differently calibrated numeric scales with common verbal
  levels and explicit fields.
- **C10 (additional prior art).** Claim challenged: two frozen sides, trainable
  inner core or metric awareness could itself be novel. **Evidence:** direct
  Denil/LoRA-XS/LoRA-SB passages above, independently checked by both. **Response:**
  I accept the stronger prior match; retain only the combined initialized-law,
  unchanged-target approximation claim. **Disposition:** closed.
- **C11 (current DMFT literature).** Claim challenged: history-based DMFT
  necessarily has full quadratic-memory storage, or nonlazy kernel computation
  is new. **Evidence:** Lauditi–Bordelon–Pehlevan2025 §§2–3/Figure1 and
  Lang et al. DYNAMITE2026 §§3.1/3.6/4.1, read directly by both agents.
  **Response:** adaptive nonlinear kernels precede this work under different
  activation/training/fixed-point assumptions. DYNAMITE appends and thins time
  history and reports sublinear memory on spin-glass tests; no universal
  quadratic lower bound follows from the older full-grid solver. **Disposition:**
  closed, with eligible compressed-history comparators in N and no unproved
  same-target equivalence or superiority claim.
- **M01 (numerical milestone loopholes).** My proposed eight-case campaign and
  2x runtime/memory thresholds were accepted. The critic correctly objected to
  relative output denominators at zero initialization, weak seed uncertainty,
  unspecified baseline tuning, and hidden target-oracle cost. **Response:**
  accepted absolute label-unit uniform-time RMS, at least ten seeds or stronger
  rigorous control, simultaneous95% bounds, explicit widths/ranks and40-candidate
  equal budget, no target-trajectory fitting/time warping, and charging any
  target-specific selection/reference work to the deployed method. I also
  clarified empirical wide-reference resolution is not a new general-d width
  theorem. Final coordinator completeness query led us both to fix one epsilon
  pair before test and require the same six cases at both epsilons, with no25%
  runtime regression on any of eight cases at either. **Disposition:** closed;
  passing N earns highly significant scoped output-trajectory simulation.
- **M02 (theory milestone loopholes).** I proposed nondegenerate two-arc T40
  family, risk<=1/4 and two-layer normalized Gram motion>=.01, followed by
  explicit usable total-error control. The critic accepted the scope and grades
  but required joint parameter uniformity, genuine target comparison, full
  numerical-axis accounting, finite-bit cost and no precomputation amortization.
  **Response:** accepted; I additionally required certified interval parameter
  input to avoid hidden exact-real oracles. **Disposition:** closed. T1 earns
  highly significant constructive DL theory; T2 earns breakthrough within
  rigorous error-controlled nonlinear deep-Gaussian-GF simulation and highly
  significant across DL theory. Failure of T2 does not erase a valid T1.
- **M03 (generalization branch).** I proposed an exact rotated odd-three-parity
  family, near-linear-polylog sample budget, polynomial unchanged GF and an NTK
  risk gap, rather than a generic promise of explanatory progress. The critic
  accepted and required explicit constants, identification, common-event
  probability, fair training-selected NTK parameters and separately measured
  predicted/reference/teacher subspaces. **Response:** accepted, including
  the100-trial/withheld-dimension mechanism checks. **Disposition:** closed;
  valid novel theoretical subpackage earns a deep-feature-learning/generalization
  theory breakthrough; full package adds checked predictive mechanism content.
- **M04 (feasibility).** Claim challenged by the final completeness check:
  G could be read as a near-term extension. Both agents independently inspected
  Damian–Lee–Bruna's Generative Leap §3 Theorem1 and §5.1 Proposition4, and
  Barzilai–Shamir's SGD Limitations §2/§5.3.2 Theorem6. The related Gaussian
  parity low-degree barrier near d^(3/2) is serious adverse feasibility evidence.
  Fresh-sample SGD/correlation-loss/smooth-target and low-degree assumptions
  are not automatically the present spherical reused-sample squared-loss GF.
  **Response:** G is explicitly high-risk, barrier-facing, with no demonstrated
  feasible polynomial schedule or near-term promise. Applicable obstructions
  must be reconciled; failure is live. No transfer proof was attempted.
  **Disposition:** closed. No agreed current grade or pass threshold was changed.

The last two barrier sources were accessed directly at
https://arxiv.org/html/2506.05500 and https://arxiv.org/html/2602.05704v2 .
The new DMFT sources were accessed directly at
https://arxiv.org/html/2502.07998v2 and https://arxiv.org/html/2604.06309v1 .
Relevant model, algorithm and theorem-statement passages were read; full proof
appendices and whole experimental records were not audited.

### Process boundary and final endorsement

I did not request, receive or use earlier debate/agent scientific summaries.
The critic disclosed that a late status-only agent-list call unexpectedly
returned completed prior-agent summaries, after our independent openings and
substantive shared commitments were settled. Root disclosed an analogous
incidental exposure. No content from those summaries was sent to me or used in
this negotiation. The final agreement explicitly records this process limit;
this assessment is not represented as a blind promotion review.

I independently read the complete final agreement, including its later explicit
N quantifiers and G barriers, and endorse **every substantive statement, the
single common current-grade table, all four conditional grade commitments,
all uncertainty and failure rules, and the process/source limitations** in
`NOVELTY_AGREEMENT.md` with SHA256:

`05d863109fcceeae46ea4a607826213b53b0eb925e6cb719085717d7a080d910`

No substantive disagreement remains on that document. I do not retain a hidden
higher present grade. My frozen maximalist opening remains preserved, with its
original hash verified after appending this record. This is a scientific
assessment contract, not a new theorem, external replication, promotion or
promise that the milestones will succeed.

### Final normalization correction and superseding endorsement

**M05:** Root's final completeness check identified that G's sphere variable
could mean either physical x or normalized u, giving different initial scales.
The critic and I agreed the intended target is normalized u on the unit sphere,
physical x=sqrt(d)u, and hence canonical first preactivation Wx/sqrt(d)=Wu with
variance one. G now explicitly fixes that convention, its teacher, its ambient
input gradients and its Gram marginal mu_U. This resolves a real ambiguity;
it changes none of the negotiated grades or numerical thresholds. **Disposition:**
closed. The previous hash endorsement is historical and superseded.

After reading the correction in the full G context and retaining my complete
reading of the unchanged document, I independently endorse the complete final
`NOVELTY_AGREEMENT.md` with SHA256:

`80ef6589ecaf79de096e5391e489a9f6ecc3a88f2658437a19a0f144f2fd5358`

This supersedes my endorsement of `05d863...`. I endorse every current judgment,
conditional upgrade, pass/fail/inconclusive rule, evidence limitation and process
disclosure in this exact final version. No substantive disagreement remains.
