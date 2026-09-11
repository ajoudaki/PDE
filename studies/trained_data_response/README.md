# Trained data response at a nonlinear fitted reference

Status: all primary claims in frozen R1 accepted by two fresh complete isolated
scientific reviews, with no required corrections. Canonical assembly and its
separate promotion reviews are in progress; nothing has been promoted.
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

| Component / route | Owner and proof | Current scope |
|---|---|---|
| Homogeneous trained propagation | `/root/propagator`, [PROPAGATOR.md](PROPAGATOR.md) | Complete author proof: singular endpoint kernel compatibility and integrable curvature/finite-rank perturbation give uniformly bounded U(t,s) |
| Actual finite weighted source | `/root/weighted_source`, [WEIGHTED_SOURCE.md](WEIGHTED_SOURCE.md) | Complete author proof: column-deletion comparison for actual finite GF, Gaussian chaining and weighted uniform integrability; bounded feature segment gives all-time population forcing |
| Actual derivative capture | `/root/capture`, [FINITE_CAPTURE.md](FINITE_CAPTURE.md) | Complete author proof: finite right derivative, fixed-program/strong multiplier passage, arbitrary fixed Borel forcing, whole-circle observations |
| Contract, synthesis and checks | Original task coordinator `/root`, [THEOREM.md](THEOREM.md) | Frozen R1 packet, executed deterministic checks; both independent reviews ACCEPT |
| Concurrent reconstruction | Task `01a090bb-ded9-7f73-b893-0fce3cf9e257`, [CONTINUATION_COORDINATION.md](CONTINUATION_COORDINATION.md) | Owns its named reconstruction/alternative files; no main-proof or README writes; its checks are author-side only |

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

The reviewed study proves all primary claims at their stated scope: forced
clock-state evolution, every fixed-horizon finite-GF capture, and a uniform
population propagator with `C_Y T ||sigma||TV` response. Conditioning is
exposed through the endpoint training Gram pseudoinverse; it has not been
numerically evaluated. Signed zero-mass extension is through the linear
equation, without assuming a two-sided probability-law neighborhood.
Both complete independent reviews found no surviving mathematical gap.

The coordinator read every component and its invoked maintained proof inputs.
The propagator author additionally read the complete source and capture proofs;
the capture author checked the complete source interface. No substantive
author-level objection remains. These are author checks, not independent review.
The concurrent [continuation reconstruction](CONTINUATION_CHECK.md) likewise
found no substantive gap. Its startup missing-source diagnosis was made while
the original author was still writing that file and is superseded. Its
`fed0567` commit preserved recovered files without changing proof bodies.
The original task acknowledges its coordination note and retains ownership
of the main proofs, README, freeze/reviews and any promotion preparation.

## Frozen inputs and reproducible checks

The complete [R1 proof](R1_PROOF.md), [dependencies](R1_DEPENDENCIES.md),
[manifest](R1_MANIFEST.json), and [neutral assignment](R1_ASSIGNMENT.md) are
immutable. Manifest SHA256:
`17cfcd0231bd39079f8f5d4b33e1911201ed3c20d62cce8fe8b5a281cd3cd362`.
Proof SHA256: `38b2c81be6e32f3d93f7fd85145487b33b2676b6d8698c504230189b9e625721`.
Dependencies SHA256: `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79`.
Fresh isolated nonauthors `/root/scientific_r1_a` and `/root/scientific_r1_b`
received only that assignment, complete frozen inputs and required skills.
Their complete reports [A](R1_REVIEW_A.md) and [B](R1_REVIEW_B.md) both
give ACCEPT, with no required corrections. The coordinator read every line,
verified the packet/component/report hashes, and inspected the actual check
outputs. Report hashes are respectively
`b52cbf930119686b2b754b1f09242d5c66ce344da13cc58d4185051ed2152ca6` and
`4a40f727abb02897a109db2dbb7741175a53960d8e1ff420ac99c9fb16949487`.
Their extra exact checks are preserved as [A check](R1_REVIEW_A_CHECK.py)
and [B check](R1_REVIEW_B_CHECK.py), in addition to original scratch and logs.
Coordinator verification is in
`data/generated/trained_data_response/review_acceptance_01/verification.json`.

From the repository root, choosing a fresh generated path:

```sh
python studies/trained_data_response/R1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/NEW_RUN
python studies/trained_data_response/R1_REFERENCE_CERTIFICATE.py
```

The first checks tangent signs/normalizations with nonzero readout, the raw
loss metric, weighted Gram identity, singular semigroup and incompatible
nilpotent boundary. Its central-difference errors decrease by a factor four
and end at `1.61e-8`; the loss-metric error is `7.91e-12` or smaller.
The exact rational reference certificate and the source's embedded exact
Laurent-polynomial identities also pass. Full outputs and hashes are under
`data/generated/trained_data_response/frozen_checks_01/`. These are algebra
and constant checks, not training or formal verification. A first optional
source check could not import SymPy and was replaced by an executed
standard-library exact check; the failed attempt remains in source_01.
The continuation's separate deterministic runs remain linked in its report.

The independent [relevance report](RELEVANCE.md) accepts assembly as C.4.6
after C.4.5.3, with only narrow reading-guide and C.4 navigation updates.
Its fresh isolated selector instance was
`01a090c0-8a58-7da1-8075-8c0b0f23f959`, launched without history; full
process/access logs and successful exit are retained in
`data/generated/trained_data_response/relevance_01/launch_03/`.
The coordinator read its complete report, verified its hash
`958f833f3039b094a7ce4c56f978d18c71c385adf5893c56906798fa036dae61`,
and checked its recorded access scope. This selector authored no mathematics.
Two earlier launcher failures remain labeled in the same generated run.

Next authorized action: `/root/capture` assembles the complete canonical
section in `CANONICAL_SECTION.md`; `/root` prepares exact ancillary edits,
standalone validation, fresh paired scientific reviews of that assembly,
and a separate fresh integration review. [prepare_promotion.py](prepare_promotion.py)
only writes a fresh generated draft; it cannot install into established files.
Scoped commits so far: `e111b63` (startup), `fed0567` (concurrent recovery),
`2c5cddb` (complete proofs and immutable R1 freeze).
Further commits use the common lock and explicit owned paths. Any required
scientific correction needs a new complete review round. Promotion requires
approval of the concrete reviewed edition. No established book/code file has
been changed by this study.
