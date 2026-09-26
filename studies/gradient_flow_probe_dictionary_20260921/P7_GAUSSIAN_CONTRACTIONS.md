# Initialized Gaussian contractions through the eighth middle-weight power

The new scalar inputs for the highest label-degree eighth-order increment
are exactly **`<U,K3>`, `<h,T>`, and `<V,V>`**, in addition to the p5
contractions `<U,U>` and `<h,V>`. The cubic output coefficient `beta` is
also needed for the lower-degree moving-residual correction. All these
constants reduce to **two-dimensional deterministic Gaussian quadrature**
after exact conditioning and Gaussian second-moment integration. No
finite-carrier pairing is substituted for a population pairing.

The next odd weight power cannot be dismissed by a common scalar-clock
argument: the initialized population cubic output correction is

```
beta_1 = 0.0534973795607894 y1^3 + 0.127655256214363 y1 y2^2,
beta_2 = 0.127655256214363 y1^2 y2 + 0.0534973795607894 y2^3.
```

These are quadrature values, not closed-form exact constants. Their unequal
coefficients mean that `beta(y)` is generally not parallel to `y`. The
calculation below exposes the corresponding distinct time-ordering slots
at weight power seven; it does not infer noncontainment from anisotropy
alone. The companion complete coefficient derivation resolves that span
question using these constants.

## Contract, scope, and claim level

Physical probes are `sqrt(2)e_a`, so normalized axes have Gram `I`.
The loss is equally weighted unhalved MSE, the initialized population
readout is zero, and `W0` and `W0*` are the two orientations of the same
initialized middle Gaussian action. All label powers below are formal
binary polynomials. Coefficient extraction fixes fields before any task
labels or training trajectory are supplied.

This audit owns only this note, `p7_gaussian_check.py`, and
`data/generated/gradient_flow_probe_dictionary_20260921/p7_gaussian01/`.
Its scientific input was restricted to the assigned study DERIVATION,
P45_DERIVATION_ROUTE, new_dictionary, new_dictionary_p45, and p45 checks,
plus the established Gaussian source/response rule in
`docs/global_nonlinear.md` C.4.7.8 (H6), §3.3, and the fixed finite-program
polynomial-envelope extension in C.4.7.10. No other study was consulted.
The investigate-conjectures and solve-math-rigorously skills governed
scope, formal claim levels, and checks. Subsequent exchange with the
independent p7 derivation was explicitly authorized by the supervisor.

The conclusions are exact finite formal identities under the initialized
Gaussian source law, and numerical checks of deterministic quadrature.
They do not establish time analyticity, population regularity to order
eight, convergence of a dictionary hierarchy, or finite-width trajectory
accuracy. The finite graph has Gaussian polynomial envelopes: tanh and
all fixed-order derivatives are bounded, and every remaining product
contains finitely many Gaussian sources. Thus all displayed moments and
Gaussian integrations by parts exist. This verifies the integrability
needed here without asserting that arbitrary products preserve a bounded
word class.

## Notation and the required contraction list

Use the p5 notation

\[
h_a=\tanh g_a,\quad Y_a=W_0h_a,\quad H_a=\tanh Y_a,\quad
\ell_a=\phi'(g_a),\quad m_a=\phi''(g_a),\quad
d_a=\phi'(Y_a),\quad e_a=\phi''(Y_a),\quad\phi=\tanh.
\]

Here `g` has independent standard Gaussian coordinates and `Y` has
independent `N(0,v)` coordinates,
`v=E tanh(G)^2`. All derivatives marked by primes refer to their scalar
argument. The ordinary Taylor coefficients needed from p5 are

\[
S=\sum_b y_bH_b,\quad U_{ab}=d_aH_b,\quad
B_2=\tfrac12\sum_b y_b(Sd_b)\otimes h_b,
\]
\[
q_a=\tfrac{y_a}{2}\ell_aW_0^*(Sd_a),\quad
V_a=\ell_aq_a,\quad
R_a=\tfrac{vy_a}{2}Sd_a+W_0V_a,
\]
\[
J=\sum_b y_bd_bR_b,\qquad
K_a=\tfrac13d_aJ+Se_aR_a,
\]
\[
B_4=\tfrac14\sum_b y_b\{K_b\otimes h_b+(Sd_b)\otimes V_b\},
\]
\[
T_a=\tfrac{y_a}{4}\ell_a^2W_0^*K_a
  +\tfrac{y_a}{4}\ell_a^2B_2^*(Sd_a)+m_aq_a^2,
\]
\[
E_a=W_0T_a+B_2V_a+B_4h_a,
\qquad N=\sum_b y_b(d_bE_b+\tfrac12e_bR_b^2),
\]
\[
K^{(5)}_a=\tfrac15d_aN+\tfrac13Je_aR_a
             +Se_aE_a+\tfrac12S\phi'''(Y_a)R_a^2,
\]
\[
B_6=\tfrac16\sum_b y_b\{K^{(5)}_b\otimes h_b+
 K_b\otimes V_b+(Sd_b)\otimes T_b\}.
\]

In these displays `B_4` and `B_6` denote their highest label-degree pieces,
not the full moving-residual coefficients. This convention is necessary
when using the following finite-order contraction audit.

The sixth lower-activation coefficient in the frozen-residual sector is
obtained as follows. Let `u_a=[t^4]g_a` and `P_a=[t^6]h_a`. Then

\[
u_a=\frac{y_a}{4}\left\{\ell_a[W_0^*K_a+B_2^*(Sd_a)]
             +m_aq_aW_0^*(Sd_a)\right\},
\]
\[
[t^6]g_a=\frac{y_a}{6}\left\{
\ell_a[W_0^*K^{(5)}_a+B_2^*K_a+B_4^*(Sd_a)]
+m_aq_a[W_0^*K_a+B_2^*(Sd_a)]
+[m_au_a+\tfrac12\phi'''(g_a)q_a^2]W_0^*(Sd_a)\right\},
\]
\[
P_a=\ell_a[t^6]g_a+m_aq_au_a+\tfrac16\phi'''(g_a)q_a^3.
\]

The sixth upper-preactivation coefficient is

\[
A_a=W_0P_a+B_2T_a+B_4V_a+B_6h_a.
\]

Writing `O=sum_b y_b[d_b A_b+e_b R_b E_b+phi'''(Y_b)R_b^3/6]`, the
new upper seventh-degree field is

\[
K^{(7)}_a=\tfrac17d_aO+\tfrac15e_aR_aN
+\tfrac13J[e_aE_a+\tfrac12\phi'''(Y_a)R_a^2]
+S[e_aA_a+\phi'''(Y_a)R_aE_a+\tfrac16\phi''''(Y_a)R_a^3].
\]

Consequently the highest degree velocity coefficient at `t^7` factors as

\[
\sum_a y_a\{K^{(7)}_a\otimes h_a+K^{(5)}_a\otimes V_a
+K_a\otimes T_a+(Sd_a)\otimes P_a\}.
\]

No dense learned correction is required to form these fields. Indeed,

\[
B_2^*K_a=\tfrac12\sum_b y_bh_b\langle Sd_b,K_a\rangle_2,
\]
\[
B_4^*(Sd_a)=\tfrac14\sum_b y_b
 [h_b\langle K_b,Sd_a\rangle_2+V_b\langle Sd_b,Sd_a\rangle_2],
\]
\[
B_2T_a=\tfrac12\sum_b y_b(Sd_b)\langle h_b,T_a\rangle_1,
\]
\[
B_4V_a=\tfrac14\sum_b y_b
 [K_b\langle h_b,V_a\rangle_1+(Sd_b)\langle V_b,V_a\rangle_1],
\]
\[
B_6h_a=\tfrac16\sum_b y_b
 [v\delta_{ab}K^{(5)}_b+K_b\langle V_b,h_a\rangle_1
 +(Sd_b)\langle T_b,h_a\rangle_1].
\]

This proves sufficiency of the stated three new contraction families for
the highest label-degree sector. Pairings with `K5` are unnecessary here.
The lower-degree seventh/eighth-order corrections require `beta`, already
expressible through `R`. Higher scalar output coefficients first multiply
initialized `H_b d_a` and `h_a` factors at these powers; after separating
those existing-span terms they need not be evaluated to form new columns.

## Exact first reverse and second forward source laws

Use a single index `i=(a,b)`, ordered `(1,1),(1,2),(2,1),(2,2)`, and write
`a(i)` for its first coordinate. Define

\[
C_{ij}=E_2[U_iU_j],\qquad
D_{ij}=E_2[\partial_{Y_j}U_i],\qquad j=1,2.
\]

The implementation calls the latter `A`; this note calls it `D` to avoid
confusing it with the sixth upper-preactivation coefficient above.
Its derivative is explicit:

\[
\partial_{Y_j}U_{ab}
 =\delta_{jb}d_ad_b+\delta_{ja}e_aH_b.
\]

The reused transpose gives

\[
Q_i=W_0^*U_i=\zeta_i+\mu_i(g),\qquad
\mu_i(g)=\sum_j h_jD_{ij},\qquad E[\zeta_i\zeta_j]=C_{ij}.
\]

The centered reverse Gaussian vector `zeta` is independent of `g`. It
must be retained: replacing `Q_i` by its response `mu_i` drops the `C`
term in every subsequent second moment.

Put `L_i=ell_(a(i))^2 Q_i` and `kappa=E ell_a^2`. When applying the
same initialized matrix again, (H6) gives

\[
W_0L_i=\xi_i+\kappa U_i.
\]

The response is `kappa U_i` because
`E_1 partial_(zeta_j)L_i=kappa delta_ij`. It is not included in the
source covariance. The forward source covariances are instead

\[
P_{ij}=E[\xi_iY_j]=E_1[L_i h_j]
 =E_g[\ell_{a(i)}^2\mu_i h_j],
\]
\[
\Sigma_{ij}=E[\xi_i\xi_j]
 =E_g[\ell_{a(i)}^2\ell_{a(j)}^2(C_{ij}+\mu_i\mu_j)].
\]

Thus `(Y,xi)` is centered Gaussian with covariance
`[[vI,P^T],[P,Sigma]]`. In particular

\[
E[\xi\mid Y]=PY/v.
\]

The two Gaussian source groups remain independent of one another. This
does not make the action answers independent: their response terms
carry precisely the reused-matrix dependencies. All matrices above are
uncentered operand second moments, never response-subtracted Grams.

Substitution gives the particularly cheap conditional upper coefficient

\[
\overline R_a(Y)=E[R_a\mid Y]
=\frac{y_a}{2}\sum_b y_b[(PY/v)_{ab}+(v+\kappa)U_{ab}(Y)].
\]

Both `R` and `K` are affine in `xi`. Hence conditional integration of
any product of `K` with a function of `Y` alone is exact by replacing
`R` by `Rbar`; no upper innovation grid is needed.

## The three new tensors and beta

For the first tensor,

\[
\langle U_{ab},K_c\rangle_2
=E_Y\left[U_{ab}\left\{\frac{d_c}{3}
 \sum_j y_jd_j\overline R_j+Se_c\overline R_c\right\}\right].
\]

For the lower Gram,

\[
\langle V_a,V_b\rangle_1
=\frac{y_ay_b}{4}\sum_{c,k}y_cy_k
 E_g\left[\ell_a^2\ell_b^2(C_{ac,bk}+\mu_{ac}\mu_{bk})\right].
\]

The term involving `C` is the conditional Gaussian second moment, not a
finite Gaussian carrier contraction.

For `<h_i,T_a>`, first set `f(g)=h_i ell_a^2` and define

\[
a_j=E_g[fh_j],\qquad b_j=E_g[fL_j]
 =E_g[f\ell_{a(j)}^2\mu_j],
\qquad c_j=b_j-(a^TP^T)_j/v.
\]

The field `W0 f` has no response because `f` contains no reverse source.
Its joint Gaussian source covariance with `Y` is `a`, and with `xi` is
`b`. Therefore conditional Gaussian multiplication gives

\[
E_2[(W_0f)K_a]
=E_Y\left[\frac{a\cdot Y}{v}\overline K_a(Y)
             +\sum_jc_j\partial_{\xi_j}K_a(Y,\xi)\right].
\tag{1}
\]

Here the named-source derivative is independent of `xi`, since `K_a`
is affine in `xi`. The derivative holds `Y`, all covariance parameters,
and all response coefficients fixed. Explicitly,

\[
\partial_{\xi_{cb}}R_a=\tfrac12\delta_{ac}y_ay_b,
\]
\[
\partial_{\xi_{cb}}K_a
=\frac{d_a}{3}\sum_j y_jd_j\partial_{\xi_{cb}}R_j
 +Se_a\partial_{\xi_{cb}}R_a.
\]

Moving the *actual* adjoint across the first term in `T_a`, and treating
its other two terms by their already displayed conditional second
moments, gives

\[
\langle h_i,T_a\rangle_1
=\frac{y_a}{4}E_2[(W_0f)K_a]
+\frac{y_a}{8}\sum_b y_b E_g[fh_b]
             \sum_{c,k}y_cy_k C_{bc,ak}
\]
\[
\hspace{12mm}
+\frac{y_a^2}{4}\sum_{b,c}y_by_c
 E_g[h_i m_a\ell_a^2(C_{ab,ac}+\mu_{ab}\mu_{ac})].
\tag{2}
\]

This is the complete contraction, including response mean products and
reverse-source variance. An independent check in the executable uses
the reverse law for `W0* K_a` directly. That law gives

\[
E_1[fW_0^*K_a]
=\sum_j E_g[fh_j]E_2[\partial_{Y_j}K_a]
+\sum_j E_g[fL_j]E_2[\partial_{\xi_j}K_a].
\tag{3}
\]

The `Y` derivative in (3) is taken at fixed named `xi`, before
conditioning. Differentiating `Kbar(Y)` instead would incorrectly add
the regression derivative `P/v`. Equation (1) and (3) agree by Gaussian
integration by parts; the code checks them independently.

Finally,

\[
\beta_a=E_Y[H_a\overline J/3+Sd_a\overline R_a],\qquad
\overline J=\sum_b y_bd_b\overline R_b.
\]

Independent sign flips and coordinate exchange imply
`beta_1=b_s y1^3+b_c y1 y2^2` and the swapped expression for `beta_2`.
These symmetries remove numerical quadrature noise in theoretical zero
slots if an implementation chooses to impose the exact symmetry. The
API reports the directly integrated tiny values, of order `1e-18`,
rather than silently pruning them.

Every expectation in this section is over two independent real Gaussian
coordinates. In particular no singular covariance inversion is needed:
the only regression denominator is `v>0`.

## Why the seventh weight power needs a separate audit

To isolate the first nonradial residual contribution, retain the part
`b_a(t)=y_a+t^3 z_a`, where `z=-beta`; common `tau` damping can be
treated separately. Let `Z=sum_a z_a H_a`. The feedback pieces at the
relevant orders are

\[
c_4=Z/4,\qquad
h_{a,5}=\frac{\ell_a^2}{5}W_0^*[(z_aS+y_aZ/4)d_a],
\]
\[
Y_{a,5}=\frac15(W_0\ell_a^2W_0^*+vI)
                 [(z_aS+y_aZ/4)d_a],
\]
\[
c_6=\frac16\sum_b(y_bd_bY_{b,5}+z_bd_bR_b).
\]

At velocity power six the upper factor paired with `h_a` therefore
contains

\[
z_aK_a+y_a[d_ac_6+(Z/4)e_aR_a+Se_aY_{a,5}].
\]

The `z_aS` and `y_aZ` slots have unequal coefficients. If `z=k y` for
a scalar `k`, this expression reduces to `(7k/4)y_a K_a`, hence adds
no new upper span. For the computed Gaussian `beta` this reduction
does not apply. This calculation independently identifies the precise
moving-residual term that must be collected before asserting any p6
count. The companion p7 derivation reports the resulting extra fields;
the source law and constants used there are those established above.

## Frozen implementation interface

`p7_gaussian_check.population_contractions(order=256)` is cached and
returns NumPy arrays with ordinary polynomial coefficients. Slot `j` of
degree `d` multiplies `y1^(d-j)y2^j`.

| Key | Shape | Meaning |
|---|---|---|
| `UK` | `(2,2,2,4)` | `<U_ab, coefficient j of K_c>` |
| `hT` | `(2,2,5)` | `<h_i, coefficient j of T_a>` |
| `VV` | `(2,2,5)` | coefficient `j` of `<V_a,V_b>` |
| `beta` | `(2,4)` | coefficient `j` of `beta_a` |
| `hV` | `(2,2,3)` | `<h_i, coefficient j of V_a>` |
| `C` | `(4,4)` | `<U_ab,U_cd>`, flattened index `2a+b` |
| `A` | `(4,2)` | `E partial_Yj U_ab`, called `D` above |
| `P` | `(4,2)` | `E L_ab h_j` |
| `LL` | `(4,4)` | `E L_ab L_cd` |

The scalar `v` uses exactly the arithmetic ordering of the inherited
256-node builder, so its stored value remains `0.3942944903978411`.
All existing p5 raw columns and their `2!,3!,4!,5!` scales must remain
unchanged. These returned tensors carry **no factorial scaling**.
They supply deterministic constants only; new coordinate fields must
still evaluate every action using the supplied initialized `W0` and its
actual transpose. The 256-node quadrature should be computed once and
reused, never fitted to finite task labels, empirical matrix Grams, or a
training trajectory.

## Bounded checks and resolution result

The numerical decision is whether deterministic contraction evaluations
agree within the fixed absolute gate `1e-9`, with independent algebra
checks below `2e-13`. The test contains no optimizer, training horizon,
or measured task performance. Its only numerical refinement changes
Gaussian integration resolution.

The initial 128/256 comparison missed the gate: its maximum discrepancy
was `2.1256582743989227e-9`. This failed result remains intact at
`p7_gaussian01/contractions.json`. The supervisor authorized one stronger
192/256 comparison at the same threshold; it passed with maximum
discrepancy `4.922569296628154e-12`. The first refined output is retained
under `refined192/`. After preserving the inherited `v` arithmetic exactly
and freezing the cached API, the final source was rerun under `final_api/`.

Final checks are:

- 192/256 maximum contraction discrepancy: `4.923e-12`, gate `1e-9`.
- Direct product Gauss–Hermite integration in two lower roots and four
  reverse innovations versus analytic Wick reduction for `<V,V>`:
  `1.388e-17`, gate `2e-13`. Three nodes in each innovation coordinate
  integrate these quadratic conditional polynomials exactly.
- Independent actual-adjoint conditioning (1) versus full reverse
  named-source response (3): error below `7e-17`, gate `2e-13`.
- Binary parity and coordinate-exchange identities for `beta`: error
  `8.327e-17`, gate `2e-13`.
- Full six-coordinate forward source covariance minimum eigenvalue:
  `0.0210785800897`, hence positive in this calculation.

The output includes source hash, NumPy version, all working tensors,
both resolution comparisons, and the failed coarse gate status. The
resolution discrepancy is a numerical consistency diagnostic, **not a
certified Gaussian quadrature error bound**. The exact mathematical
formulas above do not depend on either finite quadrature resolution.

The checks use Gaussian quadrature and exact finite polynomial identities;
they never combine empirical finite Gaussian matrix moments with an
ideal population Gram. This distinction is essential: a finite Gaussian
matrix may carry the resulting frozen functions for implementation tests,
but its row averages do not redefine the constants in these formulas.
