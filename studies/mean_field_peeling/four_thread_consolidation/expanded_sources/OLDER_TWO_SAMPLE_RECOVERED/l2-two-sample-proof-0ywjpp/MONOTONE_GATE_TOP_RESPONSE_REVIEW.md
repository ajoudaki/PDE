# Isolated adversarial audit: monotone-gate top response

## Verdict and exact scope

**PASS — the scoped deterministic actual-path lemma (5) and the full two-dimensional homogeneous propagator estimate (12), under the candidate's stated premises.** No required mathematical correction to these results or their proofs was identified.

The smoothing argument handles arbitrary readout sign changes, including accumulating zeros and intervals of zeros. The occupation estimate includes the full zero level set. The absorption constants in (5) are correct without assuming nonnegative correlation. The moving-Gram energy calculation controls the actual matrix in (11), including both off-diagonal entries, and yields exactly the constants in (12). The later-start assertion correctly uses the original history with zero initial readout. The shifted-softplus contrast calculation is correct as an algebraic statement about the pair of preactivations `(z,-z)`.

**The whole global L2/L3 theorem is explicitly NOT ESTABLISHED.** This audit does not certify existence of a population path, applicability of these premises to such a path, exponential integrability of lower forcing, the full network tangent system, an all-angle result, nonaffinity of evolved laws, or nonlazy training.

There are two optional wording clarifications below. Neither changes the scoped lemma or supplies a missing step in its proof.

## Isolation, evidence, and procedural disclosure

The sole mathematical input was:

`/tmp/l2-two-sample-proof-0ywjpp/MONOTONE_GATE_TOP_RESPONSE.md`

Expected and verified SHA256:

`05923d87529ad1705a359060aa8a3789e7f18639b9e0648910002d7b935e445a`

The candidate was read in full: 276 lines, 11,025 bytes. Its hash was verified before ingestion and again after the mathematical audit; both matched exactly. Line references below refer to that immutable candidate. The candidate was not edited.

Procedural resources read in full:

- `/home/amir/.codex/skills/review-ai-paper/SKILL.md`
- `/home/amir/.codex/skills/review-ai-paper/references/severity-rubric.md`
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`

These supplied review procedure, severity definitions, and proof-checking discipline only. The user's isolation and output instructions took precedence over their broader workflows. No other project files, prior reviews, referenced notes, external mathematical sources, or project history were consulted. There were no experiments, numerical checks, code executions of the candidate, or other agents. Evidence and claim assessment are consolidated in this single requested report; no auxiliary review artifacts were created.

The review is a mathematical audit under the user-supplied scope, not a conference review or a novelty assessment.

## 1. Premise contract and claim coverage

The following are assumptions, not conclusions established by this candidate:

1. A classical path satisfying all of (4) exists on the fixed compact interval `[0,S]`, with `w(0)=0` and continuous forcing. The forcing may depend on the path.
2. The activation is `C^2`, with `0<p<=P` and `0<=p'/p<=L`. Consequently `p` is nondecreasing, `p'<=LP`, and `phi` is strictly increasing.
3. The prescribed functions `lambda,k` satisfy (2), including `lambda>0`, `-1<k<=k_bar<1`, and `k_bar>=0`. In particular, `k` itself is allowed to be negative and to change sign.
4. For (12), the shared Gram additionally satisfies the explicit coercivity and variation bounds (3).

For a fixed coordinate, continuity on a compact interval supplies the finite bounds needed in the smoothing limits. No bound uniform over the coordinate family, and no readout moment, is inserted at this step. The differentiability of `lambda,k` is sufficient for the moving metric; their derivatives do not appear in the scalar absorption argument.

| Claim | Candidate location | Assessment |
| --- | --- | --- |
| Scalar equations and network normalization | Lines 33–59 | The displayed tensor equation gives exactly the first two equations of (4). Network applicability and the assumed feature-time/readout equation remain conditional. |
| Sign smoothing and zero-threshold occupation | Lines 84–145, (6)–(9) | Sound under the stated classical-path premises. |
| Absorption and removal of a separate readout-moment factor | Lines 147–185, (5), (10) | Sound, including negative and sign-changing `k`; constants verified. |
| Entire homogeneous `2x2` block and all later starts | Lines 187–229, (11)–(12) | Sound with (3), using original zero-time history. Moment conclusions remain conditional on an integrable majorant. |
| Shifted-softplus activation and antiparallel contrast | Lines 231–276 | Activation inequalities and contrast nonaffinity verified. Singular-Gram and global-scope limitations correctly prevent extrapolation. |

No external theorem or referenced project result is needed for the checked logical chain. The chain rules, integral limits, energy comparison, and Gaussian exponential-moment statement are justified below directly.

## 2. Exact scalar normalization and moving Gram

Write `p_a=p(z_a)`. Applying the displayed rank-one update to the current lower fields gives

\[
W_2'H_{1,1}=\tfrac w2(p_1G_{11}-p_2G_{21})
             =\lambda w(p_1-kp_2),
\]
\[
W_2'H_{1,2}=\tfrac w2(p_1G_{12}-p_2G_{22})
             =\lambda w(kp_1-p_2).
\]

The product rule for `z_a=W_2H_{1,a}` adds exactly `b_a=W_2H_{1,a}'`. Thus the factor `1/2` in the tensor update is canceled by the factor `2` in `G`; no factor is missing in (4). The lower-field motion is retained.

These identities do not require `G` to be constant. They use its current value when evaluating `W_2'H_{1,a}`. There is no additional `G'` term in this product rule: the other differentiated factor is already represented by `b_a`. The metric calculation later does require, and does retain, a `G'` term.

The network interpretation is conditional on the displayed feature-time update and readout equation. Equal Gram diagonals alone do not establish these equations for an arbitrary training process. The candidate explicitly starts from an existing symmetric path and does not claim that construction.

## 3. Smoothing, sign changes, and the occupation bound

Let

\[
\Delta=z_1-z_2,\qquad d=\lambda|w|,\qquad
X=\operatorname{sign}(w)\Delta,
\]

with `sign(0)=0`. The function `X` need not be continuous. The proof differentiates only the smooth approximations `X_delta`, never `X`.

### 3.1 Every finite-smoothing chain rule is valid

Since

\[
H'(z)=-\frac{p'(z)}{p(z)}\in[-L,0],
\]

`H` is nonnegative and nonincreasing. Strict increase of `phi` and nonincrease of `H` imply

\[
(\phi(z_1)-\phi(z_2))(H(z_1)-H(z_2))\le0.
\]

Because `alpha_delta'>=0` and `w'=(phi(z_1)-phi(z_2))/2`, the switching term in `L_delta'` is nonpositive, proving (6). This is valid also when either difference vanishes.

Likewise

\[
w'\Delta=\tfrac12(\phi(z_1)-\phi(z_2))(z_1-z_2)\ge0.
\]

The difference equation from (4) is

\[
\Delta'=\lambda w(1-k)(p_1+p_2)+(b_1-b_2).
\]

Thus

\[
X_\delta'
=s_\delta'(w)w'\Delta
 +(1-k)d_\delta(p_1+p_2)+s_\delta(w)(b_1-b_2)
\ge (1-k)d_\delta(p_1+p_2)-|b_1-b_2|,
\]

which is (7). It uses neither a sign restriction on `k` nor a derivative of `k`. The required inequality is `1-k>=1-k_bar>0`.

For each positive `delta`, these compositions are continuously differentiable on the whole interval. No division by `w`, crossing count, or bounded variation of its sign is required. On an interval of zeros of `w`, the smoothed formulas remain valid. At isolated or accumulating zeros, they remain ordinary classical chain rules.

### 3.2 The upper bound on the truncation primitive is sufficient

For the candidate's `T_h`, one has `T_h'=chi(x/h)` in `[0,1]`, with derivative equal to one on the whole half-line `x<=0`. For `x<0`, `T_h(x)=x`; for `x>=0`, its integrand vanishes beyond `h`. Therefore

\[
T_h(x)\le h\quad\text{for every real }x.
\]

Its lack of a lower bound does not harm the proof. Multiplication of (7) by the nonnegative `T_h'(X_delta)` and integration gives

\[
(1-\bar k)\int_0^t T_h'(X_\delta)d_\delta(p_1+p_2)
\le T_h(X_\delta(t))-T_h(X_\delta(0))
    +\int_0^t T_h'(X_\delta)|b_1-b_2|.
\]

Zero initial readout gives `X_delta(0)=0`, even when the initial preactivations differ. The right side is at most `h+D_t`, proving (8). No lower bound on the terminal value was used.

### 3.3 Both limits preserve the entire zero level set

Fix `h>0` first. At every time with `w!=0`, `X_delta` tends to `X` and `d_delta` tends to `d`. At every time with `w=0`, both `d_delta` and `d` are zero and `X_delta=X=0`. Hence

\[
T_h'(X_\delta)d_\delta(p_1+p_2)
\longrightarrow T_h'(X)d(p_1+p_2)
\]

pointwise at every time. The integrands are between zero and `2P d`. This majorant is time-integrable for the fixed classical path. Dominated convergence therefore yields

\[
(1-\bar k)\int_0^t T_h'(X)d(p_1+p_2)\le h+D_t.
\]

On `X<=0`, including `X=0`, the factor `T_h'(X)` is exactly one. The remaining integrand is nonnegative, so

\[
\int_{X\le0}d(p_1+p_2)\le\frac{h+D_t}{1-\bar k}.
\]

The integral on the left is independent of `h`. Taking the infimum over positive `h` proves (9). This last step requires neither indicator convergence nor a convention assigning a half-weight to the boundary.

In particular, the set `z_1=z_2` with `w!=0` is retained with full weight. The set `w=0` contributes zero through `d`, regardless of its measure or topology. There is no missing zero-threshold occupation term.

## 4. Potential inequality, absorption, and the constants in (5)

Put `j_a=p'(z_a)/p(z_a)`. Differentiating the potential and using the switching sign gives

\[
\begin{aligned}
L_\delta'
&\le-\alpha_\delta j_1z_1'-(1-\alpha_\delta)j_2z_2'\\
&=-\lambda w[\alpha_\delta p_1'-(1-\alpha_\delta)p_2']\\
&\quad+\lambda k w[\alpha_\delta p_2j_1
                         -(1-\alpha_\delta)p_1j_2]\\
&\quad-\alpha_\delta j_1b_1-(1-\alpha_\delta)j_2b_2\\
&\le-I_\delta+R_\delta+L(|b_1|+|b_2|).
\end{aligned}
\]

This verifies the signs of both terms in the candidate. In particular, the second forcing term has not been lost, and the finite-`delta` quantity `I_delta` need not be nonnegative for this argument to work.

### 4.1 The coefficient limits introduce no readout cost

Let `w_+=max(w,0)` and `w_-=max(-w,0)`. The elementary estimate for `x(1-tanh x)` gives

\[
w\alpha_\delta\to w_+,
\qquad -w(1-\alpha_\delta)\to w_-,
\]

with errors bounded by an absolute constant times `delta`, uniformly in the real value of `w`. Since `p_a'<=LP`, `p_aj_b<=PL`, `lambda<=lambda_max`, and `|k|<=1`, it follows that the time integrals converge to

\[
I_t=\int_0^t\lambda(w_+p_1'+w_-p_2'),
\]
\[
\int_0^t R_\delta\longrightarrow
\int_0^t\lambda k(w_+p_2j_1+w_-p_1j_2)
=\int_0^t k d p_{\rm other}j_{\rm active}.
\]

The integral errors are bounded by constants times `S delta` and vanish. The smoothing constants do not survive in (5). No integrability across a coordinate family is needed to take these time-integral limits.

For every `delta`, `L_delta(t)>=0` and `L_delta(0)=A_0`. Integrate first, drop the nonnegative terminal potential, and then pass to the limit. This gives exactly

\[
I_t\le A_0+LQ_t+\int_0^t k d p_{\rm other}j_{\rm active},
\]

namely (10). No convergence of a derivative of the limiting active potential is assumed.

### 4.2 The cross term is controlled on every sign region

Partition time into the following measurable regions; zeros of `w` have zero integrand and may be assigned arbitrarily.

- If `k<0`, then `k d p_other j_active<=0`. Dropping this contribution is legitimate in an upper bound.
- If `k>=0` and `X>=0`, the active preactivation is at least the other one. Monotonicity of `p` gives `p_other<=p_active`, and therefore
  \[
  k d p_{\rm other}j_{\rm active}
  \le\bar k\,d p_{\rm active}j_{\rm active}
  =\bar k\,d p_{\rm active}'.
  \]
  Equality of the preactivations creates no exception.
- If `k>=0` and `X<0`, use `j_active<=L`, `p_other<=p_1+p_2`, and (9). This region contributes at most `k_bar L D_t/(1-k_bar)`.

Nonnegativity of the curvature integrand allows the first positive-region integral to be enlarged to `k_bar I_t`. Consequently

\[
(1-\bar k)I_t
\le A_0+LQ_t+\frac{\bar k L D_t}{1-\bar k}.
\]

Dividing by the strictly positive `1-k_bar` gives

\[
I_t\le\frac{A_0}{1-\bar k}
       +\frac{LQ_t}{1-\bar k}
       +\frac{\bar k L D_t}{(1-\bar k)^2}.
\]

Finally `D_t<=Q_t` and

\[
\frac1{1-\bar k}+\frac{\bar k}{(1-\bar k)^2}
=\frac1{(1-\bar k)^2}
\]

give the second inequality in (5). All displayed constants are correct. There is no missing factor of `2`, `P`, `lambda_max`, or readout magnitude in this final bound.

The mechanism removes the separate accumulated-readout factor from this estimate. It does not make `Q_t` independent of readout or prove any distributional estimate on endogenous forcing.

## 5. The actual full homogeneous matrix and the constants in (12)

The coefficient matrix in (11) is

\[
A=\lambda w
\begin{pmatrix}
p_1'&-k p_2'\\
k p_1'&-p_2'
\end{pmatrix}.
\]

It is the complete Jacobian of the two `z` equations with respect to `z`, with readout, Gram, and forcing held as prescribed coefficients. Both off-diagonal interactions are present. It need not be symmetric in the Euclidean metric.

This is not the full tangent system in `(z_1,z_2,w,lower fields)`. For example, readout variation would enter both `z` equations, and its own variation satisfies `(delta w)'=(p_1 eta_1-p_2 eta_2)/2`. Variations of the lower fields and Gram introduce further terms. The candidate explicitly excludes their estimation by (11).

### 5.1 Energy identity with the moving inverse metric

Let `M=G^{-1}` and `D=diag(p_1',-p_2')`. Then `A=(w/2)GD`, so

\[
A^TM+MA=wD.
\]

For `E=eta^TM eta`, the product rule therefore gives

\[
E'=w(p_1'\eta_1^2-p_2'\eta_2^2)+\eta^TM'\eta,
\qquad M'=-G^{-1}G'G^{-1}.
\]

There is no commutativity assumption needed for these identities. In particular, the moving inverse metric has been differentiated, not frozen.

Coordinate evaluation follows from Euclidean Cauchy–Schwarz:

\[
\eta_a^2
=\big((G^{1/2}e_a)^T(G^{-1/2}\eta)\big)^2
\le G_{aa}E=2\lambda E.
\]

When `w>0`, only the sample-1 curvature term can be positive; when `w<0`, only the sample-2 term can be positive. Hence the curvature contribution is at most `2d p_active' E`, including at `w=0`.

With `v=G^{-1/2}eta`,

\[
\eta^TM'\eta
=-v^T(G^{-1/2}G'G^{-1/2})v
\le\|G^{-1/2}G'G^{-1/2}\|_{\rm op}\,E=mE.
\]

Thus `E'<=[2d p_active'+m]E`, exactly as stated. This argument controls the full matrix, including any Euclidean nonnormal behavior; it does not replace the system by a scalar diagonal entry.

As a direct check specific to this Gram, its fixed eigenvectors have eigenvalues `g_+=2lambda(1+k)` and `g_-=2lambda(1-k)`, and

\[
m=\max\left\{
\left|\frac{\lambda'}\lambda+\frac{k'}{1+k}\right|,
\left|\frac{\lambda'}\lambda-\frac{k'}{1-k}\right|
\right\}.
\]

This confirms that variation of both `lambda` and `k` is accounted for. Negative `k` causes no sign defect. Approaching `k=-1` can degrade the metric constants, as it should.

### 5.2 Integration, metric conversion, and arbitrary starts

For any `0<=s<=t<=S`, multiply the differential energy inequality by the integrating factor for `2d p_active'+m`. This yields

\[
E(t)\le E(s)\exp\left(2\int_s^t d p_{\rm active}'
                              +\int_s^t m\right).
\]

This proof also covers zero initial vectors without taking a logarithm of zero. Using the two endpoint metric bounds gives

\[
|\eta(t)|^2\le\gamma_+ E(t),
\qquad E(s)\le\gamma_-^{-1}|\eta(s)|^2.
\]

After taking the square root and maximizing over initial vectors,

\[
\|\Psi(t,s)\|_{\rm op}
\le\sqrt{\frac{\gamma_+}{\gamma_-}}
\exp\left(\int_s^t d p_{\rm active}'+\frac12\int_s^t m\right)
\le\sqrt{\frac{\gamma_+}{\gamma_-}}e^{I_S+V/2}.
\]

Substitution of (5) gives exactly (12). The square-root metric ratio, coefficient `V/2`, and coefficient `1` on `I_S` are all correct.

The nonnegative integral on `[s,t]` is bounded by the one on `[0,S]`. Applying (5) to that original history uses the actual assumption `w(0)=0`; it does not require or assert `w(s)=0`. No fresh initial potential or occupation bound is smuggled in at the restart time. The candidate's limitation to original-history bounds is essential and correct.

## 6. Moment implications and their limits

For a probability-space interpretation, keep the constants in the deterministic bound fixed. Write

\[
C=\sqrt{\gamma_+/\gamma_-}\,e^{V/2},
\qquad B=\frac{A_0}{1-\bar k}+\frac{LQ_S}{(1-\bar k)^2},
\qquad R=\sup_{s\le t}\|\Psi(t,s)\|_{\rm op}.
\]

For any desired moment order `r>0`, (12) gives `R^r<=C^r e^{rB}`. Therefore integrability of the joint exponential `e^{rB}` is sufficient to deduce the response moment from this estimate. Merely knowing that `A_0,Q_S` are in `L^2` does not ensure integrability of this upper bound: square-integrable nonnegative random variables can have no positive exponential moments.

No independence is available or needed if the joint exponential is controlled directly. To obtain it from separate estimates, conjugate exponents `a,a'>1` require the appropriately enlarged exponents:

\[
\mathbb E e^{rB}
\le
\left(\mathbb E e^{arA_0/(1-\bar k)}\right)^{1/a}
\left(\mathbb E e^{a'rLQ_S/(1-\bar k)^2}\right)^{1/a'}.
\]

The candidate correctly flags this issue and does not prove an exponential forcing estimate. If metric bounds were instead taken to be random, their prefactor and variation cost would also need joint control; the deterministic lemma supplies no exemption from that requirement.

The word “must” in the moment paragraph should be read as a condition for this majorant-based argument, not as a necessary condition for actual response moments. Optional clarification O1 below makes this distinction explicit.

## 7. Shifted softplus and the exact antiparallel contrast

For the stated activation,

\[
p(z)=\epsilon\sigma(z-b),\qquad
p'(z)=\epsilon\sigma(z-b)(1-\sigma(z-b)),\qquad
\frac{p'}p=1-\sigma(z-b).
\]

It is smooth, `0<p<=epsilon`, and `0<=p'/p<=1`. Thus `P=epsilon`, `L=1` satisfy (1). Boundedness of the activation itself was not assumed and is not needed.

The potential is exactly

\[
H(z)=\log(1+e^{b-z})
\le\log2+|b|+|z|.
\]

For initial Gaussian variables `Z_1,Z_2`,

\[
A_0\le\log2+|b|+\tfrac12(|Z_1|+|Z_2|).
\]

Every Gaussian variable with finite mean and variance satisfies `E exp(c|Z|)<infinity` for every finite positive `c`, since `exp(c|Z|)<=exp(cZ)+exp(-cZ)` and both Gaussian moment-generating functions are finite. Cauchy–Schwarz handles the product for the two variables without independence. This verifies every finite positive exponential moment of `A_0` for the stated Gaussian initialization. It says nothing about the later forcing or uniform constants over unrestricted families of Gaussian laws.

For the preactivation pair `(z,-z)`, define

\[
\psi(z)=\frac{\phi_2(z)-\phi_2(-z)}2.
\]

The constant offset in `phi_2` cancels. If `b=0`,

\[
\log(1+e^z)-\log(1+e^{-z})
=\log\frac{1+e^z}{1+e^{-z}}=z,
\]

so `psi(z)=epsilon z/2` exactly. The candidate identifies the correct contrast-level degeneration.

For `b>0`, differentiation instead gives

\[
\psi'(z)=\frac\epsilon2[\sigma(z-b)+\sigma(-z-b)],
\]
\[
\psi''(z)=\frac\epsilon2[\sigma'(z-b)-\sigma'(z+b)].
\]

Here `sigma'(x)=1/(2+2cosh x)` is even and decreases strictly as `|x|` increases from zero. Since `|z-b|<z+b` for every `z,b>0`, `psi''(z)>0` on the positive half-line. This includes `z=b`. Consequently the odd contrast is nonaffine. The additional checks

\[
\psi'(0)=\frac\epsilon{1+e^b},\qquad
\lim_{z\to+\infty}\psi'(z)=\frac\epsilon2
\]

are also correct. Fixing `b=1` removes the stated unshifted-softplus linear-contrast failure.

This proves an algebraic property of a function. It does not imply that every evolved law explores that nonlinearity or that training is nonlazy. The candidate explicitly makes neither inference.

### Degenerate Gram and the boundary of applicability

For the exact odd-feature relation `H_{1,2}=-H_{1,1}`, let `g=E_1[H_{1,1}^2]`. Then

\[
G=g\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

Its eigenvalues are `0` and `2g`. If `g>0`, writing it in the candidate's parameterization gives `lambda=g/2` and `k=-1`; if `g=0`, it is the zero matrix. Thus this case fails the positive-definite premise (3), and it is also outside the strict `k>-1` premise of (2) (or the positive `lambda` premise when `g=0`).

The inverse-metric propagator proof is unavailable there. The algebraic contrast check does not use that inverse metric, and the candidate does not invoke (12) for the singular Gram. A separate scalar reduction and its own verification would be required for a training theorem at this endpoint. No such reduction or endpoint theorem is certified here.

The input-geometric phrase “exactly antiparallel” is understood here in its stated intended feature relation, yielding `(z,-z)`. Opposite directions with unequal lengths do not by oddness alone imply that relation. Optional clarification O2 records this scope distinction; no unspecified architecture or input normalization is used to prove the scalar lemma.

## 8. Adversarial boundary checks

These are analytic checks of the displayed formulas, not experiments.

- **Negative or sign-changing correlation:** `1-k>=1-k_bar` remains valid, and negative cross terms can be dropped. No use of `k>=0` occurs outside the explicitly partitioned region.
- **`k_bar=0`:** All correlations are nonpositive. The absorption formula reduces correctly to `I_t<=A_0+LQ_t`.
- **`L=0`:** Then `p'=0` identically and `I_t=0`; the estimates remain valid, although possibly non-sharp.
- **`D_t=0`:** The occupation estimate forces the integral over `X<=0` to vanish. No assumption on the initial ordering of `z_1,z_2` is needed because the smoothed initial gap is zero.
- **`w=0` on sets of positive measure:** All active-curvature and cross-term integrands vanish there; finite-smoothing chain rules still apply. No zero-set measure restriction is needed.
- **`X=0` with `w!=0`:** The occupation estimate includes this set with full weight, while absorption on `X>=0` also remains valid there. These are compatible bounds, not an omitted boundary term or an adverse double count.
- **Arbitrarily many sign switches:** The proof never exchanges a limit with a differentiated sign function. The relevant limits are taken only after integration.
- **Large coordinatewise readout:** The time domination is permitted for each compact classical path; no expectation or supremum over coordinates is passed through that domination. The final estimate has no independent readout factor.
- **Later starts with nonzero readout:** The fundamental matrix estimate uses `I_S` from the original path. A bound based solely on post-restart data is not proved.
- **Nearly or exactly singular Gram:** Nearly singular paths incur the explicit metric cost. Exactly singular paths are outside the stated metric theorem; the candidate's contrast calculation does not repair that failure of premises.

## 9. Required fixes versus optional clarifications

### Required fixes

**None for the scoped lemma (5), the conditional homogeneous propagator result (12), or the stated algebraic shifted-softplus contrast calculation.** The checked arguments are sound under their exact premises. No fatal, major, or minor proof flaw was identified in that scope.

This verdict does not convert the separately acknowledged global obligations into established facts.

### Optional clarifications

**O1 — Make the majorant interpretation of moment integrability explicit (lines 223–229).** A precise formulation would be: “To deduce an `r`-th response moment from the displayed upper bound, it suffices to establish integrability of the indicated joint exponential.” The current paragraph's opening reference to what (12) gives supplies this context, but “must be integrable” should not be interpreted as necessity for the actual response.

That stronger necessity reading would be false even within the exact classical-path setting. For example, fix the shifted softplus, `lambda=1`, `k=k_bar=0`, `S>0`, and take a nonnegative random variable `Y` with finite second moment but no positive exponential moment. Set, for each realization,

\[
z_1(t)=z_2(t)=tY,\qquad b_1(t)=b_2(t)=Y,\qquad w(t)=0.
\]

These are classical paths satisfying (4). The Gram is `2I`, `A_0=H(0)` is fixed, and `Q_S=2SY`. Yet the matrix in (11) is zero, so `Psi(t,s)=I` and every response moment is finite. An explicit such `Y` has density `3(1+y)^{-4}` on `y>=0`: its second moment is finite by the `y^{-2}` tail of the second-moment integrand, while every positive exponential moment diverges. This example clarifies wording; it does not contradict either inequality or the paragraph's majorant-based interpretation.

**O2 — Spell out the exact-negative relation in the antiparallel discussion (lines 245–271).** Writing “for an exact negative input pair giving `H_{1,2}=-H_{1,1}`” would eliminate ambiguity with unequal-norm antiparallel vectors. The nonaffinity calculation itself only uses the explicitly displayed pair `(z,-z)` and is correct. The singular-Gram sentence could also mention that `k=-1` lies outside (2), in addition to failing (3). Neither clarification changes the proved lemma or establishes the missing endpoint reduction.

Under the procedural severity rubric, these are optional minor presentation points, not proof defects and not reasons to downgrade the scoped mathematical verdict.

## 10. Outstanding obligations for any global L2/L3 application

The candidate deliberately leaves the following matters unproved:

1. Construction and continuation of the full population/reference path and justification of the feature-time equations on the relevant time interval.
2. Symmetry of the appropriate sample Gram along that path, rather than an assumption of finite-realization equality.
3. Quantitative control of the Gram eigenvalues and relative variation for the intended path or family.
4. Sufficient joint exponential control of initial potential and accumulated lower forcing, including its dependence on the coupled dynamics. Ordinary `L^2` information alone does not close the bound by this route.
5. Control of readout variations, lower-field variations, Gram variations, and forcing terms in the full network tangent or stability system.
6. A valid treatment of the singular antiparallel endpoint and any uniform all-angle statement.
7. Selection and verification of the first-layer activation and, for deeper networks, re-establishment of the top equations and lower-forcing estimates at the required layer.
8. The separate distributional and dynamical claims concerning nonaffine evolved laws and nonlazy training.

These are limits of scope, not hidden assumptions supplied by this review. The absence of a separate readout-moment factor is a useful conditional response improvement; it does not settle any of these remaining obligations.

**Final assessment: PASS for the explicitly scoped actual-path lemma and its conditional full `2x2` homogeneous propagator corollary. The whole global L2/L3 theorem is not established.** Confidence is high for the displayed deterministic derivations and algebraic activation check; no confidence claim is made about project applicability or omitted global arguments.
