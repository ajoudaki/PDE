# Input perturbations of the triangle/square equilibrium

Frozen independent analytical route, 2026-09-18. Internally checked, not
promoted. The complete scientific inputs were `docs/observable_p1.md`,
`FINITE_BASIN_EXTENSION.md`, `finite_basin_geometry.md`, and
`finite_basin_tail.md`, together with the supervisor's neutral assignment.
No sibling report, other study, external source, or experiment was used.
The investigate-conjectures and solve-math-rigorously skills and their
research-contract and adversarial-audit process references were applied.
This is the only file written by this route. All conclusions below were
completed before comparison with another current route.

## 1. Result and exact scope

For the explicit regular rank-one-Hessian equilibrium with the projected
readout in `finite_basin_geometry.md`, Section 7, a small generic sphere
perturbation **destroys stationarity of the old state**. Locally, the input
lists for which that exact state remains an equilibrium form a smooth
codimension-seven set in `(S^2)^7`: every input must keep its original
first coordinate. The first input derivative of the full gradient detects
only three of these seven conditions. A second input derivative supplies
an additional obstruction and explains why checking only the linear term
would miss the exact restriction.

Allowing the state to continue within the explicit two-point lower-field,
rank-one-matrix ansatz does not remove all the restriction. Readout
stationarity forces the seven inputs to remain coplanar. This is a smooth
codimension-four condition near the triangle/square data. Hence almost
every sufficiently small input perturbation having a joint density on
the product of spheres admits **no nearby equilibrium in this ansatz**.

There is a sharper statement near the projected readout: an equilibrium
in this ansatz has nonnegative second directional loss variation in every
physical direction if and only if its classwise first and second input
moments agree. Within the coplanar data these impose four further
independent conditions. Thus the data supporting these nearby flat
equilibria form a local smooth codimension-eight submanifold of `(S^2)^7`.
This is a statement about a specified family of states. It is not a theorem
that random data have no flat positive-loss equilibrium anywhere in the
full Hilbert space, nor a basin-probability theorem.

Here “almost every” means absolute continuity with respect to local product
sphere area, or, for the first-order statement, Lebesgue measure on the
fourteen-dimensional product tangent space. An arbitrary singular noise
law can be supported on an exceptional family; arbitrary deterministic
perturbations need not destroy the equilibrium.

## 2. Model, data, and the particular regular state

Work in dimension three with the exact canonical odd marks from
`docs/observable_p1.md`. Write `phi=tanh`, with physical Hilbert state

\[
\theta=(w-g,c,M)\in L^2_{\rm odd}(P_1;\mathbb R^3)
 \oplus L^2_{\rm odd}(P_2)\oplus\mathbb R^{3\times6}.
\]

Every matrix entry remains trainable. Rank one below describes the selected
state, not its allowed physical perturbations. Let `n=e_1` be the input
axis and let `e` be the first upper coefficient axis. For a nonzero lower
coefficient `q`, put

\[
\epsilon=\operatorname{sign}(q\cdot b_1),\quad
A=E_1[b_1\epsilon],\quad
\kappa=q\cdot A=E_1|q\cdot b_1|>0,\quad B=b_2\cdot e.
\]

The assigned sources verify the nondegeneracy, odd parity, and boundedness
of these objects in the actual correlated mark law. Choose `a>0` and
`C,S>0` with `C^2+S^2=1`. The seven original inputs are

\[
u_i=Cn+S(\cos\alpha_i\,e_2+\sin\alpha_i\,e_3),
\]

with three positive labels at triangle angles and four negative labels
at square angles. Either square rotation in the assigned sources works.
Each weight is `p_i=1/7`. Define

\[
m=-1/7,\qquad
\rho_i=(m-y_i)/7=
\begin{cases}-8/49,&y_i=1,\\6/49,&y_i=-1.\end{cases}
\]

The original data satisfy

\[
\sum_i\rho_i=0,\qquad
\mu_1:=\sum_i\rho_i u_i=0,\qquad
\mu_2:=\sum_i\rho_i u_iu_i^T=0.\tag{1}
\]

Set `w=a epsilon n`, `M=e q^T`, `s_0=aC`, `t=phi(s_0)`, and
`sigma=phi'(s_0)>0`. For a scalar `s` near `s_0`, define the upper
functions and scalar prediction

\[
H_s(B)=\phi(\kappa\phi(s)B),\qquad
F(s)=E_2[cH_s],\qquad
D(s)=E_2[cB\phi'(\kappa\phi(s)B)].\tag{2}
\]

Then `F'(s)=kappa phi'(s)D(s)`. At the original common feature set
`H=H_(s_0)`, `J=B phi'(kappa t B)`, and choose precisely the projected
readout

\[
U=H-\frac{\langle H,J\rangle}{\langle J,J\rangle}J,
\qquad c_0=\frac{m}{\langle U,U\rangle}U.\tag{3}
\]

All inner products in this report are upper population pairings unless
specified otherwise. The positive-definite Gram proved in the inputs
ensures the denominators are positive. Thus

\[
F(s_0)=m,\qquad D(s_0)=F'(s_0)=0.
\]

The upper coordinate symmetries give every backward vector `d_i=0`.
The state is a full physical equilibrium of loss `48/49`. Its actual
Hilbert Hessian is

\[
D^2L[(h,k,N),(h,k,N)]=2\langle k,H\rangle^2.\tag{4}
\]

The assigned regularity proof justifies the actual Hessian in (4), not
only formal directional differentiation. For input perturbations below,
the old state is held fixed, so all input derivatives are ordinary
finite-dimensional derivatives of bounded smooth functions.

## 3. A useful strict sign for the projected readout

The projected choice (3) has

\[
\gamma:=F''(s_0)>0.\tag{5}
\]

Here is a direct proof, needed because a different readout satisfying
only `F=m` and `D=0` need not have this sign. Put `z=kappa t>0` and
`K(B)=B^2 phi''(zB)`. Differentiating (2) gives

\[
\gamma=\kappa^2\sigma^2\langle c_0,K\rangle,
\]

because the term proportional to `J` pairs to zero. Away from `B=0`,

\[
R(B)=H/J=\frac{\sinh(2zB)}{2B},\qquad
T(B)=K/J=-2B\tanh(zB).
\]

Both functions depend only on `|B|`. On `|B|>0`, `R` is strictly
increasing and `T` strictly decreasing. For the first claim, the derivative
has numerator `2z|B| cosh(2z|B|)-sinh(2z|B|)>0`; that numerator starts at
zero and has positive derivative. The second claim follows by directly
differentiating `-2r tanh(zr)` for `r>0`.

Give the upper marginal the probability weight `J^2/E[J^2]`, denoted
`nu`. This law is not concentrated at one absolute value. Then

\[
\langle U,K\rangle
=E[J^2]\operatorname{Cov}_{\nu}(R,T)<0.
\]

Indeed twice this covariance is the expectation of
`(R(B)-R(B'))(T(B)-T(B'))` for independent copies; it is nonpositive
everywhere and strictly negative with positive probability. Since `m<0`,
(3) yields `E[c_0K]>0`, proving (5). All pairings are finite because
the actual marks are bounded.

## 4. First and second input derivatives of stationarity

Let `u_i(eta)` be any `C^2` curve on the unit sphere through the original
input. Set

\[
\xi_i=u_i'(0),\quad \zeta_i=u_i''(0),\quad
\delta_i=a n\cdot\xi_i,\quad \beta_i=a n\cdot\zeta_i.
\]

The sphere conditions are `u_i dot xi_i=0` and
`u_i dot zeta_i=-|xi_i|^2`. Thus
`s_i(eta)=a n dot u_i(eta)=s_0+eta delta_i+eta^2 beta_i/2+o(eta^2)`.
The perturbed residual is
`rho_i(eta)=(F(s_i(eta))-y_i)/7`, so at zero

\[
\rho_i'(0)=0,\qquad
\rho_i''(0)=p_i\gamma\delta_i^2.\tag{6}
\]

Write `G_c,G_w,G_M` for the positive loss-gradient blocks at the frozen
state, evaluated on the perturbed inputs. Since the scalar readout depends
only on `B`, its backward vector is `D(s_i)e`, and exactly

\[
\begin{split}
G_c&=2\sum_i\rho_i(\eta)H_{s_i(\eta)},\\
G_w&=2(q\cdot b_1)\sum_i\rho_i(\eta)
        \phi'(s_i(\eta))D(s_i(\eta))u_i(\eta),\\
G_M&=2eA^T\sum_i\rho_i(\eta)D(s_i(\eta))\phi(s_i(\eta)).
\end{split}\tag{7}
\]

Let `H_1=partial_s H_s|_(s_0)=kappa sigma J`. Using
`D'(s_0)=gamma/(kappa sigma)` in (7) gives

\[
\begin{split}
G_c'(0)&=2H_1\sum_i\rho_i\delta_i,\\
G_w'(0)&=\frac{2\gamma}{\kappa}(q\cdot b_1)
                    \sum_i\rho_i\delta_i u_i,\\
G_M'(0)&=\frac{2t\gamma}{\kappa\sigma}eA^T
                    \sum_i\rho_i\delta_i.
\end{split}\tag{8}
\]

Since `n dot u_i=C>0`, the scalar sum in (8) is already determined
by the axial component of the vector sum. Thus the first input derivative
of the entire gradient vanishes exactly when

\[
\sum_i\rho_i\delta_i u_i=0.\tag{9}
\]

This is a rank-three linear condition on the product sphere tangent space.
For every `i`, the map `xi_i -> delta_i` from its tangent plane onto the
real line is surjective: the tangent projection of `n` has norm `S>0`.
The seven `u_i` span `R^3` and all `rho_i` are nonzero, so the map from
the seven independently variable `delta_i` to the vector in (9) has rank
three. Any tangent perturbation with a density violates (9) almost surely.
Along such a fixed `C^1` curve, `G(eta)=eta G'(0)+o(eta)` is nonzero
for every sufficiently small nonzero `eta`.

The first derivative is not a full description of the stationary input
set. Let `H_2=partial_s^2 H_s|_(s_0)`. From (6)--(7),

\[
\frac12G_c''(0)=
H_1\sum_i\rho_i\beta_i
+H_2\sum_i\rho_i\delta_i^2
+H\gamma\sum_i p_i\delta_i^2.\tag{10}
\]

The three upper functions `H,H_1,H_2` are linearly independent. To check
this without a Gram assumption, note that

\[
H_2=\kappa\phi''(s_0)J+\kappa^2\sigma^2K.
\]

An almost-sure relation between `H,J,K` holds throughout an open upper
support interval by continuity and positive density, hence on the real
line by analyticity. At `B -> +infinity`, `H -> 1`,
`J=4B exp(-2zB)(1+o(1))`, and
`K=-8B^2 exp(-2zB)(1+o(1))`. The constant, quadratic, and linear scales
successively force all coefficients to be zero.

Consequently `G_c''(0)=0` forces
`gamma sum_i p_i delta_i^2=0`. By (5) this means every `delta_i=0`.
Thus no nonzero first-order change of the seven heights can be tangent
to a `C^2` curve of frozen-state equilibria, even when (9) happens to
hold. Sphere accelerations cannot cancel the last term in (10).

These are derivatives of the stationarity equations with respect to
**inputs**. They do not assert a negative eigenvalue of the loss Hessian
with respect to **state**. At a perturbed input list where (7) is nonzero,
the frozen point is no longer an equilibrium, so “unstable equilibrium”
would be the wrong conclusion.

## 5. Exact local classification for the frozen state

The local restriction can be proved exactly, without stopping at a Taylor
expansion. For a finite family of distinct positive numbers `z_j`, the
functions `B -> tanh(z_j B)` are linearly independent under the canonical
upper marginal. In a putative relation, analyticity extends the equality
to real `B`; taking `B -> infinity` first gives zero total coefficient.
Subtract the limiting constants, multiply by `exp(2 z_min B)`, and let
`B -> infinity`. Only the coefficient at the unique smallest `z_j`
survives. Remove it and repeat. This proves independence.

For all sufficiently small input perturbations, every `s_i>0`. Group
indices by equality of `s_i`, equivalently equality of
`z_i=kappa phi(s_i)`. Readout stationarity and the preceding independence
imply, separately in each nonempty group `I`,

\[
\sum_{i\in I}\rho_i=0,
\qquad F(s_I)=\frac1{|I|}\sum_{i\in I}y_i.\tag{11}
\]

If a group contains `r` positive and `l` negative labels, its mean is
`(r-l)/(r+l)`. The equation that this equals `m=-1/7` is `4r=3l`.
With `0<=r<=3`, `0<=l<=4` and a nonempty group, this holds only for
`r=3,l=4`, the entire data list. There are finitely many proper nonempty
groups, so their label means have a strictly positive minimum distance
from `m`. By continuity, restrict the input neighborhood so every `F(s_i)`
is closer to `m` than that distance. Equation (11) then forces all seven
indices into one group. Hence every `s_i` is the same and `F(s_i)=m`.

For the projected readout, (5) implies that locally `F(s)=m` only at
`s=s_0`. It follows that the frozen state is stationary exactly when

\[
n\cdot u_i=C\quad\hbox{for all seven }i.\tag{12}
\]

Conversely (12) makes all features `H`, all predictions `m`, and all
backward vectors zero, so all three gradient blocks vanish. Because the
height derivative on each sphere is nonzero, (12) is a smooth
codimension-seven submanifold of the fourteen-dimensional data space.

The same exact classification holds for any fixed bounded scalar readout
with `F(s_0)=m` and `F'(s_0)=0`, even if `F''(s_0)=0`: `F` is real
analytic, `F(0)=0!=m`, and therefore `s_0` is an isolated zero of
`F(s)-m`. Such readouts can require higher input derivatives than (10)
to expose the full restriction. In particular, the third-moment readout
in the supplied synthesis should not silently be assigned the strict
sign (5), which was proved specifically for (3).

## 6. Nearby continuations in the two-point/rank-one ansatz

Allow the ansatz parameters to vary near the original state:

\[
w=\epsilon v,\qquad M=e q^T,
\qquad v\ne0,
\]

with the same canonical mark laws, a nearby admissible sign field and
coefficient choice if desired, and an arbitrary nearby odd readout `c`.
It is enough to require `kappa=E[(q dot b_1)epsilon]>0`, positive
projections `s_i=v dot u_i`, and predictions near `m`. These conditions
hold in the original finite-parameter neighborhood and are the precise
neighborhood conditions used here. The field topology alone is not being
used to identify sign-field parameters.

The features still equal `tanh(kappa phi(s_i)B)`. Scalar tanh independence
and the proper-group mean gap prove exactly as in (11) that every nearby
equilibrium in this ansatz has

\[
v\cdot u_1=\cdots=v\cdot u_7=s,\qquad f_i=m.\tag{13}
\]

This does not require the readout to depend only on `B`: its group
prediction remains one scalar because the features in a group are equal.
It also remains true if the matrix is allowed to be full while the lower
field is two-point: then `Ma_i=(MA)phi(s_i)`, and the scalar variable
`b_2 dot MA` has a support interval for every nearby nonzero `MA`.

Condition (13) puts all seven inputs in an affine plane. Conversely, every
nearby coplanar input list admits a nearby equilibrium in the displayed
rank-one ansatz: take its unit plane normal `n'`, its positive height
`C'`, set `v=(s_0/C')n'`, and retain `q,e,c_0`. Every `s_i=s_0`, so all
backward vectors vanish and all three gradient blocks are zero.

The coplanar data form a smooth codimension-four manifold locally. Three
original triangle points are affinely noncollinear and continue to define
a unique nearby plane. Requiring each of the other four points to lie in
that plane gives four equations. The derivative of its own plane equation
with respect to each remaining sphere point is nonzero, since `0<C<1`.
These four equations therefore have independent derivatives. Equivalently,
the plane has three parameters and the seven positions on its spherical
circle have seven parameters, giving dimension ten in dimension fourteen.

At first order, let `delta_i=v_0 dot xi_i` with `v_0=a n`. Differentiating
(13) permits variations `dot v` and `dot s` precisely when

\[
\delta_i=\dot s-\dot v\cdot u_i.
\tag{14}
\]

The right-hand side lies in the three-dimensional span of the seven-vectors
`1`, `cos(alpha_i)`, and `sin(alpha_i)`. They are independent at these
angles. Thus (14) is a codimension-four condition on the independent
height variations. A tangent perturbation with a density almost surely
fails it. Failure excludes a differentiable nearby ansatz continuation;
the smooth exact coplanarity classification additionally excludes any
nearby ansatz equilibrium at almost every perturbed data list.

This is the full consequence of readout stationarity in this ansatz. An
input perturbation can create or preserve equilibria with lower fields
having more than two values, and those are outside this classification.

## 7. Which coplanar continuations keep nonnegative curvature?

Consider a nearby rank-one/two-point equilibrium as in (13). Write its
common scalar projection as `s>0`, and let

\[
t=\phi(s),\quad \sigma=\phi'(s),\quad z=\kappa t,
\quad H=\phi(zB),\quad J=B\phi'(zB),
\]
\[
d=E_2[b_2c\phi'(zB)],\qquad D=e\cdot d,\qquad
Q=E_2[cB^2\phi''(zB)].\tag{15}
\]

The common prediction is `m`; hence the coefficients `rho_i` remain those
in Section 2 and `sum rho_i=0`. Define `mu_1,mu_2` by (1) for the new
data. The lower stationarity equation is exactly

\[
2\sigma D(q\cdot b_1)\mu_1=0,
\qquad\hbox{so }D\mu_1=0.\tag{16}
\]

All second directional derivatives used next exist for `L^2` directions
by bounded activation derivatives and integrable squares, as in the
assigned sources. The exhibited descent directions can also be chosen
bounded, so no Frechet assumption is needed to prove their negative sign.

**If `mu_1!=0`, every equilibrium here has a negative second variation.**
Equation (16) gives `D=0`. Choose a bounded odd lower direction `h` with

\[
b:=E_1[(q\cdot b_1)h],\qquad b\cdot\mu_1\ne0.
\]

For example `h=(q dot b_1)mu_1` has this property. Choose a bounded odd
readout direction `k` with `E[kH]=0` and `E[kJ]!=0`; the nonzero projection
of `J` off `H` supplies it. Set the matrix variation to zero. The first
prediction derivative is zero because `D=0` and `k` is orthogonal to `H`.
The loss second variation along `(h,tau k,0)` has the form

\[
4\tau\sigma\langle k,J\rangle b\cdot\mu_1
+2\sigma^2Q\,b^T\mu_2 b.\tag{17}
\]

The coefficient of `tau` is nonzero; choosing its sign and sufficiently
large finite magnitude makes (17) negative. Thus PSD curvature requires
`mu_1=0`, independently of `Q`.

Now assume `mu_1=0`. Let `K_h=E_1[b_1h^T]` and
`b=K_h^T q`. For pure lower variations with zero matrix/readout variation,
the residual part of the second variation is exactly

\[
2\sigma^2Q\,b^T\mu_2b
+2D\phi''(s)
 E_1[(q\cdot b_1)\epsilon\,h^T\mu_2h].\tag{18}
\]

The remaining part is the nonnegative sum of squared first prediction
derivatives. Since the inputs have unit norm,
`trace(mu_2)=sum rho_i=0`. Therefore a nonzero `mu_2` has both positive
and negative eigenvalues.

If `D=0` and `Q!=0`, first prediction derivatives of every pure lower
variation vanish. Taking `h=(q dot b_1)r` makes `b` a positive multiple
of any prescribed input vector `r`. Choosing an eigenvector whose
eigenvalue has sign opposite to `Q` makes (18) negative.

If `D!=0`, choose a bounded odd nonzero scalar function `psi` satisfying
`E[b_1 psi]=0`, and take `h=psi r`. Such a `psi` exists: odd bounded
functions form an infinite-dimensional space on the nonatomic canonical
carrier, while this imposes only six linear conditions. It can be obtained
explicitly from more than six disjoint sign-paired indicator sets by a
nonzero null vector of their six moment rows. As `|q dot b_1|>0` almost
surely, `E[|q dot b_1| psi^2]>0`. In the original sign choice
`epsilon=sign(q dot b_1)`, this is the weight in (18). Now `K_h=0`, so
the first term and every first prediction derivative vanish. Since
`phi''(s)<0`, choosing the sign of the eigenvalue of `mu_2` appropriately
makes the second term negative. The same argument applies to nearby
sign choices if their weighted quadratic form is known to remain
nondegenerate; the stated necessity result below uses the original
`epsilon=sign(q dot b_1)` convention.

At the projected center, Section 3 gives `Q>0`. Continuity of the moment
in (15) ensures `Q!=0` for all sufficiently nearby readouts and ansatz
parameters. Therefore the two cases above show that nearby PSD equilibria
must satisfy both `mu_1=0` and `mu_2=0`.

Conversely, if both moments vanish, the complete second-variation argument
in the assigned sources applies with the common features and backward
vector at this point: every residual second derivative cancels, leaving
`2 sum p_i (Df_i)^2>=0` in every physical direction. This includes all
matrix directions and arbitrary readout directions. Thus, with the
displayed sign convention and parameters/readout near the projected
center, the exact criterion is

\[
\hbox{nonnegative second variation in every physical direction}
\quad\Longleftrightarrow\quad\mu_1=0,\ \mu_2=0.\tag{19}
\]

When all `d_i=0`, this is the actual Hilbert Hessian criterion by the
supplied regularity estimate. When `D!=0`, (19) is only a directional
criterion; the supplied examples explain why an actual Hilbert Hessian
need not exist.

The condition `Q!=0` cannot be deleted for remote readouts: independence
of `H,J,K` permits a readout with `E[cH]=m`, `E[cJ]=0`, and `Q=0`.
At `d=0`, `mu_1=0`, such a readout has a rank-one PSD Hessian even if
`mu_2!=0`. This is an additional tuning of the state, illustrating why
generic data and generic states must not be identified.

## 8. Local codimension of the flat data family

On a common plane `n dot u_i=C`, write
`u_i=Cn+S(cos(alpha_i)e_2+sin(alpha_i)e_3)` in a smoothly chosen plane
frame. Since `sum rho_i=0`, the conditions in (19) are equivalent to
the four real equations

\[
\sum_i\rho_i e^{\mathrm i\alpha_i}=0,
\qquad
\sum_i\rho_i e^{2\mathrm i\alpha_i}=0.\tag{20}
\]

The first equation gives the transverse first moment. Once that vanishes,
the axial and mixed second moments vanish, and the second equation gives
the traceless transverse second moment; its trace is already zero.

The derivative of these four equations with respect to the seven angles
has rank four at the original seven distinct angles. Indeed a dependence
among its rows would give a real trigonometric polynomial of degree at
most two, with no constant term, that vanishes at all seven angles.
Multiplying its complex expression by `exp(2 i alpha)` turns it into a
polynomial of degree at most four evaluated at seven distinct unit-circle
points. It must be zero, so every row coefficient vanishes. The nonzero
weights `rho_i` do not affect this argument.

The precise local submanifold fact used here is: the zero set of a smooth
map from an open subset of `R^n` to `R^k`, whose derivative has rank `k`
at the point, is locally a smooth manifold of dimension `n-k`. The four
plane constraints in Section 6 meet these hypotheses, and the four
independent angular equations (20) meet them within the resulting plane
manifold. Thus the nearby flat-data family has dimension

\[
3\ \hbox{plane parameters}+7\ \hbox{angles}-4\ \hbox{moments}
=6,
\]

or codimension eight in `(S^2)^7`. Every data list in this family admits
a nearby regular rank-one-Hessian equilibrium by the converse construction
in Section 6 using `c_0`, so this is both necessary and attainable within
the specified local ansatz. Holding the old state fixed further fixes
the plane, giving dimension three, or codimension eleven for preservation
of its PSD equilibrium property.

A smooth submanifold of positive codimension has zero ambient smooth
volume locally: in coordinates it is a graph over fewer variables and
its fibers in the remaining coordinates are singletons, so Fubini gives
zero Lebesgue measure. Smooth coordinate changes preserve nullity. This
justifies all density-based almost-sure statements here without treating
the input distribution as a distribution over states.

## 9. Claim ledger and surviving gap

| Statement | Status and scope |
|---|---|
| A random tangent direction generically makes the frozen projected state nonstationary at first order | Proved; rank-three input derivative (8)--(9) |
| Vanishing first input derivative suffices to preserve the frozen equilibrium | False; second derivative (10) and exact classification (12) |
| The frozen state remains an equilibrium only on fixed-height data near the example | Proved; codimension seven |
| Nearby two-point/rank-one equilibria exist for generic perturbed data | False locally; existence is exactly coplanarity, codimension four |
| Nearby flat equilibria in this ansatz persist for generic perturbed data | False; near the projected readout their data locus has codimension eight |
| Every arbitrary perturbation destroys the example | False; common rotations, latitude-preserving changes, and the moment-preserving submanifold give explicit exceptions |
| A removed equilibrium becomes an unstable equilibrium | Incorrect inference; a nonzero gradient removes equilibrium status |
| Generic perturbed data admit no flat positive-loss state anywhere in the physical Hilbert space | Open in this route; states outside the two-point ansatz are not classified |
| Input randomization proves null bad-initialization basins | Not established; it randomizes a different object and no trapping argument was supplied |

The exact partial answer is therefore affirmative for destruction of the
old equilibrium and for exclusion of its nearby explicit ansatz under
absolutely continuous data noise. The unrestricted “all flat positive-loss
equilibria disappear almost surely” claim does not follow. Its necessary
missing step is control of all possible lower-field/state continuations,
including ones that leave the two-point representation.

## 10. Informed post-freeze check: a stronger full-Hilbert local argument

Sections 1--9 were frozen before this comparison. Their SHA256 was
`7595aec009e4f2f8e03c4b16f7c7ad2f325662518c179f4bd01258ded9c01e80`.
Afterward the supervisor supplied the following separate lead argument:
use the residual ridge function to exclude all PSD equilibria in a fixed
physical-Hilbert neighborhood, including states outside the two-point
ansatz. This section is an informed verification of that argument, not an
independent discovery. No sibling report was read.

The argument is valid with the explicit conditions and probability
quantifiers below. It strengthens the local conclusions of Sections 1--9;
their global limitation remains.

### 10.1 Precise local theorem

Let `theta_*` be the regular `d_i=0` seven-input equilibrium from the
allowed sources, with lower field `w_*=a_* epsilon n`, and assume

\[
\phi'''(a_*C)\ne0,\qquad
\lambda(a_*):=\phi'(a_*C)+a_*C\phi''(a_*C)\ne0.\tag{21}
\]

For example `a_*C=1/4` satisfies both conditions. Its readout may be the
projected readout or the strengthened third-moment readout; no sign
assumption on `F''` is used in this section.

Let the inputs follow a fixed `C^2` sphere curve
`u_i(eta)=u_i+eta xi_i+O(eta^2)`, with the original labels and weights.
Suppose

\[
\Delta:=\sum_i\rho_i n\cdot\xi_i\ne0.\tag{22}
\]

Then there is a fixed physical-Hilbert neighborhood `V` of `theta_*`
and `eta_0>0` such that, for every `0<|eta|<eta_0`, **every equilibrium
in `V` has a genuine finite-rank Hilbert Hessian with a negative
eigenvalue**. In particular, there is no PSD equilibrium anywhere in
`V`. The theorem allows the equilibrium state, including its entire lower
field and full matrix, to depend arbitrarily on `eta`.

The tangent functional (22) is nonzero on the product tangent space,
because every map `xi_i -> n dot xi_i` is surjective and every `rho_i`
is nonzero. Therefore (22) holds almost surely for a fixed tangent
direction drawn from a distribution with a density. The conclusion is

\[
\text{for almost every fixed }\xi,\quad
\exists\eta_0(\xi)>0\quad
\forall\,0<|\eta|<\eta_0(\xi):\quad\text{the stated local property}.
\tag{23}
\]

The expansion below does not by itself prove that for each fixed small
nonzero amplitude the exceptional directions form a null set. It gives
no uniform control for directions arbitrarily close to `Delta=0`.

### 10.2 Nearby equilibrium features must all coincide

For arbitrary nearby states and nearby inputs, the seven effective vectors
`v_i=M E_1[b_1 phi(w dot u_i)]` and their predictions vary continuously
in the physical Hilbert norm. For example, bounded marks and the
Lipschitz property of `phi` bound changes of the lower moments by a
constant times
`||w-w_*||_2+||w_*||_2 max_i |u_i(eta)-u_i|`.
Readout and matrix continuity follow from Cauchy--Schwarz and finite
products. Thus all `v_i` lie in a small ball around the same nonzero
`v_*`, and all predictions lie in the proper-group mean gap around `m`
used in Section 5.

We need the vector version of the tanh independence argument. Given
finitely many nonzero vectors `v_j` no two equal up to sign, the functions
`b -> tanh(b dot v_j)` are linearly independent under the canonical
upper law. A putative almost-sure relation holds on an open support box
by continuity and positive density and extends to all real `b` by
analyticity. Choose a vector `r` such that all `r dot v_j` are nonzero
and have distinct absolute values; the forbidden choices are a finite
union of proper hyperplanes. Restricting the relation to `b=t r`
reduces it to the scalar proof in Section 5, with signs absorbed into
the coefficients. This proves the claimed independence.

Readout stationarity consequently gives zero residual sum in every
signed-equality group of effective vectors. By taking their common
neighborhood small enough, no vector is zero and opposite equality is
impossible. The finitely many proper-group label means stay away from
`m`, so every nearby equilibrium must have

\[
v_i=v\ne0\quad\hbox{for all }i,\qquad f_i=m,
\qquad d_i=d\quad\hbox{for all }i.\tag{24}
\]

In particular the residuals are exactly the fixed `rho_i` in Section 2.
This conclusion used no two-point restriction on the perturbed state.

### 10.3 The residual ridge function has no nearby critical point

Define a scalar function on ordinary input-weight space `R^3`:

\[
P_\eta(s)=\sum_i\rho_i\phi(s\cdot u_i(\eta)),\qquad
R_\eta(s)=\nabla P_\eta(s)
=\sum_i\rho_i\phi'(s\cdot u_i(\eta))u_i(\eta).\tag{25}
\]

Write `s=a n+z`, where `z dot n=0`, and identify
`z=z_2 e_2+z_3 e_3`. The original residual moments through degree two
vanish. The square contributes zero to the transverse third moment,
and the triangle contributes its third harmonic. Therefore, uniformly
for `a` in a compact interval near `a_*`,

\[
P_0(a n+z)=c(a)\operatorname{Re}(z_2+\mathrm i z_3)^3+O(|z|^4),
\qquad c(a)=-\frac{S^3}{49}\phi'''(aC).\tag{26}
\]

Indeed the residual-weighted third power is
`-(6S^3/49) Re(z_2+i z_3)^3`; dividing by `3!` gives (26).
The smooth remainder has transverse derivative `O(|z|^3)` and axial
derivative `O(|z|^4)`, by Taylor expansion with uniformly bounded
derivatives. A first input variation at `z=0` gives

\[
\partial_\eta P_\eta(a n)|_{\eta=0}
=a\phi'(aC)\Delta.
\]

Differentiating in the axial coordinate and using the `C^2` input curve
therefore yields, uniformly near the axis,

\[
\begin{split}
\nabla_zP_\eta(a n+z)
 &=c(a)\nabla_z\operatorname{Re}(z_2+\mathrm i z_3)^3
       +O(|z|^3+|\eta|),\\
\partial_aP_\eta(a n+z)
 &=c'(a)\operatorname{Re}(z_2+\mathrm i z_3)^3+O(|z|^4)\\
 &\quad+\eta\lambda(a)\Delta+O(|\eta||z|+\eta^2).
\end{split}\tag{27}
\]

The cubic harmonic satisfies the exact norm identity

\[
\left|\nabla_z\operatorname{Re}(z_2+\mathrm i z_3)^3\right|
=3|z|^2.\tag{28}
\]

By (21), shrink the axial interval so `|c(a)|` and `|lambda(a)|`
are bounded below by positive constants there. Shrink the transverse
radius to absorb the `O(|z|^3)` term in the first equation of (27).
At any hypothetical critical point of `P_eta` in this fixed cylinder,
(27)--(28) would imply `|z|^2<=K|eta|`. Substituting this into the
second equation gives

\[
\partial_aP_\eta(a n+z)
=\eta\lambda(a)\Delta+O(|\eta|^{3/2}).\tag{29}
\]

The leading term has magnitude at least a fixed positive multiple of
`|eta|` by (22), so it cannot vanish for sufficiently small nonzero
`eta`. This contradiction excludes every critical point in that fixed
cylinder. Since `P_eta` is odd, `R_eta` is even; it also excludes
critical points in its negative image. Thus there is `r>0`, independent
of small `eta`, such that

\[
R_\eta(s)\ne0\quad\hbox{throughout}
B_r(a_*n)\cup B_r(-a_*n).\tag{30}
\]

For merely `C^1` input curves the remainder in (29) is
`O(|eta|^(3/2))+o(|eta|)`, still sufficient for the same conclusion.
The nonvanishing restrictions (21) are substantive: this proof does
not treat the amplitudes at which `phi'''(a_*C)=0` or
`1-2a_*C tanh(a_*C)=0`.

### 10.4 Why the physical Hilbert topology is sufficient

Choose the neighborhood `V` small enough that
`||w-w_*||_2<r/2`. Because the reference lower field takes only the
values `+a_*n` and `-a_*n`, Markov's inequality gives

\[
P_1\big(w\in B_r(a_*n)\cup B_r(-a_*n)\big)>3/4.
\tag{31}
\]

Only positive mass is needed. There is no claim of pointwise uniform
closeness and no replacement of the Hilbert norm by an essential-supremum
norm. Equations (30)--(31) imply `R_eta(w)!=0` on a positive-mass set.

At an equilibrium, (24) makes lower stationarity exactly

\[
(b_1\cdot M^Td)R_\eta(w)=0\quad\hbox{almost surely}.\tag{32}
\]

The canonical lower mark law gives every fixed nonzero coefficient
hyperplane zero mass. Therefore, if `M^Td` were nonzero, (32) could not
hold on the positive-mass set from (31). We obtain

\[
M^Td=0.\tag{33}
\]

This is valid although `w` depends on the same lower marks: no conditional
independence is used. A fixed null hyperplane has zero measure on every
measurable subset, including that selected by `w`.

Each individual lower critical coefficient is now
`T_i=rho_i M^Td=0`. The supplied regularity argument applies: the
gradient has a bounded Frechet derivative at the equilibrium. Its
derivative is finite rank because the derivative of each lower gate
multiplies the zero coefficient `T_i`; all surviving terms factor
through finitely many lower/upper moment derivatives and matrix entries.
The actual Hessian is therefore a bounded finite-rank self-adjoint
operator on the physical Hilbert space.

### 10.5 A negative physical direction and eigenvalue

At a common effective vector `v`, write
`H_v=phi(b_2 dot v)`, and let `J_*=(b_2 dot e)phi'(b_2 dot v_*)`
be the fixed original upper derivative function. Set

\[
k_v=J_*-\frac{\langle J_*,H_v\rangle}{\|H_v\|_2^2}H_v,
\quad d_{k_v}=E_2[b_2k_v\phi'(b_2\cdot v)],
\quad \ell=M^Td_{k_v}.\tag{34}
\]

These are well-defined and continuous near the reference point.
At the reference,

\[
\ell_*=q\left(\|J_*\|_2^2-
 \frac{\langle J_*,H_*\rangle^2}{\|H_*\|_2^2}\right)\ne0
\]

by linear independence of `H_*,J_*`. Shrink `V` so `ell!=0` throughout.
The bounded odd direction `(0,k_v,0)` satisfies
`Df_i[0,k_v,0]=<k_v,H_v>=0` for every input, so its loss Hessian
quadratic value is zero. Its mixed second variation with any lower
direction `h` is

\[
D^2L[(h,0,0),(0,k_v,0)]
=2E_1[(b_1\cdot\ell)h\cdot R_\eta(w)].\tag{35}
\]

Take the bounded odd direction
`h=(b_1 dot ell)R_eta(w)`. Oddness holds because the marks and `w`
are odd while `R_eta` is even. The right side of (35) becomes

\[
2E_1[(b_1\cdot\ell)^2|R_\eta(w)|^2]>0.\tag{36}
\]

Its strict positivity follows from (30)--(31) and zero hyperplane mass.
The Hessian on `(h,t k_v,0)` is consequently an affine nonconstant
function of `t`, since the pure `k_v` quadratic term is zero. A finite
choice of the sign and magnitude of `t` makes it negative. A bounded
self-adjoint finite-rank operator with a negative quadratic value has a
negative eigenvalue: restrict to its finite-dimensional range and apply
the orthogonal spectral decomposition there. This proves the theorem.

Equivalently, even without first using (33), PSD second directional
curvature would force the mixed value (35) to vanish for every `h`, since
its pure `k_v` value is zero. The nonzero `ell` and zero hyperplane mass
would then force `R_eta(w)=0` almost surely, contradicting (30)--(31).
The stationarity step (33) is what upgrades this directional exclusion
to a genuine Hilbert Hessian with an unstable linearized-flow eigenvalue.

### 10.6 What the strengthened result does and does not settle

This establishes a full-state **local** strict-saddle theorem around
the specified original equilibrium for almost every fixed sphere-tangent
perturbation direction, at sufficiently small nonzero amplitudes in the
direction-dependent sense (23). Every equilibrium in that neighborhood
has negative curvature; some perturbations may leave no equilibrium there.
The old frozen point itself is generically nonstationary, as already
proved in Sections 4--5.

The argument does not classify equilibria far from this neighborhood,
show that the perturbed system has no flat bad equilibrium anywhere,
or establish the requested global basin-null result. It also does not
cover the exceptional tangent hyperplane `Delta=0`, the two amplitude
conditions excluded in (21), or the stronger fixed-noise-radius
almost-sure claim without additional reasoning.
