# Independent relevance and placement review: revised C-H3

Selector: `/root/h3v2_relevance`, 2026-09-13. Role: Part 2 step 1 selector,
not an author, assembler, scientific acceptance reviewer, or integration reviewer.

**Recommendation: accept for assembly at the exact scope below.** The proposal
addresses a stated, substantial gap between the maintained exact population
closure and finite computation. Assemble it as a new C.4.7.10 adjacent to H1/H2,
with `pde.observable_solver` as its normal library entry point and its six
focused implementation modules. This is a relevance decision, not a declaration
that the theorem has passed independent scientific review, the implementation
is validated, C-H3 is complete, or promotion is approved.

## Selected scientific addition

The selected target is the bias-free two-hidden-layer tanh model, prescribed
stored Gaussian variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, residual `f-y`,
unhalved mean squared loss, physical time, and horizon `[0,1/200]`. The
operational family consists of the five exactly represented rational two-arc
parameters in the candidate, including its degenerate atomic cases. Its
cross-arc normalized correlations lie in `[2/5,4/5]`; nondegenerate intervals
produce nonatomic laws. Neither family nor horizon shrinks with refinement.

The addition comprises the compatible dense polynomial-plus-word closure,
finite joint Gaussian initialization, explicit input/population quadrature,
finite arithmetic, complete nonlinear time stepping, whole-circle prediction
map, training-law-averaged initial/current hidden pair laws and RMS displacement
at both layers, and own-state restart. The observation claim is precisely
the declared pair-law/RMS contract. A general numerical API for every C-H1
word is not supplied by these six files and should not be advertised implicitly.

Its convergence order is explicit: arithmetic precision first, then time
step, input quadrature, population quadrature, initializer quadrature, generic
source regularization, and finally closure order. The source-regularization
limit is unused on the fast core. The integer/rational backend supplies the
unbounded precision algorithm; fixed float64 and the practical Decimal option
are not the mathematical precision-to-infinity claim. This scope has value
without a convergence rate or a computable resolution chosen from a tolerance.

## Comparison with maintained coverage

| Maintained input | Already supplied | Distinct proposed value |
| --- | --- | --- |
| C.4.7.8 | A sufficient current-state hierarchy, exact finite Gaussian source rules, finite upward weak identities, and reached restart; finite levels retain unevaluated law fields. | The new solver implements finite numerical populations and a fixed current-state update. It does not merely repackage the H1 information theorem. |
| C.4.7.9 | An autonomous exact population closure with an exhaustive initialized dictionary, ridge filters, both action directions, convergence on an existential small law ball, and own-state restart. | A justified compatible dictionary and ridge, an explicit represented law domain, and a numerical refinement theorem at each fixed order replace its unevaluated integrals by finite operations. |
| `code/README.md`, observable-closure section | A minimal float64 tensor-Gaussian quadrature prototype, finite atomic input API, RHS/observations and one algebraic update. It expressly supplies no trajectory solver or numerical-consistency theorem. | Heun evolution, rational arcs, streamed population/input contractions, a generic joint-source compiler with a removable covariance regularizer, precision refinement, and exact working-value checkpoints. |
| `docs/README.md`, C-H3 roadmap | These are explicitly stated outstanding obligations, with feasible finite-resolution runs separated from proof and error certification. | The candidate theorem and implementation address those obligations directly; operational feasibility still needs separately supplied execution evidence. |

The new short-time scope proposition is an essential additional theorem.
The represented nonorthogonal family is not shown to lie in H2's older
existential neighborhood, and that membership is not a permissible assumption.
Instead, the candidate constructs the short-time flow and extends H2's outer
comparison using explicit source bounds. Assemble this proposition and its
necessary proof as a visible dependency. Do not write the numerical theorem
as if the larger domain were already established by C.4.7.9.

The broader all-Borel-law and finite-network clauses of that proposition have
their own proof burden. They can remain as a clearly separated prerequisite
proposition/corollary within the addition; they do not turn the rational
`ArcLaw` interface into a general executable Borel-law integration service.

## Non-vacuity and assumptions

The supplied construction does not select coefficients from a learned target
trajectory. Feature syntax, degree, ridge, Gaussian cubature, source covariance
regularization, input rule and initial coefficient contractions are specified
before evolution. The target-dependent compact-set approximation errors occur
only in the convergence proof, not in initialization, order selection, or RHS.
The literal word tail eventually exhausts the initialized observable algebra;
the four/two-dimensional fast Gaussian core alone is not assumed dense in the
full action-generated space.

The revised hierarchy proof correctly distinguishes raw-span growth from
relevant action information. Degrees 1, 3 and 5 have retained counts
`(5,3)`, `(35,10)` and `(128,21)`. The last count includes two redundant lower
constant words. Its contained orthogonal-polynomial argument exhibits a new
upper direction orthogonal to the preceding upper polynomial span but with
strictly positive pairing against `A0 tanh(g1)`. Actual adjunction preserves
that pairing in the reverse direction. This gives a substantive reason to use
those degrees for operational comparisons. It proves neither monotone error
reduction nor a measured accuracy gain.

The state retains complete within-population joint marks and moving values.
The initialized reverse response and its surviving Gaussian randomness are
present. At runtime both orientations use one coefficient matrix and its
transpose. There is no neural width parameter, raw trainable neuron matrix,
arbitrary-vector Gaussian-action service, or growing history coordinate.
Saving the two current populations, fixed marks, `M`, `D`, input rule and
arithmetic metadata determines the next numerical step. The proof separates
this working-state restart from population restart and from starting a new
finite mesh at an interpolated interior time.

No vacuous, oracle, or evidently invalid premise was identified by this
relevance reading. That is not a complete proof verdict. In particular the
new source cap/common-carrier completion, finite-network identification,
singular covariance passage, fixed-order stability, rational primitive bounds,
and composition of numerical limits require the subsequent two complete
adversarial reviews. I did not replace any of these obligations by an author's
status label or a reported check.

The new domain proposition expressly does not establish a uniform positive
hidden-motion or nonaffinity margin for every law in that domain. The selected
solver preserves the full nonlinear equations and computes the declared
paired observables. It should not inherit the older H1 activity conclusion
on this different family without a separate argument. No additional activity
margin, practical accuracy, time-40 statement, arbitrary diagonal limit,
raw-GD theorem, or tolerance-to-cost result is selected here.

## Maintenance cost and smallest destination

The implementation is substantial but focused: six sources separate exact
word syntax, rational fixed-point arithmetic, Gaussian numerical primitives,
the generic source compiler, feature initialization, and nonlinear evolution.
Python/NumPy suffices for the core library. Its source-language, covariance,
arithmetic, and checkpoint contracts must remain documented and tested together.
Three arithmetic options add maintenance cost; their distinct promises should
remain explicit rather than duplicating an undifferentiated accuracy claim.

For population sizes `P1,P2` and feature lengths `d1,d2`, the retained arrays
contain `P1(d1+5)+P2(d2+2)+2d1d2` scalars, before input arrays and metadata.
The proof also counts input blocks, optional pair arrays, initializer/source
tables, syntax caches and rational scalar bits. The coefficient-first matrix
association in the final solver avoids a population-by-feature matrix product
unrelated to the current input block. Current-state workspace is independent
of elapsed step count. Generic source dimension, feature count, conditioning,
and rational temporary bit sizes may nevertheless become expensive as order
or precision rises. Adjustable resource limits reject computations; they do
not justify claiming convergence of a permanently capped implementation.

The smallest suitable book destination is **C.4.7.10, directly after the finite
autonomous closure**. Use one theorem with its exact represented-law and
observation contract, followed by the necessary domain, density, initialization,
numerical-stability, arithmetic and cost proofs. Reference unchanged H1/H2
definitions and arguments precisely. Do not paste both the standalone cubature
proof and its repeated numerical-proof version as independent expositions, or
create a second general theory chapter merely to preserve author-file layout.
All essential proofs must still be available in maintained material.

Use `code/pde/observable_solver.py` with the candidate support modules and a
compact guide section in `code/README.md`. Preserve the existing H2 theorem and
prototype/API compatibility. The shared word grammar, source conventions and
loss/transpose factors are natural interfaces where tests should prevent drift;
a broad refactor of unrelated maintained modules is unnecessary for this
addition. The assembled library must bind every canonical import to its reviewed
source and run without study loaders, study paths, author audits, or cached data.

## What this decision does and does not authorize

Proceed to complete candidate assembly and the remaining Part 2 gates for the
selected scope. The proof and library are sufficiently distinct and useful
to justify that work. No new research is needed merely to make the result
appear broader.

Tests, bounded-run generation/analysis recipes, execution results, standalone
installation checks and a frozen proposed edition were not among this selector's
scientific inputs. None was executed here, and no empirical conclusion is made.
Any claim of feasible C-H3 computation must attach reproducible initialization,
runtime, memory, conditioning and restart evidence at declared finite resolutions.
Any required scientific correction blocks acceptance under the later gates.
The two fresh scientific reviews, standalone validation, independent integration
review, and approval of the concrete final addition remain required. This report
requests no user approval and changes no established material.

## Independence, input scope and completion evidence

The selector did not author or assemble any candidate proof or code and wrote
only this report and its assigned scratch. The assignment identified this as
independent relevance selection. I read no study README, other study, author
route, prior verdict, other review report, Git history, or trajectory output.
The candidate proof files contain author provenance and historical internal
check descriptions; those embedded passages were read as part of the assigned
complete files and were not used as acceptance evidence. Supervisor messages
about file readiness/corrections and planned operational degree choices were
not treated as empirical evidence. No scientific acceptance reviewer was
consulted or delegated to, and no Git operation or source mutation was performed.

Required process inputs were read completely: `AGENTS.md`,
`RESEARCH_WORKFLOW.md` (including all Part 2), the rigorous-math skill, and the
conjecture-investigation skill with its research-contract and adversarial-audit
references. Their versions are retained in the scratch manifest.

Scientific read coverage was complete for `docs/README.md` (717 lines),
`docs/NOTATION.md` (98), `code/README.md` (748), and the body of maintained
`docs/global_nonlinear.md` C.4.7.8–9 (lines 11441–12554). A headings-only
section-location search printed headings outside that range; no outside
scientific body was read or relied upon. No further maintained scientific
dependency was fetched: this is the relevance gate, not the complete dependency
proof audit. The unread complement of the global-nonlinear body and all other
maintained scientific files remain outside this review.

All five candidate prose files and all six candidate code files listed below
were read completely. The numerical proof was received as a completed file
with the supplied hash and read in full before this decision. The revised
hierarchy proof, solver and guide were reread completely. Initial combined
tool output truncations were repaired with bounded reads. Initial and final
hash manifests, exact foundation-section hash, and the selector's own working
notes are retained in `data/generated/observable_hierarchy/H3_v2_relevance/`.

The final numerical proof is
`8845a5b6b2e86128027bb5e52b204d69f472011decc84412b3516b29e011af22`.
The exact C.4.7.8–9 text hash is
`c7d7d9f91f6ce66df477154fad798f3d4746a0d6791cf9ccc59252809a9f5bd2`.
The full global-nonlinear file hash below identifies its containing version;
it does not assert that the full chapter was read.

## Final input identities

| Input | Lines | SHA-256 |
| --- | ---: | --- |
| `AGENTS.md` | 47 | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | 224 | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `docs/README.md` | 717 | `6daf2439bc725d63b0764967c20c980a6ef0361abec0c14bf29d396d87807fca` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | 748 | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |
| `docs/global_nonlinear.md` | body scope above | `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161` |
| `studies/observable_hierarchy/H3_v2_scope_proof.md` | 778 | `2c4c6ad2cee83ac0302a4d6beb0152f19127167f1c9ed10f6a611b83b33384dd` |
| `studies/observable_hierarchy/H3_v2_hierarchy_proof.md` | 243 | `75473b2eb19bfa6037627c63c4bf4afd92790d5557b515c231558ca8a11df104` |
| `studies/observable_hierarchy/H3_v2_cubature_proof.md` | 588 | `e1940f443d0f37ac8844d32932915644aefcfdb60d36d5bd13cfd1018c3d7ab1` |
| `studies/observable_hierarchy/H3_v2_guide.md` | 150 | `cec9a675b2c2ca440972c64b0ca1f65abdca8d86fdabb881a242d25f0b081dd8` |
| `studies/observable_hierarchy/H3_v2_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `studies/observable_hierarchy/H3_v2_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `studies/observable_hierarchy/H3_v2_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `studies/observable_hierarchy/H3_v2_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `studies/observable_hierarchy/H3_v2_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `studies/observable_hierarchy/H3_v2_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `studies/observable_hierarchy/H3_v2_numerical_proof.md` | 605 | `8845a5b6b2e86128027bb5e52b204d69f472011decc84412b3516b29e011af22` |

Final snapshot verified unchanged at report completion on 2026-09-13.
