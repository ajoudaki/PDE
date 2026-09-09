# Audit and Gaussian deleted-query reductions

## Independent audit of TOP_COUPLED_LOCALIZATION.md

PASS. The following were checked directly: identities (2)--(6), the excess-truncation chain rule q eta_R'=(R/|q|)1_{|q|>R}q', every constant K,F,H,J in (8), the history bound a^3 s^3/2, projection estimate (10), active-top variation (11a), and the conditional Gaussian variance in (12). The claims and their limitations are correct. In particular, copied-top stability does not imply independence from the deleted columns because the supplied actual bulk trajectory depends on them. A postselected set creates a further selection issue.

## 1. Gaussian integration by parts reduces tails to two bulk responses

At finite width, fix a deterministic column i and a finite feature time. Let g= sqrt(n) W0[:,i] be the standard Gaussian deleted column and let xi denote all other independent initial variables. In the top-only deleted-query construction put

    u(g,xi)=bar d(g,xi)/sqrt(n),     Y=g dot u.

The readout equation gives ||u||Euclidean<=aS deterministically, independently of the initial operator norm. Suppose the finite-dimensional function is differentiable and the expectations below justify Gaussian integration by parts (otherwise retain the corresponding cutoff/boundary terms). Let J_i be the Jacobian of bar d with respect to the raw deleted column W0[:,i]. Then

    D_g u = J_i/n,
    div_g u = Tr(J_i)/n,
    grad_g Y = u + J_i^T g/n,
    E_g[Y | xi] = E_g[Tr(J_i)/n | xi].                 (1)

These Jacobians differentiate the actual bulk path supplied to the copied top. Setting its derivative to zero is invalid.

A useful moment inequality needs no external concentration theorem. For independent standard Gaussians g,g', rotate from g to g' through g_theta=g cos(theta)+g' sin(theta). Its velocity is an independent standard Gaussian at each theta. The fundamental theorem of calculus, Minkowski, and conditional Gaussian moments give, for p>=2,

    ||Y-E_g Y||_p <= (pi/2)||N(0,1)||_p ||grad_g Y||_p
                  <= C sqrt(p) ||grad_g Y||_p.          (2)

The norms include xi; Jensen handles the conditional centering. Hence sufficient uniform bounds are

    || E_g[Tr(J_i)/n | xi] ||_p <= A p log(e+p),
    ||J_i^T g/n||_p <= A sqrt(p) log(e+p).              (3)

Together with ||u||<=aS, (1)--(3) give ||Y||_p<=C p log(e+p). Markov's inequality with p proportional to R/log R gives an L2 tail envelope

    ||Y 1_{|Y|>R}||_2 <= C exp[-c R/log(e+R)].           (4)

The single-column error in TOP_COUPLED_LOCALIZATION.md then transfers this to q_i. On a bounded initial-operator event that error is bounded. To apply (1)--(3), however, one must work under the full Gaussian law or explicitly account for event-boundary terms. The error can instead be handled in moments: its constant is at most quadratic in ||W0||op, whose Gaussian matrix moments give an O(p) contribution to the pth root moment, compatible with (4).

For population cutoff removal the constants in (3) must be uniform over neuron i, width, time in the interval, and the entire clipped comparator family. Bounds for one fixed time/discretization/cutoff do not suffice. Equation (11a) shows that J_i is a bounded Volterra response to derivatives of the actual bulk middle path. Thus (3) is a precise weaker target than bounding its entire operator norm; integration by parts does not itself prove it.

## 2. Full-pruning stability may lose two logarithms

Suppose a full-pruning construction has already established, simultaneously for all fixed-time middle subsets E of mass p, an independent-query estimate

    ||P_E W0* d^E||_2 <= C sqrt[p log(e/p)].             (5)

A uniform version of (5) also covers trajectory-selected E; separate conditional estimates without a simultaneous event do not.

Let Delta(p) bound the actual/pruned bulk-input discrepancy supplied to the two top blocks, uniformly over E and time. The exact top comparison then gives

    ||P_E q||_2
      <= C sqrt[p log(e/p)] + C sqrt(p) + C Delta(p).   (6)

The finite-horizon top comparison uses the bulk input discrepancy in sup L2 or in the corresponding instantaneous-plus-integrated norm. The term C sqrt(p) includes deletion of the actual rare columns and learned-history error.

It is sufficient for the Osgood route that

    Delta(p) <= C sqrt(p) log(e/p) log log(e^e/p).       (7)

Indeed take E={|q|>R}, p=P(E), and L=log(e/p). For small p, (6)--(7) imply

    R sqrt(p) <= ||P_E q||_2 <= C sqrt(p) L log(e+L).

When p>0 this forces L>=c R/log(e+R). The function exp(-L/2)L log(e+L) is decreasing for sufficiently large L, so substituting this lower bound in (6) yields

    ||q 1_{|q|>R}||_2 <= C exp[-c' R/log(e+R)].

For large R, small p follows already from the uniform second moment. Thus (7) suffices for the endpoint Osgood criterion. This is a conditional reduction, not an established full/pruned coupling estimate.

## 3. Bounded mutual information is insufficient

Let Q be the product of a standard n-dimensional Gaussian g and a uniform random sign vector sigma. Write u=B sigma/sqrt(n), so ||u||=B and each coordinate is bounded by B/sqrt(n). Under Q, Y=g dot u is N(0,B^2).

Define a different joint law P with the same Gaussian marginal for g: with probability 1-1/n, use an independent uniform sigma; with probability 1/n, set sigma=sign(g). The marginal of sigma remains uniform. Conditional on the adaptive branch,

    Y=(B/sqrt(n)) sum_j |g_j|,

which is of order B sqrt(n) with probability tending to one. Therefore its L2 tail does not vanish uniformly in n.

Nevertheless D(P||Q)<=log 2. Indeed the fully adaptive joint law has density 2^n 1_{sigma=sign(g)} relative to Q, hence divergence n log 2; convexity of relative entropy for the mixture gives (1/n)n log 2. Thus constant mutual information, the correct Gaussian marginal, and a uniformly bounded adaptive query do not even imply uniform integrability. This example is not a network trajectory.

A stronger information premise would work. Let L=dP/dQ. A uniform Renyi moment E_Q L^(1+epsilon)<infinity gives Gaussian query tails by Holder. A weaker sufficient assumption is

    P(log L>t) <= A exp[-c sqrt(t)/log(e+t)].

Indeed, for any event A_R={|Y|>R},

    P(A_R) <= exp(t) Q(A_R) + P(log L>t).

Choose t proportional to R^2 below the Gaussian-tail exponent. This yields an exp[-c R/log R] tail and hence the Osgood criterion. No such likelihood-ratio control has been obtained for the actual bulk transcript. Conditional on all other initial randomness, a nonconstant deterministic continuous query can even create a singular joint law; that obstacle must be addressed before using entropy identities.

## Scope

The top-localization proof passes. Neither integration by parts nor a bounded-entropy statement closes the missing bulk dependence. The three concrete sufficient targets are (3), the logarithmically weakened full-pruning bound (7), or the stated likelihood-ratio tail. Each must be proved uniformly over the actual comparator family before implying continuation.

