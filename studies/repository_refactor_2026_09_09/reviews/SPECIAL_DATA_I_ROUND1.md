# Isolated adversarial proof audit: opening conventions and Part I

## Verdict

**CLEAN for the assigned mathematical scope.** No required mathematical correction was identified. The chapter supplies the specialized arguments needed for the special-angle population construction, global physical gradient flow, exact raw-GD comparison, stated path and velocity observables, persistent distributional nonaffinity, positive hidden activity, and initial change of the full kernel.

This verdict has the theorem's actual quantifiers: fixed data, hidden depth two, correlation exactly zero or minus one, and each fixed finite physical horizon, before width tends to infinity. It does **not** certify Parts II or III, intermediate angles, a growing horizon, arbitrary initial states, arbitrary width-dependent operator probes, or asymptotic fitting. “CLEAN” records the result of this audit, not a claim that further scrutiny cannot find an issue.

Required issues: **none**. Two optional expository improvements appear below. Neither is an additional mathematical premise needed to close the proof.

## Inputs, hashes, isolation, and exact read coverage

The only mathematical source files used were:

| File | Lines | SHA-256 |
|---|---:|---|
| `/tmp/pde-special-reviewed-input.CM1FuJ/special_data_limits.md` | 6397 | `94ad0b6a9ba39e937e1f90626c74c6b9d1f652fe20523dcdf1cdbf780bdfeda0` |
| `/tmp/pde-special-reviewed-input.CM1FuJ/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both hashes were computed before the proof reading and checked again before writing this report; they agreed. The inputs were never edited. No repository contents, history, other reviews, web sources, agents, or numerical experiments were used. The rigorous-math workflow instructions were read as procedural guidance; no mathematical premise was imported from them.

Read and audited completely:

- `NOTATION.md`, lines **1–98**, through EOF.
- `special_data_limits.md`, lines **1–126**, all opening conventions. Claims about the other families in the introductory table were not independently certified.
- `special_data_limits.md`, lines **127–2086**, all of Part I through its final scope paragraph and the end of the part. This includes every subsection of I.1–I.5, not just theorem statements or selected displays.
- `special_data_limits.md`, lines **6376–6397**, the complete final scope section through EOF, with its Part I qualification at 6384–6386 checked against I.85.

Exact additional coverage disclosure: the final-scope extraction also displayed lines **6360–6375**. This was an incidental over-read of neighboring Part III text, not an invoked dependency. No mathematical conclusion in this report uses those lines, and their containing Part III proof was not audited. Thus the union of chapter lines displayed was **1–2086 and 6360–6397**. A combined tool response was truncated; the affected proof region, **773–1084**, was subsequently read again without truncation. No gap in the assigned proof coverage remains.

No mathematical dependency on another chapter section was needed. All Part I dependencies actually used lie in the fully read Part I text or the notation contract. In particular, the Gaussian theorem of III.F mentioned in the opening conventions was not used for Part I.

References below are to `special_data_limits.md` unless explicitly labeled `NOTATION.md`.

## Required versus optional issues

### Required

None found. I did not find an incorrect normalization, unsupported specialized-theorem invocation, missing restart condition, unjustified finite-GD substitution, unclosed moment or product estimate, or nonlinearity/activity claim exceeding the argument.

### Optional O1: make the population path-moment transfer explicit

**Location:** 1413–1436 and 1496–1512, particularly the use of I.72 to upgrade path convergence to all finite Wasserstein orders.

I.72 is displayed for the modified finite systems. The population path moments follow from the proved weak path convergence by testing bounded truncations of the continuous path-supremum functional and then using monotone convergence. For example, for each fixed finite \(q\), test

\[
g_M(x)=\min\{\|x\|_\infty^q,M\}.
\]

The finite expectation bound in I.72 bounds the limiting integral of \(g_M\), uniformly in \(M\); let \(M\uparrow\infty\). Choosing \(q>p\) then controls the \(p\)-tails. This is an available elementary consequence of the text, not a gap. Stating it would make the all-orders path upgrade easier to verify.

### Optional O2: clarify the wording of the remainder bound

**Location:** 1336, “Essential remainder bounds are uniform in the horizon.”

The proved statement is uniform **over times and comparison meshes within each fixed horizon**, with bound \(C_T\). It is not a constant independent of \(T\). Writing “uniform over each fixed horizon, with a constant depending on that horizon” would remove a possible ambiguity. I.63–I.66 and the explicit scope statements already supply the correct interpretation.

## Detailed checks

### 1. Storage, metric, backward fields, and clocks

**Read:** opening 21–126; I.1.1, 137–211; `NOTATION.md`, 8–42 and 70–98.

The change from canonical first weights to \(V^{(1)}=W^{(1)}/\sqrt d\) is linear. Consequently

\[
\frac dn\|\Delta V^{(1)}\|_F^2
=\frac1n\|\Delta W^{(1)}\|_F^2,
\]

and the inverse metric on \(V^{(1)}\) is \(n/d\). The Euclidean first gradient is \((2/n)\sum_a r_a\delta_a^{(1)}x_a^T\); multiplication by \(n/d\) gives precisely the first update in I.6. The middle metric is ordinary Frobenius and its gradient contains \(1/n\). The readout metric is \(1/n\) times the Euclidean squared norm, so its inverse cancels the prediction's \(1/n\). Thus all three updates have the stated factors.

The backward fields contain no residual. They implement \(\delta^{(\ell)}=n\,\partial f/\partial z^{(\ell)}\); the \(r_a\) factors occur separately in the updates. The forward action of \(W^{(2)}\) is ordinary matrix multiplication. The rank representative is \(uv^T/n\), not \(uv^T\). Its Frobenius norm is

\[
\left\|\frac{uv^T}{n}\right\|_F
=\frac{\|u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n},
\]

matching the population rank-one norm. The transpose and population adjoint contract the appropriate layers; no cross-layer neuron pairing is assumed.

Part I uses the **sum** of the two squared residuals. Its physical step is \(n^{-2}\), at nodes \(k n^{-2}\). For the mean loss the same iterates require step \(2n^{-2}\), and the same GF path is traversed at mean-loss time \(2t\). C.5 and the table agree with this. The later feature clock is not applied to raw GD.

The stored readout initialization has variance \(n^{-2}\), hence standard deviation \(n^{-1}\). The proof retains that finite array and only later compares its flow with the auxiliary zero-readout flow. It does not substitute order-one stored readout, nor infer equivalent dynamics from equal limiting initial predictions.

### 2. The geometry and the exact first-coordinate transformation

**Read:** I.1.1 and I.2.1, 137–159 and 364–419.

The unit input norms give \(G_{aa}=1\). Orthogonality requires \(d\ge2\), which is explicitly stated. At correlation minus one, equality in the input norm relation gives \(x_2=-x_1\). Oddness of arctangent and evenness of its derivative then give the exact forward opposition and backward equality in I.17 at every raw parameter state, including nonzero finite readout and GD interpolation.

For \(F(z)=z+z^3/3\), \(F'(z)=1+z^2\ge1\), and

\[
(F^{-1})'(u)=\phi'(F^{-1}(u)),\qquad
(\phi\circ F^{-1})'(u)=\phi'(F^{-1}(u))^2.
\]

Both composition maps used for stability are globally Lipschitz. At \(G=I\), multiplication of the first raw equation by \(F'(Z_a^{(1)})\) cancels its own gate exactly. At correlation minus one, reduction to one independent field gives control \(c_1-c_2=-4r_1\). It does not give \(-2r_1\), and it does not count two independent first-layer motions.

The row reconstruction I.18 preserves the initial component orthogonal to the data span. Because the retained directions are orthogonal and have squared norm \(d\), its first-parameter speed is exactly the sum over the independent first preactivation speeds. The anti-parallel case has one summand.

For intermediate nonzero correlation the offending factor is

\[
\frac{1+(Z_a^{(1)})^2}{1+(Z_b^{(1)})^2}.
\]

It is not controlled as a bounded multiplier by this proof. The final paragraph of Part I correctly excludes those angles.

### 3. Local \(L^2\) construction, the actual adjoint, and restart

**Read:** I.1.2–I.1.3 and I.2.2–I.2.3, 213–360 and 421–579.

I.20 uses a bounded readout, bounded activation and gates, and an operator norm bound. Its key estimates do not require \(Q^{(1)}\in L^\infty\). For example,

\[
\|w\phi'(z)-\widetilde w\phi'(\widetilde z)\|_2
\le \|w-\widetilde w\|_2+M\|z-\widetilde z\|_2,
\]

and the reverse-field estimate then follows by subtracting the operators and applying their \(L^2\) bounds. The rank difference splits into two ranks, with their operator and Hilbert–Schmidt norms given by I.9. This verifies the Lipschitz assertions in the transformed state norm, including when operator increments are measured in Hilbert–Schmidt norm.

The proof does not incorrectly treat an \(L^\infty\) ball as an open \(L^2\) domain. It first clips readout occurrences to define a locally Lipschitz field on an open state ball, proves the integral-map contraction there, and uses the readout integral bound to make clipping inactive on a short interval. Completeness, drift bounds and the small-time contraction condition are all supplied.

For prescribed integrable controls, the same argument uses accumulated absolute control instead of elapsed time. For physical feedback the prediction estimate closes the state comparison. If the initial operators differ, I.22 and the following paragraph keep their initial difference in operator norm while comparing learned increments in Hilbert–Schmidt norm. This distinction is needed later for the capped initial operator and is present.

The restart claim is from **reached states**, retaining the entire row, readout and operator. Such states retain bounded readout, a bounded operator, and \(F(Z^{(1)})\in L^2\). For a putative ordinary \(L^2\) solution with the same reached initialization, Fubini gives scalar absolutely continuous representatives. The scalar chain rule for \(F\) yields I.27, whose right side belongs to \(L^2\). This places the candidate in the already unique transformed class. It does not assume that the cubic composition is a globally defined Lipschitz map on arbitrary \(L^2\) data.

No Gaussian independence is reset at restart, and no arbitrary \(L^2\) readout initialization is smuggled into the theorem.

### 4. Global continuation and the energy identity

**Read:** I.2.3, 503–579.

The readout, operator increment and transformed-field bounds in I.23 follow by integrating their equations against the action \(S\). In particular, the operator increment bound integrates \(B(b_2+Bv)\), giving \(Bb_2 S+B^2S^2/2\). Each derivative is bounded by an integrable scalar on a bounded-action interval. A finite candidate endpoint therefore has a state limit; the readout also has an \(L^\infty\) limit. The local construction applies at that limit.

The \(L^2\) chain rule used for bounded continuously differentiable scalar maps is proved along curves by replacing the increment by its fixed tangent and applying dominated convergence to squared difference quotients. It does not assert unsupported Fréchet differentiability of nonlinear \(L^2\) composition.

Differentiation of the prediction using the actual adjoint gives the three kernel blocks in I.12. They are positive semidefinite Grams. With sum loss,

\[
\dot f=-2Kr,\qquad
\dot{\mathcal L}=-4r^TKr=-\|\dot\theta\|_{\rm par}^2.
\]

The first term in the last norm is the independent-first-field sum, not a duplicate sum at the antiparallel angle. This gives residual boundedness, \(S(t)\le2\sqrt2\sqrt{\mathcal L(0)}t\), and hence global continuation on every finite horizon. At zero population readout the stated bounds \(S\le4t\), \(\|W^{(3)}\|_\infty\le4Bt\), and \(\|W^{(2)}\|_{\rm op}\le8+8B^2t^2\) follow.

Only the learned operator increment has a Hilbert–Schmidt norm. No Hilbert–Schmidt property of the Gaussian initial action is needed or asserted.

### 5. Exact raw GD, stopping bounds, and velocity rates

**Read:** I.2.4, 581–678; the transfer at 1604–1616.

For the transformed Euler scheme the bounded Lipschitz field gives a local \(O(h^2)\) defect. Iteration of the explicit error inequality yields I.29. The first-exit argument bounds discrete action through the candidate exit update, so the residual stopping bound is closed by comparison with the exact flow. It is not assumed for the untruncated iterates without proof.

Raw GD is not transformed Euler. At a raw node, putting \(v=\eta c\phi'(z)q\) gives the exact identity

\[
F(z+v)-F(z)
=\eta cq+\eta^2c^2z\phi'(z)^2q^2
+\frac{\eta^3c^3}{3}\phi'(z)^3q^3.
\]

Under the stopped state bounds,

\[
\|q\|_2/\sqrt n\le C_T,
\quad \|q\|_\infty\le\sqrt n C_T,
\quad |z|\phi'(z)^2\le1.
\]

Consequently the quadratic term has normalized \(L^2\) size \(O(\eta^2\sqrt n)\), and the cubic term has size \(O(\eta^3n)\). Accumulation over \(O(T/\eta)\) steps gives \(O_T(\eta\sqrt n+\eta^2n)\). At \(\eta=n^{-2}\) this is \(O_T(n^{-3/2})\); transformed Euler's \(O_T(n^{-2})\) error is smaller. The same stopping argument closes the raw scheme.

The interpolation defect and its derivative are separately controlled in 630–635. For original first velocities, I.32 loses a factor at most \(\sqrt n\), so their normalized \(L^2\) discrepancy is \(O_T(n^{-1})\). The same estimate applies to the first activation velocity. In the second-layer identity, bounded operator action propagates that error; the last gate multiplication again costs at most the controlled coordinate maximum times the \(O_T(n^{-3/2})\) field error. Thus the stated \(O_T(n^{-1})\) original hidden-velocity errors are consistent. Rank and readout velocities retain the stronger transformed-state rate.

The operator event is justified by the displayed finite net and Gaussian tail calculation. At threshold 8 its bad probability tends to zero exponentially. The readout maximum bounds follow from its standard deviation \(1/n\) and a union bound. These events supply width-independent constants; no false uniform bound over all Gaussian initializations is used.

The path transfer to GD is stronger than a mere fixed-time RMS comparison: each base-field coordinate path error is bounded by \(\sqrt n\) times the uniform normalized error, hence \(O_T(n^{-1})\). For \(\delta^{(1)}\), the product estimate gives a maximal coordinate path error tending to zero as well. This suffices to transfer every fixed finite path Wasserstein order. Discrete GD is not assigned the exact GF loss identity.

### 6. Fixed-program moments without an \(L^p\)-bounded Gaussian operator

**Read:** I.3.1–I.3.2, 682–872.

The fixed transformed mesh has bounded readout by the elementary recursion I.41. This permits replacement of the readout factor in graph estimates by a smooth bounded extension agreeing with the actual values. The resulting coordinate operations are globally Lipschitz. The cubic \(F(G)\) is stored in an iid root tuple with all finite moments; the proof does not differentiate the cubic as if it had a bounded derivative on the Gaussian root space.

For an initial matrix \(E/\sqrt n\), its differential acting on a vector is \(W\partial x+n^{-1/2}v x\). The latter has Euclidean size bounded by \(\|v\|_F\|x\|_2/\sqrt n\). A normalized contraction has derivative bounded by \(n^{-1/2}\) times normalized vector norms and Euclidean vector derivatives. Those factors cancel correctly at scalar-times-vector nodes. This verifies the width-independent polynomial derivative bounds I.42.

I.43 is proved by rotating two independent standard Gaussian arrays. At every rotation angle the velocity is an independent standard Gaussian, so conditional Gaussian integration yields the dimension-independent gradient moment bound. Conditional Jensen supplies centering. The polynomial bounds and Gaussian norm tails justify integrability; the Lipschitz extension is enough for later supremum functionals.

Conditional means are not assumed bounded merely from Gaussian concentration. The neuron-transposition argument and root Lipschitz estimate compare \(m_i(R)\) with \(m_j(R)\); averaging over \(j\), using the RMS bound, gives I.44. The iid root tuples have all needed coordinate moments, including when their components are dependent or their covariance is singular. Combining these facts gives I.45 for every fixed graph, also for deterministic-coefficient and perturbed versions.

These are moment bounds for generated random fields. No bound for the matrix on arbitrary \(L^p\) directions is inferred.

### 7. Gaussian conditioning, actual reuse, empirical laws, and singular queries

**Read:** I.3.3–I.3.4, 874–1083.

The conditional matrix formula I.46 has both prior forward and reverse constraints. Its proposed mean satisfies \(WV=Y\) and \(W^TJ=P\), using \(J^TY=P^TV\); the residual lies in their common null space. Vectorized Gaussian orthogonal projection proves the formula. Adaptivity is handled causally: a new input is measurable from the prior transcript, and observing its answer adds that input's linear constraint. A fresh independent transpose is never substituted.

For a new input, the innovation is \(\sigma_nP_{J^\perp}e\). Removing the fixed-rank projection is justified in empirical \(p\)-moment by

\[
\frac{\mathbb E|N|^p\sigma_n^p}{n}
\sum_i(P_0)_{ii}^{p/2}
\le \frac{j\mathbb E|N|^p\sigma_n^p}{n}
\quad(p\ge2).
\]

The innovation variance is bounded by the input RMS squared, and the fixed-program moments control its tails. For smaller \(p\), normalized norm comparison applies. This is sufficient even though the finite reused coordinates themselves are not independent.

After projection removal, conditional independence supplies the variance bound I.48 for empirical continuous polynomial-growth tests. Old-tuple moments and I.49 justify truncation, coefficient convergence on compact sets, and restoration of the removed projection. Inverse-Gram coefficients are only used here when the limiting Grams are nonsingular, so they are tight on events of probability tending to one. The root induction is iid averaging.

The response rule I.50 is derived rather than cited. For \(h_\perp\) orthogonal to old forward inputs, the old reverse answer contributes only \(\mathbb E[\zeta h_\perp]\). Gaussian integration by parts gives its derivative contraction. The old forward responses cancel the least-squares correction exactly. The remaining full source has covariance equal to the **uncentered input Gram**, not a response-subtracted covariance. The reverse calculation uses the same argument with the populations exchanged.

Singular queries are regularized at the input of every initial-matrix call with a newly revealed independent Gaussian root. For each fixed positive noise level, the new limiting Gram Schur complement is at least \(\epsilon^2\). This checks the nonsingularity hypothesis needed by the preceding induction, even for zero or redundant unperturbed calls.

Noise removal does not claim uniform bounds on inverse Grams as \(\epsilon\downarrow0\). It instead uses the actual finite-graph RMS comparison, all-order moments and interpolation I.53, while the scalar source-response formula contains no inverse covariance. At each fixed finite causal step, coefficients, source covariance square roots and bounded formal derivatives converge. The proof of square-root continuity includes singular positive semidefinite matrices. Dominated convergence is legitimate under the fixed-program moment and derivative bounds.

The resulting order is fixed program and positive noise, width limit, then noise removal. Formal sample/source slots are kept at rank drops, with the explicit expression fixing their derivatives. The theorem is therefore not conditional on a nonsingular query Gram at every training node.

Finally, causal selection of deterministic contraction values identifies the deterministic-coefficient program, and finite graph subtraction compares it to actual empirical feedback. Moment interpolation and truncation upgrade RMS discrepancies to polynomial-growth tests. The cell-matching and tail argument proves Wasserstein convergence rather than treating weak convergence alone as sufficient.

### 8. One canonical operator and a common space for mesh refinement

**Read:** I.3.5, 1085–1169.

The countable construction contains mesh fields, both orientations on generated inputs, rational linear combinations, and bounded smooth cylinder functions. Every finite sublist is covered by the proved finite-program law. Covariance extensions are nonnegative because they are input Grams; the residual-variance construction also handles zero variance. The explicit countable root construction supplies ordinary countably generated probability spaces.

The two operator inequalities and the adjoint identity I.55 pass from finite widths because every involved Gram entry has a deterministic limit and the matrix norm event has probability tending to one. A nonzero limiting violation would contradict those facts. Zero-norm input relations therefore produce zero-norm answer relations, so the proposed linear actions are well defined.

Density is justified by the cylinder-event approximation argument and bounded smooth approximations of threshold indicators, followed by simple-function approximation in \(L^2\). The extensions are bounded by 8. Passing the bilinear identity to the completions makes the reverse extension the actual adjoint. The initial operator is neither an iid continuum kernel nor presumed Hilbert–Schmidt.

Different finite meshes are coupled by the same initial matrix law and included in this common space. Their limiting mesh equations use this same operator and its learned ranks. I.56 is consequently a genuine same-space deterministic Euler comparison, not a choice of unrelated subsequential marginal limits. Requested additional programs can be adjoined without changing earlier laws.

### 9. Global response rows and bounded Gaussian remainders

**Read:** I.3.6–I.3.7, 1171–1340.

This is a substantive additional argument beyond primal \(L^2\) well-posedness, and it is supplied. I.41 bounds readout and total discrete action on every finite horizon, uniformly in the number of mesh queries. Operator norms and one-step state Lipschitz factors are consequently bounded by constants depending only on that horizon. The two-coordinate auxiliary program is retained off the antiparallel invariant set; no false identification with off-invariant raw GF is made.

Inserting \(\epsilon e\) into a complete reverse answer changes the immediate state only through an \(h_s\)-weighted update. Inserting it into a forward answer may immediately change deltas, residuals and reverse answers by \(O(|\epsilon|)\), but changes subsequent states through \(h_s\)-weighted updates. Products of the later factors \(1+C_T h_k\) give I.58–I.59, including feedback changes.

The extraction of formal derivative expectations is legitimate in the specified order. First fix the mesh and nonzero forcing, and take the joint width limit of the forced run, unforced run and fresh root. In its own population the fresh root occurs only through the designated source-slot insertion; the selected scalar coefficients and covariance parameters are deterministic with respect to that local coordinate. Thus

\[
\partial_e X^\epsilon=\epsilon\partial_{\rm slot}X^\epsilon,
\qquad
\mathbb E[eX^\epsilon]
=\epsilon\mathbb E[\partial_{\rm slot}X^\epsilon].
\]

The second identity uses ordinary one-dimensional Gaussian integration by parts in an independent nondegenerate root, even when the old source covariance is singular. The unused root has zero contraction with the unforced expression. Finite Cauchy–Schwarz plus the forced discrepancy bounds control the derivative expectation after division by \(|\epsilon|\). Only then is forcing sent to zero, using the fixed-program derivative continuity already established.

This proves \(|\alpha_{ka,sb}|,|\beta_{ka,sb}|\le C_T h_s\) for past slots, with the separate bounded current diagonal response. Adding the learned terms preserves those bounds. Summing \(h_s\) gives a finite response-row bound independent of mesh length. The proof never infers transverse derivatives from an unforced singular law alone, nor extends a short-time response bootstrap without a global estimate.

Since the features and second deltas are bounded, bounded response-row sums give the bounded remainders in I.63–I.64. Cross-program source covariance identities give Gaussian isometries I.65. Strong \(L^2\) convergence of mesh inputs therefore gives strong convergence of their sources. Bounded remainder limits remain essentially bounded, and source Riemann sums converge to Gaussian integrals independent of the initial first row. These facts establish I.66 on the already constructed space.

The deterministic-time and product-almost-everywhere formulations at 1329–1338 are sufficient. Time integration uses jointly measurable representatives and Fubini; the proof does not require an unstated simultaneous pointwise bound over all times on a previously fixed null-set complement.

### 10. Supremum moments, products, and full path laws

**Read:** I.4.1–I.4.3, 1344–1521.

The product estimate I.67 is correct and addresses the actual obstruction: multiplication of a bounded gate by an \(L^2\) field is not jointly Lipschitz in two \(L^2\) inputs. Splitting at \(|b|=R\) gives a small bounded part and a squared-tail term. The proof uses this estimate rather than assuming that the reverse field is essentially bounded.

The radial matrix cap is a proof device for moments. Its 2-Lipschitz operator-norm estimate yields a \(2/\sqrt n\) bound in unscaled Gaussian matrix coordinates. The deterministic flow stability then makes each coordinate path-supremum functional Lipschitz with a width-independent constant: the factor \(\sqrt n\) for an individual coordinate cancels the normalized input change.

I.70 is justified by pointwise absolute continuity and the integral triangle inequality. The derivatives in I.71 are in \(L^2\): the readout multiplier is bounded, scalar derivatives are bounded, and every matrix action uses only the operator's \(L^2\) bound. No unbounded product of two uncontrolled \(L^2\) fields is present there. Conditional Gaussian concentration, the same conditional-mean transposition argument, and all root moments yield I.72 for path suprema. The proof also gives the uniform mesh version. Clipping the small initial readout at one preserves the necessary bounds and is inactive with probability tending to one.

The first delta is controlled by \(|\delta^{(1)}|\le|Q^{(1)}|\), so its path tails are covered without differentiating that product. The full first row follows from reconstruction and its initial Gaussian orthogonal component.

At fixed times the width/time passage uses three terms: finite GF to a fixed comparison mesh, the proved width limit of that fixed mesh, and the mesh to the common-space population flow. The mesh is chosen before width. The actual small Gaussian readout is restored by a same-initial-matrices stability comparison, with initial normalized readout norm tending to zero. This yields full-sequence convergence in probability; a width subsequence or a long-transcript Gaussian theorem is unnecessary.

For path convergence, the elementary bound

\[
\|X-\Pi_\Delta X\|_\infty^2
\le4\Delta\int_0^T|\dot X|^2
\]

applies to the listed absolutely continuous base fields. Averaging gives the empirical transport error. Finite observation-grid convergence followed by grid refinement proves joint same-neuron path \(\mathcal W_2\) convergence separately in the two populations. The product map for \(\delta^{(1)}\) is continuous on the joint continuous-path space, and its supremum is dominated by that of \(Q^{(1)}\). Supremum moments of order \(q>p\) supply the required tail control for every fixed finite path Wasserstein order. Optional O1 spells out the elementary population moment transfer.

Uniform prediction, loss and kernel convergence is supported by bounded-state Lipschitz estimates for blocks 2 and 3, the product-tail estimate for block 1, and fixed-mesh endpoint contractions plus the uniform \(L^2\) time modulus. This is stronger than convergence at a list of isolated times.

### 11. Admissible probes, original velocities, and quadratic observables

**Read:** theorem scope 305–340; I.4.2 and I.4.4, 1438–1494 and 1523–1616.

The probe quantifier is restricted to a fixed finite program of the permitted instructions and controlled \(L^2\) limits of such programs. The instructions, coefficients and additional-root laws do not vary arbitrarily with width. In particular, the small readout cannot be amplified by an unadvertised width-dependent factor. No arbitrary direction or cross-dimensional operator-norm convergence is claimed.

The velocity query \(\phi'(Z^{(1)})^2Q^{(1)}\) is not declared globally Lipschitz without qualification. Truncating \(Q^{(1)}\) makes it an admissible smooth Lipschitz instruction, while I.45 or I.72 removes truncation in normalized \(L^2\). The actual operator norm controls its forward or reverse answer error. Thus the second preactivation velocity is identified with the trained operator and its learned ranks.

First original velocities are compared using the product-tail estimate and path-supremum integrability of \(Q^{(1)}\). Rank and readout velocities are Lipschitz in the bounded transformed state. The identity

\[
\dot Z^{(2)}=\dot W^{(2)}H^{(1)}+W^{(2)}\dot H^{(1)}
\]

then gives uniform-in-time normalized \(L^2\) comparison of second preactivation velocities. At each fixed mesh, only finitely many velocity laws are needed, using the stated piecewise-constant comparison.

The final multiplication by the second gate is not justified by a norm bound alone. I.75 explicitly transfers squared-tail control from the finitely many fixed-mesh second preactivation velocity laws to the GF velocities. Its inequality follows by splitting into \(|y|\le R/2\) and its complement. The order of limits is appropriate: choose the comparison mesh for a small RMS error, take its finite-law tail cutoff large, and then refine as necessary. In the population, compactness of a continuous \(L^2\) velocity curve gives the analogous uniform integrability. I.67 now closes the last product.

The displayed quantifiers at 1544–1559 correctly concern the width limsup of the probability of a time-supremum normalized RMS error. They imply integrated mean-square comparisons after multiplication by \(T\), without identifying finite neuron indices with population labels. Squared norms converge uniformly in time by the difference-of-squares inequality and bounded RMS norms. No continuous-path law of discontinuous comparison velocities is asserted.

For middle-parameter speed the exact rank contraction is I.76, with the factor four from the sum-loss gradient. Its products are on separate layers and factor as rank Hilbert–Schmidt pairings. First speed uses the independent-row metric; readout speed uses its normalized field norm. Integration gives the stated energies. Learned increments are handled by finite sums of the rank integral and cross-time contractions, not by taking a norm of the initial operator. The GD comparison in Section 5 above transfers these claims to the specified raw interpolation and node derivative convention.

### 12. Exchange symmetry, field support, and nonaffinity

**Read:** I.5.1–I.5.2, 1620–1733.

The reflection swapping the two equal-norm inputs is explicit. The parameter map \((V,W,w)\mapsto(V\mathcal R,W,-w)\) sends predictions and residuals to the negative swapped quantities, and backward fields to their negative swapped quantities. The two signs in each residual-times-delta update cancel. The raw metric and loss are preserved, so both finite GF and GD commute with the map. Gaussian initialization is invariant, including the actual small readout law.

Passing that finite law symmetry to deterministic limiting predictions and velocity norms yields \(f_2=-f_1\) and equality of the corresponding sample speed norms. At the orthogonal angle these are population law consequences, not finite sample-pair path identities. At the antiparallel angle the stronger raw identities are available separately. The proof respects that distinction.

The first-layer decomposition is \(F(G_a)\) plus a finite-variance Gaussian integral independent of the whole initial row, plus a bounded remainder. An event bounding the Gaussian integral has positive probability. Independent initial Gaussian tails can then force either arbitrarily large sign of the first preactivation. For orthogonal inputs the independent initial pair can force all four feature corners simultaneously in the support limit, proving positivity of the two-by-two first feature Gram. At the antiparallel angle the proof retains only its nonzero one-dimensional Gram.

The second-layer source variance is the positive first-feature second moment. Its bounded remainder cannot eliminate either Gaussian tail: the inclusions underlying I.83 do not require source/remainder independence. Both hidden preactivations therefore have unbounded tails at every deterministic finite time.

For each such \(L^2\) field \(Z\), the span of \(1,Z\) is closed because the affine-regression Gram determinant is \(\operatorname{Var}(Z)>0\). Hence zero best affine error would imply an attained identity \(\arctan Z=uZ+v\) almost surely. Boundedness of arctangent and an unbounded tail force \(u=0\); strict monotonicity then forces \(Z\) constant, a contradiction. This proves distributional regression nonaffinity, not merely nonaffinity of the scalar activation function in isolation. No uniform lower margin over all times is asserted.

### 13. Strict progress and every-positive-time activity

**Read:** I.5.3, 1735–1833; final scope 6384–6386.

With \(r=(f_1-1)y\) and \(\kappa=y^TKy/4\), multiplying \(\dot f=-2Kr\) by \(y^T/2\) gives

\[
\dot f_1=4(1-f_1)\kappa,
\qquad 1-f_1(t)=\exp\!\left[-4\int_0^t\kappa(v)\,dv\right].
\]

The integral is finite on each finite horizon. At zero, only the readout block survives, and its label contrast has positive variance in both geometries. Continuity gives initial positive progress; nonnegative \(\kappa\) then gives \(0<f_1(t)<1\) for every \(t>0\). In particular the readout field is nonzero at every such time.

Positive gates make every second delta nonzero. The reverse Gaussian source therefore has positive variance, and the bounded remainder makes every \(Q^{(1)}_a\) nonzero. Together with \(1-f_1>0\), this proves strict first preactivation, first activation and first-parameter speeds.

At the orthogonal angle, the positive definite first-feature Gram bounds the second-parameter speed below by a positive multiple of the sum of second-delta squared norms. At the antiparallel angle, its reduced velocity is a nonzero rank-one operator. The second preactivation velocities cannot both vanish because I.90 is an exact adjoint identity with a strictly positive sum of hidden-parameter speed squares on the right. Exchange equality of the sample speed norms then excludes either one vanishing separately. Positive gates give strict second activation speeds.

The readout velocity can vanish only if the second-feature contrast vanishes, since \(1-f_1>0\). That would force \(f_1=\mathbb E[W^{(3)}(H_1^{(2)}-H_2^{(2)})]/2=0\), contradicting positive progress. Thus it too is strictly positive. The continuous speed norms give positive energies on positive-length positive-time intervals. At zero the hidden speeds vanish because the limiting readout and deltas vanish, consistently with the theorem.

Asymptotic fitting would require \(\int_0^\infty\kappa=\infty\). None of the arguments above establish that divergence: strict positivity on every finite time or interval is insufficient. The introductory table, I.5.6 and the final scope qualification correctly refrain from asserting fitting or finite-optimizer endpoint convergence.

### 14. Initial reused-transpose law and change of the full kernel

**Read:** I.5.4–I.5.6, 1835–2086.

The finite conditional projection I.94 has the correct empirical normalization. The response term uses \(\Gamma_n^{-1}(\mathsf Z^T\widehat{\boldsymbol\delta}/n)\), while the Gaussian remainder covariance is \(\widehat{\boldsymbol\delta}^T\widehat{\boldsymbol\delta}/n\). The reduced limiting Gram is \(\mu_0 I\) or \(\mu_0\), so inverse boundedness is justified. The deltas are bounded; the \(Z\widehat\delta\) contraction is handled by Gaussian moments, not by claiming \(Z\) bounded. The finite-rank projection remainder is negligible by the already proved empirical moment estimate.

The resulting initial reverse law includes a response depending on the first features and an independent Gaussian component with the **full delta second moment** as covariance. The covariance is not reduced by subtracting the response variance. Its diagonal is strictly positive; the stated stronger orthogonal two-sample positivity also follows from full Gaussian support and nonconstancy of \(\phi'\). Thus the initial first hidden acceleration coefficients are nonzero even with the reused transpose.

The feature clock \(s(t)=\int_0^t4(1-f_1)\) has \(s(t)=4t+o(t)\). Its orthogonal equations have coefficient \(y_a/2\); its antiparallel one-field equations have coefficient one. They are the gradient of the prediction contrast in the same raw metric.

From the readout integral, \(W^{(3)}(s)/s\to\widehat W^{(3)}\) strongly in \(L^2\). The gate-times-fixed-field argument following I.67 justifies the delta and reverse-field limits I.98 and all leading velocity limits I.100. The rank contribution in I.99 uses the initial Gram \(\mu_0 I\), producing \(y_a\mu_0\widehat\delta_a^{(2)}/2\). The first contribution uses the actual initial operator on \(\phi'(G_a)^2\widehat Q_a^{(1)}\). No unproved second Fréchet derivative of an \(L^2\) nonlinear map is required.

The constant \(d_*>0\) in I.101 is the sum of leading first-parameter and second-parameter speed squares. Its factors \(1/4\) and \(\mu_0\) follow from the orthogonal feature Gram and the rank norm identity. I.103 gives the correct one-field constants at the antiparallel angle. The adjoint identity I.102 checks the sign of the readout-kernel contribution, which cannot be inferred merely from positive hidden motion.

In feature time,

\[
\kappa_{\rm hidden}(s)=d_*s^2+o(s^2).
\]

Differentiating the readout contrast norm and dividing by \(s\), I.102 yields limit \(2d_*\) for its derivative. Thus

\[
\kappa_{\rm readout}(s)=\kappa(0)+d_*s^2+o(s^2),
\qquad
\kappa(s)=\kappa(0)+2d_*s^2+o(s^2).
\]

This explicitly checks the possible cancellation in the **full** kernel: the two quadratic contributions have the same positive sign. Since \(s^2=16t^2+o(t^2)\), the physical-time coefficient is \(32d_*>0\), exactly as in I.107. The conclusion is an initial quadratic change, not a claim that the kernel is monotone forever or changes on every later interval.

## Classical tools and proof closure

No unprovided specialized Gaussian-program, mean-field, response, propagation-of-chaos, or finite-GD theorem was accepted. The chapter proves the specialized induction, singular-query removal, common operator construction, global response extraction, path moments and exact algorithm comparison internally.

The remaining classical uses have matching hypotheses:

- Integral fixed-point construction: complete path space, local boundedness and Lipschitz field, sufficiently short interval; the \(L^\infty\) readout-domain issue is removed explicitly.
- Scalar integral/Gronwall estimates: integrable controls and bounded state-dependent constants on each fixed horizon.
- Gaussian projection and integration by parts: finite-dimensional standard Gaussian arrays; invertible Grams only where regularized or reduced Grams are positive definite; moment/derivative bounds justify the expectations.
- Gaussian covariance square roots: finite-dimensional positive semidefinite matrices, including singular limits, with the needed continuity proved in the text.
- Conditional Chebyshev, Hölder and tail truncation: the required second or higher moments are furnished by I.45 or I.72.
- Fubini, dominated convergence and differentiation along curves: jointly measurable representatives and the stated integrable \(L^2\) bounds; unbounded cubic composition is handled by a scalar absolutely continuous identity instead of a false global \(L^2\) chain rule.
- Completion and density: the generated spaces are countably generated, the queried smooth-cylinder spans are dense, and bounded actions and their bilinear identity extend to the completions.
- Wasserstein upgrades: explicit grid/cell couplings and higher-moment tails accompany weak convergence; neither endpoint convergence nor a uniform RMS bound alone is treated as an all-orders path result.

The dependency chain closes within the assigned text: I.2 supplies deterministic well-posedness and algorithm stability; I.3 proves and realizes the finite Gaussian law and global remainders; I.4 establishes the declared observations and restores the actual initialization and raw GD; I.5 uses those results to prove symmetry, nonaffinity, activity and initial full-kernel change. The final disclaimer states the corresponding limits of Part I correctly.
