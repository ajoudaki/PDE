# Isolated complete-proof audit: initialization geometry

## Verdict

**CLEAN within the stated initialization scope. No required mathematical corrections found.**

I checked the complete supplied proof, its numerical constants, parameter ranges, singular-covariance endpoints, asymptotic qualifiers, and supporting arguments. The odd-mixture bounds, convex-offset contraction and nonaffinity bounds, calibrated finite-depth bounds, and sequential width-first/depth-second limit are supported by the arguments supplied. The conclusion does not assert optimal numerical constants, a simultaneous depth-width limit, or any training result.

This is a direct mathematical audit, not an experimental assessment. The detailed checks below record the reasons for the verdict, including places where changing a hypothesis or confusing two different limits would invalidate a conclusion.

## Source identity, isolation, and complete line coverage

Only these two source files were read:

| Source | Lines | Bytes | SHA256 |
|---|---:|---:|---|
| `/tmp/pde-initialization-round4.keU2PWC4/PROOF.md` | 1343 | 48765 | `411fbe15d0701451a0e4fad0b87bfc5a11d283e200b278d3b75872fb05fa8a27` |
| `/tmp/pde-initialization-round4.keU2PWC4/NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The complete first-pass reading used numbered, bounded chunks. Every chunk returned successfully without truncation:

| Source | Actual source lines covered |
|---|---|
| NOTATION.md | 1–98, through EOF; the requested window was 1–180 |
| PROOF.md | 1–160 |
| PROOF.md | 161–320 |
| PROOF.md | 321–480 |
| PROOF.md | 481–640 |
| PROOF.md | 641–800 |
| PROOF.md | 801–960 |
| PROOF.md | 961–1120 |
| PROOF.md | 1121–1280 |
| PROOF.md | 1281–1343, through EOF |

Coverage is exactly PROOF.md 1–1343 and NOTATION.md 1–98: all 1441 source lines, with no gaps. All line references below are to these identified versions. Unless otherwise specified, a line reference means PROOF.md.

No project files, history, studies, prior reviews, network sources, skill files, or other agents were consulted. No experiments, builds, installations, or input edits were performed. The report is the only audit artifact, in a fresh private directory created for this audit.

Both source SHA256 hashes were checked again after drafting this report and exactly matched the initial hashes above. The output directory `/tmp/pde-initialization-proof-audit.YXX4uqEg` was verified to have permission mode `0700`.

The elementary background used is ordinary finite-dimensional linear algebra, Gaussian integration, basic Lebesgue integration and convergence, Cauchy–Schwarz, Jensen, elementary Taylor estimates, and completeness of the usual function spaces. The proof supplies the substantive Gaussian-series, tensor-lifting, matrix-norm, and ODE arguments; it does not need an external neural-network limit theorem or an external Gaussian-kernel theorem.

## Notation and scope audit

**NOTATION.md 1–98; PROOF.md 1–142 and 1272–1343.**

- The layer count, three samples, input dimension, and hidden width agree with NOTATION.md 10–24. The normalization is `u_a=x_a/sqrt(d)`, hence `G_ab=x_a^T x_b/d` and `G_aa=1`.
- Matrix shapes and stored-readout normalization agree. In particular, the stored readout has entry variance `n^(-2)`, and prediction has the additional factor `1/n`. Replacing either convention would change the kernel argument.
- The alternative first-layer storage has variance `1/d` and metric term `d ||dV^(1)||_F^2/n`. The factor `d` is correct: `dW^(1)=sqrt(d) dV^(1)`.
- The raw metric has inverse multipliers `n,1,...,1,n`. It is the predictor-gradient metric. The squared-loss multiplier `2/3` is correctly excluded from the kernel and stated separately.
- The backward variables contain no residual and satisfy the convention `delta=n partial f/partial z`. Transposes have their actual finite-matrix meaning. The argument never substitutes independent reverse maps.
- The population recursion uses a separate Gaussian population at each layer. Expectations of sample products contract within that layer. No joint population weight action across layers is assumed.
- Equal diagonal entries follow inductively from the identical scalar Gaussian marginals. Each diagonal therefore depends only on the activation and preceding diagonal, not on off-diagonal input geometry.
- `Q_l` is consistently the uncentered feature Gram and the covariance of the next centered Gaussian preactivation. The text correctly distinguishes this from centered feature covariance and, for the offset family, from Pearson correlation.
- Each family has a strictly positive feature second moment. Thus every normalization and relative-nonaffinity denominator used for these families is legitimate.
- The eigenvalue comparison (V.M.7) follows from positive semidefiniteness and trace three: `1 <= lambda_max(C_l) <= 3`. Both factors of three have the correct direction.
- Affine projection onto the orthonormal pair `1,xi` gives (V.M.9). The regression slope against `sqrt(q) xi` is free because `q>0`, so no extra factor of `q` belongs in the last squared term.
- NOTATION.md's general discussion of losses, clocks, and trained models is not imported as a theorem about this initialization problem. Its formal rank-one normalization and backward-field conventions are consistent with the proof. Its arctangent primitive factors are also algebraically consistent with the reciprocal activation derivatives. No training claim is inferred from those conventions.

References to other parts of a larger work are contextual distinctions, not proof dependencies. The needed initialization model, metric, Gaussian recursion, and estimates are all stated here.

## Fixed-depth finite-width identification

**Lines 144–260; equations (V.F.1)–(V.F.6). Verified.**

At the first layer, row triples are independent `N(0,G)` even when `G` is singular. A globally Lipschitz activation has at most linear growth, so each activated product has finite variance. Ordinary Chebyshev applies.

At each later layer, conditioning on preceding features gives independent Gaussian row triples with covariance equal to their empirical Gram. Bounded preceding diagonals bound the necessary Gaussian fourth moments and hence conditional product variances. Inductive convergence makes the event of bounded diagonals have probability tending to one. The conditional averaging error is therefore negligible.

The remaining conditional-expectation limit is justified also at singular covariance matrices. The compactness/uniqueness argument for positive square roots is valid in fixed dimension. Coupling with one standard three-dimensional Gaussian gives convergence in `L^2` of the activated coordinates; Cauchy–Schwarz then gives convergence of product expectations. This closes the induction, and the finite number of layers and entries permits joint convergence in probability.

The kernel block factors were checked directly:

- First derivative: `delta_a^(1) x_a^T/(n sqrt(d))`. Pairing and multiplying by mobility `n` gives `G_ab (delta_a^T delta_b)/n`.
- Middle derivative: `delta_a^(l) (h_a^(l-1))^T/n`. Unit mobility gives `(delta_a^T delta_b/n)(h_a^T h_b/n)`.
- Readout derivative: `h_a^(L)/n`. Mobility `n` gives `h_a^T h_b/n`.

These are exactly (V.F.3); no factor of width, input dimension, sample count, or loss gradient is missing.

The elementary operator-norm estimate is sufficient and correctly normalized. A maximal `1/4`-separated sphere family is a net with cardinality at most `9^n`; the packing radii are `1/8` and `9/8`. Approximating both vectors in the bilinear supremum incurs error at most half the operator norm, yielding the factor two. Each net bilinear form has variance `1/n`, so threshold ten reduces to Gaussian threshold five and gives

`P(||W||_op>10) <= 2 exp(n(2 log 9 - 25/2)) -> 0`.

The exponent is negative. A finite union suffices. No estimate for the rectangular first matrix is needed in the backward bound: that matrix is not among the subsequent matrices through which `delta^(1)` is propagated.

The stored-readout calculation is

`E ||W^(L+1)||_2^2 = 1/n`, and `E[||W^(L+1)||_2^2/n] = 1/n^2`.

Thus its RMS is `O_P(n^(-1))`. The bounded derivative and finitely many controlled hidden operator norms propagate this bound to every backward RMS. Feature RMS values are bounded in probability. Every hidden kernel block consequently vanishes, while the readout block tends to `Q_L`. The same RMS pairing proves initial predictions tend to zero. No independence between a backward field and its intervening matrices is needed for these norm inequalities.

This argument is at fixed activation, data, dimension, and finite depth. Its constants are not uniform in growing depth; the proof explicitly says so.

## Gaussian foundations and singular endpoints

**Lines 262–361; equations (V.F.7)–(V.F.11). Verified.**

The normalized probabilists' Hermite convention is correct. Integrating the two generating functions gives `exp(st)`, hence orthonormality with normalization `sqrt(j!)`.

The completeness argument contains its essential steps. At imaginary parameter `i eta`, squared coefficient norms sum to `exp(eta^2)`, giving an `L^2` limit of the Hermite series. Its pointwise entire-function sum identifies that limit, for example by extracting an almost-everywhere convergent subsequence. Pairing with a polynomial-orthogonal function gives a zero Fourier transform for its integrable Gaussian-weighted density. This step does not presume Hermite completeness.

Fourier uniqueness is supplied rather than simply invoked: the Gaussian characteristic function is obtained by integration by parts; its scaled version gives the Gaussian Fourier representation; Fubini then makes every Gaussian convolution of the density zero. The approximate-identity argument uses `L^1` translation continuity, explained through interval step functions and their elementary density. Convolution convergence gives a zero density and completes the proof.

For correlated Gaussian pairs, generating functions give the coefficient identity with factor `rho^j`. Polynomial approximation and Cauchy–Schwarz extend it to `L^2` functions. Absolute convergence follows from the square-summable coefficients. In particular `rho=1` and `rho=-1` are included directly; no nonsingular Gaussian density or limiting conditioning argument is needed at these endpoints.

The integrations by parts in (V.F.10) give coefficients `sqrt(j) a_j` and `sqrt(j(j-1)) a_j` for the first and second derivatives. At-most-linear growth and bounded first two derivatives make the Gaussian boundary terms vanish. Completeness and Parseval then give

`sum j a_j^2 = E f'(xi)^2`,

`sum j(j-1) a_j^2 = E f''(xi)^2`.

These finite sums justify uniform convergence of the differentiated covariance series. The endpoint signs at `rho=-1` are correctly retained; they are not replaced by unsigned moments. Derivatives at both correlation endpoints are correctly one-sided.

For the contraction estimate, every integer `j>=1` and `rho in [-1,1]` satisfy

`1-rho^j = (1-rho) sum_(k=0)^(j-1) rho^k <= j(1-rho)`.

This remains true for negative correlations. Combining it with the first derivative Parseval identity gives (V.F.11), including the factor `sigma^2` introduced by differentiating `phi(sigma x)`. The covariance endpoints are again covered. All activations to which this estimate is applied satisfy its stated regularity.

## Cubic lifting

**Lines 363–400; equations (V.F.12)–(V.F.13). Verified.**

For a unit-diagonal positive semidefinite Gram, unit representatives exist in a finite-dimensional Euclidean space. Absolute separation with `delta>0` makes the denominators `sqrt(1-C_ab^2)` nonzero. The vectors `v_ab` are unit and orthogonal to `v_b`.

The tensor `T_a=v_a tensor v_ab tensor v_ac` is unit, annihilates the other two cubic representatives, and pairs with its own by

`sqrt(1-C_ab^2) sqrt(1-C_ac^2) >= delta(2-delta)`.

No orthogonality among the three testing tensors is claimed or needed. The estimate `sum_a |<T_a,T>|^2 <= 3 ||T||^2` is simply three separate Cauchy–Schwarz bounds. This gives exactly the lower constant `delta^2(2-delta)^2/3`.

The tensor product need not be symmetrized for this argument. All nonnegative integer entrywise powers are positive semidefinite by their tensor Gram representation, with the degree-zero case the all-ones Gram. This supplies the positivity needed when retaining only selected Hermite degrees. Singular original Grams and `delta=1` are legitimate.

## Odd mixture: variance, nonlinear weights, and lower bounds

**Lines 402–611; equations (V.O.1)–(V.O.15). Verified.**

The theorem concerns the literal activation `(1-theta)z+theta arctan(z)`, with `0<theta<=1`. Its sharp two-sided infimum claim has the stated domain `L>=1`, `0<delta<=1/4`, and every `d>=2`. The lower argument is stronger: it applies to every realizable Gram with closed absolute separation and `0<delta<=1`.

The scalar diagonal starts at one and stays strictly positive and below its preceding value. Projection gives the coefficient `c(q)=1-theta+theta mu(q)`, where `mu(q)=E(1+q xi^2)^(-1)`. Jensen gives `c(q)>=1/2` on `0<q<=1`, hence `q/4<=q_+<q`. These inequalities remain valid at `theta=1`.

Writing `u=z-arctan(z)`, the pointwise bounds `0<=u^2<=zu` and integration by parts give

`theta(2-theta) q(1-mu) <= D(q) <= 2 theta q(1-mu)`.

The specified Cauchy–Schwarz calculation gives `E[xi^2/(1+q xi^2)] >= 1/(1+3q)`, since `E xi^4=3`. Consequently

`theta q^2/4 <= D(q) <= 2 theta q^2`,

`theta/4 <= 1/q_+ - 1/q <= 8 theta`.

For the upper reciprocal increment, both the upper decrement and `q_+>=q/4` are needed and supplied. Summing gives the variance sandwich in (V.O.6).

The squared-variance sum in (V.O.7) is also correct. The lower estimate compares a decreasing function's left sum to its integral, giving `L/(1+8 theta L)`. The upper estimate `4/theta` follows by telescoping `D(q_k)>=theta q_k^2/4`; `L` follows from `q_k<=1`. The last interpolation `min(L,4/theta)<=5L/(1+theta L)` holds on both sides of `theta L=4`.

Oddness removes the constant and all even Hermite degrees. Nonnegative weights sum to one, so the normalized correlation map decreases the absolute value of every correlation, including negative ones. Every later Gram retains the initial absolute separation.

The nonlinear residual is at most `(5/3) theta^2 q^3`: testing the linear fit uses `|u(z)|<=|z|^3/3` and `E xi^6=15`. Therefore

`-log w_1 <= (20/3) theta^2 q^2`.

Summing over any finite sequence of layers gives at most `(80/3) theta <= 80/3`. Thus each needed product of linear weights is at least `p_*=exp(-80/3)`. The empty product is one and obeys the same bound.

The cubic coefficient calculation is correct, including its sign and normalization:

`b_3(q) = -sqrt(2/3) q^(3/2) E[xi^2/(1+q xi^2)^2]`.

Under the probability measure with Gaussian density multiplied by `xi^2`, the mean of `xi^2` is three. Jensen then gives the expectation at least `(1+3q)^(-2)>=1/16`. Squaring produces `b_3^2>=q^3/384`, and division by `q_+<=q` gives `w_3>=theta^2 q^2/384`.

Cubic lifting and positivity of all discarded powers yield the matrix recursion

`C_l >= w_1 C_(l-1) + [delta^2(2-delta)^2/3] w_3 I`.

Iterating it only multiplies the injected identity terms by subsequent scalar linear weights; it does not require an unjustified monotonicity of the nonlinear matrix map. Dropping the propagated positive semidefinite input term gives

`lambda_min(C_L) >= p_* delta^2(2-delta)^2 theta^2 L / [1152(1+8 theta L)]`,

and multiplying by the lower bound on `q_L` gives (V.O.15). Finally `delta(2-delta)>=delta` and `1+8x<=8(1+x)` produce exactly the lower constants `exp(-80/3)/9216` and `exp(-80/3)/73728`. Positive definiteness follows for every separated realizable triple, even if its original Gram is singular.

## Odd mixture: composed curvature and the sharp upper bounds

**Lines 613–726; equations (V.O.16)–(V.O.22). Verified.**

Finite composition preserves odd nonnegative power-series coefficients. Rearrangement is justified first on nonnegative correlations, and monotone convergence at one gives coefficient sum one. Absolute convergence and oddness then cover negative correlations. The maps are `C^2` up to the correlation endpoints by the preceding derivative identities and finite composition. Thus the composed second derivative at one also equals its nonnegative second factorial moment; this follows by differentiating inside the open interval and taking the monotone limit to one.

For each layer the endpoint derivatives are

`d_k = q_k E phi'(sqrt(q_k) xi)^2/q_(k+1)`,

`b_k = q_k^2 E phi''(sqrt(q_k) xi)^2/q_(k+1)`.

The explicit second derivative `-2 theta z/(1+z^2)^2` gives `b_k<=16 theta^2 q_k^2`. The series gives `d_k>=1`; for odd degrees at least three, `j-1<=j(j-1)/3`, so `d_k-1<=b_k/3`. Hence `sum b_k<=64` and `sum(d_k-1)<=64/3`.

The chain-rule recurrence is correct:

`A_(k+1)=d_k A_k`,

`B_(k+1)=b_k A_k^2+d_k B_k`.

Dividing the second equation by `A_(k+1)` and telescoping gives precisely `B_L=A_L sum_k (b_k/d_k) A_k`. Since `A_k<=exp(64/3)` and `d_k>=1`, the two factors of `A` account for `exp(128/3)`. Using the variance sum gives

`F_L''(1) <= 80 exp(128/3) theta^2 L/(1+theta L)`.

The planar example is admissible in the theorem's strict domain, not merely on its closure. With `c=1-2 delta` and `r=2c^2-1`, the four required positive margins are

`delta`, `2-3 delta`, `delta(7-8 delta)`, and `2-9 delta+8 delta^2`.

For the last one, the displayed identity `(1-4 delta)(2-2 delta)+delta` proves strict positivity throughout `0<delta<=1/4`, including its upper endpoint. At that endpoint `c=1/2` and `r=-1/2`; both are strictly inside `(-3/4,3/4)`. The construction embeds into every `d>=2` and yields a nonempty admissible set for each theorem parameter choice.

The vector `(1,-2c,1)` annihilates the input Gram and has squared norm `2+4c^2>=3`. Expanding its degree-`j` tensor Gram quadratic form gives exactly

`E_j=2+4c^2+2(2c^2-1)^j-8c^(j+1)`.

For `j=1`, it vanishes identically. For `j>=3`, it and its first derivative vanish at `c=1`. Direct differentiation gives the displayed second derivative, whose four absolute-term bounds sum to `40j^2-16j+8`. The claimed comparison with `54j(j-1)` is correct: their difference is `14j^2-38j-8`, positive at three and increasing for larger integers.

Taylor's integral remainder supplies the factor one-half, yielding `E_j<=27j(j-1)(1-c)^2`. Positivity comes separately from the tensor Gram property. Dividing by the Rayleigh-vector norm gives

`lambda_min(C_L) <= 9(1-c)^2 F_L''(1) = 36 delta^2 F_L''(1)`.

Multiplication by 80 gives the normalized upper constant `2880 exp(128/3)`. The variance upper bound `q_L<=1/(1+theta L/4)<=4/(1+theta L)` gives the absolute upper constant `11520 exp(128/3)`. These are simultaneous comparison bounds in separation, mixture, and depth; the same example witnesses both infimum upper bounds.

## Odd mixture: scalar nonaffinity and depth interpretations

**Lines 728–816; equations (V.O.23)–(V.O.26) and regime table. Verified.**

The cubic coefficient survives affine projection. Its squared lower bound and the earlier tested linear fit give the absolute nonaffinity bounds in (V.O.23). The relative lower bound uses `q_+<=q`; the relative upper bound uses `q_+>=q/4`. Both directions are correct.

At layer `l`, the relevant preactivation variance is `q_(l-1)`, while the relative denominator is `q_l`. This indexing is consistent throughout. Combining the variance sandwich and (V.O.23) gives the stated uniform orders in `theta` and layer number.

For fixed positive `theta`, the variance tends to zero by (V.O.6). Dominated convergence gives `(1-mu(q))/q -> 1`, and the cubic bound on `u` makes its squared expectation `O(q^3)`. Thus `D(q)/q^2 -> 2 theta` and `q_+/q -> 1`. Averaging the reciprocal-variance increments establishes `q_l ~ 1/(2 theta l)`.

The arctangent expansion has a global bound on its remainder, rather than an unjustified Gaussian use of a local power series: integrating the exact rational identity gives a remainder at most `|z|^5/5`. Its Gaussian `L^2` norm is `O(q^(5/2))`. Orthogonal projection is a contraction in `L^2`; removing the affine terms leaves `-q^(3/2) H_3/3` plus the same order of remainder. Since `E H_3^2=6`, this proves the leading constant `2/3` in the arctangent residual.

Absorbing the activation's linear component into the regression slope gives the exact multiplier `theta^2`. Consequently the layerwise equivalents are

`R_phi(q_(l-1)) ~ 1/(12 theta l^3)`,

`R_phi(q_(l-1))/q_l ~ 1/(6 l^2)`.

These equivalents keep `theta` fixed, as the source explicitly states. They are not claimed uniformly in a depth-dependent vanishing mixture.

The normalized sample floor is uniformly positive over `L>=1` for fixed positive mixture and fixed realizable positive separation, using the lower bound on `L/(1+8 theta L)`. The absolute floor cannot remain positive because `lambda_min(Q_L)<=q_L -> 0`. The two regime-table simplifications follow by comparing `1+theta L` with one or with `theta L`, respectively, and retain the theorem's parameter range.

The boundary examples are valid. Antipodal inputs produce opposite features under an odd activation, hence a singular Gram at every layer. At the excluded parameter `theta=0`, the population recursion is exactly `Q_L=G`. The equilateral planar triple has off-diagonal entries `-1/2`, is strictly admissible for `delta<1/2`, and has the all-ones vector in its nullspace. The bias-free linear network statement follows from linearity and the zero sum of its inputs. It is an expressivity observation about that linear reference; the proof does not turn it into a training theorem.

## Literal convex offsets

**Lines 818–966; equations (V.C.1)–(V.C.8). Verified.**

The hypotheses `0<epsilon<1/2`, bounded nonconstant `C^2` shape, and the three norm bounds by one are used correctly. In particular, `b_epsilon=1-2 epsilon` is strictly positive.

The activation mean at every centered Gaussian variance is at least `b_epsilon`. The RMS recurrence satisfies `sigma_(l+1)<=(1-epsilon)sigma_l+1`; the interval with upper endpoint `1/epsilon` is invariant and contains `sigma_1=1`. The mean supplies the positive lower bound. Thus every preactivation standard deviation used by the proof belongs to the compact interval `[b_epsilon,1/epsilon]`, including the first layer. The variance bounds in (V.C.3) have the correct indices.

The derivative belongs to the positive interval `[b_epsilon,1]`. Its squared Gaussian mean is continuous in positive standard deviation. If that mean were one at any such deviation, continuity and Gaussian full support would force the derivative to be identically one. The activation formula would then force `psi'=1`, contradicting boundedness. Compactness therefore gives a single `b_epsilon<=kappa<1`, independent of the input Gram and depth. Merely bounding the derivative pointwise by one would not suffice; the supplied compactness and strictness argument is essential and valid.

Applying (V.F.11) multiplies each preceding squared sample difference by at most `kappa^2`. The initial difference is `2(1-G_ab)`, so iteration gives the first inequality in (V.C.2). The Rayleigh vector `(e_a-e_b)/sqrt(2)` has unit norm and gives half that squared difference, yielding the absolute eigenvalue bound with no missing factor of two. Division by `q_L>=b_epsilon^2` gives the normalized bound.

For the ratio, the all-ones unit direction gives

`lambda_max(Q_L) >= E[(H_1+H_2+H_3)/sqrt(3)]^2 >= 3 b_epsilon^2`.

This uses the uncentered Gram and Jensen, and is valid regardless of correlations. It accounts for the additional factor three in the denominator of the last inequality of (V.C.2). Furthermore `C_L,ab=1-D_L,ab/(2q_L)` tends to one, proving convergence of the entire normalized Gram to the all-ones rank-one matrix. This does not assert convergence of the raw variance to a particular value.

The scalar residual of the shape is positive at each positive Gaussian variance: zero residual would give an affine identity everywhere by continuity and full support; boundedness would make it constant, contrary to hypothesis. The residual formula is continuous in standard deviation with the stated dominating functions. Its compact minimum is positive. Exact absorption of the affine part supplies the factor `epsilon^2`; division by `q_l<=epsilon^(-2)` supplies the further factor `epsilon^2` for relative nonaffinity. Thus the constants in (V.C.7) are correct. They are for the fixed shape and mixture, not uniform over the full shape class or as the mixture vanishes. The scaling observation correctly explains why a shape-independent positive floor cannot follow.

For the explicit shape `arctan(z)/4`, the three norms are `pi/8`, `1/4`, and `3 sqrt(3)/32`. The last value comes from maximizing `x/[2(1+x^2)^2]` at `1/sqrt(3)`. With `epsilon=1/4`, the literal activation is `3(1+z)/4+arctan(z)/16`, with derivative between `3/4` and `13/16`. The stated contraction choice `kappa=13/16` is valid directly from the pointwise Lipschitz bound.

## Calibrated family: exact shape and finite-depth bounds

**Lines 968–1085; equations (V.D.1)–(V.D.9). Verified.**

The shape is fixed before depth is varied. Its coefficient `c_*=exp(3/2)/2` gives `w'(0)=2c_*-1>0`, proving it is nonzero; full Gaussian support gives `v_*>0`. Boundedness of the shape and each of its derivatives is immediate from its finite trigonometric formula and the positive fixed normalization.

Differentiating the supplied Gaussian characteristic function gives `E[xi sin(t xi)]=t exp(-t^2/2)`. The particular coefficient makes `2c_* exp(-2)=exp(-1/2)`. Oddness, this cancellation, and normalization prove all three orthogonality identities in (V.D.3).

For each fixed `L`, the single activation `phi_L` is used at every layer, with `gamma_L=sqrt(tau/L)`. Orthogonality makes its second moment at unit variance exactly one. Starting from unit input diagonals, induction therefore keeps all layer variances exactly one. No approximate variance-calibration argument is substituted for this exact identity.

Both mixed Gaussian terms vanish for every correlation: the representation `Y=rho X+sqrt(1-rho^2) xi'` handles one, and the reversed representation handles the other. At `rho=+/-1`, the independent term is simply zero. The correlation recursion (V.D.4) is thus exact.

The sine-product identity yields `E[sin(aX)sin(bY)]=exp(-(a^2+b^2)/2) sinh(ab rho)`. Substitution gives the displayed numerator and `N_*=exp(1) v_*>0`. For odd `j`, its coefficient numerator is exactly

`1-2^j+4^j/4 = (2^(j-1)-1)^2`.

The degree-one coefficient vanishes; the cubic coefficient is `p_3=9/(6N_*)=3/(2N_*)`. All remaining coefficients are nonnegative and their sum at one is one. Absolute convergence on bounded intervals follows from the explicit hyperbolic-sine expression. Therefore `0<=K(rho)<=rho^3` for nonnegative correlations, and oddness plus the convex-combination form of `T_gamma` gives absolute contraction on the entire correlation interval.

Every iterate remains a unit-diagonal Gram and retains absolute separation. Keeping the cubic coefficient and applying cubic lifting gives `K[C]>=mu_delta I`, with `mu_delta=p_3 delta^2(2-delta)^2/3`. Here positivity of the omitted terms is supplied by tensor powers, not by a claim that an arbitrary scalar map preserves positive semidefiniteness.

The affine matrix recursion with `b=(1+tau/L)^(-1)` gives by induction

`Q_k >= b^k G+(1-b^k) mu_delta I`.

This uses separation at the current iterate at each step; it does not assume nonlinear operator monotonicity. Dropping the first positive semidefinite term at `k=L` and applying the integer binomial inequality `(1+tau/L)^L>=1+tau` gives exactly (V.D.9). The bound is valid for each integer `L>=1`, every fixed `tau>0`, and every realizable separated Gram with `0<delta<=1`. Absolute and variance-normalized floors coincide because the diagonal is exactly one.

## Calibrated family: ODE existence, error estimate, and sequential limit

**Lines 1087–1190; equations (V.D.10)–(V.D.14). Verified.**

The recurrence uses increment coefficient `a_L/(1+a_L)` but is interpolated on the mesh `a_L=tau/L`. The proof explicitly accounts for this difference; it does not silently equate the iteration with ordinary Euler at step `a_L`.

For `F=K-id` on `[-1,1]`, the choices `B=2` and `D=1+max |K'|` are valid uniform bounds. The derivative bound is finite from the explicit entire formula. Clamping the argument to the interval gives a globally bounded, globally `D`-Lipschitz extension. On a time interval with `Dh<1`, the integral map is a contraction on continuous paths; the geometric bound on successive iterates establishes its fixed point and uniqueness. Repeating gives a global extended solution. Since both endpoints are equilibria, uniqueness at endpoint contact keeps the original solution in the correlation interval. This includes solutions starting at either endpoint. The discrete iteration also stays in the interval by its convex-combination form.

The exact-solution local error from freezing `F` is at most `DB a_L^2/2`. The coefficient discrepancy contributes at most `B a_L^2`. Lipschitz propagation contributes the factor `1+D a_L`. Thus the stated recursion

`e_(k+1) <= (1+D a_L)e_k+B(1+D/2)a_L^2`

is correct. Bounding the geometric sum by `L exp(D tau)` gives precisely

`max e_k <= B(1+D/2) tau^2 exp(D tau)/L`.

The intermediate-time comparison adds at most `B tau/L`, which is a valid, nonoptimal bound from the solution's Lipschitz continuity. All constants are uniform over the initial correlation in `[-1,1]`. The claimed uniform convergence of the piecewise-linear interpolation follows.

Applying this argument to the finitely many Gram entries gives `Q(s)`. The discrete matrices are positive semidefinite, their piecewise-linear interpolants are positive semidefinite by convexity, and this property is closed under entrywise convergence in fixed dimension. Diagonal entries stay one, so the limiting matrix is a valid unit-diagonal Gram at every depth coordinate.

The two limits in (V.D.13) have different roles and correct quantifiers. First, for each fixed `L` and its corresponding fixed activation, the empirical Gram converges in probability to its deterministic population Gram. Second, those deterministic population Grams converge as `L` grows to `Q(tau)`. No common random coupling across depths is required for this iterated-limit assertion. The same interpretation applies to the total raw initialized kernel by the already-proved fixed-depth result.

The eigenvalue lower bound follows by passing the matrix lower bound to the limit. The scalar convergence `(1+tau/L)^(-L)->exp(-tau)` follows from the supplied elementary logarithm estimate. This proves the factor `mu_delta(1-exp(-tau))`; it does not provide a finite-width error bound.

For the equilateral witness, oddness and uniqueness make every off-diagonal entry `-r(s)` with `r(0)=1/2`. On the positive interval the inequalities are `-r<=r'<=r^3-r`. The integrating factor for the first excludes a first zero and gives `r>=exp(-s)/2`. The upper inequality makes `r` nonincreasing, hence at most one-half. Therefore `u=r^(-2)` is defined and obeys `u'>=2(u-1)`, giving `u>=1+3 exp(2s)`. The resulting eigenvalues are `1-2r,1+r,1+r`. Consequently (V.D.14) is positive for every `s>0` and zero at the initial endpoint, exactly as required. A scalar multiple of the original singular Gram cannot have the resulting positive smallest eigenvalue.

## Calibrated family: local scalar checks and nonaffinity

**Lines 1192–1270; equations (V.D.15)–(V.D.19). Verified.**

The inequality `0<=1-(1+gamma^2)^(-1/2)<=gamma^2/2` yields all three estimates in (V.D.15) by the triangle inequality and `(1+gamma^2)^(-1/2)<=1`. These bounds hold for every positive `gamma`, though convergence to the identity is asserted only as `L` tends to infinity with `tau` fixed.

The value estimate is weighted globally and implies local uniform convergence. The unweighted global error is indeed infinite for every finite `L`: the coefficient of `z` in `phi_L(z)-z` is nonzero, while the remaining term is bounded. The text correctly avoids replacing weighted or local convergence by uniform convergence on the whole real line.

The shape is orthogonal to both the constant and linear Gaussian directions, so the affine projection removes exactly the normalized linear term. Its residual second moment is `gamma_L^2/(1+gamma_L^2)=tau/(L+tau)`. The total second moment is exactly one, hence the relative and absolute residuals coincide. The assertion holds at every initialized layer because all input variances to the activation are one.

For the variance map, integration by parts gives the cross term `q a(q)`, so the numerator `q+2 gamma q a(q)+gamma^2 b(q)` is correct. The explicit trigonometric expectation is

`a(q)=[2c_* exp(-2q)-exp(-q/2)]/sqrt(v_*)`.

At one, its derivative is `-3 exp(-1/2)/(2 sqrt(v_*))`. Bounded shape and derivative, with the Gaussian factor `|xi|` and `q` restricted to a neighborhood of one, justify differentiating `b(q)` and show continuity of that derivative. It follows that

`V_gamma'(1)=1-[3 exp(-1/2)/sqrt(v_*)] gamma+O(gamma^2)`.

The coefficient of `gamma` is strictly negative. Thus the derivative has absolute value less than one for sufficiently small positive `gamma`; continuity then gives a smaller neighborhood with contraction factor strictly below one. Since one is a fixed point, the mean value theorem makes that neighborhood invariant and yields convergence of its iterates. This establishes the stated local scalar attraction for sufficiently large `L`. It establishes neither a global basin nor stability of accumulated finite-width errors.

Finally, `E chi'=E[xi chi]=0`, and boundedness gives finite `M_2=E chi'^2`. Expansion of the squared derivative gives exactly `(1+gamma_L^2 M_2)/(1+gamma_L^2)`. Dropping its positive denominator and using `(1+x/L)^L<=exp(x)` gives the product bound `exp(tau M_2)`. The proof explicitly limits this to a product of scalar Gaussian moments; it supplies no network-Jacobian norm claim.

## Final comparison and gain remarks

**Lines 1272–1343. Verified within the stated scope.**

Each row of the comparison table follows from its corresponding preceding bounds and keeps its parameters fixed in the stated way. The sharp odd-mixture infima retain `delta<=1/4` and `d>=2` from the theorem. The calibrated bound uses realizability and closed absolute separation up to `delta=1`. The offset assertion requires its fixed nonconstant shape and fixed mixture. The table's rank-one limit concerns the normalized Gram itself, as proved in lines 911–913.

The distinction between a bound uniform in depth and an assertion separately valid at each finite depth is logically correct. In particular, failure of a depth-uniform initialized absolute floor and positivity at each finite depth neither prove nor disprove the trained statements mentioned only as scope distinctions.

For `g(z)=a(1+z)+e psi(z)` with `a>e>0`, the conversion `epsilon=e/(a+e)` is in `(0,1/2)` and the normalized activation has exactly the literal offset form. Its first feature Gram is multiplied by `(a+e)^(-2)`, and its diagonal is positive because its mean is at least `a-e`. Unless `a+e=1`, the first Gram therefore changes.

The general scaled-activation calculation is correct: the second Gram uses `alpha^2 E[phi(alpha Z)phi(alpha Z)^T]` with `Z` having the original first Gram as covariance. The inner argument changes as well as the external factor. For this gain activation, the claimed absence of a nontrivial pointwise homogeneity identity follows from evaluating at zero, where `g(0)>0`, and then taking the positive-infinity slope, which is `a`. This supports the warning against assuming a mere final-kernel rescaling. It does not claim that proportional final Grams are impossible for every specially chosen data set.

For the final growing-variance comparison, affine projection gives exactly `R_g(q)=e^2 R_psi(q)<=e^2`. Gaussian integration by parts gives linear coefficient `sqrt(q)(a+e E psi')`, whose squared value is at least `q(a-e)^2`. Thus iteration from `q_0=1` gives `q_l>=(a-e)^(2l)`. Dividing the residual at input variance `q_(l-1)` by the output variance `q_l` gives the displayed relative bound `e^2/(a-e)^(2l)`. The text does not assert an absolute residual floor for arbitrary shapes; its final qualification is necessary and correct.

The closing limitations accurately describe what was proved: fresh Gaussian initialization, fixed-depth finite-width identification, and a subsequent deterministic depth limit for an explicitly depth-dependent activation. No trained Gaussian recursion, positive-time approximation, interchange of limits, or growing-depth finite-width approximation is used anywhere in the argument.

## Numerical-constant cross-check

| Quantity | Checked derivation |
|---|---|
| Hidden operator-norm threshold `10` | Net factor `2` times Gaussian threshold `5`; tail exponent `-25n/2`, net count `9^(2n)` |
| Variance reciprocal increments | Lower `theta/4`; upper `8 theta` using `q_+>=q/4` |
| Squared-variance sum interpolation | `min(L,4/theta)<=5L/(1+theta L)` |
| Linear-weight product | `(20/3) theta^2 sum q_k^2 <= 80/3`, hence `exp(-80/3)` |
| Cubic squared coefficient | `(2/3)(1/16)^2=1/384` |
| Cubic-injection denominator | `384*3=1152` |
| Normalized odd lower constant | `1152*8=9216` |
| Absolute odd lower constant | `1152*64=73728` |
| One-layer curvature | `q^2 (4 theta^2 q)/(q/4)=16 theta^2 q^2` |
| Total derivative-growth exponent | `sum(d_k-1)<=64/3` |
| Composed curvature | Two derivative factors give `exp(128/3)`; `16*5=80` |
| Planar Taylor estimate | Second-derivative bound `54j(j-1)` times `1/2` gives `27j(j-1)` |
| Planar Rayleigh estimate | Divide by at least `3`, then use `(1-c)^2=4 delta^2`: `27/3*4=36` |
| Normalized odd upper constant | `36*80=2880` |
| Absolute odd upper constant | `4*2880=11520` |
| Odd fixed-mixture residual equivalent | `theta^2(2/3)(2 theta l)^(-3)=1/(12 theta l^3)` |
| Odd relative residual equivalent | Multiply by `2 theta l`: `1/(6l^2)` |
| Offset ratio denominator | All-ones Rayleigh lower bound `3 b_epsilon^2` |
| Offset explicit derivative bound | `3/4+1/16=13/16` |
| Calibrated cubic coefficient | `(2^2-1)^2/(3! N_*)=3/(2N_*)` |
| Calibrated finite-depth floor | Binomial inequality gives `1-b^L>=tau/(1+tau)` |
| Calibrated ODE mesh error | `L a_L^2=tau^2/L`, multiplied by `B(1+D/2) exp(D tau)` |
| Equilateral limiting bound | `r(0)^(-2)=4`, hence `u(s)>=1+3 exp(2s)` |

All displayed comparison constants are sufficient constants. Their large size or smallness is not a defect in the asserted uniform orders; optimal constants are explicitly not claimed.

## Endpoint, quantifier, and self-containment checklist

| Case or possible loophole | Audit result |
|---|---|
| Singular input Gram | Allowed throughout; square-root continuity and tensor arguments do not require invertibility |
| Correlation `rho=+1` or `rho=-1` | Included in the Gaussian series, contraction, and calibrated ODE arguments; derivative signs at `-1` are stated correctly |
| Coincident samples | Offset bounds allow them and give zero pair difference; separated odd/calibrated hypotheses exclude them |
| Antipodal samples | Excluded where an odd-family positive floor is claimed; explicit obstruction is correct |
| Odd parameter `theta=1` | Included; all variance and projection bounds remain valid |
| Odd parameter `theta=0` | Excluded from the positive-floor theorem and separately analyzed correctly |
| Separation `delta=1/4` in sharp upper bound | Planar example is strictly admissible |
| Separation `delta=1` in closed lower bounds | Valid whenever realizable; forces an orthogonal triple, which needs sufficient dimension |
| Dimension `d=2` | Planar construction proves nonemptiness of the sharp theorem's strict class |
| Depth `L=1` | All products, recursions, and inequalities apply; hidden-matrix products may be empty |
| Very small positive mixture | Uniform comparison bounds remain valid; fixed-mixture asymptotic equivalents are not promoted to uniform equivalents |
| Offset endpoints `epsilon=0,1/2` | Properly excluded; the proof uses strict positivity of `b_epsilon` and a nonzero mixture |
| Offset constant shape | Properly excluded for the nonaffinity floor |
| Calibrated `tau` | Fixed and strictly positive; no uniformity over all `tau` is claimed for the ODE error constants |
| Calibrated activation within one network | Same `phi_L` at all its layers; no unintended layer-dependent recursion |
| Local scalar variance attraction | Only for sufficiently large `L` and a sufficiently small neighborhood of variance one |
| Width and depth | Width tends to infinity first with finite depth and activation fixed; the later depth limit is deterministic |
| Elementary Gaussian and ODE ingredients | Derived in the supplied text, including completeness, Fourier uniqueness, derivative sums, matrix norm bound, and existence/error proof |
| References to other parts | No calculation or theorem in this audit requires their contents |
| Training and Jacobian conclusions | Explicitly outside the proved results and not inferred by this audit |

The potentially substantive proof dependencies are all present: conditional Gaussian averaging and covariance continuity; Hermite orthogonality and completeness; the covariance and derivative series with endpoints; Gaussian contraction; cubic lifting; composed-map curvature control; and a direct ODE existence and discretization-error proof. Ordinary integration, elementary function-space completeness, and finite-dimensional spectral facts are the background toolkit, not missing specialized results.

## Required corrections

**None. CLEAN.**

The supplied initialization proof supports its stated conclusions at the supplied constants and within the quantified parameter ranges. This verdict includes the supporting lemmas and endpoint handling, while preserving all explicit restrictions on training and on the order of width and depth limits.
