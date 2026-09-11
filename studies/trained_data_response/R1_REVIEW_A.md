# R1 independent scientific review A

**Overall verdict: ACCEPT for the precise frozen scope.** I found no surviving mathematical gap requiring correction in the stated forced clock-state equation, the actual finite-GF right-derivative capture on every separately fixed physical horizon and the whole circle, or the uniform population homogeneous-propagator bound. This is a scientific review of the frozen inputs, not formal verification or a promotion decision. The probability and approximation conclusions retain the quantifiers and exclusions stated below.

## Reviewer identity and isolation

Reviewer: `/root/scientific_r1_a`, an independently spawned reviewer distinct from the four authors listed in the manifest. Assignment received from `/root`; report ownership is exclusively `studies/trained_data_response/R1_REVIEW_A.md`, with scratch exclusively `data/generated/trained_data_response/review_r1_a/`.

I read only the neutral assignment, manifest, four frozen scientific/check inputs, and the two required skills with their research-contract and adversarial-audit references. I did not read the study README, author history or conversations, live component files, other review rounds, or another reviewer's findings. I performed no author startup, Git operation, input edit, training experiment, or parameter sweep. I did not delegate any reading or scientific responsibility. The coordinator's only incoming scientific instruction was the neutral assignment and expected manifest hash. My outgoing interim status contained my own progress, not a request for another reviewer's findings.

Required skills read completely:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- `/etc/codex/skills/investigate-conjectures/SKILL.md`.
- `/etc/codex/skills/investigate-conjectures/references/research-contract.md`.
- `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md`.

The deterministic certificate and algebra checks were explicitly authorized in the assignment. No theorem was supplied from memory in place of a missing frozen dependency, and no external source was needed to complete the dependency chain.

## Frozen provenance and reading coverage

The following SHA256 values were verified before substantive review and again after completing the scientific review. They match the manifest and the coordinator's independently supplied manifest hash.

| Input | SHA256 |
|---|---|
| `R1_MANIFEST.json` | `17cfcd0231bd39079f8f5d4b33e1911201ed3c20d62cce8fe8b5a281cd3cd362` |
| `R1_ASSIGNMENT.md` | `5d49497988a172dabefd80e13c214564018495f28ea0b126e83aaac475eb89d6` |
| `R1_PROOF.md` | `38b2c81be6e32f3d93f7fd85145487b33b2676b6d8698c504230189b9e625721` |
| `R1_DEPENDENCIES.md` | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `R1_CHECK_IDENTITIES.py` | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `R1_REFERENCE_CERTIFICATE.py` | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |

All four embedded component hashes also match `author_sources` in the manifest. All seven dependency-excerpt hashes match their manifest entries. I verified these against the bytes inside the frozen composite files; I did not open the live originals. The separate reference-certificate file is byte-for-byte identical to the complete Python block in the frozen dependency at lines 2677–2732.

Every line of both scientific composite files was read. Initial output truncations were repaired with overlapping smaller reads; a truncated display was not counted as coverage.

| File | Complete coverage and repair details |
|---|---|
| `R1_ASSIGNMENT.md` | Lines 1–49, complete initial read |
| `R1_MANIFEST.json` | Lines 1–90, complete JSON, including every input and dependency-excerpt entry |
| `R1_PROOF.md` | Lines 1–2358. Untruncated coverage: 1–410, 411–830, 831–1230, 1231–1640, 1641–1980, 1981–2358. The earlier partially displayed 1641–1950 read was replaced by 1641–1980. |
| `R1_DEPENDENCIES.md` | Lines 1–3238. Coverage: 1–282; 283–410; 411–617; 618–843; 844–900; 901–1175; 1176–1530; 1531–1840; 1841–2180; 2181–2510; 2511–2820; 2821–3080; 3081–3238. Reads 1–282 and 618–843 repair truncations in the initial 1–410 and 411–900 displays. |
| `R1_CHECK_IDENTITIES.py` | Lines 1–197, complete |
| `R1_REFERENCE_CERTIFICATE.py` | Lines 1–56, complete; also read its contained dependency version |

The proof's local component numbering is used below together with line locations in the frozen composite. The word “reference” means the actual canonical reference supplied by the frozen dependencies, rather than a newly chosen carrier or a conditional source ansatz.

## Exact claim reviewed

The network has two width-n tanh hidden layers, normalized input $u=x/\sqrt2$, no biases, stored variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, output $c^TH^2/n$, and unhalved mean squared loss. The trained reference law is the equally weighted opposite-label orthogonal pair. For each fixed deterministic probability law on the circle with labels in `[-Y,Y]`, the finite flow is differentiated from the right along its mixture with that reference, using the same actual initialized arrays, before taking width to infinity.

The admissible population tangent state is the full two-component first-row clock variation, a Hilbert–Schmidt middle increment, and an L2 readout variation. Its coefficients and source are functions of the already defined autonomous reference state. The initialized middle action and its actual adjoint survive; only the learned and tangent increments have an HS assertion. The observable is uniform scalar prediction-derivative error on a separately fixed compact physical-time interval and the whole input circle. State identification uses fixed-program approximants and same-width norms, not subtraction of operators on different carriers.

The all-time conclusion is a uniform bound for the population *homogeneous* propagator. A bounded persistent data source is only claimed to produce a bound linear in the finite horizon. No uniform-in-time finite-width theorem, positive-contamination nonlinear population flow, nonlinear remainder estimate, raw-GD derivative theorem, or risk/CLT conclusion is included. Constants are independent of perturbing-law support size and atom weights, whereas the convergence probability fixes the law first.

## Component verdicts

| Component or bridge | Verdict | Main proof locations |
|---|---|---|
| Frozen reference construction, fitting clock, and endpoint estimates | ACCEPT | Dependencies 1171–1600, 2034–2109, 2116–2404 |
| Actual initialized actions, reverse reuse, singular fixed programs, and HS metric | ACCEPT | Dependencies 620–1177, especially 719–1002; 1191–1209 |
| Finite right differentiation and exact forced clock equation | ACCEPT | Proof 1852–1911; 366–417; 952–969 |
| Bounded strongly continuous homogeneous generator | ACCEPT | Proof 419–463, 1807–1831 |
| Finite column-deletion query estimate and event conditioning | ACCEPT | Proof 952–1281 |
| Weighted finite uniform integrability and population source admissibility | ACCEPT | Proof 1283–1623 |
| Fixed-program tangent identification and removal of the time mesh | ACCEPT | Proof 1950–2239 |
| Whole-circle, uniform-in-time scalar observations | ACCEPT | Proof 2241–2338 |
| Singular endpoint semigroup and integrable actual-coefficient perturbation | ACCEPT | Proof 465–679 |
| Endpoint fitted-prediction kernel interpretation and nonlinear boundary | ACCEPT | Proof 739–798; 227–253; 2340–2356 |

No component is accepted merely because its deterministic check passed. The checks below supplement the analytic reconstruction.

## Scientific reconstruction and adversarial findings

### 1. Normalization, actual finite initialization, and differentiation

The finite raw metric is exactly

\[
 \|\delta w\|_F^2/n+\|\delta A\|_F^2+\|\delta c\|_2^2/n.
\]

For one input, the three predictor gradients in this metric are $u\phi'(w\cdot u)Q(u)$, $\delta(u)H^1(u)^T/n$, and $H^2(u)$. Multiplication by `-2r` and integration against the law gives the displayed mean-loss field. At the reference, the factor two cancels each atom weight one half. The finite rank normalization therefore agrees with the HS normalization, including the middle-block energy term. This is derived in the frozen finite-dynamics dependency and is retained throughout the candidate.

At fixed width the compact data domain makes the integrated loss smooth on each compact parameter ball. Its probability-law dependence is affine. Energy dissipation bounds all mixture flows on each fixed horizon in a common finite-dimensional ball. Subtraction of integral equations gives an $O(\epsilon)$ path difference, followed by convergence of the difference quotient using the uniformly continuous finite Jacobian. This supplies the actual right derivative without requiring any population law-to-flow derivative or any two-sided probability neighborhood. The argument is sound for nonatomic laws because the loss is exactly integrated, rather than replaced by an empirical data list.

The clock primitive satisfies $F'=\cosh^2=1/\phi'$. Consequently a clock tangent $\xi$ has raw variation $\phi'(w_a)\xi_a$. At the active input $e_a$, the inverse first gate and forward first gate cancel in the *exact* reference clock velocity, before differentiation. Its derivative is therefore

\[
 -2p_a\{\ell_a[V]Q_a+r_a(B^*\delta_a+A^*\delta_a[V])\}.
\]

There is no omitted own-gate curvature term: the identical term generated by differentiating the raw-coordinate conversion cancels it. In contrast, the direct law source must retain the off-support ratio $\phi'(w\cdot u)/\phi'(w_a)$. This distinction is implemented correctly in (5), (S9), and (F7).

The finite Gaussian readout is retained in both the reference GF and its derivative. The source cavity also retains it. Zero readout appears only in the separately identified auxiliary feature program and the population limit. The fixed-mesh comparison from actual readout to zero limiting readout uses its vanishing RMS and supremum, with finite induction and multiplier truncations. It does not silently reset the physical finite network.

### 2. The reference and its endpoint are actually supplied

The dependency constructs the common generated action spaces before solving the reference; its source formulas include both orientations of the same matrix. The fixed-program argument handles adaptive conditioning and singular query Grams. Countable completion gives bounded actions and actual adjoints. Its sharp action bound of two has a contained Gaussian comparison/Poincare proof, so the candidate's $2+\sqrt{10}$ action bound does not rely on an absent sharp random-matrix theorem.

The transformed reference is globally well posed on each feature interval by same-root clock stability, bounded readout, bounded actions, and rank-one differences. Replacing the action-distance norm by the HS norm of its increment preserves these estimates. The symmetry argument is a symmetry of the generated population action law, not an assertion about an individual finite network.

For the feature path, $c_s=h$, hidden velocity $J^*c$, and

\[
 b_s=\|h\|_2^2+\|J^*c\|^2=\|\theta_s\|_{\rm raw}^2.
\]

Convexity of $\|c(s)\|$ away from zero, initialized with right slope $\|h(0)\|$, yields $b_s\ge m\ge1/10$. Thus the first $b=1$ level occurs by feature time ten. The physical clock $ds/dt=2(1-b)$ reaches this endpoint only as physical time tends to infinity, and $e_t=-2b_se$ gives $e\le e^{-t/5}$. The energy path-length bound gives $\Delta(t)\le\sqrt{10}e(t)$, together with the stated readout and action bounds. The rational certificate proving the required lower bound on $m$ is present in full and passed independently.

The active endpoint L4 query bound used by the propagator is also supplied. The dependency proves its source formula by root clipping, bounded source derivatives, singular covariance square-root continuity, a fresh-root pulse estimate, and the ordered width-then-zero-pulse limit. The pulse constants sum with feature-step lengths, rather than with the number of calls. Cross-program source isometries then pass the bounded remainder to the actual flow and endpoint. I found no missing theorem in this dependency chain. The candidate's new weighted-source argument also supplies active fourth moments on the bounded feature interval, but my acceptance of the displayed endpoint dependency does not rest on substituting that route for its proof.

### 3. Column deletion, cavity conditioning, and Gaussian maxima

The source proof's main new estimate uses the actual finite continuous reference, not only a fixed finite Gaussian transcript. Delete initialized column $a_i$, train the complete resulting cavity, and keep the same roots and actual readout. The cavity is measurable with respect to the remaining initialization and independent of $a_i$. The good event used *inside* the conditional Gaussian estimate is $E_n^i$, which depends only on those remaining variables; $E_n\subset E_n^i$. Thus conditioning on the full column-dependent event is avoided legitimately, not by assuming independence after conditioning.

The full-minus-cavity identities (S21) put the full $A$ in front of the changed backward field. This matters: the remainder is exactly the isolated scalar $Z_i=a_i^T\widetilde\delta$, rather than an uncontrolled product of the deleted column with its own changed state. The forward deleted-column contribution on a bounded feature is $\|a_i\|/\sqrt n$. The reverse deleted-column contribution has RMS $ |Z_i|/\sqrt n$. Same-root clock stability consequently gives

\[
 \sqrt n\sup_{t\le T}d(t)
 \le LT e^{LT}(\|a_i\|+2Z_i^\#).
\]

I recomputed the displayed coarse constants: the state coefficients are bounded by $81D_0^4$ and the column forcing coefficients by $36D_0^3$, both dominated by $L=100D_0^4$ with $D_0\ge1$. The changed residuals are included; the cavity is not falsely driven by the full residuals.

The learned transpose term has the coordinatewise bound $4TC^2$ because its exact time integral contains bounded first activations and normalized backward pairings. Together with the cavity discrepancy and $\|a_i\|\le10$ on $E_n$, this yields (S28) with the stated constants. It does not suppose the full backward query is independent of the column.

The conditional Gaussian process has a deterministic RMS Lipschitz metric in time and circle parameter, supplied by finite raw velocity bounds and the readout supremum. The dyadic-net argument sums Gaussian maxima of increments with size $2^{-k}\sqrt{k+p}$; that series is summable, and the constants in (S31)–(S33) have slack. This proves a moment bound for the supremum of *query values*. It requires neither independence among process values nor Gaussian derivative tails. Removing conditional expectation via $E_n\subset E_n^i$ gives the per-coordinate estimate uniformly in $i,n$; averaging then proves (S4). Bounded RMS or exchangeability alone is not being used to infer empirical higher moments.

### 4. Weighted uniform integrability and the all-time population source

The potentially dangerous inverse gate is treated with the exact identity

\[
 \partial_X\cosh^2 J(X,g)=2\tanh J(X,g),\qquad
 \cosh^2 J(X,g)\le\cosh^2g+2|X|.
\]

Therefore the clock weight grows only linearly in the clock displacement beyond the Gaussian-root weight. The actual finite query supremum bounds give moments of the clocks, raw rows, and weighted query products. Gaussian roots have every fixed exponential moment; Hölder handles their dependence on the evolved queries. Higher moments give empirical square-tail estimates uniformly on $E_n$, and $P(E_n^c)\to0$ handles the complement in the stated order. This is an actual finite-GF uniform-integrability proof, not a deduction from a value-only W2 theorem.

For all physical times, the proof uses the auxiliary finite feature equation on `[0,10]` with fixed controls. Its deterministic bounds suffice for the same cavity proof even beyond the population fitting endpoint. The auxiliary zero readout is explicitly distinguished from the physical finite readout. Fixed meshes with passive calls, then width passage, then mesh removal identify its canonical feature flow. Bounded tests and monotone convergence over finite rational parameter lists produce a countable-query envelope $N^\#$ with all fixed moments.

The dense-parameter argument is enough for what follows. L2 continuity gives, for every fixed deterministic parameter, an almost surely convergent subsequence from the dense set, hence an envelope bound in that L2 equivalence class. Fubini supplies the bound for a fixed observation measure and for the active clock time integrals. The proof need not assert continuous population query sample paths or one common null set for every uncountable passive parameter. Its source conclusion is a uniform norm bound and a continuous map into the Hilbert space, both supported by these arguments.

In the main theorem, using $M_w=\sup_{t,u,a}\|\cosh^2w_aQ(u)\|_2$, the first-block squared norm is at most

\[
 \sum_a u_a^2\|\cosh^2w_a\phi'(w\cdot u)Q(u)\|_2^2\le M_w^2.
\]

Thus the constant $2(\sqrt{10}+Y)\sqrt{M_w^2+11}$ has the correct factor, without an unnecessary or missing row factor of two. The other contributions are at most ten and one after squaring.

Continuity of the weighted source is justified by the L2-to-L4 interpolation estimate with bounded L8 envelope, followed by Hölder against the fixed L4 root weight. Changing weights and gates are treated separately using the clock envelope. This gives continuity in time, input, and label into the actual tangent Hilbert space. Compactness of the parameter domain makes its range separable and bounded, so the signed-measure Bochner integral and the TV operator bound are legitimate. The same estimates yield finite random moduli with bounded moments. Exact-cell-mass quadrature therefore approximates every fixed Borel source, including nonatomic laws, without a minimum mass or a support-cardinality constant.

### 5. Bounded operators, singular endpoint conditioning, and actual propagation

The homogeneous linearized maps contain only bounded gates, bounded readout multipliers, bounded actions, rank-one maps, and fixed L2 representing fields. Their displayed norm bounds follow from the finite-rank inequality and $\|B\|_{op}\le\|B\|_{HS}$. The inverse clock conversion is not used as a bounded map. Strong continuity is proved by fixing the tested L2 vector and truncating it; no operator-norm continuity of general multipliers and no ambient Frechet differentiability of the nonlinear L2 field is assumed.

With $D=R^*R$, exact adjunction gives $E=S^*D$. Since $\phi'(w_a)>0$ almost surely, $D$ is injective, although it has no asserted positive lower bound. Consequently

\[
 \ker K=\ker S=\ker E^*,\qquad \operatorname{ran}E=\operatorname{ran}K,
 \qquad K=ES=S^*DS\succeq0.
\]

The finite-dimensional range equality eliminates the nilpotent zero-mode problem that a general positive $ES$ would leave unresolved. In particular, the displayed pseudoinverse semigroup formula follows by the absolutely convergent power series and $(SE)^j=SK^{j-1}E$. It is valid for a singular Gram and for the zero-Gram case. A finite positive spectrum may be arbitrarily poorly conditioned, but at this one fixed reference its pseudoinverse norm is finite. No continuity of the pseudoinverse along the reference or lower Gram-eigenvalue assumption is needed.

The actual nonautonomous estimate does more than freeze this endpoint. Its synthesis columns converge at rate $O(\Delta)$. For evaluation columns, the fixed endpoint L4 query controls the additional gate difference:

\[
 \|[\phi'(w_a)^2-\phi'(w_{a,\infty})^2]Q_{a,\infty}\|_2
 \le 2\|Q_{a,\infty}\|_4\|w_a-w_{a,\infty}\|_2^{1/2}.
\]

Here boundedness of the gate difference and its Lipschitz bound imply its L4 norm is at most twice the square root of the L2 preactivation difference. This is a finite-rank operator estimate, not a norm convergence claim for the multiplier on every L2 input. Residual curvature has norm $O(e)$; the finite-rank terms contribute $O(e)+O(\sqrt e)$. Both are integrable in physical time, giving exactly the displayed finite $J_0$.

Strong-operator Picard integration constructs the evolution on every finite interval. Separability makes the norm of the strongly continuous perturbation measurable. Variation of constants about the bounded endpoint semigroup, followed by the scalar iterated-integral bound, gives $C_U=B_\infty e^{B_\infty J_0}$ uniformly in $s\le t$. This establishes the *actual trained* homogeneous propagator. It also gives the stated L1 forcing bound. It does not imply bounded response for an arbitrary source with merely bounded amplitude over an infinite time interval, and the candidate does not claim that implication.

The endpoint $P_\infty$ is an oblique projection in clock norm onto $\ker E_\infty$, and after the raw conversion it agrees with the orthogonal projection off the span of the weighted raw training gradients. Thus its unseen evaluations can survive without being determined by training-output variations. The candidate correctly refrains from asserting a nonzero unseen change for every direction, a sign, a risk improvement, or convergence of the actual nonautonomous propagator to that projection.

### 6. The finite tangent bridge is supplied independently of source admissibility

After source clipping and fixed-law quadrature, the reference and tangent meshes form fixed finite programs. Every coordinate instruction has at most linear growth: a bounded gate can multiply a tangent node, and readout products have an inactive fixed clip on their already bounded varying factor. Learned and tangent matrices are expanded as finite sums of ranks, so both orientations reduce to actual initialized action calls plus same-layer scalar contractions. There is no independent reverse action substitution.

The population tangent mesh converges by consistency on fixed vectors, extended to the compact solution path using the common operator bound. This strong-operator argument is enough; uniform operator-norm convergence of all multipliers is unnecessary.

The separate finite comparison (F20) is essential and is present. The first line of its defect is not simply declared small from RMS state convergence: (F16) truncates the *mesh testing vectors*. Population testing vectors over the refining mesh family form a relatively compact L2 set, since the population tangents converge strongly and the reference action/gate operations preserve that compact family. Their square tails consequently vanish uniformly. At each separately fixed mesh the corresponding finite tails converge by joint W2. Width passage at that fixed mesh, then mesh refinement with a fixed tail cutoff, and finally removal of that cutoff makes the integrated defect small. The explicit list at proof lines 2161–2177 covers the first gate, upper gate/readout multiplier, forward and reverse action variations, rank products, and evaluation fields.

The bounded actual finite generator propagates this L1 defect to a uniform-in-time same-width tangent error. The source clipping and quadrature errors then pass through the same finite stability bound. This is an actual comparison to the finite linear equation already identified as the right derivative, rather than differentiation of a limiting reference statement. No growing transcript is inserted into the fixed-program theorem.

The topology in (F22) also supports the stated HS assertions: each proxy matrix is a finite rank sum and its HS norm is a finite sum of products of two same-layer Gram entries. The same fact treats finite-rank probes and both actions. Uniform strong proxy approximation then transfers these observations to the actual tangent. It gives the named joint finite-time/input W2 laws and second moments without inventing individual-neuron couplings across widths or a cross-carrier operator distance.

### 7. The whole-circle observable and the quantifier boundary

The Riesz field for passive evaluation has first block $u_aD_a\phi'(w\cdot u)Q(u)$, middle block $\delta(u)\otimes H^1(u)$, and readout block $H^2(u)$. Its norm is uniformly bounded on the circle by the stated reference constants. Fixed-time/input convergence follows from the tangent proxy construction and fixed-program pairings.

Time equicontinuity follows from the reference query's L2 velocity bound, truncation of the fixed reference query when a first gate changes, and the bounded finite generator plus tight source norm. The source estimates are uniform over passive inputs, so this modulus is suitable for a joint time/input net.

For input regularity, the angular derivative of the Riesz field introduces the additional product $ |w|Q(u)$, rather than a new tangent-times-root moment assumption. That product is supplied by the actual finite source envelope and its population counterpart. The proof justifies its strong derivative using the scalar mean value bound, Fubini representatives, and an L2 envelope; the remaining terms use the bounded action and readout supremum. Hence the H1 norm is bounded in probability uniformly over the physical interval at finite width and deterministically in the population. Cauchy–Schwarz gives the required square-root angular modulus. A finite product net, followed by refinement after width passage, therefore proves the full supremum in (10)/(F10).

All deterministic law-approximation and source estimates use compact-domain size, bounded labels, or total variation mass. They do not use atom count, a smallest atom mass, or perturbing-law Gram invertibility. The fixed-program proof nevertheless fixes each quadrature list before width passage, so it supports convergence for each fixed law, exactly as stated. I did not find an illicit upgrade to a probability bound uniform over all laws.

The nonlinear-continuation exclusions are necessary and accurate. The clock norm controls raw variation only in one direction; products of two arbitrary L2 variations remain outside the bounded linear theory. Weighted products along the proved reference/cavity do not automatically control weighted off-support products along an arbitrary perturbed nonlinear path. Similarly, empirical approximation of a nonatomic law in transport distance is not TV approximation. The candidate preserves these distinctions rather than claiming a nonlinear remainder or risk theorem from linear propagation.

## Commands, check results, and evidence limitations

All commands were run from `/home/amir/Codes/PDE`. Reading commands used `cat` for the assignment, manifest, and skills, `wc -l` for the four science/check files, and `nl -ba FILE | sed -n 'a,bp'` for the complete intervals recorded above. The original hash command was:

```text
sha256sum studies/trained_data_response/R1_MANIFEST.json studies/trained_data_response/R1_ASSIGNMENT.md studies/trained_data_response/R1_PROOF.md studies/trained_data_response/R1_DEPENDENCIES.md studies/trained_data_response/R1_CHECK_IDENTITIES.py studies/trained_data_response/R1_REFERENCE_CERTIFICATE.py
```

Two read-only Python heredocs independently checked (i) every manifest input hash and line count plus all seven extracted dependency hashes, and (ii) all four embedded component hashes plus byte equality of the contained and separate rational certificate. Both exited zero. Their output was, respectively:

```text
PASS: manifest entries and all seven dependency excerpt hashes
PASS: all four frozen component hashes; reference certificate equals contained dependency program byte for byte
```

The required deterministic check was run as:

```text
python studies/trained_data_response/R1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/review_r1_a/identities
```

It exited zero with `checks: PASS`; Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. Results are saved in `data/generated/trained_data_response/review_r1_a/identities/results.json`.

- Clock-tangent central-difference errors: `1.0292819331017236e-06`, `2.573205074969171e-07`, `6.433012185025226e-08`, `1.608263607613758e-08`, with the expected factor-four improvement.
- Loss/metric directional-derivative discrepancy: `7.900680110140001e-12`.
- Singular-semigroup identity discrepancies at the five fixed check times: maximum `1.5265444420160054e-14`.
- The script also checks that an incompatible rectangular factorization with `ES=0` can have nonzero nilpotent `SE`.

The complete exact rational certificate was run as:

```text
python studies/trained_data_response/R1_REFERENCE_CERTIFICATE.py > data/generated/trained_data_response/review_r1_a/reference_certificate.txt
```

It exited zero. Its readable output is:

```text
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
```

The underlying assertions use exact rational comparisons and outward rounding of summands. I checked the monotonicity directions: lower squared-tanh bounds use left tanh and right density endpoints; decreasing sech powers use right endpoints; the upper first-layer variance uses the opposite endpoints and the certified Gaussian tail beyond four. The bounds on `.624²` and `.633²` have the correct directions for the nested variance estimates. The floating-point printed list is only a summary of the exact certificate.

My independent check was created only in assigned scratch and run as:

```text
python data/generated/trained_data_response/review_r1_a/independent_checks.py
```

It exited zero with `checks: PASS`; results are in `independent_results.json` in the same scratch directory. Script SHA256: `52e006c8cb2f94367861bfa4c18327830f97b6de895c1ccda327dc322bae0c1b`.

This additional check uses exact Laurent polynomials for the clock identities and exact rational matrices for the singular pseudoinverse/projection identities. Its finite supported block is embedded in `ell²` with diagonal metric `D_jj=2^-j`, which is injective and has no uniform positive lower bound. It verifies the metric symmetry, projection identities, null-vector compatibility, and the reduced rank-one exponential formula; it also checks the incompatible nilpotent boundary and the stated cavity constant majorants. It is an algebraic boundary check, not a simulation of training or a proof of the general convergence claims.

Final verification was run with the following preserved command and exited zero with `checks: PASS`:

```text
python data/generated/trained_data_response/review_r1_a/verify_frozen.py
```

The script reproduces the input, line-count, component, excerpt, and certificate-byte checks above. Final frozen-input verification and scratch-output hashes are saved in `data/generated/trained_data_response/review_r1_a/final_verification.json`. No inputs changed during the review.

## Required corrections and optional suggestions

**Required scientific corrections: none.** No missing required frozen input or necessary proof was found. The component verdicts above are for the exact frozen theorem, with the stated finite-horizon, fixed-law, and linear-response scope.

Optional presentation suggestions, separate from the verdict:

1. In the main theorem's equation (5), explicitly name the pushforward of `sigma` under `x -> x/sqrt(2)` when writing `d sigma(u,y)`. The component proof (S9) already makes this convention explicit with `d sigma(sqrt(2)u,y)`; the mathematical normalization is consistent.
2. In the prose following equation (31), proof lines 766–769, identify `G K^+ G*` as the projection *onto* the training-gradient span and `I-G K^+ G*` as the projection *off* it. The equation is correct; this would make the subsequent “before subtraction” explanation easier to parse.
3. The weighted-source theorem supplies active endpoint L4 finiteness as well as the more specialized imported active source decomposition. Mentioning that overlap could clarify the logical role of the older explicit constant. It is unnecessary for correctness and should not replace the displayed conditioning dependence or imply that either enormous constant is numerically useful.

**Final scientific verdict: ACCEPT.** The frozen candidate provides the required finite differentiation, weighted actual-reference source estimate, fixed-program-to-actual-tangent bridge, whole-circle observation control, and bounded actual population propagator. No approval of promotion or of a larger nonlinear theorem is implied.
