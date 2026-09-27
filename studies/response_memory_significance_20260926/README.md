# Response-memory authoring and adversarial rebuttal

## Objective

This study manages a versioned author–reviewer loop for the paper in
`/home/amir/Codes/PDE/paper/`. The objective is to produce the strongest
substantively defensible paper about response-memory closure, with exact prior-work
comparisons and a complete account of proof, state complexity, implementation, and
experiments.

This is no longer a verdict-first significance exercise. Review reports identify
specific mathematical, empirical, historical, or messaging defects. After each
report, the advocate revises the manuscript and writes a point-by-point response.
The next review is performed on a newly frozen version. The loop ends only when
factual disputes are resolved and the remaining disagreements are clearly labeled
evaluative judgments.

## Roles

- **Advocate/lead author:** has access to the complete response-memory study,
  maintained book, maintained code, existing generated experiments, current paper,
  and primary literature packet. It owns revisions to `paper/main.tex` and
  `paper/references.bib` and writes an author response after each review.
- **Adversarial reviewer:** receives only the current frozen candidate, the neutral
  assignments, and the shared evidence packet. It does not see chat history,
  unrelated studies, or preliminary novelty conclusions.
- **Final referee:** after the iterative loop stabilizes, receives the final frozen
  candidate, shared evidence, and the complete versioned exchange, then adjudicates
  any remaining claims from primary evidence.
- **Coordinator:** freezes versions, verifies input identity, checks changes and
  citations, and produces the final positioning record.

## Required comparisons

Every round must address the same exact distinctions:

1. HiPPO is assessed as an ingredient precedent unless an exact theorem or
   experiment is shown to satisfy the complete neural-closure contract.
2. Neural Tangent Hierarchy is compared by training regime, represented object,
   horizon/error theorem, order-`P` state growth (including the `O(m^P)` sample
   tensor count), test-output procedure, and empirical implementation.
3. Compression of the evolving learned increments is reported separately from
   total storage and runtime, including all fixed `W_0` matrices, their forward and
   transpose actions, Gram state, prefix state, solver stages, and observed runtime.
4. Fixed-width trajectory approximation is kept separate from a width-uniform
   population theorem and from all-time uniform control.

## Frozen version zero

- TeX: `FROZEN_MANUSCRIPT.tex`, SHA-256
  `daa583a94be0c32103761d3391bde7292e5d2c5d3fe6b2ea5f1530a411a36f21`
- PDF: `FROZEN_MANUSCRIPT.pdf`, SHA-256
  `f49ede7be2a271333c9ccf43e408b465b7081d3792ef966e0c6fb1e4509d935c`

The evidence inventory is `LITERATURE_PACKET.md`. It records sources and exact
locations without adopting a novelty verdict.

## Round protocol

For round `r`:

1. Freeze `CANDIDATE_Vr.tex`, `CANDIDATE_Vr.pdf`, bibliography, and hashes.
2. Reviewer writes `REVIEW_Rr.md`, with numbered objections and exact evidence.
3. Advocate writes `AUTHOR_RESPONSE_Rr.md`, revises the live paper, and maps each
   objection to a concrete change, reasoned rejection, or explicitly retained gap.
4. Coordinator checks that the response matches the diff, compiles the paper, and
   freezes `CANDIDATE_V(r+1)`.
5. Reviewer rechecks only after the new freeze. Resolved factual claims are not
   reopened without new primary evidence.

No new training campaign is authorized by this loop. Existing raw results may be
reanalyzed or checked without altering them.

## Current status

Version zero and the neutral evidence packet are frozen. The previous
verdict-oriented opening run was stopped before reports were written. Round zero
will begin with adversarial review of version zero, followed by the first author
revision.

