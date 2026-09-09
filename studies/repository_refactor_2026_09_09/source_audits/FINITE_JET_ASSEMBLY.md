# Bounded finite MFP promotion: worker report

Workspace: `/home/amir/Codes/PDE`.
Date: 2026-09-09. Status: implemented and unit-tested; independent proof/code
verification remains with the main task. This is not a final verifier report.

## Delivered files

The entire repository write set is these two new files (both were absent
before implementation):

- `/home/amir/Codes/PDE/code/pde/finite_jets.py` — 176 lines.
- `/home/amir/Codes/PDE/code/tests/test_finite_jets.py` — 296 lines.

Additional deliverables in a newly created private directory (mode 0700):

- `/tmp/pde-mfp-promotion-4cjxieUb/PROOF.md` — 329 lines.
- `/tmp/pde-mfp-promotion-4cjxieUb/REPORT.md` — this report.

Every file creation/edit above used `apply_patch`. Existing code, package
exports, and guides were not edited. No Git commands, subagents, training
experiments, old coefficient generators, installs/builds, data outputs,
seals, or budgets were used. The donor and its tests were read, not executed.
The old finite-network and numerical-contract unit tests were executed as
authorized deterministic compatibility checks.

## Implemented scope and donor adaptation

`from pde.finite_jets import flow_jet` is the import path; no change to
`pde/__init__.py` is needed. The signature is

```python
flow_jet(parameters, inputs, labels, activation_derivative, *, order=3, kappas=None)
```

It accepts the existing `Parameters`, exactly two hidden layers, one input
sample of shape `(d,1)`, one label of shape `(1,)`, one shared scalar C3
activation derivative callback, and the finite API's positive three-block
mobility multipliers. Orders zero through three are supported. Inputs can be
unnormalized or zero; weights and readout can be arbitrary finite states.

The returned `FlowJet` contains all raw parameter coefficients, layer-indexed
preactivation/activation coefficients, output coefficients, and a checked
factorial conversion to physical output derivatives. Coefficients are ordinary
Taylor coefficients, with the sample axis retained. Middle entries `[i,j]`
map layer-one neuron `j` to layer-two neuron `i`.

The donor supplies the bounded composition formulas, coefficient convolution,
and chronological moving feature-flow recurrence. It stores an unscaled
Gaussian hidden matrix, inserts `1/sqrt(n)` in each action, scalarizes the
first weights to a preactivation with metric `q0`, and draws order-one stored
readout entries. The promotion instead takes a caller-supplied finite state
in current raw storage. The exact translation is:

- `W^(2)_current = W_donor / sqrt(n)`; hidden forward actions in the new API
  have no extra width factor, and hidden weight velocity carries `1/n`.
- `z^(1) = W^(1) x / sqrt(d)`; the scalarized first-coordinate metric is
  `G_11 = x.T @ x / d`, derived from the raw first matrix rather than supplied
  as an extra independent parameter.
- Stored readout values are accepted unchanged, with `f = readout @ h2 / n`.
  The donor's order-one readout initialization is not silently equated with
  the maintained initialization's `N(0,1/n^2)` stored readout law.
- Physical time is implemented directly with mean squared loss, residual
  `f-y`, and mobilities `(n*kappa1, kappa2, n*kappa3)`. Every required residual
  coefficient participates in the convolution before a weight coefficient
  is created. This is an elementary extension from the donor's feature clock,
  derived in the proof from the existing finite physical-flow equations.
- The same moving middle weight series is transposed in the backward sweep.
  Positive-degree matrix, readout, first-weight, and residual terms are kept.

No feature-time option, generic observable compiler, batch/depth abstraction,
population replacement, sampling harness, or new dependency was introduced.

## Callback and numerical contract

The callback is `activation_derivative(j,z)`, representing the actual j-th
scalar derivative coordinatewise. Only orders `0..order` are requested,
once per derivative per layer, at initial preactivations of shape `(n,1)`.
There is no terminal vector-field evaluation requiring derivative order four.

Inputs are copied before callback use; each callback argument is a private
preactivation copy; each callback result is validated and immediately copied.
In-place callbacks and a single reusable output buffer across derivatives
and layers are supported. Return shapes, real numeric types, and finiteness
are checked without scalar broadcasting. Parameter arrays are revalidated
at entry; all returned arrays are independent of user inputs/callback buffers.
Result arrays remain mutable, as in the current finite API.

The implementation reuses the existing private numerical helpers `_array`,
`_evaluate`, `_labels`, `_kappas`, and `_scaled_product`. Callback derivative
truth, C3 regularity, coordinatewise behavior, and absence of unrelated
external-state mutation remain caller obligations. This is consistent with
the existing callback contract, strengthened to the derivative order needed.

The first raw matrix contraction precedes input normalization. Scalar
mobility, normalization, and recurrence-degree factors use the existing
mantissa/exponent multiplication. Raw contractions, sums, and composition
powers are still float64. Nonfinite evaluated coefficients, including
unrepresentable requested output derivatives, raise `ValueError`.
No exact-arithmetic or correct-rounding claim is made.

## Proof contents

`PROOF.md` is self-contained mathematical insertion material with canonical
layer-indexed weights, finite lower-case hidden fields, residual `r_1=f-y`,
physical `t`, feature `s`, and explicit neuron indices. It contains:

1. Full finite network, backward fields, raw learning metric, and physical RHS.
2. Elementary bilinear coefficient and activation-composition identities.
3. The complete forward/backward/parameter recurrence and degree chronology.
4. Local C3 flow construction by elementary integral iteration, followed by
   the induction proving the recurrence equals actual moving-flow coefficients.
5. The raw-coordinate/feature-clock translation, zero-residual case, and
   explicit physical-time chain-rule formulas through order three.
6. Interface shapes, ownership and arithmetic conditions, complexity, and
   the boundary between local finite coefficients and population/time claims.

No specialized theorem is invoked. The proof contains no references to
study files or temporary locations. The solve-math-rigorously skill at
`/etc/codex/skills/solve-math-rigorously/SKILL.md` was read fully and used to
structure the elementary proof and state its precise claim boundary. It did
not introduce a permission gate or an independent-verifier claim.

## Read coverage

The four explicitly requested files were read completely before implementation:

| File relative to workspace | Coverage |
| --- | --- |
| `docs/NOTATION.md` | Full, lines 1–98 |
| `code/README.md` | Full, lines 1–165 |
| `code/pde/finite_network.py` | Full, lines 1–363 |
| `studies/mfp_gaussian_calculus/compiler/finite_width_jet.py` | Full, lines 1–152 |

Additional targeted reading:

| File relative to workspace | Coverage / purpose |
| --- | --- |
| `studies/mfp_gaussian_calculus/compiler/README.md` | Full, 1–131; donor model, clock, normalization, derivative cap |
| `studies/mfp_gaussian_calculus/PROOF_CONTRACT.md` | Full, 1–177; frozen model and separation from population claims |
| `studies/mfp_gaussian_calculus/PEELING_AND_PROBABILITY_LEDGER.md` | 1–245 of 706; finite transpose and moving-backward identities through (3.10), plus start of theorem map; no theorem invoked |
| `studies/mfp_gaussian_calculus/README.md` | Full, 1–310; overview and claim boundaries; not relied on for population conclusions |
| `studies/mfp_gaussian_calculus/compiler/test_finite_width_jet.py` | Full, 1–66; existing donor checks inspected but not run |
| `docs/finite_dynamics.md` | Full, 1–214; raw physical RHS, normalization, finite-flow context |
| `docs/gaussian_calculus.md` | 1–252 and 1739–1812, plus heading/keyword navigation; finite moving derivatives and finite-order scope; fixed-program population proof not read in full |
| `code/pde/__init__.py` | Full, 1–26; current imports, left unchanged |
| `code/tests/test_finite_network.py` | Full, 1–297; testing conventions and normalization |
| `code/tests/test_numerical_contract.py` | Full, 1–202; callback ownership and float64 contract |
| `code/tests/test_library_boundary.py` | Full, 1–58; inspected only, not executed |

Ancestor and scoped `AGENTS.md` discovery found no instruction files.
Early broad file/keyword searches included truncated navigation output;
the explicit reads/ranges above, not those broad results, establish coverage.
The new implementation, tests, and complete proof were also inspected during
construction. Nothing in this report asserts a read or audit of all research
artifacts linked from an overview.

## Exact source hashes

SHA-256 of the exact source files used. Hashes of partially read files identify
the whole source file; they do not enlarge the read coverage stated above.

```text
9b9fdeccb502948e8ee66347e90ff9433b26bb76b5e0d9c3f3e222e5f328616e  studies/mfp_gaussian_calculus/compiler/finite_width_jet.py
00dac0b528fb933fb466ed3e4bbaab55db4e1843023c296c774c1542da0ac101  studies/mfp_gaussian_calculus/compiler/README.md
948addc4ce4215510b2a70694aa8877d22b79739aee6906551fdb7b47b944860  studies/mfp_gaussian_calculus/PROOF_CONTRACT.md
b76d6169146f4100dc6adab08e09f1a34bee9dac442804f15eab74e3cc46da2e  studies/mfp_gaussian_calculus/PEELING_AND_PROBABILITY_LEDGER.md
6c6b81a3f7657eb7a7a01e61681d534799ec0ddbc7124466e14f2fdb9da22e25  studies/mfp_gaussian_calculus/README.md
02dabe39a44b2af62a4f86394c01f30abf4bdad113d01db332a4a21a24d2b666  studies/mfp_gaussian_calculus/compiler/test_finite_width_jet.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
```

Delivered implementation/proof SHA-256:

```text
1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2  code/pde/finite_jets.py
991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a  code/tests/test_finite_jets.py
bb927e3f7a2dc75a222664a871b7caf247ebccd0fc1f31815434f6f2e3c26fb6  /tmp/pde-mfp-promotion-4cjxieUb/PROOF.md
```

## Tests performed

Environment: Python 3.10.12, NumPy 1.26.4, one OpenBLAS/OMP thread, bytecode
writing disabled. Both commands were run from `/home/amir/Codes/PDE`.

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_finite_jets.py' -v
```

Result: 14 tests passed, 0 failures/errors, reported runtime 0.090 s.

```sh
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest test_finite_network test_numerical_contract -v
```

Result: 36 existing tests passed, 0 failures/errors, reported runtime 0.138 s.
Total: 50 passing tests. No failing implementation test preceded these runs;
there were no test-driven code revisions or repeated runs after success.
One mathematical typesetting typo and a regularity/complexity wording
clarification in the proof were corrected before the recorded proof hash.

The new tests cover raw forward/velocity/kernel agreement, every returned
shape, parameter factorial conventions, two independent hand-solvable moving
flows, changing residuals for a constant activation, second/third parameter
derivatives by central differences of the existing physical RHS, forward
fields along the parameter polynomial, independent first-layer neuron
relabeling, zero residual, zero input, truncation prefixes, derivative demand,
callback aliasing, invalid scope/arguments/callbacks, nonfinite contractions,
factorial overflow rejection, and selected subnormal/large-scaling cases.

The scalar identity control has all weights `c=(1+8t)^(-1/4)`, with output
coefficients `[1,-6,42,-308]`; freezing the initial direction would give
`[1,-6,12,-8]`. The scalar cubic control uses mobilities `(1/9,1/3,1)`,
all weights `c=(1+48t)^(-1/24)`, and output `c^13`, exercising activation
derivatives through three. Its expected coefficients are formed directly
from the four-term binomial formula using `Fraction`, then compared to the
float64 recurrence. This rational test expectation does not make the oracle
an exact-arithmetic implementation.

At the nonsymmetric two-neuron state with four input coordinates, the
parameter acceleration check uses tolerance `rtol=3e-6, atol=2e-8`, and the
jerk check `rtol=8e-6, atol=2e-7`, with displacement `2e-4`. Forward-field
third differences use displacement `4e-4` and `rtol=8e-5, atol=5e-6`.
These are bounded deterministic finite-difference checks, not trajectory
integration or training experiments. No donor population regression panel
or old reference coefficient generator was imported/executed.

## Uncovered limitations and handoff

- Only one sample, exactly two hidden layers, and a shared C3 activation are
  exposed. Layer-dependent activations, multiple samples, higher orders,
  nonsmooth activations, and other observables are outside this promotion.
- There is no built-in higher-derivative activation catalog. Callers provide
  the derivative oracle; consistency/regularity is not numerically verified.
- Backward coefficients are internal and only computed through order minus
  one. The result does not pretend to expose a full third-order backward jet.
- Results are mutable and are not globally revalidated after caller edits.
  The output-derivative property checks the values it evaluates. Returned
  parameter slices share internal backing allocations across disjoint degree
  ranges but do not alias user parameters or each other elementwise.
- The scaled helper protects scalar factors, not arbitrary raw products or
  high-order composition powers. Intermediate range loss can cause rejection
  even when a rearranged exact expression would be finite, or underflow can
  silently lose tiny coefficients. Finite-difference tolerances are not
  universal forward-error bounds. Extreme-range coverage is selective.
- Exact donor-to-current coordinate translation is proved algebraically;
  no seedwise donor execution was used as a gate, respecting the ban on old
  coefficient-generator execution. No population law or expectation target
  is certified by these tests.
- The maintained module deliberately depends on existing private finite API
  validation/scaling helpers to preserve its numerical contract. Changes to
  those helpers should include this module in future compatibility checks.
- No source guide or package export was modified. The proof is ready for
  review as standalone insertion material; integration into a chapter and
  fresh isolated proof/code audits are the main task's subsequent work.

No known recurrence defect remains from the worker checks. Independent
verification has not been claimed or substituted with these tests.
