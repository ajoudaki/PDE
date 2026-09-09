# Two-input raw-cubic plus-channel symbolic-correlation order-nine protocol

## Contract change and primary target

This strengthens, rather than replaces, `ORDER9_FIXED_RHO_PROTOCOL.md`.
The primary target is now the exact polynomial jet

\[
F_+^{(k)}(0;\rho)\in\mathbb Q[\rho],
\qquad 0\le k\le9,
\]

for the same two-input, equal-label, two-hidden-layer raw-cubic model frozen
in `PROTOCOL.md`.  The input Gram remains

\[
Q(\rho)=
\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},
\qquad -1\le\rho\le1.
\]

No numerical interpolation is allowed.  Every coefficient must be produced
directly by exact \(\mathbb Q[\rho]\)-valued Wick contraction.  The fixed
correlations \(0,\tfrac12,1\) remain exact evaluation holdouts and a fallback
result if symbolic state growth exceeds the bound.

## H1 / H0 / inconclusive outcome

- **H1:** Both exact recurrence normalizations compute identical polynomial
  derivatives through order nine within the frozen bound.
- **H0:** A comparable exact route disagreement or failure of a frozen
  algebraic identity invalidates the symbolic computation.
- **Inconclusive:** Exact state growth exceeds a runtime or memory bound.
  This rejects only efficiency through that order, not the underlying
  formal recurrence.

## Acceptance gates

1. Ordinary-Taylor and derivative-normalized assemblies agree
   coefficient-for-coefficient through the highest accepted order.
2. Orders \(0,2,4,6,8\) vanish as exact zero polynomials.
3. The two sample derivative polynomials agree exactly.
4. Orders one and three reproduce `results_order3.json` exactly.
5. Evaluation at \(\rho=1\) reproduces the frozen one-input derivatives at
   every computed order.
6. Evaluation at \(\rho=0,\tfrac12,1\) reproduces the separately computed
   fixed-correlation jets at every computed order.
7. The direct initialization gradient-block formula reproduces
   \(F_+'(0;\rho)\).
8. Exact source hashes and full coefficient lists are recorded.

The three fixed-point checks are evaluations of independently executed
fixed-coefficient recurrences, not interpolation nodes used to construct
the polynomial.

## Precommitted scaling ladder and budgets

Symbolic growth is assessed monotonically:

1. Taylor pilot through order four: at most 5 minutes and 8 GiB.
2. If valid, Taylor probe through order five: at most 10 minutes and 12 GiB.
3. If valid, Taylor probe through order seven: at most 20 minutes and 24 GiB.
4. Attempt Taylor order nine only if the order-seven probe uses at most
   12 minutes and 20 GiB; order-nine bound is 30 minutes and 32 GiB.
5. Run the derivative-normalized route at the highest Taylor order reached,
   under the same bound for that order.

Stop immediately on an exact gate failure.  If a resource bound is crossed,
record the symbolic result only through the highest order for which both
routes finished and matched.  Do not infer missing coefficients from fixed
evaluations.

## Claim boundary

Passing at order nine establishes exact fixed-order formal
\(\mathbb Q[\rho]\) coefficients through \(F_+^{(9)}(0;\rho)\) under the
accepted Gaussian-program/detransposition assumptions.  It does not prove a
Taylor convergence radius, positive-time existence, interchange of an
infinite derivative series with the width limit, or finite-width scalar
closure.
