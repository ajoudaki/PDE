# A finite-width Gaussian source bound and the moving-field cavity gap

Scoped analytic route, 28 September 2026. Inputs: `SMALL_LABEL_ENERGY.md`,
Sections 1--4 of `SMALL_LABEL_GAUSSIAN.md`, and the complete maintained
C.2 proof in `docs/03-local-population.qmd`. The research and rigorous-math
skills were applied. No other study, experiment, external search, training,
Git operation, or further agent was used.

**Result.** There is a quantitative, finite-width Gaussian source estimate
for two hidden layers, valid for arbitrary correlated inputs and even for
adapted residual coefficients. The actual dense carrier equals this source
plus a remainder of normalized `L2` size `O(Y^3)`. The remainder estimate
does not have the relative factor needed to propagate an `O(P^-1)` closure
defect. The requested arbitrary-depth, fixed-label, width-uniform endpoint
theorem remains open. The source estimate below is not a substitute for it.

## 1. An initialized carrier with its same-row correlation retained

Write `phi=tanh`. Consider two hidden layers and condition on all initial
first-layer feature vectors `h_a in [-1,1]^n`, for `1<=a<=m`. The sole
hidden Gaussian matrix is `W=(sigma/sqrt(n))G`, with independent standard
Gaussian entries. Put

\[
 z_a=Wh_a,\qquad
 K_{ab,j}=\sum_{i=1}^n W_{ij}\phi'(z_{a,i})\phi(z_{b,i}).
 \tag{1}
\]

The two factors in a summand are correlated with `W_ij`; they must not be
treated as independent. Nevertheless, for every `a,b,j`, conditionally on
the first-layer features,

\[
 |\mathbb E K_{ab,j}|\le3\sigma^2,
 \qquad
 \mathbb E\exp\{\lambda(K_{ab,j}-\mathbb E K_{ab,j})\}
       \le \exp(2\sigma^2\lambda^2).
 \tag{2}
\]

Here the expectation in each expression is over `W`. No covariance rank
or separation assumption on the inputs is required.

To prove the mean bound, set
`f_i=phi'(z_(a,i)) phi(z_(b,i))`. Gaussian integration by parts in the
single entry `G_ij` gives

\[
 \mathbb E[W_{ij}f_i]
 =\frac{\sigma^2}{n}\mathbb E\left[
 h_{a,j}\phi''(z_{a,i})\phi(z_{b,i})
 +h_{b,j}\phi'(z_{a,i})\phi'(z_{b,i})\right].
 \tag{3}
\]

The hypotheses for integration by parts hold because `f_i` and its
derivative in that entry are bounded. The bounds `|h|<=1`, `|phi|<=1`,
`|phi'|<=1`, `|phi''|<=2` give `3 sigma^2/n`; summing proves (2)'s
first assertion.

For its second assertion, let `X_i=W_ij f_i` and let `X_i'` be an
independent copy of the entire row construction. Then
`|X_i|<=sigma |G_ij|/sqrt(n)`, and Jensen's inequality gives

\[
 \mathbb E e^{\lambda(X_i-\mathbb E X_i)}
 \le\mathbb E e^{\lambda(X_i-X_i')}
 =\mathbb E\cosh\{\lambda(X_i-X_i')\}
 \le \exp(2\sigma^2\lambda^2/n).
 \tag{4}
\]

For the last inequality, use monotonicity of `cosh` on nonnegative
arguments and

\[
 \cosh\{c(|g|+|g'|)\}
 \le\tfrac12\cosh(2c|g|)+\tfrac12\cosh(2c|g'|),
 \qquad \mathbb E\cosh(2cg)=e^{2c^2}.
\]

The row variables `X_i` are independent under the conditioning, so the
product of (4) proves (2). In particular, constants `c,C>0`, depending
only on `sigma`, obey

\[
 \mathbb E\exp(c|K_{ab,j}|^2)\le C.
 \tag{5}
\]

For example, Chernoff applied to (2) gives
`Pr(|K-EK|>u)<=2 exp(-u^2/(8 sigma^2))`; integration of this tail and
the bounded mean proves (5). This also proves that all constants are
uniform in width and in the conditioned feature vectors.

Let `M_j=max_(a,b)|K_(ab,j)|`. The elementary inequality
`exp(c max |K|^2)<=sum_(a,b) exp(c |K|^2)` yields

\[
 \mathbb E\frac1n\sum_j e^{cM_j^2}\le Cm^2.
 \tag{6}
\]

Consequently, for every `0<eta<1`, with probability at least `1-eta`,

\[
 \frac1n\sum_j e^{cM_j^2}\le Cm^2/\eta.
 \tag{7}
\]

This is an explicit finite-width probability estimate. It does not
assert probability tending to one for a single fixed right-hand side.
The conditional bounds are uniform, so (5)--(7) also hold without
conditioning on the random first-layer initialization.

## 2. Arbitrary adapted residual controls do not spoil this source bound

Let scalar processes `q_b(t)` depend arbitrarily on the full Gaussian
initialization and satisfy `sum_b |q_b(t)|<=2S` for every time. Define

\[
 k^{\rm fr}_{a,j}(t)=\sum_b q_b(t)K_{ab,j}.
\]

Pointwise for every realization,

\[
 \sup_{t,a}|k^{\rm fr}_{a,j}(t)|\le2S M_j.
 \tag{8}
\]

Thus (6)--(7) give exponential-square bounds for the supremum of this
particular source process, scaled by `S`. No independence of `q` and
`W`, no deterministic-residual approximation, and no time net is used.
The reason is that all dependence on the adaptive scalar controls is
confined to a bounded combination of the fixed finite dictionary (1).

For zero initial readout, the dense flow has exactly

\[
 q_b(t)=-\frac2m\int_0^t r_b(s)\,ds,
 \qquad \sum_b|q_b(t)|\le2\int_0^t\rho(s)ds\le2S.
 \tag{9}
\]

Its first nonzero initialized-carrier derivative is also covered:
`dot k_(1,a)(0)=(2/m) sum_b y_b K_ab`. Hence it has subGaussian
scale `O(Y)` uniformly in finite width and without a diagonal input Gram.

## 3. Exact relation to the actual dense carrier

Continue with two hidden layers, zero initial readout, and the small-label
dense path of `SMALL_LABEL_ENERGY.md`. Write
`h_(2,b)(s)=phi(z_(2,b)(s))`,
`D_(2,a)(t)=diag(phi'(z_(2,a)(t)))`, and `W_0=W`. The actual
initialized carrier is

\[
 k_{1,a}(t)=W_0^T D_{2,a}(t)w(t)
 =-\frac2m\sum_b\int_0^t r_b(s)
      W_0^T[D_{2,a}(t)h_{2,b}(s)]\,ds.
 \tag{10}
\]

Using (9) in (8), subtract the initialized dictionary to obtain the exact
decomposition

\[
 k_{1,a}(t)=k^{\rm fr}_a(t)+R_a(t),
\]
\[
 R_a(t)=-\frac2m\sum_b\int_0^t r_b(s)W_0^T
 \left[(D_{2,a}(t)-D_{2,a}(0))h_{2,b}(s)
       +D_{2,a}(0)(h_{2,b}(s)-h_{2,b}(0))\right]ds.
 \tag{11}
\]

On the stated Gaussian operator event, the activity estimates give

\[
 \sup_{t,a}\frac{\|z_{2,a}(t)-z_{2,a}(0)\|_2}{\sqrt n}
       \le CS^2.
 \tag{12}
\]

Indeed zero initial readout gives normalized backward norms `O(S)`;
integrating first-layer and hidden velocities gives parameter increments
`O(S^2)`, and the two-layer forward recurrence gives (12). The normalized
feature differences satisfy the same bound. Apply `||W_0||op<=K`,
`|phi'|<=1`, and `|phi'(u)-phi'(v)|<=2|u-v|` to (11). It follows that

\[
 \sup_{t,a}\frac{\|R_a(t)\|_2}{\sqrt n}
       \le CS^3=O(Y^3).
 \tag{13}
\]

Equations (7)--(13) give an actual finite-width decomposition with
quantitative source tails. They do not give actual trained-carrier tails:
the remainder is controlled in normalized `L2` only.

Specifically, put
`e_a=phi'(z_hat_(1,a))-phi'(z_(1,a,D))`, the actual gate difference.
Its contribution from (13) is bounded only by

\[
 \frac{\|R_a\odot e_a\|_2}{\sqrt n}
 \le C\min\{S^3,\sqrt n\,S^3 x\},
 \tag{14}
\]

where `x` is the hidden/first-layer parameter distance of the energy
report. The second estimate uses `||R||infty<=||R||2` and its forward
difference bound; the first uses the bounded gate. A fixed `O(Y^3)`
additive bound in (14) does not vanish when `P` grows. Its relative
alternative still contains `sqrt(n)`. The frozen-source part by itself
also supplies a cutoff/Osgood modulus, rather than the required relative
`L2` multiplication bound for an arbitrary correlated error.

## 4. Why the immediate leave-one-column continuation does not close

For a fixed column `j`, write it as `sigma g/sqrt(n)`. A cavity dense
path initialized with that column deleted, and otherwise using the same
data and its own residual, is independent of `g`. Denote its layer-two
backward field by `delta_a^(-j)(t)`. The exact splitting is

\[
 k_{1,a,j}(t)
 =\frac\sigma{\sqrt n}g^T\delta_a^{(-j)}(t)
 +\frac\sigma{\sqrt n}g^T
          [\delta_a(t)-\delta_a^{(-j)}(t)].
 \tag{15}
\]

At each fixed time the first term is conditionally Gaussian. Its
variance is `sigma^2 ||delta_a^(-j)||_2^2/n`, so a stopped cavity RMS
bound would control it. The second term requires an estimate of the
*unnormalized* response norm
`||delta_a-delta_a^(-j)||_2`, at scale `O(Y)` with an integrable random
gain. Merely bounding each normalized field by `O(Y)` loses `sqrt(n)`.

Deleting the column changes the hidden matrix by Frobenius norm `O(1)`,
although its initial forward action on any bounded feature vector has
normalized norm `O(n^-1/2)`. Therefore the parameter comparison from the
energy report does not supply the needed localized response estimate.
Subtracting the two backward recursions introduces the same product
`(D-D^(-j)) k^(-j)` that is unresolved in the original comparison.
Freezing the original dense residual in the cavity would instead destroy
the claimed independence of the cavity from `g`.

The complete C.2 proof does not resolve this finite-width step. Its
named-source derivatives freeze deterministic coefficients and Gaussian
covariance laws; (15) concerns random finite-network coefficients and an
actual localized perturbation. A quantitative bound on that response,
together with control of its correlation with the closure error source,
is still required. The present calculation locates that missing bridge
after an explicit, genuinely finite-width Gaussian source estimate; it
does not prove that the bridge is impossible.

## 5. Differentiating the actual finite-width flow

There is a more precise distinction than saying that residuals cannot be
frozen. Let `J` be the prediction derivative from the mobility Hilbert
space to the sample space with weights `1/m`, so dense GF is
`dot theta=-2J(theta)^*r(theta)`. For a derivative `V` of the actual
dense path with respect to one primitive initial Gaussian variable,
ordinary finite-dimensional differentiation gives exactly

\[
 \dot V=-2J^*JV-\frac2m\sum_a r_a\,\operatorname{Hess}f_a[V].
 \tag{16}
\]

The Hessian and adjoint here use the fixed mobility inner product.
Differentiation through the residual gives the first term, and hence

\[
 \tfrac12\frac d{dt}\|V\|^2
 =-2\|JV\|_m^2
   -\frac2m\sum_a r_a
       \langle V,\operatorname{Hess}f_a[V]\rangle.
 \tag{17}
\]

Thus the residual-feedback derivative itself can be discarded favorably
in an upper `L2` energy estimate. It should not be identified as the sole
reason that the population response estimate fails to transfer.

The unbounded term appears explicitly before any estimate. Let
`V_(1,a)=partial z_(1,a)` for the same primitive derivative, let
`G_ab=x_a^T x_b/d`, and write `c_(1,b)=W_2^T delta_(2,b)` for the
full carrier. Thus `c_(1,b)=k_(1,b)+(W_2-W_0)^T delta_(2,b)`; the
second summand has the coordinate bound from the energy report.
Differentiating the exact first-layer preactivation equation yields

\[
 \dot V_{1,a}=-\frac2m\sum_bG_{ab}\left[
    (\partial r_b)\delta_{1,b}
   +r_b D_{1,b}\,\partial c_{1,b}
   +r_b\operatorname{diag}
        (\phi''(z_{1,b})c_{1,b})V_{1,b}\right].
 \tag{18}
\]

The last term is the actual finite-width counterpart of the random
carrier multiplying a named-source response in C.2. At finite width,
the vectors `k` and `V` depend on the same initialization. To estimate
it in a neuronwise `Lp` norm requires a joint product estimate. A bound
for `k` in `L^(2p)` and one for `V` in `Lp` do not suffice: Holder
instead demands the stronger `L^(2p)` response norm. Even an already
proved subGaussian carrier marginal would leave a response-moment
hierarchy, rather than a closed estimate at a fixed exponent.

C.2 avoids this hierarchy by an exact local response representation
with deterministic scalar coefficients, followed by its pointwise
exponential bound for derivative rows. A finite-width replacement would
need a corresponding representation or a proved estimate for the
correlated propagator in (18). The exact finite-width primitive
derivatives of initialized actions are instead

\[
 \partial(W_0h)=\frac\sigma{\sqrt n}e_i h_j+W_0\partial h,
 \qquad
 \partial(W_0^T\delta)
   =\frac\sigma{\sqrt n}e_j\delta_i+W_0^T\partial\delta
 \tag{19}
\]

for differentiation in `G_ij`. Both orientations recur at later times;
their continued responses are not independent named Gaussian slots.
Equation (19) is exact but supplies no replacement for C.2's deterministic
response coefficients.

Small total activity alone cannot absorb the unresolved term from the
currently established bounds. To see the exact norm issue, write
`||v||_(2,n)=||v||_2/sqrt(n)` and consider the admissible norm data

\[
 R=S^3\sqrt n\,e_1,\qquad V=\sqrt n\,e_1.
\]

They have `||R||_(2,n)=S^3`, `||V||_(2,n)=1`, but
`||R odot V||_(2,n)=S^3 sqrt(n)`. Integrating over activity `S`
still permits `S^4 sqrt(n)`. This is a counterexample to absorption
from these *norm bounds*, not a claim that a trained Gaussian trajectory
realizes those vectors. A localization estimate forbidding this joint
concentration is exactly what would improve the argument.

Finally, the favorable sign of the first term in (17) is specific to
the mobility Hilbert energy. It cannot be silently carried to higher
coordinate moments. For instance, for a positive rank-one matrix
`A=aa^T`, with `a=(1,2)` and `v=(1,-0.6)`,

\[
 \sum_i |v_i|^2v_i(Av)_i
 =(1-1.2)(1-0.432)<0.
\]

Consequently `dot v=-Av` increases the fourth-power coordinate norm
at that point. A finite-width high-moment source proof must therefore
also control the residual-feedback derivative in its chosen stronger
norm; Hilbert damping by itself does not certify that step.

**Remaining proof obligation.** Derive a width-uniform joint bound for
the localized actual response in (18)--(19), sufficiently strong to act
on the actual old-clock defect, while retaining its `P^-1` factor.
Neither the Gaussian source estimate proved here nor its `O(S^3)`
moving-field remainder closes that obligation. There is no assertion
that no such estimate exists.
