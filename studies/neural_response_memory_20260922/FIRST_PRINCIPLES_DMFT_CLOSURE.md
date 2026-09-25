# First-principles history equations and the finite predictive-state hypothesis

2026-09-22. This continuation follows the user's explicit correction: start
from the defining dense dynamics and their Gaussian history law, then identify
an assumption on that law which could permit present-state compression. No
external literature or prescribed memory filter was consulted in this turn.
The previous history encoder is not adopted as the answer to this request.
Its algebra is preserved, but does not establish a canonical finite closure.

**Conclusion.** The exact interaction data are forward and backward two-time
Gram kernels together with their causal Gaussian-source response kernels.
A simultaneous finite causal realization of those data would give neuron
memory equations and aggregate population coupling by derivation. It does
not require a time Taylor expansion. A constructive, small, present-law
realization for the canonical nonlinear network has not been derived here.
Stating that its coefficients are unknown functions of current moments would
not supply that missing result.

## 1. Inputs and exact population operator history

Allowed established source: `docs/special_data_limits.md`, complete III.F
(including the Gaussian-conditioning and source-response proofs), and the
canonical equations already used in this study. The fixed-program theorem
has its stated bounded-derivative/capping hypotheses. No new interchange of
growing transcript, time mesh, width or cap limits is claimed. The operator
history identity below follows directly from any justified canonical flow.

Write h_a(t)=H1(t,x_a), d_a(t)=Delta2(t,x_a), Z_a(t)=Z2(t,x_a),
Q_a(t)=W2(t)* d_a(t). Let rho_a be probability weights, r_a=f(x_a)-y_a,
and u tensor v act by z -> u E[vz] in the appropriate neuron population.
The middle flow is

    W2dot(t) = -2 sum_a rho_a r_a(t) d_a(t) tensor h_a(t).       (1)

Integrating and applying it to the **current** query gives exactly

    Z_a(t)=W20 h_a(t)
       -2 int_0^t sum_b rho_b r_b(s) d_b(s) C_h(t,a;s,b) ds,
    Q_a(t)=W20* d_a(t)
       -2 int_0^t sum_b rho_b r_b(s) h_b(s) C_d(t,a;s,b) ds,     (2)

where

    C_h(t,a;s,b)=E1[h_a(t) h_b(s)],
    C_d(t,a;s,b)=E2[d_a(t) d_b(s)].                             (3)

The current forward and backward physical equations are

    h_a=tanh(W1 x_a/sqrt(d)), H2_a=tanh(Z_a),
    d_a=c tanh'(Z_a), Delta1_a=tanh'(W1 x_a/sqrt(d)) Q_a,
    W1dot=-2 sum_a rho_a r_a Delta1_a x_a^T/sqrt(d),
    cdot=-2 sum_a rho_a r_a H2_a,
    r_a=E2[c H2_a]-y_a.                                       (4)

These display how the two populations interact: the upper population's
learned memory is weighted by lower-population forward correlations, while
the lower population's learned memory is weighted by upper-population
backward correlations. They are uncentered moments, not centered covariances
of h or d.

## 2. The initial Gaussian action adds response kernels

It would be incorrect to replace W20 h or W20* d by unrelated fresh Gaussian
answers at each time. The established fixed-program Gaussian conditioning
rule is more precise. If the old forward query inputs are v_r and old reverse
query inputs are u_s, their centered named sources are xi_r and zeta_s, and

    W20 h = xi_h + sum_s u_s E1[partial_(zeta_s) h],
    W20* u = zeta_u + sum_r v_r E2[partial_(xi_r) u].            (5)

The forward source covariance is E1[h v], the reverse source covariance is
E2[u v]. The two oriented **source groups** are independent. The answers
in (5) are not independent, because they include the response corrections.
Named derivatives hold prior deterministic coefficients, all covariance
entries, expectations, controls and mesh sizes fixed, and differentiate every
causal nonlinear path in the explicit input expression. This is the source
convention proved in the established III.F.3–III.F.5.

For clarity, a finite time-discrete recursion gives a rigorous indexing
version before a continuous-time memory density is assumed. Let step k have
size epsilon_k. Forward queries h_a^k for all samples are made before the
reverse queries d_a^k. Define

    S_h(ka,sb)=E1[partial_(zeta_b^s) h_a^k],
    S_d(ka,sb)=E2[partial_(xi_b^s) d_a^k].                     (6)

Substituting the integrated discrete version of (1) into (5) gives

    Z_a^k = xi_a^k
      +sum_{s<k,b}[S_h(ka,sb)
        -2 epsilon_s rho_b r_b^s C_h(ka,sb)] d_b^s,            (7)

    Q_a^k = zeta_a^k
      +sum_{s<=k,b} S_d(ka,sb) h_b^s
      -2sum_{s<k,b} epsilon_s rho_b r_b^s C_d(ka,sb) h_b^s.    (8)

The covariance of xi is C_h; that of zeta is C_d. The current-forward term
in (8) is retained. No current learned update is included before step k.
Equations (7)–(8) hold in the fixed-program infinite-width source law, using
the exact discrete update identity; they are not finite-width pathwise
Gaussian identities. Applying the source law to uncapped unbounded instructions requires
its derivative-valid truncation hypotheses; using a continuum response density
requires a separate mesh-limit argument. Those are not silently obtained by
writing an integral in place of the sums.

Thus even the initialized operator has a history description, but it requires
the four arrays C_h,C_d,S_h,S_d. Compressing only the learned outer-product
history leaves an essential part of the canonical model unreduced.

## 3. A structural hypothesis on global evolution

A precise candidate is **finite predictive state for the joint covariance and
response law**. Its content is stronger than choosing P averages of the past:

1. Each full causal memory kernel obtained from (7)–(8), including learned
   terms and initialized response terms, factors through a P-dimensional
   evolving state. Different channels can be stacked; P must count the total
   dimensions, including sample blocks rather than hiding them as scalar modes.
2. The two colored Gaussian source histories also admit finite causal states
   reproducing their entire two-time covariances and canonical joint law with
   local initial neuron marks, including the independence of the two oriented
   source groups. Matching their separate equal-time variances is insufficient.
3. The coefficients of these realizations and the response coefficients are
   computable from the present retained population laws and explicit retained
   sensitivity variables. No unknown exact-history kernel, future dense
   trajectory or discarded operator action is an admissible coefficient source.

Items 1 and 2 are hypotheses about the actual global two-time objects. Item 3
is an additional closure and computability obligation; it does not follow
from low rank. A hierarchy would replace exact realization by a quantified
approximation with a decreasing joint error, controlled initialization error,
and a stable effect on forward/backward trajectories. None of these small-P
properties has been established for the canonical training law.

One falsifiable version of item 1 is that, across each cut in time, the
linear kernel operator mapping all earlier forcing to all later observable
responses, with the population coefficient trajectory fixed, has rank at most
P, with compatible causal factorizations across cuts. This is not a rank claim
for the complete nonlinear closed-loop response. Approximate
compression concerns its singular-value tail in a specified weighted norm.
This is a condition on response to admissible perturbations, not fitting one
observed curve. Smoothness, boundedness, plateaus and a finite input dimension
alone do not imply it.

## 4. Derivation of the present memory equations under that hypothesis

For one matrix-valued memory kernel, suppose the proposed realization is

    K(t,s)=L(t) Phi(t,s) B(s),
    partial_t Phi(t,s)=A(t) Phi(t,s), Phi(s,s)=I_P.             (9)

No exponential, polynomial or rational time form has been imposed. Assume
enough local integrability for the following finite-dimensional integral
equations. For a neuronwise driving signal v(s), define

    m(t)=Phi(t,0)m0 + int_0^t Phi(t,s) B(s) v(s) ds.            (10)

The product rule and differentiation of the upper endpoint give

    mdot=A(t)m+B(t)v(t),
    L(t)m(t)=L(t)Phi(t,0)m0+int_0^t K(t,s)v(s)ds.              (11)

This is a derived present-state equation, conditional on (9). The first term
represents hidden initial information and cannot be dropped without a reason.
Apply (11) to the upper neuron's backward-history drive d and the lower
neuron's forward-history drive h in (7)–(8). Instantaneous response terms
such as the s=k term in (8) remain direct current-state interactions.

The displayed L,A,B are not free trainable parameters. Equation (9) must
identify them with the canonical kernels. Prescribing convenient stable
matrices without that identification defines a new model.

## 5. The Gaussian sources need their own compatible present states

For a centered Gaussian source, a finite linear Markov realization would be

    dg=A_g(t)g dt+B_g(t)dB_t,    xi(t)=L_g(t)g(t),
    g(0) Gaussian with covariance P_g(0).                     (12)

Here B_t is a Brownian innovation independent of g(0), used to realize a
Gaussian law; it is not SGD noise. Coefficients are deterministic population quantities.
Let Phi_g be the propagator of A_g. Its covariance is exactly

    Cov[xi(t),xi(s)]
       =L_g(t) Phi_g(t,s) P_g(s) L_g(s)^T,  t>=s,
    P_gdot=A_g P_g+P_g A_g^T+B_g B_g^T.                        (13)

To verify this, solve the linear stochastic equation by variation of constants.
Future Brownian increments are independent of the state at time s, giving
the cross covariance; the increment covariance gives the displayed Lyapunov
equation. Equivalently these facts can be verified using finite Gaussian
increments and their covariances. Matching (13) to C_h or C_d is a necessary
part of the proposed approximation. It is not supplied by matching a drift
memory kernel. The realization must also preserve the canonical joint law
with initial local neuron marks and independence of the two oriented source
groups. Retained sensitivities must implement the named-source convention
in (5)–(6); differentiation with respect to a Brownian innovation is not the
same derivative without an explicit valid change of coordinates.

There is an elementary discrete criterion showing exactly what is assumed.
For an augmented jointly Gaussian process g_k with positive definite covariance P_k,
write H_k=E[g_{k+1}g_k^T]. A Gaussian Markov representation, if valid, has

    A_k=H_k P_k^{-1},
    D_k=P_{k+1}-H_k P_k^{-1}H_k^T >= 0,
    g_{k+1}=A_k g_k+D_k^{1/2} eta_{k+1}.                      (14)

Gaussian regression proves (14); the residual is Gaussian and independent
of g_k. To be independent of the *entire* earlier history it must additionally
satisfy, for every j<=k,

    E[g_{k+1}g_j^T]=H_k P_k^{-1}E[g_k g_j^T].                 (15)

Then every cross covariance with the old history is zero, so Gaussianity gives
independence from that history. This is a genuine global screening condition,
not a consequence of an equal-time covariance matrix. Singular cases require
consistent range restrictions and do not justify arbitrary inverse limits.

Equations (14) are also a provenance test: if P_k and H_k still have to be read
from a completed dense trajectory, they describe a realization after the fact,
not an autonomous simulation. They must be generated from retained canonical
queries, current population expectations and valid response rules.

## 6. What is averaged, and what is trained

The exact averages are specified in (3) and (6), with the output average
E2[c H2]. A valid reduction replaces their time-indexed history arrays by
current covariance/response matrices and whatever tangent-state averages
are needed to evolve those matrices. Expected sensitivities matter as well
as moments; the derivative of a population average kernel is generally not
closed using means and variances alone.

For example the exact present output law is

    fdot(x)=-2 sum_a rho_a r_a K(t;x,x_a),
    K=C_H2 + C_h C_d + (x dot x_a/d) C_Delta1,                 (16)

where every C in (16) is the equal-time uncentered population inner product
of its named features. This follows by differentiating E2[c H2], inserting
the three weight-block flows, and using adjunction. Each term is a Gram
kernel (the middle term uses tensor products), hence K is positive
semidefinite. But its time derivative contains further responses, so (16)
does not itself close the dynamics.

In a faithful reduction there is only the original training law. Targets
enter through the residuals; the vector fields and sensitivities evolve under
that same law. An effective small interaction matrix evolves because the
canonical population correlations and responses evolve. It is not fitted by
a separate backpropagation objective. If one instead independently trains
that matrix or the realization coefficients, one has defined another
optimization procedure and owes a separate identification argument.

The natural reduced interaction can involve several covariance and response
matrices rather than one universal M. Forward and backward source groups may
be independent while their induced answers remain coupled. Enforcing an
arbitrary transpose relation between response kernels is not a replacement
for the exact same-matrix conditioning identities.

## 7. Two tempting assumptions that are too restrictive

### Finite linear transport of all retained neuron observables

If Phi_l(t,omega) obeys dot(Phi_l)=A_l(t)Phi_l with a common finite matrix,
then Phi_l(t)=T_l(t,0)Phi_l(0). All such fields stay in their fixed initial
linear span in the neuron-label Hilbert space. This is an invariant-subspace
assumption, not a generic mechanism for nonlinear moving populations.
Representing both initial-operator actions in these same spaces additionally
requires the corresponding forward and adjoint invariance; that property is
strong for a Gaussian operator. It does not follow from finite observable
transport alone or constrain every possible nonlinear realization.

The attractive formula A=E[dot(Phi) Phi^T] E[Phi Phi^T]^{-1} is only a
projection coefficient. It does not prove that the orthogonal residual
vanishes, or that dot(Phi) can be computed without omitted operator actions.
It therefore cannot be used to assert a closed model by definition.

### An exact smooth finite Gaussian Markov lift

Suppose a centered Gaussian vector g(t) is mean-square continuously
differentiable, has nonsingular G(t)=E[g(t)g(t)^T], and satisfies the Markov
screening covariance identity on an interval. Set

    A(t)=E[dot(g(t)) g(t)^T] G(t)^{-1}.

Differentiating G gives Gdot=AG+GA^T. The Markov transition
T(t,s)=E[g(t)g(s)^T]G(s)^{-1} satisfies partial_t T=A(t)T by differentiating
the screening identity at its intermediate endpoint. Conditional covariance
V=G(t)-T(t,s)G(s)T(t,s)^T therefore satisfies

    Vdot=AV+VA^T,    V(s)=0.

Uniqueness of this finite linear ODE gives V=0. Consequently
g(t)=T(t,s)g(s) in L2: there is no new observable Gaussian innovation.
Thus this exact smooth Gaussian hypothesis reduces to finite global
covariance rank. Nonsingularity and regularity are material; this is not a
no-go theorem for nonlinear non-Gaussian per-neuron states or for approximate
Gaussian realizations with rough hidden innovation coordinates.

These observations prevent a hidden return to a frozen representation while
calling it a new dynamical closure.

## 8. Nonanalyticity, plateaus, and claim status

The structural assumptions (9), (13) and (15) concern causal propagation and
prediction. They require no Taylor expansion at initialization. Population
averaging and unbounded initial marks can give zero Taylor radius even for
finite per-neuron dynamics, as proved earlier in this study. Nonanalyticity
does not establish finite predictive complexity, but does not by itself rule
it out.

Stable fundamental modes and plateau behavior require separate properties
of the derived propagators and their forcing. These cannot be selected to
fit the desired appearance without modifying the target model. Small response
state rank alone supplies no convergence-to-equilibrium guarantee, and no
small-P canonical plateau theorem is asserted here.

Exact: the canonical operator-history identity, fixed-program Gaussian
source/response structure, aggregate output kernel, and finite-state
realization identities under the displayed assumptions.

Conditional: replacement of the full joint DMFT history law by finite
population states, provided all covariance, response, initialization and
coefficient-closure requirements are satisfied.

Open: an explicit small set of canonical neuron variables satisfying those
requirements, a method for deriving their coefficients using only the current
retained state, a quantified joint approximation error, and stable nonlinear
feedback propagation. Fixed input dimension does not remove the continuum
of sample-indexed fields for population-risk training.

This derivation answers what information must be compressed and how it
determines interactions. It does not yet answer which small canonical state
actually accomplishes that compression. The latter remains the central
research problem; naming unknown coefficient functions is not its solution.
