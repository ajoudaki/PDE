# Internal model and resource-scope check

Checked 2026-09-15. This is an internal source audit, not an independent
promotion review. Complete inputs: P1_INITIALIZATION.py,
INITIALIZATION_THEORY.md, P1_ENGINE.py, NETWORK_ENGINE.py, PLAN.md, and the
established notation/initialization equations. No implementation was changed
and no training or new numerical validation was performed.

**Conclusion:** the implemented general-d first-order closure and finite-network
comparison use the stated canonical scaling. The moving-state claim
`O(Pd+d²)` is correct, including when nominal `P=n`, but is not a complete
byte count, a matched independent-sample count, or a computational-accuracy
guarantee. The qualifications below should accompany its use.

## Model and initialization

- Both engines receive `U=x/sqrt(d)` and form the first preactivation as
  `w @ U.T`. Thus the plan's unit-length image rows represent canonical
  physical inputs `x=sqrt(d) U`; no additional `1/sqrt(d)` is missing.
  The network uses `f=c @ h2/n`, Gaussian variances `(1,1/n,1/n²)`, residual
  `f-y`, full mean squared loss, and block mobilities `(n,1,n)`.
  In particular its middle velocity has `-2/n`, while first/readout velocities
  have `-2` (NETWORK_ENGINE.py:16, 23, 35). The closure correctly replaces
  finite-neuron averages by its declared probability pairings; its coefficient
  M has Euclidean gradient `-2 integral r d a^T`, without an extra `1/P`
  (P1_ENGINE.py:136, 154). Both engines integrate GF with Heun; those steps are
  not literal raw-GD updates.
- The closure sets `w=g, c=0, M=D` (P1_ENGINE.py:103), so its initial output
  is exactly zero. The actual network retains its independent random
  `c_i~N(0,1/n²)` (NETWORK_ENGINE.py:17), and its initial prediction is
  generally nonzero. Conditional on its hidden activations,
  `Var(f0)=sum_i h2_i²/n⁴ <= n^-3`. Zero closure readout matches the limiting
  small-readout convention, not the finite network's exact initial state.
  Giving both methods the same seed number does not couple their randomness.
- The full first-order dictionary has dimensions `(2d+1,d+1)` and retains
  the reverse response in `R=sqrt(tau) Z+alpha tanh(G)` and in the raw
  contraction `alpha beta+tau gamma`. Ridge `1/4096` and the right transpose
  in Cholesky normalization are correct. The repeated initial coefficient
  blocks do not constrain the evolving full matrix M. The coefficient target
  is an exact population identity; working values use finite quadrature on a
  truncated Gaussian interval, explicitly disclosed in the theory/metadata.
  They are not exact coefficients or the maintained finite-Q empirical Gram.
- With antithetic folding, nominal P must be even and **N=P/2 independent
  base samples per population** are stored; each represents itself and its
  negative. Dimensions are `b1: N×2d`, `g,w: N×d`, `b2: N×d`, `c: N`, and
  `D,M: d×2d`, with stored probabilities `1/N=2/P`.
  Odd marks and odd w,c are preserved by the field for arbitrary data; the
  constant feature pairings vanish and its M row/column stay zero. All
  operational contractions, squared motions, and initial/current activation
  Grams have even integrands. Folding therefore preserves that paired rule
  exactly in real arithmetic. It does not preserve an iid-P rule, and the
  finite network itself is not sign paired. `P=n` is a nominal resolution
  convention, not an equality of independent draws, state sizes, or errors.

## State counts and full costs

Counts below are real scalar entries for equal population sizes. Multiply by
the scalar byte size for array payloads. They exclude data, checkpoints,
integration stages, temporary contraction/observation arrays, and allocator
overhead. For folded sampling, N=P/2.

| Representation | Moving w,c,M | Frozen b1,g,b2,D,p1,p2 | Cached weighted/transposed bases |
| --- | ---: | ---: | ---: |
| Unfolded, P nodes | `P(d+1)+(d+1)(2d+1)` | `P(4d+4)+(d+1)(2d+1)` | `P(3d+2)` |
| Folded, N nodes | `N(d+1)+2d²` | `N(4d+2)+2d²` | `3Nd` |
| Actual network, width n | `nd+n²+n` | `nd+n²+n` retained initial state | none in this engine |

The closure engine's retained array total is therefore
`P(8d+7)+2(d+1)(2d+1)` unfolded and `8Nd+3N+4d²` folded, matching the
arrays listed by P1_ENGINE.py:279. These too are `O(Pd+d²)`, but with a
larger constant than moving state alone. For degenerate dimensions a contiguous
transpose may alias its source; `retained_bytes` sums tensor entries rather
than deduplicating storage. The stated d=784 production case has separate
nondegenerate caches. NETWORK_ENGINE.py:55 reports moving state only, so
include `engine.initial` when comparing retained payloads, as PLAN.md requires.

For `d=784, P=n=2048`, folded closure moving state has 2,033,152 scalars
(7.756 MiB in float32); its engine plus current state has 8,884,224 scalars
(33.891 MiB). The actual network moving state has 5,801,984 scalars
(22.133 MiB); current plus retained initial state has 11,603,968 scalars
(44.266 MiB). A separate best checkpoint adds one moving-state payload for
each model. These are analytical array counts, not measured peak GPU memory.

Input data add `O(md)` storage. Heun keeps a bounded number of moving-state
copies. Blocked direct RHS arithmetic is `O(m(Pd+d²))`; the engine can also
choose `O(Pd²)` precontractions to reduce subsequent per-input products.
One must include their formation cost. A panel of k inputs can add
`O(Pk+k²)` observation storage. Physical-horizon work additionally depends on
the selected step count. Consequently smaller moving state does not prove
lower runtime or peak memory; `P=n` gives `O(nd+d²)` versus network
`O(nd+n²)`, with no uniform advantage when d and n vary jointly.

## Two reporting qualifications

1. `observations(..., include_pairs=True)` on a folded engine returns only
   the positive-half pair arrays (P1_ENGINE.py:271). Their Grams and squared
   motions are valid full paired-rule quantities, but those raw arrays alone
   are not the full signed empirical joint law. For a joint-law claim, restore
   negative pairs and weights `1/P`, or explicitly describe the output as a
   folded representation. This does not affect the plan's Gram/RMS comparisons.
2. `save_restart` saves all operational arrays and restarts its dynamics, but
   nominal P and the antithetic interpretation enter only through caller
   metadata (P1_ENGINE.py:284). Preserve initializer metadata in reporting;
   counting stored rows as nominal P would be incorrect. The assigned files
   do not by themselves verify the production runner's metadata or memory logs.

Fixed p=1, a larger P, or the rule P=n does not establish convergence to the
actual general-d trained network. Remaining truncation, finite-width,
population-rule, time-step and arithmetic errors are distinct. The plan's
latest user clarification makes sample-by-sample network prediction agreement
primary and explicitly supersedes the older accuracy-first metric wording.

## Checked source hashes

```text
P1_INITIALIZATION.py 21dc8905f8ab17631762fcd38cd66258bf436e46f24cd870b3968d12622b08ed
INITIALIZATION_THEORY.md 46e0285c1b78ebb5c276b540c8777d551ac3edd137816c0396e39d4e03309b0a
P1_ENGINE.py f6e5ef785a329549d389dad466b23f7a2fda26566b499382627557b8120448e1
NETWORK_ENGINE.py 0c2fedf6ef6350b3715c6b0df0de91b90cba2c94a9895b970cb25ab067dc55bc
PLAN.md a7c185d55aa9757534dda07556761e42bd38dfd749bc94a108309d39d2c9b276
```
