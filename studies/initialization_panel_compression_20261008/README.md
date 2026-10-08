# Initialization-only finite-panel compression

## Contract and source scope

This new theoretical study follows the user's request to complete the analysis
of the empirically successful metric/source compression, permit construction
at q<m, and obtain an explicit dense-variability comparison with logarithmic
width dependence. It is distinct from the closed unseen-input experiment
campaign. The follow-up request now authorizes the bounded rank-safe test below;
no broad campaign, paper promotion or empirical retuning is authorized.

The target is the canonical finite Gaussian network and nonlinear gradient
flow in the current paper: fixed hidden depth L, first entries N(0,1), hidden
entries N(0,1/n), zero readout, MSE loss and mobilities (n,1,...,1,n), strip
analytic activations with bounded derivative but possibly unbounded values,
positive unweighted initial feature-Gram gap gamma, and the existing small
fixed label allowance. There are m training inputs and p additional passive
inputs declared at initialization; passive labels never enter setup or flow.
Track the complete physical-time trajectory and fitted limit on this panel.
Do not silently replace a whole-sphere benchmark by a panel quantile, or a
coupled realization by an independent reference.

Required outputs: a construction defined even at q<m; rigorous storage and
error dependencies on n,m,p,d,gamma,L,beta (and confidence/label scale where
needed); exact provenance of coefficients; initialization-only jet existence
separate from practical setup work and from global-trajectory distillation.
A full rollout is not relabelled as a cheap initialization-only algorithm
merely because an ODE is determined by its initial state. All fixed matrices,
data, residual state and temporary costs must be accounted for. No log^5 n
accuracy claim follows from prescribing the empirical q law alone.

Allowed scientific inputs are the user-referenced paper and its capture
implementation, established docs/code, and (explicit user approval in this
turn) directly relevant proofs in finite_panel_absolute_compression_20261005
and integrated_general_compression_20261004. Those proofs require fresh checks;
their prior conclusions are not premises by reputation. No other study is an
input. Generated checks belong to data/generated/initialization_panel_compression_20261008/.

## Work and ownership

Lead: source reconciliation, complete integrated argument and this README.
Scoped routes own separate flat proof notes: OPTIMIZER.md (q<m construction),
PANEL_BOUND.md (source rank and storage), INITIALIZATION.md (jets and setup).
They do not read each other's drafts during the initial round. Route claims
remain candidates until reconstruction and adversarial checks; unresolved
implications are recorded explicitly. The initial theoretical round left shared
paper/code and earlier studies unchanged; the explicitly authorized follow-up
edits only the capture executable. The lead is the only Git writer.

## Starting point

- Empirical runtime: uses a positive-definite m-by-m readout Gram and rejects
  q<m. Its sources come from a disposable full-interval dense RK4 rollout.
- Prescribing q proportional to log(en)^(5/2) gives a logarithmic inventory,
  not a theorem that its source approximation attains dense variability.
- Target theorem, removal of the construction restriction, and efficient
  strictly initialization-only setup are open at the start of this study.

## Current result and limitations

[RESULT.md](RESULT.md) is the integrated report. Detailed arguments are in
[OPTIMIZER.md](OPTIMIZER.md), [PANEL_BOUND.md](PANEL_BOUND.md), and
[INITIALIZATION.md](INITIALIZATION.md).

- A smooth bounded spectral readout and source truncation define the corrected
  metric/deficit optimizer at every positive width, including q<m. The old
  complete-source trajectory is unchanged on its certified Gram domain. The
  construction still retains m deficits; below that domain their energy is not
  necessarily prediction loss. A fresh isolated review passed these exact
  deterministic and conditional-transfer claims:
  [OPTIMIZER_REVIEW.md](OPTIMIZER_REVIEW.md).
- The finite-panel source count gives absolute log(en)^5 retained storage,
  with leading coefficient explicitly proportional to
  (L+1)(2m+p)^2[U_fin/a]^2(Ym/gamma)^4. The conservative beta-only envelope is
  beta^(120L). This is a sufficient bound, not a sharp optimum. No label-cap
  substitution is used to remove the fourth power. All data/metric/deficit and
  execution workspace charges are recorded. The guarantee is for the declared
  panel, not arbitrary undeclared queries.
  An exact, fully counted projection onto the panel's input span reduces the
  additive ambient-dimension overhead to O((L+1)(m+p)^2+(m+p)d).
- Literal zero-time-jet compilation is explicit and uses no later dense
  weights, but its certified jet count is superpolynomial. The finite compiler,
  a generic analytic-source obstruction, and a focused label-amplitude route
  are recorded separately. The latter yields norm sensitivity and a narrow
  complex disk, not the required cheap all-time compiler.
  The deterministic compiler and inverse received a separate scoped conditional
  review: [COMPILER_REVIEW.md](COMPILER_REVIEW.md). Its scalar elementary-function
  accounting observation is addressed explicitly in INITIALIZATION.md.
- A cheap polynomial/near-quadratic strictly local setup with the unchanged
  guarantee remains open. It has not been replaced by a full-interval rollout
  under another name. The experimental source producer does use such a rollout,
  and its heuristic rank and selector are not certified by this theorem.

The lead reconstructed the relevant current paper source foundation,
coordinate-selection, comparison and initialized-variance arguments; the
storage route separately checked finite-query localization and tolerance
inversion. A concrete import correction is recorded: the full-range comparison
uses coefficient 64, not the older finite-panel coefficient 32. These checks
are targeted dependency checks, not a new review of the entire paper.
The new deterministic compiler/rank implications remain explicitly separated
from the inherited stochastic source event and its qualitative width onset.

Before the targeted follow-up below, no new training experiment or shared
paper/code change was made. The next theoretical
research obligation is the reachable-coordinate/complex-amplitude estimate
identified in INITIALIZATION.md, not a new empirical sweep. Nothing has been
promoted into the established book or paper.

## Targeted rank-safe experiment: frozen design, 2026-10-08

The user requests a checkpoint of all pending work followed by a small test
that construction below q=m preserves the earlier empirical accuracy. The
checkpoint is `889e444`. Modify only the existing capture executable and this
study's evidence. Use the research-validation and canonical-notation skills.

- Two cases only: raw sklearn digits 3/8 and 1/7, d=64, m=128,
  32 disjoint unlabeled calibration inputs, all remaining inputs scored.
  Dense n=2048, two tanh hidden layers, compressed q=96, source-family rank 12.
  Keep the existing full-horizon offline source rollout and uniform-coordinate
  metric selector; this does not test a cheap initialization-only compiler.
- Implement the exact smooth spectral filter in OPTIMIZER.md with a fixed
  floor tau=0.0001 (normalized feature Gram). Below the source budget, retain
  the constant and the leading singular directions of column-normalized source
  generators, at most floor(q/4) directions total. This is an empirical source
  ordering/selector, not the certified BSS construction. Above the budget it
  keeps the complete old source span. The same initializer is used for both
  cases; no rank/floor/seed search or selection by test performance.
- Reference, iid reference, total-storage-matched small dense and compact use
  fixed Euler step 0.00625 through T=64. Dense and compact also run at twice
  that step. Setup RK4 step 0.125; seed 601; unchanged split/selection seeds.
  Count every moving array, fixed metric/inverse and one floor scalar.
- Primary metric: maximum over the shared observation times of unseen-input
  RMS discrepancy from the coupled dense reference. Also report endpoint RMS,
  actual training MSE, internal deficit energy separately, storage and timings.
  Prediction H1: compact RMS <=3 times iid-dense RMS and below matched-small
  RMS. H0: removing exact source/Gram preservation destroys that advantage.
- Numerical gate: summed dense+compact coarse/fine maximum-time RMS <10% of
  the iid-dense benchmark; finite states, valid positive metrics, and no setup
  access to scored queries. Fitting gate: all fine models have actual training
  MSE <0.01. Failures of numerical/runtime/fitting gates are inconclusive for
  a completed-training comparison, not positive evidence. Preserve raw output.
- Budgets: two GPU workers, setup <=180 seconds, each integration <=180
  seconds, <=20 minutes total wall time for the two cases. No additional
  widths, activations, seeds, ranks or reruns after a gate failure. Tiny CPU
  algebra checks cover legacy equivalence, singular readout, constant source,
  actual-vs-deficit residuals and restart before launch; one scoped final audit.
- Evidence can support or disfavor this fixed-budget empirical witness only.
  It cannot prove logarithmic asymptotic accuracy or repair cheap-setup gaps.

### Outcome: the earlier small-dense advantage did not persist

Both requested cases completed, without parameter searches or follow-up runs.
The construction runs at q=96<m=128, but these tests do **not** establish the
earlier compression-quality claim in this low-budget regime. On 1/7 it stays
within the 3-times-dense-pair comparison but loses to the storage-matched small
dense network. On 3/8 the numerical refinement gate fails; its GF comparison
is inconclusive, and its observed discrete RMS is also worse than small dense.
The algebraic definition and complete-source theorem transfer are unchanged;
neither is an accuracy guarantee for arbitrary truncated q<m sources.

RMS below is against the coupled dense predictions on every scored input,
not against ground-truth labels. Each cell is maximum over the 129 sampled
training times / endpoint. The validation counts are respectively 197 and 201.

| Digits | Independent dense | Rank-safe compact | Matched small dense | Numerical gate |
|---|---:|---:|---:|---|
| 3/8 | 0.021709 / 0.011245 | 0.089524 / 0.072374 | 0.038706 / 0.024027 | Inconclusive |
| 1/7 | 0.030664 / 0.007303 | 0.070991 / 0.036057 | 0.052144 / 0.014601 | Pass |

The compact/dense-pair maximum-RMS ratios are 4.1238 and 2.3151. The latter
passes the benchmark-only threshold but **not** the predeclared joint criterion
of beating matched small dense. No case passes that joint criterion. Dense+
compact refinement sums are 0.00235232 versus threshold 0.00217091 for 3/8,
and 0.00269645 versus threshold 0.00306641 for 1/7. These are practical Euler
refinement checks, not rigorous continuous-time error certificates.

All four fine models fit below actual training MSE 0.01. Dense, compact,
iid and small MSEs are respectively (0.009341, 0.002598, 0.009309, 0.009821)
on 3/8 and (0.004732, 0.002510, 0.004778, 0.004892) on 1/7. Compact deficit
energies are separately 0.002246 and 0.002394; the maximum endpoint residual/
deficit mismatch is 0.080956 and 0.031396. These differences are expected
outside the invertible branch and were not relabelled as prediction loss.

Every case retains 15,584 moving +27,649 fixed =43,233 compact model scalars,
including the 128 deficits and floor. Dense retains 4,327,424; matched dense
has width177 and 42,834 scalars. Model storage reduction is 100.095 times.
The common 8,320 training-data scalars, temporary execution workspaces and
query inputs are reported separately in the raw reports; including the common
training data reduces the ratio to approximately 84.1 times. No dense weights,
source history, calibration array or reconstruction factor is retained in the
deployed checkpoint. Setup retains the same full-horizon rollout provenance,
not the initialization-only compiler proved elsewhere in this study.

| Digits | Setup seconds | Fine dense | Fine compact | Fine iid | Fine small |
|---|---:|---:|---:|---:|---:|
| 3/8 | 5.60 | 8.88 | 87.65 | 8.91 | 8.71 |
| 1/7 | 4.96 | 8.79 | 86.62 | 8.81 | 8.73 |

Both used an RTX3090, one case per GPU. Geometry was assembled in float64;
deployment parameters and Euler updates used float32, while the rank-safe Gram
and spectral correction were evaluated in float64. The constructor's diagnostic
`runtime_dtype` records its pre-deployment float64 input, not the later cast;
the saved run/checkpoint dtypes give the actual deployment precision.
Coarse dense/compact runs took another
4.46/44.26 seconds and 4.46/43.53 seconds respectively. Setup GPU peaks were
approximately 1.09GB. The current sample-space spectral reconstruction is
slower than dense GPU training; the result is about retained storage, not a
training speedup. Total time including all six integrations and setup was
approximately 169 seconds and 167 seconds per case. There was no runtime cap
or nonfinite-state failure.

Full source ranks 229/293 were truncated to 24/24 before selection. Metric
condition factors were between 5.26 and 7.22, with setup identities accurate
to 2e-15. Truncation changes initial features and both initialized mixer
actions; this test does not isolate truncation from the bounded readout as the
cause of the lost small-dense advantage. Source accuracy at this budget is not
certified, and no asymptotic logarithmic claim follows from these two runs.

Reproduction: `paper/figures/capture_trajectory.py compression-probe`, using
`/home/amir/miniconda3/bin/python -B -u`, common arguments
`--width 2048 --depth 2 --activation tanh --samples 128 --calibration 32
--budget 96 --source-rank 12 --readout-floor .0001 --source-step .125
--seed 601 --horizon 64 --step .00625 --per-run-seconds 180`, with
`--device cuda:0 --digits 3 8` or `--device cuda:1 --digits 1 7` and the
corresponding fresh output folder below. Executable SHA256 for both runs:
`43b5aeafe4299eb8f0b6bf17280a7db28d030f723f94196e2aab234731f1346c`.

Raw evidence: [3/8 report](../../data/generated/initialization_panel_compression_20261008/rank_safe_digits38/report.json)
and [1/7 report](../../data/generated/initialization_panel_compression_20261008/rank_safe_digits17/report.json),
with `trajectories.npz` and `compiled_model.pt` beside each. These contain
split hashes, complete commands, software versions, actual time grids, losses,
predictions, counted storage and the complete deployed initialization.

Internal checks: all 12 existing depth/activation checks passed. New tiny CPU
checks cover inactive-filter equivalence (readout discrepancy 1.3e-13), q=1/4
singular construction, residual and deficit-energy identities, constant
preservation, explicit storage and restart. A separate scoped reconstruction
also checked singular sample/width-space spectral equivalence and arbitrary-
state residual/energy identities. Its final artifact check reproduced all RMS
and refinement summaries exactly and counted checkpoint arrays independently.
Final training states were not saved, so the recorded actual training losses
were checked against the execution/report path, not recomputed from final
weights. These checks are not a paper promotion or a broad audit. The
predeclared stop applies: no refinement or retuning campaign.

## Eight-training / sixteen-test preservation check: frozen follow-up

The user now explicitly requests a small new test in the earlier low-sample
regime, and confirms that the 16 scored test inputs may enter setup, but not
their labels. This is a continuation of implementation validation, not a new
theoretical claim or reopening of the q<m campaign.

Four cases only: digit pairs 3/8 and 1/7 crossed with (tanh, two hidden layers)
and (SiLU, three hidden layers); n=8192, m=8, p=16, raw d=64, q=383,
source-family rank15, seed601 and unchanged split/selector seeds. Use the
same full-horizon RK4 source setup (step0.125) for old and new compression.
There are no extra calibration inputs. Use the first16 points of the fixed
seed48 permutation of the held-out pool; test labels are stored only to
document provenance and never used in model initialization or training.

Compute old and new initial states independently from those same sources and
assert agreement of every state/metric array. Fix the new floor before its
integration to min(0.0001, initial normalized compact training-Gram gap/8).
This training-geometry rule is not tuned on test errors; it may be smaller
than the absolute floor in the q<m experiment. The new spectral evaluator
uses float64 internally, unlike legacy float32 Cholesky, so bitwise trajectory
agreement is not presumed. Record Gram minima at observation times, without
claiming these bound the unsampled trajectory.

All five models (dense, independent dense, matched-small, old compact, new
compact) use Euler step0.003125 to T=32. Dense and both compacts also run
at step0.00625. Report max-time and endpoint panel RMS, actual training MSE,
moving/fixed storage and times. A preservation pass requires old-new max-time
RMS <=1% of iid-dense max-time RMS. Advantage additionally requires new
compact RMS <=3 times iid-dense RMS and below matched-small RMS. Require all
fine training MSEs<0.01; each dense+compact refinement sum must be below10%
of iid variability. Failed numerical/fitting/runtime gates are inconclusive.

Run the four fixed cases on the two available GPUs, cap setup and individual
integrations at180s and each case at900s. No seed/rank/floor/width searches or
scientific reruns. Stop after one scoped code/result consistency check; failed
cases remain in the report. The executable stays in the existing single
capture script; generated products remain under this study's data namespace
and outside new Git commits, as required by the shared workflow.

### Outcome: preservation holds at both tested Euler steps

All four cases completed without retuning. Old/new maximum-time prediction
RMS difference was at most 6.055e-7 on the fine grid and 3.708e-7 on the coarse
grid. All initial state and metric arrays agreed exactly, and no source
truncation occurred. Thus the q<m extension preserves the previous full-source
implementation in these tests; this does not improve its deficient-budget
accuracy. The old and new models beat matched-small dense in all four saved
Euler runs. Two tanh cases pass the full fitting/refinement/accuracy gates;
the two SiLU cases remain inconclusive for the stricter GF-accuracy claim
because both old and new fail the predeclared refinement gate.

Maximum over the 65 recorded times of RMS discrepancy from coupled dense,
using all16 declared test inputs (not ground-truth-label MSE):

| Digits / activation / hidden depth | Iid dense | Old compact | New compact | Matched small |
|---|---:|---:|---:|---:|
| 3/8 / tanh / 2 | 0.0120061 | 0.0127820 | 0.0127820 | 0.0283108 |
| 1/7 / tanh / 2 | 0.0126452 | 0.0108903 | 0.0108903 | 0.0254512 |
| 3/8 / SiLU / 3 | 0.0627040 | 0.0451164 | 0.0451169 | 0.0781932 |
| 1/7 / SiLU / 3 | 0.0711107 | 0.0178339 | 0.0178339 | 0.2558581 |

Endpoint RMS in the same order:

| Digits / activation | Iid dense | Old compact | New compact | Matched small |
|---|---:|---:|---:|---:|
| 3/8 / tanh | 0.0120057 | 0.0127817 | 0.0127816 | 0.0281718 |
| 1/7 / tanh | 0.00983393 | 0.0108903 | 0.0108903 | 0.0164110 |
| 3/8 / SiLU | 0.0302960 | 0.0229638 | 0.0229637 | 0.0468894 |
| 1/7 / SiLU | 0.0161612 | 0.0178339 | 0.0178339 | 0.0700084 |

For tanh, the new compact model stores 171,592 moving and 440,068 fixed scalars, total
611,660 versus 67,641,344 dense: 110.5865-fold model compression. For SiLU,
318,281 moving +733,446 fixed =1,051,727 versus 134,750,208 dense:
128.1228-fold. Old compact has one fewer scalar (no floor). The matched small
widths are750 and709, with611,250 and1,051,447 scalars. Common training-data
storage is520 scalars; the declared16 test inputs occupy another1024 if kept
alongside the model. Neither data nor workspaces are included in those model
ratios. Source histories and the dense model are discarded at deployment.

All five fine models in all cases have actual training MSE below0.000401.
New compact MSEs, in table order, are 9.24014e-5, 2.95400e-4, 2.75835e-6
and9.09013e-5. The sum of dense+new coarse/fine max-time discrepancies versus
the 10%-iid thresholds is (0.00107210,0.00120061),
(0.00126104,0.00126452), (0.00685166,0.00627040) and
(0.00784479,0.00711107). The second tanh case passes narrowly; both SiLU
cases fail. Legacy refinement has the same outcomes. These are empirical
refinement diagnostics, not rigorous bounds on the continuous flow.

The fixed floors were1e-4 for tanh and 2.12663e-5 /2.17526e-5 for SiLU3/8
and1/7. The minimum observed training-Gram gaps were respectively0.00132570,
0.00117622, 0.000170130 and0.000174021, all above the corresponding floors.
These observations support the expected inactive-filter mechanism at the
sampled times; they do not certify the gap between observations or all time.
Legacy uses float32 Cholesky, new uses a float64 spectral reconstruction
cast back to float32; sub-micro RMS differences are consistent with that
arithmetic distinction. Source and initial metric assembly are float64.

| Case | Setup seconds | Fine dense | Fine old | Fine new | Fine iid | Fine small |
|---|---:|---:|---:|---:|---:|---:|
| tanh3/8 | 6.63 | 25.47 | 24.97 | 31.67 | 25.46 | 8.65 |
| tanh1/7 | 6.30 | 24.82 | 24.80 | 31.29 | 24.85 | 8.57 |
| SiLU3/8 | 11.95 | 54.16 | 34.41 | 41.50 | 50.80 | 13.04 |
| SiLU1/7 | 11.43 | 48.56 | 34.23 | 40.72 | 48.55 | 12.75 |

Every integration stayed below180s. The four cases, including all coarse
checks, took roughly7.4 minutes elapsed using both RTX3090s. No additional
experiments were launched after the failed SiLU gates. Setup still uses the
full-horizon disposable dense rollout; this check does not establish a cheap
initialization-only compiler, whole-sphere approximation or logarithmic
asymptotic accuracy. The test inputs were explicitly available to setup.

Reproduction uses [PANEL_PRESERVATION_PLAN.json](PANEL_PRESERVATION_PLAN.json):
`/home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py
compression-sweep --plan studies/initialization_panel_compression_20261008/PANEL_PRESERVATION_PLAN.json
--devices cuda:0 cuda:1 --out data/generated/initialization_panel_compression_20261008/panel_preservation_8_16
--case-seconds 900`, with a fresh output folder. Frozen executable SHA256:
`a0ca039bba4d319910c467f65f5226306bbce00b4775a13cb1b13bdd0339ab60`.
The [summary](../../data/generated/initialization_panel_compression_20261008/panel_preservation_8_16/summary.json)
links all four per-case reports, arrays, model checkpoints and logs. As in the
previous test, final training states were not saved; prediction arrays and
reported actual training losses remain distinct evidence products.

One scoped independent artifact/code check reconstructed all RMS, refinement
and gate values, verified frozen source/checkpoint hashes, and counted model
arrays. It confirmed the two sizes, the one-scalar old/new difference,
training/panel separation and test-label exclusion. All four preserve the
old implementation at both saved Euler resolutions; only the two tanh cases
pass the additional GF comparison gate. No unresolved artifact inconsistency
was found, and no extra runs or broad audit were added.
