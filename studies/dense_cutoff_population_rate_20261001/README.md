# Dense networks: auxiliary cutoff and a uniform population rate

Started 2026-10-01. This is a new investigation of the dense network, explicitly requested in the current task. It does not import proof claims from response-memory or clipping studies.

## Scientific contract

The target is the canonical dense gradient flow in `paper/main.tex`, equation `eq:dense-flow`, with fixed depth, fixed finite training data, independent Gaussian initialization, exactly zero initial readout, a positive limiting initial readout-feature Gram gap, and sufficiently small fixed label RMS. The population target is the dense Gaussian operator flow constructed in `paper/proof_alltime.tex`. The target error is

\[
\mathcal E_\mu(f_n,f_\infty)
=\left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

The requested rate is \(C_\delta/\sqrt n\) with probability at least \(1-\delta\), with constants independent of width and time. Labels and the data do not vary with width. The initial scope retains the paper's activation assumptions; any stronger regularity or boundedness needed by a route must be explicit. A theorem only for two hidden layers is a scoped result, not a theorem for arbitrary fixed depth.

The subsequent counterexample request also permits arbitrary fixed label
magnitudes. This is an authorized extension of the negative search;
it does not remove the small-label hypothesis from existing general-data
theorems. A completed large-label positive special case is identified below.

An auxiliary smooth cutoff must equal the identity on \([-M,M]\), contract magnitudes, and saturate outside a larger interval. It is a proof device. The final target is the original unclipped algorithm and its unclipped population. The three required errors are finite cutoff removal, clipped finite-to-population comparison, and population cutoff removal, all in the all-time metric. Complete finite cutoff inactivity is optional.

Strict root width, \(n^{-1/2+o(1)}\), qualitative convergence, population-only tails, and concentration about a finite-width mean are different claim levels. No one substitutes for another. No rate is assumed from the existence of a population limit.

## Inputs and boundaries

- Current repository instructions and required mathematical/research skills.
- Maintained scientific book: `docs/index.qmd`, `docs/notation.qmd`, and relevant complete passages under `docs/`.
- User-authorized current manuscript `paper/main.tex` and all its included mathematical material and captions.
- This study's own derivations and checks.

No other study is a scientific input. No manuscript edits, Git writes, or experiments are planned. Shared checkout changes are preserved. Starting HEAD: `4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`. Preexisting modifications to `paper/main.pdf` and another study README are outside this study's writes.

## Current outcome

The latest arbitrary-label follow-up is
[ARBITRARY_LABEL_RESULT.md](ARBITRARY_LABEL_RESULT.md).
**A complete strict all-time dense-to-population root-width theorem is
now proved for two hidden linear layers, one normalized training sample,
and any fixed real label.** It includes the finite-width bias, the same
physical-time comparison, the fitted endpoint, and every query law with
finite second moment. There is no clipping or small-label restriction
in this special case. The proof controls all initialized spectral
moments and sums their errors through the exact learned spectral
evolution; a complete separate internal reconstruction passed.

No slower-than-near-root canonical prediction counterexample was found.
The negative search also proves finite-network one-sample fitting for
every fixed label without bounded activation values. At arbitrary fixed
linear depth it gives a conditionally Gaussian fitted query law with
matching root-width upper and lower scales. These results rule out
specific scalar slowdown and linear spectral-concentration mechanisms;
they do not settle the nonlinear multi-sample population rate. The
exact residual-direction rotation term records why the scalar fitting
argument does not immediately extend to several samples.

The preceding general direct dense-to-population continuation is
[POPULATION_CONTINUATION_RESULT.md](POPULATION_CONTINUATION_RESULT.md).
**The requested general all-time near-root population rate, or a canonical
polynomially slower counterexample, remains unresolved.** This round
improves actual finite-neuron deletion/reinsertion and its Gaussian
response equations to \(n^{-1/2}e^{C\sqrt{\log(e+n)}}\) accuracy.
It also checks tagged-history first responses, exact averaged response
traces, and conditional localization. Those equations retain random
cavity covariance/response kernels; their replacement by canonical
population quantities at the target rate is not proved.

A separate auxiliary theorem gives root-width Gaussian path coupling
for independent bounded-Sobolev paths, without a minimum history-Gram
eigenvalue. It does not assume trained neurons are independent.
The negative search checks initialized covariance singularities,
fixed training gaps, low activation regularity, rare coordinates and
query tails, without producing a canonical prediction lower bound.
The subsequent response-transport note realizes represented responses
as contractions on common causal population spaces, including rank
changes. A separate \(n^{-1/d}\) parameter-law transport lower bound
shows why coupling entire finite and Gaussian read-in densities is too
strong for the desired prediction rate when \(d>2\). It is explicitly
not a lower bound for predictions.
Exact source versions, internal reconstructions and open steps are
linked below. No new model restriction, clipping, experiment or
manuscript change was used to assert a population theorem.

The width-\(n\) versus width-\(2n\) continuation is
[WIDTH_DOUBLING_RESULT.md](WIDTH_DOUBLING_RESULT.md).
**The requested canonical width-doubling near-root bound remains open.**
The new completed comparison concerns the block endpoint: two
width-\(n\) networks trained against their shared averaged residual
stay \(n^{-1/2}e^{K\sqrt{\log(e+n)}}\)-close to the average of their
independently trained counterparts, throughout physical time and at
their fitted limits. It retains the full preceding data, depth,
activation and query scope. Only the independently trained references
need the already proved carrier maximum. This repairs a real endpoint
issue: block-diagonal autonomous training does not give independent
trained blocks exactly.

The synthesis also proves that a near-root canonical \(n\)-versus-\(2n\)
bound, together with the already proved concentration and qualitative
population limit, would imply a near-root dense-to-population rate by
telescoping deterministic finite-width centers. No infinite union of
random events or unstopped expectation bound is needed for that
implication. The missing width-dependent center displacement is thus
the substantive population-bias problem.
Balanced covariance/mobility interpolation, exact duplication, rotations,
and conditional Gaussian response couplings were examined. No complete
trained signed-response cancellation or canonical negative construction
was obtained. The profile note improves the two-layer initialized
contrast to root width using only three bounded derivatives in the
bounded-value subclass; it does not propagate that bound through training.

The independent-copy follow-up is
[GENERAL_SELF_AVERAGING.md](GENERAL_SELF_AVERAGING.md). In the same
fixed-depth, general compatible-data, broad smooth-activation, small-label
setting as the completed compression result, two actual independently
initialized dense networks satisfy the all-time, query-integrated bound
\[
\mathcal E_\mu(f_n,f_n')
\le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}}
=n^{-1/2+o(1)}
\]
at fixed confidence for all sufficiently large widths. No clipping or
additional response assumption is used. The proof compares pairs of good
initializations, extends scalar predictions off that set, and uses
Gaussian concentration on a compactified physical-time grid.
It does not require an \(O(1/n)\) failure probability for the existing
carrier theorem. This is a proved weaker result: **strict
\(C_{\delta,\mu}/\sqrt n\) independent-copy concentration in this general
scope remains open**. It also does not assert an unconditional expectation
bound for the original all-time error over bad initializations.

The first-order, second-order, adjoint-energy and controlled-feedback
routes were examined explicitly. The missing strict estimate controls a
prediction-selected response direction, not merely the average response
over all parameter directions. Its precise mixed carrier/sensitivity
products, an exact directional entropy inequality, and the need for
time-increment and Gaussian-domain control are recorded in the three new
route files below. Their abstract alignment examples are not neural
counterexamples. The deterministic controlled-feedback estimate does
extend strictly to a single effective control direction at every fixed
depth, by exact cancellation of the control vector-field commutator;
this alone does not prove initialization concentration.

The latest same-width theorem is
[DEPTH_EXTENSION_RESULT.md](DEPTH_EXTENSION_RESULT.md): the near-quarter
order \(q_n=\lceil n^{1/4}e^{a\sqrt{\log(e+n)}}\rceil=n^{1/4+o(1)}\)
gives strict \(C_\mu/\sqrt n\) error, uniformly through the fitted
endpoint, at **every fixed depth**. The activation class is \(C^3\)
with bounded first three derivatives; **activation values may be
unbounded**. It includes tanh, sigmoid, arctan, erf, sine, cosine,
softplus, GELU and SiLU. The canonical unclipped dense network and actual
autonomous residual-RMS closure share initialization and width.
The constants and sufficiently small label threshold may depend on
fixed depth, activation and data, but not width, order or time.

The complete local and probability checks close the finite-network
joint forward/backward budget; no trained-moment or local-sensitivity
condition remains assumed. For a common nonaffine activation at every
layer and fixed sphere data, the initial feature gap is automatic under
the exact odd/even compatibility rules. For sigmoid, softplus, GELU and
SiLU, any distinct sphere inputs, including antipodal pairs, have a
positive feature Gram by the second hidden layer. Duplicate inputs
require equal labels. No orthogonality is used. The result supersedes
the former depth and bounded-value limitations; it does not cover ReLU,
growing depth, or large labels. No manuscript edit or experiment is involved.

Read [Q_ORDER_RESULT.md](Q_ORDER_RESULT.md) for the preceding two-hidden-layer tanh theorem, [ROOT_WIDTH_CONDITIONAL_THEOREM.md](ROOT_WIDTH_CONDITIONAL_THEOREM.md) for the dense-to-population conditional synthesis, and [RESULT.md](RESULT.md) for the earlier cutoff investigation. The distinct **general nonlinear unconditional strict all-time dense finite-to-population root-width theorem remains open**. The linear one-sample theorem above is a completed special case. No slower-than-root population lower bound is claimed.

The preceding population result reduces that complete root-width target to one explicit local signed response contrast, in the structured case of two tanh layers, orthonormal fixed training inputs, a bounded test-input domain, and sufficiently small fixed labels. The actual unclipped model, finite mean bias, full physical-time supremum, and fitted endpoint are all included in the conditional theorem. Its local response hypothesis is unproved and substantial. It does not assume a population convergence rate, but it is a derivative-level assertion that an auxiliary block variance profile changes the finite mean only weakly; it must not be advertised as automatically easy.

There is also an unconditional result in exactly this structured scope: [AUTONOMOUS_SELF_AVERAGING.md](AUTONOMOUS_SELF_AVERAGING.md) proves that the actual whole prediction trajectory concentrates at root width around a deterministic finite-width reference, and two independently trained finite networks differ by at most \(C_\delta/\sqrt n\) in the same all-time input-integrated norm. The reference is defined by a common expected residual driving finite networks; it is not silently identified with the population or with the mean of autonomous training. Its qualitative population limit is identified, but its quantitative bias remains open. Thus a slower-than-root obstruction here must be systematic finite-width displacement, rather than a growing random spread of training trajectories.

The large-label follow-up is in [LARGE_LABEL_ASSESSMENT.md](LARGE_LABEL_ASSESSMENT.md). It leaves the multi-sample small-label assumptions in place, but proves a one-sample exception: along the exact dense controlled gradient curve, the readout RMS is convex and the training tangent stays above its positive initialized feature energy. Consequently every fixed label is fitted exponentially at any fixed depth with bounded smooth activations. For two tanh layers, extending the finite controlled moment estimates to any fixed activity interval and using scalar monotonicity gives all-time root-width concentration around a deterministic finite-width center for arbitrary fixed label magnitude. This does not prove population bias or invoke the manuscript's small-label population theorem at large labels. A separate critical least-squares diagnostic illustrates slower endpoint response but is explicitly not a dense-network counterexample. The complete candidate and its dependencies were internally reconstructed in [LARGE_LABEL_ASSESSMENT_CHECK.md](LARGE_LABEL_ASSESSMENT_CHECK.md).

A bounded check of the alternative same-width target is recorded in [SAME_WIDTH_COMPARISON_CHECK.md](SAME_WIDTH_COMPARISON_CHECK.md). Dropping the population target removes the dense predictor's population discrepancy, while the manuscript's current proof still has a separate finite-carrier remainder. Combining this study's already checked finite-tail expectation bound with the manuscript's deterministic tracking estimate removes that remainder in the two-tanh, orthonormal-input, small-label scope: at fixed confidence the all-time same-width error is \(C_{\delta,\mu}q^{-2}e^{K\sqrt{\log(e+q)}}\). An order \(q_n=\lceil n^{1/4}e^{A\sqrt{\log(e+n)}}\rceil\), for a sufficiently large fixed \(A\), gives strict \(C_{\delta,\mu}/\sqrt n\) direct tracking. This is an internally checked implication of the existing ingredients, not a population-rate theorem or a manuscript change. The fixed mixer remains quadratic storage; fixed \(q\) does not gain a vanishing-width guarantee.

The new [Q_ORDER_POSITIVE_ROUTE.md](Q_ORDER_POSITIVE_ROUTE.md) removes orthogonality and closes the finite-network stopping argument. For every fixed compatible sphere dataset and sufficiently small fixed labels, it bounds the actual dense backward-carrier maximum by \(CS\sqrt{\log(e+n)}\) over all training time on events with probability tending to one, where \(S=2Y/\kappa\) and \(\rho(t)\le Ye^{-\kappa t}\). The proof deletes finite sets of first-layer neurons, keeps the retained network's own adaptive residuals, and reconstructs their effects through Gaussian linear and quadratic forms. The normalized trace of the response is controlled by a closed empirical exponential budget; the weaker worst-direction estimate is used only on vanishing remainders. This is a proved high-probability budget, not an expectation bound over every unstopped fitting path.

Combining that maximum with the already checked source estimate in [NONORTHOGONAL_DIRECT_ROUTE.md](NONORTHOGONAL_DIRECT_ROUTE.md) and the manuscript's dense-reference damping gives, simultaneously in order,
\[
\mathcal E_\mu(\widehat f_{n,q},f_{n,D})
\le C_\mu e^{K\sqrt{\log(e+n)}}q^{-2}\sqrt{\log(e+q)}.
\]
Thus \(q_n=\lceil n^{1/4}e^{A\sqrt{\log(e+n)}}\rceil=n^{1/4+o(1)}=o(n)\), with fixed \(A>K/2\), gives strict \(C_\mu/\sqrt n\) error. The constants and order schedule are independent of width and time; at each fixed confidence the width threshold may depend on the fixed data and labels. The comparison uses the actual same-width, shared-initialization, unclipped dense and autonomous closure trajectories with the original residual-RMS clock. It includes the fitted endpoint and a time supremum inside the query integral. No new carrier-tail or response-sensitivity hypothesis is assumed.

The separate discrepancy-ratio condition in [GENERAL_DATA_STABILITY_ROUTE.md](GENERAL_DATA_STABILITY_ROUTE.md) and the unstopped expectation target in [FINITE_MIXED_MOMENT_ROUTE.md](FINITE_MIXED_MOMENT_ROUTE.md) remain unproved in their original forms. They are no longer prerequisites for this same-width theorem. The positive proof uses the latter note's checked conditional Schatten estimate and then establishes the high-probability budget needed for that estimate through a finite-block bootstrap.

The preceding [GENERAL_DATA_ASSESSMENT.md](GENERAL_DATA_ASSESSMENT.md) records automatic quotient-Gram positivity and an arbitrary-depth fallback with order exponential in the square root of width. Its statement that useful general-data order remains open was superseded first by the two-tanh theorem and now by the fixed-depth extension. The exact compatible quotient, including fixed positive sample weights, removes a separate Gram hypothesis for the specified fixed sphere data. Inconsistent labels leave a persistent original clock and are outside this fitting theorem. A pure \(O(n^{1/4})\) schedule and an optimality result remain open. The negative searches did not produce the user's requested larger-order lower bound.

Two previously separate gaps are now closed in this structured setting. Prescribed-control fluctuations have the strict root-width rate for passive queries over the whole activity interval. A deterministic theorem transfers a population-centered estimate for the one fixed population residual history to actual adaptive training at the same physical time. Its essential estimate is a nonlinear remainder difference \(\|R^b-R^c\|\le CS^2\|b-c\|_\infty\); the initial Gram gap absorbs that difference when total activity \(S\) is small. Feature learning is retained in the remainder, and no nonvanishing additive label term is left.

For the mean bias, an exact interpolation changes both Gaussian edge variance and edge learning mobility between two independent width-\(n\) networks and one canonical width-\(2n\) network. A root-width difference between normalized within-block and cross-block expected edge responses gives a summable width-doubling bias bound. The stronger \(O(1/n)\) response contrast is verified at initialization for general query pairs, and in the first nonlinear activity coefficient for a one-sample training query. These local coefficients do not prove its propagation through training.

The preceding cutoff results remain valid: for orthonormal training inputs, tanh in the first layer, and a bounded second activation with bounded Lipschitz derivative, the actual trained finite backward carriers have quantitative Gaussian tails through the entire time supremum. A sufficiently large cutoff \(M(n)=A\sqrt{\log(e+n)}\) is inactive throughout finite training with high probability. Separately, for arbitrary fixed depth and the manuscript's activation class, population cutoff removal has all-time error \(Ce^{-cM^2}\), and clipped fitting has a cap-independent small-label threshold. Cutoff removal itself does not give the missing finite mean rate.

The preceding bounded assessment tested genuine matching of training loss, not an activity clock. Pure speed perturbations cancel, but transverse first and second responses retain carrier products. An explicit smooth two-output linear diagnostic shows that second matched-loss sensitivities may diverge near interpolation even when same-time sensitivities and finite differences remain controlled; it is not a dense width counterexample. An actual two-tanh dense initialization calculation also shows that the small-angle weak training direction has root-width fluctuations in its coefficient, so near-coincident inputs alone do not establish a worse exponent. That assessment did not yield a negative trained-width construction or a full population-rate proof.

| Artifact | Claim and scope | Check status |
|---|---|---|
| [ARBITRARY_LABEL_RESULT.md](ARBITRARY_LABEL_RESULT.md) | Arbitrary-label synthesis: completed linear one-sample population theorem, scalar fitting obstruction to negative examples, and remaining nonlinear question | Coordinator synthesis of the complete internal checks below |
| [ARBITRARY_LABEL_LINEAR_RATE.md](ARBITRARY_LABEL_LINEAR_RATE.md) | Strict root-width canonical dense-to-population prediction bound, all physical time and fitted endpoint, two hidden linear layers, one sample and arbitrary fixed label | Complete reconstruction in [ARBITRARY_LABEL_LINEAR_RATE_CHECK.md](ARBITRARY_LABEL_LINEAR_RATE_CHECK.md); includes spectral bias and clock transfer |
| [ARBITRARY_LABEL_NEGATIVE_ROUTE.md](ARBITRARY_LABEL_NEGATIVE_ROUTE.md) | One-sample and actual invariant-ray finite-network fitting for every fixed label, without bounded activation values; no slower-rate witness | Complete reconstruction in [ARBITRARY_LABEL_NEGATIVE_CHECK.md](ARBITRARY_LABEL_NEGATIVE_CHECK.md) |
| [ARBITRARY_LABEL_GEOMETRY_ROUTE.md](ARBITRARY_LABEL_GEOMETRY_ROUTE.md) | Arbitrary-depth linear passive all-time root-width error, exact conditional Gaussian fitted law and matching lower scale; two-layer spectral reduction | Complete reconstruction in [ARBITRARY_LABEL_GEOMETRY_CHECK.md](ARBITRARY_LABEL_GEOMETRY_CHECK.md), including the cosmetic correction; check also derives the exact multi-sample residual-rotation term |
| [POPULATION_CONTINUATION_RESULT.md](POPULATION_CONTINUATION_RESULT.md) | Direct continuation synthesis; target remains unresolved, with completed local finite-network and auxiliary covariance improvements | Coordinator synthesis of the separately checked results below; no population theorem |
| [POPULATION_DIRECT_COUPLING.md](POPULATION_DIRECT_COUPLING.md) | Near-root finite insertion and explicit random cavity Gaussian/response equations; exact first-chaos representation and first-step cancellation | Sections 3–5 reconstructed in [POPULATION_DIRECT_CHECK.md](POPULATION_DIRECT_CHECK.md); Sections 6–8 in [POPULATION_DIAGNOSTIC_CHECK.md](POPULATION_DIAGNOSTIC_CHECK.md) |
| [POPULATION_ADJACENT_ATTEMPT.md](POPULATION_ADJACENT_ATTEMPT.md) | Exact adjacent normalization, conditional no-exit, tagged-history derivatives, pulse/trace identities and conditional weighted finite-center comparison | Repaired conditioning argument reconstructed in [POPULATION_ADJACENT_CHECK.md](POPULATION_ADJACENT_CHECK.md); adjacent bias cancellation and full population rate open |
| [POPULATION_COVARIANCE_COUPLING.md](POPULATION_COVARIANCE_COUPLING.md) | Root-width Gaussian coupling from independent empirical path covariances with a stronger Hilbert-norm bound, including singular covariances | Complete reconstruction in [POPULATION_COVARIANCE_CHECK.md](POPULATION_COVARIANCE_CHECK.md); actual trained dependence is not covered |
| [POPULATION_NEGATIVE_SEARCH.md](POPULATION_NEGATIVE_SEARCH.md) | Exact diagnostics against several proposed slow-rate mechanisms; C3 derivative-observable trap; no canonical prediction counterexample | Coordinator reconstruction in [POPULATION_DIAGNOSTIC_CHECK.md](POPULATION_DIAGNOSTIC_CHECK.md) |
| [POPULATION_RESPONSE_TRANSPORT.md](POPULATION_RESPONSE_TRANSPORT.md) | Compatible population Gaussian isometries, exact represented-response contraction through rank changes and common-environment flow stability | Complete reconstruction in [POPULATION_RESPONSE_TRANSPORT_CHECK.md](POPULATION_RESPONSE_TRANSPORT_CHECK.md); finite-network coupling not supplied |
| [POPULATION_TRANSPORT_LIMIT.md](POPULATION_TRANSPORT_LIMIT.md) | Exact \(n^{-1/d}\) lower bound for transporting full empirical read-in laws to Gaussian laws; independent functional averages still have root-width RMS | Complete reconstruction in [POPULATION_TRANSPORT_LIMIT_CHECK.md](POPULATION_TRANSPORT_LIMIT_CHECK.md); not a prediction lower bound |
| [WIDTH_DOUBLING_RESULT.md](WIDTH_DOUBLING_RESULT.md) | Exact equivalence between quantitative canonical doubling and the near-root population rate, plus the completed split-endpoint theorem; requested canonical comparison remains open | Complete reconstruction in [WIDTH_DOUBLING_RESULT_CHECK.md](WIDTH_DOUBLING_RESULT_CHECK.md) |
| [WIDTH_DOUBLING_BLOCK_ROUTE.md](WIDTH_DOUBLING_BLOCK_ROUTE.md) | All-time near-root comparison of shared-residual blocks with independent autonomous blocks, using only the reference carrier maxima | Complete reconstruction in [WIDTH_DOUBLING_BLOCK_CHECK.md](WIDTH_DOUBLING_BLOCK_CHECK.md) |
| [WIDTH_DOUBLING_PROFILE_ROUTE.md](WIDTH_DOUBLING_PROFILE_ROUTE.md) | Autonomous signed covariance/mobility identity; bounded \(C^3\) initialization contrast; bounded-variation and finite-deletion attempts | Coordinator reconstruction recorded in [WIDTH_DOUBLING_ROUTE_CHECK.md](WIDTH_DOUBLING_ROUTE_CHECK.md); trained profile contrast remains open |
| [WIDTH_DOUBLING_COUPLING_ROUTE.md](WIDTH_DOUBLING_COUPLING_ROUTE.md) | Exact duplication, interior covariance defect, nonlinear rotation restriction and fresh-Gaussian coupling diagnostic | Coordinator reconstruction recorded in [WIDTH_DOUBLING_ROUTE_CHECK.md](WIDTH_DOUBLING_ROUTE_CHECK.md); no canonical width-bias bound |
| [GENERAL_SELF_AVERAGING.md](GENERAL_SELF_AVERAGING.md) | Unconditional fixed-confidence \(n^{-1/2}e^{K\sqrt{\log(e+n)}}\) independent-copy concentration, full physical-time supremum, general data/fixed depth/linear-growth smooth activations and finite-second-moment query law | Complete reconstruction in [SELF_AVERAGING_CHECK.md](SELF_AVERAGING_CHECK.md); strict root-width and global expectation claims remain open |
| [SELF_AVERAGING_FEEDBACK_ROUTE.md](SELF_AVERAGING_FEEDBACK_ROUTE.md) | Global two-initialization stability on the proved good set; exact controlled commutator reduction and strict one-direction control stability | Complete reconstruction in [SELF_AVERAGING_ROUTE_CHECK.md](SELF_AVERAGING_ROUTE_CHECK.md); its general-data strict restricted-response estimate remains unproved |
| [SELF_AVERAGING_SENSITIVITY_ROUTE.md](SELF_AVERAGING_SENSITIVITY_ROUTE.md) | Exact Gaussian-root derivatives, conditional direct Hessian bound, and explicit mixed directional moments in the flow second variation | Complete reconstruction in [SELF_AVERAGING_ROUTE_CHECK.md](SELF_AVERAGING_ROUTE_CHECK.md); no strict initialization concentration theorem |
| [SELF_AVERAGING_ENERGY_ATTEMPT.md](SELF_AVERAGING_ENERGY_ATTEMPT.md) | Exact adaptive adjoint energy, carrier-budget entropy inequality, and all-time sensitivity identity | Complete reconstruction in [SELF_AVERAGING_ROUTE_CHECK.md](SELF_AVERAGING_ROUTE_CHECK.md); directional entropy and mixed-response closure remain open |
| [DEPTH_TRACKING_ROUTE.md](DEPTH_TRACKING_ROUTE.md) | Arbitrary fixed-depth all-time tracking from an actual dense carrier envelope, using dense histories in the closure's own clock | Complete deterministic reconstruction in [DEPTH_TRACKING_CHECK.md](DEPTH_TRACKING_CHECK.md); probability input is separate |
| [DEPTH_RESPONSE_MODULUS.md](DEPTH_RESPONSE_MODULUS.md) | Conditional backward-response time modulus, Gaussian supremum entropy and two-endpoint Schatten trace | Complete reconstruction in [DEPTH_RESPONSE_MODULUS_CHECK.md](DEPTH_RESPONSE_MODULUS_CHECK.md); does not by itself close the budget |
| [ACTIVATION_EXTENSION_ROUTE.md](ACTIVATION_EXTENSION_ROUTE.md) | Smooth activation classes including linear-growth values, automatic Gaussian feature gaps and exact odd/even data quotients | Complete reconstruction in [ACTIVATION_EXTENSION_CHECK.md](ACTIVATION_EXTENSION_CHECK.md) |
| [DEPTH_CAVITY_ROUTE.md](DEPTH_CAVITY_ROUTE.md) | Actual all-time finite dense carrier maximum at every fixed depth, with bounded smooth activations | Local reconstruction in [DEPTH_INSERTION_CHECK.md](DEPTH_INSERTION_CHECK.md); complete probability reconstruction in [DEPTH_CAVITY_PROBABILITY_CHECK.md](DEPTH_CAVITY_PROBABILITY_CHECK.md) |
| [UNBOUNDED_ACTIVATION_CANDIDATE.md](UNBOUNDED_ACTIVATION_CANDIDATE.md) | Completed joint forward/backward budget and small-label scalar absorption for activations with bounded first three derivatives and linear-growth values; historical candidate filename retained | Local extension in [UNBOUNDED_INSERTION_CHECK.md](UNBOUNDED_INSERTION_CHECK.md), coordinator reconstruction in [DEPTH_INSERTION_CHECK.md](DEPTH_INSERTION_CHECK.md), complete probability chain in [UNBOUNDED_ACTIVATION_CHECK.md](UNBOUNDED_ACTIVATION_CHECK.md) |
| [DEPTH_EXTENSION_RESULT.md](DEPTH_EXTENSION_RESULT.md) | Fixed-depth strict all-time root-width same-width tracking at near-quarter memory order, broad smooth activation class | Synthesis of the complete internally reconstructed local, probability, activation and deterministic comparison arguments |
| [CUTOFF_REMOVAL_ROUTE.md](CUTOFF_REMOVAL_ROUTE.md) | Cap-uniform fitting, common population construction, Gaussian population cutoff error, two-threshold comparison, qualitative finite removal for every diverging cap | Internally checked in [CUTOFF_REMOVAL_CHECK.md](CUTOFF_REMOVAL_CHECK.md) |
| [FINITE_TAIL_ROUTE.md](FINITE_TAIL_ROUTE.md) | Actual finite all-time carrier moments and cutoff inactivity; two hidden layers, orthonormal inputs, tanh first activation, bounded smooth second activation | Independently reconstructed within the study in [FINITE_TAIL_CHECK.md](FINITE_TAIL_CHECK.md) |
| [WIDTH_ROUTE.md](WIDTH_ROUTE.md) | Exact dense histories, root-width initialization at fixed depth, one forward/adjoint return including its bias; repeated adaptive return remains open | Internally checked in [SUPPORTING_RESULTS_CHECK.md](SUPPORTING_RESULTS_CHECK.md) |
| [FIRST_FEEDBACK.md](FIRST_FEEDBACK.md) | One normalized input, two tanh layers: explicit third prediction derivative, \(O(1/n)\) bias and \(O(1/\sqrt n)\) RMS error | Internally checked in [SUPPORTING_RESULTS_CHECK.md](SUPPORTING_RESULTS_CHECK.md) |
| [THREE_ERROR_REASSEMBLY.md](THREE_ERROR_REASSEMBLY.md) | Conditional moment-to-cutoff transfer; all three error terms and the distinction between strict and near-root rates | Internally checked in [SUPPORTING_RESULTS_CHECK.md](SUPPORTING_RESULTS_CHECK.md) and [SYNTHESIS_CHECK.md](SYNTHESIS_CHECK.md) |
| [POPULATION_CAVITY_ATTEMPT.md](POPULATION_CAVITY_ATTEMPT.md) | Root-width fluctuations around the finite-width mean for prescribed deterministic residual controls and training queries; no population-bias or adaptive-control conclusion | Internally reconstructed in [POPULATION_CAVITY_CHECK.md](POPULATION_CAVITY_CHECK.md) |
| [SYNTHESIS_CHECK.md](SYNTHESIS_CHECK.md) | Probability, scope, and three-error accounting in RESULT | Internal reconstruction; not a promotion review |
| [LOSS_MATCHED_VARIATIONS.md](LOSS_MATCHED_VARIATIONS.md) | Exact first and second matched-loss variations, surviving transverse terms, and endpoint regularity diagnostic; smooth finite gradient flows | Internally reconstructed in [LOSS_MATCHED_VARIATIONS_CHECK.md](LOSS_MATCHED_VARIATIONS_CHECK.md) |
| [DENSE_MATCHED_LOSS_LOCAL.md](DENSE_MATCHED_LOSS_LOCAL.md) | Actual one-sample dense path, two-tanh local cancellation test, and conditional same-time transfer | Internally reconstructed in [MATCHED_LOSS_LOCAL_CHECK.md](MATCHED_LOSS_LOCAL_CHECK.md) |
| [NEGATIVE_RATE_ASSESSMENT.md](NEGATIVE_RATE_ASSESSMENT.md) | Fixed-data scope and a quantitative near-coincident two-input initialization diagnostic; no trained negative rate | Internally reconstructed in [MATCHED_LOSS_LOCAL_CHECK.md](MATCHED_LOSS_LOCAL_CHECK.md) |
| [CONTROLLED_FEEDBACK_STABILITY.md](CONTROLLED_FEEDBACK_STABILITY.md) | Deterministic all-time removal of adaptive residual selection, nonlinear remainder Lipschitz bound, bounded passive queries; two tanh layers and orthonormal training inputs | Internally reconstructed in [CONTROLLED_FEEDBACK_CHECK.md](CONTROLLED_FEEDBACK_CHECK.md) |
| [PASSIVE_QUERY_FLUCTUATIONS.md](PASSIVE_QUERY_FLUCTUATIONS.md) | Strict root-width fluctuation about the finite mean for deterministic controls, including the whole time interval and bounded passive query laws | Internally reconstructed in [CONTROLLED_FEEDBACK_CHECK.md](CONTROLLED_FEEDBACK_CHECK.md) |
| [DECISIVE_CONDITIONAL_ROUTE.md](DECISIVE_CONDITIONAL_ROUTE.md) | Exact variance/mobility width doubling, conditional mean-bias rate, and stronger initialization contrast | Internally reconstructed in [DECISIVE_CONDITIONAL_CHECK.md](DECISIVE_CONDITIONAL_CHECK.md); positive-time H remains open |
| [PROFILE_FIRST_FEEDBACK.md](PROFILE_FIRST_FEEDBACK.md) | Stronger profile contrast at the first nonlinear activity coefficient; one training sample, two tanh layers | Internally reconstructed in [PROFILE_FIRST_FEEDBACK_CHECK.md](PROFILE_FIRST_FEEDBACK_CHECK.md); no positive-activity propagation |
| [ROOT_WIDTH_CONDITIONAL_THEOREM.md](ROOT_WIDTH_CONDITIONAL_THEOREM.md) | Complete strict root-width theorem for the actual all-time dense prediction, conditional on the single finite local contrast H; structured data and bounded query domain | Internally reconstructed in Section 6 of [CONTROLLED_FEEDBACK_CHECK.md](CONTROLLED_FEEDBACK_CHECK.md); H remains unproved |
| [AUTONOMOUS_SELF_AVERAGING.md](AUTONOMOUS_SELF_AVERAGING.md) | Unconditional root-width concentration of actual autonomous training around a deterministic finite-width reference; two actual runs differ at root width; same structured scope | Internally reconstructed in [AUTONOMOUS_SELF_AVERAGING_CHECK.md](AUTONOMOUS_SELF_AVERAGING_CHECK.md); quantitative population bias remains open |
| [LARGE_LABEL_ASSESSMENT.md](LARGE_LABEL_ASSESSMENT.md) | One-sample fitting for every fixed label at fixed depth; two-tanh all-time finite concentration for arbitrary fixed labels; exact label-rescaling distinction and non-neural critical diagnostic | Internally reconstructed in [LARGE_LABEL_ASSESSMENT_CHECK.md](LARGE_LABEL_ASSESSMENT_CHECK.md); multi-sample extension and population-bias rate remain open |
| [SAME_WIDTH_COMPARISON_CHECK.md](SAME_WIDTH_COMPARISON_CHECK.md) | Bounded target-comparison check; finite-tail estimate plus manuscript tracking gives pure order error and strict root-width direct compression in the structured small-label scope | Coordinator and fresh scoped agent reconstructed the implication; finite-tail source retains its separate internal check; no population-bias claim |
| [NONORTHOGONAL_DIRECT_ROUTE.md](NONORTHOGONAL_DIRECT_ROUTE.md) | Arbitrary-input two-tanh closure defect of order \(q^{-2}\sqrt{\log q}\); conditional carrier-tail transfer | Internally reconstructed in [NONORTHOGONAL_CHECK.md](NONORTHOGONAL_CHECK.md); source and damping used in the new unconditional order theorem |
| [NONORTHOGONAL_TAIL_ROUTE.md](NONORTHOGONAL_TAIL_ROUTE.md) | Exact carrier evolution and local variational blocks; attempted cavity and tilted-response routes for general geometry | Exact identities checked in [NONORTHOGONAL_CHECK.md](NONORTHOGONAL_CHECK.md); no general finite-tail theorem |
| [GENERAL_DATA_STABILITY_ROUTE.md](GENERAL_DATA_STABILITY_ROUTE.md) | Exact same-width discrepancy energy and root-width tracking conditional on one residual-weighted fourth-moment ratio | Complete reconstruction in [GENERAL_DATA_STABILITY_CHECK.md](GENERAL_DATA_STABILITY_CHECK.md); probabilistic bound remains open |
| [FINITE_MIXED_MOMENT_ROUTE.md](FINITE_MIXED_MOMENT_ROUTE.md) | Conditional averaged finite sensitivity bounds, exact Stein products, and Gaussian transport lemmas without input orthogonality | Complete reconstruction in [FINITE_MIXED_MOMENT_CHECK.md](FINITE_MIXED_MOMENT_CHECK.md); high-probability budget closed in the new positive route, unstopped expectation target remains open |
| [DATA_QUOTIENT_CLOCK.md](DATA_QUOTIENT_CLOCK.md) | Exact signed data quotient, automatic tanh population Gram positivity, fixed-order persistent-clock convergence and endpoint filter isometry | Complete corrected reconstruction in [DATA_QUOTIENT_CHECK.md](DATA_QUOTIENT_CHECK.md); no order-uniform label threshold or tracking lower bound |
| [PERSISTENT_CLOCK_ENDPOINT_DIAGNOSTIC.md](PERSISTENT_CLOCK_ENDPOINT_DIAGNOSTIC.md) | Static historical-pairing replacement and its first query coefficient; no identification with an autonomous endpoint | Coordinator and scoped collaborator checked the complete calculation; sign and actual endpoint application remain open |
| [GENERAL_DATA_ASSESSMENT.md](GENERAL_DATA_ASSESSMENT.md) | Earlier claim inventory and unconditional all-depth root-width fallback with exponential order | Internal route checks plus separate verification of the fallback; its two-tanh open-order assessment is superseded |
| [Q_ORDER_POSITIVE_ROUTE.md](Q_ORDER_POSITIVE_ROUTE.md) | Actual finite carrier maximum and strict all-time root-width same-width comparison at \(q=n^{1/4+o(1)}\), arbitrary fixed compatible sphere data, two tanh layers | Local lemma in [Q_ORDER_INSERTION_CHECK.md](Q_ORDER_INSERTION_CHECK.md); full chain in [Q_ORDER_POSITIVE_PROBABILITY_CHECK.md](Q_ORDER_POSITIVE_PROBABILITY_CHECK.md); exact final status in [Q_ORDER_RESULT.md](Q_ORDER_RESULT.md) |
| [Q_ORDER_LOWER_ROUTE.md](Q_ORDER_LOWER_ROUTE.md) | Frozen negative attempt: residual-mode leakage and endpoint Legendre diagnostics | Author-derived diagnostics; no requested actual-network lower bound and no dependency of the positive proof |
| [Q_ORDER_REGULARITY_ROUTE.md](Q_ORDER_REGULARITY_ROUTE.md) | Actual early-time source and prediction calculations with conservative width dependence | Author-derived calculations; do not establish a necessary memory order at root-width accuracy |
| [Q_ORDER_RESULT.md](Q_ORDER_RESULT.md) | Preceding two-layer tanh theorem, scope, proof mechanism and source/check record | Coordinator synthesis of the full internally reconstructed positive route; scope extended in DEPTH_EXTENSION_RESULT |

No experiment, formal proof assistant, numerical training, manuscript edit, commit, or push was used. Validation consists of complete algebraic/probabilistic reconstruction with source hashes and explicit hypotheses. The coordinator read the complete current manuscript, included theorem/proof files, appendices, and captions. Dependencies on its Gaussian population construction are identified in the proofs rather than attributed to an unrelated study.

The user allowed only bounded, theory-directed experiments and then explicitly ruled out experiments if GPUs were unavailable. The NVIDIA device check could not contact its driver. No training experiment, CPU fallback, device repair, or numerical exponent fit was run.

## Contributors, coordination, and remaining work

The coordinator owns this README, RESULT, FIRST_FEEDBACK, THREE_ERROR_REASSEMBLY, and CUTOFF_REMOVAL_CHECK. Scoped fresh agents authored separate finite-tail, width, and cutoff-removal routes. After their initial concrete candidates, the routes exchanged specific mathematical findings within this study; they are collaborative research, not isolated promotion reviews. The width-route author reconstructed the finite-tail proof and synthesis; the cutoff-removal author reconstructed supporting results and the later prescribed-control fluctuation attempt. Exact read scopes and hashes are retained in their reports. A late metadata-only agent-status query also returned unrelated completed-task summaries; these were not used as scientific inputs or passed to this study's agents.

For the bounded loss-matching assessment, a fresh scoped agent authored LOSS_MATCHED_VARIATIONS; the coordinator authored DENSE_MATCHED_LOSS_LOCAL and NEGATIVE_RATE_ASSESSMENT. They reconstructed each other's frozen candidates and disclosed the coordinator's two mathematical additions to the general note. This was a bounded cancellation and counterexample assessment, not a commitment to a full new proof or an independent promotion review.

For the latest conditional theorem, a fresh scoped collaborator authored DECISIVE_CONDITIONAL_ROUTE and the coordinator authored CONTROLLED_FEEDBACK_STABILITY, PASSIVE_QUERY_FLUCTUATIONS, PROFILE_FIRST_FEEDBACK, ROOT_WIDTH_CONDITIONAL_THEOREM, and AUTONOMOUS_SELF_AVERAGING. They reconstructed each other's frozen candidates; report hashes and input coverage retain the exact versions. These are internal collaborative checks, not independent promotion reviews.

For the large-label follow-up, the coordinator derived and authored LARGE_LABEL_ASSESSMENT. A fresh prompt-only collaborator independently checked the scalar readout-convexity argument and supplied the sharper bounded-top-feature energy proof of global controlled existence. The collaborator was then authorized to reconstruct the complete candidate and its finite-moment dependencies inside this study. No experiment was attempted.

For the fixed-depth extension, a fresh scoped collaborator developed the exact forward/reverse finite deletion argument; another developed the deterministic all-depth source comparison. The coordinator derived the endpoint-response modulus/trace, activation/Gram criteria, and joint forward/backward budget. After initial candidates, the routes exchanged concrete findings. The coordinator reconstructed the complete local insertion and its unbounded-value extension; the second collaborator reconstructed the complete probability arguments and initialization criteria. The bounded source's activation deletion and the unbounded source's top residual offset are explicit. Source hashes and final repairs are recorded in the check files. These are internal collaborative checks, not independent promotion reviews.

For the independent-copy continuation, three existing scoped collaborators
examined initialization sensitivities, controlled feedback, and adjoint
energy. The coordinator derived the scalar-extension concentration proof
and reconstructed their complete route notes. The feedback collaborator
reconstructed the complete near-root theorem, including its probability
qualification and the full time supremum. These are collaborative internal
checks; they are not fresh isolated promotion reviews. The prior strict
two-tanh orthogonal-data self-averaging theorem is unchanged, and the new
general-data theorem is explicitly weaker in rate.
The final route reconstruction corrected one uniform-time qualification:
the omitted adjoint column equation has a response term without a
residual prefactor, so its time integral remains an explicit open
obligation. Final source hashes are recorded in
SELF_AVERAGING_ROUTE_CHECK.md.

For width doubling, the same three scoped collaborators separately
examined the autonomous block endpoint, the balanced profile and local
response contrast, and alternative Gaussian couplings before comparing
their initial derivations. The coordinator supplied the bounded-variation
control refinement, checked the route calculations, and authored the
rate-equivalence synthesis. The coupling collaborator reconstructed the
complete frozen block proof; the block collaborator reconstructed the
complete synthesis. These are internal collaborative checks, not
independent promotion reviews. No experiment or manuscript edit was used.

For the subsequent direct population continuation, two fresh scoped
collaborators pursued direct Gaussian/response comparison and negative
constructions. The negative attempt initially used only its specified
prior-study and manuscript inputs. The positive route exchanged concrete
ideas with the coordinator before its first freeze and is collaborative.
After freezing, the negative-route author reconstructed the complete
local insertion and the subsequent tagged-response/localization note,
finding a conditioning defect that was repaired with a recorded source
diff. The coordinator authored the covariance-coupling theorem and
diagnostic/synthesis records; the direct-route author reconstructed the
covariance theorem. Internal checks do not establish the outstanding
population rate and are not promotion reviews.
The direct-route author subsequently derived the common causal
response transport; the negative-route author reconstructed it.
The coordinator derived the parameter-law transport limitation,
which the direct-route author separately checked.

For the arbitrary-label follow-up, two fresh scoped collaborators pursued
negative constructions and positive geometry separately. Both and the
coordinator independently obtained the finite-target scalar continuation
argument. The coordinator and geometry collaborator independently obtained
the two-hidden-linear balance, then exchanged it. The coordinator developed
the complete spectral-moment/Volterra population-rate proof, which the
geometry collaborator reconstructed in full. The negative collaborator
reconstructed the geometry note and supplied the residual-rotation identity;
the coordinator reconstructed the negative route. Frozen hashes and the
single cosmetic geometry correction are recorded in the checks. These are
collaborative internal reconstructions, not isolated promotion reviews.

For the distinct dense-to-population target, the local profile response contrast H through a fixed small activity interval remains unresolved. Its mobility-response and Gaussian covariance-response terms must be kept together. The cavity remainder contains an order-one population response that must be identified, not dropped. The completed fixed-depth carrier and same-width estimates do not establish that mean-bias contrast. Nonsmooth activations and depth growing with width are also outside the new theorem. No mesh-dependent finite-program estimate currently closes H; cutoff removal and finite-mean concentration must not be restated as the completed population-width theorem.

The population-target request makes that particular profile route optional. The
remaining authorized objective is the actual all-time near-root
dense-to-population theorem or a canonical polynomially slower
prediction example. The direct route now needs a quantitative joint
comparison preserving both orientations of every reused matrix and
the correlations of already queried histories, while retaining
empirical averaging. Separate marginal source couplings and transport
of the whole atomic parameter law do not provide it. This is the
unresolved research step, not an additional hypothesis accepted for
the target theorem.

The arbitrary-label continuation closes that population comparison for
two hidden linear layers and one sample. Its factorially summable spectral
representation is specific to linear activations. The unresolved general
nonlinear comparison must still control the trained finite-width bias;
the scalar and linear counterexample obstructions are not proofs that
all nonlinear large-label trajectories have a root-width rate.

The user's earlier weighted-moment follow-up is assessed in [WEIGHTED_MOMENT_STATUS.md](WEIGHTED_MOMENT_STATUS.md); its then-unattempted general finite route was developed in [FINITE_MIXED_MOMENT_ROUTE.md](FINITE_MIXED_MOMENT_ROUTE.md). Its particular Stein weighted-product closure remains unfinished. The new proof instead combines its averaged sensitivity estimate with finite-set deletion to close a high-probability empirical budget, and then bounds the actual maximum. This supersedes the former absence of any general-data finite-carrier control; it does not prove every previously proposed weighted expectation.

The loss-matched first-response energy offers a more specific open target: a signed, residual-weighted prediction-Hessian quadratic form. Its gate contribution contains the backward carrier times the square of a forward sensitivity, instead of demanding a squared norm bound for every carrier-response product. Neither this expectation estimate nor the required population-bias comparison is proved. An endpoint blowup of second loss-matched derivatives should not itself be interpreted as a negative width-rate mechanism.

For the 2026-10-03 general-data continuation, three fresh scoped collaborators developed direct stability, weighted mixed moments, and the data-quotient/clock route separately before exchanging specific results. The direct-stability and clock authors reconstructed each other's complete candidates; the direct-stability author also checked the mixed-moment candidate. The coordinator authored the static endpoint diagnostic and synthesis, and collaborators checked the diagnostic and expensive-order corollaries. Checks corrected the clock note's missing normalized backward-history factor, its finite initial-time treatment for an arbitrary fixed inconsistency, and the explicit nonnegative transport parameter in the mixed-moment note. All claim limits remain explicit; these are collaborative internal checks, not promotion reviews.

For the subsequent order-gap question, three fresh scoped collaborators independently pursued finite cavity reinsertion, negative constructions, and temporal regularity before freezing their initial candidates. The finite-cavity author developed Q_ORDER_POSITIVE_ROUTE. The negative-route author then reconstructed the complete probability argument, and the regularity-route author reconstructed the local insertion lemma; both disclosed the subsequent within-study exchanges and recorded checked source hashes. The coordinator reconstructed the complete final chain and owns Q_ORDER_RESULT and these README updates. The two negative attempts remain diagnostic work, with no requested necessary-order theorem. The positive argument establishes a strict root-width comparison at a near-quarter order without a remaining probabilistic hypothesis. No promotion, manuscript change, or experiment is part of this result.

New results are research results internal to this study, not established book theorems or independent promotion reviews. No other study was read or modified.
