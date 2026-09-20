# Equal-weight finite inputs: a degenerate Hilbert equilibrium

Frozen first analytic candidate, 2026-09-18. Internally derived; not
independently reviewed or promoted. This route read exactly the assigned
scientific sources `docs/observable_p1.md`, `DEPENDENT_BASIN_RESULTS.md`,
`dependent_hilbert_geometry.md`, and `dependent_basin_functional.md`, all
completely. It used the investigate-conjectures and solve-math-rigorously
skills and the research-contract, evidence-ledger, and adversarial-audit
references. No other study, sibling approach, experiment, numerical
calculation, or external theorem was used. The construction was developed
before comparison with other current routes.

## 1. Exact conclusion and contract

The equal-weight three-input geometry does **not** extend to arbitrary
finite input count: seven equal-weight, pairwise distinct non-antipodal
unit inputs in dimension three admit an exact canonical p=1 equilibrium
with loss `48/49`, with every individual lower critical coefficient
nonzero, and with **nonnegative ordinary second directional variation in
every physical Hilbert direction**. Thus both of these proposed premises
of a general theorem are false:

1. Every sub-loss-one equilibrium has individual coefficient cancellation.
2. Every sub-loss-one equilibrium has a negative second-variation direction.

The equilibrium is nevertheless not a local minimum. Arbitrarily close
physical-Hilbert states have smaller loss; its loss lacks a second
Frechet differential. This is a counterexample to the intermediate
geometric assertions, **not** a positive-probability bad-basin construction.
The arbitrary-finite-input, all-H-endpoint null-basin statement remains
unresolved by this route.

All objects retain the exact fixed canonical correlated lower marks,
upper marks, ridge, odd sector, full matrix and actual transpose from the
allowed sources. The state space is

\[
\mathcal H_d=L^2_{\rm odd}(P_1;\mathbb R^d)
\oplus L^2_{\rm odd}(P_2)\oplus\mathbb R^{d\times2d},
\qquad \theta=(w-g,c,M),
\]

with the physical L2/L2/Frobenius norm. This is an exact equilibrium
calculation, with no approximation, sample-count limit, or altered
randomization. It concerns arbitrary H endpoints; the lower displacement
in the construction is unbounded. Its consequences therefore do not
refute a bounded-lower-displacement endpoint theorem.

## 2. A pair of different finite spherical designs

Work first in dimension three. Choose `C,S>0`, `C^2+S^2=1`. Let the
positive-label angles be

\[
\Theta_+=\{0,2\pi/3,4\pi/3\},
\]

and the negative-label angles be

\[
\Theta_-=\{\pi/4,3\pi/4,5\pi/4,7\pi/4\}.
\]

For every angle set

\[
u(\vartheta)=(C,S\cos\vartheta,S\sin\vartheta).
\tag{1}
\]

Give all seven inputs weight `1/7`, and assign labels `+1` on the
triangle and `-1` on the square. The angles are distinct. Their common
strictly positive first coordinate excludes antipodal pairs. All inputs
have unit norm.

Writing `v(vartheta)=(cos vartheta,sin vartheta)`, the triangle and square
have the same normalized first and second moments:

\[
\frac13\sum_{\Theta_+}v=\frac14\sum_{\Theta_-}v=0,
\qquad
\frac13\sum_{\Theta_+}vv^T
=\frac14\sum_{\Theta_-}vv^T=\frac12 I_2.
\tag{2}
\]

These identities follow directly by inserting the displayed angles.
In particular, the corresponding averages of `u` and `uu^T` agree.

Set

\[
F=-\frac17,\qquad
\rho_i=\frac17(F-y_i)
=\begin{cases}-8/49,&i\in\Theta_+,\\6/49,&i\in\Theta_-.
\end{cases}
\]

Since the total coefficients on the two classes are `-24/49` and
`+24/49`, equations (2) give exactly

\[
\sum_i\rho_i=0,\qquad
\sum_i\rho_i u_i=0,\qquad
\sum_i\rho_i u_i u_i^T=0.
\tag{3}
\]

The differing class cardinalities allow `F!=0` despite equal individual
weights. This is the mechanism absent from a three-input signed-pair
collision.

## 3. An exact canonical-mark equilibrium

Let `q` be any nonzero vector in `R^(2d)`, and let `e` be the first upper
coordinate vector. Define

\[
B=q\cdot b_1,\qquad \varepsilon=\operatorname{sign}B,
\qquad A=E_1[b_1\varepsilon],\qquad m=q\cdot A=E_1|B|>0.
\tag{4}
\]

The canonical lower-mark marginal has a positive full-dimensional density
on an open neighborhood of zero, as proved in the allowed functional
report. Thus `P(B=0)=0`, and `m>0`. Both marks and `epsilon` are bounded;
`epsilon` is odd. Their prescribed correlation with `g` is untouched.

Choose `a>0` and put

\[
w=a\varepsilon e_1,\qquad M=e q^T,
\qquad t=aC,\quad a_0=\tanh(t)A,\quad z=m\tanh(t)>0.
\tag{5}
\]

The lower field is bounded and odd, hence `w-g` is an admissible odd
L2 field. For every input in (1),

\[
a_i=E_1[b_1\tanh(w\cdot u_i)]=a_0,
\qquad Ma_i=ze,
\qquad H_i=\tanh(zx),\quad x=b_2\cdot e.
\tag{6}
\]

Fix any nonzero real `D`. There is a bounded odd readout `c=c(x)` with

\[
E_2[c\tanh(zx)]=F,
\qquad E_2[cx\operatorname{sech}^2(zx)]=D.
\tag{7}
\]

Here is a direct construction. The bounded odd functions
`h(x)=tanh(zx)` and `j(x)=x sech^2(zx)` are linearly independent under
the canonical upper marginal. An almost-sure relation holds on its open
support interval by continuity and positive density, hence on the real
line by analyticity. Taking `x` to positive infinity first kills the
coefficient of `h`, and then the coefficient of `j` is zero. Their
2 by 2 Gram is therefore positive definite. Its inverse applied to
`(F,D)` supplies the coefficients of a linear combination `c` satisfying
(7). Canonical upper coordinates are independent and symmetric; pairing
the other coordinates with a function of `x` gives zero. Therefore

\[
f_i=F,\qquad d_i=E_2[b_2c\phi'(b_2\cdot Ma_i)]=De
\quad\hbox{for every }i.
\tag{8}
\]

The readout gradient is `2 H_1 sum rho_i=0`. The matrix gradient is
`2De a_0^T sum rho_i=0`. Since the lower gates all equal
`s=sech^2(t)>0`, the lower gradient is

\[
2sBD\sum_i\rho_i u_i=0.
\tag{9}
\]

Thus this is an exact equilibrium of all three trained blocks. Its loss is

\[
L=\frac17\left[3\left(-\frac87\right)^2
                  +4\left(\frac67\right)^2\right]
=\frac{48}{49}\in(0,1).
\tag{10}
\]

But every individual lower coefficient is nonzero:

\[
T_i=\rho_i M^Td_i=\rho_iDq\ne0.
\tag{11}
\]

The construction works for every fixed `d>=3` by zero-padding the input
coordinates and using the actual dimension-d canonical marks. The matrix
has the permitted dimensions and is a valid point in the full matrix
space; there is no imposed rank constraint on the flow.

## 4. Every physical-Hilbert second directional variation is nonnegative

Take an arbitrary direction `(h,k,N)` in H, where `h` perturbs `w`, `k`
perturbs `c`, and `N` perturbs `M`. Define

\[
K=E_1[b_1h^T],\qquad s=\phi'(t).
\]

All entries exist by Cauchy--Schwarz. Along this direction the lower
moments have ordinary first and second derivatives

\[
a_i'=sKu_i,
\qquad
a_i''=\phi''(t)E_1[b_1\varepsilon(h\cdot u_i)^2].
\tag{12}
\]

The second formula is valid for every L2 direction: the bounded second
activation derivative gives an integrable dominating multiple of `|h|^2`.
Writing `z_i=Ma_i`, we obtain

\[
z_i'=Na_0+MsKu_i,\qquad z_i''=2NsKu_i+Ma_i''.
\tag{13}
\]

All second derivatives here are along the one-dimensional state curve;
Frechet differentiability is not presumed. Equations (3), (12), and
(13) imply

\[
\sum_i\rho_i z_i'=0,\qquad
\sum_i\rho_i z_i''=0,\qquad
\sum_i\rho_i z_i'(z_i')^T=0.
\tag{14}
\]

For the second identity, contract the third identity in (3) with
`h h^T` pointwise under the expectation in (12). For the third identity
in (14), expand the affine formula for `z_i'`; its constant, linear,
and quadratic terms vanish by the three identities in (3).

Put

\[
\ell_k=E_2[b_2k\phi'(zx)],\qquad
C_c=E_2[c\phi''(zx)b_2b_2^T].
\]

The marks are bounded and `c,k` are in L2, so these pairings are finite.
Differentiating the upper readout twice gives

\[
f_i''=2\ell_k\cdot z_i'+(z_i')^TC_cz_i'+d_i\cdot z_i''.
\tag{15}
\]

Since all `d_i=De`, equations (14)--(15) yield
`sum_i rho_i f_i''=0`. The exact unhalved square-loss formula consequently
reduces to

\[
\left.\frac{d^2}{d\delta^2}
 L(w+\delta h,c+\delta k,M+\delta N)\right|_{\delta=0}
=\frac27\sum_i(f_i')^2\ge0.
\tag{16}
\]

This holds for every H direction, including every bounded odd direction.
There is no negative second directional curvature. The group field of
the preceding strict-saddle proof also vanishes identically at this state:
there is just one effective-feature group, and

\[
R(w)=s\sum_i\rho_i u_i=0.
\]

Thus failure of that mixed-variation route reflects a true failure of its
target conclusion, rather than only an inability to find a direction.

## 5. Concentrated perturbations expose the higher-order descent

For definiteness choose `t=(log 2)/2`, so `tanh(t)=1/3` and
`phi'''(t)=2 sech^2(t)(3 tanh^2(t)-1)=-32/27!=0`; choose `a=t/C`.
Define the analytic scalar function

\[
Q(h)=\sum_i\rho_i\tanh(t+Sh\cos\vartheta_i).
\tag{17}
\]

Equation (3) gives `Q(0)=Q'(0)=Q''(0)=0`. The sum of cubed cosines
on the triangle is `3/4`, while its sum on the square is zero. Thus

\[
Q'''(0)=-\frac6{49}S^3\phi'''(t)\ne0.
\tag{18}
\]

For arbitrarily small fixed nonzero `h`, `Q(h)` is nonzero, and its sign
is opposite on the two sides of zero. Fix such an `h`.

Choose `delta>0` with `P_1(B>=delta)>0`. The canonical Gaussian carrier
is nonatomic, so it has measurable subsets `E_n` of this event with
probabilities `m_n>0` tending to zero. Let `-E_n` be their sign images.
The sets are disjoint because `B` changes sign. Perturb only `w`, by
`h e_2` on `E_n`, `-h e_2` on `-E_n`, and zero elsewhere. Denote the
bounded odd increment by `h_n`. Then

\[
\|h_n\|_2^2=2m_nh^2\longrightarrow0.
\tag{19}
\]

All effective-vector increments are `O(m_n)` because the marks and
activations are bounded. The finite-dimensional smooth upper loss map
therefore has a uniform Taylor remainder `O(m_n^2)`. Using (7), the
two sign-paired mark sets, and the unhalved loss derivative gives

\[
L(w+h_n,c,M)-L(w,c,M)
=4D Q(h)\int_{E_n}B\,dP_1+O(m_n^2).
\tag{20}
\]

Choosing the sign of the fixed small `h` so that `D Q(h)<0` shows
strictly smaller loss for all sufficiently large `n`. The opposite sign
gives larger loss. Thus the equilibrium is a degenerate saddle in the
local-value sense despite (16).

Moreover, if a second Frechet differential existed, its quadratic form
would have to equal (16) on every fixed direction. For these `h_n`, the
first effective-vector increments and hence all `f_i'[h_n]` are
`O(m_n)`, so that quadratic form is `O(m_n^2)`. The first differential
vanishes at the equilibrium. But after subtraction of half this quadratic
term, (20) divided by (19) stays bounded away from zero in absolute value:
`integral_(E_n) B >=delta m_n`. This contradicts the required
`o(||h_n||_2^2)` remainder. Consequently L has no second Frechet
differential at this equilibrium.

## 6. Claim ledger and exact unresolved issue

| Claim | Status | Evidence and limit |
|---|---|---|
| Equal weights force individual cancellation at all sub-loss-one finite-input H equilibria | Falsified | Seven-input canonical equilibrium (1)--(11) |
| Every such equilibrium has a negative ordinary second directional variation | Falsified | Complete all-H calculation (12)--(16) |
| The constructed equilibrium is a local minimum | Falsified | Concentrated signed perturbations (17)--(20) |
| The old finite-rank unstable-space graph proof applies at this equilibrium | Falsified | No positive flow-linearization quadratic direction; the needed Frechet loss regularity also fails |
| Arbitrary finite-input all-H point-convergent positive-loss basin is null under the specified Gaussian-series law | Open | No positive-probability basin is constructed, and a degenerate-saddle avoidance argument is absent |
| Bounded-lower-displacement endpoint extensions | Unchanged | This example has bounded w and therefore unbounded w-g |

The probabilistic distinction is essential. The supplied Gaussian series
has bounded field increments almost surely, and any translation and
positive scale retain the original intended initialization experiment.
An admissible ambient equilibrium, or arbitrarily near descending states,
does not determine the probability that this law gives its point-convergent
basin. In particular, the construction neither locates the deterministic
canonical initialization in a bad basin nor contradicts the proved
three-input theorem.

The higher-order degeneracy survives all specified validity checks:
input norms and distinctness are exact; no population law is changed;
all fields obey odd parity; the readout is bounded; the displacement is
square-integrable; all three exact gradients vanish; every H directional
second derivative is justified by an integrable domination; and the
loss is strictly between zero and one. The missing bridge is a theorem
about the dynamics near this kind of degenerate, non-Frechet Hilbert
equilibrium, or an explicit positive-probability basin demonstrating
that the desired extension is false.

## 7. Post-freeze comparison: a regular rank-one Hessian variant

This section was added after the first candidate was frozen and sent to
the supervisor. The SHA256 of the complete Sections 1--6 first-freeze file
was

`4ecdf786c4964e4a31afdabed64284417452c372f8e9c2743c06031c8bba4c6a`.

The supervisor independently derived and then supplied the `D=0` readout
choice below. This comparison extension verifies it without reading any
sibling report. Sections 1--6 and their `D!=0` example are preserved. The
two choices give different equilibria: the original one disproves
individual cancellation and lacks second Frechet differentiability; the
present one is Frechet regular and disproves the strict-saddle premise
even after cancellation is imposed.

Keep the seven inputs, weights, labels, and lower/matrix state from
(1)--(6). In the upper carrier write

\[
H(x)=\tanh(zx),\qquad J(x)=x\operatorname{sech}^2(zx),
\qquad x=b_2\cdot e,
\]
\[
\lambda=\frac{E_2[HJ]}{E_2[J^2]},\qquad
U(x)=H(x)-\lambda J(x),\qquad
c_0(x)=\frac{F}{E_2[U^2]}U(x),\qquad F=-\frac17.
\tag{21}
\]

The linear independence proved in Section 3 ensures `E[J^2]>0` and
`E[U^2]>0`, so every denominator is strictly positive. This is an explicit
bounded odd readout in the same canonical upper carrier. Orthogonal
projection gives

\[
E_2[UJ]=0,\qquad E_2[UH]=E_2[U^2],
\quad\hbox{hence}\quad
E_2[c_0H]=F,\qquad E_2[c_0J]=0.
\tag{22}
\]

For the first upper coordinate, the second identity in (22) is exactly
the corresponding component of `d_i`. Every other component is zero
because that canonical upper coordinate is centered, independent of `x`,
and paired with a function of `x` alone. Consequently

\[
d_i=0,\qquad T_i=0\qquad\hbox{for every }i.
\tag{23}
\]

The lower and matrix gradients vanish individually. The readout gradient
vanishes because all features are `H` and `sum rho_i=0`. The predictions
remain `F`, so this is again an exact equilibrium with loss `48/49`.

Here the actual physical-Hilbert Hessian exists. To verify the applicable
regularity result explicitly, write the lower gradient as
`2 sum_i G_i(w) T_i(theta)`, with

\[
G_i(w)t=\phi'(w\cdot u_i)(b_1\cdot t)u_i.
\]

The finite-dimensional coefficients `T_i` are locally `C^(1,1)` on H,
and the maps `G_i` are bounded and Lipschitz from the lower L2 field into
operators from the finite coefficient space to lower L2. These estimates
use bounded marks and activation derivatives and do not require bounded
lower displacement. At the present equilibrium all `T_i=0`. Subtracting
the linear term leaves a sum of a product of two `O(r)` factors and a
`C^(1,1)` coefficient remainder. Its Lipschitz constant on a radius-r
H ball is `O(r)`, exactly as in Sections 3--4 of the allowed functional
report and the final regularity calculation of the allowed geometry
report. The upper and matrix gradient blocks are locally `C^(1,1)` through
the finite moments. Thus the full loss gradient has a bounded Frechet
derivative at this equilibrium, with the small-Lipschitz remainder needed
by that regularity calculation. In particular, the Hessian here is an
actual bounded Hilbert operator, not only a directional quadratic form.

Section 4 applies unchanged with `D=0`. Since `d_i=0`, the first prediction
variation in any direction `eta=(h,k,N)` is simply

\[
Df_i[\eta]=E_2[kH]\qquad\hbox{for every }i.
\]

Equation (16) therefore identifies the actual Hessian quadratic form:

\[
D^2L[\eta,\eta]=2(E_2[kH])^2.
\tag{24}
\]

Polarization of this bounded symmetric form gives its operator exactly:

\[
\nabla^2L(h,k,N)=(0,\,2E_2[kH]H,\,0).
\tag{25}
\]

The function `H` is nonzero because `z>0` and the upper marginal has a
positive density on an interval. Thus (25) has rank one, with its only
nonzero eigenvalue `2||H||_2^2>0`. The physical gradient-flow linearization
is `-nabla^2 L`; its only nonzero eigenvalue is `-2||H||_2^2`. Its unstable
subspace is zero, its stable subspace is the one-dimensional span of
`(0,H,0)`, and every other linearized direction is central.

This is a stronger obstruction to a universal strict-saddle strategy than
the original non-Frechet example: **a regular positive-loss equilibrium
with individual cancellation can have no unstable linearized direction**.
Absence of linear instability is not a proof of attraction. The behavior
of the infinitely many central directions is not decided by (25), and
this extension makes no assertion that the equilibrium is a local minimum,
has an open basin, or attracts a set of positive Gaussian-series
probability. The leading needle term (20) vanishes when `D=0`, so the
descent proof for the original readout does not automatically transfer to
this different equilibrium. The intended arbitrary-finite-input
point-convergent basin-null theorem remains open in this route.

## 8. Special trajectories with a descending positive-loss plateau

This further post-freeze corollary follows the supervisor's suggested
strong-stable construction. It concerns the `D=0` equilibrium of Section
7, denoted `theta_*`. It establishes existence of special starts, not
positive probability or attraction of a neighborhood.

Although `theta_*=(w_*-g,c_0,M_*)` has unbounded lower displacement,
its actual lower field `w_*` and readout `c_0` are bounded. Work in the
affine chart `theta_*+X`, where

\[
X=L^\infty_{\rm odd}(P_1;\mathbb R^d)
\oplus L^\infty_{\rm odd}(P_2)\oplus\mathbb R^{d\times2d}.
\]

The exact field maps this chart into X and is smooth in its Banach norm:
all marks are bounded, all tanh derivatives needed on bounded chart
balls are bounded, moment integration is continuous, and matrix and
readout operations are finite products and continuous pairings. Thus,
in increment coordinates,

\[
x'=Ax+N(x),\qquad N(0)=0,\qquad DN(0)=0,
\quad A(h,k,N_M)=(0,-2E_2[kH]H,0).
\tag{26}
\]

Let `beta=2||H||_2^2>0`, let `E_s=span{(0,H,0)}`, and let `E_0` be
the kernel of the bounded X-functional `x=(h,k,N_M) -> E_2[kH]`.
The projections onto these complementary subspaces are bounded in X.
Use the equivalent sum norm `||x||=||P_s x||_X+||P_0 x||_X`. The
semigroups are multiplication by `exp(-beta t)` on `E_s` and the
identity on `E_0`.

On a sufficiently small X ball, the Lipschitz constant of N is
arbitrarily small. Composing N with a radial retraction onto this ball
gives a globally `epsilon`-Lipschitz map `N_hat` with `N_hat(0)=0`,
where `epsilon` remains arbitrarily small. For each `eta in E_s`, solve

\[
\begin{split}
x_s(t)&=e^{-\beta t}\eta+
 \int_0^t e^{-\beta(t-r)}P_s\widehat N(x(r))\,dr,\\
x_0(t)&=-\int_t^\infty P_0\widehat N(x(r))\,dr.
\end{split}
\tag{27}
\]

Consider continuous X-valued paths with norm

\[
\|x\|_{\rm dec}=
\sup_{t\ge0}e^{\beta t/2}
       (\|x_s(t)\|_X+\|x_0(t)\|_X).
\]

The stable integral in (27) has Lipschitz constant at most
`2epsilon/beta`: multiply the difference estimate by `exp(beta t/2)`
and integrate `exp(-beta(t-r)/2)` from zero to t. The center integral
has the same bound by integrating `exp(-beta(r-t)/2)` from t to
infinity. Thus the full map has contraction constant
`q=4epsilon/beta`; choose the chart ball so that `q<1/2`. Its unique
fixed point has

\[
\|x\|_{\rm dec}\le\frac{\|\eta\|_X}{1-q}.
\tag{28}
\]

For sufficiently small `eta`, this bound keeps the whole path inside
the ball on which `N_hat=N`. Differentiating the integrals in (27)
then verifies the original exact ODE (26), and the fixed-point bound
gives exponential convergence to `theta_*` in X, hence in H. Its
initial stable projection is exactly `eta`; therefore a nonzero `eta`
gives a nonconstant solution. Such a solution cannot meet any equilibrium
at a finite time: local uniqueness backward along its finite segment
would force it to have been stationary, contradicting its nonzero
stable coordinate and convergence to `theta_*`.

The exact physical energy identity now gives strict loss decrease at
every finite time, and continuity at the limit gives

\[
L(\theta(t))\searrow\frac{48}{49}.
\tag{29}
\]

By reducing the nonzero `eta` if necessary, continuity of L at
`theta_*` also ensures `L(theta(0))<1`. Hence there exist actual
nonstationary exact-flow trajectories starting in the sub-loss-one
region and descending to this positive equilibrium loss. Their states
remain in the affine bounded-increment chart around `theta_*`; their
lower displacements are not asserted essentially bounded.

The contraction constructs a one-parameter local strong-stable graph,
with infinitely many ambient center directions left uncontrolled. It
does not show an open attracting neighborhood, a basin of positive
measure under the specified Gaussian series, or the behavior of the
deterministic canonical state. Thus the new existence statement (29)
is compatible with the proposed exceptional-basin conclusion, whether
that conclusion ultimately proves true or false for finite inputs.
