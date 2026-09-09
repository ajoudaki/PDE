# Independent depth-uniformity obstruction audit

I read the activation-class manuscript's model, geometry/regression estimates, response construction and motion argument, and the odd-gain all-depth proof, SOURCE_RESPONSE.md and INITIAL_MOTION.md directly. I did not infer validity from any earlier review. The findings below isolate the new uniformity issue; they do not purport to reproduce the entire foundational finite-Gaussian-program theorem.

## Finding

I found no counterexample to one finite gain/amplitude pair working at every separately fixed finite hidden depth. A bounded localized perturbation destroys a depth-uniform positive nonaffinity coefficient for the proposed large-gain initialization, but its initialized regression gap decreases only geometrically at a controlled rate. The gain-driven motion decreases faster. Confusing these two quantifiers would produce a false obstruction.

The stronger source mechanism in the odd-gain proof applies to the present normalized activation after an explicit bounded-remainder check; oddness and a positive perturbation derivative are unnecessary for that mechanism. The initial-motion induction also only requires positive first derivative, nonconstant first derivative, and positive forward Grams. These hold for the present class.

## Uniform initialized Gram, with all quantifiers visible

Fix a>=4 and 0<e<=1. For raw initialized preactivation standard deviations sigma_l, sigma_1=1 and

    sigma_(l+1) >= (a-e) sigma_l >= (a/2) sigma_l,
    sigma_(l+1) <= a sigma_l+2a.

The first inequality follows from the independent-copy variance identity and phi'>=a-e; it applies to the variance of phi(sigma_l G), and its second moment is larger still. Consequently

    (a/2)^(l-1) <= sigma_l <= 4 a^(l-1).

Normalize only features, leaving raw parameters and the readout unchanged:

    K_l=a^(l-1), Z_l=z_l/K_l, X_l=h_l/a^l,
    chi_l(z)=z+K_l^(-1)[1+(e/a)psi(K_l z)].

Let Q_l be the normalized initialized feature Gram, Q_0=Gamma. Gaussian regression, including singular covariance matrices, gives linear coefficient

    beta_l=1+(e/a) E psi'(sigma_l G).

Integration by parts and boundedness of psi yield

    |E psi'(sigma G)|=|E[G psi(sigma G)]|/sigma <=1/sigma.

Set d_l=a^(-1)(2/a)^(l-1). Then beta_l>=1-d_l. At l=1 the constant regression coefficient is also at least 1-d_1; hence

    Q_1 >= (1-d_1)^2 (Gamma+11^T),
    Q_l >= (1-d_l)^2 Q_(l-1), l>=2.

Because sum_(l>=1)d_l=1/(a-2)<=1/2 and product(1-d_l)>=1-sum d_l,

    Q_L >= (1/4)(Gamma+11^T) >= (delta^2/16) I_3

for every finite L, with the same lambda=delta^2/16. The final inequality is the manuscript's proved augmented three-input Gram lemma, which includes singular input Grams and one-sided pairwise separation. This argument avoids the invalid fixed lower slope product (1-e/a)^(2L).

## Regression margin and its exact stability estimate

For any normalized bounded nonconstant C2 psi, choose a finite r with

    J=inf_(alpha,beta) integral_-r^r [psi(x)-alpha-beta x]^2 dx>0,
    c=exp(-r^2/2) J/sqrt(2 pi)>0.

Boundedness and nonconstancy guarantee such an r. Density restriction gives R_psi(sigma G)>=c/sigma for sigma>=1. Thus at any initialization with depth L,

    min_(l<=L) R_psi(z_i^l(0)) >= eta_L=c/(4 a^(L-1)).

A useful improvement on the manuscript's stability lemma is valid for arbitrary 1-Lipschitz psi:

    |sqrt(R_psi(X))-sqrt(R_psi(Y))| <=2 ||X-Y||_2.

Indeed the optimal slope has absolute value at most one by the independent-copy covariance identity. For a constant variable choose slope zero. Testing the other variable's affine predictor then proves the displayed estimate, with no variance lower bound and no monotonicity assumption.

It therefore suffices to keep every raw preactivation within sqrt(eta_L)/4 of its own initialization. The odd-gain proof's crude control estimate, which survives the added bias, is

    max_(i,l<=L)||z_i^l-z_i^l(0)||_2
       <=3 sqrt(L) (32768/a)^L T0^2/a,
    T0=12/lambda.

The ratio to sqrt(eta_L)/4 is at most

    24 sqrt(L) T0^2/(sqrt(c) a^(3/2)) (32768/sqrt(a))^L.

If a>=65536^2, the maximum over L>=2 is bounded by

    (3*2^34) T0^2/(sqrt(c) a^(5/2)).

Thus, for example, the finite selection

    a >= max{10^12(1+T0), (2^36 T0^2/sqrt(c))^(2/5)},
    0<e<=1,

has strict room for the nonaffinity transfer at every separately fixed L. It gives the absolute gap e^2 c/(16 a^(L-1)). The nonaffinity ratio is then at most 3/4. The first gain bound already exceeds 65536^2. This version uses the manuscript's internal initialized operator norm bound 10, current bound 11, and F=32^L; it does not require the sharper external random-matrix norm theorem.

For a compactly supported nonzero psi, R_psi(sigma G)<=E psi(sigma G)^2 tends to zero as sigma tends to infinity. Our initialized sigma_L tends to infinity. Therefore a positive gap uniform over L is impossible for these selected pairs, already at initialization. This does not invalidate the displayed positive gap at each fixed depth or the common activation pair.

## Direct source-mechanism adaptation

At the same actual source arrays, write X_l=Y_l+r_l and d_l=q_l+u_l. For the normalized activation and its clipped gate,

    r_l=[1+(e/a)psi(K_lY_l)]/K_l, |r_l|<=2/K_l,
    u_l=(e/a)psi'(K_lY_l) tau_R(q_l), |u_l|<=|q_l|,
    |chi_l'|, |partial_q D_l|<=2,
    |partial_z D_l|<=(e/a) K_l |q_l|<=K_l |q_l|.

The affine elimination identities in SOURCE_RESPONSE.md Section 4 are unchanged. With local product r=alpha S b<=1/8, the only changed intermediate bound is

    ||q_l-q_G||_p <=2r||q_l||_p+4b/K_l

in place of pi b/K_l. The stated next estimates still hold with their existing slack:

    ||q_G||_2<=2Q_l+4b/K_l,
    ||q_l||_p<=20(Q_l+b/K_l)sqrt(p),
    ||K_l max_i|q_(l,i)|||_p<=60(K_lQ_l+b)sqrt(p).

The forward bound with coefficient 50 likewise survives: the Q_l coefficient is at most 42 and the b/K_l coefficient is at most 44+4/sqrt(p)<50. The local source Jacobian bounds and forward/reverse coefficient-production inequalities consequently retain their stated constants. No sign of psi' or parity enters them. The global coefficient box must use F=32^L and its corresponding larger sufficient gain; the source specialist is deriving that box separately.

To use only the internal initialized action bound 10, the primal estimate is that |chi_l(y)|<=2|y| is unavailable because of the bias. Its replacement is sufficient: before raw hidden displacement one, ||X_1||_2<=5<=32 and

    ||X_l||_2<=11||X_(l-1)||_2+2<=32^l.

Thus F=32^L bounds forward norms. Backward action/gate growth is 22<=32; the coefficient-control block factor is 6/32<1. Telescoping gives ||Delta Z_l||<=32^(l-1)D+20||Delta Z_(l-1)||<=3*32^(l-1)D and ||Delta X_l||<=32^lD. Therefore D<=3 sqrt(L)F^2S^2 and the displayed drift estimate hold. Positive meshes and actual transpose returns are still required exactly as in the source proof. This is an adaptation of the displayed identities, not an inference from the assertion that the odd-gain theorem is true.

## Global primal arithmetic with the internal norm bound

For F=32^L and S=T0/a^L, the Gram error and clipped hidden contribution are bounded by 18 sqrt(L)(2^20/a^2)^L T0^2 and 27L(2^20/a^2)^L T0^2. For q<=1/4, Lq^L<=2q^2 for L>=2, so these are at most 36*2^40 T0^2/a^4 and 54*2^40 T0^2/a^4. The second is less than 4.13*10^(-37)lambda^2<lambda/4 under a>=10^12(1+T0), T0=12/lambda, 0<lambda<=1. Likewise D<=6*2^20 T0^2/a^4<1/4. There is overwhelming strict slack in these inequalities.

## Motion and normalization checks

For a>e>0, phi'>=a-e>0. A bounded nonconstant C2 psi has psi'' not identically zero, so phi' is nonconstant. Positive initialized Q_L and full Gaussian support at all l>=2 imply positive top backward Gram by the product-identity argument in INITIAL_MOTION.md. The downward fresh-covariance induction, exact same-matrix returns and forward innovation argument then apply without oddness. Every parameter block and sample-layer direction is nonzero. These lower bounds may depend on L; their strict positivity is enough.

Under the above feature normalization grad_raw f_i=a^L grad_raw F_i in every block, including the original readout C. Accordingly s=a^L t and the residual clock a^L integral ||r||_1 produce exactly the same raw gradient flow. No layer metric has been rescaled. The finite Gaussian C_n(0) must remain in both actual finite algorithms until its norm O_P(n^-1) is removed at each fixed L and a. Growing-depth width limits are a separate statement and are not justified by these estimates.

## Remaining scope of the full proof

The uniformity bottleneck is a normalized positive Gram propagated with a summable loss, plus a raw displacement rate that beats a^(−L/2). Both close above. The generic bounded-remainder source argument closes at one gain as well. A full theorem must still cite or reproduce the finite-program realization, cap-removal, uniqueness and GD/velocity/path bridges with all their hypotheses. Those foundational arguments have not been re-proved here merely because their finite-depth induction was stated elsewhere. No genuine counterexample or remaining specifically depth-uniform obstruction emerged from this independent audit.
