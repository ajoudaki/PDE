# Width-1024 closure versus parameter-matched exact networks

This user-authorized addition continues the existing finite-dictionary
approximation investigation with a new matched control. It does not reopen
earlier conditional stages. The user explicitly requested both parameter
matches after the distinction between trained and fixed scalars was explained.
No established code or theory is changed.

## Scientific design, fixed before implementation and training

Compare the constructed dictionary at n=1024, p=1,3,5 with ordinary smaller
equal-width, bias-free two-hidden-layer tanh networks. Use the existing
`quadrant_alternating` and `two_outliers_alternating` geometries from
`diverse_cases.py`: tight alternating labels and alternating labels plus two
outliers. These are selected for geometric/sign complexity, not for new
comparison outcomes. They are previously studied cases, not independent
problem-family replicates. The optional case-choice question was unanswered
when this scope was fixed; its recommended two-case scope is used.

One common full width-1024 network per case and numerical level is the target.
The network seed is 20260920. Use the unchanged canonical initialization,
actual finite random readout, all trainable blocks, unhalved training MSE,
and physical gradient-flow mobilities (width,1,width). Smaller networks use
their own width in initialization, readout normalization and mobilities.
The existing finite-carrier dictionary construction uses only full-network
initialization, retains all nominal columns, and uses the original ridge.
No target trajectory, trained features, labels or endpoint enter initialization.

### Two distinct parameter matches

With n population rows and dictionary dimensions K1,K2, the closure trains
w[n,2], c[n] and M[K2,K1]. Its nominal trained coefficient count is

    P_train = 3n + K1*K2.

Its minimal retained prediction/evolution representation additionally stores
the frozen dictionaries B1[n,K1], B2[n,K2]:

    P_total = n*(K1+K2) + 3n + K1*K2.

Uniform quadrature weights are implicit. Diagnostic initial copies g,D,
duplicate contraction caches, solver workspace and the temporary full initial
matrix are not model parameters. Actual engine retained bytes are recorded
separately. No seed compression is credited to either model. The p5 redundant
constant columns remain counted; no numerical rank threshold changes a budget.

An ordinary width-m network has P_net=m*m+3m parameters, all trained. For each
budget select the smallest integer m with P_net >= P_budget, independent of
outcome. Thus rounding slightly favors the comparator. The user's sqrt(n*K)
estimate is the leading dictionary-storage term of the total-size match.

| p | K1,K2 | P_train | matched m | P_net | P_total | matched m | P_net |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 5,3 | 3087 | 55 | 3190 | 11279 | 105 | 11340 |
| 3 | 35,10 | 3422 | 58 | 3538 | 49502 | 221 | 49504 |
| 5 | 128,21 | 5760 | 75 | 5850 | 158336 | 397 | 158800 |

Keep both small-network controls separate. Do not report their minimum,
select the better control after fitting, or reinterpret total size as trainables.

### Initialization coupling

For each fixed smaller width m, take the first m neuron indices in each layer
of the full network's initial arrays, with the canonical rescaling:

    W1_m = W1_n[:m]
    W2_m = sqrt(n/m) * W2_n[:m,:m]
    c_m  = (n/m) * c_n[:m].

This gives the exact canonical marginal independent Gaussian block law at m,
coupled to the reference without selecting neurons or seeds. It does not make
initial functions identical. Ours retains information about the full initial
realization in its frozen dictionary; the smaller network retains a fixed
subset. This is a finite-realization compression comparison, not a pure test
of hidden-feature capacity or population generalization. If a small network
fits but selects a different function, that alone does not prove it lacks
enough features to represent the reference.

### Endpoint and decision

Every predictor is evaluated at its own first detected training-MSE 0.001
crossing, using the existing adaptive-Heun parameter-chord crossing rule.
The primary metric is RMS discrepancy from the full network on 8192 uniform
circle angles. Retain L1, squared RMS, sampled maximum, 4096-grid checks,
training loss/time traces, hidden motion, complete states and initial predictions.
There are no labels between the eight training inputs; this metric measures
agreement with the full network, not unseen-label risk.

For each case,p,matched-control comparison, support for the closure means
strictly lower RMS at both selected numerical levels and all validity gates
passing. The reverse ordering at both levels favors the smaller network.
Ranking reversal or a failed gate is inconclusive. Report absolute errors,
ratios and all failures without an arbitrary effect-size cutoff. Increasing
p and the two budget definitions remain separate descriptive comparisons.
No asymptotic rate, universal superiority or capacity lower bound is inferred.

## Numerical checks and predeclared branches

Base tolerances are (rtol,atol)=(6.25e-5,6.25e-7) and
(1.5625e-5,1.5625e-7), with CUDA float64 throughout scientific calculations.
Reuse the maintained engines and existing adaptive integrator: initial step
0.05, maximum step2, minimum step1e-7, no increasing accepted loss,
physical time10000, 30000 accepted steps, 180 seconds per trajectory.

Before training check parameter counts, prefix/rescaling identities, canonical
width normalization and gradients, zero initial hidden-displacement diagnostics,
full-basis closure/network equivalence, and the initialized dictionary algebra.
Afterward independently replay all initial/final predictions and training losses
(absolute tolerance1e-10); verify source/configuration hashes, grids, fitting,
actual shapes/counts/coupling, Gram ridge condition <=1e10, triangular residual
<=1e-8, finite arrays and the two-resolution endpoint maximum discrepancy <=0.01.
Report nested8192/4096 metric changes. Refinement agreement is an operational
check, not a rigorous bound on exact-flow error.

Only fitted cells with endpoint refinement discrepancy >0.01 qualify for
numerical resolution runs. Each new level divides rtol/atol by4, up to two
extra levels per cell, at most12 extra trajectories in total. Visit literal
case order, then full followed by p1,p3,p5 and ours/trainable/total control
order, first completing all eligible first extras before eligible second extras.
Select the latest two available levels, retain every previous attempt.
No extra seed, geometry, width, loss target or favorable-outcome search.
Unresolved cells stay visible and marked after this bounded branch ends.

## Resource bounds and terminal stop

Base scope: 2 cases * (1 full + 3 orders * 3 methods) * 2 levels =40 trajectories.
At most52 new trajectories including resolution. Prior scaling/width4096 work
spent2894.574399381876 of6000 summed training-worker seconds, leaving
3105.425600618124. Reserve four600-second base workers (one case per worker)
and at most600 additional worker seconds for the numerical branch: new ceiling
3000 seconds, cumulative ceiling6000. Record actual completion times and
release unused reservations; include setup after the timer, outputs and cleanup.
Output overhead can extend a polled wall cap slightly; the unreserved105 seconds
is retained as headroom, never permission for extra scientific runs.

Use both available RTX3090 devices without modifying unrelated processes.
Stop after the base suite and eligible bounded resolution branch or when caps
are reached, regardless of which model wins. No prior endpoint is reused as a
new width1024 result. Save source/protocol hashes, exact commands, versions,
hardware, seeds, precision, raw checkpoints and all failures in fresh run roots.

## Deliverables and ownership

Study-local producer `matched_network_benchmark.py`; independent analysis and
raw replay checker; parameter-count table; separate RMS/loss plots and radial
viewer for all three model types plus the full reference. Generated products
use this study's `matched_network_*` namespace under data/generated.
Root owns this protocol, producer, README, report and sole Git writer role.
Scoped agents receive explicit source/output ownership. Internal checks do
not promote the results to established theory or maintained APIs.
