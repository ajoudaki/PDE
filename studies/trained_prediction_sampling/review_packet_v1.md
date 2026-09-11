# Neutral complete adversarial review assignment — version 1

Review the proposed canonical addition `proposal_C4_8.md` and the exact related
summary edits in `promotion_edits.json` for mathematical correctness and scope.
The candidate concerns the exact C.4.7 two-hidden-layer tanh model at physical
time 40, for every separately fixed Borel law in a positive smaller W1 ball.
It claims an actual centered whole-circle influence, an empirical remainder
with m E||r||_H^2 tending to zero, an H=L2(circle) Gaussian sampling limit with
spatial covariance, and a width-first actual finite-GF bridge. No finite-width
rate, joint fluctuation rate, ambient L2 tangent, GD extension, or nondegenerate
covariance is claimed.

You are a fresh isolated adversarial reviewer. Authors/assemblers are `/root`,
`source_response_route`, and `statistical_route`; `weak_topology_route` also
contributed mathematical reconstruction. The independent selector is
`promotion_selector`. You must be distinct from all of them and from the other
reviewer. No inherited task conversation, study history, internal verdict,
selection report, or other review is an input. Do not read other studies, Git
history, or any study artifact not explicitly listed below. Read required
skills and process instructions; scoped independent-review rules replace
ordinary author startup and study README reading.

Read every scientific line of the candidate and the complete dependency bodies
listed below. Repair truncated tool reads. Audit hypotheses, constants,
boundary/zero-mass/singular-rank cases, source-information flow, feedback,
limit orders, centering and Bochner integration, nonatomic empirical laws,
exceptional events, covariance and actual finite GF. Do not substitute a
generic formal ODE theorem for the unbounded-multiplication issue. Assess the
actual source recursions and their mesh-uniform derivative proof. The
deterministic checks below check identities only and cannot certify the neural
estimate. Run them in fresh reviewer-owned generated paths and inspect their
complete implementations and outputs.

If a scientific dependency is missing, report it before retrieving anything
outside this packet. Additional established material can be supplied in a new
complete packet. Do not infer a passing verdict from a theorem label or a
claimed earlier check. Save all actual attacks and their outcomes, including
unresolved objections. Do not edit candidate or established files.

## Exact frozen inputs

All paths are relative to `/home/amir/Codes/PDE`. A line range specifies the
complete authorized dependency excerpt; unread complements are not part of
this proof audit. Hashes are of the complete named file, so they also detect
concurrent source changes. Sections included are complete at both endpoints.

| Input | Complete required read scope | SHA256 |
|---|---|---|
| studies/trained_prediction_sampling/proposal_C4_8.md | all 1535 lines | 53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456 |
| studies/trained_prediction_sampling/promotion_edits.json | all | 8aaa48600193350eb1539929c58e4c4db999e842921a6072ca1b113060191027 |
| studies/trained_prediction_sampling/check_gaussian_calculus.py | all | 118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef |
| studies/trained_prediction_sampling/check_sampling_hoeffding.py | all | 4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a |
| docs/global_nonlinear.md | 1840–2453 (A.1–4 and B.1); 2924–3440 (C.2); 3836–4946 (C.4.1–3); 5268–11436 (complete C.4.5–7) | 9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226 |
| docs/special_data_limits.md | 3785–4286 (complete Gaussian construction III.F.1–10) | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/finite_dynamics.md | 1–227 (complete model, GF and finite-time bounds §§1–4) | a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a |
| docs/README.md | all | 5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a |
| docs/NOTATION.md | all | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| AGENTS.md | all | 7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba |
| RESEARCH_WORKFLOW.md | all | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

Personally read `solve-math-rigorously` and `investigate-conjectures` and the
applicable references required by them. No maintained code API is used or
changed by this package; the two check programs use the standard library only.
There are no training experiments or empirical claims to reproduce.

## Output ownership and validation recipes

Reviewer A writes only `studies/trained_prediction_sampling/review_v1_A.md`;
reviewer B writes only `studies/trained_prediction_sampling/review_v1_B.md`.
Each uses its matching `data/generated/trained_prediction_sampling/review_v1_A/`
or `review_v1_B/` scratch. The sampling check additionally requires its output
directory under the study's statistical-check namespace, as shown below.
Use A or B consistently in these recipes; these paths are mutually disjoint.

```
python studies/trained_prediction_sampling/check_gaussian_calculus.py --output data/generated/trained_prediction_sampling/review_v1_A/gaussian_report.json
python studies/trained_prediction_sampling/check_sampling_hoeffding.py --output-dir data/generated/trained_prediction_sampling/statistical_checks/review_v1_A
```

The report must include exact input hashes (verified before and after), complete
read coverage with truncation repairs, isolation and authorship confirmation,
commands/attacks/results, component verdicts, and every required correction or
unresolved objection. Distinguish a presentation suggestion from a correction
needed for a valid complete proof. Conclude whether the entire frozen package
passes or is blocked, with precise reasons. No Git operations or messages to
the other reviewer are authorized.
