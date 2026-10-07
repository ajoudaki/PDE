# Residual decay lowers the causal source count to logarithmic power seven-halves

2026-10-06. Scoped author derivation, pending independent reconstruction.
The conclusion concerns the physical causal source, conditional on the
existing fitting and complex-time source events. It preserves the original
nonlinear network, label allowance, physical time, and whole-sphere error.
It is not a compact decoder or a final memory theorem.

Residual decay permits a smaller numerical residual cap on each time
patch. This changes the accumulated Lipschitz exponent from order
`log(en)^(3/2)` to order `log(en)`, without enlarging the source's
complex-time domain. Combined with the checked degree-independent
integrated interpolation bound, it gives an explicit matrix-call count

\[
 C\left[d+mL\beta^{300L}(1+m/\gamma)^3
                  Z^3\sqrt{\log(en)}\right]
 \le C\left[d+mL\beta^{300L}(1+m/\gamma)^3Z^{7/2}\right].
 \tag{1}
\]

The definitions of `Z` and the fixed physical parameters are below.
Thus the physical call chronology has, in particular, a sufficient
logarithmic power four at each fixed admissible problem. The construction
still uses width-`n` vectors and initialized matrices.

## 1. Model and numerical source interfaces

Use `A=W^(1)`, hidden matrices `W^(j)` for `2<=j<=L`, and stored
readout `w=W^(L+1)`. For `v=x/sqrt(d)` with Euclidean norm one,

\[
 z^{(1)}=Av,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
 h^{(j)}=\phi_j(z^{(j)}),\quad f_n(v)=w^Th^{(L)}/n.
\]

The initialization is independent Gaussian first entries `N(0,1)`,
hidden entries `N(0,1/n)`, and exactly zero readout. All blocks train
under mean squared loss with mobilities `(n,1,...,1,n)`. Residuals are
`r_a=f_n(v_a)-y_a`; they are not part of the backward derivative.
Keep the original intersection of fitting and source label allowances.

Write

\[
 \lambda=\gamma/m,\quad r=\lambda^{-1},\quad
 Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le1,\quad
 \ell=\log(en),\quad B=\beta^{100L},
\]
\[
 Z=(a_0+1)\ell+\log(e+B(1+r)),\qquad a_0\ge1.
 \tag{2}
\]

Here `gamma` is the original unweighted training covariance gap;
`beta>=10` is the activation envelope in Section 1 of
[PHYSICAL_PARAMETER_ACCOUNTING.md](PHYSICAL_PARAMETER_ACCOUNTING.md).
The scalar `r` in (2) is inverse gap; `r_a` remains a sample residual.
For `Y=0` the predictor is identically zero and no training program is
needed.

Let `u` be learned displacement. Use its sum norm

\[
 \|u\|=\|A-A_0\|_F/\sqrt n+
        \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n.
\]

Use normalized clock `tau=lambda t` and state
`bar u(tau)=u(tau/lambda)/Y`. The supplied real fitting bound gives

\[
 \|r(\tau/\lambda)\|_2/\sqrt m\le Ye^{-\tau/4}.
 \tag{3}
\]

Its stronger decay rate `1/2` is available, but not needed for clipping.
The accounting source supplies prediction sensitivity at most `B` in
the normalized state, true complex derivative bound
`M=B(1+r)`, and a complex-time radius `r_tau` with

\[
 r_\tau^{-1}\le B\sqrt\ell.
 \tag{4}
\]

These statements concern the true trajectory at every real anchor. No
complex extension of a clipped field is asserted. Set the horizon

\[
 T=2\{a_0\log n+\log(1+66Br)\}\le CZ.
 \tag{5}
\]

The normalized prediction tail after `T` is less than
`n^(-a_0)/4`, by the inherited whole-sphere fitting estimate.

## 2. A residual cap chosen before each patch

Retain the parameter projections and the carrier clip from the accounting
source, including clipping carriers before multiplication by activation
derivatives. At a patch beginning at normalized time `tau_j`, replace
only the residual projection radius by

\[
 q_j=2^{-\lfloor\tau_j/4\rfloor},\qquad R_j=Yq_j.
 \tag{6}
\]

Project the vector of training residuals onto the Euclidean ball of radius
`sqrt(m) R_j`. The cap is fixed throughout that patch. It is a known
dyadic multiple of the input label scale, not a measured future residual.
Since `log(2)<1`,

\[
 q_j\ge e^{-\tau_j/4}\ge e^{-\tau/4}
 \quad\text{for every }\tau\ge\tau_j.
\]

Thus the projection fixes the exact trajectory throughout the patch.
The same is true of the inherited parameter and carrier projections.
The resulting real vector field, denoted by `F_j` in normalized state
and time, is globally bounded and Lipschitz. Each patch has a different
field, but uses the original nonlinear physical field on the actual
trajectory. This is an explicitly scheduled numerical computation.

The dependence on the residual radius can be retained in the subtraction
proof of accounting (8). Before normalizing time and amplitude, that proof
gives

\[
 \operatorname{Lip}(F_{R})
 \le\beta^{70L}[1+R+RS\sqrt\ell],\qquad 0<R\le Y.
 \tag{7}
\]

To verify the replacement of `Y` by `R`, subtract each gradient product
in its residual, backward-response, and forward-feature factors. The
residual-difference term uses the nonexpansive projection and the output
Lipschitz bound; it does not use the projection radius. Both other terms
are multiplied by a residual whose RMS is at most `R`. The backward
subtraction recurrence has at most one carrier maximum, proportional to
`S sqrt(ell)`. Forward, backward, and gradient block bounds otherwise
remain those of accounting (6)--(9). Consequently the constant term in
(7) stays unchanged and precisely the other two terms contain `R`.

Normalizing state and time multiplies a field Lipschitz bound by `r`,
not `r/Y`. Since `R_j=Yq_j` and `S=16Yr`, the sharper bound is

\[
 \operatorname{Lip}(F_j)\le
 \beta^{70L}[r+Yr q_j+16(Yr)^2q_j\sqrt\ell].
 \tag{8}
\]

Using `Yr<=1/16` and the slack from exponent 70 to 100, a convenient
supplied bound is

\[
 \Lambda_j=B(1+r)(1+q_j\sqrt\ell),\qquad
 \|F_j\|\le M=B(1+r).
 \tag{9}
\]

The time-dependent cap is not a change to the scientific optimizer: the
computed approximate trajectory is numerical, and the reference remains
the exact autonomous dense flow.

## 3. Accumulated stability and the causal scheme

Choose a fixed ordinary patch length, shortening only the final patch:

\[
 h=\min\{1/8,r_\tau/4,[16B(1+r)\sqrt\ell]^{-1}\}.
 \tag{10}
\]

Let the actual lengths be `h_j` and the number of patches be `H`.
Then `h_j Lambda_j<=1/8` and

\[
 H\le1+CTB(1+r)\sqrt\ell\le CB(1+r)Z\sqrt\ell.
 \tag{11}
\]

The decreasing step function `q(tau)=2^(-floor(tau/4))` has integral
eight over the nonnegative real axis. Its left sums satisfy

\[
 \sum_j h_jq_j\le8+h\le9.
 \tag{12}
\]

Indeed, for each interval the left-rule excess is at most
`h[q(tau_j)-q(tau_(j+1))]`; summing telescopes to at most `h`.
Define the explicit deterministic bound

\[
 E=B(1+r)(T+9\sqrt\ell).
\]

Equations (9) and (12) give

\[
 \sum_jh_j\Lambda_j\le E\le CB(1+r)Z.
 \tag{13}
\]

Apply the checked method in
[SANE_INTEGRATED_COLLOCATION.md](SANE_INTEGRATED_COLLOCATION.md) separately
on each patch, using `F_j` throughout its `J=K` explicit Picard iterations.
Its node integral has operator norm below two, independently of `K`, so
the contraction is at most `2h_j Lambda_j<=1/4`. It uses the same positive
endpoint weights and the same final field evaluation as that method.

For completeness, the true derivative's integrated interpolation defect
is at most `6M h_j 2^(-K)`, because the radius `2h_j` disk fits in
the unchanged true complex domain. Fixed-point comparison therefore
gives node error at most `2(e_j+6M h_j 2^(-K))`, where `e_j` is the
starting error. Starting Picard at the constant node array leaves
iteration error at most `2h_jM4^(-K)`. Endpoint positivity then gives

\[
 e_{j+1}\le(1+2h_j\Lambda_j)e_j+8Mh_j2^{-K}.
 \tag{14}
\]

There is no error charge for replacing `F_j` by `F_(j+1)` at a boundary:
each field separately agrees with the true derivative on its own real
patch, and the next comparison starts from the committed endpoint.
The product of the multipliers in (14) is bounded by
`exp(2 sum_j h_j Lambda_j)<=exp(2E)`. Interior times use the integrated
operator norm, giving exactly as in the checked method

\[
 \sup_{0\le\tau\le T}\|\bar u(\tau)-\widetilde u(\tau)\|
 \le32M(T+1)e^{2E}2^{-K}.
 \tag{15}
\]

Take `K=J` to be the least power of two not below

\[
 \max\left\{2,
 \frac{2E+\log[1+256BM(T+1)n^{a_0}]}{\log2}\right\}.
 \tag{16}
\]

Multiplying (15) by prediction sensitivity `B` gives normalized error
less than `n^(-a_0)/8`. The endpoint frozen after `T` therefore has
normalized all-time, whole-sphere prediction error less than
`3n^(-a_0)/8`, including the fitted endpoint of the true flow. Moreover,

\[
 K=J\le CB(1+r)Z.
 \tag{17}
\]

The logarithm in (16) has only `a_0 log n`, `log B`, `log(1+r)`,
and `log(T+1)` contributions, all bounded by `CZ`. No conditioning
term has been hidden in an eventual width threshold.

Each field evaluation uses `O(mL)` initialized matrix actions and their
transposes. Residual projection changes a scalar radius and adds no
matrix call. Include all `HK(J+1)` evaluations, the initialized first
row coordinates, and the already proved low-rank displacement arithmetic.
Equations (11) and (17) prove (1). A late query still adds `O(L)`
initialized actions; it has not thereby become an initialization-free
compact query algorithm.

## 4. Matrix-answer noise precision

This paragraph addresses perturbations of the physical program, not the
separate scalar-history compiler. Suppose each field evaluation has an
additive normalized-state error of norm at most `delta`, uniformly over
its stages. The contraction recurrence adds at most `2h_j delta` per
Picard iteration. Summing the geometric series adds at most
`(8/3)h_j delta` to the final node error. The endpoint uses positive
weights, so its extra error is bounded by

\[
 h_j\delta+h_j\Lambda_j(8/3)h_j\delta
 \le(4/3)h_j\delta.
\]

Interior errors have the same form with a universal larger constant.
Thus the additional prediction error is at most

\[
 CB(1+T)e^{2E}\delta.
 \tag{18}
\]

The matrix-answer perturbation interface in accounting Section 5 remains
valid uniformly for these smaller caps: the new residual projections are
nonexpansive, and their radii are no larger than before. Its sufficient
field error bound is

\[
 \delta\le CB r(1+r)\sqrt\ell\,\sigma.
 \tag{19}
\]

Consequently, for `sigma=2^(-b_sigma)`, the sufficient requirement is

\[
 b_\sigma\ge C\left[
 1+E+(a_0+4)\ell+
 \log\{1+B^2(1+r)^2(1+T)\}\right].
 \tag{20}
\]

The least such integer obeys

\[
 b_\sigma\le C\beta^{100L}(1+m/\gamma)Z.
 \tag{21}
\]

This retains the same matrix perturbation model and Gaussian RMS failure
bound `R exp(-cn)` as the supplied interface, now with the revised call
count `R`. It does not assert that all scalar arithmetic has this precision
cost. In particular, the summary-history sensitivity requirement in
accounting (24), activation evaluation, input descriptions, and rounding
of the scalar cap itself require their own accounting. The cap schedule
uses exact dyadic factors; an inexact label-scale implementation must
charge its error or round its cap upward.

## 5. What larger complex-time radii would still require

The motivating uncapped adaptive-radius argument does not follow from
the existing source event. Source Sections 7--8 use a short complex
negative-Gram propagator with norm at most two, independently stopped
cavities, and vanishing complex-minus-real Gaussian coefficient radii.
The estimate `rho(z)<=rho(t) exp(2 K |z-t|)` alone controls none of
those variational or conditional-law hypotheses on a larger domain.

For a fixed real Gram, vertical propagation is unitary after multiplying
its symmetric generator by `i`. Along a complex nonlinear trajectory
the algebraic Gram is complex symmetric, not generally Hermitian, so that
argument does not give unitarity. Even at zero residual, a backward real
segment has growth independent of the residual. For example the scalar
loss `f(theta)^2` with `f(theta)=theta` has flow `theta'=-2theta` and
variational multiplier `exp(-2z)`, including arbitrarily large backward
growth at the stationary solution. This is an obstruction to that
particular uniform factor-two proof step, not a counterexample to a
larger neural analytic domain.

A deterministic late-time radius can be obtained from the existing small
parameter ball. If a real anchor lies inside a complex parameter ball
with boundary distance `b`, and throughout that ball the source bounds
are `||theta'||<=2 sqrt(K) rho` and `||Gram||<=K`, radial integration
gives

\[
 \|\theta(z)-\theta(t)\|
 \le\frac{\rho(t)}{\sqrt K}
                 (e^{2K|z-t|}-1).
\]

Any radius with this right side strictly below `b` permits continuation
by the local holomorphic ODE theorem. In the supplied analytic-tail proof,
`b` is a fixed multiple of a ball radius of order `n^(-1/2)`; its center
is the late source state. Hence this lemma does not supply the desired
early growing radius of order `1/[rho(t) sqrt(log n)]`. A uniform complex
parameter tube of that larger size has not been assumed here. The proved
improvement in (1) uses only (4).

## 6. Boundaries, provenance, and status

Established here, conditional on the supplied source event: the patchwise
residual projection, refined Lipschitz bound, accumulated exponent,
global collocation error, matrix-call count, and physical matrix-noise
precision. The original stochastic success-width qualification and all
deterministic source gates are retained. There is no new small-label cap.

Open: replacing the width-`n` causal source by a compact autonomous
state, preserving the uniform unseen-query law under the revised chronology,
and counting its complete memory, work, and scalar precision. For example,
squaring the call count to retain every history pair would already produce
logarithmic power seven; (1) by itself does not prove logarithmic power
four or five for decoder memory. The direct dense generation work is still
`C HK(J+1)(Ln^2+dn)(m+K)`, with live stages
`O((Ln^2+dn)K)` before retained source outputs.

The scoped inputs were the accounting and short-program notes, the now
authorized integrated-collocation note and its check, maintained notation,
and the specified source, fitting, finite-query, and analytic-tail interfaces
in `integrated_general_compression_20261004`. Links from those sources
were not followed beyond the authorized packet. The custom canonical
notation skill was permission-inaccessible; the supervisor-authorized
fallback was the explicit repository notation instructions and the
maintained notation contract. The conjecture and rigorous-math skills
were read and applied. No experiment, Git write, or maintained-file edit
was performed. This note is an author result, not an independent check
or promotion certificate.
