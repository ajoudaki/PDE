# Independent relevance and placement of the signed test-risk theorem

Selector: `sign_relevance`, 2026-09-10. Assigned scope: Part 2, step 1 of
`RESEARCH_WORKFLOW.md`. This report concerns `SIGN_THEOREM.md`, including its
analytic reduction and new deterministic arithmetic certificate. It is a
selection decision, not either complete scientific audit or an integration
review.

## Decision

**Accept for assembly, with the narrow scope below.** A proved positive
equal-training-loss test-risk difference for this specified nonlinear,
two-hidden-layer Gaussian network is sufficiently relevant and distinct to
justify a book addition. Its small effect and local scope limit its
interpretation but do not make the result vacuous. The signed coefficient is
the decisive addition: activity and faster training alone did not give it.

This decision does not accept the current files for direct integration.
The complete signed candidate must pass its fresh scientific audits; the
actual maintained edition must separately meet the workflow's assembly,
reproduction, integration-review and user-approval requirements. The present
study driver is not already a reusable maintained interface.

Scientific completion and book packaging are separate outcomes. If the fresh
audits accept the signed theorem, the user's fixed central comparison is
resolved at the theorem's stated scope. It need not remain labelled open
while an optional book edition is prepared. No new teacher, design, time
estimate, training experiment or generalization research is needed to make
this selection favorable.

## Distinct value and duplication

The current book says explicitly that successful optimization does not yet
connect the selected representations to out-of-sample risk
(`docs/README.md`, scientific question and passive-input discussion).
`global_nonlinear.md` currently ends with C.3's weighted-loss activity
correction. C.1 supplies local actual-flow and vanishing-step capture;
C.3 supplies strict hidden movement, changing kernels and surviving
nonaffinity. Those statements do not compare the test risks of learned
and frozen representations at equal loss.

The proposed signed theorem supplies such a comparison. Both hidden blocks
and the readout train with the original stored Gaussian scaling; the rank-two
correlated input geometry remains present, as do both uses of the connector
and its response terms. The baseline freezes both initial hidden layers and
trains its readout with the same loss. The matching time removes the positive
training-speed contribution before taking the teacher projection. In the
source notation, the relevant scalar is

\[
\chi=2\int\cos(3\alpha)[J(\alpha)-\beta a(\alpha)]\,d\mu(\alpha),
\qquad p^T(J_{\rm train}-\beta a_{\rm train})=0.
\]

Thus the positive sign is additional information about the learned predictor
away from the three training points. It is not inferred merely from
`mathcal A>0`, `beta>0`, a nonzero hidden velocity, or a larger tangent kernel.
The trajectory remainder supplies an actual positive-time conclusion from
the coefficient, rather than treating an initialization jet as a trajectory.

The earlier `PROMOTION_C4.md` is a proposed partial reduction and is absent
from the established chapter. Its passive-circle construction, matching,
remainder and explicit coefficient are useful assembly source. A signed
edition should merge and update that material, with one final theorem and
one proof, rather than introduce adjacent open-sign and signed versions.
Its previous promotion status or reviews are not evidence for this new
selection or for the new certificate.

The implementation comparison also shows a real distinction. The maintained
`gaussian_moment` computes rational monomial moments; `gaussian_hidden_head`
evaluates supplied rational polynomial data; and `quadratic_axis_certificate`
regenerates a different exact polynomial witness. Inspection of these
implementations confirms that none supplies certified nonpolynomial tanh
cubature or this risk comparison. Their existing contracts should not be
expanded by implication. Conversely, finite moving jets and Gaussian
conditioning already have established homes and need not be republished as
new discoveries here.

This is a comparison with the inspected local book and code. It is not a
priority claim about the external literature or a fresh audit of every
chapter.

## Accepted scope and limitations

The suitable theorem retains all the following particulars:

- Exactly two tanh hidden layers, no biases, input dimension two, independent
  stored Gaussian initialization variances `(1,1/n,1/n^2)`, raw mobilities
  `(n,1,n)`, and mean squared loss on the angles `0,pi/5,-pi/5` with the
  prescribed `cos(3 alpha)` labels.
- Uniform-circle squared test risk against that fixed teacher. The training
  design is fixed, not sampled iid. The comparison is at equal training
  loss, not equal physical time or equal computation.
- A unique local matching clock and an actual-flow bound
  `|Delta(t)-chi t^3|<=M t^4`, with strict rational coefficient bounds
  `27/100000 < chi < 273/1000000` and
  `35309/1000000 < beta < 35311/1000000`.
- Consequently, strictly better test risk on a width-independent positive
  interval. The width independence is meaningful; the time endpoint and
  remainder constant have not been numerically evaluated.
- Finite GF and every deterministic vanishing raw-GD-step transfer in
  probability only on each fixed `[delta,t0]`, `delta>0`, with the actual
  small common random initial readout retained. There is no quantitative
  width threshold or uniform finite-width sign assertion down to zero.

The initial risk is `1/2`, and the leading difference is about
`0.000272 t^3`. That establishes a mathematically strict local effect, with
no demonstrated practical magnitude or specified useful training interval.
It proves neither later-time dominance nor global fitting nor a universal
benefit of hidden learning. It supplies no iid-average risk guarantee,
sample-complexity theorem, or growing-depth/sample/dimension limit.

These limitations should accompany the main theorem and its guide entry.
They are not reasons to demand stronger research before retaining this
fixed witness. In particular, an unevaluated but finite `M` and positive
`T` are sufficient for the stated existential positive-time conclusion;
requiring a numerical `t0` would change the target being selected.

## Maintenance cost and reproducibility

The sign depends jointly on the complete analytic bounds and an executed
finite calculation. Its maintenance cost is appreciably greater than that
of a short exact identity. The four new error/assembly documents currently
contain 1,124 lines, before the 642-line canonical baseline reduction; the
driver, kernel and angular-bound source add 706 lines, and their two
dedicated check scripts add 301. These counts include material that can be
consolidated, but a short theorem cannot replace its proof obligations.

The cost is bounded and justified by the scientific distinction. The saved
production metadata records a successful target-26 run, 64 evaluated
angular nodes representing a 256-point rule, 86,101,134 upper Gaussian nodes,
31.18 CPU seconds and about 37 MiB process peak RSS on its recorded system.
Those are observed production figures, not an independently reproduced
performance guarantee. Reproduction is practical enough to retain as a
bounded certificate command rather than rely on an archived answer.

The technical maintenance contract must remain explicit: Python 3.10+ and
NumPy for the current driver, a C++17 compiler with the checked flags,
binary64 round-to-nearest, at least 64 significand bits in `long double`,
and the proved grid/input ranges. The arithmetic proof deliberately avoids
assuming the accuracy of library `exp` and `tanh`; exact dyadic input/output
bits and rational covariance discrepancy bounds are substantive parts of
the method. Singular passive covariances are covered without differentiating
their numerical root factors. These details cannot be omitted from a
maintained certificate merely because a successful run printed a positive
flag.

Direct inspection found concrete assembly work:

- `certificate_driver.py` derives a repository root from its study location,
  restricts outputs to `data/generated/two_layer_test_risk`, hashes study
  documents including the README, and requires Git metadata at runtime.
- It combines constants, numerical root selection, exact interval algebra,
  subprocess execution, file output and campaign bookkeeping in one CLI.
  It also changes numerical-library thread environment variables on import.
  Its internal helpers are not a documented public API with independent
  ownership, exceptions and supported-input contracts.
- The C++ token interface is specified, and useful arithmetic and supplied
  finite-rule checks exist, but a package installation and compiler-availability
  contract has not been assembled. Unsupported arithmetic environments must
  fail explicitly.

These are concrete packaging obligations, not evidence against the study's
mathematics. A broad cubature framework, symbolic population compiler or
training solver would impose unjustified extra scope. Keep the maintained
interface fixed to this certificate and keep the compiler dependency opt-in
so ordinary finite-network imports remain simple.

A public Python API inside `pde` is **not necessary** for the mathematical
theorem or for this placement acceptance. A self-contained chapter with its
complete executable finite certificate is enough, provided that executable
has a maintained, compact reusable interface. Part 2, step 2 says code must
have a "compact reusable API with conventions, supported ranges and numerical
limitations" and calls for API examples. I interpret a precisely specified
certificate command, fixed configuration, machine-readable rational output
and documented failure contract as sufficient here; the rule does not require
putting a new general library abstraction in `pde`. Internal pure arithmetic
and contraction functions can be separated from the command's build/output
bookkeeping and tested without making every helper public. The current
study-bound CLI still needs that bounded assembly work.

## Smallest suitable concrete destination

1. Extend `docs/global_nonlinear.md` by **C.4, "Early test-risk improvement
   at equal training loss for a fixed tanh model."** Merge the existing
   proposed C.4 reduction with the signed theorem. Cite the already
   established C.1--C.3 and Gaussian-conditioning bodies instead of copying
   them again. Include the passive-circle capture, unique clock, controlled
   remainder, exact coefficient and finite-width boundary needed by this
   theorem. Keep the chapter's principal global theorem distinct from this
   local subsection.
2. Put the complete additional Gaussian, angular and arithmetic proof into
   a clearly local certificate appendix within that chapter, with one
   consistent notation and an exact displayed final enclosure. It belongs
   with its only selected application; a new generalization chapter or
   expansion of the generic Gaussian-calculus chapter is unnecessary.
3. If an established edition is pursued, the smallest code destination is
   a fixed-certificate tool such as `code/tools/tanh_risk_certificate.py`,
   its private C++ kernel and exact angular-bound helper, with focused tests
   under `code/tests/`. Its documented command should regenerate and return
   rational bounds under the declared fixed configuration and accept a
   caller-selected fresh output location. Separate pure interval/assembly
   methods from build/run/output bookkeeping. A public
   `code/pde/tanh_risk_certificate.py` API is an optional later organizational
   choice, not a selection condition. These paths describe a proposed
   destination, not code already present or approved.
4. Make the minimal corresponding updates to `docs/README.md` and
   `code/README.md`: identify the fixed local comparison, the computer-assisted
   proof, its command and limitations. The current assertions that no theorem
   relies on a generated coefficient table and that code is unnecessary to
   check the proofs must be reconciled precisely with this addition. Preserve
   the distinction between this fixed-design theorem and a general
   generalization theorem.

The maintained edition must run without `studies/`, its README, prior
verdicts, Git history or retained generated arrays. Its own source, complete
proof, fixed configuration, independent checking route and reproducible
command must suffice. A cited stored result alone would not meet this
selection's proposed destination. No established file was changed by this
report.

The coordinator reports that the two authorized full calculations have now
been used: original production and a byte-identical fresh reproduction. This
report does not read or adopt the latter reviewer's findings, and it
authorizes no third coefficient run. The smallest edition should preserve
the scientific producer and use deterministic interface, path-independence,
exact-arithmetic and supplied-rule tests for relocation. This is a
computer-assisted inequality, not an empirical training claim requiring a
new training campaign. The later gates must verify correspondence to the
already reproduced computation and inspect all assembled proof/code; a
change to the numerical algorithm, coefficient inputs or error semantics
cannot silently inherit the old execution evidence. If such a change becomes
necessary, its validation is a named remaining packaging/correctness
obligation under the user's budget, not a reason to expand this selection
into further research.

## Independence, reading and checks

I did not author or assemble the theorem, its analytic reduction, certificate
or previous proposal. The disclosed authors/assemblers are `root`,
`cubic_derivation`, `matching_remainder`, `quadrature_check`, `sign_structure`,
`certified_error`, and `certification_engine`. I read no previous selector
report, scientific-review verdict, component-review report or the concurrent
signed reviewers' findings. I did not read the study README or perform author
startup. Author provenance/status paragraphs within complete proof sources
were visible; they were not accepted as validation.

Complete source reading: root `AGENTS.md` and workflow, `docs/README.md`,
`docs/NOTATION.md`, `code/README.md`; `SIGN_THEOREM`, `RESULT`,
`CUBIC_DERIVATION`, `MATCHING_AND_REMAINDER`, `PROMOTION_C4`,
`CERTIFIED_ERROR`, `CERTIFICATION_ENGINE`, `ANGULAR_CERTIFICATE`,
`DRIVER_CERTIFICATION`; the full driver, C++ kernel, angular-bound source,
their two dedicated check scripts, `check_coefficient.py` and
`check_finite_identity.py`. I also read the neutral signed-audit assignment
to confirm its scope; I did not undertake either reserved full audit.
Truncated displays were repaired with bounded reads.

Current coverage inspection: the global-nonlinear chapter opening,
lines 2449--2665, 2760--2948, and complete C.3 through line 3829; full
`gaussian_moments.py`, and the actual `quadratic_axis_certificate` and
`gaussian_hidden_head` implementation bodies. Searches covered risk,
passive-input, equal-loss, matching and frozen-feature language across the
current chapter files and maintained package. I did not reread the entire
C.1--C.2 proof or unrelated book sections; their complete independent
scientific verification belongs to the assigned audits. No external theorem
or source was imported, and no missing input prevented this placement
assessment.

I read the original production metadata and aggregate result fields, and
loaded its JSON to count all 64 angle rows. A small exact `Fraction` check
confirmed that the recorded chi and beta endpoints lie strictly within the
theorem's rational intervals. A SHA-256 check confirmed that the recorded
driver, kernel, angular source and operative analytic source versions still
match the production metadata. I did not rerun Gaussian integration,
reassemble all primitive outputs, or execute the deterministic tests; those
checks are assigned to the independent scientific reviewers. No new
experiment or proof search was launched. HEAD at inspection was
`df1117948764a984e7fd2d28949a3c87bc284f84`; concurrent files were preserved,
and the Git index was not changed.

Key inspected versions:

| Input | SHA-256 |
|---|---|
| `SIGN_THEOREM.md` | `18979c2a785b63752e0f3019f0266699f8852055512d566fba1a1c412bbb8a28` |
| `CUBIC_DERIVATION.md` | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| `MATCHING_AND_REMAINDER.md` | `ebefcae59267dd14a71d4e93e3a287126471f178a42646fe60b5abd45894157d` |
| `PROMOTION_C4.md` | `b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4` |
| `CERTIFIED_ERROR.md` | `bcf7fa482d948b73c7ba82b60f514776dbd6d3609a3fb429744aaf507a76c9ad` |
| `CERTIFICATION_ENGINE.md` | `52768b83be66674bf9895fd28ff1a2e3a84f138b646198b583f019b9066acb16` |
| `ANGULAR_CERTIFICATE.md` | `a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2` |
| `DRIVER_CERTIFICATION.md` | `871a474c95a36790604c882949ad1cd5870d0965fe11d16c3380fa134793f3de` |
| `certificate_driver.py` | `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1` |
| `certificate_kernel.cpp` | `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9` |
| `angle_error_bound.py` | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| `docs/global_nonlinear.md` | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| `docs/README.md` | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `code/README.md` | `00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774` |
| Original certificate `result.json` | `89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d` |

The original numerical evidence is in
`data/generated/two_layer_test_risk/certificate_20260910_01/`. This report
changes only `studies/two_layer_test_risk/SIGN_RELEVANCE.md` and concludes
the assigned independent selection.
