# Endpoint projection bounds, exponential fitting, and spectral slack

Scoped analytic continuation, 28 September 2026. Scientific inputs were only
`SMALL_LABEL_ENERGY.md`, `SMALL_LABEL_STRUCTURED.md`,
`SMALL_LABEL_GAUSSIAN.md`, `GENERAL_REFERENCE_PROJECTION.md`, and the canonical
old-clock equations and their complete proof in `paper/main.tex`. The
`solve-math-rigorously` and `investigate-conjectures` skills were applied.
No experiment, external search, other study, Git operation, or further agent
was used. The coordinator independently supplied the same Sonin-energy
argument used for the elementary Legendre estimate below.
The coordinator subsequently read the complete derivation and checked its
terminal cutoff, prefix jump, norms, powers, and expanding-width bound.
The parallel structured route checked the vector endpoint and relative-forcing
arguments in Sections 2--3, then checked the scalar Sonin proof. These are
internal author checks, not a fresh complete independent promotion review.

**Result.** In the existing fixed small-label regime, after reducing its
width-independent label threshold if necessary, the **actual original
old-clock closure** has exponentially decaying residual, uniformly in width
and memory order. Its absolute velocity defect has a stronger all-time bound
than the previously available `C/P` bound:

\[
 \int_0^\infty e_E(t)\,dt
 \le C\left\{
       \frac{B_0Y^{3/2}}{P^{3/2}}
       +\frac{Y^{5/2}\sqrt{1+nY^4+\log(e+P)}}{P^2}
                         \right\}.
 \tag{1}
\]

Here `B_0=||w_0||_2/sqrt(n)<=Y`, `Y=||y||_m`, and constants depend only
on fixed depth, fixed data, the initialized hidden-operator bound, and the
initial readout-Gram gap. In particular they are independent of `n,P,t,Y`
within the chosen small-label range. No regularity of a trained Gaussian
field, normalized-residual limit, terminal eigengap, or residual-ratio
estimate is assumed.

Combining (1) with the already proved activity-weighted stability inequality
gives the following actual autonomous, all-time finite-width theorem:

\[
 \sup_{t\ge0}d_n(\widehat\theta_{n,P}(t),\theta_n^D(t))
 \le C e^{CY+C\sqrt nY^2}
 \left\{
       \frac{B_0Y^{3/2}}{P^{3/2}}
       +\frac{Y^{5/2}\sqrt{1+nY^4+\log(e+P)}}{P^2}
 \right\}.
 \tag{2}
\]

The exponential width factor in (2) is still present. Thus (2) does not
establish the requested arbitrary-depth, multiple-input, all-time,
width-uniform `C/P` trajectory theorem. It does provide explicit spectral
slack, and proves that neither absence of closure exponential fitting nor
an assumed closure backward-history regularity is needed for the stronger
finite-width consistency estimate. Section 7 states exactly what an
order/width partition still lacks.

## 1. Existing all-time inputs and conventions

Use the unchanged tanh network, canonical mobilities, and original autonomous
old clock. A hidden response norm is `||v||_2/sqrt(n)`; a hidden matrix norm
is ordinary Frobenius norm. Write these as `||v||_H` and `||A||_HS` to keep
the projection formulas independent of coordinate normalizations. Pairings
in hidden spaces are `u^Tv/n`, and a rank-one operator is `uv^T/n`.

Fix finite depth and data, and suppose

\[
 \max_{\ell\ge2}\|W_{0,\ell}\|_{\rm op}\le K,
 \qquad B_0\le Y,\qquad
 \Gamma_w(0)=\frac{H_L(0)^TH_L(0)}{mn}\succeq\lambda_0 I_m.
 \tag{3}
\]

The compatible-residual-subspace variant has the same proof with all sample
operators restricted to that subspace. Here the gap is on the full sample
space, so (3) is possible only at appropriate widths, in particular `n>=m`.
The case `Y=0`, hence `B_0=0`, is stationary and needs no estimates below.

The small-label activity theorem, as recorded in `SMALL_LABEL_ENERGY.md`,
already gives global closure existence for every `P>=1`, and

\[
 \int_0^\infty\widehat\rho\,dt\le S=4Y/\lambda_0,
 \quad 1\le\widehat\tau\le A=1+S,
 \quad\widehat\Gamma_w\succeq\lambda_0 I_m/2,
 \tag{4}
\]
\[
 \|\widehat W_\ell\|_{\rm op}\le D_*,\qquad
 \|\widehat w\|_H,\
 \max_a\|\widehat\delta_{\ell,a}\|_H\le C_*Y.
 \tag{5}
\]

The old-clock forward derivative-energy recursion gives, uniformly in its
terminal point,

\[
 Z_\ell(t):=\frac1m\sum_a\int_0^{\widehat\tau(t)}
       \|\partial_\xi\widehat h_{\ell,a}\|_H^2\,d\xi
       \le C_ZY^3.
 \tag{6}
\]

To check the power of `Y` in (6), the first-layer derivative in activity
has norm at most `CY`, and its nonconstant interval has length at most
`S=O(Y)`. Thus `Z_1<=CY^3`. At each higher layer the forward-chain
recursion from the old-clock proof has a source bounded by `CSY^2`,
the preceding `Z` multiplied by bounded operator constants, and a
defect term bounded by `CY^2Z`. Induction through fixed depth proves (6).
This is the earlier squared-defect argument and does not use the new
pointwise estimate proved below.

The exact physical equation and defect are

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,
 \quad E_1=E_w=0,\quad
 E_\ell=\frac{2\widehat\rho}{m}\sum_a
      (b_{\ell,a}-b_{\ell,a}^*)\otimes
      (h_{\ell-1,a}-h_{\ell-1,a}^*),
 \tag{7}
\]

where `b_a=(r_a/rho)delta_a`, a star denotes evaluation at the current
endpoint of the degree-below-`P` history projection, and the backward
prefix is zero. All fields in (4)--(7) are actual closure fields. Put
`e_E=sum_(ell>=2)||E_ell||_HS`.

## 2. Two endpoint bounds, with an elementary proof

Let `L_j` be the ordinary Legendre polynomial on `[-1,1]`, normalized by
`L_j(1)=1`, and put `p_j(u)=L_j(2u-1)`. The endpoint reproducing kernel
on `[0,1]` is

\[
 K_P(u)=\sum_{j<P}(2j+1)p_j(u)
       =\tfrac12\{p'_P(u)+p'_{P-1}(u)\}.
 \tag{8}
\]

The identity follows by summing
`L'_(j+1)-L'_(j-1)=(2j+1)L_j`, with the usual zero negative-index term.
Consequently, for any Hilbert-valued `q in H1(0,tau)`, integration by parts
gives the exact error formula

\[
 q(\tau)-(\Pi_Pq)(\tau)
  =\frac12\int_0^\tau
      [p_P(s/\tau)+p_{P-1}(s/\tau)]q'(s)\,ds.
 \tag{9}
\]

Indeed the bracket divided by two is the integral from zero to `s` of
the rescaled endpoint kernel. Its value is zero at `s=0`, because the two
Legendre endpoint signs cancel, and one at `s=tau`.
Orthogonality and Cauchy--Schwarz imply

\[
 \|q(\tau)-(\Pi_Pq)(\tau)\|_H
 \le\frac{\sqrt\tau}{2}
       \left(\frac1{2P+1}+\frac1{2P-1}\right)^{1/2}
       \|q'\|_{L^2(0,\tau;H)}
 \le C\sqrt{\tau/P}\,\|q'\|_{L^2}.
 \tag{10}
\]

The complementary endpoint estimate is

\[
 \int_0^1|K_P(u)|\,du\le C\sqrt P,
 \qquad
 \|(\Pi_P b)(\tau)\|_H
       \le C\sqrt P\,\|b\|_{L^\infty(0,\tau;H)}.
 \tag{11}
\]

Here is a self-contained justification of the only less immediate part,
the square-root bound. For `j>=1`, write

\[
 v(\theta)=\sqrt{\sin\theta}\,L_j(\cos\theta),\qquad
 q(\theta)=(j+\tfrac12)^2+\frac1{4\sin^2\theta}.
\]

Substitution into the Legendre differential equation gives
`v''+qv=0`. Its Sonin quantity obeys

\[
 \mathcal S=v^2+\frac{(v')^2}{q},\qquad
 \mathcal S'=-\frac{q'}{q^2}(v')^2\ge0
                    \quad(0<\theta\le\pi/2).
 \tag{12}
\]

At the midpoint the explicit values are
`L_(2k)(0)=(-1)^k binom(2k,k)/4^k`, `L_(2k+1)(0)=0`, and
`L'_j(0)=jL_(j-1)(0)`. The elementary inequality
`binom(2k,k)/4^k<=1/sqrt(k+1)` follows by induction: the ratio of
successive left sides is `(2k+1)/(2k+2)`, whose square is at most
`(k+1)/(k+2)`. These formulas give
`S(pi/2)<=2/j`, and therefore throughout the half interval

\[
 |v|\le\sqrt{2/j},\qquad
 |v'|\le\sqrt{2/j}
           \left(j+\tfrac12+\frac1{2\sin\theta}\right).
\]

On `1/j<=theta<=pi/2` this implies

\[
 \left|\frac d{d\theta}L_j(\cos\theta)\right|
 \le\sqrt{2/j}
 \left[\frac{j+1/2}{\sqrt{\sin\theta}}
                    +\frac1{\sin^{3/2}\theta}\right].
 \tag{13}
\]

The first term has integral `O(sqrt(j))`, since
`sin(theta)>=2theta/pi`; the second has integral `O(1)` on this
interval by the same inequality. On `0<=theta<=1/j`, use
`|L'_j(x)|<=j(j+1)/2`. To verify this bound, `|L_k(x)|<=1` follows
from the integral representation

\[
 L_k(\cos\theta)=\frac1\pi\int_0^\pi
       (\cos\theta+i\sin\theta\cos\phi)^k\,d\phi;
\]

the representation follows by expanding in a power-series parameter and
comparing with the generating function `(1-2xt+t^2)^(-1/2)`.
Summing the derivative identity used in (8) then bounds `|L'_j|` by the
sum of `2k+1` over `k=j-1,j-3,...`, which is `j(j+1)/2`.
The variation on this short endpoint interval is consequently at most
`j(j+1)(1-cos(1/j))/2<=1/2`. Parity treats the other half interval.
This proves

\[
 \operatorname{Var}_{[-1,1]}L_j\le C\sqrt j.
\]

Integrating (8) proves (11), including `P=1` directly. The proof applies
to vector-valued histories because the kernel is scalar and integration
uses the triangle inequality for their Hilbert norm.

## 3. A pointwise relative defect and exponential closure fitting

For the normalized residual `c=r/rho`, `||c||_m=1`, so
`|c_a|<=sqrt(m)`. By (5), the backward history, including its zero prefix,
has `sup_xi ||b_(ell,a)(xi)||_H<=C sqrt(m)Y`. Equation (11) gives

\[
 \max_a\|b_{\ell,a}-b_{\ell,a}^*\|_H\le C\sqrt P\,Y.
 \tag{14}
\]

Constants here and below may depend on fixed `m`. By (10) and (6),

\[
 \left(\frac1m\sum_a
       \|h_{\ell-1,a}-h_{\ell-1,a}^*\|_H^2\right)^{1/2}
 \le C\sqrt{A Z_{\ell-1}/P}\le C Y^{3/2}/\sqrt P.
 \tag{15}
\]

The two endpoint factors cancel in (7). The rank-one norm identity and
sample Cauchy--Schwarz therefore prove the new bound

\[
 e_E(t)\le C Y^{5/2}\widehat\rho(t)
                       \qquad(t\ge0,\ n,P\ge1).
 \tag{16}
\]

This uses no backward-history derivative estimate. At a zero residual
the raw algorithm is stationary and (16) follows by continuity.

Let `J` be the prediction differential from the canonical parameter
space to sample RMS. Since the defect has only hidden blocks, (5) gives
`||JE||_m<=CY e_E`. The exact residual equation is

\[
 \dot r=-2\widehat\Gamma r+\widehat J E,
 \quad\widehat\Gamma\succeq\widehat\Gamma_w
                         \succeq\lambda_0I_m/2,
 \quad\|\widehat\Gamma\|_{\rm op}\le G_*.
 \tag{17}
\]

The last bound follows directly from the forward and backward RMS bounds
in the explicit tangent-Gram formula. Taking inner products with `r/rho`
in (17) now gives

\[
 -(2G_*+CY^{7/2})\widehat\rho
       \le\dot{\widehat\rho}
       \le-(\lambda_0-CY^{7/2})\widehat\rho.
 \tag{18}
\]

Reduce the fixed small-label threshold so `CY_*^(7/2)<=lambda_0/2`.
Put `kappa=lambda_0/2` and enlarge a fixed `Lambda` to dominate the
left coefficient. If the initial residual is nonzero, integration proves

\[
 \rho_0e^{-\Lambda t}\le\widehat\rho(t)
       \le\rho_0e^{-\kappa t},\qquad
 \widehat a(t):=\int_t^\infty\widehat\rho(s)\,ds
                  \le\widehat\rho(t)/\kappa.
 \tag{19}
\]

The lower estimate prevents finite-time attainment of zero and validates
the differentiations on every finite interval. The same result is immediate
for a stationary initial residual, with both sides zero. This completes the
uniform exponential fitting claim for the actual closure, for arbitrary
fixed depth and any finite data satisfying the original Gram-gap condition.

## 4. Actual finite-width source regularity without a closure hypothesis

Equation (16) and the exact update formulas yield

\[
 \|\dot W_1\|_{\rm row},\quad
 \sum_{\ell\ge2}\|\dot W_\ell\|_{\rm HS}
       \le CY\rho,
 \qquad\|\dot w\|_H\le2\rho,
 \tag{20}
\]

where `||.||_row=||.||_F/sqrt(n)` and the estimates hold separately
for the first block and the hidden-block sum. The readout also has the
pointwise bound `||dot w||_infinity<=2rho`. Forward differentiation gives

\[
 \max_{\ell,a}\|\dot z_{\ell,a}\|_H,
 \quad\max_{\ell,a}\|\dot h_{\ell,a}\|_H
                            \le CY\rho.
 \tag{21}
\]

For example `dot z_l=dot W_l h_(l-1)+W_l dot h_(l-1)`; (20), bounded
features, and (5) prove (21) by induction. Thus forward histories in the
closure's own clock are in fact uniformly Lipschitz. This is a consequence
of the endpoint calculation, not an input to it.

For a finite width, every full backward carrier has supremum norm at most
`C sqrt(n)Y`, by its RMS bound and the operator norm of the next layer.
Differentiate the exact backward recurrence. The gate derivative term has
RMS at most `2C sqrt(n)Y ||dot z||_H`; the operator derivative term has
RMS at most `||dot W||_op ||delta||_H`; the remaining term is the next
backward derivative multiplied by a bounded operator. At the top layer
start with `dot delta_L=dot w tanh'(z_L)+w tanh''(z_L)dot z_L`.
Using (20)--(21), downward induction proves

\[
 \max_{\ell,a}\|\dot\delta_{\ell,a}\|_H
                   \le C(1+\sqrt nY^2)\rho.
 \tag{22}
\]

This is the sole explicit spatial width loss in the present consistency
argument. It is a proved bound for the actual closure, uniform in `P`.

Equations (16)--(17) give `||dot r||_m<=C rho`, so

\[
 \dot c=\frac{\dot r-c\dot\rho}{\rho},\qquad
 \|\dot c\|_m\le2\|\dot r\|_m/\rho\le C.
 \tag{23}
\]

No terminal convergence of `c` is needed. Differentiate `b_a=c_a delta_a`
and combine (5), (22), (23), and `|c_a|<=sqrt(m)`:

\[
 \left(\frac1m\sum_a\|\dot b_{\ell,a}\|_H^2\right)^{1/2}
       \le C\{Y+(1+\sqrt nY^2)\rho\}.
 \tag{24}
\]

Since `rho_0<=2Y` and (19) holds,

\[
 \frac1m\sum_a\int_0^T\|\dot b_{\ell,a}\|_H^2dt
                  \le CY^2(T+1+nY^4).
 \tag{25}
\]

The term proportional to `T` is deliberate: the bounded direction
derivative (23) need not be square-integrable on the infinite physical
interval. The terminal cutoff below removes that requirement.

## 5. A terminal cutoff gives a near-`P^-1` backward tail

Set `A_infinity=1+integral_0^infinity rho`. For a fixed layer collect
the `m` backward histories in the Hilbert direct sum with norm squared
`m^-1 sum_a ||.||_H²`. Write `b_0=b(1+)`. The initial backward recurrence
and (3) show `||b_0||<=CB_0`. Define

\[
 \widetilde b(\xi)=b(\xi)-b_0\mathbf1_{[1,A_\infty)}(\xi).
 \tag{26}
\]

This history joins continuously to its zero prefix, has norm bounded by
`CY`, and has the same physical derivative as `b` for positive time.
For `T>=0`, let `q_T` agree with `tilde b` through `tau(T)` and be
constant equal to `tilde b(tau(T))` thereafter. On every finite portion
it is an `H1` history. Changing variables, using (19), and then (25),
gives, for every finite endpoint `tau(t)`,

\[
 \begin{split}
 &\int_0^{\tau(t)}\xi(\tau(t)-\xi)\|q_T'(\xi)\|^2d\xi\\
 &\quad\le\int_0^T
       \tau(s)\widehat a(s)\frac{\|\dot b(s)\|^2}{\rho(s)}ds
       \le \frac A\kappa\int_0^T\|\dot b(s)\|^2ds
       \le CY^2(T+1+nY^4).
 \end{split}
 \tag{27}
\]

If `t<T`, only the integral through `t` is needed, and extending the
nonnegative majorant to `T` is valid. If `t>T`, the derivative of `q_T`
is zero afterwards. Its approximation error is supported in a clock
interval of length at most `a(T)`, so

\[
 \|\widetilde b-q_T\|_{L^2(0,\tau(t))}
              \le CY\sqrt{a(T)}
              \le CY^{3/2}e^{-\kappa T/2}.
 \tag{28}
\]

The ordinary weighted Legendre tail inequality applied to (27), best
approximation, and (28) show

\[
 \|(I-\Pi_P)\widetilde b\|_{L^2(0,\tau(t))}
 \le \frac{CY\sqrt{T+1+nY^4}}{\sqrt{P(P+1)}}
                    +CY^{3/2}e^{-\kappa T/2}.
 \tag{29}
\]

The initial step in (26) has tail bounded by `CB_0 sqrt(A/P)`.
For completeness, replace a scalar step by a ramp of width `tau/P`
on whichever side has room, for `P>=2`. Its `L2` error is at most
`sqrt(tau/P)`, and its derivative norm is at most `sqrt(P/tau)`.
Applying the usual `H1` Legendre estimate to the ramp proves the bound;
for `P=1` use projection contraction. Hilbert-valued steps follow by
multiplication by their jump vector.

Choose `T=(2/kappa)log(e+P)`. Since `Y<=1`, (29) and the step bound
give, simultaneously for all physical endpoints,

\[
 \left[\frac1m\sum_a
   \|(I-\Pi_P)b_{\ell,a}\|_{L^2(0,\tau(t);H)}^2\right]^{1/2}
 \le C\left\{\frac{B_0}{\sqrt P}
           +\frac{Y\sqrt{1+nY^4+\log(e+P)}}P\right\}.
 \tag{30}
\]

Every history here is generated by the original autonomous closure in its
own clock. There is no division by another trajectory's residual and no
dense-history replacement. The estimate does not assert a terminal limit
or finite total variation for the normalized residual direction.

## 6. Stronger actual consistency and finite-width tracking

The forward energy (6) and the weighted Legendre inequality give

\[
 \left[\frac1m\sum_a
   \|(I-\Pi_P)h_{\ell-1,a}\|_{L^2(0,\tau(t);H)}^2\right]^{1/2}
                         \le CY^{3/2}/P.
 \tag{31}
\]

The exact growing-history projection-energy identity and (7) imply

\[
 \int_0^t\|E_\ell(s)\|_{\rm HS}ds
 \le\frac2m\sum_a
    \|(I-\Pi_P)b_{\ell,a}\|_{L^2(0,\tau(t);H)}
    \|(I-\Pi_P)h_{\ell-1,a}\|_{L^2(0,\tau(t);H)}.
 \tag{32}
\]

Apply sample Cauchy--Schwarz to (32), then (30)--(31), sum over fixed
depth, and let `t` increase to infinity. Monotone convergence on the
nonnegative left side proves (1). Unlike a signed reconstruction error,
this bounds the total variation of the accumulated defect.

The proved all-time estimate (21)--(23) of `SMALL_LABEL_ENERGY.md` has
the form

\[
 \sup_{t\ge0}d_n(\widehat\theta(t),\theta_D(t))
  \le C\left(\int_0^\infty e_E\right)
                      e^{CY+C\sqrt nY^2}.
 \tag{33}
\]

Its proof only uses an upper bound on the integrated defect and therefore
accepts (1) without changing its carrier estimate. This proves (2).
For zero initial readout, every fixed-width exponent strictly below two
follows from (2). A nonzero initial readout produces the explicit `P^-3/2`
prefix term. Under canonical initialization `B_0<=2/n` holds with
probability tending to one; on the common initialized operator and Gram
events, the corresponding bound holds simultaneously for all `P` and all
time. This statement retains the displayed width factors.

## 7. What spectral slack does and does not settle

There is an exact deterministic consequence for an expanding range of
widths. Let `C_s` be the constant multiplying `sqrt(n)Y²` in (2).
If, for a fixed `alpha<1/2`,

\[
 C_s\sqrt nY^2\le\alpha\log(e+P),
 \tag{34}
\]

then multiplying (2) by `P`, using `B_0<=Y`, and observing
`nY^4<=C log²(e+P)` proves a common bound on `P sup_t d_n`.
Indeed its two order factors are at most a constant times
`P^(-1/2+alpha)` and `P^(-1+alpha)log(e+P)`, respectively, and both
are bounded. At exactly zero readout one may take any `alpha<1`.
For each fixed positive label size, this covers widths proportional to
`log²(e+P)` with an explicit proportionality depending on the fixed
small-label data. It is an improvement over a bounded-width statement.

It does not cover the complementary large-width range. The existing
finite-program transfer supplies a floor `eta_n` tending to zero without
a quantitative relation between `n` and `P`. Even granting an all-time
analogue of the width-first comparison, the schematic estimate

\[
 d_{n,P}\le C P^{-\gamma}
            e^{C\sqrt{\log(e+P)}}+\Psi(\eta_n),
                    \qquad\gamma>1,
 \tag{35}
\]

can complement (34) only if it controls
`P Psi(eta_n)` for every width beyond a constant multiple of `log²P`.
Qualitative convergence does not imply such a bound. For example an
abstract floor `eta_n=1/log(e+n)` still tends to zero, but at
`n=ceil(log²P)` its product with `P` diverges. This diagnoses the
logical use of qualitative transfer; it is not a Gaussian-network
counterexample.

Likewise, exponential decay of both residuals in (19) does not bound their
ratio. Different exponential rates can still make the dense source divided
by the closure residual non-square-integrable in the closure clock. The
proof above avoids that ratio for actual consistency, but (33) still uses
the deterministic initialized-carrier supremum bound and hence its explicit
width factor.

The remaining full-target step is therefore a width-uniform control of the
actual path's gate/carrier correlation in the energy comparison, or a
quantitative finite-array estimate strong enough to cover the complement
of (34). Neither follows from the new spectral slack alone. No replacement
of the target by a width-first limit, prescribed dense forcing, modified
clock, or easier architecture has been made.
