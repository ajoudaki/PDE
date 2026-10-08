# Why a response subspace is not automatically a nonlinear closure

This note proves two elementary structural results. Neither is an
impossibility theorem for nonlinear compression. They explain precisely
which property an intrinsic alternative to coordinate selection must
replace. Scientific inputs for these propositions are the definitions
below, not another study's claims.

## 1. Linear reductions commuting with a nonaffine activation

Let \(T:\mathbb R^n\to\mathbb R^q\) be a real linear map. Let \(\phi\)
be a real analytic nonaffine function on an interval containing all
arguments below. Apply it coordinatewise. Suppose

\[
T\phi(z)=\phi(Tz)
\tag{1}
\]

on an open box in \(\mathbb R^n\). Then each row of \(T\) contains at
most one nonzero entry.

**Proof.** Write a nonzero row as \(a^\top\). The corresponding scalar
identity is
\(\sum_i a_i\phi(z_i)=\phi(\sum_i a_i z_i)\). Differentiate once in
\(z_i\) and once in \(z_j\), where \(i\ne j\). Its left side has zero
mixed derivative, so

\[
0=a_i a_j\phi''(a^\top z)
\tag{2}
\]

throughout the box. Because \(a\ne0\), its values \(a^\top z\) contain
an open interval. A nonaffine real analytic \(\phi\) has second
derivative not identically zero on any open subinterval of its connected
domain: otherwise the power series identity theorem would make it affine
there and throughout that domain. Thus (2) forces \(a_i a_j=0\) for
every distinct pair, proving the claim. ∎

If a row has its one nonzero entry equal to \(c\), the remaining condition
is \(c\phi(t)=\phi(ct)\) on the interval in question. For a Taylor
expansion at zero with a nonzero nonlinear coefficient of degree \(k\),
it implies \(c^k=c\). For example, a nonzero quadratic coefficient
forces \(c=1\); for an odd activation such as tanh, \(c=-1\) is also
possible. A nonzero constant term forces the row sum to equal one.
These are local refinements, not assumptions needed for (2).

**Interpretation.** A dense mixing projection generally cannot preserve
the original componentwise activation. Coordinate evaluation can:
\((\phi(z))_i=\phi(z_i)\). This is why selected-neuron constructions
can retain the original nonlinear gates while compressing their
pairings. The obstruction concerns exact commutation on an open
ambient set. It does not rule out a changed reduced activation, an
approximation on a trajectory, or a nonlinear coordinate map.

## 2. Exact finite subalgebras are blockwise-constant coordinates

Equip \(\mathbb R^n\) with coordinatewise multiplication. Let
\(V\subseteq\mathbb R^n\) be a linear subspace containing the all-ones
vector and closed under this multiplication. Define \(i\sim j\) if
\(v_i=v_j\) for every \(v\in V\). Then \(V\) consists exactly of the
vectors constant on each equivalence class.

**Proof.** The inclusion of \(V\) in the blockwise-constant vectors
follows from the definition. Conversely, choose finitely many vectors
spanning \(V\). A linear combination of them can be chosen to take
distinct values on distinct equivalence classes: for each unequal
pair, the forbidden coefficients lie in a proper hyperplane; finitely
many proper hyperplanes do not cover a real vector space. One elementary
proof of the latter fact is to take the coefficient curve
\((1,t,\ldots,t^{\dim V-1})\). Each nonzero linear condition becomes
a nonzero polynomial in \(t\), so excludes only finitely many parameters.

Let \(v\in V\) be such a separating vector, with distinct block values
\(c_1,\ldots,c_r\). Because \(V\) contains constants and is closed under
multiplication, it contains every polynomial in \(v\), in particular

\[
\prod_{j\ne i}\frac{v-c_j{\bf1}}{c_i-c_j}.
\tag{3}
\]

Expression (3) is exactly the indicator of block \(i\). All block
indicators therefore lie in \(V\), and their linear span is the full
space of blockwise-constant vectors. ∎

A low-dimensional temporal response span is not generally such an
algebra. Requiring exact closure under activation products can enlarge
it drastically. This algebraic statement does not imply that approximate
closure at dense-variability accuracy has large rank.

## 3. A quantitative warning about polynomial nonlinearities

An intrinsic reduced nonlinearity can be polynomial without being small.
In \(R\) reduced coordinates, a generic scalar polynomial of total degree
at most \(k\) has

\[
\binom{R+k}{k}
\tag{4}
\]

coefficients. To count them, append the slack exponent
\(k-\sum_{j=1}^R\alpha_j\) to every multi-index with total degree at most
\(k\); the resulting \(R+1\) nonnegative exponents sum to \(k\), counted
by placing \(R\) separators among \(k+R\) positions.

Even fixed \(k=3\) gives \(\Theta(R^3)\), exceeding quadratic storage.
A total-degree expansion whose required degree grows like \(\log n\)
does not inherit an \(O(R^2)\) storage bound merely because the target
trajectory had temporal rank \(R\). Special tensor structure, a
low-dimensional admissible state set, or a separate sparse potential
approximation theorem is necessary.

This is a count for the generic coefficient representation, not a lower
bound on every polynomial, every potential, or every neural reduction.
Low-degree polynomials, separable potentials, or exploitable symmetries
may be much cheaper.

## 4. What this suggests rather than forbids

A promising alternative should change the reduced nonlinear map instead
of demanding (1), and derive its backward action from that same map.
For an RMS-orthonormal basis \(U\), with \(U^\top U/n=I\), the scalar
potential

\[
\Psi(c)=\frac1n\sum_{i=1}^n\int_0^{(Uc)_i}\phi(v)\,dv
\]

does precisely this:

\[
\nabla\Psi(c)=\frac1n U^\top\phi(Uc),\qquad
\nabla^2\Psi(c)=\frac1n U^\top
   \operatorname{diag}(\phi'(Uc))U.
\tag{5}
\]

The forward and backward actions are automatically compatible. The
outstanding compression problem is a succinct, accurate representation
of \(\Psi\), its gradient and its Hessian on the states actually needed
by the reduced dynamics. Storing \(U\) costs \(nR\), and simply calling
(5) costs width-\(n\) work; neither solves that problem.
