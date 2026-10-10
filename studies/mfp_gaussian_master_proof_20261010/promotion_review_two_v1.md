# Complete independent scientific review TWO — candidate v1

**Verdict: PASS for the assigned scientific promotion candidate.** Theory,
implementation, and examples each pass. I found no required correction, no
unresolved correctness objection, and no missing scientific input needed for
these claims. This verdict does not replace the separate integration review,
whole-edition rendering checks, or final user approval.

Reviewer identity: `/root/promotion_review_two_v1`. Review date: 2026-10-10.
The exact neutral assignment is
`studies/mfp_gaussian_master_proof_20261010/promotion_review_assignment_v1.md`.
All run-relative paths below refer to
`/home/amir/Codes/PDE/data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v1/`.
My only outputs are this report and `reviewer_two/` under that run.

## Independence and input integrity

I started as a fresh isolated reviewer with the neutral assignment and required
process instructions, without author discussion or inherited research history.
I did not author, assemble, or select any candidate. My identity is distinct
from every author/assembler and the selector listed in the packet manifest.
I did not read the study README, author/internal/selection reports, another
reviewer's report, other studies, archived book material, or task history. I
did not contact another reviewer, delegate any part of the audit, or retrieve
additional scientific material. Git status was used only for metadata; no
contents of unrelated changed files were read. I made no Git changes or
maintained-source edits and did not run training experiments.

I checked every file digest in the 116-file candidate manifest, the 14-file
changed manifest, and the 17-file packet manifest at the beginning and end.
Every check matched. The three manifest file hashes themselves are identical
in the initial and final checks:

| Manifest | Initial and final SHA-256 |
| --- | --- |
| `candidate_manifest.json` | `6fe911cd2013d240f8015e182966452ca595dfe26b60d2d29214f9ebfc369aef` |
| `changed_manifest.json` | `285700c19e090a3a7557d27d7272b82fe1425c3973e908857b20cac609b52dff` |
| `review_packet/manifest.json` | `3cf5f0c941ffffe439da4d6adafc73117a99c136d65b017015a5796c91796f03` |

The complete records are `reviewer_two/initial_hashes.json`,
`reviewer_two/final_hashes.json`, `reviewer_two/read_coverage.json`, and
`reviewer_two/process_input_hashes.json`. The tables at the end of this report
retain all read-input hashes as well.

The assembly check removed the one exact 992-line insertion and reversed the
three scoped Chapter 2 replacements. The reconstructed original chapter has
SHA-256 `c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723`,
exactly the dependency-origin hash. All four dependency excerpts match their
declared complete line ranges and source hashes. The run's candidate mapping
equals the packet mapping. Thus there is no unlisted Chapter 2 alteration in
the candidate bytes I reviewed.

## Read coverage and its boundary

I read all lines of the neutral assignment, root `AGENTS.md`, the complete
257-line `RESEARCH_WORKFLOW.md`, the canonical-notation skill and its neural
reference, and `solve-math-rigorously`. I applied their notation, scope, and
proof-audit requirements. Truncated tool output was repaired by bounded
follow-up reads, including the singular-query proof and process instructions.

I read every line of the 992-line new theory, all four complete assigned
dependency excerpts and their origin metadata, the exact book and README
patches, bibliography addition, mapping and assembly script, both supplied
primary-source attribution texts, and provenance metadata. I also read every
line of all 18 `required_edition_reads`: the three implementation modules,
all four tests, all three scripts, the API guide, complete code README, package
initialization, rational Gaussian-moment module, book index and notation,
Quarto configuration and full bibliography. These 35 packet/edition files
contain 8,762 lines, itemized below.

In the assembled Chapter 2 I inspected the actual opening replacements,
insertion boundary, end boundary, and contained-specialization replacement:
lines 1–12, 240–255, 1241–1253, and 4324–4360. The inserted theory occupies
252–1243. Its bytes and the remainder's preservation were checked exactly.
The four dependency reads supply the relevant older mathematics, rather than
claiming that all of the 7,789-line assembled chapter was reread.

The unread scientific complement comprises the other book passages and
existing modules/tests not named in the assignment. Their manifest hashes
were checked, not their scientific arguments. `finite_network.py` was an
import dependency only; its contents were not audited as a new algorithm.
Other legacy README sections were read as required interface context, but
their referenced research and numerical campaigns were not opened or rerun.
No whole-book proof audit or integration/rendering verdict is claimed.

## Theory assessment

**Theory: PASS.** I reconstructed the language, all proof stages, and the
worked deductions rather than treating the successful tests as a theorem.

The program assumptions are sufficient and are kept separate from the older
foundation: fixed finite graph, equal width, named independent Gaussian
matrices between distinct types, jointly Gaussian iid coordinate roots within
a type, independence between types and matrices, constants independent of
width, and smooth maps with polynomial growth at every derivative order.
No arbitrary tensor-index contraction, inverse, coordinate selection,
width-dependent root law, or growing transcript is hidden in the primitives.
The stronger Gaussian-root/all-order smoothness conclusion does not replace
the supplied finite-second-moment/C1 theorem or the contained C2 specialization.

For arbitrary named edges, the adaptive conditional-product argument conditions
on the complete past before each query. The query input is then fixed, so only
the queried residual matrix factor acquires the new linear constraint. Parallel
edges and cycles of vector types do not break this induction; program chronology
remains acyclic. The projection error is finite rank divided by width. The
positive-Gram argument and independent query perturbations therefore extend
the supplied foundation without importing an unproved graph-wide independence
claim.

The source-response construction uses uncentered input second moments for
centered source covariances. Different oriented groups are independent as
sources, while their output fields retain response dependence. Formal source
partials retain paths through other matrices and hold previously computed
scalar expectations fixed. Separate coordinates are preserved on singular
Gaussian support. The covariance extension is a Gram extension, and the
regularization removal uses covariance square roots, not continuity of an
inverse or pseudoinverse. I checked the supplied conditioning and
integration-by-parts proofs and the root/derivative integrability needed there.

The uniform raw-entry estimate closes by instruction induction over all
finite moment and derivative orders. For a matrix call the derivative remainder
has at most the raw derivative order many earlier-node terms. For an even
moment of the remaining row or column sum, let a tuple contain b distinct
indices and s singleton indices among p factors. Centering removes each
singleton-independent term. One fundamental-theorem-of-calculus operation
per singleton supplies s additional matrix factors. Cauchy–Schwarz then gives
`C*n^(-(p+s)/2) <= C*n^(-b)`, because `p+s >= 2b`; the tuple count is
`O(n^b)`. The case s=0 is included. The strengthened induction over independent
entry variances at most `1/n` is essential and correctly covers zeroing and
shrinking entries. Differentiation before evaluation at the shrunken array
avoids either missing chain factors or division by zero. Repeated indices,
transpose reuse, nonzero root means, scalar feedback, and all finite p are
covered by the stated Hölder/Jensen arguments.

For clipping, every cutoff family has common polynomial derivative bounds
at each required order. Uniform moments therefore apply jointly in width and
cutoff radius. The proof upgrades an L2 input error to higher finite Lp errors
before multiplying it by a polynomial-growth factor. The correlated matrix
error uses the operator-norm fourth moment and the fourth empirical error
moment, so it never treats the error as independent of its matrix. Scalar
broadcasts and averages have the same finite induction. The evaluator's
covariance-square-root coupling and polynomial Gaussian dominator justify
passing source Grams, response derivatives, and fixed moments through cutoff
removal, including rank loss. The probability convergence and subsequent
uniform-integrability argument establish every finite scalar Lp limit.
The empirical W2 statement follows by the explicitly supplied coordinate
coupling and triangle inequality.

Finite differentiation is performed before the probabilistic theorem. I
checked the normalized vector adjoints, matrix gradient rows in both
orientations, repeated-parameter accumulation, rank lowering, and both
gradient contractions. A current ambient matrix gradient is formed before
substituting its represented state. Fixed simultaneous updates close in the
language; differentiating the updated expression instead yields the stated
history pullback. The moving-flow recurrence differentiates the field itself,
so its second derivative includes `DO[DV[V]]`. Smooth local finite-dimensional
existence suffices for a finite jet; no width-uniform interval or analyticity
is asserted. Frozen seed partials are explicitly distinguished from ordinary
derivatives of the diagonal primal expression, while source derivatives retain
their value dependence.

The initialization normal form has the required literal-node restriction.
The original forward preactivations are centered joint Gaussian coordinates
with recursively determined covariances; auxiliary linear integration aliases
need not be used as derivative coordinates. Arithmetic and source responses
preserve a polynomial times activation-derivative products. Singular Gaussian
Stein reduction removes an explicit polynomial Gaussian factor at every step,
terminates, and yields moments whose covariance inputs are already determined.
The result is not claimed for nonlinearities of updated or derivative fields.

I checked the exact finite reuse correction, normalized rank update, singular
duplicate-call formula and cancellation, moving-versus-frozen example, and
two-hidden-layer gradient norm. The order-one readout differs explicitly from
the maintained small-readout law. Shared first-layer columns preserve data
geometry during parameter and data differentiation. For the linear kernel
example I independently checked the conditional readout calculation: the
velocity-square contribution is 5, each mixed position/acceleration pairing
is 4, giving `K'' -> 18*lambda_a*lambda_b` and the factorial-normalized
`J2=(9/4)*(G11*y1+G12*y2)*(G12*y1+G22*y2)` at m=2. The half-mean loss and
its physical time factor are correctly declared. This observable is the
last-hidden-layer feature Gram/readout tangent block, not the full tangent
kernel or a positive-time trajectory.

Attribution is adequate for the claims actually made. The supplied Golikov–Yang
main text states the stronger non-Gaussian theorem and Appendix J develops
uniform raw-entry moment control with variance relaxation and singleton
cancellation. The candidate explicitly credits this mechanism and supplies
its own Gaussian proof. It does not invoke the external master theorem or
claim priority over it. The supplied appendix excerpt ends during J.4; this
does not leave a proof dependency missing, because attribution is its assigned
role and the candidate's needed moment argument is complete internally.

## Implementation and examples assessment

**Implementation: PASS.** I read the whole implementation and tests. Exact
rational constant arithmetic, decimal-string float conversion, singular exact
PSD validation, typed boundaries, normalized matrix factors, simultaneous
substitution, gradients, update helpers, and finite/moving jets agree with the
guide. The scalar reducer differentiates explicit named coordinates and retains
nonflat activation integrals as atoms, avoiding an invalid terminating-Stein
claim for nested nonlinearities. The Gaussian compiler keeps call slots
distinct, stores full oriented source covariance, and uses causal expectation
coefficients. Integration aliases are separate from formal source arguments.
The finite interpreter takes actual stored arrays and introduces no additional
hidden-matrix normalization.

The implementation's resource limits are appropriately practical rather than
theorem bounds. The source module uses the standard library; importing its
parent package also uses the existing NumPy API, as disclosed. No quadrature
or finite-width-expectation promise is implied by compilation. Unsupported
symbolic covariance inputs are not silently assigned neural geometry; explicit
shared-root factors provide the guide's symbolic geometry instead.

**Examples/producer: PASS.** All new guide commands and five Python snippets
ran in the standalone edition. The producer regenerated symbolic, identity,
and quadratic order-two kernels into a fresh reviewer-owned directory. Its
six output hashes match its manifest, and every emitted expectation integrand
and covariance uses only already-defined expectation symbols. The MLP and
calculus outputs reproduce the displayed formulas.

The long quadratic kernel polynomial is a produced formula supported by the
audited finite differentiation and source-rule algorithm, exact regression
against its compact expression, generic-atom specialization, and independent
dense rational moving-jet checks at widths two and three. As the guide states,
the two compilation paths share the same source rule; that agreement is not
an independent proof of the asymptotic polynomial. I do not count it twice.
The theorem and algorithmic correctness supply the general justification;
finite tests check their implementation. I found no inconsistency in the
coefficient, its label homogeneity, geometry, normalization or clock.

## Executed attacks and results

Commands ran with working directory `edition/`, `PYTHONPATH=code`, and
`python -B`; no live-checkout module or study output was on the import path.
The environment was Python 3.10.12, NumPy 1.26.4,
Linux 5.15.0-151-generic x86_64/glibc 2.35. Import locations were explicitly
checked to be under `edition/code/`, and bytecode writing was disabled.
Every command below exited 0.

| Command after `PYTHONPATH=code python -B` | Result and evidence |
| --- | --- |
| `-m unittest discover -s code/tests -p 'test_mfp_*.py' -v` | 67 tests passed in 20.970 seconds; `reviewer_two/unittest_mfp.log` |
| `code/scripts/example_mfp_calculus.py` | All eight examples reproduced; `reviewer_two/calculus_examples.log` |
| `code/scripts/example_mfp_mlp_derivative.py` | Three generic MLP formulas reproduced; `reviewer_two/mlp_examples.log` |
| `code/scripts/example_mfp_kernel_jets.py --activation identity` | Identity kernel jets reproduced; `reviewer_two/identity_example.log` |
| `code/scripts/example_mfp_kernel_jets.py --activation all --output-dir ../reviewer_two/kernel_outputs` | All three variants produced afresh; `reviewer_two/kernel_producer.log` and `reviewer_two/kernel_outputs/` |
| `../reviewer_two/independent_probes.py` | 33 independent/boundary checks passed in the completed extended run; `reviewer_two/independent_probes_extended.log` |
| `../reviewer_two/check_packet.py` | Input hashes, exact assembly, all five Python snippets, output hashes and expectation causality passed; `reviewer_two/check_packet.log` |

The first independent probe run had 28 passing checks and is retained as
`reviewer_two/independent_probes.log`. I then added the matrix-gradient and
zero-geometry affine checks, giving the completed 33-check run. No candidate
source or test was changed and no failing probe was suppressed.

The independent raw-entry Wick oracle does not use the compiler or its scalar
Gaussian reducer for its target. It pairs equal named matrix entries, unions
their typed indices, and counts free indices to produce exact powers of n.
It obtained:

- `E[||(A.T A)1||²/n] = 2+1/n`; the compiler returns 2.
- For `(A.T A)^2 1`, the exact norm expectation is
  `14+29/n+42/n²+20/n³`; the compiler returns 14.
- For `(A.T A)^3 1`, it is
  `132+562/n+1884/n²+3229/n³+3240/n⁴+1348/n⁵`; the compiler returns 132.
- For the cyclic typed route `A: a->b`, `B: b->c`, `C: c->a`, followed
  by reuse of A, the squared norm expectation is `1+2/n²`; the compiler
  returns 1. An opposite-orientation cyclic pairing gives exactly `1/n`
  and limit 0. Two separate parallel edges correctly give independent-name
  pairings and the expected zero or unit limits.

Other direct attacks checked causal polynomial scalar feedback; physical
differentiation through an average (second-derivative limit 4, finite n=1
value 48 at x=2); singular cubic reverse cancellation; a frozen cubic seed
retaining source-response value 24 but having zero physical gradient; three
exact ambient vector updates; moving coefficients `1,-6,60,-840` obtained
independently from `x(t)^2=x(0)^2/(1+2t*x(0)^2)`; shifted zero-variance roots;
and ambient differentiation on a degenerate initialization law.

Seven boundary rejections covered a zero covariance pivot with nonzero row,
nonfinite variance, arbitrarily small negative variance, a shifted declared
preactivation, random optimizer mobility, Boolean finite root values, and a
noncallable activation. A separate matrix update checked the current gradient
action `(4/5,28/5)` against the history pullback `(16/25,112/25)`, explicitly
detecting the extra update Jacobian.

Finally, for zero data geometry and `phi(z)=1+z`, an independent analytic
reduction gives first features equal to the constant-one vector e, upper
feature `H=1+W e` for the hidden matrix W, and
`E[H²]=2`. With `ybar=(y1+y2)/2`, the surviving initial equations are
`Hdot=ybar*w` and `wdot=ybar*H`. Centered-readout cancellation gives
the kernel coefficients `(2,0,3*ybar²)`. Specializing the generated generic
graph at this singular geometry agrees exactly. This specifically exercises
zero-covariance activation aliases, nonzero `phi(0)`, the half-mean clock,
and the moving readout contribution.

## Completion and limits

No required correction or missing input remains in the assigned scientific
scope. All proposed new mathematical and implementation lines were read,
the supplied complete dependencies were checked, relevant deterministic
commands completed, and final frozen-input hashes match their initial values.
The finite pairing oracle, finite-array tests, and boundary probes are evidence
for implementation correctness, not substitutes for the proof. High-order
resource feasibility, numerical quadrature, stochastic training behavior,
growing-depth/update limits, and positive-time reconstruction are outside the
candidate's claims and this PASS. Integration/rendering and user approval
remain separate gates.

## Exact read-input hashes

The following complete-file reads were verified against their frozen manifest
hashes both initially and finally. Paths are relative to the frozen run.
| Complete file | Lines read | SHA-256 |
| --- | ---: | --- |
| `review_packet/dependency_chapter2_finite_jets.qmd` | 1–153 | `c0b29d15cb9cb4d33ae9bcd87f1390b513bb412fb333816b6c7dbf687ec83f3c` |
| `review_packet/dependency_chapter2_finite_jets.qmd.origin.json` | 1–8 | `e8dfa3fea0469e9b9cf5c383ddd5aef7077b90509935603a23979fb60323d8a8` |
| `review_packet/dependency_chapter2_opening.qmd` | 1–251 | `e18642af7b5c488228b943a7249b259db2e3826c7ea93c230e0329e620e50cc7` |
| `review_packet/dependency_chapter2_opening.qmd.origin.json` | 1–8 | `372e01960795658c163355a25dbf0a95c199c6e680aac46256463385d2cc619c` |
| `review_packet/dependency_chapter2_specialization.qmd` | 1–76 | `35bee12f8ac530798eff41a39c0aecea8e2ccacfcaa963a52091dff176363f66` |
| `review_packet/dependency_chapter2_specialization.qmd.origin.json` | 1–8 | `d221abe407ac9c4458ab877710f0e2c97fd6231dad1069bbb6bc04c866aaec5f` |
| `review_packet/dependency_finite_gaussian_law.qmd` | 1–369 | `4710e129a6b13043b6c4ffabe37d26ee3bdd7645babe7f01e11f75174c1e72a3` |
| `review_packet/dependency_finite_gaussian_law.qmd.origin.json` | 1–8 | `c3b96e0dea3322ea0b9ab8e16d8ab6c04e57ea2eb83eb0cd867a60362b16868b` |
| `review_packet/promotion_assemble.py` | 1–92 | `1d79c2791539e2093211b2e45a0320424ce0306732f5f5924ff7a610bcc64fa0` |
| `review_packet/promotion_bibliography.bib` | 1–8 | `560c91f80d729c0e27157150a518ab33157e834b94554060e056f53e804e3881` |
| `review_packet/promotion_book_patches.json` | 1–14 | `2ea8e49f5697195dc9036e44db692930e25e8fb49d454f4151e86cb45053fe4a` |
| `review_packet/promotion_code_mapping.json` | 1–13 | `08fd2e44978ca836ce9e70970912ea9e24fc1d9ffa510d5a5d0db12a3125ba9c` |
| `review_packet/promotion_code_readme_patches.json` | 1–10 | `af0af04b3252c269517f01ea82d887869651b49826341da098cb9cba643d008f` |
| `review_packet/promotion_theory.qmd` | 1–992 | `793e65c40302c1d48a36054897c1d2b22a58b71eccc5d777eec930e19ba8882f` |
| `review_packet/provenance_appendices_H_I_J.txt` | 1–914 | `ef63f1ff6febfc7b398fc399987dc0a2050652ef6c6c460b501cf635950a7832` |
| `review_packet/provenance_non_gaussian_tp_main.txt` | 1–786 | `b7bd14f1255015d5feedd8ecb1bee9b4928e96d94b679aa5f69d5afa19d3e0bc` |
| `review_packet/provenance_sources.json` | 1–16 | `7f220bdd8af61068c948f8f01ee361bf9b33818178cee9ab9af15624a6a9e004` |
| `edition/code/MFP_CALCULUS.md` | 1–403 | `f90dd09c50eeed0b4ad4785586080b8f45674591568bf9e409db6f710b4a58ce` |
| `edition/code/README.md` | 1–1266 | `5302e48be28bf0cba8c6ccc10d0a6a61eca9b00dc5f09b792466e236f3344146` |
| `edition/code/pde/__init__.py` | 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `edition/code/pde/gaussian_moments.py` | 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `edition/code/pde/mfp_compiler.py` | 1–785 | `ca48becf732dea0254d43aa49163829696b5c28d2f6d7503c7b53ee72a77d0a2` |
| `edition/code/pde/mfp_expr.py` | 1–426 | `1340df2e1cd7279d568aa07610bfba033eaf95d8fc75426d8149b2b4d9cbcfa8` |
| `edition/code/pde/mfp_finite.py` | 1–140 | `84060153c467172eaabaed073ece4e8fd0d77fbc1ed2fee3e8a66542d2c7c037` |
| `edition/code/scripts/example_mfp_calculus.py` | 1–103 | `20b727df8e386907f1ae17de427b3f41ff86b4f29f33a0cea9711bbc7a679d07` |
| `edition/code/scripts/example_mfp_kernel_jets.py` | 1–112 | `3298421fad2776bf306b0928611517b938529429de7606efd53ecf1caaa2d03c` |
| `edition/code/scripts/example_mfp_mlp_derivative.py` | 1–69 | `9c7fefb3ac2dcc50c90f1bef45cf64bf4f7f37d0c0b1b5e26c8c30a4478d4527` |
| `edition/code/tests/test_mfp_compiler.py` | 1–534 | `aa30da703732d44aefa5c1b082307d3d52c5e7b62700e62900e3619214fcd1d8` |
| `edition/code/tests/test_mfp_expr.py` | 1–189 | `06dac966c1b74ba8dfe9ebfb9a2dde1abccc175102aef435cf8ba110c1824d65` |
| `edition/code/tests/test_mfp_kernel_jets.py` | 1–304 | `a2fd1f7f64bfdf7dde921991f15f84992d30859f662dd71cd33e0996e156e3ce` |
| `edition/code/tests/test_mfp_mlp_example.py` | 1–65 | `e3dfffb2e8bb28b128903d92df84567225b81e7957f04d166dfc755972d15ad5` |
| `edition/docs/_quarto.yml` | 1–68 | `e8312b9a53ebe0dbff35b93c55f8f8f5f49bd8c3bf633bd44c8bdd2b086f55e7` |
| `edition/docs/index.qmd` | 1–260 | `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68` |
| `edition/docs/notation.qmd` | 1–98 | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `edition/docs/references.bib` | 1–74 | `58b93ea048f23043234eb2e6f05c151a6f0b78be006c115b37ef3ed2a5e491d0` |

The process instructions and neutral assignment were also read in full; their
completion-time hashes are:

| Process input | Lines read | SHA-256 |
| --- | ---: | --- |
| `/home/amir/Codes/PDE/AGENTS.md` | 1–99 | `d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97` |
| `/home/amir/Codes/PDE/RESEARCH_WORKFLOW.md` | 1–257 | `459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1` |
| `/home/amir/Codes/PDE/studies/mfp_gaussian_master_proof_20261010/promotion_review_assignment_v1.md` | 1–84 | `09cf1c1595b79796093169f37023f87559336323de1d4f082e5d3893cebc2c99` |
| `/home/amir/Codes/personal-skills/explain-with-canonical-notation/SKILL.md` | 1–144 | `daac37e41dca5e618c5baf2a65689000e526930f059b822ebec61aafbfd1abfc` |
| `/home/amir/Codes/personal-skills/explain-with-canonical-notation/references/neural-response-memory.md` | 1–151 | `c2d570aac8950b5766513d81dd2dada4a9babeba92bbb554f1042107207a52b1` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | 1–115 | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
