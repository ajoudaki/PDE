# Independent isolated integration review of proposed C-H1 edition v3

**Verdict: PASS for the complete assigned integration scope.** No required
correction or unresolved integration objection was found. The actual assembled
subsection and guide correspond exactly to the frozen proposal. Removing the
insertion recovers the recorded older chapter byte for byte. Both copied
standalone checks ran successfully in fresh scratch and reproduced the frozen
outputs byte for byte.

This is an integration verdict, not either of the two complete scientific
reviews, a whole-book proof audit, a C-H2 convergence result, a C-H3 cost result,
or authorization to promote the material. I fully read the new argument and
report below the scientific and information-interface checks I could make
within the specified older scope. I did not presume that another review gate
had established any assertion.

## Reviewer, isolation, and authority

- Reviewer: `/root/integration_v3`, on 2026-09-12.
- Neutral assignment: `integration_assignment_v3.md`, reproduced by its hash
  below. I received no author discussion, study history, earlier verdict, or
  other reviewer's findings.
- The manifest names `/root`, `/root/route_observable`, and `/root/route_weak`
  as authors/assemblers, and `/root/selector` as selector. I am distinct from
  all of them.
- I read only the assignment's listed inputs, precise older scopes, required
  skills and their applicable references, plus metadata-only Git safety
  information. I did not read the study README, routes, selection report,
  internal reports, other review reports, another study, or Git history.
- I did not delegate, browse external scientific sources, train a model,
  modify frozen inputs or established files, or make Git writes. The only
  authored files are this report and scratch under
  `/home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/`.
- Before scratch/report edits, the metadata check returned HEAD
  `a1c6c99bd0e1d2029d6f861f4a05f8ba29fbe9c3`, an empty staged-path list,
  and existing modifications to `.gitignore` and four book-exporter files.
  Their contents were not inspected and their changes were preserved.

## Actual read coverage and explicit unread complement

The following are complete reads, not claims inferred from a summary or from a
hash. Prefix **P** is `/home/amir/Codes/PDE/studies/observable_hierarchy/`;
prefix **E** is
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/edition_v3/`.

| Input | Actual coverage |
|---|---|
| P/integration_assignment_v3.md | Entire assignment |
| P/candidate_v3.md | All 642 lines; chunks 1–220, 221–440, 441–642 |
| P/README_proposed_v3.md | All 654 lines; chunks 1–220, 221–440, 441–560, 561–654 |
| P/notation_v3.md | All 98 lines |
| P/guide_current_v3.md | All 645 lines; chunks 1–170, 171–330, 331–490, 491–645 |
| P/instructions_v3.md | All 47 lines |
| P/workflow_v3.md | All 224 lines, including all of Part 2 |
| P/review_inputs_v3.json | All 19 lines |
| P/assemble_edition_v3.py | All 94 lines |
| P/edition_manifest_v3.json | All 65 lines |
| E/docs/README.md | All 654 lines; chunks 1–220, 221–440, 441–560, 561–654 |
| E/docs/NOTATION.md | All 98 lines |
| E/docs/global_nonlinear.md, new subsection | All lines 11441–12083; chunks 11441–11660, 11661–11880, 11881–12083 |
| E/docs/global_nonlinear.md, C.4.2 | All lines 4208–4631; chunks 4208–4420 and 4421–4631 |
| E/docs/global_nonlinear.md, C.4.7 introduction and contract | All lines 8978–9170 |
| E/docs/global_nonlinear.md, C.4.7.7 | All lines 11398–11440 |
| E/docs/global_nonlinear.md, following C.4.8 interface | All lines 12084–12172 |
| E/README.md.patch | All 27 lines |
| E/global_nonlinear.md.patch | All 652 lines; chunks 1–220, 221–440, 441–652 |
| E/checks/check_weak_identity.py | All 125 lines |
| E/checks/reference_certificate.py | All 56 lines |
| E/manifest.json | Entire file, identical to P/edition_manifest_v3.json |
| E/check_0.txt and E/check_1.txt | Entire files, 26 and 1 lines respectively |

The initial oversized combined read suffered aggregate truncation. I repeated
the complete skill-reference read and the process/manifest/source read with a
larger output allowance; a remaining truncated workflow portion was repaired
by reading the entire 224-line workflow separately. Subsequent bounded chunks
above were complete. No assigned new scientific line remains unread.

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely (115
lines), and `/etc/codex/skills/investigate-conjectures/SKILL.md` completely
(185 lines), with its `research-contract.md` (99), `adversarial-audit.md`
(121), `evidence-ledger.md` (157), and `decisive-experiments.md` (141)
references. The latter was read for the authorized static computation; no
research experiment or training campaign was added.

The assembled chapter has 19,396 lines. Its older scientific unread complement
is exactly **1–4207, 4632–8977, 9171–11397, and 12173–19396**. Byte hashing,
insertion removal, exact patch reconstruction, and counts of potentially
colliding equation labels operated on those bytes without exposing or reading
their proof bodies. The bodies of `special_data_limits.md` and
`gaussian_calculus.md` were not read: only their existence and hashes were
checked. I did not inspect `dependencies_v1.md`, `source_hashes_v1.json`, the
uncopied study check source, or the retained
`results/static_identity/result.json`. Their appearance in an allowed manifest
did not expand this review's input scope. No older guide-linked chapter or
external literature body was fetched.

## Correspondence, preservation, placement, and references

**PASS.** Independent verification located exactly one insertion beginning at
line 11441. The candidate has 642 lines; the assembled insertion is precisely
`candidate.rstrip() + "\n\n"`, 643 lines including its separating blank line.
Thus the scientific candidate occupies 11441–12082, with a separator at 12083.
The next unchanged heading is C.4.8 at 12084. The preserved base has SHA256
`1f079e1e891dfbee88ac87495cb3b39c9e6992da34d4acf56d98c1c024d89dc9`,
exactly the recorded original source hash. This checks every older byte,
including the unread scientific complement, without claiming to audit it.

The assembled guide equals `README_proposed_v3.md` byte for byte; the frozen
old guide equals the recorded original guide hash. Independent reconstruction
of both unified patches from the actual before/after bytes reproduced both
frozen patch files exactly. The guide has precisely two hunks: the nine-line
C-H1 result paragraph, and the replacement of “these planning milestones” by
“the later computation milestones.” There is no additional guide change.
The notation contract and two copied dependency chapters equal their recorded
source hashes. Both edition manifests are byte-identical.

C.4.7.8 is a level-five heading after C.4.7.7; its nine numbered parts are
level-six headings; the subsequent C.4.8 returns to level four. This follows
the surrounding hierarchy and does not absorb the later sampling theorem.
All nineteen equation definitions H1–H19 occur once in the new subsection;
every parenthesized H-reference resolves within that set. Automated metadata
counts found no old `(H1)`–`(H19)` or `\tag{H1}`–`\tag{H19}` collisions.
The equations are intentionally indented plain-text mathematical blocks;
their syntax is not misrepresented as executable Python or TeX.

The sole new Markdown link points to `special_data_limits.md`, which exists
in the assembled docs and has the expected hash. It has no fragment. The
guide's Markdown-link multiset is unchanged; the new C.4.7.8 reference is a
plain section reference and resolves to the inserted heading. Part references
2–9 and references to the surrounding C.4.2/C.4.7 sections are coherent with
the stated dependency interface. I did not validate anchors or proof bodies
outside the assigned scopes.

## Canonical model, notation, and neighboring interfaces

**PASS.** The subsection retains the bias-free two-hidden-layer tanh network,
input `u=x/sqrt(2)`, normalized circle, output division by n, independent stored
Gaussian variances `(1,1/n,1/n^2)`, block mobilities `(n,1,n)`, residual `f-y`,
and unhalved mean-square physical GF. Its factor `-2` and rank normalization
agree with the C.4.7 model/theorem, C.4.8's following equation, and the full
notation contract. The mean is a training-law integral, not an unnormalized
sum. No new GD or changed-clock conclusion is inserted.

The aliases `w=W^(1)`, `A=W^(2)=A0+K`, and `c=W^(3)` have explicit types.
The lowercase population aliases are explicitly identified with capitalized
canonical hidden/backward fields; they do not silently become finite neuron
coordinates. Expectations are separated by population. The reverse action is
the actual adjoint; only K and later increments are Hilbert–Schmidt. The
finite readout is still random, while the limiting initial c is zero. The
tail and raw-norm conventions in the new argument are compatible with the
specified older contracts: its sum raw norm is equivalent to the earlier
three-component Hilbert raw norm, with no hidden width normalization.

The data metric is exactly the normalized input distance plus label distance.
The neighborhood is a fixed positive open ball relative to all Borel laws,
with `delta=min(delta_Y/4,delta_act,Y,1/4)` and `T0=1/200`, independent of level.
Both nonorthogonal and nonatomic examples are supplied. No atom-count,
minimum-weight, Gram-rank, or deterministic-label restriction is inserted.
The larger interval `[0,40]` is used only through the existing reached-flow
scope; the advertised C-H1 interval remains `[0,1/200]`.

C.4.7.7's binary subclass, extremely small numerical neighborhood, quantitative
activity at 1/200, and risk at 40 are preserved. Part 8 instead gives a
qualitative positivity argument on its own fixed ball and at a fixed
`t_a in (0,T0)`. It does not transfer the old quantitative margins to every
bounded-label law, claim motion at time 40, or imply frozen-feature superiority.
C.4.8's width-first sampling theorem and fixed-time target are unaffected.

## What the hierarchy actually stores and determines

**PASS for the C-H1 information contract.** At level j, the state is a finite
list of typed acyclic graph shapes with at most j nodes and same-population
ordered output tuples of dimension at most j. The stated crude type bound is
`(20(j+1)^2)^(3(j+1))`. Each type carries a family of probability laws indexed
by at most 3j real coefficients and j circle directions; a characteristic test
adds at most j frequencies. The total real-mark bound is therefore 4j,
besides the j circle marks. These are law-valued fields over continuous mark
domains. **Their exact storage is not a finite list of scalars, and neither
quadrature size nor arithmetic cost is proved.** The subsection says this
prominently, consistently with the guide.

The stored seeds are the two current row coordinates, bounded scalar readout,
the two frozen initial Gaussian row coordinates, and the finitely requested
initial second-preactivation observations. The alphabet permits affine maps,
sin/cos/tanh, bounded products, and either orientation of the current action
on a specified bounded program. It does not accept an arbitrary L2 vector,
matrix row, distribution, arbitrary function, or transcript as one mark.
Neither A nor K is a retained operator-valued finite-level coordinate. A law
index for a finite program is therefore distinct from an unrestricted action
oracle. Completing all levels can recover an infinite relevant action; this
is explicitly acknowledged and is not presented as scalar compression.

Joints retain the same neuron for all chosen marks within a population. Taking
finite graph unions puts any separately fixed finite input/current/initial
tuple in some finite level. Separate marginals are not substituted for
`E[c h2(u)]` or paired hidden displacements. Cross-population factors in the
rank contractions are products of expectations, not missing same-neuron
correlations. The recovery of d1 is an explicitly declared bounded-gate
pushforward of `(q,z1)`; it is not an unbounded multiplication instruction
silently followed by another action. The declared action-observation scope is
the finite alphabet and its stated pushforwards/contractions, not every
possible unbounded observable permitted by another theorem.

The Gaussian initialization is a finite joint construction, retaining both
oriented source groups and response corrections of the same action. Its
singular covariance rule includes duplicated and zero-variance queries.
Initialization does not depend on the training law or future trajectory.
The new text identifies its established source dependency; this review checks
compatibility with C.4.2's stated construction, not the unread III.F proofs.

The continuum-law interface is exact integration of continuous scalar
integrands, or a certified atomic approximation followed by a limit. It is
not claimed to be an effective quadrature procedure. A separately fixed
observation program and marks precede the width limit; no all-marks uniform
or growing-program theorem is asserted. These choices agree with the older
observation contract actually read at lines 8978–9170.

## Evolution, restart, and scientific concerns checked within scope

**PASS; no substantive concern identified within the integration scope.**
The new proof was fully read. Its visible argument distinguishes the following
bridges rather than treating them as synonyms:

1. Along a strong path, bounded multipliers give L2 curve chain rules; actions
   use the ordinary product rule. This yields C1 characteristic coordinates
   without asserting ambient L2 Fréchet differentiability.
2. Reverse differentiation records every moving-action occurrence and both
   orientations. Substitution of H2 in H7 gives the normalized rank contractions
   of H8. The copied static check independently compares these with a forward
   tangent and a centered finite difference.
3. Covectors are proof devices. Their cut versions compile into the original
   alphabet by `T_R=R tanh(./R)`, with fixed graph size as R increases. The
   contraction estimate and L2 saturation convergence suffice for a fixed
   graph; they are not an order-uniform cutoff estimate. The deliberately
   loose `N=10^6(j+1)^6` bound has room for the graph, accumulated reverse
   contributions, physical fields at one new input, and their joint tuple.
   The training-law integral is outside the population coordinate list.
4. Characteristic tests determine finite laws. Equal complete joints define
   isometries on generated observable L2 spaces, preserve bounded coordinate
   operations, and intertwine both action directions. H11 establishes a
   reducing pair, so a complementary action block cannot feed the observable
   block. Moment determinacy is not substituted for this argument.
5. Restarted Euler constructions stay in the fixed generated spaces. Their
   convergence is separately justified by a one-reference tail comparison
   and the explicit Osgood estimate H14. This addresses the necessary bridge
   from Euler invariance to flow invariance rather than assuming it.
6. Transport of the actual remaining reference path constructs a continuation
   on a matching carrier with Hilbert–Schmidt increments. One-reference
   uniqueness compares an arbitrary competing strong continuation to that
   transported path, without requiring a tail hypothesis on the competitor.

The restart statement consistently requires a canonical reached reference
state, equality of the *complete* hierarchy, the same continuation law, and a
matching bounded-action/bounded-readout L2 realization. It includes matching
states reached at different times or under different former laws because
continuation is under the specified reference law. It does not claim existence
for an unmatched state switched to an arbitrary new law, or uniqueness for
unrealizable formal characteristic sequences. Time s bounds the remaining
horizon; it is not a stored time-series coordinate. The guide's short summary
does not broaden these qualifications.

I also checked the qualitative activity calculation's visible factors and
types. The two masses 1/2 and the unhalved loss give `c'(0)=S`; integrating
the first nonzero hidden velocity yields the stated `t^2/2` coefficients.
Adjunction in H17 forces nonzero first-layer coefficients, and the sum of
positive terms in H18 forces a nonzero second-layer coefficient. H19 has the
corresponding `1/8` training-average factor. L2 continuity of the affine-fit
nonaffinity functional at nondegenerate Gaussian laws and law continuity
then select one positive time and neighborhood independent of hierarchy
order. No numerical certificate is needed for this new qualitative claim.

C.4.2 already contains intrinsic generated-current-state sufficiency and the
Euler-to-flow invariance bridge. C.4.7.8 explicitly acknowledges that overlap.
Its additional finite alphabet, level and mark accounting, joint observation
dictionary, initialization procedure, finite reverse compiler and fixed
nonlinear law-family formulation make the addition more than a duplicate
assertion of raw-state uniqueness. Its placement as a subsection of the
supporting reached-flow theorem is appropriate.

The unread established Gaussian-source, passive-tail, and finite-network
identification proofs remain outside my scientific certification. This is a
limit of this assigned integration review, not a discovered missing input
within its defined scope or a presumption that those proofs pass another gate.

## Standalone verification: commands, results, and limits

The independent verifier is retained at
`/home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/verify_integration.py`.
Its source SHA256 is
`290971d44a280ac7b55eb2c0ba5e12d77db58589df2bec68014bb3f069061c75`.
The command was:

```text
cwd: /home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3
python -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/verify_integration.py
exit: 0
result: PASS
```

It parsed and copied the two complete assembled check sources, verified their
copy hashes, and invoked them once each as follows, with the same cwd:

```text
/usr/bin/python -I -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/copied_checks/check_weak_identity.py /home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/fresh_static_identity
/usr/bin/python -I -B /home/amir/Codes/PDE/data/generated/observable_hierarchy/integration_v3/copied_checks/reference_certificate.py
```

Both returned exit 0. Python isolated mode removes the current directory and
environment import-path additions; the copies import only the standard library
and NumPy. Source inspection shows no study dependency, external input read,
retained-array load, or training. Their fixed finite arrays and rational
configuration are contained in the copied sources. Execution used Python
3.10.12, NumPy 1.26.4, and
`Linux-5.15.0-151-generic-x86_64-with-glibc2.35`.

| Check | Actual result |
|---|---|
| Static H7/H8 identity | Weak RHS `0.0008986674151865981`; raw pairing and independent forward tangent both `0.0008986674151865992` |
| Centered finite difference | `0.0008986674071564947`; absolute discrepancy about `8.03e-12`, below the source's `1e-8` threshold |
| Saturated reverse compiler | Errors at R=1,4,16,64,256,1024: `2.283848724277947e-4`, `2.0198865272766115e-5`, `1.2966992833903304e-6`, `8.118165291566559e-8`, `5.07439319144716e-9`, `3.1715168186986775e-10`; final error below `1e-6` |
| Rational certificate | `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; every exact Fraction assertion passed |
| Frozen-output comparison | Both fresh stdout/stderr logs are byte-identical to `check_0.txt` and `check_1.txt` |
| End-of-check freeze verification | Every recorded permitted input hash unchanged |

The rational certificate uses 1000 deterministic cells, rational exponential
and arctangent bounds and exact inequality assertions; its printed decimals
are displays of the rational result. I make no inference about a new training
trajectory from it. The static graph has shared nodes, both action directions,
a bounded product, moving readout and a frozen observation. It is a useful
normalization/chain-rule check, not a proof for every observation graph or a
uniform cutoff-convergence experiment.

All retained results and exact subprocess commands are in `verification.json`
under the assigned scratch directory; its SHA256 is
`18667a58b21ed102d946ef35c9731bc2e5e0d26475ff8d38ac2df81747c4e6cc`.
The fresh check log hashes appear in the table below and agree with the frozen
logs. `completion_evidence.json` records required-skill hashes, fresh result
hashes, and the unchanged-input check.

The assembly script itself was fully read, but I did not execute it: its draft
construction intentionally reads unassigned study-side source packets. I
independently verified its actual output correspondence and reran the copied
checks instead. This avoids introducing those packets as scientific inputs.
The proposed maintained subsection contains no study path, report reference,
saved array, historical verdict, or unpromoted finding as a dependency.

The full old guide links chapters beyond this small standalone edition. Those
unchanged old links, guide examples for unrelated APIs, PDF rendering, and a
whole-book export were not tested. The new subsection's sole local Markdown
link and all copied checks operate within the supplied standalone edition.
This report does not claim that this selected-docs edition is a complete
standalone export of the entire existing library.

## Input SHA256 record

| Frozen input | SHA256 |
|---|---|
| P/integration_assignment_v3.md | `7d6623a17c694ff1c86e4c99781a389894270b147f1e9cc497ddd46b5b6d45ba` |
| P/candidate_v3.md | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` |
| P/README_proposed_v3.md = E/docs/README.md | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` |
| P/notation_v3.md = E/docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| P/guide_current_v3.md | `ae2f74fca1ecc93eed1f42dbcf3c8a79498546bad1b635adbba1310382f4afad` |
| P/instructions_v3.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| P/workflow_v3.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| P/review_inputs_v3.json | `18f37666301c8b9e1e497a045e3704ec74bf6999e3443f1c42934841e44eb446` |
| P/assemble_edition_v3.py | `f66535953f41f240155ab725e90e3848bd4b0d59838af4997022b749139f8428` |
| P/edition_manifest_v3.json = E/manifest.json | `c16db05d42932b885dec14fb0ad86e12289545d3b3fdd4500e13df1e7a8202e5` |
| E/docs/global_nonlinear.md | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` |
| E/docs/special_data_limits.md, hash only | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| E/docs/gaussian_calculus.md, hash only | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| E/README.md.patch | `f35ddd5e4d9b18afd6e048c75c12b9e761f377bef2509c3f62b2ec972b4af52b` |
| E/global_nonlinear.md.patch | `25f0d3b64f13edb70860e1a3788e029c569b16c8f1a5a241c36b64c549a5dadb` |
| E/checks/check_weak_identity.py | `0c2112077644de84cb9b5f6b41267297a241fd7c656d29869c18d1ecd35deb39` |
| E/checks/reference_certificate.py | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| E/check_0.txt = fresh_check_0.txt | `c7f2764a976fbfa9ee6f2f47e3aca7245065016a603249464f84e7517d32e8a0` |
| E/check_1.txt = fresh_check_1.txt | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` |

## Component verdicts and optional editorial observation

| Component | Verdict |
|---|---|
| Isolation and complete assigned reading | PASS; coverage and unread complement declared |
| Exact insertion, guide replacement, both patches, older-text preservation | PASS |
| Canonical normalization, population aliases, adjunction and clocks | PASS |
| Finite-type/mark accounting and same-population joints | PASS for C-H1 information scope |
| Cutoff interface, fixed-level interpretation and honest cost limitations | PASS |
| Reached restart statement and interface to older sufficiency | PASS within the specified older scope |
| Guide summaries, placement and duplication | PASS |
| New references and standalone copied checks | PASS |
| Whole-book scientific dependencies and full-library export | Outside this integration review |
| Required corrections or unresolved integration objections | None |

One optional editorial improvement is to make the new guide reference to
C.4.7.8 clickable and mention it in the existing chapter-role row. The current
plain reference is accurate, the heading exists, and the nearby paragraph
states the limitations; this is a navigation suggestion, not a required
correction or a condition of PASS.

Finite autonomous closure, quantitative cutoff/tail control, order-uniform
stability, population/input quadrature costs, and a certified useful solver
remain explicitly open. The integration PASS does not upgrade any of those
claims or replace the independent scientific and approval gates.
