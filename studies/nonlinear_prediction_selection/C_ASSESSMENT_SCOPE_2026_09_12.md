# Milestone C after A: scope and completion assessment

Assessment date: 2026-09-12. This is a fresh strategic assessment, not a proof of a computational construction or an independent review of A.

**Recommendation.** C should first certify an independent finite approximation of the **original physical population GF on [0,40]**, for one fixed, explicitly represented family containing correlated nonatomic laws. Use A as an optional source of estimates, a mechanism-sensitive comparison, and a possible later acceleration. Do not require a certified slow-episode solver and a certified original-flow solver simultaneously. A solver only for A's projected singular-limit episode would be worthwhile partial progress, but would not complete C's same-GF objective.

The decisive new obligation is manageable approximation of the reused Gaussian evolution. A establishes continuation and nonlinear selection in its scope; it does not establish this approximation. No source read here proves that a useful finite computational representation exists. The recommendation identifies the smallest defensible first target, not a prediction that its computational bottleneck will be easy.

## Reading scope and authority

Read completely: `docs/README.md`, `docs/NOTATION.md`, and C.4.9 of `docs/global_nonlinear.md`, including every proof unit and the source-continuity supplement. Also read the maintained model/theorem statements and observation contracts for C.4, C.4.5, C.4.6, and C.4.7 needed to distinguish the available physical horizons, nonlazy observations, law continuity, and restart domain. The ranges read in the latter file were 3815–3981, 5270–5475, 7066–7169, 8978–9175, and 12994 through the end of C.4.9. The short preceding text in the first range was included by that range selection.

Required process inputs were the investigate-conjectures and solve-math-rigorously skills, plus the research-contract and adversarial-audit references. No study history, prior verdict, other reviewer's report, code, generated data, external source, or Git history was read. No computation, implementation, new proof campaign, or Git operation was performed. This report is the only written artifact.

## What A changes, and what it leaves open

C.4.9 gives an autonomous constrained equation from the fitted reference state, with its moving projector and hidden features recomputed throughout. It proves selection by the actual fixed-mixture flow at physical times `t=τ/ε`, after the initial layer, for the specified single-added-atom compact parameter rectangle with nonempty interior. It also supplies a nonvanishing added-component risk gain and a directly paired second-hidden activation displacement. These are substantive learning results.

The source-tube estimate controls all retained backward-source coefficient rows and Gaussian query tails under a small integrated-control perturbation of the full reference history. Its bounds do not grow with physical elapsed time or the number of source slots. That distinction can be valuable for an eventual solver: long stretches of nearly inactive training need not automatically incur the same stability cost as equally long stretches of substantial force.

However, the estimate retains **every old training source**. A uniformly bounded sum of source coefficients does not by itself identify a small finite subset, bound a usable basis truncation, or control Gaussian quadrature in a growing source dimension. The construction of the endpoint and episode also retains the initialized action and its adjoint. The finite-program construction in A is a mathematical identification and convergence device, not already an executable Gaussian-action replacement with accounted cost.

The distinction is visible in the exact physical identity in proof unit C, equation (34):

\[
\theta'=\varepsilon V_p(\theta)+B(\theta)r'.
\]

The projected slow equation retains the first term after rescaling and taking a justified limit. For fixed positive ε, the normal correction and the initial layer remain part of the original dynamics. C.4.9.NS5 is qualitative, uniform only on slow-time intervals bounded away from zero. Its constants need not be practical, and it gives no quantitative joint width/contamination rate or raw-GD extension. An ε-independent projected solver cannot silently be advertised as an arbitrary-accuracy solver for the fixed-ε physical flow.

## Scope comparison

| First target | Scientific payoff | Extra burden or limitation | Assessment |
|---|---|---|---|
| Original physical GF through 40 on a represented nonatomic family | Directly addresses C's missing independent computation; uses an established nonlinear flow and law-continuity theorem | Gaussian reuse, finite-state approximation, quadrature and useful resource bounds remain unproved | Best primary target |
| Only A's projected slow episode | Directly probes added-data selection and paired hidden adaptation; may avoid resolving a very long physical interval | Still requires computational construction of the reference endpoint and its retained history; approximates a different limiting equation | Valuable component or fallback, not C completion |
| Both physical flow and certified slow acceleration immediately | Gives a broader solver with certified long-time payoff | Adds endpoint construction, singular-limit error, switching/restart, long-horizon cost and single-atom/nonatomic compatibility to the compression problem | Do not make this the initial acceptance gate |
| A as optional test or acceleration | Makes use of new theory without replacing the original target | Empirical agreement with A is not a finite-ε error certificate; certified acceleration needs a separate bridge | Recommended role alongside the primary target |

The choice of 40 is justified by C.4.7's existing physical-flow theorem, not by an inference that A's slow episode fits inside that interval. Original GF at fixed positive mixture weight remains the target throughout. A later extension to `τ₀/ε` can be substantial new mathematics even if the same software runs there.

## A meaningful first theorem

Freeze a family before choosing the requested accuracy. It should have a finite, computable law description and at least genuinely nonatomic members, rather than merely one reference law with renamed parameters. For example, small angular distributions around both reference inputs, with the associated labels and explicitly controlled optional label noise, can be described by densities or pushforwards on fixed low-dimensional domains. Their law approximation should come from that description. A finite collection of atoms approximating such a law is a numerical choice, not a restriction of the scientific target to atomic laws.

The family must be verified to lie inside C.4.7's admitted neighborhood. An existential radius `δ_Y>0` alone does not tell a program which numerical instances are certified. An effective sufficient radius or a checkable instance certificate is needed. The extremely small explicit neighborhood in C.4.5 illustrates a real precision and utility concern; writing its parameters symbolically does not erase the precision cost of resolving their consequences.

For a fixed such family `𝒞`, a suitable completion statement has the following form. Given a finitely described `μ∈𝒞`, a prediction tolerance `η>0`, a specified finite internal-observation request, and, for a randomized construction, failure probability `β>0`, an algorithm constructs and advances a finite autonomous state from the canonical initialization. Its reconstructed prediction satisfies

\[
\Pr\!\left\{\sup_{0\le t\le40,\,x\in\sqrt2S^1}
 |\widehat f_{\mu,\eta}(t,x)-f_\mu(t,x)|>\eta\right\}\le\beta,
\]

with the deterministic counterpart allowed. It also supplies the stated internal accuracy, reached restart guarantee, and explicit total resource bound. The probability and all cost dependencies must identify algorithmic randomness; the population target is not a random finite network chosen as a surrogate.

This is a **proposed contract**, not a theorem established here. Its essential details are:

1. **Same model and one physical clock.** Preserve the two tanh hidden layers, Gaussian initialization, unhalved square loss and stated mobilities. Population zero readout is the prescribed limit of the actual finite Gaussian readout. Replacing it at finite width or changing the training law partway through a run is not authorized by the population convention. An adaptive internal mesh is acceptable if it advances the same physical equation and accounts for its error.
2. **Computable coefficient provenance.** Initial values, Gaussian covariance/response calculations and future updates come from the law description, canonical primitives and current finite state. No target trajectory, inaccessible initialized-action call or fitted trajectory coefficient is permitted. The initialized action is not Hilbert–Schmidt merely because its learned increment is.
3. **Internal observation contract.** At minimum include finite named first-row/readout and forward/adjoint fields, their same-layer second moments, and paired initialized/current hidden observations. C.4.7's admitted observation grammar is a natural target. Support additional finite passive-input requests by a stated reconstruction operation and cost. A single scalar loss curve is insufficient. Cross-carrier raw norms or operator norms must not be written as though finite matrices and population operators lived on the same space.
4. **Reached restart.** A saved finite state must contain the source/response information necessary to continue, including the relevant initialized primitives and random-state metadata. Restart at any reached time through the remaining certified interval must preserve the claimed approximation. Do not reset unresolved Gaussian directions or reconstruct history from future data. Existence from every arbitrary ambient operator state, and changing the law on restart, may be deferred.
5. **Refinement and identification.** Show convergence of the proposed finite representation as its actual resolution parameters are refined, and identify that limit with C.4.7's physical GF. Convergence at each fixed source graph does not supply estimates for graphs growing with time refinement. A correctly differentiated or stable finite recursion is not enough.
6. **Complete error budget.** Bound law quadrature, Gaussian integration/sampling, state or source truncation, time integration, and numerical precision. A propagation estimate must be paired with an estimate for the error generated by the omitted information. If a bound is conditional on a source cap, a tail condition or conditioning of a covariance solve, verify that condition along the generated path or provide a certified stopping rule.
7. **Actual cost and usefulness.** Account for state size, all retained memory, source count, density dimension if any, contractions, covariance solves, quadrature, step count and precision. An explicit complexity expression must be evaluated on at least one meaningful certified case at a stated useful accuracy and resource budget. Merely proving that a finite but astronomical computation exists is a mathematical result short of C's usable-algorithm objective.

Uniformity over a family with fixed representation/regularity bounds is preferable, but an explicit instance-dependent estimate with a verifiable admission test can be a defensible first result. No rate uniform over all Borel laws, all dimensions or all physical horizons is required. The implementation may expose general inputs while the theorem covers a smaller class.

The family cannot shrink to the reference as η decreases. Otherwise returning the reference prediction could evade the changed-law computation. Conversely, demanding practical resolution of the effect of **every** admitted perturbation would be inappropriate: perturbations can be arbitrarily close to zero. Report separately whether the concrete certified resource example resolves a changed-law effect or only gives useful absolute accuracy for the trained prediction. The latter can establish computational utility on a nonlinear learned path, but cannot be described as a numerical demonstration of finite added-data adaptation. A's nonvanishing adaptation scale need not become a mandatory first-C requirement.

## Legitimate quadrature and statistical representatives

**Data quadrature is legitimate.** Replacing a represented nonatomic law by a finite quadrature law changes a data integral, not the hidden architecture. C.4.7.NL provides the relevant law-continuity bridge while both laws stay in its admitted neighborhood. A quantitative quadrature estimate must be composed with that modulus. Using independent samples instead is also legitimate, with probability and sample cost included. Training a dense network on that quadrature law would still be finite-network simulation, not C's independent solver.

**Statistical representatives of population fields can be legitimate.** They may approximate expectations of a derived source/response system, use correlated Gaussian primitives and evolve the field values needed by that system. The construction must preserve the conditional correlations caused by both action directions and reuse. Calling every new action output an independent Gaussian is invalid; correctly generated unexplored Gaussian innovations conditional on the retained source information are a different matter.

The boundary is structural, not a prohibition on all arrays or all square matrices. A finite covariance or response Gram matrix in a derived Gaussian computation may be essential and admissible. Its size, conditioning and cost must be counted. A finite matrix whose entries are the original trainable all-to-all hidden connections, updated by the same dense network GF, is a renamed network. Replacing neuron width `n` by a representative count `N` does not change that fact. Likewise, a density over one coordinate per accumulated source can hide a prohibitive quadrature problem despite being called one field.

The independence test should ask what finite state is evolved, why it closes with controlled error, what information each coefficient uses, and which refinement produces the continuum target. Independence does not require a wholly unrelated mathematics or deterministic quadrature; it requires a computational representation distinct from resimulating the raw neural parameters. Independent finite networks remain useful validation comparators. Their trajectories must not supply solver coefficients or fitted closure terms.

## What to defer, and what cannot be deferred

Defer arbitrary laws, arbitrary depth, altered activations, arbitrary-state restart, all-time convergence, simultaneous width/ε rates, final changed-law endpoints, generalization or architectural-superiority theorems, and a proof of speedup over every network simulator. Also defer a certified connection from every candidate future learning family to this solver. The roadmap explicitly allows a later compatibility milestone if that connection needs new mathematics.

For A-based acceleration, separately account for reference-endpoint initialization, the initial physical layer, the finite-ε slow-approximation error, projected evolution error and any splice/restart error. A qualitative `ε→0` theorem is not yet a computable tolerance rule for a chosen ε. Approximation of A's constrained equation may be delivered as a named partial result without claiming those missing bounds.

Do not defer the finite-state definition, full Gaussian reuse, same-GF identification, accuracy of named internal observations, legitimate reached restart, or total cost. These are the substance of C, not optional polish. A practical implementation without the identification/error theorem, and a convergence theorem with no usable resource realization, are different forms of partial progress.

Beyond the certified regime, keep the same computable equations available for larger law perturbations, wider correlations and longer physical horizons whenever their operations remain meaningful. Empirical conclusions require separately refined time steps, source/state resolution and quadrature or sample counts, together with precision checks and independent increasing-width network comparisons. Report conditioning failures and failed refinements. Agreement on prediction alone does not verify the retained internal mechanism. These are proposed validation requirements, not authorization for experiments in this assessment.

## Highest-leverage next decision

Before investing in a broad solver or another long-time theorem, require one concrete candidate representation to exhibit its exact causal variables and the first omitted-source or omitted-mode error. Ask whether that error admits a quantitative bound at a useful size while retaining forward/adjoint reuse. A's integrated-force bounds may then improve the propagation or time-resolution estimate. If no such quantitative omission bound is available, the compression question remains open even when all retained fields have bounded moments.

This decision keeps the primary C contract intact, uses A where it supplies real mathematical leverage, and avoids coupling the first computational result to every long-time and learning-family obligation at once.
