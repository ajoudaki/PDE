# Independent complete proof review A2

**Verdict: CLEAN. No required correction identified in the supplied version.**

The exact finite representation, its converse, the four supplied-query bounds, and the retained-memory estimates are valid under their stated hypotheses. The examples correctly expose missing general inferences. None establishes a counterexample for a reachable canonical network state, and the text expressly avoids that claim.

## Scope and full-read ledger

This review used only the isolated input package `/tmp/pde_query_review_2`, together with the required mathematical-review skill instructions. No checkout, studies, history, earlier review, other task, external source, or delegated analysis was consulted. No training or trajectory integration was performed. Computation was limited to file hashes, byte counts, and line counts; the mathematical checks below were analytic.

The following files were read in full, including all displayed equations and qualifications:

| Input | Full range read | Bytes | Role |
|---|---:|---:|---|
| `docs/NOTATION.md` | 1–98 | 5,110 | Complete canonical notation and conventions |
| `docs/finite_dynamics.md` | 1–214 | 8,355 | Complete finite dynamics and energy dependency |
| `docs/integrated_queries.md` | 1–242 | 10,764 | Complete primary proof |
| `INPUTS.json` | Entire manifest | 461 | Frozen input identification |

Total mathematical input: **3 files, 554 lines**. The complete notation and finite-dynamics files were read in a dedicated, untruncated output after an earlier combined output was truncated.

Required instructions read: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/etc/codex/skills/investigate-conjectures/SKILL.md`, and its `references/research-contract.md`, `references/evidence-ledger.md`, and `references/adversarial-audit.md`. Experiment-design and multi-route proof-search references were inapplicable because neither activity was undertaken.

## Input-integrity ledger

The initial hashes agree with the manifest. The final verification repeated hashes, bytes, and lines after writing this report; every supplied file remained unchanged.

| Input | SHA-256 before = after | Manifest agreement |
|---|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | Exact |
| `docs/finite_dynamics.md` | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` | Exact |
| `docs/integrated_queries.md` | `fbe02d7d7c85167242cca00393fdb01f62c2357e5d94900cc1b439157b93850e` | Exact |
| `INPUTS.json` | `521dafbbbc12bbc70de988503c2923afcc63480554fd15ad51d42692f959592a` | Baseline unchanged |

## 1. Canonical model, normalization, clocks, and initialization

The specialization is exactly `L=3`, `m=d=1`, `x=y=1`, and all mobility multipliers equal to one. Thus the first raw weight vector equals `z^1`, and the stored readout is `a=W^(4)`. The transpose remains the transpose of the same finite matrix. No independent backward random map is introduced.

Since `f=a^T h^3/n`, backpropagation yields

\[
\nabla_{z^1}f=\delta^1/n,\qquad
\nabla_{W^{(2)}}f=\delta^2(h^1)^T/n,\qquad
\nabla_{W^{(3)}}f=\delta^3(h^2)^T/n,\qquad
\nabla_a f=h^3/n.
\]

Applying block mobilities `(n,1,1,n)` gives exactly (13.2). Multiplication by `-2(f-1)` gives the gradient flow for the full square `(f-1)^2`. Therefore a represented physical orbit satisfies `ds/dt=-2(f-1)`, without another factor of `n`, `m`, or `1/2`. This conditional clock statement does not assert positivity of the clock for arbitrary initial data or global forward coverage by a feature interval. Where the canonical positive feature clock is used, `f<1` supplies its positivity. Physical global existence from the dependency is not used to claim global existence or convergence of this clock.

The initialization is the canonical one: first-coordinate variance one, middle-entry variance `1/n`, and stored-readout variance `1/n^2`, with block independence. It is not an order-one readout initialization. The identities are explicitly deterministic and conditional on a finite `C^1` solution. Bound (13.6), especially its readout infinity bound, is an additional stated hypothesis; the chapter does not substitute a readout RMS bound for it or assert an unproved probability estimate for that event.

Every rank-one matrix carries `1/n`; every hidden-vector RMS divides the ordinary Euclidean norm by `sqrt(n)`. The auxiliary finite transformed vector `X^1` and primitive `b` are explicitly typed and defined, which is permitted by the notation contract. They do not silently replace population coordinates or canonical backward sensitivities.

## 2. Exact representation and complete converse: (13.3)–(13.5)

For arctangent, `phi'(z)=1/(1+z^2)`, so `F'(z)=1+z^2=1/phi'(z)`. Strict positivity and the two infinite endpoint limits make `F` a bijection of the real line; its inverse is continuously differentiable, with derivative `phi'(F^{-1}(X))`. Consequently

\[
(X^1)'=(W^{(2)})^T\delta^2=(W^{(2)})^Tb'.
\]

Integrating the two matrix equations gives `W^(ell)=W_0^(ell)+M_ell`. In particular,

\[
\begin{aligned}
\int_0^s M_2(v)^Tb'(v)\,dv
&=\int_0^s\int_0^v h^1(u)\frac{b'(u)^Tb'(v)}n\,du\,dv\\
&=\int_0^s h^1(u)\frac{b'(u)^T[b(s)-b(u)]}n\,du.
\end{aligned}
\]

Continuity on the compact integration triangle justifies the interchange directly. This verifies the sign, transpose, ordering of arguments, and factor `1/n` in `R_1`. Substitution of the same trained matrices into the forward and backward equations produces all five lines of (13.5), including the upper transpose memory `M_3^T delta^3`. The readout integral contains no `1/n` because its mobility already canceled the output normalization.

For the converse, differentiation of the displayed `R_1` gives no endpoint contribution because `b(s)-b(s)=0`, and gives

\[
R_1'(s)=\left[\int_0^s h^1(u)b'(u)^T/n\,du\right]b'(s)
=M_2(s)^Tb'(s).
\]

Thus `(X^1)'=(W^(2))^Tb'`; the inverse derivative gives `(z^1)'=phi'(z^1) odot (W^(2))^Tb'`. The last line of (13.5) identifies `b'=delta^2`, restoring the first equation of (13.2). The integral derivatives restore both matrix equations and the readout equation. The forward `z^2,z^3` relations and backward `q^2` relation are restored by substitution. The zero primitive and stated consistent initial data restore the original initialization. No convergence of derivatives, second derivative of `b`, or infinite-dimensional interchange is needed.

There are exactly the four claimed initial-matrix actions in the representation: `W_0^(2) h^1`, `(W_0^(2))^T b`, `W_0^(3) h^2`, and `(W_0^(3))^T delta^3`. The lower initial transpose acts on the primitive, while its derivative remains in the evolution equation and trained memories. No trained increment has been discarded.

## 3. All four derivative bounds and the supplied-path mesh

Under (13.6), `c=pi/2` bounds every activation coordinate, and `|phi'|<=1`, `|phi''|<=2`. The backward bounds are

\[
\|\delta^3\|_2/\sqrt n\le B,\quad
\|q^2\|_2/\sqrt n\le B^2,\quad
\|b'\|_2/\sqrt n\le B^2.
\]

The infinity bound on `a` is what controls multiplication by `a` when differentiating `delta^3`. The explicit derivative audit is:

| Quantity | Bound on derivative RMS, or intermediate RMS | Verification |
|---|---|---|
| `h^1` | `B^3` | Two factors of `phi'` have multiplier norm at most one; `W^(2)` contributes `B` and `delta^2` contributes `B^2`. |
| `b` | `B^2` | Its derivative is `delta^2`. |
| `z^2` | `Z_2=c^2 B^2+B^4` | Differentiating `W^(2)h^1` gives `(||h^1||_2^2/n)delta^2+W^(2)(h^1)'`. |
| `h^2` | `Z_2` | Multiplication by `phi'(z^2)` cannot increase the norm. |
| `z^3` | `Z_3=c^2 B+B Z_2` | The same matrix-product differentiation uses `delta^3` in the trained increment. |
| `delta^3` | `c+2B Z_3` | Its derivative is `h^3 odot phi'(z^3)+a odot phi''(z^3) odot (z^3)'`. |

This proves all four table-argument derivative bounds with the stated `C`, independent of width for fixed `B`. Integration in finite Euclidean space proves the claimed RMS Lipschitz bound.

For `S>0`, take `k=ceil(CS/epsilon)` equal subintervals. Their `k+1` endpoints give gaps `S/k<=epsilon/C`; the left mesh projection satisfies `0<=s-pi(s)<=epsilon/C`. For `S=0`, one point suffices. Applying an initial operator to the difference then gives

\[
\|A(v(s)-v(\pi(s)))\|_2/\sqrt n
\le\|A\|_{\rm op}\epsilon\le B\epsilon.
\]

The last inequality uses (13.6) at time zero and equality of transpose operator norms. The same mesh works for all four orientations. This is a width-independent count of sampled arguments per orientation, conditional on the supplied path and bound. It neither reduces vector-coordinate dimension nor eliminates the retained matrix/history memory.

## 4. Retained rank-memory continuity

For (13.10), split the integrand difference as

\[
b'h^T-\widetilde b'\widetilde h^T
=(b'-\widetilde b')h^T+\widetilde b'(h-\widetilde h)^T.
\]

Integration by parts in the first term, with zero initial primitive difference, gives exactly the displayed identity. Since

\[
\|uv^T/n\|_{\rm op}
=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n),
\]

the endpoint, first integral, and second integral contribute `B_h e_b`, `S L_h e_b`, and `S L_b e_h`, respectively. This proves (13.10) including its normalization.

For (13.11), the first split integral has RMS at most `S L_b e_M`. For the second, writing `Delta b=b-tilde b`,

\[
\int_0^s\widetilde M^T\Delta b'\,du
=\widetilde M(s)^T\Delta b(s)
-\int_0^s(\widetilde M')^T\Delta b\,du.
\]

The initial boundary vanishes. The bounds `||tilde M(s)||_op<=S L_b B_h` and `||tilde M'||_op<=L_b B_h` give one contribution `S L_b B_h e_b` each, hence the coefficient two in (13.11). Only bounded primitive derivatives and the asserted regularity are used; convergence of `b'` is not required.

For (13.12), split the upper integrand difference into `(delta^3-tilde delta^3)(h^2)^T+tilde delta^3(h^2-tilde h^2)^T`, divide by `n`, apply the same rank-one formula, and integrate. The two terms are exactly `S B_2` times the backward difference RMS and `S D_3` times the activation difference RMS. The claims are continuity on the stated derivative-bounded path class, not unrestricted continuity on arbitrary RMS-bounded paths.

## 5. Explicit missing inferences and examples

Equation (13.13) is the difference of the two defining primitive equations `b'=phi'(z^2) odot q^2` with the same zero initial primitive. It is used for compared equation paths; the earlier standalone memory lemma can also accept more general path pairs. Its first summand is bounded by the `q^2` difference RMS. For the second summand, on `|tilde q^2|<=Q` the mean value bound gives `2Q` times the `z^2` difference RMS; on the complement `|phi'(z)-phi'(tilde z)|<=2` gives twice the tail RMS. Thus (13.14) is valid; using a sharper constant on the tail is unnecessary.

All three obstruction examples check exactly:

1. `sqrt(n)e_1` has RMS one. If `n>Q^2`, its entire RMS lies above threshold `Q`. With `z=e_1`, `tilde z=0`, arctangent derivatives differ by `-1/2` on the first coordinate, so the product with `sqrt(n)e_1` has RMS `1/2` although the input difference RMS is `1/sqrt(n)`. This defeats an estimate based only on those norms.
2. The paths `s e_j` in `ell^2` have Lipschitz constant one and norm at most `S`. At any fixed `s>0`, distinct paths are separated by `sqrt(2)s`, excluding a strongly convergent subsequence there. Temporal regularity does not supply spatial compactness.
3. `(1/j)sin(js)v` converges uniformly to zero, but its derivative is `cos(js)v`, whose squared time-`L^2` norm is `||v||^2[S/2+sin(2jS)/(4j)]`. For `S>0` this tends to `S||v||^2/2`, so derivative convergence does not follow even with uniformly bounded derivatives.

Identity (13.15) follows immediately by differentiating the initial integrated response and using `b'=delta^2`. It exposes the derivative needed for the lower backward response. The derivative example therefore correctly blocks a generic inference from uniform integrated-response approximation to hidden-velocity or raw first-kernel convergence. It does not assert that the example is a canonical training trajectory.

The supplied samples were generated using intervening unretained actions. Their measurability from only retained responses is not established. Consequently (13.9) cannot by itself justify adaptive Gaussian conditioning, a causal finite-query program, stability of changed equations, or convergence of their solutions. The text retains these distinctions explicitly, including cap removal and autonomous population restart.

## 6. Complete finite-dynamics dependency audit

The chain-rule gradients in its (1) carry `1/(n sqrt(d))` in the first block, `1/n` in each middle block, and `1/n` in the readout. The stipulated mobilities therefore produce its physical flow (2). The Frobenius rank-one pairing gives kernel blocks (3) with first factor `kappa_1 G_ab`, two normalized pairings for middle blocks, and one normalized activation pairing for the readout. Residuals occur in neither backward vectors nor kernels.

The weighted-gradient representation makes each kernel positive semidefinite. Differentiating the mean full-square loss yields `-4 r^T K r/m^2`; substituting the flow gives precisely the negative weighted squared speed. Its integrated block denominators are `n kappa_1`, `kappa_ell`, and `n kappa_(L+1)`.

The finite state vector field is locally Lipschitz because the loss is `C^2`. On a finite maximal interval, nonnegative loss and the energy identity imply the displacement bound `sqrt((t-s)L_n(0))` in the fixed positive weighted Euclidean metric. This makes the path Cauchy at any finite endpoint. The finite endpoint limit and the same local contraction construction extend the solution, excluding finite-time blowup. No bounded activation, coercivity, or GD stability assumption is silently needed.

The block displacement factors in (7) follow by multiplying the weighted bounds by the square roots of their mobilities. Bounded initial normalized first Frobenius norm, readout RMS, middle operator norms, and initial loss give their finite-horizon bounds. Forward induction uses bounded activation derivatives and `|phi(z)|<=|phi(0)|+b|z|`; reverse induction uses multiplier bounds and middle operator norms. Cauchy–Schwarz then controls every kernel entry. Constants may depend on fixed depth, data, and horizon.

For the stated Gaussian initial event, first-block squared normalized Frobenius norm has mean `d` and variance `2d/n`, hence converges to `d`; stored-readout squared RMS has expectation `n^{-2}`, hence tends to zero in probability. A maximal separated `1/4`-net of the unit sphere has at most `9^n` points by disjoint radius-`1/8` balls inside radius `9/8`. Approximating the two unit vectors in a bilinear form incurs at most half the operator norm, giving the factor two. Each net bilinear form has Gaussian variance `1/n`, whose exponential-moment tail gives `2 exp(-n M^2/8)` at threshold `M/2`. Union over the two nets gives exactly `2 9^{2n} exp(-n M^2/8)`. A fixed sufficiently large `M` and fixed depth give probability tending to one. The initial forward and readout bounds then bound the initial loss. This dependency does not provide the additional infinity-bound or stability conclusions excluded in the primary chapter.

## Findings and claim ledger

| Claim | Status in supplied scope | Required correction |
|---|---|---|
| Canonical normalization, initialization, and conditional clock relation | Exact | None |
| Finite integrated representation and converse | Proved | None |
| Four query derivative/RMS bounds and supplied-path time cover | Proved under (13.6) | None |
| Lower and upper rank-memory estimates | Proved under the stated path bounds | None |
| Three general obstruction examples and derivative identity | Exact | None |
| Finite-dynamics dependency | Proved within its stated finite-width scope | None |
| Causal finite-query construction and valid adaptive conditioning | Not established; explicitly retained as a gap | No such claim made |
| Stability, state limits, raw kernel convergence, cap removal, population restart | Not established by this chapter; explicitly retained as gaps | No such claim made |

No fatal, major, conditional, or minor issue requiring a change was identified. **CLEAN applies to this complete frozen version and its actual scoped claims, not to any of the open stronger conclusions.**
