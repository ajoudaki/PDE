# Original isolated integration review of proposed C.4.7

**Verdict: PASS for the frozen proposed edition and the integration scope below.**
The complete new material is present in canonical notation, the declared older
interfaces agree, the standalone checks pass, and exact inverse assembly
recovers every frozen base document. I found no required integration correction.
This is not a fresh audit of every older proof, a verdict on another review,
or authorization to edit the established edition.

## Identity, isolation and authorization

- Reviewer: `/root/p2_integration_review`, a fresh isolated context distinct
  from all seven author/assembler identities and the selector in the manifest.
- Assignment: `studies/trained_data_response/P2_INTEGRATION_REVIEW_ASSIGNMENT.md`,
  read completely; SHA-256
  `98a34f3dd935cdcc0d68571d112c53065f7b1cd42ccb4bc921bf8bc09c98906e`.
- Manifest: `studies/trained_data_response/P2_PROMOTION_MANIFEST.json`, read
  completely; expected and observed SHA-256
  `7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e`.
- The launch supplied only the neutral assignment, frozen manifest identity,
  input boundaries and output ownership. I did not read study README/history,
  author discussion, earlier verdicts, scientific-review reports, another
  integration report, Git history, or another study. No reviewer findings were
  obtained before freezing this original report. Progress messages were metadata
  only. The ancillary file's assembler read-scope metadata was not treated as
  this reviewer's reading or as evidence of correctness.
- I read all of `AGENTS.md`, `RESEARCH_WORKFLOW.md`, the required
  `/etc/codex/skills/solve-math-rigorously/SKILL.md` and
  `/etc/codex/skills/investigate-conjectures/SKILL.md`, and the applicable
  `adversarial-audit.md` and `research-contract.md` references. Truncated initial
  reads were repaired. This was an isolated review, not author startup or a
  new conjecture/experiment campaign.
- All writes were this report or the assigned scratch
  `data/generated/trained_data_response/p2_20260911_02/integration_review/`.
  No source input, established file, Git index, branch or commit was changed.
  No training or parameter sweep was run. Before writing, read-only Git metadata
  showed HEAD `3c9feacb0befd20fd57aa577494af36286af5758` and no tracked changes
  in the scoped inputs/docs, with optional Git locks disabled. This is metadata,
  not use of history as scientific input.

## Exact read scope

I read every line of the following frozen new inputs:

| File in `studies/trained_data_response/` | Lines |
|---|---:|
| `P2_SECTION.md` | 1–2461 |
| `P2_PROPOSED_GUIDE.md` | 1–284 |
| `P2_EDITION_ANCILLARY.json` | 1–111 |
| `P2_EDITION_BUILD.py` | 1–372 |
| `P2_PROMOTION_CHECK.py` | 1–102 |
| `P2_PROMOTION_TANGENT_CHECK.py` | 1–197 |
| `P2_PROMOTION_REFERENCE_CHECK.py` | 1–56 |
| `P2_PROMOTION_RADIAL_CHECK.py` | 1–67 |
| `P2_PROMOTION_RECIPE.md` | 1–66 |

The old scientific material was read from the exact frozen dependency packet.
The complete base guide and notation were read, as were the complete selected
units below. Line numbers in the middle column refer to
`P2_PROMOTION_DEPENDENCIES.md`; the last column gives their source-edition span.

| Complete units read | Dependency packet | Frozen established source |
|---|---|---|
| Packet preface, complete base guide and complete notation, including markers | 1–392 | `docs/README.md` 1–278; `docs/NOTATION.md` 1–98 |
| Finite dynamics introduction and §§1–4 | 393–623 | `docs/finite_dynamics.md` 1–227, plus packet separators |
| III.F.1–III.F.11, including probability, source, singular-query, carrier, HS, scalar differential and multiplier proofs | 624–1169 | `docs/special_data_limits.md` 3785–4326, plus packet separators |
| Global nonlinear A.1–A.4 | 1170–1228 | `docs/global_nonlinear.md` 1840–1898 |
| Complete C.2 weighted response/tail proof | 1788–2308 | `docs/global_nonlinear.md` 2924–3440, plus packet separators |
| Entire C.4 model/local theorem and complete C.4.1–C.4.2 | 2309–3098 | `docs/global_nonlinear.md` 3836–4625 |
| Entire C.4.5 statement, quantitative margins and limitations; complete C.4.5.1 reference/endpoint/activity/certificate, C.4.5.2 source construction/tails and C.4.5.3 transfer | 3737–5370 | `docs/global_nonlinear.md` 5264–6897 |
| C.4.6 introduction and entire theorem; complete C.4.6.2 proof units 1–2, including exact tangent generator and boundedness/strong continuity | 5371–5800 | `docs/global_nonlinear.md` 6898–7327 |
| Complete C.4.6.4 unit 7 and final interpretation/nonlinear boundary | 7388–7434 | `docs/global_nonlinear.md` 8915–8959, plus packet closing marker |

**Unread complement of the dependency packet:** lines **1229–1787**
(B introduction and B.1), **3099–3736** (C.4.3–C.4.4), and
**5801–7387** (the remaining C.4.6.2 propagator proof, C.4.6.3 source proof,
and C.4.6.4 proof units 1–6). Thus the C.4.6 arbitrary-fixed-horizon capture
theorem is an established interface here, not a fresh complete review of its
cavity and finite-capture proof. B.1 and C.4.3 were used only through the
declared interfaces and the complete selected C.4.2/C.4.5 explanations. No
unread proof is represented as independently audited.

Outside these selected established spans, document access was for hashes,
inventory, exact assembly/inverse preservation, and link/heading metadata.
The other chapters' scientific bodies were not reviewed. The complete new
assembled section was verified byte-for-byte against the fully read new source;
all seven changed navigation passages were read in exact old/new form, and
the assembled C.4.6/C.4.7 join and concluding boundary were inspected. This
does not constitute a whole-book proof audit. No additional scientific input
was needed or retrieved outside the assignment.

## Frozen input hashes

All values below were verified, including the ten established documents and
the shared instructions. The manifest itself was separately checked against
the launch's expected hash. A final post-write recheck is retained in the
assigned scratch as `final_input_hash_check.json` before communicating the
report hash.

| Flat study input | SHA-256 |
|---|---|
| `P2_SECTION.md` | `707a7d42eb2e2e58ae92fa2ee8e25343977224fe1307675e7c0c82609b0571f0` |
| `P2_PROPOSED_GUIDE.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `P2_PROMOTION_DEPENDENCIES.md` | `a68aaa0107f4f73cd0df22af8a8f3867b1c76b515c5d0a920ef387ff2d32acd3` |
| `P2_EDITION_ANCILLARY.json` | `7aae13594bc1e5139d8d67cb33c3cc2f1b2e7f5dd5cafaaaae5ebededcb1dedc` |
| `P2_EDITION_BUILD.py` | `fac14c4e375a4504c71c868a14cf9f1c6490cbc2c341731d1725f514411ab5ac` |
| `P2_PROMOTION_CHECK.py` | `9a1526c6a030ac379ec1e1ae6f041a094464ad56ef9d2112f98ca7f254150549` |
| `P2_PROMOTION_TANGENT_CHECK.py` | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P2_PROMOTION_REFERENCE_CHECK.py` | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| `P2_PROMOTION_RADIAL_CHECK.py` | `91ef15a16d42063dc210e82055da3a855c4d9e9e6694b90db8b0191f3390998a` |
| `P2_PROMOTION_RECIPE.md` | `1fc72c36d72a574b37a4e095eecf1b7e3506068497a1012f3348928c20a697eb` |

| Established/shared input | SHA-256 |
|---|---|
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | `88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721` |
| `docs/arctan_limits.md` | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` |
| `docs/gaussian_calculus.md` | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| `docs/global_nonlinear.md` | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| `docs/linear_dynamics.md` | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

The runner also compared all seven marked dependency excerpts with their
exact source bytes and recorded their individual excerpt hashes. This is
source correspondence, not proof verification of the unread complement.

## Scientific integration attacks and outcomes

### Model, metric, state and observations

I substituted the new raw equations into finite-dynamics (1)–(5) with two
hidden layers, normalized input `u=x/sqrt(2)`, unhalved probability-law loss
and mobilities `(n,1,n)`. The first/readout metric factors are `1/n`; the
middle factor is ordinary Frobenius. A population rank is represented by
`a b^T/n`, whose Frobenius pairing is the product of the two normalized
same-layer pairings. The source's loss factor `-2`, signs, final row vector
`u`, and middle rank normalization agree throughout. **PASS.**

The initialized Gaussian action remains bounded with its actual adjoint and
joint generated realization. Only `K` is HS. The stronger HS comparison is
proved by the rank difference bound and `||K||op<=||K||HS`, rather than
silently identifying an arbitrary bounded action with an HS action. The
finite initial readout is retained in actual GF and added to the proxy's
initial parameters. The zero readout used in the fresh-root extraction is
explicitly auxiliary. **PASS.**

I checked that the state assertion compares finite paths and proxies on the
same initialized arrays; it never subtracts a finite matrix and an operator
on different carriers. The fixed-program W2 observations include finite
typed action compositions, Lipschitz coordinate operations, bounded gates
times named L2 fields, and quadratic/paired contractions. Unbounded products,
clocks and inverse-gate fields need the additional proofs actually supplied.
Joint second moments and truncation, rather than an L2 norm bound alone,
justify these observation passages. **PASS.**

### A: reached nonlinear construction and continuity

Here A denotes the new strong-flow/law-continuity claim, B finite-GF capture,
and C the nonlinear response bridge; these are descriptive review labels.

I attacked the central source estimate at vanishing atom mass, repeated
queries, singular covariance, current versus past source slots, and
nonuniform time steps. N2–N8 are the literal specialization of C.2 and
III.F's named-source convention. The current beta row has one distinguished
direct slot, including at duplication/rank loss. Old pulses retain
`h_s p_b`, and N17 supplies the past-source density needed in N27a.
Consequently the law transport proof averages `e_b^(1/16)` with its mass;
it does not take a maximum of far-contaminant costs or introduce `1/p_b`.
The Gaussian difference coupling N21 follows from joint source covariances,
not Lipschitzness of a covariance square root or continuity of a Gram inverse.
**PASS.**

I checked the chronology of both cap inductions. The unsuccessful absolute
estimate N19 is explicitly not a global bootstrap. The physical reference
clock cap is instead obtained by finite same-array fresh-root forcing,
width first and forcing second, including fixed-graph source continuity at
zero variance. N39–N44 control recomputed residuals as well as feature and
action changes; forcing does not inherit an assumed energy identity.
The direct root norm is retained until its width limit. The raw-to-clock
Taylor defect N32 is differentiated before estimating, so N36 retains the
source mass and sums to `O(h_max)`. N48–N51 use previously bounded raw rows,
then construct the current alpha and beta. The subsequent changed-law
induction uses a separately fixed reference raw cap and same-mesh law
comparison N30a. Neither induction assumes a tail for its unconstructed
current query. **PASS.**

I checked the distinction between a neighborhood of reference paths and
Cauchy convergence of changed-law paths. The latter is independently proved:
NC uses one cutoff factor; exponential reached tails give the Osgood
inequality `s' <= L s log(e/s)` with exponent `exp(-Lt)>0` for this finite
horizon. No condition comparing tail exponent with the full horizon is
needed. Fine Euler paths and finite laws are Cauchy in the complete raw/HS
path norm. Joint field/law continuity passes their integral equations to a
strong C1 equation. Energy and the readout bound then belong to that actual
equation. Uniqueness against any competing strong raw solution uses only
the constructed path's tails. Restart is from reached states on the
remaining interval with retained primitives, not existence from every
ambient operator state. **PASS.**

### B: actual finite GF, law limits and nonlinear mechanism

I checked the fixed-oracle order in NAP: choose the finite interval partition,
cutoffs and required incoming accuracies backwards; choose one comparison
law and one raw mesh; only then take width. The factor
`exp(C(1+R) ell)` can be controlled against `exp(-a'R)` on each short
interval because `C ell<a'/2`. The finite number of intervals permits one
fixed program. This argument does not apply a fixed-program theorem to a
transcript growing with width. Finite GF has exact Borel loss integration
and a smooth finite-dimensional field, and its energy bounds are independent
of the actual law on the compact bounded-label domain. **PASS.**

The same comparison covers a fixed nonatomic Borel law and any deterministic
empirical sequence converging in W1, with arbitrary width growth. The iid
extension uses compact partitions, cell-frequency variance and a union bound
with initialization/proxy events; it does not demand empirical total-variation
convergence. Both width/sample limit quantifiers remain as stated. No
uniform-in-law finite failure probability or finite-width rate is inserted
by the guide. **PASS.**

All two-layer weights train in the new equation, both matrix orientations
are retained, and laws are open relative to all bounded-label circle laws.
An off-axis contaminant with arbitrarily small mass is allowed; no rank,
minimum-weight or orthogonality constraint was substituted for that class.
The reference remains an anchor for a proof, not a replacement for the
changed-law dynamics. **PASS.**

### C: exact response interface and uniform nonlinear remainder

The passive-tail argument uses a probe on the same mesh, with its only
inverse mass paid by the law modulus. Its resulting exponential marginal
moment is sufficient for the radial estimate. I checked
`|z| sech^2(z)<=1/2`, the sign-independent radial upper bound, Jensen over
time and law, and Cauchy–Schwarz with the two-dimensional Gaussian root.
The choice of gamma gives a uniformly finite `exp(gamma W_mu^2)` moment.
The weighted products then have a third moment, yielding uniform
integrability of their squares. No Lp action bound beyond L2, and no
unproved exponential moment of a supremum of all queries, enters. **PASS.**

The new absolute clock `F(w)` differs from C.4.6's `F(w)-F(g)` by one
fixed L2 field. Its variation, raw conversion and generator therefore
agree exactly. I compared the new directional-fields display with
C.4.6.T14, the generator with the complete P8–P11 product differentiation,
and the signed source with T5. The inverse gate, input coordinate, residual,
factor two and subtraction of the reference law all match. The old
finite-first derivative is not redefined through the new population map.
**PASS.**

I tested the non-Frechet obstruction explicitly at the proof level: bounded
sets of L2 directions need not have uniformly small square tails. The
argument instead obtains compact response directions from the continuous
atom-forcing map into `C([0,T];V)`, its compact closed convex hull, and the
bounded linear solution map. A finite net proves the required uniform tails.
The backward cross term `d[phi'(Z_new)-phi'(Z_*)]` is separately truncated.
The artificial response readout is allowed to be unbounded pointwise:
the one-bounded-endpoint comparison uses the actual curve's bounded
readout. Thus this is a uniform small-o first-order remainder along the
specified compact direction family, not an ambient L2 Frechet or quadratic
remainder assertion. **PASS.**

For the finite nonlinear display I checked the exact triangle inequality.
At each fixed positive epsilon, both finite prediction errors divided by
that epsilon vanish in probability; the actual finite derivative converges
by the established C.4.6.T10 interface. Only after that width limit is epsilon
sent to zero. Population uniformity over contaminating laws is preserved,
while the finite probability statement fixes each law first. There is no
joint epsilon/width rate or width-uniform finite remainder. **PASS.**

### Risk/activity, summaries, placement and scope

C.4.7.7 restricts inherited risk/activity to the binary subclass intersected
with the C.4.5 ball of radius `exp(-exp(3000))`. I read the complete reference
activity/certificate and transfer proof. Its strict bounds pass to actual GF
with zero algorithmic defect, and then to the newly constructed population
flow by whole-circle predictions and paired hidden observations. Risk is
claimed at 40 and paired hidden displacement at `1/200`; there is no claim
of activity at 40 or for every bounded-label law. **PASS.**

All seven navigation changes preserve the old local C.4.1–C.4.4 scope,
C.4.5's separate endpoint/raw-GD conditions, and C.4.6's arbitrary separately
fixed-horizon derivative theorem. The new nonlinear claim is repeatedly
restricted to the neighborhood and physical GF interval `[0,40]`. It is
not strengthened to arbitrary-horizon nonlinear continuation, endpoint
selection, universal fitting, expected-risk expansion or feature superiority.
**PASS.**

Appending one C.4.7 after C.4.6 is a coherent destination: it consumes the
reference/transport interfaces and supplies the missing nonlinear continuation
and small-contamination remainder without changing those older theorems.
The source argument, completion and variation proofs are substantive and
fully present. There is some local repetition, including deriving weaker
passive tails from active tails after stronger passive estimates are already
available; it causes no conflicting assumption or duplicated scientific
claim that requires correction. No study document or historical verdict is
a canonical mathematical dependency. **PASS.**

## Standalone execution and independent preservation checks

Working directory: `/home/amir/Codes/PDE`. The fresh runner command was:

```sh
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/integration_review/standalone_run_01
```

It exited **0**. I inspected each executed command, working directory, exit
code and complete log. The runner invoked exactly:

1. `/usr/bin/python -B /home/amir/Codes/PDE/studies/trained_data_response/P2_EDITION_BUILD.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/integration_review/standalone_run_01/edition --manifest /home/amir/Codes/PDE/studies/trained_data_response/P2_PROMOTION_MANIFEST.json`, from the repository root; exit 0.
2. `/usr/bin/python -B P2_PROMOTION_TANGENT_CHECK.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/integration_review/standalone_run_01/edition/standalone/data/generated/trained_data_response/checks/tangent`, from that standalone artifact's `validation` directory; exit 0.
3. `/usr/bin/python -B P2_PROMOTION_REFERENCE_CHECK.py`, from the same standalone `validation` directory; exit 0.
4. `/usr/bin/python -B P2_PROMOTION_RADIAL_CHECK.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/p2_20260911_02/integration_review/standalone_run_01/edition/standalone/data/generated/trained_data_response/checks/radial`, from the same standalone `validation` directory; exit 0.

The validation processes used empty `PYTHONPATH`, disabled bytecode, and
one OpenBLAS/OpenMP thread. Observed versions: Python 3.10.12, NumPy 1.26.4,
SciPy 1.13.0. The three scripts were copied unchanged and their hashes checked.
Reading their complete bodies confirms that their numerical inputs are
supplied constants. The only source-content reads in those scripts hash the
script itself; they do not load retained data, studies or Git. The reference
script imports only `fractions`; tangent/radial use installed numerical
libraries. I independently verified that the reference script is exactly the
complete Python certificate printed in C.4.5.1.

| Check | Actual result |
|---|---|
| Tangent finite differences with nonzero readout | Errors `1.0292819331e-6`, `2.5732050750e-7`, `6.4330121850e-8`, `1.6082636076e-8`; required ratios and final tolerance pass |
| Unhalved raw-loss metric directional derivative | Error `7.90068011014e-12`, below `1e-9` |
| Compatible singular semigroup identity | Maximum tested error `1.52654444202e-14`, below `2e-12`; incompatible nilpotent negative control also passes its required growth assertion |
| Exact rational Gaussian certificate | `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; all exact rational assertions pass |
| Radial identity at correlated/repeated inputs with conflicting labels | Error `5.55111512313e-17`; all four upper-bound slacks positive |
| Independent complex-step loss dissipation | Error `5.55111512313e-17`, below `1e-12` |

These are deterministic algebra/constant checks, not empirical training
evidence or verification of the uniform analytic source estimates.

I additionally wrote and ran the scratch-only independent correspondence
check:

```sh
python -B data/generated/trained_data_response/p2_20260911_02/integration_review/independent_assembly_check.py
```

It exited **0**, independently reconstructed the declared changes, reversed
them and compared every base byte, checked final document/script hashes,
the displayed reference certificate, guide/affected links, original equation
tags and the artifact inventory. There were **ten** copied documents,
**seven** replacements, **114** unique new `C.4.7.*` equation tags and no
old equation-tag changes. The section starts at assembled chapter line
**8976**, and its entire 2461-line body equals the frozen source. The builder
also verified **154** balanced display environments in the new section.

Only `docs/README.md` and `docs/global_nonlinear.md` differ from the base:

| Assembled file | SHA-256 |
|---|---|
| `docs/README.md` | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| `docs/global_nonlinear.md` | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |

The other eight document hashes equal the frozen input table. Removing the
exact newline-plus-section suffix and reversing the seven replacements in
reverse order recovers **all ten** original files exactly. The assembled
guide equals `P2_PROPOSED_GUIDE.md` exactly.

All six newly affected local links resolve to the new C.4.7 fragment. Of the
complete guide's 17 links, 12 local links resolve, four external literature
URLs are preserved without retrieval, and one preexisting interface is
explicitly excluded: **`docs/README.md` → `../code/README.md`**. That link
already exists in the frozen base; the artifact is expressly docs-only and
does not contain `code/`. No new proof or executed validation needs that
guide link. This is a declared, preserved exclusion, not a claim that every
book link is self-contained. Other older chapter links were not broadly
audited, and old chapter bodies were not reread beyond the declared scope.

The standalone inventory has no `studies`, `.git`, symlinks or bytecode
cache. Its data files are the fresh tangent/radial outputs generated by this
run, not retained inputs. The assembled documents and copied validation
scripts contain the scientific/algorithmic content required for this
edition's check without study history. The builder/runner necessarily read
the frozen packet during assembly; the standalone validation does not.

## Retained evidence and completion

All evidence paths below are under
`data/generated/trained_data_response/p2_20260911_02/integration_review/`.

| Evidence | SHA-256 |
|---|---|
| `standalone_run_01/validation.json` | `9d70a76fb520f5a420ab69fc8d4f6c89e2fc7851f7f020ed40ed61e2eb300e50` |
| `standalone_run_01/edition/validation.json` | `671a6a7113eb88395284ea1d57e5bf871436ad791dd5c35dad1eaa7ae89972e2` |
| `standalone_run_01/edition.log` | `27e8dad40b146ee34a30eb66b9f002708266c16d522fa831b39474d885cf0010` |
| `standalone_run_01/tangent.log` | `3e732b930cf23d9adfa4d21904e4f23e66ac89325fef724cec31b682bb38f42b` |
| `standalone_run_01/reference.log` | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` |
| `standalone_run_01/radial.log` | `15e0d9cc3b713eb024fd9e68bb33e1404bd5eb5e66f78e0c947485bb8c611664` |
| `independent_assembly_check.py` | `d6ff181a353bd0293c0819af96a12670e00e56dd0992c16757d5f5f803672fbf` |
| `independent_assembly_check.json` | `d25691499701de713a21a8703e3af58141d1c2c6d64f26f78827112bb0c0819d` |

Component verdicts are PASS for new scientific assembly, notation/model
interfaces, A–C scope, nonlinear mechanism, risk/activity restrictions,
guide/placement, declared link scope, deterministic scripts, standalone
execution and exact preservation. **Unresolved required objections: none.**
**Required corrections: none.** The enormous positive radius constants and
the expressly fixed nonlinear horizon are limitations of the stated result,
not missing scope claims.

The assigned integration review is complete. This is the original full
report, frozen before receiving other findings and not to be overwritten.
Its hash is communicated separately after the final frozen-input check;
the post-write verification record also retains that report hash. Any later
required integration correction needs a fresh complete review of the corrected
scope; scientific changes also reopen the paired reviews. Approval and actual
promotion remain separate workflow gates.
