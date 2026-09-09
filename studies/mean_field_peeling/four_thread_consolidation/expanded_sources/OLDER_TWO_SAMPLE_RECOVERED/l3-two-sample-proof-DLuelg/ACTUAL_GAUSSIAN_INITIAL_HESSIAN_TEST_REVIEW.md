# Isolated adversarial audit of the Gaussian initial-state Hessian test

## Audit identity, constraints, and verdict

Candidate: `/tmp/l3-two-sample-proof-DLuelg/ACTUAL_GAUSSIAN_INITIAL_HESSIAN_TEST.md`

Verified SHA256:

```text
8068a63d710643d06020701a19d5d90260bf02ce5300d158fe52bd4b10546407
```

The candidate is the only source file read for this audit. No other project or research files, histories, external sources, or experiments were used. The candidate was not edited. The arguments below independently check the mathematics; the candidate's status labels are not evidence.

**Verdict: PASS for the stated, bounded, initial-state route test.** I found no substantive mathematical correction required for equation (2), with fixed data, fixed `rho in [-1,1)`, fixed labels, and fixed real `kappa` and `M`. In particular, the recycled Gaussian query has the asserted limiting empirical law, its scalar coefficient has both unbounded tails, the actual small nonzero readout produces errors uniform over all tested rows, and differentiating the full negative-gradient Jacobian leaves the asserted leading coefficient `16 S_i`.

This verdict does not certify a global mean-field theorem, convergence of any population flow, a positive-time obstruction, or divergence of an integrated response. The precise norm-based obstruction is checked separately below. Several compressed steps and notational conventions merit clarification, but they do not invalidate the result.

## 1. Exact parameter metric and physical-time normalization

Write `w = W^(4)` and `alpha = (W^(1),W^(2),W^(3))`. The metric is the constant inner product whose squared norm is

```text
||(eta_1,eta_2,eta_3,omega)||_raw^2
 = (d/n)||eta_1||_F^2 + ||eta_2||_F^2 + ||eta_3||_F^2
   + ||omega||_2^2/n.
```

Consequently, converting a Euclidean covector into a raw gradient multiplies its four blocks by `n/d`, `1`, `1`, and `n`, respectively. These factors cannot be omitted or absorbed into time.

For a fixed sample, let `p_ell = phi'(z^(ell))` componentwise, and define

```text
q_3 = w * p_3,
q_2 = (W^(3)^T q_3) * p_2,
q_1 = (W^(2)^T q_2) * p_1,
```

where `*` denotes coordinatewise multiplication. Direct differentiation of `f = w^T h^(3)/n` gives

```text
grad_raw f = (
    q_1 x^T/d,
    q_2 (h^(1))^T/n,
    q_3 (h^(2))^T/n,
    h^(3)
).
```

Thus the actual flow is `dot theta = -2 sum_a (f_a-y_a) grad_raw f_a`, and, in particular,

```text
dot w = -2 sum_a (f_a-y_a) h^(3)_a.
```

This checks the readout equation with the stated physical time and includes both the residual and the nonzero initialized readout. No extra factor of `n`, `2`, or `d` is missing.

It is useful to use the normalized feature-vector pairing `u^T v/n`. With this pairing on feature vectors and the raw pairing on hidden parameters, `grad_alpha f = (D h^(3))^* w`. If the feature-space adjoint is instead defined using the ordinary Euclidean pairing, the identity must read `(D h^(3))^* w/n`. The candidate's estimates use the normalized pairing correctly; its short adjoint notation should be read with that convention.

For any scalar smooth function `F`, its Hessian operator is characterized by

```text
<u, Hess_raw F v>_raw = D^2 F[u,v].
```

Since the metric is constant, the vector-field Jacobian is exactly `J = -Hess_raw L`; it is self-adjoint in this metric. Its material derivative is obtained by contracting the next derivative with the actual velocity. There are no metric-derivative terms.

## 2. Activation, initial norm events, and all Gaussian endpoints

Put `c=1/10`. Direct differentiation gives

```text
phi'(z)   = c sech(z),
phi''(z)  = -c sech(z) tanh(z),
phi'''(z) = c sech(z)(1-2 sech(z)^2).
```

The first derivative is strictly positive, all three derivatives are bounded, and `phi''` is strictly negative on `(1,2)`. Also `|phi(z)-1| < pi/20 < 1/6`, so the stated bounds `5/6 < phi < 7/6` are valid. Set `a_0=7/6` below.

The initial norm estimates also have the claimed scalings:

* Writing `W^(1)_ij=G_ij/sqrt(d)`, its squared raw norm is `sum_ij G_ij^2/n`, with mean `d` and variance `2d/n`. It converges in probability to `d`, since `d` is fixed.
* Writing `w_i=G_i/n`, `b_n^2 := ||w||_2^2/n = n^(-2)(sum_i G_i^2/n)`. Hence `b_n <= 2/n` with probability tending to one.
* For each hidden square matrix, a `1/4`-net of the unit sphere has at most `9^n` points: disjoint radius-`1/8` balls around a separated set fit inside the radius-`9/8` ball. Maximality makes this a net. For a pair of deterministic unit vectors, `u^T W v` is Gaussian with variance `1/n`. Completing the square in its exponential moment and optimizing the exponential Markov bound gives `P(|u^T W v|>5) <= 2 exp(-25n/2)`. The union bound over both nets gives `2 exp(n log(81)-25n/2) -> 0`. Approximating both arguments incurs at most `||W||_op/2`, so `||W||_op <= 10` on the complementary event.

The squared-Gaussian means and variances follow from `E G^2=1`, `E G^4=3`; these identities can also be obtained by integrating the derivative of the Gaussian density. Applying the elementary bound `P(|X-E X|>epsilon) <= Var(X)/epsilon^2` establishes the probability statements. No random-matrix theorem is needed.

The first-layer pair is exactly Gaussian with covariance `C`, because each row is a Gaussian linear image of the fixed input pair. For `-1<rho<1`, this distribution has a positive density on the plane. If

```text
c_1 phi(Z_1) + c_2 phi(Z_2) = 0 almost surely,
```

continuity and positive density make the same relation hold at every pair of real arguments. Varying one argument while fixing the other forces its coefficient to vanish, since `phi` is strictly increasing. Both coefficients must therefore be zero. This is exactly the criterion for positivity of `E[H H^T]` as a quadratic form.

The singular endpoint `rho=-1` needs a separate check, which the candidate supplies correctly. Write `Z_1=G`, `Z_2=-G` and `b(G)=c atan(sinh G)`. Then

```text
H = (1+b(G), 1-b(G)).
```

Here `b` is odd and nonconstant. Let `q=E[b(G)^2]>0`; symmetry gives `E b(G)=0`, and

```text
K^(1) = [[1+q, 1-q], [1-q, 1+q]].
```

Its two eigenvalues are `2` and `2q`, both positive. Thus antiparallel inputs do not leave the second layer with a singular covariance. Once `K^(1)` is positive definite, the positive-density argument proves positivity of `K^(2)` and, if needed, `K^(3)` as well. These arguments hold regardless of the labels.

The strict exclusion of `rho=1` matters. At that endpoint, the two samples have identical features, and the sample-isolating direction used later is unavailable. Nothing in this audit extends the theorem to that endpoint or to a sequence `rho_n` approaching it.

## 3. Forward empirical laws, including the continuity step

For the new layer, conditional on all preceding layers, its row pairs are independent Gaussian vectors with covariance equal to the preceding empirical feature Gram matrix. For a bounded test `F`, the conditional variance of its empirical average is at most `||F||_infinity^2/n`. Its conditional mean is the Gaussian expectation with that covariance. Therefore it remains to check continuity of this expectation and convergence of the preceding Gram matrix.

Here covariance continuity is elementary, including singular limits. For a nonzero two-by-two positive semidefinite matrix `A`,

```text
A^(1/2) = (A + sqrt(det A) I) / sqrt(tr A + 2 sqrt(det A)).
```

Squaring this expression using `A^2 - (tr A)A + (det A)I=0` verifies the formula. It is continuous wherever `tr A>0`, which covers all covariances here. Coupling Gaussian vectors as `A^(1/2)G`, with a fixed standard two-dimensional Gaussian `G`, proves continuity of expectations of bounded continuous tests. Explicitly, restrict `G` to a large fixed ball, use uniform continuity there, and bound the complementary contribution by the test bound times the Gaussian tail probability. This also explains why a singular first-layer covariance causes no difficulty.

Each entry of the feature Gram is a bounded continuous test of a forward row. Conditional variance control, continuity of its conditional mean, and induction through the three fixed layers establish all stated Gram convergences in probability. The same reasoning proves the needed empirical law for `z^(2)` itself. A finite union bound establishes joint convergence of the finitely many quantities used below.

For tests such as `Z_b U_a(Z)`, which are not bounded, the same argument remains valid: `U` is bounded, the covariances are bounded, and the conditional second moments of `Z_b U_a(Z)` are uniformly bounded. Thus the conditional variance of their average is still `O(1/n)`. Continuity of their means follows by the same coupling, truncating the Gaussian tail and using its integrable first moment. More generally, Gaussian moments of any fixed order are uniformly bounded here; the corresponding tail truncation uses one higher moment. This verifies, rather than assumes, the unbounded test needed in the reused-matrix coefficient.

For inverse Gram matrices, one can work throughout on events where `K^(1)_n` and `K^(2)_n` are sufficiently close to their positive definite limits. These events have probability tending to one and give deterministic bounds on their inverses. In two dimensions this also follows immediately from the inverse formula and convergence of the positive determinant. There is no need to define the displayed inverses at width one.

## 4. Independent derivation of the adaptive reused-matrix law

Use row arrays: `H` is the `n by 2` second-layer feature array, `Z=W^(3)H`, and the rows of `U` are the vectors

```text
U_a(Z_k) = V(Z_k) phi'(Z_ka),
V(z) = (1/2) sum_b y_b phi(z_b).
```

Let the conditioning include all preceding arrays and `Z`. On the full-column-rank event for `H`, define

```text
K_n = H^T H/n,
Pi = H(H^T H)^(-1)H^T.
```

For one isotropic Gaussian row of `W^(3)`, its orthogonal projections onto `col(H)` and its orthogonal complement are independent: in an orthonormal basis adapted to those two spaces, the Gaussian density factors over the two groups of coordinates. Conditioning on the row's product with `H` fixes the first projection and leaves the other unchanged. Applying this row by row proves the conditional representation

```text
W^(3) = Z(H^T H)^(-1)H^T + G(I-Pi),
```

where `G` is a fresh Gaussian matrix with entry variance `1/n`, independent of the conditioning variables. This equality is a conditional distributional representation; it is not an assertion that an arbitrary independently chosen `G` equals the residual of an already fixed matrix pathwise.

Multiplying by `U` after transposition gives the exact conditional law

```text
R_n = H A_n + (I-Pi)b,
A_n = K_n^(-1)(Z^T U/n),
b = G^T U.
```

Conditional on the revealed arrays, the rows `b_i` are independent centered Gaussian vectors with covariance

```text
S_n = U^T U/n.
```

This is the step where adaptivity is controlled. `U` may depend on the revealed `Z`, and in fact does; it is fixed under this conditioning and does not depend on the unexposed Gaussian residual. Independence between the unconditioned finite reused-query rows is neither asserted nor required.

Conditional averaging, with the bounds in the previous section, gives

```text
S_n -> S = E[U U^T],
Z^T U/n -> T = E[Z U^T],
A_n -> (K^(2))^(-1) T.
```

The matrix orientation matters. With the convention

```text
Gamma_ab = E[partial_b U_a(Z)],
```

direct differentiation yields

```text
partial_b U_a(z)
 = (y_b/2) phi'(z_b) phi'(z_a)
   + 1_(a=b) V(z) phi''(z_a).
```

All these derivatives are bounded. If `p_K` is the density of `N(0,K^(2))`, then

```text
partial_b p_K(z) = -(K^(2)^(-1)z)_b p_K(z).
```

Integrating `partial_b(U_a p_K)` over expanding rectangles gives zero in the limit. Its boundary integrals vanish because `U_a` is bounded and the Gaussian density decays; its interior terms are integrable because `partial_b U_a` is bounded and the Gaussian first moment is finite. Therefore

```text
E[U Z^T] = Gamma K^(2),
T = K^(2) Gamma^T,
A_n -> Gamma^T.
```

The deterministic part of the limiting row vector is consequently `Gamma H^(2)`, exactly as in equation (5), not its transposed alternative.

The projection correction is small as an empirical error. Indeed,

```text
E[||Pi b||_F^2 | H,Z] = rank(Pi) tr(S_n) = 2 tr(S_n).
```

The entries of `U` are bounded, so `tr(S_n)` is deterministically bounded. Dividing by `n` and applying the elementary nonnegative-variable Markov bound shows `||Pi b||_F/sqrt(n) -> 0` in probability. For a test with Lipschitz constant `L`, changing all rows from `b` to `(I-Pi)b` changes its empirical average by at most

```text
(L/n) sum_i ||(Pi b)_i|| <= L ||Pi b||_F/sqrt(n).
```

This is sufficient. The proof does not need a bound on the maximum projection error.

For completeness, the remaining empirical averaging step can be written explicitly. For a bounded Lipschitz test `F(z,r)`, the conditional variance of

```text
(1/n) sum_i F(z^(2)_i, A_n^T h^(2)_i + b_i)
```

is `O(1/n)`. Couple each conditional `b_i` marginal as `S_n^(1/2)G`. Since every `h^(2)_i` is bounded, the conditional mean differs, uniformly in the old row argument, from the average of

```text
Q(z) = E_G F(z, Gamma phi(z) + S^(1/2)G)
```

by at most a constant times

```text
||A_n-Gamma^T|| + ||S_n^(1/2)-S^(1/2)|| E||G||.
```

Both terms tend to zero in probability. The function `Q` is bounded and Lipschitz, since `phi` is globally Lipschitz. The previously established empirical law of `z^(2)` applies to it. Combining these facts and the projection bound proves

```text
(z^(2),R_n) empirical law ->
(Z^(2), Gamma H^(2) + zeta),
zeta ~ N(0,S), independent of Z^(2),
```

in probability for every bounded Lipschitz test. This proves the empirical statement needed later, including the effect of the reused matrix.

## 5. Nondegeneracy for all labels and the fixed-threshold tail argument

The top-layer covariance `K^(2)` is positive definite, also when the original inputs are antiparallel. Thus `Z^(3)` has positive density everywhere in the plane.

For equal labels, `|V(z)|=(phi(z_1)+phi(z_2))/2 >= 5/6`. For opposite labels, `|V(z)|=|phi(z_1)-phi(z_2)|/2`, which is nonzero whenever `z_1 != z_2`. In either case, on a nonempty open set, `V(z)^2 phi'(z_a)^2 > 0`. Positive density then gives

```text
S_aa = E[V(Z^(3))^2 phi'(Z^(3)_a)^2] > 0
```

for either sample and all four label assignments. Positive definiteness of the entire matrix `S` is unnecessary; positivity of this diagonal entry suffices.

Conditional on `Z^(2)=z`, the scalar `R_a` is Gaussian with variance `S_aa>0` and mean `(Gamma phi(z))_a`. Its mean is uniformly bounded. Restrict `z_a` to a closed interval strictly inside `(1,2)` and the other coordinate to any compact interval with nonempty interior. This rectangle has positive probability under the nonsingular second-layer Gaussian law. On it, `|phi''(z_a)|` is bounded below by a positive constant. Hence

```text
X_a := y_a phi''(Z^(2)_a) R_a
```

has, conditionally on every point of this rectangle, a Gaussian law with nonzero variance. For every finite `T`, both events `X_a>T` and `X_a<-T` have positive unconditional probability.

Here is a direct bridge from these tails to empirical maxima, avoiding any use of unbounded tests or independence of the finite rows. The joint law of `(Z^(2),R_a)` has positive density at every point of three-dimensional space, since its conditional scalar variance is strictly positive. For a fixed `T`, choose a sufficiently large finite value of `r_a` of the appropriate sign and a sufficiently small open box in `(z_1,z_2,r_a)` on which `y_a phi''(z_a)r_a>T`. A nonnegative tent function supported inside that box, positive on a smaller box, is bounded and Lipschitz and has positive limiting expectation. Viewed as a function of the full pair `(z,r)`, it can simply ignore the unused coordinate of `r`.

The empirical law proved in Section 4 implies that the empirical average of this test is positive with probability tending to one. There must then be at least one row above `T`. Repeating with the other sign gives

```text
max_i y_a phi''(z^(2)_ia) R_(n,i,a) -> +infinity,
min_i y_a phi''(z^(2)_ia) R_(n,i,a) -> -infinity
```

in probability, in the fixed-threshold sense. A union bound gives the two statements jointly if desired. No threshold depending on `n`, extreme-value approximation, or assertion of finite-row independence is used.

## 6. Multilinear derivatives: checking every power of width

All constants in this section are independent of `n` and the row index. They can depend on the fixed architecture, activation, and fixed data. We evaluate derivatives at the initialized hidden parameters, with both hidden operator norms at most `10`.

A first-layer variation obeys

```text
||eta_1 x_a||_2 <= sqrt(d)||eta_1||_F
                 <= sqrt(n)||eta||_raw.
```

The elementary coordinate-product inequality is

```text
||v_1 * ... * v_j||_2 <= product_r ||v_r||_2.
```

For example, bound all but one factor by its maximum coordinate, and then bound each such maximum by its Euclidean norm. Dividing by `sqrt(n)` gives exactly the candidate's normalized inequality, including the factor `n^((j-1)/2)`.

The first-layer preactivation is linear in its weights. Its first three feature derivatives are therefore the appropriate coordinate products of first preactivation variations times the bounded scalar derivatives of `phi`. They have unnormalized Euclidean bounds `C_j n^(j/2) product_r ||eta_r||_raw`.

At a subsequent layer, for arbitrary mixed directions, the exact multilinear product rule is

```text
D^j(Wh)[eta_1,...,eta_j]
 = W D^j h[eta_1,...,eta_j]
   + sum_r eta_r^(W) D^(j-1)h[eta_1,...,omit eta_r,...,eta_j].
```

For `j=1`, the second term uses `||h||_2 <= a_0 sqrt(n)`. For `j=2,3`, it uses the already obtained lower derivative bound. The matrix variations obey `||eta_r^(W)||_op <= ||eta_r^(W)||_F <= ||eta_r||_raw`. These terms have no power of `n` greater than `n^(j/2)`.

The scalar chain rule gives, respectively, terms of the following types:

```text
D h:    phi' D z;
D^2 h:  phi' D^2 z,  phi'' (D z)(D z);
D^3 h:  phi' D^3 z,  phi'' (D^2 z)(D z) in three positions,
        phi''' (D z)(D z)(D z).
```

The product inequality bounds every term by `C_j n^(j/2)` times the direction norms. This proves, at both remaining layers, the candidate's equation (7):

```text
||D^j V[eta_1,...,eta_j]||_2/sqrt(n)
 <= C_j n^((j-1)/2) product_r ||eta_r||_raw,
j=1,2,3.
```

The same proof applies to either individual top feature map. No bound on the first weight's operator norm or on individual initialized preactivations is needed. Bounded activation derivatives are enough.

For `g=w^T V/n`, the mixed hidden/readout second derivative is `omega^T DV[eta]/n`, hence is bounded by `C ||omega||_2/sqrt(n) ||eta||_raw`. The hidden/hidden derivative is bounded by `C sqrt(n) b_n ||eta||_raw ||xi||_raw`. There is no readout/readout second derivative. Thus

```text
||Hess_raw g||_op <= C(1+sqrt(n)b_n),
||Hess_raw f_a||_op <= C(1+sqrt(n)b_n),
||grad_raw f_a||_raw <= C(1+b_n).
```

On `b_n<=2/n`, these are uniform constant bounds. In particular, the full Hessian norm bound includes all parameter blocks, not only the hidden block or the specially chosen directions.

For pure hidden directions, the finer bounds are

```text
|D f_a[v]| <= C b_n ||v||_raw,
|D^2 g[v,v]| <= C sqrt(n)b_n ||v||_raw^2,
|D^3 g[e,v,v]| <= C n b_n ||e||_raw ||v||_raw^2.
```

These are precisely the powers needed in the later perturbation argument. In particular, there is no unjustified uniform bound on the third derivative.

## 7. The sample-isolating row direction and its exact second derivative

Fix a sample `a`. On the high-probability inverse-Gram event, let `K=K^(1)_n` and define

```text
v_row = H_1 K^(-1)e_a / sqrt(n(K^(-1))_aa),
d_a = 1/sqrt((K^(-1))_aa).
```

An explicit norm calculation gives

```text
||v_row||_2^2
 = e_a^T K^(-1)(nK)K^(-1)e_a / (n(K^(-1))_aa)
 = 1,
v_row^T h^(1)_b = sqrt(n)d_a 1_(a=b).
```

Placing this vector in row `i` of the second weight matrix and zero in all other parameter blocks therefore produces a raw unit direction `v_i`. For a two-by-two positive definite Gram matrix, with `b` the other sample,

```text
d_a^2 = K_aa - K_ab^2/K_bb.
```

This proves `0<d_a^2<=K_aa<=a_0^2`. Since the population Gram is positive definite, `d_a^2` converges to a fixed positive constant. At the antiparallel endpoint, the explicit value of that limit is `4q/(1+q)>0`, using the `q` in Section 2. There is no hidden failure of this direction at that endpoint.

When taking derivatives, **freeze the chosen vector `v_i` at initialization**. Its dependence on the initial array is allowed in a pointwise Rayleigh-quotient test; it is not a direction transported along the flow.

Along this fixed direction the first-layer features are constant, and the second-layer preactivation changes linearly. The exact nonzero preactivation variations are

```text
Dz^(2)_a[v_i] = sqrt(n)d_a e_i,
Dz^(3)_a[v_i] = sqrt(n)d_a phi'(z^(2)_ia) W^(3)_:,i,
D^2z^(3)_a[v_i,v_i] = n d_a^2 phi''(z^(2)_ia) W^(3)_:,i.
```

For the other sample, these variations are zero. Applying the scalar second derivative at layer three gives

```text
D^2 V[v_i,v_i]
 = (y_a/2) n d_a^2 [
      phi'(z^(2)_ia)^2 phi''(z^(3)_a) * (W^(3)_:,i)^2
      + phi''(z^(2)_ia) phi'(z^(3)_a) * W^(3)_:,i
   ].
```

Pairing with `V/n` produces exactly

```text
S_i = V^T D^2V[v_i,v_i]/n
    = (y_a d_a^2/2) phi''(z^(2)_ia) R_(n,i,a) + E_i,

E_i = (y_a d_a^2/2) phi'(z^(2)_ia)^2
      sum_k V_k phi''(z^(3)_ka) (W^(3)_ki)^2.
```

In particular, neither a residual nor the actual readout belongs in this definition of `R_n`. It arises from differentiating the label-weighted feature map, whose coefficient is restored to the actual dynamics below.

The error is uniformly bounded over all rows, because

```text
sum_k (W^(3)_ki)^2 = ||W^(3)_:,i||_2^2 <= ||W^(3)||_op^2 <= 100,
```

and all other factors in `E_i` are bounded. Choose a deterministic `c_*>0` such that `d_a^2>=c_*` on an event of probability tending to one. If the scalar coefficient from Section 5 exceeds `T`, then `S_i >= c_* T/2-C`; if it is below `-T`, then `S_i <= -c_* T/2+C`. Taking a fixed sufficiently large `T` for any requested threshold proves both divergences in equation (11).

The dependence between the selected row, the Gram matrix, and the reused Gaussian query causes no problem: the tail statement is empirical and the other bounds hold simultaneously over all rows.

## 8. The actual nonzero readout and uniform material-Hessian errors

Define a concrete high-probability event by intersecting the two hidden operator-norm events, `b_n<=2/n`, a fixed bound on the first raw weight norm, and small fixed neighborhoods of the positive definite feature-Gram limits. All estimates below hold with deterministic constants on this event.

Cauchy--Schwarz gives `|f_a| <= a_0 b_n`. The exact readout velocity can be decomposed as

```text
dot w = 2 sum_a y_a h^(3)_a - 2 sum_a f_a h^(3)_a
      = 4V + e_w,
||e_w||_infinity <= C b_n,
||e_w||_2/sqrt(n) <= C b_n.
```

The hidden part of `grad_raw f_a` has norm at most `C b_n`. The residuals are bounded, so

```text
||dot alpha||_raw <= C b_n,
||dot w||_2/sqrt(n) <= C,
||dot theta||_raw <= C.
```

These are bounds on the actual initialized model. The Euclidean readout velocity can have size `sqrt(n)`; its raw norm is bounded because of the metric's factor `1/n`. Treating that Euclidean size as a raw size would give the wrong argument.

Let `B=Hess_raw g`. On a frozen pure hidden unit direction, the exact contraction is

```text
<v_i, dot B v_i>_raw
 = dot w^T D^2V[v_i,v_i]/n
   + w^T D^3V[dot alpha,v_i,v_i]/n.
```

The leading readout part is `4S_i`. The two errors are bounded, respectively, by

```text
(||e_w||_2/sqrt(n))(||D^2V[v_i,v_i]||_2/sqrt(n))
 <= C sqrt(n)b_n,

(||w||_2/sqrt(n))(||D^3V[dot alpha,v_i,v_i]||_2/sqrt(n))
 <= C n b_n ||dot alpha||_raw <= C n b_n^2.
```

Thus

```text
sup_i |<v_i,dot B v_i>_raw - 4S_i|
 <= C(sqrt(n)b_n + n b_n^2)
 <= C n^(-1/2).
```

This proves equation (13), including its uniformity. It uses no cancellation with the Gaussian readout and no assertion about a tagged row. The small readout is retained everywhere. Together with the bounded operator norm of `B`, it also proves the intermediate assertion concerning `lambda_max(dot B-kappa B^2)`.

## 9. Full signed material Jacobian: all summands and signs

The loss identity is exact because `g=(1/2)sum_a y_a f_a` and `y_a^2=1`:

```text
L = sum_a f_a^2 - 4g + 2.
```

Let `q_a=grad_raw f_a` and `H_a=Hess_raw f_a` in this section only. Differentiating twice and remembering that the vector field is the negative gradient gives

```text
J = 4B - 2 sum_a q_a tensor q_a - 2 sum_a f_a H_a.
```

Here `(q tensor q)v = q <q,v>_raw`. The previously verified full gradient and Hessian bounds imply `||J(0)||_op <= C_J` on the same high-probability event. This checks the candidate's initial Jacobian bound for the whole parameter space.

Differentiate this identity along the actual flow, then evaluate on a frozen pure hidden unit direction `v`. The result is

```text
<v,dot J v>_raw
 = 4 <v,dot B v>_raw
   - 4 sum_a D f_a[v] D^2 f_a[dot theta,v]
   - 2 sum_a dot f_a D^2 f_a[v,v]
   - 2 sum_a f_a D^3 f_a[dot theta,v,v].
```

This formula accounts for both differentiated factors in each rank-one operator and for both differentiated factors in `f_a H_a`. It is the full signed material Jacobian, not a calculation of one favorable summand.

Every other term is small on the chosen directions:

1. `|D f_a[v]| <= C b_n`, while `|D^2 f_a[dot theta,v]| <= ||H_a||_op ||dot theta||_raw <= C`. Their product is `O(b_n)`.
2. `|dot f_a| <= ||grad_raw f_a||_raw ||dot theta||_raw <= C`, while `|D^2 f_a[v,v]| <= C sqrt(n)b_n`. Their product is `O(sqrt(n)b_n)`.
3. Since `f_a=w^T h^(3)_a/n` is linear in `w`, the last third derivative splits exactly as

   ```text
   D^3 f_a[dot theta,v,v]
    = dot w^T D^2 h^(3)_a[v,v]/n
      + w^T D^3 h^(3)_a[dot alpha,v,v]/n.
   ```

   Its magnitude is at most `C(sqrt(n)+n b_n^2)`. Multiplying by `|f_a|<=C b_n` gives `O(sqrt(n)b_n+n b_n^3)`.

Including the previously bounded error in `dot B`, the resulting bound is

```text
sup_i |<v_i,dot J v_i>_raw - 16S_i|
 <= C(sqrt(n)b_n + n b_n^2 + b_n + n b_n^3)
 <= C n^(-1/2).
```

The coefficient `16` is therefore correct: one factor `4` comes from the leading physical readout velocity, and the other comes from `J=4B+...`. There is no surviving order-one or divergent cancellation from the squared-output part of the loss. This proves equation (15) for the actual initialized vector field, uniformly over the adaptive choice of row.

## 10. Operator conclusion and its probability quantifiers

Because `J` is self-adjoint in the constant raw metric,

```text
<v,J^2v>_raw = ||Jv||_raw^2 <= C_J^2
```

for every raw unit vector on the high-probability event. Consequently, for every fixed real `kappa`,

```text
lambda_max(dot J-kappa J^2)
 >= max_i <v_i,(dot J-kappa J^2)v_i>_raw
 >= 16 max_i S_i - C n^(-1/2) - |kappa| C_J^2.
```

The first inequality follows directly by maximizing the quadratic form over the unit sphere; for a self-adjoint finite-dimensional operator its maximum is an eigenvalue, as differentiation at a maximizing unit vector shows. Thus no spectral asymptotic result is being used.

Given fixed `M` and `kappa`, choose a fixed threshold for `max_i S_i` large enough to make the final expression exceed `M` for all sufficiently large `n`. The probability of that threshold event tends to one by Section 7, and the probability of the norm and Gram event also tends to one. This proves exactly

```text
P{lambda_max[dot J_n(0)-kappa J_n(0)^2] > M} -> 1.
```

The absolute value on `kappa` makes the argument valid for either sign. There is no uniform assertion for `kappa` depending on width, nor any rate of divergence inferred from the fixed-threshold empirical argument.

## 11. Existence at zero and the exact scope of the obstruction

For each fixed width, the vector field is smooth on a finite-dimensional parameter space. The local solution needed here can be justified without importing a population-flow theorem. On a sufficiently small closed ball around the initial state, the field and its first derivative have finite bounds `B` and `L`. Choose a time interval with `B tau` smaller than the ball radius. Integral iterates

```text
theta_(m+1)(t) = theta_0 + integral_0^t F(theta_m(s)) ds,
theta_(0)(t) = theta_0
```

stay in the ball, and their successive differences are bounded by `B L^m t^(m+1)/(m+1)!`. Summing this convergent series gives uniform convergence to a differentiable solution of the integral equation. Iterating the same difference estimate gives uniqueness. Smoothness of the field then gives the derivatives used in the audit. This construction is for each fixed width; no lower bound on `tau` uniform in width is needed. Equivalently, the initial material derivative is already the algebraically defined contraction `DJ(theta_0)[F(theta_0)]`.

The norm-based consequence of equation (2) is sound with the candidate's explicit list of controls. Let

```text
X_n = (
  sqrt(d/n)||W^(1)_0||_F,
  ||W^(2)_0||_op,
  ||W^(3)_0||_op,
  ||w_0||_2/sqrt(n),
  ||J_n(0)||_op
).
```

This tuple is bounded in probability. For any width-independent function `F` that is bounded on bounded sets, `F(X_n)` is bounded above in probability. To see the contradiction with an operator bound explicitly, for any radius `R` let `C_R` bound `F` on that bounded set. Then

```text
P{lambda_max(dot J_n-kappa J_n^2) <= F(X_n)}
 <= P{||X_n||>R}
    + P{lambda_max(dot J_n-kappa J_n^2) <= C_R}.
```

The second term tends to zero; tightness makes the limiting upper bound from the first term arbitrarily small by increasing `R`. Thus such an upper operator bound fails with probability tending to one under these initialized laws. This is stronger than merely identifying rare bad states, but remains an initial-state statement about this specified class of controls.

The limitations are material:

* The raw Frobenius norms of the two hidden square matrices are **not** bounded in probability. In fact `||W^(ell)||_F^2/n` is the average of `n^2` squared standard Gaussians and converges to `1`. Therefore the entire raw parameter norm is not asserted to be tight. The result does not rule out an estimate involving those diverging Frobenius norms, an explicit width dependence, or other uncontrolled parameter statistics.
* The data and `rho<1` are fixed before width tends to infinity. Positivity constants can degenerate if the data vary with width. No uniform-in-data conclusion is proved.
* The tested quadratic-form directions can depend on the initialized hidden array. This is legitimate for an operator bound; it does not establish divergence on a predetermined direction.
* The empirical law gives exceedance of every fixed threshold, with no quantified growth rate for the maximum.
* `R_a` has bounded conditional mean and fixed Gaussian conditional variance, and `phi''` is bounded. Thus the scalar coefficient can have finite moments of every order while its maximum diverges. There is no contradiction with bounds involving suitable averages.
* Only time zero is treated. No positive-time failure, integrated-response divergence, failure of population existence or uniqueness, or global MF/GF/GD conclusion follows.

These limitations agree with the candidate's opening qualification and its logical-boundary section. The phrase “primal-only” should always be understood with the particular bounded norm tuple above, rather than as a claim about every possible function of the full parameter array.

## 12. Required versus optional corrections

### Required mathematical corrections

**None found for the theorem as stated.** The conditioned Gaussian law, all-label nondegeneracy, antiparallel endpoint, raw-metric derivative powers, uniform actual-readout errors, full signed Jacobian calculation, and final probability implication all withstand the independent checks above.

No unsupported global theorem has been certified by this verdict. Expanding the conclusion beyond the fixed-data initial-state statement would require additional arguments, not a change of status label.

### Optional clarifications and proof expansions

1. **Adjoint normalization, Section 5 of the candidate.** State that the feature-space pairing in `(D h)^*w` is `u^T v/n`, or write the explicit dual pairing `D_alpha f[eta]=w^T D h[eta]/n`. With an ordinary Euclidean feature adjoint, an explicit `/n` is required. The proof's norm estimates already use the correct pairing.
2. **Inverse-Gram events, Sections 2 and 4.** Explicitly restrict inverse formulas to sufficiently large widths on the positive-definite Gram event, and give fixed neighborhoods of the population Grams when defining `E_n`. This avoids interpreting the inverse formulas at width one and makes constants fully explicit.
3. **Conditional coefficient averaging, Section 2.** Add the conditional second-moment bound for `Z_b U_a(Z)`, since this particular test is unbounded. Boundedness of `U` and of the forward covariance proves the needed bound immediately; no new assumption is required.
4. **Conditional representation and orientation, Section 2.** Identify the matrix decomposition as a conditional distributional representation and display `E[Z U^T]=K^(2) Gamma^T`. This prevents a transpose error or an unwarranted finite-row independence interpretation.
5. **Frozen test directions, Sections 4–5.** State explicitly that `v_i` is chosen at initialization and held fixed when evaluating the material derivative. The displayed calculations are correct under this intended convention.
6. **Scope wording, Section 6.** Keep the phrase “primal-only” tied to the specifically listed norms and to functions bounded on bounded sets. The hidden Frobenius norms do grow with width, and the theorem does not control all functions of the full parameters.

These are expository or notational improvements, not repairs to the route-test conclusion. The candidate supports the claimed obstruction at canonical Gaussian initialization, including its prescribed tiny nonzero readout, and supports no broader theorem without further work.
