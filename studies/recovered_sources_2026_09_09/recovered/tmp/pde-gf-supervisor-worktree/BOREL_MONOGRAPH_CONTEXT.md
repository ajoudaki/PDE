# Borel question: complete older-monograph context

Read on 2026-09-05 by the independent monograph-context agent.

## Reading coverage and source status

Read `/etc/codex/skills/teach-technical-math/SKILL.md`, then the complete 7,477-line, 44,391-word `/home/amir/Codes/PDE/FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md`, including Chapters 1–9 and Appendices A–D. Reads were in sequential manageable chunks; truncated spans were revisited. No cited external source or underlying historical report was independently opened in this subtask. Thus claims below describe and reason from this monograph, rather than claiming a fresh verification of every source it cites.

The monograph is the dated 31 July baseline, explicitly superseded within later study scopes by the August material (lines 5–15). Its mathematical claim statuses remain those of the July 28 audit; July 31 added navigation/reproduction information, not new mathematical results. The root is reading the later August 21 top-level document, which contains the actual positive Borel conjecture. This older monograph contains exactly one occurrence of “Borel.”

## The one Borel passage

Section 5.7.6, lines 3362–3368, is titled “Complete jets do not identify a real-axis trajectory.” It states that adding `exp(-1/tau^2) 1_{tau>0}` changes a smooth positive-time trajectory without changing any derivative at zero. Padé or Borel resummation selects a continuation unless quasianalyticity, summability, or an independent real-axis well-posedness theorem **identifies it with the network**. This is a non-identification warning, not a theorem that resummation always fails.

Interpretation for the present question: unique population GF existence supplies the target and a means of identification, but it does not alone identify an arbitrarily reconstructed series. Either the positive hypothesis must expressly say that the actual population observable is the Borel sum of its initialization jet, or the reconstruction must be shown to satisfy the same integral/evolution equation and initial data in the uniqueness class. Convergence and correct formal jets alone are insufficient.

A concrete mathematical illustration (our reasoning, not from the monograph): let `g(y)=exp(-1/y^2)` for y>0 and zero for y<=0. The globally smooth, bounded-derivative vector field `y'=1+g(y)`, `y(0)=0`, has a unique solution. Every initialization derivative beyond the first is zero, so its formal Taylor series is `t`, an entire and Borel-summable series. Nevertheless, its actual solution satisfies y(t)>t for every t>0. Uniqueness cannot be applied to `t`, because its evolution defect is the nonzero flat function `-g(t)`.

## Scope safeguards that survive all later population existence results

1. **Scalar observables versus representations.** The declared central target is outputs AND hidden Grams, not loss alone (lines 90–180, 652–664, 3936–3955, 6780–6803). A kernel reconstruction determines output dynamics under the fixed loss but does not reconstruct all hidden laws, operators, or Grams. Distinct hidden realizations can produce the same output curve.
2. **Canonical-start versus restart state.** Autonomy and internal restartability of an emitted surrogate are distinct from physically faithful positive-time dense restarts. The latter needs a state map and continuation estimate (lines 650–681, 4807–4833, 6883–6885, 6901–6918, 7153–7161). A Borel reconstruction from initialization coefficients by itself addresses a specified original trajectory, not changed-label, changed-data, or arbitrary state continuations.
3. **Initialization provenance.** Admissibility clauses at lines 668–681 require architecture-local initialization/drift/readouts, a predeclared approximation schedule, no positive-time trajectory oracle, and a finite-description regular compiler. A finite description cannot hide an unbounded bit string. The exact-curve Bernstein construction at lines 2223–2268 is inadmissible because its coefficients sample the unknown positive-time target.
4. **Finite syntax versus finite information.** Finitely many fields over a fixed finite-dimensional source domain need not mean finitely many scalar degrees of freedom (lines 157–180, 675–694, 4760–4777, 7154–7161). Initialization-jet convergence may give a sequence of finite approximants without any exact finite closure or width-independent computational-cost guarantee.
5. **Uniform time versus uniform model class.** The uniform-in-time supremum is explicit throughout (e.g. lines 707–743). Uniformity in model parameters/data is another quantifier; it requires common estimates and moduli (lines 6447–6455, 6551). A horizon independent of width is not automatically uniform over all activation/data choices.
6. **Compact-time versus all-time.** Compact-time approximation does not imply all-finite-horizons or all-time approximation (lines 861–890, 6625–6664). Small kernel error plus positive semidefiniteness can accumulate to an O(1) late-time error in an arbitrarily slow direction (lines 6630–6651). A new fixed T*>0 does not remove this distinction.
7. **Approximation axes.** Training-time jets, source Hermite degree, chronological response grade, nonlinear tree grade, and numerical depth resolution are distinct (lines 1661–1705, 6288–6309, 7109). Borel convergence of time-jet coefficients is not source-Hermite convergence.
8. **GF regularity versus jet regularity.** This is an additional inference for the new theorem: C^{1,1} activations/losses sufficient for local GF do not guarantee arbitrarily many initialization derivatives. Borel statements therefore need a stronger activation/loss/observable class and all-order differentiability/jet-limit hypotheses. The analytic arctan case is eligible for investigation; eligibility is not a summability proof.

## Older negative result and non-transfer

Chapter 5 uses one sample, two fully trained hidden layers with quadratic activation, order-one Gaussian stored readout, and feature time tau for readout ascent. It does not concern the current bounded-derivative arctan setting. The fixed-order limit hypothesis (FW), lines 2860–2878, is order-by-order L1 convergence of finite-width initialization coefficients to deterministic leading Wick contractions. It is logically distinct from a positive-time limit, and the July document leaves it conditional.

Under (FW), the Taylor coefficients have a factorial lower bound along odd orders, lines 3070–3093. Thus ordinary Taylor partial sums diverge for every positive feature time; the ensuing finite residual-clock compilers develop an initial boundary layer, lines 3101–3178. The result is about the specified compiler and order of limits. It does not rule out signed/Borel/nonpolynomial real-axis reconstruction, bounded activations, or every finite PDE (lines 3224–3237, 3274–3284, 3356–3368, 3924–3929, 7197–7201). It must not be imported as a divergence conclusion for our arctan GF.

The useful positive relic is the clock-shadowing theorem, lines 2592–2651: a small feature-profile error propagates to a uniform-in-physical-time output/loss error under common initial clocks, target-reaching monotonicity and upper/lower derivative bounds. It does not manufacture the small defect, and the scalar feature clock does not automatically apply to a general fixed multi-input dataset.

## A conditional implication useful for the present fixed-data GF

This is a derived consequence, not a theorem claimed by the July monograph. Use the current weighted squared loss with positive diagonal Omega=diag(omega_a), sum omega_a=1. If K(t) is the unweighted metric kernel and r=f-y, then r'=-2 K(t) Omega r. Define e=Omega^(1/2) r and A(t)=Omega^(1/2) K(t) Omega^(1/2), so e'=-2 A(t)e and A(t) is positive semidefinite.

Suppose initialization-derived Borel approximants reconstruct kernels A_M(t) with `rho_M=sup_{0<=t<=T0} ||A_M(t)-A(t)||_op -> 0`, on a fixed T0 in (0,T*], and integrate e_M'=-2 A_M(t)e_M from the same e(0). Variation of constants using the contractive propagator of the exact PSD A, followed by Gronwall, gives

`sup_{t<=T0} ||e_M(t)-e(t)||_2 <= 2 T0 rho_M exp(2 T0 rho_M) ||e(0)||_2`.

Indeed, the approximate norm is at most exp(2 rho_M t)||e(0)||, since the symmetric part of A_M is bounded below by -rho_M I; insert this into Duhamel to obtain `(exp(2rho_M T0)-1)||e(0)||`, bounded by the display. Symmetry of the approximant is not needed for this norm bound. Weighted loss is ||e||², so its uniform error also tends to zero. The established finite-width/GD-to-population convergence then combines by the triangle inequality with M->infinity after width, yielding finite-network output/loss approximation on the same interval.

This conditional conclusion is restricted to what the Borel hypothesis reconstructs. To conclude hidden-Gram or full-state approximation, those fields need their own identified reconstruction or a compatible complete-state residual estimate. To cover every t<T*, the Borel hypothesis must hold on [0,T*] or each compact [0,T] with T<T*. If it holds only on one smaller fixed [0,T_B], its direct conclusion stops at T_B. An interval shrinking to zero does not cover any fixed positive t in the limit.
