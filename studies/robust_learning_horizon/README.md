# Robust whole-circle prediction after substantial learning

Status: authored candidate complete; independent scientific and integration
reviews of frozen P1 are running. No affirmative acceptance or promotion yet.
The candidate certifies `T=40`, `delta=exp(-exp(3000))`, whole-circle endpoint
error and both population/empirical risks at most `1/4`, plus early paired
activity of both layers. The radius is positive but extraordinarily small.
See [THEOREM.md](THEOREM.md) for exact probability, width, step and sample scope.

The exact reference is `nu_*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)`.
Perturbations are arbitrary probability laws on `sqrt(2)S^1 x {-1,+1}` with
joint transport cost `|x-x'|/sqrt(2)+|y-y'|`. No support, Gram or weight
restriction is allowed. Initial variances are `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and loss is the unhalved mean square. The finite initial readout is
retained. Full first rows and both directions of the actual middle Gaussian
action must survive every comparison.

| Proof component | Owner | Source |
|---|---|---|
| Reference fitting, endpoint and initial activity | `/root/reference` | [REFERENCE.md](REFERENCE.md) |
| Transformed reference source response | `/root/response` | [RESPONSE.md](RESPONSE.md) |
| Changed-law comparison, constants, finite algorithms and synthesis | `/root` | [TRANSFER.md](TRANSFER.md), [THEOREM.md](THEOREM.md) |

Owners write only their component files. The coordinator alone edits this
README and acts as Git writer under the common workflow lock. Fresh isolated
nonauthors `/root/scientific_p1_a` and `/root/scientific_p1_b` review the same
complete frozen packet under [P1_SCIENTIFIC_ASSIGNMENT.md](P1_SCIENTIFIC_ASSIGNMENT.md).
Fresh `/root/integration_p1` separately reviews the assembled edition under
[P1_INTEGRATION_ASSIGNMENT.md](P1_INTEGRATION_ASSIGNMENT.md).
Required corrections block acceptance. Established book/code edits require
separate approval of a concrete fully reviewed package.

Startup HEAD is `7441606` (incorporated C.4). The shared index was empty.
Concurrent exporter and repository-maintenance working changes were present
and remain outside this study. Current maintained C.4 and its P2 integration
record are authoritative; its completed local audit is not reopened.

The independent selector's [RELEVANCE.md](RELEVANCE.md) recommends a narrow
C.4.5 addition and guide update. The exact candidate, dependencies, scope edits
and hashes are in [P1_MANIFEST.json](P1_MANIFEST.json). The maintained book is
unchanged. The manifest SHA256 is
`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.

Reproduce the assembly and rational certificates with
`python studies/robust_learning_horizon/validate_candidate.py --inputs studies/robust_learning_horizon --output data/generated/robust_learning_horizon/NEW_RUN/edition`
from the checkout root, choosing a fresh run path. Author verification passed
both exact-arithmetic scripts; generated records are under `author_validation_01/`.
Standalone assembly checks passed under `promotion_validation_01/`; the final
frozen manifest is rerun independently under `promotion_validation_02/` and by
each reviewer. These are arithmetic/assembly checks, not independent proof verdicts.

Source proofs and verification scripts belong here. Generated outputs and
scratch belong in `data/generated/robust_learning_horizon/<run>/`. Only
deterministic evaluation/verification of theoretical constants is authorized;
no training experiment or parameter campaign is planned. The next authorized
action is completion and adversarial verification of the exact scoped target,
or identification of a precise remaining mathematical gap.
