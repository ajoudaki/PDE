# Small dictionaries with actual hidden learning

Claim type: proved constructions and dynamical statements for deliberately
weaker closures, not an exact reduction or accuracy theorem for canonical p=1.
All new proofs use only the established book inputs recorded in README.md.

## 1. Model and what is changed

Take phi=tanh and x in sqrt(2) S1. A finite training law mu has probability
weights and real labels bounded by Y. Loss is L=E_mu[(f(x)-y)^2], unhalved,
in physical time. The moving first-layer weight is w in R2 with w(0)=g,
where g~N(0,I2). The population readout starts at c=0. The state metric
is E1|delta w|^2+E2|delta c|^2+||delta M||_F^2.

We change the retained initialized dictionary. Let b1 and b2 have positive
dimensions K1 and K2; the exact closure equations for supplied bounded marks
are

    a(x) = E1[b1 phi(w^T x/sqrt(2))],
    H(x) = phi(b2^T M a(x)),
    f(x) = E2[c H(x)],
    d(x) = E2[b2 c phi'(b2^T M a(x))],       r=f-y,

    w_dot = -2 E_mu[r phi'(w^T x/sqrt(2)) b1^T M^T d(x) x/sqrt(2)],
    c_dot = -2 E_mu[r H(x)],
    M_dot = -2 E_mu[r d(x) a(x)^T].                           (1)

These are the established C.4.7.10 equations with a smaller dictionary.
Keeping only selected initialized features is a new closure choice. It does
not make the omitted features dynamically redundant in canonical p=1.

For completeness, direct differentiation of f gives the parameter-gradient
blocks phi'(w^T x/sqrt(2)) b1^T M^T d(x) x/sqrt(2), H(x), and
d(x)a(x)^T. Thus (1) is exactly gradient flow in the declared metric,

    L_dot=-E1|w_dot|^2-E2|c_dot|^2-||M_dot||_F^2.             (2)

Bounded marks imply local Lipschitz continuity in the Banach norm of
(w-g,c,M) with L-infinity norms for fields and Frobenius norm for M.
Since L(0)<=Y^2, E_mu|r|<=Y, and if |b_l|<=B_l,

    ||c(t)||_infty<=2Yt,
    ||M(t)-M(0)||_F<=2Y^2 B1 B2 t^2,
    ||w_dot(t)||_infty<=4Y^2 B1 B2 t ||M(t)||_F.

These follow from |a|<=B1, |d|<=B2||c||_infty, and |phi|,|phi'|<=1.
The bounds prevent escape on any finite interval and give unique global
real-time continuation, with own-state restart. This reproduces the needed
fixed-dictionary existence argument without invoking a network limit.

## 2. A scalar dictionary on each population

Set eta=1/4096, and let Z be a standard Gaussian on the upper population,
separate from the lower g. Define

    nu = E phi(G)^2,               G~N(0,1),
    tau = E phi(sqrt(nu) Z)^2,
    ell_h=sqrt(nu+eta),            ell_H=sqrt(tau+eta),

    b1(g)=phi(g1)/ell_h,
    b2(Z)=phi(sqrt(nu) Z)/ell_H,
    M(0)=D=(1-tau) nu/(ell_h ell_H)>0.                       (3)

Both dictionary dimensions are one. The b1 mark is a function of the SAME
g1 used by w(0); it must not be sampled independently. There are no lower
reverse-noise marks because the corresponding reverse-probe features have
been deliberately omitted. The scalar reverse action is the same M.

These are precisely the first normalized forward feature on each side of
the p=1 tanh-core dictionary in docs/observable_p1.md. The discarded constant
features have zero contraction and remain inactive by odd population parity.
Taking the first lower and first upper normalized coordinates preserves
their original eta normalization. At initialization A0 phi(g1)=sqrt(nu) Z.
Gaussian integration by parts gives

    E[phi(sqrt(nu) Z) sqrt(nu) Z]
       =nu E phi'(sqrt(nu) Z)=nu(1-tau),

so the canonical retained contraction is exactly D in (3). There is no
invented initial coupling or independent reverse matrix.

All quantities a,d,M are now scalar; w remains a two-dimensional input
weight. Equations (1) retain all moving blocks and both nonlinear gates.

## 3. A useful scalar Gaussian identity

For independent standard G,Z define, for -1<=r<=1,

    A(r)=E[phi(G) phi(rG+sqrt(1-r^2) Z)].

This function is odd, continuous, and strictly increasing. Continuity follows
by bounded convergence. Oddness follows by negating Z and using odd phi.
For an interior r, differentiating and integrating by parts in G and Z gives

    A'(r)=E[phi'(G) phi'(rG+sqrt(1-r^2) Z)]>0.                (4)

Indeed the derivative before integration by parts is
E[phi(G) phi'(Y)(G-r Z/sqrt(1-r^2))]. The G integration gives
E[phi'(G)phi'(Y)]+r E[phi(G)phi''(Y)]; the Z integration cancels
the second term. All derivatives are bounded and Gaussian moments are
integrable on a compact subinterval of (-1,1). Strict positivity and
continuity extend strict monotonicity to the endpoints.

At initialization of (3), conditioning g^T x/sqrt(2) on g1 yields

    a_0(x)=A(x1/sqrt(2))/ell_h.                              (5)

This explicitly displays the selected coordinate direction.

## 4. Successful learning with both hidden representations moving

For every delta in (0,1], take

    x_+=sqrt(2)(delta,sqrt(1-delta^2)),       y_+=+1,
    x_-=sqrt(2)(-delta,sqrt(1-delta^2)),      y_-=-1,
    mu_+=mu_-=1/2.

These are distinct; they are non-antipodal for delta<1. Their normalized
inner product is rho=x_+^T x_-/2=1-2delta^2<1. The closure is always
the same fixed scalar construction (3), with no future-dependent input.

**Theorem.** For this family, L(t)<=exp(-4 K0 t), where

    A0=A(delta)/ell_h>0,
    K0=E2[phi(b2 D A0)^2]>0.                                (6)

For every t>0, each hidden layer has strictly positive paired L2 activation
displacement on x_+. Thus the learning is not confined to the readout.
The rate is allowed to degenerate as delta approaches zero.

**Proof.** Let R=diag(-1,1). The initial fields satisfy
w(Rg)=R w(g) and b1(Rg)=-b1(g). This symmetry is invariant under (1):
it implies a(x_-)=-a(x_+), H(x_-)=-H(x_+), and f(x_-)=-f(x_+).
The upper gate is even, so d(x_-)=d(x_+). Substitution into the w equation
then shows its velocity at Rg is R times its velocity at g, while the M
and c equations preserve the same relations. Uniqueness proves invariance.

Write A_t=a_t(x_+), f_t=f_t(x_+), e_t=1-f_t, d_t=d_t(x_+), and
H_t=phi(b2 M_t A_t). Define P_+=phi'(w^T x_+/sqrt(2)) and P_- similarly.
The symmetry gives E1[b1^2 P_+^2]=E1[b1^2 P_-^2]. Put

    C_t=E1[b1^2 P_+^2],       B_t=E1[b1^2 P_+ P_-],
    Q_t=C_t-rho B_t.

Both gates are strictly positive. Cauchy--Schwarz gives 0<B_t<=C_t,
and C_t>0. If rho>=0 then Q_t>=(1-rho)C_t>0; if rho<0 then Q_t>=C_t>0.
The exact equations reduce to

    w_dot=e M d b1(P_+ x_+/sqrt(2)-P_- x_-/sqrt(2)),
    A_dot=e M d Q,
    M_dot=2e d A,
    c_dot=2e H.                                               (7)

Differentiate f=E2[c phi(b2 M A)]. Since d=E2[b2 c phi'(b2 M A)],

    f_dot=2e K_s,
    K_s=E2 H^2+d^2 A^2+(M^2 d^2/2)Q>=0.                     (8)

The coefficient K_s is continuous and bounded on every finite interval by
the finite-time bounds of Section 1. Hence e_t=exp(-2 integral_0^t K_s ds)>0.

Initially A0>0 and M0=D>0. As long as M,A are positive, H has the sign of
b2. Equation (7) preserves b2*c>=0, whence d>=0. It follows that A and M
cannot decrease or reach zero. Continuation proves these properties for all
time. For each t>0, c has strictly the sign of b2 at almost every nonzero
b2, so d_t>0. Equations (7) then give A_dot>0 and M_dot>0 for t>0.

Thus M_t A_t>=D A0 and |H_t|>=|H_0| pointwise. In particular
K_s>=E2 H_t^2>=K0. Integrating e_dot=-2K_s e gives (6)'s loss bound.

For the lower layer, A_t-A0=E1[b1(H1_t(x_+)-H1_0(x_+))]>0 at t>0.
Cauchy--Schwarz implies its paired L2 displacement is at least
(A_t-A0)/||b1||_2>0. The upper product M_t A_t is strictly larger at
t>0, and b2 is nonzero almost surely; strict monotonicity of phi implies
its paired activation displacement is positive as well.

As a separate factor check, (7) gives
E1|w_dot|^2=2e^2 M^2 d^2 Q, |M_dot|^2=4e^2 d^2 A^2,
E2|c_dot|^2=4e^2 E2 H^2. Their sum is exactly 4e^2 K_s=-L_dot.
This agrees with the original physical gradient metric. QED.

For small times the motion can also be checked directly:
d_dot(0)=2 E2[b2 H0 phi'(b2 D A0)]>0,
M_ddot(0)=2 A0 d_dot(0)>0, and
A_ddot(0)=D d_dot(0) Q0>0. This checks strict hidden motion without
inferring it only from the output loss.

An optional selected-direction version replaces g1 by e^T g for a fixed
unit vector e and uses the corresponding initialized forward probe A0 phi(e^T g).
The scalar law and D are unchanged because e^T g is standard Gaussian.
For any two distinct equal-norm opposite-label inputs with equal weights,
choosing e parallel to x_+-x_- before training puts them in the family above
after an orthogonal coordinate change. This is a data-selected scalar
dictionary, not deletion of a coordinate of a fixed-axis p=1 dictionary.

## 5. Compression can create a stationary nonfitting problem

Fix theta in (0,pi/2) and take the balanced opposite-label pair

    x_+=sqrt(2)(cos(theta),sin(theta)), y_+=+1,
    x_-=sqrt(2)(cos(theta),-sin(theta)), y_-=-1.

The first coordinates coincide, so (5) gives identical a_0 and H_0 at
the two inputs. Since c0=0, the initial c velocity is H0(x_+)-H0(x_-)=0;
the initial d and hence w and M velocities also vanish. The entire
initialized state is an equilibrium by uniqueness, with L(t)=1 forever.
The inputs are distinct and non-antipodal and the labels are not contradictory.
This example concerns a fixed dictionary direction, not the optional
data-selected direction of Section 4.

An even simpler example, x_+=sqrt(2)e2 and x_-=-sqrt(2)e2 with labels
+1,-1, is stationary because a0=H0=0. It is representable by the SAME
scalar closure at another bounded-increment state: take

    w(g)=g+K phi(g1)e2,      M=D,      K>0.

For q(g1)=phi(g1), define m(t)=E_{g2} phi(g2+t). It is odd and strictly
increasing, so
a(x_+)=E[q(g1)m(K q(g1))]/ell_h>0. The other feature is its negative.
Put H_+=phi(b2 D a(x_+)) and choose c=H_+/E2 H_+^2. This bounded
readout fits both labels exactly. Thus the stationary example reflects a
failure of training from the chosen compressed initialization, not an
architectural impossibility of representing the labels.

Nevertheless, a scalar dictionary is not restricted to distinguishing just
two inputs. Suppose a finite input list satisfies

    x_j1 != 0 and |x_i1| != |x_j1| for i != j.               (5a)

Then its initial upper-activation Gram is strictly positive definite.
Indeed s_j=D A(x_j1/sqrt(2))/ell_h are nonzero with distinct squares,
by (4). The upper b2 law has positive density on (-1/ell_H,1/ell_H).
Any linear relation sum_j alpha_j phi(b2 s_j)=0 in L2 therefore holds
throughout this interval, by continuity. Differentiating at zero at orders
1,3,...,2m-1 gives sum_j alpha_j s_j^(2k+1)=0. The odd Taylor
coefficients of tanh are nonzero, as verified in Section 6 below. The
Vandermonde determinant in the distinct s_j^2 gives alpha_j=0 for all j.
Thus, for positive weights and labels not all zero,

    L_dot(0)=-4 ||sum_j mu_j y_j H0(x_j)||_2^2<0.            (5b)

For ANY finite list of distinct non-antipodal circle inputs, one can choose
the scalar probe direction e before training to ensure (5a) in its rotated
coordinates: avoid the finitely many directions perpendicular to x_j,
x_i-x_j, or x_i+x_j. Every other direction works. A direction selected
independently from a continuous distribution works with probability one.
The resulting linear independence concerns the nonlinear upper activation
functions, despite their scalar arguments. This proves initial progress
for generic finite data; it does not prove preservation of the Gram bound
or eventual fitting. A fixed direction still has the collisions above.

## 6. A (2,2) dictionary is a useful intermediate construction

Retain both forward probes but no lower reverse-probe features:

    b1=phi(g)/ell_h in R2,
    b2=phi(sqrt(nu) Z)/ell_H in R2,       Z~N(0,I2),
    w0=g, c0=0, M0=D I2,                                    (9)

where D is the scalar in (3). Different coordinate probes are independent
at initialization; their exact Gaussian contractions give the displayed
diagonal matrix, which is free to become a full 2 by 2 matrix during training.
Both characteristic carriers are now only two-dimensional. The lower
reverse-noise coordinates of canonical p=1 are absent by the declared change
of retained features, rather than being incorrectly averaged independently.

This construction retains both coordinate directions and avoids the scalar
initialization collision for EVERY finite list of distinct non-antipodal
circle inputs. Specifically, its initial upper-activation Gram is strictly
positive definite for such a list.

**Proof.** Equation (4) gives

    a0(x)=(A(x1/sqrt(2)),A(x2/sqrt(2)))/ell_h,
    v0(x)=D a0(x).

Strict monotonicity and oddness of A show v0(x) is nonzero, injective, and
v0(x')=-v0(x) exactly when x'=-x. For a finite admitted list write v_j=v0(x_j).
The upper b2 law has positive density on the open square
(-1/ell_H,1/ell_H)^2. Suppose sum_j alpha_j phi(b2^T v_j)=0 almost surely.
Continuity implies this relation everywhere in the open square.

Choose q in R2 outside the finitely many lines perpendicular to v_j or
v_i+-v_j. Such a choice exists because these vectors are nonzero and a
finite union of lines does not fill the plane. Then s_j=q^T v_j are nonzero
and their squares are distinct. Restrict the relation to b2=tq near zero.
The derivatives of odd orders 1,3,...,2m-1 imply

    sum_j alpha_j s_j^(2k+1)=0,       k=0,...,m-1.

Every odd Taylor coefficient of tanh is nonzero: write
phi(t)=sum_{k>=1}(-1)^(k-1)a_k t^(2k-1); phi'=1-phi^2 gives a1=1 and
(2k-1)a_k=sum_{i+j=k}a_i a_j>0 for k>=2. The preceding linear system
is a Vandermonde system in s_j^2 after multiplication by s_j. Its determinant
is nonzero, so all alpha_j vanish. This proves strict Gram positivity. QED.

At c0=0 only the readout contributes to the initial gradient. Consequently
for positive sample weights and labels not all zero,

    L_dot(0)=-4 ||sum_j mu_j y_j H0(x_j)||_2^2<0.             (10)

This is an initial non-stalling statement, not a proof of later fitting.
Near-coincident or nearly antipodal inputs may make the smallest eigenvalue
arbitrarily small; no uniform rate is asserted. Duplicates and antipodal
inputs must be grouped with the model's oddness constraint if admitted.

The (2,2) model also has actual feature learning. For the data pair
(sqrt(2)e1,+1),(-sqrt(2)e1,-1), its evolution on training inputs has an
invariant scalar subsystem (3): w2=g2 remains fixed, w1 depends only on g1,
a2=0, c depends only on Z1, d2=0, M12=M21=0 and M22=D. Independence and
oddness give a2=d2=0 at every such state, so (1) preserves it. Section 4
therefore proves motion of both hidden representations and exponential
fitting for this subsystem. Nonzero initial accelerations persist under
sufficiently small perturbations of the finite data, by bounded-gate
dominated convergence of their explicit derivative formulas. No fitting
extension to those perturbed laws is inferred from that local observation.

## 7. Dimensions and the meaning of minimal

These are generic carrier dimensions, before data-specific symmetries:

| Construction | dim b1 | dim b2 | M | joint measure domains | characteristic grids |
|---|---:|---:|---|---|---|
| Canonical p=1, inactive constants omitted | 4 | 2 | 2 by 4 | 6D / 3D | 4D / 2D |
| Both forward probes (9) | 2 | 2 | 2 by 2 | 4D / 3D | 2D / 2D |
| One matched forward probe (3) | 1 | 1 | scalar | 3D / 2D | 2D / 1D |

For (3), the lower carrier still needs g1,g2 because w0 is the full
two-dimensional Gaussian. The mark b1 is scalar, but w retains two input
components. In (9), b1 already determines g, and the lower density remains
on a two-dimensional characteristic graph within its four-dimensional domain.
Here the joint measures are the autonomous marginals rho1=Law(b1,w) and
rho2=Law(b2,c). Keeping the otherwise unused frozen initial g as an extra
coordinate enlarges the written state; it is unnecessary for their evolution.
These laws need not have Lebesgue densities on their ambient domains:
the initialized characteristic supports have the smaller grid dimensions
displayed above, and remain supported on their transported images.

For data supported on the selected axis alone, (3)'s transverse weight
never moves and the moving first coordinate depends only on g1. Then the
lower evolving field can use a 1D grid; off-axis observations still integrate
the known independent transverse Gaussian. This is a data-specific reduction.

Within this factorized two-population closure architecture, (1,1) is the
smallest positive pair of dictionary dimensions. An empty dictionary on
either side forces zero upper preactivation and a zero predictor for phi(0)=0.
Constant-only features with centered Gaussian w0 and c0=0 also yield a0=0,
H0=0, and an equilibrium even if a nonzero M0 were supplied; their true
Gaussian initialized contraction is zero. The nonconstant matched probes
in (3) avoid that triviality.

Under a regular characteristic parametrization (locally Lipschitz on each
compact coordinate patch), a one-dimensional continuous parameter cannot
produce the full two-dimensional Gaussian w0: the image of each compact
interval has planar area zero. To see this, a Lipschitz constant C permits
covering its image by O(1/epsilon) disks of radius C epsilon, of total area
O(epsilon). A countable union of compact intervals still has zero area.
This excludes a one-dimensional regular lower carrier while preserving
ordinary two-dimensional initialization. Pathological measurable encodings
are not numerical grid reductions. No minimality over every architecture,
atomic initialization, or nonlinear state representation is claimed.

The practical dimension saving of (9) is substantial without discarding a
coordinate direction: at q nodes per axis its lower grid has q^2 rather than
q^4 entries, and its upper grid remains q^2. This is a state-count comparison,
not an accuracy, speed, or equivalence guarantee relative to canonical p=1.
