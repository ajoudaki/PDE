# Arbitrarily slow memory growth: exact all-time transfer consequences

28 September 2026. Scoped mathematical continuation. This report uses only
the complete `SMALL_LABEL_ALLTIME_SYNTHESIS.md`,
`GENERAL_AUTONOMOUS_SYNTHESIS.md`, and `SMALL_LABEL_SPECTRAL_SLACK.md`.
Its conclusions are study-level deductions from their stated theorems,
not independent verification of the constituent proofs or promotion.

## 1. Setup and the unconditional order-growth conclusion

Fix finite depth and finite data, the canonical Gaussian tanh initialization,
exactly zero initial readout, and one fixed label RMS
`0<Y<=Y_*`. Neither the labels nor the algorithm change with width or
memory order. Write `q` for the sources' integer memory order `P`, and set

\[
 E_T(n,q)=\sup_{0\le t\le T}
 d_n(\widehat\theta_{n,q}(t),\theta_n^D(t)),\qquad
 E_\infty(n,q)=\sup_{t\ge0}
 d_n(\widehat\theta_{n,q}(t),\theta_n^D(t)).
 \tag{1}
\]

Here `d_n` is the sum of first-layer row RMS, ordinary hidden-matrix
Frobenius norms, and readout RMS. Dense and closure trajectories use the
same initialized arrays at each width. No coupling across widths is needed.
Let `G_n` be the common initialized operator/Gram event in the sources.
All deterministic constants below are independent of `n,q,t` on that event.
The full-sample Gram assumption is substantive; a compatible-subspace
version requires that version's hypotheses. Arbitrary correlated data do
not by themselves guarantee a positive full-sample feature Gram.

The all-time synthesis proves

\[
 \forall\epsilon>0:\quad
 \lim_{Q\to\infty}\sup_n
 \Pr\{G_n\cap[\sup_{q\ge Q}E_\infty(n,q)>\epsilon]\}=0.
 \tag{2}
\]

Consequently, for **every** deterministic integer sequence `q_n→∞`,

\[
 \Pr\{G_n\cap[E_\infty(n,q_n)>\epsilon]\}\longrightarrow0.
 \tag{3}
\]

Indeed, for any fixed `Q`, eventually `q_n>=Q`, and the event in (3)
is contained in the corresponding event in (2). Take the limsup in `n`
and then let `Q→∞`. There is no lower growth requirement relative to
width: a prescribed iterated logarithm, or any still slower divergent
sequence, is allowed. More generally (3) holds along any widths `n_j`
and orders `q_j→∞`, with the same event restriction. If
`Pr(G_n^c)→0`, then `E_∞(n,q_n)→0` in ordinary probability because its
failure probability is at most the restricted failure probability plus
`Pr(G_n^c)`. We do not drop that latter condition silently.

## 2. An order envelope and one all-order finite-width floor

The two source estimates, with fixed `Y` absorbed into constants, are

\[
 E_\infty(n,q)\le A E_T(n,q)+B e^{-\lambda T}+D/q
                       \quad\text{on }G_n,
 \tag{4}
\]
\[
 E_T(n,q)\le B_T(q)+a_n(T),\qquad a_n(T)\to0
                       \quad\text{in probability},
 \tag{5}
\]
\[
 B_T(q)=\frac{C_T\sqrt{\log(e+q)}}{q^2}
           \exp(C_T\sqrt{\log(e+q)}).
 \tag{6}
\]

Boundedly many small orders may require enlargement of the deterministic
envelope. The finite-head/tail argument in the general synthesis gives
(5) also for (6): at each fixed order its sharp width-first bound controls
the excess, while one large order threshold controls the entire tail.
No rate of decay for `a_n(T)` is supplied.

Use only integer horizons `j>=1`, and replace `B_j` by its decreasing
majorant

\[
 \overline B_j(q)=\sup_{p\ge q}B_j(p).
\]

It is finite and tends to zero, since (6) is `q^{-2+o(1)}` for each
fixed `j`. This replacement removes any issue with small-order
nonmonotonicity. Define the deterministic envelope

\[
 b(q)=\inf_{j\ge1}
 \{A\overline B_j(q)+B e^{-\lambda j}+D/q\}.
 \tag{7}
\]

Then `b` is nonnegative, decreasing and tends to zero. For the last
claim, given `epsilon>0`, choose one finite `j` for which the exponential
term is below `epsilon/2`, and then choose `q` large enough for the other
two terms to be below `epsilon/2`. This proof does not evaluate (5) at
a horizon that varies with width or order.

There is a single nonnegative random variable `a_n^∞→0` in probability
such that, simultaneously for every `q>=1`,

\[
 E_\infty(n,q)\le b(q)+a_n^\infty\quad\text{on }G_n.
 \tag{8}
\]

**Proof.** Put `X_n(q)=E_∞(n,q)` on `G_n`, and zero off `G_n`, and define

\[
 a_n^\infty=\sup_{q\ge1}(X_n(q)-b(q))_+.
 \tag{9}
\]

It remains to prove that this quantity vanishes; the definition alone
does not establish (8) with a useful floor. Fix `epsilon>0`. Choose a
single integer `j_0` and then `J` so that

\[
 A\overline B_{j_0}(J)+B e^{-\lambda j_0}+D/J<\epsilon/2.
\]

For every `1<=q<J`, choose a finite integer `j_q` whose expression in
(7) is below `b(q)+epsilon/2`. Let
`F_epsilon={j_0,j_1,...,j_(J-1)}`. Applying (4)--(5), using the common
horizon `j_0` in the tail and the chosen horizons in the finite head,
gives the explicit pathwise majorant

\[
 a_n^\infty\le\epsilon/2+
                      A\max_{j\in F_\epsilon}a_n(j).
 \tag{10}
\]

Every member of this **finite** maximum tends to zero in probability.
Thus `Pr(a_n^∞>epsilon)→0`. Countability of the integer orders and
horizons ensures measurability; continuity of each trajectory makes
the time suprema measurable via rational times. This proves (8).

In particular every divergent `q_n` satisfies
`E_∞(n,q_n)<=b(q_n)+o_Pr(1)` on `G_n`, with the random remainder
independent of the chosen orders. This is a substantive separation of
order error from finite-width transfer, but it is not a numerical rate
in either variable.

## 3. Spectral slack improves the deterministic transfer

The stronger source `SMALL_LABEL_SPECTRAL_SLACK.md`, equations
(19)--(20), gives an additional deduction. After its smaller fixed label
threshold is imposed, the actual closure obeys, uniformly in `q,n`,

\[
 \widehat\rho(t)\le Y e^{-\kappa t},\qquad
 \|\dot{\widehat\theta}(t)\|_{\rm sum}\le C\widehat\rho(t),
 \qquad\kappa=\lambda_0/2.
\]

The dense residual and velocity satisfy the corresponding bounds, with
at least this decay exponent. Integrating each velocity after `T` and
using the triangle inequality at time `T` proves

\[
 E_\infty(n,q)\le E_T(n,q)+H e^{-\kappa T}
                         \quad\text{on }G_n.
 \tag{11}
\]

For `t<=T`, use `E_T`; for `t>T`, each of the two tail motions is at
most a constant times `Y e^{-κT}/κ`. Thus no order-dependent defect
term is needed in this stronger transfer. Apply the finite-head/tail
proof above with

\[
 b_0(q)=\inf_{j\ge1}
           \{\overline B_j(q)+H e^{-\kappa j}\}.
 \tag{12}
\]

It gives `b_0(q)↓0` and an all-order floor tending to zero in probability.
This improves (7), but does not yield a positive power of `q` without
quantitative control of the compact-horizon constants `C_j`.

## 4. A confidence envelope uniform over widths and all orders

The qualitative theorem gives a different, purely probabilistic bound.
On `G_n`, the common activity and velocity bounds imply a deterministic
`H_0<∞` with `E_∞(n,q)<=H_0` for every order and width: integrate each
path's total motion from their identical initial state.

Fix `0<delta<1`. Set `epsilon_j=H_0 2^{-j}`. By (2), choose strictly
increasing integers `Q_j` so that

\[
 \sup_n\Pr\{G_n\cap[\sup_{q\ge Q_j}E_\infty(n,q)>
                \epsilon_j]\}\le\delta 2^{-j}.
\]

Define `r_delta(q)=H_0` for `q<Q_1` and
`r_delta(q)=epsilon_j` for `Q_j<=q<Q_(j+1)`. Then `r_delta(q)↓0`, and
the union bound gives

\[
 \sup_n\Pr\{G_n\cap[\exists q\ge1:
                  E_\infty(n,q)>r_\delta(q)]\}\le\delta.
 \tag{13}
\]

Thus there is a width-independent, all-time, simultaneous-in-order
confidence bound tending to zero. Its order thresholds are nonconstructive.
Equation (13) takes a supremum of probabilities over widths; it does
not assert a single event simultaneously covering infinitely many widths.
If `Pr(G_n^c)→0`, its unconditional failure probability at width `n`
is at most `delta+o(1)`.

One can also construct one envelope `r(q)↓0` with vanishing, rather
than fixed, failure probability. Choose the thresholds above with
failure bounds `2^{-j}`. For its staircase envelope,

\[
 \sup_n\Pr\{G_n\cap[\exists q\ge Q_k:
                    E_\infty(n,q)>r(q)]\}\le2^{1-k}\to0.
 \tag{14}
\]

This follows by the union bound over `j>=k`. It entails an order-only
high-probability envelope along every divergent order sequence, but no
closed-form order dependence.

## 5. A sufficiently slow diagonal can absorb the width floor

Let `beta(q)=b(q)+1/q`, using either envelope (7) or (12) and its
corresponding floor. Then `beta` is positive, decreasing, and tends to
zero. There exists a deterministic integer cap `K(n)→∞` such that,
for every deterministic sequence `q_n→∞` with `q_n<=K(n)` eventually,

\[
 \Pr\{G_n\cap[E_\infty(n,q_n)>(1+\eta)\beta(q_n)]\}\to0
                         \qquad(\eta>0).
 \tag{15}
\]

To prove this, choose increasing widths `N_k>=k` so large that

\[
 \sup_{n\ge N_k}\Pr\{a_n^\infty>\beta(k)/k\}\le1/k,
\]

which is exactly the definition of convergence in probability at the
fixed tolerance `beta(k)/k`. Set `K(n)=max{k:N_k<=n}` after the first
threshold. Then, for `q_n<=K(n)`, monotonicity gives

\[
 \Pr\{a_n^\infty>\beta(q_n)/K(n)\}\le1/K(n).
\]

Combining this with (8) proves (15). Taking the minimum of `K(n)` and
any prescribed divergent cap gives a still slower admissible cap.
The construction therefore permits arbitrarily slow diagonal schedules
with a rate measured by `beta(q_n)`. The cap is not explicit, and
`beta` is not known to be polynomial. Statement (3) is stronger as a
claim of unscaled convergence: it needs no upper cap on the order.

## 6. Why the listed estimates do not imply a polynomial rate

Even the improved transfer (11) and the fixed-horizon near-quadratic
envelope cannot determine a power of `q` without information on `C_T`.
Here is a logical example, not a network counterexample. Let

\[
 h(q)=1/\log(e+q),\qquad
 X_n(q)=\min\left\{h(q),
       \frac{e^{\sqrt n}\sqrt{1+n+\log(e+q)}}{q^2}\right\},
 \qquad
 X_{n,T}(q)=(X_n(q)-e^{-T})_+.
\]

These quantities have an exact all-time transfer
`X_n(q)<=X_(n,T)(q)+e^{-T}` and the same type of deterministic
fixed-width spectral upper bound as the sources. At each fixed `T`,
`X_(n,T)(q)=0` whenever `q` exceeds a finite threshold depending only
on `T`, since `h(q)→0`. Increasing `C_T` controls the finitely many
remaining orders by (6), uniformly in `n`, with zero width floor.
The qualitative all-width theorem holds because
`sup_n sup_(p>=q)X_n(p)=h(q)→0`. But
`sup_n X_n(q)=h(q)` is larger than every `C q^{-alpha}` eventually,
for every `alpha>0`. If desired, `X_(n,T)` is realized as the running
supremum of the continuous nonnegative scalar path
`t↦(X_n(q)-e^{-t})_+`, which starts at zero.

Thus these estimates alone allow genuinely subpolynomial envelopes.
An explicit all-time power requires an additional quantitative estimate
on horizon growth, finite-array transfer, or the actual correlated
gate/carrier stability. None of the arguments above disproves such a
stronger theorem for the Gaussian network.

The new proved deductions here are (8), (11)--(15), conditional only on
the cited study theorems and their initialization/small-label hypotheses.
They preserve the original autonomous closure, fixed positive labels,
same-width comparison, all-time norm, multiple inputs and fixed depth.
No experiment, external source, maintained manuscript edit, or Git
operation was used.
