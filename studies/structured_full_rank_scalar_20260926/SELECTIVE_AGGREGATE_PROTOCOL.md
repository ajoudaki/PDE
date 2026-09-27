# Selective aggregate cutoff: bounded follow-up

2026-09-27. The user explicitly directs replacing the expensive uniform
degree cutoff with an informed selective cutoff, continuing the same
implementation experiment. Preserve the original degree-9 results.

## Mechanism

Keep all current output and feedback contractions, including every child
needed to evaluate the derivative of the forward-memory overlap. Add every
child in the output derivatives. For the two-input training-only problem,
these are only 100 contractions, compared with 37,996 in the uniform
degree-9 closure. The selected set includes some terms above degree 9;
it is selected for its role in the equations, not by total degree alone.

An implementation audit found that the 100-state selection still drops
direct hidden-Gram motion. The experiment therefore uses a stronger default:
retain the direct derivatives of all essential feedback constituents and
both hidden-layer Gram matrices as well. This gives 526 training-only states
with zero boundary, or 532 with gate calibration moments (98.6% fewer than
37,996). A further order can retain another output-derivative dependency
generation. The 100-state count is a diagnostic, not the tested main method.

The omitted derivatives remain an approximation. Compare explicit zero
boundary values with products of evolving core and gate moments. For the
latter, remove paired activation decorations while preserving the graph's
matrix edges, reconstruct using retained core and local gate moments, and
bound the result. If no retained core exists, record an explicit zero
fallback. Do not cut G/G-transpose edges into independent zero means.
The factorization neglects core--gate correlations and has no established
small-error guarantee. Larger selected sets add dependency layers.

## Quick screen

Retain n=1024, seed1, k4, P1, tanh, MSE stop0.01, float64, existing
Gaussian references. Count candidate states/terms before training. Evolve
passive circle outputs on 64 equally spaced angles in the scalar equations;
use the embedded 32-angle subset to check RMS quadrature sensitivity. There
is no Fourier approximation. Query states cannot affect training feedback.

First test the smallest selected set on pair_cos1 with the two boundary
rules. If a candidate fits with circle RMS <=0.1 versus Gaussian, test a
dependency enlargement and then the two existing three-input tasks. Broaden
to the three tasks before spending further effort optimizing one task.
Matched block-population controls isolate compression error from replacement
error. Primary metrics are raw circle RMS differences, with every endpoint's
actual MSE and fit status. Initial contractions use and then discard the
matched finite initial pool; only aggregates evolve.

Cap each compilation at60seconds,100000states,1000000terms; cap each
training at45seconds and physical time3000. Added training budget <=5minutes.
No extra seeds, width sweep, Fourier fit, or resource-heavy run. Preserve
failures; no substitution of a sampled population for scalar results.

Validate exact retained identities and separately measure the boundary
defect on nonzero physical states. Check scalar-only runtime and passive
query independence. A successful low-loss run alone is not evidence of
correct learned functions. Neither state-count savings nor finite-time
convergence of the older cutoff certifies this new boundary approximation.
