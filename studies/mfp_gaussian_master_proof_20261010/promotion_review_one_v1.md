# Complete independent scientific promotion review ONE — candidate v1

**Verdict: acceptance blocked by one required code/semantics correction.** The finite Gaussian theorem and its supplied proof dependencies pass this review. The displayed worked examples and their maintained producers pass within their stated scopes. The implementation does not consistently preserve the documented independent frozen-seed convention under current-state substitution and repeated updates. This objection is not waived by the 67 passing supplied tests.

Reviewer: `/root/promotion_review_one_v1`. Date: 2026-10-10.

## Independence and input scope

I received the neutral `promotion_review_assignment_v1.md` and the frozen candidate location in a fresh review context. I am none of the authors/assemblers or the selector listed in the packet manifest. I neither authored, assembled nor selected this candidate. I performed the complete theory, implementation, tests, examples and attribution audit myself. I did not divide the work, spawn another reviewer, contact the other reviewer, or read author discussion, study history/README, internal reports, selection findings, other reviews, other studies or `old_docs/`.

I read `AGENTS.md`, all of `RESEARCH_WORKFLOW.md`, `explain-with-canonical-notation/SKILL.md` and its neural-response-memory reference, and `solve-math-rigorously/SKILL.md`. I used those process requirements without doing ordinary author startup. A read-only Git metadata check before writing this report showed HEAD `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`, no staged entries, and unrelated concurrent tracked changes. I did not inspect their contents or modify the index, Git history, live maintained sources or other tasks' files.

All reviewer-generated files are in `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v1/reviewer_one/`, apart from this assigned report. No stochastic training experiment or external scientific retrieval was performed.

## Required correction R1: fixed seeds are rebound during optimizer substitution

The guide, lines 162–170, defines `freeze(value)` as independent seed data with the base state's value, and defines its derivatives as partial derivatives on the enlarged parameter/seed space. The `freeze` and `directional` docstrings agree: the datum is fixed during physical differentiation. Under that convention, for a trainable vector \(x\in\mathbb R^n\), seed \(b=x_0\), loss

\[
\mathcal L_n(x;b)=\frac1n\sum_i x_i b_i,
\]

and vector mobility \(n\), the scaled gradient is \(b\). Two gradient steps of size \(\eta\), with the independent seed fixed, give \(x_2=x_0-2\eta b=(1-2\eta)x_0\).

The following admitted program instead returns \((1-\eta)^2x_0\):

```python
from fractions import Fraction
from pde.mfp_compiler import Program
from pde.mfp_finite import evaluate_finite

p = Program()
x = p.root("x", p.vector_type("a"))
seed = p.freeze(x)
loss = p.mean(x * seed)
state = p.gradient_descent(
    loss, vectors=[x], steps=2, step_size=Fraction(1, 10)
)
print(evaluate_finite(state[x], 2, {x: [1, 2]}, {}))
# Actual:   (Fraction(81, 100), Fraction(81, 50))
# Fixed-seed result: (Fraction(4, 5), Fraction(8, 5))
```

The cause is `code/pde/mfp_compiler.py:545–546`: `Program.at` rebuilds a `freeze` node with substituted children. `gradient_descent` invokes that substitution on the gradient at line 580 (and matrix-gradient factors at lines 551–554, 578). Thus, at the second step, the stored seed expression is evaluated from the current state. This is a seed refresh, although the specified enlarged parameter space has not supplied a seed update. Directly, `p.at(seed, {x: 2*x})` evaluates to `(2,4)` on the same fixture, whereas the initially assigned seed is `(1,2)`.

This is also a convention conflict with moving derivatives: treating the field as `-freeze(x)` gives zero derivative of that frozen factor, as appropriate for a fixed independent seed, while the update helper rebinds its value at each new state. A fresh seed at every step can be a legitimate different algorithm, but it needs an explicit contract and cannot simultaneously stand for the fixed datum described here.

**Required resolution:** make seed lifecycle explicit and consistent across `at`, `gradient_descent`, and moving derivatives. Preserve independent seed data during current-state evaluation, or separate a deliberately refreshed stop-gradient operation from fixed seeds, or reject unsupported combinations with a precise documented restriction. Add a meaningful multi-step fixed-seed test, including a represented matrix seed/direction if supported. I am not prescribing a particular API redesign. The present silent refresh is a blocking semantics defect for this candidate's declared operation set.

The exact reproduction, successful surrounding attacks, and actual/expected values are retained in `reviewer_one/independent_probes.py` and `reviewer_one/independent_probes.log`.

## Theory audit

**Theory verdict: PASS for the stated mathematical language.** I found no additional proof correction or missing scientific dependency. This does not remove R1 from the complete promotion candidate.

I reconstructed the proof as follows:

- The primitive language is finite and chronological, with constant-coordinate deterministic vectors, fixed Gaussian root tuples, fixed named matrices joining distinct equal-width types, same-type maps/contractions, and causal scalar feedback. It excludes width-dependent coefficients, coordinate selection, general index contractions and inverses. Independent root tuples may be singular. Parallel named edges and cycles of types do not create cycles in the instruction order.
- Conditioning on the roots and complete transcript preserves a product of residual Gaussian matrix laws. Each new query conditions only its own named residual factor. The extension from adjacent layers therefore retains the finite-rank projection estimate and the source-response cancellation. Paths through other matrix names remain in the explicit input expression. Distinct oriented source groups are independent; outputs need not be. Input second moments are uncentered source covariances.
- The source rule retains every formal call argument at singular covariance. Gaussian integration by parts and contraction with the associated input family make support ambiguities harmless only after the formal partials have been taken. The supplied bounded-program proof removes singularity by independent input perturbations and continuity of positive semidefinite square roots, without taking a limit of Gram inverses.
- In the raw-entry moment induction, the matrix product-rule remainder contains at most the fixed derivative order many earlier-node terms. For a moment tuple with \(b\) distinct indices and \(s\) singletons, the commuting zero-entry differences cancel every omitted singleton. Repeated fundamental-theorem integration supplies the additional singleton factors. The strengthened induction applies to the same raw derivatives evaluated after selected entries have been scaled, including zero variance. Cauchy–Schwarz gives \(n^{-(p+s)/2}\le n^{-b}\); the \(O(n^b)\) tuple count then closes the moment bound. The empty-singleton case needs no Taylor remainder and is included. This induction uses only finitely many earlier derivative bounds for each requested order/moment.
- Cutoffs include scalar arguments and scalar arithmetic. Their derivatives have common polynomial-growth profiles. Interpolation upgrades the earlier \(L^2\) errors to the \(L^4\) errors needed for polynomial difference bounds. The operator-norm fourth moment controls \(We\) even when \(e\) depends on \(W\). This proves clipping removal uniformly in width, including scalar broadcasts and feedback. Gaussian-prefix square-root couplings and polynomial dominators identify the unclipped source evaluator. The separate uniform higher moment bound upgrades probability convergence to every finite scalar \(L^p\). Tuple RMS couplings yield empirical \(\mathcal W_2\) convergence.
- Forward AD propagates through scalar feedback; formal source partials hold its already-computed scalar values fixed. Reverse AD uses vector adjoints \(n\,\partial O/\partial u\), ordinary scalar adjoints and ordinary matrix gradients. Both orientations and every shared occurrence accumulate. Normalized rank-one lowering and Frobenius contractions have the stated factors. Current ambient gradients are formed before state substitution; history pullbacks are different quantities.
- Fixed-order moving jets use derivatives of the field itself and factorial-normalized coefficients. Smooth finite-dimensional local existence is sufficient; no common width-dependent horizon is claimed or needed. Fixed updates and finite jets close the language, but neither an infinite series nor a positive-time reconstruction follows.
- The activation-moment reduction is correctly restricted to nonlinearities of designated original centered initialization preactivations. Adjoining linear Gaussian integration coordinates does not replace the source arguments used by formal differentiation. Stein reduction terminates by removing explicit Gaussian polynomial factors and remains valid at singular covariance.

The neural specialization retains shared first-layer columns, actual reused hidden matrices, fixed data geometry and block mobilities. It explicitly chooses order-one stored readout, and does not silently apply the fixed-law theorem to the default width-dependent small-readout law. The half-mean loss in the kernel example changes the physical clock explicitly. The new text preserves the older finite-second-moment-root/C1 foundation and the separate lower-regularity specialization.

## Code and example audit

**Code verdict: correction required (R1).** Apart from that objection, I found the examined implementation consistent with its declared finite operations and Gaussian algorithm. I read all code paths in the three new modules, including error checking, exact arithmetic, PSD validation, aliases, scalar nonlinear feedback, source covariance allocation, response construction, adjoint accumulation, simultaneous substitution, optimizer lowering, expression simplification, and the finite interpreter.

**Examples/producer verdict: PASS in their stated scopes.** All three producer families and all five Python blocks in the MFP guide ran from the standalone edition. The new examples do not use frozen seeds in repeated optimizer state substitution, so R1 does not invalidate their displayed outputs.

I independently checked the reuse finite-width identity \(q+c^2+(E[\gamma^2\phi(\gamma)^2]-q-c^2)/n\), its two-occurrence matrix gradient, the saved pre-update-vector formula \(15+(3-15\eta)^2\), duplicate singular queries, the moving/frozen values \(120\) and \(30\), and the factorial coefficient \(60\). The MLP derivative has the correct independent centered-readout cancellation, and its metric norm is \(s_1s_2+q_1s_2+q_2\).

For the linear kernel example, I checked the physical half-loss factor, shared input-column derivative, the trace moments \(E\operatorname{tr}(WW^T)/n=1\) and \(E\operatorname{tr}(WW^T)^2/n=2+1/n\), and the \(5+4+4\) contributions after the product-rule factor two. These give the stated second derivative \(18\lambda_a\lambda_b\), hence \(J_2=9\lambda_a\lambda_b\) and the displayed \(9/4\) formula for two samples. The disappearance of residual-derivative terms uses both the scalar moment theorem and readout oddness, rather than simply freezing residuals.

The quadratic kernel polynomial was regenerated, and the supplied exact finite dense backpropagation/series tests passed at widths two and three, including all moving blocks, residuals, geometry and labels. The initial kernel follows from two fourth-moment computations. I did not treat the equality of the generic-atom specialization and direct polynomial compilation as an independent asymptotic proof: they share the source-rule implementation, as the guide discloses. Its support is the audited exact finite AD, audited general Gaussian algorithm/proof, regenerated output, and disclosed regression checks. I found no contradiction in that evidence or the polynomial's degree, symmetries, degenerate geometry or label dependence.

## Executed checks and independent attacks

The working directory for numerical commands was the frozen `edition/`. Every such command set `PYTHONPATH=code`, `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, and used `python -B`; the unit suite also set `MKL_NUM_THREADS=1`. Outputs were redirected outside the edition into `../reviewer_one/`. Thus imports used the standalone code, with no live checkout or study implementation on the import path.

1. `python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v`: **67 tests passed**, 20.298 seconds, exit 0. Full log: `unit_tests.log`.
2. `python -B code/scripts/example_mfp_calculus.py`: exit 0; `calculus_example.log`.
3. `python -B code/scripts/example_mfp_mlp_derivative.py`: exit 0; `mlp_example.log`.
4. `python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir ../reviewer_one/kernel_producer`: exit 0. Complete symbolic, identity and quadratic text/JSON graphs and their producer manifest were generated freshly. The identity branch is also the guide's separate identity command, executed here through `all`.
5. The five complete `python` blocks extracted verbatim from `code/MFP_CALCULUS.md` were executed as `python -B ../reviewer_one/guide_snippets.py`: exit 0; `guide_snippets.log`.
6. `python -B ../reviewer_one/independent_probes.py`: exit 0. It includes the following independent attacks:
   - Enumerated raw-entry Gaussian Wick contractions for \(\|WVW\mathbf1\|^2/n\), with independent named edges \(W:a\to b\), \(V:b\to a\). At widths 1, 2, 3 the exact finite expectations are \(3,3/2,11/9\), agreeing with \(1+2/n^2\); the compiler gives the limiting value 1. This exercises a cycle of types and repeated forward reuse.
   - Tested singular duplicate cubic-call cancellation and preservation of a frozen value's formal Gaussian source path. Both pass.
   - Differentiated an independently implemented dense tanh network with the cycle \(a\to b\to a\to b\), reused transpose, and nonlinear scalar feedback by central coordinate differences. All vector, matrix and scalar gradients agreed after their declared normalizations. Maximum absolute discrepancy was \(2.94\times10^{-11}\), below the declared \(10^{-8}\) comparison threshold.
   - Reproduced R1 exactly with rational finite arrays; the script records the mismatch rather than asserting a false pass.
   - Checked a current **matrix** ambient gradient against a history pullback independently at width one: \(9/5\) versus \(81/50\), both correct.
   - Rejected an indefinite zero-pivot covariance, a rational covariance just beyond the PSD boundary, and NaN covariance. All pass.

The first probe run ended on a reviewer-harness scalar-versus-length-one-tuple assertion, after already printing R1. That log is retained as `independent_probes_attempt1.log`; correcting the harness comparison to its sole coordinate produced the complete successful execution above. A separate attempted harness edit initially used the wrong relative scratch path and changed no source. Neither issue was a candidate failure.

Environment: Python 3.10.12, NumPy 1.26.4, Linux 5.15.0-151-generic x86_64, glibc 2.35. These checks are deterministic and contain no training campaign. The central-difference comparison is numerical evidence, while the rational/Wick probes and supplied rational checks are exact.

## Assembly, attribution and complete read coverage

I read every line of every item in `review_packet/`, including the 992-line proposed theory, all four dependency excerpts, four origin metadata files, patches, bibliography addition, mapping, assembly script, manifests, provenance main text and supplied H/I/J excerpt. I also read `candidate_mapping.json`. The complete required edition reads were:

| File under `edition/` | Lines read |
| --- | ---: |
| `code/MFP_CALCULUS.md` | 403 |
| `code/README.md` | 1266 |
| `code/pde/__init__.py` | 26 |
| `code/pde/gaussian_moments.py` | 114 |
| `code/pde/mfp_compiler.py` | 785 |
| `code/pde/mfp_expr.py` | 426 |
| `code/pde/mfp_finite.py` | 140 |
| `code/scripts/example_mfp_calculus.py` | 103 |
| `code/scripts/example_mfp_kernel_jets.py` | 112 |
| `code/scripts/example_mfp_mlp_derivative.py` | 69 |
| `code/tests/test_mfp_compiler.py` | 534 |
| `code/tests/test_mfp_expr.py` | 189 |
| `code/tests/test_mfp_kernel_jets.py` | 304 |
| `code/tests/test_mfp_mlp_example.py` | 65 |
| `docs/_quarto.yml` | 68 |
| `docs/index.qmd` | 260 |
| `docs/notation.qmd` | 98 |
| `docs/references.bib` | 74 |

Packet dependency coverage is complete: Chapter 2 opening, 251 lines; finite-jet section, 153; contained A.1–A.4, 76; bounded Gaussian law III.F.1–III.F.6, 369. The two attribution text inputs were read fully (786 and 914 logical text lines respectively). Counts in `read_coverage.json` use Python `splitlines`; PDF text form feeds also count as separators. Truncated tool displays were repaired, specifically the process/skill batch and the opening of `docs/index.qmd`.

The source-response theorem is a genuine dependency and was audited in full. The source provenance says “Chapter 13” by its book chapter number; the frozen source file is correctly `docs/12-three-sample-learning.qmd`. No missing dependency was inferred from that filename difference.

I verified that the proposed theory appears exactly once at assembled Chapter 2 lines 252–1243, immediately after rational Gaussian moments and before the existing finite-calculus section. I inspected the adjacent assembled context and each of the three replacement texts. Removing the exact insertion and reversing those three replacements reconstructs the baseline Chapter 2 SHA256 `c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723`, matching the supplied origin metadata. All four dependency excerpt ranges match their origin source bytes. The candidate mapping and packet mapping agree. A metadata-only identifier check found all 38 native references used by the new theory and no duplicate among its 46 defined identifiers. This is not a claim that I rendered or independently reviewed the full book.

The attribution is appropriately limited: the new raw-entry bound credits the moment mechanism in Golikov–Yang Appendix J and proves the needed Gaussian specialization itself. The supplied J excerpt contains the derivative-moment induction, shrunk-entry setup and singleton-cancellation/Taylor mechanism. Although that excerpt ends during the final J.4 bound, it is an attribution input, not an unproved theorem imported into the candidate. The candidate's singleton difference proof supplies the whole needed bound and explicitly includes the empty-singleton case. I found no unsupported priority claim or attempt to present the external master theorem as a newly established general result.

**Unread complement:** I did not scientifically read the remainder of the assembled book outside the assigned Chapter 2 excerpts/insertion/context, bounded-program excerpt, index, notation, configuration and bibliography. I did not audit unrelated implementation modules or their producer/test families; the complete code README was read as the assigned interface context. `finite_network.py` was imported as the existing parent-package dependency and was hashed, but its algorithm was not reread. Other source files were hashed or scanned for identifier metadata only, not accepted as proof dependencies. The full external PDFs, appendices outside the supplied attribution excerpts, and all study history remain unread. Whole-book rendering, independent integration review and user approval remain separate gates.

## Initial/final integrity and completion evidence

At both boundaries, every manifest-listed source matched its recorded hash: 116 edition files, 14 changed edition paths and 17 packet files. The manifest files themselves had identical initial and final SHA256 values:

| Manifest | SHA256 |
| --- | --- |
| `candidate_manifest.json` | `6fe911cd2013d240f8015e182966452ca595dfe26b60d2d29214f9ebfc369aef` |
| `changed_manifest.json` | `285700c19e090a3a7557d27d7272b82fe1425c3973e908857b20cac609b52dff` |
| `review_packet/manifest.json` | `3cf5f0c941ffffe439da4d6adafc73117a99c136d65b017015a5796c91796f03` |

The exact initial inventory is `reviewer_one/initial_hashes.json`; the exact final manifest-input inventory is `reviewer_one/final_hashes.json`. `verify_packet.py`, `verification_summary.json`, `verification_summary.log` and `read_coverage.json` retain the complete checks and coverage. In particular the new theory hash is `793e65c40302c1d48a36054897c1d2b22a58b71eccc5d777eec930e19ba8882f`, and the compiler hash is `ca48becf732dea0254d43aa49163829696b5c28d2f6d7503c7b53ee72a77d0a2`.

An initial overly broad whole-directory comparison also included unlisted Quarto render caches/products. Those changed or appeared concurrently during the review; I did not create, read or rely on their contents. I narrowed the final integrity comparison to the frozen manifest inputs and verified all of them unchanged. No scientific input drift occurred. This distinction is retained rather than claiming the entire edition directory was immutable.

The full assigned scientific audit is complete. There is one unresolved required correction, R1, and no missing scientific input. **Do not accept candidate v1 unchanged.** A corrected candidate needs the fresh complete paired reviews required by the workflow; this report is not a partial permission to promote its other components.
