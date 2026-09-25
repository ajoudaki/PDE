# A concrete population history ODE with rational relaxation modes

2026-09-22, continuation of the response-memory question. Root construction,
with scoped algebraic checks by `neuron_relaxation_construction` and
`response_coupling_route`. This is theory, not a training experiment or an
established-book addition.

**Scope.** This constructs explicit evolving forward/backward history states
per neuron, and a small middle coupling for the **learned increment** of the
canonical dense layer. It gives an exact finite-history encoder, a finite
approximate dynamics when the initial dense operator is retained, an exact
closure-defect identity, and conditional plateau and history-approximation
statements. It does not eliminate the initial Gaussian operator, establish
width-independent efficiency, remove sample-count dependence, or prove that
the self-consistent approximations converge to dense training. Those gaps are
part of the result, not assumptions silently granted.

## 1. Canonical setup and normalization

Use the model and physical GF in `RESPONSE_STATE_SYNTHESIS.md`, section 3.
There are finitely many samples indexed by a, positive probabilities rho_a
summing to one, and r_a=f(x_a)-y_a. Let H_l,a be the forward activation and
Delta_l,a the backward preactivation sensitivity in layer l. In particular
Delta_2,a=c tanh'(Z_2,a), Delta_1,a=tanh'(Z_1,a) Q_a, Q_a=W2* Delta_2,a.

Each neuron population is a Hilbert space with normalized inner product;
finite width uses <v,w>=v^T w/n. Define

    (u tensor v) z = u <v,z>.

Thus the finite matrix representing u tensor v is uv^T/n, and the canonical
middle update is exactly

    W2dot = -2 sum_a rho_a r_a Delta_2,a tensor H_1,a.             (1)

All transpose/adjoint actions below use this same operator. Hilbert-Schmidt
norms use these normalized Hilbert spaces. Finite-width identities are exact;
the history identities extend to Hilbert-valued population signals whenever
the indicated Bochner integrals and norms exist. No new population-limit
identification is asserted.

## 2. An explicit closed encoder for each neuron history

Let l_k(u)=sqrt(2k+1) P_k(2u-1), k>=0, be orthonormal shifted Legendre
polynomials on [0,1], with b_k=l_k(1)=sqrt(2k+1). For a signal F(s) on
an increasing clock interval [0,a], define

    z_k(a) = (1/a) int_0^a l_k(s/a) F(s) ds.                     (2)

For continuous F, differentiation under this finite integral gives

    a dz_k/da = b_k F(a) - sum_{j<=k} A_kj z_j,                 (3)

where

    A_kk=k+1;   A_kj=b_k b_j for j<k;   A_kj=0 for j>k.         (4)

For completeness, the coefficient of l_j in (u l_k(u))' is b_k b_j for
j<k: integration by parts leaves its value at 1, since u l_j' has degree
less than k and is orthogonal to l_k. The diagonal coefficient is k+1 by
the leading polynomial coefficient; higher coefficients vanish by degree.
Substitution into the derivative of (2) proves (3). Locally integrable F
gives the same equation almost everywhere by its integral formulation.

The first P equations close exactly as encoders: they never require z_P or
any derivative of F. This is the crucial distinction from the neuron-response
derivative hierarchy. Truncation affects reconstruction, not the correctness
of the retained history coefficients for a supplied signal.

This is the scaled Legendre history encoder from the HiPPO framework;
the published definition, coefficient theorem, and complete derivation were
checked in sections 2.1–2.2, theorem 2, B.1.1 and D.3 of
[Gu et al., HiPPO (2020)](https://arxiv.org/html/2008.07669).
The elementary derivation above is also self-contained given Legendre
orthogonality. The neural activity clock and bilinear weight construction
below are this study's adaptation, not claims imported from that paper.

For P=3 the matrices are

    A = [ 1       0        0
          sqrt3   2        0
          sqrt5   sqrt15   3 ],       b=(1,sqrt3,sqrt5)^T.

The eigenvalues are 1,...,P and are distinct. Hence the homogeneous
propagator between positive clock values a_* and a is

    exp[-A log(a/a_*)],                                        (5)

whose modes are (a_*/a),...,(a_*/a)^P. These are rational powers of the
accumulated clock; if a=a0+t they are rational in physical time. Constant
F gives limiting coefficients (F,0,...,0) as a tends to infinity, since
A(F,0,...,0)^T=bF. The integral formula also proves this limit for bounded
F tending to a limit, by dominated convergence. This concerns the driven
encoder, not an unconditional convergence theorem for a coupled network.

## 3. Use a clock that stops when learning stops

A history window growing indefinitely in physical time keeps reallocating
resolution after the network stops moving. Instead set

    R(t) = sqrt(sum_a rho_a r_a(t)^2),
    a(t) = a0 + int_0^t 2R(s) ds,          a0>0.                 (6)

For each sample define clock-signals

    F_a = (r_a/R) Delta_2,a,     G_a=H_1,a,                     (7)

when R>0. Signals at zero-clock intervals need not be defined through a
division: all implementation equations below have a continuous formulation.
Extend F_a,G_a as their initial constant values on the artificial clock
interval [0,a0]. If R(0)=0 choose initial F_a=0; the system is stationary.
This artificial past is known at initialization and will be subtracted
exactly from the represented weight increment.

Let U_a,k and V_a,k be (2) for F_a and G_a. Their physical-time equations are

    Udot_a,k = (2/a)[b_k r_a Delta_2,a - R sum_j A_kj U_a,j],
    Vdot_a,k = (2R/a)[b_k H_1,a - sum_j A_kj V_a,j].             (8)

Initialize U_a,0=F_a(0), V_a,0=G_a(0), and all higher coefficients zero.
These equations are nonsingular, use no 0/0, and freeze at R=0. For every
neuron the state consists of P coordinates for each of these signals.

The same construction can be applied in **both layers**, to H_l,a and
(r_a/R) Delta_l,a, l=1,2. Thus there are evolving forward and backward
history populations in both layers. For the middle update only the lower
forward and upper backward histories enter directly; the other two histories
are optional additional retained state, not hidden requirements in (8).

For a fixed finite sample set, these are population fields, not one shared
state vector: U_a,k(omega_2), V_a,k(omega_1). Their laws can be pushed forward
under the corresponding neuron ODEs. Writing a transport PDE for those laws
does not remove the initial-operator issue described below.

## 4. The condensed coupling follows from the weight equation

Equation (1) in the clock (6) reads

    dW2/da = -sum_a rho_a F_a tensor G_a.                       (9)

Bilinear Parseval applied to (2) therefore gives the exact identity

    W2(t)-W2(0)
      = -sum_a rho_a [a(t) sum_{k>=0} U_a,k tensor V_a,k
                     -a0 F_a(0) tensor G_a(0)].                (10)

To justify the tensor identity, expand the two Hilbert-valued L2 histories
in the same complete orthonormal basis. The cross terms between a retained
mode and an omitted mode integrate to zero. The series is absolutely
convergent in Hilbert-Schmidt norm by Cauchy–Schwarz and Parseval.

Retain k=0,...,P-1 to define K_P(t). Its moving part has the form

    K_P,moving = U M V*,       M=-a(t) diag_a(rho_a I_P),        (11)

where U maps finite channel coefficients to the upper neuron population,
and V maps them to the lower population. The initialization correction in
(10) is a known fixed finite-rank addition. One can include it by augmenting
the factors and core with fixed channels. For one sample the moving M is
simply -a I_P. In this construction M is prescribed by the derivation,
not independently optimized; the nonlinear evolution is in the neuron
signals driving U,V and in the shared residual clock.

The factors are therefore **constrained evolving history coordinates**.
Although (11) is algebraically a low-rank factorization, its vector dynamics
are (8), rather than gradient descent on free factor entries. It neither
freezes those vectors nor rebrands free factor training.

## 5. Exact defect of the finite reconstructed weight dynamics

Put U_a=[U_a,0,...,U_a,P-1], V_a=[V_a,0,...,V_a,P-1] and define current
endpoint reconstructions Fhat_a=U_a b, Ghat_a=V_a b. Directly from (4),

    A+A^T = I + b b^T.                                       (12)

Differentiate a U_a V_a* using (8) and (12). The result is

    d(a U_a V_a*)/dt
      = 2R [F_a tensor G_a
             -(F_a-Fhat_a) tensor (G_a-Ghat_a)].               (13)

The dummy-history correction is constant. Thus W2hat=W2(0)+K_P obeys

    W2hatdot = -2 sum_a rho_a r_a Delta_2,a tensor H_1,a
               +2R sum_a rho_a e_F,a tensor e_G,a,             (14)

with e_F,a=F_a-Fhat_a and e_G,a=G_a-Ghat_a. At R=0 use the division-free
derivative from (8), which is zero. Formula (14) displays the finite closure
error explicitly. It is a product of two endpoint errors; it has no fixed
sign in the loss derivative. The canonical loss-dissipation theorem therefore
does not automatically transfer to the surrogate.

Evaluating all forward/backward fields with W2hat, and evolving W1 and c by
their canonical physical GF equations, makes (6),(8) a definite self-consistent
finite-width ODE. It retains the actual adjoint W2hat*. Its right-hand side
is locally Lipschitz for a>=a0. The Euclidean residual norm R is Lipschitz;
the eliminated normalization r/R does not introduce a singularity.

For finite n,P, bounded labels and fixed finite data, this ODE is global.
Indeed tanh bounds give R<=||c||+Y and ||cdot||<=2R, so c,R,a are bounded
on every finite time interval by integrating this scalar differential
inequality. The integral representation bounds each U coefficient by the
L2 clock-history norm of F, and each V coefficient by that of H1. Since
|r_a|/R<=rho_a^{-1/2} and ||Delta2,a||<=||c||, these remain bounded on finite
intervals. Equation (10) with P terms bounds W2hat. Finally
||W1dot|| is bounded by a finite constant times R ||W2hat|| ||c|| using
the bounded data and tanh'. No state can escape to infinity in finite time,
so the local solution extends globally. This is finite-width well-posedness,
not a width-uniform population convergence theorem.

## 6. What can be proved about plateaus

Homogeneous encoder modes (5) always have limits because a(t) is positive
and nondecreasing. They tend to zero if a tends to infinity; they freeze at
finite limits if a has finite limit. This says nothing by itself about an
arbitrarily forced coupled solution.

There is a concrete sufficient condition for the full finite surrogate:

    int_0^infinity R(t) dt < infinity.                         (15)

Then c has finite total variation, a tends to a finite limit, and U,V stay
bounded. Their derivatives in (8) have norms bounded by constants times R,
so they also have finite total variation. The reconstructed W2hat is bounded
and converges by (10). W1dot is bounded by a constant times R and W1
converges. Continuity of tanh, its derivative, and the finite operator
actions gives convergence of all forward/backward neuron responses.
Optional extra history states in layer1/layer2 obey the same argument.

This is a proved conditional plateau statement. It does not show that
training succeeds or that (15) holds. In particular R(t)->0 alone is weaker
than (15). Constant targets for the isolated encoders also give plateaus,
but arbitrary population feedback need not produce convergent targets.

## 7. A history error bound without Taylor analyticity

At a fixed clock value a, use the normalized histories F_a(a u),G_a(a u)
on u in [0,1], including the fixed artificial initial interval. Let Pi_P
be their orthogonal projection onto l_0,...,l_P-1. For a single sample,

    ||K-K_P||_HS
      <= a ||(I-Pi_P)F(a .)||_L2([0,1];Omega2)
             ||(I-Pi_P)G(a .)||_L2([0,1];Omega1).               (16)

For multiple samples sum the right sides with rho_a. This follows from
the vanishing retained/omitted cross terms and Cauchy–Schwarz. Hence fixed
history approximation converges for any L2 histories; no time Taylor
series is used.

There is a conditional explicit rate. For sufficiently regular histories,
define C_F^2=int_0^1 u(1-u)||dF(a u)/du||^2 du and similarly C_G. The
shifted Legendre identity

    -[u(1-u) l_k']' = k(k+1) l_k

and integration by parts imply the weighted derivative functions
l_k'/sqrt(k(k+1)), k>=1, are orthonormal for weight u(1-u). Bessel's
inequality, applied to F', therefore gives

    sum_{k>=1} k(k+1)||F_k||^2 <= C_F^2.

Since k(k+1)>=P(P+1) for k>=P,

    ||K-K_P||_HS <= a C_F C_G/[P(P+1)].                        (17)

C1 histories suffice, as do weak histories with justified integration by
parts and finite indicated energy. The normalized residual direction can
lose regularity near R=0; that regularity is not asserted automatically.
Constants depend on the reached histories and horizon. This is a passive
weight-history error bound, **not** an RMS-output convergence rate for the
self-consistent approximation. L2 history error also does not control the
endpoint errors in (14) without further regularity. Neither rate nor
efficiency is claimed uniformly in width, data complexity, or training time.

## 8. What this has and has not supplied

This gives the user's requested form for the learned history: per-neuron
forward/backward ODE states in both populations; explicit relaxation matrices;
rational homogeneous modes in a learning clock; and a condensed coupling M.
It also supplies a precise defect to study, rather than unknown closure
coefficients or a prescribed future trajectory.

Two obstacles remain to a full canonical compressed simulator:

* W2(0) is still needed when computing W2hat H1 and W2hat* Delta2. Keeping
  its full finite matrix costs quadratic storage/work; calling its population
  Gaussian action an oracle merely relocates that cost. A justified finite
  closure for this initialization-reuse action is still required.
* There are P coordinates per signal **per training sample**. A continuous
  input distribution or sample-independent complexity needs a separate
  input representation. Fixed input dimension alone does not supply it.

Even after resolving those two issues, useful small-P error and stability
under feedback must be proved or tested. The current construction is a
concrete, partially justified realization of the user's idea, not a claim
that the full hierarchy is efficient or that all of training necessarily
plateaus. It strengthens the prior generic-memory discussion by replacing
unknown encoder coefficients with exact formulas and displaying the remaining
errors. The previous caution about closure remains valid.
