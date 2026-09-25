# Response clocks for the history-moment closure

Theory-only continuation, 2026-09-25. The user asks whether an autonomous
clock can distribute changes of forward/backward responses evenly and provide
derivative bounds useful for chronological polynomial compression. This note
continues the explicitly assigned study; it does not start a training campaign
or change the existing solver. Root owns this synthesis and the README entry.

## Scope and inputs

The canonical object is a finite, bias-free tanh network with a fixed finite
dataset, all blocks trained by unhalved mean-square gradient flow, and the
positive constant block mobilities of docs/NOTATION.md. The concrete closure
has two hidden layers, retains the actual initialized W0 and its transpose,
and represents its learned increment by sample-wise history factors. General
response-clock statements apply at any fixed finite depth/width. No population,
width-uniform, successful-fitting, or all-time compression theorem is assumed.

Inputs read by root: this study's MOMENT_CONSTRUCTION.md,
RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md and MOMENT_INDEPENDENT_CHECK.md; the current
README and its corrections; docs/README.md, docs/NOTATION.md, and complete
sections 1–4 of docs/finite_dynamics.md. The user's supplied Legendre argument
is also an input. NIST DLMF 18.8 was checked for the polynomial differential
equation; the bounds below are derived here rather than imported from a
specialized approximation theorem. Scoped route reports list their own inputs.

Scientific distinction: a clock-dependent derivative bound can be proved by
construction. Efficient compression additionally requires control of total
clock length, the correct encoded signals, and closed-loop error propagation.

## 1. What the original clock removes

Write theta for all parameters, D for the positive definite constant mobility operator, M for
the number of samples, f(theta) in R^M for predictions, J=D_theta f, and

    r=f-y, rho=||r||_2/sqrt(M), V(theta)=-(2/M) D J^T r.

The existing clock is L=1+integral rho dt, not the change of rho. For any
smooth response map Psi(theta), on rho>0,

    dPsi/dL = -(2/sqrt(M)) D_theta Psi D J^T (r/||r||_2).

It removes the common residual magnitude from the gradient. It leaves the
response and prediction Jacobians and the residual direction. Thus small
loss is a useful activity proxy, but neither slow loss change nor this clock
alone implies a uniform response derivative bound.

The natural parameter-metric arclength speed is instead

    v_theta=||D^(-1/2) V||_2=sqrt(-d loss/dt).

This follows by substituting V=-D grad(loss) into the loss chain rule. The
finite energy identity gives integral_0^T v_theta^2 <= loss(0) and therefore
integral_0^T v_theta <= sqrt(T loss(0)). It does not give finite total length
as T tends to infinity.

## 2. Exact causal response arclength and its optimality

Stack any specified finite collection of current forward and backward
responses into Psi(theta), with fixed scales and a chosen norm ||.||_*.
Define

    v(theta)=||D_theta Psi(theta) V(theta)||_*,
    tau(t)=integral_0^t v(theta(s)) ds.

Then there is a 1-Lipschitz curve Y with Psi(theta(t))=Y(tau(t)). Indeed,

    ||Psi(theta(t2))-Psi(theta(t1))||_*
       <= integral_t1^t2 ||D_theta Psi V||_* dt
        = tau(t2)-tau(t1).

Equal clock readings therefore have equal responses. This defines Y even
across zero-speed intervals and proves its Lipschitz bound. On positive-speed
intervals the inverse chain rule gives ||dY/dtau||_*=1. The clock images of
those intervals have full measure in its range, proving unit speed almost
everywhere. In particular the reparameterized curve is absolutely continuous.
The construction uses current states and directional derivatives, not future
solutions. A constant response path has a zero-length clock and is handled
separately. This is a response-path parameterization, not automatically a
strictly invertible parameter clock through intervals in which only the
selected observables are constant.

For coordinate caps b_i>0, v=max_i |(D_theta Psi V)_i|/b_i gives
|dY_i/dtau|<=b_i. It is the pointwise smallest clock rate that can impose
these caps: differentiating any factorization through a b_i-Lipschitz path
gives |Psi_i_dot|<=b_i tau_dot. An RMS norm gives an RMS speed bound, not a
uniform bound for every neuron. A scalar clock preserves nonzero ratios of
coordinate velocities, so it cannot generally give every neuron the same
speed. A maximum monitor can impose simultaneous bounds, with clock length
that may depend on width and extreme neurons.

There is also an exact optimization statement in a Hilbert norm. For a
finite path and a nonnegative clock rate g, positive on the moving part,
let S=integral_0^T g dt
and x=tau/S. With v=||Psi_dot||_*,

    integral_0^1 ||dPsi/dx||_*^2 dx
       = S integral_0^T v^2/g dt
       >= (integral_0^T v dt)^2.

The inequality is Cauchy–Schwarz. Equality holds when g is proportional to
v on the moving path, with zero-speed intervals collapsed. Thus response
arclength minimizes the unweighted first-derivative energy after normalization
to a unit interval. It also attains the smallest possible essential maximum
speed, since total variation is a lower bound for that maximum on a unit
interval. This is not an optimality theorem for actual Legendre coefficient
tails, their weighted derivative energy, endpoint errors, or higher derivatives.
Multiplying g by a constant leaves the normalized curve exactly unchanged.

## 3. Length and approximation cannot be separated

Let ell_T=integral_0^T v dt. For a nonconstant arclength-parameterized curve,
F_T(x)=Y(ell_T x) has ||F_T'(x)||_*=ell_T almost everywhere. For P>=1,
let (F_T)_P denote its orthogonal projection onto modes k=0,...,P-1.
For a Hilbert norm, componentwise orthogonality of shifted Legendre polynomials gives

    ||F_T-(F_T)_P||_(L2) <= ell_T/sqrt(6 P(P+1)).

To verify the used inequality, the polynomial equation is
-(x(1-x)p_k')'=k(k+1)p_k. Integration by parts gives mutually orthogonal
derivatives in the weighted inner product and

    sum_(k>=1) k(k+1)||c_k||_*^2/(2k+1)
        <= integral_0^1 x(1-x)||F_T'||_*^2 dx.

Bessel's inequality proves this for absolutely continuous F_T with L2
derivative. Its tail k>=P is bounded by dividing by P(P+1); arclength then
gives integral x(1-x)||F_T'||^2=ell_T^2/6. The endpoint identity in the
existing orthogonal-moment route separately gives an O(ell_T/sqrt(P)) bound.
These are supplied-path projection statements, not closed-loop guarantees.

The total variation ell_infinity is invariant under continuous monotone
reparameterization. If it is infinite, no parameterization of the entire
ordered path on a compact interval can be absolutely continuous: an absolutely
continuous finite-dimensional path on a compact interval has variation at
most the integral of its derivative norm. If ell_infinity is finite,
arclength gives a Lipschitz extension to the finite terminal interval.
Therefore a finite all-time interval with controlled derivatives requires a
finite-variation theorem, which cannot be manufactured by a clock change.

The finite-width energy estimate ensures bounded parameters on every finite
physical-time interval. Smooth response maps have bounded derivatives on that
compact parameter region, giving finite ell_T for every finite T. This does
not supply an all-time, width-uniform or population bound. Task compatibility
alone supplies no such implication in this study. Smoothness of all orders
also does not follow from arclength: zero-speed points can create corners.

## 4. The actual histories depend on the clock

For a positive rate g(theta), set Ldot=g and L(0)=1. The exact physical
middle increment is represented in this coordinate using

    a_a=h_(1,a), q_a=r_a delta_(2,a), b_a=q_a/g,
    integral q_a h_(1,a)^T dt = integral b_a a_a^T dL.

The raw moment equations become

    m1_k_dot=g h1 -(g/L)[k m1_k+sum_(j<k)(2j+1)m1_j],
    m2_k_dot=r delta2 -(g/L)[k m2_k+sum_(j<k)(2j+1)m2_j].

The unweighted Legendre reconstruction retains its form. In particular one
must not replace both source terms by the new clock rate. Differentiation of
the histories gives

    da_a/dL = h_(1,a)_dot/g,
    db_a/dL = q_a_dot/g^2 - q_a g_dot/g^3,
    g_dot = D_theta g V.

Bounding h_dot/g and delta_dot/g alone is insufficient. For g=rho the
backward history contains the normalized residual direction r/rho; with
multiple samples, its derivative need not carry another residual factor.
One sample has fixed residual sign before reaching zero, which removes this
particular direction issue but not all response-growth issues.

For the closure's own dynamics there is a further implementation obligation:
its reconstructed middle derivative contains g. A monitor using its actual
response derivatives may define an implicit equation for g. An explicit
clock of the physical current state avoids a computational loop, but bounds
proved using the exact gradient field then need a separate check under the
closure's perturbed field. Neither issue affects the exact-network clock
theorems above. Section 7 gives an explicit alternative with cancellation.

## 5. A concrete regularizing clock for the encoded histories

On a region where, for a fixed sample and selected norms,

    ||h_dot||<=A rho, ||delta||<=D0,
    ||q_dot||<=B rho, |rho_dot|<=C rho, rho<=rho_max,

choose g=sqrt(rho)=loss^(1/4). Then

    ||da/dL|| <= A sqrt(rho_max),
    db/dL = q_dot/rho - q rho_dot/(2 rho^2),
    ||db/dL|| <= B + sqrt(M) D0 C/2.

Here |r_a|<=sqrt(M)rho gives ||q_a||<=sqrt(M)D0 rho. These are direct
derivative bounds for the correct encoded signals. The same first inequality
applies to raw backward responses when ||delta_dot||<=A_delta rho.

For fixed finite tanh networks these hypotheses hold on every finite physical
time interval: V/rho is bounded on compact parameter regions by the exact
gradient formula; r_dot=JV implies |rho_dot|<=||r_dot||/sqrt(M)=O(rho);
q_dot=r_dot delta+r D_theta delta V has the stated bound. Constants depend
on the architecture, width, fixed task, initialization, region and horizon.
An all-time bounded region would give all-time constants, but is an additional
hypothesis. Thus this is a proved finite-horizon regularization, not evidence
that the fourth-root clock is practically superior.

The rate sqrt(rho) is generally nonsmooth at the zero-residual set; the
derivative argument is on rho>0. A nonconstant smooth exact gradient flow
cannot reach a zero-residual equilibrium at finite physical time, by local
uniqueness applied at that equilibrium. A zero-residual initial state is
stationary and is assigned a frozen clock and zero backward history.

The scoped history report also supplies a conservative global state-envelope
construction for finite tanh networks: multiply sqrt(rho) by a sufficiently
large power of 1+||theta||_2^2. Polynomial growth bounds for the finite
response maps and their first derivatives give derivative caps without an
assumed bounded parameter orbit. Its fully stated constants and proof are in
RESPONSE_CLOCK_HISTORY_CHECK.md. Such a clock can be extremely long and
width dependent; its bounded derivative is not an efficiency theorem.

The slower-vanishing rate sqrt(rho) illustrates the tradeoff: even when
integral rho dt is finite, integral sqrt(rho) dt need not be finite. The
scalar example rho(t)=(1+t)^(-2) proves this integrability distinction; it is
not asserted here to be a realized neural trajectory.

## 6. Genuine jumps require a separate treatment

The existing artificial prefix has a=h(0), b=0, whereas actual b(0) is
generally nonzero. It is not globally absolutely continuous even for tanh.
A continuous clock cannot remove this jump. One exact alternative is a
length-one prefix with a=h(0), b=b(0), followed by subtraction of the known
constant matrix b(0)h(0)^T from the reconstructed history integral. The
histories are then continuous at the join and retain their derivative bounds;
the extra constant rank-one term cancels the artificial contribution exactly.
At order P this is a different finite closure, with at most one additional
rank-one term per sample, and requires its own accuracy checks. The physical
infinite-history target remains unchanged.

Similarly, for nonsmooth activations such as ReLU, a backward response may
jump when a gate changes. A regular time change cannot make that response
continuous. The smooth-response theorems here are stated for tanh; bounded
variation or piecewise approximation is needed for actual jumps.

## 7. A response-arclength variant with a separate integration measure

One can keep the existing learning measure dmu=rho dt and normalized source
u_a=r_a delta_a/rho, but use a different coordinate tau_dot=g for the
polynomial arguments. This removes g from the definition of the histories.
It changes the projection: Legendre polynomials are no longer orthogonal
for the new measure. Their current Gram matrix must be retained.

Let L=1+tau, p=(p_0,...,p_(P-1))^T, e=p(1)=(1,...,1)^T, and T satisfy
x p'=T p, with diagonal k and lower entries 2j+1. Store

    H_a=integral h_a p^T dmu, U_a=integral u_a p^T dmu,
    G=integral p p^T dmu.

In these integrals p is evaluated at xi/L(t), with historical actual
coordinate xi=1+tau(s); the prefix occupies 0<=xi<=1.

The prefix uses uniform dmu on [0,1]. For the original zero-source prefix,
H_a(0)=[h_a(0),0,...], U_a(0)=0, G(0)=diag(1/(2k+1)). Then

    H_a_dot=rho h_a e^T-(g/L)H_a T^T,
    U_a_dot=r_a delta_a e^T-(g/L)U_a T^T,
    G_dot=rho ee^T-(g/L)(T G+G T^T).

The weighted-projection cross product is S_a=U_a G^(-1)H_a^T. The prefix
ensures G is positive definite for every finite L and fixed P, because a
nonzero polynomial cannot vanish on a nontrivial prefix interval. It does
not give uniform conditioning. Define hp_a=H_a G^(-1)e and up_a=U_a G^(-1)e.
The product and inverse rules give

    S_a_dot=rho[u_a hp_a^T+up_a h_a^T-up_a hp_a^T].

All dilation terms cancel. Thus W_hat_dot=-(2/(nM))sum S_a_dot is independent
of the clock rate at a fixed current moment state. Compute this derivative,
then the canonical outer derivatives, forward/backward response derivatives,
rho_dot and u_dot, and finally

    g=rho+||stack of scaled h_dot and u_dot||_*.

This is explicit on rho>0 and bounds both h and u derivatives in the new
coordinate by the chosen caps when the norm dominates each scaled block
(for example stacked Euclidean norm or the maximum of block norms).
It retains an exact middle-velocity defect

    E=(2rho/(nM))sum_a (u_a-up_a)(h_a-hp_a)^T.

For g=rho one has G=L diag(1/(2k+1)), and the original method is recovered.
The matching-prefix correction of section 6 can also be used: initialize
U_a=[u_a(0),0,...] and replace S_a by S_a-u_a(0)h_a(0)^T in the reconstruction.
This weighted
variant is a derived possible solver, not an implemented or empirically
validated replacement. Its measure differs from the uniform Legendre measure,
so the original spectral error bounds cannot be transferred without proof.
Finite total coordinate length, residual-direction regularity, Gram
conditioning and closed-loop tracking remain separate obligations. The full
scoped algebraic check is RESPONSE_CLOCK_WEIGHTED_CHECK.md.

## Claim status and next obligation

Exact/proved for the stated finite smooth system: causal response arclength,
coordinate caps and first-derivative-energy optimality; the arbitrary-clock
history equations; finite-horizon fourth-root-loss derivative bounds; the
weighted Gram reconstruction and derivative cancellation. Conservative
finite-dimensional state-envelope bounds have their explicit assumptions and
proof in the history report. These are study results, not promoted material.

Open: a practically short clock with width-uniform total variation, useful
population control, a selected finite-closure accuracy/conditioning guarantee,
and superiority of any clock on the existing benchmarks. Input compatibility
by itself has not been shown to imply these properties. No experiment is
authorized or run in this continuation. The next mathematical bottleneck is
joint control of history regularity and accumulated clock length, followed by
propagation of the resulting closure defect.
