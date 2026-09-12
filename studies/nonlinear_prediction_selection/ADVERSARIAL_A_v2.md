# Incomplete isolated adversarial review record — candidate v2

**Status: STOPPED BY COORDINATOR; INCOMPLETE REVIEW; NO ACCEPTANCE VERDICT.**

Reviewer: `/root/adversarial_a_v2`.

The coordinator stopped this review after notifying the reviewer that the v2
packet was superseded and would not be submitted for acceptance. The latest
instruction was to stop new scientific reading, promptly preserve the actual
work already done, and return without inferring PASS or complete review
coverage. This document complies with that instruction. It is a record of an
interrupted review, not the original assignment's completed review report and
not an acceptance recommendation. The mathematical observations below are
provisional records of checks already performed; no further scientific audit
was undertaken after the stop instruction.

## Assignment and isolation

The original task was a fresh, complete, independent adversarial review of
`CANONICAL_ADDITION_v2.md` and the exact frozen input set specified in
`REVIEW_ASSIGNMENT_v2.md`, including the unchanged dependencies whose filenames
retain `v1`. The candidate fingerprint supplied with the assignment was
`c70839b89be14f59800016dd250fbacf0f2f29c61978c68f85170316f3205396`.

This reviewer is distinct from the contributors and prior reviewers named in
the neutral assignment. The reviewer did not read the study README, v1
candidate, author component drafts, corrections, prior reviews, study history,
other studies, other tasks, or later packets. No scientific findings were
exchanged with another reviewer. A scheduling message about preparation of a
later packet supplied no scientific information and was not used as evidence.
The later stop message is the reason this record is incomplete.

The reviewer read `AGENTS.md`, both parts of `RESEARCH_WORKFLOW.md`, the
`solve-math-rigorously` and `investigate-conjectures` skills, and the latter's
applicable `research-contract.md`, `adversarial-audit.md`, and
`decisive-experiments.md` references. No linked scientific materials outside the
frozen packet were retrieved. No training experiment, Git operation, or
established-file edit was performed. Writes were confined to this report and
`data/generated/nonlinear_prediction_selection/adversarial_a_v2/`.

## Actual reading record at interruption

The following are the actual ranges displayed and read, not a certification
that every mathematical obligation received a completed adversarial audit.
The interrupted review had reached report preparation, but its final
assessment and full original report were not completed.

| Frozen input | Actual lines read |
| --- | --- |
| `REVIEW_ASSIGNMENT_v2.md` | 1–97; reread before final consistency checks |
| `CANONICAL_ADDITION_v2.md` | 1–420, 421–840, 841–1260, 1261–1680, 1681–2100, 2101–2300; selected source, theorem, derivative, and margin passages reread |
| `PROPOSED_EDITS_v2.json` | 1–16; reread for deterministic scope checks |
| `PROPOSED_GUIDE_v1.md` | 1–285 in a separate full read after repairing truncated combined output |
| `DEPENDENCIES_GLOBAL_v1.md` | 1–620, 621–1180, 1181–1790, 1791–2360, 2361–2950, 2951–3530, 3531–4110, 4111–4690, 4691–5280, 5281–5870, 5871–6460, 6461–7060, 7061–7660, 7661–8260, 8261–8580, 8581–8901 |
| `DEPENDENCIES_GAUSSIAN_v1.md` | 1–300 and 301–550; 1–125 and 350–550 reread |
| `DEPENDENCY_GUIDE_v1.md` | 1–284 in a separate full read after repairing truncated combined output |
| `DEPENDENCY_NOTATION_v1.md` | 1–98 |
| `DEPENDENCY_MANIFEST_v1.json` | 1–44 |
| `REVIEW_MANIFEST_v2.json` | 1–42 |
| `verify_reference_certificate.py` | 1–58; reread and independently executed |

An initial combined output containing both guides reported truncation
(`original token count 13628`). Both guides were then read separately in full;
their later outputs were not truncated. The scientific line-range reads listed
above were kept below the output cap. Searches were limited to the assigned
frozen files. Guide links were not followed, and the live source documents were
not opened to fill any gap.

## Fingerprint evidence retained

The initial check computed SHA-256 and line counts for all eleven frozen inputs,
checked the ten supplied manifest fingerprints, and separately fingerprinted
the review manifest itself. A closing check after the full line-range reading
and deterministic scope checks found exactly the same hashes and line counts.
The machine-readable records are `hashes_start.json` and `hashes_end.json` in
the assigned scratch directory. The review-manifest hash is observational;
there is no manifest assertion of its own hash.

| Input | SHA-256 at initial and closing checks |
| --- | --- |
| `REVIEW_ASSIGNMENT_v2.md` | `4a465aed1717390f9cfe82d29e1258323697a98bbf2c549517d72a42aee736e9` |
| `CANONICAL_ADDITION_v2.md` | `c70839b89be14f59800016dd250fbacf0f2f29c61978c68f85170316f3205396` |
| `PROPOSED_EDITS_v2.json` | `633f389bc7cb9cf5edc549e2d657f073a443c727aba1acb3ed5aed3a76bbfff6` |
| `PROPOSED_GUIDE_v1.md` | `d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5` |
| `DEPENDENCIES_GLOBAL_v1.md` | `6ebdaf1a3b28bdd07244a7b8c1bb882a36c7c525c4170cd25af4d7661ab7d942` |
| `DEPENDENCIES_GAUSSIAN_v1.md` | `c95e358f6bb9741858e6293dabacf4fee01927a23cda1289cd3cd17e85a1ee77` |
| `DEPENDENCY_GUIDE_v1.md` | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| `DEPENDENCY_NOTATION_v1.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `DEPENDENCY_MANIFEST_v1.json` | `75f8b2ae6716fb88d8f89306b78a104a2bffc62e1bf67bb64474b8298d5b415a` |
| `verify_reference_certificate.py` | `07c51c139ebf66912ef7b730201dcc71581b11355dd29dbee6140bf2bba63118` |
| `REVIEW_MANIFEST_v2.json` | `0548103a4af767f61e5911afebe7640807f2d92392d37b915c6205b4a985780c` |

The closing command asserted equality of the entire initial/end dictionaries,
then asserted agreement with every non-null expected hash. Its output was:

```text
All eleven frozen inputs unchanged; all ten manifest-supplied fingerprints match.
```

## Deterministic certificate and scope checks actually completed

The exact certificate was executed once as an independent subprocess, with
stdout, stderr, environment and exit status saved in `certificate_run.json`.

```text
Command: /usr/bin/python studies/nonlinear_prediction_selection/verify_reference_certificate.py
Working directory: /home/amir/Codes/PDE
Python: 3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]
Platform: Linux-5.15.0-151-generic-x86_64-with-glibc2.35
Elapsed seconds: 3.2514476776123047
Exit status: 0
stdout: [0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]
stderr: <empty>
```

The printed decimal values are only presentation. All assertions in the
verifier use exact `Fraction` arithmetic. The checked code constructs lower
and upper exponential-series bounds, alternating arctangent bounds for the
Machin expression for pi, rational Gaussian-density bounds, a Gaussian-tail
allowance, and outward-rounded interval sums. The relevant assertions all
succeeded. A separate deterministic string comparison verified that the
entire verifier body after its two provenance comment lines occurs exactly in
the frozen global dependency.

The scope-check script also verified that the proposed `replace_once.old`
string occurs once in the frozen global dependency, that the append target is
`CANONICAL_ADDITION_v2.md`, and that the guide replacement is
`PROPOSED_GUIDE_v1.md`. It retained the declared unchanged paths
`docs/NOTATION.md` and `code/`. A unified diff between the two frozen guides was
saved as `guide_scope.diff`; the structured checks are in `scope_checks.json`.
That diff adds C.4.9 descriptions in the global nonlinear learning entry and
the later scope paragraph. It leaves the surrounding established descriptions
in place. These checks did not inspect or mutate the live destinations.

## Mathematical checks and provisional observations already made

These notes preserve actual attacks and reasoning from the interrupted review.
They are not component acceptance verdicts. No counterexample or required
correction had been established when the coordinator stopped the review; that
statement does not establish correctness or completeness.

### Model, scaling, and unchanged dependencies

The review compared the stated two-hidden-layer tanh architecture, first-row
covariance, middle variance, readout variance, mobilities, and unhalved mean
square with the raw gradient formulas. With normalized row/readout inner
products and ordinary Frobenius middle norm, mobilities `(n,1,n)` give the
displayed population gradient blocks. The middle rank action is
`delta tensor H1`, corresponding to `delta h1^T/n` at finite width. The
population readout is zero initially as a limit of the actual variance
`1/n^2` finite readout; it is not an authorized finite reset.

The included Gaussian-action material was examined for adaptive reuse,
singular-query treatment, finite unions, true adjunction, and scalar
differentiability. The relevant unchanged inputs are III.F.1–III.F.10 and the
finite observation/approximation portions of III.F.11, together with the
global excerpt's A.1–A.4 extensions. In particular, the scalar Taylor argument
truncates the fixed incoming backward weight before controlling its tail; it
does not require an `L2 -> L2` Frechet derivative of every activation map.
Only learned action increments are Hilbert–Schmidt. The initialized action
remains the bounded generated action and its actual adjoint.

The reference dependencies checked included the two-coordinate feature clock,
its global continuation, the reference symmetries, the rational lower bound
for the reference feature energy, the endpoint speed integral, and the
whole-circle input bound in C.4.5. The C.4.6 S40–S44 source envelope was also
read through its finite cavity/probe and passage-to-limit construction. The
long C.4.7 material was read as supplied, but its physical-time-40 nonlinear
theorem was not treated as a theorem for arbitrary `1/epsilon` horizons.
Unrelated guide claims, response corollaries, and raw-GD statements were
context rather than new obligations inferred for this candidate.

### Controlled-source transport and raw-to-clock anchor

The review attacked the possibility that bounded raw norms were being used as
query-tail estimates. Unit A instead writes each reverse query as a Gaussian
source plus a bounded deterministic-coefficient combination of bounded first
features. Obtaining the coefficient cap is the important additional step.

The control comparison uses the sum of the two programs' absolute source
masses, with normalized discrepancy
`|gamma_p - bar_gamma_p| / (|gamma_p| + |bar_gamma_p|)` when that denominator
is nonzero. It therefore does not divide by a vanishing reference control.
Zero common mass is omitted, and one-sided new controls contribute their
mass to the discrepancy. The full old source list is retained. Current
passive slots are differentiated as named slots even if their values are
duplicated or have zero variance.

The source-difference Gaussian isometry uses a joint finite-union program and
the difference of uncentered input Gram covariances. It is not a Lipschitz
bound for a covariance square root. The latter is used only for continuity
at a fixed finite graph in the clipping/forcing argument.

The reference anchor was examined in the order stated in A.4 and its
supplement: fixed graph and nonzero independent Gaussian answer forcing,
width limit, zero-forcing coefficient continuity, and only then mesh
refinement. The clock's state comparison has bounded readout and bounded
clock feature derivatives, giving a uniform finite-length amplification
bound. Source extraction uses integration by parts in the fresh root with
all selected deterministic coefficients frozen. It does not infer a
transverse derivative merely from an unforced value law.

For the raw-to-clock defect, the review checked the cancellation in
`F(w + h b phi'(w)) - F(w) - h b`. The quoted differentiated defect involves
`h^2 exp(2 h |b|) (1 + h |b|)` times the named derivatives, rather than an
uncontrolled `exp(|w|)` factor after normalization. The direct source
injection costs `O(h_s)` after division by its mass; subsequent defects sum
using `sum h_k^2 <= L_* h_max`. The transformed pulse comparison uses bounded
clock gates and deterministic reference clock-pulse envelopes.

The temporary-cap moment argument uses the exponential moment of the
mass-weighted sum of absolute queries. Jensen's inequality here requires no
independence among old queries. The source comparison was checked for
unjustified maxima and moment products: its forcing uses at most three
`L12` factors followed by an `L4` amplification factor. Inside old-gate sums,
deterministic coefficient summation occurs after a norm bound rather than
after a random maximum over source history. The upper derivative subtraction
retains the current direct impulse cancellation and bounds old rows using
coefficient density. The proposed first-failure closure depends only on
previous query rows when constructing the current alpha, then beta.

These were substantial checks already performed, but the interrupted record
does not replace a completed verification of the entire source lemma.

### Endpoint conditioning and uniform parameter family

The proposed endpoint proof was tested against dependence between the first
Gaussian roots and the reference source envelope. The argument does not need
independence: a root box around `r v` has a Gaussian lower probability of
order `exp(-C r^2)`, while the envelope event exceeding `r^2` has an upper
probability of order `exp(-c r^4)`. Subtracting the latter from the former
gives a nonempty protected event for sufficiently large `r`.

On that event the bound on the clock increment and the growth of `F'` keep
the final row close to its initial ray. A supposed linear dependence of a
finite list of first features then gives a linear dependence of the
corresponding sign patterns. Crossing one perpendicular line at a time
eliminates each coefficient when the directions are distinct and not
antipodal. The specified added directions satisfy that condition throughout
the parameter rectangle.

For middle gradients, first-feature Gram positivity can be applied pointwise
to the upper backward coefficients and then integrated on the upper carrier.
Each upper backward field is nonzero since the endpoint readout is nonzero
and `sech^2` is strictly positive at finite preactivations. This is sufficient
for positive definiteness; independence of upper fields is unnecessary.
Compactness and input continuity then supply a uniform positive minimum.
The rectangle has a nonempty open interior in location and label, and is
bounded away from axis/antipodal degeneracies. No numerical lower bound for
this minimum was supplied by the rational certificate or assumed in this
check.

### Constrained equation and original-mixture continuation

The projected field uses the full moving raw gradients and the actual Gram
inverse. The review checked that its coefficients are functions of the
current state, retained initialized action and fixed added atom, rather than
an unknown changed-law trajectory.

The construction appends projected Euler segments to increasingly long
reference prefixes on the common carrier. The integrated-control tube counts
the omitted reference suffix as part of the discrepancy. Choosing the short
segment and prefix error first gives admissible finite programs before
invoking their source tails. One-reference cutoff estimates produce an
Osgood modulus of the form `z sqrt(log(e/z))`; its reciprocal has divergent
integral at zero. This is the mechanism used for Cauchy completion and
uniqueness, rather than an assumed ambient locally Lipschitz raw field.

The actual-mixture existence argument was checked for assuming the
trajectory it is meant to construct. It first treats finite Euler prefixes
from the original initialization, compares them to the existing reference,
and then applies a stopped post-prefix Euler estimate. The residual
one-step remainder is controlled by `h^2 (|r_k| + epsilon)^2`; absorbing this
into the contraction yields a bound on `sum h |r_k|`. Thus the displayed
continuation does not simply accumulate an uncontrolled `O(h T)` defect over
`T = tau_0/epsilon`. Full-history control discrepancy includes both the
reference suffix and the actual post-prefix control mass. No pretraining or
restart is imposed on the actual mixture optimizer.

### Strong derivatives and slow-time identity

The review examined the extra product needed to differentiate the anchor
gradients along reached curves. Their row derivative contains
`(w' dot v) Q(v)`. The source-tail bounds give both factors in `L4`, so
Hölder places their product in `L2`. Bounded readout handles its product with
the upper preactivation derivative, and the other blocks use bounded gates
and rank-one identities. Coordinatewise absolute continuity and integrable
norm bounds supply the strong integral identities. An ambient raw Hessian
was not used for this step.

The derivative of `B = G M^{-1}` then follows from finite-matrix absolute
continuity and the uniform Gram gap. Substitution of the exact anchor
residual equation into the original mixture field gives
`theta' = epsilon V + B r'`. The integration-by-parts error contains
`integral B' r`, whose bound has the terms
`|r_b|^2 + epsilon |r_b| + epsilon^2 (t-b)`.

The proposed limit takes small epsilon at a fixed large reference prefix,
then sends that prefix to infinity. Conversion from `b + tau/epsilon` to
the original time `tau/epsilon` costs the slow shift `epsilon b`. The stated
uniform slow limit excludes zero by using `tau >= tau_- > 0`; that exclusion
is required by the genuine initial layer. The review did not replace this
argument by a fixed-time first-order response expansion.

### Added-risk and paired upper-hidden margins

The review checked that the risk in the theorem is the risk of the added
component without its mixture weight. Along the constrained path its exact
derivative is `-4 r^2 ||Pi g_added||^2`. The negative endpoint residual,
Gram conditioning and a uniform short-interval bound are used to retain a
strict improvement over a finite episode.

The hidden-activity argument uses a scalar contrast of the three actual
upper hidden feature fields paired with the fixed endpoint readout. Its
initial derivative is proportional to the squared hidden part of the
projected gradient. The local derivative modulus retains its sign for a
uniform interval. Cauchy–Schwarz then bounds its change by the actual
same-carrier upper-feature displacement, with the factor of three matching
the stated average. This checks a representation change rather than only a
hidden parameter velocity. The observation compares the selected episode
with the fitted reference endpoint, not with the initial untrained state.

### Finite-width bridge and scope

The finite bridge was checked at a separately fixed positive epsilon, for
which `T_epsilon` is finite. The original finite gradient flow has energy and
norm bounds on that interval. The comparison proxy uses frozen population
controls with the actual finite arrays, including the finite readout. Its
fixed-program limits are taken before refining the mesh. The one-reference
cutoff comparison requires query tails only for that proxy; it does not
assume tails for the unknown actual finite trajectory.

The actual readout maximum estimate has the Gaussian union bound
`2 n exp(-n^2 eta^2/2)` at threshold eta. The small readout is carried through
the fixed-program comparison rather than reset. Time/input nets use the full
first-row norm, so the prediction statement concerns the entire circle.
Paired hidden observations use a finite union of reference and mixture
programs with the same arrays. At fixed epsilon both runs are captured at
their finite time; the population reference endpoint is taken only in the
subsequent epsilon limit. No finite-width endpoint theorem or simultaneous
width/epsilon rate was identified as an implicit premise in these checks.

The exact scope edits describe a finite nonlinear episode, whole-circle
prediction, added-component improvement, paired second-hidden adaptation,
and width-first finite-GF capture. Their new text does not state a final
changed-law endpoint, raw-GD theorem, or out-of-sample guarantee. Equation
labels are declared local to proof units. The potentially ambiguous references
to source/clock and scalar-gradient material were read in their included
contexts; no broken reference had been established as a required correction
before interruption.

## Incomplete status and remaining limitation

No component receives a final PASS or FAIL in this record. No final acceptance
verdict was reached. The reviewer had completed the recorded line-range reads,
the exact certificate execution, the deterministic scope comparison and the
listed mathematical attacks, but had not completed the original full review
report and final adversarial assessment when instructed to stop.

No unresolved objection had been formulated as a definite failed implication
at that point. This is a report of the review's state, not a claim that no
objection exists. The obsolete packet must not be accepted on the basis of
this incomplete record. The coordinator stated that a separate fresh reviewer
would review the complete final packet; this reviewer did not inspect that
packet or its preparation.

The preserved evidence files are:

- `data/generated/nonlinear_prediction_selection/adversarial_a_v2/hashes_start.json`
- `data/generated/nonlinear_prediction_selection/adversarial_a_v2/hashes_end.json`
- `data/generated/nonlinear_prediction_selection/adversarial_a_v2/certificate_run.json`
- `data/generated/nonlinear_prediction_selection/adversarial_a_v2/scope_checks.json`
- `data/generated/nonlinear_prediction_selection/adversarial_a_v2/guide_scope.diff`

**Final recorded disposition: coordinator-stopped obsolete-packet review;
incomplete; no acceptance verdict.**
