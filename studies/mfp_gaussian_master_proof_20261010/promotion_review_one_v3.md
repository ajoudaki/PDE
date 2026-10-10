# Complete scientific promotion review ONE — candidate v3

**Verdict: PASS.** The theory, implementation, tests, and worked examples pass this complete scientific review for their stated fixed finite Gaussian scope. I found no required correction, missing scientific input, or unresolved correctness objection. This verdict is not the separate integration review, a whole-book audit, or approval to promote.

Reviewer identity: `/root/promotion_review_one_v3`. Review date: 2026-10-10. Assignment: `promotion_review_assignment_v3.md`. Frozen run: `data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v3/`. All paths in this report are relative to `/home/amir/Codes/PDE` unless explicitly absolute.

## Independence and completion

I received the neutral assignment in a fresh isolated context and read the full assignment before scientific work. I am distinct from every author/assembler and the selector listed in `review_packet/manifest.json`. I did not receive or read study history, the study README, author reports, selection reports, previous reviews, another reviewer's findings, other studies, archived book material, or external scientific material beyond the supplied provenance texts. I did not delegate this review or communicate with the other reviewer. My only outgoing coordination message to the supervisor reported my own completed reads, checks, and report progress. No author explanation was requested or used.

I read all the required process sources: `AGENTS.md`, the complete `RESEARCH_WORKFLOW.md`, the canonical-notation skill and its neural-response-memory reference, and `solve-math-rigorously`. Their exact hashes and line counts, together with the neutral assignment's hash, are retained in `reviewer_one/process_input_hashes.json` under the frozen run. These process hashes were recorded at completion; the scientific manifests were verified both before and after work.

All scientific/code reads listed below are complete, with no unresolved truncation. I completed the theoretical reconstruction, adversarial checks, code and producer review, deterministic runs, correspondence checks, and original report. I wrote only this assigned report and files in the assigned `reviewer_one/` scratch directory. I made no Git mutation, live maintained edit, frozen-source edit, stochastic training run, or external write. No fresh clone or worktree was created.

## Frozen-input identity and exact read coverage

These manifest hashes were identical at the initial and final checks:

| Manifest | SHA-256 | Entries checked |
| --- | --- | ---: |
| `candidate_manifest.json` | `541b0e75982342c181a99801cdb36269b4a1cc2a40c6e792799a3cce5da6f653` | 116 |
| `changed_manifest.json` | `ff6d10776f3add6a276f39be80e23a3517cf2b6d007a20c1eb40fa62299a69d8` | 15 |
| `review_packet/manifest.json` | `7c23c3faae35fb0a1ae4fb292d603145e54896260f3eedd3cfd71966d1f13fd9` | 18 packet hashes |

Every listed source hash matched its actual file at both checks. The initial and final records are `reviewer_one/initial_manifest_check.json` and `reviewer_one/final_manifest_check.json`. The complete per-file read inventory, line counts, and exact SHA-256 values are retained in `reviewer_one/read_coverage_hashes.json`; this is part of this review's evidence, not an author report.

I read every line of these scientific and implementation inputs:

| Frozen input | Complete line range |
| --- | --- |
| `review_packet/promotion_theory.qmd` | 1–1010 |
| `review_packet/dependency_chapter2_opening.qmd` | 1–251 |
| `review_packet/dependency_chapter2_finite_jets.qmd` | 1–153 |
| `review_packet/dependency_chapter2_specialization.qmd` | 1–76 |
| `review_packet/dependency_finite_gaussian_law.qmd` | 1–369 |
| Each of the four excerpt `.origin.json` files | 1–8 each |
| `review_packet/promotion_assemble.py` | 1–96 |
| `review_packet/promotion_book_patches.json` | 1–14 |
| `review_packet/promotion_code_mapping.json` | 1–13 |
| `review_packet/promotion_code_readme_patches.json` | 1–10 |
| `review_packet/promotion_quarto_patches.json` | 1–7 |
| `review_packet/promotion_bibliography.bib` | 1–8 |
| `review_packet/provenance_non_gaussian_tp_main.txt` | 1–786 |
| `review_packet/provenance_appendices_H_I_J.txt` | 1–927 |
| `review_packet/provenance_sources.json` | 1–16 |
| `edition/code/MFP_CALCULUS.md` | 1–416 |
| `edition/code/README.md` | 1–1266 |
| `edition/code/pde/__init__.py` | 1–26 |
| `edition/code/pde/gaussian_moments.py` | 1–114 |
| `edition/code/pde/mfp_expr.py` | 1–426 |
| `edition/code/pde/mfp_compiler.py` | 1–791 |
| `edition/code/pde/mfp_finite.py` | 1–140 |
| `edition/code/scripts/example_mfp_calculus.py` | 1–103 |
| `edition/code/scripts/example_mfp_mlp_derivative.py` | 1–69 |
| `edition/code/scripts/example_mfp_kernel_jets.py` | 1–112 |
| `edition/code/tests/test_mfp_expr.py` | 1–189 |
| `edition/code/tests/test_mfp_compiler.py` | 1–637 |
| `edition/code/tests/test_mfp_mlp_example.py` | 1–65 |
| `edition/code/tests/test_mfp_kernel_jets.py` | 1–304 |
| `edition/docs/index.qmd` | 1–260 |
| `edition/docs/notation.qmd` | 1–98 |
| `edition/docs/_quarto.yml` | 1–68 |
| `edition/docs/references.bib` | 1–74 |

I also read the complete three manifests and `candidate_mapping.json`. In the assembled Chapter 2, I inspected the inserted theory, its placement immediately after the exact rational Gaussian-moment section, the following section boundary, both amended opening paragraphs, and the amended A.2 interface passage. The inserted theory occupies assembled lines 252–1261 exactly; the three replacements occur at lines 5, 7, and 4370. The four old scientific excerpts were checked against their complete original ranges, not reconstructed from descriptions.

Unread complement: the other scientific portions of the frozen book, and implementations/tests/guides not enumerated above, were not given a fresh substantive audit. The full code README was read as required, but its unrelated established module and campaign claims were not reopened. `finite_network.py` was imported through `pde` during checks; it was not read as a new numerical algorithm, consistently with the assignment. A metadata-only identifier/reference scan covered the other frozen book files; it does not count as a scientific read. No scientific dependency was silently imported from those unread portions.

## Theory audit

### Language and source law

The theorem's scope is a fixed finite acyclic computation, with equal width, a finite list of named independent Gaussian matrices joining distinct vector types, same-type iid Gaussian root tuples, fixed means/covariances, and smooth activation derivatives of polynomial growth at every fixed order. Singular roots and query Grams are admitted. Constants and deterministic parameters stay fixed with width. The forbidden operations—coordinate selection, arbitrary tensor contraction, inverse operations, and width-dependent coefficients—are not used to obtain a stronger result indirectly.

I reconstructed the causal source law. For each matrix orientation, its covariance is the uncentered second-moment Gram of its input representatives. The opposite-orientation response differentiates the already constructed input in each separately named source slot, with prior scalar expectations and covariance entries held fixed. Source groups are independent; fields need not be. The response sum includes source paths through other named matrices. A singular joint Gaussian law does not identify formal variables before differentiation, and no unstable Gram inverse enters evaluation.

The bounded-derivative dependency is fully supplied and proved. Its successive conditioning argument preserves the product of residual matrix factors even for adaptive queries. The proposed extension to parallel edges and cycles of vector types is justified: each observation still conditions only one named residual factor, and the rank of each revealed query space is bounded by the fixed call count. It does not require a feedforward ordering of vector types. The program chronology supplies the required ordering. The conditional test-variance and second-moment calculations, finite-rank projection removal, integration-by-parts cancellation, and distinct independent input perturbations for singular queries apply at every edge.

The scalar extension is causal. A Lipschitz map of a vector and preceding scalar values gives the displayed RMS bound; normalized averages use Jensen, scalar maps preserve convergence, and matrix calls use the initialized operator bound. There is no implicit fixed point and no derivative through deterministic limit coefficients in a source partial.

### Uniform moments and clipping

The raw-entry lemma uses the correct strengthened induction: all derivative orders and finite moments are proved for each earlier node uniformly over independent Gaussian entry variances in `[0,1/n]`. At each fixed width, polynomial growth already supplies integrability, so the proof does not assume the desired uniform conclusion to justify its integrations.

I checked the matrix step in detail. With an even moment of a row sum, a pattern with `b` distinct entries and `s` singleton entries contributes at most `C n^{-(p+s)/2}` after applying the commuting zero-entry differences. Every omitted inclusion-exclusion term has a centered singleton factor independent of the remaining integrand. Replacing all selected entries consistently in the entire reused array is essential and is done explicitly. The resulting derivative is taken in raw coordinates before evaluation at the shrunk array. Its second moment is bounded by the earlier-node induction, including zero variances. There are no inverse shrink factors. Since `p+s >= 2b`, summing the `O(n^b)` index choices leaves a uniform bound. The `s=0`, zero-variance, repeated derivative-index, and transpose cases are included. Remainder terms from differentiating the matrix factor number at most the fixed derivative order. Scalar feedback and normalized averages do not introduce hidden powers of width.

The cutoff profiles are uniform at every fixed derivative order. Although cutoff Lipschitz constants need not remain bounded as the cutoff grows, the proof needs common polynomial-growth profiles, which it has. Higher moments upgrade the inductive input errors from `L²` to the `L⁴` errors used with polynomial factors. The matrix-error estimate uses Hölder with the operator norm, so it remains valid for errors correlated with the reused matrix. No independence assumption is inserted there.

For the limiting evaluator, continuous positive-semidefinite square roots provide Gaussian couplings even at rank loss. Locally convergent clipped derivatives and common polynomial bounds give a Gaussian dominator at each finite step. This justifies convergence of the input Grams, response expectations, and field moments. The finite-width comparison, followed by the fixed-cutoff limit and then cutoff removal, proves convergence in probability. Uniform moments of an order greater than the requested `p` prove the stated scalar `L^p` convergence. The same-coordinate RMS coupling and triangle inequality establish the same-type empirical `W₂` result. This proves convergence of expectations; it is not inferred from probability convergence alone.

### Physical differentiation and the activation normal form

The finite derivative tables match actual differentials. For a scalar observable `O`, the vector adjoint is `b_u=n∂O/∂u`, while matrix adjoints are ordinary Frobenius gradients. In particular, `dO=b_v^T(dA)u/n` gives `b_v u^T/n`, with the factors reversed for a transpose call. Broadcast/scalar contributions carry the necessary normalized average. Every occurrence of a shared matrix contributes.

Represented increments have a fixed finite number of normalized outer products. Differentiating their coefficients and factors, lowering their actions, and taking the admitted Frobenius contractions closes the primitive language. Ambient current gradients must be formed before substituting a trained state; the candidate correctly distinguishes this operation from a derivative through the update history. Simultaneous fixed updates preserve the representation.

The jet convention is factorial-normalized and physical. Repeated moving differentiation includes `DO[DV[V]]`; a frozen direction omits that term by a declared enlarged-space partial derivative. The finite Taylor composition and local finite-dimensional ODE argument need smoothness only to the requested finite order and supply no common width-independent time interval. Differentiation is completed before the width limit. Explicitly frozen seed values retain their random source dependence, even though physical derivatives and subsequent state substitutions keep them fixed.

The initialization moment reduction has the needed syntactic restriction. Nonlinear arguments are designated original preactivations; auxiliary nonlinear derivative fields and updated preactivations are excluded. Original preactivations and later named Gaussian sources form a finite joint Gaussian integration family on each type. Stein reduction removes one explicit Gaussian polynomial factor at each step, including when its derivative hits an activation. Singular covariance is handled by a Gaussian square root. Thus termination and the finite polynomial assembly follow without introducing covariance inverses. This is not claimed for arbitrary nonlinear programs, which retain general integrals.

### Models, worked formulas, and attribution

The neural setup preserves shared first-layer columns, `1/sqrt(d)` input normalization, `1/n` readout normalization, and the block mobilities. Its order-one stored readout is explicitly different from the maintained small-readout law. The scalar kernel example uses half mean loss, and its physical clock is correctly halved relative to the default full mean loss. `K12` is the last-hidden feature kernel/readout block, not the full metric tangent kernel.

I checked the finite reuse projection formula, its `1/n` correction, and both terms in the physical matrix gradient. The identity specialization is `2+1/n` at finite width and `2` in the compiler. The saved pre-update derivative example gives `q+(c-eta*q)^2`, hence `15+(3-15*eta)^2` for the cubic derivative. The duplicate-call example retains two partials and yields the stated factor four; opposite contributions cancel for the zero difference. The scalar moving-flow example gives frozen second derivative 30, moving second derivative 120, and second jet 60.

For the two-layer derivative-energy example, centered independent readout removes the transpose response and yields `s1*s2`; the full metric norm adds `q1*s2+q2`. The cubic values 164025 and 305775 agree with Gaussian sixth/fourth moments. The symbolic geometry produces the stated Gram and retains all shared trainable columns, including singular and zero geometry.

I independently followed the linear kernel derivation. With `lambda_b=sum_c G_bc*y_c/m`, the first-velocity product contributes `5 lambda_a lambda_b`, using the trace moments of `(I+WW^T)^2`. Each second-velocity pairing contributes `4 lambda_a lambda_b`: the three surviving terms have coefficients 1, 1, and 2. Normalized centered-readout pairings vanish, and the residual-derivative term vanishes after replacing its scalar factor by its deterministic limit. All replacements are justified by the established higher moments. Therefore the second derivative coefficient is 18 and the factorial-normalized jet is `9 lambda_a lambda_b`, which is the displayed `9/4` formula when `m=2`.

The long quadratic kernel polynomial is a produced exact formula. Its support is the proved finite differentiation/source-evaluation algorithm, the inspected implementation of that algorithm, reproduction of the symbolic output, the compact-polynomial equality, generic-atom specialization, and independent exact finite AD. The two compiler paths do share their source evaluator, and the guide accurately discloses that. I did not treat their agreement as an independent probabilistic proof or perform a separate unrestricted finite-width Gaussian integration of the whole nonlinear second coefficient. There is no missing empirical-training reproduction: no empirical trajectory claim is made. The exact algorithmic theorem supplies the limit statement.

The supplied Golikov–Yang main text and Appendices H–J support the attribution of the moment mechanism. The candidate proves the specialized lemma internally rather than using the external master theorem as a premise. The source's broader universality claims are not silently imported. Neither the candidate nor the book introduction asserts a new general priority claim. The existing finite-second-moment-root and lower-regularity statements remain explicitly separate and are not narrowed by the stronger smooth-Gaussian theorem.

**Theory verdict: PASS.**

## Implementation and adversarial checks

I inspected every implementation line, test oracle, and producer line. The frontend validates vector types, program ownership, named parameter reuse, concrete rational PSD root covariance (including zero pivots), pure rank directions, and the supported optimizer coefficient syntax. It preserves normalization in both represented orientations and in reverse accumulation. State substitution is simultaneous and preserves frozen seed expressions. Frozen higher directions freeze every rank coefficient and factor; moving derivatives retain state dependence. Scalar gradients and scalar feedback differentiate physically.

The source compiler creates a distinct formal symbol per call, sets each input-Gram covariance before using the source, and applies every earlier opposite-source correction. Preactivation aliases are integration coordinates only; source partials act on the original expressions. Expectation atoms retain their covariance and prior-coefficient dependencies. The scalar expression module's Wick/Stein recursion decreases explicit Gaussian polynomial degree for flat activation products, while nested activations are deliberately retained as general integrals. A nonlinear deterministic scalar becomes a zero-dimensional integral, so final assembly retains its declared polynomial form. Numerical quadrature is not silently substituted.

The finite interpreter uses supplied stored matrix entries with no extra scaling. Means introduce `1/n`; exact integer/Fraction arrays stay rational; finite float arrays use ordinary floating arithmetic. Its behavior is independent of symbolic differentiation and Gaussian compilation. The package's parent NumPy import is correctly disclosed. The producer creates a fresh requested directory, recomputes its formulas, and records source/output hashes and environment; it reads no study result or historical output.

All candidate runs below used the standalone `edition/` as the working directory, `PYTHONPATH=code`, `PYTHONDONTWRITEBYTECODE=1`, and `python -B`. Python was 3.10.12 and NumPy 1.26.4. The imported compiler path was asserted to lie under this edition's `code/`. Environment details are in `reviewer_one/environment.json`.

1. **Supplied complete suite.** Command:
   `env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v`.
   Exit 0: **72 tests passed in 20.452 seconds**. Full log: `reviewer_one/mfp_tests.log`. I read the independent dense backpropagation, exact perturbation polynomial, and second-order convolution oracles; test names alone were not accepted as evidence. Covered attacks include current gradients versus history pullbacks, simultaneous updates, source feedback versus physical feedback, singular slots, exact covariance, fixed seeds through repeated vector/matrix updates, moving versus frozen jets, zero geometry, and all moving neural parameter blocks.

2. **Independent raw-entry Gaussian check.** Command:
   `env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 python -B ../reviewer_one/independent_checks.py`.
   Exit 0. My new oracle enumerates raw-entry Wick pairings for linear matrix words. Each matched pair identifies its actual row and column summation indices; the number of remaining components gives the exact power of `n` after normalization. It does not use the candidate source-response recurrence. It checked **522 programs**: every legal even-length walk through length six from one type on a three-type graph with a cycle and two parallel named edges, plus longer selected Wishart and cyclic reuses through length twelve. Every compiled limit equalled the independently counted leading coefficient, with no residual integral. Exact finite-width expectation polynomials are retained for every word in `reviewer_one/independent_results.json`.

3. **Independent nonlinear finite AD.** The same script builds a two-matrix reused-transpose program with nonlinear scalar-average feedback inside `phi(x)=1+x+x^4`. An independent dense expression and exact polynomial perturbations test each raw parameter coordinate at widths 1, 2, and 3. The checked raw partial counts are respectively 5, 13, and 25, including vectors, both matrices, and a scalar. All normalized vector gradients, raw matrix/scalar gradients, primal values, and the metric directional norm identity agree exactly as rational numbers. Additional singular duplicate-call cancellation and a shifted rank-one Gaussian root relation pass. This is deterministic algebra, not sampling.

4. **Guide examples.** `reviewer_one/run_guides.py` executes the text calculus example, text MLP example, identity kernel CLI, JSON calculus example, and cubic JSON MLP example with the correct standalone environment. All five commands exit 0; both JSON outputs parse. Every one of the guide's five complete Python snippets also executes under the independent-check script. The exact commands, working directory, environment, exits, and log hashes are in `reviewer_one/guide_commands.json`.

5. **Maintained producer.** Command:
   `env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir ../reviewer_one/kernel_recipe`.
   Exit 0; all generic, identity, and quadratic variants through order two were regenerated into the fresh assigned directory. Full formulas, complete JSON graphs, and the producer manifest are retained there. Every producer source hash was checked against the frozen candidate, and every recorded output hash against the generated file. Producer log: `reviewer_one/kernel_recipe.log`.

Two reviewer harness mistakes are retained rather than hidden. An initial ad hoc guide launcher omitted `PYTHONPATH=code`, so the first subprocess failed to import `pde`; `reviewer_one/guide_command_1.log` retains that failure. It was corrected by the persisted `run_guides.py` launched with the documented environment, after which all commands passed. An initial identifier-check regular expression included punctuation colons following two references; it falsely reported those references missing. `reviewer_one/check_packet.log` retains that failure. The corrected parser strips terminal punctuation and confirms the actual targets. Neither failure came from a candidate algorithm or documented command.

These finite checks supplement the rule-by-rule audit. They are not themselves proofs of uniform moments, a width theorem, or positive-time behavior.

**Code verdict: PASS. Examples/producer verdict: PASS.**

## Assembly, preservation, and limits of this verdict

`reviewer_one/check_packet.py` reverses the precise theory insertion and all three Chapter 2 replacements, and reconstructs the original chapter hash
`c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723`.
It then verifies the dependency excerpts against the original line ranges 1–251, 1035–1187, and 3335–3410. The finite Gaussian law excerpt matches lines 316–684 of `docs/12-three-sample-learning.qmd` with source hash
`6811e9e8c0557416920c9a1bd8a144807c4f3a9d4aaac134259130c81c7f148d`.
The differing filename/chapter number reflects the book's inserted chapter, not a missing dependency.

The candidate code mapping matches the packet mapping, and the destination set plus the explicit README/book/Quarto/bibliography changes is exactly the 15-file changed manifest. The inserted theory occurs exactly once. All 50 new labels are unique in the frozen edition; their native references and relative fragment/file targets resolve. The bibliography addition and both Quarto counter replacements match their supplied patches. The report of these checks is `reviewer_one/packet_correspondence.json`, with a successful log in `reviewer_one/check_packet_corrected.log`.

I did not render the whole book to HTML/PDF/LaTeX or perform the separate full integration/placement review. Those remain the workflow's distinct gates. I did not certify efficient arbitrary-order compilation, every possible floating intermediate, non-Gaussian roots for the new all-moment theorem, width-dependent small readout under its fixed-root hypothesis, growing programs, convergence of an infinite Taylor series, or positive-time trajectory reconstruction. These exclusions are already explicit in the candidate and are not required corrections.

No required correction or unresolved objection remains in this scientific scope. The frozen candidate is complete enough for the separate integration review and eventual user approval gate.
