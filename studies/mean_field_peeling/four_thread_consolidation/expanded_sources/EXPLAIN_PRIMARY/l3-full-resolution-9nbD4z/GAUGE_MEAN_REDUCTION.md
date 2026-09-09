# Coordinate sign symmetry: a finite-width concentration lemma

This is a finite-width reduction, not a population-limit theorem.

For signs \(\sigma_i^{(1)},\sigma_j^{(2)},\sigma_k^{(3)}\in\{-1,1\}\),
transform the parameters by
\[
 z_i^{(1)}\mapsto\sigma_i^{(1)}z_i^{(1)},\quad
 W_{ji}^{(2)}\mapsto\sigma_j^{(2)}\sigma_i^{(1)}W_{ji}^{(2)},\quad
 W_{kj}^{(3)}\mapsto\sigma_k^{(3)}\sigma_j^{(2)}W_{kj}^{(3)},\quad
 W_k^{(4)}\mapsto\sigma_k^{(3)}W_k^{(4)}.
\]
Because arctangent is odd and its derivative is even, the predictor is
unchanged, each layer's preactivation and activation is multiplied by
its corresponding coordinate sign, and both exact GD and gradient flow
commute with this transformation. The prescribed independent centered
Gaussian initialization is invariant under it.

Here is the elementary concentration consequence. Suppose \(v_n(s)\)
is one of these layer vectors, \(0\le s\le S\), and that on an event
invariant under the coordinate signs,
\[
 \sup_{s\le S}\frac{\|v_n(s)\|_2}{\sqrt n}\le C,\qquad
 \frac{\|v_n(s)-v_n(u)\|_2}{\sqrt n}\le C|s-u|.
\]
Here \(S,C\) are deterministic and independent of width. Sample an
independent uniform sign vector and apply the transformation to the
whole initialized network. Its law is unchanged. Conditional on the
original network, the transformed empirical mean at a fixed time has
mean zero and variance at most \(C^2/n\):
\[
 \mathbb E_\sigma\left[
 \left(\frac1n\sum_i\sigma_i^{(\ell)}v_{n,i}(s)\right)^2
 \right]=\frac{\|v_n(s)\|_2^2}{n^2}.
\]
The transformed empirical mean has time Lipschitz constant at most \(C\),
by Cauchy--Schwarz. For a grid of spacing at most
\(\varepsilon/(2C)\), Chebyshev's inequality and a union bound give
\[
 \mathbb P_\sigma\left(
 \sup_{s\le S}\left|\frac1n\sum_i\sigma_i^{(\ell)}v_{n,i}(s)\right|
 >\varepsilon\right)
 \le
 \left(2+\frac{2CS}{\varepsilon}\right)
 \frac{4C^2}{n\varepsilon^2}.
\]
If \(C=0\), the assertion is immediate. Integrating over the original
network and adding the complement probability of the invariant event
gives the unconditional bound. If that complement probability tends
to zero, it proves uniform convergence of the empirical mean to zero.

For the finite gradient flows of READOUT_COERCIVITY.md, its
high-probability invariant initialization event supplies a deterministic
upper bound on the entire physical orbit's feature-time horizon.
The polynomial feature-time bounds on that fixed interval give the
two bounds above for all three preactivation and activation vectors.
Consequently their empirical means tend to zero uniformly over all
physical times. Combined with the strictly positive second-moment
bounds in that theorem, this gives positive empirical variances,
uniformly over physical time, with probability tending to one.

This argument proves concentration of these signed means only.
It does not prove convergence of arbitrary empirical measurements,
independence of trained coordinates, or control of the middle
backpropagated multiplier.
