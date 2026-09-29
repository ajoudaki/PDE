# Evidence log: current-draft critical review

## Review Format Resolution

Author-requested, author-owned, venue-neutral feedback, as specified in `../ASSIGNMENT.md`; no numerical score or acceptance recommendation. No confidential-venue policy gate applies. Read the complete review-ai-paper skill and its severity rubric before assessing claims. Review date: 2026-09-27. Only frozen scientific inputs under `../inputs/` were read. No other study, previous draft/review, live manuscript, Git history, or other role's output was inspected. No agents were delegated and no training was run.

Severity distinguishes demonstrated falsehood, incomplete proof, unverified evidence, and acknowledged scope. No fatal flaw was established. The two major findings below concern supplementary theorems, not a dependency of the core response-memory guarantees.

## Inventory and read coverage

- Main submission: all 1,954 lines of `main.tex`, all 390 lines of `comparison_appendix.tex`, all 29 lines of `sphere_appendix.tex`; 41-page `main.pdf`; supplied extracted text. All sections, theorem statements, proofs, captions, tables, discussion, and bibliography in the submission were read.
- Visually inspected rendered PDF pages 2, 6, 9, 13, 14, 19, 22, 23, 24, 28, 31, 34, 37, 39, 40. These cover the mechanism and moments, main comparison table, common-time and four-method plots, central proof equations, exact-compression statements, NTH/Jackson calculations, MNIST and factor figures. Not every PDF page was visually rendered; complete textual reading was through source.
- Statically read complete `figures/capture_trajectory.py` (316 lines), `frozen_ntk.py` (189), `learning_controls.py` (188), and `scripts/tikz_figures.py` (1,128). Inspected all five NPZ bundles with `allow_pickle=False`, their shapes, selected embedded provenance/metrics, and manifest metadata. Did not follow embedded links to study artifacts.
- Verified all 31 SHA-256 entries of `inputs/manifest.json`; every listed file exists and matches. `main_extracted.txt` is an additional supplied file, not one of these hash entries.
- Core response-memory/factor engines and original experiment producers are referenced outside the frozen packet. The packet intentionally contains paper-owned evidence only. Their omission is a **verification limit**, not evidence that the files are absent from the repository or an intended public release. Likewise the joint-clock sweep, frozen-dictionary numbers and 1,000-image MNIST result lack independently executable producers/results in this packet. No claim of absence beyond the packet is made.

## Scientific contract reconstructed

The proved target is a specified finite-width, finite-depth, scalar-output, full-batch squared-loss gradient flow with block mobilities `(n,1,...,1,n)`, over every prescribed finite physical-time horizon. The physical comparison is the whole parameter vector; continuity gives hidden-response and bounded-test-input prediction control. The method retains the dense initialization, outer weights, and per-training-sample, per-neuron forward/backward memories. It compresses the moving learned hidden matrices and their response-history representation. It does not prove width-independent order, long-time-uniform error, total-storage savings, runtime savings, successful fitting, or a fixed-order population limit.

The population conjecture and conditional costs are explicitly identified in Sections 6.7 and Appendix E. They do not follow just from the fixed-width theorems. The finite-width diagonal argument is valid but need not preserve `mP<n`.

## A. Critical citations: theoretical dependencies

The core proofs rederive their approximation input and use elementary energy, projection, compactness and Gronwall arguments; no unverified external theorem is indispensable to Theorems 6.1–6.2. The following primary full-text sources were retrieved for attribution and scope, rather than treated as proof substitutes.

| Source and retrieval | Exact material checked | Invocation verdict |
|---|---|---|
| Gu et al., [HiPPO](https://arxiv.org/html/2008.07669), arXiv v2, 2020-10-23; full HTML available | Theorem 2, Eq. (3), Appendix D.3; Sections 2.5 and 4/Figure 2 | LegS online projection attribution is valid. Normalized coefficients `c_k=sqrt(2k+1) H_k/tau` give its lower-triangular recurrence after changing time. HiPPO also explicitly allows memory-dependent inputs and recurrent feedback, so feedback by itself is not the new ingredient. The present training-trajectory feedback theorem remains distinct. L3. |
| Huang–Yau, [Dynamics of Deep Neural Networks and Neural Tangent Hierarchy](https://arxiv.org/html/1909.08156), full arXiv HTML accessed 2026-09-27; submission cites the unversioned record | Assumptions 2.1–2.2, Theorem 2.6, Eqs. (2.8)–(2.9), Section 2 new-input evaluation | Appendix E's exchanged width/sample symbols, training RMS normalization, even-order restriction and horizon agree. Smooth derivative/data/kernel-eigenvalue assumptions are not assumed satisfied by the present setting; they are explicitly marked incomparable. Invocation valid as a comparison, not as a theorem for the present flow. |
| Nguyen–Pham, [published full article](https://ems.press/content/serial-article-files/29198), MSL 6 (2023), pp. 201–357 | Quantitative comparison statements around Theorems 4.7, 4.12–4.13, Proposition 4.14, printed pp. 224–229 | Retrieved source supports a rate below root width in its stated general theorem and a more specialized bounded-initialization estimate. It does not establish the manuscript's matched A1. Appendix E labels A1 as a hypothesis; Table 1 should display that qualification in the cell. No complete assumption-transfer to the manuscript's Gaussian-operator parameterization was verified or claimed. L2. |

The NTH source controls a different scaling and a training-output norm on a restricted horizon. No inference that it subsumes response memory, or that response memory dominates it, follows. The manuscript's own mobility-matched hierarchy in Appendix E is instead a chain-rule identity. I checked its recursion, repeated-integration bound, factorial-kernel sufficient condition, Lambert-W allocation, and the scalar `f(theta)=theta^2` example directly. These steps are sound under their expressly conditional coefficient bounds. Tanh analyticity alone would not justify those bounds; the draft correctly says so.

## B. Critical citations: empirical baselines or methodology

| Source | Checked material and conclusion |
|---|---|
| Bordelon–Pehlevan, [DMFT full text](https://arxiv.org/html/2205.09653), arXiv v3, 2022-10-04 | Appendix B, Algorithm 1: covariance/response kernels indexed by input and time; sampled paths; per-path causal/Jacobian solution; iterative kernel estimates. The manuscript's streamed storage/work counts are reasonable implementation upper bounds. A grid-uniform contraction, Monte Carlo error bound and solver-order bound are added hypotheses, not the cited algorithm's theorem. Their absence is acknowledged in Appendix E. |
| Finite empirical NTK control | No external numerical baseline is imported: the packet provides its block formulas, kernel arrays, test cross-kernels, analytic flow and fitted times. Formula independently checked by finite differences on a tiny network; stored endpoint calculations checked. All three parameter blocks are present with correct mobilities. |
| Direct factor control | Frozen evidence describes `W0+AB`, `A(0)=0`, Gaussian `B`, unit factor mobilities, and canonical outer mobilities. Its induced matrix velocity is `-grad_W L B^T B - AA^T grad_W L`, not canonical matrix flow. This is a legitimate test of whether rank alone reproduces the chosen predictor. The draft correctly limits the claim to this baseline. It is not a comparison to all low-rank training methods. |

Tensor Programs IV, the 2023 finite-width DMFT paper, InRank, and background citations were not independently audited in this bounded pass. They are not treated as verified premises of the main mathematical results. No numerical or novelty criticism is based on an unretrieved source.

## C. Potentially missing citations or baselines

No uncited method is asserted to subsume the result. The only concrete attribution correction is L3: cite the already-cited HiPPO paper's recurrent use accurately and distinguish the **closed approximation of a specified training flow with a parameter-error theorem**. A physical-time clock ablation would illuminate the benefit of the chosen clock, but its absence is already acknowledged and is not a logical flaw in the clocks' proved guarantees.

Local attempts to preserve four source PDFs in `cited_papers/` failed because shell DNS/network access was unavailable. Browser retrieval of the primary full text succeeded. No local PDF is claimed saved. No permission escalation was needed or requested.

## Mathematical audit and findings

### Core speed-clock proof: checked, sound after local notation repairs (L1)

1. `F=-D grad L` gives `dL/dt=-||D^(-1/2) theta_dot||^2` and the finite-time path bound, so arbitrary locally regular activations do not cause finite-time dense-flow escape.
2. For a history with the specified constant/zero prefix, differentiating raw minus projected energy gives `D_q'=rho ||q-q*||^2`. The polynomial space in absolute history coordinate is fixed as an algebraic space; basis dilation cancels. Initial projection error is zero, including the backward prefix.
3. Differentiating the bilinear reconstruction gives the endpoint product defect. Cauchy–Schwarz controls its **absolute time integral**, not merely a signed endpoint matrix discrepancy. This is the key bridge to stability.
4. Endpoint evaluation has norm `P/sqrt(tau)`. Combining it with the Legendre H1 tail gives `(P+1)/P<=2` in Eq. (19); the stated coefficient is consistent. Forward derivative control then propagates layer by layer without losing order.
5. Raw backward mass is bounded; forward projection error is order `P^-2` in squared norm. Their paired defect is order `P^-1`; Gronwall and first exit close the argument. The all-orders bounded-activation extension uses a valid readout-energy bound and downward recursion, with no apparent circularity.

### Core joint-clock proof: checked, sound after local notation repairs (L1)

1. Matching both prefix responses and subtracting the prefix product preserve the initialization. Weighted projection and the Gram ODE reproduce the same product-defect identity.
2. A lower dense-residual bound and a stopped tube avoid dividing by zero. Projection contraction first bounds total physical variation independently of order; a bound on `D Psi` then bounds the clock without assuming it. This is a substantive noncircular step.
3. `d mu <= d xi` and the jointly unit-speed concatenated path give a single squared-tail bound. Applying `2 sqrt(ab)<=a+b` gives order `P^-2` for the accumulated defect.
4. The reconstruction's physical velocity cancels all clock-speed terms. Therefore `g=rho+||D Psi V||` is explicit and locally Lipschitz. First-layer `C^(1,1)` suffices because the memorized backward path starts at layer 2; second derivatives are needed only at subsequent layers.
5. The prefix guarantees positive definiteness of the Gram matrix at every fixed order and bounded clock. The proof does not claim an order-uniform minimum eigenvalue. This suffices for continuation but not numerical conditioning.
6. Checked Appendix E.4's Hilbert-valued Jackson argument: the positive even trigonometric convolution has degree below P with the specified N, its norm bound is dimension independent, and weighting by actual history mass gives Eq. (47). The final width-uniform controls remain hypotheses.

### M1 — Supplementary population closure requires unprovided scientific lemmas

Locations: Appendix C, pp. 25–28; `main.tex:1563–1743`, especially 1662–1669, 1693–1699, 1713–1735. The Osgood calculation is valid **if** its preceding differential inequality holds. The frozen text does not construct the correlated Gaussian initialized operator/observable probability spaces, prove density of the enumerated initialization programs for the evolving response curves, or state/prove the required uniform exponential tail bound for the reference backward field. Bounded L2 operator action alone does not supply such tails. The sentence that finite-N characteristic equations are locally Lipschitz also needs a space and appropriate moments, because ridge-normalized observables can be unbounded. The final claim for every quadratic observation needs corresponding uniform-integrability/moment control.

Classification: major gap in the supplied proof, not a demonstrated counterexample. Repair by supplying the missing lemmas with hypotheses or stating the theorem conditionally. Consequence: C.1/C.2 and the claimed *established* population example cannot currently carry the same evidentiary weight as 6.1/6.2. No cascade to the finite-width theorems or their corollary.

### M2 — Exact operator and scalar-nonclosure theorems are not proved in the supplied appendix

Locations: Section 5, pp. 7–8; Appendix D, p. 28, `main.tex:1752–1799`. D.1 gives a theorem followed by a one-paragraph roadmap: the initialized word-statistics/Fock construction, trace-class invariance, limit interchange and width-uniform Euler argument are not present. “Order-one initialization” is insufficient to specify the distribution/normalization behind its probability limit and zero initial output. D.2 gives the large-contraction idea but no derivation showing nonzero survival of the chosen contraction under repeated physical-time differentiation, no exact graph-independence statement accounting for index symmetries, and no definition/proof of the additional finite-order local-PDE clause.

Classification: major missing support for auxiliary results, not evidence that those results are false. Finite block differentiation is consistent with the displayed cubic equation; the contraction obstruction is plausible. Complete the theorems or present them as proof sketches/conditional background. They motivate but are not used by the main response-memory proofs.

### L1 — Local notation defects and type collisions

- Eq. (13), p. 19, line 1162: undefined upper limit `H` should be depth `L`.
- Eqs. (22), (31), (32), pp. 21/24, lines 1286, 1497, 1502–1503: `K` is undefined; the preceding Lipschitz constant is `Lambda_F`. Later Appendix D uses K for the tangent kernel, so leaving K implicit is especially unhelpful.
- Appendix A opening, lines 1090–1095, introduces barred h as a history; Appendix B line 1359 uses barred h for both an n-vector history and an n-by-P moment matrix in one equation. Use separate history/matrix symbols and include dimensions. State the parameter norm explicitly as the block Euclidean/Frobenius norm.

Classification: minor mathematical/presentation repair; no new argument needed.

### L2 — The comparison table is less precise than its appendix

Table 1, p. 6, `main.tex:372–407`, juxtaposes root-width **conditional** population error, NTH's source-scaling training error, numerical DMFT “step size,” and the proved finite-width parameter errors. The caption and Appendix E qualify much of this, so it is not an unqualified dominance claim. Still, the cells do not describe one established common-metric theorem. Put the target observable and status in each row; display `conditional n^-1/2`, identify the NTH width-dependent horizon, and make DMFT's numerical order/sampling/iteration qualifications visible. Fixed initialization/tensor/evaluator storage should accompany the moving-state column. This is a localized reporting correction; the conditional algebra in Appendix E survives.

### L3 — Sharpen the HiPPO novelty sentence

Section 6.4, lines 633–635, and Section 6.2, lines 511–514, present endogenous feedback as the difference from HiPPO. HiPPO Sections 2.5 and 4 already discuss memory-dependent inputs and recurrent architectures. The defensible novelty is the paired reconstruction and feedback-stable approximation of **the full specified parameter gradient flow**, with the endpoint-energy cancellation and clock control. This correction strengthens the conceptual claim rather than reducing the core theorem to a routine HiPPO application.

### L4 — Prefix and plotted-coordinate conventions need an explicit bridge

Section 6.3 gives a zero backward prefix; Appendix B changes to `b(0)` and subtracts its product. Both are correct but are different algorithms. The statement at lines 1557–1560 about unchanged P=1 dynamics is true for **coordinate changes with the same prefix**, not a blanket equivalence between the two displayed constructions. At P=1, the difference in their reconstruction functional includes `-(2/nm) sum_a b_a(0)[H_a/(1+int rho)-h_a(0)]^T`, which need not vanish. Say this explicitly.

Figure 2's renderer uses `legfit` coefficients `c_k=(2k+1)H_k/tau` and a zero-origin post-hoc history, whereas the main algorithm's stored variables are raw moments with a unit prefix. Label the lower distributions as projection coefficients, or describe this normalization/prefix convention. This affects exposition, not the main estimates.

### L5 — Specify initialization and show the control horizons

Section 3, lines 313–315, says the stored readout is “small.” The control code actually uses normal readout entries divided by n. Initialization determines the empirical kernel and is central to interpretation; state this law for the main experiments. For the strongest frozen-kernel example, the saved MSE crossing is about `7.086e7` in physical time; the center/edges example uses `3.329e9`. These are valid analytic endpoints, with checked small spectral/cross-formula errors, but are not the `[0,80]` common-time experiment. Add the already-saved fit times and kernel conditioning in a compact table. No new control or kernel tuning is required to substantiate the current scoped conclusion.

## Executed verification

Working directory for the substantive check: `/home/amir/Codes/PDE/paper/reviews/20260927_current_draft/reviewer`.

Exact command:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python /home/amir/Codes/PDE/paper/reviews/20260927_current_draft/reviewer/scratch/check_frozen_evidence.py
```

Exit 0; Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. Complete executable procedure and results are in `scratch/check_frozen_evidence.py` and `scratch/check_results.json`. It reads only frozen inputs, imports the inspected kernel helper without its main function, disables bytecode writes, and writes only its scratch JSON. No training, downloads or external writes.

Material results:

- All manifest hashes match; 31 entries.
- Recomputed all 30 shallow/deep circle discrepancies, all five P3/factor/NTK control rows, all three MNIST prediction discrepancies, and all three sphere discrepancies from stored prediction arrays.
- The 29 resolved wins/28 wins over factor two are consistent with **saved aggregate metadata**; only P3 across all five tasks and the paired-task arrays have independent raw-prediction confirmation for factors. This distinction matters.
- Common-time error and sensitivity arrays agree with their independently recomputed formulas. P1/P3/P7 maximum saved errors are 0.0709651, 0.00587917, 0.000175201. Among 38 positive times, 2/16/32 respectively have discrepancy at or below the saved numerical-sensitivity scale. Thus much of the very-small-P7 signal is unresolved relative to that diagnostic, as the caption permits.
- Independent tiny-network finite-difference NTK block error: `2.824e-11`. Torch is unavailable, so the authors' autograd test was not rerun. The complete stored-kernel spectral/exponential checks remain numerically consistent; the largest recomputed training cross-formula error is `1.756e-8` in the ill-conditioned center/edges case.
- A random well-conditioned raw-state algebra check of the joint reconstruction derivative gives max error `2.442e-15` against the product-defect expression. This supports the algebra, not global convergence by experiment.

Other executed utilities: `rg`, `sed`, `nl`, `wc`, `ls`, `pdfinfo`, and bounded Python inventory/hash/metadata scripts. PDF render command template, for each of the 15 pages listed above, was `pdftoppm -f PAGE -l PAGE -r 95 -png -singlefile INPUT/main.pdf reviewer/scratch/page_PAGE`; all exited 0. An initial attempted PyMuPDF rendering/import exited 1 because `fitz` was unavailable; Poppler supplied the successful fallback. Four `urllib.request.urlopen(..., timeout=20)` PDF-download attempts failed with DNS errors and wrote no files. No failing result is counted as successful verification.

## Coverage limits and assessment

Strong confidence in the checked core finite-width arguments and packet-level arithmetic; moderate confidence in the auxiliary population/linear claims because indispensable arguments are not supplied; moderate novelty confidence restricted to the primary sources checked. No independent training rerun, all-seed robustness study, population-limit proof, broad novelty search, or complete implementation audit of omitted solvers was performed. The substantive new result that survives is a causal paired-memory approximation with quantitative finite-horizon feedback control, not a proved canonical population model of learning.
