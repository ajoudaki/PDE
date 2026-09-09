# Source continuation after rejection of overall gain

2026-09-08. This is a separate theoretical route note for the revised near-identity target, not an extension of the gain theorem and not a proof of the new target. The accepted activation must be genuinely close to z in C1; a small offset is permitted. No gain is inserted into the nonlinear function or raw metric. No experiments were run.

## Exact covariance-weighted response estimate

Let xi be a finite centered Gaussian source vector with covariance Sigma, and let X be the vector of actual query inputs, so E[XX^T]=Sigma. Let d be a scalar response with the integrability needed for Gaussian integration by parts, and freeze all deterministic source coefficients. Write B=E[grad_xi d]. Then

    B Sigma=E[d xi^T],
    ||B X||_2^2=B Sigma B^T
       =||Proj_span{xi_j} d||_2^2≤||d||_2^2.

The identity holds for singular Sigma. Restrict to its support or use its fixed pseudoinverse to identify the Gaussian orthogonal projection; no continuity of a pseudoinverse is needed. Thus the complete response return, with all current and past named coefficients combined, is bounded in L2 directly by the physical backward field. Its individual unweighted coefficients need not be bounded. The learned rank integral is a separate explicit term.

This is a potentially useful replacement for a large coefficient box: it uses actual covariance and does not lose control merely because time features become nearly linearly dependent. It does not yet imply source tails or global continuation.

## Why marginal subGaussianity does not finish that argument

The covariance isometry from span{xi_j} to span{X_j} need not be bounded from Lp to Lp, p>2. This failure persists for individually smooth near-identity features.

Take G standard Gaussian, a smooth bump h supported on [-1,1] and equal to one on [-1/2,1/2], and h_m(x)=h(x−m). For fixed small epsilon, let

    X_1=G, X_2=G+epsilon h_m(G).

Both features have uniformly bounded subGaussian norms. Their generating functions are uniformly C1-close to the identity as epsilon tends to zero. But their linear span contains h_m(G), and

    ||h_m(G)||_p / ||h_m(G)||_2 -> infinity as m->infinity

for every p>2. Indeed the numerator is bounded below by the probability of [m−1/2,m+1/2] to the power 1/p, and the denominator above by the probability of [m−1,m+1] to the power 1/2. The logarithm of the ratio has leading term (1/4−1/(2p))m^2>0.

This is an obstruction to a generic span estimate, not a counterexample to the trained-network theorem. A successful use of covariance-weighted returns must exploit restrictions on the actual response-selected combinations, or a stronger property of the reachable feature span. It cannot deduce uniform subGaussianity of every normalized feature combination from marginal subGaussianity alone.

## A concrete route using the permitted offset

For a fixed nonzero small offset beta, the affine first-layer feature Gram is

    Q_aff,1=Gamma+beta^2 11^T.

It is uniformly positive definite for the admissible three-input class, including singular Gamma. Three distinct unit vectors are affinely independent: an affine line intersects a unit sphere in at most two points. More quantitatively, if a,b,c are the side lengths of their triangle, each is at least sqrt(2delta). Its circumradius is at most one because its affine plane intersects the unit sphere in a circle of radius at most one. Its area A therefore satisfies A=abc/(4R)≥delta^(3/2)/sqrt(2).

By the rank-one determinant expansion,

    det(Gamma+beta^2 11^T)
      =det(Gamma)+beta^2 1^T adj(Gamma)1
      =det(Gamma)+4beta^2 A^2
      ≥2beta^2 delta^3.

The identity for the adjugate term follows by expanding the squared exterior product (u_2−u_1) wedge (u_3−u_1). Since the trace is 3(1+beta^2), the product of the two largest eigenvalues is at most one quarter of its square. Consequently

    lambda_min(Q_aff,1)
       ≥8beta^2 delta^3/[9(1+beta^2)^2].

At each deeper affine initialized layer, Gaussian centering and addition of beta give Q_aff,l=Q_aff,l−1+beta^2 11^T. The same lower bound persists initially at every depth.

This suggests a distinct mechanism: first prove global physical training and an integrable residual/response budget for the unit-slope affine activation z+beta, and then perturb around that entire trained path by an independently small bounded nonlinear term. The comparator need not stay close to initialization. Its feature Gram positivity follows from affine geometry instead of large gain.

The decisive unresolved obligation is the global affine training and response budget in the original raw metric at general depth. Initial positive definiteness alone does not prove it. There is also a parameter-scope issue: for the strict one-parameter family z+theta(b+psi), the affine gap is of order theta^2 and the nonlinear coefficient of order theta, so independent perturbative smallness is not automatic. A family with a separately fixed small beta and a smaller nonlinear coefficient, or with different vanishing orders, needs to be within the user's accepted activation quantifiers before it can serve as the theorem's witness.

## Why the old arbitrary-control architecture should not be reused

A long-interval source lemma uniform over all bounded controls cannot hold merely from near-identity slopes and small nonlinear curvature. Already the scalar deep linear ascent equations

    w'=AC, A'=wC, C'=Aw

with positive initial w,A and C(0)=0 develop finite-time blowup. For example w(0)=A(0)=1 implies w=A, w^2−C^2=1, and C'=1+C^2, so C(t)=tan t. Thus uniformly bounded control c=1 is insufficient to prevent primal blowup even at exact identity activation.

This scalar example is a limitation of a proposed universal controlled lemma, not a counterexample to physical squared-loss training or the Gaussian three-sample theorem. Physical GF has the actual dissipation identity and raw length on [0,T] at most sqrt(T E(0)). A new global source proof must use that physical structure, a proved full affine fitting path, or another restrictive property of the actual residual controls. The former gain proof's short arbitrary-control interval does not supply this missing bridge.

Current status: the covariance-weighted return bound and the offset-induced affine Gram lower bound are exact. A fixed admissible near-identity nonlinear activation with the complete global theorem remains open in this route.
