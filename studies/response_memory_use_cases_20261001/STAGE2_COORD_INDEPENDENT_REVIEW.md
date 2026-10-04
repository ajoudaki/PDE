# Independent internal review: temporal coordination

**Verdict: the exact identities, recorded numerical results, and rejection of
both registered positive claims are independently supported. Two minor precision
issues require clarification; neither changes those conclusions. This is an
internal review, not a promotion review or an endorsement of practical optimizer
superiority.**

Reviewed frozen manifest SHA256:
`44f42c0fa58dfeb0600a23d1cc55c06c83d4342aaabd9cadb9a64b5dd6fc0359`
(manifest timestamp `2026-10-02T12:21:33Z`). The complete independent input hash
inventory is `data/generated/response_memory_use_cases_20261001/stage2_coord_review01/input_hashes.json`.

## Scope and independence

I read the assigned coordination theory, protocols, result reports, both producer
versions, curriculum producer, checks and analyzers; inspected the relevant
canonical dense `Flow` implementation and manuscript Setting/history/memory
construction; and checked the data protocol/preparation code. I examined all
assigned generated runs, their source snapshots and manifests, and all 75 saved
endpoint archives. Snapshot differences preserve the original protocols and add
the declared reflection diagnostic, curriculum extension, and information-contract
clarifications; the registered thresholds are unchanged.

I did not consult other studies, author discussions, prior reviewer verdicts,
study history, or shared gate/index outcomes. The canonical-notation,
neural-response-memory, and rigorous-mathematics skills were applied. No author
input, paper, shared code, or Git state was edited. GPU coordination messages
concerned only availability and execution permissions.

## Findings requiring clarification

**P3: the controls called “isotropic” are spectrum matched but not generated
from Haar-distributed orthogonal matrices.** In
`stage2_coord_experiment.py:97–99`, the QR factors of Gaussian matrices are used
without correcting the diagonal signs of the triangular factors. With the
executed QR convention, an independent 1,000-draw, dimension-8 diagnostic had
`Q[0,0] < 0` in every draw, with mean `-0.2933576672`. A rotationally invariant
orthogonal matrix has a sign-symmetric first entry. Thus “QR-randomized
orientation, spectrum-matched control” describes the implemented control more
precisely. Both singular-value matching and the separate singular-mode sign
controls preserving both edit Grams are correct. The failed primary gates do
not depend on isotropy, so no positive conclusion is rescued or invalidated by
this issue.

For a future Haar control, if `G = Q R` is a Gaussian QR factorization, set
`Q_H = Q diag(sign(diag(R)))`. The corresponding triangular factor then has
positive diagonal. Gaussian left-orthogonal invariance and uniqueness of QR with
positive triangular diagonal imply left-orthogonal invariance of `Q_H`; zero
diagonal entries have probability zero. Preserve the executed controls and label
any such recalculation as an additional diagnostic.

**P3: specify which backward-history Gram is invariant.**
`STAGE2_COORD_THEORY.md:44–47` says that the backward history's Gram matrix is
unchanged under temporal permutation. Flatten each backward snapshot into a row
of a matrix `Y`, and write `P` for its temporal permutation matrix. The coordinate
Gram is invariant, `(P Y)^T(P Y) = Y^T Y`; the time-indexed Gram transforms as
`(P Y)(P Y)^T = P(Y Y^T)P^T` and is generally not unchanged entrywise. The
empirical distribution, moments, and retained snapshot structure claims are
correct. The implemented invariant test uses the invariant coordinate Gram.
This clarification does not affect any variance, reconstruction, or edit result.

## Mathematical audit

The experiment uses normalized input rows `u_a = x_a/sqrt(d)`, two tanh hidden
layers of width `n`, output `f_a = w^T h_a^(2)/n`, residual `r_a = f_a-y_a`, and
unhalved mean-square loss. First-layer, hidden-layer, and readout mobilities are
`(n,1,n)`. With `h_(a,i)=h_a^(1)` and
`b_(a,i)=r_a[w odot (1-(h_a^(2))^2)]`, the recorded Euler hidden update is

\[
\Delta W^{(2)}=-\frac{2\eta}{mn}\sum_{a,i}b_{a,i}h_{a,i}^{\top}.
\]

The centered decomposition and mean-only expectation follow by expanding the
temporal means and using the vanishing centered sums. A common permutation of
backward times preserves whole backward snapshots; applying that permutation to
both histories leaves the accumulated write unchanged. For centered snapshot
matrices `B_i,H_i`, the stated variance

\[
\mathbb E\left\|\sum_iB_{\pi(i)}H_i^{\top}\right\|_F^2
=\frac1{N-1}\sum_{i,j}\|B_jH_i^{\top}\|_F^2
\]

is correct for `N>=2`. In the expansion, coincident-time terms have coefficient
`1/N`, distinct-time terms have coefficient `-1/[N(N-1)]`, and the centered
forward sums turn the latter into another positive diagonal contribution.
For `N=1`, the centered expression is zero. The independent oracle enumerated
all `5!` permutations with unrelated, multi-sample, multi-neuron histories.

The physical-time basis
`psi_j(t)=sqrt((2j+1)/T) P_j(2t/T-1)` is orthonormal. Its coefficients are
normalized projection coefficients, not the manuscript's raw activity-clock
moments. Reflection multiplies the backward coefficient by `(-1)^j`; subtracting
the original update therefore gives

\[
E_q=\frac4{mn}\sum_{a,\ j<q\text{ odd}}D_{a,j}H_{a,j}^{\top}.
\]

Consequently order 1 has exactly zero reflection edit. Orthogonality eliminates
the cross terms between retained and discarded modes, and Cauchy–Schwarz bounds
the remaining outer-product integral by the stated product of odd-tail norms.
No smoothness assumption is required for these finite piecewise-constant
histories. Independent Gaussian quadrature, unrelated histories, both odd/even
orders, and the product bounds all agree with the implementation.

For weighted loss `sum_a lambda_a r_a^2`, the correct recorded history is
`b_a=m lambda_a r_a delta_a^(2)`. The common factor `-2/(mn)` then reproduces
the hidden gradient, and both outer blocks use the same weights. Independent
autograd checks verified all three mobilities with unequal groups and zero
inactive weights. Every schedule gives each example integrated weight
`T/(2m_group)`; this is exposure equality, not equality of trajectories.

For equal temporal halves, subtracting original pairings from swapped pairings
gives

\[
E_{\rm swap}=\frac2{mn}\sum_a\int_0^{T/2}
(b_{a,A}-b_{a,B})(h_{a,A}-h_{a,B})^{\top}\,ds.
\]

Its projected formula and product-tail bound are correct. The constant-mode
coefficients are `sqrt(T/2)` times the phase-mean differences, so the phasewise
order-1 swap can be nonzero. This distinction from single-interval reflection
is essential and is handled correctly. The centered residual edit need not
itself be a history permutation, as the reports acknowledge.

The smooth-loss first-order/remainder identity is correct. Gradient projection
and ordinary curvature remain competing explanations for endpoint sensitivity;
the algebra does not establish a unique temporal mechanism.

## Independent numerical verification

All frozen source hashes, seven producer manifests, archive completion hashes,
dataset hashes, and retained raw-source checksums matched. Producer records
account for 150 solves: 96 in the original campaign, including its 60 short
continuations, and 54 in the declared curriculum extension.

The reviewer script rebuilt every saved endpoint test prediction directly from
the stored first layer, hidden matrix, readout, and input arrays, without calling
the producer's prediction/scoring functions. Across **75 archives and 873 saved
edit predictions**, the largest prediction RMS discrepancy was
`3.2614e-16`; the largest MSE discrepancy was `2.2204e-16`. Per-case JSONs matched
their aggregate result files. Coefficient reconstructions agreed with stored
edits. Independent small algebra/autograd/quadrature oracles had maximum error
`1.6454e-15`.

The following registered statistics were recomputed from the underlying
per-case evidence, not copied from the reports:

| Fixed support | Median reversal MSE change | Median excess over sign controls | Damaging seeds |
|---|---:|---:|---:|
| Fashion | -0.498032% | -0.808884% | 0/4 |
| Housing | +0.238258% | -0.206357% | 4/4 |
| HAR | -3.312216% | -16.947290% | 0/4 |

No domain reaches the registered 10% damage threshold, and each domain's
median excess over the stronger sign controls is negative. The negative
cross-domain result is unambiguous within this design.

| Curriculum | Median registered F | Median centered damage | Median phasewise order-1 loss ratio |
|---|---:|---:|---:|
| Fashion | -0.2191075 | +0.0805973 | 1.784195 |
| Housing | -0.0271304 | +0.0218864 | 1.084776 |
| HAR | +0.0436760 | -0.0446605 | 2.331918 |

Fashion and Housing have negative `F` in all four seeds; HAR has two positive
and two negative values. Every domain fails the phase-mean gate. Thus neither
mean-dominated effects nor the residual surgery support the registered positive
higher-order claim.

Independent reflection reconstruction and step-refinement calculations agree
with both analysis summaries to maximum absolute discrepancy `1.2490e-16`.
Across the 48 curriculum fits, maximum relative swap-edit errors are
`0.0459484` at order 8 and `0.00992432` at order 16; restricting to AB/BA gives
order-16 maximum `0.001004216`. Fixed-support half-step baseline prediction
discrepancies are `0.000340813`, `0.0000436194`, and `0.000119764` for Fashion,
Housing, and HAR. All three signed reversal effects exceed twice their
refinement change. Curriculum joint/AB refinement also reproduces; BA was not
refined and the full difference-in-differences is not uniformly certified in
step size. The reports retain that limitation.

**Fresh full replay:** one Fashion, seed 3401, AB trajectory on GPU1, using an
independently written row-oriented forward pass, autograd for all updates, and
streamed phase-difference moments integrated by independent Gaussian quadrature.
It used the original width 256, 512 training examples, horizon 64, and step 1/16.
There were no continuation fits. Relative parameter discrepancies were at most
`2.399e-16`, exact swap-edit discrepancy `3.496e-14`, and test prediction RMS
discrepancy `1.965e-16`. This checks the weighted model and observer together,
including passive features of inactive examples. It consumed one full fit and
2.651 seconds inside the replay function, within the assigned two-fit/five-GPU-
minute ceiling. The CPU audit and supplementary calculations consumed 37.164
and 13.373 seconds respectively, excluding interpreter startup; small additional
hash/read checks remain far below the five-CPU-minute allocation.

## Interpretation and remaining limits

The defensible positive contribution is an exact family of temporal weight
interventions with accurate compressed representations of observed histories.
The evidence rejects the two prescribed useful-chronology hypotheses. It does
not reject every conceivable task, schedule, or temporal-memory algorithm.

The practical restrictions in the result reports are substantive: all 512 union
inputs remain available and are queried even when their current gradient weight
is zero; this is not replay-free continual learning. Endpoint surgery retains
the outer parameters of the original trajectory and is not ordinary GD on
permuted time. The separately declared block-edit optimizer is causal, but its
future marginals are free to change and it has only one seed per domain.
Phasewise means, balanced-gradient corrections, recency effects, and overfitting
remain viable simpler explanations. The full target preprocessing uses the
root-designated 1,024-example training pool, including its housing target
normalization; the experiments do not establish a strict 512-label information
budget.

Four seeds replicate initialization on one fixed data split, not population
sampling. Full stepwise histories were transient working data rather than saved
archives; all saved predictions/edits were checked, and one entire trajectory
was independently replayed, but every trajectory was not independently rerun.
Theoretical identities cover arbitrary eligible histories; empirical favorable
generalization and autonomous closure fidelity do not follow. The coefficient
storage can exceed one dense matrix at this sample count, and no practical
total-memory or runtime saving was benchmarked.

## Reproduction and release

From the repository root, the reviewer commands are:

```text
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_coord_review.py --out data/generated/response_memory_use_cases_20261001/stage2_coord_review01
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_coord_review.py --out data/generated/response_memory_use_cases_20261001/stage2_coord_review01 --replay --device cuda:1
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_coord_review.py --out data/generated/response_memory_use_cases_20261001/stage2_coord_review01 --supplement
```

The replay requires host GPU access because the sandbox hides GPU device files.
No network retrieval was used. `completion.json`, `oracles.json`, `raw_audit.json`,
`replay.json`, and `supplementary.json` retain the measurements. The initial
review-script snapshot and its later supplementary extension are both preserved
in the generated review directory; the initial command's source hash therefore
remains reproducible. `review_release.json` records the final report/source
hashes and input-manifest recheck. No original input was changed to resolve the
two findings above.
