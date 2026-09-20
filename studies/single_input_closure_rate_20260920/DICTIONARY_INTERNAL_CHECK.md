# Internal check of the quantitative H3 dictionary argument

Verdict: PASS for the mathematical approximation-order theorem in the frozen
candidate. The integer thresholds are explicit and do not use the target path.
This check does not establish an additional algorithm or error rate for
computing the rational Gaussian-moment witnesses. Existential choices suffice
for the theorem, as the assembly expressly states.

Reviewed candidate: `ROUTE_DICTIONARY.md`, SHA256
`c894744d37cd0e2eb5adcf2524dce26507748a23fed84b69ef8fd0645902ea1c`.
Every section of that version was read. This is an internal component check,
not a fresh isolated promotion review. The reviewer authored the separate
feature-dynamics component, but did not author this dictionary candidate.
The parent's favorable preliminary-check status was disclosed before the
review; it was not treated as evidence. A coordination `list_agents` call
also unexpectedly exposed an unrelated completed task's status summary.
No scientific content from that summary was used in this check or either
earlier frozen report. Inputs used here are the assigned candidate, the same
study's contract, and the maintained grammar/source/filter equations.

No numerical experiment was needed. The checks below reconstruct the estimates
and their logical dependencies, rather than relying on observed accuracy.

## 1. Exact model and approximation family

The candidate retains the canonical two-hidden-tanh population, the full
first-row Gaussian pair, the actual initialized Gaussian action and its
adjoint, and the one-input feature equations obtained from the physical
unhalved-loss flow. The inverse primitive `F` is used as a proof coordinate.
The operational closure remains C.4.7.10.B's degree-plus-bounded-code-prefix
dictionary with ridge `1/[1024(N+1)^2]` and its original nonlinear equations.

The Euler programs constructed in the proof are approximation witnesses for
fields on the initialized carrier. They are not installed as runtime time
tables or substituted for the autonomous closure. Their coefficients depend
on finite initialized Gaussian programs, not on the exact trained trajectory.
The final order bound is uniform over all allowed coefficient roundings, so
even those finite-program moment values need not be known to choose the order.

## 2. Inverse-gate compiler

The primitive satisfies `F'=cosh^2>=1`, and its inverse-coordinate map obeys
`|J(g,V)-g|<=|V|`, `|partial_V J|<=1`, and
`partial_g J=cosh^2(g)/cosh^2(J)`. Thus for `|g|<=R`,
`|partial_g J|<=exp(2R)`, independently of the value of `V`.

The clamp function `r_R` is globally Lipschitz with constant less than `4R`.
After substituting `x=tanh(field/R)`, it equals the original field when
`|field|<=R` and clips it otherwise. The output discrepancy outside the
three-coordinate box is at most two. Markov's inequality and the union bound
therefore give its `L2` error at most

\[
 \frac{2\sqrt{1+1+1500^2}}R<\frac{3002}R<\lambda/16,
 \quad R=2^{16}/\lambda.
\]

This uses no independence between the constructed field `V` and the seeds.
On the clipped cube the composed function has `l1` Lipschitz constant at most
`4R exp(2R)`. The tensor Bernstein expectation has each coordinate's standard
deviation at most `1/sqrt(n)`. Consequently its uniform error is at most
`12R exp(2R)/sqrt(n)`, and the declared value of `n` makes it less than
`lambda/16`, since `exp(2R)<=2^(4R)` and `12/256<1/16`.

Rationalizing the scalar samples to denominator `16/lambda` adds at most
`lambda/16`. Nonnegative Bernstein weights sum to one, so the global output
bound `1+lambda/16` holds even outside the clipped input box. The three error
contributions are less than `lambda`; the compiler therefore satisfies its
stated bound with slack.

All runtime polynomial multiplications have bounded operands. The inverse,
clamp, and real Bernstein sample function are used only to define fixed
scalar coefficients. The actual passive grid directions are rational. Thus
their scalar sample values can be approximated by elementary interval
evaluation and monotone inversion without a hidden noncomputable input mark.
The arbitrary-real-direction version is only an existence statement; the
constructive witnesses use the declared rational grid.

The crude count `100(n+1)^4` covers the `(n+1)^3` Bernstein terms, powers,
products, scalar multiplications, and additions. The product of three binomial
coefficients is at most `2^(3n)`. Sample numerators have magnitude at most
`16/lambda+1`; inverse input scales have denominator `R`. All are safely below
the displayed numerator/denominator envelope `Acoef`.

## 3. Finite initialized-word Euler construction

Each action in the witness recursion has a bounded operand: `h_j` is bounded
by two, and `Delta_j` by `s_j<=6`. The clocks and reverse answers may be
unbounded `L2` words, which the grammar permits as inputs to the bounded
elementary gates. Products are taken only after boundedness has been obtained.
The reverse rank expansion uses exactly the adjoint of the stored forward
rank expansion. No independent transpose source is substituted.

Inductively `||c_j||infty<=s_j`. Since `||h_i||2<=2`,
`||K_j||HS<=h sum_(i<j)2s_i<=s_j^2<=36`. Hence the action norm is at most
38. The exact adjoint action on `Delta_j` has `L2` norm at most `38*6=228`;
the rounded reverse contraction sum adds at most `12 lambda`. Integrating
over length six gives `||V_j||2<=1440`, making the gate compiler's hypothesis
valid at every step without a bootstrap gap.

The forward contraction error is at most `36 lambda`, and replacing the
gate contributes at most `38 lambda`; thus the upper-activation error is at
most `74 lambda`. The upper-backward error is at most `12*74 lambda=888 lambda`.
The total three-block velocity error is bounded by

\[
 (38\cdot888+12)+(2\cdot888+6)+74=35612<40000
\]

times `lambda`, exactly as required. At the witness state, the unmodified
transformed vector field is compared in the same carrier and same increment
metric as the target; rounding has not changed the reference action or norm.

On the common readout/action ball, the candidate's field differences sum to
`17828+475+39=18342<20000` times the state distance. The chosen `L=20000`
therefore suffices. The target speed is below `M=300`. Its local exact Euler
remainder is at most `(LM/2)h^2`, obtained by integrating the Lipschitz field
along the exact curve. With `h=lambda`, the discrete error recurrence gives

\[
 \max_j E_j\le6e^{120000}(40000+3000000)\lambda.
\]

Using `e^{120000}<2^{240000}` and `6*3040000<2^{25}`, while
`lambda=2^{-(k+400000)}`, leaves substantially more than the claimed factor
`2^{-100}2^{-k}`. The proof controls a finite positive feature interval; it
does not infer trajectory convergence from formal coefficient correctness.

## 4. Finite-program fourth moments and saturation

The fourth-moment argument is essential: boundedness of the action as an
`L2` operator alone would not supply the proposed saturation rate.

For any fixed initialized program, the maintained source rule expresses an
action answer as a centered Gaussian source plus at most `W` earlier
opposite-orientation bounded operands multiplied by expected frozen named-source
derivatives of its input. If preceding supremum, derivative, and `L4` bounds
are `E_r`, its source has standard deviation at most `E_r` and `L4` norm
less than `2E_r`. Its response terms have total `L4` norm at most `W E_r^2`.
The corresponding formal named-source derivative is bounded by
`1+W E_r^2`, because all covariance and expectation coefficients are frozen.

This verifies the proposed action-node induction. Rational operations,
bounded products, and sin/cos/tanh satisfy smaller bounds. The recurrence
`4(W+1)(Acoef+1)(E_r+1)^2` dominates all cases. Correlated or singular
Gaussian source families cause no problem: only each source's scalar fourth
moment and triangle inequalities are used, and the exact finite-source rule
already allows singular Grams.

For the saturation, integrating `1-tanh'=tanh^2` on `|x/Rb|<=1`, and using
the elementary bound on its complement, verifies
`|x-Rb tanh(x/Rb)|<=x^2/Rb`. Hence `L4<=E` gives an `L2` saturation error
at most `E^2/Rb=2^{-k}/1024`. The new output is a bounded grammar word.
This is a moment bound for the finite proof program, not an unproved tail
assertion for the exact trajectory or all closure states.

## 5. Actual numeric code and positive ridge

The total DAG count `W` bounds both the quadratic number of training
contraction terms and the time-by-square-grid passive compiler calls. At most
three new nodes saturate any needed action output, so `4W` is a safe final
count. The rational scales for saturation are bounded by `Afinal`.

A rational with numerator and denominator bounded by `Afinal` has signed
numerator index at most `2Afinal` and denominator index at most `Afinal`.
Its Cantor index is therefore below `(4Afinal+4)^2=M0`. If earlier word
codes and rational indices are at most `M`, then unary instructions and
binary Cantor-paired instructions have code below `64(M+1)^2`. This validates
the finite recursion through `4W` nodes. DAG sharing is harmless: the actual
tree code is obtained recursively from preceding codes, and this recursion
bounds that code even when tree expansion is much larger than the DAG.

Every approximation witness retained for the proof is itself a bounded
output code, rather than an unretained dependency. Thus it is present in the
H3 prefix whenever `N>=N_k`, or is already literally in the polynomial core.
It can be selected by a raw coefficient vector with one unit entry. The ridge
estimate therefore reads

\[
 \|(I-Q_N)\psi\|_2\le\sqrt{\eta_N}/2=1/[64(N+1)],
\]

without dependence on Gram conditioning or the potentially enormous supremum
bound of that single word. Positivity and contraction give `||I-Q_N||<=1`,
so transferring a field to its witnessing raw feature loses only its
approximation distance plus this ridge term. No arbitrary large expansion
coefficient norm is hidden here.

## 6. Time/input nets and the four projection estimates

The exact transformed state moves by at most `300 lambda` between a time
and its preceding grid point. Its raw first row has `L2` norm below 200, and
every unit direction is within `2/m` of the square grid. The resulting
passive first-feature error is at most
`400/m=(400/2^20)2^{-k}<2^{-k}/1024`.

At a time node, the first-feature witness error is at most `E_j+lambda`;
the training upper-backward witness error is at most
`469E_j+888lambda`. Its time modulus is at most `469*300lambda`.
Applying `A0` or its actual adjoint multiplies the corresponding error by at
most two. Adding the saturation error `2^{-k}/1024` and ridge error
`<2^{-k}/65536` still leaves ample room below `2^{-k}` for each of the four
projection bounds. The `E_j<=2^{-100}2^{-k}` and lambda bounds make all
remaining terms negligible within those deterministic inequalities.

Thus the candidate proves, uniformly on feature time `[0,6]`,

\[
 \|(I-Q_1)H^1(u)\|_2,\quad
 \|(I-Q_2)\Delta(e_1)\|_2,\quad
 \|(I-Q_2)A_0H^1(u)\|_2,\quad
 \|(I-Q_1)A_0^*\Delta(e_1)\|_2\le a=2^{-k}.
\]

The whole circle occurs in the two forward quantities. The reverse quantity
is required only at the sole training input. This is sufficient for the
prediction theorem; it should not be read as a rate for every passive
reverse-query observable in the broader maintained observation language.

The two initialized-action errors are consequently at most `3a` each.
For `K_s=Delta tensor H^1(e1)`, subtracting its two filtered factors gives
`a*1+6*a=7a`. Hence the feature-time source sum is at most `13a`.
Shifting from `N_k` to `N_(k+4)` gives the normalized bound `rho_N<=2^{-k}`
because `13/16<1`. All bounds persist at every larger order.

## 7. Direct closure propagation and fixed physical time

The retained-state flow uses exactly `B_N=Q2 A0 Q1`, the filtered learned
rank velocity, and both action orientations. Subtraction yields the displayed
source constants: upper-backward source `36a`, lower-clock source
`38*36a+3a=1371a`, middle source `36a+7a=43a`, and readout source `3a`.
The resulting total is below `20000(e_N+a)`. Its integrated bound in the
candidate is loose but valid.

Prediction subtraction gives `235 e_N+18a`. Since `235*120000=28200000`,
the chosen `Cfeat=30000000 exp(120000)` is sufficient. The prediction's
feature-time derivative is bounded by
`1+6(6+38*228)=52021<71000`, for either target or closure.

The single-input feature prediction is nondecreasing by the coefficient-space
gradient identity. The physical scalar clock starts at derivative two and
cannot pass a first equilibrium `f=1`; hence `0<=s(t)<=2t`, including if
that equilibrium does not exist within the displayed feature interval.
For physical `T=3`, both clocks remain in `[0,6]`. Their difference obeys
the claimed scalar Gronwall estimate with exponent `2*71000*3=426000`.
The fixed-physical-time rate follows with the displayed `Cphys`.

The recursively defined `N_k` increases and is unbounded: all component
integer scales increase with `k`, all recursions are monotone in their positive
arguments, and `N_k>=2^(k+10)`. Taking the greatest admitted `k` therefore
gives a vanishing staircase. No monotonicity of actual closure error is needed.

## 8. Effectivity boundary and findings

The scalar Bernstein samples used by the gate compiler are elementary
computable numbers at the rational grid. The later finite-program Gaussian
expectation roundings are more delicate at adaptive singular Grams. The
candidate's instruction to approximate such an expectation to `lambda/4`
is not, by itself, an independently established certified quadrature algorithm.

This is not a gap in the mathematical rate: every finite expectation has a
rational approximation with the declared error and numerator/denominator bound.
The threshold uniformly includes every such choice, and no moment value or
choice is queried in its definition. The assembly explicitly adopts this
existential proof-witness interpretation and does not claim a coefficient-
quadrature rate. Under that stated interpretation the approximation-order
theorem is proved.

No material correction is required to the rate proof. Its complete-word
prefix is essential; this check supplies no positive rate for polynomial
degree alone on a fixed Gaussian core. The result concerns exact population
closure order, leaving numerical integration, arithmetic, time discretization,
and neural-width errors as separate axes.
