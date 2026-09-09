# Shifted softplus: local exact-GD/GF and observable bridge

Root candidate, 2026-09-06. This is a LOCAL modular theorem, not the
requested all-finite-time theorem. No experiment or external theorem is
used. Its explicitly imported mathematical dependencies, all in this
directory, are:

- SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md,
  398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d;
- SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md,
  875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603;
- SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md,
  51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f;
- SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md,
  0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b.

The assembly imports the latter three; listing all four makes the
modular boundary explicit. No claim about their proof provenance is a
substitute for their hypotheses. Their precise interfaces used below
are stated in Section 2. Nontriviality is not reproved or imported here.

## 1. Exact finite model and conclusion

Fix d and two inputs x_a with ||x_a||_2^2/d=1. Put
C_ab=x_a^T x_b/d, C_12=rho in [-1,1), and y_a in {-1,1}.
All three hidden layers use the same fixed activation

    phi(z)=1+(1/10)log(1+exp(z)).

It satisfies |phi(z)|<=2+|z|/10, 0<phi'(z)<1/10,
and 0<phi''(z)<=1/40. Width is n in each hidden layer.
Initialize W^(1) entries independently N(0,1/d), W^(2), W^(3)
entries independently N(0,1/n), and RESCALED W^(4) entries independently
N(0,n^-2); these four arrays are mutually independent. For a=1,2 set

    z^(1)_a=W^(1)x_a, h^(ell)_a=phi(z^(ell)_a),
    z^(2)_a=W^(2)h^(1)_a, z^(3)_a=W^(3)h^(2)_a,
    f_a=(W^(4))^T h^(3)_a/n, r_a=f_a-y_a,
    L=r_1^2+r_2^2,
    delta^(3)_a=W^(4) phi'(z^(3)_a),
    q^(2)_a=(W^(3))^T delta^(3)_a,
    delta^(2)_a=phi'(z^(2)_a)q^(2)_a,
    q^(1)_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=phi'(z^(1)_a)q^(1)_a.

Products in the delta formulas are coordinatewise. There is no residual
inside any delta. Exact raw GD with eta_n=n^-2 is

    W^(1)+=W^(1)-(2 eta_n/d)sum_a r_a delta^(1)_a x_a^T,
    W^(ell)+=W^(ell)-(2 eta_n/n)sum_a r_a delta^(ell)_a
                                            (h^(ell-1)_a)^T, ell=2,3,
    W^(4)+=W^(4)-2 eta_n sum_a r_a h^(3)_a.             (1)

Finite GF uses the increments in (1) divided by eta_n as its velocity.
Raw GD is linearly interpolated; all hidden quantities are recomputed
from these interpolated raw parameters. Velocities are right derivatives
at interior mesh nodes and left derivatives at an observed terminal
mesh node.

For a finite raw difference use the sum of its first input-span norm,
two ordinary matrix Frobenius norms, and readout norm divided by sqrt(n).
The first squared norm is the empirical average of v^T C^-1 v when
|rho|<1, and the empirical average of v^2 for the realizable pair (v,-v)
when rho=-1. It equals d||Delta W^(1)||_F^2/n on input-span increments.
The frozen perpendicular block is coupled identically and ignored. The
sum norm and corresponding squared-sum Hilbert norm are equivalent with
absolute constants. Population versions replace empirical averages by
expectations on their OWN separate neuron spaces, and matrix increment
norms by Hilbert--Schmidt norms.

Let S_* be the positive feature interval supplied by the assembly, with
S_*<=1/196. Set T_*=S_*/4. On [0,T_*], both exact GD and finite GF
converge, jointly and along the full width sequence in probability, to
the assembly's uncut physical population path. This includes:

- predictions, loss, the four raw 2-by-2 kernel blocks in (10) below;
- joint same-neuron two-sample current forward and backward fields;
- both directions of both hidden matrices on any fixed admissible finite
  probe program: coordinate maps globally Lipschitz with bounded first
  derivatives, linear combinations, matrix/adjoint applications, and
  finitely many within-population quadratic contractions;
- hidden preactivation/feature velocities and their squared norms and
  time integrals; joint two-sample hidden path laws in W_2(C([0,T_*])).

Current-field/velocity/probe empirical laws use every fixed continuous
test of at most quadratic growth, equivalently the corresponding finite
tuple W_2 law. Their convergence is uniform in physical time for current
programs and holds jointly at any finite set of times. Arbitrary
unbounded nonlinear probe instructions are NOT covered by the phrase
admissible. The explicitly named uncut backward and velocity formulas
are covered by the additional arguments below.

The GD and GF paths, coupled by their identical initialization, also
have vanishing same-width raw distance uniformly on this interval.
No operator-norm convergence between different population spaces is
asserted. Unique restart is only on the remaining local interval, as
provided by the assembly; no extension past it is claimed.

## 2. Imported local interfaces and fixed-cap finite references

The assembly gives separate common spaces, fixed initial operators and
true adjoints, and a C1 uncut raw population feature path Theta(s),
0<=s<=S_*. It gives nested smooth contracting caps tau_R, equal to the
identity on [-R,R], bounded by 2R, with |tau_R(u)|<=|u|. The analytical
three-cut feature equations cap the readout only INSIDE delta^(3), the
query q^(2) only INSIDE delta^(2), and q^(1) only INSIDE delta^(1).
The actual readout update still uses the uncut H^(3). Feature coefficients
are y_a/2 in all four raw blocks; the first block also includes C.
Write Theta_R for these zero-readout references. The imported results give

    sup_(s<=S_*) [d(Theta_R(s),Theta(s))
                +||Theta_R'(s)-Theta'(s)||_raw]
                        <= C exp(-c R^2),             (2)

after decreasing c and increasing C if necessary. The same rate holds
for named forward/backward fields. The old cut-defect norms obey

    sup_(s<=S_*) sum_(v=W4,q1_a,q2_a)
           ||v_R(s)-tau_R(v_R(s))||_2
                        <= C exp(-c R^2).             (3)

All reference primal RMS/operator bounds are uniform in R. The imported
asymmetric comparison uses OLD cap radius R with coefficient C(1+R)
on any fixed primal ball, even when the NEW field is wholly uncut.
Its additional terms are the OLD defects in (3), not new-path tails.
The same comparison holds at finite width with normalized vector norms
and ordinary matrix increment norms. It also bounds differences of each
named backward query and delta by C(1+R)d plus old defects. Prediction
differences cost only C d on such a ball. No R^2 coefficient is needed.

The assembly gives symmetry f_a(s)=y_a g(s), with
0<=g<=1/4, g(0)=0, and g' continuous and bounded. Define s(t) by

    s'(t)=4(1-g(s(t))), s(0)=0.                       (4)

On the local range 3<=s'<=4, so s(t)<=S_* for 0<=t<=T_*.
Moreover s''=-4g'(s)s' is continuous and bounded. The uncut physical
population path is Theta(s(t)). These statements do NOT assert sample
symmetry or a scalar residual clock for a finite realization.

At width n let Theta_(n,R)(s) be the three-cut zero-readout feature flow,
coupled to the same initial first fields and W^(2),W^(3) as the actual
paths. With probability tending to one the initial marginal RMS norms
are at most 2 and both matrix operator norms at most 10. The imported
deterministic primal theorem gives these feature references on [0,S_*]
in one fixed primal ball, uniformly in n,R. At fixed R their vector
field has a width-uniform local Lipschitz bound C_R on that ball:
apply the old-cut comparison with equal caps, so its defects vanish.
Their raw velocities and named query time-Lipschitz constants in RMS
are width-uniform at fixed R. For queries this also follows directly
by differentiating or differencing the bounded-cut coordinate maps and
the bounded current operators; no uncut-query multiplier is introduced.

For completeness, their finite-width limit is obtained in the required
order. For a FIXED feature mesh and R, exact Euler evaluation is a
fixed finite Gaussian program with admissible bounded-derivative maps.
The imported fixed-program theorem identifies all same-neuron joint
empirical polynomial-growth tests, including both orientations of both
matrices and all within-population contractions. The constant-R raw
Lipschitz estimate and uniform primal/velocity bounds give O_R(mesh)
Euler error up to a fixed larger-ball stopping boundary; the strict
primal margin removes that stopping. One then sends the feature mesh
to zero, at fixed R, on the common population spaces and at finite
width. This proves finite-reference current tuple W_2 convergence.
The elementary grid/product argument in Section 4 supplies uniform
time and velocity variants when a recomputed hidden velocity includes
a bounded gate times an unbounded L2 field.

In particular, writing e_(n,R) for the sum of OLD defect RMS norms,
the contraction of u->u-tau_R(u) and the fixed-R query time modulus give

    sup_(s<=S_*) e_(n,R)(s)
       <= C exp(-c R^2)+o_probability(1),              (5)

where the width limit is at fixed R. Indeed each defect norm is
Lipschitz as a function of its query in RMS; apply finite-grid W_2
convergence and then its time modulus. Fixed-R predictions likewise
converge uniformly. Combining with (2),

    sup_(t<=T_*) |f_(n,R,a)(s(t))-y_a g(s(t))|
       <= C exp(-c R^2)+o_probability(1).              (6)

## 3. Exact physical GD/GF comparison, including the off-label mode

Use B_(n,R)(t)=Theta_(n,R)(s(t)) as a comparison path. Its derivative
is s'(t) times the feature cut field, so its sample coefficients are
2y_a(1-g(s(t))). The actual physical coefficients are -2r_(n,a).
Their difference is exactly

    -2[f_(n,a)-y_a g(s(t))].

Split this as actual-minus-reference prediction plus (6). The first
term is bounded by C d(actual,B_(n,R)); the second includes both
finite residual modes, and is not set to zero by symmetry. The old-cut
asymmetric comparison therefore bounds the raw velocity discrepancy by

    C(1+R)d(actual,B_(n,R))
       +C e_(n,R)(s(t))
       +C sum_a |f_(n,R,a)(s(t))-y_a g(s(t))|.         (7)

The bound is valid on any fixed common primal ball. Initial distance is
||W^(4)_0||_2/sqrt(n)=O_probability(n^-1); all hidden initial blocks agree.
For finite GF integrate (7) and apply the elementary integral Gronwall
inequality. Finite GF is locally smooth. Its global finite-dimensional
existence also follows separately from dL/dt=-||grad_raw L||_raw^2:
on each finite horizon the raw distance to initialization is at most
sqrt(T L(0)); linear activation growth and bounded gates then bound its
raw velocity, ruling out finite-dimensional escape.

For GD there is no coordinate-change approximation: (1) is EXACT raw
Euler. On the reference ball the defect of B_(n,R) over any eta_n step
is at most C_R eta_n^2. To see this, its derivative is s'F_R(B), where
s' is Lipschitz, F_R is Lipschitz on the ball, and B has bounded raw
velocity. Integrate the Lipschitz derivative over the step. Discrete
Gronwall, (5)--(7), and eta_n=n^-2 give, for either dynamics,

    sup_(nodes t<=T_*) d(actual(t),B_(n,R)(t))
       <= exp(C(1+R)T_*)
          [O_probability(n^-1)+C_R eta_n
                        +C exp(-c R^2)+o_probability(1)].             (8)

For GF omit C_R eta_n and use every time. Every probability remainder
is taken with R FIXED. Taking n to infinity first and R to infinity
second makes the right side vanish. Substituting (8) into (7) also
makes raw velocity errors vanish in the same iterated order.

There is no unproved actual-path primal assumption in this use of (7).
Stop the actual path at the first exit from a primal ball whose norms
exceed all reference bounds by a fixed margin. Before exit, linear
growth of phi, bounded phi', the two operator bounds and readout RMS
bound control every forward/backward RMS norm, residual, and raw
velocity by a constant independent of width and R. A GD step has raw
length at most C eta_n, so its first exit node has at most that
overshoot. The same estimate (8), using a slightly larger fixed ball,
holds through that node. Choose a fixed sufficiently large R so the
surviving deterministic bound in (8) is smaller than one quarter of
the margin, and then let n grow. With probability tending to one no
exit is possible. GF uses the continuous stopping version. Frozen
first-weight directions never enter this argument.

Within a GD step all raw changes have norm O(eta_n), hence every
preactivation changes by O(eta_n) in RMS and by O(eta_n sqrt(n))
coordinatewise, using the bounded primal norms. Thus raw interpolation
has the same state conclusion. Named backward discrepancies follow
from the backward portion of the same comparison at nodes, and from
the product estimates of Section 4 for interpolated states.

## 4. Observation and velocity transfer without assuming iid reuse

At any fixed number of reference mesh times, the identification theorem
gives joint empirical averages after every matrix reuse. Independence
is used only in that theorem's explicit conditional Gaussian residuals,
not for finite trained coordinates. New reused outputs consist of the
response forced by preceding uses plus unexplored Gaussian randomness.
All pairings below are within one neuron population.

Here is the elementary product bridge needed in several places. If
X_n-Y_n has vanishing RMS, B_n-D_n is bounded and converges in empirical
probability, and the squared tails of Y_n are uniformly integrable,
then B_n X_n-D_n Y_n has vanishing RMS, provided B_n,D_n have a common
bound. Split at |Y_n|<=A; the bounded part is controlled by convergence
in empirical probability, and the remainder by the squared tail.
The identical statement holds on each population space. For fixed-R
reference data at a finite time grid, all finite moments from the
fixed-program theorem provide these tails. For reference curves,
approximate by a finite grid in L2; proximity to finitely many uniformly
integrable squared fields makes the whole family's squares uniformly
integrable. For example, using |Y|>A and |Y-X|<=A/2 gives |X|>A/2,
and one obtains a bound by C||Y-X||_2^2 plus a tail of X.

Ordinary admissible finite probes transfer by induction using bounded
matrix operator norms, the raw increment comparison and global
Lipschitzness of their coordinate instructions. Within-population
quadratic contractions transfer by Cauchy--Schwarz. The named uncut
backward fields are controlled by (7) and its backward comparison,
not by pretending their uncut coordinate instructions are Lipschitz.

To make velocity transfer explicit, at a raw state with raw velocity V
the recomputed finite hidden preactivation velocities are

    dot z^(1)_a=V^(1)x_a,
    dot z^(2)_a=V^(2)h^(1)_a
                          +W^(2)[phi'(z^(1)_a)dot z^(1)_a],
    dot z^(3)_a=V^(3)h^(2)_a
                          +W^(3)[phi'(z^(2)_a)dot z^(2)_a],
    dot h^(ell)_a=phi'(z^(ell)_a)dot z^(ell)_a.          (9)

Their RMS norms are bounded by C||V||_raw on a fixed primal ball.
For a fixed-cap Euler reference on a fixed coarse mesh, (9) needs one
extra truncation argument; an uncut product cannot simply be declared
an admissible instruction before applying the next matrix. At layer
one the velocity is a finite sum of bounded cut deltas, multiplied by
scalar coefficients. Localize those scalar coefficients in a fixed
bounded set (their limits and the primal bounds permit this). Thus
phi'(z^(1))dot z^(1) is an admissible bounded-derivative instruction,
using a smooth cap on the velocity argument larger than its bound.
The layer-two velocity is now identified by an admissible matrix
query and finite contractions, with all fixed empirical moments.
The uncut field phi'(z^(2))dot z^(2) is identified as a continuous
polynomial-growth test of that tuple, so its squared tails are known.
Before querying W^(3), cap dot z^(2) at an additional fixed level A.
The input error in RMS is at most (1/10) times the squared-tail norm
of dot z^(2), and the query error is at most the current operator norm
times this input error. The capped program is admissible. At fixed
coarse mesh and R, send width to infinity and then A to infinity;
the same L2 truncation works on the actual common population spaces.
This identifies the true uncapped layer-three velocity in W_2 and
gives squared-tail control by proximity to its capped versions.
Multiplication by the last bounded gate then identifies the last
feature velocity. This argument requires no whole-space Lp estimate
for an initial matrix and no moment beyond L2 for the final uncapped
matrix output. It also works jointly at the finitely many coarse
times and with the already identified forward/backward tuple.

At fixed R, coarse Euler raw states and velocities approximate the
exact reference in raw norm uniformly in n. Apply the product bridge
to the finite coarse-grid old velocity fields in (9), layer by layer,
to obtain uniform RMS convergence of the recomputed velocities as
the coarse mesh is removed. This also establishes the reference
velocity family's squared-tail control, including uniform time
continuity in the same RMS/product sense. Then (8), (7), the same
product bridge, and the population limit (2) transfer (9) to actual
GF and GD node velocities. Limits are always taken in this order:
width at fixed R/coarse mesh, coarse mesh to zero, then R to infinity.

For GD between nodes, the raw velocity V is constant on the step and
bounded in raw norm. In (9), first-layer velocity is constant, and
first-layer gate change has supremum O(eta_n sqrt(n)). The second
velocity changes by O(eta_n sqrt(n)) in RMS by its product formula;
its gate has the same supremum-change bound because its preactivation
changes by O(eta_n) in RMS. Repeating at layer three proves this bound
for every recomputed hidden velocity. Here features need only bounded
RMS, not bounded coordinate values. The error is
O(eta_n sqrt(n))=O(n^-3/2). The same node comparison can be applied to
the preceding node at a terminal time; continuity of the limiting
velocity removes the distinction between terminal-left and right
interior conventions.

The raw kernel entries are exactly

    K^(1)_ab=C_ab (delta^(1)_a)^T delta^(1)_b/n,
    K^(ell)_ab=[(delta^(ell)_a)^T delta^(ell)_b/n]
                      [(h^(ell-1)_a)^T h^(ell-1)_b/n], ell=2,3,
    K^(4)_ab=(h^(3)_a)^T h^(3)_b/n.                    (10)

Their population limits replace each empirical pairing by its
within-population expectation. All factors converge by the named
field comparisons and quadratic-test convergence, uniformly in time.
Predictions and loss follow by the same argument and bounded primal
norms. The raw chain rule, summing the four gradient contributions,
gives dot f_a=-2 sum_b(sum_(ell=1)^4 K^(ell)_ab)r_b in population;
the curvewise chain rule needed for this is already justified by the
assembly, not an L2 Frechet-differentiability assertion for phi.

Uniform RMS velocity comparisons, fixed-reference squared-tail control,
and bounded norms also give convergence of integrated squared velocities:
| ||u||_2^2-||v||_2^2 |<=||u-v||_2(||u||_2+||v||_2).
Apply this in empirical average and then integrate time. Current tuple
tests transfer from W_2 convergence using truncation and compact-set
uniform continuity. Uniform-time versions follow from the reference
time moduli and the uniform RMS comparisons just proved.

Finally, for an absolutely continuous scalar path z and its linear
interpolant I_pi z on a time mesh pi, Cauchy--Schwarz on each cell gives

    ||z-I_pi z||_infinity^2
                  <=4|pi| integral_0^T |dot z(t)|^2 dt.

Average this inequality over neurons and apply its population version.
The right sides are uniformly bounded by the raw velocity/primal
estimates and (9). On a fixed time mesh, joint W_2 laws already
converge; linear interpolation is a Lipschitz map from the finite
tuple into the supremum-norm path space. The triangle inequality and
then |pi|->0 give W_2(C([0,T_*])) convergence. The proof applies to
the pair of sample paths together and to features, either through
(9) or Lipschitzness of phi. No path-law claim for time derivatives
themselves, or for unproved derivatives of the reverse queries, is made.

Both actual dynamics were compared with the same finite reference.
Their joint full-sequence limits and same-width closeness follow by
the triangle inequality. This completes only the stated local bridge;
it supplies no global tail bound or continuation beyond T_*.
