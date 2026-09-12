# Independent complete scientific review B — frozen packet v1

Reviewer: `/root/scientific_review_v1_b`.
Date: 2026-09-12.
Final scientific verdict: **PASS for the stated finite-episode claims.**
Required corrections or unresolved acceptance-blocking objections: **none**.

This verdict covers the actual proposed C.4.10 and its guide additions, with the complete supplied dependency bodies checked below. It is not a relevance verdict, an integration review of the rest of the book, or user approval to promote the addition.

## Independence and actual input coverage

I began with the neutral launch assignment and `scientific_assignment_v1.md`. I am distinct from every listed author/assembler (`/root`, `/root/population_route`, `/root/continuation_route`, `/root/alternative_route`) and the selector (`/root/relevance_selector`). I did not receive or inspect author discussion, the study README, attempts, internal checks, relevance findings, another review, other study contents, chat history, or historical Git contents. No prior verdict was an input. No reading, mathematical reconstruction, or checking was delegated. I did not contact another reviewer. My only message to the coordinator reported my own reading/checking progress.

I read both required skills in full:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/SKILL.md`, plus its complete `references/research-contract.md` and `references/adversarial-audit.md`.

I personally read every line of every assigned packet file. The complete text was returned through `cat` or the following adjacent `sed` ranges. No output was truncated, so no truncation repair was necessary.

| Frozen input | Actual line coverage |
|---|---|
| `candidate_addition_v1.md` | 1–450, 451–900, 901–1300, 1301–1687 |
| `candidate_docs_README_v1.md` | 1–310, 311–580 |
| `frozen_global_nonlinear_v1.md` | 1–660, 661–1250, 1251–1850, 1851–2450, 2451–3100, 3101–3750, 3751–4523 |
| `frozen_special_data_limits_v1.md` | 1–280, 281–549 |
| `frozen_NOTATION_v1.md` | 1–98 |
| `frozen_docs_README_v1.md` | 1–300, 301–578 |
| `frozen_AGENTS_v1.md` | 1–47 |
| `frozen_WORKFLOW_v1.md` | 1–224, including all of Parts 1 and 2 |
| `assemble_packet_v1.py` | 1–110 |
| `validate_edition_v1.py` | 1–108 |
| `scientific_manifest_v1.json` | 1–127 |
| `scientific_assignment_v1.md` | 1–100 |

Total assigned packet coverage was 8,731 lines and 440,014 bytes. This includes every displayed proof, program, reproduction recipe, and guide paragraph, not merely theorem statements or search matches.

The complete old scientific bodies actually supplied and read are global-nonlinear A.1–A.4; B.1 through its continuous-GF width construction; C.4.1; C.4.5.1 §§1–3 and §5; C.4.5.2; C.4.6.3 §§1–6; all of C.4.9 including its supplement and all proof units; and special-data III.F.1–III.F.11. The manifest's exact old-source ranges are the scope of this reading. I did not read the omitted live-chapter complement, and do not certify its unrelated statements, the omitted B.1 GD bridge, other derivative/forcing results merely mentioned in supplied context, or the external literature summarized by the guide. These omissions leave no essential dependency of the new finite-GF theorem unavailable: the needed identities and source, reference, regularity, and width arguments occur in the supplied bodies.

Before scientific work, the current `AGENTS.md` and `RESEARCH_WORKFLOW.md` hashes equalled their frozen copies. Metadata checks before writing found HEAD `13dd024d516f490ea85d5c65878125f089f37f7e`, an empty staged path list, and unrelated concurrent tracked changes. I did not inspect those changed files. I made no Git writes, no established-file edits, no input edits, no worktree or checkout copy, and no training experiment. My writes are this report and my assigned scratch directory only.

No essential scientific input was missing.

## Input identities

These full SHA-256 values were checked against the manifest, with byte and line counts independently verified. The two launch hashes match. A completion recheck verifies that the frozen inputs remain unchanged.

| Input | SHA-256 |
|---|---|
| `scientific_manifest_v1.json` | `a64ca6999b833e24a45b9d63581950bada8306496a7008d7bab627c662865d9d` |
| `scientific_assignment_v1.md` | `337b8e294cec04c977510219f077f0364ce361d1d5d9e5c8a61ae8fbcb5c44fd` |
| `candidate_addition_v1.md` | `0a0cf81422dfbea98661d2fe57b8ae04a02b245be8c1c1b997632605e42eb046` |
| `candidate_docs_README_v1.md` | `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c` |
| `frozen_global_nonlinear_v1.md` | `e8e4a8cfc485bf6330dfbbea871c830bbc5e44d3d571b526442d614a0520218c` |
| `frozen_special_data_limits_v1.md` | `65bda2d0ea6f3b202098466382e8e37cbb359658c8171dcd7a8e15da8724c6c1` |
| `frozen_NOTATION_v1.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `frozen_docs_README_v1.md` | `26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e` |
| `frozen_AGENTS_v1.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `frozen_WORKFLOW_v1.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `assemble_packet_v1.py` | `fc7e22054e152c39df536e6d4f899105b554a1d715da1503bbb171e9cf75d00a` |
| `validate_edition_v1.py` | `af09252f91522e00be5264d4a251afdcded53f1e52b8ed003f7d7b18c57499c2` |

The current process-file hashes were respectively `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` and `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12`, as required.

The required skill/process inputs also have recorded SHA-256 values:

| Skill input | SHA-256 |
|---|---|
| `solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

The completion-only hash check passed for all eleven manifest-listed inputs, the manifest itself, and the two live process files. Its retained result is `data/generated/nonlinear_selection_generalization/scientific_review_v1_b/completion.json`.

## Mathematical audit and component verdicts

### 1. Exact model, independent task family, and observation contract — PASS

NG1–NG8 preserve the two hidden tanh layers, full Gaussian first row, middle variance `1/n`, stored readout variance `1/n²`, normalization by `n`, mobilities `(n,1,n)`, and the unhalved mean loss. The raw middle increment has Frobenius/HS norm without an additional `1/sqrt(n)` factor. The finite rank `uvᵀ/n` has precisely the asserted product-of-RMS Frobenius norm. Every physical run retains one fixed mixture from original initialization. The anchor component is exactly weighted, so the proof has no unaccounted rare-component sampling error.

The Fourier family is specified before and independently of the trained answer. At `s=1`, the absolute derivative coefficient sum is already finite; thus the asserted uniform convergence of the series and derivative is justified. Multiplication by `h=sin²(2α)` preserves oddness, kills perturbations at the anchors, and adds at most four to harmonic degree. A cap at index `N` therefore has degree at most `2N+5`. The label envelope follows from `h=4t²`, `(a³+b³)²=1-3t²+2t³ <= (1-t²)²`, and the two separate `h/8` budgets. This checks both target and noise extremes. `D=0` leaves the nonempty uniform-density class; `R=0` is allowed for approximation but is correctly excluded from the strict-learning subfamily. `sigma=0` is handled by omitting its term and failure allowance.

### 2. Complete Gaussian and reference dependencies — PASS for the consumed statements

I reconstructed III.F's conditioning argument, including adaptive queries. Once the transcript is conditioned on, the next query is fixed and adds a linear constraint to one residual matrix factor. The minimum-norm conditional mean in III.F.6 satisfies both observed orientations. The fresh projected Gaussian noise loses only a fixed rank divided by width in RMS. The source-response formula follows by integration by parts and cancellation of the old-query projection terms. Distinct orientations have independent centered source groups, while responses retain dependence of actual answers; these are compatible claims.

For singular queries, independently perturbing each query input gives a strictly positive innovation variance at each fixed regularization. The same-array bounded-action comparison is uniform in that regularization at a fixed program. Continuity is proved through covariance square roots and bounded source derivatives, rather than through a false pseudoinverse-continuity assertion. The countable language and L2 completion preserve actual adjunction. A.1 supplies the continuous linear-growth value extension; A.2 supplies fixed-graph polynomial derivative envelopes for backward products. These are appropriately fixed-program assertions, not an unjustified growing-transcript limit.

The reference feature construction has a Lipschitz clock system on bounded clock/action/readout sets. Its elementary polynomial bounds prevent finite-feature-time escape. The actual raw chain rule gives `b_s=||theta_s||²`; convexity of `||c||` gives `b_s>=m`. The exact rational certificate proves `m>=1/10`. Thus the first `b=1` endpoint is finite in feature time, whereas physical time diverges there. The resulting bounds `s_dagger<=10`, raw endpoint error `sqrt(10)e^(-t/5)`, and residual decay are sufficient for all new uses. The symmetry argument is an invariance of the population action law; it is not imposed on a finite Gaussian realization.

I also checked both supplied ways of controlling reference queries. The response-pulse argument retains formal names even at zero variance and orders width before removal of the fresh pulse. The cavity argument deletes one initialized column while retaining its learned flow, compares with the full action in the reverse-error term, and conditions on the cavity-good event independent of that column. Its Gaussian maximum proof is a summable grid argument, not a claim that adapted full queries are independent Gaussians. The protected-row separation below only requires the resulting reference moment/clock bound.

### 3. Accumulated source history and support-uniform extension — PASS

The essential audit target is C.4.9 proof unit A, not just its theorem label. In CT12–CT16, every old contribution is an explicitly retained formal source or learned rank. A current passive query has exactly one direct source; an unused old passive query has no descendants. Keeping duplicate spatial inputs as different formal names is consistent with III.F's singular-query convention.

The temporary beta-row cap implies `Q=zeta+J`, with bounded `J` and bounded Gaussian variance. CT28 controls the absolute weighted query sum by Jensen with normalized absolute coefficient masses. CT29 then controls normalized lower pulses without taking the maximum of an increasing collection of Gaussian variables. The upper recursions have bounded derivative row sums and single-old-pulse bounds proportional to its injection mass.

I checked the bootstrap's two separate inputs. First, raw proximity CT34 uses only reference tails and the two nonzero reference controls. Second, CT38–CT44 compare source coefficients using the normalized common mass `m_p=|gamma_p|+|bar_gamma_p|`. The direct discrepancy costs `e_p`; summation returns `sum m_p e_p=q_disc`. The L24-to-L12 interpolation exponent is `1/11`; bounded-gate L12 differences have exponent `1/6`. Both dominate the weakened `1/16` exponent. At most three L12 factors and an L4 propagation factor give L2. The upper derivative recursions introduce only integrated old discrepancies. Thus the first-failed-row argument is causal and does not assume its current cap.

The reference raw anchor is not inferred solely from closeness of value laws. CT22–CT25 and A-supplement.4 compare transformed raw pulses with clock pulses, including their differentiated Euler defects. Their normalized summed defect is bounded by `C_B h_max`, using `sum h_k²<=L_* h_max`; only bounded clock gates propagate it. This repairs the otherwise important distinction between raw and transformed Euler.

Every possible spatial count enters these estimates through an absolute coefficient-mass sum; direction factors have norm at most one. The reference has only its two nonzero controls. Therefore C.4.10.2 §2's extension to arbitrary finite support has no hidden factor in support size, minimal weight, separation, or Gram inverse. The constants `delta_src`, `h_src`, and the tail constants remain separate. The episode definition correctly retains the source radius, rather than deriving admissibility from a tail bound alone.

### 4. Strong construction for bounded Borel and empirical laws — PASS

NSC12–NSC16 are one-reference estimates. Splitting the upper gate against the bounded comparison readout yields a linear L2 bound for `delta` and the actual adjoint query. The remaining lower gate product has cutoff error `2Rd+tau_R(bar Q)`. Optimizing with `R=b_src sqrt(log(e/d))` gives the stated Osgood modulus. The radius `rho_s` is sufficient because `omega(d)<=sqrt(d)` and the anchor-Gram discrepancy is at most `4LC_g omega(d)`.

The projector identity NSC15 has the stated sign and both terms. The identities `B*B=M^-1` and `M>=kI/2` give the advertised projector and projected-gradient constants. The fourth-moment bound NSC17 follows directly from layer cake:

`E|Q|⁴ <= 1 + 4M_src² integral_1^infinity r exp(-2c_src r²)dr = 1 + M_src² exp(-2c_src)/c_src`.

Minkowski gives the row L4 bound. The spatial estimates therefore control full-row changing directions, including the otherwise problematic `w Q` product. Compact data space and a continuous Hilbert-valued integrand justify the Bochner integrals.

The appended Euler histories are shown source-admissible before their bounds are used. They retain the reference prefix and charge the omitted reference suffix. The explicit Osgood solution follows from differentiating `sqrt(log(e/Z))`; its branch condition prevents reaching one, and letting positive error decrease to zero proves uniqueness. The Cauchy construction is strong, so it passes the integral equations. Fatou applies to the nonnegative lower-semicontinuous function `q² 1_{|q|>R}`, preserving the original tail constants; it is not necessary to silently enlarge constants used to define the episode.

Finite quantizers of compact data space have a uniform transport error. NSC20 and NSC23 make their paths Cauchy on the common carrier. A countable dense family followed by this strong completion represents all laws, and W1 continuity also supplies the measurability needed later for random empirical laws. Repeated observations, antipodal inputs, and singular empirical configurations cause no failure. Uniqueness against a competing strong solution requires only the constructed solution's tails.

### 5. Original-mixture continuation and singular selection — PASS

NSC25–NSC28 supply genuine absolutely continuous derivatives along reached controlled curves. In particular `w' Q` is controlled using two L4 factors; bounded readout controls the upper product. The coordinatewise representatives, Fubini, and integrable L2 bounds justify the strong identities and differentiation of `B=GM^-1`. There is no unsupported ambient Hessian premise.

The fixed physical prefix comparison precedes application of the changed-program source bound. It controls the tagged integrated control discrepancy, not just raw state distance. In the post-prefix construction, the affine step is itself a fractional source-admissible update. The residual remainder has coefficient `C_R=2 sqrt(2) L T_g B_r²`: a second scalar integration contributes `1/2`, while the node control mass contributes `(2B_r)²`. NSC34 absorbs this remainder into contraction `k/8`. Telescoping gives NSC35 without an accumulated `hT` defect. Its coefficient `C_s` agrees with `sqrt(2)(8F/k+1)+2B_r`.

The four restrictions defining `T_c` leave strict source and raw margins. Choosing a sufficiently long reference prefix and then small contamination/mesh makes first exit impossible through a physical horizon of order `1/epsilon`. Finite quantization is removed at each separately fixed positive epsilon; its physical field difference has the necessary epsilon factor.

Multiplying the exact residual equation by `GM^-1` gives `theta'=epsilon V+B r'`. The now-justified product rule yields NSC40 with the minus sign on `integral B' r`. Squaring the decaying-residual bound and integrating recovers all three terms of NSC41. For fixed prefix length `b`, the epsilon-limit error is bounded by `E_b`; sending `b` to infinity afterwards removes the initial layer. At unshifted times the remaining difference is at most `V_s epsilon b`. This proves the stated uniform capture only for `tau>=tau_->0`, as required. No actual run changes its mixture or starts at the endpoint.

### 6. Actual finite Gaussian GF and paired full-circle observables — PASS

Finite loss dissipation and the readout supremum bound prevent finite-time parameter escape for every bounded Borel law. At fixed epsilon the horizon is finite. The finite-program proxy uses deterministic population coefficients but the actual same initial arrays and both actual matrix orientations. The zero-readout object is only a comparison oracle. Its fixed-program soft tails, together with the actual readout maximum bound `2n exp(-n²r²/2)`, justify removal of the small initial-readout discrepancy by a finite cutoff induction.

In NSC47 the tail sum includes the two anchor components as well as the quantized added law. Exact coupling of anchors removes their transport error, not their state-comparison tails. Constants depend on the separately fixed physical horizon and controlled mass, not quadrature cardinality. Fractional-step source bounds and L2 time regularity pass soft tails from finite interpolation grids to the entire time interval. The correct approximation order is finite cutoff, finite sufficiently fine law/time approximation, then width, followed by the strong completion; the Gaussian tail dominates the exponential cutoff amplification.

Full-circle prediction and hidden RMS input moduli follow from the full first-row norm and bounded action. Finite input and time nets upgrade fixed-program observations. The reference/mixture union uses the same Gaussian arrays, and Cauchy–Schwarz transfers mixed hidden products and squared distances. Hence NSC49–NSC51 describe an actual paired observable, not differences between independently initialized neurons. Conditioning on every realized empirical law and then bounded convergence is legitimate; no exceptional empirical design is excluded.

### 7. Signed-measure separation and finite conditioning — PASS

NSS4–NSS8 use an active-clock integral envelope, not a claimed passive-input supremum. Its Gaussian-type tail at `R_box²` decays as `exp(-c R_box⁴)`, whereas the Gaussian root box costs only `exp(-C R_box²)`. Thus positive-probability protected rows exist in every fixed direction with nonzero coordinates, even though the envelope and roots are dependent. The hyperbolic primitive traps those rows within a shrinking distance of their large initial roots.

For a finite odd signed measure, select rows from those positive-probability events after intersecting with the full-measure zero-integral set. Bounded convergence against total variation produces hemisphere-sign integrals except at perpendicular atoms. There are only countably many atom directions. The sign kernel's Fourier coefficient is `2 sin(j pi/2)/(pi j)`, nonzero for every odd integer. Oddness already kills even coefficients. The contained Fejer-kernel argument then proves uniqueness for finite measures; it does not merely assert L2 completeness for a possibly atomic measure.

NSS13's stronger middle-block assertion addresses representatives and Hilbert–Schmidt kernels explicitly. Joint representatives are constructed for the one fixed variation measure, and evenness is retained. Tensor simple approximations identify the HS integral with its product-space kernel; bounded factors justify Fubini. Choose an upper coordinate with nonzero readout outside the resulting null sets. Its gate is strictly positive almost everywhere for this variation measure, so vanishing of the weighted odd measure implies vanishing of the original measure. Injectivity of the trained action is unnecessary.

For nonsymmetric `p`, every force/norm involving products of odd functions can use the symmetrized positive density. The projected zero middle block leads to the measure in NSS16. Its density part and finite atomic part are mutually singular, forcing the residual function to vanish. Compactness of the integral operator simultaneously rules out a uniform coercivity constant on the whole infinite-dimensional odd space. The finite spaces `E_N` retain the reference residual exactly; their possible exact dependencies are removed. Compactness of the Lipschitz density class, continuity of finite matrix entries, and `I/2<=C_N<=2I` prove strict positive attained minima `lambda_N` and `lambda_H,N`. No uniform-in-N positivity is claimed.

### 8. Nonlinear approximation and explicit floor — PASS

NGL4 is the exact current-state constrained risk identity; centered population noise has zero force. The tail estimate is `||(I-P_N)r_tau||<=a_N+LV tau`, because `F_*-q_N` is retained in `E_N`. This controls both the omitted target modes and the nonlinear drift out of the endpoint analysis space.

Applying `||x+y||²>=||x||²/2-||y||²` twice gives exactly

`||T_theta r||² >= (lambda_N/4-C_d² V tau)E - (lambda_N/4+L0²/2)b²`.

The condition `C_d²VT<=lambda_N/8` yields decay `lambda_N/2` in the risk inequality and forcing `lambda_N+2L0²`. Dividing forcing by decay gives the stated floor `2(1+2L0²/lambda_N)(a_N+LVT)²`. This argument bounds cancellation between low and omitted modes; it does not incorrectly assume their images remain orthogonal. It keeps the current residual, features, and constraint projection in training. The theorem explicitly declines consistency and does not infer `a_N²/lambda_N -> 0`.

### 9. Separate design/noise errors and uniform sampling stability — PASS

Both random forcing terms are evaluated on the deterministic population path. Independence and centering therefore eliminate the cross terms in their second moments. Conditional label independence given iid inputs justifies the conditional noise calculation; empirical trained features are never asserted independent of their labels. Exact risk dissipation gives the uniform design bound `L²B0²/m`.

Cauchy–Schwarz in time and Tonelli bound the squared integrated forcing, so Markov plus the two allowances produces one event valid for every time in the episode. No unproved temporal supremum concentration result is being substituted. Subtraction under the empirical law leaves exactly `-2I_m+2N_m`; the population reference state supplies the tails for the state modulus. The explicit Osgood comparison then gives NGL9–NGL13. Its asymptotic size is `m^(-1/2) exp(O(sqrt(log m)))` at fixed episode and confidence. This separates a design error from centered label noise without pretending they are independent random terms.

### 10. Robust positive stop, unseen-risk gain, and finite second-hidden motion — PASS

The finite coefficient subfamily NGL14 has a strict budget margin and nonempty relative interior, including `N=0`. The symmetric function `psi=h(cos alpha+sin alpha)` is orthogonal under uniform circle measure to the antisymmetric reference residual `F_*-q0`. Its exact squared norm is `3/8`. The perturbation budget and `p>=1/2` give the positive uniform `e_*` in NGL15 without selecting targets from a trained prediction.

Every entry of the minimum defining the stop is positive and depends only on declared class/reference information. With zero coefficient tail, its floor restriction guarantees at least the stated risk gain. It does not require access to a changed-law trajectory, observed trained risk, unknown regression coefficients, or future noise. Its possible numerical impracticality is stated rather than hidden.

For the hidden observable, the fixed endpoint residual, projection coefficients, and readout are retained only in the analysis functional `O`, not in training. Its endpoint gradient is the hidden part of `d0`, while the actual velocity is `-2d0`; therefore `O'(0)<=-2 gamma`. The fixed-readout auxiliary-state gradient comparison and actual velocity comparison give `|O'(tau)-O'(0)|<=A_H sqrt(V tau)`. The chosen stop keeps this at most `gamma`, so integration proves finite displacement. Cauchy–Schwarz in the circle-plus-anchor direct sum yields precisely `3C²B2 J2`. Thus `j_*>0` concerns actual second-hidden activations, not just hidden parameter motion or an initial derivative. The guarantee is correctly limited to the combined circle-plus-anchor observation.

The sample threshold is the inverse of the stated Osgood bound. Because `d_*<=1/2`, the strict branch condition survives equality at `m=m_*`. The risk and hidden-observable Lipschitz constants spend at most one quarter of each population margin. The remaining margins permit width-first and contamination-second transfer, including replacement of the latent baseline risk by the paired finite reference risk. Conditional probabilities are bounded by one; finite-law capture and dominated convergence give NGL23 in its declared order. The uniformity is in the theoretical constants and sample threshold, not in a width threshold over the full class.

## Deterministic checking and source inspection

Working directory for commands: `/home/amir/Codes/PDE`.
Owned scratch: `data/generated/nonlinear_selection_generalization/scientific_review_v1_b/`.

I inspected the two supplied Python sources completely. I did not execute `assemble_packet_v1.py`, which would read unassigned author assembly units and write packet inputs. I did not execute `validate_edition_v1.py` unchanged, because it reads/copies complete live chapters beyond the frozen scientific scope. Instead I wrote and executed a reviewer-owned checker using only assigned frozen files:

```text
python data/generated/nonlinear_selection_generalization/scientific_review_v1_b/checks.py
```

Execution: exit 0, Python 3.10.12, Linux x86_64, standard library only. Full results are in `checks.json`; the extracted complete certificate is retained as `reference_certificate.py`. Checks performed:

- All manifest hashes, byte counts, and line counts, including the assignment and both author verification sources.
- The complete rational Gaussian certificate, extracted from the frozen C.4.5.1 §5, with its actual exact assertions executed in a fresh namespace. Output was `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`, matching the printed recipe. Extracted program SHA-256: `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e`.
- Exact rational arithmetic on two distinct full-rank 5-by-2 gradient matrices, checking the two-projector identity, projection/idempotence, annihilation of anchors, and the exact residual-selection identity including its signs and epsilon factors.
- An independent rational Laurent-polynomial expansion of `sin²(2alpha)(cos alpha+sin alpha)`, verifying degree five and squared L2 norm `3/8`.
- Exact reconstruction of the two norm-splitting coefficients in NGL7 and the integrated forcing/decay ratio that produces the approximation floor.
- Three numerical inverse-modulus/strict-branch checks at distances `0.5`, `0.01`, and `1e-10`, with `KT=0.1,2,5`; relative roundtrip errors were below `1.3e-15`. These check implementation algebra, not extreme-constant floating-point feasibility of the theorem.
- All 103 new equation labels are unique, paired math delimiters balance, and removal of exactly the three intended guide additions recovers the frozen old guide byte for byte.

The rational certificate is a deterministic bound evaluation. The other finite algebraic cases are sanity checks of formulas already reconstructed above; they are not a substitute for analytic proofs or universal numerical validation. No numerical training, empirical risk experiment, or width-scaling experiment was run. I make no reproduction claim for an empirical scientific result, since none is proposed. The unchanged complete book's links, exporter, and unrelated APIs remain outside this scientific review; they belong to edition/integration validation.

Reviewer checker SHA-256: `925d3807a3f29255b3100f1e5025894c08030450598a3598c0364c135eee3fe2`. Check-result SHA-256: `e809f4c140eda59a413770cacc04d81d2996756d8ec53d37bf6a49c1f7f2e4d3`.

## Objections, limits, and final decision

I found no invalid claimed theorem, missing necessary bridge, or required scope correction in this packet. The principal potential failure modes were: loss of source-mass uniformity with increasing support; using value convergence to identify transverse named derivatives; a circular continuation through `1/epsilon` physical time; an invalid Borel-law or finite-Gaussian-readout passage; continuum coercivity inferred from injectivity; empirical-feature/noise independence; a stop depending on an unknown trained solution; and hidden parameter motion substituted for finite activation displacement. The displayed arguments address these separately, with the checked bounds and limit orders recorded above.

The accepted scope is one finite positive slow episode for the declared odd Fourier family, exact weighted known anchors, bounded centered noise, full-circle input densities, and actual finite GF under ordered limits. The constants may be enormous and are not numerically evaluated. The result does not establish arbitrary-accuracy learning, an all-time changed-law endpoint, simultaneous width/contamination/sample rates, raw GD, circle-only hidden-motion lower bounds, superiority over another architecture, or an efficient independent simulator. These are explicit limitations of the claims, not unresolved objections to them.

**Final verdict: PASS. Required corrections: none.**
