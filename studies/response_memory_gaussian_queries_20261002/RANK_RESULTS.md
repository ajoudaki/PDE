# Initial online query-span screen

All four tested paths **fail the preregistered resource gate**: combined online
forward and adjoint ranks at RMS tolerance 0.001 exceed n/8=256. Feature learning
is substantial and retained-space matrix-action errors satisfy the error gate.
This rejects the proposed small-rank budget at n=2048 on these paths; it does
not establish proportional growth with width or exclude a useful larger-width
regime. No approximate Gaussian-oracle trajectory was simulated here.

The frozen protocol is `RANK_PROTOCOL.md`; raw summaries, logs, inputs and the
exact executed producer are in
`data/generated/response_memory_gaussian_queries_20261002/rank_screen01/`.

| Dataset | q | Forward rank | Backward rank | Sum / n | Final training MSE | Max feature motion, layer 1 / 2 |
|---|---:|---:|---:|---:|---:|---:|
| Circle | 1 | 212 | 298 | 0.249 | 0.31755 | 0.4649 / 0.4842 |
| Circle | 3 | 221 | 317 | 0.263 | 0.26134 | 0.4772 / 0.4776 |
| Sphere | 1 | 309 | 397 | 0.345 | 1.14e-8 | 0.3798 / 0.4207 |
| Sphere | 3 | 307 | 393 | 0.342 | 3.29e-9 | 0.3763 / 0.4244 |

Motion is the RMS over all training samples and neurons relative to initialized
activations, maximized over observed times. Both layers exceed the required
0.05 in every case. Every run uses the same canonical nonlinear architecture,
zero readout, n=2048, seed 1771, physical horizon 80 and Heun step 0.05. The
sphere data seed is 8841; exact arrays are saved in each `*_inputs.npz`.
The circle remains poorly fitted at the prescribed horizon; the sphere is
almost fitted. Neither fact changes the precommitted rank threshold.

![Combined retained ranks](../../data/generated/response_memory_gaussian_queries_20261002/rank_screen01/rank_primary.png)

## Action errors and numerical checks

For a current query v, the measured residual is v-Pv in the corresponding
never-forget basis at that query. The action error is ||W_0(v-Pv)||/sqrt(n)
for forward queries and ||W_0^T(v-Pv)||/sqrt(n) for backward queries.
This diagnostic uses the actual initialized matrix, rather than assuming that
adaptively selected residuals retain an independent Gaussian law.

| Dataset | q | Maximum forward action error | Maximum backward action error | Sum of ranks at tolerance 0.0001 |
|---|---:|---:|---:|---:|
| Circle | 1 | 0.0011932 | 0.0013004 | 349 + 476 = 825 |
| Circle | 3 | 0.0011933 | 0.0013004 | 367 + 499 = 866 |
| Sphere | 1 | 0.0011784 | 0.0011424 | 485 + 597 = 1082 |
| Sphere | 3 | 0.0011784 | 0.0011232 | 482 + 588 = 1070 |

All primary action errors are below the frozen 0.005 threshold. At tolerance
0.0001 the largest action error is 0.0001284. Final orthonormal-basis Gram
errors are at most 9.54e-7 entrywise across all monitors, below the 1e-4 gate;
all saved raw states were finite. Float64 dense reconstruction, autograd
first-layer/readout velocities, prefix reconstruction derivatives (including
a nonzero-readout check), and independent synthetic integral-moment derivatives
agree within 3.78e-15, below the 1e-10 gate. GPU arithmetic was float32 with
TF32 disabled. The small algebra checks verify normalization and transcription;
they do not establish trajectory accuracy of this timestep or closure order.

The monitor observes completed timesteps, not Heun predictor queries. The
conditional predictor audit required all four cases to pass, so it was not
run. No timestep refinement or dense-training comparison was performed. The
claim is about these discretized response-memory trajectories, not a verified
continuous-time or population limit.

## Normalized variation and resource implications

For each sample a and observed times t_j, define its normalized sampled
variation as sum_j ||v_a(t_j)-v_a(t_(j-1))||/sqrt(n). Summing over samples gives
V. Since every accepted sample query is retained forever, all acceptances
after that sample's first one can be charged to disjoint path segments of
variation exceeding the tolerance. Thus the sampled rank obeys
rank <= min(n, m+V/tolerance), in exact arithmetic.

| Dataset | q | Forward V | Backward V |
|---|---:|---:|---:|
| Circle | 1 | 6.3483 | 30.6135 |
| Circle | 3 | 6.6700 | 31.1348 |
| Sphere | 1 | 9.9824 | 35.8422 |
| Sphere | 3 | 9.8650 | 34.4655 |

At both tolerances these generic bounds saturate at n=2048 for each direction;
they do not explain a small span. The measured ranks are much smaller than
that bound but larger than the frozen budget. These discrete variations do
not upper-bound unobserved continuous-time excursions.

The actual screen retains dense W_0, using n²=4,194,304 fixed-source scalars.
A prospective oracle retaining query bases and their output images requires
about 2nR scalars, where R is the sum of the two ranks, plus cross coefficients
and workspace. The following optimistic arithmetic proxy only counts observed
queries: dense actions use 2n²K floating-point operations for K vector queries;
basis coefficient/action pairs use about 4n times the sum of retained rank
before each query. Sampling, orthogonalization, new constraints, predictor
queries, and closure moment updates are additional work.

| Dataset | q | 2nR / n² | Basis-action proxy / dense-action work |
|---|---:|---:|---:|
| Circle | 1 | 0.498 | 0.126 |
| Circle | 3 | 0.525 | 0.131 |
| Sphere | 1 | 0.689 | 0.297 |
| Sphere | 3 | 0.684 | 0.296 |

These ratios are prospective, not measured speedups. They leave only modest
fixed-source storage savings at this width before adding cross coefficients.
They do not determine how ranks scale with width. The baseline failure therefore
leaves that separate scaling question open; it does not justify declaring the
whole oracle approach impossible.

## Reproducibility and artifact defect

Run commands, from `/home/amir/Codes/PDE`, were:

```bash
PYTHONPYCACHEPREFIX=/home/amir/Codes/PDE/data/generated/response_memory_gaussian_queries_20261002/pycache /home/amir/miniconda3/bin/python studies/response_memory_gaussian_queries_20261002/rank_screen.py --validate-only
PYTHONPYCACHEPREFIX=/home/amir/Codes/PDE/data/generated/response_memory_gaussian_queries_20261002/pycache /home/amir/miniconda3/bin/python studies/response_memory_gaussian_queries_20261002/rank_screen.py --dataset circle --device cuda:0
PYTHONPYCACHEPREFIX=/home/amir/Codes/PDE/data/generated/response_memory_gaussian_queries_20261002/pycache /home/amir/miniconda3/bin/python studies/response_memory_gaussian_queries_20261002/rank_screen.py --dataset sphere --device cuda:1
```

Both GPUs were RTX 3090s, previously idle apart from small resident desktop/audio
allocations. Environment JSON files contain Python, Torch, NumPy, CUDA, device,
timestamps and source/protocol hashes. The two dataset processes took about
17.3 and 19.2 seconds of measured case time: roughly 36.5 additive GPU-process
seconds, well below the 10 GPU-minute/20 wall-minute cap. This is screen runtime,
not a deferred-oracle benchmark.

An output-filename defect was found after completion: `Path.with_suffix` treated
the decimal point in the tolerance as a suffix separator, so detailed per-query
JSON and basis arrays were overwritten between monitors within each case.
The final backward monitor at tolerance 0.0001 survives in `*_0.json` and
`*_0.basis.npy`. Every independent `*_summary.json` remains complete: it stores
all monitors' ranks, all accepted directions' times/sample indices/innovation
norms, action-error maxima, variations, orthogonality and work counts. Therefore
the reported metrics and rank curves are unaffected. Primary per-query error
traces and primary basis vectors are unavailable. No replacement experiment
was run. The exact original source is archived as `rank_screen_executed.py`;
subsequent producer repairs must not be mistaken for the executed source.

Evidence level: internally checked numerical screen, one seed/two datasets;
no promotion, external review, trajectory convergence, or operational
large-width advantage is claimed.
