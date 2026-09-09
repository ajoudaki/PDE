# Independent complete review A2 — finite reductions and positive-metric Taylor obstruction

**Verdict: CLEAN. No required mathematical, implementation, API, test, normalization, or scope correction was found in the supplied version.**

This verdict concerns exactly `/tmp/pde_continuation_review_b2`: the 15 source files in `INPUTS.json` (3,622 lines), plus the manifest. All source files were read in full, all 20 supplied tests passed, and the independent deterministic checks below passed. No checkout, history, study artifacts, prior review, other task, or unsupplied mathematical dependency was consulted. No delegation, training trajectory, sampling campaign, or high-order search was performed. Inputs were not changed.

The applicable instructions were read in `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, with the research-contract, adversarial-audit, decisive-experiments, and evidence-ledger references. This is a complete review of this packet, not a partial pass or a claim about unsupplied material.

## Contract and claim separation

The finite reductions use one sample `x=1`, input dimension one, two equal hidden widths, arbitrary finite raw parameters and real label, output division by `n`, stored middle matrix `B` without a second width normalization, and parameter metric `||du||²/n + ||dB||_F² + ||da||²/n`. Unit output ascent and full-square-loss physical flow are kept separate by `dot(theta)=-2(f-y) theta'`. The proofs do not require a positive feature clock.

Section 10 instead fixes label one and independent standard Gaussian primitive variables `(u,g,a)`, with stored matrix `g/sqrt(n)` and an order-one stored readout. It explicitly differs from the small-readout initialization in `NOTATION.md`. Its objects are fixed-order annealed initialization derivatives, followed by a width limit and then Taylor truncation. The paper does not silently turn annealed coefficients into a population trajectory, a concentration theorem, or a limit of physical finite-width losses.

The strictly positive metric obstruction is existential for `(alpha, beta)=(alpha,1)` with sufficiently small positive alpha. The canonical-metric result concerns failure of the prescribed positive Taylor polynomial family on compact intervals containing initialization. Neither is stated as a no-go theorem for other finite representations or for a nonlinear population evolution. These distinctions are mathematically necessary and are retained consistently.

## Main proof audit

### Finite reductions, Sections 5–7

- **Output gradients and scalar kernels, equations (10)–(12):** Direct differentiation of `a^T B(u²)/n` and `a^T(Bh)²/n`, followed by the inverse metric, gives exactly all QI/IQ/QQ rows. The factors 2, 4, 4, and 16 in the vector fields and first-layer kernels are correct. Matrix outer products carry `1/n`, and their squared Frobenius norms carry `1/n²`. Residuals occur only when converting to physical flow. The loss velocity is `-4r²K`.
- **Isometric blocks and Lax identities, equations (13)–(18):** Passing vectors to `v/sqrt(n)` leaves stored matrix entries unchanged. QI has `Q'=QS`; IQ has `P'=2SP`. The signature anticommutes with the symmetric generator, giving the stated commutators. The raw QI conservation of `BB^T-aa^T/n` has matching derivatives. Output and kernel readouts from the full current block matrices are correctly normalized. These retained matrices depend on width, as acknowledged.
- **Isospectrality:** The time-dependent similarity proof has the correct sign: with `Ldot=[L,F]`, solving `U'=-FU` and `V'=VF` gives `VLU` constant. The factorial integral bound establishes the auxiliary linear systems on every compact raw solution interval without assuming self-adjointness of `L`.
- **Orientation witness:** The supplied reflection maps the first readout to the second and fixes `h`. It conjugates the two signed Gram matrices, while their common output is `1/3` and total kernels are `68/9` and `28/3`. Thus the asserted difference of `16/9` is correct. This refutes restart sufficiency of the retained spectrum, current `h`, and output for the stated QI states; it does not attack the full-operator state.
- **QQ balances:** Differentiating each row/column square produces the exact cancellations in (20), including the distinct factors `2a_i²` and `u_j²/2`. The conversion to physical time preserves zero derivatives.
- **RMS differentiation, equations (21)–(29):** Both normalizers depend on every neuron and are differentiated. `DN=Pi/sigma` is correct. With epsilon positive, `Pi` is symmetric positive definite, generally not a projector. Backpropagation through both normalizers produces `c=a-fv`, `b=2z*c/beta`, and `q_tilde=Pi_h B^T b`. The first-layer field and kernel include their required powers of alpha. The displayed feature and normalizer derivatives agree with direct chain rules. The contraction `h^Tq/n=2 epsilon f/beta²` uses `||v||²/n=1-epsilon/beta²` and is exact.
- **RMS balances and reduced state, equations (30)–(32):** The row drift is `-4f v_i²`; the column drift is `4 epsilon f h_j²/beta²`. These are signed ascent derivatives, not claimed invariants. Recovering alpha from `rho_h<1` is valid. On raw-image states, `h>=0` makes `A_h=(4/alpha)Pi_h diag(h)Pi_h` positive semidefinite. It gives both `h'=A_h q` and `K_1=q^T A_h q/n`. Smoothness is only required on the open set `rho_h<1`. Raw lifts, preserved zero coordinates, arbitrary nonzero signs, local uniqueness, and global physical raw continuation together justify restartability and sign independence. No extension to `rho_h=1` or global feature-ascent solution is claimed.
- **Global physical existence, equations (33)–(34):** The polynomial models and positive-epsilon normalized model have locally Lipschitz physical fields at every finite state. The weighted energy identity and Cauchy–Schwarz make the parameters Cauchy at any putative finite maximal endpoint. At fixed width the metric is equivalent to Euclidean norm, so a finite limit can be continued locally. This proves the claimed global forward physical flow. It supplies neither an arbitrary-step GD assertion nor population uniform-integrability estimates, in agreement with the text.

### Positive-metric Taylor obstruction, Section 10

- **Primitive metric and derivatives:** Converting from stored `B=g/sqrt(n)` to `g` gives mobility `n beta`, as in (10.2). The polynomial degree of the output is seven; every nonzero primitive field has degree six. All factors and sums in (10.3) match direct differentiation.
- **Derivative forests:** The initial output is the specified two-edge tree with normalization `n^-2`. Differentiating a row decoration attaches two fresh columns; differentiating a column retains its even decoration and adds a two-edge path; differentiating an edge removes that bridge and adds a leaf, creating a new connected component. The factors are respectively `p_v`, `8 alpha q_w`, and `2 beta`. Every rewrite increases `e/2+r` by exactly one and remains a simple bipartite forest. Unrestricted labels correctly include coincident numerical indices and their product-rule multiplicities. The expansion is finite at every fixed order and independent of width.
- **Wick limit and factorization:** Pairing edge factors identifies both endpoints. With `b` covariance edges and `c` quotient components, `v<=b+c<=b+r`. The unrestricted labeling count is `n^v+O(n^(v-1))` after separating extra coincidences; decoration moments are bounded at fixed degree. Therefore no power of width diverges. A surviving pairing requires `c=r` and tree quotient components, so it pairs within each original component and factors. Isolated vertices and odd edge counts are covered. This proves existence of each annealed derivative and nonnegative mobility-polynomial coefficients. Total primitive parity gives vanishing even derivatives. No unproved independence of trained variables is used.
- **Positive-mobility moment obstruction:** Formal inversion is valid because the linear coefficient is nonzero near alpha zero. The triangular coefficient recurrence makes every fixed inverse/composition coefficient rational in finitely many jet coefficients, with only powers of the linear coefficient in possible denominators. Thus the fixed witness is continuous in alpha. The exact negative boundary value is reproduced by the supplied monomial recurrence and rational certificate. A nonnegative measure on `[0,infinity)` would make the same finite expression the nonnegative integral of `lambda p(lambda)^2`, a contradiction. The existential open interval and exclusion of a conclusion at alpha one are properly stated.
- **Canonical factorial growth:** The nonnegative primitive-coefficient cone is preserved by each block derivation. The ordered-word expansion includes the wholly frozen-first-block word with all remaining words having nonnegative Gaussian expectation; this justifies (10.14) without comparing trajectories. Conditional on `u`, the frozen `(a_i,z_i)` pairs have exactly the stated Gaussian law. The variance/convexity/Cauchy–Schwarz argument establishes convergence of every fixed polynomial moment of `q_n` to the corresponding power of three, hence (10.16). For odd order, the monomial rule gives nonnegative even-power coefficients. The invariant ray provides (10.19). The inequalities `(2u-1)!!>=u!`, `u!v!>=m!/2^m`, and `2^-v>=2^-m` prove (10.20) and the claimed factorial bound. Its root argument establishes radius zero and failure of terms to vanish at every positive feature argument.
- **Prescribed physical Taylor family:** Positivity and `c_1>0` give unique positive output roots and a well-defined residual clock. The separated integral diverges at the output-one root, proving a global finite-order physical loss. The translated polynomial solves the source PDE and its finite coefficient ODE; the supplied integral inequality proves uniqueness. Positive partial sums diverge at each fixed positive feature argument, pushing every subunit-output root and its hitting time to zero. The losses therefore have value one at zero and pointwise limit zero at every positive time. This discontinuity excludes uniform Cauchy convergence on every `[0,T]`, `T>0`. The bounded sup metric triangle inequality then correctly excludes the stated iterated common-target shadowing claim without assuming that a limiting network trajectory exists.

## Dependencies and implementation

The complete `NOTATION.md` and `finite_dynamics.md` were checked: raw gradient blocks, dataset normalization `1/m`, input factor `1/sqrt(d)`, block kernel positivity, weighted dissipation, local-to-global continuation, bounded-derivative forward/backward RMS induction, and the finite Gaussian initialization bounds are consistent. The argument is fixed depth and fixed input dimension; it does not use RMS bounds as population compactness.

The entire Gaussian dependency chapter and exact Gaussian implementation were checked, including singular covariance integration by parts, the exact Schur-complement PSD validator, the terminating moment recurrence, forest-key invariance/validation, formal reversion, determinant elimination, all seven odd derivatives through order thirteen, six moments, and the direct polynomial witness. Their numerical certificate is finite exact arithmetic and has the separate initialization-jet interpretation supplied in the text.

The complete loss-GD pullback dependency was checked. The linear mobility coordinate change preserves raw Euler steps. Frozen directional derivatives inside `T_k` and moving-field differentiation by outer words are distinguished correctly. The finite binomial operator identity and composition recurrence yield the temporal polynomials through degree five. The degree cancellation, fixed-N sixth-derivative integral remainder, arbitrary-residual cubic coefficients, stationary/affine cases, and conditional convex-tube estimate are correct. The tube explicitly contains all necessary hybrid and intermediate states. The fixed-order coefficients are not used to claim remainder control or a width limit.

`finite_reductions.py` implements the stated QI/IQ/QQ and differentiated RMS fields and their clocks. Kernel blocks are calculated as their squared metric norms. Lax output includes the IQ factor two in the generator. Raw-state validation enforces two hidden layers and input dimension one. Labels, epsilon, models, and evaluated nonfinite results are checked. Returned arrays are fresh and input parameters are revalidated and unchanged; the mutable contained arrays/dictionaries are documented. The float64 limitations and possible underflow are explicit, so ordinary intermediate-range behavior is not misrepresented as certified arithmetic. The stated work/storage bounds are appropriate.

The complete `finite_network.py`, `gaussian_moments.py`, `exact_calculus.py`, and package exports were read against the supplied API contracts. The finite core's raw gradient and kernel normalization agrees with the new reductions; custom activation ownership, mutable-parameter revalidation, simultaneous GD, scaled products, zero-step semantics, and finite-value checks match their stated scope. Exact calculus rejects its specified nonrational/noninteger input types, produces fresh results, and contains no retained coefficient table. The two new combinatorial Euler interfaces do not claim to evaluate derivatives or network moments. `API_ADDITIONS.md` accurately describes these behaviors and the narrower scopes.

No unresolved proof dependency or required repair remains within this packet. The explicit absence of a population identification theorem, a numerical endpoint for the positive-metric interval, and a general high-order compiler is a scope boundary, not a missing premise of the supplied conclusions.

## Verification

Supplied tests were run once, without bytecode writes:

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/pde_continuation_review_b2/code python -m unittest discover -s /tmp/pde_continuation_review_b2/code/tests -v
Ran 20 tests in 0.286s — OK.
```

The full 11 exact-calculus and 9 finite-reduction tests were read, including their independent constructions, and all passed. They check exact certificate arithmetic, both series compositions, independent determinant permutations, graph relabeling/validation, Euler slot enumeration and nonlinear direct Euler composition, finite core comparison, Lax chain rules and orientation witness, QQ balances, every RMS gradient coordinate, feature derivatives, energy, signed drifts, zero/residual/sign cases, ownership, and scope rejection. Numerical finite differences are treated as checks, not as proofs of the identities.

Additional checks were specified before execution and stored outside the packet in `/tmp/pde_finite_taylor_review_A2_diagnostics.py`. The hard bound was one fixed width-two state, no evolution, derivative order one for the forest calculation, and frozen orders 1, 3, 5, 7 for the factorial identities. The numerical acceptance threshold was scaled absolute gradient/reconstruction error at most `1e-12`; the algebraic checks used exact equality or rational inequalities. All passed:

| Independent check | Result |
|---|---|
| Complex-step gradient from output definitions, QI | Maximum scaled error `0` |
| Complex-step gradient from output definitions, IQ | `1.244e-17` |
| Complex-step gradient from output definitions, QQ | `1.711e-18` |
| Complex-step gradient from output definition, RMS | `8.172e-17` |
| Recover alpha from h and evaluate reduced RMS operator | Passed within `1e-12` |
| Independent Wick quotient enumeration of the first derivative forests | `d_1(alpha,beta)=48 alpha+36 beta+27` exactly |
| Frozen coefficient / lower bound, k=1 | `63 >= 27/2` |
| Frozen coefficient / lower bound, k=3 | `12960 >= 1215` |
| Frozen coefficient / lower bound, k=5 | `11439468/5 >= 91854` |
| Frozen coefficient / lower bound, k=7 | `424802880 >= 7085880` |
| Independent polynomial invariant-ray evaluations at those orders | Exact equality with `(6^(k+1)) binom(k+2,2)` |

In particular the independently obtained first annealed coefficient gives the boundary value `63` and canonical value `111`, consistent with the chapter's lower bounds. The factorial spot checks support the normalization; the all-orders proof above is what supports the divergence claim. Runtime environment: Python 3.10.12, NumPy 1.26.4, Linux x86_64. There were no failed or excluded runs.

## Complete read coverage and integrity

Every file below was read from its first through its final line; the manifest was also read in full. Source line counts total 3,622. SHA-256 values were computed before and after the review. Each source matches the manifest's hash, byte count, and line count. All 16 files, including the manifest, are unchanged and no file was added inside the packet. Before/after records are `/tmp/pde_finite_taylor_review_A2_before.json` and `/tmp/pde_finite_taylor_review_A2_after.json`.

| File | Full lines read | SHA-256 before = after |
|---|---:|---|
| `code/API_ADDITIONS.md` | 1–118 | `eb0a736a1419ff9c1e8011d6a2fd0c5d63a9b8be7d09f321010106ec6b9cf0de` |
| `code/NUMERICAL_CONTRACT.md` | 1–91 | `3791adea2ec3a4713a265ab1aa2b00e9993b51a957415060bebc88fe2399de22` |
| `code/pde/__init__.py` | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | 1–249 | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_network.py` | 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_reductions.py` | 1–251 | `b74b7da576e75749417dce2662e04c110f6028f09b724cfa1d295f1055c99225` |
| `code/pde/gaussian_moments.py` | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | 1–217 | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `code/tests/test_finite_reductions.py` | 1–239 | `bd0063b5d7865cdb9f9b13e7bbea9118379a9baf2cb28845989ffbdd77935a9e` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 1–214 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/finite_reductions.md` | 1–434 | `5c422cb6bed3ce0816853cccd78d49a85f1fd3c8ca9718528584e15dc725427f` |
| `docs/gaussian_dependencies.md` | 1–346 | `e52365e7ed2afaf3d48272b913caf60e1aa59f55d846019527f84ae15592cf84` |
| `docs/loss_pullback.md` | 1–366 | `dccefe204d607ad778a09e9a2c98ced0fbcb50a75cba869c44df9d9f652108ea` |
| `docs/positive_metric_taylor.md` | 1–496 | `bfe815697f0a7a6e090d3e48bcf72cdf357e2cc9fbeb837007ce636010b667b8` |
| `INPUTS.json` | 1–77 | `6ab215441c7a0837d2d5e27c824ec03d002b818d8d934ff492ddc243cc9bd55f` |

No required corrections. The CLEAN verdict applies only to the immutable supplied version identified by these hashes.
