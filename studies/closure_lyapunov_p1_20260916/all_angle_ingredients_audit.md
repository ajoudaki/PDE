# Internal audit of the all-angle initialization and strict-gain ingredients

Date: 2026-09-16. This is an internal continuation audit, not a promotion
review. No source file was edited.

**Verdict: PASS.** Sections 1–2 of `all_angles_cone_attempt.md` prove
`B_2(0)>0` for every pair `(a,b),(a,-b)` with
`a>=0`, `b>0`, `a^2+b^2=1`. This implies `C_0>0` for the actual
initialized upper hidden contrast. The full argument in
`scalar_strict_gain.md` then proves strict endpoint contrast gain.
Combined with the already-audited scalar-margin theorem, these ingredients
give all-time fitting and complete-state convergence for every such
reflected pair, including unit labels, at every separation in `(0,pi]`.
No persistence assumption on a lower-layer cross sign is needed.

The orientation restriction remains essential to the available proof:
this is not a theorem for an arbitrary rotation of a pair in the fixed
finite dictionary. There is no uniform positive rate or gain as the pair
approaches coincidence.

## Scope and frozen inputs

The new scientific reads were precisely sections 1–2, lines 22–255, of
`all_angles_cone_attempt.md`, and the complete `scalar_strict_gain.md`.
Only section-heading metadata was read outside that excerpt. Neither
section 3 nor other new route/check files were read. In particular, the
references in the addendum to `cross_sign_note.md` and `route_local.md`
were not followed. The required initialized structure and derivative
continuity are independently verified below from the permitted canonical
equations and the prior audited initialization.

The prior audited `scalar_margin_extension.md` and `proof.md` supply the
scalar theorem and exact canonical initialization/symmetry. Their hashes
remain unchanged. No numerical experiment was used; hash computation was
the only programmatic verification.

| Input | SHA256 |
|---|---|
| `all_angles_cone_attempt.md`, whole-file identity | `f2e66270768724b5f9e5170465e37f99259a62158a0a10de149e94e4ccd7b87c` |
| `all_angles_cone_attempt.md:22-255`, actual excerpt including original line terminators | `5c7015b34203ed54128aeb57ad8bf4207db348d004b9b22a900150abbe65f646` |
| `scalar_strict_gain.md`, complete | `3533f444850eb020f90f4159c4003aab2163cd08d0ecefd647f28542f685c50b` |
| `scalar_margin_extension.md` | `3bbf89335a49f9b9c97e4aab8ace450f62d16fc2febe59eaa068b61fcf1dd5e7` |
| `proof.md` | `8cb77d4a1a1f879fa75780efc521f39c63c56feafec4a6c32f15e97ca1621dd0` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

## 1. Exact raw-coordinate initialization

Here `A,B` denote the two regression coefficients of section 1, not the
label amplitude used in the scalar theorem. Let
`R=[[v+eta,k],[k,sigma+eta]]` and let `L` be its lower Cholesky factor.
The initialized active normalized row is
`(alpha*v,alpha*k+tau*gamma)L^{-T}/sqrt(tau+eta)`, whereas the lower
normalized block is `L^{-1}(h,y)^T`. Their pairing is therefore

\[
 k_{\rm init}
 =\frac{(\alpha v,\alpha k+\tau\gamma)
              R^{-1}(h,y)^T}{\sqrt{\tau+\eta}}.
\]

Symmetry of `R^{-1}` gives exactly equation (1). Thus the conditional
sign lemma concerns the prescribed inverse-Cholesky initialization,
not a substituted regression or a change of metric. The ridge makes
`Delta=det R>0`.

The covariance `k=E[hy]` is strictly positive: the conditional mean
`F(h)=E_zeta tanh(zeta+alpha*h)` is odd and strictly increasing and
therefore has the strict sign of nonzero `h`. All variables are bounded
except Gaussian `zeta`, so the expectations used here are finite.

## 2. Audit of the coefficient and conditional-sign inequalities

Solving the two regression equations yields

\[
 B=\frac{\alpha k\eta+\tau\gamma(v+\eta)}{\Delta}>0,
 \qquad A=\frac{\alpha v-Bk}{v+\eta}.
\]

The bound `B<=1/gamma` is valid. Gaussian integration by parts gives
`E[zeta*y]=tau*gamma`; its boundary term vanishes because tanh is bounded
and the density is Gaussian. Since `h` and `zeta` are orthogonal in
`L2`, expanding the nonnegative square
`E[(y-(k/v)h-gamma*zeta)^2]` gives

\[
 \sigma\ge k^2/v+\tau\gamma^2.
\]

Hence

\[
 \Delta\ge(v+\eta)\tau\gamma^2
              +\eta(k^2/v+v+\eta)
 \ge(v+\eta)\tau\gamma^2+\alpha\gamma k\eta.
\]

The second inequality uses `k^2/v+v>=2k` and
`0<alpha*gamma<1`. Its right side is precisely `gamma` times the
numerator of `B`. Dividing by the positive quantities proves the
claimed coefficient bound. There is no missing factor of `tau`,
`gamma`, or the ridge in this comparison.

For the three inequalities in equation (6), write
`T=tanh zeta`, `G_0=E sech^2 zeta`, and `J(t)=E sech^2(zeta+t)`.

* Pairing the two signs of `zeta` in the tanh addition formula gives
  `E tanh(zeta+t)=tanh(t) E[(1-T^2)/(1-T^2 tanh^2(t))]`.
  For `t>=0` this is at least `G_0 tanh(t)`. Concavity of tanh on
  `[0,infinity)` gives `tanh(alpha*h)>=h*tanh(alpha)` for `0<h<=1`,
  proving `F(h)/h>=G_0*tanh(alpha)`.
* Differentiation under the bounded gate derivative and pairing the
  positive and negative integration variables give exactly the displayed
  formula for `J'(t)`. For `x,t>0`,
  `q_tau(x-t)>=q_tau(x+t)`, while
  `-2 sech^2(x)tanh(x)<0`. Thus `J(t)<=J(0)=G_0` for `t>=0`.
  Integration from `0` to `alpha*h` proves `F(h)/h<=alpha*G_0`.
* The paired sech-squared addition formula has the factor
  `(1+T^2 tanh^2(t))/(1-T^2 tanh^2(t))^2`, which is at least one.
  Therefore `J(t)>=G_0 sech^2(t)`. Since `|alpha*h|<=alpha`,
  averaging gives `gamma>=G_0 sech^2(alpha)`.

All denominators in these paired formulas are positive. For each fixed
finite `t`, they are bounded below by `sech^2(t)`, so these manipulations
also preserve integrability.

Oddness extends the bound on `F(h)/h` to negative nonzero `h`, and
therefore `k=E[hF(h)]<=alpha*G_0*v`. Using the positive coefficient
`B<=1/gamma` now gives the chain

\[
\begin{aligned}
 \frac{Ah+BF(h)}h
 &=\frac{\alpha v}{v+\eta}
       +B\left(\frac{F(h)}h-\frac{k}{v+\eta}\right)\\
 &\ge\frac{\alpha v}{v+\eta}
       -\frac{G_0}{\gamma}(\alpha-\tanh\alpha)\\
 &\ge\frac{\alpha v}{v+\eta}
       -(\alpha-\tanh\alpha)\cosh^2\alpha
 \ge\alpha\left(\frac{v}{v+\eta}-\frac56\right).
\end{aligned}
\]

The potentially negative parenthesis in the first line is handled with
the correct inequality direction. The final numerical bound is valid:
`tanh(alpha)>=alpha-alpha^3/3`, obtained by integrating
`sech^2(t)>=1-t^2`, and `cosh^2(1)<5/2` imply
`(alpha-tanh(alpha))cosh^2(alpha)<=5alpha^3/6<=5alpha/6`.

All elementary constants used to make this positive check out. On the
two intervals `1<=|g|<=2`, `tanh^2(g)>1/4`, the standard Gaussian density
exceeds `1/24`, and the combined interval length is two. Thus `v>1/48`.
For `eta=1/4096`,

\[
 \frac{v}{v+\eta}>\frac{4096}{4096+48}
   =\frac{256}{259}>\frac56.
\]

The bounds `e^2<8`, `sqrt(2pi)<3`, and `tanh(1)>1/2` justify the density
and tanh estimates. Also `2<e<11/4` gives
`e^2+e^{-2}<121/16+1/4<8`, whence
`cosh^2(1)=(e^2+e^{-2}+2)/4<5/2` as required.

Consequently the specified `c_0` is strictly positive and the
conditional version
`Q(g)=E[k_init|g]` satisfies
`Q(g)>=c_0*tanh(g)/sqrt(tau+eta)>0` for every `g>0`.
The explicit conditional integral is odd under `g -> -g` together with
`zeta -> -zeta`. No pointwise sign of the noisy `k_init` is assumed.

## 3. Initial signals, cross sign, and `C_0>0`

Independence of the two lower mark blocks permits conditioning away
their two independent reverse noises. For the second coordinate this
gives

\[
 B_2(0)=E\left[Q(g_2)J_2(g_2)\right],
 \qquad J_2(t)=E_{g_1}\tanh(a g_1+bt).
\]

For `b>0`, `J_2` is odd and has derivative
`b E sech^2(a g_1+bt)>0`. Thus both factors have the strict sign of
`g_2`, making their product positive almost surely off `g_2=0`.
The bounded integrability is immediate. Hence `B_2(0)>0`, including
`a=0`. The same argument gives `B_1(0)>0` for `a>0`; at `a=0`, its
expectation is zero by independence and oddness. Changing the sign of
an input coordinate reverses the corresponding conditional function,
which also verifies the more general sign statement in section 2.

The initialized cross-sign calculation is correct but is not needed
for the combined convergence theorem. Conditioning on `(g_1,g_2)`
factors the reverse-noise expectations. Pairing the four Gaussian sign
quadrants then gives the coefficient `2` and the difference of the two
sech-fourth powers shown in section 2. For `a,b,x,y>0`,
`|ax+by|>|ax-by|`, so the integrand is strictly negative. All factors
are bounded. Thus `C_cross(0)<0` and, when `a>0`,
`B_1(0) C_cross(0)<0`. Characteristic continuity indeed preserves
this strict inequality for some pair-dependent initial interval.
This is not a persistence proof for all auxiliary times. The separate
axis reduction gives the asserted zero cross signal at `a=0`.

The remaining bridge from `B_2(0)>0` to the hypothesis of the scalar
theorem is exact. At initialization, the canonical matrix has the two
active coordinate blocks and zero constant row/column. Lower mark
symmetry makes the first lower block the same for the two reflected
inputs and the second block change sign. Thus

\[
 z_+=\beta_1 B_1+\beta_2 B_2,
 \qquad z_-=\beta_1 B_1-\beta_2 B_2.
\]

Each `beta_i=tanh(xi_i)/sqrt(tau+eta)` has a continuous positive
density on `(-1/sqrt(tau+eta),1/sqrt(tau+eta))`; in particular
`P(beta_2=0)=0`. Since tanh is strictly increasing and `B_2>0`,

\[
 U_0=\frac{\tanh z_+-\tanh z_-}{2}
\]

has the strict sign of `beta_2` and is nonzero almost surely.
Therefore `C_0=E U_0^2>0`. This argument does not need `B_1>0`
and covers the antipodal endpoint.

## 4. Strict initial contrast derivative

The strict-gain addendum needs the two-block preactivation form only
at initialization. That form was established above without consulting
the excluded subsystem notes. Scale just the second initialized active
matrix row by `1+lambda`, keeping lower weights and all other rows
fixed. This is an admissible finite-Frobenius variation of the original
coefficient matrix. It changes `B_2` to `(1+lambda)B_2` and preserves
`B_1`. Differentiating yields

\[
 \frac{dU}{d\lambda}\bigg|_0
 =\frac{\beta_2 B_2}{2}
       (\operatorname{sech}^2z_++\operatorname{sech}^2z_-),
\]

and therefore exactly

\[
 \frac{dC}{d\lambda}\bigg|_0
 =E\left[U\beta_2 B_2
       (\operatorname{sech}^2z_++\operatorname{sech}^2z_-)\right]>0.
\]

Every gate is strictly positive, `U` has the sign of `beta_2 B_2`,
and the latter is nonzero almost surely. All differentiated quantities
are bounded. Thus the hidden-state gradient `grad_h C(h_0)` is nonzero
in the actual physical metric. The factor of two from differentiating
the square precisely cancels the `1/2` in the derivative of `U`.

## 5. Hidden-gradient activity and strict potential improvement

The derivative regularity invoked by the addendum follows directly
from the allowed equations. For either unit input, the map
`a(w)=E[b_1 tanh(w.u)]` has derivative
`Da(w)delta w=E[b_1 sech^2(w.u)(delta w.u)]` from the row `L2` space
to a finite coefficient space. Bounded marks and the bounded second
derivative of tanh control its Taylor remainder by a constant times
`||delta w||_2^2`. They also give the operator-norm bound

\[
 \|Da(w)-Da(\widetilde w)\|_{\rm op}
 \le2B_1\|w-\widetilde w\|_2.
\]

The upper preactivation `b_2^T M a(w)` is bounded in the upper
supremum norm on bounded matrix/row neighborhoods. It and its
derivative depend continuously on the hidden state; the bounded
`b_2` envelope upgrades coefficient continuity to this supremum
continuity. Multiplication by its tanh derivative therefore varies
continuously as an operator on upper `L2`. Taking the two-input
difference proves continuity of `DU(h)` in the physical operator
norm along the characteristic trajectory. Adjoint operator norms
have the same continuity. No differentiability theorem for an
unrestricted `L2`-to-`L2` Nemytskii map is being assumed.

The auxiliary equation and zero readout initialization consequently give

\[
 h_s=DU(h)^*c,\qquad
 c(s)=sU(h_0)+o(s),\qquad
 h_s(s)=\frac{s}{2}\nabla_hC(h_0)+o(s)
\]

in the physical hidden norm, since `grad_h C=2DU^*U`. Because this
gradient is nonzero, there is an `s_0>0` such that
`||h_s(s)||>=s||grad_h C(h_0)||/4>0` for every `0<s<s_0`.
The particular denominator four is just a permissible remainder bound;
the source claims only strict positivity.

The scalar theorem already gives `F>0`, `q>0` for `s>0` and

\[
 qK-F^2=(qC-F^2)+q\|h_s\|^2.
\]

Its first term is nonnegative by Cauchy–Schwarz, while its second is
strictly positive on `(0,s_0)`. Thus `P_s<0` on that interval and
`P_s<=0` thereafter. To make the deduction at an arbitrarily small
positive fitting time explicit, choose
`0<r<min(s_*,s_0)`. Strict decrease on `[r/2,r]` and the initialized
limit from the audited scalar theorem give

\[
 P(s_*)\le P(r)<P(r/2)\le1/C_0.
\]

Since `q(s_*)>0` and `F(s_*)=A>0`, this ratio is positive and may be
inverted. Cauchy–Schwarz then yields

\[
 C(s_*)\ge F(s_*)^2/q(s_*)=1/P(s_*)>C_0.
\]

The squared upper-hidden separation is `4C`, so its fitted endpoint
value is strictly larger than its initialized value. This conclusion
is stronger than merely detecting a moving hidden parameter. It is
not a claim that `C` is monotone throughout training.

## Combined conclusion, limitations, and corrections

For every reflected unit-direction pair in the stated range, the
existing exact initialized symmetry and the newly verified `C_0>0`
satisfy every hypothesis of the scalar-margin theorem. Thus for every
fixed opposite label amplitude `A>0`, including `A=1`, the actual
canonical order-one physical flow has the previously audited loss
rate `A^2 exp(-4C_0 t)`, noncollapse `C>=C_0`, finite remaining
physical path length, and complete-state convergence to a fitting
endpoint. The addendum proves strictly increased upper-hidden
separation at that endpoint. The angular separation `2 arccos(a)`
covers all of `(0,pi]`.

No mathematical correction is required in the audited ingredients.
For a self-contained combined proof, include the explicit short
`B_2(0)>0 => C_0>0` bridge and the derivative-continuity argument given
above instead of depending only on references to other route files.
These are verified expansions of the stated reasoning, not new
assumptions. Keep the regression coefficients `A,B` distinct in
notation from the label amplitude when combining the documents.

The strict initial cross sign is an additional valid result, not a
premise of the all-angle fitting theorem. No later-time cross-sign
claim from the unreviewed section 3 is used. No uniform gain or rate
near coincidence, convergence between arbitrary initial states,
arbitrary-orientation result, closure-order limit, or full-network
identification is established here. No fatal, witness-fatal, major,
or constant-level objection survives within the audited contract.
