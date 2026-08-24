# Preregistration: hidden-neuron gauge-block gradient

**Frozen before generating the data described here:** 23 August 2026.

## Question

For middle neuron (j), simultaneous sign reversal of its incoming static
row and outgoing static column is an exact symmetry.  It conditionally
centers

\[
 F_j(t)=(\Gamma_2^*B_3(t))_j.
\]

Gaussian Poincare would prove a coordinatewise subexponential tail if the
Euclidean gradient with respect to the raw standard-Gaussian gauge block

\[
 \mathcal B_j=(\sqrt n\,\Gamma_{1,j:},
                \sqrt n\,\Gamma_{2,:j})
\]

has width-stable moderate moments.  This experiment estimates exactly that
block gradient by simultaneous random-direction finite differences.  It is
a mechanism diagnostic only: a pass cannot prove the signed reachable
tangent estimate, while a fail rejects its width-stable form.

## Frozen simulation

- Fully trained, bias-free, one-sample, three-hidden-layer arctan feature-time
  flow from the frozen core contract.
- Midpoint RK2, main step (h=0.01), horizons (1,2,4).
- Main widths/independent networks:
  ((256,64),(512,32),(1024,16),(2048,8)).
- Four independent paired Rademacher directions per network.  For neuron
  (j=0), perturb both blocks by

  \[
  \Gamma_{1,0:}\mapsto\Gamma_{1,0:}\pm\varepsilon v_1/\sqrt n,
  \qquad
  \Gamma_{2,:0}\mapsto\Gamma_{2,:0}\pm\varepsilon v_2/\sqrt n,
  \]

  with (arepsilon=0.002), and fully retrain every copy.
- Estimate each directional derivative by the central difference of the
  **static** query (F_0=(\Gamma_2^*B_3)_0), using the correspondingly
  perturbed initial static column rather than the current trained column.
  The square root of the four-direction mean square is the block-gradient
  estimator (G_{\rm gauge}).
- Paired numerical audits at widths 256 and 512 use eight networks:
  (h=0.005,arepsilon=0.002); then (h=0.005,arepsilon=0.001);
  then common-draw float64 at the latter settings.

Record (G_{\rm gauge}), the analogous outgoing-column-only and
incoming-row-only directional derivatives using the same trained paired
copies and the two summands of the simultaneous direction, and the query
(F_0).  The component derivatives are obtained in separate paired copies;
they are descriptive and do not alter the main gauge verdict.

## Numerical validity

At every audited width and horizon, relative RMS differences of
(G_{\rm gauge}) between coarse/fine and full/half epsilon must be at most
5 percent, and float32/float64 differences at most 2 percent.  An absolute
RMS difference below (10^{-6}) also passes.  A failed horizon is not
interpreted until rerun at half step.

## Frozen interpretation

Use 2,000 network-cluster bootstrap resamples.  Fit log--log width slopes to
the network medians of (G_{\rm gauge}), and fit the moment-growth exponent
from orders (2,4,6,8) after pooling the independent networks at each width.

Formal support requires at horizons 2 and 4:

1. the upper 95-percent confidence endpoint of the gradient width slope is
   below (0.15);
2. the upper endpoint of the fitted gradient moment exponent is below
   (0.75) at every width; and
3. the width-2048 median is at most (1.25) times the width-256 median.

Formal evidence against requires at one numerically valid horizon:

1. the lower endpoint of the gradient width slope exceeds (0.30); and
2. the width-2048 median exceeds (1.35) times the width-256 median.

All other outcomes are inconclusive.  The result changes no theorem rung by
itself.
