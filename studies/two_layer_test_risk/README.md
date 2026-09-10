# Two-hidden-layer feature learning and test-risk improvement at matched training loss

Started 2026-09-10. Current research record; study work only, not established material.
Scientific outcome: **bounded partial result; the risk sign remains open**.
The controlled cubic reduction is internally checked. The final quadrature
did not meet the declared convergence gate and does not certify a sign.
No existing study of this exact assignment was found by the initial README/content search.
Initial HEAD: `02af27154186dd3e45f83989a8ddf78e92ebceff`. Unrelated dirty paths are preserved.

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

Only approach A was used. The reserved second approach was not launched;
independent reconstruction/audits of A do not constitute a new route.
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

## Claims and checks

The exact moving-residual calculation is persisted in
[CUBIC_DERIVATION.md](CUBIC_DERIVATION.md). With `p=y/3`, initialized
`S=sum p_a H_a`, initial readout kernel `K`, and the fully specified cubic
predictor coefficient `J(x)` in that proof,

`f_t-g_t = J t^3 + O(t^4)`,
`tau(t)=t+beta t^3+O(t^4)`,
`beta=(p^T J_train)/(2 E S^2)>0`, and
`|Delta(t)-chi t^3| <= M t^4`, where
`chi=2 integral cos(3 alpha)[J(alpha)-beta g'_0(alpha)] d alpha/(2 pi)`.

The clock matching is proved uniquely on a positive local interval. The
cubic term is the first **possible** risk contribution: nonvanishing and
sign of `chi` are still open. The complete fourth-order remainder argument
is in [MATCHING_AND_REMAINDER.md](MATCHING_AND_REMAINDER.md). The constant
`M>=1` and positive interval are width-independent and not numerically
evaluated. [RESULT.md](RESULT.md) states the exact theorem, conditional sign
implication, hidden movement/nonaffinity bounds and remaining obligation.

Required source reading is complete for the coordinator; full coverage,
hashes and finite deterministic evidence are in
[SOURCE_AND_CHECKS.md](SOURCE_AND_CHECKS.md). The finite cubic identity,
kernel identity and matched-loss cancellation pass an independent
supplied-state check against the maintained moving-jet producer. This is
algebra verification only, not Gaussian or training evidence.

The prescribed quadrature checks give positive diagnostic coefficients
`0.0002932043404` (order 12), `0.0002776889548` (order 20) and
`0.0002730773235` (the conditionally authorized final order 28).
The final relative change is still about 1.69 percent. Numerical convergence
is therefore **inconclusive at the declared gate**, and there is no certified
integration error. All quadrature has stopped; positivity is not a theorem.
Details and full producer evidence are in [QUADRATURE.md](QUADRATURE.md).

| Claim | Type | Internal check | Promotion status |
|---|---|---|---|
| Unique matching, cubic coefficient and uniform fourth-order remainder | Proved local reduction | Complete; [independent adversarial report](INTERNAL_REVIEW.md) and coordinator reconstruction | Exact proof-only candidate passed separate reviews; awaiting user approval |
| Positive hidden movement and absolute nonaffinity | Existing C.3 specialized with explicit local scales | Hypotheses and expansions checked | Duplicate material stays in study |
| Positive or negative risk difference | Open | No rigorous coefficient sign or nonzero bound | Not eligible as a signed theorem |
| Positive quadrature values | Numerical diagnostic, inconclusive accuracy | Producer/identities and all saved rows checked | Excluded from candidate |

The coordinator read the full original internal review and verified its
frozen input/output hashes. Internal acceptance is not promotion review.
Independent [relevance selection](RELEVANCE.md) accepted a narrower C.4
appendix for assembly: the exact equal-loss expansion with unresolved sign,
plus one guide sentence. All numerical material stays in the study. The exact
[promotion proposal](PROMOTION_PROPOSAL.md) now passed both fresh complete
scientific reviews, [A](PROMOTION_REVIEW_A_V1.md) and
[B](PROMOTION_REVIEW_B_V1.md), and the separate fresh
[integration review](PROMOTION_INTEGRATION_V1.md). Each reports no required
corrections. The coordinator read all three original reports completely and
verified their provenance and frozen hashes. Standalone structural/link checks
passed; this is not a whole-book proof audit or code-library recertification.
The established book/code remain unchanged, pending approval of the exact
reviewed C.4 appendix and one guide sentence.

Reproduction instructions for the finite supplied-state identity are in
[SOURCE_AND_CHECKS.md](SOURCE_AND_CHECKS.md); the fixed, completed quadrature
budget and commands are in [QUADRATURE.md](QUADRATURE.md). The retained
assembler and independent integration-check source reproduce the proposed
edition and structural checks using the fresh-directory recipe in
[PROMOTION_PROPOSAL.md](PROMOTION_PROPOSAL.md). Generated evidence is preserved
under `data/generated/two_layer_test_risk/` and is excluded from commits.

## Ownership and next authorized action

The main task owns this README, synthesis, checks and the sole Git transaction.
Agent `cubic_derivation` owns `CUBIC_DERIVATION.md` and independently reconstructs
the jet and Gaussian response contraction. No agent may stage or commit.
Agent `matching_remainder` owns `MATCHING_AND_REMAINDER.md`.
Agent `quadrature_check` owns its producer and `QUADRATURE.md`.
Fresh `internal_adversary` owns the internal report; fresh `relevance_selector`
owns the independent placement report. `cubic_derivation` also assembles
`PROMOTION_C4.md`; all these authors/assemblers and the selector are excluded
from the paired isolated promotion reviews.
Fresh agents `promotion_review_a`, `promotion_review_b` and
`promotion_integration` each own their original assigned report only; all
three completed without reading prior verdicts or one another's findings.
The integration review's exact check source is also retained in the study.
Generated outputs go into fresh `data/generated/two_layer_test_risk/<run>/`.
Only owned study paths may be committed under the shared `pde-writer.lock`.
The bounded scientific calculation is complete at its unresolved scalar-sign
obligation; no further research or quadrature is running. The completed study
and exact reviewed proposal are retained together here. The next
external decision is user approval of that proposal. If approved, recheck live
dependencies and integrate only the reviewed addition under the shared lock;
changed scientific inputs require renewed reviews and approval. Do not restart
research or quadrature from this closeout note.
