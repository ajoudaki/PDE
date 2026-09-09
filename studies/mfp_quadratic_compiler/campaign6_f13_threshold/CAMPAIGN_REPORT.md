# Campaign 6: bounded $F^{(13)}(0)$ threshold probe

## Outcome

The bounded probe is **inconclusive about the Stieltjes conjecture** and is
closed without a D13 production run.  A hostile post-run audit found that the
campaign failed its frozen mandatory validity gate: it did not independently
reproduce every D9 Wick-pair sector and the accepted D11 total, and it did not
preserve the required per-run provenance records.  Consequently, the new
Campaign 6 endpoints below are analytically justified candidates and
calibration diagnostics, **not protocol-accepted certificates**.

Let

$$
D_{13}=F^{(13)}(0).
$$

The next shifted Hankel determinant is positive exactly when

$$
D_{13}\le T,
$$

where the exact rational threshold is

$$
T=
\frac{
982497059836127136743897882036793220177491977764234839125040220839477248
}{
7556538848269898446547697632297780206383
}
=1.300194546159283\ldots\times10^{32}.
$$

The best previously certified retained positive subsum remains

$$
D_{13}\ge
50\,393\,647\,763\,255\,899\,049\,472\,742\,772\,736
=0.38758544\ldots\,T.
$$

The new candidate unrestricted-pairing upper endpoint is much too loose:

$$
D_{13}\le
66\,302\,565\,413\,754\,388\,824\,762\,451\,619\,994\,815\,
152\,236\,811\,894\,359\,106\,560\,000\,000,
$$

which is approximately

$$
5.10\times10^{29}\,T.
$$

If admitted independently of the failed campaign gate, the candidate upper
inequality and the accepted pre-existing lower bound would give an interval
containing $T$ by an enormous margin.  Campaign 6 itself accepts no new
interval certificate.  Failure to separate the threshold is a failure of the
tested bounding mechanisms, not evidence for or against the conjecture.

## Protocol and resource discipline

The protocol was frozen before any Campaign 6 computation.  Its SHA-256 is

```text
1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43
```

The compact benchmark summary reports checked 512-bit arithmetic, a 4 GiB
address-space cap, a 15-minute limit, a largest process of about 2.04 GiB and
219 seconds, and less than two aggregate CPU-hours.  However, the required raw
records containing commands, source and executable hashes, CPU times, exit
statuses, and output hashes were not retained.  These resource figures are
therefore descriptive summaries, not a completed provenance certificate.

No D13 production job, old multi-day base enumeration, old eight-hour
root-class branch, or transient `/tmp` checkpoint was launched or resumed.

## Exact reference rows and the failed regression gate

The calculation loaded the previously accepted exact Wick-pair-sector rows at
orders 9 and 11 as static calibration references.  In particular,

$$
\sum_{P=1}^{10} C_{9,P}
=1\,181\,161\,141\,825\,400\,561\,664,
$$

and

$$
\sum_{P=1}^{12} C_{11,P}
=291\,982\,832\,387\,585\,872\,335\,470\,592.
$$

The stored order-11 high sectors are:

$$
\begin{aligned}
C_{11,10}&=83\,655\,641\,930\,747\,138\,444\,722\,176,\\
C_{11,11}&=49\,117\,046\,434\,067\,436\,406\,308\,864,\\
C_{11,12}&=12\,285\,503\,181\,066\,227\,920\,404\,480.
\end{aligned}
$$

The parent exact compiler was additionally run at order 9 and reproduced the
accepted **total**.  It did not reproduce the ten D9 sectors separately, and a
fresh implementation-level D11 total was not produced.  Merely summing static
accepted tables and checking that candidate caps cover them does not satisfy
the protocol's requirement that the new implementation reproduce every D9
sector and the D11 total before interpreting a new bound.  This is the main
reason for the protocol-level downgrade; no retroactive high-cost computation
was launched to repair it.

## Bound 1: total-coefficient and unrestricted-Wick envelope

After $r$ feature-ascent derivatives, let

- $x$ be the number of readout hits;
- $z$ be the number of weight hits.

Every derivative history with the same $(r,x,z)$ has the same total degrees

$$
A=r+1-2x,
\qquad
H=r+2+x+z,
\qquad
E=2(r+1-z),
$$

where $A$ is the total readout-Gaussian degree, $2H$ is the total first-feature
Gaussian degree, and $E$ is the number of remaining weight factors.  The
number of remaining weight Wick pairs is

$$
P=\frac E2=r+1-z.
$$

This $P$ labels the accepted **Wick-pair sector**; it is not the number of
connected components.  Starting from one root component, each weight hit
splits one tree, so the terminal component count is

$$
c=1+z,
\qquad P+c=r+2.
$$

At the next derivative, summing over every eligible factor gives total rewrite
coefficients

$$
A,
\qquad
8H,
\qquad
2E
$$

for readout, feature, and weight hits respectively.  Hence a two-count dynamic
program exactly sums the positive scalar rewrite coefficients of all labelled
histories without enumerating forest shapes.

For a terminal scalarized history, forget all graph restrictions and allow
every Wick pairing independently within each Gaussian species.  Merging
Gaussian index classes can only increase the product of centered even moments.
Consequently the terminal contribution is bounded by

$$
(A-1)!!\,(2H-1)!!\,(E-1)!!.
$$

Equivalently, expand each Gaussian expectation into pairings.  Under a fixed
pairing, the normalized index sum contributes either zero, a nonleading power
of width, or one at leading order; it never contributes more than one.  The
product of double factorials counts every unrestricted pairing, including all
pairings forbidden by the leading-width forest condition.  Multiplying this
cap by the exact coefficient mass and summing gives the candidate envelope,
indexed by Wick-pair sector $P$.

The envelope covers every stored accepted D9 and D11 Wick-pair sector.  This
is a useful calibration but not the missing independent reproduction gate.
It is already too loose by factors

$$
1.52\times10^{18}
\quad\text{at order 9},
\qquad
6.66\times10^{23}
\quad\text{at order 11}.
$$

Its D13 result is the candidate endpoint displayed in the outcome.  The
worsening calibration rules out this envelope as a threshold tool even before
the protocol downgrade is considered.

## Bound 2: exact small components and bounded large components

The second probe preserves forest shape.  For a chosen cap $C$:

- every terminal component with at most $C$ raw weight edges is contracted by
  the exact leading-width Wick recursion;
- every larger component is replaced by the same unrestricted-pairing upper
  cap used above.

Because terminal forest expectations factor over components, this construction
has a valid componentwise upper-bound argument.  Increasing $C$ monotonically
replaces caps by exact nonnegative component values, so the candidate bounds
decrease toward the exact answer.  The reported numerical endpoints are still
not Campaign 6 certificates because the mandatory campaign gate failed.

For the lower calibration, every component through $C$ edges is again exact,
but a larger component retains only the first positive Wick child at every
recursive pairing node.  This positive-branch construction motivates a lower
subsum diagnostic because omitted Wick branches are nonnegative.  It is
distinct from the older accepted pure component-cap certificate, which
discards every terminal history containing an oversized component.  The
unaccepted Campaign 6 calibration summary was:

| order | cap | lower / exact | upper / exact | time lower | time upper |
|---:|---:|---:|---:|---:|---:|
| 9 | 10 | $0.4278465$ | $4.65790\times10^{16}$ | 3.80 s | 2.23 s |
| 9 | 14 | $0.7036445$ | $4.65790\times10^{16}$ | 22.32 s | 20.42 s |
| 11 | 10 | $0.3169906$ | $8.92108\times10^{21}$ | 88.01 s | 28.99 s |
| 11 | 14 | $0.5877173$ | $8.92108\times10^{21}$ | 207.31 s | 151.39 s |

Two conclusions are decisive.

First, exact treatment through 14 edges barely changes the upper bound: the
omitted large components dominate the unrestricted-pairing slack.  At order
11 the upper endpoint still exceeds the exact value by more than 21 orders of
magnitude.  A useful D13 upper certificate would instead need approximately
few-percent precision near $T$.

Second, the first-Wick positive subsum recovers a *smaller* fraction when
moving from order 9 to order 11 at the same exact-Wick cap.  Separately, the
prior pure component-cap D13 certificate is only $38.76\%$ of the threshold.
Neither retained-family mechanism has a calibrated route to the missing
$61.24\%$ under the allowed resource scale.

## Why no D13 benchmark or production extension was authorized

The extension gate required a protocol-valid benchmark that credibly projected
threshold separation within at most eight additional CPU-hours.  The mandatory
validity gate was already incomplete, and the calibration also fails the
cost-benefit condition on both sides:

1. The upper method has $10^{21}$ relative slack already at order 11 after
   exact evaluation through 14 edges.  No continuation within eight hours can
   turn that into a few-percent D13 bound; the missing large-component Wick
   restriction must first be replaced by a new theorem.
2. The lower method is below $59\%$ of the exact answer at D11 for cap 14 and
   below $39\%$ of the D13 decision threshold in the existing certificate.
   The earlier full P14 inventory contains 325,190 canonical base contractions
   and has an optimistic runtime exceeding ten days, explicitly outside this
   campaign.
3. The tempting sharp target

   $$
   D_{13}\le9S_{11},
   \qquad
   S_{11}=13\,748\,366\,485\,300\,446\,891\,099\,172\,896\,768,
   $$

   would give

   $$
   9S_{11}=0.95166757\ldots,T.
   $$

   It is **not a certificate**.  Prefixwise/local charging versions are
   already falsified, including positive descendants of zero-valued parents.
   Campaign 6 neither assumes nor repairs that gap.

The correct action under the frozen stopping rule was therefore to stop before
D13 production.

## The missing algorithmic lemma

Further bounded work is justified only after proving a graph-sensitive
omitted-mass inequality.  It must do one of the following:

1. **Upper route.**  For every large terminal decorated tree, bound the number
   and Gaussian weight of *leading-width* Wick partitions using structural
   invariants retained by the compiler.  The unrestricted product
   $(A-1)!!(2H-1)!!(E-1)!!$ is useless because it ignores the acyclic
   row/column quotient condition.  The new bound must be compositional over
   components and calibrated to within a small constant factor at D9 and D11.

2. **Lower route.**  Partition all positive histories into disjoint structural
   families whose exact aggregate weights are computable without enumerating
   individual P14 bases, and prove that selected families cross $T$.  A
   branch-and-bound implementation is only useful after such family-level
   aggregation; ordering the same 325,190 bases does not change the cost.

3. **Two-generation route.**  Replace the false local parent-to-descendant
   charging rule by a nonlocal aggregate transport identity that permits mass
   to move between prefixes, and prove the special order-11 inequality needed
   for $D_{13}\le9S_{11}$.  Low-order numerical agreement is insufficient.

Without one of these lemmas, additional CPU time only evaluates a larger
fraction of an interval whose uncertified remainder remains too broad.

## Reproduction

Run the compact artifact audit:

```bash
python3 -m unittest -v test_campaign6.py
```

Regenerate the candidate coarse envelope:

```bash
python3 coarse_sector_bounds.py
```

Compile the lower and hybrid interval evaluators:

```bash
g++ -O3 -std=c++20 -march=native -DCHECKED_ARITHMETIC \
  ../peeling_lower_bound.cpp -o peeling_lower_bound_checked

g++ -O3 -std=c++20 -march=native -DCHECKED_ARITHMETIC \
  hybrid_component_interval.cpp -o hybrid_component_interval_checked
```

The binaries are intentionally ignored.  Compact source, candidate JSON
output, the frozen protocol, tests, and dependency hashes are durable.  The
missing raw benchmark provenance is not reconstructed by these commands.

## Artifact map

- `PROTOCOL.md`: preregistered decision and resource protocol.
- `FROZEN_PROTOCOL_SHA256.txt`: frozen dependency hashes.
- `coarse_sector_bounds.py`: exact coefficient-mass DP and candidate
  Wick-pair-sector envelope.
- `coarse_sector_bounds.json`: candidate endpoints, static calibrations, and
  the explicit protocol-acceptance downgrade.
- `hybrid_component_interval.cpp`: exact-small/capped-large component evaluator.
- `benchmark_results.json`: bounded D9/D11 calibration summary; it is not the
  per-run provenance record required by the frozen protocol.
- `test_campaign6.py`: exact regression and claim-level tests.
