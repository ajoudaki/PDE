# Fresh isolated adversarial review B

## Verdict

**No required mathematical correction found.** The document establishes its stated actual finite GF/GD first-layer compactness theorem, the raw first-row increment/velocity reconstruction, and convergence of the entire node-controlled first kernel along every stipulated \(W_2\)-convergent subsequence.

This verdict is for the stated assumptions and conclusions: fixed deterministic normalized inputs with \(-1\leq\rho<1\), fixed finite horizon, the displayed sum loss and parameter scalings, and simultaneous raw GD with \(\eta_n=n^{-2}\) above the specified deterministic threshold. It is not a verdict on a full mean-field identification theorem. I found no need to add residual convergence, identify an unweighted kernel, match neuron indices across widths, reconstruct initial orthogonal row components, or prove equality of GF and GD limits.

The strongest adversarial check was an admissible family with all initial first-layer speed concentrated in one neuron and a nonzero coherent readout. Its instantaneous empirical speed stays of order one at time zero, while its time-integrated empirical speed vanishes. This does not contradict the theorem: the row-work estimate controls the integrated concentration, and the claimed speed/kernel convergence is in \(L^1\) in time. The detailed construction appears below.

## Source, isolation, and integrity

- Sole mathematical source read: [ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md](/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md).
- Source length checked: 1,623 lines, 66,690 bytes.
- Read coverage: the entire document, including the opening scope statement, all twelve sections, every displayed numbered equation (1)–(106), and the provenance appendix.
- Expected SHA-256: 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9
- Before-reading SHA-256: 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9
- After-reading-and-audit SHA-256: 910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9
- Integrity result: both observed hashes match the supplied hash. The source was not edited.

I did not open provenance dependencies, other project mathematics, histories, other reviews, or other-agent material. I used no experiments, subagents, external mathematical sources, or heavy imports. The checks below are direct algebraic and analytic checks of the sole permitted source. The appendix's historical claims and dependency hashes were read as metadata, not independently verified.

Line references below refer to this hashed source. The report itself is the only file created by this review.

## Theorem-obligation ledger

| Obligation | Source location | Result and decisive reason |
|---|---|---|
| Actual GF equations and global finite-width existence | §2, lines 284–327, (22)–(25) | Pass. The displayed metric gives exactly the stated dynamics; loss dissipation supplies a finite-distance endpoint at every putative finite terminal time. |
| Actual simultaneous raw GD descent | §§4–5, lines 525–768, (43)–(60) | Pass. A stopped-node argument bounds entire candidate segments before applying the Hessian estimate. The three threshold conditions close the argument without assuming stability. |
| Primal and actual transpose-query bounds | §§2, 4–5, (26)–(33), (43)–(54) | Pass. The coordinatewise readout bound controls the differentiated second-layer reverse field; no unsupported product estimate is used. |
| Row-work and stronger moments | §§3 and 5, (34)–(42), (55)–(62) | Pass. Positive semidefinite row work, bounded activations, and controlled-query variation yield a row action linear in the envelope. GD absorbs a quantitatively small Taylor remainder. |
| Strong velocity compactness | §§6–8, (63)–(86) | Pass. The relative gate estimate and cubic moment give translations; the step-function bound removes the GD mesh uniformly over all admissible widths. |
| One compact set for every good deterministic outcome | §8, lines 1045–1198 | Pass. Uniform finite-rank approximation and fourth moments give total boundedness of the whole family, followed by an explicit existence/closure argument. |
| Gaussian event probability and compact containment | §9, (87)–(91), theorem (13)–(14) | Pass. All three tail constants check; the final union bounds need no independence between good-event components or between schemes. |
| Population compatibility | §10, lines 1310–1341, (92) | Pass. Each required relation defines a closed condition in the actual strong product topology. |
| Actual raw-row increment/velocity reconstruction | §10, (93)–(97), theorem (16)–(17) | Pass. The increment is in the input span; \(DCD=D\) gives the reconstruction and the exact \(d\)-normalization. |
| No first-layer kinetic defect | §11, (98)–(101), theorem (18) | Pass. Small-cost \(W_2\) couplings give \(L^1\) convergence of the quadratic velocity observables. |
| Every node-controlled kernel entry | §11, (102)–(105), theorem (19)–(21) | Pass. The exact identity uses \(e=Dv\); the full matrix-valued quadratic map is continuous under these couplings. No division by residuals occurs. |
| Singular antiparallel endpoint | §6 and §§10–11, (63)–(69), (95), (102)–(105) | Pass. Actual architecture and opposite labels force \(e\in E_-\), eliminating the otherwise invisible nullspace component. |
| Correct finite GD interpretation | §§1, 5, 7, 11, especially (106) | Pass. Held node controls/deltas generate raw velocities, while activation derivatives use recomputed gates. The proof keeps these conventions distinct. |

## Detailed section-by-section verification

### Opening and §1: model, topology, and precise theorem

**Coverage:** lines 1–282; equations (1)–(21).

1. **Inputs, norms, and activation, (1)–(3).** The Gram matrix is symmetric positive semidefinite with eigenvalues \(1+\rho\) and \(1-\rho\), each in \([0,2]\). Input normalization excludes zero inputs. The interior case is invertible; the included singular case is exactly \(\rho=-1\). The arctan bounds are correct: \(|\phi|\leq B\), \(0<\phi'\leq1\), and
   \[
   |\phi''(s)|=\frac{2|s|}{(1+s^2)^2}
   \leq\frac1{1+s^2}\leq1.
   \]
   The ordinary versus empirical norm conventions are consistently maintained.

2. **Forward/backward fields and dynamics, (4)–(7).** The prediction has the specified factor \(1/n\); the reverse fields themselves do not contain an additional \(1/n\). Differentiating the sum loss gives the gradients in (23), and the raw metric gives exactly (6), including the \(1/d\) first-layer rate and the unnormalized readout rate. Equation (7) is the simultaneous Euler update for this field. No layer is silently updated using another layer's new value.

3. **Raw interpolation and laws, (8)–(9).** First preactivations are affine on raw GD cells, but the activated paths are their recomputed arctangents. Thus the first velocity is a held node quantity, and the activation velocity is the recomputed gate times that velocity. The law includes both samples and all four coordinates for the same neuron. The two velocity coordinates use strong \(L^2\), which is the topology subsequently proved compact.

4. **Deterministic hypotheses and compactness, (10)–(11).** Only the stated middle-matrix operator norm, readout coordinate bound, and first-preactivation fourth moment are assumed. No bound on an initial orthogonal first-row component is needed for these observables. The proof below does establish a compact set for the union over all admissible outcomes, including every GF width and every GD width above the threshold.

5. **Probability assertions, (12)–(14).** The finite Gaussian readout is retained. The event is independent of the chosen horizon, while the compact set and GD threshold can depend on the horizon. The joint bound \(b_n\) for shared initialization is justified by one common event; the bound \(2b_n\) for separate initializations is an ordinary union bound.

6. **Subsequence conclusions, (15)–(21).** Compatibility, raw increments, raw velocities, all three speed densities, and all controlled kernel entries are the relevant conclusions. The theorem asserts them along a \(W_2\)-convergent subsequence, with its own limiting neuron law. The use of a population expectation does not turn that law into an identified mean-field solution or into an expectation over initialization. The limit is an \(L^1\) time class, not a claim about point evaluations or almost-everywhere convergence of the original entire kernel sequence.

**Finding:** no normalization, topology, quantifier, or scope correction required.

### §2: raw metric, global GF, and differentiated reverse query

**Coverage:** lines 284–425; equations (22)–(33).

1. **Metric and gradients, (22)–(24).** Multiplying the three Euclidean gradient blocks by \(n/d\), \(1\), and \(n\), respectively, gives the raw gradient. Substituting \(c_a=-2r_a\) reproduces every line of (6). Therefore
   \[
   \frac{d}{dt}\ell=-\|\dot W\|_{\rm raw}^2
   \]
   has exactly the displayed block weights. There is no missing factor two from the sum loss.

2. **Local and global existence, (25).** The finite vector field is smooth, hence locally Lipschitz on finite-dimensional bounded balls. The integral-map construction yields a unique local solution. On its maximal interval the dissipation identity implies finite action. Cauchy–Schwarz gives
   \[
   \|W(t)-W(s)\|_{\rm raw}\leq\sqrt{(t-s)\ell(0)}.
   \]
   At fixed \(n,d\), this is a positive definite norm. A finite terminal time would therefore have a finite parameter limit, from which local existence extends the solution. This argument works for arbitrary finite initial parameters; it does not rely on a uniform width-dependent bound on the full first matrix.

3. **Primal constants, (26)–(28).** Initially \(|f_a|\leq B\beta\), so \(|r(0)|\leq R_0\). Loss decrease gives the control bound \(K_c^{\rm F}=2\sqrt2R_0\). The readout grows coordinatewise at rate at most \(BK_c^{\rm F}\). The middle-matrix rate is bounded by
   \[
   \frac1n\sum_a|c_a|\,|\delta_a^{(2)}|\,|h_a^{(1)}|
   \leq BK_c^{\rm F}\bigl(\beta+BK_c^{\rm F}t\bigr),
   \]
   whose integral is exactly the stated \(A_{\rm F}-\alpha\). All subsequent \(Q_{\rm F}\), second-primal, and reverse-field bounds follow from this operator bound and the coordinatewise readout bound. The first-primal estimate uses the initial fourth moment only to bound its empirical second moment by \(m^{1/2}\).

4. **Derivative constants, (29)–(31).** Each product-rule term is present. In particular,
   \[
   \|\dot\delta_a^{(2)}\|/\sqrt n
   \leq \|\dot W^{(3)}\|_\infty+
        \|W^{(3)}\|_\infty\|\dot z_a^{(2)}\|/\sqrt n,
   \]
   which justifies \(D_\delta=D_w+MD_Z\). Applying the operator norm to the two terms of \(\dot q_a^{(1)}\) then gives \(D_q=D_AM+AD_\delta\). This is a bound on the actual evolving transpose query, not on a substitute independent Gaussian query.

5. **Residual derivative, (32)–(33).** Differentiating the prediction in each raw parameter block gives the three displayed kernel terms with normalizations \(1/n\), \(1/n^2\), and \(1/n\). Thus \(\dot r=-2kr\), and \(\dot c=4kr\). The entry bound \(K_*=Q^2+M^2B^2+B^2\) implies \(\|k\|_{\rm op}\leq2K_*\), and hence
   \[
   \sum_a|\dot c_a|\leq
   \sqrt2\,4(2K_*)R_0=8\sqrt2K_*R_0.
   \]

**Finding:** all estimates close with constants independent of \(d,n,\rho\) as claimed.

### §3: GF row work and moment gain

**Coverage:** lines 428–523; equations (34)–(42).

1. **Controlled-query variation, (34)–(38).** The product rule for \(u_a=c_aq_a\), followed by the triangle inequality in empirical \(L^2\), gives (36). The sample-coordinate \(\ell^1\) inside the empirical \(L^2\) is correctly bounded by the sum of the individual sample \(L^2\) bounds. Minkowski over time gives the envelope bound \(V_{\rm F}\). There is no unproved coordinatewise bound on \(q\).

2. **Exact work identity, (39).** Treating a row as a column gives
   \[
   \dot W_i^{(1)}=Xe_i/d,\quad v_i=Ce_i,\quad
   d|\dot W_i^{(1)}|^2=e_i^TCe_i.
   \]
   Since \(e_{a,i}=\phi'(z_{a,i})u_{a,i}\) and
   \(s_{a,i}=\phi'(z_{a,i})v_{a,i}\), one also has
   \[
   \sum_a u_{a,i}s_{a,i}=e_i^Tv_i=e_i^TCe_i.
   \]
   Cross-sample terms are included by \(C\); no diagonal-only approximation is made.

3. **Integration by parts, (40).** The exact action is
   \[
   \mathcal A_i^{\rm F}
   =[u_i\cdot h_i]_0^T-\int_0^T\dot u_i\cdot h_i\,dt.
   \]
   Bounded activations bound both endpoint terms and the integral. The definition of the envelope gives the stated \(2B\upsilon_i\) bound. Positivity comes from \(C\succeq0\), so signs or cancellations in individual controls do not undermine this step.

4. **Speed and cubic gain, (41).** The eigenvalue inequality \(C^2\preceq2C\) gives \(|v_i|^2\leq2d|\dot W_i|^2\), while \(|v_i|\leq2\upsilon_i\). Their combination gives
   \[
   \int|v_i|^2\leq4B\upsilon_i,\qquad
   \int|v_i|^3\leq8B\upsilon_i^2.
   \]
   This is precisely the extra integrability that an action bound alone would not supply.

5. **Fourth moments, (42).** The displacement bound is
   \(\|z_i-z_i(0)\|_\infty\leq\sqrt{2T\mathcal A_i^{\rm F}}\).
   Raising the sum of the initial value and this displacement to the fourth power produces \(8m+128B^2T^2V_{\rm F}^2\). Squaring the integrated speed estimate produces the fourth moment of the \(L^2\) path norm with constant \(4BV_{\rm F}\) after taking the square root. Since \(|s_i|\leq|v_i|\), the activation-velocity estimates follow as stated.

**Finding:** the row-wise moment gain is valid, including at singular \(C\). It rules out the relevant integrated energy concentration.

### §4: actual raw GD and the noncircular descent argument

**Coverage:** lines 525–643; equations (43)–(49).

1. **Stopped-node bounds, (43).** Before a candidate exit, old-node residuals are bounded by \(R\). Summing the actual readout updates through that candidate endpoint gives \(M_{\rm G}\). Each middle-layer increment is bounded by \(\eta K_c^{\rm G}M_{\rm G}B\), yielding \(A_{\rm G}\). The total time is \(N\eta\leq T+1=H\). Convexity then bounds both norms at every point on each candidate segment. This establishes the segment bounds before loss descent is invoked.

2. **First derivatives, (44).** For a raw unit tangent, \(\|\xi^{(1)}\|_F\leq\sqrt{n/d}\), \(\|\xi^{(2)}\|_F\leq1\), and \(\|\xi^{(3)}\|\leq\sqrt n\). Multiplying by an input of norm \(\sqrt d\) gives the normalized first-hidden derivative bound. The product rule gives \(Ba_2+Aa_1\) for the second-hidden derivative. The prediction derivative is consequently bounded by \(B+M(B+A)=F_*\).

3. **Second derivatives, (45)–(46).** Both mixed middle/first terms and the first-activation curvature term are present. The latter can cost a factor \(\sqrt n\); the proof retains it. The estimate
   \[
   \|u\odot v\|/\sqrt n
   \leq\sqrt n\,(\|u\|/\sqrt n)(\|v\|/\sqrt n)
   \]
   is valid without coordinatewise tangent bounds. In the second-activation curvature contribution to \(D^2f_a\), however, the readout infinity norm permits the direct estimate
   \[
   \frac1n\left|\sum_i W_i^{(3)}\phi''(z_i^{(2)})
                      (D_\xi z_i^{(2)})(D_\zeta z_i^{(2)})\right|
   \leq MJ_0^2.
   \]
   Thus \(F_{**}(n)=2J_0+MJ_0^2+M(2+A\sqrt n)\) is justified.

4. **Residual and Hessian bounds on the segment, (47).** The raw gradient norm at an old node is at most \(K_cF_*\). Therefore every prediction changes by at most \(\eta K_cF_*^2\) on that segment. The first threshold condition makes its residual norm at most \(R+1\). The Hessian identity then gives
   \(4F_*^2+2\sqrt2(R+1)F_{**}(n)\), with no unbounded residual factor.

5. **Descent and exit closure, (48).** Taylor's formula along the actual simultaneous update yields the displayed half-step descent when \(\eta H_*(n)\leq1\). Since \(H_*(n)=O(1+\sqrt n)\), \(\eta=n^{-2}\) satisfies this eventually. Induction makes every candidate exit residual at most \(R_0<R\), excluding exit. No preceding estimate assumed the desired node loss decrease.

6. **Discrete action, (49).** Summing the descent inequality gives exactly one half of the full raw squared-speed sum bounded by \(\ell_0\). This concerns full raw cells through node \(N\), and therefore also bounds any restriction to \([0,T]\). It is not an exact within-cell loss identity, and the source does not use it as one.

**Finding:** actual GD stability and the threshold dependence are proved, not assumed.

### §5: GD query regularity, Taylor absorption, and partial cells

**Coverage:** lines 645–789; equations (50)–(62).

1. **Recomputed fields, (50)–(51).** The raw velocity is a held old-node update. Its first preactivation bound gives the recomputed activation-velocity bound through \(|\phi'|\leq1\). The product rules for \(z^{(2)},\delta^{(2)},q^{(1)}\) therefore hold almost everywhere inside each cell with the same constants as before. Continuity across the finitely many nodes allows their derivative estimates to be integrated to node increments.

2. **Control variation and exact product differences, (52)–(54).** The derivative bound for the recomputed control is
   \[
   \sum_a|\dot c_a|\leq4K_c^{\rm G}F_*^2,
   \]
   since there are two predictions and each control equals minus twice its residual. Each displayed product-difference formula uses the correct old/new factor. For \(\Delta(cq)\), the old \(q\) and new \(c\) are both bounded at their respective nodes after the descent argument. This proves the stated node \(u\)-increment estimate without identifying recomputed \(u(t)\) with its held counterpart.

3. **Primal bound, (53).** Integrating the actual first-preactivation velocity through at most \(H\) time units yields the displayed normalized bound, using only the initial moment and already proved speed estimate.

4. **Envelope, (55)–(56).** The envelope includes nodes \(0,\ldots,N-1\), precisely the nodes that generate velocities. The unused terminal control is not needed. Minkowski gives its empirical \(L^2\) bound, and the maximum-coordinate consequence is \(\max_i\upsilon_i\leq\sqrt nV_{\rm G}\). This latter bound precedes and justifies the Taylor absorption.

5. **Raw step and Taylor work, (57)–(58).** The first-row update gives \(\Delta z_i=\eta Ce_{k,i}\) and
   \(|\Delta z_i|^2\leq2\eta^2a_{k,i}\). Taylor expansion is of the recomputed activation difference at the two endpoints. Its signed controlled remainder is bounded in absolute value by
   \[
   \frac12\upsilon_i|\Delta z_i|^2\leq\eta^2\upsilon_i a_{k,i}.
   \]
   No positivity is needed for an individual \(u_{k,a,i}\).

6. **Summation by parts and absorption, (59)–(60).** Both endpoint terms and all intervening control differences occur in the summation-by-parts formula. Its absolute value is bounded by \(2B\upsilon_i\). On summing (58),
   \[
   (1-\eta\upsilon_i)\mathcal A_i^{\rm G}\leq2B\upsilon_i.
   \]
   The independently established condition
   \(\eta\upsilon_i\leq V_{\rm G}n^{-3/2}\leq1/2\)
   yields \(\mathcal A_i^{\rm G}\leq4B\upsilon_i\). The three threshold conditions involve no \(m,d,\rho\), and all coefficients are independent of \(n\), except the explicitly displayed \(O(\sqrt n)\) Hessian term.

7. **Partial terminal cell and moments, (61)–(62).** The work estimate was proved over complete cells up to \(N\eta\); restriction of a nonnegative speed integral to \([0,T]\) can only decrease it. This covers \(T\notin\eta\mathbb N\), including \(0<T<\eta\), when \(N=1\) and the envelope's variation sum is empty. The resulting constants are \(\int|v_i|^2\leq8B\upsilon_i\), \(\int|v_i|^3\leq16B\upsilon_i^2\), and
   \[
   \frac1n\sum_i\|z_i\|_\infty^4
   \leq8m+512B^2H^2V_{\rm G}^2.
   \]
   The actual activation derivative uses the recomputed gate, so \(|s_i|\leq|v_i|\) remains exact.

**Finding:** no endpoint, omitted-node, remainder-sign, or mesh-size correction required.

### §6: the exact antiparallel endpoint

**Coverage:** lines 792–852; equations (63)–(69).

1. **Architecture identities, (63)–(65).** Equality \(\rho=-1\) and input normalization imply \(x_2=-x_1\). Linearity and oddness propagate the sign change through both hidden layers and the linear readout. Evenness of \(\phi'\) makes both reverse deltas and transpose queries equal between samples. The actual opposite labels then give \(r_2=-r_1\) and \(c_2=-c_1\).

2. **Actual nonzero readout, (66).** These identities hold for every parameter state. They therefore hold in GF, at every GD node, and on every raw GD segment with any readout. There is no assumption of zero prediction or zero readout at initialization.

3. **Controlled range and inversion, (67).** Positions, activations, controlled queries, and controlled reverse fields lie in \(E_-=\{(b,-b)\}\). On this subspace \(C\) acts as multiplication by two. Thus \(v=2e\) and \(e=(C/4)v\). This is the necessary extra statement at the singular endpoint; the mere identity \(v=Ce\) would not suffice to reconstruct each controlled kernel entry.

4. **Interior and constants, (68)–(69).** The explicit inverse and its norm \(1/(1-|\rho|)\) are correct. At the endpoint \(C/4\) has eigenvalues \(0,1/2\), so its norm is \(1/2\). The proof treats this separately and makes no false uniform-in-angle or limiting-inverse assertion.

**Finding:** the singular endpoint is fully addressed under the actual architecture and labels.

### §7: strong translations uniformly over all GD widths

**Coverage:** lines 854–1043; equations (70)–(80).

1. **Assembled bounds, (70)–(71).** The \(\sqrt2\) in \(K_z\) correctly combines the two per-sample bounds into the same-neuron two-vector bound. Cubic space-time moments and fourth moments of the \(L^2\) path norm have different meanings, and the proof uses each in the appropriate place.

2. **Query and position translations, (72).** GF integrates the derivative estimates. GD crosses at most \(\tau/\eta+1\) node increments; each node first-preactivation increment is the cell velocity times \(\eta\). The actual affine preactivation has the sharper bound proportional to \(\tau\). All integrals are over \([0,T-\tau]\); there is no unjustified extension past the terminal cell or before zero.

3. **Relative arctan gate, (73)–(74).** The logarithmic derivative bound is correct. For positive gate values, the ratio of their difference to their sum is the stated hyperbolic tangent, giving the bound by \(\min(1,|x-y|/2)\). The algebra in (74) holds for signed controlled queries: the step using \(\phi'(x)|v|\leq|a|+\phi'(x)|u-v|\) is valid. Taking the largest coordinate gate ratio gives the same two-vector constants. This avoids a lower bound on gates or controls.

4. **Hölder estimate, (75).** Because \(e=Dv\), the controlled field has empirical space-time \(L^3\) norm at most \(\kappa_\rho J\). Also
   \[
   \|\theta\|_{L^6}^6\leq\|\theta\|_{L^2}^2
   \leq TK_z^2(\tau+\epsilon)^2/4.
   \]
   Hölder with \(1/2=1/6+1/3\) therefore produces the one-third power, and the two shifted controlled-field norms give the factor two. Multiplication by \(C\) costs at most two.

5. **First velocity and recomputed activation velocity, (76)–(77).** Squaring the preceding bound and absorbing the linear term on \(\tau+\epsilon\leq T+1\) gives (76). The activation-velocity difference is expanded using its actual recomputed gate, whose difference is bounded by \(\min(1,|\Delta z|)\). The last, mesh-free line of (72) supplies the additional \(\tau^{1/3}\) term in (77).

6. **Removal of the mesh, (78)–(79).** For \(\tau\leq\eta\), a held velocity differs from its shift only when a starting time crosses an internal node. There are at most \(T/\eta\) internal nodes, and each contributes a set of length at most \(\tau\). The pointwise empirical squared difference is at most \(4K_z^2\). This proves the stated \(\tau/\eta\) estimate even with a shortened terminal cell. For larger shifts the trivial \(4TK_z^2\) bound applies.

7. **Uniform modulus, (80).** Splitting at \(\delta=\tau^{3/5}\) is correct. If \(\eta\leq\delta\), then \((\tau+\eta)^{2/3}\leq2^{2/3}\tau^{2/5}\); if \(\eta>\delta\), then \(\tau/\eta\leq\tau^{2/5}\). The activation remainder is of squared size \(\tau^{2/3}\), which is smaller on \(\tau\leq1\). This proves a uniform bound over all admissible widths, not just a statement after taking \(n\to\infty\).

**Finding:** the crucial uniformity needed for compact containment is proved. The exponent \(2/5\) is correctly stated for the squared translation norm.

### §8: strong joint compactness, measure limits, and tightness

**Coverage:** lines 1045–1198; equations (81)–(86).

1. **Finite-rank projection, (81).** Uniform time averaging on velocities and polygonal interpolation on positions are bounded finite-rank maps in their respective topologies. The four coordinates remain in one tuple. Projection need not preserve the nonlinear compatibility relations to serve as a compactness approximation.

2. **Velocity error, (82).** The cell variance identity has factor \(1/(2h)\). Splitting into ordered pairs removes that factor two and leads to \(h^{-1}\int_0^h C_1\tau^{2/5}d\tau=(5C_1/7)h^{2/5}\). Enlarging within-cell pairs to all pairs with the same separation only increases a nonnegative integral.

3. **Position errors, (83)–(84).** Each of the two terms in the polygonal error is bounded by \(\sqrt h\) times the local velocity norm. The squared supremum error is at most \(4h\|v_i\|_2^2\). Applying this to both positions and activations yields the \(8hTK_z^2\) contribution. Coupling each atom with its own full projection proves the displayed \(W_2\) approximation.

4. **Fourth tuple moment, (85).** The square of a sum of four squared norms is bounded by four times the sum of their fourth powers. The two velocity-path contributions are each at most \(A_{\rm kin}^2\); the activation supremum contributes \(4B^4\). Both projection operations contract the relevant norms, so the same bound holds for projected laws.

5. **Finite-dimensional total boundedness.** Moving outside-ball mass to zero costs at most \(M_4/R^2\). A bounded finite-dimensional ball has finite nets in the inherited norm. Moving mass to representatives costs at most the squared cell diameter. On the resulting fixed finite set, nearby probability vectors can couple common mass identically, with the unmatched mass costing at most that mass times the squared support diameter. These steps give \(W_2\) total boundedness of every projected family; (84) transfers it to the entire original family.

6. **Existence of a subsequential law limit, (86).** All members of the original family are finite empirical measures, so successive near-optimal couplings are finite transport tables. The interval-splitting construction realizes all successive couplings on one probability space. Summability of their \(L^2\) distances implies almost-sure summability of their distances, and completeness of \(C\times L^2\times C\times L^2\) gives a limit. The summed \(L^2\) tail estimate then gives \(W_2\) convergence and a finite second moment for the limit.

7. **Closure compactness.** Approximating a sequence from the closure by original family members within \(1/j\) transfers the preceding subsequence result to the closure. The final open-cover argument correctly derives a uniform ball radius from sequential compactness and then uses a finite net to obtain a finite subcover.

8. **Gluing detail checked.** The triangle comparisons involving a limit law can use a finite empirical measure as their middle marginal. If its atoms have masses \(p_b\), restrict each coupling to the atom \(b\), normalize by \(p_b\), and glue the two outer conditional measures independently with weight \(p_b\). This is a finite mixture and gives the required triangle estimate by Minkowski. Thus the closure step does not require an unprovided general disintegration theorem.

9. **Direct tightness.** The set \(\mathcal C\) is closed because the norm and projection-error maps are continuous. It is totally bounded by its finite-rank approximations and complete as a closed subset of the complete path space. The tail estimate is
   \[
   M_4/R^4+\sum_{j\geq1}2^{2j}\varepsilon(h_j)
   \leq a/2+\sum_{j\geq1}a2^{-j-1}=a.
   \]
   This controls the path-space laws themselves, in addition to the compactness of the family in the measure space.

10. **Zero horizon.** For \(T=0\), both \(L^2\) coordinates are zero spaces, the remaining variables are finite-dimensional initial values and their arctangents, and the fourth moment suffices. All integrated velocity/kernel statements are statements in the zero time-integral space. The separate treatment avoids using the positive-horizon partition construction.

**Finding:** the compact set contains all good outcomes, including arbitrary selections at fixed admissible widths. No compactness theorem is being used with missing hypotheses.

### §9: Gaussian probabilities, measurability, and quantifiers

**Coverage:** lines 1200–1308; equations (87)–(91).

1. **Gaussian pair distribution.** At a fixed first row the evaluations have covariance \(X^TX/d=C\), and different rows are independent. The representation using two independent standard Gaussians remains valid at \(\rho=-1\).

2. **Moment constants, (87)–(88).** The Gaussian moment recurrence gives fourth moment \(3\) and eighth moment \(105\). Expanding the mixed square gives \(1+2\rho^2\). Hence
   \[
   \mathbb E|z_i(0)|^4=8+4\rho^2\leq12,\qquad
   \mathbb E|z_i(0)|^8\leq8(105+105)=1680.
   \]
   Independence across rows bounds the variance of the empirical fourth moment by \(1680/n\). Exceeding \(13\) requires a deviation of more than one from a mean at most \(12\), which justifies the Chebyshev bound. The endpoint \(\rho=-1\) has mean exactly \(12\), so the margin remains valid there.

3. **Middle-matrix tail, (89).** The packing construction gives a deterministic \(1/4\)-net with at most \(9^n\) points. Approximating the two unit test vectors loses at most half the operator norm, so the factor two is correct. Each fixed bilinear form has variance \(1/n\). An operator norm exceeding \(8\) forces a net bilinear form to exceed \(4\) in absolute value, with probability at most \(2e^{-8n}\). The two nets have at most \(9^{2n}\) pairs, giving exactly \(2e^{-(8-2\log9)n}\).

4. **Readout tail, (90).** Each readout coordinate has variance \(n^{-2}\), not \(n^{-1}\). Its threshold-one two-sided tail is bounded by \(2e^{-n^2/2}\), and the union over \(n\) coordinates gives \(2ne^{-n^2/2}\).

5. **Containment and coupling of schemes.** Summing the three tails proves (13). It is acceptable that the bound exceeds one for some small widths; it remains a valid bound and tends to zero. No independence between the three events is used. Shared initialization gives one event for both schemes; separate initializations give the bound \(2b_n\) even under an arbitrary joint coupling of those initializations. Cross-width independence is unnecessary.

6. **Measurability.** At fixed width, GD uses a finite number of continuous updates and a fixed time partition, giving continuous dependence in \(C\) and strong \(L^2\). For GF, the action bound controls nearby initial states on a common finite-dimensional ball through time \(T\); the smooth vector field is Lipschitz there. The displayed exponential bound gives continuous dependence of paths, and evaluating the vector field gives continuous dependence of velocities. Pairing equal indices at this fixed width proves continuity of the empirical-law map in \(W_2\).

7. **Tail-in-probability statements, (91).** On the good event, the fourth tuple moment yields \(F_n(R)\leq M_4/R^2\), and the cubic space-time moment yields \(L_n(R)\leq J^3/R\). For fixed positive threshold \(a\), choosing \(R\) large makes exceedance possible only on the bad event, for all sufficiently large admissible widths. This gives the stated iterated limits. It does not bound expectations on the bad event.

8. **Input and horizon quantifiers.** The probability constants are uniform for each deterministic normalized input pair and dimension. They do not describe one realization simultaneously controlling input pairs selected after seeing the weights. The same good event can be used for each fixed horizon, with horizon-dependent deterministic constants and thresholds. No eventual-goodness conclusion along all widths is inferred from the nonsummable displayed bound.

**Finding:** the probability assertions survive adversarial dependence and outcome selection in exactly the form claimed.

### §10: population compatibility and raw first-row reconstruction

**Coverage:** lines 1310–1396; equations (92)–(97).

1. **Couplings.** Near-minimizers of the defining \(W_2\) infimum provide squared costs \(\varepsilon_n^2\to0\). An optimal coupling is not assumed. The coupling is between complete same-neuron tuples and does not presuppose any correspondence of original neuron indices across widths.

2. **Closed compatibility, (92).** The integral map is continuous from \(L^2\) to \(C\), with norm at most \(\sqrt T\). The activation map is continuous in the uniform norm. For the derivative product, the displayed decomposition fixes the limiting \(v\) in the gate-difference term, proving continuity under uniform \(z\) and strong \(L^2\) \(v\) convergence. Thus all four compatibility statements define a closed set. The bounded distance-to-set test under a small-cost coupling proves that the limit law is supported on this set. The endpoint subspace constraints are closed as well.

3. **Exact raw-row identities, (93)–(95).** Both schemes give \(\dot W_i=Xe_i/d\), with held \(e_i\) in GD, and §6 gives \(e_i=Dv_i\). In both cases \(DCD=D\), so
   \[
   A_{\rm row}^TA_{\rm row}=D/d,\qquad
   d|\dot W_i|^2=v_i^TDv_i,\qquad
   \|A_{\rm row}\|_{\rm op}^2=\kappa_\rho/d.
   \]
   At \(\rho=-1\), \(e=(b,-b)\) gives \(v=(2b,-2b)\) and
   \(d|\dot W_i|^2=4b^2=|v|^2/2\), confirming the normalization directly.

4. **Increment and joint-law convergence, (96).** Integrating the raw velocity gives the actual row increment. The map \((z,v,h,s)\mapsto(A_{\rm row}[z-z(0)],A_{\rm row}v)\) is Lipschitz with squared constant at most \(4\|A_{\rm row}\|_{\rm op}^2\). Pushing the chosen couplings through it proves \(W_2\) convergence. Retaining the input tuple adds its original transport cost, establishing the claimed joint version.

5. **What is not reconstructed, (97).** The matrix \(P=XDX^T/d\) is symmetric idempotent with range equal to the input span, including at the endpoint. Consequently
   \[
   W_i(t)=A_{\rm row}z_i(t)+(I-P)W_i(0).
   \]
   The constant orthogonal component is correctly excluded from the reconstructed observables. Its arbitrary size under the deterministic hypotheses is not a flaw in the increment theorem.

**Finding:** all reconstruction claims use actual raw rows with the correct input and width factors.

### §11: measurable time formulas, kinetic convergence, and the full kernel

**Coverage:** lines 1398–1551; equations (98)–(106).

1. **Representatives, (98).** Uniform time averages are bounded linear functions of an \(L^2\) class and give jointly measurable averaged paths. Density of finite interval-step functions proves their \(L^2\) convergence for each path. Their squared error is dominated by \(4\|V\|_2^2\), so convergence also holds in product \(L^2(\mu\times dt)\). A subsequence with summable increments supplies a jointly measurable representative agreeing with the original class for almost every path. This justifies the timewise expectation formulas without treating point evaluation as continuous on \(L^2\).

2. **Squared speeds, (99).** In a small-cost coupling, \(|M_n-M|\leq\varepsilon_n\), so the sum of the \(L^2\) moment norms is bounded. The inequality
   \[
   \bigl||v|^2-|V|^2\bigr|\leq|v-V|(|v|+|V|)
   \]
   followed by Cauchy–Schwarz in time and the coupling gives the stated \(L^1\) error. The fourth coordinate gives the activation-speed result by the same valid estimate.

3. **Raw quadratic speed, (100)–(101).** The symmetric form \(D\) obeys
   \[
   |v^TDv-w^TDw|\leq\kappa_\rho|v-w|(|v|+|w|).
   \]
   Combining this with (93) gives the raw first-matrix speed limit. For any fixed measurable time set, its integral error is bounded by the full \(L^1\) error. The normalization is \(d/n\) times the ordinary squared Frobenius speed, exactly as in the raw metric.

4. **Finite controlled kernel, (102).** Since each control is common across neurons for its sample, it can be brought inside the empirical sum. With the node convention in GD,
   \[
   j_{n,ab}=C_{ab}\frac1n\sum_i e_{a,i}e_{b,i}
   =C_{ab}\frac1n\sum_i(Dv_i)_a(Dv_i)_b.
   \]
   This is exact; it does not require convergence of the residuals, division by them, or reconstruction of the unweighted deltas.

5. **Full matrix continuity, (103)–(105).** Expanding \(ee^T-ff^T\) yields the claimed Frobenius bound. Entrywise multiplication by \(C\) is contractive in that norm because each entry has absolute value at most one. Applying \(D\) twice gives the factor \(\kappa_\rho^2\). Integrating and coupling therefore gives
   \[
   \|j_n-J\|_{L^1(F)}
   \leq\kappa_\rho^2\varepsilon_n(M_n+M)\to0.
   \]
   This handles all four entries together. The integrability and representative construction already justify the expectation defining \(J\).

6. **Sum and positivity checks.** The sum of all four entries is
   \[
   (Dv)^TC(Dv)=v^TDv
   \]
   using \(DCD=D\). At the endpoint a row contributes \(b^2\) to each entry, so the total is \(4b^2\), in agreement with raw row energy. The positivity identity is the diagonal congruence of \(C\) by the vector \(Dv\), hence valid. Positivity or the trace alone would not prove full-entry convergence; the source correctly uses the separate matrix estimate.

7. **GD loss derivative, (106).** The held raw velocity is \(-g_k\), so the actual derivative of the recomputed loss is
   \(-\langle\operatorname{grad}_{\rm raw}\ell(W(t)),g_k\rangle_{\rm raw}\).
   The proof correctly distinguishes this from \(-\|g_k\|_{\rm raw}^2\). Its controlled-kernel statement concerns held node fields, not a recomputed in-cell kernel.

8. **Compactness of observables.** The row-law map is Lipschitz, and the speed and matrix maps are continuous on \(\mathcal P_2(\mathcal E_T)\) by the coupling estimates just proved. Their joint image, retaining the original law, of the compact set in (11) is compact. On the good event all actual observables equal these images, so the joint containment probability has the same bound.

**Finding:** there is no first-layer kinetic defect along the prescribed subsequences, and the proof establishes matrix-valued \(L^1\) convergence, not merely a scalar energy limit.

### §12 and the appendix

**Coverage:** lines 1553–1623.

- Compact containment of all good deterministic outcomes indeed supplies subsequences for arbitrary sequences of such outcomes, including interleaving GF and admissible GD.
- The assertions about any already \(W_2\)-convergent subsequence follow from the exact identities and continuity arguments; uniqueness or convergence of a full width sequence is unnecessary.
- The listed exclusions match the proof: full mean-field identification, all-layer limits, unweighted-kernel recovery at vanishing controls, in-cell/node-kernel equivalence, full-sequence almost-everywhere time convergence, bad-event expectations, varying-angle uniformity, \(\rho=1\), and full-row reconstruction are not asserted.
- The statement about obtaining almost-everywhere convergence along a further subsequence from summable \(L^1\) errors is correct.
- The appendix is a provenance record. No proof step above needs a theorem from a listed dependency. I did not verify its historical assertions or open any listed dependency; that is consistent with the isolated-review instruction.

**Finding:** no excluded conclusion is needed to validate the theorem actually proved.

## Adversarial falsification attempts

### 1. A good outcome with all initial kinetic energy in one neuron

Fix any allowed input pair and positive \(\alpha,\beta\). Let \(a=n^{-1/2}(1,\ldots,1)^T\), and let \(e_1\) denote the first coordinate vector in the width space. Choose
\[
W^{(1)}_0=0,\qquad
W^{(2)}_0=\alpha a e_1^T,\qquad
W^{(3)}_0=\beta(1,\ldots,1)^T.
\]
These satisfy (10) with first-preactivation moment zero, \(\|W^{(2)}_0\|_{\rm op}=\alpha\), and \(\|W^{(3)}_0\|_\infty=\beta\). Taking \(\alpha=\beta=1\) also places them inside the displayed event \(E_n\). These coherent deterministic values are legitimate tests of a theorem quantifying over every good outcome; their being atypical under Gaussian initialization is irrelevant.

At time zero, both hidden preactivations and activations vanish, both predictions vanish, and \(c=(2,-2)\). For both samples,
\[
q_a^{(1)}(0)=\alpha\beta\sqrt n\,e_1.
\]
Consequently only the first neuron moves initially, with
\[
e^{(1)}_1(0)=2\alpha\beta\sqrt n(1,-1),\qquad
v^{(1)}_1(0)=2\alpha\beta\sqrt n(1-\rho)(1,-1).
\]
Its empirical instantaneous preactivation-speed density is
\[
\frac1n\sum_i|v_i^{(1)}(0)|^2
=8\alpha^2\beta^2(1-\rho)^2,
\]
and its empirical raw first-layer speed is
\[
g_n^{(1)}(0)=8\alpha^2\beta^2(1-\rho).
\]
The initial controlled kernel is also nonzero and independent of width:
\[
j_n^{(1)}(0)
=4\alpha^2\beta^2
\begin{pmatrix}1&-\rho\\-\rho&1\end{pmatrix}.
\]

This is a genuine stress test of strong compactness, not merely a hypothetical \(L^2\) array. The other first-layer neurons remain zero under either actual scheme: their activations are zero, their middle-matrix columns are zero, the corresponding middle-column updates remain zero, and their first-row updates therefore remain zero. GF uniqueness or GD induction preserves this invariant set.

For the single active row, (38) or (56) gives \(\upsilon_1\leq V\sqrt n\), with a fixed scheme-appropriate \(V\). The row-work estimates imply
\[
\frac1n\int_0^T|v_1(t)|^2dt=O(n^{-1/2}),\qquad
\frac1n\|z_1\|_\infty^2=O(n^{-1/2}).
\]
The activation position contributes at most \(2B^2/n\), and its integrated speed is no larger than the preactivation speed. Thus the full empirical tuple law converges in \(W_2\) to the point mass at the zero tuple. The raw action and full controlled kernel converge to zero in \(L^1\) by the same estimates and \(e=Dv\).

**Outcome:** this family defeats an unwarranted uniform-in-time speed or kernel conclusion, but does not defeat the stated theorem. It confirms that the integrated row-work gain is doing necessary mathematical work.

### 2. Concentrated initial position mass

Take \(W^{(2)}_0=W^{(3)}_0=0\), so both schemes are stationary. Choose a realizable two-vector \(b\), and let the first initial preactivation pair be \(n^{1/4}b\), with all others zero. In the interior every two-vector is realizable; at the antiparallel endpoint take \(b\in E_-\). Then
\[
\frac1n\sum_i|z_i(0)|^4=|b|^4,
\qquad
\frac1n\sum_i|z_i(0)|^2=|b|^2n^{-1/2}.
\]
Thus the moment hypothesis permits growing individual initial positions, but their quadratic contribution vanishes. The bounded activated coordinate causes no difficulty.

**Outcome:** no counterexample. The fourth moment, rather than a uniform coordinate bound, supplies the needed quadratic-tail control.

### 3. Concentration on arbitrary neuron sets or space-time sets

If a set of neurons has empirical mass \(p\), Cauchy–Schwarz and (71) give
\[
\frac1n\sum_{i\in A}\|v_i\|_2^2\leq A_{\rm kin}\sqrt p.
\]
For any measurable subset \(B\) of neuron-time space, with empirical counting times Lebesgue measure \(\lambda_n\), the cubic bound gives
\[
\int_B|v|^2\,d\lambda_n\leq
J^2\lambda_n(B)^{1/3}.
\]
In particular, these sets can be chosen after seeing the trajectory. Whole-tuple tails are additionally controlled by \(M_4/R^2\). The proof's deterministic inequalities do not assume independent particles or a favorable choice of the exceptional set.

**Outcome:** neither rare rows nor rare time intervals can carry a persistent missing integrated kinetic mass.

### 4. Rapid oscillations with bounded energy

Uniform moment bounds alone would allow velocities such as a fixed-amplitude sine with frequency tending to infinity. Their shifts at half a period have nonvanishing squared \(L^2\) distance, so such a family is not strongly compact.

Here that construction would violate (80): at a shift tending to zero, the empirical squared shift norm must tend to zero uniformly. The controlled-query derivative/increment estimate, relative gate estimate, and step-function bound establish precisely this missing restriction for actual trajectories.

**Outcome:** no gap from confusing energy boundedness with strong velocity compactness.

### 5. A final partial cell, a single cell, and shifts across a node

When \(T/\eta\) is nonintegral, the proof estimates full cells through \(N\eta\leq T+1\), then restricts nonnegative integrals to \([0,T]\). When \(T<\eta\), the single generating node suffices and the summation-by-parts formula has only its two endpoint terms. For a shift shorter than a cell, each crossed internal node contributes starting-time measure at most \(\tau\); the shortened terminal cell creates no extra internal node.

**Outcome:** the work, moment, and translation estimates remain valid in all these cases. No replacement of \(T\) by an integer multiple of the step is tacitly assumed.

### 6. Vanishing controls and very small gates

At an interior angle, if \(e=(0,b)\), then \(v=(\rho b,b)\), which may have two nonzero coordinates. Nevertheless \(Dv=(0,b)\), so the recovered controlled kernel has the required zero first row and column. The proof never attempts to infer \(\delta_1\) by dividing by a vanishing \(c_1\).

If both residuals vanish, all raw updates vanish and all corresponding controlled first-layer quantities are zero. If a gate is arbitrarily small, (73)–(75) still hold because they use a relative difference estimate with positive gates, not a positive uniform lower bound.

**Outcome:** no residual nonvanishing or gate nondegeneracy assumption is missing.

### 7. Singular inputs and an invisible controlled field

For \(C=\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\), an arbitrary field \(e=(b,b)\) would give \(v=0\) but the nonzero controlled matrix
\[
C\odot ee^T=b^2C.
\]
Thus applying a pseudoinverse without controlling the nullspace would invalidate full kernel reconstruction.

The actual model forbids this attempted counterexample: even reverse fields and opposite residuals force \(e\in E_-\) at every raw state. This remains true for a nonzero readout and along raw GD segments. At \(d=1\), the allowed normalized nonidentical inputs necessarily fall into this antiparallel case. At \(\rho=0\), \(D=I\) and the off-diagonal controlled entries vanish by the displayed factor \(C_{12}=0\).

**Outcome:** the endpoint supplement resolves the actual obstruction; it is not merely a formal pseudoinverse substitution.

### 8. Correlations approaching an endpoint

In the interior, nearly null directions make \(D\) large. The source explicitly permits compactness and reconstruction constants to depend on the fixed correlation and excludes uniformity for varying correlations approaching an endpoint.

**Outcome:** divergent interior inverse bounds do not contradict the fixed-angle theorem. No varying-angle conclusion is needed.

### 9. Unbounded initial orthogonal row components

When the input span is a proper subspace of \(\mathbb R^d\), arbitrarily large vectors orthogonal to both inputs can be added to the initial first rows. They change neither the evaluated initial fields nor any subsequent update, and remain constant. Full raw-row laws could then fail to be tight despite (10).

**Outcome:** this does not affect the theorem, which reconstructs increments and velocities and explicitly retains the missing constant component in (97).

### 10. Arbitrary couplings and adversarial good-outcome selection

All estimates up to compact containment hold for every admissible parameter outcome. Choosing the worst such outcome at every width, repeating widths, or interleaving schemes therefore stays inside the same compact set.

For subsequential convergence, the proof needs only the existence of couplings with cost tending to zero, which is precisely supplied by \(W_2\) convergence. It does not assert that every arbitrarily chosen high-cost coupling has small cost. Within a coupling, keeping both samples and all four coordinates together avoids an invalid independent matching of different observables.

For original initialization randomness, arbitrary dependence across widths or between separately initialized schemes does not change the one-width tail calculations or their union bounds. The proof does not infer almost-sure eventual goodness from the displayed nonsummable bound, or expected-energy convergence from high-probability containment.

**Outcome:** the deterministic and probabilistic quantifiers are correctly separated and withstand these coupling choices.

## Required corrections versus optional wording

### Required mathematical corrections

**None identified.** In particular, I found no failed theorem obligation, invalid normalization, circular GD stability assumption, uncontrolled Taylor remainder, missing partial-cell case, failure of uniform compactness over good deterministic outcomes, unsupported probability strengthening, endpoint nullspace error, or uncontrolled quadratic-kernel passage.

### Optional exposition only

1. In §8, the sentence about coupling triangle inequalities could explicitly mention the finite-middle-marginal mixture construction described in this report. This would make the closure argument easier to check for a reader seeking the fully elementary proof. The construction supplies the step under the existing hypotheses; no new assumption or theorem conclusion is needed.

2. At the \(T=0\) discussion, one could explicitly assign \(n_0(0,\alpha,\beta)=1\). With no GD updates and zero velocity spaces, this is already implicit. It is a convenience for the theorem's threshold notation, not a missing mathematical case.

Neither suggestion is needed to change the mathematical verdict, and neither was applied to the source.

## Final assessment

The document proves the scoped actual finite-dynamics result. Its critical mechanisms are present and correctly connected: actual query regularity, positive row work with a linear envelope bound, the relative arctan gate estimate, a mesh-uniform velocity translation bound, finite-rank \(W_2\) compactness, and exact linear/quadratic reconstruction of the controlled observables.

The source before and after the audit has the supplied SHA-256. No source edit or external dependency inspection was performed.
