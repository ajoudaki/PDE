# Isolated complete-proof audit

## Verdict

**CLEAN. No required mathematical corrections found.**

I read both supplied files completely and independently checked the theorem statements, their quantified ranges, the proofs, the displayed constants, the exceptional cases, and the closing comparisons. The arguments establish the stated initialization results under ordinary elementary analysis. I found no false inequality, unsupported nontrivial proof ingredient, missing hypothesis that changes a stated result, or illicit exchange of width and depth limits.

This verdict includes the statements and exceptions outside the two formally named theorems. It does not certify any training result or any simultaneous depth-width limit; neither is asserted by the supplied proof. The comparison orders are sharp up to universal constants in their stated parameter range, not claims of optimal numerical constants.

## Isolation, source identity, and complete reading coverage

The only source files read were:

| Source | Exact size | Complete line coverage | SHA256 |
|---|---:|---:|---|
| `/tmp/pde-initialization-round4.keU2PWC4/PROOF.md` | 48,765 bytes | 1–1343, all 1343 lines | `411fbe15d0701451a0e4fad0b87bfc5a11d283e200b278d3b75872fb05fa8a27` |
| `/tmp/pde-initialization-round4.keU2PWC4/NOTATION.md` | 5,110 bytes | 1–98, all 98 lines | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The source hashes were obtained before reading and independently checked again after the mathematical review. They matched exactly. Neither source was edited.

The bounded, line-numbered reads of PROOF.md were exactly:

`1–150; 151–290; 291–430; 431–570; 571–710; 711–850; 851–990; 991–1130; 1131–1270; 1271–1343`.

NOTATION.md was read as the single bounded chunk `1–98`. All outputs completed without truncation. Thus all 1441 supplied lines were read, with no gap or reliance on search excerpts.

No project files, history, studies, prior reviews, skills, network sources, or other agents were consulted. No experiments, builds, installations, or numerical checks were run. Computations below are analytic checks. This report was created with `apply_patch` in a fresh private directory, `/tmp/pde-initialization-complete-audit.C6gO5g5O`, whose directory permissions were verified as `0700`.

References below use `P` for PROOF.md and `N` for NOTATION.md. Line ranges refer to the exact hashes above.

## Coverage ledger

Every range below was reviewed; these are verification results, not merely an inventory of headings.

| Lines | Subject and result |
|---|---|
| N 1–14 | Model identifiers, normalized inputs, and realizability: consistent. |
| N 15–42 | Network storage, residual-free derivatives, and loss conventions: consistent with P. |
| N 43–69 | Population types, expectations, pairings, norms, and tensor convention: consistent with P. |
| N 70–89 | Initialization and clock conventions: read in full; initialization agrees with P, and no training assertion is imported into its proofs. |
| N 90–98 | Limit and scope restrictions: respected throughout P. |
| P 1–18 | Announced results and initialization-only scope: supported by the ensuing arguments. |
| P 19–143 | Model, metric, observables, and affine projection: verified. |
| P 144–261 | Fixed-depth width limit and initialized raw kernel: verified. |
| P 262–362 | Hermite completeness, Gaussian covariance identities, endpoints, and contraction: verified. |
| P 363–401 | Cubic tensor lower bound and all nonnegative integer tensor powers: verified. |
| P 402–446 | Odd-mixture theorem and its ranges: verified against both bounding arguments. |
| P 447–552 | Variance decrement, reciprocal bounds, square sums, and linear-weight products: verified. |
| P 553–612 | Cubic coefficient and spectral lower constants: verified. |
| P 613–727 | Composed curvature, strictly admissible planar example, and upper constants: verified. |
| P 728–817 | Nonaffinity, asymptotics, regime table, and linear/antipodal exceptions: verified. |
| P 818–856 | Offset theorem statement and uniformities: verified. |
| P 857–950 | Offset variance bounds, strict contraction, and positive scalar residual floors: verified. |
| P 951–967 | Explicit offset example and derivative norms: verified. |
| P 968–999 | Calibrated shape and depth-dependent activation: verified. |
| P 1000–1086 | Cancellation, variance preservation, explicit kernel, and finite-depth floor: verified. |
| P 1087–1170 | ODE existence, interpolation error, positive semidefiniteness, and sequential limit: verified. |
| P 1171–1191 | Equilateral nonlinear geometric witness: verified. |
| P 1192–1223 | Near-identity estimates and exact scalar residual: verified. |
| P 1224–1254 | Local variance attraction: verified with its stated small-gamma qualification. |
| P 1255–1271 | Scalar Gaussian derivative-moment product and its scope: verified. |
| P 1272–1293 | Comparison table and interpretation: supported by the proved results. |
| P 1294–1312 | Gain normalization and failure of an argument-homogeneity reduction: verified. |
| P 1313–1331 | Gain example separating absolute and relative residuals: verified. |
| P 1332–1343 | Final exclusions and initialization dependence: accurate. |

## 1. Model, normalization, and initialized kernel

### Storage, metric, and scalar observables — P 19–143; N 8–77

The factors of input dimension and width agree throughout. With `u_a=x_a/sqrt(d)`, the first preactivation row has covariance `G`; replacing the first stored matrix by `V^(1)=W^(1)/sqrt(d)` changes its entry variance to `1/d` and preserves that preactivation. Its metric coefficient becomes `d/n`, as stated.

The displayed parameter metric has inverse mobility `n` on the first and readout blocks and mobility one on the middle blocks. It is consequently compatible with the loss-independent kernel convention. The factor `2/3` belongs to differentiating the specified averaged squared loss and is correctly absent from the kernel.

The diagonal recursion is scalar because every preactivation marginal has the same variance. `Q_l` is a second-moment matrix, including in the offset case; it is not silently centered. It is positive semidefinite by its Gram representation. If its positive common diagonal is `q_l`, then `C_l` has trace three, so `1 <= lambda_max(C_l) <= 3`. Dividing eigenvalues by `q_l` proves both comparisons in (V.M.7). Positivity of the necessary denominators is established separately for each family.

For `q>0`, the affine approximation space is exactly the span of `1` and the standard Gaussian coordinate. These two vectors are orthonormal in Gaussian L2. The projection formula (V.M.9), including the absence of an extra factor of `q` in its last term, is correct: the optimizing preactivation slope is `E[xi g(sqrt(q)xi)]/sqrt(q)`.

### Finite-width induction — P 148–184

This proof uses exact conditional Gaussianity, not an unproved Gaussian approximation. At the first layer, the row triples are independent Gaussian vectors with covariance `G`. At a later layer, conditioning on the preceding features makes the row triples independent with covariance equal to the preceding empirical feature Gram.

Linear growth gives a uniform second moment for each activated product when the conditioning covariance has bounded diagonal: its second moment is controlled by Gaussian fourth moments and Cauchy–Schwarz. The stated conditional Chebyshev bound therefore applies. Inductive convergence of the diagonals supplies an event with probability tending to one on which that uniform bound is valid.

The argument for continuity of the positive semidefinite square root is valid at singular matrices. Bounded roots have subsequential limits; every such limit is a positive semidefinite square root of the limiting covariance and hence is unique by spectral decomposition. Coupling with a common three-dimensional standard Gaussian, Lipschitz continuity gives L2 convergence of the coordinates, and Cauchy–Schwarz gives convergence of product expectations. This closes the induction and, since the number of entries and layers is fixed, proves the asserted joint convergence in probability.

### Kernel blocks and small readout — P 186–261

Direct differentiation gives the Euclidean first derivative `delta_a^(1) x_a^T/(n sqrt(d))`. Pairing this derivative with its counterpart and multiplying by inverse mobility `n` gives `G_ab (delta_a^T delta_b)/n`. A middle block contributes the product of the two normalized pairings in (V.F.3); the readout contributes the feature Gram. No factor of `n`, `d`, or the loss is missing.

The net bound is internally complete. Radius-`1/8` balls around a `1/4`-separated sphere family fit in a radius-`9/8` ball, giving at most `9^n` points. Approximating each argument of a bilinear pairing changes it by at most one quarter of the operator norm, so the two errors give the stated factor two. For a fixed pair the variance is `1/n`, and the threshold five gives the exponent `-25n/2`. Thus

`2 * 9^(2n) * exp(-25n/2) -> 0`,

since `2 log(9) < 25/2`. Only the finitely many square hidden matrices require this bound; no unproved bound on the rectangular first matrix is needed.

The readout calculation is `E[||W^(L+1)||_2^2/n]=n^(-2)`. Consequently its RMS is `O_P(n^(-1))`. Bounded derivatives and the hidden operator norms propagate this estimate backwards exactly as in (V.F.5), without any false independence assumption between backward fields and forward features. The hidden blocks are `O_P(n^(-2))` at fixed depth, while the readout block tends to `Q_L`. The prediction bound also tends to zero.

The proof supplies neither a uniform approximation for increasing depth nor a construction of joint trained population operators. The remarks concerning zero initial backward fields do not add either assertion.

## 2. Gaussian foundations and cubic lifting

### Hermite completeness and covariance identities — P 262–342

Orthonormality follows from the product generating function with the correct probabilists' normalization. For the completeness argument, the squared coefficients at imaginary argument sum to `exp(eta^2)`, so the generating series converges in Gaussian L2. Its entire pointwise sum identifies that limit, for example by passing to an almost-everywhere convergent subsequence. Orthogonality to all polynomials therefore annihilates the Fourier transform of the L1 density `u(x) exp(-x^2/2)/sqrt(2 pi)`.

Fourier uniqueness is not left as an external theorem. The supplied argument derives the Gaussian characteristic function, uses its scaled Fourier representation in a convolution, justifies Fubini by an explicit integrable bound, and proves that Gaussian convolutions approximate an L1 function using translation continuity. Translation continuity is reduced to interval step functions and their ordinary L1 density. These are elementary analysis steps, not an unprovided special Gaussian theorem.

The correlated generating function gives the diagonal pairing `1_{j=k} rho^j`, including correlations `+1` and `-1`. L2 approximation extends it to general Gaussian L2 functions, with absolute convergence of the same-function series at both endpoints supplied by Parseval.

The derivative identities have the correct factors `sqrt(j)` and `sqrt(j(j-1))`. The assumed growth and derivative bounds make the integration-by-parts boundary terms vanish. Applying completeness to the derivatives then gives exactly the two weighted coefficient sums. Their finiteness implies uniform convergence of the differentiated covariance series on the whole closed interval.

The endpoint signs are correct: at `-1` the first derivative uses `(-1)^(j-1)` and the second uses `(-1)^(j-2)`. These are appropriately one-sided derivatives on the correlation domain. The proof does not replace either with an unsigned sum at the negative endpoint.

### Gaussian contraction — P 344–361

For every integer `j>=1` and every `rho` in `[-1,1]`,

`1-rho^j = (1-rho)(1+rho+...+rho^(j-1)) <= j(1-rho)`.

This remains valid for negative correlations; it does not require all summands in the geometric sum to be nonnegative. Combining it with the derivative Parseval identity for `f(x)=phi(sigma x)` gives precisely the factor `sigma^2 E[phi'(sigma xi)^2]`. Thus (V.F.11) is valid for each family and at singular covariance endpoints, including the offset case where a centered-feature interpretation would have been incorrect.

### Cubic tensor estimate — P 363–401

Separation gives `1-C_ab^2 >= delta(2-delta)>0`, so every denominator defining `v_ab` is valid. Each `T_a` has unit norm. It annihilates the other two sample tensor cubes, while its pairing with its own sample cube is at least `s_delta`.

For `T=sum b_a v_a^(tensor 3)`, this yields

`s_delta^2 sum b_a^2 <= sum |<T_a,T>|^2 <= 3 ||T||^2`.

The test tensors need not be mutually orthogonal or symmetric; the three separate Cauchy–Schwarz bounds suffice. This proves the exact factor `s_delta^2/3` in (V.F.12), including when the original Gram is singular. All other integer entrywise powers are positive semidefinite by their stated tensor realizations; degree zero is explicitly the constant Gram.

## 3. Literal odd mixture

### Hypotheses and variance estimates — P 402–552

Theorem V.O.1 concerns infima over actual unit triples in every dimension `d>=2`, with strict two-sided separation, integer depth `L>=1`, `0<theta<=1`, and `0<delta<=1/4`. The proof provides an admissible triple within this open constraint set; it does not assume the infimum is attained. The broader positive-definiteness lower bound uses closed absolute separation and does not extend the sharp upper comparison beyond its stated delta range.

For positive `theta` and nonzero `z`, the activation has the sign of `z` and smaller absolute value. Hence `0<q_+<q`. Gaussian integration by parts identifies the linear projection coefficient `c(q)`. Jensen gives `c(q)>=1/2` for `q<=1`, so `q_+>=q/4`.

Writing `u(z)=z-arctan(z)`, one has `0<=u(z)^2<=z u(z)`. The decrement bounds therefore retain the correct factor `theta(2-theta)` in their lower estimate. For the weighted Cauchy–Schwarz step,

`(E xi^2)^2 <= E[xi^2/(1+q xi^2)] * E[xi^2(1+q xi^2)]`,

and the second factor is `1+3q`. This proves the lower bound on `1-mu(q)`. Using `q<=1`, `2-theta>=1`, and `q/4<=q_+<=q` gives

`theta q^2/4 <= q-q_+ <= 2 theta q^2`,

`theta/4 <= 1/q_+ - 1/q <= 8 theta`.

Iteration proves (V.O.6). Summing the decrement bound gives `sum q_k^2 <= 4/theta`; monotonicity also gives `sum q_k^2 <= L`. The integral of `(1+8 theta x)^(-2)` from zero to `L` is exactly `L/(1+8 theta L)`, proving the lower square-sum bound. The final comparison with `5L/(1+theta L)` holds on both sides of `theta L=4`.

Oddness removes all even Hermite coefficients, including the constant. The correlation map is therefore an odd nonnegative-coefficient power series with coefficient sum one. It preserves absolute separation, even for negative input correlations.

The projection residual is bounded by testing the identity fit and using `|u(z)|<=|z|^3/3`. The sixth Gaussian moment gives `(5/3) theta^2 q^3`. Dividing by `q c(q)^2>=q/4` proves the logarithmic linear-weight bound `(20/3) theta^2 q^2`. Finally

`(20/3) theta^2 sum q_k^2 <= (80/3) theta <= 80/3`,

which proves the uniform product floor `p_*=exp(-80/3)` for every required subsequent product, including the empty product.

### Cubic injection and lower constants — P 553–612

Integrating the normalized third Hermite coefficient once leaves `sqrt(q) E[(xi^2-1)/(1+q xi^2)]/sqrt(6)`. The second integration-by-parts identity turns this into

`-sqrt(2/3) q^(3/2) E[xi^2/(1+q xi^2)^2]`,

so both its sign and normalization are correct. The Gaussian probability tilted by `xi^2` has mean `E_tilt[xi^2]=3`. Jensen yields an expectation at least `(1+3q)^(-2)>=1/16`, giving `b_3(q)^2>=q^3/384` and `w_3(q)>=theta^2 q^2/384`.

Tensor positivity allows all other Hermite terms to be discarded in a matrix lower bound. The degree-three term injects `s_delta^2 w_3/3` times the identity at each layer; later linear terms retain at least the factor `p_*`. The resulting normalized and absolute bounds are

`lambda_min(C_L) >= p_* s_delta^2 theta^2 L / [1152(1+8 theta L)]`,

`lambda_min(Q_L) >= p_* s_delta^2 theta^2 L / [1152(1+8 theta L)^2]`.

Here `1152=3*384`. Using `s_delta>=delta` and `1+8x<=8(1+x)` gives exactly the stated denominators `9216=1152*8` and `73728=1152*64`. These arguments require no invertibility of `G`.

### Composition and upper constants — P 613–727

Composition preserves odd powers, coefficient nonnegativity, and coefficient sum one. Rearrangement for nonnegative arguments is justified by nonnegativity; absolute convergence then supplies the negative arguments as well.

The endpoint derivative identities give the stated `d_k` and `b_k`. Since

`phi_theta''(z)=-2 theta z/(1+z^2)^2`,

the lower bound on `q_{k+1}` gives `b_k<=16 theta^2 q_k^2`. The integer inequality `j-1<=j(j-1)/3` for odd `j>=3` gives `d_k-1<=b_k/3`, while the coefficient sum gives `d_k>=1`. Consequently `sum b_k<=64` and `sum(d_k-1)<=64/3`.

The endpoint chain rule is legitimate by the earlier uniform derivative convergence and finite composition. Dividing the recurrence for `B_k` by that for `A_k` yields exactly

`B_L=A_L sum_{k<L} (b_k/d_k) A_k`.

Both factors `A` are at most `exp(64/3)`, proving the exponent `128/3`. The square-sum estimate then gives

`F_L''(1) <= 80 exp(128/3) theta^2 L/(1+theta L)`.

For the planar triple, `c=1-2delta` lies in `[1/2,1)` and `r=2c^2-1`. Its strict upper and lower margins are:

| Entry | Margin below `1-delta` | Margin above `-1+delta` |
|---|---:|---:|
| `c` | `delta` | `2-3delta` |
| `r` | `delta(7-8delta)` | `(1-4delta)(2-2delta)+delta` |

Every margin is positive throughout `0<delta<=1/4`, including at `delta=1/4`. Zero-padding realizes the same example for every larger dimension. Its null vector is `(1,-2c,1)` and its squared norm is `2+4c^2>=3`.

The expression for `E_j` and its second derivative are correct, including when `r` is negative. The absolute derivative bound is

`8+8j+32j(j-1)+8j(j+1)=40j^2-16j+8 <= 54j(j-1)`.

The last inequality holds already at `j=3` and increases thereafter. Since `E_j(1)=E_j'(1)=0`, Taylor's integral remainder gives `E_j(c)<=27j(j-1)(1-c)^2`. Tensor positivity gives its nonnegativity. The Rayleigh quotient then contributes at most `9(1-c)^2 F_L''(1)=36delta^2 F_L''(1)`.

The coefficient sum `sum j(j-1)p_{j,L}=F_L''(1)` used here follows by termwise differentiation inside `(0,1)` and monotone passage to the endpoint, whose continuous derivative has already been established. No new smoothness assumption is needed.

Thus the normalized upper constant is exactly `36*80=2880`, times `exp(128/3)`. Multiplying by `q_L<=4/(1+theta L)` gives `11520 exp(128/3)` for the absolute upper constant. The example matches the full joint parameter order, not just a limit with one parameter fixed.

### Scalar residuals, asymptotics, and exceptions — P 728–817

The squared cubic coefficient survives affine projection and gives the lower scalar residual bound. The previous identity-fit upper bound and the two variance bounds give all four inequalities in (V.O.23).

For fixed positive `theta`, (V.O.6) implies `q_l->0`. Dominated convergence gives `(1-mu(q))/q->1`, while the squared `u` term is `O(q^3)`. Hence the reciprocal variance increments tend to `2theta`. Averaging those increments proves `q_l~1/(2theta l)`; no uniformity as `theta` changes with depth is claimed for this equivalent.

The integrated arctangent identity gives a global remainder bounded by `|z|^5/5`. After Gaussian scaling and projection, the leading residual is `-q^(3/2) H_3/3` with L2 error `O(q^(5/2))`. Since `E H_3^2=6`, this proves `R_arctan(q)~(2/3)q^3`. The linear term in the mixture is absorbed exactly, giving `R_phi_theta=theta^2 R_arctan`.

At preactivation variance `q_(l-1)`, the constants become precisely `1/(12theta l^3)` for the absolute residual and `1/(6l^2)` for its relative version. The indexing shift does not change the fixed-theta equivalents. The separate joint comparison bounds remain uniform in theta and layer as stated.

Normalized sample conditioning has a positive floor at each fixed positive theta and fixed admissible separation, because `L/(1+8theta L)>=1/(1+8theta)`. Absolute conditioning has no such floor since its smallest eigenvalue is at most `q_L->0`. The two rows of the regime table follow algebraically from the proved joint orders.

The exclusions are substantive and correct. Antipodal inputs give opposite features under every odd layer. At `theta=0`, the population recursion is exactly `Q_L=G`; it cannot satisfy the positive-mixture conclusions. The equilateral planar triple is strictly admissible precisely for the claimed `delta<1/2`, has `G 1=0`, and its input sum is zero. Every bias-free linear network therefore has prediction sum zero on it and cannot produce three labels equal to one. This is explicitly a statement about that linear reference, not a training result for positive theta or a claim about arbitrary affine models with a free bias.

## 4. Literal convex offsets

### Variance interval and strict contraction — P 818–913

For the stated `0<epsilon<1/2`, the lower bound `b_epsilon=1-2epsilon` is strictly positive. The mean is at least `b_epsilon`; decomposing the activation into its linear part and a remainder bounded by one gives `sigma_next<=(1-epsilon)sigma+1`. Starting at `sigma_1=1`, the interval `[b_epsilon,1/epsilon]` therefore contains every preactivation standard deviation, and `b_epsilon^2<=q_l<=epsilon^(-2)` holds at every feature layer.

The derivative belongs to `[b_epsilon,1]`. Its squared Gaussian expectation is continuous in the positive standard deviation. Equality to one at any such standard deviation would imply derivative one everywhere by continuity and Gaussian full support, and hence `psi'=1` everywhere, contradicting boundedness. Compactness gives a maximum strictly below one, with `b_epsilon<=kappa<1`. This strictness does not need a pointwise derivative supremum strictly below one.

Applying (V.F.11) to each layer gives `D_l,ab<=kappa^2 D_(l-1),ab`, with the correct initial difference `2(1-G_ab)`. The equal-diagonal recursion justifies identifying the preceding feature difference with the next preactivation difference. Negative and singular correlations are covered by the Gaussian foundation.

The unit vector `(e_a-e_b)/sqrt(2)` gives Rayleigh quotient `D_L,ab/2`; there is no missing factor two. Dividing by the lower variance bound gives the normalized inequality. For the condition-number ratio, the constant-vector test and the common positive mean give the stronger denominator

`lambda_max(Q_L) >= E[(H_1+H_2+H_3)/sqrt(3)]^2 >= 3b_epsilon^2`.

This verifies the factor three in the fourth inequality of (V.C.2). Finally `1-C_L,ab=D_L,ab/(2q_L)` tends to zero, proving convergence of the normalized matrix to the all-ones matrix, not convergence of a centered Pearson correlation matrix.

### Nonaffinity floors and concrete shape — P 915–967

A bounded continuous nonconstant shape cannot agree almost surely with an affine function under any nondegenerate Gaussian: full support extends the equality everywhere, and boundedness would make the affine slope zero. Thus its scalar residual is positive at every positive variance. The projection formula and the stated integrable bounds make that residual continuous on the compact standard-deviation interval above, so its minimum there is positive.

Absorbing the affine part of the offset activation multiplies this residual by exactly `epsilon^2`. Dividing by `q_l<=epsilon^(-2)` gives the stated relative lower bound `epsilon^4 r_(epsilon,psi)`. The inclusion of `sigma_1=1` in the compact interval checks the first layer as well. These constants correctly depend on the fixed shape and epsilon; scaling the shape towards zero demonstrates why no uniform residual floor over the full shape class follows.

For `psi=arctan/4`, the three norms are exactly `pi/8`, `1/4`, and `3sqrt(3)/32`. The maximum of `x/[2(1+x^2)^2]` occurs at `x=1/sqrt(3)`. With `epsilon=1/4`, the derivative of the resulting literal activation lies in `[3/4,13/16]`. Its pointwise Lipschitz bound indeed gives the announced contraction rate directly.

## 5. Calibrated depth-dependent family

### Shape, cancellations, and explicit kernel — P 968–1051

The derivative `w'(0)=exp(3/2)-1` is nonzero, so Gaussian full support makes `v_*>0`. Boundedness of the shape and all derivatives follows from its finite trigonometric construction.

The characteristic-function identity gives `E[xi sin(t xi)]=t exp(-t^2/2)`. With `c_*=exp(3/2)/2`, the two terms in `E[xi w(xi)]` cancel exactly. Oddness gives zero mean, and normalization gives squared norm one. These three facts prove unit output variance for a unit-variance input. Induction therefore gives `q_k=1` at every layer, for every finite depth and every positive tau.

The Gaussian pair representation makes the linear-shape cross terms zero, including at correlations `+1` and `-1`. The resulting map is exactly `(rho+gamma^2 K(rho))/(1+gamma^2)`.

The sine product identity yields the numerator in (V.D.5). Directly checking the coefficients gives

`v_*=exp(-1)[sinh(1)-sinh(2)+(1/4)sinh(4)]`,

and for each odd degree the numerator is `(2^(j-1)-1)^2`. The linear coefficient vanishes; the cubic coefficient is `9/(6N_*)=3/(2N_*)`. All higher coefficients are nonnegative and sum to one. Their entire series implies `0<=K(rho)<=rho^3` on `[0,1]`; oddness supplies the absolute-value contraction on the negative interval.

The subscript on `phi_L` is correctly used: a single depth-dependent activation is held fixed throughout a network with that depth. It is not varied with the layer index within that network.

### Uniform finite-depth floor — P 1053–1086

For a realizable separated triple, all iterates preserve the same absolute separation and are unit-diagonal positive semidefinite matrices. Tensor positivity and the positive cubic coefficient give `K[C]>=mu_delta I`, with the displayed `mu_delta=p_3 s_delta^2/3`.

The affine matrix recursion with `b=(1+tau/L)^(-1)` gives

`Q_k >= b^k G+(1-b^k)mu_delta I`.

This induction uses a direct matrix lower bound at each step, not an unproved matrix monotonicity property of the nonlinear entrywise map. Dropping the positive semidefinite term gives (V.D.9). The integer binomial inequality `(1+tau/L)^L>=1+tau` gives exactly the floor `mu_delta tau/(1+tau)`.

Here the separation hypothesis is essential to the positive floor, and it is stated before these estimates. Its allowed endpoint `delta=1` means zero off-diagonal input Gram and is conditional on realizability. Neither the shape nor tau is selected as a function of delta. Large gamma at small depth causes no difficulty: none of this argument requires the activation itself to be monotone.

### ODE existence and discretization — P 1087–1147

The depth-coordinate equation is self-contained. `F=K-id` is bounded by two and is `D`-Lipschitz on `[-1,1]`. Clipping its argument extends it globally while preserving both bounds. The integral-map construction on intervals with `Dh<1` supplies existence and uniqueness by a geometric Cauchy estimate in the complete continuous-path space. Repetition covers every finite horizon. The constant solutions at `+1` and `-1`, together with uniqueness at an endpoint contact, prove invariance of the original interval. The discrete update also stays in it by convexity.

The discrete mesh spacing is `a_L=tau/L`, whereas its update coefficient is `a_L/(1+a_L)`. The proof accounts for this difference explicitly; it does not mistake the recursion for exact Euler with coefficient `a_L`.

The ODE increment has local error at most `DB a_L^2/2`; changing the step coefficient contributes at most `B a_L^2`. Subtracting increments gives exactly

`e_(k+1) <= (1+D a_L)e_k+B(1+D/2)a_L^2`.

Summing at most `L` terms and using `(1+D a_L)^L<=exp(D tau)` proves the constant in (V.D.12). Interpolating the endpoints adds at most the asserted `B tau/L`. The constants are uniform over every initial correlation in the closed interval. In particular, initial correlations `-1`, `0`, and `1` are exact equilibria in both constructions; the error estimate does not hide a failure there.

### Matrix and width-first limit — P 1149–1170

Entrywise interpolation is a convex combination of adjacent positive semidefinite matrices, so its limiting matrix is positive semidefinite. The diagonal is one because correlation one remains fixed. Passing the matrix lower bound to the limit gives, in fact,

`Q(tau) >= exp(-tau)G+(1-exp(-tau))mu_delta I`,

which directly implies the weaker eigenvalue bound printed in (V.D.13). The separation assumption attached to `mu_delta` remains necessary; the unrestricted scalar ODE existence assertion does not grant that floor to unseparated data.

The width limit is taken separately for each fixed `L`, with that entire activation `phi_L` fixed, and is convergence in probability. Only after it is taken does the deterministic population depth limit apply. The same order of limits applies to the raw kernel by V.F.1. The scalar interpolation rate contains no finite-width error term and therefore cannot justify a diagonal choice `L=L(n)` or an interchange of limits. The text explicitly respects this limitation.

### Equilateral witness — P 1171–1191

For the equilateral initial triple, the common off-diagonal entry is `-r(s)`, where `r(0)=1/2`. Oddness and ODE uniqueness give the stated positive-sign equation for `r`. Up to a putative first zero, `r'>=-r` yields `r>=exp(-s)/2`, excluding that zero. The upper bound `r'<=r^3-r` makes `r` nonincreasing and at most one half.

Differentiating `u=r^(-2)` reverses the upper differential inequality in the correct direction and gives `u'>=2(u-1)`. Thus `u>=1+3exp(2s)`. The eigenvalues of the equicorrelation matrix are `1-2r` and `1+r` twice, so (V.D.14) follows with the correct strict inequality for `s>0`. At `s=0` the smallest eigenvalue is zero, as it should be. This is a valid geometric witness that the evolution is not merely multiplication of the input Gram by a scalar.

### Near identity, residual, local attraction, and moment bound — P 1192–1271

Writing `A=(1+gamma^2)^(-1/2)`, the derivative difference is `(A-1)+A gamma chi'`, and the value difference is `(A-1)z+A gamma chi(z)`. The global inequality `1-A<=gamma^2/2` proves both estimates in (V.D.15); the second derivative has the extra factor `A<=1`. Local uniform convergence of values is correctly distinguished from an unweighted global supremum, which is infinite at every finite depth because `A-1` is nonzero and the shape is bounded.

At variance one, orthogonality leaves the residual `A gamma chi` after projection, with squared norm `gamma^2/(1+gamma^2)=tau/(L+tau)`. Output second moment one makes its absolute and relative versions identical. This holds at every layer of the fixed-depth calibrated network.

For the local variance map, integration by parts gives the cross term `q a(q)`. The explicit derivative-average formula has

`a(1)=0`, and `a'(1)=-3exp(-1/2)/(2sqrt(v_*))`.

Boundedness of the shape and its derivative, with `q` restricted near one, justifies differentiating `b(q)` and continuity of its derivative. The exact derivative at the fixed point is

`V_gamma'(1)=[1-3exp(-1/2)gamma/sqrt(v_*)+gamma^2 b'(1)]/(1+gamma^2)`.

Its expansion is precisely (V.D.18). The linear coefficient is strictly negative, so its absolute value is below one for all sufficiently small positive gamma. Continuity supplies a neighborhood with derivative magnitude uniformly below one; the mean value theorem makes that neighborhood invariant and gives convergence of nearby iterates. The qualification of sufficiently large `L` at fixed tau is necessary and is present. No global attraction or control of accumulated random variance errors is inferred.

Finally `E chi'=0` cancels the linear derivative cross term, giving the exact scalar moment in (V.D.19). Dropping its denominator and using `log(1+x)<=x` proves the stated product bound. It is correctly described as a product of scalar Gaussian expectations, not a product of random matrix norms, a network Jacobian estimate, or a trained backward-field estimate.

## 6. Closing comparisons, gain scaling, and scope

### Comparison table — P 1272–1293

Each entry of the final comparison table is supported by the corresponding proved bound. The sharp odd-mixture statement retains `delta<=1/4`; the calibrated lower bound retains closed separation and realizability. For the offset family, it is the normalized matrix that tends to rank one, as proved earlier. The absolute and relative scalar residual conclusions are distinct from sample conditioning and have the stated dependence on fixed parameters.

A uniform numerical initialized floor and a statement at each separately fixed finite depth are not interchangeable. The text correctly draws no conclusion about the existence or failure of a trained theorem from either initialized phenomenon.

### Normalizing a gain changes the model — P 1294–1312

For `a>e>0`, setting `epsilon=e/(a+e)` does produce the literal convex-offset shape after division by `a+e`. If that sum differs from one, the first feature Gram is already changed: its original diagonal is positive because the mean is at least `a-e`, and division multiplies it by `(a+e)^(-2)`.

For general positive scalar scaling `phi -> alpha phi`, the first Gram becomes `alpha^2 Q_1`, while the second is `alpha^2 E[phi(alpha Z)phi(alpha Z)^T]` with `Z` having covariance `Q_1`. This is the correct location of the changed inner argument. For the specified gain activation, a putative identity `g(alpha z)=c g(z)` first forces `c=1` at zero, since `g(0)>0`; the limit `g(z)/z->a` then forces `alpha=1`. Thus the claimed homogeneity reduction is unavailable. This argument is not interpreted as ruling out every accidental equality of an individual Gram entry for special data.

### Absolute versus relative gain residuals — P 1313–1331

The affine component can be absorbed in the regression, so the residual is exactly `e^2 R_psi(q)<=e^2`, using the zero fit and `||psi||_infinity<=1`. The linear projection coefficient equals `sqrt(q)(a+e E psi'(sqrt(q)xi))`. The derivative bound gives the squared second-moment lower bound `q(a-e)^2`.

With `a-e>1`, iteration from `q_0=1` yields `q_l>=(a-e)^(2l)`. Dividing the residual at preactivation variance `q_(l-1)` by its output second moment `q_l` gives exactly the stated relative upper bound `e^2/(a-e)^(2l)`. The text does not assert that an absolute residual floor actually exists for every such shape; the conclusion is explicitly independent of that unresolved property. No outside result about gain-based training is needed.

### Self-containment and final scope — P 1332–1343; N 70–98

The nontrivial specialized tools needed by the proof are present: fixed-depth conditional concentration, singular-covariance continuity, a Gaussian matrix norm bound, Hermite completeness and derivative identities, negative-correlation contraction, cubic tensor separation, the composed-curvature estimate, and a direct existence/error proof for the depth ODE. The remaining background consists of ordinary finite-dimensional linear algebra, Gaussian integration by parts and elementary integrability, Cauchy–Schwarz, Jensen and Minkowski, Chebyshev/Markov, compactness, dominated convergence, Fubini, and elementary Lp approximation. No result from another project part is required.

References to other parts or trained dynamics serve only to distinguish conventions or exclude conclusions. NOTATION.md's training terminology was read as part of the contract; it does not introduce a physical horizon or trained-law assumption into this initialization chapter. In particular, no statement here needs response histories, continuation, cap removal, or optimizer convergence.

## Adversarial challenges resolved

| Attempted failure case | Resolution |
|---|---|
| Singular input Gram invalidates the Gaussian induction or cubic lift | Square-root continuity is proved at singular matrices; tensor testing does not invert the original Gram. |
| A negative correlation breaks Gaussian contraction or an odd map bound | The full `[-1,1]` Hermite identity and the geometric-sum inequality cover contraction; odd powers cover the odd-map absolute bound. |
| The planar upper example only satisfies non-strict separation | All four margins are strictly positive, even at `delta=1/4`. |
| The claimed infimum ranges are empty in dimension two | The supplied planar example lies in the required set for every `0<delta<=1/4`. |
| The positive-mixture floor silently includes `theta=0` | That endpoint is excluded from the theorem and has an explicit singular counterexample. |
| The stronger closed-separation lower bound asserts realizability for every delta and dimension | It is conditional on realizability; the sharp two-sided theorem has its separate, verified nonempty range. |
| Nonlinearity accumulated early is erased by later near-linear layers | The subsequent linear-weight product has the proved positive uniform lower bound. |
| A factor of width or loss changes the initial kernel | Metric differentiation gives exactly the printed blocks; the small stored readout eliminates the hidden contributions at fixed depth. |
| Offset contraction is only pointwise strict, with supremum one | Compactness of the variance interval upgrades the strict Gaussian average at each variance to a uniform `kappa<1`. |
| The offset ratio bound has an unjustified factor three | The constant-vector Rayleigh quotient and positive common mean give `lambda_max>=3b_epsilon^2`. |
| Uniform offset scalar residuals contradict conditioning collapse | The scalar residual is bounded on a compact variance interval, whereas pairwise differences contract; these are different observables. |
| Calibrated variance preservation requires small gamma | Orthogonal cancellation is exact for every finite positive gamma; only local variance attraction needs small gamma. |
| The depth recursion uses the wrong Euler clock | The proof explicitly bounds the difference between mesh spacing `a_L` and update coefficient `a_L/(1+a_L)`. |
| The calibrated positive floor includes antipodal or duplicate inputs | It is conditioned on positive absolute separation; unrestricted endpoint correlations only enter the scalar ODE statement. |
| The sequential limit proves a simultaneous depth-width theorem | Its inner mode is fixed-depth convergence in probability; its outer approximation is deterministic and contains no finite-width rate. |
| A gain can be removed by one final kernel scaling | The next layer's Gaussian argument changes, and the asserted gain homogeneity identity is impossible unless the scaling is one. |
| Other project parts supply missing ingredients | Every specialized ingredient used is proved in the supplied chapter; outside-part mentions have no proof dependency. |

## Required corrections

None. The audit verdict is **CLEAN** for the exact source hashes and initialization-only claims identified above.
