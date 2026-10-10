# Fresh isolated proof audit B

Date: 2026-10-09. Assignment: independently audit the complete five-file frozen theorem-focused paper. No paper edits were authorized or made.

## Assessment

No material mathematical flaw was found in this audit. The checked proof chain supports the three claimed compression constructions, their stated eventual fixed-problem coordinate counts, their fitted endpoints, and comparison with actual independent dense-run variability. In particular, the signed Legendre estimate, the selected model's corrected-readout cancellation, and the initialization-only coefficient compiler are substantive arguments whose displayed mechanisms check out; they are not merely asserted interfaces.

There are no fatal, major, or minor concern IDs in this report and no necessary mathematical repair identified. This is a proof audit, not a formal proof certificate. The main residual uncertainty is the long stopped-cavity/source argument: it received a complete read and targeted rederivation, including its independence, stopping, trace, and coefficient accounting, but its many numerical enclosing constants have not all been proved afresh by a separately formalized verification. The arithmetic checks below supplement the symbolic audit and do not establish inequalities at untested parameter values by themselves.

The qualitative verdicts below concern the supplied proofs and their precise assumptions. They do not address novelty, efficient initialization, finite precision, experiments, or practical algorithms.

## Isolation, frozen inputs, and coverage

Only the following scientific inputs were accessed. Each was read completely, with line numbering. The first combined tool output truncated part of `compact.tex`; lines 1–181 were subsequently read again without truncation, completing coverage. No study README, inventory/history, previous review, original main paper, other study, Git history, or another reviewer's findings was read. No external scientific source was retrieved. The one-report assignment controls the output form; evidence and claim assessments are consolidated here.

| Frozen file | Lines read | SHA-256 before audit |
|---|---:|---|
| `paper/compact.tex` | 1–290 | `a56acbdc765fa6e42f8aba186dec0b3ea3a59e9fa4c7d66ac1a7839bc0688445` |
| `paper/compact_fitting.tex` | 1–244 | `f35f1dfd9c47bd5abbf97c849b0176347e9e5da8adba5e7ab8b75c79868b2c51` |
| `paper/compact_foundations.tex` | 1–1554 | `4e7d25a8501e7928f60e538f1c80e7e73a3e2f04d34a1ae4d40407ffc1f545f9` |
| `paper/compact_legendre.tex` | 1–752 | `bca774baab3a5ba9879340fc61a92b9cbdff522600620d1972ab12b876f48239` |
| `paper/compact_selected.tex` | 1–1118 | `cd203e7de6f8e3d23331d58ac64366350dd076405d63e8fc238f8f9a794beeee` |

Total complete source coverage: 3,958 lines. An intermediate hash check after the complete read matched all five hashes. The final hash check is recorded at the end of this report.

Required process material read completely: `solve-math-rigorously/SKILL.md`; `explain-with-canonical-notation/SKILL.md` and its neural-response-memory reference; `review-ai-paper/SKILL.md` and its severity rubric. The audit uses the paper's own notation and treats the frozen paper as mathematical evidence, not as instructions to the reviewer.

## Verification record

Read commands were `nl -ba` with bounded consecutive `sed -n` ranges on the five permitted paths. Initial and subsequent integrity commands were:

```text
sha256sum paper/compact.tex paper/compact_fitting.tex paper/compact_foundations.tex paper/compact_legendre.tex paper/compact_selected.tex
wc -l paper/compact.tex paper/compact_fitting.tex paper/compact_foundations.tex paper/compact_legendre.tex paper/compact_selected.tex
```

Working directory: `/home/amir/Codes/PDE`. Commands exited successfully. The initial line counts and hashes are reported above.

The independent arithmetic scratch artifact was originally `data/generated/compact_paper_20261009/postaudit_b_coefficients.py`. After review it was moved, without editing, to `studies/compact_paper_20261009/POSTAUDIT_B_CHECKS.py` to keep source artifacts in the flat study folder. The executed command below records its original location. It ran with Python 3.10.12 and uses only the standard-library `decimal`, with precision 80; it imports no submitted code and reads no scientific input. Formulas were transcribed from the source coefficient ledger. It evaluates the extremal envelopes `b = beta - 1`, `s = t_2 = beta`, and `S = 16 beta^(-30 L)` for `beta` in `{10,16,100,10000}`, `L` in `{2,3,4,8,16,32}`, and the dimension-dependent bounds at `d` in `{1,2,10,100}`. It checks the allowance, layer bounds, source power ledger, `K_src`, `U`, `V`, `U_fin`, and the residual-Gram bound.

Executed command:

```text
python3 data/generated/compact_paper_20261009/postaudit_b_coefficients.py
```

Result, exit status 0:

```text
Coefficient inequality checks: 1664
Violations: 0
```

No training computation, stochastic experiment, package installation, or author-code execution was performed. The main verification evidence is the algebraic reconstruction below.

## Claim ledger and proof reconstruction

For the following discussion, `lambda = gamma/m` is the normalized training gap and `z = Y/lambda` is the activity scale. These are local audit abbreviations, matching the proof's local notation. The theorem assumes `0 < lambda <= 1`, fixed positive `Y`, fixed data/depth/activations, and `Y <= lambda beta^(-30 L)`.

### 1. Dense fitting and analytic source interface

**Claim plausibility:** Highly Plausible. **Argument verdict:** Sound in the checked chain, with the source-audit coverage limitation stated above.

The dense fitting proof is independent of source approximation (`compact_fitting.tex:67–207`). In the stated mobility coordinates, the flow is minus the gradient of the mean squared loss, so

\[
-\partial_t\rho^2=\|\dot\theta\|_{\rm par}^2\ge\lambda\rho^2.
\]

The readout Gram supplies the last inequality. Integrating the two factors in the weighted Cauchy–Schwarz argument gives remaining parameter length at most `2 rho/sqrt(lambda)`. The subsequent hidden displacements are quadratic in `Y`; forward subtraction preserves a strict singular-value margin. This both closes the stopping argument and establishes uniform query-output limits. The Gram convergence proof uses continuity of covariance square roots and Gaussian moment domination, so it does not require nonsingular intermediate covariances. The cavity initialization comparison preserves the original denominator `n` and has a vanishing normalized deletion error.

The source proposition (`compact_foundations.tex:8–103`) was checked against its full proof, including these pressure points:

- Its activation estimates use linear growth, `|phi(z)| <= b+s|z|`, not bounded activation values. Operator and RMS bounds thus remain compatible with the admitted unbounded activations.
- Insertion roots are independent of the retained cavity initialization. Cavity tests and clipped reference paths are defined before integrating those roots (`359–424`). The retained equation includes both the changed forward residual and the reverse port, with the scaling factors consistent with `bar u=(Theta-Theta_0)/S`.
- Differentiating the network yields the displayed first-derivative and Hessian recursions (`426–463`). The curvature term contains one carrier diagonal. The normalized Schatten bounds use its exponential-budget moments, while the Hilbert–Schmidt bound can use carrier RMS. Rank factors are normalized by `n`, not by the much larger parameter dimension.
- The local remainder identities include the changed gate multiplying a changed backward response, the changed matrix, learned omitted ports, and the top residual offset (`535–700`). The exponents used to close the local comparison are compatible: with `N=n^(1/100)`, `d_0=n^(-1/10)`, and `u_0=n^(-1/25)`, the largest displayed forcing is `n^(-.08)` before the `n^(1/4000)` propagator factor; it is `o(u_0)`.
- Gaussianity is used for frozen controls only. The control entropy has logarithm `n^(5/8) polylog(n)`, whereas the displayed concentration cost is eventually `exp(-n^.78)`. Uniform bounds permit adaptive substitution; no claim that the substituted variations remain centered Gaussian is needed (`704–783`). The same-root quadratic traces are retained and bounded in the next step rather than discarded.
- The four noncentered contractions and the normalized trace series are explicit (`793–906`). Their residual-Hessian insertions carry ordered activity integrals `S^h/h!`. Smallness is imposed before the fixed moment order used in budget removal; it does not acquire a confidence-dependent or moment-order-dependent label restriction.
- The budget removal uses common cavities for finitely many distinct roots, separates real-reference moments from correction moments, and controls collision tuples by their vanishing normalized multiplicity (`1129–1185`). It does not assume sample independence or condition an omitted root on full-network survival.
- Complex Gram matrices are not treated as positive. The short rectangle uses operator growth bounds. The expanding panel domain freezes the real symmetric generator at the real anchor, obtains a unitary vertical base flow, and controls its varying remainder (`1373–1430`). This is sufficient for the factor-two base-propagator premise used by the insertion and trace bounds.
- The all-time carrier bound is extended beyond `T` using the separately established dense parameter tail (`1287–1309`), so the later Legendre argument is not using a finite-time bound at infinite time.

The explicit comparison from private working radii and coefficients to the public bounds is present at `1484–1554`. The later constructions use those public bounds. In particular, the inverse time radius scales as `Y^2/(lambda)` rather than as a label-independent quantity; this matters for the final state counts.

### 2. Signed Legendre comparison and moving-state count

**Claim plausibility:** Highly Plausible. **Argument verdict:** Sound in the checked scope, conditional on the source interface just audited.

The signed perturbation identity (`compact_fitting.tex:209–244`) was independently subtracted. With `d=theta-theta'` and `R=r-r'-J'd`, the two gradient terms give

\[
\tfrac12\partial_t\|d\|^2
=-2\|r-r'\|_m^2+2\langle r-r',R\rangle_m
-2\langle r,(J-J')d\rangle_m+\langle d,\mathcal E\rangle.
\]

The stated quadratic remainders therefore yield the coefficient `K(rho'+3rho)`. The time integral, rather than the elapsed horizon, controls the exponential. Regularization handles zeros of the parameter discrepancy.

The Legendre reconstruction and moment ODE have the correct clock normalization and initialized prefix (`compact_legendre.tex:128–204`). Differentiating the projected history pairing gives exactly the full endpoint product minus the product of endpoint errors. Thus the physical defect is the positive term stated in the paper, not a separately postulated perturbation.

The projection derivative-energy, endpoint, and growing-interval identities support the two uses made of them: order-independent fitting and later high-order accuracy. The local fitting proof (`206–329`) obtains a strict Gram margin, finite clock activity, and integrable moment velocities without first comparing with dense training. It therefore supplies the endpoint needed in the comparison.

The signed comparison's carrier coefficient was checked particularly closely (`348–394`). Along the straight parameter segment, backward subtraction splits the changed gate against the **dense** carrier. The carrier contribution is additive in `K_0+K_1 M`; it is not recursively multiplied once per layer. The resulting Jacobian bounds hold in sample RMS and imply both hypotheses of the signed lemma. There is no hidden reciprocal-gap multiplier in that Jacobian coefficient.

The dense backward comparison history is frozen after `t_q`; its projection energy uses `A-tau(t) <= rho_hat(t)/kappa` to cancel the inverse clock speed. Integrating the endpoint-defect product then produces the `q^(-2)` term and the `q^(-1)` feedback term in `491–509`. The latter is absorbed once `q >= q_abs`. Since `q_abs=n^(o(1))` at a fixed problem, the prescribed order eventually exceeds it.

Substitution of `q` proportional to `lambda^(-3) n^(1/4) log(en)^2 exp(sqrt(log(en))/2)` gives the stated `CY/(sqrt(n) log(en)^3)` error. The exact moving inventory is `n(d+1)+1+2(L-1)mnq`; the initialized hidden mixers are an additional `(L-1)n^2`. The headline correctly distinguishes these counts and does not call the Legendre count total storage.

### 3. Exact selected metric, corrected readout, fitting, and error transfer

**Claim plausibility:** Highly Plausible. **Argument verdict:** Sound in the checked scope.

The sparse-metric construction (`compact_selected.tex:11–86`) was checked by multiplication. With `P=U_I`, `G=P^TDP`, and the displayed `M`, it gives `P^TMP=I`. Its middle factor has eigenvalues in `[1/4,1]`, giving `D/4 <= M <= D`. Including the constant vector supplies the mass bounds. Consequently diagonal multiplication and coordinatewise activation have the claimed dimension-free metric bounds.

The model is correctly treated as a prescribed optimizer. The coordinate activation gate need not be self-adjoint in `M`, and no gradient interpretation of the corrected predictor is used (`219–220`). Nevertheless the squared parameter speed is exactly the Gram quadratic form, including cross-sample terms. Hence the autonomous deficit equation proves fitting and finite parameter length. The corrected readout is an orthogonal projection plus a minimum-norm interpolation term, which gives its norm bound while the training Gram stays positive.

The main cancellation can be reconstructed without a gradient assumption. Let `e=(c_C-c_n)/sqrt(m)`, `T_C=V_CQ_C^(-1)`, `p=T_Ce`, and `zeta=w_C-w_R+p`. In the derivative of `zeta`, the raw-readout term `2V_Ce` cancels the deficit term `-2T_CQ_Ce` because `T_CQ_C=V_C`. In the derivative of `||p||^2/2`, the same term contributes exactly `-2||e||^2` (`510–550`). The hidden-Gram contribution, although not sign definite after applying `T_C`, is absorbed by the stated small-label bound. This justifies the integral control of the deficit error rather than treating it as unconstrained feedback.

The source pair-defect calculation and the integrated source-energy bound retain sample normalization. In particular, the latter follows from the dense path length and avoids a spurious extra reciprocal-gap factor (`421–438`). Backward comparison again places the changed gate against the bounded dense carrier; the resulting `M` factor is additive through the recursion. The coefficient integral has the stated form

\[
\mathcal B_n\le 1+\sqrt{\log(en)},\qquad
\mathcal B_n/z\le C(1+\sqrt{\log(en)}).
\]

This gives the public error bound with `z(1+lambda^(-1/2))`, and the public tolerance allocates half of `Y/n` to the finite-horizon error. The independent fitted tails allocate the other half eventually. The runtime inventory includes initial and moving arrays, metrics, inverse/factor caches, indices, training arrays, data, directions, and query workspace. The `1020(L+1)q^2` allowance is sufficient for these matrix/array families when `m,d <= q`.

### 4. Initialization-only compiler and the two source counts

**Claim plausibility:** Highly Plausible. **Argument verdict:** Sound in the checked scope, with the explicitly stated finite-existence interpretation.

For the compiler (`compact_selected.tex:661–765`), direct substitution verifies that the disk-to-time map sends `0` to physical time `0`, sends `xi_*<1` to `T`, has nonzero derivative on the intervening real interval, and maps the open unit disk inside the supplied rectangle. The composed source is bounded by `M`; its Taylor coefficients are finite linear combinations of origin derivatives. The geometric tail is uniform on the complete physical interval. Cauchy estimates on a larger compact disk also recover each finite set of later-anchor derivatives. This does not insert a later trained parameter or trajectory sample into the initialization data.

The exact initialized-image requirement is compatible with the compiler: apply the scalar coefficient functional to a base source and multiply its vector by the fixed initialized matrix. The Euclidean coefficient error can be made smaller by the factor eight and the finite sum of basis suprema. This needs potentially enormous derivative order, precision, and preprocessing storage; all three are explicitly outside the theorem's retained-coordinate claim.

For harmonic approximation (`769–903`), the spatial projection argument uses the complex quadric rather than an unrestricted complex Euclidean ball. Zonal averaging at imaginary angle yields the exponential harmonic decay; the positive Gegenbauer coefficient argument supplies the stated polynomial prefactor. The time Fourier/Chebyshev decay then gives a weighted-simplex cutoff. Counting unit cubes gives the factorial denominator in the source dimension, rather than an untracked dimension-dependent constant. The two-point `d=1` case is handled separately.

At the supplied radii,

\[
\alpha_T^{-1}=128\beta^{30L}z^2\sqrt{d+3}\,\ell^{3/2},
\qquad r_q^{-1}=\beta^{3L}\sqrt{(d+3)\ell},
\quad \ell=\log(en).
\]

With the eventual cutoff bounded by `8 ell`, this gives source dimension proportional to `z^2 ell^(3d/2+1) (d+3)^(d/2)/d!`, up to activation/depth factors exponential in `d`. Squaring the runtime dimension gives exactly the displayed `z^4 ell^(3d+2)` order and the stated `(C/d)^(d+1)` envelope. Fixed problem parameters inside logarithms are absorbed only into the qualifying width, consistent with the theorem's quantifiers.

For the panel method (`997–1118`), half-radius Taylor panels give exponentially small tails with `K+1=O(ell)`. Multiplying by the public number of panels, and then squaring, retains both terms

\[
z^4\ell^3
\quad\text{and}\quad
\lambda^{-2}\ell^2\{\log(e+\ell)\}^2.
\]

The exact first-layer restriction to the span of declared inputs preserves their norms, all sample inner products, the Gaussian initialization law in the reduced coordinates, and the coupled panel trajectories. Its dimension is at most `m+p`. Original/transformed data and the retained input map cost the additional `C(m+p)d`. Passive inputs enter source approximation and queries but neither the deficit ODE nor the Gram inverse. The partition is a proof/compilation object and is not a runtime forcing table.

### 5. Actual dense variability and final probabilistic assembly

**Claim plausibility:** Highly Plausible. **Argument verdict:** Sound in the checked scope, conditional on the finite-query analytic source conclusion.

The final-layer innovation argument (`compact_legendre.tex:602–643`) uses only a positive definite uncentered feature Gram and finite fourth moments. The area inequality, its truncation at `||U||=R_0`, and the two spectral lower bounds yield the displayed positive coordinate variance. Thus neither centering nor a rank condition on an earlier covariance is being silently assumed.

Conditioned on both lower-layer initializations, the two last-layer row groups are independent. Linear growth supplies uniformly bounded third absolute moments of the centered row products on bounded covariance sets. The characteristic-function calculation therefore gives the conditional scalar Gaussian fluctuation. Its conditional mean may be an arbitrary lower-layer-dependent shift. A centered Gaussian maximizes interval mass at zero, so that shift cannot improve the asymptotic small-ball probability (`645–711`). This is an actual anti-concentration argument, not an upper bound on dense variance repurposed as a lower bound.

The derivative-to-trajectory lemma has the correct physical factor `2/r`, the correct Chebyshev derivative tail, and an endpoint polynomial derivative bound valid for complex coefficients. Taking `r=1/(lambda sqrt(ell))` and degree `O(ell)` turns the derivative innovation into the claimed `Y sqrt(gamma)/(sqrt(n) ell^(5/2))` positive-time witness. The witness is a training input in either promised domain. It need not, and does not, assert nonzero variability at the fitted training endpoint.

Finally, the assembly in `compact.tex:254–288` intersects approximation and dense lower-bound events by a union bound; independence between these events is unnecessary. The independent dense run is used where required for the fluctuation calculation. At each fixed confidence the deterministic error/lower-bound ratios tend to zero, and then the confidence budget tends to zero. Missing endpoints and zero denominators are explicitly counted as failures. These are the right quantifiers for convergence in probability, not a simultaneous assertion over all independently initialized widths.

## Severity triage and necessary repairs

| Category | Concern ID | Result | Disposition |
|---|---|---|---|
| Fatal flaw | None | No verified foundational contradiction found | No repair identified |
| Major flaw | None | No material missing hypothesis or failed step found | No repair identified |
| Minor flaw | None | No localized correction necessary to support the checked conclusions identified | No repair identified |
| Coverage limitation | Not a flaw ID | Stopped-cavity/source proof and large enclosing-constant ledger | Complete read and focused reconstruction; not a separate formal derivation of every numerical enclosure |

The argument depends on fixed data and positive fixed label scale, very small labels, exact real-coordinate storage, and unrestricted finite initialization work. Those limitations are explicit in the paper and are not counted as flaws. Broadening any of them would require additional work beyond the reviewed theorem.

## Final frozen-input integrity

After report creation, the final `sha256sum` and `wc -l` commands both exited with status 0. Every SHA-256 matched the corresponding before-audit value in the table, and all five line counts still totaled 3,958. No frozen-input drift was detected. This report applies to those exact hashes.
