# C-X1: many-point nonlinear observable closure

Opened 2026-09-19 at the user's explicit request to conduct and prove C-X1.
Initial HEAD: `019e3630237e33f58b9636c0aa67a039bebf0182`; the Git index was
empty. Pre-existing modifications and untracked studies are unrelated and
must be preserved. This task is the sole Git writer for this study.

## Frozen research contract

For every separately fixed integer `1 <= m <= d`, binary labels
`y_a in {-1,+1}`, and normalized inputs `u_a in S^(d-1)` sufficiently close
to the distinct coordinate vectors `e_a`, study two tanh hidden layers with
canonical independent stored Gaussian variances `(1,1/n,1/n^2)`, output
`c^T h2/n`, physical mobilities `(n,1,n)`, and unhalved **mean** squared loss.
The finite random readout is retained. The full first-row field and the
actual Gaussian middle action and its adjoint are retained.

The required result supplies a positive geometric radius and finite physical
learning horizon (allowed to depend on fixed m,d, independent of width and
every approximation resolution), canonical strong population dynamics and
finite-network capture through that horizon, final loss at most 1/4, positive
paired motion in both hidden layers at a specified positive time, and an
autonomous restartable finite observable hierarchy with qualitative numerical
and order convergence in whole-sphere prediction and declared joint hidden /
action observations. A short-time theorem or a conditional source-tail bound
alone does not resolve C-X1. No growing-m/d limit, approximation-order rate,
automatic accuracy certificate, all-time perturbed-law theorem or model
superiority is required. An actual raw-GD bridge must state and prove its
step condition; finite GF and numerical ODE integration remain distinct.

Primary data are equal-weight finite point configurations. Explicit supported
nonatomic families are a strengthening only if justified without displacing
the required finite-data result. Numerical closure state size may depend on
fixed dimension and order, not on neural width or elapsed training steps.
Coefficients must be obtained from initialization, not fitted trajectories.

## Scope and evidence

Scientific inputs: this study and established `docs/` and `code/`, with their
designated reproduction inputs. Other studies and their unpromoted findings
are not inputs. Required skills are `solve-math-rigorously` and
`investigate-conjectures`. Full independent review is required before calling
the package established; promotion additionally requires explicit approval
of the concrete reviewed book/code addition.

Current status: research in progress; no new theorem accepted. The principal
obligations are a many-anchor fitted reference, reached active/passive query
control for perturbed configurations, and compatible dimension-general
hierarchy and numerical implementation. They will be proved or recorded as
gaps separately; reference fitting does not establish the perturbed theorem.

No training campaign is authorized by this record. Deterministic verification
of the construction and code is within scope. Any bounded numerical validation
will receive a recorded purpose, configuration, resource cap, and fresh output
directory before execution. Generated files belong exclusively to
`data/generated/cx1_many_point_closure_20260919/`.

## Ownership and routes

- Supervisor owns this README, final theorem assembly, integration and Git.
- Scoped contributors receive disjoint flat output files and explicit inputs.
- Independent proof routes start in fresh contexts and do not read each
  other's outputs until frozen. Reviewers receive complete frozen inputs
  without author history or earlier verdicts.

## Next work

Read complete relevant maintained proofs; develop and check the reference,
perturbation, and closure obligations; run appropriate deterministic checks;
then assemble and independently audit a complete candidate, if obtained.
