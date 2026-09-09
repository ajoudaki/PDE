# Primary equality-partition, width, and transpose-response ledger

This ledger covers the primary compiler behind
[`PRIMARY_GAUSSIAN_NORMAL_FORM.md`](PRIMARY_GAUSSIAN_NORMAL_FORM.md).  It
records the internal branches before every temporary Gaussian is eliminated.
No internal symbol listed here survives in the terminal normal form.

## 1. Width accounting primitives

With `M0=W0/sqrt(n)` and ordinary Taylor coefficients:

| operation | finite-width normalization | surviving order |
|---|---:|---:|
| dense forward/transpose multiplication | `n^-1/2 sum` | `O(1)` fresh Gaussian plus responses |
| empirical covariance | `n^-1 sum` | `O(1)` deterministic Gram |
| gradient update `M_m` | `n^-1 b_p h_q^T/m` | `O(1)` after multiplication by a width-`n` vector |
| an additional, unforced neuron-index equality | loses one free sum | `O(n^-1)` and vanishes |

All limits are taken only after the exact update

\[
M_m={1\over mn}\sum_{p+q=m-1}b_ph_q^T
\]

has been substituted.  Thus the rank-update equality sectors are never
discarded as though the differentiated matrix were fresh.

## 2. Exhaustive branch census

For a forward multiplication at coefficient `k>=1`, every surviving
equality partition is exactly one of:

1. the all-free dense sector, producing one fresh `F_k`;
2. identification with one of the `k` earlier transpose uses, producing
   `b_s alpha_ks` for `0<=s<k`;
3. one of the `sum_m=1^k m=k(k+1)/2` exact rank-update branches in
   `M_m h_(k-m)`.

For a transpose multiplication at coefficient `k<=4`, every surviving
partition is exactly one of:

1. the all-free dense sector, producing one fresh `R_k`;
2. identification with one of the `k+1` earlier forward uses, producing
   `h_s beta_ks` for `0<=s<=k`;
3. one of the `k(k+1)/2` exact rank-update branches in
   `M_m^T b_(k-m)`.

Any partition with one more equality loses a free neuron sum and is
`O(n^-1)`.  Gaussian pairings among the surviving fresh sectors are not
dropped; they are exactly the Wick covariances `H_kl` and `B_kl`.
This classifies every equality sector through order five.

The raw high-level branch counts are therefore

| `k` | forward: fresh | forward responses | forward updates | transpose: fresh | transpose responses | transpose updates |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 | 2 | 1 |
| 2 | 1 | 2 | 3 | 1 | 3 | 3 |
| 3 | 1 | 3 | 6 | 1 | 4 | 6 |
| 4 | 1 | 4 | 10 | 1 | 5 | 10 |
| 5 | 1 | 5 | 15 | -- | -- | -- |

The `k=0` transpose response is present in the exhaustive census but
vanishes algebraically because `beta_00=E[a phi''(Z)]=0`.

## 3. Chronological coordinate census

After zero branches and identical coordinate monomials are merged, the typed
compiler records:

| `k` | `h_k` | `z_k` | `g_k` | output | `b_k` | `r_k` | `u_(k+1)` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | base | 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 2 | 2 | 2 | 3 | 2 | 3 |
| 2 | 3 | 4 | 5 | 0 | 10 | 2 | 6 |
| 3 | 6 | 12 | 15 | 12 | 26 | 5 | 16 |
| 4 | 16 | 29 | 37 | 0 | 67 | 8 | 31 |
| 5 | 31 | 73 | 91 | 67 | -- | -- | -- |

The zero output columns at even order are exact readout-parity cancellations,
not numerical pruning.

## 4. Transpose-response audit

The nonzero response pattern is parity triangular:

\[
\alpha_{ks}\ne0\Longrightarrow k-s\text{ is odd},
\qquad
\beta_{ks}\ne0\Longrightarrow k-s\text{ is odd}.
\]

The observed rows through the terminal order are

\[
\begin{array}{c|l|l}
k&\{s:\alpha_{ks}\ne0\}&\{s:\beta_{ks}\ne0\}\\ \hline
0&\varnothing&\varnothing\\
1&\{0\}&\{0\}\\
2&\{1\}&\{1\}\\
3&\{0,2\}&\{0,2\}\\
4&\{1,3\}&\{1,3\}\\
5&\{0,2,4\}&--
\end{array}
\]

In the compiler's indexing `beta_00` is explicitly evaluated and equals
zero; the displayed nonzero row for `k=1` refers to `beta_10`.
Every response is obtained by symbolic differentiation followed immediately
by the appropriate Gaussian expectation.  The terminal derivative census is
five, so no implicit derivative operator remains.

## 5. Elimination and terminal checks

The first-side Wick recursion reduces the total `R` degree by two.  The
second-side Wick--Stein recursion reduces the number of explicit fresh
`F_i,i>=1` factors by at least one.  Both are terminating exact rewrites.
After the unit-Gram quotient:

- the terminal map contains 3, 46, and 974 monomials for `A,B,C`;
- every atom is one-dimensional and has derivative order at most five;
- `M_200000` is absent because it equals one;
- exact comparison with the independent compiler has zero atomwise
  discrepancies.

See [`compiler/INDEPENDENT_COMPARISON.json`](compiler/INDEPENDENT_COMPARISON.json)
for the literal coefficient comparison.

