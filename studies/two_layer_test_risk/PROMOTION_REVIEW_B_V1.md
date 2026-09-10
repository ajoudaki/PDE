# Independent scientific promotion review B — frozen C.4 packet v1

Date: 2026-09-10. Reviewer: `/root/promotion_review_b`.

**Verdict: ACCEPT the exact scoped scientific addition.** The proposed local equal-training-loss comparison, controlled cubic population risk expansion, explicit Gaussian coefficient, and qualified finite-GF/raw-GD consequences survive this review. No required correction or unresolved scientific objection was found. This is a scientific review of the frozen addition, not approval to integrate it and not a determination of the coefficient's sign or nonvanishing.

## Independence, inputs, and complete read coverage

I received the neutral review assignment, the packet location, expected hashes, authors/assemblers' names, and the exclusions. I did not participate in authorship or assembly. I did not read author startup, study history, author reports, internal verdicts, the relevance selector's report, or the other scientific review. I did not consult another reviewer or delegate any part of this complete review. The excluded authors/assemblers are `root`, `cubic_derivation`, `matching_remainder`, and `quadrature_check`; the excluded selector is `relevance_selector`.

I read the required `solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and the latter's complete `references/adversarial-audit.md`. The relevant skill roots were `/etc/codex/skills/solve-math-rigorously/` and `/etc/codex/skills/investigate-conjectures/`.

All packet files below were read completely, including every scientific line and proof body in the dependency file. One combined tool response truncated part of the first dependency read. I repaired it by rereading dependency lines 73–244; no unread gap remains. The completed dependency coverage was lines 1–450, 451–850, 851–1230, 1231–1570, and 1571–1777, with the explicit repair inside the first interval.

| Frozen packet input | Complete coverage | Verified SHA-256 |
|---|---:|---|
| `assignment.md` | 48 lines | `8e4351e9b78e961543cd88c03ee9115aa3b92aec69815afdfbdce891f1f8267e` |
| `candidate.md` | 642 lines | `b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4` |
| `dependencies.md` | 1777 lines | `8378046bc80abc06077b34182141d282cf0ba6ac6d7fde6c84e2c6bab5b19db7` |
| `NOTATION.md` | 98 lines | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs_README_before.md` | 265 lines | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| `docs_README_after.md` | 265 lines | `e92464827a2d277a57a356167190598f52425769e23e7538cd9e3cbbe7afb371` |

The complete manifest was read. Its SHA-256 is `14316c7a0162fdc81788efabdce1f08b2a7d219adbd8fd8960f295274d5345b7`. Every packet hash agrees with it. All twelve frozen-edition file hashes also agree with the manifest. The proposed `edition/docs/global_nonlinear.md` hash is `5f31b500a60ad98fd9a200094f1169267a590a39015aaa53c8c222bc07cb3fc2`; its candidate begins at line 3831, occurs once, and is the complete suffix. The relevant boundary, edition lines 3810–3845, was also read.

I verified that the full dependency extracts are verbatim copies of the edition's original source lines 181–500, 1835–1893, and 2449–3829. Thus the claimed Section 2/3, A.1–A.4, and C.1–C.3 proof bodies, including the weighted correction, are supplied. The guide comparison changes only line 155, by adding the stated tanh risk-expansion sentence. Hash checks on the other edition files are integrity checks, not claims to have reviewed their unrelated scientific content. The guide's unchanged contextual literature discussion supplies no proof premise for C.4; I did not import an external theorem or claim a new literature audit.

No necessary input was missing. No training, quadrature, sampling, or coefficient-sign computation was run. The only computation was read-only line, hash, exact-extract, and text-difference verification. I made no Git mutation, clone, worktree, or input edit; the only created file is this assigned report.

## Exact target and component verdicts

The target is the specified two-hidden-layer tanh network, fixed three-angle design, mean squared training loss, uniform-circle risk, and small stored Gaussian readout initialization. The limiting comparison freezes both hidden blocks in `g`, while `f` trains all three blocks. The central conclusion is local and concerns the actual population flow. It is not a formal-jet approximation, a growing-design theorem, or a claim that feature learning improves risk.

| Component | Verdict | Scope of finding |
|---|---|---|
| Model, normalization, typed notation, fixed design | PASS | The stored-weight equations, variances, mobilities, loss factors, and population pairings agree. |
| Contained existence, action, response, and continuity dependencies | PASS for the needed specialization | Their hypotheses hold for this tanh model; the complete operative proofs were checked. |
| Passive whole-circle construction and finite capture | PASS | Fixed probes plus deterministic angular equicontinuity establish the required uniform prediction/risk convergence. |
| Positive training Grams and unique population matching | PASS | Singular input Gram is retained; activation/response Grams supply the needed positivity. |
| Fixed-direction fourth moments and actual integral remainder | PASS | The proof obtains the uniform fourth-order error without assuming ambient L2 smoothness or higher trained-path moments. |
| Cubic predictor coefficient, clock correction, and risk sign convention | PASS | Both hidden contributions and the readout correction remain; all normalization factors check. |
| Explicit Gaussian contraction and singular passive slots | PASS | Both source response and full innovation second moment remain, with an admissible query order. |
| Finite-GF/raw-GD matching and conditional sign transfer | PASS | The actual random initial readout is retained; claims use fixed positive lower time cutoff. |
| Strict hidden activity and absolute nonaffinity statements | PASS in the stated local model | Weighted C.3 applies; these facts do not supply a risk sign. |
| Guide addition | PASS | The sentence accurately states a fixed-design controlled cubic expansion and explicitly leaves sign/nonvanishing open. |

## Independent checks and adversarial attacks

### 1. Loss factors and the degenerate design

The raw mobilities `(n,1,n)` and the stored output pairing `/n` give the displayed population equations with coefficient `-2/3`. In particular the readout derivative at zero is `2S`, where `p=y/3`. Consequently

\[
g'_0(x)=2K_{x,\mathrm{train}}p=a(x),\qquad
L'_g(0)=L'_f(0)=-4p^\top Kp=-4B_0.
\]

These identities rule out the plausible factor-three or factor-two error caused by using C.3's original summed loss without its weighted correction. The label values, cosine correlations, and input lengths in (C4.1)–(C4.3) are correct. The relation `x_2+x_3=2c_1 x_1` proves rank two, while the first two inputs are independent. None of the three training directions is parallel to another and all three labels are nonzero.

The bounded ridge-function proof in C.3 does not infer activation rank from input rank. Its commuting finite differences isolate a single ridge; a bounded sequence with vanishing finite differences must be constant. Applied to tanh and Gaussian full support, this proves `Q>0`. Full support of `Y` then proves `K>0` by varying a single coordinate. The separate `V>0` argument remains valid where `S=0`, without division by `S`; conditioning yields `D>0`. Thus no omitted whitening or inverse of `G` is needed.

**Outcome:** the singular-design and normalization attacks fail. Their required bridges are explicitly present.

### 2. Are the population and step-limit dependencies adequate?

I checked the complete Gaussian conditioning proof, including its adaptive transcript induction, source covariance as an uncentered second moment, and singular-Gram regularization. The finite conditioning formula preserves both orientations of the same matrix. Its new input is measurable before the unexplored answer is revealed. Fixed-rank output projections vanish in normalized mean square, rather than being discarded as independent finite-width coordinates.

A.1–A.2 extend the fixed-program value/response rules to the bounded-gate products needed here. A.4 gives continuity of bounded multipliers against an L2 field and strong chain rules along actual curves, while expressly avoiding a blanket Frechet-smoothness claim for nonlinear maps on L2. The bounded initialized actions are built on the generated common spaces, and exact finite adjunction passes to those spaces.

For C.1, the preliminary operator/RMS ball precedes the tail estimate. C.2's response proof retains the single-source factor `Delta omega_b`; it does not use a maximum of Gaussian history coordinates. Its forward response caps are selected bottom to top and its backward caps top to bottom before shortening time. The literal construction order prevents either coefficient from depending on its own unconstructed current value. Jensen's estimate uses weighted sums and marginal tails without assuming temporal independence.

The one-reference cutoff estimate then closes existence, uniqueness, and the actual-GD comparison. Its growing factor is exponential in the cutoff, while the reference tail is Gaussian in that cutoff. The limit order is width first at fixed coarse mesh/cutoff, coarse mesh next, then cutoff; no hidden condition coupling `eta_n` to width appears. The finite-GF corollary uses fixed-width Euler convergence and the every-deterministic-vanishing-mesh theorem. Squared-loss energy provides finite-dimensional global GF existence at each fixed width. The present tanh model satisfies all required smoothness, moment, fixed-design, and vanishing-readout assumptions.

**Outcome:** no missing bridge from fixed programs to the particular actual local flow or the asserted step quantifiers was found. Broader unrelated chapter claims were not used to enlarge C.4.

### 3. Passive capture and unique matching

Equation (C4.9) is an exact first-layer identity: the two training basis inputs span the whole circle. The coefficient functions and their angular derivatives are bounded. The norm ball, Lipschitz tanh, bounded connector, and readout bound therefore give a common angular modulus for population and finite predictions. Appending a fixed passive probe does not change training weights. C.1's fixed-probe convergence at a finite angular net, followed by shrinking net size, proves whole-circle uniform-in-time convergence. Bounded predictions transfer it to the squared risk. This remains true for affine interpolation of the actual raw parameters.

The frozen solution has residual `-exp(-2Ks/3)y`, so its loss is strictly decreasing for every finite nonnegative `s`, with range `(0,L_g(0)]`. The full loss satisfies the stated kernel-norm differential inequality and remains positive. Thus it lies in the frozen loss range and defines a unique matching time. Comparing the lower full-loss exponential bound with the upper frozen-loss bound gives the direction of (C4.13), `tau(t)<=B_K t/lambda`, as written. Shortening time gives both the clock margin and strict full-loss decrease.

**Outcome:** neither passive-data augmentation nor a finite-time zero-loss endpoint invalidates matching. The inverse is taken where its derivative is bounded away from zero.

### 4. Fourth moments and query chronology

The initialized transpose law in (C4.14) gives a bounded lower-root response plus a Gaussian innovation with covariance `V`. This establishes fourth moments of `P`, and hence uniformly of `T_x,A_x`, without asserting that a bounded L2 action preserves L4 in general.

For (C4.15), an admissible order is: reveal the full lower root, the three training forward calls, and the three reverse calls defining `P`; form `A_x`; then query the forward action on `A_x`. The input is already measurable. Its projection onto the training activation span uses only the fixed positive matrix `Q`; the reverse correction uses only the fixed positive matrix `V`. The coefficients `q_x,v_x` and innovation scale are uniformly bounded by Cauchy–Schwarz. The response is a finite sum of Gaussian `Y_j`, bounded `U_j`, and a Gaussian innovation. Therefore `W_0^(2)A_x`, and then `R_x^hid`, have uniformly bounded fourth moments.

The argument needs no independence from the as-yet-passive `Y_x` and claims none. A marginal conditional calculation for each angle suffices for the fourth-moment bound; simultaneous independence of the innovations across angles would be false and is not used.

**Outcome:** the strongest plausible moment and anticipative-query objections are resolved by the supplied formulas. No trained-path L4 assumption was silently inserted.

### 5. Integral remainder and an independent coefficient check

The readout integral has a bounded representative of size `O(t)`. This gives backward L2 sizes `O(t)` and hidden/state increments `O(t^2)`. The gate interpolation inequality converts the lower preactivation L2 increment into an L4 gate difference of order `t`; pairing it with the fixed L4 `P_b` gives the required backward error `O_L2(t^2)`. It does not multiply two uncontrolled trained factors.

The refined first-layer and connector velocities therefore have errors of order `t^2`, integrating to (C4.19)'s `O(t^3)` errors. The fixed-direction Taylor bound (C4.20) first removes the L2 error by Lipschitz continuity; its remaining quadratic remainder is controlled by the fixed direction's fourth moment. Applied twice, it yields (C4.21) uniformly over angles. This proves an actual integral-trajectory estimate, rather than exchanging width with a finite Taylor jet.

Subtracting the trained and frozen readout equations retains the moving residual. Gronwall first bounds their difference by `O_L2(t^3)`. The residual-difference forcing then integrates to `O(t^4)`, whereas `(-y_b)(2t^2E_b)` gives the coefficient `4/3`. Pairing with the trained readout contributes `4E[S E_x]t^3`. Hence the complete coefficient is exactly (C4.6).

As an independent algebraic check on the training restriction, put `H=G circ D+Q circ V` and `C_ab=E_2[E_a H_b^(2)]` in this paragraph only. The hidden kernel blocks start with `4H t^2`; the readout kernel changes by `2(C+C^T)t^2`. Adjunction gives `Cp=Hp`. Subtracting the prediction equations therefore gives the cubic coefficient

\[
\frac23[4H+2(C+C^\top)]p
=4Hp+\frac43C^\top p,
\]

which agrees with `J_train`. Its contraction with `p` is `(16/3)mathcal A`. This cross-check would detect omission of the readout correction or a hidden-block factor.

Finally `L_f-L_g=-2p^T J_train t^3+O(t^4)`. Division through the locally nonzero derivative `-4B_0` gives `beta=8 mathcal A/(3B_0)>0`. The mean-value argument first establishes `tau-t=O(t^3)`, so substituting `L'_g(s)=-4B_0+O(s)` is legitimate. The matched prediction difference is `t^3(J-beta a)+O(t^4)`. In `R(g_tau)-R(f)`, the difference factor is its negative and the sum factor is `-2cos(3alpha)+O(t)`, giving the positive sign in the definition of `chi`.

**Outcome:** the actual remainder, coefficient factors, inverse correction, and risk sign convention pass. Positivity of `mathcal A` supplies only training acceleration; `p^T(J-beta a)=0` explicitly shows what matching removes.

### 6. Explicit contractions, repeated inputs, and antipodes

For each bounded smooth upper function used in the coefficient, the transpose response is `sum_i phi(Z_i) E[partial_i F]` plus a centered Gaussian innovation whose covariance with another innovation is `E[F_1F_2]`. Conditioning its product on the lower roots gives exactly the two terms in `Lambda`: the full innovation second moment multiplied by the lower gate moment, and the response-mean product. Adjunction then gives `mathcal C_a(F)` and (C4.29). Discarding either term or replacing the transpose by an independent matrix would change the answer; neither substitution occurs.

For a repeated passive slot `x=a`, the initialized and trained fields coincide with the corresponding training fields. Formal differentiation keeps both slots, and their source coefficients combine because the two source input fields are equal. For the antipodal slot `x=-x_a`, oddness gives `Z_x=-Z_a`, `H_x^(1)=-H_a^(1)`, `Y_x=-Y_a`, and `H_x^(2)=-H_a^(2)`. Evenness of `phi'` then gives `T_x=-T_a`, `A_x=-A_a`, `M_x=-M_a`, `R_x^hid=-R_a^hid`, `E_x=-E_a`, hence `J(x)=-J(x_a)` and `a(x)=-a(x_a)`. These are the required odd-network boundary identities. The null-covariance combination is the same zero L2 combination of source inputs, so the contracted derivatives are unambiguous in both cases.

No augmented passive covariance inverse is used. The contained singular-source regularization and continuous covariance-square-root coupling justify the Gaussian formulas at rank loss. All functions and derivatives actually integrated here are bounded, so bounded convergence supplies continuity in the passive angle and legitimizes the final circle integral.

**Outcome:** the passive singularities do not create exceptional angles, divergent coefficients, or missing response terms.

### 7. Finite clocks, small readout, and the unproved sign

The actual finite readout is shared by the two models and retained throughout their paths. Its normalized norm tends to zero; it is not set identically to zero at finite width. Thus equality of the full and frozen initial kernels is asserted only for the population limit. The finite hidden tangent blocks may already be nonzero, consistently with the stated warning about lower-order finite-width effects.

The empirical frozen kernel converges to positive `K`. Its nonzero initial residual and positive kernel give strict frozen finite-GF decay to zero with probability tending to one. For raw GD the factors are `1-(2/3)eta_n lambda_i`; eventual positivity makes both grid decay and within-step affine-interpolation decay strict. With bounded tanh, `lambda_max(K_n)<=3`, so any deterministic vanishing step eventually meets this positivity condition without a width-dependent extra restriction.

For each fixed `[delta,T]`, population full loss has a positive distance from both ends of the frozen loss range. Uniform loss capture therefore puts the actual finite full losses in that range. The clock margin confines the inverse to the available compact interval, where the population inverse is Lipschitz. This proves uniform finite-clock convergence, and uniform passive-risk capture plus continuity gives convergence of matched risks. No monotonicity of the full interpolated GD loss is needed for this pointwise inverse construction.

If `chi!=0` is separately proved, the positive lower bound on each fixed `[delta,t0]` transfers the sign in probability. The argument does not transfer a sign uniformly down to time zero, does not allow an arbitrary `delta_n->0`, and does not furnish a width rate. The candidate states precisely these restrictions.

**Outcome:** the finite scope is supported. The absence of a sign or nonvanishing proof is an expressly retained open problem, not an undisclosed premise of the accepted expansion.

## Objections, limitations, and completion

**Required corrections:** none.

**Unresolved scientific objections to the exact proposed statements:** none found after complete review. The tests above identify the possible failure signatures and the supplied arguments that exclude them in this model. They do not certify a claim outside the fixed local scope.

**Optional suggestions:** none needed for acceptance.

The accepted result leaves `chi=0` possible. It proves no numerical value, error constant, risk advantage, global continuation, sample-size limit, or general feature-learning benefit. C.3's activity and absolute nonaffinity facts survive under the weighted hypotheses, but do not fill the open risk-sign question. The guide accurately preserves that distinction.

The review is complete for the exact verified packet hashes above. Any substantive correction or expansion of those claims requires review of the changed inputs; this report must not be treated as acceptance of an unexamined revision.
