# Isolated internal review of the finite-input basin extension

2026-09-18. **Verdict: PASS for the scoped mathematical claims in the frozen
packet and the final synthesis.** No mathematical repair is required. This
is internal checking, not promotion, and it does not establish the open
unrestricted finite-input basin-null theorem.

## 1. Isolation, coverage, and frozen identities

I followed the neutral review assignment and read only the assigned frozen
scientific inputs and required process instructions. I did not read the
study README, prior reviews, other studies, author conversations, or
unassigned files. I used solve-math-rigorously and investigate-conjectures,
including its adversarial-audit reference. No numerical experiment,
external theorem lookup, or scientific computation was used. Hash checking
was the only computation. This report is the only file I wrote.

The supervisor added the fitting, loss-gap, tail, initialization, synthesis,
and triple-geometry files to the isolated packet during this review. Each
was read completely, including provenance paragraphs and post-comparison
extensions. The initial missing scalar-positivity and unrestricted-triple
dependencies were reported, then closed by these explicit packet additions.

| Complete input | Lines read | SHA256 |
|---|---:|---|
| `docs/observable_p1.md` | 1–332 | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `dependent_basin_functional.md` | 1–789 | `af691c304d2204b08e76de0ca024241f6c0f2342209f3f8ca08926be2b6173e0` |
| `finite_basin_geometry.md` | 1–594 | `379f0b6e7c56ff208b2d7454a7fefbccc3b4eaa24ff9b5e8582a39ae64319b5a` |
| `finite_basin_tail.md` | 1–466 | `8be08e54db97ec23c6b253137f3046a362e82351ee2ff8502addfd176de1dbd2` |
| `finite_critical_loss_gap.md` | 1–159 | `361c7c0a10fd6e36ec9d7f847612ffed8396d66fe5e8cdedb193ee69bba50454` |
| `dependent_finite_fitting.md` | 1–229 | `54031d2000496e70ebda0e81dbfb26c08ad32d2b3f31e35066605ba257b3c518` |
| `initialization_positivity.md` | 1–131 | `73dae11c96755efd5e5362f879db9ca4197ddf0e3860434e939ecd529e0f55f5` |
| `dependent_hilbert_geometry.md` | 1–663 | `669037005ef6efe0151e43b82e5e7969c5fdf2ed5b75a3423c46a703ec70ce99` |
| `FINITE_BASIN_EXTENSION.md` | 1–215 | `3335dfcc23064a1deb02b46de6b347ec52e2b77b7968f63e3693492b16fca99f` |

All paths other than the first are in this study. The synthesis was first
read at SHA256 `ef7488e96b2c148fe86f738d04d399c4303a1d9e210a553f70ef94b9a282001b`.
The sole subsequent change replaced “Internal review pending; no promotion.”
with “Review status is recorded in the study README; no promotion.” I
verified that reversing the supervisor's exact replacement reproduces the
old hash. Its mathematical text is unchanged; I did not consult that README.

## 2. Exact admissibility and seven-input stationarity

The construction preserves the canonical model. The normalized lower mark
is an invertible linear transform of independent coordinate pairs
`(tanh G_j, tanh(sqrt(tau) Z_j + alpha tanh G_j))`. Each pair has a smooth
positive density on the open square, so the full lower law is absolutely
continuous with positive density on a neighborhood of zero. Thus for every
nonzero q, `B=q.b_1` is nonzero almost surely and `E|B|>0`. This uses the
actual joint carrier; it does not separate b_1 from g probabilistically.
The upper normalized coordinates are bounded, independent, symmetric, and
have positive densities on their open intervals.

Consequently `epsilon=sign(B)` is an admissible bounded odd field,
`w=a epsilon e_1` is bounded, and `w-g` is odd and in L2. It is not in
L-infinity: `|w-g|>=|g|-a`. Every constructed readout is a finite linear
combination of bounded odd upper functions. A rank-one value of M is a
valid point of the full matrix space; arbitrary matrix variations remain
available throughout the arguments.

Both square rotations, pi/4 and pi/8, have vanishing transverse first
moment, transverse second moment `I_2/2`, and vanishing cubed-cosine sum.
The triangle has the same first two moments and cubed-cosine sum 3/4.
The common positive first input coordinate excludes antipodes, and none of
the selected triangle and square angles coincide. With predictions -1/7,
the residual coefficients are -8/49 on the triangle and 6/49 on the square.
Their class totals are -24/49 and 24/49. Hence all three moment identities
`sum rho_i=0`, `sum rho_i u_i=0`, and `sum rho_i u_i u_i^T=0` hold exactly.

Every input has the same lower moment and upper activation. For common
backward vector `d_i=D e_1`, the three gradients reduce respectively to
`2sDB sum rho_i u_i`, `2H sum rho_i`, and
`2D e_1 a_0^T sum rho_i`; all vanish. The loss is exactly 48/49.
For D nonzero, every individual coefficient is `rho_i D q`, hence nonzero.
For D zero, the lower and matrix gradients vanish individually.

The two-function upper Gram construction is valid: an a.s. relation among
`H(x)=tanh(zx)` and `J(x)=x sech^2(zx)` extends by positive density,
continuity, and real analyticity to the real line. The limit at positive
infinity eliminates H, and then eliminates J. The resulting Gram is
positive definite. Orthogonal projection in the D=0 branch indeed gives
`E[cH]=-1/7` and `E[cJ]=0`; transverse backward components vanish by
independent coordinate symmetry.

## 3. Every Hilbert directional second variation, and the two regularities

I checked the full three-block variation, not just a lower-field slice.
For any `(h,k,N)` in the physical Hilbert space, writing `K=E[b_1 h^T]`,
the lower variations are

`a_i'=s K u_i`,
`a_i''=phi''(aC) E[b_1 epsilon (h.u_i)^2]`.

Bounded marks and bounded phi'' dominate the second differentiation by
an integrable multiple of `|h|^2`. Thus these identities hold for every
L2 direction. The effective-vector derivatives are affine in u_i at
first order, and their residual-weighted second derivative and quadratic
first-derivative matrix sum vanish by the three moment identities.
The upper second derivative consists of the readout/effective-vector
mixed term, the upper activation second derivative, and the effective
second derivative. Each residual-weighted term cancels. All pairings
with c or k are integrable by L2-to-L1 inclusion on the probability space.
The resulting directional quadratic form is exactly

`L''[h,k,N] = (2/7) sum_i (f_i')^2 >= 0`.

In the D-nonzero geometry branch, the concentrated perturbation calculation
is also correct. At `t=(log 2)/2`, `phi'''(t)=-32/27` and
`Q'''(0)=-(6/49) S^3 phi'''(t)` is nonzero. Opposite sufficiently small
fixed h give opposite signs of Q(h). On sign-paired sets of probability
m_n each, the squared perturbation norm is `2m_n h^2`, while the exact
loss increment is

`4D Q(h) integral_(E_n) B + O(m_n^2)`.

The factor four includes both the two paired sets and the derivative of
the unhalved loss. Effective-vector increments are uniformly O(m_n),
so the upper Taylor error is uniformly O(m_n^2). Choosing sets inside
`B>=delta>0` makes the leading term bounded below in absolute value by
a nonzero multiple of m_n. This proves both nearby descent/ascent and
failure of a second Frechet differential: the alleged Hessian on these
increments is O(m_n^2), whereas the Taylor remainder divided by their
squared norm does not tend to zero. Individual directional derivatives
are entirely consistent with this failure.

In the D-zero branch, the stronger regularity claim is justified. The
finite lower moments are locally C^(1,1) in L2; their derivative changes
in operator norm by at most a constant times the lower L2 displacement.
The finite coefficients T_i are therefore locally C^(1,1). The lower
gate operators G_i are bounded and L2-Lipschitz into operators from the
finite coefficient space to lower L2. At a center with every T_i=0,
the product remainder after subtracting the linear derivative has
Lipschitz constant O(r) on an H-ball of radius r. The upper and matrix
blocks have the same bound through their C^(1,1) dependence on moments.
None of these estimates requires bounded w-g.

Thus the actual gradient derivative exists at this equilibrium. Since
`Df_i[h,k,N]=E[kH]`, its symmetric Hessian is exactly

`nabla^2 L(h,k,N)=(0, 2 E[kH] H, 0)`.

H is nonzero, so the rank is one and the only nonzero eigenvalue is
`2||H||_2^2>0`. The flow has the negative of this eigenvalue and no
positive eigenvalue. This is a genuine regular obstruction to a universal
strict-saddle premise, not merely the absence of an available Hessian.

## 4. Independent cubic calculations and regular cubic variant

The original tail route uses q supported in coordinate pair one and
`psi=1_(|G_2|<=b)-1/4`, with the event having probability 1/4. Coordinate-
pair independence gives `E[b_1 epsilon psi]=0`, including both retained
entries of each pair. It does not require independence within a pair.
Moreover `E psi^3=3/32`, so
`E[(q.b_1)(epsilon psi)^3]=3 kappa/32`. All first effective variations
vanish. The third loss derivative is exactly its displayed

`2 d_1 phi'''(aC) (3 kappa/32) (-6 S^3/49)`.

Here d_1 is negative and `phi'''(1/4)<0`, making the product negative.
The first and second derivatives vanish. This proves bounded cubic
descent and ascent for that branch.

For the post-comparison regular branch, the chain-rule formula for K_3
is correct. Its leading analytic positive-infinity asymptotic is
`16 kappa^3 phi'(s_0)^3 B^3 exp(-2zB)`, while J has only the first power
of B and H has nonzero constant limit. The leading coefficient is
strictly positive. Therefore H,J,K_3 are linearly independent and their
actual bounded-support Gram is positive definite. The prescribed moments
`E[cH]=-1/7`, `E[cJ]=0`, and `E[cK_3]=1` are simultaneously realizable.

With lower perturbation `epsilon e_2`, prediction has the exact form
`F(s_0+lambda S cos alpha_i)`. The moment constraints give F'=0 and
F'''=1 at s_0. The loss therefore has `L'=L''=0` and
`L'''=-12S^3/49<0`. This carries over from the pi/8 square to the pi/4
square because both have zero cubed-cosine sum. The regular cubic
variant retains the actual rank-one Hessian established above.

## 5. Strong-stable trajectories in the affine bounded-field chart

The affine chart is legitimate despite the unbounded displacement from g:
write a state as `theta_*+x`, with x in the bounded odd product space X.
Then its actual lower field is `w_*+x_w`. The exact field maps the chart
into X and is smooth there; scalar derivatives are bounded, moments are
continuous, and the remaining operations are finite products or bounded
pairings. No assertion that theta_* itself lies in the linear space X
of displacement coordinates is needed.

Let `beta=2||H||_2^2`. The stable projection onto `(0,H,0)` is bounded
in X, as is its complementary kernel projection. In the sum norm the
stable semigroup is `exp(-beta t)` and the center semigroup is the
identity. The nonlinear remainder has arbitrarily small local Lipschitz
constant. The radial cutoff costs at most a factor two, which can be
absorbed into the chosen epsilon.

In the path norm weighted by `exp(beta t/2)`, each integral in the
displayed fixed-point equations has Lipschitz bound `2 epsilon/beta`.
Thus `4 epsilon/beta<1/2` is sufficient. The fixed path is bounded by
`||eta||/(1-q)` and remains inside the original chart ball for eta small.
The center integral converges absolutely; differentiating it and the
stable integral gives the original ODE. The stable projection at time
zero is exactly eta, so nonzero eta gives a nonstationary trajectory
converging exponentially to theta_*.

Local uniqueness in both time directions excludes meeting an equilibrium
at a finite time. The physical energy derivative is therefore strictly
negative at every finite time. Continuity and small eta give
`48/49<L(t)<1` with limit 48/49. The same proof works for either bounded
D-zero readout, including the three-moment cubic variant. The graph is
one-dimensional and Lipschitz by parameter dependence of the contraction.
It is an existence result for special starts; it provides no positive
probability for the entire basin and no assertion about canonical starts.

## 6. Basin dependencies and restricted extensions

I checked the complete functional dependency used for the new restricted
basin statements. Local Hilbert Lipschitzness, the C1 loss and energy
identity follow from bounded marks and moments. The stated polynomial
bounds prevent finite-time blowup. Strong directional continuity of the
field derivative follows from the displayed truncation argument, and
the finite-time variational equation has an invertible strongly
continuous directional derivative. These properties are sufficient for
the stated hypersurface pullback argument; operator-norm continuity of
the field derivative is not being assumed.

The finite-family negative-curvature argument is complete in functional
Section 7: one nonzero residual group field gives a bounded mixed
variation, and analytic line restriction plus successive exponential
rate elimination separates the derivative feature from the feature span.
Choosing the readout perturbation orthogonal to that span gives the
strictly signed mixed term with factor four. The local graph contraction,
countable neighborhood cover, integer-time pullbacks, and scalar Lipschitz
extensions give the required countable hypersurface hull. The explicit
Gaussian-series proof conditions on one transverse scalar coefficient
and applies equally to every fixed translation and positive scale. The
uniform-coefficient compact series supplies the shyness witness.

The direct-sum extension is sound: projecting lower stationarity onto
each input-span block invokes the already proved one-relation
cancellation lemma on the original carrier. Orthogonality of blocks is
unnecessary. The finite-family strict-saddle argument then applies.

The conditional-mark extension is also sound. Positive definiteness of
`Q(s)=E[b_1 b_1^T|w=s]` turns the conditional squared stationarity identity
into `B(s)=0` almost everywhere. Continuity and full support extend it
to every s. Generic-line gate-rate separation forces every T_i to vanish.
Full support also makes every nonzero residual-group field nonzero with
positive probability, closing the negative-direction argument. The
canonical conditional matrix at w=g has rank at most d+1: its conditional
covariance has only d random reverse-coordinate directions, and its mean
contributes at most one additional rank. Thus the extra hypothesis does
not hold there when d>1, exactly as stated.

For both restricted theorems, the endpoint range is `0<L<1`, or more
generally positive loss with the explicit condition M nonzero. The
sub-loss-one condition supplies M nonzero automatically. These results
do not cover arbitrary H endpoints simply by dropping their endpoint
conditions, and they do not claim avoidance by a fixed canonical point.

The later-added triple geometry closes the synthesis's background
comparison. I checked the gate-ratio lemma, including the derivative of
J, the positive determinant of its convexity matrix, and the ellipse
intersection argument. Its exceptional common-feature collision is
impossible for three distinct projective directions. The subsequent
sign-rigidity classification shows that failure of cancellation below
loss one would require an unequal-weight conflicting signed pair and
a zero singleton. Equal triple weights exclude it. Consequently those
triple endpoints do have both cancellation and a negative bounded
direction; the supplied functional estimates then yield an actual
unstable linear direction and the downstream graph argument. No missing
external theorem or unprovided scientific source remains necessary for
this use of the packet.

## 7. Initialized fitting and the finite stationary-loss gap

The added positivity source correctly identifies the conditional initialized
coefficient Psi, including the reverse response and ridge subtraction.
Gaussian integration by parts and Cauchy--Schwarz give
`b^2>=tau gamma^2+eta`. I checked the subsequent upper bound on B_*,
the sign reversal when multiplying the negative quantity m-alpha, and
the elementary bounds on nu, alpha, gamma. The rational endpoint value
is exactly `J_*=2552/61425>0`. Thus the claimed strict sign of Psi is
established without a quadrature premise.

The fitting file's derivative formula for T is correct after Gaussian
integration by parts. For positive Gaussian mean, pairing opposite
arguments makes the expectation of the odd function phi phi' positive.
This proves strict increase on [0,1), with oddness and endpoint continuity
giving strict increase on the whole interval. The coordinatewise effective
input map is therefore injective modulo sign. Finite tanh-feature
independence yields the positive Gram and the explicit fitted readout.

I also checked the open-basin constants. The hidden-feature difference
is at most D_H times physical state distance; synthesis-operator norms
are at most one, so the weighted Gram changes by at most twice that
quantity. The chosen radius gives a lower bound gamma/2. The three speed
bounds sum to C sqrt(L), while readout dissipation alone gives
`L'<=-2 gamma L`. Integration preserves the specified strict sublevel,
gives finite trajectory length, and yields the stated exponential
endpoint bound. This proves a nonempty open fitting basin, with no
claim that canonical initialization lies in it.

The stationary-loss gap is independent of lower endpoint regularity.
Finite tanh-feature independence makes readout stationarity determine
each nonzero signed group's prediction as its oriented label mean.
Its loss is `4 W_+ W_-/(W_++W_-)`; a zero group contributes its mass.
A mixed group's two masses are at least p_min, so its contribution is
at least 2p_min. A nonempty zero group contributes at least p_min.
All contributions are nonnegative. Therefore every equilibrium has
loss zero or at least p_min, and the finite signed-partition list
contains all stationary losses. It is not asserted to be fully attained.

The point-convergence implication is rigorous: if the continuous field
were nonzero at a state limit, pairing velocity with its fixed limiting
field would eventually have a strictly positive lower bound and prevent
convergence. Thus the limit is an equilibrium. Loss continuity and
dissipation imply zero limiting loss when initial loss is below p_min.
This does not require, or prove, entrance into that sublevel or state
convergence. Equal weights give the stated threshold 1/m.

## 8. Integrated verdict and limits

The final synthesis accurately joins the claims and preserves their
different scopes. In particular:

* The seven-input examples disprove universal individual cancellation
  and universal negative second-directional curvature for unrestricted
  endpoints; the regular variant disproves a universal unstable-
  linearization premise even when individual cancellation holds.
* The cubic and concentrated descent constructions establish failure
  of local minimality for their respective chosen readouts. Descent
  for the two-moment projected readout is not assumed from the D-nonzero
  argument; the independent third moment supplies the regular cubic claim.
* The strong-stable trajectories establish positive limiting loss from
  special sub-loss-one starts. They do not establish a non-null basin.
* The new restricted basin results retain their explicit endpoint
  hypotheses and the specified population-field randomization.
* The finite loss gap and open fitting region are valid positive results,
  with neither converted into a global convergence or canonical-fitting
  assertion.

No fatal, major, conditional mathematical defect, or required repair was
found in the reviewed scope. The decisive open bridge is still nonlinear
control of the degenerate central directions sufficient to settle the
unrestricted finite-input bad-point-basin probability. The packet neither
proves nor disproves that desired basin theorem. This PASS does not change
the repository's internal-versus-established distinction or authorize
promotion.
