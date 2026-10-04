# Adaptive shared indexing: frozen stage2 protocol

Written before stage2 scientific execution. This route owns only
`stage2_index_*` and `STAGE2_INDEX_*`, uses GPU0, and has a terminal cap of
100 fits and75 aggregate GPU-process minutes. It uses the investigation,
canonical-notation/neural conventions, and rigorous-proof skills.

The question is whether replacing observation slots by shared, potentially
learned input functions gives useful training behavior beyond low-rank
optimization, and what adapting such an index does to retained histories.
No theorem for the manuscript's sample closure is imported for this altered
input-projected algorithm. The retained Gaussian base matrix and dictionary
evaluation data are charged explicitly.

## Mathematical bottleneck

For the current hidden feature vector h(x), covariance C=E[h h^T], and
eigenpairs CV=V Lambda with V^T V=I and Lambda>0, the orthonormal functions
psi(x)=Lambda^(-1/2)V^T h(x) satisfy
E[r delta psi^T] E[h psi^T]^T=E[r delta h^T] VV^T.
Thus instantaneous adaptive feature indexing equals right-projected gradient
descent. Retrospective reindexing of history additionally requires transporting
past moments when psi changes. We will derive the exact connection term and
an information obstruction to reconstructing it from old finite moments.
Write-time adaptive indexing is different: if psi_c(x,xi) are orthonormal at
each historical clock xi, their products with Legendre modes remain orthogonal
in joint input/time space. Its source-only moment ODE is exact, while basis
orientation affects its finite-order approximation. This distinction was
derived and added before any execution.

## Empirical contract

Three non-circle scalar-target datasets prepared independently by root, each
with fixed train/validation/test splits and train-only feature/target scaling.
Root's independently selected domains are FashionMNIST0-versus6,
CaliforniaHousing regression, and UCI-HAR stationary-versus-moving. Root
embeds train-standardized features with a constant coordinate and unit row
normalization. API rows are these unit vectors, exactly corresponding to raw
x=sqrt(d)*APIrow. Data files and their provenance are frozen
and hashed. Inputs passed to Flow are exactly declared raw x/sqrt(d).

Two tanh hidden layers of width128, no biases, independent Gaussian initial
W1 entries N(0,1), W0 entries N(0,1/n), exactly zero readout, unhalved MSE,
mobilities(n,1,n). Full training-set deterministic Euler integration; this is
an empirical input law and does not test fresh population observations.
All methods share initial W1/W0/readout and train/validation/test data.
Main step1/32, horizon128, checkpoints16,32,64,128. Select each fit's checkpoint
using validation RMSE only. Held-out test data cannot tune methods or timing.

Dictionary is train-only uncentered PCA of initialized first-hidden activations:
psi(x)=Lambda^(-1/2)V^T tanh(W1(0)x/sqrt(d)). This is a genuine evaluable function
on unseen inputs. The initial W1 copy, V, inverse eigenvalues, and fixed W0 are
retained costs. Empirical orthonormality must pass before fitting. Eigenvalues
are computed in float64 and must exceed1e-8 times the largest. Rank failure
makes that domain inconclusive without changing the declared rank. No label
or validation/test information enters the dictionary.

Pilot seed101 on each domain compares seven configurations: field C8,q3;
field C24,q1; conventional W0+AB rank24 with A(0)=0 and B entries N(0,1/24)
using common factor mobilities0.25,1,4; fixed right-projected rank24 descent
using the top24 initial feature covariance eigenvectors; canonical dense.
The outer mobilities stay canonical for every model. Field has 2nCq moving
moments; factors2nR; projected descent nR with a fixed nR right basis. Rank
counts are bounds rather than claims that effective numerical rank matches.

Freeze the lower validation-RMSE field variant and factor mobility separately
per domain. Confirmation uses new initialization seeds201,202,203,204 and the
chosen field, tuned factors, projected and dense:48 fits after21 pilots.

Primary practical prediction: across confirmation seeds, the field's median
test-RMSE ratio to tuned factors is <=0.95 on at least two domains and <=1.05
on the third. At least3/4 seeds must improve on every passing domain. Failure
on any required condition rejects this practical prediction. Intermediate
ratios are not relabeled as success. Prediction RMSE to dense, target RMSE,
actual feature motion, subspace drift, state counts and runtimes are secondary.
No speed or total-memory advantage follows from a moving-state count.

Mechanism prediction: same-state adaptive covariance functions reproduce
right-projected gradient exactly; finite-memory transport loses the part of
old histories outside the old input span. Numeric oracles check the identity
and exhibit two histories with identical retained moments and different new
moments. Network-history diagnostics measure reconstruction discrepancy and
omitted interaction, not a new population theorem.

## Warranted follow-up and terminal stop

At time64 record principal-subspace drift of current versus initial hidden
feature input spans, normalized as ||(I-P_old)U_new||_F/sqrt(C). If >0.2 on
at least two domains for pilot seed101, run a declared approximate-adaptation
branch on all three domains and four confirmation seeds in TWO variants:
refresh the PCA dictionary once at64 and Procrustes-align the new basis to
the old. Either transport old moment columns by their empirical overlap or
keep old moments and only write new sources in the new basis. The former is
approximate retrospective reindexing; the latter is write-time indexing.
Each variant gets12 fits; compare to the fixed selected field and factors using the
same frozen practical gate, while labeling the branch separately. If the
trigger fails, omit this branch. A direct retained-history oracle quantifies
transport error, and no oracle state is given to the learning algorithm.

Six refinement fits: selected field and factor, confirmation seed201, each
domain at half step1/64, same physical checkpoints. A practical conclusion
requires target-RMSE perturbation <1% of label RMS and less than one-third
the claimed absolute field/factor advantage. If violated, the affected
comparison is inconclusive; no open-ended step search. Total campaign99 fits
maximum. Remaining1 slot is only for a failed infrastructure replay or a
pre-execution documented correctness repair, never scientific reselection.

Validity: float32 GPU with TF32 disabled; one CPU thread. Float64 deterministic
oracles require errors<1e-10; orthonormality error<1e-5 float32. Eager/captured
update parity at short horizon<2e-5 relative/absolute; finite state throughout.
No adaptive timestep guard changes the scientific clock. A failed numerical
gate labels the comparison inconclusive. Each fit stops at horizon or90 wall
seconds. Every run has a fresh directory, source/protocol/data hashes, precise
command/environment, raw prediction arrays, all checkpoints and all failures.

Novelty claims are limited to the explicitly derived response-memory indexing
transport and tested construction. PCA, projected gradient methods, and low
rank parameter training are existing ideas; targeted primary sources will be
read before positioning. No exhaustive novelty claim or manuscript edit.
