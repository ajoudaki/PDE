# Growing smooth clipping levels

2026-10-01. Continuation explicitly requested by the user. Internally
checked theorem below; see M_SCALE_CHECK.md. Not promoted to the
paper or book. The conclusion permits a diverging cap, but is weaker than
a cap-independent root-width constant.

The subsequent M_LOG_SCALE_RESULT.md improves the cap prefactor and
minimum-width requirement to single exponential in M. This intermediate
argument and its separate audit are retained as a research record.

## Question and exact target

Keep the model in SMOOTH_SETUP.md, including both recursive smooth clips,
the original Gaussian mixer and its actual transpose, q=1 memories, and
the residual-RMS clock. The fixed label vector must remain nonzero and
independent of width. Seek a common positive small-label threshold for
growing clipping levels M>=1.

The error under investigation is

\[
 E_{n,M}=\left(\int\sup_{t\ge0}
 |f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

Here f_infinity,M is the own smooth-closure population, not a finite-width
mean or a dense trained predictor. A diagonal choice M=M(n) changes this
target with n. Comparison with a single unclipped population requires a
separate cap-removal theorem.

Three distinct conclusions must not be conflated: an M-independent
constant in a root-width bound; an explicit M-dependent root-width bound
that permits a diverging cap and a slower rate; and convergence of the
moving population target to an unclipped target.

## Current input and delegation

Scientific inputs are this study's complete relevant smooth-clipping
derivations and checks and its already authorized manuscript/book
dependencies. No other study is used. Three scoped independent routes
examine cavity constants, covariance/response law stability, and cap
schedules. New results remain internal research, not manuscript claims.

The cap-independent fitting estimate is already available: it uses
only |c_M(s)|<=|s|, so one fixed small label size yields exponential
fitting and bounded total residual activity for all M>0. The current
fixed-M statistical theorem additionally has a cap-dependent smallness
condition. Removing that statistical restriction, or proving it uniform,
is necessary before a fixed-label diagonal schedule is justified.

## 1. A common-label growing-cap theorem

Assume the exact two-hidden-layer tanh model above, finite fixed training
data, canonical independent Gaussian initialization, a positive initial
population readout-feature Gram gap, and a probability measure mu with
bounded query support. There is a positive label threshold Y_* independent
of M>=1. Fix one label vector with 0<Y<Y_*; the labels do not change with n
or M. Constants below may depend on these fixed data and labels.

For some C,c>0 define

\[
 T_C(M)=\exp\!\bigl(\exp(\exp(C(1+M)))\bigr).
 \tag{1}
\]

After increasing C to include fixed minimum-width requirements, for
every M>=1 and n>=T_C(M)^4 the own-population error satisfies

\[
 \left(\mathbb E[E_{n,M}^2\mid\mathcal G_n]\right)^{1/2}
 \le \frac{T_C(M)}{\sqrt n},
 \qquad \Pr(\mathcal G_n^c)\le Ce^{-cn}.
 \tag{2}
\]

The initialized fitting event G_n is the same for every cap. It bounds
the norm of the original Gaussian mixer and puts a positive lower bound
on the initial readout-feature Gram. In particular, for every fixed
delta in (0,1),

\[
 \Pr\left\{E_{n,M}>\frac{T_C(M)}{\sqrt{\delta n}}\right\}
 \le\delta+Ce^{-cn}.
 \tag{3}
\]

This is a bound for each chosen deterministic M, with explicit common
constants. It does not put a supremum over all M inside the expectation.
The time supremum is already inside E_{n,M}; convergent fitted endpoints
are included. The minimum-width condition is deliberately conservative.

Set

\[
 N_*=\exp(\exp(\exp 1)),\qquad
 M(n)=\sqrt{\log\log\log(n+N_*)}.
 \tag{4}
\]

Then M(n)>=1, M(n) tends to infinity, the width condition in (2) holds
eventually, and

\[
 \left(\mathbb E[E_{n,M(n)}^2\mid\mathcal G_n]\right)^{1/2}
 \le n^{-1/2+o(1)}.
 \tag{5}
\]

Equivalently, for every epsilon>0 the conditional RMS error is at most
n^(-1/2+epsilon) for all sufficiently large n. Formula (3) gives the
corresponding unconditional fixed-confidence statement. The o(1) is a
deterministic exponent, not a width-independent bias remainder.

## 2. Fitting and deterministic feedback need no shrinking labels

Let S(t)=integral_0^t rho and S_0=Y/lambda, with the fixed damping margin
lambda from the initialized fitting estimate. The proof uses only
|c_M(s)|<=|s|. Consequently the same choice of Y_* gives, uniformly in M,

\[
 \rho(t)\le Ye^{-\lambda t},\qquad S(\infty)\le S_0,
 \quad \|w\|_\infty\le2S(t),\quad
 \|v_a\|_\infty\le C S(t)^2,\quad \|k_a\|_\infty\le1.
 \tag{6}
\]

The normalized lower-signal norm is bounded by C S(t), although its
coordinate cap is M. The state and residual first-difference estimates,
proved in M_CAP_SCHEDULE_ROUTE.md, therefore have the form

\[
 D^+D\le C(1+M)\rho_1 E+C R,\qquad
 D^+R\le-\kappa R+C(1+M)\rho_2 E.
 \tag{7}
\]

Here D is normalized state distance, E adds mixer distance, R is residual
distance, and kappa>0 is independent of M. In the first inequality the
coefficient of R uses the normalized signal norm and has no M factor.
The second inequality absorbs hidden-motion coefficient VALUES, which
are O(S_0^2), rather than their cap-dependent Lipschitz constants.

Integrating the damped residual inequality first and using finite total
activity gives constants bounded by a polynomial in M times exp(CM).
The same estimate controls scalar freezing, centered Gaussian
concentration of the actual prediction velocity, and final autonomous
feedback restoration. None of these steps requires Y to decrease with M.

## 3. Explicit local Gaussian constants

For F_M(alpha,p)=M tanh(p sech^2(alpha)/M) and every fixed derivative order,
M_UNIFORM_CAVITY_ROUTE.md proves

\[
 |\partial_\alpha^jF_M|\le C_j M,
 \qquad
 |\partial_\alpha^a\partial_p^bF_M|\le C_{a,b}\quad(b\ge1).
 \tag{8}
\]

On the upper branch p=w is bounded by (6), so its pure preactivation
derivatives are bounded independently of M as well. For the finite
prescribed-history graph, with K_W=||W_0||op, its state Jacobian obeys

\[
 \|L(t)\|_{\rm op}\le C\rho(t)(1+M+K_W^2).
 \tag{9}
\]

The M term does not multiply K_W^2: it comes only from the direct lower
preactivation derivative. Fixed-order tangent, tagged-remainder, and
normalized-trace sensitivity constants are bounded by

\[
 C(1+M)^b(1+K_W)^b
       \exp\{C S_0(1+M+K_W^2)\}.
 \tag{10}
\]

Every higher variation solves a linear equation with the same Jacobian;
its source contains only finitely many products of lower variations.
Thus (10) has one exponential. The Gaussian operator tail integrates
the K_W factor for all sufficiently large widths with a threshold
independent of M. On a fixed operator cutoff, and after integration over
the full forced Gaussian law, the needed constants are bounded by

\[
 B_M=\exp(C(1+M)).
 \tag{11}
\]

This includes a coarse deterministic container for the empirical cavity
and expected covariance/response tuples. It is not asserted to be an
invariant domain for the entire law map. Using such an assertion would
reintroduce an unjustified cap-dependent smallness condition.

The scalar upper reinsertion equation has only a past response integral;
its lower counterpart places the instantaneous upper response atom
inside the read-in ODE. Both are causal integral equations. Replacing
the earlier small-activity absorption by ordinary integral Gronwall gives
scalar derivative and reinsertion constants at most

\[
 A_M=\exp(\exp(C(1+M))).
 \tag{12}
\]

The original Gaussian row/column removal and tagged-variation estimates
then yield a finite mean-law consistency defect at most A_M/sqrt(n).
Cutoff replacement adds A_M exp(-cn), absorbed in the same bound.
The passive feature-velocity calculation gives its physical velocity
version with the extra factor rho(t), hence an integrable error source.
The original mixer and its actual transpose remain in every calculation.

## 4. The new step: causal stability of the complete population law

The law variables and their exact scalar equations are those in
SMOOTH_MEAN_MAP_ROUTE.md. Let H=(C_h,Q_h) consist of the lower feature
covariance and its regular response density. Let Dlaw=(C_d,D,Q_d)
consist of the upper backward-signal covariance, its instantaneous
response atom, and its regular response density. The two maps are
Hout=L(Dlaw) and Dlaw-out=U(H).

For two law tuples define running, unnormalized differences on activity
interval [0,s]: covariance differences use the maximum over both times
up to s; regular responses use the supremum over target times up to s
of the integrated absolute source difference; the atom uses its ordinary
supremum. Denote their sums by e_H(s),e_D(s).

On the coarse domain (11), the complete proof in M_UNIFORM_LAW_ROUTE.md
gives

\[
 e_H(LDlaw,L\widetilde{Dlaw};s)
       \le A_M\int_0^s e_D(u)\,du,
 \qquad
 e_D(UH,U\widetilde H;s)\le A_M e_H(s).
 \tag{13}
\]

The first time integral is essential. On an Euler mesh, each lower
feature history derivative must enter through a read-in update. A
fixed source at cell j therefore retains its factor Delta_j in the
absolute derivative tensor, even when other derivative slots have the
same numerical source index. In Gaussian covariance interpolation,
group the two covariance slots by their latest source cell. Summing
the other slots leaves a deterministic bound A_M Delta_j. This proves
the first integral in (13). For a response output the distinguished
source slot is summed as a response row, so its direct source term
also retains that integral. Perturbing response inputs works by the
same update-factor argument.

The upper map has an instantaneous response atom and consequently need
not gain an integral; it has the second bound in (13). This preserves
the actual forward/transpose feedback and its current atom. No
independence substitution or resetting of past covariance blocks occurs.
The tensor bounds are deterministic entrywise bounds, so they also
justify replacing random cavity inputs by their means without exchanging
an expected supremum with a supremum of expectations. Singular covariance
matrices remain allowed by the existing Gaussian interpolation proof.

The scalar derivative bounds on a domain of size B can be taken as
exp(C(1+M+B)^12), by the finite-order positive tensor recursions and
ordinary Gronwall. Thus B=B_M gives (12). Only a fixed finite derivative
order is used; the power 12 is conservative and has no claimed sharpness.

Let delta_n=A_M/sqrt(n) be the two-sided approximate-fixed-point defect.
Section 5 of M_UNIFORM_LAW_ROUTE.md constructs a population law fixed
point on one common domain for every M>=1: lower gate derivatives have
uniform Gaussian moment envelopes, while the upper ones are uniformly
bounded. Choose the common label threshold also to put S_0 in this
common activity interval. Compare the finite expected tuple to this
fixed point; both belong to the coarse container. Their differences satisfy

\[
 e_H(s)\le\delta_n+A_M\int_0^s e_D(u)\,du,
 \qquad e_D(s)\le\delta_n+A_M e_H(s).
 \tag{14}
\]

Substitution and integral Gronwall give

\[
 e_H(S_0)+e_D(S_0)
 \le C(1+A_M)^2\exp(A_M^2S_0)\,\delta_n.
 \tag{15}
\]

For each fixed M, the qualitative finite-program/common-action passage
identifies the limiting finite observables with the own forced closure
population. The quantitative comparison (15) identifies those same
limits with the law fixed point. Thus the latter has the required own
population prediction and velocity observables; its identification is
not assumed from a finite-width mean. Bounded global gate derivatives
suffice for the qualitative fixed-M passage on this common activity
interval, without any further reduction of the labels with M.

Enlarging C bounds the right side by T_C(M)/sqrt(n). In contrast with
the previous whole-interval contraction argument, (15) never asks
A_M S_0 to be small. This removes the statistical reason for shrinking
the labels as M grows. It does not remove the fitting small-label
assumption in (6).

## 5. Return to the actual autonomous predictor

The same finite-order comparison applies to the passive lower velocity,
its same-mixer Gaussian forward action, and the exact unclipped output
derivative w sech^2(z). This supplies the integrable velocity sources
required by SMOOTH_FEEDBACK_COMPLETION.md, not merely a pointwise state
error. The current-time derivative of the key contraction is included
as in that note; no approximation bound is differentiated.

Restore the autonomous residual, clock, and moments on the common
population action spaces. Section 2 bounds the restoration factor by
polynomial(M) exp(CM), absorbed into T_C(M). The centered finite-width
fluctuation bound has that same smaller factor. Their sum yields (2),
including the deterministic finite-width/population mean bias.

The constants in passive query estimates are uniform over the fixed
bounded query set. Integrating their squared time-sup error therefore
preserves (2). The probability bound follows by conditional Markov plus
the cap-independent initialized exceptional probability. Nothing in this
argument estimates the actual all-time trajectory on the exceptional
initializations; an all-initialization all-time second moment is still
not claimed.

## 6. Check of the explicit schedule

Put u_n=log log log(n+N_*). Then

\[
 \frac{\log T_C(\sqrt{u_n})}{\log(n+N_*)}
 =\exp\!\left(\exp(C(1+\sqrt{u_n}))-\exp(u_n)\right)
 \longrightarrow0,
 \tag{16}
\]

since C(1+sqrt(u))<u eventually and their gap tends to infinity. Hence
T_C(M(n))=n^(o(1)); its fourth power is eventually less than n, proving
both the width condition and (5). The schedule is deliberately very slow.
The tower in (1) is a proof upper bound, not an observed growth law or a
lower bound on the actual error.

## 7. Exact limitations

This proves that the cap need not stay fixed to obtain vanishing full
population error uniformly throughout training. It does not prove a
strict C/sqrt(n) rate with C independent of a diverging cap. It does not
justify M=log(n), a positive power of log(n), or M=sqrt(n). It also does
not prove that any of those stronger conclusions is false.

The comparison target for (4) is f_infinity,M(n). Identifying its limit
with a single unclipped population and controlling cap-removal bias is
a separate unresolved task. The elementary pointwise bound
|s-M tanh(s/M)|<=|s|^3/(3M^2) alone does not settle that task, because
the lower carrier and its feedback sensitivities require uniform moment
control.

All new files are inside this existing study. No numerical experiments,
manuscript changes, Git writes, or promotions were performed. The fresh
combined check M_SCALE_CHECK.md reconstructed the complete assigned
proof chain and passed (2)--(5). It records all frozen input hashes; the
checked pre-status synthesis hash was
4c00f454061f91ead2ac5d301eb2061bf1177723bd489ef6c13a5d680041e0b9.
The report hash is
1abb393e458ee90aa73668840a076c07104327986b447ed3d570f677bae8bf26.
Subsequent edits here change only status and this evidence record.
