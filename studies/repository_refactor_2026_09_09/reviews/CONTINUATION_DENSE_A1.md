# Independent complete proof review A1

**Verdict: CLEAN. No required correction remains.**

The candidate establishes the stated exact identities, global finite-dimensional gradient flow, finite-horizon deterministic bounds, ordered response decomposition, exact-source factorial tails, and the separate bound for recomputed backward sources. These conclusions are valid at fixed finite width and depth. The document expressly excludes, and its proofs do not imply, a population limit, a continuous-depth limit, an autonomous compressed training approximation, eventual fitting, or nonlazy limiting behavior.

## 1. Isolation, reading, and immutable-input ledger

I reviewed only the supplied mathematical inputs in `/tmp/pde_dense_review_1`, the two requested skill files and the applicable references listed below. I did not inspect a checkout, studies, history, another task, a prior report, or external research. I did not delegate. All 380 candidate lines and all 98 canonical-notation lines were read in full, without output truncation. The manifest was also read in full.

The initial and final input hashes agree with each other and, for the two mathematical files, with the manifest:

| Input | Read extent | Bytes | SHA-256 before and after |
|---|---:|---:|---|
| `/tmp/pde_dense_review_1/INPUTS.json` | Entire file | 303 | `be467baadd47b0641eed063e0fb5f76f38ea216e7d6945f3035e8f0bfc34bb7d` |
| `/tmp/pde_dense_review_1/docs/dense_response.md` | Lines 1–380, entire file | 13876 | `446c817b40cb7b32cf83a0fd1bdc3dd54461dbc7bf7b688eacdd9f5dbe9e0286` |
| `/tmp/pde_dense_review_1/docs/NOTATION.md` | Lines 1–98, entire file | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

All other source material read in full:

| File | Lines | SHA-256 |
|---|---:|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 115 | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 185 | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 121 | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | 99 | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md` | 157 | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |

No experimental-design or multi-route proof-search reference was needed: this is an isolated proof audit, and the only computation was a permitted deterministic single-state algebra/differentiation check. Its locally authored script is `/tmp/pde_dense_review_1/check_dense_a1.py`, SHA-256 `467295ba0716e17ef31f8d0431613815cbfa07b687eaf65bb1a425105e259ebf`. It is review evidence, not an input or replacement proof.

## 2. Contract and notation audit

Candidate lines 3–8 and 12–59 correctly define a separate fully dense residual architecture. The contract is fixed finite integers `n,L,d,m >= 1`, arbitrary finite real data, arbitrary real residual strength, coordinatewise tanh, unconstrained trainable matrices, and trainable stored readout. There is no positive-definiteness or independence requirement on the data Gram.

The input is exactly `h_a^0 = B x_a`, with no `1/sqrt(d)`. The document explicitly preserves the canonical `G_ab = x_a^T x_b/d`, hence its input-block factor `x_a^T x_b = d G_ab` is correct. The architectural meaning of `L` as residual blocks is stated. Its order-one stored Gaussian readout and its block mobilities `(L,n,n)` are explicitly distinguished from the different conventions in the canonical notation file. There is no silent transplantation of small-readout or feedforward scalings.

The Gaussian assumptions in (14.2) are consistent as written: independent entries and blocks with hidden variance `sigma_w^2/n`, input variance one, and stored readout variance `A^2`. All subsequent theorems are deterministic for every finite initial state, so none depends on a probabilistic bound or an unproved Gaussian limit.

The full-mean loss is `mathcal L = (1/m) sum r_a^2`, with `r=f-y` separate from adjoints. The conversion from half-sum `E=(1/2) sum r_a^2` is `mathcal L=(2/m)E`; multiplication of its vector field by `2/m`, or the stated substitution `theta_E(2t/m)`, is correct for the same mobilities. Physical time is not confused with residual depth.

## 3. Complete identity and existence audit

### 3.1 Adjoint and parameter gradients: (14.4)–(14.6)

The block differential with respect to its hidden input is

`M_a^ell = I + (gamma/L) D_a^ell W_ell`.

Therefore `p_a^ell = (M_a^ell)^T p_a^(ell+1)` and `p_a^L = a` give exactly `p=n partial f/partial h`. The gate is on the correct side of `W^T`, and the residual is absent from the adjoint.

For an independent variation of `W_ell`, the direct hidden-state variation is `(gamma/L)D_a^ell (delta W_ell) h_a^ell`; contracting with `p_a^(ell+1)/n` gives the Frobenius gradient `(gamma/(nL)) beta_a^ell (h_a^ell)^T`. The input variation `delta B x_a` gives `p_a^0 x_a^T/n`, and the readout gradient is `h_a^L/n`. This proves all of (14.5), including orientation and normalization.

Multiplying `(2/m) sum_b r_b grad f_b` by the corresponding mobilities yields exactly (14.6): readout and input have coefficient `-2/m`, and hidden blocks have coefficient `-2 gamma/(mn)`. There is no remaining hidden depth factor in `dot W` and no input-dimension normalization.

### 3.2 Kernel, PSD, and energy: (14.7)–(14.8)

Let `J_a` be the flattened output gradient and `D_res` the positive diagonal mobility matrix. The physical kernel is `K_ab = J_a^T D_res J_b`.

The readout contribution is `(h_a^L)^T h_b^L/n`. The input contribution is `((p_a^0)^T p_b^0/n)(x_a^T x_b)`. For each hidden block, the rank-one Frobenius pairing is

`L * gamma^2/(n^2 L^2) * ((beta_a^ell)^T beta_b^ell) * ((h_a^ell)^T h_b^ell)`.

These are precisely the three terms in (14.7). The explicitly listed tensor features at lines 111–113 reproduce the same Gram matrix, including `n sqrt(L)` in the hidden feature denominator. This proves positive semidefiniteness for arbitrary data, including singular or coincident samples; no spectral or Schur-product theorem is silently needed.

The chain rule gives `dot f=-(2/m)Kr`. Differentiating the full-mean loss gives `dot mathcal L=(2/m)r^T dot f=-(4/m^2)r^T K r`. Independently, metric gradient flow gives `-dot mathcal L=(grad mathcal L)^T D_res grad mathcal L = ||D_res^(-1/2)dot theta||^2`. Its block expansion is exactly (14.8). Every factor and sign agrees.

### 3.3 Global finite gradient flow: lines 129–154

At fixed finite dimensions, the parameter vector field is smooth because it is built from finite products and compositions of tanh. On a closed ball it is bounded and Lipschitz. The document gives a local existence and uniqueness construction by contraction on continuous paths, with both the invariant-ball and contraction-time inequalities stated. The geometric-series convergence argument supplies the required fixed point; differentiating the integral equation gives the ODE.

On any existing interval, integrating the energy identity and applying Cauchy–Schwarz to the weighted velocity gives (14.9). If the maximal forward lifetime were finite, its last bound makes the parameter path Cauchy as the endpoint is approached. The positive fixed mobility matrix makes this a Cauchy bound in ordinary finite-dimensional parameter space as well. Completeness gives a finite parameter limit, and the same local construction there extends the solution. Continuity of the vector field and the integral equation make the concatenation a solution. This excludes finite-time blowup and establishes the claimed unique global forward flow.

This argument does not assume global Lipschitzness, coercivity of the loss, bounded parameters for all time, or a lower spectral bound for the kernel. The explicit refusal to deduce eventual fitting from loss monotonicity is correct.

### 3.4 Finite-horizon state and adjoint bounds: (14.10)–(14.11), lines 294–299

For the readout and input, individual terms of the weighted displacement estimate imply the first two bounds in (14.10). For residual matrices, the needed chain is

`(1/L) sum ||W_ell(t)-W_ell(0)||_op <= ((1/L) sum ||W_ell(t)-W_ell(0)||_F^2)^(1/2) <= sqrt(T E_0)`.

Adding the average initial operator norms proves the third bound, without a spurious width or depth factor. The forward recurrence adds at most `|gamma| sqrt(n)/L` at each layer because `|tanh|<=1`; the bound on `||B x_a||/sqrt(n)` then gives (14.11) for every hidden layer.

Since `||D_a^ell||_op<=1`, the average generator norm is bounded by `|gamma|` times the average matrix norm, as stated. Each adjoint multiplier has norm at most `1+||mathsf A_a^ell||_op/L`; multiplying and using `1+u<=exp(u)` gives the stated normalized adjoint bound. All constants are finite on a fixed compact horizon. No width- or depth-uniform claim has been smuggled into these deterministic estimates.

### 3.5 Physical forward and backward responses: (14.12)–(14.13)

Differentiating `h_a^0=B x_a` and inserting `dot B` gives the exact boundary source `v_a^0=-(2/m) sum_b r_b (x_b^T x_a)p_b^0`.

At an interior block,

`v_a^(ell+1) = (I+mathsf A_a^ell/L)v_a^ell + (gamma/L)D_a^ell dot W_ell h_a^ell`.

The normalization `h_b^T h_a/n=G^(h,ell)_ba` in (14.6) gives exactly the candidate's `F_a^ell` and the second term of `dot z_a^ell`. This also verifies the square of gamma in the forward forcing, including for negative gamma.

Differentiating `p_a^ell=(I+(mathsf A_a^ell)^T/L)p_a^(ell+1)` yields the homogeneous backward response plus `(dot mathsf A_a^ell)^T p_a^(ell+1)/L`. The terminal value is `w_a^L=dot a`. The derivative identities for the diagonal gate, generator, and gated adjoint in (14.13) are the ordinary product and chain rules, with each multiplication and transpose correctly typed.

The Gram derivative at lines 221–223 is the exact derivative of a normalized finite pairing. Both forward and backward directions use the same dense matrices and their actual transposes. No independent backward matrices or closure hypothesis are introduced.

## 4. Ordered grading and exact-source factorial tail audit

The product `P(ell,b)` in (14.14) has later-depth matrices on the left. Successive substitution yields precisely (14.15), including `P(ell,b+1)` after an insertion of `F^b`.

For clarity, the corresponding exact backward expression is

`w^ell = P(L,ell)^T w^L + (1/L) sum_(b>=ell) P(b,ell)^T S^b`.

The identity product for `b=ell` puts the nearest source in its correct position. This verifies the candidate's reverse-depth and transpose prescription, including the homogeneous terminal term and all source insertions.

Expanding a product of `I+mathsf A^i/L` selects distinct depth indices with their original chronological order preserved. Submultiplicativity of operator norms bounds each monomial by the product of the nonnegative numbers `c_i=||mathsf A^i||_op/L`. In the scalar expansion of `(sum c_i)^j`, each distinct-index monomial occurs `j!` times; all repeated-index terms are nonnegative. Hence the degree-`j` coefficient is bounded by `(sum c_i)^j/j!`. This is valid for arbitrary noncommuting and nonnormal real matrices. Eigenvalues do not enter the argument.

The grade recurrences in (14.16) are exactly these product expansions generated recursively. Boundary and source terms have grade zero, and multiplication by one propagator generator raises the grade by one. A source at depth `b` is multiplied only by later forward generators, or by earlier backward transposed generators, as appropriate. Strict depth ordering forces all terms above grade `L` to vanish. Summing grades therefore restores the exact inhomogeneous response recurrences and boundary data. The candidate explicitly states that the grading does not count the matrices and nonlinear factors already inside a supplied source; this restriction is essential and correctly present.

For every boundary or source insertion, the generator sum over its segment is bounded by `Lambda_T`. Applying the coefficient estimate separately to each insertion and summing its norm gives `B_(v,T) R_K(Lambda_T)` or `B_(w,T) R_K(Lambda_T)`, with exactly the displayed `1/L` weighting and `1/sqrt(n)` normalization. The supremum over samples, depths, and the compact time interval is legitimate because the constants were defined to dominate all such terms. Finiteness of these constants follows from finite-dimensional global existence and continuity of the displayed source expressions.

Finally, writing the scalar tail with `j=K+1+q` and applying `(K+1+q)! >= (K+1)! q!` proves

`R_K(Lambda) <= exp(Lambda) Lambda^(K+1)/(K+1)!`.

This holds also for `Lambda=0`; actual response errors are zero when `K>=L` even if the scalar upper bound remains positive. The conclusion is a finite ordered-product tail estimate along supplied trajectories, not a training-time Taylor series. Lines 320–324 correctly state both distinctions and the need for uniform trajectory constants before any width/depth-uniform assertion.

## 5. Recomputed-source error audit

In (14.19) the true trajectory, generators, and terminal response are held fixed. Insert the exact-source truncated response between `w` and `tilde w_K`. Its difference from `w` is bounded by (14.18). The difference of the two truncated responses has zero boundary value and is linear in `S-tilde S`. Each source insertion is propagated by a partial ordered-product sum of degrees `0,...,K`, with norm bounded by `sum_(j=0)^K Lambda_T^j/j! <= exp(Lambda_T)`. Summing its `1/L`-weighted normalized source norms gives exactly the second term of (14.19). This proves the error decomposition without a hidden stability assumption for altered nonlinear trajectories.

For the specific replacement in lines 352–354, only `v` in `dot z` changes. Thus

`dot z - tilde dot z = W_ell(v-v_K)`,

`dot D - tilde dot D = diag(phi''(z) odot W_ell(v-v_K))`.

The `D dot W` contribution to `dot mathsf A` cancels because it is held exact. Transposing the remaining `gamma (dot D-tilde dot D) W_ell` and applying it to the same exact `p^(ell+1)` gives (14.20), including its outer `W_ell^T`.

The elementary operator estimate is

`||S-tilde S||/sqrt(n) <= |gamma| ||W_ell||_op^2 ||phi''(z) odot p^(ell+1)||_infty ||v-v_K||/sqrt(n)`.

After averaging over layers and taking the stated supremum, (14.18) gives `E_(S,T) <= C_T B_(v,T) R_K(Lambda_T)`, with exactly the constant in (14.21). It is finite at fixed finite state and compact horizon. The normalized Euclidean adjoint bound alone does not give a width-independent coordinate maximum; the document explicitly acknowledges that issue. Changes to the trajectory or `dot W` produce additional error terms, so the final scope restriction is mathematically necessary and correctly stated.

## 6. Deterministic single-state verification

I executed one fixed-state check with `n=3`, `L=4`, `d=2`, `m=5`, `gamma=-0.8`, 45 parameter coordinates, deterministic sine-generated parameter entries, and correlated inputs including a repeated sample. All stored values were order one. No random sampling, optimizer update, training trajectory, parameter sweep, or experiment was run. Central finite differences used step `10^-6`; directional perturbations evaluated derivatives at the same state.

The test independently differentiated every output with respect to all parameters and also differentiated hidden states, adjoints, gated adjoints, and outputs along the analytic physical gradient-flow vector. It checked the metric kernel, energy identity, complete grade sums, a grade-one tail, and the recomputed-source identity and estimates.

| Check | Maximum absolute discrepancy |
|---|---:|
| All output parameter gradients versus finite differences | `1.522e-11` |
| Hidden-block flow formula | `3.469e-18` |
| Kernel formula versus mobility-weighted gradient Gram | `1.110e-16` |
| Energy dissipation versus weighted squared speed | `3.469e-18` |
| Forward response versus directional finite difference | `4.587e-11` |
| Backward response versus directional finite difference | `5.842e-11` |
| Gated-adjoint response versus directional finite difference | `5.870e-11` |
| Output response versus directional finite difference | `2.918e-12` |
| Complete forward grade sum | `2.776e-17` |
| Complete backward grade sum | `2.776e-17` |
| Exact recomputed-source difference (14.20) | `1.464e-18` |

The tested generator commutator had norm `0.10386001885899501`, so the check did not reduce to commuting matrices. With cutoff `K=1`, the normalized actual errors and their corresponding bounds were:

| Quantity | Actual value | Bound |
|---|---:|---:|
| Forward response truncation | `0.0021442483` | `0.0272240237` |
| Backward response truncation | `0.0042786173` | `0.0331767469` |
| Backward response with recomputed source | `0.0042785849` | `0.0332529252` |
| Averaged recomputed-source error | `0.0000368001` | `0.0035197988` |

All assertions passed. These checks support the transcription and scaling audit; the general validity rests on the algebraic and analytic proofs reviewed above.

## 7. Adversarial checks, findings, and final status

| Potential failure | Audit result |
|---|---|
| Missing input `d` or `1/sqrt(d)` factor | Excluded: architecture and input kernel consistently use `B x` and `x_a^T x_b`. |
| Readout initialization or physical-clock substitution | Excluded: different stored Gaussian scale and all mobilities/loss factors are explicit. |
| Gate/transposed-matrix orientation | Correct throughout gradients, adjoints, backward responses, and source replacement. |
| Loss monotonicity used as a coercive bound | Not used: integrated weighted speed directly prevents finite-time escape. |
| Matrix commutativity or normality assumed | Not used: chronological expansion and operator norms suffice. |
| Source counted incorrectly as part of a generator Taylor order | Avoided by the explicit grade-zero source convention. |
| Exact-source tail presented as nonlinear closure convergence | Avoided: altered-source error is separate and altered-trajectory feedback is expressly outside the result. |
| Hidden width-independent `l_infty` bound | Not asserted; the dependency is explicitly acknowledged. |
| Population, continuous-depth, all-time uniform, fitting, or nonlazy conclusion | None asserted. |
| Missing external theorem hypotheses | No specialized external theorem is relied on; the local construction and continuation proof are supplied directly. |

Boundary checks also pass: `gamma=0` gives identity depth propagators and zero generator sources; `E_0=0` makes the physical gradient field vanish; `L=1` gives the single-block formulas; `K>=L` recovers the exact responses; and singular or coincident data never require an inverse Gram matrix.

There are no fatal, major, conditional, or minor mathematical corrections to request. The candidate is self-contained for its stated finite scope, and its stronger scientific nonclaims are appropriately explicit. **Final classification: CLEAN.**
