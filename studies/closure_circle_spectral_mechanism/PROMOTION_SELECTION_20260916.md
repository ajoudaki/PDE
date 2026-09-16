# Independent relevance and placement selection — package C

Date: 2026-09-16. Selector: `/root/select_c`, a fresh scoped agent distinct
from the study authors and the future candidate assembler. This is the
workflow's relevance/placement gate, not either adversarial correctness review
or approval to change established material. No candidate chapter, implementation,
training run, or Git write was produced.

## Recommendation

**Accept for narrow assembly as explanatory mathematics attached to the existing
closure and frozen-kernel sections.** The distinct value is to tell a reader
what the retained order restricts, what its exact symmetries imply, and which
kernel is the appropriate frozen comparator. These statements remain useful
without resolving nonlinear prediction selection or demonstrating an advantage
of increasing order.

The smallest useful package has three closure remarks and one compact analytic
baseline example. Extend `docs/global_nonlinear.md` C.4.7.10.B/C.1 for the closure
remarks and the frozen-flow discussion around (C5.11) for the analytic example.
Do not add a chapter, new milestone, second closure implementation, or numerical
campaign. A brief explanation in `code/README.md` may point to those remarks;
no maintained API change is needed for this package.

## Selection by component

| Source component | Decision | Distinct value, overlap, scope, and smallest destination |
|---|---|---|
| THEORY §§1–2: initialized-mark dictionary, polynomial dimensions, ridge filtering, fixed action factorization | **Merge as context; decline independent re-promotion.** | C.4.7.9 parts 2–4 and C.4.7.10.B already give the joint marks, unrestricted characteristic coordinates, dimensions, ridge contraction and actual transpose. Restate only the minimum notation needed for the new interpretation. Cite existing (H3.1), (H3.2), (H3.N1)–(H3.N2). |
| THEORY §3: antipodal oddness and absence of a Fourier cutoff at fixed order | **Accept, with an explicit representability scope.** | Every finite represented state satisfies `f(theta+pi)=-f(theta)`; all even Fourier coefficients vanish. The explicit finite-state family in §3 has no finite trigonometric support, and each prescribed odd frequency can occur while N remains fixed. This closes a plausible misunderstanding of the established dictionary. Place after (H3.N2), using B's dictionary as context. It does not show that prescribed-initialization training reaches the witness. |
| THEORY §4: parity invariant subsystem and N=1/N=2 equivalence | **Accept narrowly as a conditional exact remark.** | Existing B says degree-two additions are even and may be inactive; the study supplies the full invariant-subsystem argument. Require a common sign-symmetric joint mark law, parity-preserving coefficient and population integration, the same positive ridge, identical active initialization, and uniqueness in the stated solution class. Then only odd-to-odd action coordinates evolve and the two active systems coincide. The maintained ridges differ and its default Halton cloud is not sign-paired. No equality or small-error assertion for the default runs is accepted. Place immediately after B's paragraph on odd orders. |
| THEORY §6: exact closure kernel blocks, Gram positivity, and its own frozen kernel | **Accept as one local identity, merging duplicated energy content.** | (H3.N2) and (H2.7) already give the gradient dynamics and dissipation. Writing the three blocks explicitly in those feature coordinates identifies the actual comparator and exposes the population-weight metric. Keep `K_c=E_2[H(u)H(v)]`, `K_M=(d(u)^T d(v))(a(u)^T a(v))`, and `K_w=(u dot v)E_1[q(u)q(v)s(u)s(v)]`, with `s=1-h^2`. At `c=0`, the latter two vanish; freezing `w,M` gives the same initial kernel while readout training remains linear. Place beside (H3.N2); derive it briefly rather than introducing a second general kernel theorem. |
| NTK_THEORY: nested Gaussian covariance kernel and equal-weight opposite-label pair/Fourier formula | **Accept narrowly as an analytic example.** | C.5 already defines the Gaussian feature covariance, the frozen solution, and population initial-kernel/readout-kernel equality. Its explicit stationary circle specialization and pair Fourier sampling factor are useful new reader-facing identities. Include the nested covariance formula, the positive antisymmetric eigenvalue, exact physical-time gain, and the Fourier coefficient with its sign and normalization. This explains why sample spacing can alter a frozen predictor's spectrum and why its normalized pair spectrum is constant over positive time. Place adjacent to (C5.11), clearly outside the fixed three-point risk theorem's statement. No nonlinear approximation or superiority theorem is inferred. |
| NTK_THEORY: arbitrary weighted, possibly singular frozen-Gram spectral solution | **Hold outside the minimal package.** | Correctly distinguishes `KW` from the symmetric `W^(1/2)KW^(1/2)` and treats nullspace coupling. The selected pair example needs only its scalar eigenmode. A general weighted-kernel API or standalone reusable baseline section would justify this extra algebra; neither is needed here. Named assembly question: whether there is a maintained consumer needing weighted/singular behavior. This is an editorial/use-case gap, not a demand for new research. |
| THEORY §2: initial action rank at most four, and the parity improvement at N=1,2 | **Merge only if one sentence helps the dictionary explanation.** | The bound is an immediate consequence of established (H3.1)'s two two-column contractions. It adds no closure convergence statement. Restrict to the requested fast-core orders and exact arithmetic; do not attach the bound to learned M or to the rank of its accumulated update. No separate proposition is warranted. |
| THEORY §5: hypothetical N=0 and the frozen comparison | **Narrow to an API clarification.** | Positive integer order is already enforced. Say that a frozen kernel is a separate choice at each order and that N=0 is not a maintained solver member. The hypothetical constant-only dead system is unnecessary in the smallest addition. Do not introduce or reserve a new N=0 API. |
| THEORY §6: initial nonlinear/frozen difference `O(t^3)` | **Decline as a separate addition.** | The finite smooth closure argument is valid at its stated local fixed-resolution scope, but C.5 already contains a stronger model-specific cubic calculation and actual-flow remainder. It is unnecessary for the selected order interpretation and must not be promoted into a general population onset theorem. |
| THEORY §7: complete-state rotation covariance and non-rotation-closed N=1 mark span | **Hold outside the minimal package.** | Potentially useful for a future supported anisotropy diagnostic. The selected material needs only the warning that an individual closure's frozen kernel need not equal the stationary population kernel. Failure of span invariance does not prove that any particular prediction is anisotropic. No observed anisotropy magnitude is accepted. |
| THEORY §8: first-harmonic interpolation and degenerate pair geometries | **Merge one caution and necessary boundary cases.** | The explicit first harmonic shows that close opposite labels can be fitted by increased amplitude without high Fourier degree. Retain that caution if interpreting the pair spectrum; retain conflicting coincident labels and the consistent antipodal case as boundary conditions. Avoid enlarging this into a bandwidth-selection theory. |
| THEORY §3: state-dependent analytic-strip Fourier decay; §9 experimental designs | **Decline from this addition.** | Decay is compatible with absent finite support, but quantifying it is unnecessary to the selected conclusion. The designs are research proposals, not results. No new experiment is authorized by this screening. |

## Non-negotiable scope and assembly requirements

The common model is bias-free, exactly two-hidden-layer tanh, normalized
direction `u=x/sqrt(2)`, unhalved probability-weighted squared loss and physical
time. The finite network has stored Gaussian variances `(1,1/n,1/n^2)` and
mobilities `(n,1,n)`. Its actual finite random readout is retained in any
finite-width statement; only the population initial readout is zero.

The three representations must remain separately typed:

1. A finite quadrature closure has fixed weighted mark tables and unrestricted
   moving `w,c,M`. Its all-state oddness, representability witness and kernel
   identities need no long-time neural-limit theorem.
2. An exact symmetric mark-law closure supports the conditional parity
   conclusion. Finite coefficient quadrature Q, population replay P, ridge,
   arithmetic, time integration and angular sampling are separate choices.
3. The full initialized neural population has the stationary nested Gaussian
   covariance kernel. A finite-order closure has its own projected initial
   kernel, which is generally a different function.

For item 1, zero-weight nodes can be omitted; positive weights make the stated
inverse-probability metric unambiguous. Derive the kernel in that metric, not
the unweighted Euclidean metric of the stored node arrays. The dissipation
claim is for exact GF, not arbitrary Heun steps.

For item 2, either retain the source's explicit population existence/uniqueness
condition or invoke the precise bounded-feature characteristic well-posedness
already proved in C.4.7.9 part 4. Do not silently infer a global canonical
neural-flow theorem from global existence of a fixed finite closure. State that
the default `eta_1=1/4096` and `eta_2=1/9216` violate matched-ridge equivalence.
No new matched-ridge solver option is part of this selection.

For item 3, include the direct finite-query initialization argument already in
NTK_THEORY if asserting initial finite-network identification; this needs no
later trajectory theorem or certificate. At a finite width the hidden tangent
blocks are small but not identically zero. The Fourier convention must be
explicit. THEORY §8 and NTK_THEORY orient the opposite labels differently;
choose one orientation and preserve its signs. Retain the physical loss factor
two and the pair's half weights. A frozen model's exact infinite-time linear
solution is not a settled nonlinear endpoint assertion.

Use N exclusively for closure order in this addition. A Fourier mode index
must be a different symbol. Neither the witness's free shape parameters nor
the study's fitted shape parameter are mobilities `kappa_ell` from NOTATION.
The canonical draft must not reuse the study's fitted parameter as a learned
selection law.

## Explicit exclusions and costs

No universal monotone order improvement, bandwidth law, `kappa(p)` law, fitted
tanh–sine theorem, settled nonlinear endpoint, off-support teacher accuracy,
finite-width rate, new C-H1–C-H4 completion, or broader-horizon convergence is
accepted. The study's numerical reconstructions and order comparisons remain
study evidence; no empirical performance table or figure is selected.

Maintenance cost is low for the selected mathematics: local algebraic proofs,
one fixed-state representability argument, one conditional parity proof and a
short scalar frozen example. The main cost is preventing notation/scope drift
between exact mark laws, finite quadrature and the neural population. Reusing
the existing equations avoids another solver contract. Promoting NTK.py would
introduce SciPy, rank/PSD tolerance semantics, quadrature behavior and a separate
numerical public interface; promoting ENGINE.py would introduce PyTorch and a
second backend. **Neither code promotion is selected here.**

The distinction between represented and reached states is the leading review
risk. The proof that high odd frequencies are available at fixed N does not
identify the output selected by its prescribed initialization and training
law. Sign symmetry excludes even modes but does not select odd coefficients.
An apparent order trend has no exact consequence beyond the established
qualitative hierarchy theorem on its own stated law family and limit order.

## Read coverage, checks and provenance

Read completely, with truncated reads repaired:

- `AGENTS.md`; all of `RESEARCH_WORKFLOW.md`; `docs/README.md`;
  `docs/NOTATION.md`; `code/README.md`; this study's `README.md`.
- This study's `THEORY.md`, `NTK_THEORY.md`, `NTK.py`, `NTK_CHECK.py`,
  `ENGINE.py`, and `ENGINE_CHECK.py`.
- Maintained `code/pde/observable_solver.py`, `observable_initialization.py`,
  `observable_words.py`, `observable_arithmetic.py`, and `finite_network.py`.
- Complete relevant established units in `docs/global_nonlinear.md`:
  C.4.7.9 opening and parts 1–4, ending immediately before part 5
  (current lines 12083–12377); C.4.7.10.B and C.1 (13161–13522);
  C.5's entire analytic body from its heading through “Finite clocks and
  limitations” (21314–21967). Also inspected surrounding material at
  12000–12082 and 12795–13160 to locate boundaries; those fragments are not
  substituted for complete dependency proofs.
- Complete retained deterministic records
  `data/generated/closure_circle_spectral_mechanism/ntk_checks/initial_01/check.json`,
  `worker_checks/cpu/checks.json` and `worker_checks/cuda/checks.json`.
- Required skills `solve-math-rigorously` and `investigate-conjectures`, with
  the latter's evidence-ledger and adversarial-audit references.

Targeted searches of established docs and the code guide checked placement and
duplicated terminology. The rest of the established chapters, C.5's later
computer-assisted certificate, generic compiler/fixed-arithmetic dependency
proofs, campaign producers/arrays and empirical analysis were not audited.
They are unnecessary to this restricted relevance decision. No other study's
scientific contents, links, history, summaries or agent findings were read.
Git status exposed other path names only as permitted coordination metadata.
The study README was read because the assignment required it; its internal
verdicts and authors' significance language are not evidence for this decision.
SYNTHESIS_AUDIT and other author/reviewer assessments were not used.

Checks performed here were complete source reading, algebraic comparison,
scope/duplication assessment and SHA-256 correspondence. No deterministic
suite or campaign was rerun, and this report makes no new reproduction claim.
The existing NTK record reports maximum 128/192-node kernel change
`4.9044e-14` and weighted matrix-exponential discrepancy `9.9921e-16`;
its claimed status concerns finite-rule diagnostics, not certified continuum
error. The existing closure CPU/CUDA records report maximal algebraic
discrepancies `4.9961e-16` and `3.3307e-16`. All sources named by those three
records match their current recorded hashes. Those checks support source
consistency; they do not replace the required fresh candidate reviews.

HEAD observed: `04b61a12795734cbfc93830bf0a164bab7d101c4`. The shared tree had
pre-existing modifications and untracked paths; none was reset, staged or
adopted. Only this assigned report was written.

Current scientific source SHA-256 values:

```text
a7686b0155bd34eb01ac8431fd187c42ac235d3d1703b269cdc789f9f8c92414  THEORY.md
6ce8d478bf8373d5adde95b088f5185bf0e4078f192b7677ed1f2a2531f2234f  NTK_THEORY.md
91ecb96a8966d60174e1517bc94769e72b2e11eecfb2128dc0fecc019cc001fc  NTK.py
a0f8a4ea9288fb02cdb8bf10d47daf593404846c6352d73aeafb8f7e7398e8c5  NTK_CHECK.py
67b381262927ac9416046a46ab95826c914b47f20e08eb184fa63ffd8335993d  ENGINE.py
b56e6165063e8501093fbffd0c176e5c8daf3d175fcf21840f039d3d3f7cf123  ENGINE_CHECK.py
cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629  docs/global_nonlinear.md
711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605  code/pde/observable_solver.py
6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2  code/pde/observable_initialization.py
b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5  code/pde/observable_words.py
2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb  code/pde/observable_arithmetic.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
```

The next authorized action is assembly of this narrowed mathematical package
inside this originating study, followed by the workflow's complete fresh
reviews and proposed-edition validation. This selector must not act as either
adversarial reviewer. Established-file edits still require approval of the
concrete reviewed addition.
