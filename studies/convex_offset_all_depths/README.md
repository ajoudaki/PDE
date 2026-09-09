# Literal convex activation at all finite depths

The full global trained-limit theorem for one fixed literal convex
activation has not been proved in this investigation.

The [self-contained report](REPORT.md) proves a precise obstruction
to transferring the gain-based argument. For every bounded
normalized C2 shape and every fixed mixing coefficient in
\((0,1/2)\), pairwise initialized feature distances contract
exponentially with depth. The smallest eigenvalue and the
smallest-to-largest eigenvalue ratio of the initialized population
raw kernel consequently tend to zero.

For example,
\[
 \phi(z)=\tfrac34(1+z)+\tfrac1{16}\arctan z
 \quad\left(\varepsilon=\tfrac14,\ \psi=\tfrac14\arctan\right)
\]
has contraction factor \(13/16\), giving
\[
 \lambda_{\min}(K_L(0))
       \le(1-\Gamma_{ij})(13/16)^{2L}.
\]

This rules out a positive initialized kernel floor uniform in
depth. It does not rule out global convergence at each finite
depth with depth-dependent rates.

Both fresh final isolated reviews PASS the exact report:
[review record](REVIEW_SUMMARY.md). Their scope is explicitly
limited to the proved obstruction, not the global trained target.

The [positive-route investigation](development/POSITIVE_ROUTE_INVESTIGATION.md)
records working local extensions and the unsuccessful global
closure attempts. It is a development document, not an additional
standalone theorem certified by those final reviewers.
