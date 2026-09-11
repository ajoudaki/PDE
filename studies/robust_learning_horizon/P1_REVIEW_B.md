# Independent scientific review B of frozen packet P1

**Verdict: ACCEPT for the precise scientific claims in P1.** I found no unresolved required mathematical correction or missing proof dependency for the new addition. This is an independent review conclusion, not a promotion decision or an assertion that unchanged chapters have been certified in full.

Reviewer: `/root/scientific_p1_b`, a fresh nonauthor distinct from `/root`, `/root/reference`, `/root/response`, `/root/selector`, and the other scientific reviewer. Review date: 2026-09-11. I read the neutral assignment first. I did not read the study README, author component files, relevance screening, study history, earlier reviews, other reviewer findings, or live canonical sources. I did not contact the other reviewer. The only coordinator clarification concerned manifest provenance fields: the supplied-input and excerpt hashes require verification; unavailable original whole-file and author-component hashes are provenance metadata. It supplied no scientific argument or verdict.

I wrote only this report and files beneath `/home/amir/Codes/PDE/data/generated/robust_learning_horizon/scientific_review_p1_b/`. I did not change an input, live document, or Git state, and ran no training experiment, parameter sweep, or network request.

## 1. Exact scope and complete read coverage

Hereafter A means `P1_ADDITION.md` and D means `P1_DEPENDENCIES.md`, both in `/home/amir/Codes/PDE/studies/robust_learning_horizon/`. All line numbers below refer to those frozen files, not live chapters.

| Input | Semantic coverage |
|---|---|
| `P1_SCIENTIFIC_ASSIGNMENT.md` | Every line, 1–70; first project file read |
| `P1_MANIFEST.json` | Entire JSON, including all input, span, and provenance records |
| A | Every line, 1–1633: statement, margins, limitations, all three proof units, and embedded certificate |
| D | Every line, 1–5014, including the complete supplied older proof bodies |
| `P1_DOCS_README.md` | Every line, 1–273, including the unchanged contextual bibliography |
| `P1_EDITS.json` | Every line, 1–39; every old/new chapter and guide replacement |
| `P1_CERTIFY_REFERENCE.py` | Every line, 1–58 |
| `P1_CERTIFY_TRANSFER.py` | Every line, 1–44 |
| `validate_candidate.py` | Every line, 1–73, before execution |
| `P1_GLOBAL_BASELINE.md` | All bytes for hash, exact excerpt correspondence, and assembly/preservation; 5257 lines |
| `P1_GLOBAL_EDITION.md` | All bytes for hash and exact assembly/preservation; 6892 lines |
| `P1_DOCS_README_BASELINE.md` | All bytes for hash and exact assembly/preservation; 269 lines |

The last three are correspondence inputs. I did not treat them as an instruction to certify the entire unchanged book. Their changed text was semantically read in the edit records, and every selected older proof body was semantically read in D.

The complete required skills were read: `/etc/codex/skills/solve-math-rigorously/SKILL.md` lines 1–115; `/etc/codex/skills/investigate-conjectures/SKILL.md` lines 1–185; its `references/adversarial-audit.md` lines 1–121. I also read its relevant `references/research-contract.md` lines 1–99 and `references/decisive-experiments.md` lines 1–141. The only computation was deterministic certificate/integrity arithmetic within the assignment.

Read-repair record: the initial combined display of D 1–650 and the guide was truncated at the orchestration output layer. I reread D 1–650 alone and reread the complete guide alone. The display of D 3051–3650 was also truncated around the beginning of III.F, and the overlapping display 3371–3850 was truncated within 3609–3620. The union of those displays, followed by an explicit untruncated reread of D 3600–3623, covers every line. No truncated region was counted as read without repair. The untruncated main A chunks were 1–560, 561–1120, and 1121–1633. Other D chunks were 651–1250, 1251–1850, 1851–2450, 2451–3050, 3851–4450, and 4451–5014.

## 2. Frozen integrity, correspondence, and missing inputs

The manifest SHA256 equals the assigned value:

`3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`.

Every entry in its eleven-file `inputs` mapping was verified. Every one of its eight supplied dependency excerpts was independently verified against its `excerpt_sha256`, exact start/end metadata, and declared line count. The three global-nonlinear excerpts also match their exact line spans in the complete frozen global baseline. The full notation span verifies that source's whole-file hash as well.

The source-component hashes and unavailable original whole-file hashes were not rehashed: those originals are outside the permitted frozen read scope. I did not silently treat provenance as verification. No mathematical conclusion here depends on their unavailable complements. In particular, the uninvoked older arctangent all-time/nonaffinity conclusions and other chapters mentioned by the reading guide were not imported to prove the tanh addition. No necessary proof body is missing from the supplied material for the new claim.

Independent assembly reconstruction gave exact equality to both frozen editions. Each of five chapter old strings and two guide old strings occurs exactly once. Their sequential start lines are respectively 27, 1805, 1824, 3842, 3954, and 155, 257. The declared chapter `rstrip` operation removes exactly one final newline byte; the specified two newlines and addition are then appended. The rest of the older complement is unchanged. The guide edits are also exactly the listed replacements. The embedded certificate matches the standalone reference certificate after its two introductory lines are removed.

Complete input/excerpt/output hash tables are recorded in the appended integrity inventory and in the independently generated `independent_integrity.json` in reviewer scratch.

## 3. Reconstructed claims and dependency audit

### 3.1 Model, metrics, and derivatives

The stored forward map is $z^1=W^1u, z^2=W^2\tanh z^1, f=(W^3)^T\tanh z^2/n$, where $u=x/\sqrt2\in S^1$. Variances are $1,1/n,1/n^2$, independently by block and entry. Differentiating the unhalved probability-mean square loss with mobilities $(n,1,n)$ gives exactly A 1345–1352. There is no residual inside the backward fields. The finite middle rank is $v h^T/n$, with ordinary Frobenius norm equal to the product of the two RMS norms. Thus A's raw Hilbert metric has squared finite norm

\[
\|dW^1\|_F^2/n+\|dW^2\|_F^2+\|dW^3\|_2^2/n.
\]

The later comparison metric is the **sum** of full-row RMS, middle operator norm, and readout RMS. Those metrics have different purposes and are not conflated. Only the learned population middle increment is Hilbert–Schmidt. No cross-width operator distance is asserted.

D 3918–4143 supplies the exact finite gradients, energy identity, and finite-GF continuation. D 3372–3912 supplies the fixed-program law, actual adjoint construction, Hilbert–Schmidt calculus, and strong curve rules. D 109–719 supplies the continuous value extension and global two-layer transform theorem. For the reference, B.1's sum-loss mobilities must be $\kappa_i=1/2$; this precisely recovers the present two-atom mean loss. Its hypotheses are met by two orthogonal normalized inputs, tanh at both layers, unit initialization variances, and the vanishing stored Gaussian readout with exponent $\beta=1$.

I checked that the argument does not require a Fréchet derivative of the tanh Nemytskii map from all of $L^2$ to $L^2$. For a strongly $C^1$ curve, the scalar difference quotient, bounded derivative, and truncation of the fixed $L^2$ velocity justify the chain rule. Bounded operator differentiation then justifies the forward product rule. The scalar-gradient/HS adjunction formula is separately proved in D. These are the exact derivatives used in the fitting proof.

### 3.2 Reference existence, symmetry, fitting, and endpoint

For $h=(H^2_1-H^2_2)/2$ and $b=\langle c,h\rangle$, the directional hidden differential $J$ and its adjoint in A 239–257 have the necessary factors $y_a/2$. The feature equation is $c_s=h, (w,K)_s=J^*c$.

Its clock representation uses $j_X=\operatorname{sech}^2j, j(0,g)=g$. At fixed root, $|j(X,g)-j(Y,g)|\le|X-Y|$; the upper readout bound makes the remaining transformed products Lipschitz in the stated $L^2$/operator metric. The closed supremum ball for the readout is complete in $L^2$, and its integral update preserves an enlarged bound locally. The explicit bounds $\|c\|_\infty\le s, \|K\|_{HS}\le s^2/2, \|A\|\le2+s^2/2$, and the polynomial clock bound exclude finite feature-time escape. Fubini and scalar uniqueness identify this with the raw equation rather than a changed optimizer.

The swap map $(w,A,c)\mapsto(wP,A,-c)$ preserves the feature and physical fields. Its invariance is an invariance of the initial joint Gaussian action law and the unique population construction; it is not a pathwise symmetry of one finite random network. Hence $f(Pu)=-f(u)$, $f_1=b=-f_2$. Odd activations give $f(-u)=-f(u)$. No finite-network symmetry is needed downstream.

Strong differentiation gives

\[
c_{ss}=JJ^*c,\qquad b_s=\|h\|_2^2+\|J^*c\|_{\rm hidden}^2=\|\theta_s\|_{\rm raw}^2.
\]

On $g=\|c\|_2>0$, $g_s=b/g$ and $g_{ss}\ge0$ by Cauchy–Schwarz. Since $c(s)=s h_0+o_{L^2}(s)$, $g_s(0+)=\sqrt m$, where $m=\|h_0\|_2^2$. The lower bound $g\ge s\sqrt m$ prevents a later zero. Therefore $b_s\ge m\ge1/10$. This argument does not assume hidden feature norms are monotone individually.

The first forward Gaussian Gram is $qI_2$, so the second preactivations are independent $N(0,q)$, $q=E\tanh^2G$. Consequently $m=v/2$, $v=E\tanh^2(\sqrt qG)$. The certificate gives the claimed lower bound with slack. Thus $b$ reaches 1 at one and only one first feature time $s_\dagger\le10$.

Before that level, the physical field is exactly $2(1-b)$ times the feature field. The integral $t(s)=\int_0^s[2(1-b(v))]^{-1}dv$ diverges at $s_\dagger$, since the continuous $b_s$ is bounded on the compact feature interval. Its inverse covers every physical time. The scalar residual obeys $e_t=-2b_s e$, so $0<e(t)\le e^{-t/5}$ and reference mean risk is $e(t)^2\le e^{-2t/5}$. In particular no finite physical-time zero is claimed.

Integrating $b_s=\|\theta_s\|^2$ and applying Cauchy–Schwarz yields the raw path-length bound and

\[
s_\dagger-s(t)\le e(t)/m,\qquad
\|\theta(s_\dagger)-\theta(s(t))\|_{\rm raw}\le e(t)/\sqrt m.
\]

Every reference state through the endpoint has $\|c\|_2\le\sqrt{10}$, $\|A\|\le2+\sqrt{10}$, and $\|w\|_2\le\sqrt2+\sqrt{10}$. The three scalar prediction gradient norms are bounded by $\|A\|\|c\|_2,\|c\|_2,1$. Their square sum gives the constant below 17, and the segment between two such states preserves the requisite norm bounds. This proves the simultaneous whole-circle estimate $17\sqrt{10}e^{-t/5}$. The input Lipschitz constant is below 76 by the product of the three state bounds. The endpoint is an actual finite-feature-time state, defined from the autonomous equation and first level crossing; its characterization contains no future trajectory oracle and does not assert uniqueness among all interpolants.

**Component verdict:** reference flow, selected endpoint, rates, and whole-circle regularity accepted.

### 3.3 Paired activity with the actual initialized matrix reused

I independently reconstructed both conditioning steps in A 514–625. With $Y_a=A_0H^1_{0,a}$, $U_a=h_0\phi'(Y_a)$, and $P_a=A_0^*U_a$, conditioning on the two initial forward queries gives

\[
P_a=\sum_b \frac{E[Y_bU_a]}q\tanh g_b+\Gamma_a,
\qquad E[\Gamma_a\Gamma_b]=C_{ab}=E[U_aU_b].
\]

The Gaussian $\Gamma$ is independent of the full first root. The deterministic term cannot be dropped. The negligible finite projection has fixed rank two and squared RMS of order $1/n$. $C$ is positive definite: continuity and full Gaussian support reduce a linear dependence to $z_1\phi'(Y_1)+z_2\phi'(Y_2)=0$ everywhere, which forces both coefficients to zero.

For $V_a=\phi'(g_a)^2P_a$, project off the two old forward inputs. The second conditioning of the **same** matrix yields

\[
A_0V_a=\sum_b\alpha_bY_b+\bar d\,U_a+\sigma_a\gamma_a,
\qquad\bar d=E\phi'(G)^2.
\]

The reverse response coefficient is $C^{-1}E[P V_a^\perp]$. Its deterministic-root contribution vanishes by the projection, and its remaining contribution is the $a$-th column of $C$ times $\bar d$. This verifies the coefficient $\bar d U_a$, including its sign. The fresh Gaussian has variance $\|V_a^\perp\|_2^2$; independence from old second-population coordinates is sufficient, and independence between the two new Gaussians is unnecessary.

Conditional variance gives $\|V_a\|_2^2,\sigma_a^2\ge C_{aa}a_0$, while the second-layer activation coefficient gains $r_0$. Here $a_0=E\phi'(G)^4>0.3$, $r_0=E\phi'(\sqrt qG)^2>0.6$, and $C_{aa}\ge vr_0/4>0.03$. Thus both coefficient norms divided by four exceed $0.01$. These are individual-input bounds, stronger than the required two-input average.

I checked the quantitative remainder arithmetic. The fixed initial reverse field has a coupling $|P_a|\le4+|G|$, $\|P_a\|_4<6$, and $\tau_{10}(P_a)<10^{-3}$. The repeated-matrix formula gives $\|R_a\|_4<8$, where $R_a=qU_a+A_0V_a$. The raw small-$s$ estimates imply the first activation remainder

\[
\tfrac12\tau_{10}(P_a)s^2+\tfrac{166}{32}s^4
\]

and the second activation remainder

\[
\tau_{10}(P_a)s^2+\tfrac{515}{32}s^4.
\]

For $s\le1/100$, the second error coefficient is at most $167/64000<0.003$; the first is smaller. They leave more than the stated $s^2/200$ displacement. The constants 44, 116, 55, and 415 in A's derivation account respectively for the reverse-field error, first activation Taylor error, middle-increment/cross-product error, and second activation Taylor error; no term has been omitted.

At physical $t=1/200$, $1-e^{-2t}\le s(t)\le2t$, so $199/20000\le s\le1/100$. The resulting per-input RMS lower bound is at least $39601/80000000000>1/2500000$. Averaging the squared paired displacements preserves this bound. The pairing uses the same initial and current neuron, and the finite-program bridge retains both times in the joint tuple. Predictor convergence alone is not used to infer activity.

**Component verdict:** both-layer activity, matrix reuse, fixed physical time, averaging law, and strict reference margin accepted.

### 3.4 Named sources, fixed-root derivatives, forcing, and response tails

I checked the actual adaptive Gaussian conditioning proof D 3471–3531, source-response cancellation D 3533–3594, and zero-query-noise proof D 3596–3639. The conditioning keeps the residual of the same matrix in its two unqueried subspaces. The finite conditional projection is negligible in normalized second moment. Gaussian integration by parts converts the regression coefficient to expected derivatives of the full named-source expression. Source covariance is the full input Gram, not a variance with an extra subtracted response. Independence of oriented source groups does not imply independence of actual answers.

A 921–1032 supplies the extra justification needed for the tanh clock. Its value extension alone would not justify source derivatives. The exact root derivative is $j_g=\operatorname{sech}^2j/\operatorname{sech}^2g$, which need not be globally bounded. Root clipping first supplies a bounded-derivative instruction at each fixed cutoff. In contrast, the needed $X$-derivative is $\operatorname{sech}^4j\le1$, uniformly in the root cutoff. The complete source chain rules include the past readout derivative and the current matching term $E[c_k\phi''(Z^2_{ka})]$. Expected coefficients, covariances, and deterministic contractions are held fixed under these coordinate derivatives.

At a fixed finite graph, chronological coefficient induction, the uniform first-source-derivative bound, and coupling by positive-semidefinite square roots remove root clipping, including at covariance rank loss. Same-array RMS subtraction independently identifies these expressions with the uncut finite value limits. No inverse covariance is continued through a singularity, and no derivative transverse to a singular support is inferred from an unforced value law.

The improved state ball is justified before forcing. The reference energy path length bounds its learned HS increment and readout RMS by $\sqrt{10}$. Transformed Euler convergence also holds in HS increment norm, since the rank-difference inequality is identical and operator norm is bounded by HS norm. At each fixed sufficiently fine mesh, finite double-Gram convergence of the accumulated ranks then puts the finite unforced programs strictly inside $\|A\|<7,\|c\|_2<4$, using finite $\|A_0\|\le3$. Small fixed forcing remains in that ball by finite same-array stability and positive slack. Its permissible size may depend on the fixed mesh. The pointwise readout bound $\|c(s_k)\|_\infty\le s_k$ survives the forcing exactly by bounded tanh increments.

For the sum metric $d=x+a+z$, I recomputed the three velocity-difference column sums: $8$, $5+16s$, and $11/2+56s$. Consequently the propagation factor is at most

\[
\exp\!\left(\int_0^{10}(8+56s)\,ds\right)=e^{2880}.
\]

A pulse in one reverse answer has immediate clock size $h_j|\epsilon|\|e\|/2$. A pulse in one forward answer has total immediate state size at most $h_j(161/2)|\epsilon|\|e\|$. A later single delta difference is at most $140d$. These establish the displayed bounds for $\alpha$ and past $\beta$; the present $\beta$ has bound $2S$ only at its matching sample.

The extraction order is essential and is correctly supplied: fix a finite mesh and a small nonzero forcing, take width to infinity jointly with the unused root, apply $E[eV^\epsilon]=\epsilon E[\partial_{\rm slot}V^\epsilon]$, bound the finite pairing by Cauchy–Schwarz, and only then send forcing to zero using the separately proved source-derivative continuity. The factor $\epsilon$ follows because the root enters the complete local expression through the designated answer/source slot; selected coefficients may depend on $\epsilon$, but not on that coordinate. This handles the initially zero reverse sources.

Summing two samples over total feature time at most 10 gives reverse response remainder

\[
2(10)(161/2)(140)e^{2880}+10(4^2)+2(10)
=225400e^{2880}+180=M_Q.
\]

The same calculation bounds the forward remainder by $100(e^{2880}+1)$. The source assignments across the countable mesh family are $L^2$ isometries, so the already constructed common flow inherits the decomposition. Bounded remainders pass by an almost surely convergent subsequence; this is not merely a marginal subsequence argument. The actual reference's reverse Gaussian variance is at most 10, with 16 used as a convenient weaker bound in transfer.

The tail estimate does not presume independence between the bounded remainder and the Gaussian. Pointwise domination by $\sigma|G|+M_Q$, elementary Gaussian exponential moments, and then a square root suffice. The passage to finite GF uses continuous positive-part cutoffs and uniform $L^2$ time-Lipschitz bounds. A fixed time grid is taken before the width limit and refined afterwards. Thus the claimed individual finite reference tails are established uniformly in time, without a maximum over a growing sample set or a Gaussian path.

**Component verdict:** source identities, zero-forcing/rank-loss order, improved exponent, reference-tail production, and finite-tail passage accepted.

### 3.5 Raw GD, finite reference, arbitrary laws, and strict event margins

The actual finite reference is GF on the two reference atoms with the same three initialized arrays as the perturbed algorithm. Its readout is not zeroed. On A (8), its initial loss is at most $25/16$. The raw energy identity bounds each displacement through time 40 by $\sqrt{125/2}<8$; each individual state component is therefore below 11. Its readout supremum is at most $1+80(5/4)=101$. This supplies the deterministic finite-state and velocity bounds used in the observation and tail passage.

The two orthogonal active projections are exactly the two first-row columns. Thus the B.1 bridge controls the full first row, allowing passive circle directions from that same trained row. At fixed auxiliary transformed mesh, adjoining finitely many passive forward measurements, active reverse answers, and paired time-zero measurements stays within the fixed-program theorem. The backward product is clipped beyond the proved readout bound; clock stability is at fixed root. Taking width first, then removing the mesh, gives the required second-moment observations. Uniform time/input estimates and fixed finite nets extend these observations to the whole circle. This is separate from convergence of actual GD with its growing transcript.

For transport, I recomputed the explicit bound from factor subtraction. On the $B=12$ ball, the top backward difference has coefficient $313(1+R)$, the lower one $3792(1+R)$, with tails $24\tau_R(\bar c)+2\tau_R(\bar Q)$. The sum of the three integrand coefficients, including the changing input vector in the first-weight field and the overall factor two, is exactly 661180, below $10^6$. The tail coefficients are bounded by 676 times the stated reference-tail sum. There is only one power of the cutoff. The proof uses an arbitrary coupling, and its tails depend only on the reference marginal, so no atom-weight lower bound, Gram inverse, support separation, or regularity of the actual law is required.

Stop the actual raw-GD/reference-GF distance at its first value 1. On that prefix both state norms are below 12. The preceding actual GD node lies on the prefix too. Both speeds in the comparison metric are bounded by $V=2(13)(144+12+1)=4082$, so replacing that node by the raw interpolant costs at most $V\eta$. The reference has no raw-field defect. Integrating the transport bound gives A (14) with $K=40\cdot10^6$. Its small right side excludes the stopping time by continuity. No GD energy identity or transformed-Euler/raw-GD equality is assumed. In this last argument $\eta\to0$ is sufficient; retaining the theorem's stronger $\eta\sqrt n\to0$ is valid.

The chosen cutoff $R=e^{2900}$ exceeds $4M_Q+20$ and 101. The logarithmic estimates leave both deterministic comparison errors strictly below $d_0/4$, $d_0=10^{-18}$. All enormous quantities remain fixed finite real constants before taking any width limit; no numerical representation of the double-exponential radius is required. Thus the positive excess of the full-time state distance above $d_0/2$ tends to zero in probability for each fixed nearby law and empirical approximation sequence.

The same-input prediction bound $2B^2D$, reference endpoint error below 0.019, and preceding-node time error give a positive excess over $1/16$ tending to zero. On the comparison event, $|f|\le12$ and its normalized-input Lipschitz constant is at most 1728. Therefore its binary squared loss has joint transport Lipschitz constant 44928. Comparing either law to the reference atoms gives limiting risk upper bound $1/256+1/256=1/128$, strictly below the announced $1/4$. The initial risk tends to 1 uniformly over binary-label laws because the initial predictor is bounded by the vanishing readout RMS.

For activity, the evolved-state change costs at most $4(B+1)D$, and changing the input in the paired squared-displacement integrand costs at most $8B^2|u-v|$. The separate paired reference convergence and the strict reference RMS bound give a deterministic lower bound exceeding

\[
(1/2500000)^2-26\cdot10^{-18}-10^{-18}
=1.59973\cdot10^{-13}>1.59\cdot10^{-13}>10^{-13}.
\]

The margins are strict, so vanishing errors actually imply probability tending to one for the displayed weak-threshold events. The three risk/prediction events and two activity events can be intersected by a finite union bound.

For iid samples, the finite Borel-partition argument proves empirical $W_1$ convergence without boundary-zero or atom assumptions. The other random events concern only initialization and one fixed reference; there is no need for a uniform-in-data width theorem. This validates arbitrary relative sample/width growth. Perturbed supports can be degenerate, nonorthogonal, nonatomic, or have conditional label noise, as long as the fixed law lies in the stated open $W_1$ ball.

**Component verdict:** actual-GD transfer, sample/width limit order, both risks, whole-circle prediction, paired activity transport, and strict probability margins accepted.

## 4. Adversarial checks and their outcomes

| Attack | Discriminator and outcome | Consequence |
|---|---|---|
| Sum loss or a half-square loss could silently change the physical clock. | Recomputed gradients and substituted B.1's $\kappa_i=1/2$; the mean-loss reference clock is $2(1-b)$. | No clock mismatch. |
| A whole-$L^2$ Fréchet derivative could be unjustified. | Checked the supplied bounded-multiplier/strong-curve proof and scalar adjunction separately. | The fitting identity uses valid derivatives. |
| Swap symmetry could be incorrectly imposed on each finite initialization. | Traced the swap through the generated population law and uniqueness. Finite GF is handled without that symmetry. | No finite symmetry assumption. |
| Readout convexity might fail at zero or allow a later zero. | Used the right derivative from $c(s)=sh_0+o(s)$ and the bound $g(s)\ge s\sqrt m$. | The scalar argument covers its initial singularity and all later feature times. |
| Source laws alone might not fix derivatives at zero variance. | Checked explicit slots, query regularization, coefficient continuity, and the independent fresh-root pulse order. | No unsupported derivative identification at rank loss. |
| Clipping the tanh root could hide an unbounded derivative assumption. | Checked the exact $j_g$ ratio and the distinct bounded $H_X$. | Root derivatives are not needed after clipping removal. |
| Better energy bounds might be applied to arbitrary forced paths. | Checked unforced HS convergence, positive finite slack, and small forcing at each fixed mesh. | The improved $M=7,C=4$ ball is legitimate locally in forcing. |
| Stability might be supplied without a small omitted source. | Recomputed pulse coefficients, their time-weighted sums, and $M_Q$. | A quantitative reference-tail source bound is present. |
| The second activity coefficient could lose the matrix-reuse response. | Recomputed both Gaussian conditioning steps and $\bar d U_a$. | Both hidden-layer lower bounds retain the actual matrix. |
| Paired displacement might be inferred from separate activation marginals. | Checked the joint time-zero/current tuple and bounded squared displacement test. | The intended same-neuron observable is retained. |
| Transformed Euler might be treated as actual GD, or used at a width-growing mesh. | Traced the fixed-mesh/width/mesh-removal order and the raw-GD/actual-GF differential comparison. | Both forbidden substitutions are absent. |
| Arbitrary perturbed supports might introduce a hidden Gram condition. | Recomputed the coupling estimate, including the explicit first-layer input vector. | Actual-law Grams are never inverted. |
| Endpoint accuracy could fail between input probes. | Checked full-row reconstruction and common input/time Lipschitz constants before removing fixed nets. | The conclusion is simultaneous over the circle. |
| Limit bounds at the threshold might not imply high-probability threshold events. | Independently checked 0.019, $1/16$, $1/128$, and $1.59973\cdot10^{-13}$ margins. | Positive slack proves the stated events. |
| A frozen or linear model might explain the same risk reduction. | The packet explicitly makes no superiority or causal-necessity claim. | This alternative survives as a mechanism explanation; it does not contradict the stated theorem. |
| The tiny law ball could be topologically vacuous. | Checked the explicit nonorthogonal and noisy nonatomic constructions and transport costs. | The ball is positive and contains the claimed examples, while being impractical in scale. |

No failed proof route was treated as a counterexample. Conversely, no passing constant script was treated as proof of the Gaussian identification, flow, or transfer argument.

## 5. Exact arithmetic, execution, and limitations

All execution commands used working directory `/home/amir/Codes/PDE`. The main authorized validation command was exactly:

```text
python studies/robust_learning_horizon/validate_candidate.py --inputs /home/amir/Codes/PDE/studies/robust_learning_horizon --output /home/amir/Codes/PDE/data/generated/robust_learning_horizon/scientific_review_p1_b/edition
```

The output directory was new (`exist_ok=False`). The process completed with exit status 0 under Python 3.10.12. It launched these exact subordinate commands, each with exit status 0 and empty stderr:

```text
/usr/bin/python /home/amir/Codes/PDE/data/generated/robust_learning_horizon/scientific_review_p1_b/edition/P1_CERTIFY_REFERENCE.py
/usr/bin/python /home/amir/Codes/PDE/data/generated/robust_learning_horizon/scientific_review_p1_b/edition/P1_CERTIFY_TRANSFER.py
```

Reference stdout was:

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

The source of these bounds is exact rational interval arithmetic, not floating-point quadrature: the 80-term exponential sum has a geometrically bounded positive remainder; the alternating arctangent brackets certify the Gaussian density bounds via Machin's identity; density/gate monotonicity gives intervalwise quadrature bounds; the two-sided tail beyond four is controlled by the displayed Gaussian integration estimate; each summand is rounded outward to denominator $10^{12}$. Decimal conversion occurs only for printed summaries. The (.624) and (.633) scales are on the correct sides of the certified square-root interval for (q). The transfer certificate checks ordinary rational/exponential lower bounds, without evaluating the enormous nested exponentials numerically.

I additionally saved and executed an independent exact arithmetic check:

```text
python data/generated/robust_learning_horizon/scientific_review_p1_b/independent_constants.py > data/generated/robust_learning_horizon/scientific_review_p1_b/independent_constants.stdout
```

Exit status 0. It independently verifies the stronger 0.019 reference error, gradient/input Lipschitz constants, the initial reverse-field tail, both activity coefficient bounds, remainder and physical-time margins, finite reference energy ball, final risk slack, and final activity slack. This is a bounded deterministic certificate check, not a training experiment. The full exact source is retained in scratch.

I independently checked assembly and the complete supplied hash/excerpt inventory, first with an inline Python command and then by saving the same check in reviewer scratch and executing:

```text
python data/generated/robust_learning_horizon/scientific_review_p1_b/independent_integrity.py > data/generated/robust_learning_horizon/scientific_review_p1_b/independent_integrity.stdout
```

Exit status 0. Its source and JSON/stdout records retain the exact operations and evidence. Before the standalone run, a read-only inline Python loop had also checked the assigned manifest hash and every `inputs` hash; the independent integrity check repeats those assertions. Read commands were `cat` for the assignment, manifest, complete skills/references, certificate sources, validation source and edit JSON; `wc -l` for coverage; and `nl -ba FILE | sed -n 'LO,HIp'` at the exact A/D ranges recorded in section 1. The complete guide was read with `nl -ba studies/robust_learning_horizon/P1_DOCS_README.md`. All read commands completed with status 0; display truncations and their repairs are recorded above.

The checks prove exact frozen assembly, preservation outside authorized edits, source/excerpt integrity, and the specified rational inequalities. They do not constitute a formal proof-assistant verification, an empirical training test, a finite-width rate, or an audit of all unchanged theory. Bibliographic context in the unchanged guide was read but was not used as an external theorem dependency; the supplied proofs suffice for the new result, and no network retrieval was authorized or needed.

## 6. Required corrections and final verdict

**Required corrections: none found. Missing necessary inputs: none found. Unresolved necessary proof obligations for this packet: none found.**

The scientifically accepted scope is a global fitted **reference** flow and its selected continuous whole-circle endpoint, plus a fixed-accuracy, fixed-time finite-network guarantee for every fixed binary law in the explicitly certified tiny neighborhood, together with early paired activity in both hidden layers. It does not establish global population dynamics or endpoint convergence for arbitrary perturbed laws, arbitrary accuracy for one fixed perturbation, a finite-width/sample rate, an almost-sure simultaneous limit, practically useful robustness radius, or superiority/causal necessity of feature learning. Those boundaries are consistently retained in the new statement, proof, scope edits, and guide.

**Final explicit verdict for manifest `3dc31cc04695cb3fd48741cbfcea8575a746f3182132e93c0ac609cd5ec6e089`: ACCEPT.**

## Appendix: complete verified integrity inventory

The following hashes are SHA256. Source paths in the dependency table identify frozen provenance, not live files read by this review.

| Supplied input | Verified SHA256 |
|---|---|
| P1_ADDITION.md | 741e9a8ee2dfd10db5638c82fc3fa6f35bde4297ab65edeae834f3ee9d001baf |
| P1_GLOBAL_BASELINE.md | 1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9 |
| P1_GLOBAL_EDITION.md | d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1 |
| P1_DOCS_README_BASELINE.md | 95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e |
| P1_DOCS_README.md | 7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e |
| P1_DEPENDENCIES.md | 6dab773038b451c74fcb3be082f92e4dbd3c1b3b6df2ab55c58a27b782d25b69 |
| P1_CERTIFY_REFERENCE.py | f61103c86b278da16334f30e7af2961c41b4bcaae7062c5b8433fe4eef7a2036 |
| P1_CERTIFY_TRANSFER.py | 09da5455910c20ded0caf5dc979a956f43ea98b6039dc3ff98977ad6f6cada90 |
| P1_EDITS.json | 2bdc66ba6ac554bc29f60fdcf6b5ed6b442c69083fad52ec16ed38801e52e1e7 |
| validate_candidate.py | a294bd8193b1393fa31ab634f505b83f08f6a95eb605b65ab57226f944b4295d |
| P1_SCIENTIFIC_ASSIGNMENT.md | aa59c19c5a27c21c7722492d365bddc3bfcc9f8bb0c87a7bc832d6858cbd7544 |

| Supplied dependency span | Verified excerpt SHA256 |
|---|---|
| docs/NOTATION.md 1–98 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md 1841–2452 | c673a8feabc88b7fafd1d57eb9861823c628a00b29a93684dbfd47f04c1c9904 |
| docs/global_nonlinear.md 3835–5257 | b1d34b78bd50354ce2d036046a180a2beba415530472cbd32264684b0b378774 |
| docs/special_data_limits.md 134–1349 | b21046f7674455290f558ebb3da0a3c2f7e5ca113c71be4f1853f91a5ca624d5 |
| docs/special_data_limits.md 3785–4326 | 8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a |
| docs/finite_dynamics.md 1–227 | bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980 |
| docs/finite_optimization_and_controls.md 1–345 | 06f3a5fc06ac766c9562cec9c774fb99e88b93b2ddfb4cf709c85d2de2fab887 |
| docs/global_nonlinear.md 2923–3439 | cf223a3eed88b3755d0379948316534fb44febc9fa1d6f0bb5d282ff8be4ac94 |

| Reviewer output relative to scratch | SHA256 |
|---|---|
| edition/P1_CERTIFY_REFERENCE.py | f61103c86b278da16334f30e7af2961c41b4bcaae7062c5b8433fe4eef7a2036 |
| edition/P1_CERTIFY_REFERENCE.py.stderr | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| edition/P1_CERTIFY_REFERENCE.py.stdout | ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900 |
| edition/P1_CERTIFY_TRANSFER.py | 09da5455910c20ded0caf5dc979a956f43ea98b6039dc3ff98977ad6f6cada90 |
| edition/P1_CERTIFY_TRANSFER.py.stderr | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| edition/P1_CERTIFY_TRANSFER.py.stdout | 97089ac3bf0eebb7a3b7058c4bc1e2e64c6f6af6321af84ff86569d9d0806df5 |
| edition/docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| edition/docs/README.md | 7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e |
| edition/docs/finite_dynamics.md | bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980 |
| edition/docs/finite_optimization_and_controls.md | 06f3a5fc06ac766c9562cec9c774fb99e88b93b2ddfb4cf709c85d2de2fab887 |
| edition/docs/global_nonlinear.md | d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1 |
| edition/docs/special_data_limits.md | 7b64006f383fa2473967332bb1a2f020e599a25ddc21191e703419564703d430 |
| edition/validation.json | fb7b1235b3ab841c8f4d34a150197b5c4f8abca18622f01473d6c3cba77f2a4c |
| independent_constants.py | 27b9ff3b14029d4a60009f523b0efc4ecd69305d09800c523fcf9354170896d3 |
| independent_constants.stdout | 62478421b69fca4b888a59bb7079661d96f01f2067325564bd63cb0b219cb0af |
| independent_integrity.json | c8e4560a8d54f275a189ef205bf922e3a1b99df188474b886e61983c85f3dabf |
| independent_integrity.py | 5999b15b828c5703e7b15b6a280d19b901117955ee48247b043eaaa8a20dc06c |
| independent_integrity.stdout | 568d3a640499c25bcf468307d79c6db69452daea98203d7191263b808d7c209f |

Standalone output root: `/home/amir/Codes/PDE/data/generated/robust_learning_horizon/scientific_review_p1_b/edition/`.
The report hash is supplied separately to the coordinator to avoid a self-referential hash.
