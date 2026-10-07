# Core analysis: what can and cannot currently be proved

## 1. Baseline being challenged

For one fixed admissible task, the integrated compact construction retains

\[
O\!\left([\log(en)]^{3d+2}\right)
\]

real coordinates and has uniform-in-time, uniform-on-the-sphere error
`n^{-1+o(1)}`.  Its selected width is

\[
O\!\left([\log(en)]^{3d/2+1}\right).
\]

The exponent comes from a joint time--sphere spectral approximation and
then from storing dense reduced mixers.  In the source count, the sphere
contributes all harmonics through a cutoff proportional to `log n`, the
proved complex query radius costs an additional square-root logarithm in
each angular direction, and the time coordinate contributes another
factor.  Squaring the selected width produces the displayed storage.

This explains the upper bound.  It does not prove that any of these costs
is necessary for an actual trained-network trajectory.

## 2. A rigorous analytic-class barrier

The following elementary lower bound isolates the genuine dimensional
obstruction without claiming that trained trajectories fill the required
function class.  Its analytic neighborhoods are fixed, bounded, and
independent of width and requested accuracy.

Assume `d >= 2` and fix an integer `p`.  The spherical polynomials of
degree at most `p` form
a space of dimension

\[
D_p={p+d-1\choose d-1}+{p+d-2\choose d-1}.
\]

Here and below the positive constant in `exp(-a p)` is a local analytic-
radius constant.  Suppose a class of trajectories contains, at one common
time, every function on the normalized-`L^2` sphere of radius
`exp(-a p)` in this space.  If a
continuous encoder into `q` real coordinates and any decoder approximate
every member with error strictly below `exp(-a p)`, then

\[
q\ge D_p.
\]

Indeed, if `q < D_p`, Borsuk--Ulam gives an antipodal pair with the same
code.  Both members therefore have the same reconstruction, and the
triangle inequality says that one of the two errors is at least the
radius.  The same argument applies to complete trajectories because
evaluation at the common time cannot increase the trajectory norm.

The trajectory supremum controls normalized `L^2`, so the conclusion also
holds when approximation is measured by the requested sphere supremum.
Taking `p` proportional to `log(1/error)` gives

\[
q\ \gtrsim_d\ [\log(1/\text{error})]^{d-1}.
\]

At error `1/(sqrt(n) log(en)^(5/2))`, this becomes a lower bound of order
`log(n)^(d-1)`.

For a full **space--time** analytic ball, use the `p` modes
`exp(-k t)-exp(-(k+1)t)`, `1 <= k <= p`, which vanish both at initial
time and at the fitted limit,
tensored with the same spherical polynomials.  The embedded sphere then
has dimension

\[
pD_p\asymp_d p^d.
\]

The identical antipodal argument gives

\[
q\ \gtrsim_d\ [\log(1/\text{error})]^d.
\]

Thus a continuous-encoder compressor for a full unit ball on those fixed
analytic neighborhoods cannot improve the logarithmic exponent from `d` to
`o(d)`.  The
spatial-only statement already gives exponent `d-1`, which is still linear
in dimension.  The time modes can share the network's zero initial
prediction and common endpoint, so those two boundary conditions do not
remove this generic-class obstruction.

This result already allows nonlinear decoding and needs only continuity of
the encoder in the real-domain supremum norm.  A Lipschitz or
well-conditioned representation is therefore also covered.  For an
autonomous model, all trajectory-dependent
coefficients of its vector field and decoder must be part of the code;
its initialization map must also satisfy the stated continuity requirement.

## 3. Why that theorem is not yet a network lower bound

The needed premise is not known for the reachable trajectories of the
dense training system.

Full input rank says that the correlations with the training inputs retain
all query directions.  It does **not** say that training independently
controls every spherical-harmonic coefficient.  Nonlinearity and moving
hidden features likewise do not imply that the reachable set contains a
high-dimensional ball.

For fixed data, labels and activations, the deterministic infinite-width
trajectory is one structured object, not an analytic ball.  Typical
finite-width randomness is only of order `1/sqrt(n)`.  At the requested
error, a packing made solely from that fluctuation would need lower bounds
on many angular covariance eigenvalues.  The integrated variability proof
establishes one nonzero direction; it supplies neither the required
high-dimensional packing nor lower spectral tails.  Consequently it
cannot be amplified into the bound in §2.

The exact missing statement is:

> For harmonic degree proportional to `log n`, the high-probability set of
> reachable dense trajectories must contain, or stably project onto, a
> ball of dimension comparable to `log(n)^(d-1)` and radius at least the
> requested comparison error.

No current argument proves this.  For initialization fluctuations the
radius of high harmonics is expected to decay with the activation's
spectrum, so the statement may actually be false at degree proportional
to `log n`.

## 4. Why unrestricted coordinate lower bounds are impossible

The existing storage theorem counts explicit numerical arrays in a fixed
compact-network architecture.  If a proposed new representation may use
an arbitrary decoder, a coordinate count alone is not an information
measure:

- one infinite-precision real can encode an arbitrary finite array;
- a task-specific decoder can hard-code a single trajectory;
- an uncounted program can recompute a very large spectral expansion using
  small working memory and unbounded time;
- a fixed low-dimensional autonomous ODE can simulate complicated digital
  computations if its coefficients and conditioning are unrestricted.

Therefore a general impossibility theorem must count decoder description
and precision, or impose a continuous/Lipschitz encoder--decoder with
bounded conditioning and a uniformly described autonomous vector field.
Without such a contract, neither `log(n)^d` nor any other positive lower
bound is mathematically meaningful.

## 5. Constructive routes and their present failure points

### Correlation coordinates

Writing a query through its correlations with the training inputs does not
reduce dimension when the inputs span `R^d`; it is merely an injective
change of coordinates.

### Sparse grids

Sparse grids beat a full tensor count only with mixed-regularity or
anisotropy estimates.  The current proof supplies isotropic strip
analyticity and no dimension-uniform coordinate weights.  Full-rank
general data provide no missing mixed-smoothness estimate.

### Tensor or separated harmonics

A tensor-train construction would work if all source fields had ranks
`log(n)^o(d)` throughout training.  Neither initialization nor the
nonlinear updates preserve such a rank in the current proof.  Assuming it
would add precisely the structural restriction that the question forbids.

### Structured mixers

Replacing dense reduced mixers by structured or low-rank maps could remove
the square in storage.  Even a successful version would leave the present
selected-width exponent proportional to `d`; it cannot by itself establish
`o(d)`.

### Mean trajectory plus fluctuations

In principle one could compute the deterministic feature-learning limit
procedurally and store only finite-width fluctuations.  To make this a
theorem here would require all of the following, none of which is in the
integrated result: a mean-field limit for this exact deep scaling, a
quantitative trajectory-level fluctuation expansion uniform on the sphere
and through the endpoint, spectral decay and truncation bounds for the
fluctuation, and a finite autonomous realization of the nonlinear limit
whose complete numerical state is counted.  Existing shallow or
different-scaling mean-field theorems do not supply those interfaces.

## 6. Current verdict

There is no proved `log(n)^o(d)` autonomous compression for the stated
general setting.  There is also no valid lower bound excluding it for the
actual reachable dense trajectories.

What is proved here is the sharp logical boundary:

1. a full unit ball on fixed bounded joint analytic neighborhoods has an unavoidable
   `log(1/error)^d` state dimension for every continuous encoding; even a
   single-time analytic class requires `log(1/error)^(d-1)`, so analyticity
   alone cannot yield the requested exponent;
2. transferring that obstruction to trained dense networks requires a
   high-dimensional reachability/packing theorem that is currently absent;
3. every plausible constructive escape requires a new low-rank,
   mixed-regularity, or mean-field-closure invariant that is likewise
   absent from the existing proof.

Accordingly, claiming either the desired compression or its impossibility
would presently overstate the mathematics.
