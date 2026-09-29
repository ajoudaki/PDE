# Direct prediction through two-time forward Grams

28 September 2026. Scoped theoretical continuation. Inputs: the complete
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`,
`ACTIVATION_GAUSSIAN_ALLTIME.md`, `QUANTITATIVE_WIDTH_ATTEMPT.md`,
`QUANTITATIVE_WIDTH_CAVITY.md`, and
`QUANTITATIVE_WIDTH_SENSITIVITY.md`. The rigorous-math and
investigate-conjectures skills were applied. No other study, experiment,
additional agent, maintained manuscript, or Git mutation was used.

**Status.** The exact all-time predictor comparison below bypasses the
trained backward-carrier floor and the bias of the trained tangent Gram.
It works for the actual autonomous response-memory closure as well as
dense training, and in the norm with the time supremum inside the test
integral. Its source is a residual-weighted discrepancy of two-time
*forward* feature Grams. A quantitative estimate for that source under
the original Gaussian assumptions has not yet been proved. In particular
this note does not assert the requested width rate or moving-state
exponent. Sections 7--11 add a nonlinear Gaussian-divergence return
identity, an adaptive-boundary version, and an inverse-free representation
of the population return vector, including the exact whole-row finite
mean-response conversion. These remove the need for a quadratic
Taylor expansion of a gate in this particular weak-return step; they do
not yet prove the joint finite-network response comparison.

## 1. Contract and exact output equation

Keep the original fixed depth, data, Gram margin, globally bounded
activation slopes and globally Lipschitz gates, canonical Gaussian
initialization, zero readout, fixed sufficiently small positive labels,
canonical mobilities, and original autonomous closure. No initialization,
regularity, history-covariance, or fitting hypothesis is added.

Write `|v|_m=(m^{-1} sum_a v_a^2)^{1/2}`. Operator norms on training
vectors use this norm. For any of these network trajectories let

\[
 Q_{ab}(t,s)=\frac{\langle h_L(t,x_a),h_L(s,x_b)\rangle}{mn},
 \qquad
 Q^x_b(t,s)=\frac{\langle h_L(t,x),h_L(s,x_b)\rangle}{mn}.
 \tag{1}
\]

For population fields replace `n^{-1}` inner products by expectations
within the last-layer probability space. Thus `Q(t,t)` is precisely the
readout-feature Gram, with the normalization used in the assigned sources.

The readout equation and its exactly zero initialization give

\[
 w(t)=-\frac2m\sum_b\int_0^t r_b(s)h_L(s,x_b)\,ds,
\]
\[
 r(t)=-y-2\int_0^t Q(t,s)r(s)\,ds,
 \qquad f(t,x)=-2\int_0^t Q^x(t,s)r(s)\,ds.
 \tag{2}
\]

These are exact identities, including when hidden matrices are
reconstructed from response moments: the closure's readout uses its own
features and residual, and it obeys the same canonical update. No
derivative of a backward gate occurs in (2).

## 2. An all-time resolvent using only the reference forward history

Use the dense population as reference, denoted by a star. The established
small-label tube and fitting estimates give constants independent of time:

\[
 Q_*(t,t)\succeq\lambda I_m,
 \quad \|Q_*(t,t)\|\le G,
 \quad \rho_*(s)\le Ye^{-\kappa s},
\]
\[
 \sup_{t\ge s}\|\partial_sQ_*(t,s)\|
       \le C Y\rho_*(s),
 \qquad
 B:=\int_0^\infty\sup_{t\ge s}
             \|\partial_sQ_*(t,s)\|\,ds\le CY^2.
 \tag{3}
\]

The derivative estimate deserves its small-label factor. Each hidden or
first-layer parameter velocity is a residual times a backward field;
the latter has RMS at most `CY`. Therefore its canonical block norm is
at most `CY rho_*(s)`. The forward differential has bounded norm on
the physical tube, using only bounded operators and activation slopes.
Consequently `||partial_s h_L(s,x_b)||_2 <= CY rho_*(s)` in population
RMS. Differentiating only the second factor of (1), and using the
bounded RMS of the first factor, proves (3). The readout velocity does
not enter a hidden feature's derivative. Absolute continuity suffices;
the displayed derivatives are required only almost everywhere.

Only finiteness of `B` will be needed. In particular the argument below
does not further reduce the already established small-label threshold.

For any finite dense or closure trajectory satisfying (2), define

\[
 D(t)=-2\int_0^t[Q(t,s)-Q_*(t,s)]r(s)\,ds,
 \qquad
 D_x(t)=-2\int_0^t[Q^x(t,s)-Q_*^x(t,s)]r(s)\,ds.
 \tag{4}
\]

These sources include the actual finite residual, not a frozen or
independent surrogate. Put `e=r-r_*` and `E(t)=integral_0^t e(s)ds`.
Subtracting (2), followed by integration by parts in the second time
argument of the reference kernel, gives exactly

\[
 e(t)=-2\int_0^t Q_*(t,s)e(s)\,ds+D(t),
\]
\[
 E'(t)=-2Q_*(t,t)E(t)
       +2\int_0^t\partial_sQ_*(t,s)E(s)\,ds+D(t),
 \qquad E(0)=0.
 \tag{5}
\]

The lower integration boundary vanishes because `E(0)=0`. No time
derivative of the discrepancy source `D` is taken. This is useful because
the unknown source may have irregular time dependence.

Let `U(t,u)` solve `partial_t U=-2Q_*(t,t)U`, `U(u,u)=I`. Symmetry
and the Gram gap imply

\[
 \|U(t,u)\|\le e^{-2\lambda(t-u)}.
 \tag{6}
\]

Indeed differentiation of `|U(t,u)v|_m^2` bounds its derivative by
`-4lambda` times itself. Set
`b(s)=sup_{t>=s}||partial_s Q_*(t,s)||`. Variation of constants in (5),
followed by exchanging the order of two nonnegative integrals, gives
on any finite interval `[0,T]`

\[
 |E(t)|_m\le \frac{\|D\|_{L^\infty(0,T)}}{2\lambda}
 +\frac1\lambda\int_0^t
  [1-e^{-2\lambda(t-s)}]b(s)|E(s)|_m\,ds
 \le \frac{\|D\|_{L^\infty(0,T)}}{2\lambda}
 +\frac1\lambda\int_0^t b(s)|E(s)|_m\,ds.
\]

The integral integrating factor, and then passage to the whole half-line,
prove

\[
 \sup_{t\ge0}|E(t)|_m
       \le\frac{e^{B/\lambda}}{2\lambda}\|D\|_\infty,
\]
\[
 \sup_{t\ge0}|r(t)-r_*(t)|_m
 \le\left[1+\frac{G+B}{\lambda}e^{B/\lambda}\right]\|D\|_\infty.
 \tag{7}
\]

Here the second inequality follows directly from (5), without asserting
that the absolute residual difference is integrable. The source's
supremum norm is enough; an absolute-time integral of `D` is unnecessary.

## 3. Passive inputs and the full test norm

Let `a(x)=1+||x||/sqrt(d)`. Forward RMS bounds for passive inputs give

\[
 G_x:=\sup_t\|Q_*^x(t,t)\|_{(\mathbb R^m,|\cdot|_m)\to\mathbb R}
       \le C a(x),
\]
\[
 B_x:=\int_0^\infty\sup_{t\ge s}
       \|\partial_sQ_*^x(t,s)\|\,ds\le C a(x)Y^2.
 \tag{8}
\]

Only the training-feature factor is differentiated; the potentially
unbounded passive-input feature appears once, through its linear-growth
RMS bound. Thus no higher test-input moment is used.

Subtracting the test equation in (2) and integrating its reference term
by parts gives

\[
 f(t,x)-f_*(t,x)
 =-2Q_*^x(t,t)E(t)
   +2\int_0^t\partial_sQ_*^x(t,s)E(s)\,ds+D_x(t).
 \tag{9}
\]

Consequently

\[
 \sup_t|f(t,x)-f_*(t,x)|
 \le\frac{G_x+B_x}{\lambda}e^{B/\lambda}\|D\|_\infty
       +\sup_t|D_x(t)|.
 \tag{10}
\]

For every fixed test law with finite second moment, Minkowski in
`L2(mu)` now proves

\[
 \left[\int\sup_t|f(t,x)-f_*(t,x)|^2\,\mu(dx)\right]^{1/2}
 \le C\|a\|_{L^2(\mu)}\|D\|_\infty
       +\left[\int\sup_t|D_x(t)|^2\,\mu(dx)\right]^{1/2}.
 \tag{11}
\]

The identical pointwise bound gives a bounded-domain uniform estimate.
There is no width-dependent input truncation, no inversion of a history
covariance matrix, and no exchange of the time supremum with the input
integral.

## 4. The exact quantitative source target

Let `D_{n,q},D_{n,q,x}` be (4) for the actual closure. To prove the
requested cost it is sufficient, at fixed confidence, to prove

\[
 \|D_{n,q}\|_\infty+
 \left[\int\sup_t|D_{n,q,x}(t)|^2\,\mu(dx)\right]^{1/2}
 \le C_\mu\{q^{-2+o(1)}+n^{-1/2+o(1)}\}.
 \tag{12}
\]

This one source estimate would imply the predictor theorem by (11), and
then the moving-state exponent by `n=epsilon^{-2+o(1)}` and
`q=epsilon^{-1/2+o(1)}`. It would not need any estimate for the dense
carrier floor in the existing strong-parameter theorem. Equation (12)
is a proof obligation, not an extra assumption attributed to the user.

For dense prediction alone the same target omits the `q` term. Its
source can be estimated from scalar empirical forward Grams, without
coupling individual neuron histories. For example, on the common fitting
event, `|r_n(s)|_m<=Ye^{-kappa s}`, so Minkowski gives

\[
 \big\|\sup_t|D_n(t)|_m\big\|_{L^2(\Pr)}
 \le 2Y\int_0^\infty e^{-\kappa s}
   \big\|\sup_{t\ge s}\|Q_n(t,s)-Q_*(t,s)\|\big\|_{L^2(\Pr)}ds.
 \tag{13}
\]

Conditioning, or multiplication by the event indicator, must be used
consistently in (13); off-event behavior is not controlled by the tube.
The passive-input counterpart follows by Minkowski over the product
probability and input spaces. Thus a weighted forward-Gram mean-square
rate would directly settle dense prediction. It is strictly a scalar
observable requirement and does not imply a strong carrier comparison.

## 5. Bias and fluctuation remain separate even in this representation

Fix one good event of probability at least one half, and use its
conditional expectation throughout this paragraph. Put
`bar Q_n=E Q_n`, `bar r_n=E r_n`. The exact mean equation has the
same form as (5), with forcing

\[
 \overline D(t)=-2\int_0^t
   \{[\overline Q_n(t,s)-Q_*(t,s)]\overline r_n(s)
       +\operatorname{Cov}(Q_n(t,s),r_n(s))\}\,ds.
 \tag{14}
\]

For example suppose the forward-Gram bias has weighted bound

\[
 \beta_n=\int_0^\infty e^{-\kappa s}
   \sup_{t\ge s}\|\overline Q_n(t,s)-Q_*(t,s)\|\,ds,
 \tag{15}
\]

and the RMS fluctuations of the Gram and residual are bounded by `l_n`
uniformly in their time arguments. Cauchy--Schwarz and the deterministic
residual envelope give

\[
 \|\operatorname{Cov}(Q_n(t,s),r_n(s))\|
       \le C l_n\min\{l_n,Ye^{-\kappa s}\}.
 \tag{16}
\]

Splitting the integral at
`kappa^{-1} log_+(Y/l_n)` proves, for fixed `Y` and `0<l_n<=1`,

\[
 \|\overline D\|_\infty
       \le C\{Y\beta_n+l_n^2\log(e/l_n)\}.
 \tag{17}
\]

The same argument applies to the passive-input Gram, with its input
factor. Equations (7)--(11) transfer (17) to the mean prediction. This
refines the earlier tangent-Gram reduction: the bias source now concerns
two-time forward features only. It still cannot be inferred from
concentration around the finite-width mean or from the initialization
Gram estimate.

## 6. Audit of the Gaussian step

The initialization covariance-interpolation lemma applies to
`F(z)=phi(z_a)phi(z_b)` because its weak second derivatives contain
only `phi' phi'` and `phi'' phi`. The corresponding trained observable
`Q_n(t,s)` is a function of the entire gradient-flow solution. Applying
the same lemma to it requires a new argument. It does not remain a
composition of just the displayed initial activations.

For a smooth activation the first initialization derivative of the
trajectory solves the tangent equation. Differentiating that equation
again differentiates its Hessian-of-prediction term and can introduce a
third activation derivative. The bounded Lipschitz gate hypothesis does
not control that derivative. Merely replacing the terminal observable
by a forward Gram therefore does not validate Gaussian covariance
interpolation for the trained trajectory. A valid weak argument would
have to exploit cancellation, Gaussian averaging, or a direct weak
comparison before taking this second path derivative.

Freezing population response coefficients also does not produce the
finite trained mean in (14). Finite residuals and the reused matrix remain
correlated in (4). The same initialized matrix is used forwards and
backwards, and its order-one response must be retained. No independence
of trained neurons or frozen-feedback substitution was used above.

The forward-kernel resolvent is now complete. The unresolved theorem-level
step is an estimate of the actual sources in (12), or first the dense
version of (13), with constants controlled as the response program is
refined. The present note establishes propagation of that weaker source,
not its production. The numerical width theorem remains open in this
route.

## 7. Exact nonlinear Gaussian return with only first weak derivatives

Here is a replacement for the strong gate-Taylor step in the previous
cavity route. Condition on a cavity sigma-field, and let
`g~N(0,I_n)` be independent of it. Conditional statements below may be
read as ordinary Gaussian statements with the cavity fixed. Let
`U:R^n -> R^n` belong to Gaussian `W^{1,2}` and write `DU` for its
Jacobian. Assume

\[
 M_0^2=\mathbb E_g\|U(g)\|_2^2<\infty,
 \qquad M_1^2=\mathbb E_g\|DU(g)\|_F^2<\infty.
 \tag{18}
\]

Define its normalized return and full response trace by

\[
 R(g)=\frac{g^TU(g)}{\sqrt n},
 \qquad C(g)=\frac{\operatorname{tr}DU(g)}{\sqrt n}.
 \tag{19}
\]

The difference is interpreted as the Gaussian divergence when necessary.
For bounded smooth approximations it equals the displayed ordinary
formula, and the divergence has an `L2` extension to (18). It satisfies

\[
 \mathbb E_g[R-C]=0,
 \qquad
 \mathbb E_g|R-C|^2
 =\frac1n\mathbb E_g\left[
       \|U\|_2^2+\sum_{i,j}(\partial_jU_i)(\partial_iU_j)\right]
 \le\frac{M_0^2+M_1^2}{n}.
 \tag{20}
\]

For completeness, the Gaussian adjoint of `partial_i` is
`delta_i v=g_i v-partial_i v`. Its commutator is
`partial_j delta_i v=delta_i partial_j v+1_{i=j}v`.
For smooth compactly supported `U`, use adjointness once in
`E(delta U)^2=E sum_j U_j partial_j(delta U)`, insert this commutator,
and use adjointness once more. This gives the equality in (20).
The trace sum is bounded in absolute value by `||DU||_F^2` by
Cauchy--Schwarz after exchanging its two indices. Centering follows from
`E delta_i U_i=0`. Smooth approximation in Gaussian `W^{1,2}` and the
inequality extend the identity and bound. No second derivative of `U`
is estimated or required.

In particular, if an actual nonlinear outside-source perturbation has
`M_0+M_1<=K_n`, then

\[
 R=C+O_{L^2}(K_n n^{-1/2}).
 \tag{21}
\]

The response Jacobian in (19) is allowed to depend on `g`. There is no
independence assumption on the tangent response and no replacement by a
cavity tangent. A sufficient but unnecessarily strong condition is
`||DU||op<=K_n/sqrt(n)`: it implies `M_1<=K_n`. Adaptive neuron
messages can instead create finitely many order-one singular values of
`DU`; their total Frobenius norm is the relevant quantity in (20).

This distinction is material. For
`U(g)=beta(g)A g/sqrt(n)`, with `||A||op<=K`, differentiation includes
`(A g/sqrt(n)) tensor grad beta`, which can have order-one operator norm.
Its rank is one and its Frobenius norm can still be order one. Imposing
the stronger operator bound would incorrectly exclude this natural
adaptive return.

The first weak derivative of an actual smooth-flow source uses the first
tangent equation. Under the activation assumptions, this equation uses
bounded weak `phi''`, but not `phi'''`. Thus (20) is compatible with
exactly the stated activation regularity once its response-norm hypotheses
have been proved. A stopped, smoothly extended source must satisfy (18)
on the full Gaussian space before the identity is applied. Applying (20)
directly to a Gaussian law conditioned on a carrier stop would be invalid.

## 8. Freezing boundary histories without freezing the nonlinear response

The adaptive trace can be separated from the returned outside response
without Taylor-expanding the outside flow. Let `B` be a Hilbert space of
boundary histories, `b(g) in B`, and
`U(g)=V(g,b(g))`. Write

\[
 A(g)=\partial_gV(g,b(g)),\qquad
 B_1(g)=D_bV(g,b(g)):B\longrightarrow\mathbb R^n,
 \qquad B_2(g)=D_gb(g):\mathbb R^n\longrightarrow B.
 \tag{22}
\]

Assume the weak chain rule applies and, in conditional norms,

\[
 \|U\|_{L^2(\ell^2)}\le M_0,\quad
 \|A\|_{L^2({\rm HS})}\le M_A,\quad
 \big\|\|B_1\|_{\rm HS}\|B_2\|_{\rm HS}\big\|_{L^2}\le M_B.
 \tag{23}
\]

The chain rule gives `DU=A+B_1B_2`. Products of Hilbert--Schmidt maps
are trace class and

\[
 \|B_1B_2\|_{\rm HS}\le\|B_1\|_{\rm HS}\|B_2\|_{\rm HS},
 \qquad
 |\operatorname{tr}(B_1B_2)|
       \le\|B_1\|_{\rm HS}\|B_2\|_{\rm HS}.
 \tag{24}
\]

For example, expand the trace in orthonormal bases of the two Hilbert
spaces and apply Cauchy--Schwarz to the paired matrix coefficients;
finite-rank approximation gives the general statement. Equations
(20), (23), and (24) prove the fully nonlinear return estimate

\[
 \left\|\frac{g^TU(g)}{\sqrt n}
       -\frac{\operatorname{tr}\partial_gV(g,b(g))}{\sqrt n}
       \right\|_{L^2}
 \le\frac{M_0+M_A+2M_B}{\sqrt n}.
 \tag{25}
\]

Constants in this convenient upper bound are inessential; its scaling
and derivative order are explicit. The derivative in the trace holds
the boundary history fixed while differentiating the **full nonlinear
outside flow at its current state**. It is neither a cavity derivative
nor a claim that the boundary history is independent of the deleted row.

A weighted `L2` space of boundary histories is a useful candidate for
`B`. An integral response operator
`v -> integral K(t,s)v(s) ds` is Hilbert--Schmidt if its vector kernel
has finite integrated squared norm. This makes (23) a concrete
node-independent target rather than a bound proportional to the number
of discretization nodes. Actual verification must track the physical
residual envelope or an equivalent finite activity weight.

This estimate addresses the exact obstruction identified in the earlier
cavity note: no Euclidean quadratic remainder for a backward gate is
required. What remains is a joint construction of the actual cavity,
its boundary histories, and the finite response trace, together with
(23) and a comparison of that trace to the population response. Those
network statements are not consequences of the abstract identity alone.

## 9. Population return vectors are Gaussian correlations, without an inverse

There is also a useful way to avoid treating unstable individual named
response coefficients as observables. Let `H` be a real separable Hilbert
space of source fields and `G(h)`, `h in H`, an isonormal Gaussian
process: `E G(h)G(k)=<h,k>_H`. For any scalar `F in L2`, Riesz
representation defines a vector `m_F in H` by

\[
 \langle m_F,h\rangle_H=\mathbb E[F G(h)]
       \quad (h\in H),
 \qquad \|m_F\|_H\le\|F\|_{L^2}.
 \tag{26}
\]

Existence and the bound follow directly from Cauchy--Schwarz and
`||G(h)||_2=||h||_H`. If
`F=F_0(xi_1,...,xi_k)` with `xi_j=G(h_j)` and has integrable weak
derivatives, Gaussian integration by parts in independent orthonormal
root coordinates gives

\[
 m_F=\sum_{j=1}^k\mathbb E[\partial_{xi_j}F_0]h_j.
 \tag{27}
\]

The vectors `h_j` may be linearly dependent. Equation (27) follows by
writing them in an orthonormal basis of their finite span and applying
one-dimensional Gaussian integration by parts to each independent root.
There is no inverse of their Gram matrix. Auxiliary independent
randomness in `F` can be conditioned on first. Approximation then
extends the correlation characterization to its `L2` closure.

The right side of (27) is precisely the **contracted return vector**
which accompanies an adjoint use of a matrix whose forward queries were
the source fields `h_j`. Individual named-slot derivatives are not the
intrinsic object. On a common isonormal space,

\[
 \|m_F-m_{\widetilde F}\|_H
       \le\|F-\widetilde F\|_{L^2}.
 \tag{28}
\]

Thus a quantitative comparison of returned vectors need not establish
continuity of `phi''` or continuity of every response coefficient. In
particular it is invalid to infer an instability of the returned vector
merely from ill-conditioning of the named history covariance. The vector
has the stable correlation representation (26).

There is a remaining finite-sample limitation. An isonormal Gaussian
process on infinite-dimensional `H` is not an `H`-valued random vector.
One cannot form an iid empirical average of `F G` and claim a
dimension-free Hilbert-space root-width law. For each fixed direction
`h`, the scalar estimator `F G(h)` does have variance at most
`E[F^2 G(h)^2]`. Uniform control over the required history directions
needs their actual regularity or a trace-class factor. It is not provided
by (28) alone.

Equations (25)--(28), combined with the all-time predictor resolvent,
give a more specific candidate route than a raw trained-Gram bias
assumption: retain full finite nonlinear response traces; center reused
Gaussian returns by divergence; formulate population return comparisons
through their correlated source vectors; and bound only the directional
contractions that enter the forward-Gram source (4). The complete joint
forward/adjoint comparison and its width-uniform norms remain to be
proved. No finite-width Gaussian response, independence, or empirical
Hilbert-space law is asserted without that step.

## 10. Audit of the proposed capped deletion induction

One concrete proposed completion is to cap carriers in a proof-only
finite system, compare it to its one-neuron cavity, apply (25), and
derive an inequality of the form

\[
 e_n(t)\le n^{-1/2}e^{CM}
       +CM\int_0^t\rho(s)e_{n-1}(s)\,ds.
 \tag{29}
\]

Iterated time ordering would then be useful, because the activity integral
is finite and its repeated integrals have a factorial denominator. Such
an inequality has not been derived here. The following two issues must
be resolved before using it.

First, let `U_n` and `U_*` denote outside-source *increments* produced by
inserting one Gaussian row. Their Euclidean sizes can be order one,
although the full source vectors have Euclidean size `sqrt(n)`. The
first-chaos bound estimates the discrepancy of mean normalized traces
by the Euclidean `L2` discrepancy of these increments. An ordinary
coupling of full fields at RMS error `e_{n-1}` only gives, by subtraction,

\[
 \|U_n-U_*\|_{L^2(\ell^2)}\le C\sqrt n\,e_{n-1}.
 \tag{30}
\]

This loses the intended gain. A successful argument needs either a
coupling that preserves the `n^{-1/2}` size of the inserted pulse, or
an exact conversion of the insertion trace to correlations with existing
order-one source Gaussians, with the correct causal contractions. The
inverse-free population identity (27) suggests such a conversion but
does not establish its finite-network counterpart. Simply reusing the
ordinary field error in (29) would be circular.

Second, a carrier cap bounds the first tangent operator. It does not
make that operator Lipschitz as a function of the state: its coefficients
can contain bounded measurable `phi''`. Comparing two tangent flows
by a Lipschitz bound on their generators would therefore reintroduce the
regularity missing in the earlier route.

There is a useful but limited history regularity fact. For a bounded
measurable operator coefficient `A(t)`, its fundamental propagator has

\[
 \partial_t U(t,s)=A(t)U(t,s),\quad
 \partial_s U(t,s)=-U(t,s)A(s),\quad
 \partial_t\partial_sU(t,s)=-A(t)U(t,s)A(s).
 \tag{31}
\]

Thus, on a finite activity interval, the pure propagator has mixed
`H1` regularity without differentiating `A`. This can help control a
centered response process in a negative Sobolev history norm. For an
insertion kernel `U(t,s)B(s)`, however, regularity in `s` additionally
requires control of `B'(s)`; if `B` already contains `phi''`, this
cannot be inferred from the assumptions. Even when the insertion uses
only Lipschitz gates and the regularity holds, it controls response
fluctuation and history approximation. It does not identify the finite
response mean. This distinction leaves (29) as a substantive proof
obligation, not a consequence of the divergence calculation.

A potentially better finite variable than the small boundary increment
is the first-chaos vector of a scalar response with respect to its entire
initialized Gaussian row. Conditional on deleting that row, let
`delta_i=F_i(g_i)` and define
`m_i=E_g[g_i delta_i]=E_g grad_{g_i}delta_i`. Then
`||m_i||_2<=||delta_i||_{L2}`, and differences satisfy the corresponding
contraction under a common row coupling. Identifying the source-population
RMS norm with the row's normalized coordinate realization preserves this
bound; there is no derivative of `phi''` in it. Nevertheless the actual
sum `W^T delta` also contains an order-one centered innovation. A finite
law theorem must identify that innovation jointly with forward calls and
control dependence between different row cavities. The first-chaos
identity identifies its mean-response candidate but is not a conditional
central limit theorem. Enlarging the deletion error variable to include
these weak rowwise projections is a concrete candidate; its recursion
and error source are still unproved.

## 11. Exact whole-row conversion of the finite mean response

The conversion suggested above can be stated without any population
limit or tangent differentiability. Fix one initialized hidden matrix
`W_0=G/sqrt(n)` and write its independent standard Gaussian rows as
`g_1,...,g_n`. Let `delta=(delta_1,...,delta_n)` be the actual scalar
backward field for one fixed sample and time. It may depend on all
initialized arrays and all trained feedback. Assume the displayed
products are integrable, for example `delta_i in L2`. Let `E_i` integrate
over row `g_i`, conditional on every other initialized random variable.
Define cavity-measurable row projections and source vectors by

\[
 m_i=\mathbb E_i[g_i\delta_i]\in\mathbb R^n,
 \qquad T_i=\sqrt n\,m_i,
 \qquad \|v\|_n=\|v\|_2/\sqrt n.
 \tag{32}
\]

The vector `g_i` is not conditioned on its trained neuron state. Its
entire Gaussian law is integrated while the other initialization variables
are fixed. For every vector `v` measurable with respect to that cavity,

\[
 \langle T_i,v\rangle_n
 =\mathbb E_i\left[\delta_i\frac{g_i^Tv}{\sqrt n}\right],
 \qquad
 \|T_i\|_n=\|m_i\|_2
       \le\|\delta_i\|_{L^2(\mathbb E_i)}.
 \tag{33}
\]

Here `inner product_n=n^{-1}` times the Euclidean inner product. The
inequality follows by testing the Euclidean vector `m_i` against all
unit vectors and using `||g_i^Tu||_L2=||u||_2`. If `delta_i` has an
integrable weak Gaussian derivative, integration by parts additionally
gives `m_i=E_i grad_{g_i}delta_i`. This derivative formula is optional;
the correlation definition is sufficient.

There is an exact decomposition of the initialized transpose branch:

\[
 W_0^T\delta=T_n+\Xi_n,
 \qquad T_n=\frac1n\sum_iT_i,
\]
\[
 \Xi_n=\sum_i\zeta_i,
 \qquad
 \zeta_i=\frac{g_i\delta_i-m_i}{\sqrt n},
 \qquad \mathbb E_i\zeta_i=0.
 \tag{34}
\]

In particular `E[W_0^T delta]=E T_n` exactly. The learned part of the
transpose branch is the separate finite-rank time integral from the
canonical updates; it is not included in `W_0` and is not discarded.

Suppose two scalar row responses `delta_i` and `delta_i^*` have been
constructed using the same standard row `g_i`, independent of their
joint cavity sigma-field. They may be different nonlinear functions of
this row. Their projections obey the exact conditional contraction

\[
 \|T_i-T_i^*\|_n
       \le\|\delta_i-\delta_i^*\|_{L^2(\mathbb E_i)}.
 \tag{35}
\]

Thus

\[
 \|T_n-T_n^*\|_{L^2(\|\cdot\|_n)}
 \le\frac1n\sum_i
       \|\delta_i-\delta_i^*\|_{L^2}.
 \tag{36}
\]

Equation (36) follows by conditional contraction, expectation, and
Minkowski. The same proof holds in a weighted `L2` space of sample/time
indices by Fubini. No continuity of a tangent generator or of `phi''`
is required. In particular a field comparison using a **common entire
Gaussian row** can control the finite mean-response vector without the
`sqrt(n)` loss in (30). This is a stronger coupling requirement than
an unspecified coupling of scalar marginal field laws.

As a normalization check, take a deterministic source vector `h` and
`delta_i=g_i^T h/sqrt(n)`. Then `m_i=h/sqrt(n)`, `T_i=h`, and
`T_n=h`; (34) is the exact decomposition
`W_0^T W_0 h=h+(W_0^T W_0-I)h`. The retained response has order-one
RMS. The centered part also generally has order-one RMS and cannot be
classified as an error term of order `n^{-1/2}`.

There are three explicit limits to the conversion.

1. The summands `zeta_i` in (34) are conditionally centered but dependent.
   Each actual `delta_i` can depend on every row. Conditional centering
   does not give a central limit theorem, independence across rows, or
   the correct joint covariance with earlier forward calls.
2. The contraction in (35) requires an entire-row coupling. A successful
   construction must preserve the same-matrix forward/transpose reuse
   and the row's independence from the two coupled cavities. An arbitrary
   coupling of scalar outputs with the same marginal laws does not
   suffice to compare their Gaussian correlations.
3. Formula (33) uses a cavity-measurable test source `v`. An actual
   trained source which depends on `g_i` cannot be moved inside that
   conditional expectation as a fixed vector. Replacing it by its cavity
   counterpart requires a quantitative influence estimate, with the
   residual and the other layers treated consistently.

The whole-row conversion therefore supplies an exact candidate for the
bias part of a coupled deletion theorem. The unproved part is now
sharper: construct the common-row comparison, identify the order-one
centered innovation in (34) jointly with all forward calls, and control
the cavity-source replacement. Neither (20) nor (35) by itself supplies
those statements. If they are proved with node-independent
`n^{-1/2+o(1)}` errors, the return-vector contraction avoids the previous
gate-derivative obstruction, and the predictor resolvent in Sections
1--4 completes the all-time propagation. The complete width rate is
not asserted here.
