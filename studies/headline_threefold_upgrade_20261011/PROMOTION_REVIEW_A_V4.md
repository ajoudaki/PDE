# Independent scientific review A, version 4 — PARTIAL / NOT COMPLETE

Reviewer: `/root/promotion_science_a_v4`. Date: 2026-10-11.

This is **not a PASS** and cannot satisfy a promotion review gate. The coordinator withdrew version 4 while this review was in progress, reporting that four native section references rendered as “Section .” in the unnumbered PDF configuration. I did not independently inspect that rendering. On receiving the withdrawal I stopped the scientific audit and preserved the frozen inputs. A corrected packet requires a fresh complete review; this context will not review it.

## Isolation and inputs

I started from the neutral version-4 assignment, without author history, prior verdicts, or another reviewer's findings. I read no study README, source notes, candidate-assembly files, other study research, archived book, or unassigned chapter. I did not ask an author for justification. The only subsequent coordinator message was the withdrawal instruction and its rendering explanation. The final Git status check exposed filenames only, as permitted coordination metadata.

Required process inputs read: `RESEARCH_WORKFLOW.md` completely, including Part 2; `/etc/codex/skills/solve-math-rigorously/SKILL.md`; `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`; and its complete `references/neural-response-memory.md`. No external mathematical source or browsing was used.

All paths below are relative to `data/generated/headline_threefold_upgrade_20261011/promotion_v4/`:

| Input | SHA-256 measured by `sha256sum` |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `01e5ded8da325cd8dfbfc9c9d9e7545e237b787853df75895c1cf76569c73652` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `chapter.diff` | `e7e55eed4956fe0ed2b125418fcd9d5a8e973633d0378d4d03a0cefd361ddef7` |
| `inputs.sha256.json` | `dd8be3766cea93ae71fc34ce4ce26b3793d07a6ce81b10bb631fea24d74e1d52` |

The chapter hash matches the manifest's `proposed/docs/08b-trajectory-compression.qmd` entry. The manifest's separate `docs/08b-trajectory-compression.qmd` entry is the established precursor, not the candidate. The index and notation hashes match their corresponding entries. Unassigned files listed in the manifest were not opened or verified.

## Actual read coverage and commands

`wc -l` reported 7,954 chapter lines, 260 index lines, 98 notation lines, and 3,007 diff lines. I read every chapter line, including all unchanged proof bodies and the nonlinear-learning ending, using nontruncated `sed -n` reads of these consecutive intervals:

`1–650`, `651–1350`, `1351–2050`, `2051–2750`, `2751–3500`, `3501–4250`, `4251–5000`, `5001–5750`, `5751–6500`, `6501–7250`, `7251–7954`.

An initial combined process/index/notation read had tool-output truncation. I reread the entire workflow separately and the entire index separately; the full notation text was visible in the initial output. The required skill texts were visible in full. The full manifest was read in a separate call.

Diff reading was incomplete at withdrawal: the `1–1000` read was truncated in the middle, and the follow-up read explicitly recovered `420–590` and read `1001–1450`. I do not certify that the former repaired every omitted diff line. Lines `1451–3007` were not read in diff form. Their candidate scientific content had already been read in the complete chapter, but that does not complete the provenance audit.

Commands were read-only `cat`, `sed -n`, `wc -l`, `sha256sum`, and the final metadata checks `git rev-parse HEAD`, `git status --short`, `git diff --cached --name-only`. HEAD was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; the cached-name listing was empty. No numerical campaign, build, executable mathematical check, or empirical reproduction was run. The only write is this report, through `apply_patch`.

Complete reading is not a claim of complete independent reconstruction. The following are the actual mathematical checks completed before interruption.

## Partial mathematical checks

### Model, events, and comparison contract

I checked the distinction between the exact-zero stored readout here and the shared notation's small-Gaussian readout, and between the physical gradient flow and any discretization. The three models use the coupled actual dense run. Legendre/Harmonic promise the sphere; Taylor promises only inputs declared before initialization. The denominator is a complete-trajectory supremum with a positive-time training witness, not an endpoint denominator. The fitted endpoints at training inputs agree. No finite-real-coordinate inventory implies a bit bound.

The normalized gradient blocks in the fitting and numerical proofs have factors `1/sqrt(n)`, `1/n`, `1/sqrt(n)` for first matrix, hidden matrices, and stored readout. Their squared gradient-flow norm is the negative derivative of residual mean square. A Gram gap `lambda/4`, with `lambda=gamma/m`, yields residual decay at rate `lambda/2` for the dense trajectory and the parameter-tail bound used later. I checked that zero residual is treated by stationary continuation, rather than division through zero.

### Finite lower bound

I reconstructed the conditional scalar argument in `sec-compression-polynomial-dense-lower`. If a conditional feature vector has Gram at least `g I`, the squared-area calculation gives

\[
V\ge \frac{(m-1)g^3(\operatorname{tr}\bar Q-g)}{4\mathbb E\|U\|^4}\|y\|^2,
\quad V=\mathbb E\|U(U^\top y)-\bar Qy\|^2.
\]

Taking `g=gamma/2`, `tr(bar Q)>=mg`, and `E||U||^4<=m^2 X^16` gives a coordinate variance at least `Y^2 gamma^4/(256 X^16)`, including `m=2`. Conditioning also on the entire second run makes that run a measurable shift; it does not demand a limit theorem for earlier-layer fluctuations.

For the stated small-ball inequality, setting `h=tau sigma_0/24` gives exponential rate at least

\[
\frac{n\tau^2\sigma_0^6}{8192 M_3^2}.
\]

The displayed bound `M_3^2/sigma_0^6<=2^30 m^6 X^96 gamma^-12` and the `2^44` width gate cover this rate. The derivative-to-trajectory conversion introduces the short analytic radius and the factor `ell_n^-2` from a Chebyshev derivative estimate. It therefore produces `Y/(sqrt(n) ell_n^(5/2))`, not a lower bound at every time. No error was established in this checked chain, conditional on its source/covariance premises.

### Legendre refinement

I checked the central proposed gain in `sec-compression-polynomial-legendre`: subtracting the integrated physical feature defect defines `g` with activity-clock derivative equal to the ordinary feature velocity divided by residual RMS. The zero initial readout makes this derivative zero at the constant-prefix join. The weighted Legendre operator then avoids a derivative jump there, and `(A-tau(t))/rho_hat(t)<=4/lambda` controls the terminal factor in its second derivative.

Consequently the proposed structure is a forward tail `O(Y P ell_n/q^2)+O(P d_T)` and a backward tail `O(Y P ell_n/q)+O(P ell_n D_T)`. The growing-projection identity gives the product bound on integrated physical defect. Under the stated bootstrap and `q<=sqrt(n)`, absorption yields order `q^-3`. Combining it with a signed-stability factor `n^(1/64)` and `q>=n^(1/4)` gives the displayed `n^(-47/64)` error and relative exponent `-15/64`. The subsequent logarithmic absorption gives the polynomial inverse-tolerance gate. This check did not fully certify every derivative coefficient or the finite source event on which those bounds depend.

### Taylor domain and storage

I checked the algebra by which the cap preserves the retained-count order: the reciprocal radius contributes `(Y/lambda)^2 sqrt(ell_n)` and `lambda^-1 log(e+ell_n)`, using `S^2=256(Y/lambda)^2` and `(log(e+ell_n))^(3/2)<=4 sqrt(ell_n)`. Multiplying by a source degree of order `ell_n` and squaring preserves the two advertised terms, including `(Y/lambda)^4 ell_n^3`. The input-span reduction preserves all declared normalized input inner products and needs no inverse input Gram. The inverse-label gate is attached to simplifying the source degree, not to the underlying normalized source probability assertion.

### Numerical source and Gaussian execution

I traced the proposed restart proof: approximation uses real activation values to build scalar polynomials, an analytic neighborhood supplies a Lipschitz bound, the local polynomial-field solution is compared to its Taylor truncation, and signed physical stability controls the accumulated defect. The next restart uses the proved prefix error. Source comparison splits into truncation, activation substitution, parameter truncation, and global parameter errors. Exact initialized images are formed from approximate base vectors, so pairing is algebraic rather than approximate.

For the Gaussian sampler, I checked the conditional mean

\[
A=YV^\top+UR^\top(I-VV^\top)
\]

and residual law `(I-UU^top)G(I-VV^top)`. A new forward orthogonal direction has mean `UR^top e` and covariance `(I-UU^top)/n`; the transpose rule is its counterpart. Orthogonal Gaussian residual projections have zero cross-covariance. Dependent queries return stored linear combinations, and full opposite rank removes the innovation. These observations support the stated conditional-law induction for adapted, interleaved layer queries. They do not identify the fresh reference with an arbitrary supplied matrix.

I also traced the four initialized hidden-matrix access classes: exact initialized training forward passes; numerical constant-anchor coefficient actions; initialized images of completed sources; and final source-basis images. The trained anchor factors represent the finite numerical continuation, not the exact continuous dense trajectory. The ledgers expressly charge their growing factors and the `nr^3` selector. With the stated orders, the dominant Taylor implicit terms each have exponent `ell_n^5`; the Harmonic selector gives `ell_n^(9d/2+3)`. This remains a partial ledger audit: every constant, scratch lifetime, scalar geometry term, and source-probability premise was not independently certified before withdrawal.

## Component status and remaining work

| Component | Status at withdrawal |
|---|---|
| Frozen chapter and dependency reading | Complete, 7,954 lines |
| Index and notation reading | Complete |
| Diff/provenance audit | Partial |
| Finite source probability and every recurrence constant | Partial; no certification |
| Dense lower estimate | Central derivation checked; dependent-event certification incomplete |
| Third-order Legendre argument | Structural reconstruction checked; full coefficient audit incomplete |
| Capped Taylor geometry and rank order | Structural algebra checked; full probability audit incomplete |
| Activation approximation, restart induction and source error | Read and traced; full audit incomplete |
| Two-direction Gaussian law | Conditional algebra and degenerate-direction cases checked; no executed test |
| Four complete work/peak-memory bounds | Partial substitution and access audit |
| Existing nonlinear-feature certificates | Fully read; not independently fully reconstructed |
| Overall scientific promotion verdict | **PARTIAL / NOT COMPLETE — no PASS** |

No mathematical counterexample or definitive scientific error was established before withdrawal. This is an account of work actually completed, not an inference of correctness from failure to find a counterexample. In particular the long finite-confidence cavity argument, all exact coefficients and every numerical backend obligation still require a complete independent audit. The reported rendering defect is coordinator-supplied operational information, not a scientific finding of this reviewer. No candidate correction is proposed or applied in this report.
