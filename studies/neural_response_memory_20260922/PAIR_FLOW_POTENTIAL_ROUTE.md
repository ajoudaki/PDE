# Pair-flow potential route

This is a prompt-only, bounded theory check. It uses no repository scientific
inputs, literature, or experiments. All conclusions concerning network dynamics
are conditional on the finite closed state laws stated below. In particular, no
finite state closure for a trained tanh network is established here.

## Contract and conclusion

Assume finitely many ordinary real coordinates per neuron, independent of
width, with prescribed regular autonomous laws. The question is whether the
learned outer-product integral can be evaluated through a universal function
of current neuron states and finitely many frozen initial marks, without
storing a growing trajectory or imposing low rank.

There is an exact sufficient condition: the outer-product source must be a
directional derivative of a universal pair potential along the closed flow.
The resulting interaction is an integral operator against the current marked
neuron distribution. Reversibility by itself does not provide this potential
globally or provide an admissible method to evaluate it.

## Exact endpoint identity

Let the state of neuron i in layer 2 be b_i in B, and that of neuron j in
layer 1 be a_j in A. Allow a finite shared state g in C. Assume

\[
\dot b_i=F_2(b_i,g),\qquad
\dot a_j=F_1(a_j,g),\qquad
\dot g=G(g),\qquad r=R(g),
\]

and assume the learned weight increment obeys

\[
\dot w_{ij}=q(b_i,a_j,g),\qquad
q(b,a,g)=-2R(g)D(b)H(a).
\]

Here D and H are prescribed scalar functions; extra vector coordinates can be
handled componentwise. Let the pair generator be

\[
\mathcal L=F_2\cdot\partial_b+F_1\cdot\partial_a+G\cdot\partial_g.
\]

If a universal C1 function U on the relevant pair-state domain satisfies

\[
\mathcal L U=q,
\]

then the chain rule gives, for every trajectory in that domain,

\[
w_{ij}(t)-w_{ij}(0)
=U(b_i(t),a_j(t),g(t))-U(b_i(0),a_j(0),g(0)).
\tag{1}
\]

The law and the potential are fixed before observing the realized trajectory.
They may depend on prescribed model parameters, but must not contain a fitted
table of the target trajectory, a hidden weight matrix, or a history-valued
coordinate. Identity (1) does not require inversion of the observed dynamics.

Append the frozen marks b_i^0=b_i(0), a_j^0=a_j(0), g^0=g(0) to the
current state. Define

\[
K((b,b^0),(a,a^0);g,g^0)
=U(b,a,g)-U(b^0,a^0,g^0).
\tag{2}
\]

If

\[
\nu_{1,t}=\frac1{n_1}\sum_j\delta_{(a_j(t),a_j^0)},
\]

then the learned contribution to a forward interaction is exactly

\[
\frac1{n_1}\sum_j [w_{ij}(t)-w_{ij}(0)]H(a_j(t))
=\int K((b_i(t),b_i^0),(a,a^0);g(t),g^0)
       H(a)\,d\nu_{1,t}(a,a^0).
\tag{3}
\]

The transpose interaction has the analogous integral against
\(\nu_{2,t}=n_2^{-1}\sum_i\delta_{(b_i(t),b_i^0)}\). No finite-rank
factorization of K is used. The frozen marks add a fixed number of ordinary
coordinates per neuron. They allow restart from current marked state without
recovering the time-zero state by backward simulation.

This treats the learned increment. An arbitrary initial dense matrix
\(w_{ij}(0)\) still requires a separate representation for its action.
Also, the prescribed finite closed laws are essential: if F or G secretly
requires the complete evolving matrix or an unspecified history, (1) has not
resolved that earlier closure problem. A shared state that is itself a full
distribution is not a finite shared state as assumed here.

## Existence is local; global existence needs compatibility

Write X=(F2,F1,G), and assume X and q are C1. Near a point where X is
nonzero, choose a codimension-one section transverse to X. The map
\((s,\xi)\mapsto\Phi_s(\xi)\), with \(\xi\) on that section, has invertible
derivative there: the flow direction is independent of the section's tangent
directions. The inverse-function theorem therefore gives local coordinates.
For any C1 boundary value c on the section, set

\[
U(\Phi_s\xi)=c(\xi)+\int_0^s q(\Phi_v\xi)\,dv.
\]

Differentiating in s gives LU=q. This proves local solvability, not an
efficient endpoint formula: computing this definition anew by following an
orbit would still be trajectory evaluation.

Two immediate global obstructions are:

* At a fixed point X(z)=0, a C1 potential requires q(z)=0.
* On a closed orbit with period P, a single-valued potential requires
  \(\int_0^P q(\Phi_s z)\,ds=0\), since U returns to its starting value.

For example, the reversible circle flow \(\dot\theta=1\) with source q=1
has no single-valued potential: its period integral is 2pi. Frozen initial
marks do not fix this obstruction, because they also agree when the current
state returns. A new clock or accumulated coordinate can remove this specific
obstruction, but changes the admitted state and does not establish a universal
tractable potential. More generally, periodic-orbit compatibility is necessary,
not a sufficient criterion asserted here.

Thus the existence of a reversible finite flow is weaker than existence of
a global potential with the required regularity and evaluation complexity.

## A future-integral construction and its limits

Suppose the known pair flow is forward complete and
\(\int_0^\infty |q(\Phi_s z)|\,ds<\infty\) on the relevant domain. Define

\[
U(z)=-\int_0^\infty q(\Phi_s z)\,ds.
\tag{4}
\]

The minus sign is necessary. Indeed,

\[
U(\Phi_hz)-U(z)=\int_0^h q(\Phi_s z)\,ds,
\]

so its derivative along the flow is q. To infer an ordinary C1 potential,
one also needs regularity of (4), for example local integrable domination
of the state derivatives of its integrand. The displayed flow identity
itself only needs convergence and the semigroup identity.

Formula (4) is a construction from a specified law, not access to observed
future data. Nevertheless, an online future rollout is not a finite-cost
current-state aggregate formula. To satisfy an operational no-replay
requirement, U needs an explicit expression or an independently constructed
representation with justified approximation and complexity bounds.

Saturation is not enough to justify (4): q tending to zero does not imply
its integrability. Nor does finite-time invertibility guarantee a uniformly
regular potential near the limiting saturated boundary.

## The single-sample residual clock

For a single prediction f(theta) and residual r=f(theta)-y, Euclidean
gradient flow of the squared loss gives

\[
\dot\theta=-2r\nabla f(\theta),\qquad
\dot r=-2r\|\nabla f(\theta)\|^2.
\]

More generally, a fixed positive semidefinite scaling M gives
\(K=\nabla f^\top M\nabla f\ge0\) and \(\dot r=-2Kr\).
On every regular finite interval,

\[
r(t)=r(0)\exp\!\left(-2\int_0^t K(s)\,ds\right).
\]

Hence r keeps its sign when r(0) is nonzero. Define the signed clock

\[
\tau(t)=-2\int_0^t r(s)\,ds.
\]

It is strictly monotone on those intervals, decreasing when r is positive.
For the full parameter flow, \(d\theta/d\tau=M\nabla f\).
If r(0)=0, the full squared-loss gradient flow is stationary.

The same simplification is available for the assumed finite coordinates only
if their closed laws factor accordingly:

\[
\dot b=-2r\widehat F_2(b,g),\quad
\dot a=-2r\widehat F_1(a,g),\quad
\dot g=-2r\widehat G(g).
\]

In that case, the weight equation becomes
\(dw_{ij}/d\tau=D(b_i)H(a_j)\), and a potential V need only solve

\[
\widehat{\mathcal L}V=D(b)H(a).
\]

Then \(\Delta w_{ij}=V(z_{ij}(\tau))-V(z_{ij}(0))\). This removes
the shared residual from the pair source. The common residual factor of the
full network gradient flow does not, by itself, prove the existence of the
postulated finite coordinate laws. Also, if the limiting residual vanishes,
the clock need not be invertible at the limit; the finite-time identity remains
valid, and an endpoint limit requires its own convergence check.

## Explicit reversible states, a plateau, and full rank

Consider a prescribed clock s and a two-coordinate state (a,u) per neuron,
with a>0 and

\[
\frac{da}{ds}=0,\qquad \frac{du}{ds}=-au.
\]

The finite-time map \((a,u_0)\mapsto(a,u_0e^{-as})\) is invertible.
For two neurons (a,u) and (b,v), let the accumulated source be uv. The
pair generator applied to

\[
U((a,u),(b,v))=-\frac{uv}{a+b}
\]

is

\[
(-au)\left(-\frac{v}{a+b}\right)
+(-bv)\left(-\frac{u}{a+b}\right)=uv.
\]

Thus, with u(0)=v(0)=1 and zero initial learned weight,

\[
w_{ab}(s)=\frac{1-u(s)v(s)}{a+b}
=\frac{1-e^{-(a+b)s}}{a+b},\qquad
w_{ab}(\infty)=\frac1{a+b}.
\tag{5}
\]

This uses only current states and fixed coefficients and reaches a nonzero
learned plateau while the amplitudes saturate at zero. For arbitrary initial
amplitudes, replace the numerator by \(u_0v_0-uv\) and retain u0,v0 as
frozen marks.

There is no rank bound from the number of state coordinates. For any n
distinct positive rates a1,...,an, the n-by-n matrix from (5) with the same
rates in both layers satisfies, for every s>0,

\[
\sum_{i,j}c_i c_j w_{a_i a_j}(s)
=\int_0^s\left(\sum_i c_i e^{-a_i z}\right)^2dz.
\]

If this is zero, continuity makes the exponential sum zero throughout the
interval. Its first n derivatives at any interior point give a Vandermonde
system in the distinct rates, with invertible diagonal exponential factors,
so all c_i vanish. The matrix is positive definite and has rank n.
The same argument applies on [0,infinity) to its Cauchy-kernel plateau.

The example proves that a finite per-neuron state and a smooth pair potential
can produce arbitrarily large matrix rank, including after saturation. It is
a mathematical witness for the representation mechanism, not a derivation
of the stated laws from a particular neural network. Bounds also deteriorate
as a+b tends to zero; no uniform small-rate claim is made.

## Status and decisive remaining obligation

Established within the stated assumptions: the endpoint identity, its current
marked-law aggregate, the global obstruction, the future-integral sign, the
single-sample residual clock, and the full-rank plateau example.

Still required for the intended trained network: derive admissible closed
finite neuron laws and construct a universal potential for their actual source
on the reachable domain, with regularity and evaluation bounds. Reversible
state trajectories, residual decay, and saturation alone do not prove these
requirements. Conversely, failure of one global potential does not prove
that all finite-state current-aggregate representations are impossible.
