# Independent promotion relevance and placement selection

Date: 2026-10-11. Role: independent selector, not an author, assembler, or final scientific reviewer. Decision: **accept for assembly, with the scopes below**. This is a relevance and placement decision, not a correctness verdict or authorization to change the established book.

## Input scope and coverage

I read the complete maintained `docs/index.qmd` (260 lines), `docs/notation.qmd` (98 lines), `docs/08b-trajectory-compression.qmd` (5,061 lines), and `docs/_quarto.yml` (68 lines), together with the supervisor's neutral description of the two requested additions. The initial combined tool output was truncated; I repaired it by rereading the complete index and chapter lines 1–600, then read chapter lines 601–1400, 1401–2200, 2201–3000, 3001–3800, 3801–4600, and 4601–5061 without truncation. Targeted numbered reads subsequently fixed the locations quoted below.

I also read `RESEARCH_WORKFLOW.md` completely, including all of Part 2, `solve-math-rigorously/SKILL.md`, `explain-with-canonical-notation/SKILL.md`, and its complete neural-response-memory reference. No study proof, prior verdict, other review, maintained code, other scientific chapter, or archived book passage was read. Repository status was used only for coordination metadata. The unread complement includes all other book chapters and all code, so this is not a whole-book or API overlap audit.

Observed HEAD: `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`. The index was empty and unrelated working changes were present. I made no Git writes and wrote only this report.

SHA-256 of the inspected inputs:

| Input | SHA-256 |
|---|---|
| `docs/index.qmd` | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `docs/08b-trajectory-compression.qmd` | `405c8e0a4d99d8b5bebcb4c13d5534317050aa0a10d33b0476b9d90c9cc5bdf5` |
| `docs/_quarto.yml` | `3a64f59b5923060d7196ffaf7ad8494ec3a6f906c90d2801e86ecdb3027d5a2e` |
| `RESEARCH_WORKFLOW.md` | `e4f53cd7805c278bd652fd6367625e3d738931e9bcbf5406271460af3a14f497` |

## Distinct value, overlap, and accepted scope

Both additions belong to **Part II, “Observable closure and approximation theory,” Chapter 9, “Complete-trajectory compression,” `docs/08b-trajectory-compression.qmd`**. The index and Quarto chapter order agree on this placement. Neither needs a new chapter, part, or change to the global notation contract.

The reference remains the chapter's finite nonlinear gradient flow: normalized inputs, independent Gaussian first and hidden matrices, exactly zero initial stored readout, squared loss averaged over the training samples, and mobilities `(n,1,…,1,n)`. Write `m` for the number of training samples, `d` for the input dimension, `L` for hidden depth, and `n` for width. The chapter's activation bound is `β`; its uncentered last-layer population feature Gram has minimum eigenvalue `γ>0`; and `Y=‖y‖₂/√m` obeys `0<Y≤(γ/m)β^(-30L)`. These assumptions and the actual nonlinear hidden updates must remain unchanged.

**Polynomial sufficient widths.** The current chapter supplies eventual per-width probabilities but explicitly declines polynomial width thresholds. A quantitative theorem for Legendre and Taylor therefore adds distinct value even though it preserves the models, retained-coordinate orders, and asymptotic convergence claim. It makes the dependence on conditioning, data size, confidence, and requested discrepancy tolerance assessable. Harmonic's threshold remains qualitative.

For clarity, let `δ∈(0,1)` be the failure allowance and `ε∈(0,1)` the requested ratio tolerance. The candidate must state which polynomial width condition ensures

\[
\Pr\!\left\{
\frac{\|f_{\rm model}-f_n\|_{\mathcal X}}
     {\|f_n-\widetilde f_n\|_{\mathcal X}}\le\varepsilon
\right\}\ge1-\delta,
\qquad
\|g\|_{\mathcal X}=\sup_{t\in[0,\infty]}\sup_{x\in\mathcal X}|g(t,x)|.
\]

Here `f_n` is the coupled ordinary dense flow, `f̃_n` an independent dense flow, and the fitted endpoint is included. Missing limits or a zero denominator retain the existing failure convention. Legendre uses the whole sphere; Taylor uses the training inputs and `p` passive inputs declared before initialization. The advertised polynomial variables are `β^L,m,d,γ⁻¹,δ⁻¹,ε⁻¹`, with `p,Y⁻¹` additionally allowed for Taylor. The candidate must expose polynomial degrees and constants sufficiently to make that dependency claim meaningful; an unspecified problem-dependent constant cannot absorb the parameters whose polynomial dependence is claimed. The same sufficient-width statement must identify which retained-count and absolute-error assertions hold on its event. Taylor retains its `Y/n` absolute bound.

This does not duplicate the existing qualitative assembly. In particular, its current Legendre comparison gives a bound of the form `A/√log(en)` with `A` fixed for a given problem and confidence. Directly forcing that bound below `ε` requires `log(en)≥A²/ε²`, which is exponential in inverse tolerance after inversion. Merely making the existing probability estimates quantitative does not resolve this issue. The complete candidate needs a stronger argument or estimate while preserving the advertised storage. This observation is a statement about the existing bound, not a disproof of the proposed improvement.

**Four initialization complexity variants.** The current initialized-jet compiler establishes finite provenance and expressly provides no preprocessing work or memory bound. The new algorithms therefore answer an existing omission. Accept one shared computational theorem, with four rows, rather than four repetitions of the selected dynamics:

| Dense initialization contract | Selected construction | Preprocessing work | Peak preprocessing memory |
|---|---|---|---|
| Supplied dense realization | Harmonic | `O(n²[log(en)]^(3d/2+1))` | `O(n²)` |
| Supplied dense realization | Taylor | `O(n²[log(en)]^(5/2))` | `O(n²)` |
| Fresh Gaussian draw represented implicitly | Harmonic | `O(n[log(en)]^(9d/2+3))` | `O(n[log(en)]^(3d/2+1))` |
| Fresh Gaussian draw represented implicitly | Taylor | `O(n[log(en)]^5)` | `O(n[log(en)]^(5/2))` |

These are the requested claims, not independently verified conclusions. Their asymptotics fix all problem parameters separately; they are not polynomial complexity bounds jointly in `d`, `m`, or inverse gap. The candidate must separately identify the dependence permitted in its computational constants, the real-arithmetic and Gaussian-sampling primitives, and the cost of activation and high-order derivative evaluation. The existing nonprimitive-evaluator charge cannot silently become a unit-cost oracle assumption.

The input contracts are scientifically different. A supplied realization must be coupled to that realization. A fresh implicit implementation must produce the law of an ordinary dense Gaussian initialization and its compatible reused forward and transpose actions; it does not provide subquadratic access to an arbitrary supplied dense matrix. Both selected runtimes retain the existing corrected nonlinear optimizer, source accuracy, fitting and endpoint bounds, and original query domains. Peak compiler memory and the much smaller final retained state must be accounted for separately.

The efficient schemes perform a high-order numerical rollout through the full finite approximation horizon `T=32(m/γ)log(en)` (or an explicitly justified complete replacement horizon). That work must appear in the theorem and accounting. Their provenance is from initialization and the training data, but their computation is not the existing origin-jet continuation without trajectory stepping. Preserve the latter as a separate alternative. None of these claims supplies finite-bit complexity, practical speedup, cheaper end-to-end training, raw-GD capture, or a pointwise-in-time ratio. No lower bound at the fitted endpoint is added.

**Maintenance and proportionality.** The useful common interfaces already exist: fitting, source approximation, exact initialized-image pairing, sparse metric selection, selected initial arrays, and autonomous runtime. Reusing them limits duplication. The substantive maintenance cost is tracking finite-width probabilities and constants, proving stable high-order rollout, charging coefficient and selection operations, and proving the adaptive Gaussian information contract. Do not add a second copy of the network equations or a second selected-model proof. No code promotion was supplied for selection and none is endorsed here.

## Smallest suitable placement

1. Add a short quantitative-width refinement immediately after `thm-compression-headline`, preserving its identifiers and all three retained-state formulas. Give the explicit Legendre/Taylor width conditions there and retain Harmonic's eventual convention. Put the necessary quantitative estimates beside their existing dependencies: initialization/fitting, real carrier/source control, dense variability, and the Legendre/Taylor constructions. Extend `sec-compression-assembly` with the finite-width probability and ratio argument. Do not label every inherited source or feature-learning statement polynomial unless it is separately proved so.

2. Within `sec-compression-selected-section`, retain `sec-compression-finite-initialized-jets-suffice` and `prp-compression-jets` as the original exact-real provenance alternative. Add one subsection for the shared computational contract and rollout construction. Place the final four-row complexity theorem after the Taylor source construction and before `sec-compression-nonlinear-learning`, where both source counts are available. Its proof can refer to the shared compiler subsection and the two existing source constructions. This is one integrated construction with two sources and two initialization contracts, not four new model sections.

3. Update only the chapter opening, probability convention, headline provenance, compiler transitions, and assembly summary necessary for consistency. The chapter title, Part II ordering, index entry, and global notation need no change. Preserve the nonlinear-feature-learning section's separate extra assumptions and qualitative constants; the new width theorem does not automatically quantify those certificates.

## Exact existing text requiring scope changes

Line numbers below refer to the hashed chapter. Quotes join physical source lines without changing their words.

| Location | Exact existing sentence or clause | Required treatment |
|---|---|---|
| Lines 13–15, chapter opening | “They compare finite neural systems and do not assert a population limit, a raw-GD approximation, a finite-precision guarantee, or efficient preprocessing.” | Remove the blanket denial of preprocessing bounds; state the four exact-real bounds under their actual contracts. Retain the other exclusions. |
| Lines 16–18, chapter opening | “Their theoretical compilers use initialization derivatives; empirical rollout-based implementations have a different setup contract.” | Distinguish the retained initialized-jet compiler from the newly proved rollout compilers. Rollout is no longer described exclusively as empirical. |
| Lines 109–112, constant conventions | “All data, $m,d,L,\gamma,Y$, and activations are fixed separately as $n$ grows.” / “Throughout the stated bounds, $C>0$ depends only on activations and depth, never on $n,m,d,\gamma,Y$ or a passive-panel size.” | Keep these as the asymptotic/storage conventions, but explicitly distinguish the finite-width polynomial quantifiers and the separately fixed-parameter computational constants. Do not reuse `C` with an undisclosed new dependency. |
| Lines 132–134, probability convention | “That threshold may depend on every fixed problem parameter, including the positive $Y$, and is not proved polynomial or practically small.” | Restrict this statement to the remaining qualitative results, especially Harmonic. Insert the Legendre/Taylor refinement and its precise dependencies. Polynomial is not a claim of practical size. |
| Lines 134–137, probability convention | “No simultaneous event over infinitely many independently initialized widths, uniform growing-data limit, or uniform limit as $Y\downarrow0$ is asserted.” | Preserve the absence of a simultaneous infinite-width event. Scope the other disclaimers to what is actually unproved: a quantitative bound may imply parameter-uniform sufficient widths within its admissible range. In particular, do not contradict a Legendre width bound with no inverse-`Y` dependence. Such bounds still do not imply a simultaneous event over all labels or unrestricted growing-data sequences. |
| Lines 139–140, probability convention | “All neural-network statements below inherit this setup and these probability conventions.” | Specify that the quantitative refinement overrides only its named width conventions. Keep unchanged the actual model and failure convention. |
| Lines 196–199, headline | “The theoretical initializers use the dense initialization, training data, and finitely many initialization derivatives; no later trained weight or dense training trajectory is an input.” | Make this explicitly the original initialized-jet alternative. Describe the supplied and fresh-implicit rollout alternatives and their full-horizon preprocessing. Saying that a later state is not an external input does not say that it is never computed. |
| Lines 205–206, headline explanation | “Coordinate counts do not bound precision or preprocessing time.” | Retain the logical distinction, but point to the separate work/memory theorem so this cannot be read as a chapter-wide absence of time bounds. |
| Lines 219–221, proof architecture | “Every dependency of that argument is supplied below; these statements concern exact arithmetic and do not assert efficient preprocessing or empirical performance.” | Separate the original storage proof from the new computational theorem. Keep exact arithmetic and absence of empirical-performance claims explicit. |
| Lines 3973–3975, transfer-to-compiler transition | “The construction itself uses the finite source spaces only through its initial arrays; the separate compiler below will establish their initialization-only provenance for the two methods.” | Refer to the two compiler contracts. The first clause remains the common runtime interface. |
| Lines 4256–4258, Harmonic statement | “Eventually at each fixed confidence, the initialized-jet construction gives a selected nonlinear model with $\|f_{\rm Harm}-f_n\|_{\mathcal X}\le Y/n$ on the whole sphere and total retained real-coordinate count at most” | Retain as the initialized-jet existence statement, or broaden by a precise reference to the new alternatives. Keep Harmonic's qualitative width status. |
| Line 4305, Harmonic proof | “All choices use initialized jets only.” | Label the proof branch as the initialized-jet construction, so this claim does not include the rollout implementations. |
| Lines 4362–4364, Taylor statement | “On the declared $(m+p)$-input panel of [the setup](#sec-compression-setup), eventually at each fixed confidence there is an initialization-only selected model with $\|f_{\rm Taylor}-f_n\|_{\mathcal X}\le Y/n$ and total state at most” | Link the polynomial-width refinement and the separate compiler alternatives. Retain the panel and `Y/n` restrictions. |
| Lines 4419–4421, Taylor proof | “Apply @prp-compression-jets to approximate every scaled base coefficient in Euclidean norm to $\eta/128$, and form its initialized image exactly.” | Keep inside the origin-jet proof branch; provide a separate verified rollout route to the same source contract. Do not present it as the algorithm achieving the new work bounds. |
| Lines 5025–5026, assembly | “The preceding constructions provide the stated retained counts and initialization-only provenance.” | Identify which provenance alternative and which sufficient-width assertion the assembly is using. Add the quantitative probability argument without weakening or replacing the existing full-trajectory norm. |

Several nearby sentences should remain true and need no mathematical weakening. In `prp-compression-jets`, lines 3994–3995 say “No later dense state or trajectory sample is needed; no bound on initialization time or working storage is asserted.” Its proof says at lines 4031–4032 that continuation covers the interval “without stepping a dense trajectory.” These are correct descriptions of that retained alternative, provided it is explicitly separated from the new algorithms. Likewise, Taylor's statement that its *centers and radii* require no later dense training data (lines 4394–4396) concerns a deterministic partition and should not be expanded into a statement about the computation of all coefficients.

The existing Legendre assembly sentence at lines 5040–5043 ending in `$[\log(en)]^{-1/2}$` may remain as a qualitative argument, but must be distinguished from a separate proof of polynomial inverse-tolerance width. The finite-width result cannot cite that sentence as sufficient justification.

## Gate after selection

Assemble the complete candidate in the originating study, including every quantitative probability estimate, numerical-error transfer, operation/memory count, Gaussian-law dependency, and affected summary passage. Supply its complete dependencies and exact cost model to two fresh isolated scientific reviewers, distinct from all authors, assemblers, and this selector. The present task supplied claims and current coverage, not the proposed proofs; their correctness and all four displayed exponents remain unverified here. A missing proof or a changed scientific contract is a named reason to hold the corresponding component at review. The workflow's edition validation, fresh integration review, and approval of the concrete reviewed addition remain necessary before established-file changes.
