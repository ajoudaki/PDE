# Independent fit and representation check

Scope: this study's neutral assignment, `docs/NOTATION.md`, and maintained
`finite_network.py`, `finite_torch.py`, `observable_torch_p1.py`,
`observable_initialization.py`, and `observable_words.py`. No other studies or
history were read. Producer implementation and training results did not inform
the frozen derivations, representation controls, or initial preflight checks;
the later authorized schema adaptation and raw replay are identified below.
The solve-math-rigorously skill was used. This report concerns the stated finite
experiment and is not a promotion review.

## Frozen replay rules and counts

For samples indexed by `a=0,...,m-1`, use
`x_a=(cos(2*pi*a/m),sin(2*pi*a/m))`, `U_a=x_a/sqrt(2)`, and
`y_a=(-1)^a`. The dense forward map is

\[
f=(c/n)^T\tanh\bigl(A\tanh(WU^T)\bigr).
\]

The closure forward map with uniform finite-carrier weights is

\[
f=(c/n)^T\tanh\bigl(B_2M[B_1^T\tanh(WU^T)/n]\bigr).
\]

Both are bias free. A fit requires the unhalved full-data mean squared loss to
be at most `0.001` **and** every product `y_a*f_a` to be strictly positive;
zero predictions count as sign errors. Raw saved arrays are recomputed with
NumPy independently of the producer's forward and optimizer routines. All
arrays must be finite; dataset coordinates, sample order, labels, shapes, and
the stored-readout convention are checked explicitly.

The ordinary dense parameter count is `2n+n*n+n=n*n+3n`: width 55 has 3190;
width 105 has 11340. At dictionary order one the four first-population
coordinates plus the constant give `K1=5`, and the two second-population
coordinates plus the constant give `K2=3`; the exhaustive prefix adds no new
features because codes 0 and 1 are the already included constants. Thus the
1024-carrier closure has `2n+n+K1*K2=3087` trainable scalars. Counting the
minimal prediction arrays `(W,c,M,B1,B2)` gives `11n+15=11279` scalars. This
last figure excludes initial-state diagnostics, implicit uniform probability
vectors, cached contractions, optimizer state, activation workspace, and the
dense matrix used only to construct the finite carrier. It is not a measured
peak-memory count or the `ClosureEngine.retained_bytes` convention.

## Parity and a finite constructive witness

Because tanh is odd and there are no biases, every network in this class obeys
`f(-x)=-f(x)`. Writing `m=2q`, the alternating labels obey
`y_(a+q)=(-1)^q*y_a`. All requested sample counts 30, 62, 126, 254 have odd
`q` and satisfy the necessary antipodal constraint. For comparison, if `q`
were even, each antipodal pair would have the same label and its average
squared loss would be `f(x)^2+1>=1`; that obstruction does not apply here.

Here is an explicit witness for every requested pair with `n>=q`. For
`j=0,...,q-1`, set

\[
\tau_j=\pi(j-1/2)/q,\qquad
R=\frac{8\sqrt2}{\sin(\pi/(2q))},\qquad
W_j=R(-\sin\tau_j,\cos\tau_j).
\]

Set the first `q` diagonal entries of `A` to one and all other entries of `A`
and remaining rows of `W` to zero. On the first half-circle,

\[
W_jU_a=(R/\sqrt2)\sin\bigl(\pi(a-j+1/2)/q\bigr),
\quad 0\le a,j<q.
\]

Its sign is positive exactly when `a>=j`, and its absolute value is at least
8. Let `S_(a,j)=1` for `a>=j` and `-1` otherwise, and let
`t=tanh(1)`. The limiting second-layer design would be `t*S`. This matrix is
invertible: if `z=S*b`, then

\[
b_0=(z_0+z_{q-1})/2,\qquad
b_j=(z_j-z_{j-1})/2\quad(1\le j<q).
\]

These formulas also show `||S^{-1}||_infinity=1` for `q>1` (the case `q=1`
is immediate). The actual finite matrix `H` differs entrywise from `t*S` by
at most `2*exp(-16)`: tanh is 1-Lipschitz and
`1-tanh(s)<=2*exp(-2s)` for `s>=8`. Therefore

\[
\|(tS)^{-1}(H-tS)\|_\infty
\le\frac{2q e^{-16}}{\tanh(1)}<3.76\times10^{-5}<1
\]

for `q<=127`. To see invertibility without invoking an unstated theorem,
if `Hb=0`, then
`b=-(tS)^{-1}(H-tS)b`, so taking the infinity norm forces `b=0`.
A square injective matrix is invertible. Finite coefficients solving the
first-half labels thus exist. Oddness supplies the other half because `q`
is odd. The actual implementation solves the full finite `2q`-sample least
squares problem for `v=c/n`, verifies the rank is `q`, and retains all weights.
No infinite weights, optimization trajectory, or limiting numerical state is
used as evidence.

The CPU float64 witness run produced:

| Samples m | Width n | Active q | MSE | Sign errors | ||W||F | ||A||F | ||c||2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 55 | 15 | 6.7382e-30 | 0 | 419.1950 | 3.8730 | 279.6951 |
| 62 | 55 | 31 | 7.6524e-30 | 0 | 1243.6939 | 5.5678 | 402.0870 |
| 126 | 63 | 63 | 5.7041e-29 | 0 | 3601.9770 | 7.9373 | 656.5795 |
| 254 | 127 | 127 | 1.9896e-28 | 0 | 10308.6492 | 11.2694 | 1879.2393 |

The corresponding first-weight row norms are 108.2357, 223.3740, 453.8064,
and 914.7447. The largest prediction error in this table is below `4.7e-14`.
Full Euclidean/Frobenius, matrix operator, maximum-entry, and optimized-readout
norms, design condition numbers, margins, and raw artifact hashes are in
`data/generated/alternating_circle_fit_capacity_20260921/check_scratch/witnesses_v2/witness_summary.json`.
The neighboring `witness_m*_n*.npz` files contain the actual weights, data,
and predictions. Padding to a larger width preserves predictions by setting
the extra hidden rows/columns and readout entries to zero and rescaling the
stored readout from `c=n*v` to the new width times the same `v`.

Consequently, an unsuccessful training attempt at width 55 for `m=30` or
`m=62` cannot establish a representational capacity failure. The witnesses
at widths 63 and 127 show compatibility of the larger targets with this
architecture at those widths; they make no claim about the sufficiency or
insufficiency of width 55 at `m=126` or `m=254`. These are structured
representation controls, not trained baselines or samples from Gaussian
initialization.

## Forward/gradient preflight

At a fixed random nonsaturated width-7 state, with no parameter updates,
Torch autograd in `(W,A,v)` was compared against maintained
`finite_network.loss_gradients` in `(W,A,c=n*v)`. The chain rule requires
`grad_v=n*grad_c`; the W and A gradients agree directly. Maximum absolute
discrepancies were `4.41e-17` for W, `2.09e-17` for A, and `5.56e-17` for v.
The maintained and Torch predictions each agreed with the independent NumPy
forward to within `5.56e-17`.

A separate width-11 closure check used fixed arbitrary finite `B1` and `B2`
marks of dimensions 5 and 3, without training or reading a producer state.
Independent NumPy and Torch predictions agreed with maintained
`ClosureEngine.predict` within `1.67e-16`; autograd gradients in `(W,M,v)`
agreed with `(-rhs.w/n, -rhs.M, -rhs.c)` within `2.78e-16`. These factors
follow from the maintained physical mobilities `(n,1,n)` in `(W,M,c)` and
`c=n*v`. The complete record is `check_scratch/closure_preflight.json`.

The successful command used `/home/amir/miniconda3/bin/python -B`, with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`, and `fit_check.py witness --output`
pointing at the fresh `witnesses_v2` directory. An earlier `witnesses_v1`
attempt saved controls but did not complete its preflight because system
Python had no Torch; it is not the authoritative result directory.

## Optimization interpretation constraints

- `v=c/n` is an invertible change of coordinates for a fixed width. It preserves
  the representable functions but changes ordinary Adam/LBFGS behavior and is
  not the maintained physical gradient flow with mobilities `(n,1,n)`.
- A first-layer gain of `m/2` changes the initialization protocol. Report its
  outcomes separately from canonical independent Gaussians with stored
  standard deviations `1,1/sqrt(n),1/n` for W, A, c.
- Readout least squares can show a feature state admits a better fit. Record
  its rank cutoff and coefficient norms, and retain the actual polished
  state. Applying the same rule to both models is necessary for comparison.
- A saved fit at an evaluated LBFGS trial is a valid finite representation
  witness, but should be identified as a trial rather than an accepted
  optimizer iterate. Save and independently replay the state actually
  associated with every claimed score.
- Finite seeds, finite optimizer schedules, and wall-clock caps establish
  observed success or failure under that protocol. An ordinary initialization
  training failure does not establish a minimum width or impossibility.

The forward equations, dataset checks, fit criterion, witness construction,
and count convention above were fixed before opening producer output. After
that freeze, the supervisor authorized the producer schema and source at
SHA256 `6d16168b069ccbfef078bbe748fb0e760689187531e671901c8618f797f104a1`.
Only schema, initialization-save, and export sections of that producer were
read to implement the adapter. The NumPy forward equations were unchanged.

`fit_check.py replay-campaign` verifies every completed attempt's declared
output hashes, regenerates the original Gaussian draws from the recorded
seed and gain, and recomputes p=1 finite-carrier raw features, normalized
features, and action matrix. It independently scores initial, final, and
best states, plus retained optimizer-terminal and least-squares candidates.
Saved prediction agreement is checked at absolute tolerance `1e-8`, MSE
agreement at `1e-9`, and sign-error counts and fit flags are checked exactly.
Discrepancies invoke additional NumPy longdouble diagnostics and remain
explicit in the report rather than automatically being labeled a capacity
failure. The replay command has a 300-second CPU budget.

The first five completed attempts were structurally valid and regenerated
their Gaussian source arrays exactly. All three `m=30` canonical attempts
passed the strict float64 replay checks. The first two `m=62` attempts had
very large readout coefficients and failed the `1e-8` prediction agreement
test despite fitting the dataset. The third `m=62` attempt also required
precision adjudication but did not fit.

The independent `adjudicate` subcommand evaluates saved `best.npz` weights
and `dataset.npz` values as exact binary64 numbers using mpmath at both 60
and 90 decimal digits. No parameters are adjusted. The initial three
precision adjudications are:

| m | Seed | High-precision MSE | Sign errors | Maximum absolute error | Fit |
|---:|---:|---:|---:|---:|:---|
| 62 | 20260921 | 8.0690686296e-11 | 0 | 1.6806763555e-5 | yes |
| 62 | 20260922 | 4.8936642107e-10 | 0 | 5.1330218698e-5 | yes |
| 62 | 20260923 | 0.6894106353780012 | 18 | 1.48169669834 | no |

The maximum change of a prediction on increasing precision was below
`7e-51` in each case. This stabilizes the fit/no-fit classifications
numerically; it is not an interval-arithmetic certificate and does not turn
the original strict float64 reproduction failures into passes.
`check_scratch/numerical_adjudications.json` is keyed by absolute attempt
path, binds each result to the original record SHA256, and points to a
`precise_<attempt>.json` evidence file with checkpoint/dataset hashes,
decimal predictions, both precision results, timing, and original double
replay diagnostics. The supervisor may invoke this same independent CLI
sequentially for later oracle-only exceptions without changing training.

The later fourth precision exception, canonical `m=126`, seed 20260921,
was also stably resolved as a nonfit: MSE `0.999999956771279`, 62 sign errors,
maximum residual `1.0004575446912074`, and precision-change discrepancy below
`8.44e-54`. Its original strict double failure remains visible.

## Completed campaign verdict

**PASS for the declared finite experimental comparison.** The independent
final raw replay covers all 33 attempts. Twenty-nine pass the original strict
float64 tests; the four earlier precision exceptions have hash-matched,
stable 60/90-digit adjudications. Every initial, best, and final state in the
selected `m=254` comparison, including its three fresh reproductions, passes
the strict float64 tolerances. Gaussian source regeneration and finite
dictionary reconstruction passed for every attempt. This is an internal
experimental check, not establishment or promotion of a theorem.

Independently reconstructed gates agree with the registered sequence:

| Model | m | Canonical fits | Rescue fits | Rescue required |
|:---|---:|:---:|:---:|:---:|
| Dense n=55 | 30 | 3/3 | — | no |
| Dense n=55 | 62 | 2/3 | — | no |
| Dense n=55 | 126 | 0/3 | 1/3 | yes |
| Dense n=55 | 254 | 0/3 | 0/3 | yes |
| Closure n=1024,p=1 | 254 | 0/3 | 3/3 | yes |
| Dense n=105 | 254 | 0/3 | 0/3 | yes |

Thus 254 is the smallest registered `m>55` with no fitted width-55 attempt.
At that case the lowest checked MSEs are `0.34743363100232755` (dense 55,
42 sign errors), `0.0009786301365027257` (closure, zero errors), and
`0.05831074517447311` (dense 105, eight errors). All three closure rescues
fit; their MSEs are `0.0009983885125683862`, `0.0009786301365027257`, and
`0.0009931809340789676`. The canonical initialization produced no fits at
this selected case. The result therefore supports closure fitting under the
declared high-gain protocol and tested budget; it does not show a Gaussian
initialization advantage or a dense-network representation lower bound.

`fit_campaign_audit.py` separately verifies the literal seed sets, rescue
gates, conditional sample choice, source/config/output provenance, exact
optimizer defaults, float64 state storage, parameter counts, timing caps,
and same-settings reproduction selection. Each reproduced source is the
lowest-MSE attempt for its model at the selected case. All three repeated
fit statuses agree, and all three independently replayed MSE differences
are exactly zero (required tolerance `1e-6`). No extra training was run by
the checker.

The 33 worker processes sum to `821.84265351668` seconds, below 2500; the
largest recorded per-attempt initialization/training/export interval is
`36.9417361728847` seconds, below 60. Recorded training intervals have maximum
concurrency two and no overlap on one GPU. Final raw replay took 0.8954
seconds internally (0.9241 seconds command wall); the protocol audit takes
about 0.11 seconds internally. Automatic precision replay used 1.1659 seconds.
Allowing a conservative 20 seconds for all earlier checker commands and
less than two seconds for the final replay/audit runs keeps the separate
checker total below 24 seconds, well below its 300-second ceiling.

Final machine-readable evidence is
`check_scratch/producer_replay.json` and `check_scratch/campaign_audit.json`;
the latter reports `passed=true`, no failures, and
`main_comparison_all_strict_float64=true`. The scientific producer remained
at SHA256 `6d16168b069ccbfef078bbe748fb0e760689187531e671901c8618f797f104a1`;
the replay/adjudication source stayed frozen at
`2bae15f0a8ca03ff8acab8c427b706f15de212dc41cba8f989abadb4dab9c6da` during
execution. The separate campaign auditor accepts the exact preserved
`PROTOCOL.md` bytes for the originally recorded README digest, records both
paths, and permits no substitution for other source or config hashes.
