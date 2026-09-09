# Finite-width boundary-layer results

The panel in `FINITE_WIDTH_PROTOCOL.md` and its only authorized extension were
run without changing any decision threshold.

## Event-time panel

The signed residual-halving times were

| width | event times | median |
|---:|---|---:|
| 32 | 0.00174658, 0.00797715, 0.01108569, 0.01985657, 0.00294061, 0.00256939 | 0.00545888 |
| 64 | 0.00273702, 0.00257015, 0.00161348, 0.00383559, 0.00247188, 0.00273385 | 0.00265200 |
| 128 | 0.00267022, 0.00391047, 0.00182569, 0.00247682, 0.00423715, 0.01190240 | 0.00329035 |
| 256 | 0.00206921, 0.00206099, 0.00568814, 0.00449775, 0.00155025, 0.00249200 | 0.00228061 |
| 512 | 0.00357577, 0.00341781, 0.00329372, 0.00211547 | 0.00335577 |

The successive median ratios are approximately

\[
0.486,qquad 1.241,qquad 0.693,qquad 1.471.
\]

## Validity gates

Every solve reached the event, every solver reported success, and the sampled
residual magnitude was monotone.  The largest invariant error was below
\(1.2\times10^{-11}\).  Tightening the tolerances by ten on the frozen
\(n=128\) audit seed left the reported event time unchanged.  The mean
initial kernel at \(n=512\) was \(110.980\), essentially the exact limit
\(111\), so all numerical validity gates passed.

## Frozen verdict

Neither preregistered hypothesis passes.  The last two ratios are not both in
\([0.8,1.2]\), so H1 does not pass; they are not both below \(0.75\), so H0
does not pass.  The result is therefore **inconclusive**.  In particular, this
small panel supplies no evidence for a monotone width-shrinking boundary
layer, but it is not a compact-time convergence theorem.
