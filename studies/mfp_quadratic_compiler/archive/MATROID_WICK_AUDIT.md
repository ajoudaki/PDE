# GF(2)/matroid Wick shortcut: restricted theorem and rejected generalization

`matroid_wick_evaluator.cpp` was developed as an alternative evaluator for a
connected decorated bipartite tree.  A later adversarial audit found that its
rank gate is not exact on arbitrary decorated trees.  The source is retained
as a failed acceleration experiment and must not be substituted for the
accepted vertex-partition or multiplicity evaluators.  Only the restricted
no-`W`-hit theorem below survives.

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

Within the no-`W`-hit sector, the theorem is used only when
`C - column_blocks == r`.  Every enumerated row block must also have even `a`
exponent and even raw-`W` degree.  These hypotheses are essential; the
unrestricted portfolio claim made in an earlier version of this note was
false.

## Counterexample to unrestricted exactness

Take rows `r0,r1,r2`, columns `c0,c1,c2,c3`, row decorations
`a=(2,1,1)`, column decorations `h=(1,1,1,1)`, and edges

```text
r0-c0, r0-c1, r0-c2, r0-c3, r1-c0, r2-c0.
```

The exact vertex-partition evaluator returns `27`, whereas the matroid
evaluator returns `0`.  In particular, the row partition
`{r0},{r1,r2}` and column partition `{c0,c1},{c2,c3}` is a valid leading
zero-or-two-cell configuration and contributes `9`, but the shortcut rejects
it because the row-signature rank is one rather than two.  Therefore the rank
gate is unsafe outside the proved no-`W`-hit/even-row setting.

## Regression gates

Before this counterexample was found, the implementation was checked base-by-base against the independent
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

Those regressions remain useful evidence about the tested states, but they do
not repair the general counterexample and do not authorize use on new state
families.

Build and run the full D9 gate with:

```sh
g++ -std=c++17 -O3 -DNDEBUG -fopenmp \
  studies/mean_field_peeling/quadratic_compiler/archive/matroid_sector_driver.cpp \
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
