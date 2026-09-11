# Training-law stability and the input-population limit

Status: active theoretical study; no result is yet marked resolved or promoted.

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
| Transport comparison | `/root/transport` | Coupled observations, full first-row distance, individual reference tails | Developing `TRANSPORT.md` |
| Strong population construction | `/root/population` | Common Gaussian generated spaces; state completion of finite laws | Developing `POPULATION.md` |
| Nonlazy open family | `/root/nonlazy` | Actual-flow C.3 activity and state continuity | Developing `NONLAZY.md` |
| Joint finite algorithm limit, statistical argument, synthesis | `/root` | Fixed finite oracle proxy and ordered limits; ghost replacement | In progress |

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

Next authorized action: complete and cross-check the four proof components,
then freeze a full candidate for isolated review. Reproduction at present is
mathematical reading; no executed numerical result is asserted.
