# An analytic-class barrier, and why it is conditional

This note proves the lower bound used in the study's diagnosis.  It is a
theorem about a full analytic class of trajectories.  It is **not** a
claim that the dense training dynamics reaches that class.

## Theorem

Let `d >= 2`.  Consider scalar trajectories on the sphere, including their
initial and limiting times, with the supremum norm

\[
\sup_{t\in[0,\infty]}\sup_{\lVert x\rVert=\sqrt d}|f(t,x)|.
\]

Put `s = exp(-t)`.  Fix a bounded complex neighborhood of `[0,1]` and a
bounded intrinsic complex neighborhood of the sphere inside

\[
\{z\in\mathbb C^d:z^Tz=d\}.
\]

Both neighborhoods, including their positive radii, are fixed independently
of `p`, `epsilon`, and `n`.  Let the admissible class contain the unit ball
of functions holomorphic and bounded by one on this product neighborhood,
subject to `f(0,x)=f(\infty,x)=0`.

Suppose one fixed deterministic encoder, continuous in the real-domain
supremum norm, sends every member to `q` real numbers, and one fixed decoder
reconstructs it, possibly nonlinearly.  Every function-dependent decoder or
dictionary coefficient is part of those `q` numbers.  If the worst-case
error is at most a sufficiently small `epsilon`, then

\[
q\ge c[\log(1/\epsilon)]^d.
\]

The positive coefficient depends on the two fixed bounded complex
neighborhoods and on `d`, but not on `epsilon`.

At the dense-variability target

\[
\epsilon=\frac{1}{\sqrt n\,[\log(en)]^{5/2}},
\]

this gives `q >= c log(n)^d` for all sufficiently large `n`.

## Proof

Fix a positive integer `p`.  Spherical harmonics through degree `p` span
a space of dimension

\[
{p+d-1\choose d-1}+{p+d-2\choose d-1}.                 \tag{1}
\]

In the time variable `s`, take the `p`-dimensional polynomial space
consisting of `s(1-s)` times polynomials of degree below `p`.  Every member
vanishes at `s=1`, which is initial time, and at `s=0`, which is the fitted
limit.  Tensoring this time space with the spherical space in (1) gives a
space of dimension

\[
p\left[{p+d-1\choose d-1}+{p+d-2\choose d-1}\right]
\asymp_d p^d.                                           \tag{2}
\]

Use probability surface measure on the sphere and define

\[
\|g\|_2^2=\int_0^1\int_{\|x\|=\sqrt d}|g(s,x)|^2\,d\sigma(x)\,ds.
\tag{3}
\]

We next prove the analytic estimate used below.  There are fixed positive
constants such that every member of the tensor space satisfies

\[
\sup_{(s,z)\text{ in the fixed complex neighborhoods}}|g(s,z)|
\le A e^{Bp}\|g\|_2.                                  \tag{4}
\]

For the time factor, choose any real `L^2[0,1]`-orthonormal basis of
`s(1-s)` times the polynomials of degree below `p`.  Each basis member has
degree at most `p+1`.  The one-dimensional polynomial `L^2`-to-supremum
inequality on `[0,1]`, followed by the Bernstein--Walsh inequality on the
fixed bounded complex neighborhood, bounds its complex value by
`A_s exp(B_s p)`.  Summing the squared bounds over `p` basis members changes
only a polynomial factor, which is absorbed into the exponential.

For the sphere, use an orthonormal spherical-harmonic basis.  The complex
addition formula on the bounded intrinsic tube gives, degree by degree,

\[
\sum_j|Y_{\ell,j}(z)|^2
\le A_x h_{d,\ell}e^{2B_x\ell}.                        \tag{5}
\]

Indeed, the left side is the Gegenbauer addition kernel evaluated at the
bounded quantity `z` paired with its complex conjugate; a degree-`ell`
Gegenbauer polynomial on a fixed bounded set is at most a fixed constant
to the power `ell`.  The multiplicity `h_{d,ell}` is polynomial in `ell`.
Summing (5) through degree `p`, tensoring with the time basis, and applying
Cauchy--Schwarz proves (4).  All remaining polynomial factors in `p` are
absorbed by increasing `B`.

It follows from (4) that the real `L^2` unit ball multiplied by

\[
r_p=A^{-1}e^{-Bp}                                      \tag{6}
\]

lies inside the stated analytic unit ball.  The common factor `s(1-s)`
preserves both endpoint conditions.

Now restrict the encoder to the boundary of that embedded ball.  If `q`
is smaller than (2), the Borsuk--Ulam theorem gives two antipodal
trajectories with the same code.  They therefore have the same
reconstruction.  Their normalized `L^2` distance is `2r_p`, so by
the triangle inequality at least one reconstruction error is at least
`r_p`.  The requested supremum norm dominates the normalized
`L^2` norm.

Consequently, error smaller than `r_p` requires at least the number
of coordinates in (2).  Choose `p` as the largest integer for which
`r_p` remains larger than `epsilon`.  Then `p` is proportional to
`log(1/epsilon)`, and (2) proves the theorem.  Substituting the displayed
dense-variability target gives the final statement.  ∎

## Single-time version

If only one common time slice contains the corresponding analytic ball,
the time factor in (2) is absent.  The same proof gives

\[
q\ge c[\log(1/\epsilon)]^{d-1}.
\]

Thus even the spatial obstruction has an exponent proportional to `d`.

## Exact limitation

The dense-network result currently supplies analyticity of each realized
trajectory.  It does not supply the much stronger inclusion of the
finite-dimensional balls used above.  In particular:

- full-rank training inputs preserve all query directions but do not make
  their harmonic coefficients independently reachable;
- nonlinear feature learning makes the trajectory non-kernel, but does
  not establish a harmonic packing;
- the proved dense lower bound gives one nondegenerate fluctuation
  direction, not the number of directions in (2).

Therefore the theorem proves that uniform membership in a **full unit ball
with fixed bounded analytic neighborhoods** cannot by itself justify
sub-`log(n)^d` compression.  Individual analyticity, a shrinking
`n`-dependent radius, or an `n`-dependent analytic norm is not enough for
this conclusion.  A lower bound for the actual dense model still needs a
reachability or high-probability packing theorem of dimension comparable to
(2).

Finally, this is a static continuous-encoder lower bound.  It also applies
to an autonomous representation only after its initialization map is shown
continuous in the stated topology and every instance-dependent vector-field
and decoder coefficient is counted.  No such property is asserted for the
current selected-neuron construction.

Continuity of the encoder is essential.  Without continuity,
bounded precision, or another stability requirement, one real number can
encode arbitrarily many coordinates and no positive coordinate lower
bound is possible.
