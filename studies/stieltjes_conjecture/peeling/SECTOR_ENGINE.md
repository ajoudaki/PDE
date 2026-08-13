# Exact Wick-pair sector engine

`sector_engine_checked.cpp` is the checked-512-bit exact implementation used
for the fixed-W-hit computations.  `sector_parallel.cpp` discovers the
dependency DAG, evaluates distinct base trees in parallel, checkpoints a
sorted value prefix, and reconstructs sectors.  `sector_parallel_reuse.cpp`
imports a completed source-sector checkpoint by canonical key and stores new
target values as restart-safe `hex(key) decimal-value` records.

## Exact grading and contraction proof

Let `A[k,w](T)` be the leading expectation after `k` further derivatives of a
connected decorated tree `T`, restricted to exactly `w` differentiations of a
W factor.  The a- and h-rewrites contribute `A[k-1,w]`.  A W-rewrite splits
`T` into `T1,T2` and contributes

```
2 sum(q=0..k-1) C(k-1,q)
  sum(s=0..w-1) A[q,s](T1) A[k-1-q,w-1-s](T2).
```

This is the Leibniz rule with a monotone counter: an a/h hit does not change
`w`, while a W hit increments it once.  Starting from one Wick pair, the
reported covariance-pair sector is `P=k+1-w`.

At a connected base with `2P` raw W edges, a leading quotient has `P+1`
vertices and `P` covariance edges.  Its image is connected, hence it is a
tree.  Therefore every occupied row-block/column-block cell contains exactly
two raw edges.  Conversely, every bipartition-respecting vertex partition
into `P+1` blocks whose cell occupancies are all zero or two specifies the
unique Wick pairing in each occupied cell.  `VertexPartitionWickEvaluator`
enumerates precisely these partitions and attaches the Gaussian double
factorial moments.  Cell occupancy above two is monotone and is pruned.

Mode 4 is an exact portfolio, not an approximation: for each canonical base
it uses the vertex-partition evaluator when the smaller bipartition side has
at most eleven vertices and the audited multiplicity evaluator otherwise.  Both
sum the same Wick contractions.  Checked `uint512` arithmetic throws on
overflow; the order-13 analytic bound is 275 bits.

## Build and strict audit

```sh
g++ -std=c++17 -O3 -DNDEBUG -fopenmp \
  studies/stieltjes_conjecture/peeling/sector_parallel.cpp \
  -o /tmp/sector_parallel
g++ -std=c++17 -O3 -DNDEBUG -fopenmp \
  studies/stieltjes_conjecture/peeling/sector_parallel_reuse.cpp \
  -o /tmp/sector_parallel_reuse

# Strict D9 P10..P1 gate (must equal the vector in README.md).
OMP_NUM_THREADS=12 /tmp/sector_parallel 9 0 9 /tmp/d9-sector.chk 4

# D11 P11 after accepting the independently exhaustive P12 value.
OMP_NUM_THREADS=12 /tmp/sector_parallel 11 1 1 /tmp/d11-w1.chk 4

# D11 P10, reusing all canonical base values from P11.
OMP_NUM_THREADS=12 /tmp/sector_parallel_reuse \
  11 1 /tmp/d11-w1.chk 2 /tmp/d11-w2.sparse 4

# Checkpointed D13 P14 attempt.
OMP_NUM_THREADS=12 /tmp/sector_parallel 13 0 0 /tmp/d13-w0.chk 4
```

The accepted D11 high-sector integers and audit metadata are recorded in
`d11_high_sectors_exact.txt`.
