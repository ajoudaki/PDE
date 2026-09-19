# Independent C-X1 implementation and conditional-closure audit

Date: 2026-09-19. Frozen candidate: proof `74be7dae60f7771123158f51c9e913b3f4b664a87754735c38fa406d514a26ae`, module `a4f31a3ae2a5fe1346f6c465d1c5b4b1ecce7c0db67974056cb58a6ffec78612`, tests `f4fd69bb965ce6147c088a228d74c6da9f4b92021dd312667e66d874ed17a735`.

## Verdict

The mathematical closure theorem passes this audit **conditional on all of Input C**, including its canonical Gaussian program rule, strong target solution, training-averaged exponential reverse-query tails, and actual finite-GF identification. I found no missing mathematical bridge in H1, H2, the dense dictionary construction, or the successive numerical limits. This is not verification that Input C holds for the study's proposed family or learning horizon.

The executable claim for every fixed input dimension requires a repair: the candidate delegates exponent enumeration to a recursive maintained helper whose call depth grows as `2d`. This fails at otherwise modest dictionary sizes in an ordinary Python process. A related syntax-work estimate omits recursive tuple-copying work. Thus the frozen candidate is **revise before accepting the full dimension-general implementation claim**, despite six passing bounded semantic tests. Neither issue refutes the conditional population theorem or the tested small-dimensional implementation.

## Scope and independence

The assignment was an isolated audit, with no author startup, study history, other study, review report, or prior verdict as scientific input. I read the complete candidate proof, module, six-test file, validation plan, operational driver, validation summary and dependency-hash manifest. Maintained scientific inputs read were `docs/NOTATION.md`; `docs/global_nonlinear.md` C.4.7.8, C.4.7.9 and C.4.7.10 completely, including D.1–D.5; and `docs/special_data_limits.md` III.F completely, with its adjacent referenced III.S material through the end of that part. The latter's separate multilayer cap theorem is not a premise of my conditional verdict. The long-horizon canonical-flow constructions cited inside maintained D.2 are background, not a substitute for assuming Input C in this assignment.

For implementation, I read the complete maintained `observable_compiler.py`, `observable_arithmetic.py`, `observable_fixed.py`, `observable_solver.py`, `observable_words.py` and `observable_initialization.py`, and the relevant observable API/precision/restart/resource sections of `code/README.md` (626–1114, plus its introduction and final general-d pointer). Other observable modules in the hash inventory were hashed for dependency consistency, not used as scientific evidence. I did not read the unrelated sources linked by the validation summary or rerun their reported checks.

The required `solve-math-rigorously` and `investigate-conjectures` skills were read, with the research-contract, adversarial-audit and decisive-experiments references. No external source, training experiment, parameter sweep, extra numerical test, or source modification was used. The only execution of candidate tests was the six-check run below. Report and evidence files are the only audit writes; no Git action was performed.

## Findings requiring attention

### I1 — Major for the executable all-d quantifier: recursive exponent enumeration

`cx1_closure.py:114` calls `_all_exponents(p, len(coordinates))`; the lower coordinate list has length `2d`. The imported helper in `code/pde/observable_initialization.py:74–84` calls `_exponents(total-first, dimension-1)` recursively until dimension is one. Consequently even the degree-zero tuple requires approximately `2d` Python generator frames. For example, dimension 600/order 1 has lower and upper core counts 1201 and 601, below the candidate's default 4096 feature allowance, but its lower enumerator needs approximately 1200 frames. Under an ordinary recursion limit of 1000 this raises `RecursionError` before the declared compiler resource checks matter. Increasing the exposed feature/source/work/byte allowances does not change this depth.

This is a static source argument, not an unreported additional run. The exact threshold depends on the calling stack and interpreter recursion setting. It defeats the candidate's unqualified implementation statement in §6 that the supplied code implements all fixed `d`; it does not affect mathematical enumeration or any of the tested dimensions 1, 2, 3, 7. An iterative weak-composition enumerator preserving total degree then descending lexicographic order repairs the mechanism without changing the mathematical dictionary. Verify its equality to the maintained enumeration on small dimensions and its operation beyond the recursion threshold before accepting the repaired artifact.

### I2 — Minor: exponent-tuple work is understated

Proof lines 609–610 state `O(d times feature count)` work for exponent tuples. The current helper constructs `(first,) + rest` at every recursive level, copying the whole suffix each time. With `r=2d` coordinates, its degree-zero generator takes `Theta(r^2)` tuple-entry copies. For degree one, `T_1(r)=T_1(r-1)+T_0(r-1)+Theta(r^2)`, hence `Theta(r^3)`, while `d times feature count` is `Theta(d^2)` at order one. The displayed bound for the number of **Word objects** need not be false; the accompanying enumeration-work assertion is.

This is not a counterexample to the overall conservative initializer order, whose dense normalization already contains a cubic feature term. It is nevertheless a mismatch in the separately advertised syntax accounting. An iterative enumerator emitting each length-r tuple with `O(r)` work also resolves this objection.

### I3 — Minor clarification: finite-precision observation weights

Returned population weights, for example three copies of the rounded value of `1/3`, need not sum exactly to one. Literal finite-precision `observe`/paired arrays therefore require normalized weights when interpreted as probability laws in W2. The maintained C.4.7.10.C.1 and D.4 state this convention and distinguish it from the unnormalized operational weights and RMS. The candidate's precision-first limit makes this harmless mathematically, but §6 should explicitly carry that convention forward. Do not renormalize the dynamics as an implicit repair: the existing literal-weight arithmetic already converges in the prescribed first limit.

## Conditional theorem checks

**Initialization and dimension adaptation.** The full union includes all dictionary dependencies and terminal forward/reverse actions. The study compiler changes lower Gaussian seed validation, values and the source offset from two to d; it preserves the maintained frozen named-source reverse traversal. At an action node that traversal records the direct named-source derivative and differentiates earlier response operands with fixed coefficients. It correctly does not differentiate the opposite-population graph input or covariance factor. The covariance extension uses the uncentered empirical operand Gram plus positive epsilon on its diagonal, retaining rather than deleting unresolved positive directions. Source groups remain distinct from action answers. The all-order generic compiler avoids applying the core-only contraction identity to later non-core source words. Inverse-lower normalization and `D=L2 @ C @ L1.T` match (8), where the code variables L1,L2 are inverse Cholesky factors.

**Dense and genuinely enriched dictionaries.** The adjusted natural code has strictly earlier dependencies and exhausts rational typed trees. Trees cover unfolded finite DAGs. All bounded prefix outputs are retained, including duplicates, and later lists contain earlier raw functions even when positions differ. Rational-mark approximation and the bounded Fourier-cylinder argument give density in the initialized observable spaces; no claim that the polynomial core alone generates them is needed. Positive densities of `(h,k)` and H prove the core polynomial dimension counts. The orthogonal odd-polynomial/artanh interpolation argument establishes a nonzero new upper action contraction at order 1 to 3; it is stronger than a changed array shape. The regularized filter estimate (10) survives duplicate/singular raw Grams and yields strong convergence of both action orientations on those observable spaces.

**H1 sufficiency.** The joint laws, rather than separate marginals, produce the unital L2 isometries and preserve all bounded coordinate operations. Word actions and actual adjunction make the generated spaces a reducing pair. Invariance is justified by Euler approximation against the supplied target, using bounded Euler speeds and a cutoff only on the target query. The logarithmic cutoff produces the Osgood modulus on every supplied finite horizon; no unjustified globally Lipschitz L2 vector field is used. Transporting the reached continuation gives existence on a matching realization, and the same one-reference comparison gives uniqueness there. Any competing strong continuation from bounded readout has a bounded readout on a compact interval by its readout equation and its bounded raw norm. The statement is correctly limited to reached, realizable complete hierarchies and the remaining supplied horizon.

**H2 and the omitted-error estimate.** The fixed-order Banach state is bounded `w-g,c` and a finite M. Bounded features give local Lipschitzness; the negative gradient identity uses weighted population L2 metrics and the coefficient Frobenius metric, with exactly the displayed factor two. Its integrated bounds prevent fixed-order finite-time escape. In the common-carrier comparison, only the learned increment is compared in HS norm; the initial operator difference is controlled strongly on compact target images. Compactness of the h1/delta2 images, the HS derivative curve, and the reducing-space property establish epsilon_N tending to zero. This supplies error production independently of the tail-based propagation estimate. Equation (18)'s two-sided filtering matches the actual M equation. The lower-gate split needs only the target's training-averaged tails, and exponential tails suffice via (19) and Osgood; fixed-cutoff Gronwall alone would not give that long-horizon conclusion.

**Observations and transposes.** Uniform action bounds and strong convergence on compact target curves propagate every separately fixed graph, including repeated action orientations. Bounded-node envelopes justify products; the multiplier lemma handles a named L2 field with a bounded continuous gate. The shared-carrier coupling gives joint W2 convergence, and Cauchy–Schwarz gives quadratic contractions. Frozen/current pairing is retained. On the exact finite weighted spaces, `apply_action` and runtime backpropagation use the same M and M transpose, so weighted adjunction is exact algebraically. Floating/fixed-point contractions have arithmetic error, covered by the precision limit and the numerical tolerance checks; no independently estimated reverse matrix is substituted.

**Numerical limits.** The order is precision b, time J, finite-data representation s when needed, population replay P, coefficient quadrature Q, source regularization epsilon, and finally closure order N. Joint Halton equidistribution plus the endpoint logarithmic-tail estimate supplies every required finite Gaussian moment. At positive epsilon, finite causal induction uses Cholesky continuity and polynomial envelopes to handle adaptively computed coefficients on the same Q cloud. Frozen P replay keeps g and all correlated marks together. At singular limiting source covariances, the proof uses positive-semidefinite square-root coupling, not continuity of a singular Cholesky inverse. Fixed-N mark stability uses feature envelopes rather than an invalid empirical contraction assumption. Exact Heun stages have a common bound before any time limit, and precision is removed at fixed positive pivots. Rational primitive algorithms terminate and are locally uniformly consistent; compact query sets justify the whole-sphere arithmetic claim. Float64-only refinement is not asserted. Subject to I1's actual syntax-generation obstruction, this is a complete conditional iterated numerical argument, not an arbitrary diagonal or an accuracy schedule.

**Restart and cost.** The saved nine arrays, finite data and arithmetic metadata contain the complete joint state. Deserialization reconstructs exact hexadecimal float or rational-unit values and calls no initializer. The inherited simultaneous Heun stage dispatch preserves the study State subclass. Same steps/backend/reduction order therefore reproduce continuation from a step endpoint; this does not claim a new mesh from an interpolated interior state matches the old mesh. The displayed state count includes both matrices, frozen g, all feature tables, population weights and moving rows/readout. Compiler work includes response walks, covariance extensions, Q/P evaluation and dense normalizations; evolution includes validation and feature contractions, with two RHS evaluations per step. Aside from I2, I found no missing width dependence or uncounted growing training transcript. Rational elementary calls are appropriately charged for exact Fraction temporaries and precision-dependent series, rather than unit bit cost. Exact input/syntax descriptions and transient serialization must remain additional to the rounded numerical state counts; no useful uniform cost in the outer limits is proved.

## Authorized independent execution

Run once from `/home/amir/Codes/PDE`:

```sh
env CX1_CLOSURE_CHECK_OUTPUT=data/generated/cx1_many_point_closure_20260919/implementation_audit_01 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout 120s prlimit --as=536870912 --cpu=120 -- python -B studies/cx1_many_point_closure_20260919/test_cx1_closure.py
```

All six tests passed, with zero failures/errors, exit status zero and recorded test time 15.024936228990555 seconds. The process had a 512-MiB address-space limit and 120-second wall/CPU limits. No budget enlargement or retry occurred. Fresh results and the two own-state restart files are under `data/generated/cx1_many_point_closure_20260919/implementation_audit_01/`.

The checks cover dictionary dimensions/enrichment counts, d=2 agreement with the maintained compiler, seventh-seed source responses, weighted adjunction and independent finite-difference loss gradients, joint observations, exact own-state continuation and rational/float agreement. The only trajectory steps are the predeclared tiny supplied-state restart checks. They do not test high-dimensional enumeration, arbitrary high orders, continuum suprema, closure accuracy, learning, or convergence rates. Operational training results described in the supplied validation summary were not rerun and are not independent audit evidence.

## Version checks and limitations

Proof, module and tests matched the assigned hashes before reading/execution and again after the run. The maintained dependency inventory was unchanged. During the audit the supervisor updated only `VALIDATION.md` to add its standalone-import record; I reread that updated allowed file. Both observed hashes are recorded below. That added claim was not independently reproduced here and changes none of this verdict. This report judges the original frozen proof/module/test versions only; any repair needs its own fresh verification.

Input C, target loss/activity/radius claims and raw neural GD step conditions remain outside the verdict. No proof that a chosen numerical resolution inherits target margins is supplied by the six tests. There is no promotion or established-library recommendation in this isolated report.

Full hash inventory and the final change check follow.

### Repository files (final audit observation)

```json
{
  "studies/cx1_many_point_closure_20260919/CX1_CLOSURE_PROOF.md": "74be7dae60f7771123158f51c9e913b3f4b664a87754735c38fa406d514a26ae",
  "studies/cx1_many_point_closure_20260919/cx1_closure.py": "a4f31a3ae2a5fe1346f6c465d1c5b4b1ecce7c0db67974056cb58a6ffec78612",
  "studies/cx1_many_point_closure_20260919/test_cx1_closure.py": "f4fd69bb965ce6147c088a228d74c6da9f4b92021dd312667e66d874ed17a735",
  "studies/cx1_many_point_closure_20260919/VALIDATION_PLAN.md": "1d6707d0d3e857b75a87d1946fabd29e4c382afebe9fd2513a4e952b961a36ed",
  "studies/cx1_many_point_closure_20260919/validate_trajectories.py": "98451f08f31e433707b80bd4ba3cfd078abd43e0ba36423e1a33cd1eb7181097",
  "studies/cx1_many_point_closure_20260919/VALIDATION.md": "173bdfb514df7014645dcee96e6cb690541ee54a41b62b690af4d54150e4726c",
  "studies/cx1_many_point_closure_20260919/DEPENDENCY_HASHES.json": "43d670289ddd492d82e1b7fa6db81424eeac72887ff08e8a42722bdff081525b",
  "docs/NOTATION.md": "199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b",
  "code/README.md": "7aa3bc9700a75294f9f209a34e05af4033cd35dd5edb736846ff8bdfdc4bdbb6",
  "docs/global_nonlinear.md": "81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c",
  "docs/special_data_limits.md": "5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489",
  "code/pde/observable_arithmetic.py": "2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb",
  "code/pde/observable_closure.py": "f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137",
  "code/pde/observable_compiler.py": "1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac",
  "code/pde/observable_fixed.py": "75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225",
  "code/pde/observable_initialization.py": "6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2",
  "code/pde/observable_laws.py": "6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503",
  "code/pde/observable_p1_initialization.py": "65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d",
  "code/pde/observable_solver.py": "711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605",
  "code/pde/observable_torch_circle.py": "4fa63eb6abdd1c8573abfa1a7dc0a107d13ec669ae078659e8298cd517000430",
  "code/pde/observable_torch_p1.py": "d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f",
  "code/pde/observable_words.py": "b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5"
}
```

The extra maintained observable modules in this inventory were metadata-hashed only, as distinguished in the scope section.

### Allowed validation-summary change

```json
{
  "studies/cx1_many_point_closure_20260919/VALIDATION.md": {
    "before": "cafcf003e8d42df801f5ecdd3801ac61d7d1a0bec3b69df57bd9025db667e0c3",
    "after": "173bdfb514df7014645dcee96e6cb690541ee54a41b62b690af4d54150e4726c"
  }
}
```

### Required process inputs

```json
{
  "/etc/codex/skills/solve-math-rigorously/SKILL.md": "9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7",
  "/etc/codex/skills/investigate-conjectures/SKILL.md": "a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de",
  "/etc/codex/skills/investigate-conjectures/references/research-contract.md": "7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e",
  "/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md": "8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501",
  "/etc/codex/skills/investigate-conjectures/references/decisive-experiments.md": "6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9"
}
```

### Fresh test outputs

```json
{
  "data/generated/cx1_many_point_closure_20260919/implementation_audit_01/rational_restart.json": "bea4871281e7eb39c312d13bc03cb09608db353616caa9e1a3c46408441e3d91",
  "data/generated/cx1_many_point_closure_20260919/implementation_audit_01/restart.json": "88fbc08ce77354e2c8560a970d19345bc8116cbbe5b87221f9485c19478d4c9c",
  "data/generated/cx1_many_point_closure_20260919/implementation_audit_01/results.json": "8ca8a9b490c298beb488bfa25e2557e6e14ddd3f7a675c9677125d78f87a2171"
}
```
