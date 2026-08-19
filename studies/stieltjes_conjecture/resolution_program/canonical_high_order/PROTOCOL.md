# Canonical high-order jet successor

Status: frozen before the first order-fifteen production run, 18 August 2026.

## Decision question

For the canonical one-input quadratic network with block metric

\[
D_{1,1}=D_a+D_u+D_W,
\]

extend the proved fixed-order Gaussian-program recurrence from the retained
jet through order thirteen to the exact canonical derivative
\(F^{(15)}(0)\).  If that extension is computationally comfortable under the
branch rule below, continue once to \(F^{(17)}(0)\).

This is a fixed-order width-limit calculation.  It does not assert a
positive-time trajectory limit or convergence of the full Taylor series.

## Primary outputs

1. Exact integers \(F^{(k)}(0)\) for every \(0\leq k\leq15\), including a
   new exact \(F^{(15)}(0)\).
2. Exact series inversion through \(\mu_6\), and every newly decidable
   ordinary or shifted canonical Hankel determinant.
3. Conditional branch only: exact \(F^{(17)}(0)\), \(\mu_7\), and its newly
   decidable shifted determinant.

The order-fifteen calculation makes the ordinary
\(4\times4\) determinant

\[
\det(\mu_{i+j})_{i,j=0}^{3}
\]

decidable.  The order-seventeen branch additionally makes the shifted
\(4\times4\) determinant

\[
\det(\mu_{i+j+1})_{i,j=0}^{3}
\]

decidable.

## Exact validity gates

1. Every retained canonical derivative through order thirteen must be
   reproduced exactly before a new value is accepted.
2. All even derivatives through the requested terminal order must vanish.
3. Two implementation routes that do not import one another's candidate
   result must reproduce each accepted new derivative exactly.
4. Downstream moments and determinants use exact rational arithmetic.  A
   floating-point sign or numerical reconstruction is not evidence.
5. A negative ordinary or shifted Hankel determinant is a canonical V1
   counterexample at that finite order.  A positive determinant is only one
   additional finite-order compatibility result, never an all-order proof.

## Resource and branch rule

- Production order fifteen: at most 15 minutes wall time and 4 GiB peak
  resident memory.
- Independent order fifteen: at most 20 minutes wall time and 4 GiB peak
  resident memory.
- Order seventeen is authorized only if the production order-fifteen run
  finishes within its cap, passes every gate, and its measured state/cache
  growth supports an estimate below 30 minutes and 8 GiB for order seventeen.
- Each order-seventeen implementation, if launched, has a hard 30-minute and
  8-GiB cap.  No order nineteen branch is authorized.
- A timeout, memory breach, failed prefix gate, or disagreement between the
  two exact routes is terminally inconclusive for that order.

## Interpretation

The smallest decisive output is the sign of the newly available canonical
Hankel determinant.  The calculation updates only the finite formal-moment
rung.  It cannot establish moment determinacy, identify a global neural
curve, or prove the canonical all-order Stieltjes conjecture from positive
finite prefixes.
