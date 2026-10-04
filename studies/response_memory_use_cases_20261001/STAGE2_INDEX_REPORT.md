# Shared indexing: an exact distinction, an obstruction, and failed practical gains

The stronger multi-domain campaign does **not** establish a competitive
learning algorithm. Its substantive result is a precise choice that adaptive
response-memory indices must make. Retrospective reindexing of stored histories
needs information discarded by the old dictionary. Write-time indexing avoids
that information requirement and retains an exact orthogonal projection, but
turns basis motion into temporal complexity. Even rotating coordinates within
an unchanged input span can erase all zeroth-order memory. The complete
definitions and proofs are in [STAGE2_INDEX_THEORY.md](STAGE2_INDEX_THEORY.md).

All99 preregistered fits completed, including24 adaptive follow-ups and six
step refinements. Across Fashion-MNIST, human-activity sensors and housing
regression, fixed and adaptive dictionaries all fail the frozen practical
criterion against validation-tuned rank-matched factors. Three additional
root-budget diagnostics show that the missing retrospective history can
change predictions substantially; recovering that history can also make
prediction worse. This is a useful obstruction to the attractive shortcut
“learn a better current dictionary and simply reindex old memories.” It is
not an impossibility theorem for every adaptive response-memory architecture.

## Exact results and scope

For a fixed input probability law mu, let h(x) be the current first hidden
activation, r(x)=f(x)-y(x), and delta(x) the second-layer backward response
excluding r. The canonical hidden gradient velocity is
G=-2E_mu[r delta h^T]/n. Let V contain orthonormal eigenvectors of E_mu[h h^T]
with positive eigenvalues Lambda. The functions
psi(x)=Lambda^(-1/2)V^T h(x) are orthonormal under mu and satisfy

\[
-\frac2n E[r\delta\psi^T]E[h\psi^T]^T=GVV^T.
\]

Thus instantaneous indexing by these current-feature functions is exactly
right-projected gradient descent. A low moving-state count alone does not
distinguish it from an established optimization construction.

For retrospective memory, the dictionary at current time t is applied to
every historical signal. Differentiating such moments produces a connection
term integrating the old history against partial_t psi. Its component within
the old dictionary is known; its orthogonal component is not. More sharply,
old coefficients determine new coefficients for **every square-integrable
history if and only if the new span lies inside the old span**. With equal
finite dimensions, their spans must coincide. The proof constructs two
histories with identical old coefficients and different new coefficients.
It concerns this history representation, not arbitrary encoders or the full
set of reachable neural histories.

For write-time memory, a history recorded at clock xi uses psi_c(x,xi).
Provided these functions are orthonormal in x at each xi, the functions
psi_c(x,xi)p_j(xi/tau) remain mutually orthogonal in joint input/time space,
with squared norms tau/(2j+1). The ordinary raw Legendre moment ODE is then
exact, without a basis-transport term. Reconstructing the hidden correction
from paired moments leaves exactly the product of the two omitted projection
tails. This identifies an implementable adaptive projection; it proves no
small-tail, trajectory, fitting, stochastic or all-time guarantee.

The caveat is concrete: rotate a two-dimensional input basis through a full
turn over the history interval while keeping its span and the underlying
signals constant. With q=1 all retained coefficients vanish, whereas the
constant basis represents the same interaction exactly. Procrustes alignment
is a reasonable coordinate choice, not a theorem controlling this temporal
complexity.

## Frozen experiment and controls

[STAGE2_INDEX_PROTOCOL.md](STAGE2_INDEX_PROTOCOL.md) was written before any
fit. Root independently prepared1024training,256validation,1024test examples
on each domain; [STAGE2_DATA_PROTOCOL.md](STAGE2_DATA_PROTOCOL.md) and the
generated data manifest specify hashes and official provenance. Fashion is
class0versus6; HAR is moving versus stationary using its561 supplied features,
with validation and test subjects disjoint from training subjects; housing
uses tanh of train-standardized house value and a random geographic mixture,
not raw-price RMSE or geographic extrapolation. Inputs are train-standardized,
clipped, appended with a constant coordinate, and normalized to unit API row
norm. Raw mathematical inputs are sqrt(d) times these rows, so Flow receives
exactly x/sqrt(d).

Every model has two tanh hidden layers, width128, Gaussian first weights of
variance1 and hidden weights of variance1/n, exactly zero initial readout,
unhalved MSE and outer mobilities n. The full training set supplies every
Euler step, with step1/32 and physical horizon128. Validation chooses among
checkpoints16,32,64,128 independently for each fit. Test data never choose
hyperparameters or checkpoints. These are finite deterministic empirical-law
experiments; fresh streaming observations are not tested here.

The field dictionary is uncentered PCA of initialized first-hidden activations,
estimated using only training inputs. Its functions remain evaluable on new
inputs from a stored initialization copy and PCA transform. Seed101 pilots
compare C8q3 and C24q1, both rank bound24, against factor corrections W0+AB of
rank24 with factor mobility0.25,1,4, and dense and fixed right-projected rank24
descent. The factor initialization is A=0 and B_ij~N(0,1/24). All retain the
same base Gaussian matrix; all evolve the first layer and readout.

Validation selects C8q3 for fashion/housing and C24q1 for HAR, with factor
mobilities0.25,4,4 respectively. The exact choice is preserved in
[STAGE2_INDEX_SELECTION.json](STAGE2_INDEX_SELECTION.json). Confirmation uses
new seeds201–204. Time64 subspace drift exceeds0.2 on fashion and HAR, firing
the preregistered adaptation branch: Procrustes-align a current-feature PCA
basis and either transport moments by overlap or replace only future source
indices. Both variants are run on every domain and confirmation seed.

## Held-out results

Median validation-selected test RMSE over four confirmation seeds:

| Learner | Fashion | HAR | Housing |
|---|---:|---:|---:|
| Fixed input field |0.671693|0.064411|0.318971|
| Retrospective overlap transport |0.671693|0.064221|0.318528|
| Write-time replacement |0.671693|0.063926|0.318486|
| Tuned rank24 factors |0.680942|0.047440|0.316133|
| Fixed right-projected rank24 |0.681459|0.065011|0.317891|
| Dense canonical flow |0.677509|0.063961|0.316212|

The primary metric is the median **paired** ratio of field RMSE to factor
RMSE, not the ratio of the two table medians. Fixed-field ratios are0.9883,
1.3789,1.0079 on fashion,HAR,housing. It wins3/4,0/4,1/4 individual seeds.
The practical gate required at least5% improvement on two domains, no more
than5% worsening on the third, and at least3/4 wins on passing domains.
No field variant reaches5% improvement on even one domain. The fixed,
transported, and write-time candidates all fail.

Both adaptive variants select the pre-refresh time64 checkpoint on every
fashion seed. Their fashion median is therefore not evidence that adapting
the dictionary helped. On HAR and housing they make small changes, leaving
their factor ratios at approximately1.37 and1.006. Fixed fields show genuine
hidden activation motion (for example, median first/second-layer RMS changes
0.411/0.409 on fashion), but feature movement does not establish a practical
advantage or identify a unique mechanism.

![All confirmation seeds and frozen factor comparisons](../../data/generated/response_memory_use_cases_20261001/stage2_index_analysis_v1/stage2_index_comparison.png)

## Missing history has a direct functional effect

After the original campaign, root authorized three additional **diagnostic**
float64 replays, charged to its separate budget. Each repeats the selected
seed101 field through time64 while a full sample-indexed observer records the
same forward/backward histories. The observer never feeds the learner.
At the frozen endpoint, compare three represented matrices while fixing the
outer weights: original fixed dictionary; overlap-transported old moments;
exact retrospective new-basis moments computed from the observer.

| Diagnostic at time64 | Fashion | HAR | Housing |
|---|---:|---:|---:|
| Relative backward-moment transport error |0.9978|0.3169|0.2772|
| Relative correction-matrix transport error |1.0024|0.2008|0.4017|
| Test prediction RMS: overlap versus exact reindexing |1.08847|0.03093|0.11064|
| Original test target RMSE |0.67417|0.07901|0.32841|
| Overlap-transported test target RMSE |0.67587|0.07986|0.32865|
| Exactly reindexed test target RMSE |1.30742|0.07758|0.34350|

These discrepancies survive calibration: original float32/float64 prediction
RMS differs by at most2.06e-7, and old observer moments agree with field moments
to at most3.13e-15 relative error. Thus the discarded history is functionally
material in these frozen-state interventions. Exact retrospective reindexing
is not necessarily a good intervention: it sharply worsens fashion and
worsens housing while slightly improving HAR. A current-feature PCA basis
optimizes current activation variance, not historical paired interactions or
current loss after a history rewrite. This diagnostic does not train with
oracle history and does not supply an algorithmic improvement claim.

## Numerical validity and resources

All99 fits have complete finite final states. Each GPU stage checks eager
versus captured updates for all four learner classes; every observed error
is exactly zero. TF32 is disabled and CPU threads are fixed to one.
The18 float64 deterministic/autograd checks pass with maximum error2.78e-15.
They independently verify canonical mobilities and loss gradients, adaptive
projection equality, write-time orthogonality and product-tail cancellation,
rotation-induced loss of zeroth moments, and overlap-transport error.
An additional no-training audit checks all 30 actual float32 PCA dictionaries
across domains, seeds and candidate ranks: maximum Gram error is 1.073e-6,
below the declared 1e-5 gate; the smallest selected eigenvalue ratio is
0.00223, above the 1e-8 cutoff. Data hashes, unit row norms, finite values
and HAR subject separation also pass. Evidence is in
stage2_index_data_checks_v1/checks.json and its flat generation source.

Halving the step on the selected field and factors at seed201 on all three
domains changes selected target RMSE by at most1.16e-5. All selected times
remain unchanged; all changes are below1% of label RMS and one-third of the
paired field/factor gap. No numerical gate blocks the negative practical
result. The adaptive branches themselves have no additional step refinement;
no positive claim depends on their tiny differences.

The99 fit loops, captures and evaluations sum to72.994seconds. The three
separately authorized float64 diagnostics sum to12.914seconds. These are
logged in-function runtimes, excluding interpreter/CUDA startup; they are
not a hardware-normalized benchmark. No failed or excluded fit is hidden.

Storage includes the common evolving first weights and readout. On fashion,
the fixed field has106753moving scalars,16384fixed base scalars and101512fixed
dictionary scalars, before its8192-entry cached training basis. Dense has
116992moving scalars and no fixed base copy. Factors have106752moving scalars
plus16384fixed base scalars. On housing, corresponding field counts are7425
moving,16384base,2184dictionary and8192cached basis; dense has17664moving.
The additional initial first-layer copy makes the dictionary especially costly
in high input dimension. The field's learned hidden state is smaller, but its
**total retained state is larger** than dense and conventional factors here.
Median fashion fit runtimes are0.989s field,0.751s factors and0.581s dense.
No storage or speed advantage is demonstrated.

## Claim state and remaining limits

| Claim | Current status |
|---|---|
| Current-feature orthonormal indexing equals right-projected gradient | Exact, proof and independent numeric check |
| Arbitrary-history lossless retrospective reindexing requires span containment | Proved for the stated finite-coefficient representation |
| Write-time indexing retains orthogonal joint projection and product-tail identity | Exact under pointwise input orthonormality |
| An unchanged span guarantees unchanged low-order write-time memory quality | False; explicit rotating-basis counterexample |
| Overlap transport retains practically irrelevant omitted history | Contradicted by three calibrated frozen-state functional diagnostics |
| Exact current-feature reindexing must improve loss | Contradicted by fashion/housing interventions |
| Tested fixed/adaptive learners give >=5% cross-domain gains over tuned factors | Failed preregistered criterion |
| General adaptive indexing cannot be useful | Open; not implied by these results |
| Dense/population/all-time tracking for adaptive indexing | Open; no theorem transferred |

PCA, subspace transport, projected gradient and low-rank factors are existing
ideas. The theory file links the limited primary-literature positioning to
LoRA, GaLore and dynamical low-rank integration; no comprehensive priority
claim is made. A future constructive route would need to control temporal
basis motion together with both response histories, rather than optimize
current forward covariance alone. This report authorizes no new search.

## Sources, evidence and reproduction

Scientific source scope: this study's complete model reconciliation,
input-field derivation/report/normalization and input-field implementation;
the current paper's setting, complete learning-speed and joint-clock
constructions/proofs, all-time results statements, finite-time statement,
resource comparison and sphere appendix; maintained docs index/notation;
the baseline implementation's network, source Flow, factor and training
classes; root's frozen stage2 data contract/manifest; required skills and
the explicitly linked external primary abstracts. The unused baseline
dictionary machinery and manuscript population proofs are not imported
dependencies. No archived book or other study supplied scientific inputs.
Root supplied its independently derived fixed-projector descent criterion
after the initial proposal; that contribution is disclosed in the theory
file and is not claimed as independently rediscovered here. No other route's
experiment outcomes were used. No maintained manuscript/API or Git state was
edited.

Generated evidence is under this study's namespace in stage2_index_pilot_v1,
stage2_index_confirm_v1, stage2_index_adapt_v1, stage2_index_refine_v1,
stage2_index_oracle_v1, stage2_index_checks_v1 and stage2_index_analysis_v1.
Each training directory contains exact source/protocol snapshots, hashes,
command/environment, per-fit configurations/results, and raw predictions.
The source code, proofs, selected configuration and report remain flat in the
study. All results are study findings; none are promoted established material.

From the repository root, with a fresh output path for each invocation:

```bash
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_checks.py --out FRESH_CHECKS
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_experiment.py --data data/generated/response_memory_use_cases_20261001/stage2_data01 --out FRESH_PILOT --stage pilot --device cuda:0
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_experiment.py --data data/generated/response_memory_use_cases_20261001/stage2_data01 --out FRESH_CONFIRM --stage confirm --selection studies/response_memory_use_cases_20261001/STAGE2_INDEX_SELECTION.json --device cuda:0
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_experiment.py --data data/generated/response_memory_use_cases_20261001/stage2_data01 --out FRESH_ADAPT --stage adapt --selection studies/response_memory_use_cases_20261001/STAGE2_INDEX_SELECTION.json --device cuda:0
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_experiment.py --data data/generated/response_memory_use_cases_20261001/stage2_data01 --out FRESH_REFINE --stage refine --selection studies/response_memory_use_cases_20261001/STAGE2_INDEX_SELECTION.json --device cuda:0
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_oracle.py --data data/generated/response_memory_use_cases_20261001/stage2_data01 --pilot FRESH_PILOT --selection studies/response_memory_use_cases_20261001/STAGE2_INDEX_SELECTION.json --out FRESH_ORACLE
```

The analysis command is stored in the analysis source and consumes the named
v1 directories. Its JSON summary contains every seed, gate and refinement,
not only table medians. Independent review remains separate from this
author-side verification.
