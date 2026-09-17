# Balanced collision configurations and necessary potential growth

2026-09-17. Author proof, exact canonical p=1 closure. No experiment.
Scientific inputs: the complete exact initialization and metric in
docs/observable_p1.md; docs/global_nonlinear.md C.4.7.9.3--4 and C.4.7.10 D.3;
docs/NOTATION.md. No other study supplies a premise.

## 1. Exact model and the questions being distinguished

Put u(theta)=(cos(theta),sin(theta)), x(theta)=sqrt(2)u(theta).
The data consist of probabilities mu_i>0 summing to one and labels y_i=+/-1,
with sum mu_i y_i=0. The characteristic state is X=(w,c,M), on the two
canonical frozen mark spaces, initially X0=(g,0,D). Its metric is

    ||delta X||^2=E1|delta w|^2+E2|delta c|^2+||delta M||F^2.

The law state is (Gamma1,Gamma2,M), retaining all (b1,g,w) and (b2,c)
correlations. The initialized p=1 dictionary is precisely the inverse-lower-
Cholesky dictionary with eta=1/4096 in docs/observable_p1.md, including the
reverse-source contribution. Its two feature maps are contractions; write
B_l=ess sup |b_l|<infinity, d0=||D||op<=2. No orientation of the dictionary
is changed with the data.

For every direction u define

    a(u)=E1[b1 tanh(w.u)], Z(u)=b2^T M a(u), H(u)=tanh Z(u),
    d(u)=E2[b2 c sech^2 Z(u)], Q(u)=b1^T M^T d(u), f(u)=E2[c H(u)].

The prediction gradient in the stated physical metric is

    grad f(u)=(sech^2(w.u) Q(u)u, H(u), d(u)a(u)^T).

Indeed variation of M gives d^T(delta M)a; variation of w gives the
actual M^T, and variation of c gives H. Thus the canonical equations are

    X'=-2 sum_i mu_i (f(u_i)-y_i) grad f(u_i),
    L=sum_i mu_i(f(u_i)-y_i)^2,
    L'=-||X'||^2, L(0)=1.                                      (1)

Fixed-order global finite-time existence, continuity and this dissipation
identity hold even for close or coincident data by the cited state/energy
proof. The lower estimates below do not assume eventual fitting.

Write tau(ell)=inf{t>=0:L(t)<=ell}, with inf empty=infinity, for 0<ell<1.
Three different questions are retained: epsilon->0 in tau(1-epsilon) for
fixed data; degeneration of the data at a fixed ell; and ell->0 for fixed
data. An initial slope cannot substitute for the latter two.

## 2. A general physical escape-time inequality

Define the signed prediction correlation and squared prediction norm by

    A(X)=sum_i mu_i y_i f_X(u_i), B(X)=sum_i mu_i f_X(u_i)^2.

The exact identity

    1-L(X)=2A(X)-B(X)<=2A(X)                               (2)

is the useful bridge from data cancellation to time. Suppose that on the
physical ball ||X-X0||<=R one has A(X)<=b_R and 2b_R<1-ell, with b_R>0.
If the target is reached, the continuous trajectory must first exit that
ball, at a time T_R<=tau(ell). At that time (1)--(2) give

    integral_0^T_R ||X'||^2 =1-L(X(T_R))<=2b_R.

The Cauchy--Schwarz bound on displacement then gives

    R^2<=T_R integral_0^T_R ||X'||^2<=2b_R T_R,
    tau(ell)>=R^2/(2b_R).                                 (3)

If the target is never reached, the same claimed lower bound is automatic.
If b_R=0, no positive-loss improvement can occur inside the ball and its
exit would require positive energy while the available energy is zero;
the trajectory cannot exit. This case has tau(ell)=infinity.

This is a nonlinear full-state estimate. It does not freeze a kernel or
assume a bound on the future tangent Gram. The small available energy
before escape is essential: using only integral ||X'||^2<=1 would miss
the stronger delay in (3).

There is also a general current-state formulation. For a center X with
L(X)>ell, let E_R(X)=L(X)-inf_{||Y-X||<=R} L(Y). If
0<E_R(X)<L(X)-ell, restarting (1) at X proves that remaining hitting time
is at least R^2/E_R(X). Its supremum over such R is a static landscape
quantity determined by the present state and fixed data, without a future
endpoint. No decay law for that quantity is asserted here.

## 3. Uniform input-derivative bounds on a physical ball

On ||X-X0||<=R set W_R=sqrt(2)+R and M_R=d0+R. Then
||w||2<=W_R, ||c||2<=R and ||M||op<=M_R. A prime in this section denotes
an angular input derivative, not training time. Since |u'|=|u''|=1,

    ||a'||<=W_R,
    ||a''||<=B1(2 W_R^2+W_R).                            (4)

The first estimate uses contraction of the b1 feature map. For the second,

    a''=E1 b1[tanh''(w.u)(w.u')^2+tanh'(w.u)(w.u'')],

and |tanh''|<=2. Only second moments of w are used. Differentiation twice
under the integral follows from the integrable bound 2|w|^2+|w|.
The upper map obeys

    ||Z'||2<=M_R W_R, ||Z'||infty<=B2 M_R W_R,
    ||Z''||2<=M_R B1(2 W_R^2+W_R).

Consequently

    |f'|<=R M_R W_R=:P1(R),
    |f''|<=R[2 B2 M_R^2 W_R^2
                    +B1 M_R(2 W_R^2+W_R)]=:P2(R).         (5)

In particular, with fixed finite initialization-dependent constants

    K1=(d0+1)(sqrt(2)+1),
    K2=2B2(d0+1)^2(sqrt(2)+1)^2
             +B1(d0+1)[2(sqrt(2)+1)^2+sqrt(2)+1],

we have Pj(R)<=Kj R for 0<R<=1. These statements concern arbitrary
physical states with the prescribed mark marginals; they do not require
an L-infinity bound on w-g or an input covariance lower bound.

## 4. Two explicit balanced difficult families

### 4.1 Opposite-label pair

Use angles theta0-delta and theta0+delta, weights 1/2 each and labels -1,+1.
For 0<delta<pi/4 the two inputs are distinct and non-antipodal. Then

    A=[f(theta0+delta)-f(theta0-delta)]/2,
    |A|<=delta P1(R)                                     (6)

on the ball. Thus for each fixed 0<ell<1, and all sufficiently small delta,

    tau_pair(ell)>=1/(2K1 delta).                         (7)

More generally, for every 0<epsilon<1 choose
R=min(1,epsilon/(4K1 delta)). Then 2b_R<=epsilon/2, so (3) gives

    tau_pair(1-epsilon)
      >=min{1/(2K1 delta), epsilon/(8 K1^2 delta^2)}.        (8)

No input reflection hypothesis is used for these lower bounds.

### 4.2 Positive endpoints and a negative midpoint

Use the three distinct angles theta0-delta, theta0, theta0+delta, labels
(+1,-1,+1), and probabilities (1/4,1/2,1/4). Total mass of each class is
exactly one half. This realizes the user's weighted three-input option.

Here

    A=[f(theta0-delta)-2f(theta0)+f(theta0+delta)]/4.

For a twice differentiable function, the numerator equals
integral_(-delta)^delta (delta-|s|) f''(theta0+s) ds. Since the triangular
weight has integral delta^2, (5) gives

    |A|<=delta^2 P2(R)/4.                                (9)

Therefore, whenever K2 delta^2/2<1-ell, (3) with R=1 gives

    tau_triple(ell)>=2/(K2 delta^2).                      (10)

Uniformly for 0<epsilon<1, choose
R=min(1,epsilon/(K2 delta^2)). The energy before exit is at most
K2 R delta^2/2<=epsilon/2. Thus

    tau_triple(1-epsilon)
      >=min{2/(K2 delta^2), 2epsilon/(K2^2 delta^4)}.       (11)

These are exact lower bounds for the full nonlinear physical flow. Individual
hidden distances may either increase or decrease. For the axis-centered
triple, sufficiently small positive delta gives independent initialized
upper features and hence representable labels; Section 7 proves this without
assuming that training freezes those features. Actual convergence for this
triple is not proved here, and (10) remains valid if its hitting time is infinite.

The first moments of the ANGULAR signed weights vanish in (9), while their
second moment is nonzero. This is why the same radius of hidden-state motion
has only order delta^2 energy available, instead of order delta in (6).
Both families have minimum angular spacing comparable to delta; the constants
do not depend on theta0. The bounds do not prove that triple training is always
slower than pair training: a lower bound alone cannot compare two true times.

## 5. Exact initial slopes and higher cancellation orders

For any fixed finite law, c0=0 gives d0(u)=0, so initially only the readout
moves. Put U0=sum_i mu_i y_i H_0(u_i). Equation (1) gives exactly

    c'(0)=2U0, w'(0)=0, M'(0)=0,
    -L'(0)=4||U0||2^2.                                  (12)

If U0!=0, differentiability and strict initial decrease imply

    tau(1-epsilon)=epsilon/(4||U0||2^2)+o(epsilon)
                  as epsilon->0 for THIS FIXED DATASET.  (13)

For example, smoothness of the initialized feature curve in population L2
gives for the pair and triple at a fixed center

    U0,pair=delta H_0'(theta0)+O_L2(delta^3),
    U0,triple=delta^2 H_0''(theta0)/4+O_L2(delta^4).        (14)

Thus the corresponding initial dissipation orders are delta^2 and delta^4
when the displayed derivatives are nonzero. Higher Gaussian moments needed
in these INITIALIZED derivatives exist. They are not assumed bounded
uniformly on a later arbitrary physical ball.

Here is an exact hierarchy at any fixed sample count N=r+1. Use

    theta_j=theta0+(j-r/2)delta, j=0,...,r,
    mu_j=2^(-r) binomial(r,j), y_j=(-1)^j.                 (15)

The positive and negative masses are both 1/2 by (1-1)^r=0. The r-fold
finite-difference identity, obtained by applying the fundamental theorem
of calculus r times, gives

    U0=(-1)^r 2^(-r) delta^r H_0^(r)(theta0)
                                         +o_L2(delta^r),
    -L'(0)=4^(1-r) delta^(2r)||H_0^(r)(theta0)||2^2
                                         +o(delta^(2r)). (16)

Every derivative is justified by dominated differentiation of the exact
initialized population integrals; its bound is a polynomial in |g| with
fixed bounded feature coefficients. The Gaussian law has every such moment.

For each r there exists a center theta0 with the displayed norm positive.
Indeed H_0 is a nonzero smooth periodic Hilbert-valued curve, and
H_0(theta+pi)=-H_0(theta). Its nonzero value on the first coordinate axis
is verified in Section 7. If its rth derivative vanished everywhere, repeated
integration would make it a polynomial in theta; periodicity makes it constant
and antipodal oddness makes that constant zero, a contradiction. This existence
statement does not identify one universal center for all orders.

The cancellation order r=N-1 is MAXIMAL among nonzero signed weights on N
distinct FIXED angular offsets in a single-scale cluster. If their moments
through degree N-1 all vanished, the Vandermonde matrix would annihilate the
weight vector. Its determinant is the nonzero product of pairwise offset
differences, forcing every weight to vanish. The binomial construction attains
cancellation of every smaller degree. This is an extremal moment statement,
not a classification of globally slowest nonlinear trajectories.

For r>2 we do NOT infer tau(ell)>=c delta^(-r) from (16). A physical L2
ball controls input derivatives only through order two by (4)--(5); it
does not control arbitrary higher row moments. Furthermore the parameters
move during the long initial phase. A high-order initial Taylor coefficient
is therefore insufficient for such a long-time inference. Formula (13) also
cannot be used with epsilon fixed while delta->0.

## 6. Necessary growth of a common-rate potential

Suppose a candidate is finite at every admitted initialization and satisfies,
on the actual initialized trajectories,

    Phi(t)<=exp(-lambda t)Phi(0),
    L(t)<=C Phi(t)^alpha,                                 (17)

where lambda,C,alpha>0 are fixed independently of the data. Then necessarily

    tau(ell)<=lambda^(-1) log[Phi(0)/(ell/C)^(1/alpha)],
    Phi(0)>=(ell/C)^(1/alpha) exp(lambda tau(ell)).          (18)

One can prove this without presuming a finite hitting time: for every t below
it, ell<L(t)<=C Phi(0)^alpha exp(-alpha lambda t). Let t increase to the
hitting time, or to infinity. In the latter case a finite Phi(0) is impossible.

For a fixed ell, (7) and (10) consequently force

    Phi_pair(0)>=(ell/C)^(1/alpha) exp(lambda/(2K1 delta)),
    Phi_triple(0)>=(ell/C)^(1/alpha) exp(2lambda/(K2 delta^2)), (19)

for all sufficiently small delta. In particular polynomial divergence in
inverse separation cannot suffice for a COMMON exponential rate and a fixed
power comparison. This is a necessary essential singularity, not a proved
sufficient order. A geometry-dependent rate can encode the difficulty instead;
that is a different normalization of the proposed result.

For a continuous strictly increasing h with h(0)=0 replacing C z^alpha,
the same argument gives Phi(0)>=h^(-1)(ell) exp(lambda tau(ell)). Thus the
fixed-threshold essential-singularity conclusion does not require a power
comparison. Interpretation of the small-loss tail DOES depend on h.

Even an upper bound on tau would not bound an arbitrary candidate's initial
value: multiplication by any data-dependent factor a(data)>=1 preserves
the same decay inequality and loss upper bound in (17). Nor do the necessary
lower bounds construct a potential. A minimal normalized certificate or
a specified functional class is needed before asking for its exact growth.

There is a second, separate test. Equation (17) forces

    liminf_(t->infinity) [-log L(t)]/t >=alpha lambda.      (20)

A large finite initial prefactor can accommodate a long delay, but cannot
repair a smaller eventual exponential exponent. We have NOT proved that the
actual terminal exponents vanish along the triple family, so (20) is a
necessary test, not a no-go theorem for its common-rate potential. With a
general slowly vanishing h, exponential Phi need not imply exponential loss.

## 7. The difficult triple is representable in this exact dictionary

This verifies absence of a finite-feature capacity obstruction for the
axis-centered triple; no trained convergence is inferred. Use the scalar
initialization constants of docs/observable_p1.md, renamed only to avoid
conflicts with current c and input angle:

    h=tanh G, v=E h^2, Xi~N(0,v), Z=tanh Xi,
    tau=E Z^2, alpha=1-tau, zeta~N(0,tau),
    k=tanh(zeta+alpha h), s=E k^2, beta=E h k, gamma=1-s,
    Rh=sqrt(v+eta), Rk=sqrt(s+eta-beta^2/(v+eta)),
    RZ=sqrt(tau+eta), eta=1/4096,
    Dh=alpha v/(Rh RZ),
    Dk=[alpha beta eta/(v+eta)+tau gamma]/(Rk RZ).

All Rh,Rk,RZ,Dh,Dk,beta are positive. For beta, the conditional mean of k
given h is odd and strictly increasing, so h E[k|h]>0 off h=0. The other
claims follow directly from the displayed positive variances and gates.

For two unit-variance joint Gaussian variables (G,V) with correlation r,
let A(r)=E[tanh G tanh V] and B(r)=E[k tanh V], where zeta is independent
of (G,V). Define

    kappa(r)=Dh A(r)/(Rh RZ)
             +Dk[B(r)-beta A(r)/(v+eta)]/(Rk RZ).          (21)

Computing D a_0(u) using the exact two nonzero initialized bands gives

    H_0(u)=tanh[Z1 kappa(u1)+Z2 kappa(u2)].                (22)

This calculation retains the joint (g,k) correlation and the tau gamma
reverse contribution. It is not a rotation-invariant dictionary assumption.

The functions A,B,kappa are odd, continuous on [-1,1], and real analytic on
(-1,1). Here is a direct analytic justification rather than an imported
kernel expansion. Write their expectations against the bivariate Gaussian
density with covariance [[1,r],[r,1]], first averaging k over zeta. The two
remaining factors are bounded. In a sufficiently small complex disk around
any real r in (-1,1), the determinant stays nonzero and the real part of the
inverse covariance stays positive definite. The density and its complex
derivatives are dominated on smaller disks by a fixed integrable Gaussian
times polynomials. Its integral is therefore analytic by its locally uniformly
convergent power series (equivalently differentiation under the integral).
Oddness follows by negating V or the first Gaussian with its reverse noise.
Continuity at +/-1 follows by coupling V=rG+sqrt(1-r^2)G' and bounded convergence.

At r=1, A(1)=v and B(1)=beta, so

    kappa(1)=Dh v/(Rh RZ)
                +Dk beta eta/[(v+eta)Rk RZ]>0.            (23)

Hence kappa is not identically zero. Its analytic series at zero has a first
nonzero coefficient of a finite odd order m. (If every coefficient vanished,
analytic continuation along overlapping real intervals would contradict
(23).) Thus kappa(r)!=0 for every sufficiently small positive r. No claim
that m=1 is needed in this proof.

For the inputs u(-delta),u(0),u(delta), their coefficient vectors in (22) are

    v_-=(kappa(cos delta),-kappa(sin delta)),
    v_0=(kappa(1),0),
    v_+=(kappa(cos delta), kappa(sin delta)).

For sufficiently small positive delta they are nonzero and no pair is equal
or opposite. Their upper functions tanh(Z.v_i) are linearly independent.
To prove this, a relation almost surely holds everywhere on the open square
(-1,1)^2 by continuity and the positive density of (Z1,Z2). Choose a vector
z avoiding the finitely many lines perpendicular to v_i or v_i+/-v_j.
Then a_i=z.v_i are nonzero with distinct squares. Restrict the relation to
Z=t z for small t. The nonzero linear, cubic and quintic Taylor coefficients
of tanh give sum_i b_i a_i^(2k+1)=0 for k=0,1,2. Factoring out the nonzero
a_i leaves a Vandermonde matrix in a_i^2, so all relation coefficients b_i
vanish. The feature Gram is therefore positive definite.

For any desired three labels, c in the finite span of these bounded features
can interpolate them with w=g and M=D: if G_ij=E H_i H_j, choose
c=sum_i (G^(-1)y)_i H_i. This is an existence certificate with a finite
readout for every fixed delta>0 under discussion. It does not modify training.

## 8. What the unconstrained maximization means

For each fixed 0<ell<1, (10) proves

    sup over balanced, distinct, representable three-input data tau(ell)
       =infinity.                                       (24)

Thus there is no finite worst-case hitting time under the user's stated
constraints. A maximizing sequence can approach the contradictory collision;
the estimate alone does not decide whether another compatible configuration
has an infinite actual hitting time and attains the supremum in that sense.

There are also exact architectural obstructions which must be excluded
before asking for fitting. The bias-free closure is odd for every state:
f(-u)=-f(u). If a balanced signed label measure is even under u->-u,
A(X)=0 for every state, L=1+B, and c=0 makes the initialized vector field
zero. For example assign +1 to e1,-e1 and -1 to e2,-e2, with weights 1/4.
These labels are incompatible with oddness despite distinct physical inputs.
The triple in Section 7 has neither coincident conflicts nor this obstruction.

Near orthogonality by itself produces no bound like (9). Small signed
correlation, cancellation order, weights and architectural parity are the
quantities used by the proof; pairwise angles alone do not specify them.
No theorem here identifies orthogonality as either a global maximizer or
minimizer of training time.

## 9. Exact limitations and next mathematical obligation

Proved: the nonlinear escape-time principle; uniform pair and triple delay
bounds; the initial finite-difference hierarchy and its maximal moment order;
representability of the hard triple; necessary essential growth of a common-
rate potential; and the infinite supremum in (24).

Not proved: a matching upper hitting-time estimate for the triple; its eventual
fitting; a sharp delta exponent for its true delay; higher-order long-time
delay exponents; uniform small-loss tail rates; or a general decaying potential.
No independent review or numerical evidence is asserted by this author report.

The most direct unresolved estimate is an upper bound of order delta^(-2),
or a demonstrably different order, for tau_triple(ell) at one fixed ell.
That would distinguish necessary barrier growth from the actual transient
scale. The terminal exponential rate is a separate question required before
committing to a geometry-independent rate at all accuracies.
