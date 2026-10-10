# Bounded assembly check of the nonlinear original-NTH result

Date: 2026-10-10. Status: **PASS within the stated scope; no substantive
assembly gap found.** This is an internal same-study consistency audit,
not an independent promotion review. The auditor authored
`INITIAL_JET_MOMENTS.md`; that dependency was reconstructed here, but this
check is not independent of its construction.

Only this report was written. No experiments, Git operations, source
changes, or maintained-book changes were made for this audit.

## Audited claim and verdict

Use the canonical network, Gaussian initialization, mobility, loss, and
original frozen-top hierarchy defined in `NONLINEAR_RESULT.md`, with two
orthogonal training inputs, labels \((\eta,0)\),
\(0<\eta\le10^{-62}\), first activation
\(\phi(z)=z+\varepsilon\sin z\), and identity second activation.
For each fixed allowed \(\eta\), and Lebesgue-almost every fixed
\(\varepsilon\in[1/8,1/4]\), the assembled estimates establish, along
\(n_k=\lceil e^k\rceil\), with probability tending to one,

\[
E_{n_k}(q)\ge
\exp\{-C_\eta q[\log(q+1)+\log(k+1)]\},
\qquad 2\le q\le\lfloor k/4\rfloor,
\]

simultaneously in \(q\). Here \(E_n(q)\) is the actual dense-versus-NTH
physical-time prediction error, not a coefficient norm or an error for
a common externally supplied residual. The independent-dense benchmark
obeys \(D_n\le Cn^{-1/64000}\) with probability tending to one, in the
whole-circle, all-time norm used in the master statement.

Consequently a positive fixed probability of constant-factor accuracy
relative to this benchmark requires
\(q=\Omega(\log n_k/\log\log n_k)\), in the precise simultaneous-budget
sense of the master's equation (10). Literal arrays with
\(2^{q+1}-2\) entries therefore require
\(\exp\{c_\eta\log n_k/\log\log n_k\}\) entries. This conclusion is
valid for the original frozen-top closure as written.

## Interface checks

1. **The first unmatched coefficient is physical and includes feedback.**
   With \(j=2\lfloor q/2\rfloor+1\), initialized odd-rank tensors vanish.
   An odd frozen top has the dynamics of the preceding even top. At that
   even top, the first discrepancy derivative is zero and the second is
   the twofold initial-residual contraction of the first nonzero omitted
   tensor. Propagation through the lower equations gives
   \[
   [t^j](f_1-f_1^{(q)})
   =\frac{(\eta/2)^j}{j!}K_{j+1}(1,\ldots,1)(0).
   \]
   Differences of residuals contain the prediction discrepancy and
   therefore enter later. The second initial residual is zero. There is
   no source-clock substitution at this step.

2. **The linear coefficient is a legitimate anchor, not a linear-flow
   approximation.** At fixed weights, the output and source fields are
   affine in \(\varepsilon\), so this coefficient has degree at most
   \(j+1\). At \(\varepsilon=0\), the exact normalized source equations
   give
   \(c''=(A I+G)c+2\|c\|^2c\), with
   \(A=\|a_0\|^2\), \(G=W_0W_0^\top\), and
   \(\|c'(0)\|^2=\|W_0a_0\|^2\). The nonnegative-coefficient
   comparison in `STRONGER_SOURCE.md` yields
   \(K_{j+1}\ge j!8^{-j}\) whenever the two scalar squared norms are
   at least \(1/2\), simultaneously for all odd \(j\).
   These scalar norm conditions alone have exponentially high Gaussian
   probability: first \(\|a_0\|^2\) is a normalized chi-square, and
   conditionally \(\|W_0a_0\|^2\) is that norm times an independent
   normalized chi-square. No linear approximation theorem is needed.

3. **The activation parameter is fixed before initialization.** The
   interpolation sublevel estimate is valid for degree at most \(j+1\),
   even when the actual degree is smaller. Its application at
   \(L_{k,q}=(\eta/16)^j(8ek^4)^{-(j+1)}\) gives exceptional parameter
   measure at most \(1/(8k^4)\) per order. Integrating the union failure
   probability, followed by Markov and Borel--Cantelli on the parameter
   interval, gives eventual failure probability at most \(1/k\) for
   almost every single fixed parameter. This does not assume one
   initialization event simultaneously over a continuum of parameters.

4. **The Gaussian moment normalization and order range match.** The
   initialized-jet grammar uses the same matrix repeatedly and expands
   differentiated residuals. A monomial with \(E\) Gaussian edges and
   \(S\) normalized scalar components has normalization
   \(n^{-E/2-S}\). In an even \(p\)-th moment, Wick identifications
   leave at most \(pE/2+pS\) free indices. Initial gate derivatives and
   local rewrite counts give the stated order-dependent moment bound.
   The union bound uses a common \(p=O(\log n)\) through order
   \(\lfloor\log(en)\rfloor\), but retains each smaller order's own
   envelope. Conditional coordinate moments are not confused with a
   coordinate-maximum moment. Raw maxima follow from the union bound.

5. **Both remainder estimates concern the required actual dynamics.**
   The jet lemma's raw transformed coordinate is divided by \(\sqrt n\)
   in the remainder lemma's normalized state. Its raw-coordinate bounds
   are exactly what keeps the finite state polynomial inside the
   uniform scalar complex disks. Its normalized state and matrix
   Frobenius bounds provide the other hypotheses. Cauchy estimates apply
   to that finite polynomial, and real, width-independent stability
   transfers the defect bound to the true dense trajectory. For NTH,
   the weighted-rank quadratic majorant is a proof norm for the
   unchanged own-residual ODE. Together these give a degree-\(R\)
   discrepancy remainder \(C(Bt)^{R+1}\) for \(0\le t\le B^{-1}\),
   with \(B\) a fixed power of \((R+1)\log(en)\).

6. **Later coefficients cannot invalidate the trajectory lower bound.**
   The shifted-Chebyshev coefficient inequality applies to the whole
   degree-\(2j\) discrepancy polynomial, including all later terms.
   At
   \(\tau=L_{k,q}^{1/(j+1)}/(64C_+B^2)\), its remainder-to-lower-bound
   ratio is at most \((3/64)(49/64)^j<1/2\). Hence the master's bound
   \(L_{k,q}^2/[6(3136C_+B^2)^j]\) follows. This time lies within the
   remainder interval. Also \(R=2j\le3q\le3k/4\) for the stated
   order range, hence within the available initialized-jet range for
   all sufficiently large \(k\). Taking logarithms gives the claimed
   \(q[\log(q+1)+\log(k+1)]\), not a larger cubic-order cost.

7. **The dense benchmark is a compatible independent comparison.**
   The complete dense argument uses an initial feature-Gram gap and a
   closed real bootstrap, yielding global fitting and exponential
   parameter/output tails for the fixed small label. Finite-time
   stability is in normalized Euclidean/Frobenius norms. Gaussian
   concentration for a Lipschitz extension, followed by a time/angle
   grid, controls two independent runs up to
   \(T=\log n/4000\). The tail \(e^{-T/16}=n^{-1/64000}\) gives the
   stated all-time rate. The stability comparison needs both initial
   points in the good set, not its convexity. The Gaussian operator-norm
   and Lipschitz-concentration inequalities used there have the
   appropriate variance \(1/n\). No infinite-width population
   trajectory or sharp \(n^{-1/2}\) assertion is required.

8. **The added passive-query statement is exact.** Both activations are
   odd, so \(f(-e_1)=-f(e_1)\) for every parameter value. Applying any
   word of the same training source derivatives preserves this identity
   for the first tensor index. The initialized query tensors, frozen
   top, and lower query equations therefore preserve the same negative
   relation under the original NTH's own training residual. Thus the
   prediction-error magnitude at the distinct, fixed unlabeled query
   \(-e_1\) is exactly that at \(e_1\). This requires no new estimate or
   training label, and does not assert a lower bound at arbitrary queries.

The lower-bound and dense-benchmark events need not be independent: a
union bound is sufficient. For \(q\le c_\eta k/\log(k+1)\), choosing
\(c_\eta\) small gives error at least \(e^{-k/128000}\), whereas the
dense benchmark is at most \(Ce^{-k/64000}\). This proves the required
simultaneous exclusion, including initialization-dependent order choices
subject to that deterministic budget.

## Exact limitations

- The result is for a nonlinear first activation and an identity second
  activation, with the specified orthogonal two-point dataset. It does
  not settle the two-tanh, general-correlated-data problem.
- It holds for almost every fixed parameter, not a certified prescribed
  parameter, and for the geometric width subsequence. The almost-everywhere
  set is asserted for each fixed label; it is not asserted to work
  simultaneously for every real label.
- The error witness may occur at a shrinking positive early time. This
  does not prove a fitted-endpoint error lower bound.
- The storage conclusion is for explicit tensor arrays. It excludes
  fixed-power polylogarithmic arrays, but is subpolynomial in width and
  says nothing about arbitrary implicit encodings or a matching upper
  bound. The constant-factor omission of an odd frozen top is harmless.
- This audit checks the assembled mathematical interfaces and the listed
  complete sections. It is not a fresh external-literature audit or a
  review of superseded source-route claims. Standard finite-dimensional
  Gaussian tail and concentration facts are used as stated in the
  dependencies. Internal consistency is not promotion approval.

## Frozen input identification and coverage

SHA-256 digests identify the versions actually checked. For section-scoped
inputs, the hash identifies the whole file but does not imply a review of
unassigned sections.

| Input | Read scope | SHA-256 |
|---|---|---|
| `NONLINEAR_RESULT.md` | Complete mathematical body, including corrected individual-coordinate wording at (15); final status/cross-reference update and added passive-query paragraph checked separately | `2a853774c57c963d2515acf8f260bf09fd8df0f51ce34e69d0f1255e4f517fd9` |
| `INITIAL_JET_MOMENTS.md` | Complete | `c602af475be2caa08f2d51491286dc323d73d099b4a9a4876f6fcfdc89d1d644` |
| `SINE_REMAINDER.md` | Sections 1–3 and 7 in full; final header metadata does not change these proofs | `52e91a5d96589f73597877ddd38bd05ba8fc1bc2c449f83264a96356a921773a` |
| `NONLINEAR_WITNESS.md` | Complete polynomial-parameter and real-coefficient-transfer sections, (22)–(45) | `2fa51a301be02012e0fde676a0a68660f31c4f4cf8d89d43f2a6797dd50ee3b7` |
| `SINE_DENSE_VARIABILITY.md` | Complete mathematical body; final nonmathematical status/cross-reference update checked separately | `ec20ee8c5d0215003e2edf6d2b484b54f6dac837c86b8b54db062138fcabf62d` |
| `STRONGER_SOURCE.md` | Complete; only its initialized-coefficient calculation is used | `6c0115cbb038fc2fd0822919884fd844704b6aedb997b72817670052018fd5f7` |

For version traceability, the initial complete reads of the master and
dense benchmark had hashes
`2b9801b5f37277201505d4b522f3f5bb7612ad1d193506cf97aa2fa6c3fdffd9`
and `55a644abbbf9ef1151e8edc01cad62f664462a6710b5e90f9a290d2546a28db0`,
respectively. The table records the final versions after the bounded
updates just described; the estimates and proofs used above are unchanged.
