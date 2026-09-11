# Trained data response at a nonlinear fitted reference

Status: all primary claims are proved and accepted in two complete isolated
R1 scientific reviews. The canonical P1 addition also has two fresh scientific
ACCEPT reports, and corrected P1I2 packaging has a fresh integration ACCEPT.
All reports, hashes and actual checks are verified. The concrete promotion
proposal is ready for specific user approval; nothing has been promoted.
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
| Homogeneous trained propagation | `/root/propagator`, [PROPAGATOR.md](PROPAGATOR.md) | Reviewed proof: singular endpoint kernel compatibility and integrable curvature/finite-rank perturbation give uniformly bounded U(t,s) |
| Actual finite weighted source | `/root/weighted_source`, [WEIGHTED_SOURCE.md](WEIGHTED_SOURCE.md) | Reviewed proof: column-deletion comparison for actual finite GF, Gaussian chaining and weighted uniform integrability; bounded feature segment gives all-time population forcing |
| Actual derivative capture | `/root/capture`, [FINITE_CAPTURE.md](FINITE_CAPTURE.md) | Reviewed proof: finite right derivative, fixed-program/strong multiplier passage, arbitrary fixed Borel forcing, whole-circle observations |
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

The complete [canonical section](CANONICAL_SECTION.md) is assembled by
`/root/capture` and frozen unchanged as [P1_SECTION.md](P1_SECTION.md).
The coordinator read all 2062 lines and the final notation corrections.
Its SHA256 is
`33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38`.
The [P1 manifest](P1_MANIFEST.json), hash
`f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d`,
freezes complete science/dependencies, proposed ancillary text, recipes,
and neutral review assignments. Two fresh isolated scientific processes
`01a090ca-1bf7-70b1-be49-7ac58e2e0f6d` and
`01a090ca-1e9e-7482-8804-54261fdfc386`, and the separate integration
process `01a090ca-1d3f-7082-b65f-2dcd9bcaa82b`, completed their reviews.
Full access/check/process logs are under `scientific_p1_a`,
`scientific_p1_b`, and `integration_p1` in the generated namespace.

Standalone validation passed, including exact base preservation outside
the selected edits, guide links/fragments and both mathematical checks.
Evidence is `standalone_01/validation_02`; its first failed validator
heading match is retained. The original [integration report](P1_INTEGRATION_REVIEW.md)
requires packaging corrections only: undeclared structural-file reads and
an extra assignment entry outside its allowed list. It found no scientific
defect. The coordinator read the entire report and verified its hash
`47dc9f59e3a3595d34bb7c7e2895aa691dc26246f998dae0a7a4afb52376b834`.
The assembler now pins every structural input and the integration-specific
manifest includes only authorized files. `standalone_02/validation` passes
and both proposed destination hashes remain identical. P1 inputs are untouched.
The frozen [P1I2 integration manifest](P1I2_MANIFEST.json), hash
`174bd123c8fd48cdc536925681f7eade0b5f37f3b3b1cebf53d7b383a0a5298f`,
has a fresh complete [integration ACCEPT](P1I2_INTEGRATION_REVIEW.md) by
instance `01a090d2-454d-7550-8cdd-ef01257c6712`, with logs in `integration_p1i2`.
The coordinator read all 263 report lines and verified its hash
`5ba1f42becdc703f7cc4cc3a1df837e079a6e156d2e599a2c0b61870db21adef`,
the successful process exit, and all actual command/audit outputs. Both
packaging objections are resolved. No required scientific or integration
correction remains. P1_BUILD.py is retained as an immutable predecessor;
use P1I2_BUILD.py and P1I2_VALIDATE.py for fresh standalone reproduction.
[P1 scientific review A](P1_REVIEW_A.md) and [review B](P1_REVIEW_B.md)
both accept with no required corrections. Both complete reports, input
hashes, independent check results, process identities and successful exits
have been read or verified by the coordinator. Their report hashes are
`1dff779a0721ce15b6d660cd7a9b46a555224537771509ccc3fb9e86beda34bd` and
`768b2fc7e20f6d65e530a6bd87e485a07314d8b1960122fe91dab601b8235349`.
Coordinator verification is in `scientific_p1_acceptance_01`; their extra
checking sources are preserved as P1_REVIEW_A_CHECK.py and P1_REVIEW_B_CHECK.py.

The complete [result and promotion proposal](PROMOTION_PROPOSAL.md) records
the exact model, norms, horizons, limit order, forcing/propagator bounds,
conditioning, downstream exclusions, review evidence, source hashes and
reproduction commands. No primary proof gap remains. Nonlinear changed-law
flows, finite-contamination remainders, transport forcing control, endpoint
continuity, sampling/risk expansions and GD derivatives remain outside this
milestone. The uniform claim is population homogeneous propagation; forced
response grows at most linearly in the horizon and width capture fixes T.

Next action requiring the user's approval: promote only the exact reviewed
P1 text using P1I2 assembly, after rechecking unchanged sources. All authorized
research and promotion preparation are complete. Established-file edits await
specific approval. [prepare_promotion.py](prepare_promotion.py) only writes a
fresh generated draft; it cannot install into established files.
The closing verification in
`data/generated/trained_data_response/final_acceptance_01/verification.json`
checks every frozen packet/report hash, all declared live inputs, process
completion and identity, and the successful independent edition audit.
Scoped commits so far: `e111b63` (startup), `fed0567` (concurrent recovery),
`2c5cddb` (complete proofs and immutable R1 freeze),
`b922d12` (accepted R1 reviews and assembly preparation),
`fb2353c` (canonical P1 freeze and standalone verification),
`bb256d8` (accepted canonical science and corrected integration packaging).
Further commits use the common lock and explicit owned paths. Any required
scientific correction needs a new complete review round. Promotion requires
approval of the concrete reviewed edition. No established book/code file has
been changed by this study.
