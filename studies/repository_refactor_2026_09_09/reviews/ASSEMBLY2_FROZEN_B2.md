**CLEAN — no required corrections found within the packet’s stated mathematical and implementation scopes.**

I conducted this review independently, without delegation. I read every line of every file listed in `INPUTS.json`, checked the dependencies used by Sections 8–9, ran the prescribed tests and guide example, and performed additional deterministic algebra and derivative checks. All packet hashes matched before and after. No packet input was changed.

**Read inventory and integrity verification.** The root was `/tmp/pde_assembly2_frozen_r2`. The following SHA-256 values were independently computed both before and after the review; each matched the manifest at both checks. Line coverage includes blank lines.

| Input | Lines read | Bytes | SHA-256, identical before and after |
|---|---:|---:|---|
| [docs/NOTATION.md](/tmp/pde_assembly2_frozen_r2/docs/NOTATION.md) | 1–98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| [code/pde/__init__.py](/tmp/pde_assembly2_frozen_r2/code/pde/__init__.py) | 1–26 | 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| [code/pde/finite_network.py](/tmp/pde_assembly2_frozen_r2/code/pde/finite_network.py) | 1–363 | 15,525 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| [code/pde/gaussian_moments.py](/tmp/pde_assembly2_frozen_r2/code/pde/gaussian_moments.py) | 1–114 | 4,464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| [code/pde/finite_reductions.py](/tmp/pde_assembly2_frozen_r2/code/pde/finite_reductions.py) | 1–346 | 15,571 | `391dc35773a35d86f889cebda9f95820d793a656f2fb05f9b01bb7453be20a4c` |
| [code/tests/test_finite_reductions.py](/tmp/pde_assembly2_frozen_r2/code/tests/test_finite_reductions.py) | 1–340 | 18,563 | `7b1a4023334956a25afd4217de7a311145b64c240fc78b87f84b16d2af7dedb0` |
| [requirements.txt](/tmp/pde_assembly2_frozen_r2/requirements.txt) | 1–2 | 111 | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |
| [docs/finite_dynamics.md](/tmp/pde_assembly2_frozen_r2/docs/finite_dynamics.md) | 1–1275 | 48,489 | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| [code/README.md](/tmp/pde_assembly2_frozen_r2/code/README.md) | 1–42 | 2,363 | `9480d7300646f1fff81501954b767f86bca606dcadc7cdb2fe27ba0d08baad77` |

Total listed inputs: **9 files, 110,807 bytes, 2,606 lines**.

I also read the complete manifest, 47 lines and 1,388 bytes. Its independently computed before/after SHA-256 was:

```text
cd32b32a8caf6d6ade39109a679ac4941b9a8f26acd09642f7261d812d29f3f7
```

I personally read these complete methodological files:

- [/etc/codex/skills/solve-math-rigorously/SKILL.md](/etc/codex/skills/solve-math-rigorously/SKILL.md)
- [/etc/codex/skills/investigate-conjectures/SKILL.md](/etc/codex/skills/investigate-conjectures/SKILL.md)
- [research-contract.md](/etc/codex/skills/investigate-conjectures/references/research-contract.md)
- [evidence-ledger.md](/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md)
- [adversarial-audit.md](/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md)

No other checkout, study, packet, previous verdict, task history, or external mathematical/code source was consulted. Diagnostics ran inline. Execution used the prescribed Python/NumPy dependencies.

**Conventions and finite dependencies.** The notation, chapter, and implementation consistently distinguish:

- Stored middle matrices acting without another width factor.
- Output normalization by \(1/n\), first-input normalization by \(1/\sqrt d\), and residual \(r=f-y\).
- Backpropagated \(\delta=n\,\partial f/\partial z\), without a residual.
- Endpoint mobilities \(n\kappa_1,n\kappa_{L+1}\) and middle mobilities \(\kappa_\ell\).
- Full mean-square loss in the core and Sections 1–7 versus half-square loss in Sections 8–9 and the frozen APIs.
- Small stored-readout initialization in `initialize` versus the separately stipulated order-one initialization in Sections 8–9.
- Simultaneous raw updates, raw-parameter interpolation, and separately discussed interpolation of grid observables.

Sections 1–4 correctly derive the raw gradients, positive-semidefinite kernel blocks, output equation, and weighted energy identity. The global finite-width continuation proof is valid: energy bounds the squared metric speed, Cauchy–Schwarz gives a square-root time modulus, and a finite maximal endpoint therefore has a finite parameter limit from which local existence extends the solution. This requires neither bounded activations nor a discrete energy inequality.

The width-independent bounds have their stated additional hypotheses: fixed depth and data, bounded activation derivatives, bounded initial normalized parameter norms, and bounded initial loss. The forward/backward inductions and Gaussian net bound are valid. These estimates alone do not control unbounded population multiplication operators or identify a population trajectory.

Sections 5–7 and their implementation also check out:

- The QI/IQ/QQ gradients and kernel factors agree with metric (8).
- Both Lax identities have the correct isometric \(1/\sqrt n\) scalar blocks and IQ factor two.
- The similarity argument establishes isospectrality without self-adjointness.
- The orientation witness has equal output and spectrum but kernels \(68/9\) and \(28/3\); its conclusion concerns insufficiency of the proposed spectrum-based state.
- The QQ row and column balances have the stated factors.
- RMS differentiation includes both normalization denominators. The matrices \(\Pi_h,\Pi_v\) are positive definite for positive \(\varepsilon\), generally not projections.
- The RMS field derivatives, contraction (29), signed balance drifts, and reduced operator \(\mathcal A_h\) are correct.
- Restartability is justified on reached raw-image states. The argument does not assert existence at \(\rho_h=1\), global feature-ascent existence, or a width-independent scalar closure.

The core routines correctly implement these interfaces, including actual transposes, mixed activations, arbitrary supplied sample geometry, and simultaneous updates. `gaussian_moments.py` correctly validates rational symmetric PSD covariance, including singular zero pivots, before evaluating its multiplicity-weighted Wick recurrence. Package imports and the guide’s module-level API imports resolve consistently.

**Section 8.1: exact frozen reduction and joint initial layer.** The raw differentiation gives, with \(c=1/\sqrt3\),

\[
\dot a=-rcz^2,\qquad
\dot z=-2cQr(a\odot z),
\]

and the two trained-block kernels are

\[
K_W=\frac{4c^2Q}{n}\sum_i a_i^2z_i^2,\qquad
K_a=\frac{c^2}{n}\sum_i z_i^4.
\]

Consequently \(\dot f=-r(K_W+K_a)\) and
\(\dot\ell=-r^2(K_W+K_a)\), with no extra factor two.

The reduction is exactly realizable. For a fixed \(h\) with \(Q>0\),

\[
W=\frac{zh^T}{nQ}+W_\perp,\qquad W_\perp h=0,
\]

realizes every \(z\). The invisible component does not affect the reduced update. For \(Q=0\), necessarily \(h=0\) and \(z=0\). Because \(h\) is fixed, raw interpolation makes \(a,z\) affine within each cell; recomputing the output then agrees exactly with the reduced-coordinate interpretation.

The probabilistic proof closes under its stated initialization and quantifiers:

1. Conditional row independence and Gaussian variances are correct. The fourth/eighth moments yield
   \[
   \operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
   \mathbb E(f_n^0)^2=\frac1n\left(1+\frac{32}{3n}\right).
   \]

2. Before a grid hit, \(s_k\) is positive and bounded as in (8.5), so each readout coordinate increases. Every currently negative row was negative at all preceding steps.

3. The negative-row estimate remains valid even when a discrete multiplier reverses the sign of \(z_i\): the bound uses its absolute value. Gaussian exponential integrability gives a uniform conditional second-moment bound, so one initialization event controls the aggregate negative contribution at every surviving grid time. No union bound over steps is required.

4. The favorable tail block has a fixed positive probability once \(T,\delta,b\) are fixed. On \(Q_n\ge1/2\), its minimum coordinate satisfies the stated scalar lower recursion.

5. The reciprocal estimate gives the claimed hitting-time bound. The important order is:
   \[
   T,\delta\ \longrightarrow\ b\ \longrightarrow\ p_b,M
   \ \longrightarrow\ n\to\infty,\ \eta_n\to0.
   \]
   Thus \(M\) can be extremely large but remains fixed before taking the joint limit. Both the row-count estimate and \(\gamma\eta_nM\le1\) eventually hold without any rate restriction between width and step.

6. The favorable contribution minus the negative bound forces \(f_n\ge2\delta\), contradicting survival. This proves \(\tau_n(\delta)\to0\) in probability.

The interpolation conclusion is also valid. Continuity forces an intermediate value \(+\delta\) or \(-\delta\) during the first crossing step, even with grid overshoot. Its half loss differs from \(1/2\) by at least \(\delta-\delta^2/2\). This contradicts uniform convergence in probability to a continuous path with the initialized trace, including a random continuous proposed limit.

This is an arbitrary **joint vanishing-step** theorem for the **permanently frozen-bottom** model. It is not a fully trained quadratic theorem, a fixed-positive-step assertion, or a discrete dissipation theorem.

**Section 8.2: deletion comparison.** The width-one counterexample is algebraically correct. The two updates have identical \(a^+,w^+\), whereas

\[
u^+/u=-1-4\varepsilon,\qquad
f_{\rm full}^+=(1+4\varepsilon)^4f_{\rm frozen}^+.
\]

The stipulated smallness conditions make \(f_{\rm frozen}^+<0\), hence the full output is strictly smaller. They can simultaneously keep the initial and both terminal outputs within \((-\delta,\delta)\).

The example works for every positive feature step with a step-dependent state. Since the initial residual is negative, it also corresponds to a positive physical half-loss step. It refutes the proposed general deletion inequality; it does not establish a typical-Gaussian obstruction or settle fully trained quadratic joint-step behavior.

**Section 9.1: reached ReLU obstruction.** The contact state and all normal-velocity calculations are correct. In particular,

\[
p=\frac38>0,\quad
q=\frac34(1/2-4\lambda)<0,\quad
v_0=\frac34(1/2-4\lambda\sigma/c).
\]

For each fixed finite \(\sigma\), one can choose \(\lambda>1/8\) with \(v_0\ne0\). The other gates remain strictly positive, so continuity supplies a neighborhood with uniform inward side velocities and a nonzero assigned contact velocity.

The noncontinuation argument covers absolutely continuous solutions satisfying the field almost everywhere. For \(w=|z_1^{(2)}|\), the derivative is negative on \(\{w>0\}\) and zero almost everywhere on its zero set. Integration forces \(w\equiv0\), contradicting the assigned nonzero normal velocity. Chattering does not evade this argument.

The reached-state proof supplies the necessary additional step: a sufficiently nearby open set in the positive sign cell hits the contact surface before leaving the controlled neighborhood or reaching another gate. The nondegenerate finite Gaussian law gives that open set positive probability.

The conclusion is correctly restricted to the prescribed pointwise field. It neither excludes differential-inclusion selections nor supplies a probability bound uniform in width.

**Section 9.2: positive local Euler output compactness.** The proof is valid for \(|\sigma|\le\sqrt2\), order-one readout initialization, and every deterministic \(\eta_n\to0\).

The normalized forward/backward estimates give

\[
|f_n|\le2R^3,\qquad |r_n|\le3R^3,\qquad
R^+\le R+6\eta R^5.
\]

The bootstrap constants satisfy exactly

\[
6+6T_*12^5=12,\qquad
T_*=2T_0,\qquad
T_0=\frac1{497664}>0.
\]

For sufficiently large \(n\), every endpoint needed through \(T_0\) lies within the bootstrap horizon. The initialization event has probability tending to one; the matrix-net exponent is negative:

\[
2\log 9-\frac92\approx-0.1055508453.
\]

Raw interpolation preserves the parameter norm bounds. The product-difference estimates give the claimed output Lipschitz bound across all cells. Together with bounded output magnitude, this produces a deterministic compact set of output paths on the high-probability event. The argument separately handles finitely many earlier widths, so it proves tightness of the entire sequence.

The initialized trace calculation \(\mathbb EF_n(0)^2=1/n\) is correct. Subsequence limits therefore have \(F(0)=0\), \(J(0)=1/2\), and inherit the algebraic relation \(J=(F-1)^2/2\).

The interpolation variants are justified. Raw-output and grid-output interpolants differ by \(O(\eta_n)\) on the controlled event. The exact loss-interpolation defect is

\[
\frac{\lambda(1-\lambda)}2(x-y)^2,
\]

which is \(O(\eta_n^2)\) there.

The proof explicitly invokes weak sequential compactness of tight probability laws on a complete separable space. Its hypotheses hold for \(C([0,T_0];\mathbb R^2)\): uniform limits give completeness, and rational polygonal approximations give separability. This is a stated theorem dependency, not an unstated population-limit assumption. The remaining compactness construction is supplied in the text.

The result establishes local tightness and subsequential distributional convergence of scalar observables. It does not establish determinism, uniqueness, convergence of the whole sequence, parameter-state compactness, kernel convergence, a dynamical loss law, or extension beyond \(T_0\).

**Section 9.3: gate occupation.** The invariant strip, boundary convention, and transformed update are correct:

\[
x_{k+1}=x_k+\lambda-I_k,\qquad x_k\in(0,1].
\]

Telescoping proves the strict discrepancy bound \(<1\) for windows within the strip. No ergodicity assumption is needed. The occupation conclusion concerns empirical proportions over growing windows, or corresponding time occupations as the step vanishes; it does not assert pointwise convergence of the binary gate.

Because \(I^r=I\), every positive integer moment of the binary occupation equals its first moment. Substituting the scalar mean would incorrectly replace the second moment by \(\lambda^2\). The equal-phase and complementary-phase examples at \(p=-q\) correctly have identical marginal occupations but joint products \(1/2\) and \(0\).

The text appropriately restricts these to frozen scalar examples. It does not claim their reachability in the random network or identify a unique generalized population flow from output compactness.

**New API, tests, and guide review.** `FrozenQuadraticEvaluation`, `_frozen_state`, `frozen_quadratic`, and `frozen_quadratic_step` agree with the mathematical reduction and documented interface.

- The evaluation fields and connector/readout kernel ordering are correct. The frozen evaluation intentionally has no separate `kernel` field; the guide correctly uses the sum of its blocks.
- Validation checks nonempty one-dimensional numeric arrays, equal shapes, finite values, booleans—including booleans in mixed numeric lists—and finiteness after float64 conversion.
- \(Q\ge0\), the \(Q=0\Rightarrow z=0\) constraint, finite scalar labels, and nonnegative finite steps are enforced.
- Neither routine initializes or updates the bottom layer.
- Both step increments use the same old state and physical step.
- Returned arrays are fresh. Work and storage are \(O(n)\), including the validation and repeated evaluation in the step routine.
- Kernel/evaluation range checks remain active at zero step, as documented. Intermediate range restrictions, rounding, and underflow are explicitly retained; mathematical exactness is not presented as exact floating-point arithmetic.
- The guide correctly distinguishes the finite primitive from the probabilistic initial-layer theorem and from a population solver.

The four frozen tests exercise raw unreduced loss/output differentiation, both kernel blocks, half-loss energy, simultaneous raw updates, recomputed interpolation, degeneracies, ownership, validation, and range rejection. The other nine tests cover the explicit mixed/RMS dependencies. Their assertions match the claims they test; none is evidence for a trajectory or population theorem.

**Executed checks and results.** The environment was Python **3.10.12**, NumPy **1.26.4**, matching `requirements.txt`. Imported packet modules resolved to this packet’s `code/pde` directory.

The exact requested command was run:

```bash
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_reductions
```

Result:

```text
Ran 13 tests in 0.103s
OK
```

The guide’s Python block was extracted and executed unchanged. Both assertions passed. Its evaluation included:

```text
output          0.004618802153517007
residual       -0.995381197846483
loss            0.4953918645131497
output_velocity 0.02309284379003842
loss_velocity  -0.02298618251341016
next_a          [ 0.30091949, -0.79977013]
next_z          [ 0.40096547, -0.19871271]
```

Additional independent checks, all passing:

| Check | Scope and result |
|---|---|
| Core raw derivatives | 60 output partials and 24 hidden-preactivation partials at fixed states; depths 1 and 3, \(d=2,m=3\), nonorthogonal/singular sample Gram, mixed activations, unequal mobilities. Checked forward output, gradients, residual-free deltas, kernel blocks, loss, dissipation, and one simultaneous update. Largest absolute discrepancy: \(2.22\times10^{-16}\). |
| Mixed/RMS derivatives | 32 output partials from independent definitions for QI, IQ, QQ, and differentiated RMS, including a zero bottom coordinate. Checked metric gradients and kernels. Largest absolute discrepancy: \(8.33\times10^{-17}\). |
| Frozen raw realization | 12 raw output partials; checked velocities, kernel blocks, energy, two connectors differing by \(W_\perp h=0\), raw-step equivalence, and interpolation at fractions \(0,0.3,1\). Largest absolute discrepancy: \(1.11\times10^{-16}\). |
| Frozen boundary/range checks | Positive \(Q\) with \(z=0\), zero-step identity and ownership, and rejection of an overflowing kernel even at zero step. Passed. |
| Exact Gaussian calculations | 11 rational moment cases, including singular covariance and negative correlation; six invalid-domain cases, including validation before odd/zero-degree shortcuts. Verified the \(32/3\) variance constant and initialization identities at three widths. Passed exactly. |
| Exact deletion witness | \(s=1/20,\varepsilon=1/8,\rho=1/1000,\delta=1/20\): initial output \(-0.001\), frozen output approximately \(-0.000999949998720064\), full output approximately \(-0.005062246868520324\). Strict ordering and bounds verified with rational arithmetic. |
| ReLU contact normal | Direct raw chain-rule calculation for six assigned slopes, with \(\lambda=0.4\). Largest absolute discrepancy: \(4.44\times10^{-16}\). |
| Compactness constants | Exact rational bootstrap and loss-interpolation identity; verified the negative net exponent. Passed. |
| Gate identities | Exact one-step strip and telescoping identities at 12 fixed states, including contact and upper boundary; binary powers and equal/complementary phase products. Passed exactly. |

The independent complex-step derivative checks used step \(10^{-20}\) and acceptance bound \(3\times10^{-12}\max(1,\|\text{reference}\|_\infty)\). These are implementation checks at fixed states, not substitutes for the analytical proofs.

**Required corrections: none.**

The clean verdict covers the supplied finite identities, their stated continuation and local compactness results, the frozen joint initial-layer theorem, the reached prescribed-field ReLU obstruction, the scoped occupation examples, and the documented finite APIs. The fully trained quadratic arbitrary-joint-step problem and identification or uniqueness of a generalized ReLU population flow remain unresolved by this packet, exactly as stated. No training, trajectory simulation, or historical campaign was run.