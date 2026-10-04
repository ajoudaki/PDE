# Restoring autonomous scalar feedback: a conditional all-time lemma

2026-10-01. This is a contained analytic implication for the smooth study,
not a claim that its law-consistency hypotheses have already been verified.
The exact model is in SMOOTH_SETUP.md. The population target must remain the
own smooth population, never a finite-width conditional mean.

The cavity route first supplies deterministic histories obtained by averaging
the actual residuals, clock, and memory contractions. Even a complete
population theorem with those histories held fixed would leave a second
step: showing that their feedback agrees with the autonomous population.
The following lemma states a sufficient, integrable form of that step.

## Damped residuals and finite activity

Let n be a positive integer. Let D and R be nonnegative continuous functions
of physical time. In the intended application D controls differences of
hidden-population observables, contractions, clock, and response kernels;
R controls the training-residual difference. Assume, for every t >= 0,

\[
D(t)\le a n^{-1/2}
 +C\int_0^t [b(s)D(s)+R(s)]\,ds,
\tag{1}
\]
\[
R(t)\le a n^{-1/2}v(t)
 +C\int_0^t e^{-\kappa(t-s)}b(s)D(s)\,ds.
\tag{2}
\]

Here a,C,kappa are positive constants independent of width and horizon,
b and v are nonnegative, B=integral b < infinity, and V=integral v <
infinity. Then

\[
\sup_{t\ge0}D(t)
 \le \frac{a(1+CV)}{\sqrt n}
          \exp\{C(1+C/\kappa)B\},
\tag{3}
\]
\[
\int_0^\infty R(t)\,dt
 \le \frac{aV}{\sqrt n}
       +\frac{CB}{\kappa}\sup_tD(t).
\tag{4}
\]

Indeed, Tonelli's theorem applied to the nonnegative convolution in (2)
gives integral_0^t R <= a V/sqrt(n) + (C/kappa) integral_0^t b D.
Substitute this into (1) and apply the scalar integral Gronwall inequality
with coefficient C(1+C/kappa)b. This proves (3); letting t tend to infinity
in the integrated residual bound proves (4). If b(t) <= B0 exp(-beta t)
and v(t) <= V0 (1+t)^p exp(-beta t), substituting (3) into (2) also gives
an integrable polynomial-times-exponential root-width bound for R.

The crucial hypothesis in (2) is an integrable discrepancy in the residual
equation. A uniform bound on prediction values alone does not imply (2).
Differentiating a bound on a state or prediction error does not prove it.

## The residual norm does not require a second derivative

Let bar r_n and bar rho_n be conditional means on the initialized fitting
event. Since rho_n=||r_n||_m and a norm is 1-Lipschitz,

\[
|\bar\rho_n(t)-\|\bar r_n(t)\|_m|
 \le E[\|r_n(t)-\bar r_n(t)\|_m\mid\mathcal G_n].
\tag{5}
\]

Consequently, if the centered residual bound is a v(t)/sqrt(n),

\[
|\bar\rho_n(t)-\rho_\infty(t)|
 \le \|\bar r_n(t)-r_\infty(t)\|_m
          +a v(t)/\sqrt n.
\tag{6}
\]

Integrating (6) controls the clock difference by (4). Thus the nonsmooth
norm at a fitted endpoint is compatible with this first-difference
restoration. An all-time Hessian of the residual norm is unnecessary.

## What would constitute a complete positive conclusion

To apply this lemma to the actual smooth closure, the two-sided population
map must yield (1) in a specified common norm, and the finite-width
consistency estimate for the true prediction velocity must yield (2).
In the latter, the upper derivative factor is w sech^2(z), not its smooth
clip. The passive lower observable dot h/rho proposed in the cavity route
is a way to obtain a velocity estimate without differentiating an error
bound. That proposal still requires its full quantitative proof.

If those hypotheses establish

\[
E\left[\int\sup_{t\ge0}|f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2
 \,d\mu(x)\mid\mathcal G_n\right]\le C/n,
\tag{7}
\]

and P(G_n complement) <= C0 exp(-c n), then there is already an
unconditional fixed-confidence full-population theorem. For every
delta in (0,1), Markov's inequality and a union bound give

\[
P\left\{\left(\int\sup_{t\ge0}
 |f_{n,M}-f_{\infty,M}|^2\,d\mu\right)^{1/2}
 >\sqrt{C/\delta}\,n^{-1/2}\right\}
 \le\delta+C_0e^{-cn}.
\tag{8}
\]

This includes the finite-width mean bias, with no additive fixed-label
remainder. It does not assert an all-initialization all-time second moment:
that stronger assertion additionally requires a moment bound on the
exceptional event. These two conclusions must not be conflated. Conversely,
the exceptional-event moment issue is not a reason to withhold (8) if (7)
has actually been proved.

**Status:** equations (3)--(6) and the implication (7) => (8) are proved
here. Equations (1), (2), and (7) for the actual population comparison are
explicit remaining hypotheses, not new established study results.
