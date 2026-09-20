# Independent review of the frozen input-perturbation report

Review date: 2026-09-18. Reviewer: isolated subagent
`/root/review_input_perturb`. This is an internal mathematical review, not a
promotion review.

**Verdict: PASS for the stated mathematical claims and their explicit local
scope.** I found no correction required in Sections 1–10. In particular,
Section 10 proves the asserted full physical-Hilbert local strict-saddle
theorem under its two amplitude nondegeneracy assumptions and its generic
fixed-tangent condition. It does not prove a global basin-null theorem or a
fixed-noise-radius almost-sure theorem. Those limitations are stated correctly.

## Assignment, isolation, and complete read coverage

The neutral assignment was to check the exact frozen input-perturbation
report, especially its full-Hilbert local theorem, against the supplied
canonical model and complete dependencies. The checks included expansions,
critical prediction grouping, sphere tangency, the L2 topology, actual
Hessian regularity, and probability quantifiers. No experiment was authorized
or performed.

I read every line of the following supplied scientific files. The initial
combined read was truncated inside the candidate; this was repaired by
explicit candidate reads of lines 1–300, 301–620, and 621–872. The canonical
document was displayed completely before that truncation. The functional
dependency was read in two complete blocks, lines 1–400 and 401–789. The
other dependencies were displayed completely in individual reads.

| Input | Lines read | SHA256 |
|---|---:|---|
| `docs/observable_p1.md` | 1–332 | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `studies/p1_sphere_extremes_20260918/input_perturb_frozen.md` | 1–872 | `9574bee85938394e921af31e2437403820788c9a6509ed58b9f47c6014a834a7` |
| `studies/p1_sphere_extremes_20260918/finite_basin_geometry.md` | 1–594 | `379f0b6e7c56ff208b2d7454a7fefbccc3b4eaa24ff9b5e8582a39ae64319b5a` |
| `studies/p1_sphere_extremes_20260918/finite_basin_tail.md` | 1–466 | `8be08e54db97ec23c6b253137f3046a362e82351ee2ff8502addfd176de1dbd2` |
| `studies/p1_sphere_extremes_20260918/dependent_basin_functional.md` | 1–789 | `af691c304d2204b08e76de0ca024241f6c0f2342209f3f8ca08926be2b6173e0` |

All five hashes were checked again after the scientific reading and were
unchanged. The candidate hash agrees with the supervisor's frozen hash.
The functional report was used only for the canonical mark density and
Hilbert regularity dependency, as assigned. Reading its complete body does
not constitute a new review of its unrelated basin theorems.

Process inputs were the supplied AGENTS instructions, `RESEARCH_WORKFLOW.md`,
the `solve-math-rigorously` and `investigate-conjectures` skills, and the
latter's research-contract, evidence-ledger, and adversarial-audit references.
I did not read the study README, other studies, prior verdicts, sibling
reports, or author discussions. I did not retrieve any additional scientific
source. The scientific files themselves contain disclosed historical
comparison sections; these were part of the assigned frozen inputs.

The candidate cites `FINITE_BASIN_EXTENSION.md`, which was not supplied.
Several dependency introductions likewise name earlier reports not supplied
here. I did not retrieve them. No missing assertion from those reports is
needed for the reviewed conclusions: the model, constructions, mark density,
and required regularity estimates are present in the five supplied bodies
and are checked below. Historical claims about previous freezes and internal
checking are not independently certified by this review.

The only file written was this assigned report. Metadata checks recorded
HEAD `019e3630237e33f58b9636c0aa67a039bebf0182`, an empty staged-path listing,
and pre-existing concurrent changes. No Git mutation or other file edit was
performed. Actual tools were text reads, line counts, SHA256 checks, Git
metadata reads, and the report write; no numerical or symbolic experiment
was used.

## Contract checked

The model is the exact canonical p=1 population system in dimension three,
with tanh activation, ridge 1/4096, actual correlated lower marks, independent
upper Gaussian-derived marks, the odd sector, physical L2/L2/Frobenius
metric, and a fully variable 3-by-6 middle matrix. Rank one describes a
particular state or a explicitly restricted continuation ansatz; it is not a
restriction on physical test directions in the curvature statements.

The seven equal-weight sphere inputs are the specified triangle and square
on a positive latitude. The labels are three positive and four negative.
Both supplied square rotations have the moment properties used in the
candidate. The fixed critical prediction is m=-1/7, the weighted residuals
are -8/49 and 6/49, and the critical loss is 48/49. These are equilibrium
and local perturbation statements. They involve no population approximation,
trained-network identification, width limit, flow convergence, or GD claim.

## Checks of Sections 1–9

1. **Reference state and actual Hessian.** The lower-mark density follows
   directly from the smooth bijection
   `(G,Z) -> (tanh G,tanh(sqrt(tau) Z+alpha tanh G))`, followed by an
   invertible linear normalization. Thus every nonzero lower coefficient
   has a zero-probability kernel. In particular kappa is positive and the
   sign field is admissible and odd. The upper marks have positive density
   on an open box. The H,J Gram is positive definite by the analytic
   independence argument. The projected readout has `<c,H>=m` and
   `<c,J>=0`; independence and symmetry of the other upper coordinates
   give every d_i=0. The three weighted moment cancellations verify all
   gradient blocks and give the loss 48/49. The coefficient-cancellation
   regularity estimate applies even though w-g is unbounded. All residual
   second derivatives cancel, while every first prediction derivative is
   `<k,H>`. Hence the actual Hessian is the claimed rank-one operator.

2. **Sign of F'' for the projected readout.** With z>0,
   `H/J=sinh(2zB)/(2B)` is strictly increasing in |B| and
   `K/J=-2B tanh(zB)` is strictly decreasing. The J-squared weighted
   marginal is nondegenerate in |B|. The covariance is therefore strictly
   negative, not merely nonpositive. Multiplication by m<0 reverses that
   sign, giving `<c_0,K> > 0` and F''(s_0)>0. All pairings exist because
   B is bounded. This proof specifically uses the projected readout;
   the report correctly avoids assigning that sign to other readouts.

3. **Sphere derivatives and first-order rank.** Sphere tangency gives
   `u_i·xi_i=0` and `u_i·zeta_i=-|xi_i|^2`, exactly as stated.
   Differentiating the three gradient blocks gives (8), with
   `D'(s_0)=F''(s_0)/(kappa sigma)`. Since the axial coordinate of
   `sum rho_i delta_i u_i` is `C sum rho_i delta_i`, that vector is the
   complete first-order condition. Each delta_i is independently
   attainable by a tangent vector because S>0. The seven u_i span R3,
   so the derivative has rank exactly three.

4. **Second input derivative.** The terms in (10) have the correct
   factors: residual second differentiation gives
   `p_i F''(s_0) delta_i^2 H`, while feature second differentiation gives
   `rho_i(H_1 beta_i+H_2 delta_i^2)`. The functions H,J,K are independent:
   after analytic continuation their asymptotic constant, B-squared
   exponential, and B-exponential scales successively force all
   coefficients to vanish. Since H_1 is a nonzero multiple of J and H_2
   has a nonzero K coefficient, H,H_1,H_2 are independent too. Thus zero
   second readout-gradient derivative forces every delta_i=0. Sphere
   acceleration terms cannot cancel this obstruction.

5. **Exact grouping and frozen-state codimension.** For distinct positive
   slopes, the scalar tanh independence proof is valid even when higher
   exponential harmonics coincide: remove the entire smallest-slope
   function after identifying its zero coefficient, then proceed.
   At readout stationarity, each equal-feature group has its own label
   mean as prediction. A proper group cannot have mean -1/7 because
   `4r=3l` has no permitted nonempty proper solution with r<=3,l<=4.
   The finite mean gap and prediction continuity therefore force one
   group. For the projected readout, F''>0 isolates F=m at s_0. This
   proves precisely the seven independent height constraints and
   codimension seven. The bounded scalar-readout extension is also
   valid: bounded B gives real analyticity under the integral, and
   F(0)=0 excludes the identically constant alternative.

6. **Ansatz continuation.** The same grouping proof applies to a two-point
   lower field, including the stated full-matrix variant with a nonzero
   MA. The common scalar projection places every input in one affine
   plane. Conversely the proposed nearby-plane construction keeps every
   scalar projection at s_0 and every d_i zero, so it is a true
   equilibrium. The first three noncollinear sphere points determine a
   smoothly varying plane; the other four plane constraints have
   independent derivatives because 0<C<1. This verifies codimension
   four, as well as the equivalent three-dimensional allowable span of
   first-order height changes.

7. **Curvature criterion.** Formula (17) correctly retains a mixed
   readout/lower term linear in its free readout multiplier, with a
   nonzero coefficient when mu_1 is nonzero. Formula (18) is the full
   residual pure-lower term. If D=0, Q nonzero and mu_2 nonzero, the
   trace-zero symmetric mu_2 has both eigenvalue signs and supplies a
   negative direction. If D is nonzero, the bounded odd moment-kernel
   function psi exists on the nonatomic carrier. With the explicitly
   stated sign convention, its weighted square has strictly positive
   expectation, so the second term again supplies a negative direction.
   This argument would require a further hypothesis for arbitrary sign
   fields; the report explicitly limits its criterion accordingly.
   Conversely mu_1=mu_2=0 cancels every residual second derivative,
   including arbitrary matrix and readout directions. The distinction
   between directional curvature and an actual Hessian is respected.

8. **Flat-data codimension.** On the nearby plane, the two complex
   Fourier-moment equations give precisely four real constraints.
   A row dependence of their angular derivative would be a degree-two
   real trigonometric polynomial vanishing at seven distinct angles;
   the corresponding degree-at-most-four polynomial must be zero.
   The angular rank is therefore four. Counting three plane parameters
   and seven angles then subtracting four gives dimension six, hence
   codimension eight in the fourteen-dimensional data space. Fixing the
   old plane leaves dimension three and codimension eleven for the
   old state's PSD equilibrium property. The supplied converse using
   c_0 verifies attainability rather than merely a necessary count.

The density-based nullity claims for these finite-dimensional submanifolds
are valid in local sphere charts. They do not require or imply any law on
the state space. No objection remains for Sections 1–9 under their stated
ansatz, sign, locality, and readout restrictions.

## Checks of the full-Hilbert theorem in Section 10

The substantive issue is whether the statement allows arbitrary nearby
L2 lower fields and full matrices, including states depending on eta. It
does. The following checks do not impose a two-point representation on
the perturbed equilibrium.

**Grouping all nearby critical predictions.** Bounded marks and the
Lipschitz activation give continuity of a_i and v_i uniformly over the
finite input list in a product neighborhood of the reference state and
data. L2 pairing gives continuity of predictions. Every v_i can thus be
kept close to v_*, away from zero and from oppositely signed equality.
For distinct vectors modulo sign, a generic line has nonzero, distinct
absolute slopes. The scalar independence proof on that line proves
vector ridge independence, after continuation from the open support box.
Readout stationarity and the same finite proper-group mean gap force
all v_i equal, every prediction m, every d_i the same d, and exactly the
fixed residuals rho_i. No independence between w and b_1 is used.

**Uniform exclusion of nearby ridge critical points.** Directly summing
the triangle's cubic transverse moment gives
`sum rho_i(z·u_i)^3=-(6 S^3/49) Re(z_2+i z_3)^3`; the square contributes
zero. Division by 3! proves the coefficient in (26). Lower Taylor
orders vanish for every axial coordinate a, so differentiating their
vanishing identities also justifies the stated axial remainder order.
The derivative of `a phi'(aC) Delta` is exactly
`[phi'(aC)+aC phi''(aC)] Delta`. These facts prove (27), uniformly on a
fixed compact axial interval and small transverse disk. The two excluded
amplitudes are genuine restrictions of this proof. The example a_*C=1/4
satisfies both: tanh(1/4)<1/4 gives phi'''(1/4)<0 and
`1-2(1/4)tanh(1/4)>0`.

The cubic harmonic is `z_2^3-3z_2 z_3^2`; its gradient norm is exactly
`3|z|^2`. After absorbing the cubic remainder, any hypothetical critical
point has `|z|^2<=K|eta|`. Its axial derivative is consequently
`eta lambda(a) Delta+O(|eta|^(3/2))`, uniformly over that cylinder.
The first term cannot be canceled when Delta is nonzero and eta is
sufficiently small of either sign. This is a fixed-neighborhood result,
not merely absence of a differentiable continuation. Evenness of the
gradient gives the corresponding exclusion at the negative reference
value. The stated C1-curve variant has the necessary o(|eta|) remainder
and is valid too.

**L2 topology and actual Hessian.** From `||w-w_*||_2<r/2`, the mass
where `|w-w_*|>=r` is strictly less than 1/4. The remaining mass lies
in the union of the two fixed balls where R_eta is nonzero. This proves
(31) without an essential-supremum bound or any assumption on conditional
mark distributions. If M^T d were nonzero, its b_1 hyperplane would have
measure zero, contradicting lower stationarity on that positive-mass
set. Thus M^T d=0 and each individual T_i=0.

The supplied regularity argument applies with only L2 lower fields and
readouts. The finite a_i moment maps are C1 with Lipschitz derivatives;
T_i and the upper/matrix field blocks are locally C^(1,1). The lower
gate operator G_i is bounded and Lipschitz into L2. At T_i=0, its
nonlinear contribution is the product of two O(r) factors plus a
C^(1,1) coefficient remainder, with Lipschitz constant O(r) on a
radius-r ball. This is sufficient for an actual bounded Fréchet
derivative of the gradient at the equilibrium. The dangerous lower
multiplication operator has coefficient T_i and vanishes. Every
remaining derivative factors through finitely many moments or matrix
entries. The Hessian is therefore finite rank and self-adjoint. Neither
global C2 regularity nor C1 regularity of the gradient on a whole
neighborhood was silently assumed.

**Strict negative direction and eigenvalue.** The projection k_v is
bounded, odd, continuous in v, and orthogonal to H_v. At the reference,
its induced lower coefficient is q times the strictly positive squared
norm of the component of J_* orthogonal to H_*. Thus ell remains
nonzero nearby. The pure k_v loss curvature is zero, and the mixed
variation has exactly the factor 2 in (35). The selected lower
direction is bounded and odd because R_eta is bounded and even.
Its mixed value (36) is strictly positive: R_eta(w) is nonzero on a
positive-mass set, and a nonzero ell cannot vanish there through a
positive-mass b_1 hyperplane. The combined quadratic value is affine
and nonconstant in the readout multiplier, hence becomes negative.
A bounded finite-rank self-adjoint operator with a negative quadratic
value has a negative eigenvalue on its finite-dimensional range.
This proves the exact stated strict-saddle conclusion.

**Quantifiers.** Delta is a nonzero linear functional on the product
sphere tangent space, since every height tangent functional is
surjective. Its kernel is Lebesgue-null. The conclusion is therefore:
for almost every fixed tangent direction, and any fixed admissible
curve with that initial direction, there is a sufficiently small
nonzero-amplitude interval on which the local theorem holds. The
neighborhood is fixed as eta varies, and equilibrium states may vary
arbitrarily with eta. The amplitude threshold may depend on the
direction and curve. This does not exchange the quantifiers to obtain
an almost-sure statement at each preassigned noise amplitude. The
report explicitly avoids that exchange.

## Component verdicts and unresolved scope

| Component | Verdict |
|---|---|
| Canonical reference state and rank-one Hilbert Hessian | PASS |
| Frozen-state first/second input expansions | PASS |
| Frozen-state exact codimension seven | PASS |
| Coplanar ansatz existence, codimension four | PASS |
| Nearby projected-readout curvature criterion and codimension eight | PASS under the stated sign convention and locality |
| Full-Hilbert local strict-saddle theorem | PASS under (21) and Delta nonzero |
| Fixed-tangent almost-sure formulation | PASS with the direction/curve-dependent amplitude threshold |
| Global disappearance of flat positive-loss equilibria | Not proved and not claimed |
| Global bad-initialization basin nullity | Not proved and not claimed |
| Fixed-noise-radius almost-sure theorem | Not proved and explicitly excluded |

No substantive correctness objection remains within the frozen claim
scope. Exceptional tangent directions, excluded amplitudes, equilibria
outside the local neighborhood, and basin probabilities remain outside
this theorem. Section 10 supersedes the earlier full-state *local* gap
for its added hypotheses; it does not contradict the preserved global
limitations in Sections 1–9. No additional experiment, dependency
retrieval, or promotion step was undertaken.

---

## Separately frozen supplement: robust PSD states under free data changes

The original 300-line review above was completed and frozen before this
supplemental audit, with SHA256
`3d34b698561220dca77d762d9891f4369100f5e066071e0bf8329c89edb1cbd9`.
The supervisor then separately authorized the complete candidate
`studies/p1_sphere_extremes_20260918/input_perturb_persist.md`, SHA256
`641204a025374966da3114bd153f10956d0d9d704d4e6420cd9659ea6cd30dae`.
That hash was verified, and all 608 lines were read in untruncated blocks
1–310 and 311–608. No new scientific dependency or experiment was used.
The candidate's cited `dependent_finite_fitting.md` was not supplied or
read; no result from it is required by the explicit proof reviewed here.

**Supplemental verdict: PASS.** The argument proves that every data
neighborhood of the specified unperturbed triangle/square contains a
nonempty open set admitting an actual physical-Hilbert rank-one PSD
equilibrium at loss 48/49. It proves neither that these equilibria
converge to the old state nor that they have positive-probability basins.
The only issue found is a nonblocking typographical comma in (30),
discussed below.

### Finite critical-point construction

The perturbed point (12) stays on the sphere, and the oppositely rotating
negative pair preserves reflection. Direct differentiation gives
`L_1=-8d/49`, `l=L_1/C`, and the claimed angular contribution
`-12 omega/(49 sqrt(2))` to v. Thus an omega imposing v=2l exists.
Only the positive angle-zero point changes its first coordinate, so the
additional weighted first-coordinate/cosine identity is exact.

The finite transverse sums are as claimed. In particular the triangle's
fourth-power sum is `9(X^2+Y^2)^2/8`, and the square's is
`X^4+6X^2Y^2+Y^4`. Their residual-weighted difference is
`-3P_4/49`; the cubic difference is `-6P_3/49`. This verifies both
coefficients and signs in (14). Differentiating the perturbed arguments
on the axis gives `q=l t phi'(t)` and
`B=phi'(t)[v-2t phi(t)l]`, including the mixed axial/transverse term.

At t_* the values `phi'=2/3`, `phi'''=0`, and
`phi''''=16/(3 sqrt(3))` are correct. The integral estimate for arctanh
proves kappa_*<1 strictly. With epsilon=delta^3, the leading expansion
of Q is a constant independent of (T,x,y), followed by
`K delta^4 [T P_3+P_4/8-aT+bx]`. Differentiating in the original
three coordinates contributes one factor delta inverse, verifying the
common division by `K delta^3` and the limiting equations. Analyticity
of the chosen sphere path supplies the smooth extension and O(delta)
errors. The definitions give a<0, b>0, and -a<b, with their stated
ratio.

For y nonzero the equations reduce exactly to

\[
 T=(y^2-3x^2)/(12x),\qquad
 (x^2+y^2)^2=4bx,\qquad x^3-3xy^2=a.
\]

The radius equation forces x>0. Writing q=x^(3/2) reduces the last
two equations to `4q^2-3 kappa q=a`. Since -b<a<0, the two quadratic
roots are positive, distinct, and smaller than kappa; hence both
displayed y-squared values are positive. The y=0 solution is the
unique negative real cube root of a, with T as in (18). These give
five distinct solutions.

The plane solution's Hessian is invertible by its nonzero T,x
off-diagonal entry and nonzero yy entry. For an off-axis solution,
division by y and elimination of T are legitimate. The reduced
two-variable Jacobian can vanish only when `5x^2=3y^2`, equivalently
`8q=3 kappa`; this is excluded by the two distinct quadratic roots.
Thus all five limiting critical points are nondegenerate. The verified
implicit function theorem gives five nondegenerate critical points
of the original Q_epsilon for each sufficiently small positive epsilon.

The equation `2t_0 tanh(t_0)=1` has exactly one positive solution, and
t_0>t_*. At this point
`q''=l phi'(t_0)[-2tanh(t_0)-2t_0 phi'(t_0)]` is nonzero.
B_0 and K_3 are both negative. With epsilon=r^2 the transverse
equations start at r^2 and the axial equation at r^3, exactly as
claimed. The limiting transverse Jacobian at x=0,y nonzero has
nonzero off-diagonal entries, and the independent T derivative is
q''(t_0). The two extra critical points therefore exist with the
stated O(epsilon) bounds. Their positive limiting t coordinate
differs from t_*, and all seven points and their negatives are distinct.

### Both feature determinant blocks

Reflection produces the stated even dimension four and odd dimension
three. Sum/difference column operations are invertible because each
reflected pair is distinct. All scalings by Y or phi'(t) below are
nonzero for sufficiently small positive epsilon.

For the even block, the three near-t_* columns have independent leading
rows `1`, `delta x`, and `delta^2(x^2-y^2)`, with nonzero multipliers
phi(t_*), phi'(t_*), and phi''(t_*)/2. The identity
`x^2-y^2=2x^2/3+a/(3x)` holds for the plane and both off-axis
solutions. The second divided difference is
`2/3+a/(3x_0 x_- x_+)>0`, since a=x_0^3. Thus their first-three-row
determinant has a nonzero delta^3 coefficient.

Their residual functional values are
`epsilon q(t_*)+O(epsilon delta)`. The near-t_0 column has transverse
coordinates O(epsilon), so its elimination coefficients against the
three t_* columns remain bounded after row scaling by 1,delta,delta^2.
Their sum converges to phi(t_0)/phi(t_*). This proves (25), rather
than assuming an ill-conditioned elimination remains bounded.
The function `q(t)/phi(t)=2lt/sinh(2t)` has strictly nonzero derivative
for t>0, so the last coefficient is nonzero. The even block passes.

For the odd block, polynomial interpolation on the three distinct cosine
values gives exactly (26). The paired data keep their first coordinate
C, and their cosine-polynomial coefficients change only by O(epsilon).
Expanding the normalized feature difference gives the third coordinate

\[
 \delta^3\frac{h_4}{6h_1}
 \left[T(3x^2-y^2)-\tfrac12x(x^2-y^2)\right]+o(\delta^3).
\]

The factor -1/2 comes from reducing xi^3 in the quartic term. No
second-order xi-squared term survives because phi'''(t_*)=0.
Eliminating T and y using the limiting equations yields exactly
`E_j=-7x_j^3/9-7a/18-b/3`. This was checked algebraically, including
the relation
`a^2/x_j^3=36b-16x_j^3+8a`.

For the t_0 pair the third coordinate is
`-epsilon phi'''(t_0) [B_0/(3K_3)]/[6phi'(t_0)]`, namely
`epsilon 49B_0/[18phi'(t_0)]`. Its representation by
`delta^3 h_4/(6h_1) [-(a+b)/3]` is correct because
`a+b=h_1 l/K` and `B_0/phi'(t_0)=v-l=l`. Equation (30) contains
an extraneous comma after epsilon; its intended multiplication is
unambiguous from these two equal expressions. Removing that comma
would improve typesetting but does not change the proof.

After scaling, the odd determinant reduces to the claimed three-point
noncollinearity test. The chord intercept of x^3 at two positive
distinct abscissae is `-x_-x_+(x_-+x_+)`. Substitution gives (31),
strictly positive because a<0. Hence the odd block passes as well,
and the complete seven-by-seven feature matrix is invertible.

### Exact carrier realization and complete Hilbert Hessian

The interpolating alpha is well-defined and can be made to have l1 norm
less than one by choosing lambda positive and small. The stated
probabilities are nonnegative, sum to one, and give the exact signed
weights alpha. Quantile intervals of the continuous variable |G_2|
realize them without adding a carrier or altering its measure.

The use of |G_2| does not break the required correlation checks.
Coordinate-one mark entries factor from |G_2|. For every other mark
entry, even when it depends on G_2 or its reverse noise, the separate
factor E sign(G_1)=0 kills the expectation. Thus (6) is exact.
The partition is even under simultaneous carrier negation and epsilon
is odd, so w is odd. Its finitely many values make w bounded and
w-g square-integrable. Evenness of grad Q makes every selected signed
critical value admissible.

The upper projection does not require the three J functions to be
independent. Their span is finite-dimensional and closed, and H cannot
belong to it because its analytically continued limit at infinity is
one while all three J functions tend to zero. Thus the projected
readout is bounded, odd, and has the exact four moments in (8).
The full vector d is zero. The full upper second-derivative matrix
C_c is zero too: J_2 kills its longitudinal entry, J_0 its transverse
diagonals, and independent centered upper coordinates every mixed
entry. This extra J_0 condition is necessary for the proof to cover
all matrix directions, and it is present.

The residual sum of arbitrary effective-vector first variations
vanishes because all a_i are equal and grad Q(w)=0 pointwise.
Consequently every term in (11), including arbitrary N directions,
cancels after residual weighting. All first prediction derivatives
are the same `<k,H>`. Coefficient cancellation T_i=0 then supplies
the actual Fréchet Hessian by the previously checked L2 remainder
argument. H is nonzero for z>0, so its PSD rank is exactly one.

### Open sets, probability, and compatibility

At each sufficiently small positive epsilon all seven critical points
have invertible Hessians and the feature matrix has nonzero determinant.
The ordinary implicit function theorem can therefore use all fourteen
sphere-chart coordinates as parameters. On the intersection of the
resulting neighborhoods the seven critical points and invertibility
persist. This proves an ambient open set, not merely an open set inside
the reflection family. Such sets can be chosen inside every prescribed
neighborhood of the original data.

A noise law with positive density throughout such a data neighborhood
assigns positive probability to its nonempty open surviving set. This
does not give a uniform probability, probability one, or any initialization
basin probability. The theorem establishes equilibrium existence, not
local minimality or attraction. It also does not claim escape from every
arbitrarily large neighborhood in state space: its precise assertion
is absence of any required continuation to the chosen old equilibrium.
With shrinking lambda the readout need not remain uniformly bounded;
with fixed effective z the matrix may instead grow. This is compatible
with the original local strict-saddle theorem and refutes the stronger
global generic-disappearance claim.

No missing input or substantive proof objection remains for this
supplemental claim. No synthesis or other review was read before
completing this supplement.

---

## Separately authorized synthesis check

The original review and supplemental audit were completed before reading
the synthesis. Their combined 504-line file had SHA256
`b6bfba872336629bbcc0e1dad34dd54296c83ff796b170d2f18bc0ef3ad6a6d3`.
The supervisor then supplied the complete frozen
`studies/p1_sphere_extremes_20260918/INPUT_PERTURBATION_RESULTS.md`.
All 263 lines were read without truncation, and its verified SHA256 was
`8b11f7b5cd50ecc7beee928a1dbac7e0ceec76a2c3e47ada7e68889cd06bd786`.
No README, finite-fitting history, or other review was read.

**Integrated mathematical verdict: PASS for the intended constructed
reference states and the stated local/global conclusions.** The synthesis
does not overstate the open-set robustness, actual Hessian conclusion,
fixed-tangent probability quantifier, or dynamical implications. Two
small scope clarifications are recommended below; neither changes either
proved frozen theorem.

The local statement has exactly two excluded positive preactivation
levels: tanh(t)=1/sqrt(3) and 2t tanh(t)=1. Their uniqueness and
distinctness follow from the monotonicity checks already present in the
packet. The normalized straight sphere path has derivative xi at zero
and is smooth, so the frozen local theorem applies. Full-Hilbert changes
are allowed, and the fixed-direction/amplitude order is preserved.

The remote construction uses precisely these two excluded levels and
is free to choose entirely different lower-field support and readout.
Its open surviving data sets refute generic global disappearance of
all positive-loss PSD equilibria under a positive-density data law.
This remains an existence assertion over states and does not identify
or quantify any attracting basin. The synthesis correctly keeps the
codimension results confined to their frozen-state or explicit-ansatz
scope and does not replace the stronger statements with them.

The general mixed-variation necessity argument in Section 3 is valid
at a common nonzero-feature equilibrium with prediction m. If W is
nonzero, `(b_2·W) phi'(b_2·v)` cannot be proportional to the common
tanh feature: restrict a putative analytic identity to a line with
both slopes nonzero and compare its decaying and nonzero limiting
terms. Orthogonal projection supplies the required nonzero readout
direction. The bounded odd choice
`h=(Mb_1)_j grad Q(w)` gives strict positivity whenever grad Q(w)
is nonzero on positive population mass and row j is nonzero. Thus the
support condition and its use in the local argument are justified.

The two recommended wording clarifications are:

1. **Reference readout in Section 2.** Say explicitly that
   `c_*=c_*(b_{2,1})`, or select exactly the stated Gram-projected
   readout. The two displayed moment equations alone, for an arbitrary
   odd scalar-valued readout, do not imply zero transverse backward
   components. For example, adding
   `b_{2,2} phi'(z b_{2,1})` to the projected readout preserves both
   equations but changes d_2 by
   `E[b_{2,2}^2 phi'(z b_{2,1})^2]>0`. The intended one-coordinate
   constructed readouts do have every d_i=0, and both frozen reports
   use those readouts. This is a description ambiguity, not a failure
   of their construction.
2. **Support condition in Section 3.** Retain explicitly the common
   nonzero feature and prediction m in the sentence preceding (1).
   They are guaranteed by the preceding nearby-state argument and by
   the later interpolation construction. For a zero common feature,
   predictions would instead be zero, so the fixed residual function
   Q with coefficients `(m-y_i)/7` could not be used without a new
   justification. No reviewed conclusion needs that broader reading.

With these intended scopes understood, no further objection remains.
The report's declarations of study status and historical checking were
not audited beyond the actual frozen hashes and read coverage recorded
here.

## Further frozen cubic-descent corollary and first synthesis repair

After completing the preceding audits, the supervisor supplied
`studies/p1_sphere_extremes_20260918/input_perturb_cubic.md`, verified
SHA256 `b050e2045487ebc1d5c1784ff6fa2cee7f348ba3207284f9bcb5a58805349020`.
All 105 lines were read completely. Only the already reviewed canonical
model and persistence construction were used as dependencies.

**Cubic-descent verdict: PASS.** The selected positive-probability
assignment event depends only on |G_2|. The spare centered even G_3
function kills every coordinate-one lower moment; for every other
coordinate-pair mark the independent sign(G_1) factor kills the moment,
even where that mark correlates with the event or G_3 function. Thus
Da_i[h]=0 exactly, and h is bounded and odd.

The readout direction is bounded, odd, and orthogonal to H, with its
longitudinal induced moment D_k equal to its strictly positive squared
norm. All first effective-vector variations vanish. Since d=0, both
first and second prediction derivatives are zero, and the third is
exactly `3t D_k q^T D^2a_i[h,h]`. Hence the unhalved loss derivative
has the factor 6 in (4). Oddness of Q makes its Hessian odd, and
independence of the three coordinate pairs reduces the carrier
expectation to the displayed product with sign sigma_0. Nondegeneracy
of the selected critical point supplies a vector r with a nonzero
quadratic Hessian value. All other product factors are strictly
positive. A sign choice of t therefore gives cubic descent and ascent
on the two sides of this bounded physical path.

The claim covers every state from the seven-nondegenerate-critical-point
construction, including the open sets of freely changed data. It does
not automatically cover an amplitude-zero limit whose critical points
may be degenerate. The loss is smooth along the bounded path, which
justifies Taylor expansion despite possible lack of general higher
Hilbert derivatives. The conclusion rules out a local minimum and
attraction of an entire neighborhood to that point. Loss continuity
and monotonicity justify the latter statement; no sign or size of a
proper basin is inferred.

The supervisor also supplied the repaired synthesis at SHA256
`9ac018610bc57ab73f88bfe20bd993ec8ea037bb170c756c56a4b2855ee29195`.
I read all 263 lines of that replacement completely. It explicitly
chooses c_*=c_*(b_{2,1}) and explicitly retains the nonzero common
feature and prediction m. These resolve both precision notes from
the preceding synthesis audit. **The repaired synthesis passes.**

## Final frozen bounded-continuation, direction, and fitting addendum

The supervisor separately supplied the complete
`studies/p1_sphere_extremes_20260918/input_perturb_bounded_continuation.md`,
verified SHA256
`5450edff98391be754d75117c96cf039348dad6d7a5ea97710b9dc80f3a7ebda`.
All 415 lines were read completely in one untruncated output. This audit
used only the already reviewed scientific packet. **Verdict: PASS for
all five sections.**

### Bounded inverse on the particular interpolation target

Reflection and V invertibility force `V^-1 1` to have equal coefficients
within every reflected pair. Replacing columns by their means gives the
stated coefficient splitting and exactly preserves the l1 norm.
The four even-coordinate basis vectors are independent because a
quadratic cannot vanish at the three paired cosine values unless zero;
the remaining e_0 vector has a nonzero residual pairing. The compressed
residual functional uses the original seven weights on even vectors,
including paired multiplicities. It annihilates 1,xi,xi-squared and
takes value -8/49 on e_0.

The coordinate change is fixed in epsilon, and its constant target is
exactly (1,0,0,0). Dividing rows by 1,delta,delta-squared,epsilon
therefore does not amplify the target. The feature Taylor expansion
gives precisely the matrix A_* in (4). A term proportional to Y-squared
also changes the constant coordinate but vanishes in that unscaled
row; the xi-squared coefficient is correctly proportional to
X-squared minus Y-squared. Axial and angle changes have the orders
claimed, and the single changed axial entry lies in the e_0 direction.
The t_0 pair contributes zero to the limiting second and third rows.

The earlier positive divided difference proves invertibility of the
first three columns in the first three rows. The fourth row's remaining
coefficient is (5), nonzero by strict monotonicity of q/phi. Thus A_*
is invertible. Continuity of the inverse proves the asserted convergence
and boundedness of this particular interpolant, despite degeneration
of the unrestricted V inverse. No uniform bound on every interpolation
target has been inferred.

### Coupled carrier continuation and a different limiting state

The probability formula in (7) has strict slack, and every signed
assignment probability is uniformly positive. All probabilities vary
continuously, including at zero. With one fixed ordering of intervals
of the same uniform transform of |G_2|, the outcome converges off a
finite set of null boundaries. Uniformly bounded critical values then
give almost-sure and L2 convergence of the lower field by dominated
convergence. The same fixed lambda keeps the effective vector z e_1
fixed, so both M and the complete projected readout can indeed be
fixed for the whole seed continuation.

The actual lower fields and readouts are bounded, and all physical
Hilbert state norms are uniformly bounded. This does not say w-g is
essentially bounded; the displacement retains the Gaussian g.
The limit has positive mass at both distinct magnitudes, with no
other magnitudes. The limiting interpolation identity preserves the
same common lower moments. The original first-moment cancellation
makes every axial lower value a critical point of Q. The original
full Hessian argument with d=C_c=0 consequently proves the limiting
equilibrium and rank-one PSD Hessian directly.

Both magnitude masses sum to one and are positive. Applying the
reverse triangle inequality pointwise and minimizing the resulting
weighted quadratic over the old magnitude proves both inequalities
in (12). Thus the limit stays at positive L2 distance from every
single-magnitude lower field, whatever its sign partition. This is a
stronger compatibility statement than possible norm divergence and
does not contradict the old local theorem.

At each positive seed amplitude, root continuation and inversion are
continuous in freely changed data. Neighborhoods can be shrunk to keep
root and interpolation changes at most epsilon. The original strict
probability slack keeps the same lambda admissible; the same interval
coupling and fixed M,c then give uniform bounds and convergence along
any such shrinking-neighborhood sequence. No lower bound on the data
neighborhood radii is claimed or needed.

### Open fixed-direction family

The normalized affine sphere paths are real analytic and have the
prescribed tangent derivative. At the seed velocity they preserve
reflection and differ from the first construction only at order
epsilon-squared. Those differences occur above every decisive order
in the root and determinant calculations.

For unrestricted nearby velocities, the divided equations are jointly
analytic after epsilon=tau^6. At t_* their unperturbed leading powers
are tau^6 because phi'''(t_*)=0; the data perturbation also starts at
tau^6. At t_0 the transverse equations start at tau^6. The otherwise
potential tau^6 axial term vanishes for every velocity because
`q_xi'(t_0)=0`; its first nonzero allowed terms start at tau^9.
Second data changes start at tau^12 and cause no negative powers.
These divisibility checks justify the analytic extensions, rather
than merely pointwise limiting formulas.

The seven limiting unknown-variable Jacobians are invertible. The
analytic implicit function theorem therefore supplies jointly analytic
root branches with nearby nondegeneracy. Their scaled limiting roots
are distinct, so the original roots remain distinct for positive
tau sufficiently small. At the seed velocity the even feature
determinant has order tau^12, the normalized odd determinant has
order tau^8, and restoring the three odd normalizations contributes
tau^7. This verifies the nonzero tau^27 coefficient of the full
determinant, also for the normalized affine seed path.

The coefficient C_27 is continuous in velocity and stays nonzero on
an open neighborhood. For each fixed velocity the determinant is
therefore a nonzero analytic function of tau. Factoring its first
nonzero Taylor power proves eventual nonvanishing for all sufficiently
small positive tau. Lower coefficients may change with direction,
so this argument correctly gives a direction-dependent threshold.
It does not give uniform boundedness of the interpolation coefficients
or states on the whole open direction family. Positive velocity
rescaling only reparametrizes amplitude; radial projection of an open
neighborhood away from zero gives the stated open unit-direction patch.

### Exact zero loss

Using target (1,2,...,7) and a separately small positive lambda gives
seven distinct positive upper tanh slopes on the unchanged carrier.
Their analytic independence follows by the smallest nonzero slope's
leading exponential term after subtracting the constant limit. Their
exact Gram is positive definite. The proposed finite linear-combination
readout has predictions y exactly, is bounded and odd, and hence gives
loss zero. This establishes attainable architectural loss zero on all
the constructed data, without making a training or reachability claim.

## Integration check of the strengthened synthesis

The complete 305-line synthesis at SHA256
`4408a1696924250fef3c73449d45d12b591d3df18de0343fd3425e60b4138e3b`
was then read completely. It correctly incorporates the seed-path
bounded continuation, shrinking open data neighborhoods, the separate
open fixed-direction existence statement, and exact zero-loss fitting.
The local/global and probability quantifiers remain correct.

One final wording clarification was requested: the statements that
"Each newly constructed PSD state" and "The new states" have cubic
descent should explicitly say positive noise amplitude. The cubic
corollary uses nondegenerate critical points, while the newly
constructed zero-amplitude axial limit has `D^2Q=0` at all of its
support values by the original second-moment cancellation. The packet
does not establish cubic descent at that limit. This does not affect
any positive-amplitude state or any bounded-continuation, strict-saddle,
or zero-loss theorem. It is a scope clarification in the synthesis.

## Final integration verdict

The final replacement synthesis was read completely, all 305 lines,
at verified SHA256
`6fd0ce34f10647dbf50ccf7fb8bbf35136fbfac360251efb612221c71ffb88eb`.
Both cubic-descent statements now explicitly refer to positive noise
amplitude. This resolves the last scope clarification. **Final verdict:
PASS for the original local theorem, the robust PSD construction, the
bounded seed continuation, the open fixed-direction family, positive-
amplitude cubic descent, zero-loss fitting, and the final synthesis.**

There are no unresolved substantive objections within those stated
scopes. The old single-magnitude local theorem is compatible with the
different bounded two-amplitude limiting state. Uniform state bounds
are confined to the seed continuation and its suitably shrinking open
data neighborhoods. The open tangent-direction theorem has only
direction-dependent amplitude thresholds and no uniform state bound.
The cubic proof applies to the positive-amplitude nondegenerate-root
construction; the zero-amplitude limit's cubic behavior remains
unclaimed. No basin-probability, canonical-training, or promoted-book
claim has been inferred.

This completes the authorized mathematical review. All source versions
and complete read ranges are recorded in the preceding sections.
The persistence report's cosmetic comma remains attached to its frozen
reviewed hash; any later typesetting-only repair is outside this final
source freeze. No experiment, new scientific retrieval, or write outside
this assigned report was performed.
