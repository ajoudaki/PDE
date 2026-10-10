# Independent relevance and placement selection

Date: 2026-10-10. Selector: `/root/promotion_selector`, a fresh scoped agent.
This is the Part 2, stage 1 selection, not a correctness verdict or permission
to integrate. I did not author or assemble the study result or a promotion
candidate. I must not serve as either scientific reviewer or integration
reviewer for this package.

## Decision

**Accept a bounded promotion for assembly, merging overlapping material into
Part I, Chapter 2, “Mean-Field Peeling: A Gaussian Calculus for Deep Networks.”**
Keep the existing three parts and all chapter titles/order. Add no chapter or
part. The appropriate destination is `docs/02-gaussian-reuse.qmd`, immediately
after “4. Exact polynomial Gaussian expectations”
(`sec-docs-gaussian-calculus-l203`) and before “7. Reusable finite calculus and
forest factorization” (`sec-docs-gaussian-calculus-l1824`). Use one new major
section, “Fixed finite Gaussian derivative programs,” with descriptive native
Quarto identifiers, for example `sec-mfp-finite-derivative-programs`.

The distinct contribution is a precise finite typed language that admits
smooth polynomial-growth coordinate functions, normalized contractions,
causal scalar feedback, exact derivative expansion, represented matrix
updates, and finite physical-flow jets. Its scalar outputs have limits in
every finite $L^p$, evaluated by an explicit Gaussian expectation graph.
The uniform-moment argument makes the expectation conclusion substantive;
it is not merely a symbolic formula or a convergence-in-probability statement.
The compiler makes this calculus usable for new admitted observables without
manual Gaussian-response bookkeeping.

The current chapter's opening says it has no general observable-grammar
theorem. The selected result changes that statement for its declared finite
language. It does not supply unrestricted parameter-tensor contractions,
growing depth or update count, positive-time reconstruction, or a trajectory
limit. Those boundaries remain necessary. This is directly relevant to the
book's population-dynamics tools even though it does not solve the trajectory
problem. No priority claim about Gaussian-program limit theory is needed.

## Component decisions

| Component | Decision and distinct value | Overlap, maintenance cost, and useful scope |
| --- | --- | --- |
| `master_proof.md`, Sections 1–3 and 5–6: language, moments, clipping, and scalar $L^p$ identification | **Accept** for assembly in the new Chapter 2 section. State the complete finite language and full uniform-moment/clipping argument. | Existing finite specializations do not supply this complete smooth polynomial-growth scalar-feedback contract. Maintain one theorem and one moment proof. Require Gaussian roots, fixed graph/data/coefficients/order, and every activation derivative of polynomial growth exactly as stated. |
| `master_proof.md`, Section 4: bounded-derivative Gaussian law | **Merge** with the established dependency in Chapter 13, III.F.1–III.F.6; do not paste its full proof again into Chapter 2. | The source rule, adaptive conditioning, singular-query removal, operator estimate, and scalar-feedback mechanism already exist. A short explicit extension argument must match the new language to the old statement, including arbitrary named typed matrix edges. Preserve the old theorem's broader finite-second-moment root and lower-regularity cases. |
| `master_proof.md`, Section 7, and `calculus_rulebook.md`: physical differentiation, ambient gradients, lowering, steps, and jets | **Merge** into the new section's operational subsections. | Chapter 2 already has moving-direction identities and full finite MLP jet recurrences. Keep those useful concrete algorithms. Add the general typed AD rules, normalized adjoints, represented updates, and compilation closure proof once; refer to existing recurrences for their network specialization. Retain the distinction between a current ambient gradient and a history pullback. |
| `master_proof.md`, Section 8: activation-moment normal form | **Accept** as a separate proposition/subsection following derivative compilation. | This gives a finite symbolic output form beyond rational polynomial moments. Its syntactic restriction to literal original initialization preactivations is essential. Do not promote it as a normal form for arbitrary nested activations or trained fields. |
| `worked_examples.md`, Example 1: reused transpose | **Merge** into the existing opening example and the new compiler example. | The existing opening already contains the exact Gaussian projection and limiting response. Add the squared observable, finite-width correction, and accumulated physical gradient where useful; do not repeat the full projection proof. The finite correction sharply explains what `compile` returns. |
| `worked_examples.md`, Examples 2–3: represented update and singular duplicate calls | **Accept**, compactly, in the new section's worked-program subsection. | These are instructive edge cases for matrix identity, $1/n$ normalization, named source derivatives, and singular laws. Their derivations are short and exercise real API failure modes. The loss in Example 2 must remain explicitly its stated scalar loss. |
| `worked_examples.md`, Example 4: moving versus frozen direction | **Merge** with the existing “3. Derivatives along the gradient direction” subsection, or give one short worked case in the new operational subsection with a backward reference. | The general distinction is already proved. The exact values 30 versus 120, and derivative versus factorial-normalized coefficient, add useful executable checks. Preserve the scalar-state example's own meaning of its state variable. |
| `compiler_usage.md` and reusable compiler | **Accept**, as an explicitly imported maintained module and a dedicated API guide. | It supplies typed symbolic physical AD plus Gaussian expectation graphs; neither `finite_jets` nor the numerical `observable_compiler` does this job. The guide must state exact rational/float-conversion semantics, frozen seed semantics, supported language, no quadrature, and potentially rapid expression growth. Avoid adding generic names to the package's top-level namespace. |
| `mlp_derivative_example.md` | **Accept** as one short neural example in Chapter 2 and an executable example in the code guide/scripts. | The example connects parameter derivatives to a nonzero scalar and explicit Gaussian moments. It is useful despite the reuse response vanishing for the stated centered readout. Preserve its order-one stored readout and $n$-scaled vector gradient; it is not the default small-readout model. |
| `symbolic_kernel_jets.md` and executable construction | **Narrow** the book presentation to the exact two-sample/two-layer setup, shared first-layer parameters, physical clock, requested three coefficients, and a compact inspectable result. Accept the full generic graph as reproducible code output. | The generic 132-expectation output is too large for the chapter and is not a separate foundation. The compact quadratic polynomial can appear as a worked result if the frozen candidate contains its complete producer and independent checks. Use $G_{ab}=x_a^\top x_b/d$ or an explicit local correspondence to the book's input Gram; distinguish the last-layer feature kernel from the full tangent kernel. Keep the half-mean-loss clock explicit. |
| Retained generated formula dumps, study manifests, and historical check reports | **Decline** as maintained theory/runtime dependencies. | Their appropriate role is study evidence. Reproduction must start from maintained code and explicit inputs. No exact coefficient or required recipe may depend solely on a retained generated file. A maintained script may generate text/JSON into a fresh requested directory. |
| Claims about generic positive-time dynamics, unrestricted contractions, arbitrary root laws, small-readout width-dependent laws, or efficient complexity | **Decline** as extensions of this package. | The selected theorem does not establish them. Do not launch new research to broaden the promotion. These exclusions do not block assembly of the stated result. |

No selected component is held for a relevance gap. Correctness, implementation,
and integration remain subject to the later complete review gates; acceptance
here is permission to assemble the bounded candidate, not evidence that it
passes those gates.

## Exact organization of the proposed addition

Within the new Chapter 2 section, use the following progression. These are
placement responsibilities, not drafted candidate text.

1. **Typed finite language and theorem.** Define types, independent matrices and
   roots, admissible coordinate/scalar instructions, normalized averages,
   represented rank sums, scalar outputs, and fixed quantities. State scalar
   $L^p$ convergence and uniform moments precisely. Give any vector-law claim
   its actual empirical-law mode rather than treating neuron values as constants.
2. **Source-response evaluation and named derivatives.** Give the construction
   needed to use the theorem, including uncentered input Grams, oriented source
   groups, distinct named slots at singular covariance, and frozen deterministic
   coefficients. This is a definition/use contract; point to existing proofs of
   the bounded-derivative law instead of duplicating them.
3. **Uniform moments and removal of clipping.** Give the new complete argument,
   including raw-entry derivatives, zero singleton cases, all moments needed
   for interpolation, scalar feedback, and correlated matrix/error products.
   The passage from probability convergence to expectation convergence belongs
   here, with its hypothesis stated.
4. **Exact finite differentiation and training instructions.** Consolidate the
   rulebook tables, ambient-gradient convention, rank-one lowering, finite GD,
   fixed and moving directions, and finite-order jets with the compilation
   proof. Use the existing finite MLP recurrence as a concrete cross-reference,
   without changing its finite-state regularity or numeric order contract.
5. **Initialization activation-moment form.** State and prove the restricted
   reduction. Refer to the existing polynomial Gaussian moment recurrence for
   the polynomial-only special case. Distinguish arbitrary fixed coefficients
   from the compiler's concrete covariance front end.
6. **Worked programs and the symbolic implementation.** Integrate the selected
   examples proportionately, ending with a short API entry point and a link to
   `code/MFP_CALCULUS.md`. Long API tables and generated formulas belong in the
   guide or regenerated output, rather than duplicating them in the book.

The existing later material retains its present scientific responsibilities:
finite numerical jets and forests, finite contraction heads, loss-GD pullbacks,
the fixed feature-ascent program theorem, contained continuity results, trained
memory, and adaptive comparison. Do not renumber or move those sections merely
to give the new theorem a numerical section label. New native IDs should be
descriptive; preserve all existing anchors.

### The existing foundation is not superseded

Chapter 13 III.F.1–III.F.6 (`docs/12-three-sample-learning.qmd`, current lines
316–684) already proves the bounded-derivative law and singular source rule.
Its iid roots only need finite second moments; its coordinate maps need $C^1$
bounded derivatives; its causal scalar operations allow locally Lipschitz
operations near deterministic limits, with their stated domain conditions.
The proposed Gaussian/$C^\infty$/polynomial language is stronger in some
outputs and narrower in these inputs. Replacing the old theorem by the new
statement would lose established scope.

Leave that foundation and its identifiers in place in this promotion. The new
chapter section can depend on it with full precise cross-references. This is
the smallest change and respects the user’s organizational constraint. A
future relocation of common foundational material would need its own complete
reference/dependency audit; it is not necessary for this addition.

One mismatch needs explicit treatment during assembly: III.F presents adjacent
layer matrices, while the proposed language permits any finite list of named
matrices between distinct types. Explain why the adaptive conditioning and
finite induction continue to hold with that list, tracking matrix identity and
type compatibility. Also show how clipped normalized averages and scalar
dependence fit the bounded-derivative/scalar-feedback construction. Do not
silently broaden the older theorem's statement by citation.

The existing Chapter 2 feature-ascent theorem is not redundant either: it has
a $C^2$ activation class, a particular exact chronology, strict-rank conclusions,
and an explicit coupling. The new finite smooth language does not replace all
of those conclusions. Likewise, contained specializations A.1–A.4 retain
non-Gaussian roots, lower regularity, and strong chain-rule roles.

## Stale scope and navigation changes

- Revise the Chapter 2 opening route paragraph (current line 5) to insert the
  typed-program theorem before the existing finite specializations. Revise
  the paragraph at line 7 so it states the new precise finite-language reach
  and retains the exclusions for infinite Taylor series and trajectories.
  Do not leave a blanket denial of an observable-grammar theorem above one.
- Keep the specialized statement in A.2 (current line 3359) local: that
  specialization itself is not an all-moment theorem for arbitrary feedback.
  Add a pointer to the new smooth Gaussian theorem and its different
  assumptions. Do not delete the qualifier as though C2/subGaussian inputs now
  inherit the new all-moment proof.
- Update the opening of `code/README.md`, which currently describes its
  narrower modules as not a general symbolic population compiler. Distinguish
  those finite numerical tools from the newly added finite typed symbolic
  compiler; retain the statement that tests do not prove a width limit.
- Add a short README section beside the current exact Gaussian moments and
  moving-jets material, linking the dedicated guide. Do not append the entire
  guide to the already long README.
- No `_quarto.yml` change is needed. The existing Chapter 2 title in
  `docs/index.qmd` already fits. Its warning that fixed Gaussian programs do
  not control a growing number of updates remains correct. No global notation
  change is necessary if local compiler types and source symbols are defined.
- Update only relevant cross-references. The source evaluator's laws and the
  finite/interacting/moving distinctions should have one canonical explanation
  each, with examples linking to it.

## Proposed maintained code destinations

| Source responsibility | Destination |
| --- | --- |
| Typed graph builder, physical AD, represented matrices, source compiler and returned DAG | `code/pde/mfp_compiler.py`; explicit import `from pde.mfp_compiler import Program, ProgramError` |
| Symbolic expression algebra, source partials, Wick/Stein reduction | `code/pde/mfp_expr.py`; supporting expression API, without top-level exports |
| Independent supplied-array primitive interpreter | `code/pde/mfp_finite.py`; explicit `evaluate_finite` import |
| Contract and executable API examples | `code/MFP_CALCULUS.md`, with a compact link/overview in `code/README.md` |
| Reuse, singularity, update and moving-direction executable cases | `code/scripts/example_mfp_calculus.py` |
| MLP parameter-derivative example | `code/scripts/example_mfp_mlp_derivative.py` |
| Symbolic two-sample feature-kernel jets | `code/scripts/example_mfp_kernel_jets.py` |
| Deterministic compiler/AD/interpreter/expression and example checks | `code/tests/test_mfp_*.py` and `code/tests/test_mfp_kernel_jets.py`, preserving independent oracles rather than importing old outputs |

Use relative package imports within the three library modules. Scripts must
work with `PYTHONPATH=code` from the standalone edition. No import should add
the study directory to `sys.path`. Example builders may remain importable in
their example scripts for tests; they should not become generic model APIs
solely because an example needs them. A separate manifest-producing runner is
optional; promote it only if it remains necessary to regenerate an accepted
explicit output, uses current maintained source paths, and writes to a fresh
user-selected directory. Do not carry over study output defaults.

Keep `pde.finite_jets` and `pde.observable_compiler` unchanged. The former
evaluates supplied finite states; the latter injects numerical arithmetic and
Gaussian integration nodes into a specific initialized-dictionary workflow.
They share Gaussian ideas with this work, but their interfaces and numerical
contracts are different. The generic `GaussianCompiler` name should therefore
remain module-qualified.

The existing `gaussian_moment` already implements exact rational monomial
moments and PSD validation. The new symbolic reducer additionally handles
symbolic covariance coefficients and activation-moment atoms, so it cannot be
replaced by that numeric-only API. Avoid an unrelated refactor of the old API.
For duplicated small PSD/Wick logic, either reuse a narrow internal helper
without changing old behavior or retain the specialized implementation with
cross-checks against the established rational API. Document the new frontend's
finite-float-to-decimal-rational convention; do not silently impose it on the
existing `gaussian_moment`, which rejects floats.

## Required candidate checks and remaining gaps

This selection does not certify the proof, library, or long quadratic formula.
The next stage must freeze their complete contents and all required established
dependencies for the two fresh adversarial reviews. Neither an internal status
notice in a source nor a prior test report supplies that gate.

In particular, the candidate needs a complete proof of its typed-graph scope,
accurate frozen-seed semantics, normalized gradient/update factors, singular
slot handling, and restricted normal form. The code checks should exercise
shared matrices, scalar feedback, negative/zero/singular covariance cases,
current gradients versus history pullbacks, moving versus fixed directions,
finite interpreter versus independent dense/rational calculations, and generic
versus polynomial compilation for the worked nonlinear jets. These are review
targets, not claims that such tests were run by this selector.

The long nonlinear second-jet formula is not independently derived in the
scientific source's own description. If it is retained as a concrete book
result, its full producer and independent mathematical/finite-array checks
must be visible in the frozen package and audited by both reviewers. Generated
text alone is insufficient. If that component cannot pass, exclude the long
coefficient claim while retaining the separately complete theorem/API/examples;
do not broaden the research program to rescue it.

Run the selected deterministic tests and all guide commands in a standalone
edition, with no studies or retained outputs. Render the complete existing
Quarto project to HTML/PDF and export editable LaTeX. Verify native IDs and
links, the unchanged part/chapter list, no duplicate theorem foundation, and
scope statements at the old and new interfaces. A fresh independent integration
review and approval of the concrete reviewed package remain required by the
workflow.

## Actual read scope and independence

I read `AGENTS.md`, all of `RESEARCH_WORKFLOW.md`, the full canonical-notation
skill and its neural-response-memory reference. Scientific scope was the
supervisor's neutral assignment; I did not read the study README, other
studies, `old_docs/`, Git history, chats, or check reports. The supplied study
sources contain embedded status notices and links to historical checks; I
encountered those notices but neither opened those reports nor used their
verdicts. This selection uses scientific content and coverage only.

Complete study prose reads: `master_proof.md`, `calculus_rulebook.md`,
`worked_examples.md`, `compiler_usage.md`, `mlp_derivative_example.md`, and
`symbolic_kernel_jets.md`. An initially truncated combined tool output was
repaired by separate reads. Complete maintained reads: `docs/index.qmd`,
`docs/notation.qmd`, `docs/_quarto.yml`, `code/README.md`,
`code/pde/__init__.py`, and `code/pde/gaussian_moments.py`.

Selected complete maintained sections read in Chapter 2: opening and sections
1–4 (lines 1–251); “Numerical interface and claim boundary” and “Decorated
forests” (538–662); “E. Reusable finite depth jets and observable heads”
(1035–1187); the fixed-program introduction and 5.1 theorem (1794–1909);
and contained specializations A.1–A.4 (3335–3410). Chapter 13 III.F.1–III.F.6
was read completely (316–684), with only the opening of III.F.7 seen in the
same read. Headings/search matches were inspected across Chapters 2 and 13
to map placement and scope. The remainder of both long chapters was not read
as a proof audit; no whole-book correctness claim is made.

Implementation inspection: complete `mfp_finite.py`; `mfp_compiler.py` lines
1–180, 205–254, and 590–785; `mfp_expr.py` lines 340–426; import and
definition metadata for those files and the directly described example/runner
sources; `code/pde/observable_compiler.py` lines 1–100; filename metadata for
maintained modules, scripts, and tests. I did not execute code or inspect test
bodies. These limited implementation reads suffice to select API placement,
not to certify implementation behavior. Missing proof/code validation is
assigned to later gates, rather than inferred from documentation.

Repository HEAD at selection: `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`.
The shared index was empty. Existing unrelated working changes were preserved.
Only this report was written; no established file or Git index was changed.

### Source fingerprints

SHA-256 of whole files, including files with only the partial read scope above:

```text
d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97 AGENTS.md
459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1 RESEARCH_WORKFLOW.md
8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68 docs/index.qmd
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023 docs/notation.qmd
e8312b9a53ebe0dbff35b93c55f8f8f5f49bd8c3bf633bd44c8bdd2b086f55e7 docs/_quarto.yml
c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723 docs/02-gaussian-reuse.qmd
6811e9e8c0557416920c9a1bd8a144807c4f3a9d4aaac134259130c81c7f148d docs/12-three-sample-learning.qmd
b038f6033e8e387c602b0e7947ab08a793fb825f179d5afa161d6c12d4495807 code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3 code/pde/__init__.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae code/pde/gaussian_moments.py
1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac code/pde/observable_compiler.py
55d979e9dbab1c13bc1f84a43b001efe9fefa6bd1b565d4479245ef5128a3388 master_proof.md
9c934578b25dd77079f1b2896829cce471ca1cf85abd7a53ae6445036f7e25d3 calculus_rulebook.md
cbcff373fdcdde122caaa8f6c8d4847f8afe87bfe2c8b730da7d8ae255374451 worked_examples.md
f8c7c6acc5931aeabb5efda7ebc9f24e4108c2c4aaeb7c05b48048d7403334ff compiler_usage.md
35f7ef91723a96df425144236b5ea8b0601d0741affefb7b7aa621fae335622b mlp_derivative_example.md
a63abf9b11d573ab251d6777621ae3aabff4e13f1ac416564d7efbf43fe59d31 symbolic_kernel_jets.md
f6d0b2f786e9a0b676476487dff3e3c393c8fd7145261661d8b45737cae215ce mfp_compiler.py
82bce3fe5f8180aa89c009fa117c1fdb6563bbb0247d20e60296fbe199f070de mfp_expr.py
7e39ff0fd2026c6fd7fd6f3f2e6f6f2a82025a72fd83b533c38d7b4be03ed6d8 mfp_finite.py
```

The unqualified filenames in this fingerprint block are in
`studies/mfp_gaussian_master_proof_20261010/`.
