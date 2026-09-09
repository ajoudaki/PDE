**CLEAN. No required corrections found.**

I independently reviewed every line of all nine listed inputs, checked the mathematical dependencies and implementation interfaces, ran the required tests and guide example, and performed the deterministic checks reported below. All packet hashes remained unchanged.

The verdict covers the claims actually stated: exact finite identities, the frozen quadratic joint initial layer, the reached ReLU obstruction for a prescribed pointwise field, and local subsequential compactness of ReLU Euler outputs. It does not extend those results to the stronger conclusions the packet explicitly leaves unresolved.

The review used no delegation, other checkout, studies, other `/tmp` packet, previous verdict, task history, or external mathematical source. Diagnostics ran inline; no training, multistep trajectory simulation, or diagnostic file creation occurred.

The complete read and integrity record follows. Paths are relative to `/tmp/pde_assembly2_frozen_r2`. Every range includes comments and blank lines.

| Input | Lines read | Bytes |
|---|---:|---:|
| `docs/NOTATION.md` | 1–98 | 5,110 |
| `code/pde/__init__.py` | 1–26 | 611 |
| `code/pde/finite_network.py` | 1–363 | 15,525 |
| `code/pde/gaussian_moments.py` | 1–114 | 4,464 |
| `code/pde/finite_reductions.py` | 1–346 | 15,571 |
| `code/tests/test_finite_reductions.py` | 1–340 | 18,563 |
| `requirements.txt` | 1–2 | 111 |
| `docs/finite_dynamics.md` | 1–1275 | 48,489 |
| `code/README.md` | 1–42 | 2,363 |
| **Listed-input total** | **2,606 lines** | **110,807** |

I also read all 47 lines of `INPUTS.json`, totaling 1,388 bytes. The full finite-dynamics chapter was read consecutively in ranges 1–330, 331–650, 651–990, and 991–1275. A truncated portion of the first core-code display was recovered by explicitly reading lines 70–105.

Each digest below was computed before the substantive review and again after all executions. **Both computations returned the displayed value.** Every listed file also matched the manifest’s SHA-256, byte count, and line count.

| File | SHA-256 before = SHA-256 after |
|---|---|
| `INPUTS.json` | `cd32b32a8caf6d6ade39109a679ac4941b9a8f26acd09642f7261d812d29f3f7` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/finite_reductions.py` | `391dc35773a35d86f889cebda9f95820d793a656f2fb05f9b01bb7453be20a4c` |
| `code/tests/test_finite_reductions.py` | `7b1a4023334956a25afd4217de7a311145b64c240fc78b87f84b16d2af7dedb0` |
| `requirements.txt` | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `code/README.md` | `9480d7300646f1fff81501954b767f86bca606dcadc7cdb2fe27ba0d08baad77` |

I personally read the two requested skills:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`
- `/etc/codex/skills/investigate-conjectures/SKILL.md`

I also read `research-contract.md`, `evidence-ledger.md`, and `adversarial-audit.md` under the latter skill’s `references/` directory. Because deterministic computation was authorized, I read its `decisive-experiments.md` reference as well. These supplied review methodology, not mathematical evidence about the packet.

**Mathematical findings.** The conventions remain consistent across the dependencies and new sections.

The first layer uses \(Wx/\sqrt d\), stored middle matrices act without another width factor, and the readout divides by \(n\). Backward vectors exclude residuals. Sections 1–4 use mean squared loss and mobilities \(n\kappa_1,\kappa_2,\ldots,n\kappa_{L+1}\); Sections 5–7 use one-sample full squared loss and unit multipliers. Sections 8–9 explicitly change to half-square loss and order-one stored readout initialization.

The activation changes are also explicit: the mixed reductions use the raw square \(z^2\), the frozen theorem uses \(z^2/\sqrt3\), and the ReLU results use \(\sqrt2\,z_+\). The RMS architecture differentiates its vector-dependent denominators. None of these is silently substituted for another model.

- **Sections 1–4: finite gradients, kernels, energy, existence, and width bounds.** Equations (1)–(5) have the correct input, width, sample, mobility, and loss factors. Each kernel block is a Gram matrix of weighted output gradients, establishing positive semidefiniteness without any input-Gram invertibility assumption.

  The global finite-flow argument is complete. Dissipation bounds the integral of squared parameter speed in the positive weighted metric. Cauchy–Schwarz makes the parameters Cauchy at any hypothetical finite maximal endpoint; fixed-width metric equivalence and local existence then extend the solution.

  The width-independent bounds in Section 4 correctly require bounded activation derivatives, bounded initial norms and loss, and fixed depth. They are not applied to the unbounded derivatives of the quadratic models. The Gaussian initialization argument supplies the asserted high-probability event.

- **Section 5: mixed quadratic identities and Lax systems.** The three ascent fields, kernel blocks, physical factor \(-2r\), and output/loss identities agree with direct differentiation. Both isometric block constructions have the correct \(1/\sqrt n\) factors. Their commutator signs and the extra factor two for IQ are correct.

  The similarity proof works for the potentially non-self-adjoint operators: with \(\dot U=-FU\), differentiating \(U^{-1}\mathsf L U\) gives zero. The autonomous states retain the full oriented matrices of size \(n+1\).

  The spectrum witness is valid: it preserves the displayed feature vector, output, and spectrum while giving kernels \(68/9\) and \(28/3\). The QQ row and column balance derivatives cancel as stated. These arguments support no spectrum-only or fixed-dimensional scalar closure.

- **Sections 6–7: differentiated RMS reduction and continuation.** The normalization derivative
  \[
  DN_\varepsilon(x)=\sigma^{-1}\left(I-\frac{N_\varepsilon(x)N_\varepsilon(x)^T}{n}\right)
  \]
  is correct. Its radial factor is \(\varepsilon/\sigma^2>0\); treating this matrix as a projection would be wrong, and the text correctly avoids that.

  I checked the backward vectors, complete differential, feature derivatives, kernel blocks, scalar contraction (29), and both signed balance drifts. The recovered normalizer
  \[
  \alpha(h)=\sqrt{\frac{\varepsilon}{1-\|h\|^2/n}}
  \]
  correctly reconstructs raw lifts on \(h\ge0,\ \|h\|^2/n<1\). Local reduced uniqueness and global raw physical continuation establish the stated restart property independently of the recovered nonzero signs.

  The proof does not extend to the boundary \(\|h\|^2/n=1\), to \(\varepsilon=0\), or to global feature-ascent time. The finite physical-flow continuation argument is valid for all the smooth models in these sections.

- **Section 8.1: exact frozen reduction.** With \(c=1/\sqrt3\), frozen \(h\), \(Q=\|h\|^2/n\), and \(z=Wh\), direct differentiation gives
  \[
  \dot a=-r\,cz^2,\qquad
  \dot z=-r\,2cQ(a\odot z).
  \]
  Multiplication of the simultaneous raw connector update by the unchanged \(h\) gives exactly (8.1). Both increments use the old residual and old coordinates.

  The connector and readout kernel blocks are, respectively,
  \[
  K_W=\frac{4c^2Q}{n}\sum_i a_i^2z_i^2,\qquad
  K_a=\frac{c^2}{n}\sum_i z_i^4.
  \]
  Hence \(\dot f=-r(K_W+K_a)\) and
  \(\dot\ell=-r^2(K_W+K_a)\), with no extra factor two.

  The reduced domain is correct. If \(Q>0\), every finite \(z\) has a raw realization
  \[
  W=\frac{zh^T}{nQ};
  \]
  additional connector components annihilating \(h\) do not affect the reduction. If \(Q=0\), then \(h=z=0\), and both trained-block velocities and kernel blocks vanish. Thus the reduction is an exact current-state description of this frozen model.

- **Section 8.1: arbitrary joint width/step initial layer.** The probabilistic initialization and conditioning are correct. The Gaussian moments give
  \[
  \operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
  \mathbb E(f_n^0)^2=\frac1n\left(1+\frac{32}{3n}\right).
  \]

  The negative-row argument does not assume that a negative row’s preactivation keeps its sign. On survival, \(a_i^k\) is increasing, and
  \[
  |1-x|\le e^x\quad(x\ge0)
  \]
  bounds even a sign-flipping multiplier. A currently negative row was negative at all preceding steps, so the product bound (8.6) follows from its initial values. Gaussian exponential integrability supplies a uniformly bounded conditional second moment. Conditional Chebyshev therefore gives one initialization event controlling all relevant times; no union bound over steps is needed.

  The favorable-row comparison is also valid. On \(Q_n\ge1/2\), both positive coordinates dominate
  \[
  y^+=y+\gamma\eta_n y^2.
  \]
  Before a fixed level \(M\), the reciprocal decrement is at least \(\gamma\eta_n/2\) once \(\gamma\eta_nM\le1\). For each fixed \(T,\delta\), the proof chooses \(b\), then \(p_b>0\), then finite \(M\), all independently of \(n\). The favorable-row count and \(\eta_n\to0\) can therefore be used together without a relative rate condition.

  The selected rows contribute at least \(cp_bM^3/2\); all negative rows contribute at least \(-B_T\). Their combination contradicts survival. This proves the stated hitting-time convergence in probability.

  Raw-parameter interpolation makes the predictor continuous. Crossing to either \(\delta\) or \(-\delta\) forces a loss displacement from \(1/2\) of at least \(\delta-\delta^2/2\). The resulting uniform-convergence obstruction applies to deterministic or random continuous proposed limits with the initialized traces. No rate for the hitting time, fully trained quadratic theorem, or discrete energy inequality is inferred.

- **Section 8.2: deletion comparison.** The counterexample is algebraically correct and uses simultaneous updates with identical updated top blocks. Its bottom update multiplies the final output by \((1+4\varepsilon)^4\); since the frozen output is negative, the full output is smaller.

  An independent exact-rational instance used
  \[
  a=-1,\quad u=\frac1{25},\quad w=\frac{125}{2},\quad s=\frac1{10}.
  \]
  It gives
  \[
  f^0=-0.01,\quad
  f_{\rm frozen}^+\approx-0.00998998977024262,\quad
  f_{\rm full}^+\approx-0.050574323211853255,
  \]
  with exact ratio \(f_{\rm full}^+/f_{\rm frozen}^+=81/16\). All three outputs lie in \((-0.1,0.1)\). The common half-loss physical step is \(10/101\).

  This refutes the proposed pathwise lower comparison. It does not establish a typical-Gaussian-trajectory event or transfer the frozen theorem to full training.

- **Section 9.1: reached ReLU obstruction.** The raw chain rule at the specified contact gives exactly
  \[
  p=\frac38,\qquad
  q=\frac34\left(\frac12-4\lambda\right),\qquad
  v_0=\frac34\left(\frac12-\frac{4\lambda\sigma}{c}\right).
  \]
  For every fixed real \(\sigma\), one can choose \(\lambda>1/8\) with \(v_0\ne0\).

  The neighborhood argument preserves inward normal velocities on both sides and a nonzero convention-assigned velocity on the gate. For an absolutely continuous continuation starting there, \(w=|z_1^{(2)}|\) has negative derivative wherever positive and derivative zero almost everywhere on its zero set. Integration forces \(w\equiv0\), contradicting the assigned normal velocity.

  The open-set reachability step is supplied: bounded speed prevents escape from the neighborhood before the strictly decreasing positive normal coordinate reaches zero. Nondegenerate Gaussian density then gives positive probability at width two. The result concerns the prescribed pointwise field, even in the absolutely continuous almost-everywhere solution class; it makes no width-uniform probability claim or differential-inclusion claim.

- **Section 9.2: positive local Euler output compactness.** The pathwise norm estimate
  \[
  R^+\le R+6\eta R^5
  \]
  correctly bounds all three raw updates, including the connector’s rank-one operator norm. With \(R_*=6,\ S=12\), the bootstrap closes because
  \[
  R_*+6T_*S^5=S,\qquad
  T_*=\frac1{192\cdot6^4},\qquad
  T_0=\frac1{497664}.
  \]
  Thus \(T_0\approx2.0093878600823047\times10^{-6}\) in the stated half-loss clock.

  The initialization event has probability tending to one. In particular, the matrix-net bound decays because
  \[
  \frac92-\log81\approx0.1055508453>0.
  \]
  Once \(\eta_n\le T_0\), every endpoint required for interpolation through \(T_0\) lies within the bootstrap horizon.

  The feature and predictor product-difference bounds are valid across gates. The stated predictor Lipschitz constant \(60S^7\) safely exceeds the derived \(36S^7\). The bounded common Lipschitz class is compact in the uniform topology; the continuous loss map produces a compact class of pairs. The finite-prefix argument correctly upgrades asymptotic tightness to tightness of the whole sequence.

  Initialization gives \(\mathbb EF_n(0)^2=1/n\), so subsequential limits have the stated initial traces. Raw-recomputed and grid-interpolated predictors differ by \(O(\eta_n)\) on the high-probability event. The loss interpolation identity
  \[
  (1-\lambda)\ell(x)+\lambda\ell(y)
  -\ell((1-\lambda)x+\lambda y)
  =\frac{\lambda(1-\lambda)}2(x-y)^2
  \]
  proves the claimed loss variants.

  This establishes local tightness and continuous subsequential distributional limits of outputs and losses. It does not identify parameter limits, kernels, a unique limiting equation, determinism, convergence in probability, or continuation beyond \(T_0\).

- **Section 9.3: frozen gate occupation.** The half-open strip \(\eta q<z\le\eta p\) is invariant, including the convention at zero. Inside it, the coordinate transformation gives exactly
  \[
  x_{k+1}=x_k+\lambda-I_k,\qquad \lambda=\frac p{p-q}.
  \]
  Telescoping proves the discrepancy bound \(<1\) on every finite window within the strip. Consequently the empirical occupation error is \(<1/N\).

  All positive integer gate moments have the same empirical limit because \(I_k^r=I_k\). Substituting the scalar mean would incorrectly change the second moment to \(\lambda^2\). The equal-phase and half-circle-shift examples at \(p=-q\) correctly distinguish joint occupations while preserving the same marginals.

  These are frozen scalar examples. The text does not claim they are reached random-network configurations or use them to identify a generalized population loss law.

I found no missing substantive proof bridge or unstated population-result import. The finite ODE arguments give their contraction and continuation mechanisms; the compact-function argument is supplied directly. The weak compactness step explicitly invokes the applicable probability theorem: tight probability measures on the complete separable space \(C([0,T_0];\mathbb R^2)\) admit weakly convergent subsequences. Its hypotheses hold here. The Gaussian moments and concentration steps require only the stated conditioning and elementary Gaussian identities; no external source was needed.

**Implementation findings.** All supplied Python was reviewed, including package imports and the helpers used by the new APIs.

`finite_network.py` implements the stated forward scaling, residual-free backpropagation, mean-square gradients, mobility factors, kernel blocks, and simultaneous raw GD. The core interfaces used by the reduction tests were additionally checked against independent raw-network complex-step derivatives. The initializer implements the separate small-readout convention; the frozen APIs neither call it nor reset a supplied readout.

`gaussian_moments.py` correctly validates rational symmetric positive-semidefinite covariance, including zero pivots and singular matrices, before the zero-degree or odd-degree shortcuts. Its Wick recurrence has the correct pairing multiplicities. Cache ownership and the stated computational limitations agree with the implementation.

The mixed, Lax, and RMS routines agree with their mathematical definitions. The RMS denominators are differentiated throughout, and the Lax implementation preserves orientation and the IQ generator factor two.

For the new frozen APIs:

| API | Finding |
|---|---|
| `FrozenQuadraticEvaluation` | Fields match the guide. Kernel blocks are in connector/readout order; velocities use half-loss physical time. |
| `_frozen_state` | Validates nonempty matching real numeric vectors, rejects booleans including mixed lists, checks finiteness after float64 conversion, copies inputs, and enforces \(Q\ge0\) and \(Q=0\Rightarrow z=0\). |
| `frozen_quadratic` | Correct output, residual, half loss, both kernel blocks, both state velocities, output velocity, and loss velocity. Arbitrary finite scalar labels are handled consistently. |
| `frozen_quadratic_step` | Validates finite nonnegative `eta`, uses the same old evaluation for both increments, returns fresh arrays, and checks updated coordinates for nonfinite values. |

The implementation and guide correctly restrict execution to ordinary float64 evaluation, including intermediate range limitations. Underflow and rounding remain possible. The step routine evaluates the kernel even for a zero step; this agrees with its documented evaluation requirement. No arbitrary-step stability, exact finite-time flow, Gaussian initialization, or population-solver behavior is promised.

The guide’s direct imports from `pde.finite_reductions` are valid; the absence of these names from the package-level `__all__` does not break the documented API.

**Execution and independent-check record.**

The required command ran exactly as requested:

```text
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_reductions
```

Result:

```text
.............
----------------------------------------------------------------------
Ran 13 tests in 0.103s

OK
```

The thirteen tests cover four mixed-reduction checks, four RMS checks, one reduction-contract check, and four frozen-quadratic checks. I reviewed their assertions as well as running them. In particular, the frozen tests differentiate the unreduced connector/readout output and half loss, compare raw simultaneous updates, check recomputed interpolation, and exercise validation and ownership.

The exact Python block at guide lines 11–17 was extracted and executed unchanged. Both assertions passed. The environment was Python **3.10.12** and NumPy **1.26.4**, matching `requirements.txt`.

The guide produced:

```text
output   = 0.004618802153517007
residual = -0.995381197846483
loss     = 0.4953918645131497

next_a = [ 0.30091949 -0.79977013]
next_z = [ 0.40096547 -0.19871271]
```

All additional checks were deterministic and evaluated fixed states or single updates:

| Independent check | Coverage and result |
|---|---|
| Raw core differentiation | Three configurations: \((n,L)=(2,1),(3,2),(2,3)\), all with \(d=2,m=3\), dependent input columns, nonunit mobility multipliers, and arctan, square/identity, or tanh/arctan/square activations. Checked every parameter derivative by complex step, output, mean loss, velocities, kernel blocks and sum, energy identity, last-layer backward scaling, and one simultaneous GD step. **Passed.** |
| Exact Gaussian moments | Nine cases: standard fourth and eighth moments; correlated fourth and sixth moments; singular anticorrelated covariance; rational covariance; zero covariance directions; zero degree; odd degree. **All exact Fraction results matched.** |
| Invalid covariance rejection | Three indefinite covariance matrices, each tested with zero total degree and odd total degree. **All six rejected before moment shortcuts.** |
| Frozen raw differentiation | Width-one and width-three raw connector/readout networks. Checked complex-step output gradients, both kernel blocks, velocities, half loss, output derivative, and raw metric energy. **Passed.** |
| Frozen reduction geometry | Checked \(Wh=z\) for the explicit raw lift and \(\|\dot W\|_F^2=\|\dot z\|^2/(nQ)\) for the induced rank-one update. **Passed.** |
| Frozen step and interpolation | Compared one reduced step with simultaneous raw updates and recomputed output at cell fraction \(0.37\). **Passed.** |
| Degenerate states and ownership | Checked zero preactivation at both \(Q=0\) and \(Q>0\), stationary updates, float64 conversion, and absence of returned-array aliasing with inputs. **Passed.** |
| Deletion-order algebra | Exact rational counterexample above, plus a separate positive-state single step showing the reverse universal order also fails. **Passed.** |
| ReLU contact differential | Five prescribed conventions, each with negative-side, positive-side, and contact normal velocities: fifteen comparisons against the raw differential. **Passed; maximum absolute error \(4.441\times10^{-16}\).** |
| ReLU local bounds | Three single-update checks at a state containing bottom and top gates, using \(\sigma=-c,0,c\); exact bootstrap arithmetic and Gaussian-net exponent check. **Passed.** |
| Frozen gate map | Five exact-rational one-step strip/conjugacy cases, including zero and the upper boundary; complementary half-circle phases. **Passed.** |
| Loss interpolation and variance constants | Two exact-rational loss interpolation cases and the exact quadratic variance constant \(32/3\). **Passed.** |

For the core and frozen floating comparisons, the error measure was
\[
\frac{\|{\rm computed}-{\rm reference}\|_\infty}
{\max(1,\|{\rm reference}\|_\infty)}.
\]
The acceptance threshold was \(5\times10^{-12}\); complex-step size was \(10^{-30}\). The maximum observed error was \(2.776\times10^{-17}\) for the core checks and \(5.551\times10^{-17}\) for the frozen checks. The ReLU contact checks used an absolute threshold of \(5\times10^{-14}\). Exact-rational checks used equality.

**Required corrections: none.**

The unresolved boundaries remain exactly those stated in the packet: the fully trained quadratic arbitrary-joint-step problem; identification and uniqueness of a generalized ReLU population flow or loss law; parameter-state and kernel convergence; and extension of the ReLU compactness theorem beyond its explicit local horizon. Passing algebra and implementation checks does not resolve those questions.