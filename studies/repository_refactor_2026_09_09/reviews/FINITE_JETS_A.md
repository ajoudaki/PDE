# Isolated adversarial audit: finite moving physical-flow jets, orders 0–3

## Verdict and required corrections

**PASS for the stated finite, real-arithmetic theorem and its explicitly limited float64 implementation. No blocking proof or implementation defect was found. Required corrections: none.**

The recurrence retains the physical residual, all three moving raw weight blocks, and the actual transpose of the moving middle matrix. Its normalization and ordinary-coefficient factorials are correct. The supplied C³ assumption suffices through order three; a fourth activation derivative is not needed. This conclusion rests on a direct mathematical and source audit, supplemented by independent exact-rational differentiation and deterministic checks, rather than on the supplied tests alone.

This verdict does not certify arbitrary extreme-range floating-point inputs, the caller's derivative callback, a positive-time approximation error, or any population claim. In particular, the implementation can reject an exactly stationary state if an evaluated backward contraction overflows, and it can lose a mathematically representable coefficient through an underflowing raw contraction. Both behaviors fall within the express numerical exclusions; concrete examples appear below.

## Isolation, read scope, and hashes

Input root: `/tmp/pde-finite-jet-isolated.HqTCyhjQ`.

Output directory: `/tmp/pde-finite-jet-audit.gsaA489l`, created by a successful invocation of `mktemp -d /tmp/pde-finite-jet-audit.XXXXXXXX`. This `REPORT.md` is the only output file created by the audit.

All eight supplied files were read in full, including the complete proof, implementation, tests, and every supplied project-local dependency. Total: **1,567 lines, 73,074 bytes**. No studies, history, other repository source, prior reviews, internet, skill files, or agent files were read. References to other documents inside the supplied documents were not followed.

SHA-256 hashes were computed before the substantive audit and recomputed after all execution and in-memory mutation checks. Every hash matched:

| Supplied relative path | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `PROOF.md` | 329 | 15,133 | `bb927e3f7a2dc75a222664a871b7caf247ebccd0fc1f31815434f6f2e3c26fb6` |
| `NOTATION.md` | 98 | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `NUMERICAL_CONTRACT.md` | 165 | 8,203 | `0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93` |
| `pde/__init__.py` | 26 | 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `pde/finite_network.py` | 363 | 15,525 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `pde/gaussian_moments.py` | 114 | 4,464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `pde/finite_jets.py` | 176 | 8,466 | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `tests/test_finite_jets.py` | 296 | 15,562 | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |

All Python execution used `PYTHONDONTWRITEBYTECODE=1`, `python -B`, and `PYTHONPATH=/tmp/pde-finite-jet-isolated.HqTCyhjQ`; the working directory was the private input root. BLAS and OpenMP thread counts were set to one. Runtime metadata: Python **3.10.12**, NumPy **1.26.4**. Imported `pde` and `pde.finite_jets` paths were checked and resolved inside the private root.

No training, initialization draws, workload/data generators, builds, installs, data-file work, or Git operations were performed. Additional checks ran from standard input; mutation checks changed source strings only in process memory. No input file was edited.

The source-review boundary includes all project-local dependencies used by the target and its tests. NumPy and the Python standard library were used as the permitted execution runtime; their implementation sources were not read or independently audited. `gaussian_moments.py` was read because the package imports it, but the target does not invoke its moment evaluator. No claim about the separate Gaussian-moment API is needed for this verdict.

## Mathematical and implementation audit

### Normalization, residual, and physical time

The model in [PROOF.md:18](/tmp/pde-finite-jet-isolated.HqTCyhjQ/PROOF.md:18) agrees with the finite conventions: `W1 @ x / sqrt(d)`, `W2 @ h1`, and `W3 @ h2 / n`. There is no hidden forward width divisor. The Gram entry is `x.T @ x / d`, so it can be zero and need not be one; its nonnegativity follows from the definition.

Independently differentiating the scalar network gives

```text
grad_W1 f = delta1 x.T / (n sqrt(d))
grad_W2 f = delta2 h1.T / n
grad_W3 f = h2 / n.
```

For `loss=(f-y)^2`, multiplication by the block mobilities `(n*kappa1, kappa2, n*kappa3)` produces exactly J3. The loss factor two and its negative sign are both retained. For one sample there is no additional averaging divisor. The corresponding consistency identity is

```text
K = (kappa1*G11/n) ||delta1||²
    + (kappa2/n²) ||delta2||² ||h1||²
    + (kappa3/n) ||h2||²
f_dot = -2 (f-y) K,       loss_dot = -4 (f-y)² K.
```

This independently checks the signs and width/input factors in both the proof and the older API used by the tests. The code applies the raw first contraction before division by `sqrt(d)` at [finite_jets.py:137](/tmp/pde-finite-jet-isolated.HqTCyhjQ/pde/finite_jets.py:137), and combines the update's scalar factors at [finite_jets.py:167](/tmp/pde-finite-jet-isolated.HqTCyhjQ/pde/finite_jets.py:167).

The label is subtracted only for residual degree zero. Positive residual degrees equal the corresponding output degrees, and participate in every next-weight update. The feature-clock calculation J11 is also correct: differentiating `s'=-2(F(s)-y)` gives the stated second and third clock derivatives, and the third output derivative has cross coefficient `-8 b² F'F''`, not a frozen-clock expression. The auxiliary `sqrt(n)*W2` coordinate change and its transformed mobility are correct and do not alter the raw forward normalization.

### Moving transpose and coefficient chronology

J4 is the ordinary-coefficient convolution rule: it has no binomial factor. J5 has the correct second- and third-order composition factors, including the full `phi'' * z1 * z2` cross term and `phi''' * z1³ / 6` term.

At [finite_jets.py:156](/tmp/pde-finite-jet-isolated.HqTCyhjQ/pde/finite_jets.py:156), `delta2[k]` includes every split of moving readout and activation-derivative degree. `propagated[k]` then includes every split of middle-weight degree and `delta2` degree with `w.T @ v`. Convolving that with the first-layer derivative yields exactly

```text
delta1[k] = sum_(a+b+c=k) phi_prime1[a] * (W2[b].T @ delta2[c]).
```

The positive-degree `W2[b].T` terms are present. The same stored middle matrix supplies the forward and reverse actions; first- and second-layer neuron indices are not identified.

The update convolutions are also complete. In particular, forming `residual_delta = residual * delta2` first and then convolving with `h1.T` retains every triple split of J8; it does not freeze any factor. The readout contraction has shape `(n,)`, as required, rather than a column-shaped parameter.

Before degree `k` is evaluated, all weights through `k` are available. The first layer is evaluated before the second, then the output, then the necessary backward fields, then the three degree-`k+1` parameter arrays. All three raw contractions are formed before any next-degree array is assigned. This is the required simultaneous physical-flow chronology, with no same-degree circularity. Future zero-initialized entries are not used by the convolutions.

The factor `1/(k+1)` converts a vector-field coefficient into the next ordinary parameter coefficient. Returned output derivatives multiply by `k!`, with no corresponding factorial multiplication applied to the stored coefficients. The code's terminal `break` occurs before residual/backward construction, so order zero evaluates only forward values and the highest backward degree is `R-1`.

### C³ regularity and local proof

The existence argument at [PROOF.md:194](/tmp/pde-finite-jet-isolated.HqTCyhjQ/PROOF.md:194) has the needed hypotheses. The finite vector field is C² because the activation is C³ and the vector field uses only the activation and its first derivative. On a closed finite-dimensional ball, both the vector field and its first derivative are bounded. Choosing a sufficiently short symmetric time interval makes the integral map preserve the ball and be a contraction on continuous curves. Its fixed point is locally unique. Bootstrapping the integral equation gives a C³ parameter trajectory, and the forward fields are C³ compositions.

The induction then extracts forward coefficients through degree three, but the vector field only through degree two. The largest derivative needed when composing `phi'` is therefore `phi'''`; neither the theorem nor the implementation needs `phi''''`. Differentiating a generic little-o remainder is unnecessary: the actual C³ trajectory and its C² derivative have their own Taylor expansions.

The proof correctly claims a Peano remainder `o(|t|^R)`, and expressly declines a generally stronger `O(|t|^(R+1))` remainder, infinite Taylor convergence, a width-uniform estimate, or a positive-time error bound. For editorial precision only, the explanation of J5 at lines 100–108 could explicitly say to use the order-`q` Taylor formula when `q<3`; the displayed cubic argument and its lower-order versions are mathematically standard and do not create a substantive proof gap.

A separate runtime check used `phi(z)=z+|z|^(7/2)` at zero preactivation in both layers. It is C³ and not C⁴ there. With `n=d=1`, weights `(0,1,1)`, input one and label one, the initial first-weight velocity is two. Every returned coefficient through degree three agreed with the identity-activation jet, as required by their identical derivatives through order three at zero. Thus the check is not restricted to a stationary trajectory or analytic activation.

### Zero residual and zero input

In real arithmetic, residual zero makes J3 identically zero at the state. Local uniqueness makes the physical solution constant. In the recurrence, zero residual degree zero gives zero degree-one weights; induction then gives zero positive forward, residual, and weight coefficients. There is no residual division or singular clock inversion.

Input zero forces all positive-order first-weight and first-preactivation coefficients to vanish. It need not freeze the rest of the network when `phi(0)` is nonzero. Both behaviors are exercised by the supplied suite. The numerical qualification for an overflowing backward field at zero residual is documented separately below.

### Validation, shapes, and ownership

The new API explicitly restricts depth to two and samples to one. `Parameters.validate()` rechecks mutable parameter arrays. Input shape `(d,1)`, label shape `(1,)`, and positive finite multipliers of shape `(3,)` are enforced. Order accepts integral values 0–3, including NumPy integers, but rejects booleans, floats and other out-of-range/type values. Callback return arrays must have the exact input shape; scalar broadcasting is rejected even for width one. The common `_array` helper accepts supported real numeric array dtypes, casts to float64 and rejects nonfinite values; it does not accept complex or boolean-typed arrays.

The implementation requests exactly derivative orders `0,...,R` at each initial preactivation. It cannot verify that these are derivatives of a single coordinatewise C³ function. Consistency and the prohibition on callbacks mutating unrelated calculation state are explicit caller obligations, not unimplemented validator promises.

The input, label and multiplier arrays are copied, and supplied parameters are copied into newly allocated coefficient storage before callbacks run. The used `_evaluate` helper at [finite_network.py:194](/tmp/pde-finite-jet-isolated.HqTCyhjQ/pde/finite_network.py:194) copies each callback argument and then copies its result immediately. In-place callbacks and reusable result buffers therefore cannot corrupt cached initial coordinates or earlier derivative values.

Parameter coefficients are views into new internal per-block storage. Different degree slices have disjoint elements; they may share a base allocation. This is compatible with the stated ownership contract and does not alias supplied parameters. Preactivation, hidden and output arrays are separately allocated. `output_derivatives` allocates a fresh finite array. The frozen dataclass does not promise deep immutability; its arrays are intentionally mutable.

Additional checks with read-only, negatively strided parameter/input views succeeded. All returned arrays were writable, did not overlap any supplied input array, and had no pairwise element overlap. Distinct nontrivial permutations of both hidden layers at width three preserved output coefficients and correctly permuted every returned parameter and forward-field coefficient.

## Floating-point boundary: verified behavior, not defects

The mantissa/exponent helper was fully read. For the small fixed number of finite factors used here, it prevents premature exponent-range loss while combining mobility, loss, normalization and degree factors. It does not recover information already lost inside an unscaled product or sum. `_array` checks evaluated compositions, contractions, residuals and parameter coefficients for finiteness. Output derivative conversion rejects overflow when the property is requested, without imposing that requirement during `flow_jet` construction.

The implementation intentionally does not compute a loss square, a terminal backward field, or an order-zero-only residual. Deterministic checks confirmed:

| Case | Result |
| --- | --- |
| Identity activation, scalar weights `(1,1,2^1023)`, input `1`, label `-2^1023`, `R=0` | Succeeds with output `2^1023`; the unrepresentable unused residual is not formed. |
| Identity activation, scalar weights `(0,1,1)`, input `0`, label `10^200`, `R=3` | Succeeds with zero positive coefficients; the unrepresentable loss square is not formed. |
| Identity activation, scalar weights `(2^-1023,0,2^1023)`, input `1`, label `1` | `R=1` succeeds, with output coefficient one equal to `2`. `R=2` rejects the now-required overflowing moving-transpose contraction. |

Two adversarial examples show why the exclusions in [PROOF.md:311](/tmp/pde-finite-jet-isolated.HqTCyhjQ/PROOF.md:311) and [finite_jets.py:94](/tmp/pde-finite-jet-isolated.HqTCyhjQ/pde/finite_jets.py:94) matter:

1. **An exactly zero residual does not guarantee numerical success.** For identity activation, scalar weights `(2^-1023,2,2^1023)`, input `1`, label `2`, and `R=1`, the output and residual are exactly `2` and `0`. However, the evaluated backward field is `delta1=2^1024`, so the API raises `ValueError: jet contraction must be finite`. The real trajectory is constant. This does not contradict the real-arithmetic theorem or the express allowance for raw-contraction overflow; the code makes no unconditional extreme-range stationary-state guarantee.

2. **A representable final coefficient can be lost before scaling.** For identity activation, scalar weights `(0,1,2^-600)`, input `1`, label `-2^-600`, multipliers `(2^1000,1,1)`, and `R=1`, the exact first-weight coefficient is `-2^-199`, approximately `-1.2446030555722283e-60`. The raw product `residual*delta1=2^-1200` underflows first, so the returned first-weight coefficient is zero. The documented exclusions explicitly cover this raw-product underflow. Scaled scalar factors cannot repair it afterward.

Neither example justifies a required correction under the current contract. They would become implementation defects if a future contract promised success whenever only the returned coefficients are representable, or guaranteed exact zero jets at all finite stationary states regardless of intermediate ranges. No such stronger claim should be inferred from this audit.

## Independent checks and their evidence

### Supplied suite

Command, run from the private root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde-finite-jet-isolated.HqTCyhjQ OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s tests -p test_finite_jets.py -v
```

Result: **14 tests passed**, with unittest reporting 0.079 seconds. The test source was read in full before execution. No other suite was run or relied upon.

### Exact-rational differentiation of the scalar loss

A separate, in-memory reference calculation differentiated the network's scalar loss directly with respect to its 14 raw coordinates. It did not call the old forward/velocity/kernel implementations or reuse `finite_jets` composition, convolution, or backward routines to obtain expected values.

The fixed setup was `n=2`, `d=4`, so `sqrt(d)=2`, with

```text
W1 = [[ 1/4, -1/8, 3/8,  1/2],
      [-1/2,  1/4, 1/8, -3/8]]
W2 = [[3/8, -1/2], [7/8, 1/4]]
W3 = scale * [3/4, -1/2]
x  = [1/2, -3/4, 1/4, 5/4]^T
kappas = [1/2, 3/2, 5/4]
phi(z) = 1/4 + z + z²/4 + z³/8
G11 = 39/64.
```

The two `(scale,label)` pairs were `(1,3/8)` and `(1/32,-1/4)`, covering both residual signs and a smaller readout. All scalar algebra for expected values used `fractions.Fraction` until the final comparison.

Method: represent local multivariate polynomials in the 14 coordinate perturbations through total degree three, using exact rational coefficients. Evaluate each forward field and the scalar loss in that algebra. Differentiate the loss polynomial coordinatewise and apply diagonal mobility `(1 repeated 8 times, 3/2 repeated 4 times, 5/2 repeated 2 times)` to obtain the vector-field polynomial through degree two. Then compute

```text
v = V(theta0)
a = DV(theta0) v
j = D²V(theta0)[v,v] + DV(theta0) a.
```

Expected parameter coefficients are `(theta0,v,a/2,j/6)`. Substituting `v*t+a*t²/2+j*t³/6` into each independent local field polynomial gives its expected time coefficients. Truncating the loss at degree three is sufficient because the vector field is needed only through degree two.

This compared **184 scalar entries**: four degrees of 14 parameter coordinates plus nine forward/output coordinates, for each of two fixed states. All comparisons passed at `rtol=3e-13`, `atol=3e-14`.

| Readout scale | Maximum absolute parameter error | Maximum absolute forward/output error |
| --- | ---: | ---: |
| `1` | `8.881784197001252e-16` | `1.7763568394002505e-15` |
| `1/32` | `5.551115123125783e-17` | `1.1102230246251565e-16` |

Exact-reference output coefficients, rounded to float64:

```text
scale 1:    [-0.012534389358101711, 1.054033700286816,
             -1.8432047658561659, 4.4924440987562]
scale 1/32: [-0.0003916996674406785, -0.47447115612629087,
              0.446588470397978, -0.46419106695889223]
```

These are pointwise deterministic checks, not a proof over all states. Their independence specifically reduces the possibility of a shared normalization or backward-recurrence error in the two library implementations.

### Supplied-test independence and coverage

The suite contains useful checks with different strengths:

| Test group and source lines | Independence and coverage |
| --- | --- |
| Raw API and first derivative, 53–72 | Checks normalization, shape and first derivative against the existing forward, velocity and kernel APIs. Independent of the new recurrence, but shares the finite API, callback evaluation, scaling and validation helpers. |
| Identity and cubic scalar hand solutions, 74–103 | Strong analytical references for moving coefficients and factorials through degree three; cubic activates all requested activation derivatives. Scalar width and equal-weight trajectories alone cannot settle general transpose orientation or width normalization. |
| Constant activation, 105–115 | Independent exponential-residual solution detects the changing physical clock with nonunit readout mobility. Hidden motion vanishes here, so it does not test moving-transpose coupling. |
| Acceleration and jerk, 117–134 | Differences of the old RHS check `DV V` and `D²V[V,V]+DV(DV V)` at a nonsymmetric width-two state with nonunit rates. Valuable independent chronology check, subject to finite-difference error and shared old-RHS assumptions. |
| Forward fields on parameter polynomial, 136–150 | Checks composition and reported forward fields against old forward evaluations. Because it uses the new oracle's own parameter polynomial, this test alone cannot validate that polynomial as the true moving flow. |
| First-layer relabeling, 152–163 | Checks a separate permutation of the first layer and corresponding middle columns. It does not explicitly test a separate second-layer/readout permutation. |
| Zero residual/input, 165–176 | Checks equilibrium, vanishing first-layer motion at zero input, and surviving readout motion. Uses moderate magnitudes. |
| Contract tests, 180–292 | Covers order prefixes and requested derivative orders, callback ownership, invalid scope/types/shapes, mutable-state revalidation, rejected nonfinite values, derivative conversion overflow, and selected extreme scaling cases. |

The callback-invalidity loop at lines 254–265 injects a bad return at each derivative index while calling the default order-three oracle. Its loop variable does not select the API truncation order. This is still useful coverage, but should not be described as a full invalid-callback-by-truncation-order matrix. Likewise, the narrative about broader tests in `NUMERICAL_CONTRACT.md` is not evidence that those other, unsupplied tests were inspected or passed here.

### In-memory mutation sensitivity

To probe whether the supplied tests actually distinguish the principal failure modes, eleven single-change versions of `finite_jets.py` were compiled and exercised in process memory against the unchanged supplied suite. No modified source was written to disk. Every mutation was detected:

| Deliberate defect | Number of test methods detecting it |
| --- | ---: |
| Omit first forward input normalization | 5 |
| Add an extra hidden forward width factor | 4 |
| Omit middle update width normalization | 2 |
| Replace loss factor `-2` with `-1` | 6 |
| Omit the degree divisor | 4 |
| Freeze positive residual coefficients to zero | 4 |
| Subtract the label at every degree | 3 |
| Freeze the middle matrix in backward propagation | 3 |
| Replace the transpose by the forward orientation | 3 |
| Force a straight parameter trajectory after degree one | 4 |
| Halve the cubic composition cross term | 2 |

Detection counts include assertion failures or errors from the changed module. They demonstrate sensitivity to these selected changes, not exhaustive mutant coverage or independence from shared dependencies.

## Nonblocking recommendations

No correction is required to J1–J11, the recurrence, or the stated finite numerical contract on the evidence of this audit. For a stronger permanent regression suite, retain small versions of the checks added here:

- An exact scalar-loss differentiation reference at a nonsymmetric, nonunit-Gram state with unequal mobilities, including both residual signs and a small readout.
- A C³-but-not-C⁴ activation at a moving initial state.
- Separate second-layer/readout relabeling, alongside the existing first-layer permutation check.
- Explicit read-only/noncontiguous inputs and ownership checks for all returned arrays.
- Cases proving that unused residual, loss and terminal backward quantities are skipped, together with clearly labeled tests of the admitted raw underflow/overflow limitations.

These are coverage improvements, not evidence of an outstanding mathematical or code defect. The contained theorem remains a local finite physical-gradient-flow Taylor result through order three, with exactly the claim boundaries stated in the supplied proof.
