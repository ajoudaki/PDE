# Endpoint regularity and a weaker cutoff-removal criterion

Status: the endpoint regularity and Osgood comparison statements below are proved reductions. They do not prove local existence from every reached endpoint of the canonical Gaussian flow. No computation was used.

## 1. A finite endpoint is a regular point of the existing path

Let an uncut solution exist on [0,S*), with S* finite, canonical zero readout, and the bounds in LOCAL_ACTION_SPACE_AND_FLOW.md. Write a=pi/2, D_l=phi'(Z_l), and q=(W3)*[W4 D3]. All assertions are on the common population spaces.

There are strong endpoint limits of X1 in L2, each trained matrix increment Wl-Wl_0 in Hilbert--Schmidt norm, and W4 in L-infinity. Each rank-one matrix velocity has HS norm equal to the product of its L2 factors and obeys the same finite-horizon bound as its operator norm. The first coordinate has bounded L2 velocity. Finally,

    ||W4(t)-W4(s)||infinity <= a|t-s|.

At the limiting state all forward fields, backward fields, and the uncut four-block velocity converge in their L2/HS spaces. The nontrivial continuity step is

    ||(D2(s)-D2*) q*||2 -> 0.

Uniformly bounded gates converging in probability multiply a fixed L2 variable continuously in L2: restrict q* to |q*|<=R, pass to the limit, and then remove R. This is continuity, not a Lipschitz estimate. Thus the existing solution extends C1 to the closed interval and satisfies the ODE also at its endpoint.

There is also a derivative limit for q. Set

    B = E1[(H1)^2] I + W2 M_(D1^2) (W2)*,
    m2 = E2[(H2)^2],     delta3 = W4 D3.

The exact equations give

    Z2' = B D2 q,
    Z3' = m2 delta3 + W3 D2 B D2 q,

hence

    q' = b + L q,
    b = H2 ||delta3||2^2
        + (W3)*[H3 D3 + W4 phi''(Z3) m2 delta3],
    L = (W3)* M_(W4 phi''(Z3)) W3 D2 B D2.

The operator L is uniformly bounded on a finite horizon. Its bounded multiplication coefficients converge strongly on L2, and matrix actions converge in operator norm. Thus b(s)->b* and L(s)q(s)->L*q* in L2. The field q is C1 up to S*.

This regularity concerns an existing path; it supplies no solution on a right neighborhood of the endpoint.

## 2. An Osgood criterion weaker than exponential tails

The fixed-cutoff amplification exp(C R S) is not intrinsic to all cutoff arguments. Optimizing the cutoff at the current error gives a weaker sufficient criterion.

For a collection of reference states/paths with common primal and readout bounds, suppose uniformly that

    ||q 1_{|q|>R}||2 <= G(R),      R>=1,

where G is nonincreasing and tends to zero. Define

    rho(u) = C u + C inf_{R>=1} [R u + G(R)].

The constant uses only the common primal and readout bounds. The infimum of these affine functions is nondecreasing and concave; rho is continuous on (0,infinity) and tends to zero at zero. Assume

    integral_(0+) du/rho(u) = infinity.                 (O)

For uncut states A and B, with B in the reference collection,

    ||V(A)-V(B)|| <= rho(d(A,B)).

Indeed,

    delta2(A)-delta2(B)
      = D2(A)[q(A)-q(B)] + [D2(A)-D2(B)]q(B).

The first term is at most C d using the top readout bound. Splitting the second term on |q(B)|<=R gives C R d + C G(R). The other blocks use the usual rank-one and forward/reverse bounds. Infimize over R.

For clipped flows at levels K,L, both in the reference collection,

    ||V_K(A)-V_L(B)||
      <= rho(d(A,B)) + C[G(K)+G(L)],

because each clipped-to-uncut velocity error at a fixed state is bounded by its tail. Thus their path distance satisfies

    e(t) <= e(0) + C t[G(K)+G(L)] + integral_0^t rho(e(s)) ds.

On a fixed horizon replace the first two terms by epsilon. Let

    y(t)=epsilon+integral_0^t rho(e(s)) ds.

Then e<=y and y'<=rho(y), giving

    integral_epsilon^{y(t)} du/rho(u) <= t.

As epsilon tends to zero, (O) forces the uniform error to zero on every fixed finite horizon. This proves Cauchy convergence. It also proves uniqueness against an uncut reference solution with the stated envelope.

In particular, if all clipped flows started from an endpoint admit one common envelope satisfying (O) on a right neighborhood, they converge there. The limit solves the uncut equation because, with theta_K in the reference position,

    ||V_infinity(theta)-V_K(theta_K)||
      <= rho(d(theta,theta_K)) + C G(K) -> 0.

Comparison with theta_K gives uniqueness against any bounded-primal competing uncut solution. No tail assumption on that competing solution is needed. This is a complete restart theorem under the explicit uniform-comparator premise.

For example,

    G(R) <= A exp[-c R/log(e+R)]

suffices. Choosing R proportional to log(1/u) log log(1/u) gives, for small u,

    rho(u) <= C u log(1/u) log log(1/u),

whose reciprocal integral diverges by two logarithmic substitutions. Nevertheless exp(C R h)G(R) need not tend to zero for any fixed h>0. More generally, G(R)<=A exp[-c R/(log(e+R))^beta] suffices for 0<=beta<=1.

## 3. Smooth endpoint convergence does not imply that criterion

The following is a scope check, not a canonical-network trajectory or a counterexample to the target.

Take disjoint events E_k of probabilities 2^(-4k). Put

    e_k = 1_(E_k)/sqrt(P(E_k)),
    q* = sum_(k>=1) 2^(-k) e_k
       = sum_(k>=1) 2^k 1_(E_k).

Then q* is in L2 and its L2 tail is comparable to 1/R for R>=2. Let t_k=1-1/k. Use a fixed smooth switch, flat at both ends, to turn coefficient 2^(-k) from zero to its full value on [t_k,t_(k+1)]. Define q(t) by summing these switched coefficients times e_k, and set q(1)=q*.

At every t<1, only finitely many coordinates occur: q(t) is bounded and has a Gaussian exponential moment for some finite constant. On the kth switching interval its mth derivative has L2 norm at most

    C_m 2^(-k)[k(k+1)]^m -> 0.

Therefore q is C-infinity up to time one, with every positive-order endpoint derivative zero. Yet its endpoint tail is only comparable to 1/R. The optimized modulus for that tail is comparable to sqrt(u), and its reciprocal is integrable at zero.

Even q=A*v with A bounded and v pointwise bounded does not exclude the example. On another probability space take orthonormal Rademacher functions r_k, define the partial isometry A*r_k=e_k, and put

    v(t)=sum 2^(-k)c_k(t) r_k,

with the same switches. Then ||A||op<=1, ||v(t)||infinity<=1, v is C-infinity in L-infinity, and A*v(t)=q(t). This retains only the bounded operator/top-field structure; it does not retain Gaussian initialization or coupled network feedback.

## Exact research consequence

Every finite maximal endpoint of the existing canonical solution has a state and velocity limit in the specified spaces; q additionally has a derivative limit. Those facts do not alone provide local existence or uniqueness past it. The Osgood lemma supplies a weaker sufficient restart mechanism than Gaussian or exponential-tail cutoff removal. What remains unproved is a canonical-network estimate on the clipped continuation family from a reached endpoint that implies (O), or a different network-specific existence mechanism. The smooth example rules out deriving that estimate from temporal L2 regularity alone, and says nothing against the canonical flow.

