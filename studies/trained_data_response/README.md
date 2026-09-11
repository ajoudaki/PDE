# Trained data response at a nonlinear fitted reference

Status: active research; no primary theorem is yet independently accepted.
This study addresses milestone 1 only: capture the data-direction derivative
of actual finite gradient flow after substantial learning, including T=40,
and construct a usable forced population evolution.

The model is two width-n tanh hidden layers, no biases, d=2, normalized
input u=x/sqrt(2) on S¹, stored initialization variances (1,1/n,1/n²),
mobilities (n,1,n), unhalved mean squared loss, and physical time. The finite
Gaussian readout is retained. The reference is
nu*=½ delta_(sqrt(2)e1,+1)+½ delta_(sqrt(2)e2,-1), using its actual C.4.5
global flow and fitted endpoint. For every fixed deterministic Borel law nu
on sqrt(2)S¹ × [-Y,Y], Y≥1, differentiate actual finite GF at epsilon=0+
along (1-epsilon)nu*+epsilon nu, then take width to infinity. Nonatomic
finite losses are integrated exactly. No training experiments are authorized.

The target state is full first-row clock L², middle-increment Hilbert–Schmidt,
and readout L². The initialized middle action is retained with its actual
adjoint and need not be Hilbert–Schmidt. Required convergence is in probability
uniformly on each fixed [0,T] and the whole input circle, with identified
state/action measurements. No cross-carrier operator-norm limit, uniform
failure probability over laws, or uniform-time finite-width limit is claimed.

| Component / route | Owner and assigned file | Current scope / bottleneck |
|---|---|---|
| Homogeneous trained propagation | `/root/propagator`, PROPAGATOR.md | Candidate: finite-rank Gauss–Newton endpoint plus integrable curvature; singular endpoint must be handled |
| Actual finite weighted source | `/root/weighted_source`, WEIGHTED_SOURCE.md | Candidate: column-deletion cavity estimates for passive reverse queries; weighted uniform integrability required |
| Actual derivative capture | `/root/capture`, FINITE_CAPTURE.md | Fixed-program approximation and strong multiplier passage; depends on actual finite source lemma |
| Contract, synthesis and checks | `/root`, remaining study files | Assemble complete proofs, deterministic algebra checks, then freeze for isolated reviews |

The coordinator alone edits this README and writes Git, taking the common
nonblocking writer lock for each scoped transaction. All generated files and
reviewer scratch go to `data/generated/trained_data_response/<run>/`.
No established book/code change is authorized. Startup HEAD was
`ca98db4ff20fd8e6ccdc7b0b1a606193177106f3`; the index was empty. Concurrent
PDF-exporter and repository-maintenance work is outside this study and preserved.

Authoritative sources are the maintained `docs/global_nonlinear.md` B.1,
C.4 and C.4.5, `docs/special_data_limits.md` III.F and applicable value,
response and obstruction passages, `docs/finite_dynamics.md` §§1–4,
and the shared notation and reading guide. The training-law stability P2
and robust-learning-horizon P1 packages are incorporated; their historical
drafts are not substituted for maintained proofs. Both required mathematical
skills and applicable research-contract, evidence, audit and proof-search
references are in use.

The primary theorem remains open until the exact equation, admissible
off-support forcing, actual finite-width identification and population
propagator estimates have complete proofs. A failed estimate is not a
counterexample. Signed zero-mass extension will be through the linear equation,
without assuming a two-sided probability-law neighborhood.

Next authorized action: complete the three proof routes, reconstruct and check
their arguments, then freeze complete inputs and obtain two fresh isolated
adversarial reviews. Any required correction needs a new complete review round.
Promotion, if justified, requires all additional workflow gates and approval
of a concrete reviewed edition; this study does not itself authorize promotion.
