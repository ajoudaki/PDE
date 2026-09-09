# Independent document-only mathematical review — round 2

Verdict: **NEEDS_CORRECTIONS**.

Two local corrections are required: specify a nonzero target for the physical-GD version of the activation-stability witness, and square the Wasserstein distance in the neuron-pairing bound. Neither correction changes the report's project-level assessment or invalidates its GF/GD diagonal argument. No other required correction was identified in this document-only review.

## Evidence boundary and full-read record

- Sole research evidence: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- SHA256: `9c5a1c80e8eff6975939ed0481e2eaa11a5f6c1bc46ba8b9d2cc11001afcc529`.
- Size: **91,964 bytes; 574 lines**.
- Full-read coverage: **1–574 inclusive, 574/574 lines (100%)**, including every table entry, qualification, and final audit obligation. Fully visible reading coverage was 1–120, 121–180, 181–280, 281–420, and 421–574. The initial combined tool response was truncated; the affected region was reread, including complete reads of 121–180 and 181–280. Additional focused rereading covered 94–119.
- The source hash and size were unchanged when rechecked after the full read and focused checks. Line references below refer to that version.
- Operational instructions only: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, read completely, 115 lines. Its hypothesis and implication checks were applied within the user's document-only boundary.
- No linked source, other project document, source audit, prior review, task history, browser result, or other agent output was read. No experiments or new proof campaign were conducted. The master was not edited; this assigned review is the only file written.

This reviews internal mathematical statements and implications in an accurately qualified synthesis. It does not independently certify the underlying source theorems, coefficient tables, imported proofs, historical read counts, hashes quoted inside the report, or remote task identities. Openly declared missing evidence is not treated as a mathematical defect.

## Required corrections

### R1. The physical-GD discrepancy requires a fixed nonzero target

Location: [§4.2, line 117](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:117), using the arrays at lines 110–114.

The feature-time calculation is correct. The additional sentence that the order-$h$ discrepancy persists in physical square-loss GD “because both initialized predictions tend to zero” omits the necessary nonzero-target hypothesis. Prediction convergence to zero only gives a nonzero limiting residual when the target is nonzero.

This can be checked directly from the displayed witness. Write $\psi_n=\psi+n^{-1/2}$. Its reference prediction is zero, while the perturbed first hidden vector is $n^{-1/2}\mathbf 1$, its second preactivation is $e_1$, and its prediction is

\[
f_{n,\mathrm{pert}}
=\frac{\psi(1)+n^{-1/2}}{\sqrt n}
=\frac{1+\pi/4}{\sqrt n}+\frac1n.
\]

For half-square loss and the same physical step $h$, the two first-preactivation increments therefore are

\[
\Delta z_{\mathrm{ref}}^{(1)}=4hy\mathbf 1,
\qquad
\Delta z_{\mathrm{pert}}^{(1)}=3h(y-f_{n,\mathrm{pert}})\mathbf 1.
\]

Their RMS difference is $|h|\,|y+3f_{n,\mathrm{pert}}|$. At $y=0$ it is $O(|h|n^{-1/2})$, whereas for fixed $y\ne0$ it converges to $|hy|$. Full-square loss multiplies both increments by two and gives the same distinction. Section 4.2 does not specify a nonzero target.

Minimal accurate fix: replace the physical-GD sentence with:

> For a fixed nonzero target, for example $y=1$, the residual factors in physical square-loss GD converge to a common nonzero value, so the order-$h$ discrepancy persists.

This preserves the deterministic counterexample at its valid scope. It does not establish a Gaussian-typical counterexample, and the report correctly refrains from that inference.

### R2. The neuron-pairing estimate bounds squared Wasserstein distance

Location: [§7.1, line 253](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md:253).

The sentence says that pairing neurons bounds the hidden-path $W_2$ distance by their averaged **squared** uniform-path difference. As written, this misses a square on $W_2$, or a square root on the average. For empirical path laws with the same number of neurons, the coupling gives

\[
W_2(\mu_n,\widetilde\mu_n)^2
\le \frac1n\sum_{i=1}^n
\|H_i-\widetilde H_i\|_\infty^2.
\]

For example, if every first path is identically zero and every second path is identically $\varepsilon\in(0,1)$, the distance is $\varepsilon$ and the average squared difference is $\varepsilon^2$. The unsquared inequality asserted by the wording is false.

Minimal accurate fix: insert “square of the” before “hidden-path $W_2$ distance.” Both sides of the corrected estimate tend to zero as needed, so the deterministic-mesh diagonal and the finite-GF corollary remain valid at the stated scope.

## Other mathematical checks

1. **Gaussian conditioning and reuse, lines 72–77 and 408–413.** The finite conditioning formula has the correct random mean $a_n\mathbf 1$ and conditional covariance $\|g(y)\|_2^2P/n$. The replacement of $a_n$ by $\mathbb E g'(G)$ is explicitly a limiting operation. The later generated-action example is internally consistent: the even bump removes the first forward-query response, while the next forward call retains the transpose response with coefficient $\mathbb E[G\tanh G]=\mathbb E\operatorname{sech}^2G$. The displayed Gaussian innovation variance and the $\varepsilon^{1/p-1/2}$ concentration scale are compatible with that construction. The report correctly fixes $\varepsilon$ before taking width to infinity and does not identify these queries as actual training queries. This is an internal consistency check, not certification of an unread generated-action proof.

2. **GF/GD diagonal, lines 246–261.** Apart from R2, the logic is sound. For nonnegative square loss and fixed nonnegative mobility, $\|D_n\nabla\mathcal E_n\|^2\le\|D_n\|\nabla\mathcal E_n^TD_n\nabla\mathcal E_n$ yields the displayed integrated speed bound. On a finite interval it supplies a Cauchy endpoint at any hypothetical finite escape time. Finite-dimensional local Lipschitzness supplies continuation and fixed-width Euler approximation. Convergence in probability at each fixed width permits a deterministic sufficiently fine mesh with the stated error probability. The universal deterministic-mesh hypothesis then permits the triangle argument. No width-uniform Euler rate, global population continuation, or same-neuron coupling across arbitrary mesh sequences follows or is claimed.

3. **Formal versus actual no-gos, lines 125–176.** The report consistently separates fixed-order annealed coefficients, formal inversion, positive Taylor approximation families, assumed tagged dynamics, and actual neural trajectories. The nonzero initial residual at lines 152–166 is the appropriate clock-invertibility condition. The explicit Gaussian example $g(t)=\mathbb E(1+t^2G^2)^{-1}$ is smooth by Gaussian moment domination, has even Taylor coefficients $(-1)^k(2k-1)!!$ and zero radius, and is exactly represented by the displayed smooth autonomous ODE. The counterexample refutes the stronger smooth-ODE inference without supplying a neural closure. The canonical initial-layer claim remains qualified; the frozen-bottom, fixed-step, and fully trained assertions are not conflated.

4. **Clipping, lines 347–392.** The three constructions have distinct rules, scales, and conclusions. The comparison error tends to zero for $R_n=o(\log n)$ because its logarithm is $-(\log n)/24+o(\log n)$. Closeness of two varying constructions does not prove convergence of either. For the metric projection, the box normal satisfies $u_R^Te_R=R\|e_R\|_1$, agreeing with the displayed identity. The integrated normalized $L^1$ defect controls bounded tests, but does not imply squared-defect or excess-work convergence. The coefficient-dependent $C\sqrt n$ inactivity statement and its extension to all physical time on the fitting event are appropriately separated from a fixed-cap population theorem.

5. **Other displayed formulas and scientific scope.** The identity for $D^3f$ at lines 83–96 has the correct coefficients and is explicitly distinguished from $J_{\phi,L}$. Output order 17 supplies eight output moments after the stated inverse/composition/shift; the extra Ward-derived hidden order is not promoted to output order 19. The one-sample kernel floor, feature hitting time, physical clock, and loss exponent at line 282 agree. The relative-nonaffinity bound at lines 293–301 follows from the two independent-copy variance bounds and is not incorrectly applied to equal linear/nonlinear coefficients. The depth asymptotics at line 337 are consistent with the cubic expansion of the stated activation. The mean-loss dissipation factors at lines 487–494 and the prescribed-accuracy probability inequality at lines 496–504 are correct. Fitting symmetry obstructions are distinguished from existence of a population evolution. None of these checks certifies numerical constants or larger theorem proofs merely quoted from sources.

## All 36 task-map entries checked against the body

The first group contains 17 entries and the second 19. Their numbering is internally complete. The following records the body comparison for every entry; no substantive scope contradiction was found. Exact identity and historical attribution cannot be independently verified under the document-only boundary.

| Map group / task number | Body comparison and disposition |
|---|---|
| PDE / 1 | §7.2: fixed-depth bounded shifted activation, one sample; global scope agrees. |
| PDE / 2 | Map-only Borel/basis reconstruction details remain conditional; no unconditional body theorem is attributed to them. |
| PDE / 3 | §7.2: two-sample offset/separation extension and dependency qualification agree. |
| PDE / 4 | §§8–9: adaptation, caps, projection, and generated-action obstruction are retained at their separate scopes. |
| PDE / 5 | §7.1: positive local interval and finite-GF corollary agree; R2 is a local estimate correction. |
| PDE / 6 | §§7.3, 9: original order-one-readout global problem remains open; the zero-label stationary exception does not contradict this. |
| PDE / 7 | §§7.3, 11: older L2 GF scope and import qualification agree. |
| PDE / 8 | §6: bounded-contraction representation restrictions coexist with the operator positive. |
| PDE / 9 | §5.3: the canonical initial-layer claim remains unclosed. |
| PDE / 10 | §9: finite RMS identities/global finite GF remain distinct from population and kinetic gaps. |
| PDE / 11 | §6: L2 spectral description and conditional broader-depth identification agree. |
| PDE / 12 | §§5.1, 6.1: QI/IQ algebra and model-specific negative remain separate from canonical existence. |
| PDE / 13 | §5.1: activation/depth-specific signs and finite positive prefixes agree. |
| PDE / 14 | §5: formal/compiler negatives and assumed tagged-model scope agree. |
| PDE / 15 | §§4–5.1: missing noncommutative transform/reconstruction is retained; extra method/history details do not promote a global theorem. |
| PDE / 16 | §5.1: output order 17, Ward-derived hidden order, and open all-order positivity agree. |
| PDE / 17 | §4.1: weighted replacements and the outstanding concentration step agree. |
| PDE-2 / 1 | §§7.2, 7.4: shape extension, moderate sine local result, and qualification agree. |
| PDE-2 / 2 | §7.2: all-fixed-depth extension and odd-gain result agree; no no-gain conclusion is inferred. |
| PDE-2 / 3 | §7.2: improved two-sample exponent agrees; generic three-sample no-gain scope remains open. |
| PDE-2 / 4 | §§7.2, 7.4: gain/shape and initialization results retain their separate quantifiers. |
| PDE-2 / 5 | Recovery-only entry, consistent with §2's history-access qualification. |
| PDE-2 / 6 | §§7.1–7.3: local, orthogonal, affine-first, and special-angle results remain distinct. |
| PDE-2 / 7 | §7.3: original L3 local theorem and finite GF/GD coercivity do not become global population identification. |
| PDE-2 / 8 | §§6, 7.3: corrected sin+cos fixed-program result and separate deep-linear theorem agree. |
| PDE-2 / 9 | §5.3: quadratic/ReLU mesh distinctions and withdrawn broader inferences agree. |
| PDE-2 / 10 | §5.3: limited mathematical scope agrees; unavailable attribution/history is explicitly qualified. |
| PDE-2 / 11 | §§1, 3: scaling distinction is compatible; the unrecovered nested primary theorem is not certified. |
| PDE-2 / 12 | §4.1: finite-depth/fixed-step package is not a mesh-refinement theorem. |
| PDE-2 / 13 | §§7.3, 9: original-model continuation remains open and history remains qualified. |
| PDE-2 / 14 | §§7.3, 9: original autonomous algebra does not become an established global limit. |
| PDE-2 / 15 | §7.3: exposition is not counted as a new theorem or independent audit. |
| PDE-2 / 16 | §§7.3, 10: stationary tanh and scalar-particle versus dense ResNet distinction agree. |
| PDE-2 / 17 | §10: the scalar-particle width/depth theorem is retained without a dense-network inference. |
| PDE-2 / 18 | §4.1: order-five and finite-step machinery retain their fixed-order/step scope. |
| PDE-2 / 19 | §5.1 and §2: local moment results agree; no exhaustive private-history claim is made. |

## Optional improvements

None is needed to resolve this review beyond R1 and R2. Adding primary proofs or repairing the openly marked research dependencies is outside the required correction scope. The existing qualifications should remain visible after these two local edits.
