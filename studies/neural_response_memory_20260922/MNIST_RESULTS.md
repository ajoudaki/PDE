# MNIST 3 versus 8: response-history moments

The bounded campaign is complete. All twelve trajectories (dense and P=1,2,3
at three numerical tolerances) reached training MSE .001 without hitting a
resource limit. These are finite-width empirical results, not a population
convergence theorem or an asymptotic rate.

## Design and observable

Use 500 official training images of each digit, selected without replacement
with seed 20260924, and all 1,984 corresponding official test images as the
held-out validation panel. Flatten 784 pixels and normalize each image to
unit Euclidean length before the stored first-matrix action; physical inputs
therefore have RMS one. Labels are -1 for 3 and +1 for 8. No PCA, whitening,
augmentation, validation fitting or validation-based training stop is used.

The model is bias-free two-hidden-layer tanh, width 1,024, canonical Gaussian
initialization with stored variances (1, 1/n, 1/n^2), output divided by n, unhalved
mean squared loss and physical mobilities (n, 1, n). Every model shares the
same exact initial weights and training subset. Full-batch gradient flow is
integrated in float64 by adaptive Heun. The moment models retain the actual
W0 and its transpose and use MOMENT_CONSTRUCTION.md, with P retained history
modes (degrees 0 through P-1). Algebraic tanh responses are recomputed from the
current state: this is the same continuous closure without redundant lifted
response-coordinate drift. The learned dense correction is not formed by
the closure's evolution code.

The primary metric is sqrt(mean_validation((f_closure-f_dense)^2)). All
comparisons below stop each model at its own first training-MSE .001 crossing;
they do not compare equal physical times or claim infinite-time endpoints.
The five predeclared loss milestones are retained in the analysis. All four
models reached every milestone at every tolerance, so .001 is the primary
endpoint under the frozen selection rule.

## Results and numerical precision

The finest executed tolerance is rtol 1.25e-5, atol 1.25e-7.

| Model | Validation RMS from dense | Own last-refinement prediction RMS | Physical time |
|:---|---:|---:|---:|
| Dense | 0 by definition | 0.000220387 | 512.69234 |
| P=1 | 0.018771946 | 0.000235695 | 629.00734 |
| P=2 | 0.001918187 | 0.000048596 | 514.79149 |
| P=3 | 0.001232135 | 0.000198822 | 513.34032 |

The finest-run predictions of every closure are close to dense on this panel,
with substantially smaller measured errors for P2/P3 than P1. Numerical
resolution must be distinguished from these measured discrepancies. The
frozen strict gate requires each predictor's latest refinement change to be
at most both .005 and 10% of the closure-dense RMS. P1 passes at the primary
endpoint. P2 and P3 do not: the dense change .000220387 exceeds their relative
thresholds .000191819 and .000123214; P3's own change also exceeds its threshold.
The protocol therefore does not classify their strict GF comparison or an
order trend involving them as numerically resolved.

The observed combined refinement sensitivities (dense plus closure) are
.000456082, .000268982 and .000419208 for P1, P2, P3. These are diagnostics,
not rigorous error bounds or statistical confidence intervals. In particular,
the P2-P3 score difference .000686052 is slightly smaller than their summed
sensitivities .000688191. Do not infer a resolved P2-versus-P3 ranking, a
convergence rate, or results on other digits/initializations.

Secondary label metrics: every model classifies all 1,000 training samples
correctly at the stopping point. Held-out classification accuracy is 97.4798%
for dense, P2, P3 and 97.3286% for P1. These do not replace prediction agreement.

## Resources and checks

Both RTX 3090 GPUs were used. The twelve main/refinement trajectories consumed
2513.422 cumulative integration seconds excluding observations, or 2524.426
seconds including observations during evolution. The two successful throughput
pilots add 7.007 pure integration seconds. All four conditional refinements
were used under MNIST_NUMERICAL_DECISIONS.md; no training branch remains.
The initial pilot attempts failed before training due to CUDA lazy
initialization of peak-memory statistics; their logs are preserved separately.

| Model | Moving state plus retained W0, MiB | Finest-run integration seconds |
|:---|---:|---:|
| Dense | 14.13 | 80.12 |
| P=1 | 29.76 | 165.68 |
| P=2 | 45.38 | 258.70 |
| P=3 | 61.01 | 343.51 |

These state counts exclude dataset arrays, saved initialization copies,
solver stages and workspace; measured CUDA peaks are separately recorded.
With 1,000 samples, the 2*n*1000*P history coordinates exceed dense learned-matrix
storage at n=1,024. This experiment measures prediction fidelity, not a measured
memory or runtime saving at this size. Keeping a fixed number of history
coordinates during training is a different property.

Five existing moment tests and five new MNIST-runner tests passed. Independent
checks cover raw IDX data, split selection, preprocessing, autograd gradients,
noninitial moment/defect identities, initial tangency, own-state continuation,
and validation-image/label isolation. The independent saved-state check
reconstructs full physical matrices only in the audit, then reproduces train
and validation predictions and checks the exported metrics and scatter points.
The complete audit and exact hashes are in MNIST_CHECK.md. Numerical gate
failures above remain explicit even when implementation/metric checks pass.

## Artifacts and reproduction

All generated paths below are under
data/generated/neural_response_memory_20260922/:

- mnist_data01/prepared.npz and provenance.json: inputs, IDs, raw checksums.
- mnist_pilot01: retained pre-training failures; mnist_pilot02: successful pilots.
- mnist_primary01: eight primary runs, two-GPU launch receipt and logs.
- mnist_refined01: four predeclared extra numerical refinements.
- mnist_analysis02: final metrics_summary.json, CSV tables, paired scatter
  arrays, scatter_primary.png/pdf, rms_vs_order.png/pdf and loss/time plots.
- mnist_analysis01: preserved first-stage analysis before extra refinements.
- mnist_audit01: independent algebra, input, reconstruction and analysis checks.

From the repository root, use /home/amir/miniconda3/bin/python -B with
PYTHONDONTWRITEBYTECODE=1, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1,
MKL_NUM_THREADS=1 and CUBLAS_WORKSPACE_CONFIG=:4096:8. Source commands:

```text
python -B studies/neural_response_memory_20260922/prepare_mnist_moments.py --output <fresh-data-directory>
python -B studies/neural_response_memory_20260922/test_orthogonal_moment_engine.py
python -B studies/neural_response_memory_20260922/test_mnist_moment.py
python -B studies/neural_response_memory_20260922/run_mnist_campaign.py --phase primary --dataset <prepared.npz> --out <fresh-run-directory> --width 1024
python -B studies/neural_response_memory_20260922/mnist_moment_run.py --dataset <prepared.npz> --out <fresh-run-directory> --model moment --order 3 --width 1024 --device cuda:0 --rtol 1.25e-5 --wall-seconds 600
python -B studies/neural_response_memory_20260922/analyze_mnist_moments.py --dataset <prepared.npz> --runs <primary-directory> <refinement-directory> --output <fresh-analysis-directory>
```

The refinement command is repeated for moment orders 1, 2, 3 and dense
(`--model dense`); every actual command is preserved in its summary.json.
Use fresh output directories. No maintained code/docs or Git index changed.
Runner SHA256: a5d5b0f75b2ff99651737d0fa3ac7f344f9744beeba84e2f7265593dde964df3.
Analyzer SHA256: 061eff090b9b868edaeb77f7bc774ad1d4460eb95c4866f7168c4bbcb0736653.
