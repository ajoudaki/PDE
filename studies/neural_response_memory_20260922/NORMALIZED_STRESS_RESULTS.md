# Deep normalized high-frequency stress tests

Executed 2026-09-25. This is a bounded finite-step experiment in the existing
neural-response-memory study, not a numerical certificate for gradient flow.
Root authored the implementation extension, checks, cases, execution and report.
All four task workers exited successfully; all predeclared cases are retained.

## Main findings

- 82 fits completed; 39 attained training RMS <=0.05, 16 attained <=0.01.
  The other endpoints hit the 10s integration cap; no state became nonfinite.
- LayerNorm AFTER activation is generally more useful under this budget.
  Depth20 GELU on the full high-frequency circle: dense training RMS 0.0100
  after-normalization versus 0.9993 before-normalization. Both use the same
  seed, initialization scaling and Euler step. This is one setting, not a
  universal normalization-placement ranking.
- Even among adequately fitted endpoints, P<=3 is not uniformly accurate.
  GELU after-normalization on the full circle has P3/dense RMS 0.1201 and
  0.2054 at depths10/15. Neither row improves monotonically over P1/P2/P3.
  GELU on the full sphere improves with order at each depth, with P3 errors
  0.0078, 0.0276 and 0.1017 at depths10/15/20.
- The clearest fitted restricted-support discrepancy is ReLU at depth20
  with after-normalization on the spherical cap: dense/P3 train RMS
  0.025793/0.037000, but whole-sphere discrepancy 0.818805. It is 0.334122
  inside the cap and 0.925586 outside, so extrapolation amplifies disagreement.
- Circle-patch fits remain too incomplete for clean fitted comparisons;
  their achieved errors are shown, not interpreted as intrinsic closure floors.
  SELU spherical-cap closures also remain substantially underfit (P3 RMS1.0094),
  although the dense reference reaches0.0363.
- Task generalization itself is poor. On the full sphere, GELU dense test RMS
  is1.2573/1.1556/1.1019 at depths10/15/20; the zero predictor scores1.
  Near interpolation of64 training labels does not recover this oscillatory
  target at unseen points. Several closures reproduce that poor dense predictor
  quite closely. Approximation error and target error must remain separate.

## Model, data and checks

Width2048; depths10/15/20; float32; seed20260920; simultaneous Euler1/128;
64 samples;8192 test directions; training RMS target0.01;10s/20000-update
per-fit limits;8-update GPU blocks. Main sweep: GELU after-normalization at
all depths and four tasks. GELU before-normalization is tested at depth20.
ReLU/SELU are tested at depth20 after-normalization on the two patch tasks.
The two unnormalized depth20 GELU dense controls remain at their initial
training RMS1.0000/1.0331. This control retains the original gain-one Gaussian
initialization, and does not establish failure of every unnormalized design.
No residual connections, adaptive optimizer, step search or repeated fitting.

Circle target is sqrt(2)sin(24theta). Training is either whole-circle or a
90-degree arc containing six full oscillations, with midpoint-spaced inputs.
Sphere target is sin(6pi x)sin(6pi y), scaled to unit full-sphere RMS using the
fixed test quadrature. Training is uniform on the sphere or the cap z>=0.5.
That cap is one quarter of the sphere. The task generator fixes seed20260926.
Sphere test points are an equal-area Fibonacci grid; circle test angles are
uniform midpoints. For patch cases, all outside-region points are unsupported
by training. For full cases, the same regional mask is only a reporting split.

LayerNorm is non-affine, per-sample/across-neuron, epsilon1e-5, with derivatives
through both mean and variance. Its exact Jacobian and the unchanged hidden-link
outer-product gradient/moment construction are recorded in README.md. The old
pointwise-activation convergence theorems are not automatically theorems for
this neuron-coupled normalization. Initialization operators remain dense.

The muP scaling retains f=c^T h/n, hidden weights initialized with variance1/n,
first-weight/readout mobilities n and internal mobilities1, with the existing
vanishing-readout initialization. This matches the width exponents of
[MuSGD](https://github.com/microsoft/mup/blob/main/mup/optim.py) in these stored
coordinates. A constant learning rate on every stored block would not match it.
The [official coordinate-check guidance](https://github.com/microsoft/mup#checking-correctness-of-parametrization)
motivates the additional width check, with feature MOVEMENT rather than just
normalized feature norms. On a smooth32-sample sphere diagnostic at time2,
20-hidden-layer GELU after-normalization gives:

| Width | First-layer feature movement RMS | Last-layer feature movement RMS |
|---:|---:|---:|
|256|0.04165|1.19123|
|512|0.04540|1.23436|
|1024|0.04407|1.23188|

The12 probes cover both placements, depths10/20 and these three widths. The
before-normalization depth20 first-layer movement is0.02286/0.02154/0.02293,
and last-layer movement is0.72562/0.72415/0.70614. This supports width-consistent
nonlazy feature learning in the tested regime, not a joint depth-width theorem.

CPU validation:282 independent PyTorch layer_norm/autograd comparisons, maximum
absolute error9.95e-14, including nonzero reconstructed closure histories and
query-batch independence. The original unnormalized path still passes1122
checks with maximum error2.22e-16. Four tiny GPU graph/eager comparisons agree
exactly. Post-run source/input hashes match, and574 scalar scores recomputed
from saved predictions agree with the producer (absolute tolerance1e-12).

## Full achieved-endpoint table

Test columns are whole-manifold closure-versus-matching-dense RMS. Target
columns compare against the actual regression function. The same dense
reference is used within each task/depth/normalization/activation group.
A dagger means one compared training RMS exceeds0.05; such entries are
inconclusive as fitted-model comparisons. Many unmarked rows hit the time cap
between0.01 and0.05; exact statuses, steps and times are in stress_rms.csv.

| Task | Depth | Norm | Activation | Dense train | P1 test | P2 test | P3 test | P3 train | Dense target | P3 target |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| circle_full | 10 | after | gelu | 0.0098 | 0.1048 | 0.1082 | 0.1201 | 0.0098 | 0.3584 | 0.3538 |
| circle_full | 15 | after | gelu | 0.0095 | 0.1503 | 0.2254 | 0.2054 | 0.0099 | 0.3001 | 0.3320 |
| circle_full | 20 | after | gelu | 0.0100 | 0.2654 | 0.7926† | 0.7204† | 0.7501 | 0.3562 | 0.7925 |
| circle_full | 20 | before | gelu | 0.9993 | 0.0054† | 0.0002† | 0.0011† | 0.9997 | 0.9994 | 0.9997 |
| circle_patch | 10 | after | gelu | 0.1100 | 0.9406† | 0.9591† | 0.9942† | 0.1723 | 0.8735 | 1.3080 |
| circle_patch | 15 | after | gelu | 0.2136 | 1.0373† | 1.0361† | 1.0365† | 0.1835 | 0.8769 | 1.3423 |
| circle_patch | 20 | after | gelu | 0.4463 | 0.9974† | 0.9680† | 0.9315† | 0.3536 | 0.9107 | 1.2695 |
| circle_patch | 20 | before | gelu | 0.5614 | 0.9251† | 0.5800† | 0.5029† | 0.8865 | 0.9284 | 1.0264 |
| circle_patch | 20 | after | relu | 0.0535 | 0.6706† | 0.5963† | 0.8084† | 0.3902 | 0.8769 | 1.2193 |
| circle_patch | 20 | after | selu | 0.7011 | 0.5804† | 0.5267† | 0.3455† | 0.8344 | 1.1852 | 1.0960 |
| sphere_full | 10 | after | gelu | 0.0100 | 0.0227 | 0.0092 | 0.0078 | 0.0100 | 1.2573 | 1.2581 |
| sphere_full | 15 | after | gelu | 0.0132 | 0.0563 | 0.0340 | 0.0276 | 0.0156 | 1.1556 | 1.1556 |
| sphere_full | 20 | after | gelu | 0.0226 | 0.1188 | 0.1086 | 0.1017 | 0.0263 | 1.1019 | 1.1068 |
| sphere_full | 20 | before | gelu | 0.0666 | 0.2545† | 0.2964† | 0.1381† | 0.0772 | 1.2817 | 1.3173 |
| sphere_patch | 10 | after | gelu | 0.0100 | 0.0806 | 0.0797 | 0.1026 | 0.0105 | 1.0882 | 1.1143 |
| sphere_patch | 15 | after | gelu | 0.0173 | 0.0858 | 0.0852 | 0.0880 | 0.0206 | 1.0726 | 1.0825 |
| sphere_patch | 20 | after | gelu | 0.0261 | 0.1462 | 0.1368 | 0.1719 | 0.0318 | 1.0750 | 1.1087 |
| sphere_patch | 20 | before | gelu | 0.0871 | 0.6201† | 0.5682† | 0.5155† | 0.5212 | 1.1387 | 1.2789 |
| sphere_patch | 20 | after | relu | 0.0258 | 0.8767 | 0.5625 | 0.8188 | 0.0370 | 1.1227 | 1.4051 |
| sphere_patch | 20 | after | selu | 0.0363 | 0.8144† | 0.7580† | 0.8826† | 1.0094 | 1.3100 | 1.0243 |

## Interpretation limits and evidence

Endpoints have their own training stop, not common physical time or exactly
matched loss. Equal wall budgets also permit fewer updates as depth increases.
Thus increased errors at greater depth cannot be attributed exclusively to
architecture or memory order. The finite-step comparison is useful practical
evidence; no time-step refinement was run, so discretization and closure
truncation are not isolated. Nonfinite-state absence is not an accuracy test.
These observations do not establish a positive limiting training loss or
refute a continuous-flow order-convergence theorem.

Worker elapsed seconds (including setup/queries/saving, excluding process
startup): circle_full161.77, sphere_full166.43, circle_patch281.81,
sphere_patch275.45. Full-space workers and then patch workers ran in pairs
on the two GPUs (about7.5 minutes of paired worker phases, plus launch gaps).
Total measured integration is 790.05 summed GPU seconds,
within the820-second primary cap apart from permitted final-block overshoot.
No further experiment was triggered. Earlier depth4 results retain their scope.

Sources: compact_flow.py, check_normalized_flow.py, quick_normalized_stress.py,
summarize_normalized_stress.py. Reproduce each task with:

```
python -B studies/neural_response_memory_20260922/quick_normalized_stress.py --task circle_full --device cuda:0 --out <fresh-output>
```

Use circle_patch/sphere_full/sphere_patch analogously. Run the CPU checker
without arguments; coordinate probes use --device cuda:0 --out <fresh-json>.
Analyze the four task folders with summarize_normalized_stress.py <root>.
Every producer results.json retains its exact command, environment and hashes.
Generated data: data/generated/neural_response_memory_20260922/compact_normalized_stress01/.
Full scores: stress_rms.csv; summary: summary.json; complete predictions/data
are in the four task directories; coordinate/implementation checks are retained
as coordinates.json, graph_check.json and checks.json.
