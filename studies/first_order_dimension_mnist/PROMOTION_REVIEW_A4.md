# Independent complete scientific promotion review A4

**Verdict: PASS for the frozen v3 candidate's stated finite initialization, algebra, implementation and comparison-method scope. No necessary correction or unresolved scientific objection was found.** This is one independent scientific review, not promotion approval, a whole-book review, or the separate assembled-edition integration review.

Reviewer: `/root/review_a4`, 2026-09-16. Candidate manifest SHA256: `c150f99336f891c6f38c8485b58c3ba0f1971123da142240e85b267108867de0`. Frozen root: `/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v3`. All review outputs are in `/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a4_v3/`, except this original report. Every one of the 36 manifest-listed file hashes matched before the audit and again after execution.

## Independence, input boundary and read coverage

I received the neutral review assignment and manifest in a fresh reviewer context. I have not authored, assembled or selected this candidate. I read no study README, history, author checks, selector report, prior verdict, other review, other study, or scientific conversation. I used no subagent findings. Placement and assembly files were hashed without reading their contents or using them scientifically. No live established code or documentation was used in testing; the import path pointed only to frozen_v3/code. I did not change the frozen inputs, live code/docs, or Git.

I applied the complete Part 2 scientific-review requirements from the supplied workflow, and the `solve-math-rigorously` skill. I also read the supplied investigation skill and its adversarial-audit and decisive-experiments references for the bounded checks. The system mathematical skill read at `/etc/codex/skills/solve-math-rigorously/SKILL.md` has exactly the packet's skill hash. The neutral assignment outside the packet likewise has exactly the packet assignment hash.

Complete substantive read coverage, with file lengths:

| Frozen input | Lines read |
|---|---:|
| docs/observable_p1.md | 1–332 |
| docs/NOTATION.md | 1–98 |
| code/GENERAL_P1.md | 1–212 |
| code/pde/observable_p1_initialization.py | 1–181 |
| code/pde/observable_torch_p1.py | 1–403 |
| code/pde/finite_torch.py | 1–153 |
| code/pde/closure_comparison.py | 1–128 |
| code/tests/test_general_p1.py | 1–297 |
| code/scripts/example_general_p1.py | 1–131 |
| code/scripts/analyze_general_p1.py | 1–46 |
| dependencies/global_nonlinear_source_units.md | 1–393 |
| code/pde/finite_network.py | 1–363 |
| code/pde/gaussian_moments.py | 1–114 |
| code/pde/__init__.py | 1–26 |
| code/pde/observable_initialization.py | 1–397 |
| code/pde/observable_words.py | 1–217 |
| code/pde/observable_arithmetic.py | 1–230 |
| code/pde/observable_fixed.py | 1–223 |
| dependencies/original_docs_README.md | 1–738 |
| dependencies/original_code_README.md | 1–1113 |
| docs/README.md | 1–742; verified identical complete original prefix plus read four-line addition |
| code/README.md | 1–1117; verified identical complete original prefix plus read four-line addition |

The original guides were read in full as context, including their numerical-scope distinctions. I verified by full-file diffs that their candidate versions contain exactly their unchanged complete prefixes and the displayed four-line additions. This covers every scientific line in both versions without treating the repeated older material as a new theorem dependency. Truncated combined tool output was repaired: the tensor engine tail was reread from line 210 through the end; the entire source-unit dependency was reread in ranges 1–115 and 116–393; the original theory guide's affected middle was reread in ranges 360–550 and 551–590. The implementation guide was read in contiguous ranges 1–390, 391–755 and 756–1113. No required scientific text remains truncated or unread.

The source-unit file supplies complete source sections 2–3, H3.1, and H3.N1/N2, including the conditional Gaussian projection, empirical induction, source-response derivation and singular-Gram argument. I did not fetch the original full global_nonlinear chapter. Its original whole-file hash is manifest metadata rather than a independently rehashed original file. Other chapter links and the original guides' external literature are contextual, not imported to finish the candidate's proof.

Unread complement: the placement/assembly contents; nonapplicable investigation references (research-contract, evidence-ledger, proof-search-orchestration) and agent configuration YAMLs, all nevertheless hashed; all unlisted established chapters/modules/tests; all generic compiler implementation not supplied; all study history and other studies. The compiler is not a p=1 dependency, as verified below. There is no missing necessary scientific or runtime input for this candidate. No general-d trained-network convergence theorem, higher-order theorem, MNIST/PCA conclusion or timing superiority was reviewed or inferred.

## Scientific audit

### Initialized law, reused source response and normalization: PASS

The contract distinguishes order p, population integration count P, width n, dimension d and input count m. It uses bias-free two-hidden tanh, stored variances (1,1/n,1/n²), U=x/sqrt(d), output c-transpose h2/n, unhalved probability-weighted square loss and physical mobilities (n,1,n). The finite comparator retains its actual nonzero random readout; the initialized population closure has c=0. These are not coupled by assigning equal integers as seeds.

I independently checked the source calculation. The first d lower tanh features have uncentered covariance v I. Their forward sources therefore have law sqrt(v) times independent upper standard Gaussians. The upper outputs have covariance tau I, and their mean source derivative is alpha I. The actual reversed reused action is consequently R_i=sqrt(tau) Z_i+alpha h_i, jointly with the original G_i. Its innovation variance is tau, without subtracting response variance. The production initializer uses independent child streams for G, reverse noise and upper noise, while computing k from the same lower h; it preserves precisely this required lower dependence.

For a retained lower F and upper B, Gaussian regression on the old forward sources and one-dimensional integration by parts give the first sum of the displayed contraction identity. The source-rule response of the appended forward call gives its second sum. In particular F=k_i has derivative 1-k_i² in reverse source i. Thus C_(H_i,k_i)=alpha beta+tau gamma. Replacing the reverse action by independent Gaussian noise would incorrectly remove both the joint lower correlation and this reuse response. The candidate does neither. The finite smooth-program hypotheses hold for these tanh/linear compositions: finite query count, bounded first derivatives, Gaussian roots with all moments. The supplied singular-Gram proof is complete for the use made here; this is not a growing-time program argument.

Oddness removes feature means and cross-coordinate blocks. Cauchy–Schwarz gives beta²<=v s, and the fixed ridge eta=1/4096 gives b²>=eta+s eta/(v+eta)>0. The exact Cholesky transformation is b=L^{-1}psi, so row tables multiply by L^{-T}, while D=L2^{-1} C L1^{-T}. Subtracting beta/(v+eta) times the h column in the second band leaves alpha beta eta/(v+eta)+tau gamma. The displayed denominator factors a,b,c and production indexing agree. Only the initialized matrix has repeated bands; there is no restriction on later M entries.

The complete d=2 dictionary and decoder establish the claimed (5,3) feature count and order. Codes 0 and 1 are the existing population constants. At p=1 there is no retained tail and every action is in the forward/reverse core. Beyond inspection and the maintained dictionary check, I executed initialize_features(1) with a deliberately failing generic-compiler callback; it completed without calling that callback. Changing epsilon_cov from 0.1 to 0.01 left every returned numerical array exactly equal, consistent with the recorded unused source regularizer.

Quadrature is described with the right claim level. Production uses a normalized truncated-normal positive Legendre rule, and its refinement difference and omitted scalar mass are explicitly not coefficient error certificates. A separate untruncated 256-node Gauss–Hermite calculation reproduced v,tau,alpha,s,beta,gamma with largest observed difference 1.11e-16. This is a strong numerical cross-check, not a rigorous quadrature bound. An independent run of the older d=2 finite-Q method at Q=128 differed from the new D by 0.0236935435, as expected from its empirical full Gram and distinct coefficient rule. No finite-Q equivalence was asserted.

### Folding, finite equations and metric: PASS

The proof of the antithetic invariant class uses simultaneous negation of the entire joint mark, not independent sign changes of components. For arbitrary data, lower/upper activations and c are odd, their gates are even, a's constant entry and the upper backward pairing's constant entry vanish. This leaves the constant row and column of M zero and preserves odd w/c velocities. All retained dynamical pairings are even. The base-half mean therefore represents the full paired rule in real arithmetic through both Heun stages. This argument permits a dense nonconstant M and arbitrary input directions and labels; data symmetry is not an assumption. Finite summation differences are correctly limited to roundoff.

For general P1,P2,K1,K2 and nonnegative population weights, differentiating the actual finite predictor gives the pi1-scaled w gradient, pi2-scaled c gradient and unweighted Frobenius M gradient. Multiplying by the stated negative population metric reproduces every factor of two and sample weight in rhs. The reverse contraction uses exactly the transpose of the same moving M. At zero population weights no division is needed: the loss derivative still equals minus the weighted velocity squares. I explicitly tested zero population weights as well as zero input-law weights, unequal populations and unequal feature dimensions. The weighted autograd chain rule and dissipation agreed to floating roundoff; an independent directional loss difference agreed within 1.42e-11 absolute in the tested case.

Blocking only partitions fixed-state sums. Reference and optimized associations, forward precontraction and reverse precontraction preserve the full equations. The implementation never updates between blocks. Heun's second stage uses all three predicted blocks together, and the final update uses both complete velocities. The documented absence of finite-step monotone loss, global numerical stability and a general-d network identification theorem is appropriate.

### Actual finite network comparator: PASS

I read the complete canonical NumPy runtime rather than relying on a Torch-to-Torch comparison. Its initializer draws W1, W2 and the stored readout in that order with standard deviations 1,1/sqrt(n),1/n. NetworkEngine calls it and copies those exact arrays. The mean-square output gradient has factors 1/n; first/readout mobilities cancel those factors, while the middle velocity retains 1/n. The Torch equations and canonical oracle agree on U versus X scaling and all residual/transpose factors. The maintained tests compare the actual random initialization, predictions, dense moving-state RHS and simultaneous Heun against NumPy, and compare nonuniform weighted gradients independently with autograd. My additional width-one test checked both tanh gates with repeated/zero/nonunit inputs and zero/nonuniform sample weights.

Torch's derivative is computed as 1-tanh². This differs numerically from the canonical oracle's protected saturated-tanh derivative in extreme ranges; the candidate expressly discloses this and does not claim the NumPy range protection. Float32/64 and intermediate-overflow limitations are not hidden by the oracle agreement at moderate states.

### Ownership, observations, restart, arithmetic and cost: PASS

Construction and prepared data own copies. Moving states are independently cloned when requested, including zero-step evolution. Fixed tensor/cache and prepared-data identity/version checks reject ordinary in-place edits or replacements. Deliberate PyTorch version-tracking bypass is expressly outside the contract. My checks independently mutated original constructor inputs, original data arrays and returned observation arrays; predictions on the retained prepared data did not change. Mutating the cached b2 transpose and replacing a prepared label tensor were rejected on the next evaluation.

The initial/current observations use identical marks and inputs; the upper initial activation is reconstructed from g and D. Initial/current cross Grams have initial rows and current columns. Folded paired observations explicitly append the negative half and halve the base weights. I checked a supplied nonuniform antithetic base law including zero weights: both signs, their equal half masses, zero first and third signed moments, and cross Grams agree with direct summation. This matters because an even Gram alone would fail to detect an incorrect unsigned pair law.

Independent permutations of the two populations leave predictions and the matrix velocity unchanged while permuting the associated row/readout velocities. This verifies that matching population array indices carry no unintended cross-population coupling.

The pickle-free restart stores current/frozen arrays, data, representation and arithmetic policy. Same-device, same-policy continuation matched uninterrupted working states exactly on both CPU and CUDA, including my unequal-population, zero-weight case. The implementation checks recorded device type and policy, while exact replay additionally requires the caller to preserve the documented device/reduction environment. No cross-device, cross-version or cross-platform bitwise promise is made. Time is caller metadata and no trajectory or source tape is required.

I recalculated the symbolic retained-state totals, including both frozen transposes/caches, both copies of the action matrix and retained network initialization. They agree with the theory: unfolded equal P uses P(8d+7)+2(d+1)(2d+1) scalar entries; folded B=P/2 uses 8Bd+3B+4d². My unequal-size engine counted 223 float64 entries, exactly 1784 bytes. The maintained example counted closure 2016 bytes and network 5120 bytes. These are tensor-entry counts, not allocator/process memory. Heun's number of state copies is bounded; block activations and optional observation panels are separately accounted for. Full-panel network observations and saved trajectories have their disclosed additional storage. There is no claimed uniform advantage when d grows with n or cost-to-accuracy result.

### Comparison methods and executable recipe: PASS

The comparison API requires aligned ordered unique integer/string sample IDs and matching sample axes. Grams are raw uncentered objects; neither predictions nor Grams are fitted, centered or calibrated before comparison. Constant predictions have undefined correlation even for nonbinary decimals such as 0.1, avoiding a rounded-mean residual falsely producing a correlation. Zero-reference and absent-class cases use the documented null/zero conventions. All individual seed pairings and the reference mean are exposed; identical seed indices are not treated as coupled initializations.

Loss matching receives only times, training losses and a target; it cannot select by passive prediction agreement. It handles nonmonotone losses, requires the target inside the attained saved range, resolves equal-distance ties by earliest time, and reports lower/upper loss brackets. The guide correctly distinguishes physical-time comparison, independent stopping, one fixed reference loss and one common loss across all systems. Matching training loss supplies no pure-clock-change or map-equivalence theorem.

I read the complete producer and analyzer. The producer builds fresh initialization, performs both actual finite evolutions, writes full current/frozen arrays and source/output provenance, and declares a narrowly operational scope. The analyzer independently reconstructs predictions and Grams using NumPy, checks their tolerances and output hashes, recomputes metrics and checks optional repeated arrays exactly. It is a replay/operation check rather than an independent network-approximation experiment. Four fresh producers completed: two CPU and two cuda:0, followed by both exact-repeat analyzers. Both guide Python examples also ran successfully, and importing pde alone did not import torch.

## Executed checks and evidence

All commands used `/home/amir/miniconda3/bin/python -B`; environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130; one numerical thread, `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, `PYTHONDONTWRITEBYTECODE=1`, `CUBLAS_WORKSPACE_CONFIG=:4096:8`, and `TMPDIR=/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a4_v3/tmp`. `PYTHONPATH` was `/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v3/code`. The assigned GPU was cuda:0, an NVIDIA GeForce RTX 3090. GPU processes used the declared 0.15 allocator fraction. Reference settings disabled TF32 and used deterministic algorithms and highest float32 matmul precision. Guide examples used their unmodified process policy; reference comparisons used the explicit policy above.

The following command forms were actually executed with absolute interpreter/import paths and fresh study-owned destinations. Let F denote the frozen root and R the reviewer output root declared above:

```sh
PDE_TEST_DEVICE=cpu /home/amir/miniconda3/bin/python -B "$F/code/tests/test_general_p1.py"
PDE_TEST_DEVICE=cuda:0 /home/amir/miniconda3/bin/python -B "$F/code/tests/test_general_p1.py"
/home/amir/miniconda3/bin/python -B "$F/code/scripts/example_general_p1.py" --output "$R/cpu_a" --device cpu
/home/amir/miniconda3/bin/python -B "$F/code/scripts/example_general_p1.py" --output "$R/cpu_b" --device cpu
/home/amir/miniconda3/bin/python -B "$F/code/scripts/analyze_general_p1.py" --run "$R/cpu_a" --repeat "$R/cpu_b" --output "$R/cpu_analysis.json"
/home/amir/miniconda3/bin/python -B "$F/code/scripts/example_general_p1.py" --output "$R/cuda_a" --device cuda:0
/home/amir/miniconda3/bin/python -B "$F/code/scripts/example_general_p1.py" --output "$R/cuda_b" --device cuda:0
/home/amir/miniconda3/bin/python -B "$F/code/scripts/analyze_general_p1.py" --run "$R/cuda_a" --repeat "$R/cuda_b" --output "$R/cuda_analysis.json"
/home/amir/miniconda3/bin/python -B "$R/extra_checks.py" --device cpu --output "$R/cpu_extra.json"
/home/amir/miniconda3/bin/python -B "$R/extra_checks.py" --device cuda:0 --output "$R/cuda_extra.json"
```

The guide check imported pde and asserted torch was absent from sys.modules, then extracted and executed both `python` fenced blocks from the complete frozen GENERAL_P1.md in their displayed order, using the same declared TMPDIR. `guide_examples.log` records both successes. No unrelated examples in the original context guides were executed or claimed as validated.

| Check | Actual result | Retained evidence under R |
|---|---|---|
| Maintained CPU suite | 13/13 pass, unittest time 0.308 s | cpu_tests.log |
| Maintained CUDA suite | 13/13 pass, unittest time 0.980 s | cuda_tests.log |
| CPU recipe with exact repeat | Pass, NumPy replay maximum error 2.220446049250313e-16 | cpu_a/, cpu_b/, cpu_analysis.json, cpu_a.log, cpu_b.log |
| CUDA recipe with exact repeat | Pass, NumPy replay maximum error 1.1102230246251565e-16 | cuda_a/, cuda_b/, cuda_analysis.json, cuda_a.log, cuda_b.log |
| Additional CPU attacks | All pass, script work time 0.292 s | extra_checks.py, cpu_extra.log, cpu_extra.json, cpu_extra.npz |
| Additional CUDA attacks | All pass, script work time 1.218 s | extra_checks.py, cuda_extra.log, cuda_extra.json, cuda_extra.npz |
| Guide examples and lightweight package import | Both Python blocks pass; pde import remains NumPy-only | guide_examples.log |
| Frozen input integrity | 36/36 hashes match before and after checks | input_hashes.json; inventory below |

The extra checks were fixed in `check_plan.md` before their implementation/execution. They used seed 91037, one worker/thread, a 120-second alarm, float64 algebra tolerances 2e-11 absolute/2e-10 relative, directional-loss tolerance 3e-7 relative to max(1,energy), and short-run float32 tolerance 5e-6 absolute/5e-4 relative. No failure-driven parameter search or unrecorded discarded attempt occurred. Largest additional float32 prediction differences after 20 steps of 0.01 were 2.7446311e-9 on CPU and 2.8610464e-9 on CUDA. These are bounded finite-state checks, not error bounds for arbitrary states or horizons.

All producer status files say complete. Recorded validation-work times were 0.07235/0.07055 seconds for CPU and 0.36915/0.38722 seconds for CUDA; these exclude interpreter/import/device setup and final record writes exactly as the guide says. Maximum observed process RSS among these producers was 920518656 bytes. Both CUDA runs recorded peak allocated 33610752 bytes and peak reserved 35651584 bytes. These process measurements include both systems and substantial Torch overhead. They are not individual-system speed/memory benchmarks or cost-to-accuracy comparisons.

## Required corrections, optional improvements and limits

Required corrections: **none found**. Missing required inputs: **none**. Unresolved objections to the finite statements or supported executable behavior: **none**.

Optional maintenance improvement: the current Torch build emits a warning about the legacy TF32 policy API used by the reference tests/producer. A later, separately validated compatibility update could use the supported replacement API. The warning did not affect correctness, determinism or completion on the explicitly documented tested Torch version; changing it is not required for this candidate's acceptance.

The surviving limitations are the candidate's explicit ones: no rigorous finite-quadrature error certificate or automatic tolerance selection; no general-d trained-network or closure-order convergence theorem; no MNIST/PCA empirical result; no finite-resolution approximation accuracy, width requirement, matched-accuracy speedup, global numerical stability, extreme-range guarantee or cross-environment exact-replay guarantee. Passing this review supports the exact algebra and finite implementation under their stated contracts, without upgrading any of those open claims.

The complete proof/dependency reading, independent attacks, maintained CPU/CUDA execution, producer/analyzer reproduction, coverage record and final frozen-hash check are finished. No requested scientific review component is left pending.

## Input hash inventory

The following inventory records every manifest-listed input, including hash-only metadata. `input_hashes.json` retains expected and actual digests, byte counts, line counts and match flags. All entries matched. The manifest itself has the digest stated at the top of this report.

| Frozen path | SHA256 |
|---|---|
| PROMOTION_PLACEMENT.md | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| PROMOTION_REVIEW_ASSIGNMENT.md | `ac4b0fe843f21b54a195ff49d7fe1e82d91eba93be6dd2240c6b21ef7095a2b3` |
| PROMOTION_assemble.py | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| code/GENERAL_P1.md | `982cace29181a9e049fe9e9e88a735c8631015d36614c13d8c81b9074f90f114` |
| code/README.md | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| code/pde/__init__.py | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| code/pde/closure_comparison.py | `650f93aee1590aaf25549dc555e5b2d706c5058e25469b31e988a2b4883ea6f1` |
| code/pde/finite_network.py | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| code/pde/finite_torch.py | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| code/pde/gaussian_moments.py | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| code/pde/observable_arithmetic.py | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| code/pde/observable_fixed.py | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| code/pde/observable_initialization.py | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| code/pde/observable_p1_initialization.py | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| code/pde/observable_torch_p1.py | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| code/pde/observable_words.py | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| code/scripts/analyze_general_p1.py | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| code/scripts/example_general_p1.py | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| code/tests/test_general_p1.py | `9c6b55f4e4efd68fca45ffd0b2095c6a390b582dec28c5dadba50c8b6c15ae12` |
| dependencies/global_nonlinear_source_units.md | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| dependencies/original_code_README.md | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| dependencies/original_docs_README.md | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/README.md | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| docs/observable_p1.md | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| instructions/AGENTS.md | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| instructions/RESEARCH_WORKFLOW.md | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| instructions/investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| instructions/investigate-conjectures/agents/openai.yaml | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| instructions/investigate-conjectures/references/adversarial-audit.md | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| instructions/investigate-conjectures/references/decisive-experiments.md | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| instructions/investigate-conjectures/references/evidence-ledger.md | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| instructions/investigate-conjectures/references/proof-search-orchestration.md | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| instructions/investigate-conjectures/references/research-contract.md | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| instructions/solve-math-rigorously/SKILL.md | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| instructions/solve-math-rigorously/agents/openai.yaml | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |

Outside-packet duplicate inputs also checked: the neutral study assignment has SHA256 `ac4b0fe843f21b54a195ff49d7fe1e82d91eba93be6dd2240c6b21ef7095a2b3`; the system solve-math-rigorously skill has SHA256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`. Both match their frozen copies.
