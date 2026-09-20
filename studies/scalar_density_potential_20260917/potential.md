# Minimum readout correction as a population-state potential

All new statements below concern the deliberately reduced scalar dictionary
closure specified here. They do not assert a canonical p=1 or neural-network
limit. The proof is self-contained given the elementary bounded-gate local
existence argument recalled below. No other study's theorem is a premise.

## 1. Exact system, initialization, and metric

Let phi=tanh, x in sqrt(2) S1, and let mu be a probability training law with
bounded labels. The state is rho1=Law(b1,w), rho2=Law(b2,c), M in R,
with scalar frozen marks b1,b2 and w in R2. The two population integrals
are separate. The current-state contractions are

    a(x)=integral b1 phi(w^T x/sqrt(2)) d rho1,
    H(b2,x)=phi(b2 M a(x)),
    f(x)=integral c H(b2,x) d rho2,
    d(x)=integral b2 c phi'(b2 M a(x)) d rho2,
    r(x,y)=f(x)-y.

The characteristic equations and their density form are

    w_dot=-2 integral r b1 M d(x) phi'(w^T x/sqrt(2)) x/sqrt(2) d mu,
    c_dot=-2 integral r H(b2,x) d mu,
    M_dot=-2 integral r d(x) a(x) d mu,                       (1)

    partial_t rho1+div_w(rho1 w_dot)=0,
    partial_t rho2+partial_c(rho2 c_dot)=0.

The densities may be singular, so the latter equations mean transport of
probability measures. The physical speed squared and unhalved loss are

    V(t)^2=integral |w_dot|^2 d rho1
           +integral |c_dot|^2 d rho2+|M_dot|^2,
    L=integral (f(x)-y)^2 d mu.

The block gradients of L give directly

    L_dot=-V^2.                                               (2)

To fix the scalar dictionary choose the first coordinate direction. On the
lower carrier g~N(0,I2), and the separate upper carrier Z~N(0,1), set

    eta=1/4096,
    nu=E phi(G)^2, tau=E phi(sqrt(nu) G)^2, G~N(0,1),
    b1=phi(g1)/sqrt(nu+eta),
    b2=phi(sqrt(nu) Z)/sqrt(tau+eta),
    w0=g, c0=0,
    M0=D=nu(1-tau)/sqrt((nu+eta)(tau+eta))>0.                  (3)

These are the retained matched forward coordinates of the initialized
coefficient target in docs/observable_p1.md. Their raw Gaussian contraction
is E[sqrt(nu) Z phi(sqrt(nu) Z)]=nu E phi'(sqrt(nu) Z)=nu(1-tau).
Thus D follows by exactly the declared normalization. The lower mark uses
the same g as w0. Reverse-probe features are omitted as part of the model
definition, not replaced by independent copies of a reused action.

For completeness, bounded marks |b_l|<=B_l imply that (1) is locally
Lipschitz in bounded increments w-g, bounded c, and finite M. At label
bound Y, (2) implies E_mu|r|<=Y, and hence

    ||c_t||_infty<=2Yt,
    |M_t-D|<=2Y^2 B1 B2 t^2,
    ||w_dot||_infty<=4Y^2 B1 B2 t |M_t|.

The finite-time bounds prevent escape and give unique continuation through
every finite time. This is also the bounded-mark specialization of
docs/global_nonlinear.md C.4.7.10.C.3. All differentiations below are justified
on finite intervals by these bounds and bounded tanh derivatives.

## 2. Exact fitting set and geometry of a readout correction

For states with given frozen mark marginals define the fitting set by L=0.
This specifies the desired outputs and imposes no unique hidden representation.
The fixed marked quadratic transport cost between rho=Law(b,z) and
rho'=Law(b,z') with the same b marginal is

    W_b(rho,rho')^2 = inf_pi integral |z-z'|^2 d pi,

where pi ranges over couplings of rho and rho' supported on equal marks.
Use z=w on the lower population and z=c on the upper population. The full
state distance is

    D_state(S,S')^2 = W_b1(rho1,rho1')^2
                      +W_b2(rho2,rho2')^2+|M-M'|^2.

Only states of finite second moment are used. The cost on each moving
coordinate is the same Euclidean cost at all times.
At a current state keep rho1 and M fixed, and consider a readout correction

    (b2,c) -> (b2,c+q(b2)).

The cost is integral q(b2)^2 d rho2. It is the squared population-L2
displacement in the original physical metric. Allowing arbitrary couplings
of c and a new c', with the mark b2 unchanged, gives the corresponding
marked quadratic transport cost. The correction formulas below attain the
minimum in this larger class too.

For a two-input state with H(b2,x_-)=-H(b2,x_+), labels +1,-1, and f(x_-)=-f(x_+),
write H=H(b2,x_+), e=1-f(x_+), and K=integral H^2 d rho2. Suppose K>0.
Fitting requires integral q H d rho2=e. Cauchy--Schwarz implies

    integral q^2 d rho2 >= e^2/K,

with equality for q=e H/K. For an arbitrary mark-preserving coupling the
same proof uses q=c'-c inside the coupling and has the same equality witness.
Consequently the explicit state functional

    Phi(S)=L(S)/K(S)=e^2/K                                   (4)

is EXACTLY the minimum squared readout transport to a fitting state with
the current hidden features. In particular it bounds from above the squared
distance to the full fitting set, since that set also allows hidden motion.
No endpoint, future path, or preselected fitting readout is an input to Phi.

Although the slice of fitting states changes when the hidden features move,
the transport cost uses a fixed physical metric. The K_dot term below
accounts explicitly for the motion of that slice.

## 3. A reflected opposite-label family

For each delta in (0,1] take

    x_+=sqrt(2)(delta,sqrt(1-delta^2)),  y_+=1,
    x_-=sqrt(2)(-delta,sqrt(1-delta^2)), y_-=-1,
    mu=1/2 delta_(x_+,1)+1/2 delta_(x_-,-1).

The scalar dictionary (3) is fixed for the entire family. Inputs are
non-antipodal for delta<1, with normalized inner product
gamma=x_+^T x_-/2=1-2delta^2<1. Both class weights are positive and equal.
On its preserved symmetry class,

    integral |H(b2,x_+)-H(b2,x_-)|^2 d rho2 = 4K.

Thus Phi is four times the loss divided by the squared upper-representation
separation of the two classes. The proof controls the evolving separation
using both the first-population dynamics and the middle coefficient.

**Theorem.** Along the prescribed initialized trajectory, K_t is positive
and nondecreasing, Phi is defined for all finite times, and

    Phi_dot <= -4 K_t Phi <= -4 K0 Phi,
    L_t <= Phi_t <= exp(-4 K0 t) Phi_0.                       (5)

There is a fitting limiting state S_infinity. More strongly, the full
remaining physical path length satisfies

    (integral_t^infinity V(s) ds)^2 <= Phi(S_t).              (6)

Thus both population measures and M converge in the marked quadratic
transport / scalar Euclidean geometry, with squared distance to that limit
at most Phi_t. Both hidden activation fields actually move at every t>0.

**Proof of initial positivity.** Define, for |q|<=1,

    A(q)=E[phi(G) phi(qG+sqrt(1-q^2)Z)],

with independent standard G,Z. Oddness and bounded convergence give A(0)=0
and continuity. For |q|<1, differentiating and Gaussian integration by parts
give

    A'(q)=E[phi'(G) phi'(qG+sqrt(1-q^2)Z)]>0.

Indeed the differentiated integrand is
phi(G)phi'(Y)(G-qZ/sqrt(1-q^2)); integration by parts in G produces the
displayed term plus q E[phi(G)phi''(Y)], and the Z term cancels the latter.
All integrals are justified by bounded derivatives and Gaussian moments on
compact interior q intervals. Continuity gives strict monotonicity at the
endpoints as well. Therefore

    a_0(x_+)=A(delta)/sqrt(nu+eta)>0,
    K0=E phi(b2 D a_0(x_+))^2>0.                             (7)

**Proof of preserved geometry.** Let R=diag(-1,1). Initially
w(Rg)=R w(g) and b1(Rg)=-b1(g). This implies a(x_-)=-a(x_+), hence the
same relation for H and f, whereas d(x_-)=d(x_+) because phi' is even.
Substitution in (1) shows w_dot(Rg)=R w_dot(g), preserving the symmetry.
Uniqueness gives these identities for all time.

Suppress x_+ in a,f,d,H and put e=1-f. Let

    P_+=phi'(w^T x_+/sqrt(2)), P_-=phi'(w^T x_-/sqrt(2)),
    C=E1[b1^2 P_+^2]=E1[b1^2 P_-^2],
    B=E1[b1^2 P_+ P_-], Q=C-gamma B.

Strict gate positivity gives C,B>0. Cauchy--Schwarz gives B<=C. If
gamma>=0 then Q>=(1-gamma)C>0; if gamma<0 then Q>=C>0. The full
equations, before any monotonicity assumption, give

    w_dot=e M d b1(P_+ x_+/sqrt(2)-P_- x_-/sqrt(2)),
    a_dot=e M d Q,
    M_dot=2e d a,
    c_dot=2e H.                                               (8)

Differentiating f yields

    f_dot=2e Theta,
    Theta=K+a^2 d^2+(M^2 d^2/2)Q >= K >= 0.                 (9)

Theta is finite and continuous on every bounded time interval, so
e(t)=exp(-2 integral_0^t Theta(s) ds)>0. This proves the sign of e
without assuming the sign bootstrap that follows.

Initially a,M>0. While they remain positive, H has the sign of b2,
so c_dot=2eH preserves b2*c>=0, hence d>=0. Equations (8) then give
a_dot,M_dot>=0, ruling out loss of their positivity. This continuation
argument applies for all time. At every t>0, c has strictly the sign of
b2 almost surely, so d>0 and a_dot,M_dot>0.

The b2 marginal stays fixed. Differentiating its activation norm gives

    K_dot=2(Ma)_dot E2[b2 phi(b2Ma) phi'(b2Ma)] >=0,
    (Ma)_dot=e d(2a^2+M^2 Q)>=0.                             (10)

The expectation in (10) is positive because Ma>0 and b2 is nonzero almost
surely. Thus K_t>=K0>0. Since |phi|<=1, also K_t<=1.

**Proof of potential decay.** Symmetry gives L=e^2. Equations (9)--(10)
give the exact formula

    Phi_dot=-(4 Theta+K_dot/K) Phi <= -4 K Phi.              (11)

This includes the entire time derivative of the moving denominator. Using
K>=K0 and K<=1 yields (5). Also K0 Phi<=L<=Phi, so decrease cannot be
explained by a collapsing notion of distance. Directly summing the squared
velocities in (8) independently checks the metric factors:

    E1|w_dot|^2=2e^2 M^2 d^2 Q,
    |M_dot|^2=4e^2 d^2 a^2,
    E2|c_dot|^2=4e^2 K,
    V^2=4e^2 Theta=-L_dot.                                   (12)

**Proof of the full-state conclusion.** Fix t, and take s>=t. Equations
(10) and (12) imply V(s)^2>=4K_t L_s. Since L_s>0 at finite s,

    V(s) <= (-L_dot(s))/(2 sqrt(K_t) sqrt(L_s)).

Integrating to T gives

    integral_t^T V(s) ds
       <= (sqrt(L_t)-sqrt(L_T))/sqrt(K_t) <= sqrt(Phi_t).

Let T tend to infinity. Loss tends to zero by (5), proving (6).

Realize all times on the original fixed Gaussian carriers. The curve
(w_t,c_t,M_t) lies in the complete Hilbert space
L2(g;R2) x L2(Z;R) x R. Its speed is V and its remaining length tends to
zero, so it is Cauchy and converges to (w_infinity,c_infinity,M_infinity),
with squared Hilbert displacement at most Phi_t. This proves strong
convergence, not a compactness-only assertion.

The fixed-mark coupling supplied by these same carriers has exactly that
displacement cost. Hence the corresponding sum of squared marked transport
distances plus |M_t-M_infinity|^2 is at most Phi_t. This upper bound is
enough; no equality of carrier and optimal-transport distances is assumed.

Bounded marks and the Lipschitz property of phi give uniformly over the
input circle

    |a_t(x)-a_infinity(x)| <= B1 ||w_t-w_infinity||_2.

The M component and readout norms are uniformly bounded by the initial
norms plus the finite total path length. It follows that the upper
activations converge in L2, uniformly in x, and then that f_t converges
uniformly in x. Thus L(S_infinity)=0. The limiting state is an equilibrium
because r vanishes on the training support.

Finally a_t(x_+)>a_0(x_+) for t>0, so the paired lower activation norm is
at least (a_t-a_0)/||b1||_2>0. Since M_t a_t>D a_0, the upper activation
also differs strictly from initialization on every nonzero b2. This proves
actual hidden learning while controlling its remaining motion. QED.

Selecting the dictionary direction parallel to x_+-x_- before training
puts any distinct equally weighted opposite-label circle pair into the
same form after a rotation (the perpendicular coordinate can be reflected).
For a previously fixed direction, the theorem has precisely the reflected
family stated above. Such selection changes the scalar dictionary; it is
not an invariance assertion about the fixed-axis canonical p=1 closure.

## 4. Why a theorem for every training law is false

Keep the fixed first-coordinate dictionary (3). For theta in (0,pi/2),
take equally weighted inputs

    x_+=sqrt(2)(cos(theta), sin(theta)), y_+=1,
    x_-=sqrt(2)(cos(theta),-sin(theta)), y_-=-1.

The initial lower contractions agree by the symmetry g2 -> -g2; hence
the upper activations agree. At c0=0, d=0 and the w,M velocities vanish.
The c velocity is H(x_+)-H(x_-)=0. This exact initialized state is an
equilibrium by uniqueness, and L_t=1 for all t.

The inputs are distinct and non-antipodal, so these are compatible labels.
The same scalar model can represent them at a different finite-second-moment
state: take w(g)=(0,g1), keep M=D, and write

    a_*=E[phi(g1) phi(sin(theta) g1)]/sqrt(nu+eta)>0,
    H_*(b2)=phi(b2 D a_*),
    c_*(b2)=H_*(b2)/E H_*^2.

Then a(x_-)=-a(x_+), and the displayed bounded readout gives predictions
exactly +1,-1. This witness is an admissible finite-second-moment state;
it is not claimed reachable from the stalled initialization.

Therefore no finite nonnegative state functional Phi with L<=F(Phi),
F(0)=0 and F(s)->0 as s down to zero, can satisfy Phi_t<=exp(-lambda t)Phi_0 with
lambda>0 along every initialized trajectory of this fixed scalar dictionary.
At the equilibrium Phi is constant and the exponential inequality forces
Phi=0, contradicting L=1 and the loss-control condition. Allowing Phi=+infinity
there does not give a fitting guarantee and amounts to excluding the case.
Loss remains a non-strict Lyapunov function; this obstruction concerns a
strict, fitting-controlling assertion. It does not disprove a theorem for
generic collision-free data, or for a data-selected dictionary.

## 5. General finite data: exact candidate and the missing estimate

For m inputs with positive weights p_i summing to one, let

    h_i(b2)=sqrt(p_i) H(b2,x_i),
    R_i=sqrt(p_i)(f(x_i)-y_i),
    K_ij=E2[h_i h_j].

This section uses a matrix K, distinct from the scalar K of the pair
reduction above; each is the upper readout Gram on its effective residual
space. When K is positive definite, the same least-norm correction argument
gives a completely explicit current-state potential candidate

    Phi=R^T K^{-1} R.                                       (13)

Indeed the fitting constraints are E[h_i q]=-R_i. The minimizer is
q(b2)=-h(b2)^T K^{-1}R. Decomposing any other admissible q into this
correction plus a component orthogonal to every h_i proves minimality.
The same conclusion follows for general mark-preserving transport couplings.
Since trace(K)=sum_i p_i E H_i^2<=1, the bound L=|R|^2<=Phi holds.
For singular K the same geometric definition gives Phi=R^T K^dagger R
if R belongs to range(K), and Phi=+infinity otherwise. This follows by
diagonalizing the finite symmetric Gram and solving the same constraints
on its positive eigenspaces. The pair theorem has one positive residual
direction and reduces exactly to (4). Formula (14) below is asserted only
on intervals where K is invertible; no omitted derivative of a changing
nullspace is being suppressed.

Let Theta be the full weighted tangent Gram, the sum of the readout K,
the Gram of the L2(g) vectors

    sqrt(p_i) b1 M d(x_i) phi'(w^T x_i/sqrt(2)) x_i/sqrt(2),

and the Gram of the scalar M gradients sqrt(p_i) d(x_i) a(x_i).
Direct differentiation of f gives

    R_dot=-2 Theta R,       Theta>=K in the positive-semidefinite order.

Differentiating (13) and writing v=K^{-1}R gives exactly

    Phi_dot=-v^T [K_dot+2(Theta K+K Theta)] v.                (14)

Thus an exponential estimate would follow from the directional inequality

    v^T [K_dot+2(Theta K+K Theta)] v >= lambda v^T K v        (15)

along the initialized trajectory, together with continued invertibility
of K and lambda>0. Neither property is proved here for generic multiple
inputs. Theta>=K does not settle (15): the symmetrized product of positive
matrices need not be positive, and K_dot has no established sign. No
assertion is made that either obstruction is realized along every or any
particular generic initialized trajectory.

An elementary check of this logical issue is K=diag(1/100,1/2) and
Theta=K+ones(2,2). Then Theta>=K>0, but Theta K+K Theta has diagonal
(101/5000,3/2), off-diagonal 51/100, and determinant -1149/5000<0.
These matrices are an algebraic example only, not a claimed reachable
kernel pair of this scalar model.

At initialization c0=0 gives w_dot=M_dot=0, hence K_dot=0 and Theta=K.
Whenever K0 is positive definite, (14) gives Phi_dot(0)=-4L0<0 for
nonzero labels. This is initial progress, not an all-time estimate.

There are many such initialized datasets. The scalar Gaussian identity in
Section 3 shows that a0(x)=A(x1/sqrt(2))/sqrt(nu+eta). If the x_i1 are
nonzero and distinct in absolute value, then the numbers s_i=D a0(x_i)
are nonzero with distinct squares. The b2 law has positive density on an
interval around zero. A linear relation among phi(b2 s_i) in L2 then
holds throughout that interval by continuity. Its derivatives at zero of
orders 1,3,...,2m-1 give a Vandermonde system in s_i^2, so all coefficients
vanish. The odd tanh Taylor coefficients are nonzero: writing
phi(t)=sum_{k>=1}(-1)^(k-1)a_k t^(2k-1), phi'=1-phi^2 gives a1=1 and
(2k-1)a_k=sum_{i+j=k}a_i a_j>0. This proves strict Gram positivity.

For any finite list of distinct non-antipodal circle inputs, all except
finitely many unit probe directions give these nonzero, distinct absolute
projections: exclude directions perpendicular to x_i and x_i+-x_j.
The long-time estimate (15), not the initial Gaussian calculation, is the
remaining obstruction to promoting this candidate to a generic-data theorem.

## 6. Scope and interpretation

The theorem proves a current-state potential, a quantitative bound on full
remaining physical motion, convergence to some fitting state, and actual
motion of both hidden layers on the explicit pair family. It does not claim
contraction between arbitrary trajectories or convergence to a unique hidden
representation. The changing readout geometry is differentiated exactly,
and the final distance statement uses a fixed physical transport metric.

All rates depend on the geometry through K0. As delta approaches zero,
a0 and K0 approach zero; no geometry-independent positive rate is asserted.
The stationary counterexample forbids the unrestricted all-law fitting
statement for a fixed scalar dictionary. Generic collision-free multiple
inputs remain open, with the exact required inequality displayed above.
