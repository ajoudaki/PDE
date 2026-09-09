# Two-input raw-cubic plus-channel order-nine fixed-correlation protocol

## Decision question

Can the accepted two-input Gaussian-program/detransposition recurrence be
specialized at fixed rational input correlations and compute the exact
plus-channel feature derivatives through \(F_+^{(9)}(0)\) without changing
the model or replacing the two examples by an effective one-example input?

## Canonical model

Keep exactly the model and metric in `PROTOCOL.md`: two deterministic
unit-RMS inputs, two equal-width hidden layers, raw cubic activation at both
layers, all three parameter blocks trained, equal labels \((1,1)\), and

\[
Q(\rho)=
\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},
\qquad
g=\frac{f_1+f_2}{2},
\qquad
D_+=n\nabla g\cdot\nabla.
\]

Here \(\rho\) is the normalized inner product (cosine similarity), not the
angle itself.  The three precommitted correlations are

\[
\rho\in\left\{0,\frac12,1\right\},
\]

corresponding to angles \(90^\circ,60^\circ,0^\circ\).

For each fixed \(\rho\), compute

\[
F_+^{(k)}(0;\rho)
=\lim_{n\to\infty}E[D_+^k g],
\qquad 0\le k\le9,
\]

with width taken first at every fixed derivative order.  Specializing the
coefficient ring from \(\mathbb Q[\rho]\) to \(\mathbb Q\) before expansion
is permitted.  Collapsing the two sample-indexed Gaussian laws, deleting
cross-example responses, changing the bottom Gram factor, or interpolating
from nearby correlations is forbidden.

## H1 / H0 / inconclusive outcome

- **H1:** Fixed-correlation specialization retains the exact recurrence and
  both coefficient conventions finish through order nine with identical
  rational derivatives at all three correlations.
- **H0:** A valid exact route disagreement or a failed frozen identity shows
  that the proposed specialization is incorrect.
- **Inconclusive:** A route exceeds its resource bound or fails a provenance,
  arithmetic, or execution gate before producing a comparable exact jet.

The result concerns fixed-order formal width-first coefficients only.  It
does not test positive-time convergence or justify a finite-width scalar
closure.

## Primary observable and acceptance gates

The primary output is the exact rational vector

\[
\bigl(F_+^{(0)}(0;\rho),\ldots,F_+^{(9)}(0;\rho)\bigr)
\]

at each precommitted correlation.  A production result is accepted only if:

1. the ordinary-Taylor and derivative-normalized recurrence assemblers agree
   exactly at every order;
2. readout reflection gives exact zeros at orders \(0,2,4,6,8\);
3. the two sample outputs agree exactly at every order;
4. orders one and three match exact evaluation of the already audited
   symbolic \(\mathbb Q[\rho]\) polynomials in `results_order3.json`;
5. the \(\rho=1\) jet agrees at all ten orders with the independently frozen
   one-input artifact
   `../depth2_gaussian_program/results_order9.json`;
6. every retained coefficient is rational and has no residual symbolic
   \(\rho\)-degree;
7. the direct initialization gradient-block formula for \(F_+'(0;\rho)\)
   agrees exactly;
8. source hashes match the frozen values recorded by the runner.

For \(\rho=0\) and \(\rho=\tfrac12\), orders five, seven, and nine are new.
Their strongest available check is exact agreement of the two independently
normalized recurrence assemblies.  The contracted fixed-batch GNF provides
an additional independently derived check only through order three; it
cannot validate the new higher orders.

## Bounded pilot, production budget, and stopping rule

- One Taylor-route pilot may run through order four at \(\rho=\tfrac12\)
  solely to assess sparse-state growth.  It is not confirmatory evidence.
- Pilot bound: 3 minutes wall time and 4 GiB resident memory.
- Production bound: 20 minutes wall time and 12 GiB resident memory per
  route and correlation.
- Maximum production runs: six, one for each
  (correlation, coefficient-convention) pair.
- Exact arithmetic only; no floating-point reconstruction is admissible.
- A failed identity is a failed computation.  Resource exhaustion is
  inconclusive and does not count against the mathematical method.
- Stop after all six valid runs finish, after the first exact route
  disagreement, or when a required run exceeds its bound.

## Claim boundary

Passing establishes the exact formal derivatives through order nine for the
three frozen correlations under the accepted fixed-order
Gaussian-program/detransposition assumptions.  It does not establish a
symbolic-in-\(\rho\) order-nine polynomial, Taylor-series convergence,
positive-time mean-field existence, global kernel closure, or exact scalar
dynamics for a generic finite-width realization.
