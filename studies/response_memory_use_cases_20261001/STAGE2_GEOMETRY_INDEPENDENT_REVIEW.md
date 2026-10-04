# Independent internal review: finite-order ascent and exact loss certificate

Reviewer: `geometry_stage2_review`, 2026-10-02. This is an isolated internal
mathematical/code review, not a promotion review. The frozen theorem input is
`STAGE2_CHALLENGE_THEORY.md`, SHA-256
`717ce7b1dfe6937e08c93a1cf3d990e5fdf88f57bd7d6af39d0602f559bcfabb`.

**Verdict: the assigned mathematical claims pass, with their stated
quantifiers and limitations.** The finite-order initialized binary-label
counterexample, width replication, Gaussian-support conclusion, rank-at-most-
`2C` physical velocity, exact loss certificate, common clock/memory gate, and
commutation criterion are correct. Independent numerical checks support the
implementation. The practical improvement prediction fails in every tested
domain. No promotion or competitive-optimizer claim is justified by this review.

## Review scope and independence

The mathematical verdict was derived from the complete frozen challenge note,
`MODEL_RECONCILIATION.md`, `INPUT_FIELD_DERIVATION.md`, and the model/clock
definitions in repository-central `paper/main.tex` and `paper/results.tex`.
The paper's convergence theorems were not imported. The implementation review
used `input_field.py`, the relevant `Flow` and `LowRankFlow` definitions in
`baseline_compact_flow.py`, `stage2_root_gate.py`, `stage2_root_gate_analyze.py`,
the imported `pca` and `TunedFactors` definitions in
`stage2_index_experiment.py`, and the data protocol/preparation source.
The initial displayed read of the index source extended through line 115;
only `pca` (27–39) and `TunedFactors` (42–50) were used as review inputs or
executed. The audit script enforces that restriction by extracting those two
AST definitions. It omits the baseline's unused maintained-dictionary import,
so execution does not acquire additional scientific inputs from that module.

Raw inputs were restricted to `stage2_data01`, `stage2_root_gate01`,
`stage2_root_gate_diagnostics01`, `stage2_root_gate_analysis01`,
`stage2_root_gate_checks01`, and
`stage2_challenge/finite_q_v2_20261002` under the study's generated directory.
Other generated directory names were incidentally listed as metadata; their
contents were not read. No other study, prior independent review, author chat,
Git history, or archived book was read. Required canonical-notation/neural
conventions and rigorous-math skills were read and applied.

The newly supplied author interpretation `STAGE2_ROOT_GATE_RESULTS.md` was
read only after the independent theorem audit and raw recomputation completed.
Its reviewed hash was
`0615a82f2a5a1230b90b7c25b3b95f2d420159cdabfd0dbec543a52902205fa9`.
No input was edited; only this report, the owned audit source, and
`stage2_geometry_review01` were written. No Git operation, GPU work, or full
training fit was performed.

## Mathematical findings

The setup is the stated two-hidden-layer tanh network with output
\(f_a=w^\top h_a^{(2)}/n\), residual \(r_a=f_a-y_a\), loss
\(\mathcal L=m^{-1}\sum_a r_a^2\), and block mobilities \((n,1,n)\).
Backward responses \(\delta_a\) exclude the residual. The input functions
are fixed and orthonormal for the empirical training law. The finite-order
state includes both families of raw moments and the clock \(\tau\).

**Initialized ascent at each fixed finite order.** For the scalar-width
binary construction, the inputs are the three normalized coordinate inputs,
labels are \(\alpha(-1,1,1)\), initial first activations are
\((3/4,1/4,1/4)\), initialized hidden weight is \(\varepsilon\), and initial
readout is exactly zero. The first-activation mean is \(H_0=5/12\), while
\(\mathbb E[yh(0)]=-\alpha/12\).

At \(\varepsilon=0\), the exact background has
\(\tau_0=1+\alpha t\), \(\bar h_0=\tau_0 H_0\), and all higher forward
and all backward modes zero. For every higher forward mode, the zeroth-mode
dilation term cancels the incoming source. This verifies the actual prefix
and activity clock, rather than replacing them by an untruncated-history
limit. On the compact horizon in question, \(\rho=\alpha>0\) and
\(\tau\ge1\), so the finite vector field is smooth in state and perturbation.
Smooth parameter dependence can be applied in a compact tube for each fixed
\(q\). The parity transformation in the note is an exact symmetry of both
equations and initialization, including first-layer motion and residual RMS.

Consequently the leading reconstruction is
\(v=\varepsilon-2H_0\bar\delta_0+O(\varepsilon^3)\), in a uniform
\(C^1\) expansion. The zeroth backward source is
\(-\alpha w/3+O(\varepsilon^3)\), giving

\[
\dot v=\frac{5\alpha}{18}w+O(\varepsilon^3),\qquad
\dot w=-\frac\alpha6v+O(\varepsilon^3).
\]

At \(t_*=3\pi\sqrt{3/5}/\alpha\), these equations give
\(v=O(\varepsilon^3)\) and
\(w=-\sqrt{3/5}\,\varepsilon+O(\varepsilon^3)\).
The true hidden loss gradient is
\(\partial_v\mathcal L=\alpha w/6+O(\varepsilon^3)\).
Both canonical outer blocks contribute nonpositive dissipation, and their
orders are too small at this endpoint to cancel the hidden contribution.
Thus \(\dot{\mathcal L}(t_*)=\alpha^2\varepsilon^2/36+O(\varepsilon^4)>0\).
All constants may depend on the fixed order and fixed label scale. The proof
does not require a uniform remainder in \(q\).

Width replication is exact under
\(W_0^{(2)}=\varepsilon\mathbf1\mathbf1^\top/n\), replicated first rows,
replicated moment coordinates and readout. The output normalization and
mobilities cancel the replication factors correctly. Continuity on the
compact solution interval produces an open neighborhood in the first and
initialized hidden weights, while the readout stays exactly zero and the
prefix is reinitialized from those first weights. The independent Gaussian
laws have positive density in that finite-dimensional space. This yields
positive probability separately for each fixed \(n,q,\alpha\). It supplies
no uniform probability, typical-draw assertion, periodic orbit, eventual
nonfitting result, or common \(\varepsilon\) for all orders. The note states
these limits correctly. Its earlier untruncated two-label and binary
constructions also have the correct signs and constants.

**Physical velocity and certificate.** Define current input coefficients
\(H_c=\mathbb E[h\psi_c]\), \(R_c=\mathbb E[r\delta\psi_c]\), and endpoint
evaluations \(h_c^*=\tau^{-1}\sum_{j<q}(2j+1)\bar h_{c,j}\),
\(b_c^*=\tau^{-1}\sum_{j<q}(2j+1)\bar\delta_{c,j}\).
Direct differentiation of the reconstructed hidden matrix gives

\[
V=\dot W=-\frac2n\sum_c
\left[R_ch_c^{*\top}+\rho b_c^*(H_c-h_c^*)^\top\right].
\]

The coefficient of each diagonal mode product is
\((2j+1)(1+2j)=(2j+1)^2\); the two triangular sums supply all off-diagonal
products once. This is the necessary cancellation of the clock/dilation
terms. The bound is on instantaneous physical velocity, not on the rank of
its time integral. It is at most \(2C\), while the represented correction
has the separate bound \(Cq\).

With \(S=2(nm)^{-1}\sum_a r_a\delta_a^\top Vh_a\) and
\(D=(\|\dot W^{(1)}\|_F^2+\|\dot w\|_2^2)/n\), the chain rule gives
\(\dot{\mathcal L}=-D+S\). The claimed extra contraction costs follow
from applying the displayed factors and summing stored modes. Fixed dense
base storage and ordinary forward/backward work remain.

**Common gate and regularity.** For fixed \(\kappa>0\),
\(\gamma=\operatorname{clip}(-S/\kappa,0,1)\) satisfies \(\gamma S\le0\).
Multiplying every forward/backward moment derivative and the common clock
derivative by the same scalar gives the physical velocity \(\gamma V\).
Both outer equations remain unchanged, so the modified flow satisfies
\(\dot{\mathcal L}=-D+\gamma S\le-D\). Scaling only writes would not
prove this identity.

The residual RMS is a norm of a smooth residual map and is locally Lipschitz,
including at exact fit. The reconstruction only divides by \(\tau\ge1\),
and clipping is Lipschitz. Products of these functions are locally Lipschitz
on bounded neighborhoods. This proves local well-posedness of the modified
finite-dimensional flow and \(\dot\tau=\gamma\rho\ge0\). There is no
global-existence, Euler-step monotonicity, dense-tracking, or fitting theorem.
The note correctly describes a changed optimizer.

**Commutation criterion.** For the sample feature matrix
\(H=[h_1,\ldots,h_m]\), Gram matrix \(A=H^\top H\), backward matrix
\(B=[r_1\delta_1,\ldots,r_m\delta_m]\), and orthogonal projector \(P\),
the pairing is \(\operatorname{tr}(B(AP+PA)B^\top/2)\). Its nonnegativity
for every \(B\) is equivalent to \(AP=PA\): in the range/kernel split of
\(P\), a nonzero off-diagonal block gives an arbitrarily signed cross
term against a zero lower diagonal block. The converse follows from the
positive semidefinite upper block. The quantitative bound in (17) follows
from restricting to singular vectors of that off-diagonal block and is
correct, including its \(b=0\) exception. Arbitrary backward matrices are
not automatically realizable network states; the proof and report preserve
that distinction. The PCA dictionary commutes with the initial feature Gram;
it need not commute with the later Gram when first-layer features move.

The temporal-rotation/SVD and endpoint Taylor calculations in section 5 also
check. They concern endpoint sensitivity, not alternate reachable histories
or causal retraining.

## Independent computations and empirical conclusions

The owned source `stage2_geometry_review.py` implements direct scalar ODEs,
an explicit outer-product reconstruction differentiated with autograd/JVP,
source parity, width replication, random-matrix tests, and raw-output checks.
It covers 36 randomized float64 states, orders 1, 3, 7, and all three gate
branches. No full fit is part of these checks.

| Independent check | Maximum absolute discrepancy |
|---|---:|
| Autograd loss directional derivative versus certificate | 2.67e-15 |
| Reconstruction JVP versus gated physical velocity | 1.78e-14 |
| Singular values beyond the rank-2C bound | 1.12e-14 |
| Original fit-source versus expanded diagnostic-source state RHS/metrics | 0 |
| Ungated certificate learner versus original input-field RHS | 4.45e-16 |
| Spatial-plus-lag decomposition | 1.78e-15 |
| Exact-fit RHS | 0 |
| Width-one versus replicated width-five states/velocities | 8.68e-19 |
| Imported PCA orthonormality | 1.67e-15 |

Ten independent random-matrix cases also satisfy the negative-eigenvalue
bound, and a backward row chosen along the negative eigenvector realizes the
predicted negative pairing. These finite tests support rather than replace
the proofs.

Fresh scalar ODE checks at orders not used by the author give the following
positive endpoint derivatives divided by \(\varepsilon^2/36\):

| q | epsilon=0.03 | epsilon=0.015 |
|---:|---:|---:|
| 3 | 1.010456703059 | 1.002610648943 |
| 8 | 1.010446562425 | 1.002608151041 |

They use the actual prefix and clock, both outer equations, DOP853,
`rtol=1e-12`, `atol=1e-14`. The larger perturbation is intentionally outside
the author's two-point numerical protocol; its ratio being above 1.01 is
not a failure of that frozen protocol. Halving the perturbation reduces the
normalized remainder by approximately four. Recomputing the author's
twelve retained rows confirms its original gates and a maximum coarse/fine
ratio difference of 8.521e-12.

All 132 primary/refinement checkpoint test RMSEs were recomputed directly
from frozen predictions and targets, agreeing within 3.98e-8. All 33
validation-selected checkpoint indices and scalar diagnostic dictionaries
agree with the raw arrays. Diagnostic replay predictions and the original
seven metric columns are exactly equal to the original seed-4101 field runs.
The saved gated total derivative is nonpositive at every sampled time;
there are no positive one-unit sampled loss increments. This does not
resolve unobserved times or certify every Euler step.

| Domain | Ordinary field median test RMSE | Gated median | Factors median | Practical gate |
|---|---:|---:|---:|---|
| Fashion | 0.6679202914 | 0.6750220656 | 0.6777333021 | Fail |
| HAR | 0.0634784326 | 0.0687632635 | 0.0379050076 | Fail |
| Housing | 0.3173756003 | 0.3185952008 | 0.3137605190 | Fail |

The gated method loses to ordinary memory on all nine paired seeds. It beats
factors only on Fashion, by far less than the required 5%. The largest
seed-4101 step-refinement change in selected test RMSE is 2.094e-5, and all
six changes pass the declared 1%-of-training-label-RMS threshold.

For ordinary Fashion, positive hidden contributions occur at 90.625%,
88.28125%, and 87.5% of the 128 sampled times. Total loss derivatives remain
negative at those samples. In the seed-4101 decomposition the current input
projection is positive at 90.625% of samples and temporal lag at 21.875%.
The signed sampled sums of both contributions are negative. Thus high
frequency of positive hidden contribution is not net integrated harm and
does not prove a benefit from freezing the hidden matrix. HAR and housing
have no positive hidden sample in the ordinary runs.

The final relative off-diagonal values are 0.2640602, 0.0585357, and
0.0944706 for Fashion, HAR, and housing. In code the precise denominator is
\(\|AZ\|_{\rm op}\), with \(A=H^\top H/m\) and
\(Z=\Psi/\sqrt m\); the numerator is
\(\|(I-ZZ^\top)AZ\|_{\rm op}\). This is a normalized projector/Gram
off-diagonal block, not a universal predictive score or a causal estimate.

Frozen dataset hashes and retained source-byte hashes match their manifest.
Input norms agree with one within 2.23e-16, training/validation selections
are disjoint, and HAR subject partitions are disjoint. This review inspected
the preprocessing source and checked these invariants; it did not independently
repeat every archive-to-array transformation. The housing target is the
declared bounded transformed value, not raw-dollar prediction.

## Implementation limits and minor reporting corrections

The original 33-fit source and expanded three-replay source have separate
snapshots whose hashes match the manifests. Their training RHS is identical;
the later additions enrich diagnostics. The source restores every evolving
tensor after CUDA warmup and capture and then replays exactly the prescribed
step count. Fixed bases/dictionaries are not mutated in the captured RHS.
Stored four-step CUDA/eager discrepancies are zero for all methods. This
review inspected that logic and checked CPU source parity; it did not freshly
repeat GPU capture.

The dense `V` allocation occurs in diagnostic snapshots, outside `rhs`.
The actual learner computes the certificate by low-rank actions. The report
correctly preserves dense fixed storage and dictionary/cached-basis costs.
The recorded fit times include instrumentation and are not an allocator or
throughput benchmark.

No blocking mathematical or experiment-source defect was found. Three narrow
limits should remain explicit:

1. The author-report phrase “Ordinary/gated trajectories in the three
   diagnostic replays” is inaccurate: those replays are ordinary field only.
2. Figure prose that outer dissipation “keeps total loss decreasing” should
   say “at sampled times” when describing these data.
3. The reusable class sets `kappa=.001*mean(labels**2)` without rejecting all-
   zero labels. That corner case gives `0/0` in the gated implementation and
   lies outside the theorem's `kappa>0` assumption. All assigned datasets have
   positive label MSE, so this does not affect any reported fit or verdict.

The first two corrections were sent to the supervisor after the independent
verdict. They do not change the quantitative conclusions. The third is a
reusability caveat, not a requested implementation change in frozen inputs.

## Execution record and artifact hashes

All working commands used `/home/amir/Codes/PDE` as the current directory.
Read-only source inspection used `cat`, bounded `sed`, targeted `rg`,
`sha256sum`, scoped `find`, and a `diff -u` between the two assigned gate
source versions. The scientific executable commands were:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/response_memory_use_cases_20261001/stage2_geometry_review.py > data/generated/response_memory_use_cases_20261001/stage2_geometry_review01/run.log 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/stage2_geometry_review.py > data/generated/response_memory_use_cases_20261001/stage2_geometry_review01/run_conda.log 2>&1
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_geometry_review.py > data/generated/response_memory_use_cases_20261001/stage2_geometry_review01/run_conda_final.log 2>&1
```

The first command stopped at import because the system interpreter has no
PyTorch; no numerical work ran. The second completed, then the script was
expanded to explicitly check PCA, compare every diagnostic dictionary against
raw arrays, and recompute frozen oracle gates. The final command completed
those additional checks. There were eight tiny scalar ODE solves in total
across the two successful audit executions, zero full fits, and zero GPU
seconds. CPU work after imports was approximately 2.80 seconds in total;
the final execution used 1.42 seconds. Each process had a 300-second CPU cap
and one numerical thread. Python 3.10.14, NumPy 1.26.4, SciPy 1.11.4,
PyTorch 2.9.0+cu130 were used for the successful CPU executions.

The complete per-file input SHA-256 map, source-manifest checks, environment,
independent numerical results, and raw comparisons are in
`data/generated/response_memory_use_cases_20261001/stage2_geometry_review01/results.json`.

| Review artifact | SHA-256 |
|---|---|
| `stage2_geometry_review.py` | `cecd5c552bcf11a7fc9f91f77b06b69ed2a7b40e10b9fc37a8b87ab121f8f3fb` |
| `stage2_geometry_review01/results.json` | `2a28e30912975a31c78933a1b5a1b84a13d7b5c78f298732df32ff9c7137ce8c` |

The review report's release hash is supplied separately to the supervisor so
that the report itself can remain a frozen artifact.
