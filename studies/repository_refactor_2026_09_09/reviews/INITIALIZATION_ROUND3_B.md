# Isolated adversarial review of Part V

## Verdict

**CORRECTION REQUIRED — one minor literal-quantifier defect in the final gain discussion.**

The sentence at PROOF.md:1298 universally says that dividing the gain activation by `a+e` changes the recursion, although the stated assumptions `a>e>0` permit `a+e=1`. In that case the division is the identity. The precise correction and an admissible counterexample are below.

I found no mathematical defect in Theorem V.O.1, Theorem V.C.1, the calibrated finite-depth bounds or sequential limit, their constants, or the final relative-nonaffinity estimate under `a-e>1`. The required correction is confined to a literal statement in the comparison prose. It does not invalidate those results.

## Inputs, isolation, and complete read coverage

Only these two input sources were read:

| Input | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `/tmp/pde-initialization-round3.zWfKUzam/PROOF.md` | 48406 | 1337 | `6d05666ef6101778febf2e95a73906672eb67dfdfd0a60e58693e6fc3749db45` |
| `/tmp/pde-initialization-round3.zWfKUzam/NOTATION.md` | 5110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

PROOF.md was read through EOF with complete line coverage 1–340, 341–675, 676–1010, and 1011–1337. An aggregate tool response truncated part of the middle interval; the complete 676–1010 interval was then explicitly retrieved again and read without truncation. NOTATION.md was read in full, lines 1–98 through EOF. No omitted passage was inferred from a heading or summary.

No project, study, history, earlier review, skill source, network source, or agent was consulted. No numerical experiment, symbolic-algebra program, simulation, or other research computation was run. Tools were used only to obtain the two inputs and their line/byte counts and hashes, create a fresh private temporary directory, and write this report. All mathematical checking was by direct reasoning. The inputs were not edited.

The output directory `/tmp/pde-part-v-private-review.46cXkaWV` was freshly created by `mktemp -d`, rather than selected from an existing review directory.

Post-write verification reproduced both input SHA-256 hashes exactly as listed above. Filesystem metadata confirmed that the new output directory has mode `0700`, so the report is inside a private directory.

All line references below refer to these exact input bytes. NOTATION.md was used as the notation/model contract, not as a license to import results from other parts of the library.

## Required correction R1: the identity normalization is allowed

**Location:** PROOF.md:1294–1305, especially line 1298.

**Statement:** Under `a>e>0`, put `epsilon=e/(a+e)` and divide `g(z)=a(1+z)+e psi(z)` by `a+e`. The text then says, “This division changes the recursion under the fixed matrix initialization.”

**Counterexample satisfying every stated hypothesis:** Take

\[
a=\frac34,\qquad e=\frac14,\qquad \psi(z)=\frac14\arctan z.
\]

The shape is bounded, nonconstant, and C², with the three required norms `pi/8`, `1/4`, and `3 sqrt(3)/32`, as independently verified in the audit of V.C.8 below. Here `a>e>0` but `a+e=1`, and

\[
g(z)=\frac34(1+z)+\frac1{16}\arctan z,
\qquad \frac{g}{a+e}=g.
\]

Consequently the activation, every population recursion step, and every finite-width network remain identical. This is an exact exception, not an asymptotic one.

**Minimal required replacement for the sentence at line 1298:**

> If \(a+e\ne1\), this division changes the recursion under the fixed matrix initialization; if \(a+e=1\), it leaves the activation and recursion unchanged.

Alternatively, changing the original claim to “This division changes the recursion in general” removes the universal assertion. The displayed scaling formulas already handle the identity case correctly. The subsequent explanation about the lack of a general homogeneity reduction can remain; its purpose is a general comparison, not a claim that the identity scaling is nontrivial.

**Severity and effect:** Minor, local correction to a literal quantifier. There is no required change to a theorem, constant, rate, witness, or limiting argument. In particular, the later assumption `a-e>1` implies `a+e>1`, so this exception does not affect the final exponentially decaying relative-nonaffinity bound.

## 1. Model, observables, and notation: lines 1–143

The initialization-only scope in the preamble is respected by the proved limit statements. The discussion of possible trained theorems is expressly nonassertive; the linear representational obstruction later in the text is elementary algebra and requires no training result.

V.M.1–V.M.5 agree with NOTATION.md: `L` is hidden depth, the first preactivation is `W x/sqrt(d)`, hidden matrices have entry variance `1/n`, the stored readout has entry variance `n^-2`, and the predictor has its separate factor `1/n`. Singular realizable input Grams are expressly allowed. All subsequent Gaussian arguments either admit singular covariance directly or explicitly handle its endpoints.

The storage change is correct: `W^(1)=sqrt(d) V^(1)` implies that the first metric term becomes `d ||dV^(1)||_F²/n`. The inverse metric multiplies first-layer and readout derivative pairings by `n`, and middle-layer pairings by one. The factor `2/3` belongs to the specified squared-loss derivative and is correctly excluded from the predictor-gradient kernel.

The common population diagonal follows by induction because every sample starts at variance one and uses the same scalar activation. `Q_l` is consistently the uncentered feature second-moment matrix. Fresh centered independent next-layer weights make this uncentered matrix the covariance of the next Gaussian preactivation, including in the offset case. No centered-feature covariance is substituted for it.

For V.M.6–V.M.7, `C_l` is PSD with diagonal one and trace three. Its largest eigenvalue lies in `[1,3]`; dividing its smallest eigenvalue by that largest eigenvalue gives exactly the two claimed factor-three inequalities. These require only `q_l>0`, which is established for each family. The reciprocal spectral condition number is not confused with the absolute floor.

For V.M.8–V.M.9, `1` and `xi` are orthonormal in Gaussian L², and `span{1,sqrt(q) xi}=span{1,xi}` for `q>0`. Orthogonal projection therefore gives the displayed attained residual formula. At-most-linear growth ensures square integrability. All three stated activations have positive second moment at every positive variance, so their relative residual is defined. The later layerwise denominators are consistently `q_l`, with preactivation variance `q_(l-1)`.

## 2. Finite-width initialization and kernel: lines 144–260

**V.F.1, forward induction.** At the first layer, row triples are independent Gaussians with covariance `G`; singular `G` does not affect independence across rows. Linear growth gives finite fourth moments of activated coordinates and hence finite variance of each product. Chebyshev applies to each empirical product.

Conditionally on preceding features, the next independent Gaussian weight rows give independent centered triples with covariance exactly V.F.1. If preceding diagonal entries are bounded by `M`, Cauchy–Schwarz and Gaussian fourth moments bound each product's conditional second moment by a constant depending only on `M` and the fixed activation. The conditional Chebyshev bound is thus uniform on that event. By the preceding induction step, choosing `M` strictly above the deterministic limiting diagonals makes its complement have probability tending to zero.

The supplied square-root argument proves covariance continuity even at singular PSD matrices: bounded sequences of PSD roots have subsequential limits, each squares to the target covariance, and the unique PSD square root is given by finite-dimensional spectral decomposition. Coupling through a common standard Gaussian then gives L² convergence of activated coordinates by Lipschitzness. Cauchy–Schwarz gives convergence of expected products. Applying this continuous map to the preceding empirical covariance finishes the induction. Finite numbers of entries and layers give joint convergence in probability.

**V.F.2–V.F.3, exact kernel factors.** The backward fields are `n` times the predictor derivative with respect to preactivation, consistent with NOTATION.md. The first derivative is `delta_a u_a^T/n`; its metric pairing is `G_ab delta_a^T delta_b/n`. The middle pairing is `(delta_a^T delta_b/n)(h_a^T h_b/n)`. The readout pairing is `h_a^T h_b/n`. Thus there is no missing width, dimension, readout, or loss factor in V.F.3.

**V.F.4–V.F.5, norm estimates.** A maximal `1/4`-separated sphere family is a net. Its disjoint radius-`1/8` balls fit inside a radius-`9/8` ball, giving cardinality at most `9^n`. Approximating the two unit vectors in a bilinear supremum incurs at most `||W||_op/2`, giving the factor two. For deterministic unit net vectors, `u^T Wv` has variance `1/n`. The Gaussian two-sided tail at five is `2 exp(-25n/2)`, and the union over net pairs gives exactly V.F.4. Its exponent decays. Only the square hidden matrices are needed in the backward product; no unproved norm bound on the rectangular first matrix is used.

The readout satisfies `E ||W^(L+1)||²/n=n^-2`; Markov yields `||W^(L+1)||/sqrt(n)=O_P(n^-1)`. With fixed depth, the finitely many matrix norm factors and bounded activation derivatives give V.F.5. Independence between backward fields and those matrices is unnecessary for this deterministic product inequality.

**V.F.6 and the final remarks.** Hidden-block entries are `O_P(n^-2)` times bounded feature pairings, and vanish. The readout block tends to `Q_L`. The same readout and feature norm estimates make `f_(n,a)` tend to zero. The remark about zero initialized population backward fields is consistent with zero limiting readout; it is not used to construct joint trained population operators. Every argument holds with activation, data, and finite depth fixed. None supplies an estimate uniform in growing depth.

## 3. Gaussian and Hermite foundations: lines 262–361

**V.F.7 and completeness.** The Gaussian product generating function is `exp(st)`, so coefficient comparison gives the stated normalization. Gaussian exponential moments justify coefficient comparison in a bounded neighborhood of the parameters.

The completeness argument is not an appeal to an unprovided Hermite theorem. At `t=i eta`, the squared L² norms of the generating-series terms sum to `exp(eta²)`, so its partial sums converge in L². Their pointwise generating-function limit identifies the L² limit (equivalently, take an almost-everywhere convergent subsequence). Orthogonality to every polynomial therefore forces the Fourier transform of `u` times the Gaussian density to vanish. Cauchy–Schwarz gives its L¹ integrability.

The Fourier uniqueness step is supplied in the file: Gaussian integration by parts gives the characteristic function; rescaling gives the Gaussian Fourier integral; Fubini is justified by the displayed absolutely integrable bound; convolution is zero; and Gaussian convolution tends to the original density in L¹ by translation continuity and concentration of the Gaussian near zero. Density of finite interval step functions and the corresponding translation-continuity argument are elementary L¹ facts. No Fourier inversion theorem or nontrivial Gaussian basis result is imported.

**V.F.8–V.F.9, correlations and endpoints.** The joint generating identity is valid for any centered Gaussian pair of unit variances, including `Y=X` and `Y=-X`. Polynomial approximation extends the covariance formula by Cauchy–Schwarz without any nondegeneracy assumption. Parseval supplies `sum a_j²<infinity`, which makes the covariance series absolutely convergent at both endpoints.

**V.F.10, derivative identities.** Gaussian integration by parts against Hermite polynomials gives `sqrt(j) a_j` and `sqrt(j(j-1)) a_j`. The stipulated linear growth and bounded first two derivatives kill all boundary terms and put both derivatives in Gaussian L². Completeness and Parseval identify both weighted square sums. Consequently both differentiated covariance series converge uniformly on `[-1,1]`. The signs at `rho=-1` are correctly `(-1)^(j-1)` and `(-1)^(j-2)`; the file does not replace them with the unsigned values at `+1`. Endpoint derivatives are correctly one-sided.

**V.F.11, contraction.** For every `rho` in `[-1,1]`,

\[
1-\rho^j=(1-\rho)\sum_{k=0}^{j-1}\rho^k\le j(1-\rho).
\]

This remains true for negative correlations: each summand is at most one, and `1-rho` is nonnegative. Applying V.F.9 and the first derivative Parseval identity to `f(x)=phi(sigma x)` gives exactly the factor `sigma² E phi'(sigma xi)²`. The squared preactivation difference is `2 sigma²(1-rho)`. Both singular endpoints are therefore covered with the displayed constant, with no missing restriction to nonnegative correlation.

## 4. Cubic tensor floor: lines 363–400

For V.F.12–V.F.13, absolute separation ensures that every denominator `sqrt(1-C_ab²)` is positive, including when the original Gram is singular. Each `v_ab` has norm one and is orthogonal to `v_b`; its inner product with `v_a` is `sqrt(1-C_ab²)`.

The ordinary, not necessarily symmetric, unit tensor `T_a` is orthogonal to each of the other two cubic feature tensors by its corresponding factor. Its pairing with its own cubic feature is at least `delta(2-delta)`. Hence for any real coefficient vector,

\[
s_\delta^2\sum_a b_a^2
\le\sum_a|\langle T_a,\sum_b b_bv_b^{\otimes3}\rangle|^2
\le3\left\|\sum_b b_bv_b^{\otimes3}\right\|^2.
\]

This proves the claimed `s_delta²/3` matrix floor without requiring the three inputs to be linearly independent. The ambient tensor construction is legitimate even though the cubic feature tensors themselves are symmetric. The endpoint `delta=1` is also valid: the off-diagonal entries must be zero. Every other nonnegative integer entrywise power is PSD by the same Gram construction; degree zero is explicitly the all-ones Gram. No external Schur-product result is needed.

## 5. Literal odd mixture: lines 402–816

### 5.1 Variance and summable weights, V.O.1–V.O.11

The assumptions throughout this section are `0<theta<=1`, with integer hidden depth and realizable triples; the two-sided sharp theorem further has `0<delta<=1/4` and `d>=2`. The strict admissible set is nonempty throughout that theorem's range by the explicit witness checked below.

Gaussian integration by parts gives `E[Z arctan Z]=q mu(q)`, so `c(q)` is precisely the linear regression coefficient. Jensen gives `mu(q)>=1/(1+q)`, whence `c(q)>=1/2` on `0<q<=1` and `q_+>=q/4`. The strict pointwise inequality `0<|phi_theta(z)|<|z|` for nonzero `z` proves `0<q_+<q`. Iteration therefore remains inside the stated variance domain.

For `u=z-arctan z`, `0<=u²<=zu`. Thus

\[
\theta(2-\theta)q(1-\mu)\le q-q_+\le2\theta q(1-\mu).
\]

The specified Cauchy–Schwarz factors have pairing `E xi²=1`, while the second squared norm is `1+3q`. They give `E[xi²/(1+q xi²)]>=1/(1+3q)`. Combining this with the upper bound by `E xi²=1` yields V.O.5. In particular division by `q q_+`, using `q/4<=q_+<=q`, gives exactly the reciprocal-increment interval `[theta/4,8 theta]`. Summation proves V.O.6.

For V.O.7 the lower sum is the left-endpoint sum of the decreasing function `(1+8 theta x)^-2`, whose integral is `L/(1+8 theta L)`. The upper bound `4/theta` follows by telescoping the lower decrement `theta q_k²/4`; the other upper bound is `L`. The final comparison `min(1,4/x)<=5/(1+x)` is valid on both sides of `x=4`, including equality there.

The Hermite coefficients in V.O.8 are nonnegative squares, have total weight one, and have only odd indices. This proves `|K_q(rho)|<=|rho|`, so absolute separation survives at every layer, including negative input correlations. All matrix power series used below converge entrywise and preserve PSD by the tensor argument and closure of the PSD cone.

The residual after affine projection is `R(q)=q_+-q c(q)²`. Testing the fit `z` gives `R<=theta² E u(Z)²<=(5/3)theta² q³`, using `|u(z)|<=|z|³/3` and `E xi^6=15`. Since `q c²>=q/4`,

\[
-\log w_1=\log\left(1+\frac{R}{qc^2}\right)
\le\frac{20}{3}\theta^2q^2.
\]

The sum of `theta² q_k²` over any finite selection of layers is at most `4 theta<=4`. Thus every consecutive product, including the empty product needed at the last injection, is at least `p_*=exp(-80/3)`. There is no assumption of a fixed variance in this product estimate.

### 5.2 Cubic coefficient and lower constants, V.O.12–V.O.15

The first integration by parts replaces `H_3` with `sqrt(q) H_2/(1+q xi²)`. The identity `E[(xi²-1)r(xi)]=E[xi r'(xi)]`, with `r=(1+q x²)^-1`, then gives

\[
b_3(q)=-\sqrt{2/3}\,q^{3/2}
E\frac{\xi^2}{(1+q\xi^2)^2}.
\]

The coefficient's sign and normalization are both correct. Under the probability measure with density `xi²`, the mean of `xi²` is three. Jensen therefore gives the expectation lower bound `(1+3q)^-2>=1/16`. Squaring produces `b_3²>=q³/384`, and division by `q_+<=q` gives `w_3>=theta² q²/384`.

The matrix inequality preceding V.O.14 retains the degree-one Gram and degree-three floor and discards only PSD terms. Applying it at each actual separated Gram and iterating a linear matrix comparison is valid; it does not assume entrywise nonlinear maps are monotone in Loewner order. Each scalar injection receives a subsequent linear-weight product at least `p_*`. This gives the factor `1/(3*384)=1/1152` in V.O.14. Multiplication by the lower variance gives V.O.15.

These lower bounds hold on the larger weakly separated domain `|G_ab|<=1-delta`, `0<delta<=1`, and so also on the strict theorem domain. Using `s_delta>=delta` and `1+8 theta L<=8(1+theta L)` yields exactly

\[
\frac{e^{-80/3}}{9216}
\frac{\delta^2\theta^2L}{1+\theta L},\qquad
\frac{e^{-80/3}}{73728}
\frac{\delta^2\theta^2L}{(1+\theta L)^2}.
\]

No assumption of invertibility of the original input Gram enters either bound.

### 5.3 Composition and strict planar upper witness, V.O.16–V.O.22

Composition preserves an odd power series with nonnegative coefficients. Rearrangement for `0<=rho<1` uses nonnegative terms; continuity and monotone convergence at one make the coefficient sum one. Oddness and absolute convergence then give the formula on the negative half-interval as well.

V.F.10 gives the exact first and second endpoint derivatives in V.O.17. The bound `|phi_theta''(z)|<=2 theta |z|`, together with `q_(k+1)>=q_k/4`, yields `b_k<=16 theta² q_k²`. The odd-degree inequality `(j-1)<=j(j-1)/3` for `j>=3` proves `1<=d_k` and `d_k-1<=b_k/3`. Thus `sum b_k<=64` and `sum(d_k-1)<=64/3`.

The continuous one-sided chain rule is applicable at one. Dividing the second-derivative recursion by `A_(k+1)=d_k A_k` gives

\[
B_L=A_L\sum_{k=0}^{L-1}\frac{b_k}{d_k}A_k.
\]

Each `A_k<=exp(64/3)` and `d_k>=1`, hence

\[
F_L''(1)\le16e^{128/3}\theta^2\sum q_k^2
\le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]

For the composed series, `sum j(j-1)p_(j,L)=F_L''(1)`: inside `(0,1)` one can differentiate the power series; then nonnegativity and continuity of the already established second derivative give this identity at one by monotone convergence. Thus the curvature bound legitimately controls the later tensor-degree sum.

For the witness, `c=1-2 delta` belongs to `[1/2,1)` and `r=2c²-1`. The four strict margins are

\[
\delta,\quad 2-3\delta,\quad
\delta(7-8\delta),\quad
(1-4\delta)(2-2\delta)+\delta.
\]

All are strictly positive throughout `0<delta<=1/4`, including the final endpoint. Thus the example itself is admissible; no limit from a forbidden boundary is used. It embeds into every `d>=2`.

The vector `(1,-2c,1)` lies in the input Gram's nullspace and has squared norm `2+4c²>=3`. Its degree-`j` quadratic form is the displayed `E_j(c)`, nonnegative by the tensor Gram identity. Direct differentiation verifies the displayed formula for `E_j''`. On `[1/2,1]`, the triangle bound is

\[
8+8j+32j(j-1)+8j(j+1)=40j^2-16j+8.
\]

This is at most `54j(j-1)` for every integer `j>=3`: the difference is `14j²-38j-8`, positive at three and increasing thereafter. The two vanishing conditions at `c=1` give the Taylor bound `E_j(c)<=27j(j-1)(1-c)²`. The degree-one term is exactly zero.

Dividing by the Rayleigh-vector squared norm gives the factor nine, and `(1-c)²=4 delta²` gives

\[
\lambda_{\min}(C_L)\le36\delta^2 F_L''(1).
\]

The normalized upper constant is therefore `36*80=2880` times `exp(128/3)`. Multiplication by `q_L<=4/(1+theta L)` gives the absolute upper constant `11520 exp(128/3)`. The same admissible witness proves both upper bounds for every allowed triple of parameters `(delta,theta,L)`. Along with the lower bounds, this verifies the claimed sharp joint orders, not merely separate one-parameter asymptotics.

### 5.4 Scalar nonaffinity, asymptotics, and exclusions, V.O.23–V.O.26

The degree-three coefficient survives affine projection, giving the lower residual in V.O.23; testing the linear fit gives the upper residual. Division by `q/4<=q_+<=q` gives the two relative constants as printed. Combining with V.O.6 gives the uniform layer orders with preactivation index `l-1`.

For fixed allowed `theta>0`, dominated convergence gives `(1-mu(q))/q -> 1`. The `u²` term is `O(q³)`, so the decrement divided by `q²` tends to `2 theta`, while `q_+/q -> 1`. Since V.O.6 already forces `q_l -> 0`, averaging the reciprocal increments proves `q_l~1/(2 theta l)`.

The integrated rational identity gives the global fifth-order remainder bound for arctangent, including negative arguments. In Gaussian L² its remainder is `O(q^(5/2))`; orthogonal projection cannot increase that norm. Removing the affine part of the cubic term leaves `-q^(3/2) H_3/3`. Its squared norm is `(2/3)q³`, with a smaller-order error. Multiplication of the residual by `theta²` is exact because the added linear part is absorbed by projection. Substitution yields exactly `1/(12 theta l³)` for absolute nonaffinity and `1/(6 l²)` for relative nonaffinity.

The positive normalized floor uniform in depth follows directly from `L/(1+8 theta L)>=1/(1+8 theta)` for integer `L>=1`. The absolute floor cannot persist because `lambda_min(Q_L)<=q_L -> 0`. The two regime rows follow from bounding `1+theta L` between one and two for `theta L<=1`, or between `theta L` and `2 theta L` for `theta L>=1`; their constants are universal in the stated theorem domain. The fixed-theta asymptotic equivalents are not claimed uniformly as theta tends to zero.

Antipodal input pairs have opposite features for every layer under the odd activation, so their Gram is singular. At `theta=0`, the recursion is the identity on `G`. The equilateral planar Gram is strictly admissible exactly as claimed for `0<delta<1/2`, and its all-ones null vector follows from the zero sum of its inputs. Any bias-free linear predictor has zero sum on those inputs and cannot match `(1,1,1)`. No conclusion about positive-mixture training is inferred from this algebraic obstruction.

## 6. Literal convex offsets: lines 818–966

**Hypotheses and V.C.1–V.C.3.** Both strict restrictions `0<epsilon<1/2` and nonconstancy of the bounded C² shape matter. The three norm bounds give `b_epsilon<=phi_epsilon'<=1`, with `b_epsilon=1-2 epsilon>0`. The mean is at least `b_epsilon` at every centered Gaussian variance. Minkowski gives

\[
\|\phi_\varepsilon(\sigma\xi)\|_2
\le(1-\varepsilon)\sigma+(1-\varepsilon)+\varepsilon
=(1-\varepsilon)\sigma+1.
\]

Thus `[0,1/epsilon]` is invariant under the upper recursion and contains `sigma_1=1`. The mean lower bound gives the lower RMS bound after each step; the initial value also satisfies it. Consequently every preactivation RMS lies in the compact positive interval `[b_epsilon,1/epsilon]`, and every feature second moment lies in `[b_epsilon²,epsilon^-2]`. The first layer is included in the argument; no `q_0` exception is overlooked.

**V.C.4, strict averaged contraction.** Dominated convergence makes the Gaussian derivative-square expectation continuous in positive sigma. Its pointwise upper bound is one. If its expectation equaled one, positivity of the derivative would imply `phi'=1` almost surely; continuity and the Gaussian's positive density extend this to all real arguments. This would require `psi'=1` everywhere, incompatible with boundedness. Every expectation in the compact interval is therefore strictly less than one, and its attained maximum remains strictly below one. The positive square root satisfies `b_epsilon<=kappa<1`. Compactness away from zero, established before this step, is essential and is supplied. The constant depends only on the fixed shape and epsilon, not on the Gram or depth.

**V.C.2, all four inequalities.** Equal sample variances make the preactivation squared difference exactly the previous feature squared difference, with `D_(0,ab)=2(1-G_ab)`. V.F.11 applies also to negative correlations and singular covariance endpoints, so iteration gives `D_(L,ab)<=2(1-G_ab) kappa^(2L)` for every normalized realizable triple, without a separation assumption.

The unit vector `(e_a-e_b)/sqrt(2)` has quadratic form `D_(L,ab)/2`, verifying the second inequality's factor. Dividing by `q_L>=b_epsilon²` gives the third. For the fourth, the unit all-ones vector has quadratic form at least the square of the sum of the feature means divided by three, which is `3 b_epsilon²`. Hence the denominator in the reciprocal-condition-number estimate is exactly `3 b_epsilon²`, as printed. This bound is stronger than simply using `lambda_max(Q_L)>=q_L` and is justified by the offset means.

The formula `C_(L,ab)=1-D_(L,ab)/(2q_L)` then gives entrywise convergence to the all-ones matrix. The argument establishes rank-one collapse of the normalized Gram with scale bounded away from zero. It does not assume convergence of the scalar variance itself or require a centered-covariance interpretation. Duplicate samples, which make the pair bound zero, present no exception: they indeed force a zero Gram eigenvalue.

**V.C.6–V.C.7, persistent scalar nonaffinity.** For every positive sigma, zero affine residual for the continuous shape would make it affine everywhere by Gaussian full support. Boundedness would make that affine function constant, contrary to the hypothesis. The projection formula is continuous in sigma: boundedness dominates the second moment and mean, and `||psi||_infinity |xi|` dominates the linear pairing. Its minimum over the same compact positive interval is therefore strictly positive.

The affine term in the activation can be absorbed exactly by regression, leaving `epsilon² R_psi(q)`. The absolute floor is `epsilon² r_(epsilon,psi)`. Since the relative denominator is at most `epsilon^-2`, its floor is `epsilon^4 r_(epsilon,psi)`. Both statements are uniform over layers, including layer one, for the fixed shape and mixture only. The file correctly declines uniformity over shapes: multiplying an allowed nonconstant shape by a small positive constant keeps it allowed and scales its residual by the square of that constant. Nor can a positive bound hold uniformly as epsilon tends to zero, since `R_phi<=epsilon²`.

**V.C.8, explicit constants.** For `psi=arctan/4`, the supremum norms are

\[
\|\psi\|_\infty=\frac\pi8,\qquad
\|\psi'\|_\infty=\frac14,\qquad
\|\psi''\|_\infty=\max_{x\ge0}\frac{x}{2(1+x^2)^2}
=\frac{3\sqrt3}{32}.
\]

Differentiating the last expression locates the maximum at `x=1/sqrt(3)`. Each norm is below one. With `epsilon=1/4`, the activation and derivative interval are exactly those printed. The pointwise Lipschitz constant `13/16` gives all four V.C.2 bounds using the already established variance and mean bounds. It is permissible to use this upper contraction constant even if the averaged constant defined in V.C.4 is smaller.

## 7. Calibrated family: lines 968–1270

### 7.1 Shape, cancellation, and finite-depth geometry, V.D.1–V.D.9

The calibrated family is clearly distinguished from both fixed literal mixtures. For each fixed total depth, one common activation is used in all layers. Its depth subscript is not a layer-dependent-activation index. Since `w'(0)=e^(3/2)-1>0`, the smooth bounded odd shape is nonzero, and Gaussian full support gives `v_*>0`. Dividing by its square root is legitimate. All derivatives of this fixed trigonometric shape are bounded; none is incorrectly required to satisfy V.C's unit norm restrictions.

Differentiating the contained Gaussian characteristic function is justified by the integrable factor `|xi|`, and gives `E[xi sin(t xi)]=t exp(-t²/2)`. The choice `2c_* exp(-2)=exp(-1/2)` then gives exactly `E chi=0`, `E xi chi=0`, and `E chi²=1`. It follows that `E phi_L(xi)²=1`, so induction from `q_0=1` fixes every variance at one.

For a correlated standard Gaussian pair, representing `Y=rho X+sqrt(1-rho²) xi'` makes `E[Y chi(X)]` zero by the two orthogonalities and independence; the swapped cross term is also zero. This representation remains valid when `rho=+1` or `rho=-1`. Thus V.D.4 has the exact coefficient `gamma²`, rather than an unaccounted first-order term in gamma.

The sine-product identity follows from the difference of the two Gaussian cosine expectations. Before normalization, the covariance of `w` is

\[
e^{-1}\left(\sinh\rho-\sinh(2\rho)+\frac14\sinh(4\rho)\right).
\]

At one this equals `v_*`, so `N_*=e v_*>0`. At every odd degree the coefficient numerator is

\[
1-2^j+\frac{4^j}{4}=(2^{j-1}-1)^2.
\]

The degree-one term vanishes; the degree-three coefficient is `9/(6N_*)=3/(2N_*)`; all remaining coefficients are positive; and their sum is one. The trigonometric covariance series is absolutely convergent on bounded intervals, so no endpoint summability issue remains. For `0<=rho<=1`, every power has degree at least three, giving `0<=K(rho)<=rho³`. Oddness supplies the corresponding absolute-value bounds on negative correlations and hence the separation-preserving bound for `T_gamma`.

For any realizable weakly separated triple, V.F.3 applied to the actual unit-diagonal Gram gives

\[
K[C]\succeq p_3 C^{\circ3}\succeq
\frac{p_3\delta^2(2-\delta)^2}{3}I.
\]

With `b=(1+tau/L)^-1`, the exact recursion is a convex combination of `Q_k` and `K[Q_k]`. Induction therefore yields `Q_k >= b^k G+(1-b^k) mu_delta I` in Loewner order. This again uses a scalar linear comparison and does not presume Loewner monotonicity of `K`.

At `k=L`, discarding only the PSD term `b^L G` gives V.D.9. The binomial inequality `(1+tau/L)^L>=1+tau` is valid for every integer `L>=1` and every positive tau, giving the exact finite-depth uniform lower factor `tau/(1+tau)`. The bound allows singular `G` and the endpoint `delta=1` whenever the triple is realizable in the input dimension. If no such triple exists in a given dimension, the explicitly stated realizability hypothesis prevents a false existence claim. Absolute and variance-normalized eigenvalue floors coincide because `q_L=1`.

### 7.2 Sequential limit and error, V.D.10–V.D.13

The exact population step is `a_L/(1+a_L) F(rho)`, where `a_L=tau/L` and `F=K-id`. The interpolation mesh is `a_L`, not `a_L/(1+a_L)`. The proof correctly treats their difference as an error and does not silently substitute a different depth coordinate.

On `[-1,1]`, `|F|<=2=B` and `F` is `D`-Lipschitz with `D=1+max|K'|`. The displayed entire formula for `K` makes this finite. Clipping the input to `[-1,1]` preserves both properties globally. The supplied contraction iteration on continuous paths is complete: on an interval with `Dh<1`, successive differences sum geometrically, the uniform limit exists by completeness, continuity gives a fixed point, and the same contraction estimate gives uniqueness. Concatenation gives the extended solution for every finite depth coordinate. Because `F(+1)=F(-1)=0`, uniqueness at the first endpoint contact prevents crossing. The original scalar solution remains in the correlation interval. Each discrete step does too, as a convex combination of two points in that interval.

The exact solution increment differs from `a_L F(x)` by at most `DB a_L²/2`, since the solution is `B`-Lipschitz in the depth coordinate. Also

\[
0\le a_L-\frac{a_L}{1+a_L}=\frac{a_L^2}{1+a_L}\le a_L^2.
\]

Subtracting increments gives the displayed recursion

\[
e_{k+1}\le(1+D a_L)e_k+B(1+D/2)a_L^2.
\]

Summing at most `L` terms, bounding their growth by `exp(D tau)`, and using `L a_L²=tau²/L` gives exactly V.D.12. There is no missing factor of `D` or tau in this sufficient bound. Interpolating endpoint errors and using the solution's Lipschitz bound adds at most `B tau/L`; in fact a smaller bound is possible, so the printed one is valid. All constants are uniform over the initial correlation, including both endpoints.

Applying the scalar result to the finitely many matrix entries produces a unit-diagonal matrix path. Every approximating interpolated matrix is a convex combination of PSD population Grams. The entrywise limit is PSD because each of its quadratic forms is a limit of nonnegative quadratic forms. Continuity of the smallest eigenvalue follows directly from its minimum Rayleigh quotient, so the V.D.9 floor passes to the limit. Finally `(1+tau/L)^-L -> exp(-tau)` follows from the elementary logarithm estimate supplied in the text. This proves the factor `mu_delta(1-exp(-tau))`.

The double-limit statement is properly sequential: with `L` and the entire activation `phi_L` fixed, V.F.1 gives convergence in probability as width tends to infinity; those deterministic population limits then converge as depth tends to infinity. V.F.6 identifies the same sequential limit for the raw initialized kernel. The ODE error bound is not represented as a finite-width estimate. No coupling across widths, simultaneous `L(n)` limit, or interchange of limits is needed or asserted.

### 7.3 Equilateral witness, V.D.14

The off-diagonal entries remain equal by the scalar entrywise equation and uniqueness. Oddness makes them `-r(s)`, with `r'=K(r)-r` and initial value `1/2`. The inequalities used for positive r are applied only up to a first hypothetical zero. Differentiating `exp(s)r(s)` gives `r(s)>=exp(-s)/2`, which rules out any finite zero and justifies extending the argument. The upper differential inequality makes r nonincreasing, hence at most `1/2`.

For `u=r^-2`, the sign reversal on multiplication by `-2r^-3` is correct:

\[
u'\ge2(u-1),\qquad u(0)=4,
\qquad u(s)\ge1+3e^{2s}.
\]

The Gram with diagonal one and off-diagonal `-r` has eigenvalues `1-2r` and twice `1+r`. Since r is positive, the first is the smallest. Substitution gives precisely V.D.14, strictly positive for `s>0`. Any scalar multiple of the singular input Gram retains its nullspace, so it cannot reproduce this effect. This is a valid witness of nonlinear geometry, not just preserved variance.

### 7.4 Near-identity estimates and scalar residual, V.D.15–V.D.16

Writing `alpha=(1+gamma²)^-1/2`, the identity `phi_L=alpha z+alpha gamma chi` gives the derivative and weighted-value bounds by `0<=1-alpha<=gamma²/2` and `alpha<=1`. The second derivative is `alpha gamma chi''`, also bounded as stated. Thus the first two derivatives approach those of the identity uniformly, and the values approach locally uniformly with the given weighted global control. Higher fixed derivative orders, if intended by the prose, also follow directly from bounded derivatives of chi.

For each finite L and fixed positive tau, `alpha-1` is nonzero. Its unbounded linear contribution to `phi_L-z` cannot be canceled by the bounded trigonometric term. The unweighted supremum is therefore infinite, as expressly stated; there is no false global-uniform near-identity assertion.

Orthogonality removes exactly `alpha z` in Gaussian affine regression at variance one. The remaining residual has second moment `alpha² gamma²=gamma²/(1+gamma²)=tau/(L+tau)`. Since the feature second moment is exactly one at every layer, this is also the relative residual. Its vanishing with depth is compatible with the proved accumulated geometric floor.

### 7.5 Local variance attraction and scalar derivative product, V.D.17–V.D.19

The cross term in the scalar variance map is `E[Z chi(Z)]=q E chi'(Z)` by Gaussian integration by parts, so V.D.17 has the correct factor `2 gamma q a(q)`. The trigonometric expectation gives the printed `a(q)`. At one, `a(1)=0` and

\[
a'(1)=\frac{-4c_*e^{-2}+\tfrac12e^{-1/2}}{\sqrt{v_*}}
=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]

For q in a positive neighborhood of one,

\[
b'(q)=E\left[\chi(\sqrt q\xi)\chi'(\sqrt q\xi)\frac{\xi}{\sqrt q}\right]
\]

exists and is continuous by boundedness and an integrable multiple of `|xi|`. Thus differentiation is justified, and

\[
V_\gamma'(1)=
\frac{1+2\gamma a'(1)+\gamma^2 b'(1)}{1+\gamma^2}
=1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]

The coefficient of gamma is strictly negative. For sufficiently small positive gamma this derivative has absolute value below one; continuity gives a positive-variance neighborhood with a strict Lipschitz constant below one. Since `V_gamma(1)=1`, the mean-value inequality makes a sufficiently small closed neighborhood invariant and its iterates convergent to one. This establishes precisely the stated local attraction for sufficiently large L at fixed tau. Neither a common neighborhood nor a contraction margin uniform in L is claimed, and none is needed for the initialization recursion that already remains exactly at variance one.

Finally, `E chi'=E xi chi=0`, so expanding the derivative square gives exactly `(1+gamma_L² M_2)/(1+gamma_L²)`. The bounded derivative makes `M_2` finite. Dropping the positive denominator and applying `(1+x)^L<=exp(Lx)` yields the printed bound `exp(tau M_2)`. It is a sufficient, not optimal, constant. The statement expressly limits this to a product of scalar Gaussian moments; it does not infer a network Jacobian norm estimate, independence of backward products, or trained stability from it.

## 8. Final comparisons and exact scope: lines 1272–1337

The table follows from the preceding results with their inherited parameter ranges. Its convex-offset row refers to convergence of the normalized Gram to rank one, as proved in V.C; it does not require convergence of the raw variance. The odd-mixture scalar equivalents are for fixed theta as depth tends to infinity, while the displayed infimum comparisons have universal constants in the joint theorem range. The calibrated row concerns a different activation for each total depth, with tau and chi fixed. No fixed-activation conclusion is substituted for that family statement.

The subsequent discussion correctly separates a numerical absolute kernel floor uniform in depth from positive definiteness at each fixed depth and from a possible trained theorem. Under this model the raw initialized limiting kernel is `Q_L`, so the loss of an absolute floor for the odd mixture is compatible with its positive normalized floor. No training assertion is proved by, or inferred from, either fact.

**Gain normalization:** The algebra `epsilon=e/(a+e)` and `1-epsilon=a/(a+e)` is exact and gives `0<epsilon<1/2` under `a>e>0`. For an actual activation scaling `tilde phi=alpha phi`, the first covariance is `alpha² Q_1`, and the next Gaussian can be coupled as `alpha Z` with `Z~N(0,Q_1)`. The second covariance is therefore precisely `alpha² E[phi(alpha Z)phi(alpha Z)^T]`, even for singular `Q_1`. These formulas correctly demonstrate why there is no general reduction of nonhomogeneous activation scaling to a single final kernel multiplier. The one required correction is the identity-division exception R1 above; the formulas themselves are correct.

**Final high-gain comparison:** Under `a-e>1`, `0<e<=1`, and the stated shape bounds, absorbing the affine part in regression gives

\[
\mathcal R_g(q)=e^2\mathcal R_\psi(q)\le e^2.
\]

The upper bound tests the zero affine fit for the shape and uses `E psi²<=1`. The linear Gaussian projection coefficient of g is

\[
E[\xi g(\sqrt q\xi)]
=\sqrt q\left(a+eE\psi'(\sqrt q\xi)\right).
\]

Its square is a lower bound on the full uncentered second moment. Since `E psi'>=-1` and `a-e>1`, the expression inside parentheses is positive and at least `a-e`, so squaring preserves the lower bound. This verifies the displayed `q(a-e)²` estimate with the correct power of q.

Iteration from `q_0=1` gives `q_l>=(a-e)^(2l)`. At layer l the residual is evaluated at `q_(l-1)` but divided by the output second moment `q_l`, so the final relative bound is exactly `e²/(a-e)^(2l)`. There is no layer-index shift error. The argument does not assume or prove a positive absolute residual floor for an arbitrary allowed shape, and the text correctly makes that possibility conditional. The condition `e<=1` is unnecessary for this particular inequality but harmless; no claimed conclusion requires dropping it.

The final scope paragraph correctly restricts all finite-width results to fixed depth and activation. The later calibrated limit is sequential and deterministic after the width limit. None of the derivations asserts a simultaneous growing-width/depth limit, finite-width ODE error control, positive-training-time convergence, cap removal, a trained Gaussian closure, or fitting. The fresh-Gaussian initialization premise used in every layer is explicit.

## 9. Dependency and coverage closure

The nontrivial mathematical mechanisms actually used are provided in these inputs: the finite-width Gaussian induction and raw-kernel identification, Hermite completeness and its endpoint derivative identities, the Gaussian contraction inequality, the cubic tensor floor, the arctangent coefficient and composed-curvature estimates, and the ODE construction with an explicit discretization error. The remaining tools are elementary probability, finite-dimensional linear algebra, calculus, Hilbert-space projection, and standard elementary integration/convergence facts. No result from an unread Part III, earlier review, external Gaussian-kernel theorem, tensor-conditioning theorem, or numerical calculation is needed to complete a step.

| Substantive input coverage | Equations and claims checked | Result |
|---|---|---|
| PROOF 1–143 | Scope, V.M.1–V.M.9, raw/normalized conditioning and nonaffinity | Verified |
| PROOF 144–260 | V.F.1–V.F.6, covariance continuity, finite-width kernel and zero predictor | Verified |
| PROOF 262–361 | V.F.7–V.F.11, completeness, all correlation endpoints and derivative signs | Verified |
| PROOF 363–400 | V.F.12–V.F.13, tensor PSD powers, singular and endpoint cases | Verified |
| PROOF 402–552 | Theorem V.O.1 hypotheses, V.O.1–V.O.11, variance and product constants | Verified |
| PROOF 553–612 | V.O.12–V.O.15, cubic coefficient, accumulated floors and lower constants | Verified |
| PROOF 613–727 | V.O.16–V.O.22, composition, strict planar witness, upper constants | Verified |
| PROOF 728–816 | V.O.23–V.O.26, joint regimes, nonaffinity asymptotics, linear obstruction | Verified |
| PROOF 818–966 | Theorem V.C.1, V.C.1–V.C.8, rank-one collapse and both scalar floors | Verified |
| PROOF 968–1085 | V.D.1–V.D.9, exact calibration, correlation coefficients, finite-depth floor | Verified |
| PROOF 1087–1190 | V.D.10–V.D.14, ODE, uniform error, sequential matrix/kernel limit, witness | Verified |
| PROOF 1192–1270 | V.D.15–V.D.19, local versus global closeness, residual, scalar stability/product | Verified |
| PROOF 1272–1337 | Comparison table, scaling formulas, high-gain residual and final scope | Verified except minor R1 at 1298 |
| NOTATION 1–98 | Complete read; all conventions used in Part V checked for consistency | No conflict |

Intervening lines outside the tabulated substantive spans are blank separators; they were also included in the full reads. Every displayed equation and every substantive assertion in Part V has been checked. No section was screened only by its conclusion.

**Required action:** Apply the one-sentence correction R1. No other required mathematical correction was identified. With that literal exception qualified, this review's verdict on the complete Part V proof is CLEAN under its stated initialization-only scope.
