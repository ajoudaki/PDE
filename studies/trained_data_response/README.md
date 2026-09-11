# Trained data response at a nonlinear fitted reference

Status: promoted on 2026-09-11, with the user's explicit approval, as
[established C.4.6](../../docs/global_nonlinear.md#c46-trained-data-response-at-the-fitted-tanh-reference).
All primary claims are proved. The R1 and canonical P1 packets each have two
complete isolated scientific ACCEPT reports, and corrected P1I2 packaging
has a fresh integration ACCEPT. The exact approved edition is installed;
live correspondence and affected standalone checks pass. See the final
incorporation record below for approval, gates, hashes and commits.
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

The original coordinator owns the milestone-1 and promotion records in this
README. The separately started P2 task owns its P2 artifacts and later README
checkpoint, as declared in [P2_COORDINATION.md](P2_COORDINATION.md). Each Git
transaction uses the common nonblocking writer lock. All generated files and
reviewer scratch go to `data/generated/trained_data_response/<run>/`.
Only the exact reviewed book addition and ancillary edits were authorized
for promotion on 2026-09-11; they are now incorporated. Startup HEAD was
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

The preparation-stage next action was promotion of the exact reviewed P1
text using P1I2 assembly after specific approval and source rechecking. That
action is now complete; the incorporation record below supersedes its pending
status. [prepare_promotion.py](prepare_promotion.py) only writes a fresh generated
draft; it cannot install into established files. The preparation verification in
`data/generated/trained_data_response/final_acceptance_01/verification.json`
checks every frozen packet/report hash, all declared live inputs, process
completion and identity, and the successful independent edition audit.
Scoped commits so far: `e111b63` (startup), `fed0567` (concurrent recovery),
`2c5cddb` (complete proofs and immutable R1 freeze),
`b922d12` (accepted R1 reviews and assembly preparation),
`fb2353c` (canonical P1 freeze and standalone verification),
`bb256d8` (accepted canonical science and corrected integration packaging).
Further commits use the common lock and explicit owned paths. Any required
scientific correction needs a new complete review round. The book was unchanged
at the preparation checkpoint; the later approved incorporation is recorded below.

## Independent milestone assessment — 2026-09-11

At the user's request, a separate coordinator checked the original milestone
contract against the complete unchanged P1 proof and dependencies, verified
the existing review hashes and completion evidence, and reran standalone
validation. Two new complete isolated audits, [A](ASSESSMENT_FRESH_A.md) and
[B](ASSESSMENT_FRESH_B.md), accepted with no required corrections. The
[full assessment](MILESTONE1_ASSESSMENT.md) records the evidence and concludes
that A–C accomplish milestone 1. Its [separate strategic challenge](ASSESSMENT_STRATEGY.md)
is advice, not an additional reviewed theorem. Fresh generated evidence is in
`data/generated/trained_data_response/assessment_root_20260911/` and the
separate reviewer namespaces documented in their reports.

The recommendation is to pursue nonlinear trained-law continuation and a
controlled finite-contamination remainder through time 40, with transport
continuity adequate for empirical laws. This is a proposed next research
target, not a completed consequence or authorization to start another campaign.
At the assessment checkpoint the scientific candidate remained unchanged and
promotion awaited explicit approval; the later approval and incorporation below
supersede that pending status. This assessment task owns only the four
assessment reports linked above and this README addition; concurrent
continuation, exporter and maintenance artifacts were preserved.

## Approved incorporation — 2026-09-11

The user approved the concrete package in the original research task:
"btw, I approve of promoting your result to the established part , make sure
you pass the gates specified in the research flow". This approval applies to
the unchanged P1 section and ancillary edits in [the proposal](PROMOTION_PROPOSAL.md),
using the reviewed P1I2 assembly. No new scientific scope was added.

The coordinator reread current AGENTS.md and both workflow parts, checked
HEAD/index/status, and reverified all frozen packets, reports, declared live
scientific/support hashes, reviewer launch prompts, event logs, distinct
instances and successful exits. Instructions had changed, but scientific inputs
had not. Part 2 step 3 explicitly permits reuse of completed reviews with
identical inputs and complete evidence; no new scientific review was needed.
Independent relevance, both canonical scientific reviews and the corrected
fresh integration review remain accepted with no unresolved required correction.
The optional attempt to delegate an additional evidence audit hit the agent
thread limit; that extra audit was not a required or claimed scientific gate.

Fresh assembly, pre-installation standalone validation, and post-installation
live correspondence/standalone validation all pass. The new
[CHECK_ESTABLISHED.py](CHECK_ESTABLISHED.py) checks the eleven declared live
book/support files against the reviewed final hashes, constructs a fresh
standalone edition and runs the unchanged reviewed validator. It was first
checked against the approved draft, then executed on the actual live files.
It writes only generated products and changes no maintained API. Reproduce:

```sh
python studies/trained_data_response/CHECK_ESTABLISHED.py --output data/generated/trained_data_response/NEW_RUN
```

The frozen pre-promotion builder retains its old-base hash requirements;
use this command for the incorporated edition. Checks cover exact candidate
correspondence, base restoration outside the accepted edits, guide links and
fragments, mathematical display structure, tangent/metric normalization,
singular-semigroup boundary cases and the exact rational reference certificate.
No training experiment was run. The unrelated PDF exporter was not modified.
The ordinary Git whitespace check reports one trailing space already present
in the immutable P1 section; its exact byte was retained to match the approved
edition. This is a formatting diagnostic, not an unresolved scientific or
integration-review correction. An initial metadata snapshot attempted to hash
an unreadable inherited maintenance file and failed; the successful snapshot
uses metadata only for other studies, without changing their files or permissions.

Final mapping and SHA256:

| Frozen input / operation | Established destination | Final SHA256 |
|---|---|---|
| P1_SECTION.md appended as C.4.6; one declared navigation replacement | docs/global_nonlinear.md | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| Two declared P1_ANCILLARY.md guide replacements | docs/README.md | `88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721` |

The incorporated section retains SHA256
`33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38`.
All other declared scientific and structural dependencies retain their reviewed
hashes. Exact approval, preflight, application and live check evidence are under
`data/generated/trained_data_response/promotion_20260911_01/`, particularly
`preflight.json`, `application.json`, `check_live/correspondence.json` and
`check_live/validation/validation.json`. Original review reports and failed runs
are preserved unchanged. The incorporation commit is
`1e293fdf26231d80b1f8a7170db5f3eaa5399732`, parent
`81447293842a9848509f546c2650194e5c86e806`, and changes exactly the two
established destinations above. Its lock/path/hash evidence is in
`incorporation_commit.json` in the same run. The separate study-record commit
contains this README, the updated proposal status and CHECK_ESTABLISHED.py.

This task has no remaining milestone-1 or promotion action. The separately
started P2 task's ownership is recorded above; its research is outside this
completed promotion, and no P2 conclusion is established here.

## Milestone 2 — complete and incorporated as C.4.7

**A–C are established through physical time 40** in
[C.4.7](../../docs/global_nonlinear.md#c47-nonlinear-training-near-the-fitted-tanh-reference).
The theorem gives a positive Wasserstein neighborhood among all bounded-label
Borel laws, strong population GF and reached restart, quantitative raw-state
and predictor continuity, actual finite capture with unrestricted empirical-law/
width rates, and a uniform nonlinear contamination remainder equal to P1's
response with the required width-first finite bridge. The exact model, Gaussian
action/adjoint and finite random readout are retained. The radius may be very
small; existing risk/activity consequences retain their exact admitted subclasses.

The complete [frozen section](P2_SECTION.md) and ten-input
[promotion packet](P2_PROMOTION_MANIFEST.json) are unchanged. Both fresh
complete canonical [review A](P2_CANONICAL_REVIEW_A.md) and
[review B](P2_CANONICAL_REVIEW_B.md) PASS without required corrections,
as does the separate [integration review](P2_INTEGRATION_REVIEW.md).
The independent [relevance assessment](P2_RELEVANCE.md), original
[full review A](P2_FULL_REVIEW_A.md) and [full review B](P2_FULL_REVIEW_B.md)
remain preserved with their exact inputs. The [historical checkpoint](P2_REPORT.md)
retains earlier conditional routes and failures.

The user explicitly [approved](P2_APPROVAL.md) the
[exact proposal](P2_PROPOSAL.md). Only C.4.7 and seven navigation replacements
were incorporated in docs/global_nonlinear.md and docs/README.md. Both live
files match the reviewed complete hashes. All frozen P1 inputs are unchanged;
the C.4.6 mathematical proof is retained with only the approved scope/navigation
sentences adjusted. No maintained code changed and no training was run.

Post-incorporation correspondence, exact reversal to every base byte,
complete dependency excerpts, affected links and all three deterministic
standalone checks PASS. Reproduce against this incorporated edition with:

```sh
python -B studies/trained_data_response/P2_CHECK_ESTABLISHED.py --output data/generated/trained_data_response/NEW_RUN
```

Use a fresh output path. The frozen pre-incorporation recipe remains evidence
for its original base; it intentionally rejects the changed live book.
Commands, hashes, original reports and commit evidence are in
[P2_RUN_RECORD.md](P2_RUN_RECORD.md). Fresh incorporation evidence is under
`data/generated/trained_data_response/p2_20260911_02/incorporation_check_01/`,
with `incorporation_commit.json` in the parent run. Earlier generated runs
remain intact. [Ownership](P2_COORDINATION.md) records the separate checker
scope and root as sole Git writer. **No milestone-2 or promotion work remains.**
