# Debiasing independently trained block hierarchies

This is a bounded, prompt-only theoretical design assessment. Scientific inputs
were the supervisor's assignment and `docs/notation.qmd`; no other study,
external source, or experiment was used. The mathematical-proof and
conjecture-analysis skills governed the derivations. All new results below are
internal and conditional where indicated.

**Conclusion.** A signed ensemble of independently trained widths is an
implementable candidate for cancelling block-width bias, while preserving
block-Gaussian initial actions and globally learned updates. Richardson
cancellation requires a trained-observable expansion that is not supplied by
ordinary dense-population existence. Multilevel telescoping avoids that
expansion assumption, but still requires convergence to the dense trained
target. Unbiased randomized telescoping additionally needs sufficiently fast
coupled mean-square decay relative to work. None of these bridges follows from
the supplied assumptions alone.

## 1. Object and clock

Fix the finite training data, depth, tanh activation, zero stored readout,
positive initial training-Gram gap, and small fixed labels in the assignment.
Use the mean squared loss and canonical mobilities in `docs/notation.qmd`.
In particular, a network of total width `n` uses first-layer and readout
mobilities `n κ₁` and `n κ_{L+1}`, and hidden mobilities `κ₂,…,κ_L`.
Changing block size or total width does not authorize fitting a new time scale.

Let `X_*` be a fixed finite set of test inputs, with no target test labels
available to the construction. Write `F(t) ∈ R^s` for the canonical dense
population predictions on these inputs. Its final prediction is
`F(∞) = lim_{t→∞} F(t)`, **when this limit is established**. Ordinary existence
of the dense flow does not itself establish that limit. Training interpolation
alone would not identify a test prediction.

At width `n = Bk`, initialize each hidden matrix with `B` independent aligned
Gaussian `k × k` blocks of entry variance `1/k`; first-layer Gaussian rows are
independent, and the readout is zero. Thereafter all learned updates are global.
Let `Q_{k,B,q}(t)` be the resulting test prediction from a specified response
closure and time solver; `q` denotes the retained response/history budget.
Its initialization and any numerical randomization are included in its law.
All levels are compared at the same physical time `t`. Final predictions mean
that every component is actually taken to its own physical-time limit.

If an exact structured-population prediction `F_k(t)` exists as `B→∞`, define
its block bias `b_k(t) = F_k(t) − F(t)`. Otherwise the exact finite estimators
below remain meaningful using their means, but no structured-population bias
has yet been defined. When useful, decompose

`Q_{k,B,q} = F + b_k + e_{k,B,q} + ξ_{k,B,q}`,

where `e = E Q − F_k` contains finite-block-count, closure, and time-solver
bias, and `E ξ = 0`. Independence of initial blocks does **not** make the
trained blocks independent: their residual and learned updates are global.
Thus a bound such as `E||ξ||² = O(B⁻¹)` needs a separate interacting-system
argument. It cannot be imported from independent sample averaging.

## 2. Richardson and signed mixtures: exact consequences

Train the `k` and `2k` systems separately, each using its own residual against
the same training labels, and form the test-output ensemble

`R_k(t) = 2 Q_{2k,B₂,q₂}(t) − Q_{k,B₁,q₁}(t)`.

Assume, explicitly and additionally, the trained expansion

`F_k(t) = F(t) + c(t)/k + ρ_k(t)`, with `||ρ_k(t)|| ≤ C/k²`.

Then cancellation is exact algebra:

`E R_k − F = 2ρ_{2k} − ρ_k + 2e_{2k} − e_k`,

and consequently

`||E R_k − F|| ≤ 3C/(2k²) + 2||e_{2k}|| + ||e_k||`.

The remainder constant and expansion must apply on the requested physical
horizon. An expansion at initialization is not an expansion after training.
For coupled realizations, put `V_j = E||ξ_j||²` and
`C_{12} = E⟨ξ_k,ξ_{2k}⟩`. The exact mean-square error is

`E||R_k − F||² = ||E R_k − F||² + 4V_{2k} + V_k − 4C_{12}`.

Independent runs give `C_{12}=0`; coupling can help or hurt and must be
measured or bounded. In particular, cancelling deterministic bias does not
cancel stochastic or closure errors automatically.

More generally, if the first bias is `c(t)k⁻ᵖ` with a **known, proved** exponent
`p>0`, use

`R_k^{(p)} = [2ᵖ Q_{2k} − Q_k]/(2ᵖ−1)`.

A remainder bounded by `C k^{−p−δ}` yields block-bias bound
`C(1+2⁻δ) k^{−p−δ}/(2ᵖ−1)`. Its coefficient norm is
`(2ᵖ+1)/(2ᵖ−1)`, which also controls worst-case amplification of equally
bounded implementation errors. For levels `a_j k`, a deterministic mixture
`Σ_j w_j Q_{a_j k}` preserves the target term exactly when `Σ_j w_j=1` and
cancels a `k⁻ᵖ` term exactly when `Σ_j w_j a_j⁻ᵖ=0`.

With `w_j≥0`, finite `a_j>0`, and `Σ_j w_j=1`, the last sum is strictly
positive. Thus a positive mixture cannot cancel a common nonzero leading
bias coefficient. This is a statement about this expansion, not a theorem
that positive mixtures can never improve prediction. Signed weights permit
the algebraic cancellation, at a variance and robustness cost.

Without an expansion, the only unconditional deterministic Richardson identity
is `R_k−F = 2b_{2k}−b_k` for exact component predictions. Even convergence
`b_k→0` provides no improved order. For example, an abstract convergent bias
sequence `b_k = v/log k` retains its leading order after this transformation.
This sequence is a logical counterexample to inferring acceleration from
convergence alone; it is not asserted to be a realized tanh-network bias.
Ordinary dense-flow existence supplies even less than convergence of `b_k`.

## 3. Separate training is essential to this identity

The preceding ensemble is formed after each component follows its own
autonomous gradient flow, including its own global residual. It is itself
restartable by retaining the product of those finite component states.

Training a mixture under a common residual is a different dynamical system.
Already for scalar models with positive rates `a_j`, separately trained
solutions of `ḟ_j = −a_j(f_j−y)`, `f_j(0)=0`, give

`Σ_j w_j f_j(t) = y[1−Σ_j w_j exp(−a_j t)]`.

If instead `ḟ_j = −a_j(g−y)` and `g=Σ_j w_j f_j`, with positive weights
summing to one, then

`g(t) = y[1−exp(−(Σ_j w_j a_j)t)]`.

These are generally different. Actual joint gradient descent through a signed
output also inserts the signed coefficient in each component's derivative.
Therefore Richardson weights cannot simply be put into a common-residual
architecture while retaining the separate-flow bias cancellation proof.
Any useful common-residual construction needs its own limiting equation and
its own expansion.

## 4. An exact Gaussian antithetic coupling

A concrete paired initialization is available without querying the dense
trajectory. For each layer and fine `2k × 2k` block, sample independent standard
Gaussian matrices `G₁₁,G₁₂,G₂₁,G₂₂` of size `k × k` and set

`A_f = (1/√(2k)) [[G₁₁,G₁₂],[G₂₁,G₂₂]]`,

`A_c^{(1)} = G₁₁/√k`,  `A_c^{(2)} = G₂₂/√k`.

Do this independently across fine blocks and layers. Split the first-layer
Gaussian rows correspondingly and use zero readouts throughout. The fine
network has `B` blocks and width `2Bk`; each of the two coarse networks has
`B` blocks and width `Bk`. Each coarse network uses its own correctly scaled
canonical mobilities and its own global residual. This gives the exact
prescribed marginal laws at both widths, and the two coarse initializations
are independent of one another, though coupled to the fine initialization.

For any matched numerical settings, define the antithetic increment

`D_k = Q_{2k}^f − (Q_k^{c,1}+Q_k^{c,2})/2`.

Then `E D_k = E Q_{2k} − E Q_k` exactly. A paired Richardson output is
`2Q_{2k}^f − (Q_k^{c,1}+Q_k^{c,2})/2`, with the same Richardson mean as above.

No strong-error rate is established by this coupling. The fine off-diagonal
blocks create order-one Gaussian contributions, while each retained
diagonal block changes normalization. Fine and coarse neuron trajectories
are not automatically close. Antithetic cancellation would require a proved
regularity and averaging property of the *trained* observable. Exact Gaussian
marginals validate the expectation identity, not a variance improvement.

## 5. Multilevel and randomized telescoping

Choose `k_ℓ = 2^ℓ k₀` and explicitly chosen budgets `B_ℓ,q_ℓ` and time-solver
tolerances. Let `Q_ℓ(t)` denote each implementable level, with mean `μ_ℓ(t)`.
Each adjacent pair must have these exact level marginals; the coupling above
is one example when block counts and numerical settings permit it. Put
`D₀=Q₀` and `D_ℓ=Q_ℓ^f−Q_{ℓ−1}^c`; a coarse antithetic average with the same
mean is also allowed. Then, for every finite `J`,

`Σ_{ℓ=0}^J E D_ℓ(t) = μ_J(t)`.

This exact identity does not use a bias expansion. With independent batches
across levels and independent repetitions within each level, the estimator

`Y_J = Σ_{ℓ=0}^J (1/N_ℓ) Σ_{i=1}^{N_ℓ} D_ℓ^{(i)}`

satisfies

`E||Y_J−F||² = ||μ_J−F||² + Σ_{ℓ=0}^J V_ℓ/N_ℓ`,

where `V_ℓ = E||D_ℓ−E D_ℓ||²`. If one pair costs `C_ℓ`, the continuous
allocation minimizing work for variance budget `v` is

`N_ℓ = v⁻¹ √(V_ℓ/C_ℓ) Σ_{j=0}^J √(V_j C_j)`.

This follows directly by applying Cauchy–Schwarz to
`Σ√(V_ℓ C_ℓ) = Σ√(V_ℓ/N_ℓ)√(N_ℓ C_ℓ)`; the displayed choice attains equality.
Rounding positive counts upward gives total work at most

`v⁻¹ (Σ_{ℓ=0}^J √(V_ℓ C_ℓ))² + Σ_{ℓ=0}^J C_ℓ`.

Zero-variance levels can be handled separately. To turn this into an
accuracy theorem one still needs a trained identification/bias bound
`||μ_J−F||≤A2^{−αJ}`. If additionally `V_ℓ≲2^{−βℓ}` and
`C_ℓ≲2^{γℓ}`, the variance-work factor is bounded when `β>γ`, grows as
`J²` when `β=γ`, and as `2^{(γ−β)J}` when `β<γ`. The finest-level rounding
cost must still be included. None of `α,β,γ` is fixed by Gaussian initialization
alone, particularly if response budgets grow with level or horizon.

An exactly unbiased randomized variant can be defined without Richardson.
Independently sample an integer `N≥0` with probabilities `p_ℓ>0`, simulate
one increment with level-`N` law, and output `Z=D_N/p_N`. If

`Σ_ℓ E||D_ℓ|| < ∞` and `μ_J→F`,

then absolute integrability and telescoping give `E Z=F`. Furthermore,

`E||Z||² = Σ_ℓ A_ℓ/p_ℓ`,  `E work = Σ_ℓ p_ℓ C_ℓ`,

where `A_ℓ=E||D_ℓ||²`, including its squared mean. Cauchy–Schwarz gives

`(E||Z||²)(E work) ≥ (Σ_ℓ √(A_ℓ C_ℓ))²`.

For costs bounded below by a positive constant, finiteness of the last sum
allows the choice `p_ℓ ∝ √(A_ℓ/C_ℓ)` on nonzero increments, giving finite
second moment and expected work. Levels known to have zero increment can be
omitted. For bounds `A_ℓ≲2^{−ηℓ}` and `C_ℓ≲2^{γℓ}`, the sufficient condition
is `η>γ`. A central-variance estimate alone is insufficient: a mean-increment
bound must also control `A_ℓ`. The geometric distribution parameter can be
fixed from proved exponents; exact unknown moments are not required.

This removes truncation bias **only if the full implementable hierarchy
converges to the intended trained target**. With no such identification it is
unbiased for an unidentified limit, if a limit exists at all. Each realization
uses finite memory almost surely, but the level and memory are unbounded
random variables; this is not a deterministic fixed-memory debiaser. Imposing
a hard maximum level restores bias.

## 6. Cost and long-time obligations

The assigned memory proxies for one level are

`M_fixed(k,B) = O(L B k²)`,

`M_moving(k,B,q) = O(L m B k q)`.

They describe the sparse initial matrices plus global learned-response
factors, not a permanently block-diagonal trained network. A layer action on
one vector has the corresponding operation bound
`O(Bk² + mBkq)` when the learned part has at most `mq` stored rank-one factors.
Applying these actions to all `m` training samples costs
`O(LmBk² + Lm²Bkq)` per such forward/backward sweep. Response-factor evolution,
time integration, and test evaluations must be accounted for separately if
they cost more. No bounded-in-time `q` is assumed.

With the same `B,q` at both sizes, ordinary two-level Richardson has fixed
memory proportional to `5LBk²` and moving memory to `3LmBkq`; the antithetic
version with two separately trained coarse systems uses respectively factors
`6` and `4`. Each has only constant-factor overhead over its finest level.
If instead every ordinary two-level system has the same total width `n`, so
`B_k=n/k` and `B_{2k}=n/(2k)`, its combined proxies are `3Lnk` and `2Lmnq`.
These are different budget comparisons and should not be conflated. Sequential
multilevel sampling needs the peak memory of one coupled pair, rather than
the sum of all sample memories.

For an unbounded hierarchy with fixed `B`, bounded `q`, and a bounded number
of sweeps per level, the initial-matrix action already gives the work exponent
`γ=2`. The single-term randomized construction would then need a proved
second-moment increment rate with exponent `η>2`. Merely postulating
`A_ℓ=O(k_ℓ⁻¹)` would not meet that sufficient condition, and a matching lower
bound of this order would violate the necessary summability condition.
Antithetic marginal matching supplies neither the required faster rate nor
a counterexample to it. Growing integration and response budgets increase
the work requirement. Holding total width fixed is not an unbounded
`k→∞` hierarchy, since `k≤n`.

The final-predictor claim needs a separate long-time bridge. For example,
define the train and test tangent matrices by

`ṙ = −(2/m) Θ_train(t) r`,
`Ḟ_test = −(2/m) Θ_test(t) r`.

If, for every relevant component and the dense target, one has the uniform
bounds `Θ_train(t) ≽ λI` and `||Θ_test(t)||≤M` for all `t≥0`, then zero initial
prediction gives

`||r(t)|| ≤ ||y|| exp(−2λt/m)`,

`||F_test(∞)−F_test(T)|| ≤ (M/λ)||y|| exp(−2λT/m)`.

The first inequality follows by differentiating `||r||²`; the second follows
by integrating the test derivative and the first inequality. A finite
ensemble's stopping error is amplified by the sum of absolute weights.
These hypotheses establish uniform tails, but still do not produce a
block-width expansion. An initial Gram gap plus small labels is a possible
starting point for proving the hypotheses; it is not their proof.

For Richardson at final time, either prove an expansion directly for
`F_k(∞)`, or establish an expansion uniform in physical time together with
existence of the final limits. A compact-time expansion whose constants grow
with `T` cannot silently be passed to `T=∞`. Multilevel/randomized final-time
claims likewise require final-time identification and moment bounds. If
levels use finite stopping tolerances, those tolerances must vanish in the
hierarchy and be included in the bias and strong-error estimates.

## 7. Concrete proposal and the remaining bottleneck

The immediately implementable candidate is the antithetic pair in Section 4:
train one `2k` system and two coupled `k` systems at matched physical time,
retaining global learned updates within each system, and return
`2Q_{2k}−(Q_k^{c,1}+Q_k^{c,2})/2`. All randomness comes from legitimate initial
Gaussian samples; its fixed coefficients use no dense trajectory or test
labels. It preserves cheap structured actions with the constant-factor costs
above. Its exact claims are the marginal laws, mean identity, and conditional
error formula. **An improved trained block-bias rate is open.**

If the aim is to remove bias without assuming a power series, prefer the
telescoping hierarchy as the mathematical route. The first necessary proof
obligation is a trained-target identification bound, ideally uniform in time,
for the actual finite-block/global-update/response construction. Only after
that bridge is established does a coupled increment estimate decide whether
randomized exact unbiasedness is computationally viable. A positive-mixture
architecture or a shared-residual signed network is a different candidate
and cannot inherit the separate-training argument.

| Claim | Status in this assessment |
|---|---|
| Richardson cancellation given the displayed expansion | Exact conditional algebra |
| Positive weights cannot cancel a common nonzero `k⁻ᵖ` term | Proved under the displayed expansion |
| Antithetic Gaussian marginal laws and increment mean | Exact finite construction |
| Multilevel mean, variance, and allocation identities | Exact under stated moment/independence assumptions |
| Randomized unbiasedness and finite expected work | Conditional on target identification and summability |
| Existence of a trained block-width expansion | Open; not supplied by ordinary dense-flow existence |
| Convergence of the implementable hierarchy to the dense final predictor | Open |
| Fast antithetic variance decay and uniform response-memory budget | Open |
