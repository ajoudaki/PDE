# Small labels, structured memory error, and an all-time scalar-clock theorem

Scoped analytic continuation, 28 September 2026. The allowed scientific inputs
were the canonical setting and complete old-clock proof in `paper/main.tex`,
`OLD_CLOCK_ROUTE.md`, `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`,
`LOSS_DECAY_SYNTHESIS.md`, `AUTONOMOUS_ONE_SAMPLE.md`,
`GENERAL_GEOMETRIC_STABILITY.md`, and `docs/notation.qmd` in this study and
the established book. The `solve-math-rigorously` skill was applied. No
experiment, external search, other study, additional agent, maintained-file
edit, or Git operation was used. This is an author derivation, not an
independent promotion review.

**Result.** The arbitrary-depth, multiple-input target remains unresolved.
There is a complete restricted theorem: with one normalized input, two tanh
hidden layers, zero initial readout, a positive initial top-feature norm, and
sufficiently small label, the original autonomous old-clock closure tracks
dense gradient flow for **all physical time**, with error at most
`C/[P(P+1)]` in the population-scale parameter norm. The constants are
independent of width and memory order. Gaussian initialization satisfies the
required initial bounds with probability tending to one. This strengthens the
compact-time theorem in `AUTONOMOUS_ONE_SAMPLE.md` without assuming decay of
the closure residual, and without estimating a difference of tangent kernels.

A separate weighted-history calculation below identifies a sufficient
all-time dense-reference `P^-2` estimate at arbitrary depth. The remaining
general-case estimates are stated explicitly; they are not assumptions
silently used to claim the original target.

## 1. Restricted theorem and proof architecture

Use one datum `(x,y)`, with `v=x/sqrt(d)` of norm one, and exactly two hidden
tanh layers. Let `H_1,H_2` be probability-space `L2` spaces, let the initial
first weight row field belong to `L2(Omega_1;R^d)`, and let
`W_0:H_1 -> H_2` be a bounded operator used with its true adjoint. Take
`w_0=0`. Put

\[
 u_0=a_0v,\quad k_0=\tanh(W_0\tanh u_0),\quad
 K_0=\|W_0\|_{\rm op},\quad \|k_0\|_{H_2}^2\ge\lambda_0>0.
 \tag{1}
\]

At finite width every `H_l` norm is explicitly `||z||_2/sqrt(n)`, every
pairing is `u^T v/n`, and every rank-one operator is `uv^T/n`. Hidden
Hilbert--Schmidt norms are ordinary Frobenius norms. Thus the parameter norm
controlled below dominates

\[
 d_n^2=\frac{\|\widehat W^{(1)}-W^{(1)}\|_F^2}{n}
       +\|\widehat W^{(2)}-W^{(2)}\|_F^2
       +\frac{\|\widehat w-w\|_2^2}{n}.
 \tag{2}
\]

There are numbers `Y_*>0` and finite `C`, depending only on `K_0,lambda_0`
and an upper bound for `|y|<=Y_*`, such that the original dense flow and
every original old-clock closure satisfy

\[
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
       \le\frac{C}{P(P+1)}\qquad(P\ge1).
 \tag{3}
\]

The same conclusion holds in the stated population spaces, with no
probabilistic assumption on the bounded operator. Both systems fit the datum
and have finite total residual activity. The case `y=0` is stationary.

For nonzero labels the proof constructs two auxiliary paths in a signed
activity variable, including continuation beyond their fitted points. Their
equations contain no residual factor. They are Lipschitz in the shifted
first-layer coordinate, and the closure's own paired history error gives
`P^-2` tracking on a fixed activity interval. The dense signed residual is
strictly decreasing on that interval. This both locates a fitted point for
every closure and contracts the discrepancy between the two physical clocks.
The auxiliary continuation is a proof device; it does not modify either
training algorithm.

## 2. Construct the paths before choosing physical time

Let `Y=|y|>0`, `sigma=-sign(y)`, and choose

\[
 S=2Y/\lambda_0,\qquad A=1+S,\qquad R=B=2S,
 \qquad K=K_0+2AR.
 \tag{4}
\]

Define

\[
 G(z)=z/2+\sinh(2z)/4,\qquad
 U(\eta)=G^{-1}(G(u_0)+\eta),\qquad h(\eta)=\tanh U(\eta).
 \tag{5}
\]

Both `U(eta)-u_0` and `h(eta)` are globally 1-Lipschitz from `H_1` into
`H_1`, because their scalar derivatives are `tanh'(U)` and
`tanh'(U)^2`, respectively, in `[0,1]`. No integrability of `G(u_0)`
is required: it is only a fixed pointwise origin. For a state
`X=(eta,W,w)` write

\[
 z=Wh,\quad k=\tanh z,\quad \delta=w\tanh'(z),\quad
 q=W^*\delta,\quad f=\langle w,k\rangle.
\]

The extended dense activity path has initial state `(0,W_0,0)` and solves

\[
 \eta'=-2\sigma q,\qquad W'=-2\sigma\delta\otimes h,
 \qquad w'=-2\sigma k,\qquad 0\le s\le S.
 \tag{6}
\]

Primes in Sections 2--5 mean derivatives in `s`. The extended closure has
the same outer equations, `tau=1+s`, and raw moments

\[
 \begin{split}
 H_j'&=h-\tau^{-1}\left(jH_j+\sum_{i<j}(2i+1)H_i\right),\\
 B_j'&=\sigma\delta-\tau^{-1}
                 \left(jB_j+\sum_{i<j}(2i+1)B_i\right),\\
 \widehat W&=W_0-\frac2\tau\sum_{j<P}(2j+1)B_j\otimes H_j.
 \end{split}\tag{7}
\]

Initially `H_0=tanh u_0`, and all other moments vanish. Its backward history
is `b=sigma delta` after the unit prefix and zero on the prefix; its forward
prefix is constant. The label enters only through `sigma` and the interval
length `S`.

Both extended systems exist on `[0,S]`, uniformly in the sense of the
following bounds:

\[
 \|w\|_\infty,\ \|w\|_{H_2}\le2s\le R=B,\quad
 \|\delta\|_{H_2}\le R,\quad \|W\|_{\rm op}\le K,
 \quad \|q\|_{H_1}\le KR.
 \tag{8}
\]

Indeed the readout equation gives the first bound by pointwise integration.
For the closure, projection contraction gives

\[
 \|\widehat W-W_0\|_{HS}
 \le2\|\Pi_P b\|_{L^2(0,\tau;H_2)}
         \|\Pi_P h\|_{L^2(0,\tau;H_1)}
 \le2R\sqrt{SA}\le2AR.
\]

Dense integration gives `||W-W_0||_HS<=2SR<=2AR`. Also
`||eta'||<=2KR`; each raw moment is bounded by its history integral.
For full existence rigor, clip `w` to `[-B-1,B+1]` only inside `delta`.
The resulting fields are locally Lipschitz on the product Hilbert spaces:
clipping and (5) are Lipschitz, the clipped multiplier is bounded, and
`|tanh''|<=2`. Picard iteration gives local solutions. Bounds (8) make the
clipping inactive; all state velocities are bounded for each fixed `P` on
the prescribed interval. A finite endpoint has a norm limit, and local
existence from that limit extends the solution. This is valid in Hilbert
space and does not assume that bounded sets are compact. The same bounds
give uniqueness for the original equations.

To make the population uniqueness assertion explicit, any original
absolutely continuous solution has almost-everywhere scalar representatives
for u, by its integral equation and Fubini. The scalar chain rule then gives
G(u(s))-G(u_0)=integral_0^s(-2 sigma q(v))dv. The right side is an H_1
Bochner integral on every bounded regular interval by (8), even when the
unshifted G(u_0) is not in H_1. Thus the solution lifts to exactly the
locally Lipschitz transformed system above and is unique there. The same
argument in physical time uses -2r q as the integrand.

## 3. Uniform consistency and stability in activity

Define

\[
 \begin{gathered}
 Z=4SK^2R^2,\quad I=2R^2A^2Z,\quad
 V=16R^2S+4I+2K^2Z,\quad J=8S+8B^2V,\\
 D_1=AR\sqrt{SZ},\qquad D_2=\tfrac12A^2\sqrt{ZJ}.
 \end{gathered}\tag{9}
\]

The differentiated reconstruction has the exact form

\[
 \widehat W'=-2\sigma\delta\otimes h+\mathcal E_P,
 \qquad \mathcal E_P=2(b-b^*)\otimes(h-h^*).
 \tag{10}
\]

For either history `g`, its squared projection error obeys
`D_g'=||g-g^*||^2`, with zero initial error. Hence

\[
 \int_0^s\|\mathcal E_P\|_{HS}\,da
 \le2\sqrt{D_b(s)D_h(s)}.
 \tag{11}
\]

The entire forward history is `H1`, and `||h'||<=2KR`, so its derivative
energy is at most `Z`. The Legendre bound and backward mass give

\[
 D_h\le\frac{A^2 Z}{4P(P+1)},\qquad D_b\le SR^2.
 \tag{12}
\]

Endpoint evaluation has norm `P/sqrt(tau)`, so
`||b-b^*||<= (P+1)R`. Equations (10)--(12) imply

\[
 \int_0^S\|\mathcal E_P\|_{HS}^2\,ds
 \le4(P+1)^2R^2D_h(S)\le I.
 \tag{13}
\]

Using `W'=-2b tensor h+E`, `z'=W'h+Wh'`, and the square-of-sum
inequality gives

\[
 \int_0^S\|W'\|_{HS}^2\,ds\le8R^2S+2I,
 \qquad \int_0^S\|z'\|_{H_2}^2\,ds\le V.
\]

The identity `delta'=w' tanh'(z)+w tanh''(z)z'`, the pointwise readout
bound, and `||w'||<=2` consequently give derivative energy at most `J`.
Since `b=sigma delta` and `delta(0)=0`, its history joins the zero prefix
continuously. Thus

\[
 D_b\le\frac{A^2J}{4P(P+1)},\qquad
 \int_0^S\|\mathcal E_P\|_{HS}\,ds
 \le\min\left\{\frac{D_1}{\sqrt{P(P+1)}},
                  \frac{D_2}{P(P+1)}\right\}.
 \tag{14}
\]

These are estimates for the closure's own histories, not a dense replay.
The scalar chain rules used above are justified on almost-everywhere
absolutely continuous representatives, with the displayed integrable bounds
giving the Hilbert-valued derivative statements.

Compare the two extended paths with

\[
 e(s)=\|\widehat\eta-\eta_D\|_{H_1}
       +\|\widehat W-W_D\|_{HS}+\|\widehat w-w_D\|_{H_2}.
\]

Set

\[
 \begin{gathered}
 A_z=K+1,\quad A_f=1+RA_z,\quad A_\delta=1+2BA_z,\\
 A_q=KA_\delta+R,\quad
 \ell=2(A_q+A_\delta+R+A_z),\quad
 M=2(KR+R+1).
 \end{gathered}\tag{15}
\]

The response differences have bounds

\[
 \|\Delta h\|\le e,\quad \|\Delta z\|,\|\Delta k\|\le A_z e,
 \quad |\Delta f|\le A_f e,
 \quad\|\Delta\delta\|\le A_\delta e,
 \quad\|\Delta q\|\le A_q e.
 \tag{16}
\]

The only pointwise multiplier used in the backward estimate is `w`, bounded
by `B`; the first-layer carrier does not multiply a gate difference in the
transformed equation. The sum of differences of the three right sides in
(6) is therefore at most `ell e`. Subtracting the integral equations and
iterating their scalar integral inequality proves

\[
 \sup_{0\le s\le S} e(s)\le\varepsilon_P,
 \qquad
 \varepsilon_P=e^{\ell S}
 \min\left\{\frac{D_1}{\sqrt{P(P+1)}},
                  \frac{D_2}{P(P+1)}\right\}.
 \tag{17}
\]

Also the extended dense speed in this sum norm is at most `M`.

## 4. A coercive dense residual on the entire extended interval

Let

\[
 R_D(s)=\sigma(f_D(s)-y),\qquad
 R_P(s)=\sigma(\widehat f_P(s)-y).
 \tag{18}
\]

These are signed residual functions on the auxiliary interval; past their
first roots they need not be residual norms. Initially both equal `Y`.
The dense path obeys

\[
 R_D'=-2\Gamma_D,\quad
 \Gamma_D=\|k_D\|^2+
       \|\delta_D\|^2\|h_D\|^2+
       \|\tanh'(u_D)q_D\|^2.
 \tag{19}
\]

For example the first-layer contribution follows by differentiating
`f=<w,tanh(Wh)>` along `u'=-2 sigma tanh'(u)q`; the other two terms
follow from (6). Thus every term in (19) is nonnegative.

Along the extended dense path,
`||W'||_HS<=2R`, `||h'||<=2KR`, and consequently
`||k'||<=||z'||<=2R(1+K^2)`. Therefore

\[
 \big|\|k_D(s)\|^2-\|k_0\|^2\big|
 \le2\|k_D(s)-k_0\|\le4SR(1+K^2)
 =8S^2(1+K^2).
 \tag{20}
\]

Choose `Y_*` small enough that, whenever `0<Y<=Y_*` and (4), (9),
(15) are evaluated at `S=2Y/lambda_0`,

\[
 8S^2(1+K^2)\le\lambda_0/2,
 \qquad A_f e^{\ell S}D_1/\sqrt2\le Y/2.
 \tag{21}
\]

Such a positive threshold exists: as `S` decreases, `K` stays bounded,
`ell` stays bounded, and `D_1=8AKS^3`, whereas `Y=lambda_0 S/2`.
The choice can be made using only upper bounds for `K_0` and a fixed
positive lower bound for `lambda_0`.

Equations (19)--(21) yield `R_D'<=-lambda_0` throughout `[0,S]`.
In particular `R_D(S)<=Y-lambda_0 S=-Y`. Equations (16)--(17) and
(21) give `R_P(S)<=-Y/2` for every `P>=1`. Both residual functions
therefore have a first zero in `(0,S)`.

## 5. Recover the original algorithms and compare their physical clocks

For each extended path solve the scalar initial-value problem

\[
 \dot s_D=R_D(s_D),\qquad \dot s_P=R_P(s_P),
 \qquad s_D(0)=s_P(0)=0.
 \tag{22}
\]

Each right side is locally Lipschitz on `[0,S]`, positive before its first
zero, and zero at that first zero. Uniqueness prevents finite-time crossing
or attainment of that equilibrium from below. Thus the solutions exist for
all physical time, remain below their respective first roots, and increase
to them. Indeed any limiting value strictly below the first root has a
strictly positive right side, incompatible with convergence. In particular
`integral_0^infinity rho dt=s(infinity)<S` and both residuals tend to zero.

Along (22) the sign of the physical residual is exactly `sigma` and its
absolute value is `R(s(t))`. Composing (6)--(7) with (22) gives the original
dense gradient equations and the original raw old-clock moment equations:
for example `B_j` has source `R sigma delta=r delta`, and
`dot tau=R=rho`. The reconstructed matrix and initial moments also match
exactly. The first-layer identity in original coordinates follows from (5),
as `G'(u)tanh'(u)=1`. Thus these are the requested physical algorithms,
by uniqueness, rather than an alternative rescaled optimizer.

Put `d=s_P-s_D`. On `[0,S]` the perturbation bound is
`|R_P-R_D|<=A_f epsilon_P` and `R_D'<=-lambda_0`. Subtract (22):

\[
 \dot d=[R_P(s_P)-R_D(s_P)]+[R_D(s_P)-R_D(s_D)].
\]

Multiplying by the sign of nonzero `d`, and using the monotonicity of
`R_D`, bounds the upper right derivative of `|d|` by
`A_f epsilon_P-lambda_0 |d|`. The same inequality holds at zero as an
upper right derivative. Integration with the factor `exp(lambda_0 t)` gives

\[
 |s_P(t)-s_D(t)|\le\frac{A_f\varepsilon_P}{\lambda_0}
                    (1-e^{-\lambda_0t}).
 \tag{23}
\]

No derivative or Lipschitz estimate for the tangent kernel has been used.
Finally compare the states first at the same activity and then along the
dense extended path, whose speed is at most `M`:

\[
 \sup_{t\ge0}
 \left(\|\widehat\eta(s_P(t))-\eta_D(s_D(t))\|
       +\|\widehat W(s_P(t))-W_D(s_D(t))\|_{HS}
       +\|\widehat w(s_P(t))-w_D(s_D(t))\|\right)
 \le\left(1+\frac{MA_f}{\lambda_0}\right)\varepsilon_P.
 \tag{24}
\]

Since `G^{-1}` is 1-Lipschitz and first-layer motion is along the unit
vector `v`, (24) controls (2) and proves (3), with
`C=(1+MA_f/lambda_0) exp(ell S) D_2`. Taking a common majorant for
`S<=2Y_*/lambda_0` makes the same constant valid for all permitted labels.
Each path converges to its fitted endpoint, so the same bound holds for
the two limiting parameter states.

For a test input `x'`, the first-layer preactivation difference is at most
`||x'||/sqrt(d)` times the transformed discrepancy. The forward recurrence
then bounds prediction error by `1+R+RK||x'||/sqrt(d)` times the right
side of (24). Thus the all-time rate also holds on every bounded test-input
set. This is tracking of the dense predictor, not a bound on its test risk.

For Gaussian first weights and hidden entries `N(0,1/n)`, the initialized
top-feature mean square converges in probability to a positive number:
for the unit input, `q_1=E tanh^2(Z)>0` and
`q_2=E tanh^2(sqrt(q_1) Z)>0`. The first layer uses the law of large
numbers; conditional independence of the second-layer Gaussian rows and
boundedness of tanh give the second convergence. Also `||W_0||_op<=10`
with probability tending to one by the two-sphere-net bound in
`OLD_CLOCK_ROUTE.md`. On the common event `||k_0||^2>=q_2/2` and
`||W_0||_op<=10`, take `lambda_0=q_2/2` and use the common constants
above. Hence (3) holds simultaneously for every order on an event whose
probability tends to one. No first-weight coordinate maximum enters.

### Small nonzero readout, including the canonical Gaussian initialization

The same argument covers `Y=|y|>0` and a common initial readout with
`B_0=||w_0||_infinity<=Y`; put `R_0=||w_0||_H2<=Y`. If the initial
residual is zero, both original algorithms are stationary. Otherwise take
`sigma=sign(f_0-y)` and replace (4) by

\[
 S=4Y/\lambda_0,\quad A=1+S,\quad R=R_0+2S,
 \quad B=B_0+2S,\quad K=K_0+2AR.
 \tag{24a}
\]

All constants (9), (15) retain their formulas. Replace the readout part
of (8) explicitly by
`||w(s)||_infinity<=B_0+2s<=B` and `||w(s)||_H2<=R_0+2s<=R`;
the other bounds in (8) follow with these new `R,B`. The extended paths
now start from `(0,W_0,w_0)`. The forward
history and squared-defect estimates are unchanged. The backward history
has the initial jump `sigma delta_0`, where
`delta_0=w_0 tanh'(W_0 tanh u_0)`. Subtract this step before applying the
derivative-energy estimate. Its scalar projection error is at most
`(3/2)sqrt(A/P)`: replace the step by a ramp of length `tau/P`, whose
`L2` difference from the step is at most `sqrt(tau/P)` and whose Legendre
tail is at most half that quantity; if the remaining interval is shorter,
comparison with zero gives the bound directly. Hence (14), (17) become

\[
 \begin{split}
 \varepsilon_P=e^{\ell S}\min\left\{
 \frac{D_1}{\sqrt{P(P+1)}},\quad
 \frac{D_2}{P(P+1)}+
 \frac{D_{3/2}}{P\sqrt{P+1}}\right\},\\
 D_{3/2}=\tfrac32 A^{3/2}\|\delta_0\|_{H_2}\sqrt Z.
 \end{split}\tag{24b}
\]

Choose the small-label threshold to ensure

\[
 4SR(1+K^2)\le\lambda_0/2,
 \qquad A_f e^{\ell S}D_1/\sqrt2\le Y.
 \tag{24c}
\]

The first left side is `O(Y^2)` and the second is `O(Y^3)`, uniformly
over the stated readouts, so such a common threshold exists. Since
`rho_0<=Y+R_0<=2Y`, the extended dense residual at `S` is at most
`2Y-lambda_0 S=-2Y`; the closure residual there is at most `-Y`.
Everything in Sections 4--5, including (23)--(24), consequently holds with
(24a)--(24c). In particular

\[
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le C\left(P^{-2}+R_0P^{-3/2}\right),
 \tag{24d}
\]

with a common width- and order-independent constant for the given initial
bounds and sufficiently small labels. No positive uniform lower bound on
the initial residual is required.

For the canonical stored readout `w_(0,i)~N(0,n^-2)`, the event
`R_0<=2/n` has probability tending to one by concentration of the mean
of the squares of standard Gaussians. For each fixed `Y>0`, a scalar
Gaussian tail and a union bound give
`Pr{B_0>Y}<=2n exp(-n^2 Y^2/2)`. On this event intersected with the
hidden-operator and feature-gap events, (24d) is the all-time bound
`C(P^-2+n^-1 P^-3/2)`, simultaneously for every `P>=1`.

## 6. What dense-reference P^-2 regularity would require in general

There is a useful all-time refinement of the usual unweighted history
argument. It does not complete the multiple-input or deeper-network theorem.
Consider a finite-width dense path, use sample RMS `||.||_m`, and assume

\[
 \dot r=-2\Gamma(t)r,\quad
 \lambda I\preceq\Gamma(t),\quad \|\Gamma(t)\|\le J_0^2,
 \quad \int_0^\infty\|\dot\Gamma(t)\|_{\rm op}dt=V_\Gamma<\infty.
 \tag{25}
\]

These are sufficient hypotheses of this calculation, not proved uniform
facts for general Gaussian deep training. Write `rho=||r||_m`,
`c=r/rho`, `tau=1+integral_0^t rho`, and `a(t)=integral_t^infinity rho`.
The residual gap gives `a(t)<=rho(t)/(2lambda)`. Differentiating the
normalized direction and its Rayleigh quotient gives exactly

\[
 \dot c=-2(\Gamma-\kappa I)c,\quad
 \kappa=\langle c,\Gamma c\rangle_m,\quad
 \dot\kappa=\langle c,\dot\Gamma c\rangle_m-\|\dot c\|_m^2.
 \tag{26}
\]

Integrate on a finite interval, use `kappa>=0`, and then take the supremum
of the nonnegative integrals. This proves

\[
 \int_0^\infty\|\dot c\|_m^2dt\le J_0^2+V_\Gamma.
 \tag{27}
\]

Suppose the layer-`l` backward responses additionally satisfy

\[
 \max_{a,t}\frac{\|\delta_{\ell,a}(t)\|_2}{\sqrt n}
 \le\beta_\ell,\qquad
 T_\ell:=\int_0^\infty\frac1{mn}\sum_a
                      \|\dot\delta_{\ell,a}(t)\|_2^2dt<\infty.
 \tag{28}
\]

For zero initial readout, all backward responses initially vanish. Thus
`b_(l,a)=c_a delta_(l,a)` joins its zero prefix continuously. With
`A=tau(infinity)` and derivatives in the dense clock, changing variables
and using `|c_a|<=sqrt(m)` gives the terminal weighted derivative bound

\[
 \begin{split}
 \mathcal B_\ell
 &:=\frac1{mn}\sum_a\int_0^A
       \xi(A-\xi)\|b_{\ell,a}'(\xi)\|_2^2d\xi\\
 &\le\frac A\lambda
       \left[\beta_\ell^2(J_0^2+V_\Gamma)+mT_\ell\right].
 \end{split}\tag{29}
\]

Indeed the real-history integral equals
`integral tau(t) a(t) ||dot b(t)||^2/rho(t) dt`. Bound `a/rho` by
`1/(2lambda)`, expand `dot b=dot c delta+c dot delta`, and use
`||u+v||^2<=2||u||^2+2||v||^2` together with (27)--(28).

Let `mathcal H_(l-1)` denote the analogous terminal weighted forward
derivative energy. On each finite clock interval `[0,tau]`, the Legendre
tail bound uses the smaller weight `xi(tau-xi)<=xi(A-xi)`. Hence the
dense-driven moment reconstruction in **the dense path's own clock** has

\[
 \int_0^\infty\|E_{\ell,D,P}(t)\|_Fdt
 \le\frac{2\sqrt{\mathcal B_\ell\mathcal H_{\ell-1}}}{P(P+1)}.
 \tag{30}
\]

For every finite physical endpoint, the same-history projection-energy
identity proves this estimate with its finite endpoint tails; (29) bounds
them uniformly. Monotone convergence of the absolute defect integral gives
(30). The estimate therefore controls absolute accumulated reconstruction
velocity error, not just a signed matrix error. The forward energy is
already bounded by the activity estimates, for example
`mathcal H_l<=A^2 Z_l^*/4`.

Unweighted `H1` regularity of the normalized residual direction can fail
at the terminal clock even for a constant positive definite kernel. For
example, for two residual components decaying as `exp(-2lambda_1 t)`
and `exp(-2lambda_2 t)`, with
`lambda_1<lambda_2<=3lambda_1/2`, the second normalized component behaves
as `(A-xi)^(lambda_2/lambda_1-1)` and has a non-square-integrable clock
derivative. Its weighted energy in (29) is nevertheless finite. Thus a
positive residual lower bound on every compact physical interval should
not be extrapolated to all time; the weighted calculation is the appropriate
replacement when its hypotheses are available.

## 7. Exact boundary of the general route

Small labels and zero readout already give width-uniform activity and the
closure's own `O(P^-1)` absolute defect. The learned-adjoint smoothing bound
in `GENERAL_GEOMETRIC_STABILITY.md` controls the learned increment, while
an internal backward derivative still contains

\[
 \tanh''(z_{\ell,a})\odot
       [(W_{0}^{(\ell+1)})^T\delta_{\ell+1,a}]
       \odot\dot z_{\ell,a}.
 \tag{31}
\]

The available activity and operator bounds put each of the last two factors
in normalized `L2`; they do not bound their product in normalized `L2`.
Smallness of their norms does not change that multiplication issue. Hence
(28), and the total kernel variation needed in (25), have not been proved
with width-independent constants. Finite-width smoothness alone gives
finite constants on the bounded dense path, but does not make them uniform
over widths. Gaussian initialization at time zero is not a proof of the
required trained finite-width moment bounds.

Even if (25), (28), and (30) were supplied uniformly, (30) concerns a
dense-driven reconstruction in the dense clock. A noncircular stability
estimate for the actual autonomous moment histories, including their own
clock and backward carriers, would still be needed. Multiple samples have
a residual direction instead of a constant sign, so (6)--(7) no longer
eliminate the residual from the activity dynamics. At larger depth, even
one sample retains internal backward gate-carrier products. The restricted
theorem does not evade these issues by assuming them away.

The coordinator proposed the scalar signed-activity continuation and clock
contraction while this scoped derivation was independently reaching the
same idea. Sections 1--5 provide the completed shared-author argument.
No general-data or general-depth all-time trajectory theorem is claimed.
