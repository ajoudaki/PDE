# Independent document-only review: round 2 coverage

Verdict: **NEEDS_CORRECTIONS**.

The report is a substantially qualified research synthesis. Its principal distinctions between formal jets, fixed-program limits, local and global population identification, finite optimization, and generalization are internally coherent. The required corrections below concern incomplete thematic coverage, one missing hypothesis in an explicit mathematical implication, and undefined quantities in an important displayed construction. They do not invalidate the cited source theorems or turn openly acknowledged proof-audit dependencies into new defects.

## Evidence boundary and full-read record

- Sole research evidence: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- SHA256, identical before and after the full read: `9c5a1c80e8eff6975939ed0481e2eaa11a5f6c1bc46ba8b9d2cc11001afcc529`.
- Size: 91,964 bytes; 574 lines.
- Full, untruncated line coverage: **1–220, 221–350, 351–445, 446–515, 516–574**, including the final line and all 36 task-map rows. These intervals cover every line without a gap.
- The operational skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely. It informed checks of hypotheses, quantifiers, and definitions; it supplied no mathematical research evidence.
- No linked source, project index, source audit, earlier review, task history, browser result, or other agent output was read. No experiments or new proof campaign were performed. Only this assigned review file was written; the master was not edited.

All line references below refer to the above hash. Statements in the report about what source auditors read or accepted are treated as the report's provenance assertions, not as independently verified evidence. In particular, this review does not certify any missing or imported primary proof.

## Required corrections

### R1. Integrate the Borel/basis contribution into the thematic synthesis

**Location:** task-map line 517; thematic §§4–5, lines 68–176.

PDE task 2 contributes initialization-jet/Borel and alternative-basis reconstruction routes, conditional on transform, growth, and identification assumptions. This contribution appears only in its task-map row. The thematic discussion of jets, zero Taylor radius, and possible signed resummation does not actually identify these retained routes or state their disposition. Mentioning that signed resummation is not excluded at line 152 does not convey that the project already investigated conditional reconstruction routes.

This is a coverage omission, not a complaint that the report lacks a full Borel proof. The existing task-map qualification is sufficient evidence for a short thematic entry.

**Minimal fix:** add to §4.2 or §5.2 a sentence or short paragraph such as:

> The initialization-jet/Borel and alternative-basis reconstruction routes remain conditional on their transform, growth, and trajectory-identification assumptions. No new unconditional global theorem is inferred from them, and their full Borel dependencies were not re-audited.

Give task 2 the corresponding section reference. No stronger mathematical assertion is needed.

### R2. Retain the original order-one-readout L3 arctangent program in the body, with the tanh exception stated accurately

**Location:** task-map lines 521, 550–551; §7.3, lines 305–321.

Three map entries retain the original L3 order-one-Gaussian-readout arctangent program: exact autonomous/operator algebra, failed or retracted moment/cluster and ordered-limit arguments, and a dynamic cavity/Schur–Volterra continuation route. The body separately discusses the old L2 order-one-readout theorem, the newer L3 small-readout local theorem, and the L3 tanh corrective result. It never gives the original L3 arctangent program its own explicit disposition. The distinction at line 49 and the generic response discussion in §9 do not supply this missing coverage.

This omission matters because the report itself warns that changing the readout initialization changes backward fields and training. A reader of the thematic body should not need to reconstruct the original L3 model's status from three task-map rows or confuse it with the small-readout theorem.

There is also a qualification to preserve when adding this paragraph: line 521 says the original order-one-readout “arctan/tanh limit remains open,” while line 321 records a proved stationary zero-label tanh specialization. The open-target wording should explicitly concern the nonzero-label feature-learning target rather than swallowing that stated exception.

**Minimal fix:** add a short paragraph in §7.3 identifying the original L3 order-one-readout arctangent algebra and conditional continuation routes, and stating that the reported moment/cluster and ordered-limit bridges do not establish its global population limit. Cross-reference it from PDE task 6 and PDE-2 tasks 13–14. Qualify line 521's open arctan/tanh target by the nonzero-label scope, while retaining the zero-label tanh result already in the body. Preserve the existing private-history qualifications; no additional source certification is requested.

### R3. The physical square-loss counterexample needs a nonzero target

**Location:** §4.2, lines 110–117.

The feature-time counterexample gives initial update directions $4\mathbf 1$ and $3\mathbf 1$. The next sentence says their order-$h$ discrepancy persists under physical square-loss GD because both initial predictions tend to zero. That implication requires a fixed **nonzero** target, which is not specified in this example. Vanishing predictions by themselves do not imply a nonvanishing residual.

This can be checked directly from the displayed example, without a source import. For the full square loss $(f-y)^2$, the physical first-step directions are

\[
8(y-f_0)\mathbf 1,
\qquad 6(y-\widetilde f_0)\mathbf 1.
\]

Here $f_0=0$ and $\widetilde f_0\to0$. Their difference tends to $2y\mathbf 1$. Thus a fixed nonzero $y$ retains the claimed discrepancy, whereas $y=0$ makes it vanish with width. Using half-square loss changes the factor, not the need for the hypothesis. The report already handles this same residual-clock distinction correctly in §5.2, line 152.

**Minimal fix:** replace the physical-loss sentence with:

> For physical square-loss GD with any fixed nonzero target, the residual factors tend to the same nonzero constant, so the order-$h$ discrepancy persists. This physical-loss conclusion is not asserted for zero target.

The feature-time counterexample and the careful distinction between a deterministic energy-ball failure and a Gaussian-typical theorem remain intact.

### R4. Define the reverse fields and clipping map used in §8

**Location:** §3, lines 39–53; §8, lines 357–390; reused in §9, lines 396–413.

The important distinction between coordinate-query clipping and projection of the complete reverse field is displayed using $\tau_R$, $\delta^{(3)}$, and $\delta^{(2)}$. None is defined in the report. In particular, the text does not specify whether these reverse fields contain the residual or the factor $1/n$ from the output. Those choices determine both the clipping location and the meaning of the $C_S\sqrt n$ threshold. Here the missing definitions impede use of the mathematical presentation; they are not missing primary proofs.

**Minimal fix:** introduce a compact convention before the first clipping equation. For the residual-free, one-sample feature-time convention suggested by the displayed formulas, specify coordinatewise clipping,

\[
\tau_R(u)=\max\{-R,\min\{u,R\}\},
\]

and the reverse recursion, using the report's existing output normalization,

\[
\delta^{(L)}=W^{(L+1)}\odot\phi'(Z^{(L)}),
\qquad
\delta^{(\ell)}=\phi'(Z^{(\ell)})\odot
(W^{(\ell+1)})^*\delta^{(\ell+1)}.
\]

State explicitly that there is no residual in these fields and that, at finite width, this convention corresponds to $\delta^{(\ell)}=n\nabla_{z^{(\ell)}}f$ with transpose in place of adjoint. Identify the unit lower-block rate convention implicit in the displayed $M$, or state the actual convention if different. If the intended definitions differ, print those definitions and reconcile the formulas rather than silently adopting this suggested convention.

## All-36 thematic coverage crosswalk

“Covered” here means the map entry's substantive contribution is represented at the report's declared synthesis level. It does not mean its source proof was independently checked. Repeated, teaching, and recovery tasks need not be assigned separate mathematical theorems. Numbering is local to each host group, as in the report: **17 + 19 = 36**. The external identity index was not consulted.

| Group / task | Map line | Thematic location and disposition |
|---|---:|---|
| PDE 1 | 516 | §7.2, lines 272 and 282: all-fixed-depth bounded shifted-atan global result; covered. |
| PDE 2 | 517 | Conditional Borel/basis routes occur only in the task map; **R1**. |
| PDE 3 | 518 | §7.2, lines 273–280: two-sample angle/separation extension, with extension qualification; covered. |
| PDE 4 | 519 | §§8–9, lines 347–418: clipping, causal adaptation, projection, generated-action and response obstructions; covered. |
| PDE 5 | 520 | §7.1, lines 229–261: local joint theorem, separate activity, and finite-GF corollary; covered. |
| PDE 6 | 521 | Original L3 order-one-readout arctangent disposition is missing from the body; tanh exception is in line 321; **R2**. |
| PDE 7 | 522 | §7.3, line 305, and §11, line 462: old L2 result and import scope; covered. |
| PDE 8 | 523 | §6, lines 202–209: scalar/PDE representation barriers and compatible operator positive; covered. |
| PDE 9 | 524 | §5.3, lines 172–174: canonical initial-layer claim withheld for concrete gaps; covered. |
| PDE 10 | 525 | §9, line 420: RMS quadratic finite positives and population obligations; covered. |
| PDE 11 | 526 | §6, lines 182–200: L2 spectral result, completed L3 theorem, and broader conditional identification; covered. |
| PDE 12 | 527 | §5.1, line 141, and §6.1, lines 211–225: partial-quadratic moment/algebra results; covered. |
| PDE 13 | 528 | §5.1, lines 134–146: architecture-specific negatives and finite positive prefixes; covered. |
| PDE 14 | 529 | §§5.2–5.3, lines 150–174: formal no-go scope and conditional DMFT distinction; covered. |
| PDE 15 | 530 | §3 and §§5.1/6.1: mobility conventions, exact finite update examples, and uncompleted multi-input transform at line 148; covered at synthesis level. The historical experiments are not promoted. |
| PDE 16 | 531 | §5.1, lines 125–132: canonical moment prefix, Ward distinction, coefficient qualification, and open all-order positivity; covered. |
| PDE 17 | 532 | §4.1, line 81: backward peeling and uncompleted concentration; covered. |
| PDE-2 1 | 538 | §7.2, line 276, and §7.4, line 345: shape extension and moderate-sine local result; covered. |
| PDE-2 2 | 539 | §7.2, lines 275, 278 and 301: all-depth two-sample extension, odd gain, and scientific limitation; covered. |
| PDE-2 3 | 540 | §7.2, line 274, and §12: improved two-sample power and remaining general no-gain direction; covered, with private-branch limit explicit in the map. |
| PDE-2 4 | 541 | §§7.2/7.4: separated two-sample, three-sample shape/gain, and sharp initialization results; covered. |
| PDE-2 5 | 542 | §2 and map: recovery/reconstruction and access qualification; no independent theorem is claimed or needed. |
| PDE-2 6 | 543 | §§7.1–7.3, especially lines 270–271 and 309: local, orthogonal, affine-first, and special-angle scopes; covered. |
| PDE-2 7 | 544 | §7.2, line 269, and §7.3, lines 315–317: original baseline, local L3, and finite fitting; covered. |
| PDE-2 8 | 545 | §7.3, line 319, and §6: withdrawn sin+cos global claim and retained deep-linear/representation results; covered. |
| PDE-2 9 | 546 | §§4, 5.3, 6, and 7.3: fixed-program distinctions, quadratic/ReLU mesh results, and corrected operator scope; covered. |
| PDE-2 10 | 547 | §5.3, lines 174–176, and §3: mesh/scaling distinctions; attribution/history limitation explicitly retained in the map. |
| PDE-2 11 | 548 | §3, lines 41–51, and §11, line 456: mobility and connector-scaling distinction; missing finite-type primary theorem is explicitly not certified. |
| PDE-2 12 | 549 | §4.1, lines 94–104: finite-step/Price/cubic package and nonuniform mesh limitation; covered. |
| PDE-2 13 | 550 | Original L3 order-one-readout cavity/Schur–Volterra route lacks an explicit thematic disposition; **R2**. |
| PDE-2 14 | 551 | Original L3 order-one-readout algebra and failed ordered-limit bridge lack an explicit thematic disposition; **R2**. |
| PDE-2 15 | 552 | §7.3, line 305: the underlying L2 theorem is covered; teaching is correctly not counted as another theorem or review. |
| PDE-2 16 | 553 | §7.3, line 321, and §10: tanh correction and residual/dense distinction; covered. |
| PDE-2 17 | 554 | §§3–4 and §10: continuous-time bridge scope and scalar-particle versus dense residual architecture; covered. |
| PDE-2 18 | 555 | §4.1, lines 92–104: order-five recurrence, finite-step identification, and limitations; covered. |
| PDE-2 19 | 556 | §5.1: high-order moments and counterexamples; the map correctly declines to claim exhaustive private amendments. |

## Internal checks with no additional required correction

- The formal cubic identity at lines 83–88 and the distinct Euler coefficient at lines 96–104 are not conflated: the report explicitly distinguishes the coefficient of the third derivative.
- The metric/activation Stieltjes negatives do not contradict the canonical finite positive prefix. Output order 17, the additional Ward-derived hidden coefficient, and the lack of all-order positivity are consistently separated.
- The smooth zero-radius ODE example defeats only the claimed logical implication; it is expressly not presented as a neural closure or a proof of a trained trajectory.
- The local theorem's deterministic-mesh quantifier supports the finite-GF diagonal argument. Fixed-width continuation, population local time, observable restrictions, and the inherited dependency grade remain distinct.
- The special global table keeps fixed depth separate from uniformity in depth, allows singular raw Grams where stated, separates absolute nonaffinity from useful relative nonlinearity, and retains the odd-gain exception to the small-perturbation variance bound.
- The zero-label tanh specialization is qualified correctly in the body. Finite pure-atan fitting is not promoted into global population identification.
- The three clipping constructions are not concatenated. The estimate at lines 369–370 does tend to zero for $R_n=o(\log n)$ on a fixed horizon, while it still does not establish a limit of either varying construction. The projection argument does not claim RMS control from an integrated weak defect.
- The generated-action obstruction keeps width first at each fixed bump scale and distinguishes its test queries from actual training. The report does not substitute deterministic or conditional effective-model witnesses for canonical Gaussian-trajectory impossibility.
- Scalar-particle joint width/depth convergence, dense Gaussian ResNet approximation, optimization, and generalization remain separate scientific claims. The prescribed-accuracy implication in lines 496–504 does not exchange the infinite-width and infinite-time limits.
- The chronological qualifications are generally careful: later narrow positives do not erase broader open targets, corrected negatives remain withheld, and recovered bytes are not identified with inaccessible current remote versions. The report's claims of source-audit completion remain claims at their stated scopes; I have not verified them externally.

## Optional presentation improvements

These are not additional verdict blockers.

1. Add a short notation key for GF/GD, RMS, $W_2$, and the learning-metric kernel. A block formula such as $K_{ab}^{(\ell)}=(\nabla_{\theta_\ell}f_a)^T D_\ell\nabla_{\theta_\ell}f_b$ would make the later loss-dissipation formula easier to use. The first use of feature time could also state its residual-clock relation.
2. In the deep-linear operator display, briefly identify the space/type of $C$ and why the indicated trace and Hilbert–Schmidt norm are defined in that construction. The present “explicit colored Fock-space realization” phrase points outward rather than explaining the displayed objects locally; reproducing the realization or its proof is unnecessary.
3. State the exact allowed raw-GD mesh in the finite-fitting paragraph at line 315. The adjacent local theorem specifies $n^{-2}$, but a reader should not have to infer whether the finite global result uses the same condition.
4. Replace the unexplained “SG's” at line 569 with “the broad local theorem's.” Consistent section links in every substantive task-map row would also improve navigation.

The four required corrections are modest changes to this synthesis. A corrected document can remain explicitly dependency-qualified throughout; a clean document-only verdict would still not certify the unavailable sources or complete the main global population/generalization program.
