# P1 independent scientific review A

**Overall verdict: ACCEPT for the exact proposed C.4.6 scope and its proposed guide/navigation statements.**

I found no surviving mathematical gap requiring correction. The conclusion is the actual finite-GF right data derivative limit on each separately fixed physical horizon, together with a separate bound uniform in time for the population homogeneous propagator. It is not a nonlinear perturbed-law flow theorem. The proofs supply the otherwise necessary weighted finite-source estimates and the finite-tangent/mesh comparison; acceptance does not rest on formal differentiation or numerical checks alone.

## 1. Fresh reviewer identity, isolation, and authority

- Actual runtime `CODEX_THREAD_ID`: **01a090ca-1bf7-70b1-be49-7ac58e2e0f6d**.
- Fresh audit-run identifier: **P1-A-fresh-14144a1c-1759-4cc9-9cd7-8d85a02ac9db**, generated at `2026-09-11T14:06:21.723174+00:00`.
- `/root` is a reusable orchestration role label, not a process identity. This review's runtime identity differs from the manifest's author/original-task identity `01a090b5-1a52-7072-a829-cd2aad518558` and selector identity `01a090c0-8a58-7da1-8075-8c0b0f23f959`. The manifest's child role labels do not identify this reviewer either. The short-lived shell PID recorded when generating the audit identifier is not offered as the LLM/thread identity.
- I performed this fresh review independently. I read only the neutral assignment, the six other allowed packet files, and the required skills and applicable references listed below. I read the two complete guides as frozen inside the packet, not from live project files. I did not read the study README, author history, earlier rounds, reviewer reports, other project files, or external scientific sources. No author startup, Git command, delegation, or contact with another task occurred.
- The only non-scientific runtime metadata inspected for identity was `CODEX_THREAD_ID`; no other environment-variable inventory was read. Package imports and runtime versions were used to execute the authorized checks.
- I wrote only this assigned report and files under `/home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_a`. I did not edit any input. This scientific verdict is not authorization to modify established files.

The governing assignment is `P1_ASSIGNMENT.md`. I applied the complete `solve-math-rigorously` and `investigate-conjectures` skills, including `research-contract.md`, `adversarial-audit.md`, and, because deterministic computation was explicitly authorized, `decisive-experiments.md`. No experimental search or training was conducted.

## 2. Frozen inputs, hashes, and complete reading coverage

The six manifest-listed scientific/assignment inputs matched both their declared SHA-256 hashes and line counts before review. The manifest itself was also hashed. All seven files were checked again after the substantive audit; none changed. The manifest's build/integration entries were treated only as provenance and were not opened.

| Allowed input | Lines | SHA-256 before and after (identical) |
|---|---:|---|
| `P1_ASSIGNMENT.md` | 47 | `a9f61d5f27d84e8a9de85d7ba5faaf39c4adb19e7829c27c285a455916488199` |
| `P1_MANIFEST.json` | 83 | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |
| `P1_SECTION.md` | 2062 | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| `P1_ANCILLARY.md` | 300 | `649f0ee17af3c0a2f4b995e971929f8e7a62d9d420614baee418af62d6cdd420` |
| `P1_DEPENDENCIES.md` | 3238 | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `P1_CHECK_IDENTITIES.py` | 197 | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P1_REFERENCE_CERTIFICATE.py` | 56 | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |

Completed reading ranges, inclusive:

| Input | Complete ranges read |
|---|---|
| Assignment | 1–47 |
| Manifest | 1–83 |
| Proposed section | 1–360; 361–700; 701–1080; 1081–1480; 1481–1840; 1841–2062 |
| Ancillary | 1–180; 181–300 |
| Dependencies | 1–300; 301–650; 651–950; 951–1260; 1261–1660; 1661–2010; 2011–2370; 2371–2740; 2741–3040; 3041–3238 |
| Identity checker | 1–197 |
| Reference certificate | 1–56 |

The first combined tool response exceeded its outer output budget. Its section range 1–360 appeared complete; the ancillary and dependency portions could not be credited as complete. I repaired the read by rereading ancillary 1–180 and 181–300 and dependencies 1–300 with adequate budgets and line numbers. All subsequent chunks were complete. The ranges above have been mechanically checked for contiguity and exact final line coverage. No scientific line remains unread.

Dependency coverage included the original complete guide, notation, finite dynamics §§1–4, all supplied III.F.1–11 proofs, global nonlinear A.1–A.4 and B.1, C.4.1, the supplied C.4.2 construction, and complete C.4.5.1–2, including the embedded certificate. The revised complete guide and exact navigation replacement were read in the ancillary packet. Background chapter descriptions in the guides were read for consistency and scope; their unrelated mathematical content is not a new claim under review.

| Required skill/reference (read completely) | Lines | SHA-256 |
|---|---:|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 115 | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | 185 | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/research-contract.md` | 99 | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | 121 | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `/etc/codex/skills/investigate-conjectures/references/decisive-experiments.md` | 141 | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |

Machine-readable records are retained as `hashes_before.json`, `hashes_after.json`, `skill_hashes.json`, `reviewer_identity.json`, and `read_coverage.json` in the assigned scratch directory.

## 3. Reconstructed mathematical contract

The network has two tanh hidden layers, width (n), normalized input (u=x/\sqrt2\in S^1), no biases, and prediction (c^T\tanh(A\tanh(wu))/n). Stored initial variances are (1,1/n,1/n^2), independently across entries and blocks. The last is the **stored** readout variance. The unhalved mean square and mobilities ((n,1,n)) give the raw increment norm

\[
\|\Delta w\|_F^2/n+\|\Delta A\|_F^2+\|\Delta c\|_2^2/n.
\]

The reference law is the equal-weight pair ((e_1,+1),(e_2,-1)) in normalized coordinates. A fixed deterministic Borel probability law \(\nu\) may be nonatomic and have arbitrary correlations and support within the bounded-label circle. The direction is \(\sigma=\nu-\nu_*\). All perturbed finite flows use the same actual initialized arrays. Right differentiation at each finite width precedes every width limit.

The population reference is the canonical autonomous reference of the supplied dependencies. Its initial action (A_0) is bounded, has its actual adjoint, and is not assumed Hilbert–Schmidt. The learned increment and the tangent middle block are Hilbert–Schmidt. The first-row clock satisfies

\[
F(j(X,g))=F(g)+X,\quad F'=\cosh^2,\quad j_X=\operatorname{sech}^2j.
\]

Thus \(\delta w_a=D_a\xi_a\), with \(D_a=\phi'(w_a)>0\). The state norm for the response is clock (L^2\oplus\mathrm{HS}\oplus L^2), stronger than the pulled-back raw norm. No bounded inverse of the clock conversion is available or needed.

The claimed observable is the finite derivative predictor, uniformly over each compact time interval and the whole circle, converging in probability over initialization. State identification uses same-width finite-program approximations, canonical Hilbert convergence, finite same-layer joint (W_2) laws, rank contractions, and both action directions. It does not posit an operator-norm distance between different carriers.

The approximation order is: finite right derivative; fixed source truncation, fixed data quadrature, fixed auxiliary time mesh; width limit for that finite program; removal of auxiliary approximations by the proved uniform estimates. Constants may depend on the fixed horizon, label bound, and fixed reference. Deterministic bounds do not depend on the number, weights, or Gram rank of the perturbing law's atoms. Convergence is for each fixed law, without a law-uniform failure-probability assertion.

## 4. Component verdicts

| Component | Verdict | Proof locations principally checked |
|---|---|---|
| Model, metric, rank normalization, both action orientations | PASS | Section 18–119; dependencies 408–613, 947–1002 |
| Canonical Gaussian action, singular finite programs, value/response extensions | PASS | Dependencies 620–1189, 1191–1209, 2034–2109 |
| Reference feature flow, physical clock, fitting and actual endpoint | PASS | Dependencies 2116–2422 |
| Active endpoint fourth moment and coefficient provenance | PASS | Dependencies 2745–3234; section 271–309 |
| Finite right differentiation and actual stored readout | PASS | Section 1529–1588 |
| Column-deleted flow comparison and conditional Gaussian query maximum | PASS | Section 838–1167 |
| Weighted finite uniform integrability | PASS | Section 1169–1233 |
| Canonical uniform population weighted source and Borel forcing | PASS | Section 1235–1518 |
| Strong generator, metric identity, singular endpoint compatibility | PASS | Section 315–504 |
| Integrable perturbation and uniform population propagator | PASS | Section 506–664 |
| Fixed-program tangent identification and time-mesh removal | PASS | Section 1590–1917 |
| Actual prediction derivative on the whole circle | PASS | Section 1919–2016 |
| New ancillary scientific statements and exclusions | PASS | Ancillary 159, 267–272, 294–300; section 2018–2062 |

The following details record the actual tests of the necessary proof bridges, rather than replacing them with the table.

## 5. Algebra, finite differentiation, and the reference dependencies

### 5.1 Normalization and exact differential

Differentiating the predictor in raw coordinates gives first, middle and readout gradients proportional to (\phi'(w\cdot u)Q(u)u/n), (\delta(u)H^1(u)^T/n), and (H^2(u)/n). Multiplication by the stated mobilities cancels the first and last factors (n) but not the middle factor. This yields exactly the three blocks of (-2\int r\,q_{\mathrm{raw}}\,d\mu). The population rank (\delta\otimes H^1) has finite representative (\delta H^{1T}/n); its ordinary Frobenius norm equals the product of the two finite RMS norms. The HS metric is therefore the correct middle metric, without an extra factor (n).

At the reference, row (a) is trained only by (e_a). Dividing its raw velocity by (D_a) cancels the first gate *identically*: (X'_a=-r_aQ_a). Its homogeneous differential is (-\ell_a[v]Q_a-r_aq_a[v]). Equivalently, differentiating \(\delta w_a=D_a\xi_a\) in time produces (\dot D_a\xi_a); this cancels the raw gate-curvature term. This explains the absence of a multiplication by (Q_a\) on an arbitrary row tangent in the transformed generator. The off-support law derivative does not enjoy that cancellation and correctly retains the ratio (\phi'(w\cdot u)/\phi'(w_a)).

The variation chain in T14 has the correct types and includes both (BH^1+A\delta H^1) and (B^*\delta+A^*\delta\delta). Applying the finite product rule to the three raw velocities gives the synthesis/evaluation term, residual-curvature term, and signed source with precisely the stated loss factor two and reference subtraction.

For each finite (n), bounded labels and compact parameter sets justify differentiating the integrated loss even for a nonatomic law. The raw energy identity supplies a common finite-dimensional parameter ball for the probability segment. On this ball the smooth vector field and its derivative are bounded. Subtracting integral equations first yields an (O(\epsilon)) trajectory difference. The integral mean-value formula then gives uniform convergence of the difference quotients to the linear variational equation. This is a valid finite right-derivative proof; no width-independent differentiability estimate is silently required here.

### 5.2 Canonical action and finite-program inputs

The contained Gaussian conditioning formula is the minimum-Frobenius-norm solution to the forward and reverse constraints plus the Gaussian projection onto their common homogeneous subspace. Its adaptive conditioning proof fixes queries only after conditioning on the preceding transcript. Conditional independence of the remaining matrix factors is preserved instruction by instruction. This avoids treating an adapted query as initially independent of its matrix.

The finite-rank projection of fresh Gaussian noise has normalized squared mean rank/n. Under positive limiting query Grams this gives the stated fixed-program (W_2) induction. The singular-query proof adds a distinct fresh root to each query, proves the fixed positive-noise limit, controls same-array errors uniformly in width, and then removes noise. Covariance square roots, rather than empirical pseudoinverses, are used in the final continuity argument. The source corrections preserve forward/reverse dependence even though their oriented Gaussian source groups are independent.

Generated cylinder functions and their smooth approximations are dense in each stated (L^2) space. Passing the finite norm inequality and transpose pairing on their span constructs bounded canonical actions with actual adjoints. The sharp constant two used later has its own contained comparison and Gaussian Poincare proof in A.3. It is not inferred from the cruder sphere-net constant ten.

A.1 supplies continuous at-most-linear *value* instructions by ordered smooth approximation and (W_2) tails. A.2 separately treats expected source derivatives for fixed neural product programs. For the tanh clock, C.4.5.2 additionally clips the frozen root: (J_g=\phi'(J)/\phi'(g)) is bounded after clipping, while the source derivative (H_X=\operatorname{sech}^4J) remains bounded uniformly in the clipping threshold. Its chronological source-limit proof is supplied. I did not substitute an unproved derivative theorem for A.1's value conclusion.

### 5.3 Fitted reference and its active moment

The feature equation is (c_s=h,(w,K)_s=J^*c), so the strong curve chain rule gives (c_{ss}=JJ^*c), and

\[
b_s=\|h\|_2^2+\|J^*c\|^2=\|\theta_s\|_{\mathrm{raw}}^2.
\]

On the first interval with (g=\|c\|>0), (g_{ss}\ge0) by Cauchy–Schwarz and (g_s(0+)=\sqrt m). Thus (g_s\ge\sqrt m), the interval cannot end by returning to zero, and (b_s\ge m\ge1/10). This proves a unique first (b=1) feature time at most ten. The physical clock (ds/dt=2(1-b)) stays positive and takes infinite physical time to approach that endpoint because (b_s) is bounded on the compact feature segment. It gives (e(t)\le e^{-t/5}).

Integrating the feature energy identity and using Cauchy–Schwarz gives the actual raw endpoint estimate (d_{\mathrm{ref}}\le e/\sqrt m\le\sqrt{10}\,e). The reference supremum bound on (c), action bound (2+\sqrt{10}), and readout (L^2) bound \(\sqrt{10}\) all follow within the packet.

I also checked the supplied active-response proof. A pulse in a complete reverse answer changes only the immediate clock update by (h_j\sigma_b\epsilon e/2); a pulse in a complete forward answer has the additional upper backward and readout effects included in (P=161/2). The displayed stability coefficients sum to at most (8+56s), so the integrated amplification is (e^{2880}). At fixed mesh and nonzero pulse, finite value convergence and Gaussian integration by parts give the source coefficient bounds; only afterwards is the pulse removed. The continuity of the source derivatives at zero variance is explicitly proved. Summing old, learned, and current reverse coefficients gives (2SPKE+SC^2+2S=225400e^{2880}+180). Passing the coupled Gaussian sources and bounded remainders to the canonical feature endpoint gives a genuine (L^4) bound for the active (Q_{a,\infty}). No empirical fourth moment is inferred from (W_2) convergence.

The rational certificate's exponential remainder, alternating arctangent bounds, density bounds, monotonicity choices and outward rounding have the required signs. The code was run in full. Its certified (q>.39,q<.4,v>.2) give (m=v/2>.1); the other supplied margins were checked as well. The early hidden-motion proof in the dependency was also read and checked, but it is not used to infer a risk benefit of the derivative theorem.

## 6. The weighted-source proof and its principal attacks

### 6.1 Why the cavity argument is valid

The obstacle is that (Q=A^*\delta) is adapted to (A_0). A bounded matrix operator norm alone controls RMS but not the coordinate moments needed after multiplication by the inverse gate. The proof instead deletes only initialized column (a_i), trains the entire resulting cavity system with its own residuals, and conditions on the remaining initialization.

The event (E_n^i) involves the column-deleted initial matrix, roots and readout, and is independent of (a_i). The full event (E_n\subset E_n^i) is used only to apply the deterministic comparison. Conditional Gaussian estimates are made on (E_n^i), never by conditioning the column's law on (E_n). This is the correct direction of event inclusion and conditioning.

The direct forward perturbation is (a_i\widetilde H_i), whose RMS is at most (\|a_i\|/\sqrt n). The direct reverse perturbation is (e_i a_i^T\widetilde\delta). In S21 the remaining backward error is multiplied by the full (A^T), which avoids an additional uncontrolled column-dependent reverse term. The estimates for (V,D,P,R_{\mathrm{cav}}) include residual differences and give the displayed Gronwall inequality in the sum of clock RMS, middle Frobenius, and readout RMS distances. In particular the cavity is not driven by the full system's residuals.

The learned transpose term is controlled coordinatewise by its exact rank integral, with bound (4TC^2). Combining it with the comparison yields

\[
\sup_{t,u}|Q_{n,i}(t,u)|\le A_T Z_i^\#+B_T \quad\hbox{on }E_n.
\]

I checked the constants here: (4D_0^2\|a_i\|[J_T(\|a_i\|+2Z_i^\#)+\|a_i\|]), with \(\|a_i\|\le10\), is bounded by the stated (80D_0^2J_T Z_i^\#+400D_0^2(J_T+1)). The learned term gives the remaining (4TC^2).

### 6.2 Gaussian query process and weighted finite tails

Conditionally, (Z_i(t,u)=a_i^T\widetilde\delta(t,u)) is a centered Gaussian process whose covariance is the normalized cavity pairing. Its parameter metric is Lipschitz because the cavity's backward field is Lipschitz in normalized (L^2), using only a first-row RMS bound and the pointwise bounded readout. A time/circle parametrization fits a two-dimensional square. The contained grid-parent telescoping proof, finite Gaussian maximum estimate and summable (2^{-k}\sqrt k) increments give the claimed (C\sqrt p) moment bound for the supremum. It uses no Gaussian bound for input derivatives.

The resulting estimate is a genuine coordinate expectation bound, uniform in (i,n) on (E_n). Averaging therefore proves S4 without relying on exchangeability to replace a missing bound. Integrating (X'_a=-r_aQ_a) gives (X^\#_a\le3TN_i). The exact identity

\[
\partial_X\cosh^2j(X,g)=2\tanh j(X,g)
\]

gives (\cosh^2w_a\le\cosh^2g_a+2|X_a|) for either sign of (X_a). Gaussian root exponential moments and Hölder control products of this weight with (N_i), with no independence between them. A moment strictly above two then makes empirical squared tails vanish in probability by Markov's inequality. The high-probability complement of (E_n) is removed only after taking the width limsup. These steps establish S39 for the actual finite physical GF, including its random readout.

### 6.3 Uniform population source and canonical identification

The auxiliary zero-readout finite **feature** equation on (0\le s\le10) is used solely to obtain bounds for the already identified population feature path. Its explicit polynomial state bounds permit the same cavity argument, with fixed feature controls and no residual-difference terms. This use does not reset the actual finite physical readout.

At each fixed mesh the feature program and appended passive queries are legitimate value programs, with bounded readout clipping inactive. Same-root stability gives width-independent mesh errors in clock/HS/readout norm. The order width first, mesh removal second identifies the canonical query tuples. Testing finite rational lists with bounded maxima, then removing the truncation and increasing the list, constructs the population (N^\#\) envelope. For every other deterministic query parameter, (L^2) continuity supplies an almost surely convergent subsequence from that list. Thus the envelope bounds its equivalence class. Fubini provides exactly the almost-everywhere assertion needed for integration against each fixed Borel law. No simultaneous continuous pointwise realization on an uncountable input set is presumed.

Active-clock integration gives (\sup_s|X_a|\le SN^\#/2). Hölder consequently yields

\[
\|\cosh^2w_a Q(s,u)\|_2
\le2^{5/4}e^8C_*+4SC_*^2.
\]

The sum of the two squared coordinate norms gives the stated \(\sqrt2\) factor in S45. For T9 the sharper (M_w=\sup_{t,u,a}\|\cosh^2w_aQ(t,u)\|_2) combines with \(\sum_a u_a^2=1\); there is no unnecessary factor \(\sqrt2\) in that row bound. The other squared block bounds are ten and one, producing (2(Y+\sqrt{10})\sqrt{M_w^2+11}\).

For continuity, the interpolation (\|V\|_4\le\|V\|_2^{1/3}\|V\|_8^{2/3}) is correctly used on query differences. The remaining changing factors are controlled by the root/query envelope and the clock-weight identity. This gives a continuous Hilbert-valued source on the compact feature/data parameter set and hence a Bochner integral against every finite signed Borel measure. The linear extension to zero-mass signed measures is not justified by a nonexistent two-sided probability neighborhood; it is defined directly by that integral.

For nonatomic laws, transferring exact cell masses to representatives is a proof approximation. Minkowski and the source modulus, or the separately clipped Lipschitz proof in F14–F15, make its error small independently of atom count or minimum mass. Neither proof claims TV convergence of these quadrature measures. Middle forcing is a finite sum of ranks at fixed quadrature, with its HS norm identified by both layer Gram contractions. Source/action extensions remove their clips using the just-proved weighted tails and bounded actions, not a false general (L^p\to L^p) action theorem.

## 7. Strong evolution, singular endpoint, and integrable perturbation

The maps in P8 are bounded on every tangent vector because all activation gates are bounded, (c\) is bounded pointwise, and (A\) is bounded. The synthesis columns are actual (L^2/\mathrm{HS}/L^2) fields. Their norm bound and the evaluation bound are

\[
\|S\|,\|E\|\le L_0=\sqrt{1+10(1+(2+\sqrt{10})^2)}<17.
\]

Strong continuity is proved on each fixed vector by bounded-multiplier convergence and truncation of that vector. The argument does not claim operator-norm convergence of arbitrary multiplication operators, or Fréchet differentiability of an (L^2)-valued nonlinear field.

With (R\) the raw conversion and (D=R^*R), exact adjunction gives (E=S^*D) and \(\Gamma=S^*DS\). Because every (w_a\) is finite almost surely and tanh's gate is strictly positive, (D\) is injective. It need not have a positive lower bound. Nevertheless

\[
\alpha^T\Gamma\alpha=\|RS\alpha\|^2
\]

vanishes exactly when (S\alpha=0). Also (E^*=DS), so

\[
\ker\Gamma=\ker S=\ker E^*,\qquad\operatorname{ran}E=\operatorname{ran}\Gamma.
\]

The last equality uses the finite-dimensional target of (E); no closed-range theorem for an infinite-dimensional Gram is needed. This supplies the essential zero-mode compatibility. Positivity of (ES) alone would not suffice, as the retained nilpotent example demonstrates.

The power identity ((SE)^j=S\Gamma^{j-1}E), combined with range compatibility, proves the pseudoinverse semigroup formula at zero eigenvalues as well as positive eigenvalues. If \(\Gamma=0\), then (S=0) and the formula is the identity. For the fixed finite endpoint Gram, its pseudoinverse has finite norm regardless of rank. Consequently the frozen semigroup is bounded by (B_\infty); no trajectory-wise pseudoinverse continuity or gap assumption is needed.

The remaining issue is the actual nonautonomous generator. Factor subtraction gives the (O(d_{\mathrm{ref}})) differences of the synthesis fields. The evaluation's extra field is (D_a^2Q_a). For (b=\phi'(w_a)^2-\phi'(w_{a,\infty})^2), \(|b|\le\min(1,4|w_a-w_{a,\infty}|)\) implies

\[
\|bQ_{a,\infty}\|_2
\le\|b\|_4\|Q_{a,\infty}\|_4
\le2M_4\|w_a-w_{a,\infty}\|_2^{1/2}.
\]

This is the specific use of the supplied endpoint fourth moment. It does not multiply two unrestricted tangent fields. Therefore the finite-rank evaluation difference is (O(d_{\mathrm{ref}})+O(d_{\mathrm{ref}}^{1/2})). Residual curvature is (O(e(t))). With \(d_{\mathrm{ref}}\le\sqrt{10}e\) and \(e\le e^{-t/5}\), both terms are integrable in operator norm. The coefficients in P21 integrate with factors five and ten, giving exactly P22's (J_0).

For bounded strongly continuous coefficients, the vector-valued successive integral series has the summable bound (L^j(t-s)^j/j!). This constructs the strong evolution and proves uniqueness. Applying variation of constants around the compatible frozen semigroup gives

\[
\|U(t,s)\|\le B_\infty\exp\!\left(B_\infty\int_s^t\|\mathcal B(q)\|\,dq\right)
\le B_\infty e^{B_\infty J_0}.
\]

The argument controls the actual trained generator, including possible transient amplification. For (L^1_{\mathrm{loc}}) forcing the vector integral is strongly absolutely continuous and solves the equation almost everywhere; the continuous data forcing gives a strongly (C^1) solution. The TV bound then gives response growth at most linear in the horizon. This is not a uniform-in-time bound on a persistently forced response.

The endpoint projector identities and their raw conversion follow from the same compatibility. (G\Gamma^+G^*), with (G=R_\infty S_\infty), is the raw orthogonal projection onto the gradient span. The clock projector is generally oblique. The proof neither asserts that the nonautonomous propagator converges to this projector nor infers a sign or benefit for unseen evaluations.

## 8. Actual finite-tangent capture and whole-circle observations

### 8.1 The width/mesh bridge

The theorem cannot follow simply by appending formal tangent nodes to a fixed-program theorem: the number of mesh instructions diverges when the mesh is removed. The supplied proof addresses this distinction.

For fixed source clip (R), quadrature and time mesh, expand all learned reference and tangent matrices as finite sums of ranks. All new unbounded tangent coordinate factors are multiplied by bounded gates or the clipped readout. Thus each coordinate instruction is continuous with at most linear growth; causal scalar contractions are treated through their deterministic oracle. A.1 and the finite-program theorem identify each fixed program, including both orientations and quadratic contractions. The actual finite initial readout discrepancy tends to zero both in RMS and supremum, and a finite same-array induction propagates it. The actual GF and its derivative are never reinitialized with zero readout.

The finite reference Euler error is (O_T(h)) uniformly in width on (E_n). The HS strengthening is justified by the rank difference inequality, not by upgrading operator convergence without proof. On the population carrier, bounded generator norms and strong multiplier consistency on each fixed vector extend uniformly to compact vector families by a finite net. Applying this to the compact response path gives convergence of the population tangent Euler paths.

For the actual finite tangent, F20 displays the defect against its same-width mesh proxy. The mesh increment and clipped-source errors are (O(h)) in integrated state norm. Each coefficient error in its first line is either controlled by action/HS subtraction or is a bounded multiplier difference acting on a mesh testing node. The complete list includes row tangent, upper backward tangent, changed readout times upper preactivation variation, reverse actions, rank factors, and the representing (Q_a) field.

F16 splits such a product at a fixed testing-node magnitude (M). The bounded part is at most (\operatorname{Lip}(b)M\) times the (O(h)) reference discrepancy. The unbounded part is a mesh-node square tail. The population testing nodes over a countable refining mesh sequence form a relatively compact (L^2) family, because the population mesh tangents and reference fields converge strongly with bounded actions. Their tails vanish uniformly. At each separately fixed mesh, finite empirical cutoff moments converge by the fixed-program (W_2) theorem. Width first, then mesh refinement at fixed (M), then (M\to\infty), makes the integrated defect vanish. A finite linear Gronwall inequality transfers this to uniform-in-time same-width tangent error. Finally F14–F15 remove the source and law approximations.

This is a complete bridge from the fixed-program result to the actual finite derivatives. It supplies small error production as well as bounded error propagation. It does not assume higher moments of arbitrary finite tangent fields, uniform control for growing Gaussian transcripts, or operator-norm convergence of varying gate multipliers.

Rank expansions identify middle Frobenius norms and pairings from two-layer Gram products; the same-width approximation transfers them to actual tangents. Applying the same compact-tail multiplier argument to a finite list of observations identifies the stated joint (W_2) laws. The topology is accurately limited: no individual-neuron coupling across widths or hidden tangent path law in coordinate supremum norm is asserted.

### 8.2 Passive evaluation and circle/time modulus

The response predictor's Riesz field in clock coordinates is

\[
\ell_u=((u_aD_a\phi'(w\cdot u)Q(u))_a,\;\delta(u)\otimes H^1(u),\;H^2(u)).
\]

This contains (D_a\), whereas the direct data forcing contains (D_a^{-1}\); interchanging these would invalidate the proof. Its norm is uniformly bounded by the stated reference constants. Fixed-point scalar convergence therefore follows from the identified same-layer moments and rank contractions.

For time regularity, reference (Q) is (L^2)-Lipschitz using the actual raw velocities and bounded (c). Changed gates multiplying (Q) are treated by its *reference* tails. The tangent velocity is bounded in probability by the bounded finite generator and the source estimate. These facts provide the requisite scalar time equicontinuity without a tangent higher-moment premise.

For the circle parameter \(\alpha\), the strong curve rule gives (\partial_\alpha H^1=\phi'(w\cdot u)(w\cdot u')), then \(\partial_\alpha Z^2=A\partial_\alpha H^1\), and finally \(\partial_\alpha Q=A^*[c\phi''(Z^2)\partial_\alpha Z^2]\). These derivative norms use only (L^2) bounds and the pointwise bounded readout. Differentiating the first Riesz block adds the particular product (\phi''(w\cdot u)(w\cdot u')Q(u)\). The proved \(|w|Q\) envelope makes it (L^2). Strong differentiation is justified by the displayed difference-quotient dominator and coordinate absolute continuity; this is not a purely formal product rule.

Thus the Riesz fields have a bounded (H^1) circle norm in the population and a tight such norm uniformly in finite time. The Hilbert-valued fundamental theorem and Cauchy–Schwarz give a half-Hölder circle modulus. Multiplying by the tight uniform tangent norm gives the scalar derivative modulus. A fixed finite product of time and circle nets, followed by a finite union bound and then refinement of those nets, proves the claimed compact-time whole-circle convergence. It does not interchange width with an infinite physical horizon.

## 9. Retained commands and numerical/algebraic outcomes

All check programs were inspected completely before execution. Both supplied programs were executed without modification. The working directory for the runs was the assigned scratch directory. Exact command arrays, timestamps, return codes, full stdout and stderr are retained in `supplied_identities.json`, `supplied_certificate.json`, and `independent_run.json`, with separate text logs. The supplied identity program also produced `identities/results.json` in a freshly created subdirectory.

```text
/usr/bin/python /home/amir/Codes/PDE/studies/trained_data_response/P1_CHECK_IDENTITIES.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_a/identities
/usr/bin/python /home/amir/Codes/PDE/studies/trained_data_response/P1_REFERENCE_CERTIFICATE.py
/usr/bin/python /home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_a/independent_checks.py
```

All three runs exited **0**, with empty stderr. Runtime: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. No failed check or excluded run was suppressed. `check_plan.md` and `independent_check_plan.md` were written before their corresponding executions. The independent script's SHA-256 is `a023507a9ac4594cf2e245f9f90e27a4f214e71c8b3eefde954363deec550526`.

Supplied identity results:

- Tangent central-difference errors: `1.0292819331017236e-06`, `2.573205074969171e-07`, `6.433012185025226e-08`, `1.608263607613758e-08`. Each refinement has the expected second-order reduction.
- Raw loss/metric error: `7.900680110140001e-12`.
- Singular-semigroup errors at the supplied times: `0`, `2.5723099259051144e-16`, `6.175621784463053e-16`, `3.9466663458119664e-15`, `1.5265444420160054e-14`.
- The deliberately incompatible nilpotent factorization grows as expected.

The complete exact rational certificate returned:

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

These are outward bounds with the printed decimals only a readable summary; the assertions themselves use rational arithmetic.

### Independent attacks and checks

1. **Raw variational equation versus transformed tangent.** At one fixed two-neuron nonsymmetric state with nonzero stored readout, complex-step differentiation of the raw field and conversion using the time derivative of (D) agreed with the separately assembled clock tangent to `2.220446049250313e-16`. Deliberately omitting the clock time-correction produced error `0.06550122766632116`, exceeding the preregistered detection threshold. This checks the nontrivial cancellation rather than only the final displayed formula.
2. **Passive output and full angular Riesz derivative.** At the fixed angle 0.73, prediction variation error was `2.7755575615628914e-17`; the full angular Riesz-field error was `1.1102230246251565e-16`. Both forward and transpose actions are present.
3. **Actual readout and signed-source boundaries.** With zero readout, hidden and middle source blocks vanished exactly while the readout source norm was `1.9265993138038193`. At the fixed nonzero readout the hidden and middle source norms were `1.0717283614264799` and `0.5532127917755968`. This demonstrates why resetting the actual finite readout changes the finite source. Identical law gave zero source, and splitting an atom left the source unchanged to exact floating-point equality.
4. **Singular Gram with an injective noncoercive metric.** On (L^2([0,1])), take (Dv(x)=xv(x)) and (S(\alpha)(x)=\alpha_1+2\alpha_2). Then (E v=(m,2m)), (m=\int_0^1xv(x)dx), and \(\Gamma=\tfrac12\begin{pmatrix}1&2\\2&4\end{pmatrix}\) is singular with kernel ((-2,1)). (D) is injective, but unit vectors supported on ([0,1/k]) have \(\|Dv\|\le1/k\). The projector is (Pv=v-2m\), and the exact semigroup is (P+e^{-5t}(I-P)). Exact Fraction computations on the invariant polynomial span ((1,x)) verified idempotence and the kernel relations; the exponential check at (t=.7) had error `1.3183898417423734e-16`. The general proof is the algebra above; this example shows that no positive lower metric bound is being smuggled in. For (S=(1,0)^T,E=(0,1)), by contrast, (ES=0) and (e^{-2tSE}=I-2tSE), which is unbounded.
5. **Clock envelope at both signs and a saturated root.** The predetermined cases ((g,X)=(0,0),(2,-.4),(-1,.7),(20,0)) verified the exact derivative identity and nonnegative envelope slack. The largest identity error was `2.220446049250313e-16`. The general envelope follows by integrating \(|\partial_X\cosh^2j|\le2\), not by these point checks.
6. **Independent reference integrals.** Adaptive scalar quadrature over ([0,8]) gave (q=0.3942944903978399), (v=0.2364504104992942), (a_0=0.3415092073166634), (r_0=0.6365445624738778). Reported quadrature errors were at most `1.203158415089242e-12`; the elementary omitted two-sided Gaussian tail is at most `1.2630677708842232e-15`. The scaled integrals use numerical (q), as recorded in the results, and are supplementary. The rational program supplies the rigorous margins. The independent value of (L_0) is `16.65806430551687`.

Full independent configuration, code, and numerical outputs are retained as `independent_check_plan.md`, `independent_checks.py`, `independent_results.json`, `independent_checks.stdout.txt`, and `independent_checks.stderr.txt`. These fixed deterministic checks are not a training experiment or parameter sweep, and no numerical pass is presented as a proof of a width or long-time limit.

## 10. Surviving gaps, required corrections, and optional suggestions

**Surviving gaps in the proposed scope: none identified. Required corrections: none.**

The decisive potential obstructions were adapted-column conditioning, inverse-gate weights, passage of weighted moments to the canonical reference, nonnormal growth at a singular endpoint, lack of operator-norm multiplier continuity, lack of uniform finite tangent higher moments, and exchange of width with mesh refinement. Each has a specific supplied argument checked above. The independent bad factorization shows that the endpoint compatibility assumption is substantive; the actual metric identity supplies it here. The readout boundary check shows that actual finite initialization matters; the proof retains it.

The following remain outside the theorem and must not be inferred from acceptance: nonlinear population flows for changed laws; a finite-contamination remainder; uniform-time finite-width convergence; a law-uniform failure probability; continuity of trained endpoints in the law; a risk improvement from the response; a raw-GD derivative; a sampling CLT; a transport forcing theorem; and convergence of a training-time Taylor expansion. In particular, homogeneous bounded propagation plus a bounded persistent source yields only the displayed horizon-linear estimate. The packet states these limits explicitly.

The new guide row, scope paragraph and navigation replacement accurately describe the theorem: each fixed horizon and whole-circle finite-GF derivative capture, separate uniform population homogeneous propagation, and TV forcing control. They do not extend the older special-reference risk statement to the derivative or to arbitrary perturbed population dynamics. No correction to those additions is required.

Optional presentation suggestions, not acceptance conditions:

- In the brief guide/navigation text, “along the fitted reference trajectory” could make the distinction from a derivative of the terminal fitting map even more immediate. The section's definitions already make this precise.
- A short reader-facing dependency list separating B.1 value capture, C.4.5 reference fitting/active moments, and the new cavity/mesh estimates would help navigation through the long proof. It would not change the mathematics.
- Keep the present distinction between symbolic finiteness and an evaluated conditioning certificate. The bound involving (B_Q\), \(\Gamma_\infty^+\), and (J_0\) proves finiteness; this review supplies no useful numerical response constant.

**Final scientific decision: ACCEPT the exact frozen proposed scope.**
