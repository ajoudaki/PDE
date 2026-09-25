# Scalar tail deletion: obstruction audit

2026-09-25. Scoped independent theoretical route. Scientific inputs read in
full: `POPULATION_TO_AGGREGATES.md`,
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`, and
`DEEP_ACTIVATION_ERROR_THEOREM.md`. Required process inputs: the
solve-math-rigorously skill and the investigate-conjectures skill, including
its research-contract and adversarial-audit references. No other study
artifacts, other route findings, experiments, solver code or Git history were
read. This report is frozen before exchange with other routes. It is an
internal analysis, not an independent promotion review.

**Conclusion.** The specified scalar compiler is an exact algebraic starting
point, but boundedness of the target, exact residual/clock coefficients,
small boundary moments and agreement of increasingly many initial
derivatives do not by themselves imply convergence of zero-tail deletion
on every fixed time interval. A counterexample below proves this statement
for a connected-moment compiler that keeps its residual and clock exact;
the example even has exponentially small exact boundary defects and bounded
target particles. It is not a realization of the specified tanh
response-memory network, so it does not falsify convergence of that exact
neural hierarchy. That convergence remains open on the supplied inputs.

## 1. Exact claim under examination

Fix the neural width n, history order P, realized initialization, data and a
finite physical horizon T. The approximation is precisely (5)--(6) of
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`: keep connected diagrams of size
at most K; factor disconnected diagrams; delete a monomial when any
connected factor is omitted; keep the residual coefficients and
rho(q)=RMS(f(q)-y), L'=rho(q) exactly. Initialization uses the true initial
diagram contractions. No target trajectory supplies later information.

The missing assertion is that these finite ODEs eventually exist through T
and their named outputs converge uniformly there as K tends to infinity.
This is separate from width-uniform accuracy, a population limit, P
refinement and convergence as T tends to infinity. The counterexample in
this report attacks a proposed general implication from the compiler's
structural properties to that missing assertion, not the full admissible
class of scalar approximations.

In particular, a counterexample obtained by lifting every product to an
independent state and truncating its total degree does not automatically
apply here. The specified compiler keeps products of disconnected
components as nonlinear products, and keeps rho and residuals as nonlinear
coefficients. The example below respects both of those distinctions.

## 2. A bounded connected-moment system with exact residual and clock

Choose 0<a<1 and any positive integer n. Consider particles x_i with output,
target, residual and clock

    q_1 = (1/n) sum_i x_i,   y=-1,
    r=q_1+1,   rho=|r|,   L'=rho,   L(0)=1,
    x_i'=-rho x_i^2,       x_i(0)=a.                    (1)

These are a deliberately specified generic particle system, not neural
gradient flow. The homogeneous initial condition remains homogeneous by
uniqueness. Its common value x stays positive and at most a: its derivative
is negative at positive x, and zero is an equilibrium. The bounded vector
field on [0,a]^n gives global continuation. On the homogeneous trajectory,
rho=1+x lies between 1 and 1+a, so L is finite on every finite physical
interval as well.

There are no fixed edges and there is one local species. The connected
diagram with k decorations on one vertex has value

    q_k=(1/n) sum_i x_i^k,   q_0=1,
    q_k'=-k rho(q_1) q_(k+1).                           (2)

Disconnected diagrams factor into products of these q_k, exactly as in the
neural compiler. The diagram for q_(k+1) is connected: its decorations
belong to the same averaged particle. It cannot generally be replaced by
q_k q_1. Even with the homogeneous initialization, the symbolic compiler
does not impose the additional evolving identity q_k=q_1^k. Doing that
would specify a different closure.

Since the connected size is k+1, size cutoff K=N+1 produces exactly

    (q_k^N)'=-k rho(q_1^N) q_(k+1)^N,  1<=k<N,
    (q_N^N)'=0,
    (L^N)'=rho(q_1^N),
    q_k^N(0)=a^k,  L^N(0)=1.                            (3)

Thus residual feedback, its absolute-value norm, disconnected
factorization, the clock and every retained coefficient remain exact.
Only the connected boundary term in the final moment equation was
deleted. The RHS is locally Lipschitz. It uses no hidden particle arrays at
runtime and its number of scalar types is independent of n.

### Exact solution in activity time

Put s=L-1. Along the target ds/dt=1+x>0, and (1) becomes

    dx/ds=-x^2,   x(s)=a/(1+as).                         (4)

For the approximate solution put s=L^N-1. Where its residual is positive,
the common coefficient rho cancels from (3), giving

    dq_k^N/ds=-k q_(k+1)^N,   dq_N^N/ds=0.

Successive integration from the highest retained moment yields

    q_1^N(s)=p_N(s)
       =a sum_(j=0)^(N-1)(-as)^j
       =a[1-(-as)^N]/(1+as).                            (5)

For every odd N, p_N(s)=a[1+(as)^N]/(1+as)>0 for s>=0.
Consequently the positive-residual condition used to derive (5) holds
throughout the approximate trajectory. Its physical clock equation is

    ds/dt=1+p_N(s),
    t(s)=integral_0^s du/[1+p_N(u)].                     (6)

For odd N>=3 the polynomial p_N has degree N-1 with positive leading
coefficient. Therefore

    t_N := integral_0^infinity du/[1+p_N(u)] < infinity. (7)

As t increases to t_N, s and q_1^N both diverge. Thus every such finite
closure has finite-time blow-up although its exact target is bounded and
global. This is an actual solution failure, not only a weak error estimate.

### The blow-up times stay bounded as the cutoff grows

As odd N tends to infinity, p_N(s) tends to a/(1+as) for 0<=as<1 and
to infinity for as>1. On 0<=as<=1 the integrands in (7) are at most one.
For as>=1 and odd N>=3,

    p_N(s) >= a(as)^3/(1+as),

whose reciprocal after adding one is integrable on [1/a,infinity), since
it is O(s^-2). Splitting at 1/a and applying the elementary dominated
integral limit therefore gives

    t_N -> t_* := integral_0^(1/a) ds/[1+a/(1+as)]
               = 1/a - log[(2+a)/(1+a)] < infinity.     (8)

For every fixed T>t_*, all sufficiently large odd cutoffs fail to exist
through T. Hence there is no convergence on every fixed physical-time
interval for this connected zero-tail family.

### The exact boundary defect nevertheless tends to zero

Evaluate the omitted term along the exact target. All retained defects
except the last one are zero, while

    R_(N,N)(t)=-N rho(t) x(t)^(N+1),
    sup_(t<=T)||R_N(t)||_infinity
       <=N(1+a)a^(N+1) -> 0.                            (9)

The initial moments are exactly realizable by a probability measure
supported inside (0,1), and their tails decay geometrically. The defect is
exponentially small uniformly on every target interval. The failure is
therefore not explained by unbounded target variables or a nonvanishing
unweighted source. Growing propagation constants and loss of surrogate
containment cannot be omitted from a convergence theorem.

Even before blow-up, realizability is lost. For odd N>=3,

    q_(N-1)^N(s)=a^(N-1)[1-(N-1)as].                    (10)

The index N-1 is even, but this moment becomes negative at a finite
activity time strictly before blow-up. No real particle distribution can
have that value for an even moment. The corresponding threshold
1/[(N-1)a] tends to zero. Thus exact realizability at initialization and
bounded realizable target paths provide no realizability preservation for
the deletion rule.

This example is a **proof-route falsifier** for a theorem based only on the
shared connected-hierarchy, boundedness, residual/clock and tail properties.
No mapping from (1) to an admissible fixed-P tanh network is established
here. It is consequently not a witness-fatal counterexample for the neural
construction in the sources.

## 3. Why the history theorem supplies a different mechanism

The history result has more than bounded trajectories and a clock.
Equations (9)--(11) of `DEEP_ACTIVATION_ERROR_THEOREM.md` give genuine
nonnegative projection errors D_f, the exact identity

    D_f'=rho ||f-fstar||^2,

and a bound on the integrated physical defect by products of these
projection errors. Polynomial approximation in the history variable then
gives D_f=O(1/[P(P+1)]) from a derivative-energy bound. The derivative
estimate is tied to the same variable in which approximation degree grows.
The new clock makes the monitored histories Lipschitz in that variable.
These facts produce a small defect before the stability and containment
argument is used.

For scalar diagram deletion, K measures the number of graph vertices,
edges and local multiplications. It is not history-polynomial order. No
nonnegative best-approximation error, energy identity or K-decaying
approximation theorem is supplied for that operation. Smooth variation in
physical or activity time does not turn powers of a local field into an
orthogonal approximation tail. In (1), all exact target variables and
their time derivatives are regular on every finite interval, but the
same-vertex moments still generate the failure above.

The target's bounds do have value. At fixed n and P, if every local species
and rescaled edge entry has magnitude at most B>=1, then the normalized
definition of a diagram directly gives

    |q_H| <= B^(|D(H)|+|E(H)|).

There are n^|V(H)| assignments and the normalization cancels that count.
This is a finite bound, not a small tail. Even a much stronger geometric
tail such as (9) is insufficient without a compatible stability estimate.
The degree factors in the product rule grow with K, so a finite size
increment per derivative does not itself provide a uniform propagator.

## 4. A concrete limit of the neural energy argument

There is an exact useful identity within the specified neural compiler.
For K>=3 both q_(c^2) and all outputs f_a=q_(c h3,a) are retained. The
outer-weight equation c'=-2 mean_a r_a h3,a gives

    (q_(c^2)^K)'=-4 mean_a r_a^K f_a^K
       =mean_a y_a^2-4 mean_a(f_a^K-y_a/2)^2.           (11)

No deleted high connected diagram appears in this equation. Therefore

    q_(c^2)^K(t)<=q_(c^2)^K(0)+t mean_a y_a^2          (12)

on every existing approximate segment. On an actual network one combines
this with nonnegativity and Cauchy--Schwarz,

    f_a^2 <= q_(c^2) q_(h3,a^2),   0<=q_(h3,a^2)<=1,

to control outputs and rho. In the zero-tail scalar ODE, these inequalities
are extra moment-realizability constraints. Their preservation is not
proved by the compiler, and (12) alone does not control the output: a
quantity with only an upper bound may become negative while its derivative
integrates an arbitrarily large output square.

This calculation identifies a precise missing step in copying the bounded-
activation proof. It does not show that the particular neural trajectory
actually violates these constraints. Neither loss of realizability nor
blow-up of that exact neural closure has been established in this route.

## 5. What a clock can and cannot repair

A pure positive reparametrization changes the speed along a fixed scalar
orbit, not that orbit. With the inverse physical-time equation retained,
the error at a given physical time is unchanged. Equations (5)--(8) already
show that an exact activity clock and exact current residual do not force
the desired global-on-fixed-T convergence.

Changing the history clock can improve approximation in history order P,
as the source proves, because it changes the regularity of the function
being projected. It supplies no immediate decay in diagram size K. To
obtain such a conclusion one would have to define a new scalar closure
and prove how its approximation error is controlled. Changing the clock
inside the fixed-P history construction also changes the target being
compressed; it cannot be silently inserted into a theorem about the
specified fixed-P old-clock target.

Similarly, rescaling each moment by a known degree-dependent constant is
only an invertible diagonal coordinate change if the same deletion is
performed. It may improve estimates or conditioning, but cannot eliminate
the blow-up in (3). Resetting or recentering a local expansion could change
the approximation family, but it would need an admissible rule for the
new moments and its own consistency and stability proof. Exact moments
from the unknown target at restart times are not permitted inputs.

## 6. Surviving theorem obligations

For the actual neural compiler, the conditional estimate in the source
remains correct. A successful proof must establish a small **propagated**
defect in a norm controlling the named outputs, together with existence
and containment of the approximate states. Plausible structural routes
would require an additional proved ingredient, for example a preserved
realizable set with useful compactness and identification, a degree-weighted
propagator estimate that controls high-to-low transfer, or a different
closure equipped with a genuine approximation-energy identity. Merely
listing these possibilities proves none of them.

The current findings have distinct scopes:

| Claim | Status from this route |
|---|---|
| Exact finite-n diagram identities and a finite autonomous deletion rule | Preserved |
| Bounded targets plus exact residual/clock and small boundary defects imply fixed-T convergence for connected zero-tail compilers | False by (1)--(10) |
| The fixed-P tanh zero-tail solver fails on an admissible neural instance | Not established |
| The fixed-P tanh zero-tail solver converges for every fixed n,P,T | Open |
| The prior history projection theorem automatically proves K convergence | Unsupported; the small-defect mechanism is different |
| Every admissible finite scalar compression is impossible | Not implied |

The highest-leverage missing fact for this particular closure is a
structure-specific stability and tail argument, or a fully mapped neural
counterexample. The generic obstruction prevents replacing that fact by
boundedness or clock regularity alone.

## 7. Collaborative post-freeze audit: forests and the positive local theorem

This addendum follows a new, explicit supervisor assignment after the
independent report above froze. I then read the complete root candidate
`SCALAR_COMPRESSION_BOUND_ASSESSMENT.md` and the complete independent
`SCALAR_POSITIVE_ROUTE.md`. This is a collaborative mathematical audit, not
an isolated or promotion review. The files were checked at these SHA-256
hashes; both newly reviewed files still had the same hashes after the audit:

* `SCALAR_COMPRESSION_BOUND_ASSESSMENT.md`:
  `b580384d4de77da09664b54a44c83f1a7d8c9fd713444d13d90c95a48c78ae68`
* `SCALAR_POSITIVE_ROUTE.md`:
  `4b6b15b7322b8adedbb6038e834229377facd9d62c4c4e28e37d86a0c7125a5a`
* `POPULATION_SCALAR_CONSTRUCTION_CHECK.md`:
  `8a2e44ad6d50995ef626a65402babed19b761f9685d9ef91fb63de7633944383`

**Internal verdict: PASS for the forest-preservation/pruning lemma and for
the fixed-n, fixed-P short-time convergence theorem, with their stated
scope.** I found no missing generator operation that invalidates either
argument. The arbitrary-fixed-T extension in the positive report is valid
conditionally on its scalar-trajectory exponential-envelope hypothesis;
that hypothesis remains unproved for the actual neural truncations.

### Forest preservation and observability

The compiler's primitive operations are local multiplication, normalized
pairing, initialized matrix or transpose action, scalar multiplication,
finite addition and substitution of the reconstructed learned factors. A
local multiplication identifies the roots of otherwise fresh rooted
expressions. It does not identify their other vertices. Thus products of
rooted trees remain rooted trees. An initialized action adds a fresh root
and one edge, regardless of forward or transpose orientation. Normalized
pairing identifies the two local roots and sums that root; the result is
an unrooted tree. A learned action contributes a local history field times
a normalized pairing, so its additional scalar pieces are detached trees.

The two matrix velocities and the lifted forward velocities use only
these same operations after differentiating the rank-one history products.
Their explicit evaluation order does not introduce traces, edge squaring
with two shared endpoints, or identifications of separate summed indices.
Backward recursions add initialized transpose actions and local gates;
expanding each gate as 1-h^2 only adds local decorations. Differentiating
a diagram replaces a decoration at one existing vertex and grafts fresh
rooted pieces there. It preserves every existing edge and attaches no
piece at two different existing vertices. Consequently no cycle is
created from a tree. The possible removal of an undecorated isolated root
does not affect this conclusion.

This also checks the potentially misleading repeated-index case. Two
copies of an initialized action in a squared backward field have separate
summation variables, even when some assignments happen to give those
variables equal numerical values. They form separate branches in the
symbolic graph. Those collisions are already included in the normalized
sum; they do not make a parallel-edge graph with symbolically identified
endpoints. Such an identification would require an additional contraction
operation that is absent from this compiler.

The ordinary outputs, means and same-layer Grams in the starting list are
therefore forest expressions after expanding backward fields. Every
forest row depends only on forest coordinates, including its residual
and clock dependence through ordinary outputs. Moving a static diagram
value into a stored coefficient does not create an exception: a static
cyclic factor cannot be generated in a forest row by the operations just
checked. The cutoff test uses connected component sizes, so restricting
the full cutoff vector field to its forest coordinates gives the same
finite equations as compiling only those coordinates. Equal initial
forest values and local uniqueness prove equal output trajectories on
the common existence interval.

The limitation concerning the common interval is necessary and is stated
in the root candidate. A cyclic component outside this subsystem could
in principle end the full ODE's existence earlier; autonomous continuation
of the forest subsystem would not prove continuation of the full state.
The lemma also does not say that arbitrary cyclic observables can be
recovered from trees, that all tree contractions have finite population
limits, or that pruning alone gives convergence. In particular, the
parallel-edge Frobenius-norm obstruction applies to the original whole
dictionary but is not generated by these ordinary output observables.
The root candidate confines its conclusion appropriately.

### The short-time majorant

The positive route correctly strengthens the compiler's finite component
increment to a finite total-size increment. A decoration substitution
removes one decoration, adds one fixed finite rooted expression, and
identifies its root with the old vertex. All additions to total size are
therefore bounded by a constant independent of the original graph.
Factoring a disconnected union preserves the sum of component sizes;
removing an isolated undecorated vertex reduces it. At most a fixed number
of components is added, and there are at most O(s(H)) uncombined terms
because the product rule selects a decoration. Canonical relabeling can
combine such terms but does not create extra multiplicities beyond their
sum of absolute coefficient bounds.

The residual and rho remain nonlinear coefficients, precisely as required
by the actual solver. Their dependence is controlled by the size-three
output coordinates. Since L>=1, all powers of L^-1 are bounded. On a box
|q_H|<=b^s(H), with b>=1, these facts justify

    |F_(K,H)| <= A s(H) b^(s(H)+D),

with constants independent of K. Static diagrams can equivalently be kept
as zero-velocity coordinates for this argument, so treating some of them
as stored coefficients does not evade their size-dependent bound.

The barrier b'=2A b^(D+1), b(0)=2B gives a strict inward inequality at
the first contact with |q_H|=b^s(H). It applies simultaneously to every
coordinate of each finite cutoff. The target is only used to choose
finite initial/true-diagram bounds; realizability of the approximate
moments is not assumed. The separate clock estimate bounds L from above
and below. At each fixed K the resulting bounded state lies in a compact
subset of L>0, proving continuation through the stated short interval.
No cutoff-independent finite-dimensional Lipschitz constant is needed.

### The dependency-distance error estimate

After dividing a row of size s(H) by R^s(H), telescoping a monomial
difference costs at most R^delta_tot times a fixed number of factor
errors. The coefficient differences are controlled by output and clock
errors, because the norm defining rho is Lipschitz even at zero. The
O(s(H)) product-rule factor therefore gives the claimed bound C m
E_(m+delta). This estimate applies to the complete exact row whenever
m+delta<=K, so the low-row comparison contains no omitted source at that
stage.

The r-fold integral iteration is valid with
r=floor((K-m)/delta): its final level is retained, and all previous rows
are unaffected by deletion. The ordered integration simplex contributes
t^r/r!, while successive row bounds contribute
product_(j=0)^(r-1)(m+j delta). Bounding m by
delta ceil(m/delta) gives exactly the geometric factor times the binomial
polynomial written in equation (10) of the positive report. Initial
errors vanish, and the terminal weighted errors are bounded by two on
the majorant box. Thus the advertised uniform short-time convergence of
each fixed output follows for the actual specified compiler, not only
for a generic moment hierarchy or its initial derivatives.

Under the additional full-horizon exponential envelope, the same bound
holds with a common constant on [0,T]. The positive report's two-limit
argument is legitimate: at a proof-interval boundary, first fix the finite
iteration depth r and send K to infinity, using convergence of finitely
many fixed coordinates; then send r to infinity to remove the terminal
geometric bound. A finite number of intervals covers T. These are
comparison intervals, not restarts of the running scalar ODE and not
injections of target moments.

This positive result refines the initial status table above: the actual
neural deletion rule now has an internally checked fixed-n, fixed-P
short-time convergence theorem. Convergence on every prescribed finite
T remains open. There is no conflict with the bounded counterexample in
sections 2--3: that example also admits a short-time envelope, but no
uniform envelope through a horizon beyond its accumulating blow-up time.
Its early loss of high-moment realizability also shows that realizability
preservation is not necessary for the short-time result; a direct weighted
bound can suffice.

## 8. Collaborative audit of the saturated variant and explicit cutoff

A further explicit supervisor assignment authorized this audit of the
new saturated closure. I read the complete updated
`SCALAR_COMPRESSION_BOUND_ASSESSMENT.md`, first at the intermediate
SHA-256 `eb3698b08f07ca804a165f12e513a975fe6c66e94bd9a783edbe69ead66f78bc`,
then again in full at the final candidate SHA-256
`e80540f9052049ee6e805037af99a57a83aa9acd0d98a3ff1f42d2ff39cd5309`.
The verdict below applies to the latter complete candidate, including its
section 9 equations (18)--(25). I did not read another route's saturation
audit. This is a collaborative post-freeze check, not an independent
promotion review. No experiment, implementation or Git operation was used.

**Internal verdict: PASS.** For every fixed finite n, P, initialization,
data/query list and T, the defined saturated scalar closure has global
existence at every finite cutoff and converges uniformly on [0,T] to the
named fixed-P outputs. The explicit cutoff certificate is valid. This
establishes a theorem for a changed scalar vector field. It neither proves
arbitrary-horizon convergence of the original unsaturated zero-tail solver
nor gives width-uniform accuracy, a small state count or practical
efficiency.

### Saturation, existence and consistency

The essential admissible input is a proved bound B_T on the true primitive
species and initialized entries over the prescribed horizon. The parent
old-clock tanh theorem provides such finite bounds from the initial data.
Bounding products in the normalized contraction then gives
|q_H(t)|<=B_T^s(H) for all true diagrams. This uses an analytic upper bound;
it does not require evaluating the unknown trajectory to choose thresholds.

Choose R>=B_T and clip each coordinate to [-R^s(H),R^s(H)] inside every
evaluation of the finite generator. Clipped output coordinates must also
be used in the residual, rho and clock equation, exactly as specified in
the candidate. The reported clipped output then agrees with the output
used for feedback. The clipping map is 1-Lipschitz and does not mix
coordinates, so it preserves both local well-posedness and the generator's
dependency structure. The proof never differentiates the clipping map.

The actual old-clock primitive templates involve only nonpositive powers
of L: raw moment transport uses L^-1, reconstruction uses L^-1, and its
derivative adds L^-2 together with rho. Further finite substitutions and
matrix actions preserve this property. Thus the stated absolute generator
bound on L>=1 applies to clipped inputs. Since the output clipping bounds
rho, L starts at one and remains finite on each finite interval. Every
fixed coordinate z_H has the global derivative bound
A s(H)R^(s(H)+D). At fixed K no finite-time state blow-up or approach to
L=0 is possible, so the finite locally Lipschitz ODE extends for all time.
This is a global existence statement, not accuracy beyond the horizon used
to choose the thresholds.

Integrating the derivative bound gives, with c=AT R^D and h=s(H),

    |z_H(t)|<=R^h(1+c h)<=[R(1+c)]^h,   0<=t<=T.

The inequality holds for every integer h>=1 by the binomial expansion.
It provides the common envelope R_T=R(1+AT R^D), independent of K, for
the raw evolving coordinates. Static coordinates are already inside
their clipping thresholds and have zero velocity. No assertion that the
raw z_H remain inside the smaller clipping box is needed or made.

For a true target coordinate, S_H(q_H)=q_H throughout [0,T]. Therefore
saturation contributes zero additional velocity defect on the target.
The inequality |S_H(z_H)-q_H|<=|z_H-q_H| holds also when the target is
exactly at a threshold. Hence the interior-row comparison uses the same
weighted raw error and the same dependency increment as before. Its
telescoping estimate remains uniform in K. The clock comparison is
controlled by the clipped output differences through the Lipschitz norm
formula for rho. The envelope above bounds all normalized errors by two.
These facts establish every hypothesis of the conditional continuation
argument; that argument now becomes unconditional for this modified ODE.

### Check of the explicit grade-halving bound

Write C_T for the common row-comparison constant, delta for the positive
integer dependency increment, and set

    N=max(1,ceil(16 C_T delta T)),
    a=ceil(3/delta),
    J=floor(K/(delta 2^N)).

For C_T>0, intervals of length h=T/N have
lambda=C_T delta h<=1/16. Set x_k=E_(delta k) for integer k>=a; then
the row comparison has coefficients k lambda after integration. Suppose
at one interval's beginning all levels a<=k<=J0 have error at most
epsilon. For a<=k<=J1=floor(J0/2), take r=J0-k. These inequalities imply
r>=1 whenever J1>=a, and every row used by the r-fold substitution has
its dependency level within the retained set. It gives

    sup x_k <= epsilon sum_(i=0)^(r-1)
                         binomial(k+i-1,i) lambda^i
               +2 binomial(J0-1,r) lambda^r.

The initial-data factor is at most (1-lambda)^-k, by multiplying k
geometric series. The remainder is at most
2*2^J0*(1/16)^(J0-k). Since k<=J0/2, this is at most
2*2^-J0<=2*4^-J1, including odd J0. Also
(1-lambda)^-k<=(16/15)^J1. If the previous interval supplied
epsilon=2(j-1)4^-J0, then J0>=2J1 and 16/15<4 imply

    epsilon(16/15)^J1<=2(j-1)4^-J1.

Consequently interval j has error at most 2j4^-J1 on its newly controlled
levels. Starting from exact initialization and J0=floor(K/delta), repeated
integer halving gives exactly
floor(K/(delta 2^j)); nesting the floors introduces no extra loss. If the
last cutoff J is at least a, every previous controlled cutoff also is.
The intermediate bounds are at most 2N4^-J, so the estimate is uniform
over the entire horizon, not merely at its final endpoint.

Finally E_3<=E_(delta a), and the physical output coordinate has weight
R_T^3. Clipping cannot increase its error. Thus the candidate's certificate

    max_a sup_(t<=T)|S_f(z_f^K(t))-f_(P,a)(t)|
       <=2N R_T^3 4^-J

is valid under J>=a. The sufficient choice

    K>=delta 2^N max(a,ceil(log_4(2N R_T^3/epsilon)))

both guarantees that grade condition and gives the requested positive
tolerance epsilon. In particular, the maximum with a prevents a negative
or zero cutoff when the tolerance is large. For smaller cutoffs K>=3,
the separately stated trivial bound 2R_T^3 is valid. At T=0 initialization
gives zero error directly. A positive upper bound C_T may always be chosen;
if a zero comparison constant is used, the interior recursion already
gives zero error for the sufficiently inclusive cutoffs in the certificate.

### Updated research status and limits

The report's original obstruction survives unchanged for unsaturated
zero-tail deletion. Its explicit polynomial solution no longer describes
the modified closure once clipping is active, so it does not contradict
the repaired theorem. This is an example of a valid witness repair, not
a retrospective proof of the earlier witness.

The result establishes arbitrary prescribed finite-horizon approximation
at fixed finite width with thresholds and sufficient K allowed to depend
on that width, P, T, data and initialization. Combining it with the already
proved parent P approximation, in the stated order of first choosing P and
then K, gives a finite scalar approximation to the named dense outputs.
The constants and state count can be very large. No efficient compression,
finite population limit, width-independent tolerance certificate,
all-time-uniform approximation or numerical performance result follows.
The candidate makes these distinctions explicit and does not claim them.
