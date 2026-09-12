# Shared notation and model conventions

This file is the notation contract for the established library. A chapter may
introduce a typed auxiliary variable, but must not silently change these
conventions. A theorem's stated initialization, loss and learning rates override
no other theorem: different models are explicitly distinguished.

## Network, data and layers

`L` counts hidden layers, `m` samples, `d` input coordinates and `n` hidden width.
These quantities are fixed separately unless a theorem explicitly takes their
limit. Samples are `(x_a,y_a)`, with `x_a` in `R^d` and scalar label `y_a`.
The input Gram is `G_ab = x_a^T x_b/d`; normalized inputs have `G_aa=1`.
No diagonalization, whitening, orthogonality or nonsingularity is implicit.

The finite first matrix has shape `n` by `d`, the hidden matrices have shape
`n` by `n`, and the stored readout is a vector of length `n`:

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)}\quad(2\le\ell\le L),
\qquad h_a^{(\ell)}=\phi^{(\ell)}(z_a^{(\ell)}),\qquad
f_{n,a}=\frac{(W^{(L+1)})^T h_a^{(L)}}n.
\]

For the one-input datum `x=1`, `d=1`, the first preactivation and first weight
vector coincide. A common activation is written `phi`; layer-dependent
activations retain their layer superscripts. Write activation derivatives
explicitly as `phi'` rather than introducing a second name for the derivative.

The residual is always `r_a=f_a-y_a`. It is not part of the backpropagated
derivative. In a finite network define

\[
\delta_a^{(L)}=W^{(L+1)}\odot(\phi^{(L)})'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=(\phi^{(\ell)})'(z_a^{(\ell)})\odot
(W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
\]

Thus `delta_a^(ell)=n partial f_(n,a)/partial z_a^(ell)`. The main squared-loss
convention is `mathcal L_n = m^{-1} sum_a r_(n,a)^2`. Sum or half-sum losses
must be stated where used and change physical time by the corresponding factor.

## Populations, operators and norms

Finite hidden coordinates are lower-case `z^(ell), h^(ell)`; population
coordinates are capitalized `Z^(ell), H^(ell)`. Every hidden layer has its own
probability space `Omega_ell` and expectation `E_ell`. An expectation contracts
only objects in the same population. Population weight operators and the
population readout retain the layer-indexed symbol `W^(ell)`; their operator or
random-variable types are stated explicitly. Population backward coordinates
may be written `Delta^(ell)`; plain `Delta` without a layer is a proof mesh.

Finite transpose is `T`; a population Hilbert-space adjoint is `*`. These are
the actual two directions of the same operator, not independent random maps.
Initial Gaussian population actions can be bounded without being Hilbert–Schmidt;
the trained increments may belong to a smaller operator class.

Use ordinary finite Euclidean, Frobenius and operator norms. A finite RMS is
`||v||_2/sqrt(n)` and a finite normalized pairing is `u^T v/n`; do not hide
these factors in new norm or inner-product symbols. A population norm is
`||U||_(L^p(Omega_ell))=(E_ell |U|^p)^(1/p)`. Typed abstract Hilbert spaces in
the linear or operator constructions use ordinary Hilbert norms and pairings.

The population rank-one operator `U tensor V` means
`g -> U E[V g]`; its finite coordinate representative is `u v^T/n`.
The Wasserstein distances between laws are written `mathcal W_p`, with the
underlying Euclidean or path metric stated; they are not weight matrices.

## Initialization and clocks

The nonlinear small-readout convention has independent first weights
`N(0,1)`, hidden-matrix entries `N(0,1/n)`, and **stored** readout entries
`N(0,1/n^2)`. Its limiting initial readout is zero. A chapter using order-one
stored readout states that different initialization explicitly. Equal limiting
initial predictions do not identify the two regimes.

`t` is physical training time, `eta_n` the actual GD step and `Delta` an
auxiliary proof discretization. `kappa_ell` denotes a fixed positive mobility
multiplier. For the preceding first-weight convention the block mobilities are
`n kappa_1, kappa_2,...,kappa_L,n kappa_(L+1)`. Raw GD updates the weights,
which are linearly interpolated; hidden quantities are then recomputed.

For one sample, unit mobilities and label one, feature time obeys
`ds/dt=2(1-f)=-2r` on an interval where this is positive. It is not a new
optimizer. The arctangent coordinate change `F(z)=z+z^3/3` is exact for the
continuous flow only. For `phi(z)=1+arctan(z)/10`, the corresponding primitive
is `F(z)=10(z+z^3/3)`. Neither turns exact raw GD into exact transformed Euler.

## Scope of a limit statement

Every result specifies the physical horizon, mode and topology of convergence,
step condition, observables and restart domain. Compact-time means each fixed
finite `[0,T]`, not one bound valid for all time or for an arbitrary growing
sequence `T_n`. A local theorem remains local. Loss decay, population existence,
finite-width approximation, nonaffinity and hidden feature motion are separate
claims. A fixed finite number of operator or function fields is not a
finite-dimensional scalar state.
