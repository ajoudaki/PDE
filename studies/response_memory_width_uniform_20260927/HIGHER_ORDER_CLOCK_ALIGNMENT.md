# Clock alignment and the terminal history lemma

Scoped analytic continuation, 28 September 2026. This report belongs to
`response_memory_width_uniform_20260927`. The assigned five scientific
inputs were read completely: `SMALL_LABEL_GAUSSIAN.md`,
`GENERAL_AUTONOMOUS_SYNTHESIS.md`, `GENERAL_REFERENCE_PROJECTION.md`,
`SMALL_LABEL_SPECTRAL_SLACK.md`, and `SLOW_ORDER_UNIFORM_BOUND.md`.
`docs/notation.qmd` and the investigate-conjectures and
solve-math-rigorously skills were also read. No other study, experimental
calculation, external search, or new agent was used. After an initial
independent investigation of the dense-reference clock, the supervisor
supplied the precise terminal-history lemma in Section 2 for an independent
check; no other route's draft was read.

**Result.** The terminal-history lemma is valid, including its exact
moving-endpoint energy identity, the zero prefix, Hilbert-valued sources,
memory order one, and passage to infinite physical time. Under its stated
hypotheses, the backward history has a uniform projection tail

\[
 \|(I-\Pi_{q,\tau})b_M\|_{L^2(0,\tau)}
 \le \frac{C\{1+M+\sqrt{\log(e+q)}\}}q.
 \tag{1}
\]

Here every finite physical endpoint is allowed, as is the finite terminal
clock endpoint. Paired with an actual forward history whose projection
tail is `C/q`, this yields `C q^-2(1+M+sqrt(log(e+q)))` for the integrated
product of their endpoint errors. This is an absolute integrated error
estimate, not merely a signed reconstruction estimate.

The new lemma bypasses the need to divide a dense source by the closure
residual. It does not itself construct the auxiliary clipped field or
bound its difference from the actual backward field. Those are separate
feedback obligations, made explicit in Section 5.

## 1. What the dense-reference clock does and does not supply

The exact dense learned-matrix reconstruction in the closure clock uses

\[
 B_D(\xi)=\frac{r_D(t(\xi))\delta_D(t(\xi))}
                         {\widehat\rho(t(\xi))},
 \qquad d\xi=\widehat\rho(t)\,dt.
 \tag{2}
\]

Consequently its squared history norm contains

\[
 \int_0^\infty
 \frac{|r_D(t)|^2\|\delta_D(t)\|^2}
      {\widehat\rho(t)}\,dt.
 \tag{3}
\]

Separate exponential upper/lower residual estimates give only a majorant
of the form `C exp((Lambda-2 lambda)t)` for this integrand. They do not
make (3) finite when `Lambda>=2 lambda`. A vanishing initial readout
removes the prefix jump but does not control this terminal denominator.
The physical bound on the derivative of `r_hat/rho_hat` controls a
different quantity and likewise does not directly bound (3).

This is an obstruction to an implication between the available estimates,
not a counterexample involving the actual neural dynamics. In particular,
the actual closure has the additional small relative residual forcing
`||J_hat E||/rho_hat <= C Y^(7/2)`. Arbitrarily chosen scalar exponential
histories need not respect that structure.

One possible further route would use the dense terminal eigendirection,
coarse state closeness, and invariant spectral cones to improve the
closure's lower residual bound. It was not completed here and no rate is
claimed from it. Even a signed dense-reference projection estimate would
still require an all-time damped comparison that accepts signed parameter
defects. The supplied all-time comparison in
`SLOW_ORDER_UNIFORM_BOUND.md` instead uses the integral of their absolute
norms. The lemma below directly addresses that stronger norm.

## 2. Precise terminal-history lemma

Let `H` be a real Hilbert space and fix `Y>0`, `kappa>0`, `Lambda>0`.
Let a positive, locally absolutely continuous scalar function `rho` obey

\[
 Y e^{-\Lambda t}\le\rho(t)\le Y e^{-\kappa t},
 \qquad
 a(t):=\int_t^\infty\rho(s)\,ds\le\rho(t)/\kappa.
 \tag{4}
\]

Write

\[
 \tau(t)=1+\int_0^t\rho(s)\,ds,
 \qquad A=1+\int_0^\infty\rho(s)\,ds\le1+Y/\kappa.
 \tag{5}
\]

Let `c` be a scalar, locally absolutely continuous function and let
`delta_M:[0,infinity)->H` be locally absolutely continuous. Suppose,
with constants independent of `M`, that

\[
 |c(t)|+|\dot c(t)|\le C_0,\qquad
 \|\delta_M(t)\|_H\le C_0,\qquad
 \delta_M(0)=0,
 \tag{6}
\]
\[
 \|\dot\delta_M(t)\|_H\le C_0(1+M)\rho(t)
 \quad\hbox{for almost every }t.
 \tag{7}
\]

Define one fixed history on `[0,A)` by

\[
 b_M(\xi)=0\quad(0\le\xi\le1),\qquad
 b_M(\tau(t))=c(t)\delta_M(t)\quad(t\ge0).
 \tag{8}
\]

For `1<=u<=A`, let `Pi_(q,u)` be ordinary Lebesgue `L2(0,u;H)`
orthogonal projection onto polynomials in the original clock coordinate
of degree strictly below the integer `q>=1`. The lemma asserts

\[
 \sup_{1\le u\le A}
 \|(I-\Pi_{q,u})b_M\|_{L^2(0,u;H)}
 \le \frac{C\{1+M+\sqrt{\log(e+q)}\}}q,
 \tag{9}
\]

where `C` depends only on the constants in (4)--(7). The value at `A`
is interpreted as an `L2` history; no pointwise terminal trace is
assumed. A finite list of sample-indexed histories is covered by taking
their Hilbert direct sum, with the sample RMS norm. The hypotheses then
hold with constants depending on the fixed sample count.

Only the positivity on compact intervals, the upper exponential estimate,
and the remaining-activity bound in (4) enter the proof. No estimate for
the ratio of two residuals is needed.

## 3. Proof of the terminal-history estimate

### 3.1. Freeze at a physical time

The product rule gives

\[
 \left\|\frac{d}{dt}b_M(\tau(t))\right\|_H
 \le C\{1+(1+M)\rho(t)\}.
 \tag{10}
\]

For any `T>=0`, define `v_T` to agree with `b_M` up to `tau(T)` and
to be constant equal to `b_M(tau(T))` on the rest of `[0,A]`. The zero
prefix joins continuously at clock time one, because `delta_M(0)=0`.
On the finite interval before `tau(T)`, the clock inverse is Lipschitz
by the positive lower residual bound on `[0,T]`. Thus `v_T` belongs
to `H1(0,A;H)`. The constant extension adds no jump and has derivative
zero after `tau(T)`.

The boundedness in (6) and the length of the changed interval give,
simultaneously for all `1<=u<=A`,

\[
 \|b_M-v_T\|_{L^2(0,u;H)}
 \le 2\sup_\xi\|b_M(\xi)\|_H\sqrt{a(T)}
 \le C e^{-\kappa T/2}.
 \tag{11}
\]

This estimate does not assert that `b_M` has a terminal limit. It only
uses its boundedness on a terminal interval whose clock length tends to
zero.

### 3.2. Weighted derivative energy

Fix a finite endpoint `u=tau(t)`. The change of variables
`d xi=rho(s) ds` yields

\[
 \begin{split}
 &\int_0^u \xi(u-\xi)\|v_T'(\xi)\|_H^2\,d\xi\\
 &\quad=
 \int_0^{\min(t,T)}
 \tau(s)\{\tau(t)-\tau(s)\}
 \frac{\|\frac{d}{ds}b_M(\tau(s))\|_H^2}{\rho(s)}\,ds\\
 &\quad\le\frac A\kappa
 \int_0^T
 \left\|\frac{d}{ds}b_M(\tau(s))\right\|_H^2\,ds.
 \end{split}
 \tag{12}
\]

For the last step, `tau(t)-tau(s)<=a(s)<=rho(s)/kappa`.
The same calculation applies directly at `u=A`. By (10), the scalar
inequality `(x+y)^2<=2x^2+2y^2`, and
`integral_0^infinity rho^2 <=Y^2/(2 kappa)`,

\[
 \sup_{1\le u\le A}
 \int_0^u \xi(u-\xi)\|v_T'(\xi)\|_H^2\,d\xi
 \le C\{T+(1+M)^2\}.
 \tag{13}
\]

No unweighted derivative energy uniform in `T` is claimed. The weighted
factor near the terminal endpoint is what cancels the inverse clock
speed in (12).

### 3.3. Weighted polynomial inequality and choice of cutoff

For every Hilbert-valued `v in H1(0,u;H)`, the shifted Legendre
Sturm--Liouville identity gives

\[
 \|(I-\Pi_{q,u})v\|_{L^2(0,u;H)}^2
 \le \frac1{q(q+1)}
      \int_0^u\xi(u-\xi)\|v'(\xi)\|_H^2\,d\xi.
 \tag{14}
\]

For clarity, if `ell_j` is the orthonormal shifted Legendre basis,
then
`-d/dxi[xi(u-xi) ell_j']=j(j+1) ell_j`. Integration by parts,
whose boundary terms vanish because the coefficient is zero at both
ends, identifies the coefficient derivative energy. Bessel's inequality
in the weighted derivative space gives
`sum_(j>=1) j(j+1)||<v,ell_j>||_H^2` at most the right-hand energy.
The terms omitted by degree-below-`q` projection all have
`j(j+1)>=q(q+1)`. This proves (14). The argument applies componentwise
to finite-dimensional projections of `H` and then by monotone convergence
to the separable closed span of the Bochner-measurable history. It
therefore includes infinite-dimensional Hilbert spaces.

Projection contraction, (11), (13), and (14) now give

\[
 \|(I-\Pi_{q,u})b_M\|_{L^2}
 \le C e^{-\kappa T/2}
     +\frac{C\sqrt{T+(1+M)^2}}{\sqrt{q(q+1)}}.
 \tag{15}
\]

Choose `T=2 log(e+q)/kappa`. Then the first term is `C/(e+q)`, and
the second is bounded by the right side of (9). This proves the lemma.
The denominator `sqrt(q(q+1))` is positive at `q=1`, so no exceptional
small-order argument is required.

## 4. Exact moving-endpoint identity

Let `b in L2(0,A;H)` be any fixed history. For `0<u<=A`, define

\[
 p_u=\Pi_{q,u}b,\qquad
 V(u)=\int_0^u\|b(\xi)-p_u(\xi)\|_H^2\,d\xi.
 \tag{16}
\]

On any compact interval of positive `u`, the coefficients of `p_u` in
the fixed monomial basis `1,xi,...,xi^(q-1)` are locally absolutely
continuous Hilbert-valued functions. Indeed their vector of moments is
locally absolutely continuous; it is multiplied by the inverse of the
smooth, positive definite scalar monomial Gram matrix. Consequently,
for almost every such `u`, differentiation gives

\[
 V'(u)=\|b(u)-p_u(u)\|_H^2
       -2\int_0^u
         \langle b(\xi)-p_u(\xi),\partial_u p_u(\xi)\rangle_H\,d\xi.
 \tag{17}
\]

The derivative `partial_u p_u` is still a polynomial of degree below
`q` in the original variable `xi`. Projection orthogonality therefore
makes the integral vanish. Hence the exact identity is

\[
 V'(u)=\|b(u)-(\Pi_{q,u}b)(u)\|_H^2
 \quad\hbox{for almost every }u.
 \tag{18}
\]

The moving shifted-Legendre basis does not change this conclusion: its
span is exactly the same polynomial subspace used in (16). Conversely,
the identity would need reconsideration for an approximation family whose
function space itself changed with the endpoint.

If the history is exactly represented over the unit prefix, then
`V(1)=0`. This includes a zero backward prefix and a constant forward
prefix, because `q>=1`. Integrating (18) and changing variables proves

\[
 \int_0^t\rho(s)
 \|b(\tau(s))-(\Pi_{q,\tau(s)}b)(\tau(s))\|_H^2\,ds
 =\|(I-\Pi_{q,\tau(t)})b\|_{L^2(0,\tau(t);H)}^2.
 \tag{19}
\]

At infinite physical time, the nonnegative integral increases to its
limit. The right side converges to
`||(I-Pi_(q,A))b||_L2(0,A)^2`: the finite list of moments, the scalar
Gram matrix, and the integral of `||b||^2` all converge as `u` increases
to `A`. Thus (19) holds with `t=infinity` and terminal endpoint `A`,
without a terminal trace for `b` or its normalized residual factor.

## 5. Consequence for absolute defect and the exact feedback obligation

Write `e_b(s)` and `e_h(s)` for the two moving-endpoint errors in
(19). For histories whose prefixes are exactly represented,
the rank-one Hilbert--Schmidt norm identity and Cauchy--Schwarz give

\[
 \int_0^\infty\rho(s)
      \|e_b(s)\otimes e_h(s)\|_{\rm HS}\,ds
 \le
 \|(I-\Pi_{q,A})b\|_{L^2}
 \|(I-\Pi_{q,A})h\|_{L^2}.
 \tag{20}
\]

If the forward projection tail is `C/q`, substituting (9) proves

\[
 \int_0^\infty\rho\,
       \|e_{b_M}\otimes e_h\|_{\rm HS}
 \le \frac{C\{1+M+\sqrt{\log(e+q)}\}}{q^2}.
 \tag{21}
\]

Thus the order exponent supplied by this analytic lemma is two up to
the displayed logarithmic/cutoff factor. If a later feedback argument
uses `M=O(sqrt(log(e+q)))` and multiplies by `exp(CM)`, its order
envelope would be `q^-2 sqrt(log(e+q)) exp(C sqrt(log(e+q)))`, which
is bounded by `C_gamma q^-gamma` for each fixed `gamma<2`.
That last sentence specifies the consequence of those additional
estimates; the lemma does not assert them.

There is a precise way to isolate the remaining source error. If
`b_hat=b_M+d`, projection linearity and contraction give

\[
 \|(I-\Pi_{q,A})b_{\rm hat}\|_{L^2}
 \le \frac{C\{1+M+\sqrt{\log(e+q)}\}}q
       +\|d\|_{L^2(0,A;H)}.
 \tag{22}
\]

Using (20) for the actual backward and forward histories then bounds
the actual absolute defect by

\[
 \int_0^\infty e_E(s)\,ds
 \le \frac{C\{1+M+\sqrt{\log(e+q)}\}}{q^2}
       +\frac Cq
         \|b_{\rm hat}-b_M\|_{L^2(0,A;H)},
 \tag{23}
\]

with the finite sums over layers and samples absorbed into `C`.
This is the exact place where a clipped-closure construction and
one-reference carrier control must enter. It is insufficient to know
only that the difference norm in (23) is bounded: that reproduces
`C/q`. A bound by a small coefficient times the actual path discrepancy
plus controlled dense-only tails would instead give an absorbable
feedback term, provided it is combined with the established all-time
damped comparison with its constants tracked. The present check does
not assume that last bound or an empirical closure Gaussian law.

## 6. Check outcome and scope

The supplied terminal-history lemma is proved under exactly (4)--(7).
The moving-endpoint identity is exact for Hilbert-valued histories and
the original unweighted old-clock polynomial projection. Zero readout
is used specifically to join the zero prefix without a jump. Neither
bounded variation nor convergence of the normalized residual direction
at infinite time is needed. All statements retain the original clock.

No new theorem on the full autonomous parameter or prediction error is
claimed by this report alone. The old dense/closure ratio route remains
unclosed here, while the terminal-history mechanism supplies the
stronger absolute-error ingredient (23) for the separate feedback proof.
This is an internal analytic check, not a complete independent promotion
review.

## 7. Subsequent complete-candidate check

The supervisor subsequently supplied the complete frozen file
`NEAR_QUADRATIC_ALLTIME_BOUND.md`, SHA-256
`89d85b31167ab5087e89f5a716655d6215e6e6b654e7563f8280c923b6afa259`,
for a check of its new proof chain, with its Section 2 prior theorems
accepted as supplied inputs. That entire frozen file was read. No
other route draft or additional scientific input was read during this
check. The following result concerns this hash only.

**Scoped PASS:** Sections 1--6 prove the stated all-time parameter bound
from the supplied Section 2 inputs. In particular, the new clipping and
feedback steps fill the obligations left open in Section 5 of this
report. No repair is required in that analytic chain.

The potentially delicate implications were checked explicitly:

1. **Clipped recursion.** With `D_hat=tanh'(z_hat)`, `D_D=tanh'(z_D)`,
   and `k_D=W_D^T delta_D,next`, the exact subtraction is

   \[
   \begin{split}
   \delta^M-\delta_D={}&
   D_{\rm hat}\{\operatorname{clip}_M(W_{\rm hat}^T\delta^M_{\rm next})
                  -\operatorname{clip}_M(k_D)\}\\
   &+(D_{\rm hat}-D_D)\operatorname{clip}_M(k_D)
        +D_D\{\operatorname{clip}_M(k_D)-k_D\}.
   \end{split}
   \]

   The first term costs the next-layer mismatch times a bounded operator
   norm plus the matrix difference times a bounded dense backward RMS
   norm. The second costs `2M ||z_hat-z_D||_RMS`; the last costs the
   dense carrier tail. Thus descending through fixed depth adds the
   `M d` terms and does not multiply their `M` factors. The ordinary
   un-clipped subtraction has the same bound by splitting the dense
   carrier at `M`. Their triangle inequality is exactly candidate (18).
   At the top, `w_D` is coordinatewise bounded, and the auxiliary and
   actual top fields coincide.

2. **Clipped derivative.** Coordinatewise clipping is a contraction
   and is one-Lipschitz. Its chain rule is valid almost everywhere
   along each finite-width absolutely continuous path. In the product
   rule the gate derivative multiplies the clipped carrier and costs
   `2M ||dot z_hat||_RMS`; the other terms propagate the derivative
   through a bounded matrix or multiply `dot W_hat` by a bounded
   backward RMS norm. Candidate (5) therefore proves (13) with one
   power of `1+M`. All auxiliary fields vanish at initial time because
   the readout is exactly zero.

3. **Change of activity measure.** From the preceding subtraction and
   bounded coefficients `c_a`,
   `||b-bM||_L2(dxi)` is bounded by `C(1+M)D` plus
   `C (integral rho_hat H_n^2)^(1/2)`. Since the dense carrier RMS
   tail is bounded deterministically on the common physical event,

   \[
   \int\rho_{\rm hat}H_n^2
   \le C\int\rho_D H_n+C\int|\rho_{\rm hat}-\rho_D|
   \le C(Z_n+Q).
   \]

   No relative residual comparison or tail bound on a closure carrier
   enters this estimate.

4. **Absorption.** With `U=eps+Z_n`, the supplied damping estimates give
   `D<=A_M U` and `Z_n+Q<=C(1+M)A_M U`. Candidate (21) follows.
   After the linear coefficient is at most `1/4`, the exact inequality
   `h sqrt(U)<=U/4+h^2` leaves a source
   `C(1+M)A_M/q^2`. Multiplying by the outer stability factor `A_M`
   gives candidate (22), including its `A_M^2` term. No smallness of
   `U` was used for this absorption.

5. **Uniform orders and widths.** All preceding inequalities hold on
   the same event, for every integer cutoff, every physical freeze
   time, and every order. It is therefore legitimate to choose the
   cutoff using the random dense-only remainder. With
   `s=q^-2+a_n`, one has `s>=q^-2`, so the selected cutoff obeys
   `M<=C+C sqrt(log(e+q))`. Hence
   `(1+M) exp(KM)/q` tends to zero uniformly in width and in `a_n`.
   This gives one sufficient order threshold. Fixed smaller orders
   and the non-small-`s` regime are covered by the supplied common
   physical parameter bounds. The resulting remainder is independent
   of order; no event common across different widths is asserted.

The direct prediction consequence also follows: on a bounded set of
test inputs, forward subtraction bounds prediction discrepancy by
`C_test D`. Over a test law with a finite second input moment, the
pointwise estimate is `C(1+||x||)D`, giving the corresponding norm
bound after integration. The arithmetic of the conditional powers in
candidate Section 7 is consistent with its stated, unproved numerical
width certificates.

**Supplied premise for Section 7:** after the core proof check, the
supervisor additionally authorized treating the stated observation and
population-predictor transfer theorem of `POPULATION_TEST_ERROR.md`
(SHA-256
`9618e8cff7dca52a52e9fe63df00630ee8d07303a2b40d3171ed16db03744186`)
as a supplied input. Its underlying construction of fixed-order predictor
limit points was not reread or reconstructed here. With that explicit
premise, Section 7's improved predictor envelope is the closed-bound
limit consequence of the verified finite-width estimate, and passes
within that scope. The principal parameter theorem (2) does not depend
on this extra input.

This is a scoped internal author check against supplied prior theorems,
not a reconstruction of their complete proofs or an independent
promotion review.
