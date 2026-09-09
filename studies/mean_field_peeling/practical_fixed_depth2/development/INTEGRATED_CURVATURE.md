# Integrated curvature: exact cancellation, an improved orthogonal-input cap, and the remaining obstruction

2026-09-08. This is a theoretical follow-up to `ENERGY_ROUTE.md` and
`CAVITY_ROUTE.md`, for the activation and actual architecture in
`../CONTRACT.md`. No experiments or external results are used. The canonical
action and its genuine adjoint are retained throughout.

**Established:** a width-independent signed integral bound for the sum of the
two troublesome curvature forms along the actual finite GF velocity; an exact
bounded integrating factor for first-layer curvature when the inputs are
orthogonal; and, in that orthogonal-input case, global energy-dissipating
approximations which require only the readout-velocity cap. There is also an
exact upper-field balance identity for both physical and energy-capped paths.
For any nonorthogonal input pair, no smooth positive row-state metric near
zero can cancel all sample incoming coefficients simultaneously, even if the
metric is allowed to be curved.

**Not established:** a comparison estimate between arbitrary physical or
capped trajectories for the contract's general input Gram, cap removal, or
the requested global population and actual finite-width limits. In particular,
the velocity-direction integral below does not control general tangent
directions. The nonorthogonal-input calculation explains precisely why the
scalar fast-crossing cancellation does not immediately extend.

## 1. Setup and the exact troublesome quadratic form

Use the notation of `ENERGY_ROUTE.md`: the raw Hilbert state is
`Theta=(w,U,C)`, `A=A0+U`, `z_i=w dot u_i`, `h_i=phi(z_i)`,
`v_i=A h_i`, `b_i=C phi'(v_i)`, and `q_i=A* b_i`. Write

\[
p(s)=\phi'(s)=\tfrac34+\tfrac14\operatorname{sech}^2s,
\qquad \ell(s)=\frac{p'(s)}{p(s)}.
\]

Thus `3/4 <= p <= 1`, `|p'| <= 1/2`, and
`-log(4/3) <= log p <= 0`. The function `ell` tends to zero at both
infinities, but is nonconstant.

For a raw variation `xi=(xi_w,xi_U,xi_C)`, define

\[
Z_i=\xi_w\cdot u_i,\qquad
V_i=\xi_Uh_i+A[p(z_i)Z_i].
\]

At every finite width the following Hessian identity is exact:

\[
\begin{split}
D^2E[\xi,\xi]
={}&\sum_i(Df_i[\xi])^2+\mathcal B(\Theta;\xi)
       +\mathcal C(\Theta;\xi),\\
\mathcal B(\Theta;\xi)
={}&2\sum_i r_i\left\{
 \langle\xi_C,p(v_i)V_i\rangle
 +\langle b_i,\xi_U[p(z_i)Z_i]\rangle\right\},\\
\mathcal C(\Theta;\xi)
={}&\sum_i r_i\left\{
 \langle C\phi''(v_i),V_i^2\rangle
 +\langle q_i\phi''(z_i),Z_i^2\rangle\right\}.
                                                        \tag{1}
\end{split}
\]

This follows by differentiating `f_i=<C,phi(A phi(z_i))>` twice:
the mixed `C` variation gives the first term in braces in `B`; the mixed
`U,h` variation gives the second; and the two activation second derivatives
give `C`. All finite inner products in (1) are normalized, with the raw
matrix variation measured in Frobenius norm.

Suppose a path lies in a fixed raw ball and its residual norm is bounded.
Put `a=||A||op`, `c=||C||2`, `H=max_i ||h_i||2`, and
`K=max_i ||phi(v_i)||2`. These quantities have uniform bounds on that ball.
For `L_v=H+a` and `L_f=K+c L_v`,

\[
\|V_i\|_2\le L_v\|\xi\|,
\quad |Df_i[\xi]|\le L_f\|\xi\|,
\quad |\mathcal B(\Theta;\xi)|
 \le2\|r\|_1(L_v+c)\|\xi\|^2.                         \tag{2}
\]

For the last bound use `||xi_U||op<=||xi_U||HS`, bounded gates,
and Cauchy--Schwarz. Thus only `C` in (1) resists an ambient raw quadratic
bound. These formulas do not assert an ambient twice Frechet differentiable
population loss: products such as `C V_i^2` need not be integrable for
arbitrary population `L2` directions.

## 2. A genuine integrated bound along the physical velocity

Let `Theta_n` be any actual finite-width raw GF on `[0,T]`, with its actual
small Gaussian initial readout. Suppose its initial loss, initial raw
primal norms, and initialized operator norm are bounded by specified
constants. The finite energy identity then puts every path on this interval
in one common raw ball. Consequently all constants in (2), the residuals,
and `||g||=||nabla E||` have bounds independent of width.

The finite smooth gradient equation gives

\[
\frac{d}{dt}\frac12\|g(t)\|^2
 =-D^2E[g(t),g(t)],\qquad \dot\Theta=-g.                \tag{3}
\]

The same quadratic form is obtained at `g` and `-g`. Substituting (1),

\[
\begin{split}
\int_0^t\mathcal C(\Theta(s);\dot\Theta(s))\,ds
={}&\frac12\bigl(\|g(0)\|^2-\|g(t)\|^2\bigr)\\
 &-\int_0^t\sum_i(Df_i[\dot\Theta])^2\,ds
  -\int_0^t\mathcal B(\Theta;\dot\Theta)\,ds.           \tag{4}
\end{split}
\]

The two integrals on the right have absolute values at most

\[
\left(3\sup_{s\le T}L_f(s)^2
 +2\sup_{s\le T}\{\|r(s)\|_1(L_v(s)+c(s))\}\right)E(0),
                                                               \tag{5}
\]

because `integral ||dot Theta||^2 <= E(0)`. Also
`||g|| <= ||r||1 L_f`. Equations (4)--(5) give

\[
\sup_{t\le T}\left|
 \int_0^t\mathcal C(\Theta_n(s);\dot\Theta_n(s))\,ds
 \right|\le K_T,                                      \tag{6}
\]

with `K_T` independent of width on the stated initial event. This is an
actual physical-trajectory estimate. It needs neither pointwise incoming
field bounds nor estimates of their tails.

Its limitations are precise. It bounds the signed primitive of the **sum**
of the two activation-curvature terms, in the actual velocity direction.
It does not bound their absolute integrals, their negative parts separately,
or their values on a general tangent or difference. In particular the
identity for a variational solution `J'=-Dg J`,

\[
\frac{d}{dt}\|J\|^2=-2D^2E[J,J],
\]

does not yield a bound for `J`: using its endpoint norm as an input would be
circular. The velocity is one variational solution, associated with time
translation; (6) controls that one solution only. No population limit of the
separate curvature integrals is asserted.

For the existing energy caps, write `dot Theta=-P(Theta)g` at a finite width,
where `P` is the positive block multiplier from `ENERGY_ROUTE.md`. Direct
differentiation instead gives

\[
E''=2D^2E[\dot\Theta,\dot\Theta]-\langle g,\dot P g\rangle.
                                                               \tag{7}
\]

The term involving `dot P` has no sign supplied by the cap construction.
Thus (6) is not silently transferred to those capped velocities.

## 3. Exact first-layer cancellation for orthogonal inputs

Assume in this section that the three unit inputs are orthogonal. Let

\[
\psi(s)=\int_0^s\frac{da}{p(a)},\qquad y_i=\psi(z_i).
                                                               \tag{8}
\]

The map `psi` is a smooth increasing bijection, with derivative in `[1,4/3]`.
Its inverse has derivative in `[3/4,1]`. In particular

\[
\|z-\bar z\|_2\le\|y-\bar y\|_2
 \le\tfrac43\|z-\bar z\|_2.                            \tag{9}
\]

The component of `w` perpendicular to the input span is fixed. Hence (9)
is an equivalence of the changing first-layer raw norm and its transformed
norm, at finite width and on the population space. Gaussian initialization
is mapped to a well-defined `L2` field since `|psi(s)|<=4|s|/3`.

For true GF and for the existing scalar first-row cap respectively,

\[
\dot z_i=-r_iq_i p(z_i),\quad \dot y_i=-r_iq_i;
\qquad
\dot z_i=-r_i H_R(q)_i p(z_i),\quad
\dot y_i=-r_i H_R(q)_i.                                \tag{10}
\]

These are exact path identities. The transformed feature map

\[
\alpha(y)=\phi(\psi^{-1}(y))
\quad\hbox{satisfies}\quad
\alpha'(y)=p(\psi^{-1}(y))^2\in[9/16,1].                \tag{11}
\]

Consequently no lower incoming multiplier appears in the direct
first-layer gate difference in these coordinates.

Here is the corresponding scalar integrating factor. If
`z'=-a(t)p(z)`, then

\[
a(t)p'(z(t))=-\frac{d}{dt}\log p(z(t)),\qquad
\left|\int_s^t a(u)p'(z(u))\,du\right|\le\log(4/3).
                                                               \tag{12}
\]

No monotonicity of `z` is required. If its linearized equation is
`eta'=-a p'(z) eta-p(z) delta a`, the quotient rule gives

\[
\frac{d}{dt}\frac{\eta}{p(z)}=-\delta a.               \tag{13}
\]

In the homogeneous equation the amplification is exactly
`p(z(t))/p(z(s))`, between `3/4` and `4/3`. This removes the apparent
large integrated `q phi''` coefficient, even with repeated crossings.
For the cap, `a_i=r_i H_R(q)_i`; since `H_R` is 1-Lipschitz, differentiating
this product introduces no incoming maximum through the cap derivative.
The dependence of `q` on the top gate remains and is treated next.

### A global cap family with no first-layer cap in this case

For each `R`, define the following equations in the transformed coordinates:

\[
\dot y_i=-r_iq_i,\qquad
\dot U=-\sum_i r_i b_i\otimes h_i,\qquad
\dot C=-\tau_R\left(\sum_i r_i\phi(v_i)\right),
\quad h_i=\alpha(y_i).                                 \tag{14}
\]

These preserve the true first-layer and middle-matrix updates after (8) is
undone; only the readout velocity is capped. For construction on `[0,T]`,
replace `C` by `tau_M(C)` in `b,q`, with `M=1+2RT`, while retaining true
forward predictions and the stated readout update.

This extension is locally Lipschitz on the raw transformed Hilbert space.
Indeed (11) controls the forward gate. On a primal ball the top backward
gate has the estimate

\[
\|\tau_M(C)p(v)-\tau_M(\bar C)p(\bar v)\|_2
 \le\|C-\bar C\|_2+M\|v-\bar v\|_2.                   \tag{15}
\]

Apply the bounded genuine adjoint to get a corresponding `q` difference.
The product `r_i q_i` then has an `L2` Lipschitz bound since `r_i` is a
scalar, `q_i` has a primal-ball `L2` bound, and residual differences have a
raw Lipschitz bound. The rank update and capped readout have the same
estimates as in `ENERGY_ROUTE.md`. Thus the complete field is locally
Lipschitz with constant `K_{B,T}(1+R)`; no lower incoming cap was needed.

Picard iteration gives a local strong solution. Starting from `C(0)=0`,
the readout equation implies `|C(t)|<=2Rt<M` pointwise, so the extension is
inactive. In the original raw coordinates the exact chain rule gives

\[
E'=-\|g_w\|^2-\|g_U\|^2
       -\langle g_C,\tau_R(g_C)\rangle
 \le-\|\dot\Theta\|^2.                                \tag{16}
\]

Thus the raw displacement is at most `sqrt(T E(0))`. Equivalence (9)
also bounds the transformed displacement. Every field norm is bounded on
this ball independently of `R`: use bounded actions and gates, linear
growth of `alpha`, and `|tau_R(s)|<=|s|`. A hypothetical finite maximal
endpoint is consequently an `L2` Cauchy endpoint. Its readout retains the
pointwise bound under `L2` convergence, so local existence continues the
path. This proves existence on `[0,T]`. The same local uniqueness and
pointwise bound identify constructions with different horizons on their
overlap, giving one global path for each `R`.

At finite width the actual nonzero random readout is retained. Replace
`M` by `2+2RT` on the event `||C_n(0)||infinity<=1`; the extension remains
inactive there. The exceptional probability is at most `2n exp(-n^2/2)`.
The actual finite version of (14) also has direct global continuation from
(16), without requiring this event.

There is a useful improvement in the cap comparison. With distance measured
in `(y,U,C)`, the asymmetric top-gate split using `|C_R|<=2RT` yields, for
`S>=R`,

\[
\|\dot X_R-\dot X_S\|
 \le K_T(1+R)\|X_R-X_S\|
 +\|g_{C,S}\mathbf1_{|g_{C,S}|>R}\|_2.                 \tag{17}
\]

There is **no `q` tail defect** in (17), since both first-layer updates are
uncapped in (14). Equation (17) follows from (15), the genuine adjoint,
and the scalar cap comparison; it does not presume tail control for `q`.
It still needs a sufficiently strong uniform tail estimate for `g_C` to
remove the remaining cap. No such estimate is proved here. Also,
orthogonal inputs are a proper subclass of the contract, not a replacement
for its general Gram.

## 4. Why the endpoint cancellation fails for a general input Gram

For fixed sample coefficients `a_i=r_i q_i`, the first-layer vector fields
on the input span are

\[
X_i(w)=p(w\cdot u_i)u_i.
\]

Their Lie bracket, with convention `[X_i,X_j]=DX_j X_i-DX_i X_j`, is

\[
[X_i,X_j]
=\Gamma_{ij}\{p(z_i)p'(z_j)u_j-p(z_j)p'(z_i)u_i\}.
                                                               \tag{18}
\]

For independent, nonorthogonal `u_i,u_j` it is nonzero on an open set.
A smooth coordinate change that made all these fields constant would make
their brackets zero, since the chain rule preserves the displayed bracket
and constant fields have zero bracket. Thus no such simultaneous flattening
exists there. This refutes only that coordinate construction.

The signed curvature trace makes the obstruction more explicit. Assume
temporarily that `Gamma` is invertible. Since

\[
\dot z=-\Gamma\operatorname{diag}(p(z))a,
\qquad M=\sum_i a_i p'(z_i)u_i\otimes u_i,
\]

and `||u_i||=1`,

\[
\operatorname{tr}M
=-\sum_{i,j}\ell(z_i)(\Gamma^{-1})_{ij}\dot z_j.
                                                               \tag{19}
\]

Define the one-form

\[
\vartheta=\sum_{i,j}\ell(z_i)(\Gamma^{-1})_{ij}\,dz_j.
                                                               \tag{20}
\]

For `Gamma=I`, (20) is `d sum_i log p(z_i)`, recovering (12).
For the admissible block Gram

\[
\Gamma=\begin{pmatrix}1&\rho&0\\\rho&1&0\\0&0&1\end{pmatrix},
\qquad 0<\rho<1-\delta,
\]

its restriction to the first two variables has exterior derivative

\[
d\vartheta
=-\frac{\rho}{1-\rho^2}
   [\ell'(z_1)-\ell'(z_2)]\,dz_1\wedge dz_2.           \tag{21}
\]

This is not identically zero: `ell'(0)=-1/2`, while `ell'(s)->0` as
`s->infinity`. For completeness, the integral of the nondiagonal part of
(20) around the rectangle `[a,b] x [c,d]`, counterclockwise, is

\[
-\frac{\rho}{1-\rho^2}
\{(d-c)[\ell(b)-\ell(a)]
 -(b-a)[\ell(d)-\ell(c)]\}.                            \tag{22}
\]

Choosing short intervals near points with different `ell'` makes (22)
nonzero by the definition of a derivative. The diagonal part has zero
closed-loop integral. Hence signed curvature can accumulate on a closed
bounded path; decay of `phi''` does not make (19) an endpoint difference.

There is an exact controlled-path interpretation, useful only as a test of
the proposed estimate. Prescribe such a closed absolutely continuous `z`
path and take
`a=-diag(p(z))^{-1} Gamma^{-1} z'`. It is a solution of the first-layer
equation with these external coefficients. Its homogeneous variational
matrix satisfies `J'=-M J`, and differentiating its determinant gives

\[
\log\det J(T)=-\int_0^T\operatorname{tr}M\,dt
             =\oint\vartheta.                         \tag{23}
\]

Choose orientation so this is positive and repeat the loop `N` times.
The logarithmic determinant grows linearly with `N` although the path's
range is unchanged. For one row of dimension three, the operator norm is
at least the cube root of this determinant. Thus there is no universally
bounded integrating factor based only on the range and the scalar decay
of `phi''` for these general controlled first-layer fields.

This is **not** an actual training trajectory and is **not** a
counterexample to the contract. The control `a=rq` has not been produced
by the genuine adjoint, middle update, and physical residual. It identifies
the missing ingredient: those physical relations would have to prevent
the accumulated nonexact part of (20), or bound it in the actual difference
directions. A primitive depending only on preactivation endpoints cannot
provide that ingredient for a general Gram.

### No smooth positive local metric can cancel all the lower coefficients

There is a stronger obstruction than failure of flat coordinates. Assume
some pair of inputs is nonorthogonal. The contract's strict separation
ensures that this pair is linearly independent. There is **no** `C2`
positive definite matrix metric `N(w)`, defined near `w=0`, for which every
sample field `X_i` is an infinitesimal isometry. Uniform equivalence to the
Euclidean metric is not needed for this impossibility.

The precise condition and proof are as follows. For an externally prescribed
coefficient vector `a(t)`, the lower equation and its homogeneous variation
are

\[
\dot w=-\sum_i a_iX_i(w),\qquad
\dot\eta=-\sum_i a_i DX_i(w)\eta.
\]

Differentiation of the candidate squared norm gives

\[
\frac{d}{dt}[\eta^TN(w)\eta]
=-\sum_i a_i\eta^T\{(X_i\cdot\nabla)N
                  +DX_i^TN+N DX_i\}\eta.              \tag{M1}
\]

Cancellation for every choice of the sample coefficients therefore requires

\[
(X_i\cdot\nabla)N+DX_i^TN+N DX_i=0\quad\hbox{for all }i.
                                                               \tag{M2}
\]

This is the Killing equation for these fields, not a requirement that the
metric be flat.

Here is a direct local contradiction, without an assumption about the
Lie algebra of isometries. At zero, the activation satisfies

\[
p(0)=1,\qquad p'(0)=0,\qquad p''(0)=-\tfrac12.
\]

Thus `X_i(0)=u_i`, `DX_i(0)=0`, and
`D_{u_j}DX_i(0)=-(Gamma_ij/2) u_i u_i^T`.
Differentiate (M2) in the constant direction `u_j` and evaluate at zero.
Terms containing `DX_i(0)` vanish, giving

\[
D_{u_j}D_{u_i}N(0)
-\frac{\Gamma_{ij}}2
 \{u_i u_i^T N(0)+N(0)u_i u_i^T\}=0.                  \tag{M3}
\]

Exchange `i,j` and subtract. The mixed derivatives agree because `N` is
`C2`, and `Gamma_ij=Gamma_ji`. For a nonzero `Gamma_ij` this implies

\[
S N(0)+N(0)S=0,\qquad S=u_i u_i^T-u_j u_j^T.           \tag{M4}
\]

The real symmetric matrix `S` is nonzero because the two unit inputs are
not parallel. Hence it has a real nonzero eigenvalue `lambda` and a
corresponding real vector `e`. Taking the quadratic form of (M4) on `e`
gives `2 lambda e^T N(0)e=0`, contrary to positive definiteness. This
proves the assertion. It applies also when the full three-input Gram is
singular; only one independent nonorthogonal pair was used.

Geometrically, (18) vanishes at zero but its derivative is
`(Gamma_ij/2)(u_i u_i^T-u_j u_j^T)`. This is a nonzero symmetric
linearization with real eigenvalues. A Killing field vanishing at a point
would have a skew-adjoint linearization in that point's positive metric.
Equations (M3)--(M4) are the direct calculation of this incompatibility.

Allowing a smooth metric `N(t,w)` does not change the obstruction if the
requirement is to remove every incoming coefficient: differentiation adds
`eta^T partial_t N eta` to (M1), while each coefficient still multiplies
the same expression in (M2), at every fixed time. A smooth local squared
distance with a positive definite quadratic expansion on its diagonal
would similarly induce a metric satisfying (M2) if it were invariant under
all these sample flows, so merely replacing a norm by such a distance does
not evade this particular obstruction.

The scope matters. A metric depending on the **entire actual network
state**, or on its physical past, need not satisfy (M2): its derivative
through other state variables can contribute additional terms correlated
with `r_i q_i`. Such a metric is not excluded. Nor are nonsmooth distances
or estimates for only the actually reached coefficients. The contradiction
rules out exact cancellation by a smooth positive row-state metric for
arbitrary sample coefficients; it is not a nonexistence result for the
physical GF or its canonical limit.

## 5. Exact upper-layer balance, including the lower return

Write `P_i=r_i b_i=r_i C p(v_i)` and `H_ia=<h_i,h_a>`.
For a true path define `chi=1`; for the energy cap of `ENERGY_ROUTE.md`,
define `chi=chi_R(Q)` pointwise on the first layer. Direct differentiation
of `v_i=A h_i` gives

\[
\dot v_i=-\sum_a\mathcal L_{ia}P_a,\qquad
\mathcal L_{ia}
=H_{ia}I+\Gamma_{ia} A M_{\chi p(z_i)p(z_a)}A^*.
                                                               \tag{24}
\]

Here `M_m` denotes multiplication by the real bounded function `m`.
The first term in (24) comes from the exact rank update of `A`; the second
is the genuine lower-layer return. The readout cap does not alter (24).

On the direct sum of the three upper-layer spaces, `L` is bounded,
self-adjoint, and positive semidefinite. To check the last statement, for
`s=(s_1,s_2,s_3)` its quadratic form is

\[
\sum_{i,a}H_{ia}\langle s_i,s_a\rangle
 +\int_{\Omega_1}\chi\left|
       \sum_i p(z_i)(A^*s_i)u_i\right|^2\ge0.          \tag{25}
\]

The first term is nonnegative since `H` is a feature Gram, and the second
is a square. Bounded slopes, `0<chi<=1`, and bounded primal/action norms
give a cap-independent operator-norm bound. Positivity in (25) does not
give pointwise positivity of any particular return field.

Separating just the pointwise self term in (24), set

\[
\begin{split}
B_i={}&-\sum_{a\ne i}H_{ia}P_a
 -\sum_a\Gamma_{ia}A M_{\chi p(z_i)p(z_a)}A^*P_a,\\
\dot v_i={}&-H_{ii}r_i C p(v_i)+B_i.                  \tag{26}
\end{split}
\]

Every `B_i` has a cap-independent `L2` bound on a raw ball. On any interval
where `H_ii` stays strictly positive, (26) yields the pointwise identity

\[
r_i C\phi''(v_i)
=-\frac1{H_{ii}}\frac{d}{dt}\log p(v_i)
 +\frac{\ell(v_i)}{H_{ii}}B_i.                         \tag{27}
\]

For finite width, an absolutely continuous test direction `V_i(t)` can be
inserted in (27) and integrated exactly:

\[
\begin{split}
\int_s^t\langle r_i C\phi''(v_i),V_i^2\rangle\,du
={}&-\left[\left\langle\log p(v_i),
                   \frac{V_i^2}{H_{ii}}\right\rangle\right]_s^t\\
&+\int_s^t\left\langle\log p(v_i),
               \frac{d}{du}\frac{V_i^2}{H_{ii}}\right\rangle du\\
&+\int_s^t\left\langle\ell(v_i)B_i,
                         \frac{V_i^2}{H_{ii}}\right\rangle du.
                                                               \tag{28}
\end{split}
\]

The boundary term is controlled by `log(4/3)` and the endpoint quadratic
norms. The second term requires variation control of the direction. The
last still contains an `L2` multiplier against its square. An `L2` bound
on `B_i` and on `V_i` does not bound `integral |B_i| V_i^2`; that would,
for example, require an additional suitable `L4` bound on `V_i`.
Consequently (28) has not removed the key multiplication obstruction.
Discarding the second term in (26) would wrongly discard the order-one
tagged return identified in `CAVITY_ROUTE.md`.

No global lower bound for `H_ii` is presumed in this argument. Initially
it is positive, and (27)--(28) are valid on any interval with a stated
positive lower bound. If that bound is unavailable, (24)--(26) remain the
unconditional identities, and division by `H_ii` is not justified.

## 6. Coupled feature coordinates: a coercive comparison and its exact defect

This last test concerns actual pairs of physical paths, not just the
velocity direction. Work on an interval where both feature Grams have
smallest eigenvalue at least a specified `lambda>0`. This condition holds
locally whenever the starting feature Gram is positive definite; it is
not asserted globally from initialization alone.

Let `T_h:R3 -> H1` have columns `h_i`, and write
`H=T_h* T_h`, `P_h=T_h H^{-1}T_h*`. Let `V:R3 -> H2` have columns
`v_i`, and define `U_perp=U(I-P_h)`. There is the exact reconstruction

\[
U=(V-A_0T_h)H^{-1}T_h^*+U_\perp,
\qquad U_\perp T_h=0.                                 \tag{C1}
\]

Thus `(w,V,U_perp,C)` are valid bundle coordinates on this region; the
constraint on `U_perp` moves with `w`. No fixed complement is substituted
for that constraint.

For a tangent, let `delta T_h` have columns `p(z_i)Z_i`, and let
`B=delta V-A delta T_h`. Orthogonal decomposition of `delta U` on the
domain `P_h H1` and its complement gives the exact raw metric

\[
\begin{split}
\|\delta\Theta\|^2={}&\|\delta w\|^2+\|\delta C\|^2
 +\|\delta U_\perp+U\delta P_h\|_{\rm HS}^2\\
 &+\operatorname{tr}(B^*B H^{-1}).                    \tag{C2}
\end{split}
\]

Indeed `delta U T_h=B`, so its component on `P_h H1` is
`B H^{-1}T_h*`. Its component on the complement is
`delta U(I-P_h)=delta U_perp+U delta P_h`. Those components are
Hilbert--Schmidt orthogonal and the first has squared norm
`tr(B*B H^{-1})`, proving (C2).

On any bounded primal region with `H>=lambda I`, differentiation of the
explicit formula for `P_h` bounds `||delta P_h||op` by a constant times
`||delta w||2`. Formula (C2) is therefore uniformly equivalent to the
product tangent norm in these coordinates. The same statement holds for
finite differences of two states in this region: use (C1), the Lipschitz
activation, and
`H^{-1}-bar H^{-1}=H^{-1}(bar H-H)bar H^{-1}`.
Consequently, putting `s_i=psi(v_i)` with (8),

\[
\mathscr D(\Theta,\bar\Theta)^2
=\|w-\bar w\|^2+\|C-\bar C\|^2
 +\|U_\perp-\bar U_\perp\|_{\rm HS}^2
 +\sum_i\|s_i-\bar s_i\|_2^2                          \tag{C3}
\]

is a genuine coercive two-state comparison functional there: upper and
lower bounds by the squared raw distance have constants depending only on
the primal bounds, `||A0||op`, and `lambda`. This establishes coercivity,
not its required evolution estimate.

The remaining evolution defect can be written exactly. In the direct sum
of the upper-layer spaces, let `D` multiply component `i` by `p(v_i)`;
let `a_i=r_i C`; and use the physical operator `L` of (24), with `chi=1`.
Then `P=D a` has components `r_i b_i`, and

\[
\dot s=-B a,\qquad B=D^{-1}\mathcal L D.              \tag{C4}
\]

For the second physical path use bars. Set `R=D bar D^{-1}`, a diagonal
multiplication operator whose coefficients lie in `[3/4,4/3]`. Direct
multiplication, without differentiation, gives

\[
B-\bar B
=\bar D^{-1}(\mathcal L-\bar{\mathcal L})\bar D
 +D^{-1}[\mathcal L,R]\bar D,
\quad [\mathcal L,R]=\mathcal L R-R\mathcal L.
\]

Therefore the exact difference equation is

\[
\frac{d}{dt}(s-\bar s)
=-B(a-\bar a)
 -\bar D^{-1}(\mathcal L-\bar{\mathcal L})\bar P
 -D^{-1}[\mathcal L,R]\bar P.                         \tag{C5}
\]

The first term is bounded in `L2` by a constant times the raw state
distance: `a_i-bar a_i=(r_i-bar r_i)C+bar r_i(C-bar C)`, and residual
differences have a raw Lipschitz bound. Most of the second term has the
same bound. To isolate its exception, expand, for
`m_ia=p(z_i)p(z_a)`,

\[
\begin{split}
A M_{m_{ia}}A^*-\bar A M_{\bar m_{ia}}\bar A^*
={}&(A-\bar A)M_{m_{ia}}A^*
 +\bar A M_{m_{ia}}(A-\bar A)^*\\
 &+\bar A M_{m_{ia}-\bar m_{ia}}\bar A^*.
\end{split}
\]

The first two terms, and the feature-Gram difference in `L-bar L`, have
the required operator estimates. The last term applied to `bar P` is
exactly

\[
\mathcal R_{{\rm low},i}
=\sum_a\Gamma_{ia}\bar A\left[
 \{p(z_i)p(z_a)-p(\bar z_i)p(\bar z_a)\}
       \bar r_a\bar q_a\right].                      \tag{C6}
\]

This preserves the genuine returned lower field. The corresponding upper
defect is the commutator `D^{-1}[L,R]bar P` in (C5). The multipliers
`R-I` are bounded pointwise and Lipschitz in the preactivation difference,
but only its `L2` size is supplied by (C3). A bounded operator `L` does not
bound this commutator on `bar P` by `||R-I||2 ||bar P||2`.
Likewise (C6) contains a lower gate difference multiplied by an `L2`
returned field. A raw `L2` difference estimate for that product is the
same missing multiplication estimate, now in feature coordinates.

The upper contribution to the derivative of (C3) accordingly contains the
two exact terms

\[
-2\left\langle s-\bar s,
 \bar D^{-1}\mathcal R_{\rm low}
       +D^{-1}[\mathcal L,R]\bar P\right\rangle.       \tag{C7}
\]

Although `L` is positive and self-adjoint, its commutator with the
self-adjoint multiplier `R` is skew-adjoint, which gives no sign in
(C7): the two arguments are `s-bar s` and `bar P`, not the same vector.
The bounded local self-multiplication part of `L` commutes with `R`;
sample mixing and the genuine returned operators need not do so.

For comparison, at finite width differentiating (C4) at a single state
produces precisely the same structure. If `Lambda` multiplies component `i` by
`ell(v_i) delta v_i`, then

\[
\delta\dot s
=-B\delta a-D^{-1}(\delta\mathcal L)D a
  +[\Lambda,B]a.
\]

The gate part of `delta L` is the linearization of (C6), while the last
term is the linearization of the commutator in (C5). Thus passing from
finite differences to tangents does not remove either defect.

Finally, preserving (C2) as the comparison metric is just preserving the
original raw metric under a coordinate change; its tangent derivative
reproduces the two curvature forms in (1). Using the product functional
(C3) gives an alternative coercive functional but leaves (C7), together
with the lower-coordinate and moving-complement evolution terms. The
identity `dot U_perp=-U dot P_h` retains the latter exactly, since the
rank update satisfies `dot U(I-P_h)=0`.

No cancellation of (C7) with those other block terms has been established,
and no sign or bound for (C7) follows from the available primal and energy
bounds. This ends this particular coupled-coordinate branch. It does not
exclude a different whole-state or history-dependent metric using further
properties of actual physical paths.

## 7. Claim boundary and exact remaining work

The energy identity does yield one integrated curvature estimate on actual
physical trajectories, namely (6). Scalar first-layer fast crossing has
the stronger exact cancellation (12)--(13), and for orthogonal inputs it
gives the improved global cap construction (14)--(17). These are proved
results at their stated scopes.

For the contract's general Gram, a scalar endpoint primitive misses the
nonexact form (20); a smooth positive row-state metric cannot cancel every
incoming coefficient either, by (M1)--(M4). At the upper layer the exact balance introduces the
genuine returned field `B_i` in (26), whose raw `L2` bound cannot control
the quadratic pairing in (28) on arbitrary raw directions. The known
energy bound and scalar curvature decay do not supply either missing
estimate.

A full resolution therefore still needs a proved estimate exploiting
physical reachability and the correlation of the propagated comparison
direction with these returned fields, or a different direct strong
comparison argument. Nothing here assumes such an estimate or presents
it as a completed lemma. In particular no global canonical population
uniqueness, cap removal, full-sequence width convergence, or GF/GD velocity
bridge is claimed from these partial identities.
