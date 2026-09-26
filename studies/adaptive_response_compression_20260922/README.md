# Efficient hierarchies for nonlinear dense learning

New theory/design study, 2026-09-22, explicitly motivated by the user's request
to reconsider efficient compression beyond frozen derivative dictionaries.
This is a materially different direction from extending a particular frozen
dictionary. No experiment, training campaign, maintained-source edit, or
promotion is authorized or undertaken here.

## Question and scope

Find one or a few principled approximation hierarchies for the canonical
nonlinear dense population dynamics that have a plausible small-order
accuracy advantage and a credible convergence mechanism. Moving bases,
operator response representations, and density descriptions are admissible;
a list of named techniques without a closed model and its obligations is not.
The user wants conceptual depth and substantive mathematical support, not
an asserted theorem that has not been proved.

The model is the established two-hidden-layer tanh network with Gaussian
initial hidden weights and zero limiting readout, canonical parameter metric,
fixed-dimensional inputs, correlated finite data or a fixed input law, and
both trained hidden layers. The middle operator is W2(t)=W2(0)+K(t), with
the actual reused adjoint. A half squared population loss may be used with
the factor-two physical-time conversion stated. Desired observables include
whole-input predictions and the forward/backward actions needed to evolve
them, at least on a fixed nonlinear time interval. The approximation order
must reflect actual stored state/work, including Gaussian initialization
queries, changing subspaces and any field/distribution resolution.

Existence of a rank-p approximation of a known trajectory is distinct from
an autonomous causal compressed evolution. Dense initialized storage or an
exact action oracle must be counted; retaining either is not full dense-layer
compression. No freezing of feature learning, replacement of the adjoint by
independent randomness, post-training oracle basis, or label fitting alone
may substitute for the intended question.

Allowed scientific repository inputs are this new study and established docs/
and code/ only. Prior study artifacts and unpromoted prior-turn derivations
are not inputs. The user's qualitative dissatisfaction with earlier results
is motivation only; no earlier empirical table or unpromoted theorem is
imported. Relevant facts must be derived from the canonical equations here
or read in established sources. External primary literature may be checked.

## Work and ownership

Root owns this README and ASSESSMENT.md. Fresh-agent allocation was
unavailable. A reused agent was restricted to prompt-only arithmetic and
logical checks, excluding prior scientific inputs; those are not fresh
independent creative routes or promotion reviews. It owns
TRACE_BOUND_CHECK.md and ADAPTIVE_PRIMITIVES_CHECK.md. Required mathematical
and research skills and applicable references apply. The explicit source
scope replaces author startup. No agent writes maintained files, another
study, or the shared Git index.

At start HEAD was ab6dd76987007b925b4d9559a936234e224ef6e9 and the tracked
working tree/index were clean; unrelated untracked studies were preserved.
No compute budget is requested or consumed for experiments.

## Status

The requested theoretical assessment is complete in ASSESSMENT.md. The
recommended direction is adaptive response-space compression, combining
streaming compression of learned updates with a bidirectional Gaussian
initial-action cache. Exact elementary trace, rank-approximation, streaming,
and finite Gaussian-conditioning statements were internally checked.

Full nonlinear trajectory convergence, useful low-order accuracy, economical
query growth, and population-resolution cost remain open. The learned
increment's algebraic rank bound is not a convergence theorem for either
the earlier frozen dictionary or the proposed evolving solver. No numerical
experiment, GPU run, maintained-source edit, Git-index write, or promotion
was performed.

## Authorized empirical continuation: train the initialized p3 vectors

The user requested a test on the hardest previous circle task and explicitly
clarified that p3 means the exact derivative dictionary's p3 vectors as
initialization, now trainable. This authorizes the one-case experiment in
TRAINABLE_P3_PROTOCOL.md and narrowly permits that benchmark's derivative and
original-circle archives as empirical inputs. It supersedes the earlier
theory-only/no-archive restrictions for this test alone. The requested model
is factor-coordinate gradient flow, not the streaming/cache construction.

BENCHMARK_INPUT_CHECK.md identifies the task, exact saved initialization and
common dense reference. At n2048, frozen p3 circle RMS is1.1001187614 and
frozen p7 is0.7564240400. The p3 dimensions remain6 lower and12 upper vectors.
Making these trainable increases trained scalar count6216 ->43080, while
retaining the same working model storage. No dense residual or extra basis
normalization is introduced. Population L2 mobilities for the added vectors
are fixed before training, with no learning-rate search.

Root owns trainable_dictionary.py, run_trainable_p3.py, protocol, analysis and
results. The scoped benchmark checker owns BENCHMARK_INPUT_CHECK.md; the
implementation checker owns test_trainable_dictionary.py and
TRAINABLE_DICTIONARY_CHECK.md. Six CPU gradient/oracle/serialization tests
passed before training. Two numerical levels run concurrently on both GPUs;
one frozen-p3 reproduction and at most one gate-triggered refinement complete
the bounded600 summed GPU-worker-second protocol.

**Completed:** TRAINABLE_P3_RESULTS.md records finer RMS0.8964250064 versus
frozen p3's1.1001187614 (18.52% lower) and frozen p7's0.7564240400 (18.51%
higher). Both numerical levels agree; all models fit training MSE0.001.
The trainable p3 flow takes2581.882 time units versus241.985 for frozen p3.
This improves the same p3 representation but fails the requested p7
superiority test and does not establish efficiency of the separate adaptive
response/sketch hierarchy. No learning-rate or initialization search occurred.

All numerical gates pass. Endpoint refinement max0.0030338942 is below0.01,
so no extra is eligible. Frozen reproduction matches within9.46e-14 on the
circle. TRAINABLE_RESULTS_CHECK.md independently replays38 snapshots and3
endpoints with223 passing checks, max prediction discrepancy1.73e-14.
Root read complete scoped reports, reconciled metrics and inspected the figure.
Seven CPU gradient/serialization/runner tests also pass. These are internally
checked results, not established/promoted material.

Raw runs: data/generated/adaptive_response_compression_20260922/
trainable_p3_primary01,trainable_p3_refined01,frozen_p3_replay01.
Final metrics/loss-function plots: trainable_analysis02. Independent NumPy
audit: independent_trainable01. Exact commands and hashes are in each run's
config and the results report. The earlier trainable_analysis01 presentation
is preserved. No maintained source, old artifact or Git index was changed.

GPU-worker timers sum69.195830s. Charging the whole40s startup/check overhead
reserve conservatively gives109.195830s, leaving887.013736s of the inherited
allowance. All workers exited, with no outstanding reservation, eligible
extra or authorized tuning branch. This bounded request is complete.

The user's subsequent direction explicitly discontinues the unfrozen-factor
approach. Its completed experiment remains preserved; no tuning or additional
run is authorized. The materially different response-history question is
handled in a separate theory study and does not reopen this campaign.
