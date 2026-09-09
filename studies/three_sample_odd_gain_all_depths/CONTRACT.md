# Research contract: three samples, one nonlinear activation at every depth

2026-09-08. This continues the user's request for the strongest rigorously
proved global general-depth theorem for three samples. The user also asks
for adversarial agents to check the proofs.

The network, initialization, raw metric, simultaneous raw GD step n^-2,
canonical population construction and observables are the same as in the
preceding three-sample/two-hidden-layer contract. Here L counts hidden
layers and ranges over all fixed finite integers L>=2. The three inputs
obey ||x_i||²=d and |x_i^T x_j/d|<=1-delta, 0<delta<=1, with arbitrary
binary labels. Singular input Grams are allowed. All weights train.

The primary previously requested family is the odd convex mixture
(1-theta)z+theta atan(z). The user has now permitted a small constant
offset, while explaining their expectation that excluding antipodal
inputs ought to suffice for oddness. No counterexample to the strictly
positive convex-mixture global theorem has been established.

This directory develops a separately identified theorem for
phi_delta(z)=a_delta(z+atan z). Its overall gain is an extra degree of
freedom. A question about whether this also meets the user's preferred
activation constraint remains pending as of this contract's creation.
Proving this additional theorem does not prove the unit-sum convex-mixture
claim, nor the claim with only a small additive offset. Dividing the
activation by its gain is not an allowed inference about the same raw
training dynamics.

The candidate quantifier is one a_delta depending on delta alone, working
for every fixed finite L>=2 and every admissible triple. The desired
dependence is a_delta=C delta^-2, with equal positive coefficients on z
and atan z. No width/time dependence, frozen hidden weights, altered
learning rates or positive input-Gram assumption is allowed. Field/time
normalizations must be exact identities for the original raw metric.

The full target includes global canonical strong GF, nonsymmetric
bounded-primal uniqueness and reached-state restart; full-sequence
compact-time finite GF/raw-GD limits; genuine adjacent adjoints; all L+1
raw kernels; same-layer path and velocity W2, second moments and integrated
speeds; uniform absolute activation regression nonaffinity; nonzero
initial acceleration of every hidden block and every sample/layer; and
a changing projected kernel. Infinite time and infinite width are not
interchanged. No L growing with width is asserted.

Only new theoretical work and local research artifacts are undertaken.
No experiment, commit, publication or change to older theorem files is
part of this turn. The source, gain and motion routes are developed
independently, then the complete candidate is frozen and adversarially
reviewed. Mathematical correctness and satisfaction of the user's
preferred activation constraint are separate questions.
