# Independent integration review — frozen version 1

Review date: 2026-09-11. Reviewer: fresh agent `/root/integration_v1`.

**Review complete; integration acceptance blocked by four required corrections below.** The frozen inputs were available and matched their specified hashes. The fresh standalone edition and both isolated deterministic checks passed. These passes do not cure the notation and presentation defects. No additional scientific obstruction was found in the assigned integration scope; this is not a complete audit of the older Gaussian construction or whole book.

## Required corrections

Locations below use `proposal_C4_8.md` line numbers. The corresponding assembled line is the proposal line plus 11439, in both `standalone_v1/docs/global_nonlinear.md` and the independently generated `integration_v1_edition/docs/global_nonlinear.md`.

### R1. Malformed inequality in the localization argument

At proposal line 1178 / assembled line 12617, the support statement contains `\ler_{\rm loc}/2`. TeX reads `\ler` as one control word; it is not the intended inequality followed by the radius. No definition of this command occurs in the addition or supplied notation contract. Replace it with `\le r_{\rm loc}/2`.

This is a minor presentation defect in a used proof statement. The intended estimate is consistent: with epsilon equal to the localization radius divided by 16 and each finite test difference at most b, (R11) gives radius/4 + radius/4 = radius/2. The validator checks delimiter counts and labels but does not detect this malformed command.

### R2. Finite norm notation contradicts the unchanged book contract

At proposal lines 1479–1501 / assembled lines 12918–12940, a new RMS norm `\|v\|_{(n)}` is introduced and then unqualified finite norms in (P18) and the following readout bound mean RMS norms. The unchanged `docs/NOTATION.md`, lines 59–63, explicitly requires ordinary finite Euclidean/Frobenius/operator norms and displayed normalization factors, saying “do not hide these factors in new norm or inner-product symbols.” The original chapter also states this convention at lines 16–18; C.4.7 displays all finite factors explicitly.

Use ordinary norms throughout this finite paragraph. The correct inequalities, with exactly the intended scaling, are

\[
 \frac{\|\dot c_n\|_2}{\sqrt n}
 \le 2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right),\qquad
 \|\dot K_n\|_F
 \le 2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
              \frac{\|c_n\|_2}{\sqrt n},
\]
\[
 \frac{\|\dot w_n\|_F}{\sqrt n}
 \le 2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
       (\|A_{n,0}\|_{\rm op}+\|K_n\|_F)
       \frac{\|c_n\|_2}{\sqrt n}.
\]

Apply the same explicit normalization to the integrated readout bound. This is a notation/interface correction, not a changed metric or scientific conclusion. The locally typed source-field aliases in the source lemma are understandable; the finite norm conflict is the specific required change here.

### R3. Restore the assembled heading hierarchy and remove stale numbering

At proposal line 1 / assembled line 11440, C.4.8 is an h3 heading, whereas C.4.5, C.4.6 and C.4.7 are h4 subsections of the h3 C.4. heading. Its own C.4.8.1–4 headings are h5. Change the C.4.8 heading to h4 so the new material belongs to C.4 in the document outline and its subunits have the correct nesting. The generated navigation slug is unaffected by heading depth, but the validator's literal heading assertion must track the corrected heading.

The new assembly also retains local headings `3. Actual atom response...` (line 916), `4. A usable characterization...` (1020), and `6. Actual finite gradient flow...` (1475), without corresponding preceding numbered headings in those proof units. At line 922 it cites “the larger ball of Section 2,” although C.4.8.2 has no locally numbered Section 2. Remove those stale prefixes or renumber their own local units consistently. Replace that reference with the named preceding subsection or explicitly with the ball of radius `3 delta_Y / 4`. This avoids a reader having to infer a missing unit from author assembly history.

These are minor organization/reference defects. Placement after C.4.7 is substantively appropriate. The new navigation link itself resolves to the correct slug.

### R4. Correct the middle-update norm sentence

At proposal lines 1486–1488 / assembled lines 12925–12927, the text identifies the full update `-2n^{-1}\int r\Delta h^T\,d\mu_m` and says its Frobenius norm is bounded by the product of two normalized vector norms. As written, this drops both the residual integral and the factor two. The relevant identity applies to the rank alone:

\[
 \|\Delta h^T/n\|_F
    =\frac{\|\Delta\|_2}{\sqrt n}
       \frac{\|h\|_2}{\sqrt n}.
\]

Consequently the full update satisfies

\[
 \|\dot K_n\|_F
 \le2\int |r|\,
       \frac{\|\Delta\|_2}{\sqrt n}
       \frac{\|h\|_2}{\sqrt n}\,d\mu_m.
\]

For example, at width one with one datum, `c=1`, `A=0`, first preactivation 1 and label 1, the update norm is `2 tanh(1)` while the rank norm is `tanh(1)`. Thus the missing scalar is not an available bound. This is a local explanatory error: the subsequent (P18) already contains the correct factor and is valid under its declared RMS interpretation. Replace the sentence with the rank identity and resulting integrated bound, alongside R2.

## Scope, independence and complete reading evidence

I received the neutral supervisor assignment and personally read the entire `integration_packet_v1.md` (86 lines), then only its authorized scientific inputs and required process/skill files. I did not read the study README, history, author drafts, selector verdict, previous reviews, paired reviewers' reports or messages, other studies, or Git history. No other reviewer was contacted. No book/code edit, Git operation, training run, or parameter sweep was performed.

Required process inputs were read completely:

- `AGENTS.md`, all 47 lines; `RESEARCH_WORKFLOW.md`, all 224 lines, including all of Part 2. The independent-review instruction replaces author startup and prohibits Git operations in this assignment.
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`, complete.
- `/etc/codex/skills/investigate-conjectures/SKILL.md`, complete, and its complete `references/research-contract.md` and `references/adversarial-audit.md`. These are applicable to scope/non-vacuity and hostile integration checking. This assignment did not resume research history, conduct a multi-route proof search, or run a research experiment, so the other references were not applicable.

Complete new-material reading:

- All 1535 lines of C.4.8 in the frozen assembled chapter, read without omission as 11440–11839, 11840–12239, 12240–12639 and 12640–12974. All lemma statements, proofs, finite-source recursions, statistical arguments and final interpretation were included.
- The entire proposal was byte-read and independently proved equal to that exact assembled line range. Thus the scientific text read is exactly the complete proposed source, not an excerpt of a different draft.
- All 23 lines of `promotion_edits.json`.
- Live and frozen-assembled `docs/README.md`, all 284 lines in each; live and frozen-assembled `docs/NOTATION.md`, all 98 lines in each.
- All 132 lines of `validate_proposal.py`, all 146 lines of `check_gaussian_calculus.py`, all 368 lines of `check_sampling_hoeffding.py`.

Older scientific reading, exactly as authorized:

- Original `docs/global_nonlinear.md`: 1–32; 1803–1835; 3836–3980; 5268–5472; 6902–7167; 8976–9293; 9294–9605; 10300–10608.
- Original `docs/finite_dynamics.md`: 1–227, complete for that range.

One combined tool output containing the skill references and three verification programs was truncated by the aggregate output limit. I repaired it by reading the complete validator and Gaussian check together in a bounded call and the complete sampling check separately. Every later scientific range read and the complete guide reads returned without truncation. The two skill references were visible completely in their individual returned block. I also read all of the fresh validation report, Gaussian report, sampling report and independent-check report completely.

**Unread complement:** every older chapter body outside the ranges above, including the earlier long proof bodies and the Gaussian construction, remains scientifically unread in this review. The assembler byte-reads the frozen Gaussian source file and emits its authorized 3785–4286 excerpt; this establishes input integrity only. I did not infer a proof audit from that copy or inspect the excerpt scientifically. The independent label check extracted tag metadata from the assembled chapter without reading additional proof bodies. Linked external context sources in the README were not scientific dependencies of this review and were not fetched. This is neither a whole-book proof/link/export audit nor the paired complete dependency review.

## Integration findings within that scope

**Exact edits and preservation.** The fresh chapter and README match the original frozen assembled versions byte-for-byte. Independently removing the exact two-newline/proposal suffix and reversing only the declared replacements recovers each original live file byte-for-byte: one replacement in `global_nonlinear.md`, two in `README.md`. The notation file is unchanged. No older material is deleted or rewritten beyond the declared summary sentence insertion. New equation tags are unique across the complete assembled chapter; 88 new tags and 67 distinct explicit new tag references are valid. Named older references and their ranges were checked against the authorized interfaces: in particular C.4.7.N2–N8, N9–N17, N-cap and NW1 have the advertised roles.

**Model and normalization.** C.4.8 uses the same two hidden tanh layers, `u=x/sqrt(2)`, independent Gaussian stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, output divided by n, unhalved mean/integrated squared loss, physical time 40, actual finite readout, and common initial Gaussian action/adjoint as C.4.7. Direct specialization of finite-dynamics (1)–(2) gives the three factors in (P1) and the finite rank factor `1/n`. The normalized circle output measure is a probability measure, so its L2 norm is at most the C(circle) norm. R2 and R4 are the finite-paragraph exceptions requiring correction.

**Source interface.** S2–S7 preserve the exact two-orientation source recursion and distinguished current-query slot convention of C.4.7.N2–N8. The rows F and D retain the learned-rank corrections and actual adjoint response; singular or duplicated source slots are named rather than reconstructed by a Gram inverse. The first-response equations differentiate residuals, contractions, source covariance and both coefficient arrays. They do not substitute a frozen kernel or arbitrary operator having the same norm. The source-cap neighborhood and low-order bound dependencies are expressly retained. The deeper proof of the original source realization/cap is outside this integration read scope.

**Value-to-influence and topology.** The new argument first obtains finite-program TV response bounds, uses pointwise mesh value convergence from C.4.7 for common quotients, and then passes finite-law values to Borel laws through weak/W1 continuity. It does not require TV convergence of empirical laws to a nonatomic law. The `delta_Y/4`, `delta_Y/2` and `3 delta_Y/4` regions leave the stated contamination margin: diameter at most `2+2Y` and epsilon at most `delta_Y/[4(2+2Y)]` give the required outer radius. Centering is established for the actual C-valued limit. P13 characterizes it from the finite recursion, independent of quantization and mesh choices. At the reference it agrees with C.4.6 by the C.4.7 contamination statement, without asserting finite-network derivative capture at every perturbed base law.

**Sampling and bounded extension.** The theorem asserts the actual derivative in C(circle) but the whole-function Gaussian limit in the separable Hilbert space H. The proof does not promote the H-valued limit to a C(circle) functional CLT or infer point-evaluation convergence from L2 alone. Its spatial averages and covariance kernel are correctly distinguished. The explicit zero extension outside `U_Y` makes every sample outcome defined and bounded. The auxiliary smooth finite-test cutoff agrees near each separately fixed sampling law, and its exponentially small mismatch transfers the mean-square remainder to that exact zero extension. Thus the moment statement is not silently asserted for an arbitrary unbounded or undefined population endpoint on exceptional laws.

**Width-first bridge.** At each fixed sample size the conditional law is a separately fixed finite law; independence preserves the prescribed initialization distribution. C.4.7.NW1 controls the good event, bounded convergence handles the conditional errors, and bounded-Lipschitz tests bound the bad event by twice its probability. This supports the order written in P6. No simultaneous square-root-sample/width rate, finite-width second-moment theorem, GD sampling CLT, all-time theorem or law-uniform failure probability is introduced in either the theorem or its new summaries.

**Placement, value and duplication.** C.4.7 constructs the nonlinear law map and reference contamination derivative; the new section supplies actual centered response at every separately fixed law in a smaller neighborhood and the Hilbert sampling limit with covariance and mean-square remainder. This is distinct from the earlier local expected generalization-gap bound, reference derivative capture and finite-contamination limit. Restating the source recursion and a direct finite continuation argument is useful to make this section readable, though the latter overlaps established finite-dynamics/C.4.7 facts. No scientific content depends on the study history, reviewer verdict, generated arrays or these check programs. The check programs only verify stated algebra on fixed self-contained fixtures. The three new summary sentences accurately describe the theorem's horizon, topology and width-first qualification. R3 concerns actual heading/reference integration, not a need to change the destination.

## Fresh deterministic validation and provenance

Working directory for all top-level commands: `/home/amir/Codes/PDE`. Environment: Python 3.10.12; Linux 5.15.0-151-generic x86_64, glibc 2.35. The checks use the Python standard library, exact rational arithmetic and fixed literals; no random seed, accelerator, external package, retained array or training data is involved.

Executed fresh assembly, exit 0:

```text
python studies/trained_prediction_sampling/validate_proposal.py --output data/generated/trained_prediction_sampling/integration_v1_edition
```

The directory was freshly created with `exist_ok=False`. The program copied only its explicitly listed documents/excerpts/check sources, not the checkout or Git metadata. Its isolated subprocesses ran from the fresh edition, with `PYTHONPATH` removed and Python `-I`:

```text
/usr/bin/python -I <fresh>/verification/src/check_gaussian_calculus.py --output <fresh>/verification/gaussian_report.json
/usr/bin/python -I <fresh>/verification/src/check_sampling_hoeffding.py --output-dir <fresh>/data/generated/trained_prediction_sampling/statistical_checks/standalone
```

Here `<fresh>` is the absolute `integration_v1_edition` directory given above. The full literal commands, working directories, stdout, empty stderr and exit codes are retained in `integration_v1_edition/validation_report.json`.

Observed results:

- Gaussian check: exit 0, six exact identities passed. The independent-normal substitution oracle checks first and mixed-second covariance differentiation for two polynomial observables for all s,t, including the rank-one line s=t. It checks algebraic factors, not the neural uniform estimates.
- Sampling check: exit 0, 748 exact checks passed, 16 Bernoulli base states and six pairs with 64 original/replacement configurations each. All four Hoeffding orders and all three remainder components have positive energy. Higher-order energy is `11044728/390625`, the pair bound is `1652616/15625`, and strict slack is `30270672/390625`. Both sides of the exact scaled remainder identity are `548332/3125`. This is a nondegenerate finite identity check, not empirical evidence for the theorem's asymptotic hypotheses.
- Assembly: PASS; unchanged input hashes before/after; exact inverse preservation; 88 unique new tags; 67 explicit new references; new navigation link resolved.

I separately wrote and executed, exit 0:

```text
python -I data/generated/trained_prediction_sampling/integration_v1/independent_checks.py
```

Its complete source and output are in the assigned scratch directory. It independently uses byte operations for preservation, verifies the complete proposal/exact assembled-range equality and fresh/frozen correspondence, checks new tags against the assembled chapter, computes the heading slug, records source/output hashes, and inventories the new TeX control words. Its PASS is limited to those integrity checks and explicitly records the outstanding corrections. It neither imports the validator nor adopts its verdict as the review verdict.

Complete retained outputs:

- `data/generated/trained_prediction_sampling/integration_v1_edition/validation_report.json`
- `data/generated/trained_prediction_sampling/integration_v1_edition/verification/gaussian_report.json`
- `data/generated/trained_prediction_sampling/integration_v1_edition/data/generated/trained_prediction_sampling/statistical_checks/standalone/report.json`
- `data/generated/trained_prediction_sampling/integration_v1/independent_checks.py`
- `data/generated/trained_prediction_sampling/integration_v1/independent_checks.json`

## Hash record

All packet-frozen values below were checked before substantive review and remained identical after the fresh assembly and independent audit. Paths abbreviated as `proposal`, `edits`, and Python filenames are in `studies/trained_prediction_sampling/`. The table records full SHA256 values.

| Input | Before and after SHA256 |
|---|---|
| proposal_C4_8.md | `53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456` |
| promotion_edits.json | `8aaa48600193350eb1539929c58e4c4db999e842921a6072ca1b113060191027` |
| validate_proposal.py | `fc03a4933832ee1adf0c72be5886639c35ac60ea7f662433ee5101ea55b79458` |
| check_gaussian_calculus.py | `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef` |
| check_sampling_hoeffding.py | `4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a` |
| original docs/global_nonlinear.md | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |
| original docs/README.md | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| original docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| original docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| frozen and fresh assembled global_nonlinear.md | `d1ebb0763c6cdfcdfa7465bac3adea3a51f28a0b6129f889e059c128249738ac` |
| frozen and fresh assembled README.md | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| frozen and fresh assembled NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The assembler additionally verifies the full Gaussian source hash `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` before/after. Its emitted excerpt is `43704820690a545e42673b93791a679985376351df9f349c39b4282bdef85b2f`; the finite-dynamics excerpt is `bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980`. These are provenance checks, not a scientific read of the Gaussian proof.

Neutral packet SHA256: `39bbf30def6f2ee1c92f7fe579ffbe531f722331c853c099c9358c1830f59b3f`. Process hashes: AGENTS `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba`; workflow `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12`. Required skill hashes: solve-math `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`; investigate-conjectures `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de`; research-contract `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e`; adversarial-audit `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501`.

Fresh report hashes are also retained in `independent_checks.json`: assembly `ecd10d4377a3782dc70b5c784e7769a6cf5fd560f1ac2cc2af6b50c76b0c212f`; Gaussian `74379f1ba103d4dbb1f24ab221c3d38eb247ac3d364339b07a828f1378342e6c`; sampling `239cb63cc6a4b9d0f9e9cb34b7380b2743b6bb7b26b9c03297231a26bb0be57d`.

## Completion statement

The assigned complete new-material integration read, exact older interface read, source review, fresh isolated deterministic validation and independent preservation/navigation audit are complete. No missing input or inaccessible dependency prevented this integration review. Acceptance of v1 is blocked by R1–R4; obtain a fresh complete integration review of the corrected assembled scope, retaining this report and frozen packet. Any scientific change must also follow the paired-review rule. Nothing in this report substitutes for those separate complete scientific reviews or user approval of a reviewed promotion.
