# Independent complete review A1

**Verdict: REQUIRED CORRECTION — not CLEAN.** I found one explicit canonical-notation violation. I found no mathematical error in the exact representation, converse, conditional derivative estimates, supplied-path time cover, memory-continuity bounds, or scoped obstruction examples. No stronger causal, limit, stability, or kernel-convergence theorem is established or asserted by those results.

## Scope and full-read ledger

The review used only the supplied `/tmp/pde_query_review_1` input bundle and the required skill instructions. I did not inspect the checkout, studies, history, prior reviews, other tasks, or outside mathematical sources. I did not delegate, run experiments, or integrate trajectories. All mathematical checks below are deterministic derivations.

Read in full:

| Input | Lines read | Bytes | SHA-256 before review |
|---|---:|---:|---|
| `docs/NOTATION.md` | 1–98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 1–214 | 8355 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/integrated_queries.md` | 1–242 | 10322 | `24fd4516debfee2bba468b1782559ead07c4ffee3c90c10585cf60aca3e08d6d` |

Total: all 554 supplied source lines. The complete finite-dynamics dependency was read again separately after a combined display truncated part of that file. The manifest `INPUTS.json` was read in full; its SHA-256 is `6017a21158164007de63e9208263e8de42fdca9392fd478bebc72f8337419a58`. Actual source hashes, byte counts, and line counts matched the manifest.

Required instructions read in full:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/SKILL.md`;
- its `references/research-contract.md` and `references/adversarial-audit.md`.

## Required finding

### A1-1. Restore the canonical finite norm and pairing notation

**Location:** `docs/integrated_queries.md`, lines 13–14, and subsequent uses throughout the section.

The section introduces

\[
\langle v,w\rangle_n=v^Tw/n,\qquad \|v\|_n=\|v\|_2/\sqrt n.
\]

This directly conflicts with `docs/NOTATION.md`, lines 59–61: “A finite RMS is `||v||_2/sqrt(n)` and a finite normalized pairing is `u^T v/n`; do not hide these factors in new norm or inner-product symbols.” The notation contract at lines 3–6 also requires chapters to preserve its conventions. The explicit local definition does not remove this conflict with the explicit prohibition.

**Required correction:** delete these two local shorthand definitions and replace their uses by the canonical expressions, including the table-related derivative and approximation bounds, rank-one identity, memory estimates, and counterexample computations. For example, write

\[
R_1(s)=\int_0^s h^1(u)\frac{b'(u)^T[b(s)-b(u)]}{n}\,du,
\qquad
\sup_{s\le S}\frac{\|A[v(s)-v(\pi(s))]\|_2}{\sqrt n}
\le B\varepsilon.
\]

**Severity:** minor as mathematics, but a required correction against the supplied canonical contract. The formulas are mathematically consistent with their local definitions; no change to constants or theorem scope is needed.

## Complete mathematical checks

### Model, initialization, clocks, and dependency

The main section fixes three hidden layers, one datum with scalar input and label one, arctangent activation, and the stored readout `a=W^(4)`. Its mobilities `(n,1,1,n)` specialize the dependency's `(n kappa_1,kappa_2,kappa_3,n kappa_4)` with unit multipliers. For the single full-square loss, the gradient equations in `finite_dynamics.md` (1)–(2) give exactly `-2(f-1)` times (13.2); the first preactivation is the first weight vector because `x=d=1`.

The feature clock is conditional on representing a physical orbit by a feature orbit. The equations justify `ds/dt=-2(f-1)` by the chain rule. They do not claim a globally increasing clock for arbitrary initialization: an increasing clock requires `f<1`, while `f=1` makes the physical velocity zero and `f>1` gives the reverse feature direction. Nothing in the representation is asserted for raw GD after the nonlinear coordinate change.

The Gaussian initialization agrees with the canonical stored-readout variance `n^(-2)`. The identities hold for arbitrary consistent deterministic initial values on a supplied finite `C^1` feature solution. Lines 39–42 explicitly avoid a new probability assertion for the cap (13.6). In particular, the dependency's physical-time RMS bounds are not silently used to supply the stronger feature-time readout supremum bound.

I also checked the entire finite-dynamics dependency. Backpropagation contributes the required factor `1/n`; contraction of rank-one gradients gives all three raw kernel blocks. Their quadratic forms are squared mobility-weighted gradient norms and are nonnegative. The identities

\[
\dot f=-2Kr/m,
\qquad
\dot{\mathcal L}_n=-4r^TKr/m^2
=-\|D^{-1/2}\dot\theta\|_2^2
\]

give the energy estimate and parameter increments by Cauchy–Schwarz. At fixed width the positive diagonal metric is equivalent to Euclidean distance, so a finite maximal endpoint would have a finite Cauchy limit and the locally Lipschitz vector field could be restarted there. This proves the stated physical gradient-flow existence. Bounded activation derivatives then give the claimed forward/backward RMS inductions and kernel-entry bounds on fixed physical horizons.

The dependency's Gaussian initialization argument is also consistent. The first squared Frobenius RMS has mean `d` and variance `2d/n`; the stored-readout squared RMS has mean `n^(-2)`. These facts alone give the respective convergence-in-probability bounds by Chebyshev and Markov. For a middle matrix, a maximal `1/4`-separated sphere set covers the sphere and has at most `9^n` points: its disjoint radius-`1/8` balls fit in a radius-`9/8` ball. Approximating both unit vectors in a bilinear form incurs error at most half the operator norm, so the norm is at most twice the largest net form. Each fixed form has Gaussian variance `1/n`; its exponential-moment bound is `P(|Z|>u)<=2 exp(-nu^2/2)`. Taking `u=M/2` and a union bound over the at most `9^(2n)` pairs gives exactly the displayed probability estimate. Fixed depth permits a further finite union bound. None of these dependency results identifies a width limit.

### Exact integrated representation and converse

For arctangent, `F'(z)=1+z^2=1/phi'(z)>0`, and `F(z)=z+z^3/3` tends to the corresponding signed infinities. It is therefore a bijection of the real line, with differentiable inverse whose derivative is `phi'(F^(-1)(X))`.

Since `b'=delta^2`, cancellation of the first activation derivative gives

\[
(X^1)'=(W^{(2)})^Tb'.
\]

Integrating the two middle equations gives `W^(ell)=W_0^(ell)+M_ell`. Substitution into the preceding equation gives

\[
\int_0^s M_2(v)^Tb'(v)\,dv
=\int_0^s\int_0^v
h^1(u)\frac{b'(u)^Tb'(v)}n\,du\,dv
=\int_0^s h^1(u)\frac{b'(u)^T[b(s)-b(u)]}n\,du.
\]

The integrand is continuous on a compact finite-dimensional triangle, so the change of integration order is justified. This proves (13.4), including its sign and normalization. Multiplying each matrix increment by its forward or transpose query proves all of (13.5).

For the converse, differentiating `R_1` gives no upper-endpoint contribution because `b(s)-b(s)=0`. Its remaining derivative is `M_2(s)^Tb'(s)`. Hence `(X^1)'=(W^(2))^Tb'`, and the inverse chain rule gives `(z^1)'=phi'(z^1) odot (W^(2))^T delta^2=delta^1`. The integral definitions give the other two matrix velocities and `a'=h^3`. The forward identities and the transpose expression for `q^2` reconstruct all of (13.1). The stated zero primitive and initial data supply the correct initial conditions. There is no missing integration constant or missing transpose action.

The four initial actions are exactly `W_0^(2) h^1`, `(W_0^(2))^T b`, `W_0^(3) h^2`, and `(W_0^(3))^T delta^3`. Replacing the lower transpose argument by its primitive does not remove `b'=delta^2` from the dynamics or eliminate either trained matrix memory.

### Four query derivatives and time cover

Under (13.6), multiplication by `phi'` has operator norm at most one, each activation RMS is at most `c=pi/2`, and the readout RMS is at most its supremum norm `B`. Therefore the RMS bounds for `delta^3`, `q^2`, and `b'` are respectively `B`, `B^2`, and `B^2`.

The chain and product rules give every line of (13.7). In ordinary Euclidean notation their bounds are

\[
\begin{aligned}
\|(h^1)'\|_2/\sqrt n&\le B^3,\\
\|(z^2)'\|_2/\sqrt n&\le c^2B^2+B^4=Z_2,\\
\|(h^2)'\|_2/\sqrt n&\le Z_2,\\
\|(z^3)'\|_2/\sqrt n&\le c^2B+BZ_2=Z_3,\\
\|(\delta^3)'\|_2/\sqrt n&\le c+2BZ_3.
\end{aligned}
\]

The last estimate uses the stated supremum cap on `a` when multiplying `phi''(z^3) (z^3)'`; an RMS readout cap would not justify it. Together with the separate `b'` estimate, these bound all four query derivatives by the specified `C`. Integrating the derivative proves the time Lipschitz estimate.

For `S>0`, set `p=ceil(CS/epsilon)` and take the uniform mesh `s_j=jS/p`, `0<=j<=p`. It contains exactly `1+p` points and has gaps at most `epsilon/C`. For `S=0`, use just zero. Taking the latest mesh point at or before `s` gives the argument error at most `epsilon` in RMS; multiplying by the initial matrix bounds it by `B epsilon`. The initial operator bound follows by evaluating (13.6) at zero, and transpose preserves operator norm. This proves the count and (13.9), conditional on fixed `B,S,epsilon`, with no width-dependent factor.

The conclusion concerns four initial responses along a supplied exact path. It keeps the full trained memories. It provides neither a bound on total stored scalar information nor an autonomous procedure for producing the mesh arguments.

### Rank-memory estimates

Write `d=b-tilde b` and `g=h-tilde h`. The zero primitives make the initial endpoint vanish in

\[
M-\widetilde M
=d(s)h(s)^T/n-\int_0^s d(h')^T/n\,du
+\int_0^s\widetilde b'g^T/n\,du.
\]

The exact rank-one operator norm is `||v||_2 ||w||_2/n`, obtained from Cauchy–Schwarz and equality on the direction of a nonzero `w` (with the zero cases immediate). The endpoint, first integral, and second integral are bounded by `B_h e_b`, `S L_h e_b`, and `S L_b e_h`. This proves (13.10).

For the second memory, the first split term is at most `S L_b e_M`. Integrating the second by parts gives

\[
\widetilde M(s)^Td(s)
-\int_0^s(\widetilde M')^Td\,du.
\]

The endpoint is at most `S L_b B_h e_b`, and the integral has the same bound because `||tilde M'||_op<=L_b B_h`. Their sum proves (13.11), including its factor two. This requires bounded primitive derivatives and the stated `h` regularity, but does not require convergence of primitive derivatives.

For top memory, split the difference of its rank-one integrands as

\[
(\delta^3-\widetilde\delta^3)(h^2)^T/n
+\widetilde\delta^3(h^2-\widetilde h^2)^T/n.
\]

Its integrated operator bound is precisely (13.12). These are continuity estimates for supplied paths satisfying the stated bounds, not solution stability estimates for modified integral equations.

### Scope, examples, and unproved bridges

For two paths satisfying the displayed primitive evolution with the same initial primitive, subtraction and integration give (13.13). On the coordinates where `|tilde q^2|<=Q`, the mean value bound `|phi'(z)-phi'(tilde z)|<=2|z-tilde z|` yields the first term of (13.14). On the remaining coordinates, the bound by two on the difference of derivatives yields its tail term.

The stated examples have the advertised values:

- `sqrt(n)e_1` has RMS one, and its tail RMS remains one whenever `n>Q^2`.
- `z=e_1`, `tilde z=0`, `tilde q=sqrt(n)e_1` give product RMS `1/2`, because `phi'(1)-phi'(0)=-1/2`, while the preactivation difference has RMS `1/sqrt(n)`.
- In `ell^2`, the curves `s e_j` are bounded by `S` and have Lipschitz constant one, yet distinct values at any fixed positive time have distance `sqrt(2)s`. They have no strongly convergent subsequence there.
- The curves `j^(-1) sin(js)v` converge uniformly to zero and have bounded derivatives `cos(js)v`; integrating `cos^2(js)` gives exactly `S/2+sin(2jS)/(4j)`. Thus the derivative squared time norm tends to `S||v||^2/2` for positive `S`.

The source explicitly scopes the first examples to generic deterministic arrays, rather than states proved reachable from the canonical initialization. It likewise uses the Hilbert and oscillatory examples only to disprove general implications from the available estimates. It does not claim a network counterexample.

Equation (13.15) correctly differentiates the lower integrated initial response and adds the retained trained response. Uniform primitive approximation consequently does not provide the missing derivative or raw first-kernel convergence. The text also correctly leaves query-transcript measurability, Gaussian conditioning of adaptive calls, stability of a self-generated approximation, strong state convergence, cap removal, and autonomous population restart unproved. A finite set of sampled responses taken from the actual trajectory is not asserted to be a causal finite program.

## Integrity conclusion

Post-review source hashes, byte counts, and line counts were rechecked against `INPUTS.json` and matched the before-review ledger exactly. The input bundle was not modified. The only produced artifact is this review, outside the input directory.

Subject to the one required canonical-notation correction A1-1, the supplied main section's mathematical claims and their stated limitations pass this complete isolated review.
