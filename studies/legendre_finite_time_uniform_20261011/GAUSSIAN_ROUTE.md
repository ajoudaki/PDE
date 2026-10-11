# Gaussian reachable-state route

Scoped theoretical route, 11 October 2026. This is a study result, not
established book material or an independent promotion review. No experiment,
Git operation, or change to the paper or book was performed.

The unrestricted nonlinear target remains open in this route. The positive
result below is an author derivation, not independently reviewed: a
deterministic implication from a uniform empirical tail bound
for the **actual finite dense carriers**, together with the physical bounds
of the energy route, gives an all-width, all-large-order tracking envelope
`q^-2 sqrt(log(eq)) exp(C sqrt(log(eq)))`. It has no finite-width error
floor, and implies every exponent strictly below two. The empirical tail
hypothesis is a major missing theorem, not an initialization fact or a
minor regularity qualification. An exact `C/q^2` conclusion is also not
obtained from this implication.

The required rigorous-proof, conjecture-investigation, and canonical-notation
skills, including the neural-network reference, were applied. Scientific
inputs were the compact paper setup and Legendre construction; the authorized
prior study's `GENERAL_GAUSSIAN_TRANSPORT.md`,
`GENERAL_REFERENCE_PROJECTION.md`, `GENERAL_AUTONOMOUS_SYNTHESIS.md`,
`GENERAL_ENDPOINT_CHECK.md`, and `ACTIVATION_UNIT_LABEL_FINITE_TIME.md`;
`docs/notation.qmd`; and the complete C.2 proof unit in
`docs/03-local-population.qmd`. The supervisor additionally supplied the
energy-route proposal recorded in Section 2 below. No other study was read.

## 1. Model, target, and probability quantifiers

Use the compact paper's model, with normalized inputs
`v_a=x_a/sqrt(d)`, `||v_a||_2=1`, hidden width `n`, depth `L`, and
finite labels `y_a`. Thus

\[
 z_a^{(1)}=W^{(1)}v_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_a=w^\top h_a^{(L)}/n,
\]
\[
 r_a=f_a-y_a,\qquad
 \rho=\|r\|_2/\sqrt m,\qquad
 \mathcal L=\rho^2.
\]

Here the paper's `w` is the book's readout `W^{(L+1)}`. Define full
backward carriers and residual-free responses by

\[
 k_a^{(L)}=w,\quad
 k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\quad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]

The dense vector field is

\[
 F_1=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 F_\ell=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 F_w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{1}
\]

The first Gaussian matrix has entry variance one, the hidden Gaussian
matrices have entry variance `1/n`, and all blocks are independent.
The readout is exactly zero initially. Each layer activation is real on
the real axis and holomorphic on a common strip, with bounded first
derivative there. Consequently its values have linear growth on the real
axis, and its first two real derivatives have finite bounds. These latter
bounds suffice for the conditional argument below.

The actual order-`q` closure retains the prescribed moments
`bar h_(a,j)^(ell-1), bar delta_(a,j)^(ell)`, uses its own residual and
clock `tau_hat=1+integral rho_hat`, and reconstructs the hidden matrices
exactly as in `paper/compact_legendre.tex`. No clock, activation, or
training equation is changed here. Hats denote this actual closure;
the superscript `D` denotes the actual same-initialization dense flow.
Use the mobility distance

\[
 d_n(\theta,\vartheta)^2
 =\frac{\|W^{(1)}-V^{(1)}\|_F^2}{n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-V^{(\ell)}\|_F^2
 +\frac{\|w-v\|_2^2}{n}.
\tag{2}
\]

The target asks for constants `C(T,data,L,activations,delta)` and `q_0`
independent of width such that, at each individual width, an event of
probability at least `1-delta` supports the bound `C/q^2` on the whole
input sphere and physical interval `[0,T]`, for all sufficiently large
orders. A common event across independently initialized widths is neither
needed nor asserted. There is no label cap or Gram-gap premise.

## 2. What Gaussian initialization and energy already supply

Uniform initialization bounds require no eventual-width convention. For
every `0<delta<1` there are finite `K,A`, depending only on `L,d,delta`,
such that at every width

\[
 \Pr\left\{\max_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}\le K,
       \ \|W_0^{(1)}\|_F/\sqrt n\le A\right\}\ge1-\delta.
\tag{3}
\]

Here is an elementary verification. A `1/4`-net of the unit sphere in
`R^n` has at most `9^n` points, by placing disjoint balls of radius
`1/8` around a maximal separated set and comparing volumes. For any
matrix, approximation of its two maximizing unit vectors gives its
operator norm at most twice the maximal absolute bilinear form on the
two nets. Each fixed bilinear form of a hidden initialized matrix is
`N(0,1/n)`. The exponential-moment Gaussian tail bound and a union bound
therefore give

\[
 \Pr\{\|W_0^{(\ell)}\|_{\rm op}>K\}
 \le2\exp\{-n(K^2/8-2\log9)\}.
\]

Choose `K^2=8[2 log9+log(4(L-1)/delta)]`. The sum over hidden layers
is at most `delta/2`, uniformly for `n>=1`. Also
`E||W_0^(1)||_F^2/n=d`, so Markov's inequality with `A^2=2d/delta`
costs at most the other `delta/2`.

Let `Y=||y||_2/sqrt(m)`. The exact dense energy identity in (2) is

\[
 \frac d{dt}\mathcal L_D=-\|F(\theta_D)\|_{\rm par}^2,\qquad
 d_n(\theta_D(t),\theta_0)\le Y\sqrt t.
\tag{4}
\]

The second inequality uses Cauchy--Schwarz and the zero initial predictor.
It proves global finite-dimensional dense continuation and gives bounded
operator/readout/forward/backward RMS quantities on every prescribed
finite interval, with constants independent of `n` on (3). Linear
activation growth, not bounded activation values, suffices for the
forward bounds.

The supervisor's energy route supplies the following proposed additional
lemma: on such initialization bounds, the actual closure also remains in
a width-independent mobility ball through `[0,T]` for every
`q>=q_phys`, with `q_phys` independent of width. Its mechanism is the
width-independent accumulated defect `C_R/q` on a stopped ball, followed
by

\[
 \int_0^t\|F(\widehat\theta)\|_{\rm par}^2
 \le Y^2+C_R\int_0^t\|E\|_{\rm par},\qquad
 d_n(\widehat\theta(t),\theta_0)
 \le\sqrt{T(Y^2+C_R^2/q)}+C_R/q.
\]

The present report uses the **conclusion** of that lemma as an explicit
dependency. The supervisor reports that its separate audit has finished
positively, with scope qualifications recorded in the energy route.
The conditional proposition below can instead simply assume that common
physical ball; it does not assert this dependency was independently
reviewed here. No probability or carrier-tail claim follows from the
physical ball by itself.

## 3. Conditional theorem with no width floor

Fix `T<infinity`, positive `Y`, and uniform initialization/physical bounds
as above, for dense flow and all closure orders `q>=q_phys`.
Assume further that the **actual finite dense** full carriers satisfy,
on the same event,

\[
 H_n(R):=\sum_{\ell=1}^L\max_a\sup_{0\le t\le T}
 \frac{\|k_a^{(\ell),D}(t)
          \mathbf1_{\{|k_a^{(\ell),D}(t)|>R\}}\|_2}{\sqrt n}
 \le B e^{-cR^2}\qquad(R\ge1),
\tag{5}
\]

where `B,c>0` are independent of `n` and `q`.
Then there are `C,q_0`, depending only on the fixed problem, physical
bounds, `T,B,c`, and independent of width, such that for all `q>=q_0`

\[
 \sup_{t\le T}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t))
 \le \frac{C\sqrt{\log(e+q)}}{q^2}
                \exp\{C\sqrt{\log(e+q)}\}.
\tag{6}
\]

The same envelope, with a changed constant, bounds
`sup_(t<=T, ||x||=sqrt(d)) |f_hat(t,x)-f_D(t,x)|`.
In particular for each `0<alpha<2`, this discrepancy is at most
`C_alpha/q^alpha`. If events supporting the physical bounds and (5)
have probability at least `1-delta` **at every width** with the same
constants, then (6) has that same probability at every width and
simultaneously for all `q>=q_0`. This is a conditional quantitative
all-width theorem, not a width-first limit.

### 3.1. Clock estimates requiring no trained tails

On a common physical ball the slopes, operator norms, forward/backward
RMS norms, residuals, and clock length are bounded by constants independent
of width and order. Let `Pi_q^A` be the Legendre projection on `[0,A]`.
For the actual forward histories, constant on `[0,1]`, the argument in
Sections 4--5 of `ACTIVATION_UNIT_LABEL_FINITE_TIME.md` proves

\[
 \frac1{mn}\sum_a\int_0^{\widehat\tau(t)}
       \|\partial_\xi\widehat h_a^{(\ell)}\|_2^2d\xi\le C.
\tag{7}
\]

For clarity, this is an energy induction, not a backward derivative
assumption. At the first layer differentiate its clock-time equation.
At each next layer differentiate `h=phi(Wh_previous)`, split into the
canonical weight update, its defect, and the propagated feature derivative.
The endpoint evaluation norm of degree-below-`q` polynomials is
`q/sqrt(A)`. Hence the bounded backward history has endpoint error at
most `C(q+1)`. The growing-interval projection identity and the forward
Legendre tail bound then give

\[
 \int_0^t\widehat\rho
       \|E_\ell/\widehat\rho\|_F^2ds
 \le C\frac1{mn}\sum_a\int_0^{\widehat\tau(t)}
       \|\partial_\xi\widehat h_a^{(\ell-1)}\|_2^2d\xi.
\]

The factors `(q+1)^2/[q(q+1)]` are bounded. The three-term induction
therefore closes (7) for every fixed depth, retaining the finite forward
RMS factors when activations are unbounded.

For an `H^1` history the Legendre endpoint error is at most
`sqrt(A/(3q))||h'||_(L^2)`. For a bounded Hilbert-valued backward
history its projected endpoint is at most `64 sqrt(q)||b||_(L^infinity)`.
These are the compact paper's proved projection identities. Their product
in the exact physical defect gives

\[
 \sum_{\ell=2}^L\|E_\ell(t)\|_F\le C\widehat\rho(t),\qquad
 \|\dot{\widehat\theta}(t)\|_{\rm par}\le C\widehat\rho(t).
\tag{8}
\]

The predictor differential has a width-independent norm on the same
ball, by forward differentiation and the normalized readout pairing.
Consequently `||dot r_hat||_2/sqrt(m)<=C rho_hat`. Since `rho_hat(0)=Y`,

\[
 Ye^{-CT}\le\widehat\rho(t)\le Ye^{CT},\qquad
 \left\|\partial_t(\widehat r/\widehat\rho)\right\|_2/\sqrt m\le C.
\tag{9}
\]

Before any hypothetical first residual zero the logarithmic inequality
proves the first bound; continuity then excludes that zero. The quotient
rule gives the second bound. Thus the inverse actual clock is Lipschitz
with a width- and order-independent constant. Zero labels are treated
separately below.

### 3.2. One-reference feedback and dense time regularity

Forward subtraction on the physical ball gives
`||z(theta)-z(vartheta)||_2/sqrt(n)<=C d_n(theta,vartheta)`.
In backward subtraction, the only new multiplication requiring more
than operator/RMS control is

\[
 [\phi_\ell'(z)-\phi_\ell'(z_D)]\odot k_D.
\]

Bound this term by the bounded second derivative below carrier level `R`,
and by twice the bounded first derivative above it. Then its RMS is at
most `C R d_n+C H_n(R)`. Descending through the layers only propagates
earlier discrepancies through bounded matrices and gates and adds the
new gate term. Therefore

\[
 \max_{\ell,a}\frac{\|\delta_a^{(\ell)}(\theta)
                   -\delta_a^{(\ell),D}\|_2}{\sqrt n}
 +\|F(\theta)-F(\theta_D)\|_{\rm par}
 \le C\{(1+R)d_n(\theta,\theta_D)+B e^{-cR^2}\}.
\tag{10}
\]

In bounding hidden velocity differences use
`||uv^T/n||_F=(||u||_2/sqrt(n))(||v||_2/sqrt(n))`.
Thus there is one power of `R` at fixed depth, not one power per layer.
Using **full** dense carriers is essential for unbounded activations;
their learned contributions need not be bounded coordinatewise.

Dense speed is bounded on the physical ball. Apply the response part
of (10) to the dense states at times `s,t`. With `h=|t-s|`, choose
`R` so that `B exp(-cR^2)<=C h`. Bounded response norms cover larger
separations. For `T_1=max(1,T)`,

\[
 \max_{\ell,a}
 \frac{\|\delta_a^{(\ell),D}(t)-\delta_a^{(\ell),D}(s)\|_2}{\sqrt n}
 \le C\psi(h),\qquad
 \psi(h)=h\sqrt{\log(eT_1/h)},\quad\psi(0)=0.
\tag{11}
\]

No actual dense backward time derivative was assumed here.

### 3.3. The actual absolute defect gains almost two orders

All histories now use the actual closure clock `xi=tau_hat(t)`.
Write its backward history and a proof-only comparison history as

\[
 \widehat b_a^{(\ell)}(\widehat\tau(t))
   =\frac{\widehat r_a(t)}{\widehat\rho(t)}
                     \widehat\delta_a^{(\ell)}(t),\qquad
 \widetilde b_a^{(\ell)}(\widehat\tau(t))
   =\frac{\widehat r_a(t)}{\widehat\rho(t)}
                     \delta_a^{(\ell),D}(t).
\tag{12}
\]

Both have zero prefix. The second joins its prefix continuously because
the actual dense initial readout is exactly zero. Equations (9)--(11)
give it the modulus `C psi` in clock time, after changing fixed constants
for the bounded interval and inverse-clock Lipschitz constant.

For a Hilbert-valued history with this modulus, linear interpolation on
`q` equal cells has `L^2` error at most `C sqrt(log(e+q))/q` and derivative
`L^2` norm at most `C sqrt(log(e+q))`. These estimates follow by bounding
the error and difference quotient on each cell by its endpoint modulus.
The Legendre `H^1` tail inequality applied to that interpolant, followed
by best approximation, yields

\[
 \|(I-\Pi_q)\widetilde b\|_{L^2(\xi;\mathrm{RMS})}
 \le C\frac{\sqrt{\log(e+q)}}q,
 \qquad
 \|(I-\Pi_q)\widehat h\|_{L^2(\xi;\mathrm{RMS})}\le C/q.
\tag{13}
\]

Here the RMS of all samples and neurons includes the explicit factor
`1/sqrt(mn)`; alternatively sum the finitely many separate sample bounds.
Put `D(t)=sup_(s<=t) d_n(theta_hat(s),theta_D(s))`. Projection contraction
and (10), applied in (12), give

\[
 \|(I-\Pi_q)\widehat b\|_{L^2(\xi;\mathrm{RMS})}
 \le C\frac{\sqrt{\log(e+q)}}q
       +C\{(1+R)D(t)+B e^{-cR^2}\}.
\tag{14}
\]

For each history `g`, let `D_g(A)=int_0^A ||g-Pi_q^A g||_2^2`.
The exact growing-interval identity is
`dD_g/dA=||g(A)-(Pi_q^A g)(A)||_2^2`. Its initial value is zero for
the constant forward and zero backward prefixes. Cauchy--Schwarz in
clock time, in the exact defect

\[
 E_\ell=\frac{2\widehat\rho}{mn}\sum_a
        e_{b,a}^{(\ell)}e_{h,a}^{(\ell-1)\top},
\]

therefore bounds its accumulated Frobenius norm by twice the product of
the corresponding aggregate `L^2` projection tails. Combining (13)--(14)
and summing the fixed number of hidden links proves

\[
 \int_0^t\sum_{\ell=2}^L\|E_\ell(s)\|_Fds
 \le C\frac{\sqrt{\log(e+q)}}{q^2}
       +\frac Cq\{(1+R)D(t)+B e^{-cR^2}\}.
\tag{15}
\]

This estimates the actual closure's absolute accumulated defect. It
requires neither an oracle evolution nor a projected backward-history
supremum bound independent of order.

### 3.4. Absorption, whole-sphere predictions, and exact limitations

Subtract the actual physical equations, use their common initialization,
then combine (10) and (15):

\[
 D(t)\le C\frac{\sqrt{\log(e+q)}}{q^2}
       +\frac{C(1+R)}qD(t)+CB e^{-cR^2}
       +C(1+R)\int_0^t D(s)ds.
\tag{16}
\]

Choose `R=max(1,sqrt(3 log(e+q)/c))`. There is a fixed `q_0` such
that the coefficient `C(1+R)/q` is at most `1/2` whenever `q>=q_0`.
After absorption, Gronwall's integrating factor yields (6). All constants
are independent of width because (5) is an actual finite-array bound.

For each `alpha<2`, set `u=log(e+q)`. The logarithm of the ratio of
the envelope to `q^-alpha` is bounded above by
`C sqrt(u)+(1/2)log u-(2-alpha)u+O(1)`, which has finite supremum.
This proves the stated power consequence. The same argument cannot set
`alpha=2`: the two positive logarithmic terms then remain unbounded.

The initial first-matrix Frobenius bound and physical mobility ball
bound first-layer RMS uniformly for every unit query `v`. Forward
subtraction through bounded operators and globally Lipschitz activations,
then Cauchy--Schwarz at the normalized readout, gives

\[
 \sup_{\|x\|_2=\sqrt d}|\widehat f(t,x)-f_D(t,x)|
       \le C d_n(\widehat\theta(t),\theta_D(t)).
\tag{17}
\]

No test-input net, query carrier bound, or input-Gram inverse is needed.
If `Y=0`, both systems are stationary at zero readout and the prediction
error is exactly zero, without any division by a residual.

## 4. Why the missing probability statement is substantial

A sufficient form of (5) would be a high-probability bound, uniform in
width, on

\[
 \max_{\ell,a}\sup_{t\le T}\frac1n\sum_{i=1}^n
       \exp\{c_T|k_{a,i}^{(\ell),D}(t)|^2\}.
\tag{18}
\]

An exponential-square moment bounds the RMS cutoff tail by a Gaussian
exponential with smaller exponent: use
`u^2 1_(|u|>R) <= [2/(ec_T)] exp(-c_T R^2/2) exp(c_T u^2)`.
No independence between coordinates is needed for this implication.
But (18) is about training with reused Gaussian matrices. Conditioning
on a learned backward vector does not leave its reused matrix independent
Gaussian. The hidden learned increments also do not preserve Gaussianity.

The maintained C.2 lemma already covers bounded-slope `C^2` activations
with unbounded values. It proves mesh-uniform **local population marginal**
Gaussian tails and freezes deterministic residuals, contractions, and
covariance laws in its source derivatives. Its finite cap construction
requires, among other inequalities, `f_l T B_(P,l)<=1`, and bounds
responses by exponentials involving the response caps themselves. It
does not supply arbitrary-time continuation of those response bounds,
nor (18) for actual trained finite arrays. Restarting its proof with
independent Gaussian weights would change the model.

The authorized prior Gaussian-program comparison carefully avoids
claiming (18). Its fixed-program error is `o_Pr(1)` only after choosing
the finite program and cutoff. Removing that error requires width to
infinity at fixed approximation order; multiplying it by `q^2` is not
licensed. The earlier qualitative all-width completion over finitely
many exceptional widths gives no tight family of scaled error constants.

Even the conjunction of fixed-width quadratic rates, width-first
quadratic rates, and qualitative uniform convergence cannot supply the
target. The deterministic array

\[
 e_{n,q}=q^{-2}\bigl(1+n\mathbf1_{\{q\ge n\}}\bigr)
\]

has all three properties: for fixed `n` its quadratic constant is
`1+n`; for fixed `q` its large-width value is exactly `q^-2`; and
`sup_n e_(n,q)<=(1+q)/q^2 ->0`. Nevertheless
`sup_(n,q) q^2 e_(n,q)=infinity`. This is a quantifier diagnostic, not
a counterexample generated by the neural network.

## 5. Weighted Gaussian norms and an unfinished own-clock comparison

The Gaussian weighted-error idea attacks the true multiplication
obstruction rather than an arbitrary physical ball. If `G=sigma e·g`
for a standard Gaussian vector and unit direction `e`, integration by
parts gives

\[
 \|Gu\|_{L^2}\le\sigma\|u\|_{L^2}
                         +2\sigma\|D_eu\|_{L^2}.
\tag{19}
\]

Indeed `E[(e·g)^2u^2]=E[u^2]+2E[(e·g)u D_eu]`; solving the resulting
quadratic inequality proves (19), with extension by smooth approximation.
For a Gaussian-plus-bounded carrier this can replace a cutoff when the
**actual error** has a controlled source-direction derivative.

No closed estimate of those error derivatives was obtained here.
Differentiating the actual finite residual-clock error differentiates
empirical contractions, the residuals, `tau_hat`, and the arguments of
the moving Legendre polynomials. Applying (19) to the differentiated
equation introduces second source derivatives, and iteration creates a
hierarchy. A population derivative that freezes scalar coefficients does
not estimate this hierarchy. Similarly, a diagonal tail weight does not
automatically give a width-independent weighted operator norm for a
reused initialized matrix. The direction of the actual projection error
is structured, but that structure has not yet closed either estimate.

A separate potentially useful comparison would parameterize **both**
existing systems by their own residual clocks and compare them at equal
clock value `xi`; augment the comparison by their inverse physical times,
which obey `dt/dxi=1/rho`. This would not change either algorithm. A
uniform positive residual floor would control the additional scalar
time error. Dense histories in their own clock could then retain higher
time regularity, without division by the actual closure residual in the
reference history.

Why this could help: zero readout implies all hidden/first-layer
velocities vanish initially, so dense forward histories have zero
right derivative at the constant-prefix join. If one could prove
width-uniform dense forward `H^2` and backward `H^1` history bounds,
their paired projection error would have order `q^-3`. This spare power
could absorb `exp(C sqrt(log q))` and leave exact `C/q^2` under a
finite-carrier tail event. For `H^2` histories the stronger Legendre
tail follows by applying the Sturm--Liouville operator
`-partial_xi[xi(A-xi)partial_xi]` and its eigenvalues `j(j+1)` twice
in the squared coefficient estimate; the prefix derivative match avoids
a distributional jump in the second derivative.

This own-clock proposal is **unproved** here. In particular, the equal-clock
continuation argument and the required actual finite trained higher
regularity remain to be established. Computing backward derivatives
already introduces `phi''(z) z' k`; forward second derivatives introduce
`phi''(z)(z')^2`. RMS physical bounds control neither product. Tail
control of all relevant forward tangent fields, or another correlated
product estimate, would be required. Temporal analyticity at each fixed
finite width does not make these constants tight over widths.

## 6. Claim status and recommended route status

| Claim | Status and exact scope |
|---|---|
| Uniform Gaussian initialization event | Proved in (3), every individual width |
| Dense finite-time physical ball | Proved by (4), all finite labels and horizons |
| Closure finite-time physical ball at width-independent sufficient order | Supervisor energy-route dependency; separately audited there |
| All-width near-quadratic envelope | Proved conditional on that ball and the actual finite trained-tail event (5) |
| Actual finite trained-tail event for arbitrary finite horizons | Open; not implied by initialized Gaussian tails or local population C.2 |
| Exact width-uniform `C/q^2` for nonlinear activations | Open even after the conditional estimate (6) |
| Gaussian derivative/weighted-norm closure | Open; source derivatives, scalar feedback, and clock terms are not controlled |
| Own-clock extra-regularity comparison | Proposal, not a theorem |

The affine-activation boundary is already covered by
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md`: its gate modulus is zero, so
`s_(n,T)=1`; zero readout removes the prefix jump; the resulting fixed-time
`C/q^2` bound and sufficient order are independent of width. This verifies
that the missing mechanism concerns nonlinear gate-carrier products. It
is not a new resolution for the full activation class.

Recommended registry status: **partial result completed; full route open**.
The most useful reopening input would be a proved probability estimate
for actual finite dense carriers and tangent histories on every prescribed
finite interval, with constants independent of width, or a closed norm for
the actual projection-error response. No unconditional nonlinear positive
tracking rate on arbitrary finite horizons is claimed by this route.
