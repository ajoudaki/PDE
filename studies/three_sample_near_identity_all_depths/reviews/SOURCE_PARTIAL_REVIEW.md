# Independent audit of the accepted near-identity partial results

2026-09-08. **Verdict: PASS for the initialization theorem and the conditional necessary fitting-scale theorem; the requested global near-identity theorem remains OPEN.** The source note correctly isolates a missing reached-field tail estimate and does not claim to close it. No gain result is used to satisfy the accepted target. No experiments were run.

The reviewed activation is exactly `(1-theta)z+theta atan(z)`, `0<theta<=1/2`. The raw metric, Gaussian initialization and original training algorithm are unchanged. The initialization theorem covers every admissible three-input Gram and every fixed finite depth. The fitting lower bound uses the admissible equilateral triple, hence applies to the uniform-data target for `0<delta<=1/2`. Its statement is conditional on reaching the specified loss, and its time bound additionally assumes a true strong raw gradient flow with the energy identity.

## Exact reviewed versions

| Artifact | SHA-256 |
|---|---|
| INITIALIZATION.md | `f53b4893ae4cacc2180ab1149c2c00a1b8f8b0b941d3319df5a3c0009f531163` |
| NECESSARY_FITTING_SCALE.md | `98705d5550bb977f26712e273b47592340ba2899cf952025889b386349af1fbd` |
| SOURCE_ROUTE.md | `06f5cbe85d86587efaf1e8636e4da40d8f4497b95ab1dc5200f4f8766e36431e` |

The complete contents of the two theorem notes were read and their calculations independently checked. The source route's projection, counterexample and offset statements were also rechecked. These hashes distinguish the final spectral-monotonicity proof from the earlier temporary initialization draft with an unnecessary exponential loss. The fitting-scale audit was subsequently updated from hash `30633b10fa528424deef6b49378d155a9968f8ab5da475c38975cd3ba102bfc7` to the displayed version to check its added fixed-radius first-exit argument; the earlier bounds are unchanged and remain valid.

## Initialization theorem

All displayed constants and quantifiers check.

The lower variance estimate uses two valid Jensen steps: first in the integral representation of atan(z)/z, then under the probability measure with density G^2 against standard Gaussian measure. The latter measure has mean of G^2 equal to three. They give

    q_new >= q/(1+theta*q)^2.

Since q<=1 and theta<=1/2, reciprocal increments are at most `(5/2)theta`. The upper variance estimate uses

    1−atan(z)/z >= z^2/[3(1+z^2)],
    1−(1−theta*h)^2 >= theta*h,
    E[G^4/(1+G^2)] = E[1/(1+G^2)] >= 1/2.

It gives `q_new<=q−theta*q^2/6`, and reciprocal increments at least `theta/6`. Positivity of every finite-depth variance is retained. Thus

    [1+(5/2)theta*k]^−1 <= q_k <= [1+theta*k/6]^−1

holds with the stated indexing, including k=0.

The normalized spectral argument is exact. The transformed Gaussian covariance is a nonnegative Hermite-weighted sum of entrywise powers of the correlation matrix. Oddness excludes the constant coefficient, and the remaining normalized weights sum to one. The Hermite identity is justified internally by the Gaussian generating function; L2 approximation passes products and yields matrix-norm convergence of the resulting series in dimension three. Singular Gaussian pairs do not obstruct this argument.

If R is a correlation matrix and `S=R^(circ(m−1))`, then S is positive semidefinite with diagonal one, also for m=1 using the all-ones convention. Tensor Gram representations prove positive semidefiniteness of entrywise products. Hence

    (R−lambda_min(R)I) circ S >= 0,
    (lambda_max(R)I−R) circ S >= 0,

which implies that every `R^(circ m)` has its spectrum inside the previous extremal interval. Convex averaging proves that the normalized minimum eigenvalue cannot decrease and the normalized maximum cannot increase. This is a statement about spectral extrema, not a Loewner comparison of successive correlation matrices. The note makes that distinction correctly.

The initial strictly positive floor is supplied separately by the cubic feature component. The dual tensors have unit norm, annihilate the other two input tensors, and pair with their own input by at least `delta(2−delta)`. Summing the resulting squared Cauchy–Schwarz estimates yields `Gamma^(circ3)>=delta^2(2−delta)^2 I/3` even for singular Gamma.

For the cubic arctangent coefficient, two Gaussian integrations by parts give

    b_3(sigma)=−(2sigma^3/sqrt(6))
                 E[G^2/(1+sigma^2 G^2)^2].

At sigma>=1, the stated change of variable and the interval |x|<=1 give the lower square bound `eta0=1/(108*pi*e)` exactly. Only sigma=1 is used for the first-layer Gram. The independent Gaussian covariance recursion and the Hermite covariance identity therefore give `Q_1>=eta0*theta^2*delta^2 I/3`. Normalized spectral monotonicity propagates this floor without loss; multiplication by the proved lower bound for q_L proves

    Q_L >= eta0*theta^2*delta^2 /
                 {3[1+(5/2)theta*L]} I.

The claim that the smallest initial eigenvalue has order L^−1 for fixed positive theta and delta follows by combining this lower bound with `lambda_min(Q_L)<=q_L` and the upper variance estimate. It is correctly an initialized-network statement.

The nonaffinity bounds also check. Three Gaussian integrations by parts and Bessel's inequality give

    6 V(q) <= E|[phi_theta(sqrt(q)G)]'''|^2
           <=4theta^2 q^3,

because the absolute third derivative of atan is at most two. The affine residual equals V(q) by oddness and Gaussian linear regression. Weighted Jensen gives `E[G^2/(1+qG^2)^2]>=(1+3q)^−2`, so the cubic component proves

    theta^2 q^3/384 <= V(q) <= (2/3)theta^2 q^3,
    0<q<=1.

Thus the initialization-only absolute gap has order ell^−3 with depth for fixed theta. This genuinely excludes a positive absolute gap uniform over all depths for this exact activation. It does not exclude a time-uniform gap at each fixed depth.

## Necessary fitting scale

The equilateral example is within the stated geometry exactly when `delta<=1/2`, with dimension at least two. Its zero input sum is preserved by the first linear projection for every trained first-layer state. For `a=1−theta`, summing the activation identities gives

    S_1=theta*T_1,
    S_l=a A_l S_(l−1)+theta*T_l,
    ||T_l||_2<=3*pi/2.

Induction proves equation (1) of the note without an assumption about the trained field distribution. At loss at most 3/8, Cauchy–Schwarz forces `sum_i f_i>=3/2`. The readout identity and the sum-field bound then force equation (2), with constant exactly `1/(pi*theta)`.

At joint raw distance R from the canonical initialization, `||C||<=R` and `||A_j||op<=2+R`; the initialized operator bound was verified in the earlier common-action audit from the Gaussian norm theorem and passage on a dense generated span. The physical field normalization is unchanged here. Bounding the geometric sum by `L(2+R)^(L−1)` gives the explicit inequality in (3). In deriving its last line one uses `R(2+R)^(L−1)<=(2+R)^L`, so the displayed lower bound is valid, although deliberately conservative.

For the sharper constant, the relevant variables are the readout norm c and the L−1 middle-block Hilbert–Schmidt displacements d_j. The first-block displacement is included in R but need not occur in the upper bound. Their squared sum is at most R^2. The unique term of degree L in the product estimate is bounded by

    c product_j d_j <= (R^2/L)^(L/2).

Its coefficient a^(L−1) is at most one. All other finitely many terms have degree at most L−1 with coefficients bounded solely in terms of fixed L. This justifies the remainder `C_L(1+R)^(L−1)` uniformly as theta decreases. Along a subsequence where `theta^(1/L)R` is bounded, multiplication by theta makes that remainder vanish. Equation (2) therefore implies

    liminf_(theta->0) theta^(1/L) R
        >=sqrt(L)*pi^(−1/L).

The unbounded-subsequence case is automatic. No assumption that successful states exist for every theta is used beyond the conditional family to which the implication is applied.

If a true strong raw GF reaches that loss at time T, its initial loss is 3/2 and its energy identity gives `R^2<=(3/2)T`. The explicit time bound and the asymptotic result

    liminf_(theta->0) theta^(2/L) T
        >=(2L/3)*pi^(−2/L)

follow. For L=2 this is indeed `4/(3*pi)`. These are necessary bounds, not matching upper bounds or a proof of global fitting. They do rule out a theta-independent exponential fitting rate with a theta-independent finite prefactor on this admissible family. They leave theta-dependent rates and a theorem selecting one fixed positive theta possible.

The subsequently added fixed-radius first-exit argument also passes, and strengthens the time exponent when L>2. Set `B_L=(3^L−1)/2` and suppose `theta<1/(pi*B_L)`. A successful state's radius must exceed one, since otherwise the left side of (2) is at most B_L. Strong continuity therefore supplies a first t_1<=T with radius one. At that state `||C||<=1`, all adjacent norms are at most three, and the exact sum-feature bound yields

    sum_i f_i(t_1) <=(3*pi*theta/2) B_L.

The exact squared-loss difference, including its negative quadratic term, is

    E(0)−E(t_1)=sum_i f_i(t_1)−(1/2)sum_i f_i(t_1)^2
               <=(3*pi*theta/2) B_L.

The true energy identity makes this difference nonnegative. Cauchy–Schwarz on the raw path to t_1 gives `1<=t_1[E(0)−E(t_1)]`. Combining the two inequalities proves precisely

    T>=4/[3*pi*(3^L−1)*theta].

The strict condition on theta holds eventually in every theta-to-zero family at fixed L. Thus `liminf theta*T` is at least the displayed positive constant, and for L>2, `theta^(2/L)*T` tends to positive infinity along every successful family. This supersedes the earlier exponent 2/L for the strongest necessary time-order conclusion at L>2; it does not invalidate the earlier distance estimate or time inequality. At L=2 the earlier constant `4/(3*pi)` is stronger. The first-exit proof uses no trained Gaussian law, sample-exchange symmetry, uniqueness, or assumption of a global solution beyond the conditional strong flow through its successful time.

## Source route and remaining gap

The exact covariance-weighted response identity is valid under its stated Gaussian integration-by-parts hypotheses. With `Sigma=E[XX^T]` and `B=E grad_xi d`, Gaussian integration by parts gives `B Sigma=E[d xi^T]`. The full return BX has squared L2 norm equal to the squared norm of the projection of d onto the linear Gaussian source span, hence at most `||d||_2^2`. Restricting to the support of Sigma handles singularity. No covariance inverse is differentiated, and every current named return remains in B.

This does not yield the required tails. The smooth-bump example correctly shows that individually subGaussian, uniformly C1-near-identity features can span normalized combinations with arbitrarily large Lp/L2 ratios. The Gaussian probability bounds stated in the note give logarithmic growth with positive leading coefficient `(1/4−1/(2p))m^2` for p>2. It is a counterexample only to the proposed generic span estimate, not to the reachable-network theorem.

The scalar arbitrary-control example is also exact: `w=A=sec s`, `C=tan s` solves `w'=AC`, `A'=wC`, `C'=Aw` from `(1,1,0)` and blows up at s=pi/2. Its role is explicitly limited to disproving a long-horizon unrestricted bounded-control premise; it is not a counterexample to squared-loss GF or to the Gaussian three-sample model.

The optional offset Gram bound was checked as a separate geometric observation. Three distinct unit vectors are affinely independent, their triangle has circumradius at most one, and the determinant expansion gives the stated `8 beta^2 delta^3/[9(1+beta^2)^2]` lower bound. The note correctly leaves both a full affine-trajectory bridge and the admissibility of independently tunable offset/nonlinearity scales unresolved.

The actual source bottleneck remains: obtain a cap-independent tail estimate for reached incoming fields, or a replacement stability modulus strong enough for uniqueness and the full population/finite-width bridge, while retaining actual physical residual feedback and all same-matrix returns. The new initialization theorem supplies no trained Gaussian-law assumption or trained Gram barrier. The necessary fitting scale explains why an initialization-neighborhood proof cannot be uniform as theta tends to zero. Neither result establishes global existence, global fitting, cap removal, or the requested global observation theorem. Those claims remain open in the accepted near-identity scope.
