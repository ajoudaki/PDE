# Critic opening: independent evidence-based assessment

Opening frozen 2026-09-16 before reading the advocate's opening. This is a
read-only retrospective assessment, not a new proof audit, experiment, research
study or promotion. I read the investigate-conjectures skill and its four
required references. The assignment's six expressly authorized circle studies
are included; no older debate, agent verdict or unlisted study was consulted.

## Strongest skeptical position

The finite computation is a structured neural network trained by backpropagation.
Its middle matrix is replaced by a prescribed two-sided feature factorization,
and its population node coordinates move by ordinary weighted gradient flow.
This does not invalidate the work: an approximation theorem for a specifically
initialized compression can be valuable. It does put the novelty burden on the
construction and convergence guarantee, not on avoiding neural networks,
backpropagation, mean-field theory, low rank, or Galerkin approximation.

Write B1 and B2 for the fixed node-by-feature tables, p1,p2 for their weights,
W for the moving first rows, c for the moving readout and M for the moving
coefficient matrix. The actual finite forward map is

    h1 = tanh(W u)
    h2 = tanh(B2 M B1^T diag(p1) h1)
    f  = c^T diag(p2) h2.

Thus the effective middle array has rank at most min(K1,K2,P1,P2).
The same M transpose carries the backward signal. Moving W and c are not
restricted to fixed feature expansions. Population-weight inverse mobilities
on their gradients and a Frobenius gradient on M give the existing equations
H2.5/H3.N2, already derived in the book and checked by the engine autograd audit.
This finite representation differs from a dense iid Gaussian network and from
arbitrary low-rank factors because B1,B2,D have prescribed correlated Gaussian
observable provenance and remain frozen. It is not algebraically exotic.

The strongest surviving contribution is the specific initialized-word,
two-orientation, fixed-current-state approximation hierarchy and its scoped
convergence to the *unchanged* dense Gaussian gradient-flow population target,
plus an implementation that can be run independently of a target trajectory.
I have not found an exact prior theorem matching that entire contract in the
sources inspected. This is a novelty candidate, not a certified priority claim.

## Objections and evidence

Each item begins open for direct negotiation; responses and dispositions will
be appended without replacing this independently frozen opening.

### C01 — Architecture and optimizer novelty are limited

Claim challenged: the p-closure is fundamentally outside neural-network
training, replaces backpropagation, or is not a low-rank representation.
Evidence: H2.4–H2.7; H3.N1–H3.N2; P1_ENGINE.py fields/RHS; weighted-gradient
audit in COMPUTE_REPORT.md. The explicit finite map above refutes those broad
claims. A restricted architecture is not thereby equivalent to every generic
bottleneck optimizer: the metric, initialization and fixed factor subspaces
matter. Li et al. (2018), section 2.1, equation (2), already train in frozen
parameter subspaces. Its random global subspace is not this exact construction.
Disposition sought: exact finite algebraic equivalence acknowledged, novelty
relocated to provenance, approximation target and theorem.

### C02 — Classical approximation ingredients do much of the work

Claim challenged: finite coefficient matrices, ridge-normalized bases,
particle integration, strong convergence of two-sided projections, or
autonomous finite ODEs are individually new principles.
Evidence: H2.0–H2.2, H2.10–H2.16, H3.2–H3.3. Q is a positive contraction,
not exactly an orthogonal projection when the ridge is positive. The proof
combines dense initialized-word spans, compact-set strong approximation,
Hilbert–Schmidt increment approximation and target-tail stability. These
are familiar approximation techniques applied to a difficult neural target.
Unlike standard dynamical low rank, the feature subspaces are frozen, not
adapted by tangent-space evolution on a rank manifold. The nontrivial neural
obligations are joint Gaussian reuse, actual adjoint, target identification
and propagation without assuming an omitted tail is small. They deserve
credit; labels alone neither prove novelty nor refute it.

### C03 — Infinite-width nonlinear feature learning has major antecedents

Claim challenged: this is the first framework to retain nonlinear feature
learning, reused forward/backward dependence, or compute an infinite-width
deep model beyond NTK.
Evidence: Yang–Hu Tensor Programs IV, sections 2–5 and discrete-time
dichotomy; Bordelon–Pehlevan, sections 2–4, equations (2)–(7), Algorithm 1
and Table 1; Yang–Santacroce–Hu pi-limit, sections 2–3. TP and DMFT are
direct prior context. The displayed muP initialization is not identical to
this book's exceptionally small stored readout, and fixed-program SGD
identification does not by itself give the current GF/closure theorem.
The DMFT procedure retains kernels indexed by pairs of data and time; its
published Table 1 has O(samples^2*time_points^2) kernel storage. Pi-limit
changes training by projection and appends gradients as training proceeds.
Those distinctions leave room for a fixed-state approximation to the original
flow. They do not make feature learning or computable infinite-width networks
new. Rigorous multilayer neuronal-embedding and high-dimensional DMFT results
also exist, under different target scalings/domains.

### C04 — The proved guarantee is much narrower than the empirical target

Claim challenged: MNIST at d784 or PCA d240, p1 and T600 is justified by the
circle theorem or shows general trained-network convergence.
Evidence: complete C.4.7.9, C.4.7.10 statement/part B/C.1 and D.1, current
docs/code guides, INITIALIZATION_THEORY.md. The maintained short-time
numerical theorem is for a rational two-arc family on S1 through T=1/200.
The time40 theorem uses a different explicit family of radius
rho=2^(-E10), E0=8192, E(j+1)=2^(Ej); its perturbations collapse at practical
declared precision. The theorem has meaningful exact nonlinear content but
does not resolve practically separated time40 inputs. General-d p1
initialization is valid finite algebra; trained dynamics identification and
order convergence on MNIST remain open. No all-time or endpoint result is
established by finite settling diagnostics.

### C05 — Fixed order and fixed memory are not dimension-free efficiency

Claim challenged: p1 approximates arbitrary accuracy by increasing P, or the
hierarchy avoids difficult high-dimensional computation at useful accuracy.
Evidence: H3.N3/N6; code guide; MODEL_SCOPE_CHECK.md. Closure order, initializer
quadrature, population rule, data integration, time step, arithmetic, network
width and physical horizon are distinct axes. The theorem is iterated, not
arbitrary joint refinement. Exact populations are distributions, not finitely
many numbers. Fully numerical state is fixed during one run, but required
order/resolution may grow with T and accuracy. The general-d total-degree
core, if extended directly, has binomial(2d+p,p) and binomial(d+p,p) features
before additional action words. The implemented p1 saves O(Pd+d^2) versus
O(nd+n^2) moving entries; no uniform saving when d grows with n follows.
Generic initialized-action compilation can grow rapidly. No cost-to-error
bound or computable tolerance selector is available.

### C06 — The empirical signal is real but not an efficiency frontier

Claim challenged: the PCA speedup establishes a broadly better learning
algorithm or a cheaper way to reproduce a wide network to a given fidelity.
Evidence: PCA_REPORT.md, FULL_4096_CHECK.md, PCA_RUN_CHECK.md. At common
attainable training MSE0.011080311898, closure/reference mean RMS is .0431777
original and .0416288 PCA; PCA closure/original network is .1053142 and
PCA network/original network .0975023. Centering removes a mean component
containing45.87% of uncentered energy; keeping98% centered variance retains
only53.05% uncentered energy. The changed representation is a changed target.
The within-PCA relative RMS4.09–4.62% and strong within-digit correlations are
positive evidence beyond label clustering. The fourfold fixed-T100 speedup
and80.20% allocation reduction are useful measurements, not matched-fidelity
or matched-loss walltime. Smaller dense networks, generic fixed bottlenecks,
trainable low-rank factors and other dimension reductions are missing controls.
P=n counts nominal antithetic nodes, only P/2 independent marks. The width
doubling changes P and n simultaneously, so cannot identify residual truncation.

### C07 — Output agreement can conceal inaccurate representations

Claim challenged: visually close outputs or moving hidden Grams establish
faithful internal dynamics.
Evidence: quadrant README: N5 output RMSE .04569 but second Gram relative error
.6488; frozen second Gram .6788, N1 .8653. Endpoint-discrimination README:
at T1000 N5 gap error .24814 versus N1 .55573/N3 .56036, but all plateau gates
fail; the N5 quadrature and network half-step gates also miss thresholds.
Time40 and broader arcs show useful Gram improvements but unresolved
quadrature. Circle spectral comparisons show N3 improves on N1 descriptively
across six multi-point cases, N5 improves three and deteriorates three; only
quad30 passes all available transition controls. These observations disprove
unqualified monotone *measured* improvement, not the asymptotic theorem.

### C08 — Nonlazy behavior does not establish useful ML generalization

Claim challenged: being closer than NTK to trained-network extrapolation proves
better out-of-sample risk, depth advantage, or explanatory generalization.
Evidence: XOR/quadrant matched-loss NTK comparisons strongly distinguish
nonlinear network-shaped extrapolation from frozen-kernel extrapolation, even
after equalizing training fit. No teacher exists off those training points.
The sparse-pair tanh–sine template is descriptive and fitted, not a derived
selection law. The current canon has narrowly scoped additional generalization
and frozen-feature comparison results, acknowledged in docs/README; those do
not automatically describe the numerical benchmark family or imply efficiency.
The simplest serious surviving alternative is that several small nonlinear
architectures learn similar easy-task predictors, with no special benefit from
the closure's Gaussian-informed dictionary. A fair fidelity/cost baseline is
the direct discriminator.

## Initial significance position for negotiation

Suggested ordinal rubric: 0=no substantiated contribution; 1=useful scoped
construction or pilot; 2=substantial specialist result; 3=major advance for
a stated research community; 4=broad field-shaping consequence. These are our
operational assessments, not promises of reception or publication.

- Mathematics: 2 for the scoped canonical hierarchy/identification theorem,
  with priority unresolved and no fresh full-foundation proof recertification.
- Numerical method: 1 currently, supported as a promising structured simulator;
  upgrade to2 requires resolved cost-to-fidelity advantage over appropriate
  cheaper comparators and separate resolution controls.
- Wider ML: 1 as evidence/prototype, not an established broadly competitive
  algorithm or explanation of practical generalization.

Major-level potential requires concrete bridges: (i) a nondegenerate broader
unchanged-model theorem with rate/complexity or verifiable error control,
(ii) broad controlled fidelity/cost wins, and/or (iii) a useful selection or
generalization mechanism with independent targets. These will be negotiated
as precise packages, not treated as conclusions already earned.

## Source inventory and actual read coverage

Repository: complete docs/README.md, docs/NOTATION.md, code/README.md;
complete C.4.7.9; C.4.7.10 opening, A.1, B, C.1, D.1 and relevant equations.
The full long source-cap/time40 foundation has not been independently
reproved/re-audited here. Complete required current-study README and eight
reports were read; relevant producer initialization and both RHS/forward maps
were inspected. The six earlier-study READMEs were read; feature_geometry has
only its startup README, hence supplies no completed result. Current circle
reports and numerical-control summaries were inspected; this assessment
does not pretend to rerun or recalculate their full arrays.

Primary literature (searched directly on2026-09-16):

1. Yang–Hu, *Tensor Programs IV*, PMLR139 (2021), sections2–5,
   https://proceedings.mlr.press/v139/yang21c/yang21c.pdf . Direct PDF text,
   relevant definitions/theorems read; not the full arXiv proof appendix.
2. Bordelon–Pehlevan, *Self-Consistent Dynamical Field Theory of Kernel Evolution
   in Wide Neural Networks*, https://arxiv.org/html/2205.09653v3 . Direct HTML,
   model/algorithm/cost sections and Algorithm1 located/read; no complete
   independent derivation audit. Same primary publisher/author version found:
   https://pehlevan.seas.harvard.edu/sites/g/files/omnuum6471/files/pehlevan/files/bordelonpehlevan_jstat_2023.pdf .
3. Yang–Santacroce–Hu, *Efficient Computation of Deep Nonlinear Infinite-Width
   Neural Networks That Learn Features*, https://openreview.net/pdf?id=tUMr0Iox8XW .
   Search-rendered primary text of sections2–3 and author publication page
   inspected; direct full-PDF request met a browser challenge. Full appendix
   not read. https://www.microsoft.com/en-us/research/?p=831388 .
4. Li et al., *Measuring the Intrinsic Dimension of Objective Landscapes*,
   https://arxiv.org/pdf/1804.08838 , section2.1 equation2 and section2.2
   objective/baseline distinction read directly. Shared subspace technique,
   not an identified exact priority match.
5. Nguyen–Pham, *A Rigorous Framework for the Mean Field Limit of Multilayer
   Neural Networks*, https://arxiv.org/pdf/2001.11443 . Introduction,
   embedding definitions11–13, theorem15 location, iid-degeneracy and
   correlated-initialization scope inspected; no full125-page proof audit.
6. Celentano–Cheng–Montanari, *The high-dimensional asymptotics of first order
   methods with random data*, https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf .
   Direct primary source accessed; scope is high-dimensional random-design
   dynamics, not an established matching theorem for this fixed-d width limit.
7. Koch–Lubich dynamical-low-rank bibliographic trail and author primary
   numerical article https://www.sciencedirect.com/science/article/pii/S0378475408001390
   inspected for moving-rank-space distinction. No claim of a full prior
   theorem match follows from the abstract/preview coverage.

Queries included neural-training Galerkin/low-rank/mean-field/finite-memory,
fixed random bases and intrinsic dimension; TP/DMFT/pi-limit; and2025–2026
fixed-basis closure terms. Many hits concerned neural PDE solvers, a different
target. This is a targeted literature check, not comprehensive exclusion of
prior art or proof of priority. No direct external text is quoted here.

## Debate record

The coordinator confirmed both openings frozen before either was exchanged.
The following is the subsequent direct exchange with the advocate; the opening
above is preserved as the initial position, including its superseded ordinal
scores. The final jointly negotiated rubric replaces those incomparable scores.

### Resolutions of opening objections

| ID | Advocate's substantive response | Critic's disposition |
|---|---|---|
| C01 | Accepts exact structured-network and weighted-backprop identity; particular Gaussian-informed factors and metric still matter. | Resolved: identity does not imply identical initialization/trajectory to arbitrary bottlenecks. No architectural or backprop novelty claimed. |
| C02 | Familiar approximation primitives do not discharge joint initialized law, true adjoint, target identification and stable exhaustive hierarchy obligations. | Accepted concession: the joint theorem is substantive; describing it as Galerkin alone does not assess it. |
| C03 | Accepts TP/DMFT/pi-limit and different parameterization/optimizer scope. | Resolved: feature learning and infinite-width computation are prior; the complete present contract remains only an unmatched candidate in inspected sources. C11 updates computational comparisons. |
| C04 | Accepts local versus tiny-radius time40 domains and absence of a MNIST theorem. | Resolved: microscopic domain does not invalidate exact theorem, but limits its present reach. |
| C05 | Accepts population laws, distinct refinement axes, dimension/order cost and accuracy-dependent resolution. | Resolved: fixed numerical state per run is precise; dimension-free efficiency is unproved. |
| C06 | Existing savings and own-target fidelity merit positive proof-of-concept credit even without frontier baselines. | Accepted concession: significant simulation proof of concept; superior cost-to-fidelity remains open. |
| C07 | Unresolved controls do not erase exploratory patterns; resolved quad30 supports both order transitions. | Accepted concession: retain positive controlled case and all adverse/missing controls; no monotone finite-order or internal-fidelity generalization. |
| C08 | Controlled own-frozen-kernel shape discrepancies and matched-loss extrapolation are real evidence of nonlazy dynamics. | Accepted concession: pure frozen-only account is rejected in those cases; generalization, selection and compression-superiority claims remain open. |

### Additional objections raised after exchange

**C09, coordinate dependence.** A fixed finite dictionary anchored to selected
input directions need not preserve the rotation symmetry of the target model.
The permitted spectral INSIGHT report gives rotation deviations around
2.6–2.8% at N1 and 0.7–1% at N3/N5, with its stated control qualifications.
PCA also changes coordinates, centering and scale. Advocate accepts this;
the final explanation must not imply automatic finite-order invariance.
The numerical milestone includes explicit rotations and a centering/PCA
decomposition diagnostic. Resolved.

**C10, more direct factorization and metric antecedents.** Both debaters
independently inspected Denil2013 sections2–3, LoRA-XS sections3–3.3 and
LoRA-SB sections3.1–3.6. Denil writes W=UV with a frozen dictionary U and
trained V, including ridge-constructed dictionaries. LoRA-XS freezes both
outer factors and trains a small middle matrix. LoRA-SB explicitly corrects
the core gradient by inverse outer-factor Grams; its orthonormal initialization
simplifies that correction. This strengthens the objection to architectural
novelty and to treating metric awareness as new. Neither inspected adapter
paper supplies the present whole-middle Gaussian initialization and
unchanged-flow population hierarchy theorem. Advocate expressly withdrew any
implication of novelty for the two-sided trainable-core ingredient. Resolved.

**C11, current nonlazy computation and compressed-history solvers.** Both
debaters inspect the recent primary sources rather than treating older direct
DMFT storage costs as universal lower bounds. Lauditi–Bordelon–Pehlevan2025
studies adaptive kernel predictors for Bayesian/noisy dynamics and GF with
weight decay at convergence. Its displayed setup uses homogeneous activations,
and its Figure1 distinguishes unregularized GF from that fixed-point predictor.
This is important prior nonlazy computation; it does not establish the present
unregularized tanh trajectory contract. DYNAMITE2026 compresses stored two-time
history using adaptive interpolation and thinning. Its algorithm appends
then sparsifies past slices; spin-glass benchmarks show sublinear, approximately
t^(1/3), memory. Hence quadratic storage is not inherent to every DMFT solver.
No implemented same-target feedforward comparison or fixed-current-state
equivalence was found here. The proposed comparator list includes practical
compressed-history methods when an exact target mapping is available.

### Significance negotiation and concessions

**A01, advocated higher present mathematical grade.** Advocate initially argued
for "highly significant within rigorous constructive approximation of deep
Gaussian feature-learning dynamics," given the coupled initialized-law,
adjoint and autonomous-convergence obligations. I agreed that those obligations
are substantive, but withheld that label because the result does not yet cross
the practical mathematical bottleneck of nondegenerate long-time reach or
usable quantitative error control: the existing theorem is qualitative and
local, or uses the microscopic time40 domain. This is not a demand that a
mathematics result beat ML benchmarks. Advocate accepted that bottleneck-based
rubric and withdrew the stronger present grade rather than narrowing its
community until the label fit. Resolved with genuine common assessment.

**A02, numerical significance.** I accepted the advocate's argument that
resolved quad30 refinement and measured current-model savings already justify
"significant numerical simulation proof of concept." Appropriate generic
compression baselines are required for a superiority claim, not for all
positive scientific significance. My initial numerical ordinal score is
superseded by that shared label.

Agreed current labels: **significant substantive specialist mathematical
contribution**; **significant numerical simulation proof of concept, superiority
unestablished**; **promising wider-ML proof of concept, below an established
significant methodological advance**. No present breakthrough, groundbreaking
or landmark label. These are our assessments of checked material, conditional
on the stated source/proof-read limitations, not external community verdicts.

### Negotiated future commitments, pending exact final-document audit

The advocate proposed explicit packages N (cost-to-output-fidelity frontier),
T1 (nondegenerate time40 family), T2 (usable certified computation, depending
on T1), and G (derived feature selection/generalization on rotated odd3-parity).
I accepted their target directions and exact pass-triggered labels, with
specific strengthened gates sent directly: separate reference and numerical
uncertainty included within tolerance, at least10 independent runs or rigorous
alternative, simultaneous95% bounds, continuous-time interpolation remainder,
no target-trajectory tuning, explicit total computational constants, no assumed
feature alignment and no deliberately weak kernel regularization comparator.
The final agreement will contain the complete contracts; this paragraph is
not a substitute for them or permission to execute them.

Additional direct primary-source coverage after the frozen opening:

- Denil et al., [Predicting Parameters in Deep Learning](https://proceedings.neurips.cc/paper/2013/file/7fec306d1e665bc9c748b5d2b99a6e97-Paper.pdf), sections2–3 read, including factorization and ridge dictionary; no full experimental audit.
- Bałazy et al., [LoRA-XS](https://arxiv.org/html/2405.17604v2), sections3–3.3 read; fixed outer factors and core, additive pretrained-weight context; no full proof/experiment audit.
- Ponkshe et al., [LoRA-SB](https://arxiv.org/html/2411.19557v3), sections3.1–3.6 and explicit Gram-corrected gradient read; no full appendix proof audit.
- Huang–Yau, [Dynamics of Deep Neural Networks and Neural Tangent Hierarchy](https://arxiv.org/pdf/1909.08156), section2 assumptions/theorem2.3, equation2.7 and theorem2.6 read. It truncates a kernel hierarchy in a width-expansion regime with an almost-static limiting NTK, not the present initialized-mark approximation to a rich population trajectory.
- Lauditi–Bordelon–Pehlevan, [Adaptive kernel predictors from feature-learning infinite limits of neural networks](https://arxiv.org/html/2502.07998v2), introduction, sections2–3 and target-limit distinctions read directly; not full appendices or numerical audit.
- Lang et al., [DYNAMITE](https://arxiv.org/html/2604.06309v1), sections2.3,3.1–3.6, memory scaling and limitations inspected directly; no new implementation test or audit of all error estimates.

### Late process disclosure

After the independent openings, shared present grades and N/T1/T2/G commitments
had already been negotiated, I called `collaboration.list_agents` solely to
check whether the advocate was still actively drafting. Unexpectedly, its
status response included completed older agents' final summaries. Thus prior
debate text was incidentally exposed in my context at this late stage. I notified
the coordinator and advocate immediately, did not request those summaries as
inputs, and did not use them to add evidence or change any scientific judgment.
The independent opening and the direct agreement preceding that call retain
their original provenance. This disclosure qualifies any broader reading of
the opening's no-prior-verdict statement: no prior verdict had been exposed
when that opening was written, but the later status call did expose such text.
The exact event was the `collaboration.list_agents({})` response after my
messages accepting G's concrete constants and sending the T2 fixed-word and
N target-specific-tuning cost clarifications, while the advocate was assembling
the agreed document. It preceded my immediate disclosure messages to both
agents. The clock was subsequently checked at 2026-09-16 08:44:20 UTC; it was
not sampled at the instant of exposure, so no invented wall-clock timestamp
is assigned to that event. The coordinator acknowledged the disclosure and
instructed preservation of the already settled collaborative assessment.

### Final contract precision and feasibility check

N's quantifiers were jointly made explicit: one prespecified epsilon pair;
the same at least six of eight cases, including both MNIST representations,
must pass at both tolerances; the no-greater-than25% runtime-regression gate
covers all eight cases at both chosen tolerances. Target-specific tuning costs
cannot hide a dense solve. T2 counts fixed64-bit work/storage, elementary-function
and multiword costs, with a uniform worst-case bound per requested law; it also
accounts for finite-precision parameter input. G specifies a common probability
event for the learning/kernel gap and separately tests predicted versus actual
subspace and actual versus teacher subspace.

**C12, G is not known feasible or near term.** Following the coordinator's
completeness question, both debaters independently inspected primary barrier
literature and directly agreed the qualification. [Damian–Lee–Bruna,
The Generative Leap](https://arxiv.org/html/2506.05500), section3 Theorem1 and
section5.1 Proposition4, gives a low-degree-polynomial weak-detection barrier
and identifies Gaussian r-parity's generative leap as r, yielding the related
d^(3/2) sample scale for three-parity. [Barzilai–Shamir, Limitations of SGD
for Multi-Index Models Beyond Statistical Queries](https://arxiv.org/html/2602.05704),
section2 equation3 and section5.3.2 Theorem6, studies fresh-sample SGD with
different loss/input, smoothness, width and gradient-condition hypotheses.
These are serious obstacles, not an automatically established impossibility
theorem for G's spherical reused-sample squared-loss gradient flow. The agreed
G contract is explicitly high risk, with no present feasible schedule or
near-term claim. An applicable obstruction would fail that route without
erasing N/T1/T2. No proof of applicability or escape was attempted.

This new literature was obtained by direct primary searches prompted by the
milestone-feasibility question; it was not taken from the incidental earlier
status output. Only the relevant statements/assumptions were read, not the full
barrier proofs. An older Abbe–Boix Adsera–Misiakiewicz COLT2023 primary abstract
and PDF were also located as background; no new conclusion is attributed to
an unread proof there. Current grades and conditional upgrade thresholds did
not change; the explicit feasibility qualification prevents interpreting those
thresholds as a prediction that they can readily be met.

## Final exact-document endorsement

I have read the complete final `NOVELTY_AGREEMENT.md`, including its final
N quantifiers, all T1/T2/G gates, current-literature and G-barrier qualifications,
and the explicit process/read-coverage limitations. I independently computed
and rechecked its SHA256:

    05d863109fcceeae46ea4a607826213b53b0eb925e6cb719085717d7a080d910

I **fully endorse this exact document** as the critic. No opposed present grade,
unaccepted qualification or substantive dispute remains. The agreed uncertainty
about priority, theoretical reach and empirical superiority is part of that
endorsement, not a residual advocate–critic disagreement.

I am committed to the document's stated upgrades when its explicit sufficient
conditions pass: N earns its highly significant numerical-simulation grade;
T1 earns its highly significant constructive-theory grade; T2 earns its scoped
simulation-theory breakthrough and broader deep-learning-theory highly
significant grade; G's valid novel theoretical subpackage earns its stated
feature-learning/generalization breakthrough, and its empirical subpackage
earns the additional checked-prediction wording. These are firm assessment
commitments under the exact target, attribution and validity gates, not a
promise merely to reconsider. The feasibility cautions remain fully endorsed.

Only the critic report was edited by this agent. No experiment, proof search,
scientific source edit, promotion or Git operation was performed.

### Superseding final endorsement after explicit input normalization

The coordinator identified an ambiguity in G's sphere variable after the
preceding endorsement. The advocate and I agreed to make our intended convention
explicit: normalized input u is uniform on S^(d-1), physical x=sqrt(d)u,
canonical Wx/sqrt(d)=Wu, and S_f uses the ambient derivative with respect to u.
This convention is already used in MODEL_SCOPE_CHECK.md and NETWORK_ENGINE.py's
canonical comparison. It changes no target intended by the debate, threshold
or significance grade; it prevents interpreting G as a different d-dependent
small-preactivation regime. G's Gram marginal is correspondingly named mu_U.

I have now reread the **entire revised final document** and independently
computed its exact SHA256:

    80ef6589ecaf79de096e5391e489a9f6ecc3a88f2658437a19a0f144f2fd5358

I **fully endorse this exact final document and every stated milestone/grade
commitment**. This is my operative final endorsement, superseding the earlier
hash retained above as process history. No substantive disagreement or opposed
grade remains. The shared uncertainty and feasibility limits remain endorsed.
