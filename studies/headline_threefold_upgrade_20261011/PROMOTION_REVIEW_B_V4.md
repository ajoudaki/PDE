# Scientific promotion review B, version 4 — PARTIAL / NOT COMPLETE

Reviewer: `/root/promotion_science_b_v4`, distinct from the named authors,
assemblers and selector. This context received the neutral assignment and no
inherited author discussion, study history or earlier verdict. I read only the
assigned frozen scientific inputs and required process/skill instructions.
The only subsequent supervisor message withdrew this packet because of a
reported rendering defect. I have not inspected another review or version.

**No PASS is issued.** The supervisor withdrew version 4 before this review
was completed and instructed me to stop, preserve the packet, and record
actual coverage. This report cannot satisfy either complete scientific review
gate, and cannot be reused as acceptance of a corrected packet. No candidate
file was edited. No empirical or maintained-code correctness claim was tested.

## Identity and actual coverage

All paths in the following table are relative to
`data/generated/headline_threefold_upgrade_20261011/promotion_v4/`, except
the assignment. Actual hashes were obtained with `sha256sum`.

| Input | SHA-256 |
|---|---|
| `docs/08b-trajectory-compression.qmd` | `01e5ded8da325cd8dfbfc9c9d9e7545e237b787853df75895c1cf76569c73652` |
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `chapter.diff` | `e7e55eed4956fe0ed2b125418fcd9d5a8e973633d0378d4d03a0cefd361ddef7` |
| `inputs.sha256.json` | `dd8be3766cea93ae71fc34ce4ce26b3793d07a6ce81b10bb631fea24d74e1d52` |
| `studies/headline_threefold_upgrade_20261011/PROMOTION_REVIEW_ASSIGNMENT_V4.md` (repository relative) | `2d09e6d36784c6a91c8d28541bd9dc159e6f295d12f26e5ddc275e2268aed587` |

The manifest's `proposed/docs/08b-trajectory-compression.qmd` entry matches
the actual candidate. Its different `docs/08b-trajectory-compression.qmd`
entry records the pre-addition input, not the assembled candidate. Index
and notation hashes also match their manifest entries.

The complete candidate's 7,954 lines were read, including all unchanged proof
bodies and the nonlinear-learning appendix. Successful untruncated reads cover
1–350, 351–800, 801–1500, 1501–2250, 2251–3000, 3001–3750,
3751–4500, 4501–5250, 5251–6000, 6001–6750, 6751–7500 and
7501–7954. An earlier combined output containing lines 1–800 was truncated;
the later 1–350 and 351–800 reads repaired that entire range. The index was
read again in a complete standalone call after an earlier combined result
was truncated. Notation's complete 98 lines were visible. The complete
manifest and assignment were read.

The diff has 3,007 lines. Its initial 1–1000 read was truncated and was **not
repaired before withdrawal**. Lines 1001–3007 were not read. Candidate content
was read independently in full, but diff coverage is incomplete and no
mechanical inverse-diff/provenance reconstruction was performed.

Required process material read: `RESEARCH_WORKFLOW.md` (including a separate
complete read of its promotion requirements), `solve-math-rigorously`, and
`explain-with-canonical-notation` with its complete neural-network reference.
An initial combined workflow output was truncated; the separate 175–320
read restored the promotion portion. I do not claim repaired complete reading
of the unrelated author-startup portion. The assignment is an isolated review,
so no study README or author startup scientific material was read.

Commands actually used were `cat`, bounded `sed -n` reads, `wc -l`, and
`sha256sum` on these frozen inputs and required instructions. Metadata-only
`git rev-parse HEAD` returned
`ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; the assigned report path was absent
from `git status --short`. No numerical test, experiment, renderer or code
audit was run. No scratch script was created.

## Mathematical work completed before withdrawal

The following are actual analytical checks, not component acceptance verdicts.
Their dependencies were read but the complete adversarial reconstruction and
persisted proof audit required by the assignment was still in progress.

1. **Model and domains.** I checked the normalization of the gradient blocks
   against the mean squared loss and mobilities `(n,1,...,1,n)`. The stored
   readout starts at exactly zero. The Legendre/Harmonic comparison covers the
   sphere, while Taylor covers only inputs declared in advance. The finite
   lower bound is witnessed at training inputs at positive time; it does not
   purport to separate fitted training endpoints. The additional nonlinear
   feature certificates impose nonaffineness and nonparallel inputs separately.

2. **Fitting and signed stability.** With `lambda=gamma/m` and residual RMS
   `rho`, the stopped readout Gram gives
   `-d(rho^2)/dt >= lambda*rho^2`. Combining
   `integral ||theta_dot||^2/rho <= 2 rho(t)` with
   `integral rho <= 2 rho(t)/lambda` gives the stated finite parameter length.
   For the signed comparison, subtracting the two flows retains the negative
   term `-2 ||r-r'||_m^2`; Taylor remainders contribute at most
   `K(rho'+3 rho)e^2`. This checks the displayed cancellation, not merely an
   unsigned Lipschitz estimate.

3. **Finite covariance and lower comparison.** The initialization calculation
   uses Gaussian RMS concentration and polarization, then scalar marginal and
   covariance recurrences; it does not invert singular intermediate covariance
   matrices. I checked the two spectral inequalities in the squared-area
   innovation argument. In the finite lower proof, conditioning on the first
   run through layer `L-1` and the entire other run leaves conditional iid final
   rows and a measurable shift. The Fourier Gaussian majorant is shift-uniform.
   Applying the derivative-to-trajectory estimate contributes the time radius
   and the square of the truncation degree, hence the stated logarithmic
   power `5/2`. I checked that the final ratio exponents are `15/64` for the
   improved Legendre bound and `1/2` before log absorption for Taylor.

4. **Source probability and geometry.** I followed the normalized cavity ports,
   the frozen-control linear/quadratic Gaussian tests, retained-measurable
   endpoint grid, four nonzero traces, and the distinct-root moment argument.
   For the finite panel, the second radius cap controls the complex-minus-real
   correction at fixed moment exponent; high moment order is used for the
   much smaller singleton/common-cavity differences. This is the mechanism
   that must prevent a confidence-dependent exponential width. The complete
   numerical inequalities in that finite ledger had not all been independently
   verified when the packet was withdrawn.

5. **Third-order Legendre defect.** Subtracting the accumulated physical feature
   defect defines a history `g` with `partial_tau g=a` and
   `partial_tau^2 g=a_dot/rho_hat`. The initial readout zero makes the first
   derivative vanish at the constant-prefix join. The remaining activity bound
   `(A-tau)/rho_hat <= 4/lambda` removes the terminal denominator in the
   weighted Legendre operator. Its spectral eigenvalues `j(j+1)` give a
   forward tail of order `q^-2`; pairing it with the backward `q^-1` tail
   gives the displayed third-order defect. I checked the bootstrap scaling
   `n^(1/64)/q^3 <= n^(-47/64)` and the subsequent ratio-log absorption.

6. **Selected geometry and endpoints.** I checked that the displayed metric
   obeys `P^T M P=I` on the source basis and that both directions of the
   initialized mixer are paired in this metric. The corrected readout enforces
   the training prediction equation exactly; its gates are not silently treated
   as self-adjoint in `M`. The cancellation in the variable `zeta=z_readout+T_C e`
   removes `2 V_C e`, using `T_C Q_C=V_C`. Both fitted tails are included in
   the all-time error transfer.

7. **Numerical source routine.** I followed the real signed defect inequality,
   moving complex balls, activation interpolation/aliasing and Cauchy derivative
   bounds, local contraction, and induction over restarted polynomial panels.
   The path is continuous at panel joins and its total integrated defect enters
   the real stability bound. Its four-term source error split distinguishes
   Taylor truncation, activation substitution, parameter truncation and global
   path error. These are finite exact-real algorithms, with no original high
   activation derivative oracle. Their complete constants still needed final
   independent checking.

8. **Source construction and setup coupling.** Taylor uses real interpolation
   nodes on the capped source cover; Harmonic accumulates global coefficients
   using positive quadrature rather than retaining separate local-panel blocks.
   Forming images after the base linear combination establishes exact pairing.
   The Gaussian sampler's conditional kernel is
   `A+(I-UU^T)G(I-VV^T)` with
   `A=YV^T+UR^T(I-VV^T)`. A new forward unit direction `e` splits the residual
   into its action on `e` and a residual on the orthogonal complement; their
   cross covariance is zero. The transpose split is the same calculation on
   the other side. This establishes the stated algebraic invariants and handles
   zero/dependent queries and exhausted opposite rank without a Gram inverse.
   The completed fresh matrices are proof objects. This does not give a method
   for querying an arbitrary supplied realization in subquadratic work.

9. **Operation inventory.** I followed all four initialized-matrix access
   classes, including final basis images beyond paired source images. Grouping
   each numerical endpoint increment into `mK` factors explains the accumulated
   factor cost. The selector's `nr^3` term is present. Substituting the stated
   fixed-parameter orders gives implicit Taylor work `n log(en)^5` from three
   separate terms: sampler, previous-factor actions and activation composition.
   Implicit Harmonic is dominated by `nr^3`, with exponent `9d/2+3`. The exact
   full parameter formulas were read, but an exhaustive independent operation
   and peak-allocation check had not been completed.

## Component status and unresolved work

| Component | Status at withdrawal |
|---|---|
| Polynomial Legendre width | PARTIAL — final finite-source and coefficient audit incomplete |
| Polynomial Taylor width | PARTIAL — same source audit and complete retained-count audit incomplete |
| Harmonic supplied-dense setup | PARTIAL — numerical constants and full arithmetic/memory audit incomplete |
| Taylor supplied-dense setup | PARTIAL — same; compatibility passages read and partially checked |
| Harmonic fresh-implicit setup | PARTIAL — sampler algebra reconstructed; full client audit incomplete |
| Taylor fresh-implicit setup | PARTIAL — sampler algebra reconstructed; full client audit incomplete |
| Diff/provenance coverage | INCOMPLETE — truncated first diff block and unread remainder |
| Overall scientific promotion gate | NOT COMPLETE; no acceptance recommendation |

No claim was independently refuted during this partial audit. This is not an
assertion that the candidate is correct or free of gaps. The required complete
audit, final adversarial checks and component verdicts remain undone.

The supervisor reported four native section references rendering as “Section .”
under the existing unnumbered book configuration and withdrew the candidate to
replace them with titled anchor links. I did not reproduce or locate that
rendering defect and do not treat the supervisor's report as my own evidence.
No later packet may inherit a scientific PASS from this report.
