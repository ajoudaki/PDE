# A necessary fitting scale for every fixed depth

This is a conditional lower bound for the accepted convex mixture. It
does not assert existence or successful fitting of a global population
flow. It explains why decreasing theta is not uniformly a small change
to the trained trajectory for three inputs.

Fix L>=2 and phi_theta(z)=a z+theta atan z, a=1-theta, 0<theta<=1/2.
Take three unit planar directions u_1+u_2+u_3=0 with pairwise inner
products -1/2, and all three labels equal to +1. Multiplying by sqrt(d)
gives the original input normalization for every fixed d>=2. This triple
obeys |rho_ij|<=1-delta whenever 0<delta<=1/2.

For any raw parameter state, let S_ell=sum_i h_i^ell and
T_ell=sum_i atan(z_i^ell). Linearity of the first preactivation gives
sum_i z_i^1=0, so the exact recursions are

    S_1=theta T_1,
    S_ell=a A_ell S_(ell-1)+theta T_ell,
    ||T_ell||_2<=3*pi/2.

Consequently

    ||S_L||_2 <= (3*pi*theta/2)
       sum_(k=1)^L a^(L-k) product_(j=k+1)^L ||A_j||op.       (1)

The empty product for k=L is one. This bound uses no distributional
assumption on the trained fields.

Suppose this state has loss E=||f-1||²/2<=3/8. Then
|sum_i(f_i-1)|<=sqrt(3)||f-1||<=3/2, hence sum_i f_i>=3/2.
Since sum_i f_i=<C,S_L>, (1) implies

    ||C||_2 sum_(k=1)^L a^(L-k) product_(j=k+1)^L ||A_j||op
                                      >=1/(pi*theta).       (2)

At canonical initialization C_0=0 and every initialized adjacent
action has norm at most two. Let R be joint raw distance from that
initialization, including all hidden blocks and the readout. Then
||C||_2<=R and ||A_j||op<=2+R. Therefore

    R sum_(k=0)^(L-1) [a(2+R)]^k >=1/(pi*theta),
    R L(2+R)^(L-1) >=1/(pi*theta),
    R >= [(pi*L*theta)^(-1/L)-2]_+.                         (3)

Thus no theta-independent bounded raw neighborhood can contain a
successful fitting state for this example.

There is a sharper asymptotic constant using the joint metric. Put
c=||C||_2 and d_j=||A_j-A_j,0||HS for j=2,...,L, so
c²+sum_j d_j²<=R². The leading-degree term in the left side of (2),
after bounding ||A_j||op by 2+d_j, is no larger than

    c product_(j=2)^L d_j <=(R²/L)^(L/2),                  (4)

by the arithmetic-geometric mean inequality. All the remaining terms
have degree at most L-1 in c,d_2,...,d_L, have nonnegative coefficients
bounded in terms of L, and hence total at most C_L(1+R)^(L-1).
The coefficient a^(L-1) of the leading term is at most one.
Equations (2)--(4), together with the fact R tends to infinity as theta
tends to zero, prove for any family of such successful states

    liminf_(theta->0) theta^(1/L) R
                                >=sqrt(L)*pi^(-1/L).       (5)

To justify the limit if the left side is finite, pass to a subsequence
where theta^(1/L)R stays bounded; theta(1+R)^(L-1) tends to zero there.
Multiply (2) by theta and apply (4). If no bounded subsequence exists,
(5) is automatic.

If a true strong raw GF reaches E<=3/8 at time T, its exact energy
identity and Cauchy--Schwarz give

    R² <= T integral_0^T ||dot Theta||raw² dt <=(3/2)T.

Combining with (3) and (5) yields

    T >=(2/3)[(pi*L*theta)^(-1/L)-2]_+²,
    liminf_(theta->0) theta^(2/L)T
                              >=(2L/3)*pi^(-2/L).          (6)

At L=2 this recovers the leading constant 4/(3*pi) in the earlier
two-hidden-layer necessary fitting-time estimate. These are necessary
bounds, not matching convergence-time upper bounds. They concern a
fixed L as theta decreases and do not claim sharpness of the depth
dependence of successful training.

In particular a loss-decay rate depending only on delta and L, with a
theta-independent finite prefactor, cannot hold uniformly over all
positive theta below a cutoff for this admissible family: it would
force a bounded time to reach loss 3/8, contradicting (6). A rate that
depends on theta, or a theorem choosing one fixed positive theta for
each delta,L, remains possible. Nothing here disproves either version.

## A stronger time order from first exit at a fixed raw radius

For every fixed L, the true-gradient energy identity also gives a
necessary inverse-theta time scale. Define

    B_L=sum_(k=0)^(L-1) 3^k=(3^L-1)/2.

Assume theta<1/(pi B_L), and suppose a true strong raw GF reaches
E<=3/8 at time T. A successful state must have R>1: if R<=1, the
left side of the first inequality in (3) is at most B_L, contradicting
1/(pi theta)>B_L. By continuity there is a first time t_1<=T at which
the joint raw distance from initialization equals one.

At t_1, the readout norm is at most one and each adjacent action norm
is at most three. The exact feature-sum estimate (1), with a<=1,
therefore gives

    sum_i f_i(t_1)<=|<C,S_L>|<=(3*pi*theta/2) B_L.

The initial predictions vanish, so the exact loss difference is

    E(0)-E(t_1)=sum_i f_i(t_1)-(1/2)sum_i f_i(t_1)^2
                         <=(3*pi*theta/2) B_L.

On the other hand, Cauchy--Schwarz and the true energy identity imply

    1=R(t_1)^2
       <=t_1 integral_0^(t_1) ||dot Theta||raw^2 dt
       =t_1 [E(0)-E(t_1)].

Consequently every such successful trajectory satisfies

    T>=t_1>=4/[3*pi*(3^L-1)*theta].                       (7)

For any family of successful true strong flows at fixed L this yields

    liminf_(theta->0) theta T>=4/[3*pi*(3^L-1)]>0.

In particular, when L>2,

    liminf_(theta->0) theta^(2/L) T=+infinity.             (8)

Thus (7) improves the theta exponent in the earlier necessary time
bound at every fixed depth L>2. It uses neither sample symmetry nor
a uniqueness assertion, only a true strong solution and its energy
identity. This remains a conditional obstruction to uniformly fast
fitting; it does not prove existence or successful fitting, or supply
a matching time upper bound.
