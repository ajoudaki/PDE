# Recovered L2 mixed-activation global finite-GF results

Read-only evidence audit, 8 September 2026. No new proof or experiment. The six requested proof/review files were read completely: 564-line clock theorem, 171- and 290-line isolated clock reviews, 1008-line exact-GD manuscript, 147-line permanent-gate theorem, and 223-line isolated gate review. Their recovered bytes were checked against the recovery manifest; the two accepted manuscripts also exactly match the SHA-256 values recorded by their reviewers.

The result missing from the narrow population-only inventory is **global optimization and convergence of actual finite gradient flow**, with width-uniform constants on an explicit event whose probability tends to one. A second reviewed theorem adds permanently unsaturated first-layer mass. A complete exact-GD manuscript is also recovered, but its independent review/acceptance record has not been recovered. None of these files establishes a global population limit for this mixed-activation model.

## Exact model shared by the results

| Item | Conditions |
|---|---|
| Depth/samples | Two hidden layers of equal finite width `n`; two fixed inputs in `R^d`, `d>=2`. |
| Inputs | `||x_1||²=||x_2||²=d`, `x_1ᵀx_2/d=ρ`, with **any fixed `−1<ρ<1`**. Both endpoints excluded; no constants uniform near them. |
| Labels/loss | Exactly `y=(1,−1)` and summed unhalved loss `L=(f_1−1)²+(f_2+1)²`. No arbitrary-label or same-label extension claimed here. |
| First activation | `φ_1(z)=∫₀ᶻp(u)du`, where `p` is even, nonnegative, smooth, supported on `[-R,R]`, and strictly positive on `(-R,R)`. Hence `φ_1` is an odd smooth saturation with values `±A`, `A=∫₀ᴿp>0`, on the two tails. |
| Second activation | `φ_2(z)=z+ε atan(z)` for fixed `ε>0`, with `1<=φ_2'<=1+ε`. It is unbounded with linear growth and bounded homogeneity defect `zφ_2'(z)−φ_2(z)`. |
| Finite normalization | `z_a^(1)=W^(1)x_a`, `z_a^(2)=W^(2)h_a^(1)`, `f_a=(W^(3))ᵀh_a^(2)/n`. `W^(3)` is the stored rescaled readout. |
| Independent Gaussian initialization | Entries of `W^(1)_0~N(0,1/d)`, `W^(2)_0~N(0,1/n)`, **stored** `W^(3)_0~N(0,n^(−2))`. The tiny readout is nonzero almost surely; it is not replaced by zero. |
| GF scaling | With residual-free backpropagation `δ`, `Ẇ^(1)=−(2/d)Σ_a r_aδ_a^(1)x_aᵀ`, `Ẇ^(2)=−(2/n)Σ_a r_aδ_a^(2)(h_a^(1))ᵀ`, `Ẇ^(3)=−2Σ_a r_ah_a^(2)`. These are gradient mobilities `(n/d,1,n)`. |
| Exact GD scaling | Simultaneous update of all blocks from the same old node with the above right-hand sides times the single fixed `η=n^(−2)`; physical time `t=kη`. |

These activations differ from both the pure-arctan branches and the all-layers affine-plus-small-arctan branch. Their conclusions must not be merged solely because the top activation contains arctan.

## M-P1: reviewed global finite GF optimization and endpoints

Primary: [COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md). Exact accepted hash: `cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b`.

There are three distinct layers of assertion in its complete proof.

**For every finite initial parameter state**, actual smooth finite GF exists uniquely for all finite times. The exact metric energy identity is

`−L̇=||Ẇ^(3)||²/n + ||Ẇ^(2)||_F² + (d/n)||Ẇ^(1)||_F²`.

It controls each finite-time parameter displacement and prevents finite-time blowup. No positive Gram, loss margin or Gaussian-success event is needed for this existence assertion. It does not by itself ensure interpolation.

**Deterministic conditional optimization theorem:** let `N_s,N_o` count first rows initially saturated at both inputs with same versus opposite signs. Those entire first rows stay exactly unchanged. Their Gram contribution gives

`G_1(t)=(H^(1)(t))ᵀH^(1)(t)/n >= γ_n I`, `γ_n=(2A²/n)min(N_s,N_o)`.

If `γ_n>=γ>0`, the initial middle operator norm is bounded, and the actual solution achieves `L(t_0)<=2−δ` with `δ>0`, then loss decays exponentially after `t_0`, all three finite parameter paths have finite total variation and converge to interpolating endpoints, and both residual clocks are finite:

`X(∞)=∫₀∞sqrt(L(t)) ||W^(3)(t)||/sqrt(n) dt <∞`,

`S_∞=∫₀∞sqrt(L(t)) dt <∞`.

The proof also bounds the centered middle Frobenius displacement `||W^(2)(t)−W^(2)(0)||_F`, middle operator norm, stored-readout RMS and upper-preactivation RMS for all time.

**The Gaussian hypothesis is actually discharged.** For every fixed `ρ∈(−1,1)` and the stated fixed activations, there is an explicit finite width threshold `N_*` and an initialization event `E_n` of probability at least `max(0,1−p_n)`, with `p_n=O(1/n)+O(exp(−cn))`, on which the actual finite GF achieves a fixed margin below loss `2` at a fixed time `τ>0`. All optimization, clock, norm and parameter-endpoint conclusions above then hold with constants independent of width and time on `E_n`.

The event combines: sufficient counts of both saturated row types; positive initial top-feature Gram; initial middle operator norm at most `8`; and stored-readout RMS at most `2/n`. Its probability proof uses conditional Gaussian row moments and union bounds, without falsely treating the two middle-matrix events as independent. The short-time margin follows from the exact energy identity and persistence of the initial top-feature Gram, including feature transport. It allows initial loss slightly above `2`; neither a negative initial derivative nor replacement by exactly zero readout is used as a shortcut.

For the explicit rate, the manuscript defines fixed `γ,β_*,s_*,τ>0` and proves on `E_n`

`L(t)<=s_*² exp(−4γβ_*²(t−τ))`, for `t>=τ`,

`X(∞)<=X_*`, `S_∞<=S_*`, `sup_t||W^(2)(t)||op<=U_*`, and `sup_t||W^(3)(t)||/sqrt(n)<=b_*`.

It also bounds all normalized total variations and `sup_t||z_a^(2)(t)||/sqrt(n)<=AU_*`. At each fixed finite width, actual parameter limits exist and their predictions equal `(1,−1)`. No width/infinite-time interchange or convergence of these endpoints as width grows is asserted.

The central closure is worth preserving because it resolves an actual open premise of the deterministic theorem. With `B=W^(2)−W^(2)(0)`, `a=||B||_F`, `b=||W^(3)||/sqrt(n)`, differentiation gives a centered balance `|a²−b²+b_0²|<=C_DX`. It uses the **initial operator norm**, not its order-`sqrt(n)` Frobenius norm. The achieved loss margin implies `b>=c/(1+sqrt(X))`. The exact kernel coercivity `K_2>=γb²I` and `X'=sqrt(L)b` then bound the increasing divergent primitive `F(X)=2(sqrt(X)−log(1+sqrt(X)))`. Thus the total weighted clock is proved finite rather than assumed. It subsequently yields `b>=β_*>0`, exponential loss and finite unweighted clock.

Both [review A](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK_REVIEW_A.md) and [review B](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK_REVIEW_B.md) read the full exact manuscript as their sole mathematical source, recorded matching before/after hash `cb0a9abb…`, and returned **PASS with no required correction**. They independently checked all 49 numbered equations, every explicit threshold/probability constant, the actual nonzero Gaussian readout, both finite/global time quantifiers and the endpoint claim. This is strong recorded mathematical review evidence, not proof-assistant verification.

## M-P2: reviewed permanent unsaturated first gates

Primary: [COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES.md](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES.md), hash `dcaaea01fe2f22b8848da127eed58fbcf29bc8fe9fba516ebcaa0dde70abac20`. Its header still says “UNVERIFIED”, but the later complete [isolated review](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES_REVIEW.md) records that exact hash and **PASS with no required fix**. The review therefore supersedes the stale header as evidence of review status.

For the same actual finite GF, add an explicit initial strip-count event to `E_n`. Then each sample has a fixed individual subset of at least `nm_ρ/4` first rows, independent of time though allowed to depend on the full trajectory, that stay a fixed positive distance from saturation for **all `t>=0`**. In particular,

`inf_(t>=0) (1/n)Σ_i φ_1'(z_(a,i)^(1)(t))² >= (m_ρ/4)p_*² >0`, for both samples.

The additional failure probability is at most `8(1−m_ρ)/(nm_ρ)`, with explicit `m_ρ>0` for every fixed interior correlation. Thus the result again holds with probability tending to one, with width/time-independent constants.

The finite weighted clock controls the RMS of the individual total first-row driving budgets. For a row with one preactivation interior and the other sufficiently far exterior, the exact identity `z_b−ρz_a=constant` persists while the exterior gate is zero. An integrating-factor estimate bounds the interior coordinate's distance from the saturation boundary. A global count of rows with large driving budget is subtracted separately from each initial strip count. No independence between those future-dependent budgets and the initialization is assumed.

This is **gate positivity**, not permanent nonzero force or velocity. It gives no lower bound on the reverse field, a residual-weighted kernel, moving mass, nonlazy learning or top-layer distributional nonaffinity. The independent review explicitly preserves all of these limitations.

## M-C1: complete global exact-GD manuscript, acceptance not recovered

The complete [COMPACT_FIRST_LINEAR_TAIL_TOP_RAW_GD.md](OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_RAW_GD.md), 1008 lines, hash `4cfb3649a27b6110c1f61e1caff2d59de8c11ab1538f6ee50b7017783b7a3ede`, is **stronger than a conditional raw-GD estimate or an unfinished template**. It claims and supplies a full deterministic plus canonical high-probability theorem for exactly the simultaneous updates and `η=n^(−2)` above.

Its claimed conclusion includes all-time certified loss decrease along each full raw update segment; an actually attained loss margin by a fixed physical time; bounded upper norms and weighted/unweighted residual sums; geometric nodal loss decay; finite total variation and interpolation at limiting finite parameters. The width threshold is chosen before either induction and is independent of the terminal step count. No GF/GD comparison is used.

The proof explicitly supplies the complete raw-coordinate Hessian bound `||∇²L||op<=sqrt(n)H(U,V)`, including mixed layer terms. It first contains the full proposed segment using an old-node gradient bound, then applies the Hessian descent certificate. A separate finite initial induction supplies the loss margin by discrete action. Its exact centered balance contains the quadratic Euler correction, whose accumulated absolute value is at most `2ηL_0` on the certified prefix. The later induction uses the clock bound to restore the guard bounds at each candidate next node. The claimed rate is

`L_k<=s_*²(1−2ηγβ_*²)^(k−m) <=s_*² exp(−2γβ_*²(t_k−t_m))`.

This source's independent mathematical review or final acceptance disposition has **not been recovered**. No separately named review for this mixed-activation GD file is present in the recovered directory. Reviews of `COMPACT_GATE_RAW_GD_AND_GAUSSIAN_PATHS.md` concern a different source and must not be relabelled as this review. Accordingly this entry records a complete claimed positive candidate and its exact scope, but does not place it in the same accepted tier as M-P1/M-P2. The theorem's assumptions are discharged inside its manuscript; “conditional” here would be misleading unless used solely for its unresolved acceptance status. Population convergence, GF/GD path closeness and permanent-gate consequences for GD remain unproved by this file.

## Distinct negative findings that should survive consolidation

| ID | Finding and evidence | Scope |
|---|---|---|
| M-N1 | **Fixed-width almost-sure interpolation is false** for this exact independent Gaussian model. Review A gives an event of positive probability `m_s^n` on which every first row is same-sign saturated, hence first features coincide forever, `f_1=f_2=u` and `L=2u²+2>=2`. | Actual initialization/trajectory counterexample. Compatible with the high-probability asymptotic theorem because it lies outside its success event. |
| M-N2 | A positive frozen first Gram does not imply strict improvement from loss `2`. Set the upper matrix and readout to zero; all velocities vanish and `L≡2`. | Deterministic counterexample to replacing the achieved strict margin by `L<=2`. The successful Gaussian event's initial top-feature Gram prevents this case. |
| M-N3 | The clock theorem's success event `E_n` alone does **not** guarantee unsaturated first mass. The gate reviewer constructs a positive-probability open Gaussian event with all first rows saturated, half same-sign/half opposite-sign, while all `E_n` inequalities hold strictly. | Shows why M-P2 must retain the additional strip-count event. Optimization may occur through upper weights with every first derivative zero. |
| M-N4 | Width-uniform upper operator/RMS bounds, positive first Gram and even small loss do not imply width-uniform coordinatewise curvature `|W_i^(3)φ_2''(z_(i,a)^(2))|`. Review A gives bounded-norm states with this product `εsqrt(n)/2` and loss tending to zero. | A parameter-state counterexample, not a claim those states lie on the canonical trajectory. It blocks this inference, not global population existence by every possible method. |
| M-N5 | At `ρ=1` the inputs coincide and opposite labels make loss below `2` impossible. At `ρ=−1` the odd features are antipodal and the two-dimensional frozen Gram is rank deficient. | The first is an actual optimization impossibility; the second only defeats this full-rank proof and does not establish failure for the compatible antipodal labels. |

No global mean-field/population construction, limiting uniqueness, propagation, or full feature-learning theorem follows from the clock/optimization estimates alone. The present audit adds no such inference. The later Generalize result supplies a broader positive-time GD/population theorem in a class containing these activations, but it does not supply this branch's all-time population theorem.

## Recovery provenance, chronology and remaining gap

Original source directory `/tmp/l2-two-sample-proof-0ywjpp` was not directly readable in the recovery workflow. The parent audit recovered exact historical `fileChange` contents and patches from the app event database. [OLDER_TWO_SAMPLE_RECOVERY_MANIFEST.json](OLDER_TWO_SAMPLE_RECOVERY_MANIFEST.json) records each original path, recovered path, source task/turn, event ordinal and computed SHA-256. The reconstructed accepted hashes match independent contemporaneous reviewer hashes, providing stronger identity evidence than a path or conversational paraphrase.

| Source | Source task / event order | Full reading and review status |
|---|---|---|
| Clock theorem | Author `01a078b3-b1aa-7862-bbd9-baeef2691fb3`, event 58 | All 564 lines read; recovered SHA matches both reviewers. |
| Clock review B | `01a078ba-92cd-79e2-bf5a-6ff7e539d322`, event 53 | All 290 lines read; isolated full PASS. |
| Clock review A | `01a078ba-9262-7af0-92ce-6d10efeec95a`, event 62 | All 171 lines read; isolated full PASS plus additional scoped counterexamples. |
| Permanent gates | Parent `01a07192-e207-7ab2-8b41-d34600659e7e`, turn `01a076fb-5b40-70f0-9d67-79274d044101`, event 13889 | All 147 lines read; later independent review supersedes initial UNVERIFIED header. |
| Gate review | `01a078c3-159c-7543-a314-5e9b28c9ccd1`, event 45 | All 223 lines read; exact source/dependency hashes and PASS on augmented event. |
| Exact GD | Author `01a078bf-43e8-73a1-a684-f536b9daea55`, events 56 and 69 | All 1008 lines read, including final patch; complete candidate, independent acceptance missing. |

The recovered 730-line `CONTRACT_AND_SEARCH.md` has earlier scope entries and no occurrence of this clock/mixed-activation result; it is not treated as the final disposition of these later manuscripts. Its older omissions cannot erase the directly recovered proofs and reviews. The exact-GD review gap has been reported to the root auditor for possible final-task recovery. [L2_MIXED_FINITE_GF_HASH_CHECK.json](L2_MIXED_FINITE_GF_HASH_CHECK.json) records all six reread hashes and manifest identity checks.
