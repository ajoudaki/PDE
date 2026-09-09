# Independent complete calculus review B2

**Verdict: clean complete packet. No required correction found.** The proof,
implementation, guide examples, and supplied deterministic tests agree within
their stated finite and asymptotic scopes. A nonblocking block-label clarification
is recorded below.

## Independence and complete-read attestation

I personally read the complete contents of all ten allowed packet files, including
all 1,025 proof lines, all 153 guide lines, all 98 notation lines, all 1,714
implementation lines, and all 996 test lines: 3,986 packet lines in total. I also
personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` in full and applied
its proof-audit requirements. Any truncated tool display was followed by another
read covering the missing portion.

I did not consult history, other source files, previous reviews, Git, or external
sources; did not delegate; and did not edit any candidate file. The reviewed
documents were treated as review data. Only this review file was written. The
supplied tests, both guide examples, and the independent checks described below
were run without bytecode writes. No training, sampling campaign, or large
coefficient campaign was performed.

The packet hashes were collected and rechecked after the audit; they were
unchanged.

| Allowed input | Lines | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_CALCULUS_ADDITION.md` | 1025 | `c1a6b9597132c3851484d11f18e8cdb99d040f5a7013674b3672f19b5dd2e8ef` |
| `studies/repository_refactor_2026_09_09/FINAL_CALCULUS_CODE_GUIDE.md` | 153 | `fdefd7d9f4468ba6f0eca3cd046e0b72503c8585567f8d70240f6911504b9fe0` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/pde/exact_calculus.py` | 774 | `7fd7fd515028a924bb4c28dcd374d652a3a3af15c9339c1ce2361390faa48e1a` |
| `code/pde/finite_jets.py` | 437 | `a8e22e14c7ce387636a7981a5e80556b975f83f8cf6a2b85ab22af877f5cca4c` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/tests/test_exact_calculus.py` | 551 | `dcb5f213cc5f4598c40f67598e405fef3c1507104e29b507a32e3bcbc8b78028` |
| `code/tests/test_finite_jets.py` | 445 | `566b4a6bf93e4a0efca0b7cdbc8ca29ba91c03ffb85f2dec366940eabc8cf555` |

The personally read skill has SHA-256
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

## Mathematical and implementation findings

- **A: constant-metric derivative trees.** Differentiating a vertex tensor adds
  exactly one leaf; every vertex, including repeated symmetry-orbit members,
  contributes. The canonical-key recursion represents the unrooted isomorphism
  classes while accumulating attachment multiplicities. The singleton convention,
  constant-matrix hypothesis, derivative regularity, and factorial total weights
  are consistent with the implementation. I independently checked the displayed
  order-five multiset `2,14,16,22,30,36`.

- **B: exact normalized forests and concentration.** Separate row and column
  equality partitions account for unrestricted numerical labels, with distinct
  block-label counts given by the two falling factorials. Zero Gaussian moments
  handle parity, including odd total edge count. The quotient bound
  `v <= e/2 + components` forces component-preserving quotient trees at leading
  order. The zero-or-two-cell implementation is valid also for disconnected
  forests and isolates: an extra component identification would violate equality
  in that bound. Disjoint-union multiplication then proves convergence of all
  moments, centered even moments, and every finite Lp norm. The conclusion is
  restricted to fixed finite forest combinations and does not assert coordinate
  convergence or estimates uniform in derivative order.

- **C: weighted rewrites.** Direct differentiation in auxiliary `(u,g,a)`
  coordinates gives the stated `1/n`, `4*alpha`, and `2*beta` primitives. Row,
  column, and edge rewrites preserve the required normalizations; a deleted edge
  is a bridge, so its replacement raises component count by one. The connected
  recursion's binomial convolution follows from Leibniz and leading component
  factorization. The hit-count identities, increments `19,13,17`, Ward identities,
  hidden-root normalizations, and initial values `1,3,3,27` check algebraically.
  The code preserves ordered block differentiation and performs neither forbidden
  zero-prefix pruning nor the invalid binary-rank shortcut.

- **D: loss Euler closure and the width-first theorem.** Each original factor is
  substituted once, and all fresh factors remain unupdated inside that step.
  Multiple hits at a vertex retain the correct binomial coefficients. Full-loss
  feedback is the forest polynomial `2*step*(label-f)`, evaluated at the pre-update
  state; the implementation expands its powers rather than freezing its limiting
  value prematurely. Fixed finite programs remain finite forest combinations,
  proving all finite moments as claimed. The activation scaling is `c^3` for
  both the output and feature field. In D.1 the frozen-row comparison is
  coefficientwise before expectation, so signed Gaussian states cause no invalid
  samplewise inequality. The selected monomial after `2k` steps has exponents
  `(4^k,2*4^k)` and step degree `3*(4^k-1)`; the displayed Gaussian-moment lower
  bound diverges and proves the stated hitting-time obstruction. The theorem
  keeps width first, takes no arbitrary joint diagonal, and makes no post-hit,
  terminal-loss, or finite-width gradient-flow claim.

- **E: finite moving jets and observables.** The ordinary coefficient recurrence
  uses every convolution split, the moving residual, every moving parameter
  block, and the actual reused transpose. The first input factor, output `1/n`,
  full mean-loss `2/m`, endpoint mobilities, interior `1/n`, and integration
  factor `1/(k+1)` match the raw API. `finite_flow_jets` supports orders zero
  through five, requests only derivatives zero through the requested order,
  and returns backward degrees through one lower order. The stated C^(q+1)
  hypothesis suffices for local flow and finite differentiation; no analytic
  time series is inferred. Observable Bell formulas, squared-RMS product
  coefficients, reflection parity, deterministic square-root conversion, and
  the physical-clock identities through order five check directly. The Gram API
  contracts only the selected layer and distinguishes ordinary coefficients from
  derivatives.

- **E.1: polynomial Gaussian head.** Every Bell and product coefficient in E9
  matches the code. Complete rational PSD covariance is validated before any
  parity shortcut, the independent blocks and unit Z variance are enforced, and
  singular laws need no covariance inverse. Polynomial expansion and Wick
  recursion compute the stated expectations exactly. Response partials hold all
  other coordinates and constants fixed before expectation, including on
  singular supports. In particular `A43=lambda43*E[phi'(Z)^2]`; the fourth RMS
  output is a derivative with factors `2,8,6`. The implementation offers only
  the documented polynomial actual-Gaussian mode and forms derivatives zero
  through four; it does not silently implement the broader formal-atom or
  nonpolynomial discussion as a neural population model.

- **F: typed held-fixed curvature.** The local source uses incoming backprop,
  not the already slope-multiplied backward vector. The Hessian chain rule gives
  `E + D W.T R W D` with the last-width normalization intact. The word compiler
  respects unequal-width matrix types and multiplication order, omits only
  declared affine source terms, and retains affine slopes in other source terms.
  The numeric evaluator uses the existing common-width state contract. Its
  output is the downstream preactivation Hessian, not a full parameter Hessian
  or a material derivative along training.

- **G: shallow comparisons.** Raw identity GD closes exactly on `(f,q,d)`;
  the continuous invariant and scalar limiting equation give the stated global
  population flow and decay. The stopped-box discrete error proof covers a
  growing number of updates for every `eta_n -> 0` on each fixed horizon, and
  the raw interpolation formula supplies the within-cell estimate. The identity
  moment density and strict Hankel positivity follow from the explicit integral.
  The raw-square characteristic formulas, pole obstruction, multiplier-three
  frozen-block reduction, and determinant exponent `-18` check independently.
  I regenerated all six shallow moments and the exact negative determinant in
  G12 from the stated scalar monomial derivation, independently of the production
  certificate routine, and verified their scaling against that routine.

- **H and the remaining exact APIs.** Formal inverse coefficients are triangular;
  the highest-derivative coefficient and the output/hidden dependency counts
  follow with the stated factorials. The singular Schur threshold is accepted
  exactly when the supplied column lies in the range. The implementation's
  arbitrary solution of `Ax=b` gives the same `b.T*x` on that range. Bernstein
  conversion and degree elevation are exact and certify only supplied
  polynomials. I also read and checked the existing Euler-word compiler, paired
  Euler weights, determinant, series reversion, and fixed axis-certificate code.

The guide's signatures, imports, data shapes, rational-versus-floating types,
explicit clock, and supported scopes agree with the implementation. The existing
package exports remain accurately used through their documented modules. Counts
reject booleans and nonintegral values; exact rational operations reject floating
and boolean scalars. Forest keys are immutable and canonical, returned
polynomials are freshly owned, and numeric callbacks receive private arrays with
copied results. The floating routines disclose ordinary roundoff and intermediate
overflow/underflow limits rather than claiming exact numerical certificates.

## Executed validation

The exact requested command passed:

```text
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 python -B -m unittest test_exact_calculus test_finite_jets
Ran 41 tests in 0.759s
OK
```

Both complete Python blocks extracted from the guide executed successfully,
including every assertion. The supplied tests contain substantive independent
oracles: unrestricted finite label sums, direct simultaneous raw updates,
scalar differential-operator words, rational permutation determinants,
schoolbook composition, exact Gaussian quadrature with an independent time-series
head, raw gradient and second-variation checks, and independently differentiated
downstream polynomials. These test mechanisms are appropriate to the finite
claims; passing tests were not used as a substitute for auditing the proofs.

Additional small deterministic checks passed:

1. Independent order-13 shallow monomial differentiation, inverse-series
   composition, six displayed rational moments, permutation determinant, and
   multiplier-three scaling.
2. A genuinely nonlinear order-five jet with `phi(z)=z^5`, one neuron, equal
   initial parameters, and mobilities `(1/5,1)`: the invariant solution
   `a(t)=u(t)=(1+20t)^(-1/10)` verifies every parameter, hidden, and output
   coefficient through order five, including the nonzero fifth activation
   derivative.
3. The affine local-head response identities
   `A43=lambda43*b^2` and
   `A41=lambda41*b^2+lambda43*d32*lambda2*b^4` for `phi(z)=a+b*z`.
4. A zero-expectation isolated row whose derivative has expectation three;
   two odd-edge components with leading expectation zero and finite-width
   expectation `1/n`; and the empty-forest loss pullback.
5. A singular rank-two rational Schur example with an intermediate zero pivot,
   its out-of-range rejection, singular Gaussian Wick moments, and the zero-law
   constant moment.
6. Numeric Hessian agreement under callbacks that overwrite their private input
   and reuse an output buffer, followed by mutation of all returned array groups
   while confirming that input parameters and data remain unchanged.

## Nonblocking wording clarification

At proof lines 741–743, the two shallow identity kernel values are correct as
an unordered pair but are not named. Explicitly, the first-weight block is
`kappa*(q+d)/2`, and the readout block is `kappa*(q-d)/2`. This is the order
returned by `finite_network.kernel_blocks`. For `u=2`, `a=3`, and `kappa=1`,
the API returns first/readout values `(9,4)`. Naming the blocks would avoid a
reader interpreting the proof's displayed order as the API's storage order.
The current text does not assign the opposite names, so this is a clarity
suggestion, not a required mathematical correction.

The clean verdict applies to the precise finite algorithms and explicitly
ordered limit statements reviewed here. It does not certify numerical
correctness beyond the documented float64 limits or extend any fixed-order,
fixed-program, or local claim to an unstated uniform regime.
