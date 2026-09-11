# Neutral independent integration assignment — version 1

You are a fresh integration reviewer, distinct from every author, assembler,
selector and paired adversarial reviewer. Review the complete proposed C.4.8
addition in its assembled book context, the exact summary changes, notation,
interfaces, placement, duplication and preservation. This is not a fresh
whole-book proof audit. Do not read any earlier review, selection verdict,
study README/history, chats, other studies or Git history. Do not edit inputs.
Read AGENTS.md, RESEARCH_WORKFLOW.md, both required mathematical skills and
their applicable references personally; independent-review scope applies.

Authors/assemblers: `/root`, `source_response_route`, `statistical_route`;
mathematical contributor: `weak_topology_route`; selector: `promotion_selector`.
Paired reviewers are separate fresh agents. Their reports are not inputs.

## Complete new material and exact edits

Read the entire addition in
`data/generated/trained_prediction_sampling/standalone_v1/docs/global_nonlinear.md`,
lines 11440–12974 (all of C.4.8), and compare it byte-for-byte with the complete
`studies/trained_prediction_sampling/proposal_C4_8.md`.
Read all of `studies/trained_prediction_sampling/promotion_edits.json` and
all of the assembled `docs/README.md` and `docs/NOTATION.md` in standalone_v1.
Review the full source of `validate_proposal.py`, `check_gaussian_calculus.py`
and `check_sampling_hoeffding.py` from this study. No maintained code is added;
these are self-contained deterministic verification tools, not empirical work.

Verify these frozen hashes:

| Input | SHA256 |
|---|---|
| proposal_C4_8.md | 53ef8e1c31795ecd1ae8400c9ed8183cc8f1a86a2e71c74a0d736b7eb2b33456 |
| promotion_edits.json | 8aaa48600193350eb1539929c58e4c4db999e842921a6072ca1b113060191027 |
| validate_proposal.py | fc03a4933832ee1adf0c72be5886639c35ac60ea7f662433ee5101ea55b79458 |
| check_gaussian_calculus.py | 118b4d359f9c0e2dcfd42ab3b70df2c3e7970d940f9c1c463aaf96df13700cef |
| check_sampling_hoeffding.py | 4a681e66870b25bccaed976cfc171bc29491a28ea235e15be0e64f9a0f5c807a |
| standalone_v1/docs/global_nonlinear.md | d1ebb0763c6cdfcdfa7465bac3adea3a51f28a0b6129f889e059c128249738ac |
| standalone_v1/docs/README.md | 5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f |
| standalone_v1/docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

Short source names are relative to `studies/trained_prediction_sampling/`;
standalone_v1 is relative to `data/generated/trained_prediction_sampling/`.

## Precise older read scope and unread complement

Read live `docs/README.md` and `docs/NOTATION.md` completely. In the original
`docs/global_nonlinear.md`, read these ranges for interfaces and placement:
1–32; 1803–1835; 3836–3980; 5268–5472; 6902–7167; 8976–9293;
9294–9605 (source-recursion and cap interface); 10300–10608 (completion,
finite capture and the reference-contamination statement). Read
`docs/finite_dynamics.md` 1–227 for metric/finite-GF conventions. The remaining
older chapter bodies are explicitly outside this integration review. Gaussian
construction and the earlier long proofs receive their complete dependency
audit in the separate paired-review scope, not by implication here.

The original hashes are: global_nonlinear
`9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226`;
README `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a`;
NOTATION `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`;
finite_dynamics `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a`.
The validation program also byte-reads the explicitly frozen Gaussian dependency
excerpt; this is an assembly input, not an expansion of the scientific read
scope or a claim that you audited its unread proof.

## Independent validation and output

Run a fresh standalone assembly and isolated verification:

```
python studies/trained_prediction_sampling/validate_proposal.py --output data/generated/trained_prediction_sampling/integration_v1_edition
```

Inspect its outputs and exact inverse-preservation check, and independently
check the new navigation link, equation labels/references, model/normalization,
the distinction between C(circle) influence and H-valued CLT, the bounded
extension, and width-first scope. The addition must work without any study
proof/history/retained array as a scientific dependency. No training experiment,
full-book exporter audit, or unrelated code testing is required.

Write only `studies/trained_prediction_sampling/integration_v1.md` and scratch
under `data/generated/trained_prediction_sampling/integration_v1/`, plus the
fresh edition directory in the recipe. Record all complete reads and truncation
repairs, hashes before and after, commands/results, scientific/presentation
objections, and a clear complete/blocked verdict. State the unread complement
honestly. Do not contact other reviewers, perform Git operations, or alter the
established book. Report missing inputs before expanding scope.
