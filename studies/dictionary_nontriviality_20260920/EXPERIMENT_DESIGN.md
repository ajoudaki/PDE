# Dictionary nontriviality: proposed bounded numerical design

Status: frozen proposal, 2026-09-20. No experiment has been run for this report, and no performance result is assumed. The numbers below are proposed execution caps and design conventions, not mathematical guarantees or empirical findings. This document was produced from the supervisor's scoped assignment and required process instructions only; it imports no other study's findings.

## 1. Decision question and scope

Does the population dictionary attain a fixed prediction-trajectory accuracy at lower total cost than strong generic alternatives, once information provenance, numerical resolution, and the training mechanisms are matched?

The canonical dense model has input dimension two, \(L\) hidden tanh layers, the initialization and parameter scaling specified by the study, output \(f=c^\top h_L/n\), unhalved weighted mean squared loss, and mobilities \((n,1,\ldots,1,n)\). All parameter groups train. A short trajectory of this fully trainable model is the target; it is not assumed to reach an optimizer's terminal solution. Before implementation, the precise initialization convention must state whether each quoted scale is a variance, standard deviation, or stored-variable scale. No method may silently change that convention, the factor two in the loss gradient, the mobility, or the physical clock.

The closure retains a full joint mark population per layer, moving endpoint row/readout, and \(L-1\) learned finite coefficient matrices with the true transpose used in backward propagation. A basis comparison should first vary the basis while retaining this common dynamical structure. An independent function-space surrogate can be an additional competitor, but must be identified as a different reduced model rather than treated as the same closure with a different dictionary.

Competing explanations are:

- Special efficiency: the proposed dictionary gives a reproducible accuracy-cost advantage beyond generic low-dimensional compression.
- Generic compression: random, orthogonal, PCA/POD, Fourier, or polynomial bases achieve comparable accuracy at comparable total cost.
- Information advantage: offline snapshots explain the gain.
- Weak-motion regime: the horizon is sufficiently close to initialization that almost any reasonable method succeeds.
- Good representation but bad dynamics: projection error is small while autonomous rollout error is large.

The conclusions concern tested numerical witnesses and regimes. They do not establish hierarchy convergence, an infinite-width identification theorem, or impossibility of other finite representations.

## 2. Two scientific roles that must remain separate

**Paired finite-carrier compression.** Use the same finite neuron/mark carrier, training set, initialization realization, and physical reference trajectory for all bases. Project/restrict the finite operators consistently and integrate the reduced dynamics. This is the cleanest diagnostic of basis quality, projection, and transpose consistency. Dense matrix access and storage during construction are charged. A basis or coefficient array indexed by every dense neuron remains width-dependent. Success here establishes compression of that finite realization; it does not establish a width-free population closure.

**Width-free population closure.** Specify basis functions evaluable on new marks, a finite closure state, finite populations used as numerical quadrature, and autonomous evolution without dense-reference queries. For a fixed accuracy target, the advertised dictionary/state specification must not simply retain the dense width in disguised form. Independently refine population quadrature and dictionary resolution, then compare to width-refined dense ensembles. Report both the symbolic representation and the actual sampled implementation cost. Evidence across several widths is useful but does not prove ambient-width independence.

The proposed pilot uses paired finite-carrier diagnostics first and allocates the main comparison to population closures that pass those diagnostics. The two roles receive separate figures and conclusions. If only finite-carrier implementations are available, the program ends with that narrower conclusion; it must not relabel them population evidence.

## 3. Basis controls and coordinate invariance

The six primary families are the proposed dictionary, random basis, orthogonalized random basis, PCA/POD, Fourier, and polynomial/Hermite Galerkin. Galerkin is a projection procedure, so its basis, trial/test spaces, quadrature, and coordinate metric must be specified. Use the same mark variables and declared scaling where the bases act on the same object. Fourier domain truncation and polynomial conditioning are separate numerical issues. Rank alone is not a cost match.

An independent random orthogonal subspace is a random-subspace competitor. An orthogonalized copy of the same random span is a coordinate/conditioning control; it must not be counted as independent evidence from a second representation family.

**An equal-span orthogonal rotation is an invariance check, not an independent baseline.** Rotate a fixed basis by an orthogonal matrix and transform initialization, matrices, endpoints, backward maps, and state consistently. With the same Euclidean metric in the transformed coordinates, physical trajectories should agree to solver tolerance. A large accuracy improvement after such a rotation is an implementation, regularization, or numerical-conditioning issue rather than evidence of a new span.

**General QR requires a metric transformation.** If old coordinates and new coordinates satisfy \(\theta=Pz\), and the old flow is

\[
\dot\theta=-M\nabla_\theta\mathcal L,
\]

then the equivalent new flow is

\[
\dot z=-P^{-1}MP^{-\top}\nabla_z\mathcal L.
\]

Keeping identity mobility after a nonorthogonal coordinate change generally changes the dynamics. The coordinate-equivalent QR control must transform the metric, regularization, initialization, and all coupled maps. A QR version intentionally using a different metric is a separate preconditioning experiment, with that change reported. Nonorthogonal coordinate representations also require their Gram-weighted adjoints: for a coordinate map \(A\) with input/output Gram matrices, the adjoint is \(G_{\rm in}^{-1}A^\top G_{\rm out}\), assuming the Gram matrices are nonsingular. This coordinate fact does not authorize replacing the physical backward transpose by an independently fitted operator.

Before comparisons, check the weighted bilinear adjoint identity and compare the reduced RHS to finite differences of the declared loss at nondegenerate states. These checks are especially important because zero initial gradients can hide an incorrect backward implementation.

## 4. Provenance, initialization degeneracy, and holdouts

Use distinct leaderboards:

1. Initialization only: construction may use initial marks/operators and the common permitted training inputs. It may not use future dense states. Any access to labels during construction must be identical across the relevant competitors and stated explicitly.
2. Offline snapshots: every competitor receives the same donor-trajectory, time, and storage allowance, including an offline version of the proposed dictionary. Construction costs and dense donor simulations are charged.

In the population initialization with identically zero readout, the actual backward fields are zero. Small random finite-width readout values must not be confused with a nonzero population backward signal. A dictionary made from actual initial backward fields therefore has a genuine rank degeneracy. Do not whiten zero modes, divide by their norm, report a zero backward approximation error as informative accuracy, or insert future snapshots into an initialization-only method. If the method needs a supplemental basis, declare it: for example, forward features, seeded random directions, or synthetic probes. Give appropriate controls the same allowance. Synthetic adjoint probes can test an operator, but are not observations of the actual training trajectory. Actual backward-field accuracy is evaluated only after its signal exceeds numerical uncertainty.

Use four disjoint seed sets: numerical pilots, offline donors, method/rank selection, and confirmation. Pair the training dataset and dense initialization between competing methods within each evaluated instance. Repeat random dictionary draws rather than selecting a favorable draw. Report variability across data/initialization seeds and dictionary draws separately where possible.

Input holdout, future-time holdout, and initialization-seed holdout answer different questions:

- Input holdout tests whether trajectory agreement extends beyond the training and basis-fitting inputs. A proposed small setup is 256 training inputs, 1,024 tuning inputs, and 4,096 final evaluation inputs on a fixed two-dimensional bounded domain. Final inputs do not select bases or ranks. Their size is separately refined for quadrature accuracy.
- Future-time holdout tests autonomous continuation beyond snapshot times. In the recommended offline track, donor snapshots are restricted to \([0,T/3]\), while the target rollouts continue to \(T\). Report the whole interval and the future interval \([T/3,T]\) separately. No test-trajectory state is supplied during rollout.
- Seed holdout tests a construction on new neuron/mark realizations. Standard POD vectors expressed in one realization's neuron coordinates cannot simply be copied to another random neuron basis. A transferable POD method needs an explicit out-of-sample lifting, such as a fixed feature representation or a fitted extension evaluable on new marks. Train and charge that extension using donor data only. Without it, POD is a within-carrier baseline and cannot enter a cross-seed population leaderboard.

If a same-seed prefix is instead used to fit a basis and initialize a reduced state at \(T/3\), report a separate warm-start forecasting experiment on \([T/3,T]\), charge the prefix and projection, and give all competitors the same prefix information. This is not initialization-only prediction. POD fitted to the complete evaluated trajectory is an oracle projection ceiling, never a causal competitor.

Restart the closure at an interior time using only its exported advertised state, and inspect the state inventory. Agreement with uninterrupted integration checks that hidden trajectory buffers, dense arrays, or omitted solver-independent memory are not required for that tested continuation.

## 5. Proposed staged execution envelope

Use \(L=3\) first: it retains two internal learned matrices and their coupled backward use. Depth generalization is outside this capped first pilot; a later depth test needs its own frozen allocation. Fix two targets before method screening, one tanh-ridge mixture and one rotated multiscale odd Fourier target. Odd targets avoid an avoidable expressivity mismatch if the canonical architecture has no biases. Both are smooth and nonzero, with target amplitude fixed from permitted training information. Frequencies, ridge directions, and coefficients must be recorded before screening and must not be selected for a favorable dictionary result.

The following counts are upper bounds, not an authorization to execute and not a promise that all branches fit:

| Stage | Purpose | Dense trajectory cap | Reduced trajectory cap |
| --- | --- | ---: | ---: |
| Numerical pilot | Two pilot seeds; reference-width/step checks; finite-carrier invariance, adjoint, and population-resolution checks | 8 | 36 |
| Offline donors | Disjoint donor seeds and declared snapshot prefix | 4 | 0 |
| Screening | Six families, three proposed ranks \(4,8,16\), two paired selection seeds, two provenance tracks | 4 | 72 |
| Confirmation | Proposed method and up to two frozen generic finalists per track; six new paired seeds on each of two targets; one frozen operating point per finalist | 12 | 72 |
| Conditional reserve | Resolution failures, next-rank checks, or predeclared mechanism ablations | 2 | 60 |
| **Total cap** | **Stop when either cap is exhausted** | **30** | **240** |

A rerun at a different timestep, population size, or random dictionary seed counts as another trajectory. Cheap algebraic checks without a trajectory are logged separately. Actual wall-time and memory caps must be set after implementation feasibility is known and before launching any execution. The allocation is a proposed envelope; if the reference or portability requirements cannot fit, reduce the scope explicitly or stop, rather than silently weakening validity gates.

Choose the reference width from a predeclared ladder, provisionally \(512,1024,2048\); these numbers are trial resolutions, not claimed adequate widths. Choose the shortest of a predeclared bounded set of short horizons that passes the feature-learning and numerical gates on dense pilots alone. Freeze that horizon before screening. Failure of all allowed horizons ends the feature-learning comparison. Select generic finalists and operating points using selection data only. Confirmation data do not reopen that search.

Before running, also freeze solver/tolerance options, population-size ladder, dictionaries and extensions, snapshot times, random-seed lists, hardware, maximum wall time, peak-memory cap, and exact target formulas. These currently missing implementation choices are required launch inputs, not unspecified permissions to search for success.

## 6. Signal and feature-learning gates

The following numerical levels are conventions chosen to make the intended distinction observable. They can be revised before execution, with a new frozen design, but not after inspecting method comparisons.

A pilot horizon is informative for substantive feature learning only if:

- Dense loss falls at least 20% from its initial value.
- Full-network predictions differ from the exact initial tangent-model evolution by at least 5% of the full reference prediction change, and by at least five times the measured uncertainty in that comparison.
- At least one internal hidden-layer activation Gram matrix changes by at least 10% of its initial Frobenius norm, and its change exceeds five times the uncertainty obtained from time/width/evaluation refinements. Report scale change and normalized Gram-shape change separately; do not attribute pure scaling to shape change.

Also compare readout-only/frozen-hidden training and report motion for every layer. Large relative motion obtained by dividing by an almost-zero initial backward field or coefficient is invalid. Use forward-activation scales, fixed nonzero target scales, or absolute differences accompanied by a numerical error estimate. Report actual backward fields only when they exceed that error floor.

Do not silently discard confirmation seeds with little hidden motion. Report all seeds and gate failures. A claim about feature-learning performance on a target requires the prespecified gates on at least five of its six confirmation instances; otherwise downgrade that target to a weak-motion or mixed-regime comparison.

## 7. Metrics and fair cost accounting

For evaluation interval \(I\), define

\[
D_I=\max\left\{\max_{t\in I}\|f_{\rm ref}(t)-f_{\rm ref}(\inf I)\|_{L^2(\mathrm{eval})},\;0.1\|y\|_{L^2(\mathrm{eval})}\right\},
\qquad
E_I=\frac{\max_{t\in\mathcal T\cap I}\|\widehat f(t)-f_{\rm ref}(t)\|_{L^2(\mathrm{eval})}}{D_I}.
\]

Use a frozen sufficiently dense physical-time grid containing the endpoints. Refine it to check that transient errors are resolved. Do not fit a time reparameterization, amplitude correction, or post-hoc alignment. The primary accuracy threshold is \(E_{[0,T]}\leq0.05\). The offline track additionally requires \(E_{[T/3,T]}\leq0.05\), reported separately.

The primary efficiency outcome is the minimum **tested** total cost meeting tolerance. A rank grid identifies only a tested operating point, not an unrestricted minimum. If every rank fails, report “not attained”; if the smallest rank passes, do not infer its cost is minimal without testing a cheaper point. A next-rank check is allowed only under the frozen reserve rule.

Secondary metrics are loss-trajectory error, prediction-velocity error, hidden Gram trajectories, tangent-kernel drift, nonzero backward-field error, gradient alignment, and static projection error versus autonomous rollout error. Static snapshot reconstruction is never substituted for rollout accuracy.

Report error against all of:

- Total stored scalar state, including joint populations, endpoints, coefficient matrices, basis/lifting parameters, and any retained data-dependent arrays.
- Peak memory and estimated arithmetic/evaluation work, including derivatives and forward/backward operations.
- Measured integration time and end-to-end time, including construction, orthogonalization, snapshot collection, donor simulations, and extensions.

Use the same hardware and precision, include failed runs, and specify the accounting boundary. Show online and end-to-end costs separately. Offline amortization must state the number of future deployments; do not assume unlimited amortization. Equal rank or equal trainable-matrix count is not sufficient. Keep population size and basis resolution as independent axes, and do not hide width-dependent carrier storage outside the stated state count.

## 8. Numerical validity and common references

Independently check dense width, dense/reduced solver step or tolerance, population quadrature, evaluation quadrature, basis resolution, and conditioning. Increasing rank does not validate any of the other axes.

Compare dense widths over paired seed ensembles and report both mean changes and variability. A particular coupling of random matrices across widths does not automatically supply pathwise convergence, so do not interpret individual path differences as a universal width-error bound. Distinguish agreement to a finite dense realization from agreement to a width-refined statistical target.

Require each measured numerical uncertainty to be below one fifth of the 5% accuracy tolerance and below one fifth of the inter-method advantage being claimed. These are empirical resolution criteria, not rigorous bounds. If a claimed advantage is smaller than the resolvable numerical uncertainty, classify it as inconclusive. Time and population refinements must use the same scientific configuration, initial information, and reference; avoid comparing ranks against different favorable references.

Monitor Gram singular values/condition numbers, regularization sensitivity, transpose residuals, and solver failures. Record Fourier-domain/tail sensitivity and high-degree polynomial conditioning where applicable. A regularization change changes the method unless it is part of a frozen numerical rule. Numerical failures are reported, with any reserve reruns and exclusions visible.

## 9. Precommitted decisions and branches

The following are design conventions for practical discrimination, not theorem thresholds.

**Special-efficiency pass.** The proposed dictionary meets accuracy and all validity/feature-learning gates, and has at most half the minimum tested cost of the strongest frozen generic finalist, separately on both confirmation targets. Require consistency in paired comparisons and a prespecified paired 95% uncertainty interval supporting lower cost. Make the provenance track and cost measure explicit; a wall-time pass alone does not imply a state-size pass. If uncertainty or the discrete tested operating points cannot support the stated ratio, withhold that claim.

**Practical tie.** A generic method meets the same accuracy and validity gates, with costs inside a prespecified ratio band \([0.8,1.25]\) relative to the proposed method and prediction errors within 0.01 normalized units. A formal equivalence statement requires the paired uncertainty interval to lie inside the equivalence margins. Mere failure to detect superiority is not equivalence. Report “no resolved advantage” when intervals are too wide.

**Generic win.** A generic method meets tolerance and the proposed method fails at comparable or higher tested cost, or a valid reverse cost advantage is resolved. Conclude that the proposed special-efficiency explanation is disfavored in that tested regime.

**Inconclusive.** Numerical/feature-learning gates fail, portability is absent, intervals overlap decision boundaries, targets disagree, all methods miss tolerance, or the execution cap prevents resolution. State the exact reason. All-method failure can reject these witnesses/budgets; it does not reject arbitrary finite-closure existence.

Only these reserve branches are proposed:

1. A numerical gate fails: spend reserve on the single implicated resolution axis. Stop that comparison if the gate remains unresolved or the reserve is exhausted.
2. A finalist's frozen rank misses tolerance: evaluate its next predeclared rank once if affordable; retain the failed operating point and charge both runs.
3. A valid efficiency difference survives confirmation: run the predeclared mechanism ablations below, using remaining reserve, without tuning a new target.
4. A generic method ties or wins: accept the generic explanation at this scope and stop the special-efficiency search. A further search is a new proposal.

## 10. High-value mechanism ablations and interpretations

Apply causal ablations to both the proposed basis and the strongest generic finalist where budget permits. Their purpose is to identify a necessary ingredient, not to manufacture weak competitors.

- Freeze internal coefficient matrices while allowing endpoint motion. A shared loss of accuracy supports the importance of generic low-rank adaptation, not a unique dictionary mechanism.
- Freeze endpoint motion while allowing internal matrix learning. This probes whether moving rows/readout are essential to the tested trajectory.
- Destroy cross-coordinate dependence in the joint mark law while preserving selected marginals. Use a declared permutation/coupling construction and repeated permutations to distinguish a correlation effect from sampling noise. Failure shows the importance of retained joint information; it does not establish that one basis is special.
- Break true transpose reuse only as a deliberately altered-mechanism diagnostic, preferably accompanied by the instantaneous adjoint/gradient checks. A failure is expected if the dynamics have changed; it is not evidence that generic bases cannot represent the correct coupled model. An untied model with extra parameters must not masquerade as an equal-budget basis control.

Interpretation examples:

- Good static projection and bad rollout: represented snapshots do not establish a closed autonomous dynamics.
- Offline success with initialization-only failure: information from learned trajectories is useful; do not attribute all gain to the basis architecture.
- Tiny-rank success by all methods: the tested problem admits an easy low-dimensional explanation.
- Output agreement with wrong hidden/velocity diagnostics: observable accuracy may conceal cancellation or an insensitive regime.
- Rank improvement that disappears under population/time refinement: the apparent hierarchy trend was numerically confounded.
- Finite-carrier success without a transferable basis: useful realization-specific compression, with the population-closure question still open.

Freeze exact implementation configuration and source identifiers before any execution, retain raw outputs and failures, and attach the final file hash to the supervisor's record. No execution, implementation, publication, or promotion is performed by this design document.
