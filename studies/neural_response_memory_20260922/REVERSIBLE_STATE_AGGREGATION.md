# One-sample learned interactions in current neuron-state coordinates

2026-09-22. Theory-only continuation of the user's reversible neuron-state
proposal. No external literature, training experiment, or Git write is used.
This note assumes the desired state law and derives the interaction it must
carry. It does not attempt to prove that a small canonical state exists.

## Current contract and corrections

There is one training pair (x,y). Both hidden layers have width n. The
activation remains phi, with derivative phi'. The output is the normalized
neuron average. The loss is the unhalved squared residual and the canonical
physical mobilities are (n,1,n). W0 is the actual initialized middle matrix,
including its normalization, and is retained together with its actual
transpose. Only the learned increment and its history are being represented
macroscopically. This supersedes any requirement in earlier notes that this
continuation must also eliminate the initialized operator.

A finite reversible state per neuron does not imply finite separation rank
of the learned matrix. The earlier finite-factor explanation is only a
special case. For example, states (a_i,v_i) obeying a_i'=0, v_i'=-a_i v_i,
v_i(0)=1 have polynomial dynamics, whereas

    int_0^t v_i(s)v_j(s) ds = (1-v_i(t)v_j(t))/(a_i+a_j)

has rank n whenever t>0 and the positive a_i are distinct. Its quadratic
form is int_0^t (sum_i c_i exp(-a_i s))^2 ds. If zero, differentiating the
vanishing exponential sum at zero through order n-1 gives a nonsingular
Vandermonde system and hence c=0. The example only disproves the rank
implication; it is not a claimed trajectory of the canonical neural model.

## 1. Assumed motion and the exact learned-weight source

Use a for a possible first-layer state and b for a possible second-layer
state. Let their spaces be finite-dimensional, of dimensions P1 and P2.
Write h1(a) for the first-layer activation readout and delta2(b) for the
second-layer backward readout for the fixed input x. All required initial
marks and explicit-time dependencies must be included or stated. The
readouts below are fixed functions of these augmented states.

The stipulated state equations are

    m1_j' = F1(t,m1_j; Q_t),
    m2_i' = F2(t,m2_i; Q_t).

Q_t denotes the current shared quantities used by the assumed closure;
these must be computed from the current retained model, rather than read
from a completed dense trajectory. They can include the current population
measures, interaction field, residual and fixed-operator signals. This is
a stronger assumption than invertibility of the full dense network alone:
the displayed velocity must be single-valued in its stated arguments.

For a given Q_t path, assume F_l continuous in time, C1 in state, and locally
bounded with locally bounded state derivative. Work on a finite interval
where their flows exist and are invertible between transported domains.
Assume the readouts are C1 and impose the integrability needed for each
population integral. No analyticity is assumed.

Set r(t)=f(t)-y and assume this residual path is continuous on the interval.
Continuous canonical network trajectories provide this regularity. Define
the learned kernel entries w_ij by

    W2_ij(t) = W0_ij + w_ij(t)/n.

The canonical middle-weight equation is exactly

    w_ij'(t) = -2 r(t) delta2(m2_i(t)) h1(m1_j(t)),
    w_ij(0)=0.                                               (1)

Thus the rank-one update has the same fixed source for every state pair.

## 2. Derive a current-coordinate interaction field

Let Phi_l(s;t,m) denote the state at earlier time s on the trajectory that
has state m at t, with the shared coefficient path understood. The literal
inverse-flow representation is

    k_t(b,a) = -2 int_0^t r(s)
                    delta2(Phi_2(s;t,b)) h1(Phi_1(s;t,a)) ds. (2)

It is a definition, not the proposed numerical evaluation method. Along
every actual neuron pair it equals the integral of (1).

The equivalent forward equation, obtained by differentiating along a pair
of moving states, is

    partial_t k + F2(t,b) dot grad_b k + F1(t,a) dot grad_a k
        = -2 r(t) delta2(b) h1(a),
    k_0(b,a)=0.                                              (3)

This is a transport equation for one scalar function on the product of
the two neuron-state spaces. The two gradient terms move the coordinate
arguments with their neuron populations; the right side deposits the
current rank-one learning contribution.

Proof of equivalence and conditional uniqueness: evaluating (3) at
(m2_i(t),m1_j(t)) and using the chain rule gives exactly (1). The initial
values agree, so w_ij=k_t(m2_i,m1_j). More generally, each product
characteristic starts on the initial domain and has a unique value obtained
by integrating the source. The invertible C1 flows give a single-valued
C1 field on the transported domain. Two solutions differ by a quantity
constant on characteristics with zero initial value, so their difference
vanishes. This proves existence/uniqueness for the given velocity and
residual paths, not well-posedness of the entire coupled closure.

Equation (3) can be evolved forward together with the populations. It needs
no stored list of past responses and no backward trajectory replay. Its
current macro state is nevertheless a function k_t, not a fixed number of
scalar moments. Calling its domain finite-dimensional must not hide that
distinction.

## 3. Aggregate interactions evaluated on the current populations

Let mu_l,t be the current neuron-state distribution. At finite width it is
exactly n^{-1} sum_i delta_{m_l,i(t)}. Define

    J2(t,b) = int k_t(b,a) h1(a) mu_1,t(da),
    J1(t,a) = int k_t(b,a) delta2(b) mu_2,t(db).               (4)

At an actual neuron, these equal the corresponding action of the learned
matrix and its transpose:

    z2_i = (W0 h1)_i + J2(t,m2_i),
    b1_j = (W0^T delta2)_j + J1(t,m1_j),
    h2_i = phi(z2_i),
    delta1_j = phi'(z1_j) b1_j.                              (5)

Here h1_j=phi(W1_j x/sqrt(d)), delta2_i=c_i phi'(z2_i),
f=n^{-1} sum_i c_i h2_i, and r=f-y. The original read-in and read-out
updates remain W1_j'=-2r delta1_j x^T/sqrt(d), c_i'=-2r h2_i.
The hypothetical closure supplies any further state components and their
velocities consistently with these relations.

The same k appears in both directions with its arguments exchanged under
the integral; two unrelated interaction kernels would lose the common
matrix/transpose constraint. For equal widths the normalized empirical
averages provide precisely the 1/n in the learned matrix. No independence
of the neuron states or of W0 is used in these finite-sum identities.

The measures evolve by state transport:

    partial_t mu_l + div(F_l mu_l)=0.                        (6)

In weak form, d/dt int q dmu_l = int grad(q) dot F_l dmu_l.
For empirical measures this is the chain rule applied to a finite sum.
For a continuum measure transported by the flow it follows by pulling the
integral back to the initial measure and differentiating, when integrable.
This is a conditional population formulation, not a new width-limit proof.

The retained W0 acts on the actual indexed populations. Their two unmarked
marginal distributions do not generally determine that action. Any claimed
closed implementation must preserve this fixed coupling and its correlation
with current states, as explicitly authorized by the user. If the proposed
F_l needs a neuron-dependent signal not determined by its stated arguments,
additional state/marks or an explicit coupling argument is required.

## 4. The induced moment/message hierarchy

The macroscopic aggregates are derived rather than chosen. For a fixed
differentiable scalar observable q(a), define its learned message to an
upper neuron at state b:

    A_q(t,b) = int k_t(b,a) q(a) mu_1,t(da).

The actual learned forward field is A_h1. Along a receiver trajectory b(t),
the product rule gives

    d/dt A_q(t,b(t))
      = -2r(t) delta2(b(t)) E_1[h1 q]
        + A_(F1 dot grad q)(t,b(t)).                         (7)

At finite width, differentiate n^{-1} sum_j
k_t(b(t),m1_j(t)) q(m1_j(t)). The first factor's derivative is (1)'s
source; the second is grad(q) dot F1. This proves (7) with no integration
by parts or boundary assumptions. The transported continuum proof uses the
same initial-coordinate integral and sufficient domination. There is no
extra divergence term.

Similarly, with B_q(t,a)=int k_t(b,a)q(b)mu_2,t(db),

    d/dt B_q(t,a(t))
      = -2r(t) h1(a(t)) E_2[delta2 q]
        + B_(F2 dot grad q)(t,a(t)).                         (8)

If an observable itself depends explicitly on time or evolving shared
coefficients, replace F_l dot grad(q) by its full partial_t q+F_l dot grad(q).

Equations (7)–(8) expose the analogue of a statistical-physics moment
hierarchy: local response factors, population cross moments, and the next
message obtained by differentiating an observable along the state flow.
For example the forward source uses E_1[h1^2] when q=h1; its next message
uses the current observable F1 dot grad(h1), the instantaneous derivative
of the first-layer response. No time Taylor series is involved.

If F_l is polynomial of degree d_F and q has degree p, F_l dot grad(q)
has degree at most p+d_F-1. Nonlinear polynomial drift therefore does not
generally close any fixed-degree polynomial family. A finite invariant
observable family can close the number of message channels, but the source
moments and their receiving-state dependence must also be computable from
retained state. None of this implies finite rank of the full learned matrix.

## 5. A stronger simplification: an antiderivative along the state flow

If the law becomes autonomous on an augmented state z=(b,a,g), where g
contains shared coordinates and fixed initial marks are retained, let V(z)
be its velocity and S(z)=-2r(g)delta2(b)h1(a). A function U satisfying

    V(z) dot grad U(z) = S(z)                               (9)

immediately yields w_ij(t)=U(z_ij(t))-U(z_ij(0)). This follows by the chain
rule and integration. Hence a state-only readout may sometimes replace even
the evolving pair field; the initial term is evaluated from stored initial
marks, not reconstructed by unstable backward integration.

Finding U is an additional equation to solve from the known dynamics.
Reversibility alone does not ensure a global regular solution: on a closed
orbit the source integral must vanish, and at an equilibrium a differentiable
U requires S=0. A clock-augmented version reduces to the time-dependent
transport formulation (3), which is the general finite-horizon construction.
No unspecified future-integral formula is licensed as an online coefficient.

## 6. Scope and status

Exact under the stated reversible single-neuron laws: pair transport,
finite-width learned matrix reconstruction, forward/transpose population
integrals, weak measure transport, and the message hierarchy.

No additional rank or finite-separable-moment assumption is used. The pair
field can represent a full-rank sampled matrix. The continuous field may
still be costly to resolve; retaining a fixed state-space domain is not a
proof of a small numerical description, stable inversion, a plateau, or a
closed finite list of macroscopic scalars.

The assumed canonical state law is not derived here. Neither is a general
width-limit interchange, global coupled well-posedness, or an approximation
rate. This result supplies a first-principles form in which to study those
questions, with the learned interaction and its coefficient provenance
explicit.

## Inputs and checks

Root used the canonical one-sample equations and current conversation,
the established notation already read in docs/README.md and docs/NOTATION.md
(hashes rechecked unchanged), and the exact operator-history identity read
in this study. No other study or external scientific source was consulted.
Two fresh prompt-scoped routes wrote PAIR_STATE_TRANSPORT_ROUTE.md and
PAIR_FLOW_POTENTIAL_ROUTE.md. The transport route independently checked its
core equations, then checked root's supplied message-hierarchy extension.
Root read both route reports completely. Both agents then checked the
completed synthesis in their assigned scopes and found no blocking errors;
an explicit continuity assumption on r was added following the transport
check. These are collaborative internal checks, not independent promotion
reviews.
