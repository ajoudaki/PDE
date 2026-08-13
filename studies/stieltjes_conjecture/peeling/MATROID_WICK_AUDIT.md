# GF(2)/matroid Wick evaluator audit

`matroid_wick_evaluator.cpp` is an exact alternative evaluator for a connected
decorated bipartite tree. It enumerates parity-valid row partitions and uses
the existing exact column DP except in the tight-nullity case, where binary
matroid components determine the column partition directly.

## Tight-nullity theorem

In the no-W-hit sector every raw row has even degree. The original row
incidence vectors are therefore linearly independent over GF(2): a nonempty
dependence would select a nonempty subgraph in which every selected row and
every incident column has even degree, but a finite nonempty forest always has
a leaf.

After quotienting the rows into `r` blocks, their parity incidence vectors
still have rank `r`. Thus a column partition making every row-block/column-block
cell even requires at least `r` column identifications. When exactly `r`
identifications are allowed, every column block has nullity one and the blocks
are precisely the connected components of the represented binary matroid.
The evaluator obtains these components from fundamental circuits, checks that
each component is a circuit, and then multiplies the ordinary Gaussian double
factorial moments using the full integer cell decorations.

The theorem is only used when `C - column_blocks == r`. All other cases use
the pre-existing exact `ColumnDP`; the portfolio is exact, not approximate.
Every enumerated row block is also required to have even `a` exponent and even
raw-W degree.

## Regression gates

The accepted implementation was checked base-by-base against the independent
vertex-partition evaluator on all 317 D7/P8 bases. It also reproduced all ten
accepted D9 sectors exactly:

```text
P10 87101527431460847616
P9  285610646257352368128
P8  385587855340280672256
P7  277387051973394751488
P6  114581150906254331904
P5  27185927724027592704
P4  3490984312448606208
P3  211436756895006720
P2  4546495309086720
P1  14627977297920
```

Build and run the full D9 gate with:

```sh
g++ -std=c++17 -O3 -DNDEBUG -fopenmp \
  studies/stieltjes_conjecture/peeling/matroid_sector_driver.cpp \
  -o /tmp/matroid_sector_driver
OMP_NUM_THREADS=4 /tmp/matroid_sector_driver 9 0 9
```

## Superseded D13 benchmark

An exploratory shortcut forced singleton row blocks for D13/P14 bases with 14
rows and reported an apparent subtotal and millisecond timing. That shortcut
was invalid: it omitted the even-`a` Gaussian parity condition. The reported
subtotal `47918983440444991875` and timing `0.0106489 s` are retracted and must
not be used. The shortcut does not appear in the preserved source.

The earlier correct 100-base benchmark did not complete under the short cap,
so no exact R=14 family subtotal, recurrence-weighted P14 value, or credible
runtime estimate is certified.
