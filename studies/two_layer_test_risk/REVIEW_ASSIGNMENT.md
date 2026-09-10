# Neutral bounded internal review assignment

Review the study's precise local claims and limits. This is an internal
adversarial check, not either of the two isolated promotion reviews.
Do not author a new approach, change the model, run training or extend the
quadrature budget. Do not inspect historical studies or other reviewers.

The fixed target is two tanh hidden layers, linear stored readout,
initialization variances `(1,1/n,1/n^2)`, all-block mobilities `(n,1,n)`,
mean square loss on the three angles `0,pi/5,-pi/5` of the radius-sqrt(2)
circle, labels `cos(3 alpha)`, and uniform whole-circle test risk for that
teacher. Compare fully trained population flow with its initial hidden
features frozen, at uniquely matched training loss. The desired full result
is a finite-time sign; a rigorously scoped partial reduction may be valid
without satisfying that desired full result.

Read every scientific line in the following unchanged input files:
`RESULT.md`, `CUBIC_DERIVATION.md`, `MATCHING_AND_REMAINDER.md`,
`check_coefficient.py`, `check_finite_identity.py`, `QUADRATURE.md`.
Read the complete relevant dependency statements and proof bodies:
docs NOTATION; docs README; global_nonlinear sections 2--3, A.1--A.4,
and C introduction/C.1--C.3 including weighted correction;
finite_dynamics introduction/sections 1--4; gaussian_calculus sections
1--3, 7.1 and E; code README and called finite_flow_jets producer plus
argument/scaling/parameter dependencies in finite_network.
These dependency files remain at the hashes listed in SOURCE_AND_CHECKS;
use that file only for hashes/read locations, not as a correctness verdict.
Read both required math/research skills and applicable audit references.
The input files are frozen for this review; report if their hashes change
or a needed proof input is missing. No checkout clone/worktree is allowed.

Check normalizations, moving residual, two directions of reused matrices,
singular input/passive geometry, initialization moments, uniform-in-angle
remainder, the clock inverse, hidden motion/nonaffinity, finite GF/raw-GD
quantifiers and whether the numerical evidence warrants any sign conclusion.
Reconstruct nontrivial steps rather than accepting author verdicts. Inspect
the retained numerical result/metadata files as evidence; further quadrature
executions are forbidden because its three-run budget is exhausted.

Write only `INTERNAL_REVIEW.md`, with complete read coverage and input hashes,
actual attacks and outcomes, exact accepted claim scope, unresolved objections,
and an explicit distinction between a valid partial theorem and an unproved
finite-time sign. No Git commands that mutate the index or history.
