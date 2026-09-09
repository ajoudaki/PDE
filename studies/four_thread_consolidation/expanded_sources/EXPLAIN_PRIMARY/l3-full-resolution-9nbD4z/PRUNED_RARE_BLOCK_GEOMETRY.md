# Gaussian geometry of a fully pruned middle block

This is a new reference-geometry lemma for the canonical two Gaussian
matrices. It concerns a fully pruned network, not the actual unpruned
trajectory. It does not prove the required full/pruned comparison.

Fix feature time S>0. For every deterministic middle index set E, use the
fully pruned zero-readout dynamics in PRUNED_GAUSSIAN_SUBSET_BOUND.md:
both h_E^(2) and delta_E^(2) vanish on E. An optional fixed smooth clipping
of the middle backward action may also be used. All bounds below are
independent of that prescribed clipping level.

Two initial blocks are entirely unused by this pruned dynamics:

    P_E W_0^(2),             W_0^(3) P_E.

The first is the collection of deleted incoming rows; the second is the
collection of deleted outgoing columns. The complete active trajectory
is measurable with respect to

    z_0^(1), (I-P_E)W_0^(2), W_0^(3)(I-P_E).

It is independent of both unused Gaussian blocks, which are also
independent of each other. The deleted rows of W_E^(2) and deleted columns
of W_E^(3) never train. We may still evaluate unused forward and backward
queries with those frozen blocks.

Write D_{1,E}(s)=diag(phi'(z_E^(1)(s))). The reference middle mobility
is the actual formula evaluated at the pruned lower state:

    A_E(s)=(||h_E^(1)(s)||2^2/n) I
                  + W_E^(2)(s) D_{1,E}(s)^2 (W_E^(2)(s))^T.

Its E-by-E block is exactly

    P_E A_E(s) P_E
       = (||h_E^(1)(s)||2^2/n) P_E
         + P_E W_0^(2) D_{1,E}(s)^2 (W_0^(2))^T P_E.       (1)

The main conclusion is that (1), restricted to the E coordinates, is
uniformly close to a scalar matrix for every small set E:

    alpha_E(s) I_E,
    alpha_E(s)= [||h_E^(1)(s)||2^2
                         + sum_i phi'(z_{E,i}^(1)(s))^2]/n.  (2)

The approximation error tends to zero as |E|/n tends to zero, uniformly
in feature time and in the choice of the deleted set. The proof below
specifies the finite-width probability and error.

## Conditional weighted Gaussian Gram estimate

The elementary estimate needed is valid for signed weights. Let G be an
m-by-n matrix with independent N(0,1/n) entries, independent of a real
diagonal matrix D with |D_jj|<=B, where B>0 is deterministic. Conditional
on D, for a fixed Euclidean unit vector u in R^m,

    u^T[G D G^T-(Tr D/n)I_m]u
       = (1/n) sum_j D_jj (g_j^2-1),                     (3)

where the g_j are independent standard Gaussians.

For |lambda|<=n/(4B), the logarithm of the exponential moment of (3)
is at most 2 lambda^2 B^2/n. Indeed, each factor has logarithm

    -lambda D_jj/n - (1/2)log(1-2lambda D_jj/n),

and -x/2-log(1-x)/2 <= x^2/2 for |x|<=1/2. Sum over j and use
sum_j D_jj^2<=nB^2. Applying this bound with both signs of lambda,
and choosing lambda=min(nt/(8B^2), n/(4B)), gives

    P(|(3)|>t | D)
       <= 2 exp[-min(nt^2/(16B^2), nt/(8B))].

In particular, for v>=0,

    P(|(3)|>8B[sqrt(v/n)+v/n] | D) <= 2exp(-v).

A Euclidean 1/4-net of the unit sphere in R^m has at most 9^m points.
For a symmetric matrix its operator norm is at most twice the maximum
absolute quadratic form over this net: replacing a maximizing unit
vector by a net point incurs at most half the operator norm. Hence

    P( ||G D G^T-(Tr D/n)I_m||op
         >16B[sqrt(v/n)+v/n] | D ) <= 2 9^m exp(-v).       (4)

Conditioning on arbitrary additional data independent of G is allowed.
In particular D can be a complicated function of the fully pruned
active trajectory.

## Simultaneous subsets and times

Suppose for each E a diagonal path D_E(s) depends only on the undeleted
initial blocks, satisfies |D_E,jj(s)|<=B, and satisfies

    ||D_E'(s)||F/sqrt(n) <= L

almost everywhere on the event that the two active initial operator norms
are at most M. Here L is independent of n,E. Outside that active-data
event replace the entire path by zero. This preserves independence from
the unused Gaussian block and makes the bounds unconditional.

Take N<=ceil(nS)+1 grid points, including 0 and S, with gaps at most 1/n.
For 0<alpha<1, put

    v_m=m log(en/m)+m log 9+log(2nN/alpha),   1<=m<=n.

Apply (4) at each grid time and to each subset of size m. There are at
most (en/m)^m such subsets. A union bound over times, sets, and m gives
probability at least 1-alpha for all these Gram bounds simultaneously.

For 0<p<=1, set

    b_n(p)=p[log(e/p)+log 9]+log(2nN/alpha)/n.

The function p[log(e/p)+log 9] is increasing on (0,1]. Thus all sets
with 1<=|E|<=pn satisfy the grid-time bound

    ||G_E D_E(s) G_E^T-(Tr D_E(s)/n)I_E||op
         <= 16B[sqrt(b_n(p))+b_n(p)].                    (5)

For the lower matrix, G_E consists of the rows P_EW_0^(2). For the top
matrix, G_E is the transpose of the columns W_0^(3)P_E. Each has the
required conditional Gaussian law.

Now intersect with the full initial norm event

    ||W_0^(2)||op<=M,          ||W_0^(3)||op<=M.

Every selected diagonal path is then the genuine one. Moreover
||D_E'(s)||op<=||D_E'(s)||F<=L sqrt(n). On this event the Gram matrix
is time-Lipschitz with constant M^2 L sqrt(n), while its scalar center
has time-Lipschitz constant L. Passing from a grid point to any time
adds at most

    M^2 L/sqrt(n)+L/n                                      (6)

to (5). No conditioning on the full norm event was used to assert
independence in (4).

For M=10, the probability of failure of the full norm event is at most
4 exp[-(25/2-2 log 9)n], by the two-sided spherical-net Gaussian bound
proved in PRUNED_GAUSSIAN_SUBSET_BOUND.md. Thus (5)--(6) have a completely
explicit high-probability meaning. Taking alpha=1/n makes the extra
grid term vanish with n for every fixed p.

## The lower rare block is approximately scalar and coercive

Apply this result with

    D_E(s)=D_{1,E}(s)^2,            B=1.

The derivative condition follows from the existing uniform primal bounds:
if ||(z_E^(1))'||2/sqrt(n)<=K_S, then

    ||(D_{1,E}^2)'||F/sqrt(n)<=4K_S,

because |phi'|<=1 and |phi''|<=2. The active-data norm selection in
the preceding proof is independent of both deleted Gaussian blocks.
The same bounds hold with the middle backward clipping.

Equations (1), (5), and (6) prove the stated uniform approximation
of P_E A_E P_E by alpha_E I_E. It has an important deterministic
lower bound that does not require a separate hidden-moment argument:

    phi(z)^2+phi'(z)^2 >= 1/4,       z in R.              (7)

If |z|<=1, then phi'(z)^2=(1+z^2)^(-2)>=1/4. If |z|>1, then
phi(z)^2>(pi/4)^2>1/4. Averaging proves

    1/4 <= alpha_E(s) <= a^2+1,          a=pi/2.

Consequently, whenever the error (5)--(6) is at most 1/8, every such
rare block has its smallest eigenvalue at least 1/8, uniformly in
time and deleted set. Its nonscalar part has operator norm at most
that same error, of order sqrt(p log(e/p)) as n tends to infinity.

## The analogous top rare response block

An additional application uses the signed diagonal path

    D_E(s)=diag(W_E^(4)(s) phi''(z_E^(3)(s))).

It is independent of W_0^(3)P_E and has B=2aS. Its normalized
derivative is bounded by

    2a+8aS J_S,

where ||(z_E^(3))'||2/sqrt(n)<=J_S, using |phi'''|<=8. Therefore

    (W_0^(3)P_E)^T D_E(s) (W_0^(3)P_E)

restricted to E is uniformly close to the scalar
(Tr D_E(s)/n) I_E, with the same form of error (5)--(6). The scalar
can have either sign. This is a bounded top-response coefficient,
not a positive energy.

For both applications on one event, use alpha/2 in each of their
probability bounds and take their intersection.

## Independent reference queries and precise scope

Conditional on the active initial data, the unused reference queries

    P_E W_0^(2) h_E^(1)(s),
    P_E (W_0^(3))^T delta_E^(3)(s)

have independent Gaussian coordinates within each vector. The two
vectors are conditionally independent of one another. Their variances
per coordinate are respectively ||h_E^(1)(s)||2^2/n and
||delta_E^(3)(s)||2^2/n. This is a statement about pruned reference
queries, not about the reused coordinates of the actual network.

The earlier simultaneous query proof applies to both vectors, using
their uniform normalized time-Lipschitz bounds and two union bounds.
It gives uniform small-set normalized norms of order
sqrt(p log(e/p)), plus terms vanishing with n.

The new information beyond those query norms is the nearly scalar
rare-block mobility (1)--(7), with a uniform positive scalar center.
This uses the canonical Gaussian incoming rows as well as outgoing
columns, which arbitrary bounded operators do not supply.

The ACTUAL unpruned first-layer gate depends on the deleted rows and
columns. It cannot replace D_{1,E} in the conditional Gram argument.
Similarly the actual top gate cannot replace the pruned top gate.
Any stability proof using this geometry must control the difference
between those actual and reference gates and the resulting bulk
response. No such replacement or full-network continuation is
proved by this lemma.
