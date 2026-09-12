# Internal sampling/continuation interface check

Author: `continuation_route`, 2026-09-12. This is an internal interface audit,
not a promotion review. The frozen continuation and sampling files are not
modified. The statistical lemma passes this audit under the continuation
premises; explicit coefficients satisfying those premises are derived below.

## Inputs and coverage

Read in full: `sampling_lemma.md`, SHA-256
`02ba380b261f69295b6cfb92b32684ffdf9c2683a43130ded0b246de92c1a5d1`.
The entire frozen continuation proof was authored and checked in the prior
round: `attempt_continuation.md`, SHA-256
`49e8c43cd425ebd27772bbde6cff1cdbc46d252772d29337b0ff9f2a934bf032`.
Its established source/dependency read coverage is recorded there. The
scientific source `docs/global_nonlinear.md` remains at SHA-256
`7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.
No other route's proof was read for this audit. The supervisor authorized
comparison after first-round freezing. Required skills and process references
were already read; current shared instructions were checked again.

No experiment, simulation, numerical training, Git operation or independent
promotion review was performed. This report contains mathematical checking
and explicit bounds. Its author is also the continuation author, so this is
not an independent audit of that continuation theorem.

## 1. Declared constants and radius

Use the exact C.4.9 raw Hilbert norm and normalized input `|u|=1`. Assume
the reached source tube, including the endpoint, supplies

\[
\|c_\theta\|_\infty\le L_{src},\qquad
\tau_R(Q_\theta(u))\le M_{src}e^{-c_{src}R^2}
\quad(R\ge1),
\tag{S1}
\]

uniformly over its deterministic inputs and states, with
`c_src>0`, `M_src>=0`. Here `L_src` may be the total accumulated absolute
control-mass bound: the zero population initial readout then gives its
first assertion. If `L_src` was assigned a different meaning, substitute
the actual readout-supremum bound in its place. No random coordinate
supremum over all input queries is required.

Let

\[
a=\|A_\dagger\|_{op}+1,\quad c=\|c_\dagger\|_2+1,\quad H=L_{src},
\quad k=\lambda_{min}(M_\dagger)>0.
\tag{S2}
\]

On the closed raw unit ball about `theta_dagger`, the action norm is at
most `a` and readout `L2` norm at most `c`. Define the following explicit
positive constants:

\[
L=\sqrt{1+c^2(1+a^2)},\qquad z=\sqrt{1+a^2},
\]
\[
D=\sqrt{1+4H^2z^2},\quad Q_0=c+aD,\quad D_0=Q_0+D+c+z,
\]
\[
b=\max\{1,c_{src}^{-1/2}\},\qquad
C_g=D_0+2b+M_{src}/e,
\tag{S3}
\]

and the radius

\[
\rho=\min\left\{\tfrac12,\left(\frac{k}{8LC_g}\right)^2\right\}.
\tag{S4}
\]

Here the symbol `Q_0` is a scalar bound, not a training law or query field.
The continuation neighborhood may be decreased to this radius. All
constructed paths referred to below must lie in this smaller neighborhood;
the continuation proof permits the corresponding reduction of its episode.
On that neighborhood, the usable sampling constants are

\[
B_f=c,\qquad L_f=L_g=L,
\]
\[
K=2\left[L^2+(c+Y)C_g\left(1+\frac{4L}{\sqrt k}\right)\right].
\tag{S5}
\]

These formulas depend only on the supplied source constants, anchor gap,
endpoint action/readout norms and bounded-label constant. No task-specific
trajectory, sample, target coefficient or Fourier cutoff enters `K`.
The first-row endpoint norm is not needed for this same-input state bound;
it is needed for spatial bounds in the continuation proof.

The established endpoint inequalities permit the fully reference-based
choices `a=3+sqrt(10)` and `c=1+sqrt(10)`, if exact endpoint norms are
not evaluated. Using upper bounds for `a,c,H,M_src` and a positive lower
bound for `k,c_src` in these displays preserves every assertion.

## 2. Derivation of the gradient modulus

First, at every state in the unit ball the three gradient blocks have norms
at most `ac,c,1`. Thus `||g_theta(u)||raw<=L`. Along the straight segment
between two unit-ball states this bound remains valid. The scalar prediction
is continuously differentiable by the established strong scalar-gradient
theorem. Integrating that derivative gives

\[
|f_\theta(u)-f_{\bar\theta}(u)|\le Ld,
\qquad d=\|\theta-\bar\theta\|_{raw}.
\tag{S6}
\]

Also `|f_theta(u)|<=c`. These prove `L_f=L_g=L`, `B_f=c`.

For gradient comparison only the barred state must have (S1). Let
`x=||w-bar w||2`, `y=||K-bar K||HS`, `v=||c-bar c||2`, so
`x^2+y^2+v^2=d^2`. The forward difference is bounded by
`||Z2-bar Z2||2<=y+ax<=z d`. Since `|phi''|<=2` and the barred
readout is bounded by `H`, splitting its upper gate gives

\[
\|\delta-\bar\delta\|_2
\le v+2H(y+ax)\le Dd.
\tag{S7}
\]

For the actual adjoint query, subtract the action first:

\[
\|Q-\bar Q\|_2
\le c y+a\|\delta-\bar\delta\|_2\le Q_0d.
\tag{S8}
\]

The middle rank difference has norm at most `(D+c)d`, and the readout
gradient difference at most `zd`. For the row block,

\[
\phi'(w\cdot u)Q-\phi'(\bar w\cdot u)\bar Q
=\phi'(w\cdot u)(Q-\bar Q)
 +[\phi'(w\cdot u)-\phi'(\bar w\cdot u)]\bar Q.
\]

Because `0<=phi'<=1`, its gate difference is at most 1 pointwise, and
also at most `2|(w-bar w).u|`. Splitting `bar Q` at `R>=1` therefore
gives the row bound `(Q_0+2R)d+M_src exp(-c_src R^2)`. The raw norm is
at most the sum of block norms, so

\[
\|g_\theta(u)-g_{\bar\theta}(u)\|_{raw}
\le(D_0+2R)d+M_{src}e^{-c_{src}R^2}.
\tag{S9}
\]

For `0<d<=1` choose `R=b sqrt(log(e/d))`, with `b` from (S3).
Then `R>=1`, `c_src b^2>=1`, and the tail is at most `M_src d/e`.
Since `d<=omega(d)=d sqrt(log(e/d))`, (S9) becomes

\[
\|g_\theta(u)-g_{\bar\theta}(u)\|_{raw}\le C_g\omega(d).
\tag{S10}
\]

At zero the gradients coincide. This bound uses no ambient Hessian or
local Lipschitz claim for the raw neural field.

## 3. Anchor gap and a sharper projector estimate

Both anchor columns have norm at most `L`. Thus `||G||op<=sqrt(2)L`,
and (S10) gives `||G-bar G||op<=sqrt(2)C_g omega(d)`. In particular,

\[
\|M_\theta-M_\dagger\|\le4LC_g\omega(\|\theta-\theta_\dagger\|).
\tag{S11}
\]

For `0<s<=1`, `s log(e/s)<=1`, since its derivative is `-log(s)>=0`
and its value at 1 is one. Hence `omega(s)<=sqrt(s)`. Equations
(S4), (S11) yield `M_theta>=k I/2` throughout the radius-`rho` ball.
Two states there have distance at most one, so (S10) applies to every
comparison required by the sampling lemma.

Write `P=GM^{-1}G*`, `Pi=I-P`, and `B=GM^{-1}`. Because
`B*B=M^{-1}`, one has `||B||<=sqrt(2/k)`. For two states the exact identity

\[
P-\bar P=\bar\Pi(G-\bar G)B^*
                  +\bar B(G-\bar G)^*\Pi
\tag{S12}
\]

follows from `P-bar P=bar Pi P-bar P Pi`, with `bar Pi bar G=0`
and `G*Pi=0`. Orthogonal projectors have norm at most one. Consequently

\[
\|\Pi-\bar\Pi\|\le2\sqrt{2/k}\|G-\bar G\|
\le\frac{4C_g}{\sqrt k}\omega(d).
\tag{S13}
\]

This avoids an unnecessary squared inverse-gap factor from directly
expanding three projector factors. For the projected gradient
`d_theta(u)=Pi_theta g_theta(u)`, subtract its gradient and projector:

\[
\|d_\theta(u)-d_{\bar\theta}(u)\|
\le C_g\left(1+\frac{4L}{\sqrt k}\right)\omega(d).
\tag{S14}
\]

For any probability law `Q` with labels in `[-Y,Y]`, split the field
difference into the changed scalar prediction and changed projected gradient.
Use `||d_theta||<=L`, (S6), `|f_bar theta-y|<=c+Y`, and (S14). The result is

\[
\|V_Q(\theta)-V_Q(\bar\theta)\|
\le2L^2d+2(c+Y)C_g(1+4L/\sqrt k)\omega(d)
\le K\omega(d),
\tag{S15}
\]

with exactly (S5). The barred state is the source-bearing one; the other
state can be any raw state in the smaller ball. This is the precise premise
needed when the sampling lemma compares two states under the empirical law.

## 4. Explicit derivative bounds along reached curves

This subsection also makes the continuation/sampling horizon interface
quantitative. It does not assume differentiability on an arbitrary raw ball.
Let the reached controlled curve have total absolute force mass `m(t)` per
unit time, allowing a signed measure over inputs. Under (S1), the tail
layer-cake identity gives

\[
E|Q(u)|^4=4\int_0^\infty r^3\Pr(|Q(u)|>r)dr
\le1+4M_{src}^2\int_1^\infty r e^{-2c_{src}r^2}dr
=1+\frac{M_{src}^2e^{-2c_{src}}}{c_{src}}.
\]

The probability bound used here is `Pr(|Q|>r)<=tau_r(Q)^2/r^2`.
Define

\[
q_4=\left(1+M_{src}^2e^{-2c_{src}}/c_{src}\right)^{1/4},
\quad Z_t=c(1+a^2),
\]
\[
D_t=1+2HZ_t,\quad Q_t=c^2+aD_t,
\quad T_g=2q_4^2+Q_t+D_t+ac^2+Z_t.
\tag{S16}
\]

The controlled equations yield
`||w'||2<=ac m`, `||w'||4<=q_4 m`, `||K'||HS<=c m`, and
`||c'||infty<=m`. Strong forward differentiation gives
`||Z2'||2<=Z_t m`, upper differentiation gives `||delta'||2<=D_t m`,
and actual adjunction gives `||Q'||2<=Q_t m`. The row-gradient derivative
is bounded by `(2q_4^2+Q_t)m`, its middle derivative by
`(D_t+ac^2)m`, and its readout derivative by `Z_t m`. Thus

\[
\|g_\theta(u)'\|_{raw}\le T_g m(t),\quad
\|G'\|\le\sqrt2T_g m(t),\quad \|M'\|\le4LT_g m(t).
\tag{S17}
\]

These are strong absolutely continuous identities: coordinatewise scalar
chain rules follow from the integrable raw velocities and Fubini, the
bounded readout handles upper products, and Hölder with the two `L4`
factors handles `w'Q`. Their derivatives are Bochner integrable, giving
the strong fundamental theorem. Uniform `L8` query bounds from the source
tails and `L2` continuity also give `L4` strong measurability by interpolation.

Differentiating the finite inverse and using its gap bound now gives

\[
\|B'\|\le T_B m(t),\qquad
T_B=\frac{2\sqrt2T_g}{k}+
                \frac{16\sqrt2L^2T_g}{k^2}.
\tag{S18}
\]

This explicitly supplies the `B'(t)r(t)` product bound from the continuation
argument, with no hidden Hessian constant.

## 5. What determines an available common episode

The source radius `delta_src>0` is a separate output of C.4.9 unit A.
The three numbers `(L_src,M_src,c_src)` do not by themselves assert how
large a perturbation remains in their source tube. Consequently they
determine (S5), but **do not alone determine a positive stopping horizon**.
The source-tube radius and reference convergence bounds must also be used.
The continuation proof has these inputs; a combined theorem should retain
them explicitly instead of implying that tails alone imply continuation.

Here is one completely specified sufficient reduction of its episode once
`delta_src` is supplied. Put `B_r=c+Y` and define

\[
A_s=2B_r+4B_rL/\sqrt k,\qquad V_s=2B_rL,
\]
\[
C_s=32B_rL^2/k+\sqrt2+2B_r.
\tag{S19}
\]

The constrained added controls have total mass at most `2B_r`; their
anchor controls `2M^{-1}G*v` have `l1` norm at most
`2sqrt(2)||B*||||v||<=4B_rL/sqrt(k)`. This proves `A_s`; `Pi` being a
contraction proves `V_s`.

For the physical mixture in this neighborhood, at `epsilon<=1/2`, the
anchor residual equation has contraction at least `lambda_0=k/4` and
forcing norm at most `F epsilon`, where `F=2sqrt(2)B_rL^2`. Its Euler
residual expansion has remainder

\[
|R_j|\le C_Rh_j^2(|r_j|+\epsilon)^2,
\qquad C_R=2\sqrt2LT_gB_r^2.
\tag{S20}
\]

Indeed node control mass is at most `sqrt(2)|r_j|+2B_r epsilon`, hence
at most `2B_r(|r_j|+epsilon)`. On an affine step, (S17) bounds its
anchor-gradient derivative by `T_g` times that mass, while speed is at
most `L` times the mass. A second scalar integration and the `sqrt(2)`
factor for the two residuals prove (S20). Intermediate affine states are
fractional Euler updates, so the same source bounds apply while stopped
inside the source tube.

Let `R_max=sqrt(2)(c+1)`. Choose the proof mesh with

\[
h_j\le\min\{(2L^2)^{-1},\ k/[8C_R(R_{max}+1)]\},
\tag{S21}
\]

and sufficiently small for the source control-clock threshold and the
inner/outer raw step margins. Absorbing (S20) gives residual contraction
`lambda_0/2=k/8` and forcing `F+lambda_0/2`. Telescoping then proves

\[
\int_b^t m^h(s)ds\le\frac{8\sqrt2}{k}|r_b|
                      +C_s\epsilon(t-b),
\tag{S22}
\]

where (S19) is exactly the resulting slow-time coefficient. Raw displacement
is bounded by `L` times this mass. No `hT` accumulation enters.

For example the following positive time is sufficient for the constrained
construction and the physical continuation first-exit budgets:

\[
T_{cont}=\min\left\{
\frac{\delta_{src}}{16A_s},\frac{\rho}{16V_s},
\frac{\delta_{src}}{16C_s},\frac{\rho}{16LC_s}\right\}.
\tag{S23}
\]

Here is a precise choice order that verifies the remaining margins. First
use the fixed reference bounds
`||theta_*(b)-theta_dagger||<=sqrt(10)e^(-b/5)`,
`|r_*(b)|<=sqrt(2)e^(-b/5)` and
`s_dagger-s_*(b)<=10e^(-b/5)` to choose `b` so that each of:

- reference raw endpoint error;
- `L(8sqrt(2)/k)|r_*(b)|`;
- `(8sqrt(2)/k)|r_*(b)|`;
- remaining reference control mass

is below respectively `rho/32,rho/32,delta_src/32,delta_src/32`.
Each is an explicit exponential inequality, hence supplies an explicit
finite `b`. Next choose epsilon and the proof mesh small enough that the
mixture-prefix raw error and its effect on `r_b` use at most the same
margins, and its integrated control discrepancy is below `delta_src/32`.
The continuation proof's fixed-`b` cutoff estimate tends to zero uniformly
over added laws and ensures those choices. The actual optimizer uses no
prefix splice; this is only its proof decomposition.

The source-distance total after `b` is then at most its prefix discrepancy,
reference suffix, the residual term in (S22) and `C_s T_cont`. The raw
distance is bounded by the endpoint error plus `L` times (S22). The stated
choices keep both strictly below their inner half-radii. Constrained
appended Euler has the same strict budgets from `A_s,V_s`. Thus (S23) is
compatible with the complete continuation construction. Any learning
argument may decrease this time further using explicit class/reference
constants. The smallness threshold for epsilon may depend on the selected
reference prefix; there is no claimed explicit finite-width rate.

## 6. Audit of the statistical argument

Every step of `sampling_lemma.md` is valid under the supplied premises:

1. The Hilbert functions `r_t(X)d_t(X)` and `xi d_t(X)` use the
   deterministic population path. Strong measurability follows from the
   continuation construction; their bounds give the required moments.
2. The centered design average has second moment at most
   `L^2 E(t)/m`; the conditional label-noise average has second moment at
   most `L^2 sigma^2/m`. Off-diagonal terms vanish by independence and
   conditional centering. This does not assume independence of a trained
   empirical feature from its own label.
3. Cauchy–Schwarz in time gives the stated second-moment bounds on
   `2 integral ||I_m||` and `2 integral ||N_m||`. Markov followed by a
   union bound gives the declared `eta_m` with separate failure allowances.
4. Compare changed states under the empirical law, with the population
   state on the tail-bearing side. Equation (S15) is exactly this uniform
   one-reference premise. The remaining law difference at that fixed
   population state is `-2 I_m+2 N_m` with the displayed signs.
5. The Osgood integral inequality is valid up to its first proposed exit
   at one. Its strict initial-size condition prevents the exit. The zero
   case follows by decreasing positive upper errors to zero.
6. The risk triangle inequality and additive bounded-prediction risk
   estimate are valid, and hold on the same event uniformly in time.
7. Conditioning on a fixed sample is legitimate because continuation and
   width transfer hold for every fixed empirical law. Bounded conditional
   failure probabilities allow integration, then epsilon tends to zero,
   then sample count increases. A positive lower stopping time is needed
   only for the initial-layer transfer, not for the slow-path comparison.

The lemma's `B_0=sqrt(10)+1` is valid in the frozen class: `|q|<=1` and
`||F_*||infty<=sqrt(10)`. The population excess error is nonincreasing by
the constrained gradient identity, independently of any approximation
theorem. No target spatial smoothness is required for this statistical
proof. It is stronger than the design-Wasserstein sampling bound in the
frozen continuation attempt and can replace that estimate in a synthesis.

There is no required correction to the frozen sampling lemma. Its warning
that it does not independently supply an observable stopping rule is
appropriate. The constants above close its continuation interface; a
population learning bound must still supply any desired improvement claim.

## 7. Explicit sample threshold and stopping interface

Fix a declared deterministic `0<T<=T_cont`, further decreased as needed
by the learning bound, and failure allowances `delta_I,delta_N>0` with
sum less than one. Let

\[
C_{stat}=2TL\left(\frac{B_0}{\sqrt{\delta_I}}
                         +\frac{\sigma}{\sqrt{\delta_N}}\right).
\tag{S24}
\]

For any desired raw error `0<r<1`, define

\[
\eta_*(r,T)=e\exp\left[-\left(\sqrt{\log(e/r)}+KT/2\right)^2\right],
\]
\[
m_*(r,T)=\max\left\{1,
\left\lceil\left(C_{stat}/\eta_*(r,T)\right)^2\right\rceil\right\}.
\tag{S25}
\]

For `m>=m_*`, the sampling lemma's argument obeys
`eta_m=C_stat/sqrt(m)<=eta_*`. Taking square roots of logarithms shows
`sqrt(log(e/eta_m))>=sqrt(log(e/r))+KT/2>1+KT/2`.
Thus its admissibility condition holds and inversion is exact:

\[
\Pr\left\{\sup_{t\le T}\|\theta_{\hat\nu_m}(t)-\theta_\nu(t)\|\le r,
\quad\sup_{t\le T,x}|P_{\hat\nu_m}(t,x)-P_\nu(t,x)|\le Lr\right\}
\ge1-\delta_I-\delta_N.
\tag{S26}
\]

If `sigma=0`, omit the noise allowance and use
`C_stat=2TLB_0/sqrt(delta_I)`. For a requested prediction error `e_p>0`,
take `r=min(1/2,e_p/L)`. For an additive excess-risk tolerance `e_R>0`
in the frozen class, take
`r=min(1/2,e_R/[2(c+1)L])`. All thresholds then use class/reference
quantities only. They can be enormous, but are declared finite numbers.

For example, if a population theorem at a deterministic declared time
`T_stop` in `(0,T_cont]` gives excess-risk improvement at least `Delta>0`,
choose `r=min(1/2,Delta/[4(c+1)L])`. At sample count (S25), empirical
population-carrier improvement is at least `Delta/2` with the displayed
confidence. The stopping rule is simply the declared slow endpoint
`T_stop`; actual finite GF stops at physical `T_stop/epsilon`. Both time
and sample requirement are determined before observing a trained path.
If `Delta` or `T_stop` instead requires the unknown regression function,
this is not an observable rule unless the learning theorem replaces them
by class/reference bounds. No statistical argument can supply that missing
learning input merely from continuity.

For a data-selected stopping time in a declared `[T_min,T]` with `T_min>0`,
(S26) remains valid because its event is uniform in time. The same width,
epsilon, sample ordering then applies. A rule using unknown population
risk is not made available by this fact alone.

## Conclusion of this internal check

The sampling lemma's statistical proof is correct under its stated
premises. Equations (S1)–(S15) give a complete explicit coefficient `K`,
region, and observation constants from the continued source bounds.
Equations (S16)–(S23) make the time-regularity and positive-horizon
interface explicit once the separate source radius is retained.
Equations (S24)–(S26) give the exact finite sample threshold.
An improvement-based stopping rule still requires the separately proved
population learning margin. Nothing in this check constitutes promotion
or an independent review of the continuation candidate.
