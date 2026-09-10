# Independent signed-theorem review A, frozen version 1

Reviewer: fresh isolated agent `/root/sign_review_a`. Date: 2026-09-10.

**Verdict: ACCEPT the stated fixed-model local signed theorem.** I found no required mathematical, executable, or numerical correction in this version. This is a scientific acceptance of the frozen study result, not permission to promote it or an assertion that a subsequent book integration has been reviewed. The exact inequalities proved are those in SIGN_THEOREM (S2), with the actual-flow remainder and local consequences in (S1), (S3). The finite-width statement remains convergence in probability on each fixed interval bounded away from zero; it is not a quantitative finite-width theorem or a practical-size claim.

This verdict rests on reading and reconstructing the complete proof chain, a fresh execution of the hash-verified original driver, and an independently implemented exact interval reassembly. A saved positive flag, an old review, and agreement of floating midpoints were not premises.

## Independence, input completeness, and exact coverage

I read only the neutral live assignment, its frozen copy, the full frozen packet and evidence, and the required skills/references. I did not read the live study README/history, author startup material, prior reviews, another reviewer's report or findings, or administrative endings removed from the packet. No other agent supplied mathematical evidence for this review. I did not delegate any mathematical component, modify an input, train a network, sample randomness, change the model or resolutions, or run a second Gaussian coefficient integration. I performed no Git mutation or manual Git command. The explicitly authorized original driver itself performs a read-only `git rev-parse HEAD` for provenance and hashes its original-source README without exposing or reading its administrative content into this review.

The skills read completely were `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's `references/adversarial-audit.md` and `references/decisive-experiments.md`. Initial tool-output truncations were repaired. The read coverage is all 6,031 lines in all 18 packet files, including all scientific lines of the complete dependency units. Detailed packet line counts and SHA256 values appear in the appendix. The dependency coverage includes global nonlinear Section 2 and Sections 3.1–3.4, A.1–A.4, all of C.1, all of C.2, all of C.3, and its final weighted-loss correction. The notation and reading guide were read completely, but their contextual bibliography was not treated as a theorem premise. No external theorem was imported to fill a proof gap.

The manifest identifies the author/assembler group as `root`, `cubic_derivation`, `matching_remainder`, `quadrature_check`, `sign_structure`, `certified_error`, and `certification_engine`; my identity is separate. The manifest SHA256 is:

`133358ebec642bfec1af8b46a2d239e7ef93877a36825c21d08260a58b350bbc`.

Before execution I verified all 625 declared hashes: 14 original study scientific/code sources, 5 original scientific book sources, 18 frozen packet files, and 588 evidence files. Every comparison passed; there were no unlisted frozen packet/evidence files. Original sources were hashed as bytes without importing prohibited live histories. The full path-by-path expected/actual values are retained in `data/generated/two_layer_test_risk/sign_review_v1/reviewer_a/hash_audit.json`. A final source/evidence recheck is recorded separately. All 588 evidence files were subsequently loaded again by the independent numerical auditor; every JSON was parsed, and every production primitive input/output was interpreted and checked. This is programmatic numerical-evidence coverage, distinct from my line-by-line source/proof reading.

The manifest's enumerated omissions are administrative endings in SIGN_THEOREM, CUBIC_DERIVATION, MATCHING_AND_REMAINDER, CERTIFIED_ERROR, CERTIFICATION_ENGINE, and DRIVER_CERTIFICATION; RESULT supplies only the complete relevant movement/nonaffinity proof. The candidate-check preface and a preflight-review historical reference were also removed. PROMOTION_C4 and all code are unabridged. I did not identify a missing scientific input or correction necessary for the claimed implication. The older open-sign language in the baseline reduction is consistent with its conditional role and is superseded only by the new coefficient enclosure.

## 1. Exact model, initial laws, and matching

The stored finite prediction is

\[
f_n(x)=n^{-1}(W_n^{(3)})^\top\tanh(W_n^{(2)}\tanh(W_n^{(1)}x/\sqrt2)).
\]

All three blocks train. Their independent Gaussian entry variances are respectively `1`, `1/n`, and `1/n^2`, and their raw mobilities are `(n,1,n)`. Here `L=2` counts hidden layers, `d=2`, `m=3`. The training angles are `0,pi/5,-pi/5`, and the labels are exactly `1,(1-sqrt(5))/4,(1-sqrt(5))/4`. Mean loss has no factor `1/2`; set `p=y/3`. The teacher is `cos(3 alpha)` with normalized uniform-circle risk. The preserved Gram is

\[
G=\begin{pmatrix}1&c&c\\c&1&q\\c&q&1\end{pmatrix},
\quad c=(1+\sqrt5)/4,\quad q=(\sqrt5-1)/4.
\]

It has rank two because it is the Gram of three distinct unit directions in the plane, while two of these span the plane. No inverse of this Gram is used. The lower tuple is produced by the actual two Gaussian roots; the upper initialization is a Gaussian tuple with covariance `Q_ab=E[tanh(Z_a)tanh(Z_b)]`, not independent Gaussian samples.

The raw finite derivatives give `delta^(2)=W^(3) tanh'(z^(2))`, `delta^(1)=tanh'(z^(1))(W^(2))^T delta^(2)`. The mobilities and the readout factor `1/n` give the population updates with coefficient `-2r_b/3`. The connector update is a rank-one operator `delta_b^(2) tensor H_b^(1)`, with tensor convention `u E[v ·]`. The same connector occurs forward and adjoint. The kernel has first, connector, and readout blocks `G o E[delta^1 delta^1]`, `E[H^1H^1] o E[delta^2delta^2]`, and `E[H^2H^2]`; therefore `f'=-2Kr/3` and `L'=-4r^T Kr/9`. These factors agree in every coefficient proof and the implementation.

The population readout starts at zero. Consequently the full initial tangent kernel equals the readout kernel `K_ab=E[H_aH_b]`. This validates the frozen comparison at population initialization without setting the actual finite random readout to zero.

The bounded ridge-independence proof is sufficient for `Q>0`: commuting finite differences kill all but one nonparallel ridge, and the resulting bounded sequence with vanishing high finite difference must be constant. Full Gaussian support promotes an almost-sure linear identity to an everywhere identity. Since the upper training Gaussian then has full support, varying one coordinate similarly proves `K>0`. In particular `B0=p^T Kp>0`.

The exact frozen residual is `r^g(s)=-exp(-2Ks/3)y`, so

\[
L_g'(s)=-\tfrac49(r^g(s))^TKr^g(s)<0
\]

at every finite `s`, and `L_g(s)` decreases continuously from `L(0)` to zero. The full-flow norm ball bounds the full kernel by `B_K=3(B^4+B^2+1)`, yielding `L_f(t)>=L_f(0)exp(-4B_Kt/3)>0`. Thus matching exists uniquely. With `lambda=lambda_min(K)`, comparison gives `tau(t)<=B_K t/lambda`. The baseline reduction chooses a clock margin `tau(T)<=T_*/2`, then shortens for strict trained-loss decrease and a frozen inverse derivative bounded away from zero. This supplies a genuine common positive local interval.

## 2. Audit of the operative population theorem

The target satisfies every C.1 hypothesis: fixed finite depth/data/dimension, positive weights `1/3`, bounded smooth tanh with bounded first two derivatives, Gaussian first roots and connector, and a readout perturbation with RMS tending to zero. Frozen hidden mobilities are explicitly admitted. C.3's additional Gaussian/nondegeneracy hypotheses hold: positive variances/mobilities, zero population readout, nonzero labels, and pairwise nonparallel normalized inputs.

I checked the construction underlying the theorem rather than treating its statement as an unexplained black box:

* Fixed finite adaptive matrix programs use the exact Gaussian conditional mean and residual projection. Inputs are measurable before their query. Removed output projections have fixed rank and normalized squared size tending to zero. Conditional empirical averaging proves both weak laws and second moments; quadratic-growth tests are justified by the corresponding squared-tail control.
* The source/response law follows by Gaussian integration by parts with coefficient choices held fixed. Adding fresh input roots makes each fixed-program Gram nonsingular; a same-array bounded-action comparison and continuous positive-semidefinite square roots remove that regularization. It does not assume inverse convergence at rank loss.
* The countable compatible union of program laws supplies common layer spaces. Finite matrix operator bounds and adjunction pass to their generated spans and closures. A.1's approximation order allows continuous linear-growth products without assuming uniform cutoff Lipschitz constants. A.2's fixed-program polynomial derivative envelopes handle bounded-gate/unbounded-factor response derivatives without claiming higher-moment control for arbitrary growing programs.
* The preliminary RMS/operator ball and velocity bounds precede the tail argument. In C.2, a single backward source pulse retains its factor `Delta omega_b`. The expected forward derivative rows have bounded row sums, while forward responses have entrywise bounds proportional to that pulse. Weighted-time Jensen controls exponential moments without a maximum over a growing Gaussian history or an independence-over-time assumption.
* The cap choice is noncircular: choose forward caps bottom-up, backward caps top-down, then a short time making the finitely many exponential factors at most two. The construction order uses past fields and already constructed current higher responses. The recurrences yield marginal subGaussian tails uniformly over meshes.
* The localization estimate is linear in cutoff `R`, not `R^L`. Downward propagation multiplies previous errors by bounded gates/operators, adding each new cutoff source. Only a reference trajectory needs exponential tails. This gives the Cauchy estimate with `exp(CRT-cR^2)`, hence existence and uniqueness in the complete field/operator norm space.
* Finite raw GD is compared with a fixed coarse-mesh same-array oracle whose scalar contractions converge. The actual trajectory requires only its norm ball; the tail estimate is imposed on the reference. The order is width to infinity at fixed coarse mesh/cutoff, then mesh to zero, then cutoff to infinity. Thus there is no hidden condition such as `eta_n sqrt(n)->0`.
* Strong chain rules use bounded multipliers and fixed-reference uniform integrability. Derived-velocity cutoffs occur after state stability. The path-law argument uses averaged integrated squared speeds, not per-neuron sup-norm bounds. The finite-GF diagonal follows from every-mesh convergence and fixed-width smooth ODE convergence; finite squared-loss energy bounds prevent finite-time escape.

These facts give precisely the local observable and probe convergence needed here. Passive circle evaluation is obtained from the exact linear representation of its first-layer input by the two training directions, followed by bounded/Lipschitz coordinate operations and the actual connector. A finite angular net and a uniform norm-ball Lipschitz constant turn finite probe convergence into uniform circle/time prediction convergence; bounded predictions transfer it to risk. This does not enlarge the theorem to a growing dataset or horizon.

## 3. Actual-flow cubic coefficient and fourth-order remainder

Use the weighted initial fields of CUBIC_DERIVATION: `S=sum p_bH_b`, `U_b=S tanh'(Y_b)`, `P_b=W*U_b`, `B_b=tanh'(Z_b)P_b`, `T_x=sum G_xb p_bB_b`, `A_x=tanh'(Z_x)T_x`, `M_x=sum p_b Q_xb U_b`, `R_x=M_x+WA_x`, and `E_x=tanh'(Y_x)R_x`. All expectations are within their typed population.

The two conditional matrix uses supply fixed fourth moments. The first gives

\[
P_b=\sum_jh_j[Q^{-1}E(YU_b)]_j+\Gamma_b,
\qquad \operatorname{Cov}(\Gamma)=V=E[UU^T].
\]

The innovation is independent of lower roots and its covariance is the full second moment. Since its mean part is bounded, `P_b` has finite fourth moment. For the next forward action, subtract the projection of `A_x` on the training `h` span. Conditional projection gives a sum of fixed-coefficient Gaussian `Y`, bounded `U`, and a Gaussian innovation with standard deviation `||A_x^perp||_2`. The fixed inverses `Q^-1,V^-1` and Cauchy–Schwarz give uniform fourth moments in the passive angle. The input is known before this query; independence from `Y_x` is neither needed nor assumed.

Directly from the actual readout integral, `||v(t)||_infinity=O(t)`. The hidden velocities are therefore `O_L2(t)`, their increments and the connector increment are `O(t^2)`, and `r(t)=-y+O(t)`. Comparing `v/t` and the backward fields with their initial directions gives `O(t)` errors. The lower gate change has `L4` norm `O(t)` because bounded Lipschitz gates obey `||b(X)-b(Y)||_4<=C||X-Y||_2^(1/2)`. Hölder against the fixed fourth-moment `P_b` closes the lower backward estimate.

Integrating these estimates gives

\[
Z_x^{(1)}(t)-Z_x=2t^2T_x+O_{L^2}(t^3),\qquad
W(t)-W=2t^2\sum_b p_bU_b\otimes h_b+O_{op}(t^3).
\]

The activation step is justified by removing an `O_L2(t^3)` residual by Lipschitz continuity and Taylor expanding only along a fixed `L4` direction. Its Taylor error is bounded by `C t^4 ||direction||_4^2`. It does not assert Fréchet smoothness of the ambient activation map on `L2`. This yields uniformly over the circle

\[
H_x(t)-H_x=2t^2E_x+O_{L^2}(t^3).
\]

For the learned-minus-frozen readout `e=v-w`, exact subtraction retains both residuals:

\[
e'=-\tfrac23\sum_b[(f_b-g_b)H_b+r_b^f(H_b(t)-H_b)].
\]

Together with `f_x-g_x=E[eH_x]+E[v(H_x(t)-H_x)]`, Gronwall first gives `e=O_L2(t^3)`. Substitution then gives `e=(4/3)t^3 sum p_bE_b+O_L2(t^4)`. Consequently

\[
f_t(x)-g_t(x)=t^3J_x+O(t^4),\qquad
J_x=4E[SE_x]+\tfrac43\sum_b p_bE[H_xE_b].
\]

This includes lower-feature motion, learned connector motion, and induced readout motion. The moving residual affects both individual predictors at order two, while its difference term contributes at order four here; dropping it at the outset would not be a valid derivation.

Adjunction gives `E[SE_a]=sum p_b(G_abD_ab+Q_abV_ab)`. Thus

\[
p^TJ=16\mathcal A/3,\qquad p^Ta=2B_0,
\quad \beta=\frac{p^TJ}{2B_0}=\frac{8\mathcal A}{3B_0}.
\]

The loss difference is `-2p^TJ t^3+O(t^4)`, and the initial frozen-loss derivative is `-4B0`. Its inverse gives `tau=t+beta t^3+O(t^4)`, with the required exact leading constraint `p^T(J-beta a)=0`. Expanding the difference of the two squared risks, whose common leading residual is `-cos(3 alpha)`, gives

\[
\Delta(t)=2t^3\int\cos(3\alpha)(J_\alpha-\beta a_\alpha)d\mu+O(t^4).
\]

Uniform angle bounds justify integration and give one finite `M>=1` on one width-independent interval. This is an actual-trajectory remainder, not a formal jet/width derivative interchange.

## 4. Explicit contractions and singular Gaussian laws

For four formally separate slots, including a passive slot with `p_x=0`, Gaussian integration by parts yields

\[
W^*F=\sum_i h_iE[\partial_iF]+\Gamma_F,
\qquad E[\Gamma_F\Gamma_G]=E[FG].
\]

The scalar covariance identity at singular inputs follows either by a Gaussian root representation or regularization; zero covariance directions are also zero `L2` source combinations. Multiplying two such responses and conditioning on the lower roots gives

\[
\Lambda_{ab}(F,G)=L_{ab}E[FG]+
\sum_{i,j}T_{abij}E[\partial_iF]E[\partial_jG].
\]

I checked both derivative formulas, including the passive slot:
`partial_i U_a=p_i d_i d_a+1_(i=a) S dd_a` and
`partial_i(H_x d_a)=1_(i=x)d_xd_a+1_(i=a)H_xdd_a`.
Adjunction then gives the two channels `4 C_x(U_x)` and `(4/3)sum p_a C_a(H_x d_a)` in `J`. The code's training response `M_bj`, its two forward passive-response contributions, and its two reverse derivative contributions implement this full formula. No response mean product is omitted or replaced by an independent matrix.

The independent reviewer program implemented this as a generic full four-slot `Lambda` contraction, not the producer's optimized separation of terms. Its synthetic and actual evidence checks include signed labels, correlated source Gram, `Q/L/T` row-major indexing, the training-only moment dimension, the conditional passive moment dimension, both response directions, and the clock division.

## 5. Analytic error proof and all primitive radii

The one-coordinate strip proof bounds Fourier coefficients after a contour shift by `M exp(a^2/2-a|w|)`. Periodization has an absolutely convergent Fourier expansion, giving the infinite trapezoid error `2M exp(a^2/2)/(exp(2pi a/h)-1)`. Deleted Gaussian tails are at most `2M0 gamma(mh)/(mh)`. Telescoping positive tensor rules multiplies previous-coordinate errors by the actual mass bound `1+2/(exp(2pi^2/h^2)-1)`; it does not assume normalized masses or a simultaneous multicoordinate analytic strip.

On `|Im z|<=pi/4`, the exact formulas give `|tanh z|<=1`, `|tanh' z|<=2`, `|tanh'' z|<=4`. Every source column uses `a c<=3/4<pi/4`, so these bounds apply even when small columns permit a large root strip. The driver verifies rationally `6a/h-a^2/2>=26`, `h^2<=18/26`, and radius at least eight. Exact rational partial exponential sums verify the declared exponential lower bounds. Substitution proves the four-dimensional envelope `5e-11 Mstrip+6e-15 Mreal`; three-root training moments legitimately use this conservative envelope without an extra passive mass factor.

Covariance perturbation uses the interpolation identity

\[
|E_QF-E_{\widehat Q}F|\le\tfrac12\max_{ij}|Q_{ij}-\widehat Q_{ij}|
\sum_{ij}\|\partial_{ij}F\|_\infty.
\]

Adding `epsilon I`, differentiating the positive definite Gaussian density and integrating by parts proves it; bounded continuity passes to zero regularization. I checked the product Hessian constants, including repeated slots, using `|H|,|H'|,|H''|<=1`, `|H'''|<=2`, and `|H''''|<=5`. The needed Hessian sums are `4,6,10,18`. Thus covariance coefficients are respectively `2,3,5,9`. Treating every numerical factor entry as an exact dyadic and forming `Ahat Ahat^T` exactly makes the comparison covariance positive semidefinite regardless of an approximate solve or clipped passive variance. Root smoothness is irrelevant.

Every primitive radius in the producer is the sum of arithmetic `1e-9`, the analytic rule envelope, the tabled covariance coefficient times its certified discrepancy, and any label error. With `P=27/50` and `ep=sum |p-phat|`, the full table checked is:

| Primitive | Strip / real bounds | Covariance coefficient | Label radius |
|---|---|---|---|
| Q | 1 / 1 | 2 | 0 |
| L | 4 / 1 | 3 | 0 |
| T | 4 / 1 | 9 | 0 |
| ES2 | P² / P² | 2P² | 2P ep |
| V, dynamic_V | 4P² / P² | 9P² | 2P ep |
| ddgram, dynamic_dd | 4 / 1 | 3 | 0 |
| ESdd, dynamic_ESdd | 4P / P | 5P | ep |
| dynamic_C | 4P / P | 9P | ep |
| dynamic_Hdd | 4 / 1 | 5 | 0 |
| dynamic_SH | P / P | 2P | ep |

For Q/L/T the discrepancy is the exact lower-input covariance discrepancy; for all upper rows it is the certified Q versus dyadic-root covariance discrepancy. Both exact and rounded label absolute sums are below P. Independent maximal radii and exact discrepancies are retained in `reviewer_a/independent_audit.json`; they range from approximately `1.05001e-9` to `6.45004e-9`. The largest independently calculated upper covariance discrepancy is about `1.05000634e-9`; the lower direction discrepancy is about `1.36717e-16`. These errors are charged before nonlinear contraction and division.

## 6. Angular and computer-arithmetic audit

The angular proof constructs the initial upper Gaussian process as an isonormal image of the lower feature curve. Lower angular derivatives have finite Gaussian moment bounds; Gaussian isometry and moment equivalence supply every required upper `Lp` derivative. Chain/product rules with these integrable bounds justify differentiation of expectations. No passive conditional square root is differentiated.

I reconstructed A6–A9 term by term. The forward channel bounds are
`P^3[l0*u1+3g*l1*u1+g*l2*u2]`, where the last term uses `h_x e_x=-tanh''(Z_x)/2`. The reverse channel bounds are `P^3[4u0+2l0*u1]`. Combining `J=4F+(4/3)B` yields coefficients `20/3,12,4,16/3` in A9, with the separate clock term `2|beta|P u0`. Bell and Stirling recurrences, Gaussian product moment bounds, and Cauchy's radius-3/4 derivative bounds are sufficient through order eight. The fresh exact majorant execution gives

\[
D_8=\frac{41272525446939874982}{31640625},\qquad
\frac{2(8/7)D_8}{256^8}
=\frac{20636262723469937491}{127677049435953561600000000}
<10^{-6}.
\]

This is approximately `1.616286e-7`; the producer uses the larger `1e-6`. Each independently enclosed beta satisfies `|beta|<=1/10`, so the conditional angular bound is applicable. Eight integrations by parts and absolute Fourier summability justify the periodic error. Reflection and antipodal oddness make the full integrand even and pi-periodic; the teacher vanishes at pi/2. The exact 256-node mean therefore has weights `2/256` at zero and `4/256` at indices 1–63. The numerical evaluation need not have exact parity for this enclosure argument.

For arithmetic, the build excludes fast-math and fused contraction. Binary64 radix/significand/size, round-to-nearest, and at least 64-bit long-double significand are checked. The observed platform is x86_64 Linux/glibc 2.35, g++ 11.4.0. Every supplied and returned real is checked/transported as its 64-bit pattern.

I checked the exponential construction without a libm accuracy assumption. Degree-12 Horner on `r/256<=1/4` has initial relative error below `46u`, `u=2^-53`; eight squarings give `(1+46u)^256(1+u)^255-1<2e-12`. Both comparisons were verified again with rational arithmetic. The tanh ratio is Lipschitz in the positive exponential input, its subtraction is bounded absolutely near zero, and the saturation branch above 16 has error below `3e-14`. The global activation error `5e-12` is valid. Dot-product perturbations raise the node activation bound to `6e-12`; the gate bounds `1.3e-11` and `2.6e-11` cover the actual derivative polynomials. At most six activation/gate factors and the signed coefficient absolute-sum bound give the declared pointwise-and-weight contribution below `2e-10`. The only second-derivative factors occur in small products; the real bound `|tanh''|<1` also prevents a hidden product amplification.

The positive exact Gaussian mass is below `1.000001` per axis. Relative weight error and at most four weight products are accounted for. The inner accumulator has at most 401 terms, the outer one at most `401^3`, and `4 gamma_(401^3)(2^-64)<1.5e-11`; I checked this exact inequality. Remaining products/casts and underflow slack keep the full error below `2.2e-10`, within `1e-9`. Ranges exclude overflow. The argument covers the full finite sum, not only final rounding.

The driver's interval endpoints use exact Fraction arithmetic and outward dyadic rounding after every operation. Scalar fractions are multiplied before outward rounding, so small Taylor coefficients are not accidentally quantized away. Reciprocal excludes zero. Machin's identity is justified by its tangent identity and quadrant; alternating-series arctangent remainder and integer square roots enclose pi, sqrt(5), and the normal constant. Taylor remainders enclose all angles and teacher values inside the declared range. Ordinary numerical linear algebra only chooses a root whose exact covariance discrepancy is subsequently bounded.

## 7. Executed computations and exact sign evidence

The fresh original producer command was:

```text
python /home/amir/Codes/PDE/studies/two_layer_test_risk/certificate_driver.py --target 26 --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/certificate_reproduction_20260910_01
```

It completed with exit status zero, 64/64 angles, **30.66773 CPU seconds**, elapsed 30.62135 seconds, and 86,101,134 total upper nodes. The declared full budget was 900 CPU seconds and the per-kernel budget 60; no second coefficient run occurred. Peak recorded Python RSS was 37,828 KiB. The original driver, kernel, and final result SHA256 values are:

* driver: `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1`
* kernel source: `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9`
* compiled binary: `8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7`
* result: `89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`

The final result is byte-identical to frozen production. The independent auditor also verified byte identity of all **322 invariant files**: all 128 primitive input files, all 128 primitive output files, 64 per-angle enclosures, constants, and result. Timing-bearing audit/metadata files were loaded and checked for their proper content and links rather than expected to be byte-identical.

The saved exact coefficient interval is

\[
\left[
\frac{5358604107658561212253567}{19807040628566084398385987584},
\frac{21597479156841685713774185}{79228162514264337593543950336}
\right].
\]

Exact rational comparison places this strictly inside `(27/100000,273/1000000)`. The separately saved clock intersection is

\[
\left[
\frac{2797504526179671494928101665}{79228162514264337593543950336},
\frac{2797556156441557459457527739}{79228162514264337593543950336}
\right]
\subset(35309/1000000,35311/1000000).
\]

For clarity, the raw nodal teacher projection is enclosed approximately by `[0.00043878816447,0.00043880549634]`, and the nodal clock subtraction by `[0.00016720698500,0.00016724779411]`. Their difference, followed by the angular radius, gives the coefficient above. Positive raw projection by itself would not decide this comparison.

The reviewer also executed the two frozen deterministic tests into fresh owned directories, with `PYTHONDONTWRITEBYTECODE=1`:

```text
python .../sign_review_v1/packet/check_certificate_driver.py --output .../sign_review_v1/reviewer_a/driver_check
python .../sign_review_v1/packet/check_certificate_kernel.py --output .../sign_review_v1/reviewer_a/kernel_check
python .../sign_review_v1/packet/angle_error_bound.py --output .../sign_review_v1/reviewer_a/angle_bound
python .../sign_review_v1/reviewer_a/independent_audit.py
```

Here each `...` is `/home/amir/Codes/PDE/data/generated/two_layer_test_risk`. Exact output commands are recoverable from these stated paths and the source/metadata. Driver checks completed in 3.10582 elapsed seconds and kernel checks in 0.79773 seconds; all are far below 60 CPU seconds each. The kernel test compares primitive outputs against an independent rational exponential/tanh oracle and checks small supplied finite tensors against a direct tensor implementation. Its maximum contraction discrepancy was `5.88419e-15`; observed primitive checks were also within their proved envelopes. The direct tensor reference uses numerical NumPy functions and is an indexing sanity check, not a substitute for the analytic rounding proof. The synthetic driver test compares optimized contractions with direct finite response means and checks constants, grid conditions, square roots, and symmetry weights. The singular-root branch is exercised explicitly.

My independent audit program imports no producer module, uses its own 112-bit outward interval class, a longer independently enclosed Machin series and trigonometric recurrence, all raw supplied root bits, all primitive radii, and the generic four-slot contraction. It checked every input's grid, range, exact bit transport, row counts, masses, source/output hashes, and all denominator/beta conditions. The minimum independent `B0` lower bound is about `0.00744965183975777`. All per-node/intermediate intervals overlap the separately valid saved intervals. Its fresh exact final enclosure is

\[
\left[
\frac{702362844149632942196239090521}{2596148429267413814265248164610048},
\frac{353853155230390394383065539151}{1298074214633706907132624082305024}
\right],
\]

approximately `[0.0002705403266745527,0.0002725985550296455]`. It independently satisfies the same strict rational chi bounds and independently verifies the beta intersection bounds. It completed in 3.49325 CPU seconds under an explicit 60-second CPU resource limit.

Two reviewer-scratch diagnostics are preserved, not concealed. The first auditor attempt wrongly treated scalar metadata `long_double_mantissa_bits` as an iterable bit array; this was corrected by restricting array iteration to lists. The second demanded containment of an independently regrouped interval inside the producer's interval; regrouping distributes products and can enlarge interval dependency overestimation (about `5.96e-11` at the first J node). This condition was replaced by the mathematically appropriate overlap check plus an independent final strict-sign proof. These were reviewer-auditor errors, not changes to or failures of the frozen candidate. The logs `independent_audit.log`, `independent_audit_v2.log`, and `independent_audit_v3.log` preserve all attempts. No additional Gaussian integration was involved.

## 8. Hostile checks and finite-time implication

| Target and strongest objection | Discriminator and result | Consequence |
|---|---|---|
| Hidden learning is only faster training | Derive unique inverse-loss clock and retain the `beta a` subtraction; independently subtract its enclosed teacher projection | The positive coefficient is at equal training loss |
| Reused matrix response was replaced by fresh noise | Reconstruct simultaneous reverse covariance and subsequent forward conditional mean; audit every full-slot derivative contraction | Both response directions and mean products remain present |
| Rank-two data or passive collisions invalidate conditioning | Check ridge Gram positivity only for training inverses; use formal slots and PSD covariance interpolation for passive moments | No inverse/passive-root derivative is needed |
| The remainder is merely formal | Reconstruct the actual integral bootstrap and its fixed-direction fourth moments | Uniform `O(t^4)` risk error on a positive local interval is supplied |
| Gaussian tails or unnormalized masses were ignored | Check contour, truncation, tensor telescoping, rational grid inequalities, and every primitive radius | All these sources enter before contraction |
| A circle discretization artifact mimics the sign | Independently check eighth-derivative bound and exact symmetry weights after rigorous beta verification | The added `1e-6` radius covers the omitted circle modes |
| Floating arithmetic or a bad root factor creates positivity | Audit arithmetic proof, input/output bits and exact covariance products; execute one fresh run and independent rational assembly | A positive interval remains after all charged errors |
| Small random readout changes early finite-width orders | Retain the actual finite readout and inspect inverse-loss convergence on `[delta,t0]` | No sign uniform down to zero at finite width is claimed |
| Motion/nonaffinity is being mistaken for useful prediction | Separately audit those activity claims and the signed teacher projection | Activity survives, but benefit uses the new independent scalar sign premise |

The signed conclusion follows without another theorem: for `0<t<=min(T,27/(200000M))`, the actual remainder gives

\[
\Delta(t)\ge t^3(\chi-Mt)
>\frac{27}{200000}t^3>0.
\]

The non-strict lower inequality displayed in the candidate is conservative and valid. Since constant, linear and quadratic differences vanish and chi is strictly positive, the cubic term is the first nonzero matched-risk term.

Finite matching is a separate argument. The empirical frozen kernel tends to positive definite K and the initial residual tends to `-y`; its GF loss is strictly decreasing. For sufficiently small raw step every frozen residual eigenmode has a positive contraction factor, including along affine interpolation, giving a strictly decreasing frozen loss. Uniform finite losses on a fixed `[delta,T]` enter the interior of that range. The population inverse-loss derivative and clock margin bound finite matching-clock errors; circle risk convergence then transfers the sign because the population lower bound has a positive minimum on `[delta,t0]`. This proves exactly the stated convergence-in-probability conclusion for finite GF and every deterministic step tending to zero, with no width rate or moving `delta_n` conclusion.

Finally, C.3's nondegenerate transpose innovation makes `D>0`; each training onset T has a nonzero coefficient in that Gram. Conditional variance remains after projecting A on the initial forward span, so the next forward Gaussian innovation forces the upper onset to be nonzero too. Positive tanh gates preserve activation movement. The Gaussian best-affine-fit error is strictly positive by strict Cauchy–Schwarz, and continuity of moments preserves fixed local positive lower bounds. These establish the stated training-hidden activity and nonaffinity, not order-one motion at arbitrarily small time.

No unresolved fatal, witness-fatal, major, conditional, or minor required correction remains. The ordinary surviving limitation is scope: this one fixed deterministic design/teacher and sufficiently early positive times. The proof does not quantify T or M, demonstrate a practically substantial gain, establish later-time dominance, supply iid sample-complexity/generalization guarantees, or cover growing depth/sample/dimension. Those are outside the exact accepted claim.

## Appendix: packet coverage and immutable hash record

The table and final audit digest below are generated from the read frozen packet and review-owned outputs. They record coverage; hashes are not substitutes for the derivations above.

| Packet input | Read lines | Frozen SHA256 |
|---|---:|---|
| ANGULAR_CERTIFICATE.md | 1–214 | `a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2` |
| CERTIFICATION_ENGINE.md | 1–220 | `1e6fe519f1b69580dbd16d5f6502b9c98ed7ce268b2b27cc318ad4fda640db81` |
| CERTIFIED_ERROR.md | 1–325 | `f3b73f701fb0ce53974b858942ce324f4b62ac002272b93b8273189d7c9742e1` |
| CUBIC_DERIVATION.md | 1–399 | `faf23db85ac2a03f00dd9bd2aa5bf918631982042649b4b84d7cd75721604742` |
| DRIVER_CERTIFICATION.md | 1–244 | `5a16e2e78da438c3b7645d7f014ee3837bc84f20ad8702fa5084df322cd27000` |
| MATCHING_AND_REMAINDER.md | 1–538 | `6b7e9efe4ab6b2c4224df237886e9d573cc9272e6a5830d99201e6732d8bd282` |
| PROMOTION_C4.md | 1–642 | `b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4` |
| RESULT.md | 1–56 | `91fa906514233ed42123e24e634da0d8bce59a6f7f6cbff9e7e099c37ae3580d` |
| SIGN_THEOREM.md | 1–173 | `e78046a220ed618adacaf05348762a5a33cce66c88a388df11f7b181c6182a88` |
| angle_error_bound.py | 1–88 | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| assignment.md | 1–73 | `40774ddaadd44abaa626ad2c4e7ffa63d878cdd1eb186e09afff470e0feb4208` |
| certificate_driver.py | 1–382 | `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1` |
| certificate_kernel.cpp | 1–236 | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| check_certificate_driver.py | 1–140 | `3313df40cbf8170c423d4951bf06aff9733c3260c6d76e01cb3f3d8cee6de989` |
| check_certificate_kernel.py | 1–161 | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| dependencies.md | 1–1777 | `8378046bc80abc06077b34182141d282cf0ba6ac6d7fde6c84e2c6bab5b19db7` |
| docs_NOTATION.md | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs_README.md | 1–265 | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |

The original-source hashes were checked before the reproduction and again after all work:

| Original study source | SHA256 |
|---|---|
| SIGN_THEOREM.md | `18979c2a785b63752e0f3019f0266699f8852055512d566fba1a1c412bbb8a28` |
| PROMOTION_C4.md | `b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4` |
| CUBIC_DERIVATION.md | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| MATCHING_AND_REMAINDER.md | `ebefcae59267dd14a71d4e93e3a287126471f178a42646fe60b5abd45894157d` |
| RESULT.md | `845374726a1a378c3edd922a0e3b9ffc86e60c91cc191013deea96f11f815139` |
| CERTIFIED_ERROR.md | `bcf7fa482d948b73c7ba82b60f514776dbd6d3609a3fb429744aaf507a76c9ad` |
| CERTIFICATION_ENGINE.md | `52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16` |
| ANGULAR_CERTIFICATE.md | `a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2` |
| DRIVER_CERTIFICATION.md | `871a474c95a36790604c882949ad1cd5870d0965fe11d16c3380fa134793f3de` |
| certificate_driver.py | `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1` |
| certificate_kernel.cpp | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| angle_error_bound.py | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| check_certificate_kernel.py | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| check_certificate_driver.py | `3313df40cbf8170c423d4951bf06aff9733c3260c6d76e01cb3f3d8cee6de989` |

| Original scientific book source | SHA256 |
|---|---|
| docs/global_nonlinear.md | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| docs/gaussian_calculus.md | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/README.md | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |

All 625 hashes passed the final recheck. The frozen manifest remained unchanged. The review-owned audit artifacts have these final hashes:

| Artifact under reviewer_a | SHA256 |
|---|---|
| hash_audit.json | `c226533828cd8c7510aa2f9d0c553a721d8eeda1af8b93b3e25fff7ff750e88b` |
| final_hash_recheck.json | `9ac20078ab5b36475fc4b42e25cf89bc4d4921c213589a5f68024bc230ce2641` |
| independent_audit.py | `3676752b44e46bee29408ce800290e76348cf640b34fd725878d4d4e3ce62601` |
| independent_audit.json | `36401c84899e677994270c90368662d742844ba8666b9a92750f5d60617a0049` |
| driver_check/result.json | `707204b58bbc8408f52a87f526b0af1bbd0821081962144c19727c15ed1800d0` |
| kernel_check/result.json | `0da8177f8901e7e54459e64cc3e6bb1b6ae8fd505bf191258203d06544386cb3` |
| angle_bound/result.json | `2a1d5ec88889cbe2f9dd80cd9b4faa7274b727db33a6c37d8c122122662c5f0a` |
| reproduction_stdout.log | `9946df302b07d0c18967cf64cc0c07a52914ddc1819825c2c8f6b00af2f271e8` |
| reproduction_stderr.log | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

| Component | Verdict |
|---|---|
| Fixed model, normalization, and frozen baseline | PASS |
| Operative population construction, convergence, and weighted correction | PASS |
| Actual-flow uniform fourth-order remainder and inverse-loss matching | PASS |
| Complete two-direction Gaussian response contraction | PASS |
| Gaussian tails, strip rule, tensor masses, and covariance perturbation | PASS |
| Angular differentiability, majorants, and exact symmetry reduction | PASS |
| Primitive floating arithmetic, constants, intervals, and bit transport | PASS under the checked arithmetic/compiler contract |
| Complete saved evidence and the one fresh target26 execution | PASS |
| Independent four-slot exact interval reassembly and rational sign checks | PASS |
| Strict finite-time conclusion, finite-width scope, activity/nonaffinity | PASS |

Review complete. The report is original to reviewer A and contains no borrowed verdict.
