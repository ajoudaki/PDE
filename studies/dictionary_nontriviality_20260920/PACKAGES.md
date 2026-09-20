# C-N1–C-N4: numerical tests of dictionary value

2026-09-20. Proposed experimental package contracts, local to this study.
These labels do not edit the established roadmap. This document specifies
comparisons; no experiment or empirical superiority claim has been made.
Revision 2 incorporates the five scoped design-review findings. The first
reviewed version is retained as PACKAGES_V1.md; PACKAGE_CHECK.md records its
hash and the original findings. This contract governs implementation choices
where the initial proposal memos differ.

## Central question and possible answers

Does the initialized forward/adjoint dictionary give more faithful autonomous
training dynamics per unit of actual resource than simpler dictionaries?
The tests must allow four informative answers: generic features suffice;
ordinary low-rank or response information explains the benefit; a particular
ingredient of the dictionary helps; or the comparison remains unresolved.
Convergence of a hierarchy alone establishes none of these efficiency claims.

The maintained candidate is the complete C-H3 dictionary in
`docs/global_nonlinear.md`, C.4.7.10 B and C.1: Chebyshev products in initialized
forward/reverse marks, the exhaustive initialized-word additions, its positive
ridge schedule, complete joint marks, and the autonomous coefficient/endpoint
equations. Its exact two-layer state and dynamics are C.4.7.9 (H2.3)–(H2.6).
Its ridge embedding produces a positive contraction, not generally an
orthogonal projection. Every run must identify the exact full or ablated
dictionary, rather than call a small polynomial core the full hierarchy.

Depth variants are to be defined afresh from the maintained finite network
and typed projection construction, with a versioned adapter. No other study's
unpromoted implementation or proof is imported. An empirical finite-depth
comparison does not require or establish a population continuation theorem.

## Common model and comparison rules

Start with d=2, bias-free tanh in every hidden layer, normalized unit inputs,
independent Gaussian first rows of covariance I, hidden entries of variance
1/n and stored readout entries of variance 1/n^2. Use output c^T h_L/n,
unhalved probability-weighted square loss, and mobilities (n,1,...,1,n).
The finite reference retains its actual random readout. A canonical population
closure starts with the prescribed limiting zero readout; any discrepancy
between these initializations must be exposed rather than silently removed.

Compare two explicitly different settings:

1. **Common finite population.** Fix the same initialized dense matrices and
   n-neuron populations for every dictionary. Compute each initial coefficient
   block by the same declared weighted action contraction. Evolve the same
   projected gradient equations with all endpoint rows/readouts and coefficient
   blocks trainable, and actual transposes. This isolates representation and
   filtering at finite n. Its stored n-by-r mark tables and n endpoint rows
   are width-dependent and fully charged. All entrants start with the same
   actual finite first rows and random readout as that dense reference.
2. **Population implementation.** Construct each permitted dictionary's joint
   mark law and initialization from its advertised inputs; approximate it using
   P_l nodes independently of dense-reference width. Retain all joint marks,
   endpoint variables, coefficients and construction metadata. A method needs
   an explicit descriptor/replay or extension rule to enter this comparison.
   A neuron-index POD vector alone supplies no such rule. The common-finite-
   population experiment cannot be relabelled a width-independent solver.

L=2 is the implementation and established-model anchor; L=3 is the first
depth stress. L=5 and higher input dimensions belong to the transfer package,
after a useful comparison is resolved at lower cost. Depth and horizon changes
are labelled empirical extensions unless a matching established theorem exists.

All methods in the main comparison use the same frozen-basis closure equations.
Dictionary selection, coefficient evolution, population integration and
nonlinear hyper-reduction are separate interventions. Ordinary Galerkin is
the framework for projection, not a unique competing dictionary. Petrov–
Galerkin/LSPG and moving bases are separate dynamics comparisons, with their
own metrics and evaluation costs, if the fixed-basis tests justify them.

### Information access

Use separate labels and comparisons for:

- I0: model and initialization only; no realized training data for basis choice.
- IX: I0 plus training inputs/weights and initial forward or synthetic adjoint
  probes; no labels for basis choice.
- IY: IX plus labels and explicitly computed initial responses.
- P_tau: dense snapshots only up to a predeclared burn-in tau, followed by a
  frozen basis and autonomous continuation. Charge the dense burn-in.
- O: evaluated future snapshots, used only for an explicitly labelled oracle
  compression diagnostic.

All surrogates subsequently train on the same labelled training data. The
labels above concern basis construction and tuning, not access during training.
Within every class use equal hyperparameter search budgets and disjoint
calibration and confirmation instances. Compare the candidate with alternatives
given the same extra information before attributing an advantage to its design.

At zero population readout the true initial backward fields vanish. Therefore
initialization backward-PCA must use declared nonzero artificial readout/hidden
probes, or a specified first nonzero initial response driven by the exact
initial vector field. The latter can depend on labels. Neither is a positive-
time snapshot, and neither may be described as nonzero true backprop at t=0.

### Metrics and costs

Let U_test be held-out unit-circle inputs with fixed probability weights nu,
and let T_grid contain the common evaluation times. For prediction error use

    E_f = max_t ||f_red(t)-f_ref(t)||_(L2(nu))
          / max(max_t ||f_ref(t)-f_ref(0)||_(L2(nu)),
                0.1 ||y||_(L2(nu))).

Also retain the unnormalized discrepancy and the numerator/denominator. The
0.1 floor is a declared numerical convention, not a theorem. It prevents
division by a vanishing initial prediction. A separate change-relative error
without that floor is reported only when the reference change is resolved
well above numerical uncertainty. Include off-grid maximum prediction error
and loss-trajectory error as secondary checks.

Hidden-dynamics fidelity is co-primary for a claim about the closure:
per-layer errors of H(t)-H(0), preactivations, nonzero backward fields, and
their input Gram trajectories. On a common finite carrier use paired RMS;
on different population clouds compare complete initial/current joint laws
and Gram observables, not arbitrary row-index pairings. If sliced Wasserstein
is used, call it that diagnostic rather than exact multidimensional W2.
Record both absolute and change-relative errors and sign/direction alignment;
matching norms or loss alone does not match representations.

Those laws live in a common physical observable space. For each fixed layer
and the same declared inputs u_j, use the tuple of initial/current
preactivations and activations, current backpropagated fields Delta_l and
incoming fields q_l (q_L=c). Each initial/current pair is evaluated on the
same neuron within its own population. Layer one can additionally include
the initial/current first row. The tuple never includes candidate-specific
dictionary coordinates. Fix the input list, component scales and norm in the
manifest; report per-component errors as well as any combined metric. Separate
the initial-field error from the law of H_l(t)-H_l(0), normalized by the
resolved dense motion. All methods reconstruct the same quantities or state
that the corresponding fidelity claim is unavailable. A finite family of law
diagnostics is not described as equality of every possible joint observable.

At reference snapshots also measure offline projection error and the defect
between the projected dense vector field and the reduced vector field at the
projected state. These are diagnostics, not autonomous forecasts. Keep initial
operator/field mismatch separate from subsequent accumulated error. Never
compare basis-dependent raw coefficient matrices without mapping them to the
represented actions or observables.

Report error against (a) actual layerwise ranks, (b) all retained scalar bytes,
(c) peak working memory, (d) measured online time, and (e) end-to-end time.
Count descriptors, joint mark arrays, endpoint rows/readouts, every coefficient
and initial block, initialization matrix products, snapshot acquisition,
nonlinear evaluations, solver work, precision and any dense operators retained.
Include CPU/GPU type and threads. Amortized costs require a stated number of
tasks; also report the single-task cost. Match actual dimensions, not the
nominal order p across unrelated bases. Record effective Gram/filter spectra
in addition to literal stored dimension; never silently delete candidate modes.

## C-N1. Does a generic dictionary work just as well?

**Question.** Is the candidate's autonomous error/cost curve better than strong
initialization-only alternatives, or is its apparent quality generic?

**Required baseline families:**

| Family | Concrete construction and role |
|---|---|
| Isotropic random span | Gaussian or Rademacher neuron vectors, properly normalized; QR/Haar version as the strong random-space control. Finite-population storage is charged. |
| Random mark features | Random tanh features and random Fourier features cos(omega dot z + b) of the same permitted initialization descriptors z. Tune scales only on calibration cases. |
| Orthogonal random Fourier features | Orthogonal frequency blocks with the appropriate radial distribution, on those same descriptors; this changes the sampled span, unlike rotating existing columns. |
| Initialization POD | Forward snapshots, declared nonzero adjoint probes, and their explicitly weighted union; include label-aware initial-response POD only in IY. |
| Simple mark-space approximation | Kernel/Nyström landmark columns or piecewise-constant mark clustering; compare uniform and information-matched landmark selection. |
| Krylov/adjoint enrichment | A small seed bank followed by a fixed number of typed initialized forward/adjoint applications, optionally bounded tanh transforms, then a declared rank reduction. |

Generic polynomial families on the identical descriptors and with the same
complete degree span are primarily coordinate/filter controls: Chebyshev versus
Legendre alone may leave the span unchanged. Random projections of a common
larger candidate pool provide another fair span-selection test if that pool's
construction cost is charged to every user of it.

**First screen.** Use the candidate, a random orthogonal span, mark-space RFF,
initialization joint forward/probe POD, Krylov/adjoint enrichment, and one
uniform Nyström or clustering alternative: six methods at three actual rank
budgets. Select which landmark method on calibration data before screening.
RFF/ORF, random tanh and polynomial reparameterizations are bounded follow-ups,
not an automatic multiplication of the first grid.

**Deliverable.** Paired reconstruction/defect/rollout and cost curves, full
initialization specifications, failed-run records and a clear generic-match,
candidate-advantage or inconclusive outcome. At least the strongest generic
competitor selected in screening must be tested on fresh confirmation seeds.

## C-N2. Is ordinary low-rank or PCA structure the explanation?

**Question.** Does success come from a small forward/adjoint snapshot span or
small learned matrix increments, rather than the full initialized-word design?

Compare forward-only, adjoint-only and joint POD at equal final layerwise rank.
Normalize snapshot families by a calibration-only rule; do not let a larger
physical scale receive almost every mode by accident. Evaluate both snapshots
and their changes from initialization, because high-variance static structure
can hide the smaller learned directions. Add vector-field snapshots only with
their access class and acquisition cost declared.

Use three distinct tests: initial probes (I0/IX/IY), an early burn-in with basis
frozen at tau (P_tau), and full-horizon oracle POD (O). Future-POD reconstruction
is a diagnostic of the best tested linear snapshot representation. It is not
a lower bound on nonlinear autonomous rollout error. Starting a predictor from
the dense state at tau is training-assisted compression, not an initialization-
only forecast; test its continuation beyond the snapshot window.

A POD basis indexed by one network's neurons cannot be transferred to another
random initialization merely by matching column numbers. For transfer, either
rebuild from that new network's legitimately available snapshots, or fit an
explicit descriptor-to-basis extension on donor data and charge its training,
parameters and error. Do not import future evaluation snapshots into that fit.

Also inspect singular values of learned increments K_l(t)=W_l(t)-W_l(0),
their vector fields and a union across time. A dense-initialization-plus-trained-
low-rank-update control isolates whether preserving the random initial operator
is the main benefit. Its dense initial memory and products remain in the cost.

Joint neural forward/backward POD is not automatically balanced POD. A genuine
balanced-POD alternative requires a specified dynamical linearization, inputs,
outputs and the actual adjoint of the training dynamics. Retain it as a later
control if the cheaper joint-POD result leaves an output-sensitivity question.

**Deliverable.** A representation-versus-rollout panel and an access/cost table.
If PCA or low-rank updates match the candidate, report that simpler explanation
and the information needed for it. If even oracle POD reconstructs poorly,
only that rank and linear snapshot family have been excluded.

## C-N3. Which ingredient actually helps?

**Question.** If a performance gap survives, does it come from approximation
space, forward/adjoint information, initialized correlations, symmetry, or
conditioning/filtering?

Use a small conditional ablation set, applied to both the candidate and the
strongest generic competitor where meaningful:

1. Orthogonal rotations within the same feature span, transporting coefficients
   and initialized blocks: represented dynamics should agree to numerical error.
   For general invertible reparameterization also transport mobility and the
   represented initial operator. Native re-whitening with identity mobility can
   change the ridge filter and is a separately labelled intervention.
2. Forward-only versus forward-plus-adjoint information at matched dimension;
   add adjoint enrichment to a generic basis as a positive control. A gap that
   disappears supports the simpler response-information explanation.
3. Full hierarchy versus polynomial core, useful-parity/symmetry pruning, and a
   small greedy or POD selection from the same permitted feature pool. Charge
   selection and show whether pruning makes the construction simpler/cheaper.
4. Permute complete dictionary rows relative to initialized neuron labels while
   preserving the dictionary Gram and row distribution. Recompute initialization
   under the same rule and measure its mismatch. Later degradation alone does
   not isolate a new dynamical effect if worse initialization already explains it.

Keep two additional comparisons distinct. The native-method panel preserves
the candidate's exact raw features and ridge schedule, with equally budgeted
calibration of permitted competitor hyperparameters. Equal raw rank and equal
numerical ridge values do not match their contraction spectra. A separate
common-filter panel orthonormalizes each numerically resolved span in the same
population inner product and uses Q_l=alpha_l Pi_l, where Pi_l is its orthogonal
projector and the default shared alpha_l is one. Use the same coefficient
metric across this panel, a calibration-frozen numerical rank threshold, and
disclose every removed dependent/near-dependent direction and actual rank.
Charge all preprocessing. This panel changes the native candidate's filter
and generally its represented initialization/dynamics; it is a labelled
span/filter ablation, not a coordinate-equivalent run of the original method.
The same-span invariance check above instead preserves the original operator,
filter and metric. Only the matched panel supports a span-specific attribution.

Random dictionary columns drawn once and frozen are legitimate competitors,
with their own consistent joint law and coefficient initialization. Consistently
changing a joint law is also a valid changed-construction ablation. Deliberately
incorrect negative controls include redrawing nominally frozen variables during
rollout, using inconsistent copies of a required shared mark in different
equations, or breaking actual transpose reuse. Their failure cannot prove special
efficiency. Frozen-hidden and exact-initial-tangent controls separately test
whether the selected regime can reveal feature learning at all.

If source/closure defects are small but rollouts diverge, inspect accumulated
error and sensitivity before inventing more features. If projection is good
but the vector-field defect is large, basis refinement alone may be ineffective.
Same-span agreement is an implementation prerequisite, not a scientific win.

**Deliverable.** A causal attribution table, including simpler replacements
that preserve performance and explicit surviving alternative explanations.

## C-N4. Is any advantage useful after all costs and transfer?

**Question.** Does a surviving advantage persist in end-to-end resources and
new instances, or was it due to uncounted preparation, an easy output task,
or a favorable choice of width, depth or integration resolution?

Compare complete error-versus-memory and error-versus-time Pareto curves,
including initialization and any dense snapshot costs. Add a narrower fully
trained dense network as a practical utility comparator and retain the full
dense network as reference. A small network changes the approximation class;
its useful performance is still relevant to whether the closure is economical.

Include ordinary input-space Fourier/RFF, random-feature regression and the
initial tangent or frozen-hidden predictor in a separate output-utility table.
They may make the dictionary unnecessary for a particular prediction task,
but matching outputs does not establish hidden-dynamics fidelity. Use the same
training labels and honest tuning budgets; no fitted time warping against the
evaluation trajectory.

Transfer checks vary one axis at a time: new initialization seeds, rotated or
correlated inputs, target/label family, physical horizon, depth, width, and
population quadrature P_l. Rebuild a method only using its declared access.
Use own-state restarts during an autonomous rollout. Dense checkpoint resets
are forbidden in an initialization-only rollout. A P_tau method may initialize
once from its declared, charged end-of-burn-in checkpoint, then continue without
further dense resets. Additional dense checkpoints are used only for separately
labelled projection/defect diagnostics, not for its autonomous trajectory.

If nonlinear population evaluation dominates, compare common fixed bases with
full quadrature versus coreset/DEIM-style sampled evaluation. Count the extra
nonlinear basis and solve conditioning. Dense-coupling dependencies may still
require full-size work; sampled activation entries alone do not prove cheap
evaluation. Change evolution to LSPG or operator inference only as a separately
labelled model, after representation and evaluation costs have been isolated.

**Deliverable.** A measured resource recommendation, with the smallest method
that meets the declared accuracy and observable requirements on held-out cases.
Report width dependence separately from dictionary rank dependence; finite-width
agreement alone is not identification of an infinite-width target.

## Proposed bounded first execution, to be instantiated before running

This task designs packages. The following is a concrete proposed envelope for
a later run, not an executed preregistration or a claim of available throughput.

The complete screen and confirmation run at exactly one primary depth: L=3
once its explicit adapter is checked. L=2 is an implementation anchor, limited
to at most two dense and four reduced trajectories within the pilot allocations
below, plus logged algebraic checks. There is no full two-depth grid in these
caps. If only the maintained L=2 adapter is ready, select L=2 as the primary
depth before screening and defer L=3; do not choose depth based on which method
wins. Deeper transfer needs a separate allocation. Use d=2, a predeclared finite circle
training set (initial proposal: 16 nonorthogonal directions), held-out circle
inputs, and two fixed odd smooth label functions, such as cos(3 theta) and
(sin(3 theta)+0.4 cos(5 theta))/1.4. Odd targets respect the bias-free network's
input-sign symmetry. A rotation/clustered-input panel is reserved for transfer.
Dense pilot widths 512 and 1024 are proposed starting resolutions, not assumed
population accuracy. Use three candidate dictionary budgets fixed by its actual
feature lists; all competitors match those layerwise sizes or an explicit
equal-resource envelope, never arbitrary common order labels.

Pilot horizon candidates are {1/200, 1/20, 1/4, 1, 4}. Choose one per benchmark
using dense-reference signal and numerical resolution only, before comparing
methods. The short-theorem arm stays at its justified interval. Other horizons
or depths are empirical finite-network comparisons. Do not lengthen a horizon
because a preferred method has not separated.

For a short-time comparison, require the prediction change and each claimed
hidden-motion signal to exceed five times its numerical uncertainty, and use
change-relative errors. A stronger feature-learning arm additionally requires
at least 20% loss reduction, a full-versus-initial-tangent prediction separation
of at least 5% of the dense prediction change, and a resolved internal Gram
change (proposed threshold 10%, reporting magnitude and normalized shape).
These stronger gates are not prerequisites for the local convergence theorem.
If they fail, the result remains an onset comparison and cannot establish
efficiency in a substantial feature-learning regime.

Proposed seed groups: calibration 11001–11002, screening 21001–21002,
confirmation 31001–31006, donor/conditional follow-up 41001–41002. Derive
independent dictionary draws from a fixed (seed,method,draw) key; do not select
the best draw on evaluated trajectories. Freeze dataset and evaluation seeds
separately. Snapshot-donor and evaluated future windows do not overlap.

| Stage | Dense-trajectory cap | Reduced-trajectory cap | Purpose |
|---|---:|---:|---|
| Numerical/signal pilot | 8 | 12 | Solver, state conventions, usable signals; no method winner |
| Broad first screen | 4 | 72 | Six methods, three budgets, two seeds, two tasks |
| Fresh confirmation | 12 | 96 | Candidate versus selected strongest generic method; reserved refinements/draws |
| Conditional PCA/ablation | 6 | 60 | One named unresolved explanation or validity repair |
| Total | 30 | 240 | No automatic Cartesian expansion |

Reserve verification runs within those caps; if additional numerical resolution
is required, reduce scientific breadth rather than silently increasing the
budget. Proposed hardware envelope: one worker, one BLAS thread, 8 GiB peak RAM,
8 cumulative CPU-hours and 24 elapsed hours, stopping at the first limit. A
timing pilot must establish feasibility; failure is a resource outcome, not
evidence against either dictionary. No GPU or external compute is presumed.

Before execution, freeze exact source hashes, permitted baseline adapters,
model/task arrays, ranks, solver tolerances, snapshot times, Gram handling,
input quadrature, precision, commands and hardware in a run manifest. Use a
fresh generated-data directory. The current contract supplies no performance
result until that implementation and execution exist.

## Decision rules and numerical validity

Suggested target: E_f<=0.05 with the declared hidden-motion errors also <=0.1
on resolved signals. These are practical thresholds, not mathematical constants.
Report the entire predeclared error/cost grid, nonattainment and failures;
do not publish only the cheapest successful point. A measured minimum cost
on that grid is an empirical frontier, not an automatic accuracy certificate.

Independently refine dense solver time accuracy, closure time accuracy,
population quadrature, input evaluation and conditioning/precision on selected
hard cases. A rank trend does not validate those axes. Uncertainty in each
primary observable should be below one fifth of the target tolerance and below
one fifth of the claimed inter-method difference. For empirical ties, compare
uncertainty against the equivalence band instead of a zero difference. Width
checks concern distributions/ensembles; arbitrary pairing of different widths
does not justify trajectory convergence. Fixed-width results remain valid
fixed-width results even if a population interpretation is unresolved.

Use paired confidence intervals over held-out initialization/task blocks;
dictionary draws are nested repeats, not independent network seeds. With small
samples intervals can remain wide: absence of a significant difference is not
equivalence. Proposed practical outcomes, applied separately by information tier:

- **Candidate advantage:** on both held-out tasks, target accuracy is reached
  on at least five of six confirmation seeds, median end-to-end cost is at most
  half the strongest confirmed generic method's cost, and paired uncertainty
  supports a ratio below one. Report online-only and memory outcomes separately.
- **Generic equivalence:** both methods meet accuracy and the paired cost-ratio
  interval lies inside [0.8,1.25], with hidden-dynamics agreement also resolved.
  This supports a simple replacement in the tested regime.
- **Generic advantage:** the reverse comparison satisfies the same substantive
  criteria. Keep that outcome; the package is not designed to protect the candidate.
- **Unresolved:** intermediate ratios, failed signal/resolution gates, inconsistent
  tasks, censored nonattainment that prevents comparison, or wide intervals.

If only one method reaches the target on the fixed budget grid, retain that
bounded-grid success/failure contrast symmetrically for either method. Do not
erase it merely because the other method's unobserved cost prevents a numerical
factor-of-two estimate; also do not extrapolate a cost ratio beyond the grid.

A future-snapshot PCA win is a compression diagnostic. A past-snapshot PCA win
is a training-assisted method win after acquisition costs. Neither establishes
an initialization-only equivalence. Good projection with bad autonomous rollout
means a representation result without a successful dynamical closure.

The first highest-value action after implementation is the six-method C-N1
screen plus the same-span invariance check. Select one next explanatory test
from its predefined outcomes. C-N1–C-N4 are completed by reproducible answers,
including negative or equivalent outcomes, not by necessarily proving that
the existing dictionary wins.
