# Baseline design for initialization-derived dictionary closures

Status: design only. No experiments, computed evidence, literature assessment, or claim of novelty. This is a scoped proposal based exclusively on the supervisor's assignment and clarifications, with the required investigate-conjectures skill and its research-contract and decisive-experiments references used for process. No other study files or scientific sources were read. This document supplies no new scientific input from another study.

## Decision question and fixed target

Does the proposed initialization-derived population dictionary deliver a better autonomous trajectory-error versus total-cost curve than strong alternatives with the same information access? Separate three possible advantages: a better approximation space, a more faithful closed evolution in that space, and a numerically better parameterization.

The assigned reference is a fully trained dense tanh network with L hidden layers, fixed input dimension d=2, independent first-layer rows N(0,I), hidden matrices with entries N(0,1/n), stored initial readout entries N(0,1/n²), output cᵀh_L/n, unhalved probability-weighted squared loss, and mobilities (n,1,...,1,n). These conventions must be preserved in the dense reference. The population closure retains moving first-layer rows w and readout c, frozen joint population features b_l, and L−1 trained coefficient matrices M_l. Its hidden interaction is

    z_l = b_lᵀ M_l E[b_(l−1) h_(l−1)],

and reverse propagation uses the actual transpose. Architecture-preserving controls replace the dictionary, not these defining ingredients. Freeze the coefficient-mobility rule before comparing them. Output-only models are a separately labeled utility comparison.

The initial work should test finite, declared widths, ranks, tasks, and horizons. A rank trend at fixed width is distinct from a width trend at fixed rank. No proposed test establishes a continuum limit, convergence of a hierarchy, or arbitrary-accuracy existence.

## 1. Information classes

Every construction, initialization rule, hyperparameter selector, and checkpoint operation receives an access label. A benchmark table must not silently mix these classes.

| Class | Permitted construction information | Forbidden construction information | Interpretation |
|---|---|---|---|
| I0: seed and model only | Realized initialization, architecture, declared probability law, independent construction randomness | Realized training inputs or labels; positive-time dense states | Strict initialization-only geometry |
| IX: initial input-aware | I0 plus training inputs and their probability weights; forward evaluations at time zero | Training labels; positive-time dense states | Input-adapted initialization geometry |
| IY: initial label-aware | IX plus labels, exact initial vector field, and explicitly computed derivatives or responses at time zero | Positive-time dense states; fitted future responses | Supervised initialization geometry |
| Pτ: past-snapshot | A declared initial dense trajectory through fixed time τ, then a frozen construction and autonomous continuation | Dense states after τ; later oracle refreshes | Training-assisted compression; charge acquisition cost |
| O: future-snapshot oracle | All prescribed dense trajectory snapshots in the evaluation horizon | Nothing within that declared oracle record | Representation and closure diagnostic; not initialization-only evidence |

Independent construction randomness is permitted at the relevant class, but it must not select winners by evaluated trajectory error. Hyperparameter development may use separate calibration instances, with its cost and provenance recorded. Calibration instances are not evaluation seeds. Selecting a method against the evaluated future trajectory makes that selection oracle access even if its final features are functions of initial variables.

Classes describe access used to construct or select the frozen representation. Ordinary supervised training of the surrogate subsequently uses the assigned training inputs and labels; this does not turn an I0 dictionary into an IY construction.

### Zero initial backward fields

Do not normalize zero backward snapshot columns. If the exact population initialization has zero readout, its true initial backward fields are zero. The finite reference's small Gaussian stored readout is not identically zero; any rescaling of its backward snapshots must declare which finite-width or limiting quantity is being studied.

Two valid initialization constructions can replace the unavailable nonzero true backward snapshots, but their provenance and meaning differ:

- **Explicit probe responses:** substitute a declared nonzero readout probe into the initial adjoint calculation, or inject a declared probe at a named hidden population. This is a synthetic response, not the actual initial backward field. A nonzero output cotangent alone does not repair a zero readout: propagation through the zero readout remains zero. Choose probe distributions and counts without observing future trajectories. Probe choice may be label-free or label-aware and must be labeled accordingly.
- **First nonzero initial response:** compute a specified derivative from the exact initial vector field, for example a response driven by the initial readout velocity when that is nonzero. State the derivative order and label dependence. This is IY if it uses labels. A small positive-time dense snapshot is Pτ, not an initial derivative merely because τ is small.

If neither construction yields nonzero, informative columns under the permitted access, report the backward part as absent. Do not add numerical noise and call it backward information.

## 2. Distinguish three evaluation modes

1. **Offline representation:** project prescribed dense states, forward fields, adjoint fields, or operators into a fixed dictionary. Future states may be used for evaluation without giving the construction future access. Oracle-selected dictionaries must remain labeled O.
2. **Local closed-vector-field check:** initialize the reduced state using a declared projection of a dense checkpoint and compare the reduced derivative with the projected dense derivative. This isolates a local closure defect. A checkpoint reset is oracle-assisted for that checkpoint and is not an autonomous continuation from time zero.
3. **Autonomous rollout:** initialize once using permitted information, integrate the prescribed closed dynamics, and do not refresh features, coefficients, or states from the dense reference. Restart from the surrogate's own saved current state to check that hidden history or dense-state access is unnecessary.

An offline projection can explain why a dictionary has representational promise. It cannot demonstrate autonomous fidelity. Oracle snapshot reconstruction errors bound only the corresponding linear reconstruction problem, not the error of an arbitrary nonlinear rollout.

## 3. Baseline families

### 3.1 Generic population vectors and population subspaces

Use independent Gaussian coordinate vectors on each n-neuron population, then normalize and orthogonalize in the same population inner product used by the closure. Also use independent Haar-distributed rank-r_l population subspaces. Match layerwise ranks, construction seeds, initialization rules, and closure dynamics.

These are random coordinates on the finite neuron population. They are not necessarily evaluations of a fixed-dimensional function of a neuron's initialization marks. Their n×r_l storage must be charged. Distinguish:

- a random orthogonal **span**, sampled in the ambient population, which changes the approximation space;
- an orthogonal change of coordinates **inside the same span**, which does not change the approximation space and is an invariance control;
- arbitrary unnormalized Gaussian features, whose conditioning can be substantially different and which are only a weak control if compared against a well-conditioned proposed basis.

Use multiple random draws, retaining failures and the entire declared aggregation rather than selecting the best draw on evaluation trajectories. Include a full-rank check only as an implementation sanity check; full ambient rank is not compression evidence.

### 3.2 Functions of permitted initialization marks

For every population, explicitly identify the mark vector ξ_l from which the proposed dictionary's rows are computed. A mark is a declared collection of initialization-derived quantities; its dimension, extraction cost, and any retained arrays count toward complexity.

Strong comparisons include orthogonal-polynomial/Galerkin features on the same ξ_l, Hermite features when the selected coordinates and measure justify them, and random nonlinear features such as cos(ωᵀξ_l+β). Choose degree, feature count, and any frequency scale on calibration instances, then freeze them. Use the actual empirical population inner product for conditioning checks.

Do not pretend an arbitrary neuron index has a physical Fourier geometry. Do not grant mark-function baselines a hidden full trajectory, an inaccessible finite-dimensional latent description, or a cheaper mark-extraction process than the proposed construction. Conversely, do not handicap them with poorer initialization information. If no common mark representation is defined, mark-function RFF/Galerkin remain conditional proposals rather than fully specified comparators.

Ordinary RFF or Galerkin features of the external input x are different objects. They enter the output-utility tier below unless a precise population-space lift and its dynamics are supplied.

### 3.3 Forward, adjoint, joint, and balanced snapshot bases

For each admissible access class, compare forward-only POD/PCA, adjoint-only POD/PCA where nonzero adjoint information exists, and a joint basis formed from both snapshot families. Use probability weights over input samples and declared time weights over snapshots. For initialization-only backward information, apply the zero-field rules above.

Build the same basis for both roles at a population when retaining the stipulated transpose closure. Independently selected forward trial and backward test spaces would create an additional Petrov–Galerkin model class and must be labeled as such.

For joint POD, disclose how each family is scaled; differing physical units or vanishing amplitudes otherwise determine the result. Forward neural activations and network backpropagation fields support a joint forward/sensitivity POD control. They do not, merely by being called forward and backward snapshots, define genuine balanced POD of the training dynamics.

A genuine balanced-POD baseline must first specify the dynamical system being reduced, its inputs and outputs, the chosen trajectory or equilibrium linearization where needed, and the actual adjoint of that dynamical system. Its forward and adjoint response factors then have declared reachability and observability meanings. A neural-network backpropagation vector is not automatically a state of that dynamical adjoint. If these system definitions and adjoint responses are not supplied, retain the name joint forward/backward POD and do not claim balanced truncation. Genuine balanced constructions require declared conditioning and singular-value truncation. If they produce distinct trial/test spaces, compare either their orthonormal union within the common-basis closure, charging its full rank, or label the resulting biorthogonal dynamics as a separate baseline.

Past-snapshot and oracle tiers may additionally include temporal differences or vector-field snapshots. Charge all additional snapshot production. A union can require more columns than either constituent; match its final rank or compare at equal total cost rather than granting free capacity.

### 3.4 Krylov and adjoint enrichment

Start from the same permitted seed vectors as the proposed dictionary or a declared input/label/probe family. Generate a bounded number of applications of initialized forward operators, their actual adjoints, or specified initial linearized response operators; orthogonalize each population's accumulated vectors and use the resulting frozen span in the common closure.

Specify the map's domain and codomain. A forward or adjoint operator can move a vector between populations; a within-population Krylov power requires a declared compatible composition, such as A* A. Since tanh derivatives depend on the chosen initial input state, specify whether applications use individual input states, a weighted aggregate, or a union of resulting vectors. Do not replace that dependence with an unexplained universal operator.

Freeze depth/order, seeds, and rank before evaluation. Initial-operator enrichment is initialization access; enrichment using evolving dense operators is Pτ or O. Constructing the feature set once with dense matrix products may be admissible but is not cost-free. This baseline tests whether ordinary response-space enrichment explains the proposed structure.

### 3.5 Nyström, landmarks, and coarsened neurons

Include coordinate/landmark neuron subspaces, uniformly sampled neurons, and permitted-information leverage or diversity sampling. A coordinate basis can be normalized in the population inner product; it should then run through the same closure with the same coefficient initialization rule.

For a Nyström control, name the positive semidefinite kernel or Gram operator being approximated and the allowed information used to select landmarks. Report kernel construction, landmark selection, solve conditioning, and all retained blocks. Do not assume an arbitrary dense hidden matrix is itself a symmetric positive semidefinite kernel.

For coarsening, partition neurons using declared initial marks and use normalized cell indicators as a common population dictionary. Compare uniform/random partitions with input-aware or mark-aware clustering at the same final rank. This tests whether simple quantization or representative-neuron aggregation suffices.

A separate narrow-network or sampled-subnetwork model can test utility at a similar online budget, but changes to normalization, sampling weights, training geometry, or architecture must be explicit. It is not automatically the same dictionary closure.

### 3.6 Low-rank-update and simple-output explanations

As an oracle diagnostic, inspect low-rank approximations of hidden matrix increments W_l(t)−W_l(0). As a stronger dynamical alternative, preserve W_l(0) exactly and train low-rank increments. This asks whether initialized dense transport plus simple update structure explains the success. Charge its dense initial storage and multiplication; it is not a low-storage population closure merely because its trainable increment is small.

Compare output behavior with low-degree regression, input RFF/Galerkin, initialized random-feature predictors, and a frozen-tangent predictor. These test whether the chosen tasks, outputs, or regime are sufficiently simple that sophisticated closures are unnecessary. Report their training/prediction objective and clock conventions. Matching a final fitted output or loss does not establish a match of the dense training trajectory.

## 4. Same-span and alignment controls

Let B_l be the n×r_l matrix of dictionary rows. Under the uniform empirical population measure, the represented hidden matrix is

    A_l = B_l M_l B_(l−1)ᵀ / n.

For invertible S_l, replacing B_l by B_l S_l and replacing

    M_l by S_l^(-1) M_l S_(l−1)^(-T)

preserves A_l. This supplies a same-span control, including whitening when the empirical Gram is nonsingular. Singular directions require an explicit rank truncation; dropping them changes the approximation space.

Parameterization equivalence also requires the correct dynamics. If reduced coordinates satisfy θ′=Tθ and the original gradient dynamics are θdot=−K∇_θF, the equivalent transformed mobility is K′=T K Tᵀ. Reusing an unchanged Euclidean coefficient mobility after a general whitening transform defines a different optimization dynamics. Compare such an optimizer only as a labeled conditioning/mobility ablation. An orthogonal within-span rotation with a compatible isotropic coefficient metric is an especially clean invariance check.

The supervisor supplied an additional construction-specific distinction: the maintained ridge-normalized dictionary mechanism uses Q=UU*, a positive contraction that need not be an orthogonal projector. Here U denotes the ridge-normalized feature embedding, and * its adjoint in the declared inner products. Therefore the span alone does not determine the native filtering operation. QR or whitening followed by recomputation of the native initialized operator from the new features can change that filter as well as the coefficient-gradient metric. To claim invariance, transport the already represented initialized operator, coefficient state, and mobility together; do not regenerate native initialization from whitened features with identity mobility and call it the same model. Orthogonal coordinate rotations preserve the native Gram/ridge construction directly. A separate comparison that replaces the contraction with an orthogonal projection is an explicit filter ablation, even if the range is the same.

To test initialization alignment, permute complete rows of B_l relative to the initialized network. This preserves the dictionary Gram matrix and multiset of row vectors while disrupting their assignment to neurons. Recompute coefficients by the same declared initialization procedure and report the changed initial error. Do not interpret later degradation as an alignment-only effect if a larger initial mismatch already explains it. Random ambient orthogonal scrambling is another changed-span control but need not preserve row statistics.

## 5. Fairness, metrics, and numerical validity

Compare at both equal layerwise ranks and equal measured storage/online budgets. Count frozen dictionaries, mark-generation dependencies, moving w and c, all M_l, stored dense operators, snapshot buffers, construction work, and solver work. In particular, moving first rows and readout already retain order-n state in this finite population implementation. A coefficient count of order r² is not the whole state size.

Freeze a common coefficient-initialization rule. Weight projection, initial-output fitting, and fitting several initial derivatives are different rules with different data access and cost; do not let one method use all three while another receives only one. Record initial approximation error separately from accumulated rollout error.

Primary output metric: supremum over the prescribed time checkpoints of probability-weighted RMS output discrepancy on held-out inputs. Declare a common, nonzero normalization before comparing methods; an approximately zero initial output is not a reliable denominator. Also report training-input output discrepancy, loss discrepancy, and the unnormalized output error.

Mechanistic diagnostics: forward and adjoint reconstruction errors in named norms, initial and checkpoint vector-field defects, dense and surrogate feature movement, and autonomous trajectory error. Normalize families using declared reference scales and retain raw values. Zero-energy families require explicit absent/zero handling. Matrix Frobenius error is informative about matrix approximation, but does not replace an output or dynamical metric.

Numerical gates include time-step or tolerance refinement, actual-transpose and gradient consistency checks, population-weight consistency, conditioning/rank thresholds, and common-reference consistency. Validating the reference and representative difficult cases is preferable to repeatedly running every redundant check. Distinguish numerical invalidity from scientific failure.

Use paired initialization seeds and identical tasks, probability weights, stopping horizons, and evaluated input sets. Match tuning budgets. Do not tune time rescalings or choose favorable checkpoints against the evaluated dense trajectory. Report failures, excluded runs, and their preregistered reasons. Wall time should accompany operation/storage counts because implementations can have different overheads.

## 6. Bounded experimental packages for later authorization

These are design packages, not permission to execute. Before implementation, freeze actual tasks, L, widths, ranks, horizon, tolerances, thresholds, seed count, run count, and terminal resource budget. The assignment does not supply defensible numerical values for those choices.

### Package A: autonomous usefulness at equal access

Use the proposed initialization dictionary, orthogonal random subspaces, and the strongest available initialization joint forward/response POD at a small fixed rank ladder. Add a mark-function or Krylov comparator if the proposed construction's mechanism makes it the stronger alternative. Preserve a genuinely feature-moving regime and enough multilayer interaction to exercise the claimed closure; do not rely exclusively on a near-frozen-feature task.

Measure offline reconstruction, local vector-field defect, and autonomous rollout error separately. Compare both rank and total-cost curves. A meaningful advantage over random orthogonal spaces and ordinary initialized response spaces supports empirical usefulness; parity leaves a generic-subspace explanation viable.

### Package B: conditioning and alignment

Apply a metric-correct same-span transformation that also preserves the represented initial operator and any ridge filter, normalized changed-span controls, and the row-permutation alignment ablation. Equivalent same-span runs must agree within numerical tolerance. Native reinitialization after whitening is a separate filter/optimizer ablation. If a proposed advantage disappears after a controlled conditioning intervention that preserves the operator and intended dynamics, conditioning remains a sufficient explanation. If permuting initialization alignment worsens performance, check whether the initial projection error accounts for the difference before attributing it to dynamic structure.

### Package C: PCA, enrichment, and low-rank alternatives

If Package A leaves a material unresolved gap, compare a fixed past-snapshot tier using forward-only, backward/response-only, joint, and suitably balanced POD. Include a bounded Krylov/adjoint or landmark/coarsening control if not already used. Reserve future POD and matrix-increment SVD for oracle diagnostics. The dense-initialization-plus-low-rank-update control isolates whether compressing the initial operator is the obstacle.

Good oracle reconstruction with poor rollout points toward a closure or stability problem; poor oracle reconstruction identifies a limitation of the tested rank and reconstruction family. Neither result settles every admissible dictionary.

### Package D: simple tasks and transfer

Evaluate output-side predictors, held-out inputs, unseen initialization seeds, and a predeclared task/label perturbation family. A simple predictor matching output accuracy at lower cost weakens the case for the closure on those tasks. It does not establish equivalence of hidden dynamics. Separately vary width at fixed rank and rank at fixed width; avoid merging these approximation axes.

### Outcome and stopping rules

Before execution, define an error/cost advantage threshold, an indifference region, numerical gates, a paired replication rule, an explicit conditional follow-up, and a total terminal budget. A pass updates only the named empirical utility or mechanism claim. A failure can reject the current construction or a proposed explanation without rejecting general finite-representation existence. Inconclusive comparisons stop unless their specific resolution was preauthorized.

## Recommended first comparison

Begin with Package A plus the inexpensive metric-correct same-span check from Package B. The key discriminator is whether a permitted initialization-derived dictionary predicts the autonomous dense trajectory better per total cost than random orthogonal and ordinary initialized forward/response spaces. Treat snapshot access, operator preservation, and simple-output alternatives as explicit subsequent explanations, not interchangeable evidence for the same claim.
