# Exact mean-field peeling engine

This directory contains a computer-algebra implementation of the leading-width
peeling calculation for the one-sample, two-hidden-layer quadratic network at
`gamma=1`.  It computes

\[
F^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n],
\qquad
D_n=n\nabla f_n\mathbin\cdot\nabla,
\]

directly in exact integer arithmetic.

`source_hashes.txt` intentionally retains the pre-consolidation filenames that
were frozen with the certified runs.  The one preserved binary,
`export_evaluator_checked512`, is part of the accepted order-eleven provenance;
other exploratory build products have been removed from the live study.

## Scalarized state

A monomial is encoded by a decorated bipartite forest:

- each row vertex is an index `i` and stores the exponent of `a_i`;
- each column vertex is an index `j` and stores half the exponent of `u_j`;
- each edge `(i,j)` is one factor `W_ij`.

The root is `a_i W_ij W_ik u_j^2 u_k^2`.  Applying `D_n` to a scalar factor
has exactly three graphical rewrites:

1. hitting `a_i` adds two fresh `W` edges from row `i`;
2. hitting `u_j^(2p)` adds a fresh row with one edge to `j` and one edge to a
   fresh column, with coefficient `8p`;
3. hitting `W_ij` removes that edge, increments the decorations at its
   endpoints, adds one fresh edge from row `i`, and has coefficient `2`.

The first two operations preserve connectedness.  The third deletes a bridge
of a tree, so it splits one connected component into exactly two.

## Why leading Wick contractions factor

Suppose a forest has `r` original components and `2P` weight edges.  A Wick
pairing turns every pair of weight edges into one covariance edge after
identifying their row endpoints and their column endpoints.  Let the quotient
covariance graph have `V` vertices, `c` connected components, and cycle rank
`beta`.  Because it has `P` edges,

\[
V=P+c-\beta.
\]

The scalarized monomial has width normalization `n^(-(P+r))`; hence its
leading expectation requires `V=P+r`.  Since pairing can only merge original
components, `c<=r`, and `beta>=0`.  Equality therefore forces `c=r` and
`beta=0`.  No leading covariance pair joins two original components, and each
component's quotient covariance graph is a tree.  Consequently the leading
expectation factors exactly over the original forest components.

## Connected recursion

Let `A_k(C)` be the leading expectation after `k` further applications of
`D_n` to a connected decorated tree `C`.  For `k=0`, `A_0(C)` is evaluated by
an exact Wick-pairing dynamic program; it keeps only quotient forests with
`P+1` free row-plus-column index classes and multiplies the remaining Gaussian
moments as double factorials.

For `k>0`, apply one graphical rewrite.  A row or column hit gives one child
tree `C'` and contributes its rewrite coefficient times `A_(k-1)(C')`.  A
weight hit produces two children `C_1,C_2`; the remaining `k-1` derivations
distribute over them by the exact Leibniz rule:

\[
2\sum_{q=0}^{k-1}\binom{k-1}{q}
A_q(C_1)A_{k-1-q}(C_2).
\]

Canonical unrooted colored-tree keys memoize `A_k(C)`.  Global parameter
negation supplies an exact parity prune.  The implementation also records root
contributions by the first hit (`a`, `u`, or `W`).

## Independent audit routes

- `component_recursion.cpp` is the compressed connected recurrence.
- `exhaustive_reference.cpp` expands every global derivative forest first and
  contracts afterward.  It is much slower but mathematically independent of
  the Leibniz convolution.
- `export_evaluator_reference.cpp` evaluates exported exhaustive forests by a
  second equality-partition/Wick implementation.
- `graph_compiler_reference.py` is the earlier transparent Python prototype.
- `finite_width_jet_reference.py` gives a finite-width formal-jet recurrence
  for numerical pilots; it is not an exact mean-field certificate.

The current exact regression values are

```text
D^1 f = 111
D^3 f = 1685184
D^5 f = 77400633120
D^7 f = 7315868433079296
D^9 f = 1181161141825400561664
```

The exhaustive `D^9` audit decomposes the last integer by the number `P` of
Wick covariance pairs:

```text
P=1   14627977297920
P=2   4546495309086720
P=3   211436756895006720
P=4   3490984312448606208
P=5   27185927724027592704
P=6   114581150906254331904
P=7   277387051973394751488
P=8   385587855340280672256
P=9   285610646257352368128
P=10  87101527431460847616
```

Their sum is the stated `D^9 f`.  Dividing by `9!`, reverting `F`, and
substituting into `K=F' o F^(-1)` reproduces the already-audited coefficient

\[
[y^8]K(y)=
-\frac{21749547365571716077696}{13618704359108797313085}.
\]

This is a strict regression gate: order 11 or 13 output is not accepted unless
all five values above are reproduced exactly.
