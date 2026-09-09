# Isolated adversarial proof audit: Part II

Verdict: **NOTCLEAN**.

The submitted text contains a required correction in the persistent-motion proof: four occurrences of `m` use it as an activation lower bound even though the notation contract and Part II explicitly fix `m=2` as the sample count. Two displayed assertions then directly contradict the activation upper bound. This is a localized, repairable proof error, not a counterexample to Theorem II.1. Replacing those occurrences by `c_-` repairs the affected estimates without changing the theorem or its numerical fitting rate. I found no additional mandatory mathematical gap in the audited Gaussian construction, two-query estimate, finite-algorithm comparison, observation closure, or initial nonlazy expansion. The detailed checks below distinguish that assessment from acceptance of the erroneous submitted statements.

## 1. Provenance, immutable inputs, and read coverage

Audit date: 2026-09-09. This was a fresh isolated audit. The only mathematical sources were:

| Input | Lines | SHA-256 |
|---|---:|---|
| `/tmp/pde-special-reviewed-input.CM1FuJ/special_data_limits.md` | 6397 | `94ad0b6a9ba39e937e1f90626c74c6b9d1f652fe20523dcdf1cdbf780bdfeda0` |
| `/tmp/pde-special-reviewed-input.CM1FuJ/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Line references below refer to this exact chapter snapshot unless explicitly marked `NOTATION`. Inputs were never edited. Hashes were checked before and after the audit.

The mathematical proof-read coverage was:

| Source interval, inclusive | Coverage and use |
|---|---|
| `NOTATION.md:1–98` | Entire notation contract, through EOF. |
| Chapter `1–126` | Entire assigned opening and conventions. |
| Chapter `2087–3498` | Entire Part II, through the end of II.D.5: theorem; II.A.1–3; II.B.1–6; II.C.1–6; II.D.1–5. |
| Chapter `3777–4318` | Entire III.F, including III.F.1–11, through the section end. This includes the finite empirical-law proof, source rule, singular-query regularization, common generated spaces, genuine adjoints, HS integrals, multiplier/curve rules, scalar differentiability, and fixed-cap discussion. |
| Chapter `6376–6397` | Entire final scope section through chapter EOF; its Part II and shared quantifier assertions were checked against Theorem II.1. |

Thus 2102 chapter lines and all 98 notation lines were read as complete assigned/dependent sections. Truncated tool displays were followed by overlapping reads covering the omitted intervals. A navigation search across chapter headings/references and an incidental tail window at `6260–6375` were not used as mathematical premises and do not constitute an audit of Part III.A. No proof was accepted on the basis of search snippets.

Dependency closure for the conclusions reviewed here is the opening, NOTATION, all of II, and III.F. The generic portions of III.F apply directly. Its application-specific references to III.M/S/N/V are not extra premises for this Part II audit: II.B and II.C supply their own cap construction and observation closure, and II.D.5 supplies its own derivative-valid initialization truncation. No Part I result or other Part III theorem was imported.

The procedural `solve-math-rigorously` skill was read to structure the checks; it supplied no mathematical premises. No repository content, history, prior reviews, web sources, agents, numerical experiments, simulations, or computer algebra were used. Tools were used for text/metadata reads, hashes, and writing this review.

## 2. Required issue

### R1. Activation lower-bound symbol is wrong in II.D

Classification: required mathematical/notation correction; localized and repairable. Locations: `3204`, `3221`, `3233`, `3282`. Governing definitions: `2138–2139`, `2343–2344`, `3162–3165`, and `NOTATION:10`.

The model has

\[
m=2,\qquad c_-=5/6,\qquad a=7/6,\qquad c_-<\phi(z)<a.
\]

At `3204` the submitted text claims

\[
\frac12\mathbb E(H^{(1)}_1+H^{(1)}_2)^2\ge 2m^2=8.
\]

But the pointwise activation bound gives

\[
\frac12\mathbb E(H^{(1)}_1+H^{(1)}_2)^2
<2a^2=49/18<8.
\]

This is a direct contradiction, already at initialization, not a missing uniformity argument. The subsequent covariance lower-bound definitions at `3221` and `3233` repeat `2m^2`.

At `3282` the proof says `W^(4)(s)>=ms` pointwise. In the positive-label feature flow, however,

\[
(W^{(4)})'(s)=\frac{H^{(3)}_1(s)+H^{(3)}_2(s)}2<a,
\qquad W^{(4)}(0)=0.
\]

Consequently `W^(4)(s) <= a s < 2s = ms` for every positive `s`. The same contradiction holds for positive-time Euler nodes using the bounded readout update. The stated lower bound cannot be used to prove top-backward covariance positivity.

Required correction, without modifying any model convention:

\[
\begin{aligned}
\tfrac12\mathbb E(H^{(1)}_1+H^{(1)}_2)^2&\ge2c_-^2,\\
c_1&=\min(2c_-^2,d_1/2),\\
c_2&=\min(2c_-^2,d_2/2),\\
W^{(4)}(s)&\ge c_-s.
\end{aligned}
\]

The first and last follow immediately by averaging the two positive features; the middle definitions are then valid positive covariance lower bounds. The constant `b_0=(4/5)c_-s_0 epsilon` at `3293` already uses the correct quantity. In particular, the corrected bounds suffice for every density rectangle, backward positivity argument, and trace-product step downstream. The `min` definitions themselves need not be numerically false for the small constructed `d_j`; the explicit eigenvalue and readout assertions above are false, and the repeated symbol must be corrected consistently.

This finding prevents a CLEAN verdict for the immutable submission. It does not disprove population fitting, persistent nonaffinity, or positive speeds; the supplied proof mechanisms establish those statements once this explicit local correction is made.

## 3. Optional editorial issue

### O1. Undefined `C` in the first-row metric explanation

Location: `2231`. The sentence says `X^T X=dC`, although the input Gram is `G` and the surrounding displayed metric uses `G^{-1}`. Replace `C` by `G`. This is unambiguous from the immediately adjacent formulas and does not require a new argument. Unlike R1, the correct mathematical identity is already used on both sides of the stray symbol, so I classify this as optional editorial cleanup rather than an independent substantive proof gap.

## 4. Normalization, finite geometry, and theorem quantifiers

### Raw storage and loss clocks: checked

The first storage change is linear: `V^(1)=W^(1)/sqrt(d)`. Therefore

\[
\frac d n\|\Delta V^{(1)}\|_F^2
=\frac1n\|\Delta W^{(1)}\|_F^2.
\]

For `f_a=(W^(4))^T h_a^(3)/n`, the derivative with respect to `V^(1)` is `delta_a^(1)x_a^T/n`. Multiplication by the inverse metric `n/d` gives `delta_a^(1)x_a^T/d`. The middle and readout gradients are respectively `delta_a^(ell)(h_a^(ell-1))^T/n` and `h_a^(3)`. Thus the summed squared-loss updates in II.A have the correct factor `-2r_a`, the first preactivation update has exactly `G_ba`, and all four kernel blocks in II.A.2 have the correct normalization.

For the first block,

\[
\frac d n\left\langle\frac{\delta_a x_a^T}{d},
\frac{\delta_b x_b^T}{d}\right\rangle_F
=G_{ab}\frac{\delta_a^T\delta_b}{n}.
\]

For a middle block, the ordinary Frobenius pairing of the two normalized outer products is the product of the two normalized within-layer vector pairings. This is also why the kernels are positive semidefinite even if individual entries of `G` are negative. The physical identities are `dot f=-2Kr` and `dot L=-4r^T Kr`; they are flow identities, not exact discrete prediction updates.

The common mean loss at two samples is half the Part II loss. Accordingly the same iterates have mean-loss step `2n^{-2}` and mean-loss time `2t`, as stated at `76–96`. The theorem's actual step is `n^{-2}` for summed loss. There is no hidden factor-of-two clock change.

The zero-readout program is an auxiliary reference. The actual finite initialization retains readout variance `n^{-2}`; its RMS is `O_probability(n^{-1})`, the discrepancy used in II.C.4. It is not an order-one stored readout.

### First-row reduction, including the antipodal endpoint: checked

For `-1<rho<1`, the in-span first-row variation with sample values `(v_1,v_2)` is `(v_1,v_2)G^{-1}X^T/d`, whose squared raw norm is `(v_1,v_2)G^{-1}(v_1,v_2)^T`. The full-row reconstruction in II.C.r1 therefore restores both values and preserves the initialized orthogonal component. The norm-equivalence constant may depend on the fixed `rho`; no uniformity as `rho` tends to an endpoint is claimed.

At `rho=-1`, equal input norms force `x_2=-x_1`, hence `Z_2^(1)=-Z_1^(1)`. Multiplying the first-update formula by the two opposite inputs shows the constraint is preserved. The first tangent norm is the single-field `L^2` norm, and II.C.r2 reconstructs its first row. No inverse of the singular two-by-two Gram is used there. Adding the full initial row to the root tuple respects III.F.1: within-tuple dependence is allowed.

### Symmetry and fixed quantifiers: checked

The reflection in II.A.5 exchanges the two inputs and is an isometry of the first metric. The optional readout sign gives the stated label/readout symmetry. At finite width it proves equality in law, not equality of a realized pair of predictions. II.C.3 obtains deterministic scalar limits first and only then infers equal limiting predictions. This removes the potential invalid inference from symmetric random laws to pointwise equality.

The actual proof can use this deterministic-limit symmetry without constructing explicit involutions `J_ell` on every population. The conditional involution discussion in II.A.2 is not needed as an additional premise for the main result. Exchange also applies to the differentiated finite observation programs, giving equal limiting sample speed norms later.

The theorem fixes the dataset, `rho`, depth three, activation, and each finite physical horizon before width tends to infinity. It does not state uniformity in `rho`, an increasing horizon `T_n`, finite-width convergence of infinite-time optimizer endpoints, or global opposite-label depth-three dynamics. The opening and final scope agree on this. The broader label identities and short feature-time estimates do not silently enlarge the global equal-label theorem.

## 5. Complete III.F dependency audit

### Finite empirical laws and adaptive conditioning: checked

III.F.1 permits any fixed finite root tuple and any fixed finite number of adjacent independent Gaussian matrices. Part II uses three layer types, two matrices, and a Gaussian bottom pair, optionally augmented by its full first row. The singular antipodal pair has finite second moment and iid neuron tuples, exactly as required. The theorem is not restricted to Part III's three-sample application.

The norm bound in III.F.2 follows from a `1/4` sphere net with at most `9^n` elements and a Gaussian tail for each bilinear form. The union bound has exponent `2n log 9-100n/8<0`; a finite union covers both matrices. No limiting spectral theorem is imported.

In III.F.3, conditioning on the entire transcript makes each next query input measurable and fixed. A coordinate operation adds no randomness. A new matrix answer conditions only that matrix's residual factor; other residual factors remain conditionally independent. This justifies the Gaussian conditioning for adaptive reuse. The proof does not pretend that query inputs are unconditionally independent of the queried matrix.

For constraints `WV=Y` and `W^T U=Q`, compatibility is `U^T Y=Q^T V`. The stated mean `M` satisfies both constraints and is Frobenius-orthogonal to the homogeneous space `P_(U-perp) K P_(V-perp)`. Gaussian projection thus gives the displayed conditional law. For a new forward input, the coefficient of the old reverse inputs is `(U^T U/n)^{-1}(Q^T h_perp/n)`; the fresh variance is `||h_perp||^2/n`. These factors match II.B's normalization.

With nonsingular limiting query Grams, contractions converge by induction, and fixed-size inversion is continuous. Removing the projected noise costs normalized mean square `rank(U)/n`; the rank is bounded by the fixed transcript length. Conditional fresh coordinates are independent, so a bounded test's empirical variance is `O(1/n)`. Expanding the new square gives a cross-term conditional variance of order `||m||^2/n^2` and Gaussian-square variance `2/n`. This proves weak and second-moment convergence. The finite-dimensional `W_2` bridge in III.F.1 explicitly uses tail control, not just bounded second moments.

### Source responses and singular supports: checked

For a new forward query, the old reverse output is `q_s=zeta_s` plus a deterministic combination of old forward inputs. Orthogonality of `h_perp` to those inputs removes that response in `E[q_s h_perp]`. Gaussian integration by parts then gives

\[
\mathbb E[\zeta h_\perp]
=G_U\mathbb E[\nabla_\zeta h_\perp].
\]

The input is a fixed finite composition of bounded-derivative coordinate maps and deterministic linear responses. Its source derivatives are bounded by finite deterministic constants and its growth is at most linear. Conditioning on the independent roots and other source groups therefore matches the integration-by-parts hypotheses. Substitution cancels the derivatives of the least-squares projection. The remaining new Gaussian has covariance `E[h v_r]` with old forward sources and variance `E[h^2]`. Reverse calls follow by interchanging the layer roles. Both orientations' answers remain dependent through responses despite independent primitive source groups.

III.F.5 handles singular query Grams by adding a distinct independent Gaussian input of amplitude `varepsilon` at each call. Its conditional squared distance from the old query span has limiting contribution at least `varepsilon^2`; this gives positive definite perturbed Grams. Same-width program errors are `O(varepsilon)` on the norm event because the transcript is finite and every coordinate instruction is Lipschitz.

The scalar removal argument uses continuity of covariance square roots, not continuity of pseudoinverses. Node expressions have a uniform linear-growth envelope and bounded source derivatives over each compact coefficient set. Coupling finite source prefixes by square roots gives `L^2` value convergence; bounded continuous derivatives give convergence of their expectations. The induction is causal, so compact coefficient bounds follow one instruction at a time. The width limit followed by `varepsilon` removal proves the full-sequence claim.

Formal source slots of zero variance are retained. The kernel-nullspace argument at III.F.14 shows that changes of derivative representatives on a singular Gaussian support cancel after contraction with the corresponding input tuple. This is essential at initialization in II.B, where a reverse source has zero value but its formal derivative need not vanish.

### Feedback and common actions: checked

III.F.6 first fixes the causal deterministic oracle coefficients and then compares actual empirical feedback against them using normalized Cauchy–Schwarz. Part II's learned contractions and Euler coefficients fit this scope: they use finitely many already available second moments, with no singular divisions. No theorem is applied directly to the `O(n^2)` actual GD transcript.

III.F.7 builds a countable union of finite programs and uses the deterministic limits of finite unions for consistency. Same-layer generated cylinder functions are dense in `L^2`; the supplied smooth family and truncation justify that density. Passing the finite norm bound and zero linearity errors to limiting second moments defines well-defined bounded linear actions on the dense span, then on its completion. Passing exact finite transpose pairings and using density proves that reverse actions are the actual adjoints. Countability avoids an unproved simultaneous assertion over arbitrary finite-width adaptive vectors.

Arbitrary fixed real coefficients and needed Lipschitz instructions are included through the stated approximation/`L^2` closure. This is sufficient for the fixed cap and mesh programs in II, and for the finite generated probes in the theorem. It is not a cross-width operator-norm convergence statement.

### HS and differential calculus: checked

III.F.8 proves the rank-one HS identities and completeness. With the finite normalized layer pairing the rank-one matrix is `uv^T/n`, and its HS norm is its ordinary Frobenius norm. Therefore learned increments belong to the claimed affine raw Hilbert space even though the initialized actions need not be HS.

III.F.9's multiplier lemma splits off the strongly convergent `L^2` factor and truncates one fixed old factor in the remaining term. It does not infer uniform integrability from bounded `L^2` norms. The curve chain rule uses boundedness and continuity of `phi'`, strong convergence of difference quotients, and this multiplier argument. It makes no false global `L^2`-valued Fréchet-differentiability assertion.

The scalar derivative proof in III.F.10 applies to the shifted arctangent without rescaling: choose every layer function to be `phi`, use `w=sqrt(d)V^(1)` and normalized inputs `x_a/sqrt(d)`. Both derivatives of `phi` are bounded. At each backward step a fixed `L^2` weight multiplies the scalar Taylor remainder; its truncated part costs `C M ||q||_2^2` and its tail costs `C ||v 1_(|v|>M)||_2 ||q||_2`. This is `o(||q||_2)`, first taking the small increment and then removing `M`. Action cross terms are quadratic because HS increments bound operator increments. The downward expansion and genuine adjunction identify continuous scalar gradients.

The generic Picard/Euler argument in III.F.11 has the usual bounded-ball hypotheses. For Part II the needed local Lipschitz field is proved separately in II.C.1 on the closed, pointwise-bounded readout path class. The Part III.S-specific opening of F.11 is not being applied to uncapped Part II products.

## 6. II.B two-query bootstrap

At fixed caps all update coordinate maps admit the claimed bounded-derivative extension; in particular the readout is bounded by `aS` pointwise. Unrolling the learned matrices gives the factor `Delta/2` in both forward and reverse learned responses. All sample correlations stay in the input second moments. Primitive groups are independent, while each group's time/sample covariance can be singular.

The current construction order matters: `A^(2), Z^(2), A^(3), Z^(3), delta^(3), B^(3), q^(2), delta^(2), B^(2)`. Current `U_k` is not used to prove itself. Zero-time forward-source derivatives vanish because the zero reverse input is multiplied by `tau(0)=0`; the reverse-source derivative of that same expression is retained.

For a single bottom reverse source, direct injection into a later first preactivation is at most `Delta epsilon/2`. The linearized update has coefficients `|q|/5` on the gate variation and `1/10` on the query variation. The latter contributes another factor `1/10` through `H=phi(Z)`. Thus the exponent in II.B.6 is `Delta sum(max_a |q_a|/5+U_r/100)`. The two-sample update has total absolute coefficient at most one, not two. Multiplying by the outer feature gate gives `Delta/200`.

With past `V_r<=1`, the upper reverse norm is bounded by

\[
Q_0=aS/10+a\le161/120.
\]

The lower reverse source variance is at most `(Q_0/10)^2`. The bound on the exponential of the maximum of two absolute Gaussian coordinates uses a sum of two half-normal bounds and needs no independence between samples. Jensen over time needs no temporal independence. This gives `E E^(1)<6` and hence

\[
|A^{(2)}|<\frac\Delta2\left(\frac{49}{36}+\frac3{50}\right)
<\frac{3\Delta}{4}.
\]

For the middle total forward-source row there is one direct identity contribution per output row. Summing the two update samples cancels the `1/2`; it does not create another factor two. The stated exponent bound is

\[
\mathbb E(E^{(2)})^p
\le4\exp\left(\frac{219p}{400}
+\frac{3969p^2}{1280000}\right).
\]

Its `p=1` and `p=2` consequences are respectively `<8` and `||E^(2)||_2<7/2`. They give

\[
|A^{(3)}|<\frac\Delta2\left(\frac{49}{36}+\frac3{25}\right)
=\frac\Delta2\frac{1333}{900}<\frac{3\Delta}{4}.
\]

The top gate/readout differentiation contributes `S/100+aS/5=(73/300)S`. Its past recursion bounds the top derivative row by `exp(657/800)<5/2`. Adding the learned covariance row gives

\[
V_*\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}<1,
\qquad
Q_*\le\frac7{40}+\frac76V_*=\frac{24829}{19200}.
\]

Cauchy–Schwarz for the current middle derivative uses the already established `L^2` bound on `E^(2)`, giving

\[
U_k\le\frac72\left(\frac{Q_*}5+\frac{V_*}{100}\right)
+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}.
\]

These constants and sample factors check. The learned covariance term has exactly `S Q_*^2/100`, with `S<=3/2`.

Finally each actual reverse query is `zeta+beta`, with `|beta|<=a` and source variance at most `(7/40)^2`. No independence between `beta` and `zeta` is needed for `(zeta+beta)^2<=2zeta^2+2a^2`. The Gaussian square integral yields the stated exponential bound below two. This controls both problematic query multipliers, not only the top one.

## 7. Construction, cap removal, physical restart, and fitting

The cap field has bounded readout growth, then bounded top-operator growth, then bounded middle-operator growth, and finally bounded first-field speeds. This order gives cap-independent primal bounds. For two states, only the reference readout must be bounded pointwise when splitting `Wout_A phi'(Z_A)-Wout_B phi'(Z_B)`. The middle clipped product costs `C(1+R)d`. At the bottom the existing query difference has a bounded gate coefficient, while the new gate-difference term costs `R`; these costs add, so the Lipschitz coefficient is linear in `R`, not quadratic.

The zero-readout Picard integral preserves `|Wout(s)|<=as` in a closed path class. Together with the enlarged primal ball this provides a complete contraction domain on a short interval. The primal bounds permit continuation. At fixed cap, Euler defects are quadratic in the mesh and accumulated errors linear, uniformly in width on the initial norm event. Applying III.F only to a fixed coarse transcript and then refining establishes the fixed-cap limit.

The asymmetric two-tail estimate II.C.3 splits each product at the reference state. It requires tails of the reference `q^(2)` and clipped-middle `q^(1)` only. From `E exp(q^2/16)<=2`,

\[
\mathbb E[q^2\mathbf1_{|q|>u}]\le64e^{-u^2/32},
\quad
\|(|q|-R/2)_+\|_2\le8e^{-R^2/256}.
\]

Summing four query tails gives `epsilon_R=32 exp(-R^2/256)`. Fatou is used after strong fixed-cap Euler convergence; it gives a uniform bound on each time's expectation, not an unjustified exponential moment of the time supremum. The per-time bound is exactly what the integral comparison needs.

Gronwall costs `exp(CR)`, which is beaten by `epsilon_R`. It makes cap states Cauchy, and the same product splits give convergence of the actual uncut backward fields and directions. Rank-one differences also converge in HS norm. The limiting integral equations therefore define a strong uncut feature flow on all of `[0,3/2]`.

A bounded-primal uncut competitor can be compared with the same capped reference without a tail bound for the competitor. Starting at a reached time only adds an initial reference error of the same `exp(CR)epsilon_R` type. Another finite `exp(CR)` factor still vanishes. This establishes the stated reached-state restart, not arbitrary-state global well-posedness.

For equal positive labels, scalar differentiability and symmetry identify the feature field as `grad g`, with

\[
g_s=\|\nabla g\|_{\rm raw}^2
\ge\mathbb E\left[\left(\frac{H_1^{(3)}+H_2^{(3)}}2\right)^2\right]
\ge c_-^2=25/36.
\]

The continuous bounded gradient gives a unique crossing `s_*<=36/25<3/2`. If `B` bounds `g_s`, then `1-g(s)<=B(s_*-s)`, so the reciprocal clock integral diverges. Hence `s(t)<s_*` at every finite physical time, and the physical solution exists for all time. Its residual satisfies

\[
(1-g)_t=-4g_s(1-g)\le-\frac{25}{9}(1-g).
\]

The claimed `1-g<=exp(-25t/9)` and summed-loss bound `2exp(-50t/9)` follow. The negative-label sign flip preserves these norm statements.

Physical uniqueness is not restricted to symmetric competitors: II.C.3 compares their full loss vector field with the time-changed capped reference, absorbing both residual components through prediction differences. The reference's discrepancy from a true cut-loss path is itself `exp(CR)epsilon_R`. The same cap removal works on every fixed physical horizon and from every reached full state. This avoids circularly assigning a symmetric clock to an arbitrary competitor.

## 8. Actual finite GF/GD and off-mode comparison

The comparison path is the same-width, zero-readout capped feature flow evaluated at the deterministic population clock. Its two predictions approximate the two population predictions separately. Consequently the residual error decomposes into the actual/reference prediction discrepancy and the reference/population discrepancy for each sample. This controls the off-mode residual directly; no finite pathwise equal-label identity is used.

At fixed cap the quadratic tail functional is continuous under `W_2`. The fixed-cap query time modulus promotes convergence to a uniform-in-time tail bound. These are empirical tails of the actual reused query outputs. They are not replaced by hypothetical iid trained Gaussians.

The actual GD update is exact Euler in the raw parameters. The reference has a local defect `C_(R,T)eta_n^2`: its fixed-cap field is Lipschitz and `s''=-4g_s(s)s'` is bounded and continuous on a fixed horizon. Thus the global reference-defect term is `C_(R,T)eta_n`. With the initial RMS readout discrepancy, Gronwall gives exactly the structure of II.C.8.

The order of limits is essential and correct: fix `R`, send width to infinity (including the actual `eta_n=n^{-2}`), then send `R` to infinity. All cap-dependent finite-program and Euler constants are fixed in the first limit. The surviving `exp(C_T R)epsilon_R` terms vanish in the second. There is no diagonal long-transcript Gaussian theorem.

The stopping argument uses primal bounds one unit beyond the bounded reference. Raw speed is bounded before the stop by operator/readout norms and bounded gates/features. The step into the first bad node overshoots by at most `C eta_n`, so the stopped estimate still applies at that endpoint and contradicts exit once the error is small. Finite GF also has an independent global energy argument: integrated squared raw speed is bounded by the initial loss, and Cauchy–Schwarz makes the path Cauchy at any finite endpoint, where finite-dimensional local smoothness continues it.

Within a raw GD step, vector RMS and operator displacements are `O(eta_n)`. A vector coordinate displacement is therefore at most `O(eta_n sqrt(n))`. Bounded `phi''` controls the gate changes in supremum norm, and multiplying by RMS-bounded direction fields gives the stated recomputed-velocity error. At `eta_n=n^{-2}` this is `O(n^{-3/2})`. The same reasoning covers the prescribed right-node and terminal-left derivatives. A nonlinear change of coordinates is never substituted for exact raw GD.

Comparing GF and GD to the same finite reference, then using fixed-cap laws, proves joint convergence in probability along the full width sequence. The argument is stronger than a choice of convenient width subsequences, although almost-sure subsequences can legitimately be used within individual Fatou/compactness steps.

## 9. Kernel, velocity, product, path, and parameter bridges

The extra details in II.C.6 are necessary and adequate. For an already identified incoming `L^2` field `P`, the product `phi'(Z)P` is first replaced by `phi'(Z)tau_M(P)`. At fixed `M` its coordinate derivatives are bounded. The error is controlled by the positive-part tail of `P`, a Lipschitz functional of its `W_2` law. Thus the finite empirical tail converges at fixed `M`, and its population value vanishes as `M` increases. Operator norm bounds transfer this error to the next layer.

The ordered observation induction keeps outer caps fixed while removing inner caps. It therefore never invokes III.F's bounded-derivative theorem directly on an unbounded velocity or backward product. No arbitrary derivative identity for an unbounded observed product is needed just to identify values and second moments.

For velocities, the recursion is

\[
P_\ell=\dot W^{(\ell)}H^{(\ell-1)}+W^{(\ell)}U_{\ell-1},
\qquad U_\ell=\phi'(Z_\ell)P_\ell.
\]

Truncating only the reference multiplier bounds the new gate error by `C M` times the forward state discrepancy plus a reference velocity tail. Propagated earlier velocity errors have bounded coefficients; they are not multiplied by another `M`. This explains the linear `1+M` bound in II.C.o2 and prevents a hidden cap-growth loss. The analogous downward argument controls true backward fields.

A continuous population velocity curve is compact in `L^2`. Covering it by finitely many `L^2` balls and using the Lipschitz tail functional gives uniform tail removal. II.C.6 first transfers this to population coarse Euler velocities and then to finite cap-flow velocities. After the physical time change it removes the training cap at fixed observation cap, then removes the observation cap. This order avoids multiplying an uncontrolled, cap-dependent high-moment constant by a small state error. Bounded population actions on `L^p` for `p>2` are not assumed.

The four kernels need only the identified second moments. A middle kernel entry is a product of two scalar within-layer contractions; it is not an expectation of an unbounded four-factor same-neuron product across layers. Likewise a cross-time HS rank-one pairing is `E[U_t U_s] E[V_t V_s]`, with separately typed layers. Cauchy–Schwarz and joint-time `W_2` convergence supply these contractions. The same strong comparison/time-net reasoning gives uniform backward moments and hence uniform kernel and squared-speed limits. Their time integrals then converge uniformly on a fixed horizon.

The path bridge is also sufficient: coordinate absolute continuity follows from the strong integral and Fubini, and

\[
\|z-I_\pi z\|_\infty^2\le4|\pi|\int_0^T|\dot z|^2.
\]

Averaging this inequality gives a vanishing transport error to a finite-grid interpolant. Joint `W_2` convergence at the finite grid, followed by mesh removal, proves the asserted two-sample same-layer `W_2(C([0,T]))` laws. It does not require a uniform supremum norm for every neuron. Lipschitz `phi` transfers these laws to features.

Rank-one HS integrands are continuous and bounded on compact time intervals. Finite Riemann sums and the proved cross-time contractions identify increment norms and cross-time parameter observations. First-row reconstruction is bounded linear at each fixed admissible `rho` (with its separate antipodal formula); readout integration is direct. These conclusions compare scalar observations, not operators at different widths.

## 10. Persistent nonaffinity and motion, with R1 explicitly corrected

### Forward separation and unbounded marginals

The first-coordinate displacement is dominated by a sum of bottom reverse Gaussian-source magnitudes plus `a`. That dominator is independent of the initial root pair, and its expectation is below `1/5`. Its event of being at most one therefore has probability at least `4/5`. For `rho<1`, the root event `G_1>=2, G_2<=-2` has positive probability; at `rho=-1` it is just `G_1>=2`. This gives a fixed positive feature difference and `d_1(rho)>0`.

With R1 corrected, exchange symmetry gives positive lower bounds for both eigenvalues of the uncentered feature second-moment matrix. This distinction is important at the antipodal root: `H_1+H_2=2` initially, but the uncentered second-moment matrix is still positive definite. A centered-covariance argument would not suffice here; the proof correctly uses the uncentered matrix as the next Gaussian source covariance.

At the middle layer the displacement dominator has expectation at most `483/1600<1/3` and is independent of its forward source group. The Gaussian covariance has lower eigenvalue `c_1>0` and upper eigenvalue `2a^2`, so its density on `[2,3] x [-3,-2]` is bounded below by the stated positive expression. Intersecting with the independent dominator event gives middle separation. At the top the displacement is deterministically bounded by `63/160<2/5`, so no independence of the correction is required for its rectangle argument.

All these statements are about fixed cut Euler laws. Strong limiting field convergence and the closed-set inequality preserve their positive probability lower bounds. Unbounded marginal tails follow by moving the single-coordinate Gaussian threshold arbitrarily far while retaining the bounded/independent dominator event. The bounds are for each fixed tail threshold, which is enough to establish unbounded support at each time.

For `Z in L^2` with these tails, the affine regression minimum exists because `Var(Z)>0`. Zero regression error would make bounded `phi(Z)` affine in an unbounded `Z`, forcing zero slope, and strict monotonicity would then force `Z` constant. This contradiction proves positivity. The regression moments are continuous along the `L^2` path; the positive variance and regression error have positive minima on each compact interval. Uniform empirical moment convergence transfers a smaller positive bound. This uses fixed nonlinear amplitude and does not infer nonaffinity just from the formula for the activation.

### Backward covariance and every-positive-time speeds

With `Wout>=c_-s`, the top backward fields are positive. On the source rectangle `[4,5] x [-1/10,1/10]`, the bounded top correction gives `|Z_1|>=18/5` and `|Z_2|<=1/2`. The readout cancels in their ratio, yielding the ratio below `1/4`, and the larger field is at least `(4/5)c_-s_0 epsilon` for times at least `s_0>0`. On the swapped rectangle the roles reverse. For any unit coefficient vector, selecting the rectangle where its largest coefficient multiplies the larger field gives the stated positive quadratic-form lower bound. There is no assumption that the readout is independent of the top source.

The next reverse source therefore has positive definite covariance. A bounded response shift cannot remove any sufficiently remote signed Gaussian rectangle. On the resulting four query quadrants, positive gates preserve signs. No nonzero fixed linear combination of the two middle deltas can then vanish almost surely: choose the quadrant aligned with its nonzero coefficients. The same argument proves positive definiteness for the bottom deltas. This requires only fixed-time positivity, not a uniform lower eigenvalue down to time zero.

For the first parameter block, `G` is positive semidefinite with trace two even at `rho=-1`, so pairing it with a positive definite delta second-moment matrix gives a strictly positive trace product. At the other two blocks the feature second-moment matrix is positive semidefinite with positive trace, giving the same conclusion. Thus every hidden parameter block has nonzero feature-time speed.

The adjoint identity II.D.4 telescopes the forward derivative pairings into the sum of lower-block squared gradient norms. All pairings are integrable by `L^2` Cauchy–Schwarz. Its positivity forces at least one sample velocity to be nonzero; exchange symmetry of the joint derivative laws gives equal sample norms, so both are nonzero. Multiplication by the everywhere positive bounded gate preserves a nonzero feature velocity. The clock derivative is positive at every finite physical time. This proves the asserted all-layer motion with R1 repaired, including the singular root.

### Initial nonlazy coefficients and changing kernel

At zero readout the hidden directions vanish. Define the bounded linearized forward map `D_0` on raw hidden directions and `B=D_0^*V_0`. This is a directional/curve linearization, not a claim that the whole feature map has an operator-norm-continuous Fréchet derivative on `L^2`.

The top initial backward coefficient is `beta_a^3=V_0 phi'(Z_a^3)`. Its two-by-two second-moment matrix is positive definite by the same gate-ratio rectangles. The first reverse coordinate map has bounded first derivatives, so III.F applies directly and gives the `R^2` formula, including both the `D_a D_b/2` term and the diagonal curvature term.

For the second reverse call the proof clips `q^2` before multiplying by the middle gate. Its source derivative is precisely the two terms displayed at `3431–3432`. Since `q^2` is Gaussian plus a bounded response, `C(1+|q^2|)` is an integrable dominating function. The derivatives therefore pass by dominated convergence, the inputs pass in `L^2`, and the source covariances pass by second-moment convergence. Covariance-square-root coupling and the actual bounded adjoint identify the uncut answer. The empirical input-clip error is removed in width-then-observation-cap order using the already known `W_2` law. This supplies the specialized derivative/product bridge within Part II; no absent general unbounded-product theorem is invoked.

The bounded responses and nondegenerate Gaussian quadrants show positive definiteness of each lower initial backward pair. Trace products then show each block of `B` is nonzero, including the antipodal first block. Put `Gamma_ell=||B_ell||^2>0` and `Gamma=sum Gamma_ell`.

Strong multiplier continuity along the reached curve gives `Wout(s)/s -> V_0` and `alpha'(s)/s -> B`. Integration gives `alpha(s)-alpha(0)=s^2 B/2+o(s^2)`. The forward curve rule gives `V'(s)=s D_0 B+o(s)` and the actual adjoint gives `E[V_0 D_0 B]=Gamma`. Hence the readout kernel term changes by `Gamma s^2`, the sum of hidden terms is `Gamma s^2+o(s^2)`, and the total mode kernel changes by `2Gamma s^2+o(s^2)`.

The corresponding forward leading velocities `T_a^(ell)` exist in `L^2`. Dividing II.D.4 by `s^2` pairs them with the initial backward coefficients and gives the positive sum of the lower `Gamma_j`. Exchange makes both sample norms nonzero. Integrating the feature curve gives the stated coefficient `phi'(Z_0)T/2` in feature time. Since `s(t)=4t+o(t)`, physical feature changes have coefficient `8 phi'(Z_0)T`; readout-mode and total-mode kernel changes have coefficients `16Gamma` and `32Gamma`. The factors and noncancellation check.

These are nonzero initial quadratic changes and nonconstant kernels. Their transfer to finite models is through already proved fixed-horizon field and kernel convergence; it does not exchange a width limit with a Taylor limit depending on width. Every-positive-time speed was established separately above, rather than inferred from the initial Taylor coefficient.

## 11. Audit disposition

Required: correct R1's four symbol uses and retain `m=2` throughout. Optional: replace the stray `C` in O1 by `G`. No input edits were made in this audit.

The main analytic and probabilistic mechanisms reviewed here are supported by proofs inside the supplied chapter and by classical tools with matching hypotheses. In particular, neither singular initialization, actual finite off-mode residuals, raw GD, empirical joint laws, product integrability, reached-state restart, nor initial nonlazy motion was dismissed by citing an unavailable specialized theorem. The mandatory error remains the explicitly contradictory lower-bound notation in the submitted motion proof. Accordingly the exact hashed submission is **NOTCLEAN**, with the narrower conclusion that no further mandatory gap was identified in this assigned scope.
