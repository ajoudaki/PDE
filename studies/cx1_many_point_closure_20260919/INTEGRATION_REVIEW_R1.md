# C-X1 independent integration and reproduction review R1

Date: 2026-09-19. Scope: the supervisor-assigned integration and bounded
reproduction review of the frozen candidate, not mathematical acceptance or
book promotion.

**Verdict: PASS for the prescribed operational reproduction and the reviewed
source/interface correspondence, with minor provenance and presentation
findings below.** All five configurations were executed once. All reported
losses, paired RMS values and passive predictions match `operational_02`
bit for bit; all five midpoint checkpoint files and all five observation
archives have identical SHA256 hashes. No blocking integration discrepancy
was found in the reviewed execution path. This verdict does not validate the
candidate's source estimates, strong completion, neural-width limit,
dictionary-order convergence or final mathematical theorem.

## Independence, frozen inputs and actual coverage

I read `REVIEW_ASSIGNMENT_R1.md`, `REVIEW_INPUTS_R1.json`, the subsequently
authorized `REVIEW_DEPENDENCY_SUPPLEMENT_R1.json`, and the required
`solve-math-rigorously` and `investigate-conjectures` skills, including the
research-contract, adversarial-audit and decisive-experiments references.
I did not read the study README/history, prior or concurrent scientific
reviews, other studies, Git history or task discussions. The narrower
integration assignment controls the verdict; this is not a second complete
scientific acceptance review under the packet's broader neutral assignment.

Complete candidate coverage: `THEOREM.md`, `REFERENCE_PROOF.md`,
`PERTURBATION_PROOF.md`, `FINITE_CAPTURE_PROOF.md`, `CX1_CLOSURE_PROOF.md`,
`ASSEMBLY_PROOF.md`, `cx1_closure.py`, `test_cx1_closure.py`,
`check_reference_constants.py`, `validate_trajectories.py`,
`VALIDATION_PLAN.md`, and `VALIDATION.md`.

Complete directly imported observable-module coverage:
`observable_arithmetic.py`, `observable_fixed.py`, `observable_words.py`,
`observable_compiler.py`, `observable_initialization.py`, and
`observable_solver.py`. The first-order/Torch/comparator and older closure
modules listed in the manifest were hashed but were not reviewed in full;
the candidate does not call their numerical initializers or evolution code.
After explicit authorization of the dependency supplement, I also read
`code/pde/__init__.py`, `finite_network.py`, and `gaussian_moments.py` in full.
These close the executed project-module import tree. Package import creates
definitions and activation descriptors; it performs no neural initialization,
training, archived-array read or moment computation.

Maintained mathematical/API coverage actually read: complete `docs/NOTATION.md`;
complete `special_data_limits.md` III.F.1--11; complete
`global_nonlinear.md` A.1--A.4, C.4.7.8 section 3, and C.4.7.10 C.1--C.6;
the B.1 model/hypothesis/interface excerpt at lines 1903--2075; and the
`code/README.md` model/normalization and complete finite observable closure,
numerical closure, observation, restart, precision and validation guide
sections at lines 626--940. Other maintained mathematical dependencies were
not audited completely. In particular, this report does not certify their
proofs or use a two-dimensional theorem as acceptance of the new general-d
claims.

Every file in the 30-entry frozen manifest matched before review and again
after the source and reproduction work. The manifest itself was unchanged:

`55a69888bfd1a234d01d44012cc33c6820ef9b54636aa459c7c0aa151fe38051`.

The full per-file records are `input_hashes_before.json` and
`input_hashes_after.json` in
`data/generated/cx1_many_point_closure_20260919/integration_r1_operational/`.
No input, maintained file or Git state was edited. The three supplementary
files were hash-verified on admission and again at completion, as recorded in
`supplement_hashes_admission.json` and `supplement_hashes_after.json`.
The supplement was supplied after the operational execution, so its checks
are not represented as an independent pre-run snapshot.

## Theorem/proof interfaces

The six candidate units specify a compatible model: separately fixed
`1 <= m <= d`, binary labels and equal training weights for the assembled
theorem, normalized directions `u`, physical inputs `sqrt(d) u`, independent
stored variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, and unhalved mean
squared loss. The full `d`-coordinate first row is retained. Only the learned
middle increment is Hilbert--Schmidt; the initialized action is bounded and
uses its actual adjoint. The Hilbert square-sum norm used for gradient energy
and the equivalent sum distance used for comparisons are distinguished.
The perturbation unit's loose action bound ten and the reference/closure
bound two are compatible with the same initialized carrier.

The dependency interfaces are explicit and do not require numerical runs:

| Unit | Supplied interface | Consumer |
| --- | --- | --- |
| Reference | Orthogonal reference, `T=5m`, strict risk, fixed activity time and both-layer motion/nonaffinity constants | Assembly |
| Perturbation | Raw-Euler construction, uniform query-tail cap, strong flow and configuration continuity on a fixed radius | Finite capture and closure Input C |
| Finite capture | Actual random-readout finite GF and simultaneous raw-GD interpretation; fixed-program probability order | Perturbation section 8 and theorem |
| Closure | Conditional construction using strong target flow and target query tails; separate numerical and dictionary limits | Assembly |
| Assembly | A smaller explicit positive radius preserving all strict margins | Final theorem |

The reference's stronger sufficient GD condition `eta_n sqrt(n) -> 0` is
not silently substituted for the assembled `eta_n -> 0`: the latter is
assigned to the distinct fixed-proxy argument in `FINITE_CAPTURE_PROOF.md`
sections 3--4, imported explicitly in perturbation section 8. The source
coefficient bootstraps, fresh-root extraction, completeness and this stronger
GD theorem remain mathematical review obligations; operational Heun runs
provide no evidence for them.

The closure theorem permits more general fixed finite data under Input C;
that is not an enlargement of the assembled learning theorem. The latter
keeps equal weights, binary labels, its proved-radius condition, and fixed
`m,d`. The `m=d=1` discrete-sphere exception and the requirement `m>=2` for
a genuinely correlated family are stated. The nonorthogonal operational
example is explicitly outside any assertion of certified membership in the
unevaluated radius.

The numerical order agrees across theorem, closure proof and maintained
arithmetic interfaces: precision, time mesh, optional coordinate
representation, population quadrature, initialization quadrature, positive
source regularization, and finally dictionary order. The optional data limit
is omitted for exactly represented data. No joint width/order limit, order
rate, automatic tolerance selector or finite-resolution accuracy certificate
is inferred.

## Source/implementation correspondence and information use

`cx1_closure.py:88--171` implements the stated total-degree/descending-lexical
polynomial core and retains every bounded valid prefix code through the
order, including duplicate outputs. The iterative exponent generator has no
recursive dimension ceiling. The code prefix is exhaustive as order grows;
the tested orders alone do not demonstrate density. At `d=3`, orders one and
three produce feature dimensions `(8,5)` and `(85,21)` as recorded, including
the duplicate constants. The finite resource guards reject requests without
changing their specified order.

`DimensionCompiler` changes the first-population Gaussian seed dimension and
offset to `d`, while retaining the maintained structural union and frozen
named-source differentiation. `initialize` always uses this generic compiler;
it does not replace order one with the separate maintained p=1 initializer.
It appends both action orientations, computes coefficients/Grams at `Q`,
replays the complete joint marks at `P`, normalizes with the specified ridge,
and stores a single forward matrix `D`. Positive source pivots are retained;
an unresolved pivot raises an error. The finite positive regularizer is
identified as an approximation, not exact singular-source handling.

The displayed closure equations (12) agree with the maintained `_fields`
and `rhs`: the data probabilities supply `1/m`, the three velocity blocks
have the factor `-2`, and the reverse contraction uses the same `M.T` with
the opposite population weights. The dimension-specific subclasses supply
validation and stage-state construction to the inherited integrator.
`evolve` is simultaneous explicit Heun for the finite closure ODE. It is not
the actual raw neural optimizer, and none of the five runs constructs a
finite neural network.

The saved arrays are exactly `b1,g,w,p1,b2,c,p2,M,D`, plus finite data and
arithmetic metadata. Moving `w,c` are population-node characteristic values,
and `M` indexes observable features. The compiled source program is local to
initialization and is not in the returned state. No clock, past velocity,
growing transcript or target trajectory appears in the state. The reviewed
initializer/RHS paths have no file reads or fitted coefficients. Their only
candidate file read is the explicitly requested checkpoint loader. The
static import/file-operation inventory is saved as
`static_import_io_audit.json`, including the subsequently authorized package
initializer and its two eagerly imported modules. There is no project-level
archive or trajectory read hidden in those imports.

Paired observations reconstruct the initial lower field from the retained
`g` and initial upper field from `g,D` on those same population marks.
They therefore preserve initialized/current coupling. Restart preserves
working floats in hexadecimal form and calls no initializer. The reproduced
restart checks compare all nine saved arrays after continuation.

For equal population size `P`, the proof's scalar count
`P(k1+2d+1)+P(k2+2)+2k1*k2` yields exactly the reproduced float64 array
byte counts `11904`, `87440`, and `146320`. Metadata and data are accounted
separately, and process peak memory is distinct. The reviewed initializer,
RHS and fixed-stage implementation match the stated fixed-order storage and
classical dense-work forms. This source check does not establish a useful
cost-to-accuracy relation or independently certify all asymptotic bit bounds.

## Bounded reproduction and independent comparison

Decision rule: execute only the five predeclared configurations once, retain
all results, and require the plan's finite-state, unchanged-shape and bitwise
own-state-restart gates. Independently compare all recorded numerical losses,
paired RMS values and passive predictions against `operational_02` by their
binary64 representations. Differences in time or resource measurements are
not failures. No accuracy threshold or follow-up sweep was introduced.

Command, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=code \
python -B studies/cx1_many_point_closure_20260919/validate_trajectories.py \
  --output data/generated/cx1_many_point_closure_20260919/integration_r1_operational
```

The driver enforced a 360-second alarm and 512-MiB address-space cap in one
process. Python was 3.10.12, NumPy 1.26.4, Linux x86_64; all three numerical
thread variables were one. The five configurations completed in 15.9941
seconds total, with maximum recorded resident peak 41,588 KiB. There was no
failed launch or trajectory rerun. Each configuration contains its prescribed
direct and restarted second half. The output directory was fresh when the
driver launched.

| Configuration | Final loss | Layer 1 RMS | Layer 2 RMS | Array bytes |
| --- | ---: | ---: | ---: | ---: |
| reference_o1 | 1.9462130137628105e-6 | 0.30216212508208007 | 0.3645336208855828 | 11,904 |
| reference_o3 | 1.5697638387230484e-6 | 0.27673104499026546 | 0.47192812819291935 | 87,440 |
| reference_o3_time | 1.5697998332438315e-6 | 0.27673153861857636 | 0.47192897333129075 | 87,440 |
| reference_o3_integration | 2.4174070968028094e-8 | 0.3166192238389536 | 0.5006690220292088 | 146,320 |
| perturbed_o3 | 7.047905067274504e-7 | 0.2790705494369338 | 0.4845592920567913 | 87,440 |

All five have finite states/predictions, unchanged shapes and bitwise exact
own-state restart. Initial/midpoint/final losses, both RMS values, all eight
passive predictions, metadata and retained byte counts match the baseline.
The baseline's ten recorded output hashes were verified independently before
comparison. All ten reproduced files have those same hashes. Source and
configuration records also match. The full comparison and hashes are in
`independent_comparison.json`; the driver's complete outputs are in
`record.json` and its named checkpoints/archives.

The maximum eight-probe difference from `reference_o3` is
`1.8238870613807023e-7` for time refinement, but
`0.06096994978466419` for integration/population refinement. These are
descriptive finite-rule differences, not error bounds. They do not certify
whole-sphere accuracy, canonical loss/motion margins, the neighborhood radius
or convergence with dictionary order.

The permitted `closure/deterministic_v4/results.json` reports seven passing
semantic tests with hashes matching the frozen test and module; the complete
test source was inspected. The permitted exact-rational certificate record
also matches its frozen source and reports success. These suites were not
rerun because the assignment excludes redundant checking absent a concern.
They are existing evidence, distinct from the five fresh runs above.

## Findings, severity and unresolved limits

1. **Minor: incomplete standalone run-source fingerprint.**
   `validate_trajectories.py:37--40` fingerprints a hand-selected list that
   omits directly/transitively imported `observable_words.py` and
   `observable_initialization.py`, although both are frozen by the separate
   review manifest and verified here. It also omits the Python package
   initializer. That means a bare operational `record.json` is not a complete
   transitive source certificate. Include the executed maintained dependency
   closure in future operational records. This omission did not cause a
   numerical mismatch in the present frozen comparison.

2. **Resolved missing-input issue; pre-run provenance limit retained.**
   The original manifest omitted `code/pde/__init__.py` and its eager imports
   `finite_network.py` and `gaussian_moments.py`. These were subsequently
   frozen and authorized by `REVIEW_DEPENDENCY_SUPPLEMENT_R1.json`, then read
   completely and hash-verified. They contain no hidden archive loading or
   import-time training. The code-coverage question is resolved. Their hashes
   were not independently captured before this review's five-run execution,
   which remains a limited historical-provenance caveat; the original 30-file
   before/after comparison is unaffected.

3. **Minor: normalized versus physical prediction notation.**
   `THEOREM.md:14` writes `f_n(u)`, whereas reference equation (1.1) and
   finite-capture equation (F13) write `f_n(sqrt(d)u)` for the same displayed
   forward computation. All input equations and the implementation clearly
   consume normalized `u`; the physical convention is recoverable. Add one
   explicit identification of the two notations to avoid interpreting F13
   as passing a nonunit vector to the closure API. No model change is needed.

4. **Minor: stale semantic-test count.** `VALIDATION_PLAN.md:31` says six
   semantic tests; the frozen suite and final permitted record have seven,
   including the exponent-enumeration regression. `VALIDATION.md` already
   explains the seventh. Update the plan's cross-reference when issuing a
   later version; the five operational configurations are unaffected.

There are no remaining failures of the assigned five-run gates. Mathematical
acceptance of the complete candidate, high-order practical feasibility and
finite-resolution accuracy
remain outside this PASS. No source correction, extra simulation, full neural
training, precision sweep or promotion action was performed.
