# D13/P14 exact attempt (partial certificate)

Date: 2026-08-12 (Europe/Zurich).

## Certified facts

For order 13 and `W_hits=0` (`P=14`), dependency discovery found exactly
465,075 graded recurrence states and 325,190 distinct canonical base trees.
The file

```text
/tmp/sector_d13_w0_adaptive.chk
```

contains the exact checked-512-bit Wick values for the first 704 bases in the
lexicographically sorted canonical-key list produced by `SectorDiscovery`.
It has 704 decimal lines, 7,473 bytes, and SHA-256

```text
0ba6dd99a95267a542f90df5e1ac951948363ed0f6665c4a495882383e8342a2
```

The command was

```sh
bash -c 'ulimit -v 8388608; exec /usr/bin/time -v \
  env OMP_NUM_THREADS=12 /tmp/component_sector_parallel_adaptive11 \
  13 0 0 /tmp/sector_d13_w0_adaptive.chk 4'
```

The final binary SHA-256 was

```text
5e8cb68b0f8547c447823b5c43cb1810499478ff7613bf748a60b63888d66c3c
```

Mode 4 selected the vertex-partition evaluator when the smaller bipartition
side had at most 11 vertices and the audited multiplicity evaluator otherwise.
This crossover was accepted only after reproducing all ten D9 sectors exactly:

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

The gate used 58.05 seconds wall time and 75,024 KiB peak RSS.

## Why brute force was stopped

The sorted prefix contains difficult leaf-rich 28-edge trees.  Bases 608--639
have bipartition sizes 9x20, 10x19, or 11x18; rows have degrees mainly 4 and
2, while columns have degrees mainly 3, 2, and 1.  The threshold-10 portfolio
needed about 3.5 minutes for that 32-base batch.  On representative base 616
(11x18), multiplicity recursion did not finish within 90 seconds, while the
vertex-partition evaluator returned the exact value 251895015 in 19.86 seconds
of evaluator time.  Raising the crossover to 11 reduced the next batches to
roughly 90 seconds each, still far too slow for 325,190 bases.

Even an unrealistically constant 90 seconds per 32 bases implies

```text
ceil((325190-704)/32) * 90 seconds = 912330 seconds ~= 10.56 days.
```

The observed cost is strongly nonuniform and later bases have larger smaller
bipartition sides, so this is an optimistic lower estimate, not an ETA.  The
run was stopped only after line 704 was atomically checkpointed.

## Rejected checkpoints

The following files use rigorous positive sub-sums, not the full Wick sum, and
must not be merged into the exact checkpoint:

```text
/tmp/sector_d13_w0_first.chk       19040 lines  sha256 abb26552e5a711903d0d79c8ac9f74cc8e28fe1b3b4d66153d87a39e56338d3a
/tmp/sector_d13_w0_first_adj.chk     704 lines  sha256 c6e40c82dc54c210b64d79a7b6b518c97f1b13fdc3ce6a755d213698484a6fff
/tmp/sector_d13_fastadj.chk        92096 lines  sha256 3fb57fedcff4b56d1717f03fa66f857fc79a28228f5ab6c4c56c1bd559004d44
```

`first_wick_only` returns after the first positive Wick child.  On the full D9
P10 base set it reconstructs 3901440889891749888, not the exact
87101527431460847616.  `FastAdjacentWick` retains only a stricter adjacent-edge
sub-sum and reconstructs 1715192207769600.  The first 608 entries of both
families disagree with the exact adaptive entries (the two `first` files agree
with each other on their common prefix).  They are useful lower-bound evidence
only.

## Not certified

No D13/P14 sector scalar, no complete D13 sector, and no D13 total is certified
by this attempt.  The 704 checkpoint values are base-level facts and cannot be
summed without the remaining 324,486 canonical base contractions and exact
recurrence reconstruction.

The accepted implementation is documented in `SECTOR_ENGINE.md`; exact D11
P12/P11/P10 results are in `d11_high_sectors_exact.txt`.
