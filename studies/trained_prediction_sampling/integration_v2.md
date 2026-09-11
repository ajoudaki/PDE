# Independent integration review of the frozen C.4.8 version 2

**Verdict: COMPLETE — PASS for the assigned integration scope.** I found no
required scientific or presentation correction and no missing input within
this scope. The complete new section, exact summary edits, finite normalization,
source interfaces, navigation, and preservation checks pass. This is not a
whole-book proof audit, a replacement for either paired adversarial review, or
approval to change the established book.

Reviewer: fresh isolated agent `/root/integration_v2`, distinct from every
author, assembler, contributor and selector named in `integration_packet_v2.md`.
Review date: 2026-09-11. Candidate SHA256:
`98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928`.

## Isolation and complete read coverage

The only scientific inputs were the neutral assignment and the exact materials
it authorizes. I did not read study README/history, earlier proposals or reports,
selection findings, paired-reviewer findings/messages, other studies, chats or
Git history. I did not delegate any review component or contact another reviewer.
No Git operation, maintained book/code edit, training run or parameter sweep was
performed. Writes were confined to this report, the assigned
`data/generated/trained_prediction_sampling/integration_v2/` scratch, and the
fresh `integration_v2_edition/` directory.

I personally read these process sources completely:

- `AGENTS.md` and both parts of `RESEARCH_WORKFLOW.md`.
- `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- `/etc/codex/skills/investigate-conjectures/SKILL.md`, and its applicable
  `references/research-contract.md` and `references/adversarial-audit.md`.

The independent-review instructions replace author startup reading. I applied
the research-contract and adversarial checks to scope and proof claims; there
was no resumed research-state synthesis, proof-search campaign or experiment
requiring the other optional references.

Scientific and implementation reads were:

| Input | Complete content read |
|---|---|
| `integration_packet_v2.md` | Entire neutral assignment |
| `proposal_C4_8_v2.md` | All 1,552 lines, in blocks 1–410, 411–820, 821–1230, 1231–1552 |
| `standalone_v2/docs/global_nonlinear.md` | All new lines 11440–12991, independently read in blocks 11440–11849, 11850–12259, 12260–12669, 12670–12991 |
| `promotion_edits_v2.json` | All 23 lines |
| `validate_proposal_v2.py` | All 136 lines |
| `check_gaussian_calculus.py` | All 146 lines |
| `check_sampling_hoeffding.py` | All 368 lines |
| Live `docs/README.md`, `docs/NOTATION.md` | Entire files: 284 and 98 lines |
| `standalone_v2/docs/README.md`, `docs/NOTATION.md` | Entire files: 284 and 98 lines |
| Live `docs/global_nonlinear.md` | Exactly 1–32; 1803–1835; 3836–3980; 5268–5472; 6902–7167; 8976–9293; 9294–9605; 10300–10608 |
| Live `docs/finite_dynamics.md` | Exactly 1–227 |
| Fresh edition outputs | Entire validation report, Gaussian report and sampling report |
| Reviewer checks | Entire independently written check source and its output |

One initial batched tool result exceeded the aggregate output allowance. I
repaired this by rereading all three Python sources in one adequately bounded
call and rereading the live and assembled guide/notation pairs in separate
bounded calls. The candidate and assembled addition were subsequently covered
by the explicit blocks above. No truncated scientific or code body is counted
as a completed read.

### Exact older unread complement

The original `docs/global_nonlinear.md` has 11,436 lines. Its scientific unread
complement is **33–1802; 1836–3835; 3981–5267; 5473–6901; 7168–8975;
9606–10299; 10609–11436**. In `docs/finite_dynamics.md`, **228–1275** are
scientifically unread. The other older chapter bodies are scientifically
unread, including all of `docs/special_data_limits.md`. In particular I did not
read or audit the Gaussian proof excerpt 3785–4286; the authorized validator
byte-read, hashed and copied it as an assembly dependency. The long source-cap,
Gaussian construction and reference-response proof bodies outside the stated
ranges have not acquired an implied proof audit from this review.

The original complete documents were byte-read for frozen hashes and inverse
preservation. A collision check byte-scanned the original global chapter only
for the 88 new equation-tag strings. These operations did not retrieve or audit
the unread scientific text.

## Frozen inputs and preservation

All twelve packet hashes matched before verification and remained identical
after it. Full before/after records are in
`data/generated/trained_prediction_sampling/integration_v2/hashes_before.json`
and `hashes_after.json`.

| Input | SHA256 before = after |
|---|---|
| `proposal_C4_8_v2.md` | `98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928` |
| `promotion_edits_v2.json` | `50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c` |
| `validate_proposal_v2.py` | `e54689af496ce014ec2cc793f34fbefe370f1571122b3f6447863f3b73c81940` |
| `check_gaussian_calculus.py` | `118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef` |
| `check_sampling_hoeffding.py` | `4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a` |
| Frozen assembled global chapter | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| Frozen assembled README | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| Frozen assembled NOTATION | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Original global chapter | `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226` |
| Original README | `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a` |
| Original NOTATION | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Original finite dynamics | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |

The assembly also verified the authorized Gaussian dependency's full-source
hash `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489`
before and after its run. Its copied excerpt hash is
`43704820690a545e42673b93791a679985376351df9f349c39b4282bdef85b2f`;
the finite-dynamics excerpt hash is
`bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980`.

The independent reviewer check operates on raw bytes, rather than relying on
the validator's text equality. It confirms that assembled lines 11440–12991
equal the candidate bytes exactly. Removing the exact two-newline suffix plus
candidate, then reversing the single declared global-chapter replacement,
recovers the original global file byte-for-byte. Reversing the two README
replacements recovers its original bytes. NOTATION is unchanged. The fresh
edition's three complete documents are byte-identical to the frozen edition.

## Independent assembly and executed verification

Working directory for the commands below was `/home/amir/Codes/PDE`; Python was
3.10.12. Both top-level commands exited 0.

```text
python studies/trained_prediction_sampling/validate_proposal_v2.py --output data/generated/trained_prediction_sampling/integration_v2_edition
python -I data/generated/trained_prediction_sampling/integration_v2/independent_checks.py
```

The fresh assembler returned PASS. Its full evidence is
`data/generated/trained_prediction_sampling/integration_v2_edition/validation_report.json`.
The three output hashes are exactly the frozen assembled hashes above.
It copied and executed the two check sources with Python `-I`, removed
`PYTHONPATH`, and used the fresh edition as the working directory:

```text
/usr/bin/python -I /home/amir/Codes/PDE/data/generated/trained_prediction_sampling/integration_v2_edition/verification/src/check_gaussian_calculus.py --output /home/amir/Codes/PDE/data/generated/trained_prediction_sampling/integration_v2_edition/verification/gaussian_report.json
/usr/bin/python -I /home/amir/Codes/PDE/data/generated/trained_prediction_sampling/integration_v2_edition/verification/src/check_sampling_hoeffding.py --output-dir /home/amir/Codes/PDE/data/generated/trained_prediction_sampling/integration_v2_edition/data/generated/trained_prediction_sampling/statistical_checks/standalone
```

Both isolated commands exited 0 with empty stderr. The Gaussian program passed
six exact polynomial identities, covering its rank-one covariance line. The
sampling program passed 748 exact rational checks: decomposition, conditional
centering, orthogonality, all six double replacements, the higher-order bound,
first-projection symmetry and the exact three-term remainder identity. All
four Hoeffding orders and all three remainder terms were nonzero. Its direct
scaled remainder and the sum of terms both equal `548332/3125`; the
higher-order bound has strict slack `30270672/390625`.

These programs use only their supplied literal fixtures and Python's standard
library. They do not import a study proof, training output, maintained API or
retained array. Their results validate the stated algebra, not the uniform
neural response estimates by themselves.

The reviewer source and full result are
`data/generated/trained_prediction_sampling/integration_v2/independent_checks.py`
and `independent_report.json`. Besides raw-byte inversion and tag/navigation
checks, it independently verified the cutoff product identity R14 with exact
rationals. A separate fixed width-three, three-observation network fixture
checked every one of its 18 physical velocity components against a centered
finite difference of the unhalved mean-square loss. It retained a nonzero
readout and a repeated input with incompatible labels. Maximum velocity/gradient
discrepancy was `9.630901631751954e-11` at step `1e-6`; the dissipation discrepancy
was `5.082795295763276e-12`. The finite rank normalization agreed within `1e-14`.
This was a one-state deterministic normalization check, not training or evidence
for a limiting theorem.

## Scientific and integration findings

### Model, normalization and source interface — PASS

The new statement preserves two equal-width bias-free tanh hidden layers,
normalized input `u=x/sqrt(2)`, stored Gaussian variances `(1,1/n,1/n^2)`, output
division by `n`, mobilities `(n,1,n)`, and physical GF for an unhalved loss.
The population readout starts at zero while the actual finite random readout
is retained. The law is fixed separately in the smaller neighborhood; no
orthogonality, positive Gram rank, minimum atom mass or deterministic label
function is imposed on it.

P1 agrees with C.4.7.NF. S2–S7 agree with the personally read C.4.7.N2–N8,
including the distinguished current forward-source derivative in the reverse
row and its treatment of duplicated or singular queries. S8 uses precisely
the N-cap and N9–N17 interface: absolute backward row sums and forward
time/atom density. It does not substitute two independent actions for the
retained initialized action and its adjoint.

The first response differentiates the actual residuals, both source
covariances, both response arrays and all trained blocks. S19–S20 contain the
two distinct mixed parameter/covariance terms and the `1/4` fourth-source
term. The regularization argument avoids differentiating a singular covariance
square root. S38–S42 retain all mixed cross terms. The short-interval argument
separates history-dependent additive bounds from the base absorption constant;
larger fixed moment estimates are obtained after the low-order absorption,
so it does not require one step size small enough for every moment order.

The repeated-source derivative sums in S11–S18 do not assign a new atom-mass
factor to each repeated derivative. The boundary subtraction in S30–S31
uses the same passive input and an old-source expression; it supplies the
needed interval-length factor on every covariance entry with a new endpoint.
The second response reuses this linear unknown part and treats products of
first responses as known forcing. I found no mismatch between these new
arguments and the supplied older interfaces. The proof of the older cap
itself remains outside this integration audit.

P18 uses ordinary Euclidean/Frobenius/spectral norms with explicit `sqrt(n)`
and `1/n` factors. In particular the learned middle increment is measured in
ordinary Frobenius norm, and `Delta h^T/n` has Frobenius norm equal to the
product of the two RMS norms. This matches both the notation contract and
finite-dynamics equations (1)–(7). Its finite continuation argument applies
to every realized finite array, including exceptional sample laws.

### Completion, influence and statistical scope — PASS

The choice of nested radii leaves room for contaminations and common finite
quantizations. The C.4.7 completion and law continuity are invoked at the
same physical endpoint and in the same continuous-prediction topology. The
uniform finite Taylor remainder makes the derivative limits Cauchy; the
uniform forward-quotient limit then supplies actual, jointly continuous
`C(circle)`-valued influence for Borel laws. Centering is passed through the
finite derivative identity and norm convergence of Banach-valued integrals.
P11 and P12 use admissible probability segments and rectangles, rather than
assuming a two-sided ambient probability neighborhood or an unproved second
derivative of the completed flow.

The source recursion followed by mesh and quantization limits is a defined
construction of the response. It is not an endpoint-derivative oracle. At the
reference, the equality to C.4.6 is justified by the C.4.7 actual-contamination
interface. No finite-width derivative theorem at other base laws is inferred.

The generic sampling lemma is self-contained for its new statistical steps.
Its finite continuous-test cutoff has support strictly within the analytic
neighborhood. The product identity and telescoping over small rectangles
preserve mixed differences without assuming a second derivative of `F`.
The Taylor bias, double-replacement bound and first-projection convergence
lead to the exact orthogonal remainder identity R23. The `1/4` replacement
factor and the resulting total `6 M_*^2/m` bound are consistent. The singleton
data-space case and degenerate covariance are covered.

The derivative is in the stronger continuous-function norm, whereas the CLT
and mean-square remainder are in `H=L^2(circle,rho)` with normalized arc
length. The projection proof uses finite second moments and uniformly small
Hilbert tails. The continuous spatial covariance kernel represents the same
positive trace-class operator. Spatial averages are the asserted continuous
linear tests; the text does not infer a point-evaluation or supremum-norm CLT
from Hilbert convergence. Population expectations leave no external random
initialization environment; the generic lemma explicitly distinguishes a
conditional Gaussian mixture when such an environment is present.

The explicitly zero-extended endpoint is bounded and Borel. The finite-test
localization makes its discrepancy from the smooth cutoff exponentially
rare, so the `m`-weighted second moment still vanishes. P17 is therefore a
population sampling moment assertion for this bounded extension, not a
finite-width moment assertion. No additional test-circle labels or risk
claim are introduced.

For finite networks, conditioning first on a fixed sample leaves the
initialization law unchanged. C.4.7.NW1 is used only when that finite law
belongs to `U_Y`. Bounded convergence of `min(2,sqrt(m)*error)` gives P19
at fixed `m`; bounded test functions cost at most `2 Pr(E_m^c)` otherwise.
The triangle inequality then gives the stated width-first limit. No
simultaneous width/sample scaling, width rate, raw-GD fluctuation limit,
all-time conclusion or finite-network tangent limit has been inferred.

### Placement, notation, summaries and dependency independence — PASS

C.4.8 is at heading level four, matching C.4.5–C.4.7 under the C.4 parent.
Its four numbered children are level five and internal proof topics level
six. The equation sets are exactly P1–P20, S1–S43 and R1–R25: 88 unique labels,
with no collision against an older tag. All new named equation references
resolve. The helper's 67 distinct parenthesized references resolve, and the
independent broader check found no undefined new label occurrence.

The README link targets the heading slug
`c48-sampling-fluctuations-of-the-trained-prediction`, independently derived
from the actual heading. The one global summary and two README replacements
accurately state the fixed time, smaller law neighborhood, centered influence,
Hilbert Gaussian sampling limit, mean-square remainder and width-first GF
bridge. They preserve the older local, fitted-reference and nonlinear-law
claims. Scoped aliases for fields and the locally defined mass/statistical
variables are explicit; finite normalization is never hidden in a new RMS
norm symbol. The existing C.4 use of `W1` and the stated data metric make the
new `W_1` distance unambiguous relative to the weight notation.

The source equations repeat a limited part of C.4.7 to support the genuinely
new first/second response proof. The statistical lemma supplies the missing
sampling step beyond the older value and reference-response statements.
This duplication is justified by the complete proof and does not introduce
a competing model or theorem. The substantial section is placed next to
its immediate nonlinear training dependency.

The canonical addition has no scientific dependency on a study path,
historical verdict, scratch proof or retained array. Its dependencies are
the established book interfaces and the new proofs it includes. The isolated
check programs are supplementary algebra checks, not required scientific
inputs to the theorem. This review does not claim that the minimal edition
contains every unrelated chapter linked by the unchanged reading guide;
no full-book link/exporter or unrelated-code audit was requested or performed.

## Completion statement

All required new material and specified older interface ranges were read;
the initial output truncation was repaired; the fresh edition and independent
checks completed; the declared frozen inputs remained unchanged. There are
no unresolved integration objections or missing inputs within this assignment.
The exact older unread complement and the non-audited dependency proofs remain
as stated above. This PASS concerns only this exact frozen integration package.
