# Universal activation does not require data-uniform proof constants

User clarification, 2026-09-05: the activation must be independent of
the data, but all proof estimates may depend on the fixed input/label
configuration and finite physical horizon. This is the authoritative
interpretation of the ultimate target. It agrees with CONTRACT.md's
existing allowance of constants depending on the input pair.

The order of quantifiers is

    there exists ONE fixed nonlinear activation phi
    such that for every allowed fixed dataset D
    and every finite physical T,
    the full uncut joint population/GF/exact-GD theorem holds on [0,T],
    with finite constants C(phi,D,T) as needed.

No activation parameter may depend on D, T, width, mesh, cap, or the
realized training trajectory. The proved angle-specific theorem has
the weaker order: for every D, there exists epsilon(D)>0. It remains a
certified intermediate result, not the ultimate theorem.

In this project's notation rho=x_1^T x_2/d is the normalized inner
product, not the angle. Coincident RMS-unit inputs have rho=1; their
angle theta=arccos(rho) tends to zero as rho increases to one. Opposite
labels at exactly coincident inputs have no population training signal
at the prescribed zero readout: their equal features cancel in the
readout gradient, and the hidden gradients vanish. This excluded
degeneracy does not impose a uniform speed on distinct inputs.

## What may depend on data

Learning-signal lower bounds, initial hidden-acceleration lower bounds,
stability constants, response envelopes, required feature duration,
nonaffinity lower bounds on a fixed time interval, and convergence
estimates may all deteriorate as inputs coalesce. They need only have
the asserted finite or strictly positive value for each fixed allowed
dataset and fixed finite interval. No positive data-uniform infimum is
required. Zero population hidden velocity at t=0 from zero readout is
already allowed; the nonlazy obligation is genuine later hidden motion
and kernel change, as in the certified contract.

Data dependence does not remove the need for suitable width-, mesh-,
or auxiliary-cutoff-uniform estimates when passing those limits at FIXED
data and T. Nor does it make an infinite Gaussian moment finite. The
remaining analytic estimates must still justify the actual limit.

## Consequences for the route registry

1. The divergence of interpolation displacement and feature duration
   as opposite-label inputs coalesce, proved in UNIVERSAL_ANGLE_ROUTE.md,
   is a scaling observation, NOT an obstruction to the user target.
   A single short feature interval for all datasets is unnecessary.

2. Failure of an angle-uniform polynomial response envelope or of
   angle-uniform moments in QUARTIC_FINITE_ANGLE_BOUNDARY_LAYER.md is
   NOT an obstruction either. It excludes only that stronger estimate.
   In the exact zero-common-coordinate formula the fixed-angle bound
   is already at most (1+e)^((1-delta^2)/delta^2), where
   delta=sqrt((1-rho)/2)>0. This finite deterministic bound permits
   all moments at each fixed angle, despite divergence as delta tends
   to zero. This is only a local pure-channel observation, not control
   of the actual network forcing.

3. Driver-uniform local estimates are optional sufficient tools. A
   fixed-data, finite-time estimate with controlled driver dependence
   could equally close the theorem. Local arbitrary-forcing examples
   do not refute estimates using actual canonical network structure.

4. The genuine unresolved restriction in the certified perturbative
   theorem is epsilon<=epsilon_*(D), inherited from a smallness condition
   involving the data-dependent affine time and primal bounds. Growing
   proof constants are acceptable; forcing the activation parameter
   itself to shrink with data is not. A new proof may use data-dependent
   continuation intervals or constants with ONE epsilon fixed in advance.
   No data-uniform bound on those intervals/constants is being sought
   as a theorem obligation.

This clarification changes research prioritization, not any frozen proof
or audit hash. The ultimate universal-activation theorem remains open.
