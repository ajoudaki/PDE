# A coefficientwise local response estimate for the arctan L=3 model

This is a research lemma for the parent agent, not a claim that global-in-time closure has been proved. It assumes the exact fixed-program Gaussian response representation, whose proof must separately be supplied (Gaussian conditioning plus integration by parts). It does not assume invertible source covariance matrices: all derivatives below are derivatives of explicitly given scalar functions in formal source coordinates, evaluated at the possibly singular Gaussian source law. All deterministic coefficients are held fixed during these derivatives.

Use g=phi composed with F^{-1}, so |g'|<=1. Write p1=(W2)*delta2 and p2=(W3)*delta3. Only in this technical lemma use Q=p2 and scalar Gaussian sources G1,G2,S2,S3 for the Gaussian parts of p1,p2,z2,z3 respectively. The scalar recursion at Euler mesh h is

    H1_k = g(X1_0 - 2h sum_{r<k} r_r p1_r),
    p1_k = G1_k + sum_{s<=k} D2_ks H1_s,
    Z2_k = S2_k + sum_{s<k} C2_ks delta2_s,
    H2_k = phi(Z2_k),
    Q_k = G2_k + sum_{s<=k} D3_ks H2_s,
    Z3_k = S3_k + sum_{s<k} C3_ks delta3_s,
    W4_k = -2h sum_{r<k} r_r phi(Z3_r),
    delta3_k = W4_k phi'(Z3_k),
    delta2_k = phi'(Z2_k) tau_R(Q_k).

The response coefficients are

    A2_ks = E[partial H1_k / partial G1_s],
    B2_ks = E[partial delta2_k / partial S2_s],
    A3_ks = E[partial H2_k / partial G2_s],
    B3_ks = E[partial delta3_k / partial S3_s].

Here C2=A2 minus the learned forward coefficient 2h r_s E[H1_s H1_k]; C3 has the analogous H2 contraction. D2=B2 minus the learned backward coefficient 2h r_s E[delta2_s delta2_k], with no learned term at s=k; D3 is analogous with delta3. The strict causality A2_ks=A3_ks=0 for s>=k is essential.

Let b bound |phi|, |phi'|, |phi''|. On a sufficiently small deterministic interval T, the elementary output recursion supplies |r_k|<=2 and |W4_k|<=cT uniformly in cutoff and mesh: |r_k|<=1+b||W4_k||infty and ||W4_{k+1}||infty<=||W4_k||infty+2hb(1+b||W4_k||infty), followed by a geometric sum. Denote by K the largest subGaussian norm of Q_k; B2,B3 below denote the largest row sums of the expectations of absolute derivatives, not merely absolute expectations. Then

    Q2 := max_k sum_s |D2_ks| <= B2 + c T K^2,
    Q3 := max_k sum_s |D3_ks| <= B3 + c T^3.

All constants c below depend only on the activation bounds and the residual bound.

## 1. Every C2 coefficient has an individual factor h

Set v_{k,s}=|partial H1_k/partial G1_s|. Because the transformed first-layer update is linear in p1,

    v_{k,s} <= c h [1_{s<k} + sum_{r<k} sum_{u<=r} |D2_ru| v_{u,s}].

If V_{r,s}=max_{u<=r}v_{u,s}, the inner sum is bounded by Q2 V_{r,s}. Discrete Gronwall gives the pointwise, deterministic estimate

    v_{k,s} <= c h exp(c T Q2).

Consequently |C2_ks|<=h L2, where L2=c(1+exp(cTQ2)). There is no random unbounded p1 factor in this argument; this is where using F(z1) matters.

## 2. Every C3 coefficient has an individual factor h

Fix source G2_s and put v_k=|partial Z2_k/partial G2_s|. Differentiation of delta2=phi'(Z2)tau_R(Q), using |tau_R(Q)|<=|Q| and |tau_R'|<=1, gives

    v_k <= h L2 + c h L2 sum_{r<k} (|Q_r| v_r + sum_{u<=r}|D3_ru|v_u).

Thus

    max_{u<=k}v_u <= h L2 exp(c L2 h sum_{r<k}(|Q_r|+Q3)).

For arbitrarily dependent Q_r with subGaussian norm at most K, convexity/Jensen over time gives

    E exp(a h sum_{r<k}|Q_r|) <= max_r E exp(a T |Q_r|)
                                           <= 2 exp(c a^2 T^2 K^2).

Therefore

    |A3_ks| <= c h L2 exp(c L2 T Q3 + c L2^2 T^2 K^2),
    |C3_ks| <= h L3,
    L3 := c + c L2 exp(c L2 T Q3 + c L2^2 T^2 K^2).

This estimate includes every previous source s; no aggregate path count removes the time factor.

## 3. Top backward response is bounded deterministically

Let J_k=sum_{s<=k}|partial Z3_k/partial S3_s| and S_k=sum_{s<=k}|partial delta3_k/partial S3_s|. Then

    J_k <= 1 + h L3 sum_{r<k}S_r,
    sum_s |partial W4_k/partial S3_s| <= c h sum_{r<k}J_r,
    S_k <= c h sum_{r<k}J_r + c T J_k.

Thus J_k<=exp(c L3 T^2) and

    B3 <= c T exp(c L3 T^2).

These are pointwise derivative bounds. Correlations or singularities among S3 source Gaussians do not enter.

## 4. Middle backward response and Q tails

Let J_k=sum_{s<=k}|partial Z2_k/partial S2_s|, and S_k=sum_{s<=k}|partial delta2_k/partial S2_s|. Then

    J_k <= 1+h L2 sum_{r<k}S_r,
    S_k <= c |Q_k|J_k+c Q3 max_{u<=k}J_u.

Therefore max J_k <= exp(c L2 h sum_{r<k}(|Q_r|+Q3)). Cauchy-Schwarz, followed by the same Jensen exponential bound, gives

    B2 <= c(K+Q3) exp(c L2 T Q3+c L2^2 T^2 K^2).

Finally Q_k=G2_k+sum_s D3_ks H2_s. The Gaussian variance is E[delta3_k^2]<=cT^2, while the response is pointwise bounded by bQ3. Thus

    K <= c(T+Q3).

## 5. Uniform local bootstrap

These estimates close sequentially in program time, rather than by assuming the desired bounds. At step k, A2_k only uses B2 rows of steps r<k. A3_k only uses delta2 at r<k and D3 rows r<k. Hence B3_k is bounded first using earlier rows; then Q_k obtains its Gaussian-plus-bounded tail estimate; then B2_k is bounded.

Choose constants in the triangular order B3_*=large universal constant, K_*=2c(1+B3_*), B2_*=2c(K_*+B3_*). Choose T0>0 so small that assuming B2<=B2_*T, B3<=B3_*T, K<=K_*T makes every exponential above at most 2 (and L2,L3 bounded by fixed constants), with strict margins in the three output inequalities. Induction over k proves these bounds for all kh<=T0, uniformly in h and R. At k=0 all backward sources and responses vanish. This supplies a uniform subGaussian bound for Q in the cutoff population Euler systems; passage h->0 gives the same bound for cutoff population flows.

## 6. Cutoff removal uses only reference tails

For an uncut state and a cutoff reference state, write their Q fields as Q and Q_R and their second preactivations as Z and Z_R. Exactly,

    phi'(Z)Q-phi'(Z_R)tau_R(Q_R)
      = phi'(Z)(Q-Q_R)
        +[phi'(Z)-phi'(Z_R)]tau_R(Q_R)
        +phi'(Z)[Q_R-tau_R(Q_R)].

The first term is Lipschitz in the state distance because Q=(W3)*delta3 and W4 is bounded. The second is at most c(R+1)||Z-Z_R||2. The third is a tail of the cutoff reference alone. Together with the other update estimates,

    e(t) <= C integral_0^t (1+R)e(s)ds
             + C integral_0^t ||Q_R-tau_R(Q_R)||2 ds.

The uniform subGaussian estimate makes the tail <=C exp(-cR^2), and therefore e(t)<=C exp(C(1+R)T-cR^2)->0. This compares the actual finite uncut flow to the cutoff reference after passing width to infinity, makes cutoff population flows Cauchy, and proves uniqueness of any bounded-L2 uncut population solution on [0,T0]. For comparing two cutoff levels R'<R use the smaller cutoff as reference and the 1-Lipschitz property of the larger cutoff, with the same reference-tail estimate.

The remaining global issue is genuine: the above bounds contain nested exponentials in K,B2,B3 and do not by themselves prevent these response quantities from blowing up at a finite larger time. The global L2 energy bounds prevent state norm blowup but do not presently control these response masses. A fresh-slab continuation needs a new estimate on old-source response transport; no such estimate is established here.
