# Quantitative cavity return estimates with no time-node factor

28 September 2026. Bounded scoped continuation of the same study. Inputs:
the complete current `ACTIVATION_NEAR_QUADRATIC_ALLTIME.md` (SHA-256
`0801cb31acd77d8fbd157833090de3f88e5484a23cb471349b6e9c1b7e413bb7`)
and `ACTIVATION_GAUSSIAN_ALLTIME.md` (SHA-256
`6385264a060893eb226e94b4302ff86a095e00bf34e9fa364f4e7759486139d0`).
The rigorous-math skill remains in force. No other study, experiment,
external search, additional agent, manuscript edit, or Git mutation was
used. This file records new exact lemmas and the precise remaining
cavity construction, not a completed quantitative width theorem.

**Outcome.** Small total activity does give a response-propagator bound
`exp(C(1+M)S)` on a carrier stop at level `M`, independent of width and
the number of time nodes. A Gaussian nonlinear-return lemma below then
gives an `n^{-1/2}` error, with polynomial moment factors and no node-count
loss, even with adaptive scalar response coefficients. An exact scalar
self-feedback model closes its own Gaussian stop when its feedback
coefficient is `O(Y^2)` and proves a root-width quantitative return law.

What is not proved is that the full deep trained network has the requisite
dispersed cavity expansion with kernels independent of the deleted
Gaussian row. The ordinary stopped tangent bound alone cannot give its
quadratic remainder under merely `C^{1,1}` activations: differentiating
the gradient field differentiates a gate, and the derivative of that
gate need not be Lipschitz. Section 6 isolates this obstruction by an
explicit regularity example. Thus the `epsilon^{-5/2+o(1)}` consequence
is still conditional; no conditional central-limit theorem is invoked.

## 1. Exact stopped response bound for dense gradient flow

Use precisely the canonical model, averaged squared loss, zero readout,
Gaussian initialization, fixed small labels, and activation class of
the synthesis. Let `S=CY` be the proved activity bound. The parameter
Hilbert norm is

\[
 \|v\|_{\mathcal H_n}^2
 =\|v_1\|_F^2/n+\sum_{\ell=2}^L\|v_\ell\|_F^2+\|v_w\|_2^2/n.
 \tag{1}
\]

Write `J(theta):H_n -> R^m` for the prediction differential, with the
sample RMS norm in its target. Then the exact dense vector field is

\[
 F(\theta)=-2J(\theta)^*r(\theta),\qquad
 DF=-2J^*J-\frac2m\sum_a r_a\,\nabla^2 f_a.
 \tag{2}
\]

The second equation is first interpreted for smooth activations and then
by mollification or almost-everywhere differentiation. On the common
physical tube, stop additionally before any full backward carrier,
including the readout, has absolute coordinate exceeding `M>=1`.
There is a constant independent of width such that

\[
 \|\nabla^2 f_a\|_{\mathcal H_n\to\mathcal H_n}\le C(1+M).
 \tag{3}
\]

Here is the complete reason no width factor appears in (3). A unit
parameter perturbation changes every forward field by at most `C` in
RMS: use `||Vh||_2/sqrt(n)<=||V||F ||h||_2/sqrt(n)` and descend
the fixed-depth forward recurrence. The directional derivative of a
backward field is a sum of a bounded gate multiplying the next carrier
derivative and the term `phi''(z) P Dz`. The latter has RMS at most
`j M ||Dz||_2/sqrt(n)` on the stop. The operator-perturbation term has
RMS bounded by its Frobenius norm times the next backward RMS. Descending
the backward recurrence therefore adds factors `C M`; it does not
multiply them through depth. Finally differentiate the Jacobian blocks
`delta_1 tensor x`, `delta_l tensor h_(l-1)`, and `h_L`. The normalized
rank-one norm identity proves (3). No coordinate bound on `h` is used.

Let `U(t,s)` be the variational propagator along the stopped dense flow.
For `v'=DF(theta(t))v`, positivity of `J^*J` and Cauchy--Schwarz in
the finite sample index give

\[
 \frac12\frac d{dt}\|v\|_{\mathcal H_n}^2
 \le C(1+M)\rho(t)\|v\|_{\mathcal H_n}^2.
\]

Consequently

\[
 \|U(t,s)\|\le
 \exp\!\left(C(1+M)\int_s^t\rho(u)du\right)
 \le e^{C(1+M)S}.
 \tag{4}
\]

For an additive perturbation `b`, variation of constants gives
`v(t)=U(t,0)v(0)+integral_0^t U(t,s)b(s)ds`, with exactly this
bound. It is independent of physical time and time discretization.
Mollification preserves the bounded slope and derivative-Lipschitz
constants; the same norm inequality survives its limiting comparison.
This is a bound on the genuine tangent equation, not on a Picard
replacement of training. It applies as well to a masked-neuron cavity
gradient flow up to its corresponding physical and activity stops.

Forward-output response kernels obtained by composing (4) with the
bounded forward differential have operator bound `C exp(C(1+M)S)`.
Backward-output differentials contribute at most one extra factor
`C(1+M)`. Thus

\[
 K_M=C(1+M)e^{C(1+M)S}=n^{o(1)}
 \quad\text{when }M=C_0\sqrt{\log n}.
 \tag{5}
\]

Equation (5) is conditional on the stop. It neither assumes that the
stop is improbable nor proves that assertion. In particular using (4)
to multiply a Gaussian driving term by `K_M` would not close a stop
at `C_0 sqrt(log n)`; the resulting bound is much larger than that stop.
The small self-response coefficient in Section 4 serves a different role.

## 2. Conditional Gaussian quadratic averaging, without node counting

Let `F_cav` be any sigma-field, and let `g~N(0,I_n)` be independent
of it. All matrices in this section may be `F_cav`-measurable. For a
real matrix `B` with `||B||op<=K`, put

\[
 Q_B=\frac{g^TBg-\operatorname{tr}B}{n}.
\]

For every `p>=2`, conditionally on `F_cav`,

\[
 \|Q_B\|_{L^p}\le CK\{\sqrt{p/n}+p/n\}.
 \tag{6}
\]

To prove this, replace `B` by its symmetric part and diagonalize it.
If its eigenvalues are `lambda_i`, the log moment-generating function is

\[
 \log\mathbb E e^{tQ_B}
 =\sum_i\left[-t\lambda_i/n
       -\tfrac12\log(1-2t\lambda_i/n)\right]
 \le2t^2\sum_i\lambda_i^2/n^2
 \le2t^2K^2/n
\]

for `|t|<=n/(4K)`. Chernoff in the positive and negative directions
gives `Pr(|Q_B|>CK(sqrt(u/n)+u/n))<=2 exp(-u)`. Integrating that
tail proves (6). Singular matrices are allowed; there is no inverse Gram.

Now let there be arbitrarily many indices `r`, deterministic nonnegative
weights `alpha_r` with `sum alpha_r<=S`, cavity matrices `B_r` with
operator norms at most `K`, and scalar coefficients `beta_r(g)` with
`|beta_r(g)|<=B_0`. The coefficients may depend on all of `g`; no
independence or smoothness of them is required. Minkowski and (6) imply

\[
 \left\|\sum_r\alpha_r\beta_r(g)Q_{B_r}\right\|_{L^p}
 \le C S B_0K\{\sqrt{p/n}+p/n\}.
 \tag{7}
\]

The same proof works with integrals and a deterministic integrable
dominating weight. Random update weights are allowed only when their
absolute values have such a domination; the condition that their sum is
bounded pathwise, by itself, would let them select a maximum and would
not justify (7). For the actual small-label physical trajectories,
`|r_a(t)|<=sqrt(m)Y exp(-kappa t)` is an available deterministic
dominating weight on the proved initialization event. For a population
reference program, its activity steps are already deterministic.

This lemma directly handles arbitrarily long weighted response sums.
There is no union bound over time nodes and no conditional CLT.

## 3. Nonlinear return lemma for dispersed cavity perturbations

Assume `phi` has bounded slope `s` and derivative-Lipschitz constant `j`.
Let `z in R^n` and `A_r in R^(n by n)` be cavity-measurable, with
`||A_r||op<=K`. Let the weights and adaptive coefficients satisfy
the conditions above, and set

\[
 u(g)=\frac1{\sqrt n}\sum_r\alpha_r\beta_r(g)A_rg,
 \quad D=\operatorname{diag}(\phi'(z_j)),\quad
 R(g)=\frac{g^T[\phi(z+u(g))-\phi(z)]}{\sqrt n}.
 \tag{8}
\]

Then, conditionally on the cavity, for every `p>=2`,

\[
 \left\|R(g)-\sum_r\alpha_r\beta_r(g)
                    \frac{\operatorname{tr}(DA_r)}n\right\|_{L^p}
 \le C S B_0sK\{\sqrt{p/n}+p/n\}
       +\frac{Cj(SB_0K)^2p^{3/2}}{\sqrt n}.
 \tag{9}
\]

This is a nonlinear Gaussian return estimate with arbitrary adaptive
scalar messages; every dimension and weight is explicit. In particular
`K=exp(O(sqrt(log n)))`, polynomial-logarithmic `B_0,p`, and fixed
`S` make its error `n^{-1/2+o(1)}`.

For the proof, Taylor's integral formula and the Lipschitz derivative give

\[
 \phi(z_j+u_j)-\phi(z_j)=\phi'(z_j)u_j+e_j,
 \qquad |e_j|\le(j/2)|u_j|^2.
 \tag{10}
\]

The linear term in (8) is a sum of `alpha_r beta_r g^TDA_rg/n`.
Apply (7) with `||DA_r||op<=sK` to obtain the first term of (9).
For every coordinate and every `q>=2`, the Gaussian moment of a row
linear form and Minkowski give

\[
 \|u_j\|_{L^q}
 \le\frac{B_0}{\sqrt n}\sum_r\alpha_r
                       \|(A_rg)_j\|_{L^q}
 \le\frac{C S B_0K\sqrt q}{\sqrt n}.
 \tag{11}
\]

This remains valid for adaptive `beta_r` because its absolute bound was
taken before expectation. Hölder with three factors and (11) now give

\[
 \left\|\frac1{\sqrt n}\sum_jg_je_j\right\|_{L^p}
 \le\frac{j}{2\sqrt n}\sum_j
         \|g_j\|_{L^{3p}}\|u_j\|_{L^{3p}}^2
 \le\frac{Cj(SB_0K)^2p^{3/2}}{\sqrt n}.
 \tag{12}
\]

This proves (9). Notice that the remainder was not bounded by
`||g|| ||u||^2`; that coarser bound would lose the width gain.
The gain comes from dispersal: every coordinate in (11) is of size
`n^{-1/2}`, though the vector's Euclidean norm can be of order one.
No third derivative of `phi` is involved in this lemma.

If the actual perturbation is `u+e`, an additional deterministic bound is

\[
 \left|\frac{g^T[\phi(z+u+e)-\phi(z+u)]}{\sqrt n}\right|
 \le s\frac{\|g\|_2}{\sqrt n}\|e\|_2.
 \tag{13}
\]

Thus an `L^{2p}` Euclidean error `||e||2=O(n^{-1/2+o(1)})`
would suffice to preserve the rate. A mere RMS error of this size would
not suffice: it is larger by `sqrt(n)`.

## 4. An exact self-feedback model that closes its own Gaussian stop

This section verifies the small-self-response mechanism in a complete
cavity return problem. It is not asserted to be the full deep network.
Condition on arbitrary `z,h` independent of `g`, with
`||h||2/sqrt(n)<=B`. Let `epsilon>=0` satisfy `2 epsilon s<=1/2`,
and consider the scalar equation

\[
 q=\zeta+\frac1{\sqrt n}g^T
       [\phi(z+\epsilon qg/\sqrt n)-\phi(z)],
 \qquad\zeta=g^Th/\sqrt n.
 \tag{14}
\]

On `E={||g||2^2/n<=2}`, the second term in (14) is a contraction
in `q`, with Lipschitz constant at most `2 epsilon s<=1/2`.
Successive substitution therefore gives its unique real solution and

\[
 |q|\le2|\zeta|.
 \tag{15}
\]

The Gaussian norm tail from the same moment-generating calculation as
Section 2 gives `Pr(E^c)<=2 exp(-cn)`. Conditional Gaussianity of
`zeta` gives `Pr(|zeta|>B sqrt(2u))<=2 exp(-u)`. Thus for any
polynomial number of such rows, even dependent across their cavities,
a union bound gives `max |q|<=C B sqrt(log n)` with polynomially
high probability. The constant in (15) does not contain the much larger
response factor `K_M`. This is how a small self-return, rather than a
large Gronwall multiplier on the Gaussian drive, closes a carrier stop.

Set `dbar=n^{-1}sum_j phi'(z_j)` and define the corrected Gaussian
return `q_*=zeta/(1-epsilon dbar)`. Its denominator is at least `3/4`.
Taylor expansion as in Section 3 gives the exact error identity

\[
 (1-\epsilon\bar d)(q-q_*)
   =\epsilon q Q_D+\mathcal R,\qquad
 |\mathcal R|\le\frac{j\epsilon^2q^2}{2n^{3/2}}
                           \sum_j|g_j|^3.
 \tag{16}
\]

By (15), `||q 1_E||Lp<=CB sqrt(p)`. Hölder and (6) give

\[
 \|(q-q_*)\mathbf1_E\|_{L^p}
 \le C\epsilon Bs\{p/\sqrt n+p^{3/2}/n\}
      +Cj\epsilon^2B^2p^{5/2}/\sqrt n.
 \tag{17}
\]

For the remainder use `q^2` in `L^{2p}`, the cubic sum in `L^{2p}`,
and Minkowski; no independence of `q` and `g` is presumed. Taking
`p` proportional to `log n` and applying Markov proves a uniform
`n^{-1/2}` times a power of `log n` correction error for polynomially
many rows. The trace in (16) is the retained Gaussian self-response;
discarding it would leave an order-`epsilon` bias.

For the neural problem the relevant desired self-feedback coefficient is
`epsilon=O(S^2)=O(Y^2)`: the readout and backward RMS grow as `S`,
and the hidden update integrates one more activity factor. The population
response recurrences exhibit precisely this two-step scale. Equations
(14)--(17) show rigorously that this scale can close a Gaussian stop
without multiplying its driving Gaussian by `exp(CM)`. They do not by
themselves identify the actual finite-network self-response with (14).

## 5. Gaussian driving histories and concentration around a center

There are two further estimates available before identifying the bias.

First, let a cavity-measurable curve `v:[0,S]->R^n` obey
`||v(t)||2/sqrt(n)<=B` and
`||v(t)-v(s)||2/sqrt(n)<=A|t-s|`. For an independent Gaussian row,
elementary Gaussian chaining gives

\[
 \left\|\sup_{0\le t\le S}
       |g^Tv(t)|/\sqrt n\right\|_{L^p}
 \le C B\{\sqrt p+\sqrt{\log(2+AS/B)}\}.
 \tag{18}
\]

If `B=0` the curve is zero. Otherwise start with a mesh of spacing at
most `B/A`, containing `N<=C(1+AS/B)` points, and successively bisect
its cells. Each level-k Gaussian increment has standard deviation at
most `CB2^{-k}`, and there are at most `CN2^k` such increments. The
Gaussian tail union bound and integration give an `Lp` maximum at most
`CB2^{-k}sqrt(p+log(2N)+k)`. Sum this bound over `k>=0` and include
the coarse-node Gaussian maxima. The series converges and proves (18).
The continuous Gaussian linear form in the fixed vector curve is the
limit of those dyadic evaluations. This proof introduces no dependence
on a computational time-node count.

Dense forward histories have the required activity Lipschitz bound by
their deterministic small-label velocity estimate. On the carrier stop,
backward histories have an activity Lipschitz constant at most
`C(1+M)` by the gate derivative recurrence. Thus the logarithm in (18),
and not a factor `M` multiplying the Gaussian deviation, is the cost of
the more rapidly varying stopped backward history. This observation is
applicable to a genuinely row-independent cavity history; independence
is still essential.

Second, consider the set `E_M` of Gaussian initialized arrays whose
actual dense paths satisfy the common tube, Gram/activity bounds, and
the full-carrier coordinate stop never occurs. For two arrays in this
set, the synthesis's residual-damping comparison with cutoff `M` and
zero tail term gives

\[
 \sup_{t\ge0}\|\theta(t)-\widetilde\theta(t)\|_{\mathcal H_n}
 \le Ce^{C(1+M)S}
                      \|\theta(0)-\widetilde\theta(0)\|_{\mathcal H_n}.
 \tag{19}
\]

Here both initial predictions vanish, so the initial residual difference
is zero. One obtains (19) by first integrating the damped residual
difference, then substituting it into the parameter difference equations;
the remaining integrating factor is against `rho`, not physical time.
This proof compares two good paths directly and does not require that
the segment between their initial arrays stay in `E_M`.

Represent every initialized first/hidden Gaussian entry by standard
Gaussian coordinates `G`. The normalization in (1) gives exactly
`||theta_0(G)-theta_0(G')||H_n=||G-G'||2/sqrt(n)`.
Consequently each scalar test prediction at a fixed input, restricted
to `E_M`, is Lipschitz as a function of `G`, with constant

\[
 L_{n,M}(x)\le
 C(1+\|x\|/\sqrt d)e^{C(1+M)S}/\sqrt n.
 \tag{20}
\]

Extend this scalar function from `E_M` by the explicit McShane formula
`inf_(G' in E_M){f(G')+L_(n,M)||G-G'||2}`. It equals the actual
prediction on `E_M` and is globally Lipschitz with the same constant.
The Gaussian Lipschitz concentration inequality therefore gives

\[
 \Pr\{|f_n(t,x)-\mu_{n,M}(t,x)|>u\}
 \le\Pr(E_M^c)+2e^{-u^2/(2L_{n,M}(x)^2)},
 \tag{21}
\]

where `mu_(n,M)` is the expectation of that extension. The concentration
inequality used here is the elementary Gaussian form: for a real
L-Lipschitz function of independent standard normal coordinates,
`E exp(t(F-EF))<=exp(t^2L^2/2)`; its two Chernoff bounds give (21).
It may be proved by the Gaussian log-Sobolev inequality applied to
`exp(tF/2)` and integration in `t`. No claim about `Pr(E_M^c)` is
inserted into (21).

Finite time/input nets and the common physical/spatial prediction
moduli make the same statement uniform on a bounded input set and all
physical time, with additional `sqrt(log n)` factors: truncate time at
`C log n`, use a polynomial-size net, and bound the remaining variation
by `C exp(-kappa T)`. At `M=C_0 sqrt(log n)`, the displayed
fluctuation scale is `n^{-1/2+o(1)}`. This controls fluctuation around
an unspecified deterministic center. It supplies neither a bound on
the stop probability nor the center's bias toward the population flow.

## 6. The missing full-network cavity construction, stated sharply

Deleting a neuron removes its incident Gaussian rows/columns from the
outside system. Conditional on that outside system, an incident row is
independent Gaussian. The desired expansion for an outside source is

\[
 h^{\rm full}-h^{\rm cav}
 =\phi\!\left(z^{\rm cav}
       +n^{-1/2}\sum_r\alpha_r\beta_r(g)A_rg+e\right)
                    -\phi(z^{\rm cav}),
 \tag{22}
\]

where the matrices `A_r` are measurable with respect to the cavity,
their operator bounds satisfy (5), the scalar coefficients have proved
stopped bounds, their absolute weights have deterministic total `O(S)`,
and `||e||2` is `n^{-1/2+o(1)}` in sufficiently high moments.
Equation (9) would then quantify the corresponding reused-matrix return
without a query-Gram condition number or a number-of-nodes loss.
One must obtain (22) jointly for forward and transpose calls, with
the same matrices and the actual trained feedback. Independent copies
of those calls would change the object.

The following tempting derivation is invalid under the current hypotheses:
linearize the whole outside gradient flow around the cavity, bound its
tangent kernel by (4), and assert a quadratic Taylor remainder for its
vector field. That vector field contains `phi'(z)P`. Although `phi`
has a Lipschitz derivative, `phi'` need not itself have a Lipschitz
derivative. Thus the vector field need not have a Lipschitz derivative.

For a concrete example choose `0<alpha<1` and a smooth compactly
supported cutoff `chi` equal to one near zero. Define

\[
 \phi'(z)=\chi(z)|z|^{1+\alpha},\qquad
 \phi(z)=\int_0^z\chi(u)|u|^{1+\alpha}du.
 \tag{23}
\]

This activation has globally bounded slope and a globally Lipschitz
derivative, exactly as required. The gate is differentiable at zero
with derivative zero, but its first-order Taylor remainder there is
`|u|^(1+alpha)`, not `O(u^2)`. For `n` coordinates at that point,
each perturbed by `n^{-1/2}`, the Euclidean norm of the gate remainder
is `n^{-alpha/2}`, exceeding `n^{-1/2}`. Hence no deterministic
quadratic gate-remainder bound follows from the tube and carrier stop.

This example does not show the desired Gaussian theorem is false:
an actual Gaussian cavity does not have every preactivation zero.
It shows precisely why the proposed deterministic cavity remainder
argument is incomplete. A valid repair must use Gaussian averaging,
integration by parts, or a joint weak comparison that avoids demanding
pointwise quadratic expansion of the gate. The bounded weak derivative
`phi''` alone does not justify substituting the cavity tangent kernel
for the full, row-dependent tangent kernel with the error required in
(13). Imposing `C^{2,1}` regularity would change the stated problem.

Once (22) and its transpose counterpart are proved with the requisite
self-response smallness, Sections 2--5 provide the following legitimate
route: close the actual coordinate stop using Gaussian driving histories
and an `O(Y^2)` return coefficient; use the node-uniform errors (9) to
couple the same-matrix finite program to the population response; use
the existing small-activity damping comparison to handle actual feedback;
then integrate the carrier error against the deterministic exponentially
decaying residual envelope. This would give the needed all-time
`n^{-1/2+o(1)}` bias and tail-transfer bounds. The present work proves
the response norm, averaging, nonlinear-return, and scalar stop lemmas,
but not that full joint cavity expansion. The quantitative width theorem
and its moving-state exponent are therefore not marked proved.
