# Structured initialization variants for response-memory training

28 September 2026. A new study for the user's request to modify block
Gaussian initialization while retaining inexpensive fixed actions, a small
moving response-memory state, and approximation of canonical dense trained
predictors. This is a bounded theoretical design investigation. No neural
experiments, paper edits, or Git writes are authorized or planned here.

## Contract and inputs

Use the canonical model and learning rates in docs/notation.qmd, with fixed
finite depth and training data, tanh as the initial activation target,
zero initial readout, and small fixed labels with a positive initial
training feature-Gram gap. The intended target is the canonical dense
Gaussian population flow and its whole-test predictor throughout training,
including the final predictor. The existence of a regular dense flow may
be assumed; no quantitative trained-width or structured-initialization
comparison is assumed.

Baseline design: n=Bk neurons, aligned independent k-by-k initialized
Gaussian blocks with entry variance 1/k; all learned updates remain
globally connected. New variants may alter this initialization or combine
several autonomous estimators, but must disclose each change, its exact
state/runtime cost, and any remaining target-identification obligation.
Matching initialization kernels or spectra alone is not a trained theorem.

Scientific inputs are the self-contained problem, fresh derivations here,
and maintained docs/ material (entry point and notation read in full).
Other studies are not dependencies. The investigate-conjectures and
solve-math-rigorously skills, including research-contract and
adversarial-audit references, govern the work.

## Assignments

- Parent: exact reuse diagnostics for structured matrices, literature
  applicability if needed, synthesis and this README.
- A fresh prompt-only route: static block/sparse mixing alternatives.
- A fresh prompt-only route: extrapolation or multilevel alternatives.

## Results and recommendation

The bounded design assessment is complete. No proposed modification is yet
proved to preserve the canonical trained predictor at the desired cost.
Two concrete candidates deserve distinction:

1. **Fast global mixing with a prescribed Gaussian-limit spectrum.**
   `STATIC_VARIANTS.md` gives an explicit signed Hadamard construction,
   O(n) fixed storage and O(n log n) fixed actions, deterministic operator
   norm at most two, and exact fresh-input/reuse diagnostics. The persistent
   fixed-k discrepancy disappears in those diagnostics. Independent-block
   particle structure is lost. Nonlinear adaptive matrix/transpose reuse,
   even on compact training intervals, still requires a comparison theorem.
2. **Two block sizes with a signed output correction.**
   `DEBIAS_VARIANTS.md` gives ordinary and coupled/antithetic variants,
   exact Gaussian marginals, algebraic cancellation under an explicitly
   stated trained expansion, and constant-factor state overhead. This keeps
   the block initialization structure in each autonomous component. It
   requires a trained-bias expansion, and is an ensemble rather than one
   canonically trained network under a common residual.

For a single changed initializer, candidate 1 is the more direct attempt
to remove locality while keeping fast actions. For preserving the existing
block-particle analysis, candidate 2 changes less. Neither is a theorem-level
replacement for the dense initializer in the paper.

`PARENT_DIAGNOSTICS.md` independently derives the spectral obstruction to
mere orthogonal scrambling and the forward correction remaining in
biorthogonal blocks. It also gives a conservative conditioned-Gaussian
proposal: bounded block norms with whole-path coupling failure at most
O(L B exp(-c k)). This repairs a tail issue, not the trained block bias;
the transfer is not uniform in B at fixed k.

## Checks and source scope

Both independent prompt-only route reports were read in full. Their claims
are new internal calculations, not promoted results. The parent checked the
biorthogonal fourth-moment formulas against its independent derivation.
An exhaustive enumeration of all 256 intermediate sign configurations at
n=8 verified the fast mixer's row/column norms, second/fourth entry moments,
and spectral second moment to 1e-12. This is an algebra check, not a neural
experiment or evidence of trained convergence.

Full primary PDFs of Fastfood (2013) and Giles's multilevel path simulation
(2008) were retrieved. Their relevant computational/kernel and conditional
multilevel statements are documented in `PARENT_DIAGNOSTICS.md`; no neural
trained theorem is imported from either. No other study was a scientific
input. No experiments, paper edits, or Git writes were made.

The main open obligation is quantitative approximation of the canonical
trained dense predictor under a changed initialization, including nonlinear
matrix/transpose reuse and all-time test behavior. A favorable
initialization diagnostic, an exact telescoping identity, or a norm bound
does not discharge that obligation.

## Continuation: matched-error compression proof

The user now prioritizes a complete multiple-input, small-label compression
theorem against the canonical dense population over retaining any particular
initializer. This continues the same target investigation. The selected
initial route is ordinary Gaussian blocks, without extrapolation or new
global mixing: it preserves the Gaussian conditioning mechanism and avoids
adding an unproved trained universality or bias-expansion hypothesis.

The desired error is sup over t>=0 of the L2(mu) passive-test discrepancy,
in probability (or a specified second-moment bound), including the final
predictor where it exists. Fixed depth, finite normalized training data,
tanh, zero readout, a positive initial population feature-Gram gap and a
sufficiently small fixed label RMS are the intended model conditions.
Constants may depend on these fixed data and mu; width, block size, moment
order and physical time are approximation variables. The Gram gap is a
necessary explicit data/initialization condition, not a consequence of small
labels alone. Dense regular population existence is allowed; a quantitative
dense-width or trained block-bias estimate is not.

Two fresh restricted routes completed their initial attempts:
`TRAINED_WEAK_RATE.md` derives the initialized k-rate and the exact missing
trained Gaussian interpolation cancellation; `BLOCK_PARTICLE_RATE.md`
derives quantitative particle statements with visible k,q constants.
They used maintained docs/ but no other studies or previous route reports.
The parent independently derived initialization bias/variance and the
small-label canonical-flow bounds, then checked the complete complexity
implication. A third prompt-only derivation checked the latter bounds.
Later explicit consolidation messages ended blind independence; all
subsequent exchanges are ordinary collaboration.

The current synthesis is `MATCHED_ERROR_STATUS.md`. Its central target
remains open. Concrete progress:

- `INITIAL_GRAM_RATE.md`: initialized kernel bias O(1/k) and fluctuation
  O(1/sqrt(Bk)), proved without an input-Gram inverse. The independent
  Gaussian route derived the same covariance recursion.
- `SMALL_LABEL_KERNEL_CHECK.md`: fully deterministic all-time fitting of
  canonical GF, and width-independent O(Y^3) comparison with the initial
  readout-kernel flow. Parent checked the complete proof and constants.
  Combined with initialization, this gives an actual finite-block bound
  CY[1/k+1/sqrt(n delta)+Y^2], on explicit norm/gap events. Its Y^3 budget
  prevents arbitrary-accuracy conclusions at a fixed nonzero Y.
- `BLOCK_PARTICLE_RATE.md`, Sections 1–3: exact moment passivity and a
  single small-label threshold proving global existence, finite activity,
  fitting and passive endpoints uniformly in B,k,q, for bounded initial
  block operators. The cap is an explicit conditioned-Gaussian initializer;
  finite unconditioned systems transfer only on their stated norm event.
  `BLOCK_ACTIVITY_CHECK.md` records a scoped independent check, two small
  clarifications, their resolution and the final source hash. Parent read
  both reports completely and verified the estimates. This is internal
  checking, not promotion or a canonical dense-prediction theorem.
- The supplementary particle rate in Section 4 has a k,q-dependent label
  threshold. It has been read by the parent, but was outside the independent
  activity check; it is not used to assert the desired joint limit.
- `UNIFORM_ACCUMULATOR_RATE.md`: at that same single label threshold,
  the actual finite-q closure has integrated middle-weight velocity defect
  at most C Y^3/q, uniformly in B,k,q and over all physical time. The same
  bound controls its reconstructed learned operator against the exact
  accumulator of its OWN responses. The proof combines the exact moment
  energy/projection identity with a layer-by-layer activity-H1 estimate;
  it does not differentiate backward histories or the residual direction.
  Parent derived the mechanism and read and checked the complete final
  proof. This is source consistency, not tracking of the dense trajectory.

Remaining: trained bias that vanishes with k at fixed Y, quantitative
particle control under the single fixed label threshold, and amplification
control converting the uniform source defect into a finite-q/dense-target
prediction bound. No universality,
trained Taylor expansion, or Monte Carlo rate is inserted as an assumption
to declare the target solved. No neural experiments, paper edits or Git
writes were made.
