# Result and exact scope

For each fixed normalized bounded nonconstant C2 shape \(\psi\)
and separation \(0<\delta<1\), one can use one activation
\[
                    \phi(z)=a(1+z)+e\psi(z)
\]
at every separately fixed finite hidden depth \(L\ge2\).
Any one \(e\in(0,1]\), including \(e=1\), is allowed.

An explicit sufficient gain is
\[
 \lambda=\delta^2/16,\quad T_0=12/\lambda,\qquad
 a=\max\left\{10^{12}(1+T_0),
       \left(2^{36}T_0^2/\sqrt{c_\psi}\right)^{2/5}\right\},
\]
where \(c_\psi>0\) is the finite-interval affine-regression
constant defined and proved positive in the manuscript.
It depends only on the shape.

The [complete self-contained manuscript](MANUSCRIPT.md) proves
global canonical strong population raw GF, uniqueness and
reached-state continuation, exponential fitting, full-sequence
compact-time limits of actual finite GF and raw GD, all true
kernel blocks, hidden fields and velocities, whole path laws,
second moments and integrated squared speeds. It also proves
nonzero initial acceleration of every hidden block and every
sample/layer, and the exact projected-kernel coefficient 18.

The activation pair is independent of depth, width, time and
the particular admissible triple. Width-convergence constants
may depend on the separately fixed depth. No growing-depth
width limit is claimed.

For the broad shape class, the all-time nonaffinity lower bound
is \(e^2c_\psi/(16a^{L-1})\). Compactly supported shapes show why
a positive uniform-in-depth margin is impossible for the whole
class. An infinite-dimensional open C2 ball around \(\arctan/4\)
also admits a positive nonaffinity margin independent of depth.

The literal convex mixture requested subsequently has a different
status. Dividing this activation by \(a+e\) changes the network
under its fixed initialization and raw metric. The result above
does not prove the full global theorem for that convex mixture;
see the separate [convex-family report](../convex_offset_all_depths/REPORT.md).
