# Independent internal MNIST implementation and result check

Status: implementation and output audit **PASS**, complete for all twelve
scientific trajectories and the final analysis. This is separate from the
scientific numerical gates: at the primary endpoint P1 passes, while P2 and
P3 remain inconclusive under the frozen relative refinement criterion.

This is a scoped internal audit, not an independent promotion review. Inputs
were the frozen MNIST protocol, moment construction, two moment engines,
MNIST preparation/runner/tests, the established finite-network implementation,
and the expressly assigned MNIST generated directories. No other study,
earlier campaign verdict, or another review report was consulted.
The audit owns `check_mnist_moments.py` and this report. Its scratch and
machine-readable evidence are in
`data/generated/neural_response_memory_20260922/mnist_audit01/`.

## Independent checks already completed

- Raw IDX files were parsed without torchvision. Compressed-resource MD5 and
  every recorded raw SHA-256 match. NumPy seed 20260924 exactly reproduces all
  selected/shuffled training indices: 500 threes and 500 eights without
  replacement. Validation comprises all 1010 threes and 974 eights from the
  distinct official test array. No exact selected-image pixel duplicate occurs
  between the two splits. Labels and all prepared pixels reproduce exactly;
  each input has unit Euclidean norm. No estimated preprocessing is present.
- Gaussian draws, their order, and scaling reproduce exactly. Independent
  autograd at perturbed noninitial dense weights verifies unhalved mean squared
  loss, output division by n, and physical mobilities (n,1,n). Maximum absolute
  dense velocity discrepancy was 1.12e-16.
- For each P=1,2,3, independent NumPy reconstruction checks current predictions,
  both middle-matrix actions, both outer velocities, every moment's triangular
  transport, and the physical-defect identity. The checks include nonzero
  evolved/perturbed moments, not only zero-history initialization. Identities
  agree to floating-point roundoff; a central-difference reconstruction
  derivative differs by at most 5.9e-13. An independent Gaussian-quadrature
  derivative of moving-interval integrals checks the Legendre transport
  coefficients to 1.81e-11. Initial canonical middle velocity agrees to
  3.5e-18 for all three orders.
- A nonlinear scalar ODE checks the accepted Heun continuous extension and its
  bisection root against an explicitly derived quadratic. Root precision does
  not certify the flow interpolation error. The producer's endpoint convention
  is checked further through its actual tolerance comparisons.
- Two tiny CPU runs radically change both validation images and labels while
  retaining the training set. Training states, all accepted times/steps/errors,
  losses, and training predictions remain bitwise identical. Source inspection
  shows no held-out predictions or labels in the vector field, acceptance norm,
  loss crossings, or model-parameter selection. These CPU checks are validation
  of implementation, not additional scientific training trajectories.

## Contract and operational details

The protocol originally described fresh fractional Heun endpoint steps. I
flagged that its runner used the quadratic continuous extension. The supervisor
amended the protocol before a successful pilot or any primary run to specify
32 bisections of that extension. This report audits the amended contract;
the two methods are not silently equated. The frozen primary runner includes
the CUDA initialization-before-memory-reset fix; the initial failed pilot
attempt did not reach a training step.

The wall cap includes observation work, whereas reported integration time
separately subtracts observations. It therefore enforces a conservative
integration budget. A trajectory stopped by that operational wall cap can
depend on inference runtime, though not on validation labels or performance.
This is distinct from statistical validation leakage and matters if a capped
trajectory is compared to another model's fitted endpoint.

The implementation computes tanh from weights and moments, so it does not
numerically integrate redundant activation coordinates. Closure RHS calls use
factor contractions; only the initialized W0 is retained densely. Dense learned
matrix reconstruction in this check is an audit-only oracle. At M=1000 and
n=1024, storing these moments is not a measured memory reduction over a dense
middle matrix.

## Result reproduction

All eight primary and four conditional refinement trajectories pass independent
reconstruction of training and validation predictions at their five saved
crossing states plus initial and final states: 84 observation records covering
60 crossing checkpoints.
Maximum held-out prediction discrepancy against saved GPU predictions is
6.92e-15. Every original trajectory reached all five levels, so the predeclared
primary endpoint is training MSE 0.001. Source/data/array hashes, seeds,
initialization draws, retained W0, moment dimensions, interval-length
invariants, times, and crossing losses were checked. Immutable hashes allow
the final aggregate to reuse completed checks without repeating reconstruction.

The separate final analysis check reproduces all 15 endpoint/order comparisons, 84
sets of label metrics, exported scatter predictions/errors, selected times,
refinement requests, numerical gate decisions, and order-comparison verdicts.
I also inspected the primary scatter image: axes, digit colors, equality
line, and numerical caveats correspond to the analyzed data. Final evidence is
`mnist_audit01/final02/audit.json`; the preflight, partial checks, and first
analysis check remain preserved in the same audit directory. Maximum
discrepancy between independently recomputed and reported RMS formulas is
1.74e-18.

The original two tolerances trigger a permitted additional run for each of
dense, P1, P2, and P3. For P1 the trigger is the earlier MSE 0.1 endpoint:
its tolerance change 0.000624920 exceeds ten percent of its fine-resolution
closure–dense RMS 0.00285430. P1 passes the relative check at MSE 0.001;
the contract checks every reached endpoint. All four permitted extra runs
were performed and reached MSE 0.001; no scientific trajectory was capped.

At MSE 0.001, using rtol 1.25e-5 for every model:

| Order | Validation RMS versus dense | Latest closure tolerance change | Numerical gate |
|---:|---:|---:|:---|
| P1 | 0.01877194597 | 0.00023569525 | Pass |
| P2 | 0.00191818689 | 0.00004859559 | Inconclusive |
| P3 | 0.00123213503 | 0.00019882182 | Inconclusive |

The latest dense predictor change is 0.00022038667. It exceeds ten percent
of both the P2 and P3 discrepancies; the P3 predictor change also exceeds its
relative threshold. Their small observed discrepancies are reproducible
finite-integrator measurements, but do not pass the predeclared test of
gradient-flow precision. The P2–P3 RMS gap is 0.00068605186 versus the sum
0.00068819076 of their observed refinement margins, so that ordering remains
unresolved even by this empirical margin comparison. These margins are not
rigorous error bounds. No convergence rate or verified monotone order trend
follows. The P1 discrepancy is below the declared practical threshold 0.1 and
passes its observed refinement gate.

The compared stopping times are each model's own training-loss crossing.
For the final dense/P1/P2/P3 runs they are respectively 512.6923, 629.0073,
514.7915, and 513.3403. They are not common-time trajectory comparisons.

The successful P3 pilot used 0.1750024 seconds per Heun trial and peaked at
651,211,264 allocated CUDA bytes, so the frozen width rule selects n=1024.
The twelve scientific trajectories total 2513.42165 integration seconds;
including successful pilots gives 2520.42815, below the 7260-second budget.
The largest individual scientific integration time is 347.556 seconds.
Independent summation and summary digests are in
`mnist_audit01/final01/resource_check.json`.

## Frozen provenance

All saved scientific summaries agree on these data, initialization, and
producer digests. Full source, archive, checkpoint, and prepared-array hashes
are retained in the audit JSON.

| Object | SHA-256 |
|:---|:---|
| Prepared data | `001d62792dccc16176d8e5cf832687e540c78f8a0f4dded5e42cd04adb74269c` |
| Shared initial weights | `27c1064fb9ccbaf20cde46879148fe86bd60ae5f9e2d6562b85cdc19b103a674` |
| MNIST runner | `a5d5b0f75b2ff99651737d0fa3ac7f344f9744beeba84e2f7265593dde964df3` |
| Orthogonal moment engine | `32f80cf35c44b5015821fa8c8726bb8ff3bc6f7eb3e1b7abe9ee62ea8f529909` |
| Analysis source | `061eff090b9b868edaeb77f7bc774ad1d4460eb95c4866f7168c4bbcb0736653` |
| Independent checker | `6b1d251a4b9495b6f7a2a8b8fab9b1f2a9c26a50333000ed621c452ab930e371` |
| Final audit JSON | `b049ae13ca8d67d6e36fe552429d91ca4f97e5511a7ad67e9475dc2986fb5845` |
| Final analysis summary | `2da1d9e42e362297cac7fc1cc91f8e054121db7357c891fb78c1573f84675e50` |

## Reproduction and scope limits

Interpreter: `/home/amir/miniconda3/bin/python -B`; NumPy 1.26.4 and torch
2.9.0+cu130. CPU checks set `PYTHONDONTWRITEBYTECODE=1`,
`OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`.
The checker takes `--data`, `--output`, and optional `--runs` directories;
`--data-only` skips torch oracles and `--cached-audits` reuses previously
verified unchanged archives. Full source/data/array digests are stored in its
JSON output, not shortened in the executable provenance.

For a fresh full reconstruction, pass all directories matching
`mnist_primary01/{dense,P1,P2,P3}_level{0,1}` and
`mnist_refined01/{dense,P1,P2,P3}_level2` to `--runs`, and
`mnist_analysis02` to `--analysis`. Omit `--cached-audits` to recompute every
saved state. Omitting `--data-only` additionally reruns the tiny preflight
oracles and isolation test.

This audit verifies finite implementation and saved-output consistency. It
does not independently rerun full training, certify a uniform solver error
bound, prove convergence in moment order, establish global-in-time hypotheses,
or generalize beyond this initialization and digit pair. Two-tolerance changes
are empirical resolution diagnostics, not rigorous error bars.
