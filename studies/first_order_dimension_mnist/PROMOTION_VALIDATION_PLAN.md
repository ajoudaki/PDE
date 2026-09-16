# General-d p=1 candidate validation, precommitted 2026-09-16

Assembler `/root/author_a`. Scope: finite algebra/implementation and bounded
synthetic producer operation, not neural approximation on MNIST or PCA.
Scientific inputs: this study's initializer/theory and tensor/network engines;
established source-rule and H3 equation bodies; canonical finite-network oracle.

Competing implementation hypotheses: the cleaned APIs preserve the displayed
finite vector field and initialization; versus response, normalization, metric,
sign-law or serialization errors. Deterministic tests compare dense Cholesky,
sample-by-sample NumPy contractions, independent autograd and the canonical
finite-network oracle. Same-device identical-arithmetic restart must be bitwise.
All declared tests must pass. Float64 comparisons use atol 2e-12 / rtol 2e-11;
12-step float32/64 prediction uses atol 3e-6 / rtol 3e-4. Fixed seeds are in the
test source. Invalid arguments/mutations must reject; no parameter search.

Run one CPU and one CUDA suite after author corrections. Fixing a code bug can
trigger the affected suite again, but never a search for favorable cases. CPU
uses one numerical thread and 300 seconds wall; CUDA uses only cuda:1, one
worker, at most 4 GiB allocated, <=600 cumulative seconds wall including the
small example/replay; no MNIST training. Set CUBLAS_WORKSPACE_CONFIG=:4096:8,
disable TF32 and enable deterministic algorithms before constructing engines.
Test source imposes 0.15 device memory fraction (RTX3090: <4 GiB); external
wall timeout stops overruns. Retain all failed logs with their version hashes.

Example producer: synthetic d=3, m=9 finite data (including zero/nonunit and
correlated directions), n=P=16, seed=101, 10 simultaneous Heun steps at .005.
Output comparisons demonstrate API execution only: no threshold concerning
closure versus network accuracy is imposed or inferred. Repeat producer once
with the same options in a fresh directory; independent analyzer validates IDs,
metrics/Grams and exact repeat arrays. No other experimental branch authorized.

MNIST/PCA numerical claims are excluded. Selected historical original and PCA
full-horizon controls reportedly cost 45.52 and 35.74 summed GPU-process minutes.
A full maintained three-seed original/PCA reproduction, full controls and
analysis cannot responsibly be promised under this candidate's 10-minute GPU
validation allowance. Existing campaign drivers also depend on historical
study paths and pilot products. Cleaning that entire campaign is unnecessary
for the selected core library and is deferred with its numerical claims.
