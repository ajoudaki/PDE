# Stage2: strong tests of memory addresses and temporal coordination

The requested two directions received a substantial theoretical and experimental
push. The strongest supported results are structural: memory addressing changes
optimizer geometry; moving addresses face a precise history/coordinate tradeoff;
and Legendre moments implement controlled temporal interventions. Neither route
establishes the requested broad practical breakthrough. All tested architecture
candidates fail their frozen practical advantage gates, and the temporal tests
do not establish useful higher-order chronology beyond phase means and ordinary
gradient controls. These negative outcomes must accompany the exact results.

There are330 author-run training/continuation solves on three real datasets,
plus separately documented independent reproductions. The count includes short
continuations and numerical replays, not330 independent statistical experiments.
Both RTX3090 GPUs were used, with simultaneous independent routes, CUDA capture
checks, held-out confirmation initializations, strong controls, and step/width
tests. The common model remains a two-hidden-layer scalar-output tanh network;
these are mechanism studies on real data, not modern large-model benchmarks.

## 1. Memory addresses are part of the learning rule

Suppose H is the n-by-m current feature matrix, R the n-by-m matrix of residual
times backward response, and P an orthogonal projector on the chosen input
address functions evaluated at the training examples. The dense hidden gradient
is proportional to R H^T. Even before truncating time, shared input indexing
replaces it by R P H^T. Orthogonality in sample space does not make this a
descent direction in weight space.

An exact criterion identifies the problem. Put K=H^T H. Then

    <R H^T, R P H^T>_F >= 0 for every R  if and only if  KP=PK.

Thus a universally descent-preserving input projection must respect the current
feature Gram geometry. This condition concerns every possible backward matrix;
failure of commutation alone does not prove ascent for the actual network's R.
Current-feature PCA obeys the condition instantaneously and yields ordinary
right-projected gradient descent. A fixed initially suitable basis can lose
that property as features move. Parameter-space projected-gradient methods
should not be conflated with the unsafe sample-space projection above.

This also identifies a protective feature of the manuscript's original sample
indexing. There P=I, so the instantaneous spatial term is the genuine negative
hidden gradient; any extra hidden-motion discrepancy comes from finite temporal
memory. Replacing sample addresses can introduce a SECOND error mechanism that
survives arbitrarily accurate time resolution. This is a direct design lesson
for extending the paper's object, rather than a claim that the original closure
has failed the altered architecture's experiment.

The construction is more than an arbitrary-state warning. For every fixed
finite Legendre order q>=1, a binary-label three-input tanh example with zero
readout and the exact prefix/activity clock has increasing TOTAL loss at a
specified finite time. The leading learning mode is an oscillator. With
initial hidden amplitude epsilon and labels(-1,1,1), the derivative is
epsilon²/36+O_q(epsilon⁴) at t=3pi sqrt(3/5). The proof includes all outer
updates and extends to an open set of Gaussian-supported initializations at
each finite width. It gives no typical-width probability or eventual failure
claim. Importantly, increasing time order cannot universally repair a bad
spatial address system. This is an extension/counterexample for shared indexing,
not a contradiction of the paper's original sample-indexed theorem.

The finite-order equations also give an exact inexpensive diagnostic. The
reconstructed hidden velocity has rank at most2C for C input addresses,
regardless of q, and its loss contribution can be contracted without a dense
hidden gradient. It splits into an instantaneous spatial-projection term and
a temporal-lag term. On three fresh Fashion initializations, the hidden motion
opposes fitting at87.5–90.6% of sampled times while outer-layer dissipation
keeps the sampled TOTAL derivative negative. The seed4101 decomposition shows
the same positive-time fraction in the spatial term; the temporal term is
mostly helpful. HAR and housing do not show this hidden ascent. Early helpful
contributions are larger, so the frequency does not prove net harm or justify
freezing the layer.

A common Lipschitz gate on every memory derivative and the common clock
guarantees nonpositive hidden loss contribution in continuous time, without
new moving coordinates. That new optimizer was tested too. It did not improve
practical accuracy against ordinary fields and tuned factors. Descent safety
and useful learning are distinct requirements.

Proofs: [geometry and finite-q theorem](STAGE2_CHALLENGE_THEORY.md).
Experiments and diagnostic figure: [loss certificate and gate](STAGE2_ROOT_GATE_RESULTS.md).
Independent review: [geometry review](STAGE2_GEOMETRY_INDEPENDENT_REVIEW.md).

## 2. Adapting addresses has two different meanings

Retrospective reindexing applies the NEW dictionary to every old observation.
Old coefficients determine new coefficients for every square-integrable history
if and only if the new span lies within the old span. With equal dimensions,
the spans must coincide. Moving outside the old span requires discarded history;
overlap transport cannot recover it. The theorem concerns this coefficient
representation and arbitrary histories, not all possible encoders or a neural
reachability impossibility theorem.

Write-time indexing instead keeps the address that was present when each
observation was written. If input functions are orthonormal at each historical
time, their products with Legendre modes are orthogonal on joint input/time
space. The ordinary source-plus-dilation ODE and product-tail identity remain
exact for that projection, without a retrospective transport term. But changing
coordinates can make even a constant signal require higher temporal order.
The prefix-compatible sign-flip example demonstrates complete q1 memory loss
with an unchanged spatial span. Thus avoiding missing-history transport does
not automatically make the representation useful.

The theoretical distinction has material numerical consequences. In a calibrated
Fashion frozen-state diagnostic, exact retrospective reindexing into current
feature-PCA addresses changes test predictions by1.088 RMS relative to overlap
transport and worsens target RMSE from0.674 to1.307. Recovering omitted history
is not automatically beneficial: the current-feature variance objective differs
from the historical paired-response objective. This is a frozen-state diagnostic,
not evidence for an oracle training algorithm.

All99 fixed/adaptive field comparisons failed the preregistered advantage gate.
Median paired fixed-field/factor RMSE ratios were0.9883 Fashion,1.3789 HAR,
1.0079 housing; adaptive retrospective and write-time variants did not rescue
them. The gate was at least5% improvement on two domains, with no more than5%
degradation on the third and seed consistency. The field also retained extra
dictionary storage and was slower than the tested controls.

The final alternative used supervised label populations rather than feature-PCA
addresses: two classes, or four training-target quantile bins. It needs no query
label and avoids the initialized-first-layer dictionary copy. Another42fits
tested q1 and a rank-bound24 higher-order variant against tuned rank24factors.
The matched variant's median paired ratios were1.0057,1.2043,0.9973 on Fashion,
HAR,housing. It also failed. This rules out those simple rescues in these tests,
not every possible learned or nonlinear index.

Sources: [indexing theory](STAGE2_INDEX_THEORY.md),
[indexing campaign](STAGE2_INDEX_REPORT.md),
[prefix correction](STAGE2_INDEX_REVIEW_CORRECTION.md),
[label-population candidate](STAGE2_LABEL_INDEX_RESULTS.md).
Its [independent review](STAGE2_LABEL_INDEX_INDEPENDENT_REVIEW.md) verified all
42fits and168 checkpoint selections/test metrics and reproduced a Housing run
bitwise, after independently rebuilding the datasets and checking grouped sources.
The [independent indexing review](STAGE2_INDEX_INDEPENDENT_REVIEW.md) audited
all99records, rebuilt every dataset row from raw downloads, and reproduced a
fresh confirmation trajectory bit for bit. Its one minor prefix-example issue
is repaired in the separate correction without rewriting frozen sources.

## 3. Legendre moments give a precise temporal intervention tool

For a recorded dense Euler trajectory, hidden weights accumulate products of
the current forward feature and residual-weighted backward response. Permuting
one history preserves its entire empirical distribution while changing the
pairing. Applying the same permutation to both histories leaves the update
exactly unchanged. Uniformly random re-pairing has the mean-only q1 increment
as its exact expected matrix, with a closed second-moment formula.

Legendre parity makes a particular intervention especially concrete. For shifted
Legendre p_j on normalized time u in[0,1], p_j(1-u)=(-1)^j p_j(u). Reversing
one history therefore changes only the odd-mode interaction. Its weight edit
can be constructed from stored coefficient vectors, with an exact omitted-tail
product bound. No stepwise history is needed by the coefficient formula. In the
confirmation runs q8 reproduces reversal's test predictions within5.88e-4 RMS;
q16 has at most0.035% relative edit error on the six step/width stresses.

These are physical-time, prefix-free OBSERVER moments, explicitly different
from the manuscript's raw activity-clock moments inside an autonomous closure.
Observed dense coefficients need not equal self-consistent closure coefficients.
An edited endpoint is not the endpoint of ordinary GD under a realizable
alternative history. Those distinctions are essential to scientific use.

The strong empirical controls reject a simple useful-chronology story. On fixed
data, reversal's median changes in test MSE were−0.50% Fashion,+0.24% housing,
−3.31% HAR. Mean-only replacement and norm-matched ordinary gradient edits often
matched or exceeded the improvement. The controls preserve both left/right
edit Gram matrices, as well as norm and singular spectrum; isotropic noise
alone would have made learned-direction effects look more special than they are.

We then tested joint, sequential AB/BA and alternating supports with exactly
equal integrated exposure per example, four fresh seeds and three domains.
The targets never changed. Effects became larger and more structured. On Fashion
BA, within-phase reversal increases median test MSE by21.22%, while swapping
whole phases decreases it by7.65%. Yet phasewise q1 swap already decreases it
by7.94%; for AB the q1 improvement is8.45% versus3.31% for the full swap.
Phase means, detailed within-phase timing and support order have different
effects. “Destroying temporal structure hurts” is not a valid general account.

On housing, subgroup curves and ordinary-gradient controls identify substantial
last-support bias. The declared cross-domain phase-alignment statistic fails
every domain, and every domain fails the requirement that higher-order structure
explain more than phasewise means. These are useful discriminations of competing
mechanisms, but no tested intervention establishes optimizer superiority.

All training inputs remain available to the observer, including currently
zero-weight inputs. This is NOT replay-free continual learning. The higher-order
observer can use more state than one dense matrix; only temporal-history
compression is demonstrated, without a production memory or speed claim.

Sources: [complete temporal identities](STAGE2_COORD_THEORY.md),
[fixed-support tests](STAGE2_COORD_FIXED_RESULTS.md),
[equal-exposure curricula](STAGE2_COORD_CURRICULUM_RESULTS.md).
The [independent temporal review](STAGE2_COORD_INDEPENDENT_REVIEW.md) checked
all75 endpoint archives,873 saved edit predictions, and a full Fashion AB
autograd replay. It supports the identities and both negative experimental
conclusions, with two nonblocking precision corrections: the old Gaussian-QR
rotation controls were spectrum matched but not Haar-isotropic; permutation
preserves the coordinate Gram, while the time-indexed Gram is conjugated.
The [correction and calibration](STAGE2_COORD_REVIEW_CORRECTION.md) supplies the
precise statements and156 corrected Haar directions on60 frozen endpoints.
Old controls reproduce exactly, corrected invariants pass, and the largest
curriculum aggregate absolute effect remains0.114%. Neither correction changes
the stronger same-Gram sign controls or the failed primary gates. No training
was added by that calibration.

## Paper use and terminal decision

The defensible new contributions are a design criterion/obstruction for shared
memory addresses, an exact finite-order loss-direction certificate, and controlled
history interventions with interpretable coarse/fine temporal components.
These can support a structural scientific discussion or motivate a new research
program. They do not yet support presenting a competitive architecture,
continual-learning solution, generic generalization benefit, or a major practical
breakthrough. Their originality beyond related projection/memory literature
also needs a dedicated novelty assessment before a publication claim.

The current paper remains the scientific baseline. No paper claim is extended
to changed input indexing, gated clocks, weighted curricula, or observer surgery
without a separate derivation. The paper and its included mathematical files
still match the stage1 hashes; no manuscript/source-baseline edit was made.
No unrelated study, archived book or historical conversation claim supplied a
proof dependency. The original authorized canonical source copy remains intact.

This campaign ends after its frozen controls and final supervised-index candidate,
rather than continuing to choose new variants after each unfavorable result.
The contracts, negative outcomes and earlier abandoned interpretations remain
visible. The Stage1 differentiable-training-signal result is not strengthened
or retested by this continuation. All new findings are study results; even
independent internal checks do not constitute established-book promotion or
external peer review.

## Reproduction, resources and exact source variants

All code/proofs/configurations live flat in this study; generated data, raw public
datasets, source snapshots and summaries are in its designated generated folder.
Official dataset sources/splits/transforms are fixed in STAGE2_DATA_PROTOCOL.md.
Fashion is T-shirt/top versus shirt; HAR is moving versus stationary on supplied
features with subject-disjoint splits; housing is bounded target regression.
There is one data split per domain and multiple initialization replications,
not independent population replications. Validation selects architecture
checkpoints; test targets never select interventions or hyperparameters.

Author solve accounting: index99; diagnostic index replays3; temporal fixed96
(including60short continuations); temporal curricula54; gate33; gate diagnostic
replays3; supervised label index42. Sum330. Three independent full replays bring
the total to333; four independent internal reviews record their scopes and
checks explicitly. Tiny finite-dimensional algebra/ODE checks are
recorded separately, including one failed boolean serialization and identical
rerun. Captured/eager parity, autograd mobilities, orthogonality, exact history
identities and step refinements all passed their stated gates. Review corrections
concern the prefix example, reusable zero-label gate, random-orientation control
distribution and history-Gram wording. They change no training trajectory or
primary practical conclusion. The old artifacts remain frozen.

The full-fit ceiling was amended before the final42-fit candidate from300to360;
aggregate GPU-process cap remains240minutes. Logged producer sections are about
13GPU-process minutes including the offline control repair, with startup/check/
analysis overhead additional, not a
performance benchmark. Reproduction commands are in the exact per-run manifests
and route reports. Current source includes documented output-path/zero-label
repairs; original numerical producer snapshots remain available for exact replay.
Final integrity evidence is generated stage2_final_audit01/audit.json, covering
all manuscript-input hashes, immutable baseline, unchanged HEAD/index, flat-source
syntax, local result links and the four frozen independent review hashes.
