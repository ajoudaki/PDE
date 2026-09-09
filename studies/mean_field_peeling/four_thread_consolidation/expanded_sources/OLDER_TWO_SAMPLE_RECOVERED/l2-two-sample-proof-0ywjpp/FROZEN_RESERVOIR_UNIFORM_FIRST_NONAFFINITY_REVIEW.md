# Independent isolated adversarial review: frozen-subset first-activation nonaffinity

Review date: 2026-09-06.

## Provenance and isolation

The sole mathematical source for this audit was
`/tmp/l2-two-sample-proof-0ywjpp/FROZEN_RESERVOIR_UNIFORM_FIRST_NONAFFINITY.md`.
It was read entirely: 134 lines, 6,301 bytes. References to source lines below refer to that snapshot.

Expected SHA-256:
`203249b51ba4be6d4b304a9cf81a745bede8a906fa077846a2cfddbcd7aebb5f`

Observed SHA-256:
`203249b51ba4be6d4b304a9cf81a745bede8a906fa077846a2cfddbcd7aebb5f`

The hashes match. The only additional file read was the procedural skill
`/etc/codex/skills/solve-math-rigorously/SKILL.md`, read in full for its proof-verification procedure. No other project files, history, reviews, mathematical sources, or external references were consulted. In particular, the separate audit mentioned in source lines 8–9 was not consulted. No agents, numerical experiments, or simulations were used. The source was not edited. This report was written with `apply_patch` to the user-specified output path. The calculations below are independent analytic checks of the frozen source.

## Verdict and findings

The frozen-subset regression argument is mathematically sound within its stated scope. I found no required mathematical correction to the population inequality conditional on preservation, the empirical probability statement, or preservation under the displayed finite GF/GD rule. The singular endpoint `rho = -1` does not invalidate any of them.

The result is a persistent obstruction to fitting the **first activation across the neuron distribution** by one affine function, separately for each training sample. Its witness is an unchanged subset of the initial Gaussian neurons. It is compatible with completely static paths and with lazy dynamics. It is **not a nonlazy theorem, a global mean-field theorem, a construction of a population flow, or a finite-width-to-population convergence theorem**.

Two optional clarifications would improve the standalone presentation:

| Finding | Status | Source location | Assessment |
|---|---|---|---|
| O1. Specify the coupled population inequality | Optional clarification; necessary if the displayed inequality was intended componentwise | 123–127 | The argument works with the two-component preactivation vector, its maximum norm, and the sum of the absolute total controls. A componentwise scalar reading is generally false. The vector reading is consistent with the source's notation `G` for the Gaussian pair. |
| O2. State the status of the first-row update normalization | Optional specification | 104–113 | The file supplies the operative first-row rule, but not all forward normalizations, the loss normalization, or the layerwise learning-rate convention needed to independently derive its numerical prefactor. Frozen-row preservation holds for the supplied rule and is insensitive to that scalar prefactor. |

There is no substantiated required repair under the natural vector interpretation of O1 and the displayed-rule interpretation of O2. Neither clarification supplies any of the excluded dynamical or mean-field conclusions. The distinction between these interpretations and independently established claims is maintained below.

## 1. Initialization and activation assumptions

The source assumes a smooth, even function `p`, positive on `(-R,R)` and zero outside `[-R,R]`, with `R > 0`. Continuity forces `p(R) = p(-R) = 0`, including at the cutoff boundary. Its primitive satisfies

\[
\phi_1'(z)=p(z),\qquad
\phi_1(-z)=-\phi_1(z),\qquad
|\phi_1(z)|\le B,
\]

and

\[
\phi_1(z)=B\operatorname{sign}(z)
\quad\text{for }|z|\ge R,
\qquad B=\int_0^R p(s)\,ds>0.
\]

Thus the asserted saturation values and zero first derivatives are exact, including at equality in the definition of `F`. Smooth compact support also gives a finite global Lipschitz constant

\[
L=\sup_{z\in\mathbb R}|p'(z)|<\infty.
\]

For each initial row, the stated Gaussian covariance follows directly from the input normalization:

\[
\mathbb E[G_aG_b]
=x_a^\top(I_d/d)x_b
=\begin{cases}1,&a=b,\\ \rho,&a\ne b.\end{cases}
\]

Independence is across rows. The two coordinates of a row need not be independent; in particular, they are perfectly anticorrelated at `rho = -1`. No subsequent argument requires their independence.

When `|rho| < 1`, the Gaussian density is positive on the open set where both coordinates have absolute value greater than `R`. Consequently `m > 0`. The first coordinate takes intervals of different magnitudes on positive-probability portions of this set, so its absolute value is not constant conditional on `F`. Exchange symmetry supplies the same conclusion for the other coordinate.

At `rho = -1`, `G_2 = -G_1` almost surely and `F = {|G_1| >= R}`. The absolute value still has a nonconstant tail distribution. Also `F` is contained in `{|G_a| >= R}`, so `m < 1`, and `J_1,J_2` are finite, with `J_2 > 0`. There is no lost positive-mass assumption at the singular endpoint.

## 2. Exact restricted regression constant

All three quantities `m,J_1,J_2` in the source are **unconditional truncated moments**, not moments conditional on `F`. This matters for the normalization of the lower bound.

Let

\[
Q_a(u,v)=\mathbb E\big[(B\operatorname{sign}(G_a)-uG_a-v)^2\mathbf 1_F\big].
\]

Since `R > 0`, `sign(G_a)^2 = 1` on `F`. Joint central symmetry preserves `F` and changes the signs of both `G_a` and `sign(G_a)`. Therefore

\[
\mathbb E[G_a\mathbf 1_F]=0,
\qquad
\mathbb E[\operatorname{sign}(G_a)\mathbf 1_F]=0,
\qquad
\mathbb E[G_a\operatorname{sign}(G_a)\mathbf 1_F]=J_1.
\]

Expanding all terms gives exactly

\[
Q_a(u,v)=B^2m-2uBJ_1+u^2J_2+v^2m.
\]

In particular, the slope–intercept cross term vanishes; it was not omitted without justification. Completing squares gives

\[
Q_a(u,v)
=J_2\left(u-\frac{BJ_1}{J_2}\right)^2+mv^2
+B^2\left(m-\frac{J_1^2}{J_2}\right).
\]

The unique restricted population regression coefficients are

\[
u_*=\frac{BJ_1}{J_2},\qquad v_*=0,
\]

and the exact restricted minimum is the source's constant

\[
c_{\rho,R}=B^2\left(m-\frac{J_1^2}{J_2}\right).
\]

For another view of strict positivity, write the conditional mean and second moment of `|G_a|` as `mu = J_1/m` and `s_2 = J_2/m`. Then

\[
c_{\rho,R}
=B^2m\frac{\operatorname{Var}(|G_a|\mid F)}{\mathbb E[G_a^2\mid F]}>0.
\]

This also verifies the factor of `m`. Omitting it would incorrectly normalize the restricted sample as a probability law of mass one. The source does not make that error. Its Cauchy–Schwarz equality argument is valid, including for the singular Gaussian pair.

This constant is the exact minimum of the restricted quadratic. It is a lower bound, and need not be the exact optimum, for the full evolved law. The full-law minimizing slope or intercept need not equal `u_*` or zero.

### Explicit check at `rho = -1`

Let

\[
\varphi(r)=(2\pi)^{-1/2}e^{-r^2/2},\qquad
\overline\Phi(R)=\int_R^\infty\varphi(r)\,dr.
\]

Using `varphi'(r) = -r varphi(r)` and integration by parts,

\[
\int_R^\infty r\varphi(r)\,dr=\varphi(R),\qquad
\int_R^\infty r^2\varphi(r)\,dr=R\varphi(R)+\overline\Phi(R).
\]

It follows that

\[
\begin{aligned}
m&=2\overline\Phi(R),\\
J_1&=2\varphi(R),\\
J_2&=2\big(R\varphi(R)+\overline\Phi(R)\big),\\
u_*&=\frac{B\varphi(R)}{R\varphi(R)+\overline\Phi(R)},\\
v_*&=0,\\
c_{-1,R}
&=2B^2\left(\overline\Phi(R)
-\frac{\varphi(R)^2}{R\varphi(R)+\overline\Phi(R)}\right)>0.
\end{aligned}
\]

No inverse of the singular two-sample Gaussian covariance is used. The regression matrix is instead `diag(J_2,m)`, which is positive definite. The two matrices serve different purposes and must not be conflated.

For completeness, the nonsingular constants can also be written as exact one-dimensional integrals. If `sigma = sqrt(1-rho^2)` and

\[
A_\rho(g)
=\overline\Phi\left(\frac{R-\rho g}{\sigma}\right)
+\overline\Phi\left(\frac{R+\rho g}{\sigma}\right),
\]

then the representation `G_2 = rho G_1 + sigma H`, with `H` independent standard Gaussian, gives

\[
m=2\int_R^\infty\varphi(g)A_\rho(g)\,dg,
\quad
J_1=2\int_R^\infty g\varphi(g)A_\rho(g)\,dg,
\quad
J_2=2\int_R^\infty g^2\varphi(g)A_\rho(g)\,dg.
\]

The direct endpoint calculation above avoids inserting `sigma = 0` into these expressions.

## 3. Population statement: exactly what is conditional

Fix any considered deterministic time `t` and sample `a`. The assumption `Z_a(t) = G_a` on `F`, almost surely, implies

\[
\begin{aligned}
\mathbb E[(\phi_1(Z_a(t))-uZ_a(t)-v)^2]
&\ge
\mathbb E[(\phi_1(Z_a(t))-uZ_a(t)-v)^2\mathbf 1_F]\\
&=Q_a(u,v)\ge c_{\rho,R}.
\end{aligned}
\]

Taking the infimum over real `u,v` preserves the inequality. The restricted quadratic contains no evolved variable and no time parameter, so the same constant works at every considered time. The coefficients may be chosen separately for each time and each sample; this does not weaken the lower bound.

There is no unjustified interchange of expectation, infimum, and time. The proof first establishes a bound for every pair of real coefficients, and then takes their infimum. It does not assert a lower bound for a pointwise infimum taken separately at every neuron, which would be a different and false statement.

Square integrability of `Z_a(t)` is not needed for the inequality. The expectations are well-defined as nonnegative extended-real integrals. Moreover, choosing `u = v = 0` gives a full-law error at most `B^2`, so the infimum itself is finite. If `Z_a(t)` is square integrable, the usual Hilbert-space affine-regression interpretation applies exactly as the source states.

The word “conditional” here is a logical restriction: **given a measurable family on the specified probability space that preserves the indicated subset**, the inequality holds. It is not a proof that such a family solves a population evolution equation or exists globally. It is also not a statement about conditioning the Gaussian law on arbitrary additional random information; that would change the moment assumptions unless justified separately.

An almost-sure preservation statement for each deterministic time is enough for these deterministic expectation inequalities. It need not supply a single null set outside which an arbitrary measurable family is preserved at all times. For example, with an atomless measurable variable `U` on the initial space, the family equal to `G_a` except that `Z_a(t) = 0` when `t = U` agrees almost surely with `G_a` at every fixed time, while evaluation at the neuron-dependent random time `U` is identically zero. This is a boundary on an unstated random-time extension, not a counterexample to the source's fixed-time expectation theorem. The integral-flow argument below supplies stronger pathwise preservation when its hypotheses hold.

## 4. Finite empirical inequality and the common probability event

For any fixed initialization and any paths preserving every selected row, discarding the nonnegative contributions from other rows gives, for each `u,v`,

\[
\frac1n\sum_i
(\phi_1(z^{(1)}_{a,i}(t))-uz^{(1)}_{a,i}(t)-v)^2
\ge
\frac1n\sum_{i:F_i}
(B\operatorname{sign}(G_{a,i})-uG_{a,i}-v)^2.
\]

Taking infima gives the source's inequality (4), pathwise and simultaneously for all times at which preservation holds. The factor is `1/n`, not the reciprocal of the number of selected rows. This is consistent with the population truncated moments.

Writing `theta = (u,v)^T`, the restricted quadratic is

\[
B^2m_n-2\theta^\top b_{n,a}+\theta^\top M_{n,a}\theta.
\]

Whenever `M_{n,a}` is positive definite, its unique minimizing coefficient vector is `M_{n,a}^{-1}b_{n,a}` and the value is exactly

\[
c_{n,a}=B^2m_n-b_{n,a}^\top M_{n,a}^{-1}b_{n,a}.
\]

Thus the signs, order of the slope and intercept, and powers of `B` in source equation (5) are correct.

The needed initialization averages are

\[
\begin{gathered}
m_n,\qquad
q_{n,a}=n^{-1}\sum_i\mathbf 1_{F_i}G_{a,i}^2,\qquad
r_{n,a}=n^{-1}\sum_i\mathbf 1_{F_i}G_{a,i},\\
h_{n,a}=n^{-1}\sum_i\mathbf 1_{F_i}|G_{a,i}|,\qquad
s_{n,a}=n^{-1}\sum_i\mathbf 1_{F_i}\operatorname{sign}(G_{a,i}),
\qquad a=1,2.
\end{gathered}
\]

There are nine scalar averages, counting the shared `m_n` once. Their means are respectively `m,J_2,0,J_1,0`. Each has finite variance: for the potentially largest term, the second moment of `G_a^2 1_F` is at most `E[G_a^4] = 3`. Chebyshev and a finite union bound therefore give joint convergence in probability. Neither independence between the samples nor independence between these nine averages is required.

The limiting matrix is `diag(J_2,m)`, whose smallest eigenvalue is positive. Matrix inversion and the displayed quadratic minimum are continuous in a neighborhood of these limiting moments. This proves convergence of both `c_{n,a}` to the same positive `c_{rho,R}` in probability. The possible singularity of empirical matrices outside that neighborhood is harmless: the original infimum exists there and lies between zero and `B^2m_n`. No inverse on that event is needed.

One can make the initialization event explicit. Let `E_n(epsilon)` be the event that all nine averages are within `epsilon` of their means. For a sufficiently small fixed positive `epsilon`, continuity guarantees, simultaneously for both samples,

\[
M_{n,a}>0,
\qquad
B^2m_n-b_{n,a}^\top M_{n,a}^{-1}b_{n,a}
\ge \frac12c_{\rho,R}.
\]

For example, the sum of the nine one-row variances is at most
`1/4 + 2(3+1+1+1) = 49/4`, so the elementary estimate

\[
\Pr(E_n(\epsilon)^c)\le\frac{49}{4n\epsilon^2}
\]

is available. The admissible neighborhood size can depend on the fixed parameters. This crude optional bound is only an analytic elaboration of the source's Chebyshev argument, not an added experiment or a claim of parameter-uniform rates.

On this **single initialization event**, inequality (4) gives both full empirical gaps at least `c_{rho,R}/2` at every admissible time. There is no union bound over time, no discretization of an uncountable time interval, and no appeal to evolved-neuron independence. The event is determined entirely by the initial first-layer rows and works for any evolution that preserves the selected rows, including the displayed finite GF and raw GD.

“Simultaneously at every time” is therefore correct for each width on its event. It does not assert one event of a specified probability that simultaneously covers every width, or a deterministic positive lower bound for all small widths.

Two adversarial checks are useful here:

* Positive definiteness of an empirical design matrix alone does **not** imply a positive regression residual: if all selected values have the same sign, a constant fits their saturated activations exactly. The proof correctly uses convergence of the residual value as well as invertibility.
* With at most two distinct selected values, an affine function fits the restricted activation values exactly. In particular, at widths one and two the full empirical activation law itself is affine-fit exactly. Also, the event that no row is selected has probability `(1-m)^n > 0` at every finite width. None of this contradicts an asymptotic high-probability theorem.

At `rho = -1`, the two empirical gaps on the selected rows are exactly equal: replacing every `G_{1,i}` by `-G_{1,i}` changes the restricted squared residual with intercept `v` into that for sample one with intercept `-v`. Joint control of both samples remains valid even though they are then completely dependent.

## 5. Preservation in the finite GF and raw GD

For a fixed neuron, define the two total controls along a finite trajectory by

\[
C_b(t)=(f_b(t)-y_b)
\big[(W^{(2)}(t))^\top\delta_b^{(2)}(t)\big]_i,
\qquad b=1,2.
\]

The displayed first-row GF rule becomes

\[
\dot W_i^{(1)}
=-\frac2d\sum_{b=1}^2 C_b(t)p(z^{(1)}_{b,i}(t))x_b^\top.
\]

If the row equals its initial value and `F_i` holds, both factors `p(z^{(1)}_{b,i})` vanish. Its vector field is then zero for **every finite value of the other parameters**. This is stronger than merely having a zero initial derivative.

To justify invariance, constrain all selected rows to their initial values and solve the reduced ODE for the remaining coordinates. Along that constrained system the selected-row components of the full vector field vanish identically, so adjoining the constant rows produces a solution of the full ODE. The finite network has a smooth vector field in its finite parameters under the stated smooth activations and raw gradient rule. Its local uniqueness forces every full solution from the same initial condition to coincide with this constrained solution locally. Repeating this reasoning along any continuation gives preservation throughout its existence interval.

This argument does not assume that the other rows stay Gaussian, are independent, have uniformly bounded trajectories, or remain close to initialization. It uses their finiteness at times where the finite ODE solution exists. Smoothness gives local uniqueness, not a global-existence conclusion. The proof also handles cutoff equality because `p(+-R) = 0` and uniqueness still applies there.

For raw simultaneous GD, the selected row update is

\[
W^{(1),k+1}_i-W^{(1),k}_i
=-\frac{2\eta}{d}\sum_{b=1}^2
C_b^k p(z^{(1),k}_{b,i})x_b^\top.
\]

If the row has not moved at step `k`, both derivative factors are zero, so the next increment is exactly zero. Induction starts from initialization and proves preservation at every defined step. It holds in particular for `eta = n^{-2}` and does not need a small-step estimate. On each raw affine interpolation segment, the row is constant because its two endpoint values are equal. Evaluating the network along the interpolated parameter path does not alter this fact.

Loss descent, convergence of GD, and boundedness of other coordinates are not prerequisites for this preservation statement. An added update term, such as weight decay on the first rows, would require a different argument and is not part of the specified raw update.

### O2: what was and was not verified about “actual” GF/GD

The full forward definition of the second preactivation, the loss normalization, and the layerwise time or learning-rate convention are not all provided in the frozen source. Therefore the numerical coefficient `2/d` cannot be independently rederived from a completely specified loss in this isolated audit. It is supplied as the operative first-row rule at source lines 109–113.

This is not a counterexample to preservation: the proof above verifies it for that rule, and the same vanishing derivative factors occur in the first-weight gradient of a canonical feedforward network whose first rows enter only through `phi_1(W_i^{(1)}x_b)`. Changing a finite scalar normalization of that gradient does not change the invariant subset. A short statement making the displayed rule the definition for this proposition, or supplying the omitted normalization convention, would eliminate the specification ambiguity. It would not establish any other omitted network theorem.

## 6. Population integral-flow addendum and the coupled Gronwall step

This is the least explicit part of the source, but it has a direct valid completion under the usual meaning of an integral flow. Here is the precise version needed.

For almost every initial-neuron label, suppose the two preactivation paths are locally absolutely continuous and satisfy the first rule in integral form, with the **total** controls `C_1,C_2` locally integrable along that supplied path. The controls include the residual factor and the upper-layer backpropagated factor together. Integrability of two separate factors would not by itself prove integrability of their product.

Let

\[
K_{ab}=x_a^\top x_b/d,
\qquad K=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]

Taking the first-row rule against `x_a` gives, almost everywhere in time,

\[
\dot Z_a(t)=-2\sum_{b=1}^2K_{ab}C_b(t)p(Z_b(t)).
\]

On `F`, both `p(G_b)` vanish. Define

\[
D(t)=\max_{a=1,2}|Z_a(t)-G_a|,
\qquad A(t)=|C_1(t)|+|C_2(t)|.
\]

Since `|K_{ab}| <= 1` and `p` is globally Lipschitz,

\[
\|\dot Z(t)\|_\infty
\le 2\sum_{b=1}^2|C_b(t)|\,|p(Z_b(t))-p(G_b)|
\le 2LA(t)D(t)
\]

almost everywhere. The integral equation and the initial condition `Z(0) = G` consequently give

\[
D(t)\le 2L\int_0^t A(s)D(s)\,ds.
\]

For clarity, the scalar Gronwall conclusion can be obtained without invoking any population uniqueness theorem. On a compact time interval, `D` is continuous and bounded and `A` is integrable. Put

\[
H(t)=2L\int_0^t A(s)D(s)\,ds.
\]

Then `H(0) = 0`, `0 <= D <= H`, and `H' <= 2LAH` almost everywhere. Multiplication by `exp(-2L integral_0^t A)` shows that this nonnegative product is nonincreasing from zero. Hence `H = D = 0`. Localization gives the result throughout the supplied path's interval of existence. The row itself is then fixed because its first-row right-hand side vanishes.

The coefficient `2` in this version is correct with the maximum norm for `Z-G` and the sum norm for the controls. It follows from the input normalization and `|rho| <= 1`; no inverse of `K` is used, so `rho = -1` is allowed.

### O1: why the vector interpretation matters

The source's notation `|zdot| <= 2 Lip(p) |control| |z-G|` does not define these norms or the control. Reading `z` as the two-component vector yields the valid bound just proved. Reading it as a single `Z_a` generally does not: the other sample can contribute to its derivative.

For example, take `rho = 1/2`, `C_1 = 0`, `C_2 = 1`, `Z_1 = G_1 > R`, and `Z_2 = 0`. The displayed first rule then has

\[
\dot Z_1=-p(0)\ne0,
\qquad |Z_1-G_1|=0.
\]

Thus no bound by a finite control times the single difference `|Z_1-G_1|` holds in general. This configuration disproves that componentwise algebraic reading; it is not an escaping trajectory from the jointly frozen initial subset. The vector Gronwall argument excludes such escape under the actual hypotheses.

Explicitly naming the vector, the two norms, local absolute continuity, and pathwise integrability of the total controls would close the presentation issue. None of these checks proves that population controls of this kind exist. They do not prove uniqueness of the full population evolution either: preservation of one subset under every supplied admissible path is a much narrower fact.

## 7. Finite nonaffinity, population nonaffinity, and limiting claims

There are two separate valid conclusions:

1. At large finite width, with probability tending to one over first-layer initialization, each empirical first-activation affine-fit gap is bounded below at every time of the actual displayed GF/GD evolution where the parameters exist.
2. For a supplied population family preserving the Gaussian subset on its reference probability space, each population first-activation affine-fit gap has the deterministic positive lower bound `c_{rho,R}` at every considered time.

The second is not obtained by passing to a limit in the first. The frozen source neither constructs a width limit nor proves that such a limit is a population solution with the required reference-space preservation. A limiting theorem would have to establish its own existence, convergence, and identification statements. The present inequalities could then be used if their hypotheses were verified.

The gap concerns the scalar relation between `Z_a` and `phi_1(Z_a)` across neurons for a fixed training sample. It does not establish that the input-to-output predictor is nonlinear, that training learns a representation, or that a second activation is nonaffine across its neuron law. In particular, testing an affine fit across many neuron values for one sample is different from fitting predictions on the two training inputs.

An explicit admissible population family is `Z_a(t) = G_a` for all times. It already obeys the theorem with no motion at all. Thus neither a positive gap nor its uniformity in time supplies evidence of nonlazy evolution. The proof's witness is the portion that never changes.

## 8. Exclusions and quantifier limits

The source's explicit exclusions are justified and must be preserved when the result is cited or reused:

| Excluded conclusion | Why this proof does not establish it |
|---|---|
| Nonlazy dynamics | The lower bound comes entirely from fixed neurons and holds for static paths. |
| Movement of a positive mass of neurons | There is no lower bound on displacement or on the mass of moving rows. |
| Second-activation nonaffinity | The regression and frozen-subset arguments involve only the first preactivation and `phi_1`. Smoothness of `arctan` assists finite ODE regularity but gives no second-layer regression bound here. |
| Population existence, especially global mean-field existence | A population family or integral flow is supplied as a hypothesis. No construction, a priori bound, or continuation argument for it is provided. |
| Width convergence or identification of a population limit | The convergence proved is only for a finite list of initialization moments, not for evolving network parameters, fields, or laws. |
| Restart uniqueness or uniqueness of population dynamics | Finite-dimensional local ODE uniqueness and pathwise subset preservation do not imply either claim for an unspecified population system. |
| Global existence of every finite GF trajectory | The finite conclusion is explicitly restricted to times where its parameters exist. |
| Gaussian evolved fields or independent evolved neurons | Neither is assumed or proved; all probability estimates use initialization only. |
| A positive bound at every fixed small width | Finite empirical laws can have exact affine fits. The probability statement is asymptotic in width. |
| Rates uniform as `rho` approaches an endpoint | No such uniformity is established in the source. This is a limit on the stated claim, not an assertion that uniform rates are impossible. |
| A random-time theorem for every merely measurable population family | Almost-sure equality at each deterministic time does not in general give simultaneous pathwise equality. Integral-flow regularity supplies a stronger statement when available. |
| Other training sets or modified optimizers | The frozen event covers the two specified samples and the raw first-row rule. Additional sample gradients or extra update terms would need a new preservation check. |

The endpoint `rho = 1` is excluded by the source's input assumptions. The restricted regression argument itself would also work for `G_2 = G_1`; this observation does not authorize enlarging any surrounding network theorem. Conversely, the included endpoint `rho = -1` has been checked directly and requires no nondegenerate bivariate-density argument.

## 9. Required versus optional disposition

**Required mathematical fixes:** none identified for the claims actually stated, with the coupled population inequality understood as a vector-norm bound and the displayed finite first-row rule taken as the specified dynamics.

**Optional improvements:** specify that vector-norm bound and its total-control integrability hypotheses (O1), and clarify the normalization convention or definitional status of the displayed first-row update (O2). The explicit endpoint formulas and the common initialization event supplied in this report are useful proof expansions; they are not missing assumptions in the existing regression argument.

**Required limits on interpretation:** any use of this result must retain its frozen-subset, first-activation scope; the population statement remains conditional; the finite statement remains restricted to existence intervals and an asymptotic initialization probability. Calling it a nonlazy theorem, a global mean-field theorem, or a proof of finite-width convergence would exceed what the frozen source establishes.
