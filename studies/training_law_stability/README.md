# Training-law stability and the input-population limit

Status: research resolved at its stated local-time scope. Frozen R1 passed
two complete isolated scientific reviews. The corrected canonical proposal
P2 passed two fresh complete scientific reviews and an independent integration
review, with no required corrections remaining. Promotion is ready for user
approval; no established material has changed.

The target is quantitative stability of the entire learned predictor with respect
to every probability law on `sqrt(2) S^1 x [-Y,Y]`, for two width-n tanh hidden
layers, no biases, canonical forward normalization, independent Gaussian stored
weights of variances `(1,1/n,1/n^2)`, all-block mobilities `(n,1,n)`, mean squared
loss, physical time, and simultaneous preceding-state raw GD. The initial finite
random readout is retained. No separation or Gram inverse assumption is allowed.

The requested law modulus is `C q exp(C sqrt(log(e/q)))`, `0<q<=1`, for the
joint cost `|x-x'|/sqrt(2)+|y-y'|`. The intended consequences are replacement
stability, the precisely ordered expected generalization-gap bound, joint
sample/width/step consistency without relative growth restrictions, and an open
family with positive finite-time RMS motion of both hidden representations.
The limiting state must retain full first-row fields and the initialized
Gaussian middle action and its adjoint; predictor compactness alone is inadequate.

## Scope and current proof routes

| Component | Owner | Mechanism | Current status |
|---|---|---|---|
| Transport comparison | `/root/transport` | Coupled observations, full first-row distance, individual reference tails | Accepted research: [TRANSPORT.md](TRANSPORT.md) |
| Strong population construction | `/root/population` | Common Gaussian generated spaces; state completion of finite laws | Accepted research: [POPULATION.md](POPULATION.md) |
| Nonlazy open family | `/root/nonlazy` | Actual-flow expansion, positive adjunction, state continuity | Accepted research: [NONLAZY.md](NONLAZY.md) |
| Joint finite algorithm limit, statistical argument, synthesis | `/root` | Fixed finite oracle proxy and ordered limits; ghost replacement | Accepted research: [ALGORITHM_AND_STATISTICS.md](ALGORITHM_AND_STATISTICS.md), [THEOREM.md](THEOREM.md) |

All contributors edit only their assigned flat study files. The coordinator is
the only Git writer and README editor. Scratch and generated evidence belong to
`data/generated/training_law_stability/<run>/`. No experiments are authorized or
planned; only necessary deterministic verification. No maintained API is used.

Startup HEAD: `839c101a70c47019a6a5df6190027fe8fbfcf26b`. The index was empty;
unrelated working changes in repository maintenance and book export were present
and are preserved. Unreadable inherited maintenance-review files were observed
as metadata only and are outside this study's proof dependencies. No exact prior
study was found. Sources: current `docs/global_nonlinear.md` C.1–C.3 and full
Gaussian/common-space dependencies, `docs/special_data_limits.md` III.F, and
`docs/finite_dynamics.md` §§1–4, with the notation and research workflow.

## Verification and completion contract

Each new implication requires a complete persisted proof. Present conjectures
remain open until checked; fixed-data convergence is not growing-data convergence.
Reference-tail propagation, full-state construction, limit ordering, and genuine
representation motion are separate obligations. Two fresh complete isolated
adversarial reviews of frozen proofs and necessary dependencies are required;
original reports, assignments and hashes will remain here. Required corrections
trigger a corrected frozen packet and two fresh complete reviews.

After scientific resolution, a distinct independent selector will assess current
coverage and placement. A concrete self-contained proposed addition, paired
scientific reviews, standalone validation and independent integration review
must precede the user's promotion approval. Established book/code files are not
within current write scope. No fitting, risk improvement, superiority, global
time control or quantitative finite-width rate is part of the target.

## Candidate and actual checks

The complete frozen input is [R1_PROOF.md](R1_PROOF.md), with complete
[dependencies](R1_DEPENDENCIES.md), [hashes and source ranges](R1_MANIFEST.json),
and the [neutral assignment](R1_ASSIGNMENT.md). The coordinator reconstructed
all component arguments and read the complete invoked dependencies; the
nonlazy author additionally read the whole algorithm/statistics component and
checked the ghost exchange and paired displacement bridge. These are author
checks, not independent reviews. No formal proof assistant or numerical
experiment was used. The reference nonlazy positivity proof was simplified to
an averaged adjunction identity; no fresh-forward conditioning claim from C.3
is required. The population proof directly constructs full-row Euler limits;
C.1's projection-only state is not used as a substitute.

The frozen packet is reproducible by concatenating THEOREM, TRANSPORT,
POPULATION, ALGORITHM_AND_STATISTICS and NONLAZY in that order, plus the
verbatim line ranges recorded in its manifest. The frozen source contents,
whole-file dependency hashes and all scientific input hashes are retained.
Generated/scratch reviewer outputs belong in the separately assigned run
directories; complete original reports belong in this flat study.

## Resolved statements and independent evidence

The exact statements are [THEOREM.md](THEOREM.md), frozen in R1. They prove
the requested `C q exp(C sqrt(log(e/q)))` law modulus for full state and
whole-circle predictions; `C/m exp(C sqrt(log(em)))` sample replacement and
`sup_t |E_S gap_t|`; the arbitrary simultaneous sample/width/GD-step limit;
both corresponding loss/risk limits; and a relative open W1 neighborhood of
the explicit two-input reference with positive finite-time activation RMS
displacement in both hidden layers. All support degeneracies remain admitted
in the stability and limit theorem. Constants depend only on Y and the fixed
model, except the reference activity time/neighborhood/margins.

Original complete reports: [review A](R1_REVIEW_A.md) and
[review B](R1_REVIEW_B.md), by fresh isolated nonauthors
`/root/research_review_a` and `/root/research_review_b`. Each reports reading
all 1,841 proof and 1,310 dependency lines and verifying the frozen hashes;
each accepts with no required correction. The coordinator read both reports
completely and verified their input/provenance correspondence. Review B also
performed a small exact Wick-pairing consistency check, not a training
experiment or finite-width rate validation. There are no adverse review
findings or superseded proof claims to conceal. No formal proof assistant was
used; acceptance is based on complete mathematical reconstruction.

## Concrete promotion preparation

The independent [relevance decision](RELEVANCE.md), by nonauthor
`/root/selector`, accepts the exact research scope for assembly as C.4 after
C.3. This preserves the existing D–J fragment assignments. The canonical
addition consolidates the repeated state/ball, multiplier, modulus and
displacement proofs. It does not supersede C.1–C.3's broader fixed-data results.

The current frozen proposed edition is [P2_ADDITION.md](P2_ADDITION.md), with
[five chapter scope edits](P2_GLOBAL_EDITS.json), the complete
[proposed guide](P2_DOCS_README.md), [assembled chapter](P2_GLOBAL_EDITION.md),
[complete dependencies](P2_DEPENDENCIES.md), and [input hashes](P2_MANIFEST.json).
The two destinations are `docs/global_nonlinear.md` and `docs/README.md`.
No code API or notation-guide change is proposed.

[Standalone validation](P2_VALIDATION.md) passed in
`data/generated/training_law_stability/promotion_validation_02/` using only
frozen inputs and the standalone validator. It checks exact assembly and
preservation, newly added links, mathematical environments and equation
references. This is proof-only validation, with no training or unrelated
exporter check. The complete original research-review evidence remains tied
to R1, independently of the canonical consolidation.

P1 received two fresh complete scientific acceptances, with original reports
[A](P1_REVIEW_A.md) and [B](P1_REVIEW_B.md). Its original independent
[integration report](P1_INTEGRATION_REVIEW.md) **did not accept the exact
edition**, requiring canonical activation-derivative notation and an explicitly
typed population norm/finite state distance. It found no substantive
mathematical gap. The coordinator read all three reports completely. The
entire original P1 packet and reports remain unchanged; P1 is superseded for
promotion, not retroactively relabeled accepted.

P2 corrects both required notation issues and also removes the unnecessary
nondecreasing-modulus alternative, identifies the observation-law diameter
explicitly, and repairs a local section pointer. No theorem, assumption,
constant, limit order or conclusion is changed. Before review dispatch,
author diff inspection caught and corrected a replacement-script residual
subscript typo; the intermediate validator output and correction note remain
in the P2 generated run. The final P2 packet was frozen only after that check.

P2 received two fresh complete scientific acceptances under the retained
[P2 scientific assignment](P2_SCIENTIFIC_ASSIGNMENT.md): original reports
[A](P2_REVIEW_A.md) and [B](P2_REVIEW_B.md), by `/root/p2_scientific_a` and
`/root/p2_scientific_b`. Both read all 1,423 new proof lines and 1,310
dependency lines, verified the exact hashes and found no required corrections
or missing mathematical inputs. The coordinator read both reports completely.

A separate fresh complete [integration review](P2_INTEGRATION_REVIEW.md)
accepted the exact P2 edition under the retained
[P2 integration assignment](P2_INTEGRATION_ASSIGNMENT.md). Because the
collaboration tool's reviewer-thread capacity was exhausted, it ran in a
fresh ephemeral reviewer process, instance
`01a08fe2-bba2-7d73-aae5-41c67ea02f31`, with no inherited conversation.
The neutral prompt, invocation, complete event transcript and outputs are
retained under `data/generated/training_law_stability/integration_review_p2/`.
The process completed with exit code zero. Its original report accurately
discloses the generic `/root` role label: that label is not the evidence of
independence. The coordinator launched a new ephemeral process, with neither
resume nor fork, supplied only the neutral review prompt, and verified the
distinct instance in the event transcript. The recorded file-access commands
show only assigned inputs, required skills and reviewer-owned scratch, with
no author history or prior reports. The reviewer attests the same isolation.
Its initial truncated dependency output was fully reread in smaller chunks.

The coordinator read the complete integration report and its independent
correspondence-check source, verified all input/provenance identities and
confirmed the exit-zero independent rerun. Both editions contain the same
six scientific artifacts byte for byte. All original P1/P2 reports remain
unaltered, including adverse and optional findings. Optional P2 presentation
suggestions are not changes to the accepted frozen edition.

There is no remaining required proof or integration correction within this
scope. All frozen proof hashes and the seven live dependency/destination
baselines were rechecked unchanged after review. Mathematical review is not
formal machine verification; deterministic checks establish assembly and
reproducibility, not a numerical learning-performance claim. Only the user's
approval remains before established book/code changes. The concrete
[promotion proposal](PROMOTION_PROPOSAL.md) identifies the exact two-file
edition and its limitations.
