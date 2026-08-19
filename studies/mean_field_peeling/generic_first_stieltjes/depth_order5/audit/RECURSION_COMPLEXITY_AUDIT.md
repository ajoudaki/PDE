# Hostile audit of the arbitrary-fixed-depth recurrence

## State actually carried

At derivative order five, each reused initialized matrix requires the
following independent deterministic entries:

| family | entries per matrix |
|---|---:|
| forward covariance, orders `0,...,5` | 21 |
| reverse covariance, orders `0,...,4` | 15 |
| forward response `alpha`, `s<k<=5` | 15 |
| transpose response `beta`, `s<=k<=4` | 15 |
| total | 66 |

The producer implementation stores both orientations of the symmetric
covariance tables, hence its raw dictionary counts are 36 and 25 per matrix;
these are storage duplicates of the 21 and 15 independent values, not missing
states.  The response tables retain all 30 chronological slots before parity
zeros are simplified.

The equations in `primary/ARBITRARY_DEPTH_RECURSION.md` include every required
nonlocal-in-time dependency: the `alpha` sum over earlier reverse uses, the
`beta` sum over all chronologically available forward uses (including the
same-order forward use), and every integrated rank-one update.  Coefficients
inside these slots depend on the complete earlier forward/reverse chronology,
but that dependency is carried by deterministic arithmetic DAGs; it is not
silently discarded.

Thus, at fixed derivative order, the registry size is exactly `66(H-1)` and
the outer schedule is one forward/reverse sweep per Taylor order.  This is a
valid arbitrary-*fixed*-depth construction.  It is not one global
constant-state scalar recurrence: memory is linear in the number of matrices.

## Formula-size attack

The flat tagged `C` polynomial sizes are

| hidden depth | terms |
|---:|---:|
| 2 | 1,045 |
| 3 | 27,421 |
| 4 | 462,776 |

The corresponding primary factored-DAG reachable-node counts are 1,105,
2,320, and 3,536.  Consequently:

- `O(H)` registry transitions do not imply `O(H)` arithmetic time when DAG
  operations and canonicalization costs are charged;
- the near-linear DAG-node growth observed only through `H=4` is evidence,
  not an arbitrary-depth complexity theorem;
- fully distributing layer-tagged products already grows by factors about
  26.2 and 16.9 across the two available increments;
- there is no depth-uniform compact flattened formula and no result for
  `H=H(n)`.

The self-contained report states all four qualifications.  Its factored CSE
appendices are legitimate terminal formulas because their leaves are only
rationals, `Q0`, and declared one-dimensional activation moments; they are
not instructions to run the response recursion.

## Deep-linear closed form

The independently proved controls stop at `H=3,4`.  The displayed formulas
for general-depth linear `B_H,C_H` interpolate the exact Route-S values through
`H=10`, but no transfer classification or degree bound has been proved.
They must therefore remain conjectures.  The final report does label them as
finite-difference discoveries and does not use them to certify the generic
maps.
