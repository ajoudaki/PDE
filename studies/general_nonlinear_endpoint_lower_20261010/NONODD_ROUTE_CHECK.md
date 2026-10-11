# Independent check of the nonodd innovation and moment routes

2026-10-11. Independent isolated review of the assigned frozen inputs. This
report checks the paired-query argument, extraction of training moments from
the existing source proof, the resulting two-layer bound, and the specifically
assigned shortcut obstructions. It does not newly certify every lemma in the
existing 1526-line source proof, audit the rest of the manuscript, or prove an
endpoint lower theorem.

## Inputs and verdicts

All six assigned scientific files were read completely. The rigorous-math
skill and canonical-notation skill, including its neural-network reference,
were read and applied. No study README, history, other review, other study,
unassigned dependency, or external source was accessed. The supplied inputs
suffice for these targets; no missing scientific input was needed.

SHA-256 hashes of the final reviewed versions, including the narrow
presentation repairs and setup clarification verified in the follow-up below:

| Frozen input | SHA-256 |
| --- | --- |
| `NONODD_INNOVATION_ROUTE.md` | `0121e871a3c4aa7356a33616948fe87b290b91d118a8eaf60d8737f9f4bb4853` |
| `NONODD_MOMENT_ROUTE.md` | `882de8bf0e33e7d7c6a62cb1afd29d633531ccc7a6b4cdb1942cccef98c4fa93` |
| `PRODUCT_QUERY_ROUTE.md` | `d405d3da64274381272d85a01298da21cf5975c3236345264d6a973412343dfd` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |

The first three paths are relative to this study; the last three are relative
to the repository root.

| Target | Verdict |
| --- | --- |
| Innovation §§1–3: positive paired variance and anti-concentration conditional on the entire active initialization, at arbitrary fixed depth | **PASS**, under the inherited canonical assumptions stated below |
| Moment §§1–3: extraction of all-time training moments from the source-proof exponential budget, with no additional label cap | **PASS as an extraction from the existing source proof** |
| Moment §4: exact two-layer centered scalar consequence | **PASS**, including both numerical coefficients and gap powers |
| Innovation §5: diagonal/envelope information does not bound the relative paired scale away from zero | **PASS** for the stated obstruction to an absolute-error transfer |
| Innovation §6: full conditional feature covariance has no uniform positive matrix lower bound | **PASS**, already at initialization |
| Moment §6: no activation-only energy-normalized fourth-moment bound over the full class; weaker envelope-only obstruction for an all-nonaffine class | **PASS**, with the stated distinction between these two quantifiers |

Two minor presentation defects were found and subsequently repaired by the
author; the corrected passages were verified separately below. Neither changes
the mathematical verdict. These results do not imply the full nonodd
trained-endpoint lower bound under the existing label cap.

## 1. Reconstruction of the paired-query argument

The canonical setup inherited from `compact.tex` includes fixed
\(m\ge2\), \(L\ge2\), normalized training directions
\(\|v_a\|=1\), independent Gaussian initialization, and zero initialized
readout. These assumptions matter: unit norms give common population
diagonals, and \(m\ge2\) makes a constant activation incompatible with
\(Q=Q^{(L)}\succ0\). The final innovation §1 now explicitly recalls
\(m,L\ge2\), the input normalization, and the fixed-problem limit.
This clarification introduces no new assumption beyond its canonical source.

Let \(\mathcal A_n\) contain all initialized first-layer coordinates in
the training span and all initialized hidden matrices. A unit orthogonal
query supplies \(Z\sim N(0,I_n)\), independent of \(\mathcal A_n\).
With the initialized top training-feature matrix \(\mathsf H_0\), put
\(\widehat Q_n=\mathsf H_0^\top\mathsf H_0/n\). The frozen predictor is
exactly

\[
F_n(Z)=\frac1n h_0^{(L)}(Z)^\top
                    \mathsf H_0\widehat Q_n^{-1}y.
\]

Setting it to zero when \(\widehat Q_n\) is singular is sufficient; the
probability of that event tends to zero. Take an independent copy \(Z'\),
with the same active weights. This is a conditional product construction
and requires only one actual orthogonal input direction.

For the common diagonal and off-diagonal recursion \(q_j,c_j\) in
innovation (2), nonconstant activations give
\(q_j>c_j\ge0\). Nonnegativity follows from the squared Hermite
coefficients at correlation \(c_{j-1}/q_{j-1}\ge0\). Strict inequality
follows because the Gaussian pair at the preceding layer has full support:
zero mean square of the activated difference would force the continuous
activation to be constant. A constant activation anywhere would leave the
final training Gram with rank at most one, contradicting \(m\ge2\) and
\(Q\succ0\). This also verifies that each variance in the recursion is
positive.

For the top Gaussian vector \((X,U,V)\), put
\(H=(\phi_L(X_a))_a\), \(T=H^\top Q^{-1}y\),
\(A=(U+V)/2\), and \(B=(U-V)/2\). The two query cross columns agree,
so \(B\) has zero covariance with \((X,A)\) and is independent of it,
even if the latter Gaussian vector is singular. Its variance is
\((q_{L-1}-c_{L-1})/2>0\), while \(A\) has variance
\((q_{L-1}+c_{L-1})/2>0\). Since the nonzero real analytic function
\(\phi_L'\) has a discrete zero set, \(\phi_L'(A)\ne0\) almost
surely. For every such value \(a\), the function
\(b\mapsto\phi_L(a+b)-\phi_L(a-b)\) has derivative
\(2\phi_L'(a)\ne0\) at zero, hence positive squared Gaussian integral.
Finally

\[
\mathbb E T^2=y^\top Q^{-1}y>0.
\]

Conditioning on \((X,A)\) therefore proves
\(V_{\rm pair}=\mathbb E[(\phi_L(U)-\phi_L(V))^2T^2]>0\).
All moments are finite by linear activation growth. The second-derivative
estimate in innovation (5) is also correct: on
\(|B|\le|\phi_L'(A)|/(2\beta)\), integration across an interval of
length \(2|B|\) gives an activated difference of magnitude at least
\(|B\phi_L'(A)|\).

Here is the empirical inverse step independently. Condition on every
initialized layer below the top, including both auxiliary query columns,
and denote the resulting augmented covariance by \(S\). The top rows
\((H_i,U_i,V_i)\) are independent Gaussian transforms. Define

\[
\Delta_i=\phi_L(U_i)-\phi_L(V_i),\quad
Q(S)=\mathbb E_S H_iH_i^\top,\quad
d(S)=\mathbb E_S H_i\Delta_i.
\]

Let \(\widehat Q=n^{-1}\sum_iH_iH_i^\top\) and
\(\widehat d=n^{-1}\sum_iH_i\Delta_i\). The exact difference is
\(F_n(Z)-F_n(Z')=\widehat d^\top\widehat Q^{-1}y\).
The population covariance limit \(S_0\) has \(Q(S_0)=Q\) and
\(d(S_0)=0\). In a fixed neighborhood of \(S_0\), restricted to
positive semidefinite covariances, \(Q(S)^{-1}\) is uniformly bounded.
Conditional Gaussian fourth moments give
\(\widehat Q-Q(S),\widehat d-d(S)=O_{\mathbb P}(n^{-1/2})\)
uniformly there. The inverse identity with a quadratic remainder gives

\[
\begin{aligned}
\sqrt n\{\widehat d^\top\widehat Q^{-1}y
              -d(S)^\top Q(S)^{-1}y\}
 &=n^{-1/2}\sum_i\Psi_S(H_i,U_i,V_i)+o_{\mathbb P}(1),\\
\Psi_S(H,U,V)
 &=\{\phi_L(U)-\phi_L(V)-d(S)^\top Q(S)^{-1}H\}
                         H^\top Q(S)^{-1}y.
\end{aligned}
\]

The unscaled remainder is \(O_{\mathbb P}(n^{-1})\). Its proof uses
products of the two empirical errors and the bounded inverse on the event
\(\|\widehat Q-Q(S)\|\) is sufficiently small; the complementary
probability tends to zero uniformly. The influence has mean zero exactly.
Gaussian square-root coupling and polynomial domination show that its
variance tends to \(V_{\rm pair}\) as \(S\to S_0\), and its third
absolute moment is uniformly bounded. The characteristic-function Taylor
remainder is therefore bounded by a fixed multiple of \(n^{-3/2}\);
taking the \(n\)-th power gives the centered Gaussian limit along every
deterministic sequence \(S_n\to S_0\).

Convergence to a continuous Gaussian distribution gives uniform convergence
of distribution functions. A finite partition with small Gaussian mass
between adjacent points proves this directly, including the tails. The
result is locally uniform in the covariance: a failure would provide a
deterministic sequence of covariances tending to \(S_0\) contradicting
the preceding argument. Thus arbitrary conditional population centerings
are harmless for upper bounds on interval masses. The normal distribution
maximizes the mass of an interval of fixed length when the interval is
centered. Since the empirical lower-layer covariance converges in probability
to \(S_0\), averaging yields innovation (6). This argument neither
asserts an unconditional centered CLT nor conditions Gaussian top-row
independence on \(\mathcal A_n\).

For the final conditioning step, let
\(\nu_n=\operatorname{Law}(F_n(Z)\mid\mathcal A_n)\) and
\(b_n(r)=\Pr(|F_n(Z)-F_n(Z')|\le2r\mid\mathcal A_n)\).
Conditional independence gives
\(\nu_n([a-r,a+r])^2\le b_n(r)\) for every center \(a\).
With
\(c_\delta=\delta^3\sqrt{2\pi V_{\rm pair}}/16\), the annealed bound
gives \(\limsup_n\mathbb E b_n(c_\delta/\sqrt n)\le\delta^3/4\).
Eventually this expectation is at most \(\delta^3/2\), so Markov at
threshold \(\delta^2\) bounds the exceptional active probability by
\(\delta/2\). This proves exactly innovation (9), uniformly over
centers, and its conditional variance consequence (10). The singular
empirical-Gram event is absorbed by its vanishing probability.

## 2. Training moments and the two-layer consequence

Here \(\gamma=\lambda_{\min}(Q)\), \(\lambda=\gamma/m\le1\),
\(Y=\|y\|/\sqrt m\), and \(\beta\) is the activation envelope of
`compact.tex`. The budget coefficients \(\eta_*,S_*\) are the explicitly
defined activation/depth constants in the supplied source proof.

The source proof explicitly defines the budget in `cp:src-budget`, proves
the fixed-order bound in `cp:src-budget-removal`, and verifies the domains
on which it is removed. Its fixed-order estimate is

\[
\limsup_n\Pr\{\text{a full budget is hit}\}
       \le mL(16L/\mathcal B)^u,\qquad
\mathcal B=1024e^2L.
\]

Taking the infimum over positive integers \(u\) after the width limit
makes this zero. The allowance \(S_0=16Y/\lambda\le S_*\) is established
before the moment order, in `cp:src-powers`, solely from
\(Y/\lambda\le\beta^{-30L}\). Thus the extraction correctly uses a
probability tending to one and does not impose a confidence-dependent,
sample-dependent, or further activation-dependent label restriction. The
source argument uses linear growth, retains its conditional trace terms,
and applies its estimates to independently stopped cavity paths; it does
not assume that actual trained coordinates remain Gaussian.

Because the top training carrier equals \(w\), the budget immediately
gives moment-route (3). With \(T=32\log(en)/\lambda\), the fitting tail
in the physical parameter norm gives, coordinate by coordinate,

\[
\frac{\sup_{t\ge T}|w_i(t)-w_i(T)|}{S_0}
\le\frac{\sqrt{n\lambda}}8(en)^{-16}\le\frac18.
\]

Parameter convergence includes \(t=\infty\). Since \(\eta_*\le1\),
the exponential budget for \(M_i=\sup_{t\in[0,\infty]}|w_i(t)|\)
is at most \(2\mathcal B\). Applying
\(x^p\le(p/e)^pe^x\) proves moment-route (6)–(7), including

\[
\frac1n\sum_iM_i^4
\le 2\mathcal B\left(\frac{64}{e\eta_*}\right)^4
                                  (Y/\lambda)^4.
\]

The quoted source powers imply
\(C_4\le\beta^{101L+25}\le\beta^{114L}\) for \(L\ge2\).
The forward subtraction and the source's real-tail carrier subtraction
likewise extend the training preactivation/carrier budget through the
endpoint. Both tail corrections tend to zero after the indicated carrier
normalization. The resulting factor-two budget, fixed moments, and mixed
training-product bounds in moment §3 are valid. None of these statements
extends the budget to passive or mixed-time backward fields.

On a proper training span, restriction to an orthonormal basis of that span
leaves the normalized training vectors, Gaussian active initialization,
first-layer mobility, and training dynamics unchanged. Running the fitting
and finite-list source arguments there produces the required active-measurable
event. The unused query Gaussian remains independent. This justifies the
conditioning used in the scalar consequence.

For the top hidden displacement
\(E^{(L)}=W^{(L)}(\infty)-W^{(L)}(0)\), put
\(b_L=\sup_{x\in\mathbb R}|\phi_L'(x)|\) and
\(H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}\). The exact row update,
sample Cauchy–Schwarz, the feature bound \(2H\sqrt n\), and
\(\int\rho\le2Y/\lambda\) give

\[
\|E_{i,:}^{(L)}\|\le
       \frac{8Hb_L(Y/\lambda)}{\sqrt n}M_i,
\qquad
|E_{i,:}^{(L)}\mathbf1|\le8Hb_L(Y/\lambda)M_i.
\]

These prove both weighted estimates in moment (11), with the stated factor
\(n\) only in the row-sum bound. At two layers, differentiation of
the actual scalar feature difference and Gaussian Poincare give moment
(12), exactly as in `PRODUCT_QUERY_ROUTE.md`. The gradient is square
integrable because both activation derivatives are bounded and the query
features have finite second moments. No outer activation-value bound is
used. For \(L=2\), let \(s\) be the fitting proof's derivative envelope
and \(U_2=2Hs\). Substituting

\[
\|E\|_F^2\le64U_2^2Y^4/\lambda^3,
\quad \|w\|^2\le4nY^2/\lambda,
\quad \|W_0\|_{\rm op}^2\le64
\]

gives the first coefficient \(2\cdot64\cdot4=512\), with denominator
\(n\lambda^4\). The second coefficient is
\(2\cdot64\cdot64=8192\), with denominator \(n\lambda^6\) and
factor \(\mu^2+\sigma^2/n\). Thus moment (13) is correct as written.
It closes the specific fourth-moment gap in the earlier product-query
argument at the \((Y/\lambda)^3/\sqrt n\) scale. It does not give the
stronger readout-energy normalization or compare the entire trained
predictor with its frozen interpolant.

## 3. The scoped shortcut obstructions

### Innovation §5

For \(\phi_\varepsilon(z)=1+\varepsilon(z+\tanh z)\), fixed
\(0<\varepsilon\le1/10\), the strip and derivative bounds permit the
common \(a=1,\beta=16\). The activation is nonodd, nonaffine, and
unbounded. With orthogonal normalized inputs the common mean is one and
\(q_j\ge1\), so the stated diagonal lower condition is satisfied.
Nonconstancy yields \(q_L-c_L>0\). The equal labels
\(Y_\varepsilon=(q_L-c_L)16^{-30L}/2\) satisfy the original cap
exactly and stay fixed as width grows.

For each fixed depth, Gaussian square-root coupling and uniform linear
growth give \(q_j,c_j\to1\) and top features tending to one in each
fixed finite \(L^p\). The expression in innovation (15) therefore gives
\(V_{\rm pair}/e_0^2\to0\). Its denominator tends to four and its
numerator tends to zero, while every fixed member has positive paired
variance. This disproves a positive relative scale supplied solely by the
diagonal condition and common upper envelope. It does not show that the
actual endpoint error fails to become proportionately smaller.

The additional kernel observation is valid. The population scalar kernel
has a power series with nonnegative coefficients, and its constant
coefficient is \(c_L\). Entrywise powers of the input Gram are positive
semidefinite, so \(Q-c_L\mathbf1\mathbf1^\top\succeq0\). For the
orthogonal projection \(P\) onto \(\mathbf1^\perp\),
\((m-1)\gamma\le\operatorname{tr}(PQ)\le m(q_L-c_L)\).
This proves the claimed unweighted bound, without implying the required
weighted lower bound involving \(T^2\).

### Innovation §6

For the specified first activation and softplus second activation, the
strip calculations are correct. Conditionally on the active weights, a row
query preactivation is
\(b_i+\varepsilon\sum_jW_{ij}\eta(Z_j)\), where
\(b_i=\sum_jW_{ij}\) and \(\eta(z)=z+\tanh z\). Oddness of
\(\eta\), \(|\eta(z)|\le2|z|\), and independence give

\[
\mathbb E_Z e^{2\varepsilon\sum_jW_{ij}\eta(Z_j)}
\le e^{8\varepsilon^2\|W_{i,:}\|^2}.
\]

Since softplus is bounded above by \(e^x\) on the real line, this gives
the conditional variance bound (18). With probability tending to one,
some row sum is at most \(-\sqrt{\log n}\), and all row norms are at
most two. The stated Gaussian and chi-square estimates establish these
facts without requiring independence between the sum and norm within a
row. The minimum diagonal variance, and hence the covariance minimum
eigenvalue, is at most
\(e^{-2\sqrt{\log n}+32\varepsilon^2}\to0\).

The chosen two training inputs have a positive definite first-layer
covariance. Full support and strict variation of softplus in either
coordinate prove the final Gram is positive definite. Its gap satisfies
\(\gamma\le4\varepsilon^2\) by the real Lipschitz bound, and its
diagonal is at least \((\log2)^2\) by Jensen. Thus the other displayed
admissibility conditions can hold simultaneously. This refutes precisely
the proposed full-matrix bound, including zero perturbation. It leaves
open a covariance bound evaluated at the actual fitted readout.

### Moment §6

For fixed identity lower layers and top cosine, the parity combination is
indeed

\[
T_k(G)=\cos(G_0/\sqrt2+k\pi/2)
                       \prod_{j=1}^k\sin(G_j/\sqrt{2k}).
\]

The independent sine factors have kurtosis
\((x^2+2x+3)/2>2\), where \(x=e^{-1/k}\). The first independent
factor has kurtosis at least one. Thus the product kurtosis exceeds
\(2^k\). The distinct frequencies \(\{v_\sigma,-v_\sigma\}\)
make the cosine Gram strictly positive definite: restriction to a line
with distinct projected frequencies reduces linear independence to an
invertible Vandermonde system. Choosing \(y_0=Qc\) realizes this
combination as the frozen population readout.

The transfer to canonical training is justified. The fitting displacement,
readout, and residual-integral bounds give, uniformly in width on the
fitting event,
\(w_\infty=\mathsf H_0b+v\),
\(\|v\|_{2,n}=O_{\rm data}(\alpha^3)\), and
\(Q_nb=\alpha y_0+O_{\rm data}(\alpha^3)\).
The Gram gap yields the stated \(O_{\rm data}(\alpha^2)\)
normalized \(L^2\) comparison after division by \(\alpha\).
Bounded cosine and the integrated readout equation give coordinate bounds
for both compared vectors, upgrading it to an
\(O_{\rm data}(\alpha)\) comparison in normalized \(L^4\).
Conditional top-row averaging supplies the empirical second and fourth
moment limits. For any proposed activation-only constant, first choose
fixed \(k\) with a strict kurtosis margin, then choose a fixed positive
\(\alpha\) sufficiently small to preserve it and satisfy the existing
cap, and finally take width to infinity. This is a valid counterexample
for either proposed energy normalization, including the actual endpoint
RMS readout energy.

Replacing the lower identities by \(z+\tau\tanh z\) gives the stated
all-nonaffine obstruction by continuity of finite-panel Gaussian moments
and persistence of the Gram gap. Because \(\tau\) may depend on
\(k\), this part rules out an envelope/depth-only constant, not an
unspecified constant for each fixed all-nonaffine activation tuple. The
note makes this distinction correctly.

## 4. Corrections and remaining scope

Two presentation defects were present in the initially frozen versions:

1. Moment §6, line 422: the complex parity-generating expression needs
   \(2^{-k}e^{iG_0/\sqrt2}\prod_j(e^{itG_j}-e^{-itG_j})\), or a factor
   \(1/2\) inside each product factor. As printed, the division by two
   sits outside the product. Equation (15) and all subsequent moment
   computations use the correct normalization.
2. Innovation equation (19), line 429: `\!left` should be `\!\left`.
   This is a LaTeX delimiter error only.

The initial innovation and moment hashes were, respectively,
`830ee71bdfe1faf99288dd8bab4416e2ba36e47a68344fd25fff685c4e195fc5` and
`8f68d57e035ed94f9d384ad551e0b627e0f7a6a93e9c08f790fa591171dcf399`.
After the author applied these two repairs, a narrow follow-up inspected the
corrected expressions and recomputed the hashes shown in the input table.
The parity expression now has the required \(2^{-k}\) prefactor and the
covariance display now has `\!\left`. Both repairs are correct and close
these findings. No theorem re-review was necessary for these presentation
changes.

A second narrow follow-up verified that innovation §1 now recalls
\(m,L\ge2\), \(\|x_a\|=\sqrt d\), and fixed data and activations
before width increases. The earlier innovation hash after the delimiter
repair was `7405440fe7953e9660ad93ac193a47bb4cc1e92411d273c1c8c653b977387f48`;
the input table records its final hash after this setup clarification.
This resolves the standalone-statement clarification noted in §1 without
altering the proof or its inherited assumptions.

No substantive correction is required for the assigned claims. The
innovation theorem is a frozen-feature conditional anti-concentration
result. The training moments yield a two-layer centered hidden-feature
perturbation estimate, not a full arbitrary-depth passive-query estimate.
Neither result proves a relative endpoint remainder small enough compared
with \(V_{\rm pair}^{1/2}/\sqrt n\) under the original cap. The notes
identify these unproved steps rather than supplying them by Gaussianity,
centering, bounded activation values, or an additional label assumption.
