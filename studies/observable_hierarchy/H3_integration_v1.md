# H3 frozen bounded-reference capsule: independent integration review v1

Reviewer: `/root/h3_integration`. Date: 2026-09-12.

**Execution, imports and saved-error carry: PASS at the bounded reference scope. Complete capsule integration: NEEDS ONE MINOR DOCUMENTATION CORRECTION. Full C-H3: NOT MET. A canonical edition has not been assembled or reviewed here.**

The required correction is the missing proof filename referenced by
`H3_circle_kernel.py:6`: it names `H3_circle_kernel_proof.md`, whereas the
complete supplied proof is `H3_candidate_circle_v1.md`. This does not change
the numerical result or remove a proof body, but prevents a clean navigation
sign-off for the complete new material. No other required correction was found
in this integration scope. A passing execution check is not acceptance of the
complete capsule while this correction remains.

## Assignment, independence and authority

I started as a fresh isolated integration reviewer, distinct from the listed
authors/assemblers (`/root`, `/root/h3_shorttime_route`,
`/root/h3_effective_route`), selector (`/root/h3_relevance`), and scientific
reviewers. I read the neutral assignment and manifest, required process and
skills, the complete new frozen H3 material, the complete supplied guides and
notation, and the older passages listed below. I did not read the study README,
history, numerical/route/relevance/internal reports, other review reports,
other studies, chats, or Git history. I did not obtain any scientific review
results or verdicts. I did not delegate.

The supervisor explicitly specialized the generic scientific assignment to
integration: no third complete scientific proof audit, no additional reference
trajectory or initialized-circle reproduction, and at most 60 core seconds on
one core with 8 GiB for tests/scalar checks. I followed that specialization.
The generic assignment's empirical producer run belongs to the two scientific
reviewers. Their outcomes are not premises of this report.

I read root `AGENTS.md` and all of `RESEARCH_WORKFLOW.md` as process instructions,
including the distinction between a study capsule, a proposed canonical edition,
scientific review, integration review, and user-approved promotion. I read
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, together with the latter's
`research-contract.md`, `adversarial-audit.md`, and `decisive-experiments.md`.
No prior-state reconciliation or proof-search campaign was undertaken.

Writes are confined to this report and
`data/generated/observable_hierarchy/H3_integration_v1/`. No frozen input,
established file, Git index or Git metadata was edited. Before the first write,
HEAD was `675e43fc666aabb81f1ee68efa5e4315a3f0ed93`; a metadata-only tracked-status
check counted five changed entries, whose contents were not inspected or adopted.

## Frozen inputs, hashes and complete new read coverage

The manifest hash is
`bc60684162353c63704644f4a543b2f644eb7a27ec6179e293a3bbbb71f241f9`.
The neutral assignment is 87 lines, SHA-256
`229c7f94c3571772c03be7226e48d887028ec65ff090d29eebc92c550db8c683`.
Both were read completely. The manifest itself has 108 lines.

Every line of each new candidate, implementation, test, configuration and
builder below was read. The initial combined output of the reference candidate
was truncated; it was repaired with complete numbered reads of 1–240, 241–470,
and 471–620. No truncated read is counted as complete coverage.

All paths in the table are under `studies/observable_hierarchy/` unless an
explicit `docs/` or `code/` prefix appears. The frozen file hashes and line
counts were checked before building and checked against actual copied bytes
again after the tests.

| Input | Lines read | SHA-256 |
|---|---:|---|
| H3_candidate_reference_v1.md | 1–620, complete | `2135a0d1f3bd9cdb754b1a0f08f7ae9d3c059cfb646360487f7eb1f92c2c78a2` |
| H3_candidate_circle_v1.md | 1–342, complete | `567247c7afa09ac4502bafa4f3dfea0197c449ba5ca46a8a3826ff74d37f54dc` |
| H3_stability_proof.md | 1–124, complete | `a5a68240508b3601faddbc30005626c144190fe38d02d1291787ef3ebeb69735` |
| H3_stability.py | 1–140, complete | `a59194db71e5b17fcd8a4884a0a5839a16c93007cd4e06dc65dbd1bb22bcf65d` |
| H3_shorttime_solver.py | 1–530, complete | `cf3b479826c8900bc4097d023128330c380df415d83b2a782054c5e565542e6b` |
| H3_shorttime_test.py | 1–154, complete | `11dd36c0d7ead265ddc3bfc20f7d5b688d1f6dacac7cfe8b7b652468c81eedb5` |
| H3_circle_kernel.py | 1–337, complete | `ec4975ae0f469755f0fa025e4b4b0b185f6b05fd97dbfa74bd60d34e61ffdef2` |
| H3_circle_kernel_test.py | 1–98, complete | `6550f472cc5876307832e62ed8a0cb451bccfe9a3deafe67ce9d86fb9a1aeb45` |
| H3_reference_solver.py | 1–106, complete | `5ce7e2789083269ed9f5b02a02fc277d9464551655f31b2bc890a0fed1273f62` |
| H3_make_review_capsule.py | 1–58, complete | `7fea40ee5aaa34c666bb94155350e0c839312e2babb97ce96915b506f33f72b1` |
| H3_demo_config_v1.json | 1–55, complete | `baacdb913ed2b92053aa8b647744c2e9260c70d2f6d2b74e0a464d9345091125` |
| dependencies_v1.md | selected older coverage below; 3569 total | `6a40bc9ee6e6de49fbefd9118298c4ab807b1ef52ecf29b99a71937eab0a63d7` |
| H2_proposed_section_v3.md | 1–470, complete older context | `c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2` |
| docs/README.md | 1–670, complete supplied guide | `269f481c6198971875ec22cb1b7e451ad0f3fbf3fe21a41be42a72dd49ae7ce2` |
| docs/NOTATION.md | 1–98, complete supplied notation | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| code/README.md | 1–748, complete supplied guide | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |

The generated `RUN.md` was also read completely. Its SHA-256 is
`40ff512716ca61d14ebb5182443903ae777da82126d0351497a9d7258cbd7669`.

## Precise older dependency scope and unread complement

In `dependencies_v1.md`, the complete scientific passages actually read are:

- **1–591:** packet scope; III.F.1–10 in full, including finite Gaussian
  programs, adaptive conditioning, source response, singular covariance,
  common actions/adjoints, Hilbert–Schmidt ranks, strong multiplier/chain
  calculus and scalar gradients; plus global-nonlinear A.1–4 in full,
  including the sharp norm-two initialized action proof.
- **2032–2627:** C.4.7 model and conclusions 1–3; its supplied observation
  contract; C.4.7.2 in full; C.4.7.3 introductory statement and parts 1–2 in
  full, through N19. This is the source-cap interface used by the new
  short-horizon stability component, including N3 and N9–N19.
- **3322–3569:** C.4.7.4–5 in full, including completion, energy, reached
  uniqueness, actual finite Gaussian readout retention, and same-population
  observation limits.

The unread scientific-body complement is **592–2031 and 2628–3321**:
C.4.1/C.4.2, the older fitted-reference and reference-tail proof excerpts,
and C.4.7.3's weighted transport, mesh-error and reference-anchor machinery.
A heading-only search across the frozen dependency packet exposed the section
titles in these ranges; it did not expose or audit their scientific bodies.
No original chapter outside the supplied packet was opened. This report does
not claim a new proof audit of the long-time foundation or every transitive
dependency of H2.

I read all of `H2_proposed_section_v3.md`, specifically its statement/dependency
scope (1–44), dictionary/action construction (46–164), saved state and equations
(166–225), existence/restart (227–293), convergence comparison (295–388),
observation interface and finite-readout interpretation (390–449), and family
and numerical limitations (451–470). This is exact older placement/API context,
not a rerun of H2's completed prototype audit. In the supplied guides, the
directly relevant interface passages are `docs/README.md:313–431` and
`code/README.md:623–748`; the rest of both supplied guides was also read as
requested context. Their linked older modules and chapters were not read or
executed. The H1 subsection cited by H2 is not supplied as a separate complete
input, so I make no additional H1 proof-verification claim.

## Actual capsule mapping and standalone execution

From `/home/amir/Codes/PDE`, I ran:

```sh
python -B studies/observable_hierarchy/H3_make_review_capsule.py --output data/generated/observable_hierarchy/H3_integration_v1
```

The destination was fresh and the builder succeeded. It verifies all input
hashes before creating the destination and copies files without rewriting
their contents. I independently compared source and destination bytes for
all 16 entries: **426,718 bytes, all equal, all SHA-256 hashes and line counts
matching**. The copied `manifest.json` also equals the supplied manifest byte
for byte. The actual mapping is the manifest's `capsule_name` field; filenames
are unchanged except `docs/README.md -> docs_README.md`,
`docs/NOTATION.md -> NOTATION.md`, and `code/README.md -> code_README.md`.

The original builder is a source-checkout assembly tool. Its copied copy still
expects the original source layout and manifest name; `RUN.md` does not ask
the consumer to rebuild a capsule from inside itself. That limitation does
not affect the four published consumer commands.

I parsed every copied Python file's imports. All are standard-library modules
or copied H3 siblings. I then imported the five implementation/builder modules
and both test modules under Python isolated mode. Every H3 module's resolved
`__file__` was directly inside the fresh capsule. No `pde` module was imported;
the source study and maintained `code/` directory were absent from `sys.path`.
The only explicit added import root was the capsule itself. This verifies
execution without imports from the source checkout's study or maintained APIs.

The frozen JSON is a documentary fixed configuration, not a runtime input
loaded by the driver. I compared its horizon, normalized directions, labels,
masses, normalization, precision, Simpson count, radius, observation/restart
times and signal/error thresholds with the complete hard-coded producer.
They agree. This is not an API accepting arbitrary configuration changes.
The combined CLI pins a core and limits address space/CPU; the resource claim
still requires actual empirical runtime measurements, assigned elsewhere.

## Deterministic tests and scalar checks actually executed

From the fresh capsule directory, the retained harness command was:

```sh
python -I -B integration_checks/run_static_checks.py
```

It loads and runs **both complete original test modules, unchanged**: nine
short-time tests and seven circle tests, 16 total, zero failures/errors. These
are the full suites behind the first two `RUN.md` commands, executed together
under a stricter import/resource environment. The full named-test log is
`integration_checks/full_tests.log`.

Coverage includes exact rational arithmetic and exponential checks, pi and
odd symmetry, the zero-variance Gaussian moment boundary, independent exact
four-point contraction algebra, the derivative envelopes, nonzero-width
checkpoint serialization, malformed-state rejection, uncertain restart,
exact Hermite correlated-Gaussian identities through degree seven,
normal-density derivative algebra, linear-kernel serialization/evaluation,
parameter-error perturbations, and represented irrational/rational circle
directions with boundary rejection.

Additional retained checks used synthetic finite scalar fixtures:

- Saved/reloaded all seven coefficient intervals and nonzero-width `b,beta`
  endpoints exactly. Advanced a synthetic uncertain state by `1/400` and
  checked the eight endpoint combinations against independently computed
  rational alternating-series bounds for `exp(-kh)`, including `beta` carry.
- Serialized/reloaded an exact linear test kernel and supplied `b` with
  radius exactly `1e-8`. Its returned prediction contains both exact readout
  endpoint predictions; prior readout width is charged rather than discarded.
- Checked the combined wrapper at total times `0`, `1/400`, and `1/200`.
  Each result equals the numerical kernel enclosure widened by the cumulative
  analytical envelope evaluated at that total time. The enclosure expands
  from midpoint to final time, so reload cannot reset that error origin.
- Rejected negative/excess continuation, excessive readout uncertainty,
  a box disjoint from the unit circle, and a state beyond the horizon.
- Evaluated the static circle configuration bounds and `H3_stability.report()`
  using only scalar arithmetic. The latter passes its exact rational
  inequalities: `L=8.2608`, Gaussian tail upper bound approximately
  `1.159625253499717e-16`, and the **conditional** error bound for a separately
  proved defect `1e-5` approximately `5.1046964863380474e-8`.

The synthetic fixtures are interface tests, not certificates for the actual
reference law or new empirical hidden-motion observations. After the original
suites, the harness explicitly replaces the reference and initialized-circle
producer/integration entry points with functions that raise if called.
The only Gaussian moment evaluation was the original suite's authorized
**zero-variance, 512-panel static boundary test**. I did not execute
`H3_reference_solver.reproduce`, `H3_shorttime_solver.run`,
`H3_circle_kernel.initialize`, or a neural network. I did not inspect any
scientific reviewer's reproduction output.

Measured combined test/scalar process: **2.213854946 s wall,
2.212478 s user CPU + 0.000207 s system CPU, 21,528 KiB peak RSS**;
affinity was the single CPU `{0}`. The harness imposed 58 CPU seconds,
a 60-second alarm, and an 8-GiB address-space limit. Python was **3.10.12**,
Decimal precision **60**, on
`Linux-5.15.0-151-generic-x86_64-with-glibc2.35`.
The test runner reported 2.102 seconds for the 16 original tests.
The additional inventory/hash/AST checks were small single-process metadata
checks; no numerical campaign or budget extension occurred.

## Interfaces, notation, links, and preservation

The declared target matches the supplied normalization: bias-free two-hidden
tanh, `u=x/sqrt(2)`, residual `f-y`, unhalved population squared loss, physical
time `T=1/200`, mobilities `(n,1,n)`, initialized variances `(1,1/n,1/n^2)`,
two separate populations, and the actual adjoint of the reused action. The
finite-network interpretation keeps the actual random readout; population
`c(0)=0` is explicitly its limit. No finite-width neural initialization was
silently changed by an executable here, because none was executed or built.

The finite-law formulas specify general `b,beta`, while the actual reference
implementation uses the two scalar symmetry-reduced coordinates. This is
stated in N4 and must remain visible. The candidate distinguishes `fB`, its
hidden Duhamel approximation, from the cheaper frozen-kernel prediction `fF`;
the numerical prediction API uses the latter with its separate canonical-GF
envelope. The paired RMS formulas concern the same initial/current population
coordinate. Their expansion and error terms do not substitute independently
coupled marginals or zero hidden motion. Full independent proof verification
and empirical measurement remain the scientific reviewers' work.

At the interface, the circle module returns an enclosure for `fF` given a
provenanced current `b`; `H3_reference_solver.prediction()` then adds the
canonical-GF envelope at the saved cumulative time. The two initialized
components need no shared random sample: they independently enclose
deterministic contractions of the same prescribed Gaussian initialization.
The complete code uses interval endpoints/positive `q,k` gates, and the circle
API charges coordinate-box width and rejects lower Decimal precision. The
loaders validate structure but do not authenticate the scientific provenance
of invented coefficients; the candidate explicitly retains that premise.

The symmetry-reduced checkpoint has two moving intervals and seven initialized
intervals, plus exact elapsed time and fixed certificate metadata. The circle
record contains `q,v` and eight coefficient intervals, with derived rational
tail/error summaries. Runtime also holds rational midpoints/Lipschitz bounds,
streamed integration accumulators, configuration/error dictionaries and output
records. Thus the state is not correctly described by only “two scalars” or
only the moving coordinates. The full producer is a bounded fixed computation,
not a storage/conditioning theorem as accuracy or input denominator size grows.
The measured RSS above is for this review's deterministic process, not a new
measurement of the numerical producer's complete storage claim.

The supplied H2 section remains qualitatively broader: it has retained joint
population states, nested initialized dictionaries and asymptotic convergence.
The new scalar component does not implement H2's arbitrary-order law fields or
`pde.observable_closure` API. Its use of `b`, `beta`, `v`, etc. is locally typed;
the circle proof explicitly distinguishes its upper variance `v` from the
short-time reverse-source `v`. No new maintained symbol or API overwrites H2.

A scan of copied Markdown found 25 relative file links, of which 24 do not
resolve within this flat capsule. These belong to the **unchanged supplied
context guides**, which link to the full established library and code examples;
they are not missing new theorem bodies or promised runnable H3 examples.
The four external contextual URLs were read as text and not fetched. The
dependency packet retains original chapter paths as provenance while supplying
the selected bodies. A canonical edition would need functioning chapter/API
navigation and its guide examples checked in that edition; this capsule does
not claim those checks. The available new proof body is discoverable from the
manifest and candidates, but the stale direct module reference remains a
separate required correction:

1. **Required, minor navigation correction:** change the new circle module's
   proof pointer from `H3_circle_kernel_proof.md` to the supplied
   `H3_candidate_circle_v1.md`, or provide an explicit capsule navigation
   mapping for that legacy name. Preserve this frozen v1 packet and this
   adverse report; review the corrected integration scope before declaring a
   clean integration PASS. No scientific formula change is requested.

The raw file-reference scan also matched `platform.py` inside
`platform.python_version()`; those are lexical false positives, not missing
modules or proof links. They are not counted as findings.

## Component decisions and unresolved original obligations

| Component | Integration decision | Boundary |
|---|---|---|
| Byte-preserving assembly and standalone imports | PASS | 16 exact files; runtime imports only copied siblings/stdlib |
| Both complete deterministic suites | PASS | 9 + 7 tests; no empirical producer reproduction |
| Checkpoint/kernel serialization and error carry | PASS | Actual endpoints preserved; synthetic scalar composition checked |
| Static source-cap/conditional propagation interface | PASS | No assertion that a numerical full-RHS defect is available |
| Combined prediction interface | PASS | Provenanced reference state, represented unit input, cumulative GF envelope |
| Complete new capsule navigation | NEEDS MINOR CORRECTION | One stale proof filename at circle module line 6 |
| Candidate empirical numerical claims | NOT INDEPENDENTLY REPRODUCED HERE | Explicitly assigned to the two scientific reviewers |
| Proposed canonical edition | NOT ASSEMBLED / NOT REVIEWED HERE | No maintained new chapter/module/guide changes supplied |
| Original full C-H3 | NOT MET | Fixed-order reference component leaves the stated obligations open |

The bounded component concerns only the orthogonal opposite-label two-atom
reference and specified hidden RMS observations, with whole-circle prediction.
It supplies no effectively represented active nonorthogonal/nonatomic family
with computable membership in H2's existential neighborhood. Increasing
quadrature panels or precision does not remove its analytical nonlinear
error floor. It gives no terminating arbitrary-positive-tolerance refinement
of nonlinear GF, and no certified general fixed admissible joint-observation
tuple interface. It does not make all H2 population/source/input integrations
effective with accuracy-dependent total cost and precision accounting.
These are substantive original milestone gaps, explicitly admitted by the
candidate, not corrections that this integration review attempted to solve.

Likewise this report supplies no third empirical reproduction, no independent
whole-book proof audit, no acceptance based on another reviewer's verdict, no
user promotion approval, and no candidate-to-installed-edition correspondence.
Those statuses must not be inferred from the successful capsule execution.

## Retained evidence

All generated evidence is under
`data/generated/observable_hierarchy/H3_integration_v1/integration_checks/`:

| Artifact | SHA-256 |
|---|---|
| run_static_checks.py | `c3325daa510b5ac1b8c2188b66583765d62c0da2ea050d3a01a334fee1c60e9a` |
| full_tests.log | `942f6a27110a05b3b7a4e39c00e9d178fc770346b8aa5d2484536599d7652168` |
| static_result.json | `84be804cc2bf675c7d8fa0e826540bb56861cabaa52a73769cbe8f4598c3abb2` |
| capsule_inventory.json | `1f4bccad381eb4ce2f9eb447e84f41bd59af8ce3ce86530f093eea592d7537b2` |

`static_result.json` retains module origins, import path, environment, precise
resource measurements, synthetic outputs and hashes of the test/scalar
evidence. The inventory retains every actual source-to-copy byte/hash mapping,
import list and raw navigation scan. `synthetic_checkpoint.json` and
`synthetic_kernel.json` are explicitly synthetic interface fixtures;
`circle_configuration_static.json` and `stability_scalar.json` are scalar
verification outputs. No empirical run output is concealed among these files.
