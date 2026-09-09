# An actual two-time rare-return estimate

## Scope and notation

This note extends the rare self-block geometry to the actual retarded
tangent kernel. It proves a short-time-separation operator estimate for
the same rare set at both ends, and consequently for two disjoint sets
whose union is rare. It does not control rare-to-large-bulk transport
or the unbounded middle curvature
multiplier. It does not establish global continuation.

Use the actual uncut feature-time tangent decomposition from
ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md:

    y'=L_s y+R_s M_(b_s) T_s y+f_s,
    T_s y=A H1(s)+W2(s) D1(s)^2 x,
    R_t v=(W2(t)^*v, v tensor H1(t), 0, 0).

Let U_L(s,t) be the propagator of L and define

    K(s,t)=T_s U_L(s,t)R_t,        0<=t<=s<=S.

All vector norms are normalized Euclidean norms and the tangent state
uses L2 vector norms and HS/Frobenius matrix norms. On the established
primal bounds, ||L_s||, ||T_s||, ||R_s||<=C_S independently of width
and max|q2|. The estimates below are on the corresponding common
initial-operator event.

Fix E and a fully pruned reference, with or without a prescribed middle
clipping level. Denote its lower fields by hats and its second matrix
by V_s. Let d_E(s) be the full state distance used in the local proof;
in particular it dominates

    ||X1(s)-X1hat(s)||_n+||W2(s)-V_s||_op.

Write h(p)=p log(e/p), h(0)=0, and
omega(d)=d[1+log_+(1/d)], omega(0)=0.

## Exact algebra before any probabilistic estimate

Direct composition gives

    T_s R_t
      = <H1(s),H1(t)> I+W2(s)D1(s)^2 W2(t)^*.          (1)

No derivative of T in operator norm is used. The bounded propagator
satisfies

    ||U_L(s,t)-I|| <= exp(C_S(s-t))-1 <= C'_S(s-t),

and hence

    ||K(s,t)-T_sR_t||_op <= C'_S(s-t).                 (2)

This separates the bounded tangent propagation from the unbounded
middle multiplier, which is outside K in the Volterra equation.

For the reference, the deleted rows are frozen at both times:

    P_E V_s=P_E V_t=P_E W_0^(2).

Therefore its analogue of (1), compressed to E, is exactly

    <H1hat(s),H1hat(t)> I_E
      +W_0,E^(2) D1hat(s)^2 (W_0,E^(2))^T.              (3)

Its scalar center is

    alpha_E(s,t)=<H1hat(s),H1hat(t)>
                          +mean[D1hat(s)^2].           (4)

In particular the Gram part of (3) involves one diagonal at time s;
no two-time Gaussian conditioning assumption is needed.

## Adaptive actual-versus-reference comparison

On the simultaneous submatrix event of
ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md, set

    q_n=log(2n^2/alpha_sub)/n.

For every pair s,t and every E of mass at most p, the difference
between the actual compression of (1) and (3) is at most

    C_S[omega(d_E(s))+d_E(t)+h(p)+q_n].                (5)

To verify this, write U_s=W2(s), D_s=D1(s)^2 and
hat D_s=D1hat(s)^2. Expand the matrix term as

    U_s D_s U_t^*-V_s hat D_s V_t^*
      =(U_s-V_s)D_s U_t^*
         +V_s D_s(U_t-V_t)^*
         +V_s(D_s-hat D_s)V_t^*.

The first two terms are bounded by C_S[d_E(s)+d_E(t)].
After compression, the last term is exactly

    W_0,E^(2)(D_s-hat D_s)(W_0,E^(2))^T.

The signed diagonal has magnitude at most one and mean absolute
value at most 4d_E(s). The adaptive signed-diagonal lemma bounds this
term by C[h(p)+omega(d_E(s))+q_n]. The scalar inner-product difference
is at most a[d_E(s)+d_E(t)], since both feature vectors are bounded
by a=pi/2 and their L2 differences are bounded by the transformed
first-layer differences. This proves (5) at all distances.

All sets and signed diagonals are covered on one submatrix event.
Consequently no time grid or independence of the actual gate is used
in (5).

## Two-time return near a scalar matrix

Let r_n(p) be the explicit uniform reference Gram error from
PRUNED_RARE_BLOCK_GEOMETRY.md, with its probability allocation and
time interpolation terms. Intersect its event with the submatrix
event above. Equations (2)--(5) give simultaneously for every
|E|<=pn and every 0<=t<=s<=S,

    ||P_E K(s,t)P_E-alpha_E(s,t) I_E||_op
      <= r_n(p)+C_S[(s-t)+omega(d_E(s))+d_E(t)
                                             +h(p)+q_n]. (6)

The failure probabilities of the two Gaussian events are added;
the full initial-operator event is imposed as in the reference lemma.
For example, choosing both probability allocations proportional to
1/n makes the width-dependent errors vanish. No independence between
the two good events is required.

The scalar center remains positive close to the diagonal. Indeed

    alpha_E(s,s)=mean[phi(zhat1(s))^2+phi'(zhat1(s))^2]
                  >=1/4.

The uniform reference velocity bound
||H1hat'(u)||_n<=L_S gives

    |alpha_E(s,t)-alpha_E(s,s)| <= a L_S(s-t).

Thus alpha_E(s,t)>=1/8 whenever aL_S(s-t)<=1/8. If L_S=0 there
is no restriction from this condition. If the right side of (6)
is also at most 1/16, then for every real vector v supported in E,

    <v,K(s,t)v> >= (1/16)||v||_n^2.

This is coercivity of the symmetric part of the compressed kernel.
At different times K need not be self-adjoint, so a claim that all
its eigenvalues are real would be incorrect.

## Disjoint rare supports through their jointly pruned reference

Let E and F be disjoint and put D=E union F. Apply (6) with the
FULLY pruned reference for D, not with either singly pruned reference.
If |D|<=pn, multiplying (6) on the left by P_E and on the right by
P_F annihilates its scalar term. Therefore

    ||P_E K(s,t)P_F||_op
      <= r_n(p)+C_S[(s-t)+omega(d_D(s))+d_D(t)
                                             +h(p)+q_n]. (7)

All sets D were already included in the simultaneous event, so this
requires neither a further union bound nor independence of the
selection of E and F. The distance in (7) is to the network with
the ENTIRE union D pruned. A distance to only one of the two
pruned networks cannot be silently substituted.

Thus close-to-diagonal transfer between two rare supports has a
small conditional-on-closeness bound. If one support is the large
complement of the other, their union need not be rare and (7)
does not give a small bound.

## Remaining limitation

The estimate covers a genuine two-time return of the actual tangent
system, not only its instantaneous mobility. It does not give a small
rare-to-large-bulk estimate, or control multiplication by
b_t=phi''(z2(t))q2(t) in the time-ordered expansion. It also requires
the explicitly displayed full/pruned distances to be small before
its scalar approximation is small. Those distances have not been
controlled by this note. No global response-moment or continuation
claim follows from (6) alone.
