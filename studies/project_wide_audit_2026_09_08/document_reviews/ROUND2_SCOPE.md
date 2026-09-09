# ROUND2_SCOPE — independent document-only review

**Verdict: NEEDS_CORRECTIONS.** One narrow hypothesis correction is required in the physical-square-loss version of the activation-stability example. The feature-time counterexample survives. I found no required change to the main scientific recommendation or a contradictory promotion of results in the 36-task map.

## Evidence and full-read coverage

- Sole research evidence: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- SHA256: `9c5a1c80e8eff6975939ed0481e2eaa11a5f6c1bc46ba8b9d2cc11001afcc529`.
- Length and coverage: **574 lines; lines 1–574 read completely, including tables, equations, qualifications, and the final task map**.
- Complete, untruncated numbered reads covered **1–124, 125–230, 231–335, 336–450, and 451–574**. An initial aggregate display was truncated; coverage is claimed from the subsequent untruncated reads, not from the truncated aggregate.
- The hash and line count were checked again after the substantive review and were unchanged.
- The only additional input file read was the expressly permitted operational skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`. It informed the hypothesis and implication checks; it supplied no outside mathematical evidence. The newly written review was subsequently read to verify its formatting.
- No linked sources, other project documents, source audits, prior reviews, histories, browser results, or other agent outputs were consulted. No experiments or new proof campaign were performed. The master was not edited; this assigned review file is the only write.

This verdict concerns internal accuracy of a qualified synthesis. Source-proof inspection, source hashes, historical recovery, imported theorems, and coefficient certificates described in the master are reported evidence, not independently certified by this review. Their openly stated limitations are not themselves defects.

## Required correction

### R1. Specify a fixed nonzero target in the physical-GD counterexample

**Location:** lines 110–117, specifically the sentence at line 117 claiming that the order-$h$ discrepancy persists in physical square-loss GD because both initialized predictions tend to zero.

The target is not specified in this example. Vanishing initial predictions give a nonvanishing physical residual only when the fixed target is nonzero. The report permits zero labels elsewhere and correctly recognizes the stationary-residual exception in line 152, so this hypothesis cannot be inferred from a general square-loss convention.

This can be checked directly from the displayed example, without any source theorem. Write the perturbed activation as $\psi_n=\psi+n^{-1/2}$. With the displayed arrays and averaged readout, the reference initial prediction is zero and the perturbed one is

\[
b_n=\frac{1+\pi/4}{\sqrt n}+\frac1n.
\]

For full square loss $(f-y)^2$, the physical descent direction is the feature-ascent direction multiplied by $2(y-f)$. Thus the displayed feature updates $4h\mathbf1$ and $3h\mathbf1$ become

\[
\Delta z_{\rm ref}^{(1)}=8hy\mathbf1,
\qquad
\Delta z_{\rm pert}^{(1)}=6h(y-b_n)\mathbf1.
\]

Their RMS difference is $|2hy+6hb_n|$. For fixed $y\ne0$ this tends to $2|hy|$, as intended. For $y=0$ it is instead $O(|h|n^{-1/2})$. Using half-square loss changes the common numerical factor, not this distinction.

**Minimal accurate fix:** replace the physical-GD sentence with:

> In physical square-loss GD with a fixed nonzero target, for example $y=1$, the residual factors must also be included; the order-$h$ discrepancy persists because both initialized predictions tend to zero while the target remains nonzero.

This is a missing hypothesis in the stated physical extension, not a refutation of the deterministic feature-time objection, the negative audit conclusion, or any Gaussian-typical theorem.

## Scientific scope and implication checks

- **Method obstruction versus model impossibility:** §§4–6 and §§8–9 consistently distinguish failed deterministic estimates, formal Taylor or Stieltjes constructions, bounded-contraction encoders, and ambient regularity bounds from nonexistence of actual population dynamics. The disputed canonical initial-layer claim is explicitly withheld. The valid-flow/non-Lipschitz example is not used to deny flow existence.
- **Symmetry and fitting:** line 470 correctly separates identical-input conflicts, odd-network antipodal constraints, and an even first activation's antipodal constraint. These concern attainable labels and do not preclude a population evolution. The discussion allows a symmetry-changing model adjustment without claiming it supplies response estimates.
- **Activation strength and gain:** the relative-nonaffinity estimate in lines 293–301 follows from the independent-copy variance inequalities as stated for the positive perturbation scales under discussion. The report correctly declines to apply that estimate to the equal-coefficient odd-gain activation. Absolute nonaffinity, moderate relative nonlinear strength, hidden motion, and kernel change are kept distinct.
- **Optimizer and architecture changes:** whitening, frozen layers, coherent initialization, affine first layers, large gains, RMS normalization, and scalar-particle residual architectures are identified as changes of scope. Fixed query clipping is auxiliary dynamics; metric projection is a different rule. No uncut theorem is obtained by combining incompatible caps or weak-defect estimates, and activation rescaling is not presented as a universal physical-time change.
- **Theorem quantifiers:** the summary distinguishes fixed depth from continuous depth, fixed programs from a growing number of updates, local from arbitrary compact-time convergence, finite optimization from population identification, and initial activity from persistent activity. The general local existence theorem's affine/zero-rate cases are not incorrectly assigned its separate nonlinear activity conclusion. The all-depth activation rows retain their depth, separation, label, gain, and step restrictions.
- **Optimization and generalization:** with a uniform positive residual-direction constant, lines 487–494 give exponential decay at rate $4\kappa/m$ for the stated mean-square loss. Initial Gram positivity is not substituted for a trained coercivity estimate. The fixed-accuracy bridge in lines 496–504 preserves the order of quantifiers, and no training-loss result is promoted to a risk theorem.
- **Scientific recommendation:** lines 483–485 recommend controlling the actual reached/comparison response class for a fixed moderately nonlinear model. This is consistent with the qualified evidence. Separation is not asserted to solve trained tails, and the unresolved negative proofs are not treated as constraints that activation design must satisfy.

## All 36 task-map entries checked against the body

Here `PDE` denotes the 17 entries at lines 516–532, and `PDE-2` the 19 entries at lines 538–556. “Consistent” means consistency inside this document, not verification of task identity, remote bytes, chronology, or primary proofs. Entries containing map-only provenance or methods do not automatically create missing theorem obligations in the body.

| Entry | Body comparison and disposition |
|---|---|
| PDE 1 | §7.2: fixed bounded shifted activation, one sample, every separately fixed depth at least three; consistent. |
| PDE 2 | Borel/reconstruction routes remain explicitly conditional in the map; no unconditional body theorem is attributed to them. |
| PDE 3 | §7.2: separation-dependent two-sample activation results retain extension qualification; consistent. |
| PDE 4 | §§8–9: causal comparison, adaptive Gaussian law, projection, and generated-action obstruction retain distinct conclusions; consistent. |
| PDE 5 | §7.1: local positive interval, separate activity result, and finite-GF corollary; consistent. |
| PDE 6 | §§7.3 and 9: original order-one-readout global problem remains distinct from changed activation/readout successes; consistent. The zero-label tanh exception is explicit in the body. |
| PDE 7 | §7.3: original L2 GF prediction/kernel/loss result and fixed-program qualification; consistent. |
| PDE 8 | §6: restricted representation negatives coexist with the operator positive theorem; consistent. |
| PDE 9 | §5.3: adaptive bridge and row-bound defect prevent certification of canonical nonexistence; consistent. |
| PDE 10 | §9: finite RMS action and initial information do not close population gates; consistent. |
| PDE 11 | §6: L2 result and conditional broader proposal do not establish every depth/data case; consistent. |
| PDE 12 | §§5.1 and 6.1: partial quadratic reductions and QI witness do not establish a canonical QQ limit; consistent. |
| PDE 13 | §5.1: depth/activation-specific witnesses and the three-hidden-layer positive prefix are distinguished; consistent. |
| PDE 14 | §§5.2–5.3: formal compiler restrictions and assumed tagged DMFT retain their qualifications; consistent. |
| PDE 15 | §5.1: noncommutative transform/reconstruction remains incomplete; additional map-only mobility/history statements do not claim global identification. |
| PDE 16 | §5.1: output order 17 and Ward-derived hidden information do not supply output order 19 or all-order positivity; consistent. |
| PDE 17 | §4.1: weighted replacement and missing concentration remain visible; consistent. |
| PDE-2 1 | §§7.2 and 7.4: shape-class global result and moderate-sine local result are not merged; consistent. |
| PDE-2 2 | §7.2: later fixed-depth extensions and odd-gain theorem do not answer the no-gain target; consistent. |
| PDE-2 3 | §§7.2 and 7.4: improved two-sample powers do not solve generic three-sample no-gain continuation; consistent. |
| PDE-2 4 | §§7.2 and 7.4: offset/gain results and sharp initialization are distinguished from trained no-gain results; consistent. |
| PDE-2 5 | Explicit recovery-only attribution in the map; no new global theorem is inferred. |
| PDE-2 6 | §§7.1–7.3: arbitrary-angle local, orthogonal global, affine-first, and partial special-angle results have separate scopes; consistent. |
| PDE-2 7 | §§7.1, 7.3, and 8–9: original local proof and finite fitting do not close uncut population continuation; consistent. |
| PDE-2 8 | §§6 and 7.3: corrected sin+cos fixed-program scope and separate linear operator theorem; consistent despite the historical task title. |
| PDE-2 9 | §§5.3 and 7.3: mesh/scaling discussion does not reinstate the withdrawn full nonlinear GF claim; consistent. |
| PDE-2 10 | §5.3 and the map preserve the distinction between located mesh manuscripts and an unrecovered experiment/history record; no additional limit theorem is claimed. |
| PDE-2 11 | §3 and the map distinguish effective mobilities and connector scalings; the missing original nested theorem is expressly uncertified. |
| PDE-2 12 | §4: finite-depth/finite-step comparison remains distinct from mesh refinement; consistent, subject to R1 for the separate physical-GD counterexample. |
| PDE-2 13 | §§7.3 and 9: original order-one-readout continuation remains open; consistent. |
| PDE-2 14 | §§7.3 and 9: exact algebra is not a completed original-model global bridge; consistent. |
| PDE-2 15 | §7.3: exposition is not counted as an independent theorem or review; consistent. |
| PDE-2 16 | §§7.3 and 10: zero-label tanh and scalar-particle residual results retain their limited scope; consistent. |
| PDE-2 17 | §10: scalar-particle joint width/depth result does not establish a dense Gaussian ResNet limit; consistent. |
| PDE-2 18 | §4.1: order-five recurrence and fixed-step identification retain coefficient/dependency and mesh limitations; consistent. |
| PDE-2 19 | §5.1 and the map do not claim that retained high-order proofs exhaust unavailable private amendments; consistent. |

## Optional improvements, not required corrections

1. At lines 472–481, explicitly say “labels +1 and −1, each with absolute prediction error at most $\varepsilon$.” That makes the intended normalization behind $2(1-\varepsilon)$ immediately visible. The displayed necessary readout cost is correct under that binary-label convention.
2. At line 494, spell out “a constant $\kappa>0$ uniform along training.” This makes the intended coercivity quantifier explicit; the surrounding recommendation already treats it as an estimate that must hold during training.

After R1's target qualifier, no further required correction was found at this document-only scope. That assessment does not certify the unread primary proofs or resolve any expressly open population, optimization, or generalization problem.
