# An adaptive rare-block modulus for the actual first-layer gate

## Scope

This is a finite-width Gaussian geometry lemma and its deterministic
application to a full/pruned comparison. It controls the change of the
rare E-by-E middle mobility block even though the actual gate depends
on the deleted Gaussian rows. It does not prove stability of the bulk
trajectory, nor a global population limit.

Write h(p)=p log(e/p) for 0<p<=1 and h(0)=0. Let

    omega(d)=d[1+log_+(1/d)],    d>0,       omega(0)=0.

Thus omega(d)=d log(e/d) for d<=1 and omega(d)=d for d>=1.
All matrix operator norms are ordinary Euclidean operator norms;
vector norms ||v||_n mean ||v||_2/sqrt(n).

## One event controls every Gaussian submatrix

Let W be n-by-n with independent N(0,1/n) entries. For 0<alpha<1 set

    q_n=log(2n^2/alpha)/n,
    C_0=8(1+log 9).

With probability at least 1-alpha, simultaneously for every row set E
and column set F,

    ||W_{E,F}||_op^2
       <= C_0[h(|E|/n)+h(|F|/n)+q_n].                  (1)

Here an empty submatrix has norm zero. To prove (1), fix nonempty sets
of sizes m,l and take 1/4-nets of their unit spheres, with at most
9^m and 9^l points. The matrix norm is at most twice the maximum
bilinear form over these nets. For fixed unit vectors u,v, u^T W v
is N(0,1/n). Thus, for a threshold t,

    P(||W_{E,F}||_op>t) <= 2*9^(m+l) exp(-n t^2/8).

Choose

    t^2=(8/n)[(m+l)log 9+m log(en/m)+l log(en/l)
                                      +log(2n^2/alpha)].

There are at most (en/m)^m(en/l)^l pairs of sets of these sizes.
The total failure probability for these sizes is at most alpha/n^2.
Sum over 1<=m,l<=n. Since h(p)>=p, the resulting threshold is
bounded by the right side of (1).

## Arbitrary adaptive signed diagonals

On the same event, for every E and EVERY vector a in [-1,1]^n,
including one selected using all of W and an entire trained trajectory,

    ||W_E diag(a) W_E^T||_op
       <= C_0[h(|E|/n)+h(n^(-1)sum_j|a_j|)+q_n].        (2)

No independence of a and W is required. Indeed the norm of the signed
matrix is at most that of W_E diag(|a|) W_E^T, by the two Loewner
inequalities obtained from -|a|<=a<=|a|. With

    F_t={j: |a_j|>t},       rho(t)=|F_t|/n,

the layer-cake identity gives

    W_E diag(|a|) W_E^T
       = integral_0^1 W_{E,F_t} W_{E,F_t}^T dt.

Apply (1) under the integral. Concavity of h and Jensen give

    integral_0^1 h(rho(t))dt
       <= h(integral_0^1 rho(t)dt)
       = h(n^(-1)sum_j|a_j|),

which proves (2). The simultaneous submatrix event justifies applying
this argument to arbitrary adaptive level sets without any further
union bound or conditioning.

## Actual-versus-pruned rare self-blocks

Use W=W_0^(2). Let a full state and its fully pruned reference for E
have first-layer coordinates z,z^E, transformed coordinates
X=F(z), X^E=F(z^E), and matrices U=W^(2), V=W_E^(2). Suppose

    ||U||_op, ||V||_op <= M,
    d=||X-X^E||_n+||U-V||_op.

The state distance in the local proof dominates this d. The reference
has the exact frozen-row identity

    P_E V=P_E W_0^(2),                                  (3)

because its backward field vanishes on E, so these rows never train.
This identity holds with or without any prescribed middle clipping.

Define the two middle mobility matrices

    A=||phi(z)||_n^2 I+U diag(phi'(z)^2) U^T,
    A^E=||phi(z^E)||_n^2 I+V diag(phi'(z^E)^2) V^T.

Then, on the event (1),

    ||P_E(A-A^E)P_E||_op
       <= C_M[omega(d)+h(|E|/n)+q_n],                   (4)

where C_M is deterministic and independent of E, width, time, or
clipping. The estimate holds simultaneously for every pair of states
satisfying the indicated norm bound and (3).

To check this, put D=diag(phi'(z)^2), D^E=diag(phi'(z^E)^2). Expand

    U D U^T-V D^E V^T
      =(U-V)D U^T+V D(U-V)^T+V(D-D^E)V^T.

The first two terms have norm at most 2M||U-V||_op. In particular,
differences of the learned matrix updates cost at most C_M d, with
no Frobenius bound or entrywise comparison needed. The scalar centers
differ by at most 2a||X-X^E||_n, where a=pi/2, because phi and F^(-1)
are 1-Lipschitz and |phi|<=a.

For the last term restricted to E, use (3) and (2) with

    a_j=phi'(z_j)^2-phi'(z_j^E)^2.

These signed entries have magnitude at most one. Also

    n^(-1)sum_j|a_j| <= 4||X-X^E||_n <= 4d,             (5)

since |(phi'^2)'|<=4 and F^(-1) is 1-Lipschitz. The mean in (5) is
also at most one. For every d>=0,

    h(min{1,4d}) <= 4 omega(d).

For d<=1/4 this follows by substitution; for d>=1/4 use h<=1<=4d.
Combining the estimates proves (4), for example with
C_M=2a+2M+4C_0. Thus (4) does not leave large distances undefined.

## Combination with the independent pruned Gram lemma

Let r_n(p) denote the explicit error in PRUNED_RARE_BLOCK_GEOMETRY.md,
including its time-grid error and its chosen failure probability. That
lemma gives, simultaneously for all |E|<=pn and all s<=S,

    ||P_E A^E(s)P_E-alpha_E(s)I_E||_op <= r_n(p),
    1/4 <= alpha_E(s) <= a^2+1.

Intersect its event with (1), allocating their failure probabilities
separately. The actual rare self-block then obeys

    ||P_E A(s)P_E-alpha_E(s)I_E||_op
       <= r_n(p)+C_M[omega(d_E(s))+h(p)+q_n].           (6)

For each fixed p, q_n tends to zero if alpha=1/n; after that r_n(p)
and h(p) tend to zero as p decreases. If d_E(s) is small, (6) retains
the approximately scalar, coercive reference block for the actual
adaptive gate. Since the event controls all signed diagonals and all
sets, no additional time grid is needed for (4) or (6).

This resolves an actual-versus-reference gate replacement for the
rare self-block. It does not control the rare-to-bulk blocks, establish
a bound on d_E(s), or remove the remaining unbounded products after
the arctangent characteristic transformation. Those steps remain open.
