# Exact quadratic-network mean-field peeling compiler

The root of this directory contains a computer-algebra implementation of the
leading-width peeling calculation for the canonical one-sample,
two-hidden-layer quadratic network at `gamma=1`.  It is an exact compiler for
this model, not yet a generic MLP compiler.  The bounded campaign
subdirectories extend the same grammar to relative and independently weighted
block metrics, two and three symmetry-reduced inputs, and a shifted
first-hidden activation.  A separate threshold campaign audits a bounded D13
probe without producing an accepted new coefficient or bound.  The canonical
root compiler computes

\[
F^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n],
\qquad
D_n=n\nabla f_n\mathbin\cdot\nabla,
\]

directly in exact integer arithmetic.

`HISTORICAL_SOURCE_HASHES.txt` intentionally retains the pre-consolidation filenames that
were frozen with the certified runs.  The one preserved binary,
`export_evaluator_checked512`, is part of the accepted order-eleven provenance;
other exploratory build products have been removed from the live study.

The general MFP theorem program is maintained in
[`../CURRENT_RESEARCH_STATE.md`](../CURRENT_RESEARCH_STATE.md).  Stieltjes
moments and Hankel certificates derived from these raw feature derivatives
are conceptually owned by the separate
[`../../stieltjes_conjecture/`](../../stieltjes_conjecture/) study.  Compact
campaign-local certificates are colocated here with the exact jets whose
integrity they audit.

## Exact parameter-extension campaigns

Five bounded parameter extensions of this compiler are maintained as
separate, auditable campaigns.  They reuse the peeling/Wick grammar but do not
alter the accepted canonical derivatives above.  Campaigns 1--4 reached exact
finite Hankel endpoints; Campaign 5 reached exact lower jets and partial
moment signs only.

- [`campaign1/`](campaign1/) varies the relative feature-ascent metric
  ($D_\lambda=D_a+\lambda(D_u+D_W)$) and jointly computes the output and
  hidden squared-RMS responses.  Exact ordinary and shifted $2\times2$
  Hankel tests pass for both responses over the full ray $\lambda\ge0$.
- [`campaign2/`](campaign2/) treats two equal-norm inputs in the same-label
  and opposite-label symmetry channels.  It retains the input Gram matrix in
  both the initialization covariance and first-layer gradient metric.  Exact
  order-seven ordinary $2\times2$ Hankel tests pass throughout the full
  correlation interval; the degenerate opposite-label endpoint is handled by
  its exact normalization.
- [`campaign3/`](campaign3/) replaces the first activation by
  $u^2-c$, $0\le c\le2$.  In the centered coordinate
  $u^2-c=(u^2-1)+(1-c)$, exact Sturm certificates prove the available
  moment and ordinary $2\times2$ Hankel inequalities on both halves of the
  parameter interval.
- [`campaign4/`](campaign4/) separates the first-hidden and middle-weight
  block metrics:
  $D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W$ on the full quadrant.  All 125
  atomic sectors through order nine completed, and exact positive-coefficient
  certificates prove $\mu_0,\ldots,\mu_3$ plus ordinary and shifted
  $2\times2$ Hankel positivity, strictly away from the constant-kernel origin.
- [`campaign5_b3/`](campaign5_b3/) treats three equicorrelated equal-label
  inputs on $-1/2\leq\rho\leq1$, retaining the Gram matrix in both the
  initialization covariance and first-layer gradient metric.  It gives an
  exact faithful scalar loss channel, exact jets through order five, a genuine
  signed triangle invariant, and exact $\mu_0,\mu_1>0$ on the full interval.
  Its frozen order-seven W0 pilot exceeded 1800 seconds, so it has no
  $F^{(7)}$, $\mu_2$, or Hankel determinant and is not counted as a Hankel
  pass.

[`campaign6_f13_threshold/`](campaign6_f13_threshold/) is not a parameter
extension or successful certificate.  It records a bounded canonical D13
threshold probe whose candidate bounds were nonseparating and whose mandatory
fresh-regression/provenance gate was incomplete.  It is protocol-inconclusive
and contributes no accepted new D13 interval or bound.

These are continuum-valued, finite-order compatibility results.  They neither
prove all-order Stieltjes positivity nor identify the formal jets with an
independently established global mean-field trajectory.  The consolidated
mathematical account is
[`../../stieltjes_conjecture/EXACT_PARAMETRIC_CAMPAIGNS.md`](../../stieltjes_conjecture/EXACT_PARAMETRIC_CAMPAIGNS.md).
The frozen latest-portfolio decisions, including why no B=4 or metric-ray
order-eleven conditional branch was launched, are in
[`../../stieltjes_conjecture/NEXT_CAMPAIGN_OUTCOMES.md`](../../stieltjes_conjecture/NEXT_CAMPAIGN_OUTCOMES.md).

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
D^11 f = 291982832387585872335470592
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

Their sum is the stated `D^9 f`.  The independently audited twelve-sector
decomposition of `D^11 f` is recorded in
[`D11_LOWER_SECTOR_AUDIT.md`](D11_LOWER_SECTOR_AUDIT.md) and
[`d11_high_sectors_exact.txt`](d11_high_sectors_exact.txt). Dividing `D^9 f`
by `9!`, reverting `F`, and
substituting into `K=F' o F^(-1)` reproduces the already-audited coefficient

\[
[y^8]K(y)=
-\frac{21749547365571716077696}{13618704359108797313085}.
\]

This is a strict regression gate: order 11 or 13 output is not accepted unless
all five values above are reproduced exactly.
