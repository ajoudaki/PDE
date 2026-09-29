# Visionary scientific review of the current draft

## 1. Summary

The paper's strongest result is that **deep nonlinear feature learning can be reproduced by a closed dynamics of finite response memories, with a proved error on the whole parameter trajectory over any prescribed finite horizon**. Each learned hidden interaction is an integral pairing forward features with residual-weighted backward responses. The paper replaces those histories by online polynomial coordinates, reconstructs the network from them, and controls the resulting feedback. The fixed initialized matrices are retained. At fixed finite width and depth the error is O_T(P^{-1}); a second clock and weighted projection improve it to O_T(P^{-2}) under stronger smoothness.

This is a substantial conceptual contribution. The paper supplies a candidate set of dynamical coordinates for learning, not merely a compact representation of a trained function. Its population interpretation is promising but remains a conjecture. The central theorem does not need that conjecture to be interesting.

## 2. Main Contributions

The key mechanism is the pairing of two compressed histories. Orthogonality removes mixed retained/omitted terms, leaving an interaction defect that is a product of two projection errors. More importantly, the proof converts that identity into control of the *accumulated absolute velocity defect* and closes the self-consistent neural feedback loop. This is the step that makes the result about training dynamics.

The two clocks reveal a useful scientific distinction. The learning-speed clock supplies enough forward regularity for a first-order rate without requiring a smooth normalized backward history. The joint clock regularizes both histories and earns the second-order rate. The resulting low-rank increment is generated causally by the network's own responses; it is not a rank assumption imposed on the original flow.

The resource comparison is valuable when read as the paper defines it: the number of evolving coordinates at a prescribed accuracy, with fixed sources and numerical work reported separately. Keeping the entire initialization limits its computational benefit but does not erase the reduction in learned dynamical state.

## 3. Strengths

**The full finite-width argument is the scientific center.** I checked the main chain in Appendices A and B: dense energy control, the projection-energy identity, the product defect, the cancellation of the apparent order loss through depth, joint-clock total variation before the clock bound, and first-exit continuation. I found no central mathematical error in those arguments. They are appreciably stronger than fitting a polynomial to a known dense history after training.

**The relationship to prior machinery is largely well judged.** HiPPO supplies the online projection ingredient; it does not itself prove this feedback theorem. The NTH is also a real feature-learning description, and the manuscript correctly constructs a mobility-matched hierarchy instead of dismissing it as a frozen kernel. Its published accuracy estimate has different scaling and data hypotheses. DMFT removes explicit width through two-time response objects; the present fixed-width theorem compresses another resource. These are complementary scientific descriptions, and identifying a shared ingredient does not establish that an earlier method solved the present closure problem. Relevant source checks are documented in `evidence_log.md`.

**The controls address a meaningful question.** Matching the labels and matching rank do not determine the function selected by dense training. The five-task controls show that response memory stays substantially closer to that function than the specific frozen empirical kernel or Euclidean factor dynamics. The saved metrics reproduce, including all 29 resolved factor wins. This supports the importance of the response-derived evolution law. The common-time trajectory example adds separate evidence of tracking, and the text appropriately avoids treating endpoint agreement as a trajectory certificate.

**The most consequential limits are acknowledged.** The paper distinguishes moving from fixed state, admits no runtime improvement, states width/horizon dependence, marks ReLU as outside its smooth theorem, reports nonmonotone small-order behavior, and formulates the population closure as a conjecture. These are useful boundaries around an ambitious claim.

## 4. Weaknesses and Claim-Level Concerns

**M1 — The ancillary theorems are not established at the standard of the main two.** Appendix C, p. 27 (`main.tex:1721`), invokes an exponential tail bound for reference backward fields without proving or citing it. That estimate carries the Osgood argument; bounded operator norms on L² do not by themselves supply it. Appendix D, p. 28 (`main.tex:1776`), replaces the operator construction, trace-class estimate, word-statistic limit and Euler convergence proof with a summary paragraph. The scalar nonclosure result likewise needs a complete noncancellation/graph-independence argument. These are gaps in the supplied proofs, not demonstrated false conclusions. Supply the missing arguments or label those results as conditional/sketched. Their independence from Theorems 6.1–6.2 means they should not obscure the sound central contribution.

**L1/L6 — Notation currently makes the mechanism harder to follow than it is.** In Appendix A, equation (13) uses undefined H instead of L; equations (22), (31) and (32) use K where the established Lipschitz constant is Lambda_F. Define the parameter norm explicitly. More consequentially, Appendix A uses barred symbols for histories, while Appendix B writes a moment matrix and a history with the same barred h in one defining equation (`main.tex:1359`). Distinguish instantaneous responses, clock histories, raw moments and endpoint projections. Figure 2 plots normalized coefficients `c_k=(2k+1)\bar h_k/tau`, as its script confirms, rather than the raw moment integrals. A small notation table would resolve all four object types. A paired two-clock table should also show the different backward prefixes and the joint prefix subtraction, which is why its rank bound is m(P+1).

**L2 — Table 1 should carry its qualifications inside the table.** It presently places conditional population root-width rates, fixed-width parameter rates, published NTH rates and a numerical time-step order in one short error column. Appendix E is much more careful. Add target/status labels, mark the conditional cells, and describe the NTH row as width-suppressed corrections rather than a specific n^{-1/2} feature-learning correction; the cited source's Corollary 2.4 gives an O(n^{-1}) kernel-velocity estimate. This is a repair to the comparison's presentation, not an objection to making the comparison.

**L3/L4 — Explain the dramatic controls with numbers already in hand.** The frozen controls are legitimate for the declared same-initialization fitted-function target. However, “the stored readout is small” (§3, p. 5) hides a consequential experimental choice: the supplied code uses standard deviation 1/n. The initial kernel is almost wholly the readout block. On quadrant-alternating, the recorded frozen fit time is about 70.9 million, versus 244 for memory P=3. Put the readout law, block traces, fitting times and conditioning in a small supplementary table. This makes the large NTK outputs interpretable without weakening the positive memory result. State “MNIST 3 versus 8” at first mention in §7; it is currently explicit only in the figure caption. The shallow discrepancy reduction spans approximately 1.5–3.5 orders, rather than 1.5–3.

**L5 — Let the theorem earn the broader analogy.** The Turing-machine opening promises a canonical theory of learning before the reader knows the precise object proved. Lead with the obstacle—equal functions can have different futures—and the response-memory construction. Then use the idealized-model analogy to explain why these coordinates might matter. The manuscript need not retreat into a generic compression-method narrative. It should clearly identify the discovery it already supports before describing what a population theorem would add.

## 5. Questions for the Authors

These are prioritized revision requests rather than requests for a new experimental campaign:

1. Can Appendices C–D supply their missing supporting lemmas, or can the paper explicitly distinguish those sketches from its complete convergence proofs? This controls the assessment of those ancillary claims.
2. Can one compact definition table identify the instantaneous responses, history functions, raw moments, projected endpoint values, and prefixes for both clocks? This would substantially improve verifiability of the central mechanism.
3. Can Table 1 mark its target/error metric and conditional status in the rows, while keeping Appendix E's fuller derivations?
4. Can the existing control records be summarized with precise initialization and stopping-time information, and can the binary MNIST setting be named in the main text?
5. Can the introduction foreground the theorem and reserve the idealized-learning analogy for its interpretation? No additional result is needed to make that stronger story.

## 6. Reproducibility and Code

All supplied manifest hashes match. I read the four supplied Python files and independently recomputed the available saved circle, trajectory, binary-MNIST, sphere and control metrics. The 39-time discrepancies and coarse/fine sensitivity arrays agree with their definitions. For P=7, only six of the 38 positive shared times have discrepancies larger than the sensitivity scale, consistent with the paper's caution about tiny errors.

The deliberately paper-only packet does not include the closure engines, factor trainer or all sweep records referenced by its wrappers. I did not inspect outside paths or rerun training. This is a verification limit of this review, not a finding that the repository or eventual release lacks those resources. A distributable package should make replay dependencies explicit and distinguish saved-prediction rendering from training reproduction. Details are in `code_audit.md`.

## 7. Limitations and Ethical Considerations

The result is a finite-horizon, fixed-width theorem. It does not yet explain why very small orders work, establish width-uniform constants, compress sample dependence or the initialized operator, or improve total storage and runtime. The joint clock's stronger asymptotic rate need not win at low order. These are scientific scope limits already largely disclosed, not reasons to discount the proved closure.

No task-specific ethical issue was identified in the supplied mathematical and small benchmark material. This assessment is not an audit of unrelated data or deployments.

## 8. Overall Scientific Assessment

The central message stands: **the learned interactions of a deep nonlinear network admit an autonomous finite-order memory representation that tracks the full finite-width learning trajectory on compact horizons.** The scientific advance is the identification and controlled evolution of these response coordinates. Its strongest empirical companion is that the same small memory reproduces the dense-selected function while equally fitting rank-matched and frozen controls do not.

The ambitious interpretation is credible as a research direction: width and temporal memory may be separable sources of complexity, and paired neuron-level response memories may become useful state variables for a population theory of feature learning. The paper proves the temporal-compression half at fixed width. The population theorem is the clearly stated next step. Prioritize complete supporting proofs and a sharper notation/narrative hierarchy; the current evidence already supports a meaningful scientific contribution.

## 9. Confidence and Verification Coverage

High confidence in the stated fixed-width contract, the checked main proof architecture, the supplied-array arithmetic, and the interpretation of the tested controls. Moderate confidence in broad novelty because this was a focused three-source comparison, not an exhaustive literature review. Lower confidence in Appendices C–D as complete theorems and in original experimental replay because required proofs or engines are outside the supplied evidence. Entire manuscript and included appendices read; all 41 pages visually reviewed; no training, expensive experiments, or manuscript edits performed.
