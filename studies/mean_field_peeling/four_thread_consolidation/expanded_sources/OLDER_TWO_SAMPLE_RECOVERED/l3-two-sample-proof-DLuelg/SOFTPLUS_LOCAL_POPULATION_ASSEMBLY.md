# Local uncut softplus population construction and energy bridge

Root candidate, 2026-09-06. UNREVIEWED modular proof, NOT the global
two-label theorem and NOT the final self-contained deliverable. It
imports three explicitly identified local lemmas. The finite-program
and primal/comparison candidates are still under their first isolated
reviews when this assembly is written. Their status must be reconciled
before this assembly is promoted.

Dependencies, all read in full by the root:

- SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md, SHA256
  875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603.
  Used for fixed finite programs, both initial actions/adjoints,
  joint empirical continuous polynomial-growth tests, and singular Grams.
- SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md, SHA256
  51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f.
  Used for the primal box on S<=1/10, exact Euler forward increments,
  and local asymmetric comparison with a coefficient linear in the
  old output ceilings. Its population version is conditional on supplied
  bounded initial operators; those operators are constructed here.
- SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md, SHA256
  0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b.
  Used for its conditional finite-law response and Gaussian tails on
  S<=S_0, including its strictly positive deterministic S_0. Its full
  409-line first isolated review found no required corrections; the
  primal and finite-law premises of that lemma are discharged below.

The fixed activation is phi(z)=1+0.1 log(1+exp z). Write e=0.1 and
c=0.025, so 1<=phi(z)<=2+e|z|, |phi'|<=e, |phi''|<=c. Neuron
populations remain separate. Transposes of finite matrices are ^T;
population adjoints are ^*. The initial readout in this construction
is zero; comparison to the small canonical finite-width readout is
an additional obligation not claimed here.

## 1. Local claim and state geometry

Fix rho in [-1,1) and labels y_a in {-1,1}. Let
C=[[1,rho],[rho,1]]. For |rho|<1 the first state is the pair
Z^(1)=(Z^(1)_1,Z^(1)_2), with first-field norm

    ||v||_first^2=E_1[v^T C^(-1)v].                    (1)

At rho=-1 use one field Z^(1), with pair (Z^(1),-Z^(1)) and
norm ||v||_first^2=E_1 v^2. This is the raw metric on the input
span, or equivalently the quotient by the frozen directions invisible
to the two inputs. Indeed if e_a=x_a/sqrt(d) are unit vectors with
Gram C, the minimum-norm raw increment inducing pair v has squared
norm v^T C^(-1)v. At the rank-one endpoint this reduces to v^2.
The canonical raw first-weight metric d||dW^(1)||_F^2/n becomes
exactly (1) on those directions. In particular

    ||v_a||_2<=||v||_first,
    ||(1/2)C(y_1d_1,y_2d_2)^T||_first
                         <=(1/2)(||d_1||_2+||d_2||_2). (2)

The first inequality is Cauchy--Schwarz in the C^(-1) metric with
C_aa=1; the second follows by representing the gradient increment
as (y_1 d_1 e_1+y_2 d_2 e_2)/2. Both hold at the rank-one endpoint
in its reduced representation.

The other state components are W^(2), W^(3), and W^(4). The first
two are fixed bounded initial operators plus Hilbert--Schmidt
increments. State distance is the SUM of (1), the two HS norms of
increment differences, and the L2 readout norm. The associated raw
Hilbert norm instead takes the square root of the sum of squares.
These norms are equivalent with constants between one and two.

Claim, conditional only on the three proved dependency lemmas:
there is S_*>0 independent of rho and labels, and fixed probability
spaces Omega_1,Omega_2,Omega_3 with bounded initial operators and
their genuine adjoints, on which a unique regular uncut feature path
exists for 0<=s<=S_*. Its state consists of the above four components,
not a growing list of time slots. It solves the autonomous equations

    H^(ell)_a=phi(Z^(ell)_a),
    Z^(2)_a=W^(2)H^(1)_a,   Z^(3)_a=W^(3)H^(2)_a,
    delta^(3)_a=W^(4)phi'(Z^(3)_a),
    q^(2)_a=(W^(3))^*delta^(3)_a,
    delta^(2)_a=phi'(Z^(2)_a)q^(2)_a,
    q^(1)_a=(W^(2))^*delta^(2)_a,
    delta^(1)_a=phi'(Z^(1)_a)q^(1)_a,

    (Z^(1)_b)'=(1/2)sum_a C_ba y_a delta^(1)_a,
    (W^(ell))'=(1/2)sum_a y_a delta^(ell)_a tensor H^(ell-1)_a,
                                                       ell=2,3,
    (W^(4))'=(1/2)sum_a y_a H^(3)_a.                  (3)

Here (u tensor v)h=u E[vh]. The population initial first pair is
Gaussian with covariance C; the initial operators are the common-space
limits of the prescribed two independent Gaussian matrices. W4(0)=0.
Regular means continuously differentiable in first/readout L2 and in
the HS increments, with all forward/reverse fields as in (3).

Uniqueness is among regular solutions on these SAME spaces/operators,
or absolutely continuous solutions satisfying the integral equations
and continuous state paths. No competing solution is required to have
Gaussian tails. The path can be restarted uniquely at an interior
time for its remaining portion of this local interval. Existence
past S_* is NOT asserted by this restart statement.

Let f_a=E_3[W4 H3_a], g=(1/2)sum_a y_a f_a. The constructed path
has sample symmetry, f_a=y_a g, and

    g'=||theta'||_raw^2,       0<=g(s)<=1/4.            (4)

The two actual reverse queries and readout have uniform Gaussian-square
moments at each time on this interval. These conclusions supply the
EXISTING-PATH, energy and symmetry hypotheses of the softplus curvature
action notes on this interval only. Raw GD, full observable convergence,
every-time nonlazy learning, and global opposite-label continuation
are not part of this local claim.

## 2. Construct the initial actions on a common generated space

Fix rho. Take a countable collection of finite query programs closed
under finite unions, rational linear combinations, constants in each
population, the root Gaussian pair, both orientations of both initial
matrices, and the globally Lipschitz C1 coordinate maps used below.
Include phi and phi', the capped product maps, and a countable family
of smooth bounded Lipschitz functions dense on compact subsets of
every finite-dimensional coordinate space. Such a family is obtained
by approximating continuous functions on finite rational grids by
piecewise linear functions and smoothing at rational scales. Include
all finite rational-step reference Euler programs and integer caps.
Auxiliary query noise used to prove the identification lemma is removed;
it is not an additional input to the network.

The identification lemma supplies the joint law in each population
of every finite union of these programs. These laws are consistent
because they are limits of the same finite-width calculations. The
countable probability extension principle gives one probability space
Omega_ell for each population carrying its countable coordinate slots.
Equivalently successively sample the conditional distribution of each
additional real slot given the preceding slots; consistent finite
marginals give the specified laws. The sigma field is generated by
these slots, completed under their probability law.

The linear span of the generated functions is dense in L2(Omega_ell).
To see this, approximate a square-integrable function by bounded
functions of finitely many generating slots, using conditional
expectations on the increasing finite-slot sigma fields. This elementary
projection convergence follows by first approximating indicators in
the sigma field generated by the union and then simple functions.
For a finite Borel law, a bounded measurable function can be approximated
in L2 by bounded continuous functions: approximate each indicator
between a compact subset and an open superset and use a continuous
distance cutoff. Approximate the continuous function on a compact set
by the included countable smooth family. Its complement has arbitrarily
small measure. This proves the density assertion.

The elementary Gaussian matrix norm estimate in the identification
lemma gives P{||W^(ell)_0||_op<=10}->1. For a fixed rational linear
combination U of generated inputs, pass the finite inequality

    ||W^(ell)_0 U_n||_2/sqrt(n)
                           <=10||U_n||_2/sqrt(n)

to the deterministic limiting second moments. It gives

    ||W^(ell)_0 U||_{L2(Omega_ell)}
                            <=10||U||_{L2(Omega_(ell-1))}. (5)

Generated linearity and this inequality imply that an L2-zero input
has an L2-zero output, even if presented by a different program.
Therefore the action is well defined on equivalence classes. Density
extends it uniquely to a bounded linear operator of norm at most 10.
Construct the reverse action in the same manner. Passing the exact
finite transpose pairing through the joint second-moment law yields

    E_ell[V W^(ell)_0 U]
                   =E_(ell-1)[U (W^(ell)_0)^* V].       (6)

Density extends (6) to all L2 arguments. This proves that the reverse
action is the adjoint, not a resampled independent action. The two
different neuron spaces and both trained operator directions remain
distinct. Joint empirical laws within each population are used; there
is no assertion that reused finite neurons are iid.

Real coefficients and real finite step sizes follow by approximation
from rational coefficients, propagating errors through a fixed number
of Lipschitz coordinate maps and the bounded operators (5). Thus all
finite references needed below live on these same spaces. The laws of
the full initial actions, not just their current two-sample Grams,
are retained by this construction.

## 3. Fixed caps and discharge of the primal hypotheses

For definiteness choose ONE nested smooth family with identity radius R
and output ceiling at most 2R. Here is an explicit construction. Put
a(u)=exp(-1/u) for u>0 and a(u)=0 for u<=0, and for t>=0 define

    chi(t)=a(2-t)/(a(2-t)+a(t-1)),
    psi(t)=integral_0^t chi(v)dv.

The denominator is positive. The function chi equals one on [0,1],
zero on [2,infinity), and is nonincreasing between them. Smoothness
at the joining points follows because every fixed derivative of
exp(-1/u) is a polynomial in 1/u times exp(-1/u), tending to zero
as u decreases to zero. Extend psi oddly and put tau_R(x)=R psi(x/R).
Then tau_R is smooth, 0<=tau_R'<=1, identity on [-R,R], and
|tau_R(x)|<=min(|x|,2R). For t>=0,

    psi(t)>=t chi(t),

because chi is nonincreasing. Differentiating R psi(x/R) in R
shows tau_R(x) is nondecreasing in R for x>=0. Oddness therefore gives

    |tau_{R'}(x)-tau_R(x)|<=|x-tau_R(x)|, R'>=R.        (7)

Use this family for the three reference cuts, initially all with
the same radius R. The reference equations are (3) with delta3
replaced by tau_R(W4)phi'(Z3), delta2 by phi'(Z2)tau_R(q2), and
delta1 by phi'(Z1)tau_R(q1). The readout update stays uncut.

The affine state space consisting of the first field, two HS kernels,
and readout is complete. The primal/comparison lemma applies on its
bounded primal subsets, by (2), (5), and the HS rank-one norm identity.
At a fixed finite R it gives local Lipschitz continuity of this vector
field and bounded velocity on slightly enlarged primal balls. The
integral map on continuous paths in a sufficiently small closed ball
is a contraction: its Lipschitz constant is the field constant times
the interval length. The velocity bound keeps that ball invariant.
Geometric convergence of the iterates proves a unique local fixed-cap
solution. No population differentiability theorem is invoked here.

The continuous-time version of the primal lemma gives, through any
existing part of [0,1/10],

    max_a||Z1_a||_2<3,   ||W2||_op,||W3||_op<11,
    ||W4(s)||_2<=7s,
    ||H1_a||_2<=2.3, ||H2_a||_2<=4.53, ||H3_a||_2<=7.   (8)

The two HS increments and first-field displacement also remain bounded
by constant multiples of s^2. Hence the fixed-cap solution can be
continued to 1/10: on an enlarged bounded ball the same finite Lipschitz
and velocity constants give a uniform positive length for each local
extension. The margins in the primal box are strictly positive. This
argument uses no clipped gradient energy identity.

For a fixed R, bounded velocity and Lipschitzness bound the exact
one-step Euler defect by C_R Delta^2. Summing the elementary recursion
d_(k+1)<=(1+C_R Delta)d_k+C_R Delta^2 gives

    sup_(s<=1/10) d(theta_(R,Delta)(s),theta_R(s))
                                                   <=C'_R Delta. (9)

Recomputed forward/reverse fields have the corresponding uniform L2
convergence at fixed R, by the same vector-field product estimates.
Nodal feature interpolation need not equal recomputation inside a raw
step; both differ by at most a fixed velocity constant times Delta.

We next justify using the conditional response lemma without circularity.
For each FIXED finite width program, initialize the first Gaussian pair
and two Gaussian matrices as specified. The event that both first
marginal RMS norms are at most two and both matrix norms at most ten
has probability tending to one. On that event the deterministic
primal/Euler lemma proves every bound (4)--(5) of the response note:
the reverse fields obey 0.7s,7.7s,0.77s as required, and the two
feature time metrics are at most 0.0847 S and 0.5005 S, both below
one for S<=1/10. These estimates hold simultaneously at all nodes of
this fixed mesh and for every choice of caps.

The fixed-program lemma gives convergence of all relevant empirical
second and mixed moments to the scalar law. A deterministic limiting
moment cannot exceed a bound holding with probability tending to one.
Applying this to each field and each pair of time nodes proves all
primal hypotheses (4)--(5) in that scalar law. Its well-definedness
and formal derivative expectations are also provided by identification.
Thus the response lemma now applies unconditionally to the actual
reference laws for S<=S_0. No uniform-in-number-of-queries Gaussian
identification has been assumed: width goes to infinity at a fixed
mesh, and the response estimate is a separate deterministic induction
uniform over those meshes.

For any fixed time s<=S_0 choose mesh nodes tending to s. Equation
(9), continuity of the fixed-cap fields, and Fatou along an almost-
surely convergent L2 subsequence give

    sup_(R>=1, s<=S_0, a) E exp(eta |q^(j)_(R,a)(s)|^2)<=C,
    sup_(R>=1, s<=S_0) E exp(eta |W4_R(s)|^2)<=C, j=1,2. (10)

Use the same constants as the response lemma, weakening the readout
bound from W4/S_0 to W4 if necessary. The statement is uniform over
each time separately; it does not assert continuous scalar query
paths or a bound on their time supremum. The exponential tail argument
at the end of that lemma yields

    sup_s [||W4_R-tau_R(W4_R)||_2
       +sum_(j=1,2) max_a||q^(j)_(R,a)-tau_R(q^(j)_(R,a))||_2]
                                                <=C exp(-c_0R^2). (11)

## 4. Remove the cuts and prove unrestricted local uniqueness

Compare R'>=R references on these same spaces. Their initial states
are identical and their primal norms satisfy (8). The old OUTPUT
ceiling in the comparison lemma is 2R, so its coefficient is bounded
by C(1+R), not C(1+R)^2. Its defects concern only the old actual
reference fields. Nesting (7) and (11), followed by the scalar
integrating-factor inequality, give

    sup_(s<=S_0) d(theta_R'(s),theta_R(s))
        <=CS_0 exp(C(1+R)S_0-c_0R^2)
        <=C_5 exp(-c_5R^2).                            (12)

The final bound follows by completing the square in R and enlarging
the constant. It is uniform in all R'>=R. Completeness gives a
continuous limiting state theta in the same finite list of fields
and operators. Bounds (8) pass to that limit. The full vector-field
comparison, together with (11)--(12), also shows that the reference
velocities are uniformly Cauchy in the state norm. Their limit is
continuous and theta is its time integral, hence theta is C1.

We verify that this limiting velocity is the uncut expression (3).
The needed product-continuity fact is the following: if A(t) is a
continuous L2 curve on a compact interval, B_m(t)->B(t) uniformly
in L2, and h is bounded and Lipschitz, then

    sup_t ||A(t)[h(B_m(t))-h(B(t))]||_2 ->0.            (13)

Indeed the set of values of A is compact in L2, so its square tails
are uniformly small. To prove the latter, use a finite L2 net and
the fact that x -> (|x|-K)_+ is 1-Lipschitz; each net point has a
vanishing tail and the net error is arbitrary. On |A|<=K the product
is bounded by K Lip(h)||B_m-B||_2; on the complement it is bounded
by 2||h||_infinity times the L2 tail. First fix K, then increase it.

Forward states converge by Lipschitzness of phi, bounded operators,
and the rank-one comparison. At the top, (11) and (13), with A=W4
and h=phi', identify the limiting delta3 as W4 phi'(Z3). Bounded
trained adjoints then identify q2. That curve is continuous in L2.
Use (11) and (13) again with A=q2 to identify delta2; then identify
q1 and delta1 in the same order. The first updates, HS rank-one
updates, and readout update therefore converge to exactly (3).
Fatou also transfers (10) to the uncut fields. This proves existence,
the claimed regularity, and the indicated local Gaussian moments.

For uniqueness let another continuous absolutely continuous integral
solution start at the same state and exist on a subinterval of
[0,S_0]. Its state image is compact and thus contained in some bounded
primal ball; the same holds for the references. Apply the asymmetric
comparison with this uncut solution as the NEW state and theta_R as
the OLD state. The comparison lemma permits an identity new cut and
needs no pointwise bound on the new readout/query. Its constant C_ball
may depend on the competing path's bounded primal norms, but not on R.
Its OLD defects are still (11). Gronwall gives

    sup_s d(theta_competitor(s),theta_R(s))
       <=C exp(C_ball(1+R)S_0-c_0R^2) ->0.

This proves equality with theta. A competing integral solution need
not have Gaussian tails or a bounded multiplier on L2. If it starts
at an interior time u with value theta(u), comparison with theta_R
on [u,v] adds only the initial discrepancy from (12), also Gaussian
in R. The same argument proves uniqueness after that restart for
v<=S_0. Existence of that portion is supplied by theta itself; no
existence beyond the original interval is inferred from its endpoint.

## 5. Symmetry, chain rule, and the actual local action premises

Consider first y=(1,sigma), sigma in {-1,1}. At finite width with
zero readout, swap the two initial first-layer fields while retaining
the same two initial matrices. The initial law is invariant under
this operation. The exact reference Euler equations transform as

    Z_a,H_a -> Z_(3-a),H_(3-a),
    W^(2),W^(3) -> W^(2),W^(3),
    W4 -> sigma W4,
    delta_a,q_a -> sigma delta_(3-a),sigma q_(3-a).     (14)

To check the first update use C_ba=C_(3-b),(3-a) and
y_(3-a)=sigma y_a. For each hidden update the factor sigma from
delta cancels the relabeling of y; the readout update acquires sigma.
Oddness of all three cuts is needed for the reverse transformation.
Thus (14) holds inductively, not by presuming a limiting uniqueness
theorem. Initial-pair exchange has the same law even when rho=-1.

The deterministic finite-program limits therefore have equal sample
feature second moments in every population and f_a=sigma f_(3-a).
Fixed-cap mesh convergence and cut removal preserve these statements.
Consequently f_a=y_a g, where g=(f_1+sigma f_2)/2. The two remaining
label vectors are obtained by reversing both signs; W4 and backward
fields reverse sign while the hidden states are unchanged. The same
conclusion holds with g=(1/2)sum_a y_a f_a for every label choice.

For rigor, composition by phi has the ordinary chain rule ALONG a C1
L2 curve Z, despite not requiring a locally Lipschitz gradient on the
entire state space. Write the difference quotient as

    [phi(Z(t+h))-phi(Z(t))]/h
       = integral_0^1 phi'(Z(t)+v[Z(t+h)-Z(t)])dv
                      [Z(t+h)-Z(t)]/h.

The second factor tends in L2 to Z'(t). The first is uniformly bounded
and converges in probability to phi'(Z(t)). Multiplication by the fixed
L2 vector Z'(t), by truncation exactly as in (13), gives L2 convergence
to phi'(Z(t))Z'(t). The derivative is continuous by (13). Products of
C1 bounded-operator and L2 curves obey the ordinary bilinear chain
rule. Therefore every H^(ell), Z^(ell) is C1 in L2, and the readout
pairings defining f_a and g are C1.

Expand g' through the forward layers and move each bounded operator
to its genuine adjoint. The coefficient of Z1_b' is y_b delta1_b/2.
The coefficient of W^(ell)' in its HS pairing is
(1/2)sum_a y_a delta^(ell)_a tensor H^(ell-1)_a. The coefficient
of W4' is (1/2)sum_a y_a H3_a. Substitution from (3) gives

    g'=||(Z1)'||_first^2+||(W2)'||_HS^2
                            +||(W3)'||_HS^2+||(W4)'||_2^2. (15)

For the first term at |rho|<1 put b_a=y_a delta1_a/2; its contribution
is E b^T C b=E (Cb)^T C^(-1)(Cb). At rho=-1 the realizable pair
velocity is (v,-v), and the same pairing is v^2 in the reduced raw
metric. Thus no inverse of a singular C or missing sample factor is
hidden in (15). All pairings are finite by Cauchy--Schwarz; no product
of two unbounded fields is asserted to belong to L2 without a bound.

Because W4(0)=0, g(0)=0. Bounds (8) give |f_a(s)|<=49s and
|g(s)|<=49s. Reduce the interval to

    S_* = min(S_0,1/196).

Then (15) gives 0<=g(s)<=1/4 and

    integral_0^s ||theta'(v)||_raw^2 dv=g(s)<=1/4.       (16)

For opposite labels, (14) supplies exactly the feature second-moment
symmetries in the first two populations, and (3), (15)--(16) supply
the uncut path/energy hypotheses of the previously audited softplus
top and middle curvature-action estimates. They may therefore be
applied to THIS constructed local path, once this assembly and its
dependencies have passed review. This is a discharge of their local
existence premises, not an all-time bound on historical sensitivities.

One may also define physical time on this local path by
dt/ds=[4(1-g(s))]^(-1). Its derivative is between 1/4 and 1/3,
so the reparametrized path exists at least through t=S_*/4 and
solves the population squared-loss physical equations with the correct
factor -2r_a. Equation (15) does not imply that the feature path has
been constructed for every later physical horizon. No such inference
is made here.
