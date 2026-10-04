# What response memory is useful for: completed exploratory campaign

The strongest outcome is a differentiable model of feature learning that can
help design a training signal. A second outcome is a memory buffer that carries
effective learning between infrequent changes to a dense base matrix. Both
have controlled demonstrations. The first directly tests a new use beyond
trajectory approximation; the second gives approximation an operational purpose.
The streaming extension works but loses to a conventional factor learner, and
historical repair is informative but only conditionally useful.

This is a completed bounded investigation, not a claim that all practical
directions have been exhausted. Two RTX3090 GPUs were used concurrently. Every
route retained its unfavorable controls and stopped after the specified branch
or confirmation, without a broad benchmark or hyperparameter search. Sources
and protocols live in this study; generated evidence lives only in its own data
namespace. The manuscript, established code, and original implementation were
not edited. No result is promoted or asserted to be a first-of-its-kind method.

## 1. Design labels by differentiating through the closure

Suppose training for a fixed budget will produce a network, and we can choose
the labels on eight support inputs. We want those labels to make the resulting
network predict a prescribed smooth circle function well. The design problem
requires anticipating how representations change during learning. A frozen
feature predictor answers a different problem, even if its own label-design
objective is solved exactly.

We differentiate through the autonomous order-q response-memory learner, including
its activity clock and all recurrent moment dependencies, optimize the labels,
and then restart the actual dense learner on those labels. Evaluation uses
the dense learner's final predictions on a disjoint circle grid. Thus a good
fit by the surrogate alone is not counted as success. The exact teacher,
optimization budget, initializations, label constraints and source mapping are
in [HYPERGRADIENT_REPORT.md](HYPERGRADIENT_REPORT.md).

On five fresh width512 initializations, q1 retains88.96--90.91% of the improvement
obtained by optimizing through dense training itself, with median90.52%.
Its median reduction from original-label dense error is79.85%. Frozen-feature
design does substantially worse; solving that frozen objective to its boxed
convex optimum makes its transfer worse still. This rejects incomplete outer
optimization as the explanation for that particular control's failure.

Subsequent stronger comparisons are important. Training the first layer and
readout while freezing the middle matrix does not reproduce q1's label-design
benefit on two matched seeds. A rank-eight learned correction, with virtually
the same number of moving coordinates as q1, does produce substantial benefit
at its slowest prescribed factor rate. q1 has lower dense error on both seeds,
by51% and19% relative to that best tested rate. The factor alternative remains
viable; more extensive rate or parameterization search was not performed.
Irregular support angles preserve roughly90% retained improvement on two
additional seeds. One second-teacher stress also passes. Details and numerical
qualifications are in [HYPERGRADIENT_CONTROL_RESULTS.md](HYPERGRADIENT_CONTROL_RESULTS.md).

The useful scientific distinction is between **being easy to train** and
**being a faithful guide for choosing how another learner should train**.
The factor learner with mobility1 fits its own designed-label problem better
than the slower factor learner, but its labels transfer much worse to dense
training. The closure offers a prescribed dynamics for this second purpose.
The experiment supports its usefulness without showing that its particular
history variables are uniquely responsible for the effect.

There is also a concrete memory tradeoff. With identical16-step checkpointing,
one width512 outer gradient uses21.09MiB allocated peak for q1 versus54.29MiB
for dense differentiation, including fixed matrices. It takes.870s versus.539s.
This implementation saves memory and costs time. It does not eliminate the
fixed n-by-n matrix, prove an optimal memory bound, or outperform every possible
recomputation scheme. The comparison is one warmed benchmark, not a hardware
performance study.

An independent internal reviewer freshly reproduced complete n128 and n512
dense/q1 label designs, audited explicit matrix and gradient oracles, and found
MSE discrepancies below6e-8. The [review](HYPERGRADIENT_INDEPENDENT_REVIEW.md)
supports this narrow result. Its scope corrections are applied in the control
addendum: reused evaluation grid, fixed design/retraining initialization,
antipodal rank deficiency, retained dense initializers, and auxiliary-script
reproduction limitations. The practical labels and, for the regular support,
the singular full-sample Gram lie outside the manuscript's stated all-time
theorem assumptions. Prediction-approximation theory alone does not prove
hypergradient accuracy.

**Paper value:** a concrete experiment showing that response memory can serve
as a differentiable inner learner in an outer design problem. The proposed
contribution is this use of the paper's autonomous feature-learning object,
not a new invention of dataset distillation or a general competitive benchmark.
The [primary-literature note](HYPERGRADIENT_LITERATURE.md) distinguishes the
construction from established data-design and memory-efficient differentiation
work. This is the best candidate for a focused new application figure.

## 2. Learn between infrequent writes to the base matrix

Consider a system in which changing a large matrix is expensive, but reading it
and updating smaller digital state are possible. Merely postponing gradient
writes leaves the function stale while later gradients are computed. The closure
instead changes the effective operator continuously through the response moments.
At chosen times its current correction is added to the base, and fresh moments
are initialized from the current features. Consolidation preserves the function
on every query exactly at the instant of the reset; its future finite-q dynamics
change because their remembered history has changed.

The decisive experiment uses eight successive training supports, each rotated
relative to the last, so fitting must continue after each consolidation.
At width256, q3 uses eight base consolidations over4096 accepted training steps.
Across five new initializations, average whole-circle RMS discrepancy from dense
learning is.00108. The matched delayed-gradient control gives.2525; rank24
factor learning gives.0475. The delayed control keeps full uncompressed gradient
history and writes at the same eight boundaries, so losing that history does
not explain its failure. Every buffer block fits to RMS below.00085.

The [report](WRITE_BUFFER_REPORT.md) includes source-level identities, the
product-form local velocity defect, half-step repeats, and a width512 check.
Its approximately.001 dense discrepancy is comparable to some finite-step
changes, so the decimals do not certify continuous-flow accuracy. The much
larger gap to delay survives numerical refinement. A shifting-input feature
diagnostic was excluded because it mixed input movement with feature learning.

The base is still stored and read; this is not a total-storage reduction.
The PyTorch buffer is about twice as slow as dense training, and no energy was
measured. Factor learners can fit well while selecting a different function,
so dense fidelity is not itself a predictive advantage. This is an algorithmic
demonstration for a possible write-constrained platform, not a demonstrated
hardware benefit or a solution to catastrophic forgetting.

**Paper value:** a precise explanation of why low-order continuous feedback
can be useful even when ordinary low-rank adapters or batched writes are
available. It is a secondary use case with an explicit systems constraint.

## 3. Replace observation slots by an input dictionary

The original moments index a fixed training support. The input-field extension
projects forward and response histories onto a prescribed Fourier dictionary
under the uniform circle distribution, replacing sample sums by expectations.
Incoming batches estimate those sources; there are no permanent slots for
observed examples. Indicator dictionaries recover the finite-support equations
with the exact normalization, giving an algebraic consistency check.

The canonical streaming panel uses n128, q3, five dictionary functions, fresh
IID batches of64 for4096 steps, and262144 observed input-label pairs. All models
share the same input sequence. Median evaluation RMSE across five fresh seeds:
response field.01802, dense.01219, readout-only.38139, moving-first-layer with
fixed middle matrix.02055, and trained rank15 factors.01014. The field improves
over the fixed-middle model on all five seeds, but loses to factors on all five.
Feature motion on fixed query inputs is substantial.

The first81 fits had an extra input factor1/sqrt(2). The error was found during
the root audit, recorded, and corrected before rerunning exactly the same81
configurations without retuning. The old experiment is retained as an explicitly
scaled-input variant; the figures above use only the canonical rerun. See
[INPUT_FIELD_NORMALIZATION.md](INPUT_FIELD_NORMALIZATION.md) and the corrected
[report](INPUT_FIELD_REPORT.md).

The construction is a valid exploratory architecture, but moving-coordinate
savings do not remove its fixed matrix. Total persistent storage exceeds dense
storage at this tested width, and it is slower. The strongest control wins.
This is a useful negative finding: making the closure accept new inputs does
not, by itself, establish a practical reason to replace a fully connected layer.
No structured-mixer or recurrent-model search was launched to rescue the result.

## 4. Use response histories to inspect and repair previous learning

Here the moments observe an actual dense trajectory; they do not drive an
autonomous approximation. Two known corrupted examples supply recorded
contributions to the hidden-matrix update. Four Legendre modes reconstruct
their accumulated matrix contribution within.23% relative Frobenius error,
using32 times fewer coordinates than a separate matrix accumulator per example
at width256. Subtracting the reconstructed contribution, then doing two time
units of clean training, closely reproduces the exact-history edit.

Five fresh seeds have positive error reductions, with24.64% median reduction
relative to equal-budget cleanup alone. One improves only1%, failing the original
10% practical criterion. A clean-training-loss line search preserves an advantage
over matched current-gradient edits in all five seeds, while25% extra ordinary
cleanup catches up in two. The earlier attempt to show a large effect from
destroying centered historical pairing failed its specified gate and was stopped.
The [full report](HISTORY_RESULTS.md) preserves both outcomes and the online
moment derivation.

This can inspect a recorded route by which learning changed a matrix; it does
not reconstruct what training would have done without those examples. Other
examples' histories and the outer layers were also affected by corrupted labels.
It therefore supplies neither certified forgetting nor a competitive unlearning
method. q1 repairs better than exact history on all five confirmations, further separating
historical fidelity from optimal intervention. This is an interesting diagnostic
side result, weaker than the first two application candidates. An
[independent check](HISTORY_INDEPENDENT_REVIEW.md) reproduced every saved
seed201 scientific value and array exactly, while documenting the failed
practical-effect gate, incomplete coordination controls, and observer-helper
limitations outside this positive-activity benchmark.

## Recommended scientific emphasis

The strongest addition would ask whether the closure can guide decisions about
learning, then answer with the label-design experiment, its strong controls,
and the measured memory/time tradeoff. The write-buffer demonstration can supply
a second operational use with a clearly stated matrix-write constraint. The
streaming and repair routes are worth retaining as bounded evidence about where
the same idea does and does not yet add value.

The demonstrations are small synthetic circle problems with two tanh layers.
They establish reproducible uses of the object, not broad real-world advantage
or a claim of literature-wide novelty. Further scope would require new tasks,
new controls and explicit resource allocation. This campaign stops here; it
does not keep searching until all routes become positive. All results remain
study-owned and unpromoted.
