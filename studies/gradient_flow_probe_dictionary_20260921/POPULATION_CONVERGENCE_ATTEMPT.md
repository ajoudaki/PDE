# Population order-convergence attempt

Continuation explicitly requested by the user, 2026-09-21. This is theory in
the existing derivative-dictionary study. No experiment, maintained-code
change, promotion, or Git transaction is part of this attempt.

## Contract and routes

The target is the actual population, zero-readout, two-hidden-layer tanh
network and its frozen derivative dictionaries from two fixed normalized axis
probes. The dictionary collects symbolic-label coefficients of tensor factors
in the learned W^(2) increment, as in the p1--p7 specifications. It compresses
the entire initial middle operator, uses the true adjoint and canonical
gradient flow, and uses eta_p=1/[1024(p+1)^2]. First-layer and readout fields
continue to train. The natural all-order continuation retains all prior raw
columns at their original scales. Computed finite-order population identities
are not assumed to imply convergence of a temporal power series.

For a single nonzero input x and label y, seek convergence to the full dense
population prediction, uniformly over all physical t>=0 and passive inputs
on the same circle (or ball). Fixed compact physical-time convergence would
be a weaker but substantive result. Population width is fixed at infinity
before p tends to infinity. Success requires identifying the limit with the
dense model, not merely a limit within the selected dictionary spaces.
No sample-aligned probes, added seeds, product completion, orthogonal metric
at finite p, retained dense background, or trajectory-dependent coefficients
may be silently substituted. A changed construction is a separate claim.

The prior all-time certificate is SINGLE_SAMPLE_GLOBAL_BOUND.md. This attempt
must prove its approximation source becomes small, or establish convergence
by another mechanism; restating its conditional bound does not solve the task.

Independent scoped routes, each starting without inherited discussion:

| Route | Assigned mechanism | Owned report | Outcome |
|---|---|---|---|
| population_density_route | Gaussian span/controllability and coefficient structure | POPULATION_DENSITY_ROUTE.md | finite innovation results; all-order density open |
| population_obstruction_route | invariants and an actual population counterexample | POPULATION_OBSTRUCTION_ROUTE.md | projected-limit proof and kernel falsifier; no actual counterexample |
| population_analytic_route | population derivative-span uniqueness, analytic/localized methods | POPULATION_ANALYTIC_ROUTE.md | explicit analytic-route counterexample; actual model unresolved |
| root | ridge limits and identification of the limiting dynamics | this file | projected-limit convergence proved; dense identification open |

Each scope contains the current study's stated derivations/specifications and
the relevant established model, but no other study or another route's draft.
The first route round is bounded to concrete mathematics, followed by synthesis
and a separate check of any candidate claim. No GPU budget is consumed.

## A ridge-limit lemma independent of Gram conditioning

Let H be either real population Hilbert space. For each p let R_p:R^{k_p}->H
synthesize the raw dictionary columns, with literal nested prefixes. Write
V=closure(union_p ran R_p) and P for orthogonal projection onto V. Define

    Q_p=R_p(R_p*R_p+eta_p I)^(-1)R_p*,  eta_p>0, eta_p->0.

Then Q_p converges strongly to P. No uniform lower bound on the nonzero
eigenvalues of the growing Gram matrices is needed.

Proof. For any v in H, minimizing over coefficients a gives

    <v,(I-Q_p)v>
      = min_a (||v-R_p a||^2 + eta_p ||a||^2).                 (1)

Indeed completing the square gives the minimizer
(R_p*R_p+eta_p I)^(-1)R_p*v and the displayed minimum. The Q_p are positive
self-adjoint contractions, vanish on V-perp, and have range in V.
If v=R_m a and p>=m, append zeros to a in (1). Thus

    ||(I-Q_p)v||^2 <= <v,(I-Q_p)v> <= eta_p ||a||^2.           (2)

The first inequality uses 0<=I-Q_p<=I. The bound tends to zero for every
fixed finite-column combination. For general v in V, approximate it by such
a combination and use ||I-Q_p||<=1. On V-perp, Q_p=0. This proves strong
convergence to P on H. The same contraction bound and a finite epsilon-net
give uniform convergence on each compact subset of H.

Consequently the actual initialized middle operators

    B_p=Q_(2,p) W^(2)(0) Q_(1,p)

converge strongly, along with their adjoints, to

    B_infinity=P_2 W^(2)(0) P_1.                              (3)

For example the difference applied to a fixed v is

    Q_(2,p) W0 (Q_(1,p)-P_1)v +(Q_(2,p)-P_2)W0 P_1 v.

The first term tends to zero by bounded W0 and the contraction Q_(2,p);
the second uses strong convergence on the fixed vector W0 P_1 v.
Repeat with the actual adjoint. Uniform
operator bounds are ||B_p||,||B_infinity||<=||W0||.

This resolves the ridge-to-projection limit for a nested continuation. It
does not identify P_2 W0 P_1 with the required dense initialized actions.
Nor does finite-list nesting alone identify the closed spaces V_1,V_2.

## Convergence to the closed-span dynamics

This result identifies what the sequence converges to without assuming that
the answer is the dense network. Use normalized unit training input x and
passive inputs ||u||<=1; the physical input in canonical d=2 notation is
sqrt(2)x. Half squared loss fixes the physical clock; unhalved loss rescales
it by two. Assume the stated Gaussian initialized fields and bounded W0 on
the established population carrier. A nested all-order continuation consists
of well-defined finite L2 raw lists and eta_p->0 as above.

Define a limiting projected model, only for analysis, by

    W_infinity=B_infinity+K_infinity, B_infinity=P_2 W0 P_1,
    dK_infinity/ds=sign(y)(P_2 Delta_infinity) tensor(P_1 H1_infinity),

with the actual first-layer/readout equations and their shared initial values,
including W3(0)=0. The finite-p model has precisely the same equations with
P_l replaced by its actual ridge Q_l,p. The infinite projected model need
not be a finite compression and is not a proposed substitute experiment.

**Theorem (limit identification within the chosen spaces).** For every fixed
physical T<infinity, the p-model converges uniformly on [0,T] and the passive
unit input ball to this limiting projected model. If its initial upper energy

    q_infinity=||tanh(B_infinity H1(0,x))||_2^2

is positive, the prediction convergence is uniform over all physical t>=0.
For training at either fixed axis probe, q_infinity>0 is proved below. No
identity between this limit and the full dense model is asserted.

Proof. Let Y=|y|. If y=0 both zero-readout models predict zero identically,
so take Y>0 and sigma=sign(y). All positive contractions, including the
P_l, obey the existence and elementary estimates in
SINGLE_SAMPLE_GLOBAL_BOUND.md, sections 1--2. On any fixed residual-time
interval [0,S], their readouts satisfy |W3|<=S pointwise, their increments
have HS norm <=S^2/2, and their middle operators have norm <=M=||W0||+S^2/2.
Put g=W1 x, X=F(g) with F(z)=z/2+sinh(2z)/4. Then

    X_s=sigma W*Delta,
    c_s=sigma H2,
    K_s=sigma(Q_2 Delta) tensor(Q_1 H1).

For the limiting system replace Q_l by P_l. Both F^{-1} and
tanh composed with F^{-1} are 1-Lipschitz. The initial X,K,c agree. The
initial perpendicular first-row component is fixed under one-sample
training; hence first-hidden differences at all ||u||<=1 are bounded by
the X difference at the training input.

On the fixed limiting residual-time curve define

    a_p=sup_(s<=S,||u||<=1) ||(B_p-B_infinity)H1_infinity(s,u)||_2,
    b_p=sup_(s<=S) ||(B_p*-B_infinity*)Delta_infinity(s,x)||_2,
    d_p=sup_(s<=S) ||(Q_2,p Delta_infinity) tensor(Q_1,p H1_infinity)
                    -(P_2 Delta_infinity) tensor(P_1 H1_infinity)||HS.

All three tend to zero. The argument sets are compact L2 sets: the curves
are continuous, and passive H1 is jointly continuous in s,u on a compact
finite-dimensional input ball. Strong convergence and uniform operator
norm bounds give uniform action convergence on these sets. The rank
difference in d_p is bounded by the sum of one-factor errors times the
bounded norms of the other factors.

Write epsilon_p=a_p+b_p+d_p and let e_p be the sum of the X, HS increment,
and readout differences. Subtract the two vector fields, evaluating all
action/filter forcing on the fixed limiting curve. For z=W H1,

    ||z_p-z_infinity||_2 <= M||X_p-X_infinity||_2
                            +||K_p-K_infinity||HS+a_p,
    ||Delta_p-Delta_infinity||_2
         <=||c_p-c_infinity||_2+2S||z_p-z_infinity||_2.

The X derivative error is bounded by

    2SM^2 e_X +(2SM+S)e_K +M e_c +2SM a_p+b_p.

For the middle derivative, use contraction of both Q factors and then
subtract the limit-filtered rank. Its error is bounded by

    (S+2SM)e_X +2S e_K +e_c +2S a_p+d_p.

The readout derivative error is at most M e_X+e_K+a_p. Consequently, with
L=2+2M+4S+8SM+4SM^2 independent of p,

    e_p'<=L e_p+L epsilon_p, e_p(0)=0,
    sup_(s<=S) e_p(s)<=(exp(LS)-1)epsilon_p ->0.               (4)

The output at the same residual time obeys

    sup_(s<=S,||u||<=1)|f_p(s,u)-f_infinity(s,u)|
      <=[ (1+S(M+1))(exp(LS)-1)+S ]epsilon_p =: E_p ->0.      (5)

The limiting and finite-p signed training predictions are nondecreasing
in residual time: their derivatives are their nonnegative canonical
gradient energies, including the positive filtered middle energy. Their
physical clocks solve s'=Y-sigma f(s,x), start at zero, and satisfy
0<=s(t)<=Yt. This follows from the nonnegative residual solving
r'=-K(s(t))r and f(0,x)=0; on a finite segment its bounded nonnegative
kernel excludes residual sign crossing. If d=s_p-s_infinity, subtracting
the two clocks and using monotonicity of the limiting signed prediction
gives the upper absolute derivative (|d|)'<=E_p. Thus |d(t)|<=T E_p on
[0,T]. Choose S=YT+1. All passive feature-time prediction speeds are
bounded by J=1+S^2(1+M^2). Equation (5) then gives the uniform physical
time/output bound (1+JT)E_p, proving compact-time convergence.

If q_infinity>0, strong convergence B_p H1(0,x)->B_infinity H1(0,x)
and the Lipschitz tanh map imply q_p->q_infinity. For all sufficiently
large p, q_p>=q_infinity/2. The positive-readout-norm argument in the
prior proof gives both physical clocks <=S=2Y/q_infinity. On this one
fixed residual segment the limiting signed prediction has derivative
at least q_infinity. The clock difference therefore satisfies

    (|d|)'<=-q_infinity|d|+E_p,
    sup_t |d(t)|<=E_p/q_infinity.

Together with the passive speed bound J this proves

    sup_(t>=0,||u||<=1)|f_p(t,u)-f_infinity(t,u)|
      <=(1+J/q_infinity)E_p ->0.                              (6)

For an axis sample x=e_a, H1(0,x)=h_a belongs to V_1 from the first
nonzero increment list.
Also U_aa=tanh(Y_a)sech^2(Y_a) belongs to V_2, with Y_a=W0 h_a a
nondegenerate centered Gaussian. Therefore

    <U_aa,B_infinity h_a>
     =<U_aa,W0 h_a>=E[Y_a tanh(Y_a)sech^2(Y_a)]>0.

The integrand is positive except at zero and is integrable, so
B_infinity h_a is nonzero in L2. Injectivity of tanh at zero gives
q_infinity>0. This proves the unconditional all-time projected-limit
statement for either axis training sample. It does not rotate the fixed
dictionary to a general training sample.

## The exact remaining identification question

The projected limiting middle has background P_2 W0 P_1 and update
(P_2 Delta) tensor(P_1 H1). To identify its flow with the dense one it
would suffice to prove, along the dense residual-time curve and passive
input ball,

    (P_2 W0 P_1-W0)H1(s,u)=0,
    (P_1 W0*P_2-W0*)Delta(s,x)=0,
    (P_2 Delta(s,x)) tensor(P_1 H1(s,x))
                              =Delta(s,x) tensor H1(s,x).    (7)

These statements have not been proved for the derivative-only spaces.
They hold for the larger complete word construction in the established
book under its stated dynamical assumptions, but its Fourier/product/action
completion is not present in the tested derivative lists. The ridge lemma
is also a specialization of the book's filter argument to any nested raw
list, not a newly established density theorem.

Only sufficient action identities are asserted in (7). Equality of output
trajectories could conceivably occur without full state/action equality;
failure to prove (7) is not a counterexample to output convergence.

## Checked result and remaining gap

POPULATION_CONVERGENCE_CHECK.md records the complete independent scoped
check of the ridge and projected-limit argument. The checking agent derived
its own route before receiving this proof; its report distinguishes that
independent work from the subsequent comparison. This is internal checking,
not promotion. The root read that entire check and the three route reports.

The density route proves that the initial upper Gaussian seeds are measurable
from the four first upper factors, but cannot be recovered linearly from the
p3 upper span. A positive conditional-innovation bound persists even under
arbitrary coefficient enrichment that remains linear in the first response
fields. The actual higher dictionary also has nonlinear products and further
queries, so that bound does not disprove its all-order density.

The analytic route gives a self-contained example F(s)=tanh(s G^3), G Gaussian,
with a bounded test orthogonal to every initialized derivative but not to the
later trajectory. Finite-width derivative spans for this example are complete,
so fixed-width analyticity also cannot justify exchanging width and order.
This is an obstruction to a general proof principle, not a counterexample to
our canonical network. The root checked the explicit Gaussian integrals and
the distinction from the specified dynamics.

The obstruction route supplies a genuine falsifier for the target: a nonzero
gap between the dense initial test kernel and the kernel of B_infinity gives
a fixed positive-time prediction gap, with a uniform Taylor remainder that
avoids exchanging derivatives and p limits. No such gap was proved for the
actual all-order Gaussian dictionary.

**Convergence to the full dense population remains open.** This attempt proves
the sequence converges to its projected limit on compact physical intervals,
and uniformly for all time when its initial training energy is positive
(proved at either fixed axis sample). It does not identify that limit with
the dense network, prove an order rate, or supply an all-order density theorem.
The precise open mechanism is cancellation of the successive Gaussian
innovations while approximating the required forward/reverse/update fields
by actual linear combinations of the retained columns. Merely approximating
their conditional means cannot complete that argument.

No experiment or GPU run occurred. Source/dictionary definitions, empirical
results, maintained book/code, shared Git index and the remaining compute
allowance were unchanged.
