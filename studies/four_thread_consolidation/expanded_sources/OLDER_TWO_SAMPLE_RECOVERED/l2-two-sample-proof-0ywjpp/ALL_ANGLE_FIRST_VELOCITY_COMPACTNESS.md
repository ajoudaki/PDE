# Relative gates and strong first-velocity compactness

Root draft, 2026-09-06. UNREVIEWED. This note separates an elementary
deterministic implication from its application to the two actual
finite L=2 schemes. It does not construct a population limit or prove
its uniqueness. The only intended applications are arctan GF and exact
raw GD with the bounds spelled out below. No experiment or external
theorem is invoked.

## 1. The relative-gate estimate

Let p(z)=1/(1+z^2). Its logarithmic derivative is
-2z/(1+z^2), of absolute value at most one. For any x,y,

    |p(x)-p(y)|/(p(x)+p(y))
      =tanh(|log p(x)-log p(y)|/2)
      <=min(1,|x-y|/2).                                    (1)

If d=p(x)u and e=p(y)v, put theta equal to the ratio in (1).
Then, without dividing by u,v or a residual,

    |d-e|<=2|u-v|+theta(|d|+|e|).                         (2)

Indeed |d-e|<=p(x)|u-v|+|p(x)-p(y)||v|. The second term is
theta(p(x)+p(y))|v|. Since p(x)|v|<=|d|+p(x)|u-v|,
(2) follows from p<=1 and theta<=1. This uses BOTH endpoint
weighted fields, not a lower bound on p.

For a two-sample vector apply (2) componentwise. Replacing the two
ratios by their maximum gives the Euclidean bound with the same
coefficients, and that maximum is at most min(1,|x-y|/2).

## 2. Explicit uniform hypotheses on finite arrays

Use the product measure (1/n)sum_i dt on first-neuron coordinates
i=1,...,n and time in [0,T]. Fix rho in (-1,1), and
C=[[1,rho],[rho,1]]. Constants below may depend on this fixed rho.
There are two alternatives.

For continuous GF assume differentiable two-sample arrays z_i,u_i and

    d_i(t)=diag(p(z_i(t)))u_i(t), dot z_i=C d_i.             (3)

For exact raw GD with step eta, let bar z_i(t),u_i(t) be their
left-node step values on each cell, and assume

    d_i(t)=diag(p(bar z_i(t)))u_i(t), dot z_i=C d_i,         (4)

where z_i is the raw piecewise-affine interpolation of its endpoints.
Velocity statements are almost everywhere in time. The last cell may
be restricted to [0,T]. Put e=0 for GF and e=eta for GD.

Assume the following constants are bounded uniformly over the arrays:

    sup_t [(1/n)sum_i |dot z_i(t)|^2]^(1/2)<=K,
    [(1/n)sum_i integral_0^T |dot z_i|^3]^(1/3)<=J,
    [(1/n)sum_i (integral_0^T |dot z_i|^2)^2]^(1/2)<=A,
    (1/n)sum_i sup_t |z_i(t)|^4<=B.                       (5)

For GF also assume the analogous RMS bound K_u on dot u. For GD
assume each consecutive node difference of u has RMS at most K_u eta.
These imply, for 0<tau<T,

    ||u(.+tau)-u(.)||_(L2(dt times empirical))
       <=sqrt(T)K_u(tau+e).                              (6)

For GD there are at most tau/eta+1 crossed node increments; apply
the triangle inequality. For GF integrate dot u. The same argument
gives the RMS bound K(tau+eta) for the difference of bar z at two
shifted times in GD. For the actual interpolated z and for GF it
gives K tau.

These hypotheses hold, with finite constants, in the finite-GF and
exact-GD action estimates in the two explicitly named candidate notes
ALL_ANGLE_FIRST_LAYER_ACTION.md and ALL_ANGLE_RAW_GD_ACTION.md, on
their specified initial-norm and initial-fourth-moment bounds. To
verify this implication rather than import a new premise, use
u_{a,i}=c_a q^(1)_{a,i}. Those notes bound its time derivative or its
node increments in RMS, and its variation envelope U_i in RMS.
Their pointwise work bound gives integral |dot z_i|^2<=C U_i, hence
the third bound in (5). Their other bounds give K,J,B. No moment
of an unrestricted matrix action is being assumed here.

At rho=-1 with BOTH activations odd and labels (1,-1), the exact
finite network has opposite forward fields, equal reverse fields,
and opposite residual controls. Thus d_i=(d_{1,i},-d_{1,i}) and
dot z_i=2d_i. In this invariant case every argument below applies
with ||d_i||<=|dot z_i|/2 instead of inverting C. This covers the
antiparallel arctan case, including the actual nonzero finite readout.
No singular inverse is used. The aligned case rho=1 is not asserted.

## 3. First-velocity time-translation estimate

For rho in (-1,1), d_i=C^(-1)dot z_i, so

    ||d||_L3<=||C^(-1)||_op J.                            (7)

Use (2) at t and t+tau, with z for GF or bar z for GD. The maximum
ratio theta_i(t) is bounded by one and by half the corresponding
two-vector difference. Consequently

    ||theta||_L6^6<=||Delta z_or_bar_z||_L2^2/4
                    <=T K^2(tau+e)^2/4.                  (8)

Holder's inequality with exponents 6 and 3, followed by (6)--(8),
gives a finite constant C_T,rho such that

    ||d(.+tau)-d(.)||_L2
       <=C_T,rho[(tau+e)+(tau+e)^(1/3)].                  (9)

Multiplication by C gives the same bound for dot z. On tau+e<=T+1
the linear term can be absorbed by a horizon constant times the
one-third power. The antiparallel invariant case uses the bound
specified after (6) instead of (7). Constants need not be uniform
as a nondegenerate rho tends to +/-1.

For the recomputed first activation h=arctan(z), dot h=diag(p(z))
dot z. Its shifted difference is bounded by the difference of dot z
plus the product of dot z at one endpoint with
min(2,|Delta z|). This last multiplier's L6 norm is O(tau^(1/3)),
by its boundedness, the Lipschitz bound on p, and the RMS bound on
Delta z. Apply Holder again using the L3 velocity bound in (5).
Thus (9) also holds for dot h. In the GD case this calculation uses
the ACTUAL interpolated z in dot h; it is not a node activation
interpolation identity.

## 4. Finite-projection compactness of the velocity laws

We give the relevant approximation directly. For a uniform partition
of [0,T] into cells of length h=T/m, let P_h v be the cellwise time
average of an L2 velocity v. On a cell I, expanding the square proves

    integral_I |v-(1/h)integral_I v|^2
      =(1/(2h))integral_I integral_I |v(t)-v(s)|^2 ds dt.

Sum over cells and enlarge the integration region. Averaging over
neurons, (9) then gives

    (1/n)sum_i ||dot z_i-P_h dot z_i||_(L2[0,T])^2
       <=(1/h)integral_0^h
               ||dot z(.+tau)-dot z(.)||_L2^2 dtau
       <=C_T,rho (h+e)^(2/3).                           (10)

The same statement holds for dot h. For GF e=0. For a sequence of
GD widths e=n^-2 tends to zero; thus first let width tend to infinity
at fixed projection mesh, and then let h tend to zero. Finitely many
excluded small widths do not affect relative compactness of a sequence.

For a fixed h the projected velocities lie in a fixed finite-dimensional
space. Moreover (5) gives the FOURTH moment bound on their L2 path
norms:

    (1/n)sum_i ||P_h dot z_i||_(L2)^4
      <=(1/n)sum_i ||dot z_i||_(L2)^4<=A^2.               (11)

Hence their empirical probability measures are precompact in quadratic
Wasserstein distance on this finite-dimensional space. One direct
proof truncates a Euclidean ball using (11), covers the ball by finitely
many small cells, and passes to a subsequence of the finitely many
cell masses; the fourth moment makes the quadratic transport cost of
the discarded tail small. No independence of neurons is used.

The same-neuron coupling between a velocity and P_h of itself has
cost (10). A diagonal subsequence on finer projection meshes, with
these costs tending to zero, shows quadratic-Wasserstein precompactness
of the original velocity laws in L2([0,T];R^2). Completeness can also
be seen constructively: choose successively finer finite-support
approximants with summable L2 coupling errors, glue their finite
transport tables along their common marginals, and take the almost
sure and mean-square limit of the resulting Cauchy sequence in L2.

For JOINT first-position/velocity laws use the same-neuron finite
approximation (Pi_h z_i,P_h dot z_i). The polygonal position error
has empirical squared supremum norm at most
4h (1/n)sum_i integral|dot z_i|^2, by Cauchy--Schwarz on each cell.
The initial fourth moment and (5),(11) give uniform quadratic tails
of the resulting finite tuples. The previous finite-cell argument
therefore proves precompactness in

    W2( C([0,T];R^2) times L2([0,T];R^2) ).                 (12)

One may include h and dot h in the same tuple: the Lipschitz position
map and the bounds already proved give the same argument, with the
finite projection of dot h included explicitly.

If a sequence of these joint laws converges in (12), its limiting
position/velocity pair still satisfies z(t)=z(0)+integral_0^t v.
The set of pairs satisfying this equation is closed: uniform position
convergence and L2 velocity convergence give uniform convergence of
the integrals by Cauchy--Schwarz. The integral of squared velocity
also converges under W2 convergence, since it is the squared norm of
the second coordinate and its quadratic tails are uniformly controlled.
This rules out a FIRST-layer kinetic-energy defect along these
subsequences. It does not identify the limiting velocity equation.

## 5. Scope

The deduction (5)--(12) uses actual first-layer work bounds and the
bounded logarithmic derivative of the arctan gate. It controls
time translations of the first velocities and yields stronger
first-layer compactness than weak path tightness alone. Both sample
coordinates stay in the same neuron tuple; no post-training iid
assertion is made.

The global finite-GF/raw-GD moment estimates named in Section 2 must
be independently verified before promoting their application here.
Even then this proves neither joint identification of reused Gaussian
matrix queries along a full trajectory, higher-moment action bounds
for either matrix orientation, second-layer kinetic-energy compactness,
nor uniqueness/restart of an uncut population flow at general angles.
Those remain genuinely additional obligations.
