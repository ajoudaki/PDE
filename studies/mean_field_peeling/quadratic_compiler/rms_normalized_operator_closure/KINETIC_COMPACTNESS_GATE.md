# Kinetic compactness gate

Status: the action theorem and conditional compactness implication are
proved; propagation of the kinetic entropy from iid initialization is open
and under independent audit.

## 1. Uniform action available on every fixed interval

Fix feature time `S<infinity`.  On an event whose probability tends to one,

\[
\sup_{s\le S}\|A(s)\|_n\le S+2,
\qquad
\inf_{s\le S}\langle H(s)^2\rangle_n
\ge {1\over1+16\epsilon}.                       \tag{1.1}
\]

Indeed, `||Y||_n<=1` gives the first bound.  If
`m=<u^2>_n`, the exact identity

\[
m'={8\epsilon^2f\over\alpha^2\beta^2}          \tag{1.2}
\]

and monotonicity `f(s)>=f(0)` show that `m` cannot fall appreciably from its
Gaussian initial value.  Jensen then gives
`<u^4> >= m^2` and hence (1.1).

Since `f'=K` and `|f(S)|<=S+2`,

\[
\int_0^S\langle R^2\rangle_n\,ds=O_{S,\epsilon}(1),
\qquad
\int_0^S\langle (u')^2\rangle_n\,ds=O_S(1),     \tag{1.3}
\]

where

\[
(u_i')^2={4\over\alpha}H_iT_i^2.                \tag{1.4}
\]

Furthermore

\[
\sup_{s\le S}\|G(s)\|_{op}=O_{S,\epsilon}(1),
\qquad
\int_0^S\langle T^2\rangle_n\,ds
=O_{S,\epsilon}(1).                             \tag{1.5}
\]

For (1.5), use `G=G(0)+int R tensor H`, Cauchy--Schwarz,
the Gaussian operator-norm bound for `G(0)`, and
`||T||_n<=||G||_op||R||_n`.

These estimates are dimension-free but only `L1` in the product of time and
neuron counting measure.

## 2. Exact kinetic interpretation of both dangerous tails

Coordinatewise,

\[
\boxed{
\beta^{-2}Z_i^2C_i^2={1\over4}R_i^2,
\qquad
\alpha^{-1}H_iT_i^2={1\over4}(u_i')^2.}         \tag{2.1}
\]

Thus the missing compactness is not a generic state-moment estimate: it is
uniform integrability of the two coordinate kinetic-energy densities.

## 3. Conditional de-la-Vallée-Poussin theorem

Suppose that for some increasing convex `Phi` satisfying
`Phi(r)/r -> infinity`,

\[
\sup_n\mathbb E\int_0^S
\left\langle\Phi(R^2)+\Phi((u')^2)\right\rangle_n ds
<\infty.                                           \tag{DV}
\]

Then the spatial-tail condition `(UI)` in
`REACHABLE_TAIL_AUDIT.md` holds.

To prove this, first use (1.1), (1.3), and (1.5) to obtain uniformly in
probability

\[
\nu_n\{Z^2+C^2>L\}=O(L^{-1}),
\qquad
\nu_n\{H+T^2>L\}=O(L^{-1}),                       \tag{3.1}
\]

where `nu_n=ds` times normalized counting measure.  For every `M>0`, (2.1)
then gives

\[
\begin{aligned}
4J_{n,L}\le{}&\int_0^S\left\langle
R^2 1_{\{R^2>M\}}+(u')^2 1_{\{(u')^2>M\}}
\right\rangle_n ds\\
&+M\nu_n\{Z^2+C^2>L\}
+M\nu_n\{H+T^2>L\}.                         \tag{3.2}
\end{aligned}
\]

For fixed `M`, the second line vanishes as `L->infinity`.  If
`a_M=sup_{r>=M}r/Phi(r)`, then `a_M->0`, and `(DV)` makes the expectation of
the first line `O(a_M)`.  Markov's inequality and then `M->infinity` prove
the claim.

## 4. Why the missing hypothesis is substantive

Neither exchangeability nor convergence of every fixed coordinate implies
`(DV)`: an energy atom of size `n` placed at a uniformly random coordinate
is invisible to every fixed-coordinate limit but contributes order one to
the empirical kinetic energy.

Nor can `G(0)H_t` be treated as a fresh Gaussian vector.  For one selected
Gaussian row `W_k`, choose an admissible nonnegative normalized field

\[
H_j=\rho{(W_{kj})_+\over
\{n^{-1}\sum_l(W_{kl})_+^2\}^{1/2}},
\qquad0<\rho<1.
\]

Then `||H||_n=rho`, but

\[
(G(0)H)_k\sim\rho\sqrt{n/2}.                    \tag{4.1}
\]

This is an ambient adaptive-alignment witness, not an iid-reachability
theorem.  It proves that a fresh-Gaussian conditioning argument is invalid
without a trajectory-level cavity estimate.

Finally, a state entropy alone does not close.  For smooth convex `Psi`,

\[
{d\over ds}\langle\Psi(H)\rangle_n
={4\over\alpha}\left[
\langle H\Psi'(H)T\rangle_n
-\langle H^2T\rangle_n\langle H\Psi'(H)\rangle_n
\right],                                           \tag{4.2}
\]

which has no sign.  Young inequalities introduce higher moments and recreate
the unbounded hierarchy.  There are exact bounded-state configurations for
which (4.2) vanishes for every `Psi` while the second kinetic density in
(2.1) has an order-one atom.

The unresolved theorem is therefore precisely the propagation of `(DV)`, or
an equivalent dynamic no-condensation estimate, on the actual iid-Gaussian
trajectory.  Low action, marginal propagation of chaos, and state-only
entropy do not imply it.

