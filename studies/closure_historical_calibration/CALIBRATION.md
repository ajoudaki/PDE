# Historical calibration, frozen before target access

Status: final proposed freeze version; joint approval is recorded against an external hash manifest after the four-file audit. No target scientific evidence or previous target assessments have been read by either historical agent. This file is the joint synthesis; the advocate owns edits and preserves the critic's differences.

## Scope, evidence and selection

The unit is a scientific contribution at publication, not an author, venue, citation count, paper length or modern reputation. Twenty-five contributions cover neural approximation/expressivity, random features, GP/kernel limits, optimization/implicit bias, mean-field and feature-learning theory, and one adjacent model-reduction case. We selected mechanisms and contrasting kinds of advance, not desired grade frequencies. H02, H07, H10, H13, H21 and especially H25 test refinement-versus-new-capability boundaries. H08 and H15 combine contemporary closely related contributions, while preserving each paper's separate hypotheses. Revised versions of one contribution do not count twice.

This is a purposive calibration set, with substantial concentration in 2016–2022 wide-network theory. It is not a representative sample of all mathematical, computational or deep-learning research. Statistical generalization, PAC-Bayes theory and modern architectures receive sparse coverage. It omits many deserving advances and cannot assign percentile ranks. H24 calibrates a methodological analogy; a fluid-dynamics judgment is not automatically a deep-learning-theory judgment.

Both agents inspected primary statements/setup and decisive discussion for every case and exchanged individual challenges and responses using the stable IDs below. Division of lead collection did not substitute for independent inspection. Neither undertook a full proof re-audit or new experiment. Sources, section-level reading coverage, predecessor comparisons, strongest positive and critical arguments, responses, uncertainties and later-impact evidence are in [the advocate's 25-case record](HISTORICAL_ADVOCATE.md) and [the critic's independent record](HISTORICAL_CRITIC.md). They are integral to this calibration. The [critic's audit](CALIBRATION_AUDIT.md) checks the synthesis and freeze boundary.

Primary sources support what was established. Follow-on research and substantive historical exposition support later influence. A bibliography entry alone is insufficient. When independent influence was not established in the reading, the case says so. That means uncertainty, not absence of influence. In particular, a new contribution will not be penalized for lacking decades of subsequent adoption.

## Rubric derived from the comparisons

The defensible publication-time scale has four bands, not five subtly differentiated superlatives:

| Band | Meaning, assessed relative to predecessors and intended scientific audience |
|---|---|
| Below significant | A bounded useful correction/refinement whose effect falls below a meaningful field-level advance for that audience. This is compatible with correct, publishable or practically useful work. |
| Significant (S) | Resolves a meaningful scoped question or adds a useful capability, with a clear difference from prior work. |
| Highly significant (H) | Supplies a substantial theorem, mechanism or capability that changes several nearby questions or provides unusually strong resolution of an important scoped obstacle. |
| Breakthrough / groundbreaking (B) | Removes a recognized important obstruction, establishes a consequential new viewpoint with usable scientific content, or opens a reusable framework that materially changes what can be analyzed or done. These two words are merged because this sample supports no stable ordinal distinction between them. |

**Landmark is a separate retrospective qualifier**, requiring demonstrated sustained influence or field organization. It is not a stricter publication-time theorem checklist and is not forecast by requiring every new paper to have historical uptake. H01 and H09 provide strong landmark anchors; H03 supports an approximation-specialist landmark; H06 and H24 support plausible specialist/computational landmark qualifications with more uncertainty. These historical judgments concern their scoped contributions, not claims to have explained all deep learning.

Apply the bands through five questions, without an additive numerical score:

1. What exact obstacle or missing capability was present in the closest predecessors, and what is now possible?
2. How much scientifically relevant territory does the surviving result cover, including the importance of the structured class?
3. Does the mechanism or method transfer to nearby questions, or is it a selected isolated witness? Either can be valuable, but their kinds of value differ.
4. Which limitations merely define the question, and which remove a necessary bridge in the contribution actually claimed?
5. How strong is the evidence for the scoped claim, separately from how significant that claim would be if established?

Report two audience judgments: **specialist significance** and **broader deep-learning-theory significance**. A specialist breakthrough can be highly significant, significant or only adjacent in the broader field. H24 makes that distinction explicit. Ranges are genuine judgment uncertainty, not numerical error bars.

## Twenty-five historical anchors

The concise rows below point to complete case discussions. S, H and B have the definitions above; '<S' means below significant for the specified audience. Publication-time bands are distinct from the final column's later evidence. No cell asserts that a restricted theorem solves a broader practical problem.

| ID and contribution | Surviving capability and decisive limitation | Specialist / broad at publication | Subsequent influence, assessed separately |
|---|---|---|---|
| [H01 Cybenko 1989](HISTORICAL_ADVOCATE.md#H01) | One-hidden-layer density; no width/rate/training guarantee, shared contemporary credit | B / B | Foundational theorem in independent modern exposition; landmark defensible |
| [H02 Hornik 1991](HISTORICAL_ADVOCATE.md#H02) | Wider activation/measure/derivative approximation classes; extends an existing program | H / S–H | Leshno et al. explicitly extend its theorem; scoped influence |
| [H03 Barron 1993](HISTORICAL_ADVOCATE.md#H03) | Quantitative approximation on a Fourier class; norm may hide dimensional cost, search not solved | B / H–B | Barron-space extensions and substantive survey treatment; specialist landmark |
| [H04 Telgarsky 2016](HISTORICAL_ADVOCATE.md#H04) | Constructive depth-efficiency obstruction; selected oscillatory targets, no learnability | H–B / H | Independent work addresses resulting optimization/expressivity gap |
| [H05 Eldan–Shamir 2016](HISTORICAL_ADVOCATE.md#H05) | Polynomial-versus-exponential fixed-depth separation; constructed distribution/target | B / H | Reproduced as central depth example; later optimization separations |
| [H06 Rahimi–Recht 2007](HISTORICAL_ADVOCATE.md#H06) | Scalable explicit kernel features; fixed kernel, approximation not all statistical guarantees | B / H–B | Substantive error/statistical extension program; computational landmark plausible |
| [H07 Williams 1997](HISTORICAL_ADVOCATE.md#H07) | Analytic infinite-network covariance/inference; selected units, fixed hyperparameters | H / S–H | Deep-GP papers build directly on shallow computational correspondence |
| [H08 Deep GP, 2018](HISTORICAL_ADVOCATE.md#H08) | Deep prior limits and computation; Lee/Matthews conditions distinct, not trained features | H / H | General architecture limits and training-kernel distinctions build on it |
| [H09 Jacot et al. 2018](HISTORICAL_ADVOCATE.md#H09) | Limiting function-space training kernel; specified scaling, smoothness and horizon | B / B | Independent developments reorganize wide-network analysis; landmark |
| [H10 Lee et al. 2019](HISTORICAL_ADVOCATE.md#H10) | Quantitative simultaneous-width/all-time linearization under conditioning | H / H | Higher-order kernel dynamics sharpen/use the result |
| [H11 Chizat et al. 2019](HISTORICAL_ADVOCATE.md#H11) | General scaling explanation of laziness; stronger all-time hypotheses, selected experiments | H–B / H | Later parameterization/feature-learning frameworks use the distinction |
| [H12 Mei et al. 2018](HISTORICAL_ADVOCATE.md#H12) | Feature-moving probability-law dynamics; shallow/smooth, finite-time bounds | B / H–B | Structured learnability develops mean-field dynamics; shared wave credit |
| [H13 Rotskoff–Vanden-Eijnden 2018](HISTORICAL_ADVOCATE.md#H13) | Particle/fluctuation and error-suppression program; population/online sampling, long-time hypotheses/rate-source uncertainty | H / S–H | Contemporary mean-field contribution; specific rate influence not established here |
| [H14 Chizat–Bach 2018](HISTORICAL_ADVOCATE.md#H14) | Homogeneity/topological escape mechanism; W2 convergence assumed | H–B / H | Specific independent impact not fully traced; no landmark claim |
| [H15 Deep GD convergence wave, 2019](HISTORICAL_ADVOCATE.md#H15) | Overparameterized deep optimization guarantees; large widths/nondegeneracy, distinct papers | B / H–B | Quantitative near-initialization optimization program developed further |
| [H16 Soudry et al. 2018](HISTORICAL_ADVOCATE.md#H16) | Algorithm-selected max-margin direction; separable linear/exponential-tail setting | B / H–B | Independent margin extensions and survey framework; durable influence |
| [H17 Gunasekar et al. 2017](HISTORICAL_ADVOCATE.md#H17) | Parameterization/initialization-induced bias; commuting theorem versus false wider conjecture | H / S–H | Independent rank-dynamics correction shows influence while revising explanation |
| [H18 Saxe et al. 2014](HISTORICAL_ADVOCATE.md#H18) | Exact nonlinear training trajectories in a structured linear network | H–B / H | Later structured dynamics; independent lineage only partly traced here |
| [H19 Yang 2019 TP I](HISTORICAL_ADVOCATE.md#H19) | Reusable cross-architecture GP calculus; admissible finite programs at initialization | H–B / H | Framework used beyond original authors; later installments not backdated |
| [H20 Yang–Hu 2021](HISTORICAL_ADVOCATE.md#H20) | Deep feature-learning limits and parameterization dichotomy; restricted abc/activation class | B / H–B | Independent DMFT recovers and develops the process |
| [H21 Huang–Yau 2020](HISTORICAL_ADVOCATE.md#H21) | Quantitative tangent-hierarchy truncations; order/time/width/data conditions | H / S–H | Independent survey develops hierarchy as a beyond-linear approach; scoped uptake |
| [H22 Abbe et al. 2022](HISTORICAL_ADVOCATE.md#H22) | Structural SGD learnability and kernel separation; fixed sparsity, genericity/activation costs | H–B / H | Later independent influence not sufficiently traced; publication merit stands separately |
| [H23 Bordelon–Pehlevan 2022](HISTORICAL_ADVOCATE.md#H23) | Self-consistent nonlinear kernel dynamics and computation; formal analysis/history cost | H / S–H | No substantiated broad historical-impact claim in this reading |
| [H24 Schmid 2010 DMD](HISTORICAL_ADVOCATE.md#H24) | Temporal modes from snapshots; local linear-map assumption, no general extrapolation certificate | B / S (adjacent) | Independent analysis/extensions/application evidence; specialist landmark plausible |
| [H25 Sutherland–Schneider 2015](HISTORICAL_ADVOCATE.md#H25) | Useful estimator/error corrections; fixed kernel and narrower advance | S / <S–S | Independent optimal-rate work compares and improves these guarantees |

## Neighboring-band comparisons and boundary audit

**Below S to S.** H25 may be below broad-field significance while significant for random-feature specialists because estimator choice and prediction-error validity matter to that local question. A correct isolated constant improvement without such consequence could fall below S even locally. This is a calibrated possibility, not a quota requiring a negative case.

**S to H.** Compare H25's local estimator/error improvement (specialist S) with H02's expanded family of activation, input-measure and derivative-approximation results (specialist H). Compare H13/H21's valuable fluctuation or correction capability with H10's broader characterization of the entire linearized training/prediction process. The comparison depends on the actual consequence, not whether a theorem contains a rate.

**H to B.** H10 supplies strong quantitative refinement of a regime; H09 identifies the governing training object and makes a new analysis framework possible. H02 extends an approximation program; H03 changes what quantitative approximation can be shown on a nontrivial class. H21 is more than an identity because it controls truncation, but H20's constructive deep feature-limit/classification changes which infinite-width behaviors are available. A major theorem in a structured class can cross this boundary even when it has no practical benchmark.

**B versus groundbreaking.** We found no defensible repeatable separation between these words. They are one band. Splitting them merely to use all proposed labels would create false precision.

**Historical landmark.** This is a different axis. H01/H09 have clearly nonempty upper historical anchors; H03 offers a specialist one. A new result cannot yet have observed decades of influence. It may still be compared to the publication-time content of a later landmark.

**Spacing and occupancy.** The upper publication band is populated by major cases rather than rendered unreachable by an all-time/rate/application checklist. The middle is populated by clear refinements and substantial narrower results, especially H02/H07/H10/H13/H21. H25 establishes a credible lower boundary. The sample was not adjusted to make every label equally common. Overlap between adjacent bands reflects uncertainty; merging B/groundbreaking removes the most artificial gap.

## Equal scrutiny and claim-specific limitations

Historical and target work must receive the same level of scrutiny. Reconstruct material assumptions even where a paper's abstract does not emphasize them. Do not count limitations, compare paragraph lengths, or reward incomplete disclosure. Judge their consequences for the central contribution and its claimed scope. Separate (a) significance of an established/scoped result, (b) evidence confidence, and (c) historical influence.

Concrete rules supported by cases:

- **Qualitative guarantees can be major.** H01 resolves a representability question without rates. H19's reusable limit calculus need not provide finite-width complexity to be valuable. A qualitative assertion that merely restates an already known existence result would have a different novelty assessment.
- **Missing rates matter when the claimed capability needs them.** H07 permits exact limiting-model inference without finite-width rates. H21's actual advance is controlled truncation, so replacing its estimates by an unclosed hierarchy would remove a necessary capability. H13's exact long-time rate is not verified cleanly in the inspected conference display; this affects confidence in that rate, not proof of failure of the particle method.
- **Restrictive assumptions can preserve a breakthrough.** H03's function class, H16's linear separable model and H18's structured trajectories isolate substantial mechanisms. They block generic conclusions but do not automatically make the result incremental.
- **Some conditions narrow the central claim.** H14's assumed convergence prevents an unconditional optimizer-convergence interpretation. H17's unproved and later-falsified general conjecture cannot receive theorem credit. H20's activation and parameterization restrictions prevent a universal classification slogan.
- **Horizon requirements are claim-specific.** H09/H12 compact-time limits establish limiting dynamics; all-time validity is stronger. H10 actually proves stronger uniform-time control under additional hypotheses. The existence of an all-time result elsewhere does not make every compact-time theorem insignificant.
- **Compute requirements follow the intended use.** H24's operational analysis of measured data is valuable without a general nonlinear closure certificate. H23's history-dependent stochastic-process computation is informative even though it is not a bounded-state autonomous solver. An efficiency or finite-memory claim would require additional evidence.
- **Benchmarks are not a universal gate.** H04/H05 answer representation questions. H06's scalable-computation claim appropriately includes computational evidence. H22's learnability claim needs an algorithmic/statistical bridge that mere expressivity would not supply.

There was no automatic grade revision following the user's equal-scrutiny clarification. It sharpened the already-used distinction between scoped limitations and central missing bridges. H13/H14/H17 are explicit checks that the distinction is applied to historical papers, including papers with ambitious titles.

## Residual differences and evidence limits

The agents agree on the factual scoped comparisons, not on a forced single ranking. The critic centers H06's broad significance at H; the advocate allows H–B because the computational access changed what large-scale kernel learning could do. The critic centers H18's specialist significance at H; the advocate retains an H–B boundary for exact dynamical mechanism. Both center H23 at H specialist; the advocate allows a speculative B boundary for computational unification, while the critic considers recovery of the earlier Yang–Hu process decisive against that stronger novelty reading. The table uses the shared H center for H23. Other H–B ranges reflect genuine audience/breadth judgments.

Primary inspection is substantial but bounded: theorem/setup/decisive discussion, not full proofs. H13 contains a specific unresolved source-normalization issue; H02/H03 required extracted/OCR primary text after access problems. Long supplements were sampled only for relevant statements. Some later-impact searches remain incomplete. These limits are visible in each case and prohibit categorical claims of exhaustive literature priority, universal correctness or nonexistent influence.

## Freeze protocol

The four required artifacts are CALIBRATION.md, HISTORICAL_ADVOCATE.md, HISTORICAL_CRITIC.md and CALIBRATION_AUDIT.md. Every case must appear in both agents' inspected/debated coverage. The advocate proposes a final byte-identical version after factual corrections; the critic audits it against the critic's independent record. Both approve an exact external SHA-256 manifest of the same four files, including these residual disagreements. A self-referential embedded file hash is not used. The supervisor then saves an immutable snapshot before releasing any Phase 2 target evidence. Neither agent independently fetches or infers the target.
