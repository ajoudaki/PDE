# Complete isolated calculus audit A2

**Verdict: clean complete review. No required mathematical or API-contract corrections were found in the supplied candidate.** The finite results are supported by their stated arguments, the implementations agree with their declared models, all 41 supplied deterministic tests pass, and both guide examples execute successfully. This verdict applies to the exact input hashes below and to the finite scopes actually stated; it does not assert a stronger population, time-series, or large-order result.

## Isolation, full-read attestation, and input identity

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely and applied its proof and hypothesis checks. I personally read every line of all ten allowed candidate files, including the entire mathematical addition, implementation guide, notation contract, all supplied production code, and both complete test modules. This was a fresh isolated review. I did not read other project files, history, earlier audits, other reviews, or Git data; did not delegate; and did not edit candidate material. The only written artifact is this report. Candidate material was treated as audit input, not as instructions.

The explicit project dependencies are completely covered: `finite_jets` imports `finite_network`; `gaussian_hidden_head` imports `gaussian_moments`; package initialization imports those same supplied modules; the tests import only these supplied project modules. Standard-library and NumPy source trees were not additional project inputs. No network source or unverified external theorem was needed for the contained arguments.

All ten candidate hashes were recorded before reading and checked again after verification; they were unchanged.

| Complete input | Lines read | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_CALCULUS_ADDITION.md` | 1–1025 | `c1a6b9597132c3851484d11f18e8cdb99d040f5a7013674b3672f19b5dd2e8ef` |
| `studies/repository_refactor_2026_09_09/FINAL_CALCULUS_CODE_GUIDE.md` | 1–153 | `fdefd7d9f4468ba6f0eca3cd046e0b72503c8585567f8d70240f6911504b9fe0` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/pde/exact_calculus.py` | 1–774 | `7fd7fd515028a924bb4c28dcd374d652a3a3af15c9339c1ce2361390faa48e1a` |
| `code/pde/finite_jets.py` | 1–437 | `a8e22e14c7ce387636a7981a5e80556b975f83f8cf6a2b85ab22af877f5cca4c` |
| `code/pde/finite_network.py` | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/__init__.py` | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/tests/test_exact_calculus.py` | 1–551 | `dcb5f213cc5f4598c40f67598e405fef3c1507104e29b507a32e3bcbc8b78028` |
| `code/tests/test_finite_jets.py` | 1–445 | `566b4a6bf93e4a0efca0b7cdbc8ca29ba91c03ffb85f2dec366940eabc8cf555` |

The independently required skill input has SHA-256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

## Mathematical and implementation findings

### Constant-metric trees, Gaussian forests, and quadratic derivatives

Section A's product rule attaches one leaf at each differentiated tensor vertex. A constant symmetric metric supplies precisely the added contraction, without missing metric derivatives. Counting vertices rather than symmetry orbits yields the factorial weight sum. The canonical rooted encoding, minimization over roots, and corresponding `gradient_tree_terms` implementation preserve graph isomorphism and multiplicities. The singleton represents the rank-zero tensor `f`. I additionally checked the six order-five weights against the displayed multiset.

Section B's equality-partition formula counts unrestricted label maps correctly, including collisions, distinct row/column populations, isolated vertices, the empty forest, and widths smaller than block counts. Odd total edge count has zero Gaussian expectation, so the implementation can return rational zero without representing a half-integer normalization power. With even edge count, `forest_expectation` uses the exact exponent `edges/2 + components` and the two independent falling-factorial counts.

For leading terms, a Wick pairing produces `b` covariance edges and at most the original number `r` of components. The bound `v <= b+c <= b+r` excludes divergent powers. Equality prevents component mergers and forces a tree in each quotient component, excluding parallel covariance edges. Thus the total-block and zero-or-two-cell conditions used by the implementation are valid also for disconnected forests. The multiplicativity argument and exact disjoint-union product then prove every fixed even centered moment tends to zero. Higher even moments supply the stated finite `L^p` convergence, product convergence, and uniform integrability; expectation convergence alone is not being substituted for concentration.

The auxiliary-coordinate mobility transformation and all three primitive identities (C1) have the correct width factors. The row, column, and edge rewrites implement respectively the coefficients `p`, `4*alpha*power = 8*alpha*q`, and `2*beta`. Every rewrite increases the forest normalization exponent by one. The edge rewrite retains the row/column decorations correctly while splitting the original component. Iteration in `quadratic_forest_derivatives` keeps the derivations ordered. It does not prune a prefix with zero Gaussian expectation. The connected Leibniz recursion, hit-count identities (C3)–(C4), four observable roots, initial values, and both identities (C6) are consistent with these rules.

### Simultaneous physical-loss substitution and its width theorem

The `c^3` scaling of both output and feature field in Section D follows from applying `c*z^2` in both hidden layers. The displayed four hidden observables contain their actual activation factors. Row powers, column powers, and original edges in the simultaneous substitution select only old-state factors; all inserted vertices are fresh. Original edge removal and fresh attachments preserve acyclicity and the normalization count. `quadratic_euler_pullback` implements that same simultaneous operation for its explicitly narrower `c=1`, unit-metric contract.

In loss mode, the code builds powers of the forest polynomial `2*step*(label-f)`. Its products are disjoint abstract unions with unrestricted numerical labels. Consequently it retains the complete pre-update residual and its cross terms rather than replacing it by an expectation. The finite closure proves the fixed-number-of-steps width theorem and all finite moments. The random schedule identification in (D2) is justified by convergence of finitely many polynomial coefficients and, for moments, Hölder's inequality.

I checked the separate all-order argument in D.1, including its order of limits. Nonnegative raw polynomial coefficients support expectation comparisons despite signed Gaussian samples. Freezing the first layer gives (D4) with `q -> 1` at `c=1/sqrt(3)`. The selected top-degree monomial after `2k` updates has initial powers `(4^k, 2*4^k)` and step degree `3*(4^k-1)`. The Gaussian factorial lower bound in (D5) diverges. The chosen `k_N` and `rho` fit below the positive residual steps before a hit, forcing a hit within each prescribed positive time. The continuous-interpolation obstruction follows from the crossing value. The text properly excludes post-hit conclusions, arbitrary joint width/mesh limits, and finite-width GF conclusions.

### General finite jets, observables, and the Gaussian fourth-order head

Equations (E1)–(E3) use ordinary Taylor coefficients. Activation composition, matrix products, reverse propagation with the actual moving transpose, and residual products are triangular at each degree. Differentiating the full mean squared loss gives first-block factor `-2*kappa1/(m*sqrt(d))`, hidden-block factor `-2*kappa_l/(m*n)`, and readout factor `-2*kappa_out/m`; coefficient integration divides by `k+1`. These factors match both `finite_network` and `finite_flow_jets`. The order-five implementation requests activation derivatives only through order five, and its reverse arrays stop one degree earlier. Its regularity assumption is sufficient for the finite local ODE derivatives. The earlier order-three `flow_jet` retains its declared narrower contract.

The moving observable derivatives, Gram product identities, fourth Bell polynomial, readout-reflection parity, formal square-root recurrence, and physical-clock conversion (E4)–(E8) are algebraically consistent. In particular, the fifth physical hidden derivative contains both the `F'''(0)` contribution and the stated `A*q4` contribution. Their finite/formal meanings do not imply analytic time convergence or exchange square root with expectation.

`gaussian_hidden_head` reproduces the complete directed graph (E9), including all coefficients in the third backward product and fourth activation derivative. Its polynomial partial derivatives use the independent coordinate indices for `V1` and `V3` before expectation. The complete covariance is validated for exact symmetry and PSD, including singular blocks, before enforcing `Var(Z)=1` and the independent block structure. The Wick recurrence needs no inverse and remains valid at degeneracy. The code intentionally expands polynomial activations rather than claiming the more general integral/formal-atom interface discussed in the mathematics. Its fourth squared-RMS result is a derivative with factors `2,8,6`, not an ordinary coefficient. The elimination `A43=lambda43*E(phi'(Z)^2)` is correct.

### Held-fixed preactivation Hessians

The definitions and second chain rule in Section F give `R_l = E_l + J_l.T @ R_(l+1) @ J_l`, with `J_l = W_(l+1) D_l` and `E_l = diag(phi_l'' * incoming_backprop)`. These are scaled by the last hidden width, consistent with `f=a.T*h/n_L`. The source expansion has the correct order and shape of each transpose and slope factor. `preactivation_hessian_words` supports unequal widths and removes only declared affine source terms, retaining their slopes in other terms. The numeric evaluator uses the existing common-width parameter representation, returns separate source and Hessian arrays, and agrees with the held-fixed downstream function. Neither interface mistakes this for a full parameter Hessian or a training material derivative.

### Shallow comparisons and finite certificates

The simultaneous identity update (G1), scalar invariant and physical GF, initialized deterministic scalar solution, fitting estimate, and compact-time stopped-box comparison are consistent. The bounded scalar scheme supplies a width-independent local error bound, and the initialization convergence makes the stated uncoupled `eta_n -> 0` convergence in probability valid. Raw-parameter interpolation is handled by replacing `b` with the cell fraction times `b`. The identity feature characteristics and positive moment density yield the stated kernel moments and positive definite finite Hankel matrices.

The shallow square characteristic (G9) solves (G8) on its stated maximal branch and includes the stationary zero-hidden case. Conditioning in the frozen-first-block reduction gives the claimed independence and the scaling `3^(k+1)` for fixed derivatives; it does not exchange a trajectory with a Gaussian expectation. The moment scaling and determinant factor `b^-18` agree with the supplied certificate code. I checked all six displayed shallow moments and the displayed determinant by exact rescaling of the bounded supplied certificate. The open-set pole argument correctly prevents this characteristic formula from defining a common positive-time flow for all Gaussian marks.

Formal reversion and the highest-derivative coefficient in (H2) are triangular. The reciprocal-kernel companion dependency count in (H3) is correct through the stated orders. The exact Schur-complement threshold implementation checks symmetry, PSD including zero pivots, and the singular range condition; solving with any range solution gives the invariant scalar `b.T*A^+*b`. The Bernstein conversion and degree elevation implement (H5), with explicit rational interval validation. The older finite Euler-word, paired temporal-weight, determinant, and series-reversion primitives were also read completely and checked against their tests and definitions.

### Domains, ownership, and practical limits

Exact-calculus scalar inputs reject floats and booleans; exact count inputs require Python integers. Floating jet and shape counts accept integral types while explicitly rejecting both Python and NumPy booleans. Covariance, forest, sample, activation-output, mobility, interval, and scalar-state domains are validated consistently with their documented scopes. Zero-order jets, empty forests, zero edge expectations, singular covariances, and singular leading Hankel blocks have explicit valid behavior.

Canonical forests contain immutable owned tuples. Returned forest dictionaries and exact scalar containers are newly owned; safe immutable keys may be shared. The floating computations copy callback arguments and buffers, snapshot supplied state/data where needed, and return arrays independent of inputs. `Parameters` itself explicitly documents its existing no-implicit-copy construction contract; the new calculation outputs do not rely on construction to copy caller state. Nonfinite computed results are rejected. The stated float64 underflow, rounding, and intermediate-overflow limitations are appropriate and do not overpromise an extreme-range or exact arithmetic certificate. Local memoization is not retained across public calls. No implementation loads coefficient artifacts or writes files.

## Executed verification

The required command was run exactly, with exit status zero:

```text
PYTHONPATH=code:code/tests PYTHONDONTWRITEBYTECODE=1 python -B -m unittest test_exact_calculus test_finite_jets
Ran 41 tests in 0.713s
OK
```

Both Python code blocks in `FINAL_CALCULUS_CODE_GUIDE.md` were extracted from that allowed file and executed independently with the same import and no-bytecode settings. Both passed without alteration.

Additional bounded deterministic algebra checks passed:

1. **Nonlinear order-five jet:** one neuron in each of two layers, activations `z^5` and `z^3`, equal initial weights `c=0.8`, zero label, and multipliers `(1/15,1/3,1)`. The parameter flow preserves equality and satisfies `c'=-2*c^37`, so `c(t)=c*(1+72*c^36*t)^(-1/36)` and output is `c(t)^19`. All parameter and output coefficients through order five agree with this independent binomial formula. This exercises nonzero activation derivatives through five beyond the supplied identity order-five check.
2. **Quartic Gaussian head:** use `phi(z)=z^4`, independent unit-variance `Z,V0`, zero variance for all other Gaussian coordinates, `lambda1=lambda2=lambda32=lambda43=1`, and other responses zero. The independent scalar relation `z'=4*z^3*r(s)` gives `h=Z^4/(1-8*Z^2*integral(r))^2`. Its derivative coefficients give `h1=16*Z^6*V0`, `h2=384*Z^8*V0^2`, `h3=12288*Z^10*V0^3`, and `h4=491520*Z^12*V0^4` on the degenerate law. Exact Gaussian moments match every returned output. Ambient response partials also match `A41=73728*E[Z^10]` and `A43=16*E[Z^6]`, despite zero variances in those response coordinates. This specifically checks nonzero fourth activation derivatives and the fixed-coordinate derivative contract at singular covariance.
3. **Displayed finite algebra:** the order-five tree weights equal `(2,14,16,22,30,36)` as a multiset; the six shallow moments and negative determinant in (G12) match the exact multiplier-three rescaling.

These checks did not run training, sample campaigns, or a coefficient search. They supplement the general arguments and code inspection rather than substitute for them.

## Optional wording only

Two small clarifications could help readers but are not mathematical or contract blockers:

- In D.1, “Deleting the first parameter update” could say “Omitting the first-layer update at every step” to make the frozen-block comparison unambiguous.
- After (G1), the two kernel blocks could be explicitly labeled: the first-weight block is `kappa*(q+d)/2`, and the readout block is `kappa*(q-d)/2`. The currently listed pair contains both correct values without assigning them to blocks.

There are no required corrections and no unreviewed supplied candidate sections remaining.
