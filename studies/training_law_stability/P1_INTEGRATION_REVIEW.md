# Independent integration review of frozen P1

Decision: **not accepted as the exact frozen integration**. Two local notation corrections are required below. Neither is a counterexample to the theorem. I found no substantive mathematical gap in the new proof under its stated model and local scope. The standalone validator passed, and an independent binary reconstruction and output-hash audit passed.

## Identity, isolation, and authority

Reviewer: `/root/integration_review`, a fresh agent distinct from the authors/assembler `/root`, `/root/transport`, `/root/population`, `/root/nonlazy`, the selector, and the scientific reviewers. This report is my original assessment. I read the neutral assignment before the inputs, did not read any study README, research history, relevance report, scientific review, prior verdict, or another reviewer's findings, and had no contact with another reviewer. I did not run author startup or use an earlier acceptance as evidence. I made no Git, candidate, live-book, or maintained-code writes.

The only reviewer writes are this report and `data/generated/training_law_stability/integration_review/`. The computation was the authorized standalone document validator plus a standard-library preservation audit. It performed no training or numerical experiment. No live-source verification beyond the frozen material is claimed.

I read the complete `solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and the latter's `references/adversarial-audit.md`. I applied their proof, hypothesis, topology, limit-order, and adverse-alternative checks. No external theorem was needed beyond the complete supplied mathematical dependencies and elementary results whose needed arguments are given there. Unchanged literature-orientation links were not followed or used as proof evidence.

## Inputs and exact reading coverage

No required input was missing.

I read semantically, in full:

- `P1_INTEGRATION_ASSIGNMENT.md`, `P1_MANIFEST.json`, all five old/new entries of `P1_GLOBAL_EDITS.json`, and `P1_VALIDATION.md`.
- `P1_ADDITION.md`, lines 1–1416, including every theorem assertion and all four complete proof units.
- `P1_DEPENDENCIES.md`, lines 1–1310. This includes the entire notation contract; special-data III.F.1–III.F.9, with singular-query regularization, source-response formulas, common actions/adjoints, Hilbert–Schmidt increments, and strong chain rule; global-nonlinear A.1–A.2; the full weighted response proof C.2; and finite-dynamics §§1–4.
- Both complete reading guides: `P1_DOCS_README.md`, lines 1–269, and `P1_README_BASELINE.md`, lines 1–265.
- `validate_promotion.py`, all 105 lines, and the complete original and fresh `edition/validation.json` files.

Older chapter semantic reading was baseline lines **1–180, 1799–1834, and 2449–3829**, as assigned, plus **1835–1858** through the complete frozen A.1–A.2 body. Thus the union actually reviewed is **1–180, 1799–1858, 2449–3829**. C.1, C.2 and C.3 were read in full. The C.2 excerpt was checked against its baseline range by the independent audit; its body agrees exactly after separator blank-line normalization.

The precise older complement without substantive proof reading is baseline **181–1798 and 1859–2448**. The complete baseline and assembled chapter were read as bytes for reconstruction and preservation, including that complement. Whole-file text searches also produced isolated notation matches outside the semantic scope; those are not a proof audit of the surrounding sections. In edition coordinates the corresponding unaudited older blocks are **184–1801 and 1863–2452**. No whole-book proof audit is claimed.

For the assembled edition, I inspected all changed text semantically through the complete addition and every old/new replacement, then verified exact correspondence with the full 5250-line edition. C.4 occupies edition **3835–5250**. The old chapter's 3829 lines become 3833 lines after the declared edits, followed by the separator and C.4. The full standalone edition files were inspected by byte comparison with these semantically read source bodies, so no second independent reading of identical copies is implied.

SHA-256 values computed by the reviewer:

| Frozen input | SHA-256 |
|---|---|
| `P1_INTEGRATION_ASSIGNMENT.md` | `810d426b72d5537c00b4d08264dd3bae68105658a766becf077b2119697d0147` |
| `P1_MANIFEST.json` | `10c04c581f72aaa11eb9ddb7fabd1b958cd5b82d5052ae9903f529c4f69f1c06` |
| `P1_ADDITION.md` | `fc613e20c3ee502fcacfbfeeab87d8b9ea5145cf80afad48a8a5ef8b18a56f0b` |
| `P1_DOCS_README.md` | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| `P1_GLOBAL_EDITS.json` | `bd802de5b3a69d1c903eb1454f7a5d353195e340ceb16a63ba85de9c820e369a` |
| `P1_DEPENDENCIES.md` | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |
| `P1_GLOBAL_BASELINE.md` | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| `P1_README_BASELINE.md` | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| `P1_GLOBAL_EDITION.md` | `f48415a7017cd3b5bae48af29d3925263e139eda0b826ed95eb6ba546ac539d1` |
| `P1_VALIDATION.md` | `7b6500bb2b9cfed149a54eedafdb3db372c78ca0138d28cca9f01927a43e6f2d` |
| `validate_promotion.py` | `565dc0933eaefa07461c964e7f2bb802b1907923b0036bb4de8715736a36a996` |

All seven hashes governed by the manifest match. The eight standalone input files, including the manifest, are byte-identical to the reviewed study inputs; the copied validator is byte-identical too. The manifest's hashes for complete unchanged live chapters/instruction files were not independently verified by reading those live files: the review was confined to frozen inputs. The frozen complete notation body does reproduce the manifest's notation hash.

## Mathematical and interface findings

### Exact finite model and transport

The addition fixes two hidden tanh layers, input dimension two, equal hidden width, no biases, the normalized circle, bounded labels, independent Gaussian initialization with stored readout variance `n^-2`, mean squared loss, and block mobilities `(n,1,n)`. The stated clock and simultaneous preceding-state raw-GD update agree with finite-dynamics (1)–(2). The full first row is retained, including its second Gaussian coordinate when a reference law does not span the input plane. The finite middle rank-one update carries `1/n`, and the readout is the stored parameter. There is no model or loss-normalization substitution.

The transport estimate (T7) has the required changing-input contribution in the first gradient. Its cutoff is applied only to the reference readout and reference lower backward field. The adjoint expansion multiplies previous backward error by bounded operators and bounded gates; it adds the next cutoff term, so the coefficient grows linearly in `R`, not quadratically. Coupling integrates individual reference tails against the reference law. There is no data maximum, smallest-Gram-eigenvalue denominator, or unavailable root/backward product estimate.

### Gaussian construction, strong flow, and restart

The complete III.F proof supplies compatible finite-program laws, both orientations of the same Gaussian matrix, singular-query treatment, density of generated coordinates, and actual Hilbert adjunction. The addition uses it only for fixed programs. A.1 admits the continuous linear-growth products; A.2 verifies their fixed-program response formulas by clipping and integrable derivative envelopes. The common two-root language and completion support passive directions and real coefficients independently of the training law.

The hypotheses of C.2 are verified at the point of use: fixed depth two, bounded tanh derivatives, unit input Gram diagonal and bounded entries, bounded residual/source RMS norms, independent Gaussian initialization, and weighted finite laws. Its single-source-pulse and weighted-history estimates preserve the atom weight and yield constants independent of atom count and Gram rank. I checked the causal order in the cap construction, including that current forward and backward coefficients do not require their own unconstructed values.

The bounded-multiplier argument proves the continuity needed for the Banach-valued field. Compact input support gives separable compact integrand ranges even in the ambient operator space; thus the Bochner integrals are legitimate. The middle integral is also Hilbert–Schmidt, although the initial action need not be. The finite-law Euler comparison is Cauchy in the complete full-state topology. Joint field/law continuity passes the integral equations through finite-law completion.

The tail transfer to arbitrary laws is correctly integrated over the training law, rather than promoted to a pointwise subGaussian bound over every input. This exact integrated estimate suffices for the one-reference uniqueness argument. Competing strong solutions need only the common ball. Restart is confined to the remaining constructed local interval and the stated bounded class; the direct Euler-to-existing-reference comparison supplies the missing continuation argument without assuming Gaussian tails at arbitrary restarted states. No global restart theorem is inferred.

### Quantitative law continuity, actual GD, and statistics

Optimizing `exp(a R)((1+R)q+exp(-c R^2))` at `R=K sqrt(log(e/q))` gives the stated modulus for `0<q<=1`; zero and large distances are treated separately. The forward input/state estimates transfer it uniformly over the whole circle.

The actual-GD argument freezes a finite reference law and coarse proof mesh before the width limit. The proxy uses the actual initialized arrays and includes the actual small random readout as an additive term. Fixed-program second moments control the finitely many contraction and assigned-velocity errors; reference cutoff moments then control recomputed backward quantities. The comparison involves only same-width full-state distances, never a finite-to-population operator-norm distance. The reference choices precede the large-width limit, and the final cutoff limit removes the Gaussian remainder. No growing program is passed through the fixed-program theorem.

Finite input/time nets apply to bounded-speed forward evaluations and to the paired initial/current activation observations. This justifies uniform predictor convergence and the displacement-observable limit separately. The latter is not incorrectly inferred from predictions. The partition proof of empirical `W1` convergence and the initialization/reference-program event give the stated iid sampling result without relative growth assumptions. Both risk limits use bounded/Lipschitz losses on the common ball and the actual joint input-label metric.

The sample-replacement coupling costs at most the observation-space diameter divided by `m`. The ghost-sample exchange is valid for the same deterministic measurable empirical-law learning map. The conclusion is exactly `sup_t |E_S[gap(t)]|`; the proof does not claim `E|gap|`, `E sup_t |gap|`, excess risk, or useful-risk reduction. The guide retains this distinction.

### Nonlinear hidden motion and comparison with C.1–C.3

The reference law has two orthogonal normalized inputs with equal positive labels; `p=Y/4` is the weighted label. Direct integration of the mean-loss equations yields the factors `2t` and `2t^2` in (6). The strong bounded-multiplier argument justifies activation expansions along the actual existing flow. The two initial upper Gaussian fields are independent because their limiting covariance is diagonal, not because a trained matrix is resampled.

The lower adjunction identity is strictly positive, proving nonzero lower activation displacement. The upper identity retains both the learned-matrix and moving-lower-representation contributions and proves the averaged upper assertion needed here. No unproved individual-input assertion is substituted. The actual-flow definition of `t_0`, the positive margin, law continuity, and paired-observable convergence establish the relative open family and its finite-width persistence. Nearby correlated atomic laws and spread-out nonatomic laws are admissible. Zero conditional label mean remains compatible with a stationary flow.

This result does not overwrite the stronger but differently conditioned fixed-finite-data C.3 activity statement. C.4's special reference computation overlaps the onset mechanism in C.3, but its shorter averaged positivity argument and law-continuity transfer are a coherent proof of a different conclusion. It does not import C.3's positive-definite-Gram machinery as an unstated assumption on every law.

## Placement, guide scope, consolidation, and preservation

C.4 is appended immediately after the complete weighted-loss end of C.3. The five declared edits adjust the main chapter's introduction, the fragments' fixed-data scope statement, the obsolete proof-unit count, the C row in the destination table, and the C introduction. The exact baseline/edition start lines of the edits are respectively `23/23`, `1801/1804`, `1814/1817`, `1819/1822`, and `2451/2455`.

Every D–J destination row is byte-identical, and the text still directs those fragments to the special-data chapter. The standalone assembly contains exactly these replacements and the C.4 addition. It does not alter other theorem bodies or relocate older fragments. C.1–C.3 retain their previous scopes. Both complete guides were read; the actual guide diff consists only of the global-nonlinear chapter row and the closing scope paragraph. Those changes accurately qualify the local model and expected-gap order. Unchanged general discussion of useful representations remains consistent because the new result does not prove useful-risk improvement.

The new proof has no study-path, runtime-data, author, or research-packet dependency. The Gaussian source proof and finite dynamics are available through canonical chapter links; A.1–A.2 and C.2 are present earlier in the assembled chapter. The new Gaussian fragment and C.4 guide anchors resolve. The repeated common-space/multiplier explanations serve their full-row/law-completion interfaces; I found no conflicting duplicate theorem or need to move the new result to another chapter. Broader editorial shortening is optional, not a condition of this review.

## Commands, actual outcomes, and validator limits

The authorized rerun was executed from:

```text
/home/amir/Codes/PDE/data/generated/training_law_stability/promotion_validation_01
```

with:

```text
python validate_promotion.py --inputs inputs --output /home/amir/Codes/PDE/data/generated/training_law_stability/integration_review/edition
```

It exited **0**, using Python **3.10.12**. The fresh output is retained, including its complete `validation.json`. The original and fresh validation JSONs differ only in `output_directory`. The six output-file hashes are identical and independently checked against the actual bytes in both editions:

| Output | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| `docs/finite_dynamics.md` | `6250c68f805b5e05aa328e631842babc4b3c61b88f90211fdf6cd950329a774b` |
| `docs/global_nonlinear.md` | `f48415a7017cd3b5bae48af29d3925263e139eda0b826ed95eb6ba546ac539d1` |
| `docs/special_data_limits.md` | `9f44c38b42b9388116f2bb0cbc7c57f2274de255e37a58e377ee84096dc85746` |
| `standalone_proof.md` | `e540b33b16a50805876b39f6e564905160a965a0c8e2d378369ac9fb71a87ae6` |

The independent preservation audit was run as:

```text
python data/generated/training_law_stability/integration_review/audit.py
```

It exited **0**. Its saved `audit.json` contains the complete reviewed-input hashes, dependency span hashes, preservation outcomes, reading scope, output checks, and validation-file hashes; `guide_diff.patch` preserves the full guide comparison. `command.txt` records the standalone rerun.

One earlier reviewer-only inline audit exited **1**: after the exact reconstruction had already passed, it incorrectly asserted that the baseline ended with two newlines. Direct inspection found one terminal newline. The saved audit measures trailing whitespace and removed that unjustified reviewer assumption. This was not a candidate or validator failure; it is recorded in `audit.json` rather than omitted.

The validator checks seven hashes, exact declared assembly, absence of selected forbidden dependency strings in the addition, balanced display delimiters and `begin/end` environments in the addition/dependencies, set membership of T/P/A references, and the new Markdown links/anchors. It does **not** prove mathematics, enforce the notation contract, verify equation-reference locality or numerical equation references, detect semantic duplication, render the whole book, check unchanged guide links, or verify the complete live dependency hashes. The six generated file hashes exclude the generated validation JSON itself; the reviewer audit separately records both JSON hashes. Its passing status is therefore preservation/document evidence, not a mathematical certificate.

## Required corrections

**R1 — obey the existing activation-derivative notation contract.** `P1_DEPENDENCIES.md` lines 40–41 explicitly requires activation derivatives to be written as `phi'` rather than introducing a second name. The new proof introduces `g=tanh'` at `P1_ADDITION.md` line 854 and uses it in (A5), and introduces `b(s)=sech^2(s)=tanh'(s)` at line 1162 with recurring uses through line 1267. In the assembled edition these are lines **4688–4692** and **4996–5101**. Replace the activation-derivative aliases by `phi'` (with the already fixed `phi=tanh`) or an explicit tanh derivative throughout these two passages. Generic bounded-multiplier variables in the abstract continuity argument are a different matter and need not be renamed. This is an explicit contract violation, not an optional preference or a mathematical error.

**R2 — type the state norm correctly and explicitly define its named finite counterpart.** In (T3), addition line **192** / edition line **4026**, `L^2(R^2)` denotes the wrong domain notation for a random two-component row. Use `L^2(Omega_1;R^2)` as in the stated state space. Immediately after (T3), the prose refers to a finite counterpart but never actually defines the `D_n` subsequently used at addition lines **866, 901, 907 and 1077**. Display its definition with the ordinary Frobenius/Euclidean norms and explicit RMS factors:

```text
D_n(theta,theta_bar)
 = ||W^(1)-W_bar^(1)||_F/sqrt(n)
   + ||W^(2)-W_bar^(2)||_op
   + ||W^(3)-W_bar^(3)||_2/sqrt(n).
```

This makes the central same-width comparison topology unambiguous and follows the frozen norm convention at dependency lines 71–75 and edition lines 17–18. The intended formula is recoverable from the prose and the mathematics uses it consistently; the required correction is to the exact integrated statement and interface, not a change of topology or proof strategy.

These are bounded corrections to notation. They should be reflected in the frozen assembled edition and manifest before a fresh exact-version integration decision. I do not approve a hypothetical edited version in advance.

## Optional comments and limitations

- Addition line **1101** / edition line **4935** says the common fields (T1) are “from Section C.4.2”; their defining display is in **C.4.1**. Correcting that local pointer would improve navigation. C.4.2 explicitly imports those same fields, so this does not leave a missing dependency or block the proof.
- The theorem concerns a specific local two-hidden-tanh model and its stated predictor/risk/displacement observables. It supplies no all-time, excess-risk, quantitative finite-width stability, or whole-book validity result. The review's positive mathematical assessment has exactly those limits.
- The full source-independent proof packet was reviewed, but the unchanged older complement, other chapter claims in the guide, external literature characterizations, exporter, maintained APIs, and empirical reproduction are outside this assignment. No test outcome concerning those items is inferred.

Final decision for the hashed P1 edition: **NONACCEPTANCE pending R1 and R2**. Mathematical consistency, placement, scope, source independence, and preservation checks otherwise support the proposed addition within the stated review coverage.
