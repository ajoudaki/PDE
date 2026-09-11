# Independent complete scientific review of P1

Reviewer: `/root/promotion_review_a`  
Date: 2026-09-11  
Verdict: **ACCEPT for the scientific content and scope of the frozen P1 addition.**

There are no required corrections and no missing mathematical inputs needed
for the proposed theorem. This verdict concerns the frozen scientific packet;
it is not an integration check, a promotion authorization, a claim of novelty,
or a review of unrelated existing chapter results.

## Identity, isolation, and exact coverage

I am distinct from the listed authors/assembler `/root`, `/root/transport`,
`/root/population`, `/root/nonlazy`, and selector `/root/selector`. I used the
neutral scientific assignment and the frozen inputs below. I did not read a
study README, research history, previous verdict, author check, other review,
or live author source. I did not contact another reviewer or delegate any
part of this review. No candidate or Git writes and no training experiments
were performed. The sole review artifact is this assigned report.

The review covered the full addition, including every proof body, all complete
supplied mathematical dependencies, the entire proposed guide, and all five
old/new global replacements. An initially truncated combined tool display was
repaired by reading the affected files in separate complete chunks.

| Input | Exact coverage | SHA-256 |
|---|---|---|
| `P1_ADDITION.md` | Lines 1–1416; complete reads of 1–355, 356–725, 726–1090, 1091–1416 | `fc613e20c3ee502fcacfbfeeab87d8b9ea5145cf80afad48a8a5ef8b18a56f0b` |
| `P1_DEPENDENCIES.md` | Lines 1–1310; complete reads of 1–330, 331–670, 671–1020, 1021–1310 | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |
| `P1_DOCS_README.md` | Lines 1–269, complete | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| `P1_GLOBAL_EDITS.json` | Lines 1–22, all five replacement objects | `bd802de5b3a69d1c903eb1454f7a5d353195e340ceb16a63ba85de9c820e369a` |
| `P1_SCIENTIFIC_ASSIGNMENT.md` | Complete | `db876bce25296c037246f578df903b4d39c4cf048d7e2616d407e8e001290e19` |
| `P1_MANIFEST.json` | Complete | `10c04c581f72aaa11eb9ddb7fabd1b958cd5b82d5052ae9903f529c4f69f1c06` |

All four scientific-input hashes equal the corresponding manifest entries.
The assembled/baseline files and live-dependency hashes are not a substitute
for these reads and were not used as scientific evidence. The neutral
assignment expressly permits excluding the unchanged chapter complement.

I also read the following required skills and applicable references in full:

| Instruction source | SHA-256 |
|---|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

## Reconstructed claim and contract

The target is the actual two-hidden-layer, width-n tanh network with full
first rows in R², stored readout, Gaussian variances `(1,1/n,1/n²)`, unhalved
mean squared loss, and stored-weight mobilities `(n,1,n)`. The data space is
the normalized circle with bounded labels and metric `|u-u'|+|y-y'|`.
The horizon is one positive interval determined only by Y and the fixed
model. The construction admits every probability law on this space.

The claimed population state is infinite dimensional: the full first-row
L² field, one bounded middle action, and the readout L² field. The initialized
action is fixed by joint finite Gaussian programs and its reverse is its
actual adjoint. The autonomous equation evolves this current state; source
histories are a proof device, not prescribed future forcing. The claimed
restart domain consists of reached states and continuations on the remaining
local interval in the stated bounded class.

The law comparison is in the full state sum norm, with forward observations
uniform in input and time. The finite-network limit is in probability for
uniform predictions and paired activation-displacement observables, along
arbitrary relative sample/width/step growth. It does not compare finite and
population operators in operator norm. The statistical result is
`sup_t |E(gap(t))|`, not either `E|gap|` or `E sup_t |gap|`.

The activity claim is positive averaged squared activation displacement at
a fixed positive physical time on a relative open family of laws. It is not
a fitting or useful-risk theorem. These distinctions are maintained in the
statement and proof.

## Dependency reconstruction

**Finite dynamics §§1–4 and the notation contract: pass.** Differentiating
`f=c^T h²/n` gives first-block gradient `δ¹u^T/n`, middle gradient
`δ²(h¹)^T/n`, and readout gradient `h²/n`. Multiplication by `(n,1,n)`
and the derivative of the unhalved mean squared loss gives exactly (T2),
including the finite rank-one representative `δ²(h¹)^T/n`. The full first
row is used directly, so the incidental reference in the dependencies to a
different isometric first coordinate does not require an omitted theorem.
The finite energy, continuation and initial-norm arguments are correct in
their stated scopes; the new GD argument does not assume their GF energy
identity for Euler updates.

**Gaussian programs III.F.1–6: pass.** The adaptive conditioning proof
conditions on the transcript before exposing a matrix answer; this preserves
the product of residual Gaussian matrix factors. The minimum-Frobenius-norm
conditional mean satisfies both forward and reverse constraints. The
projected fresh-noise error has normalized expected squared norm equal to a
fixed rank divided by n. Conditional bounded-test concentration and the
separate second-moment calculation yield joint W₂ convergence.

The response formula follows by subtracting the old forward projection and
using Gaussian integration by parts against the reverse-source covariance.
The correction cancels the old response terms exactly. Fresh independent
oriented source groups do not mean independent forward/reverse answers.
Regularizing every fixed query with its own fresh Gaussian input gives
strictly positive limiting Schur complements. The fixed-program RMS error
is O(ε) on the Gaussian operator event. Passing ε to zero through covariance
square roots and integrable derivatives does not require continuous
pseudoinverses. The causal scalar-feedback extension also preserves the
fixed-program qualification.

**III.F.7–9, common actions and strong calculus: pass.** The countable
generated language has compatible finite joint laws. Norm inequalities,
finite linear identities, and density of its smooth cylinder functions give
well-defined bounded actions on the generated L² spaces. Passing the finite
transpose pairing first on generated nodes and then by density proves
adjunction. No arbitrary independently sampled operator extension is needed.
The rank-one Hilbert–Schmidt norm and difference formula justify learned
increment integrals. The multiplier and curve chain rules need only the
stated strong convergence and bounded continuous multiplier; they do not
assert Fréchet differentiability of the nonlinear map on an L² ball.

**A.1–A.2, nonlinear value and response extensions: pass.** Continuous
at-most-linear coordinate maps preserve W₂ convergence because squared
outputs are uniformly integrable. The order of prefix approximation avoids
requiring a uniform Lipschitz constant for all clips. For each fixed neural
program, source derivatives of the clipped backward products have finite
polynomial envelopes in subGaussian roots and a finite Gaussian source
tuple. This gives uniform integrability and identifies the response
coefficients as clips are removed. It does not supply an unwarranted
all-moment empirical theorem for a growing transcript.

**C.2 weighted response/tail proof: pass.** I checked the exact forward and
reverse response decompositions, including their separate initialization
variance factors and trained-memory terms. The forward-slot derivative-row
sum obeys a causal Gronwall inequality whose random coefficient is a weighted
sum of individual backward magnitudes. A single reverse-slot pulse enters
the forward recurrence with its own factor `Δω_b`; this factor survives
the derivative bound. The resulting constants contain neither `1/ω_b` nor
a Gaussian maximum over samples or history.

The field/response cap selection is noncircular: forward-response caps are
chosen bottom to top, backward-response caps top to bottom, and then the
positive time is reduced. Within one Euler step the current lower forward
state precedes its forward response and the current upper backward state
precedes the next backward response. Jensen's weighted exponential estimate
does not need independence among samples or times. It supplies the Gaussian
RMS tails needed here uniformly in finite atom count, weights, Gram rank and
proof mesh. The variable-step extension correctly treats a single affine
interpolation time, without taking a random path supremum.

## Candidate proof audit

| Component | Verdict | Main reason |
|---|---|---|
| Exact finite field and local bounds, C.4.1 §1 | Pass | Correct normalization and simultaneous updates; full-row RMS and middle operator norms control all forward fields; the velocity bound supplies a law-independent Euler/GF ball. |
| One-reference transport, C.4.1 §2 | Pass | Both changes in data and state are controlled, including the explicit input factor in the first-row gradient; only weighted individual reference tails occur. |
| Common strong population flow, C.4.2 §§1–5 | Pass | Common action realization, strong integrability, finite-law Euler completion, and then law completion identify the full integral equation. |
| Uniqueness, restart and quantitative modulus, C.4.2 §6 | Pass | Reference tails suffice even when a competing solution has no tail hypothesis; cutoff removal closes uniqueness and restart. |
| Actual GD and joint limits, C.4.3 §§1–4 | Pass | Same-array finite proxy, vanishing actual random readout, fixed-program identification, direct arbitrary-law comparison, and explicit limit order. |
| Replacement and expected gap, C.4.3 §5 | Pass | Replacement transport cost is at most `(2+2Y)/m`; the ghost exchange has the stated expectation/supremum order. |
| Paired representation limit, C.4.3 §6 | Pass | Joint time-zero/current second moments and input/time nets establish the observation itself, separately from prediction convergence. |
| Actual-flow activity and open family, C.4.4 | Pass | Correct physical expansion and positive adjunction identities; transport continuity and paired finite limits transfer the positive margin. |
| Guide and five global scope edits | Pass | The C.4 claims remain local and model-specific, with no stronger generalization, fitting, activity or rate assertion. |

The following details were material to these conclusions.

1. In (T10) one cuts off the reference multiplier, obtaining
   `2R ||Z-Zbar||₂ + 2τ_R(Pbar)`. Passing from δ² through A* to δ¹
   does not multiply two cutoff factors: the earlier backward error is
   propagated by a bounded operator and bounded gate, while the new gate
   produces an additive R term. Thus the transport coefficient is O(1+R),
   as required for the claimed nearly linear law modulus. The vector u in
   the first-row gradient is also varied explicitly.

2. A continuous data-indexed integrand has compact, separable range, so its
   Bochner integral is well defined even in the ambient bounded-operator
   space. Rank-one continuity also holds in Hilbert–Schmidt norm. Joint
   state/law continuity (P9) follows by splitting a coupling at a small
   distance threshold. Completion is in `C([0,T_*]; E)`, not merely in
   scalar predictions. Passing the assigned Euler velocities through this
   continuity yields a strongly C¹ integral solution.

3. The continuum-law tail transfer uses bounded clipped exponentials and
   integrates over the approximating law before removing the exponential
   cap. It proves an integrated exponential moment, which is exactly enough:
   Cauchy–Schwarz in the data law turns it into (P18). No continuum-wide
   pointwise subGaussian conclusion is assumed. For equal initial states,
   comparison gives `C exp(aR-cR²)`; sending R to infinity proves uniqueness
   against any strong competing solution in the ball. Restarted Euler
   trajectories can use the already reached solution as their reference,
   so no fresh response-tail theorem from arbitrary restart states is hidden.

4. With `q<=1`, choosing `R=K sqrt(log(e/q))` and `cK²>=2` makes the
   Gaussian remainder at most q². The polynomial cutoff prefactor is
   absorbed into the exponential in `sqrt(log(e/q))`. This expression tends
   to zero as q tends to zero. The proofs separately treat q=0 and q>1.

5. In (A3) the finite proxy includes the actual random readout additively,
   whereas its deterministic-coefficient oracle has zero readout root.
   Its squared RMS expectation is exactly n⁻². The forward and reverse
   finite contractions in (A4) converge at each fixed reference law and
   proof mesh. The cutoff estimate (A5) supplies consistency for the
   otherwise unbounded backward product. Rank-one norm bounds give the
   assigned-velocity consistency in the same-width full-state metric.

6. The o_P(1) terms in (A7) involve only the fixed reference program and
   initialized arrays. Actual-data atom count and actual fine-step history
   do not enter those errors. For a desired tolerance one can first fix R,
   then fix a finite reference law and proof mesh, and only then send the
   actual sequence index to infinity. This validates arbitrary relative
   sample/width/step growth. Recomputing forward fields at appended passive
   inputs and interior interpolation times identifies parameter
   interpolation, rather than interpolation of feature or prediction values.

7. The compact observation-space partition proof of empirical W₁
   convergence is valid for atomic and singular laws. The reference
   comparison is uniform in the actual training law on the event of small
   empirical W₁ error. This, and the law-independent initialization event,
   justifies the iid conclusion without a growing-data Gaussian-program
   theorem. Bounded and uniformly input-Lipschitz squared residuals then
   justify both risk limits.

8. At each fixed time the exchange of `(Z_i,Z_i')` converts the ghost loss
   into the loss of the replaced-sample algorithm evaluated at `Z_i`.
   Uniform deterministic replacement stability bounds its expected
   difference. Taking the time supremum afterward is valid and gives
   precisely (A13). This derivation would not justify moving either an
   absolute value or a time supremum inside the expectation.

9. For the activity reference, `p=Y/4`, the independent upper initial
   Gaussians have variance `q_0=E tanh²(g)>0`, and the readout derivative
   is `2S`. Thus δ²/t tends to `2U_a`; integration gives lower
   preactivation increment `2t² p b(g_a)P_a`, matrix increment
   `2t² sum_b p U_b tensor h_b`, and activation coefficients exactly
   as in (6). No second Fréchet derivative is required. Adjunction gives
   `<h_a,P_a>=p E[ξ_a tanh(ξ_a)b(ξ_a)]>0`, proving lower activity.
   The identity
   `p sum_a <U_a,R_a> = p² q_0 sum_a ||U_a||² +
   p² sum_a E[b(g_a)²P_a²] > 0`
   prevents cancellation of both upper-layer motion coefficients. Both
   moving-matrix and moving-lower-feature terms are retained.

10. The definition of s₀ from the actual small-time expansion yields a
    positive t₀ strictly inside the interval where both lower bounds hold.
    A squared-displacement change costs at most `4 C_H ω(q)+8B²q`;
    hence the selected open W₁ ball has a common positive margin. Including
    both time-zero and current activations in the fixed oracle's joint
    second moments transfers this margin to the finite networks. A positive
    limit of at least j₀/2 implies probability tending to one for either
    a strict or non-strict threshold j₀/4.

## Adversarial cases and outcomes

| Attack | Actual check and outcome |
|---|---|
| A law supported on one direction | The full w row, including its unused Gaussian component, remains in the state; forward input continuity follows from its full RMS. No division by the active Gram is used. |
| Duplicate or coincident inputs, incompatible labels | The vector field is an integral over joint observations and remains defined. The fixed-program regularization covers the associated singular query Grams. No interpolation claim is needed. |
| A new atom of arbitrarily small weight ε | The C.2 source pulse is proportional to `Δε`; all tail integrals retain the same weight. No inverse weight or count-dependent maximum occurs. The transport contribution is O(ε) before cutoff optimization. |
| Singular Grams and nearly dependent inputs | Covariance square-root continuity, rather than pseudoinverse continuity, removes fixed-program regularization. The law comparison uses full-row norms and operator norms only. |
| Passive directions far from the training span | Full-row control gives `||Z¹(u)-Z¹(v)||₂ <= B|u-v|`; bounded actions propagate this to the second layer and predictions. Fixed input nets may be appended without becoming training observations. |
| Zero signal | If `E[y|x]=0`, then c=0, w=g and A=A₀ solve the population equation: the readout integral vanishes and both hidden gradients vanish. Uniqueness makes this stationary. This is consistent with activity being asserted only on the stated open family. |
| Nonzero labels with cancellation | Symmetric opposite inputs with equal labels can also have a cancelling initial readout update because the network is odd. The proof does not assert universal activity or fit and is not contradicted by this case. |
| q=0 and q>1 | Equal laws give equal flows. For q>1 bounded predictions give 2B directly; no out-of-domain logarithm is needed. |
| Small m, including m=1 | Use the uniform predictor bound and enlarge the constant for finitely many small m. For large m the unspecialized cutoff estimate with `q<=(2+2Y)/m` proves the bound directly. |
| Actual random readout | Its RMS, rather than its largest coordinate, vanishes. The proxy shares it exactly at initialization, and its effect is retained in the consistency estimate. |
| Extremely slow width growth and fast sample/step-count growth | Only a fixed auxiliary reference law and fixed coarse mesh use a width theorem. The actual arrays enter a uniform deterministic comparison. No relative-rate condition is introduced. |
| State-space/topology escape | The flow is completed in the full strong state topology. Learned increments are strong Hilbert–Schmidt integrals. No bounded-set compactness in an infinite-dimensional norm is assumed. |
| False generalization strengthening | The ghost calculation retains `sup_t |E gap|`. It provides no expectation of the absolute gap, expected path supremum, excess-risk rate, or useful-risk guarantee. |
| Activity caused only by readout motion | The actual-flow coefficients for both hidden activation displacements are nonzero by adjunction, with a width-independent positive physical time and margin. |

## Required corrections, optional suggestions, and limits

**Required corrections: none.** Every necessary bridge of the stated theorem
is provided by the candidate and its complete frozen dependencies.

Optional editorial suggestions, neither of which affects the proof:

* At `P1_ADDITION.md` line 745, replace “The maximum possible distance”
  with “The maximum possible training-law W₁ distance” to make the intended
  referent explicit after a sentence about the state distance D.
* In C.4.3 §5, the direct unspecialized cutoff proof already handles the
  replacement estimate. It could be used alone to avoid the parenthetical
  reference to a “nondecreasing enlarged modulus”; the displayed formula
  itself need not be monotone on all of `(0,1]` for an arbitrary enlarged C.

The guide's new C.4 descriptions and all five global replacements match the
proved model and local horizon. The guide's unrelated chapter inventory and
literature orientation are contextual text; no claim from them was used to
close a gap in this theorem, and this review does not reprove the unrelated
library or verify its contextual bibliography.

Acceptance does not establish quantitative finite-width or finite-step
rates, useful risk reduction, fitting, endpoint selection, global-time
control, universal activation activity, or a depth-uniform theorem. The
candidate expressly excludes these extensions. There is no remaining
scientific blocker within the requested frozen scope.
