# Can the logarithmic exponent be made sublinear in dimension?

## Answer

**Not with any result currently proved.**  Under the exact requested scope,
there is presently neither

1. a construction with total retained size
   \[
   C_{\rm task}[\log(en)]^{r(d)},\qquad r(d)=o(d),
   \]
   nor
2. a lower bound proving that such a construction is impossible for the
   trajectories actually reached by the dense training dynamics.

The current integrated construction remains the best proved autonomous
result: its error is `n^{-1+o(1)}` in the complete time--sphere norm and its
all-retained storage is

\[
O_{\rm task}([\log(en)]^{3d+2}).
\]

This study proves a **conditional barrier** and identifies the exact
missing network theorem.  It does not replace the integrated result.

## Canonical target

Here `n` is dense width, `d` is input dimension, `m >= d` inputs span
`R^d`, and fixed depth satisfies `L >= 2`.  All existing activation, gap,
and label assumptions are retained.  The compact model must be autonomous,
restartable, nonlinear, and must evolve hidden features; a frozen kernel or
stored playback does not qualify.

To make “at the dense self-variability level” unambiguous, the study uses
the stronger proved lower scale, up to fixed-task constants:

\[
\frac{1}{\sqrt n[\log(en)]^{5/2}}.
\]

This guarantees a comparison at or below a discrepancy that is known to
occur between independent dense runs.  The exact dense variability is only
bracketed between this scale and `n^{-1/2+o(1)}`; it is not known sharply.

## What is now proved

For the full unit ball that is bounded and holomorphic on fixed bounded
complex neighborhoods of time and the sphere, every continuous encoding
into real coordinates that reconstructs the class to error `epsilon` needs
at least

\[
c[\log(1/\epsilon)]^d
\]

coordinates.  At the target above, this is

\[
c[\log n]^d.
\]

Here the positive constant depends on dimension and on the two fixed
complex neighborhoods, but not on `epsilon` or `n`.

The proof uses only one local integer degree.  Spherical harmonics through
that degree contribute order `degree^(d-1)` independent directions.  The
complete trajectory contributes one further factor of `degree` from
independent analytic time modes.  Their tensor product has order
`degree^d` directions.  An
analytic ball contains a sphere of radius exponentially small in the
degree.  Borsuk--Ulam then says that a continuous encoder with fewer
coordinates identifies an antipodal pair, forcing error at least that
radius.

The same argument at one fixed time gives the spatial lower bound
`c log(1/epsilon)^(d-1)`.  Hence an exponent proportional to dimension is
unavoidable for a generic analytic class.  Better use of analyticity alone
cannot produce `r(d)=o(d)`.

If one uses the smaller time and query radii actually proved for the dense
source fields, the same ambient-class calculation gives
`log(n)^(3d/2+1)`, exactly the exponent of the existing selected source
rank.  Thus that source-mode count is sharp for the surrounding analytic
ellipsoid.  This does **not** prove that the ellipsoid is reachable, and it
does not make the subsequent quadratic mixer storage necessary.

The complete proof, including zero initial value and a common fitted
endpoint, is in [ANALYTIC_BARRIER_PROOF.md](ANALYTIC_BARRIER_PROOF.md).

## Why this is not yet the requested impossibility theorem

The dense trajectory set may be much smaller than a full analytic ball.
The assumptions currently prove regularity of each trajectory, but not
independent control of all of its harmonic coefficients.

- Full input rank preserves all query directions; it does not create a
  high-dimensional packing of reachable predictors.
- Nonlinear feature learning changes the features; it does not by itself
  make all analytic directions reachable.
- The dense variability lower bound proves one nondegenerate fluctuation
  direction.  A storage lower bound needs exponentially many separated
  trajectories, or an embedded ball with dimension of order `log(n)^d`.
- There is also an amplitude mismatch.  Typical finite-width variation is
  of size `1/sqrt(n)`.  Relative to the chosen target, this leaves only a
  `log(n)^(5/2)` resolution factor, whose logarithm is `log log n`.  Without
  an order-one reachable family, a spectral packing naturally gives powers
  of `log log n`, not the required powers of `log n`.
- A packing made from rare or zero-probability initializations would not
  contradict a compressor that succeeds with probability `1-delta`.

The missing negative-result lemma is therefore precise: on a set of dense
initializations of nonnegligible probability, prove a stable packing of
complete trajectories large enough to carry order `log(n)^d` independent
coordinates at the target error.  No current proof or located paper gives
this lemma.

The existing dense lower does rule out one degenerate proposal: one
initialization-independent, task-only trajectory cannot approximate two
independent dense runs below a sufficiently small multiple of their proved
separation.  This shows that some initialization-dependent information is
necessary, but gives no lower bound growing with `n`.

## Constructive routes checked

No route produced the requested construction.

- **Training-input correlations:** because the inputs span `R^d`, these
  correlations are an injective reparameterization, not a dimension
  reduction.
- **Sparse grids:** they require mixed anisotropy or coordinate weights.
  The current hypotheses give only isotropic analytic control.
- **Tensor or separated harmonics:** they would work only after proving a
  sublinear-in-`d` rank bound preserved by nonlinear training.  No such
  invariant is available.
- **Kernel-section closure:** the predictor velocity is exactly a sum of
  `m` evolving tangent-kernel sections, but differentiating those sections
  opens an unclosed hierarchy of feature and response fields.  Freezing
  them would be the forbidden kernel approximation.
- **Structured compact mixers:** this could remove some quadratic storage,
  but the only exact simplification found is that each mixer velocity has
  rank at most `m`.  Its time integral can have full rank as those rank-one
  directions rotate.  Even a hypothetical linear-cost mixer would leave
  the current selected width with a logarithmic exponent proportional to
  `d`, so it cannot by itself reach `o(d)`.
- **Mean trajectory plus finite-width fluctuation:** this is the only route
  that might genuinely evade the generic analytic count.  It would require
  a quantitative mean-field and fluctuation theory for this exact deep
  scaling, uniform over the whole sphere and all training times, followed
  by a finite autonomous realization whose complete state is counted.
  Existing results do not provide that chain.

## Why the lower-bound interface must be stable

An unrestricted count of exact real coordinates has no lower-bound
content: one real can encode an arbitrary finite table, and an uncounted
task-specific decoder can hide the whole trajectory.  Any valid general
lower bound must therefore use a continuous or quantitatively Lipschitz
encoder/decoder with controlled conditioning, or explicitly count bits and
decoder description.  All task- and initialization-dependent metrics,
bases, mixers, programs, and fixed coefficients must be included in total
storage.

This is consistent with stable-manifold-width theory; it is also why a
generic entropy calculation cannot simply be called a neural-network lower
bound.

## Final claim boundary

The proven conclusion is:

> Uniform control of a full fixed-neighborhood analytic ball has a
> `log(1/error)^d` trajectory barrier, so any successful
> `log(n)^o(d)` construction must exploit a new structural property
> specific to reachable nonlinear feature-learning dynamics.

Whether such a property exists, or whether reachable trajectories instead
contain the required high-dimensional packing, remains open.  Claiming
either the desired construction or its impossibility under the full stated
scope would currently overstate the mathematics.

Proof and audit map: [analytic barrier](ANALYTIC_BARRIER_PROOF.md),
[independent check](ANALYTIC_BARRIER_CHECK.md),
[lower-bound route](LOWER_BOUND_ROUTE.md),
[constructive route](CONSTRUCTION_ROUTE.md), and
[representation/literature audit](LITERATURE_AND_CONTRACT.md).
