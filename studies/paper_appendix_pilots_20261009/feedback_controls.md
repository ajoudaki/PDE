# Conditioning and low-rank baseline checks

## Frozen bounded diagnostic

Allowed inputs are the current `paper/figures/capture_trajectory.py`, the two
explicitly assigned paper pilot studies, their generated arrays, the supplied
feedback attachment, and established notation/process instructions. No other
study supplies scientific inputs. Root owns shared notes and Git; this scoped
helper owns only the selector, its setup option, and these diagnostics.

The question is whether the three saved construction failures come from
uniform coordinate selection at the existing width. Rebuild exactly the old
source rank ladder, source seed, dense initialization and full horizon. Check
the old precursor residuals and original failed condition value first. The
only replacement is deterministic pivoted QR for a nonsingular initial row
set followed by greedy additions maximizing the determinant increase. Keep the
entire existing source span, unweighted coordinates, exact metric correction,
and condition cap 16. No source truncation, larger condition gate, extra seeds,
source fits, or selector search is allowed. There is one replacement candidate
per case at widths 512 (SiLU and 16 training examples) and 256 (dimension 64).

A construction passes only if both layers satisfy the original condition gate
and source-isometry/metric-inverse errors are below 1e-8. Run one compact Euler
fit per successful construction, using the old step 0.00625, horizon 32 and
65 recorded times, then compare with the hash-verified old dense pair. Both
endpoint RMS and maximum-recorded RMS must be at most the corresponding dense
pair values (factor 1). A completed inaccurate fit is a failure; any failed
numerical/provenance gate or timeout is inconclusive. Per source or fit cap is
120 seconds, whole queue cap 240 seconds, and at most three compact fits.
No larger-width follow-up is part of this diagnostic.

The low-rank check differentiates the actual factorized model and verifies its
induced matrix velocity. The existing trained-both-factors baseline is retained.
A fixed-orthonormal-right additive control is used only in a tiny full-rank
Euler oracle. Passing these checks establishes implementation consistency, not
the strength of untuned LoRA as a competitor or any compression theorem.

Reproduce with `/home/amir/miniconda3/bin/python -B
paper/figures/capture_trajectory.py feedback-control-check` and
`/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py
feedback-conditioning --config
studies/paper_appendix_pilots_20261009/feedback_conditioning.json`.
The configured output must be fresh. Results are appended below after execution.

## Results of the fixed-width selector diagnostic

The queue finished in 47.53 seconds. All three precursor residual traces were
reproduced exactly; the recorded original failed conditions were reproduced
within 2e-8. No dense Euler reference or partner fit was repeated; each original
full-horizon source construction was rebuilt once. The deterministic replacement
preserved source ranks 122/128 (SiLU), 130/144 (16 examples), and 118/62
(dimension 64). Source-isometry and metric-inverse errors were below 2.2e-14.

| Case | New layer conditions | Construction | Endpoint / dense pair | Maximum / dense pair |
|---|---|---|---:|---:|
| SiLU, width 512 | 16.9901, 17.9181 | Inconclusive; cap 16 exceeded | — | — |
| 16 examples, width 512 | 12.4915, 10.7875 | Pass | 7.4877 | 8.7671 |
| Dimension 64, width 256 | 14.4985, 10.3358 | Pass | 0.67862 | 0.67862 |

The 16-example construction now works but its completed trajectory fails the
factor-one criterion. Its final training MSE is 0.001035: fitting labels and
capturing the dense trajectory remain different questions. The dimension-64
witness passes with 82,184 moving and 196,609 fixed scalars. These results
characterize one numerical selector and two finite Euler trajectories. They
do not certify the theoretical source compiler or the existence of a uniformly
accurate compressed model. The replacement is opt-in; existing configurations
retain uniform selection.

Evidence: `data/generated/paper_appendix_pilots_20261009/feedback/conditioning/`.
Its report retains full provenance, source diagnostics, both selectors' layer
conditions, and fit details. Per-case archives retain actual sources, complete
source bases, selected indices and the two completed trajectories.

## What the low-rank baseline actually optimizes

For one adapted layer, let $p$ be its input width and write
$W=W_0+UV^\top$, where $U\in\mathbb R^{n\times r}$ and
$V\in\mathbb R^{p\times r}$. The frozen $W_0$ equals the dense initialization.
Both factors evolve. The network has two tanh hidden layers, zero initial
readout, forward maps $h_a^{(1)}=\tanh(W^{(1)}x_a)$ and
$h_a^{(2)}=\tanh(W^{(2)}h_a^{(1)})$, and prediction
$f_a=W^{(3)\top}h_a^{(2)}/n$. The stored inputs $x_a$ already include the
normalization factor. For residuals $r_a=f_a-y_a$ and loss
$\mathcal L=m^{-1}\sum_a r_a^2$, put $G=\partial\mathcal L/\partial W$.
With common factor mobility $\mu$, the chain rule gives

$$
\dot U=-\mu GV,\qquad \dot V=-\mu G^\top U,\qquad
\dot W=-\mu(GVV^\top+UU^\top G).
$$

For the first matrix, $p=d$ and $\mu=nd/r$; for the hidden matrix, $p=n$ and
$\mu=n/r$. The dense block mobilities are respectively $n$ and $1$; the
readout mobility is $n$ in both models. Initially $U=0$ and $V$ has orthonormal
columns sampled uniformly. Thus $\mathbb E[VV^\top]=(r/p)I$ makes
the expected initial induced block velocity equal to the dense velocity.
With $n\ge d$ and full ranks $r=d$ and $r=n$, the initial equality is exact. After
training, $VV^\top$ and $UU^\top$ evolve; the induced matrix metric generally differs
from the dense metric. A later full-rank trajectory mismatch is therefore not
an implementation error. At finite Euler step there is additionally the
usual step-squared product of simultaneous factor increments.

The deterministic float64 check uses n=12, d=3, m=5. Automatic differentiation
matches the implemented factor velocities to 8.33e-17; the induced-metric
identities match to 2.78e-17. A nonzero-readout probe makes the initial full-rank
block comparison nonvacuous and matches to 5.56e-17. Over 32 Euler steps of
size 0.04 from the original zero-readout initialization, a separate additive
oracle with fixed full orthonormal right factors matches dense weights to
8.89e-16. The actual trained-both-factors baseline differs in prediction by
1.6792e-5, as its different equations permit. No baseline equation changed.
These tests do not establish that the baseline is optimally tuned.

## Leading arithmetic behind the cost table

Here n is dense width, d input dimension, m training count, q Legendre order,
and k the common compact width. Count one scalar multiplication followed by
accumulation as one MAC. Only a training RHS/Euler update is counted; source
setup, observations, passive queries, storage copies, synchronization and
pointwise nonlinearities are excluded. The lower terms stated below are not
timing predictions.

Dense uses three n-by-n matrix products with m columns (forward, backward,
hidden update) and two first-layer products, giving 3n^2m+2ndm+O(nm).
Legendre uses two frozen-mixer products and four applications of rank-qm
factors, giving 2n^2m+8qnm^2+2ndm+O(qnm+nm). Moment transport uses cumulative
sums, not a quadratic-in-q matrix multiplication.

The metric compact runtime uses ten k-by-k products with m columns, two
first-layer products, five k-contracted sample-Gram products and one input
Gram. Its count is 10k^2m+2kdm+5km^2+dm^2+O(k^2+km+m^3), where the final
term includes the m-by-m Cholesky or spectral solve. Both Harmonic and
Logarithmic call this runtime. The actual fields, backward, RHS, readout and
Legendre transport methods were compared by Python AST against the saved
circle-n4096 source snapshot and agree exactly; concurrent Euler fusion
changes allocations/rounding but does not remove these contractions.

## Authorized follow-up branch, frozen before execution

After the fixed-width results, root authorized exactly one SiLU width-768
candidate at source rank 37 with the same selector and condition cap, and one
16-example width-512 half-step run at step 0.003125. Both use the saved source
arrays without a new source rollout. No further branches are authorized.
The follow-up GPU queue has a total cap of 120 seconds.

For the half-step check, compare the coarse/fine compact difference on the
same recorded grid to the old dense-pair endpoint and maximum RMS. Both ratios
must be at most 0.1 to classify the original compact Euler error as small
relative to that benchmark. Also record the fine-compact versus coarse-dense
ratio explicitly as a mixed-step diagnostic, not a gradient-flow certificate.

The follow-up queue finished in 51.87 seconds with no source rollouts. The
SiLU width-768 candidate has layer conditions 9.36797 and 8.63393, so it builds
without relaxing the gate. It retains 592,136 moving plus 1,769,473 fixed
scalars and finishes the old Euler grid. Endpoint and maximum-recorded errors
are respectively 1.35382 and 0.44550 times the old dense pair. The endpoint
criterion still fails; no further selector or width was tried.

The 16-example half-step run used the same source arrays and exactly matching
compiled-model diagnostics. The geometry constructor and selector ASTs were
also compared against the preceding run's frozen executable and matched.
Its common-grid compact coarse/fine discrepancies are 0.0207458 endpoint RMS
and 0.119381 maximum RMS, equal to 3.12895 and 6.51951 times the old dense-pair
benchmark. Both exceed the predeclared 0.1 numerical gate substantially.
The fine-compact versus coarse-dense comparison is 4.99665 at the endpoint
and 2.63046 for the maximum. These last ratios are explicitly mixed-step
diagnostics, not a refined comparison to gradient flow.

Consequently the original 16-example finite-Euler mismatch remains recorded,
but its attribution to intrinsic approximation error is **inconclusive**:
discretization sensitivity is too large on the relevant scale. A conditionally
well-posed construction does not establish a stable numerical trajectory.
No further refinement or source change was run. The dimension-64 factor-one
pass and SiLU endpoint failure likewise remain finite-grid, single-seed claims;
neither received a refinement certificate here.

Evidence is in `data/generated/paper_appendix_pilots_20261009/feedback/conditioning_followup/`.
Reproduce with `/home/amir/miniconda3/bin/python -B
paper/figures/capture_trajectory.py feedback-conditioning-followup --config
studies/paper_appendix_pilots_20261009/feedback_conditioning_followup.json`,
using a fresh output directory and the preceding cached sources. Root may now
update the study README; no additional controls/conditioning runs are pending.
