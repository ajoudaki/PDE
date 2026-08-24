# Preregistration: causal susceptibility-trace diagnostic

Frozen before inspecting any output from this experiment.

## Mathematical target

Run the exact feature-time Euler flow from the frozen contract.  Add an
external vector forcing `F[k]` only to the middle adjoint field used by the
lower update,

\[
 R_2^k\longmapsto R_2^k+F^k
\]

in \(B_2^k=D_2^k(R_2^k+F^k)\), while allowing all later lower and upper
states to respond normally.  At \(F=0\), define

\[
 J_{m\ell}=D_{F^\ell}X_2^m,
 \qquad
 \kappa_{m\ell}=n^{-1}\operatorname{Tr}J_{m\ell}.
\]

Because one Euler impulse contains a factor \(h\), the continuum row-total
variation diagnostic is

\[
 V_{n,h}(T)=\sum_{\ell<m}|\kappa_{m\ell}|,
 \qquad m=T/h,
\]

not \(h\sum|\kappa|\).  This is the empirical counterpart of the extra
row-cavity susceptibility isolated after deleting a top row.  It includes
all subsequent transpose reuse through the other top rows; it is not a
frozen-lower response.

For independent Rademacher vectors
\(\gamma_q\in\{\pm n^{-1/2}\}^n\), estimate

\[
 \kappa_{m\ell}^{(q)}
 =\gamma_q^T J_{m\ell}\gamma_q
\]

by reverse automatic differentiation, average over probes before taking
absolute values, and report also probe-split estimates.

## Frozen runs

- activation: unscaled arctangent;
- feature-time Euler, no label or physical clock;
- iid canonical Gaussian initialization;
- horizons \(T\in\{1,2,4\}\);
- main mesh \(h=0.02\), widths \(n\in\{128,256,512\}\);
- refinement meshes \(h=0.01\) at \(n\in\{128,256\}\), and \(h=0.005\)
  at \(n=128\);
- at least 8 probes per orbit and enough independent orbits to obtain at
  least 64 probe-orbit blocks at each main width (resource permitting);
- float32 main runs; common-draw float64 checks at \(n=64,128\);
- centered finite-difference checks for two impulse times on at least four
  small orbits.

Increasing replicas or probes and adding larger widths is allowed, but the
statistics and verdict thresholds below may not be changed.

## Recorded statistics

For each orbit and endpoint:

1. \(V=\sum_\ell|\bar\kappa_\ell|\), where the bar averages probes;
2. signed mass \(S=\sum_\ell\bar\kappa_\ell\);
3. positive and negative variations \(V_+,V_-\);
4. \(\max_\ell|\bar\kappa_\ell|/h\);
5. first-half/second-half probe estimates of every statistic;
6. the direct one-step coefficient \(\bar\kappa_{m,m-1}/h\);
7. solver replay, centered finite-difference, and float32/float64 errors.

The analysis uses medians over orbits, cluster bootstrap confidence intervals
with the orbit as cluster, log-width slopes, and paired mesh ratios whenever
the common seed is available.

## Frozen interpretation

The experiment gives **formal support** to the susceptibility-TV premise if:

1. every numerical audit is within 5 percent relative error (or \(5\times
   10^{-4}\) absolute near zero);
2. at \(T=2,4\), the upper 95-percent endpoint of the log-width slope of
   median \(V\) is below 0.15;
3. at fixed width, the upper 95-percent endpoint of the fitted divergence
   exponent in \(V\propto h^{-\alpha}\) is below 0.20;
4. the median half-probe discrepancy in \(V\) is below 15 percent and its
   95th percentile below 35 percent.

It gives **formal evidence against** that premise if a numerical audit passes
but either the lower 95-percent endpoint of a width slope exceeds 0.25 or the
lower 95-percent endpoint of a mesh-divergence exponent exceeds 0.35.

The sign statistics are mechanism diagnostics only.  Predominantly positive
mass favors a passivity/monotonicity route; substantial stable cancellation
favors a signed Dyson/Abel route.  Neither sign outcome proves a theorem.

No experimental verdict changes C3--C5.  Even formal support leaves the
uniform causal response lemma and its row-cavity approximation to be proved.
