# Independent review of supervised population addresses

Review date: 2026-10-02. This is an internal implementation and evidence review,
not promotion approval. The numerical and implementation checks below pass.
The registered positive performance gate fails: no domain reaches its required
5% median paired improvement, and HAR is materially worse than its factor control.
There is no numerical defect found that reverses that conclusion.

## Scope and reproducibility

The evidence used was the assigned `STAGE2_LABEL_INDEX_PROTOCOL.md`,
`stage2_label_index.py`, `input_field.py`, `baseline_compact_flow.py`, the
`TunedFactors` definition in `stage2_index_experiment.py`,
`MODEL_RECONCILIATION.md`, `STAGE2_DATA_PROTOCOL.md`, `stage2_data.py`, and the
complete frozen `stage2_label_index01` and `stage2_data01` products. The author
results report and other research results were not used to reach this verdict.
Canonical-notation, neural-response-memory, and rigorous-proof instructions were
applied. The original paper and maintained book were outside this assignment;
the reference model was the supplied reconciliation.

The independent executable is `stage2_label_review.py`. To avoid executing
unrelated legacy imports, it compiles exact AST-selected definitions from the
frozen sources: `_activation`, `Flow`, `LowRankFlow`, `InputFieldFlow`,
`TunedFactors`, and the label-run construction/capture/fit functions. It does not
alter those definitions. Oracles separately construct grouped sources,
materialized matrices, automatic-differentiation gradients, split selections,
and normalized data arrays. No original regression suite that imports other
studies was run.

Commands, from this checkout:

```bash
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_label_review.py
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_label_review.py --gpu-only
```

The environment matched the run: PyTorch 2.9.0+cu130, NumPy 1.26.4, one CPU
thread, and an NVIDIA GeForce RTX 3090 for the replay. TF32 was disabled.
Only one full fit was replayed: Housing, seed 4501, `population_matched`,
step 1/64, width 256, through physical time 128. Including three tiny fresh
capture/eager checks, the GPU work took 1.943 seconds. The replay's four test
prediction arrays and all twelve train/validation/test checkpoint metrics were
bitwise identical to the original. Each fresh capture/eager state discrepancy
was zero. GPU0 was released after the checks.

All artifacts below live in
`data/generated/response_memory_use_cases_20261001/stage2_label_review01/`:

| Artifact | SHA256 |
|---|---|
| `input_hashes.json` | `01d4fd727d61cd1463fc3cc83dc0591e878adfd61277c9c78c454a9e9a374bfe` |
| `summary.json` | `57e9235a8339d90976677a713963270d3c2b09e37d18544096fed6b2115903e5` |
| `cpu_oracles.json` | `bb1b21d462c73475c8a36e603fa7fc7a35fef1b3365520d2a205c92e1eda128b` |
| `data_checks.json` | `534785714dcefcfd1ee39b4fb30a0b68545ac6072ea5a218ab791807c1c2c82f` |
| `result_audit.json` | `6a18e37e60f7a31b7c4462999eeda1c0fd2c8c9d7c350b2ca0e05508e3737fd9` |
| `gpu_replay.json` | `ee19c3d43e170abffab898ee87defee03d42b835a224deaf77ddee866a072470` |

The input hash manifest records 112 files, including all original predictions,
results, raw data, source snapshots, assigned live sources, and this reviewer
script. All original recorded source/data checksums match; the live experiment
sources match their frozen copies. All 112 hashes were checked again unchanged
after the computations. The experiment protocol hash is
`84311e244f70a685356d32b7941d053fc02142bbf5c73017cad30b6b1c603aeb`, and its
runner hash is `d262a9f11c86a6d62e0ebe3f4b895ea7e5a9cf322b9ce90e49feac1e5b85a96f`.

## Mathematical and implementation checks

Let the fixed training set have \(m=1024\) pairs, and write
\(E_m F=m^{-1}\sum_a F_a\). For training group \(c\), let
\(p_c=m^{-1}\#\{a:g(y_a)=c\}>0\) and
\(\psi_c(x_a,y_a)=\mathbf 1\{g(y_a)=c\}/\sqrt{p_c}\).
Then

\[
E_m[\psi_c\psi_d]=\mathbf 1\{c=d\},\qquad
E_m[F\psi_c]=\sqrt{p_c}\,E_m[F\mid g(y)=c].
\]

The second identity determines the normalization of every grouped source and
the forward prefix. Replacing it by an unweighted class mean would be wrong
when the classes are imbalanced. The implementation uses the correct empirical
probability normalization, including the actual Housing tie counts.

| Domain | Training group counts | Training probabilities |
|---|---|---|
| Fashion, negative/positive | 519, 505 | 0.5068359375, 0.4931640625 |
| HAR, negative/positive | 590, 434 | 0.576171875, 0.423828125 |
| Housing, increasing target bins | 255, 254, 259, 256 | 0.2490234375, 0.248046875, 0.2529296875, 0.25 |

Housing edges are the training-target quartiles
\((-0.6496325731277466,-0.22610414028167725,0.46253566443920135)\)
after the declared float32 cast. `digitize(..., right=False)` sends an exact
tie to the upper bin. Independently computing float64 quartiles on the saved
training targets gives the same assignments. No empty group occurs. Float64
Gram errors are at most \(2.11\times10^{-15}\); every saved float32 Gram error
and every fresh CPU construction meets \(10^{-5}\).

For clarity, the API input is \(u_a=x_a/\sqrt d\), with \(\|u_a\|=1\).
The actual two-layer network used in the check is

\[
\begin{aligned}
h_a^{(1)}&=\tanh(W^{(1)}u_a),&
h_a^{(2)}&=\tanh(\widehat W^{(2)}h_a^{(1)}),\\
f_a&=w^\top h_a^{(2)}/n,&r_a&=f_a-y_a,\qquad
\rho=(E_m r^2)^{1/2},\\
\delta_a^{(2)}&=w\odot(1-(h_a^{(2)})^2),&
\delta_a^{(1)}&=(\widehat W^{(2)\top}\delta_a^{(2)})\odot(1-(h_a^{(1)})^2).
\end{aligned}
\]

Here \(n=256\) in the fits; \(w\) is the readout, called `c` in code.
The code field `w` instead denotes \(W^{(1)}\). The loss is unhalved
\(E_m r^2\). The checked outer velocities are
\(\dot W^{(1)}=-2E_m[r\delta^{(1)}u^\top]\) and
\(\dot w=-2E_m[rh^{(2)}]\), corresponding to mobility \(n\) for both
outer parameters. The base hidden matrix has independent
\(N(0,1/n)\) entries; the first weights have independent \(N(0,1)\)
entries. Both learners use the same seed for those draws and an exactly zero
readout. Factor initialization uses a separate seeded generator.

For each temporal mode \(j=0,\ldots,q-1\) and population \(c\), the raw
vector memories are \(\bar\delta_{c,j}^{(2)},\bar h_{c,j}^{(1)}\in\mathbb R^n\).
The clock is \(\tau=1+s\), with \(\tau(0)=1\) and \(\dot\tau=\rho\).
The represented matrix and raw moment equations are

\[
\begin{aligned}
\widehat W^{(2)}
&=W_0^{(2)}-\frac{2}{n\tau}
 \sum_{j,c}(2j+1)\bar\delta_{c,j}^{(2)}\bar h_{c,j}^{(1)\top},\\
\dot{\bar\delta}_{c,j}^{(2)}
&=E_m[r\delta^{(2)}\psi_c]
 -\frac{\rho}{\tau}\left(j\bar\delta_{c,j}^{(2)}
 +\sum_{k<j}(2k+1)\bar\delta_{c,k}^{(2)}\right),\\
\dot{\bar h}_{c,j}^{(1)}
&=\rho E_m[h^{(1)}\psi_c]
 -\frac{\rho}{\tau}\left(j\bar h_{c,j}^{(1)}
 +\sum_{k<j}(2k+1)\bar h_{c,k}^{(1)}\right).
\end{aligned}
\]

Initially \(\bar\delta_{c,j}^{(2)}=0\),
\(\bar h_{c,0}^{(1)}=E_m[h^{(1)}(0)\psi_c]\), and higher forward moments
are zero. Thus the length-one constant forward prefix is retained. There is no
extra \(1/m\) in the matrix reconstruction: each memory already contains an
empirical expectation. As a direct check, choosing the complete sample basis
\(\psi_c(a)=\sqrt m\,\mathbf1\{a=c\}\) gives the original sample moments
divided by \(\sqrt m\), restoring the original factor \(1/m\).
Five-step trajectory checks verified this correspondence for \(q=1,3\).

The CPU oracle uses unequal two- and four-group populations, orders
\(q=1,6,12\), and nonzero arbitrary memories/readout. It checks the above
sources against direct conditional means; independent autograd checks the
outer mobilities and backward signals. It also checks raw transport, actual
matrix transpose, prefix initialization, simultaneous Euler updates, and
stationarity at zero residual. No raw equation divides by \(\rho\).
For the factor control, autograd confirms mobilities
\((n,n,\eta,\eta)\) on first weights, readout, and two factors, where
\(\eta=0.25\) for Fashion and \(4\) for HAR/Housing. The baseline rates are
fixed inputs to this review; their earlier selection was outside scope.

There are 202 passing CPU assertions, with maximum absolute discrepancy
\(8.88\times10^{-16}\). These are algebra and implementation checks, not
a fitting or dense-trajectory approximation theorem.

**No query-label leakage was found.** Construction reads only `X_train` and
`y_train`; training labels determine the population addresses, prefix, and
residual-driven writes. `predict(inputs)` uses the current first weights,
readout, and reconstructed matrix. It never evaluates an address at the query.
At nontrivial states, poisoning both stored labels and the entire cached basis
with NaNs leaves the query prediction bitwise unchanged. Restoring them is
necessary for subsequent updates. The test arrays are used only for checkpoint
metrics and saved predictions; validation RMSE alone selects the checkpoint.

The projection identity has its stated limited force. For arbitrary vector
fields \(F,G\) on the empirical training-pair law, define
\(\Pi F=\sum_c E_m[F\psi_c]\psi_c\). Orthogonality gives

\[
E_m[FG^\top]-\sum_c E_m[F\psi_c]E_m[G\psi_c]^\top
=E_m[(F-\Pi F)(G-\Pi G)^\top].
\]

Both mixed terms vanish because the residual fields are orthogonal to each
\(\psi_c\). Cauchy–Schwarz bounds the Frobenius norm by
\(\sqrt{E_m\|F-\Pi F\|^2\,E_m\|G-\Pi G\|^2}\).
The independent oracle verifies this identity and bound on imbalanced groups.
The omitted quantity is within-population covariance; additional temporal
modes do not restore omitted spatial components merely by increasing \(q\).
The identity gives no descent, fitting, tracking, stochastic-law, or prior-shift
guarantee.

## Data, configuration grid, and checkpoint evidence

All saved feature, target, index, group, and subject arrays were independently
reconstructed bitwise from the retained raw archives. Training-only coordinate
means/scales, clipping, appended constant coordinate, and row normalization
were checked. Maximum unit-norm error was \(2.22\times10^{-16}\).
Fashion class selection and official pool separation, the seeded Housing
random split and bounded target transform, and all three disjoint HAR subject
sets match the declared protocol. Raw-file hashes and the required Fashion
MD5/Housing SHA256 checksums pass. This does not independently authenticate the
HAR archive beyond its retained source URL and recorded SHA256.

The completed grid has exactly 36 main fits plus six seed-4501 half-step fits,
with no duplicates or missing configurations. Every fit uses width 256 and
checkpoints 16, 32, 64, 128. Population orders are 1 or 12 for the two binary
tasks and 1 or 6 for Housing; all matched corrections have rank bound 24, and
factors have rank 24. The source uses simultaneous explicit Euler, not an
adaptive method or early stopping. Warmup and graph capture restore all moving
coordinates before physical-time integration.

Each per-fit JSON equals its corresponding aggregate record. All 42 data
hashes match. All 168 test RMSEs were recomputed from saved predictions against
the exact retained targets; the maximum difference from the logged float32
metric is \(6.00\times10^{-8}\). All 168 logged train/validation/test values
and saved predictions are finite. All 42 selected indices are exactly the
first validation-RMSE minimizer among the four declared checkpoints. The source
also asserts finite terminal state before writing a fit.

Train and validation prediction vectors and final state tensors are not saved.
Therefore their metrics and terminal-state finiteness could not be independently
recomputed for all 42 fits; this review checked their code path and records and
reproduced all those metrics for the one fresh Housing replay. The remaining
41 fits were not retrained.

## Registered performance gate

For each domain and paired seed \(s\), let \(R_s^{\rm pop}\) and
\(R_s^{\rm factor}\) be the test RMSEs at each learner's own validation-selected
checkpoint. The paired fractional improvement is
\(I_s=(R_s^{\rm factor}-R_s^{\rm pop})/R_s^{\rm factor}\).
The table reports the median of these four paired fractions, not a ratio of
unpaired model medians.

| Domain | Paired improvements, seeds 4501–4504 | Median improvement | Wins | Meets domain gate? |
|---|---|---:|---:|---|
| Fashion | −0.9148%, −0.4987%, −0.6431%, −0.1379% | −0.5709% | 0/4 | No |
| HAR | −27.6773%, −13.1842%, −56.4714%, −8.5324% | −20.4308% | 0/4 | No |
| Housing | +1.9597%, +0.2428%, +0.3056%, −0.2107% | +0.2742% | 3/4 | No |

The required improvement of at least 5% on at least two domains is absent.
HAR also violates the allowed 5% median worsening on a remaining domain.
Thus the primary positive gate fails without any borderline comparison.
Housing's three wins do not satisfy its magnitude requirement.

All six half-step fits retain their original selected time. Absolute changes in
selected test RMSE are:

| Domain | Matched population | Factors |
|---|---:|---:|
| Fashion | 0.00000625849 | 0.00000137091 |
| HAR | 0.00000968203 | 0.00000897422 |
| Housing | 0.00000038743 | 0.00000348687 |

Every change is below 1% of training-label RMS. As an additional scale check,
each is below one third of its domain's absolute seed-4501 paired RMSE gap;
the largest fraction of such a gap is 0.001012. No positive primary claim is
being licensed by this comparison. Refinement was prescribed only for seed
4501 and the two primary learners, so it is not an all-seed or all-order
integration certificate.

The \(q=1\) learner is a secondary comparison. Its predictions perform very
similarly to the higher-order population learner: the largest paired change in
selected test RMSE is 0.0003103 on Fashion, 0.0005765 on HAR, and 0.00005764 on
Housing. This does not rescue the primary gate, and does not establish that
temporal memory has no value on other tasks.

## State costs and limits of the conclusion

All stored count fields match fresh model construction. The matched population
learner has \(nd+n+2nqC+1\) moving scalars; factors have
\(nd+n+2n\cdot24\). The extra population scalar is its clock. Every learner
also retains the \(n^2=65536\)-scalar base matrix. The population basis stores
\(mC\) scalars, plus small degree/weight vectors; no initialized-first-layer
dictionary is retained.

| Domain | q1 moving | Matched moving | Factor moving | Population basis |
|---|---:|---:|---:|---:|
| Fashion | 202241 | 213505 | 213504 | 2048 |
| HAR | 145153 | 156417 | 156416 | 2048 |
| Housing | 4609 | 14849 | 14848 | 4096 |

These are state counts, not peak GPU memory. They exclude shared training/query
data, transient activations, CUDA graph buffers, and allocator overhead.
The cheap \(q=1\) learner has a different parameter count. No optimized
runtime or memory superiority follows from this experiment; the original
91.872 seconds are instrumented sum-of-fit wall time including setup and
evaluation, not an optimized-system benchmark.

Two provenance limitations should remain visible. First, the original runner
records source and data hashes but does not put each prediction archive's
SHA256 in its per-fit record. This review now hashes every archive, and the
Housing replay matches exactly, but a retrospective hash is not evidence of
immutability since the original run. Second, source snapshots and their hashes
establish the audited contents; without an independently timestamped
registration they do not alone prove that the protocol preceded every fit.
Neither limitation makes the observed negative gate positive.

The justified conclusion is narrow: on these three fixed small datasets,
with this empirical label partition, width, horizon, seeds, initialization,
and fixed factor controls, the supervised population-address candidate fails
its declared practical-advantage test. The implementation is consistent with
the stated finite empirical model. This is neither a universal impossibility
result nor evidence for an all-time theorem, a new-data streaming law,
prior-shift robustness, raw-dollar Housing prediction, or production-scale
generalization. No source inputs were edited, and no Git, paper, or maintained
book changes were made by this review.
