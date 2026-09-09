# Isolated adversarial editorial and integration review

Date: 2026-09-09

Verdict: **CLEAN**

No required corrections were found in the supplied guide within the requested editorial/integration scope. No changes to the library are proposed or made. This verdict is not a fresh certification of every chapter proof or of the cited papers' proofs.

## Isolation and reviewed version

The only substantive inputs read were the standalone copy at `/tmp/pde-guide-advisory-review.Cj5OAuVD` (`docs/`, `code/`, `Makefile`, `requirements.txt`) and the four primary PDF URLs in its guide. No repository, studies, conversation history, source reviews, external skill files, or other research materials were inspected. No references linked from the four papers were followed. No Git operations, installations, builds, generators, or scientific experiments were performed. The only executed validation was the explicitly permitted copied `make check`.

The guide's SHA-256 is exactly the requested value:

```text
4c11fe4d4f12e7ccb348a0c480f1496c617ca7be04997cfa115811e91b1841b3
```

All 21 supplied files were hashed before and after the check; the hashes agree. The manifest below identifies the reviewed copy, independently of concurrent work elsewhere. This report was created with `apply_patch` in a separate directory created by `mktemp -d`.

## Findings

### Accuracy transfer: valid, with the correct quantifiers

`docs/README.md:89–122` correctly requires compact-time loss approximation and fitting for the same model and admissible joint scaling. After fixing an accuracy, the deterministic population trajectory supplies one finite time independent of width. If the finite loss at that time exceeds epsilon while the population loss is at most epsilon/2, the absolute discrepancy is strictly greater than epsilon/2. This proves exactly the displayed event inclusion, including its strict/non-strict inequality conventions. Uniform convergence in probability on that fixed interval makes its probability vanish.

Thus for each fixed accuracy and confidence level, sufficiently large widths along the admissible step sequence attain the stated accuracy at the selected interpolated time. Corresponding path approximation requires those path observables to belong to the chapter's convergence contract, as the guide explicitly says. There is no exchange of infinite time and width, no claim about arbitrary growing horizons, no universal width for all accuracies, and no endpoint conclusion. The positive achievable-loss version is valid when the population loss approaches that benchmark and the thresholds are shifted accordingly. It is conditional on fitting to that benchmark, not a deduction of fitting from dissipation.

The clocks and interpolants are compatible with `docs/NOTATION.md:70–98`. In particular, `docs/special_data_limits.md:76–96` explicitly converts its sum and half-sum losses to the shared mean-loss convention. The guide does not silently use one physical clock or one step prescription for all chapters.

### Mechanism preservation and learning certificates: appropriately separated

`docs/README.md:18–87` states the intended dense-network target while exposing the mechanisms that approximations must retain: actual Gaussian matrix actions, reuse in both directions, sample correlations, and hidden representation motion. The conditional-response discussion is supported by `docs/gaussian_calculus.md:9–158`; it is not a claim that trained matrix outputs are independent Gaussian coordinates.

The guide distinguishes normalization from forced orthogonality, sufficient activation assumptions from impossibility results, and dataset-dependent constants from uniformity over nearly coincident inputs. Its statements about conflicting identical inputs and achievable risk do not require an interpolation premise to define the dynamics.

The activity distinctions in `docs/README.md:69–77` survive comparison with the actual chapter claims. In particular:

- The shifted-arctangent one-sample theorem states positive feature velocity at every positive finite time, while initial hidden velocities vanish (`docs/global_nonlinear.md:163–170,1755–1789`). Its absolute nonaffinity certificate is separately stated and justified (`1686–1753`).
- Special-data Part I establishes strict progress and positive-time motion without claiming asymptotic fitting; Part II includes fitting and positive-time all-layer motion; Part III establishes initial acceleration and persistent absolute nonaffinity without claiming positive velocity at every later time (`docs/special_data_limits.md:9–19,2088–2144,3711–3769,6377–6398`).
- The Part III activation is an affine term with a bounded nonlinear perturbation, with a large selected gain. Its depth-uniform absolute margins for selected classes do not establish a depth-uniform relative nonlinear contribution. The chapter's compact-support counterexample and final scope language make that limitation explicit (`6230–6398`). The guide does not promote this family into a general correlated-data theorem or equate it with a uniform relative-strength result.

### Chapter roles: no material scope inflation

The eight entries at `docs/README.md:152–159` agree with the supplied statements and decisive scope passages:

| Guide entry | Checked scope and supporting location |
|---|---|
| Finite dynamics | Arbitrary finite depth/batch; C2 activations suffice for global finite GF by energy and continuation. Bounded slopes and initial norm/loss bounds give finite-horizon bounds uniform in width. No population identification or general GD stability follows (`finite_dynamics.md:11–24,111–214`). |
| Gaussian calculus | Finite reuse identities and exact moments; the feature-ascent limit fixes depth, step count and nonzero feature step, with order-one stored readout and its stated activation assumptions. It supplies no growing-program or GF theorem (`gaussian_calculus.md:253–350,1719–1812`). |
| Arctangent limits | One sample, label one, tiny stored readout. L2 is global on compact physical intervals under `eta_n sqrt(n) -> 0`; L3 is local under `eta_n=n^-2`. The separate capped population/width result is global on finite feature-time horizons for each fixed cap and is explicitly not the original optimizer (`arctan_limits.md:1–128,690–904,1306–1482,1730–1807`). |
| Global nonlinear | The particular activation `1+arctan(z)/10`, one datum `(1,1)`, and each separately fixed hidden depth L>=3. The theorem includes raw GD at `n^-2`, finite GF, fitting, named observations and activity; it does not take a joint growing-depth limit (`global_nonlinear.md:1–180,1791–1796`). |
| Special data | The actual admissible sets are explicit: Part I correlations 0 or -1 with opposite binary labels; Part II each fixed -1<=rho<1 with equal binary labels; Part III three separated normalized samples, binary labels, and L>=2 with its selected shape/gain. The guide directs the reader to the separate clocks and activity/fitting claims (`special_data_limits.md:1–125,137–151,2088–2144,3511–3776,6377–6398`). |
| Linear dynamics | L3, one input, identity activation and variance-one stored readout. A global operator population, finite GF/GD approximation and fitting coexist with a restricted nonclosure theorem. GD allows any deterministic step sequence tending to zero. Rooted operator observations do not assert empirical neuron-coordinate laws or cross-space operator-norm convergence (`linear_dynamics.md:13–143,719–828`). |
| Continuous depth | Scalar residual particles, explicit parameter assumptions A1–A2, and exact GF. The positive result is joint width/depth convergence on fixed training horizons with the specified initialization. No dense Gaussian-matrix, GD-step, or fitting theorem is claimed (`continuous_depth.md:1–103,329–391,1474–1490`). |
| Finite optimization/controls | Canonical finite L3 arctangent GF and raw GD fitting with finite endpoints on the stated Gaussian events. The separate metric projection has an integrated L1 middle-equation defect and exactness for a sufficient cap with its constant multiplying sqrt(n). It supplies no projection population or GD theorem (`finite_optimization_and_controls.md:183–233,329–371,741–778,951–990,1032–1123,1202–1231`). |

The guide's treatment of restartability is compatible with the stated admissible domains. The nonlinear statements typically restart from reached full states; the linear and continuous-depth chapters state broader domains. The guide does not upgrade these into arbitrary-state nonlinear well-posedness. The examined cap-removal passages construct and identify a continuing path rather than merely noting an endpoint (`global_nonlinear.md:996–1086,1233–1258`; `special_data_limits.md:5045–5106`).

### Negative statements and representations: no unjustified impossibility claim

`docs/README.md:170–199` preserves the distinction between scalar closure and operator/function representations. The linear obstruction requires its specified bounded-contraction encoders, width-uniform degree bounds, and state-universal polynomial or specified analytic identities. It is not an obstruction for arbitrary encoders or only the Gaussian-initialized trajectory (`docs/linear_dynamics.md:719–828`). The chapter even gives an unrestricted transport-profile realization and explains that its initialization uses the future output path (`1059–1138`).

Likewise, the same-space multiplication and coefficientwise jet obstructions have explicit domains, and the zero-Taylor-radius example does not exclude a smooth autonomous ODE (`docs/gaussian_calculus.md:1739–1812`). The guide accurately preserves the value of these intermediate results without presenting them as either population theorems or general representation prohibitions.

### Primary-source orientation: narrow descriptions supported

Only the four permitted texts were used. The following are contextual validations, not imported theorem hypotheses or full proof audits.

- **Yang–Hu**, guide `208–215`: the parameterization/classification discussion, Theorem 5.1 and equations (8)–(9) support feature-learning and discrete-training limit formulas. Section 5.2 explicitly discusses dependence between a reused middle Gaussian matrix and its transpose. The fixed-time/step description supports the guide's statement that a refining-mesh target requires additional uniform control. It does not justify dismissing tensor-program methods, and the guide does not do so. [Permitted paper](https://proceedings.mlr.press/v139/yang21c/yang21c.pdf).
- **Nguyen–Pham**, guide `217–224`: the abstract, trajectory comparison in Theorem 15/Corollary 17, and Section 7 support neuronal embeddings, trajectory approximation and scoped optimization conclusions. Section 7.1 uses hidden-sum normalization by the preceding width; Section 7.3 includes special correlated initialization/diversity and additional assumptions, including a convergence assumption. The guide's wording about specified setups does not assert unconditional optimization from ordinary iid dense Gaussian initialization. [Permitted v3](https://arxiv.org/pdf/2001.11443v3).
- **Celentano–Cheng–Montanari**, guide `226–232`: the abstract and Theorem 2 establish bounded-horizon trajectory limits under proportional input/sample growth. Section 4's equation (24) explicitly fixes the number of hidden units in its shallow-network application. The guide correctly identifies a rigorous DMFT result and a different limit; it does not reduce this work to formal equations. [Permitted paper](https://web.stanford.edu/~chen96/papers/fom_dynamics.pdf).
- **Chizat–Bach**, guide `234–240`: Theorem 2.6 supplies many-particle approximation, Section 3 supplies qualified optimization results, and Section 4.2 supplies single-hidden-layer applications. These results retain their own hypotheses; in particular the stated optimization theorems include a convergence assumption. Appendix C.4, Lemma C.15 and its proof give a direct approximation/accuracy bridge under population objective convergence. This supports the guide's deliberately limited precedent claim and its rejection of novelty for the logical strategy. The guide does not state an unconditional shallow or deep fitting theorem from this citation. [Permitted v2](https://arxiv.org/pdf/1805.09545v2).

`docs/README.md:187–189,203–206,242–247` explicitly rejects comprehensive literature-exclusion and priority claims. The inspected descriptions do not dismiss rigorous multilayer mean-field or rigorous DMFT results, or imply that an architecture difference makes them scientifically valueless.

### Self-containment and omitted work

The guide and notation were read in full. All local Markdown file links resolve inside the copied `docs/` and `code/` boundary. The displayed arctangent fragment links have matching explicit anchors. Text searches found no exploratory-file dependency, external local path, or required generated artifact. The generic mention of an earlier report at guide line 163 expressly removes such a dependency; the historical-environment comment in `requirements.txt:1` supplies no external requirement.

The source-identification, cap-removal, algorithm-comparison and activity components named by the guide are present as internal chapter sections, with the examined decisive passages matching their claimed roles. This is an integration assessment of their presence, scope and dependencies, not a statement that every intervening estimate has been re-proved in this review.

`docs/README.md:124–146,249–262` treats passive-input/generalization questions and broader depth/data limits as further obligations. It explicitly excludes a general correlated-data uncut L3 arctangent population theorem, a general input-population limit, a dense joint depth/width/time theorem and a generalization theorem. The finite endpoint and auxiliary-cap results are not used to imply those missing theorems already exist.

## Exact local read coverage

Line numbers are one-based in the hashed standalone copy. Ranges below are substantive text actually read, with overlapping repeat reads consolidated. In addition, all supplied files were included in full-file hash and dependency-text scans, all chapter headings were inventoried, and the supplied checker read all 19 Markdown/Python files. Those machine scans are not counted as reading every proof or implementation line.

| File | Substantive read coverage |
|---|---|
| `docs/README.md` | 1–262, complete; 89–262 reread with line numbers. |
| `docs/NOTATION.md` | 1–98, complete. |
| `docs/finite_dynamics.md` | 1–214, complete. |
| `docs/gaussian_calculus.md` | 1–350; 1719–1812. |
| `docs/arctan_limits.md` | 1–128; 690–904; 1306–1486; 1730–1811. |
| `docs/global_nonlinear.md` | 1–180; 812–869; 996–1086; 1226–1259; 1686–1796. |
| `docs/special_data_limits.md` | 1–361; 2088–2145; 3500–3777; 4985–5107; 5446–5484; 6013–6038; 6096–6127; 6230–6398. |
| `docs/linear_dynamics.md` | 1–143; 719–828; 1059–1166. |
| `docs/continuous_depth.md` | 1–103; 329–391; 1474–1490. |
| `docs/finite_optimization_and_controls.md` | 1–95; 183–233; 329–371; 635–674; 741–822; 951–990; 1032–1129; 1202–1231. |
| `code/README.md` | 1–165, complete. |
| `code/tools/check_library.py` | 1–100, complete. |
| `code/tests/test_library_boundary.py` | 1–58, complete. |
| `Makefile` | 1–9, complete. |
| `requirements.txt` | 1–2, complete. |
| Other six Python files in the manifest | Hash/dependency scans and execution by the supplied check only; no line-by-line implementation audit. |

Dependency-text searches covered URLs, local Markdown links and HTML anchors, outside paths, and terms including `studies/`, `exploratory`, `report`, `campaign`, `supplement`, `external`, `unproved`, `TODO`, `FIXME`, `omitted`, `elsewhere`, and `prior review`. Matches were interpreted in context, not treated automatically as defects. A final hidden/unignored inventory of `docs/` and `code/` still contained only the 19 supplied files, with no bytecode files.

## Exact primary-source access coverage

Coverage was passage-level through the browser's PDF text reader. The following records the access requests precisely; the reader also returned surrounding text and discontiguous search excerpts, sometimes including incidental contents, proof snippets, experiments or bibliography. None of that constitutes full-page or full-proof review. Offsets refer to the reader's zero-based extracted text lines, not manuscript line numbers. Initial opens requested each exact permitted URL without a line offset. No internet search queries or other URLs were used.

| Primary text | Subsequent text-reader opens | In-document find terms | Decisive passages assessed |
|---|---|---|---|
| Yang–Hu, PMLR PDF, 11 PDF pages | 423; 476; 782 | `any fixed` (no match); `4.1.` | Parameterization/classification in Sections 2–3; Definition 4.1; Section 5.1/Theorem 5.1, equations (8)–(9), and fixed-step qualification; Section 5.2 matrix reuse. Decisive text is on PDF pages 2–7. |
| Nguyen–Pham v3, 125 PDF pages | 0; 2490; 7630 | `correlated`; `Theorem 6` (no match); `Theorem 18` (no match); `Theorem 38.`; `Theorem 15.`; `Theorem 38 (` | Abstract; trajectory distance and Theorem 15/Corollary 17 on PDF pages 19–21; Section 7 introduction/model on pages 43–44; assumptions and Theorem 38 on pages 45–46; Corollary 40 on page 48. Returned find snippets also exposed parts of the comparison/proof discussion, without proof auditing. |
| Celentano–Cheng–Montanari, 83 PDF pages | 0; 652 | `hidden units`; `Theorem 2.` | Abstract; Theorem 2 and Remark 3.2 on PDF pages 8–9; Section 4, equation (24), and its planted-signal discussion on page 9. Returned theorem-search excerpts also included discretization and tightness discussion from later pages; these were not audited. |
| Chizat–Bach v2, 32 PDF pages | 396; 579 | `Theorem 2.6`; `4.2` | Theorem 2.6 on PDF page 5; structural/initialization discussion and Theorems 3.3/3.5 on pages 6–7; single-hidden-layer applications on pages 8–9; Lemma C.15 and its finite-accuracy argument on pages 25–26. Other returned appendix snippets were not audited. |

Remote PDF byte hashes were not available from the text-reader interface and are not claimed. Their exact permitted URLs and version suffixes above identify the accessed sources; only the copied local files have byte-level hashes here.

## Checks performed

From the copied library directory, ran exactly:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 make check
```

The supplied Makefile additionally uses Python `-B` and preserves the one-thread/no-bytecode test settings. Exit status was 0. Output reported:

```text
Library boundary and local links checked: 19 files.
Ran 52 tests in 0.149s
OK
```

These are the supplied small deterministic structural, finite-network and exact-moment tests. They validate their stated contracts and do not establish population-limit proofs. No additional tests or scientific computations were introduced. The declared NumPy pin was read; no installation or separate verification of the runtime package version was performed.

## SHA-256 manifest

Paths are relative to `/tmp/pde-guide-advisory-review.Cj5OAuVD`. The following values were identical in the initial and post-check reads.

```text
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
4c11fe4d4f12e7ccb348a0c480f1496c617ca7be04997cfa115811e91b1841b3  docs/README.md
19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead  docs/arctan_limits.md
0930e1b2a4c219749cd1994ffb657093aea0a103b2d4a414c21bd697604d5362  docs/continuous_depth.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
a12a4f2541dd989a01920541f07ce8f80058b88d3e19db65c4b376c1fcf6653e  docs/finite_optimization_and_controls.md
cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e  docs/gaussian_calculus.md
becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95  docs/global_nonlinear.md
36988f8175a433264671e1d980df752c8c52b34e1802de1c3d560d3ed3d8f41b  docs/linear_dynamics.md
e491ea163cf325ced50a3f1d19ab79cf9f84df85977ad644b68f4c96775e36ea  docs/special_data_limits.md
0b855079acbe28a96b6bde2a0c5727a6ab02b663ca765d3145409864e8216a93  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a  code/tests/test_library_boundary.py
c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92  code/tests/test_numerical_contract.py
7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6  code/tools/check_library.py
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
```

Required corrections: **none**.
