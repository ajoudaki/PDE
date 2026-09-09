# Raw-cubic depth-2 derivatives through order nine

## Result

For the raw activation \(\phi(x)=x^3\), two equal-width hidden layers,
standard Gaussian initialization, input Gram one, and all parameter blocks
trained with unit metric, the exact width-first jet is

| \(k\) | \(F^{(k)}(0)\) |
|---:|---:|
| 0 | 0 |
| 1 | 305,775 |
| 2 | 0 |
| 3 | 154,118,008,098,000 |
| 4 | 0 |
| 5 | 302,467,842,967,104,331,335,000 |
| 6 | 0 |
| 7 | 1,412,600,607,141,756,021,360,853,290,900,000 |
| 8 | 0 |
| 9 | 12,844,661,809,234,735,951,068,178,383,554,688,801,750,000 |

Here

\[
F^{(k)}(0)=\lim_{n\to\infty}D_n^kf_n,
\qquad
D_n=n\nabla f_n\cdot\nabla,
\]

with the model fixed in `PROTOCOL.md`.

## Validation record

- Frozen protocol SHA-256:
  `a50e6414bf17176a3f30b6f3735aec69ae712afad28a05f01d2ba2c03ed0f2a2`.
- Exact program SHA-256:
  `edb16223deb34586019a936809eec8cd7553c9eeea10e1cc957a6984a122af72`.
- The ordinary-Taylor and derivative-normalized routes agreed exactly at all
  ten orders.
- Both routes reproduced the independently frozen cubic controls at orders
  one and three.
- Both routes reproduced the order-five value obtained by exact evaluation
  of `LAYER_SEPARATED_ABC_NORMAL_FORM.txt` at `(0,0,0,1)`.  That source
  artifact has SHA-256
  `5219b3558aec52a2065b93ba7d6ce0e350ee930c2048518fcd012ba61f605ec9`.
- Orders \(0,2,4,6,8\) vanished exactly, as required by readout parity.
- Every output was an integer.
- Under the frozen 4 GiB and 10-minute per-route bound, the order-nine run
  took 2.492 seconds for the Taylor route and 2.450 seconds for the
  derivative-normalized route on the audit host.
- At order nine the largest retained sparse polynomial was \(B_9\), with
  256 monomials.  The two exact Wick caches contained 13,030 column moments
  and 24,131 row moments.

## Interpretation

The experiment accepts the frozen hypothesis through order nine: changing
the activation from raw quadratic to raw cubic does not break the
Gaussian-program/detransposition method for this two-hidden-layer network.
The feature flow and moment degrees change, but the calculation still closes
chronologically and remains far inside the stated resource bound.

This result is limited to the formal width-first derivatives through order
nine.  It does not assert convergence of the positive-time Taylor series,
an all-order formula, or the same performance for arbitrary depth or
activation.
