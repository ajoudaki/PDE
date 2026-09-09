# Isolated adversarial review of the special-angle modular bridge

Date: 2026-09-06.

## Verdict and exact scope

**Core canonical bridge: PASS, relative to the actual premises in A and P.**
No unresolved required mathematical gap was identified in the fixed-program
adaptation, common-space operator construction, global special-angle flow,
full-sequence width limit, or the stated raw-GD, path, kernel, probe, and
quadratic velocity/energy conclusions.

**Separate response/remainder strengthening: PASS.** The independent-root
argument establishes the expected formal source coefficients, including
singular and zero-variance slots. Its estimates imply the mesh-uniform row
bounds and bounded Gaussian remainders. The optional integral memory
representation is valid with the stated completed-Lebesgue measurability
and without uniqueness of the individual kernels.

These are separate verdicts. The core bridge does not require the response
row bounds or the bounded-remainder representation. Its uniform
integrability is independently obtained in Section 8. A failure of the
additional response argument would therefore require withdrawing Sections
5--6 and their advertised consequences, but would not by itself defeat
Sections 4 and 7--10. In this snapshot, I find no such failure.

This is a modular result for L=2, both activations arctan, rho=0 or rho=-1,
loss SUM, labels (1,-1), the specified initialization and raw physical
normalization, and each fixed finite time horizon. It is not a final
self-contained global-all-angle theorem. In particular, this verdict does
not establish intermediate angles, distributional nonaffinity, nonlazy
learning at every time, arbitrary width-dependent probes, or a long-time
limit.

All mathematical input was confined to the following three files, each
read completely. No referenced project files, history, other reviews,
external mathematical sources, experiments, or agents were used. The
candidate and its dependencies were not edited.

| Name | File | Lines | Verified whole-file SHA-256 |
| --- | --- | ---: | --- |
| C, candidate | `/tmp/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLE_CANONICAL_BRIDGE.md` | 1288 | `de061c34befd83240e938c2511adc68168d6c2cbaa45b2c5b4b48e86a7a741c5` |
| A, deterministic dependency | `/tmp/l2-two-sample-proof-0ywjpp/ORTHOGONAL_ANTIPARALLEL_FLOW_ANCHOR.md` | 1015 | `c3f147633689050f8d9a4749e23861b02640dd7ba0e201b0f05a609b9c76cf39` |
| P, fixed-program dependency | `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | 862 | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |

The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`
was read completely and used to require explicit hypotheses, limit-order
checks, and complete treatment of nontrivial transitions. It supplied no
mathematical premise. Its verified SHA-256 is
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

The embedded proof-content hashes were also checked using the files'
specified prefix convention. C gives
`20f7c2f3c36d810aa9416974a4790eef25d2929e94fbf0b6e0c72bedebc1ddd5`;
A gives
`3e1da9dc804fc922ece75a1cf66f4cb3290971d99478547de59fa915a9a84af9`.
Both match their declarations. Whole-file hashes, not these prefix hashes,
identify the reviewed snapshots.

## Coverage and dependency boundary

Here “required” means required for the core bridge; the stronger claims
are separately required if the entire candidate, including Sections 5--6,
is imported.

| Obligation | Status and role | Principal location |
| --- | --- | --- |
| Cubic iid root and all finite moments | Pass; required | C 3.1, lines 223--321; P 3 |
| Actual empirical residual feedback | Pass; required | C 2, 3.2; P 7 mechanism |
| Both Gaussian conditioning orientations | Pass; required | C 3.2, starting line 323; P 4--5 |
| Singular Grams and retained formal slots | Pass; required | C 3.2; P 6 |
| Countable common space and dense queried domains | Pass; required | C 4, lines 440--528 |
| Bounded canonical initial action and true adjoint | Pass; required | C (21)--(22) |
| Independent-root source extraction and coefficient feedback | Pass; separate strengthening | C 5, lines 530--723 |
| Mesh-uniform response rows and bounded Gaussian remainders | Pass; separate strengthening | C (27)--(30) |
| Measurable integral kernels and every-time rows | Pass; optional representation | C 6.1, lines 777--856 |
| Same-operator global GF, Euler convergence, restart | Pass; required | C 7; A 5--7 |
| Uniform integrability independent of response rows | Pass; required | C 8, especially (38)--(41) |
| Full-sequence width/time passage and random readout | Pass; required | C 9, starting line 1078 |
| Same-neuron two-sample paths and finite Wasserstein orders | Pass; required | C 8--10 |
| Products, kernels, forward/transpose probes | Pass within stated admissibility; required | C (35)--(37), 9 |
| Original velocities, squared norms, and energies | Pass at W2/quadratic level; required | C 9.1, lines 1134--1196 |
| Exact raw GD and recomputed raw interpolation | Pass; required | C 10; A 8--9 |
| Antiparallel factor four and raw metrics | Pass; required | C 2, (35), (46); A 3--4, 6 |

A actually supplies the deterministic bounded-operator result needed
here. It supplies a construction on bounded-readout sets, the loss
identity, continuation and restart, a width-independent transformed Euler
estimate, and a closed raw-GD bootstrap. Its displayed primal assumptions
(8.3) are not an unresolved hypothesis: A 8.2 proves them on the stated
initialization event. Its same-width estimates do not themselves identify
a population operator or width limit; C supplies those missing steps.

P cannot be applied verbatim as a theorem about this dynamics. Its own
program is a capped, three-layer softplus program with fixed weights and
fixed query count. C correctly reuses its proved conditioning, projection,
moment, singular-transfer, and feedback mechanisms, and separately checks
the cubic root, uncapped bounded readout, arctan maps, and residual weights.
No mesh-uniform theorem or continuum assertion is imported from P. Files
named inside A or P were not treated as additional premises.

## 1. Finite program, cubic root, and moment extension

C (2)--(3) is the transformed Euler program for the two geometries in A.
The finite operator acts without an extra normalization, the rank-one
update is `V H^T/n`, and the adjoint is the same matrix's transpose. The
updates are simultaneous after the stated forward and reverse calls.

The essential cancellation is exact:

    F'(z)D(z) = (1+z^2)/(1+z^2) = 1,
    g'(u) = D(g(u)),     H'(u) = D(g(u))^2.

The cubic root is legitimate as a stored iid tuple `(G,F(G))`. Its second
moment is `1 + (2/3)·3 + 15/9 = 14/3`, and its higher moments are finite.
The conditioning proof needs derivatives in matrix parameters and in
later source slots; it does not need a globally bounded derivative of
`G -> F(G)`.

The readout bound (9) is dimension independent. Indeed, bounded J gives
`|f_a| <= B ||w||_infinity`, whence summing the two readout increments
gives

    ||w_next||_infinity
      <= (1+4B^2 eta)||w||_infinity + 4B eta.

Thus `w D(Z)` is a globally Lipschitz coordinate instruction on the entire
range this fixed graph can attain. Replacing its w argument by a smooth
bounded map equal to the identity on a larger interval is an exact graph
representation. It is not an unproved removal of a backward-field cap.

The non-Gaussian-root moment proof in C (10)--(14) closes a real issue
that P's Gaussian-root proof alone would leave open. Conditional on the
stored roots, induction yields polynomial bounds for normalized vector
norms and for ordinary Euclidean matrix-parameter differentials. For a
normalized scalar contraction its differential has the extra `n^-1/2`;
this cancels the `sqrt(n)` in a subsequent scalar-times-vector node.
All polynomials depend on the fixed graph, not on n.

The conditional means require an additional argument. If
`m_i(R)=E_matrix[x_i|R]`, independent population permutations and the
root-Lipschitz estimate give

    |m_i(R)-m_j(R)|
      <= P(K_R) sum_l |R_li-R_lj|.

Averaging over j, bounding the average absolute mean by its normalized
L2 norm, and bounding average root magnitudes by their RMS norms yields
(13). Jensen bounds every moment of a normalized root norm; Hölder then
controls its product with a fixed coordinate root. The dimension-free
Gaussian rotation inequality (11), conditional on R, controls fluctuations
around these means. This proves all finite coordinate moments, rather
than merely an empirical second-moment estimate. Populations without
local roots are covered by equality of their conditional means.

The operator-net estimate gives uniformly bounded matrix-norm moments
and an event `||A0,n||<=8` whose probability tends to one. The argument
uses no maximum of the first Gaussian coordinates and no Lp operator
bound. Independent auxiliary all-moment roots are covered by the same
proof. These checks also cover the actual empirical-feedback graph.

## 2. Conditioning, covariance support, and scalar feedback

The conditional mean in C (15) satisfies both constraints: the first
term gives WV=Y, and the second corrects the transpose constraint on
the orthogonal complement of the old forward inputs, using
`U^T Y=Q^T V`. The residual has both required null projections. At an
adaptive query, conditioning on the previous transcript fixes its input;
revealing the answer adds a linear constraint on the remaining Gaussian
matrix. This proves the adaptive use of the formula, including its
transpose version.

The discarded finite-rank projection is small in every finite empirical
moment, not just in L2. For p>=2 its conditional pth moment is bounded by
`m_p sigma^p J/n`, since a projection has diagonal in [0,1] with sum J.
The input moment bound controls sigma. For p<2, L2 suffices. Conditional
variance estimates for the remaining independent Gaussian coordinates,
followed by bounded-ball approximation and higher-moment tails, justify
continuous polynomial-growth tests.

The integration-by-parts identity

    E[zeta h] = Gamma E[gradient_zeta h]

is valid with singular Gamma by writing `zeta=L e`. In the nonsingular
conditioning calculation it cancels the derivatives of the old forward
projection and gives C (17). The same calculation applied to the
transpose gives the reverse rule. The covariance is the uncentered
input second moment. It is not a centered covariance of inputs and is
not obtained by subtracting the response variance. The innovation has
residual variance, while the complete source has full input variance.

The two orientation groups remain independent of each other and of the
local roots in the scalar construction. This is a statement about the
separate population laws. It does not assert an empirical coordinate
pairing across neuron populations or an independent transpose matrix.

For singular queries, the perturbation in C 3.2 is to each initial-matrix
query input, with a fresh independent root. It gives a positive Schur
complement at least epsilon squared while retaining the actual matrix
and leaving learned rank factors unperturbed. The graph comparison (19)
and all-order moments imply small errors in every finite empirical Lp.

The scalar limit is passed through the source recursion, which has no
inverse Gram. At each fixed finite induction stage the coefficients lie
in a compact set, source derivatives are bounded there, and the stored
root/source expression has a common integrable polynomial envelope.
Continuity of the positive covariance square root, including at rank
drops, and dominated convergence then give the next covariance and
derivative expectation. No differentiability of that square root is
needed. The regularized and zero-noise programs are compared before
taking any growing-query or time limit.

Zero slots must remain formal slots. For a null vector v of the reverse
input Gram, `sum_s v_s V_s=0` in L2, so ambiguity by v in a derivative
vector does not alter the contracted response. The explicit expression
still fixes the individual coefficients. In particular, the initial
zero reverse fields do not justify deleting their slots.

Finally, the residual coefficients are selected causally, after the
relevant fields and contractions exist. The contraction difference bound
and finite graph induction transfer the deterministic-coefficient law to
the empirical-feedback program. This is not an implicit fixed point for
the residuals. When computing responses, differentiating the selected
macroscopic coefficients would give a different rule; C correctly freezes
them, retains the explicit earlier readout derivative, and obtains
`beta_(ka,kb)=1_(a=b) E[w_k D'(Z_ka)]` without a current learned-rank term.

## 3. Canonical common space and actual adjoint

C 4 constructs the operator from joint finite-program laws, rather than
substituting an arbitrary operator with norm at most eight. Its countable
closure has finitely many parents per instruction, includes both
orientations and the desired Euler meshes, and permits the source nodes
themselves by subtracting their selected responses. Every finite set of
nodes is therefore covered by the fixed-program result.

The successive Gaussian construction is consistent because every new
same-orientation covariance is an input Gram. Its innovations can be
realized with countably many independent Gaussians; the supplied binary
digit construction suffices for this countable probability space. Zero
variance causes no construction problem. Consistency of old finite
marginals also follows from their being limits of the identical finite
empirical marginals when unused queries are inserted.

The operator proof needs both (21) and (22). Finite norm inequalities
and the exact finite transpose identity pass to deterministic limiting
Gram entries on the event of probability tending to one. Consequently,
an L2-zero input relation has an L2-zero answer relation. This makes the
linear actions well defined on queried spans, not merely bounded as
lists of unrelated input/output pairs.

Density is adequately justified. Finite-cylinder events generate the
countable field sigma algebra; approximation in measure extends from the
cylinder algebra to that sigma algebra. Smooth bounded threshold
approximations, with one-sided limits where necessary, cover atoms as
well as continuous marginals. Rational parameters give a countable dense
collection. Truncation and simple-function approximation then give L2
density. Since every such node is eventually queried, both input spans
are dense.

The two bounded extensions exist on the completions. Their pairing
identity extends by continuity and says precisely `B0=A0*`. Uniqueness
is uniqueness on the specified generated spaces, up to the
law-preserving identifications of the same generating family. It is not
operator-norm convergence of finite matrices, a continuum iid kernel,
or an arbitrary Lp extension. Adding genuinely new independent probe
roots can enlarge a realization; the old observable laws remain the
same. No uniqueness of an extension to an unrelated larger sigma algebra
is needed for the stated bridge.

## 4. Independent-root extraction: detailed adversarial check

This is the most delicate additional argument, C 5.1--5.2. A bounded
operator and L2 flow stability alone do not bound an arbitrary formal
off-support source derivative. C explicitly recognizes that obstruction
and supplies a further finite-program construction. The construction
does resolve it.

First, (23a) is the complete frozen-coefficient derivative recursion.
The transformed bottom update contributes a direct source impulse plus
the response through the H fields. It has no attained Q multiplying a
curvature derivative of a first-layer factor. The top recursion retains
both the past readout derivative and the term `w D'(Z) partial Z`.
Current reverse coefficients and all learned rank terms remain present.
No unproved convolution or resolvent majorant is used.

For clarity, the extraction has four logically distinct steps.

1. **An actual finite-width forcing.** A fresh independent iid normal
   array e is added to one complete query answer after that answer and
   before its descendants. This is a permitted extra linear instruction.
   It is not a perturbation of a matrix entry or a claim that the
   designated source direction lies in the old covariance support.

2. **A width- and mesh-independent state bound.** For reverse forcing,
   the immediate state change is in U and has size at most
   `C_T eta_s |epsilon| ||e||_n`. For forward forcing, J, V, f, the
   residual weights and the reverse answers change at the forced step;
   the subsequent U, A and w state changes all carry eta_s. The operator
   bound controls the changed reverse answer. Iterating the actual
   one-step factor `1+L_T eta_k` proves (24)--(25), with all scalar and
   rank feedback included. This estimate does not depend on the number
   of mesh points. Bounded H and J give the required operator and readout
   bounds even for the off-invariant auxiliary transformed program at
   rho=-1. That auxiliary program need not itself be raw GF.

3. **Identification before integration by parts.** Fix a mesh and a
   nonzero epsilon. Apply Section 3 to the two runs and e together. In
   the resulting scalar law, local e is independent of the Gaussian
   source groups. Every selected coefficient and covariance is a
   deterministic number for this fixed epsilon. In the affected
   population the explicit use of e is through the replacement
   `source_slot + epsilon e` at the chosen answer. Thus, holding the
   other formal sources and selected numbers fixed, induction through
   the descendants gives

       partial_e X^epsilon
          = epsilon partial_slot X^epsilon,
       E[e X^epsilon]
          = epsilon E[partial_slot X^epsilon].

   Future sources can have epsilon-dependent joint covariance, and
   response coefficients can depend on epsilon. Neither fact makes
   them functions of the realized local coordinate e. Thus neither
   contributes an additional term to this one-dimensional integration
   by parts. Performing this operation directly on empirical feedback
   at finite n would require extra terms; C does not do that.

4. **Recovery of the stipulated zero-noise derivative.** At epsilon=0
   the unused root is independent of the output, so `E[eX^0]=0`.
   The finite-width Cauchy--Schwarz inequality and the state estimates,
   passed through the fixed-program limit, yield

       |E[e(X^epsilon-X^0)]| <= C_T eta_s |epsilon|.

   Dividing by epsilon bounds the expected formal derivative for the
   perturbed scalar expression. At this fixed mesh, continuity of its
   selected coefficients, covariances, and bounded source derivatives
   identifies the epsilon-to-zero limit with exactly (5)'s retained-slot
   convention. The fixed-mesh continuity need not be uniform over
   meshes: its limiting bound already has a mesh-independent constant.

In step 3, later source variables are held fixed as formal arguments,
even if correlated with the designated slot. The independent e always
has a nondegenerate one-dimensional Gaussian density. This is why the
calculation remains valid for an initial zero slot, duplicated slots,
and the antiparallel singular covariance. It neither inverts the old
covariance nor infers an off-support derivative from the unperturbed law
alone. Step 4 specifies that derivative by the actual perturbed graph
and the fixed expression convention.

For a past slot the resulting bounds are `|alpha|,|beta|<=C_T eta_s`.
For a current slot, V uses the old w and the direct current Z, giving
the diagonal bound M_T and zero formal off-diagonal coefficient. Bounded
H, V, and `|gamma_sb|<=C_T eta_s` then supply (28), including the
learned memories. These are bounds on expected response coefficients;
they do not purport to bound every pointwise formal derivative path.

I find no missing coefficient-feedback term or covariance-support
assumption in this extraction. A conclusion that (27) fails solely
because the unperturbed source covariance is singular would overlook
the independent-root identification in steps 3--4.

## 5. Remainders and optional integral memories

The row bounds directly imply the three decompositions in (29). The
forward remainder is bounded by the row sum times `||V||_infinity`;
the reverse remainder is bounded by its row sum times B, including the
current diagonal term. Substitution in the accumulated U update leaves
a Gaussian linear combination of the reverse sources plus a bounded
remainder. Its variance is bounded by the square of the total weighted
sum of their standard deviations. Its coefficients are deterministic,
so it is Gaussian and independent of the original first-neuron root.

The remainder need not be independent of its Gaussian term. The
assertion is not conditional Gaussianity of the evolved field. Since
g is 1-Lipschitz, (30) follows, giving Gaussian tail upper bounds for
Z, Q and g(U), and all finite moments with a cubic-Gaussian tail bound
for U. None of these upper bounds proves nonaffinity or nonlazy learning.

On the common space, source covariance gives
`||xi_h-xi_h'||_2=||h-h'||_2`, and similarly for the reverse inputs.
Thus these Gaussian assignments extend isometrically to the needed
closed spans. Same-space strong Euler convergence carries their sources
to the time limit. Strong L2 limits of uniformly essentially bounded
remainders preserve that bound by a summable-error almost-everywhere
subsequence. Characteristic functions preserve Gaussianity and root
independence of the Gaussian linear combinations. The U source integral
is an L2 Riemann limit with deterministic continuous coefficients.

For C 6.1, the bounded densities (past coefficients divided by their
step sizes) admit the supplied diagonal weak-L2 extraction. The bound
survives testing against indicators, as does the triangular support.
Pairing the kernels with `1_(s<t)<V_b(s),v(t)>`, or its H counterpart,
is legitimate: on each finite square this is L2 by the uniform L2
field bound. Strong field convergence controls the replacement error.
This gives the memory identity almost everywhere in t.

The every-time extension is also valid under the stated measurability
convention. A row limit along nonexceptional times is weakly compact by
the same elementary basis argument; L2 continuity of fields and sources
passes the equality to the exceptional time. Each chosen row is
measurable and bounded. All replacements lie over a Lebesgue-null set
of t, whose product with a finite s interval has measure zero, so they
preserve measurability in the completed product space. This does not
promise joint Borel measurability for every arbitrary row selection.

The instantaneous reverse term `j_a(t)H_a(t)` is correctly separate.
Individual density representatives, especially at singular covariance,
need not be unique or converge along the full sequence. The fields,
sources, and contracted memories are already canonical; the subsequence
here only represents them. This representation is optional for the
core theorem.

## 6. Global flow, same-operator Euler limit, and uniqueness

The constructed operator has norm at most eight, the initial cubic
coordinates are in L2, and the readout is bounded. These are precisely
A's hypotheses. C does not ask A to construct the operator or to select
its reuse law. The learned operator increment is Hilbert--Schmidt,
although A0 need not be.

A's local construction resolves the fact that an L-infinity ball is not
open in L2 by truncating the readout in the vector field and then proving
the truncation inactive. Its chain rule along L2 paths is justified by
a fixed-direction dominated-convergence argument; no false assertion of
Frechet differentiability of a nonlinear L2 Nemytskii map is used. The
rank updates and actual adjoint justify the loss identity. At zero
readout, loss starts at two, total action is at most 4T, and the bounds
in C (33) follow from A (6.1).

Every included Euler program obeys its equations with this very A0 and
its actual adjoint. Applying A's deterministic estimate on the common
space therefore gives (34) and the transformed velocity estimate.
Nonuniform steps replace the local-error sum by `sum eta_k^2<=h(T+h)`.
No rowwise response estimate occurs in this comparison. Additional
fixed meshes can be included jointly before applying the same argument.

Restart is at the full reached state, with the existing operator,
readout and correlations. A also proves the necessary extension of
uniqueness to ordinary-L2 raw integral solutions: pointwise absolute
continuity and the scalar chain rule imply

    F(z(t)) = F(z(0)) + integral c(s)Q(s) ds

in L2. Thus membership in the cubic-coordinate class follows from the
raw equation rather than being imposed as an extra uniqueness
restriction. The antiparallel relation is preserved. No unproved
continuity, restart, or uniqueness premise is needed here.

## 7. Uniform integrability, products, and paths

An L2 state estimate alone would not justify convergence of `D(z)Q`.
C (36) supplies the correct bounded-multiplier/tail split. Section 8's
independent moment argument supplies its uniform square-tail hypothesis.

For that moment argument only, the initial matrix is radially clipped
to norm eight. The radial map is 2-Lipschitz in operator norm; hence its
change under an unscaled matrix perturbation E is at most
`2||E||_F/sqrt(n)`. A's stability bounds the normalized state difference
by a constant times this change and the normalized stored-root change.
Multiplication by sqrt(n) to control any single coordinate therefore
gives a dimension-independent Lipschitz constant for the coordinate
path supremum. The constants are independent of the size of U because
H and J are bounded and the transformed first drift has no unbounded
multiplier.

The RMS bound for the vector of path suprema is not inferred from a
bound on the supremum of RMS norms. It is separately proved by (40).
For U, z, H, Z, J, w and V the derivative formulas give bounded L2
variation; for Q use

    dot Q = dot A* V + A* dot V,
    dot V = dot w D(Z) + w D'(Z) dot Z.

All multiplying factors used here are bounded and all operator actions
are in L2. Fubini supplies pointwise absolutely continuous versions.
The initial U contribution is handled by the stored root norm.

The conditional Gaussian moment inequality and the permutation/mean
argument then apply to the supremum functionals themselves. Smooth
approximation suffices for their nondifferentiability. Euler uses the
sum of successive L2 variations and the same stability constants.
Clipping the initial finite readout to [-1,1] for this estimate gives
uniformly bounded-root data. Both modifications disappear on events
whose probability tends to one.

Thus (41) supplies empirical tail control in probability for the actual
arrays. It need not prove uniformly bounded expectations for their
unmodified values on the vanishing exceptional events, and the theorem
does not require that stronger assertion. In particular, Q has uniformly
integrable squared path norms in probability. Since `|d|<=|Q|`, the same
tail control covers d without a state-Lipschitz claim for d.

At a fixed mesh, all polynomial-growth observables are identified by
Section 3. Unbounded operator inputs such as `D(z)^2 dot U` are first
smoothly truncated in Q. Their input L2 errors vanish by higher moments;
the L2 operator bound transfers the error to the answers. This proves
the admissible untruncated W2 probe limit without claiming an Lp matrix
bound. Both orientations are treated this way.

For paths, (42) bounds the empirical mean squared supremum error from
a fixed observation-grid interpolation by the grid spacing times the
integrated normalized squared derivative. This order of operations
avoids interchanging coordinate supremum and expectation incorrectly.
Fixed-grid joint convergence followed by this bound proves the path-W2
claim for (39). Multiplication by D(z) is continuous on continuous-path
space, and the Q path tails upgrade the resulting d convergence to W2.
Higher finite path orders follow by truncating the path norm and using
(41) at a larger order. Population tail bounds needed in this argument
can also be obtained from finite observation grids and monotone/Fatou
passage. The two samples remain in the same population tuple throughout.

## 8. Full sequence, original velocities, and observables

The full-sequence argument has the correct quantifiers. Fix the desired
error, choose a deterministic sufficiently fine comparison mesh using
the width-independent Euler/GF estimates, and only then send n to
infinity for that fixed finite program. The high-probability operator
event tends to one. This proves convergence of the entire width
sequence; no uniform-in-query theorem or subsequence law selection is
being assumed. Observation-grid passage and tail truncation then extend
the conclusion to paths, products and polynomial-growth finite-time
observables.

The finite random readout is retained in the final model. Its maximum
bound (44) implies its normalized L2 norm tends to zero. Coupling its
finite GF with zero-readout GF on the same matrices and applying A's
stability gives a vanishing state discrepancy. The product and path
arguments transfer the stated observables. This identifies zero as the
population initial readout instead of resetting the finite readout.

Uniform-in-time scalar prediction and kernel convergence follows from
the same comparisons and finite grids. K1 specifically uses the product
tail estimate for d; K2 and K3 use bounded fields and their inner
products. Probe convergence is restricted to fixed finite-program
probes and L2 approximations with the specified uniform empirical error.
This admissibility is essential; it is not a claim about arbitrary
directions chosen from the full finite matrix after seeing it.

For velocities, the dependency chain in C 9.1 is sufficient:

* Q is Lipschitz in the bounded transformed state. Its square-tail
  control justifies the products in dot z and dot H.
* Rank-one algebra directly controls dot A in HS and dot w in L2.
* The identity `dot Z=dot A H+A dot H` then gives the L2 comparison of
  dot Z, using only the true operator bound.
* At each fixed comparison mesh the truncated-probe construction gives
  W2 identification of dot Z and therefore square-tail control for its
  empirical law. There are only finitely many such probes.
* The L2 comparison with those probes and inequality (45) transfer this
  tail control to GF uniformly in time in the width limsup. One first
  fixes a sufficiently fine mesh, sends the tail cutoff to infinity,
  and then refines the mesh. Applying (36) now justifies
  `dot J=D(Z)dot Z`.

This last step is necessary: a uniform bound on `||dot Z||_2` alone
would not suffice. The candidate supplies the additional approximation
and tail argument and does not assume it from an Lp operator norm.
On the population space a continuous L2 path has uniformly integrable
squares by a finite L2 cover and (45), which supplies the corresponding
population step.

The conclusions are W2 laws at fixed times, uniform-in-time convergence
of squared norms in probability, and the resulting integrated energies.
They do not require continuous sample paths for discontinuous Euler
velocities. The stated one-sided convention at mesh points is adequate.
Parameter-increment assertions are also supported: first-layer and
readout increments follow from their paths, while the operator increment
is a rank integral whose norm is expressed through within-population
time Gram contractions. Initial A0 is never asserted to be HS.

## 9. Raw GD, interpolation, and normalization

A 8--9 contains exactly the same-initialization deterministic estimates
that C 10 imports. With `eta=n^-2`, `||Q||_infinity<=sqrt(n)||Q||_n`,
and `|z|D(z)^2<=1`, the two cubic defect terms have one-step orders
`eta^2 sqrt(n)` and `eta^3 n`. Summation through fixed T gives
`O_T(n^-3/2+n^-3)`. The first-exit bootstrap supplies the operator,
readout and residual bounds uniformly on the initialization event.
It does not presume trained-coordinate Gaussianity.

The raw interpolation is genuinely checked. Its transformed-coordinate
defect is

    (theta^2-theta) z (Delta z)^2
       + (theta^3-theta) (Delta z)^3/3,

and A bounds this and its time derivative. Consequently C (47) applies
to the recomputed cubic coordinate of linearly interpolated raw matrices,
not to a substituted transformed interpolation.

The original first-field product loses a factor sqrt(n) in the
same-width comparison. The available `O_T(n^-3/2)` state error still
gives the stated `O_T(n^-1)` raw first and hidden-field velocity errors;
operator/readout velocity errors retain the faster order. The same
estimates give the kernel and energy comparisons. These finite-width
uses of a coordinate maximum are compatible with, and distinct from,
the mesh-uniform population tail argument.

For (39), the coordinate supremum of the GD/GF path difference is at
most sqrt(n) times the uniform normalized state/field error, hence
`O_T(n^-1)`. For d, the same-width product estimate gives normalized
error `O_T(n^-1)`, so its coordinate supremum error is at most
`O_T(n^-1/2)`. Either vanishes. Thus the finite-path coupling transfers
the finite higher-Wasserstein claims without requiring a new raw-GD
moment theorem. This also explains the d part of the terse final
path-order statement in C 10.

The normalization checks give no discrepancy:

* With normalized neuron inner products, `v tensor h=vh^T/n`, the
  operator norm is the ordinary matrix spectral norm, and the HS norm
  is the ordinary matrix Frobenius norm.
* In the orthogonal geometry, first-matrix velocity has metric
  `(d/n)||dot W1||_F^2=sum_a ||dot z_a||_n^2`. Only one independent
  field occurs at rho=-1.
* At rho=-1, odd activations give H2=-H1, Z2=-Z1 and J2=-J1; even D
  gives V2=V1, Q2=Q1 and d2=d1. Also r2=-r1. Each reduced state
  update therefore has coefficient `-4r`, including both labels.
* Each kernel block is its nonnegative scalar coefficient times
  `[[1,-1],[-1,1]]`. Hence `dot r=-4 kappa r`, and since `L=2r^2`,
  `dot L=-16 r^2 kappa`. This equals minus the sum of the three raw
  squared velocity metrics. Counting two independent first-matrix
  motions in this geometry would be wrong; C (46) correctly uses m=1.

The raw-GD conclusion remains restricted to its specified `eta=n^-2`.
The separate transformed-Euler joint width/mesh limit needs no relation
between n and its mesh size because A's comparison is width independent.

## Required corrections, optional clarifications, and import decision

**Required corrections for the core bridge: none identified.**
**Required corrections for the response/remainder strengthening: none
identified.** No new mathematical hypothesis or external heavy theorem
is needed to close the checked arguments.

The following clarifications would be useful but are optional; they do
not change the verdict or require editing the candidate for this audit:

1. In a standalone reuse of Section 5.2, retain the explicit order
   “fixed mesh, fixed nonzero forcing, width limit, local-root integration
   by parts, forcing to zero.” Deleting it would obscure why empirical
   coefficient feedback creates no missing derivative term.
2. Retain the generated-space qualification on operator uniqueness.
   Equality of old laws after adding probes does not assert a unique
   operator extension to an arbitrary larger probability space.
3. Retain completed-product measurability for the every-time kernel
   representatives, and keep the current reverse term separate from
   their Lebesgue densities. No Borel selection or unique density is
   established or needed.
4. Distinguish in-probability tail control for the actual unmodified
   finite arrays from the expectation bounds proved for the clipped
   auxiliary arrays. Also retain the W2/quadratic restriction on the
   unbounded velocity/probe claims.
5. For nonuniform partitions, the phrase “k eta within T” in Section 6
   should simply be read as “t_k within T.” All estimates use the sum
   of the actual step sizes; this is a notation issue only.

**Precise modular import decision:** the reviewed snapshot may be used
as the special-angle canonical bridge with dependencies A and P as
identified above, including its separately verified response/remainder
strengthening and its optional, nonunique integral-memory representation.
It must not be promoted to the excluded all-angle, nonaffinity/nonlazy,
arbitrary-probe, Lp-operator, or long-time statements. The closing
declaration of no unresolved obligation is supported within this stated
modular scope.
