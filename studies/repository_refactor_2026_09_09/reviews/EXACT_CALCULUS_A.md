# Isolated adversarial proof and code audit

Audit date: 2026-09-09.

Input root: `/tmp/pde-exact-calculus-isolated.c6rGfOO8`.

Output directory: `/tmp/pde-exact-calculus-audit.H7SCP2MP`, created by a genuine `mktemp -d /tmp/pde-exact-calculus-audit.XXXXXXXX` invocation. This report is the only file created for the audit, using `apply_patch`. No input was edited.

## Verdict and required corrections

**PASS within the explicitly stated scope. No required corrections identified.**

The finite-forest expectation factorization, canonical colored forest keys, rational reversion and determinant algorithms, and frozen-first-mobility quadratic initialization-jet certificate withstand this audit. Independent computations reproduce the full coefficient chain and both negative certificates. No free-label counting error, decoration collision error, missing normalization, incorrect rational fraction, algorithmic defect, or ownership/type defect was found in the new exact-calculus implementation.

The probability conclusion is the limit of the expectation of each fixed-order finite initialization derivative. The formal series constructed from these limits is not identified with a positive-time limiting trajectory. The negative shifted moment witness excludes a nonnegative measure with the six specified moments, and consequently any proposed representation requiring those moments for this frozen-block system. It does not refute a unit-mobility or strictly positive first-mobility assertion. These restrictions are present in the supplied proof and are respected here.

This is a source audit with mathematical arguments and bounded deterministic verification, not a machine-checked formal proof or exhaustive verification of every floating-point execution of the finite-network dependency.

## Exact read scope and integrity

All seven supplied files were read completely, totaling 1,259 lines. Where a combined tool response truncated material, the missing material was reread. The inspected source scope was exactly:

| File relative to input root | Lines | SHA-256 before and after verification |
| --- | ---: | --- |
| `PROOF.md` | 345 | `a02761d75c0eeb0e233cdd9cba460003ce3892238762abb0b3c79f221b12b0cf` |
| `NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `pde/exact_calculus.py` | 191 | `482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41` |
| `tests/test_exact_calculus.py` | 122 | `b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439` |

Final enumeration with hidden and ignored files included returned exactly these seven files. All final hashes matched their initial values.

No repository, studies, history, previous reviews, skill files, agent instructions, internet sources, external datasets, or external source files were inspected. No Git, installation, build, scientific experiment, simulation, sampling, or historical generator was used. Python checks ran with `PYTHONDONTWRITEBYTECODE=1`, `python -B`, and `PYTHONPATH=/tmp/pde-exact-calculus-isolated.c6rGfOO8`, from the private input root. Additional checks were supplied on standard input; no test-script files were created. Python's ordinary runtime and installed NumPy were loaded as needed for package imports and finite arithmetic; their external implementation files were not inspected.

The import dependency is relevant: importing `pde.exact_calculus` first executes `pde/__init__.py`, which imports `finite_network` and `gaussian_moments`. The exact-calculus module itself uses only `Fraction` and `factorial`; its certificate does not call the finite training solver or the general Gaussian moment routine. Both local dependencies were nevertheless read and checked.

## Mathematical audit

### Gaussian moments and covariance validation

Section 4's integration-by-parts derivation is valid for singular covariance: a finite PSD square root permits reduction to independent standard Gaussians, and polynomial integrands make boundary terms vanish. In (9), choosing an index with positive exponent, removing its first occurrence, and summing over the remaining occurrences produces exactly the coefficient `alpha_j - 1_(j=i)`. The zero coefficient is omitted before any second decrement. Every recursive term lowers total degree by two.

The implementation at `gaussian_moments.py:93–109` uses precisely that recurrence. Symmetry and exact PSD validation occur before the zero/odd-degree shortcuts. The zero-pivot branch is sound because symmetry has already been checked: a zero diagonal in a PSD matrix forces the corresponding row and column to vanish. At a positive pivot, completing the square yields the implemented Schur complement. No inverse at a zero pivot or floating tolerance is used.

Rational inputs are copied into immutable rows, exponent values are converted to integers, and the local moment cache is cleared even on failure. The dependency deliberately accepts integral types more broadly than the stricter new exact-calculus API; this does not introduce floating arithmetic into the recurrence.

### Forest expectations: label counts and collisions

For a pairing of the `2p` edge occurrences, endpoint identifications respect the two populations. Collapsing each paired occurrence to one edge leaves a multigraph with exactly `p` edges; parallel edges must remain counted, as they do in the proof. Isolated vertices remain vertices and components. Connectivity of each original component is preserved under this quotient, giving `c <= r`, and the componentwise connected-graph bound gives `v <= p+c`.

For a fixed quotient, label assignments injective within each population number `(n)_(v1)(n)_(v2)`. Equality of numerical labels across different populations is unrestricted and does not identify random variables; there is no erroneous global injectivity requirement. Powers from vertices identified by the edge pairing add before taking their decoration moment.

An additional same-population label equality can create nonzero moments from decorations that individually had odd powers. It can also change already nonzero moments. The proof does not discard these cases as independent: they have at most `O(n^(v-1))` labelings, and every resulting moment is bounded by a constant depending on the fixed total decorations. After normalization their order is at most `n^(v-p-r-1)`, hence at most `n^-1`. This is the essential collision check.

The only possible leading pairings have `v=p+r`, hence `c=r`. Pairing edges from different original components would merge those components and force `c<r`, so every surviving pairing is internal to original components. Equality in the edge bound forces each quotient component to be a tree. Conversely, taking an independently surviving internal pairing for each component gives a surviving whole-forest pairing, with product decoration weight and leading label-count coefficient one. Summing yields the factorization. Odd-edge components have no internal complete pairing. Odd total edge count is zero by symmetry of all edge Gaussians. Isolated and empty forests are covered.

As an independent exact check, for the stated two-edge decorated star and two disjoint copies, direct Gaussian label enumeration gave

\[
T_n(\text{star})=3,\qquad
T_n(\text{two stars})=9+\frac{114}{n}+\frac{192}{n^2}.
\]

The second identity also follows independently by conditioning on `u`: the star observable is the empirical mean of `z_i^2`, so its squared expectation is `(1+2/n) E q_n^2`, with `E q_n^2=9+96/n`. Two isolated first-population vertices each decorated by power one instead give `1/n`; two disjoint undecorated single-edge components also give `1/n`. These explicitly test finite-width contributions that vanish in the theorem. The theorem asserts limiting expectation factorization, not exact finite-width factorization or concentration.

### Canonical colored forest keys

The proof's inductive rooted-tree argument is complete: the pair consisting of the root color and sorted child-key tuple preserves child multiplicity and recursively characterizes rooted color-preserving isomorphism. Equal unrooted minima furnish roots with equal rooted keys; a genuine unrooted isomorphism also preserves the set of possible rooted keys. Sorting component keys preserves component multiplicity, including identical isolated vertices.

`forest_key`, at `exact_calculus.py:88–140`, implements this construction. Layer and decoration are separate exact integer entries. An index is checked before indexing; negative indices and booleans cannot exploit Python indexing behavior. Edge validation rejects loops, out-of-range endpoints, same-layer edges, duplicates in either orientation, and cycles. Once acyclicity holds, omitting only the parent in recursion is sufficient. Union-find mutation is confined to locally created arrays. Keys contain tuples and integer scalars only, so later caller mutations cannot alter their values or hashes.

This key describes the supplied fully summed, simple, vertex-decorated forest model. There are no distinguished unsummed endpoints in that model. Reusing the key for objects with such endpoints, extra edge decorations, or other omitted structure would require extending the colors/key; the source makes no assertion authorizing that extension. Similarly, the key does not itself calculate an expectation or implement a general coefficient compiler.

### Finite initialization derivatives and width normalization

For the stated stored coordinates,

\[
\partial_{a_i}f_n=z_i^2/n,\quad
\partial_{W^{(2)}_{ij}}f_n=2a_i z_i u_j^2/n.
\]

Readout mobility `n` and stored hidden mobility one therefore give `a_i'=z_i^2` and, using `g=sqrt(n) W^(2)`, `g_ij'=2a_i z_i u_j^2/sqrt(n)`. Freezing `u` gives `z_i'=2q_n a_i z_i` with `q_n=n^-1 sum u_j^4`. Thus both the width factors and the coordinate conversion in (7.C1)–(7.C3) are correct. The chain rule applies repeatedly because `q_n` is constant along this auxiliary flow.

Conditional on `u`, independent Gaussian rows of `g` give independent `z_i ~ N(0,q_n)`, independent also of the readout. Substituting `z=sqrt(q) xi` makes the differential operator equal to `q` times the variance-one operator, and the starting polynomial contributes another factor `q`. Consequently the conditional expected derivative is `c_k q_n^(k+1)`. The degenerate value `q=0` follows directly from the polynomial identity as well.

The annealed passage to the limit uses actual moment control: `E(q_n-3)^2=96/n`, Jensen gives uniformly bounded moments `E q_n^(2b)`, and the difference-of-powers bound followed by Cauchy–Schwarz gives `E|q_n^b-3^b| -> 0`. This proves the stated fixed-order expectation limit. No derivative of an expected positive-time solution, infinite-series interchange, or uniform existence interval is needed. The polynomial finite ODE has a local solution at each initial state, sufficient for its initialization derivatives.

The monomial rule (7.C5) and its parity argument are correct. The new implementation applies this rule, starts from `a*z^2`, and computes exactly orders zero through thirteen.

### Formal inversion and the Stieltjes obstruction

Since `d_0=0` and `d_1=63`, formal inversion is well defined over the rational field. At each degree `k`, the only term depending on the new inverse coefficient is `a_1 b_k`, proving the recursion (7.C8). Oddness of `F` implies oddness of its inverse and evenness of `F'(B)` by formal uniqueness. Derivatives through order thirteen suffice for the even kernel coefficients through degree twelve and hence for all six displayed moments. The conversion from derivatives to ordinary coefficients correctly divides by `k!`.

An independent derivation avoided repeatedly applying the implementation's differential operator. Put `w=z^2`, so `a'=w` and `w'=12aw`; hence

\[
a'=6a^2+(W-6A^2),\qquad a(0)=A,\quad W=Z^2.
\]

Integrating as a polynomial-valued formal series, with coefficients `h_k`, gives `h_0=A`, `h_1=W` and

\[
h_{k+1}=\frac6{k+1}\sum_{i=0}^k h_i h_{k-i}\quad(k\ge1).
\]

Coefficients of `a*a'` were then averaged using Gaussian moments expressed with factorials. This reproduced all fourteen ordinary coefficients of `F` and therefore all fourteen derivatives, including every integer in (7.C6).

A separate inverse candidate was obtained by powering the reciprocal series `s/F(s)`. Its two composition identities were checked explicitly by schoolbook power sums, so correctness did not rely on assuming an inversion theorem. Finally `K=1/B'` was computed by reciprocal-series recursion, independently of production Horner composition. It agreed with every returned inverse/kernel coefficient and every fraction in (7.C9).

For the shifted moment matrix, the independently computed leading two-by-two determinant is

\[
\mu_1\mu_3-\mu_2^2=
\frac{2068914936324736}{9811856586021847245}>0.
\]

Solving its two equations with `v_2=1` gives precisely the two displayed witness coefficients. Direct multiplication verifies that the first two entries of `Mv` vanish. Both

\[
\det M=-\frac{86245462994269879146938487857152}
{200150589172828762588730609071155193161975}
\]

and

\[
v^T Mv=-\frac{673792679642733430835456936384}
{329714727520793070279653295504327135}
\]

were reproduced. The independent identity `det(M)=(mu_1 mu_3-mu_2^2)*(v^T Mv)` also passed. A representing nonnegative measure on `[0,infinity)` would make the latter quadratic form equal to `integral lambda*(v_0+v_1 lambda+lambda^2)^2 dnu >= 0`. All powers involved are among the assumed finite moments. This contradiction requires neither analyticity of `F` nor a positive-time dynamical identification.

## Algorithm and dependency audit

`_multiply` performs finite convolution. `_compose` uses Horner order. Truncating the outer series is legitimate at its actual call sites because the inner inverse series has zero constant term. These private helpers are not advertised as composition routines for arbitrary nonzero-constant inner series. `revert_series` uses the previous inverse coefficients with the current unknown coefficient still zero, then cancels the degree-`k` error by division by the nonzero rational linear coefficient. Input coefficients are copied and every returned coefficient is a `Fraction`. Its conservative `O(N^4)` rational-operation bound is consistent with the loops.

`determinant` copies every row before elimination, selects a nonzero remaining pivot, changes sign on row exchange, and multiplies the unchanged pivots. Row subtraction preserves the determinant. If a remaining pivot column is zero, the remaining block is singular. Empty and singular cases return exact `Fraction` values. Aliasing of immutable scalar values is harmless; source rows are not mutated.

The new public rational interfaces reject floats and booleans by exact type checks. Forest indices/colors similarly require exact Python integers. Returned certificate lists and dictionaries are constructed anew on every call, and the graph result is immutable. The certificate's local integer moment function and rational polynomial accumulator introduce no floating operations. There is no global cache, file output, sampling, or hidden coefficient table.

The finite-network dependency's mathematical normalization agrees with `NOTATION.md`: first-layer input scaling is `1/sqrt(d)`, output scaling is `1/n`, backpropagated deltas exclude residuals, loss is the mean squared loss without one-half, and endpoint block mobilities are `n*kappa`. Inspection and independent rational differentiation agree on gradients, weighted kernel blocks, physical velocity, and simultaneous GD. Activation callback arguments and outputs are copied in `_evaluate`; update arrays are newly allocated. Parameter arrays themselves are intentionally not copied on construction, as documented, so a frozen dataclass is not a promise of immutable underlying arrays.

`finite_network._kappas` accepts strictly positive mobilities and therefore cannot directly run the zero-first-mobility example. This is not a proof/implementation mismatch: (7.C2) separately defines an auxiliary feature-ascent system, and `quadratic_axis_certificate` implements its scalar initialization recurrence without calling that training API. No use was made of `initialize`, whose documented small-readout initialization differs from the certificate's explicitly stated order-one readout.

## Executed deterministic verification

The supplied test command was:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde-exact-calculus-isolated.c6rGfOO8 python -B -m unittest discover -s tests -p test_exact_calculus.py -v
```

All **7 supplied tests passed**. Their exact coefficient comparisons were supplemented, rather than treated as independent proof of their shared constants, by the Riccati calculation described above.

Additional bounded checks, all passing:

| Check | Extent and independent oracle |
| --- | --- |
| Reversion | 324 length-six series: linear coefficient in `{-2,-1/3,1,2/3}`, four subsequent coefficients in `{-1,0,1}`. Reciprocal-power inverse candidates, both independently computed composition identities, production equality, and unchanged inputs. |
| Determinants | All 19,683 three-by-three matrices with entries in `{-1,0,1}`, plus empty, rational singleton, and a four-by-four matrix requiring pivot swaps: 19,686 cases against Leibniz permutations. |
| Forest isomorphism | All layer splits with at most five vertices, all simple bipartite edge subsets, and decorations in `{0,1}`. 5,173 valid decorated inputs and 656 cyclic rejections. An independent adjacency encoding minimized over within-layer permutations yielded 812 isomorphism classes. Both directions of key/oracle equivalence and relabeling invariance passed. |
| Forest ownership | Mutated nested input color/edge lists after key construction; the old key and hash remained equal to a fresh key for the original graph. |
| Finite forest sums | Five examples at each of widths 1, 2, 3, 4: 20 exact label-sum checks, including the star identities, an isolated second-layer squared decoration, odd-decoration collisions, and cross-component edge pairings. |
| Gaussian recurrence | 200 exponent choices against independent polynomial expansion of `X=A G`, using full-rank, zero-row, rank-one, and three-variable singular rational covariance examples. |
| PSD validation | All 729 symmetric three-by-three matrices with upper-triangle entries in `{-1,0,1}`; acceptance compared with nonnegativity of every principal minor computed by permutations. Invalid types and validation before zero/odd-degree shortcuts also checked. |
| Entire certificate | Independent Riccati integration, candidate inverse checked in both composition directions, reciprocal derivative for the kernel, all fourteen derivatives, all six moments, permutation determinant, witness equations, determinant/witness identity, exact scalar types, and fresh ownership after mutation of every returned list. |
| Finite dependency | A deterministic width-two, input-dimension-four, three-hidden-layer quadratic network with two samples: all 18 parameter derivatives and four kernel blocks compared with exact rational forward-mode differentiation; output, loss, physical velocity, GD, and update ownership checked. Floating comparisons used tolerances at most `2e-14` relative and `1e-14` absolute. |
| Certificate coordinates | A deterministic width-four quadratic network checked stored-to-unscaled hidden mobility, readout mobility, `z'=2qaz`, and the first chain-rule derivative. No time integration or sampling. |

The finite exhaustive cases test the implementations; the general forest and rational-algorithm claims are supported by the mathematical arguments above. Recursion-depth and coefficient-size limits remain the explicitly documented implementation limits, not correctness claims for unbounded inputs.

## Corrections and residual scope

Required proof corrections: **none found**.

Required exact-calculus code corrections: **none found**.

Required changes to the claimed probabilistic scope: **none**; the supplied text already limits its bridge to fixed-order annealed initialization jets and explicitly excludes the stronger dynamical and unit-metric conclusions.

No result here certifies an unimplemented general forest expectation evaluator or general-depth coefficient generator. No result establishes series convergence, empirical concentration, a positive-time population equation, or behavior with strictly positive first-block mobility. Those are outside the supplied claims, rather than gaps in the theorem actually audited.
