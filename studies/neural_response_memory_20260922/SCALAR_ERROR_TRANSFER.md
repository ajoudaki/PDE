# Scalar deletion error: accumulated defects, existence, and the finite-time gap

2026-09-25. Scoped theory route. Scientific inputs read completely:
`POPULATION_TO_AGGREGATES.md`, `POPULATION_SCALAR_CONSTRUCTION_CHECK.md`,
`POPULATION_FINITE_CLOSURE_CHECK.md`, and
`DEEP_ACTIVATION_ERROR_THEOREM.md`. No other research source was read.
Process inputs were the rigorous-math and conjecture skills, with the latter's
research-contract and adversarial-audit references. No experiment or Git
operation was performed. This first candidate was completed before receiving
another route's mathematical findings. It is an internal theory contribution,
not a promotion review.

The comparison argument does transfer: a small **signed accumulated scalar
defect**, combined with stability in an explicitly specified aggregate norm,
gives finite-time error and existence by a target-centered bootstrap. It does
not require the approximate aggregates to represent any network. The missing
part is an estimate making that scalar defect small after propagation. The
Legendre history estimates do not supply this estimate.

There is a further positive result at fixed finite width: finite rooted
generator templates give a common short interval on which the reference
zero-tail scalar closures exist and converge on every fixed output as the
graph cutoff increases. This interval and its constants can depend on width.
The argument uses graph distance and a scalar majorant, and does not extend
automatically to an arbitrary prescribed finite horizon. A dissipative scalar
gradient-flow example below shows precisely why bounded target trajectories,
bounded moments and generator bandedness are insufficient for that extension.

## 1. Fixed target and exact defect

The construction actually supplied by the sources is the old activity-clock,
three-hidden-layer tanh closure at finite width n and fixed history order P.
Call its state m and its vector field F_P. In the notation below, n and P
are fixed. The actual initialized matrices and their actual transposes remain
part of this target. No population existence or width limit is assumed.

Let S_K be the connected diagrams of size at most K, including every desired
training and passive-query output. Write

    z*(t) = ((q_H(m(t)))_(H in S_K), L(t)).

Static diagram coordinates may either be included with derivative zero or
stored as coefficients. Their storage and initial evaluation are still
counted. Let G_K be the finite scalar field obtained by deleting a whole
generator monomial whenever one of its connected factors is omitted. Its
clock is L'=rho, with rho the RMS of its own output residuals. Then

    (z*)' = G_K(z*) + R_K,       z' = G_K(z),           (1)

where the clock component of R_K is zero and every other component is the
explicit sum of deleted generator monomials evaluated on m(t). This is an
identity, not a closure hypothesis. R_K is a proof quantity, never a forcing
supplied to the scalar evolution.

The algebraic domain is L>0. The scalar field is locally Lipschitz there,
including at zero residual, and L'>=0 gives L>=1 on every solution initialized
at L=1. This rules out the clock singularity but does not by itself rule out
finite-time growth of other scalar coordinates.

## 2. Signed accumulated defect and a target-only existence theorem

Choose a norm ||.||_K on the retained scalar state. Define

    A_K(t) = integral_0^t R_K(s) ds,
    a_K(T) = sup_(t<=T) ||A_K(t)||_K.

Assume the target exists on [0,T]. Fix a radius r_K>0 such that the closed
r_K-neighborhood of its compact path is contained in L>0. Suppose

    ||G_K(v)-G_K(z*(t))||_K <= Lambda_K ||v-z*(t)||_K  (2)

whenever ||v-z*(t)||_K<=r_K, uniformly in t. A Lipschitz bound on each
target-centered ball suffices; realizability of v is not required. In finite
dimension such a finite bound exists for each fixed K on any compact tube
strictly inside the domain. Its growth with K is the important issue.

Let the initial scalar error be e_0=z(0)-z*(0). If

    exp(Lambda_K T)(||e_0||_K+a_K(T)) < r_K,           (3)

then the scalar solution exists uniquely through T and

    sup_(t<=T)||z(t)-z*(t)||_K
       <= exp(Lambda_K T)(||e_0||_K+a_K(T)).           (4)

For an output readout O_K with Lipschitz constant C_K on the tube, multiply
(4) by C_K. The construction's output readouts are coordinate projections,
so C_K is determined entirely by the chosen norm and weights.

**Proof.** Until the first exit from the tube, subtraction and integration
of (1) give, with e=z-z*,

    e(t)=e_0-A_K(t)+integral_0^t [G_K(z(s))-G_K(z*(s))] ds.

Consequently ||e(t)||_K<=b(t)+Lambda_K integral_0^t||e(s)||_K ds, where
b(t)=||e_0-A_K(t)||_K. Iterating this scalar integral inequality gives the
slightly sharper estimate

    ||e(t)||_K <= b(t)
       + Lambda_K integral_0^t exp(Lambda_K(t-s)) b(s) ds.   (5)

For example, the iteration follows by substituting the inequality into its
integral repeatedly; the remainder after j substitutions is bounded by a
finite supremum times (Lambda_K t)^j/j!, which tends to zero. Bounding b by
||e_0||_K+a_K(T) gives (4). The strict inequality (3) excludes a first exit.
On each finite-dimensional compact tube G_K is bounded and locally Lipschitz.
A solution with a finite maximal endpoint has bounded derivative, hence a
limit there, and local existence from that limit extends it. Thus a failure
of continuation before T is also excluded. This proves the assertion.

Exact permitted preprocessing makes e_0=0. Numerical or approximate
population initialization would contribute its own nonzero e_0; it cannot
be dropped from the comparison.

A simpler sufficient source estimate is

    a_K(T) <= integral_0^T ||R_K(s)||_K ds.             (6)

The signed version can exploit cancellation unavailable in (6). Neither
version is known to decrease for the diagram cutoff. The old history proof
actually establishes an absolute integrated-velocity bound using positive
projection energies, so it is stronger than merely observing cancellation.
There is currently no corresponding projection-energy identity for deleting
graph monomials.

## 3. Observable propagation can be weaker than full-state stability

On a stopped tube, write exactly

    G_K(z)-G_K(z*) = B_K(t)(z-z*).                     (7)

When G_K is continuously differentiable on the segment, one may take the
segment average of its Jacobian. Smoothness is not essential here. Polynomial
products and inverse powers of L admit finite telescoping difference
identities. For the residual norm, if u,v are the residual vectors,

    ||u||_2-||v||_2 = [(u+v)/(||u||_2+||v||_2)] dot (u-v),

with coefficient zero when both vectors vanish. This constructs a bounded
measurable secant B_K preserving the generator's coordinate dependence even
at zero residual.

Let U_K(t,s) solve partial_t U_K=B_K(t)U_K, U_K(s,s)=I. A bounded measurable
finite matrix B_K has this propagator: successive substitution of the
integral equation converges absolutely, bounded by the exponential series.
Variation of constants, verified by differentiating its right-hand side,
then gives

    e(t)=U_K(t,0)e_0-integral_0^t U_K(t,s)R_K(s) ds.    (8)

For a scalar output ell^T z, set lambda(s)=U_K(t,s)^T ell. It satisfies

    -lambda'=B_K(s)^T lambda,  lambda(t)=ell,
    ell^T e(t)=lambda(0)^T e_0-integral_0^t lambda(s)^T R_K(s) ds. (9)

Thus output accuracy only needs control of the defect after its pairing
with the relevant backward sensitivities. Large errors in irrelevant graph
coordinates need not spoil a given output. Conversely, small coordinatewise
boundary errors alone do not control an amplified output.

These are proof identities. The secant and adjoint depend on compared paths;
they are not coefficients available to the autonomous scalar solver. A useful
theorem must bound them from permitted initial information or an independently
proved tube estimate. Output-only estimates also do not prove full scalar
continuation without a separate bound keeping the finite scalar state bounded.

Integrating (8) by parts in the defect primitive gives

    e(t)=U_K(t,0)e_0-A_K(t)
       -integral_0^t U_K(t,s)B_K(s)A_K(s) ds.          (10)

This is the propagator form of the accumulated-defect comparison and shows
the derivative/propagator control needed to exploit cancellation.

## 4. A precise sufficient weighted-tail hypothesis

One possible global-on-[0,T] theorem would use a sequence space X for all
diagram coordinates and L, with compatible finite restrictions. Required
properties are:

1. The exact aggregate path Q(t) is continuous in X. Projections Pi_K have
   norm at most one, and
   tau_K=sup_(t<=T)||(I-Pi_K)Q(t)||_X tends to zero.
2. The infinite generator G is defined on a neighborhood containing this
   path and its sufficiently large truncated projections, and is Lipschitz
   there with one finite constant Lambda. Its finite restriction satisfies
   G_K=Pi_K G E_K, where E_K inserts zeros into omitted coordinates.
3. The target-centered scalar tubes have a positive common radius, and the
   desired readouts are bounded linear maps on X with a common bound C.

Zero insertion implements exactly the specified whole-monomial deletion.
Under these assumptions,

    ||R_K(t)||_X
      =||Pi_K[G(Q(t))-G(E_K Pi_K Q(t))]||_X
      <= Lambda tau_K.                              (11)

The previous bootstrap therefore proves eventual existence and output error
at most C Lambda T exp(Lambda T) tau_K with exact initialization. A direct
bound on the propagated defect could replace these stronger assumptions.

This is an explicit sufficient hypothesis, not a property established for
the present dictionary. In a weighted supremum norm

    ||q||_w = sup_H |q_H|/w_H,

it is necessary to control the whole weighted tail and the generator's
weighted row sums; bounded individual graph values are insufficient. For
supremum norms, uniform boundedness alone does not imply a vanishing tail.
Using a stronger exponential envelope than the target's can make the tail
small, but differentiation introduces factors proportional to graph degree.
It generally loses that stronger envelope. Uniform generator boundedness
therefore does not follow merely by selecting weights after seeing a
coordinatewise bound.

At finite n the physical theorem bounds the finitely many neuron fields
and the fixed initialized entries on a prescribed interval. Consequently,
for some finite D_T>=1,

    |q_H(m(t))| <= D_T^(size(H)).                     (12)

Indeed every summand in its normalized contraction is bounded by the product
of the entry/field bounds, and there are exactly n^|V| summands. This is a
growth estimate, not a decaying graph tail or a stable propagation estimate.
D_T can grow with n. In particular the raw parallel-edge coordinate already
diverges with n under the specified Gaussian scaling. Nothing here repairs
that population obstruction.

## 5. What generator bandedness does prove

Give outputs and the clock a fixed grade h_0 (one may use h_0=3 for
q_(c h3,a)), and give a diagram grade max(h_0,size(H)). Increase Delta if
needed so that a grade-h equation depends only on grades at most h+Delta.
The compiler provides a finite such Delta. For K>=h_0, defects occur only
in grades h>K-Delta. Static rows have zero defect.

On a tube, use normalized coordinates with weights w_H. Suppose a secant
as in (7), in these coordinates, has absolute row sums at most a(h) in a
grade-h row. An output row of grade h_0 in a j-fold matrix product can only
reach grades at most h_0+j Delta. Its absolute row sum is at most

    product_(r=0)^(j-1) a(h_0+r Delta).               (13)

To verify this, after one multiplication the grade bound is the generator
bound, and the row sum is at most a(h_0). Each subsequent multiplication
increases the reachable grade by at most Delta and multiplies the row-sum
bound by the supremum row bound at that grade. Replacing a by its increasing
envelope if necessary proves (13) by induction.

If D_K bounds the normalized defect norm, exact initialization and the
time-ordered expansion of (8) give

    |output error|/w_output
      <= D_K sum_(j=d_K)^infinity
           [T^(j+1)/(j+1)!] product_(r=0)^(j-1) a(h_0+r Delta),
    d_K=floor((K-h_0)/Delta).                        (14)

Empty products are one. Terms j<d_K vanish because their reachable grades
do not meet the boundary defect. The simplex of j+1 integration times has
volume T^(j+1)/(j+1)!, giving the displayed denominator. At fixed K the exact
series converges using the largest finite row bound; (14) is useful whenever
its larger displayed majorant converges. Delta=0 is the separate trivial
case: retained equations have no omitted factors and the finite system is
exact on its retained outputs.

If a(h)<=C independently of h, the factorial in (14) gives fast suppression
of distant boundary errors on every fixed horizon, provided D_K does not
overwhelm it and scalar existence is separately secured. For the present
product-rule compiler the natural estimate is instead a(h)<=C_R h on a
fixed exponential envelope. The product then equals

    C_R^j Delta^j (h_0/Delta)_j,

where (a)_j=a(a+1)...(a+j-1). This is almost factorial growth. The majorant
has a positive-time convergence condition C_R Delta T<1, not an
all-finite-time consequence of bandedness.

### A nonvacuous short-time theorem for the actual finite-n compiler

For fixed n,P,data,initialized arrays and a finite query list, there is a
T_0>0 independent of K such that the reference scalar closure exists through
T_0 for every K containing the outputs and converges uniformly there to the
fixed-P outputs as K tends to infinity. This assertion does not say T_0 or
the necessary K is uniform in n.

Here are the additional estimates and proof; they are derived from the
finite rooted compiler, rather than assumed as a scalar-tail hypothesis.

Each differentiated diagram has at most h decorated sites. Replacing one
site inserts one of a fixed finite collection of rooted expressions. It
introduces only a bounded number of disconnected factors, and the sum of
their sizes is at most h+D for a fixed D, after absorbing the finite residual
and rho powers into this bound. The same bound includes the clock as a low
grade coordinate. Inverse powers of L are bounded on L>=1. Thus constants
C,D, independent of K and h, exist such that an envelope

    |q_H|<=b^(grade(H)),  1<=L<=b^h_0,  b>=1

implies

    |(G_K)_H| <= C h b^(h+D),                         (15)

and the corresponding clock bound. Deleting terms cannot worsen this
absolute estimate. This follows before canonical graph collection: each
site contributes a bounded finite list, so their absolute coefficient sum
is at most C h. The number of resulting factors per monomial is bounded
independently of h. No estimate on the number of all graph types is needed.

Choose b_0>1 larger than all initialized field magnitudes and all |nW0_ij|.
The exact initialized diagrams obey |q_H(0)|<b_0^h. Increase C and D to
cover the low-grade clock and let

    b'=2C b^(D+1),   b(0)=b_0.                       (16)

For D>0 this gives b(t)=b_0(1-2CD b_0^D t)^(-1/D) up to its positive
blowup time; for D=0 it gives b_0 exp(2Ct). The derivative of b^h is
2C h b^(h+D), strictly larger than (15). A first-crossing argument in the
finite scalar state therefore bounds every closure coordinate by b(t)^h
as long as this majorant is finite. The clock remains at least one. These
finite-dimensional bounds give continuation for every K on any smaller
common interval.

The old tanh target exists on that interval by the parent theorem, with
finite bounds on all raw fields. Fix a smaller interval and an R that bounds
both b(t) and the raw-target envelope from (12). On the segment between
target and scalar states, both have normalized coordinate magnitudes at
most one in weights R^h. Telescoping each generator monomial shows that the
normalized secant row sums are at most C_R h. In fact the number of factors
per monomial is uniformly bounded, their total grade is at most h+D, and
the inverse-L and rho differences obey the bounds in section 3. The same
absolute estimate gives D_K<=C_R K for the normalized boundary defect.

Now reduce T_0 further so that lambda=C_R Delta T_0<1. Equation (14) gives

    sup_(t<=T_0)|output error|/R^h_0
       <= C_R K T_0 sum_(j=d_K)^infinity
                      lambda^j (h_0/Delta)_j/(j+1)!. (17)

The ratio (a)_j/j! grows at most polynomially: for a>=1, write its factors
as 1+(a-1)/r and use log(1+x)<=x and
sum_(r=1)^j 1/r<=1+log(j+1); for 0<a<=1 the ratio is at most one.
The tail of a polynomial times lambda^j is exponentially small in d_K.
Since d_K grows linearly with K, the right side of (17) tends to zero even
with its prefactor K. This proves uniform convergence of each fixed output.

The theorem uses no neural runtime state: the large initialization bound
and all target moments are proof quantities. It proves only a positive
interval, not useful computational complexity or a finite-population model.
The constants can be extremely poor. It also does not justify resetting
missing high moments to their exact trained values to repeat the interval;
those values would be unavailable to the scalar solver.

### Why the short-time theorem cannot simply be iterated

Consider the standalone dissipative scalar flow

    x'=-x^3,  x(0)=1,  x(t)=(1+2t)^(-1/2).

It is gradient flow for the nonnegative loss x^4/4. The target exists and
stays bounded for every t>=0. Every moment q_k=x^k lies in [0,1] and obeys

    q_k'=-k q_(k+2),  q_k(0)=1.                       (18)

This is a banded hierarchy with linear-in-k row growth. Apply exactly the
zero-tail rule q_j=0 for j>K. Repeated integration of the finite triangular
system gives

    q_1^K(t)=sum_(j=0)^floor((K-1)/2)
                (-1)^j [(2j-1)!!/j!] t^j.           (19)

For j=0 the double factorial is one. The magnitude ratio between consecutive
terms is t(2j+1)/(j+1), tending to 2t. If t>1/2, the terms fail to tend to
zero, so the partial sums cannot converge. All finite truncations themselves
are polynomial solutions existing for every time.

Thus global physical existence, dissipative energy, bounded target moments,
an exact hierarchy, matching arbitrarily many initial derivatives and
bandedness together still do not prove zero-tail convergence on every finite
horizon. This is a counterexample to that proof principle, not a
counterexample to the specific neural scalar hierarchy. A fresh special
estimate or a modified admissible closure could still establish the desired
neural result.

## 6. Connecting the distinct P and K errors

The scalar compiler in the assigned sources is the old activity-clock
tanh compiler. It has not been supplied for the new weighted Gram/response
clock. Accordingly, use the old parent rate only:

    sup_(t<=T)||theta_P(t)-theta_dense(t)||
       <= C_old(T)/sqrt(P(P+1)).                     (20)

For tanh this is available for every P>=1 on a fixed finite-width horizon.
On the parent theorem's common compact physical region, each fixed query
output has a finite physical-parameter Lipschitz constant a_query(T).
The forward and backward bounds used for training outputs extend to a
fixed passive-query list by enlarging the finite input bound. Hence, whenever
the scalar error theorem has actually supplied an output error E_(n,P,K)(T),

    sup_(t<=T)|f_scalar-f_dense|
      <= E_(n,P,K)(T)
         + a_query(T) C_old(T)/sqrt(P(P+1)).          (21)

The scalar approximation is compared directly in output space. No parameter
vector theta_scalar is introduced or inferred from scalar realizability.
The constants and feasible K in the first term may depend strongly on P.
For arbitrary-accuracy approximation on a prescribed T one would first
choose P for the second term, then need a scalar theorem at that fixed P
covering that same T. The positive interval in section 5 does not supply
this missing arbitrary-T assertion.

The parent's quadratic rate for the new clock could enter such a triangle
inequality only after constructing and validating the corresponding new
scalar compiler, domain and defect. Replacing the exponent in (21) by two
without that work changes the target.

For an every-angle readout from a finite passive-query grid, add the separate
target angular interpolation error B_T h, as in the source. Physical-time
uniform bounds do not by themselves compare fitted stopping times, nor do
they control infinite-time fitting endpoints.

## 7. Exact missing obligations and present status

| Obligation | What the parent finite-time theorem supplies | What it does not supply |
|---|---|---|
| Fixed-P target existence | Old tanh closure exists on every finite horizon | Scalar closure existence at arbitrary K,T |
| Target boundedness | Finite raw-field and physical bounds at finite n | Width-uniform arbitrary graph bounds |
| Scalar consistency | Supplied separately by the exact compiler | A decreasing graph-cutoff defect |
| Defect production | Legendre projection energies control the P error | A graph-tail energy, cancellation estimate, or decay in K |
| Stability | Physical field comparison on a physical compact set | Uniform aggregate Lipschitz, semigroup, or adjoint bounds |
| Scalar continuation | Follows if the target-tube error closes; also follows locally from (16) | Network loss monotonicity or realizability for arbitrary scalar states |
| Population identification | No population claim in the parent theorem | Finite limits, domains, integrability and uniqueness for the raw graph hierarchy |

Established here: the accumulated-defect bootstrap, exact observable/adjoint
identities, a sufficient weighted-tail theorem, and finite-n short-time
convergence from the compiler's rooted locality. Open: convergence and useful
accuracy on every prescribed finite horizon, width-independent accuracy,
efficient initialization and any identified population limit. The key next
proof obligation is a propagated graph-boundary estimate on the actual
reachable target family, together with scalar continuation on that horizon.

## 8. Collaborative check after the independent candidates froze

The supervisor next authorized the following complete additional inputs,
which were read in full. This check is collaborative, not an independent
promotion review. No experiment or additional scientific source was used.

| Frozen artifact | SHA256 |
|---|---|
| This report before the present addendum | `e002d902bff3737c439802935141d9ebc23a84c45729a4c3756243e9d7142431` |
| `SCALAR_POSITIVE_ROUTE.md` | `4b6b15b7322b8adedbb6038e834229377facd9d62c4c4e28e37d86a0c7125a5a` |
| `SCALAR_COMPRESSION_BOUND_ASSESSMENT.md` | `b580384d4de77da09664b54a44c83f1a7d8c9fd713444d13d90c95a48c78ae68` |

### Local dependency-distance estimate

The positive route's finite-template estimates agree with the independent
derivation in section 5 above. Its direct iteration of the interior error
inequality is simpler and sharper than bounding the explicit boundary defect.
For normalized maximal errors E_m over all diagrams of size at most m and
the clock, it obtains

    E_m(t)<=C m integral_0^t E_(m+delta)(s)ds,
       m+delta<=K,

and closes the final iteration using E_(m+r delta)<=2 on the common bounded
interval. With r=floor((K-m)/delta), this gives

    E_m(t)<=2 (Ct)^r/r! product_(j=0)^(r-1)(m+j delta).

Every substituted row is an interior row: in the last substitution,
m+(r-1)delta+delta<=K. The final E_(m+r delta) need not obey an interior
equation; its envelope bound is sufficient. The clock is included at every
level, and its dependence only on training outputs fits the same inequality.
The geometric-polynomial convergence proof is therefore valid. This version
removes the prefactor proportional to K introduced by the coarse boundary
defect bound in (17). Both prove the same fixed-width positive-interval
convergence statement.

### Arbitrary finite horizons under a scalar-trajectory envelope

The positive route proves a useful sufficient continuation result stronger
than merely writing a conditional Lipschitz comparison. Suppose for the
prescribed finite T that all sufficiently large truncations satisfy

    |q_H^K(t)|<=R_T^(size(H)),

with one finite R_T independent of K on their maximal intervals through T.
Enlarge R_T to cover the genuine target diagrams as well. The clock then
has the bound 1<=L<=1+T(R_T^3+Y). For each fixed K these bounds give compact
continuation through T. The same local template estimate has a constant C_T
independent of K throughout the horizon.

Choose h>0 with C_T delta h<1. If all fixed-degree errors tend to zero at
the left endpoint s, r substitutions on [s,s+h] yield a finite sum of
initial errors E_(m+j delta)(s), j<r, plus a remainder bounded by a
polynomial in r times (C_T delta h)^r. At fixed r, every degree in that
finite sum is fixed, so letting K tend to infinity makes the sum vanish.
Then r tends to infinity and eliminates the remainder. This proves uniform
convergence on that interval for each fixed degree and the clock. The
initial errors are zero on the first interval, and induction over finitely
many intervals covers [0,T].

The order of these limits is valid and needs neither one cutoff working
uniformly over all graph degrees nor values supplied from an intermediate
target state. Each cutoff is fixed once and its original ODE runs throughout
the proof. Thus this is an authentic conditional arbitrary-finite-T theorem
for the specified autonomous witness. It does not conflict with the warning
against automatic iteration in section 5: the uniform bound on *scalar
truncation trajectories* is exactly the extra hypothesis absent there and
absent from the parent physical theorem. The counterexample (18)--(19)
violates this hypothesis already in its lowest output at large times.

### Forest preservation in the actual old-clock compiler

The synthesis's forest lemma is correct for its stated starting observables
and compiler. Each operation in the specified rooted-expression construction
preserves a rooted tree or a product of such components:

* Componentwise products identify only the roots of fresh copies.
* An initialized action adds a new root, one edge, and the old rooted tree.
* A normalized average closes a root's index without identifying vertices.
* Learned matrix actions are rooted local fields multiplied by scalar
  normalized pairings. Matrix velocities and forward/backward chain rules
  are sums and products of the same operations.

Differentiating one decoration attaches a fresh rooted expression only at
that vertex, so an original tree cannot acquire a symbolic cycle. Starting
primitive means and Grams have one vertex; expanding backward fields before
forming their products gives the same rooted-tree construction. Repeated
forward/transpose use remains covered: for example, W0^T W0 acting on a
field produces a path with a fresh leaf in the original layer, not a trace
cycle. Coincidences between numerical neuron indices in a finite sum do not
identify the corresponding symbolic vertices.

Therefore every retained forest row of the full graph-cutoff ODE depends
only on forest factors. Its deletion test and initialized values are
unchanged when cyclic coordinates are discarded. The forest subsystem is
autonomous and agrees, by finite-dimensional uniqueness, with the forest
coordinates of the full system on their common existence interval. A cyclic
observable deliberately requested as an output would lie outside this
claim. Gaussian averaging could also reorganize symbolic expressions, but
no such probabilistic rewrite occurs in the supplied compiler.

This is an exact and useful pruning result. It removes the specific static
parallel-edge obstruction from the output-generated subsystem without
proving width-uniform bounds or finite population limits for its trees.
The local convergence arguments apply to this subsystem as well: deleting
unneeded cyclic rows does not change the finite-template bounds. No
substantive mathematical flaw was identified in the checked claims. The
root synthesis at the recorded hash had not yet incorporated the independent
local theorem; the supervisor is adding that result separately.

## 9. Constructive repair: a bounded-input scalar closure on any finite horizon

After the preceding candidates and checks froze, the supervisor proposed
the following explicit modification for independent audit. It is a new
stabilized witness within this same scalar-compression investigation, not
an assertion about the original unsaturated zero-tail ODE. The derivation
below uses only the already authorized sources and the stated proposal.
No experiment or further source was used.

**Theorem.** Fix finite n,P,T, the old-clock three-hidden-layer tanh target,
finite data and initialized arrays, and a fixed finite query list. There is
an explicitly specified autonomous scalar closure with the same graph list
at cutoff K and a static componentwise saturation such that:

1. Every finite cutoff containing the output diagrams exists uniquely for
   all positive time.
2. Its reported outputs converge uniformly to the fixed-P target outputs
   on [0,T] as K tends to infinity.
3. The equations, saturation thresholds and initial coordinates use only
   data, initial arrays, P, T and their derived a priori bounds. No evolving
   neuron state, target forcing or population refresh is supplied at runtime.

The theorem holds for either the complete graph list or its exact forest
subsystem. Its sufficient cutoff and constants may depend on n. It gives
neither a practical complexity bound nor a finite population limit.

### Definition and permitted thresholds

The parent old-clock tanh theorem bounds all physical fields, raw history
fields and the clock through T from initial data. Include the fixed numbers
|nW0_ij| in the bound. As in (12), choose a finite R>=1 with

    |q_H(m(t))|<=R^(s(H))  for all diagrams H and 0<=t<=T.          (22)

One can use a common bound on every raw field entry and every initialized
edge entry. It is crude but depends only on permitted initial information;
it does not require measuring a trained target trajectory. The explicit
raw-moment bounds in `SCALAR_POSITIVE_ROUTE.md`, section 2, explain how the
parent field bounds provide this input. This same R covers initialization.

For each retained diagram define the scalar map

    S_H(v)=max(-R^s(H), min(v,R^s(H))).

It is 1-Lipschitz and equals the identity on the corresponding target
coordinate throughout [0,T]. Let S act componentwise on diagram coordinates
and leave the clock separate. For the original zero-tail field G_K, define
the modified diagram and clock equations by

    y_H' = (G_K)_H(S(y),ell),
    ell' = rho(S(y_output)),
    y_H(0)=q_H(m(0)),  ell(0)=1.                                  (23)

Static coordinates have derivative zero. Their saturation is inactive at
their exact initialized values, so one may equivalently store them as fixed
coefficients. Every occurrence of a diagram factor or training output inside
the right-hand side, including residuals and their RMS, uses the same S(y).
Only the initialized contraction values and the finite symbolic table are
needed after preprocessing.

For an unambiguous readout, define

    fhat_a=S_(c h3,a)(y_(c h3,a)),
    rhat_a=fhat_a-y_a,  loss_hat=mean_a rhat_a^2.                    (24)

Then the residuals and activity clock in (23) use the declared predictions.
The raw output coordinate also converges by the proof below. Reporting that
raw coordinate instead would require stating that internal residuals are
computed from its clipped version; (24) avoids that discrepancy. No loss
monotonicity or moment realizability is asserted for (23).

### Global finite-cutoff existence and the missing envelope

Use the finite-template constants A,D from the positive route, enlarged if
necessary so that D>=1. All saturated inputs obey |S_H(y_H)|<=R^s(H),
and ell>=1 because its derivative is nonnegative. Consequently, globally
in the raw diagram variables y,

    |y_H'|<=A s(H) R^(s(H)+D),
    0<=ell'<=R^3+Y.                                               (25)

For each fixed K the field is locally Lipschitz on ell>0: saturation and
the residual norm are Lipschitz, products have bounded inputs locally, and
the inverse-clock denominators are regular there. The derivative bounds
(25) prevent finite-time escape, while ell stays at least one. A finite
maximal endpoint would therefore have a finite state limit and extend by
local existence. This proves global finite-cutoff existence.

On the prescribed interval let c=A T R^D and set W=R(1+c). Integration
of (25), followed by the elementary binomial inequality, gives for h=s(H)>=1

    |y_H(t)| <= R^h(1+c h) <= [R(1+c)]^h = W^h,
    1<=ell(t)<=L_*:=1+T(R^3+Y).                                   (26)

Indeed (1+c)^h>=1+h c for every integer h>=1. The scalar envelope W is
independent of K. This proves, rather than assumes, the stability hypothesis
that was missing for the original deletion rule.

### Consistency and convergence

On the genuine target S(q(t))=q(t), so the modified retained target equation
has exactly the same deletion remainder as before. Saturation introduces
no extra defect along that target on [0,T]. For every coordinate,

    |S_H(y_H)-q_H(t)|
       =|S_H(y_H)-S_H(q_H(t))|
       <=|y_H-q_H(t)|.                                           (27)

Use the normalized errors

    E_m(t)=max(|ell(t)-L(t)|/L_*,
               max_(s(H)<=m)|y_H(t)-q_H(t)|/W^s(H)),  m>=3.

The target also obeys the bounds in (26), so E_m<=2. The finite-template
product estimates, (27), the Lipschitz residual norm and inverse-clock
bounds give one finite C, independent of K and m, such that every interior
level satisfies

    E_m(t)<=E_m(s)+C m integral_s^t E_(m+delta)(u)du,
       m+delta<=K.                                              (28)

Here delta is any valid positive component increment, and both paths exist
through T. Saturation does not introduce new coordinate dependencies, so
the same delta applies. The constant can be bounded explicitly by the
finite templates using W and L_*.

On an interval of length tau with C delta tau<1, iterate (28) a fixed r
times. The result is a finite sum of fixed-level initial errors plus the
terminal bound 2 times a polynomial in r times (C delta tau)^r. As proved
in section 8, first taking K to infinity at fixed r and then r to infinity
gives uniform convergence on that interval. The initially identical diagram
values start the induction. Finitely many such proof intervals cover
[0,T]. This proves convergence of every fixed raw diagram and the clock.
Equation (27) transfers it to the readouts (24), including passive queries.

These proof intervals do not alter or restart the scalar ODE. Their exact
target endpoint values occur only in the comparison proof. The actual
algorithm has the fixed thresholds chosen before training and evolves (23)
without any reference-state update.

### A computable finite-cutoff certificate

The proof need not leave the sufficient K as an unknown trajectory-dependent
choice. The following finite recursion provides an explicit, although
potentially very conservative, bound from the template constants.

Take N=max(1,ceil(2C delta T)), tau=T/N and

    b_(m,p)=(C tau)^p/p! product_(i=0)^(p-1)(m+i delta),
    b_(m,0)=1.

For fixed K and integer 3<=m<=K define B_0^K(m)=0. For j=1,...,N define

    B_j^K(m)=min_(0<=r<=floor((K-m)/delta)) {
        sum_(p=0)^(r-1) b_(m,p) B_(j-1)^K(m+p delta)
        +2 b_(m,r) }.                                            (29)

At r=0 the sum is empty and the candidate value is 2. Iterating (28) r
times on proof interval j and using the preceding interval's endpoint
bound proves that B_j^K(m) bounds the maximum E_m on interval j. The
argument only uses finitely many numbers and no trained target values.

For each fixed j,m, B_j^K(m) tends to zero as K increases. For j=1 this is
the geometric-polynomial remainder. Inductively, at fixed r all finitely
many B_(j-1)^K(m+p delta) tend to zero, after which r can increase to make
the remainder vanish. Hence

    max_a sup_(t<=T)|fhat_a(t)-f_a(t)|
       <= W^3 max_(1<=j<=N) B_j^K(3) -> 0.                       (30)

The same expression covers every retained passive output. Searching K using
the explicit right-hand side gives a finite sufficient cutoff for any
positive tolerance, using initial-data bounds and the generator templates
only. The theorem does not claim that this search or the resulting graph
system is computationally efficient.

### Claim boundary

This repair upgrades the existence claim for an explicit stabilized scalar
witness: for fixed finite n,P and any prescribed finite T, arbitrary output
accuracy is obtained by a sufficiently large finite cutoff. Its dimension
and coefficient-table type count at fixed cutoff are independent of width,
but R,W,C, the sufficient cutoff and preprocessing cost need not be. A
width-independent accuracy theorem still requires substantially stronger
estimates. The old parent P-error can be added as in (21), so choosing P
and then this modified scalar cutoff yields arbitrary finite-time dense
output accuracy at fixed finite width.

The original unsaturated zero-tail hierarchy still has only the proved
local theorem and conditional arbitrary-T result. Saturation changes its
off-target evolution. The new conclusion must therefore be attributed to
(23), not retrospectively to the original solver. It also does not establish
the new weighted-clock scalar compiler, an infinite-population construction,
all-time uniform error, useful small-cutoff performance, numerical stability
or efficient initialization.
