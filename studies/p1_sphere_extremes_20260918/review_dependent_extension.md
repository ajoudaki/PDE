# Independent internal review: finite dependent-input extension

Reviewer scope: isolated mathematical review requested 2026-09-18. No desired
outcome was assumed. This is an internal check, not promotion approval.

## Frozen inputs and coverage

The neutral assignment and the required `solve-math-rigorously` skill were
read. Scientific inputs read were exactly the following assigned material:

| Input | SHA-256 | Coverage |
| --- | --- | --- |
| `dependent_finite_fitting.md` | `54031d2000496e70ebda0e81dbfb26c08ad32d2b3f31e35066605ba257b3c518` | Complete, 229 lines |
| `../../docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` | Complete, 332 lines |
| `initialization_positivity.md` | `73dae11c96755efd5e5362f879db9ca4197ddf0e3860434e939ecd529e0f55f5` | Complete, 131 lines |
| `basin_spectral_route.md` | `baab073c128990f035ece90f3ac7b0dea15e2f57e9c99849aac7aea7732f051e` | Initially assigned Sections 1–2; subsequently authorized and read completely, 664 lines |
| `basin_hilbert_null_extension.md` | `cf0b0cf735f281e7d5c7b0dbd53ab9987933de4fe031d8d3644911a0aff2f473` | Subsequently authorized and read completely, 364 lines |
| `dependent_hilbert_geometry.md` | `669037005ef6efe0151e43b82e5e7969c5fdf2ed5b75a3423c46a703ec70ce99` | Subsequently authorized and read completely, all six sections, 663 lines |
| `plateau_finite_critical.md` | `3aa693f975862230fec875ab787de48f56116814afd37f52be6b66a042f54ffd` | Subsequently authorized and read completely, 507 lines |
| `dependent_basin_functional.md` | `af691c304d2204b08e76de0ca024241f6c0f2342209f3f8ca08926be2b6173e0` | Subsequently authorized and read completely, all eight sections, 789 lines |
| `DEPENDENT_BASIN_RESULTS.md`, initial frozen integration | `fa0e6b343b85da2f418fc58f1c1f666c33f3fd00de8bed238f05181770329f26` | Read completely, 456 lines |
| `DEPENDENT_BASIN_RESULTS.md`, final clarification | `880a9dd5675060ad6c7b9fe97e485ed28c44f1e606af68a6b13fc86a16529117` | Complete earlier content plus the inspected convergence-implies-equilibrium paragraph, 461 lines |

The exact UTF-8 prefix of `basin_spectral_route.md` before `\n## 3.` has SHA-256
`e8c979fe005c8124bf4516d6a05b3da718dccdb10d1f109c023697e23d37e30d`.
This prefix was the original bounded assignment; its later expansion was
explicitly authorized before the rest of the file was read.
No README, history, other study, other review, unassigned dependency, or
another current agent's scientific findings was consulted. No experiment was
used. Other cited own-study documents were not retrieved. The optional
continuous-carrier assertion whose construction was not assigned is
explicitly excluded from certification below; it is not a premise of the
main integration.

## Claim verdicts

| Claim | Verdict within the stated finite-data, odd-sector population model |
| --- | --- |
| Scalar sign protection extends to every fixed input dimension | PASS |
| The initialized effective feature map is injective modulo sign | PASS |
| Arbitrarily many distinct nonzero effective vectors give independent tanh features | PASS |
| Explicit exact interpolation for every finite architecturally compatible law | PASS |
| Exact attained architectural loss floor for incompatible finite laws | PASS |
| Explicit nonempty open fitting region in the physical Hilbert norm | PASS |
| Exponential loss decay and Hilbert-state convergence throughout that region | PASS |
| Three-direction projective gate-ratio rigidity | PASS |
| Bounded negative directional curvature at every sub-loss-one H equilibrium for at most three inputs | PASS |
| Exact dependent H equilibrium with no second Fréchet differential of the loss | PASS |
| Stated reflected-pair obstruction and sufficient data criterion for individual cancellation | PASS |
| Equal active weights imply individual cancellation for dependent triples | PASS |
| Hilbert trapping graphs, category and explicit probability nullity, conditional on individual cancellation and negative curvature | PASS |
| Integrated full-H basin theorem for equal weights and for the stated generic/explicit nonexceptional data class | PASS |
| Finite exceptional-loss classification and fitting on convergence below the data threshold | PASS |
| Balanced binary class masses give exceptional threshold at least one-half | PASS |
| Bounded-lower-endpoint basin theorem for arbitrary triples and finite families with at most one input relation | PASS |
| Optional compact continuous-carrier topology assertion | NOT CERTIFIED: the full construction dependency was not assigned; not used by the main theorem |

These conclusions do not establish attraction from the canonical readout-zero
initial state, a basin of full measure, a geometry-independent convergence
rate, or an infinite-support interpolation theorem. The finite-fitting
argument alone proves no dependent-input saddle-basin theorem; the separately
reviewed geometry and conditional basin arguments are assessed below.

## Reconstruction of the initialized feature argument

Write the scalar normalization constants from the coefficient source as
`nu, tau, alpha, s, beta, gamma_s, eta, a, b, c_s`, using `gamma_s=1-s`
to distinguish the scalar gate expectation from the later convergence rate.
The positive ridge is exactly `eta=1/4096`. Each coordinate of the lower
joint law is an independent copy of

\[
h=\tanh G,\qquad k=\tanh(\sqrt\tau Z+\alpha h).
\]

The conditional coefficient is

\[
\Psi(h)=\frac{d_h}{a}h+
\frac{d_k}{b}\left(K(h)-\frac{\beta}{\nu+\eta}h\right),
\quad K(h)=E_Z\tanh(\sqrt\tau Z+\alpha h).
\]

I checked the scalar positivity dependency, rather than assuming its
conclusion. Its important bounds are obtained as follows. Gaussian
integration by parts applied to the residual `k-(beta/nu)h`, followed by
Cauchy–Schwarz, gives `s-beta²/nu >= tau gamma_s²`. Consequently
`b² >= tau gamma_s²+eta`. Since `0<beta<=alpha nu`, the coefficient

\[
B=\frac{\alpha\beta\eta/(\nu+\eta)+\tau\gamma_s}{b^2}
\]

satisfies `0<B<=1/gamma_s`. Integrating
`K'(h)>=alpha(1-tau-alpha²h²)` yields
`K(h)/h>=alpha²(1-alpha/3)` for `0<h<=1`. Substitution gives precisely

\[
\frac{c_s\Psi(h)}h\ge
\frac\alpha{\gamma_s}
\left[\gamma_s\frac\nu{\nu+\eta}-1+\alpha-\frac{\alpha^2}3\right].
\]

The analytic estimates `nu<3/7`, `alpha>11/15`, and `nu>1/64` in the
dependency are valid: `sech² z>=exp(-z²)` gives the first two, and
restricting `|G|` to `[1/2,1]` with `tanh(1/2)>=11/24` gives the third.
Also `gamma_s>=alpha-alpha²nu`. The bracket is bounded below by

\[
2\alpha-1-\alpha^2(\nu+1/3)-1/65
\ge 7/15-1936/4725-1/65=2552/61425>0.
\]

The monotonicity in `alpha` used here is valid on the specified rectangle,
since its derivative is at least `2-2(3/7+1/3)>0`. Thus the positivity
bound includes the actual ridge and reverse-response coefficient. No
dimension enters these scalar expectations.

At the initialized lower state `w=g`, conditioning first on the coordinate
pair and then on `G_j` gives, for any unit `u`,

\[
(Da_0(u))_j=T(u_j),\qquad
T(r)=E[\Psi(\tanh G)\tanh(rG+\sqrt{1-r^2}V)].
\]

The conditional Gaussian decomposition remains valid when `u_j=+1` or
`-1`, by its degenerate limit. There is no independence assumption on the
list of data vectors in this calculation.

For fixed `g>0`, put `m_r(g)=E tanh(rg+sqrt(1-r²)V)`. Differentiating for
`0<=r<1` and integrating the term containing `V` by parts yields

\[
\partial_r m_r(g)=gE\phi'(Z_r)-rE\phi''(Z_r),
\quad Z_r=rg+\sqrt{1-r^2}V.
\]

For `r>0`, the mean of `Z_r` is positive. The function
`phi(z)phi'(z)` is odd and strictly positive on the positive half-line.
Pairing the Gaussian densities at `z` and `-z` proves
`E[phi(Z_r)phi'(Z_r)]>0`. As `phi''=-2 phi phi'`, both terms in the
derivative above are positive. At `r=0`, the first term remains strictly
positive. The bound `|partial_r m_r(g)|<=|g|+2` justifies differentiation
under the outer expectation against bounded `Psi(tanh G)`. Oddness in `g`
and strict sign agreement with `Psi(tanh g)` show `T'(r)>0` on `[0,1)`.
Oddness of `T` gives strict increase on the negative half; dominated
convergence supplies the endpoints. Strictness at the endpoints follows
by inserting an intermediate interior point. Therefore `T` is injective
on `[-1,1]`, vanishes only at zero, and satisfies `T(-r)=-T(r)`.

Coordinatewise application proves that `Da_0(u)` is nonzero for every
unit `u`, and `Da_0(u)=+/-Da_0(v)` holds exactly when `u=+/-v` with the
same sign. This checks the needed injectivity, stronger than mere
componentwise sign protection.

The nonconstant upper mark `b_2` is the independent-coordinate image of
Gaussian variables under scaled tanh, so its law has positive density on
an open cube about zero. Given nonzero vectors `v_i` distinct modulo sign,
an almost-everywhere relation among `tanh(b_2 dot v_i)` holds throughout
this cube by continuity. Choose a vector `e` outside the finitely many
hyperplanes with normals `v_i`, `v_i-v_j`, and `v_i+v_j`; all these
normals are nonzero. Then the projected slopes have nonzero, pairwise
distinct absolute values. Restriction to a short segment `b_2=se`,
followed by the identity theorem for real analytic functions on the
connected line, gives an identity on all real `s`.

Absorb each slope sign into its coefficient and denote its magnitude by
`a_i>0`. At positive infinity the constant terms give `sum A_i=0`.
If any coefficient is nonzero, let `a_*` be the smallest slope with
nonzero coefficient. Using
`tanh(as)=1-2 exp(-2as)+O(exp(-4as))`, the remaining identity has leading
term `-2 A_* exp(-2a_*s)`, impossible. This also checks that integer or
rational relations among slopes create no exception. Hence every finite
Gram `K` in the packet is strictly positive definite.

## Interpolation, merging, and the architectural floor

The formula `c_*=sum_i (K^{-1}y)_i H_i^0` is bounded, square-integrable,
and odd under upper-mark negation. At `w=g,M=D`, its predictions are
`K K^{-1}y=y`. This explicitly supplies a fitted point in the claimed
physical Hilbert space for every finite compatible representative list.

For every state, bias-free tanh composition makes prediction odd in the
input, independently of any symmetry of the data. Its state differential
has the same input sign. Thus when two samples are coincident with equal
labels, or antipodal with opposite labels, both their loss contributions
and their three block gradients merge by addition of their masses.

For an arbitrary signed class `x_i=sigma_i x_G`, let `z=f(x_G)`. Direct
completion of the square gives

\[
\sum_{i\in G}p_i(\sigma_i z-y_i)^2
=W_G(z-m_G)^2+\sum_{i\in G}p_i y_i^2-W_Gm_G^2.
\]

For the stated labels `y_i in {+1,-1}`, this is
`W_G(z-m_G)^2+W_G(1-m_G²)`. Interpolating the finite real target list
`m_G` with the same Gram construction attains the floor. Neither the
algebra nor the interpolation requires these class means to be binary.
The normalized-sphere assumption excludes zero inputs, which otherwise
would require their own forced-zero contribution.

## Physical Hilbert flow and the open fitting region

The assigned existence argument extends from its original three-input
setting to arbitrary finite `m,d`: the marks remain bounded, `|u_i|=1`,
and all input sums are finite. Lower moments are Lipschitz in `w` in L2.
All upper gates depend on the finite vectors `M a_i`, and pairings with
`c` are locally Lipschitz in L2. Subtracting the lower gate and its
bounded finite-dimensional coefficient separately proves local
Lipschitz continuity of the full field on H.

The moment derivative has a quadratic remainder bounded by
`(B_1/2)||phi''||_infty ||delta w||_2²`; its derivative is Lipschitz in
operator norm by Cauchy–Schwarz. The loss is consequently continuously
Fréchet differentiable and its H gradient is the negative stated field.
The usual local contraction proof for an ODE on a Hilbert space applies
to this locally Lipschitz field. Along its solutions,

\[
L'=-\|\dot\theta\|_H^2.
\]

With `R=sqrt(L(0))`, weighted Cauchy–Schwarz gives
`sum p_i|r_i(t)|<=R`. Thus `||c(t)||_2` grows at most linearly on finite
intervals, `||M(t)||_F` at most quadratically, and the bound on
`||w'(t)||_2` is a finite polynomial in time. The state has a finite
limit at a putative finite maximal time and the local existence argument
continues it. This proves the global positive-time H flow used here,
without input independence or an all-time state bound.

Explicit permissible mark bounds, if desired, are

\[
B_1^2=d\left[a^{-2}+
\frac{(1+|\beta|/(\nu+\eta))^2}{b^2}\right],
\qquad B_2^2=d/c_s^2.
\]

In particular all denominators and constants in the packet are finite
and positive. For `h=||theta-theta_*||_H`,

\[
|Ma_i-Da_i^0|
\le B_1\|M-D\|_F+B_1\|D\|_F\|w-g\|_2
\le B_1(1+\|D\|_F)h.
\]

The upper tanh Lipschitz bound gives the claimed `D_H h` bound in the
supremum norm. Notice that this decomposition uses the global bound on
`a_i`, so it does not hide a quadratic term in `h`.

Let `S_theta z=sum_i sqrt(p_i)z_i H_i`. Weighted Cauchy–Schwarz gives
`||S_theta||<=1` and `||S_theta-S_*||<=D_H h`. Therefore

\[
\|S_\theta^*S_\theta-S_*^*S_*\|
\le 2D_Hh.
\]

Taking `rho<=gamma/(4D_H)` ensures a current weighted readout Gram at
least `(gamma/2)I` whenever `h<rho`. The readout gradient alone then
gives `L'<=-2 gamma L`. No lower or middle tangent-kernel coercivity is
assumed.

Splitting `f_i(theta)-y_i` as
`E[(c-c_*)H_i]+E[c_*(H_i-H_i^0)]` proves
`sqrt L<=K_f h`. On `h<rho<=1`, Cauchy–Schwarz in the upper population
gives exactly the three speed bounds in the packet, and their sum gives
`||theta'||_H<=C sqrt L`. This bound applies also when `c` and `w-g`
are merely L2 rather than bounded functions.

Put `q=sqrt L`. Where `q>0`, `q'<=-gamma q`; at zero residual the full
field vanishes, so uniqueness makes that state stationary. On any
interval before an exit from `h<rho`, integration gives

\[
\int_0^t Cq(s)\,ds\le(C/\gamma)(q(0)-q(t)).
\]

The norm triangle inequality then bounds
`h(t)+(C/gamma)q(t)` by its initial value. An initial strict inequality
in the definition of U rules out a first exit by continuity. U is open
because the loss is continuous, and it contains the displayed positive
radius ball by `q<=K_f h`. It follows that

\[
L(t)\le L(0)e^{-2\gamma t},\qquad
\int_t^\infty\|\theta'(s)\|_H ds
\le(C/\gamma)\sqrt{L(0)}e^{-\gamma t}.
\]

Completeness of H supplies `theta_infty`; continuity of the prediction
map proves `L(theta_infty)=0`. These are the claimed constants and
exponents, including the unhalved-square-loss factor. Finite-time
preimages of U are open by continuous dependence and consist of fitting
trajectories; the explicit time-zero bound above is asserted for U,
while an earlier preimage obtains the bound after its entry time.

## Hostile checks and limits

- **More samples than dimensions:** the tanh argument uses a finite list of
  distinct projected slopes, not linear independence of the vectors. It
  permits every finite `m>d`.
- **Dependent three-point configurations on a circle:** once duplicate and
  antipodal obstructions are removed, injectivity and the Gram argument
  apply verbatim; no change of the mark law is made.
- **Nearly coincident or nearly antipodal directions:** strict Gram
  positivity persists for each distinct list, but its smallest eigenvalue
  can tend to zero. The packet correctly makes no uniform-radius claim.
- **Exact coincident/antipodal samples:** compatibility permits exact
  merging; incompatibility is captured by the completed-square floor.
- **Unbounded L2 perturbations:** the gate estimates use bounded marks and
  L2 pairings, not L-infinity control of the perturbed state. Thus the
  claimed openness is in the physical H norm.
- **Saturated lower gates and rare large perturbations:** the fitting
  proof depends only on the readout Gram; it does not infer a uniformly
  positive lower gate or a bounded inverse for the lower moment map.
- **Potential regularity overclaim:** the proof requires a locally
  Lipschitz field and a C1 loss on H, both verified above. It does not
  require the tanh substitution operator to be C2 from L2 to L2.
- **Canonical initial trajectory:** the center has `c=c_*`, generally
  different from zero. The proof gives no membership or eventual entry
  of the canonical state into U.

No substantive mathematical correction is required in the reviewed
finite-fitting packet within its stated scope.

## Dependent triple geometry: complete reconstruction

### Projective gate-ratio rigidity

The proposed rigidity lemma is correct for three unit directions distinct
modulo sign in a two-dimensional Euclidean plane. I checked its nontrivial
convexity step for an arbitrary positive quadratic form, including a
nonzero cross term; convexity merely for the Euclidean norm would not
suffice after changing coordinates by the two linear functionals.

For `K>1`, set `F(y)=arcosh(K cosh y)`. Then `F>|y|`,
`F'=tanh(y)/tanh(F)`, and
`F''=coth(F)(1-F'^2)>0`. With the packet's function `J(a,b)`, direct
differentiation for `a>b>=0` gives

\[
\partial_aJ\ge\tanh a+a\operatorname{sech}^2a
-a^2\operatorname{sech}^2a/\tanh a>0.
\]

Multiplication by `sinh(a)cosh(a)` gives
`sinh²(a)+a tanh(a)-a²>0`, proving the strict sign. Since `J(b,b)=0`
for `b>0`, with the case `b=0` direct, substitution `a=F(y),b=|y|`
gives

\[
F-yF'>\tfrac12 y^2F''.
\]

For a positive-definite symmetric matrix Q, twice differentiating
`q(y)=(F(y),y)Q(F(y),y)^T` gives `q''=2 tr(QP)`, with precisely the
matrix P printed in the packet. Its lower diagonal entry is one and

\[
\det P=F''(F-yF'-\tfrac14y^2F'')>0.
\]

Hence P is positive definite and `tr(QP)>0` for every such Q.
Strict convexity excludes three equal level values, since the middle
one would have to lie strictly below the chord joining the outer two.

When the two vectors s,t in the lemma are independent, the unit circle
is transformed to just such a centered positive-definite ellipse.
After choosing the representative with `s dot u>0`, the gate relation
is its intersection with `x=F(y)`. Three distinct projective directions
would give three distinct `y`, which is impossible. The special case
`K=1` instead gives the union of the two lines orthogonal to `s-t`
and `s+t`, admitting at most two projective directions. When s,t
are dependent, the strict monotonicity of
`cosh(|alpha|r)/cosh r` for `|alpha|!=1` reduces the condition to
equal absolute projections on three projective directions. A circle
intersects the two corresponding parallel lines in at most two
antipodal pairs. Zero vectors and zero projection values are included
in these case checks. The conclusion is exactly `s=+/-t`.

### Negative directional curvature without bounded displacement

For a residual-bearing effective-feature group J, write
`R_J(w)=sum_(i in J) rho_i phi'(w dot u_i)u_i`. If it is nonzero on a
set of positive probability, the canonical lower law gives `Mb_1!=0`
almost surely when `M!=0`. Some component therefore yields the bounded
odd direction

\[
h=(Mb_1)_\ell R_J(w),\qquad
\left[\sum_{i\in J}\rho_iM Da_i[h]\right]_\ell
=E[(Mb_1)_\ell^2|R_J(w)|^2]>0.
\]

The needed density facts follow directly from the canonical coefficients:
each pair `(tanh G_j,tanh(sqrt(tau)Z_j+alpha tanh G_j))` has a
positive density on `(-1,1)^2`; coordinate pairs are independent;
the normalization is an invertible linear map. In particular the
entire law is absolutely continuous, and its density is positive
near zero. This justifies both the null-hyperplane conclusion here
and the later sign argument.

Group orientation signs cause no missing factor: all derivative gates
are even, so the residual-weighted upper variation is

\[
S(b)=b\cdot z_Z+\sum_G(b\cdot z_G)\phi'(b\cdot v_G).
\]

At least one coefficient vector is nonzero. The supplied analytic
separation proof is complete. On a generic line the polynomial term
must first vanish; then at the smallest remaining exponential rate,
division by the line parameter removes the derivative coefficient,
and the undivided limit removes the tanh coefficient. Delete that
whole rate before continuing. Thus coincidences among higher
harmonics do not invalidate the induction. This argument works for
every finite number of effective groups.

For `E=span{H_i}`, set `k=S-P_E S`. This is a nonzero bounded odd
readout direction, orthogonal to every current feature. Direct
differentiation along `(h,s k,0)` gives

\[
\frac{d^2}{d\epsilon^2}L(\theta+\epsilon(h,s k,0))\big|_0
=Q_h+4s\|k\|_2^2.
\]

All terms are finite even for `c in L2`, because the carriers have
unit mass and all features and directional gate variations are
bounded. Taking finite `s` sufficiently negative gives the asserted
negative ordinary second derivative.

For at most three distinct projective input directions, the only
unresolved case of `R_J=0` could be a dependent triple all in one
nonzero signed effective group. Its one-dimensional relation space
forces the three lower gates to have fixed ratios almost surely.
The projective lemma makes the projection of w to the input plane
equal to `+/-s_0`. Therefore `a_i=t_i A`,
`v_i=t_i MA`, with `t_i=tanh(s_0 dot u_i)`. A common nonzero
effective magnitude would force all three `|s_0 dot u_i|` equal,
which the circle-intersection argument excludes. The all-zero
effective group has loss one, outside the theorem. This reconstructs
the claimed negative direction at every H equilibrium with `0<L<1`.

### Exact failure of second Fréchet differentiability

I checked all three equilibrium blocks and the concentrated-direction
argument in the example. For the stated reflected pair and zero
singleton, the moment construction gives predictions `(F,F,0)`,
weighted residuals `(-r,r,-p_3)`, and derivative moments
`(D e,D e,D_0 e)`. The three one-variable upper functions in the
readout construction are independent: on the full real line the
linear growth, the nonzero tanh limit, and then the remaining
derivative feature eliminate their coefficients in that order.
The Gram therefore solves all three prescribed moments with bounded
odd c. Independent symmetric upper coordinates make all its other
derivative-moment components zero.

The readout and middle gradients cancel pairwise; the lower gradient
is a scalar multiple of
`[-2r S D sech²(t)-p_3 D_0]e_2`, which vanishes by the specified
choice of `D_0`. Its loss is
`1-(p_1-p_2)²/(p_1+p_2)`, strictly between zero and one. The individual
vectors `rho_i M^T d_i` are nevertheless all nonzero. Since w is
bounded and g is Gaussian, this is an H state whose lower displacement
does not belong to L-infinity.

For the odd small-support increments, direct substitution gives

\[
\Delta L=4T(h)\int_{E_n}B\,dP_1+O(m_n^2),
\quad \|h_n\|_2^2=2m_nh^2.
\]

The factor four is correct. The effective-vector increments are
uniformly `O(m_n)` because marks and tanh are bounded. The residual
contraction of their second derivative vanishes by `T''(0)=0`;
every other ordinary second-variation term is `O(m_n²)`. Were a
second Fréchet differential present, it would agree with these
ordinary derivatives on each bounded direction `h_n` separately.
The difference between the exact increment and its asserted quadratic
part, divided by `||h_n||_2²`, cannot tend to zero: `T(h)!=0` and
`integral_(E_n) B>=delta m_n`. This proves failure of a Hilbert
second differential, not merely lack of operator-norm continuity of
an otherwise existing Hessian.

### Data criterion and equal-weight corollary

At a dependent triple equilibrium, the lower critical equation is
equivalent to equality of

\[
\phi'(w\cdot u_i)\,b_1\cdot(T_i/\lambda_i)
\]

for the unique nonzero input relation `(lambda_i)`. A single zero
`T_i` forces all of them to vanish by positive gates and the positive
lower Gram. If none vanish, the associated nonzero linear forms
have the same sign almost surely. Positive density near zero forces
them to be positively proportional: any nonproportional pair has
opposite signs on a nonempty open set, and a negatively proportional
pair has opposite signs away from its kernel. Thus their common
linear factor can be cancelled almost surely, giving fixed gate
ratios and again the representation `v_i=t_i V`.

Readout stationarity and finite tanh independence exclude every
nonzero effective singleton, because every residual is nonzero.
Three equal nonzero magnitudes are excluded by the projective lemma.
The only remaining configuration is a nonzero signed pair and a
zero singleton k. Its projected lower vector is perpendicular to
`u_k`, and equality of the two other absolute projections gives
`|u_i dot u_k|=|u_j dot u_k|`. With the intrinsic orientation sign
sigma, equal oriented labels would make both pair residuals zero,
which is impossible under the premise. Conflicting oriented labels
give exactly the stated pair prediction and loss. Loss below one
then requires unequal pair weights.

Therefore all three data conditions are necessary for failure of
individual cancellation. Their simultaneous absence for every
permutation is sufficient for cancellation. Equal active weights
are a valid corollary, including reflected circle geometries and
all choices of binary labels. The source correctly stops short of
claiming that every violation is realizable for every configuration;
the phrase “sharp data criterion” must be read as this proved
sufficient criterion, not an unproved necessary-and-sufficient
classification of all data laws admitting an exception.

## Conditional Hilbert basin and probability mechanism

The complete spectral and nullity dependencies were checked for the
following exact premises at the endpoint: equilibrium; individual
`T_i=rho_i M^T d_i=0`; and a bounded odd direction of strictly negative
loss curvature. No bounded endpoint displacement is needed for these
steps once those premises are supplied.

The finite moment coefficient maps `T_i` are locally C1,1 on H. The
operators `G_i(w)t=phi'(w dot u_i)(b_1 dot t)u_i` are bounded and
Lipschitz as maps from w in L2 to operators into L2. At an equilibrium
with `T_i=0`, the lower field derivative is
`-2 sum_i G_i(w_*) DT_i(theta_*)`; the potentially infinite-rank gate
multiplier vanishes. Subtracting its linearization splits the
remainder into

\[
[G_i(w)-G_i(w_*)]T_i(\theta)
+G_i(w_*)[T_i(\theta)-DT_i(\theta_*)(\theta-\theta_*)].
\]

Both terms have Lipschitz constant `O(r)` on a radius-r H ball.
The other blocks have the same property from local C1,1 regularity.
This proves the small-Lipschitz remainder needed for the graph
construction, with no unproved C1 neighborhood assertion for the
full field.

The derivative is finite rank and self-adjoint in the physical H
metric. In dimension d with m inputs its range is contained in the
space spanned by the `2dm` bounded lower functions, the `(d+1)m`
bounded upper functions, and the `2d²` matrix coordinates. Thus

\[
\operatorname{rank} DF(\theta_*)\le (3d+1)m+2d^2.
\]

Mixed derivatives on bounded directions are symmetric; density and
boundedness extend symmetry to H. Self-adjointness makes the
orthogonal complement of this finite range part of the kernel.
The negative loss direction gives a strictly positive flow
eigenvalue. The spectral projections onto its nonzero eigenspaces
have bounded odd ranges. These are the only changes needed to the
dimension-three finite-range argument when d or m changes.

For a smallest positive flow eigenvalue lambda, radial retraction
of the remainder to a small ball gives a globally epsilon-Lipschitz
remainder, with epsilon arbitrarily small. In the weighted path
norm `sup e^(-lambda t/2)||x(t)||`, the forward center-stable and
backward unstable integral operators have combined contraction
bound `4 epsilon/lambda`. Choosing this below one-half gives the
global closed Lipschitz graph. Bounded original trajectories trapped
in the ball satisfy the same backward unstable integral formula,
because the terminal unstable term decays to zero. Uniqueness of
the fixed path puts every such trajectory on the graph.

Separability of H gives a countable subcover by smaller equilibrium
neighborhoods with closures inside the corresponding trapping
neighborhoods. A trajectory converging to any equilibrium in this
class eventually lies in one larger neighborhood, even when the
chosen center differs from its limit. An integer-time state lies
on that neighborhood's graph. Thus the complete point-convergence
basin is covered by countably many integer-time graph preimages.
Continuity and openness of finite-time maps make these preimages
closed nowhere dense. This uses no countability assumption on the
equilibrium set itself.

For probability nullity, the stronger geometric pullback argument
is also valid. The field has norm Gâteaux derivatives on all of H.
The only delicate term is multiplication by
`phi''(w dot u_i)(zeta dot u_i)`: dominated convergence proves each
fixed directional derivative, and truncating the fixed L2 direction
proves strong continuity in the base state. Derivative norms are
bounded on each H ball. The variational equation along a finite
trajectory then gives an invertible bounded linear derivative for
the time map. Joint continuity of `(theta,h)->DF(theta)h` and a
compact-time subsequence argument justify the uniform error estimate
in the difference-quotient proof; Gronwall gives the claimed
directional derivative and its strong continuity. Solving the
linear equation backwards proves invertibility independently of
an inverse-function theorem.

For a scalar Lipschitz hypersurface, choose a source direction whose
time-map derivative is its target transverse direction. Strong
continuity in just that fixed source direction makes the derivative
stay inside a strict transverse cone in a small product cylinder.
The Banach-valued fundamental theorem of calculus along its lines
gives a uniform strictly positive slope for the scalar graph
equation. Comparing two roots via the cylinder cross-point gives
a Lipschitz root coordinate. The scalar infimum extension of that
coordinate yields a global closed hypersurface containing the local
preimage. No differentiability of the original graph, inverse-map
derivative, or operator-norm derivative continuity is used. Second
countability therefore places the basin inside a countable union
of closed Lipschitz hypersurfaces.

For the proposed probability laws, let `(e_n)` be dense in the
Hilbert unit sphere, with positive summable coefficients `(a_n)`.
The Gaussian series `sum a_n g_n e_n` converges absolutely almost
surely by the finite expectation of its norm sum. Every continuous
linear functional has the asserted Gaussian variance. Finite
coefficient approximations and a small independent tail establish
full support in H. Each hypersurface has an open cone of transverse
directions, containing some `e_n`. Every affine line in that
direction has at most one intersection with every translate of
the hypersurface. Conditioning on all variables except its
atomless coefficient proves probability zero, for each translate.
Countability gives nullity of the entire Borel hypersurface hull.

Replacing the Gaussians by independent uniforms preserves this
nullity and gives a compactly supported witness: summability makes
the coefficient-product image continuous with uniformly small
tails, hence compact. Taking the directions from bounded odd fields
and `a_n=2^(-n)/(1+||e_n||_X)` makes either series converge in X and
preserves all these H conclusions. This does not require X to be
separable; the series lives in the separable closed X-span of its
countable directions. Gaussian nullity for a translated/scaled
series is preserved by positive-probability conditioning on an
open H event.

One scope detail must be retained when extending from bounded
endpoints to arbitrary H endpoints: an affine trapping graph may
be centered outside X. Its intersection with X is still an
X-Lipschitz graph because its unstable range lies in X. Explicitly,
if its affine center is theta_*, write it over `xi in E_cs intersect X`
as

\[
\xi+P_u\theta_*+h(\xi-P_{cs}\theta_*).
\]

The finite-dimensional unstable term belongs to X and is Lipschitz
in its inherited X norm. Thus the relative X category statement,
if used, follows from this graph structure, not from intersecting
an arbitrary H nowhere-dense set with X.

The conditional mechanisms pass. The dependent geometry packet
supplies their premises for triples satisfying its sufficient data
criterion. The explicit non-Fréchet equilibrium lies outside that
criterion, so there is no contradiction. No argument reviewed here
turns these category or probability conclusions into avoidance by
the fixed canonical initial state.

## Bounded-lower endpoints and one-relation finite families

The full functional packet supplies the cancellation premise for
`dim ker U<=1` under the sole endpoint regularity assumption
`w-g in L-infinity`; the endpoint readout may be L2. Its proof is
valid without independence between g and the lower marks.

For a one-dimensional kernel, write its generator as alpha and its
support as J. Lower stationarity makes
`phi'(w dot u_i)(b_1 dot T_i)=lambda alpha_i` almost surely.
Outside J the coefficients vanish directly. If one coefficient on
J vanishes, all do. Otherwise sign agreement and the positive mark
density make `T_i/alpha_i=beta_i V` with all `beta_i>0`. Cancelling
the common nonzero linear form gives a fixed strictly positive
ratio of any two derivative gates on J.

Choose two such distinct directions and a unit e perpendicular to
the first but not the second. On the positive-probability event
`|g-te|<1`, bounded lower displacement keeps the first argument
bounded and sends the absolute value of the second to infinity.
The ratio is bounded by `4 exp(4C-2ta)` with `a>0`, contradicting
its fixed positive value for sufficiently large finite t. The
mark null sets have total probability zero and cannot exhaust
this event; no product of probabilities or conditional independence
is invoked. The proof also handles relations with some zero
coordinates. With no kernel, positivity of gates and input
independence give cancellation immediately.

For any finite number of inputs and any positive-loss endpoint
with `M!=0` and bounded lower displacement, the required negative
direction is established independently of this kernel restriction.
For a residual-bearing group, choose a generic ray with pairwise
distinct nonzero absolute input projections. On a distant Gaussian
ball, dividing its gate sum by the slowest-decaying gate leaves
the unique nonzero coefficient times its input direction, with
uniformly vanishing other terms. Thus the group field R is nonzero
on a set of positive probability. The bounded lower perturbation,
finite-family derivative-feature separation, orthogonal readout
perturbation, and mixed-curvature formula already checked above
then apply without any bound on the number of samples. Pairings
against the endpoint readout use only `c in L2`.

Consequently the finite-rank and small-Lipschitz graph mechanism
applies to every such endpoint when `dim ker U<=1`. The range bound
is exactly `(3d+1)m+2d²`. This includes arbitrary triples in any
ambient dimension and one-relation `m=d+1` configurations; it
does not imply a theorem for several independent input relations.
The X-category statement with merely L2 endpoint readout is
justified by the explicit affine parametrization in Section 7 of
the functional packet, including centers outside X.

The source's loss-one example with equilateral inputs, `w=0`, and
a suitable linear upper readout also checks: all effective features
are zero, readout and middle velocities vanish, and the lower
velocity cancels through `sum u_i=0`, although the individual
coefficients are nonzero. Its displacement is `-g`, hence not
bounded. It demonstrates the need for the stated cancellation
restriction at general losses and does not contradict the equal-
weight sub-loss-one theorem.

The strong-stable assertion in functional Section 6 is valid
conditionally on the stated finite equilibrium: pure readout
curvature supplies a negative flow eigenvalue at `0<L<1`, and
the decaying-path contraction in the complete spectral dependency
gives nonstationary exponentially convergent X trajectories with
strictly decreasing positive limiting loss. No existence of such
an equilibrium for every dependent data law is claimed.

The other Section 6 assertion about an exact compact continuous-
carrier realization is secondary. Its displayed tanh addition
identity and bounded-denominator observation are correct. Its
complete construction source `basin_continuous_carrier.md` was
not assigned and was not read, so this review does not certify
that separate topology theorem. The physical-Hilbert results
reviewed here do not depend on it.

## Integrated theorem and corollaries

The final integration passes within its stated scope. The exact
randomization is a fixed-carrier state randomization with full
Hilbert support and bounded increments, as required by the
reviewed nullity proof; it is not a random draw of the already
integrated canonical population marks.

The final synthesis adds the explicit equilibrium bridge: a
convergent trajectory for a continuous autonomous field must end
at a zero of that field. If the limiting field value were nonzero,
its Hilbert pairing with that value would eventually be bounded
below by a positive constant. Integrating would contradict
convergence of the same scalar pairing of the state. I inspected
this paragraph and verified that removing exactly it and its
following blank line from the final synthesis recovers the entire
initially frozen hash `fa0e6b343b85da2f418fc58f1c1f666c33f3fd00de8bed238f05181770329f26`.
This is a correct completeness clarification, not a change of
theorem or a repair of a false claim.

For equal active weights, the exceptional-pair condition is
impossible. With at most two active representatives, distinct
projective directions are independent; with three, rank three
uses the earlier cancellation and rank two uses the new criterion.
Thus every equally weighted compatible original three-sample law
is covered: if merging changes its active masses, it also reduces
the active count to at most two. There is no hidden minimum-angle
or bounded-limit-field assumption.

For arbitrary weights, the explicit set E is a sufficient
classification of the unresolved data cases. Its geometric
exclusions are proper angle equations. With two projectively
distinct circle angles fixed,

\[
\cos^2(\theta_i-\theta_k)
-\cos^2(\theta_j-\theta_k)
=-\sin(\theta_i+\theta_j-2\theta_k)
  \sin(\theta_i-\theta_j).
\]

The second factor is nonzero. Hence only finitely many remaining
angles are excluded, and the union over three pairs is closed
with empty relative interior and angular measure zero. This
justifies the stated open, dense, full-angular-measure sufficient
class. It makes no claim that every reflected data law is bad.

For arbitrary weighted triples, all regular positive sub-loss-one
endpoints have the checked null basin. The cancellation theorem
places every other such endpoint at one of the listed values

\[
\ell_{ij;k}=1-\frac{(p_i-p_j)^2}{p_i+p_j}.
\]

There are at most three candidate pairs, and each value lies
strictly between zero and one when it belongs to E. Their
minimum together with one is therefore a strictly positive,
data-defined threshold `ell_*`. If initial loss is strictly
below it, monotonicity excludes every irregular positive limit;
the regular positive-limit event is null. Hence state convergence
implies fitting almost surely under the specified randomization
conditioned on this open sublevel. The conditioning event has
positive probability for every fixed translation and positive
scale because the exact fit exists, its strict sublevel is
nonempty open, and the law has full H support. This is conditional
fitting, not a proof that state convergence occurs almost surely.

For balanced binary class masses, after possibly interchanging
the labels, the three masses are `a,1/2-a,1/2` with `0<a<1/2`.
For the same-label pair, the ratio subtracted from one is
`2(2a-1/2)²<1/2`. For a mixed-label pair it is

\[
\frac{(1/2-a)^2}{1/2+a}<\frac12,
\]

because the right denominator times one-half minus the numerator
is `a(3/2-a)>0`. Interchanging the two smaller masses handles
the other mixed pair. Thus every candidate exceptional value
is actually strictly greater than one-half at positive weights;
the claimed weaker bound `ell_*>=1/2` and the sufficient strict
initial sublevel `L(0)<1/2` are correct.

The bounded-lower-endpoint alternative correctly retains arbitrary
H initial states and H convergence while restricting only the
endpoint lower displacement. In the triple case the two-point
projection classification independently rules out an irregular
endpoint satisfying that bound, since a Gaussian projection is
unbounded. The finite-family extension with one relation uses
the stronger functional proof above.

No numerical premise, unassigned source, or external theorem is
needed for these main integrated conclusions. No mathematical
revision is required in the final reviewed synthesis. The
remaining unequal-weight reflection/all-H basin problem, several-
relation finite-family problem, deterministic canonical-state
membership, and absence of a state limit remain unresolved as
explicitly stated in the packet.
