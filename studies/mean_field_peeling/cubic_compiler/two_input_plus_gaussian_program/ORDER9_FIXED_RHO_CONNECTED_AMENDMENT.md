# Fixed-correlation order nine: connected-scalar amended route

## Prior fixed-correlation attempt

The six planned explicit Gaussian-polynomial runs were not completed.  The
three Taylor order-nine jobs at \(\rho=0,\tfrac12,1\) each reached the
20-minute cap and were terminated with exit status 130.  No order-nine
values were emitted, so those attempts are **inconclusive**.

## Amended exact representation

Use the cubic connected-tree recursion already audited
coefficient-for-coefficient through \(F_+^{(5)}(0;\rho)\), including its
plus-channel global color quotient.  Before terminal contraction, specialize
every occurrence of \(\rho\) to one of

\[
0,\qquad \frac12,\qquad 1.
\]

The scalar coefficient ring is:

- checked multiprecision integers for \(\rho=0,1\);
- exact dyadic rationals for \(\rho=\tfrac12\).

The two sample colors, the cross-example derivative rewrites, and both
occurrences of the Gram geometry remain in the tree recursion.  Fixed
specialization is evaluation of exact coefficients, not replacement by a
one-input model.

## Frozen gates

1. Through order five, scalar connected values equal exact evaluation of the
   accepted \(\mathbb Q[\rho]\) polynomials.
2. At \(\rho=1\), all orders equal the frozen one-input order-nine jet.
3. At every correlation, even orders vanish and raw values have the required
   \(2^{k+1}\) normalization.
4. The scalar and polynomial connected sources traverse identical canonical
   rewrite keys through order five.
5. The direct and quotient terminal evaluators agree on the audited
   lower-order source keys before specialization.
6. Source hashes and exact rational outputs are recorded.

## Scaling ladder and hard stop

1. Run \(\rho=1\) through order seven under 8 minutes and 16 GiB.
2. If it passes, run \(\rho=1\) through order nine under 30 minutes and
   32 GiB.  This is the decisive independent one-input endpoint gate.
3. Only after the endpoint passes, run \(\rho=0\) and \(\rho=\tfrac12\)
   through order nine, each under the same 30-minute and 32 GiB cap.
4. No further implementation amendment or resource increase is authorized
   after a scalar order-nine timeout.

A timeout is inconclusive.  A completed value is accepted only after all
available lower-order and endpoint gates pass.

## Claim boundary

Passing gives exact formal derivatives through order nine at the three
listed correlations.  It does not reconstruct the missing symbolic
\(F^{(7)}(\rho)\) or \(F^{(9)}(\rho)\), and it does not strengthen any
positive-time, convergence, or finite-width claim.
