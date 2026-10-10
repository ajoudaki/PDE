# Independent audit of the shortened feature-learning proof

Verdict: **PASS within the assigned scope.** I found no substantive gap in the shortened proof of Theorem `thm:nonlinear-learning`. Given the preceding real-fitting lemma and the three supplied absolute compression-accuracy results, the argument is self-contained at the usual level of a mathematical research proof. The scalar adjoint calculation supplies the feature-motion and kernel conclusions without an omitted full vector acceleration theorem.

This review used the setup, headline statement and proof architecture in `paper/compact.tex`, and the complete files `paper/compact_fitting.tex`, `paper/feature_learning_theorem.tex` and `paper/compact_feature_learning.tex`. It did not review or independently certify the three compression constructions, their storage derivations, or the broader compression theorem. No other study's evidence was used. The rigorous-math and canonical-notation instructions, including the neural-network conventions, were applied.

## 1. Nonlinear initial kernel and four deterministic witnesses

The argument in `compact_feature_learning.tex:17–75` covers all the stated activation and data cases. Bounded real derivative gives linear growth and Gaussian square integrability even when the activation itself is unbounded. At every positive variance, finite Hermite support would make the analytic activation a polynomial on the real axis, and its bounded derivative would then make it affine. Thus a nonaffine activation has unbounded Hermite support. Squared Hermite coefficients give the nonnegative covariance series; composition preserves unbounded positive support because the inner series has a positive coefficient of positive degree. The diagonal covariance stays positive throughout.

For distinct nonparallel and nonantiparallel normalized inputs, the tensor Gram with entries `(v_a^T v_b)^k` tends to the identity. This proves positive definiteness at every hidden layer, regardless of the rank of the input Gram and in particular when `m > d`.

The projected kernel `R_k` is positive semidefinite: it is the Gram of the tensor feature after its constant and linear spherical components have been removed. Its stated constant and linear coefficients are the orthogonal projection coefficients. They tend to zero, so the finite training Gram of `R_k` also tends to the identity. Consequently a nonzero label vector cannot cancel all nonlinear components of the limiting initial velocity. This handles even activations and arbitrary label signs, not merely generic labels or odd activations.

The additional data hypothesis and `m >= 2` imply both `d >= 2` and `dim V >= 2`. If the velocity were affine on every great circle, its antipodal average would be a global constant and its odd part would have a homogeneous extension linear on every two-dimensional plane, hence globally linear. The claimed nonaffine great circle therefore exists. Three distinct points on that circle determine an affine function on its plane, and a fourth point witnesses failure. Normalizing their affine dependence produces exactly the required four-point functional, including its absolute coefficient sum of one. All choices use only the fixed problem. The finite-query initialization argument in the preceding fitting lemma applies to the augmented list without requiring a Gram gap on that list.

## 2. Gaussian backward conditioning and positive hidden energies

The conditioning identity in `compact_feature_learning.tex:102–135` is valid for the tied forward/backward use of each hidden matrix. Conditional on the forward answer `WH = Z`, the residual matrix is a fresh Gaussian matrix multiplied on the right by `I - Pi_H`. Before its reverse answer, the query `U` is measurable from the forward transcript and reverse answers of higher matrices, so it does not expose this matrix's remaining Gaussian randomness. The reverse answer is therefore

\[
W^\top U=H Q_n^{-1}C_n+(I-\Pi_H)\Xi D_n^{1/2}
\]

in conditional law, with the definitions in the proof. Each matrix is used only once in reverse order. There is no missing second adaptive query or additional conditioning correction.

The removed projection has conditional squared empirical norm `rank(H) tr(D_n)/n`, which vanishes because the number of training inputs is fixed and the existing second moments converge. Positive definiteness of the limiting hidden Grams gives invertibility of the finite Grams on events with probability tending to one. No inverse of `Q^(0)` is needed.

The empirical quadratic-Wasserstein induction is sufficient here. Independent Gaussian augmentation, convergent finite covariance matrices, and continuous maps of at most linear growth preserve the joint row laws with second moments. In particular, the map `(z,u) -> phi'(z)u` has the required growth because `phi'` is bounded. This proves the claimed joint law for the full first-layer rows, the pre-gated backward vectors and the first-layer acceleration; no higher-moment assertion is silently needed later.

The top backward Gram is positive definite. Because `L >= 2`, the top preactivation vector has a full-support Gaussian law. A null vector would make the product of the nonzero analytic label combination and a linear combination of the derivative functions identically zero. Analyticity forces the derivative combination to vanish identically, and varying one coordinate at a time forces every coefficient to vanish. Downward propagation then adds a fresh Gaussian innovation with positive definite covariance independent of the lower forward fields. The displayed lower bound for the gated Gram follows by conditioning on those fields.

The acceleration energies have the exact limiting form

\[
e_\ell=\left(\frac2m\right)^4
y^\top\bigl(Q^{(\ell-1)}\circ D^{(\ell)}\bigr)y>0.
\]

For the first layer this uses the normalized Frobenius norm; for later layers it uses the ordinary Frobenius norm. The stated Schur-product lower bound is valid even for singular `Q^(0)`, since its diagonal is positive. Thus every hidden block contributes positive limiting energy.

## 3. Real estimates and the quantifiers in the remainders

The preceding fitting lemma supplies the deterministic operator, feature and residual bounds used in `compact_feature_learning.tex:177–225`, on one event with probability tending to one. They imply readout and backward responses of order `t`, hidden weight and feature increments of order `t^2`, and the predictor expansion through its initial velocity. These bounds are uniform in the query sphere. The initial pre-gated vectors are also bounded in empirical norm: their top value is a fixed label combination of initial features and the downward recursion applies bounded operators and gates.

The multiplier estimate is enough to replace a width-dependent maximum-coordinate Taylor bound. Joint row-law convergence with second moments implies that, for any prescribed positive tolerance, a fixed cutoff makes every required initial squared tail smaller than that tolerance with probability tending to one. The cutoff is chosen first; a deterministic small time is chosen second. On the fitting event, the first term of the multiplier estimate is then uniformly small for every time in that interval, including points on each activation segment.

This establishes the exact `o_*` convention stated in the lemma: for every positive error tolerance there is one deterministic interval on which the probability of any normalized-remainder violation tends to zero. It is not merely convergence at each fixed time or an informal interchange of the width and time limits. Finite backward recursion, finite sums, and integration preserve this form of control. The normalized outer-product identities then justify the weight expansion in the inverse-mobility norm.

## 4. The scalar adjoint identity supplies the missing forward information

Let `k = 2/m`, and use the initial fields `P_a^(ell)` and `B_a^(ell)` from the proof. The integral formula for the activation and the multiplier estimate give

\[
\langle P_a^{(\ell)},\Delta h_a^{(\ell)}\rangle_n
=\langle B_a^{(\ell)},\Delta z_a^{(\ell)}\rangle_n+o_*(t^2).
\]

For a hidden matrix, pairing the direct increment `Delta W h(0)` with the label-weighted `B` vectors gives

\[
\frac1{k^2}\langle\ddot W^{(\ell)}(0),\Delta W^{(\ell)}\rangle_F
=\frac{t^2}{2k^2}E_{\ell,n}+o_*(t^2).
\]

For the first layer the same formula includes the factor `1/n` in both the inner product and `E_{1,n}`. The term `W(0) Delta h` is exactly the lower-layer adjoint pairing, and `Delta W Delta h` is of order `t^4` in empirical norm. Telescoping therefore proves the stated scalar identity at every layer, including the first-layer base case.

Each sum of energies has a positive deterministic limit. Cauchy–Schwarz against the bounded initial adjoints consequently yields the claimed order-`t^2` motion of every layer's training features. This is a complete argument for the norm lower bound; a vector expansion of all forward feature accelerations is unnecessary.

## 5. Cubic departure from the frozen kernel

The readout part of the label-contracted kernel increment is twice the top adjoint pairing, hence has leading coefficient `t^2 sum_ell E_(ell,n)/k^2`. The hidden tangent-kernel terms have precisely the same coefficient, by `delta_a^(ell)(t) = kt B_a^(ell) + o_*(t)` and the exact squared-force identities. Thus

\[
y^\top[K(t)-K(0)]y
=\frac{2t^2}{k^2}\sum_\ell E_{\ell,n}+o_*(t^2).
\]

The variation-of-constants formula uses the same initial zero prediction and the same coupled initial kernel. Replacing the exponential by the identity and `y-f_n(s)` by `y` costs order `t^4`, since the matrix kernel increment is of order `s^2`. Integration gives the coefficient `2/(3k) = m/3`, with the positive sign in the source. The order-`t^3` prediction gap therefore follows on a training input by division by `||y||_1`, which is nonzero.

## 6. The nonlinear part of the first-layer increment

The pointwise nonaffinity assertion in `compact_feature_learning.tex:291–296` is correct for every pair of nonzero vectors `g,r` in `V`. If `phi_1'(g^T v)(r^T v)` were affine on the sphere, its zero values on the equator orthogonal to `r` force that affine function to be a multiple of `r^T v`. Division off the equator and continuity then make `phi_1'` constant on a nontrivial interval, contradicting analyticity and nonaffineness.

The limiting projected Gaussian row `g` is nonzero almost surely, and positive acceleration energy gives positive probability that `r` is nonzero. The squared distance from affine functions is continuous and bounded by a constant times `||r||^2`. The established joint law with second moments therefore makes its empirical mean converge to a strictly positive constant, with no independence assumption between `g` and `r`.

The bounded-row Taylor estimate and the second-moment tail estimate give the stated `o_*(t^2)` remainder in the joint neuron-and-sphere norm. The weight-expansion error is controlled in that norm by the bounded derivative. Contractivity of orthogonal projection transfers the positive projected acceleration to an order-`t^4` squared nonlinear increment.

## 7. Probability and compression transfer

The dense conclusions hold after choosing common positive constants and a sufficiently small deterministic interval. Positive limiting energies, the positive four-point initial-velocity limit and the fitting event provide probability tending to one. Finitely many layers and witnesses require only a finite intersection.

The supplied vanishing absolute compression errors then transfer both prediction gaps at every fixed positive time by the triangle inequality. This is exactly the theorem's quantifier: no uniform compressed gap over all times approaching zero with the width is asserted. Eventual approximation at every fixed confidence implies convergence in probability, so there is no residual fixed failure budget. The first-layer and every-layer feature claims concern only the dense reference, as stated.

Appending at most four deterministic unlabeled Taylor witnesses preserves all required query coverage. Since `m+p >= 2`, the quadratic panel factor increases by at most nine and the linear data factor by at most three. The declared storage orders are consequently unchanged. No endpoint gap, trained population-flow theorem, bounded activation value, or identification of compressed coordinates with dense neurons is needed.

No correction is required for the new theorem or its shortened proof on the reviewed inputs.
