**CORRECTIONS REQUIRED.** I found one reproducible API-validation defect: mixed numeric lists containing booleans are accepted despite the documented rejection of booleans. I found no required mathematical correction in Sections 1–9. The new frozen-quadratic formulas, physical clock, simultaneous update, and interpolation interpretation are correct within their stated scope.

All 13 supplied tests pass. The guide example passes. The independent algebra and derivative checks described below pass, apart from the deliberate reproductions of the validation defect. Every packet input is unchanged.

The required correction is:

1. **Reject boolean elements before mixed-sequence coercion, and add regression coverage.** In [_frozen_state](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py:277), `np.asarray(value)` runs before the dtype check. Consequently, `[True, 2]` becomes an integer array and `[True, 0.5]` becomes a floating array. Both pass validation. This contradicts [the guide’s input contract](/tmp/pde_assembly2_frozen_r1/code/README.md:28). The [input-validation test](/tmp/pde_assembly2_frozen_r1/code/tests/test_finite_reductions.py:313) covers a homogeneous boolean vector, which retains boolean dtype, but misses mixed sequences. Preserve enough information to reject Python and NumPy boolean elements in supplied mixed sequences, and test both vector arguments through both public APIs. Already numeric NumPy arrays need no reconstruction of their earlier provenance.

The following calls currently succeed:

```python
frozen_quadratic([True, 2], [1, 1], 1).output
# 0.8660254037844388

frozen_quadratic([1, 2], [True, 0.5], 1).output
# 0.4330127018922194

frozen_quadratic_step([True, 2], [1, 1], 1, 0.01)
# Returns updated arrays instead of rejecting the boolean.
```

I also reproduced acceptance of a mixed list containing `np.bool_(False)`. This is a minor implementation-contract defect; it does not invalidate the mathematical results.

The review was performed independently, without delegation. I read only the manifest-listed files as mathematical/code inputs, plus the expressly requested instruction files. I did not consult another checkout, packet, previous verdict, task history, or external source. All diagnostics ran inline; no packet file was edited.

I personally read the complete requested instruction files:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`
- `/etc/codex/skills/investigate-conjectures/SKILL.md`
- Its `references/research-contract.md`, `references/evidence-ledger.md`, and `references/adversarial-audit.md`.

The complete packet read and integrity record follows. The hash column gives **both independently computed values: before review and after all checks**. They were identical. Every listed file also matched its manifest hash, byte count, and line count in both passes.

| File | Lines read completely | Bytes before/after | SHA-256 before = SHA-256 after |
|---|---:|---:|---|
| [INPUTS.json](/tmp/pde_assembly2_frozen_r1/INPUTS.json) | 1–47 | 1,388 / 1,388 | `377e0945d0f8e3ed8429fc9e3fc04df7fc7d1a5cf51f367f986c7ab16e6514f1` |
| [docs/NOTATION.md](/tmp/pde_assembly2_frozen_r1/docs/NOTATION.md) | 1–98 | 5,110 / 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| [code/pde/__init__.py](/tmp/pde_assembly2_frozen_r1/code/pde/__init__.py) | 1–26 | 611 / 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| [code/pde/finite_network.py](/tmp/pde_assembly2_frozen_r1/code/pde/finite_network.py) | 1–363 | 15,525 / 15,525 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| [code/pde/gaussian_moments.py](/tmp/pde_assembly2_frozen_r1/code/pde/gaussian_moments.py) | 1–114 | 4,464 / 4,464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| [code/pde/finite_reductions.py](/tmp/pde_assembly2_frozen_r1/code/pde/finite_reductions.py) | 1–342 | 15,309 / 15,309 | `1af9d5b2d4517355ddee9410e75007e31ff7aa732720153c5e60b61a8804fcbc` |
| [code/tests/test_finite_reductions.py](/tmp/pde_assembly2_frozen_r1/code/tests/test_finite_reductions.py) | 1–333 | 18,170 / 18,170 | `6445164cfb700bb0da053058c16e45524933e4a0c12fc6cf9b426916c87dbc17` |
| [requirements.txt](/tmp/pde_assembly2_frozen_r1/requirements.txt) | 1–2 | 111 / 111 | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |
| [docs/finite_dynamics.md](/tmp/pde_assembly2_frozen_r1/docs/finite_dynamics.md) | 1–1268 | 48,114 / 48,114 | `f9bc305b6c438d87a81cb25407a44b7a2109ef29413a1fb6023505ad327641bb` |
| [code/README.md](/tmp/pde_assembly2_frozen_r1/code/README.md) | 1–42 | 2,363 / 2,363 | `9480d7300646f1fff81501954b767f86bca606dcadc7cdb2fe27ba0d08baad77` |

The nine listed inputs total **109,777 bytes and 2,588 lines**, excluding the manifest.

The notation and model distinctions are internally consistent. The first layer uses \(x/\sqrt d\), stored hidden matrices act without another width normalization, and the stored readout is divided by \(n\). Backward vectors exclude the residual. Ordinary Euclidean/Frobenius norms and the stated mobility metric produce the displayed normalized pairings.

The initialization distinctions are preserved: the general small-readout initialization has stored-readout variance \(1/n^2\); Sections 8–9 explicitly use variance one. Sections 5–7 require no distributional initialization. The general loss is the mean full square; Sections 8–9 and the new APIs use the half square. Thus the full one-sample loss runs the same gradient-flow path twice as fast, and its Euler step \(\eta\) corresponds to half-loss step \(2\eta\). Feature ascent in Sections 5–7 and 8.2 is an algebraic vector field and does not assume a globally valid positive feature clock.

For **Sections 1–4**, I checked the derivative and energy foundations used downstream. Differentiation gives the first-layer factor \(1/(n\sqrt d)\), middle-layer factor \(1/n\), and readout factor \(1/n\). Applying endpoint mobilities \(n\kappa\) and middle mobilities \(\kappa\) yields equation (2), including its \(2/m\) loss factor. Every GD block uses the same old state.

The kernel blocks are the weighted Gram matrices of these output derivatives. Their positive semidefiniteness follows directly from the squared norm of a linear combination of weighted gradients. Consequently,
\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr
=-\|D^{-1/2}\dot\theta\|^2.
\]
The integrated energy identity and Cauchy–Schwarz give the stated square-root displacement modulus.

The global finite-width existence argument is complete: \(C^2\) activations give a locally Lipschitz finite-dimensional vector field; local contraction gives existence and uniqueness; finite initial loss and energy dissipation make the parameters Cauchy at any proposed finite maximal endpoint; the positive fixed-width metric is equivalent to Euclidean distance; local existence at the resulting finite state extends the solution.

The width-uniform bounds correctly require bounded activation derivatives, fixed depth/data, bounded initial normalized parameter norms, and bounded initial loss. Forward and backward norm inductions establish the claimed RMS and kernel-entry bounds. The Gaussian initialization event follows from Gaussian-square concentration and the displayed finite-net operator-norm estimate. These arguments do not supply uniform coordinate bounds, unbounded-multiplier control, a population identification, or arbitrary-step GD stability. In particular, the bounded-derivative width estimate is not silently applied to quadratic activations.

For **Section 5**, the QI, IQ, and QQ vector fields and metric factors agree with direct differentiation. In QI, \(q=B^Ta\) gives \(u'=2u\odot q\), \(B'=ah^T/n\), and \(a'=z\). In IQ and QQ, \(b=a\odot z\), \(q=B^Tb\), \(B'=2bh^T/n\), and \(a'=z^2\); the first-block fields are respectively \(2q\) and \(4u\odot q\). Squaring these fields in the stated metric gives all three kernel tables and the full-square physical energy identities.

The Lax constructions use the correct isometry \(v\mapsto v/\sqrt n\). QI satisfies \(\mathsf Q'=\mathsf QS\) and \(\mathsf L'=[\mathsf L,S]\); IQ satisfies \(\mathsf P'=2S\mathsf P\) and \(\mathsf L'=2[\mathsf L,S]\). The signature anticommutation supplies the signs. The stated output and kernel reconstructions retain the required orientation information.

The isospectrality proof correctly uses similarity, without assuming self-adjointness. The equations for \(U\) and its inverse have continuous bounded coefficients on each compact solution interval, and differentiation of \(U^{-1}\mathsf LU\) proves constancy. The orientation witness has equal output \(1/3\), orthogonally similar Lax matrices, and kernels \(68/9\) and \(28/3\). It therefore defeats the specified spectrum-plus-current-feature/output state. It does not defeat the full operator state. The QQ row and column balances have the correct coefficients \(2a_i^2\) and \(u_j^2/2\).

For **Sections 6–7**, both RMS denominators are differentiated. The normalization derivative
\[
DN_\varepsilon(x)=\sigma^{-1}
\left(I-\frac{N_\varepsilon(x)N_\varepsilon(x)^T}{n}\right)
\]
has the claimed positive eigenvalues for \(\varepsilon>0\). The matrices called \(\Pi\) are correctly described as generally non-idempotent.

The backward fields \(c=a-fv\), \(b=2z\odot c/\beta\), \(q=B^Tb\), and \(\widetilde q=\Pi_hq\) give the full differential, ascent fields, and kernel blocks. I checked every displayed feature derivative, the contraction
\[
h^Tq/n=z^Tb/n=2\varepsilon f/\beta^2,
\]
and both signed balance drifts. The residual exponential formula follows from its scalar linear equation and includes zero initial residual.

The reduced state \((a,h,E)\) is correctly restricted to the stated domain. On raw-image states, \(h\ge0\) and \(\|h\|^2/n<1\), so \(\alpha(h)\) is finite and the reduced first-layer operator is positive semidefinite. Recovering \(u_j^2=\alpha(h)h_j\) gives a valid raw lift. Different choices of nonzero signs project to the same locally unique reduced solution. The raw energy argument supplies global physical continuation from reached states. No continuation on the boundary \(\|h\|^2/n=1\), global feature-ascent result, or width-independent operator construction is asserted.

For **Section 8.1’s exact frozen reduction**, freezing \(h\) gives
\[
\nabla_a f=\frac c n z^2,\qquad
\nabla_W f=\frac{2c}{n}(a\odot z)h^T.
\]
With half-square loss and mobilities \(n\) for the readout and one for the connector,
\[
\dot a=-rcz^2,\qquad
\dot z=-2rcQa\odot z.
\]
Multiplying the simultaneous raw connector update by the unchanged \(h\) proves equation (8.1) exactly. There is no continuous-flow approximation in that reduction.

The connector and readout kernel blocks are
\[
K_W=\frac{4c^2Q}{n}\sum_i a_i^2z_i^2,\qquad
K_a=\frac{c^2}{n}\sum_i z_i^4.
\]
Their sum gives \(\dot f=-rK\) and \(\dot\ell=-r^2K\). When \(Q=0\), the raw state necessarily has \(h=z=0\), and these velocities and kernel blocks vanish. For \(Q>0\), any specified \(z\) has the raw realization
\[
W=\frac{zh^T}{nQ}.
\]
These facts justify the reduced API’s state variables and its zero-\(Q\) constraint.

For **Section 8.1’s joint initial-layer theorem**, the proof is complete for its stated frozen Gaussian model and every deterministic positive sequence \(\eta_n\to0\). It imposes no monotonicity of that sequence and no rate relation to width.

Conditioning on the frozen bottom vector gives independent Gaussian rows, with independent readout and preactivation coordinates. The initialization calculations are correct:
\[
\mathbb E Q_n=1,\qquad
\operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
\mathbb E(f_n^0)^2=\frac1n\left(1+\frac{32}{3n}\right).
\]
The last identity uses centered independent readouts to eliminate cross terms. No independence between trained rows is subsequently assumed.

On survival below the output threshold, \(s_k\) is bounded above and below by positive multiples of \(\eta_n\), and every readout coordinate increases. A row still having negative readout must have been negative at all earlier steps. The bound on its preactivation multiplier remains valid even if a large individual Euler multiplier changes sign:
\[
|1-2cQ_ns_k|a_i^k||\le
\exp(2cQ_ns_k|a_i^k|).
\]
This yields equation (8.6), controlled entirely by initialization, without a step-count union bound or a hidden maximum-coordinate step restriction.

The negative-row envelope has uniformly bounded conditional second moment on \(Q_n\in[1/2,2]\). Gaussian exponential integrability and conditional Chebyshev therefore establish one initialization event that controls all negative contributions throughout survival.

The favorable block has fixed positive Gaussian probability \(p_b\). Its row count concentrates conditionally. Positive selected coordinates remain positive and dominate
\[
y^{k+1}\ge y^k+\gamma\eta_n(y^k)^2.
\]
The reciprocal estimate is valid while the comparison variable is below fixed \(M\) and \(\gamma\eta_nM\le1\). It gives the stated common hitting-time bound. Choosing \(b\) first from \(T,\delta\), then \(M\) from \(p_b,B_T,\delta\), fixes both independently of \(n\). Eventually the sole comparison-step condition holds because \(\eta_n\to0\). The resulting favorable contribution exceeds the negative envelope, contradicting survival.

Thus the proof establishes the claimed hitting-time convergence in probability. Its use of a possibly very rare but fixed tail block affects how large \(n\) must become; it does not invalidate the asymptotic quantifiers.

The interpolation conclusion is also justified. With frozen \(h\), raw linear interpolation makes \(a\) and \(z\) linear within each cell, while the predictor is recomputed from them. Continuity forces a crossing of \(+\delta\) or \(-\delta\) before the first grid hit. At that crossing the output change is at least \(\delta/2\) on the stated initialization event, and the loss differs from \(1/2\) by at least \(\delta-\delta^2/2\). Uniform convergence in probability to a continuous initialized path would force these changes to vanish. The argument remains valid for a random continuous proposed limit through its samplewise modulus of continuity.

This establishes the frozen model’s obstruction. It supplies no arbitrary-joint-step theorem for fully trained quadratic networks.

For **Section 8.2**, the one-step comparison counterexample is algebraically correct. With \(f=aw^2u^4\), the raw-square ascent fields are exactly those in (8.10). The chosen state satisfies \(w^2u^2=R\), \(w^2u^4=\rho\), and
\[
u^+/u=-1-4\varepsilon.
\]
The frozen and full steps have identical updated \(a,w\), but the full output is \((1+4\varepsilon)^4\) times the negative frozen output. It is therefore strictly smaller. The conditions on \(\rho\) can be imposed simultaneously and keep the initial and both terminal outputs within the prescribed threshold interval.

The scope is stated correctly: this defeats the proposed universal pathwise lower comparison, for states depending on the step. It is not a typical-Gaussian-trajectory assertion. Both states initially have the same residual, so the comparison also uses a common physical half-loss step \(\eta=s/(1-f)\). Adding a nonnegative kernel contribution at one common state does not establish an ordering of subsequently different trajectories.

For **Section 9.1**, the reached ReLU obstruction is complete, including the distinction between an isolated contact example and an open set of initial conditions that reaches such a contact.

At the displayed contact, \(h=(c,c)\), \(z=(0,2)\), \(f=1/4\), and
\[
WW^T=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]
The first normal velocity is
\[
\dot z_1=\frac34(4a_1v+2a_2c).
\]
This gives the stated negative-side velocity \(p=3/8>0\), positive-side velocity \(q=\frac34(1/2-4\lambda)<0\), and prescribed contact velocity \(v_0\). For every fixed finite \(\sigma\), choosing \(\lambda>1/8\) while avoiding at most one value makes \(v_0\ne0\). Continuity within each adjacent cell and along the gate gives the uniform local inequalities (9.3).

The noncontinuation argument uses only valid absolutely continuous calculus. If a continuation starts at contact, \(w=|z_1|\) is absolutely continuous, has derivative at most \(-\gamma\) where positive, and has derivative zero almost everywhere on its zero set. Integrating forces \(w\equiv0\). Then \(z_1'=0\) almost everywhere, contradicting the prescribed nonzero normal component on the gate.

The reachability argument supplies an open set on the positive side. The normal velocity is uniformly inward, other gates remain away from zero, and bounded parameter speed prevents exit from the chosen ball before contact. Smooth local ODE existence applies inside that sign cell. The independent width-two Gaussian law has positive density throughout parameter space, so the open set has positive probability.

The result excludes absolutely continuous continuations satisfying the prescribed pointwise field almost everywhere. It does not exclude differential-inclusion solutions with another selection rule, and it asserts no width-uniform probability bound.

For **Section 9.2**, the positive local Euler-output compactness theorem is valid with \(|\sigma|\le\sqrt2\), all three blocks trained, the specified order-one readout initialization, and half-loss time.

The forward and backward RMS bounds give \(|f|\le2R^3\), \(|r|\le3R^3\). Each parameter increment in its designated norm is at most \(6\eta R^5\), including the connector through its rank-one operator norm. Therefore \(R^+\le R+6\eta R^5\).

The bootstrap constants close exactly:
\[
6+6T_*12^5=12,\qquad
T_*=\frac1{192\cdot6^4}=2T_0.
\]
The initialization event has probability tending to one. The matrix-net tail decays because \(\log81<9/2\); the first and readout bounds follow from Gaussian-square variance \(2/n\).

For all sufficiently large \(n\), the endpoints required to interpolate through \(T_0\) lie within \(T_*\). Convexity preserves the parameter norm bounds along raw interpolation. ReLU Lipschitzness and product differences give the displayed feature and output moduli. The intermediate output estimate \(36S^7|t-s|\) is safely bounded by the chosen \(60S^7|t-s|\). None of this requires differentiability at a gate or discrete energy dissipation.

The uniformly bounded, uniformly Lipschitz output set is compact in the uniform topology. The continuous half-loss map gives compactness for the pair. The finite-prefix argument correctly upgrades asymptotic tightness to tightness of the whole sequence, even when the early step sizes are large: each such width has finitely many steps, and bounded initial parameters give finite bounds through the scalar recurrence.

The probability-measure weak compactness theorem is explicitly invoked on the complete separable continuous-path space. This is a legitimate stated theorem dependency. The Euler maps are measurable under the fixed gate convention.

The initialization identity \(\mathbb E F_n(0)^2=1/n\) is correct. Continuous evaluation at zero then fixes every subsequential limit’s traces at \(0\) and \(1/2\). The loss relation persists under uniform convergence.

The alternative interpolations are also handled correctly. Grid predictor interpolation differs from the raw-recomputed predictor by \(O(\eta_n)\) on the common high-probability event. For grid outputs \(x,y\), the exact difference between interpolated losses and the loss of the interpolated output is
\[
\frac{\lambda(1-\lambda)}2(x-y)^2,
\]
hence \(O(\eta_n^2)\). These estimates establish the claimed equivalence of the interpolation variants.

The proven horizon is precisely
\[
T_0=\frac1{497664}\approx2.00938786008\times10^{-6}
\]
in half-loss physical time. The theorem gives subsequential distributional compactness of scalar outputs and losses on this local interval. It does not establish deterministic limits, uniqueness, parameter-state compactness, tangent-kernel convergence, a limiting loss-dissipation law, or continuation beyond this horizon.

For **Section 9.3**, the frozen gate calculation correctly retains occupation information. The half-open strip \(\eta q<z\le\eta p\) is invariant under the stated convention at zero. Every initial point enters it after finitely many steps. Inside the strip, the change of variable gives
\[
x_{k+1}=x_k+\lambda-I_k,\qquad
\lambda=\frac p{p-q},
\]
including contact with zero. Telescoping yields
\[
\left|\sum_{k=j}^{j+N-1}I_k-N\lambda\right|
=|x_j-x_{j+N}|<1.
\]

The occupation assertion is a time-average, or weak-in-time, assertion; it does not assert pointwise convergence of binary gates. A gate initialized in the strip has uniformly \(O(\eta)\) position while its average occupation approaches \(\lambda\). Since \(I^r=I\), all positive integer gate moments have that same average. Replacing the gate by its mean changes its second moment to \(\lambda^2\).

For \(p=-q\), the two phase examples correctly give marginal occupations \(1/2\) with average joint products \(1/2\) or zero. These examples establish that marginal occupation alone does not determine joint occupation. The text expressly limits them to frozen scalar examples and does not claim their reachability in the random network. Their relevance to squared backward fields and reused transpose contractions does not itself identify a neural-kernel limit.

The final scope separation is valid: classical noncontinuation does not rule out continuous scalar Euler subsequences, and output compactness does not uniquely identify a generalized population flow.

For the **implementation audit**, I checked the complete supplied Python, including the earlier interfaces used by the reduction tests.

`finite_network.py` implements the documented layer normalization, activation dispatch, backward recursion, loss factors, mobility factors, kernel blocks, and simultaneous raw update. `Parameters` validates dimensions and finiteness while deliberately retaining array ownership as documented. Activation evaluations copy callback arguments and outputs, protecting cached fields from callback buffer mutation. `initialize` uses a local seeded generator and the stated standard deviations \(1\), \(1/\sqrt n\), and \(1/n\). This initialization is not silently invoked by the frozen APIs.

The loss-gradient contractions, physical-block scaling, and raw kernel factors match the mathematics. The mantissa/exponent helper improves range handling for products and updates; it does not make preceding matrix contractions arbitrary-range exact. Nothing in the new routines relies on such a stronger guarantee. The core’s default full-square clock is distinct from the new half-square clock.

The existing mixed and RMS evaluators match Sections 5–6. Their field derivatives, balance arrays, output/loss velocities, and kernel ordering are correct. `mixed_lax` includes the IQ factor two in its generator, as documented. Returned reduction arrays are copied or freshly constructed. The existing finite models remain separate from the frozen model.

`gaussian_moments.py` correctly validates square symmetry, rational entries, nonnegative integer powers, and positive semidefiniteness before handling zero or odd total degree. Its exact Schur-complement test handles both positive pivots and the necessary zero-row condition at a zero pivot. The moment recurrence removes one selected factor and pairs it with each remaining factor with the correct multiplicity. It agrees with the coefficient recurrence from the centered Gaussian generating function, including singular covariance. Cache lifetime, stated state-count bound, and recursion-depth limitation are consistent with the implementation.

`__init__.py` imports and exports the supplied core and moment routine. The guide imports reductions explicitly from `pde.finite_reductions`; no top-level export of the new APIs is promised or needed. The source imports require only the standard library, NumPy, and the supplied relative modules. `requirements.txt` pins NumPy 1.26.4, which matches the execution environment.

For **FrozenQuadraticEvaluation**, the eight fields accurately represent the evaluated state and physical velocities. The two kernel blocks are in connector/readout order, although equation (8.2) writes their sum in the opposite textual order. The guide explicitly defines the API order, so there is no inconsistency. The absence of a separate `kernel` field is consistent with the guide’s instruction to sum `kernel_blocks`. Array fields are fresh and caller-owned; the frozen dataclass does not imply that their contents are immutable.

For **_frozen_state**, the shape, equal-length, nonempty, finiteness, float64-copy, and \(Q\)-realizability checks are correct, subject to the boolean defect already identified. Nonfinite values introduced by conversion are checked again. The exact \(Q=0\Rightarrow z=0\) restriction is mathematically necessary. For \(Q>0\), imposing an additional relation between \(a,z,Q\) would be unjustified.

For **frozen_quadratic**, the implementation calculates \(c=1/\sqrt3\), \(f=c\,a^Tz^2/n\), residual \(f-\text{label}\), and half-square loss. Its two vector velocities and two kernel blocks match the raw derivatives above. `output_velocity=-residual*kernel` and `loss_velocity=-residual**2*kernel` have the correct half-loss factors. Labels are independently validated. Zero residual stops both parameter velocities while permitting a positive kernel.

The evaluator does no initialization and does not freeze a newly recomputed first layer behind the caller’s back. It operates on the supplied \(a,z,Q\). Its intermediate float64 range restrictions, finite-result rejection, and allowance for rounding and underflow are expressly documented. I found no additional range-contract defect within that stated limitation.

For **frozen_quadratic_step**, `eta` is validated as finite, real, and nonnegative. Both increments use a single evaluation of the old state. Because \(h\) is frozen, the returned preactivation equals the preactivation induced by the simultaneous raw connector update. Returned arrays do not alias the supplied arrays. The step evaluates the kernel and other fields even at zero step; the documented representability requirement covers that behavior. Repeated validation/copying changes constants but preserves the claimed \(O(n)\) work and storage.

The step supplies one Euler update. It makes no unsupported claim of finite-time flow exactness, energy decrease, numerical stability, or population approximation.

The **test audit** found meaningful coverage across all 13 tests. The four mixed-model tests cover core agreement, Lax chain rules and orientation, and QQ balances. The four RMS tests cover coordinate gradients, differentiated fields, physical energy, signed balances, the sign quotient, and degeneracies. The shared contract test checks model scope, input validity, ownership, and mutated nonfinite parameters.

The four frozen tests differentiate the unreduced raw connector/readout output and half loss, construct mobility-weighted kernel blocks, compare simultaneous raw updates, check recomputed interpolation, test zero feature and zero residual, and exercise ownership and range rejection. Their finite-difference denominators correctly account for the half loss. Their missing mixed-boolean cases explain why the supplied suite passes despite the required correction. These tests validate finite calculations; they do not serve as empirical proof of the joint-limit or compactness theorems.

The **guide audit** found its model, trained blocks, activation scale, loss convention, kernel order, old-state update rule, raw-interpolation explanation, complexity claim, and scope limitations correct. Its numerical example executes as written. Its blanket boolean-rejection statement is the contract violated by the implementation and is covered by required correction 1.

The requested execution used exactly:

```text
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_reductions
```

Observed result:

```text
.............
----------------------------------------------------------------------
Ran 13 tests in 0.107s

OK
```

The runtime was Python **3.10.12**, NumPy **1.26.4**. I extracted and executed the guide’s actual fenced Python example. Both assertions passed. Its evaluated output was `0.004618802153517007`, its loss was `0.4953918645131497`, and its updated coordinates were approximately:

```text
next_a = [ 0.30091949, -0.79977013]
next_z = [ 0.40096547, -0.19871271]
```

The additional independent checks were bounded algebra/derivative checks, with no training or trajectory simulations:

| Independent check | Construction and result |
|---|---|
| Gaussian moments | **147 exact comparisons** against independent binomial expansions for nonsingular, singular, and zero-coordinate covariance examples, with powers 0–6 in each coordinate. All passed. |
| PSD rejection | **Six checks** of invalid covariance matrices at zero and odd total degree. All were rejected before trivial-degree shortcuts. |
| Initialization constants | Independently verified Gaussian moments \(3,105\) and variance coefficient \(32/3\). Passed. |
| General core interfaces | A fixed width-two, depth-three, two-input-coordinate example with three correlated samples, a singular sample Gram, mixed activations, and nonunit mobilities. Checked **14 raw-coordinate loss gradients**, **18 preactivation derivatives**, all four kernel blocks, full-loss clock, physical energy, and one simultaneous update. Passed. |
| Core derivative errors | Maximum raw loss-gradient absolute error: `2.271702270739695e-11`. Maximum kernel-block absolute error: `1.21488374915657e-11`. |
| Frozen raw derivatives | Independently differentiated **28 raw connector/readout coordinates** across widths 1, 2, and 4, using an unreduced scalar-loop output definition. Checked both velocities, both kernel blocks, and half-loss energy. Passed. |
| Frozen reduction and interpolation | Checked raw connector lifts, one-step endpoints, four interpolation fractions per width, and \(Q=0\) with a nondefault label. Passed. Maximum frozen finite-difference comparison error: `2.0643400183706362e-11`. |
| Deletion counterexample | Exact rational one-step checks at \(s=1/100,1,100\), including strict output-order reversal and all outputs inside \((-1/10,1/10)\). Passed. |
| ReLU contact geometry | Direct raw normal-velocity checks at five prescribed kink values, including the need to avoid a zero-contact-normal choice of \(\lambda\). All side and contact signs passed. |
| Compactness constants | Exact rational verification of the bootstrap identity and **eight** grid-loss interpolation identities. Passed. |
| Gate identities | **Eight exact one-step strip/occupation checks**, including contact and the upper boundary, plus the complementary half-strip phase identity. Passed without trajectory runs. |
| Boolean contract | Three mixed-boolean input families were accepted by `_frozen_state`, the evaluator, and the step. This reproduced required correction 1. |

One diagnostic status line initially mislabeled the general-core coordinate count as 16. The executed loop covered all 14 coordinates—three \(2\times2\) matrices and one length-two readout—and the count was explicitly corrected in the subsequent diagnostic output.

The proof-dependency audit found no missing nontrivial bridge within the claims actually made. The arguments use finite-dimensional differentiation, absolute-continuity calculus, contraction-based local existence, energy continuation, elementary Gaussian moments and tails, Chebyshev concentration, compactness of uniformly bounded equicontinuous paths, and the explicitly stated weak compactness theorem for tight probability laws on the continuous-path space. The relevant hypotheses are satisfied where these tools are used. No unstated population-limit, kernel-identification, generalized-flow-selection, or fully trained quadratic comparison theorem is needed for the displayed conclusions.

The final scope is therefore precise: the finite identities and new numerical formulas pass; the frozen Gaussian arbitrary-joint-step obstruction passes; the deterministic deletion counterexample passes; the reached width-two ReLU noncontinuation proof passes; and the positive ReLU result establishes local scalar output/loss tightness with the stated initialization and interpolation variants. Identification, uniqueness, broader horizons, kernel convergence, and the fully trained quadratic arbitrary-step problem remain outside the established claims. The packet requires the single boolean-validation correction above, and all inputs remain unchanged.