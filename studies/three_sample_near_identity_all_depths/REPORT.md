# Three inputs at general depth, with the accepted near-identity activation

2026-09-08. The required overall conclusion remains **unproved in this
analysis**. No valid theta_(delta,L)>0 threshold for the full global
canonical population/GF/raw-GD theorem is claimed here. The separate
large-gain construction does not answer the user's requirement and is
not used in any result below.

The accepted activation is a genuine perturbation of identity. The
results here use exactly

    phi_theta(z)=(1-theta)z+theta atan(z), 0<theta<=1/2,

with the original architecture, Gaussian initialization and raw metric.
The input condition is |rho_ij|<=1-delta for three RMS-unit inputs,
including singular input Grams. L counts hidden layers.

## 1. A sharper theorem that does hold within the required family

At Gaussian initialization, let Q_L be the three-sample feature Gram
after L hidden layers, and q_L its common diagonal entry. For every
L>=1 and every 0<theta<=1/2,

    1/[1+(5/2)theta L] <= q_L <= 1/[1+theta L/6],

    Q_L >= theta² delta² /
           {324*pi*exp(1)*[1+(5/2)theta L]} I_3.             (1)

In particular no additional small-theta threshold is needed for this
initialization result. It is strictly nonlinear for every theta>0.

There is also exact spectral structure. For C_L=Q_L/q_L,

    lambda_min(C_(L+1)) >= lambda_min(C_L),
    lambda_max(C_(L+1)) <= lambda_max(C_L).                  (2)

After the first layer the Grams are positive definite, so their
condition numbers cannot increase with initialized depth. Multiplying
by the scalar q_L does not change a condition number. Absolute feature
energy decays like 1/(1+theta L), but normalized conditioning improves.
For fixed positive theta,delta, the order 1/L in (1) is optimal as a
depth order: lambda_min(Q_L)<=tr(Q_L)/3=q_L<=1/(1+theta L/6).
This does not claim joint optimality in theta,delta and L of every
constant in (1).

The proof is in INITIALIZATION.md. An odd activation's normalized
Gaussian kernel is a convex combination of positive integer entrywise
powers of C_L. Each such power preserves the interval between its
smallest and largest eigenvalues, by the positive-semidefinite
entrywise-product identity. Cubic Gaussian features supply the first
strict gap, including for singular input Grams. Two reciprocal-variance
inequalities give the explicit depth dependence in (1).

The same companion proves an absolute initialization nonaffinity bound.
For a preactivation of variance q in (0,1],

    theta² q³/384
      <= inf_(alpha,beta) E[phi_theta(sqrt(q)G)-alpha-beta sqrt(q)G]²
      <=(2/3)theta² q³.                                    (3)

Thus this absolute gap is of order L^-3 at initialized depth L for fixed
theta. A positive absolute gap uniform over all depths is impossible
for this exact family already at initialization. A time-uniform gap
allowed to depend on each fixed L is not ruled out.

Equations (1)--(3) are initialization statements. Training changes the
Gaussian law, so (2) must not be interpreted as monotonicity in training
time or a bound on the trained Gram.

## 2. Why removing antipodal inputs does not finish the training proof

Excluding rho=-1 removes the direct oddness obstruction f(-x)=-f(x).
It does not force three inputs to be linearly independent. For example,
three planar unit vectors with pairwise rho=-1/2 sum to zero and are
admissible for delta<=1/2. With all-positive labels, the identity network
cannot fit them. The positive nonlinear mixture DOES supply independent
features, as (1) proves; this example is not a counterexample at theta>0.

The dynamics nevertheless become singular as theta decreases. For the
same example, every successful fitting state of loss at most 3/8 must
have raw distance R from canonical initialization satisfying

    R >= [(pi*L*theta)^(-1/L)-2]_+.

If a true strong GF reaches that loss at time T, then

    T >=(2/3)[(pi*L*theta)^(-1/L)-2]_+²,
    liminf_(theta->0) theta^(2/L) T
                         >=(2L/3)*pi^(-2/L).               (4)

A stronger depth-order conclusion comes from its first exit from a
fixed raw ball. For every fixed L>=2, whenever
theta<2/[pi(3^L-1)],

    T >= 4/[3*pi*(3^L-1)*theta].                           (5)

Thus fitting time is at least of order theta^-1 at every fixed depth.
For L>2 this is stronger than the time exponent in (4). The prefactors
in these necessary bounds are not asserted to be optimal.

NECESSARY_FITTING_SCALE.md proves these claims by an exact recursion
for the sum of the three sample features, the joint raw metric and
the true GF energy identity, also applied at a first radius exit.
They show that a theta-independent rate
cannot be imported from the identity reference. They do not rule out
a global theorem with theta-dependent rates, which remains the target.

## 3. The remaining proof obligations and the routes checked

The complete requested result needs more than (1): a global strong
canonical population solution, control of actual incoming-field tails
for identification with finite GF/GD, and a mechanism giving fitting
and maintaining nonaffinity along its trained trajectory. Three
different approaches were examined after the gain was rejected.

**Covariance-weighted source control.** The full response return has
an exact L2 bound as an orthogonal Gaussian projection, including
singular source covariance. This avoids estimating unstable individual
response coefficients. However, L2 bounds for those returns do not
give their higher moments. SOURCE_ROUTE.md gives a smooth near-identity
feature-span example demonstrating the failure of that generic
inference. A bound specific to actual reachable response combinations
is still missing.

**Approximation that preserves the gradient energy identity.**
ENERGY_GALERKIN_ROUTE.md constructs finite-partition true-gradient
approximants on the canonical spaces. Each is global with the original
restricted metric and genuine adjoints, and with a uniform finite-time
energy/path-length bound. Passage to a strong infinite-dimensional
flow remains conditional on an explicitly stated unresolved-coordinate
compactness estimate. Bounded Hilbert norms alone do not supply it.
These auxiliary approximants are not a substitute for the actual
finite-width Gaussian training algorithms.

**Small-offset affine comparison.** A legitimate candidate is
phi_theta(z)=z+theta[b+epsilon atan z], with b small and epsilon>0.
Its affine reference has initialized Gram
Gamma+theta² b² 11^T, which is positive definite for three distinct
unit inputs. The missing step is global fitting and a finite useful
response budget for that unit-slope affine reference; its initialized
Gram does not establish this. No epsilon threshold for the complete
trained theorem is claimed from this candidate.

None of these failed implications is a counterexample to the requested
positive-theta theorem. The mathematical bottleneck remains global
control of the actual near-identity trajectory, not an established
need for a large gain or an offset.

## 4. Adversarial checking and claim boundaries

The initialized-depth theorem was derived and independently checked by
multiple agents; the joint-metric fitting lower bound is separately
audited. REVIEW_STATUS.md records exactly which frozen files the
reviews cover. Their passing verdict concerns these partial results.
It must not be presented as a passing review of the still-unproved
global near-identity theorem.

The old gain theorem's mathematical reviews are stored separately and
have no bearing on satisfaction of the accepted activation constraint.
No experiment, commit or external publication was performed.
