# Scope check: the 2026 dynamical cavity theorem

Primary source: Dandi, Gamarnik, Pernice, and Zdeborová,
[Rigorous Asymptotics for First-Order Algorithms Through the Dynamical
Cavity Method](https://arxiv.org/html/2603.14573v1), especially
Definition 1.1, assumptions A1--A4, Theorems 1.3 and 2.7, and Remark 2.8.
The [COLT publication page](https://proceedings.mlr.press/v336/dandi26a.html)
identifies the published version.

The source was checked directly. Theorem 1.3 treats a fixed number of
iterations of a single random-matrix/transpose algorithm, with globally
Lipschitz coordinate update functions. Theorem 2.7 gives derivative
moment constants independent of width, but indexed by iteration count,
derivative order, and moment order. Remark 2.8 explicitly describes an
induction invoking higher derivative and moment orders. Neither statement
provides constants uniform as a fixed physical horizon is resolved with
an increasing number of time steps.

Here is the immediate canonical hypothesis failure, independent of the
additional multi-matrix encoding issue. The middle backward update uses
\[
 (z,u)\longmapsto\phi'(z)u=\frac{u}{1+z^2}.
\]
At \(z=1\), its derivative with respect to \(z\) equals \(-u/2\).
This map has no global Lipschitz constant. Multiplying it by any fixed
positive Euler step does not change that conclusion. A prescribed
clipping of \(u\) repairs this particular hypothesis, but the resulting
constant depends on the clipping and does not discharge cutoff removal.

Thus this source supplies no direct all-time continuation theorem for
the present model. Its off-coordinate derivative mechanism may inform
a new proof, but a mesh-uniform, unclipped adaptation must actually be
proved. No statement here refutes the canonical theorem or rules out
all uses of the cavity method.
