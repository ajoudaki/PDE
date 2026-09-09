# Marked-Traffic / OU-Semigroup Candidate: Adversarial Audit

## Verdict

The candidate correctly identifies a one-time marked-traffic algebra and the
finite-dimensional current-time derivation.  It also predicts the correct
`1/n` Gaussian-influence scale for normalized scalar observables at
initialization.  It does **not** provide a compact-time completion theorem.

The proposed first-sensitivity estimate fails to close: weighted sensitivity
energy can align with rare coordinates, and a row/column cavity of that
sensitivity introduces mixed second derivatives.  Controlling those
derivatives introduces third derivatives, and so on.  This is the adaptive
response hierarchy the proposal was meant to eliminate.  Gaussian OU
smoothing, the positive maximum principle, and finite-microstate
recompression each require an additional major theorem.  They are not
consequences of the low-influence calculation.

Accordingly this route is rolled back as a completion mechanism.  Its exact
algebraic language and initialization calculation remain reusable.

## 1. Exact calibration at initialization

Use the two-hidden-layer model, write `G=Gamma+L`, and differentiate with
respect to the standardized Gaussian entry `g_ab`, where

\[
 \Gamma_{ab}=g_{ab}/\sqrt n.
\]

At initialization put

\[
 x=\phi(u),\quad z=\Gamma x,\quad q=\phi'(z),\quad
 b=A\odot q,
\]

and set

\[
 p=\phi'(u),\quad h=p^2,\quad
 M=\Gamma\operatorname{diag}(h)\Gamma^\top,
\quad v=h\odot\Gamma^\top b.
\]

Then

\[
 \partial_{g_{ab}}z=n^{-1/2}e_a x_b,
\]

while the exact field velocity is

\[
 \dot z=\langle x,x\rangle_n b+Mb.
\]

For the normalized forward test `K=<z,z>_n`,

\[
 \boxed{\mathcal C_g(K)
 =\sum_{a,b}(\partial_{g_{ab}}K)^2
 =\frac4n\langle z,z\rangle_n\langle x,x\rangle_n.}
\tag{1}
\]

For the tied forward/transpose test

\[
 J=\langle z,b\rangle_n
  =\langle x,\Gamma^\top b\rangle_n,
\]

put `s=A odot (q+z odot phi''(z))`.  Direct differentiation gives

\[
 \boxed{\mathcal C_g(J)
 =\frac1n\langle x,x\rangle_n\langle s,s\rangle_n.}
\tag{2}
\]

Thus the proposed `O(1/n)` scale is dimensionally correct and respects exact
transpose reuse.  Differentiating (1)--(2) once along the path again produces
`1/n` times finite normalized contractions.  For these parity-definite tests,
the first annealed derivative vanishes under `g -> -g`; pathwise it is
generically nonzero.  This establishes only initialization and fixed formal
time derivatives, not a compact-time estimate.

## 2. The nonclosing sensitivity equation

For one Gaussian direction let

\[
 U=\partial_g u,\quad V=\partial_g A,\quad K_L=\partial_gL.
\]

With

\[
 X=\phi'(u)U,
\]

\[
 Z=E^{ab}x+K_Lx+GX,
\]

\[
 B=\phi'(z)V+A\phi''(z)Z,
\]

and the analogous tied transpose fields `R,C`, the exact linearized system is

\[
 \dot U=C,\qquad \dot V=\phi'(z)Z,
 \qquad \dot K_L=B\otimes_nx+b\otimes_nX.
\tag{3}
\]

After summing (3) over all standardized Gaussian directions, the row
sensitivity density

\[
 \rho_i^Z=\sum_{a,b}|Z_i^{ab}|^2
\]

generates the occupation term

\[
 \frac1n\sum_i A_i^2\phi''(z_i)^2\rho_i^Z.
\tag{4}
\]

Ordinary sensitivity energy controls only `n^-1 sum_i rho_i^Z`.  No
dimension-free deterministic estimate of (4) follows from this and an
empirical Gaussian/Orlicz bound for `A`: a unit sensitivity density may
concentrate where `|A_i|` is of order `sqrt(log n)`.

Polynomially weighted energies generate the next polynomial weight.
Exponentially weighted energies suffer the same problem after matrix
transport: an operator-norm bound on `G` does not control

\[
 \sum_i e^{\alpha A_i^2}|(GX)_i|^2
\]

by the correspondingly weighted input energy.

## 3. Why a naive cavity does not repair it

Deleting a source row or column to decorrelate `G` from `X` requires comparing
the sensitivity with its cavity counterpart.  The comparison contains

\[
 \partial_{g_{ik}}X^{ab}
 =\partial_{g_{ik}}\partial_{g_{ab}}x,
\]

a mixed second sensitivity.  Repeating the argument on that object produces
third sensitivities.  Gaussian integration by parts has the same escalation.
No finite recursive inequality was found that sums this hierarchy or rules
out rare-coordinate alignment.

This is a precise rollback gate: calling the missing all-order estimate an
OU commutator bound merely renames the adaptive-response problem.

## 4. Independent defects in the semigroup proposal

OU smoothing only in the frozen Gaussian coordinates regularizes neither the
transported state variables nor the singular graph-supported joint law of
source and trajectory.  Smoothing the full finite-dimensional state instead
encounters extensive divergence.  For example,

\[
 \operatorname{div}_L \dot L
 =n\,\langle x,x\rangle_n
   \langle A,\phi''(z)\rangle_n,
\tag{5}
\]

whose compressibility constants are not dimension-free.

Even a valid low-influence estimate would establish concentration, not
uniqueness of the limiting hierarchy.  The positive maximum principle gives
dissipativity but not maximal dissipativity or dense resolvent range.  A
separate reachable-state uniqueness or resolvent theorem is necessary.

Likewise, density of finite microstates does not provide an effective,
positive, source-compatible recompression algorithm or a bound on the
discarded generator residual.  Those are independent theorems.

## 5. Claim ledger

| Claim | Status |
|---|---|
| One-time marked-traffic representation preserves source/transpose reuse | Exact |
| Current-time Liouville derivation on finite tests | Exact |
| `O(1/n)` influence for the displayed normalized tests at `t=0` | Proved |
| First pathwise time derivative retains the `O(1/n)` prefactor | Proved |
| Compact-time `C_T/n` influence | Open |
| First-sensitivity plus OU/Orlicz/cavity closes | Falsified as proposed |
| Positive maximum principle gives a unique semigroup | Falsified |
| Low influence implies positive finite recompression | Falsified |
| Candidate completes mesh removal or restartability | Not established |

The remaining trace-propagator/occupation estimate is not a local
commutator lemma.  Without a genuinely summable marked-response calculus it
is essentially the original hard probabilistic stability problem.
