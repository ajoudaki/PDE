# Updated revision plan after the latest pull

Compared the reviewed draft at `b7b5424` with the current draft at `7ffb91f`, pulled on 27 September 2026. This is a targeted reconciliation of the existing reviews with the editorial changes, not another independent audit. The manuscript source has not been edited in this task.

## Build and changes

`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed successfully from `paper/`. The updated `main.pdf` has 40 pages, versus 41 in the reviewed snapshot. The final LaTeX log has no undefined references, citation warnings, or overfull/underfull box warnings. The previous comparison-table overflow is resolved. The relocated table, trajectory panel, and supplementary mechanism/moments page were visually inspected.

Six commits mainly reorganize presentation:

- The setting now includes the definition of global approximation and moving state.
- Exact and approximate closure are combined in Section 3; the principal theorems are now 3.1 and 3.2 and appear on page 7.
- Related work and Table 1 follow the experiments, reducing the delay before the construction and guarantees.
- The introductory discussion repeats the state–accuracy axis less often.
- Figure 1 now shows only shared-time radial snapshots. The detailed RMS/sensitivity plot is Figure 9 in the appendix, with the measured maxima retained in the main text.
- The mechanism and moment illustration are Figures 7 and 8 in the appendix. The circle RMS table also moved there. The four-method comparison is now Figure 3.

The source bodies of Appendices A–D are unchanged. `comparison_appendix.tex` and `sphere_appendix.tex` are also unchanged. Consequently, moving these claims or figures has not resolved the scientific and notation issues in the earlier reviews.

## Recommended changes, in order

### 1. Complete or explicitly condition the supporting theorems

Appendix C still invokes the reference exponential-tail bound without supplying it (`main.tex:1599`), along with the initialized-operator/density/moment facts identified by both readers. Appendix D still gives a roadmap for the operator limit (`main.tex:1654`) and a short contraction argument rather than a complete nonclosure proof.

These results can remain part of the motivation, but their evidentiary status must agree with their actual supplied proofs. If the arguments exist in unpublished author material, import the necessary statements and proofs; do not treat that material as an implicit published dependency. Otherwise state the missing hypotheses or label the incomplete arguments explicitly. Also align the introduction and Section 3.1, which still describe these results as established or completely proved.

This remains the most substantial revision. It does not undermine the separate proofs of Theorems 3.1–3.2.

### 2. Complete the notation cleanup

Current locations of the earlier defects:

| Location in `main.tex` | Required correction |
|---|---|
| 1040 | Replace obsolete depth `H` by `L`. |
| 1164, 1375, 1380–1381 | Use the defined Lipschitz constant `Lambda_F` in the exponential instead of undefined `K`. |
| 1237–1238 | Distinguish an n-vector history from its n-by-P matrix of moments. |
| 1401, 1409 | Reconcile leftover `C_T/K_T` and `a*` notation with the surrounding `Gamma_JF/Lambda_F` and forward endpoint `h*`. |
| Setting and history definitions | State the block Euclidean/Frobenius parameter norm and clearly distinguish responses, histories, raw moments, coefficients, and endpoint projections. |

A small notation guide would help more than another global renaming. Figure 8 now needs the earlier Figure 2 caption correction: the plotted quantities are normalized post-hoc polynomial coefficients with an illustrative prefix convention, rather than the algorithm's raw stored moments.

### 3. Retain Table 1's new position; correct its scientific shorthand

The table now fits the page and follows the evidence. Preserve that improvement. Its scientific cells remain essentially unchanged (`main.tex:707–747`): explicitly mark the root-width rate as conditional, distinguish fixed-width parameter error from population prediction error, and identify the NTH horizon and DMFT solver assumptions. Replace the caption's overly specific `n^{-1/2}` characterization of feature corrections with the already-used, defensible phrase “width-suppressed higher kernels.”

The goal is a defensible organizing axis, not to imply that all displayed exponents are published guarantees for one identical target. Appendix E already provides much of the necessary distinction. Put concise status/metric labels in the table rather than adding another long disclaimer paragraph.

### 4. Make two short conceptual corrections

HiPPO wording remains at `main.tex:317–319`, `429–431`, and `801–803`. Feedback alone is not the distinguishing advance: the substantive distinction is paired reconstruction with quantitative, feedback-stable approximation of the specified neural parameter flow.

The two clocks have different backward prefixes. Clarify at `main.tex:1435–1438` that the P=1 coordinate-invariance remark assumes the same prefix and does not identify the two complete algorithms.

### 5. Add the missing experimental context from existing records

Specify the readout law instead of “small” (`main.tex:208–210`). Add the frozen-kernel fit times and conditioning to Appendix I; very long analytic fitted endpoints remain valid for the endpoint-function question, but are different from the common-time panel. Identify binary digits 3 versus 8 in the main MNIST paragraph (`main.tex:677`). Correct the shallow-gallery improvement range to approximately 1.5–3.5 orders of magnitude (`main.tex:610`). These changes require no new training.

## What no longer needs action

Do not repeat the recommendation to move comparison material later: it has been done. Do not restore the long introduction or duplicate the axis discussion. The table overflow is fixed. Moving the RMS panel is acceptable because the main text retains the measured maxima and numerical-sensitivity qualification, with a direct reference to the full plot.

Moving all mechanism illustrations to the appendix is a presentation trade-off, not a scientific flaw. A compact mechanism panel beside the construction could help a less specialized audience, but is optional; there is no need to reverse the new layout before resolving the substantive items above.

## Scientific message to retain

The strongest supported message is unchanged: paired response memories provide an autonomous approximation to deep nonlinear training, with a fixed number of evolving coordinates on each prescribed horizon and a quantitative bound on the full parameter trajectory. The improved reading order helps this message. The next revision should make its proof support and notation equally clear, without expanding the manuscript into another research campaign.
