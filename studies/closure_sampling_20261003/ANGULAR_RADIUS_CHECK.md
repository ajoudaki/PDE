# First-layer tanh sources obstruct a wider common angular strip

2026-10-04. Bounded prompt-only check. No additional research sources,
experiments or Git operations were used. The conclusion concerns source
holomorphy, not an output-approximation or storage lower bound.

Fix `d>=2` and restrict normalized inputs to the coordinate circle

\[
v(\theta)=(\cos\theta,\sin\theta,0,\ldots,0).
\]

At initialization, the canonical first-layer Gaussian rows give

\[
h_i(\theta)=\tanh(a_i\cos\theta+b_i\sin\theta),
\qquad (a_i,b_i)\overset{\rm iid}{\sim}N(0,I_2),
\qquad i=1,\ldots,n.
\tag{1}
\]

Set `R_i=sqrt(a_i^2+b_i^2)`, which is positive almost surely. Choose a
real angle `beta_i` with `a_i=R_i cos beta_i` and
`b_i=R_i sin beta_i`. The preactivation is
`g_i(theta)=R_i cos(theta-beta_i)`. At

\[
\theta_i=\beta_i+\frac\pi2+i\eta_i,\qquad
\eta_i=\operatorname{arsinh}\!\left(\frac\pi{2R_i}\right),
\]

one has

\[
g_i(\theta_i)=-iR_i\sinh\eta_i=-\frac{i\pi}{2},
\qquad
g_i'(\theta_i)=-R_i\cosh\eta_i\ne0.                    \tag{2}
\]

The function `tanh z=sinh z/cosh z` has a simple pole at `z=-i pi/2`:
its denominator vanishes there with derivative `sinh(-i pi/2)=-i`,
while its numerator is nonzero. Its residue is one. Consequently (2)
gives a simple, nonremovable pole of `h_i` at `theta_i`, with residue
`1/g_i'(theta_i)`. There is no numerator cancellation. Existence of
this pole suffices; no identification of every complex singularity is
required.

Let `M_n=max_{i<=n}R_i` and

\[
\eta_{\min,n}
 =\min_{i\le n}\eta_i
 =\operatorname{arsinh}\!\left(\frac\pi{2M_n}\right).
\tag{3}
\]

If all coordinates in (1) are holomorphic on the common open strip
`|Im theta|<r`, then necessarily `r<=eta_min,n`: any larger radius
contains at least one of the poles constructed in (2). Equality merely
places that particular pole on the boundary of the open strip and is
not excluded by this argument.

The two-dimensional Gaussian radial density gives exactly

\[
\Pr\{R_i>u\}
=\int_u^\infty s e^{-s^2/2}\,ds=e^{-u^2/2},\qquad u\ge0.
\]

For every fixed `0<epsilon<1`, independence and a union bound imply

\[
\Pr\{M_n\le(1-\epsilon)\sqrt{2\log n}\}
=\left(1-n^{-(1-\epsilon)^2}\right)^n
\le \exp\{-n^{2\epsilon-\epsilon^2}\}\longrightarrow0,
\]
\[
\Pr\{M_n\ge(1+\epsilon)\sqrt{2\log n}\}
\le n^{-2\epsilon-\epsilon^2}\longrightarrow0.
\tag{4}
\]

Thus `M_n/sqrt(2 log n)` converges in probability to one. Since
`arsinh x/x` tends to one as `x` tends to zero, (3)--(4) give

\[
\eta_{\min,n}\sqrt{\log n}
          \xrightarrow{\Pr}\frac\pi{2\sqrt2}.           \tag{5}
\]

In particular, for every fixed `c>pi/(2 sqrt(2))`, with probability
tending to one there is no common holomorphy strip of radius
`c/sqrt(log n)` for all first-layer coordinates (1). A proposed radius
asymptotically larger in order than `1/sqrt(log n)` is therefore
impossible for these tanh source coordinates already at time zero.
The same restriction applies to any joint time/query source domain
whose time slice at zero contains this circle strip.

This is an obstruction for the individual source coordinates of this
activation and angular parameterization. It does not give a lower bound
for network outputs, which can have cancellations and are initially
zero under zero readout, or for the size of any compressed autonomous
representation. It also does not assert such an obstruction for every
bounded strip-holomorphic activation.
