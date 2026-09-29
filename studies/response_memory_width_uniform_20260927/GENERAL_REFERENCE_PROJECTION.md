# General reference-history projection for the autonomous old clock

Frozen independent candidate, 28 September 2026. The scoped inputs were
`OLD_CLOCK_ROUTE.md`, `ENERGY_STABILITY_ROUTE.md`,
`LEARNED_GATE_RESTORATION.md`, the setting and both clock constructions and
proofs in current `paper/main.tex`, and `docs/notation.qmd`. The
`solve-math-rigorously` skill was applied. No other agent's active output,
other study, experiment, or literature search was used before this freeze.

**Result and limit.** For arbitrary fixed depth and arbitrary finite,
possibly correlated data, the dense-history reference can indeed improve
the old clock's consistency from `P^-1` to `P^-3/2`. Only bounded variation
of dense residual-weighted backward sources is needed. The resulting
comparison is an `L1` Volterra inequality; no uniform pointwise bound on a
projected step or projected backward history is required. The apparent
obstacle from those projected steps is removable by an absorbable remainder.
Superexponential-in-cutoff reference tails would then convert this slack
into `C_T/P` tracking. Such trained Gaussian tails and their uniform
finite-width transfer are not consequences of dense existence and ordinary
time regularity. This note therefore does **not** claim the requested full
arbitrary-data Gaussian theorem. It also gives an unconditional width-uniform
old-clock argument for the degenerate case of all labels zero, and a precise
version of the reference comparison allowing a small reference equation
defect.

**Post-freeze update.** Sections 11--14 supersede the need for BV source
regularity when dense Gaussian carrier tails are available. Typed finite
Gaussian-program proxies then prove the old-clock `C_T/P` rate with
width taken first, and in fact every width-first exponent below two.
No trained finite-network tail estimate is assumed. The quantitative
supremum over all finite widths and the general whole-horizon dense
Gaussian-tail theorem remain unresolved.

## 1. Notation and the uniform bounds already available

The activation is tanh, the mobilities and finite arrays are exactly those
of `paper/main.tex`, and the actual closure uses its own gates and its own
old clock. There is no supplied-gate intervention. Write

\[
 a_{\ell,a}=r_a\delta_{\ell,a},\qquad
 d_n(\theta,\vartheta)=\frac{\|W_1-V_1\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_F
       +\frac{\|w-v\|_2}{\sqrt n}.
 \tag{1}
\]

Population versions use row `L2`, hidden Hilbert--Schmidt, and readout
`L2` norms. To write the derivation once, the formulas below use probability
space Hilbert norms and the tensor `u tensor v: g -> u E[v g]`. At finite
width these mean respectively `||u||_2/sqrt(n)` and `uv^T/n`; the hidden
Hilbert--Schmidt norm is the ordinary Frobenius norm. Thus no factor of
width is hidden in the final distance (1).

Fix a physical horizon `T` and common bounds on initial hidden operator
norms and initial readout RMS. The proved old-clock bounds give constants
`Q,A,K_l,beta_l,Z_l,C_comp`, independent of `n,P`, with

\[
 \widehat\rho,\rho_D\le Q,\quad 1\le\widehat\tau\le A,
 \quad\|\widehat W_\ell\|_{\rm op},\|W_\ell^D\|_{\rm op}\le K_\ell,
 \quad\|\widehat\delta_{\ell,a}\|_2,\|\delta^D_{\ell,a}\|_2\le\beta_\ell,
 \tag{2}
\]
\[
 \sum_a\int_0^{\widehat\tau}
       \|\partial_\xi\widehat h_{\ell,a}\|_2^2d\xi\le mZ_\ell,
 \qquad
 \int_0^T\sum_{\ell=2}^L\|E_\ell\|_{\rm HS}dt\le C_{\rm comp}/P.
 \tag{3}
\]

The actual closure exists at every finite width for every `P`. The proof
of (2)--(3) does not use stability or backward-history regularity. All
arguments below concern that actual closure.

There are width-independent forward constants `U_l` such that

\[
 \|\widehat z_{\ell,a}-z^D_{\ell,a}\|_2,
 \|\widehat h_{\ell,a}-h^D_{\ell,a}\|_2\le U_\ell d_n,
 \quad U_1=X,\quad U_\ell=1+K_\ell U_{\ell-1},
 \tag{4}
\]

where `X=max_a ||x_a||/sqrt(d)`. In particular the sample residual RMS
difference is at most `C_f d_n`, with `C_f=1+B U_L` and `B` a readout
RMS bound. The same differentiation, applied to a tangent vector at any
state obeying (2), gives `||Dr[v]||_(sample RMS)<=C_f ||v||_sum`.
The velocity formulas give `||F||_sum<=V rho`, where

\[
 V=2\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].
 \tag{5}
\]

Consequently, if `rho_D(0)>0`, then

\[
 \rho_D(t)\ge\rho_D(0)e^{-C_fVT}=:\mu>0.
 \tag{6}
\]

Indeed `|dot rho_D|<=||dot r_D||_(sample RMS)<=C_f V rho_D`, and
integration of the logarithmic inequality gives (6). It uses no lower
bound on an input Gram eigenvalue and no fitting assumption. Stop the
comparison while `d_n<=mu/(2C_f)`; (4) then gives
`widehat rho>=mu/2`. This is a provisional first-exit condition, not an
assumed global lower bound on the closure residual.

If at least one fixed label is nonzero, let
`Y=(m^-1 sum y_a^2)^(1/2)>0`. Since `||f(0)||_(sample RMS)<=R_0`,
the event `R_0<=Y/2` gives `rho_D(0)>=Y/2`. Canonical small readout has
`R_0=||w_0||_2/sqrt(n)->0`, so this supplies a uniform `mu` for large
widths on the common initial bounds. Section 8 treats `Y=0` separately.

## 2. Two elementary projection facts

For the ordinary `L2(0,tau)` projection `Pi_P` onto degree below `P`,
the existing Legendre estimate is

\[
 \|(I-\Pi_P)q\|_{L^2}\le
       \frac{\tau}{2\sqrt{P(P+1)}}\|q'\|_{L^2}.
 \tag{7}
\]

The following step bound avoids a special-function asymptotic. For every
`s in [0,tau]`,

\[
 \|(I-\Pi_P)\mathbf1_{[s,\tau]}\|_{L^2(0,\tau)}
       \le C\sqrt{\tau/P}.
 \tag{8}
\]

For `P=1` this is contraction. For `P>=2`, replace the step by a linear
ramp across the intersection with `[0,tau]` of an interval of length at
most `2 tau/P` about `s`, choosing the ramp on one side if needed near
an endpoint. One can choose a ramp `v` with
`||v-step||_2^2<=2 tau/P` and `||v'||_2^2<=P/tau` (a one-sided ramp of
width `tau/P` suffices whenever that side has room). Best approximation,
the triangle inequality and (7) give (8), with an absolute constant.

If a Hilbert-valued history is absolutely continuous except for finitely
many jumps, write it as a constant plus its jumps times scalar steps plus
the integral of `q'(s) 1_[s,tau]`. Minkowski's inequality and (8) yield

\[
 \|(I-\Pi_P)q\|_{L^2}\le
       C\sqrt{\tau/P}\operatorname{Var}(q).
 \tag{9}
\]

Here variation includes all jumps. The same statement for Hilbert-valued
bounded-variation histories follows by replacing the derivative and jump
sum by their finite vector measure. Only the absolutely continuous plus
one-prefix-jump case is needed below.

We also use the proved bound from `OLD_CLOCK_ROUTE.md`, valid for
Hilbert-valued `H1` histories:

\[
 \|\Pi_Pq\|_{L^\infty(0,\tau;H)}
 \le\tau^{-1/2}\|q\|_{L^2}+C\tau^{1/2}\|q'\|_{L^2}.
 \tag{10}
\]

Its constant is independent of `P`, including evaluation at an endpoint.
Applied to the actual closure's forward histories, (2)--(3) give
`sup_xi ||Pi_P widehat h_(l,a)(xi)||_2<=M_h`, uniformly in `P,n`.
No backward projection is covered or assumed by (10).

## 3. Dense histories reparameterized by the actual closure clock

On the stopped interval let `t=t(xi)` invert the closure clock. Define

\[
 H_{\ell,a}(\xi)=h^D_{\ell,a}(t(\xi)),\qquad
 B_{\ell,a}(\xi)=
       \frac{a^D_{\ell,a}(t(\xi))}{\widehat\rho(t(\xi))}
       \quad(\xi>1).
 \tag{11}
\]

The forward prefix is its common initial value; the backward prefix is
zero, exactly as in the actual old-clock system. Since
`d xi=widehat rho dt`,

\[
 A^D_\ell(t):=W^D_\ell(t)-W_{0,\ell}
   =-\frac2m\sum_a\int_0^{\widehat\tau(t)}
             B_{\ell,a}\otimes H_{\ell-1,a}\,d\xi.
 \tag{12}
\]

This is an identity even though the dense and closure clocks differ.
The reference reconstruction

\[
 A^{\mathrm{ref},P}_\ell
  =-\frac2m\sum_a\int_0^{\widehat\tau}
       (\Pi_P B_{\ell,a})\otimes(\Pi_P H_{\ell-1,a})\,d\xi
 \tag{13}
\]

is proof-only; it is not a new algorithm.

The dense forward derivatives are bounded from (2),(5) and the usual
forward chain rule. Thus, because `widehat rho>=mu/2`,

\[
 \int_0^{\widehat\tau}\|H'_{\ell,a}\|_2^2d\xi
   =\int_0^t\frac{\|\dot h^D_{\ell,a}\|_2^2}{\widehat\rho}ds
   \le C_{T,\mu}.
 \tag{14}
\]

The minimal additional time regularity used in the present argument is

\[
 \sum_{\ell,a}\left(
    \sup_{s\le T}\|a^D_{\ell,a}(s)\|_2
       +\int_0^T\|\dot a^D_{\ell,a}(s)\|_2ds\right)\le M_a.
 \tag{15}
\]

This is `W^(1,1)` regularity of the dense residual-weighted backward
sources, with a width-independent constant if a family of finite dense
networks is being considered. At one population, `C1` regularity of the
source on a compact time interval implies (15). Mere existence or `C0`
regularity does not.

The closure residual has uniformly bounded total variation without any
backward derivative estimate:

\[
 \operatorname{Var}(\widehat\rho)
   \le C_f\int_0^T\|\dot{\widehat\theta}\|_{\rm sum}ds
   \le C_f(VQT+C_{\rm comp}).
 \tag{16}
\]

Using the quotient rule only for the scalar denominator,

\[
 \operatorname{Var}(B_{\ell,a})
 \le\frac{2\|a^D_{\ell,a}(0)\|_2}{\mu}
  +\frac2\mu\int_0^T\|\dot a^D_{\ell,a}\|_2ds
  +\frac4{\mu^2}\sup_s\|a^D_{\ell,a}(s)\|_2
                       \operatorname{Var}(\widehat\rho)
 \le C_{T,\mu,M_a}.
 \tag{17}
\]

Variation is invariant under the increasing reparameterization; the
first term covers the zero-prefix jump. Therefore (7),(9),(14),(17)
give, separately for every finite sample and layer,

\[
 \|(I-\Pi_P)H\|_{L^2}\le C/P,
 \qquad \|(I-\Pi_P)B\|_{L^2}\le C/P^{1/2}.
 \tag{18}
\]

Orthogonality eliminates the mixed projection terms in (12)--(13):

\[
 A^{\mathrm{ref},P}_\ell-A^D_\ell
 =\frac2m\sum_a\int
       ((I-\Pi_P)B_{\ell,a})\otimes
       ((I-\Pi_P)H_{\ell-1,a})\,d\xi.
 \tag{19}
\]

The rank-one Hilbert--Schmidt norm identity and Cauchy--Schwarz prove

\[
 \sup_{t\le T}\sum_{\ell=2}^L
       \|A^{\mathrm{ref},P}_\ell-A^D_\ell\|_{\rm HS}
       \le C_{T,\mu,M_a}P^{-3/2}.
 \tag{20}
\]

The signs are retained in (19); this is not an estimate of the actual
closure's accumulated absolute velocity defect. It is stronger precisely
because it compares against regular prescribed dense histories.

If additionally the dense sources are `H1` in physical time, then the
old-clock squared-defect estimate implies a uniform `L2` bound on
`dot widehat rho`; applying the quotient rule gives an `H1` bound on
the non-prefix part of `B`. Consequently (18) improves to

\[
 \|(I-\Pi_P)B\|_{L^2}\le C\left(P^{-1}
                                  +\|B(1+)\|_2P^{-1/2}\right).
 \tag{21}
\]

At exactly zero initialized readout all initialized backward sources are
zero, so `B(1+)=0` and (20) improves to `C P^-2`. Canonical finite small
readout instead contributes a jump bounded by `C R_0`, giving
`C(P^-2+R_0 P^-3/2)`. This sharpening is optional; (20) already has the
slack needed for an old-clock endpoint rate under the tail condition below.

## 4. Removing the projected-backward-history obstacle

Write `widehat b=widehat a/widehat rho` in the closure clock and set
`Delta h=widehat h-H`, `Delta b=widehat b-B`. The prefixes agree.
The exact reconstruction difference can be split as

\[
 \begin{split}
 &\int (\Pi_P\widehat b)\otimes(\Pi_P\widehat h)
           -(\Pi_P B)\otimes(\Pi_P H)\,d\xi\\
 &\quad=\int\Delta b\otimes(\Pi_P\widehat h)\,d\xi
            +\int B\otimes\Delta h\,d\xi
            -\int (I-\Pi_P)B\otimes(I-\Pi_P)\Delta h\,d\xi.
 \end{split}
 \tag{22}
\]

For the first term, (10) and the clock substitution cancel its denominator:

\[
 \left\|\int\Delta b\otimes(\Pi_P\widehat h)d\xi\right\|_{\rm HS}
 \le M_h\int_0^t\|\widehat a(s)-a^D(s)\|_2ds.
 \tag{23}
\]

For the second term, use `||a_D||_2<=C` and (4):

\[
 \left\|\int B\otimes\Delta h\,d\xi\right\|_{\rm HS}
 \le C\int_0^t d_n(s)ds.
 \tag{24}
\]

For the last term, contraction, (18), and (4) give

\[
 \begin{split}
 \left\|\int (I-\Pi_P)B\otimes(I-\Pi_P)\Delta h\,d\xi\right\|_{\rm HS}
 &\le C P^{-1/2}
       \left(\int_0^t\widehat\rho(s)d_n(s)^2ds\right)^{1/2}\\
 &\le C\sqrt{QT}\,P^{-1/2}\sup_{s\le t}d_n(s).
 \end{split}
 \tag{25}
\]

Thus no uniform `L-infinity` projection bound for `B`, its prefix step,
or `widehat b` appears. The potentially dangerous backward-projection term
is an explicitly vanishing multiple of the same supremum error and can
be absorbed. This is the main technical improvement over the earlier
uncompleted reference projection proposal.

## 5. Exact arbitrary-depth, arbitrary-data feedback algebra

The only remaining non-Lipschitz quantities are initialized carriers along
the reference:

\[
 k_{L,a}=w_0,\qquad
 k_{\ell,a}=W_{0,\ell+1}^*\delta^D_{\ell+1,a}\quad(\ell<L),
 \qquad
 H(M)=\sum_\ell\max_a\sup_{t\le T}
         \|k_{\ell,a}\mathbf1_{|k_{\ell,a}|>M}\|_2.
 \tag{26}
\]

The exact dense history gives
`||(A_(l+1)^D)^*delta_(l+1,a)^D||_infinity<=2S beta_(l+1)^2`
and `||w_D-w_0||_infinity<=2S`, where `S=QT`. Subtracting the full
autonomous backward recurrences gives

\[
 \begin{split}
 \widehat\delta_\ell-\delta^D_\ell={}&
  \widehat D_\ell\widehat W_{\ell+1}^*
          (\widehat\delta_{\ell+1}-\delta^D_{\ell+1})
 +\widehat D_\ell(\widehat A_{\ell+1}-A^D_{\ell+1})^*
          \delta^D_{\ell+1}\\
 &+(\widehat D_\ell-D^D_\ell)(A^D_{\ell+1})^*
          \delta^D_{\ell+1}
 + (\widehat D_\ell-D^D_\ell)k_\ell,
 \end{split}
 \tag{27}
\]

with the analogous top identity obtained by splitting `w_D=w_0+(w_D-w_0)`.
Since `|tanh'(u)-tanh'(v)|<=min(2|u-v|,1)`,

\[
 \|(\widehat D_\ell-D^D_\ell)k_\ell\|_2
 \le 2M U_\ell d_n+
       \|k_\ell\mathbf1_{|k_\ell|>M}\|_2.
 \tag{28}
\]

Descending through (27), all propagation coefficients are bounded hidden
operator norms; the `M` terms are added at each layer. Consequently

\[
 \max_{\ell,a}\|\widehat\delta_{\ell,a}-\delta^D_{\ell,a}\|_2
  +\max_{\ell,a}\|\widehat a_{\ell,a}-a^D_{\ell,a}\|_2
 \le C\big[(1+M)d_n+H(M)\big].
 \tag{29}
\]

The source bound follows by writing
`widehat r widehat delta-r_D delta_D =
widehat r (widehat delta-delta_D)+(widehat r-r_D)delta_D`, using (2),(4)
and the finite sample count. The coefficient of `M` is affine at every
fixed depth; there is no `M^L` loss and no input-Gram inverse.

Put

\[
 \omega(u)=C\left[u+\inf_{M\ge1}\{Mu+H(M)\}\right].
 \tag{30}
\]

It is increasing and concave. Comparing the unchanged first-layer and
readout integrals uses (29),(4); comparing hidden reconstructions uses
(20),(22)--(25),(29). With `D(t)=sup_(s<=t)d_n(s)`, one obtains

\[
 D(t)\le C P^{-3/2}
        +C P^{-1/2}D(t)+\int_0^t\omega(D(s))ds.
 \tag{31}
\]

To justify the supremum, each earlier-time inequality is bounded by its
right side with the integral extended to `t`, since all terms are
nonnegative and `omega` is increasing. For `P` exceeding the fixed
threshold with `CP^-1/2<=1/2`, absorption yields

\[
 D(t)\le C P^{-3/2}+2\int_0^t\omega(D(s))ds.
 \tag{32}
\]

This is the promised general-data, general-depth, one-reference `L1`
comparison. It does not square the modulus and does not assume a
Lipschitz stability theorem.

## 6. What would close the endpoint, and what the dense premise supplies

Suppose the reference carriers satisfy the extra quantitative bound

\[
 H(M)\le B e^{-cM^\alpha},\qquad \alpha>1.
 \tag{33}
\]

Then choosing `M` proportional to `log(A/u)^(1/alpha)` in (30) gives
`omega(u)<=C u log(A/u)^(1/alpha)` for small `u`. The elementary scalar
comparison for (32), setting `z=log(A/v)` in
`v'=2 omega(v)`, gives

\[
 D(T)\le C P^{-3/2}
          \exp\{C_T(\log P)^{1/\alpha}\}
       \le C_T/P.
 \tag{34}
\]

The last inequality follows because
`C_T (log P)^(1/alpha)-(1/2)log P` has a finite supremum on `P>=1`.
For large `P`, (34) is below `mu/(2C_f)`, so the provisional stopping
condition is removed by first exit. Remaining bounded orders can be
covered by the global parameter increment bounds (2). At zero initial
readout with `H1` sources, replace `P^-3/2` in (34) by `P^-2`; this
still does not give an exact `P^-2` conclusion under a non-Lipschitz
modulus.

Condition (33) is a trained dense-reference tail assertion. It is not a
closure-stability assertion, but it remains a substantive extra statement
about the Gaussian neural dynamics. A smooth path with all finite moments
can have `k(s)=[log(1/s)]^p` on `(0,1)` for any `p>1`; its tail is only of
order `exp(-c M^(1/p))`. Multiplying a bounded gate discrepancy supported
on `(0,epsilon)` by this field gives a norm at least
`c ||Delta z||_2 log(1/||Delta z||_2)^p`. Thus neither arbitrarily smooth
time paths nor all finite moments imply the required modulus. This is a
diagnostic of the analytic implication, not a Gaussian-network
counterexample.

Moreover, differentiating the dense backward recursion produces
`tanh''(z) dot z (W_0^*delta)` and similar products. Bounded operator
norms and `L2` dense trajectories do not by themselves imply (15).
Explicit `C1` or `W^(1,1)` source regularity would be an appropriate
dense regularity premise for this approximation step. It supplies no
quantitative bound like (33).

## 7. Finite-width transfer and its error floor

A regular population reference alone does not make (15),(33) uniform
for finite dense trajectories. Convergence of predictions is weaker than
convergence of the initialized carriers. Even strong uniform-in-time
`L2` carrier convergence only yields the following bound. If on compatible
probability spaces

\[
 \max_{\ell,a}\sup_{t\le T}
     \|k^n_{\ell,a}-k^\infty_{\ell,a}\|_2\le\eta_n,
 \tag{35}
\]

then a truncation at `M/2` gives

\[
 H_n(M)\le C\eta_n+H_\infty(M/2).
 \tag{36}
\]

For one field, split according to `|k_infinity|>M/2`. On its complement,
`|k_n|>M` implies `|k_n-k_infinity|>M/2>=|k_infinity|`; the triangle
inequality therefore bounds this part by twice the `L2` difference.
This proves (36). The additive `eta_n` is not an exponential tail bound
for arbitrarily large `M`.

If source variation bounds have also transferred, (32) becomes

\[
 D_n(t)\le C(P^{-3/2}+\eta_n)
       +C\int_0^t D_n(s)
           [\log(A/D_n(s))]^{1/\alpha}ds.
 \tag{37}
\]

Writing
`Phi_T(epsilon)=C epsilon exp(C_T log(A/epsilon)^(1/alpha))`, with a
bounded extension away from zero, gives

\[
 D_n(T)\le\Phi_T(P^{-3/2}+\eta_n)
       \le C_T/P+C_T\Phi_T(\eta_n).
 \tag{38}
\]

For the last bound, distinguish which of the two arguments is larger
and absorb the factor two into the constants. Thus the method has an
amplified finite-width floor, rather than automatically preserving a
given population-approximation rate. Taking `n->infinity` first removes
that floor, giving an endpoint bound for the limit superior. It does
not establish `sup_n P D_n(T)<infinity`.

Uniform `C0` source convergence also does not transfer variation bounds:
the scalar functions `n^-1 sin(n^2 t)` converge uniformly to zero while
their total variations grow. A finite-width transfer of (15) needs
additional information or a reference construction with uniformly
controlled source variation. One cannot silently replace population
`C1` regularity by finite-network `C1` bounds.

## 8. All-zero labels: a complete autonomous old-clock estimate

The residual-floor issue when `Y=0` has a separate direct resolution for
canonical small readout; it need not be declared a missing hypothesis.
The unchanged readout equation gives

\[
 \frac d{dt}\|\widehat w(t)\|_2^2=-4n\widehat\rho(t)^2\le0,
 \qquad \|w_D(t)\|_2\le\|w_0\|_2.
 \tag{39}
\]

Here the displayed readout norms are ordinary finite Euclidean norms.
Let `R=||w_0||_2/sqrt(n)`. In (2), every backward RMS bound has the form
`beta_l=R c_l`, with `c_l` bounded by a fixed recursion involving
`T,R` and the initialized hidden operator bounds. Therefore the dense
initialized carriers obey actual coordinatewise bounds

\[
 \|k_{\ell,a}\|_\infty
 \le\|W_{0,\ell+1}\|_{\rm op}\|\delta^D_{\ell+1,a}\|_2
 \le K_{0,\ell+1}c_{\ell+1}\|w_0\|_2
 \quad(\ell<L),
 \qquad\|w_0\|_\infty\le\|w_0\|_2.
 \tag{40}
\]

The middle norm in (40) is again ordinary Euclidean. It is bounded
uniformly in width on an event `||w_0||_2<=M_0`, rather than on an event
bounding only its RMS. Under stored `N(0,n^-2)` readout,
`E||w_0||_2^2=1/n`, so this is a natural uniformly probable bound.

Use (40) directly in the exact subtraction (27). All gate multipliers
are now bounded, giving
`||F(widehat theta)-F(theta_D)||_sum<=L_T d_n`, with `L_T` independent
of `n,P` on the initial bounds. The actual defect estimate (3), followed
by the scalar integrating factor, proves

\[
 \sup_{t\le T}d_n(\widehat\theta_P,\theta_D)
       \le C_{\rm comp}e^{L_TT}/P.
 \tag{41}
\]

This uses the actual autonomous closure, all samples, any fixed depth,
and arbitrary inputs, with no dense-tail premise, residual lower bound,
or prescribed gates. If `w_0=0` exactly, both flows are stationary.
The eventwise constants do not automatically prove any particular
moment bound on `exp(L_TT)`; expectation claims need a separate
integrability argument. This special label case is included only to
close the residual-floor edge case, not as a replacement for general data.

## 9. An approximate reference and a fixed-mesh proxy

The reference need not solve the dense ODE exactly. Suppose a bounded
reference path `theta_R` has the same initialized matrices, its forward
histories have a common physical-time `H1` bound, and it obeys

\[
 \dot\theta_R=F(\theta_R)+R(t),\qquad
 \int_0^T\|R(t)\|_{\rm sum}dt\le\eta.
 \tag{42}
\]

The reference hidden history identity (12) then has an additional
matrix `J_l(t)=integral_0^t R_l(s)ds`, whose Hilbert--Schmidt norm is
at most `eta`. Accordingly (20) becomes `C P^-3/2+eta`.
The first-layer and readout integral comparisons likewise acquire at
most `eta`.

There is one extra point in the backward comparison: a small
Hilbert--Schmidt reference defect does not have a bounded pointwise
adjoint output. Split the learned reference carrier as

\[
 (A_{\ell+1}^R)^*\delta^R_{\ell+1,a}
  =\left(-\frac2m\sum_b\int
        a^R_{\ell+1,b}\otimes h^R_{\ell,b}\,ds\right)^*
           \delta^R_{\ell+1,a}
       +J_{\ell+1}^*\delta^R_{\ell+1,a}.
 \tag{43}
\]

The first term is pointwise bounded by the same learned-history
calculation as before. For the second, the bounded gate difference gives

\[
 \|(\widehat D-D^R)J_{\ell+1}^*\delta^R_{\ell+1,a}\|_2
       \le\|J_{\ell+1}\|_{\rm HS}\|\delta^R_{\ell+1,a}\|_2
       \le C\eta.
 \tag{44}
\]

At the top, a readout equation defect is handled the same way, with
an additive `C eta`, rather than falsely calling the readout remainder
pointwise bounded. Thus the reference-tail modulus gains an additive
`C eta`, and (32) becomes

\[
 D(t)\le C(P^{-3/2}+\eta)+C\int_0^t\omega(D(s))ds.
 \tag{45}
\]

If (15) and the quantitative reference tails hold with constants uniform
over the references, this gives `C/P+C Phi_T(eta)`, with precisely the
same amplification floor as (38). A positive reference residual lower
bound can be imposed by closeness to the dense reference using (4), or
derived from (42) when its accumulated forcing is small relative to the
dense residual floor.

For a fixed-mesh construction, the source-variation constant must be
audited rather than inferred from a small equation defect. The useful
stronger formulation permits **prescribed proxy histories** `H,a` in
(12), with small algebraic mismatches from the responses recomputed at
`theta_R`. A uniform bound on `H` and its `H1` seminorm and on the
variation of `a`, together with integrably small source mismatches and
small integral-equation defects, produces (45) with those mismatch
integrals added to `eta`. In (23) split
`widehat a-a=(widehat a-a(theta_R))+(a(theta_R)-a)`; in (24) use the
corresponding split for `H`. A prescribed forward mismatch in the
remainder (25) contributes `C P^-1/2 ||H-h(theta_R)||_(L2(time;L2))`.
This last norm must be small as well, or follows from bounded responses
and an `L1` mismatch by Cauchy--Schwarz. The carrier-tail estimate must
refer to actual or consistently approximated reference backward fields;
it is not supplied by the scalar predictor error.

Piecewise linear interpolation of a given `H1` dense history has a
uniform `H1` seminorm: on `[t_j,t_(j+1)]`, Jensen gives
`||[H(t_(j+1))-H(t_j)]/(t_(j+1)-t_j)||^2`
at most the interval average of `||dot H||^2`. Summing proves the
claim. Piecewise constant or linear interpolation of a dense bounded-
variation backward source has variation at most the dense variation.
These facts can keep the approximation constants uniform in the mesh
without differentiating a trained finite network. Transferring their
finite list of same-array observations still requires the relevant
finite-width coupling theorem. Qualitative convergence of each fixed
mesh, followed by mesh refinement, can give qualitative uniform
convergence; an endpoint bound uniform over **all** widths additionally
needs quantitative control of the mesh/width/order interaction.

## 10. Why this does not establish the joint-clock endpoint

The original joint clock is `g=widehat rho+||dot widehat Psi||_2`,
with its original unnormalized concatenated finite-coordinate norm.
Its projection measure is `widehat rho dt` on physical history and
Lebesgue measure on the matching prefix. Dense histories placed at
the closure's clock can again reproduce exact dense learned matrices
using `a_D/widehat rho` and the corresponding prefix subtraction.
The projection-product identity remains valid for the weighted projector.

However, three needed old-clock ingredients do not transfer for free:

1. A width-uniform bound on the original joint clock is not implied by
   (2). The unnormalized response path can have speed proportional to
   `sqrt(n)`, and its backward derivative also contains the same
   unbounded gate carriers. Rescaling this clock would change the
   algorithm.
2. The weighted polynomial projector need not satisfy the uniform
   `H1 -> L-infinity` bound (10) under only domination of its measure by
   Lebesgue measure. Prefix positivity proves invertibility at fixed
   `P`, not an order-uniform projection norm.
3. Even if both reference histories had `H1` regularity in a bounded
   clock, the product gives `P^-2`. A non-Lipschitz modulus amplifies
   that by a subpower factor; the exact joint `C/P^2` target requires
   additional approximation slack, or stronger stability. Smooth dense
   time histories alone do not give extra regularity after composing
   with the actual joint clock, whose higher derivatives are not
   controlled by dense regularity.

Therefore the completed analytic advance here is the general old-clock
reference inequality (32), its source-regularity threshold, its
approximate-reference extension (45), and the zero-label result (41).
The full general-data endpoint theorem still needs a proved quantitative
Gaussian-reference regularity/tail and transfer mechanism, or a different
argument using correlations of the actual projection error.

## 11. Post-freeze combination: dense tails imply enough time regularity

After freezing Sections 1--10, the coordinator supplied the half-Hölder
regularity reduction below. I read the completed
`GENERAL_GAUSSIAN_TRANSPORT.md` and the complete maintained proof units
C.1 of `docs/03-local-population.qmd` (lines 56--555) and A.1--A.2 of
`docs/02-gaussian-reuse.qmd` (lines 1803--1834). The following argument
replaces the extra BV premise in the original frozen candidate. It is
a width-first endpoint theorem, not an all-width endpoint theorem.

Assume the strong canonical dense population flow exists on `[0,T]`
from zero limiting readout and its full backward carriers satisfy

\[
 \sup_{t\le T}\max_{\ell,a}
       \mathbb E_\ell e^{c|c^D_{\ell,a}(t)|^2}\le C,
 \quad c^D_{L,a}=w_D,\quad
 c^D_{\ell,a}=(W^D_{\ell+1})^*\delta^D_{\ell+1,a}.
 \tag{46}
\]

The maintained C.1--C.2 provide a verified local source-tail mechanism;
an extension of (46) to arbitrary prescribed `T` remains a dense-only
regularity premise. This section does not prove that extension.

The dense parameter velocity is bounded in the sum norm (1), by (2),(5)
and the rank-one Hilbert--Schmidt identity. In particular
`d(theta_D(t),theta_D(s))<=C|t-s|`. Apply the exact backward subtraction
at these two dense states, with the state at `s` as the reference. The
cutoff inequality and (46) give

\[
 \|\delta^D_{\ell,a}(t)-\delta^D_{\ell,a}(s)\|_2
 \le C[(1+M)|t-s|+e^{-c'M^2}],\qquad M\ge1.
 \tag{47}
\]

Since the residuals are Lipschitz in physical time, the same bound holds
for `a_D=r_D delta_D`. For `0<h=|t-s|<=1/2`, choose
`M=max(1,sqrt(log(1/h)/(2c')))`. Then `e^(-c'M²)<=C sqrt(h)` and
`h(1+sqrt(log(1/h)))<=C sqrt(h)`. Larger `h` are covered by bounded
source norms. Therefore

\[
 \|a^D_{\ell,a}(t)-a^D_{\ell,a}(s)\|_2\le C_T|t-s|^{1/2}.
 \tag{48}
\]

The same proof gives every exponent strictly below one, but one-half
already provides the needed slack. This derivation needs no source time
derivative or product of two unbounded derivative fields.

The actual old closure's residual also has a uniform half-Hölder bound.
The old squared-defect estimate gives

\[
 \int_0^T\|E(t)\|_{\rm sum}^2dt
 \le (L-1)Q\sum_{\ell=2}^L
            \int_0^T\widehat\rho\|E_\ell/\widehat\rho\|_{\rm HS}^2dt
 \le C_T.
 \tag{49}
\]

Together with `||F||_sum<=VQ`, this bounds
`integral ||dot widehat theta||_sum²` independently of order and width.
The norm map is Lipschitz, so almost everywhere, including any zero
residual times, `|dot widehat rho|<=C_f ||dot widehat theta||_sum`.
Thus

\[
 |\widehat\rho(t)-\widehat\rho(s)|\le C_T|t-s|^{1/2}.
 \tag{50}
\]

On the residual bootstrap, a bounded half-Hölder source `a` therefore
makes `a/widehat rho` half-Hölder in physical time. The inverse closure
clock is Lipschitz with constant `2/mu`, so it is half-Hölder in `xi`
as well. The zero backward prefix either matches its initial value or
adds one jump; both cases have a `P^-1/2` projection tail.

Here is the needed elementary polynomial estimate. If a Hilbert-valued
`q` on `[0,tau]` has Hölder exponent `gamma in (0,1]` and constant `K`,
let `v` interpolate it linearly at `P+1` equally spaced nodes. Then

\[
 \|q-v\|_{L^2}\le 2K\tau^{\gamma+1/2}P^{-\gamma},\qquad
 \|v'\|_{L^2}\le K\tau^{\gamma-1/2}P^{1-\gamma}.
 \tag{51}
\]

The first inequality follows cellwise from the Hölder bound; the
second sums the squared difference quotients over the `P` cells.
Apply (7) to `v`, then best approximation and the triangle inequality:

\[
 \|(I-\Pi_P)q\|_{L^2}
       \le C K\tau^{\gamma+1/2}P^{-\gamma}.
 \tag{52}
\]

Constants in `q` are represented exactly. If there is a prefix jump,
subtract its step and apply (8) as well. With `gamma=1/2`, (52)
supplies exactly the backward tail in (18), with no BV assumption.
All the algebra (19)--(32) remains valid.

## 12. Constructing finite same-array reference histories from dense samples

The following construction avoids transferring derivatives or tails of
actual trained finite networks. It uses only fixed finite Gaussian
program convergence and dense (46).

### 12.1. Typed program approximants of sampled sources and features

Take a uniform time mesh `t_j=j Delta`, `j=0,...,N`, with `N Delta=T`.
The canonical population spaces in maintained C.1 are the `L2` closures
of a countable family of finite Gaussian programs and their finite
unions, retaining each initialized matrix and its true adjoint. For any
`epsilon>0`, choose finite program nodes

\[
 H^\epsilon_{\ell,a,j}\in L^2(\Omega_\ell),\qquad
 A^\epsilon_{\ell,a,j}\in L^2(\Omega_\ell)
 \tag{53}
\]

with errors at most `epsilon` from `h^D_(l,a)(t_j)` and
`a^D_(l,a)(t_j)`, respectively. Include every layer, including layer one
for its outer update and layer `L` for the readout. Take one finite
union program for all these nodes, using the same initialized operators
and roots. Clip each `H` node to `[-1,1]`; this does not increase its
error, since the target is tanh-bounded. At `j=0` use the exact initial
forward nodes and set all `A` nodes to zero, since the dense limiting
readout is zero.

No independence of these approximants is asserted or needed. Finite
unions preserve all same-neuron and same-array correlations. Every
tensor below maps from `Omega_(l-1)` to `Omega_l`; no expectation pairs
fields from different populations. A finite implementation uses the
actual array `W_(0,l)` for each forward action and its actual transpose
for its reverse action.

Let `H^(Delta,epsilon)(t)` and `A^(Delta,epsilon)(t)` be the piecewise
linear interpolants of (53). Let `r^Delta(t)` linearly interpolate the
deterministic dense residual samples. These are prescribed proof-only
histories. Define a parameter reference by their exact integrals:

\[
 \begin{split}
 W_1^R(t)&=W_{0,1}-\frac2m\sum_a\int_0^t
                           A_{1,a}(s)q_a^Tds,\\
 W_\ell^R(t)&=W_{0,\ell}-\frac2m\sum_a\int_0^t
                           A_{\ell,a}(s)\otimes H_{\ell-1,a}(s)ds,
                       \quad 2\le\ell\le L,\\
 w^R(t)&=w_0-\frac2m\sum_a\int_0^t r_a^\Delta(s)H_{L,a}(s)ds,
 \qquad q_a=x_a/\sqrt d.
 \end{split}
 \tag{54}
\]

At the population set `w_0=0`. At finite width use the actual small
readout root in the first term, so the proxy starts from exactly the
same finite parameters. Its vanishing RMS contributes only a vanishing
fixed-program initialization perturbation.

The integrals in (54) are finite rank at every time. For example, on
one cell write `A=A_j+s Delta A_j`, `H=H_j+s Delta H_j`, with
`0<=s<=1`. The increment through fraction `s` of the cell is

\[
 \Delta\left[s A_j\otimes H_j+
       \frac{s^2}{2}(\Delta A_j\otimes H_j+A_j\otimes\Delta H_j)
       +\frac{s^3}{3}\Delta A_j\otimes\Delta H_j\right].
 \tag{55}
\]

Thus every learned matrix is a finite sum of correctly typed
`uv^T/n` at finite width, and its transpose is the exact reverse of
that sum. Its Frobenius norm is controlled by products of the finite
RMS norms. Its population counterpart is Hilbert--Schmidt. We do not
approximate the initialized operator in Hilbert--Schmidt norm.

### 12.2. The regularity constants are uniform in the mesh

The dense forward histories have a common `H1` bound from their bounded
physical parameter velocities and the forward chain rule. Linear
interpolation of their exact samples does not increase the `H1`
seminorm, by Jensen on each cell. If `e_j` is a nodal error with
`||e_j||_2<=epsilon`, the interpolated error satisfies

\[
 \|\partial_t e^{\rm lin}\|_{L^2(0,T;L^2)}
  \le \left(\sum_j\frac{(2\epsilon)^2}{\Delta}\right)^{1/2}
  =2\sqrt T\,\epsilon/\Delta.
 \tag{56}
\]

Hence the prescribed forward histories in (54) have a common `H1`
bound whenever `epsilon<=C Delta`; choosing `epsilon=o(Delta)` makes
this extra seminorm vanish.

Linear interpolation of samples from a `gamma`-Hölder Hilbert-valued
path preserves its Hölder constant up to an absolute factor. For two
times less than `Delta` apart, sum the adjacent-cell slope bound
`K Delta^(gamma-1)` over the intervening distance. For times farther
apart, compare to the nearest mesh endpoints and use their Hölder
bound. The interpolated nodal error has increment bounded both by
`2epsilon` and by `2epsilon |t-s|/Delta`; therefore its Hölder seminorm
is at most `2epsilon Delta^-gamma`. Applying (48) with `gamma=1/2`,

\[
 [A^{\Delta,\epsilon}]_{C^{0,1/2}(L^2)}
       \le C_T+C\epsilon/\sqrt\Delta.
 \tag{57}
\]

Take, for example, `epsilon=Delta^2`. Equations (56)--(57) give all
projection constants independent of mesh and program approximation.
They use differences of nearby dense samples, not derivatives of an
Euler response or a trained finite network.

At every fixed mesh and fixed approximating program, the empirical
RMS norms and pairings of all nodes and their differences converge by
A.1. The finite forward energy in (56) is a finite sum of these
second moments. The finite source Hölder constant can be bounded by
the maximum over the finite set of nodal increment quotients and
then the interpolation argument above. Consequently the limiting
upper bounds for these finite constants are the same mesh-independent
ones, with probability tending to one as width tends to infinity.
The width threshold may depend on the fixed mesh and program.

### 12.3. Approximate network consistency and carrier tails

At the population, uniform interpolation error tends to zero as
`Delta->0`, `epsilon=Delta^2`. In the first layer and readout, use
the integral equations directly. For each hidden link, subtract its
two rank-one integrands and use

\[
 \|A\otimes H-a_D\otimes h_D\|_{\rm HS}
 \le\|A-a_D\|_2\|H\|_2+\|a_D\|_2\|H-h_D\|_2.
 \tag{58}
\]

This proves
`sup_t d(theta_R(t),theta_D(t))->0` in the stronger sum topology.
The one-reference cutoff inequality against the dense state, followed
by (46), gives uniform `L2` convergence of recomputed backward fields
and their initialized carriers. Forward fields and residuals converge
by (4). In particular there is a deterministic `nu_Delta->0` bounding
all the population mismatches

\[
 \begin{split}
 &\|h_{\ell,a}(\theta_R(t))-H_{\ell,a}(t)\|_2,\qquad
 \|a_{\ell,a}(\theta_R(t))-A_{\ell,a}(t)\|_2,\\
 &|r_a(\theta_R(t))-r_a^\Delta(t)|,
 \qquad\|k_{\ell,a}(\theta_R(t))-k^D_{\ell,a}(t)\|_2.
 \end{split}
 \tag{59}
\]

No rate for `nu_Delta` is needed in the width-first argument.

The learned-adjoint bound used later in (29) holds directly for this
proxy, despite its prescribed sources differing from its recomputed
`r delta`. Indeed, (54) and the clipping `|H|<=1` give, for every
current Hilbert vector `v`,

\[
 \|(W_\ell^R-W_{0,\ell})^*v\|_\infty
 \le\frac2m\sum_a\int_0^t
           \|A_{\ell,a}(s)\|_2\|v\|_2ds\le C_T\|v\|_2.
 \tag{59a}
\]

The same calculation at finite width uses the normalized pairing
`A^T v/n` and is exact. Likewise
`||w_R-w_0||_infinity<=2 m^-1 sum_a integral |r_a^Delta|`.
Thus all learned gate-carrier terms in the autonomous subtraction
are uniformly bounded pointwise. Only the initialized reference
carriers require the cutoff. No identity equating the prescribed
source to the recomputed proxy source is used in this bound.

At finite width, reconstruct (54) from the finite program nodes using
the sampled initialization. For any fixed time, append the population
forward/backward evaluations at that proxy to the same finite program,
freezing its finitely many scalar contractions at their population
values. A finite proxy matrix acting on a node differs from its
prescribed action by a finite sum of terms

\[
 u_n\left(v_n^Tz_n/n-\mathbb E[VZ]\right).
 \tag{60}
\]

Their RMS norms tend to zero. The transpose action has the same
calculation with the two correctly typed tensor factors exchanged.
Induction up the forward layers uses Lipschitz tanh; induction down
the backward layers uses a cutoff on the fixed reference nodes and
their convergent second moments, exactly as in maintained C.1. Thus
the recomputed finite proxy responses and carriers have the expected
joint `L2`-consistent fixed-program laws.

This statement is uniform over physical time on the fixed compact
interval. To see this without invoking an infinite computation,
first use a finite time net. Equation (54) has uniformly bounded
parameter speed, because the prescribed source and forward norms
are bounded. Its forward fields are uniformly Lipschitz in time.
Between adjacent points of the time net, backward subtraction against
the preceding reference time gives `C(1+M)` times the parameter
increment plus the empirical cutoff tail at that net point. At a
fixed net and cutoff those tails converge. First choose the cutoff
large for the compact population proxy path, then choose the time
net fine, and finally take width large. This proves uniform response
consistency and uniform vanishing of its empirical extra error.

The same argument and the truncation inequality (36) give, for every
fixed `M,Delta`, a single error `o_Pr(1)` independent of closure order
such that the finite proxy initialized-carrier tail is at most

\[
 H_R^n(M)\le C e^{-c'M^2}+C\nu_\Delta+o_{\mathbb P}(1).
 \tag{61}
\]

For a precise cutoff transfer one may use a continuous cutoff equal to
one above `M` and zero below `M/2`; this is a continuous quadratic-growth
measurement covered by A.1. This avoids any assumption about atoms at
the cutoff. There is no trained finite-network tail assertion in (61).

## 13. The resulting width-first old-clock endpoint theorem

Assume (46), first with `Y>0`. By (6) the dense population residual has
a positive lower bound `mu_D`. For fine fixed mesh and large width,
(59)--(60) put the proxy residual above `3mu_D/4`. Stop the actual
closure when its distance from the proxy is `mu_D/(4C_f)`; then its
residual is at least `mu_D/2`. On this stopped interval use the
prescribed histories (54) in the closure clock, with backward history
`A/widehat rho` and zero prefix. Equations (49)--(50),(56)--(57)
give a `P^-1/2` backward tail uniformly in mesh, order and large width.
The prescribed forward tail is `P^-1`. Its exact reference integral
is (54), so signed consistency is `C P^-3/2` with no reference ODE
defect.

In the comparison (22)--(25), replace `h_D,a_D` by the prescribed
`H,A`. Their differences from recomputed proxy fields contribute
`C(nu_Delta+o_Pr(1))` to (23)--(24). The last term (25) becomes

\[
 CP^{-1/2}\left[D(t)+\nu_\Delta+o_{\mathbb P}(1)\right],
 \tag{62}
\]

because the mismatch bound (59) is uniform in time. The source
comparison (29) uses the **actual proxy** as reference and (61).
All errors here depend on the fixed program and initialized arrays,
not on the closure order. Absorb (62), then apply the scalar
integrating factor at a fixed cutoff `M`. For every sufficiently
large fixed `P_0`, simultaneously for all `P>=P_0`,

\[
 \sup_{P\ge P_0}\sup_{t\le T}
 d_n(\widehat\theta_{n,P}(t),\theta^R_n(t))
 \le C e^{C(1+M)T}
       [P_0^{-3/2}+\nu_\Delta+e^{-c'M^2}+o_{\mathbb P}(1)].
 \tag{63}
\]

Constants can absorb a factor `1+M` multiplying `nu_Delta`; either
form vanishes in the ordered limit at fixed `M`. The ordinary forced
ODE comparison between the actual finite dense flow and the same
proxy gives (63) with the term `P_0^-3/2` removed. This comparison
uses only the finite proxy equation mismatch from (59), and its
tails (61); it does not differentiate a trained dense field.

Take width to infinity at fixed `M,Delta` and its fixed approximating
program, then let `Delta->0` with `epsilon=Delta^2`. Choose

\[
 M=\max\left(1,\sqrt{\frac{3}{2c'}\log(e+P_0)}\right).
 \tag{64}
\]

The tail in (63) is at most `C P_0^-3/2`. Triangle inequality gives,
with constants depending only on the fixed horizon and dense bounds,

\[
 B_*(P_0)=C P_0^{-3/2}
                    e^{C_T\sqrt{\log(e+P_0)}}\le C_T'/P_0,
 \tag{65}
\]

and for every fixed sufficiently large `P_0` and every `zeta>0`,

\[
 \lim_{n\to\infty}
 \mathbb P\left\{\sup_{P\ge P_0}\sup_{t\le T}
  d_n(\widehat\theta_{n,P}(t),\theta_n^D(t))
                        >B_*(P_0)+\zeta\right\}=0.
 \tag{66}
\]

For the first-exit argument, first take `P_0` large enough that (65)
is below `mu_D/(8C_f)`. The cutoff, mesh and width errors can then be
chosen below the remaining margin; thus (63) excludes the stopped
exit with probability tending to one. Global finite old-clock
existence was already proved independently. No lower residual bound
for the actual closure was assumed beyond this removable stop.

When `Y=0`, Section 8 gives the stronger direct autonomous estimate
on common initial bounds, and the limiting reference is stationary.
For the literal envelope in (66), write `R=||w_0||_2/sqrt(n)->0`.
Uniformly over all orders, readout increments are `O(R)`, first-row
increments are `O(R²)`, and hidden closure increments are
`O(R^(3/2))` by projection contraction
`||A_l||_op<=||A_l||_HS<=2 sqrt((1+TR)TR) beta_l`, with
`beta_l=O(R)`. Dense hidden increments are `O(R²)`.
Thus `sup_(P>=1) e_(n,P)->0` in probability on the initialized
operator bounds, which is stronger than the fixed-`P_0` assertion
(66). This edge case does not require dividing by a vanishing dense
residual. Forward recursion transfers (66) to predictions on any
fixed bounded input set. Taking the dense width limit then gives
the corresponding width-first approximation to the population
predictor.

The order of quantifiers in (66) is essential. For each fixed `P_0`
the proof chooses a fixed cutoff and then a sufficiently accurate
finite program before taking width large. Its width threshold can
depend on `P_0`. This proves the width-first constant-times-`P^-1`
endpoint without finite trained tails or dense-source BV. It does
not establish an all-width rate, a width-uniform expectation bound,
or a global-in-time Gaussian source estimate. Those are separate
obligations, unchanged by this combination.

## 14. Separate sharpening: every width-first exponent below two

This optional extension was derived after freezing Sections 11--13. It
uses the same dense-only premise (46), the same original autonomous old
clock, and the same finite-program proxies. It does not alter their
construction or require dense backward-source derivatives.

Optimize (47) with `e^(-c'M²)` of order `h` instead of `sqrt(h)`. On
the fixed horizon, define the increasing concave modulus

\[
 \psi(h)=h\sqrt{\log(eT_1/h)},\quad 0<h\le T_1,
 \qquad T_1=\max(1,T),\quad\psi(0)=0.
 \tag{67}
\]

Then

\[
 \|a_D(t)-a_D(s)\|_2\le C_T\psi(|t-s|).
 \tag{68}
\]

The derivative of `psi` is
`sqrt(log(eT_1/h))-1/[2sqrt(log(eT_1/h))]>0`; differentiating once
more gives a negative number. Thus `psi` is increasing and concave,
and `psi(h)/h` is decreasing. Linear interpolation of its sample
values preserves a `psi` modulus up to an absolute factor: for
`h<=Delta`, the slope bound gives `C psi(Delta) h/Delta<=C psi(h)`;
for `h>=Delta`, comparison with adjacent mesh endpoints gives the
claim using monotonicity and `psi(3h)<=3psi(h)` where applicable.
The bounded extension for arguments above `T_1` only changes constants.
An interpolated nodal error of size `epsilon` has modulus constant
at most `2epsilon/psi(Delta)`, by its two increment bounds
`2epsilon` and `2epsilon h/Delta`. Consequently the source proxies
with `epsilon=Delta²` have a mesh-uniform version of (68).

Let `A(xi)` denote one such prescribed source placed in the actual
closure clock, extended as zero over the unit prefix. It is continuous
there because its initial sample is exactly zero. The residual
bootstrap and the Lipschitz inverse clock preserve the modulus (68),
with constants depending only on the fixed residual floor and horizon.
Extend `g(xi)=1/widehat rho(t(xi))` constantly over the prefix. By
(49)--(50), its weak derivative satisfies

\[
 \int_0^{\widehat\tau}|g'(\xi)|^2d\xi
   =\int_0^t\frac{|\dot{\widehat\rho}(s)|^2}
                    {\widehat\rho(s)^5}ds\le C_T,
 \qquad \|g\|_\infty\le 2/\mu_D.
 \tag{69}
\]

Its prefix extension is continuous, so no jump appears in (69).
The backward reference history is `B=gA`. Its direct Hölder modulus
would be limited by that of `g`, but its polynomial approximation need
not lose that regularity: smooth only the source factor.

Let `A_J` interpolate `A` on `P` equal cells of the clock interval.
The modulus (68) gives

\[
 \|A-A_J\|_{L^2}\le C P^{-1}\sqrt{\log(e+P)},\qquad
 \|A_J'\|_{L^2}\le C\sqrt{\log(e+P)},\qquad
 \|A_J\|_{L^\infty(L^2)}\le C.
 \tag{70}
\]

The proofs are the cellwise calculation in (51), now using
`psi(tau/P)`. Since `g` is scalar `H1` and `A_J` is Hilbert-valued
piecewise linear, the product rule holds and gives

\[
 \|(gA_J)'\|_{L^2}
 \le\|g\|_\infty\|A_J'\|_{L^2}
       +\|A_J\|_{L^\infty(L^2)}\|g'\|_{L^2}
 \le C\sqrt{\log(e+P)}.
 \tag{71}
\]

Best approximation, (7),(69)--(71) therefore yield

\[
 \|(I-\Pi_P)B\|_{L^2}
 \le\|g(A-A_J)\|_{L^2}
       +\|(I-\Pi_P)(gA_J)\|_{L^2}
 \le\frac{C\sqrt{\log(e+P)}}P.
 \tag{72}
\]

The prefix zero is essential for this sharpening. At nonzero population
initial readout a `P^-1/2` step term must be restored. Canonical finite
small readout does not cause that step in this proof-only proxy: its
assigned initial source is zero while its physical readout uses the
same small finite root; the resulting small recomputation mismatch
was already included in the fixed-program `o_Pr(1)`.

Pair (72) with the forward `P^-1` tail. The signed consistency in
(63) improves to `C P_0^-2 sqrt(log(e+P_0))`, and the absorbable
coefficient improves to `C P_0^-1 sqrt(log(e+P_0))`. Take
`M=max(1,sqrt(2 log(e+P_0)/c'))`, and repeat the same ordered limits.
The sharper version of (65)--(66) has

\[
 B_{**}(P_0)=\frac{C\sqrt{\log(e+P_0)}}{P_0^2}
                e^{C_T\sqrt{\log(e+P_0)}}.
 \tag{73}
\]

For every fixed `gamma<2`,
`sup_(P>=1) P^(gamma-2) sqrt(log(e+P)) exp(C_T sqrt(log(e+P)))`
is finite, so `B_**(P_0)<=C_(T,gamma) P_0^-gamma`.
This is an old-clock **width-first** rate with every exponent below
two. It does not prove an exact `C/P²` rate, modify the joint-clock
algorithm, or improve the all-width quantifiers.
