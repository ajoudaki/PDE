# Independent integration review of frozen promotion_v1

**Verdict: PASS for integration at the exact bytes identified below.** No
required integration correction was found. This is a completed, independent
placement, consistency, preservation and standalone-boundary review. It is
neither a whole-book mathematical audit nor either of the two required complete
scientific reviews. It does not authorize promotion or presume those reviews'
outcomes.

Reviewer: `/root/promotion_integration`. Review date: 2026-09-10.

## Independence and frozen scope

I followed only `PROMOTION_INTEGRATION_ASSIGNMENT.md`, the dispatched frozen
packet and edition, and the required `solve-math-rigorously` and
`investigate-conjectures` skills, including the latter's adversarial-audit
reference. I did not read study history, author derivation or internal reports,
selector findings, or either scientific review. The packet's neutral scientific
assignment was read as a frozen packet input; its paired-review role did not
replace this review's integration assignment.

My identity is distinct from all declared authors/assemblers (`root`,
`cubic_derivation`, `matching_remainder`, `quadrature_check`), the selector
(`relevance_selector`), and scientific reviewers (`promotion_review_a` and
`promotion_review_b`). No reviewer outcome was communicated to me or used as
evidence. I changed no frozen input, established file or Git state. My only
writes were this report and files in the assigned `integration_scratch/`.
No training, Gaussian/angle quadrature, cloning or worktree operation occurred.

All following edition paths refer to
`data/generated/two_layer_test_risk/promotion_v1/edition/`.

## Complete read coverage and unread complement

The entire new appendix was read: `packet/candidate.md`, lines 1–642. Exact
byte comparison proves that this is the assembled `docs/global_nonlinear.md`,
lines 3831–4472, with no omitted, altered or additional scientific text.

I read the full notation contract, lines 1–98, and the full after-guide,
lines 1–265. The before-guide was covered by reading its old global-nonlinear
row in the exact diff and verifying line by line that all other 264 lines are
identical to the fully read after-guide. Thus the whole before/after guide
content, including its broader question and limitations, is accounted for.
The packet copies of the notation and after-guide equal the edition copies
exactly.

I read every line of `packet/dependencies.md`, lines 1–1777. Its three complete
operative excerpts were verified against these exact edition ranges:

| Older global chapter range | Complete content read |
|---|---|
| 181–500 | Section 2 and all of Section 3, including adaptive conditioning, source/response laws and singular-query regularization |
| 1835–1893 | A.1–A.4, including their full proof bodies |
| 2449–3829 | The C introduction and all of C.1, C.2 and C.3, including C.3's weighted-loss correction |

For cross-reference resolution I additionally read the complete older
orientation passage at `docs/global_nonlinear.md`, lines 1799–1834, and inspected
the heading destinations for special-data Sections III.F and III.V. In the
edition those legacy labels point to the special-data chapter, as its
orientation states. Their destinations exist; the supplied Section 3 proof
contains the operative finite-program conditioning and source/response
arguments used in this review. The packet's legacy-label explanation was not
treated as permission to assume unread scientific results.

The old global chapter's unread scientific complement is precisely lines
1–180, 501–1798, and 1894–2448. Searches returned isolated headings or reference
lines in those ranges, but did not constitute full scientific reading. The
other seven mathematical chapter bodies were not audited; special-data
reference-heading inspection was not an audit of those proof bodies. The
unchanged implementation-guide body was not audited, and no implementation
modules were included or executed. I read all 100 lines of the frozen
`code/tools/check_library.py` before running it. Machine hashing and boundary
scanning covered every edition file; neither is represented as mathematical
reading. Both neutral assignments, manifest and supplied validation were read
in full. An initially truncated combined display was repaired by separate full
candidate and guide reads and complete, bounded dependency reads.

## Exact identities, hashes and commands

SHA-256 values fixing the reviewed addition and its evidence are:

| Input | SHA-256 |
|---|---|
| Integration assignment | `4338707e35eb6f78fc7401f539c95bf8dcc823c8bd98b0f0bac6b323155b2f34` |
| `packet/assignment.md` | `8e4351e9b78e961543cd88c03ee9115aa3b92aec69815afdfbdce891f1f8267e` |
| `packet/candidate.md` | `b807efbd793b5b6ebc67e7f673efbcae4a234eacd28e667c304597c51d7435d4` |
| `packet/dependencies.md` | `8378046bc80abc06077b34182141d282cf0ba6ac6d7fde6c84e2c6bab5b19db7` |
| Notation, packet and edition | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Before-guide | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| After-guide and edition `docs/README.md` | `e92464827a2d277a57a356167190598f52425769e23e7538cd9e3cbbe7afb371` |
| Old global-chapter prefix | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| Edition `docs/global_nonlinear.md` | `5f31b500a60ad98fd9a200094f1169267a590a39015aaa53c8c222bc07cb3fc2` |
| `manifest.json` | `14316c7a0162fdc81788efabdce1f08b2a7d219adbd8fd8960f295274d5345b7` |
| Supplied `validation.json` | `fa418e16e1586924084004314edc462573637544a18ba8a513c2bd5eac6bc420` |

The complete computed hash inventory, excerpt hashes and assertion outcomes
are retained in [check_results.json](/home/amir/Codes/PDE/data/generated/two_layer_test_risk/promotion_v1/integration_scratch/check_results.json).
The independently written reproducible check is
[check_integration.py](/home/amir/Codes/PDE/data/generated/two_layer_test_risk/promotion_v1/integration_scratch/check_integration.py),
SHA-256 `028cba4a0ff9c166c484dadbb290391fe1c25f6b5c7204a1c6e3d33616273727`.

Executed from `/home/amir/Codes/PDE`:

```text
python -B data/generated/two_layer_test_risk/promotion_v1/integration_scratch/check_integration.py
```

It completed with status 0 and established:

1. All six packet hashes and all twelve edition hashes equal their manifest
   values. The edition contains exactly the twelve declared files and no
   symlinks.
2. The assembled global chapter is exactly its 183,317-byte old prefix,
   followed by one newline, followed by the 25,235-byte candidate. The prefix
   hashes to the declared input-source hash. Thus no earlier chapter byte was
   edited or dropped.
3. Comparing all edition files to the declared copied-source hashes produces
   exactly `docs/README.md` and `docs/global_nonlinear.md` as changed paths.
   Every other copied file is unchanged. Source preservation here is verified
   against the frozen source hashes; no live checkout or Git object was read.
4. The guide has exactly one changed line, line 155, produced solely by
   appending the one designated sentence before its table-cell terminator.
   The exact [guide.diff](/home/amir/Codes/PDE/data/generated/two_layer_test_risk/promotion_v1/integration_scratch/guide.diff)
   is retained. No surrounding scope statement changed.
5. Every supplied dependency excerpt is an exact copy of its stated edition
   line range. All 31 C4 equation tags occur once, in order, and every C4
   equation reference resolves to one of those tags. The C.4 heading occurs
   once in the global chapter.
6. The candidate contains no study, generated-artifact, promotion-packet,
   review/verdict or Git dependency reference.

The check independently invoked the inspected frozen structural checker,
with working directory equal to the standalone `edition/`:

```text
/usr/bin/python -B code/tools/check_library.py
```

It completed with status 0, empty stderr, and exactly:

```text
Library boundary and local links checked: 12 files.
```

This verifies local file links and the proof-only library boundary. The
checker intentionally does not prove mathematics, validate external URLs,
resolve prose equation references, or execute the implementation catalog's
examples. Equation references were checked separately as above. The edition
is sufficient for the assigned proof reading and boundary check; it is not
being certified as a complete executable distribution of the maintained APIs.

## Integration findings and adversarial checks

| Component | Finding |
|---|---|
| Placement | PASS. C.4 follows the local C.1–C.3 results and the immediately relevant weighted-loss correction. Its title and opening identify a local result despite the chapter's global main title. It does not import the earlier shifted-arctangent model's activation or one-input assumptions. |
| Duplication within the audited scope | PASS. C.1 supplies flow/capture, and C.3 supplies strict activity; neither supplies the new equal-loss risk comparison. Restating the fixed model and initialized fields is needed to make the new theorem independently readable. The proof uses the earlier results without presenting their old conclusions as new risk benefits. No assertion of a whole-book semantic duplication audit is made. |
| Canonical model and types | PASS. Two hidden layers, dimension two, three fixed inputs, `x/sqrt(2)`, stored readout normalization `1/n`, initialization variances `1,1/n,1/n^2`, mean squared loss and mobilities `(n,1,n)` are stated together. Finite transpose and population adjoint are distinguished; same-layer expectations and auxiliary field types are explicit. The risk `R` is separated from `R^hid`. |
| Dependency interface | PASS. C.1 permits the zero-mobility frozen model and vanishing finite readout perturbation, its stated finite probes support the passive construction, and its C introduction supplies finite GF. C.3's weighted correction uses `p=y/3`, so its summed-loss factors are not silently imported. Only positive training activation/response Grams are inverted; the singular input Gram remains intact. |
| Guide/theorem correspondence | PASS. The exact new guide sentence states a fixed two-hidden-layer tanh design, controlled cubic test-risk expansion, equal training loss, and unresolved sign/nonvanishing. It does not promise a generalization theorem, nonzero cubic coefficient, or signed benefit. The surrounding guide's broader generalization question remains appropriately open. |
| Actual-flow versus formal expansion | PASS at the integration interface. C.4 supplies its own fixed-direction fourth-moment argument, uniform passive bounds and integral remainders. It does not claim that a finite jet or C.3's little-o onset alone supplies an order-four population remainder. The full mathematical validity remains the paired scientific reviews' separate responsibility. |
| Response and singular-slot boundaries | PASS. The defined coefficient retains the connector's forward and adjoint uses and readout correction. Its explicit contraction retains both innovation second moments and mean response products. Passive slots may coincide or be antipodal without inverting their augmented covariance. No independence between every passive Gaussian answer is asserted. |
| Clock and sign boundaries | PASS. Strict frozen decrease and a local clock margin support matching. The displayed positive `beta` concerns training speed. The identity `p^T(J-beta a)=0` explicitly removes that contribution at matched loss; it cannot determine the teacher projection `chi`. The signed consequence has the separate premise `chi!=0`, and a zero coefficient requires further work. |
| Finite-width/GD boundaries | PASS. The actual small random stored readout is retained. Exact finite matching and its sign transfer are restricted to fixed intervals bounded away from zero, in probability, after the width limit. The raw-GD assertion uses every deterministic vanishing step on a fixed local horizon. No width rate, growing horizon, arbitrary shrinking lower endpoint, or uniform finite-width sign near zero is advertised. |
| Standalone proof boundary | PASS. New proof dependencies are contained in the edition; no study note, numerical table, code output, training run or prior verdict is required. No new implementation or empirical claim is introduced. The Gaussian formula specifies an unevaluated coefficient, not numerical evidence. |

## Corrections, limitations and acceptance condition

**Required corrections: none identified in this integration scope.** No
unresolved integration objection remains. No scientific correction is proposed
by this report. The coefficient's sign and nonvanishing remain open scientific
questions expressly outside the asserted result; they are not review defects
that can be filled by an internal numerical estimate.

This PASS applies only to the unchanged candidate, guide, dependencies and
assembled edition hashes recorded above. It does not certify the unread book
complement or substitute for two fresh complete scientific reviews. Any
scientific correction to the candidate or its operative premises requires
renewed complete scientific reviews of a newly frozen packet, followed by
integration verification of that edition. User approval of the concrete
reviewed addition remains a separate promotion requirement.
