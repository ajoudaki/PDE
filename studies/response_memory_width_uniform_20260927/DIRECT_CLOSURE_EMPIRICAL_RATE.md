# Direct closure: order-uniform empirical contraction estimates

28 September 2026. Scoped theoretical continuation. Inputs: complete
`DIRECT_CLOSURE_WIDTH_ROUTE.md`, `ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`,
and the author's `WIDTH_RATE_ACTIVITY_CAVITY_R2.md`. No other study,
external search, experiment, agent, manuscript edit, or Git operation.
Only this report was written. The rigorous-math and research-audit
instructions remain in force.

**Result.** The learned contractions of the actual closure have an exact
coupling decomposition into particle/moment errors and empirical
covariance errors of an independent reference. All moment coefficients
are projections of one two-time covariance kernel. Its Hilbert--Schmidt
variance is exactly of order `1/n`, with no factor of `q`. This remains
true for the closure's random activity clock: the projection can depend
on the entire actual network, because its clock measure is dominated by
a deterministic finite measure.

The result is conditional only at the reference-construction step: one
needs independent copies of a correctly identified population reference
with the stated mixed moments. Actual trained neurons are never assumed
independent. The initialized forward and transpose actions leave two
explicit source terms which the empirical estimate does not bound.
Consequently this is analytic progress on the learned branch, not a
completed direct closure width theorem.

## 1. A deterministic dominating measure handles the random clock

On the assigned common initialization event, every actual closure obeys

\[
 0\le\rho_n(t)\le \bar\rho(t):=Y e^{-\kappa t},\qquad
 \tau_n(t)=1+\int_0^t\rho_n(s)\,ds\le A:=1+Y/\kappa.
 \tag{1}
\]

Use a history domain consisting of a prefix interval `[0,1]` followed by
physical times `[0,infinity)`. The actual clock measure and its
deterministic dominating measure are

\[
 \nu_n=d\sigma\big|_{[0,1]}+\rho_n(t)dt,
 \qquad
 \bar\nu=d\sigma\big|_{[0,1]}+\bar\rho(t)dt.
 \tag{2}
\]

Forward histories equal their initial value on the prefix; backward
histories are zero there. At physical endpoint `t`, the prefix plus the
physical past `[0,t]` is carried by the cumulative clock to
`[0,tau_n(t)]`. This change of variables is valid even if `rho_n`
vanishes: flat physical intervals have zero clock measure.

Let `e_k^tau` be the shifted orthonormal Legendre functions of the
assigned route. For any scalar history `v`, write

\[
 M^{n,q}_{v,k}(t)=
   \int_{\text{past}(t)} e_k^{\tau_n(t)}(\operatorname{clock}_n(s))
                                               v(s)\,\nu_n(ds).
 \tag{3}
\]

The moment map is a contraction from the actual history `L2` space into
`ell2({0,...,q-1})`. This statement is pathwise. Its validity does not
require the clock, the projection, or its endpoint to be independent of
the histories.

## 2. One covariance kernel controls every moment contraction

For the moment suppose reference row histories `(v_i,u_i)`, `i<=n`,
are independent copies of a pair `(v,u)`. Independence is required
between rows, not between `v_i` and `u_i` in one row. Vector-valued
histories of fixed training dimension are allowed. All statements can
also be read conditionally on one common environment, if the rows are
conditionally independent and the displayed moment bounds hold there.

Define the raw empirical covariance error, before choosing any clock,

\[
 K_n(s,t)=\frac1n\sum_i v_i(s)u_i(t)-\mathbb E[v(s)u(t)].
 \tag{4}
\]

Its relevant norm is the Hilbert--Schmidt, or product `L2`, norm

\[
 \mathcal K_n^2
 =\int_0^\infty\int |K_n(s,t)|^2\,\bar\nu(ds)\bar\rho(t)dt.
 \tag{5}
\]

The first variable includes the prefix, and the second is physical time.
For vector histories use the sum over the fixed component pairs.
Assume the explicit mixed fourth-moment condition

\[
 V:=\mathbb E\!\left[
    \|v\|_{L^2(\bar\nu)}^2
    \|u\|_{L^2(\bar\rho dt)}^2\right]<\infty.
 \tag{6}
\]

Then independence of the centered row tensors gives the exact identity

\[
 \mathbb E\mathcal K_n^2
 =\frac1n\left\{
   \mathbb E\|v\otimes u\|_{\rm HS}^2
                    -\|\mathbb E(v\otimes u)\|_{\rm HS}^2\right\}
 \le V/n.
 \tag{7}
\]

Indeed expand the squared Hilbert norm of the sum. Every cross-row term
vanishes by independence and centering; the rank-one tensor norm is
`||v tensor u||HS=||v|| ||u||`. No time independence is used.

The empirical error of the moment/current-field contraction is

\[
 \xi^{n,q}_k(t)=\frac1n\sum_iM^{n,q}_{v_i,k}(t)u_i(t)
 -\int_{\text{past}(t)}e_k^{\tau_n(t)}(\operatorname{clock}_n(s))
                       \mathbb E[v(s)u(t)]\,\nu_n(ds).
 \tag{8}
\]

The second expression is the population covariance passed through the
same, possibly random, projection. It is not incorrectly described as
the conditional expectation of the first expression given that clock.
Subtraction and (4) show that (8) is exactly the projection of the
covariance-error column `K_n(.,t)`. Projection contraction and measure
domination therefore give, pathwise,

\[
 \int_0^\infty\rho_n(t)
            \sum_{k<q}|\xi^{n,q}_k(t)|^2dt
 \le\int_0^\infty\bar\rho(t)
           \int|K_n(s,t)|^2\bar\nu(ds)dt
 =\mathcal K_n^2.
 \tag{9}
\]

The bound holds simultaneously for every `q` and every clock satisfying
(1), for these one set of reference histories. In particular the clock
may be selected from all the Gaussian initialization arrays, the actual
trained trajectory, and the same reference rows. No net over `q`, clock
paths, or time nodes is needed.

If the population reference itself changes with `q`, equation (9) still
gives the same constants for each order with uniform reference moment
bounds, hence along every deterministic choice `q=q_n`. It does not by
itself create one simultaneous event for infinitely many different
reference laws.

### Higher moments and probability bounds

For `p>=2`, symmetrization of independent Hilbert-valued row tensors and
the random-sign Hilbert norm bound give

\[
 \|\mathcal K_n\|_{L^p}
 \le \frac{C\sqrt p}{\sqrt n}
       \big\|\|v\|_{L^2(\bar\nu)}
                    \|u\|_{L^2(\bar\rho dt)}\big\|_{L^p}.
 \tag{10}
\]

To verify the sign bound, replace signs by centered Gaussian multipliers
using conditional Jensen over their absolute values. For a Gaussian
Hilbert sum `sum gamma_i x_i`, its `Lp` norm is at most
`C sqrt(p) (sum ||x_i||^2)^(1/2)`; diagonalizing its covariance and
using the Gaussian square moment-generating function proves this bound.
Minkowski in `Lp/2` then completes (10).

For example, uniform subGaussian marginal bounds for the reference
histories imply
`|| ||v||L2 ||Lp <= C sqrt(p)` by Minkowski in the time integral;
no subGaussian supremum over time is required. Equation (10) then gives
`||mathcal K_n||Lp<=C p^(3/2)/sqrt(n)`. Taking `p` proportional to
`log n` gives polynomially high probability with logarithmic losses,
uniform in the allowed projections. Such marginal bounds have to be
proved for the chosen closure reference; they are not asserted for the
actual finite trained array by this argument.

There is one reference to which these hypotheses can already be applied
under the original assumptions. The assigned synthesis supplies a unique
dense population flow with uniform subGaussian time marginals for its
forward and backward fields. Independent copies of its whole row history
therefore satisfy (6) and (10), including `b_a=c_a delta_a` because its
normalized residual coefficients are deterministic and bounded. Thus
the integrated root-width empirical source theorem is already valid for
the projected **dense population reference**, simultaneously in its
moment order and admissible clocks. Comparing that projected reference
with the actual closure additionally retains an order-truncation defect;
it does not identify an order-`q` population closure law. Its initialized
action coupling is still the separate problem in Section 6.

## 3. Exact application to the learned forward and backward branches

Fix a hidden matrix and suppress its layer index. Group sample and
moment indices into one coefficient space `E_q=R^(m q)`. For actual
neurons write `H_i,B_i in E_q` for their moment vectors, and `h_i,delta_i`
for a current training field. A star denotes a coupled reference row.
Its moment vectors in this section use the **actual clock** (3), so
they need not themselves be independent after that transformation.
Only the underlying reference physical histories are independent.

Let

\[
 c_n=\frac1n\sum_i H_i h_i,\qquad
 d_n=\frac1n\sum_i B_i\delta_i,
\]
\[
 c_*^{\nu_n}=\int e^{\tau_n}(\operatorname{clock}_n(s))
                  \mathbb E[h_*(s)h_*(t)]\,\nu_n(ds),
\]
\[
 d_*^{\nu_n}=\int e^{\tau_n}(\operatorname{clock}_n(s))
                  \mathbb E[b_*(s)\delta_*(t)]\,\nu_n(ds).
 \tag{11}
\]

The vector-valued basis notation includes the training sample index.
The learned fields, before their fixed factor `-2/m`, are
`B_i dot c_n` and `H_i dot d_n`.

Use RMS over rows for scalar and `E_q`-valued arrays. Set
`E_H=||H-H_*||RMS`, `E_B=||B-B_*||RMS`,
`e_h=||h-h_*||RMS`, and `e_delta=||delta-delta_*||RMS`.
Let `R_H,R_B` be actual moment RMS bounds, and let

\[
 R_{H,*}^2=\frac1n\sum_i\int|h_i^*(s)|^2\bar\nu(ds),\qquad
 R_{B,*}^2=\frac1n\sum_i\int|b_i^*(s)|^2\bar\nu(ds).
 \tag{12}
\]

Projection contraction bounds the reference moment RMS by these last
two quantities at every time, order, and admissible clock.

Let `xi_F,xi_B` be (8) for the two respective history/current pairs

\[
 (v,u)=(h_*,h_*),\qquad (v,u)=(b_*,\delta_*).
 \tag{13}
\]

Exact subtraction gives

\[
 c_n-c_*^{\nu_n}
 =\frac1n\sum_i(H_i-H_i^*)h_i
       +\frac1n\sum_iH_i^*(h_i-h_i^*)+\xi_F,
\]
\[
 d_n-d_*^{\nu_n}
 =\frac1n\sum_i(B_i-B_i^*)\delta_i
       +\frac1n\sum_iB_i^*(\delta_i-\delta_i^*)+\xi_B.
 \tag{14}
\]

Thus, if the actual current RMS bounds are `||h||RMS<=C_h` and
`||delta||RMS<=C_delta`,

\[
 \|c_n-c_*^{\nu_n}\|
 \le C_h E_H+R_{H,*}e_h+\|\xi_F\|,
\]
\[
 \|d_n-d_*^{\nu_n}\|
 \le C_\delta E_B+R_{B,*}e_\delta+\|\xi_B\|.
 \tag{15}
\]

For the learned fields themselves use the asymmetric expansion

\[
 Bc_n-B_*c_*^{\nu_n}
    =(B-B_*)c_n+B_*(c_n-c_*^{\nu_n}),
\]
\[
 Hd_n-H_*d_*^{\nu_n}
    =(H-H_*)d_n+H_*(d_n-d_*^{\nu_n}).
\]

Since `||c_n||<=R_H C_h` and `||d_n||<=R_B C_delta`,

\[
 \|Bc_n-B_*c_*^{\nu_n}\|_{\rm RMS}
 \le R_H C_h E_B
  +R_{B,*}(C_hE_H+R_{H,*}e_h+\|\xi_F\|),
\]
\[
 \|Hd_n-H_*d_*^{\nu_n}\|_{\rm RMS}
 \le R_B C_\delta E_H
  +R_{H,*}(C_\delta E_B+R_{B,*}e_\delta+\|\xi_B\|).
 \tag{16}
\]

Every coefficient is independent of the coefficient-space dimension.
This proof uses no independence between the empirical source and the
reference moment array multiplying it. In particular

\[
 \|R_{B,*}\xi_F\|_{L^2(\rho_n dt;E_q)}
                 \le R_{B,*}\mathcal K_{F,n},\qquad
 \|R_{H,*}\xi_B\|_{L^2(\rho_n dt;E_q)}
                 \le R_{H,*}\mathcal K_{B,n}.
 \tag{17}
\]

Equations (7), (12), and (17) give an `O_Pr(n^-1/2)` all-time activity
`L2` source under the stated reference moments, uniformly in `q`.
Higher moments follow by Hölder and (10). Independence of different
layers is not needed; only the within-layer reference row law used in
each empirical contraction is required.

## 4. Centering the forward prefix exposes the small-label factors

The actual deterministic estimates permit a useful sharper decomposition.
Training-sample sums are suppressed in this section; the formulas apply
componentwise and then sum over the fixed sample count.
Put `S=Y/kappa`. The given forward derivative energy is
`integral ||partial_tau h||RMS^2 d tau<=C Y^3`, and the available clock
length after the prefix is at most `S`. Cauchy--Schwarz gives

\[
 \sup_t\|h(t)-h(0)\|_{\rm RMS}\le CY^2.
 \tag{18}
\]

Write `d_h(s)=h(s)-h(0)` after the prefix and zero on the prefix.
Since `e_0^tau=1/sqrt(tau)`, the exact moment decomposition is

\[
 H_q(t)=\sqrt{\tau_n(t)}\,e_0 h(0)+D_q(t),
 \qquad D_q=M_{d_h}^{n,q}.
 \tag{19}
\]

Here `e_0` without a superscript is the zeroth coordinate unit vector
in the coefficient space, rather than the scalar basis function.

For the actual finite arrays, uniformly in order and time,

\[
 \|D_q\|_{\rm RMS}\le CY^{5/2},\quad
 \|B_q\|_{\rm RMS}\le CY^{3/2},\quad
 \|B_0\|_{\rm RMS}
 =\frac1{\sqrt{\tau_n}}\left\|\int_0^t\rho_n b\,ds\right\|_{\rm RMS}
 \le CY^2.
 \tag{20}
\]

The first two inequalities use history energy and the zero backward
prefix; the last uses `||b||RMS<=C Y` and total activity `S`.
Consequently the learned forward field splits exactly into

\[
 B_q\cdot c_q
 =\sqrt{\tau_n} B_0\,\langle h(0),h(t)\rangle_n
     +B_q\cdot\langle D_q,h(t)\rangle_n.
 \tag{21}
\]

The corresponding backward field splits as

\[
 H_q\cdot d_q
 =\sqrt{\tau_n}h(0)\,\langle B_0,\delta(t)\rangle_n
      +D_q\cdot\langle B_q,\delta(t)\rangle_n.
 \tag{22}
\]

The leading terms have deterministic sizes `O(Y^2)` and `O(Y^3)`;
the remaining products have sizes `O(Y^4)` and `O(Y^5)` in RMS/operator
estimates, using the actual field bounds. This improves the coarser
product of the total uncentered moment energies.

If the independent reference also has the natural marginal `L4` scales

\[
 \|h_*(t)\|_4+\|h_*(0)\|_4\le C,\quad
 \|h_*(t)-h_*(0)\|_4\le CY^2,\quad
 \|b_*(t)\|_4+\|\delta_*(t)\|_4\le CY,
 \tag{23}
\]

then applying (7) separately to (21)--(22) yields learned forward
stochastic forcing `O_Pr(Y^2/sqrt(n))` and backward stochastic forcing
`O_Pr(Y^3/sqrt(n))`, for fixed positive `Y`; the centered remainders
carry the extra powers just displayed. The constants in a higher-moment
version are fixed by the corresponding explicit mixed moments.

Equation (23) is a stated sufficient reference condition, not a new
assumption inserted into the desired theorem. The deterministic RMS
bounds (18)--(20) do not themselves imply (23), nor even the mixed
fourth moment (6). For example a scalar random variable with tail
`Pr(X>t)=t^-3` for `t>=1` has finite second moment and infinite fourth
moment. An energy estimate alone therefore cannot justify the variance
calculation for its empirical square. The needed reference moments must
come from the closure's population response construction or another
proved bound. Without (23), the order-uniform root-width source still
holds under (6), with its displayed moment-dependent constant.

## 5. Readout sources and uniform-in-time versus integrated control

The zero readout means the reference row obeys

\[
 w_i^*(t)=-\frac2m\sum_b\int_0^t r_b^*(s)h_{b,i}^*(s)\,ds.
 \tag{24}
\]

When the population residual is deterministic, or deterministic given
the common reference environment, the empirical readout/feature error
is exactly an integral of the same forward covariance kernel:

\[
 \frac1n\sum_iw_i^*(t)h_{a,i}^*(t)
                   -\mathbb E[w^*(t)h_a^*(t)]
 =-\frac2m\sum_b\int_0^t r_b^*(s)K_{ba,n}(s,t)\,ds.
 \tag{25}
\]

If `|r_b^*(s)|<=C bar_rho(s)`, Cauchy--Schwarz gives its all-time
`L2(bar_rho dt)` norm at most `C sqrt(S) mathcal K_n`. Thus one need
not estimate every readout contraction independently.

The product `L2` covariance norm in (5) does not control a supremum in
the current-time variable. A valid sufficient strengthening can be
stated exactly. Compactify physical time by `x=e^(-kappa t) in [0,1]`.
Suppose the current reference field, as a function `u(x)`, satisfies

\[
 \mathbb E\!\left[
   \|v\|_{L^2(\bar\nu)}^2\|u\|_{H^1([0,1])}^2\right]<\infty.
 \tag{26}
\]

Apply the independent Hilbert-row variance identity to `v tensor u`
in `L2(bar_nu) tensor H1([0,1])`. It yields an `O(n^-1)` squared
error in that stronger norm. The Hilbert-valued one-dimensional
inequality
`sup_x ||F(x)||^2<=C integral (||F||^2+||F'||^2)` follows by the
fundamental theorem and Cauchy--Schwarz. Therefore

\[
 \sup_t\int|K_n(s,t)|^2\bar\nu(ds)
       =O_{\Pr}(n^{-1}),
 \quad
 \sup_{q,t}\|\xi^{n,q}(t)\|=O_{\Pr}(n^{-1/2}).
 \tag{27}
\]

This is still uniform over all admissible random clocks. It requires
the mixed derivative moment (26), which has not been inferred from an
unweighted second-moment speed bound. Differentiating the reference
fields once uses bounded `phi''`, not `phi'''`, but the corresponding
integrability and uniform-in-order bound must still be established.

### The bounded-variation forcing needed by the readout resolvent

This stronger source norm can be derived without taking a supremum of
the covariance kernel. Use the convention

\[
 K_{ab,n}(t,s)=\frac1n\sum_i h_{a,i}^*(t)h_{b,i}^*(s)
                       -\mathbb E[h_a^*(t)h_b^*(s)].
\]

Let `r_b(s)` be any coefficients satisfying
`|r_b(s)|<=sqrt(m) bar_rho(s)`. They may be the actual residuals and
may depend on all reference rows. Define

\[
 D_a(t)=-\frac2m\sum_b\int_0^t K_{ab,n}(t,s)r_b(s)\,ds.
 \tag{27a}
\]

Assume reference forward paths are locally absolutely continuous and
continuous in probability `L2` on each compact time interval, as for the
strong population forward flow. Put
`v_a(t)=dot h_a^*(t)/bar_rho(t)`. It suffices that the following
two deterministic quantities are finite:

\[
 J_0=\sum_{a,b}\int_0^\infty\bar\rho(t)
        \left(\mathbb E|h_a^*(t)h_b^*(t)|^2\right)^{1/2}dt,
\]
\[
 J_1=\sum_{a,b}\int_0^\infty\bar\rho(t)
         \int_0^t\bar\rho(s)
       \left(\mathbb E|v_a(t)h_b^*(s)|^2\right)^{1/2}ds\,dt.
 \tag{27b}
\]

Then the exact root-width estimate is

\[
 D(0)=0,\qquad
 \|\operatorname{TV}_{[0,\infty)}D\|_{L^2(\Pr)}
                \le \frac{C_m(J_0+J_1)}{\sqrt n}.
 \tag{27c}
\]

In particular, a bound uniform in `t,s` on the two mixed moments in
(27b) gives `C(S+S^2)/sqrt(n)`, with the corresponding moment constants.
This is the source norm required by a resolvent estimate of the form
`integral ||Delta r||<=C(||D(0)||+TV(D))`.

For the proof, local absolute continuity, Fubini, and (27b) justify
differentiating the covariance in its first time variable and then the
integral (27a). Almost everywhere,

\[
 \dot D_a(t)=-\frac2m\sum_b
 \left[K_{ab,n}(t,t)r_b(t)
        +\int_0^t\partial_tK_{ab,n}(t,s)r_b(s)\,ds\right].
 \tag{27d}
\]

The normalized derivative covariance error is

\[
 \frac{\partial_tK_{ab,n}(t,s)}{\bar\rho(t)}
 =\frac1n\sum_i v_{a,i}(t)h_{b,i}^*(s)
                              -\mathbb E[v_a(t)h_b^*(s)].
 \tag{27e}
\]

Independent-row variance bounds its probability `L2` norm by
`n^-1/2 (E|v_a(t)h_b^*(s)|^2)^(1/2)`. The same variance calculation
applies to the diagonal kernel with its first mixed moment in (27b).
Bound the coefficients `r` before expectation; then use Minkowski in
the one-time and triangular two-time integrals of (27d). This gives
(27c). No derivative of the residual coefficients is introduced, and
their adaptivity causes no independence error. The integrability also
shows that `D` has finite total variation and a limit at infinity.

The assumed row independence is still that of the reference. Equation
(27c) is not a bounded-variation concentration theorem for actual
trained finite neurons.

The supplied dense population marginal tails verify `J_0<infinity`.
They do not alone verify `J_1`: a marginal `L2` bound on the velocity
and a Gaussian tail for the feature do not control their mixed second
moment. There are two narrower cases where the needed check is direct.
If all forward features in the relevant layer are uniformly bounded,
the population tube and first forward time-derivative recursion give
`||dot h_a^*(t)/bar_rho(t)||2<=C Y`; hence `J_1<infinity` by the
deterministic feature bound. Also, in the first layer,
`dot z_1/rho_*` is a finite deterministic linear combination of the
backward fields `delta_1`; bounded `phi'_1` and the supplied backward
Gaussian tails give all fixed moments of `v_1`. With the supplied
forward tails, Cauchy--Schwarz verifies `J_1` for the first-layer
kernel even when its activation is unbounded. These checks concern
the dense reference only. For higher unbounded layers, or for a new
fixed-order closure reference, the required mixed velocity moment
remains an explicit input to establish.

## 6. The exact initialized-action sources left by the decomposition

Suppose a candidate population closure law has been constructed, with
reference row fields and its own clock measure `nu_*`. Let
`U_{ell,a}^*` and `V_{ell-1,a}^*` denote its full initialized forward
and initialized transpose responses, respectively. These include the
proper reused-matrix response law; they are not asserted to be fresh
independent Gaussians. The population identities have the form

\[
 z_{\ell,a}^*=U_{\ell,a}^*-\mathcal L_{F,\ell,a}^{*,\nu_*},
 \qquad
 p_{\ell-1,a}^*=V_{\ell-1,a}^*
                           -\mathcal L_{B,\ell,a}^{*,\nu_*},
 \tag{28}
\]

where the learned fields include the factor `2/m`.
For a coupling of the actual initialized matrices and the independent
reference row paths, define the two **initialized-action defects**

\[
 A_{F,\ell,a}=W_{\ell,0}h_{\ell-1,a}^*-U_{\ell,a}^*,\qquad
 A_{B,\ell,a}=W_{\ell,0}^T\delta_{\ell,a}^*-V_{\ell-1,a}^*.
 \tag{29}
\]

Then exact subtraction gives

\[
 z_{\ell,a}^n-z_{\ell,a}^*
 =W_{\ell,0}(h_{\ell-1,a}^n-h_{\ell-1,a}^*)+A_{F,\ell,a}
 -[\mathcal L_{F,\ell,a}^{n}-\mathcal L_{F,\ell,a}^{*,\nu_n}]
 -[\mathcal L_{F,\ell,a}^{*,\nu_n}
                         -\mathcal L_{F,\ell,a}^{*,\nu_*}],
\]
\[
 p_{\ell-1,a}^n-p_{\ell-1,a}^*
 =W_{\ell,0}^T(\delta_{\ell,a}^n-\delta_{\ell,a}^*)+A_{B,\ell,a}
 -[\mathcal L_{B,\ell,a}^{n}-\mathcal L_{B,\ell,a}^{*,\nu_n}]
 -[\mathcal L_{B,\ell,a}^{*,\nu_n}
                         -\mathcal L_{B,\ell,a}^{*,\nu_*}].
 \tag{30}
\]

The first terms are controlled by the initialized operator norm and
particle field errors. The first bracket in each line is controlled by
(16)--(17), with order-uniform root-width empirical source. The last
brackets are clock-repacking defects, to be estimated deterministically.
The two defects (29) require a joint quantitative Gaussian-response
coupling. Neither is estimated by the covariance variance identity.

The last bracket in each line of (30) is deliberately left unresolved.
One cannot automatically apply an estimate requiring a history-speed
bound against its own clock to that bracket alone: a reference history
repacked using `nu_n` need not satisfy `||dot h_*||<=C rho_n`.
A valid deterministic proof may instead compare the full actual and
reference reconstructions, each using its own clock, before separating
their empirical source. The random-clock estimate (9) remains valid;
it does not supply this missing deterministic clock comparison.

A natural norm for these remaining sources is

\[
 \mathfrak A_n^2=\sum_{\ell,a}\int_0^\infty\bar\rho(t)
  [\|A_{F,\ell,a}(t)\|_{\rm RMS}^2
                       +\|A_{B,\ell,a}(t)\|_{\rm RMS}^2]dt.
 \tag{31}
\]

For moment differences using the same clock, the exact energy identity
in the assigned route gives

\[
 \frac d{d\tau}(E_H^2+E_B^2)
    \le e_h^2+e_b^2.
 \tag{32}
\]

Thus (17) and (31) are source norms of the correct strength for a
moment-energy comparison. They are not merely errors of individual
moments whose sum could cost `q`. Closing the complete equation also
requires the residual/outer-weight differences, gate products, and the
clock-repacking terms in (30). No order-uniform all-time stability
constant is inferred from (32) alone.

For clarity, pairing an independent population Gaussian output with an
actual matrix output does not solve (29). Even for a deterministic
unit-RMS input to one Gaussian matrix, an independent Gaussian reference
output with the correct marginal law has an order-one RMS difference
from that matrix output. Small empirical covariance error identifies a
law; it is not already a sufficiently strong coupling of the two
forward/transpose actions.

## 7. Why finite moment state does not yet reduce the actual cavity to R2

The Hilbert return theorem in the author's R2 report used independent
Gaussian rows and a rowwise nonlinear response depending on the adaptive
message through `inner_product(g_i,beta)`. Its uniform empirical bound
survived adaptive messages because the independent row structure existed
before their substitution.

The closure's learned branch now has precisely the independent-reference
empirical structure needed for (7)--(17), even after its random clock is
substituted. The outside initialized branch does not acquire that
structure merely from keeping `mq` moments. After deleting one neuron,
the outside current features still interact through the full initialized
matrix and its transpose. An incident Gaussian coordinate changes other
rows' features and moments, which are queried again by those same dense
matrices. The outside response is consequently a coupled vector map of
the whole incident Gaussian row, rather than separate functions of its
individual coordinates and the displayed empirical learned contractions.

Including the current learned contractions among the adaptive messages
does not encode those remaining initialized actions. Equations (29)--(31)
state exactly the missing quantities; calling the whole current outside
trajectory a message would not prove their smallness. The R2 Hilbert
theorem therefore cannot be applied to them without a new factorization
or joint cavity comparison.

## 8. Status

| Statement | Status |
|---|---|
| Random-clock projection bound for all learned contraction coefficients | Exact, (8)--(9) |
| Dimension/order-independent reference covariance variance | Proved under (6), (7) |
| Actual learned-field coupling decomposition without actual iid neurons | Exact, (14)--(17) |
| Deterministic centered moment scales and leading small-label terms | Proved, (18)--(22) |
| Root-width learned stochastic source along arbitrary growing order | Conditional on a correct iid reference with uniform stated moments |
| Uniform current-time source control | Conditional on (26), proved in (27) |
| Readout forcing with root-width total variation | Conditional on the explicit mixed moments (27b), proved in (27c) |
| Simultaneous initialized forward/transpose coupling and clock stability | Unresolved inputs in (29)--(32) |
| Direct all-time closure-to-population width theorem | Not established by this report |

The concrete new contribution is that neither the number of stored
moments nor the dependence of the activity clock on the actual network
causes an empirical loss on the learned branch. The initialized-action
and deterministic clock-comparison obligations remain explicit.

## Source hashes

`DIRECT_CLOSURE_WIDTH_ROUTE.md`:
`485fb66f3b873fad7b642de7b8e5adb1311e79760874bb9edeeb579c72362896`.

`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`:
`0801cb31acd77d8fbd157833090de3f88e5484a23cb471349b6e9c1b7e413bb7`.

`WIDTH_RATE_ACTIVITY_CAVITY_R2.md`:
`580a047a0a6ba6c2b089db780c05a0b237d4436d2ecbabfd99e37f1583165204`.
