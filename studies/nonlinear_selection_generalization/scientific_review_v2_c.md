# Independent complete scientific review C — frozen packet v2

Reviewer: `/root/scientific_review_v2_c`. Date: 2026-09-12.

**Disposition: PASS for the precise proposed C.4.10 and its stated scientific dependencies and reading-guide addition.** I found no required correction or missing essential scientific input. This is a scientific acceptance recommendation for this frozen packet, not an integration review, a whole-book audit, a numerical-practicality certificate, or user promotion approval.

## Independence, scope and actual reading

I began by reading `scientific_assignment_v2.md`. I am distinct from the authors/assemblers and selector named there. I worked from the neutral assignment and frozen inputs, without author discussion, study README, attempts, old packet, internal verdicts, other reports, other studies, historical Git content, or reviewer messages. I did not delegate any reading, calculation, or judgment. No scientific input was fetched externally. Links in the guides were read as guide content, not followed; those guides explicitly identify their literature list as context rather than theorem dependencies.

I read every line of every file in the following coverage table. The reads were bounded `cat`/`sed` displays, with adequate output budgets. None was truncated. No repair of a truncated read was needed. Later targeted numbered rereads were additional to, not substitutes for, complete reading.

| Input | Complete actual coverage | Read batches |
|---|---:|---|
| `scientific_assignment_v2.md` | 1–100 | Complete initial `cat` |
| `scientific_manifest_v2.json` | 1–127 | Complete `cat`, then hash/size verification |
| `candidate_addition_v2.md` | 1–1693 | 1–300, 301–650, 651–1000, 1001–1350, 1351–1693 |
| `frozen_global_nonlinear_v2.md` | 1–4523 | 1–300, 301–600, 601–900, 901–1250, 1251–1600, 1601–1950, 1951–2300, 2301–2650, 2651–3000, 3001–3350, 3351–3700, 3701–4050, 4051–4400, 4401–4523 |
| `frozen_special_data_limits_v2.md` | 1–549 | 1–280, 281–549 |
| `frozen_AGENTS_v2.md` | 1–47 | Complete `cat` |
| `frozen_WORKFLOW_v2.md` | 1–224 | Complete `cat`, including both parts |
| `frozen_NOTATION_v2.md` | 1–98 | Complete `cat` |
| `frozen_docs_README_v2.md` | 1–578 | 1–210, 211–400, 401–578 |
| `candidate_docs_README_v2.md` | 1–580 | 1–210, 211–402, 403–580 |
| `assemble_packet_v2.py` | 1–110 | Complete `cat` |
| `validate_edition_v2.py` | 1–108 | Complete `cat` |

I separately read both required skills completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, including the latter's complete `references/research-contract.md` and `references/adversarial-audit.md`. Their applicable requirements were used for the contract, quantifiers, counterexample search, complete dependency reading, and calibrated disposition. The assignment prohibits delegation and experiments; I performed only the allowed deterministic checks.

The frozen global file contains complete source ranges 1840–1898, 1903–2274, 3982–4207, 5475–5782, 5999–6595, 7652–8258, and 12994–15322 of `docs/global_nonlinear.md`, with the exact section descriptions in the manifest. The special-data file contains complete source range 3785–4326, III.F.1–III.F.11. I read the complete included proofs, not just their statements. The other portions of the old chapters were not read and are not asserted to have been audited. In particular, the excluded B.1 GD bridge is not needed for this GF-only candidate. References in the supplied material to unrelated chapter results do not discharge any obligation here; the actual dependencies used below have their proofs present in the packet.

Before scientific work, metadata hashes of live `AGENTS.md` and `RESEARCH_WORKFLOW.md` matched their frozen copies exactly. Before writes I inspected current HEAD, status and index names only. HEAD was `b384475316cc0e18bab14438f0140f8f2ede6c9a`; the staged-name list was empty. Existing modifications were preserved and their scientific contents were not read. I made no Git write. My only writes are this report and the assigned reviewer scratch directory.

## Frozen input identities

All hashes are SHA-256. The deterministic check verified every manifest hash, byte count and line count, and the launch manifest hash. The same identities were rechecked at completion, without changing any input.

| File | Bytes | Lines | SHA-256 |
|---|---:|---:|---|
| `candidate_addition_v2.md` | 70286 | 1693 | `b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d` |
| `frozen_global_nonlinear_v2.md` | 188099 | 4523 | `e8e4a8cfc485bf6330dfbbea871c830bbc5e44d3d571b526442d614a0520218c` |
| `frozen_special_data_limits_v2.md` | 46445 | 549 | `65bda2d0ea6f3b202098466382e8e37cbb359658c8171dcd7a8e15da8724c6c1` |
| `frozen_AGENTS_v2.md` | 3045 | 47 | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `frozen_WORKFLOW_v2.md` | 14944 | 224 | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `frozen_NOTATION_v2.md` | 5110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `frozen_docs_README_v2.md` | 44963 | 578 | `26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e` |
| `candidate_docs_README_v2.md` | 46335 | 580 | `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c` |
| `assemble_packet_v2.py` | 5485 | 110 | `1b15be2ce2ff93c88af08fe961f38b103874378c2fe3e7e496e4f9ab6f35933d` |
| `validate_edition_v2.py` | 5657 | 108 | `6a747c207416fb21bb3406a4e10709cbf546b947b67b4ad7d2ec47189e1d65cb` |
| `scientific_assignment_v2.md` | 6009 | 100 | `6d6774ec35ceab6f1011a9dbf2832b2eca95cc156e96750a96b25b196a91f555` |
| `scientific_manifest_v2.json` | 3842 | 127 | `cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7` |

The skill hashes were `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` (solve-math), `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` (investigate-conjectures), `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` (research-contract), and `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` (adversarial-audit).

The assembly-unit hashes recorded inside the manifest are provenance metadata. The author units themselves are outside this assignment and were not read. The actual assembled candidate, rather than those units or a historical summary, is the scientific object reviewed.

## Contract and dependency audit

The claim concerns the exact two-hidden bias-free tanh model, with independent stored Gaussian variances `(1,1/n,1/n^2)`, raw mobilities `(n,1,n)`, readout division by `n`, and unhalved mean-square physical GF. The first-row norm is RMS at finite width; the middle increment uses the ordinary Frobenius norm, corresponding to Hilbert–Schmidt norm; the readout uses RMS. The initialization is fixed independently of observations. Every original run trains from initialization under its fixed mixture, with the two anchor weights exactly `(1-epsilon)/2`.

The main object is an infinite-dimensional raw-state evolution on the established generated Gaussian carrier. It is not advertised as a finite-dimensional scalar closure or a practical solver. The reference endpoint is fixed by a fully specified autonomous feature flow, not a changed-law trajectory. The selected field recomputes features, residuals, gradients, and the anchor projection. Fixed reference data used in constants or in an observation do not replace any trained block.

The horizon is one positive class-dependent slow interval. Limits are width first at separately fixed positive contamination and realized finite sample, then contamination to zero, then increasing sample size. This order is part of the theorem. Uniformity over added laws in the population selection estimate does not imply a uniform width threshold. The candidate explicitly excludes zero slow time from capture and makes no all-time, simultaneous-rate, arbitrary-accuracy, GD, or architectural-superiority claim.

| Dependency | Finding |
|---|---|
| III.F.1–5: fixed Gaussian programs | PASS for the use here. Adaptive Gaussian conditioning keeps the constraints of the reused matrix. Conditional residual matrices and fresh Gaussian answers are used causally. Singular input Grams are treated by fresh-query regularization followed by source-covariance square-root continuity; no inverse is passed through rank loss. Formal named slots survive duplicated queries. |
| III.F.6–8: feedback, common actions, HS metric | PASS. The oracle feedback argument uses normalized pairings and fixed-program bounds. Countable generated laws, finite unions and completion produce the same bounded forward action and its Hilbert adjoint. The rank-one finite representative is `uv^T/n`; its ordinary Frobenius norm is the correct HS counterpart. |
| III.F.9–11 and global A.1–4 | PASS for the consumed statements. Strong multiplier continuity handles bounded gates against fixed L2 variables. Scalar prediction differentiability is proved by weighted Taylor truncation, without asserting an ambient L2-valued nonlinear Fréchet derivative. Continuous at-most-linear instructions are approximated in the appropriate order. Fixed unbounded backward products get derivative-valid clipping at fixed transcript. The sharp initialized bound is supplied by contained Gaussian comparison and Poincaré arguments. The unneeded broader fixed-cap references are not imported as substitutes for source tails. |
| Global B.1 GF construction | PASS for the orthogonal reference. The same-root activation clock gives bounded-set Lipschitz control, with a separate readout supremum, global finite-horizon bounds, HS upgrade for trained ranks, and the fixed-Euler width bridge. The different loss normalization is accounted for when this is used for the two-anchor mean loss. |
| C.4.1 full-row comparison | PASS. Its one-reference cutoff retains the explicit input vector and the full Gaussian row, with one power of cutoff in the propagation coefficient. Neither an input Gram inverse nor a Gaussian maximum over observations is introduced. |
| C.4.5.1 reference endpoint and rational certificate | PASS. The feature energy gives `b_s=||theta_s||raw^2`, positivity of the readout norm yields `b_s>=m`, and the reproduced certificate gives `m>=1/10`. The physical clock remains positive, diverges at the fitted feature level, and gives the stated exponential endpoint bounds and symmetries. |
| C.4.5.2 source responses | PASS. Source extraction takes width at fixed forced graph before zero forcing, with derivative continuity separately justified. The ensuing Gaussian-plus-bounded decomposition is mesh uniform; the actual finite GF bridge retains its Gaussian readout. |
| C.4.6.3 §§1–6 | PASS for the included source/moment claims. Column deletion keeps the learned cavity flow and its changed residuals. Gaussian estimates condition on the cavity-measurable good event, using the subset relation for the full event. The exact learned-transpose coordinate bound and cavity response estimate control actual queries. Dyadic Gaussian increments give the required moments; finite-list truncation, monotone convergence and Fubini transfer the feature-segment envelope to the common population carrier. |
| Complete C.4.9, including A-supplement | PASS. I checked its controlled-source construction, raw-to-clock defect, temporary-cap bootstrap, protected-row conditioning, continued physical mixture, strong residual identity, finite hidden contrast, actual Gaussian readout, and paired width bridge. These provide the exact starting interface extended by C.4.10. |

The most consequential source-bootstrap details are worth recording. In C.4.9.A, old lower pulse injection has its own coefficient mass; zero-control slots inject no later response. Under a temporary beta cap, the query is Gaussian plus a bounded remainder. Jensen is applied to absolute coefficient masses in CT28, so the random amplification has every fixed moment without taking a maximum over an expanding source list. The raw reference anchor obtains a source cap from clock pulses, the transformed raw defect CT22–23, and a causal alpha-then-beta comparison. In CT36–44 the lower-pulse difference is divided by common mass, not a reference mass; summing `m_p e_p` gives the integrated control discrepancy. The L2/L24 interpolation exponent for an L12 difference is `1/11`; weakening to `1/16` accommodates bounded gate differences. Three L12 factors and an L4 amplification supply L2 control. Current alpha uses earlier reverse rows, and current beta uses that alpha and earlier upper responses, so the first-failure argument is not circular. These observations verify the support-uniform extension used below, rather than merely trusting the old theorem label.

## Reconstruction and adversarial checks of the new argument

### 1. Model and target family — PASS

Candidate lines 12–126 specify a family independently of the trained prediction. The coefficient condition with `s>=1` gives uniform convergence of both the odd Fourier series and its derivative. Multiplication by `h=sin^2(2alpha)` preserves oddness and enforces zero perturbation at both anchors. The highest target harmonic at cap N is `2N+5`; the analysis space is permitted to retain the nonpolynomial reference residual separately.

The label bound is valid in the worst sign configuration: with `t=|cos alpha sin alpha|<=1/2`, `(a^3+b^3)^2=1-3t^2+2t^3<=1-2t^2<=(1-t^2)^2`, while `h=4t^2`. Thus the perturbation and noise each consume at most `h/8` of the `h/4` margin. The cases `R=0`, `s=1`, `N=0`, and zero noise remain meaningful; strict improvement is claimed only on the later `R>0` robust subfamily. Positive bounded densities guarantee whole-circle support, including `D=0`, where the uniform density is available. Nonsymmetric densities do not destroy the odd-function argument because the relevant products are even and use the symmetrized density.

### 2. Uniform controls, gradient estimates and Borel completion — PASS

Candidate lines 128–529 extend the finite support result through total masses rather than support cardinality. I checked the references to CT12–16, CT28–31 and CT36–44 against their full proofs. Distinct formal slots at duplicate or antipodal inputs remain valid; passive slots with no future use add no history response. A source radius and a control-mesh threshold are retained separately from the numerical tail constants.

The explicit constants in NSC3–4 have the right dependencies. On the unit endpoint ball, the three gradient blocks are bounded by `a_b c_b`, `c_b`, and one. Forward subtraction has bound `sqrt(1+a_b^2)d`; upper-gate subtraction has coefficient `sqrt(1+4H^2(1+a_b^2))`. The lower changed gate costs `2Rd+tau_R`, since the gate difference is at most one. The chosen cutoff gives `C_g omega(d)`, with `omega(d)<=sqrt(d)` on `[0,1]`. The radius then ensures an anchor gap of at least `k/2`.

For NSC15, expansion gives `barPi P-barP Pi=P-barP`; substituting the gradient columns yields the displayed identity. Since `||GM^-1||<=sqrt(2/k)`, its coefficient is the claimed `4C_g/sqrt(k)`. Thus the projected gradient and field moduli are one-reference estimates, valid even if an arbitrary competing state lacks the constructed tails.

For the fourth moment, layer cake gives

`E|Q|^4 <= 1+4 M_src^2 integral_1^infinity R exp(-2c_src R^2)dR = 1+M_src^2 exp(-2c_src)/c_src`.

This checks NSC17 exactly. The spatial row-gate product uses `||w||4 ||Q||4`; its two factors are supplied by the controlled row update and this bound, without an Lp action assumption. The integrands are continuous into a separable compact Hilbert-valued range, so the Borel-law integrals are Bochner integrals.

Euler histories are source admissible before their tails are invoked. Finite-law paths are Cauchy by the explicit Osgood comparison. Finite quantizers of compact data space have uniform transport error, and the law-force bound passes their strong integral equations to every Borel law. The same constants pass to the limiting query tails: the hard-tail integrand `q^2 1_(|q|>R)` is nonnegative lower semicontinuous, so an almost surely converging subsequence and Fatou retain NSC2 itself. This avoids changing the constants after the episode was fixed. L8 bounds and L2 convergence give the L4 continuity needed later. Restart uniqueness uses the already constructed path's tails and introduces no fresh action or history.

### 3. Strong derivatives and original-mixture continuation — PASS

Candidate lines 530–825 contain the required existence-before-estimate construction. The derivative of a reached gradient is a strong absolutely continuous derivative: `w'` is L4, `Q` is L4, and their product is L2. The other products use bounded readout or bounded activation gates. These bounds justify Fubini and the scalar chain rules, and then the ordinary finite-matrix derivative of `B=GM^-1`. The constants `Z_t,D_t,Q_t,T_g,T_B` dominate each listed derivative term.

The physical residual equation has the correct anchor factors:

`theta'=-(1-epsilon)Gr-2epsilon v`, `r'=-(1-epsilon)Mr-2epsilon G*v`.

The separately fixed prefix is compared to the known reference using only reference tails; the integrated tagged-control discrepancy is then proved small before applying the changed-history source bound. Thus the proof does not assume original-mixture existence in order to obtain it.

At a post-prefix Euler node, the residual Taylor remainder is at most `2sqrt(2)L T_g B_r^2 h^2(|r|+epsilon)^2`, matching `C_R`. The two step restrictions leave contraction `k/8` and forcing `F+k/8`. Telescoping gives a post-prefix control coefficient

`(8sqrt(2)/k)(F+k/8)+2B_r = 32B_r L^2/k+sqrt(2)+2B_r = C_s`.

There is no accumulating `hT` error. The endpoint, residual and missing reference-tail margins, followed by the common `T_c`, keep the first exiting node strictly inside both control and raw radii through physical time `b+T_c/epsilon`. Quantization then gives the same Borel-law flow on each fixed such physical horizon.

Multiplying the exact residual equation by `GM^-1` gives `theta'=epsilon V+B r'`. The proved absolute continuity of B makes integration by parts legitimate. Integrating the exponentially decaying residual and its square gives NSC41, including its mixed `epsilon r_b` and `epsilon T_c` terms. The resulting error has an epsilon-limsup tending to zero as the separately chosen prefix b increases. The shift from `b+tau/epsilon` to `tau/epsilon` uses `tau>=tau_->0`; no interchange of an unproved growing-horizon width theorem occurs, and no physical run is pretrained or switched.

### 4. Actual finite Gaussian GF and paired observations — PASS

Candidate lines 826–973 correctly retain the finite Gaussian readout. Its supremum bound is `2n exp(-n^2 r^2/2)` and its initial RMS tends to zero; it is removed only in a fixed-program comparison oracle. The zero-readout comparison is not the actual optimizer. Fixed graph cutoff induction uses empirical soft-tail second moments to transfer values, avoiding a width-dependent ambient Lipschitz estimate.

The finite raw energy estimate prevents finite-time escape even for Borel training laws. The quantized proxy is fixed before width increases; it uses the same initialized forward matrix and transpose. NSC47 sums query tails over the entire quantized mixture, explicitly including anchors. Coupling identical anchor inputs removes their transport discrepancy but does not erase their state-comparison tails. The readout tail is present separately. This is necessary for the comparison and is supplied as written.

At fixed cutoff, finite soft-tail norms converge. Fixed interpolation grids followed by their refinement give uniform time control because query differences are L2-Lipschitz on the bounded-readout ball. The order is cutoff choice, then sufficiently fine finite quantization and mesh, then width. Gaussian tails dominate the exponential-in-cutoff amplification. Whole-circle input and time nets use proved RMS/L2 forward bounds. Joint finite unions on the same arrays give cross-products for paired hidden activations; separate marginal convergence would not suffice. Conditioning on every realized empirical law, followed by dominated convergence of bounded failure probabilities, is valid because sample draws and initialization are independent and the fixed-law theorem includes repeated observations.

### 5. Signed-measure separation and finite conditioning — PASS

Candidate lines 974–1322 supply the substantial new separation argument. The integrated reference envelope has Gaussian-order moment growth and does not need independence from the Gaussian roots. For fixed nonaxis direction v, a box near `R_box v` has probability of order `exp(-O(R_box^2))`, whereas exceeding the allowed envelope `R_box^2` has probability at most `exp(-c R_box^4)`. Their intersection has positive probability. The clock primitive then protects the large first-row coordinates, so selected rows divided by `R_box` converge to v.

For a fixed finite odd signed measure, Fubini identifies the zero Bochner integral pointwise outside a null set. The protected rows give the sign-ridge integrals for directions whose perpendicular inputs are not atoms. The excluded directions are null because a finite variation measure has at most countably many atoms. The sign-cosine Fourier coefficient is `2 sin(j pi/2)/(pi j)` for nonzero j, hence every odd coefficient of the measure vanishes. Oddness kills the even coefficients. The supplied Fejer-kernel approximation proves measure uniqueness, including signed and atomic measures; no density-only theorem is substituted.

The weighted middle-block argument is also complete. It constructs a jointly measurable finite preactivation representative for the particular variation measure, preserving oddness and named atoms. The tensor HS norm agrees with the product-space kernel L2 norm by finite expansion and completion. Bounded readout makes Fubini applicable. A second-population coordinate with nonzero readout exists because the reference fits an anchor. At almost every input its tanh gate is strictly positive, so the weighted measure must vanish only if the original measure vanishes. The choice of representatives is made for each measure, and no unjustified exceptional set uniform over all measures is required.

After projection, a vanishing middle block gives an odd measure consisting of an absolutely continuous density term and anchor atoms. Mutual singularity forces the density residual to vanish. This establishes injectivity for `T_p` and its hidden restriction. It does not imply a continuum coercivity constant: compactness follows from finite input partitions, and an orthonormal odd sequence has images tending to zero. The proposed positive constants are confined to the finite spaces `E_N`.

The fixed basis for `E_N` is independent of density and target coefficients. Including `F_*-q_0` in this analysis space does not redefine the target family. Compactness of the bounded Lipschitz density class, continuity of its finite matrices, and `I/2<=C_N(p)<=2I` ensure attained positive generalized minima. Exact linear dependencies among generators are explicitly removed. No uniform positivity as N grows is asserted.

### 6. Approximation floor and sampling — PASS

Candidate lines 1323–1497 keep three different errors separate: target-mode tail, nonlinear movement, and finite sampling. The residual is odd; `F_*-q_N` lies exactly in `E_N`, and the omitted component obeys `||(I-P_N)r_tau||<=a_N+LV tau`. The finite coefficient tail is at most `R/(2N+3)^s`; it is zero for the declared finite cap.

Applying `||x+y||^2>=||x||^2/2-||y||^2` twice gives

`||T_theta r||^2 >= (lambda_N/4-C_d^2 V tau)E -(lambda_N/4+L_0^2/2)b(tau)^2`.

This includes possible cancellation between projected and omitted modes in parameter space; it does not assert that their images are orthogonal. Multiplying by the exact dissipation factor `-4`, and using the stopping condition, gives decay `lambda_N/2` with forcing `lambda_N+2L_0^2`. Dividing forcing by decay gives exactly the displayed floor `2(1+2L_0^2/lambda_N)(a_N+LVT)^2`. The analysis operator is frozen only to estimate the evolving nonlinear field.

Sampling forces are evaluated on the deterministic population path, not on trained empirical features. Conditional centering removes noise cross terms, and iid pairs give the required conditional independence. The design variance uses the decreasing population excess risk; the noise variance uses `sigma^2`. Cauchy–Schwarz in time, Tonelli, Markov, and a union bound give separate integrated errors with their respective failure allowances. The uniform state comparison then uses the population path as its tail-bearing reference under the empirical law. The explicit Osgood formula and its strict branch condition prove the simultaneous-time bounds. Zero noise is handled by omitting its allowance and term, not dividing by zero.

### 7. Robust positive stop and finite second-hidden displacement — PASS

Candidate lines 1498–1613 give a nonempty coefficient family with budget `2a+a/4=9R/16<R`, for every fixed finite N including zero. The symmetric component `h(cos alpha+sin alpha)` is orthogonal in uniform arc measure to the antisymmetric reference residual. Its squared norm is `3/8`; allowing the coefficient ball and using `p>=1/2` yields the positive `e_*`. This uses an independently specified target component and is not a lower bound chosen after observing a fitted risk.

Every quantity in the stop depends only on the declared finite class and the fixed reference. All are finite and the needed eigenvalues are strictly positive. The stop ensures a floor below `e_*/2`, hence a positive unseen-risk gain `a_*`. The constants may be extremely small or large; this affects usefulness, not existence of the claimed positive time and finite threshold.

For hidden activity, the fixed-readout scalar contrast has endpoint gradient `((d_0)_H,0)` and derivative `-2||(d_0)_H||^2`. The endpoint conditioning supplies `gamma`. Its derivative remains negative throughout the declared interval because the auxiliary fixed-readout state lies in the unit raw ball and the one-reference estimate bounds its gradient. The constant `A_H` accounts for both contrast-gradient change and actual velocity change. Integrating the sign gives `|Delta O|>=gamma tau`, then Cauchy–Schwarz in the second population and in the circle-plus-two-anchor direct sum gives `J_2>=gamma^2 tau^2/(3C^2 B_2)`. This proves finite activation displacement, rather than merely a hidden parameter velocity. The theorem correctly specifies the combined observation measure and does not claim a circle-only lower bound from this estimate.

### 8. Sample threshold and ordered finite-GF conclusion — PASS

Candidate lines 1615–1693 invert the Osgood modulus on its correct branch. `d_*<=1/2` ensures the strict inequality needed for the comparison. For any fixed confidence and class the inverse error is positive, so `m_*` is a finite integer in exact arithmetic. The hidden Lipschitz coefficient `H_L=sqrt(1+a_b^2)` follows by action/first-feature subtraction. The squared-distance difference is at most `4H_L` times raw distance, while risk differs by at most `2(c_b+1)L` times that distance. The chosen threshold therefore loses at most one quarter of each positive population margin.

Width and contamination transfer use the remaining margin from `3/4` to `1/2`, with same-array reference observations at the same finite physical time. Uniform circle prediction convergence implies excess-risk convergence. Dominated convergence over sample realizations does not exchange width with contamination; the empirical-law theorem holds for each realization. Increasing m only after the other limits gives probability tending to one, as claimed. There is no inferred simultaneous growth regime.

## Actual deterministic checks and verification-source audit

Working directory was `/home/amir/Codes/PDE`. I ran:

```text
python data/generated/nonlinear_selection_generalization/scientific_review_v2_c/checks.py
```

The command exited 0 under Python 3.10.12 on Linux x86_64. The script is reviewer-owned scratch, reads only the frozen scientific packet plus shared instruction hashes, and performs no training. Source SHA-256 is `c56148b31008a34731b4db50a5f8ca7cac2f4a22d85b325ccf16f63407eddf16`. The complete output is `data/generated/nonlinear_selection_generalization/scientific_review_v2_c/checks.json`, SHA-256 `7e8762e38201733f4652cb9e22b6b4112fa2dfc1f954119749f11c3d3a8d1836`.

The executed checks were:

- Exact manifest hash, byte, and line assertions for all frozen files; exact launch manifest identity; live/frozen process-file equality.
- The complete rational Gaussian certificate extracted from the already-read frozen C.4.5.1 §5. The extracted program SHA-256 is `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e`. Its output was `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; all exact rational assertions passed. I checked its exponential remainder ratio, outward rounding, density bounds from the arctangent identity, monotone quadrature directions, and Gaussian tail allowance by reading the complete producer.
- Exact rational nonorthogonal 3-by-2 examples of the projector identity NSC15 and anchor annihilation.
- Exact rational boundary substitutions for the label margin, the completed-square identity, the contraction-floor ratio, and the robust Fourier zero-mode coefficient `3/8`.
- Osgood inverse round trips at `(radius,KT)=(0.5,0.1),(0.01,2),(1e-6,5)`, including strict branch assertions. Relative errors were approximately `6.66e-16`, `1.21e-15`, and `4.24e-16`.
- Balanced new display/inline delimiters, 103 unique new equation labels, no collision with labels in the selected frozen dependencies, no study/generated-path dependence in the addition, and the two new C.4.10 guide fragments plus the roadmap sentence.

The rational identities and test cases are supplemental checks, not proofs of the infinite-dimensional arguments. The Gaussian certificate is exact arithmetic; the three inverse round trips are floating-point diagnostics. The general identities and limiting steps were checked analytically above.

I read `assemble_packet_v2.py` and `validate_edition_v2.py` completely but did not execute their original main functions. The assembler reads excluded author units and writes the packet; the validator reads the unread full old chapter complement and makes a selected-file edition. Instead, the allowed frozen-input checks, including the same complete rational certificate, were run in my own scratch. This preserves the assignment's scientific input boundary and does not claim a separate full-edition integration validation. The supplied validator's own limitations are appropriately stated: elementary checks and assembly preservation do not certify analytic continuation or generalization. Its source has no training experiment or empirical claim. No unrelated exporter was run.

## Required corrections, limitations and final disposition

Required corrections: **none identified**. Missing essential scientific inputs: **none identified**. Unresolved objections blocking the exact stated theorem: **none identified**.

The reading-guide additions accurately summarize finite-episode generalization for the independently specified odd Fourier family, separated design/noise error, a positive class-determined stop, robust unseen-risk improvement, the combined circle-plus-anchor upper-hidden observable, and the ordered GF limits. Their caveat about unevaluated conditioning constants matches the theorem. The older guide and chapter complement remain outside this fresh proof audit.

The proof does not establish efficient computation of its constants, universal consistency, arbitrary target learning, arbitrary-accuracy fitting by extending this interval, a final changed-law endpoint, a circle-only hidden-motion margin from NGL19, a simultaneous width/contamination/sample rate, raw GD, or advantage over another architecture. These are explicit scope limits, not missing premises for the result actually claimed.

**Final scientific disposition: PASS for frozen candidate `b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d` under manifest `cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7`.** The original complete report is retained at this path. Its completion hash is returned separately to the coordinator.
