# Deterministic Stieltjes proxy engine

This directory contains the offline, non-GPU half of the global-curve
experiment.  It consumes only already accepted exact MFP artifacts.  It does
not estimate new derivatives, simulate a network, fit a target trajectory, or
claim that a finite-width curve equals the formal mean-field object.

## Exact construction

For an accepted odd feature jet, `exact_series.py` reverses the feature series
over the rational numbers and obtains

\[
K(y)=A+y^2\sum_{r\geq0}(-1)^r\mu_r y^{2r}.
\]

`hierarchy.py` converts every prefix
\((\mu_0), (\mu_0,\mu_1),\ldots\) into the corresponding S-fraction
convergent.  With a true Stieltjes measure, odd prefix lengths are zero-Radau
upper bounds and even prefix lengths are Gaussian lower bounds.  The hierarchy
therefore adds exactly one accepted moment per level:

1. the zero-moment constant kernel (NTK/frozen-feature lower bound);
2. one-moment zero-Radau upper bound;
3. two-moment Gaussian lower bound;
4. three-moment zero-Radau upper bound;
5. and so on.

The implementation also emits the equal-information raw Taylor controls.
Those controls have no global ordering theorem and are not treated as the
primary hierarchy.

`curves.py` constructs feature and physical squared-loss curves by the
hitting-time maps

\[
S(y)=\int_0^y\frac{du}{K(u)},\qquad
T(y)=\int_0^y\frac{du}{2(y_*-u)K(u)}.
\]

The output coordinate is the primary comparison grid.  This avoids numerical
differentiation of output-versus-time and makes kernel, output, and loss
ordering transparent.

## Artifact-backed family inventory

`inventory.py` evaluates, at an explicitly supplied rational parameter point:

- the canonical one-input kernel (five moments);
- the normalized middle-weight variance homotopy (five moments);
- the relative block-metric output kernel and independent second-hidden
  companion observable (four moments each);
- two-input equal- and opposite-label physical channels (three moments);
- the centered-activation family (three moments);
- the independent hidden-block metric quadrant (four moments);
- the three-input equal-label equicorrelation channel (two moments).

Every result records the hashes of the checked source artifacts.  No automatic
parameter grid is present.  The opposite-label channel rejects its singular
physical endpoint \(t=1\).  The second-hidden companion is marked as not
driving training.  The normalized variance family records the physical target
\(z_*=1/\alpha\) for \(\alpha>0\); its \(\alpha=0\) Lambert-W boundary is a
singular exact calibration model, not a finite-target physical run.

## Exact variance-boundary calibration

`variance_boundary.py` implements

\[
\kappa_0(z)=36e^{W(z^2/9)/2}\bigl(1+W(z^2/9)\bigr)
\]

and its exact feature inverse.  `boundary_benchmark.py` compares every
available rational level and Taylor control against this global reference.
It is bounded by 2,001 output points and never launches itself on import.

## Hard implementation guards

- at most 10,001 points in a generic curve call;
- at most 2,001 points in the exact-boundary benchmark;
- exact parameter points only (binary floats are converted through their
  decimal spelling);
- domain checks for every family;
- failure on a negative or inconsistent S-fraction coefficient;
- no GPU, no subprocess, no exploratory grid, no result file written by the
  library;
- physical-time inversion refuses requests beyond a declared output cap.

The campaign-level runtime, width, replication, uncertainty, and branch
cutoffs belong in the frozen parent protocol, not in this reusable engine.

## Verification

From the repository root:

```bash
pytest -q studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy
```

The suite checks exact canonical and family-intersection regressions, the
variance boundary and canonical endpoints, the audited Gaussian/Radau atoms,
S-fraction nesting, loss-flow ordering, singular-endpoint guards, source
inventory completeness, and bounded calibration behavior.
