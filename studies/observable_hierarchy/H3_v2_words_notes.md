# Exact initialized-word correction after the earlier freeze

2026-09-13. The coordinator's numerical-proof audit found that the initializer
still used the maintained Word builder's floating conversion of rational scale
factors and floating syntax envelopes. That dependence imposed an unintended
finite range even when later numerical arithmetic was refined. This correction
adds `H3_v2_words.py`, proposed canonical module `pde.observable_words`.

The only change to `H3_v2_initialization.py` is its import from
`pde.observable_closure` to `pde.observable_words`. Its dictionary selection,
Gaussian integration, contraction formula, normalization and returned state
are unchanged. The test bootstrap loads the new canonical module and the static
suite adds exact-syntax checks. No compiler, arithmetic, solver or trajectory
equation was edited. No trajectory was run. The coordinator preserves the
earlier source edition and records the new freeze separately.

## Exact finite grammar

The initialized grammar contains the same operations and typing rules:

| Operation | Population rule | Deterministic envelope |
|---|---|---|
| constant one | Either population | `Fraction(1)` |
| `g1,g2` | Population 1 | Unbounded (`None`) |
| rational scaling | Same population | `abs(a)*parent.envelope` if bounded |
| sum | One population | Sum of envelopes if both bounded |
| bounded product | One population, both operands bounded | Product of envelopes |
| sine, cosine, tanh | Same population, any L2 operand | `Fraction(1)` |
| initialized action | Bounded operand, opposite output population | Unbounded (`None`) |

Every non-`None` envelope is a `Fraction`, computed by exact integer/rational
operations. The scalar interface accepts integers and `Fraction` instances,
rejecting floating scalars. There is no floating conversion or fixed bit/range
bound in this module. The explicit caller resource limits still govern actual
dictionary/compiler requests. They reject requests rather than redefining the
word language.

These envelopes are proved by induction on the finite expression graph:
triangle inequality handles a sum, absolute homogeneity handles scaling,
the scalar product bound handles a bounded product, and the three elementary
gates are bounded by one. Actions are retained as L2 fields without a claimed
pointwise envelope. Zero times an unbounded seed keeps the original L-sort
typing; no new simplification rule is introduced.

Words expose `op,population,args,scalar,envelope,bounded`, which is the existing
compiler's required structural interface. Only initialized seeds `g1,g2` are
provided; this module is not the runtime observation API for moving `w,c` or
arbitrary frozen direction marks.

## Natural codes are unchanged

Codes 0, 1, 2 and 3 are the two constants and `g1,g2`. For `n>=4`, write
`n-4=8k+j`, `0<=j<8`. Opcodes 0, 1 and 2 apply sine, cosine and tanh to code
`k`; opcode 3 applies the correctly oriented action to that bounded child.
For the remaining opcodes, Cantor-unpair `k` into `(a,b)`. Opcodes 4 and 7 add
codes `(a,b)`; opcode 5 multiplies them with the original bounded typing;
opcode 6 scales code `b` by `r(a)`. Cantor pairing and unpairing are exact
integer operations, with `math.isqrt` for unpairing. The signed-rational
enumeration `r` is exactly the original one and returns a `Fraction`.

Each dependency is strictly smaller than its parent code. The decoder keeps
an explicit stack, first decoding missing dependencies and then applying the
corresponding constructor. Invalid dependencies or typing cache `None`. An
induction on the natural code therefore proves the following: every code has
the same valid/invalid status, operation, population, ordered operand syntax,
rational scalar and B/L sort as the stated original mathematical grammar.
The old floating implementation may cease to implement that mathematical
grammar at very large rationals; the correction removes that limitation.

The decoder processes only the requested dependency graph, not every integer
up to a potentially huge isolated code. There is no Python recursive call for
decoding and no fixed code ceiling. Its cache contains only finitely many
entries after any finite collection of calls.

## Literal equality and arbitrarily deep finite DAGs

Word nodes are immutable. Each node caches a hash computed from its operation,
population, scalar and its already cached child hashes. Hashing a constructed
node never descends recursively into its parents. Structural equality uses
an explicit stack of node pairs. It checks node attributes and ordered children,
and skips a pair already visited; hence shared subgraphs do not cause an
exponential unfolding of the corresponding expression tree. Hash collisions
do not imply equality: the structural stack still checks the full literal
syntax. Equal literal syntax always produces the same cached hash.

There is no algebraic simplification. For example `1` and `scale(1,1)` remain
distinct words, while two separately constructed copies of the same expression
compare equal. Rational scalars have the canonical equality of `Fraction`, as
in the original builders. These are precisely the initializer's literal
deduplication semantics. A compact `repr` avoids recursive graph expansion
and avoids formatting huge rational integers through decimal-string limits.

The Chebyshev builder already forms its degree recurrence iteratively. With
exact envelopes and cached nonrecursive word hashes, its degree-dependent
graph construction no longer encounters either the old floating-envelope
overflow or recursive Word hashing/equality. This is a syntax statement, not
a claim that storing all total-degree features at a huge degree is economical.

## Deterministic verification

The updated `H3_v2_initialization_tests.py` executes sixteen static checks.
All passed in 0.389 test seconds (0.569 seconds with its subprocess wrapper),
under the assigned 600 CPU-second and 4 GiB address-space limits. The environment
was Python 3.10.12, NumPy 1.26.4, one BLAS thread.

New exact-word checks covered:

- Every code 0 through 2048, inclusive, compared with the maintained decoder's
  complete ordered expression syntax, population, rational scalar, and bounded
  type. Valid bounded new outputs had `Fraction` envelopes.
- Scaling by a 20,000-bit numerator and by its reciprocal scale, including
  exact cancellation of the envelope to `1/3`, without overflow or underflow.
- Literal deduplication, rational equivalence, immutable attributes, and invalid
  cross-population/unbounded-product/action typing.
- Two separately constructed 2,500-level shared DAGs: equality, hashes, set
  deduplication and exact exponentially growing envelope.
- A 2,200-level natural-code dependency chain decoded by the explicit stack.
- A degree-1,500 Chebyshev expression with an exact large syntax envelope and
  nonrecursive hashing, without allocating its full multivariate dictionary.

The previous ten initializer checks were rerun unchanged apart from bootstrap:
feature dimensions and nesting, independent Q/P replay, named derivatives,
Cholesky orientation, nonzero Gaussian response, Decimal/rational arithmetic,
generic-compiler integration on a small explicit fixture, constant-column
retention, and resource rejection. No trajectory was included.

Command from the repository root:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/observable_hierarchy/H3_v2_initialization_tests.py
```

Evidence:

- `data/generated/observable_hierarchy/H3_v2_route_basis/exact_words_correction_20260913/tests.log`
- `data/generated/observable_hierarchy/H3_v2_route_basis/exact_words_correction_20260913/record.json`

The record preserves the command, environment, resource limits, exit status
and all used source hashes. Principal changed-source hashes at this check:

| Source | SHA-256 |
|---|---|
| `H3_v2_words.py` | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `H3_v2_initialization.py` | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `H3_v2_initialization_tests.py` | `49333c6d33bf9ded8526c941c35b7b2b0523e4cc57b0fe6d37c2c6a0152577d2` |

This closes the identified *word-generation* numeric-range and recursion
dependencies. It does not certify all remaining arithmetic or population-weight
validation code, which the coordinator is auditing separately. The new freeze
and any promotion reviews must include this exact-word module.
