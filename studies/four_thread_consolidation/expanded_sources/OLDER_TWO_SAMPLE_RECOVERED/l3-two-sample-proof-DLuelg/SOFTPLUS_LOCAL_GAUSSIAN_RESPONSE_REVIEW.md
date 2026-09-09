# Isolated adversarial audit: shifted-softplus finite Gaussian response lemma

Date: 2026-09-06.

Candidate: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md`.

Exact candidate SHA-256:

```text
0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b
```

The audited candidate has 473 lines and 18,947 bytes. Line references below refer to this exact version.

## Verdict and required fixes

**The conditional finite-law response lemma passes this audit. No required mathematical fix was found.** Under the stipulated law (2)--(3), its formal-derivative convention, and the expressly assumed primal bounds (4)--(5), the proof establishes (6)--(7) and the one-law clipping estimate (31). Its estimates are uniform in the mesh, labels, input correlation, and three cap sizes. The identity-cut statement is also valid with the same conditional premises.

In particular, I found no circular use of current backward rows, no missing factor from a sample sum or source injection, no unjustified factorization, and no loss of formal zero-variance source directions. The constants can be chosen before the induction and give a strictly positive common horizon. Detailed checks and the underlying derivative recurrences appear below; the verdict does not rest solely on the candidate's assertions that the recursions are causal.

## Scope and isolation

The candidate was read in full, through its final line. It was the only mathematical or contextual input read. No project files, history, other candidates, prior reviews, external sources, experiments, or agents were used. The candidate was not edited.

The existence of the precise finite Gaussian law and the explicitly assumed existence of its displayed formal derivative expectations are accepted. Equations (4)--(5) are accepted as premises for that law. Thus this is a verification of their stated implication, not a derivation of those premises.

This report neither requires nor certifies a finite-width identification, a derivation of the primal hypotheses from training, a common population-operator construction, a mesh limit, convergence as caps are removed, or a local/global theorem for uncut training. Those are expressly outside the candidate's claim. In particular, (31) is an error estimate for clipping a random variable under one already specified law; it is not a comparison theorem between laws with different caps.

## 1. Setup, activation, and formal source convention

At lines 13--17, direct differentiation gives

```text
phi'(z)  = e exp(z)/(1+exp(z)),
phi''(z) = e exp(z)/(1+exp(z))^2,
```

where `e=1/10` is the activation parameter. Consequently `0<phi'<=e` and `|phi''|<=e/4=1/40=c`. Also `log(1+exp(z))<=log(2)+|z|`, so `1<=phi(z)<=2+e|z|`. All activation inequalities used later are valid. No higher derivative bound on a cap is needed: every response estimate uses only `|tau(q)|<=|q|` and `|tau'(q)|<=1`.

The source covariance identities at lines 58--61 use uncentered input second moments. For example, their exact consequence is

```text
E[(xi^(ell)_ka-xi^(ell)_ra)^2]
    = E[(H^(ell-1)_ka-H^(ell-1)_ra)^2].
```

This identity remains valid when the features have nonzero mean. Replacing the stipulated covariance by a centered-feature covariance would be a different law; the proof does not do so.

All derivative calculations below use the convention at lines 77--80: deterministic coefficients and covariance parameters are frozen, and every displayed source coordinate is a separate formal variable. Thus a derivative in an `xi2` slot does not differentiate a `zeta2` coordinate through its covariance, and there is no derivative of `A` or `B` through the expectations defining it. This is exactly the response appearing in (3), including when the Gaussian covariance is singular. It is not being interpreted as a derivative restricted to the support of the Gaussian law.

## 2. Gaussian chaining and interpolation: (8)--(11)

The scalar two-sided Gaussian tail (8) is correct, including zero variance. Applying the exponential moment formula to each sign gives the result without a nondegeneracy assumption.

At dyadic level `j`, only odd-index children have a nonzero difference from the stated parent. There are at most `2^j` relevant increments, each of standard deviation at most `DS 2^(-j)`. Hence their union probability is bounded by

```text
2^(j+1) exp[-(u+2 sqrt(j)+2)^2/2]
 <= 2 exp(-u^2/2) exp[(log(2)-2)j-2],
```

because `u>=0` and the discarded cross terms are nonnegative. The geometric series over `j` converges since `log(2)-2<0`. The initial-value failure probability is at most `2 exp(-u^2/2)`; using `v` in place of the actual standard deviation only weakens this bound.

The dyadic approximants from below telescope from zero for every `t<S`. The countable event controlling all increments therefore controls every such approximant and, by continuity, the whole interval, including the endpoint `S`. No uncountable union bound is being taken. The sum used in (9) satisfies

```text
sum_(j>=1) 2^(-j)(u+2 sqrt(j)+2) <= u+6 <= 8(u+1).
```

Thus (9) holds with room in the constant. The proof uses no independence of increments.

For `v<=7`, `D<=1`, and `S<=1/10`, the scale `v+8DS` is at most `7.8<8`. A union bound over the two sample paths gives (10), irrespective of their correlation. For `t>=16`, `u=t/8-1>=t/16`, so

```text
P(N>t) <= 2 C_G exp(-t^2/512).
```

The distribution-function integral in lines 179--187 is justified by Tonelli for nonnegative integrands, even before finiteness has been established. At exponent `1/2048`, the remaining large-`t` integrand has Gaussian decay proportional to `t exp(-3t^2/2048)`. The initial interval is bounded. This proves (11) with an absolute constant.

For `xi2` and `xi3`, (4) gives initial standard deviations at most `2.3` and `4.53`, respectively, both within the chosen upper bound `7`. The covariance identity above and (5) give the node increment metric with constant one. On an interval of length `Delta`, the linearly interpolated process has `L2` speed at most one. Splitting at mesh nodes and applying the triangle inequality proves the same Lipschitz estimate across arbitrary intervals. A finite linear interpolation is a continuous Gaussian process, also for singular arrays. Thus the application to both full forward-source maxima `N_2,N_3` is valid and introduces no mesh-cardinality factor.

## 3. Reverse time averages and the common random envelope: (12)--(13)

For every reverse-source node, (4) and the exact covariance law give

```text
sd(zeta2_ka) = ||delta3_ka||_2 <= 0.7 s_k <= 0.07,
sd(zeta1_ka) = ||delta2_ka||_2 <= 0.77 s_k <= 0.077.
```

In particular the variance bound by one is valid, including at the terminal node. The weights in the definition of each reverse time average are exactly `Delta/S=1/M`, over exactly `M` nodes. They are nonnegative and sum to one. The function `x -> exp(alpha x^2)` is convex, so the first inequality in (12) holds pointwise. At each time, the exponential of the maximum of two squares is bounded by the sum of their exponentials. For a centered Gaussian with variance at most one, each expectation is at most `(1-2alpha)^(-1/2)`. This proves (12) without any independence across times or samples.

The same two-coordinate argument applies to `G_*`, uniformly in `rho`, including `rho=+/-1`.

For the six summands in `T=1+G_*+N_2+N_3+V_1+V_2`, the candidate first uses Cauchy--Schwarz in the deterministic form `T^2<=6 sum x_i^2`. Convexity then gives

```text
exp(eta_0 T^2) <= (1/6) sum_(i=1)^6 exp(36 eta_0 x_i^2).
```

Taking `eta_0=1/(36*2048)` is permissible. The constant summand contributes just `exp(36 eta_0)`; all other terms have the required bounds from (11)--(12). This proves (13) with a universal finite `C_1`. This argument uses no factorization of random variables, whether or not they are independent.

The time averages omit node `M` deliberately and correctly: every update producing a forward state or readout through time `M` uses only reverse queries at `r<M`. The final reverse queries themselves are handled later using their own individual Gaussian source, not by trying to recover it from a time average.

## 4. Simultaneous path bounds under the partial bootstrap: (14)--(19)

Here and below a backward row bound is deterministic. It is a bound on a coefficient row, not a random event on which the Gaussian law is conditioned. Consequently the unconditional source moment estimates remain available throughout the induction.

Suppose the past `B2` and `B3` rows are at most one. For a past node `r`, the sum defining its query includes only feature nodes `v<=r`, whence

```text
max_a |q1_ra| <= max_a |zeta1_ra|+2+e X_1(r),
max_a |q2_ra| <= max_a |zeta2_ra|+2+e X_2(r).
```

The time-diagonal terms in these rows are included in these inequalities; they are not omitted. Taking a maximum over earlier feature times is legitimate because the sums of nonnegative upper bounds are increasing in the terminal index.

For the bottom layer, the factor `Delta/2` multiplied by the sum over two update samples leaves `Delta`, since `|C_ab|<=1` and `|y_b|=1`. The gate contributes `e`. This gives exactly the recursion above (14). Its multiplicative coefficients are `e^2 Delta`, and its terminal additive bound is `G_*+e S(V_1+2)`, proving (14).

For the middle layer, the bound `|A2|<=20 Delta/2` gives a total update factor `20 Delta` after summing the two samples. The inequality `|delta2|<=e|q2|` gives (15), with multiplicative coefficients `20 e^2 Delta` and additive bound `N_2+20eS(V_2+2)`.

For the top layer, the exact readout update gives `|W4_r|<=s_r[2+eX_3(r)]`. In the strictly past update for `Z3_k`, this is needed only at `r<k`. The total coefficient after summing two samples is `60 Delta`; hence its recursion has multiplicative coefficients `60e^2 Delta s_r` and additive contribution `120e Delta sum s_r`. The bounds `Delta sum_(r<k) s_r<=S^2` yield (16). There is no same-time implicit equation hidden in this use of the readout.

The discrete product estimate applies to all three recursions; a nondecreasing inhomogeneous term can be replaced by its terminal value before induction. It does not require a limiting mesh argument.

The full-source upper bound used for the top feature envelope during a partial induction can be written explicitly as

```text
K = 2+e exp(60e^2 S^2)[N_3+120eS^2].
```

It bounds `2+eX_3(j)` at every currently established top time. It does not use a future actual field maximum before future coefficients have been bounded. Using the full Gaussian maximum `N_3` here is harmless: its moment bound was obtained directly from the accepted primal premises, without the coefficient conclusion.

As a concrete check of universality, one may take `C_2=3` in (17). Indeed, with `S<=0.1`, the three bounds are at most

```text
exp(0.001)[G_*+0.01 V_1+0.02],
exp(0.02) [N_2+0.2 V_2+0.4],
exp(0.006)[N_3+0.12],
```

respectively. Each is at most `3T`, and the displayed `K` is also at most `3T`. Thus `|W4_j|<=3s_jT` as well. All these statements hold on the same realization for every time whose required coefficients have already been selected. They are simultaneous path bounds, not a collection of individual-node probability estimates.

Using `C_2=3`, the sums in lines 281--284 satisfy

```text
L_1 <= S[c V_1+2c+ce C_2 T+e^2] <= 0.0925 S T,
L_2 <= 20S[c V_2+2c+ce C_2 T+e^2] <= 1.85 S T.
```

For example `C_3=2` therefore works for both. This supplies an explicit check that the constants in these estimates do not depend on any current backward coefficient or on the eventual horizon `S_0`.

For each fixed `p>=1`, `exp(x)-1<=x exp(x)` and Cauchy--Schwarz give the displayed bound (18). The estimate

```text
lambda T <= eta_0 T^2/2+lambda^2/(2eta_0)
```

and (13) give a uniform finite bound on the last expectation for all `S<=0.1`. Thus a deterministic finite `D_p` exists with `E exp(pL_j)<=1+D_p S`. The convergence to one, rather than only boundedness by a fixed constant, is correctly established.

Taking positive such constants `D_1,D_2`, a valid choice is

```text
S_a = min(1/10, 1/D_1, 3/D_2).
```

Then `E exp(L_1)<=2` and `||exp(L_2)||_2^2=E exp(2L_2)<=4`, which is exactly (19). These estimates have used only the provisional backward threshold one, the fixed forward thresholds 20 and 60, and the accepted primal premises.

## 5. Zero time and the causal selection order

At time zero, `W4_0` is an empty sum. Hence `delta3_0` is identically zero as a formal function, and every time-zero `B3` entry is zero. The variance of every `zeta2_0` coordinate is therefore zero, so its attained value is zero almost surely.

Nevertheless, with `B3_0=0`, the formal expression remains

```text
delta2_0a = phi'(xi2_0a) tau_R2(zeta2_0a).
```

Its derivative in its own `xi2` coordinate is `phi''(xi2_0a)tau_R2(0)=0` on the attained law, and the other `xi2` partials are zero as well. Thus `B2_0=0`. Its formal derivative in its own `zeta2` coordinate is `phi'(xi2_0a)tau_R2'(0)=phi'(xi2_0a)`, which is nonzero. Likewise, `zeta1_0=0` on the law, while the derivative of `delta1_0a` in its own reverse slot is `phi'(G_a)`. This checks every zero-variance claim at lines 308--313. In particular, an attained zero value is not incorrectly promoted to a constant formal function.

At a general time `k`, the response dependencies are:

| Object being estimated | Coefficients it actually needs |
| --- | --- |
| `H1_k` and its reverse response, hence `A2_k` | `B2` rows strictly before `k` |
| `Z2_k`, its forward responses, and `H2_k`'s reverse response, hence `A3_k` | the now-selected `A2` coefficients through `k`, and `B3` rows strictly before `k` |
| `Z3_k`, `delta3_k`, and their top-source responses, hence `B3_k` | the now-selected `A3` coefficients through `k`; no backward row |
| `q2_k`, `delta2_k`, and the response defining `B2_k` | the already-selected current `B3_k`, and the previously established `Z2` responses |
| `q1_k` | the already-selected current `B2_k` |

The covariance terms in each coefficient use fields available at the corresponding point in the stipulated causal order. This verifies that the partial envelopes invoked at each stage have already been justified for the times they cover. There is no same-time `B2`/`B3` cycle.

## 6. Single-source injections and forward responses: (20)--(23)

For clarity, all maxima of responses in this section can be taken over past times and samples, with future source-coordinate derivatives padded by zero. Strictly historical forward updates justify that padding.

Fix one bottom reverse slot `(s,b)` and put `F_j=max_(v<=j,a)|partial Z1_va/partial zeta1_sb|`. It is zero through `j=s`. The direct term in `partial q1_ra` is one only for `(r,a)=(s,b)`. Its contribution to any later bottom preactivation is bounded by `Delta e/2`. There is only one injected sample; it must not be multiplied by two. All propagated terms satisfy

```text
F_j <= Delta e/2
       + Delta sum_(r<j)[c max_a|q1_ra|+e^2] F_r,
```

with the harmless constant term also usable at times before injection. The `c|q1|` term comes from differentiating the feature gate; the `e^2` term comes from the `phi'` factor in `delta1` and the derivative of the returned feature in `q1`. The `B2` row is bounded by one. Multiplying the resulting bound for `F_k` by the final feature gate `e` gives precisely (20):

```text
|partial H1_ka/partial zeta1_sb|
    <= (Delta e^2/2) exp(L_1).
```

The direct forcing is bounded by the same constant for every later `j`; the argument does not assume that the memory coefficient appears only in the first later update.

Cauchy--Schwarz and (4) bound the feature-product term in `A2` by `(2.3)^2`. Taking expectations in (20) and using (19) gives

```text
|A2_ka,sb| <= (Delta/2)[5.29+0.02]
             = 5.31 Delta/2 < 20 Delta/2.
```

This proves the current forward bound before using the current middle state in subsequent coefficient selection.

For the total middle forward-source derivative row `R_j` from line 343, the direct derivative of `xi2_ja` has row sum exactly one. Even if several Gaussian slots coincide almost surely, their formal direct row still has just its own unit entry. Let `F_j=max_(v<=j)R_v`. After differentiating `delta2` and its returned features as at lines 348--349, one gets

```text
F_j <= 1+20 Delta sum_(r<j)[c max_a|q2_ra|+e^2] F_r.
```

Here a `q2` derivative in the `xi2` directions has no direct reverse-source term, since the `zeta2` coordinates are held fixed. The row bound for each past `B3` includes its diagonal and all its earlier times. Product induction yields `F_k<=exp(L_2)`.

For a single reverse slot `zeta2_sb`, the corresponding recurrence has constant direct forcing at most `20 Delta e/2` instead of one. The direct term again occurs for only one sample slot. The final feature derivative contributes one additional factor `e`. This proves (22):

```text
|partial H2_ka/partial zeta2_sb|
    <= (20 Delta e^2/2) exp(L_2).
```

The response contribution to the bracket defining `A3` is therefore at most `20e^2 E exp(L_2)<=40e^2=0.4`. The feature-product contribution is at most `(4.53)^2=20.5209`. Thus (23) is correctly normalized:

```text
|A3_ka,sb| <= (Delta/2)[20.5209+0.4]
             = 20.9209 Delta/2 < 60 Delta/2.
```

Neither response calculation uses a current backward row. The factors `Delta/2`, `e`, and the final feature gate are all accounted for.

## 7. Top derivative, readout derivative, and current B3: (24)--(27)

Write `D^3_j=max_a sum_(s<=j,b)|partial delta3_ja/partial xi3_sb|` and retain the candidate's notation `T_j` for the total `Z3` response row. Differentiating the readout itself gives

```text
sum_(s<=j,b)|partial W4_j/partial xi3_sb|
    <= e Delta sum_(r<j) T_r.
```

The readout has two update samples, which cancel its denominator two; each feature derivative supplies `e`. Differentiating `delta3=tau_Rw(W4)phi'(Z3)` therefore yields

```text
D^3_j <= e^2 Delta sum_(r<j) T_r + c|W4_j| T_j
       <= S(e^2+cK) max_(r<=j)T_r.
```

This is (24). The first term differentiates the readout; the second differentiates the feature gate. Both are present, and the unbounded readout is controlled by the random envelope `K`, not a deterministic cap-dependent constant.

The top forward recursion has a unit direct row and a strictly past sum. Consequently, with `F_j=max_(v<=j)T_v` and `Q=e^2+cK`,

```text
F_j <= 1+60 Delta S Q sum_(r<j)F_r
    <= exp(60 S s_j Q)
    <= exp(60 S^2 Q).
```

This proves (25), including the power `S^2`. No current unknown response occurs inside a same-time feedback equation.

For (26), `K<=C_2T` and the Gaussian-square moment of `T` control every needed polynomial times exponential of `K`. Explicitly, with the permissible `C_2=3`, `Q<=0.085T` and `60S^2Q<=0.051T`. Hence `Q exp(60S^2Q)` is bounded by `0.085T exp(0.051T)`, whose expectation is finite uniformly by (13), Cauchy--Schwarz, and completion of the square. Thus the supremum defining `D_0` is finite over all relevant partial inductions with `S<=0.1`; it does not assume the eventual current backward bound or a choice of `S_0`.

For each fixed coefficient row, absolute values can be moved inside the finite sum and expectation. The derivative contribution to its norm is at most `S D_0`. Cauchy--Schwarz gives for the learned covariance contribution

```text
(Delta/2) sum_(r<k,b)
    ||delta3_ka||_2 ||delta3_rb||_2
 <= Delta sum_(r<k)(0.7S)^2
 <= 0.49 S^3.
```

No sign cancellation or independence is used. The learned term is absent on the time diagonal exactly as required by (3). Since `S^2<=0.01`, this proves (27) with `C_V=D_0+0.0049`.

## 8. Current middle derivative and B2: (28)--(29)

Once `B3_k` has been selected and bounded, the current middle query has total `xi2` derivative row at most

```text
e sum_(v<=k,b)|B3_ka,vb| R_v
    <= e V_k exp(L_2).
```

This includes the current-time feature return. There is no direct `zeta2` injection in these derivative directions. Differentiating `delta2` then gives exactly (28):

```text
sum_(s<=k,b)|partial delta2_ka/partial xi2_sb|
    <= [c|q2_ka|+e^2 V_k] exp(L_2).
```

The bound `exp(L_2)` for `Z2` responses still uses only backward rows strictly before `k`. It therefore remains available before proving anything about the current `B2` row.

Cauchy--Schwarz, rather than an independence claim, now gives

```text
E[|q2_ka| exp(L_2)]
    <= ||q2_ka||_2 ||exp(L_2)||_2 <= 2(7.7)S.
```

Also `E exp(L_2)<=2`, and `V_k<=C_VS` is deterministic. The expected derivative row is thus at most `2[c(7.7)+e^2C_V]S`, as at line 416. The learned covariance contribution is bounded by `(0.77)^2S^3`, by the same two-sample calculation used for `B3`. It follows that

```text
U_k <= C_U S,
C_U = 2[7.7c+e^2C_V]+0.77^2/100
    = 0.390929+0.02C_V.
```

Equation (29) is correct. In particular, the proof does not use a supremum over reverse queries in time, or a higher primal moment of `q2`.

## 9. Self-consistent constants and closure at S_0

The constants have an acyclic order of dependence:

| Constant or threshold | Inputs needed before it is chosen |
| --- | --- |
| `eta_0,C_1` | Gaussian covariance law, (4)--(5), fixed ceiling `S<=0.1` |
| `C_2,C_3` | fixed forward thresholds `20,60`, backward bootstrap threshold `1`, activation bounds, ceiling `0.1` |
| `D_1,D_2,S_a` | preceding envelope and Gaussian-moment constants |
| `D_0` | the top-source envelope and its Gaussian-square moment on the fixed ceiling interval |
| `C_V` | `D_0` and the stated `delta3` primal bound |
| `C_U` | `C_V`, (19), and the stated `q2,delta2` primal bounds |
| `C_B` | `max(C_U,C_V)` |
| `S_0` | `min(S_a,1/10,1/(2C_B))` |

The first constants are obtained uniformly for partial inductions under provisional thresholds; they do not require those thresholds already to hold at every future time. In particular, the supremum in `D_0` is dominated on the fixed interval `S<=0.1`, rather than being defined using the yet-unknown final horizon.

Both `C_U` and `C_V` are finite and positive, so the chosen `S_0` is strictly positive. For any law with `S<=S_0`, start with the verified zero rows at time zero. At each subsequent time the order in Section 5 of this report first establishes the current forward coefficients, then `V_k<=C_VS<=1/2`, then `U_k<=C_US<=1/2`. These improve the provisional threshold one and supply the next induction step. The argument is a finite induction on time, not a bootstrap depending on continuity of a solution or on a mesh limit. It covers `M=1` and `Delta=S`.

There is no requirement in the claim that `S_0` be numerically large or optimized. Finite Gaussian-square moments suffice for the deterministic constant choices actually claimed.

## 10. All-node envelopes, nodewise reverse tails, and clipping: (7), (31)

After closure, the common pathwise envelope holds through `M`:

```text
max_(k,a)|Z^(ell)_ka| <= C_2 T,
max_k |W4_k/S| <= C_2 T.
```

The latter follows from `s_k<=S` and `S>0`. Therefore (13), with a smaller exponent, proves the first two lines of (7). No union over mesh nodes and no independent-copy argument is needed.

For a reverse query at any single node, the now-established complete backward row bound gives exactly the inequalities at lines 440--441. Its source variance is at most one by the primal hypothesis, even at node `M`. The square inequality and convexity suffice to combine this scalar Gaussian with the field envelope, without independence between the query source and its shift.

For an explicit common exponent check, the verified choice `C_2=3` gives

```text
|qj_ka| <= |zetaj_ka|+3T,
|qj_ka|^2 <= 2|zetaj_ka|^2+18T^2.
```

Taking `eta=eta_0/36` yields

```text
E exp(eta |qj_ka|^2)
 <= (1/2) E exp(4eta |zetaj_ka|^2)
    +(1/2) E exp(36eta T^2)
 <= (1/2)(1-8eta)^(-1/2)+(1/2)C_1.
```

The same `eta` works for the forward maxima and normalized readout, since `9eta<=eta_0`. A single finite `C_E` can therefore serve all the bounds in (7). This also verifies explicitly that the final tail constants can be chosen uniformly after the response constants have been fixed.

The claimed distinction between all-node forward bounds and only nodewise reverse bounds is respected. Time Jensen controls an average of reverse-source magnitudes; the proof never turns it into an unproved supremum estimate for reverse queries.

For (31), oddness and monotonicity of the cap imply it has the same sign as its input, and the absolute-value condition prevents overshoot. Together with agreement with the identity on `[-R,R]`, this gives

```text
|Q-tau_R(Q)|^2 <= Q^2 1_(|Q|>R).
```

For the final Gaussian-square exponent `eta`, the quantity `x^2 exp(-eta x^2/2)` is bounded. On `|Q|>R`, it follows that

```text
Q^2 <= [sup_x x^2 exp(-eta x^2/2)]
        exp(eta Q^2) exp(-eta R^2/2).
```

Taking expectations proves (31), with constants independent of the three reference caps. For the readout, `S<=0.1<1` implies `W4^2<=(W4/S)^2`, so the normalized estimate already supplies the required unnormalized one. This step is valid for all the stated `R>=1`.

If the cuts are identities, every inequality used in the response and tail proof still holds: the proof uses contraction in absolute value and a derivative bounded by one, not the finite upper bound `2R`. Accordingly the identity-cut conclusion is valid when that law and its primal hypotheses are separately assumed, exactly as stated. This observation does not construct that law or identify it as a cap limit.

## Independence audit

Mutual independence of the entire stipulated source groups is accepted as part of the law. No later step silently substitutes independent coordinates within a source group or differentiates along random covariance-dependent coordinates.

Specifically, the chaining proof uses a union bound; time averaging uses pointwise Jensen; the common random envelope uses pointwise convexity; feature and delta covariance coefficients use Cauchy--Schwarz; the current middle derivative expectation uses Cauchy--Schwarz; and the final reverse-query estimate again uses convexity. None of these steps factors a source from its response shift or factors two evolved quantities. Singular covariances and coincident Gaussian coordinates cause no exception to these arguments.

## Optional notes

No optional expansion is needed to make the conditional proof valid. For easier future checking, the candidate could display the total-row recurrences underlying (20), (22), and (25), or the constant dependency order above. Its existing product-induction statements do yield those recurrences and bounds; their present compression is not a missing mathematical argument.

The notational reuse of `V` for reverse time averages and backward row norms is explicitly disclosed in the candidate and does not change any estimate. Renaming one would be purely editorial.

## Final scope of acceptance

Accepted: the local, mesh- and cap-uniform response and tail implication (6)--(7), and the single-law clipping consequence (31), under the exact finite Gaussian law and the explicitly accepted primal hypotheses. No required correction to this implication was identified.

Not assessed or certified: any of the construction, identification, limiting, comparison, or global-training obligations disclaimed at lines 466--473. Their absence is not counted as a defect in this conditional lemma.
