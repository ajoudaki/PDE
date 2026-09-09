# Canonical hidden preactivation norms through order sixteen and Ward order eighteen

Status: **accepted exact finite-order computation**, 19 August 2026.

## What is—and is not—the Stieltjes observable

For the canonical one-input quadratic network, the polynomial hidden
observables are the squared preactivation RMS values

\[
Q_1(s)=\mathbb E[u(s)^2],\qquad Q_2(s)=\mathbb E[z(s)^2],
\]

with \(Q_1(0)=1\) and \(Q_2(0)=3\).  Put \(G=F^{-1}\),
\(N_j(y)=Q_j(G(y))\), and \(x=y^2\).  The two tested companion series are

\[
\frac{N_1(\sqrt x)-1}{x}=\sum_{r\ge0}(-1)^r\rho_rx^r,
\qquad
\frac{N_2(\sqrt x)-3}{x}=\sum_{r\ge0}(-1)^r\nu_rx^r.
\]

This is an output-coordinate statement, not a claim that either hidden norm
is Stieltjes in physical training time.  The first response is inherited from
the output conjecture through the exact Ward identity

\[
Q_1'(s)=8F(s),
\]

whereas the second response is a genuinely independent companion conjecture.

Literal RMS is also covered.  We tested the rational moment sequences in

\[
\frac{\sqrt{N_j(\sqrt x)/N_j(0)}-1}{x}
=\sum_{r\ge0}(-1)^r\omega^{(j)}_rx^r.
\]

The unnormalized second-layer RMS sequence is \(\sqrt3\,\omega^{(2)}\), a
common positive factor that cannot change a Hankel sign.

## Exact hidden jets

Two isolated exact Gaussian-program recurrences agree on the entire feature
jet through order seventeen and on both hidden jets through order sixteen.
The new nonzero derivatives are

| order | \(Q_1^{(k)}(0)\) | \(Q_2^{(k)}(0)\) |
|---:|---:|---:|
| 10 | 9449289134603204493312 | 487967758483103808178176 |
| 12 | 2335862659100686978683764736 | 145387231337138218955012063232 |
| 14 | 822828098233973314828964208181248 | 60684843616663232253966043066638336 |
| 16 | 392633476632616859814117035223934304256 | 33941339036399103897550977212861900095488 |

Every odd hidden derivative through order fifteen vanishes exactly.  The Ward
identity additionally gives

\[
Q_1^{(18)}(0)=8F^{(17)}(0)
=244447759152768795963558845204174218993336320.
\]

This supplies the ninth first-hidden moment without computing
\(F^{(19)}(0)\).  The second-hidden branch stops at \(Q_2^{(16)}(0)\), as
frozen.

## Squared-RMS moments

The exact rational values are retained in
[HIDDEN_MOMENT_HANKEL_AUDIT.json](HIDDEN_MOMENT_HANKEL_AUDIT.json).  Their
decimal values are

| \(r\) | first hidden \(\rho_r\) | second hidden \(\nu_r\) |
|---:|---:|---:|
| 0 | 0.03603603603603604 | 0.5020696372047724 |
| 1 | 0.01110082897933568 | 0.1207670309680934 |
| 2 | 0.005300110514806151 | 0.05443398035412124 |
| 3 | 0.003029492778031199 | 0.03030837122899150 |
| 4 | 0.001910358591145997 | 0.01882835199368644 |
| 5 | 0.001281662698829191 | 0.01251048885167848 |
| 6 | 0.0008973702602433460 | 0.008700364350576971 |
| 7 | 0.0006482174161243495 | 0.006253439819099579 |
| 8 | 0.0004795223862277053 | -- |

Thus the calculation extends the previously retained second-hidden sequence
from four moments to eight.  It supplies nine moments for the first-hidden
response because of the Ward identity.

## Exact Hankel verdict

For a moment sequence \(m\), write

\[
H_d=(m_{i+j})_{i,j=0}^d,
\qquad
H_d^+=(m_{i+j+1})_{i,j=0}^d.
\]

Every accessible matrix is positive definite, and every nonempty principal
minor is strictly positive.

| observable | moments | largest ordinary gate | determinant | largest shifted gate | determinant |
|---|---:|---:|---:|---:|---:|
| first hidden squared RMS | 9 | \(H_4\succ0\) | \(6.491699822806497\times10^{-21}\) | \(H_3^+\succ0\) | \(1.469342142818156\times10^{-16}\) |
| second hidden squared RMS | 8 | \(H_3\succ0\) | \(9.816612856790002\times10^{-10}\) | \(H_3^+\succ0\) | \(2.629245972991328\times10^{-12}\) |
| first hidden normalized RMS | 9 | \(H_4\succ0\) | \(2.045229473997248\times10^{-22}\) | \(H_3^+\succ0\) | \(9.859501690272903\times10^{-18}\) |
| second hidden normalized RMS | 8 | \(H_3\succ0\) | \(8.609531236307642\times10^{-13}\) | \(H_3^+\succ0\) | \(3.324737566200535\times10^{-15}\) |

For each first-hidden sequence this means 46 distinct principal minors in the
two maximal matrices (83 evaluations when every nested accessible size is
listed).  For each second-hidden sequence it means 30 distinct principal
minors in the two maximal matrices (52 nested evaluations).  The JSON
certificates retain every exact rational matrix entry and minor; the decimal
determinants above are descriptive only.

## Validation

The production route completed in 228.136 seconds with 189.496 MiB peak RSS.
The independent sparse representation completed in 158.110 seconds with
95.852 MiB peak RSS.  Both reproduced the accepted Campaign-1 \(Q_1,Q_2\)
jets through order eight, the canonical feature jet through order seventeen,
all parity zeros, and the Ward identity before any new value was accepted.

Two downstream routes then agreed exactly:

1. direct reversion of \(F\), followed by composition in \(y\); and
2. algebraically separate reversion of \(x=rA(r)^2\), followed by composition
   of the even hidden jets in \(r=s^2\).

The second route also reproduced the first-hidden moments independently from
the reciprocal-kernel Ward formula.  The complete directory test suite has
15 passing tests.

## Interpretation

There is no finite-order hidden-norm falsification through the newly reached
orders.  Both hidden layers, including literal RMS after normalization, are
strictly compatible with every Stieltjes Hankel condition that these jets can
decide.

This remains finite-order evidence.  It does not prove the independent
all-order second-hidden companion conjecture, the canonical output
conjecture, moment determinacy, or identification with a global neural
trajectory.
