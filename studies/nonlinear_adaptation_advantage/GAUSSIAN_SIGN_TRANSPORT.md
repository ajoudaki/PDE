# Frozen follow-up: transporting the Gaussian covariance signs

Date: 2026-09-12. Author: scoped `gaussian_sign_route` agent.

**Result.** No sign at the fitted endpoint is proved. The exact covariance
transport equation is derived below, with its actual first-layer/adjoint
remainder exposed. A proposed pointwise ordering cone is **false for the
actual reference flow**: at every sufficiently small positive feature time,
a positive-probability set of second-layer coordinates reverses its initial
anchor-contrast ordering. The proof retains the reused Gaussian action and
its response terms, and has an `O(s^4)` strong remainder; it is not a formal
time jet. This defeats that particular cone argument, not the possibility
that the expected covariance signs persist to the fitted endpoint.

This is a bounded follow-up to `ROUTE_GAUSSIAN_SIGN.md`, whose early-reference
covariance sign theorem is preserved. No other route or review was inspected.
No experiments, changed task family, alternate optimizer, or Git writes were
used. Only this assigned artifact was written.

## 1. Inputs and conventions

The allowed established inputs and exact network/clock/metric conventions
are those recorded in the frozen source report. The present derivation uses
its definitions and proof, the full reference equations in C.4.5.1–2, their
source/tail proof, A.1–A.4, and the contained finite Gaussian program/source
rules in `docs/special_data_limits.md` III.F. The first-layer contribution is
retained throughout, with the actual initialized action and adjoint.

No trained field below is assumed jointly Gaussian. Only the explicitly
identified initial variables and finite-program innovation are Gaussian.

To remove label signs from the formulas without changing the problem, write

\[
v_1=w_1,\quad v_2=-w_2,\quad H_a=\tanh v_a,\quad z_a=AH_a,
\quad T_a=\tanh z_a,\quad S_a=\operatorname{sech}^2z_a,
\]
\[
m_a=\operatorname{sech}^4v_a,\quad
h=\tfrac12(T_1+T_2),\quad \delta_a=cS_a,\quad Q_a=A^*\delta_a.
\tag{T1}
\]

All variables except `v_a,H_a,m_a,Q_a` live on population 2. The latter four
live on population 1, and `A:H1->H2` has its actual Hilbert adjoint. The pair
`(-e2,+1)` is exactly equivalent to `(e2,-1)` for the odd network. Thus (T1)
is only an algebraic relabeling of the actual reference equations, not a
different learning problem.

Let

\[
v_0=E\tanh^2G\in(0.39,0.4),\quad X=z_1(0),\quad Y=z_2(0),
\quad \xi_+=X+Y,\quad \xi_-=X-Y.
\tag{T2}
\]

Then `X,Y` are independent `N(0,v0)`, exactly as in the source report. With
its matrix `B`, define

\[
\beta_\pm(s)=e_\pm^TB(s)e_\pm
 =\frac1{2v_0}E_2[\xi_\pm c(s)(S_1(s)\pm S_2(s))].
\tag{T3}
\]

The established initial slopes are

\[
b_+^0=\tfrac12(\eta+\mu^2)>0,\qquad
b_-^0=\tfrac12(\eta-\mu^2)\le-D/5<0,
\tag{T4}
\]

where `mu,eta,D` have their definitions in the source report.

## 2. Exact transport, including the first-layer remainder

The actual reference equations in these coordinates are

\[
c'=h,\qquad v_a'=\tfrac12\operatorname{sech}^2(v_a)Q_a,
\quad H_a'=\tfrac12m_aQ_a,
\quad A'=\tfrac12\sum_b\delta_b\otimes H_b.
\tag{T5}
\]

Primes throughout this report mean reference feature time `s`. Let
`L_ab=<H_a,H_b>_1`. Product differentiation gives exactly

\[
z_a'=\tfrac12\sum_bL_{ab}\delta_b+\mathcal R_a,
\qquad \mathcal R_a=\tfrac12A(m_a A^*\delta_a).
\tag{T6}
\]

The term `R_a` is the first-row contribution to the current second
preactivation. It is an actual-state expression, including all prior source
reuse, not independent noise newly inserted into the evolution.

Equivalently, on `H2 direct-sum H2`, define

\[
(\mathcal L\delta)_a=\sum_bL_{ab}\delta_b+A m_a A^*\delta_a.
\]

Here multiplication by `m_a` is a bounded positive operator. Consequently
`L` is a Gram matrix, `A m_a A*` is self-adjoint positive semidefinite, and
`mathcal L` is self-adjoint positive semidefinite. Nevertheless

\[
z'=\tfrac12\mathcal L\delta,\qquad
\delta_a'=hS_a-2cT_aS_a z_a'
\tag{T7}
\]

contain multipliers of changing sign. Positivity of `mathcal L` in its
Hilbert metric is not positivity of its coordinate action and does not
control the mixed pairing with the fixed Gaussian variables in (T3).

**Exact covariance transport.** The two covariances are strongly `C1` and

\[
\beta_\pm'(s)=\frac1{2v_0}E[\xi_\pm h(S_1\pm S_2)]
 -\frac1{v_0}E[\xi_\pm c(T_1S_1z_1'\pm T_2S_2z_2')].
\tag{T8}
\]

All products are integrable. Indeed `c` is bounded on a finite feature
horizon, the tanh gates are bounded, `z_a'` is in `L2` by (T6), and
`xi_pm` is fixed in `L2`. The strong chain and product rules from A.4 or
III.F.9 give (T7). They then permit pairing with `xi_pm`, establishing (T8)
without differentiating an unrestricted `L2` Nemytskii map.

In integral form the precise transport remainder is

\[
\begin{aligned}
\beta_\pm(s)-s b_\pm^0
={}&\frac1{2v_0}\int_0^s E\{\xi_\pm[
 h(t)(S_1(t)\pm S_2(t))-h(0)(S_1(0)\pm S_2(0))]\}\,dt\\
&-\frac1{v_0}\int_0^s E[\xi_\pm c(t)
 (T_1S_1z_1'\pm T_2S_2z_2')]\,dt.
\end{aligned}
\tag{T9}
\]

Substituting (T6) splits the second line into the learned-middle rank part
and the first-row part. The latter is exactly

\[
-\frac1{v_0}\int_0^s E[\xi_\pm c(t)
 (T_1S_1\mathcal R_1\pm T_2S_2\mathcal R_2)]\,dt.
\tag{T10}
\]

Thus the missing information is a signed, current-gate-weighted mixed
correlation involving `A m_a A* delta_a`, in addition to the other terms in
(T9). The scalar values `beta_+,beta_-` do not specify these functions or
these weighted expectations. No closed differential inequality for them
has been established here.

The bounds from the actual reference give
`M=2+sqrt(10)`, `||A||<=M`, `||c||2<=min(s,sqrt(10))`, and `||c||infinity<=s`.
Equation (T6) implies

\[
\|z_1'\|_2+\|z_2'\|_2
 \le(2+M^2)\min(s,\sqrt{10}).
\]

Consequently valid but unsigned bounds are

\[
|\beta_\pm'(s)|\le\sqrt{2/v_0}
 [1+s(2+M^2)\min(s,\sqrt{10})],
\tag{T11}
\]
\[
\begin{aligned}
|\beta_\pm(s)-sb_\pm^0|
\le{}&2\sqrt{2/v_0}\,s\\
&+\sqrt{2/v_0}(2+M^2)
        \int_0^s t\min(t,\sqrt{10})\,dt.
\end{aligned}
\tag{T12}
\]

For the first term use `|h(S1±S2)|<=2` twice and
`||xi_pm||2=sqrt(2v0)`. For the second use (T6) and Cauchy–Schwarz.
The first coefficient in (T12) alone exceeds either possible initial slope
magnitude (both are at most one). It supplies no endpoint sign margin.

In fact the fitted feature endpoint is not in an arbitrarily small feature
interval: `b(s)=<c,h><=s` because both `|h|<=1` and `|c|<=s`. Since
`b(s_dagger)=1`,

\[
1\le s_\dagger\le10.
\tag{T13}
\]

No inequality in (T9)–(T12) permits continuing (T4) to that endpoint.

## 3. The natural ordering cone and its exact obstruction

The exchange symmetry of the two equal-label representations in (T1) gives
`L11=L22=:ell` and `L12=L21=:m`; uniqueness of the reference and invariance
of the initial Gaussian law justify this equality of deterministic moments.
Since the Gram is positive semidefinite, `ell±m>=0`. Put
`a=z1+z2`, `d=z1-z2`. Equation (T6) becomes

\[
a'=\tfrac12(\ell+m)c(S_1+S_2)+\mathcal R_1+\mathcal R_2,
\]
\[
d'=-(\ell-m)c h(T_1-T_2)+\mathcal R_1-\mathcal R_2.
\tag{T14}
\]

The second identity uses the exact tanh relation

\[
S_1-S_2=-(T_1+T_2)(T_1-T_2)=-2h(T_1-T_2).
\tag{T15}
\]

In particular the negative covariance can be written

\[
\beta_-(s)=-\frac1{v_0}E[\xi_- c h(T_1-T_2)].
\tag{T16}
\]

A sufficient pointwise cone for its negativity would require
`c h>=0` and `xi_- d>=0`, because tanh is strictly increasing. The analogous
sum alignment `xi_+c>=0` would imply nonnegative `beta_+` directly from (T3).
These are sufficient conditions, not necessary conditions for either
covariance sign.

Let

\[
b(s,\omega)=
\begin{cases}(T_1-T_2)/(z_1-z_2),&z_1\ne z_2,\\
\operatorname{sech}^2z_1,&z_1=z_2.
\end{cases}
\]

This is a continuous scalar gate with `0<b<=1`. Then, with
`lambda=(ell-m)c h b`, the exact integrating-factor identity is

\[
d(s)=e^{-\int_0^s\lambda}
 \left[\xi_-+\int_0^s e^{\int_0^t\lambda}
               (\mathcal R_1-\mathcal R_2)(t)\,dt\right].
\tag{T17}
\]

The formula holds for almost every population-2 coordinate using the
absolutely continuous representatives from the strong equations. Its
integrals exist on finite horizons, since `c` and the gates are bounded and
the remainder is Bochner-integrable in `L2`. It needs no sign of `lambda`.
The missing contrast-order condition is precisely the signed accumulated
forcing in (T17). Its norm bound cannot be compared pointwise with
`|xi_-|`, whose Gaussian law has positive density arbitrarily close to zero.

This is more than a missing estimate: the proposed contrast ordering itself
fails on the actual reference, as proved next.

## 4. Actual reversal of the initial contrast ordering

**Theorem (failure of the pointwise ordering cone).** There is `s1>0` such
that every deterministic `0<s<s1` satisfies

\[
\Pr\{X-Y>0,\ z_1(s)-z_2(s)<0\}>0.
\tag{T18}
\]

These are the actual continuous-reference fields on their common generated
probability space. Thus `sign(z1-z2)=sign(X-Y)` is not an invariant of this
reference. The theorem does not say that `beta_-` becomes nonnegative;
indeed its negative sign at sufficiently small time is already proved.

### 4.1 A controlled strong expansion

First obtain a local moment bound directly from the established source proof.
Run C.4.5.2 §§3–4 with terminal feature horizon `0<S<=1`, still using its
valid outer ball `M=7,C=4`. Its formulas give

\[
E_S=e^{8S+28S^2}\le e^{36},\quad
P_S=8S+\tfrac12\le17/2,\quad K_S=\max(1,14S)\le14.
\]

The sum of reverse response coefficients is therefore at most
`2 S P_S K_S E_S + S C² + 2 S <= (238e^36+18)S`. The reverse Gaussian
source variance is at most `S²`, using the actual `|c(t)|<=t<=S`, rather
than the looser outer-ball variance. Passage of this decomposition to the
actual flow is exactly the strong source-isometry passage in §4 of that
proof. It follows that

\[
\|Q_a(t)\|_4\le C_Q S\quad(0\le t\le S),\qquad
C_Q=3^{1/4}+238e^{36}+18.
\]

Taking `S=t` gives

\[
\|Q_a(t)\|_4\le C_Q t\qquad(0<t\le1).
\tag{T19}
\]

This specialization changes no source rule. The bound is very large but
finite; only its order at zero is needed below. In particular it is a
quantitative moment bound, not an assumed Taylor radius.

Write the initial first fields as `H_a^0=tanh(v_a(0))`, let
`m_a^0=sech^4(v_a(0))`, and put

\[
h_0=\tfrac12(\tanh X+\tanh Y),\qquad
d_a^0=h_0\operatorname{sech}^2X_a,\qquad
q_a^0=A_0^*d_a^0,
\quad (X_1,X_2)=(X,Y).
\tag{T20}
\]

The following orders are norm estimates with fixed finite constants on a
neighborhood of zero, not formal series:

\[
\begin{aligned}
v_a-v_a(0)&=O_{L^4}(s^2),&K&=O_{HS}(s^2),&z_a-X_a&=O_{L^2}(s^2),\\
c-sh_0&=O_{L^2}(s^3),&\delta_a-sd_a^0&=O_{L^2}(s^3),
&Q_a-sq_a^0&=O_{L^2}(s^3).
\end{aligned}
\tag{T21}
\]

Here is a complete justification. Integrate (T19) in the first equation
for `v_a` to obtain `||v_a-v_a(0)||4<=C_Q s²/4`. The rank equation and
`||delta_a||2<=s` give `||K||HS<=s²/2`. Bounded action and the Lipschitz
activation then imply `z_a-X_a=O_L2(s²)`. Integrate the resulting
`h-h0=O_L2(s²)` to obtain the readout estimate. In the delta difference,
subtract `c-sh0` and then use the bounded derivative of `sech²` and
`|h0|<=1`; both errors are `O_L2(s³)`. Finally write
`Q_a-sq_a^0=A0*(delta_a-sd_a^0)+K*delta_a`; the two terms have that same
order. Also `q_a^0` is in `L4`: (T19) bounds `Q_a(s)/s` uniformly in `L4`,
and its `L2` limit is `q_a^0`, so an almost surely convergent subsequence
and Fatou give `||q_a^0||4<=C_Q`.

Now subtract the leading term from `v_a'`. The error from
`Q_a-sq_a^0` is `O_L2(s³)`. The remaining error is bounded using Hölder:

\[
s\|[\phi'(v_a)-\phi'(v_a(0))]q_a^0\|_2
 \le2s\|v_a-v_a(0)\|_4\|q_a^0\|_4=O(s^3).
\]

Integration and the rank equation yield

\[
v_a=v_a(0)+\frac{s^2}{4}\phi'(v_a(0))q_a^0+O_{L^2}(s^4),
\quad
K=\frac{s^2}{4}\sum_b d_b^0\otimes H_b^0+O_{HS}(s^4).
\tag{T22}
\]

The scalar tanh remainder is at most `|v_a-v_a(0)|²`, whose `L2` norm is
`O(s^4)` by the `L4` bound already proved. Therefore

\[
H_a=H_a^0+\frac{s^2}{4}m_a^0q_a^0+O_{L^2}(s^4).
\]

At initialization `<H_a^0,H_b^0>=v0 1_(a=b)`. Multiplying the two expanded
factors in `z_a=(A0+K)H_a` gives

\[
z_a(s)=X_a+\frac{s^2}{4}
        [v_0d_a^0+A_0(m_a^0q_a^0)]+O_{L^2}(s^4).
\tag{T23}
\]

Every mixed operator error has the stated norm by `||K||op<=||K||HS`.
This proves the strong remainder needed to infer a positive-probability
event from the leading term.

### 4.2 The reused-action innovation is nondegenerate

Apply the exact III.F source rules to the fixed program with initial
forwards `X=A0H1^0`, `Y=A0H2^0`, the two reverse inputs `d_a^0`, and then
one additional forward query. The backward rules give

\[
q_1^0=\zeta_1+\frac\eta2H_1^0+\frac{\mu^2}2H_2^0,\qquad
q_2^0=\zeta_2+\frac{\mu^2}2H_1^0+\frac\eta2H_2^0.
\tag{T24}
\]

The reverse Gaussian pair is independent of the full first-row root and has
covariance

\[
E\zeta_1^2=E\zeta_2^2=:\gamma_d=E[(d_1^0)^2],\qquad
E\zeta_1\zeta_2=: \gamma_o=E[d_1^0d_2^0]\ge0.
\]

The diagonal derivatives in the source
rule are `eta/2` and the off-diagonal ones `mu²/2`, by the explicit Gaussian
calculation in the source report.

Set

\[
r=m_1^0q_1^0-m_2^0q_2^0,\quad
\bar m=E\operatorname{sech}^4G,\quad
\kappa=E[\operatorname{sech}^4G\tanh^2G],
\quad
\alpha=\frac{\eta\kappa-\mu^2\bar m v_0}{2v_0}.
\tag{T25}
\]

In the new forward call, `E partial_(zeta1)r=bar m` and
`E partial_(zeta2)r=-bar m`. Its actual response is therefore

\[
A_0r=\xi_r+\bar m(d_1^0-d_2^0).
\tag{T26}
\]

The source `xi_r` is jointly Gaussian with `X,Y`. Independence and oddness
in the two first-row roots give

\[
E[rH_1^0]=\tfrac12(\eta\kappa-\mu^2\bar m v_0)=\alpha v_0,
\quad E[rH_2^0]=-\alpha v_0.
\]

For example the term `mu² m1 H2 H1/2` has zero expectation by oddness,
whereas `-mu² m2 (H1)²/2` has expectation `-mu² bar m v0/2`.
These are exactly the source cross-covariances by III.F.4. Gaussian
orthogonal projection consequently yields

\[
\xi_r=\alpha(X-Y)+\sigma G_*,
\tag{T27}
\]

where `G_*` is standard normal independent of `X,Y`. The variance `sigma²`
is strictly positive, as follows without assuming any independence of the
actual forward and reverse answers.

Indeed, the part `m1^0 zeta1-m2^0 zeta2` of `r` has zero conditional mean
given the first-row root. It is orthogonal both to all root-only functions
and to the span of `H1^0,H2^0`. Hence subtracting the projection onto that
span from `r` leaves its variance intact. The smallest eigenvalue of the
reverse source covariance is

\[
\gamma_d-\gamma_o=\tfrac12E[h_0^2(S_X-S_Y)^2]>0,
\quad S_X=\operatorname{sech}^2X,\quad S_Y=\operatorname{sech}^2Y.
\]

Strictness holds because the complement of the finitely many lines
`X=Y`, `X=-Y` has positive Gaussian measure, and the integrand is positive
there. Therefore

\[
\sigma^2\ge2(\gamma_d-\gamma_o)E[\operatorname{sech}^8G]>0.
\tag{T28}
\]

The fixed program uses products of bounded smooth gates with Gaussian-plus-
bounded reverse fields. Its values and named derivatives are covered by A.2
and the derivative-valid clipping argument of C.4.5.2 §2. Thus (T24)–(T28)
are legitimate actual-action identities. The response in (T26) is essential;
it has not been dropped or replaced by an independently resampled transpose.

Subtracting the two expansions in (T23) and using (T26)–(T27) now gives

\[
\begin{aligned}
z_1(s)-z_2(s)=X-Y+\frac{s^2}{4}\{&\alpha(X-Y)+\sigma G_*\\
&+(v_0+\bar m)h_0(S_X-S_Y)\}+E_s,
\qquad \|E_s\|_2\le C s^4.
\end{aligned}
\tag{T29}
\]

The constant `C` is finite and independent of `s` on a sufficiently small
fixed interval; its existence was derived in §4.1. The potentially large
constants affect how small that interval is, not the positive-probability
conclusion. In particular the first-row term has a genuine additive Gaussian
innovation transverse to the initial contrast. It is not a scalar multiple
of that contrast.

### 4.3 A positive-probability crossing in the actual flow

The Gaussian variables `a=X+Y`, `d0=X-Y`, and `G_*` are independent, with
`a,d0~N(0,2v0)`. For small `s`, consider the event

\[
\mathcal A_s=\{|a|\le1,\quad
        0<d_0<\sigma s^2/16,\quad -2\le G_*\le-1\}.
\tag{T30}
\]

There is a constant `c0>0` such that `Pr(A_s)>=c0 s²` for all sufficiently
small `s`: the first and third events have fixed positive probability; on
the shrinking second interval the centered Gaussian density is bounded
below by a fixed positive number.

Since `sech²` is two-Lipschitz,
`|S_X-S_Y|<=2|d0|`. Thus the non-Gaussian term in braces in (T29), together
with `alpha d0`, is bounded in magnitude by `C1|d0|`, with fixed
`C1=|alpha|+2(v0+bar m)`. On `A_s`, the expression in (T29) before `E_s`
is at most

\[
\frac{\sigma s^2}{16}-\frac{\sigma s^2}{4}
       +\frac{C_1\sigma s^4}{64}
\le-\frac{\sigma s^2}{8}
\]

after decreasing `s`. On the other hand Chebyshev's inequality and the
strong remainder give

\[
\Pr\{|E_s|>\sigma s^2/16\}
 \le(16C/\sigma)^2s^4.
\tag{T31}
\]

This is smaller than `c0 s²` for all sufficiently small positive `s`.
Hence `A_s` intersects `|E_s|<=sigma s²/16` in positive probability. On
that intersection `d0>0` but the actual difference is strictly negative.
This proves (T18). No conditioning on a probability-zero hyperplane, formal
series inference, or sample experiment is involved. ∎

## 5. Consequence for the endpoint question

The early-reference **expected** covariance signs remain as previously
proved. The new theorem concerns a stronger pathwise order assertion, which
is false even while the negative contrast covariance holds. Thus its
failure does not contradict the earlier result.

The exact transport remainder (T9)–(T10) remains the necessary object. A
successful endpoint proof could still exploit cancellations in its expected
weighted contractions; it cannot rely on preservation of the initial
pointwise contrast ordering. The positive semidefinite operator in (T7)
does not control the required Gaussian mixed pairing, and the actual
first-layer term produces the transverse innovation in (T29). This is a
concrete obstruction to the natural order-cone argument, not merely an
absence of a convenient estimate.

No closed inequality with a verified inward boundary condition for
`(beta_+,beta_-)` has been obtained. No theorem giving either covariance
sign at `s_dagger` is claimed. No inference about a favorable added-time
risk gap follows: both E₀ learners inherit the same reference, and the
population risk contraction required by the contract is a different signed
quantity involving all projected raw tangent blocks.

| Claim | Current status |
|---|---|
| Early actual mixed covariance signs from the source report | Preserved |
| Exact actual reference covariance transport (T8)–(T10) | Proved |
| Initial contrast ordering is a pointwise invariant cone | Falsified for the actual reference by (T18) |
| Every possible invariant cone or covariance inequality fails | Not claimed |
| A sign of either covariance at the fitted endpoint | Open |
| E₀ finite-time advantage or relative component benefit | Open; unchanged by this follow-up |

## 6. Check and provenance

This report was analytically self-checked for the label change, population
types, factors of two, Gram signs, source-response contractions, nonzero
innovation variance, actual `L2` remainder order, and the probability scaling
in (T30)–(T31). It has not received an independent audit and is not promoted.
The source report is not superseded: this follow-up adds an exact transport
identity and a failure theorem for one stronger proposed invariant.

At the pre-write metadata check HEAD was
`d6dab473d1daf2134896603a13dd4afdb45d1d7e`, with empty staged index. The
shared instructions and established scientific source hashes matched those
in the original report. No source or instruction change requiring a
different argument was observed.

```text
ROUTE_GAUSSIAN_SIGN.md
2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c
AGENTS.md
7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba
RESEARCH_WORKFLOW.md
8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12
docs/global_nonlinear.md
5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483
docs/special_data_limits.md
5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
```
