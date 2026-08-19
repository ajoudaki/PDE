# Research contract: order five across hidden depth

**Status:** frozen before the depth-three and depth-four coefficient maps are
compared.

## Canonical model and limit

For one input with \(Q^0=\lVert x\rVert^2/d_0\), \(H\geq1\) hidden layers,
standard independent Gaussian initialization, and a shared activation
\(\phi\), use

\[
z^1=W^1x/\sqrt{d_0},\qquad
z^\ell=W^\ell\phi(z^{\ell-1})/\sqrt n\quad(2\leq\ell\leq H),
\qquad
f_n=a^T\phi(z^H)/n.
\]

Every parameter is trained and

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,\qquad
F_H^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n].
\]

Differentiate at finite width first.  Width tends to infinity with fixed
\(H\) and one fixed sample.  No Hermite or polynomial approximation of
\(\phi\) is allowed.

## Required coefficients and terminal language

Compute exactly

\[
A_H=F_H'(0),\qquad B_H=F_H^{(3)}(0),\qquad C_H=F_H^{(5)}(0)
\]

for \(H=3,4\), followed by

\[
\mu_{0,H}=\frac{B_H}{2A_H^2},\qquad
\mu_{1,H}=\frac{4B_H^2-A_HC_H}{24A_H^5}.
\]

For arbitrary forward variances, terminal atoms are layer-tagged
one-dimensional expectations

\[
M^{\ell}_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,Q^{\ell-1})}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad Q^\ell=M^\ell_{200000}.
\]

For the clean unit-Gram specialization, identify every layer tag with

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad M_{200000}=1.
\]

An explicit sparse polynomial or a deterministic factored arithmetic DAG is
acceptable.  A terminal answer may not contain tangent variables, backward
carriers, Gaussian innovations, pseudoinverses, implicit Stein derivatives,
or an instruction to run a response recursion.

## Depth-recursion target

Seek a finite-state, layer-local transition which, for every fixed \(H\),
emits \(A_H,B_H,C_H\) into the terminal language above.  Distinguish:

1. an exact response-aware proof intermediate representation;
2. an exact contracted Gaussian-expectation oracle;
3. a fully flattened moment polynomial;
4. the size of the recursive state versus the size of the expanded output.

No \(O(H)\) flat-formula-size claim is permitted merely because the oracle
state has bounded dimension.  No statement uniform in \(H=H(n)\) is in
scope.

## Promotion gates

1. Two routes independently derive and freeze the \(H=3,4\) maps.
2. Literal atomwise comparison has zero discrepancies after matching the
   declared moment quotient.
3. Exact finite-width moving-feature jets agree with an independent raw or
   automatic-differentiation oracle.
4. Readout parity gives \(F_H^{(0)}=F_H^{(2)}=F_H^{(4)}=0\).
5. Constant, affine, and deep-linear controls pass; the deep-linear values
   must be derived independently, not fitted from the generic map.
6. At least one smooth nonpolynomial \(H=3\) and \(H=4\) finite-width
   regression agrees with the frozen prediction under a preregistered
   tolerance.
7. Every equality partition and transpose-response family generated through
   order five is accounted for before the width limit.
8. The annealed theorem states its exact activation regularity and uniform-
   integrability bridge.

Failure to flatten is reported as an unresolved-branch ledger; it is not
replaced by a higher-level recursion.

## Claim boundary

The coefficient theorem is pointwise in fixed \(H\).  It does not establish
positive-time convergence of the neural flow, convergence of the Taylor
series, positivity of the Stieltjes moments, or complexity uniform in depth.
