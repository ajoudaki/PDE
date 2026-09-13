# Tanh polynomial initializer: implementation and deterministic checks

2026-09-13. Implementation artifacts:

- `H3_v2_initialization.py`: dictionary, fast core initialization, normalization,
  generic compiler fallback and resource checks.
- `H3_v2_initialization_tests.py`: executable static checks with canonical-module
  test bootstrap.
- `H3_v2_basis_synthesis.md`: mathematical contraction and normalization argument.

This is an implementation-stage synthesis after the route freeze, not an
independent review or promotion. The original `H3_v2_route_basis.md` is unchanged.
No trajectory or neural simulation was run, and no Git operation was performed
for this implementation task. Only this route's files and generated test logs
were written.

## Public interface

The proposed canonical module is `pde.observable_initialization`. It imports the
existing Word builders from `pde.observable_closure`; optional default imports
resolve `pde.observable_arithmetic.gaussian_points` and
`pde.observable_compiler.compile_raw_dictionary`. There are no study-module
imports or runtime path modifications in the implementation.

```python
dictionary = build_dictionary(order, limits=InitializationLimits(...))

features = initialize_features(
    order,
    arithmetic=ar,
    initialization_nodes=Q,
    population_nodes=P,
    epsilon_cov="0.01",
    limits=InitializationLimits(...),
    gaussian_points=optional_gaussian_rule,
    raw_compiler=optional_compiler_callable,
)
```

The optional Gaussian callable has signature `(count, dimension, arithmetic)`
and returns a complete same-population Gaussian cloud. The optional compiler
has the agreed `compile_raw_dictionary` interface. The caller passes the
arithmetic object; all arithmetic and array algebra occur within its context.
The float, Decimal and rational fixed-point backends are supported through the
same scalar interface.

The result has exactly these fields:

| Field | Shape / content |
|---|---|
| `b1` | `P × d1` frozen first-population feature values |
| `g` | `P × 2` Gaussian seeds from those same first-population nodes |
| `p1` | `P` first-population probabilities |
| `b2` | `P × d2` frozen second-population feature values |
| `p2` | `P` second-population probabilities |
| `D` | `d2 × d1` initialized compressed action coefficients |
| `metadata` | finite scalar/string/list configuration, counts and estimates |

The solver constructs `w=g`, `c=0` and `M=D` from this output. No initial
finite-neural array is created. The compiler/source tape, quadrature source
expressions, Grams and normalization matrices are discarded when initialization
returns. Metadata contains no dense arrays or hidden source program.

## Dictionary and the actual fallback boundary

The core is the total-degree Chebyshev dictionary in

```text
X1 = (tanh g1, tanh g2, tanh p1, tanh p2),
X2 = (tanh xi1, tanh xi2),
xi_i = A0 tanh g_i,  p_i = A0* tanh xi_i.
```

Exponent tuples are ordered first by increasing total degree, then descending
lexicographically. Recurrences expand into the existing ordinary bounded Word
operations. Dependencies are compiled but never automatically retained as
feature columns. The original valid bounded code prefix through `N` is appended
after the polynomial outputs. Only equal symbolic words are deduplicated;
linearly dependent but syntactically distinct values remain.

The first three output dimensions are exactly `(5,3)`, `(15,6)` and `(35,10)`.
Their strictly increasing span dimensions are proved in the synthesis report.
At order four, code 4 adds `sin(1)` as a distinct syntax column, giving `(71,15)`;
this deliberate constant dependence is regularized, not pruned.

The fast evaluator supports all bounded words using only the four/two existing
core coordinates, including the later no-new-action trigonometric tail words.
It dispatches to the generic compiler when a *retained bounded output* has an
action dependency outside the four core action words. In particular, code 7
is the unbounded word `A0(1)`, so code 7 alone does not trigger fallback. Its
first bounded wrapper is code 60, `sin(A0(1))`. This corrects an early planning
message that suggested fallback at order seven.

This original code schedule has a mathematically dense continuation but an
expensive first outside-core polynomial order. The implementation does not
pretend that degree 60 is practical. It neither replaces the required exhaustive
tail nor silently caps the mathematical dictionary. Every request is governed
by explicit caller-adjustable resource limits; no rejected request produces a
smaller dictionary.

## Fast coefficient integration and separate population replay

For coefficient integration size `Q`, generate a four-dimensional cloud and a
two-dimensional cloud through the supplied Gaussian rule. Recompute, in the
chosen arithmetic,

```text
v = E_Q tanh² G,
tau_core = E_Q tanh²(sqrt(v) G),
alpha = E_Q [1-tanh²(sqrt(v) G)].
```

Use the exact symmetry-reduced model structure `xi_i=sqrt(v) Z_i` and
`p_i=sqrt(tau_core) Z'_i + alpha tanh g_i`. Thus the scalar expectations are
numerically integrated, while the diagonal covariance structure is fixed by
the proved canonical symmetry. The resulting finite rule is an approximation
to canonical initialization. Nonpositive unresolved scalar variance or response
raises a numerical error; it is not repaired by deleting a field.

The raw core matrices use the bounded-integrand identity proved in the
synthesis report:

```text
C[B,F] = sum_i E_Q[F tanh g_i] E_Q[partial_xi_i B]
       + sum_i E_Q[partial_zeta_i F] E_Q[B tanh xi_i].
```

The second sum is the nonzero reverse-to-forward response. Derivatives are
formal named-source derivatives. They are computed through the explicit
Chebyshev recurrence, with the tanh chain factor, rather than differentiating
quadrature nodes, covariance estimates or the source normalization. Mixed
polynomials are handled with a direct product rule that never divides by a
possibly zero feature value.

These coefficient estimates and the raw `Q`-point feature Grams are then
frozen. New `P`-point Gaussian clouds evaluate the entire joint raw mark maps,
retaining `g` on the same first-population row. No individual feature column
is sampled separately. Changing `P` at fixed `Q` leaves `D` unchanged and
replays the same feature functions. The tests verify this with two distinct
population counts.

The fast core needs no numerical source covariance regularizer, since its
four named source variances are explicitly nondegenerate. The common public
parameter `epsilon_cov` must be positive but is unused in this branch; metadata
records `epsilon_cov_used=False`. In the generic branch, it is passed to the
complete compiler and is active. It must not be confused with `tau_core`, the
strictly positive model variance. A source-regularizer limit is vacuous for
the fast branch and remains a distinct axis for the generic branch.

## Normalization, generic branch and numerical semantics

The same normalization is applied to both branches:

```text
eta = 1/[1024(N+1)^2],
G_l + eta I = L_l L_l.T,
T_l = inverse(L_l),
b_l = raw_l @ T_l.T,
D = T_2 @ C @ T_1.T.
```

The right transpose in `D` is necessary because inverse-Cholesky transforms
are nonsymmetric. A deterministic raw-filter oracle checks this orientation.
The synthesis report proves that this gives exactly the symmetric ridge
filter and equivalent Euclidean coefficient dynamics up to orthogonal change
of coordinates.

For the generic branch, the initializer requests the full first/second word
lists from `compile_raw_dictionary`, which compiles their complete same-program
joint union. It consumes `psi1,psi2,g,probabilities1,probabilities2` at population
resolution `P`, and `gram1,gram2,C` at coefficient resolution `Q`. It uses the
forward raw contraction `C` and the actual transpose in future evolution;
`C_reverse` is a compiler diagnostic and is not independently substituted or
averaged into this initializer. The full compiler's source covariance and
arithmetic limits remain separate from the feature ridge.

There is no operator-norm clipping. At finite integration and population
resolution, neither an exact `||D|| <= 2` assertion nor a contraction assertion
for the independently replayed `P`-point feature Gram is made. Those assertions
hold at the exact canonical coefficient-law limit; finite-resolution stability
uses the fixed-order bounded-feature comparison in the mathematical report.
Likewise finite arithmetic probabilities are approximations to `1/P`; their
exact real values occur in the innermost arithmetic limit.

## Resource boundaries

`InitializationLimits` separately controls retained features per population,
dictionary DAG nodes, enumerated codes, Gaussian point counts, estimated peak
working bytes and estimated scalar algebra work. The optional `compiler_limits`
is passed intact to the general source compiler. Feature/count limits are
checked before building the large feature arrays; byte/work estimates are
checked before requesting clouds. Resource exhaustion raises
`InitializationResourceLimit`; it never drops a word, an eigenmode or a source.

The initializer reports both its output scalar count and the scalar count of
the complete closure state before data storage:

```text
output: P(d1+d2+4) + d1*d2,
closure: P(d1+4) + P(d2+1) + 2*d1*d2 + 2P.
```

The latter includes `g,w,c`, both feature tables, `M,D`, and both probability
vectors. These are counted scalar entries, not bits or guaranteed resident
memory. The working-byte estimates include conservative numeric-array factors;
they are allocation guards, not a resource certificate. Generic source work
is checked again by the compiler. Increasing degree, precision or quadrature
can require increasing several explicit limits. No default limit is part of
the mathematical definition of the dense hierarchy.

## Executed deterministic checks

Command, from the shared checkout root:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/observable_hierarchy/H3_v2_initialization_tests.py
```

The test bootstrap loads the candidate files under their planned canonical
module names; it does not edit the established package. The final run enforced
600 CPU seconds and 4 GiB address-space limits. It used Python 3.10.12,
NumPy 1.26.4 and one BLAS thread. All ten tests passed in 0.286 test seconds
(0.418 seconds including the subprocess wrapper):

- exact first-three dictionary counts, nesting and exclusion of the unbounded
  code-7 dependency from retained columns;
- first-population reverse and second-population forward named derivatives
  against independent finite differences, including degree-three mixed terms;
- inverse-Cholesky normalization against a direct raw-filter linear-algebra oracle;
- the known `alpha*v` covariance entry and a nonzero reverse-response contribution;
- independent coefficient/population axes and replay at all first-three orders;
- a thirty-versus-fifty-digit Decimal refinement check at a fixed finite initializer;
- a small rational fixed-point initializer compared with Decimal arithmetic;
- actual generic-compiler dispatch and normalization on a small explicit
  outside-core-action fixture;
- resource rejection before Gaussian cloud allocation;
- retained `sin(1)` constant dependence at order four without rank pruning.

The generic fixture is deliberately a small augmented degree-one word list.
It validates the actual cross-module interface, not execution of the enormous
full order-60 dictionary. No trajectory, prediction-error trend, trained feature
motion or empirical large-order cost was measured.

The first run had eight passes and one error caused by placing an upper-population
test word in the fixture's lower list. The fixture was corrected; the original
failed log remains. The corrected nine-test run passed, and the final run added
the retained-constant-tail check. Evidence locations:

- `data/generated/observable_hierarchy/H3_v2_route_basis/initialization_check_20260913/tests.log`
- `data/generated/observable_hierarchy/H3_v2_route_basis/initialization_check_20260913_corrected/tests.log`
- `data/generated/observable_hierarchy/H3_v2_route_basis/initialization_check_20260913_final/tests.log`
- `data/generated/observable_hierarchy/H3_v2_route_basis/initialization_check_20260913_final/record.json`

The final record preserves the command, environment, limits, exit code and all
used implementation hashes. At that run:

| File | SHA-256 |
|---|---|
| `H3_v2_initialization.py` | `f4b580fc7dcbe4206ec626d4b20df37030e8e0c13cffbd08b49d7de611772e10` |
| `H3_v2_initialization_tests.py` | `0e04bb3633d094d381403a5158e62a6207bb5fe8bbe6d9d78abf12f6d62ddacb` |
| `H3_v2_compiler.py` | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `H3_v2_arithmetic.py` | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `H3_v2_fixed.py` | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |

Static checks establish the stated finite implementation identities and the
tested interfaces. They do not independently establish the Halton W2 theorem,
full generic source-compiler limit, nonlinear trajectory limit or promotion
readiness. Those are separately proved/reviewed dependencies in the assembled
candidate.
