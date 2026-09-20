# Isolated review of the continuous-carrier and basin framework

Review date: 2026-09-18. This is an internal mathematical review, not a promotion
review. No empirical work was performed and no candidate source was edited.

## Frozen inputs and scope

The initial assignment supplied `basin_continuous_carrier.md`, SHA-256
`3570b140e391f762363be25cd1ab1c061855f2a8ae2bfd5d5fe448ba5cff87b5`.
Its permitted scientific dependencies were the complete
`docs/observable_p1.md`, the exact state/equations/existence material in
`docs/global_nonlinear.md` C.4.7.9.3--4 and C.4.7.10.D.3, and the complete
own-study `plateau_finite_critical.md`.

The supervisor subsequently supplied, and explicitly authorized complete
reading of, these frozen supplementary inputs:

* `basin_probability_route.md`, SHA-256
  `2afe5cbdcf72961d2713f1b778f276472ed56f8fd05e6bf81a61de340d9603a2`;
* `rank_one_nonlinear_obstruction.md`, SHA-256
  `07b481e396584ebbcfb30b155b157778179a6c11c929a85376e94e31d072784c`;
* `basin_spectral_route.md`, SHA-256
  `baab073c128990f035ece90f3ac7b0dea15e2f57e9c99849aac7aea7732f051e`;
* `basin_hilbert_landscape.md`, SHA-256
  `816527cfb86c14f5e319023d67effc900c25ec1c608a26e52b8fc36f4bdb2567`;
* `basin_open_fitting.md`, corrected SHA-256
  `dea26f190a47d292a3de27d9e15ad645f5ff2e5444b4825c986d52ecb7ed9175`;
* `basin_hilbert_null_extension.md`, original reviewed SHA-256
  `acb04b58dba1c16859cbcd6587168ae8f29a66474227b8327807252d2b7a1ca8`,
  display-repaired final SHA-256
  `cf0b0cf735f281e7d5c7b0dbd53ab9987933de4fe031d8d3644911a0aff2f473`;
* `basin_escape_route.md`, SHA-256
  `ae5eb9716505d790bd7fffcfbba4c5f85d7aab98145e8ddaa19b272048e46553`;
* `basin_hilbert_fitting.md`, SHA-256
  `ec0321804d55c1b85b5ee8d748602c5a362aa0aa7c7771f10967c153e1ec482f`;
* final integrated `BASIN_RESULTS.md`, SHA-256
  `45315a08179f83a9ec811562f95a704aea586514cc67e4cffb4539c246017a4d`.

The probability route is used only through Sections 1--5. Its Section 6
uses an activation-zero reference which need not correspond to bounded
`w-g`, and is excluded from the reviewed continuous-carrier conclusions.
Its strong-stable construction is not needed: the spectral route supplies
a separate construction at admissible finite equilibria.

Dependency hashes checked during this review were
`3aa693f975862230fec875ab787de48f56116814afd37f52be6b66a042f54ffd`
for `plateau_finite_critical.md` and
`0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`
for `docs/observable_p1.md`. The whole-file metadata hash for the scoped
sections of `docs/global_nonlinear.md` was
`81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
Only the authorized scientific sections were used. References from the permitted reports to
other study material were not followed. No study README, history, other
review, or other study was used. The required investigate-conjectures and
solve-math-rigorously skills and the research-contract/adversarial-audit
references were read.

To avoid a notation collision, this review writes `X_c` for the
continuous-carrier space, `X_infty` for the bounded-measurable space of
the spectral report, and `H` for the physical Hilbert space.

## Component verdict

**Final integrated PASS for `BASIN_RESULTS.md` at the hash above and
the complete supplied carrier, spectral, landscape, probability, and
fitting chain.** No blocking
mathematical error was found. The initial carrier construction preserves
the exact canonical law, its forward flow has the asserted regularity,
and its critical Hessian has rank at most 48 and both signs when
`0<L<1`. The spectral report supplies the previously missing local
trapping graph using an equilibrium-specific Hilbert estimate. The
probability report correctly derives category and explicit randomization
conclusions from graphs and a `C1` flow. The later Hilbert-null extension
supplies a separately valid weaker-regularity route directly on `H`.

Combined with the full-Hilbert landscape lemma, the reviewed chain proves
an `F_sigma` meagre shy hull, null under the stated explicit Gaussian
randomizations, for all initial states whose trajectory has an `H` limit
with loss in `(0,1)`. The limit need not be bounded or continuous. This
does not exclude the prescribed deterministic initialization from that
basin, or assert convergence of every trajectory.

The fitting construction and its Hilbert extension additionally prove
a nonempty open fitting basin in `H`, with exponential endpoint
convergence, and a separate continuous-field region with the stronger
supremum/Frobenius convergence. Exact nonstationary trajectories
converging to positive-loss equilibria also exist from other starts.

## 1. Exact compact carrier and canonical initialization

The normalized odd features in `observable_p1.md` are bounded, including
the ridge-normalized reverse-derived coordinates. Their pushforward
support together with the three initial training activations is therefore
a compact metric subset of a finite-dimensional box. Using its actual
pushforward probability preserves every correlation. In particular this
does not sample an independent copy of `g`, alter the Gaussian tails, or
replace population expectation by quadrature.

For each finite Gaussian realization, `|z_i^0|<1`. Thus the boundary
`|z_i^0|=1` has zero measure, although it belongs to the topological
compactification. The first three odd lower coordinates are
`tanh(g_j)/a`, where the positive constant `a` is fixed by the exact
normalization. Hence `g_j=artanh(a b_{1,j})` almost surely. The other
three coordinates similarly recover the reverse tanh variables, and
then their Gaussian reverse roots. Consequently the compact coordinates
retain the entire lower initialized mark information up to null sets.
The upper coordinates similarly recover their Gaussian roots. This also
identifies the Hilbert completions with the canonical finite Gaussian
carrier spaces used by the spectral report.

The identity

`tanh(g.u_i+v.u_i)=T(z_i^0,v.u_i)`

is the exact addition formula. Its denominator stays uniformly positive
when `v` is in a fixed bounded state ball. Thus the added boundary has
a continuous dynamical extension without changing any population
integral. The field displayed in the candidate is exactly the canonical
physical field, including the actual transpose of the complete `3 x 6`
matrix and the factor two for unhalved loss. Its initial state is the
single deterministic point `(0,0,D)`.

The supplementary obstruction resolves the initial packet's otherwise
unspecified reference to explicit bad states. Its displacement (7) is
linear in `b_1`, hence continuous and odd on `K_1`. Its readout (10) is
a finite combination of `tanh(B_1)`, `B_1 sech^2(B_1)`, and `B_2`, hence
continuous and odd on `K_2`. The positive normalization denominator in
(9) is justified by nonproportionality on the upper density interval.
Thus these actual admissible stationary examples, including the
zero-backward-response variant, belong to `X_c`.

## 2. Separable smooth flow and the physical metric

Continuous functions on each compact metric carrier are a Banach space
in supremum norm and have a countable dense set. The rational-polynomial
argument is valid: real polynomials separate points and contain
constants, real Stone--Weierstrass gives density, and finitely many
coefficients can then be approximated rationally. Odd symmetrization
preserves density in the closed odd subspace. Finite products with the
matrix space preserve separability and completeness.

Uniform scalar Taylor remainders on a bounded state ball justify every
Fréchet derivative of `T(z_i^0,v.u_i)` as a map into continuous fields.
All other gates have bounded arguments on such a ball; integrations are
bounded linear maps. Products and compositions therefore give a `C∞`
vector field with locally bounded derivatives. The simultaneous-sign
parities are correct in each block.

Full support makes the inclusion `X_c -> H` injective. The exact
gradient belongs to `X_c`, and differentiation of the bounded integrands
gives

`L'=-||v'||_2^2-||c'||_2^2-||M'||_F^2`.

For arbitrary initial `X_c` states, weighted Cauchy--Schwarz and energy
monotonicity bound `sum_i p_i |r_i|` by `sqrt(L(0))`. Thus the readout
supremum grows at most linearly on a finite horizon, the matrix has a
finite quadratic bound, and the lower displacement has a finite
polynomial bound. Local speed bounds give Cauchy endpoints, so local
existence continues through every finite positive time.

The forward time map is injective by uniqueness. Along any finite
trajectory segment, solving the reversed local equation from nearby
terminal data gives a neighborhood in its image. The variational
equation has continuous bounded-operator coefficients along that
segment; its inverse is obtained from the reversed linear equation.
Together with `C1` dependence on initial data, this gives a `C1`
diffeomorphism onto the open image. No negative-time completeness or
all-time boundedness is used.

## 3. Rank 48 and both signs of the critical Hessian

At a critical point, the lower gradient is zero as an odd continuous
field. Linear independence of the three inputs separates its scalar
coefficients almost surely. The positive lower gates and positive
definite lower Gram then imply

`p_i r_i M^T d_i=0` for every `i`.

This cancels the sole derivative term which acts by local multiplication
on the lower variation. More explicitly, differentiating the lower
gradient leaves linear combinations of
`b_{1,j}(1-h_i^2)u_i`. Differentiating its readout block gives linear
combinations of `H_i` and `b_{2,k} phi'(b_2^T M a_i)`. The matrix block
already has 18 dimensions. The total range bound is therefore

`18 + (3+9) + 18 = 48`.

Each remaining coefficient is a bounded linear Hilbert moment of the
variation; for example
`delta a_i=E[b_1(1-h_i^2)(delta v.u_i)]` and the two terms in `delta d_i`
are a readout moment and a bounded coefficient times
`delta(M a_i)`. Thus the Hessian extends boundedly to `H`. Symmetry
extends from the dense continuous fields, giving a finite-rank
self-adjoint Hilbert operator. Its range consists of continuous odd
fields. Nonzero eigenvectors therefore lie in `X_c`; their finite
Hilbert projection formulas are bounded on `X_c`. This proves the
claimed positive/negative/kernel splitting in the Banach space.

When `0<L<1`, `M=0` is impossible because it gives every prediction zero
and loss one. The strict-saddle construction in the permitted plateau
report applies, since independent inputs are distinct modulo sign.
In fact its perturbations are already in `X_c`: its lower direction is
`(M b_1)_k` times a finite sum of continuous even gates times input
vectors; its readout direction is a continuous upper function minus its
projection onto a finite span of continuous upper features. The
nonvanishing separation and mixed second-variation calculation yield
the strictly negative quadratic form. Hence the candidate's proposed
Hilbert approximation is valid but unnecessary here.

For the opposite sign, some `H_j` is nonzero whenever `L<1`. The pure
readout perturbation `delta c=H_j` gives

`D²L[delta c,delta c]=2 sum_i p_i <H_j,H_i>²>0`,

with strictness from `i=j` and `p_j>0`. Both signs are consequently
present. For the flow Jacobian their signs reverse, exactly as stated.

## 4. The supplemental Hilbert remainder and trapping proof

The spectral report correctly avoids asserting a `C1` Hilbert flow.
An `L2` gate Nemytskii map need not be Fréchet differentiable. The
finite moment map is different: integration makes its Taylor remainder
bounded by `C||delta v||_2²`, and the norm of the difference of its
derivatives is bounded by `C||v-v_tilde||_2`. Thus the finite moments,
the coefficient maps `T_i`, and the upper/matrix vector-field blocks
are locally `C^(1,1)` in the required Hilbert norms.

The lower block is locally Lipschitz on `H` because its gate has an
`L2` Lipschitz bound and its state-dependent coefficient is pointwise
bounded. It need not be differentiable on a neighborhood. At an
equilibrium, however, each `T_i` vanishes. In the report's equation
(11), the first product has two factors of size `O(r)` on the radius-r
ball, each with bounded Lipschitz constant. Its difference is therefore
`O(r)||x-y||_H`. The second term is a `C^(1,1)` Taylor remainder with
the same bound. This proves the actual equilibrium derivative and the
small-Lipschitz estimate (12), without an illicit Hilbert smoothness
assumption.

The extension of the exact field to all of `H` is meaningful, locally
Lipschitz, and satisfies the continuously differentiable loss identity.
The polynomial energy bounds give global forward existence there. The
locally reversed equation proves open time maps with locally Lipschitz
inverses, which is sufficient for the spectral report's category claims.

The radial retraction used to globalize the remainder is indeed
2-Lipschitz in an arbitrary norm. For example when `||x||>=||y||>=r`,
subtracting the two radial factors gives at most
`(r/||x||)(||x-y||+||x||-||y||)<=2||x-y||`; the mixed inside/outside
case obeys the same bound, and the inside case is the identity.
Composition therefore retains an arbitrarily small global Lipschitz
constant after reducing the ball radius.

The Lyapunov--Perron equation (19) is a contraction on the stated
complete weighted continuous-path space. The two convolution norms are
`epsilon/gamma` and `epsilon/(lambda-gamma)`, so choosing
`gamma=lambda/2` gives the claimed bound `4 epsilon/lambda`. Its
fixed-point graph is closed and Lipschitz over the center-stable
subspace. Every orbit trapped in the original ball satisfies the same
integral equation: its backward terminal unstable term vanishes, and
the improper integral converges. This is the stronger all-trapped-orbits
property required by the probability report, including convergence to
an equilibrium different from the graph's chosen center.

For `X_infty`, intersecting this Hilbert graph is legitimate because
the finite unstable eigenvectors are bounded. The restriction is an
`X_infty`-Lipschitz graph over the spectral complement. This is a
specific graph argument, not the false general principle that the
intersection of a Hilbert nowhere-dense set with any stronger space is
nowhere dense.

## 5. Countable covering, hypersurfaces, and explicit probability

The countable-cover argument is valid even for an arbitrary uncountable
or nonmeasurable equilibrium set. A separable metric space has a
countable base, and every subspace is Lindelöf. Select a countable
subcover by smaller equilibrium neighborhoods. Any convergent orbit is
eventually trapped in the corresponding larger neighborhood, so some
integer-time image belongs to its graph. This gives a countable union
of backward graph images, without asserting that the limiting point is
one of the chosen centers.

In the spectral report, continuity and openness of the Hilbert and
bounded-field time maps preserve closedness and empty interior of the
backward images. This proves its stated category conclusion, including
Hilbert convergence from bounded-field initial data.

In the probability report, positive-codimension Lipschitz graphs are
contained in scalar hypersurfaces by projecting along any nonzero
complement direction and extending the scalar Lipschitz function.
Under a local `C1` diffeomorphism, the displayed difference estimate (3)
is correct after using inverse-derivative coordinates and making the
nonlinear remainder's Lipschitz constant sufficiently small. It gives
a scalar graph on a projected subset, and scalar Lipschitz extension
gives a global hypersurface. Second countability supplies a countable
cover of all such local preimage pieces. Thus an `F_sigma` hull made of
closed nowhere-dense global Lipschitz hypersurfaces is obtained.

For the explicit probabilities, fix a dense sequence of unit directions.
Every hypersurface has a nonempty open cone of directions whose lines
meet it at most once. A member of the dense sequence lies in that cone.
Conditioning the uniform or Gaussian random series on every other
coordinate reduces membership in any translated hypersurface to at
most one value of an atomless scalar variable. The set is Borel, so
Fubini applies; countable subadditivity gives nullity of every translate
of the entire hull. The uniform series converges uniformly over the
compact coefficient product, giving compact support. The Gaussian
series is absolutely convergent almost surely by its summable expected
norms; every continuous linear functional is Gaussian. The given
finite-head/independent-small-tail argument verifies full support.
These proofs do not presume an infinite-dimensional Lebesgue measure.

All of probability Sections 1--5 apply on `X_c` with displacement
coordinates, once the graphs being pulled back are graphs in `X_c`.
The reference point for random perturbations is `(0,0,D)`, not the
generic activation coordinate denoted `z_0` in that report.

## 6. Strong-stable trajectories and integration boundary

The spectral report's decaying-path contraction (23) has the stated
operator bounds. For small stable coordinate it stays inside the region
where the radial retraction is inactive, so its fixed point is an exact
trajectory of the original equation. The quadratic local remainder
gives `h_ss(xi)=O(||xi||²)`. Nonzero stable coordinate excludes the
equilibrium, and finite-time uniqueness excludes hitting any equilibrium
later. The energy identity and convergence then give strictly decreasing
loss with the prescribed positive limit. Its initial loss can be kept
below one by continuity.

This construction also runs directly on `X_c` at its continuous
equilibria: the finite spectral projections preserve `X_c`, its field
is `C∞`, and all semigroup and contraction estimates use the indicated
equivalent split norms. The explicit obstruction supplies such an
equilibrium for every independent input triple, positive weights, and
binary labels. Thus exact nonstationary positive-limit trajectories
exist from other initial fields within the continuous-carrier model.
No intersection with the canonical initial point is shown.

An integration using only the continuous-flow argument would encounter a
trajectory starting in `X_c` which converges only in `H` to a finite
equilibrium outside `X_c`. Its Hilbert unstable eigenvectors can be
merely measurable, so the simple spectral graph-intersection formula
(21) cannot automatically be applied to `X_c`. A valid integration can
instead choose a continuous direction in an open Hilbert transverse
cone (using density), restrict the hypersurface along that direction,
and prove a scalar Lipschitz graph in the stronger `X_c` norm. The final
Hilbert-null extension reviewed in Section 9 avoids that restriction
step altogether, by proving backward-image geometry directly in `H`.
No unproved dense-intersection assertion is needed in the final chain.

Neither component result proves avoidance from the single canonical
initialization. Neither finite dissipation nor finite-time existence
supplies all-time compactness. The probability route's excluded
activation-zero Section 6, dependent input extensions, positive-loss
escape, and distance approach to an arbitrary compact continuum of
equilibria are not included in this verdict.

## 7. Supplemental full-Hilbert landscape extension

**PASS for the complete frozen `basin_hilbert_landscape.md`.** The
gated matrix `K_i=E[b_1 b_1^T phi'(w.u_i)]` is positive definite at
every Hilbert state: `w` is finite almost surely, so the gate is strictly
positive; for nonzero `q`, positive definiteness of the ungated Gram
ensures `(b_1.q)^2>0` on a set of positive measure. Boundedness of marks
also makes every matrix entry finite. No uniform lower eigenvalue
bound over states is asserted or needed.

The dual-input variation `t_i(b_1^T K_i^{-1} A)` is bounded and odd,
changes `a_i` by precisely `A`, and leaves the other lower moments
unchanged to first order. This avoids importing the bounded-displacement
Gaussian-tail argument into an unbounded Hilbert state.

The derivative-feature separation proof is complete. Positive upper
density upgrades an almost-sure analytic identity to an identity on
an open cube; restriction to a generic line extends to all real scalar
parameters. After grouping equal/opposite features and orienting the
rates positively, the least nonzero tanh coefficient has a nonzero
constant multiple of `exp(-2 a_min s)` as its leading tail. It cannot
equal `C s exp(-2 a s)`: division by the former exponential gives either
zero or unbounded magnitude on the right and a nonzero finite limit
on the left. The zero effective-vector case is excluded separately by
linear growth versus bounded tanh combinations.

The projection residual `k` is bounded, odd, nonzero, and orthogonal to
all current features. Its mixed Hessian with the lower direction is
`2 rho_i ||k||_2²`, producing the displayed quadratic-form cross term
`4 s rho_i ||k||_2²`. The scalar sign and magnitude can therefore force
negative curvature. The base readout need only be in `L2`: all other
factors are bounded, so the necessary pairings are integrable. The
equilibrium derivative and Hilbert Hessian already exist by the
spectral small-remainder proof, which used no essential-bound condition
on the equilibrium.

Thus the Hilbert trapping graphs and countable category conclusion
extend to every Hilbert equilibrium with `0<L<1`. A Hilbert-convergent
orbit has a critical limit: if the limiting vector field were nonzero,
a continuous linear functional positive on it would remain uniformly
positive on the late-time velocities, contradicting convergence upon
integration. Loss is continuous in `H`. The initial boundedness
qualification on possible positive-loss endpoints is therefore removed.
This extension does not itself assume backward-image probability
regularity. The separate proof resolving it is reviewed in Section 9.

## 8. Supplemental nonempty open fitting basin

**PASS for the complete corrected frozen `basin_open_fitting.md`.**
Only the corrected packet with distinct mark-bound and coordinate
symbols was reviewed; its recorded earlier notation-only version was
not used.

The lower moment construction has the required uniform interior
margin. The inequality `E|b_1.e|>=q_1/B_{1,max}=2 kappa` follows from
`|b_1.e|²<=B_{1,max}|b_1.e|` for unit `e`. For target `A_i=kappa e_i`,
the convex objective is bounded below by
`kappa|xi|-E|g.u_i|-log 2`, while its value at zero is at most
`E|g.u_i|<=1`. This verifies existence, uniqueness, and the stated
`(2+log 2)/kappa` minimizer bound. The dual-input field realizes all
three moments simultaneously. The matrix sends them to distinct
coordinate vectors, and independence/centering of the upper coordinates
gives the diagonal readout Gram and exact fitted predictions.

All neighborhood constants have the claimed signs and bounds. The
factor `D_H=B_{1,max} B_{2,max}(1+m_*)` bounds the upper-feature
difference by splitting the matrix and lower-moment increments.
The weighted synthesis operator has norm at most one, since the weights
sum to one and the features are bounded by one. Its difference has norm
at most `D_H d`, so the Gram perturbation is at most `2D_H d`. Thus
`rho<=gamma/(4D_H)` gives the claimed `gamma/2` lower Gram bound.
The local prediction estimate uses the bounded fitted readout and has
the stated `K_f` factor.

The three physical velocity bounds sum to exactly the stated safe
constant `C`. The readout block alone dissipates at least
`2 gamma L`, giving `L'<=-2 gamma L` in the same neighborhood.
No comparison between the physical Hilbert norm and the stronger
state-speed norm is assumed.

The first-exit proof has the correct inequality direction. With
`q=sqrt(L)`, `-q'>=gamma q` implies
`integral_0^t C q <= (C/gamma)(q(0)-q(t))`, up to any first exit.
If `q` vanishes the state is stationary, so the integrated assertion
continues to hold. The triangle inequality therefore preserves the
strict initial bound on `distance+(C/gamma)q`. Taking a hypothetical
first-exit limit contradicts distance `rho`. This proves both trapping
and forward invariance of the open set, rather than merely assuming a
future Gram bound.

The explicit radius in (23) is strictly positive and lies inside that
open set by the local prediction estimate. The exponential loss bound
and the state-speed bound give finite `X_c` length and the stated
exponential endpoint estimate; completeness then supplies the fitted
endpoint. The strict initial margin also keeps the endpoint inside the
same open set. Finite-time backward images yield the enlarged open
forward-invariant fitting basin as claimed.

The constants can be independent of the geometry of an independent
triple: unit input norms and the globally bounded gate derivative
control the neighborhood estimates. The constructed center itself
depends on the dual vectors and may move arbitrarily far from canonical
initialization near input degeneracy. The report correctly retains
that distinction.

## 9. Final Hilbert time-map regularity and nullity extension

**PASS for the complete frozen `basin_hilbert_null_extension.md`, and
for its combination with the full-Hilbert landscape extension.** This
closes the previously separate backward-image probability obligation
without claiming a Fréchet `C1` flow on `H`.

The field's displayed directional derivative is correct in every block.
The lower multiplication term has a bounded coefficient and acts on a
fixed `L2` direction. Difference quotients converge in `L2` by dominated
convergence; all remaining operations use the already verified finite
moments and finite-vector smooth gates. On bounded Hilbert state balls,
the derivative operator norm has a finite uniform bound. Its strong
continuity follows from the given truncation argument: on the region
where the fixed variation is bounded, the multiplier difference is
controlled by the `L2` gate difference; on the remaining region, the
uniformly bounded gate coefficient multiplies a uniformly small `L2`
tail of the variation. Thus the derivative evaluation is jointly
continuous in the state and the direction, although operator-norm
continuity need not hold.

The flow differentiation proof addresses the main uniformity issue
correctly. Bounded derivative norms and fixed-direction continuity
justify line integration and bounded-ball Lipschitzness of the field.
The variational equation has a unique continuous solution with an
exponential operator bound. In the difference-quotient comparison,
the unknown difference `Delta_epsilon-V_h` is multiplied by the uniformly
bounded perturbed operator `A_epsilon`. The remaining operator
difference is tested only against the reference solution `V_h(s)`.
The set of pairs `(u(s),V_h(s))` on the finite time interval is compact.
Joint continuity therefore makes this latter error uniformly small in
time and in the line-integration parameter. Gronwall proves the actual
norm Gâteaux derivative of the time map. The same comparison proves
strong continuity in the initial state. This argument never requires
operator-norm convergence of `A_epsilon` to `A`.

Backward solution of the bounded strongly continuous variational
equation supplies a bounded inverse for the time-map derivative.
Nonlinear local reverse solutions along finite trajectory segments
supply the already needed local bi-Lipschitz homeomorphism and open
image. Neither assertion needs a Fréchet inverse-function theorem or
global negative-time existence.

The directional pullback lemma is valid. At a preimage base point,
choose the fixed input direction whose derivative image is the output
hypersurface's transverse direction. Strong continuity in that one
direction gives a positive lower scalar slope and an arbitrarily small
projected transverse error. The small product cylinder ensures that
the cross points used in the proof remain inside the controlled region.
The scalar graph residual is strictly increasing along each fiber,
with slope at least `m=a-Lb>0`, and is Lipschitz in the complementary
coordinate. Therefore its root is unique where it exists and is a
Lipschitz function on its projected domain. Scalar extension gives a
closed global hypersurface containing the local preimage. This is the
geometric property that mere bi-Lipschitzness would not have supplied.

The full-Hilbert landscape proof allows the set of equilibria here to
be all critical `H` states with `0<L<1`, rather than only bounded-field
equilibria. The spectral Hilbert graph proof used only the equilibrium
small-remainder estimate, finite-rank split, and negative curvature;
all hold for that enlarged set. The countable-cover argument and the
directional pullback lemma consequently give an `F_sigma` union of
closed Lipschitz hypersurfaces containing every initial state with an
`H` limit of loss in `(0,1)`. Meagreness, compact-witness shyness, and
nullity for the explicit dense-direction Gaussian series then follow
by the already checked conditioning argument.

The optional bounded-field randomization is also justified. Choose
Hilbert-dense unit directions in `X_infty` and coefficients
`2^{-n}/(1+||e_n||_{X_infty})`. The expected sum of their Gaussian
`X_infty` norms is finite, so the series converges there absolutely
almost surely. Its range lies in a separable closed subspace generated
by those directions, resolving the potential measurability issue.
The positive coefficients and Hilbert-dense span preserve full support
in `H`. No full support in the nonseparable `X_infty` norm is asserted.

The original packet had one cosmetic defect: the convergence arrow in
the display comparing `Delta_epsilon` and `V_h` in Section 2 was
malformed. The surrounding sentence and Gronwall argument specified
convergence to zero unambiguously. The lead restored the missing
backslash and appended a display-only repair record, yielding final
SHA-256 `cf0b0cf735f281e7d5c7b0dbd53ab9987933de4fe031d8d3644911a0aff2f473`.
I removed that appended record in memory and inverted the single
replacement; the reconstructed bytes had exactly the original reviewed
SHA-256 `acb04b58dba1c16859cbcd6587168ae8f29a66474227b8327807252d2b7a1ca8`.
Thus no other source change occurred, and the repaired version retains
the same PASS. No candidate source edit was made by the reviewer.

## 10. Ancillary dissipation and compactness statements

The complete authorized `basin_escape_route.md` was read. The ancillary
claims actually used by the integrated synthesis are independently
verified here, although they are not premises of the basin theorem.
Its unused conditional equation (5) invokes a further prior report
outside this review packet; that conditional extension is not certified
by the present review.

Finite total physical dissipation gives the claimed `o(sqrt(t))`
displacement by splitting the integrated velocity at a fixed time `A`,
using Cauchy--Schwarz on the remaining tail, taking `t` to infinity,
and then taking `A` to infinity. This controls every block in the
physical norm and does not imply boundedness.

The readout pairing gives exactly
`(||c||_2²)'=-4<r,f>_p=2(1-L-||f||_p²)`.
The completed-square estimate gives derivative at most one, while
subdiffusive displacement gives `||c(t)||_2²/t -> 0`. Dividing the
integrated identity by time proves the displayed time-average limits
for prediction norm and label correlation. A convergent finite
prediction vector then has the stated orthogonality to its residual.
No prediction convergence is inferred from those averages.

The stationary readout fiber is exact: adding an admissible bounded
odd function orthogonal to the current upper features and their nine
derivative features leaves all predictions and backward vectors
unchanged, hence leaves every gradient zero. The odd upper Hilbert
space is infinite dimensional, and finitely many linear constraints
leave an infinite-dimensional bounded-function subspace. This
substantiates the synthesis's neutral-direction explanation.

For the explicit noncompact family, the centered sine functions of
the independent third upper coordinate, after subtracting their
projection onto that coordinate, satisfy all the required constraints.
Their supremum bounds are uniform. The supplied step-function
approximation proves the Fourier integral limits, so their squared
norms tend to one and their pairwise squared distances tend to two.
Thus the fixed-loss stationary sequence is bounded and has no strongly
convergent subsequence. It is correctly presented as many stationary
trajectories, not a nonconvergent canonical orbit.

## 11. Fitting is open in the physical Hilbert topology as well

**PASS for the complete frozen `basin_hilbert_fitting.md`.** It uses
the same explicitly constructed fitted center and the same safe
constants as the continuous-field fitting theorem.

The lower moment difference is bounded by
`B_{1,max}||delta v||_2`, by Cauchy--Schwarz. Splitting the upper
argument gives
`B_{1,max}B_{2,max}(||delta M||_F+m_*||delta v||_2)`;
each component norm is at most the product Hilbert distance, so the
unchanged `D_H=B_{1,max}B_{2,max}(1+m_*)` is valid. The weighted Gram
estimate therefore remains unchanged. The prediction estimate uses
`||c-c_*||_2` and the same valid bound `C_*` for `||c_*||_2`.

Inside the known Hilbert ball, `||c||_2<=R_c` suffices for every
backward-vector bound. The three physical block speeds have the
displayed estimates, and their product Hilbert norm is no larger than
their sum, so the same `C` bounds total speed by `C sqrt(L)`. The
readout dissipation gives the same `-2 gamma L` loss bound.

Consequently the first-exit proof and explicit positive-radius ball
apply in `H` without any supremum bound on the current fields. They
give an open forward-invariant fitting region, finite Hilbert length,
and the stated exponential Hilbert endpoint convergence. Its
finite-time backward saturation is open and consists of fitting
starts. This proves an open fitting basin in the same topology as
the thinness result. The original continuous-field region separately
supplies its stronger norm conclusion; no stronger norm is inferred
for an arbitrary Hilbert initial state.

## 12. Final integrated synthesis check

The complete initial synthesis and its complete Hilbert-fitting revision
were checked against the reviewed components. The last wording repair
was then verified directly at final SHA-256
`45315a08179f83a9ec811562f95a704aea586514cc67e4cffb4539c246017a4d`.
It corrects a minor set-scope ambiguity: the positive-limit-loss set
`P_+` restricts the initial loss to be below one, whereas `B_+` does not.
The final text now explicitly states the valid relation
`B_+ intersect {L(theta_0)<1} subset P_+`, rather than implying an
unqualified set inclusion. This required no proof alteration.

The final synthesis correctly assembles all of the following:

* the exact unchanged population model and a globally defined physical
  Hilbert flow;
* local trapping graphs at every Hilbert equilibrium with loss in
  `(0,1)`, including unbounded or discontinuous limiting fields;
* a countable closed Lipschitz hypersurface **superset** of the
  point-convergent bad basin, with meagreness, an arbitrarily small
  compact shyness witness, and the stated explicit Gaussian nullity;
* actual nonstationary strong-stable trajectories converging to
  positive-loss equilibria from other initial fields;
* a nonempty forward-invariant fitting region open in the physical
  Hilbert norm, and a separately proved continuous-field region with
  stronger endpoint convergence;
* the remaining deterministic canonical-initialization, escape,
  nonprecompactness, and non-point-convergent limit-set gaps.

The thin outer hull is not identified with the exact bad basin. The
strong-stable graphs are correctly distinguished as actual bad-basin
subsets. The probability law perturbs population fields and is not
confused with Gaussian neuron marks or a random law on the fixed
canonical initial state. No conclusion about convergence of every
trajectory, fitting for every randomized start, or canonical initialized
fitting is asserted. The ancillary global estimates are independently
checked above but are not used to supply a missing compactness premise.

The final assembly has no remaining blocking proof or scope issue in
the reviewed statement. The harmless convergence-arrow display defect
was repaired and the exact scope of that repair verified in Section 9.
This is an internal verification only; no promotion or candidate source
edit was performed by the reviewer.
