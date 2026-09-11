# Robust whole-circle prediction after substantial learning

Status: mandatory fixed-accuracy target resolved and exact user-approved P1
incorporated as [established C.4.5](../../docs/global_nonlinear.md#c45-robust-whole-circle-prediction-after-substantial-learning),
with its reviewed reading-guide update. Two fresh complete independent
scientific reviews and a separate integration review accepted the same bytes.
No required correction or necessary proof gap remains. Approval, unchanged-input
gate recheck, final hashes and integration evidence are recorded in
[PROMOTION_INTEGRATION.md](PROMOTION_INTEGRATION.md).
The theorem certifies `T=40`, `delta=exp(-exp(3000))`, whole-circle endpoint
error and both population/empirical risks at most `1/4`, plus early paired
activity of both layers. The radius is positive but extraordinarily small.
See [THEOREM.md](THEOREM.md) for exact probability, width, step and sample scope.

The exact reference is `nu_*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)`.
Perturbations are arbitrary probability laws on `sqrt(2)S^1 x {-1,+1}` with
joint transport cost `|x-x'|/sqrt(2)+|y-y'|`. No support, Gram or weight
restriction is allowed. Initial variances are `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and loss is the unhalved mean square. The finite initial readout is
retained. Full first rows and both directions of the actual middle Gaussian
action are retained in every comparison.

The global reference endpoint is the actual autonomous feature state stopped
at its unique first `b=1`, at feature time at most 10. Its whole-circle error
is at most `17 sqrt(10) exp(-t/5)`. The finite result holds in probability for
every fixed nearby law, deterministic empirical W1 approximations, widths
`n_k->infinity` and actual steps `eta_k sqrt(n_k)->0`, at the preceding node
to T. Independent iid samples of size tending to infinity obey the same joint
conclusion without relative sample/width restrictions. At `t_act=1/200`,
both training-averaged paired initial/current squared RMS activation
displacements exceed `1e-13` with probability tending to one.

The radius admits nonorthogonal, nonatomic and label-contaminated laws but is
impractical: `log10(log10(1/delta))` is approximately `1302.52`. The result
does not give global population dynamics/endpoints for perturbed laws, a
finite-width rate, useful risk for a uniform-circle teacher, or superiority
or causal necessity of feature learning.

| Proof component | Owner | Source |
|---|---|---|
| Reference fitting, endpoint and initial activity | `/root/reference` | [REFERENCE.md](REFERENCE.md) |
| Transformed reference source response | `/root/response` | [RESPONSE.md](RESPONSE.md) |
| Changed-law comparison, constants, finite algorithms and synthesis | `/root` | [TRANSFER.md](TRANSFER.md), [THEOREM.md](THEOREM.md) |

Owners write only their component files. The coordinator alone edits this
README and acts as Git writer under the common workflow lock. Fresh isolated
nonauthors `/root/scientific_p1_a` and `/root/scientific_p1_b` reviewed the same
complete frozen packet under [P1_SCIENTIFIC_ASSIGNMENT.md](P1_SCIENTIFIC_ASSIGNMENT.md).
Fresh `/root/integration_p1` separately reviewed the assembled edition under
[P1_INTEGRATION_ASSIGNMENT.md](P1_INTEGRATION_ASSIGNMENT.md).
Required corrections block acceptance. Established book/code edits require
separate approval of a concrete fully reviewed package.
Full original reports, hashes, complete read coverage, execution records,
isolation and coordinator verification are linked in
[P1_REVIEW_COMPLETION.md](P1_REVIEW_COMPLETION.md). All three verdicts are
ACCEPT with no required corrections; all reports were read completely.

Startup HEAD is `7441606` (incorporated C.4). The shared index was empty.
Concurrent exporter and repository-maintenance working changes were present
and remain outside this study. Current maintained C.4 and its P2 integration
record are authoritative; its completed local audit is not reopened.

The independent selector's [RELEVANCE.md](RELEVANCE.md) recommends a narrow
C.4.5 addition and guide update. The exact candidate, dependencies, scope edits
and hashes are in [P1_MANIFEST.json](P1_MANIFEST.json). The two maintained files
now match the reviewed editions exactly. The manifest SHA256 is
`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.

Reproduce the assembly and rational certificates with
`python studies/robust_learning_horizon/validate_candidate.py --inputs studies/robust_learning_horizon --output data/generated/robust_learning_horizon/NEW_RUN/edition`
from the checkout root, choosing a fresh run path. Author verification passed
both exact-arithmetic scripts; generated records are under `author_validation_01/`.
The final frozen manifest passed standalone validation under
`promotion_validation_02/` and independently in each reviewer's new directory.
[P1_VALIDATION.md](P1_VALIDATION.md) gives commands, actual outputs, hashes
and limits of those arithmetic/assembly checks. Independent mathematical
verdicts remain the separate full reports.

Source proofs and verification scripts belong here. Generated outputs and
scratch belong in `data/generated/robust_learning_horizon/<run>/`. Only
deterministic evaluation/verification of theoretical constants is authorized;
no training experiment or parameter campaign was run. Scoped progressive
commits are `7cf8c26` (startup/transfer), `5159004` (complete frozen P1), and
`0ecf050` (review completion/proposal). The promotion commit is recorded in
[PROMOTION_INTEGRATION.md](PROMOTION_INTEGRATION.md). Generated products remain
outside new Git commits. Promotion is complete; no further action is required
for this package. The later conversational frozen-feature comparison is outside
this reviewed addition. The original proposal and review records retain their
historical checkpoints unchanged.
