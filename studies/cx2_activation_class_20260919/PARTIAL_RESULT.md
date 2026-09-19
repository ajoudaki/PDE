# C-X2: precise positive results and the unclosed horizon

Author candidate, 2026-09-19. This is **not a completion of C-X2** and is
not a promotion proposal. It combines a local theorem for the full requested
activation class, a fitted orthogonal-reference theorem for its bounded
subclass, and explicitly conditional continuation/closure results. No
experiment or useful numerical accuracy is claimed.

## 1. Exact model and conclusions

Fix a nonaffine function phi in C1,1(R), with bounded derivative; C1,1 means
the derivative is globally Lipschitz. Both hidden layers use this same phi.
It may be unbounded, nonodd, nonmonotone, and have flat gates. Fix two
nonparallel normalized unit inputs u1,u2 in R², physical inputs sqrt(2)u_a,
labels (+1,-1), and weights (1/2,1/2). All variances, mobilities, loss and
population spaces are those of CLOSURE_PROOF.md (1)--(2): stored Gaussian
variances (1,1/n,1/n²), mobilities (n,1,n), unhalved mean squared loss,
full first-row field, actual initialized Gaussian action and its adjoint,
and Hilbert--Schmidt learned increment. Finite initial readout is retained.

**Local full-class result.** There is a positive T0, independent of width
and closure/numerical resolutions, on which:

1. The unique canonical strong autonomous population GF exists and is the
   limit of actual finite GF and simultaneous raw GD for every eta_n->0.
2. The activation-independent observable hierarchy in CLOSURE_PROOF.md
   converges to that same flow. Its state has two current joint populations
   and a finite feature-action matrix, with no growing time history or
   neural width. Convergence is uniform in time and on the whole input
   circle for predictions, and includes every separately fixed declared
   same-population observation tuple, both action orientations, and
   initial/current activation pairs with their second moments.
3. Both hidden layers have strictly positive paired activation displacement
   for sufficiently small positive times, and positive visited-law
   best-affine-fit error on a possibly shortened initial interval.
4. The exact-real finite-order systems are globally well posed. Their
   separate cubature and time refinements converge. Literal arbitrary-
   precision execution additionally requires supplied, locally uniformly
   consistent evaluators for phi and phi'; regularity alone does not imply
   computability. No executable general-activation solver is delivered here.

Each dataset and activation is fixed separately. The local existence time
can be chosen uniformly over this two-point geometry with the activation
bounds fixed, as in maintained C.1; strict activity constants need not be
uniform near parallel inputs. There is **no** claim of substantial fitting
at T0, a hierarchy-order rate, arbitrary refinement diagonal, or a practical
cost-to-accuracy bound.

**Fitted bounded reference.** If phi is additionally bounded and the inputs
are exactly e1,e2, REFERENCE_PROOF.md proves

    L(t) <= exp(-4 q0 t),       T_phi=log(8)/(4 q0),

with the strictly positive initialization constant

    q0 = (1/4) E[phi(Y1)-phi(Y2)]²,
    Cov(Y)=v I + mu² 11^T,
    mu=E phi(G), v=Var(phi(G)), G~N(0,1).

Thus L(T_phi)<=1/8. This is a global orthogonal-reference flow result,
without an oddness or monotonicity assumption. B.1 supplies its actual finite
GF capture and sufficient raw-GD condition eta_n sqrt(n)->0. Neither a
correlated-input fitting theorem nor dense-closure convergence through this
longer horizon is asserted from B.1 alone.

**Conditional full-class fitting.** For any phi in the full class, the same
rate holds on every strong canonical symmetric reference interval. To
conclude L(T_phi)<=1/8 one still has to construct that interval through
T_phi. The sufficient readout-tail interface is explicitly stated and
proved in REFERENCE_PROOF.md §6; it has not been verified for the general
unbounded activation. The conditional closure hypotheses S and E are
explicit in CLOSURE_PROOF.md §1.

## 2. Proof of the local statement and the full-row upgrade

Maintained global_nonlinear.md C.1 applies literally with d=m=L=2,
omega_a=1/2, unit mobilities, X=Y=1, and the fixed bounds
|phi(0)|, ||phi'||infinity, Lip(phi'). Its Gaussian initialization is the
specified one; its final initialization-perturbation clause retains the
vanishing but nonzero finite Gaussian readout. C.2 supplies mesh-uniform
subGaussian forward and backward fields on the same positive interval;
its constants survive the C1,1 mollification in C.1. These include c and
q_a=A*{c phi'(Z_a²)}, the two multipliers required by closure premise E.
Fatou transfers the tails to the strong target. No large-horizon restart
is inferred from this use of the initial theorem.

C.1 states the bottom equations in sample projections and uses operator
norm for the middle increment. The following direct upgrade supplies S in
the required full-row/HS topology. Include the full Gaussian row g in the
common initial carrier. Along the constructed sample solution set

    w(t)=g - 2 sum_a omega_a u_a integral_0^t r_a(s) delta_a¹(s) ds.

Projecting onto each u_b gives exactly C.1's bottom equation, including
its Gram factor and initial projection. Thus all fields are unchanged.
The continuous rank-one middle velocity has a strong HS integral, by
III.F.8, and equals the operator-norm integral already constructed. The
bounded-multiplier chain rule makes these velocities continuous, so the
upgraded state is C1 in full-row L² + HS + readout L². The local Euler
comparison in C.1 also holds in these stronger increment norms: replace
the rank-one operator inequality by III.F.30 and estimate the full-row
velocity with |u_a|<=1. It therefore gives the same canonical limit and
finite capture in the strengthened within-width comparison metric.

The countable carrier can include the smooth universal dictionary, all
Euler programs, and their finite unions before construction. III.F.7 and
A.1 make the source laws consistent. Its dictionary subspaces form the
reducing pair proved in CLOSURE_PROOF.md §2. Hypotheses S/E now hold on
[0,T0]; the complete argument in §§3--8 of that file gives the local
closure and numerical consistency. The scalar predictions have common
input Lipschitz constant on each bounded raw ball: two activation
Lipschitz bounds, the middle operator bound and Cauchy--Schwarz give

    |f(u)-f(v)| <= ||c||2 D1² ||A||op ||w||2 |u-v|.

A finite circle net upgrades fixed-query finite convergence to a circle
supremum, both for finite networks and their target. The closure proof
already establishes its own whole-circle convergence in the common state
space. These are two distinct comparisons; no cross-width operator norm
is used.

Weighted C.3 applies because the inputs are pairwise nonparallel, both
labels are nonzero, the three initialization variances/mobilities are
positive, and the population readout is zero. Its final weighted-loss
paragraph uses p_a=omega_a y_a, not y_a. It proves positive order-t² paired
activation displacement in each layer, as well as positive Gaussian
initial affine-fit errors persisting by L² continuity. This supplies item
3 on a shortened positive interval and transfers to declared pairs by
their proven convergence. It gives no later endpoint activity statement.

## 3. Conditional finite-network bridge on a longer interval

This additional lemma separates the finite algorithm from the unknown
continuation. Suppose S and E of CLOSURE_PROOF.md hold on a fixed [0,T]
for the actual canonical action and fixed finite data. Then actual finite
GF and raw GD with every eta_n->0 converge to that target for the declared
prediction and observation bundle. In this lemma S/E are hypotheses, not
conclusions about the requested unbounded activation class at T_phi.

Here are the details beyond the maintained short-time theorem. The
one-reference raw estimate in CLOSURE_PROOF.md (14)--(18) also compares two
states with the same initialized action, without filters or action error:

    ||F(theta)-F(theta_ref)|| <= C(1+R)d + C tau_ref(R).

It holds at finite width with normalized vector norms and ordinary
Frobenius increment norm as well. Only reference c and q_a are localized.
All constants are uniform on a fixed raw/action ball. Since phi has linear
growth and bounded derivative, the raw speed is uniformly bounded on that
ball. Strong-target tails are <=M exp(-aR).

Population Euler with mesh Delta converges to S by the Osgood/first-exit
argument in CLOSURE_PROOF.md §§5--6, using the target as reference. Call
its state error e_Delta->0. Its velocities and all needed backward nodes
also converge uniformly: bounded continuous multiplier continuity is
uniform on the compact target path. Denote the maximum of these errors
by z_Delta->0. This step does not assume mesh-uniform exponential tails
of these Euler programs.

At each fixed Delta, use A.1 on the complete finite oracle program:
expand all learned middle updates into finitely many ranks, and replace
every scalar feedback contraction and residual by its deterministic Euler
value. Coordinate instructions phi and (c,z)->c phi'(z) are continuous
with at most linear growth, so A.1 applies without second derivatives.
Build finite proxy parameters from these nodes and the rank expansion.
Recomputed matrix actions differ by finitely many rank factors times
vanishing scalar contraction errors, as in C.1 (11). Recomputed backward
products converge by localization against each fixed oracle L² law;
only uniform integrability at this fixed finite transcript is used here.
Thus proxy velocities, node laws and quadratic tails converge at fixed
Delta. All limiting raw norms and speeds are bounded uniformly for small
Delta, since population Euler approaches S.

For fields v,u at either width or population, with normalized norm,

    ||v 1_{|v|>2R}||2 <= 2||v-u||2 + 2||u 1_{|u|>R}||2.

Consequently the limiting proxy grid tails are bounded by
C z_Delta + C exp(-aR), with constants independent of Delta. Compare the
actual finite path and proxy interpolant on a subinterval of length tau.
Both velocities are evaluated at their respective preceding grid nodes;
their distance from interpolants is O(eta_n+Delta). At fixed R,Delta the
comparison gives, on the common ball,

    sup d_n <= C exp(C(1+R)tau) [d_n(start)
                  +(1+R)(eta_n+Delta)+z_Delta+exp(-aR)+o_P(1)].

Choose tau with C tau<a; the finite number of such intervals depends only
on T and target bounds. On the first interval the initial discrepancy
vanishes: the actual Gaussian readout has normalized L² norm tending to
zero, while the proxy may start with population readout zero. The actual
readout is never changed by the algorithm. First take n->infinity at
fixed R,Delta, then Delta->0, then R->infinity. The displayed bound tends
to zero. Repeat on the next interval, using the already vanishing initial
distance and the same limit order. Grid endpoints can be aligned with
the finite partition, or their O(Delta) errors included in the bound.

For raw GD, stop at first exit from a ball one unit larger than the proxy
path; the same estimate precludes that exit with probability tending to
one. No discrete energy claim or maximum-neuron tail bound is needed.
For GF, finite-dimensional energy provides global existence and the
required raw bounds; eta_n is absent in the same comparison. Fixed-grid
observations pass by A.1, and the state comparison plus strong multiplier
continuity and compact target-node curves removes grid/cutoff errors.
Fixed typed joint tuples pass by induction through the actual bounded
actions and adjoints. Their second moments converge by the same-index
L² coupling and Cauchy--Schwarz, preserving initial/current pairs.
The input Lipschitz estimate in §2 supplies the whole-circle prediction
assertion. This proves the conditional bridge.

## 4. Exact limits of this result

SOURCE_PROOF.md records a genuine failure of one convenient proof tool:
for phi(z)=z+epsilon sin(z), 0<epsilon<1, the first exact raw Euler state
has unbounded negative loss curvature in unit HS directions. This forbids
an ambient raw/clock Hilbert local-Lipschitz argument there. It does not
disprove neural GF existence, fitting, tails, or closure convergence.

The unresolved C-X2 requirements are:

- strong canonical continuation for every unbounded phi through T_phi;
- adequate reached-source tails for the actual flow and its construction;
- continuation and those tails for one positive correlated-input
  neighborhood through that horizon;
- a general-activation executable solver and its validated implementation.

The latter implementation should not be advertised as a solution of the
first three mathematical obligations. A uniform raw energy bound, a
conditional source theorem, or a sequence of globally existing bounded
approximations does not establish the missing limit or uniqueness.
