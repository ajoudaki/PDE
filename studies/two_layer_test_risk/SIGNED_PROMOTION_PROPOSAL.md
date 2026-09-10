# Proposed signed finite-time comparison and reproducible certificate

This proposal supersedes the earlier unsigned recommendation in
PROMOTION_PROPOSAL.md. It concerns the immutable signed edition in
`data/generated/two_layer_test_risk/signed_promotion_v1/`, whose manifest is
`bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3`.
The scientific study is complete. This file records the separate proposal
for established book/code; no live established file has been changed.

## Scientific addition

For the prescribed two-hidden-layer tanh network, three fixed correlated
training inputs, canonical Gaussian initialization and mobilities, and
uniform-circle teacher `cos(3 alpha)`, the fully trained population network
has lower test risk than its frozen initial hidden features at equal
training loss on a width-independent positive early-time interval.

The complete proof establishes unique loss matching and
`|Delta(t)-chi*t^3| <= M*t^4`, with finite `M>=1` on `[0,T]`, and certifies
`27/100000 < chi < 273/1000000`. Thus
`Delta(t) >= (27/200000)*t^3 > 0` for
`0<t<=min(T,27/(200000*M))`. All three trained blocks, the moving residual,
and both directions and response means of the reused connector are retained.
The broad C.1--C.3 population theorem is used unchanged as a foundation.

The effect is of order `0.000272*t^3`, against initial risk `1/2`.
Neither the remainder constant nor the interval length is numerically
evaluated. This gives no practical effect-size claim, later-time dominance,
universal benefit, iid-average or sample-complexity result. Finite GF and
vanishing raw-GD steps inherit the sign only in probability on each fixed
`[delta,t0]`, `delta>0`, retaining the common actual small random readout.
There is no quantitative width rate or finite-width sign uniform down to zero.

## Exact destinations

The reviewed edition changes or adds exactly nine files:

| Destination | Complete proposed content |
|---|---|
| `docs/global_nonlinear.md` | Append [PROMOTION_SIGN_C4_V2.md](PROMOTION_SIGN_C4_V2.md) as C.4, including the actual-flow proof, finite-capture corollary and all four certificate/error proofs. Preserve the existing chapter byte for byte, with one separating newline. |
| `docs/README.md` | [PROMOTION_SIGN_DOCS_README.md](PROMOTION_SIGN_DOCS_README.md), the complete revised guide, reconciling the new fixed-design theorem and computer-assisted proof with existing scope. |
| `code/README.md` | Append [PROMOTION_CODE_README_APPENDIX.md](PROMOTION_CODE_README_APPENDIX.md) to the unchanged guide. |
| `code/tools/two_layer_risk/certificate.py` | [PROMOTION_certificate.py](PROMOTION_certificate.py), standalone `certify(output, target=26)` and CLI. |
| `code/tools/two_layer_risk/certificate_kernel.cpp` | [certificate_kernel.cpp](certificate_kernel.cpp), the executed arithmetic kernel. |
| `code/tools/two_layer_risk/angle_error_bound.py` | [angle_error_bound.py](angle_error_bound.py), exact rational circle-error bound. |
| `code/tools/two_layer_risk/check_driver.py` | [PROMOTION_check_driver.py](PROMOTION_check_driver.py), focused exact and synthetic-contraction checks. |
| `code/tools/two_layer_risk/check_kernel.py` | [PROMOTION_check_kernel.py](PROMOTION_check_kernel.py), elementary and finite-tensor checks. |
| `code/tools/two_layer_risk/README.md` | [PROMOTION_TOOL_GUIDE.md](PROMOTION_TOOL_GUIDE.md), full conventions, supported platform, usage, errors and limitations. |

No public `pde` API or other established source is changed. The tool is an
opt-in fixed mathematical certificate, not a training/parameter-search driver.
It uses fresh outputs, rejects optimized Python and unsupported inputs, and
requires the documented Linux/IEEE/compiler conditions. Its runtime requires
no study files, Git repository, historical reports or archived arrays.

Candidate C.4 SHA256:
`dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc`.
Maintained driver SHA256:
`36dd0b21dea51647dcbb9aef7c958d8f2ddadc397529e629ada5b122af0d2810`.
Every remaining proposed destination and input hash is in the frozen manifest.
The full standalone edition is under that run's `edition/` directory.

## Reproduction and verification

The primary calculation and one fresh full independent reproduction both
completed within 32 CPU seconds. Their 322 invariant files, including the
exact final rational certificate, agree byte for byte. The proof includes
Gaussian strip/tail bounds, nonunit rule masses, singular-safe covariance
perturbations, input/label errors, elementary arithmetic and summation,
outward rational intervals, and the circle-rule error. A floating numerical
sign or agreement between runs alone is not the proof.

The maintained command has the same numerical helpers and complete
calculation/assembly operations as the executed study source. Its changes
are interface, source location, provenance and process isolation. Fresh
reviewers independently checked that correspondence, reconstructed all saved
primitive contracts and intervals, rebuilt the identical kernel binary,
and evaluated an independently implemented full four-slot contraction.
No third full coefficient calculation was run. The full-run CLI/API examples
are documented reproduction recipes; their interfaces were exercised with
bounded checks, and their numerical content verified by exact correspondence
to the two completed executions. Target 30 was checked analytically and in
small tests but was not used for a full coefficient calculation.

The original internal reports and independent relevance selection are
retained. All separate signed promotion gates have now passed:

| Gate | Original full report and outcome |
|---|---|
| Independent relevance | [SIGN_RELEVANCE.md](SIGN_RELEVANCE.md): accept narrow assembly. |
| Fresh complete scientific review A | [SIGNED_PROMOTION_REVIEW_A_V1.md](SIGNED_PROMOTION_REVIEW_A_V1.md): ACCEPT, no required corrections. |
| Fresh complete scientific review B | [SIGNED_PROMOTION_REVIEW_B_V1.md](SIGNED_PROMOTION_REVIEW_B_V1.md): PASS, no required corrections. |
| Fresh complete integration review | [SIGNED_PROMOTION_INTEGRATION_V1.md](SIGNED_PROMOTION_INTEGRATION_V1.md): ACCEPT, no required corrections or missing operative inputs. |

The coordinator read all three original full reports and their retained
checker sources, verified all 1,194 frozen payload hashes and current source
correspondence, and checked exact report/output provenance. Review B's first
combined saved-bit replay hit its 60-CPU-second cap; the two separate bounded
replays passed, and the capped attempt remains recorded. The first complete
study-level scientific audit had already performed the sole reserved fresh
full coefficient reproduction. The later promotion reviews replayed that
evidence and checked the maintained source correspondence independently.

Two inert source comments retain historical filenames. Reviewers explicitly
classify them as nonblocking; they introduce no missing runtime/proof input.
They remain unchanged in this accepted version. The integration reviewer
could not authenticate the nonoperative study-builder hashes within its
isolated packet; it checked assembled bytes directly. The coordinator has
verified those builder/assembler hashes against the retained study sources.
Reviewers did not audit the unrelated older book/library complement.

## Approval boundary

Recommendation: promote exactly the frozen nine-file addition. All required
pre-approval gates are complete. The original user instruction and
[RESEARCH_WORKFLOW.md Part 2, step 5](../../RESEARCH_WORKFLOW.md)
require approval of the concrete reviewed package before changing established
book/code. Research/commit authorization does not itself approve promotion.
After approval, recheck live dependencies and concurrent work, apply only the
accepted mapping, verify correspondence and affected integration checks, and
commit under the shared writer lock. A changed scientific package needs new
reviews and approval. The study's signed theorem requires no further research.
