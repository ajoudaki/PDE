# Permanent first-layer gate activity from the finite residual clock

2026-09-07. Root candidate, UNVERIFIED. This note proves an all-time
first-gate consequence of the finite-GF clock theorem. It is not a
population construction or a nonzero-velocity theorem.

The sole dependency is COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md, SHA256
cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b.
Its entire proof was read by the author. Its explicit raw equations,
Gaussian initialization, and successful event are used without change.
No experiment, external theorem, or modified gradient is used.

Fix the first activation phi_1(z)=integral_0^z phi_1'(u)du, where
phi_1' is smooth, even, positive on (-R,R), and zero outside that
interval. Set L_1=sup|phi_1''|>0. The upper activation is
phi_2(z)=z+epsilon arctan(z), epsilon>0 fixed, and M=1+epsilon.
Let the fixed inputs have squared norms d and inner product rho*d,
with -1<rho<1, and labels (1,-1). All three raw parameter blocks and
the rescaled readout have exactly the initialization and equations
(4)--(5), (37) of the dependency.

Write c_a(t)=-2(f_a(t)-y_a) and, with no residual inside the reverse
query, define

    q_a(t)=(W^(2)(t))^T [W^(3)(t) phi_2'(z^(2)_a(t))].

Products inside brackets are coordinatewise. Let G_(a,i)=z^(1)_(a,i)(0).
The first-layer equations at each row are exactly

    dot z^(1)_(1,i)=phi_1'(z^(1)_(1,i)) c_1 q_(1,i)
                    +rho phi_1'(z^(1)_(2,i)) c_2 q_(2,i),
    dot z^(1)_(2,i)=rho phi_1'(z^(1)_(1,i)) c_1 q_(1,i)
                    +phi_1'(z^(1)_(2,i)) c_2 q_(2,i).       (1)

Here and below all norms are ordinary Euclidean norms with the displayed
normalizations. On the successful event of Theorem 3 of the dependency,
its fixed constants U_* and X_* in (47)--(48) give

    sup_(t>=0) ||W^(2)(t)||_op <= U_*,
    integral_0^infinity sqrt(L(t)) ||W^(3)(t)||/sqrt(n) dt <= X_*.
                                                               (2)

These constants depend on the fixed activation and input correlation,
not on width or time. The event has probability at least 1-p_n with
p_n as explicitly given in (46) of the dependency, for n>=N_*.
Its finite-dimensional solution exists globally on every realization.

For each row put

    V_i=integral_0^infinity sum_(a=1)^2 |c_a(t)q_(a,i)(t)| dt,
    V_*=2sqrt(2) M U_* X_*.

Then on this same event

    (1/n) sum_i V_i^2 <= V_*^2.                           (3)

Indeed ||q_a(t)||/sqrt(n)<=M U_* ||W^(3)(t)||/sqrt(n), and
sum_a|c_a|<=2sqrt(2)sqrt(L). The Euclidean triangle inequality for
the two samples and for the time integral proves (3) first on every
finite interval. For the infinite integral, all integrands defining
V_i are nonnegative; take the monotone limit of their finite-interval
squares and sums. In particular every V_i is finite at each fixed n.
No independence of the V_i and the initialization is asserted.

Let Phi be the standard Gaussian distribution function and set

    m_rho=[2Phi(R/2)-1] * 2[1-Phi(3R/sqrt(1-rho^2))] >0,
    B_*=2 V_*/sqrt(m_rho),
    delta_*=(R/2) exp(-L_1 B_*),
    p_*=min_(|z|<=R-delta_*) phi_1'(z)>0.                 (4)

These are fixed finite constants (strictly positive where indicated).
For each ordered pair of distinct samples a,b define the initial strip

    S_a={i: |G_(a,i)|<=R/2,
              |G_(b,i)-rho G_(a,i)|>=3R}.                (5)

Claim: on the event (2) and |S_1|/n,|S_2|/n>=m_rho/2, each sample
has one fixed subset I_a of at least n m_rho/4 first rows such that

    |z^(1)_(a,i)(t)|<=R-delta_*  for every t>=0, i in I_a,
    inf_(t>=0) (1/n)sum_i phi_1'(z^(1)_(a,i)(t))^2
                        >= (m_rho/4) p_*^2 >0.          (6)

The subsets may depend on the entire trajectory but do not change
with time. The proof of their existence is deterministic.

First consider any row in S_a. Initially its a-coordinate is interior,
and its b-coordinate is exterior, since
|G_b|>=3R-|rho|R/2>R. As long as these strict inequalities persist,
the b gate is zero, so (1) gives the exact identities

    z_b(t)-rho z_a(t)=G_b-rho G_a,
    dot z_a(t)=phi_1'(z_a(t)) c_a(t)q_a(t).              (7)

For an interior scalar x, Lipschitz continuity of phi_1' and its zero
values at the endpoints imply
0<=phi_1'(x)<=L_1(R-|x|). The absolutely continuous distance
D(t)=R-|z_a(t)| therefore satisfies almost everywhere before exit

    dot D(t)>=-L_1 |c_a(t)q_a(t)| D(t).

Multiply by exp(L_1 integral_0^t |c_a q_a|) and integrate. Equations
(3), (5), and (7) imply before a putative finite exit

    D(t)>=(R/2)exp(-L_1 V_i)>0,
    |z_b(t)|>=3R-|rho|R>2R.                             (8)

Continuity preserves both strict margins at that exit, a contradiction.
Thus (7)--(8) hold for every finite time, with the same margins. This
also proves the assertions for the whole unbounded time axis; an exit
cannot occur at a finite time, and the lower bound is time independent.

By (3), the fraction of all rows with V_i>B_* is at most
V_*^2/B_*^2=m_rho/4. Set I_a=S_a intersect {V_i<=B_*}. Subtracting
this bound from |S_a|/n>=m_rho/2 yields |I_a|/n>=m_rho/4 for each
sample separately, even if all large-V rows lie in its strip. Equations
(4), (8) now prove (6). The minimum in (4) is strictly positive by
continuity and strict positivity on the compact interior interval.
No monotonicity of the gate or of the controls is used.

Finally the probability statement uses only initialization. The pairs
(G_(1,i),G_(2,i)) are iid centered Gaussians with covariance C. For an
ordered pair a,b, G_a and G_b-rho G_a are jointly Gaussian with zero
covariance and variances 1 and 1-rho^2. Their joint characteristic
function factors, so they are independent. Thus each membership
indicator in S_a has mean m_rho; distinct rows are independent.
The count variance is n m_rho(1-m_rho). Markov's inequality for the
squared centered count and a union bound give

    P(|S_1|/n<m_rho/2 or |S_2|/n<m_rho/2)
                   <=8(1-m_rho)/(n m_rho).              (9)

Combining (9) with the dependency's successful event requires no
independence between them. Therefore (6) holds for the ACTUAL finite
GF, for both samples simultaneously and all t>=0, with probability
at least max(0,1-p_n-8(1-m_rho)/(n m_rho)), whenever n>=N_*.
The activation is fixed across all interior input configurations;
constants may depend on the configuration and need not be uniform
as rho approaches an endpoint.

This proves permanent unsaturated first-gate mass, not permanent
nonzero force. In particular it does not lower-bound q, residuals,
velocities, or a reverse-field-weighted kernel. It proves no population
limit or top-layer nonaffinity. Antiparallel inputs and raw GD are not
included in this note. The first frozen-subset affine-fit argument is
compatible with this result, but is neither imported nor needed here.
