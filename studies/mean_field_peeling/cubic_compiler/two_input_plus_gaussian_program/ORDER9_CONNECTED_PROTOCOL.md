# Cubic two-input connected-tree compiler: frozen order-nine protocol

## Motivation and canonical target

The explicit sample-indexed Gaussian-polynomial route was exact through
order five but its fixed-correlation order-nine runs exceeded the frozen
20-minute bound.  This protocol tests a representation change that preserves
the same model: connected bipartite raw Wick trees with exact
\(\mathbb Z[\rho]\) coefficients.

The target remains

\[
F_+^{(k)}(0;\rho)
=\lim_{n\to\infty}E[(n\nabla g\cdot\nabla)^k g],
\qquad
g=\frac{f_1+f_2}{2},
\qquad 0\le k\le9,
\]

for two unit-RMS inputs with Gram
\(Q(\rho)=\left(\begin{smallmatrix}1&\rho\\rho&1\end{smallmatrix}\right)\),
raw cubic activation in both hidden layers, and all blocks trained.

The connected representation is adapted from the previously audited
quadratic two-input compiler in
`../../quadratic_compiler/campaign2/two_input_connected.cpp`.  It is
not allowed to change the activation, sample count, Gram placement, metric,
channel, or width-first limit.

## Exact raw-tree rewrites

Use \(A_+=f_1+f_2=2g\) and
\(\widetilde D_+=2n\nabla g\cdot\nabla\).  If
\(J_k=E[\widetilde D_+^k A_+]\), then

\[
F_+^{(k)}(0;\rho)=\frac{J_k(\rho)}{2^{k+1}}.
\]

A row vertex carries a power of the readout Gaussian \(a\); a column vertex
carries the exponent pair of \((u^1,u^2)\); edges are raw middle-layer
Gaussian factors.  For a sample color \(\alpha\):

1. an \(a\)-hit replaces one \(a\) by three new
   \(u_\alpha^3\) columns attached to that row;
2. a \(u_\beta\)-hit has factor \(9Q_{\beta\alpha}\), replaces the hit
   \(u_\beta\) by \(u_\alpha^2\), and attaches a fresh \(a\)-row to the hit
   column and to two new \(u_\alpha^3\) columns;
3. a middle-weight hit has factor \(3\), removes the hit bridge, multiplies
   its column by \(u_\alpha^3\), increments the row \(a\)-power, and attaches
   two new \(u_\alpha^3\) columns to that row.

The root for sample \(\alpha\) is one \(a\)-row attached to three
\(u_\alpha^3\) columns.  Every rewrite toggles both edge parity and total
\(a\)-parity, so only odd derivative orders can survive.

Terminal expectations use exact row Gaussian moments, exact bivariate
column moments, and the same leading-width bipartition-respecting vertex
partition contraction as the audited quadratic parent.

## H1 / H0 / inconclusive outcome

- **H1:** The cubic connected compiler reproduces the independent
  Gaussian-program polynomials through order five and computes the exact
  symbolic jet through order nine within the bound.
- **H0:** Any exact discrepancy through order five, endpoint mismatch, parity
  violation, nonintegral normalization, or disagreement between the two
  terminal evaluators invalidates the compiler.
- **Inconclusive:** Resource exhaustion at order seven or nine leaves the
  connected representation unresolved at that order.

## Frozen gates

1. \(F^{(0)},F^{(2)},F^{(4)},F^{(6)},F^{(8)}\) are exact zero polynomials.
2. Orders one and three match `results_order3.json`
   coefficient-for-coefficient.
3. Order five matches both exact Gaussian-program coefficient conventions
   coefficient-for-coefficient.
4. At \(\rho=1\), every order through nine matches
   `../depth2_gaussian_program/results_order9.json`.
5. The direct vertex-partition terminal evaluator and the independent
   quotient-Wick evaluator agree on every terminal tree reached through
   order three and on a source-key-complete order-five audit.
6. Each raw polynomial coefficient is divisible by \(2^{k+1}\) before
   reporting \(F_+^{(k)}\).
7. Exact evaluation at \(\rho=0,\tfrac12,1\) agrees with every separately
   completed fixed-correlation Gaussian-program order.
8. The adapted source, parent source, protocols, and accepted inputs are
   hash-gated.

## Scaling ladder and hard stop

- Compile with optimization and checked multiprecision integers.
- Order-five pilot and full lower-order audit: 5 minutes and 8 GiB.
- Order-seven production: 20 minutes and 24 GiB.
- Order nine is authorized only if order seven finishes in at most
  12 minutes and 20 GiB.
- Order-nine production: 30 minutes and 32 GiB.
- One production run per authorized maximum order; cached lower orders are
  emitted from the same run.
- Stop on the first failed exact gate or resource cap.  Do not enlarge a cap
  after observing a timeout.

## Claim boundary

A pass establishes exact formal fixed-order polynomials under the accepted
leading-width connected-tree and detransposition assumptions.  It does not
prove convergence of the derivative series, a positive-time width limit, or
finite-width scalar closure.
