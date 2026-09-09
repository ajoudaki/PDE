# Fresh isolated adversarial proof/code audit

Audit date: 2026-09-09.

**Verdict: PASS for the stated finite-expectation, canonical-key, rational-arithmetic, and fixed-order annealed initialization-jet claims. No required mathematical or implementation correction was found.** This is a source and exact-calculation audit, not a machine-checked proof or a positive-time identification result.

The finite-forest theorem is an asymptotic statement about expectations. The certificate concerns the explicitly frozen first block, order-one stored readout, and feature-ascent clock. It rules out the specified nonnegative Stieltjes moment representation for those formal coefficients. It does not refute a unit-mobility model, strictly positive first mobility, or positive-time nonlinear dynamics.

## Read scope and immutable input manifest

The sole input root was `/tmp/pde-exact-calculus-isolated.c6rGfOO8`. All seven files below were read completely, including all of the contained Gaussian Section 4 and new Section 7.2. Total: 1,259 lines. Every input was a regular file. SHA-256 hashes were computed before the checks and recomputed afterward; all matched. A second file inventory still contained exactly these seven files.

| Relative input path | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `PROOF.md` | 345 | 17119 | `a02761d75c0eeb0e233cdd9cba460003ce3892238762abb0b3c79f221b12b0cf` |
| `NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `pde/__init__.py` | 26 | 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `pde/finite_network.py` | 363 | 15525 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `pde/gaussian_moments.py` | 114 | 4464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `pde/exact_calculus.py` | 191 | 7542 | `482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41` |
| `tests/test_exact_calculus.py` | 122 | 5875 | `b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439` |

No repository, studies, history, prior reviews, internet, skill files, or agent instructions were read. No input was edited. No sampling, scientific experiments, historical generators, builds, installations, Git operations, or data artifacts were used. Additional checks were small deterministic Python programs executed from standard input; they were not saved as files. Every Python invocation used `PYTHONDONTWRITEBYTECODE=1`, `-B`, and `PYTHONPATH=/tmp/pde-exact-calculus-isolated.c6rGfOO8`, with working directory `/tmp`.

Package imports execute `pde/__init__.py`, which imports the supplied finite-network and Gaussian-moment modules. These sources were read in full. The production exact-calculus module itself uses `fractions.Fraction` and `math.factorial`; its certificate implements its own scalar Gaussian moments. Existing Python/NumPy runtime imports were used for deterministic checks, but external runtime/library source was not inspected or independently certified.

This report is the only created file. Its containing directory was obtained by a successful `mktemp -d /tmp/pde-exact-calculus-audit.XXXXXXXX`, returning `/tmp/pde-exact-calculus-audit.lsG87FJV`.

## 1. Gaussian moments and exact covariance validation

Sources: `PROOF.md:1–59`; `pde/gaussian_moments.py:9–114`.

The integration-by-parts argument is valid for singular positive semidefinite covariance: write `X=AG`, integrate in the standard Gaussian variables, and apply the chain rule. Polynomial growth removes the boundary terms. Selecting one occurrence of coordinate `i` gives precisely the coefficient `alpha_j - 1_(j=i)` in (9). Odd total degree vanishes; degree zero is one; every retained term decreases degree by two.

The implementation subtracts that selected occurrence before iterating through the remaining counts, skips zero covariance entries, and never creates a negative exponent. Dimension, symmetry, scalar type, exponent, and PSD validation all precede the odd/zero-degree exits. The nonempty-covariance restriction is explicit in the API. Returned moments are exact `Fraction` values for the intended input types.

The Schur-complement PSD validator also matches the proof. A negative pivot fails; a zero pivot requires an entirely zero remaining first row; a positive pivot reduces to its exact Schur complement. Symmetry is checked initially and preserved by the reduction. No zero-pivot division or numerical tolerance occurs. Local memoization is cleared in `finally`, with no cross-call cache. Input covariance rows and exponents are copied into immutable tuples.

Independent checks: 270 moment cases agreed with direct enumeration of labeled Wick pairings, including zero, singular, rational, and negatively correlated covariances. Another 87 checks verified PSD/symmetry acceptance or rejection, including invalid covariances with odd and zero requested degree.

## 2. Finite-forest expectation factorization

Sources: `PROOF.md:73–130`; population conventions in `NOTATION.md:46–55`.

The free-index count is correct. For a fixed pairing of `e=2p` Gaussian edge factors, covariance of `g_ij` with `g_kl` identifies **both** corresponding endpoints. The quotient keeps all original vertices modulo these identifications, including isolated vertices, and keeps `p` edges with multiplicity. Consequently `v <= p+c`, including when some quotient components are isolated, and `c <= r` because identifying vertices cannot split an original component.

For this pairing the normalization is `n^(-p-r)`. Distinct quotient labels must be counted separately in the two populations: `(n)_(v_1) (n)_(v_2)`, with leading term `n^v`. A numerically equal label in different populations does not identify their variables. The proof does not make that erroneous identification.

Each quotient vertex receives the **sum** of all decorations identified there. Thus the decoration factor is the Gaussian moment of that summed exponent, not the product of the original vertex moments. Additional equalities between distinct quotient vertices of the same layer cost at least one free label. They can turn an otherwise zero decoration expectation into a nonzero one, but their moments remain bounded by a fixed decoration-dependent constant, so they cannot restore leading order. The same argument covers isolated decorated vertices and vertices originating in different components.

Every pairing contributes at most order one. Equality `v=p+r` forces both `c=r` and equality in each connected edge bound. A pairing across original components necessarily merges components, so cannot survive. The surviving pairings are exactly the products of internally surviving component pairings, their decoration moments multiply, and their free-label leading coefficients are one. This proves the asserted product of limits. An odd-edge component has no complete internal pairing; total odd edge count vanishes exactly by Gaussian symmetry. Empty forests and isolated vertices are covered.

The argument never substitutes finite-width independence for expectation factorization. In particular, two disjoint graph components can share labels in the sum and can be dependent at finite width.

An independent finite check enumerated typed label-equality partitions, aggregated decoration powers and Gaussian edge multiplicities, and used exact falling-factorial label counts. It did not use the proof's edge-pairing quotient algorithm. Across bipartite population sizes `(0,0), (0,2), (2,0), (1,1), (1,3), (2,2), (2,3), (3,3)`, it checked 1,637 decorated forests from 410 underlying forests. All expected numerator degrees satisfied the claimed normalization bound, and every leading coefficient equaled the product of the connected-component leading coefficients. All 195 cyclic graphs in the graph inventory were rejected by `forest_key`.

Useful exact collision checks were:

| Graph | Exact normalized expectation |
| --- | --- |
| One two-edge star with leaf decorations `u^2,u^2` | `3` |
| Two disjoint copies of that star | `9 + 114/n + 192/n^2` |
| Two isolated first-layer vertices, each decorated by `u` | `1/n` |
| Two disjoint undecorated one-edge components | `1/n` |

For the two-star case, if `S_n=n^(-1) sum_i z_i^2`, then `E[S_n^2 | u]=q_n^2(1+2/n)` and `E q_n^2=9+96/n`. This independently explains the displayed finite correction terms. No graph/free-index/decoration collision defect was found.

## 3. Canonical colored forest keys

Sources: `PROOF.md:132–152`; `pde/exact_calculus.py:88–140`.

The rooted tuple is a structured pair of `(layer, decoration)` and the sorted tuple of child keys. Its nesting retains tree structure, vertex colors, and repeated children. Induction gives the stated equivalence with color-preserving rooted isomorphism. Minimizing over every root gives an unrooted isomorphism invariant that is also complete: equal minima exhibit suitable roots and an isomorphism. Sorting the component keys preserves repeated components, so the forest key is complete as well. Layers, zero decorations, isolated vertices, and the empty forest remain distinguishable.

The union-find implementation rejects self-loops, out-of-range indices, same-layer edges, duplicate edges in either orientation, and cycles. Accepted indices, layer values, and decorations are exact Python integers, excluding booleans and integer subclasses. Colors are copied to tuples, and all returned key containers are tuples. Mutating the caller's nested input lists afterward does not change the key or its hash.

For all 1,637 decorated forests above, keys were compared with an independent complete vertex-permutation/adjacency canonicalization, not another recursive tree-key algorithm. The 661 distinct colored-isomorphism classes had neither collisions nor different keys within one class. The supplied tests additionally verify all 120 vertex orders of a five-vertex example, with reversed edge order and orientation.

The documented all-roots cost and Python recursion limit are genuine scope limits, not hidden large-graph guarantees. No key defect or ownership defect was found.

## 4. Rational reversion and determinants

Sources: `PROOF.md:242–261,305–315`; `pde/exact_calculus.py:13–85`.

`revert_series` is correct over the rational field. At step `k`, `b[0]=0`, coefficients below `k` have already been determined, and `b[k]` is still zero. Any occurrence of the unknown `b[k]` in a power of `b` of order at least two has degree greater than `k`. Therefore the missing degree-`k` term is exactly `a[1]*b[k]`, justifying the assignment. Truncating the outer polynomial at degree `k` is valid because the inner constant is zero. This zero-constant condition also holds at every production call of the private composition helper; no unsupported general composition behavior is needed.

Horner composition and multiplication preserve ordinary coefficient normalization. Rational conversion occurs before division, so `1/a[1]` and subsequent quotients remain `Fraction`; no floating division is introduced. The inverse has the input length and fresh mutable storage. Nonzero constant, zero linear term, short input, floats, booleans, and unsupported containers/types are rejected.

`determinant` copies all rows into rational working rows, including when caller rows alias. It tracks row-swap signs and multiplies successive nonzero pivots. Eliminating below each pivot preserves the determinant, and no remaining pivot implies singularity. The empty determinant is exactly `Fraction(1)`. Rectangular inputs and nonrational values are rejected without input mutation.

Independent direct-power composition checks passed for 135 additional rational series in both inverse directions. An independent Leibniz-permutation determinant matched all 81 two-by-two matrices over `{-1,0,1}` and all 512 three-by-three matrices over `{0,1}`. Supplied tests cover further rational matrices, negative linear coefficients, singular matrices, row swaps, and empty cases. No algorithm or exact-fraction defect was found.

## 5. Frozen-first-block initialization-jet bridge

Sources: `PROOF.md:156–240`; `NOTATION.md:16–24,70–86`; `pde/finite_network.py:202–238,276–314,341–355`.

The stored-coordinate normalization in (7.C2) is correct. Differentiating (7.C1) gives

`partial f_n / partial a_i = z_i^2/n`,

`partial f_n / partial W^(2)_ij = 2 a_i z_i u_j^2/n`.

Readout mobility `n` therefore gives `a_i'=z_i^2`. Hidden stored-block mobility one and `g_ij=sqrt(n) W^(2)_ij` give `g_ij'=2 a_i z_i u_j^2/sqrt(n)`. Freezing `u` makes `q_n=n^(-1) sum_j u_j^4` constant along this auxiliary flow, and hence `z_i'=2q_n a_i z_i`. There is no omitted residual, factor two from a loss, or additional width factor in this feature-ascent clock.

Repeated chain rule now gives (7.C3). The polynomial finite-dimensional vector field has a local smooth solution at every finite initial state, which is sufficient to define every finite initialization derivative. No uniform positive-time interval or interchange of expectation and time differentiation is needed.

Conditional on `u`, the rows of `g` and the independent readouts give iid pairs with law `N(0,1) tensor N(0,q_n)`. In the variables `z=sqrt(q)*xi`, the operator and observable become `D_q=q D_1` and `a z^2=q a xi^2`. Thus the conditional expected derivative is `c_k q_n^(k+1)`. The change of variables holds almost surely since `q_n>0` almost surely; the resulting polynomial identity also extends to `q=0`.

The width limit is justified explicitly: `E(q_n-3)^2=96/n`, and Jensen bounds `E q_n^(2b)` by `E|u|^(8b)` uniformly in `n`. The factorization bound for `x^b-3^b`, followed by Cauchy–Schwarz, proves convergence of each required moment. Consequently

`lim_n E[f_n^(k)(0)] = E[D^k(A Z^2)]`, with `D=z^2 partial_a + 6az partial_z`.

This is exactly the annealed initialization-derivative claim. It does not identify a positive-time mean, assert convergence of the formal Taylor series, or require concentration of the derivative average. As a finite-width normalization check, the first derivative satisfies `E[f_n'(0)]=7 E q_n^2=63+672/n`.

A separate deterministic rational state at `n=4` checked the stored-network derivatives and hidden-plus-readout kernel against these formulas. It gave `f=17/8`, `q_n=9/2`, and the frozen-block feature kernel `5237/16`, agreeing exactly after converting the finite-library results to rational values. No random initialization or time integration was used.

The existing finite-network flow API rejects zero first mobility, as required by its own positive-mobility contract. This is not a missing implementation of the certificate: the proof explicitly introduces a different auxiliary model, and `quadratic_axis_certificate` directly implements its polynomial recurrence. Its order-one stored readout is likewise explicitly different from `initialize`'s small readout. No metric or initialization ownership was silently transferred between the models.

## 6. Coefficients, inverse, and Stieltjes witness

Sources: `PROOF.md:218–301,317–326`; `pde/exact_calculus.py:143–191`.

The monomial differentiation rule, independent Gaussian moments with variances one and three, and the parity conclusion all hold. Every application toggles the `a` exponent parity and preserves the even `z` parity, so all even-index derivatives vanish. The code combines terms at identical exponent pairs by addition; no monomial collision overwrites a coefficient.

An independent derivation solved the formal ODE in `a` and `h=z^2`:

`a'=h`, `h'=12ah`, `a(0)=A`, `h(0)=Z^2`.

Ordinary polynomial-series convolution generated `a(s)h(s)` through degree thirteen. Applying the separately audited multivariate Gaussian-moment function to each coefficient reproduced all fourteen derivative entries, including the odd subsequence

```text
63
77760
274547232
2141006515200
31149221916487680
759035131220036321280
28719223368439752070594560
```

This route does not reuse the production Lie-derivative recurrence. Dividing by factorials yields the ordinary coefficients of `F`, as required; confusing them with exponential-series coefficients would change the result and did not occur.

Reversion and kernel coefficients were also checked independently by rational reciprocal-series arithmetic and the formal coefficient identity

`[y^m] G(B(y)) = (1/m) [s^(m-1)] G'(s) (s/F(s))^m`, for `m>=1`.

The identity is applicable because `F(0)=0` and `F'(0)=63` is invertible in the rational field. It follows by substituting `y=F(s)` in formal coefficient residues and differentiating `F(s)^(-m)`; it requires no analytic convergence. Taking `G(s)=s` reproduced all fourteen inverse entries; taking `G(s)=F'(s)` reproduced all thirteen kernel entries. Direct-power composition additionally verified both inverse identities through the supplied order.

Computing `K` through degree twelve requires `F` through degree thirteen, which is exactly what is generated. The sign convention `mu_j=(-1)^j [y^(2j+2)]K` is correct. All six moments agreed exactly:

```text
mu_0 = 480/49
mu_1 = 43756/151263
mu_2 = 7214528/200120949
mu_3 = 12545175968/2402451992745
mu_4 = 171752915595136/200241971143303005
mu_5 = 2199776554157960896/14570607030242443158825
```

For the shifted matrix `M_ij=mu_(i+j+1)`, the leading two-by-two determinant is

`2068914936324736/9811856586021847245 > 0`.

The displayed `v_0,v_1` solve the first two equations of `M v=(0,0,*)` with `v_2=1`. Independent rational multiplication and the permutation determinant give

```text
det M = -86245462994269879146938487857152 /
         200150589172828762588730609071155193161975

v = (40042013405871059816/2310453239160606810795,
     -14165989123115588/49896409440894219,
     1)

v^T M v = -673792679642733430835456936384 /
           329714727520793070279653295504327135
```

The additional identity `v^T M v = det(M)/(mu_1 mu_3-mu_2^2)` was verified exactly. For a nonnegative measure on `[0,infinity)` with these six moments, the same quadratic form would be `integral lambda*(v_0+v_1 lambda+lambda^2)^2 dnu`, which is nonnegative. Only moments through order five are needed, and their assumed finiteness justifies this finite polynomial integral. The negative value is therefore a complete finite obstruction to that moment representation.

No coefficient, index shift, normalization, determinant, witness, or truncation correction is needed. The formal coefficient construction supplies no additional positive-time claim, and the source does not assert one.

## 7. Test and ownership results

The supplied test command was run successfully:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde-exact-calculus-isolated.c6rGfOO8 \
python -B -m unittest discover \
  -s /tmp/pde-exact-calculus-isolated.c6rGfOO8/tests \
  -p test_exact_calculus.py -v

Ran 7 tests — OK
```

All additional deterministic checks described above passed. They are bounded checks supporting the source-level arguments, not exhaustive proofs for arbitrary graph sizes or coefficient orders.

Additional ownership/type checks covered mutation of nested graph inputs after key creation, aliased determinant input rows, mutation of a returned inverse, and independent ownership of every mutable list in separate certificate results. Every returned scalar and certificate list element had exact `Fraction` type. Float, complex, string, boolean, `None`, and numeric-subclass inputs were rejected by the exact rational interfaces; graph scalars required exact Python integers. No cross-call mutation or cache contamination was found.

`finite_network.Parameters` intentionally retains caller arrays, as its docstring states; that contract is not immutable array ownership. Its callback evaluation copies arguments and outputs, and the target finite normalization checks passed. This audit does not independently establish all numerical extreme-range behavior of the unrelated floating-point dynamics routines or correctness of Python/NumPy themselves.

## Required corrections and residual scope

**Required corrections: none.** There are no unresolved mathematical or implementation findings against the requested claims in the hashed input snapshot.

One optional editorial correction is concrete: at `PROOF.md:183`, change `\mathscr D_{q_n}^{,k}` to `\mathscr D_{q_n}^{k}`. The stray comma in the superscript is harmless because the following paragraph explicitly defines repeated application; it does not affect the proof or code.

No claim is certified here about a general coefficient compiler, large-order feasibility, concentration, empirical-law convergence, an analytic infinite series, positive-time population dynamics, the unit-mobility case, or strictly positive first mobility. Those are outside both the audited theorem's asserted bridge and this audit's verdict.
