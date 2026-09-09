# Independent isolated proof-and-code audit

## Verdict: CLEAN

No required mathematical or implementation correction was found for the stated result: two hidden layers, one sample, arbitrary positive finite dimensions, arbitrary finite real initial state and input, fixed positive multipliers, and one shared scalar C3 activation, with ordinary moving physical gradient-flow coefficients through orders 0–3.

This verdict uses the actual numerical claim in PROOF.md, lines 311–321: float64 evaluation can reject a calculation because an intermediate raw product or composition power overflows, even when the exact coefficients are finite. It is not a guarantee that every finite real state has an evaluable float64 jet. Two explicit examples of this boundary are recorded below. They are disclosed limitations, not contradictions of the stated contract.

The correctness conclusion rests on the mathematical derivation and complete implementation inspection. Passing tests supply corroboration, not a proof.

## Isolation, read coverage, and input identity

Audited input root: `/tmp/pde-finite-jet-isolated.HqTCyhjQ`.

All task-source and document reads were confined to the following eight files. Each was read completely, including the numerical contract's sections outside the jet API and all functions in both local dependency modules. A combined display was truncated; the affected dependency/implementation text and final finite-network lines were reread to completion. All line references below are relative to this input root.

| File | Complete line coverage | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `PROOF.md` | 1–329 | 15133 | `bb927e3f7a2dc75a222664a871b7caf247ebccd0fc1f31815434f6f2e3c26fb6` |
| `NOTATION.md` | 1–98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `NUMERICAL_CONTRACT.md` | 1–165 | 8203 | `0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93` |
| `pde/__init__.py` | 1–26 | 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `pde/finite_network.py` | 1–363 | 15525 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `pde/gaussian_moments.py` | 1–114 | 4464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `pde/finite_jets.py` | 1–176 | 8466 | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `tests/test_finite_jets.py` | 1–296 | 15562 | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |

Total: 1567 lines, 73074 bytes. All eight hashes were checked again after the executions and matched exactly.

Local dependency closure: `finite_jets.py` imports `Parameters`, `_array`, `_evaluate`, `_kappas`, `_labels`, and `_scaled_product` from `finite_network.py`. Package initialization also imports `gaussian_moments.py`. The supplied tests additionally use the finite forward, velocity, and kernel APIs. Every one of these local modules was read in full. The Gaussian routines are not called by the jet computation; their import introduces no numerical work or dependency on a Gaussian assumption.

Python's standard library and NumPy were used as the permitted execution runtime, not separately source-audited. No outside project sources, studies, history, repository audits, Internet sources, skill files, other agents, or linked documents were consulted. No training, initialization/sampling, generators, builds, installs, Git operations, or data-file operations were run. No input files were edited. Checks ran through standard input or the supplied test file, with bytecode writing disabled. The sole authored file is this report, created using `apply_patch` inside the genuine directory returned by `mktemp -d /tmp/pde-finite-jet-audit.XXXXXXXX`.

## Mathematical obligations

### 1. Network normalization, gradients, and physical mobility

Equations J1–J3 agree with NOTATION.md and the finite numerical contract. In particular, the middle forward matrix acts without an extra width factor. With first-layer index j and second-layer index i,

\[
\delta_i^{(2)}=W_i^{(3)}\phi'(z_i^{(2)}),\qquad
\delta_j^{(1)}=\phi'(z_j^{(1)})\sum_i W_{ij}^{(2)}\delta_i^{(2)}.
\]

Direct differentiation gives

\[
\nabla_{W^{(1)}}f=\frac{\delta^{(1)}x^T}{n\sqrt d},\quad
\nabla_{W^{(2)}}f=\frac{\delta^{(2)}(h^{(1)})^T}{n},\quad
\nabla_{W^{(3)}}f=\frac{h^{(2)}}n.
\]

Multiplication by the gradient of the unhalved loss, `2(f-y)`, and mobilities `(n*kappa1, kappa2, n*kappa3)` yields exactly J3. There is no omitted sample factor because m=1. The backward fields are residual-free.

The input only enters through the raw first matrix and `x/sqrt(d)`. Its Gram entry is `x^T x/d >= 0`; the phrase “need not be ... positive” allows zero, not negative Gram entries. No normalization, inversion, or nondegeneracy hypothesis is used. Consequently the proof includes x=0 and arbitrary nonunit input norm.

Evidence: PROOF.md, J1–J3 and lines 176–192; NOTATION.md, lines 8–42 and 78–81; `finite_network.py`, lines 202–214, 227–238, 276–314.

### 2. Local existence, uniqueness, and exactly sufficient regularity

As a function of the finite raw parameter vector, f is C3. Therefore

\[
V(\theta)=-2(f(\theta)-y)D\nabla f(\theta)
\]

is C2, for a fixed positive block-diagonal D. On a closed ball about any initial state, V and DV are bounded by compactness. The integral map on continuous curves in that ball maps the ball of curves into itself for sufficiently small two-sided time radius and is a contraction when `a*M < 1`. The geometric-series argument in the proof establishes convergence, the integral equation, and local uniqueness. This does not need any probabilistic or global boundedness assumption.

The integral equation first makes theta C1. Since V is C2, differentiating its composition with theta twice makes theta C3. Explicitly,

\[
\theta'=V,\qquad \theta''=DV\,V,\qquad
\theta'''=D^2V[V,V]+DV(DV\,V).
\]

Every forward field is C3, while the residual-free backward fields need only be C2. Thus phi''' suffices. Neither the existence argument nor the third coefficient requires phi''''. A C3 Taylor expansion yields `o(|t|^3)` at order three; a fourth-order bound or infinite analytic series does not follow.

Evidence: PROOF.md, lines 194–211 and 231–238; `finite_jets.py`, lines 125–128, 141–155. A non-C4 activation was also exercised below.

### 3. Coefficient algebra and induction

J4 is the ordinary-coefficient Cauchy product for any fixed finite-dimensional bilinear operation. Bounded retained polynomials multiply Peano remainders without changing their required order, including the continuous degree-zero case. Transposition is linear, so the coefficient of a transpose is the transpose of the same coefficient.

For composition, expand `e=z-z0`. Through degree three, the contributions from e² are `z1²` and `2*z1*z2`, and the degree-three contribution from e³ is `z1³`. This gives J5 with the factors 1/2 and 1/6 as written. For a function with only q derivatives, use its order-q Taylor expansion; the lower-degree statements do not assume a third derivative of that function. In particular phi' is only used through degree two.

Before degree k's forward sweep, the raw weight coefficients through k exist. J6 successively constructs the first preactivation, first activation, second preactivation, second activation, and output. If k<R, the residual and backward coefficients through k are then available. Equating the degree-k coefficient of the vector field with `(k+1)*W[k+1]` gives J8. This closes the induction without any same-degree circular dependency. For R=0, the computation stops at the network value.

Evidence: PROOF.md, J4–J8 and lines 213–233; `finite_jets.py`, lines 51–69 and 134–172.

### 4. Product splits and the reused moving transpose

The implementation's propagated coefficient is

\[
P_k=\sum_{b+c=k}(W_b^{(2)})^T\delta_c^{(2)}.
\]

Its next convolution gives

\[
\delta_k^{(1)}=\sum_{a+b+c=k}\mathcal C_a(\phi',z^{(1)})\odot
(W_b^{(2)})^T\delta_c^{(2)},
\]

exactly J7/J9, including every b>0 trained-matrix term. `middle` is the same array used in the forward pass; the reverse product explicitly uses `w.T`. Independent neuron populations are not identified.

Similarly, `residual_delta[k]` first computes the coefficients of `r*delta2`; its convolution with h1 expands to every triple `(a,b,c)` in the middle update. The first update uses the coefficients of `r*delta1` followed by the fixed outer product with x. The readout update contracts `(n,1)` hidden coefficients with `(1,)` residual coefficients, obtaining the required `(n,)` result. All sums are complete and use ordinary coefficients, with no missing multinomial factors.

Evidence: `finite_jets.py`, lines 64–69, 140, 148, and 156–170; PROOF.md, J7–J9. This is an algebraic check for arbitrary finite n and d, not an inference from the width-two test.

### 5. Moving residual and the feature clock

The code subtracts y only at degree zero and retains `r[k]=f[k]` thereafter. These higher residual coefficients enter every subsequent weight update, so the computed curve is the moving physical flow.

For the separately defined feature ascent, set `A=D*grad(f)`, `F(s)=f(theta(s))`, and `b=-2*r(0)`. Differentiating `s'=-2(F(s)-y)` gives `s''=-2*b*F'` and `s'''=-2*b²*F''+4*b*(F')²`. Consequently,

\[
f_t'=bF',\qquad
f_t''=b^2F''-2b(F')^2,\qquad
f_t'''=b^3F'''-8b^2F'F''+4b(F')^3.
\]

The coefficients in J11 are correct, including the factor 8. Merely multiplying the kth feature derivative by b^k would omit terms. A negative b reverses the local feature parameter; the proof restricts its assertion about an increasing clock to positive clock speed. At zero residual, local uniqueness gives the constant real-arithmetic physical solution without dividing by the residual.

The first feature coordinate satisfies `dz1/ds=kappa1*(x^T x/d)*delta1`. Under `What2=sqrt(n)*W2`, the middle equation and the unit-multiplier mobility transformation in the proof also have the stated factors.

Evidence: PROOF.md, lines 240–288; `finite_jets.py`, lines 150–170. The constant-activation and equal-weight hand solutions in the supplied tests distinguish residual motion and weight acceleration from a frozen direction.

## Implementation and numerical contract

| Obligation | Evidence and assessment |
| --- | --- |
| Valid L=2, m=1, positive n,d, finite mutable parameters | `finite_jets.py:100–117`; `finite_network.py:111–144`. Parameters are revalidated before evaluation. |
| Integer order 0–3, excluding booleans; positive finite three-entry kappas | `finite_jets.py:105–116`; `finite_network.py:254–258`. Correct. |
| Shared coordinatewise derivative callback | A single callable is used for both layers, `finite_jets.py:141–146`. Shape/type/finiteness are checked; actual derivative consistency and scalar C3 semantics necessarily remain caller obligations. |
| No fourth derivative or terminal backward evaluation | Backward arrays have length R, and `k==order` breaks before residual/backward construction, `finite_jets.py:125–128,150–155`. For R=3, shifted composition reaches derivative index 3, not 4. |
| Callback argument and result ownership | `finite_network.py:194–199` calls on `z.copy()` and immediately copies the checked return value. Derivative tuples therefore survive both in-place callbacks and shared output buffers. |
| Input/result ownership | Inputs, labels, and rates are copied at `finite_jets.py:114–116`; raw state values are assigned into freshly allocated coefficient arrays at lines 118–122. Returned parameter slices share their private backing storage, not caller inputs. This does not contradict the documented ownership claim. |
| Ordinary coefficients and output derivatives | Raw updates divide by k+1 at lines 169–170. `output_derivatives`, lines 43–48, returns a newly allocated factorial-scaled finite array and rejects unrepresentable conversion. |
| Normalization and scaling | First raw matrix contraction precedes division by sqrt(d), line 137. Rate, normalization, degree, and loss factor -2 are combined by `_scaled_product`, line 170; helper at `finite_network.py:31–54`. The bounded factor count keeps nonzero mantissa products away from exponent-range failure until magnitude restoration. Rounding remains ordinary float64 rounding. |
| Nonfinite results | `_array` rejects nonfinite checked arrays; compositions, convolutions, parameters, and outputs are checked. The errstate block suppresses warnings, not validation. |
| Computational claim | With fixed R<=3, there are only a bounded number of coefficient splits and matrix actions. Storage and algebraic work are O(nd+n²), excluding callback costs, as claimed. |

The general finite-network helpers used as test comparators were also checked: forward normalization, transpose-based backward fields, residual contractions, mobility factors, and one-sample kernel identity agree with J1–J3. No jet computation invokes Gaussian moments, initialization, GD, or a loss evaluation.

## Deterministic execution evidence

Every Python invocation used `PYTHONDONTWRITEBYTECODE=1`, `python -B`, `PYTHONPATH=/tmp/pde-finite-jet-isolated.HqTCyhjQ`, `OPENBLAS_NUM_THREADS=1`, and `OMP_NUM_THREADS=1`. NumPy reported version 1.26.4. No test scripts or generated data were written.

### Supplied tests

From the isolated root:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde-finite-jet-isolated.HqTCyhjQ OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s tests -p test_finite_jets.py -v
```

Result: all 14 tests passed, reported duration 0.097 seconds. Coverage includes exact scalar identity/cubic hand solutions, a constant-activation moving residual, velocity and kernel normalization, acceleration/jerk differences, forward-field differences, first-layer relabeling, zero residual/input, order prefixes, callback ownership, invalid arguments/outputs, and range checks. Finite-difference comparisons to the existing RHS share a dependency and are not an independent proof of that RHS.

### Independent exact rational gradient check

A separate in-memory check differentiated the scalar network directly, without calling the library's forward, backward, velocity, or kernel implementations to construct expectations. The fixed example was n=2, d=4,

```text
phi(z) = 1/4 + z + z²/2 + z³/6
W1 = [[1,-2,3,1],[-3,1,2,-1]] / 8
W2 = [[2,-3],[1,4]] / 8
W3 = [3,-2] / 8
x = [1,-1/2,3/2,1/4]^T
y = 3/4
kappas = [3/8,5/4,7/8]
```

All expected arithmetic used `fractions.Fraction`. The 14 raw parameters were differentiated using the algebra `Q[e,s]/(e²,s³)`: substitute `theta+s*u+e*ei` into the scalar network; the coefficient of e gives the ith partial derivative as a polynomial in s. Multiplying by `-2*(f-y)*Dii` produces V, DV[u], and `D²V[u,u]/2`. Three directional evaluations give

```text
v = V(theta)
a = DV(theta)[v]
j = D²V(theta)[v,v] + DV(theta)[a]
parameter coefficients = [theta, v, a/2, j/6]
```

Thus the expectations come from coordinate differentiation of the global scalar network, not the audited transpose/product recurrence. Independently evaluating the explicit scalar network on these exact parameter polynomials through degree three gives all forward and output expectations.

All 56 raw parameter coefficients and all 36 preactivation/activation/output coefficients passed comparison with `rtol=2e-13, atol=2e-15`. Both maximum absolute discrepancies were `1.1102230246251565e-16`; the maximum parameter discrepancy scaled by `max(1,abs(expected))` was the same. All four output order prefixes matched exactly. As an exact base-value checkpoint, the output at degree zero was

```text
80517221497149968005 / 7083549724304467820544
```

### C3 activation with no fourth derivative

Used the single shared activation

\[
\phi(z)=1+z+z^2/2+z^3/6+|z|^{7/2}.
\]

It is C3 on R and not C4 at zero. Its third derivative is `1+(105/8)*sign(z)*sqrt(abs(z))`, continuous at zero. For n=d=1, state `(W1,W2,W3)=(0,1,1)`, x=1, y=0, and unit kappas, the initial first preactivation is zero and its physical velocity is nonzero. The degree-three computation succeeded with callback indices exactly `[0,1,2,3,0,1,2,3]`. First weight derivatives agreed with `(-44,-44,-242/9)` and all returned output derivatives were finite. The mathematical regularity argument above, rather than this execution alone, establishes third-order validity.

### Ownership and zero cases

A callback retained every private argument, overwrote all previously retained arguments on each new call, overwrote its current argument after evaluation, and reused one shared output buffer across all derivative orders and both layers. All eight argument arrays had disjoint memory. After return, every retained argument, the scratch buffer, the original parameters, inputs, labels, and rates were modified. Every returned parameter, preactivation, activation, and output coefficient still matched an independent reference call exactly.

A separate width-two zero-input case with `phi(z)=0.4+sin(z)` had all positive first-matrix coefficients zero, while both the middle and readout first coefficients were nonzero. This agrees with the raw equations: x=0 freezes W1, but phi(0) need not vanish.

With constant phi=1, state `(0,0,2^1023)`, x=1, y=-2^1023, order zero returned the finite output even though the unused residual overflows. Order one rejected with `ValueError: residual coefficient must be finite`. With state `(0,0,2^600)`, x=1, y=0, and kappas `(1,1,2^-601)`, order one returned readout and output coefficient -1 despite an unrepresentable squared loss. No loss square is needed.

## Explicit numerical limits, not required corrections

1. **Zero residual does not bypass overflowing backward fields.** With identity activation, n=d=1, `(W1,W2,W3)=(0,2^600,2^600)`, x=1, y=0, the exact physical solution is stationary. Order zero succeeds. Order one evaluates the required backward contraction `W2*W3=2^1200` before multiplying by the zero residual and rejects with `ValueError: jet contraction must be finite`. The real-arithmetic zero-residual conclusion remains correct; the implementation does not promise to avoid this evaluated intermediate. Relevant code: `finite_jets.py:156–162`; disclosed boundary: PROOF.md, lines 311–321.

2. **Finite exact jets can encounter an overflowing composition power.** For identity activation, n=d=1,

   ```text
   (W1,W2,W3) = (0,1,2^-450), x=1, y=-1
   kappas = (2^1000,1,1)
   ```

   the exact ordinary coefficients through degree two are

   ```text
   W1: [0,      -2^551, 2^651]
   W2: [1,       0,     2^101]
   W3: [2^-450,  0,     2^551]
   f:  [0,      -2^101, 2^201]
   ```

   All these and their forward-field counterparts are representable. Order one returns the displayed first coefficients. Order two rejects with `ValueError: activation jet coefficient must be finite`: `series[1]**2` at `finite_jets.py:57` overflows before multiplication by the zero identity second derivative, producing `0*inf`. PROOF.md explicitly excludes protection of composition powers, and `finite_jets.py:94–97` repeats that limitation. This example would contradict an unconditional float64 representability claim, but that stronger claim is not made here.

3. **Range checking is not an error bound.** Raw matrix products, finite convolution sums, and composition powers can also underflow or suffer cancellation. Finiteness validation cannot certify relative accuracy. `_scaled_product` protects the combination of the supplied scalar factors; it cannot recover information already lost in a raw contraction. The contract accurately makes this distinction. A separate probe with identity activation, `(0,1,1)`, y=-1, and kappa1=2^600 rejected at order two because the parameter coefficient itself was unrepresentable, also as expected.

The verdict does not establish global-in-time flow, positive-time numerical accuracy, a uniform-in-width bound, Gaussian or population results, arbitrary depth/batch behavior, or orders above three. No required correction remains within the audited claim.
