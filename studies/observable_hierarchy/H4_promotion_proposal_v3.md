# C-H4: qualitative observable computation through physical time 40

Status: complete and independently reviewed; ready for user approval. This
proposal does not authorize or apply established-book/code changes.

The proposed addition extends H3's finite autonomous observable method from
its short horizon to `[0,40]` on a fixed, explicitly represented family with
nonorthogonal atomic and nonatomic members. It proves convergence to the same
nonlinear population gradient flow and supplies a reusable executable law
interface, bounded validation producer and observation analyzer. The intended
book placement is C.4.7.10, part D, immediately before C.4.8. The existing
chapter bytes are preserved.

## Exact scientific scope

Keep the bias-free two-hidden-layer tanh model, independent stored Gaussian
variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved squared loss and
physical gradient-flow time. The initialized Gaussian action and its actual
adjoint are unchanged. Finite-network identification retains the actual
finite random initial readout and converges in probability to the canonical
population flow.

The family is fixed once and for all. Set `E0=8192`, `E(j+1)=2^Ej` for ten
steps, and `rho=2^(-E10)`. For rational intervals `[a,b]` and `[c,d]` in
`[-1,1]`, use equal label masses on `sqrt(2)*U(rho*S)` with label `+1` and
`sqrt(2)*R*U(rho*V)` with label `-1`, where `S,V` are uniform on their
respective intervals, `R` is a quarter-turn, and
`U(s)=((1-s²)/(1+s²),2s/(1+s²))`. Degenerate intervals give atoms. The
choice `a=b=0,c=d=1` is nonorthogonal; nondegenerate intervals give nonatomic
laws. Neither parameters nor support shrink with refinement.

The complete support proof gives an explicit positive time-40 neighborhood
containing this family. It reuses the established raw-source comparison,
tail estimates, strong completion and actual finite-GF identification, with a
new explicit cap transfer and proof that the displayed dyadic radius is
admissible. It does not assume that the new radius lies within an unnamed
earlier neighborhood. The target flows satisfy

\[
R_\mu(f_\mu(40))\le\tfrac14,\qquad
J_{\ell,\mu}(1/200)\ge10^{-13}\quad(\ell=1,2).
\]

For each separately fixed represented law, the exact order-`N` closure
converges uniformly on `[0,40]` and the entire input circle to that flow.
At fixed `N`, finite numerical realizations converge to the exact closure.
The stated deterministic iterated limit removes finite arithmetic error,
time discretization, input-law integration, retained population integration,
initialization quadrature and generic source regularization, in that order;
closure order tends to infinity last. The generic source regularizer is
unused on the optimized core branch. Resource allowances increase when
needed to admit each finite member of the limit.

Both layers' training-averaged same-population initial/current activation
pair laws converge uniformly in time in `W2`, as do their RMS displacements
and the risks. The joint initialization and current populations, forward and
adjoint contractions, nonlinear residual feedback and complete current state
are retained. Computation starts at its prescribed initialization and reaches
40 using bounded state and stage storage at fixed resolution. Checkpoint
continuation uses its own complete state. No target states, accumulated
trajectory history, raw neuron-by-neuron middle matrix, surrogate or runtime
arbitrary-action oracle is used.

The complete canonical proof is [H4_proposed_section_v2.md](H4_proposed_section_v2.md).
The 271-input final [review manifest](H4_review_manifest_v3.json) identifies
the complete dependencies, full guides, code, tests and original empirical
records. The final standalone edition is
`data/generated/observable_hierarchy/H4_candidate_v3/`, with edition-manifest
SHA256 `64bd43d30e11e1f591b12f9c07c76d192c5fa7dcd8f22c1c0e3fd313c27e8250`.

## Numerical scope and limitations

The law's exact exponent expression and rational endpoints are executable and
retained in every configuration and restart. Input integration uses a
refinable midpoint rule; its exact transport error is at most `rho/m`.
The exact denominator needs `E10+1` bits when resolved, and this cost is
explicitly charged. Default resource limits reject representations they
cannot hold.

At every tested precision the twelve supported runs explicitly collapse the
perturbation to the reference. They demonstrate operation through 40 via the
atomic and nonatomic law interface, but do not numerically resolve the
supported perturbations. Two broader radius-`1/20` nonatomic cases are
resolved and clearly labelled exploratory; the time-40 theorem is not
asserted for that radius. This limitation is present in the theorem, guide,
metadata, producer checks and records.

No quantitative convergence rate, arbitrary simultaneous refinement,
finite-run accuracy certificate, automatic tolerance selection or
cost-to-accuracy bound is claimed. Target substantial-learning bounds are
not finite-run acceptance tests. No activity assertion at time 40 is added.

## Validation and independent reproduction

The predeclared plan contains fourteen configurations at genuinely enriched
orders 1, 3 and 5, with feature dimensions `(5,3)`, `(35,10)` and `(128,21)`.
It includes separate time, initialization, population and input-law
refinements, two resolved exploratory arc rules, and a tiny rational
24/36-digit comparison. Each configuration runs from initialization to 40
and checks exact own-state restart from 20, comparing all state and data
arrays, metadata, arithmetic and final prediction.

All fourteen author configurations passed. Worker CPU totaled 506.291
seconds, with peak RSS 56,119,296 bytes. The deterministic observable suite
passed all 67 tests, as did the inherited exact rational reference-constant
check. Each run was bounded in advance by 1200 CPU/wall seconds and 4 GiB,
with one worker/thread and 7200 cumulative CPU seconds per set. No broad
sweep or finite-network training campaign was performed.

The [fresh independent reproduction](H4_reproduction_v1.md) repeated all
fourteen configurations and 67 tests through the maintained producer and
analyzer in the standalone workspace. It completed in 510.725 charged CPU
seconds, peak RSS 56,193,024 bytes. Its independently decoded exact
observation archives and a later coordinator comparison verify that all 112
exact observation/checkpoint files match the author's outputs byte for byte.

The reproduced runtime, initializer, solver, arithmetic, producer, analyzer
and plan are byte-identical to the final v3 candidate. Two test docstrings
and scratch-error messages changed; test logic is identical. The final v3
clean-environment guide recipe separately passed all 67 supplied tests.
[H4_final_correspondence_v3.py](H4_final_correspondence_v3.py) and its generated
record verify every frozen input, exact runtime correspondence, all 112
archives and the unchanged live destination bases. The independent reproducer
also checked this correspondence in [a final static addendum](H4_reproduction_addendum_v3.md),
including a complete reading of the final code guide and all three test
setups. No additional trajectory or test was run for that addendum. The later
guide was not represented as an input to the original execution. A preserved
[wording correction](H4_reproduction_addendum_v3_correction.md) distinguishes
the original code-only manifest from the directory's later documentation
supplement; runtime correspondence is unaffected.

## Exact proposed destinations

The [final mapping](H4_promotion_mapping_v3_final.json) records all source, destination,
current-base and proposed hashes, including the one canonical test-import
rename. The [complete proposed diff](H4_proposed_changes_v3.patch) is a
reviewable preview of these exact bytes; it has not been applied. Only these
eleven established paths are proposed:

| Destination | Addition or change |
|---|---|
| `docs/global_nonlinear.md` | Insert the complete time-40 part D within C.4.7.10; preserve existing text. |
| `docs/README.md` | Update the H4 roadmap and scope, preserving the book's philosophy. |
| `code/README.md` | Add the law API, limits, resource accounting and reproduction guide; supply fresh scratch in all three affected test recipes. |
| `code/pde/observable_laws.py` | Exact law descriptions, guarded arithmetic realization, quadrature and refinement. |
| `code/tests/test_observable_laws.py` | Law representation, collapse, refinement and resource-bound tests. |
| `code/scripts/validate_observable_horizon.py` | Time-40 producer, paired observations and exact own-state restart. |
| `code/scripts/run_observable_validation.py` | Optional worker selection, retaining the existing H3 default. |
| `code/tests/test_observable_horizon_validation.py` | Producer, archival precision and restart checks. |
| `code/scripts/analyze_observable_horizon.py` | Independent loss/pair algebra and declared refinement comparisons. |
| `code/tests/test_observable_horizon_analysis.py` | Meaningful analyzer checks. |
| `code/validation/observable_horizon_plan.json` | The fixed fourteen-configuration bounded plan. |

The solver, initializer, compiler, arithmetic and word modules are unchanged.
Maintained code and proofs require no study history or archived trajectory as
an input. Generated evidence remains in the study's generated-data namespace.

## Review gate and recommendation

Both fresh complete scientific reviews,
[E](H4_scientific_E_v3.md) and [F](H4_scientific_F_v3.md), returned **PASS**
for the whole qualitative objective, implementation and bounded empirical
claims, with no required corrections or missing inputs. Each read all 1754
new scientific lines, all 8531 dependency lines, full guides and all supplied
code/tests/plans. Each verified all 271 frozen files and completed independent
algebra and archive attacks. The separate [integration review](H4_integration_v3.md)
also returned **PASS**, with its precise older read scope and unread complement
stated explicitly. This is not a claim to have freshly reviewed the entire book.

The coordinator read all three original full reports and handwritten checkers,
verified their provenance and results, and rechecked the unchanged packet.
The [acceptance record](H4_acceptance_v3.md) preserves these details and the
original report hashes. Prior adverse reports and explicitly incomplete
stopped reviews remain preserved and do not substitute for the final gates.

I recommend applying exactly the eleven mapped additions/changes. The full
qualitative time-40 result is complete at its stated fixed-family scope, and
the executable method has been independently reproduced within the declared
budget. No established changes have been made. Part 2, step 5 of
`RESEARCH_WORKFLOW.md` requires explicit user approval of this concrete
reviewed package before promotion.
