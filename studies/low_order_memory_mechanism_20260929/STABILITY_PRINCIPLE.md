# Stability principles for the autonomous moment closure

This is a scoped theoretical analysis of `MODEL.md`, using the notation
contract in `docs/notation.qmd`. No other research inputs, experiments, or
dense reference trajectory are used. Results below concern the closure's own
finite-width continuous-time solution. They are internally derived results,
not promoted material or claims about a width limit.

The main conclusions are: every finite-order tanh closure is globally defined
in physical time; its memory filters have an exact passivity law; this law
does not make its loss a state-space Lyapunov function; and the first-order
closure does fit a single datum at every scalar depth, almost surely under
the stated scalar Gaussian initialization. The last result uses a reachable
sign-and-order cone, rather than stability of arbitrary moment states.

## 1. An exact filter identity, valid for every finite q

On an interval with rho>0 use activity tau as time. Fix a link and sample,
write h=h_a^(ell-1), b=(r_a/rho)delta_a^ell, and put

    d_k=2k+1,
    hhat=(1/tau) sum_k d_k B_k,
    bhat=(1/tau) sum_k d_k C_k,
    e_h=h-hhat, e_b=b-bhat.

These are length-n vectors; hats reconstruct the current endpoint of the
retained history polynomial, not the current network response itself. Let A
be the q-by-q matrix with A_kk=k, A_kj=d_j for j<k, and zero otherwise, and
D=diag(d_k). Direct entrywise calculation gives

    D A + A^T D + D = d d^T.                         (1)

For either moment family X with input u (B,h or C,b), define the nonnegative
scalar storage E_X=(1/(2tau))sum_k d_k ||X_k||_2^2. Its activity derivative is

    E_X' = <xhat,u> - (1/2)||xhat||_2^2
         = (1/2)||u||_2^2 - (1/2)||u-xhat||_2^2.    (2)

Indeed differentiating the factor 1/tau and substituting
X_k'=u-(AX)_k/tau produces the quadratic form (1). This is an exact
input-output passivity identity. With the prescribed initialization,

    (1/tau)sum_k d_k ||B_k||_2^2
       + integral_1^tau ||e_h||_2^2 dxi
       = ||h(0)||_2^2 + integral_1^tau ||h||_2^2 dxi,

    (1/tau)sum_k d_k ||C_k||_2^2
       + integral_1^tau ||e_b||_2^2 dxi
       = integral_1^tau ||b||_2^2 dxi.              (3)

In particular, tanh gives sum_k d_k||B_k||_2^2 <= n tau^2.
There is no small-error conclusion at fixed q: the right side also pays for
endpoint prediction error. The stored energy can increase under forcing.

For the matrix cross-storage S=(1/tau)sum_k d_k C_k B_k^T, the same calculation
gives a more informative identity:

    S' = b hhat^T + bhat h^T - bhat hhat^T
       = b h^T - e_b e_h^T.                        (4)

Thus the closure differs from an instantaneous gradient middle update by
the product of its own forward and backward endpoint errors. This is an
exact statement about the closure, without any approximation comparison.

## 2. The closure's own loss derivative

Set alpha=2/(mn), loss=rho^2, and, for each hidden link,

    G_ell=sum_a r_a delta_a^ell (h_a^(ell-1))^T,
    R_ell=sum_a e_(b,ell,a) e_(h,ell,a)^T.

Returning (4) to physical time gives

    dot W_ell=-alpha(G_ell-rho R_ell).                  (5)

Also define g_w=sum_a r_a h_a^L and
g_1=sum_a r_a delta_a^1 x_a^T/sqrt(d). The chain rule, with
partial loss/partial W_ell=alpha G_ell and the mobilities in `MODEL.md`, yields

    dot loss = -4/(m^2 n)(||g_w||_2^2+||g_1||_F^2)
            -alpha^2 sum_ell ||G_ell||_F^2
            +alpha^2 rho sum_ell <G_ell,R_ell>_F.      (6)

At rho=0 all physical velocities and dot loss vanish; no division by rho is
needed to define the original ODE. Equations using b are restricted to
rho>0, or interpreted after multiplying by rho.

The final term in (6) has no automatic sign. For example, the following two
conditions, if proved along a particular reachable trajectory, would suffice
for exponential fitting:

    rho sum_ell <G_ell,R_ell>_F
       <= kappa sum_ell ||G_ell||_F^2,   0<=kappa<1,

    D_total(t):=4/(m^2 n)(||g_w||_2^2+||g_1||_F^2)
             +alpha^2 sum_ell ||G_ell||_F^2 >= c loss(t), c>0.

Equation (6) then gives loss(t)<=loss(0)exp(-(1-kappa)c t).
Neither the filter storage law nor its nonnegative dissipation proves these
two additional alignment and coercivity conditions.

There is also a simple all-q readout passivity law:

    d/dt [||w||_2^2/(2n)]
       = -(2/m)sum_a r_a f_a
       = (2/m)sum_a y_a f_a -(2/m)sum_a f_a^2.      (7)

It bounds output work supplied by labels; it is not a residual-decay law.

## 3. Global existence at fixed width and order

**Proposition.** For finite m,n,d,L,q, finite data and initial matrices, and
tanh activation, the prescribed initial-value problem has a unique solution
for every finite physical time. This does not assert bounded weights as
t tends to infinity, convergence, or any bound uniform in width.

**Proof.** The finite-dimensional vector field is locally Lipschitz on
tau>0: rho is a Euclidean norm of a smooth residual map, and division occurs
only by tau. Consequently the local existence and continuation theorem for
locally Lipschitz ODEs applies: a solution can fail to extend to a finite
endpoint only if it leaves every compact subset of this domain.

Write Y=(m^(-1)sum_a y_a^2)^(1/2). Since ||h_a^ell||_2<=sqrt(n),

    rho <= ||w||_2/sqrt(n)+Y,
    ||dot w||_2 <= 2sqrt(n)rho,
    ||w(t)||_2 <= sqrt(n)Y(exp(2t)-1),
    rho(t) <= Y exp(2t).

The third inequality is the scalar integral inequality obtained from the
first two and w(0)=0. Thus tau>=1 and tau is bounded on each finite interval.
The linear B equations then have bounded coefficients and bounded forcing,
so every B is bounded there (also directly by (3)). At the last layer,
||delta_a^L||_2<=||w||_2, so the C_L equations have bounded coefficients and
forcing. Their integral inequality bounds C_L, hence the reconstruction
bounds W_L. Descending one layer, ||delta_a^(L-1)||_2 is bounded by
||W_L||_op ||delta_a^L||_2 because |tanh'|<=1. Repeating bounds C_(L-1),
W_(L-1), and all remaining hidden links. Finally dot W1 is bounded by its
displayed update and the finite inputs. All state coordinates stay bounded,
and tau stays separated from zero, giving the required compact subset and
continuation. The local uniqueness theorem gives global uniqueness. QED.

## 4. A reachable q=1 learning theorem

**Proposition (scalar single-datum fitting).** Suppose q=1, m=n=1, L>=2,
x!=0, the initial first preactivation is nonzero, and each initial hidden
scalar link is nonzero. For arbitrary scalar y, the prescribed closure fits
the datum. If y!=0, with H0=|h^L(0)|>0,

    (f(t)-y)^2 <= y^2 exp(-4 H0^2 t).              (8)

The output moves monotonically from zero toward y. These nonzero conditions
hold almost surely under the specified scalar Gaussian initialization.

**Proof.** The case y=0 is stationary. Here is the sign change explicitly.
Set epsilon=sign(y), sigma_1=sign(z^1(0)), and recursively
sigma_ell=sigma_(ell-1)sign(W0_ell). Replace z^ell,h^ell by
sigma_ell z^ell,sigma_ell h^ell, W1 by sigma_1 W1, each hidden link by
sigma_ell sigma_(ell-1)W_ell, and w by epsilon sigma_L w. Replace each
B_ell by sigma_(ell-1)B_ell and C_ell by sigma_ell C_ell. Oddness of tanh
and evenness of its derivative give transformed f=epsilon f,
r=epsilon r, and delta^ell=epsilon sigma_ell delta^ell. Therefore the
transformed target is |y|, the transformed moment equations and weight
reconstruction have exactly the same form, and the effective initial first
preactivation and all hidden scalar links are positive. Suppressing bars,
it is enough to prove the result for these positive coordinates and y>0.
Put U_ell=B_ell/tau.
For q=1 and m=n=1,

    dot U_ell=(rho/tau)(h^(ell-1)-U_ell),
    dot C_ell=r delta^ell,
    dot W_ell=-2[r delta^ell U_ell
                  +(rho/tau)C_ell(h^(ell-1)-U_ell)].       (9)

Consider the interval before the first fit f=y. Here r<0. The following
constraints are invariant:

    w>=0, C_ell<=0, U_ell>=0,
    h^(ell-1)-U_ell>=0,
    z^1>=z^1(0)>0, W_ell>=W_ell(0)>0.              (10)

To verify this rather than assume it, under (10) backpropagation gives
delta^ell>=0. The W_ell derivatives in (9) are nonnegative,
dot z^1=-2r delta^1 ||x||_2^2/d>=0, dot w=-2r h^L>=0,
dot C_ell<=0, and dot U_ell>=0. Differentiating the feedforward equations
therefore gives dot h^j>=0 for every j. At a boundary
h^(ell-1)-U_ell=0 its derivative is dot h^(ell-1)>=0.
All constraints hold initially. These boundary signs prove invariance by
the elementary locally-Lipschitz orthant argument: the sum of squares of
negative constraint coordinates has derivative bounded by a local constant
times itself, and is initially zero. One may regard W and the constraint
coordinates as auxiliary variables with their differentiated equations;
their defining relations are preserved.

Consequently h^L(t)>=H0 and every term in

    dot f=dot w h^L+w dot h^L
          >=2(y-f)(h^L)^2 >=2 H0^2(y-f)            (11)

is nonnegative. At a first fit all raw velocities vanish; uniqueness implies
that the state stays fixed, so the output cannot cross y. Before any such
time, multiplying (11) by -2(y-f) and integrating gives (8). Global
existence from Section 3 completes the argument on all t>=0. QED.

The mechanism is temporal coherence. U is an average of past nonnegative
features and remains below the current feature; C has the residual's sign
times a nonnegative backward response. Both summands of the reconstructed
hidden velocity then improve the output. This proof does not require the
endpoint backward error e_b itself to have a fixed sign.

**Deterministic extension to arbitrary width.** For one sample and q=1,
suppose the initial first feature is entrywise positive, all hidden W0 are
entrywise nonnegative, and ||h^L(0)||_2>0. With the prescribed zero readout
and moments, the same proof works entrywise: U>=0, h-U>=0, C<=0,
delta>=0, and every hidden matrix derivative in

    dot W_ell=-(2/n)[r delta^ell U_ell^T
                      +(rho/tau)C_ell(h^(ell-1)-U_ell)^T]

is entrywise nonnegative before fit. All forward features are therefore
nondecreasing. After the target-sign reduction, w>=0, and
dot f>=2(y-f)||h^L(0)||_2^2/n. Consequently

    loss(t)<=y^2 exp(-4||h^L(0)||_2^2 t/n).

These are restrictive deterministic sign hypotheses, not a claim that a
typical Gaussian matrix satisfies them. They isolate a mechanism that
survives width rather than proving general Gaussian-width learning.

A wider sufficient condition is visible without scalar sign gauges. For a
single datum before first fit, suppose, for every hidden link and all earlier
times s<=t,

    0 <= <h(t),h(s)> <= ||h(t)||_2^2,
    <delta(t),delta(s)> >= 0.                      (12)

The initial unit activity segment uses h(0). Then <h,U>>=0,
<h,h-U>>=0, and r(t)<delta(t),C(t)>>=0. Contracting (9), with its general
factor 2/n, against r delta h^T shows that every hidden contribution to
dot loss is nonpositive. If additionally ||h^L(t)||_2^2/n>=gamma>0, the readout
contribution alone gives loss(t)<=loss(0)exp(-4 gamma t). Conditions (12) are
sufficient trajectory conditions, not established facts for general width.

## 5. What the identities do not establish

**Loss ascent at an arbitrary state.** Take q=1,m=n=d=1,L=2,tanh,x=y=1,
and the state

    W1=atanh(1/2), W0_2=1/4, w=1,
    tau=2, B=-1, C=-1/4.

Then h^1=1/2, U=-1/2, reconstructed W2=W0_2-2CU=0,
h^2=f=0, r=-1, delta^2=1, and delta^1=0. Thus dot W1=dot w=0,
dot W2=-3/4, dot f=-3/8, and dot loss=3/4>0.
This is a valid point of the autonomous state space with consistent
reconstruction and the elementary bound |B|<=tau. It is **not** asserted
reachable from the prescribed initialization. In fact the scalar invariant
cone just proved excludes it. It disproves a state-space loss-Lyapunov claim,
not loss monotonicity or fitting for the specified random initialization.

**Exact stalled initial states.** For any q, if

    sum_a y_a h_a^L(0)=0,

the prescribed w(0)=0 makes all physical network updates and C updates
vanish forever; B0=tau h(0), B_k=0 for k>0, and the network remains f=0.
This follows by substitution and uniqueness. It is a precise initialization
obstruction to an unconditional fitting statement. Whether it has positive
probability for a fixed realizable dataset under Gaussian initialization is
a separate question; choosing labels after seeing initialization or using
an unrepresentable dataset does not answer that question.

**Finite order is not O(1) scalar state.** The fixed-q system stores
2qm(L-1)n moment coordinates, the outer weights, and the original fixed
operators W0 and their actual transposes. The scalar storages in (2) are not
a closed autonomous state: their derivatives require endpoint errors, whose
derivatives require nonlinear forward and backward fields. Even first and
second neuron moments do not determine basic tanh derivative statistics:
the four values (a,a,-a,-a) and (sqrt(2)a,0,-sqrt(2)a,0), for
0<a<1/sqrt(2), have the same mean and mean square but different fourth
moments. For h=tanh(z), the mean of tanh'(z)^2 is
1-2 mean(h^2)+mean(h^4), so those statistics differ. This refutes closure by
those particular aggregates, not every conceivable finite representation.
No finite scalar closure or Gaussian-coordinate independence has been
derived here.

## 6. Strongest next conjecture and the decisive gap

**Conjecture, not established:** Fix q=1,m=1,L=2, finite width n>=2, a
nonzero deterministic input, and a deterministic scalar target. Under the
independent Gaussian initialization in `MODEL.md`, the closure satisfies
f(t)->y almost surely as t->infinity.

The conjecture deliberately does not add pointwise loss monotonicity,
uniform-in-width rates, a finite scalar closure, or identification with a
dense flow. Section 4 proves its scalar-width counterpart. Section 3 rules
out finite-time blowup but leaves infinite-time escape and residual trapping
open. The central missing bridge is a reachable-history control on the last
term of (6), together with persistent readout sensitivity; filter passivity
alone supplies neither. A positive-probability family of nonfitting reachable
Gaussian initializations would falsify this conjecture. A loss-ascent point
outside the reachable set would not.

The highest-leverage next theoretical step is the first non-scalar case
n=2,L=2,m=1: establish a replacement for the scalar cone that controls
accumulated adverse alignment in (6), or construct a reachable obstruction.
Adding more moment orders without resolving this bridge would not itself
explain successful learning.
