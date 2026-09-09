# Incorporation acceptance and exact scope

This is a progressive record after checkpoint `a257e59`, not a blanket audit
of every historical source. The starting library inventory is preserved in
`reviews/INCORPORATION_BASE_LIBRARY_INPUTS.json`. The final integrated edition
is listed in `LIBRARY_INPUTS.json`; its separate final integration check and
navigation receipt follow the scoped package records below.

## First accepted package: correlated-data partial results

The complete Part IV proof is identical to
`FIRST_LAYER_COMPACTNESS_ADDITION.md`, SHA-256
`02500ea3eee80f9dadd36790a5ccaea6258c06d0c6901564b54417624452ef93`.
The source was the fully read 1,623-line
`ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md` in the recovered
`l2-two-sample-proof-0ywjpp` directory, source SHA-256
`910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9`.
The assembly translates its first weights to the shared normalization,
preserving the actual raw GF/GD and mean-versus-sum clock distinction.

The original assembly's two isolated reviews required eight Gram-symbol
repairs and one continuity-codomain repair. They remain preserved without
relabeling in `reviews/FIRST_LAYER_ROUND1_A.md` and
`reviews/FIRST_LAYER_ROUND1_B.md`. Two fresh reviewers, seeing only the
corrected complete proof and notation, returned CLEAN at the exact current
hash: `reviews/FIRST_LAYER_ROUND2_A.md` and
`reviews/FIRST_LAYER_ROUND2_B.md`.

The complete Sections 10–11 proof is identical to
`MIXED_FITTING_ADDITION.md`, SHA-256
`36a50c2aa599302db2b2942d0ddb21d5561488ac0eff5e4b34dd7e43e3717a78`.
Its fully read sources in the same recovered directory are:

| Source | SHA-256 |
|---|---|
| `COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md` | `cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b` |
| `COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES.md` | `dcaaea01fe2f22b8848da127eed58fbcf29bc8fe9fba516ebcaa0dde70abac20` |

The historical permanent-gate review was also read fully, but not used as a
mathematical premise. The new assembly contains its proofs with the shared
first-weight normalization, explicit sufficient constants, all Gaussian
event estimates and the necessary extra strip event. Two fresh isolated
complete-proof reviewers returned CLEAN with no corrections:
`reviews/MIXED_FITTING_A.md`, `reviews/MIXED_FITTING_B.md`.

Both pairs read the exact proof and the complete notation contract only;
they did not see studies, prior verdicts or other agents. Their individual
reports give full read coverage and exact input hashes. The additions invoke
no unprovided specialized theorem. Ordinary finite-dimensional ODE facts,
elementary Gaussian identities and norm inequalities are used at the stated
hypotheses; the nontrivial compactness and clock arguments are contained.

The first result is strong first-layer compactness for actual arctangent
GF/GD, including kinetic and residual-weighted kernel conclusions along
strong subsequences. It is not a common full-sequence population flow.
The second is finite-GF fitting and finite parameter endpoints on explicit
events, plus gate mass on an augmented event; it is not a population/GD or
persistent-feature-velocity theorem. Introductory chapter and guide summaries
have been updated to keep these scopes distinct. The prior complete theorem
proofs are unchanged.

## Second accepted package: finite calculus and reusable implementation

The moving L2, one-sample, order-three physical-GF recurrence is fully contained
in `FINITE_JET_ADDITION.md`, SHA-256
`bb927e3f7a2dc75a222664a871b7caf247ebccd0fc1f31815434f6f2e3c26fb6`.
Two isolated reviewers read the entire proof, notation, numerical contract,
implementation, tests and complete local import dependencies. Both returned
CLEAN with no required corrections: `reviews/FINITE_JETS_A.md` and
`reviews/FINITE_JETS_B.md`. Their independent rational coordinate-differentiation
checks complement, rather than replace, the recurrence proof. The floating-point
range exclusions remain explicit, including intermediate overflow even when
an exact coefficient exists.

The forest factorization, key, reversion/determinant algorithms and quadratic
zero-first-mobility certificate are contained in `EXACT_CALCULUS_ADDITION.md`,
SHA-256 `1babf900769e75b6951d1579108e4e3159d1fd297589f5d580f7382d5f95b799`.
Both full isolated reviews are CLEAN with no required corrections:
`reviews/EXACT_CALCULUS_A.md` and `reviews/EXACT_CALCULUS_B.md`.
Their proof input also contained the complete Gaussian Section 4; all supplied
code, tests and import dependencies were fully read. Independent Riccati/formal
ODE coefficient derivations and independent inverse/determinant calculations
reproduced every displayed certificate coefficient. These checks do not supply
concentration or a positive-time identification claim, which are not asserted.

The book's Section 7 preserves both proof bodies except for heading levels and
the optional harmless superscript typo `^{,k}` changed to `^{k}` in (7.C3).
The original reviewed fragment is retained unchanged. This is an editorial
correction, not a new probability or arithmetic assertion. The code guide adds
API contracts, examples, limitations and the complete certificate command.

| Accepted implementation/test | SHA-256 |
|---|---|
| `code/pde/finite_jets.py` | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `code/tests/test_finite_jets.py` | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |
| `code/pde/exact_calculus.py` | `482a45deb3e5fb721acdd0ae97654f9f5db57da145e0902d9ff1b24f01c8fc41` |
| `code/tests/test_exact_calculus.py` | `b4a7f5795def064e53b2e7a849637d29dcaa0bad403e8e8ff893863b8468a439` |

`make check` passes all 73 small deterministic tests and the structural boundary
check. No training experiment, high-order campaign, data or figure was generated.
The code/API/reproduction integration review is also CLEAN, with the exact
read scope in `reviews/CODE_INCORPORATION_INTEGRATION.md`. It fully read all
in-scope code/tests and guide, complete finite dynamics, Gaussian Section 4,
and the entire new Section 7; it independently passed all 73 tests and all
four guide examples. It is not a whole-book mathematical review. The incidental
concurrent PDF-exporter files were excluded and never used as proof or tests.

## Third accepted package: quantitative fixed-program discretization

The complete 863-line addition, `QUANTITATIVE_ADDITION.md`, has SHA-256
`bc41e23b07917257ce5810018d3d6ab2937551ce079a44d6e936965061f0d46d`.
It is inserted unchanged as calculus Section 8. Two fresh isolated reviewers
read all 2,676 lines of the combined original calculus and addition, plus the
complete notation contract. Both returned PASS/CLEAN with no required
correction: `reviews/QUANTITATIVE_A.md`, `reviews/QUANTITATIVE_B.md`.
The common combined proof hash was
`acfee00f63de4f35023521fe5c9baef00d018dae3fe79186ea3d6147ea1e77ce`.
Section 7 was not an input or a dependency of that review; its independent
acceptance is recorded above. The final integration checks the chapter assembly.

The proof contains singular-covariance Price differentiation, explicit derivative
and syntax budgets, the exact compiler coefficient, fifth-order remainder,
and the full fixed-program expectation-identification dependency. It assumes
the stated C12 activation bounds and normalized Gaussian second moment,
one sample, order-one readout and feature-ascent updates. Depth and update
count are separately fixed. It supplies no growing-update or physical-loss-GF
limit. Conditioning constants in the fixed-program dependency refer to the
chosen activation and its actual Gram gaps; no class-uniform gap is accepted.
The new inverse-free remainder exponent is explicitly given in terms of its
own stated activation bound, not inferred from such a gap.

The full source and dependency read record is in
`source_audits/QUANTITATIVE_ASSEMBLY.md`; its historical audits are locators,
not mathematical premises. No compiler campaign or data generation was needed.

## Fourth accepted package: shallow, spectral and fixed-depth exact capture

The complete Sections 8–12 addition, `EXACT_CAPTURE_ADDITION.md`, has SHA-256
`b1b0de36b4e5ac66f51310e10af98aae4029e574c05202bf7826e36e17535f3d`.
Its source read/provenance record is `source_audits/EXACT_CAPTURE_ASSEMBLY.md`.
The coordinator read the complete assembly and canonicalized only editorial
framing before review. The first pair's reports are retained as
`reviews/EXACT_CAPTURE_A.md` and `reviews/EXACT_CAPTURE_ROUND1_B.md`.
The first was CLEAN; the second required explicit trace-class foundations
under the strict self-containment standard, rather than relying on their
classical status. That qualification was not waived or relabeled.

The added `TRACE_IDEAL_FOUNDATIONS.md`, SHA-256
`c056507eabe88fefa8cbe56f452f0e50a5f233423c3500de53d043abcfb902bb`,
is inserted completely as Section 2.A. It derives compact singular expansion,
approximation numbers, trace-norm completeness, finite-rank density, ideal
and trace operations, singular-Gram continuity and full nuclear-tail bounds.
Two fresh isolated reviewers read the complete amended 2,634-line chapter,
including every earlier internal dependency, and the complete notation
contract. Both returned CLEAN with no required correction:
`reviews/EXACT_CAPTURE_ROUND2_A.md` and
`reviews/EXACT_CAPTURE_ROUND2_B.md`. The common proof hash is
`c17c6adeb1c728e614b0b1e5d67706d9462223559182057134d56462e707d6ae`.
No study, earlier review, outside paper or other agent was supplied to them.

The whole proof bodies are inserted without mathematical alteration. Only
the chapter title and its introductory scope now describe the added material;
that editorial assembly has SHA-256
`c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090`.

The three additions are one-input, order-one-stored-readout physical-GF
theorems. The shallow theorem has marked nonlinear characteristics, all
finite-moment restarts, and uniform scalar/block-energy limits, not general
fitting or an empirical path-law theorem. The every-fixed-linear-depth theorem
has full endpoint/operator-increment state, fixed rooted readouts, trace-norm
increment limits and uniform nuclear tails, not arbitrary data or all-depth
fitting. The L2 spectral theorem has its explicit two-channel source, negative
atom and mass-two scalar representation, global canonical physical flow,
fitting and the stated scalar/block-energy limits. Its global restart scope
is along that initialized solution, not every ambient spectral state.

The Gaussian word/net, fixed-Picard-to-flow and spectral-measure proofs are
contained; sharp spectral-edge, asymptotic-freeness and spectral-inversion
theorems are not imported. Agreement on overlaps is proved at matching
observables. The existing L3 raw-GD theorem remains separate: none of the
new GF statements acquires a raw-GD, growing-depth or arbitrary-data extension.

## Fifth accepted package: initialization geometry and activation comparisons

The complete Part V is identical to `INITIALIZATION_ADDITION.md`, SHA-256
`411fbe15d0701451a0e4fad0b87bfc5a11d283e200b278d3b75872fb05fa8a27`.
Its 1,343 lines contain the finite-width initialization and raw-kernel bridge,
Hermite/Fourier foundations, cubic tensor floor, all three activation families,
the explicit limiting-depth ODE and error bound, and the closing comparisons.
The source read/provenance record is `source_audits/INITIALIZATION_ASSEMBLY.md`.
The donor's conditional trained-continuation portion is not incorporated.

The original draft and three unsuccessful paired review rounds are preserved
without relabeling in the source record and `reviews/INITIALIZATION_ROUND1_*`,
`INITIALIZATION_ROUND2_*`, and `INITIALIZATION_ROUND3_*`. Their findings led to
explicit signed negative-endpoint derivative sums, centered Gaussian and
off-diagonal hypotheses, valid derivative-index ranges, gain-comparison
assumptions, and the identity-scaling exception. The main bounds, witnesses,
numerical constants and conclusions did not change. The coordinator read the
complete assembly and the corrections, rather than accepting historical labels.

Two fresh isolated reviewers then read all 1,343 proof lines and all 98 notation
lines at the exact accepted hash, with no studies, earlier verdicts, external
source or other agent. Both returned CLEAN with no required corrections:
`reviews/INITIALIZATION_ROUND4_A.md` and
`reviews/INITIALIZATION_ROUND4_B.md`. Their complete argument, constant and
endpoint checks are retained. No numerical experiment was used.

The results distinguish three different observables: absolute initialized
sample conditioning, conditioning normalized by feature second moment, and
scalar affine-regression residual. Odd mixtures have the sharp joint
depth/mixture/separation orders and matching strict planar examples; normalized
conditioning can persist while absolute scale and newly introduced scalar
nonaffinity decay. Literal convex offsets can lose sample distinctions despite
positive absolute and relative scalar nonaffinity. The calibrated family has
an explicit sequential width-first/depth-second geometric limit, with a
depth-dependent activation and declining per-layer nonlinear amplitude.

Every finite-width assertion fixes the entire activation and depth first.
The calibrated outer depth limit is not a joint trained width/depth theorem.
No initialization result supplies trained Gaussian laws, incoming-tail control,
cap removal, persistent trained feature motion, or eventual fitting. The
chapter introduction and final scope, and the book's chapter table, retain
these distinctions. Their assembled hashes are recorded in the final inventory.

## Final assembled-edition acceptance

All five packages, comprising seven separately reviewed proof/code groups,
have their own paired clean complete reviews. A further fresh isolated
[assembled-book integration review](reviews/INCORPORATION_FINAL_INTEGRATION.md)
is CLEAN, with no required corrections. It received only the 25-file standalone
scientific library, never the studies, source histories, prior reviews, data,
or concurrent exporter. All 25 inputs remained unchanged during its audit.

That reviewer read 11,989 of the edition's 26,350 lines: eighteen files in full
and seven chapters at explicitly listed ranges. It read every requested new
addition, the guide, notation and implementation in full, and checked the
remaining chapter contracts at their actual model and observable scopes.
Its exact read and unread ranges, whole-file hashes and selected-passage hashes
are retained. It is not a second line-by-line certification of unread older
proofs; their earlier complete reviews remain separately identified.

The independent structural/link check passes on all 23 docs/code files, and
all 73 unit tests pass. `Makefile` and `requirements.txt` are the other two
inputs. The test suite directly regenerates the displayed rational certificate;
it does not implement or certify the general population compiler. The guide's
external contextual bibliography was not rechecked in this no-network review.

The coordinator checked all 25 repository files against the isolated edition
and its `LIBRARY_INPUTS.json`, including full proof-fragment preservation and
absence of truncation artifacts. The mechanical checks and scope are recorded
in `source_audits/INCORPORATION_ASSEMBLY.md`; final fingerprints and navigation
results are in `INCORPORATION_FINAL_CHECKS.json`.

The three agreed incorporation priorities are completed. The broader backlog
in `ADVISORY_COVERAGE_DISPOSITION.md` remains deliberate and separately scoped.
No new training experiment or historical high-order campaign was run; no
empirical dataset or figure was promoted. This acceptance neither resolves
the general uncut nonlinear population theorem nor asserts generalization.
The six concurrent PDF-exporter files from `eb6e628` are preserved but excluded
from this task's scientific-library inventory and acceptance.

## Continuation from ae43aa4: capped spaces and finite loss calculus

The checkpoint was verified in the same shared checkout. Eight inherited
modified review artifacts were left untouched; their credential-limited
metadata receipt is `CONTINUATION_START_STATE.json`. The previous 25-file
scientific edition is preserved byte-for-byte as
`reviews/CONTINUATION_BASE_LIBRARY_INPUTS.json`. The six PDF-exporter files
from `eb6e628` remain excluded and unchanged. Only the coordinator writes Git.

Finite-controls Section 12 contains the complete 417-line
`GIVEN_SPACE_CAPS_ADDITION.md`, SHA-256
`cdda914e481b46d51366a5d80661cd192b0f319d6507bc8b29eba69d87f9f95d`.
It proves global dissipative capped dynamics on specified separable L2/HS
spaces, then strong uncapped convergence, raw kernels and reached-state
restart conditional on uniform exponential square tails. The prescribed
bounded initial operator, three-input activation/clock, zero readout and
tail premise are explicit. It constructs no canonical Gaussian action and
identifies no finite-network GF/GD population limit.

Gaussian Section 9 contains the complete 366-line
`CALCULUS_PULLBACK_ADDITION.md`, SHA-256
`dccefe204d607ad778a09e9a2c98ced0fbcb50a75cba869c44df9d9f652108ea`.
It derives exact Euler pullback words, rational paired temporal weights, the
fixed-N integral remainder, an arbitrary-residual cubic full-loss identity,
and a separate convex-region comparison bound. New exact APIs are
`euler_pullback_words` and `paired_euler_weights`; they evaluate combinatorial
weights, not predictor derivatives or neural moments. Code/test hashes are
`d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3`
and `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242`.

The first paired complete reviews are retained unchanged as
`reviews/CONTINUATION_CAPS_PULLBACK_A1.md` (CLEAN) and
`reviews/CONTINUATION_CAPS_PULLBACK_B1.md` (CORRECTIONS REQUIRED). The latter
found that a smooth squared loss need not have a C3 predictor. The tensor
specialization now states that additional condition; it is not inferred from
loss regularity. Both fresh complete corrected-version reviews are CLEAN:
`reviews/CONTINUATION_CAPS_PULLBACK_A2.md` and
`reviews/CONTINUATION_CAPS_PULLBACK_B2.md`. Each read all eleven files and
2,501 lines, verified every input hash, passed all eleven supplied tests and
independent bounded algebra/metric checks. They received only complete
candidate material and explicit dependencies, never project histories or
prior verdicts. The unsuccessful version was not promoted.

Source proofs and correction reads are in
`source_audits/GIVEN_SPACE_CAPS_ASSEMBLY.md` and
`source_audits/CALCULUS_PULLBACK_ASSEMBLY.md`. No specialized external theorem
is used without a contained proof. Both reviewed proof fragments are inserted
byte-exactly; chapter introductions and guides describe their different scopes.
A standalone copy of the 25 scientific inputs, without studies/data/exporter,
passes `make check` and all 77 tests. The live six-module scientific allowlist
also passes 77 tests. The four added methods are finite deterministic checks;
no training, population simulation or historical campaign was run.

## Continuation: finite quadratic/RMS identities and formal-jet obstructions

The preceding caps/pullback package is committed at `f7801db`. This next
package adds finite-dynamics Sections 5–7 and Gaussian Section 10. Their
complete byte-exact proof fragments are:

| Fragment | Lines | SHA-256 |
|---|---:|---|
| `FINITE_IDENTITIES_ADDITION.md` | 434 | `5c422cb6bed3ce0816853cccd78d49a85f1fd3c8ca9718528584e15dc725427f` |
| `POSITIVE_METRIC_TAYLOR_ADDITION.md` | 496 | `bfe815697f0a7a6e090d3e48bcf72cdf357e2cc9fbeb837007ce636010b667b8` |

The finite section covers QI/IQ/QQ raw gradients and kernels, isometric Lax
identities and similarity, an orientation-sensitive spectrum insufficiency
witness, QQ balance laws, differentiated RMS gradients/features/normalizers,
signed balance drifts, a raw-image reduced-state lift, and global finite
physical GF. It is one input, one sample, two hidden layers, arbitrary finite
state/readout and label, canonical unit block mobilities, and full square loss.
No width or Gaussian population claim is attached. Both RMS normalizers are
differentiated; the source's epsilon-zero row-balance remark is corrected.

The formal section proves the complete normalized derivative-forest grammar
and fixed-order annealed Gaussian expectation limit. It derives continuity
of a finite negative Stieltjes witness, hence failure on some existential
interval of strictly positive first mobilities with beta=1. It supplies no
numerical endpoint, high-order positive-alpha table or unit-metric Stieltjes
verdict. At the canonical metric it separately derives factorial growth from
a nonnegative primitive-polynomial comparison and an explicit raw-square
frozen branch, then proves that the prescribed residual-clock Taylor losses
are not uniformly Cauchy on any interval containing initialization. No
concentration or actual positive-time network identification is inferred.

The complete source/correction read records are
`source_audits/FINITE_IDENTITIES_ASSEMBLY.md` and
`source_audits/POSITIVE_METRIC_TAYLOR_ASSEMBLY.md`. The questionable generic
detransposition import, matroid shortcut, two-hit charging upper bound and
historical high-order tables are not used. Every needed proof is contained.

Both isolated complete corrected-input reviews are CLEAN with no required
correction: `reviews/CONTINUATION_FINITE_TAYLOR_A2.md` and
`reviews/CONTINUATION_FINITE_TAYLOR_B2.md`. Each read all 15 supplied files
and 3,622 lines, passed all 20 supplied tests plus independent bounded
derivative/rational checks, and verified unchanged input hashes. The packet
includes the corrected complete loss-pullback dependency. Two earlier review
tasks were interrupted when that dependency changed; they supplied no accepted
verdict and are not counted as completed reviews. Their draft and final packet
manifests remain `CONTINUATION_B1_INPUTS.json` and `CONTINUATION_B2_INPUTS.json`.

The new `code/pde/finite_reductions.py` hash is
`b74b7da576e75749417dce2662e04c110f6028f09b724cfa1d295f1055c99225`;
its nine-test file hash is
`bd0063b5d7865cdb9f9b13e7bbea9118379a9baf2cb28845989ffbdd77935a9e`.
The entire 118-line API fragment has hash
`eb0a736a1419ff9c1e8011d6a2fd0c5d63a9b8be7d09f321010106ec6b9cf0de`
and is present unchanged in the code guide. The state evaluators use ordinary
float64 arithmetic and retain explicit intermediate overflow/underflow limits.
No time integrator or population solver is added.

A new 27-file standalone scientific library passes its boundary/link checks
and all 86 tests; both new guide examples run there. See
`reviews/CONTINUATION_FINITE_TAYLOR_STANDALONE.md` and its edition manifest.
No studies, data, prior verdicts or PDF exporter were supplied. The thirteen
new methods since the 73-test baseline check finite identities/combinatorics.
No new training experiment or historical coefficient campaign was run.

## Continuation: integrated queries and dense residual identities

The preceding finite-reduction/formal-jet package is committed at `b341572`.
Two further complete proof additions extend existing chapters:

| Fragment | Destination | Lines | SHA-256 |
|---|---|---:|---|
| `INTEGRATED_QUERIES_ADDITION.md` | Finite controls, Section 13 | 242 | `fbe02d7d7c85167242cca00393fdb01f62c2357e5d94900cc1b439157b93850e` |
| `DENSE_RESPONSE_ADDITION.md` | Continuous depth, Section 14 | 380 | `446c817b40cb7b32cf83a0fd1bdc3dd54461dbc7bf7b688eacdd9f5dbe9e0286` |

The integrated-query result treats a finite three-hidden-layer arctangent
network, one scalar input/sample, and its specified small-readout initialization
and feature-ascent clock. It derives both trained-matrix memories, the four
remaining initial matrix actions, their full derivative bounds, a time cover
independent of width for a supplied path under the stated bounds, and the
integration-by-parts memory estimates. The tail-stability, finite-transcript
causality and strong velocity/kernel identification requirements remain
explicitly unproved. The diagnostic counterexamples do not claim reachability.

The first full review `reviews/CONTINUATION_QUERIES_A1.md` required removal
of noncanonical finite RMS notation. The rejected candidate is retained as
`reviews/CONTINUATION_QUERIES_R1_CANDIDATE.md`. All normalization factors are
now explicit. Both fresh complete corrected-version reviews are CLEAN:
`reviews/CONTINUATION_QUERIES_A2.md` and
`reviews/CONTINUATION_QUERIES_B2.md`. Each read all three supplied documents
and 554 lines, including the complete finite-network dependency and notation,
and verified their unchanged hashes. Neither used numerical or training work.

The dense result uses a separately specified finite tanh residual network,
linear input map, arbitrary finite data, order-one stored readout, all trained
blocks, mobilities `(L,n,n)`, and full mean square loss. It proves raw gradients,
kernel positivity and dissipation, global finite physical GF, finite-horizon
state bounds, exact response recurrences, finite ordered-product grades,
factorial tails along a supplied trajectory, and separate source-recomputation
error bounds. No width/depth limit or autonomous compression theorem follows.
The chapter distinguishes these results from its scalar-particle Sections 1–13.

Both complete isolated dense reviews are CLEAN without a required correction:
`reviews/CONTINUATION_DENSE_A1.md` and
`reviews/CONTINUATION_DENSE_B1.md`. Each read all 478 lines of the two supplied
documents and verified unchanged input hashes. Independent single-state
derivative/algebra checks supplement the contained proofs. Reviewer A's own
diagnostic script was initially written in the temporary packet, then moved
outside it; no mathematical input changed. Reviewer B explicitly confirmed
that it never read or executed the extra script and confined mathematical
reads to the two manifest documents. No report or diagnostic was shared as
a mathematical review input.

The complete source/correction read records are
`source_audits/INTEGRATED_QUERIES_ASSEMBLY.md` and
`source_audits/DENSE_RESPONSE_ASSEMBLY.md`. No specialized external theorem
is imported by either proof. Both accepted fragments occur byte-exactly once
in their maintained destinations. These are proof additions, with no new
solver, empirical promotion or data product. The complete bounded disposition
of the remaining families is `CONTINUATION_DISPOSITION.md`; it retains actual
probability, tail, generator, semantics and identification gaps as such.

## Final continuation assembly acceptance

All six continuation packages have paired clean complete independent reviews
at the accepted bytes, with failed versions and their corrections retained.
The further isolated integration review is CLEAN with no required correction:
[CONTINUATION_FINAL_INTEGRATION.md](reviews/CONTINUATION_FINAL_INTEGRATION.md).
It received only the 27-file scientific library and its manifest, without
studies, data, prior verdicts, historical arrays or the unrelated exporter.
All 27 inputs and the manifest remained unchanged.

The reviewer read 9,283 of 29,482 scientific lines: twenty files in full and
seven chapters at explicitly recorded ranges. All new sections, their needed
Gaussian proof dependencies, the entire finite-dynamics chapter, guides,
notation, production code, tests and boundary checker were read in full.
The report records every complementary older body range not freshly reviewed.
This is a scoped integration acceptance, not a new whole-book certification.

The standalone boundary/local-link check passes on all 25 docs/code inputs;
`Makefile` and `requirements.txt` are the other two scientific inputs.
All 86 tests and both new guide examples pass under Python 3.10.12 and
NumPy 1.26.4. The unchanged logs are retained in
`reviews/CONTINUATION_FINAL_STANDALONE.md`. The exact final 27-file inventory,
totaling 1,338,187 bytes, is `LIBRARY_INPUTS.json`, also preserved as
`reviews/CONTINUATION_FINAL_LIBRARY_INPUTS.json`. The review's original input
manifest is `reviews/CONTINUATION_INTEGRATION_INPUTS.json`.

The coordinator verified all final scientific bytes against that isolated
snapshot, all six exact proof-fragment insertions, preservation of the prior
proof bodies and code definitions, and the six unchanged PDF-exporter hashes.
`CONTINUATION_FINAL_CHECKS.json` records the checks and their limits. The eight
inherited modified review artifacts remain untouched; their contents are
unreadable to this credential, so only metadata preservation is claimed.
The concurrently appearing `TASK_NAME_INDEX.md` remains untouched and unstaged.

The maintained book and implementation contain every dependency used by the
accepted additions. No empirical figure, generated array, historical campaign
or training result was promoted. Coverage and the promotion ledger now point
to the explicit remaining-family disposition; none of the listed unresolved
premises is silently treated as a theorem.

## Resumed assembly: sharp shallow discretization

The resumed work starts at `caf975a`; `ASSEMBLY2_START_STATE.json` records the inherited changes. The first further accepted addition is the complete 551-line `SHALLOW_DISCRETIZATION_ADDITION.md`, SHA-256 `4321fc6bf9fdddedccb752072f3326134d514edbdd576c328923432e4345efd9`, inserted exactly once as Gaussian-calculus Section 11. The previous proof body is unchanged. `source_audits/SHALLOW_DISCRETIZATION_ASSEMBLY.md` records complete source and correction reads.

Two fresh isolated complete reviews are CLEAN: `reviews/ASSEMBLY2_SHALLOW_A1.md` and `reviews/ASSEMBLY2_SHALLOW_B2.md`. Each received only the 551-line candidate, 98-line notation contract and hash manifest, with no studies, history or prior verdict. Both read every line, substantiated all derivative envelopes, expectation interchanges, constants, parity, cubic coefficient, sharp fifth-order scaling and restricted dyadic conclusion, and verified unchanged hashes. The initial B1 output is preserved unchanged as `reviews/ASSEMBLY2_SHALLOW_B1.md` but is **not accepted or counted**: its final artifact lacked a complete mathematical audit. B2 is a fresh full replacement, not a continuation of B1. No mathematical correction was required.

The theorem concerns one hidden layer, one input/sample, independent order-one Gaussian stored readouts, a normalized activation with bounded derivatives through order twelve and at most linear growth, and simultaneous feature-ascent Euler steps. It gives exact equality of finite-width expectations, the cubic discrepancy with a uniform `k^4 |h|^5` remainder on `k |h| <= 1/(16 M)`, and a short-interval uniform dyadic limit of terminal expected outputs. It does not supply physical loss GD, growing-program hidden-state convergence, arbitrary partitions, a restart state or an ODE identification.

`reviews/ASSEMBLY2_SHALLOW_R1_INPUTS.json` seals the complete proof inputs. `reviews/ASSEMBLY2_SHALLOW_LIBRARY_INPUTS.json` and the current `LIBRARY_INPUTS.json` identify the accepted scientific edition, assembled from the preceding baseline with only the Gaussian chapter replaced. The standalone dependency check passes on all 25 docs/code inputs; `Makefile` and `requirements.txt` complete the inventory. Other live additions remain under assembly until their own acceptance. No implementation or empirical result was added in this commit.

## Resumed assembly: frozen quadratic and ReLU calculus

The shallow addition is committed at `f4d6dfa`. The next accepted proof is the complete 613-line `SCOPED_OBSTRUCTIONS_ADDITION.md`, SHA-256 `45169438edc521dfe84e80c703a71233f810f3acb8aee314fcdebb44a96ecda1`, inserted exactly once as finite-dynamics Sections 8–9. All earlier proof text is preserved. The introduction now distinguishes the C2 theorem in Sections 1–4 from the separate ReLU solution convention.

The exact frozen reduction fixes an arbitrary bottom feature vector, trains connector/readout with mobilities one and n, and uses top activation z²/sqrt(3) and half-square loss. Its probabilistic initial-layer theorem additionally freezes Gaussian-square first features and uses independent order-one Gaussian stored readouts. It covers every deterministic positive step sequence tending to zero jointly with width, without a relative rate condition. The exact deletion counterexample does not transfer this theorem to the fully trained quadratic network.

The ReLU result gives a reached width-two positive-probability obstruction to the prescribed pointwise classical/absolutely-continuous field, separately for every real assigned kink slope. It does not exclude differential-inclusion selections. Beside it, the full three-block raw Euler model with kink slope of modulus at most sqrt(2) has tight scalar output/loss laws and continuous initialized subsequential limits on the explicit half-loss horizon `1/(384*6^4)`. Neither determinism, uniqueness, full-state/kernel convergence nor a larger horizon is inferred. Exact frozen-gate occupation and joint-phase identities preserve the missing product information.

The existing `finite_reductions.py` now contains `FrozenQuadraticEvaluation`, `_frozen_state`, `frozen_quadratic`, and `frozen_quadratic_step`. They evaluate a supplied finite state and one simultaneous raw half-loss step; no initializer, trajectory solver or experiment was added. Four meaningful test methods check raw derivatives, both kernel blocks, energy, raw interpolation, degeneracies, ownership and validation. The complete 42-line guide fragment occurs exactly once in the unchanged earlier guide.

Both first complete independent reports, `reviews/ASSEMBLY2_FROZEN_A1.md` and `reviews/ASSEMBLY2_FROZEN_B1.md`, required the same mixed-boolean validation correction and found no required mathematical correction. Their full reports and original code, tests and chapter remain unchanged under `reviews/ASSEMBLY2_FROZEN_R1_*`; `ASSEMBLY2_FROZEN_R1_INPUTS.json` seals all original inputs. The corrected validator examines supplied elements before accepting numeric coercion. Regression cases cover Python/NumPy booleans, both vectors and both public APIs. No reconstruction of provenance of an already numeric array is promised.

Both fresh complete corrected-version reviews are CLEAN, with no required corrections: `reviews/ASSEMBLY2_FROZEN_A2.md` and `reviews/ASSEMBLY2_FROZEN_B2.md`. Each received only the same nine-file packet and manifest, read all 2,606 lines including the full 1,275-line finite-dynamics chapter, verified unchanged hashes, ran all 13 finite-reduction tests and the exact guide example, and performed independent bounded raw-derivative/algebra checks. No project history, prior verdict, study or archived array was supplied. The final proof/code input seal is `reviews/ASSEMBLY2_FROZEN_R2_INPUTS.json`.

Complete source and correction records are `source_audits/SCOPED_OBSTRUCTIONS_ASSEMBLY.md` and `source_audits/FROZEN_API_ASSEMBLY.md`. The latter verifies preservation of every earlier production definition and test class. The accepted 27-file edition and dependency check are `reviews/ASSEMBLY2_FROZEN_LIBRARY_INPUTS.json` and `reviews/ASSEMBLY2_FROZEN_STANDALONE.md`. The unchanged scientific implementation passes all 90 tests in the separate standalone final-assembly packet; that does not accept its other pending proofs. The concurrent exporter and inherited artifacts remain outside this commit.

## Resumed assembly: coherent kernel and full finite tangent geometry

The frozen/ReLU package is committed at `b0482b2`. Two further complete additions now extend existing chapters:

| Fragment | Destination | Lines | SHA-256 |
|---|---|---:|---|
| `COHERENT_KERNEL_ADDITION.md` | Continuous depth, Section 15 | 589 | `19c267a56658d6980ed5bd4957d2db9fda5f7178c4eb7024dde961c285a8fd53` |
| `REACHABLE_HESSIAN_ADDITION.md` | Finite controls, Section 14 | 985 | `1dbf61698ef88e716a9bf1ef11b6d5ded2d21b321f5f50b9d1a4fba89fa9bbf1` |

Each fragment occurs byte-exactly once in its maintained destination; the earlier chapter proof bodies remain unchanged. Their complete source/correction records are `source_audits/COHERENT_KERNEL_ASSEMBLY.md` and `source_audits/REACHABLE_HESSIAN_ASSEMBLY.md`. Every needed model-specific argument and dependency is inside the maintained chapter. No specialized external theorem, source array or historical verdict carries a proof step.

The coherent result defines a distinct residual model with dense untied trunk matrices normalized by W/n, residual steps alpha/L, fixed bounded input/readout profiles, a bounded C2 activation, finite arbitrary data and lower-bounded C2 loss. It derives the finite mobility Ln² and its continuum energy metric, defines and proves completeness of the strongly measurable row/column Bochner carrier, establishes depth existence and the genuine Fréchet gradient, and proves global physical training existence, uniqueness and restart by the ordered energy/adjoint/column/row estimates. It supplies no Gaussian W/sqrt(n) theorem, noisy joint approximation, trained-endpoint extension, fitting or finite scalar closure.

The full finite tangent geometry retains the three-hidden-layer arctangent network, one sample x=y=1, all trained blocks, scaled hidden matrix coordinates sqrt(n)W, stored readout, full squared loss and mobilities (n,1,1,n). It derives the full Hessian and material derivative, including both mixed matrix terms, and the exact physical Jacobian with its rank-one residual-clock correction. The explicit correlated deterministic family is reachable from exactly zero readout; its entire segment has bounded primal norms and its terminal Hessian is bounded, but its signed material form grows linearly with width. No Gaussian-typical, common fixed-time or integrated signed obstruction is inferred.

The positive part is also incorporated: two-sided global finite feature flow with explicit polynomial primal bounds; nuclear/trace bounds; every-plane intrinsic tangent-volume control; unconditional Gaussian expected absolute log-volume bounds of order n on fixed horizons under stored readout variance n^-2; and forward physical counterparts for either initial residual sign, with all clock terms retained. Exact hidden-projection determinants isolate at most n angle factors, including singular projections, and give feature/physical slope equations only on invertible branches. Intrinsic volume does not provide a projected determinant lower bound, hidden entropy, response covariance or adaptive Gaussian-query control.

Both fresh complete independent reviews are CLEAN with no required corrections: `reviews/ASSEMBLY2_KERNEL_HESSIAN_A1.md` and `reviews/ASSEMBLY2_KERNEL_HESSIAN_B1.md`. Each received only the same two complete candidates, the 98-line notation contract and their manifest; each read all 1,672 mathematical lines plus the 17-line manifest and checked unchanged hashes. Neither used project history, prior verdicts, studies, external sources, delegation or training. Both independently substantiate every subsection, constant, carrier, gradient, clock and volume/projection argument. `reviews/ASSEMBLY2_KERNEL_HESSIAN_R2_INPUTS.json` seals that packet. Its R2 name reflects addition of the positive-volume proof before either review began, not a failed review.

All four resumed additions now have paired complete clean reviews at their accepted bytes. The current full scientific inventory is `LIBRARY_INPUTS.json`, also retained as `reviews/ASSEMBLY2_FINAL_LIBRARY_INPUTS.json`: 27 files. The coordinator's standalone edition passes the boundary/local-link check and all 90 deterministic tests plus the new guide example; logs are in `reviews/ASSEMBLY2_FINAL_STANDALONE.md`. This is independent of the fresh assembled-library integration verdict, which remains pending at this commit. Its first read-only environment blocked five temporary-fixture tests; a fresh full audit is running on byte-identical, read-only inputs with separate writable scratch. No source or implementation correction was needed for that environment issue.
