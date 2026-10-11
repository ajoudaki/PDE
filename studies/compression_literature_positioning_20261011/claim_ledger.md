# Comparative claim ledger

Date: 11 October 2026. This supersedes the initial reconnaissance ledger. Source-level reports contain the full assumptions, counterexamples, repair attempts and exact locations. “Not established” is not “impossible.” The current manuscript is the comparison target, not independently re-proved by this literature audit.

## C1. Earlier work already proves the same general polylogarithmic dynamics-compression result

**Claim type:** potential novelty objection. **Assessment:** unsupported for the reviewed sources.

Universal compression theory is the closest advertised result. Its hypotheses concern fixed-dimensional permutation-symmetric objects and regularity of the composed trained observable. Its discussion leaves all-wide deep-network rates unresolved. It does not discharge width- and time-uniform regularity for our canonical dense reference.

The objection also cannot simply rely on the advertised proof. Theorem 3's width-uniform local bound has an explicit fixed-polynomial counterexample: for repeated points at three positions on a line, the determinant of the summed three-dimensional feature outer products grows cubically in object count, whereas every weighted two-point representation has determinant zero. The claimed linear-in-count bound fails. This invalidates a step used downstream, **not** the final polylogarithmic support rate itself: three support points solve that example exactly. Growing approximation order also requires uniform derivative/analytic estimates not supplied by a fixed-order Taylor argument. Theorem 8 uses a false small-sublevel-set lemma and a false inference from cell volume to empirical occupancy.

DLRT is a different legitimate conditional theorem: it assumes small normal-to-rank-manifold gradient components near the dense path. Deriving that property for our Gaussian all-wide model is not a formality. The cited integrator constants depend on the training horizon; a counterexample in the stated abstract smooth-gradient class rules out silently making the comparison time-uniform. This does not disprove the finite-time integrator theory.

**Conclusion plausibility versus proof:** analytic moment reduction and robust low-rank dynamics are plausible, nontrivial ideas. The universal local bound is clearly false as written; downstream rate proofs are not certified. DLRT's finite-horizon conditional mechanism survives. Neither yields our conjunction of model, retained state, query domain, horizon and reference coupling. See [universal fresh check](UNIVERSAL_FRESH_CHECK.md) and [DLRT audit](AUDIT_DLRT.md).

## C2. NTH is the only earlier finite closed description, and it necessarily stores more than the dense network

**Claim type:** proposed positioning assertion. **Assessment:** false as a general statement.

Huang–Yau, Dyer–Gur-Ari and the effective-theory book all exhibit initialized finite-order closed evolution. Their states genuinely use same-realization quantities. At fixed sample set and order the scalar tensor count is independent of width. Dyer's leading correction retains output, kernel and a third-order tensor, plus a fixed fourth-order tensor. The book has a related, not identical, derivative-contraction hierarchy and explicitly derives trajectory and fitted-predictor formulas.

Their default fixed-depth scaling has representation-learning corrections shrinking with width. A formal initialized correction is not a proved complete-trajectory emulator in a persistent-feature-learning scaling. Dyer expressly assumes series/limit interchange for general nonlinear time evolution; the general diagram rule is partly conjectural. The book's ordinary pathwise remainder cannot be inferred from ensemble power counting: an allowed random-feature example has a nondegenerate omitted term of order n^(-3/2), not its displayed n^(-2) reading. Local endpoint signs are also wrong but readily repairable.

Huang–Yau's invalid differentiation of a max-norm inequality has a short **integral bootstrap repair** preserving the width exponent, independently checked in this audit. That particular issue must not be inflated into a broken theorem. Its probability convention still overstates the tail for polylog-bounded Gaussian coordinates.

Our own n^(Theta(log m)) hierarchy benchmark concerns a specified deep-linear, zero-readout, feature-learning-scaled hard family and literal ordered arrays. It is not a lower bound for the original Huang–Yau parameterization or every possible compressed encoding.

**Novelty consequence:** do not claim first finite closed dynamics, first same-seed correction, or universal failure of NTH. Claim the full stronger compression contract. See [Huang–Yau and repair](HIERARCHIES.md), [final Dyer audit](AUDIT_DYER_FINAL.md), [full book audit](AUDIT_EFFECTIVE_THEORY.md).

## C3. Existing limit and fluctuation theories already give a fully certified substitute for our finite-reference theorem

**Claim type:** potential novelty objection. **Assessment:** not established; several distinct reasons.

Tensor Programs IV gives genuine fixed-step feature-learning limits. DMFT gives substantive nonlinear response equations and useful empirical validation. The projected infinite-width model gives an explicit computable limit. None should be dismissed as “not dynamical” or “no feature learning.” The projected model deliberately changes initialization and optimization; it does not prove that unrestricted dense Gaussian dynamics are low rank. Its representation appends directions with training steps. General TP/DMFT evaluation keeps evolving laws or sample-time covariance/response history.

Nguyen–Pham gives a substantial rigorous finite-time mean-field framework in its own normalization and hypotheses. An arbitrary cross-layer coupling passage fails without product structure, but that does not erase its finite-horizon comparison machinery. Neural Hilbert Ladders has a reconstructible static sampling theorem; its training proof still needs uniform empirical/moment estimates and correction of displayed equations. Static approximation is not closed trajectory compression.

**Correction to the initial assessment:** Pham–Nguyen 2021 constructs a genuinely sampled-neuron-coupled correction, but its sharp O_T(n^(-1)) output remainder must be called a **claimed rate requiring proof repair**, not a rate verified by this audit. Its pair-sampling lemma is false and a later sensitivity invocation yields a weaker exponent than asserted. An additional in-scope counterexample refutes a uniform weight-response bound used in its long-time argument. The limiting stationary output-variance mechanism survives. Theorems about a width-first limiting variance are also not finite-width, all-time trajectory comparison theorems.

Other bounded findings: TP IV's smoothed-ReLU derivative limit used in one classification branch is false; this does not invalidate its separate fixed-step limit. The DMFT fluctuation action lacks the leading random-initial-output boundary term for the general stated initialization; an explicitly centered variant is different. Adaptive-kernel identities at a stationary homogeneous ridge point survive, but equilibrium existence, zero-temperature scaling, normalizability and a proposed deep solver require separate qualifications.

**Novelty consequence:** even granting repaired versions of their strongest advertised finite-horizon conclusions, finite retained coordinates, complete-trajectory control and our reference/query contract still require new work. Do not base novelty on claiming no one has studied fluctuations or coupled finite networks. See the AUDIT_TP4, AUDIT_DMFT, AUDIT_DMFT_FLUCTUATIONS, AUDIT_PI_LIMIT, AUDIT_NGUYEN_PHAM, AUDIT_FLUCTUATIONS, AUDIT_NHL and AUDIT_ADAPTIVE_KERNELS reports.

## C4. Small subspaces or empirical pruning establish the same small-state learning guarantee

**Claim type:** inference from algorithms and experiments. **Assessment:** invalid in general.

NTT directly studies transferring training trajectories, so “all earlier compression concerns snapshots” is false. Its exact theorem, however, uses a linear student and exact initial prediction/kernel matching. With a binary coordinate mask, the omitted kernel is a sum of positive-semidefinite outer products. Exact matching therefore permits pruning only coordinates identically zero across the training data. For generic nonzero coordinates, that exact antecedent supplies no nontrivial pruning. This is a restriction of the theorem, not a refutation of its nonlinear empirical results.

Intrinsic-dimension, tiny-subspace and DLDR experiments show useful concentration or successful constrained training. A reduced coordinate vector can still require a dense basis and dense gradients. DLDR's final appendix confirms substantial training-prefix setup; it does not supply a missing width-uniform trajectory theorem. Existence of a successful straight-line restricted path does not imply that the unconstrained gradient path is straight, even for a simple strictly convex quadratic. Armijo decrease alone also does not guarantee BFGS positive curvature.

Koopman/DMD and DEIM use training snapshots and retain dense weights, bases or operators; their measured savings do not imply polylogarithmic total retained state. NTK-SAP targets initialization trace/spectrum proxies; a trace is not a kernel, and even an identical spectrum is not identical label-conditioned dynamics. Its source itself acknowledges later divergence.

**Empirical status:** no experiments or code were reproduced. Credit task performance and acceleration as reported, without converting them into seed-coupled all-time fidelity. See [NTT/subspaces](AUDIT_NTT_AND_SUBSPACES.md), [DLDR](AUDIT_DLDR.md), [DEIM/DMD](AUDIT_DEIM_DMD.md), [NTK-SAP](AUDIT_NTK_SAP.md).

## C5. Our stated theorem represents a distinct and substantive conjunction

**Claim type:** positive positioning of the current manuscript. **Assessment:** supported relative to this reviewed corpus, conditional on the manuscript's own proofs; not a global priority certificate.

The distinctive claim is a **small dynamically sufficient state for a specified finite nonlinear learner**, not merely a limiting description or low-dimensional recording. The comparison uses the same whole-trajectory norm and a lower bound on actual independent dense-run discrepancy. The following qualifications are indispensable:

| Contract component | What the current manuscript states |
|---|---|
| Dense reference | Its specified Gaussian initialization, zero readout, layer mobilities and fixed-depth fully connected architecture |
| Regularity and stability | Strip-analytic activations with controlled derivatives, positive population feature-Gram gap, fixed nonzero small labels |
| Harmonic | Polylogarithmic **total retained real coordinates**, whole-sphere query guarantee, complete-trajectory error of order n^(-1) at fixed problem parameters |
| Taylor | Total order (log n)^3 at fixed problem parameters, **setup-declared finite panel**, passive labels unused, complete-trajectory error of order n^(-1) |
| Legendre | n^(5/4+o(1)) moving coordinates at fixed problem parameters; quadratic fixed mixers remain |
| Actual variability | Ratio of **two trajectory suprema** tends to zero in probability; denominator lower-bound witness is early, not an endpoint-only lower bound |
| Nonlinear feature learning | Local extra assumptions, early-time separation from affine input predictors and the reference's own frozen NTK; dense hidden motion is distinct from compressed predictor conclusions |
| Setup | Supplied explicit-reference and fresh implicit-reference costs differ; initialization provenance does not mean zero computation or no numerical rollout |
| Resource meaning | Real-coordinate count, not bits, practical wall time, minimality or automatic test-risk improvement |

The allowed label cap and positive separations need not shrink with width. They are not therefore meaningless, but can be small and geometry-dependent. A dense-to-population approximation transfers by the triangle inequality **if independently available in the same norm**; no new all-time population theorem is implied.

Structured feature-learning results likewise remain relevant: Nichani–Damian–Lee's staged theorem and Allen-Zhu–Li's progressively enabled quadratic DenseNet address learning a target, not emulating a prescribed dense trajectory. Backward correction keeps earlier enabled layers trainable; its full information-gap/accuracy qualifications and side-result issues are in [the complete audit](AUDIT_BACKWARD_CORRECTION.md). No broad claim that all earlier deep theory freezes layers is justified.

The two conceptual burdens are deriving compressible response geometry from dense training and proving stability after feeding the compressed responses back into learning. Neither symmetry, analyticity, low rank observed afterward, nor a finite list of kernels supplies both automatically.

## Severity triage

Identifiers below are scoped to the linked source reports, preserving their finer dependency analyses. No global fatal verdict or misconduct finding is assigned.

| Concern | Affected statement | Classification / surviving contribution |
|---|---|---|
| Universal local bound and optimality lemmas | Theorems 3 and 8; downstream proof steps | Verified false intermediate statements, major proof problems; ultimate polylog rate not disproved |
| DLRT horizon suppression | Time-independent interpretation of comparison constants | Major for all-time interpretation; finite-time conditional integrator survives |
| Dyer M2 | Universal Hessian bulk scale / first moment | Major, explicit counterexamples; exact hierarchy and linear counting survive |
| Dyer L3 | Discrete first-correction sums | Minor, explicit index repair; continuous coefficient unaffected |
| Effective theory M1 | Individual-realization remainder | Major for strong pathwise interpretation; weak/formal theory remains |
| Effective theory L1 / M2 | Endpoint signs / earlier-layer covariance suppression | Minor sign repair; major for extra depth suppression, not book-wide collapse |
| Huang–Yau Appendix B | Differential majorant | Minor after independently checked integral repair; earlier bounds still inputs |
| TP IV smooth-ReLU branch | Vanishing squared-second-derivative limit | Major for affected classification proof, not separate fixed-step limit |
| Mean-field 2021 M1 / M2 | Sharp coupling rate / long-time response bound | Major proof gaps; coupled construction and stationary output mechanism survive |
| Mean-field 2023 coupling passage | Unrestricted cross-layer coupling telescoping | Major within that comparison step; finite-time framework not thereby disproved |
| NHL training proof | Error initialization, algebraic differentiation, uniform empirical control | Major proof-certification gap; static approximation survives |
| DMFT fluctuation boundary | General randomly initialized output | Major model/derivation mismatch; centered special case and response mechanism distinct |
| Adaptive kernels | General deep solver / broad Bayesian saddle / temperature limit | Major scope/derivation qualifications; conditional ridge identities survive |
| NTT exact masking | Generic nontrivial sparsity under perfect matching | Restrictive antecedent, not a false conditional theorem |
| DLDR Armijo/BFGS | Positive curvature from decrease alone | False implication with standard repair; empirical results not refuted |

## Holistic judgment and wording rules

The prior literature is substantial. Its advertised strongest formulations should not be treated as proved without inspecting hypotheses and remainders. Conversely, isolated mistakes do not erase sound restricted results. Our strongest positioning does not need either distortion.

Use: **“A finite autonomous representation of nonlinear feature-learning trajectories, through convergence and below the reference network's actual whole-trajectory seed variability, with explicit retained-state bounds.”**

Avoid: “mean field is not a dynamical system”; “operators require dense matrices”; “no prior same-seed correction”; “NTH is the only finite closure”; “all earlier results only concern endpoints”; “every deep theory trains layerwise”; “we rule out every kernel”; “Taylor handles unrestricted new post-setup inputs”; “all our storage is polylogarithmic”; “we prove the ratio small separately at every time.”

The remaining scope guard is epistemic: the corpus is selected rather than exhaustive, the author's theorem was not re-proved here, and reading full papers is not the same as independently validating all their claims.
