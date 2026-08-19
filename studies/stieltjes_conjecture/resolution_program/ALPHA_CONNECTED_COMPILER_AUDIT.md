# Independent connected-compiler audit of the positive-alpha jet

This audit is algebraically distinct from the Gaussian tensor recurrence in
`block_metric_positive_alpha_jet.py`.  It regrades the accepted connected-tree
compiler directly by the number of first-hidden hits.

For a connected decorated tree \(T\), let

\[
V_{k,r}(T)=\operatorname{coeff}_{\alpha^r}
  (D_a+D_W+\alpha D_u)^kT.
\]

The readout rewrite contributes \(V_{k-1,r}\), the first-hidden rewrite
contributes \(V_{k-1,r-1}\), and a middle-weight rewrite that splits \(T\)
into \(T_1,T_2\) contributes

\[
2\sum_{q=0}^{k-1}\binom{k-1}{q}
 \sum_{r_0=0}^r
 V_{q,r_0}(T_1)V_{k-1-q,r-r_0}(T_2).
\]

Thus the new grade merely extracts a coefficient from the already-proved
Leibniz recurrence; it makes no tensor-program or detransposition assumption.
The exact executable source is `alpha_connected_sector_probe.cpp`.  It imports
the accepted tree canonicalizer and Wick evaluator and retains checked
512-bit unsigned arithmetic.

## Exact overlaps

The connected route reproduced every one of the 30 retained \(\beta=1\)
coefficients at orders \(1,3,5,7,9\).  Against the new tensor jet it then
independently reproduced

- order eleven: powers \(0,1,2,3,4,5,6,11\);
- order thirteen: powers \(0,1,2,3,4\).

Every integer agrees exactly.  The complete values are retained in
`ALPHA_CONNECTED_COMPILER_AUDIT.json`.

There is also a full off-axis gate.  Summing the tensor polynomial at
\(\alpha=1\) gives

\[
F_1^{(11)}(0)=291982832387585872335470592,
\]

exactly the independently accepted connected-compiler value in
`quadratic_compiler/derivatives_order11.json`.

The leading order-eleven coefficient was recomputed by a second organization:
pure-\(D_u\) dependency discovery, independent parallel Wick contraction of
1,301 bases, then a pure-\(D_u\) reconstruction.  It gives

\[
[\alpha^{11}]F_\alpha^{(11)}(0)
=221895065540516313563136.
\]

The order-nine version of that route first reproduced its retained leading
coefficient.  The order-eleven run used 58.99 seconds wall time, 562.57 CPU
seconds, and 500,780 KiB peak RSS with twelve threads.

## Exact commands

From the repository root:

```sh
g++ -O3 -std=c++17 -DNDEBUG \
  studies/stieltjes_conjecture/resolution_program/alpha_connected_sector_probe.cpp \
  -o /tmp/alpha_connected_sector_probe

/tmp/alpha_connected_sector_probe 13 2
```

The displayed probe regenerates

```text
17931688202114583797612298240
```

for \([\alpha^2]F_\alpha^{(13)}(0)\).  Other coefficients use the same command
with the last argument changed.

## Resource boundary

A complete connected-forest recomputation of order thirteen was deliberately
not launched.  Even the special pure-\(D_u\) leading coefficient has 7,741
distinct base contractions.  Six spread-out exact multiplicity-Wick samples
took between 3.29 and 26.26 seconds each, projecting to hours even before the
harder middle coefficients are included.  The broader previously audited
zero-\(W\)-hit order-thirteen inventory has 325,190 bases and an optimistic
10.56-day estimate.

Accordingly this route is a strong partial independent audit, not a claimed
second full order-thirteen production.  Its exact overlaps cover all old
coefficients, thirteen genuinely new order-eleven/order-thirteen
coefficients, the order-eleven leading edge, and one complete strictly
positive off-axis value.
