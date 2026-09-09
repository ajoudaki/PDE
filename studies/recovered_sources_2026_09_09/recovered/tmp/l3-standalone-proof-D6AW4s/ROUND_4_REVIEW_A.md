# Independent adversarial mathematical review

**Verdict: PASS.** The full theorem stated in Section 1 is proved within its stated scope. I found no false assertion, missing mathematical hypothesis, circular dependency, unjustified limiting operation, or unproved specialized theorem that requires mathematical repair. No erroneous or consequentially ambiguous notation requiring correction was identified.

This is a full-document verdict, including the convergence, existence, uniqueness, restart, observation, whole-path, and nontriviality assertions. It is not a verdict limited to the Gaussian calculations or to a finite-time local construction.

## 1. Identity, coverage, independence, and access record

The sole mathematical source was:

`/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

The observed SHA256 was:

`bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e`

It exactly matches the supplied frozen hash. I computed the hash at the start of the reading, after completing the reading and mathematical audit, and after writing the report; all three observations were identical. The file has 1,789 lines and 81,999 bytes.

I read the entire document, including the theorem, all displayed calculations, all explanatory qualifications, and the final paragraph. The numbered reading windows were 1–260, 258–530, 530–800, 792–1080, 1080–1360, 1360–1625, and 1625–1789. The last request extended to line 1800 and reached EOF at 1789. These overlapping windows cover every line, with no omitted interval. The substantive output was not truncated.

The only additional input file accessed was the mandatory procedural skill:

`/etc/codex/skills/solve-math-rigorously/SKILL.md`

I read this file completely: it has 115 lines and 7,593 bytes, and the reading request covered lines 1–240 through EOF. It supplied procedural instructions for rigorous mathematical checking, not mathematical evidence or dependencies. I followed no mathematical reference from it. Its general instruction to verify specialized results externally was subordinate to the user's express prohibition on external mathematical sources; no external verification was performed.

Other inspection consisted only of the execution/editing tool descriptions and file checksums, line counts, and byte counts. The report was created with `apply_patch` at the requested output path, then its own content and file metadata were inspected to verify the deliverable. That generated output was not an independent mathematical source. I did not edit the proof, inspect another project or research file, inspect prior reviews or reports, read another conversation, contact agents, browse, or run numerical experiments or simulations. The arithmetic checks and additional identities below are direct analytic checks of the supplied document. No previous verdict or correction history was used or inferred.

All proof locations below refer to the frozen source's numbered lines.

## 2. Full theorem obligation ledger

| Obligation | Source locations | Audit result |
|---|---|---|
| Correct finite model, normalization, raw updates, and population equations | 18–154; 1111–1239; 1241–1256 | Established. The transformed first coordinate and the raw gradient metric agree with the displayed updates. |
| Finite adaptive Gaussian laws in both orientations | 258–427 | Established by conditional Gaussian projection and conditional empirical averaging. |
| Singular and vanishing query covariances | 429–475 | Established by independent input perturbations, bounded-action comparison, and continuous causal source recursion. |
| Actual feedback contractions and same-population joint laws | 518–619 | Established by finite oracle comparison; no independence of reused coordinates is assumed. |
| Three fixed population spaces and bounded initial actions with their actual adjoints | 621–680 | Established by consistent countable laws, density, the finite norm inequality, and transpose pairings. |
| Fixed-clip existence, uniqueness, and fixed-mesh approximation | 682–790 | Established by the stated norm estimates and a contraction construction. |
| Response bounds uniform in mesh and clipping | 792–978 | Established by a correctly ordered induction with checked constants and complete source derivatives. |
| Removal of clipping; uncut feature flow; uniqueness and restart | 980–1060 | Established by strong comparison with a Gaussian-tail error that dominates every fixed exponential comparison factor. |
| Finite uncut feature-flow convergence with the prescribed small readout | 1062–1109 | Established by same-width comparison against the zero-readout clipped reference. |
| Genuine raw gradient structure and all finite physical horizons | 1111–1239 | Established, including scalar Fréchet differentiability, the physical clock, and raw-coordinate competitors. |
| Exact raw GD, interpolation, and same-width GD/GF convergence | 1241–1390 | Established by the cubic coordinate-change identity and a stopped positive-step comparison. |
| All stated probes, backward fields, kernels, velocities, time lists, and path laws | 1392–1505 | Established by strong comparisons, truncation, finite time grids, and the path interpolation inequality. |
| Nonzero initial motion coefficients and a nonconstant total kernel | 1509–1663 | Established by two correct initial transpose calculations and strong small-time expansions. |
| Positive affine-approximation error throughout compact physical intervals | 1665–1743 | Established by persistent unbounded tails and continuity of the explicit least-squares error. |
| Nonzero hidden feature velocity at every positive finite physical time | 1745–1782 | Established sequentially from top to bottom and then by the actual adjoint identities. |

The following sections explain the checks underlying this ledger, including potential failure mechanisms that do not occur here.

## 3. Setup, normalizations, and elementary tools

### 3.1 Model and coordinate change

The factors of \(n\) in (1.3), (1.6), and (1.7) are consistent. With vector variation norm squared

\[
\|v\|_2^2/n
\]

and ordinary Frobenius variation norm squared for a matrix, the finite predictor gradient has vector blocks \(\delta^{(1)}\) and \(h^{(3)}\), and matrix blocks \(\delta^{(\ell)}(h^{(\ell-1)})^T/n\). Their squared gradient norms are exactly the four kernel blocks in (1.6). Multiplication by \(-2r_n\) gives (1.3). The residual is correctly excluded from the definitions of the deltas.

The transformation is also consistent:

\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(F^{-1})'=\phi'\circ F^{-1},\qquad
\chi'(F(z))=(\phi'(z))^2.
\]

Thus the raw equation for \(Z^{(1)}\) becomes the displayed equation for \(X^{(1)}\). The proof does not claim that the standard Hilbert gradient in the transformed coordinate is the raw gradient; Section 9 expressly supplies the raw parameter metric.

The initial pair \((G,F(G))\) has the moments required for its empirical second moments. Treating that pair as a root, rather than applying the cubic as an arbitrary Lipschitz program instruction, is essential and is done explicitly at lines 172–178 and 623–632.

### 3.2 Initial bounds and convergence tools

The activation bounds at lines 167–175 are valid. The weaker constants \(m=5/6\), \(a=7/6\), and \(|\phi''|\le1/5\) suffice everywhere they are used.

The net estimate (2.2) has the correct normalization. Each fixed unit-vector bilinear form has variance \(1/n\); a quarter-net on both spheres gives the factor two in the operator bound and the exponent \(-100n/8\) after the Gaussian tail estimate. The union bound decays exponentially. The small readout estimate follows directly from its stated variance and needs no maximum-coordinate estimate.

Section 2 provides the limiting facts needed later. Weak convergence plus convergence of second moments supplies uniformly integrable squared tails; the excess-moment argument with \(\min(\|x\|^2,R^2)\) yields ordinary squared-tail control by increasing the threshold, since

\[
\|x\|^2\mathbf 1_{\{\|x\|>\sqrt2R\}}
\le 2(\|x\|^2-R^2)_+.
\]

The finite-cell coupling then proves the stated \(\mathcal W_2\) implication. Continuous tests of quadratic growth are legitimate because those squared tails are controlled. The same-index coupling (2.3) has the correct dimension-free normalization.

The product convergence (2.4) uses a bounded continuous gate and a strongly convergent \(L^2\) factor. It does not follow from weak convergence alone, and the document does not use it that way. Its use for derivatives along a particular \(L^2\)-differentiable curve is valid and does not assert unrestricted Fréchet differentiability of a nonlinear map on \(L^2\). Both Gronwall comparisons have nonnegative coefficients and the boundedness/integrability needed in their later uses.

## 4. Adaptive Gaussian reuse: both orientations and empirical averaging

### 4.1 Exact conditioning

Equations (3.1) and (3.2), lines 274–309, are correct. Conditional on the forward observation, the unexplored matrix is projected on the input side. In its transpose action, the fresh Gaussian term has variance multiplier \(\|u\|_2^2/n\). There is no subtraction of the squared response coefficient. The response and the unexplored Gaussian contribution are separate terms in the answer.

For the general formula (3.3), the dimensions and the compatibility condition are correct. The prescribed mean satisfies both \(WV=Y\) and \(W^TU=Q\). The residual lies in precisely the matrix subspace annihilating the old forward and reverse queries. Orthogonal projection of an isotropic Gaussian entry vector therefore gives the displayed conditional law.

The adaptive argument at lines 332–336 is sufficient: at each step the input is measurable with respect to the preceding transcript, and the new answer reveals a linear observation of only the queried residual. Conditional independence of the two residual matrices is preserved inductively. A coordinate instruction only computes a measurable function of data already revealed. It does not secretly reveal another component of either matrix.

I checked the reverse orientation explicitly, rather than relying only on the phrase that the sides interchange. If

\[
\lambda_n=(U^TU)^{-1}U^Tu,\qquad u_\perp=u-U\lambda_n,
\]

then the transpose of (3.3), together with compatibility, yields

\[
W^Tu\mid\mathcal F\ \overset d=
Q\lambda_n+V\gamma_n+
\frac{\|u_\perp\|_2}{\sqrt n}P_{V^\perp}g,
\qquad
\gamma_n=(V^TV/n)^{-1}(Y^Tu_\perp/n).
\]

This is exactly the counterpart required by the asserted reverse induction. In particular, forward calls after reverse calls retain the \(U\beta_n\) term in (3.4), and reverse calls after forward calls retain the \(V\gamma_n\) term. Neither reuse orientation is replaced by a fresh iid matrix.

### 4.2 Same-population empirical laws

The argument at lines 348–373 handles the dependence that matters. At a fixed number of calls, the removed Gaussian projection has conditional expected normalized squared norm at most the fixed rank divided by \(n\). Its multiplier is bounded in probability by the already controlled input second moment.

After removing that negligible projection, the new Gaussian coordinates are conditionally independent given the transcript. The old coordinates need not be independent. The conditional variance bound for bounded tests, the integrated Gaussian test applied to the old tuple, and the displayed cross-term and Gaussian-square variance calculations establish both weak convergence and second-moment convergence. All contractions in this induction pair fields on the same population, where the required joint law is available.

In particular, the proof does not replace a same-population empirical average after reuse by an iid law of large numbers. The relevant law of large numbers for the new answer is conditional on the entire old tuple.

### 4.3 Source/response identity

The derivation of (3.5), lines 375–427, checks out. Orthogonality of \(h_\perp\) to the old forward inputs removes all the old-input terms in \(q_s\), leaving

\[
\mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]

Gaussian integration by parts then multiplies the expected source derivative by the reverse-input Gram matrix. In the nonsingular case, its inverse gives the displayed coefficient, and substituting the old forward decompositions cancels the projected-input derivative contribution. The new source is a linear combination of old same-orientation sources plus a fresh independent Gaussian; expansion of its covariance gives the full uncentered input second moments.

The Gaussian integration is justified for the finite programs being considered: compositions of their bounded-derivative coordinate instructions have bounded formal derivatives when their finitely many deterministic coefficients are fixed, and the root variables are integrable. Other source groups can be conditioned upon because they are independent. The singular Gaussian integration identity itself follows by writing the source as \(AG\); it is not being used to invert a singular Gram matrix.

The coefficients and covariance parameters are explicitly held fixed during these derivatives. This is the right derivative for the conditional Gaussian calculation. Differentiating coefficient selection would instead introduce terms absent from the finite conditional formula.

### 4.4 Singular queries

Lines 429–475 resolve the singular-query obligation without assuming inverse convergence at a rank drop. A fresh independent input root gives a strictly positive additional Schur-complement contribution \(\epsilon^2\). At each fixed \(\epsilon>0\), the preceding nonsingular argument therefore applies.

The comparison with the unperturbed finite program uses the original matrices on their bounded operator-norm event. The maps in this comparison are the actual Lipschitz instructions, not ill-conditioned regression inverses. For a fixed finite program the resulting \(C\epsilon\) bound is uniform in width and in \(\epsilon\le1\), as required.

The zero-noise source limit is justified causally. Expected derivative coefficients are bounded at each finite stage by previous coefficient bounds and bounded coordinate derivatives. Input covariances converge by strong convergence of the previous expressions. Continuity of finite-dimensional positive-semidefinite square roots, proved by polynomial approximation in the document, supplies a common Gaussian coupling. Continuity and boundedness of the formal derivatives justify convergence of their expectations. This avoids differentiating a covariance square root or taking a pseudoinverse limit.

The convention for distinct formal source slots at a singular covariance is consequential and correctly specified. A zero-variance source value does not force its formal derivative to vanish. The null-space calculation at lines 471–475 shows why a derivative-coefficient ambiguity in a covariance-null direction cannot change the contracted response: its matching linear combination of input fields is zero in \(L^2\).

## 5. Actual scalar program and fixed population operators

### 5.1 Learned updates and feedback

The unrolling in (4.2) has the correct forward and reverse rank-one terms and factors of \(\Delta/n\). The deterministic oracle meets the finite-program assumptions at fixed mesh and clip: readout and both delta fields have the stated bounds, so the required products have bounded-derivative extensions. The initial cubic occurs only in the root pair.

Restoration of empirical contractions at lines 542–555 uses their joint quadratic-growth convergence and the displayed bilinear difference inequality. It is a finite induction with bounded matrix norms. No uniform-in-mesh Gaussian program theorem is silently assumed here.

The source laws (4.3)–(4.5) reflect the actual order of calls: forward corrections use previous reverse inputs, whereas a reverse call can respond to the present forward source. The covariance terms are uncentered second moments, as required for this nonzero-mean activation.

I separately checked the current return in (4.6). With coefficients fixed,

\[
\partial_{\xi^{(2)}_k}Z^{(2)}_k=1,\qquad
\partial_{\xi^{(2)}_k}q^{(2)}_k
=b^{(3)}_{kk}\phi'(Z^{(2)}_k).
\]

Differentiating the two factors in \(\phi'(Z^{(2)}_k)\tau_R(q^{(2)}_k)\) gives both terms displayed for \(b^{(2)}_{kk}\). The response returning through matrix 3 is present. Past-source derivatives likewise use the complete expressions.

### 5.2 Fixed spaces, bounded actions, and actual adjoints

The countable construction at lines 623–654 has the necessary consistency: each finite union is identified as the limit of the same finite-width calculation, and restriction preserves those laws. Each coordinate space is a real Borel space. The countable probability extension principle therefore has its required hypotheses. The included bounded smooth coordinate functions, truncation, and finite-coordinate approximation give the stated density in each layer's \(L^2\).

Passing the finite operator-norm inequality to joint second-moment limits gives (5.1) for every generated finite rational combination. This is stronger than an informal Gaussian description of individual outputs: it ensures that equal \(L^2\) inputs have equal \(L^2\) outputs and that the resulting action is linear and bounded. Density then gives an action on the whole \(L^2\) space. Real coefficients and additional fixed Lipschitz instructions follow by approximation through these bounded actions.

The reverse action is not chosen independently. Equation (5.2) is the limit of the exact finite transpose pairing, with each side averaged in its own population. Continuity and density extend that identity to all inputs. Hence the reverse action is the actual Hilbert adjoint of the forward action on the fixed spaces.

There is no assertion of operator-norm convergence between unrelated finite and population spaces. The constructed initial operators are fixed deterministic maps on function spaces carrying the specified random-coordinate laws; later learned increments belong to the same operator spaces.

## 6. Fixed-clip construction and the response estimate

### 6.1 Bounds and contraction

The coarse estimates (5.5) proceed in a noncircular order: readout, matrix 3, matrix 2, then the first-coordinate velocity. They use bounded features and gates and the rank-one norm identity. The constants are independent of clip and width.

The important top-gate comparison (5.7) uses a pointwise bound on the reference readout only. Expanding with that readout multiplying the gate difference gives the stated estimate even when the other readout is merely in \(L^2\). The middle clipped-gate bound follows from \(|\tau_R|\le2R\), its unit Lipschitz constant, and the gate derivative bound. Together with bounded operators it gives the stated \(C_S(1+R)\) stability.

The contraction construction starts with zero readout. Its pointwise readout constraint is closed under the relevant \(L^2\) limits and is preserved by integrating the bounded activation. The enlarged primal bounds are preserved on sufficiently short intervals. The resulting contraction, the uniform a priori bounds, and the stepwise restarts prove the fixed-clip flow assertion. The local Euler defect and the discrete comparison give (5.8). Only after a fixed finite program is identified does the proof refine the mesh.

### 6.2 Audit of the full response induction

The quantitative calculation at lines 792–958 is the main uniform estimate. I checked its dependence order as well as its constants.

At zero, the readout and top delta vanish identically as formal expressions, and the current middle forward-source derivative vanishes for the stated reason. This gives \(U_0=V_0=0\) without incorrectly annihilating all derivatives in degenerate backward-source directions.

Assuming only previous \(U_r,V_r\le1\), a single bottom source influences the integrated first coordinate with a factor \(\Delta\). The bound \(\chi'\le1/100\) gives (6.2). In the middle forward derivative row, the direct source contributes one in total; it does not contribute one for each earlier slot. Differentiating the middle gate retains the factor \(|q^{(2)}_r|/5\), and differentiating its reverse-query response gives the \(V_r/100\) term. The discrete Gronwall envelope in (6.3) therefore bounds the whole derivative row. The separate impulse from one middle backward source has the \(A\Delta/10\) size used in (6.4).

The envelope moment estimate does not assume temporal independence or independence between \(q^{(2)}\) and its response shift. It first bounds the shift by \(aV_r\), then applies Jensen to the time sum of absolute Gaussian sources, using only their marginal variance bound. This proves (6.5), including at singular source covariances. The checked consequences are

\[
\|E_j\|_1<4,\qquad \|E_j\|_2<3,\qquad
|a^{(2)}_{js}|,\ |a^{(3)}_{js}|<\tfrac32\Delta.
\]

The top source row retains both the readout-sum derivative and the current gate derivative. Their total bound is \((73/300)S\max T_v\). Its past-time recursion gives \(\max T_v<5/2\), so the current top backward row satisfies

\[
V_k\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}<1.
\]

This precedes use of the current query bound. It gives \(\|q^{(2)}_k\|_2\le161/120\). The complete current middle derivative row, including the matrix-3 return, then gives

\[
U_k\le\frac{167}{200}+\frac{77763}{2880000}
=\frac{2482563}{2880000}<\frac9{10}.
\]

Thus neither current-row conclusion is assumed to prove itself. The induction closes for every allowed mesh and clip. The Gaussian variance, shift, and exponential-square estimates (6.10)–(6.11) follow with the displayed constants. In particular, the uniform conclusion is about each time marginal, not a Gaussian path supremum.

## 7. Strong removal of clipping, finite feature laws, and uniqueness

The mesh limit at each fixed clip is strong enough to pass (6.11) by an almost-everywhere subsequence and Fatou. Different fixed times may use different subsequences; because the resulting bound is deterministic and identical at every time, this does not compromise (7.1).

The asymmetric identity (7.2) is algebraically exact. Its last bracket vanishes for \(|q_B|\le R\) for every \(R'\ge R\), including the uncut case. Its magnitude elsewhere is bounded by \(2|q_B|\). The other terms require only the reference clip and reference readout bounds. This establishes both the middle-delta comparison and the full vector-field comparison (7.3) without any tail hypothesis on the competing state.

From (7.1), the tail estimate gives explicitly

\[
\varepsilon_R=8\exp(-R^2/256).
\]

Consequently \(e^{CR}\varepsilon_R\to0\) for every fixed comparison constant \(C\), also with an additional factor \(1+R\). This is sufficient for all three uses: the Cauchy construction of the flow, convergence of the actual uncut velocities, and comparison with an arbitrary bounded-primal integral solution.

The construction passes to the limit in the Banach state norm. It then applies (7.3) to identify the limit of the clipped velocities as the actual uncut vector field. No unbounded product is passed using weak convergence. Uniform convergence of continuous velocities gives the continuously differentiable integral solution. For restarts, the exponentially small initial discrepancy at the reached state survives the additional Gronwall factor, as shown at lines 1054–1058.

Section 8 correctly transfers the reference tail control to finite width through the continuous function \(b_R^2\), a quadratic-growth test. It does not assume finite-width exponential moments or convergence of a discontinuous tail indicator. For fixed clip, the query and \(b_R\)-norm are uniformly Lipschitz in time on the initial norm event, giving (8.1) by a finite grid. Equation (8.2) then allows the prescribed unbounded-in-coordinate readout initialization on the competing side; only its normalized \(L^2\) norm must vanish. The strong middle-delta comparison, followed by the reverse action, also controls the named unbounded backward fields.

## 8. Gradient structure, physical time, and raw competitors

The initial operators are not assumed Hilbert–Schmidt. Only their learned increments need that property. Continuous rank-one velocities have the displayed Hilbert–Schmidt norm, and their integrals belong to that space. The same rank-one difference estimate proves convergence in Hilbert–Schmidt norm where Section 9 needs it.

The scalar predictor differentiability proof at lines 1131–1169 addresses the potentially invalid \(L^2\) chain rule correctly. Estimate (9.2) splits a fixed \(L^2\) coefficient into a bounded part and a small \(L^2\) tail. First taking the perturbation to zero, then the truncation to infinity, makes the scalar remainder little-o of the parameter norm. Expanding from the top down pairs each activation remainder with a fixed old readout or reverse coefficient in \(L^2\). The terms involving both a matrix perturbation and an activation perturbation are quadratic. The derivative is therefore (9.3), and the rank-one Hilbert–Schmidt identity gives (9.4). The product convergence from Section 2 proves continuity of this gradient.

The inverse-coordinate curve rule gives \((Z^{(1)})'=\delta^{(1)}\). Thus the feature flow is the raw predictor gradient flow, and the predictor derivative is the sum of the nonnegative kernel blocks. The lower bound

\[
f_s\ge K^{(4)}\ge25/36
\]

gives a unique level-one feature time \(s_*\le36/25<3/2\). On \([0,s_*]\), the upper bound on the continuous kernel gives the logarithmic divergence of the physical-clock integral. Its inverse exists for every finite physical time and stays strictly below \(s_*\). Equation (9.6) has the correct inequality direction for its positive lower bound on \(s_*-s(t)\).

The uniqueness proof also covers raw competitors not initially assumed to have transformed \(L^2\) membership. Their continuous backward fields and rank-one integral equations justify the raw gradient identity. The deficit solves the displayed scalar linear equation and stays positive on a compact interval. Coordinate absolute continuity and Fubini justify applying the scalar chain rule to the cubic \(F\); equation (9.8) then proves transformed membership from its \(L^2\) right-hand side. Feature uniqueness and the nonattainment of \(s_*\) identify the competitor from the initial state or from any reached state.

This proves all finite physical horizons using one bounded feature interval. It does not require an unproved extension of the uncut feature flow to arbitrary feature time or arbitrary initial population states.

## 9. Exact GD, stopping, and interpolation

Finite physical GF is globally defined on finite horizons by the loss/deficit identity and successive readout, matrix, and first-coordinate bounds. At each fixed width these rule out finite-dimensional escape. Its feature clock lies below the finite level-one point on the stated high-probability initialization event. The condition \(f_n(0)>-1/24\) is consistent with \((25/36)(3/2)=25/24\). Uniform feature-predictor convergence and the scalar clock comparison identify finite physical GF.

The separate raw-GD treatment is necessary and is supplied. I checked the cubic identity (10.1): for \(v=\alpha\phi'(z)q\), expansion of \(10(z+z^3/3)\) gives the linear term \(\alpha q\), the quadratic term \(10\alpha^2z(\phi'(z))^2q^2\), and the cubic term shown.

The remainder bound does not require fourth or sixth empirical moments. The deterministic inequalities

\[
\|q^2\|_2\le\|q\|_2^2,\qquad
\|q^3\|_2\le\|q\|_2^3
\]

and the normalized second-moment bound give a one-step error of size \(C(\alpha_k^2\sqrt n+\alpha_k^3n)\). Summing a positive prefix of bounded total feature length gives (10.2), which vanishes for \(\eta_n=n^{-2}\).

The stopping argument does not assume its conclusion. Bounds before the first bad node control the step into that node, keeping its feature-time endpoint below \(3/2\). The asymmetric comparison and clipped local Euler defect therefore apply through the stopped endpoint. The random time partition causes no averaging difficulty: the reference tail-norm path is Lipschitz, so (10.4) is a pathwise quadrature estimate.

The stopped predictor error tends to zero by first fixing the clip and then removing it after the width limit. The clock comparison uses only this error and the Lipschitz population predictor. At a putative bad endpoint, the margins \(36/25<147/100\) and the positive physical deficit \(\rho\) contradict both stopping conditions. The extra physical interval in the definition of \(\rho\) covers a terminal interpolation node. There is no assumed residual margin uniform in an infinite physical horizon.

Using a fractional step in the same cubic identity controls the specified raw interpolation between nodes. Comparing both GD and GF to the same finite clipped reference at their converging clocks gives exactly the same-width distance (1.7). This is not an invalid comparison of operator norms on different spaces. The final order of approximation yields the full width sequence in probability, not merely a subsequence selected during a Fatou argument.

## 10. Observables, velocities, and whole paths

The finite probe class is compatible with the proof. Lipschitz coordinate maps, bounded products, and bounded current-operator calls propagate state errors. The named middle backward field requires the extra asymmetric estimate; the document supplies it before using the subsequent reverse action.

A bounded continuous gate multiplying an unbounded \(L^2\) field is handled by clipping that field first. The limiting continuous \(L^2\) path has compact image and uniformly integrable squared tails. Uniform \(\mathcal W_2\) convergence supplies the corresponding finite empirical tails in probability. This justifies gate products and subsequent bounded matrix calls without an unstated stronger moment assumption. Finite time grids and these same comparisons handle joint lists of time arguments.

Predictions and kernels are the claimed quadratic-growth averages or products of such averages. The normalizations match (9.5).

The three feature-time preactivation derivative formulas in (11.1) follow by differentiating the forward actions and their rank-one increments. In particular the layer-2 propagated term contains \((\phi'(Z^{(1)}))^2q^{(1)}\), and the layer-3 propagated term contains \(\phi'(Z^{(2)})(Z^{(2)})'\); these are the correct chain-rule factors. Physical time multiplies the formulas by \(2(1-f)\).

For the raw GD interpolation, recomputation of the hidden fields changes the within-step velocity formulas. Lines 1442–1480 estimate precisely that change. The normalized preactivation increments are \(O(\eta_n)\), hence their coordinate suprema change by at most \(O(\eta_n\sqrt n)\). The globally bounded gate derivative converts this into a gate-supremum estimate. Multiplication by the bounded normalized node velocity then gives the stated \(O(\eta_n\sqrt n)=O(n^{-3/2})\) velocity error. The argument propagates from layer 2 to layer 3 and to the feature velocities. The prescribed right-node and terminal-left conventions are compatible with these estimates and the continuous limiting velocities.

Finally, continuous separable-\(L^2\) velocity paths admit the measurable versions and coordinate integrals used at lines 1482–1488. The Cauchy–Schwarz interpolation estimate (11.3) controls empirical and population path-supremum errors by the time mesh times integrated squared velocity. On a fixed grid the law is already identified; linear interpolation is Lipschitz into \(C([0,T])\). This proves the stated path-space \(\mathcal W_2\) convergence directly. It does not substitute finite-dimensional distributions alone for a whole-path argument or invoke an unproved path-space compactness theorem.

## 11. Nonlinearity and nonfreezing

### 11.1 Initial laws and motion

The initial second moments in (12.1) correctly retain the constant term one. Gaussian symmetry removes only the odd cross term.

Both initial transpose calculations are valid. For matrix 3, the reverse input is a function of its observed forward answer, so (3.2) gives a response plus a Gaussian innovation of full variance \(\mathbb E[(B^{(3)})^2]\). The coefficient \(c_3\) is positive after the odd part of the Gaussian expectation is removed; no false pointwise positivity assertion for negative preactivations is used.

For matrix 2, conditioning additionally on the entire independent matrix 3 determines the actual reverse input while leaving the conditional residual of matrix 2 unexplored. The first transpose law supplies the same-population pairings needed for the second. Its unbounded gated input is admissible through truncation and the established \(\mathcal W_2\) law. The independent Gaussian component has variance \(\sigma_2^2>0\), and (12.5) has the correct factor \(c_3/(100m_1)\).

The actual adjoint identities give (12.6). In particular the lower-layer contribution to \(\mathbb E[B^{(3)}V^{(3)}]\) is retained, so its value is \(\Gamma\), not just the direct top-layer term. These identities prove that each motion coefficient is nonzero.

The limits of \(W^{(4)}(s)/s\) and of the scaled backward fields are strong \(L^2\) limits. The curve product rule and bounded actions therefore justify both velocity expansions and their integrated state expansions in (12.7). The kernel expansions are consequently valid. The derivative expansion for \(K^{(4)}\) follows from the velocity expansion itself, not from differentiating an uncontrolled little-o remainder. The physical factors in (12.8), including \(8\Gamma\) in the total kernel, agree with \(s(t)=2t+o(t)\). The integrated squared-velocity coefficients are positive and have the correct factor \(16/3\).

### 11.2 Persistent nonaffinity

The later-time tail arguments use legitimate dominators. The top correction is bounded deterministically. The middle correction is bounded by a variable depending only on the reverse source group, which is independent of the middle forward source. The bottom correction is bounded by a variable independent of the initial first-layer root. The actual corrections themselves need not be independent, and the proof does not assume that they are.

The constants in (12.9)–(12.11) are consistent with the response and marginal variance bounds. Markov's inequality gives the displayed intersection probabilities. The passage to a limiting closed half-line uses the correct direction: its limiting probability is at least the limsup of the approximating probabilities. Thus the positive lower tail probabilities do survive weak convergence.

For each reached law, the affine least-squares minimum in (12.12) is attained because \(\operatorname{Var}(Z)>0\). If it were zero, boundedness of \(\phi\) and unbounded support of \(Z\) would force zero slope, and strict monotonicity of \(\phi\) would then force a constant \(Z\), contradicting the tails. All moments in the explicit formula are continuous along the strong \(L^2\) path. Compactness of a finite physical interval therefore gives a positive minimum, and uniform empirical second-moment convergence transfers a smaller lower bound to finite width.

### 11.3 Nonzero velocity at every later time

The nonfreezing argument is sequential, not circular. Positive readout and a strictly positive gate first give \(\delta^{(3)}(s)\ne0\). Its squared norm supplies a positive variance for the middle reverse Gaussian source in approximating scalar programs. A bounded response shift cannot remove its arbitrarily distant tails, and the closed-half-line passage gives nonzero \(q^{(2)}(s)\), hence nonzero \(\delta^{(2)}(s)\). The same argument then gives nonzero \(\delta^{(1)}(s)\).

Nonzero deltas by themselves would not rule out cancellation in higher-layer preactivation velocities. The document supplies the necessary additional argument: using the actual adjoints in (11.1) gives

\[
\mathbb E[\delta^{(2)}(Z^{(2)})']=K^{(2)}+K^{(1)}>0,
\]

\[
\mathbb E[\delta^{(3)}(Z^{(3)})']
=K^{(3)}+K^{(2)}+K^{(1)}>0.
\]

These pairings exclude zero preactivation velocities. Multiplication by a strictly positive bounded gate cannot annihilate a nonzero \(L^2\) field. The physical clock multiplier also remains strictly positive at every finite physical time. This proves the theorem's every-positive-time hidden feature-motion assertion, beyond the small-time expansion.

## 12. Foundational facts and absence of hidden heavy dependencies

I checked the theorem invocations under the user's rule allowing foundational classical facts with their actual hypotheses verified.

The relevant classical facts are finite-dimensional Gaussian projection and integration, ordinary laws of large numbers for the iid integrable root tuples, conditional expectation, Fubini, dominated convergence, Fatou, elementary Markov/Cauchy–Schwarz inequalities, countable probability extension on real Borel coordinates, elementary regularity of finite Borel measures, and basic Hilbert/Banach completeness and orthogonal-projection facts. Their hypotheses are available where used: finite program length, integrable roots, bounded formal derivatives, consistent countable coordinate laws, square-integrable factors, or integrable velocity bounds, as appropriate.

The nontrivial task-specific results are developed inside the document: adaptive two-orientation empirical Gaussian induction, source responses, singular-query removal, bounded population actions and adjoints, the uniform response estimate, strong clip removal, the physical-time construction, raw-GD comparison, and the path-law argument. Finite-dimensional square-root continuity, the needed Wasserstein moment criterion, scalar predictor differentiation, and the contraction/comparison arguments are also explained internally. There is no reliance on an external tensor-program limit, propagation-of-chaos theorem, spectral limiting law, uncut Banach-space local-Lipschitz theorem, or specialized continuation theorem.

## 13. Defects, notation, and final disposition

**Mathematical defects requiring repair: none identified.** There is consequently no severity-ranked failure list, missing obligation, or counterexample to report.

**Erroneous or consequentially ambiguous notation requiring correction: none identified.** In particular:

- Finite transpose \(T\), population adjoint \(*\), and layer-local expectations are explicitly distinguished at lines 80–85 and used consistently.
- Feature-time primes, physical-time dots, and scalar-function derivatives are explicitly distinguished at lines 479–487.
- The omitted clip subscript on middle delta fields in the scalar programs is authorized at lines 530–531; later uncut uses are specified in their own context.
- Formal source-slot derivatives at singular covariances and the frozen-coefficient convention are specified at lines 389–392 and 469–475. They do not denote differentiation through coefficient or covariance selection.
- The distinction between raw GD and transformed Euler, and between the transform of raw interpolation and interpolation of transformed nodes, is explicitly maintained.
- Same-width state distances are not presented as operator-norm distances between different population spaces.

These conventions resolve mathematical interpretation; asking for different symbols or additional cosmetic restatement would be an optional editorial preference, not a defect.

**Final verdict: PASS.** No required mathematical repair remains for the complete theorem as stated in the frozen document.
