# Targeted geometry follow-up: readout balance and tanh saturation

Status: **the balance route does not determine the actual-neural sign**.
The exact constrained readout identity contains a positive squared-motion term
and two unbounded-in-sign anchor-curvature contributions. Tanh's saturation
defect has a pointwise sign but is integrated against signed task/anchor
controls and correlated backward fields. Neither mechanism proves a favorable
next term in the symmetry-cancelled diagnostic, or a negative endpoint cubic
for the fixed ordinary family. This is an obstruction to these particular
sign arguments, not a counterexample or no-go theorem for E₀.

This is the final bounded adaptive follow-up to frozen `ROUTE_GEOMETRY.md`,
SHA-256 `e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04`.
That file is unchanged. The task family remains exactly its (G1)–(G3).
No other route, new task family, experiment, or numerical source calculation
was used. Statements below use the same raw metric, full first rows, actual
Gaussian action and adjoint, anchor projection, and selected physical-GF
limit as the frozen report. All prediction integrals are angular pullbacks.

## 1. Separate the readout and hidden equations without freezing controls

Write `x_h=(w,K)` for the two hidden raw blocks and `H_u=H^2_theta(u)`.
At the current state define the signed finite measure

\[
\mu_\tau(du)=r_\tau(u)p(u)d\rho(u)
                  -\sum_{a=1}^2\beta_{\tau,a}\delta_{e_a}(du),
\quad
\beta_\tau=M_\theta^{-1}G_\theta^*
                     \int r_\tau(u)g_\theta(u)p(u)d\rho(u). \tag{B1}
\]

It is a signed force measure, not a new training probability. Put

\[
h_\mu=\int H_u\,d\mu(u),\qquad
J_\mu z_h=\int DH_u[z_h]\,d\mu(u),\qquad
b=\int g_\theta(u)d\mu(u)=\Pi_\theta v_r.
\]

Here `DH_u` is the bounded strong directional map into the upper `L2` space;
its adjoint is the actual first-row/middle adjoint formula. Thus

\[
b_c=h_\mu,\qquad b_h=J_\mu^*c,\qquad
c'=-2h_\mu,\qquad x_h'=-2J_\mu^*c. \tag{B2}
\]

These are exact. All coefficients of `mu_tau`, including anchor multipliers,
continue to evolve. Differentiating the readout equation yields

\[
c''=4J_\mu J_\mu^*c-2h_{\mu'},
\qquad
\langle c,c''\rangle
=4\|b_h\|^2-2\langle c,h_{\mu'}\rangle. \tag{B3}
\]

For this differentiation, `r'=-2K_tau r`, NSC28 differentiates the two-by-two
anchor inverse, and the strong derivatives in the frozen report §5 give
continuous raw `b'`. Therefore `mu'` exists as a finite-variation measure
derivative and `c''` exists strongly in `L2`. No third raw derivative is used.
The product rule is obtained by differentiating the finite-variation
coefficients separately from the strong feature derivative and applying
the bounds in NSC25–NSC28.

The feature-clock reference has constant signed coefficients. For that
specific equation the second term is absent and the familiar positive
`J J*` readout acceleration is valid. In the constrained square-loss episode
the second term is generally present. More explicitly, because the anchor
predictions stay at `y=(1,-1)`,

\[
-2\langle c,h_{\mu'}\rangle
 =4\int f_\theta(u)(\mathsf K_\tau r_\tau)(u)p(u)d\rho(u)
                  +2\beta_\tau'\!\cdot y. \tag{B4}
\]

The known nonnegativity of `K_tau` concerns its quadratic form on one common
function. It does not give a sign for the cross pairing with `f_theta` in
(B4), or for `beta' dot y`. Thus importing the reference's positive `J J*`
term alone would omit actual square-loss and anchor feedback.

## 2. Exact endpoint identity in the symmetry-cancelled diagnostic

This section uses a diagnostic residual `r=r_S` symmetric under coordinate
swap, with `p=1`, at the actual reference endpoint. It does not propose the
trained-prediction-dependent target `F_*-r_S` as an E₀ family.

All symbols in this section are at the endpoint. Let

\[
\Phi_\mu(\theta)=\int f_\theta(u)d\mu(u),\qquad
H_\mu[z,z']=\int\mathcal H_u[z,z']d\mu(u),\qquad
h_A(b,b)=(\mathcal H_{e_1}[b,b],\mathcal H_{e_2}[b,b]). \tag{B5}
\]

The measure in (B5) is held fixed solely while taking its displayed scalar
derivatives. Its gradient is `b`; its directional Hessian is the polarization
of (G12). Every direction used below is a finite-variation combination of
actual gradients, or the bounded readout direction, so the `L4` first-row
and bounded-readout hypotheses of that formula hold.

Let `e_c=(0,0,c_dagger)`, its normal projection `n=G M^{-1}y`, and its
tangent projection `a=Pi e_c=e_c-n`. The equality `G*e_c=y` follows from
linearity in the readout and exact anchor fitting. Readout linearity gives
the useful positive mixed derivative

\[
H_\mu[b,e_c]
 =\langle c_\dagger,J_\mu b_h\rangle
 =\|b_h\|^2. \tag{B6}
\]

However, `e_c` is not an admissible anchor-preserving direction: it changes
the anchor predictions by `y`. For the actual tangent direction one instead
has

\[
H_\mu[b,a]=\|b_h\|^2-H_\mu[b,n]. \tag{B7}
\]

The second term in (B7) is an actual reference contraction, not a nuisance
parameter or a removable coordinate convention.

Here is an exact acceleration calculation that also displays the second
anchor term. At fixed `r`, differentiating the vector `Pi v_r` in direction
`b` gives

\[
\partial_b(\Pi v_r)=-G M^{-1}h_A(b,b)+\Pi H_\mu b. \tag{B8}
\]

To check this, write `v_r=b+G beta`. Differentiating the projector on its
tangent argument gives `-GM^{-1}(partial_b G)*b`, whose anchor vector is
`h_A(b,b)`. Differentiating it on `G beta` gives `-Pi(partial_b G)beta`.
Combining that with `Pi partial_b v_r` is exactly `Pi H_mu b`. This
derives (B8) without an ambient twice-differentiable manifold theorem.

Now include the actual residual derivative. With `D` as in (G5),

\[
b'=-2\mathsf D\mathsf K r-2\Pi H_\mu b+2G M^{-1}h_A(b,b),
\]
\[
\theta''=4\mathsf D\mathsf K r+4\Pi H_\mu b-4G M^{-1}h_A(b,b). \tag{B9}
\]

The reference-fixing raw swap isometry sends `b` for a symmetric residual
to `-b`; it fixes `e_c`. The frozen prediction kernel preserves symmetric
functions, so `D K r` lies in that same negative raw sector. Hence
`<e_c,D K r>=0` in the diagnostic. Equations (B7)–(B9) then prove

\[
\left.\frac{d^2}{d\tau^2}\|c(\tau)\|_2^2\right|_{0}
=8\left\{\|b\|^2-H_\mu[b,n]
                       -y^TM^{-1}h_A(b,b)\right\}. \tag{B10}
\]

The first readout-norm derivative is zero by the same symmetry. Both adverse
terms in (B10) are quadratic in the forcing `r_S`; neither is excluded by
symmetry. In particular the positive term in (B6) is not a proof of positive
constrained readout-norm acceleration, much less a risk advantage.

The exact reference balance makes the unresolved numerator more explicit.
Define the anchor contrast
`B(theta)=(f_theta(e1)-f_theta(e2))/2` and let `g_B=G y/2`. At the endpoint
the feature-clock reference equation is `theta_s=g_B`, with
`B_s=||g_B||²>0`. Swap symmetry makes `M` have equal diagonal entries, so
`My=2B_s y`. Consequently

\[
n=g_B/B_s,\qquad y^TM^{-1}h_A(b,b)=H_B[b,b]/B_s,
\]
\[
\left.\frac{d^2}{d\tau^2}\|c(\tau)\|_2^2\right|_0
=8\left\{\|b\|^2-
             \frac{H_\mu[b,g_B]+H_B[b,b]}{B_s}\right\}. \tag{B11}
\]

Thus the established reference monotonicity verifies the positive denominator
only. It leaves the sum of two mixed actual-neural Hessian contractions.
Neither is a squared norm. The `H_B` term is the normal acceleration required
to keep the fitted anchor contrast fixed while the hidden/readout state moves.
The `H_mu[b,g_B]` term couples the added-force Hessian to the reference fitting
direction. Equation (G12) supplies their full first-row, middle, and readout
integrands; no available inequality relates their sum to `B_s ||b||²` with
the sign needed in (B11).

For a general member of (G1)–(G3), the exact version of (B10) also contains
`8<e_c,D K r>`. There is no parity cancellation of this term. Even a positive
answer to the readout diagnostic would therefore require another signed
argument on the actual baseline family, and would still concern a hidden
state observable rather than the full prediction-risk comparison.

## 3. Tanh saturation gives signed identities, not a favorable inequality

Put

\[
\chi(z)=\tanh z-z\operatorname{sech}^2z.
\]

It is odd, `chi(0)=0`, and
`chi'(z)=2z tanh(z) sech²(z)>=0`. Therefore `z chi(z)>=0` and `|chi(z)|<=1`.
This is the exact Euler homogeneity defect of tanh.

The middle action is not Hilbert–Schmidt, so a formal derivative of
`||A||HS²` would be inadmissible. A finite renormalized quantity nevertheless
exists on these reached curves. Each middle velocity is a finite-variation
integral of rank-one operators with integrable trace norm. Hence `K` is
trace-class from the original reference start through the selected episode.
Its trace-norm bound follows from
`||delta(u) tensor H1(u)||trace=||delta(u)||2 ||H1(u)||2` and the finite
accumulated control mass. Define

\[
\mathcal A=\|K\|_{HS}^2+2\operatorname{Tr}(A_0^*K). \tag{B12}
\]

The trace pairing is well defined because `A_0` is bounded. Approximation by
the finite rank sums in the integral, together with the same rank subtraction
bound in trace norm, proves
`Acal'=2 Tr(A* K')`. This is a finite difference of middle-block squared
norms, not a norm asserted for the initialized population action.

Substitute the actual controls (B1) in the three parameter equations.
The exact saturation balances are

\[
\frac d{d\tau}(\|c\|^2-\mathcal A)
     =-4\int\langle c,\chi(Z^2(u))\rangle\,d\mu_\tau(u), \tag{B13}
\]
\[
\frac d{d\tau}(\mathcal A-\|w\|^2)
     =-4\int\langle Q(u),\chi(w\cdot u)\rangle\,d\mu_\tau(u). \tag{B14}
\]

For (B13), the two derivatives are respectively
`-4 int<c,phi(Z2)>dmu` and
`-4 int<c phi'(Z2),A H1>dmu`; subtract and use `AH1=Z2`.
For (B14), the row derivative is
`-4 int<(w.u)phi'(w.u),Q(u)>dmu`. Apply the actual adjoint to the
middle derivative and subtract. These manipulations use bounded `chi`,
integrable controls, and `L2` fields, so they require no extra tail or
higher-derivative assumption.

The scalar inequality `z chi(z)>=0` cannot be applied to either right side:
the multipliers are `c` and `Q`, respectively, rather than the corresponding
preactivation; neither multiplier is known to have its preactivation's sign
coordinatewise. Also `mu_tau` is signed and contains the exact fitted-anchor
subtraction. These correlations and weights are part of the actual model.
They are not eliminated by full-circle density or by the positive gradient
Gram. At the pure symmetric endpoint the two first derivatives vanish by
symmetry, so these balances provide no uncancelled positive leading term.

The hidden curvature terms of (G12) exhibit the same obstruction directly:
`phi''(z)=-2 tanh(z) sech²(z)` changes sign with `z`, and its integrals
have the signed effective force and readout/backward weights. Passing to a
higher derivative is not a pointwise-sign remedy: the exact scalar formula
`phi'''(z)=2 sech²(z)(3 tanh²(z)-1)` has both signs even at nonnegative `z`.
This scalar observation is not an assertion that the population predictor
has the corresponding third time derivative.

## 4. What would be needed after the symmetry cancellation

The frozen report proves `K'_0` and its continuous drift, giving
`Delta E=o(t²)` for pure symmetric forcing. It does not prove `K''_0` or
an evaluated second-order kernel remainder. No next integer-order risk term
is claimed for the actual population path here.

There is a useful conditional algebra check on any smooth realization where
these additional derivatives do exist. Write `K=K_0`, `H=K'_0`, `J=K''_0`.
Successive differentiation of `r'=-2K_tau r` gives

\[
\Delta E'''(0)=-48\langle r,KHr\rangle+4\langle r,Jr\rangle. \tag{B15}
\]

For verification, `E''=16<r,K²r>-4<r,Hr>`. Differentiate this identity,
substitute `r'=-2Kr`, and use self-adjointness to get
`E'''=-64<r,K³r>+48<r,KHr>-4<r,Jr>`; the frozen third derivative is its
first term alone. In the pure symmetric diagnostic `K` preserves the parity
sector and `H` switches it, so `<r,KHr>=0`. If `D''` additionally exists,

\[
\Delta E'''(0)=8\{\|D'_0r\|^2+\langle b,D''_0r\rangle\}. \tag{B16}
\]

This follows by twice differentiating `K=D*D`. It isolates the tempting
positive square and the remaining signed contraction. Equations (B15)–(B16)
are conditional calculus identities only. Neither the existence nor the
sign of their last contraction has been established for the actual
population model. Readout linearity (B6), the constrained balance (B11), and
the saturation identities (B13)–(B14) do not remove it. In particular, writing
only the square in (B16) would omit a term of the same order.

Returning to the fixed ordinary family, put `r=r_A+r_S` at `p=1`. The actual
antisymmetric component contains `F_*-q_0` and the antisymmetric parts of
the independently varying coefficients. The already proved exact cubic is

\[
\mathcal C_1(r)=c(r_A,r_A,r_A)+3c(r_A,r_S,r_S). \tag{B17}
\]

The pure symmetric diagnostic has both terms zero only because `r_A=0`.
It gives no sign for either term at the actual baseline. In particular,
small `R` controls the added symmetric perturbation, but it does not make
`F_*-q_0` smaller than a favorable higher-order contribution. No evaluated
bound for that baseline or for the sign in (B17) was derived by the balance
calculation. Density perturbations additionally remove the exact orthogonal
swap-sector cancellations. Their robustness cannot be concluded before a
strict base margin is known.

## 5. Conclusion, scope, and provenance

The substantive new identities are (B10)–(B11) and (B13)–(B14). They show
exactly why two plausible sign arguments fail:

1. The positive readout/hidden mixed Hessian is in a direction that changes
   the fitted anchors. Its tangent correction and the required normal
   acceleration leave the two signed contractions in (B11).
2. Tanh saturation produces homogeneity-defect integrals against the actual
   signed control and correlated backward fields. Pointwise saturation
   positivity does not give a sign for those integrals.

Accordingly no analytic sign mechanism from this targeted balance route
survives to prove E₀. The actual remaining endpoint obligation is still the
negative sign of (G13), equivalently the terms in (B17) at uniform density,
on the fixed ordinary family. The relative-component sign and quantitative
remainder remain separate after that. The hypothetical next-order diagnostic
would require additional regularity and the signed contraction in (B16),
neither supplied by the balances.

No new scientific files were read beyond the frozen route and its previously
authorized sources. Their detailed complete read scopes and source hashes
remain those recorded in frozen report §7. At follow-up startup, the frozen
route, contract, workflow, and `docs/global_nonlinear.md` hashes were checked
and unchanged. Repository status was inspected only for shared-write safety;
no other artifact's scientific content was opened. This report alone was
written; the original report, established files, shared notes, and Git index
were preserved.

Checks performed: direct reconstruction of the projector derivative and
normal/tangent decomposition (B8); independent readout differentiation
(B3)–(B4) agreeing with (B10); the anchor Gram symmetry and factor of two
in (B11); actual rank/adjoint substitutions in the saturation balances; and
the conditional loss-derivative calculation (B15). No source or training
experiment, symbolic tool, new external theorem, or independent review was
used. The result is a frozen partial research follow-up, not internally
checked by another reviewer or promoted.
