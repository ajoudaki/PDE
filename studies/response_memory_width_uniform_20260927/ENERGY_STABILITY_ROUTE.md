# Energy and dense-carrier tails for the autonomous old clock

Scoped analytic route, 28 September 2026. Inputs: `LEARNED_GATE_RESTORATION.md`,
`OLD_CLOCK_ROUTE.md`, `LIMIT_REGULARITY_ROUTE.md`, the setting and old-clock
proof in the current `paper/main.tex`, and `docs/notation.qmd`. The
`solve-math-rigorously` skill was applied. No other study, experiment or
literature search was used. This note changes no maintained theorem.

**Outcome.** Gradient-flow energy gives an unconditional approximate
energy-dissipation identity for the fully autonomous closure, but does not
remove the initialized-carrier obstruction in trajectory stability. A
one-reference truncation argument reduces that obstruction to a *single*
dense-carrier tail profile: its cutoff constant is affine in the cutoff,
not raised to a power by depth. Exponential tail control would imply
width-uniform autonomous convergence, with the precise rates below.
Those trained dense tails are additional assumptions here. Smooth dense
paths, bounded operator norms, and arbitrary finite moments do not prove
them or the requested constant-times-`P^-1` rate.

## 1. Setup and an unconditional energy consequence

Work at a finite width, with tanh and the canonical mobilities. For parameter
increments use the Hilbert norm

\[
 \|v\|_{\rm mob}^2
 =\frac{\|v_1\|_F^2}{n}
  +\sum_{\ell=2}^L\|v_\ell\|_F^2
  +\frac{\|v_w\|_2^2}{n}.
 \tag{1}
\]

Its population counterpart uses row `L2`, hidden Hilbert--Schmidt, and
readout `L2`. The actual dense flow is `F=-grad_mob L`, for
`L=m^-1 sum_a (f_a-y_a)^2`. By the old-clock consistency result the fully
autonomous closure satisfies

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,
 \qquad E_1=E_w=0,
 \qquad \int_0^T\sum_{\ell=2}^L\|E_\ell\|_F\,dt
 \le \varepsilon_P:=\frac{C_{\rm comp}}{\sqrt{P(P+1)}}.
 \tag{2}
\]

All subsequent constants depend on a fixed horizon, data and depth and
the initial RMS/operator bounds. They have no additional width or order
dependence. Write `Q` for the common residual bound and `beta_l` for the
backward RMS bound furnished by that result. Then

\[
 \|F_\ell(\widehat\theta)\|_F\le2Q\beta_\ell,
 \qquad 2\le\ell\le L.
\]

Set `M=2Q max_(2<=l<=L) beta_l`. The exact chain rule gives

\[
 \frac{d}{dt}\mathcal L(\widehat\theta)
 =-\|F(\widehat\theta)\|_{\rm mob}^2
   -\langle F(\widehat\theta),E\rangle_{\rm mob}.
 \tag{3}
\]

Since the error has only hidden blocks,

\[
 \left|\mathcal L(\widehat\theta(t))
       -\mathcal L(\widehat\theta(s))
       +\int_s^t\|F(\widehat\theta(u))\|_{\rm mob}^2\,du\right|
 \le M\varepsilon_P,\qquad 0\le s\le t\le T.
 \tag{4}
\]

In particular the total positive variation of the closure loss is at most
`M epsilon_P`. Integrating (3) from zero also gives

\[
 \int_0^T\|F(\widehat\theta)\|_{\rm mob}^2dt
 \le\mathcal L(\theta_0)+M\varepsilon_P,
\]
\[
 \int_0^T\|\dot{\widehat\theta}\|_{\rm mob}dt
 \le\sqrt{T\,[\mathcal L(\theta_0)+M\varepsilon_P]}
       +\varepsilon_P.
 \tag{5}
\]

The second estimate uses the triangle inequality, (2), and Cauchy--Schwarz
in time. Equations (3)--(5) hold for the actual autonomous closure, for
every order. They do not compare its loss, predictor or parameters with
the dense trajectory: the dissipation integrals on the two paths can
differ. Thus approximate energy dissipation is an additional property of
the closure, not the missing stability theorem.

## 2. What the quadratic error energy actually contains

Let `e=widehat theta-theta_D`. Finite-dimensional differentiation along
the segment joining the two states gives the exact identity

\[
 \frac12\frac d{dt}\|e\|_{\rm mob}^2
 =-\int_0^1 D^2\mathcal L(\theta_D+s e)[e,e]ds
   +\langle e,E\rangle_{\rm mob}.
 \tag{6}
\]

At any fixed state and parameter direction `v`,

\[
 D^2\mathcal L[v,v]
 =\frac2m\sum_a\bigl(Df_a[v]^2+r_aD^2f_a[v,v]\bigr).
 \tag{7}
\]

The first term is nonnegative. The residual-weighted second derivative
has no definite sign. Here is its complete relevant structure. Let
`j_(l,a)=Dz_(l,a)[v]`, `D_(l,a)=diag tanh'(z_(l,a))`, and define full
backward carriers

\[
 c_{L,a}=w,\qquad c_{\ell,a}=(W^{(\ell+1)})^*\delta_{\ell+1,a}
 \quad(\ell<L).
\]

Using normalized finite pairings or population pairings, the second
derivative of the predictor is

\[
\begin{split}
 D^2f_a[v,v]={}&2\langle v_w,D_{L,a}j_{L,a}\rangle
  +2\sum_{\ell=2}^L
      \langle\delta_{\ell,a},v_\ell D_{\ell-1,a}j_{\ell-1,a}\rangle\\
 &+\sum_{\ell=1}^L
      \langle c_{\ell,a},\tanh''(z_{\ell,a})j_{\ell,a}^2\rangle.
\end{split}
 \tag{8}
\]

To verify (8), differentiate
`z_l=W_l h_(l-1)` twice. Its mixed term is
`2v_l D_(l-1)j_(l-1)`; the remaining second derivative of the activation
is `tanh''(z_(l-1))j_(l-1)^2+D_(l-1)D^2z_(l-1)[v,v]`.
Backpropagating the second summand through the finitely many layers gives
the displayed curvature terms. Differentiating the readout adds the first
mixed term.

The tangent recurrence

\[
 j_{1,a}=v_1 x_a/\sqrt d,\qquad
 j_{\ell,a}=v_\ell h_{\ell-1,a}
              +W^{(\ell)}D_{\ell-1,a}j_{\ell-1,a}
\]

bounds all `j_l` in RMS by a constant times `||v||_mob` on the known
operator bounds. Therefore the two mixed parts in (8) are bounded by
`C||v||_mob^2`. At the dense state, the learned part of each carrier is
bounded pointwise by the exact dense-history estimate in
`LEARNED_GATE_RESTORATION.md`. The remaining initialized part is only in
`L2`. Multiplication by it in the last line of (8) need not be bounded as
a quadratic form on `L2`.

This is an actual obstruction to a general semiconvexity argument. The
stationary construction in Section 3 of `LIMIT_REGULARITY_ROUTE.md` has
`||v||_mob=1` but

\[
 D^2\mathcal L[v,v]
 =\frac43\operatorname{sech}^2(c)\tanh''(a)n^\alpha(1+o(1))
 \longrightarrow-\infty,
 \qquad 0<\alpha<\tfrac12.
\]

Its nonnegative term in (7) tends to zero. Thus retaining the full
Gauss--Newton contribution does not cancel the bad curvature in general.
This example is deterministic with nonzero initial readout, and its memory
defect is zero. It is not a counterexample to the canonical Gaussian
closure or its actual structured perturbation. The Gaussian nearby-state
example in `OLD_CLOCK_ROUTE.md` separately rules out a uniform bound on
fixed-radius normalized tubes around canonical initialization. Neither
example resolves stability restricted to the two actual paths.

## 3. A reference-tail inequality without repeated carrier multiplication

For this section use the sum distance `d`, consisting of first-layer row
RMS, hidden Frobenius norms, and readout RMS. This is uniformly equivalent
to (1) at fixed depth. Use population notation for neuron norms and
pairings; at finite width each such `L2` norm means the explicit RMS and
each population pairing means `u^T v/n`.

Write `A_l^D=W_l^D-W_(0,l)` and `v_D=w_D-w_0`. Define *only along the
dense reference*

\[
 k_{L,a}(t)=w_0,\qquad
 k_{\ell,a}(t)=W_{0,\ell+1}^*\delta_{\ell+1,a}^D(t)
 \quad(\ell<L),
\]
\[
 H_T(M)=\sum_{\ell=1}^L\max_a\sup_{t\le T}
 \|k_{\ell,a}(t)\mathbf1_{\{|k_{\ell,a}(t)|>M\}}\|_{L^2},
 \qquad M\ge1.
 \tag{9}
\]

For a family of widths take the supremum over that family in (9), on
events where the common physical bounds hold. The profile is finite by
the response/operator bounds. At zero initial readout its top term is
identically zero.

Let `U_l` be a common width-independent constant such that every sample's
preactivation discrepancy has `L2` norm at most `U_l d`. The elementary
forward recurrence gives these constants from bounded hidden operators.
For any one reference carrier, tanh gates satisfy

\[
 \| (\widehat D-D^D)k\|_{L^2}
 \le2M\|\widehat z-z^D\|_{L^2}
       +\|k\mathbf1_{\{|k|>M\}}\|_{L^2}.
 \tag{10}
\]

Indeed `|tanh'(u)-tanh'(v)|<=min(2|u-v|,1)`. Split the carrier at
`|k|=M` and use the first bound on the bounded part and the second bound
on the tail. No moment of the closure carrier is used.

For lower layers the *fully autonomous* exact subtraction is

\[
\begin{split}
 \widehat\delta_\ell-\delta_\ell^D={}&
  \widehat D_\ell\widehat W_{\ell+1}^*
       (\widehat\delta_{\ell+1}-\delta_{\ell+1}^D)\\
 &+\widehat D_\ell(\widehat A_{\ell+1}-A_{\ell+1}^D)^*
       \delta_{\ell+1}^D\\
 &+(\widehat D_\ell-D_\ell^D)(A_{\ell+1}^D)^*
       \delta_{\ell+1}^D
  +(\widehat D_\ell-D_\ell^D)k_\ell.
\end{split}
 \tag{11}
\]

The top identity is

\[
 \widehat\delta_L-\delta_L^D
 =\widehat D_L(\widehat w-w_D)
  +(\widehat D_L-D_L^D)v_D
  +(\widehat D_L-D_L^D)w_0.
\]

Let `S` bound the integrated dense residual, `K_l` bound hidden operators,
and `beta_l` bound dense backward responses, as in the input results.
The dense-history estimates are

\[
 \|v_D\|_\infty\le2S,\qquad
 \|(A_{\ell+1}^D)^*\delta_{\ell+1,a}^D\|_\infty
 \le2S\beta_{\ell+1}^2.
\]

Consequently a bound
`max_a ||widehat delta_l-delta_l^D||_(L2)<=V_l(M)d+T_l(M)`
is given by the finite descending recursion

\[
 \begin{split}
 V_L(M)&=1+4SU_L+2MU_L,\\
 V_\ell(M)&=K_{\ell+1}V_{\ell+1}(M)+\beta_{\ell+1}
       +4S\beta_{\ell+1}^2U_\ell+2MU_\ell,\\
 T_L(M)&=\max_a\sup_{t\le T}
           \|k_{L,a}\mathbf1_{|k_{L,a}|>M}\|_{L^2},\\
 T_\ell(M)&=K_{\ell+1}T_{\ell+1}(M)
       +\max_a\sup_{t\le T}
           \|k_{\ell,a}\mathbf1_{|k_{\ell,a}|>M}\|_{L^2}.
 \end{split}
 \tag{12}
\]

The initialized carriers occur only as additive reference forcing in
(11). In particular `V_l(M)` is affine in `M` at every fixed depth, and
`T_l(M)<=C H_T(M)`. Replacing this recursion by a factor `M^L` would lose
information.

The canonical velocity formulas and predictor Lipschitz bound on the
physical operator ball now give

\[
 \|F(\widehat\theta(t))-F(\theta_D(t))\|_{\rm sum}
 \le C_T\bigl[(1+M)d(t)+H_T(M)\bigr],\qquad M\ge1.
 \tag{13}
\]

For clarity, the common-residual first-layer contribution is bounded by
`2QX(V_1(M)d+T_1(M))`; hidden block `l` is bounded by
`2Q[(V_l(M)+beta_l U_(l-1))d+T_l(M)]`; the readout contribution is
`2QU_Ld`. Residual differences cost at most a width-independent constant
times `d`, since the predictor is Lipschitz on these operator/readout
bounds. Summing proves (13).

This is a derived stability *modulus* from reference fields, not an
assumed closure-stability estimate. With (2), it implies both

\[
 \sup_{t\le T}d(t)
 \le \exp(C_T(1+M)T)
       [\varepsilon_P+C_TT H_T(M)]
 \quad\hbox{for every }M\ge1,
 \tag{14}
\]

and the sharper nonlinear comparison

\[
 d(t)\le\varepsilon_P+\int_0^t\omega_T(d(s))ds,\qquad
 \omega_T(u)=C_T\left[u+\inf_{M\ge1}(Mu+H_T(M))\right].
 \tag{15}
\]

The infimum of the increasing affine functions in (15) is increasing
and concave. If the reference tails vanish uniformly, it tends to zero
at zero. No width-independent tail decay follows just from the finite
value of `H_T(1)`.

## 4. Exact conditional consequences and their rate limits

Assume, in addition, that the dense reference family satisfies

\[
 H_T(M)\le B_Te^{-c_T M^\alpha}\quad(M\ge1),
 \qquad B_T,c_T,\alpha>0,
 \tag{16}
\]

with constants independent of width. This is a condition only on dense
initialized carriers, not on closure fields. It is **not proved here for
trained Gaussian networks**.

For sufficiently small `u>0`, choosing
`M=[(2/c_T)log(A/u)]^(1/alpha)`, with a fixed sufficiently large `A`,
in (15) gives

\[
 \omega_T(u)\le K_T u\,[\log(A/u)]^{1/\alpha}.
 \tag{17}
\]

To see the comparison directly, define
`v(t)=epsilon_P+integral_0^t omega_T(d(s))ds`.
Then `d<=v` and `v'<=omega_T(v)` by monotonicity. While `v` is small,
write `z=log(A/v)`; (17) implies
`z'>=-K_T z^(1/alpha)`. Integration gives the following bounds. For
orders sufficiently large, each displayed bound stays within the small
region on `[0,T]`, so first exit justifies using (17) throughout.

If `alpha>1`, put `p=1/alpha<1`. Then

\[
 \sup_{t\le T}d(t)
 \le A\exp\!\left(-
   [\log(A/\varepsilon_P)^{1-p}-(1-p)K_TT]^{1/(1-p)}\right)
 \le\varepsilon_P\exp\!\left(C_T[\log(A/\varepsilon_P)]^p\right).
 \tag{18}
\]

The first expression uses a positive bracket, guaranteed at large order.
For the second, apply the mean-value theorem to
`s -> s^(1/(1-p))` between
`log(A/epsilon_P)^(1-p)-(1-p)K_TT` and
`log(A/epsilon_P)^(1-p)`. Thus sub-Gaussian carrier tails (`alpha=2`)
give `P^-1 exp(C_T sqrt(log P))`; for every fixed `gamma<1` this is
`O(P^-gamma)`, but it is not a constant-times-`P^-1` bound.

If `alpha=1`, integration instead gives

\[
 \sup_{t\le T}d(t)
 \le A(\varepsilon_P/A)^{\exp(-K_TT)}.
 \tag{19}
\]

This still proves width-uniform convergence for every fixed horizon,
with a smaller power. If `alpha<1`, the same comparison gives an upper
bound with a strictly positive limit as `epsilon_P` decreases to zero.
Indeed, for `p=1/alpha>1`,

\[
 z(t)\ge
 [\log(A/\varepsilon_P)^{1-p}+(p-1)K_Tt]^{-1/(p-1)}.
\]

The right side stays finite at positive time as `epsilon_P->0`. This
failure is a limitation of the modulus argument, not failure of the
autonomous algorithm. Equivalently, the integral
`integral_(0+) du/[u log(A/u)^p]` diverges exactly when `p<=1`.

Whenever these bounds yield tracking, the forward recurrence transfers
them to predictions uniformly on bounded input sets. Extra approximation
slack could restore the endpoint rate: if an independently proved
consistency estimate had order `P^-q`, `q>1`, then (18) would imply
`O(P^-1)`. The currently unconditional old-clock estimate (2) has
`q=1`; that extra slack cannot be inserted without another proof.

## 5. Why smooth paths and finite moments do not fill (16)

A compact continuous family in `L2` is uniformly square-integrable:
cover it by finitely many small `L2` balls, truncate the finitely many
centers, and use

\[
 \|u\mathbf1_{|u|>M}\|_{L^2}
 \le2\|u-v\|_{L^2}
       +\|v\mathbf1_{|v|>M/2}\|_{L^2}.
\]

Thus `L2`-continuous dense fields on one fixed population provide
vanishing tails. A compact strongly convergent family, on compatible
probability spaces, can provide uniform vanishing tails as well.
Neither statement provides their decay rate or the divergent integral
needed by (15).

There is a simple sharp diagnostic at the multiplication step. On
`(0,1)` with Lebesgue probability measure, let

\[
 k(s)=[\log(1/s)]^p,
 \qquad u_\delta(s)=a\mathbf1_{(0,\delta)}(s),\quad a\ne0.
\]

The field `k` has every finite polynomial moment for every fixed
`p>0`; it may also be a constant, hence infinitely smooth, time path.
Take a fixed reference preactivation `b` for which
`tanh'(b+a)-tanh'(b)` is nonzero. If
`d_delta=||u_delta||_(L2)=|a|sqrt(delta)`, the gate-product norm obeys

\[
 \|[\tanh'(b+u_\delta)-\tanh'(b)]k\|_{L^2}
 \ge c\,d_\delta[\log(1/\delta)]^p.
 \tag{20}
\]

Here one merely restricts the integral to `(0,delta)`, where
`k>=[log(1/delta)]^p`. The corresponding quadratic curvature pairing
also satisfies

\[
 \int_0^1 k\,u_\delta^2ds
 \ge d_\delta^2[\log(1/\delta)]^p.
 \tag{21}
\]

So passing from the vector estimate to its quadratic energy does not
remove the logarithmic factor in unrestricted concentrated directions.
For `p>1` its comparison modulus is non-Osgood despite all finite
moments. These are sharp multiplier diagnostics, not a construction of
the actual memory error.

At Gaussian initialization, a fresh independent Gaussian matrix sends a
fixed independent vector to Gaussian coordinates. The trained dense
operand `delta_(l+1)^D(t)` is a function of the same initialized matrix
and its true adjoint; that independence is unavailable. Bounded readout
coordinates and hidden operator norms alone do not restore it. Therefore
(16), even with `alpha=1`, remains a substantive trained-reference
estimate. Energy dissipation (4) controls the gradient in the normalized
Hilbert norm, not the exponential tails of these individual carriers.

The full autonomous arbitrary-depth Gaussian closure remains open in
this route. The exact conclusions are (4)--(5), the reference-tail
reduction (13)--(15), and the conditional rates (18)--(19). A successful
endpoint proof must add genuinely proved dense-tail information plus
approximation slack, or exploit correlations of the actual memory error
that the unrestricted multiplier and Hessian estimates discard.
