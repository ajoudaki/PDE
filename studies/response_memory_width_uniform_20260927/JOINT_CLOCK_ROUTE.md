# Joint-clock route: proved bounds, reference oracle, and the remaining bridge

This is a scoped proof attempt using `paper/main.tex`, its comparison appendix,
and `docs/notation.qmd`. It does not establish the requested width-uniform
trajectory theorem. It establishes several of its missing estimates in the
bounded-activation case, including a useful old-clock reference oracle and,
for two hidden layers, width-uniform joint-clock consistency. The unresolved
step is feedback stability; smoothness of a dense trajectory in physical time
does not itself establish that step.

The statements below preserve both clocks, the matching prefixes, the dense
initialized matrices and their true transposes. No population closure is
assumed. Norms of neuron vectors are ordinary Euclidean norms, with the
normalizing factor displayed explicitly.

## 1. A deterministic uniform region is available

Assume throughout this section that all activations and their first
derivatives are globally bounded, by H and A respectively. This includes
tanh, but is stronger than the manuscript's general local hypotheses.
Suppose the initialized hidden operator norms, first-weight Frobenius norm
divided by sqrt(n), and readout norm divided by sqrt(n) are bounded by fixed
constants. Work on any regular interval of either finite-width closure.

Write Y for label RMS. The unchanged readout equation gives exactly

    d||w||_2^2/dt
      = n Y^2 - (4n/m) sum_a (f_a-y_a/2)^2 <= n Y^2.

Consequently, on [0,T],

    ||w||_2/sqrt(n) <= R := sqrt(||w(0)||_2^2/n + Y^2 T),
    rho <= q := H R + Y,
    integral_0^T rho dt <= S := Tq,
    mass(mu_t) <= M := 1+S.

Here mu_t is the actual joint-clock insertion measure; for the old clock it
is Lebesgue measure on the clock interval. These estimates do not depend on P.

There is a top-down recursion controlling all hidden operator norms. Let
D_l bound max_a ||delta_a^(l)||_2/sqrt(n), and let D_l^0 be the corresponding
initial bound. Start with D_L=AR. If K_l^0 bounds ||W_l(0)||_op, set, descending
from l=L to l=2,

    K_l = K_l^0 + 2H(M D_l + D_l^0),
    D_(l-1) = A K_l D_l.

Then ||W_hat_l||_op <= K_l and the asserted D bounds hold. To verify the
reconstruction estimate, put b_a=r_a delta_a/rho. Pointwise in the clock,

    (1/(mn)) sum_a ||b_a||_2^2 <= D_l^2,
    (1/(mn)) sum_a ||h_a||_2^2 <= H^2.

Projection contraction and Cauchy--Schwarz, first in the history measure and
then in the sample index, imply

    ||(2/(nm)) sum_a integral (Pi b_a)(Pi h_a)^T dmu||_F
      <= 2 M D_l H.

The joint prefix subtraction adds at most 2 D_l^0 H. For the old clock that
term is absent, so the same upper bound is valid. The recursion has no
circular dependence: delta at layer l uses only layers strictly above l.

The first layer is then bounded by integrating

    ||dot W_1||_F/sqrt(n) <= 2 rho D_1 X,

where X=max_a ||x_a||_2/sqrt(d). Thus all these physical bounds are uniform
in width and order. They use operator norms of W_0, not its diverging
Frobenius norm.

This applies on events whose Gaussian-initialization probabilities tend to
one. For example, a 1/4-net on each Euclidean unit sphere has at most 9^n
points; the bilinear-form Gaussian tail and the two-net estimate give

    Prob(||W_0||_op > K) <= 2 exp[n(2 log 9 - K^2/8)].

Choosing K sufficiently large and summing in n gives eventual bounds almost
surely, without any independence assumption between widths. The analogous
initial first-weight and readout bounds follow from their Gaussian quadratic
moments and exponential tails. This observation supplies the deterministic
region above; it is not a closure convergence theorem.

## 2. Coarse physical variation is also uniform

Measure a parameter increment by

    ||Delta W_1||_F/sqrt(n)
      + sum_(l=2)^L ||Delta W_l||_F
      + ||Delta w||_2/sqrt(n).

Only increments, rather than the initialized hidden matrices themselves,
are measured in Frobenius norm. The manuscript's exact defect-energy identity
and 2 sqrt(uv)<=u+v give, for either clock,

    integral_0^T sum_(l=2)^L ||E_l||_F dt
      <= M sum_(l=2)^L (D_l^2 + H^2).

Indeed every projection error is bounded by its unprojected history energy.
Combining this with

    ||F_1||_F/sqrt(n) <= 2rho D_1 X,
    ||F_l||_F <= 2rho D_l H,
    ||F_w||_2/sqrt(n) <= 2rho H

proves a width- and order-independent total-variation bound for the physical
parameter increments. This is obtained before any small-error estimate.

These facts repair two overly pessimistic constants in a direct reading of
the fixed-width proof. They do not bound the normalized response variation
for arbitrary depth: differentiation of backward responses introduces a
product of two neuron fields controlled only in L2.

For the dense flow, forward time derivatives need no backward derivative.
The chain rule and the preceding bounds give recursively finite constants
B_l, independent of n, such that

    max_a ||dot h_a^(l)||_2/sqrt(n) <= B_l.

One may take

    B_1 = 2 A q D_1 X^2,
    B_l = A(2q D_l H^2 + K_l B_(l-1)).

Also, dense residuals have a uniform positive lower bound on [0,T] when
their initial residuals have one. The prediction differential in the same
parameter metric is bounded using delta, h and X, so
|dot rho_dense| <= C rho_dense. Hence rho_dense(t)>=rho_dense(0)e^(-CT).
The nontrivial small-readout population case with Y>0 supplies such an
initial lower bound eventually in n. This does not claim one when the
limiting initial residual is zero.

## 3. An old-clock reference oracle removes closure derivatives

This construction is proof-only and does not modify the actual algorithm.
Stop the old-clock closure before rho_hat falls below c>0. Its clock has
1<=tau_hat<=M. Use its clock and its measure to insert the dense histories

    h_a^circ(t) = h_a^dense(t),
    b_a^circ(t) = r_a^dense(t) delta_a^dense(t)/rho_hat(t).

Use the original old-clock prefixes: h(0) on [0,1] and zero backward history.
The exact, unprojected product gives precisely the dense increment, since

    b_a^circ h_a^circ^T dxi
      = r_a^dense delta_a^dense h_a^dense^T dt.

The forward reference history is continuous at the prefix join and obeys

    (1/n) integral ||partial_xi h_a^circ||_2^2 dxi
      = (1/n) integral ||dot h_a^dense||_2^2/rho_hat dt
      <= T B_(l-1)^2/c.

The Legendre estimate therefore gives a forward projection tail O(P^-1)
in normalized L2 history norm. The backward reference history needs only
its bounded L2 mass; no derivative of rho_hat is used. Orthogonality yields

    sup_(t<=T) ||W_l^circ(t)-W_l^dense(t)||_F <= C/P,

where W^circ is reconstructed from the projected reference histories and
C depends on c,T,H,A,X and the preceding uniform region, not on n or P.

Comparison between the actual and reference reconstructions has a
P-independent stability constant in history norms. Both use exactly the
same measure and projector, so expand

    (Pi b_hat)(Pi h_hat)^T - (Pi b_circ)(Pi h_circ)^T
      = Pi(b_hat-b_circ)(Pi h_hat)^T
        + (Pi b_circ)Pi(h_hat-h_circ)^T

and apply projection contraction. As a result,

    ||W_hat_l(t)-W_l^dense(t)||_F
      <= C/P + C [integral_0^t R_l(s)^2 ds]^(1/2),

where one can take R_l^2 to be the sum over samples of

    ||h_hat_a^(l-1)-h_dense_a^(l-1)||_2^2/n
      + ||r_hat_a delta_hat_a^(l)-r_dense_a delta_dense_a^(l)||_2^2/n.

This avoids an order-dependent Lipschitz estimate on the raw moments and
avoids differentiation of the closure histories. If a uniform response
secant bound R_l(t)<=C e(t) in a compatible parameter-error metric were
proved, this estimate together with the unchanged first/readout equations
would imply

    e(t)^2 <= C/P^2 + C integral_0^t e(s)^2 ds,

and hence the requested O(P^-1) rate and a uniform continuation threshold.
The secant bound is the missing implication, not a background assumption
made here.

## 4. Two-hidden-layer joint consistency can be proved

Suppose L=2, activations also have globally bounded second derivatives, and
the regular joint closure is stopped on rho_hat>=c>0. In this case Psi
contains only h^(1) and b^(2). The small Gaussian initialization gives an
eventual uniform bound on ||w(0)||_infinity. The readout equation then gives

    ||w(t)||_infinity <= ||w(0)||_infinity + 2HS.

The unchanged first-layer equation bounds dot h^(1) in normalized L2.
Furthermore,

    dot z^(2) = dot W^(2) h^(1) + W^(2) dot h^(1),
    dot delta^(2) = dot w phi'(z^(2))
                    + w phi''(z^(2)) dot z^(2).

Consequently the integral of ||dot delta^(2)||_2/sqrt(n) is bounded by the
coarse physical variation from Section 2. Differentiating
f=w^T h^(2)/n also bounds integral |dot r|. Finally

    dot b_a^(2)
      = (dot r_a delta_a^(2) + r_a dot delta_a^(2))/rho
        - b_a^(2) dot rho/rho

has bounded normalized total variation because rho>=c. Summing the fixed
number of sample components proves

    (1/sqrt(nm)) integral_0^T ||dot Psi||_2 dt <= V_T

with V_T independent of n and P. The existing weighted Jackson estimate
therefore proves

    integral_0^T ||E_2||_F dt <= C_T/P^2

on this stopped interval, for the joint clock exactly as written.

For L>=3 the analogous derivative of delta^(l) contains

    phi''(z^(l)) dot z^(l) [W^(l+1)^T delta^(l+1)].

Neither of the last two fields is generally bounded pointwise. The preceding
L2 and variation bounds do not control their product in L2. Thus Section 4
does not extend by the same induction to arbitrary fixed depth.

Even for L=2, the O(P^-2) defect estimate does not finish the trajectory
theorem: the first-layer equation contains the unbounded upstream adjoint
field described next.

## 5. Why the feedback bridge is substantive

Forward responses are uniformly Lipschitz in the normalized parameter
metric on the region of Section 1. Backward response differences instead
contain, for a dense reference,

    [phi'(z_hat^(l))-phi'(z_dense^(l))]
      [W_dense^(l+1)^T delta_dense^(l+1)].

The other difference terms are controlled by the bounded hidden operator
norms and the response RMS bounds. This displayed term is multiplication
of the preactivation difference by a dense upstream adjoint field. Its L2
operator norm is that field's essential supremum. A Gaussian-type field
usually has no finite essential supremum, despite having every finite
moment. Time smoothness of the dense path does not alter this multiplier
fact. At finite width, replacing the essential supremum by an empirical
maximum generally introduces a growing constant.

This is not merely the familiar sqrt(n) choice of norm: if q is an
unbounded L2 random variable, choose unit L2 functions supported where
|q|>N. Multiplication by q maps these to functions of L2 norm at least N.
Truncation of q therefore does not prove a uniform Lipschitz bound; it
leaves a tail term involving stronger error norms. Finite moments lead
to a hierarchy of stronger norms unless an additional structural argument
closes it. No claim is made here that the algorithm produces these worst
directions, or that this is a counterexample to the desired theorem.

A scalar prediction discrepancy alone does not close the estimate. Dense
prediction dynamics have the form dot f=-K(theta)r. Closeness of f does not
control K. Already the scalar model f=uv has K=u^2+v^2: states with the same
prediction can have arbitrarily different subsequent prediction velocities.
The example only disproves that proposed inference; it is not a
counterexample satisfying the full initialized network setting.

For the joint clock there is a second issue with a reference-only oracle.
Using the dense clock gives good approximation to the dense history but
compares different polynomial subspaces with the actual closure. Using the
closure clock gives the P-independent projection contraction comparison
above, but its total normalized length must still be bounded. Uniform
closeness to a smooth reference curve does not bound variation: e.g.
n^-1 sin(n^2 t) converges uniformly to the smooth zero curve while its
variation diverges. A mechanism specific to this closure is required.
Section 4 supplies such a mechanism only for L=2.

## 6. Population passage and exact quantifiers

A completed width-uniform result would need, for every fixed T, constants
C_T and P_0(T), independent of n, and an identified probabilistic mode such
that, for all P>=P_0(T),

    sup_(t<=T) ||f_hat_(n,P)(t)-f_dense_n(t)|| <= C_T P^-q

on uniform events or in an explicitly integrable expectation estimate.
Dense convergence then adds its own width error. If only existence of the
canonical population limit is assumed, no n^-1/2 rate follows.

A direct population construction followed by a fixed-P particle limit
would require a separate proof for each P of existence, uniqueness and
convergence of the actual moment/Gram system with reused Gaussian W_0 and
its adjoint. Dense-flow convergence does not prove that result. Its
quantifiers would be

    for each fixed P: n -> infinity gives f_hat_(infinity,P),
    then: P -> infinity approximates f_infinity at the claimed rate.

Neither a diagonal choice P=P(n) nor fixed-width closure convergence
permits these limits to be exchanged. The joint clock also requires
control of the clocks and of the effective weighted polynomial spaces in
that passage. Its unit prefix ensures invertibility of each finite-width
Gram matrix, but need not give a uniform lower eigenvalue after a clock
whose raw size grows like sqrt(n) is rescaled. This is a transfer obligation,
not a proved failure of the physical reconstruction.

The proved estimates here substantially reduce the work: physical region,
residual mass, coarse physical variation, old-clock oracle consistency,
and two-layer joint consistency can all be obtained without assuming
closure bounds. What remains is a Gaussian/response-specific feedback
argument, and for deeper joint clocks a response-variation argument, that
follows from an explicitly stated dense regularity class rather than
assuming finite-width stability or population closure convergence.
