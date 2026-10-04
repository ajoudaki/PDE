# Assessment of the explicit width-rate study

2026-10-01. Requested review of this study against the updated manuscript at commit `690e3d4f56ca7ecbad37bb6bacb757b8cfff7682`.

**Verdict: no blocking mathematical defect found in the quantitative extension, relative to the current paper's stated and proved small-label population foundations.** The conservative logarithmic remainder is supported by the proof chain reviewed here. This is an internal mathematical assessment, not promotion approval, a priority claim, or an independent certification of every foundational theorem in the paper.

The result is an explicit asymptotic rate, with problem-dependent constants and an unspecified sufficiently large width threshold. It is not a practical numerical width bound, a polynomial width rate, or an identification of the autonomous fixed-order population dynamics.

## What was checked

The lead reviewer read the complete `RESULT.md`, `PROGRAM_RATE_ROUTE.md`, `PROGRAM_RATE_ADDENDUM.md`, and `DAMPED_TRANSFER.md`, reconstructed their principal inequalities, and then read the existing `PROGRAM_RATE_CHECK.md`. The study README and the complete `WIDTH_OBSTRUCTION_ROUTE.md` were also read. The current manuscript's `results.tex`, `proof_alltime.tex`, and `proof_tracking.tex` were read completely; `main.tex` was read through line 401 for the exact setting and closure, and `NOTES_alltime_theorem.md` was read completely. Other studies and historical research claims were not inputs.

Three fresh scoped reviewers received source assignments without the existing check, README, other reviewers' reports, or other-study material:

| Report | Independently checked scope | Verdict boundary |
| --- | --- | --- |
| [Gaussian review](REVIEW_GAUSSIAN_20261001.md) | Adaptive conditioning in both matrix orientations, noisy-query covariance gaps, iid scalar references, growing-program constants, population bias, empirical contraction and soft-tail tests | No blocker; relies on the current paper's original population carrier tails and common bounded initialized operators |
| [Transfer review](REVIEW_TRANSFER_20261001.md) | Physical proxy reconstruction, exact consistency, current physical carrier tails, activity-damped comparison, original-flow and all-time transfer | No blocker conditional on the quantitative program event, which the Gaussian review addresses |
| [Paper and rate review](REVIEW_PAPER_RATE_20261001.md) | Complete current manuscript and all included theorem/proof/appendix files; assumptions, norms, target, all-order events, passive queries, second-moment test laws, exponent and confidence arithmetic | No blocker conditional on the program and proxy estimates, addressed by the other two reviews |

The lead read all three completed reports and checked that their dependency boundaries agree. These are complementary checks, not three independent complete reconstructions of the entire theorem. No numerical experiment was needed or run. No manuscript or original study proof was edited.

## The mathematical contribution

There are two width errors to control. The paper's parameter-tracking remainder comes from the dense trajectory's integrated backward-carrier tails, through

\[
b_n=C\Phi(a_n),\qquad
\Phi(u)=u\exp\{K\sqrt{\log(e+1/u)}\}.
\]

The prediction remainder additionally includes dense-to-population prediction error. Quantifying only the first term would not prove the displayed population prediction theorem. The study does quantify both.

The quantitative Gaussian argument handles repeated use of the same initialized matrix and its actual transpose. Proof-only independent noise supplies a positive innovation variance even when the original queries coincide or have singular covariance. The inverse covariance bounds grow with instruction count, but are tracked explicitly. Clipping and noise are removed through a comparison with the original population program, whose carrier tails the paper controls. They do not alter the actual trained system.

The essential transfer step is the ordered residual subtraction

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\]

Here the actual dense Gram supplies damping; no proxy Gram gap is needed. The response-change term retains the proxy residual. Integrating gives an amplification controlled by

\[
\exp\!\left(C(1+R)\int_0^T\rho_p(t)\,dt\right),
\]

which is bounded by `C exp(CR)` under the established activity bound. It does not acquire exponential growth in elapsed time. This makes the finite-program approximation useful all the way to the fitted endpoint.

With `K_n=floor(log(e^e+n)^(1/128))`, `N=ceil(C_0 K_n^3)`, `T=O(log K_n)`, and `R=O(sqrt(log K_n))`, the quantitative Gaussian loss is admissible because

\[
N^5=O((\log n)^{15/128})=o(\log n).
\]

The dominant trajectory error is `K_n^(-1+o(1))`; exponential fitting bounds the remaining interval after `T`. The carrier transform costs only another `K_n^{o(1)}`. Uniformly normalized passive-query estimates, followed by Tonelli and Markov, give the finite-second-moment test-law conclusion. The advertised exponent `1/512` has slack at these steps.

The dense-only tail event can be used in the paper's deterministic comparison for every order at once. The proof does not union-bound infinitely many order-dependent events. The test-law event is for each fixed law; it is not one event simultaneously uniform over all laws or all widths.

## Qualifications that matter

1. **Small labels remain essential.** The label RMS must satisfy the paper's problem-dependent smallness threshold. Canonical labels in `{−1,+1}` have RMS one, so the present theorem does not automatically apply to that regime. Rescaling labels changes the system being asserted to fit and must be stated explicitly.
2. **The rate is extremely slow.** Ignoring constants, making `r_n` at most `epsilon` requires `log(e^e+n) >= epsilon^(-512)`. Thus the sufficient width grows like `exp(epsilon^(-512))`. Unknown constants and the width threshold prevent using this as a numerical prescription. It does not justify an `epsilon^(-5/2)` complexity law.
3. **The population target is the dense population predictor.** At fixed order, the current paper establishes subsequential population predictor limits with an order error. It expressly leaves uniqueness and determinism of those limits, and a unique autonomous population moment-state equation, unidentified (`paper/results.tex`, “What the population conclusion identifies”). The new width rate does not close that gap. In particular, at `q=1` the order term does not disappear as width grows.
4. **A high-probability statement is not an unconditional RMS statement.** The study correctly uses a deterministic prediction envelope on the original good event and integrates there. It does not discard exceptional initialization events when claiming an unconditional expectation bound.
5. **The proof depends on the current paper's population foundations.** Uniform carrier tails for the original population Euler programs and bounded common initialized operators with true adjoints are substantive upstream results. The reviews located and examined their supplied arguments; this extension should continue citing them explicitly rather than presenting the quantitative program estimate as valid for arbitrary adaptive programs.

The study's separate linear obstruction gives useful perspective: an unused Gaussian input direction produces a fitted test prediction whose conditional standard deviation is of order `n^(-1/2)`. The lead checked the displayed unused-column argument and the two-hidden-layer balance-law derivation. This supplementary route was not part of the three fresh scoped reviews and is not needed for the logarithmic upper theorem. Its obstruction concerns the population **prediction** error, not the distinct closure-to-dense tracking remainder; it rules out universal `n^(-1)` RMS prediction accuracy, not `n^(-1)` mean squared error. It supplies no general nonlinear root-width upper bound.

## Presentation findings

No mandatory mathematical correction was found. One minor clarification would help: `RESULT.md` says noise is added at “every initialized-matrix query.” The construction treats the first layer as exact iid Gaussian row roots; the noisy calls are the square hidden initialized matrices and their transposes. The addendum already makes this distinction correctly.

The sharper consistency factor `(T+1+R)xi` in `RESULT.md` is justified by Addendum equations (A28)–(A35). The weaker `(1+T)(1+R)eta` in `DAMPED_TRANSFER.md` is compatible with it, not a contradiction. The review initially checked this possible discrepancy and resolved it from the source derivation.

## Source snapshot

All primary proof hashes were unchanged at completion of the three scoped reviews and the lead's final source check. Full paper hashes and exact per-review reading coverage are recorded in those reports.

```text
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
8050f8ff34f00e1263e422d8b8a51bba85be4ae216cec5bd66299b7b2454c267  RESULT.md
d6c7683057b03f710f73be4922a4411ad514bb3e508d3f17678c411a58a0547a  PROGRAM_RATE_ROUTE.md
a11c6e70204a0202da18075afc6565f6e46205de08865cdbcc5c5c38fccd43b7  PROGRAM_RATE_ADDENDUM.md
27ee61e6aa1367329e0baf3e1ae41993ead53f323ba98af2942a1f034bd3a96c  DAMPED_TRANSFER.md
27a371294f84fa73c4e7530c89d0a01160c013b3b8b9668a38a15914b7bdbb3d  PROGRAM_RATE_CHECK.md
fb042f21717b6cd677770cb82d318d3f502b2869721fea22d7ee56c36deb4bc9  WIDTH_OBSTRUCTION_ROUTE.md
```
