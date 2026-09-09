# Isolated adversarial audit: stopped raw-GD cavity trace approximation

## Verdict and audit boundary

**PASS for the stopped approximation stated for the explicitly defined algorithm (4).** I found no substantive mathematical gap, counterexample, missing normalization, omitted nonlinear product, invalid conditioning step, or source-indexing error that invalidates (34), (35), or (78)–(79). This verdict follows from checking the calculations below, not from accepting the source's proof labels.

The result is conditional on the cavity initialization event and concerns one deterministic distinguished neuron, through the minimum of the two node stops, including the stopping node and incoming interpolation cells. It does not establish stop removal, a bounded limiting trace, a closed limiting equation, or convergence of solutions of such an equation. None of those stronger conclusions is needed for this verdict.

There are **no required mathematical corrections** for that scope. Optional clarifications appear at the end, particularly the meaning of “raw GD”: the updates use different effective learning rates in the three raw parameter blocks. They are not common-learning-rate Euclidean descent in the unscaled raw parameters.

### Isolation and source integrity

- Sole source read: /tmp/l2-two-sample-proof-0ywjpp/CAVITY_STOPPED_TRACE_RAW_GD_TEST.md.
- Entire source read: **1,199 lines, 47,728 bytes**, in consecutive ranges 1–200, 201–440, 441–680, 681–920, and 921–1199. A subsequent equation/heading index was obtained from that same source.
- No project, history, other review, dependency, skill, or referenced predecessor file was read. The predecessor's historical provenance and hash quoted by the source were not independently verified and are not premises of this audit.
- No experiments, external imports, external research, other agents, or source edits were used. The only file written was this requested review, using apply_patch.
- Source SHA-256 before the audit: 5453ebedc1b4989aec222857feedd6ed53be87945b5c02a5359e552de5572d2d.
- Source SHA-256 after the audit: 5453ebedc1b4989aec222857feedd6ed53be87945b5c02a5359e552de5572d2d.
- Source integrity result: **IDENTICAL before and after**. The second hash was computed after the full audit and review body had been written; only these integrity fields in the review were finalized afterwards. The source was never edited.

## Detailed coverage table

Line ranges refer to the source. Every numbered display, (1)–(81), is covered. “Pass” means the claim was checked with the hypotheses available where it is used.

| Source location | Coverage and adversarial check | Result |
|---|---|---|
| Lines 1–37 | Scope and dependency boundary; whether an earlier theorem is silently assumed | No earlier mathematical assertion is needed. Historical provenance deliberately not verified. |
| Lines 38–78; (1)–(3) | Gram matrix, initialization, activation regularity, ordinary norms | Pass. \(C\) is positive definite; \(\xi\sim N(0,C)\). Both first activations have the bounded derivatives used. |
| Lines 80–118; (4)–(6) | Signs, factors \(2,n,d\), simultaneous evaluation, first-layer projection, interpolation | Pass for (4). Raw block rates are \(\eta n/d,\eta,\eta n\) for the loss in (18). |
| Lines 120–165; (7)–(8) | Cavity measurability, root in conditioning, node stops, equality cases | Pass. Only \(g\) is excluded from conditioning; first-hit definitions include equality. |
| Lines 167–198; (9)–(10) | Global bounds without loss monotonicity or survival | Pass. Bounded output activation closes the readout recursion; matrix increments are \(O(\eta)\) in Frobenius norm. |
| Lines 200–240; (11)–(13) | Recomputed derivatives, cell moduli, overshoot, stop at zero | Pass. Field derivatives are \(O(\sqrt n)\); no positive-cell claim is made when \(s=0\). |
| Lines 242–281; (14)–(16) | Trained-column restoration and direct/learned/bulk decomposition | Pass. Both \(g^TD^{\rm dir}\ell\) and the complete \(\ell^T\delta\) are retained. |
| Lines 283–296; (17) | Coordinate dimension and raw-row metric | Pass. Dimension \(n^2+2n-2\); metric weights \(d/n,1,1/n\). |
| Lines 298–325; (18)–(20) | Scaled-coordinate gradient and fixed external input | Pass. Holding \(E\) fixed gives the exact bulk update at \(E=e_k/\sqrt n\). |
| Lines 327–395; (21)–(25) | First variations, residual derivative, transpose term, trained outer products | Pass. No residual, matrix, feature, or readout variation is missing. |
| Lines 397–410; (26) | Map norms and the sole threshold-dependent term | Pass. Only first-layer curvature multiplying cavity \(q\) needs its coordinate maximum. |
| Lines 412–426; (27) | Operator moduli for recomputed cavity queries | Pass. Third derivatives suffice; no affine-hidden-field assumption. |
| Lines 428–448; (28)–(29) | Ordered products and post-freeze extension | Pass. Later factors are on the left; post-freeze products are explicitly an independent artificial extension. |
| Lines 450–493; (30)–(32) | Source insertion, fractional forcing, endpoint agreement, trace dimension | Pass. Kernel is \(L_kU(k,r+1)\mathcal B_r\); current source uses \(P=I\). |
| Lines 495–560; (33)–(37) | Quantifiers, probability, rates, Gaussian-law scope, measurability | Pass after the estimates below. \(A_*\) can be independent of \(K\); fixed-\(K\) errors vanish. |
| Lines 562–602; (38)–(39) | Linear and nonsymmetric quadratic Gaussian tails | Pass. Direct calculation gives the thresholds, optimizer, and constants. |
| Lines 604–640; (40)–(42) | Test families, \(O(n^6)\) count, union bound, norm tail | Pass. All tests are cavity-dependent and cover deterministic nodes before actual stopping is imposed. |
| Lines 642–675; (43)–(45) | Recurrence solution, adaptive features, Euclidean/coordinate bounds | Pass. Uniform kernel bounds justify arbitrary bounded feature histories. |
| Lines 677–693; (46) | Continuum extension | Pass. Old sources compare to \(k\); current source compares to \((k+1,k)\). No uncountable union bound. |
| Lines 695–760; (47)–(51) | Taylor hypotheses, upper cross term, backward/residual remainders | Pass. Remainder scale \(D_*(\alpha+D_*/\sqrt n)\), with another \(1/\sqrt n\) for the residual. |
| Lines 762–780; (52) | Every first-layer product remainder | Pass. Six contributions are present; only \(r_p\widehat q\) needs \(R_n+1\). |
| Lines 781–797; (53) and readout remainder | Every matrix and readout product remainder | Pass. All six matrix terms and three readout terms satisfy the stated norms. |
| Lines 799–812; (54) | Physical differences at equal upper input | Pass. Neither a coordinate maximum nor a small secant is needed. |
| Lines 814–841; (55)–(57) | Actual old-node stability and forcing sensitivity | Pass. The curvature product uses actual \(q\), not comparison-state or secant \(q\). |
| Lines 843–872; (58)–(59) | Discrete consistency and iteration to stopping node | Pass. No time-discretization approximation; last step starts at \(s-1\). |
| Lines 874–900; (60)–(61) | Coordinate, Euclidean, and residual comparisons | Pass. No extra \(\sqrt n\) in the backward difference; no independent-root replacement. |
| Lines 902–922; (62) and first (34) | Zero-input readback and adaptive trace replacement | Pass. Zero-input linear coordinates are separately covered by row tests. |
| Lines 924–945; (63) | Learned history, both backward factors, old residual replacement | Pass. Total error \(O(H_n/\sqrt n)\). |
| Lines 947–964; (64) | Direct diagonal comparison, trained readout, \(\ell\) term | Pass. Upper/readout coordinate errors control \(D^{\rm dir}-D\). |
| Lines 966–982; (65) | Initial upper mismatch, step-zero source, \(s=0\) | Pass. Initial scalar is not falsely asserted Gaussian. |
| Lines 984–1010; (66)–(67) | Affine response and endpoint transfer | Pass with usual endpoint convention \(Y(N\eta)=Y_N\). Only raw coordinates are interpolated in this argument. |
| Lines 1012–1043; (68)–(70) | Response/root increments and query coordinate controls | Pass. Query \(h_a(t)\) needs only boundedness for (70). |
| Lines 1045–1077; (71)–(73) | Recomputed fields and zero-input readback inside cells | Pass. Static expansions at the moving cavity point supply the nonlinear comparison. |
| Lines 1079–1088; (74) | Query quadratic readback and total source weight | Pass. \(\sum_r\omega_r(t)=t\); no factor counting nodes or queries. |
| Lines 1090–1099; (75) | Query learned term with old-node sources | Pass. Only the readback factor is evaluated at the query. |
| Lines 1100–1112; (76) | Query direct term and combined errors | Pass. Contributions fit within \(H_n^{30}(a_n+b_n)\). |
| Lines 1114–1152; (77)–(79) | Actual root equation, old/query replacements, integration | Pass on included cell interiors, hence almost everywhere. |
| Lines 1154–1180; (80)–(81) | Net argument and initialization probabilities | Pass. These estimates concern initialization only. |
| Lines 1182–1199 | Established/open boundary | Accurate. No continuation, limiting closure, or uniform trace bound is established implicitly. |

## 1. Exact GD normalization and bulk coordinates

Use the specified loss \(\mathcal L=\sum_a(f_a-y_a)^2\), with \(c_a=-2(f_a-y_a)\). Direct differentiation gives

\[
\begin{aligned}
-\nabla_{W^{(1)}}\mathcal L
 &=\frac1n\sum_a c_a[\phi_1'(z^{(1)}_a)\odot q_a]x_a^T,\\
-\nabla_A\mathcal L
 &=\frac1n\sum_a c_a\delta_a(h^{(1)}_a)^T,\\
-\nabla_w\mathcal L
 &=\frac1n\sum_a c_a h^{(2)}_a.
\end{aligned}
\]

Consequently (4) uses raw learning rates

\[
(\eta_{W^{(1)}},\eta_A,\eta_w)=(\eta n/d,\eta,\eta n).
\]

The factor \(2\) is already in \(c\). Neither \(q\) nor \(\delta\) includes the first-layer gate, which appears exactly once in the first update. Multiplication by \(x_b\) gives

\[
\Delta z^{(1)}_{b,i}
 =\eta\sum_a C_{ba}c_a\phi_1'(z^{(1)}_{a,i})q_{a,i}.
\]

This verifies (6), including the distinguished root and every \(d\)-factor. All factors on this right-hand side are evaluated at the old node.

For a moving row, \(\Delta W_i=\sum_a b_a x_a^T\) gives

\[
\Delta z_i=dCb,\qquad
\|\Delta W_i\|^2=d\,b^TCb,\qquad
\Delta z_i^TC^{-1}\Delta z_i=d\|\Delta W_i\|^2.
\]

The squared bulk-coordinate displacement is therefore exactly

\[
\frac dn\|\Delta W_I\|_F^2+\|\Delta B\|_F^2+\frac1n\|\Delta w\|^2.
\]

Orthogonal first-row components never move. There are \(2(n-1)+n(n-1)+n=n^2+2n-2\) coordinates. The changes of variables have derivatives \(\partial z_i/\partial u_i=\sqrt n C^{1/2}\) and \(\partial w/\partial v=\sqrt n I\); applying them to the raw gradients proves (19). A common step \(\eta\) in these coordinates gives (20).

In the bulk partial derivative the distinguished raw column and row are fixed. Thus the actual physical input \(e_k=A_{:,j,k}h_{j,k}\) is held fixed in \(F(X_k,e_k/\sqrt n)\). Its dependence on the past trajectory does not change this partial derivative. The source handles this distinction correctly.

The covariance assertions also follow directly: each first-layer row has covariance \(I_d/d\), so its two preactivations have covariance \(C\); the column \(g\) has covariance \(I_n/n\) and is independent of every retained initialization variable, including \(\xi\). Fixed \(\rho\in(-1,1)\) makes the coordinate transform invertible. No dependence on \(d\) remains in the bounds.

## 2. Global bounds, freezing, and stopping endpoints

Bounded \(\phi_2\) gives \(|f_a|\leq\|\phi_2\|_\infty M_k\), hence

\[
1+M_k\leq(1+C\eta)^k(1+M_0)\leq2e^{C(T+1)}.
\]

This bounds residuals independently of first-layer parameter sizes and \(q\). Then

\[
\|\Delta A_k\|_F
\leq\frac\eta n\sum_a|c_a|\|\delta_a\|\|h^{(1)}_a\|
\leq C_T\eta.
\]

The initial spectral norm is at most \(8+2=10\). Summation bounds \(A\); bounded gates give the remaining Euclidean bounds. The cavity uses denominator \(n\), so its bounds are identical. Freezing and raw interpolation preserve them. No descent lemma or loss monotonicity is needed.

On a raw cell, parameter derivatives are old-node update velocities:

\[
\|\dot z^{(1)}_a\|_2=O(\sqrt n),\qquad
\|\dot A\|_F=O(1),\qquad \|\dot w\|_\infty=O(1).
\]

The product/chain rules give the three recomputed derivatives preceding (11). Each upper, backward, and \(q\) derivative is \(O(\sqrt n)\). Also

\[
\dot f_a=\frac1n\left[\dot w^Th^{(2)}_a+
w^T\operatorname{diag}(\phi_2'(z^{(2)}_a))\dot z^{(2)}_a\right]=O(1).
\]

Thus vector fields move by at most \(C_T\eta\sqrt n=C_Tb_n\) in a cell, and residuals by \(O(\eta)\). An incoming cell starts below \(R_n\), so its entire coordinate maximum, including the endpoint, is at most \(R_n+C_Tb_n\). Cavity initialization equality is allowed by \(\mathcal C_n\) and remains safe.

If the actual stop is zero, its initial maximum need not satisfy the overshoot bound. The proof never uses that bound in this case: there is no positive included cell, and the initial identities still apply. If \(s=N\), the node theorem may include \(N\eta>T\); all bounds use \(T+1\), while the query interval is cut at \(\tau\).

The cavity stop is a measurable function of \(\mathcal F_{-j}\). Its frozen extension and all extended kernels are deterministic after conditioning. The actual stop is not; it appears only later in deterministic comparisons. In particular, a continuous crossing inside an incoming cell does not invalidate the node-stop argument, and restricting to such a crossing requires no new conditioning.

The column formula (14) follows by summing exactly its simultaneous updates. Each increment has norm at most \(C_T\eta/\sqrt n\), so \(\|\ell(t)\|\leq C_T/\sqrt n\). The fundamental theorem of calculus for \(\phi_2'\) proves (15). Expanding
\((g+\ell)^T(\delta^0+D^{\rm dir}(g+\ell)h)\)
gives (16), with the entire \(\ell^T\delta\) in \(M\). Its size is \(O(1)\), as is \(S\). No column-history or cross term has been omitted.

## 3. Complete first variations, norms, and ordered sources

For \(Y/\sqrt n\) in bulk coordinates, physical increments are \(\Delta z_i=C^{1/2}u_i=\zeta_i\), \(\Delta B=V/\sqrt n\), and \(\Delta w=v\). Including physical input \(e\),

\[
\begin{aligned}
dz^{(2)}_a&=VH_a/\sqrt n+\widehat BP_a\zeta_a+e_a=\lambda_a,\\
d\delta_a&=V_av+D_a\lambda_a,\\
dq_a&=V^T\widehat\delta_a/\sqrt n+\widehat B^Td\delta_a,\\
dc_a&=-\frac2n[v^T\widehat h^{(2)}_a+\widehat\delta_a^T\lambda_a]=\chi_a.
\end{aligned}
\]

These reproduce (22)–(23). Differentiating \(c\phi_1'q\) gives three variations; differentiating \(c\delta H^T\) gives \(\chi\delta H^T+c\,d\delta H^T+c\delta(P\zeta)^T\); differentiating \(c h^{(2)}\) gives \(\chi h^{(2)}+cV_a\lambda\). They are exactly (24), including the trained transpose and both outer-product factors.

The normalization of (25) is exact:

\[
\left.\frac d{d\epsilon}\right|_0
\sqrt n F(\widehat X+\epsilon Y/\sqrt n,\epsilon e/\sqrt n)
=D_XF\,Y+D_EF\,e.
\]

For map bounds, \(\|VH_a/\sqrt n\|\leq C\|V\|_F\), \(\|V^T\widehat\delta_a/\sqrt n\|\leq C_T\|V\|_F\), and
\(|\chi_a|\leq C_T(\|Y\|+\|e\|)/\sqrt n\).
The latter cancels the \(\sqrt n\) size of the residual-gradient vectors. In the matrix block, the \(O(n)\) outer product is multiplied by both \(1/\sqrt n\) and \(\chi=O((\|Y\|+\|e\|)/\sqrt n)\). Only \(\widehat c\phi_1''\widehat q\zeta\) requires the coordinate maximum \(R_n+1\); it vanishes for a pure input variation. This proves (26), including an \(R_n\)-independent source bound.

For (27), first-gate increments use \(\phi_1''\), second-gate increments use \(\phi_2''\), and increments of \(D\) use \(\phi_2'''\) and \(\Delta w\). They are \(O(b_n)\) in operator norm. Further, \(\Delta B=O(\eta)\) and \(\|\Delta\widehat\delta\|/\sqrt n=O(\eta)\). Substitution into \(Z,L,Q\) proves all map moduli, including \(B^TD\). Frozen cells give zero increments. No fourth derivative or derivative of \(J(t)\) is needed.

At the first two nonzero response nodes,

\[
Y_1=\eta\sum_b\mathcal B_{b,0}gh_{b,0},
\]

\[
Y_2=\eta\sum_b A^c_1\mathcal B_{b,0}gh_{b,0}
    +\eta\sum_b\mathcal B_{b,1}gh_{b,1}.
\]

There is no \(A^c_0\) acting on the source from step zero. A step-\(r\) source enters at node \(r+1\) and is subsequently multiplied by \(A^c_{r+1},\ldots,A^c_{k-1}\), in that order of action. This is precisely \(U(k,r+1)\), with later factors on the left. Multiplicative norm bounds prove (29) without commuting Jacobians.

At a fractional step, previous sources acquire \(I+\theta\eta J_k\), and the new source is \(\theta\eta\mathcal B_{b,k}gh_{b,k}\). At the next endpoint, previous products become \(U(k+1,r+1)\), and the new source has \(U(k+1,k+1)=I\). This verifies every case of (31), endpoint agreement in (32), and the \(n\times n\) trace dimension. The post-freeze extension is legitimate because it is used only to make a deterministic Gaussian test family; it is not claimed to be the derivative of the frozen transition.

## 4. Conditional Gaussian estimates and adaptive features

After fixing the cavity, \(g=Z/\sqrt n\) with \(Z\sim N(0,I_n)\). Completing the square and optimizing exponential Markov gives (38).

For a nonsymmetric \(K\), only \(S=(K+K^T)/2\) contributes. Diagonalization gives

\[
g^TKg-\operatorname{Tr}K/n
=\frac1n\sum_i\lambda_i(Z_i^2-1).
\]

Writing \(v=\|S\|_F\), \(b=\|S\|_{\rm op}\), direct Gaussian integration and the logarithmic series give

\[
\log\mathbb E e^{t(g^TKg-\operatorname{Tr}K/n)}
\leq\frac{t^2v^2/n^2}{1-2|t|b/n}.
\]

For \(v>0\), the stated optimizer \(t=n\sqrt x/(v+2b\sqrt x)\) is admissible. Its product with the threshold \(2v\sqrt x/n+2bx/n\), minus this moment bound, equals \(x\). Replacing \(S\) by \(-S\) gives the other tail; \(v=0\) is immediate. Thus (39), including its constants and nonsymmetric applicability, is correct.

The largest output family has \(O(n^2)\) rows, and there are \(O(N^2)=O((T+1)^2n^4)\) source/readback pairs. The finite sample/map labels and the smaller extra families give \(M_n\leq C(T+1)^2n^6\). Consequently

\[
2M_ne^{-\log(2M_nn^{p_*})}=n^{-p_*}.
\]

All matrices are cavity-determined on the full deterministic range. No actual feature, stop, or random query is inserted into them. Their row/operator norms are at most \(H_n\), and their symmetric Frobenius norms at most \(\sqrt nH_n\), after choosing \(A_*\). Linear and quadratic deviations are \(O(H_na_n)\) and therefore fit within \(H_n^2a_n\). Also

\[
\Pr(\|g\|>2)\leq e^{-n}2^{n/2}
=e^{-(1-\log2/2)n}\leq e^{-n/2}.
\]

No independence between this norm event and the test events is needed.

Actual features are inserted afterwards through pathwise bounds:

\[
\eta\sum_{r<k,b}|h_{b,r}|\leq2B_1(T+1),\qquad
\sum_{r,b}\omega_r(t)|h_{b,r}|\leq2B_1t.
\]

A simultaneous kernel deviation bound \(u_n\) therefore gives a weighted deviation at most \(2B_1(T+1)u_n\) for every such feature sequence, including sequences depending on \(g\). The same applies to row actions. This proves (44)–(45) without assigning a Gaussian law to \(Y^{\rm lin}\). The identity-row family controls the first-coordinate and readout increments; the \(Z,L,Q\) families control all other stated coordinates.

For \(r<k\), the query kernel difference is

\[
[L_a(t)-L_{a,k}]U(k,r+1)\mathcal B_{b,r}
+L_a(t)\theta\eta J_kU(k,r+1)\mathcal B_{b,r},
\]

which is \(O(H_n^3b_n)\). For \(r=k\), compare to \(L_{a,k+1}\mathcal B_{b,k}\); (27) gives the same bound. The other readback row families work identically. On \(\|g\|\leq2\), row actions change by at most twice their operator difference and

\[
|g^TEg-\operatorname{Tr}E/n|\leq5\|E\|_{\rm op}.
\]

This proves a uniform cell extension of the finite-test event. The \(D(t)\) and \(\widehat B(t)^TD(t)\) families extend directly using (27). There is no uncountable union bound or conditioning at a stopping time.

Finally, \(G_a(t)=g^T\widehat\delta_a(t)\) is a deterministic linear image of the original conditional Gaussian, with covariance \(\widehat\delta_a(t)^T\widehat\delta_b(u)/n\). The source correctly limits this assertion to the original conditional law, not its restriction to the good event or survival.

## 5. Nonlinear defect: all product terms checked

In this section abbreviate \(D_*\) by \(D_0\), distinguishing it from the diagonal gate \(D_a\), and put \(r=D_0(\alpha+D_0/\sqrt n)\). Bounded derivatives give

\[
\|r_1\|_2+\|r_p\|_2\leq C\alpha D_0,\qquad
\|\Delta h^{(1)}\|_2\leq CD_0.
\]

The exact upper-field increment is

\[
\Delta z^{(2)}=\lambda+
\underbrace{\widehat Br_1+(V/\sqrt n)\Delta h^{(1)}}_{\beta}.
\]

Thus \(\|\beta\|\leq C_T(\alpha D_0+D_0^2/\sqrt n)=C_Tr\). Under \(\alpha\leq1\) and \(D_0/\sqrt n\leq1\), also \(\|\Delta z^{(2)}\|\leq C_TD_0\). The Euclidean forcing need not be small: Taylor expansion is first applied to the coordinate-small vector \(\lambda\), and Lipschitz continuity handles the remaining displacement \(\beta\).

The upper activation and backward field satisfy

\[
\Delta h^{(2)}=V_a\lambda+r_2,\qquad
\Delta\delta=d\delta+r_\delta,\qquad
\|r_2\|+\|r_\delta\|\leq C_Tr.
\]

The trained-readout cross term is bounded by

\[
\|v\odot[\phi_2'(\widehat z^{(2)}+\Delta z^{(2)})
              -\phi_2'(\widehat z^{(2)})]\|
\leq C\|v\|_\infty\|\Delta z^{(2)}\|
\leq C_T\alpha D_0.
\]

The next two remainder identities are exact:

\[
r_q=\widehat B^Tr_\delta+(V/\sqrt n)^T\Delta\delta,
\qquad
r_c=-\frac2n[\widehat w^Tr_2+v^T\Delta h^{(2)}].
\]

They imply

\[
\|r_q\|\leq C_Tr,\quad |r_c|\leq C_Tr/\sqrt n,\quad
\|\Delta q\|+\|\Delta\delta\|\leq C_TD_0,\quad
|\Delta c|\leq C_TD_0/\sqrt n.
\]

For example, the two residual remainder contributions are \(O(r/\sqrt n)\) and \(O(D_0^2/n)\), and the latter is at most \(O(r/\sqrt n)\). This verifies the important extra normalization on the residual.

For a term-by-term check of (52), suppress the sample label, write \(\psi=\phi_1'\), and interpret vector products coordinatewise.

| Exact first-layer remainder contribution | Euclidean bound, up to \(C_T\) |
|---|---|
| \(\widehat c\,\psi(\widehat z)r_q\) | \(r\) |
| \(\widehat c\,r_p\widehat q\) | \((R_n+1)\alpha D_0\) |
| \(\widehat c\,(\Delta\psi)\Delta q\) | \(\alpha D_0\) |
| \(r_c\psi(\widehat z)\widehat q\) | \(r\), using \(\|\widehat q\|_2=O(\sqrt n)\) |
| \(\Delta c(\Delta\psi)\widehat q\) | \(\alpha D_0\), using the same Euclidean bound |
| \(\Delta c\psi(z)\Delta q\) | \(D_0^2/\sqrt n\) |

Expansion of \((\widehat c+\Delta c)(\psi(\widehat z)+\Delta\psi)(\widehat q+\Delta q)\) and subtraction of the three first variations produces precisely these six terms. The cubic product is included in the last expression with \(\psi(z)\).

The six matrix terms in (53) satisfy:

| Exact normalized matrix remainder contribution | Frobenius bound, up to \(C_T\) |
|---|---|
| \(\widehat c\,r_\delta H^T/\sqrt n\) | \(r\) |
| \(\widehat c\,\widehat\delta r_1^T/\sqrt n\) | \(\alpha D_0\) |
| \(\widehat c\,\Delta\delta(\Delta h^{(1)})^T/\sqrt n\) | \(D_0^2/\sqrt n\) |
| \(r_c\widehat\delta H^T/\sqrt n\) | \(r\) |
| \(\Delta c\,\Delta\delta H^T/\sqrt n\) | \(D_0^2/\sqrt n\) |
| \(\Delta c\,\delta'(\Delta h^{(1)})^T/\sqrt n\) | \(D_0^2/\sqrt n\) |

Here \(\|\delta'\|\leq C_T\sqrt n\): the comparison readout maximum is bounded by \(\|\widehat w\|_\infty+\alpha\). The readout remainders \(\widehat c r_2\), \(r_c\widehat h^{(2)}\), and \(\Delta c\Delta h^{(2)}\) have bounds \(C_Tr,C_Tr,C_TD_0^2/\sqrt n\). Summing samples and applying the fixed \(C^{1/2}\) proves (47).

This checks both outer-product factors and every residual cross term. Only the first-layer \(r_p\widehat q\) term requires the threshold. The activation hypotheses suffice: Taylor expansion of \(\phi_1'\) and \(\phi_2'\) uses their second derivatives, namely \(\phi_1'''\) and \(\phi_2'''\); no fourth derivative is hidden. The sign of the compactly supported \(p\) is never needed.

## 6. Actual old-node stability and discrete error budget

For two bulk states at equal physical input \(e\), let \(W=\sqrt n(X-X')\). Physical first-layer and readout differences have norm \(O(\|W\|)\); the matrix difference has Frobenius norm at most \(\|W\|/\sqrt n\). Exact product differences give

\[
\|\Delta z^{(2)}\|+\|\Delta\delta\|+\|\Delta q_I\|
\leq C_T\|W\|,\qquad
|\Delta c|\leq C_T\|W\|/\sqrt n.
\]

For example, \(\Delta B h^{(1)}+B'\Delta h^{(1)}\) has this bound. Bounded spectral and readout-maximum norms at the two states suffice, even for large \(W\); no smallness or maximum along an intervening parameter segment is used.

In (55), the first residual term is bounded by \(|\Delta c|\|q\|=O(\|W\|)\). The gate-difference term is bounded by
\(C_T\|q\|_\infty\|\Delta z^{(1)}\|\leq C_TR_n\|W\|\).
The backward-difference term is \(O(\|W\|)\). Crucially, the \(q\) in the gate term is the actual old-node field. Thus (56) needs no maximum bound at the approximate state, the next node, or a secant point.

At fixed bulk state, varying physical input gives \(d\delta=D_a\,de\), \(dq=B^TD_a\,de\), and \(dc=-2\delta^Tde/n\). Substitution into the normalized field blocks bounds their variation by \(C_T\|de\|\). First-layer gates do not move in this derivative. Bounded readout and spectral norms hold along the input segment because they are fixed, so integration proves (57), independently of \(R_n\).

For the approximate response, (44)–(45) give \(D_0\leq H_n\), \(\alpha\leq H_n^3a_n\). Since \(a_n\geq1/\sqrt n\) for \(n\geq3\),

\[
r\leq(H_n^4+H_n^2)a_n\leq2H_n^4a_n.
\]

Choose \(A_*\) large enough that \(2C_T(1+R_n)\leq H_n^2\); this is possible uniformly for \(R_n\geq0\), without dependence on \(K\). Equation (47) then gives the \(H_n^6a_n\) defect in (58). The approximate matrix and readout are bounded because
\(\|V\|_F/\sqrt n\leq H_n/\sqrt n\) and \(\|v\|_\infty\leq H_n^3a_n\).
The condition \(H_n^{40}(a_n+b_n)\leq1/2\) is stronger than each required smallness condition.

The input difference is exactly \(\ell_k h_k\), with norm \(O(1/\sqrt n)\). It is not an omitted order-one forcing. At \(k<s\), both the actual and the cavity update identities are available. Combining them with the exact response recurrence gives

\[
E_{k+1}\leq(1+C_T\eta(1+R_n))E_k
 +\eta(H_n^6a_n+C_T/\sqrt n),\qquad E_0=0.
\]

Direct iteration yields

\[
E_k\leq(T+1)e^{C_T(1+R_n)(T+1)}
(H_n^6a_n+C_T/\sqrt n)\leq H_n^9a_n
\quad(k\leq s).
\]

This is a discrete comparison, not a comparison to gradient flow. There is no missing time-discretization remainder. Every invoked update starts below \(s\), and the final one starts at \(s-1\), so the stopping endpoint is included. If \(s=0\), the only discrepancy is exactly zero.

The field expansions at the approximate state, followed by (54) and the small input difference, prove (60). For the upper field, the coordinate-small linear part is \(\lambda\), and the Euclidean-small nonlinear part is \(\beta\). The \(Q\)-row tests control the backward coordinates after the matrix transpose. Both ingredients are necessary and present.

In Euclidean norm, the bulk difference is at most \(H_n+E_k\leq2H_n\). The physical forcing has bounded norm. The backward difference is consequently \(O(H_n)\), and the output normalization supplies the residual difference \(O(H_n/\sqrt n)\), as in (61). These statements do not require any closeness between the distinguished root and its initialization.

## 7. Node readback and complete learned-term replacements

At zero upper input, \(Z_aY_k^{\rm lin}\) is coordinate-small because the row family (40) includes \(Z_a\) itself. One need not infer this solely from a bound on \(Z_aY_k^{\rm lin}+gh_{a,k}\). The same static expansion and the bulk error give

\[
\|\delta^0_{a,k}-\widehat\delta_{a,k}-L_{a,k}Y_k^{\rm lin}\|
\leq H_n^{12}a_n.
\]

After multiplication by \(g\) and substitution of (43), the scalar is a sum of \(h_{b,r}g^TK_{ab}(k,r)g\), plus \(O(H_n^{13}a_n)\). The simultaneous quadratic event replaces every quadratic form by its normalized trace. The bounded total source weight gives \(O(H_n^2a_n)\), proving the first line of (34) through the exact split (16).

The exact trained-column history is

\[
M_{a,k}=\frac\eta n\sum_{r<k,b}
c_{b,r}h_{b,r}\delta_{b,r}^T\delta_{a,k}.
\]

Replacing its two backward factors uses the identity

\[
\delta_{b,r}^T\delta_{a,k}
-\widehat\delta_{b,r}^T\widehat\delta_{a,k}
=(\delta_{b,r}-\widehat\delta_{b,r})^T\delta_{a,k}
+\widehat\delta_{b,r}^T(\delta_{a,k}-\widehat\delta_{a,k}).
\]

The difference is \(O(H_n\sqrt n)\) before division by \(n\), because unchanged factors keep their global \(O(\sqrt n)\) norm. Residual replacement costs \(O(H_n/\sqrt n)\) after normalization. The bounded old-feature/time weights give (63). Both source residuals and both trained backward factors are accounted for.

For the direct term,

\[
\|e_{a,k}\|_\infty
\leq B_1(\|g\|_\infty+\|\ell_k\|)
\leq C_TH_n^2a_n.
\]

Its base \(Bh_I=z^{(2)}-e\) differs coordinatewise from the cavity upper input by at most \(H_n^{13}a_n\). The readout-coordinate difference, bounded \(\phi_2''\), and bounded \(\phi_2'''\) then give
\(\|D_a^{\rm dir}-D_a\|_{\rm op}\leq H_n^{14}a_n\).
Explicitly,

\[
\begin{aligned}
S_{a,k}-d_{a,k}h_{a,k}
=h_{a,k}\big[&
g^T(D_a^{\rm dir}-D_a)g
+(g^TD_ag-\operatorname{Tr}D_a/n)\\
&+g^TD_a^{\rm dir}\ell_k\big].
\end{aligned}
\]

The three terms have sizes \(O(H_n^{14}a_n)\), \(O(H_n^2a_n)\), and \(O(1/\sqrt n)\), respectively. This proves (64) with room in \(H_n^{16}a_n\). Combining the three scalar errors fits within \(H_n^{20}a_n\).

At node zero, bulk parameters agree but the upper mismatch is exactly \(g\phi_1(\xi_a)\). Thus \(\delta^0_0=\widehat\delta_0\), \(\ell_0=0\), and

\[
q_{a,j,0}=G_{a,0}+\phi_1(\xi_a)g^TD_{a,0}^{\rm dir}g.
\]

The initial residual difference is precisely (65), obtained by subtracting the two normalized outputs. The response starts at zero but its step-zero forcing, including \(\chi\)'s residual variation, is present. Nothing here assigns a Gaussian law to the complete initial scalar. These identities also cover \(s=0\).

## 8. Whole-cell recomputation and error accounting

On an included cell, raw interpolation is affine interpolation in \(X\): first preactivations are linear in \(W^{(1)}\), and the other blocks are scaled raw parameters. The response satisfies the exact identity

\[
Y(t)=(I+\theta\eta J_k)Y_k
 +\theta\eta\sum_b\mathcal B_{b,k}gh_{b,k}.
\]

Its discrepancy from \(\sqrt n(X(t)-\widehat X(t))\) is therefore the affine combination of the two endpoint discrepancies. Convexity of the norm proves (67). If the last cell is cut at \(T\), its right endpoint is still covered by the node theorem even when beyond \(T\).

This raw-coordinate argument would not suffice for hidden fields. The source supplies the additional estimates:

- The recurrence bounds \(\|Y(t)-Y_k\|\) by \(H_n^2\eta\).
- Cavity-map changes are \(O(b_n)\), so changes in \(Z_aY,L_aY,Q_aY\) cost \(O(b_nH_n+H_n^2\eta)\).
- Query forcing \(gh_a(t)\) is coordinate-small using \(\|g\|_\infty\) and \(|h_a(t)|\leq B_1\). The term \(B^TDg\) uses its node row test and operator modulus.
- Static expansions at the moving cavity state, followed by actual-minus-approximate comparison and the \(O(1/\sqrt n)\) input correction, establish (71)–(73).

For zero-input readback, the pure \(Z_a(t)Y(t)\) coordinates are controlled as well; removing the bounded direct \(gh_a(t)\) term costs only its already small coordinate norm. The Taylor conditions follow from \(D_0\leq H_n\), \(\alpha\leq H_n^6(a_n+b_n)\), and the theorem's smallness condition.

The current direct input uses \(h_a(t)\), but the response history uses the actual old-node features \(h_{b,r}\), including \(h_{b,k}\) for the fractional source. The source correctly distinguishes these two uses.

Multiplying the recomputed zero-input estimate (72) by \(g\), inserting (66), and using the extended quadratic event gives (74). The total time weight is \(t\leq T\); there is no accumulated per-query error.

The exact query learned term is

\[
M_a(t)=\frac1n\sum_{r,b}\omega_r(t)c_{b,r}h_{b,r}
                      \delta_{b,r}^T\delta_a(t).
\]

Only its readback factor is evaluated at \(t\). The same two-factor identity as above, with node bounds at each source and (73) at the query, proves (75). Direct-term replacement uses (71), the bounded \(\phi_2'''\), the small coordinate forcing, and the deterministic extension of the quadratic bound for \(D(t)\); it proves (76). This includes the trained readout, the full \(\ell(t)\) term, and all within-cell gate changes.

The error powers have adequate margins. Fixed constants can be absorbed by one sufficiently large \(A_*\):

| Quantity | Available bound | Use |
|---|---|---|
| Node static defect | \(H_n^6a_n\) | Forcing per unit time in the discrete error recursion |
| Node/affine bulk response error | \(H_n^9a_n\) | (59), (67) |
| Node zero-input readback vector error | \(H_n^{12}a_n\) | (62) |
| Node bulk-response scalar error | \(O(H_n^{13}a_n)+O(H_n^2a_n)\) | First line of (34) |
| Node learned-column replacement | \(C_TH_n/\sqrt n\) | (63) |
| Node direct replacement | \(H_n^{16}a_n\) | (64) |
| Both final node errors | At most \(H_n^{20}a_n\) | (34) |
| Query linear coordinate control | \(H_n^6(a_n+b_n)\) | (70) |
| Query field/zero-input readback errors | \(H_n^{15}(a_n+b_n)\), \(H_n^{16}(a_n+b_n)\) | (71), (72) |
| Query bulk-response scalar error | \(O(H_n^{18}(a_n+b_n))\) | (74) |
| Query learned-column replacement | \(C_TH_n/\sqrt n\) | (75) |
| Query direct replacement | \(H_n^{20}(a_n+b_n)\) | (76) |
| Both final query errors | At most \(H_n^{30}(a_n+b_n)\) | (35) |

There is no circular use of smallness: the linear response is constructed and bounded on the full independent-kernel event first; its nonlinear defect and bounded comparison-state norms follow; old-node stability then transfers it to the actual bulk. Actual bulk closeness is not assumed in obtaining that stability.

The powers are conservative but sufficient. The distinct \(b_n\) scale records query-map motion and recomputed-field cell moduli; it is not a gradient-flow approximation error.

## 9. Root equation, initialization probability, and asymptotics

The exact root derivative is the old-node expression (77). Replacing its residual by the cavity query residual costs

\[
C_TR_n(\eta+H_n/\sqrt n).
\]

The actual root moves by \(O(\eta R_n)\) inside the cell, so gate replacement costs \(C_T\eta R_n^2\). Finally, the old backward scalar differs from the query trace representation by at most

\[
C_Tb_n+\varepsilon_n^{\rm cell},
\]

using first the actual recomputed-field cell modulus and then (35). This does not require separately bounding \(G\) or differentiating the trace kernels.

These three costs give the first bound in (79), and absorption into \(H_n^{35}(a_n+b_n)\) is valid. The equation holds on included cell interiors and hence almost everywhere. The raw root preactivation is absolutely continuous, so integration gives at most \(T H_n^{35}(a_n+b_n)\). For a stop at zero the integration interval has zero length. No uniqueness or solution-comparison theorem for a separate closed equation is being used.

For (80), disjoint radius-\(1/8\) balls around a maximal \(1/4\)-separated subset of the unit sphere fit in a radius-\(9/8\) ball. This gives at most \(9^k\) points and a covering net. Approximating both vectors in a bilinear form loses at most \(\frac12\|B_0\|_{\rm op}\), so

\[
\|B_0\|_{\rm op}\leq2\max_{\text{net pairs}}|u^TB_0v|.
\]

There are at most \(9^{2n-1}\leq9^{2n}\) pairs, each form has variance \(1/n\), and threshold \(4\) has tail \(2e^{-8n}\). Thus

\[
\Pr(\|B_0\|_{\rm op}>8)
\leq2e^{-(8-2\log9)n}.
\]

For (81), \(nw_{l,0}\sim N(0,1)\), so the coordinate tail and union bound give
\(2n\cdot n^{-(q_*+2)}=2n^{-(q_*+1)}\).
On the two complementary events,

\[
\|\widehat q_{a,0}\|_\infty
\leq\|B_0\|_{\rm op}\|\widehat\delta_{a,0}\|_2
\leq8\|\phi_2'\|_\infty\sqrt n\,\|w_0\|_\infty.
\]

This is the stated \(O(\sqrt{\log n/n})\) bound. For fixed \(K>0\), it is eventually below \(K\sqrt{\log n}\), and the readout threshold is eventually below one. Hence the advertised probability of \(\mathcal C_n\) is correct. This calculation gives no positive-time survival result.

For every fixed exponent \(m\),

\[
\log H_n^m=mA_*(1+K\sqrt{\log n})=o(\log n).
\]

Therefore \(H_n^ma_n=n^{-1/2+o(1)}\), \(H_n^mb_n=n^{-3/2+o(1)}\), and all final errors vanish. The width conditions are eventually satisfiable at fixed parameters, without implying practical finite widths. Polynomial factors in \(1+R_n\) can be absorbed in \(e^{A(1+R_n)}\) with \(A\) independent of \(K\).

The coefficient bounds use
\(|\operatorname{Tr}K|/n\leq\|K\|_{\rm op}\),
\(|d_a|\leq\|D_a\|_{\rm op}\), and
\(|m_{ab}|\leq|\widehat c_b|\|\widehat\delta_b\|\|\widehat\delta_a\|/n\).
These prove (37) on the full deterministic ranges. Only the response trace can grow subpolynomially. That growth suffices for the errors here but does not establish a width-uniform trace or an uncut theorem.

## Adversarial failure modes specifically tested

| Potential failure | Why it does not invalidate this proof |
|---|---|
| A hidden factor \(n,d,\sqrt n\), or \(2\) in the raw gradient | Direct raw differentiation and the metric calculation give exactly (4), (6), and (19). |
| Independence lost by stopping or by including the root initialization | The cavity stop is \(\mathcal F_{-j}\)-measurable; \(\xi\) is independent of \(g\). The actual stop is imposed after the finite Gaussian event. |
| Treating adaptive \(h\) as Gaussian-independent | Only individual cavity kernels are tested; bounded absolute time weights handle every feature history pathwise. |
| Wrong source index or commutation of Jacobians | The first two recurrence steps and the fractional endpoint identity give \(U(k,r+1)\), with the stated order. |
| A missing initial forcing because bulk states agree at zero | The physical upper mismatch is nonzero, and the step-zero source, including residual variation, is retained. |
| A large Euclidean perturbation invalidating Taylor expansion | The linear physical coordinates are small in maximum norm; matrix cross products carry \(1/\sqrt n\). The upper nonlinear remainder is handled separately. |
| A missing trained outer-product or residual cross term | The exact six first-layer terms, six matrix terms, and three readout terms were expanded and bounded above. |
| Stability requiring an unproved secant maximum | Identity (55) places the gate-difference multiplier on actual old-node \(q\). |
| Stopping-endpoint overshoot invalidating iteration | Only old nodes need the actual bound; the stopping node is reached from \(s-1\). |
| Replacing recomputed hidden fields by affine interpolation | Affinity is used only for \(X\) and \(Y\); moving-cavity Taylor expansions and operator moduli handle all hidden queries. |
| Losing one factor of the learned memory or changing source time | Both backward factors and residuals are replaced explicitly; source residuals/features remain at their old nodes. |
| Uniform-in-time concentration requiring infinitely many tests | Operator continuity and \(\|g\|\leq2\) extend the finite event to every cell. |
| Silently claiming a Gaussian law under survival | The Gaussian statement is explicitly for the original conditional measure. |
| Inferring uncut or limiting conclusions | The theorem and final scope statements leave these open. |

## Required corrections versus optional suggestions

### Required corrections

**None for the stated stopped theorem and explicitly defined algorithm.** The calculations support the finite-width conditional node theorem, the whole-cell theorem for recomputed hidden fields, and the vanishing error in the actual first-root equation.

### Optional suggestions

1. **State the raw block learning rates next to (4).** They are \(\eta n/d,\eta,\eta n\) for \(\sum_a(f_a-y_a)^2\), equivalently step \(\eta\) in (17). This prevents “raw GD” from being mistaken for a common raw-coordinate learning rate. If that different algorithm were intended, the theorem would need reformulation; it is not the algorithm currently defined.
2. **Make the terminal response convention explicit.** After defining the affine response in Section 9, write \(Y^{\rm lin}(N\eta)=Y_N^{\rm lin}\). Ordinary affine interpolation already supplies this convention, but the two-endpoint formula should not be read literally with an undefined \(Y_{N+1}\).
3. **Clarify the two ranges in (20).** The actual identity holds for every \(k<N\); the cavity identity holds for \(k<s_c\). The current placement is harmless because comparison uses \(k<s\), but separate qualifications would be clearer.
4. **Retain a compact error-power ledger.** The powers \(20,30,35,40\) have enough margin. Explicitly listing the intermediate costs would make the bookkeeping easier to verify.

These are presentation improvements, not substitute assumptions or missing proof steps. No source changes were made.

## Final assessment

Adaptive root features, the \(g\)-dependent actual stop, noncommuting Jacobians, the initial mismatch, trained-column feedback, coordinate-sensitive nonlinear defects, and whole-cell recomputation are all accounted for within the stopped scope. The proof needs neither Gaussianity after survival conditioning, a bound on a secant Hessian, affine interpolation of hidden fields, nor comparison to gradient flow. The stopped approximation passes this isolated audit.
