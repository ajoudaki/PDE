# Sign switches can generate a hyperbolic control loop — root draft, unaudited

2026-09-06. This is a PRESCRIBED-control discriminator for the new
Gaussian gate, not a trained-network counterexample. No actual
backpropagation query is asserted to follow the constructed schedule.
The proof is written for independent checking before any promotion.

Let p(z)=epsilon exp(-z²), epsilon=1/10, and fix 0<|rho|<1.
Set C=[[1,rho],[rho,1]], and define two smooth bounded vector fields

  X_1(z)=p(z_1)Ce_1, X_2(z)=p(z_2)Ce_2.

The control equation is z'=u_1(t)X_1(z)+u_2(t)X_2(z).
Every field and each fixed derivative is bounded. Write Phi_a^s for
the complete flow of X_a, which exists and is smooth by its integral
equation and the bounded-derivative estimates.

For all sufficiently small fixed tau>0 there is an initial point
z_tau=O(tau) and a period-4tau piecewise constant control taking
the successive values e_1,e_2,-e_1,-e_2, such that after N periods

  ||D_z_tau z(4tau N)|| >= exp(c_tau N), c_tau>0.      (1)

The total absolute control cost is proportional to N. Consequently
no polynomial in that cost, with constants even allowed to depend
on rho and z_tau, bounds these frozen-control tangents uniformly
over sign-changing controls. The same failure can be placed on the
fixed interval [0,1] by time-rescaling the prescribed control.

## 1. The return map and its second-order term

The one-period return map is

  P_tau=Phi_2^(-tau) composed Phi_1^(-tau)
                         composed Phi_2^tau composed Phi_1^tau.

Uniformly with its first state derivative near zero,

  P_tau(z)=z+tau² B(z)+O(tau³),
  B=DX_2 X_1-DX_1 X_2.                               (2)

For an explicit sign check, write a=X_1(z), b=X_2(z), A=DX_1(z),
D=DX_2(z). The first two flow steps give
z+tau(a+b)+tau²(Aa/2+Da+Db/2)+O(tau³).
The negative first-field step gives
z+tau b+tau²(Da-Ab+Db/2)+O(tau³), and the negative second-field
step cancels tau b and Db/2, leaving tau²(Da-Ab).
This proves the coefficient in (2). Uniform C1 remainders follow
by applying the time Taylor formula to each smooth flow and its
variational equation; on a fixed small ball the needed derivatives
through order four are bounded. The same Taylor formula shows
G(tau,z)=(P_tau(z)-z)/tau² extends continuously with its state
derivative to tau=0, where it equals B(z).

Direct differentiation of the vector fields gives

  B(z)=rho[p(z_1)p'(z_2)Ce_2-p(z_2)p'(z_1)Ce_1].

Since p(0)=epsilon, p'(0)=0, p''(0)=-2epsilon,

  B(0)=0,
  M:=DB(0)=2rho epsilon² C diag(1,-1),
  M²=4rho² epsilon^4(1-rho²)I.

Thus M has two distinct real eigenvalues +-lambda, where
lambda=2|rho|epsilon² sqrt(1-rho²)>0. In particular M is invertible.

## 2. An actual fixed point, not just a formal bracket trajectory

Here is a direct contraction argument supplying a genuine return
point. For z in a sufficiently small fixed closed ball around zero,
DB(z) is as close to M as desired. From the uniform C1 remainder
in (2), D_zG(tau,z)=DB(z)+O(tau). Consequently

  Psi_tau(z)=z-M^-1 G(tau,z)

has Lipschitz constant at most 1/2 on that ball for sufficiently
small tau. Also G(tau,0)=O(tau), so Psi_tau(0)=O(tau). Reducing tau
further makes the ball invariant under Psi_tau. Iterating this
contraction gives a unique fixed point z_tau in the ball, with
||z_tau||<=2||Psi_tau(0)||=O(tau). Its defining equation is
G(tau,z_tau)=0, equivalently P_tau(z_tau)=z_tau.

The state derivative of (2) at this point is

  DP_tau(z_tau)=I+tau²[M+O(tau)].                     (3)

The real two-by-two matrix in brackets has, for sufficiently small
tau, distinct real eigenvalues mu_+,mu_- with mu_+>=lambda/2 and
mu_-<=-lambda/2. For example its characteristic discriminant tends
to 4lambda²>0, and the quadratic formula makes the roots continuous.
It follows that DP_tau(z_tau) has a real unit eigenvector with
eigenvalue at least 1+lambda tau²/2.

After N repetitions the orbit returns to z_tau, so the derivative
of the full return is DP_tau(z_tau)^N. Evaluating on that eigenvector,

  ||DP_tau(z_tau)^N|| >=(1+lambda tau²/2)^N
                         >=exp(lambda tau² N/4),     (4)

where tau was reduced to make lambda tau²/2<=1, and log(1+x)>=x/2
for 0<=x<=1 follows by integrating 1/(1+x)>=1/2. This proves (1).
There is no inference from an instantaneous eigenvalue alone: the
same fixed return point and return derivative repeat at each period.

## 3. Cost, rescaling, and exact boundary

The L1 cost integral over N periods is 4tau N. With the activation-
scaled convention U=epsilon integral||u||_1, it is 4epsilon tau N.
Thus (4) grows exponentially in U with a positive coefficient for
each fixed small tau. A finite-power polynomial cannot dominate it.

If the N-period horizon is T_N=4tau N, define on [0,1] the prescribed
schedule u_N(s)=T_N u(T_N s). Its solution from any initial point is
the old solution at time T_N s. The tangent at time one and the
total cost are unchanged. Both controls are held fixed under initial-
state differentiation. The class here requires only integrability,
which this piecewise constant schedule satisfies.

The example does not contradict a bound for controls confined to
one fixed sign quadrant. It crosses quadrants every quarter-period.
It also does not contradict the exact weighted-area determinant
identity of a Gaussian gate: a hyperbolic return expands one
direction and contracts another. Neither area preservation nor an
initial response sign is a bound on the largest singular value.

Most importantly, this does NOT prove that canonical gradient flow
can generate the periodic control schedule. Full-network gradient
ascent has additional coupling and energy identities absent here.
No failure of the requested two-sample theorem, no failure of its
Gaussian initialization, and no impossibility of this activation
follow. The conclusion is only that a universal polynomial bound
for all exogenous sign-changing controls cannot be the missing
continuation bridge for the Gaussian-gate strategy.
