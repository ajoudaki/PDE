# Fast environments for response-memory learning

New study, 2026-10-02, under the user's explicit broad search for substantive
practical extensions of the current paper. This is a materially separate
architectural efficiency question from attention, recurrence and controlled
curricula; it has its own source and generated namespace. Root is sole author
at startup. No other study's results or code are inputs.

## Question and scope

Can a fast fixed operator preserve the forward/transpose reuse relevant to
feature learning when it replaces the paper's dense Gaussian initialization?
The learned part remains the manuscript's self-consistent paired Legendre
history, with exact sample indexing, residual clock, unit prefix, normalizations
and canonical outer-layer mobilities. The initialized operator is explicitly
CHANGED; the original Gaussian theorem does not automatically apply.

Primary sources: complete current `paper/main.tex` and all included math and
captions, explicitly authorized by the user, plus maintained docs (index and
notation read). The complete manuscript was read by root in the current turn;
the independent startup hash manifest records the version. No maintained API
is used; implementation will be study-owned. External primary sources include
Fastfood (Le, Sarlos, Smola, ICML2013), initialized spectral universality
(Pennington et al., AISTATS2018), and asymptotic liberation (Anderson/Farrell2014)
for novelty/limits, not as unverified proof dependencies.

The candidate is W0=U diag(s) V^T with fast orthogonal U,V and a prescribed
singular spectrum. Compare flat s (orthogonal), Gaussian-singular/quarter-circle
s, and standard iid Gaussian W0. Matching variance or initial forward fields
does not by itself match adjoint reuse. Fixed storage O(n) and matrix actions
O(n log n) are algorithmic possibilities, not a measured speedup claim.

## Initial discriminator, before training

Use a Gaussian input vector h and odd bounded nonlinear response psi. Compare
normalized energy of W0^T psi(W0 h) against the Gaussian reference, holding
the average squared singular value at one. Theory predicts an explicit
dependence on the FOURTH singular moment even though forward marginal variance
is identical. First prove/check that dependence; then decide whether to test
actual two-hidden-layer training. This is a mechanism gate, not a final use case.

Readout/hidden learning under a changed mixer needs a fresh empirical or
theoretical transfer claim; no same-seed operator-norm approximation is claimed.

## Resource contract and progress

CPU/deterministic pilot (amended before implementation/run to add strong
Fastfood-spectrum and Gaussian controls): at most 16 widths/spectral cases and 256 probe vectors
per case, <10 CPU minutes, exact dense oracle only up to width1024. Numerical
Hermite/Gaussian integrations need convergence checks. A training campaign
requires a written protocol before execution; initial reserve <=24 trained
runs and 30 GPU-process minutes, drawn from the user's ongoing authorization.
Other tasks currently own GPU0/GPU1; do not run competing GPU jobs until released.
No package installation, manuscript edits, shared code edits or Git writes.

## Current result and evidence

The route remains a **supporting population-simulation contribution**. A bounded
reference-only split Hadamard implementation resolved the original hardware
limit, and the frozen accuracy–cost screen passes:3.76-fold savings against the
cheapest eligible Gaussian ensemble on its declared grid. See
[POPULATION_COST_SPLIT_REFERENCE_RESULTS.md](POPULATION_COST_SPLIT_REFERENCE_RESULTS.md)
and the scoped [kernel check](SPLIT_REFERENCE_CODE_CHECK.md). All128 candidate
costs and the original [blocked attempt](POPULATION_COST_RESULTS.md) are preserved.

However, a subsequent decision-changing challenge found that the sparse grid
inflates that advantage. Allowing ordinary integer ensemble sizes gives an
estimated Gaussian width2048/K18 competitor and reduces the estimated advantage
to1.689-fold. See [POPULATION_COST_GRID_SENSITIVITY.md](POPULATION_COST_GRID_SENSITIVITY.md).
This is analytical extrapolation from16 trajectories, not a fresh18-run result,
but it defeats the broader interpretation of robust twofold superiority over
strong cheap alternatives. The frozen grid PASS remains valid in its scope.
Accuracy is against a finite32768 ensemble with resolution diagnostics, not a
certified infinite-width truth. The new cost campaign is not freshly reproduced.
No further optimization or validation is authorized by default; both GPUs from
this study are released and the main research effort is elsewhere.

[RESULTS.md](RESULTS.md) is the current empirical synthesis. At width16,384,
the fast Gaussian-spectrum implementation takes 5.22 times less measured
training/evaluation time and 5.40 times less peak allocated CUDA memory than
the same-width dense fixed Gaussian implementation. Both run the actual
nonlinear q=1 learner with moving representations. This is a computational
gain for simulating a specified wide population, not a classification win:
a narrower dense learner already achieves the same six validation errors.

The fresh-seed, width8192 confirmation passes all five predeclared comparisons
of Gaussian-ensemble predictions, within-layer Grams and feature motion.
The complete20-run confirmation was repeated bitwise, as were all10 additional
mechanism-control runs. A separate reviewer independently reproduced two
confirmation trajectories on the other GPU. All numerical evidence is from
one fixed digits3/8 split; it is not a broad architecture benchmark.

The decisive adversarial control preserves the singular spectrum but removes
right-side mixing: learned-trajectory discrepancies grow substantially even
though the independent Gaussian-probe diagnostic is unchanged. Conversely,
the two-point spectrum matching the Gaussian second and fourth moments is
too close on this task to establish that higher spectral moments are needed.
Both outcomes, including the failed discriminator, are retained in RESULTS.

## Derivations and checks

[REUSE_THEORY.md](REUSE_THEORY.md) gives an exact Hermite identity: an odd
nonlinear forward/transpose return depends on the fourth singular moment,
even when forward Gaussian marginals agree. [FAST_REUSE_REVIEW.md](FAST_REUSE_REVIEW.md)
independently checked the proof and exactly reproduced all16 numerical cases.
This result is internally checked in its Gaussian-probe scope, not promoted;
it proves neither trained universality nor priority. Protocol discrepancies
are preserved in the review; its check of the original acceptance rule passes.

[TRAINING_PROTOCOL.md](TRAINING_PROTOCOL.md) and [fast_training.py](fast_training.py)
implement the exact raw q=1 closure with a changed fixed mixer. On digits3/8,
three seeds and widths512/2048 show substantial feature motion and improvement
over frozen features. Exploratory ensemble prediction, both layer Gram and
feature-motion trajectories are closest to Gaussian with the quarter-circle
spectrum. Precise aggregate distance definitions were specified only after
initial output inspection, so this is not a fully preregistered superiority
result. A missing-activation artifact bug was repaired, preserving v1 and
training01; all24 predictions reproduced bitwise in training02. The two reserved
step-halved cases change predictions by at most1.14e-5 RMS. Sources, config and
data are retained in those generated directories. [TRAINING_CODE_REVIEW.md](TRAINING_CODE_REVIEW.md)
and [CONFIRM_REVIEW.md](CONFIRM_REVIEW.md) give the completed internal code,
measurement and independent reproduction checks.

Closest-prior audit has found Wang--Zhong--Fan arXiv2206.13037v3 explicitly
constructing fast prescribed-spectrum Hadamard ensembles for nonlinear AMP.
The spectral construction is therefore not our novelty. [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)
records the precise prior-art boundary. [POLYNOMIAL_TRANSFER.md](POLYNOMIAL_TRANSFER.md)
proves a finite-step ensemble-universality corollary for polynomial activations,
including adaptive residual and clock feedback; [POLYNOMIAL_REVIEW.md](POLYNOMIAL_REVIEW.md)
is a separate internal PASS. This changes the activation and is not substituted
for the actual tanh learner.

[TANH_TRANSFER.md](TANH_TRANSFER.md) proves the actual tanh result. Its
deterministic reverse-order clipping bridge is in
[TANH_CLIPPING_REVIEW.md](TANH_CLIPPING_REVIEW.md), and its finite Lipschitz-program
universality reduction is in [LIPSCHITZ_PROGRAM_TRANSFER.md](LIPSCHITZ_PROGRAM_TRANSFER.md).
The complete integration passed a separate internal mathematical audit in
[TANH_TRANSFER_REVIEW.md](TANH_TRANSFER_REVIEW.md). Neither result is a
continuous-time, all-time, finite-width-rate or same-realization approximation
theorem. No material is promoted.

[APPLICATION.md](APPLICATION.md) explains the proposed paper use case.
[CONTRIBUTION_REVIEW.md](CONTRIBUTION_REVIEW.md) and
[NOVELTY_ADDENDUM.md](NOVELTY_ADDENDUM.md) delimit its significance: a serious
supporting population-simulation use case, not established broad architecture
superiority or a new general universality principle. A further local orientation
identity in [INITIAL_ACCELERATION.md](INITIAL_ACCELERATION.md) passed the
separate internal audit [INITIAL_ACCELERATION_REVIEW.md](INITIAL_ACCELERATION_REVIEW.md).
It isolates actual initialized feature acceleration beyond isotropic probe
diagnostics in its stated local/small-scale scope and is not a long-time or
memory-specific effect.

## Reproduction and ownership

Protocols precede each confirmation, scaling and mechanism campaign. Exact
original protocol versions and source versions v1/v2/v3 are retained; repairs
are documented rather than silently changing the registered criteria. Generated
data and logs are under data/generated/response_memory_fast_mixing_20261002/.
RESULTS gives the producer/reproduction commands and complete artifact map.
All campaigns are closed. The initial accuracy–cost reference attempt stopped
at its explicit resource gate; a separately authorized bounded completion then
supplied all32 references without changing candidates or thresholds. The
integer-grid challenge narrows its practical significance. No ongoing job needs
to be resumed. Both GPUs were released after the bounded completion.

Current ownership: root owns overall assembly; frontier_attention completed
the explicitly delegated accuracy–cost producer repair, protocol addendum,
analysis, results and README status, alongside the scoped literature and
program-transfer derivations;
fast_reuse_review and frontier_control_proof_review own their internal audit
reports. These scoped assignments import no scientific findings from other
studies. Neither manuscript, maintained book/code nor Git index was changed.
