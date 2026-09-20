# Slow starts, protected fitting, and terminal obstructions in the p=1 closure

This study concerns the exact canonical population closure at order p=1 in
dimension three. It proves a genuine slow-start family and an unconditional
exponential-fitting theorem on an open family of three-input laws. It does
not settle fitting or terminal rates for every three-input law. Complete
proofs and isolated internal reviews are listed in the README; none of this
study has been promoted into the established book.

For the latest terminal classification attempt, see
`PLATEAU_CLASSIFICATION.md`: compatible triples have no finite nonoptimal
local minima, every finite positive-loss initialized accumulation point
is a strict saddle, and a separate theorem restricts plateau levels or
forces upper-parameter escape. A configuration-only iff remains open.

The subsequent weighted continuation is assembled in
`WEIGHTED_THREE_INPUT_RESULTS.md`: it completely classifies asymptotically
vanishing onset, proves the exact architectural minimum for every weighted
triple, and constructs strict initialized descent from loss 1 to a positive
floor 1/2 on three distinct balanced inputs. That floor is imposed by
same-label antipodes. Failure to reach an available zero-loss fit remains
open outside the positive classes proved here. These later results do not
alter the slow-family and protected-fitting proofs below.

## 1. Exact object and physical clock

Inputs x_i lie on sqrt(3) S2. The model is bias-free, phi=tanh, and

  L=sum_i p_i(f(x_i)-y_i)^2, p_i>0, sum_i p_i=1, y_i in {+1,-1}.

Use the exact general-dimensional initialized joint Gaussian marks and
ridge eta=1/4096 from docs/observable_p1.md. In the exact odd invariant
sector, b1 has six coordinates, b2 has three, and

  Gamma1=Law(b1,g,w), Gamma2=Law(b2,c), M in R^(3x6).

Initially w=g~N(0,I3), c=0, and M=D. Both dictionaries are frozen with
their complete joint correlations. Every entry of M trains, and reverse
propagation uses its actual transpose. These are the full closure equations
in the exact parity-reduced representation, not a scalar-M substitute.

For each x_i put

  a_i=E1[b1 phi(w.x_i/sqrt(3))],
  H_i=phi(b2^T M a_i), f_i=E2[c H_i],
  d_i=E2[b2 c phi'(b2^T M a_i)], Q_i=b1^T M^T d_i.

Then

  w'=-2 sum_i p_i(f_i-y_i) phi'(w.x_i/sqrt(3)) Q_i x_i/sqrt(3),
  c'=-2 sum_i p_i(f_i-y_i) H_i,
  M'=-2 sum_i p_i(f_i-y_i) d_i a_i^T.                       (1)

The metric is population L2 for w,c and Frobenius for M. Consequently

  L'=-||w'||2^2-||c'||2^2-||M'||F^2, L(0)=1.               (2)

The established bounded-feature characteristic existence proof extends
directly to these fixed dimensions. Each finite time has bounded c,
bounded M and bounded w-g: c_inf<=2t, ||M-D||F<=2t^2 and the w-increment
bound follows by integrating 4t ||b1||inf(||D||op+2t^2). This proves
unique finite-time continuation of (1), not a general-d neural-width limit.

## 2. A balanced genuine family with a long beginning

For 0<epsilon<=1/2, choose

  x_+=sqrt(3)(sqrt(1-epsilon^2-epsilon^4), epsilon, epsilon^2),
  x_-=sqrt(3)(sqrt(1-epsilon^2-epsilon^4),-epsilon, epsilon^2),
  x_0=sqrt(3)(1,0,0),

with labels (+1,+1,-1) and masses (1/4,1/4,1/2). The determinant of
the normalized input rows is 2 epsilon^3. Every positive member has three
distinct linearly independent inputs and exactly balanced class mass.

There are canonical constants C,c_0>0 such that

  -L_epsilon'(0)=c_0 epsilon^4+o(epsilon^4),
  inf{t:L_epsilon(t)<=1-delta} >=1/(C epsilon^2)             (3)

for every fixed delta in (0,1) and all sufficiently small epsilon.
The hitting time is permitted to be infinite; no eventual fitting claim
for this particular family is implicit in (3).

The mechanism is a second difference of complete current upper features,

  m_epsilon=(H(x_+)+H(x_-)-2H(x_0))/4.

On a fixed raw state ball about initialization, its L2 norm is at most
K epsilon^2. The bound uses the actual w and M, and follows from bounded
first and second input derivatives; it does not freeze hidden features.
If R is raw displacement from initialization, the exact loss expansion
and physical path energy give, while R<=1,

  0<=1-L<=C epsilon^2 R,  R^2<=t(1-L).

Thus

  R(t)<=C epsilon^2 t,  1-L(t)<=C^2 epsilon^4 t
       for 0<=t<=1/(C epsilon^2).                          (4)

A first exit from this ball needs at least that much time. A fixed loss
reduction is impossible inside the ball for small epsilon, proving (3).
The exact nonzero fourth-order initial slope is checked analytically in
early_delay.md, including a possible cancellation of its first coefficient.

This proves slow initial progress without confusing initial slope with
actual hitting time. It does not prove polynomial terminal decay at a
fixed positive epsilon, a positive terminal loss floor, or a matching
upper bound of order epsilon^-2.

## 3. An unconditional positive theorem on an open family

For a small positive angle theta, set

  a=cos(theta)/sqrt(3)+sqrt(2/3)sin(theta),
  b=cos(theta)/sqrt(3)-sin(theta)/sqrt(6).

Thus a>b>0, a^2+2b^2=1. Consider equally weighted, mixed-label inputs

  (x_1,y_1)=(sqrt(3)(a,b,b),+1),
  (x_2,y_2)=(sqrt(3)(b,a,b),+1),
  (x_3,y_3)=(-sqrt(3)(b,b,a),-1).                          (5)

For every sufficiently small fixed theta>0, there is an open neighborhood
of this configuration in (sqrt(3) S2)^3 times the positive probability
simplex, and a lambda>0, such that every law in that neighborhood obeys
the original initialized dynamics and

  Phi(Gamma1,Gamma2,M)=L,
  Phi'(t)<=-lambda Phi(t), Phi(t)<=exp(-lambda t)Phi(0).    (6)

All three inputs and all weights may vary independently within that
neighborhood. The state has an actual bounded fitted endpoint. The rate
is uniform within a sufficiently small chosen neighborhood; its size and
rate may depend on theta. The reference masses are 1/3, so the mixed
classes have masses 2/3 and 1/3. A balanced three-atom theorem is not claimed.

This is a genuinely open three-input result, not a reduction imposed on
the perturbed trajectories. The reference normalized determinant has
absolute value (a-b)^2(a+2b)>0. The neighborhood can be chosen to preserve
independence. It is an open family, not all generic or all separable triples.

A stronger result holds for the symmetric references themselves. Let P
cyclically permute coordinates. For every x on sqrt(3) S2, the equal-mass
law on

  (x,+1), (Px,+1), (-P^2x,-1)

has L'<=-4k_*L for one k_*>0 independent of x, and has a bounded fitted
endpoint. All independent openings 0<theta<pi/2 are included; this
symmetry-only result is not restricted to small openings. The proof in
cyclic_uniformity.md uses sign preservation of the initialized effective
vector, a linear/cubic noncancellation of its three averaged tanh features,
and compactness of the input sphere to make the initial activity uniform.
It does not expand the independent-perturbation neighborhoods beyond the
range established above.

At the 120-degree endpoint x+Px+P^2x=0, the signed data have
x_3=x_1+x_2 and sum_i p_i y_i x_i=0. A bias-free linear predictor cannot
even classify the three labels correctly: positivity on x_1 and x_2
forces positivity on their sum x_3, whose label is negative. The nonlinear
p=1 closure nevertheless fits exponentially by the same theorem. This
endpoint is a dependent triple, expressly distinguished from its nearby
independent triples. A vanishing first signed input moment is therefore
not by itself a negative case for this closure.

### Why the proof is stronger than loss dissipation

Oddness allows simultaneous sign reversal of an input and label without
changing the full vector field. After this reversal in (5), the reference
has three all-positive cyclically permuted inputs. Canonical coordinate
permutation symmetry gives equal predictions F along that reference.
Let Hbar be their mean upper activation and C=E2[c^2]. A proof clock s
defined by dS/ds=grad F retains every trained block and satisfies

  F_s=||grad F||^2>=||Hbar||2^2>=F^2/C, C_s=2F.

Therefore the current-state ratio obeys

  (F^2/C)_s=(2F/C^2)(C F_s-F^2)>=0,
  lim_(s->0+) F^2/C=k=||Hbar_0||2^2>0.                   (7)

The initialization-only k is a declared Gaussian expectation. Its strict
positivity, including at the collapsed diagonal reference, is proved
analytically with the canonical ridge and reverse response in
initialization_positivity.md. It is not assumed or estimated numerically.

Equation (7) protects the output produced per unit squared readout norm.
It gives F_s>=k even though the entire hidden representation changes.
Finite-clock polynomial bounds prevent escape, so F reaches one at an
actual bounded clock s_*<=1/k. The physical clock is ds/dt=2(1-F), giving

  L'=-4 F_s L<=-4k L                                    (8)

on the exact reference. This also yields convergence of the full state,
not just loss. The reference rate stays positive uniformly as theta->0.

### The first hidden layer supplies the missing perturbation control

At the collapsed diagonal reference, coordinate permutation symmetry
gives M a=rho v and d=delta v with v=(1,1,1)/sqrt(3). The initialized
rho is strictly positive. In the ascent clock, c_s=phi(rho b2.v), and

  delta=E2[(b2.v)c phi'(rho b2.v)]>0 for s>0,
  rho_s=delta[|a|^2+v^T M E1[b1 b1^T phi'(w.v)^2] M^T v]>=0.

Thus rho stays positive to fitting, and the actual endpoint has
Q=b1^T M^T d nonzero in L2. Finite-clock continuity transports this
nonvanishing to the endpoints of all sufficiently small noncollapsed
cyclic triples. No hypothetical future Gram bound is used.

For three independent input directions, the first-layer part of any
linear relation among the three prediction gradients is

  sum_i zeta_i Q_i phi'(w.x_i/sqrt(3)) x_i/sqrt(3)=0.

Input independence and the strictly positive tanh gates force each
zeta_i Q_i=0. Nonzero Q_i therefore forces all zeta_i=0: the full
prediction differential has row rank three. This controls all residual
directions, including those created by symmetry-breaking perturbations.

The quantitative version, useful for interpreting geometry, is as follows.
Let G_ij=x_i.x_j/3 and K_ij=sqrt(p_i p_j)<grad f_i,grad f_j>raw. Then

  lambda_min(K)>=lambda_min(G)
       min_i {p_i E1[Q_i^2 phi'(w.x_i/sqrt(3))^2]}.         (9)

To verify (9), apply the smallest-eigenvalue inequality for G pointwise
to the coefficients sqrt(p_i) zeta_i Q_i phi'_i and integrate; the
other two gradient blocks add nonnegative quadratic forms. Equation (9)
shows both the geometric conditioning and the first-layer backward
signal. A loss of upper-feature rank alone does not eliminate progress.

At each constructed fitted endpoint the full rank is now proved. Local
Hilbert continuity gives a state/data neighborhood where K>=kappa I.
The reference reaches it at a finite time with sufficiently small loss.
Finite-time data continuity puts all sufficiently small independent
perturbations there too. Their remaining path length is bounded by
(B/kappa)sqrt(L(T)), smaller than the distance to the boundary, so they
cannot exit. This proves entrance and all-time retention, hence fitting.
The reference gradient is bounded away from zero on the finite entrance
interval; shrinking the data neighborhood preserves this property and
establishes (6) from time zero. Complete details are in protected_family.md.

## 4. What a slow terminal example would actually have to do

For three independent inputs, terminal_geometry.md gives an exact
finite-state nullspace test for the full prediction differential.
At a fitting state with unit labels, readout dependencies require a
collision of label-oriented upper coefficient vectors y_i M a_i.
For a full-gradient singularity, the participating lower reverse fields
must additionally vanish, and the middle gradients must cancel.

Thus collapse or dependence of upper activations alone does not establish
a slow terminal mode. First-layer and middle responses can remove it.
The signed-coordinate-axis class is proved to have the exact asymptotic

  L(t)=A exp(-4 kappa_* t)(1+o(1)), A,kappa_*>0,

and the open family (5)--(6) excludes subexponential terminal fitting as
well. These are actual protections, not deductions from unsuccessful
counterexample searches.

Outside these classes, for architecturally compatible data, the
reachability of singular fitting states, bounded positive-loss critical
states, or unbounded trajectories from the prescribed initialization is
unresolved. The subsequent weighted continuation does construct a bounded
positive-loss endpoint on architecturally incompatible data and proves
that it attains the exact global loss minimum; see
`WEIGHTED_THREE_INPUT_RESULTS.md` and `plateau_construction.md`.
An arbitrary ambient stationary state is not an initialized negative
example. Nor does a deteriorating rate across a family imply a
nonexponential terminal tail for any fixed member.

## 5. Consequence for the size of a proposed universal-rate potential

Suppose a potential on the slow family satisfies

  Phi'<=-lambda Phi, L<=C_1 Phi^alpha,

with positive lambda,alpha and finite C_1 uniform across epsilon. Before
a fixed loss threshold ell is reached, these inequalities force

  Phi(0)>=(ell/C_1)^(1/alpha) exp(lambda tau_ell).

Combining with (3) gives the necessary lower bound

  Phi_epsilon(0)>=(ell/C_1)^(1/alpha)
                   exp(lambda/(C epsilon^2)).             (10)

So insisting on a common positive decay rate forces at least this
exponential-in-inverse-geometry growth of the initial potential. A
geometry-dependent rate may instead deteriorate. This is a necessary
growth bound; it does not identify a maximizing configuration or prove a
matching upper bound for an unknown potential. The potential L in (6)
uses a geometry-dependent family rate and is fully consistent with (10).

The remaining central question is whether the balanced slow family, and
then arbitrary independent triples, always recover and fit. The missing
estimate is global control of residual-relevant prediction-gradient
degeneracy or escape along those actual initialized trajectories. The
proved energy barrier establishes the early delay; the present endpoint
protection theorem closes that estimate only for the stated open family.
