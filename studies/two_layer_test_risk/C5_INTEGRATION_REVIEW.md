# Independent C.5 integration review — frozen edition v2

**Verdict: ACCEPT for integration, with no required corrections.** This verdict
applies only to the nine destinations in the frozen edition whose manifest is
`bff8f94655977a14491d3777463513069a1895bf2eaea7f924e6e58802b31941`.
It is separate from the paired scientific gate and is not permission to bypass
the remaining promotion requirements. No established file or Git state was
changed by this reviewer.

## Assignment, independence, and complete read coverage

I started fresh from `C5_INTEGRATION_ASSIGNMENT.md` and the named frozen root
`data/generated/two_layer_test_risk/c5_promotion_20260912_v2/`. I read the
required `solve-math-rigorously` skill. I did not read live author notes, the
study README, prior reports/verdicts, selector findings, scientific reviewer
findings, other studies, chats, or Git history. I did not delegate this review.
An initial file inventory exposed filenames of other scratch directories; their
contents were neither opened nor used. The assignment and skill SHA256 values
are respectively:

```
206cfdc53a01495d718293f3acc7b430f68bed28a12e3368a851006b6f431d58
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
```

Read completely:

- The 1,736-line candidate, including all flow, matching, Gaussian-response,
  cubature, arithmetic, angular and interval-assembly arguments. Exact inverse
  title/label comparison establishes correspondence with the complete
  1,736-line `original_candidate.md`; all its scientific text was read through
  the identical relabeled candidate.
- All 1,775 lines of `packet/dependencies.md`, containing the full operative
  Sections 2–3, A.1–A.4, C.1–C.3 and weighted-loss correction. I checked their
  correspondence to the assembled chapter, including its current C introduction.
- The complete 98-line notation contract, byte-identical in packet and edition.
- All six new tool files: `certificate.py` (429 lines), kernel (236),
  `angle_error_bound.py` (88), `check_driver.py` (140), `check_kernel.py` (161),
  and tool guide (169).
- The complete 382-line original executing numerical driver, and the full
  source diff against the new driver.
- Complete before/after documentation guides (580/578 lines) and code guides
  (591/621 lines). The code guide's entire 591-line old prefix is byte-identical
  in the new guide; the complete added 30 lines were read separately.
- Both complete raw evidence trees: 580 files per run, including every one of
  the 64 angles' input tokens, primitive output arrays, audit records,
  enclosures and empty stderr files; constants, metadata, compile logs and full
  aggregate result records. Numerical records were consumed completely by the
  exact reconstruction checks described below, rather than reading only their
  final flags or decimal summaries.
- The frozen structural checker, including its link and import-boundary logic.

The precise older chapter prose/proof scope read, using **current edition**
line numbers, is:

| Lines | Scope |
|---|---|
| 1–184 | Opening and complete main theorem/model statement and proof architecture |
| 185–503 | Complete operative Sections 2 and 3, via the packet with byte correspondence |
| 1760–1834 | Closing §12.4 body and appendix organization/introduction/table, as placement context |
| 1840–1896 | Complete A.1–A.4, via byte-corresponding packet text |
| 2454–3834 | Current C introduction and complete C.1–C.3 proof units, including weighted correction |
| 3836–3998 | C.4 introductory scope, model, theorem, limitations and architecture, plus the first state-definition lines of C.4.1 |
| 16995–17016 | Final C.4.10 paragraphs adjoining the proposed addition, as boundary context |
| 17018–18753 | Complete new C.5 candidate |

I also inspected the chapter's heading inventory for placement and fragments.
The unread older complement is lines 504–1759, 1835–1839, 1897–2453,
3835, and 3999–16994, except heading metadata; in particular I did **not**
freshly audit the older §§4–12 proofs, B, or the C.4.1–C.4.10 proof development.
For later C.4 claims I used the complete current guide as assigned. Reading the
last C.4.10 paragraphs does not constitute an audit of that proof. Other
established chapters were hash/link/heading-scanned where needed, not reviewed
as scientific proofs. The unrelated `pde` implementation and old core examples
were not audited or executed; they are not included as source files in this
edition and are unchanged by these destinations.

The packet's legacy line comments do not describe current chapter offsets.
There is also one innocuous context difference: its C introduction predates
the current paragraph's explicit C.1/C.3 names and C.4 scope sentence. The
entire remaining C.1–C.3 text matches. My first structural assertion detected
that difference rather than silently accepting the packet as the assembled
context. I then read and explicitly compared the current paragraph and
recorded the exact difference in `integration/structure.json`. No proof
premise changes, no contradictory scopes, and no candidate correction result.

## Input integrity and exact destination correspondence

All **1,187** manifest/packet/edition/evidence files listed for this review were
hashed and checked, including all 1,160 evidence files. The complete per-file
hash inventory is
[input_hashes.json](../../data/generated/two_layer_test_risk/c5_promotion_20260912_v2/integration/input_hashes.json),
whose SHA256 is
`fb4a9446caaf27987aca0d08bd8ee257624c2eaa7f69bc9c28cd65ac6befa727`.
This records every frozen input hash, rather than only the principal files.
Historical source names/hashes recorded in raw metadata are provenance, not
additional proof inputs fetched outside the packet.

| Destination | Exact correspondence | Destination SHA256 |
|---|---|---|
| `docs/global_nonlinear.md` | All 750,093 old bytes/17,016 old lines preserved, then one newline and exactly `packet/candidate.md` | `1f079e1e891dfbee88ac87495cb3b39c9e6992da34d4acf56d98c1c024d89dc9` |
| `docs/README.md` | Five local changes described below; all other text preserved | `75b01a8d3888674d6034e8543a42bac13e5fdad4c989e3a6a9081c81cbc8d9d8` |
| `code/README.md` | Entire old prefix preserved; 30-line optional-tool section appended | `3cb90e55b630870c391e56158432a909fc60872b4af724756b2be19884ef7d6e` |
| `code/tools/two_layer_risk/certificate.py` | Original executing numerical core plus reviewed standalone boundary/worker changes | `773f8c90c08b17736fe3fb37213ecce6ef3fb5c848fd3ff2e4f73e8f9b909855` |
| `code/tools/two_layer_risk/certificate_kernel.cpp` | Original executed source except one explanatory comment substring | `a75b60a5615df7853e54179458ff8f0b5c646a5fe956eb87f31b1431c1251cc7` |
| `code/tools/two_layer_risk/angle_error_bound.py` | Byte-identical to the manifest's source | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| `code/tools/two_layer_risk/check_driver.py` | Byte-identical to the manifest's source | `1f70dda734e117dca6ed25e1f2656242fbb085ee8cd0fd6f7ee9b7de8da9a4e2` |
| `code/tools/two_layer_risk/check_kernel.py` | Byte-identical to the manifest's source | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| `code/tools/two_layer_risk/README.md` | Full standalone contract read and verified against implementation | `fa51953f28a7ef39c6770ccf9c2e9a18d9302ecefe36d8a16d288988fca86681` |

The candidate hash is
`70c25097ff8133a48ebe683537c4329a5b74440488eb792de41edc76496a263d`.
Its inverse transform—restore the original title, replace `C5.` with `C4.`,
and replace `C.5 certificate:` headings with `C.4 certificate:`—recovers the
original exactly, SHA256
`dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc`.
The existing C.4 subsection labels are therefore untouched. All 60 new
equation labels occur once in the complete chapter; every new C5 reference
resolves to that set, with no stale C4 equation reference in the candidate.
The guide's C.5 fragment resolves uniquely to the assembled heading. Existing
guide C.4 fragments and all new local links resolve within `docs/` or `code/`.

The documentation guide makes five surgical changes: one opening scope
sentence; a C.5 clause appended to the global-nonlinear chapter table entry;
the explanation that C.5 uses executed arithmetic jointly with analytic
proof; a separate C.5 summary in the scope section; and the final statement
about reproducible computer-assisted evidence. The complete roadmap is
byte-identical. Existing C.4.5–C.4.10 summaries, including the finite-episode
C.4.10 result, are preserved without weakening or strengthening them. C.5 is
not presented as completing the roadmap's class-level comparison milestones.
The exact guide diff is retained as `integration/docs_guide.diff`.

## Model, claim boundaries, and proof-to-code interface

The text and guides consistently retain two tanh hidden layers, no biases,
stored forward factors `1/sqrt(2)` and `1/n`, initialization variances
`(1,1/n,1/n^2)`, raw mobilities `(n,1,n)`, residual `f-y`, and mean loss with
weights `1/3`. Thus the initialization coefficients use `p=y/3` and physical
time throughout. The three directions and signed labels are fixed. Their
input Gram remains correlated and rank two; the positive training activation
Gram, rather than the input Gram, is inverted where needed.

The comparator freezes **both** hidden layers and trains only its readout.
Its equality with the full initial tangent kernel is stated only for the
population limit. At finite width the common actual small random readout is
retained, so the trained network's hidden tangent blocks need not initially
vanish. No finite full-tangent comparator has been substituted.

The passive-input construction follows the exact linear first-row span and
bounded-action probe contract. The uniform angular net argument supplies the
whole-circle limit without changing training weights. C.1 permits the frozen
mobilities, arbitrary deterministic vanishing GD steps and the vanishing
readout perturbation; its squared-loss finite-GF corollary is explicit.
Positive training activation/kernel Grams and the exact frozen exponential
loss justify the unique matching clock. The finite comparison is restricted
to fixed `[delta,T]`, then fixed `[delta,t0]` for its sign, in probability.
There is no width rate, arbitrary `delta_n -> 0`, or finite-width uniform sign
down to zero.

The population remainder is derived from strong integral equations. The
fourth-moment arguments concern fixed initialized directions; the activation
Taylor step removes the `L2` error before expanding along the `L4` direction.
It does not assume ambient `L2` Fréchet smoothness or infer a positive-time
Taylor theorem from a finite-width jet. The moving residual and readout
correction are retained. In particular
`p.T J_train = (16/3) A`, `p.T a_train = 2 B0`, and
`beta = 8 A/(3 B0)` give `p.T(J_train-beta*a_train)=0`; the positive training
speed alone is not used to establish the risk sign.

The Gaussian scalar formulas retain the full second-moment innovation and
the response mean product of the **same** matrix in both orientations.
Formal passive slots remain distinct at singular covariance. The code's
training indices `0,1,2` and passive index `3`, including all four tensor
indices, agree with the explicit bijection. Upper training moments use three
roots; the seventeen distinct dynamic moments use the conditional fourth
root without accidentally multiplying training moments by its truncated
mass. The independent synthetic response-mean test exercises the tensor
contraction, and the direct small-rule test exercises actual source indexing.

The numerical proof has a complete interface: exact constant/trigonometric
intervals; exact dyadic grids and echoed input bits; covariance perturbation
from exact rational `A A.T`; arithmetic and Gaussian-rule radii; label error;
outward rational interval propagation; strictly positive denominator;
independently enclosed clock subtraction; and the circle error after checking
`|beta| <= 1/10`. No accuracy premise is assigned to the numerical root
proposal, a clipped conditional variance, ordinary library tanh, or agreement
between two runs. Source comments contribute no proof premises.

The stated conclusion remains the small local fixed-design advantage, with
`T` and the fourth-order remainder constant finite but unevaluated. The sign
certificate does not supply later-time superiority, sample complexity, an
architectural/depth comparison, an independent trained-dynamics solver, or a
practical magnitude claim. Its size and those limitations remain visible in
all new guide prose.

## Source semantics and reproducibility checks

The original executing driver hash is
`a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1`,
matching both supplied metadata records. Every one of its 20 numerical/helper
function or class definitions other than `run` is AST-identical after removing
the explanatory `grid` docstring. The complete 64-angle body is AST-identical;
the aggregate formulas were also checked directly. The new differences are
the neighboring-source lookup, removal of study/Git runtime dependencies,
public argument validation, fresh isolated worker, caller-environment
preservation, source metadata, and explicit rejection of optimized Python.
Compiler version collection moves within recorded timing; no numerical
formula or error budget changes. The complete diff is retained as
`integration/driver_source.diff`.

Restoring the one kernel comment substring recovers SHA256
`9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9`,
matching both original executed-source hashes. A new compilation of the
candidate kernel with the required flags produced binary SHA256
`8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7`,
also exactly matching both recorded original binary hashes. The original
binary files themselves are not part of the frozen evidence; this equality
comes from the newly compiled candidate binary and supplied provenance.

The public API rejects booleans/noninteger/unsupported targets, empty/NUL/byte
or invalid paths, existing output, dangling output symlinks, and optimized
Python before output creation. The documented namespace import and help
command work without starting a calculation or compiler. A clearly marked
inert worker mock verified the launch arguments, target 30 forwarding,
one-thread child environment, unchanged caller environment, and independent
JSON return ownership. That mock is not a coefficient execution. The source
and guide correctly describe the 900-second cumulative run gate and separate
kernel limits; they do not claim a hard total compiler/wall timeout.

## Original evidence and new command outcomes

The supplied metadata records these original target-26 commands, each with
working directory `/home/amir/Codes/PDE`:

```
studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_20260910_01
/home/amir/Codes/PDE/studies/two_layer_test_risk/certificate_driver.py --target 26 --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/certificate_reproduction_20260910_01
```

Both report completed status, exit 0, target 26, 256 angular nodes reduced to
64 evaluations, 96 interval bits, no random seed, empty compile/stderr logs,
and 86,101,134 upper nodes. Recorded CPU times are 31.17975 and 30.66773
seconds. Both aggregate result hashes are
`89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`.

The new review used `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`, `python -B`,
and fresh assigned scratch. Commands below are exact apart from the table's
explicit path aliases: `ED` means the frozen `edition/`, `S` the frozen
`integration/`, and `CHECK` means
`/home/amir/Codes/PDE/studies/two_layer_test_risk/C5_INTEGRATION_CHECK.py`.
The four focused script commands ran with cwd `ED` and additionally set MKL
and NumExpr threads to one. Every check completed below 60 CPU seconds;
the reviewer checkers have a 60-second soft CPU limit, and the focused runner
used child limits plus a 60-second wall bound.

| Command | Outcome |
|---|---|
| `python -B CHECK structure` | PASS; 1,187 hashes, nine destinations, preserved prefixes/roadmap, 60 labels, source correspondence and links |
| `python -B CHECK replay --run certificate_20260910_01` | PASS; all 580 records, every interval and aggregate reconstructed exactly; 23.59 s elapsed |
| `python -B CHECK replay --run certificate_reproduction_20260910_01` | PASS; all 580 records reconstructed independently of the first check; 23.54 s elapsed |
| `python -B CHECK boundary` | PASS; 16 invalid-request cases, optimized rejection, help, namespace import and inert-worker interface checks; 0.77 s elapsed |
| `python -B code/tools/check_library.py` | PASS; frozen source boundary and local links, 17 Markdown/Python files; 0.198 CPU s |
| `python -B code/tools/two_layer_risk/check_driver.py --output S/driver_check` | PASS; longer rational constant/trig oracle, square-root/grid inequalities at 26 and 30, synthetic response means and Fourier weights; 3.175 CPU s |
| `python -B code/tools/two_layer_risk/check_kernel.py --output S/kernel_check` | PASS; independent rational elementary-function oracle and supplied finite-rule sums; 0.917 CPU s |
| `python -B code/tools/two_layer_risk/angle_error_bound.py --output S/angle_check` | PASS with its beta premise verified separately; 0.037 CPU s |
| `python -B /home/amir/Codes/PDE/studies/two_layer_test_risk/C5_INTEGRATION_EXTRA.py` | PASS; six malformed/private-kernel rejection cases and direct 27-node zero-passive-root dynamic moments; 0.028 s elapsed |

The first structural run stopped at my overstrong assumption of literal
identity of the C introduction; the discrepancy and its resolution are
described above. No frozen input was edited to pass a check. The saved checker
was narrowed to assert the exact inspected context-only difference. This did
not alter replay or boundary logic; their saved checker hashes identify the
version actually run. The extra kernel check was first performed as the same
inline script, then retained and rerun as `C5_INTEGRATION_EXTRA.py`.

The focused kernel maximum direct-rule discrepancy was
`5.88418203051333e-15`, below the declared `1e-9` arithmetic enclosure; the
additional zero-passive-root dynamic check had maximum discrepancy
`5.6343818499726694e-15`. These finite tests check correspondence and arithmetic
behavior; the complete analytic argument supplies the uniform bound. The
kernel reports 64 long-double significand bits. The angular helper reproduces
exactly `D8=41272525446939874982/31640625` and
`20636262723469937491/127677049435953561600000000 < 1/1000000`.

Both exact supplied-bit reconstructions recover

```
chi lower = 5358604107658561212253567/19807040628566084398385987584
chi upper = 21597479156841685713774185/79228162514264337593543950336
beta lower = 2797504526179671494928101665/79228162514264337593543950336
beta upper = 2797556156441557459457527739/79228162514264337593543950336
```

Exact comparisons verify the displayed theorem bounds. The raw nodal teacher
projection is approximately `[0.000438788164474,0.000438805496334]`; the
separately charged matching subtraction is approximately
`[0.000167206985003,0.000167247794100]`. Their nodal difference, followed by
the `1/1000000` circle radius, gives the displayed positive chi enclosure.
All decisions were made with rational endpoints, not these decimal displays.

This review performed **no new Gaussian coefficient integration, training,
resolution sweep or search**. Exact reconstruction recomputed constants,
grid checks, covariance errors, primitive error radii and interval contractions
from the supplied bits. It did not re-evaluate the original 86 million Gaussian
nodes. The maintained full-run command and API example were validated by
source/interface correspondence, focused executions, and complete original
evidence, not falsely reported as freshly executed full certificates.

Original commands and raw records remain in the frozen `evidence/` trees.
My complete check records are in
[integration](../../data/generated/two_layer_test_risk/c5_promotion_20260912_v2/integration/),
including exact input hashes, both replay records, structure/boundary records,
the focused command list with captured stdout/stderr, and the extra kernel
record. The review's own checkers are
[C5_INTEGRATION_CHECK.py](C5_INTEGRATION_CHECK.py) and
[C5_INTEGRATION_EXTRA.py](C5_INTEGRATION_EXTRA.py).

## Objections and final disposition

No required correction was found. The dependency packet's legacy offsets and
older C introductory wording are explicitly reconciled above; they do not
change an operative proof or the proposed addition. The unchanged chapter
opening/table are historical orientation rather than a complete new C.5
summary; the preserved current guide provides the accurate later-C.4 and C.5
orientation required by this assignment.

The nine-destination integration is accepted at the frozen hashes. Any
required edit after this verdict needs a new complete integration review;
scientific changes also reopen the paired scientific review. This report does
not certify unread older proofs, execution on unsupported platforms, a fresh
full coefficient run, or promotion outside the remaining gates.
