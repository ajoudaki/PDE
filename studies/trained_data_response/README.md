# Trained data response at a nonlinear fitted reference

Status: active research; no primary theorem is yet independently accepted.
This study addresses the primary response milestone: capture the data-direction derivative
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
| Homogeneous trained propagation | original `/root/propagator`; reconstruction `/root/propagator_reconstruct`, PROPAGATOR_CHECK.md | Complete author candidate in PROPAGATOR.md; checking singular endpoint and dependencies |
| Actual finite weighted source | `/root/weighted_source_recovery`, WEIGHTED_SOURCE.md | Missing source recovered by a new column-deletion cavity proof; not yet complete |
| Independent source route | `/root/source_alternative`, SOURCE_ALTERNATIVE.md | Population passive weighted source and alternatives to strong finite moment hypotheses |
| Actual derivative capture | original `/root/capture`; coordinator owns FINITE_CAPTURE.md | Conditional fixed-program bridge; requires the missing weighted-source lemma |
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

Continuation checkpoint, 2026-09-11: HEAD `e111b63`; index initially empty.
Recovered untracked THEOREM.md, PROPAGATOR.md, FINITE_CAPTURE.md and
check_identities.py without replacing them. The prior WEIGHTED_SOURCE.md was
absent, so every conclusion depending on it remains conditional. The theorem
draft's references to that missing proof are obligations, not accepted evidence.
The current coordinator read the complete recovered component drafts and the
maintained B.1/C.4/C.4.5 proofs. The resumed author agents above are not isolated
reviewers and cannot count toward the two fresh scientific reviews.

Deterministic check: `python studies/trained_data_response/check_identities.py
--output data/generated/trained_data_response/algebra_recovery_20260911`
exited zero with PASS on Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0.
The script hash is `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f`.
Its retained results check finite tangent/source factors, the raw loss metric,
the singular semigroup identity and a nilpotent incompatible-factor witness.
They do not validate the missing probabilistic estimate or constitute training
experiments. Generated evidence is in the indicated separate data directory.
