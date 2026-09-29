# Small activity globalizes the dense Gaussian response construction

Scoped candidate, 28 September 2026. The `solve-math-rigorously` skill was
applied. Inputs were the assigned activity and Gaussian/reference reports,
the canonical setting and complete old-clock proof in `paper/main.tex`,
`docs/index.qmd`, `docs/notation.qmd`, the complete maintained C.1--C.2
proof units in `docs/03-local-population.qmd`, and A.1--A.2 in
`docs/02-gaussian-reuse.qmd`. No other study, experiments, external search,
or further agents were used. This is an internal derivation, not promotion
or an independent review.

**Result.** For zero population readout and a positive initial readout
Gram, sufficiently small labels give a global strong dense population
flow with a uniform-in-time Gaussian carrier estimate. This supplies the
dense-only premise left conditional in the earlier Gaussian transport
report on every prescribed physical horizon. The proof uses deterministic
population Euler programs, stopped by accumulated activity, before it
constructs the continuous flow. Consequently the use of activity is not
circular, and there is no assumption about trained finite-network tails.

The desired all-time, all-finite-width high-probability `C/P` tracking
theorem is **not proved here**. Finite-program transfer remains qualitative
in width. Also, regularity in the dense flow's own finite activity clock
does not automatically give regularity in the actual closure's clock.
Sections 5--6 record these separate boundaries.

## 1. Statement and norms

Fix finite depth `L`, finite data, tanh, the canonical mobilities, Gaussian
first and hidden initialization, and zero initial readout. At population
level each hidden layer has its own probability space and each initialized
hidden action is paired with its true adjoint, exactly as in C.1. Write

\[
 Y=\|y\|_m>0,\qquad X=\max_a\|x_a\|_2/\sqrt d,
 \qquad \Gamma_w(0)=\frac1m
       (\mathbb E[H_{L,a}(0)H_{L,b}(0)])_{a,b}.
 \tag{1}
\]

Assume `Gamma_w(0) >= lambda_0 I` for some `lambda_0>0`.
The argument also works on a fixed invariant compatible residual subspace
with the gap imposed only there. For clarity the proof uses the full
sample space. The Gaussian initial Gram result in
`LOSS_DECAY_SYNTHESIS.md`, Sections 1--2, verifies this assumption for fixed
nonzero pairwise nonparallel inputs, and for a single nonzero input.

Let `K>=1` bound the initialized hidden operator norms on the canonical
generated spaces. Such a deterministic bound is part of C.1's construction:
the finite Gaussian operator event and fixed-program second-moment
convergence give the same bound on every finite generated span, and then
on its closure. Differences of learned hidden increments below use
Hilbert--Schmidt norm; the initialized actions need not be
Hilbert--Schmidt. Use the sum distance

\[
 d(\theta,\vartheta)=\|W_1-V_1\|_{L^2(\mathbb R^d)}
   +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_{\rm HS}
   +\|w-v\|_{L^2}.
 \tag{2}
\]

At finite width the corresponding blocks are first-row RMS,
ordinary hidden Frobenius norm, and readout RMS, as in the existing study.
The fixed finite number of blocks makes the sum and Hilbert direct-sum
norms equivalent, with constants depending only on depth.

**Theorem.** There is `Y_*>0`, depending only on the fixed data, depth,
`K`, `lambda_0`, and the fixed Gaussian initialization convention, such
that for `0<Y<=Y_*` there is a unique global strong dense population flow
from these initial data. It has

\[
 \rho_D(t)\le Y e^{-\lambda_0t},\qquad
 \int_0^\infty\rho_D(t)\,dt\le Y/\lambda_0,
 \tag{3}
\]

and finite total parameter variation in (2). In particular it converges
to an interpolator. For some `c,C>0`, independent of physical time,

\[
 \sup_{t\ge0}\max_{\ell,a}
 \mathbb E\exp(c|c^D_{\ell,a}(t)|^2)\le C,
 \quad c^D_{L,a}=w_D,\quad
 c^D_{\ell,a}=W_{\ell+1,D}^*\delta^D_{\ell+1,a}.
 \tag{4}
\]

Constants in (3)--(4) can be chosen uniformly over label directions and
over `0<Y<=Y_*`. This statement is about the dense population. It does
not assert an empirical version of (4) for actual finite trained paths.

## 2. Activity bounds before Gaussian regularity

Put `R=K+1`. Consider a population Euler program, and, at a node `k`,
write its physical step as `h_k`, its residual as `r_k`, and

\[
 a_k=h_k\rho_k,\qquad s_j=\sum_{k<j}a_k.
 \tag{5}
\]

Stop at a small deterministic activity cap `S`, truncating a final step
if necessary so that `s_j<=S`. The truncation is determined by population
scalar quantities, so every resulting finite program remains deterministic
at the coefficient level. Zero residual produces zero updates and can
be held stationary thereafter.

Up to a first exit of a hidden operator from the ball of radius `R`,
bounded tanh and the exact Euler updates give

\[
 \|w_k\|_2\le2S,\qquad
 \max_a\|\delta_{\ell,a,k}\|_2\le2S R^{L-\ell},
 \tag{6}
\]

\[
 \|W_{\ell,k}-W_{0,\ell}\|_{\rm HS}
       \le4S^2R^{L-\ell}\quad(\ell\ge2),\qquad
 \|W_{1,k}-W_{0,1}\|_{L^2(\mathbb R^d)}
       \le4XS^2R^{L-1}.
 \tag{7}
\]

For example, a hidden update has norm at most
`2h_k rho_k max_a ||delta_(ell,a,k)||_2`, and its sum is bounded
by (7). The same estimates hold on affine segments, because their
increments are fractions of the endpoint increment. If
`4S^2 max_(ell>=2) R^(L-ell)<1`, (7) excludes the operator exit.

Define deterministic constants

\[
 A_1=4X^2R^{L-1},\qquad
 A_\ell=R A_{\ell-1}+4R^{L-\ell}\quad(2\le\ell\le L).
 \tag{8}
\]

The forward recurrence and the Lipschitz constant one of tanh give

\[
 \max_a\|H_{\ell,a,k}-H_{\ell,a}(0)\|_2\le A_\ell S^2.
 \tag{9}
\]

Both the initial and current features have norm at most one. Expanding
the two factors of the Gram therefore gives

\[
 \|\Gamma_{w,k}-\Gamma_w(0)\|_{\rm op}\le2A_LS^2.
 \tag{10}
\]

Choose a fixed `S_b>0` small enough that these physical estimates hold
and `2A_L S_b^2 <= lambda_0/2`. All programs stopped at an activity cap
`S<=S_b` then satisfy

\[
 \Gamma_k\succeq\Gamma_{w,k}\succeq\lambda_0 I/2,
 \qquad \|\Gamma_k\|_{\rm op}\le G,
 \qquad \|F(\theta_k)\|_{\rm sum}\le V\rho_k.
 \tag{11}
\]

Here `G,V` are fixed constants on the common physical ball. The same
velocity and predictor bounds hold along affine segments. No trained
Gaussian assertion was used to obtain (6)--(11).

## 3. The C.2 response lemma in activity and the noncircular exit argument

For a nonzero residual set `u_(a,k)=r_(a,k)/rho_k`. Since the sample
weights are `1/m`, `|u_(a,k)|<=sqrt(m)`. Every Euler update can be
written exactly as

\[
 \Delta W_1=-\frac{2a_k}{m}\sum_a
     u_{a,k}\delta_{1,a,k}x_a^T/\sqrt d,
 \quad
 \Delta W_\ell=-\frac{2a_k}{m}\sum_a
     u_{a,k}\delta_{\ell,a,k}\otimes H_{\ell-1,a,k},
 \tag{12}
\]

with the analogous readout formula. Thus C.2 applies with step lengths
`a_k` and bounded deterministic coefficients `u_(a,k)`.

This substitution uses two explicit provisions of that proof:

* Its final variable-step paragraph permits arbitrary deterministic
  positive step lengths and uses only their sum. The Jensen weights and
  each one-source pulse retain the corresponding step length.
* Its hypotheses allow arbitrary bounded deterministic residual
  coefficients, frozen together with scalar contractions and covariance
  laws when taking named-source derivatives.

At each fixed population Euler program, both `a_k` and `u_k` are such
deterministic numbers. They need not be specified in advance of the
causal population calculation. Their dependence on earlier deterministic
population expectations does not become a source derivative. This is
exactly the frozen-coefficient convention already used for the population
residual feedback in C.1. It would not be correct to apply this reasoning
directly to the random coefficients of a finite trained network.

The preliminary source RMS bounds required by C.2 are (6) and bounded
tanh. Therefore C.2 supplies an `S_r>0` and `c,C>0` such that every
program stopped at total activity at most `S_r` has

\[
 \mathbb E e^{c|c_{\ell,a,k}|^2}\le C
 \tag{13}
\]

uniformly in the number of nodes and their physical times. Use
`S<=min(S_b,S_r)` from now on. Source lengths that vanish correspond to
zero updates and can be deleted. Hence their failure to be strictly
positive causes no exception.

We next prove that sufficiently fine physical Euler programs never hit
their activity cap. This step cannot be replaced by assuming that the
limiting continuous flow already has finite activity.

Let `J(theta)` denote the prediction differential from the mobility
Hilbert space to sample RMS. A first-layer differential is a backward
field paired with the row perturbation; a hidden differential is paired
with `delta_(ell,a) tensor H_(ell-1,a)`; the readout differential is
paired with `H_(L,a)`. Forward subtraction and descending backward
subtraction, using a cutoff `M` only on the reference carriers, give

\[
 \|J(\vartheta)-J(\theta_k)\|
 \le C\{(1+M)d(\vartheta,\theta_k)+e^{-cM^2}\}.
 \tag{14}
\]

Indeed the only unbounded multiplier in backward subtraction is bounded
by

\[
 \|[\tanh'(z)-\tanh'(z_k)]c_k\|_2
 \le2M\|z-z_k\|_2+
            2\|c_k\mathbf1_{|c_k|>M}\|_2.
\]

The tail term is controlled by (13); downward propagation multiplies
previous differences only by bounded operators. Each Jacobian block
then uses the rank-one norm identity or a fixed input norm. This proves
(14) also with Hilbert--Schmidt hidden differences. An affine segment
has distance at most `V h_k rho_k` from its reference node, so integration
of the prediction differential along that segment gives

\[
 r_{k+1}=r_k-2h_k\Gamma_k r_k+q_k,
 \qquad \|q_k\|_m\le h_k\rho_k\,\omega(h_k),
 \qquad \omega(h)\longrightarrow0.
 \tag{15}
\]

To see uniformity, the physical ball bounds `rho_k` by a fixed `Q`.
One may take
`omega(h)=C inf_(M>=1)[(1+M)hQ+exp(-cM^2)]`.
This modulus is independent of the number of physical steps and their
elapsed time. No tail bound for the nonreference affine state is needed.

For `h_k<=1/(2G)`, the spectral bounds (11) give

\[
 \|(I-2h_k\Gamma_k)r_k\|_m
       \le(1-\lambda_0h_k)\rho_k.
\]

Choose the maximal physical mesh small enough that
`omega(h_k)<=lambda_0/2`. It follows that

\[
 \rho_{k+1}\le(1-\lambda_0h_k/2)\rho_k,
 \qquad
 \sum_{k<j}h_k\rho_k
       \le\frac{2(\rho_0-\rho_j)}{\lambda_0}
       \le\frac{2Y}{\lambda_0}.
 \tag{16}
\]

Set `S=4Y/lambda_0` and choose `Y_*` small enough that this cap is
at most `min(S_b,S_r)`. The strict margin `s_j<=S/2` contradicts
first attainment of `S`, including a truncated final step. Thus the
stopped programs actually extend through every finite physical horizon
and satisfy all the common bounds above. This closes the bootstrap.

## 4. Constructing the global flow and identifying the limit

Include, from the outset, countable sequences of the just constructed
Euler programs for every positive integer physical horizon, and their
finite unions, in one common generated action space of C.1. Fix any
finite `T` within one such integer horizon. Adaptive deterministic
coefficients do not obstruct this:
there are still countably many selected finite programs, and their laws
are consistent under deletion of instructions. A.1--A.2 apply separately
to each fixed program. The same Gaussian operator bound constructs the
common initialized actions and adjoints.

C.1's reference-cutoff comparison now applies on `[0,T]`, because its
two required a priori inputs, a common physical ball and Gaussian
reference tails, have just been proved independently of `T`. For two
Euler meshes of maximum physical step `h,h'`, it gives

\[
 \sup_{t\le T}d(\theta^h(t),\theta^{h'}(t))
 \le C_T e^{C(1+M)T}
       \{(1+M)(h+h')+e^{-cM^2}\}.
 \tag{17}
\]

The same proof works in (2): the difference of rank-one increments
has Hilbert--Schmidt norm bounded by the two products of field norms;
the first row is reconstructed by integrating its fixed input vectors.
At fixed `M`, let `h,h'` tend to zero, then let `M` tend to infinity.
The factor `exp(CMT-cM^2)` tends to zero for each fixed `T`.
The complete state spaces give a limit. The bounded-gate product
continuity argument in C.1 passes its integral equations to this limit.
This constructs a strong dense solution on `[0,T]`.

The argument also gives uniqueness against any other strong solution
while it remains in a slightly larger physical ball: only the constructed
solution supplies the carrier tails. A first-exit argument and uniqueness
on successive compact intervals exclude an earlier departure by a
competing solution. Constructions on two different horizons therefore
agree on their overlap and define one global solution.

The Gram gap survives the limit. The exact dense residual equation
`dot r=-2Gamma r` gives

\[
 \dot\rho_D=-2\langle r_D,\Gamma_Dr_D\rangle_m/\rho_D
               \le-\lambda_0\rho_D.
 \tag{18}
\]

If `Y>0`, the bounded upper Gram norm also gives
`rho_D(t)>=Y exp(-2Gt)>0` on each finite interval, so division in
(18) is legitimate. This proves (3). The velocity estimate gives

\[
 \int_t^\infty\|\dot\theta_D(v)\|_{\rm sum}\,dv
       \le \frac{VY}{\lambda_0}e^{-\lambda_0t}.
 \tag{19}
\]

Completeness gives the limiting parameter; prediction continuity and
(3) show that it interpolates. At each time the Euler carriers converge
in `L2`. Almost-sure subsequences and Fatou pass (13) to the limit, with
the same constants at every time. This proves (4), including the
endpoint by another `L2` limit. Uniformity here means a bound on each
time marginal, not an exponential moment of a path supremum.

At every fixed finite `T`, the finite-array oracle passage in C.1 also
applies with these same references, with the following stopping step.
Stop the actual finite path on exit from a ball strictly larger than the
uniform reference bounds. On the stopped interval the C.1 comparison
constants are finite for this fixed T. First choose the carrier cutoff,
then a sufficiently fine fixed reference program, and then width large
enough that its finite-array errors make the comparison smaller than the
ball's exit margin with the desired probability. First exit is then
impossible on that event. The original short-time physical-ball estimate
is not being applied unchanged to an arbitrary horizon.
Consequently canonical finite dense
GF converges in the maintained observable topologies on that horizon.
This passage first fixes the finite reference program, then takes width
to infinity, and then refines the program. It supplies no quantitative
bound on the width needed for a chosen approximation resolution.

## 5. What terminal regularity follows, and what still needs alignment

There is useful endpoint regularity without assuming an `H1` normalized
residual. By (19), the cutoff estimate, and Gram contraction identities,

\[
 \|\Gamma_D(t)-\Gamma_\infty\|_{\rm op}
       \le C e^{-\lambda_0t}\sqrt{1+t},
 \qquad \Gamma_\infty\succeq\lambda_0 I/2.
 \tag{20}
\]

The elementary spectral argument below implies that the normalized
residual has finite variation and approaches one terminal eigendirection
exponentially. It is included to specify exactly what can be used about
the terminal clock; no uniform spectral gap between distinct eigenvalues
is assumed across different datasets or labels.

For completeness, let `A(t)=A_*+E(t)` be a finite-dimensional matrix
with real symmetric `A_*`, and `||E(t)||<=C exp(-a t)`. Write its
distinct eigenvalues as `mu_j` and its eigenspace projections as `Q_j`.
Choose `eta>0` smaller than `a` and every nonzero spectral gap; if there
is only one eigenvalue, only the condition `eta<a` is needed. For a
vector `v` in eigenspace `j`, seek a solution
`x(t)=exp(-mu_j t)(v+z(t))` on `[T,infinity)`. Put
`B=A_*-mu_j I`. The equation for `z` is `z'=-Bz-E(v+z)`.
For its projections onto negative, zero and positive eigenspaces of `B`,
respectively, impose the integral equations

\[
 z_i(t)=\int_t^\infty e^{-(\mu_i-\mu_j)(t-s)}
                      Q_iE(s)(v+z(s))\,ds \quad (i<j),
\]
\[
 z_j(t)=\int_t^\infty Q_jE(s)(v+z(s))\,ds,
 \qquad
 z_i(t)=-\int_T^t e^{-(\mu_i-\mu_j)(t-s)}
                      Q_iE(s)(v+z(s))\,ds \quad (i>j).
 \tag{21}
\]

Each integral operator is bounded on the norm
`sup_(t>=T) exp(eta(t-T))||z(t)||`; its part multiplying `z`
has norm at most a fixed constant times `exp(-aT)`. Choose `T` so
this is less than one. Successive substitution then gives a unique
`z=O(exp(-eta(t-T)))`; differentiating the integrals gives the same
decay for `z'`. For an orthonormal eigenbasis the resulting `v+z(T)`
are independent when `T` is large. They therefore form a basis of
solutions of the finite-dimensional linear ODE. In any nonzero solution,
select the least eigenvalue with nonzero coefficient. The other modes
decay relative to that one, so, for some `mu>0`, `eta'>0`, and `v!=0`,

\[
 r_D(t)=e^{-\mu t}\{v+O(e^{-\eta't})\},\qquad
 \left\|\frac{d}{dt}\frac{r_D(t)}{\rho_D(t)}\right\|
                       \le C e^{-\eta't}
 \tag{22}
\]

for large `t`. Apply this to `A(t)=2Gamma_D(t)`, using (20) with
any smaller exponential rate. Multiplicities are handled by whole
eigenspaces in (21); exponential resonances cause no difficulty because
`eta` is strictly smaller than both the decay rate and positive gaps.
On finite initial intervals the normalized residual is continuously
differentiable, since its denominator is positive. Its total variation
is therefore finite. This does not assert a constant uniform over
families whose distinct terminal spectral gaps approach zero.

In the dense activity variable `s=int_0^t rho_D`, put `s_*=s(infinity)`.
Equation (22) gives `s_*-s(t)` comparable to `exp(-mu t)`. Consequently
the normalized residual extends to an `alpha`-Hölder function of `s`
for some `0<alpha<1`: its derivative with respect to `s` is bounded
by `C(s_*-s)^(alpha-1)`, and integration gives the Hölder bound.
Meanwhile `d(theta_D(s),theta_D(v))<=V|s-v|`. The uniform Gaussian
cutoff estimate gives, for each backward field,

\[
 \|\delta_D(s)-\delta_D(v)\|_2
       \le C|s-v|\sqrt{\log(e(1+s_*)/|s-v|)}.
 \tag{23}
\]

Reduce `alpha` if necessary. The normalized history
`b_(ell,a)=(r_a/rho_D)delta_(ell,a)` is then `alpha`-Hölder through
`s_*`, while every forward history is Lipschitz in `s`. At `s=0`
the backward history is zero because the readout is zero. Hence the
unit zero backward prefix joins continuously.

These facts do give a uniform-in-time signed dense-history approximation
in the **dense flow's own clock**. The Legendre `H1` inequality and
piecewise-linear interpolation of the Hölder history give

\[
 \|(I-\Pi_P)H_D\|_{L^2}\le C/P,
 \qquad \|(I-\Pi_P)b_D\|_{L^2}\le C/P^\alpha.
 \tag{24}
\]

To verify the second bound, interpolate on `P` equal cells. The error
is `O(P^-alpha)` and the interpolant derivative norm is
`O(P^(1-alpha))`; projection contraction and the `H1` inequality
give (24). All prefix intervals have length between one and `1+s_*`,
so their constants are uniform. Orthogonality in the paired history
reconstruction then bounds its signed hidden-matrix error by
`C P^(-1-alpha)` through the terminal endpoint.

This is reference consistency, not a theorem about the autonomous
closure. In the closure's clock the exact dense reference history is

\[
 B(\xi)=\frac{r_D(t(\xi))\delta_D(t(\xi))}
                     {\widehat\rho(t(\xi))}.
 \tag{25}
\]

Neither (22) nor finite activity bounds the residual ratio in (25).
For example, two positive exponentially decaying scalar functions
`rho_D=e^(-at)` and `rho_hat=e^(-bt)` both have finite activity,
yet the squared quotient history in the second clock has integral
`int exp((b-2a)t)dt`, which diverges if `b>=2a`. This is a diagnostic
of the estimate, not a counterexample involving actual neural flows.
One needs a proved ratio estimate, a comparison in matched activity with
controlled physical-time alignment, or another stability argument.

## 6. Finite-width quantifiers and the remaining target

The global dense construction proves the Gaussian premise (10) of
`GENERAL_GAUSSIAN_TRANSPORT.md` on every prescribed finite `[0,T]`,
with constants in that premise independent of `T`. Thus the already
proved finite-horizon qualitative uniform-width approximation and
width-first rates are no longer conditional on extra dense regularity
in this small-label regime. Their comparison constants can still
depend on `T`; the Gaussian premise alone does not remove that factor.

For actual finite networks, the initialized Gram and operator events
from `LOSS_DECAY_SYNTHESIS.md` tend to probability one. On those events
the small-label activity and all-time `C/P` **velocity-defect** bounds
apply to every order, with deterministic constants independent of width.
The present argument supplies no extra finite-array estimate beyond
fixed-program convergence. In particular it does not control either

\[
 \sup_n\Pr\left\{\sup_{P\ge P_*}P
      \sup_{t\ge0}d_n(\widehat\theta_{n,P}(t),\theta^D_n(t))>C(q)\right\}
 \tag{26}
\]

or a corresponding bound restricted to all sufficiently large widths.
The width threshold needed for a fixed-program tolerance can depend on
that tolerance and hence on `P`. Treating finitely many smaller widths
after a qualitative compactness argument does not bound their scaled
`P`-constants as the cutoff width grows. Also a full positive initial
sample Gram cannot hold at widths `n<m`; a finite-width small-label
theorem invoking that event must specify its width range or compatible
residual subspace.

The new reusable result is therefore (3)--(4), with the noncircular
Euler construction in Sections 2--4. Equations (20)--(24) give additional
dense own-clock endpoint regularity. Uniform finite-width feedback
control and the closure-clock endpoint bridge remain genuine missing
steps toward (26).
