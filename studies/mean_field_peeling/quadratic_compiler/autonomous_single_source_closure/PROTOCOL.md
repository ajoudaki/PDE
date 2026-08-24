# Protocol: one-time autonomous closure for quadratic depth two

Status: frozen after correcting the bounded-source bias, 20 August 2026.

## Models

All models have one sample, one scalar target, width `n`, iid standard
Gaussian initialization, and full-MSE Euclidean-muP gradient flow.  In
feature time write `G=W/sqrt(n)` and normalized inner product
`<v,w>=n^{-1}v^T w`.

The three staged feature maps are

\[
\begin{array}{c|c|c|c}
\text{model}&X&Z&f\\ \hline
Q I&u^2&G X&\langle A,Z\rangle,\\
I Q&u&G X&\langle A,Z^2\rangle,\\
Q Q&u^2&G X&\langle A,Z^2\rangle.
\end{array}
\]

Every displayed square is coordinatewise.  The final row is the canonical
raw-square model.

## Required meaning of a successful closure

1. It evolves in physical MSE time and has the residual or loss as a direct
   current-state readout.
2. It is autonomous and restartable from its full declared present state.
   No past-time kernel, stored trajectory, or positive-time oracle is
   allowed.
3. It uses a fixed finite list of scalar fields on an explicit fixed
   finite-dimensional source domain.  Neither the field list nor the source
   dimension may grow with width, elapsed time, or derivative order.
4. A one- or multi-variable *spatial* integral kernel is admissible only if
   its domain, source, regularity, and initialization are explicit and do not
   encode a width-sized matrix or an arbitrary future curve.
5. The immutable source must be derived from the Gaussian initialization.
   It may be unbounded.  Compact support, analytic time dependence, and a
   positive Taylor radius are **not** requirements.
6. The equation must identify the width-first network output uniformly on
   compact physical-time intervals.  Agreement of every formal derivative
   is necessary but not sufficient.

In particular, zero Taylor radius is not a falsifier.  An unbounded spectral
or characteristic source can have all moments, a divergent Taylor series,
and a finite real-axis integral evolution.

## Claim ladder

- C1: exact finite-width one-time equations and rank-one elimination;
- C2: an explicit width-independent immutable source;
- C3: a closed one-time field equation for each partial model;
- C4: a closed one-time field equation for the both-square model;
- C5: well-posedness on the physical real axis;
- C6: compact-time finite-width identification and direct loss readout.

No claim is promoted by a formal jet, an existing two-time formulation, or a
generic operator renamed as one field.

## Controls

The exact first feature slopes are

\[
F'_{QI}(0)=10,\qquad F'_{IQ}(0)=11,\qquad F'_{QQ}(0)=111.
\]

For `QQ`, an implementation must reproduce the accepted odd derivatives

\[
111, 1\,685\,184, 77\,400\,633\,120,
7\,315\,868\,433\,079\,296,
1\,181\,161\,141\,825\,400\,561\,664
\]

through order nine.  The partial-model recurrence in this directory supplies
independent exact controls for `QI` and `IQ`.

## Competing mechanisms to test

1. conserved spectral/Lax variables, allowing an unbounded source;
2. real-axis characteristic transport over immutable Gaussian labels;
3. output-coordinate resolvent/Stieltjes or signed-resolvent realization;
4. an explicit spatial-kernel PDE, accepted only if it is a genuine
   deterministic continuum source rather than a continuum spelling of the
   microscopic matrix;
5. a proof that the requested compiler class is impossible, accepted only
   after the class and the separating network observables are both formalized.

