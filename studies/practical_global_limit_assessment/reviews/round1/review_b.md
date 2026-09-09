# Independent adversarial audit B

**Verdict: one minor required correction; otherwise PASS as a strategic research assessment.**

I read `/home/amir/Codes/PDE/studies/mean_field_peeling/practical_global_limit_assessment/ASSESSMENT.md` in full. I used no other files, sources, skills, agents, or chat history as mathematical input. The cited earlier results and literature descriptions are attributed premises here; this audit does not independently certify them.

## Required correction

**Line 36: state the amplitude restriction used by the denominator estimate.** The implication

`E phi(Z)^2 >= (a-e)^2 sigma^2`

from Gaussian projection is valid with the normalized bounds `||psi||_infinity <= 1`, `||psi'||_infinity <= 1` when `0 <= e <= a`. The subsequent direct estimate by `4e^2/a^2` uses `e <= a/2`. The text states only `a >= 2`; it should explicitly carry forward the intended restriction `0 <= e <= 1` from the construction being discussed, and spell out these two normalized bounds if they are not otherwise part of the report's convention.

A minimal replacement is: “For the normalized shape bounds `||psi||_infinity, ||psi'||_infinity <= 1`, with `0 <= e <= 1`, `a >= 2`, and centered Gaussian `Z` of standard deviation `sigma >= 1`, ...”. The displayed claims then follow as written.

This is a genuine missing hypothesis for the denominator claim, even though the intended gain construction uses `e=1`. For example, with `psi(z)=-sin(z)`, `a=2`, `e=10`, and standard Gaussian `Z`, the denominator equals

`8 + 50(1-exp(-2)) - 40 exp(-1/2)`,

approximately `26.972`, whereas `(a-e)^2=64`. This correction does not change the practical conclusion about the large-gain construction. The final relative-fraction bound can also be extended to larger `e/a` by using the trivial bound of one, but that does not validate the intermediate denominator estimate without a restriction.

## Findings that pass

- **Scope and compact training time:** Lines 7–11 request one fixed activation and one autonomous global population flow, valid on every finite training interval. They allow constants depending on the interval while explicitly rejecting a time-dependent activation cutoff. They do not demand exponential fitting, a perpetual kernel floor, or a finite residual clock. This is the appropriate distinction between global existence via compact intervals and uniform control for all training times. The text expressly leaves the trained conjectures open.
- **Architecture and metric:** The fixed-depth route retains the original initialization, raw metric, trained blocks, and observables. The residual route and the variance-calibrated dense Gaussian route are identified as new models/classes. The `1/L` residual branch derivative and `O(1/L)` total branch kernel under the stated unaveraged metric are correct; the resulting need to specify training normalization is made explicit. No residual theorem is silently transferred to dense Gaussian training.
- **Practicality:** The gain formula has asymptotic order `delta^(-2)` for fixed positive shape constant: its two terms scale respectively as `delta^(-2)` and `delta^(-8/5)`. The two reported numerical upper bounds on `e/a` are correct. The assessment correctly distinguishes absolute nonaffinity from relative nonlinear contribution and from function-level evidence. Three distinct points on a sphere are affinely independent, because a line intersects a sphere in at most two points.
- **Energy and finite width:** The dissipation and displacement inequalities follow from the raw-metric gradient-flow identity and Cauchy–Schwarz. In a finite-dimensional smooth system with fixed positive definite metric, these bounds prevent finite-time escape and yield continuation. They do not supply strong compactness or local Lipschitz regularity in the population space; the text correctly says so. The initial-loss limit is an attributed model premise rather than something checked from the assessment alone.
- **Proposed tail/energy route:** Sub-Gaussian cap errors dominate the stated `exp(C R)` comparison factor for each fixed `T,M`. Conditional on that comparison and on converting the incoming-field tails into a gradient error, the proposed route is coherent. If `||G-G_R|| <= epsilon_R(T,M)` on the stopped trajectory, Young's inequality gives `dE/dt <= -(1/2)||G_R||^2 + (1/2)epsilon_R^2`. Consequently the squared displacement is bounded by `T(2E(0)+T epsilon_R^2)`. Choosing `M > sqrt(2T E(0))` first, then taking the cap sufficiently large at this fixed `M`, removes the stop. The dependence of tail constants on `M` therefore does not itself create circularity. The report appropriately leaves the tail lemma, applicability of comparison estimates, and finite-width/observation bridges to future proof; it does not establish them by the energy identity alone.
- **Bounded-control counterexample:** `w=A=sec(s)`, `C=tan(s)` exactly solves all three displayed ascent equations and blows up at `pi/2`. It demonstrates why a bounded external ascent control cannot replace physical squared-loss feedback.
- **Residual forward example:** The transformation `u=sinh(h)` gives `u'=beta u`, hence the displayed solution. Its derivative equals `exp(beta)` at zero and tends to one at infinity. Euler convergence follows from boundedness and global Lipschitz continuity of `tanh`. The stated limitation to forward composition is correct.
- **Gaussian `1/L` calculation:** Gaussian integration by parts gives the cross term and cancellation in normalized covariance exactly, including degenerate covariance matrices. For nonnegative `beta`, and the stated regime `e=beta/L <= 1/2`, the variance and accumulated correlation-error bounds follow with the displayed constants. The affine-offset example also follows exactly from the covariance recursion. These conclusions concern initialized normalized geometry and do not settle trained behavior.
- **Calibrated `1/sqrt(L)` calculation:** Orthogonality of `r` to `G`, positivity of `v`, exact variance preservation, and the correlation recursion all hold. Bounded `r'` gives the claimed Lipschitz bound by covariance differentiation, with continuity at the endpoints from Gaussian integrability. The local error is uniformly `O(L^(-2))`, so the Euler limit follows. Oddness, `R'(0)=0`, and `R(1)=v>0` prove that `R`, and hence the generator for nonzero `beta`, is nonaffine. The report explicitly notes that `r` is unbounded in value and that these are initialization facts, not trained-limit theorems.

## Nonblocking precision improvement

Because line 137 distinguishes pointwise probability statements from a supremum event, line 9 could say explicitly that the desired finite-width identification is uniform over `t in [0,T]` in the specified observable topology and probabilistic mode. “On every finite training interval” already reasonably communicates this pathwise compact-time intent in a strategic assessment, so I do not treat this as a defect requiring revision.

No other required mathematical or scope correction was found under the stated attributed-premise boundary.
