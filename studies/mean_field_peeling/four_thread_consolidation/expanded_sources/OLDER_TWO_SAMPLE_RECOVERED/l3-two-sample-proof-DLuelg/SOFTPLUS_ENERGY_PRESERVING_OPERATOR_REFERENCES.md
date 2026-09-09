# Energy-preserving uncut operator references for shifted softplus

Root candidate, 2026-09-06. UNREVIEWED. This is a new approximation
route, not the canonical global theorem. The reference INITIAL operators
and first fields are approximated. No reference clips a gradient, a
backward query, or the readout during training. Every hidden layer and
the readout follow the exact uncut raw gradient equations for those
reference initial states. The desired theorem still concerns the
prescribed Gaussian initialization, not one of these references.

This note uses the complete explicit uncut model and raw metrics in
SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md, SHA256
398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d,
read in full. Its common-space construction and local theorem are
modular hypotheses here; they remain under review. The local comparison
calculation used below is also stated directly. No global result is
imported. The top/middle curvature estimates in the last section are
reproved in their needed form rather than assumed to apply to an
internally clipped flow.

Fix phi(z)=1+e log(1+exp z), e=1/10. Then phi>=1,
|phi(z)|<=2+e|z|, 0<phi'<=e and |phi''|<=e/4. All positive-order
derivatives are bounded. The two fixed inputs have Gram
C=[[1,rho],[rho,1]], rho in [-1,1), and labels y=(1,sigma),
sigma in {-1,1}. Reversing both labels reverses only the readout and
the backward fields. Probability spaces Omega_ell remain separate.

## 1. Globally regular dynamics from bounded-kernel initial operators

First consider ANY initial first fields bounded in L-infinity on
Omega_1, respecting the rank-one relation at rho=-1, and ANY two
initial operators having bounded kernels on their product probability
spaces. The initial readout is zero. The kernels themselves need not
be finite rank. The state is the first field pair, the two current
bounded kernels, and the readout field. On the product of the relevant
L-infinity spaces, the physical vector field

    (Z1_b)^dot=-2 sum_a C_ba r_a delta1_a,
    (W^ell)^dot=-2 sum_a r_a delta^ell_a tensor H^(ell-1)_a,
                                                     ell=2,3,
    (W4)^dot=-2 sum_a r_a H3_a,                         (1)

with H^ell_a=phi(Z^ell_a), Z2=W2H1, Z3=W3H2 and the TRUE uncut
delta3=W4 phi'(Z3), q2=W3*delta3, delta2=phi'(Z2)q2,
q1=W2*delta2, delta1=phi'(Z1)q1, is locally Lipschitz on bounded
sets. Bounded kernels act from L-infinity to L-infinity, and bounded
scalar derivatives make every displayed composition and product locally
Lipschitz there. The predictions are f_a=E_3 W4 H3_a and r_a=f_a-y_a.
The elementary integral-map contraction therefore constructs a unique
local solution in this Banach space.

It is also C1 in the raw Hilbert metric: first norm
E v^T C^(-1)v, or E v^2 at rho=-1; HS kernel increments; L2 readout.
Differentiation along this bounded path and transpose pairing give

    dL/dt=-||theta_dot||_raw^2,   L=sum_a r_a^2,
    ||theta(t)-theta(0)||_raw<=sqrt(t L(0))=sqrt(2t).    (2)

The second inequality follows by integrating the speed and applying
Cauchy--Schwarz. It concerns the increments in the raw Hilbert norm,
not the initial HS size of the kernels. In particular, on a fixed
physical horizon T every middle operator norm, first L2 norm and
readout L2 norm is bounded by a constant depending only on their
INITIAL Hilbert/operator bounds and T. By linear growth of phi and
bounded phi', every forward/backward L2 norm and |r_a| has such a
bound. Denote one common bound, enlarged finitely many times, by M_T.
It is independent of initial kernel SUPREMUM norms if their operator
norms and the first L2 norms are held bounded. Also |r_a|<=sqrt(2).

We prove that these L2 bounds prevent finite-time escape in
L-infinity when the initial kernels and first fields are bounded.
Let D be a bound on both orientations of both initial operators from
L2 to L-infinity. A bounded kernel has this property: the rowwise or
columnwise L2 kernel norm is at most its supremum, by probability
mass one. Exact rank-memory unrolling gives, for ell=2,3,

    Z^ell_a(t)=W^ell_0 H^(ell-1)_a(t)
       -2 integral_0^t sum_b r_b(u)delta^ell_b(u)
                    E[H^(ell-1)_b(u)H^(ell-1)_a(t)]du,

    q^(ell-1)_a(t)=(W^ell_0)*delta^ell_a(t)
       -2 integral_0^t sum_b r_b(u)H^(ell-1)_b(u)
                    E[delta^ell_b(u)delta^ell_a(t)]du. (3)

These are identities for the full trained operators; both orientations
of both trained memories are retained. Every scalar coefficient in
the integrals is bounded by a constant depending only on M_T. Write
z_ell(t)=max_a||Z^ell_a(t)||_infinity,
q_j(t)=max_a||q^j_a(t)||_infinity, and w(t)=||W4(t)||_infinity.
All are finite on the current local existence interval. Then (3)
and the uncut updates imply inequalities with finite C_T:

    z_1(t)<=z_1(0)+C_T integral_0^t q_1(u)du,
    q_1(t)<=D M_T+C_T integral_0^t [2+e z_1(u)]du,

    z_2(t)<=D M_T+C_T integral_0^t q_2(u)du,
    q_2(t)<=D M_T+C_T integral_0^t [2+e z_2(u)]du,

    z_3(t)<=D M_T+C_T integral_0^t w(u)du,
    w(t)<=C_T integral_0^t [2+e z_3(u)]du.             (4)

For example, the initial term in q2 is bounded using
||delta3_a(t)||_2<=M_T, NOT a readout supremum. Its trained term
uses the L2 delta covariances from (3), leaving only H2(u) in the
pointwise estimate. This is why the middle two inequalities close
without multiplying z2 by w or by an unknown kernel supremum.
The same observation applies to q1. In the forward z2 integral use
|delta2|<=e|q2|; in z3 use |delta3|<=e|W4|.

Add each pair of inequalities in (4), absorb constants, and use
the elementary Gronwall bound. Each of the six functions is bounded
on [0,T] by a finite constant depending on T,M_T,D,z1(0). The current
kernel supremum is then bounded by its initial supremum plus the
integral of the bounded products delta^ell_b H^(ell-1)_b in (1).
Thus every state component remains in a bounded L-infinity ball.
The vector field has a uniform finite Lipschitz and velocity bound
on a slightly larger ball. The local integral-map construction can
be extended in fixed positive increments there, contradicting any
finite maximal time below T. Since T is arbitrary, the reference
physical flow is global. The proof used no independence and no clips.

The same argument applies to feature ascent
theta'=grad_raw g, g=(1/2)sum_a y_a f_a, on any interval where
g<=1. Replace -2r_a in (3) by y_a/2; replace (2) by

    g'=||theta'||_raw^2,
    ||theta(s)-theta(0)||_raw<=sqrt(s g(s))<=sqrt(s).    (5)

Thus the feature solution cannot escape from L-infinity on any
bounded feature interval before reaching g=1. This is an actual
continuation statement at fixed bounded-kernel initialization.

## 2. Strongly approximate the prescribed initial actions

Work on the common generated probability spaces of the local assembly.
They have separable L2 spaces and a countable dense collection of
bounded functions. Choose increasing finite-dimensional spans of these
functions with dense union, and let P_(ell,N) be their L2 orthogonal
projections. An orthonormal basis of each finite span consists of
finite linear combinations of bounded functions and is therefore
bounded. Let

    W^ell_(0,N)=P_(ell,N) W^ell_0 P_(ell-1,N), ell=2,3. (6)

These are finite-rank bounded-kernel operators. Explicitly their kernels
are finite sums of bounded basis products with coefficients
E[e_i W^ell_0 e_j]. They satisfy

    ||W^ell_(0,N)||_op<=10,
    W^ell_(0,N) U -> W^ell_0 U,
    (W^ell_(0,N))* V -> (W^ell_0)* V                    (7)

in L2 for every fixed U,V. The last two statements follow by inserting
P_(ell-1,N)U or P_(ell,N)V and using strong convergence of both
projections to the identity, together with the fixed operator bound.
Neither operator-norm nor HS convergence to W^ell_0 is claimed.

Set Z1_(0,N),a=tau_N(G_a), using the same smooth odd scalar truncation
on both samples. At rho=-1 this retains the opposite-pair constraint.
For |rho|<1 any pair is realizable in the two-dimensional input span.
These first fields converge to G in the first raw norm and have a
uniform first raw norm bound depending on the fixed rho. Indeed they
converge coordinatewise in L2 by domination, and the fixed C^(-1)
is a bounded two-by-two matrix. At rho=-1 use its scalar version.
They are bounded in L-infinity for each N. The initial readout remains
exactly zero.

The projections can be chosen to preserve sample symmetry. To justify
this without introducing a new initialization assumption, enlarge the
countable generating programs by their images under exchanging the
root pair. The joint finite laws are invariant, since the finite
Gaussian root distribution is exchangeable and both initial matrices
are unchanged. On each population this defines a measure-preserving
involution J_ell of the generated algebra, extending to a unitary
involution on L2. It preserves bounded functions and satisfies

    J_ell W^ell_0=W^ell_0 J_(ell-1).                   (8)

One proves (8) on generated queries and then uses density and the
operator bounds. Include both f and J_ell f in every finite spanning
family. Its span is invariant, and its orthogonal projection commutes
with J_ell. Equation (6) therefore retains (8). The truncated first
pair satisfies J_1 Z1_(0,N),a=Z1_(0,N),3-a.

Applying Section 1 constructs a GLOBAL genuine uncut physical flow
for each of these reference initial states. Its L2/operator and raw
energy bounds on fixed physical horizons are uniform in N. Its
L-infinity bounds need not be uniform in N; D in (4) can diverge.
This latter distinction is essential, not a negligible technicality.

## 3. Uniform finite feature budget and preserved action

Uniqueness of the bounded-kernel flow and invariance of its equations
under the involution give

    J_ell H^ell_a=H^ell_(3-a),
    J_3 W4=sigma W4,
    f_a=y_a g, 
    E[(H^ell_1)^2]=E[(H^ell_2)^2].                    (9)

Indeed the first-pair transformation is exchange, the operator
transformation is W -> J_out W J_in, and the readout transformation
is W4 -> sigma J_3 W4. The initial state is fixed by this transformation.
Substitution in the equations uses y_(3-a)=sigma y_a and gives the
same vector field. This proves (9), including second moments, without
postulating a stochastic independence of trained fields.

For either label configuration let alpha denote the three hidden
parameter blocks, and put V(alpha)=(1/2)sum_a y_a H3_a. Then

    W4'=V(alpha),       alpha'=D V(alpha)^* W4.         (10)

The derivative D V uses only phi', forward features, and current
bounded operators, so its first-variation formula is a bounded operator
from the raw hidden Hilbert tangent space to L2. Precisely, define it
first on bounded tangent fields by the L-infinity chain rule and
extend that linear formula by density and the raw norm bound. This
does not assert Frechet differentiability of a nonlinear Nemytskii
map on the entire L2 space. On the existing bounded reference path,
the curve chain rule gives W4''=D V D V^* W4 in L2. Let
k_N=||V(alpha(0))||_2^2. If k_N>0, g'(0)=k_N and g' is nonnegative,
so g>0 for positive feature times and r(s)=||W4(s)||_2 is positive.
Differentiating its norm for s>0 gives

    r''=[||W4'||_2^2-(r')^2+||D V^*W4||_raw^2]/r>=0.  (11)

The inequality is Cauchy--Schwarz for r'=E[W4 W4']/r. Also
W4(s)=sV(alpha(0))+o(s), so r'(0+)=sqrt(k_N). Convexity gives
r'(s)>=sqrt(k_N), hence

    ||V(alpha(s))||_2^2>=k_N,        g'(s)>=k_N.         (12)

By the before-fit continuation statement after (5), g reaches one
at some s_N<=1/k_N. If it had not reached one by that time, (5)
and (4) would extend the bounded-kernel solution to that time, whereas
integration of (12) would give g>=1. No strong endpoint is used as
a substitute for existence: L-infinity continuation has been proved.

The initial reference forward fields converge in L2 to the original
Gaussian-initialization forward fields. This follows from (7), uniform
operator bounds, and Lipschitzness of phi, first at layer 1 and then
recursively through layers 2 and 3. The original initial top feature
Gram is positive definite: the first Gaussian pair has full support
when |rho|<1, so a linear relation between two strictly increasing
features forces both coefficients zero. At rho=-1 the pair is (G,-G),
and phi(G)-phi(-G)=eG while phi(G)+phi(-G)>=2, giving two positive
Gram eigenvalues. The next centered Gaussian pair has the previous
uncentered feature Gram as covariance, so it has full support; repeat
the same argument for the second and third layers. Thus

    k_N -> k_0>0.                                     (13)

For all sufficiently large N, k_N>=k_0/2 and s_N<=S_max=2/k_0.
This bound may depend on rho and the label choice. Uniform first
L2 and initial operator bounds, together with (5), now give uniform
primal and field L2 bounds on every reference's ENTIRE before-fit
feature interval [0,s_N]. Both matrix operator norms are at most
10+sqrt(S_max), and the total raw action up to fit is exactly one.

Physical time is recovered by dt/ds=1/[4(1-g)]. The upper primal
bound also bounds g'=||theta'||_raw^2 above by a finite constant
uniform in large N, because the gradient formulas use only bounded
gates, operator norms and feature/readout L2 norms. Thus
1-g(s)<=C(s_N-s), and the physical clock diverges as s increases
to s_N. Every finite physical horizon therefore corresponds to a
portion of this uniformly bounded before-fit feature interval.

Here is the promised global-reference action consequence for opposite
labels. Write U^ell=(H1^ell+H2^ell)/2,
V^ell=(H1^ell-H2^ell)/2, kappa_ell=||V^ell||_2^2, and use +/-
for half-sum/half-difference of other sample pairs. From (9),
E U^ell V^ell=0. The exact uncut gradients give

    (W^ell)'=delta^ell_- tensor U^(ell-1)
                         +delta^ell_+ tensor V^(ell-1),
    ||(W^ell)'||_HS^2
       =||U^(ell-1)||_2^2||delta^ell_-||_2^2
                        +kappa_(ell-1)||delta^ell_+||_2^2. (14)

Since U>=1, integration of (14) and (5) bounds the sum of
||delta2_-||_2^2, ||delta3_-||_2^2,
kappa1||delta2_+||_2^2, and kappa2||delta3_+||_2^2 by one.

For p_a=phi'(Z^ell_a), phi''=p-p^2/e gives, with the SAME coefficients
A=1-(p_1+p_2)/e and B=p_1p_2/e on both samples,

    (phi''(Z^ell)q^ell)_+ =A delta^ell_+ +B q^ell_+,
    (phi''(Z^ell)q^ell)_- =A delta^ell_- +B q^ell_-,
    |A|<=1, 0<=B<=e.                                  (15)

At the middle layer q2_+/-=(W3)^*delta3_+/-. Consequently, with
M=10+sqrt(S_max), its actual curvature fields M2_+/- satisfy

    integral_0^s_N ||M2_-||_2^2 ds<=2(1+e^2M^2),
    integral_0^s_N kappa2||M2_+||_2^2 ds<=4e^2M^2.      (16)

For the second inequality use kappa2<=e^2M^2 kappa1, obtained from
the shared forward operator and Lipschitzness of phi. At the top,
|phi''(x)-phi''(y)|<=|phi'(x)-phi'(y)| and phi''<=phi' give
|M3_-|<=|delta3_-| and |M3_+|<=|delta3_+|; their joint integral
with weights 1,kappa2 is at most one. These estimates are uniform
over all sufficiently large N and cover their full physical lives
in feature time. They are estimates on actual globally constructed
reference paths, not conditional energy claims about internally
clipped equations.

## 4. Local consistency with the canonical path, and the remaining gap

We record an actual convergence property to distinguish these references
from an unrelated easier model. On the canonical local interval of the
assembly, the N-reference states converge in first/readout L2 and in
the HS norm of their trained INCREMENTS to the canonical local state.
Full operators are compared through their initial strong approximation
and their increment difference; no HS difference between initial
operators is presumed.

Fix an old canonical three-cut reference with radius R. Write
W^ell_N=W^ell_(0,N)+K^ell_N and W^ell_R=W^ell_0+K^ell_R.
The exact forward difference, for example, is

    W2_N H1_N-W2_R H1_R
      =W2_N(H1_N-H1_R)+(K2_N-K2_R)H1_R
                            +(W2_(0,N)-W2_0)H1_R.     (17)

The adjoint difference is the identical split with delta_R as its old
input. The four additional initial-operator errors tend uniformly to
zero on the local interval at each fixed R: their old input fields
are continuous L2 curves, hence compact sets, and uniformly bounded
strongly convergent operators converge uniformly on compact sets.
For the latter assertion choose a finite epsilon-net, use strong
convergence on its finitely many points, and bound the remaining
error by the uniform operator bound times epsilon. Use (7) for both
orientations. Call the sum of these uniform errors epsilon_(N,R).

The old-cut multiplication split

    phi'(z_N)v_N-phi'(z_R)tau_R(v_R)
      =phi'(z_N)[v_N-tau_R(v_R)]
                          +tau_R(v_R)[phi'(z_N)-phi'(z_R)]

places every gate difference next to the bounded OLD cut. The first
bracket is split through v_R. Repeating this from delta3 to delta2
to delta1, using (17), bounded operator norms and bounded feature L2
norms, gives a state-velocity comparison

    ||F_N(theta_N)-F_R(theta_R)||
       <=C(1+R)[d(theta_N,theta_R)+epsilon_(N,R)]
                                 +C tails_R.          (18)

Here d compares first fields, HS trained increments, and readout.
Primal constants are uniform in N on this local interval by (2), or
by (5) before fit. No extra cap multiplies a previously obtained
backward-field difference: its coefficient is the bounded phi'.
Thus the dependence on R is linear. The canonical OLD tails obey
sup_s tails_R<=C exp(-cR^2) by the local assembly. First fields have
initial distance tending to zero; trained increments and readout
start at zero for both paths.

Gronwall in (18), first taking N to infinity at fixed R, gives

    limsup_N sup_s d(theta_N,theta_R)
                                  <=C exp(C_R S_*-cR^2),
    C_R<=C(1+R).

Let R increase to infinity and use convergence of the canonical cut
references to theta. This proves the stated local consistency. The
same velocity inequality and the field splits yield local velocity
consistency as well. The comparison holds on the full canonical local
interval [0,S_*]: the reference initial first marginal norms are at
most one and their operator norms at most ten, so the same small-time
primal box yields |g_N(s)|<=49s before fit on s<=1/10. Since
S_*<=1/196, the before-fit continuation proof then guarantees every
reference reaches S_* with g_N<=1/4, before its fitting time. No finite-width
or global consistency is inferred from this local calculation.

The global convergence problem is still open. In particular:

- The kernel L2-to-L-infinity constants D_N can diverge; (4) is NOT
  a uniform Gaussian tail bound over the references.
- Strong convergence of the initial operators is uniform only on
  compact sets of inputs. Energy-bounded families of reference fields
  need not form a compact subset of L2.
- The uniform integrated curvature bounds (16) do not bound their
  products with arbitrary correlated source sensitivities, nor do they
  supply the missing nonlinear comparison on later intervals.

This reference construction therefore preserves precisely the gradient,
readout-convexity and actual curvature-action structure needed for a
possible next estimate, while changing initialization only temporarily.
Replacing the final canonical theorem by any fixed bounded-kernel
reference would violate the target and is not proposed here.
