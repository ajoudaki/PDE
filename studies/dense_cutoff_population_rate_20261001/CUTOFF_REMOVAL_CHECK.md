# Internal reconstruction of cutoff removal

Checker: root/coordinator, 2026-10-01. This is an internal mathematical check, not an isolated promotion review. The coordinator suggested the independent comparison threshold and is therefore a contributor to that extension. No formal proof assistant or training experiment was used.

Candidate read completely: `CUTOFF_REMOVAL_ROUTE.md`, final SHA-256 `78ab82a56f3adb18f4462b4f59b6328f072d04bcdff85fe6cf48d089f873d300`. One presentation correction made during checking specifies a **countable dense** smooth coordinate family in the common-space construction; closure under every smooth function would not remain countable.

The complete current manuscript and all included mathematical files and captions were read during this investigation. Relevant mathematical dependencies were reconstructed against `paper/proof_alltime.tex` (SHA-256 `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d`) and `paper/proof_tracking.tex` (SHA-256 `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be`). The Gaussian operator construction and its marginal carrier-tail theorem are supplied manuscript inputs. This check is not a fresh independent promotion audit of those source theorems.

## Reconstruction and attacks

1. **The auxiliary equation is a different training rule.** Direct differentiation of the unchanged output gives the matrix pairing a true backward gradient at evaluated sample \(a\) with a clipped update response at driving sample \(b\). The factors \(1/m\), \(1/n\), and the first-layer input pairing are correct. The hidden contribution is neither assumed symmetric nor assumed nonnegative.

2. **Fitting does not depend on the cap.** On the activity tube, the unchanged zero-initialized readout is \(O(S)\) in RMS. Both backward recursions are then \(O(S)\), since clipping contracts magnitude. Hidden displacements and feature-Gram changes are \(O(S^2)\); the mixed hidden residual matrix is also \(O(S^2)\). Thus its symmetric part remains positive for small \(S\). Choosing the activity stop proportional to fixed label RMS excludes the stop by exponential residual decay. No coordinate maximum or factor \(M\) appears in this argument. It remains valid for \(M\downarrow0\).

3. **Population existence is not assumed from formal substitution.** At each fixed positive cap the bounded clipped carrier makes the backward recursion locally Lipschitz in the specified \(L^2\)/Hilbert--Schmidt parameter norm. Bounds are uniform on bounded state sets at that cap. The finite-activity a priori estimates therefore give continuation in the complete state space. The chain rule along differentiable \(L^2\) curves is justified by a fixed-direction dominated-convergence argument; Fréchet differentiability of the whole Nemytskii map is unnecessary.

4. **The two population paths use one action and its true adjoint.** Finite unions of Gaussian programs, the countable coordinate family, and completion preserve adjunction. The clipped solution stays in the enlarged generated space. No independent backward Gaussian map is introduced. Fixed-cap identification uses qualitative fixed-program convergence before mesh refinement, which is adequate for existence/identification but does not imply any width rate.

5. **The two thresholds have different roles.** In the changed-gate term, \(|\chi_M(P_D)|\le|P_D|\) permits a split at independent threshold \(R\). The omitted clip is bounded at the algorithmic threshold \(M\). This gives one factor \(1+R\) plus the two reference tails at every backward layer. Propagating through a fixed number of bounded operators adds constants without multiplying successive cutoff factors.

6. **Infinite time is paid for with residual activity.** The exact residual difference equation damps by the symmetric part of the clipped residual matrix. Its source and the parameter source both carry the *dense* residual. After integrating the residual difference, Gronwall has coefficient \(C(1+R)\rho_D(t)\), whose total mass is \(O((1+R)Y)\). No ratio of residuals, unweighted infinite-time tail integral, or exponential in physical training time is used.

7. **Gaussian cutoff removal uses only marginal tails.** The supplied population exponential moment yields a uniform deterministic \(L^2\) tail at each time. Multiplying by residual and integrating preserves that Gaussian decay. Taking \(R=M\) absorbs the linear exponential amplification into \(e^{-cM^2}\). The parameter estimate holds for all time and therefore controls the convergent fitted endpoint.

8. **The query metric is the requested one.** Forward subtraction at a passive query costs \(C(1+\|x\|/\sqrt d)\) times parameter distance. The time supremum is taken before the \(L^2(\mu)\) integral; finite second input moment is sufficient. No discretization of the test law or interchange of supremum and integral is used.

9. **Growing finite caps are only qualitative without a finite tail rate.** In the two-threshold bound, hold \(R\) fixed and let \(n\to\infty\) with any \(M_n\to\infty\). The manuscript's uniform qualitative tail remainder vanishes at that fixed \(R\). Then let \(R\to\infty\). This proves qualitative removal for every diverging cap, but supplies no numerical width rate. The final limitation is stated correctly.

## Verdict

PASS for the stated cap-uniform fitting, population wellposedness/identification, all-time Gaussian population cutoff removal, deterministic two-threshold comparison, and qualitative finite removal. Constants can depend on fixed depth, inputs, activation bounds, Gram margin, and the fixed admissible label threshold, but not on width, cap, or training time where uniformity is claimed.

The strict dense finite-to-population root-width theorem remains open. This proof does not settle its bias or fluctuations, and it does not assert a slower-than-root lower bound.
