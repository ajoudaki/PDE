# A simultaneous Gaussian bound for fully pruned middle populations

Status: a finite-width probability lemma, not a proof of the global
three-layer limit. The comparison network below is fully pruned, not a
copy of the top block driven by the actual unpruned bulk trajectory.
That distinction is essential for independence.

Fix a feature-time horizon S>0 and n. All vector norms below are ordinary
Euclidean norms. Put a=pi/2. Start with the canonical independent Gaussian
matrices W_0^(2), W_0^(3), whose entries have variance 1/n, and the canonical
first-layer initialization. For this lemma take the readout initially zero.
The tiny finite readout is not included in this statement.

For each deterministic set E of middle-neuron indices let P_E be the diagonal
coordinate projection onto E, and construct a separate, fully pruned network.
All its variables in the following definitions carry an E subscript.
Define

    h_E^(1)=phi(z_E^(1)),
    z_E^(2)=W_E^(2) h_E^(1),
    h_E^(2)=(I-P_E) phi(z_E^(2)),
    z_E^(3)=W_E^(3) h_E^(2),       h_E^(3)=phi(z_E^(3)),
    delta_E^(3)=W_E^(4) phi'(z_E^(3)),
    delta_E^(2)=(I-P_E) phi'(z_E^(2)) (W_E^(3))^T delta_E^(3).

Products of equal-sized vectors here are coordinatewise. The complete
feature-flow equations are

    (z_E^(1))'=phi'(z_E^(1)) (W_E^(2))^T delta_E^(2),
    (W_E^(2))'=delta_E^(2) (h_E^(1))^T/n,
    (W_E^(3))'=delta_E^(3) (h_E^(2))^T/n,
    (W_E^(4))'=h_E^(3).

Initialization is shared with the full network. These are the training
equations for the pruned prediction: deleting the activation also deletes
the corresponding backward gate. In particular, the columns of W_E^(3)
indexed by E never change and never contribute to its forward pass.
Consequently the entire trajectory delta_E^(3) is a function of

    z_0^(1), W_0^(2), W_0^(3)(I-P_E),

and does not depend on the deleted Gaussian columns W_0^(3)P_E.

We first make the required deterministic uniform bounds explicit.
Suppose ||W_0^(2)||op and ||W_0^(3)(I-P_E)||op are at most M. The irrelevant
deleted columns can be set to zero when deriving these bounds, since neither
the active forward pass nor the active backward gate uses them. For 0<=s<=S,

    ||W_E^(4)(s)||infinity <= aS,
    ||delta_E^(3)(s)||2/sqrt(n) <= aS = B,
    ||W_E^(3)(s)(I-P_E)||op <= M+a^2 S^2/2 = M3,
    ||delta_E^(2)(s)||2/sqrt(n) <= M3 aS,
    ||W_E^(2)(s)||op <= M+a^2 M3 S^2/2 = M2.

The last bound follows by integrating
||(W_E^(2))'||op <= a ||delta_E^(2)||2/sqrt(n).
The displayed constants may overestimate the integrals; they are independent
of E and n. These bounds and the corresponding first-layer velocity bound
exclude finite-time escape in this finite-dimensional smooth ODE.

Differentiating the second preactivation gives

    (z_E^(2))'=
      [ (||h_E^(1)||2^2/n) I
        + W_E^(2) diag(phi'(z_E^(1))^2) (W_E^(2))^T ]
        delta_E^(2).

Therefore

    ||(h_E^(2))'||2/sqrt(n)
      <= (a^2+M2^2) M3 aS,

and differentiating z_E^(3) gives

    ||(z_E^(3))'||2/sqrt(n)
      <= a^3 S + M3^2 (a^2+M2^2) aS = J3.

Since |phi'|<=1 and |phi''|<=2,

    ||(delta_E^(3))'||2/sqrt(n) <= a+2aS J3 = L.

Thus the top backward trajectory has a uniform normalized norm bound B and
a uniform normalized time-Lipschitz constant L.

For every E define beta_E(s) to be delta_E^(3)(s) if the two initial
operator bounds above hold, and the zero vector for every s otherwise.
This selection event depends only on the undeleted data. Hence beta_E,
as a complete trajectory, is independent of W_0^(3)P_E, and the bounds
B,L now hold without any conditioning on a norm event involving deleted
columns.

For a fixed deterministic E of size m and a fixed s, conditional on all
undeleted data, the coordinates in

    P_E (W_0^(3))^T beta_E(s)

are independent centered Gaussians with variance
||beta_E(s)||2^2/n <= B^2. If the variance is zero the vector is zero.
For m independent standard Gaussians G_1,...,G_m and u>=0,

    P(sum G_i^2 >= 4(m+u))
      <= exp[-m-u] 2^(m/2) <= exp[-u].

This is Markov's inequality applied to exp(sum G_i^2/4); its expectation
is 2^(m/2). Consequently

    P( ||P_E (W_0^(3))^T beta_E(s)||2^2/n
         > 4 B^2 (m+u)/n ) <= exp[-u].

Take a deterministic time grid of N points containing 0 and S whose largest
gap is at most 1/n. One can choose N<=ceil(nS)+1. Fix alpha in (0,1), and,
for each 1<=m<=n, set

    u_m=m log(en/m)+log(nN/alpha).

There are at most (en/m)^m subsets of size m. A union bound over all subsets,
all m, and all grid points gives an event of probability at least 1-alpha
on which every such query satisfies

    ||P_E (W_0^(3))^T beta_E(s)||2^2/n
      <= 4 B^2 [ (m/n)(1+log(en/m)) + log(nN/alpha)/n ].

No independence between different subsets or different times is used.
For 0<epsilon<=1 the function x(1+log(e/x)) is increasing on (0,1].
Thus, on this same event, all subsets with 1<=|E|<=epsilon n satisfy
at every grid time

    ||P_E (W_0^(3))^T beta_E(s)||2/sqrt(n)
      <= 2B sqrt[ epsilon(1+log(e/epsilon))
                         + log(nN/alpha)/n ].

The empty subset has zero query. On the additional event

    ||W_0^(2)||op<=M,       ||W_0^(3)||op<=M,

all beta_E equal their genuine pruned trajectories simultaneously, and the
query time-Lipschitz constant is at most ML. Moving to a nearest grid point
therefore adds at most ML/n to its normalized norm. We have proved

    sup_{E: |E|<=epsilon n} sup_{0<=s<=S}
      ||P_E (W_0^(3))^T delta_E^(3)(s)||2/sqrt(n)
      <= 2B sqrt[ epsilon(1+log(e/epsilon))
                         + log(nN/alpha)/n ] + ML/n,

except on an event of probability at most alpha plus the probability that
one of the two full initial operator norms exceeds M.

For completeness M=10 gives an elementary exponentially small bound for the
latter event. A 1/4-net of the Euclidean unit sphere with at most 9^n points
can be constructed by a maximal separated set and volume comparison.
For any matrix its operator norm is at most twice the largest |u^T W v|
over pairs of net points: approximate maximizing unit vectors, and bound the
two approximation errors by one half of the operator norm.
For each deterministic pair, u^T W_0^(ell) v is N(0,1/n), so

    P(||W_0^(ell)||op>10)
      <= 2 exp[-(25/2-2 log 9)n].

A union bound over the two matrices completes the claimed high-probability
estimate.

For any fixed epsilon, choosing alpha=1/n (n>=2) makes the grid term tend to
zero. The limiting squared upper bound is at most a constant depending only
on S times epsilon log(e/epsilon), which then vanishes as epsilon decreases
to zero. Importantly, the estimate holds simultaneously for all deterministic
subsets, so E may subsequently be selected using the entire unpruned network.
There is no postselection independence assumption.

The same statement holds for each prescribed clipped comparison family:
replace delta_E^(2) by

    (I-P_E) phi'(z_E^(2))
      tau_R((W_E^(3))^T delta_E^(3)),

where tau_R is a fixed smooth coordinatewise clipping map with
|tau_R(v)|<=|v|. Leave the other displayed updates unchanged. Deleted
columns still do not enter the active flow. Every bound above uses only
||delta_E^(2)||2/sqrt(n)<=M3 aS, which clipping preserves. The
differentiated preactivation identities also remain unchanged, since they
use the current delta_E^(2), not its derivative. Thus B,L,M2,M3 and the
probability estimate are independent of R. This is uniformity of the
estimate for each prescribed R, not a claimed single finite-width event
simultaneous over an uncountable collection of clipping levels. For finite
R these are proof-comparator dynamics, not gradient flow of the pruned
prediction.

## What this lemma does not prove

The random vector delta_E^(3) belongs to the FULLY pruned network. A copied
top block driven by the unpruned bulk middle trajectory is close to the
actual top block, but its input can still depend on W_0^(3)P_E. Such a copy
cannot be substituted for delta_E^(3) in the conditional Gaussian argument.

To turn this lemma into a tail bound on the actual backward field one would
need an additional full-versus-pruned comparison controlling the bulk middle
feedback. No such comparison is proved here. This is a uniform Gaussian
sampling bound for an independent surrogate, not global stability of the
original dynamics.
