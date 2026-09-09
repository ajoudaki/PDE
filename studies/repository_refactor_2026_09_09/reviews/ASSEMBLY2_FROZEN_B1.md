**CORRECTIONS REQUIRED.** I found one reproducible input-validation defect in the new frozen APIs: mixed Boolean/numeric vectors are accepted despite the guide’s explicit Boolean-rejection contract. The supplied tests miss this case.

I found no mathematical correction required in Sections 8–9, their earlier finite identities, or the reduction formulas. The specified 13 tests, the guide example, and the independent checks described below passed, apart from the deliberately tested Boolean-contract counterexamples.

The review was independent and used no delegation, external sources, other checkouts, studies, previous verdicts, or task history. All diagnostics ran inline. No packet input was changed.

**Read coverage and hash verification.** I read every line of all nine manifest-listed inputs: 109,777 bytes and 2,588 lines. I also read `INPUTS.json` in full and personally read these requested instruction files:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`
- `/etc/codex/skills/investigate-conjectures/SKILL.md`
- Its `references/research-contract.md`, `references/evidence-ledger.md`, and `references/adversarial-audit.md`

Each SHA-256 below was independently computed before and after the review. Both measurements equal the displayed digest and the manifest value; byte and line counts also matched before and after.

| Input | Bytes | Lines read in full | SHA-256 before = SHA-256 after |
|---|---:|---:|---|
| `docs/NOTATION.md` | 5,110 | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/pde/__init__.py` | 611 | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 15,525 | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 4,464 | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/finite_reductions.py` | 15,309 | 1–342 | `1af9d5b2d4517355ddee9410e75007e31ff7aa732720153c5e60b61a8804fcbc` |
| `code/tests/test_finite_reductions.py` | 18,170 | 1–333 | `6445164cfb700bb0da053058c16e45524933e4a0c12fc6cf9b426916c87dbc17` |
| `requirements.txt` | 111 | 1–2 | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |
| `docs/finite_dynamics.md` | 48,114 | 1–1268 | `f9bc305b6c438d87a81cb25407a44b7a2109ef29413a1fb6023505ad327641bb` |
| `code/README.md` | 2,363 | 1–42 | `9480d7300646f1fff81501954b767f86bca606dcadc7cdb2fe27ba0d08baad77` |

`INPUTS.json` itself was unchanged: 1,388 bytes, 47 lines, SHA-256 before and after
`377e0945d0f8e3ed8429fc9e3fc04df7fc7d1a5cf51f367f986c7ab16e6514f1`.

**Required correction.**

1. **Reject mixed Boolean/numeric vector inputs before NumPy promotes their elements.** In [_frozen_state](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py:277), `np.asarray(value)` runs before the dtype check. Consequently, a Boolean mixed with integers or floats becomes an ordinary numeric value and passes validation. This contradicts [the guide](/tmp/pde_assembly2_frozen_r1/code/README.md:28), which says “Booleans are rejected.”

   These calls were executed and accepted:

   ```python
   frozen_quadratic([True, 0.3], [0.4, -0.2], 0.7)
   frozen_quadratic([0.3, -0.8], [0.4, False], 0.7)
   frozen_quadratic([True, 2], [0.4, -0.2], 0.7)
   ```

   Their outputs were, respectively, `0.049652123150307835`, `0.013856406460551023`, and `0.06928203230275512`. `_frozen_state` and `frozen_quadratic_step(..., eta=0.01)` also accepted all three cases. Pure Boolean vectors and Boolean scalar `Q` were correctly rejected.

   Inspect supplied sequence elements for Python and NumPy Booleans before numeric promotion, while retaining rejection of Boolean-dtype arrays. Add regression cases for mixed Boolean readouts and preactivations through both public APIs. An already numeric ndarray does not retain the provenance of earlier Boolean-to-number conversions; the check should concern the input as supplied.

   This is a limited implementation/contract defect. It does not invalidate the mathematical formulas or the Section 8–9 theorems.

**Notation and earlier mathematical dependencies.** The notation contract consistently distinguishes stored matrices, normalized pairings, raw parameter interpolation, initialization regimes, and clocks. In particular, the general core uses first/readout mobilities \(n\kappa\), middle mobilities \(\kappa\), and mean full squared loss. Sections 8–9 explicitly change to one sample, half-square loss, and order-one stored readout initialization. That change is not silently imported into the core initializer.

In Sections 1–2, differentiating the output gives the stated \(1/n\) factors and the first-layer \(1/\sqrt d\). Applying the mobility cancels \(1/n\) in the first and readout velocities, but retains it in middle updates. The backward variables contain no residual. The kernel blocks follow from the Frobenius rank-one pairing, with no Gram inversion or data whitening. Their weighted-gradient representation proves positive semidefiniteness and yields
\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr
=-\|D^{-1/2}\dot\theta\|^2.
\]

Section 3’s global finite-width continuation argument is valid for the stated \(C^2\) activations. Local Lipschitzness gives local existence and uniqueness. The integrated energy identity bounds parameter displacement by \(\sqrt{(t-s)\mathcal L(0)}\) in the fixed-width learning metric. A finite maximal endpoint would therefore have a finite parameter limit, where local existence extends the solution. This argument does not require bounded activations and does not establish arbitrary-step GD stability.

Section 4’s width-independent bounds correctly add bounded activation derivatives and bounded initial normalized norms. The forward and backward inductions use operator norms and RMS norms with the correct factors. The Gaussian matrix net estimate has the correct exponent and cardinality. These bounds do not automatically apply to the unbounded derivative of a quadratic activation, nor does the smooth-flow theorem automatically apply to ReLU. Sections 8–9 supply separate arguments.

Section 5’s QI, IQ, and QQ ascent fields and three kernel blocks agree with direct differentiation in the metric
\[
\|du\|^2/n+\|dB\|_F^2+\|da\|^2/n.
\]
The distinction between unit output ascent and physical velocity \(-2r\theta'\) is maintained even at zero residual or with negative labels.

Both Lax identities have the correct isometric \(1/\sqrt n\) factors. QI uses \(\mathsf Q'=\mathsf QS\); IQ uses \(\mathsf P'=2S\mathsf P\). Anticommutation with the signature matrix gives the displayed commutators. The supplied similarity argument proves isospectrality without assuming self-adjointness. The width-three orientation witness is raw-realizable: its two kernels are \(68/9\) and \(28/3\), despite equal output, common \(h\), and equal spectrum. It therefore defeats the specified spectrum-based restart state, while leaving the full operator states intact. The QQ row and column balances cancel exactly.

Section 6 differentiates both RMS denominators. Its matrices \(I-hh^T/n\) and \(I-vv^T/n\) are correctly treated as positive definite and generally non-idempotent for \(\varepsilon>0\). The backward fields, feature derivatives, kernel, and signed balance drifts agree with the chain rule. In particular,
\[
h^Tq/n=2\varepsilon f/\beta^2
\]
supplies the column-balance correction; omitting it would change the dynamics.

The reduced RMS state is legitimately restartable on the stated raw-image domain. The reconstruction
\[
\alpha(h)=\sqrt{\varepsilon/(1-\|h\|^2/n)},\qquad
u_j=\pm\sqrt{\alpha(h)h_j}
\]
has the required normalizer. Sign choices project to the same locally unique reduced solution. Global finite physical continuation follows through raw lifts, without asserting continuation on the boundary \(\|h\|^2/n=1\), global feature-ascent existence, or width-independent state dimension. Section 7’s energy continuation proof remains valid for these smooth finite models.

**Section 8.1: exact frozen reduction.** With fixed \(h\), \(Q=\|h\|^2/n\), \(z=Wh\), and \(c=1/\sqrt3\), direct differentiation gives
\[
\nabla_a f=\frac cn z^2,\qquad
\nabla_W f=\frac{2c}{n}(a\odot z)h^T.
\]
For half-square loss, connector/readout mobilities \(1,n\), and \(r=f-1\), this yields
\[
\dot a=-rcz^2,\qquad
\dot z=-2rcQ(a\odot z).
\]
Multiplying the simultaneous raw connector update by the unchanged \(h\) proves (8.1) exactly. No flow approximation, updated-readout substitution, or sequential block update is used.

The kernel blocks are
\[
K_W=\frac{4c^2Q}{n}\sum_i a_i^2z_i^2,\qquad
K_a=\frac{c^2}{n}\sum_i z_i^4.
\]
Thus \(\dot f=-r(K_W+K_a)\) and
\(\dot\ell=-r^2(K_W+K_a)\), with no extra factor two. Although the chapter displays the readout term first in (8.2), the API explicitly returns connector/readout order and implements that order correctly.

The state domain is also correct. For \(Q>0\), any \(z\) has the raw realization
\[
W=\frac{zh^T}{nQ}.
\]
For \(Q=0\), necessarily \(h=0\) and \(z=0\); output, kernel, and both velocities vanish. Components of \(W\) invisible to \(h\) do not affect the reduced update. This is an exact width-dependent finite reduction.

**Section 8.1: joint initial-layer theorem.** The proof preserves its specific frozen Gaussian initialization: bottom features \(cu_j^2\), connector entries of variance \(1/n\), and stored readouts of variance one. Conditional on the bottom features, the row pairs are independent with laws \(N(0,1)\) and \(N(0,Q_n)\).

The initialization calculations are correct:
\[
\operatorname{Var}(Q_n)=\frac{105-9}{9n}
=\frac{32}{3n},
\qquad
\mathbb E(f_n^0)^2=\frac{\mathbb E Q_n^2}{n}.
\]
The latter uses centered independent readouts to remove cross terms. Hence \(Q_n\to1\) and \(f_n^0\to0\) in probability.

On survival inside \((-\delta,\delta)\), the step multiplier satisfies
\[
(1-\delta)\eta_n\le s_k\le(1+\delta)\eta_n.
\]
Every readout is then nondecreasing. If a row is still negative, all its preceding readouts were negative and their magnitudes were bounded by its initial negative part. The estimate
\[
|1-x|\le1+x\le e^x,\qquad x\ge0,
\]
justifies the bound on its preactivation even when a discrete step changes the preactivation’s sign. Iterating gives (8.6). Once the readout becomes nonnegative, the lower bound remains valid automatically.

The aggregate negative-row bound is established on one initialization event. On \(Q_n\in[1/2,2]\), the summands have uniformly bounded conditional second moments, because Gaussian polynomial moments with \(e^{b|G|}\) are finite. The conditional mean is separated from \(B_T\) by a positive margin. Conditional Chebyshev therefore proves (8.8), without a union bound over the potentially enormous number of steps.

For the favorable rows, \(b\) is fixed before taking \(n\to\infty\). Their conditional binomial count is at least \(np_b/2\) with probability tending to one. Both coordinates remain positive and their minimum dominates
\[
y^{k+1}=y^k+\gamma\eta_n(y^k)^2.
\]
Before reaching a fixed level \(M\), the reciprocal decrement is at least \(\gamma\eta_n/2\) once \(\gamma\eta_nM\le1\). Thus the stated hitting-time bound follows, including the case of a row already above \(M\).

The order of choices is essential and is respected: fix \(T,\delta\); choose \(b\); then choose \(M\); finally let \(n\) increase. Both constants may be very large, but neither depends on \(n\). Consequently \(\eta_n\to0\) alone eventually supplies the needed small-step condition. There is no hidden requirement involving \(\eta_n\log n\), coordinate maxima, or a width-dependent tail cutoff.

At the common level, favorable rows contribute at least \(B_T+2\delta\), while negative rows contribute at least \(-B_T\). This contradicts survival. The argument therefore proves
\[
\Pr\{\tau_n(\delta)>T\}\to0
\]
for every fixed \(T>0\), exactly the asserted convergence in probability.

The interpolation consequence is valid despite possible grid overshoot. Recomputed output along continuous raw interpolation must cross \(+\delta\) or \(-\delta\). At that crossing the output change is bounded below, and the half loss differs from \(1/2\) by at least \(\delta-\delta^2/2\). Since initialization converges to the stated traces, uniform convergence in probability to a continuous initialized path is impossible. The modulus-of-continuity argument also covers a random continuous proposed limit.

This theorem concerns the frozen model and this mode of convergence. It does not establish the corresponding fully trained quadratic theorem or a claim about all possible weaker convergence topologies.

**Section 8.2: failure of the deletion comparison.** The section explicitly changes to deterministic width one and raw square activation. Its three simultaneous ascent increments are the correct derivatives of \(aw^2u^4\).

The chosen parameters satisfy \(w^2u^2=R\), \(w^2u^4=\rho\), and \(u^+/u=-1-4\varepsilon\). The frozen and full updates have identical \(a^+,w^+\), so
\[
f_{\rm full}^+=(1+4\varepsilon)^4f_{\rm frozen}^+
<f_{\rm frozen}^+<0.
\]
The small-\(\rho\) conditions are compatible and keep the initial and terminal outputs within the specified interval. This gives a counterexample for every positive ascent step, with a step-dependent state. At the common initial residual, the ascent step also corresponds to a common positive physical half-loss step.

The counterexample validly refutes the proposed pathwise lower comparison. It does not show that the fully trained Gaussian theorem is false, and the text makes no such inference. Its explicit activation normalization and deterministic scope are preserved.

**Section 9.1: reached ReLU classical obstruction.** At the displayed contact state, the bottom gates and second top gate are strictly positive, while the first top preactivation is zero. Direct raw differentiation gives
\[
\dot z_1=\frac34(4a_1v+2a_2c),
\]
and therefore the three normal velocities in (9.2). The negative-side velocity is positive; the positive-side velocity is negative whenever \(\lambda>1/8\). For every fixed real \(\sigma\), at most one choice of \(\lambda\) makes the assigned contact velocity zero, so the required choice exists.

The strict inequalities persist in a sufficiently small neighborhood, including a nonzero lower bound on the magnitude of the assigned gate velocity. For an absolutely continuous continuation starting on the gate, \(w=|z_1|\) is absolutely continuous. Its derivative is negative where \(w>0\), and zero almost everywhere on its zero level set. Integrating forces \(w\equiv0\), which contradicts the nonzero assigned derivative of \(z_1\) there. The argument establishes nonexistence even in the stated almost-everywhere absolutely continuous solution class.

Reachability is established separately. The positive-side perturbation has small positive normal coordinate. Bounded speed controls departure from the neighborhood, while the uniformly negative normal velocity forces contact first. Strict inequalities persist for a small open set of initial states. The nondegenerate finite Gaussian law assigns that open set positive probability.

The result is therefore stronger than an isolated example initialized exactly on a gate. Its scope nevertheless remains width two, with a convention-dependent positive-probability set. It provides neither a uniform-in-width probability bound nor a prohibition on differential-inclusion solutions with another selection rule.

**Section 9.2: positive local Euler output compactness.** The proof correctly uses ReLU Lipschitzness and the bound \(|\sigma|\le\sqrt2\), without importing smooth-flow energy dissipation into Euler updates.

The forward and backward estimates imply
\[
|f|\le2R^3,\qquad |r|\le3R^3.
\]
Each normalized first/readout increment and the connector operator-norm increment is bounded by \(6\eta R^5\). The connector estimate uses the exact rank-one operator norm. Hence \(R^+\le R+6\eta R^5\) is valid, including at gates.

The bootstrap constants check exactly:
\[
6+6\left(\frac1{192\cdot6^4}\right)12^5=12.
\]
The induction bounds every required grid endpoint through \(T_*=2T_0\). Once \(\eta_n\le T_0\), this includes the endpoint beyond \(T_0\) needed for interpolation. Thus there is no missing last-cell estimate.

The initialization event has probability tending to one. Chebyshev controls the two Gaussian vector RMS norms. The matrix proof uses two \(1/4\)-nets of size at most \(9^n\), a Gaussian tail at threshold three, and the factor-two approximation of the operator norm. The resulting bound tends to zero because \(\log81<9/2\).

Convexity preserves the norm bound under raw parameter interpolation. The product-difference estimates yield the displayed Lipschitz constants for first features, second preactivations, second features, and output. The calculated output constant \(36S^7\) is safely bounded by the stated \(60S^7\). Summing across cells gives a common modulus on the entire interval.

Uniform output bounds and this common modulus provide a compact subset of the continuous-path space. The half-loss map is continuous on it, giving compactness for output/loss pairs. The treatment of finitely many smaller widths is valid: bounded initialization sets and finitely many finite Euler steps yield separate compact sets whose finite union remains compact.

The probability-measure compactness theorem invoked here is explicit: tight laws on the complete separable space \(C([0,T_0];\mathbb R^2)\) admit weakly convergent subsequences. Its hypotheses are satisfied. Completeness follows from uniform convergence, and separability from piecewise-linear approximations with rational data. No population-flow existence or identification theorem is being imported through this step.

The initialization identity \(\mathbb E F_n(0)^2=1/n\) correctly conditions successively on the bottom variables, connector rows, and independent readouts. Continuous evaluation at time zero gives the asserted limit traces.

The interpolation comparisons also check. Raw-recomputed and linearly interpolated grid predictors agree at endpoints and differ uniformly by \(O(\eta_n)\) on the high-probability event. The exact loss interpolation identity is
\[
(1-\lambda)\ell(x)+\lambda\ell(y)
-\ell((1-\lambda)x+\lambda y)
=\frac{\lambda(1-\lambda)}2(x-y)^2,
\]
bounded by \((x-y)^2/8\). This supplies the stated \(O(\eta_n^2)\) comparison between interpolated grid losses and the loss of interpolated grid predictors.

The resulting theorem is local tightness of scalar output/loss laws and subsequential distributional convergence on
\[
T_0=\frac1{497664}\approx2.0093878600823047\times10^{-6}.
\]
It does not assert deterministic limits, uniqueness, full parameter compactness, kernel convergence, an identified loss evolution law, or continuation beyond this horizon.

**Section 9.3: frozen gate occupation identities.** The strip \(\eta q<z\le\eta p\) is invariant with the stated zero convention. Points below it repeatedly move upward; points above it repeatedly move downward until entering it. The endpoint choices are consistent with the convention at zero.

Inside the strip,
\[
x_{k+1}=x_k+\lambda-I_k,\qquad
\lambda=\frac p{p-q},
\]
holds also when \(z_k=0\). Telescoping proves the strict discrepancy bound below one because both endpoint phases lie in \((0,1]\).

This establishes occupation frequencies over increasing windows, and the corresponding occupation averages over fixed positive physical windows as \(\eta\to0\). It does not assert pointwise convergence of the binary gates. Since \(I^r=I\), all positive integer occupation moments equal the same limiting \(\lambda\); substituting a constant mean would instead give \(\lambda^2\) for the second moment.

For \(p=-q\), the identical-phase and half-period-shifted examples have the stated equal marginals and different joint products. The distinction is exact. The text correctly limits these examples to frozen scalar gates and does not claim their joint configurations are reachable in the random neural network. They explain why output compactness alone cannot identify the gate products appearing in kernels.

**Implementation audit of the new APIs.** [FrozenQuadraticEvaluation](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py:257) contains exactly the quantities documented in the guide. Its velocities are physical half-loss velocities, and its two kernel blocks have connector/readout order. It does not expose a separate total-kernel field; the guide correctly instructs callers to sum the blocks. `frozen=True` protects field assignment, while the arrays remain caller-owned mutable arrays.

`_frozen_state` correctly enforces nonempty one-dimensional numeric arrays, equal shapes, finite values before and after float64 conversion, finite scalar \(Q\), nonnegative \(Q\), and \(z=0\) when \(Q=0\). It copies both vectors. The Boolean-promotion defect described above is the required exception to this otherwise correct validation implementation.

[frozen_quadratic](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py:294) implements the output, residual, half loss, two velocities, kernel blocks, and output/loss derivatives derived above. It permits arbitrary finite labels as documented by the API; this is broader than the theorem’s fixed label one and does not change the theorem’s assumptions. It performs no initialization and no bottom update.

[frozen_quadratic_step](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py:324) validates a finite nonnegative physical step, evaluates one old state, and adds both increments simultaneously. The returned preactivation equals the updated raw connector applied to the fixed feature vector. Zero steps return fresh arrays. The function evaluates the kernel and other fields even at zero step, consistently with its documented representability requirement.

Both functions use \(O(n)\) work and storage and return fresh arrays. They reject evaluated nonfinite values and overflow encountered by the guarded arithmetic. The module explicitly disclaims a range-proof implementation: representable mathematical answers can still be rejected because of overflowing intermediate calculations, and ordinary rounding or underflow can occur. The implementation should therefore be read as floating evaluation of exact formulas, not exact arithmetic or an unconditional finite-range guarantee.

**Audit of the remaining implementation inputs.** In `finite_network.py`, parameter shapes, layer ordering, first-layer normalization, readout normalization, backward transpose reuse, sample averaging, and block mobilities agree with the finite identities. `flow_velocity` evaluates the physical RHS; `gd_step` uses one pre-update state and returns new arrays. The initializer uses standard deviations \(1\), \(1/\sqrt n\), and \(1/n\), giving the specified variances. Custom activation evaluation protects inputs and returned fields from callback buffer reuse; differentiability assumptions remain the caller’s responsibility.

The earlier `finite_reductions.py` routines correctly implement QI/IQ/QQ and differentiated RMS fields. Their physical multiplier is the full-loss \(-2r\), separate from the frozen half-loss APIs. `mixed_lax` incorporates the IQ factor two in its generator and retains full raw-image orientation. The balance and field arrays match the chapter’s definitions.

`gaussian_moments.py` validates dimensions, symmetry, rational entries, powers, and positive semidefiniteness before zero- or odd-degree shortcuts. Its zero-pivot rule correctly rejects a nonzero covariance row at a zero diagonal. Positive pivots use the exact Schur complement. The Wick recurrence has the correct remaining-exponent multiplicities, terminates by reducing degree by two, and returns rational values with a local cache cleared after use. Its documented complexity and high-order limitations are consistent with the implementation.

`__init__.py` exports the stated core and moment APIs. The guide imports the frozen APIs from `pde.finite_reductions`, so their absence from package-root `__all__` is not an interface error. `requirements.txt` pins NumPy 1.26.4, which matches the executed environment.

The guide correctly states the frozen architecture, half-loss clock, fixed \(Q\), update simultaneity, block order, ownership, computational complexity, and distinction from a population solver. Its Boolean-rejection sentence requires the implementation correction already identified.

**Supplied tests and guide execution.** I ran the exact requested command:

```text
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_reductions
```

Result:

```text
Ran 13 tests in 0.101s
OK
```

The test file contains four mixed-reduction tests, four RMS tests, one shared-contract test, and four frozen tests. I inspected every helper and assertion.

The frozen tests independently differentiate the unreduced connector/readout output and half loss, compare both mobility-weighted kernel blocks, check simultaneous raw updates, verify metric dissipation, and differentiate output and loss along a raw affine parameter perturbation. They also check recomputed interpolation, stationary cases, ownership, invalid inputs, and range failures. Their finite differences are algebra/derivative diagnostics, not trajectory experiments. Their validation coverage omits mixed Boolean/numeric vectors.

I extracted and executed the guide’s Python block unchanged. Both assertions passed under Python 3.10.12 and NumPy 1.26.4. It produced:

```text
output = 0.004618802153517007
loss   = 0.4953918645131497
next_a ≈ [ 0.30091949, -0.79977013]
next_z ≈ [ 0.40096547, -0.19871271]
```

**Independent checks performed.** These checks used fixed states, exact rational calculations, derivative perturbations, or individual updates. No training, trajectory simulations, or historical campaigns were run.

| Check | Scope and result |
|---|---|
| Core raw derivatives | Complex-step differentiation of 14 raw coordinates in a three-hidden-layer, three-sample network with correlated/singular sample Gram and nonunit mobilities. Maximum absolute gradient error \(2.78\times10^{-17}\); physical-velocity error \(5.55\times10^{-17}\). |
| Core kernels and backward variables | Independently assembled all kernel blocks from raw output Jacobians; maximum error \(3.47\times10^{-17}\). Checked every backward-coordinate derivative, MSE convention, simultaneous GD, and update ownership. Passed. |
| Frozen raw derivatives | Complex-step raw-output derivatives for 28 connector/readout coordinates across widths 1, 2, and 4. Checked three labels per state, both kernel blocks, physical velocities, and metric half-loss dissipation. Maximum evaluation error \(1.11\times10^{-16}\). |
| Frozen update and domain | Checked zero and positive steps against raw connector/readout updates, an interior raw interpolation point, \(Q>0\) realizations, stationary zero preactivations for \(Q=0\) and \(Q>0\), and `_frozen_state` ownership. Passed. |
| Boolean contract | Three mixed Boolean/numeric vector examples were accepted by both public APIs and `_frozen_state`. Pure Boolean and Boolean-scalar controls were rejected. This establishes required correction 1. |
| Gaussian moments | Eight exact moment cases, including fourth/eighth moments, correlated covariance, singular covariance, and zero covariance; six invalid-input controls. Passed. Independently recovered \(\operatorname{Var}(Q_n)=32/(3n)\). |
| Deletion counterexample | Exact rational one-step calculation with \(s=1/100\), \(\varepsilon=1/4\), \(\rho=1/1000\). Obtained \(u^+/u=-2\), \(f_{\rm full}^+/f_{\rm frozen}^+=16\), strict reversed comparison, and all absolute outputs below \(0.1\). |
| Frozen growth estimates | Checked the negative-row factor bound and the exact reciprocal-growth identity with rational arithmetic. Passed. |
| ReLU contact | Recomputed normal derivatives directly from raw parameter velocities for five kink conventions, including negative, zero, and larger-than-\(c\) values. The three contact formulas and required signs agreed. |
| Compactness constants | Verified the bootstrap equality and exact half-loss interpolation-gap identity with rational arithmetic. Passed. |
| Frozen gate identities | Checked invariant-strip bounds and the telescoping increment at fixed phases, including \(z=0\), for two choices of \(p,q\). Passed. |

No unstated specialized theorem or unsupported population identification is needed for the reviewed arguments. The standard compactness, local ODE, and continuity facts used in the proofs have the necessary hypotheses here. The remaining mathematical boundaries are the ones the packet explicitly preserves: finite versus population dynamics, frozen versus fully trained models, full versus half loss, classical solutions versus Euler subsequences, scalar output compactness versus gate/kernel identification, and local versus arbitrary-horizon conclusions.