# Two-hit charging bound: audited status

This note records a proposed analytic upper bound for `D^13 f` and, in
particular, separates its proved bookkeeping from its unproved contraction
claim.  **No D13 upper bound is certified by this note.**

## Exact two-hit bookkeeping

Fix odd derivative order `k` and a Wick-pair sector `P`.  In a derivative
history let `x,y,z` be the numbers of `a`, `h`, and `W` hits.  Then

```text
x+y+z = k,       z = k+1-P,       x+y = P-1,
A = k+1-2x,      H = 2k+3+x-P,    E = 2P.
```

Here `A` is total `a` exponent, `H` is total half-`u` exponent, and `E` is
the number of raw `W` factors.  The sum of coefficients of all possible next
unit rewrites is

```text
L = A + 8H + 2E = 17k+25+6x-4P.
```

An `a`, `h`, or `W` hit changes `L` by 19, 13, or 17.  Consequently the exact
sum of coefficients of all ordered two-hit extensions of this history is

```text
C(A,H,E) = A(L+19) + 8H(L+13) + 2E(L+17)
         = L^2 + 19A + 104H + 34E.
```

At fixed `(k,P)`, `C` is increasing in `x`, since replacing `x` by `x+1`
changes it by `12L+102`.  Thus its sector maximum is attained at

```text
x_max = min((k+1)/2, P-1).
```

Let `F[k,P]` be the exact leading expectation in sector `P`, and put

```text
S_k = sum_P C_max(k,P) F[k,P].
```

For the exact D11 sector vector,

```text
S_11 = 13748366485300446891099172896768.
9 S_11 = 123735298367704022019892556070912.
```

The desired threshold is

```text
130019454615928300000000000000000,
```

so a proof of `D^13 f <= 9 S_11` would suffice, with 4.833 percent headroom.

## Exact aggregate regressions

The ratios `D^(k+2) f / S_k` from all available exact transitions are

```text
k=1: 7.258217903659293
k=3: 7.055230756049670
k=5: 7.144276787102653
k=7: 7.260778220448249
k=9: 7.374154728458297
```

Thus the proposed factor nine passes every available aggregate test.  These
tests are evidence, not a proof at order eleven.

## The local charging lemma is false

Expand rewrite coefficients into unit hit choices and Gaussian moments into
labeled Wick/scalar pairings.  A tempting local lemma would bound the total
leading contractions of all two-hit descendants of each fixed prefix forest
by nine times `C` times the leading contractions of that prefix.  Exact
enumeration falsifies this statement.

At order one the worst prefix is the connected tree

```text
a = [1,1], h = [1,1,1],
edges = [(0,0),(0,1),(1,0),(1,2)].
```

It has prefix Wick value 3, `L=34`, exact two-hit count `C=1642`, and
two-hit descendant contraction sum 64428.  The ratio is

```text
64428 / (3*1642) = 13.07917174177832 > 9.
```

At order three the worst nonzero prefix found has prefix Wick value 9,
`L=60`, `C=4468`, and descendant sum 983316, giving ratio
`24.453297523127425`.  Moreover, three order-three prefix forests have zero
leading Wick value but positive two-hit descendant sums.  Deleting the two
new rewrite gadgets can therefore destroy parity or the leading free-index
count; it cannot define a prefix-preserving charge.

The enumerator used for this falsification is
`/tmp/two_hit_parent_test.cpp`, SHA256
`219c0da1253e3e33aadb72c71f225dbde3f9914a40a65217539c31d84fabf55b`.
It includes the independent exhaustive implementation
`/tmp/leading_wick_top2.cpp` and performs exact integer contractions.

## Current claim level

The only remaining candidate is a genuinely aggregate, cross-prefix
injection: terminal two-hit contraction objects would have to be reassigned
among leading contractions of different order-`k` histories, with maximum
load nine after the sectorwise padding by `C_max`.  No invariant-preserving
map, Gaussian integration-by-parts inequality, or tree-switching argument
establishing that reassignment is known.  Ordinary Gaussian moment or
hypercontractive inequalities do not supply the required constant, and the
explicit local counterexamples rule out the simplest deletion proof.

Therefore `D^13 f <= 9 S_11`, and hence the desired D13 upper bound, remains
**unsupported**.  It must not be used as a certificate without a new
cross-prefix switching theorem or an independent exact/interval computation.
