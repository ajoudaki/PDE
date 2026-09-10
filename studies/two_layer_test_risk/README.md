# Two-hidden-layer feature learning and test-risk improvement at matched training loss

Started 2026-09-10. This is the single current research record.
**Scientific status: complete, internally checked positive finite-time comparison.**
Both fresh complete scientific audits accepted the signed theorem with no
required corrections. This is a study result; established book/code are unchanged.
No existing study of this exact assignment was found at startup. Initial HEAD
was `02af27154186dd3e45f83989a8ddf78e92ebceff`; the first phase was committed as
`df1117948764a984e7fd2d28949a3c87bc284f84`. Unrelated shared-checkout work is preserved.

## Answer and exact scope

For the fixed model below, learning both hidden layers gives strictly lower
uniform-circle test risk than freezing them, **at the same training loss**, for
all sufficiently small positive physical times. The unique matching clock and
actual-flow remainder were already proved; the continuation resolved the
previously open sign by a complete deterministic arithmetic certificate:

`27/100000 < chi < 273/1000000`,
`35309/1000000 < beta < 35311/1000000`, and
`|Delta(t)-chi t^3| <= M t^4` on `[0,T]`.

Consequently, with `t0=min(T,27/(200000M))`,
`Delta(t) >= (27/200000)t^3 > 0` for `0<t<=t0`.
The cubic term is now proved to be the first nonzero contribution.
The complete statement and signed proof are in [SIGN_THEOREM.md](SIGN_THEOREM.md).
Its initial pending-audit preface records its frozen version; the audit
condition is now satisfied by the original reports linked below.

The benefit is small: its leading term is about `0.000272 t^3`, against
initial test risk `1/2`. The width-independent positive interval exists, but
`T`, `M`, and `t0` are not numerically evaluated. This proves no practically
substantial gain, later-time dominance, universal feature-learning benefit,
iid-average risk/sample-complexity theorem, or growing-design/depth limit.
Finite GF and every deterministic vanishing raw-GD step inherit the sign in
probability on each fixed `[delta,t0]`, `delta>0`, with the actual common small
random readout retained. There is no width rate or finite-width sign claim
uniformly down to zero. Hidden activation and preactivation movement begins
at nonzero order `t^2`; the local absolute nonaffinity bounds in
[RESULT.md](RESULT.md) remain at their original scope.

## Evidence and independent checks

The full exact coefficient retains the moving residual, all trained blocks,
and both directions and response means of the reused connector; see
[CUBIC_DERIVATION.md](CUBIC_DERIVATION.md). Unique matching and the actual
uniform fourth-order remainder are proved in
[MATCHING_AND_REMAINDER.md](MATCHING_AND_REMAINDER.md). Passive-circle capture
is a supporting corollary of the established population theorem, not a new
population-existence achievement.

The new certificate's complete components are
[CERTIFIED_ERROR.md](CERTIFIED_ERROR.md),
[CERTIFICATION_ENGINE.md](CERTIFICATION_ENGINE.md),
[ANGULAR_CERTIFICATE.md](ANGULAR_CERTIFICATE.md), and
[DRIVER_CERTIFICATION.md](DRIVER_CERTIFICATION.md). They bound Gaussian
integration and tails, covariance/root errors including singular cases,
elementary arithmetic and summation, labels/input constants, rational
interval propagation, and the whole-circle rule. No statistical confidence
level or numerical convergence heuristic decides the sign.

The primary target-26 run and sole reserved fresh reproduction both exited
zero, taking respectively 31.18 and 30.67 CPU seconds. Each used 64 evaluations
of the exact symmetry-reduced 256-angle rule and 86,101,134 upper Gaussian
nodes. Their final rational certificate and all 322 invariant input/output
files agree byte for byte. The enclosing chi interval is approximately
`[0.00027054037037366814,0.00027259851133052906]`, entirely positive after
all error charges. Raw data and provenance are in fresh runs
`certificate_20260910_01/` and `certificate_reproduction_20260910_01/` under
`data/generated/two_layer_test_risk/`.

Component audits [angular](ANGULAR_REVIEW.md), [kernel](KERNEL_REVIEW.md),
and [driver](DRIVER_REVIEW.md) passed. A preflight interval-efficiency bug
was fixed before any coefficient execution and its adverse evidence retained.
The two fresh complete final audits are [A](SIGN_REVIEW_A_V1.md) and
[B](SIGN_REVIEW_B_V1.md). Both read the complete proof/dependency/code packet;
A performed the reserved fresh full reproduction. Each separately rebuilt
all 64 enclosures using its own rational interval implementation of the full
four-slot Gaussian contraction, and independently proved the positive bound.
Their checker corrections and limitations are preserved in the original
reports. The coordinator read both reports completely and verified all 625
frozen hashes, report provenance and exact rational sign comparisons.

[SOURCE_AND_CHECKS.md](SOURCE_AND_CHECKS.md) records complete source-reading
coverage, hashes, commands and verification evidence. Generated results are
reproducible from retained sources, never committed as unique proof source.

## Approaches, adverse findings and supersession

The user explicitly asked to continue until the comparison was completely
resolved. That reopened the old scalar-sign stop without changing the fixed
model, local-time scope, or prohibition on training/witness searches.
Exactly two analytic approaches were used:

| Approach | Outcome |
|---|---|
| A: moving-flow expansion and analytic structure | Complete coefficient, unique matching and remainder. Structural symmetry/matching identities alone did not establish a sign; adverse and useful identities are retained in [SIGN_STRUCTURE.md](SIGN_STRUCTURE.md). |
| B: certified deterministic integration | Strict positive coefficient proved with full analytic/arithmetic error enclosure and one fresh identical reproduction. |

The earlier Gauss--Hermite orders 12/20/28 gave positive diagnostics but the
last 1.69 percent change failed their declared convergence gate. They remain
inconclusive diagnostics in [QUADRATURE.md](QUADRATURE.md). The new proof
does not retrospectively certify those arrays. Old open-sign statements in
RESULT and the original proof-only promotion documents describe that earlier
version; the signed theorem and this current record supersede that obligation.
No third approach, new teacher/design, training, GPU work or further full
coefficient run is authorized or needed.

## Frozen contract

Exactly two hidden layers, both tanh, scalar linear readout, no biases:
`z1=W1 x/sqrt(2)`, `z2=W2 tanh(z1)`, `f=W3^T tanh(z2)/n`.
Independent initialization variances are respectively `1`, `1/n`, `1/n^2`
for the stored weights. All blocks train with mobilities `(n,1,n)` under
`L=(1/3) sum_a (f(x_a)-y_a)^2`; residual always means `f-y`.
Dimension is two; the three training angles are `0, pi/5, -pi/5`,
`x(alpha)=sqrt(2)(cos(alpha),sin(alpha))`, and labels are
`1,(1-sqrt(5))/4,(1-sqrt(5))/4`. The correlated rank-two input Gram is retained.
Test risk is the uniform whole-circle integral of squared error against
`cos(3 alpha)`. This is fixed-design prediction, not an iid/sample-complexity claim.

Compare the actual population predictor `f_t` with `g_s`, which freezes both
initial hidden layers and trains the readout with the same normalization.
Its limiting initial readout is zero, so its kernel equals the full initial
tangent kernel. Finite-network statements must retain the actual random
small readout. Matching must be proved: `L(g_tau(t))=L(f_t)`, `tau(0)=0`.
The observable is `Delta(t)=R(g_tau(t))-R(f_t)`.

Use only a positive physical-time interval inside the established C.1--C.3
theorem of `docs/global_nonlinear.md`. That theorem is a foundation, not an
open problem here. No global continuation, growing depth/dimension/sample
count, training runs, GPU work, parameter sweeps, or search for another witness.
No quantitative width rate may be invented. Passive-input capture is a
supporting corollary only. At most two analytic approaches are allowed.

## Promotion and remaining authorized work

Independent [signed-result relevance selection](SIGN_RELEVANCE.md) accepts
narrow assembly: one signed C.4 with its full certificate proof, an opt-in
self-contained fixed-certificate command, focused tests and minimal guide
updates. The scientific result is complete independently of this packaging.
The complete canonical edition and tool are frozen and all promotion gates
before user approval have passed. The concrete nine-file addition is in
[SIGNED_PROMOTION_PROPOSAL.md](SIGNED_PROMOTION_PROPOSAL.md), with the full
[C.4 proof](PROMOTION_SIGN_C4_V2.md) and [tool guide](PROMOTION_TOOL_GUIDE.md).
Two fresh isolated complete scientific reviews
[A](SIGNED_PROMOTION_REVIEW_A_V1.md) and
[B](SIGNED_PROMOTION_REVIEW_B_V1.md), and the separate fresh
[integration review](SIGNED_PROMOTION_INTEGRATION_V1.md), accepted exactly
the frozen edition with no required corrections. The coordinator read every
full report and verified all 1,194 frozen payload hashes and current sources.
These reviews used no prior verdict as a premise and ran no third coefficient
integration. They independently checked the unchanged numerical core,
both complete saved runs, standalone interfaces and focused tests; each
scientific reviewer also rebuilt the full four-slot contraction independently.
The old [proof-only proposal](PROMOTION_PROPOSAL.md) and its passing reviews
cover only their earlier unsigned scope and are superseded as a recommendation.
They are preserved unchanged and are not reused to accept the signed edition.

Root owns this README, synthesis, source checks, canonical theory assembly
and the sole Git transaction. Original authors own their named proof/code
sources. `sign_code_assembly` owns only the new candidate tool/guide/checks.
All scientific reviewers and the selector own their original assigned reports
and separate scratch; none may stage or commit. Only explicit owned study
paths will be committed under the common nonblocking `pde-writer.lock`.

Research is closed with the positive theorem; there is no unresolved
coefficient or remainder obligation. Final integrity checks passed; the
study-only Git transaction evidence is retained under
`data/generated/two_layer_test_risk/signed_commit_20260910_01/`.
The only next step is user approval of the exact reviewed
promotion proposal, followed by dependency rechecking and integration under
workflow Part 2. Do not run further coefficient calculations or change live
established book/code before that approval.

## Preserved calculation contracts

The following pre-execution specifications are retained with their original
limits. Both permitted certificate runs are now complete.

### Preregistered certificate calculation

The second approach now has complete analytic Gaussian-tail/strip and
covariance-error bounds in `CERTIFIED_ERROR.md`, plus the independent circle
bound in `ANGULAR_CERTIFICATE.md`. Exact rational derivative arithmetic gave
an angle error below `1.62e-7` (fresh `angle_bound_20260910_01`); the executing
certificate conservatively charges `1e-6`, conditional on verifying
`|beta|<=1/10`. This small scalar majorant check is not a coefficient run.

Before executing a new coefficient calculation, freeze: the exact original
model; 256-angle periodic rule reduced by exact symmetry to 64 evaluations;
Gaussian tensor trapezoid with root radius at least eight; strip exponent
target B=26, all root spacings dyadic, chosen from the certified column
bounds alone; and exact rational interval propagation through every moment,
covariance perturbation, matrix response and clock division. Elementary
functions in the bulk are polynomial/rational evaluations with proved
rounding bounds. The certificate must verify all declared numeric contracts
and a strictly positive denominator; no empirical convergence test substitutes.

Primary outcome is the complete enclosing interval for chi: lower endpoint
positive proves benefit, upper endpoint negative proves disadvantage, and
an interval containing zero is inconclusive. The second run is reserved
either for independent fresh reproduction if the first valid interval
excludes zero, or for B=30 refinement if the first valid interval contains
zero and Gaussian integration error is the removable bottleneck. All other
scientific settings remain unchanged.
At most two full coefficient runs, at most fifteen CPU minutes per run and
thirty CPU minutes total, on CPU with one calculation process at a time.
No random seeds, sampling, training or data/teacher search. Each run goes in
a fresh generated directory and retains inputs, bit-exact primitive output,
source hashes, environment, limits, errors and exit status. Source failures
are preserved; fixing a demonstrated implementation bug is not evidence of
the coefficient's sign. Small deterministic primitive and contraction tests
are separate verification, capped at one CPU minute each.

## First decisive calculation and bounded plan

Approach A: the moving-residual physical-flow jet. With `K0` the initial
readout kernel and `c=2/3`, both predictions start with
`f'_0(x)=g'_0(x)=c sum_a K0(x,x_a)y_a`. Hidden velocities vanish at zero
population readout. Derive the first hidden-induced predictor term, then
subtract the part removed by training-loss time matching before testing its
whole-circle teacher projection. A changing kernel or positive feature speed
alone will not count as a risk result. The first calculation to resolve is
the matched coefficient, including the moving residual and both directions
of the same connector operator. Its order/sign are not assumed.

In the first completed phase, only approach A was used. The second approach
was reserved then and was launched only after the user reopened the study.
Independent reconstruction/audits do not constitute another analytic route.
Stop with either a complete locally uniform sign/remainder theorem or an
explicit unresolved coefficient/remainder obligation. Preserve adverse findings.
Small deterministic algebra or quadrature checks may be used only after
their precise scope, fixed resolutions and stopping rule are recorded here.

### Deterministic verification contract (before execution)

The moving-flow calculation identifies a candidate cubic matched-risk coefficient.
Verify its algebra on one fixed small deterministic matrix state using the
maintained finite-jet recurrence (no trajectory integration), and verify its
Gaussian contraction identities by deterministic quadrature. The population
coefficient will use exactly the fixed teacher/data above, full Gaussian
response means, and all three trained blocks. Numerical sign is diagnostic
only: without certified integration error it cannot establish a sign theorem.
Quadrature budget: tensor Gauss--Hermite orders 12 and 20 with respectively
64 and 128 equally spaced circle angles; one final order-28/128-angle
resolution check is permitted only if the two values differ by more than
1 percent relative or disagree in sign. No further resolutions or witness
changes. Record absolute/relative differences, training contraction identity,
symmetry error and covariance eigenvalues. An identity error exceeding
1e-9 relative to max(1,scale) invalidates algebraic interpretation; unconverged
quadrature remains inconclusive. Cap each calculation at five CPU minutes
and the full verification at fifteen CPU minutes; no GPU or random sampling.
Use fresh run paths, preserve code/hashes, environment and full output.
