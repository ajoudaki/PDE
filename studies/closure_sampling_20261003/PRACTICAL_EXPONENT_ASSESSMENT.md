# What the theorem does and does not determine about practical scaling

2026-10-04. Continuation of the same sampling investigation. This is a
deterministic numerical and algebraic assessment, not a new training campaign
or a new dense-to-compressed approximation theorem. The previous GPU campaign
remains closed. All calculations use this study's artifacts.

The new theorem makes the scaling architecture much clearer: source-space
accuracy, selection accuracy and dynamical stability are separate. It does
not identify the optimal practical exponent. In particular the previous
rank-16, ordinary weighted-gradient-flow sampler is not the theorem's
non-diagonal-metric, internal-residual, corrected-readout optimizer.

## The exponents actually supplied by the theorem

Use the notation of ERROR_PREFACTOR_REFINEMENT.md: original width n, input
dimension d, training count m, label RMS Y, initialized covariance gap gamma,
normalized gap lambda=min(1,gamma/m), and ell_n=log(en). The theorem assumes
Y<=c lambda and compares to the same realized dense flow uniformly over
physical time and the entire sphere. Its source coordinate tolerance is n^-1.

The depth-independent source construction has temporal degree bounded by
C lambda^-1 ell_n^(3/2)[ell_n+log(e/lambda)] and degree per input angle bounded
by C ell_n^(1/2)[ell_n+log(e/lambda)]. There is one temporal variable and d-1
angular variables. Their product yields

\[
R\le C\lambda^{-1}\ell_n^{d/2+1}
          [\ell_n+\log(e/\lambda)]^d,
\]

where R bounds the number of source directions per layer. The construction
selects O(R) neurons and stores O(R^2) fixed and moving coordinates, including
its metrics and caches. For n>=1/lambda, these **sufficient** powers are:

| Input domain | Ambient dimension d | Source/neuron power | Total-state power |
|---|---:|---:|---:|
| Circle | 2 | 4 | 8 |
| Sphere in R^3 | 3 | 5.5 | 11 |
| Sphere in R^5 | 5 | 8.5 | 17 |

The source/neuron power is (3d+2)/2, while the total-state power is 3d+2.
Neither is a lower bound. Replacing the old exponential error prefactor by
CY lambda^(-3/2) changes neither source tolerance nor these powers.

The powers expose the costs being paid: physical horizon proportional to
lambda^-1 log n, a worst-coordinate analytic radius proportional to
(log n)^(-1/2), logarithmic approximation accuracy in each analytic variable,
and a final squaring to store the small matrices/metrics. Choosing source
accuracy n^(-alpha) with a different fixed positive alpha changes the leading
accuracy-degree constant, not this power count. One needs a different
approximation argument or measured effective complexity to justify a lower
power, rather than merely a tighter error prefactor.

This assessment uses the complete INPUT_DEPTH_REFINEMENT.md,
STORAGE_QUADRATIC_IMPROVEMENT.md, ERROR_PREFACTOR_REFINEMENT.md and
ERROR_PREFACTOR_ASSEMBLY_CHECK.md as internally checked study inputs. It does
not independently re-audit their entire inherited stochastic-source chain.

## A new numerical check: previous labels versus the theorem's regime

For each of the twelve fixed experimental datasets, we computed the two-layer
tanh initialized population covariance recursively from Q^(0)=U U^T, using
two-variable Gaussian quadrature for each entry. Here U contains the unit
directions x_a/sqrt(d). We used Gauss--Hermite orders 64,128,256; all datasets
passed the predefined convergence checks. On the eight-point circle the
relative gap change from order128 to256 was 3.52e-10. A separate conditional
Gaussian parameterization reproduced the final covariance to 8.33e-16.
Degenerate correlations 0,+1,-1 were also checked. These are converged
numerical values, not interval-certified quadrature bounds.

| Geometry | gamma | lambda=gamma/m | Y/lambda |
|---|---:|---:|---:|
| 15-degree pair, either label sign | .00992737 | .00496368 | 20.15 |
| Four circle points, harmonic labels | .0127106 | .00317764 | 33.38 |
| Four circle points, smooth labels | .0127106 | .00317764 | 35.18 |
| Eight circle points, either tested labeling | .000157229 | .0000196537 | 5688.7 |
| Same eight circle points embedded in R^3 or R^5 | .000157229 | .0000196537 | 5688.7 |
| Four-point tetrahedron | .0205498 | .00513744 | 24.81 |
| Eight general sphere points in R^3, smooth | .00238988 | .000298734 | 276.0 |
| Same R^3 points, nonlinear labels | .00238988 | .000298734 | 270.8 |
| Eight general sphere points in R^5 | .0139494 | .00174368 | 40.05 |

All these ratios are much larger than a sufficiently small structural
constant. Thus the previous numerical labels cannot be justified as lying
in the theorem's small-label regime merely because their absolute values
are below .2. The numerical successes and failures remain observations about
those fixed-label flows; they are not tests of the theorem's guaranteed regime.

The embedded-circle covariance is unchanged because normalized input inner
products are unchanged. Their increased query-domain difficulty is therefore
not explained by a different population training gap. This separates training
conditioning from the complexity of predictions away from the training plane.
Different ambient dimensions still use different realized initializations and
setup probes, as disclosed in the experiment report.

For the eight-point circle, even the simplification n>=1/lambda asks for n
around 50881, above the tested 512--2048 range. The explicit size prefactor
lambda^-2 is about 2.59e9 before logarithms or unknown structural constants.
The theorem is an asymptotic sufficient existence result, not a numerically
usable state count for those previous tasks and widths.

Rescaling the labels into the theorem's regime while keeping an absolute
.15/sqrt(n) empirical tolerance could also make a zero predictor competitive
at these widths. A future small-label comparison must keep accuracy relative
to label scale or paired dense variability visible, so the target does not
become vacuous. No labels or error criteria were changed in this assessment.

## An initialization-only way to choose response rank

The saved sampler sources permit an exact finite-matrix diagnostic. In one
layer, let F collect the weighted initial source columns used by the
constructor: forward features, initial temporal responses and their mixer
partners. Each nonempty group of weight a contributes n*a^2 to ||F||_F^2
under the recorded column normalization. Let Q have orthonormal columns
spanning the training-priority vectors, and let sigma_j be the singular
values of (I-QQ^T)F in descending order. Both the group normalization and
these singular values are archived before training.

For a specified relative source tolerance tau, the minimum total dimension
among linear spaces containing those priorities and approximating this
particular finite source list in Frobenius norm is

\[
r(\tau)=\dim Q+
 \min\left\{k:\sum_{j>k}\sigma_j^2
                         \le\tau^2\lVert F\rVert_F^2\right\}.
\]

This formula follows directly by projecting onto the first k left singular
vectors. To see optimality within the stated subproblem, any orthogonal
rank-k projector P in the complementary space captures
tr(P C C^T), where C=(I-QQ^T)F. In an eigenbasis of C C^T, the diagonal
entries of P lie in [0,1] and sum to k. Their weighted sum is at most the
sum of the k largest eigenvalues. The discarded energy is therefore at
least sum_(j>k) sigma_j^2, with equality for the singular-vector choice.
This is only a finite linear approximation optimum, not an optimum for
the predictor or the autonomous dynamics.

We evaluated this formula using all70 successful baseline witnesses; the
two failed constructions remain missing. No new source computation or
training was used. As a diagnostic, set tau=1/sqrt(n). The median required
second-layer ranks are:

| Task | n512 | n1024 | n2048 |
|---|---:|---:|---:|
| Nearby pair, same labels | 13.5 | 16 | 19.5 |
| Nearby pair, opposite labels | 14.5 | 18 | 21 |
| Four-point harmonic circle | 19 | 22 | 24.5 |
| Eight-point smooth circle | 20.5 | 23 | 25.5 |
| Same circle embedded in R^3 | 38 | 47.5 | 56.5 |
| Same circle embedded in R^5 | 71.5 | 89.5 | 107 |
| Eight general sphere points in R^3, smooth | 38 | 48 | 60* |
| Eight general sphere points in R^5 | 75.5 | 96 | 115 |

Half-integers are medians of two integer ranks. The starred entry has one
successful witness because the other baseline constructor failed. In these
records the second layer also gives the larger rank requirement when the
two layers are compared at the same tolerance.

The result explains why a universal rank16 is a poor scaling policy for
this source representation. The rank can instead be selected from actual
initialization spectra. It also quantifies the dimensional change in source
complexity without running a training grid.

However, tau=1/sqrt(n) here is a **diagnostic source tolerance**, not a proved
sufficient prediction tolerance for the practical sampler. The theorem
requires uniform coordinate accuracy for entire moving source families,
whereas this calculation concerns weighted Frobenius accuracy on a finite
list of initial sources and32 setup probes. The latter does not control
unseen source directions, higher temporal responses, cubature defects or
feedback along training. For example rank24 already gave a good finite-time
output discrepancy in the R^3 diagnostic even though this stronger chosen
source tolerance asks for roughly57 directions. That difference must remain
visible; the table is not a proposed necessary neuron lower bound.

There is an additional exact reason not to interpret these ranks as an
optimal label-dependent budget. For positive global label rescaling
y->alpha*y, the initialized features and preactivations are unchanged,
the initial reverse sources delta'(0) and W0^T delta'(0) scale by alpha,
and h''(0), g''(0) and W0 h''(0) scale by alpha^2. Each source column in
the current constructor is then divided by its own RMS. Those factors
cancel exactly, so the normalized source matrix, its priority spaces and
the singular-tail rank diagnostic are unchanged in exact arithmetic, provided
no column crosses the numerical tiny-column cutoff. Thus this particular
diagnostic does not exploit smaller label amplitude at all. A practical
amplitude-sensitive selector must keep the sizes with which sources enter
future updates and predictions, instead of discarding those sizes during
normalization. The theorem's improved label-dependent error constant does
not automatically provide such a selector or its full-trajectory guarantee.

## What can be said about a practical exponent now

There are three separate practical choices:

1. Grow the source representation until its omitted forward and backward
   responses meet the desired source tolerance. Source rank should depend
   on the actual spectra and include directions beyond the training priorities.
2. Given those spaces, choose enough neurons for stable quadrature/metrics
   and both mixer actions. The selected neuron count N and source rank r are
   different parameters. A numerical equality-constraint failure is not a
   proof that N is too small.
3. Test the resulting autonomous predictor through fitting on separate
   initializations, with the requested output norm and numerical refinements.
   Initial source checks do not replace this step.

If a usable construction retains N proportional to the measured r, its
matrix storage is proportional to r^2. For descriptive purposes alone,
using the two extreme widths in the table gives the local proxy power

\[
p_{\rm proxy}=
 \frac{2\log[r(2048)/r(512)]}{\log[\log(2048)/\log(512)]}.
\]

It is 2.53 for the four-point harmonic circle, 2.17 for the eight-point smooth
circle, 3.95 for the embedded R^3 case, and 4.02 for the embedded R^5 case.
Across the other listed tasks it ranges up to about4.7. These values suggest
testing lower powers with adaptive rank rather than automatically increasing
the old exponent. They are **not fitted prediction-error exponents**: N=O(r)
at the needed practical accuracy has not been established for the ordinary
weighted sampler, the source tolerance is only a diagnostic, and the fixed
32-probe list eventually imposes an artificial finite-rank ceiling. The
additive training-priority rank further distorts a short-range power fit.

An operational practical optimum would minimize the complete retained count
over an explicitly specified construction family, tolerance, width range,
dataset collection and confidence level. The existing experiments supplied
budget schedules; they did not find the minimum successful count at each
width. Regressing those supplied counts simply recovers the exponent we
imposed. Also, the previous p=1/p=2 attempts had unresolved optimizer failures;
they were not excluded by valid prediction lower bounds.

Accordingly the current conclusions are:

- **Available internally checked sufficient theorem:** total powers8,11,17
  for d=2,3,5, with its exact optimizer, small-label condition, all-time
  supremum norm and eventual-width qualifications.
- **Available empirical sufficient rule:** p=4 on the earlier two-input
  circle suite for the practical weighted-gradient sampler. It is not
  established as optimal and did not transfer unchanged to all new tasks.
- **New numerical evidence:** a directly measurable adaptive-rank criterion;
  substantially different finite source ranks across circle/sphere tasks;
  previous labels well outside the theorem's small-label ratios.
- **Still open:** an optimal practical total-state exponent, or even a
  single validated sufficient schedule across the new multi-input tasks
  through their fitted endpoints. No exponent between2 and5 is newly
  certified by this analysis.

## Reproduction and check status

[PRACTICAL_EXPONENT_PROTOCOL.md](PRACTICAL_EXPONENT_PROTOCOL.md) was written
before the calculation. [assess_practical_exponents.py](assess_practical_exponents.py)
performed the 12 covariance calculations and140 layer-rank calculations in
2.04seconds. It has a120second CPU/wall limit and performs no training.
Tiny exact tail-selector tests and the independent Gaussian parameterization
check passed. The rank calculation also verifies that all resolved priority
directions were present before using the saved remainder singular values.
These are coordinator-performed internal numerical checks, not an independent
promotion review or a certificate for nonlinear prediction.

```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/closure_sampling_20261003/assess_practical_exponents.py --analysis data/generated/closure_sampling_20261003/gpu_multidata_20261004_final_analysis_checked --output data/generated/closure_sampling_20261003/practical_exponent_assessment_reproduction
```

Use a fresh output directory. The original output is
`data/generated/closure_sampling_20261003/practical_exponent_assessment_20261004/`,
including raw quadrature matrices at all three orders, all140 rank rows,
input/source hashes, source snapshot and the deterministic check result.
The separately persisted checker is
[check_practical_exponents.py](check_practical_exponents.py), with its command,
source snapshot and output in the corresponding `_check/` generated root.
No old sampler, training result, theorem, manuscript, maintained code or
Git state was modified. The output-norm preference question remains pending;
the new rank diagnostic and conditioning calculation are valid independently
of that choice. The practical experimental comparisons above retain their
original RMS norm, and the theorem retains its sphere supremum norm.
