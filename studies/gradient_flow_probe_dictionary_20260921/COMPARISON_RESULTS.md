# Derivative dictionary versus the old polynomial dictionary

The new p=3 dictionary improves approximation on the paired-label task with
fewer vectors. The old dictionary is more accurate on the outlier task at every
tested order, and at p1/p2 on both tasks. These are the two retained width4096
cases; no fresh rotations or negative control was included.

## Design

Both families compress the entire middle matrix and train read-in, middle
coefficients and readout, from the same actual initialized finite network.
Tanh, width4096, circle radius sqrt(2), Gaussian initialization seed20260920,
full-batch physical gradient-flow equations, ridge rule and fixed probe scale
are shared. Adaptive simultaneous Heun integrates the equations in CUDA float64.
The new frozen vectors use initialized activation derivatives and additional
forward/backward actions, with no task labels or training inputs in construction.
The old vectors are the maintained Chebyshev dictionary.

Each model stops at its own first detected training-MSE0.001 crossing. RMS
measures its output difference from the dense network's fitted output on8192
uniform circle angles. This is approximation of that learned function; it is
not prediction error against a known target between the eight training points.
Own crossing times differ. All models fit the training labels to the threshold.

Archived dense references and oldp1/p3 runs are reused without retraining.
Oldp2 had never been run and was added. Newp1/p2/p3 and oldp2 received two
tolerance levels; a single predeclared extra numerical-resolution run was needed
for outlier newp2. Seventeen new trajectories were executed in total.

New p=0 labels the vanishing order-t increment; new p1,p2,p3 mean terms through
t²,t³,t⁴ in the middle-weight increment. Old p is polynomial total degree.
The empirical candidate uses the small increment-factor spans to compress the
entire middle layer; it does not claim to preserve the initialized dense
function or exactly reproduce finite-width Taylor jets. Both constructions use
the historical normalized-axis probes, as fixed in COMPARISON_PROTOCOL.md.

| p | New lower / upper vectors | Old lower / upper vectors | New / old total vectors | New / old middle entries |
|---:|---:|---:|---:|---:|
| 1 | 2 / 4 | 5 / 3 | 6 / 8 | 8 / 15 |
| 2 | 2 / 4 | 15 / 6 | 6 / 21 | 8 / 90 |
| 3 | 6 / 12 | 35 / 10 | 18 / 45 | 72 / 350 |

All empirical raw ranks equal these column counts. Every model also trains
12288 read-in/readout scalars. At p3, total trainable scalars are12360 new versus
12638 old: the large reduction concerns dictionary storage and middle entries,
not an equally large reduction in all trainable parameters. New p1 and p2 have
identical raw feature spans; their small result difference comes from the
inherited p-dependent ridge, eta=1/[1024(p+1)^2].

## Finer selected results

| Task | p | New RMS | Old RMS | Lower RMS |
|---|---:|---:|---:|---|
| Paired labels | 1 | 0.820528 | 0.266726 | Old |
| Paired labels | 2 | 0.820129 | 0.261636 | Old |
| Paired labels | 3 | 0.085701 | 0.138019 | New |
| Alternating labels with two outliers | 1 | 2.521709 | 1.098322 | Old |
| Alternating labels with two outliers | 2 | 2.533049 | 1.067914 | Old |
| Alternating labels with two outliers | 3 | 1.235899 | 0.497921 | Old |

Every displayed ordering holds at both selected numerical levels. Paired p3
has37.91% lower RMS with60% fewer dictionary vectors (18 versus45), and72
middle coefficients rather than350. Its RMS is also below the old p2 value,
despite18 versus21 vectors. The t4-derived enrichment therefore gives a concrete
finite-budget improvement on this task.

The same enrichment reduces the new dictionary's outlier error from about2.53
to1.24, but it remains worse than even oldp1 (1.10 with8 vectors). Thus this
construction does not deliver a general improvement across these two tasks.
There is no fitted asymptotic rate or claim of universal superiority. These
are finite-width, single-initialization, user-selected stress cases, and the
absolute ridge makes normalization part of the compared method.

## Validation and artifacts

The initial source/feature checks reproduce archived oldp1/p3 bases and initial
predictions, recover the same read-in/readout/dense initialization, verify the
collected derivative coefficients and all-block gradients, and pass the
conditioning/triangular gates. Preflight evidence is in `comparison_preflight02`
and `implementation_check01` under this study's generated namespace.

Final `comparison_analysis02` has12/12 valid rows. Maximum initial/final replay
discrepancy is1.6654e-14. Every selected predictor/refinement endpoint difference
is <=0.01; the largest is0.00912345 for outlier newp2. Its earlier failing pair
(0.01511448) and the original analysis remain preserved. Halving the angular
grid changes RMS by at most2.23e-16 and sampled maximum by1.26e-5. These are
numerical consistency checks, not certified exact-flow or continuum bounds.

An independently implemented checker rebuilds both dictionaries, replays all
saved snapshots, checks losses/initialization/metadata and computes errors
without importing the producer, maintained engines or main analyzer. Its initial
audit independently identified exactly the same extra-eligible cell. The final
audit passes2254 checks over29 trajectories/279 saved states and527 agreement
checks against the main analysis, with largest metric discrepancy8.88e-16.
The complete report is COMPARISON_INDEPENDENT_CHECK.md and evidence is in
`comparison_independent02`. These are internal checks, not promotion.

Generated root: `data/generated/gradient_flow_probe_dictionary_20260921/`.

- `comparison_primary01`, `comparison_refined01`, `comparison_extra01`: complete
  saved trajectories, states, frozen dictionaries, diagnostics and provenance.
- `comparison_analysis02`: metrics, selected paths/tolerances, numerical gates,
  both-level comparisons, complete endpoint fields and file/source hashes.
- `comparison_plots02`: linear-vector/log-RMS plot, log-loss versus physical time
  plots, and `radial_comparison.html` with task/order/accuracy selectors and a
  display-only radial amplitude control. Metrics are copied from the analysis.

New training consumed434.73531890287995 summed worker seconds. Under the
conservatively retained old allowance,2174.519788134843 seconds remain unused;
all reservations are released and the bounded protocol is complete. No dense
baseline training, random-control run, seed search, maintained-source edit or
Git index change was performed for this comparison.
