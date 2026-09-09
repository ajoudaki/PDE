# Independent complete mathematical audit A2

**Verdict:** The mathematical arguments pass within their expressly stated finite, probabilistic, clipped, and conditional analytic scopes. I found no substantive false claim, missing specialized theorem dependency, normalization error, or invalid probability-conditioning step. The source does require one explicit display correction at candidate line 1509: a literal tab followed by `frac12` must be replaced by `\frac12` (or `\tfrac12`). The correctly rendered descent inequality is proved by the surrounding argument. This report does not certify any uncut population limit, cap removal, autonomous restart, or physical-time/GD/kernel convergence beyond the conclusions actually stated.

## Input contract and identification

I independently read every line of these three scientific inputs, totaling 4,651 lines. Line references below are one-based and refer to these exact snapshots.

| Input | Lines | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_CONTROLS_ADDITION.md` | 4,308 | `6a5c29d04b5efade2d13b5c404fde669933dbece31a6ee68590f1f596887d135` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_CONTROLS_DEPENDENCIES.md` | 245 | `e36cf31741b43271b66b1c21469fcba2dfff6cb170e1a55ac9070cab2465d1e4` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The only procedural source read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`, which names no additional required dependency. I consulted no other project documents, studies, audit reports, verdicts, Git information, external scientific sources, or experimental results. I did not delegate. The only numerical checks were bounded deterministic arithmetic on displayed constants and rational exponents, together with inspection of the malformed source line. I changed no input or Git state; this report is the sole output file.

“Candidate” below means the 4,308-line addition. “Dependency” means the supplied 245-line finite-controls note. Ordinary finite Euclidean and Frobenius norms retain every displayed width factor. Local reused letters have the types assigned in their respective fragments.

## Explicit correction

**A2-1 — Display/transcription defect, low severity.** Candidate lines 1507–1510 intend the raw-gradient descent estimate

\[
\mathcal L(\Theta+hV)\le\mathcal L(\Theta)
-h\|V\|_{raw}^2+\frac12(11000\sqrt n B^9)h^2\|V\|_{raw}^2
\le\mathcal L(\Theta)-\tfrac12h\|V\|_{raw}^2.
\]

At line 1509 the actual bytes contain `+`, a literal tab, and `frac12`, rather than a backslash introducing a fraction. That expression does not render the required coefficient. Replace the tab-plus-`frac12` substring by `\frac12`. This is a necessary source repair, not a change to the theorem, constant, step restriction, or proof: the scalar Taylor remainder for a gradient with Lipschitz constant `11000 sqrt(n) B^9` has coefficient one half, and (E.8) makes the final inequality valid. No mathematical conclusion below relies on treating the malformed letters as a meaningful coefficient.

## Complete coverage map

| Candidate lines | Material audited | Result |
|---|---|---|
| 1–8 | Models, local labels, normalization conventions | Consistent with supplied notation |
| 9–384 | S: Hessian Frobenius bound, all singular-value logarithms, physical Jacobian, initialization, response limitation | Pass |
| 388–857 | I: conditional reused-Gaussian law, empirical convergence, fourth moments, strict curvature positivity | Pass |
| 860–1282 | C: clipped/uncut finite feature flow, remainder, probability and expectation bounds, positive fractions, measurability | Pass |
| 1285–1715 | E: moderate-sine activation, raw estimates, GD/GF energy, weak path tightness, conditional strong endpoint, ambient counterexample | Pass mathematically; A2-1 display repair |
| 1718–2045 | Q2: frozen triangular forcing, effective rank, slow histories, maximum bounds, actual-path temporal premise | Pass |
| 2048–2199 | Q3: complete rectangular martingale concentration proof and its matrix trace dependency | Pass |
| 2203–2426 | Q4: adaptive half-step martingale, exact identities, localization, truncation, quantitative bound | Pass |
| 2430–3264 | Q5: complete noisy recursion, warmups, filtration, two adaptive passes, state/rank/error estimates, edge cases | Pass |
| 3267–3669 | Q6: deterministic clipped comparison, quadrature, filter contraction, memory retention, limits | Pass |
| 3672–3822 | Q7: explicit cap dependence and diagonal growing-cap comparison | Pass with its clipped reference |
| 3825–4308 | G: exact two-matrix transcript law, sequential Gaussian conditioning, innovations, bounded-test transfer | Pass with stated exclusions |

Separating blank lines contain no further claims. Dependency lines 1–245 and notation lines 1–98 were also audited in full, as detailed below.

## Notation and supplied finite-controls dependency

The notation contract distinguishes the stored readout from any rescaled readout, finite transpose from a Hilbert-space adjoint, ordinary norms from RMS factors, and the physical loss clock from an auxiliary discretization. The candidate respects those distinctions. Its one-sample arctangent feature dynamics use block mobilities `(n,1,1,n)` and full-square loss. Its two-sample moderate-sine model separately states the mean-square loss, normalized samples, and the actual raw-GD step. The two samples are never assumed independent merely because their neuron coordinates are Gaussian. The affine population space in E declares its initial operators and its Hilbert–Schmidt increments separately.

Dependency lines 12–85 correctly derive the exact integral representation. Since `F'=1/phi'`, differentiation gives

\[
(X^1)'=(W_0^{(2)}+M_2)^Tb',\qquad
M_2(s)=\int_0^s b'(u)h^1(u)^T/n\,du.
\]

Substituting `M_2` and exchanging the continuous finite-dimensional integrals over `0<=u<=v<=s` gives

\[
R_1(s)=\int_0^s h^1(u)\,b'(u)^T[b(s)-b(u)]/n\,du.
\]

Its derivative is `M_2(s)^Tb'(s)`; the other memory equations and the converse reconstruction follow directly. This confirms that the lower initial transpose takes the primitive `b`, while the lower backward vector still enters `b'`.

Dependency lines 99–143 correctly bound the four query derivatives. With both operator norms and readout maximum at most `B`, the successive RMS derivative bounds are `B^3`, `(c^2+B^2)B^2`, the same bound for `h^2`, `c^2B+BZ_2`, and `c+2BZ_3`. The primitive derivative is at most `B^2`. The last preceding mesh point therefore gives initial-response error at most `B epsilon`, using the initial operator norm at time zero. The supplied path, rather than an implementable causal transcript, is the object being sampled.

Dependency lines 145–190 correctly use integration by parts to remove the difference of primitive derivatives. For the lower rank memory,

\[
e_M\le(B_h+SL_h)e_b+SL_be_h.
\]

For the returned memory, splitting its difference and integrating the second term by parts gives `SL_b e_M+2SL_bB_h e_b`. The top-memory bound follows by subtracting its two rank-one factors. Initial primitive values are zero, so no omitted boundary term appears.

Dependency lines 192–245 correctly identify the limitations. The nonlinear gate difference is bounded by a `2Q` times state-error term plus twice the backward-field tail RMS. The arrays `sqrt(n)e_1` disprove a uniform tail conclusion from RMS boundedness; with `z=e_1` and the other preactivation zero they give gate-product RMS exactly `1/2`. The Hilbert paths `s e_j` lack a strongly convergent subsequence at positive time. The derivatives of `j^{-1}sin(js)v` retain squared time norm `||v||^2[S/2+sin(2jS)/(4j)]`. These are valid counterexamples to proposed abstract inferences, explicitly not canonical-network counterexamples.

## S: full response and squared logarithms

Candidate lines 25–85 use Euclidean coordinates `(z^1,sqrt(n)W^2,sqrt(n)W^3,c)`. The Euclidean gradient of `P=c^Th^3` is exactly the feature vector field, because the hidden matrix blocks are divided by `sqrt(n)` and the prediction is `P/n`. The coordinate metric is `n` times the displayed raw metric; no Gaussian whitening occurs.

The hidden variation maps in lines 116–149 have bounds `1`, `K_2=a+M`, and `K_3=a+MK_2`. Their stated estimates use ordinary operator norms and the fact `||h||/sqrt(n)<=a`. The backward field bounds are `MR sqrt(n)` and `M^2R sqrt(n)`, and the matrix-variation maps have norms at most `MR` and `R`.

The second variation in lines 152–200 contains all three activation-curvature terms and both cross terms from varying a hidden matrix and its input. The three diagonal terms have Frobenius bounds

\[
2M^2R\sqrt n,\quad 2K_2^2MR\sqrt n,\quad 2K_3^2R\sqrt n.
\]

Each cross map has rank at most `n`; bounding its operator norm and then adding its transpose gives `2MR sqrt(n)` and `2RK_2 sqrt(n)`. The off-diagonal readout block costs `sqrt(2n)K_3`. Their sum is exactly the stated `C_B(M,R)sqrt(n)`. No maximum readout coordinate is needed here.

Lines 208–261 prove the logarithmic implication without assuming differentiable eigenvectors. For the full-column-rank transported matrix `V`, the positive definite Gram matrix `G=V^TV` remains bounded above and away from zero on each compact interval. The resolvent derivative of its logarithm is integrably dominated. Trace cyclicity gives

\[
\mathcal E'=\operatorname{Tr}[(\log G)Q^TD_{sym}Q],\quad
\mathcal E=\tfrac14\operatorname{Tr}(\log G)^2.
\]

Thus `|E'|<=2 sqrt(E)||D_sym||_F`. Applying this to `sqrt(E+epsilon)` and then taking `epsilon` to zero proves (S.7), including repeated singular values and `E=0`. Initial isometry gives zero initial logarithmic energy. Taking `D=B` proves (S.3); the count in (S.4) follows by summing at least `r^2` per selected singular value. The embedding may depend on the path because the assertion is deterministic for every isometric embedding on that same path.

Lines 263–330 keep the full physical Jacobian

\[
B_{phys}=2(1-f)B-(2/n)bb^T.
\]

The four gradient blocks give the displayed `K_b^2`; the rank-one Frobenius norm is `||b||^2`, so (S.9) follows with the extra `sqrt(n)` conservatively inserted using `n>=1`. The two sphere nets yield the stated failure probability `4 exp((2 log 9-100/8)n)`. The tiny stored-readout RMS has second moment `n^{-2}`, giving the Markov error `4a^2/n^2`. The successive polynomial bounds `P_3,P_2` prevent finite feature-time escape. Since `f'=||b||^2/n` and the physical residual satisfies its scalar linear equation, an initial prediction of modulus at most one half yields `0<=s(t)<=3t`, and no clock derivative is omitted in the physical response estimate.

Lines 332–384 correctly identify the column embedding and conditional probe covariance. Squared covariance logarithms are four times squared singular-value logarithms. The inequality `Z_i^TZ_i<=2Y_i^TY_i+2I`, eigenvalue monotonicity, and `3+2u^2<=5 max(1,u^2)` prove (S.10), including vanishing singular values of `Z_i`. The example with generator `diag(sqrt(n),0,...)` saturates the logarithmic estimate and has divergent normalized squared amplification. It establishes the insufficiency of this bound for amplitude control, without asserting such a network orbit exists.

## I: the reused Gaussian initialization law

Candidate lines 396–486 specify a nondegenerate Gaussian forward chain and the test class of all continuous functions of at most quadratic growth. The bounds on `g=phi'phi`, `xg(x)`, and the Gaussian variances establish `m_1,m_2,sigma^2>0` and `0<beta<=1`.

Lines 490–558 correctly condition each row of the upper matrix on its forward projection. The orthogonal residual has covariance `(I-P)/n` and is independent of that projection by factorization of the joint Gaussian characteristic function. Multiplying by `g(z^3)` gives the exact conditional law

\[
u_n^{(2)}=_{law}\beta_n h^2+\sigma_n(I-P)\xi.
\]

The coefficient `beta_n` retains the correlation from using the same matrix twice. The zero-denominator event is null and is nevertheless assigned compatible conventions. At `n=1`, the residual projection vanishes as the formula requires.

Lines 560–624 prove convergence of the random variances and coefficients by conditional sample-average variance estimates and bounded continuous functions of the random variance. Division is justified on `m_{2,n}>=m_2/2`, whose probability tends to one; no deterministic finite-width lower variance is assumed.

Lines 628–718 construct an equality-in-law coupling with independent Gaussian vectors. The removed projection has expected squared RMS at most `H^2/n`. The two comparison coordinates form iid pairs with the declared population law, and their mean squared coordinate discrepancy tends to zero in probability. The modulus-of-continuity estimate for bounded uniformly continuous tests is valid without independence of the original coordinates.

Lines 722–814 supply the moment closure needed for unbounded tests: `E beta_n^4<=105`, `E|z_i^2|^4<=3H^4`, and `E|u_i^2|^4<=864H^4`. The last coefficient is `8*105+24`. A compactly supported cutoff has uniformly controlled expected error of order `R^{-2}` because `(1+r^2)1_{r>R}<=2r^4/R^2`. The empirical averages have bounded second moments, so convergence in probability implies the stated `L^1` convergence by the explicitly supplied Cauchy–Schwarz estimate.

Lines 816–857 apply this test class to `[v phi''(z)]_+`. On `1<=Z^2<=2` and the displayed negative independent Gaussian event, the positive part is at least `2/25`. Both event factors have positive probability. Thus the curvature constant is strictly positive and finite, and the expectation convergence is justified rather than inferred from probability convergence alone.

## C: actual small-time middle curvature

Candidate lines 872–974 derive deterministic global finite-feature-time bounds for each fixed dominated 1-Lipschitz scalar clipping, including the identity. The readout grows at most linearly, then the upper matrix, lower backward field, and lower matrix are bounded in that order. The constants `K_3,K_2,J,K` correctly track the operator norms and forward velocities. The finite vector field is locally Lipschitz even if the clipping is not differentiable; bounded states and velocities justify continuation. The proof never differentiates the clipping to obtain (C.5).

Lines 977–1074 differentiate the actual upper transpose response. Its three terms are the trained-matrix derivative, the readout derivative, and the derivative of the top gate. Integrating their bounds gives exactly the powers and coefficients in (C.12): constant initial error `M epsilon`, the integral of `c(epsilon+cs)^2`, the integral of `A(epsilon s+cs^2/2)`, and the integral of `2K_3K(alpha+cs)(epsilon+cs)`. The query is expanded around `s u_n^{(2)}` while retaining the actual tiny-readout error. The curvature comparison uses the 1-Lipschitz positive-part map, `|phi''|<=2`, and `|phi'''|<=8`; the displacement-product term in (C.14) has its required factor `s`.

Lines 1078–1180 correctly import I for the same hidden initialization and provide the extra canonical probability and integrability estimates. On `Omega_n`, `epsilon<=2/n` and `alpha<=2/sqrt(n)`; the unrestricted moment argument uses the polynomials in the pathwise bound, not a discarded bad event. The operator-norm tail bounds every fixed moment uniformly in width. The stored-readout moments scale as `n^{-2k}` for `epsilon^{2k}` and at most `n^{-k}` for `alpha^{2k}`. Cauchy–Schwarz therefore proves (C.22) for the full expectation.

Lines 1184–1254 correctly order the limits. First choose a fixed small `s_0`, then fix any `a>0`; the high-probability lower bound holds simultaneously for `s in [a,s_0]` once the width is sufficiently large depending on `a`. It is not asserted uniformly down to zero at fixed width. The displayed `D` bounds the coefficient RMS by `Ds` when `epsilon<=s`. Splitting the mean at `c_*s/4` then gives the positive coordinate fraction `(c_*/(4D))^2`. This is a scalar-coefficient statement, not a full Hessian eigenvalue assertion. The expectation estimate retains its order-`s^3` uncertainty at fixed positive time and correctly obtains the iterated small-time slope `c_*` without asserting fixed-time width convergence.

Lines 1256–1282 substantiate the rejection of a fifth-order mean positive-part bound and of coordinatewise nonpositivity, while preserving the distinction from actual-response stability. Continuous dependence on initial data and on a fixed map in the compact-open topology follows from uniform local Lipschitz constants on a common finite-dimensional bounded set. Consequently the measurably selected fixed-map expectation clause is justified; the argument does not require an uncountable Gaussian-event intersection.

## E: moderate-sine physical estimates and conditional endpoints

Candidate lines 1289–1320 correctly normalize the activation. Gaussian Fourier moments give the variance `v` of the nonzero component `sin(2G)-2e^{-2}G` orthogonal to `G`. Hence `N>1`, `E Phi(G)^2=1`, and the derivative bounds follow from `a-2b=(1/5-4e^{-2}/5)/N>0`, `a+2b<2`, and `4b<2`. The subsequent estimates use only the stated upper derivative bounds and `Phi(0)=0`.

Lines 1324–1405 correctly derive the raw physical gradient for the two-sample mean-square loss. Each sample-gradient contribution is weighted by its residual once, rather than by a feature-time clock. The field table yields `sum|r_a|<=18B^4`, each raw block velocity is at most `144B^7`, and their sum gives the conservative `576B^7`. The first-layer normalization uses `||x_a||^2=d`; it does not depend on the correlation being nondegenerate.

Lines 1409–1477 correctly propagate raw state differences. Forward constants are `1,2,4B,8B,12B^2,24B^2`; each prediction difference is at most `32B^3 d_0`. Bounding finite coordinate maxima by Euclidean norms introduces the retained `sqrt(n)` in the backward constants `26,28,72,76,160`. Expanding residual, backward, and feature factors gives block constants `3392,3248,2672,944`, whose sum is exactly `10256<11000`. The primal set is convex in the actual raw parameters, so the segment used in the descent estimate satisfies the same bound.

Lines 1481–1531 prove the finite-horizon raw-GD induction at step `n^{-2}`. The provisional raw displacement radius and one-step speed bound keep the entire next segment inside the larger primal ball. After the display correction A2-1, Taylor's estimate gives loss decrease at least `h||V||^2/2`. Summing and applying Cauchy–Schwarz bounds displacement by `sqrt(2khE_0)`, strictly inside the provisional radius. This closes the stop rather than assuming it. Canonical initial predictions tend to zero because, conditionally on bounded hidden fields, their variances are `||h_a^3||^2/n^4=O(n^{-3})`. The sample correlation does not obstruct the separate concentration and finite union bound. The result establishes energy stability, not comparison of GD to continuous flow or a population limit.

Lines 1535–1565 correctly use exact gradient-flow energy to prevent finite-dimensional escape. The forward derivative bounds are valid almost everywhere for linearly interpolated raw weights with hidden fields recomputed. Together with the energy sum they bound the empirical mean squared `H^1` norm of same-layer four-coordinate sample paths. The common `1/2`-Hölder modulus and a dense-time diagonal argument give compact sets in `C([0,T];R^4)`; the `H^1` lower-semicontinuity keeps the closed ball compact. The ensuing empirical-measure tightness is weak tightness in probability. A bounded squared norm alone is not asserted to give uniform integrability or Wasserstein-2 compactness.

Lines 1569–1645 explicitly assume separable population action spaces and bounded initial operators. The backward multiplication is continuous in `L^2`, as the varying query is split from a fixed integrable query and bounded gates permit dominated convergence along subsequences. This supports continuity of all state fields and rank-one Hilbert–Schmidt updates. Scalar prediction differentiability is valid even without Fréchet differentiability of the whole activation map `L^2->L^2`: pairing the remainder `min(|U|^2,4|U|)` with a fixed `L^2` field and truncating that field makes the scalar remainder `o(||U||_2)`. Layerwise telescoping and quadratic operator/feature cross errors give the claimed continuous scalar gradient.

Lines 1647–1691 prove the conditional endpoint statement for an already existing strong flow. The scalar chain rule gives the energy identity, the path is Cauchy at a finite endpoint, and completeness yields a strong raw-state limit. Continuity yields strong limits for the vector field and every layer field. Hilbert–Schmidt convergence controls both operator orientations on converging probes. The extended path has compact `L^2` image, and the displayed finite-cover tail inequality proves qualitative uniform tail decay for that one path.

Lines 1695–1715 correctly show that continuity of the ambient backward multiplication need not be local Lipschitz continuity, despite a positive activation slope. Perturbing the preactivation by a fixed small amount on distant Gaussian intervals where `sin(2z)` remains positive gives an output/input norm ratio at least `2b inf I_j`, diverging. The perturbations tend to zero in `L^2`. This is an ambient-map counterexample, not a claim about reached network states. The endpoint theorem consequently asserts neither existence nor uniqueness beyond that endpoint.

## Q2: frozen forcing and deterministic history compression

Candidate lines 1724–1766 correctly group coefficients of independent Gamma entries. The forward suffix starts at `i`; the reverse suffix starts strictly after `i`. Both output normalizations are retained, including the extra division of the raw reverse perturbation by `sqrt(m)`.

Lines 1768–1813 give the correct positive-diagonal Cholesky factor for a repeated query and the telescoping identity `sum_{i<=l}d_i(a)^2=l/(sigma^2+la^2)`. Inserting this identity gives (Q2.C) with coherent time integration, including the zero first reverse term. For general histories, cyclicity of trace gives `sum||t_i||^2=r_eff`; bounded query norms therefore imply (Q2.D) in both orientations. The statements are for fixed deterministic histories.

Lines 1815–1848 correctly obtain the integrated maximum by pathwise Cauchy–Schwarz and the unintegrated maximum by a Gaussian squared-norm exponential moment. If a Gaussian covariance has trace at most `v^2`, then

\[
\log E e^{\|Z\|^2/(4v^2)}\le\tfrac12,
\]

and `log K+1/2<=log(2K)` gives the factor four in (Q2.F), without independence between query times. The zero-trace case is treated separately.

Lines 1850–1922 correctly handle integer block partitions and rank approximation. Replacing each history block by its first column gives squared Frobenius error at most `K(MT/r)^2`; the effective-rank tail costs at most that error divided by `sigma^2`. Choosing the clipped ceiling of the cube-root optimizer gives `min(K,1+2(KM^2T^2/sigma^2)^{1/3})`, including zero Lipschitz constant and small `K`. Independent additive noises have integrated second moments proportional to `T eta`, and the supplied maximal-submartingale argument proves the factor four for their partial sums. With `K` of order `m^2` and `sigma=m^{-1/4}`, the effective-rank exponent is `5/6`; hence the integrated covariance error is `O(m^{-1/6})` and additive error `O(m^{-5/2})`. The logarithmic unintegrated maximum rates also agree.

Lines 1924–2045 preserve the distinction between independent frozen auxiliary arrays and an adaptive perturbed trajectory. Actual feature paths have uniformly bounded RMS derivatives for `h^1,h^2,delta^3` and `q^2` under the stated primal event. The derivative of `delta^2` contains a product of two RMS-bounded vectors, yielding only the stated normalized `L^1` derivative estimate in the uncut case. Fixed clipping provides the extra coordinate bound and a Lipschitz constant growing with its cap. The explicit mapping into the matrix comparison has `m=n`, `G=sqrt(n)W_0`, `theta=delta/sqrt(n)`, and `omega=h`. No independent Gaussian law is asserted after conditioning on an auxiliary-Gamma-dependent perturbed trajectory.

## Q3: contained matrix concentration proof

Candidate lines 2050–2199 contain the specialized matrix argument needed later; the named outside references are not needed to close its proof.

The positive block matrix with entries `T,I,I,T^{-1}` and its Schur complement give inverse Jensen under `sum U_i^*U_i=I`. Integrating the resolvent expression gives operator Jensen for `-log`. The same resolvent identity proves that log preserves positive-definite order. On the Hilbert space of matrices, the specific operators

\[
T_iX=B_iXA_i^{-1},\qquad U_iX=\sqrt{p_i}\,XA^{-1/2}A_i^{1/2}
\]

satisfy all three algebraic identities in the text. Their left and right multiplication factors commute. Pairing logarithmic Jensen with `A^{1/2}` proves joint convexity of `Tr[A(log A-log B)]`. The elementary scalar inequality for modified entropy, evaluated in the two eigenbases, establishes its nonnegativity. The variational expression for `Tr exp(H+log A)` then gives trace concavity by testing the convex combination of the two maximizers. Thus the crucial matrix trace-concavity dependency is actually supplied.

For bounded centered self-adjoint increments, the scalar exponential power-series estimate gives `log E_{k-1} exp(theta X_k)<=g V_k`, where `g=theta^2/[2(1-theta c/3)]`. Conditional Jensen for the just-proved concavity yields the nonnegative trace supermartingale with compensator `g sum V_k`. Approximation by simple matrices on a compact positive spectral range justifies conditional Jensen. Bounded stopping at the first spectral crossing gives the claimed exponential bound. Choosing `theta=x/(v+cx/3)` produces exactly `x^2/[2(v+cx/3)]`; zero variance or zero increment bound makes all increments zero. Rectangular self-adjoint dilation has the two stated variance blocks and top eigenvalue equal to the rectangular operator norm. This proves (Q3.1) with dimension factor `d_1+d_2`, including its maximum over the finite horizon.

## Q4: adaptive Gram martingale and localization

Candidate lines 2210–2281 specify enough independent primitive randomness and the precise row-before-column filtration. Prefix-consistent positive Cholesky factors make each `t_i,s_i` permanent. The contractions have eigenvalues `d_j^2/(d_j^2+sigma^2)`, so they are at most the identity, their traces are increasing, and each individual column has norm at most one. The fresh row and column vectors have the stated conditional centered Gaussian covariances, making the two half-step rank-one increments martingale differences with finite moments.

Lines 2283–2311 correctly derive the exact Gamma decompositions from

\[
s_j^T\omega_l/\sqrt m=(A_\omega-\sigma^2A_\omega^{-T})_{jl}.
\]

The inverse transpose is lower triangular, so the correction appears only on the diagonal of the relevant column. The strict reverse sum uses `B_{l-1/2}`, not the full-step matrix. Its residual still contains the fresh row, as stated. The Schur-complement formula gives `A_{ll}>=sigma` even for dependent or zero query vectors.

Lines 2346–2386 use predictable permanent stopping before a rank threshold is exceeded. Row acceptance sees the new reverse rank and old forward rank; column acceptance additionally sees the new forward rank. Hence accepted sums of squared column norms remain within their corresponding ceilings. The conditional second moments imply

\[
W_{left}\preceq2R_\omega I,\qquad W_{right}\preceq2R_\theta I.
\]

The histories themselves remain those of the original recursion, which is legitimate for this predictable localization. There is no factor equal to the number of calls.

Lines 2388–2426 truncate each fresh vector by its norm, preserving conditional centering by Gaussian symmetry and reducing both positive semidefinite variance matrices. At accepted steps the covariance has norm at most one and trace at most `r`, giving a tail at `sqrt(2r+4u)` at most `e^{-u}`. The union over at most `2K` steps costs `alpha/2`. Applying Q3 to the truncated process costs the other `alpha/2`: for `L=2sqrt(rv)+(2/3)cv`, expansion gives `L^2>=2v(2r+cL/3)`. On the final rank event and outside both failures, the original and localized/truncated processes coincide. The pointwise query-error estimates follow without conditioning on the final rank event. If both rank ceilings vanish, both Gamma perturbations vanish on that event.

## Q5: the actual causal recursion and its own rank bounds

Candidate lines 2437–2504 distinguish `N` updates from `K=N+1` calls per matrix and fix the parameters `eta=n^{-2}`, `sigma=n^{-1/4}`, `epsilon=n^{-1/8}`. The probability statement is for each deterministic map, including a deterministic width-dependent choice, with uniform constants but potentially different events.

Lines 2508–2634 correctly specify the primitive transform, canonical seeds, independent auxiliary arrays, and all oracle normalizations. Both raw outputs have direct-noise coordinate variance `sigma^2`; normalized errors divide these vectors by `sqrt(n)`. At a zero reverse warmup, `t_1=0` and both Gamma perturbations vanish, but forward direct noise remains. The two exact noisy warmup identities therefore do not assert canonical exact hidden initialization or permit hidden extra matrix calls.

Lines 2638–2763 supply every update and its filtration. The lower reverse argument is the primitive register, the upper reverse argument is the top backward vector, and both forward arguments are selected from the pre-step state. The returned memory uses pre-step `M_2`. Its double-sum expression has the strict inequality `u<i<j`, equivalently the primitive difference `a_j-a_{u+1}`; no diagonal time contribution has been inserted. Positive regularization gives finite measurable Cholesky factors and inverses at every finite prefix, proving finite measurable recursion without any probabilistic size premise. For either matrix, adjoining the other matrix's entire primitive Gamma array to the initial sigma field preserves independence from its own Gamma array. The state at its next call uses only its own preceding prefix, so the interaction does not invalidate the fresh-row/fresh-column conditions of Q4.

Lines 2767–2959 apply Q4 in the exact required normalization. The first rank ceiling `r=n` is automatic. The operator-net failure bound is `4 exp(-(8-2log9)n)` and the stored-readout maximum failure is at most `2n exp(-n^2/2)`. There are exactly `4K` direct-noise vectors. Their maximum event costs `n^{-2}`, and the two initial adaptive applications cost `2n^{-2}` in total. Thus `E_C` has complement bounded by `p_0(n)+3n^{-2}`. Since `u,v=O_S(log(e+n))`, this first pass bounds each oracle output by a logarithmic multiple of its own query norm plus `O_S(sigma)`. The noisy warmup displacements from canonical values have bounds `sigma D_n` and `9sigma D_n`, with no independence after event selection invoked.

Lines 2963–3051 then obtain state bounds in a noncircular order: bounded activations imply bounded readout maximum and top backward RMS; these bound upper memory, then the actual upper reverse output and lower backward RMS by `O(log n)`, then lower primitive and memory by `O(log n)`, then returned memory by `O(log^2 n)`. The filter coefficient `eta/epsilon=n^{-15/8}` lies in `(0,1]`, so target bounds yield register bounds by convexity. The bottom transformed coordinate is bounded only through its displacement from its possibly large initialized value, which is sufficient.

Lines 3055–3181 establish the actual normalized history Lipschitz constants. A common deterministic bound is `M_*=C_*(S)log(e+n)^2/epsilon`. The upper reverse warmup is zero while its first mesh query need not be zero at the same time; the proof explicitly retains the warmup exactly rather than imposing a false temporal bound across this pair. Blocking the remaining `N` columns gives rank at most `d+1` and error `N(M_*T/d)^2`. Projecting onto the approximant's column space proves the effective-rank estimate directly, including when the history has more columns than rows. The integer optimizer and universal ceiling handle all small-dimensional cases. With the prescribed scales,

\[
(NM_*^2T^2/\sigma^2)^{1/3}
=O_S(n^{11/12}\log(e+n)^{4/3}).
\]

Prefix monotonicity then yields the same ceiling at every call.

Lines 3185–3258 apply the second martingale bound unconditionally with that deterministic smaller ceiling. Subtracting its two bad events from `E_C` costs `2n^{-2}`; hence the total failure allowance is precisely `p_0(n)+5n^{-2}`. This step neither conditions the martingale theorem on the first pass nor resamples any arrays. The refined operator bound is

\[
L(r_n)/\sqrt n
\le C_S n^{-1/24}\ell_n^{5/3}+C_S n^{-1/2}\ell_n^{3/2}.
\]

The largest query norm carries one additional `ell_n`, giving `n^{-1/24}ell_n^{8/3}`. The smaller term is absorbed because its ratio is `n^{-11/24}ell_n^{-1/6}<=1`; direct noise contributes `O_S(n^{-1/4})`. The mesh primitive bound is the ordinary deterministic triangle inequality. The `S=0` case in lines 3260–3264 is separately correct: reverse histories and Gamma perturbations vanish, and only warmup noise remains.

## Q6 and Q7: qualified clipped comparisons

Candidate lines 3276–3420 specify a deterministic bounded clipping, the common canonical seeds, noisy warmups, arbitrary adaptive query errors, and `eta<=epsilon<=1`. The reference is an actual finite clipped feature flow; the filtered algorithm has separate algebraic registers. The primitive identity (Q6.4) is obtained by differentiating the exact arctangent transform and retains all learned matrix memory. The error bound is for mesh states in the displayed RMS/Frobenius distance and does not claim derivative convergence.

Lines 3424–3513 first establish bounds independent of cap size by using the dominated clipping and bounded top activation/readout. These estimates do not assume that the filtered and reference states are close. Convex filter updates bound the registers and displacement of `x^1`; finite-dimensional local uniqueness and the sequential primal bounds justify the reference through the entire horizon. Forward, top backward, and ordinary middle-query velocities are uniformly bounded independently of the cap. The clipped lower backward field is time-Lipschitz with constant proportional to `1+R`, using a difference quotient rather than a nonexistent clipping derivative. The five slow right sides therefore have the asserted order-`eta^2` local quadrature errors.

Lines 3517–3619 control the filters in feedforward order. The geometric sum is `eta sum(1-eta/epsilon)^j<=epsilon`, so the three register errors are bounded by the running slow-state error plus query, filter, and warmup errors, with no exponential in `1/epsilon`. The middle query difference depends only on top-layer/readout/memory errors and query forcing. Its lower gate difference adds exactly `2R B_k`. Expanding each slow right side one factor at a time retains the returned memory and gives an ordinary discrete Gronwall inequality. This proves (Q6.9), including its constants independent of width and the initial transformed coordinate magnitude.

Lines 3623–3669 correctly connect Q5 warmups and raw query errors to Q6 for every fixed bounded clipping, and bound the algebraic-constraint discrepancy of reconstructed raw forward fields. For the identity map the necessary estimate retains the product of the preactivation gate difference and the reference backward query. RMS boundedness alone does not produce a width-uniform Lipschitz constant for that product, as the supplied dependency already demonstrates. The filter derivatives include `1/epsilon`, so state convergence alone does not justify their convergence.

Candidate lines 3678–3807 make the cap dependence explicit. The state/operator bounds and filter constants remain cap-independent. Every slow difference and quadrature bound costs at most one factor `1+R`, because only the lower backward field introduces that factor and no product of two backward differences appears. Thus the derived deterministic comparison constant is bounded by

\[
C_{S,M}(1+R)\exp(C_{S,M}(1+R)).
\]

Q5 bounds each orientation separately, while Q6 assumes their sum: the prescribed choice `b=2B_n` in lines 3781–3782 correctly supplies that factor two. The initial warmup error is `O_S(n^{-1/4})`; all other scales satisfy Q6 after finitely many widths. If `R_n=o(log n)`, the logarithm of the full prefactor, including `log(e+n)^{8/3}`, is `o(log n)`. Therefore the error is `n^{-1/24+o(1)}` on the same good events and tends to zero in probability. The sequence implicit in the exponent can depend on the prescribed deterministic cap sequence, as the proof makes explicit.

Lines 3809–3822 correctly limit this to two systems with the same width-dependent clipping. A bound `R_n->infinity` does not even require the chosen maps to approach the identity; the zero map remains admissible. Consequently neither convergence to an uncut process nor existence of a common population limit can be inferred, and the text does not make either inference.

## G: exact coupled transcript law and its consequences

Candidate lines 3836–3920 state both causal rules in raw coordinates. The factors and regularization are the same as Q5. The original rule has the common initialized Gaussian matrix plus the two correctly scaled triangular perturbations and direct noise. The replacement rule is linear in its own independent `Z_for,Z_rev,Lambda` arrays at a fixed history. The reverse term is strict, allowing its forward-history coefficients to be known before the current forward query is selected. The initialized matrices themselves are excluded from the retained joint transcript.

Lines 3924–4010 compute all three covariance blocks at arbitrary deterministic query histories. The forward covariance is `V_omega(l,k)(I+T_min)` and the reverse covariance is `V_theta(l,k)(I+S_(min-1))`, with the strict endpoint in the latter. For the cross covariance, the original rule yields

\[
\theta_k\omega_l^T/\sqrt n+a_{l,k}b_{l,k}^T,
\]

while the replacement yields

\[
\theta_kb_{l,k}^T+a_{l,k}\omega_l^T/\sqrt n.
\]

If `l<k`, the full Cholesky reconstruction gives `b_{l,k}=omega_l/sqrt(n)`; if `l>=k`, it gives `a_{l,k}=theta_k`. These exhaust all cases, including equality, and prove the cross-covariance identity. The Lambda cross term is zero because matching its two indices would require `i=k<=l=j<k`, a contradiction. Independent direct noise contributes `sigma^2 I` to the original full frozen covariance, giving positive definiteness without any query-rank hypothesis.

Lines 4014–4079 supply the needed adaptive conditioning argument rather than incorrectly treating an adaptive output vector as jointly Gaussian. At a fixed previous output prefix, each next coefficient matrix is fixed. Induction maintains a Gaussian posterior on the finite primitive vector, with mean `L^T(LL^T)^{-1}y` and covariance the orthogonal complement of the observed row space. Conditioning the next linear observation and using the block inverse gives the stated next-output mean and Schur-complement covariance. Positive definiteness gives invertibility and ordinary conditional densities; measurability of the coefficients and inverses makes these valid kernels. The possible singularity of the posterior on the primitive space is harmless: each next observed covariance is the positive Schur complement. Matching fixed-history covariance matrices therefore matches the sequential kernels and then the entire transcript law. It does not give a frozen-query norm isometry for adaptively selected coefficients.

Lines 4083–4135 apply this to both interacting matrices in one chronological observation sequence, fixing the independent non-matrix roots first. At a hypothetical transcript, all coefficients depend only on previous outputs, and the two matrices' primitive arrays are independent. Cross-matrix frozen covariance blocks are zero, while the same-matrix blocks just computed agree. These statements remain true for prefixes ending at a reverse call. The entire joint output law, including discarded reverse warmups, consequently agrees, and every computed register, learned increment, and returned memory has the same law. This preserves neither the initial matrix as an observed coordinate nor a pathwise identification of the two realizations. The identity clipping is allowed at this exact finite-law level.

Lines 4139–4246 give a correct enlarged-primitive filtration for the replacement upper reverse call. Its new `Z_l^rev` and Lambda row entries have not appeared in previous calls or the current lower pair. Thus the split into `m_l^{(2)}` and `nu_l^{(2)}` is predictable mean plus conditionally centered Gaussian innovation with covariance

\[
A_{\theta,ll}^2I+\sigma^2\sum_{i<l}s_is_i^T.
\]

The Schur-complement diagonal is at most the current reverse query norm squared plus `sigma^2`. Bounded readout coordinates and bounded activation give the covariance ceiling `(B_4^2+2sigma^2)I`; the displayed scalar moment-generating-function and tail bounds follow. The actual learned upper transpose term has the coordinate bound `(S+1)(pi/2)B_4^2`, obtained from its full rank-one history. The predictable Gaussian-history mean has no bound in this proof. Therefore unconditional Gaussianity, iid query coordinates, or a cap-uniform tail theorem for the full middle query does not follow, and the text expressly says so.

Lines 4250–4308 correctly combine Q7's coupling with Q6's cap-independent middle-query difference estimate. The augmented distance includes mesh states through `N` and queries only through `j<N`, exactly where queries are defined. For a bounded-by-one, 1-Lipschitz test, the good-event discrepancy is bounded by that distance and the bad-event discrepancy by two. Exact transcript equality transfers the all-original expectation to the replacement expectation. This yields (G.22), with the stated failure allowance and constants absorbed into `n^{-1/24+o(1)}`. It remains a bounded-test approximation on changing finite-dimensional arrays; it does not imply convergence to a fixed population law, preservation of conditional laws, transfer of arbitrary discontinuous tail indicators, or unbounded-moment convergence.

## Dependency closure and final scope

The scientific dependencies close inside the permitted material. I uses only its displayed elementary Gaussian conditioning and moment arguments; C imports I for the same hidden initialization. E reuses S's supplied sphere-net estimate. Q2's low-rank and Gaussian maximum estimates are derived in the candidate. Q3 supplies the matrix trace-concavity and martingale-concentration argument needed by Q4. Q4 supplies the two adaptive passes in Q5. Q6 directly proves the clipped deterministic comparison, using the same exact integral memory structure verified in the dependency note. Q7 explicitly extracts Q6's dependence on the clipping cap and checks the Q5 inputs. G supplies its own full covariance and adaptive-conditioning proof, and its final bounded-test transfer uses Q5–Q7 within their scopes. The outside bibliographic links in Q3 are attribution, not an unresolved proof dependency.

All probability events are used with their proper quantifiers. Deterministic C bounds can hold simultaneously over allowed fixed maps because they have a common initial-data envelope. Q5–Q7 and G require each prescribed deterministic map or sequence; their adaptive events are not intersected over all maps. Final-rank events enter Q4 by localization and intersection of failures, never by falsely preserving the original Gaussian law under conditioning. Warmup noise is retained in the state comparison. Finite feature-time assertions are not silently converted to physical-time claims, and the only actual raw-GD statement concerns the separately specified moderate-sine model and its energy estimate.

The negative and limitation claims are appropriately qualified. Positive scalar middle curvature obstructs the specific nonpositivity and fifth-order positive-part claims, not all stability proofs. Squared-logarithmic response control does not bound amplitude. RMS bounds do not imply a uniform spatial tail envelope; temporal regularity does not imply strong infinite-dimensional compactness or derivative convergence. Conditional strong endpoints do not construct new infinite-dimensional solutions. Growing clipped caps do not remove clipping. Exact finite Gaussian transcript laws and bounded-test approximation do not establish an uncut population process, restartability, or kernel/velocity convergence.

**Sealed outcome:** complete mathematical audit passed under the stated scopes, with the single explicit source-display repair A2-1 required. The three input hashes above identify the unchanged material audited; no later correction is included in this verdict.
