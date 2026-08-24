# Fixed Gaussian operator-source audit

Status: exact candidate-specific obstructions; no universal finite-field
impossibility theorem.

## 1. Why an ordinary Banach algebra cannot be the phase space

Let `B` be a Banach space of measurable scalar fields such that

\[
\|xy\|_B\le M\|x\|_B\|y\|_B,
\qquad \|x\|_{L^1}\le N\|x\|_B.              \tag{1.1}
\]

For every positive integer `k`,

\[
\mathbb E|x|^k\le NM^{k-1}\|x\|_B^k.
\]

Taking `k`th roots and then `k->infinity` gives

\[
\|x\|_{L^\infty}\le M\|x\|_B.              \tag{1.2}
\]

Thus a single Banach algebra with continuous expectation contains only
essentially bounded fields and cannot contain the Gaussian initialization.
Any valid source must use a scale/Fréchet algebra, an unbounded multiplication
domain, or a different operator structure.  This lemma is a construction
constraint, not a no-go for the full contract.

## 2. Ordinary kernels and white noise

An `L2` kernel is Hilbert--Schmidt.  In contrast,

\[
\|W_n/\sqrt n\|_F^2\sim n,
\]

so the Gaussian core has no Hilbert--Schmidt kernel limit.  A noncompact
bounded operator is not excluded by this fact, but an ordinary graphon loses
the central-limit-scale fluctuations.

Replacing the kernel by Gaussian white noise preserves those fluctuations
but creates the opposite problem.  Integrating a two-dimensional white-noise
sheet against a column function produces spatial white noise in the row
variable, which is a distribution rather than an `L2` sample field.
Its pointwise square is not canonically defined.  Wick renormalization would
change the network's coordinatewise square and its RMS denominator.  Hence a
bare graphon or white-noise-sheet ODE is not an exact source for this model.

## 3. The algebraic source that does work, and its boundary

A two-sorted pointed Gaussian-traffic/GNS construction can represent all of

\[
H\mapsto\Gamma H,
\qquad R\mapsto\Gamma^*R,
\qquad (x,y)\mapsto x\odot y                  \tag{3.1}
\]

at every fixed graph order.  The Gaussian edge map is bounded in its traffic
Hilbert norm, but rooted multiplication is unbounded.  Smooth coordinate
cutoffs make a finite-order evolution formal and locally Lipschitz on a
bounded domain.  Removing the cutoff is exactly the weighted-tail problem in
`REACHABLE_TAIL_AUDIT.md`.

The full pointed-traffic law is indexed by every rooted graph evaluation.
Treating that entire law as one state is the exact all-grade hierarchy, which
the frozen contract excludes.  Merely renaming it a probability measure does
not prove compression, well-posedness, or positive-time identification.

## 4. Why one Gaussian response does not close the source action

For a source-dependent equation `X'=V(Gamma,X)`, the first Malliavin response
`J=D_Gamma X` satisfies the closed variational equation

\[
J'=V_XJ+V_\Gamma.                              \tag{4.1}
\]

One Gaussian integration-by-parts step applied to a coefficient depending
only on `(Gamma,X)` therefore uses only `(X,J)`.  But applying it to the
response equation or to a coefficient depending on `J` introduces
`D_Gamma J=D_Gamma^2X`.  Repeating the operation generates every Gaussian
jet.  The scalar witness is

\[
\delta(Dx)(g)=g x'(g)-x''(g),                 \tag{4.2}
\]

which is not determined by the value and first derivative of `x`.
Consequently one-response Fock/Malliavin closure is false.  A construction
that retains `Gamma,Gamma^*` as primitive unbounded actions remains possible,
but must prove an invariant strong domain; representing all jets as one
module is again at risk of storing the complete hierarchy.

## 5. Precise remaining positive-source obligation

The exact finite-width Markov rewrite uses the fixed source `Gamma=G(0)` and
the three current fields `(A,H,Q)`, where `Q=G-Gamma`:

\[
Z=(\Gamma+Q)H,\quad Y=N_\epsilon(Z^2),\quad
R={2\over\beta}Z(A-fY),                        \tag{5.1}
\]

\[
A'=Y,\qquad Q'=R\otimes H,\qquad
H'={4\over\alpha}(I-H\otimes H)M_H
     (I-H\otimes H)(\Gamma+Q)^TR.             \tag{5.2}
\]

This is autonomous and restartable at every finite width.  A terminal
positive theorem must build a canonical, non-ultraproduct realization of
the bidirectional source action in (5.1)--(5.2), name a domain on which
pointwise products and the displayed kernel readout are continuous, prove
that domain invariant for every finite time, and identify the finite-width
limit.  None of Sections 1--4 proves that such a source is impossible; they
eliminate the ordinary Banach-algebra, graphon, bare-white-noise, and
one-response shortcuts.

