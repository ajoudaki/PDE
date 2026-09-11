# P2 proof inputs, deterministic validation and write record

Run: data/generated/trained_data_response/p2_20260911_02/.
Coordinator: /root, task 01a09106-41c4-7193-9db9-8068144fd825.
Date: 2026-09-11. Working directory for all commands below:
/home/amir/Codes/PDE, unless a standalone directory is explicitly stated.

No training run, parameter sweep, external scientific retrieval, repository
clone/worktree, reset, or established-book/code edit was performed.
The generated products check algebra/provenance only. The reached-query
estimate H is proved in the later frozen source argument and canonical
section; its proof and all A–C passed the complete reviews recorded below.

## Complete scientific reading and provenance

The coordinator read the full current docs/README.md (278 lines),
docs/NOTATION.md (98), this study's README, P1_SECTION.md (2062),
P1_DEPENDENCIES.md (3238), and P1_MANIFEST.json. The complete relevant
current global_nonlinear units were C.2 (2924–3440) and the C.4 introduction
through C.4.6 (3836–8959), including every proof of C.4.1–C.4.5.
The dependency packet supplied complete finite_dynamics §§1–4,
special_data_limits III.F.1–III.F.11, global_nonlinear A.1–A.4 and B.1,
and the reference proof units. The duplicated old-base excerpts were
verified against their corresponding live proof text after accounting
for the approved P1 incorporation.

The full code/README.md (591 lines) and the complete two P1 check scripts
were read before executing the standalone checks. No maintained API was
changed. Several initial large displays were truncated; missing ranges
were subsequently read explicitly, including the code guide's middle,
the dependency packet and all author/reviewer reports used. A full-file
hash is not treated as evidence of reading.

The coordinator personally read both requested skill instructions:
/etc/codex/skills/solve-math-rigorously/SKILL.md and
/etc/codex/skills/investigate-conjectures/SKILL.md. The latter's applicable
research-contract, evidence-ledger, adversarial-audit and
proof-search-orchestration references were read. Root AGENTS.md and the
complete workflow were read; later metadata rechecks found them unchanged.
No other study's scientific content or prior P1 review verdict was read.

| Input | SHA-256 |
|---|---|
| AGENTS.md | 7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |
| docs/README.md | 88757537ae600ebf79cf265288d6ca3034254caba236b4dcb055a21dd568c721 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| docs/global_nonlinear.md | 3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf |
| docs/finite_dynamics.md | a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| P1_SECTION.md | 33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38 |
| P1_DEPENDENCIES.md | ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79 |
| P1_MANIFEST.json | f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d |

All ten files listed in the frozen manifest's inputs map match their
declared hashes. Only explicitly invoked scientific files were used as
premises; metadata/hash verification of other manifest files does not
claim that their review or integration content was a scientific input.

P1 is now promoted as C.4.6. The section is an exact byte substring of
the current book. Removing that substring, reversing the one declared
book navigation edit, and restoring the single ending newline gives
the frozen pre-promotion book SHA
d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1.
Reversing the two declared guide edits gives the old guide SHA
7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e.
All other declared scientific base files still match their old hashes.
All seven frozen dependency excerpts match their exact old-base spans.
These operations take place in memory, not by editing the live book.

## Executed deterministic commands and outcomes

The following commands completed with exit status zero.

~~~sh
python -B studies/trained_data_response/P1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/p2_20260911_02/p1_algebra
python -B studies/trained_data_response/P1_REFERENCE_CERTIFICATE.py
python -B studies/trained_data_response/P2_VALIDATE.py --output data/generated/trained_data_response/p2_20260911_02/validation_01
python -B studies/trained_data_response/P2_CHECK_RADIAL.py --output data/generated/trained_data_response/p2_20260911_02/radial_01
~~~

Use a fresh generated output path when reproducing. The two P2 scripts
refuse an already existing output directory and confine their products
to this study's generated namespace.

P1 algebra results:

- Four directional Taylor errors were
  1.0292819331017236e-6, 2.573205074969171e-7,
  6.433012185025226e-8 and 1.608263607613758e-8.
- The unhalved loss/metric identity error was 7.90068011014e-12.
- The tested homogeneous propagator identities, including singular
  boundary cases, had errors at most 1.53e-14.
- Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0.

The exact rational reference certificate also completed successfully;
its displayed five numerical bounds were
0.392108947877, 0.396376711612, 0.233120735618,
0.339792209687 and 0.631761866359. The certificate script, not these
rounded values alone, provides its exact rational inequalities.

P2_VALIDATE checks all ten frozen input hashes, exact approved
incorporation/base restoration, and all seven dependency excerpts.
It then creates a standalone subdirectory containing only the two frozen
scientific texts and two check scripts. This is a small dependency-test
workspace in the generated namespace, not another checkout.
From
data/generated/trained_data_response/p2_20260911_02/validation_01/standalone/
it runs:

~~~sh
/usr/bin/python -B P1_CHECK_IDENTITIES.py --output algebra
/usr/bin/python -B P1_REFERENCE_CERTIFICATE.py
~~~

The subprocess environment sets PYTHONPATH to the empty string,
PYTHONDONTWRITEBYTECODE=1, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1.
Both exits are zero. Full stdout/stderr is retained in command_1.log
and command_2.log in validation_01. Their SHA-256 values are respectively
3e732b930cf23d9adfa4d21904e4f23e66ac89325fef724cec31b682bb38f42b and
ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900.
The machine-readable validation.json records exact commands, working
directories, all source hashes, exits and outcomes.

P2_CHECK_RADIAL uses one supplied parameter configuration and exact
gradient contractions, including nonzero readout and correlated and
repeated inputs with conflicting labels. It performs no flow integration.
The row radial-identity error and independent complex-step scalar
loss-gradient error are both 5.551115123125783e-17. All four radial
upper-bound slacks are positive:
0.0718663967809445, 0.6391692365525048, 0.706321708394638,
0.12351401925965669. Its result is PASS. This verifies normalizations
and algebra at the supplied state, not a general theorem by sampling.

| Source/check | SHA-256 |
|---|---|
| P1_CHECK_IDENTITIES.py | b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f |
| P1_REFERENCE_CERTIFICATE.py | 112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e |
| P2_VALIDATE.py | adcf8e60760c27dc56831ab98acd4708b472bd1d611ed9f08efbfc5c0b3ae3aa |
| P2_CHECK_RADIAL.py | c23fd43ede3a0660a2a9e2f31a1361e63d871e4ec3ad4444928cb342d876d30c |

## Independent routes, original reports and corrections

The initial three author contexts were fresh, without inherited
conversation. Their explicit source/output scopes are in
P2_COORDINATION.md. The original reports were frozen before comparison:

| Author/report | Frozen SHA-256 |
|---|---|
| /root/p2_reached_tails, P2_REACHED_TAILS.md | 837535f363d8140516ed993698f0e48d183dc029fe66cffc1277aff79e328716 |
| /root/p2_continuation, P2_CONTINUATION.md | fe59ffe02281be549d6d7815d9c3b58bfe9b51545236cbffb9899339838669d2 |
| /root/p2_variation, P2_VARIATION.md | ef28df6745758adc1c587a4d73442c3a49db575026ac2bee86708a24de44c5fd |

The continuation author subsequently read the other allowed frozen
arguments for a disclosed mature comparison, producing
P2_COMBINED_TAIL_CONTRACT.md. It preserves the original reports.
The independent conditional variation audit is P2_VARIATION_AUDIT.md;
its neutral assignment and missing-equation supplement are preserved
in P2_VARIATION_AUDIT_ASSIGNMENT.md. This is a scoped conditional check,
not an unconditional milestone acceptance.

The variation author separately checked the two root lemmas as a
collaborator. P2_ROOT_LEMMAS_CHECK.md records its old input hashes.
The root files were then corrected: the population loss gradient has
its factor 2(f-y), the normalized data metric is explicit, the gates
are bounded continuous functions, the initial/current observation fields
are precisely scoped, and the finite bridge states its population
premises and fixed-law quantifiers. The original adverse report is
unchanged. Current hashes:

- P2_REFERENCE_COMPARISON.md:
  a6d229fd69be98df8bf41fa7fdde9dad55cfcae86799f2c268791dc3e3904c4d.
- P2_RESPONSE_BRIDGE.md:
  7a410d6d5e2fc16a07b4a04ab355878d51ec9940a1d52c1ca506b6288d528e89.

The combined report's old root-file hash is a record of its construction
input, not the current edition. The combined audit was explicitly told
to read the two corrected root files completely. No prior verdict was
supplied to that fresh reviewer.

## Shared write and commit evidence

This is the same task as the existing P2 ownership metadata, resumed in
a fresh generated run; no other P2 unfinished argument was present.
The old generated run is preserved. Startup HEAD was
96e02035386b24d058b623dcd53186ff5afbca45 and the index was empty.
Unrelated modifications were inspected only as Git safety metadata.

Root alone writes Git. Every successful stage/verify/commit transaction
takes a nonblocking exclusive flock on .git/pde-writer.lock, rechecks the
HEAD and empty index, hashes each explicit owned path, stages only those
paths, verifies the exact staged list, runs git diff --cached --check,
commits, records the result and releases the lock. The lock is never
unlinked or held during research. No other's staged change was cleared
or adopted.

The initial sandbox attempt to open the Git lock failed with read-only
filesystem error 30 before any mutation. The narrowly scoped escalated
writer transaction was then accepted by automatic review. This was an
environment permission issue, not a scientific failure or user rejection.

| Commit | Purpose | Generated evidence |
|---|---|---|
| ae37dfe5400cc4fbc1c260e29272b7667a92ab87 | P2 contract and independent input/write scopes | commit_01.json |
| 48da1046efc2e1f4a8da6c0d5cbaf4c10febe394 | Frozen route reductions, raw comparison, deterministic checks and README checkpoint | commit_02.json |
| e960b4a8d6f7645fffa4c970ec1018ffeddb107f | Conditional audits, corrected observation/bridge contract, exact gap and bounded-feature route | commit_03.json |
| 0772d18e8816c87144948f861022b132c81d9dc9 | Complete author candidate, source proof, frozen dependencies and standalone recipe | commit_04.json |
| 3c9feacb0befd20fd57aa577494af36286af5758 | Both complete success reviews and independent promotion selection | commit_05.json |
| 5be000b2d5d1feed8e0582b00e1022b156ede4e1 | Complete frozen canonical edition, standalone implementation and fresh review assignments | commit_06.json |
| Recorded in commit_07.json | Final canonical reviews, original check archives and approval-ready records | commit_07.json |

The second commit changes nine assigned study files; the third changes
thirteen. Neither includes generated products. The third transaction's
first strict whitespace check found one final blank line in the original
frozen variation audit and stopped before committing. The index then
contained only the thirteen staged owned files. On retry their exact
staged blobs and source hashes were verified under the shared lock.
All other files passed the ordinary strict check; that one frozen report
passed with only blank-at-EOF checking disabled so its original bytes
and hash were preserved. The original diagnostic and both transaction
outcomes are in commit_03_attempt_01.json and commit_03.json.
No scientific or other whitespace exception was introduced.

Subsequent checkpoint hashes and validation are recorded with their own
transaction evidence. All scientific source,
original reviews, essential proof arguments and check scripts are in the
flat study directory; generated files contain only reproducible evidence.

## Full author candidate and standalone packet

After the earlier conditional checkpoint, the source author proved a
physical reference clock coefficient bound by fresh query insertion,
then used differentiated raw-to-clock consistency and a weighted
law/source comparison to claim H. Root read all 1,070 lines of
P2_SOURCE_BOOTSTRAP.md and checked its two bootstraps, causal ordering,
atom/step density bounds, Gaussian-source coupling and moment steps.
The original is frozen at SHA
0cf6d54dbb85c6d7f4c5b737dbbe3c92956aef4680d7a88214bd2c34c5034efb.

A fresh prompt-only checker independently derived the conditional
coefficient-difference estimate, retaining every source's atom mass.
Root read all 586 lines after it froze. P2_KERNEL_CHECK.md has SHA
bb0b3d15f4b6338daf51494a64cfa4511e76fe86c3004ef45e20900480e3477b.
The checker had no source report or prior verdict. Its estimate is
stronger than needed; the candidate retains the original conservative
exponent and does not depend on this separate check's acceptance.

P2_THEOREM.md states all A–C and the observation, restart and limit
contracts explicitly. P2_MANIFEST.json freezes sixteen full inputs,
including all needed proofs, the complete additional established units,
and applicable assembly/check scripts. Its SHA is
e0ea00ceedcec700811af7584ead90af44e15a40bb48dc9374db04e90e436e7d.
This is an author candidate, pending two fresh complete isolated
mathematical reviews. No prior review report is in their input manifest.

The full standalone command was:

~~~sh
python -B studies/trained_data_response/P2_BUILD_PACKET.py --output data/generated/trained_data_response/p2_20260911_02/full_packet_01
~~~

Exit status was zero, result PASS. The assembler verified every frozen
input hash, the five current established source hashes, all four exact
additional dependency excerpts, and the frozen P1 correspondence. It
copied only the proof/check packet, without Git or unrelated files, into
the generated standalone directory. From that packet it executed both
P1 algebra/certificate scripts and the P2 supplied-state radial check
with empty PYTHONPATH and one BLAS/OpenMP thread. All three passed.
Commands, working directories, complete logs and final rechecked hashes
are in full_packet_01/validation.json. Its checks establish exact input
correspondence and standalone algebra, not correctness of the new proof.

The fresh full reviewers and separate relevance selector have distinct
file/scratch ownership recorded in P2_COORDINATION.md. Their original
reports and complete coverage must be retained before any success or
promotion conclusion.

## Complete mathematical review outcome and canonical assembly

Both fresh complete isolated reviews of the unchanged sixteen-input
packet passed all A–C, with no required corrections. Root read both
original reports completely, including all coverage, source/excerpt hash
records, source/tail attacks, continuation and actual finite capture,
uniform nonlinear response and the width-first finite bridge, applicable
check code and results. Their reports are frozen as:

- P2_FULL_REVIEW_A.md, 201 lines, SHA256
  00efc606e4511b90e27387a3a79bc30430b35aacc387fff9fcff43d142381e17.
- P2_FULL_REVIEW_B.md, SHA256
  f9c21865c76ae87770489e2022793e04a688dd052943ef8045fd64740b1c4ccc.

Both reviewers read every scientific input line, verifying exact duplicate
dependency correspondence where a body was read once. Both ran the full
standalone packet and their own bounded source/clock algebra checks.
Reviewer A checked the direct source chain, zero-mass pulse and canceled
clock-defect derivatives. Reviewer B additionally checked source-atom
duplication with a tiny far atom. All passed; no training was run. Their
original evidence remains in full_review_a/ and full_review_b/. Neither
reviewer received the other's findings before freezing. Their complete
neutral assignments remain P2_FULL_REVIEW_ASSIGNMENTS.json.

P2_RELEVANCE.md, SHA256
d7bf17c8e1534055abf07b6d99a30e01b7fb903dff3642c10d790fd5fed1446e,
independently accepts the full result for assembly as one C.4.7 appended
after C.4.6, plus small guide/navigation edits. Root read its entire
report. This is separate from mathematical correctness and is conditional
on canonical scientific and integration gates. The original mathematics
has now met the user's two-review success requirement. Promotion remains
unapproved and unperformed.

The canonical assembly removes historical conditional labels and repeated
setup while retaining every substantive proof in canonical notation.
P2_COORDINATION.md records separate source/remainder assembler ownership.
This rewrite will be a new frozen packet, with fresh complete mathematical
and integration reviews; earlier verdicts are not canonical review inputs.

## Frozen canonical edition and standalone validation

Root read both complete canonical component drafts and their author notes:
P2_CANONICAL_SOURCE.md (1,063 lines; 1,011 scientific lines) and
P2_CANONICAL_VARIATION.md (918 lines; 843 scientific lines). Their original
hashes are 9a7e927206fbeaad283487276a6dcb459f5a4297b5efa0475c75cfb915606738
and 10b1cc4f33e6fe710fba5ba3276954a5a7c4f112c9ac2aea3c9c371353bddad5.
The complete new arguments were checked against the original frozen routes;
no mathematical route change or new assumption was introduced. Root wrote
the precise theorem, raw HS comparison, strong completion/finite capture
and inherited-subclass corollary in the other three canonical component
files. P2_ASSEMBLY_MAP.json records the five body sources, exact hashes,
the raw sum-distance alias normalization, two local constant renamings,
and the C.4.7 equation namespace applied to every new tag and reference.
Historical author notes remain outside the assembled scientific section.

P2_SECTION.md contains 2,461 lines and 114 unique C.4.7 equation tags,
with SHA256 707a7d42eb2e2e58ae92fa2ee8e25343977224fe1307675e7c0c82609b0571f0.
The complete proposed guide has 284 lines and SHA256
5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a.
The seven verbatim navigation replacements and exact base hashes are
P2_EDITION_ANCILLARY.json. Root read that entire file and the entire
P2_EDITION_BUILD.py implementation. Its author's pre-section guardrail
checks are retained in edition_builder/pre_section_checks.json.

P2_PROMOTION_DEPENDENCIES.md supplies seven complete exact established
units (7,434 lines): the current guide and notation, finite dynamics §§1–4,
special-data III.F.1–11, global-nonlinear A.1–A.4/B.1, complete C.2, and
complete C.4 through C.4.6. These are the complete units root had already
read; exact excerpt checks verify their correspondence. The ten canonical
scientific/implementation inputs are frozen by P2_PROMOTION_MANIFEST.json,
SHA256 7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e.
Neither prior reports nor review verdicts occur in this input set.

Executed from /home/amir/Codes/PDE:

```sh
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/promotion_check_01
```

Exit zero, PASS. Root inspected every subprocess log and the edition's
preservation/link results. All ten frozen inputs, ten copied established
document hashes, seven dependency excerpts and shared instructions match.
The standalone artifact contains docs, three fresh validation scripts and
fresh check outputs, with no studies or Git directory. It recovers every
base byte by exact inverse edits. The eight other copied documents are
unchanged. New/affected guide links and fragments resolve; the only explicit
preexisting local exclusion is ../code/README.md in the docs-only artifact.
No code API or empirical claim is added. External URLs are preserved,
not retrieved; unrelated older chapter links are outside this check.

The tangent, loss-metric, compatible singular semigroup, rational
certificate and correlated/repeated-input radial checks all pass with the
same outcomes as recorded above. The radial check changes only its output
path policy for standalone execution; the first two scripts are exact
byte copies. Full logs, commands, environment and hashes are under
promotion_check_01/. Its standalone chapter hash is
9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226;
its guide hash is the proposed-guide hash above. This does not certify
the theorem and does not edit established files.

Two fresh complete canonical mathematical reviewers and a separate fresh
integration reviewer are now reading the unchanged packet. Exact neutral
assignments and all three launch messages are persisted in
P2_CANONICAL_REVIEW_ASSIGNMENT.md, P2_INTEGRATION_REVIEW_ASSIGNMENT.md and
P2_PROMOTION_REVIEW_LAUNCHES.json. They receive no earlier verdicts or
each other's findings. Their reports must be read in full before the
canonical package can be approved for an incorporation request.

A pre-stage whitespace check of the new complete dependency collection
reports exactly one trailing space on its line5513, the exact copied
established C.4.6 line `` `ell(t,u)v`. ``. That byte is part of the frozen
dependency hash and is preserved. The new scientific section passes the
strict whitespace check. The writer transaction verifies that this is the
only dependency whitespace diagnostic, checks all other files strictly,
and disables only blank-at-EOL checking for that immutable dependency file.
This is a preexisting formatting diagnostic, not a proof correction.

## Final canonical gates, original evidence and resolved status

Both fresh complete isolated canonical scientific reviews PASS every A–C
obligation, all complete invoked dependency proofs and applicable check
implementation, with no required corrections. The separate fresh integration
review also PASSes without required corrections. No frozen scientific
input changed after the canonical manifest was sealed. Root read all three
original reports completely; one truncated sentence in scientific review B
was explicitly recovered by reading lines110–170. The reports are:

| Original report | SHA256 |
|---|---|
| P2_CANONICAL_REVIEW_A.md | 80b92cb312d9dc79424b2216163e8867e1dfc000f1f7bc81f72c7c5c812e26ac |
| P2_CANONICAL_REVIEW_B.md | 5984c09e172825c0834971c449b9a1baaa2effd9419e51ad8047a92fa0f3773c |
| P2_INTEGRATION_REVIEW.md | 588a2465b78e6752632732a803372ca271561c2312b1e0abd7a1729ed7187fb2 |

Each scientific reviewer read the complete 2,461-line new section, all
7,434 dependency lines, the full proposed guide, exact ancillary edits,
manifest, recipe and every applicable script. Their detailed reports record
source-density and mass-splitting attacks, complete residual feedback in
query forcing, raw/clock differentiated consistency, the two causal
bootstraps, Osgood completion, arbitrary-strong-competitor uniqueness,
finite-GF/empirical-law limit order, reached integrability, compact-direction
Taylor and the exact P1 finite derivative bridge. Neither reviewer received
prior verdicts, author history or the other reviewer's findings.

The integration reviewer read the complete new assembled section and new
guide/navigation/implementation. Its older scope includes complete finite
§§1–4, III.F.1–11, global A.1–A.4/C.2, C.4 introduction/C.4.1–2,
complete C.4.5, the C.4.6 theorem and first two proof units, and its final
scope boundaries. Its explicit unread older dependency spans are
1229–1787 (B.1), 3099–3736 (C.4.3–4), and 5801–7387 (the remaining
C.4.6 propagation/cavity-capture proofs). Those established interfaces are
used without claiming a fresh whole-book audit; both scientific reviewers
read their complete proofs. Integration checked notation, placement,
exact A–C scope, dependency and implementation closure, independent
preservation and affected link correspondence.

Each reviewer independently ran the same frozen supported command with
its own fresh output path:

```sh
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/canonical_review_a/standalone_run
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/canonical_review_b/standalone_run
python -B studies/trained_data_response/P2_PROMOTION_CHECK.py --output data/generated/trained_data_response/p2_20260911_02/integration_review/standalone_run_01
```

All three completed with exit zero and PASS, including all component
commands. Complete original commands, logs, environments, hashes and
review-specific checks remain in those generated namespaces. Reviewer A's
additional scalar/HS/activity check passed using standard-library Decimal.
Reviewer B independently checked complete forward-query forcing at one
fixed supplied state and the canceled clock identities at three declared
scalar points. The forcing error was 1.734723475976807e-18; duplicate-atom
additivity error was 5.421010862427522e-20. Suppressing residual feedback
produced the intended nonzero signal 0.0010650008147578167. The three
70-digit Decimal identity errors were at most 3.47e-43. These are bounded
algebra checks, not flows or parameter sweeps. Both reviewers' initial
optional mpmath imports failed before computation; original failed attempts
were retained and no package was installed. Their standard-library checks
then passed. The integration reviewer's independent edition check passed.

P2_REVIEW_CHECK_ARCHIVE.json maps five byte-exact supplemental reviewer
check sources from generated scratch to flat study-owned files. Root read
all five sources in full and verified both original and archived hashes.
The original reports, sources and outputs remain unchanged. These archives
are forensic copies of already executed independent checks, not additions
to the frozen canonical scientific dependency set. Do not execute those
copies in the study directory: some retain original output paths or write
adjacent output. Fresh supported reproduction uses P2_PROMOTION_CHECK.py.

Root's final inline Python/hashlib audit is final_audit_01.json. It checks
the exact three manifest hashes and all 10 P1, 16 original P2 and 10
canonical input hashes; all ten base documents and both shared instructions;
all six original review/selection hashes; and the five archived check
correspondences. It checks the two assembled output hashes, exact P1
substring in the actual book, exact P2 substring only in the standalone
book, and the empty shared index before the closure transaction. Result:
PASS. A separate bounded read-only metadata recheck by the integration
reviewer independently confirmed every canonical input/base/instruction and
both assembled hashes, with no discrepancy and no file writes.

A–C are resolved by the frozen proof, including the previously missing H.
The positive law radius may be extremely small and no practical numerical
radius is claimed. The finite nonlinear response statement has exactly the
required width-first order and no arbitrary joint epsilon/width rate.
Existing risk/activity results apply only on their exact admitted subclass.
There is no unresolved mathematical lemma in the primary target. Earlier
partial-route reports and their original verdicts remain historical evidence.

The complete recommendation is P2_PROPOSAL.md. Every required scientific,
relevance, standalone and integration gate has passed. Only explicit user
approval and the subsequent approved two-file incorporation remain. No
established document or maintained API has been changed by this P2 task.
The final study-only transaction and exact staged paths/hashes are recorded
in checkpoint_07_inputs.json and commit_07.json under the common writer lock.
