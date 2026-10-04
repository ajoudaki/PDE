# Current-correlation saved-endpoint diagnostic

## Frozen protocol, before implementation or evaluation

2026-09-30. This diagnostic evaluates exactly the three existing width-1024,
seed-1 Gaussian endpoints `near_pair_sin9`, `cluster_triple_cos9`, and
`cluster_triple_cos1`, at their own saved MSE 0.001 stopping times. It reads
only the assigned study reports/code and these saved NPZ/JSON inputs under
`all_tasks_j2_20260927/references`. No training, fitting, parameter selection,
other study, or sibling route is allowed. The smooth cluster is the fixed
same-input, different-label control. Endpoints are not at a common time.

Decision: distinguish a current readout-energy signal from joint second-layer
gate geometry and readout/gate correlation, while separately measuring the
first-layer tangent contribution. These are endpoint comparisons, not a
causal decomposition of training trajectories or a test of closure convergence.

Write averages over width as `<.>`. With current second features `h_a`, gates
`d_a=1-h_a^2`, and readout `c`, evaluate `q=<c^2>`, `K_ab=<h_a h_b>`,
`G_ab=<d_a d_b>`, and `D_ab=<c^2 d_a d_b>`. Compare the naive factor
`q <d_a><d_b>` with the stronger independent-readout factor `q G_ab`.
The former discards gate covariance and readout/gate correlation; the latter
discards only the correlation between `c^2` and `d_a d_b`. Both use exact
current marginals, so failure cannot be blamed on inaccurate marginals.

Primary metrics are relative Frobenius errors of both factors against `D`,
and their signed/absolute relative errors after contraction against the unit
current residual and the unit weakest eigenvector of the initial feature Gram.
Also retain full matrices, diagonals, unnormalized residual contractions,
the empirical spread/effective fraction of `c^2`, and exact readout, middle,
and first-layer tangent blocks. Middle blocks equal `D_ab <h1_a h1_b>`;
the first block uses the exact current `W^T(c d_a)` response. Relative errors
use the exact nonzero quantity as denominator; zero denominators are reported
as null. Absolute errors remain available near weak denominators.

Competing explanations: if the independent-readout factor is small-error but
the naive factor is large-error, joint gate geometry is necessary at these
states. Large independent-readout error instead identifies a readout/gate
association remaining after exact gate geometry is supplied. First-layer
fractions measure what a middle-only response omits. Descriptive error bands
are fixed at `<0.1` small, `>0.5` large, otherwise intermediate/inconclusive;
none is a trajectory-causality or asymptotic-concentration threshold.

If the same one-pass budget permits, evaluate the exact instantaneous `Ddot`
using the canonical dense RHS, decomposing readout, middle-gate and first-gate
terms. Check against one central difference per saved state, with
`epsilon=1e-5/max(1, rms(wdot), ||Wdot||_F/sqrt(n), rms(cdot))`.
This perturbs the current state along its exact RHS without integrating it.
Also report derivatives of both factor formulas using exact current moment
derivatives, explicitly without interpreting these as autonomous closures.

Validity gates: float64; one BLAS thread set before NumPy import; finite
arrays; exact task input/label replay for tasks defined in the assigned
`circle_tasks.py` (the smooth cluster uses its saved definition); dense saved
train and 256-circle prediction replay below `1e-10` absolute; training MSE
replay below `1e-12`; `mean(d_a)=1-K_aa` below `1e-12`; full tangent/RHS
identity below `1e-10` relative; central-difference `Ddot` below `1e-6`
relative. Failed gates invalidate associated interpretations and are retained.

Hard budget: at most 30 seconds cumulative data reads and numerical endpoint
evaluation, one pass through exactly three saved endpoints, one BLAS thread,
no tuning and no repeat except to repair a documented implementation bug.
The script stops numerical work at 25 seconds and has a 28-second alarm.
Terminal condition is completion of the three endpoints or the deadline.
No scientific follow-up experiment is authorized by any outcome.

Outputs: this report, `current_correlation_diagnostic.py`, and fresh
`data/generated/structured_full_rank_scalar_20260926/current_correlation_20260930/diagnostic/`.
Hash every used source and input, snapshot used sources, and retain raw
results and negative evidence. Input snapshots are represented by their
immutable full-file hashes and saved-state metadata; originals are unchanged.

## Results

**Current readout energy and current feature Gram do not give an accurate
universal gate factorization on these saved states.** Exact joint gate
geometry helps the hard cluster's weak initial direction, but does not
consistently repair the factorization. The independent-readout factor has
large errors for the near pair and smooth cluster, where readout energy is
negatively associated with squared second-layer gates. The exact first-layer
response contributes substantially in both tested directions and is especially
important in the smooth cluster's weakest initial mode. These observations
separate different omitted quantities; they do not identify the cause of
the earlier scalar trajectory errors.

The single pass evaluated all three endpoints in 0.2421 seconds. No training,
fitting, numerical rerun, or implementation repair occurred. Every numerical
validity gate passed. The states are at their own saved stopping times:
8.3386, 28.6918, and 3.4246, respectively, with replayed MSE 0.001.

### Exact current identities

Use row index `j` for second-layer neurons and index `i` for first-layer
neurons. The exact quantities evaluated here are

\[
h^1_{ia}=\tanh(w_i\cdot x_a),\quad
h_{ja}=\tanh\Big(\sum_i W_{ji}h^1_{ia}\Big),\quad
e_{ia}=1-(h^1_{ia})^2,\quad d_{ja}=1-h_{ja}^2.
\]

With `H_ab=<h1_a h1_b>`, define

\[
b_{ia}=\sum_jW_{ji}c_jd_{ja},\qquad
F_{ab}=(x_a\cdot x_b)\frac1n\sum_i e_{ia}b_{ia}e_{ib}b_{ib}.
\]

The exact canonical tangent kernel is

\[
T=K+F+H\odot D,
\qquad \dot f=-\alpha Tr,\quad\alpha=2/m,
\]

where `F` is the first-layer block and `H⊙D` is the middle-layer block.
The symbol `K` in this report always denotes the **current second-feature
Gram**, not the full tangent kernel. The naive approximation uses only its
diagonal because

\[
\mu_a=\langle d_a\rangle=1-K_{aa},\qquad
D^{\rm naive}_{ab}=q(1-K_{aa})(1-K_{bb}).
\]

The two omitted covariances separate exactly:

\[
D-D^{\rm naive}
=\underbrace{D-qG}_{\operatorname{Cov}(c^2,d_ad_b)}
+q\underbrace{(G-\mu\mu^\top)}_{\operatorname{Cov}(d_a,d_b)}.
\]

Thus restoring `G` removes the second term but need not decrease total error:
the two omitted terms can partially cancel. This is visible in all three
Frobenius comparisons below. It is preserved as negative evidence against
a blanket claim that joint gate geometry alone repairs the approximation.

### Energy, diagonal values, and matrix errors

Vectors below preserve saved training-input order. Full matrices, diagonal
absolute/relative errors, and all contractions are in `diagnostic.json`.

| Task | q | diag K | diag D | diag naive factor | diag independent-readout factor |
|---|---:|---|---|---|---|
| near_pair_sin9 | 3.8837 | (0.3229, 0.3222) | (1.0387, 1.0339) | (1.7808, 1.7840) | (1.9692, 1.9799) |
| cluster_triple_cos9 | 8.8887 | (0.3672, 0.4154, 0.3491) | (4.0156, 3.0010, 4.2370) | (3.5596, 3.0383, 3.7655) | (4.3370, 3.7462, 4.5200) |
| cluster_triple_cos1 | 1.7480 | (0.5098, 0.5365, 0.5121) | (0.2247, 0.1795, 0.2250) | (0.4200, 0.3755, 0.4162) | (0.5539, 0.5054, 0.5444) |

| Task | D naive rel. Frobenius error | D independent-readout rel. Frobenius error | Middle naive error | Middle independent-readout error |
|---|---:|---:|---:|---:|
| near_pair_sin9 | 0.7492 | 0.8987 | 0.7301 | 0.9030 |
| cluster_triple_cos9 | 0.0775 | 0.1197 | 0.0808 | 0.1297 |
| cluster_triple_cos1 | 1.0070 | 1.5972 | 1.0028 | 1.6001 |

The naive matrix approximation is in the preregistered small-error band only
for the hard cluster. Its stronger comparator is intermediate there; both
approximations are in the large-error band for the other two states. In every
task, every diagonal entry of `D-qG` is negative. Their vectors are
(-0.9305, -0.9460), (-0.3214, -0.7452, -0.2830), and
(-0.3292, -0.3258, -0.3194). Readout energy preferentially occupies neurons
with smaller squared gates, in the precise empirical covariance sense.
This is an association at the saved state, not a direction of causation.

The coefficients of variation of `c^2` are 1.2276, 1.5287, and 0.7641;
the participation fractions `q^2/<c^4>` are 0.3989, 0.2997, and 0.6313.
These are spatial spread diagnostics for one realized width, not estimates
of variance of `q` across seeds and not a test of a width-limit concentration
theorem. A large or well-concentrated scalar `q` would not imply independence
of `c^2` and the gates.

### Directional evidence

`r` denotes the unit current residual; `v0` is the unit weakest eigenvector
of the initial feature Gram. Direction signs do not affect contractions.
The raw, unnormalized residual contractions are also saved.

| Task / direction | exact vᵀDv | naive vᵀDv | independent-readout vᵀDv | naive relative error | independent relative error |
|---|---:|---:|---:|---:|---:|
| near pair / r | 0.034751 | 0.000107 | 0.079969 | 0.9969 | 1.3012 |
| near pair / v0 | 0.034656 | 0.000044 | 0.079967 | 0.9987 | 1.3075 |
| hard cluster / r | 0.032132 | 0.001453 | 0.070176 | 0.9548 | 1.1840 |
| hard cluster / v0 | 0.139797 | 0.064829 | 0.132094 | 0.5363 | 0.0551 |
| smooth cluster / r | 0.452715 | 0.923517 | 1.212200 | 1.0400 | 1.6776 |
| smooth cluster / v0 | 0.004480 | 0.004514 | 0.005589 | 0.0074 | 0.2474 |

The hard cluster's weak initial direction gives the precommitted contrast:
joint gates reduce a large 53.6% error to a small 5.5% error. Its residual
direction instead remains badly approximated, and the near pair and smooth
cluster show that this local success is not uniform. The smooth cluster's
naive weak-direction error is only 0.74%, despite its 100.7% Frobenius error.
Therefore neither global matrix norms nor a single weak-direction success
can classify all of the relevant contractions.

The middle tangent uses the entrywise product `H⊙D`; a directional error
for `D` is not itself the same directional error for that tangent block.
For example, the hard cluster's naive middle block has only 4.7% residual
error and 15.4% weak-direction error. Supplying exact joint gates increases
these to 44.0% and 26.8%. These are additional negative controls against
translating an improvement for one observable directly to the full response.

| Task / direction | readout vᵀKv | first vᵀFv | middle vᵀ(H⊙D)v | first / lower tangent | first / full tangent |
|---|---:|---:|---:|---:|---:|
| near pair / r | 0.49646 | 0.16687 | 0.17640 | 48.6% | 19.9% |
| near pair / v0 | 0.49646 | 0.16729 | 0.17637 | 48.7% | 19.9% |
| hard cluster / r | 0.29675 | 0.10571 | 0.17562 | 37.6% | 18.3% |
| hard cluster / v0 | 0.29960 | 0.14536 | 0.18683 | 43.8% | 23.0% |
| smooth cluster / r | 1.22475 | 0.10822 | 0.22855 | 32.1% | 6.9% |
| smooth cluster / v0 | 0.00114 | 0.00631 | 0.00177 | 78.1% | 68.4% |

The first/middle tangent diagonals are respectively
(2.5092, 2.5694)/(0.3203, 0.3169),
(3.6397, 1.9080, 3.8755)/(2.3313, 1.7629, 2.4574), and
(0.0860, 0.0388, 0.0873)/(0.1137, 0.0953, 0.1140).
Large first-layer diagonals on the near pair coexist with much smaller
first-layer fractions in the residual and weak directions. Keeping these
directional distinctions prevents a misleading claim of uniform first-layer
dominance.

### Instantaneous evolution requires additional correlations

Let `z_a=W h1_a`. Exact differentiation gives

\[
\dot D_{ab}
=2\langle c\dot c\,d_ad_b\rangle
-2\langle c^2d_ad_b(h_a\dot z_a+h_b\dot z_b)\rangle,
\]

\[
\dot c=-\alpha\sum_s r_s h_s,\qquad
\dot z_a=\underbrace{\dot W h^1_a}_{\text{middle gate motion}}
 +\underbrace{W(e_a\odot(\dot w x_a))}_{\text{first gate motion}}.
\]

In particular the readout term uses `<c h_s d_a d_b>`. The middle-gate
velocity is `zdot_middle,a=-alpha sum_s r_s c d_s H_sa`, so its substitution
introduces moments such as `<c^3 d_a d_b h_a d_s>`. The first-gate term
additionally carries the current `W`-dependent backpropagated responses.
These exact formulas expose quantities not explicitly retained in the
proposed `(q,K)` factorization. This is a dependency statement; no
nonidentifiability theorem or impossibility of a larger finite closure is
claimed.

| Task | ||Ddot||F | ||readout term||F | ||middle-gate term||F | ||first-gate term||F | naive derivative rel. error | independent derivative rel. error |
|---|---:|---:|---:|---:|---:|---:|
| near_pair_sin9 | 0.007818 | 0.070367 | 0.031145 | 0.031462 | 7.0556 | 9.1586 |
| cluster_triple_cos9 | 0.060216 | 0.154620 | 0.060294 | 0.052810 | 0.7711 | 1.1088 |
| cluster_triple_cos1 | 0.008924 | 0.041528 | 0.022610 | 0.010033 | 1.5010 | 3.8323 |

The derivative comparator differentiates each factor using **exact current
marginal derivatives**. It is an optimistic instantaneous test, not a
closed evolution law. Even the hard cluster's 7.7% naive state-matrix error
coexists with 77.1% derivative error. On the near pair, readout growth and
gate motion substantially cancel; the large relative derivative error has
exact norm 0.007818 as denominator and absolute errors 0.055159/0.071600.
Both absolute and relative quantities are retained so a small denominator
cannot silently drive the conclusion.

The first-gate derivative term need not have the sign of its diagonal
entries after contraction: on the near pair its weak-direction contraction
is +0.000232 while its diagonal entries are negative. The saved matrices
retain this sign information. No positivity assumption on a time derivative
was used.

### Validity, provenance, and claim limits

All saved train and circle predictions and training MSEs replayed exactly.
All NPZ hashes match their saved JSON hashes. The gate identity error is at
most 8.89e-16; the full tangent/RHS relative discrepancy is at most 2.94e-15.
One central difference per endpoint checked `Ddot` with relative errors
2.27e-9, 1.79e-9, and 1.03e-9, below the frozen 1e-6 gate. The finite
differences perturb the same saved states along the exact RHS and do not
advance or retrain a model.

`diagnostic/diagnostic.json` contains source/input SHA256 hashes, environment,
full current matrices, both residual normalizations, weak directions,
derivatives, and all replay gates. `diagnostic/source_snapshot/` preserves
the exact source files and the pre-evaluation version of this protocol;
the protocol hash therefore intentionally differs from this appended report.
There were no exclusions, failed gates, or discarded numerical attempts.

Established here: the finite-state algebra and the reported numerical
contractions at three preserved endpoints. Disfavored: using current `q`
and marginal gates as a uniformly accurate substitute for `D`, or using
exact joint gates as a sufficient universal repair. Supported locally:
joint gates matter for the hard cluster's weak initial direction, and the
first-layer response is material in the tested tangent directions. Open:
trajectory causality, the time of first failure, approximation by a richer
autonomous closure, width-limit concentration, and hierarchy convergence.
The completed pass authorizes no further experiment.
