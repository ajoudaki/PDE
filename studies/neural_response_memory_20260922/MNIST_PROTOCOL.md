# MNIST continuation: dense prediction versus response-history moments

Authorized 2026-09-24: repeat a two-digit MNIST comparison with 1000 total
training images, moment orders P=1,2,3, validation scatter plots and RMS
differences from the dense network. This continues the present method's
empirical testing; it does not reopen the circle or factor campaigns.

## Frozen scientific configuration

The maintained sources have no designated MNIST recipe. This is a fresh
reproducible instantiation, not a claim to reproduce unspecified earlier
MNIST scores. Select digits 3 and 8 before looking at results: 500 images
per class from the official training split, sampled without replacement with
NumPy seed 20260924. Use every 3/8 image of the official test split as the
held-out validation set. No validation image participates in training,
preprocessing estimation, stopping or parameter selection. Labels are -1
for 3 and +1 for 8. Flatten all 784 pixels and normalize each image to unit
Euclidean length, equivalently physical inputs with RMS one. No PCA,
whitening, augmentation, centering or feature selection. Preserve original
indices, downloaded-file checksums and prepared-array hashes.

Bias-free two-hidden-layer tanh, equal width initially n=1024, canonical
Gaussian initialization with stored variances (1,1/n,1/n^2), seed 20260924,
output divided by n, unhalved average squared loss and physical mobilities
(n,1,n). Dense and all closures share the exact initial weights and data.
Use the established study's moving-interval orthogonal moment equations,
P=1,2,3 (polynomial history degrees 0 through P-1), prefix length one,
retained actual W0 and transpose. Compute tanh responses from the current
weights/moments rather than numerically integrating redundant activation
coordinates; this is the same continuous closure on its invariant manifold.
No learned dense correction is retained or materialized in the closure RHS.

Primary observable: square root of the validation mean of
(closure prediction - dense prediction)^2. Scatter axes are dense prediction
and closure prediction, colored by digit, with the equality line. Report
training loss and classification accuracy separately as context. These do
not substitute for prediction agreement.

Save endpoints at training MSE .1, .03, .01, .003, .001. The primary matched
endpoint is the smallest of these levels reached by all four models at both
resolutions. Report every reached level, and explicitly report capped models.
If even .1 is not jointly reached, no fitted-endpoint claim is made. This
predeclared rule avoids favoring a closure with a different amount of fitting.
Also retain time/loss traces and dense-versus-closure endpoint stopping times;
own-loss comparisons are not same-physical-time trajectory comparisons.

## Numerical gates and resource boundaries

Full-batch gradient flow integrated by adaptive Heun with its embedded Euler
error estimate, float64, no Adam/SGD/momentum or factor optimization. Compare
rtol=2e-4 and 5e-5, atol=rtol/100. Component RMS scaling bounds integration
error without the prohibitive rank-squared factor-Gram calculation. Maximum
step 2, physical time 10000, 30000 steps, 600 integration seconds per primary
trajectory. Stop at MSE .001 or a cap, whichever comes first. Loss crossings
are located by 32 bisections of the accepted Heun step's second-order
continuous extension, using training loss only. This convention is checked
under tolerance refinement along with the trajectory.

Before primary runs, at most two 30-step/30-second throughput pilots at n=1024
on the fixed 1000-image training subset, one dense and one P=3. Pilots are
only for numerical performance, not scientific endpoint selection. If P=3
takes more than .5 seconds per Heun trial or peaks above 12 GiB allocated,
use n=512 for all primary runs; otherwise retain 1024. Record both pilot
results and the chosen width before comparing validation predictions.

Eight primary trajectories (four models, two tolerances) run across both
GPUs, maximum 4800 cumulative primary integration seconds. If a model reaches
an endpoint but its two-tolerance validation prediction RMS difference
exceeds .005 or 10% of the closure-dense discrepancy, permit one additional
refinement per affected model at rtol=1.25e-5, capped at 600 seconds, at most
four refinements. Numerical trend claims require margins resolved by observed
refinement changes; otherwise label inconclusive. Total cap is 7260 GPU
integration seconds including pilots, with no seed/configuration search.
Counters are checked between steps, so a final step can cause a small
recorded wall overshoot. Validation inference/analysis are separately timed.

Hypothesis tested: these low history orders approximate the dense predictor
on held-out images after substantial fitting, with improvement as P increases.
An RMS below .1 is the declared coarse practical agreement threshold for
labels +/-1, not a theorem. Resolved worsening, persistent large discrepancy,
or inability to fit is retained as adverse evidence. Invalid numerical
comparisons are inconclusive. One initialization and one digit pair cannot
establish a universal rate or population convergence.

The state contains 2*n*1000*P moment scalars. At the tested widths this need
not reduce total memory or effective rank relative to a dense middle matrix;
report actual storage/runtime rather than calling prediction agreement a
measured compression gain on this dataset.

## Ownership and validation

Root: this protocol, data preparation, analysis, README and results.
Scoped mnist_engine_plan agent: mnist_moment_run.py and test_mnist_moment.py.
An independent scoped check will verify the canonical gradient, initial
closure velocity, saved predictions/metrics and split isolation. Fresh run
directories and full source/data/environment provenance are required. No
changes to established code/docs or Git index, and preserve concurrent work.

## Feasibility decision, before primary comparison

mnist_pilot01 failed before initialization/integration: CUDA peak-memory reset
needed explicit lazy device initialization. The runner was corrected with
torch.cuda.set_device; failed logs are retained, and no trajectory was run.
The unchanged scientific configuration was rerun in mnist_pilot02. At n=1024,
30 accepted steps cost 1.75644 integration seconds for dense (2 rejected
trials), and 5.25007 seconds for P=3 (0 rejected), with CUDA allocated peaks
214404096 and 651211264 bytes respectively. P=3 cost .175003 seconds/trial,
so n=1024 is fixed for every primary run under the preregistered rule.
Runner SHA256: a5d5b0f75b2ff99651737d0fa3ac7f344f9744beeba84e2f7265593dde964df3.
The wall cap includes intermediate observation work and is therefore more
conservative than an integration-only cap; pure integration time is also
recorded. No pilot validation score was used to select the configuration.
