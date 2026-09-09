# Polynomial affine geometry and capped primal comparison

This is a new theoretical note for the exact raw metric and initialization in
`studies/mean_field_peeling/two_sample_odd_activation_theorem`. It changes no
algorithm. All constants below are uniform for `a in [1/2,1]`, all binary label
pairs, and `|rho| <= 1-delta`. It proves a polynomial restriction for the affine
comparison, endpoint, and nonaffinity parts. It does **not** prove a polynomial
restriction for the source-response construction.

## 1. Exact normalization of the active affine problem

Use the notation of AFFINE_CORE.md: `v=v_u=(1+tau_label rho)/2`,
`r=sqrt(v)`, `P_1=w dot u`, and `sigma=y_1`. Define

\[
 p=P_1/r,\qquad D=\sigma C,\qquad
 \lambda=a^3r,\qquad t=\lambda s,
 \qquad F=\langle D,BAp\rangle.
\]

Here `s` is the original feature time and `t` is only an auxiliary time in this
note. In particular `g=lambda F`, and

\[
 \frac{\sqrt\delta}{8\sqrt2}\le\lambda\le1.
\]

The first raw metric on active increments becomes exactly `||dp||_2^2`:
`d ||dw||_2^2 = ||dP_1||_2^2/v = ||dp||_2^2` for increments parallel to `u`.
All first-layer directions perpendicular to `u` are constant in the affine
flow. In normalized time its four equations are exactly

\[
 \dot p=A^*B^*D,\quad
 \dot A=B^*D\otimes p,\quad
 \dot B=D\otimes Ap,\quad
 \dot D=BAp.                                                   \tag{1}
\]

The four component spaces carry the `L2`, HS, HS, `L2` metrics. The canonical
initialization has

\[
 \|p_0\|=1,\quad \|A_0\|,\|B_0\|\le10,\quad D_0=0,
 \quad\|B_0A_0p_0\|=1.                                       \tag{2}
\]

The last equality is the initial Gaussian forward norm identity already in
the existing affine proof. No finite random readout is reset: (1) describes
the zero population limit of that readout, as in the original construction.

## 2. Exact balance identities and their consequences

Put `c=||D||`. Differentiating bounded-operator identities in (1) gives

\[
 BB^*-D\otimes D=B_0B_0^*,
\]
\[
 AA^*-B^*B=A_0A_0^*-B_0^*B_0,
\]
\[
 A^*A-p\otimes p=A_0^*A_0-p_0\otimes p_0.                    \tag{3}
\]

There are no traces of infinite-dimensional identity operators in this
argument. Scalar differentiation also gives

\[
 \|p\|^2=1+c^2,\qquad \frac d{dt}c^2=2F.                    \tag{4}
\]

The first two balances imply

\[
 \|B\|^2\le100+c^2,\qquad \|A\|^2\le200+c^2.              \tag{5}
\]

The first and third balances, using positivity of the initialized Gram
operators and `||p_0||=1`, give the more useful lower bounds

\[
 \|B^*D\|^2=c^4+\langle D,B_0B_0^*D\rangle\ge c^4,
\]
\[
 \|Ap\|^2=\|p\|^4+\langle p,(A_0^*A_0-p_0\otimes p_0)p\rangle
 \ge\|p\|^4-\|p\|^2=c^2(1+c^2).                            \tag{6}
\]

Because (1) is gradient ascent for `F`,

\[
 \dot F=\|BAp\|^2+\|B^*D\|^2\|p\|^2
       +c^2\|Ap\|^2+\|A^*B^*D\|^2
 \ge2c^4(1+c^2).                                           \tag{7}
\]

In particular `F>=0`. Equations (4) and (7), with zero initial values, imply

\[
 F^2\ge\frac23c^6+\frac12c^8,
 \qquad F\ge c^4/\sqrt2.                                   \tag{8}
\]

For a direct verification without division at `c=0`, the derivative of the
difference on the first line is
`2F [dot F-2c^4(1+c^2)] >= 0`.

The existing radial argument specializes to `D''=J J* D`, where `J` is the
hidden derivative of `BAp`. Thus `c` is convex, with initial right slope one
by (2). Consequently

\[
 c(t)\ge t,\qquad \dot c=F/c\ge c^3/\sqrt2\quad(t>0).       \tag{9}
\]

## 3. Duration, norm, and integrated curvature bounds

Let `T` be the first normalized-time hit of `F=3/(2lambda)`, and set

\[
 M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\]

Before this hit, (8) gives `c<=M`. If the hit has not occurred before `c=1`,
that level is reached by time one, and (9) bounds the remaining duration by
`sqrt2 integral_1^M c^{-3} dc`. Therefore

\[
 T<2,\qquad S=T/\lambda\le2/\lambda,
 \qquad \sup_{t\le T}c(t)\le M.                            \tag{10}
\]

These also prove existence through the hit. Indeed, before it all four
vector-field components are bounded by a constant depending on `M`, by (5),
so their raw increments have a strong limit at a finite maximal endpoint.
Local polynomial-field existence continues the solution there. An unbounded
branch below the target contradicts (9) and the bound `c<=M`.

The same change of variable yields

\[
 \int_0^T c^2\,dt\le1+\sqrt2\log M,
 \quad
 \int_0^T(200+c^2)\,dt\le401+\sqrt2\log M.                 \tag{11}
\]

The contribution before `c=1` is at most one. Afterwards use
`dt/dc<=sqrt2/c^3`.

All affine primal norms used in the original proof are bounded by

\[
 R(t)=\sqrt{200+c(t)^2}.                                   \tag{12}
\]

For the first sample projections, `Q_1` is constant and
`z_i^1= +/- (r p +/- Q_1)`. Since `||Q_1||=sqrt(1-r^2)`, Cauchy--Schwarz
already gives `||z_i^1||<=sqrt(2+c^2)<=R`; the stronger existing Gaussian
orthogonality identity is unnecessary here.

The full raw displacement is also `O(M)`, not just the operator displacement.
For example, before `c=1`, both `||dot A||HS` and `||dot B||HS` are at most
201 and the duration is at most one. After `c=1`, each is at most
`c(200+c^2)`, whose time integral is at most

\[
 \sqrt2\int_1^M(200/c^2+1)\,dc\le\sqrt2(200+M).
\]

Thus each learned HS increment is at most `500 M`. The first raw increment
is `||p-p_0||<=3M` and `||D||<=M`, giving the convenient sum bound `1100 M`.
This verifies strong continuation with constants uniform in the input
dimension.

For the affine objective in the original raw metric, its Hessian has
zero diagonal blocks and six pairs of cross blocks. Each cross block has
norm at most `lambda R^2`: it is the product of the other two factors of
`lambda <D,BAp>`. In the sum of the four component norms, its operator norm
is at most `3lambda R^2`. The same bound holds on the full raw first-layer
space, because projection onto the normalized `u` direction is a contraction
and the affine objective annihilates the orthogonal directions. Hence

\[
 \int_0^S\|\nabla^2g(\Theta_0(s))\|\,ds
 \le1203+3\sqrt2\log M.                                  \tag{13}
\]

The affine variational propagator is therefore polynomial in `1/lambda`.
Crucially, the factor `lambda` in the Hessian is retained. A bound on the
unscaled Hessian by a polynomial primal radius would lose this conclusion.

## 4. Full raw comparison with the original capped nonlinear field

Fix any cap. Let `Theta_e` be its original feature-time path for
`phi(z)=az+e atan z`, and `Theta_0` the affine path with the same `a`. Use
the sum norm of the original raw first-layer increment, two HS increments,
and readout. Let `E(s)=||Theta_e(s)-Theta_0(s)||_sum`. Stop at `E=1` if that
occurs, and put

\[
 b(s)=R(\lambda s)+1.
\]

Every state on the line between the two paths has all relevant primal
norms at most `b`. This includes the normalized active first coordinate `p`:
raw first-layer distance bounds its difference with constant one. No
symmetry or affine inactive-field identity is imposed on `Theta_e`.
The affine field depends only on `p,A,B,D`, even on those nonsymmetric
nearby states.

The existing term-by-term, cap-uniform same-state comparison remains valid:

\[
 \|V_{a,e,Rcap}(\Theta)-V_{a,0}(\Theta)\|_{sum}
 \le40e b^3.                                               \tag{14}
\]

It uses only `|atan|<=pi/2`, `|phi'-a|<=e`, and `|tau_Rcap(q)|<=|q|`.
Thus an odd divided-difference estimate, though available, is not needed
to gain the essential `lambda` in the stability coefficient. Subtract the
affine fields after making (14), rather than differentiating the nonlinear
field. This gives the integral/Dini inequality

\[
 E'\le3\lambda b^2 E+40e b^3.                              \tag{15}
\]

Since `R>=sqrt(200)>14`,

\[
 b^2\le(7/6)(200+c^2),\quad
 \int_0^S3\lambda b^2ds\le(7/2)(401+\sqrt2\log M)
 \le1404+5\log M.                                        \tag{16}
\]

Also `b^2<=235 M^2` and `b^3<=3600 M^3`. Gronwall and `S<=2/lambda` now give

\[
 E(s)\le288000\exp(1404)e\lambda^{-1}M^8
       =C_0 e\lambda^{-3},
 \qquad C_0=1296000\exp(1404).                             \tag{17}
\]

Consequently the explicit restriction

\[
 0\le e\le\min\{1/2,\lambda^3/(2C_0)\}                  \tag{18}
\]

closes the tube with `E<=1/2` and gives capped strong existence/comparison
through the entire affine endpoint. In delta-only form it is sufficient
that

\[
 e\le\frac{\delta^{3/2}}{2C_0(8\sqrt2)^3},
 \qquad
 E(s)\le C_0(8\sqrt2)^3 e\delta^{-3/2}.                   \tag{19}
\]

The proof is cap uniform. It gives continuous population capped paths, and
bounded-mesh versions follow by discrete variation of constants and then
mesh refinement. A separate source-response bound is still required to
remove caps with the desired probabilistic/tail properties.

## 5. Forward and scalar endpoint estimates

Directly expanding the actual forward equations on the tube yields

\[
 \|z_{i,e}^1-z_{i,0}^1\|\le E,
\]
\[
 \|z_{i,e}^2-z_{i,0}^2\|\le2b E+(\pi/2)e b,
\]
\[
 \|z_{i,e}^3-z_{i,0}^3\|\le3b^2 E+\pi e b^2.               \tag{20}
\]

For example the last line follows by bounding the propagated second-layer
difference by `b` times its norm, the `B`-difference term by `E R^2`, and
the third-layer arctangent term by `(pi/2)e b`. Because `b>=1`, the stated
bound dominates their sum. Combining (17), `b^2<=235 M^2`, and
`M^2<1.5lambda^{-1/2}`, gives the convenient uniform bound

\[
 \max_{i,\ell,s\le S}\|z_{i,e}^\ell-z_{i,0}^\ell\|
 \le C_z e\lambda^{-7/2},\qquad C_z=1500 C_0.              \tag{21}
\]

For the scalar prediction, same-state forward comparison gives
`||h_e^3-h_0^3|| <= (pi/2)e(b^2+b+1)`. Therefore
`|g_e(Theta_e)-g_0(Theta_e)| <= 5e b^3`.
For the affine state difference retain its exact coefficient:
`|g_0(Theta_e)-g_0(Theta_0)| <= lambda b^3 E`.
Together these imply

\[
 |g_e(S)-3/2|\le C_g e\lambda^{-11/4},
 \qquad C_g=14400 C_0.                                    \tag{22}
\]

Indeed `b^3<=3600M^3`, `lambda E+5e<=2C_0e lambda^{-2}`,
and `M^3=(3/sqrt2)^{3/4}lambda^{-3/4}<2lambda^{-3/4}`.
Their product is bounded by the displayed constant.
It is enough to require `e<=lambda^{11/4}/(4C_g)` for endpoint margin `1/4`.

## 6. Absolute Gaussian variance and nonaffinity margins

The apparent degeneration of the affine marginal variance with `delta` is
also removable. Radial convexity gives `||BAp||=||dot D||>=dot c>=1`.
Together with (5) and (6), this implies

\[
 \|Ap\|^2\ge\max\{c^2(1+c^2),(100+c^2)^{-1}\}\ge1/101.     \tag{23}
\]

For the last inequality split at `c^2=1`. The existing affine Gaussian
construction and frozen inactive-field orthogonality now give, for both
samples,

\[
 \operatorname{Var}(z_i^1)=v\|p\|^2+(1-v)\ge1,
\]
\[
 \operatorname{Var}(z_i^2)=a^2\{v\|Ap\|^2+(1-v)\}\ge1/404,
\]
\[
 \operatorname{Var}(z_i^3)=a^4\{v\|BAp\|^2+(1-v)\}\ge1/16. \tag{24}
\]

Thus every affine marginal is `sigma G` with `sigma>=m_*:=1/sqrt(404)`,
independently of `delta`, and no upper variance bound is needed for the
following nonaffinity estimate.

Let `H_3(G)=G^3-3G` and `h(sigma)=E[atan(sigma G)H_3(G)]`. Gaussian integration
by parts, with integrable polynomial bounds justifying differentiation,
gives

\[
 h(\sigma)=-2\sigma^3 E\frac{G^2}{(1+\sigma^2G^2)^2},
 \qquad
 h'(\sigma)=-2\sigma^2 E\frac{G^4}{(1+\sigma^2G^2)^2}<0.     \tag{25}
\]

For the derivative, first differentiate under the expectation and then use
`E[G^4 k(G)]=3E[G^2 k(G)]+E[G^3 k'(G)]` with
`k(G)=(1+sigma^2G^2)^{-1}`. For the first identity use
`E[H_3 f]=E[(G^2-1)f']` and then
`E[(G^2-1)k]=E[G k']`.

Since `H_3` is orthogonal to both `1` and `G` and has squared norm six,
Cauchy--Schwarz gives

\[
 \mathcal R(\sigma G)\ge h(\sigma)^2/6\ge h(m_*)^2/6.
\]

On `|G|<=1`, the standard normal density is at least
`exp(-1/2)/sqrt(2pi)`, so

\[
 E[G^2\mathbf1_{|G|\le1}]\ge
       \frac{2\exp(-1/2)}{3\sqrt{2\pi}}.
\]

Equation (25) consequently proves the explicit absolute lower bound

\[
 \mathcal R(\sigma G)\ge\eta_*:=
 \frac{4\exp(-1)}{27\pi}\frac{m_*^6}{(1+m_*^2)^4}
 =\frac{4\cdot404\exp(-1)}{27\pi\,405^4}>0
 \qquad(\sigma\ge m_*).                                  \tag{26}
\]

The square root of this regression residual is 1-Lipschitz in `W_2`. Here is
a self-contained verification. An optimal slope for regressing `atan Z` on
`Z` lies in `[0,1]`, by

\[
 \operatorname{Cov}(Z,\arctan Z)
 =\tfrac12E[(Z-Z')(\arctan Z-\arctan Z')]
 \in[0,\operatorname{Var}(Z)],
\]

where `Z'` is an independent copy. At zero variance choose slope zero.
For every `beta in [0,1]`, `z -> atan z-beta z` is 1-Lipschitz, since its
derivative is between `-beta` and `1-beta`. Using either variable's optimal
intercept and slope as a competitor for the other therefore proves

\[
 |\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
 \le\|Z-Z_0\|_2.                                         \tag{27}
\]

Equations (21), (26), and (27) preserve at least half of the square-root
margin, and hence `R(z_e)>=eta_*/4`, whenever

\[
 e\le\frac{\sqrt{\eta_*}}{2C_z}\lambda^{7/2}.              \tag{28}
\]

For a completely explicit delta-only restriction, define

\[
 c_*:=\min\left\{\frac12,
 \frac1{2C_0(8\sqrt2)^3},
 \frac1{4C_g(8\sqrt2)^{11/4}},
 \frac{\sqrt{\eta_*}}{2C_z(8\sqrt2)^{7/2}}\right\}>0.
\]

Then

\[
                  0<e\le c_*\delta^{7/4}                 \tag{29}
\]

simultaneously implies the tube restriction (18), endpoint margin `1/4`
from (22), and nonlinear regression margin `e^2 eta_*/4`. This follows from
`lambda>=sqrt(delta)/(8sqrt2)` and
`delta^{7/4}<=delta^{3/2},delta^{11/8}` on `(0,1]`.
Thus a polynomial coefficient restriction with exponent `7/4` suffices for
**all primal affine comparison, endpoint, and nonaffinity work**. For the
convex mixture take `a=1-e`; all estimates are uniform in that choice.

This improves the earlier exponent `13/4`, which unnecessarily used the old
`delta`-dependent lower variance bound. The change uses the already proved
inactive-field freezing and Gaussianity, without strengthening the model.

## 7. Why the original feature time cannot be logarithmic

The normalized-time argument also locates the necessary growth. While
`c<=1`, (5) and (4) give
`||dot D||<=sqrt(101*201*2)<202` and `F<202c`. If `lambda<=1/200`, the target
`3/(2lambda)` exceeds 202, so the flow must first reach `c=1`, which takes
normalized time at least `1/202`. Hence

\[
 S\ge\frac1{202\lambda}\qquad(\lambda\le1/200).            \tag{30}
\]

For `c>=1`, the same product bounds give `F<202c^4`, so its terminal readout
also satisfies `c(T)>[3/(404lambda)]^{1/4}` for small `lambda`. Thus the
rates `S=O(lambda^{-1})` and `c=O(lambda^{-1/4})` are sharp up to constants
from this model's initial bounds. The mechanism that permits a polynomial
comparison is integrated curvature, not logarithmic original feature time.

## 8. Exact remaining limitation

The old source threshold contains `exp(36P^2 S)` and a second chronological
response Gronwall `exp(KS)`. Merely inserting (10) and the improved primal
radius into those expressions still gives nonpolynomial smallness.
Equation (13) identifies a polynomial affine *raw variational propagator*,
which may permit a stronger source-program response argument. Such an
argument must identify the actual chronological source resolvent, including
both action orientations, learned-memory terms, and current transpose
returns. No equivalence of that resolvent with (13) is proved here.
Consequently this note does not certify polynomial `theta_delta` for the
complete theorem, cap removal, uniqueness, or finite GF/GD limits.
