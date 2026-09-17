# Joint assessment of novelty, significance and decisive next milestones

Assessment date: 2026-09-16. Prepared by the independently initialized advocate
and critic, after freezing their strongest openings and debating directly.
Final endorsement is recorded against this document's exact SHA256 in
NOVELTY_ADVOCATE.md and NOVELTY_CRITIC.md. Those records preserve the initial
disagreement and the reasons for its resolution.

## Agreed present judgment

**This is a substantive, significant specialist mathematical contribution and a
significant numerical simulation proof of concept. It is not currently an
established breakthrough, a validated superior learning method, or a broadly
significant advance in practical machine learning.** The strongest contribution
is a particular constructive route from initialized Gaussian deep-network
training to autonomous population approximations, with scoped convergence to
the unchanged training target. The numerical evidence gives that route concrete
promise, including genuinely nonlinear behavior and useful measured savings.

Neither the finite architecture nor its optimizer is a new mathematical species:
it is a structured neural network trained by backpropagation. Classical low-rank,
Galerkin, population and gradient ideas are essential ingredients. What needs
assessment is the combined initialized-law construction, preservation of both
action directions, identification of the target and convergence guarantee.
Calling the implementation a low-rank network does not settle those questions;
calling it a closure does not establish architectural or algorithmic priority.

We jointly use the following scope-sensitive rubric. These are our assessment
commitments, not predictions of community reception, publication or prizes.

| Level | Meaning in the explicitly named field |
|---|---|
| Proof of concept | A sound construction or credible bounded demonstration; general advantage remains open. |
| Significant | A substantive specialist result or informative validated demonstration. |
| Highly significant | An important advance over a specified scientific bottleneck on a meaningful class. |
| Breakthrough | A decisive new ability on a named class that resolves a major obstacle, supported by proof or discriminating evidence. |
| Groundbreaking | A breakthrough whose method demonstrably enables several materially different problem classes. |
| Landmark | Sustained, independently established influence or broad enabling consequences; a single internal campaign cannot establish this. |

| Object and field | One jointly endorsed current grade | Why it stops there |
|---|---|---|
| Canonical mathematics, within rigorous theory of deep-network feature learning | **Significant, substantive specialist contribution** | Qualitative constructive convergence is valuable, but useful quantitative error control and a nondegenerate long-time theorem are missing. |
| Numerical method, as a simulator of the specified nonlinear network dynamics | **Significant proof of concept** | Real fidelity and cost evidence exists; a matched-fidelity advantage over cheaper structured and dense alternatives is unestablished. |
| Wider practical ML, as a learning algorithm or account of generalization | **Promising proof of concept, below an established significant methodological advance** | Current tasks, targets, baselines and controls do not show broad competitive learning or a predictive generalization mechanism. |

The advocate initially defended a higher mathematical grade even in a narrow
specialist field. The critic identified the missing concrete consequence:
qualitative approximation on short time or an extraordinarily small long-time
family does not yet overcome the practical or robust dynamical approximation
bottleneck. The advocate accepted that criterion. This table is a common
judgment, not an average or a concealed pair of opposed grades. Broad ML success
is not required to earn a mathematical upgrade; the independent theorem branch
below specifies what would earn it.

## What the finite and continuum models actually are

With fixed feature tables B1,B2, quadrature weights p1,p2, moving first-layer
rows W, moving readout c and moving full coefficient matrix M, the finite map is

    h1(u) = tanh(W u)
    h2(u) = tanh(B2 M B1^T diag(p1) h1(u))
    f(u)  = c^T diag(p2) h2(u).

The middle array therefore has rank at most min(K1,K2,P1,P2). The same M
transpose carries the backward signal. W and c themselves move; they are not
restricted to fixed expansions in B1 and B2. The population-weighted gradient
metric on W,c and the Frobenius metric on M give the maintained equations.
Changing those weights or training arbitrary low-rank factors generally changes
the dynamical target. Backpropagation remains present in full.

At the population level the state includes complete joint laws of initialized
marks, dictionary coordinates and moving particle coordinates. A law is not a
finite list of scalars. A fixed closure order makes the coordinate domain finite;
finite population quadrature then gives an actual finite ODE and finite storage.
Its state can restart the run without a growing training transcript. All fixed
feature tables, compiler products retained during integration, quadrature nodes,
readout coordinates and the full M must count in resource claims.

Initialization is scientifically essential. The dictionaries come from a joint
Gaussian construction and bounded initialized action words using both A0 and
A0*. A ridge-normalized feature map gives a positive contraction Q=UU*, generally
not an exact orthogonal projector. D=U2* A0 U1 is initialized from that law; the
learned M is unrestricted within its coefficient shape. The target operator is
approximated through B_N=Q2 A0 Q1 and a Hilbert–Schmidt learned increment. The
proof uses strong approximation in both directions on the needed compact sets,
not operator-norm approximation of the whole Gaussian operator.

The general-d first-order initializer contains a Gaussian-response term as well
as the forward covariance term. Write h=tanh(G), v=E h^2,
H=tanh(sqrt(v) Ztilde), tau=E H^2, alpha=1-tau and
R=sqrt(tau) Z+alpha h, for independent standard Gaussian coordinates.
The lower population samples (G,R) jointly. The upper Gaussian-mark population
is independent of it, without paired lower/upper node indices; the reused A0
enters through D's contraction and response term. Omitting that response changes
the initializer. The first-order folded middle block
has d by 2d moving coefficients; it does not remain diagonal during training.
A generic bottleneck with independent marks is therefore a useful comparator,
not automatically the same initialized dynamical model.

Closure order counts dictionary/action resolution, not input Fourier degree or
network depth. Already order one can have high odd input harmonics. The odd,
no-bias architecture excludes even target functions regardless of increasing
order. The polynomial core alone is not the proved exhaustive dictionary:
initialized action words are part of the convergence construction. A finite
coordinate-anchored dictionary need not be rotation invariant.

The implemented first-order moving-state scaling is O(Pd+d^2), compared with
O(nd+n^2) for a dense width-n network, plus fixed tables, caches and initialization
cost. This is useful when d is suitably smaller than n. It is not a uniform
saving when d grows like n. Direct total-degree extensions have core sizes
binomial(2d+p,p) and binomial(d+p,p), before additional action words. Fixed storage
along one trajectory does not imply order or quadrature independent of desired
accuracy, horizon or dimension.

## What is established and what remains open

The relevant canonical statements are in docs/global_nonlinear.md,
C.4.7.9–C.4.7.10; the maintained guides describe their scope. They establish an
autonomous initialized-population hierarchy and convergence of the declared
finite observation tuples, including current/frozen observations and both action
directions, for the stated target domains. The omitted-source control is derived
from the exact target's compact reachable sets and Hilbert–Schmidt increments;
it is not an assumption that the approximate model already has small omitted
tails. This is a meaningful constructive result.

The short-time circle population result is through T=1/200. Its fully numerical
statement represents a particular rational two-arc law family on S1, with mixing
weight in [1/3,2/3] and arc parameters in [-1/20,1/20]. The distinct time40 theorem
uses a law neighborhood with radius rho=2^(-E10), where E0=8192 and
E(j+1)=2^(Ej). That is a positive exact mathematical neighborhood, but its
perturbations collapse at the declared practical numerical precisions. This
cannot be described as a theorem for numerically separated time40 inputs. The
risk and early-motion statements have their exact times and domains; early
motion is not evidence of persistent late-time feature evolution.

The fully numerical guarantee is iterated across arithmetic precision, time
mesh, data integration, population and initializer quadrature, source
regularization, and outer order. An arbitrary joint refinement is not proved.
There is no general practical tolerance selector, order-to-error cost bound,
all-time theorem, or theorem identifying the MNIST d784/d240, order-one T600
runs with this circle target. General-d initialization algebra is a different
claim from general-d trained-dynamics convergence.

The canonical guide also records narrowly scoped frozen-feature comparisons
and generalization consequences. Those established results are not erased here;
they do not by themselves identify the present empirical benchmark family or
justify broad learning-efficiency or generalization claims for this simulator.

This assessment reads and compares established repository statements; it is not
a fresh complete proof recertification of their long foundations. Internally
checked empirical results below are not new independently replicated theorems,
and nothing is promoted by this assessment.

## What the existing experiments support

The current benchmark is MNIST 3 versus 5 with two hidden tanh layers, no biases,
canonical stored variances (1,1/n,1/n^2), mobilities (n,1,n), and unhalved MSE.
There are 10,552 training, 1,000 validation and 1,902 test examples. The large
comparisons use n=P=4096, three seeds, T600 and the maintained Heun integration.
Closure nodes are antithetic: P counts nominal nodes, with P/2 independent base
marks. Equal seed integers do not couple a finite network and the closure.

PCA is trained only on the training data, centered, unwhitened and not followed
by per-example renormalization. Its 240 coordinates retain 98.00167% of centered
variance but only 53.05% of original uncentered energy; centering removes a mean
component containing 45.87%. It changes mean, scale, coordinates and dimension,
hence changes the network target as well as computational cost.

At the common attainable training MSE 0.011080311898, using nearest stored
checkpoints with mismatch at most 1.85%, the three-seed mean prediction RMS is:

| Comparison | Mean RMS difference |
|---|---:|
| Original-input closure / original-input network | 0.0431777 |
| PCA closure / PCA network | 0.0416288 |
| PCA closure / original-input network | 0.1053142 |
| PCA network / original-input network | 0.0975023 |

The within-target relative RMS is 4.35–4.54% original and 4.09–4.62% PCA. Positive
within-digit correlations at T600 remain about .977–.984 in the PCA comparison;
this is useful evidence beyond simple agreement on two separated label clouds.
At equal T600 the respective mean RMS values are .05288, .04060, .10474 and
.09842. Original-network seed spread is about .0192, below the closure/network
difference: the present error is not all explained by that observed seed spread.

Crossed same-device T100 integration benchmarks show PCA closure 3.75–3.96 times
faster than the PCA network, with 130.52 versus 659.07 MiB peak live allocated
GPU memory, a reduction of 80.20%. The original closure is 1.64–1.89 times
faster, with 278.42 versus 756.96 MiB. These are fixed-time integration
measurements, not end-to-end times to matched loss or matched prediction
fidelity. Full-run scheduling times are not interchangeable with these controls.
Smaller dense networks, general fixed bottlenecks and trainable low-rank
comparators are absent. Jointly doubling n and P from 2048 to 4096 improves the
original comparison but does not isolate width, quadrature or truncation error.

Full-horizon half-step checks, independent saved-checkpoint replays and 5,607
analysis/export checks pass. They constrain integration and bookkeeping errors;
they do not establish every convergence axis. Full-horizon float64, independent
external replication and a general-d higher-order campaign remain absent.

The expressly authorized earlier circle evidence adds substance and boundaries:

- Wide-network and wider-arc comparisons show moving hidden geometry and useful
  closure agreement; longer horizons and some Gram tests leave population
  quadrature unresolved. These are finite-time results, not endpoint theorems.
- The non-antipodal XOR and alternating-quadrant examples distinguish nonlinear
  trained-network extrapolation from matched-training-fit NTK extrapolation.
  There is no teacher off the training points, so that distinction is not an
  out-of-sample-risk victory. Some dramatic matched-fit NTK comparisons require
  exceptionally long kernel physical times; they are shape comparisons.
- In the quadrant case order-five output RMSE is about .04569, while its second
  hidden-Gram relative error is about .649, versus .679 for the frozen network.
  Close predictions do not establish faithful internal representations.
- The endpoint-discrimination campaign selected a hard-label configuration after
  a declared screen. At T1000 order five has much smaller off-training gap error
  than orders one and three, but none of the plateau gates passes; network step
  and order-five quadrature gates also miss their thresholds. No settled-endpoint
  conclusion is earned, and first-layer Gram improvement is not monotone.
- The spectral study includes actual finite-width networks after its early
  surrogate-only work. Its controlled two-point experiment differs substantially
  from its own frozen kernel, with movement in both hidden layers; this rejects
  a frozen-only explanation for that example. The fitted tanh–sine shape is
  descriptive, not a derived endpoint-selection law.
- Across six multi-point network cases, order three improves over order one in
  the recorded output errors for all six, while order five improves three and
  worsens three. Only quad30 has the full available controls supporting both
  order transitions. This is useful resolved positive evidence and adverse
  evidence against unqualified finite-order monotonicity.
- The spectral rotation diagnostics also show that finite-order coordinate
  choices matter. The feature-geometry study contains only a startup plan and
  contributes no completed scientific result.

These outcomes support nonlinear simulation promise. They neither disappear
because some controls fail nor become general superiority because some succeed.

## Prior art and the smallest surviving novelty claim

The literature check is targeted, current through the search date, and based on
primary sources. Failure to find an exact match is not proof of priority. The
following matches are positive findings, not merely lists of possibly related
names.

| Primary antecedent | What already matches | What was not identified as the same result in the inspected passages |
|---|---|---|
| [Denil et al., Predicting Parameters in Deep Learning (2013)](https://proceedings.neurips.cc/paper/2013/file/7fec306d1e665bc9c748b5d2b99a6e97-Paper.pdf), §§2–3 | Fixed basis/dictionary with trained coefficients; low-rank matrix factorization, ridge-derived factors, fixed pooling interpretation. | Joint Gaussian action law and a hierarchy converging to the present unchanged dense gradient flow. |
| [Li et al., Intrinsic Dimension (2018)](https://arxiv.org/pdf/1804.08838), §2.1 | Training in a fixed parameter subspace. | The same initialized population law, metric and approximation theorem. |
| [LoRA-XS](https://arxiv.org/pdf/2405.17604), §§3.1–3.3; [LoRA-SB](https://arxiv.org/pdf/2411.19557), §2, Theorem 3 | Two frozen factors surrounding a trained core; projection in Frobenius geometry; explicit correction for factor Gram matrices. | These passages concern additive adaptation of pretrained weights, not the present whole-middle Gaussian population approximation. The factor/core architecture and metric awareness themselves cannot carry a priority claim. |
| [Yang–Hu, Tensor Programs IV (2021)](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf), model/dichotomy sections and [supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), Appendix G | Rigorous nonlinear feature-learning width limits, reused Gaussian matrices and transposes, computational prescriptions for fixed programs. | A fixed-program discrete-training theorem alone does not give this autonomous continuous-time hierarchy and its fully numerical convergence. The usual displayed readout initialization is not identical to the present small-readout target. |
| [Bordelon–Pehlevan, Self-Consistent Dynamical Field Theory (2022/2023)](https://arxiv.org/html/2205.09653v3), §§2–4, Algorithm 1, Table 1 | Deep Gaussian feature learning, response terms, evolving kernels and numerical computation. The displayed solver stores data/time indexed kernels. | The present frozen initialized dictionary/current-state construction and its stated theorem. Its published full-grid costs do not lower-bound all possible DMFT solvers. |
| [Yang–Santacroce–Hu, pi-limit (2022)](https://openreview.net/pdf?id=tUMr0Iox8XW), §§2–3 | Efficient nonlinear infinite-width networks and empirical applications; projected training with expanding gradient features. | This modifies the training rule; no same fixed-state approximation theorem for the present unchanged flow was identified. Direct PDF access met a browser challenge; search-rendered primary sections and the [author publication page](https://www.microsoft.com/en-us/research/publication/efficient-computation-of-deep-nonlinear-infinite-width-neural-networks-that-learn-features/) were inspected. |
| [Nguyen–Pham, multilayer mean field](https://arxiv.org/pdf/2001.11443), embedding/initialization statements; [Chizat–Bach, population gradient flows](https://arxiv.org/pdf/1805.09545v2), Theorem 2.6 | Rigorous population/particle gradient-flow limits and multilayer feature-learning theory. | Their hypotheses, normalization and initialization must be compared; these sources do not by their inspected statements identify the present Gaussian 1/sqrt(n) middle-operator construction. |
| [Huang–Yau, Neural Tangent Hierarchy](https://arxiv.org/pdf/1909.08156), Theorems 2.3/2.6 | A controlled hierarchy beyond the leading kernel approximation. | Its derivative-kernel/width expansion is a different approximation axis from this initialized-observable population hierarchy. |
| [Koch–Lubich, Dynamical Low-Rank Approximation (2007)](https://epubs.siam.org/doi/10.1137/050639703) | Low-rank dynamical approximation and projection are established numerical ideas. | Its moving rank-manifold/tangent-space construction differs from the present fixed feature spaces. Coverage here was bibliographic/abstract-level, not a complete theorem comparison. |
| [Celentano–Cheng–Montanari, high-dimensional first-order dynamics](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf) | Rigorous dynamical mean-field limits exist. | Its high-dimensional random-data limit is not an identified match to this fixed-input-dimension width limit; one should not call all previous DMFT merely formal. |
| [Lauditi–Bordelon–Pehlevan, Adaptive Kernel Predictors (2025)](https://arxiv.org/html/2502.07998v2), §§2–3, Figure1 | Computable nonlazy adaptive kernels and benchmark comparisons. | The inspected construction uses homogeneous activations and Bayesian/noisy or weight-decayed fixed points. Figure1 explicitly distinguishes unregularized flow from its final adaptive-kernel predictor; it is not the present unregularized tanh trajectory theorem. |
| [Lang et al., DYNAMITE (2026)](https://arxiv.org/html/2604.06309v1), §§3.1/3.6, §4.1 | Efficient DMFT integration with interpolation and controlled thinning of stored history; sublinear memory on the tested spin-glass models. | It appends and compresses history rather than supplying this fixed-current-state Gaussian feedforward approximation. No same-target feedforward comparison was identified. Universal quadratic-memory claims about DMFT are therefore rejected. |

The smallest defensible novelty candidate is the **combined Gaussian-aware,
two-orientation initialized population hierarchy, autonomous at fixed resolution,
with identification and scoped convergence to the unchanged dense Gaussian
training flow and its declared observations**. Neither first-order algebra,
nonlinear infinite-width learning, fixed dictionaries, a trained inner matrix,
backpropagation, nor metric-aware low-rank updates is separately new on this
record. The candidate remains substantive even though its priority is unverified.
A future exact prior match would narrow attribution; it would not erase a valid
independent construction or its measured evidence.

## Milestones and exact commitments

These are proposed future research packages, **not work executed or authorized
for execution by this assessment**. They define sufficient conditions for our
specified upgrades, not necessary conditions for all possible valuable research.
Numbers are negotiated decision thresholds, not claims that the thresholds are
already attainable. Any replacement target or relaxed threshold requires a new
explicit assessment; it cannot silently count as passing this contract.

The dependency graph is small:

    common target/attribution and validity checks
       |-- N: matched-fidelity numerical frontier
       |-- T1: nondegenerate nonlinear time40 theorem --> T2: usable certificate
       `-- G: feature-selection/generalization theorem and withheld predictions

N, T1 and G can progress independently. T2 depends on T1. None requires practical
ML success to earn its explicitly theoretical grade. Passing N or G does not
automatically give a wider-ML highly-significant grade.
N most directly extends the existing computational work, but its competitive
pass is not predicted. T1 requires a substantial new proof; T2 additionally
requires useful quantitative control that the current qualitative construction
does not provide. G is the most speculative branch, with explicit barriers
discussed below. We make no claim that these packages are quick or assured.

The common check requires an explicit equation-level target/metric/initializer
match, a search for exact prior statements, separation of theorem and empirical
claims, reproducible artifacts and a fresh independent audit appropriate to the
claim. An exact algebraic clone is an equivalence control, not a competitor whose
identical performance can be counted as a novelty win. A same-target prior result
must receive attribution; demonstrated extension or independently useful result
must then be assessed honestly. All subsequent commitments assume the claimed
result is valid and the surviving contribution has the stated scope.

### N — A validated output-trajectory simulation advantage

**Target/domain.** The same tanh/no-bias Gaussian gradient-flow target and metric
as above. Prespecify the six existing spectral multi-point problems
(triple20/40/60, quad15/30/45) through T120, plus original and PCA MNIST3-versus-5
through T600: eight cases. Preserve each training law and train/validation/test
split. Treat original and PCA inputs as separate targets.

**Deliverable and comparators.** A reproducible end-to-end cost/fidelity frontier
for the initialized closure against smaller dense networks, random fixed
two-sided bottlenecks, generic initializer-informed two-sided bases, trainable
low-rank factors, and practical same-target DMFT formulations where available,
including compressed-history solvers where applicable. An unrelated spin-glass
solver is not automatically an eligible neural comparator. Frozen NTK is a
mechanistic comparator where it can meet tolerance, not the sole efficiency
baseline. Publish the finite equal tuning budget and tune only using training
and designated validation trajectories. Final heldout target trajectories remain
untouched during model/dictionary selection. Report failures to reach tolerance.

Use dense widths {256,512,1024,2048,4096,8192}, extending the reference by doubling
until its uncertainty is resolved. Generic balanced ranks are
{8,16,32,64,128,256,512,1024,2048}, supplemented by every closure's actual
two-sided dimensions where feasible. Allow 40 candidate configurations per method
family/case, frozen before final test-reference trajectories are opened. Disclose
the prescribed physical-time metric/rate rule; use comparable optimization
software and precision controls. Resolution/hyperparameter selection may use
the designated validation trajectories, but dictionaries/initializers may not
be fitted to the target trajectory, and post-hoc time warping is forbidden.
The claimed frontier is relative to this explicit tested pool, not all possible
algorithms.

**Norm and validity.** For heldout probe law nu, use

    E_f = sup_{0<=t<=T} ||f_candidate(t)-f_target(t)||_{L2(nu)}.

Errors are in units of the +/-1 labels, avoiding a vanishing initial-output
relative denominator. nu is uniform angular measure for the circle tests and
the fixed heldout example distribution for each MNIST representation. The
reference is a separately width-resolved dense-GF ensemble, not one n4096 run
or a checkpoint selected to match training loss. This is empirical resolution
to a declared wide-network reference, not by itself a proof of its general-d
infinite-width limit. Continuous-time comparison
requires a certified or independently resolved interpolation/sampling remainder.
Use at least ten independent seeds per randomized method/reference, or a
rigorous alternative with stronger uncertainty control, and simultaneous
one-sided 95% bounds for all declared primary gates.

At epsilon in {.05,.025,.01}, reference uncertainty must be at most .2 epsilon.
Separately assess candidate order truncation, population quadrature,
initializer/data integration, time discretization and arithmetic; individual
numerical contributions must be at most .1 epsilon and their aggregate at most
.4 epsilon. Include these uncertainties conservatively in the final epsilon
bound; they are not extra error allowed outside the tolerance. An empirical
order comparison does not itself bound all higher-order truncation; target
comparison and any claimed certificate must cover that gap. Hidden-Gram or
action-fidelity claims require their own norms and the same control discipline.

Count initialization plus integration, all retained tables/caches, peak memory
including initialization, and any repetitions required for the claimed predictor
fidelity. Publish both runtime and work; use synchronized comparable hardware.
Any target-specific reference computation needed by the deployed method to
select its dictionary, order or settings must also be charged. Evaluator-only
reference construction is excluded because it is not an algorithm input;
generic preregistered development/tuning costs are reported separately using
the same convention for every method.
Raw/centered/full-PCA/truncated-PCA and orthogonal-rotation diagnostics distinguish
preprocessing and coordinate effects. They are diagnostics, not an invariance
pass gate unless invariance is claimed.

**Pass.** Select one common pair of the three epsilon values before final test
trajectories are opened. On at least six of the same eight cases, including both
MNIST representations, the closure achieves at both selected epsilons at least a factor
of two reduction in end-to-end runtime and peak memory against the best eligible
competitor meeting the same tolerance. Conservative simultaneous bounds must
support these factors. On none of the eight cases may runtime be more than 25%
worse at matched fidelity at either selected epsilon. Report all three epsilon
values; success cannot use a different pair for different cases. There must be
a feasible resolved comparator, or no comparative win is
counted for that case. All validity gates pass.

**Fail/inconclusive.** Resolved errors or competitive costs outside these gates
fail this package. Unresolved reference, axis or uncertainty controls are
inconclusive, not evidence of superiority or inferiority. Failure withdraws the
specified frontier claim on this suite, while retaining the current proof of
concept and any independently valid mathematical result.

**Both commit upon passing:** *highly significant within numerical simulation of
nonlinear deep-network output trajectories on the specified low-dimensional
and image-input class*. This is an expanded numerical grade, not a promise of
better general-purpose ML training or faithful hidden representations.

### T1 — A nondegenerate long-time constructive theorem

**Target/domain.** Preserve exactly the two-hidden tanh architecture, Gaussian
initialization, no biases, unhalved squared risk and gradient-flow metric. Let
U(s)=((1-s^2)/(1+s^2),2s/(1+s^2)) and let R90 rotate by 90 degrees. A law puts
mass p in [1/3,2/3] on label +1 with s uniform on [a,b] and mass 1-p on label -1 with
s uniform on [c,d] followed by R90. Require

    a,c in[-.05,-.02],    b,d in[.02,.05].

Include every global rotation of this family. These are genuinely separated
positive-width arcs, not a radius that collapses at working precision.

**Deliverable.** A self-contained proof, uniform over that entire family through
T40, of target existence, identification from finite-width Gaussian GF, and
convergence of the autonomous hierarchy for the declared observations. Prove
risk at T40 at most 1/4. For hidden layer ell define

    Motion_ell(t)=||G_ell(t)-G_ell(0)||_{L2(mu_X x mu_X)}
                  / ||G_ell(0)||_{L2(mu_X x mu_X)}.

Here mu_X is the input marginal and G_ell is the actual target hidden-feature
Gram kernel. Prove for each layer Motion_ell(t)>=.01 at some time in [1,40],
with the time selection stated by the theorem and uniform validity over the
family. Both layers may attain the threshold at different times. Denominators
must be proved positive. This is a meaningful nonlinear-motion requirement;
an infinitesimal initial derivative does not pass it.

**Comparator/validity.** The comparator is the exact unchanged Gaussian target,
not the approximant's own flow or a changed projected training law. Explicitly
compare the result's scope with TP/DMFT/mean-field prior theorems. A fresh
independent full proof review must check initialization, both action directions,
limit order, uniformity, stability and the risk/motion consequences.

**Pass/fail/inconclusive.** All statements on the full parameter box pass.
A counterexample or necessary restriction excluding part of the box fails this
package as stated. An incomplete proof is inconclusive; a simulation does not
replace it. Failure does not retract the present smaller-domain theorem.

**Both commit upon passing:** *highly significant within constructive rigorous
theory of nonlinear deep Gaussian feature-learning dynamics*. This removes the
present nondegenerate-long-time obstacle; it does not yet supply useful cost.

### T2 — A usable rigorous error certificate

**Dependency and target.** T1, with the same entire family and T40 horizon.

**Deliverable/norm.** Give an algorithm, initialized without access to a future
target trajectory, which accepts epsilon in(0,.05] and certifies uniform-in-time
output L2(mu_X) error at most epsilon; both hidden-Gram L2(mu_X x mu_X) errors
normalized by their initial norms at most epsilon; and forward/backward action
errors at most epsilon in their corresponding population L2 norms, integrated
over mu_X. The action tests include A_t h1_t(u) and A_t* delta2_t(u), with delta2
exactly the backward variable of the maintained equations; their reconstruction
and coupling to the target must be explicitly defined. This tests the actual
adjoint, not a separately fitted backward map.
Law parameters must be supplied as certified binary intervals. Bound the input
precision needed and prove the certificate uniformly for every compatible
parameter value; an exact-real input oracle cannot hide unlimited computation.

Bound the total error from truncation, law approximation, initializer and input
integration, time discretization and arithmetic. If comparison to finite width
is claimed, include its error/probability separately and in the total advertised
budget. No target-dependent unknown source envelope may serve as a computable
certificate without a valid computable upper bound. Give explicit polynomial
exponents and constants for work/storage in epsilon^(-1), at this fixed domain,
including the required bit precision. At epsilon=.01, the worst-case cost for
any requested law in the family must be at most 10^12 fixed-word (64-bit)
arithmetic-equivalent operations and 2^30 stored 64-bit words. Count certified
elementary-function evaluation, multiword arithmetic, initialization, compiler
products, particles, caches, certification and trajectory interpolation.
Charge any universal precomputation once to each primary comparison; no
amortization is allowed for this gate. The theorem must guarantee this budget
uniformly for every requested family member; one finite run need not output
the continuum of all possible trajectories. Unit-cost real arithmetic cannot
conceal unbounded-precision work.

**Comparator/validity.** Mathematical error is against the identified dense
Gaussian GF limit. A validated implementation checks the certificate on a
prespecified covering of the parameter family and audits every numerical axis;
the family-wide guarantee comes from proof, not the finite covering alone.
Fresh independent proof and implementation audits are required. Report a
same-target direct/DMFT reference comparison where executable; it cannot replace
the theorem or be used to tune unreported error constants.

**Pass/fail/inconclusive.** All accuracy, uniformity, explicit-cost and validity
gates pass. A valid bound exceeding the specified budget fails the usable-cost
part; merely asymptotic convergence or uncomputable constants is inconclusive
for this package. A failed certificate changes the algorithmic claim, not an
otherwise valid T1 theorem.

**Both commit upon passing:** *breakthrough within rigorous error-controlled
simulation of nonlinear deep Gaussian gradient flow; highly significant within
deep-learning theory more broadly*. This is an explicitly narrow breakthrough
commitment, not a dimension-free or wider-ML claim.

### G — A predictive feature-selection and generalization theory

**Feasibility assessment.** G is a high-risk, barrier-facing target, not a
near-term extension of the closure theorem.
[Damian–Lee–Bruna, The Generative Leap](https://arxiv.org/html/2506.05500),
Theorem 1 and Proposition 4, gives a d^(3/2)-scale low-degree computational barrier
for related Gaussian three-parity, making the requested O(d polylog d) sample
scale particularly ambitious.
[Barzilai–Shamir, Limitations of SGD](https://arxiv.org/html/2602.05704v2),
§2 and Theorem 6, supplies further algorithm-specific obstacles under different
assumptions. Neither is automatically an impossibility proof for this spherical,
reused-sample, squared-loss full-batch GF. A successful proof must explicitly
reconcile applicable barriers; no feasible polynomial schedule is established
here. Failure is a live possibility and would redirect this branch, without
retracting independent N/T1/T2 results.

**Target/domain.** For all d>=d0, the normalized input u is uniform on S^(d-1) and

    y=sign[(v1 dot u)(v2 dot u)(v3 dot u)],

where (v1,v2,v3) is any unknown orthonormal triple. Use
m=ceil(C d(log d)^k) independent training examples, with explicit constants
0<C<=100, 0<=k<=2 and 3<=d0<=256 supplied by the theorem. Preserve the same
two-hidden tanh Gaussian model, no biases, unhalved squared loss and gradient-flow
metric; do not assume learned feature alignment as an initial condition. State
the model using physical input x=sqrt(d) u: the canonical first preactivation
W x/sqrt(d) is therefore W u, with variance one at initialization. All input
gradients and sphere observables below use normalized coordinates u with marginal
law mu_U. The horizon and any necessary width,
closure-order and population schedules must be explicit polynomials in d and
required inverse error. Any theorem for a limit must prove that limit's relevant
identification, not infer it from the existing circle theorem.

**Theoretical deliverable and comparator.** Derive feature selection and a
population classification risk at most .1 at the stated polynomial horizon.
Prove population classification risk at least .2 for the corresponding
initialized-NTK ridge-regression and gradient-flow early-stopping predictors at
the same sample budget and dimensional regime. The lower bound must allow
training-selected regularization and stopping, not a deliberately poor fixed
choice. Both risk inequalities must hold on a common event of probability at
least .9 over the training sample and relevant initialization, uniformly in the
unknown orthonormal triple. All probability components, sample splits and finite-width/limit
interpretations must be explicit. This is a new same-target comparison, not a
claim that general neural-versus-kernel separations are themselves new.

**Mechanism predictions and empirical deliverable.** From initialized dynamics
and training data, predict the learned subspace and both hidden Gram kernels
without fitting parameters to the terminal reference network. Define

    S_f = E_u[grad_u f(u) grad_u f(u)^T]

using the ambient normalized-input gradient of the network's natural extension off the
sphere; the tested subspace is its leading three-dimensional eigenspace.
Account for eigenvalue degeneracy explicitly: an undefined or unstable leading
subspace does not pass. Freeze predictions and resolution rules before testing
withheld dimensions {d0,2d0,4d0} and fresh Haar-distributed teacher triples.
Write V_ref for the target network's leading subspace, V_pred for its frozen
theoretical prediction, and V_teacher=span(v1,v2,v3). The sine of the largest
principal angle must be at most .2 both between V_ref and V_teacher and between
V_pred and V_ref.
Both predicted Gram kernels must have L2(mu_U x mu_U) error, normalized by the
corresponding initial Gram norm, at most .1. Test at least 100 independent
sample/teacher/initialization trials per dimension, resolving width, population,
initializer, step, arithmetic and probe integration uncertainty to at most 20%
of each error threshold in aggregate, included in that threshold. Require a
success rate at least .9, established by simultaneous one-sided 95% lower bounds
for the declared dimensional/observable gates. A valid stronger rigorous
uncertainty alternative is allowed; a favorable mean alone does not pass.

**Validity and pass/fail/inconclusive.** A fresh independent proof audit must
check the learning guarantee, the kernel lower bound, identification, scale,
probabilities and polynomial schedules. Independent code/analysis audit must
verify the withheld tests and absence of terminal-output fitting. All statements
and prediction gates must pass for the combined package. Numerical agreement
cannot replace the generalization proof. A failed kernel gap refutes the claimed
separation on this family; a failed prediction refutes the proposed mechanism
accuracy; unresolved limits or numerics are inconclusive. Neither failure erases
unrelated T1/T2/N successes.

**Both commit upon passing:** *breakthrough within rigorous theory of deep
feature learning and generalization, with independently checked predictive
mechanism content*. A complete valid novel theorem meeting the theoretical
subpackage already earns the theory breakthrough; the full wording including
checked predictions requires the empirical subpackage. This is a precise
upgrade commitment, not a claim that the current fitted circle template has
already explained feature selection or generalization.

No package here, alone or combined, automatically earns *highly significant in
wider practical ML*, *groundbreaking* or *landmark*. Those labels would require
a further explicitly specified body of broader consequences, relevant real-task
comparisons and, for landmark status, independent sustained impact. We do not
replace that missing evidence with a generic promise to reconsider. The firm
commitments actually offered are N, T1, T2 and G, whose scopes and gates are
fixed above.

## Evidence boundary and reading coverage

The evidence cutoff is the frozen repository inventory at
`data/generated/first_order_dimension_mnist/novelty_debate_20260916/input_inventory.json`.
The current study's README administrative assessment entry was added separately;
no scientific inputs were edited by this debate. We used canonical docs/code,
the assigned current MNIST/PCA reports and relevant producer equations. The
current reports include REPORT.md, PCA_REPORT.md, INITIALIZATION_THEORY.md,
MODEL_SCOPE_CHECK.md, COMPUTE_REPORT.md, FULL_4096_CHECK.md and PCA_RUN_CHECK.md.

The user's retrospective handover expressly allowed the scientific evidence of
exactly six earlier circle studies: wide_network_closure_comparison,
xor_network_closure, quadrant_network_closure, closure_endpoint_discrimination,
closure_feature_geometry and closure_circle_spectral_mechanism. Their own
READMEs and named scientific reports provide the provenance; their failures
and scope restrictions remain in this assessment. Earlier debates, agent verdicts
and arbitrary other studies were not requested or used as scientific evidence.
After both independent openings and the substantive common grades/milestone
commitments were settled, a critic's status-only agent-list call unexpectedly
returned completed prior-agent summaries. The critic disclosed this incidental
exposure and excluded it from the assessment; the advocate received no such
content. Root reported an analogous incidental status-output exposure earlier.
These process limitations are recorded rather than claiming perfect blindness.
Root coordinated permissions, provenance and source locators; the two debating
agents negotiated the judgment. This is a collaborative assessment with frozen
independent openings, not a blind promotion review.

Both agents read the complete assigned current reports and canonical guides,
C.4.7.9 and the relevant C.4.7.10 statements/definitions, and inspected the finite
forward/RHS and initialization formulas. The advocate read almost all of
C.4.7.10 in sequence; the critic concentrated on the complete relevant statement,
construction and theorem-domain sections. Neither performed a new complete audit
of every foundational proof or reran experiments. The existing internal tests
remain internal; reading saved reports is not independent numerical replication.

The literature table states the relevant accessed sections. Both agents directly
inspected primary TP/DMFT, population/mean-field scope, fixed-basis/LoRA methods,
and the 2025 adaptive-kernel/2026 compressed-history comparisons. The advocate
additionally inspected the TP Appendix G definitions, NTH statements and
Chizat–Bach's population theorem; the critic inspected Li et al.'s explicit
subspace formula. Long proof appendices and full experiment sections were not
uniformly read. Pi-limit full-PDF access was blocked by a browser challenge;
primary indexed sections and the author page were available. Dynamical-low-rank
coverage was more limited than the directly accessed neural-model equations.
For G's feasibility assessment both agents additionally read the Generative
Leap model, low-degree lower-bound statement and Gaussian-parity case, and the
SGD Limitations input/update setting and multi-index theorem hypotheses. Their
proof appendices were not audited, and no new reduction transferring a barrier
to the present model was attempted.

Queries covered initialized Gaussian feature learning, autonomous/finite-memory
closures, Galerkin and low-rank neural training, fixed bases, TP, DMFT, pi-limits,
and 2025–2026 follow-ups. An additional 2026 simple mean-field Bayesian model was
checked at abstract/setup level and did not establish an exact deterministic-GF
match. This was a focused comparison of likely matches, not an exhaustive
priority search. We retain **uncertainty about exact priority and the eventual
reach of the method as an agreed conclusion**, without treating uncertainty as
proof either of novelty or of redundancy.
