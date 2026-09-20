# Isolated mathematical review: rate-adapted readout perturbations

2026-09-19. Internal theoretical review, not a promotion review.

**Verdict: the principal mathematical result passes. One minor scope correction is required for the optional-refresh sentence at candidate line 326.** The fixed-duration hidden-tube construction, exact noise covariance, state-independent success probability, dimension-polynomial proposal bounds, elapsed-clock bounds, and strong full-state endpoint are valid. No fitted-target oracle, stopped hidden gradient, vanishing state metric, or uncounted rejection time is needed for these conclusions under their declared algorithm and clock. They do not establish the same rates for unmodified gradient flow, ordinary additive noise, minibatch noise, or a numerical population implementation.

## 1. Assignment, isolation, and read coverage

The reviewer is the fresh scoped agent `/root/review_readout_rate`, distinct from the candidate author. The assignment was to review the frozen candidate and its supplied dependencies, check all-time confinement, covariance, success probabilities, rates, endpoint claims, initialization orders, and possible hidden oracle/clock/metric assumptions; perform theory only; and write only this report. The reviewed candidate was not edited. No experiment, discretization, or numerical integration was performed.

The permitted scientific input was the candidate `RATE_ADAPTED_READOUT.md`, its supplied in-study dependencies `ESCAPE_AND_LIMITS.md`, `INITIAL_EXCLUSION.md`, `INITIAL_REVIEW.md`, `NOISE_GLOBAL_PROGRESS.md`, the canonical ranges 13161–13786 and 15146–15528 of `docs/global_nonlinear.md`, and `docs/NOTATION.md`. No study README, other study, other route candidate, other review, history, or external scientific source was consulted. Git status was inspected only as coordination metadata before writing; no Git mutation was performed.

Actual scientific reading was complete for all five supplied study files: candidate lines 1–355; `ESCAPE_AND_LIMITS.md` lines 1–345; `INITIAL_EXCLUSION.md` lines 1–401; `INITIAL_REVIEW.md` lines 1–142; and `NOISE_GLOBAL_PROGRESS.md` lines 1–328. The notation contract was read completely, lines 1–98. Both assigned canonical ranges were read completely, including their proof bodies. An initially truncated combined display was repaired by dedicated rereads, including the last seven lines of `INITIAL_EXCLUSION.md`. No scientific content outside those scopes was retrieved. Sections outside a dependency's cited proof body were read for context but are not independently certified wholesale by this report.

The supplied `INITIAL_REVIEW.md` was an explicitly authorized proof dependency for its order-one extension. Its prior verdict was therefore visible; this report does not claim blindness to that supplied dependency's verdict. The extension was rechecked directly against the canonical odd-block definitions and the positivity argument, rather than accepted from its verdict. No earlier review of the current rate candidate was supplied or read.

Required process sources read: `AGENTS.md`, `RESEARCH_WORKFLOW.md`, and the complete `/etc/codex/skills/solve-math-rigorously/SKILL.md`. The scientific audit used direct algebra, deterministic continuation estimates, Gaussian probability inequalities, and summability arguments. No additional external theorem is required.

## 2. Necessary scope correction

Candidate Section 1 states compatibility of label signs but does not explicitly impose binary labels. Its referenced `ESCAPE_AND_LIMITS.md` Section 1 also allows general finite real labels. At candidate line 326, keeping the initialized readout `c=0` does preserve every zero prediction, but its loss is

\[
L_0=\sum_i\mu_i y_i^2,
\]

which equals one for binary labels, not for every compatible real-label dataset. For example, one observation of label 2 is compatible and has loss 4 at `c=0`.

Correct line 326 to say “Keeping `c=0` preserves every initialized prediction and the initial loss \(L_0=\sum_i\mu_i y_i^2\) (equal to one for binary labels).” Alternatively, explicitly declare `y_i in {-1,1}` in Section 1. The first repair preserves the stronger scope already supported by the argument. No constant or rate formula otherwise changes: all use the actual `L0`. If all labels vanish, the initialized state is already fitted and the stated terminal convention applies.

This is a normalization/scope defect, not a defect in the positive-Gram theorem, the refresh construction, or any displayed rate.

## 3. Exact model, metric, and deterministic confinement

The closure equations agree with (H3.N2), (H3.CS2), and (H40.C6). The population spaces stay fixed, the transpose is the actual matrix transpose, and the velocities are gradients in the fixed population `L2`/Frobenius metric for the unhalved weighted loss. The input reduction is exact: oddness gives `f(-u)=-f(u)` at every state, so compatible duplicate or antipodal terms combine into one weighted square. Equality of the loss functionals on the whole Hilbert state space also gives equality of their gradients.

The whole-Hilbert local-Lipschitz and continuation proof in `ESCAPE_AND_LIMITS.md` Section 1 is sufficient here. In particular, finite-dimensional `a_i` is Lipschitz in `w`, bounded `b2` turns its preactivations and gate variations into `L-infinity` quantities, and these multiply the `L2` readout without a regularity loss. The first-layer gate is Lipschitz into `L2` and multiplies a bounded `q_i`. The loss is `C1`, with locally Lipschitz gradient; the argument does not need the generally unavailable `C2` Nemytskii regularity on `L2`. Energy and successive speed bounds continue each segment for every finite time from every finite Hilbert state.

Writing \(T=A^*K^{-1}\), whenever \(K\ge\kappa I\),

\[
T^*T=K^{-1}AA^*K^{-1}=K^{-1},\qquad
\|T\|\le\kappa^{-1/2}.
\]

The operator perturbation estimate in candidate (5) is valid because both `A` and `A0` have norm at most one and

\[
\|AA^*-A_0A_0^*\|
\le (\|A\|+\|A_0\|)\|A-A_0\|.
\]

The radius `rho` therefore preserves `K >= kappa0/2`, including at a hypothetical first boundary point. A kick does not change this Gram because the hidden fields alone determine it.

An accepted kick satisfies \(|Z|\le1+\sqrt\theta\), hence its readout norm is at most \((1+\sqrt\theta)\sqrt{\ell_j/\kappa}\). Since \(\ell_j\le\theta^jL_0\), the sum of these bounds is finite. On the following flow segment, loss is at most \(\theta\ell_j\). Thus the cumulative readout flow travel is at most \(2h\sqrt\theta R_*\), and `h<=1` gives exactly the declared `Cbar`. Within the hidden tube, the cumulative hidden travel is bounded by

\[
2Bh\overline C(1+\overline M)\sqrt\theta R_*\le\rho/2.
\]

Every term in the denominator defining `h` is finite and strictly positive: `L0>0`, `0<theta<1`, `kappa0>0`, and the positive readout-travel contribution makes `Cbar>0`. The first-exit contradiction is consequently noncircular. It uses only past accepted steps and a partial current flow segment; it does not assume that a future trial succeeds. Induction supplies every finite accepted history. Unbounded rejected candidates are immaterial because they are never installed as states.

This proves a deterministic restriction on the actual hidden path, with the original hidden velocities retained during every full-GF interval. It is an imposed small-total-travel regime, but not a frozen-hidden substitution. The original metric remains fixed throughout; no rescaled or degenerating metric is used to claim convergence.

## 4. Covariance, success probability, and the dimension bound

Conditioning on the current state, the proposal is centered Gaussian in the current feature span with covariance

\[
\operatorname{Cov}(\delta c\mid S)
=\ell\sigma^2A^*K^{-2}A.
\]

Its exact prediction effect is \(A\delta c=\sqrt\ell Z\). Thus acceptance is precisely \(|e/\sqrt\ell+Z|^2\le\theta\). The normalized residual is a unit vector. Rotational invariance makes its conditional success probability equal to candidate (10), independently of residual orientation, data conditioning, and stage. The ball involved has positive radius, so its Gaussian probability is strictly positive.

The rotation is solely a proof device. The algorithm neither rotates a proposal toward `-e` nor supplies a fitted readout. It uses the current feature map and its Gram inverse, which provide an exact right inverse on prediction space, and the scalar current loss. This is substantial exact linear-algebra/population-expectation information, explicitly admitted by the candidate; it is not knowledge of a future endpoint or a label-fitted target.

For the proposed dimension-dependent scale, the event

\[
-2\le G_1\le-1,\qquad \sum_{j=2}^mG_j^2\le2(m-1)
\]

has probability at least \(e^{-2}/(2\sqrt{2\pi})\). The coordinate event has probability at least its interval length times the minimum Gaussian density there. For `m>1`, Markov's inequality gives probability at least one half for the independent remaining-coordinate event; for `m=1` that event holds surely. On this event,

\[
2\sigma G_1\le-\frac1{2m},\qquad
\sigma^2|G|^2\le\frac{2m+2}{16m^2}
\le\frac1{4m},
\]

where the last inequality is equivalent to `m>=1`. This proves `q>=q_*` uniformly, including the boundary case `m=1`. The Gaussian remains centered and isotropic in weighted prediction coordinates. No input-separation constant enters this probability estimate.

Nevertheless, neither physical kick sizes nor the chosen GF interval are uniformly geometry independent: the inverse Gram and `kappa0` appear explicitly. No small physical-noise or computational-efficiency guarantee follows from the uniform probability alone, as candidate lines 270–273 acknowledge.

## 5. Unconditional proposal, endpoint, and elapsed-time conclusions

Given the full past before each trial, its success probability is the same `q`. Applying conditional expectation successively to any finite pattern of success/failure events gives the Bernoulli product law. In particular, the geometric waiting times are independent with mean `1/q`. An exact fit at a positive-loss Gaussian proposal requires a single value of `Z` and has probability zero. A locally Lipschitz autonomous flow cannot first reach a zero-loss equilibrium in finite time: local uniqueness run backward from that equilibrium makes a solution reaching it constant on a preceding interval. Thus termination causes no hidden change to the Bernoulli argument; the candidate's fictitious-indicator convention also covers it.

If `B_k` is the number of successes among the first `k` trials and `L_k` is measured after each possible following GF segment, then pathwise

\[
L_k\le L_0\theta^{B_k}.
\]

The Bernoulli generating function gives \(E L_k\le L_0(1-q+q\theta)^k\), exactly (11). This expectation is unconditional because the Gram tube is deterministic. Waiting for `J_epsilon` successes gives the mean bound `J_epsilon/q`; Markov's inequality gives (12). The estimate

\[
-\log(1-1/(4m))\ge1/(4m)
\]

then gives `J_epsilon <= 1+4m log(L0/epsilon)`, so (14) is valid. The exponentially summable exceptional-event estimate proves the stated eventual almost-sure proposal rate for every fixed `a<q(1-theta)`.

There are infinitely many successes almost surely unless fitting terminated the process, since each geometric wait is finite almost surely and a countable intersection preserves this event. Summability of all accepted readout jumps and all flow travel makes the sequence, and its intervening actual-state path, Cauchy in the complete fixed Hilbert state space. It has a finite strong limit. Continuity of the finite-data loss and `ell_j<=theta^j L0` give zero loss at that limit. This conclusion does not infer compactness from boundedness and does not discard neutral readout coordinates; total travel controls them directly. The same estimates cover the state while waiting on rejected proposals because it is then constant.

Under the declared elapsed clock, each complete trial with its optional GF segment takes at most `Delta+h`. Therefore at least `floor(t/(Delta+h))` complete trials have occurred by time `t`, unless the already-fitted state has terminated the process, in which case all bounds are immediate. Monotonicity of actual-state loss gives (15) even when `t` falls within a trial or a GF segment. Completing `J_epsilon` successes costs an expected `J_epsilon Delta/q` in trials and exactly `J_epsilon h` in GF intervals, which proves the upper bound in (16); earlier hitting can only reduce the time. Markov's inequality gives the displayed tail bound for the first hitting time.

Rejection durations are included explicitly; the flow pauses while proposals are evaluated. `Delta` is an assigned exact-oracle evaluation cost, not measured runtime for an infinite-population calculation. The text states that distinction, so its elapsed-time claim contains no hidden computational-cost assertion. Fixed positive `h` and infinitely many successes give infinite accumulated original GF time almost surely. Finite hidden travel does not imply finite accumulated GF time, and the proof does not make that inference.

## 6. Initialization at orders one and two, and optional order-three refresh

The initial feature-independence proof in `INITIAL_EXCLUSION.md` is valid. Canonical parity removes all even-to-anything contraction blocks, but the lower odd pairs retain their nonzero correlation and reverse-source response. The exact raw contraction row is `(alpha v, alpha kappa+tau beta)`, and inverse-Cholesky substitution gives full ridged Gram inverses. The resulting scalar response has derivative of strictly positive sign: the lower bound `b_* >= (529/1024)b^*` makes `2b_*-b^*>0`, and every discarded ridge contribution in equation (14) is nonnegative. Gaussian integration by parts cancels the gate-derivative terms and proves strict monotonicity of `F` on the interior; continuity plus an intermediate interior point handles the endpoints.

Consequently `A(u)=(F(u1),F(u2))` is injective and nonzero on the circle and identifies antipodes exactly. For distinct vectors modulo sign, choosing a line with distinct positive absolute projections reduces a possible upper-feature dependence to a dependence among `tanh(lambda_j t)`. Analytic continuation, the limit at positive infinity, and successive removal of the slowest exponential prove independence even when slopes are commensurate. Positive density of the upper Gaussian-tanh coordinates upgrades an almost-sure relation to the required pointwise one. Positive observation weights then make the weighted Gram in the candidate positive definite.

At order one the same odd lists and same raw Gaussian program occur; only the ridge changes to `eta1=1/4096`. The positivity proof above holds for every positive ridge, so the supplied Section 6 extension is valid without identifying order-one and order-two trajectories. This proves the canonical starting-Gram hypothesis for all finite compatible data at both orders, with no minimum input separation. Their Gram eigenvalues can still deteriorate arbitrarily with geometry.

The candidate correctly does not extend that canonical-initialization proof to order three. Its optional alternative follows from `NOISE_GLOBAL_PROGRESS.md` Section 2: constants belong to the lower span, `X=tanh(xi1)` belongs to the upper span with positive density, and the lower Gaussian marks are nonatomic. Select finitely many directions distinguishing all input sign patterns up to sign; finite proper hyperplanes cannot cover the positive-mass simplex, so one can choose weights with nonzero pairwise sign-distinct mixture values. A quantile partition realizes these weights on the existing lower carrier. With `w_T=T v` and `M_*=e l^T`, the upper functions are exactly `tanh(X s_i(T))`; for sufficiently large finite `T` their slopes remain nonzero and distinct up to sign. The same elementary independence proof applies.

This hidden choice depends only on inputs and canonical marks. Although the dependency also constructs a fitted `c_T` to prove expressivity, the candidate uses only the preceding hidden construction and keeps `c=0`; it never computes or receives `c_T`. The jump is a finite, loss-neutral replacement of the hidden starting state, not the unchanged canonical trajectory. Subject to the line-326 loss normalization repair, its role at `p=1,2,3` is accurately stated.

## 7. Frozen versions and completion evidence

The candidate hash matched the supervisor's supplied SHA256 before report writing. All listed inputs were rehashed after the scientific reads; their values are below. The canonical book hash covers the whole file for version identification, but reading was restricted to the stated ranges. Shared checkout HEAD at review time was `ccd783d8d461bfed9a77a35d21831565cf48b314`; the index had no staged paths. Other modified or untracked files were seen only as status metadata and preserved.

| Input | SHA256 |
|---|---|
| `RATE_ADAPTED_READOUT.md` | `0d8dcaf93a5b4bc60291c348fe2a8046abae244ee906e367e7c09e27a8a01535` |
| `ESCAPE_AND_LIMITS.md` | `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2` |
| `INITIAL_EXCLUSION.md` | `34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c` |
| `INITIAL_REVIEW.md` | `6fd58a9faa1b07a0eaa53fe9595b63180b225e72df35a7f50fe9f6e629d64baf` |
| `NOISE_GLOBAL_PROGRESS.md` | `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `AGENTS.md` | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `RESEARCH_WORKFLOW.md` | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

All assigned checks are complete. The only requested correction is the explicit binary-label assumption or general-label loss formula in Section 2 of this report. No further scientific input or computational evidence is needed for the scoped theorem. This report certifies neither promotion readiness nor claims about the original unmodified optimizer or finite-width networks at unbounded times.

Completion provenance: the scientific review and this report were finished before the supervisor supplied an informal sketch of a possible future inverse-free extension. That later sketch was not used in this review and has not been reviewed here. The supervisor also agreed to repair the binary-label scope wording. A final rehash after report creation confirmed that the frozen candidate and every listed dependency still had the hashes above; this report therefore evaluates the original frozen version and records the correction rather than silently certifying an amended candidate.

## 8. Follow-up closure of the label-scope correction

On 2026-09-19 the supervisor supplied the repaired candidate, SHA256 `1e1ad47811a41d9f09d625746c7b4bc6f95857a1a08521a80b4c80bf9dfb610b`. I reread its complete 356 lines. Section 1 now explicitly states that labels belong to `{-1,1}`. The subsequent loss-one claim for initialized `c=0` is therefore correct. A byte-level verification replaced exactly that amended introductory text in memory with its former text and recovered the original SHA256 `0d8dcaf93a5b4bc60291c348fe2a8046abae244ee906e367e7c09e27a8a01535`; no other candidate change occurred. The scientific dependency hashes remain unchanged.

**Final internal verdict for the corrected hash: PASS, with the sole original correction closed.** The original frozen-version findings above are retained. This is an informed follow-up verification by the same reviewer, not a new isolated promotion audit.
