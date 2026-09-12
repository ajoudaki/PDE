# Bounded attempt to sign the actual family midpoint

Author: /root/harmonic_route, 2026-09-12.

**Outcome: no sign proved.** I tested a favorable readout-direction comparison
for the actual midpoint contraction and conditional averaging over both
symmetric coefficients of the unchanged family. The comparison exposes a
negative hidden-motion square, but its required force alignment and three
remaining actual-neural contractions are uncontrolled. Averaging does not
repair this inequality. The antisymmetric baseline remains in every test.

This is a bounded continuation of the frozen parity calculation, not a new
independent route, a certificate framework, or an impossibility result.
No target, coefficient interval, optimizer, initialized action, or anchor
projection was changed. No experiment or Git operation was performed.

## 1. Exact inputs

Read REFERENCE_SIGN_ATTEMPT.md (315 lines) and GEOMETRY_SIGN_FOLLOWUP.md
(351 lines) completely, including their proofs and limitations. Retained the
already completely read ROUTE_GEOMETRY.md and the frozen parity reduction.
Their hashes are:

| Input | SHA-256 |
|---|---|
| REFERENCE_SIGN_ATTEMPT.md | 6cfef322be7e9ee1d49c8287e3bfd94e6069c17ce40dfdf6619745472c1afa6f |
| GEOMETRY_SIGN_FOLLOWUP.md | 7400b12eb9655a24f8ba23af2fd41b60733947ca5fc184850d2629eafd980719 |
| ROUTE_GEOMETRY.md | e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04 |
| PARITY_SIGN_REDUCTION.md | 41767114a3d7a6dd81c519eee306f06107bc6f4ca1c538b9f751b34b499d10c1 |

The already read established reference identities in global_nonlinear.md
C.4.5.1–2 and its strong gradient/adjoint dependencies remain the scientific
foundation. No new established-source range or another current attempt was
read. The global_nonlinear.md hash is
5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483;
RESEARCH_WORKFLOW.md remains
8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12.
The required mathematical skills remain applied.

## 2. The precise attempted favorable inequality

Work at $p=1,\zeta=0$, a necessary subcase of the full robustness claim.
Use the fixed functions $\bar r,A_1,A_3,S_1,S_3$ from the parity report.
For an actual antisymmetric residual
$A=\bar r-xA_1-yA_3$, retain its effective signed measure
$\mu_A=A\rho-\sum_a(\beta_A)_a\delta_{e_a}$, and similarly for each
$S_i$. Write $b_f=\Pi\int f g\,d\rho$ and
$H_f[z,z']=\int\mathcal H_u[z,z']\,d\mu_f(u)$.
All these are the full raw quantities with the actual adjoint.

The mixed coefficient is

$$
\Gamma(A,S):=3\mathcal T(A,S,S)
     =H_A[b_S,b_S]+2H_S[b_A,b_S].
\tag{F1}
$$

The favorable comparison tested was $b_A\approx-\Pi e_c$, where
$e_c=(0,0,c_\dagger)$. This approximation was not assumed.
Set $n=GM^{-1}(1,-1)^T$, $a=\Pi e_c=e_c-n$, and keep its exact discrepancy
$e_A=b_A+a$. The readout identity
$H_S[b_S,e_c]=\|(b_S)_h\|^2$ then gives

$$
\Gamma(A,S)=-2\|(b_S)_h\|^2+\mathfrak R(A,S),
$$
$$
\mathfrak R(A,S)=H_A[b_S,b_S]
       +2H_S[e_A,b_S]+2H_S[n,b_S].
\tag{F2}
$$

At the original midpoint, $A=\bar r-(R/32)A_3$ and $z=3R/32$.
Its cubic is $\mathcal C_1(A)+z^2\Gamma(A,S_1)$.
The desired strict midpoint inequality is therefore equivalently

$$
\mathfrak R(A,S_1)+\frac{\mathcal C_1(A)}{z^2}
                  <2\|(b_{S_1})_h\|^2.
\tag{F3}
$$

I could not prove (F3). Each failure is specific:

* The discrepancy is
  $e_A=(b_{\bar r}+\Pi e_c)-x b_{A_1}-y b_{A_3}$.
  Reachability gives no alignment of $b_{\bar r}$ with $-\Pi e_c$.
  Small task coefficients do not make the fixed first term small.
* The normal contribution is the actual
  $2H_S[g_B,b_S]/B_s$. Reference monotonicity signs its denominator,
  not this numerator. Discarding it would violate the fitted anchors.
* $H_A[b_S,b_S]$ includes the actual signed bulk residual, anchor
  multipliers, and both tanh curvature terms. It is not a positive or
  negative Hessian merely because $A$ is antisymmetric.
* $\mathcal C_1(A)$ has not been signed. Division by $z^2$ in (F3)
  makes explicit why an uncontrolled antisymmetric baseline cannot be
  suppressed by small symmetric coefficients.

Full-gradient injectivity gives $b_S\ne0$, but supplies no positive lower
bound on its hidden block $\|(b_S)_h\|$. Thus even the isolated square lacks
the needed hidden-block coercivity. Norm bounds and Young's inequality can bound the remaining
terms in absolute value, but supply neither the small alignment error nor
the favorable baseline required by (F3).

This test does not assert that the discrepancy or any remainder is large
in the actual network. It identifies the signed domination that has not
been established.

## 3. Averaging both symmetric coefficients does not close the test

Keep the exact domain inherited from the original four independent intervals:

$$
|x|\le R/32,\quad R/48\le y\le R/24,\quad
L(x):=R/16+|x|\le z\le U(x):=R/8-|x|,
$$
$$
|w|\le d(y):=\min(y-R/48,R/24-y).
\tag{F4}
$$

For the auxiliary uniform average over the original coefficient box,
conditioning on interior $x,y$ makes $z$ uniform on $[L,U]$ and $w$
uniform on $[-d,d]$, independently. This average changes no training law.
Both symmetric coefficients genuinely vary there. Their moments are

$$
m_1=\mathbb E z^2=(3R/32)^2+(R/16-2|x|)^2/12,\qquad
m_3=\mathbb E w^2=d(y)^2/3,\qquad \mathbb E zw=0.
$$

Thus averaging removes the off-diagonal coefficient but leaves exactly

$$
\mathbb E_{z,w}\mathcal C_1(r)
=\mathcal C_1(A)+m_1\Gamma(A,S_1)+m_3\Gamma(A,S_3).
\tag{F5}
$$

The attempted averaged version of (F3) requires
$\mathcal C_1(A)+\sum_{i\in\{1,3\}}m_i\mathfrak R(A,S_i)
<2\sum_{i\in\{1,3\}}m_i\|(b_{S_i})_h\|^2$.
It has the same uncontrolled alignment, normal, and baseline terms.
Moreover $m_3$ vanishes at permitted endpoints of the $y$ interval; uniform
coercivity cannot be inferred simply from two components varying in the
interior.

There is a direct check that the averaging does not manufacture a square.
Following REFERENCE_SIGN_ATTEMPT.md, put
$k_f=\int H_u\,d\mu_f$ and $U_f=Dk_f$, holding $\mu_f$ fixed for this
derivative. Then $b_f=(U_f^*c,k_f)$. Expanding (F1), one averaged readout
contribution is

$$
2\langle k_A,\mathcal P c\rangle,\qquad
\mathcal P=\sum_{i\in\{1,3\}}m_iU_{S_i}U_{S_i}^*\succeq0.
\tag{F6}
$$

Positivity of $\mathcal P$ does not sign this cross pairing:
$k_A$ is the task-and-anchor feature integral, not $c$.
The other readout cross terms and fixed-readout hidden Hessians remain.
Replacing $k_A$ by $c$ would change the actual contraction.

Finally, a negative conditional average would not by itself prove a uniform
negative sign on the original box. Both signs of $w$ are present, so a
uniform upper bound must retain the worse off-diagonal contribution
$2|q_{12}(x,y)|z|w|$ from the frozen parity reduction. No value or sign
of the average in (F5) was obtained.

## 4. What actual reference reachability contributes

The exact history $c_\dagger=\int_0^{s_\dagger}h(s)\,ds$ turns (F6) into
$2\int\langle k_A,\mathcal P h(s)\rangle\,ds$.
The positive readout acceleration $c_{ss}=J(s)J(s)^*c(s)$ does not sign
these task-weighted cross-time pairings. The explicit PSD-acceleration
countercheck in REFERENCE_SIGN_ATTEMPT.md shows why that inference alone
is invalid; it is not a counterexample to the actual neural sign.

The reference fitting identities establish the anchor level and positive
$B_s$. They do not identify $\mu_A$ with the reference's fixed anchor
contrast measure. Such an identification would remove its non-atomic
residual and change (F1). Likewise the saturation balances are integrated
against signed $\mu_A,\mu_{S_i}$ and correlated backward fields, so their
pointwise scalar signs do not supply the missing inequalities.

The attempt therefore ends at the same actual midpoint contraction,
without signing either of its terms. No favorable sign for the affine
quadratic form on (F4), no sign on the full family, and no beneficial
relative component conclusion has been obtained. The exact obstacle for
this attempted argument is (F3), or its averaged counterpart, including
the antisymmetric baseline. No general impossibility statement follows.

Checks performed: retained the sign and factor three in (F1); reconstructed
the projected-readout subtraction in (F2); checked the midpoint scaling;
derived the conditional distribution from the exact original intervals;
expanded the averaged readout term in (F6); and compared each desired
inequality with the actual reference history and anchor identities.
No actual tensor value or trajectory was numerically evaluated.
