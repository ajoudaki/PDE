# Robust whole-circle prediction after substantial learning

Status: active theoretical research; no result is yet accepted or proposed for
promotion. The mandatory target is a fixed useful learning time and an explicit
positive training-law radius for the C.4 two-hidden-layer tanh model, relative to
the orthogonal opposite-label reference. Whole-circle endpoint approximation,
population and empirical risk, actual simultaneous raw GD, and paired motion
of both hidden representations are separate proof obligations.

The exact reference is `nu_*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)`.
Perturbations are arbitrary probability laws on `sqrt(2)S^1 x {-1,+1}` with
joint transport cost `|x-x'|/sqrt(2)+|y-y'|`. No support, Gram or weight
restriction is allowed. Initial variances are `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, and loss is the unhalved mean square. The finite initial readout is
retained. Full first rows and both directions of the actual middle Gaussian
action must survive every comparison.

| Proof component | Owner | Current bottleneck |
|---|---|---|
| Reference fitting, endpoint and initial activity | `/root/reference` | Strong readout acceleration and explicit accuracy time |
| Transformed reference source response | `/root/response` | Named-source identities and quantitative tails through fitting |
| Changed-law comparison, constants, finite algorithms and synthesis | `/root` | Quantitative radius with strict deterministic margins |

Owners write only their component files. The coordinator alone edits this
README and acts as Git writer under the common workflow lock. Two fresh
isolated nonauthor reviewers will receive complete frozen inputs; their full
reports, assignments, hashes and completion evidence will be retained.
Required corrections block acceptance. Established book/code edits require
separate approval of a concrete fully reviewed package.

Startup HEAD is `7441606` (incorporated C.4). The shared index was empty.
Concurrent exporter and repository-maintenance working changes were present
and remain outside this study. Current maintained C.4 and its P2 integration
record are authoritative; its completed local audit is not reopened.

Source proofs and verification scripts belong here. Generated outputs and
scratch belong in `data/generated/robust_learning_horizon/<run>/`. Only
deterministic evaluation/verification of theoretical constants is authorized;
no training experiment or parameter campaign is planned. The next authorized
action is completion and adversarial verification of the exact scoped target,
or identification of a precise remaining mathematical gap.
