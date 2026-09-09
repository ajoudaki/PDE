# Completed independent review record

Date: 2026-09-05.

The completed theorem is in
[GENERAL_POPULATION_GF_PROOF.md](/tmp/pde-gf-supervisor-worktree/GENERAL_POPULATION_GF_PROOF.md).
Its essential uniform response estimate is in
[GENERAL_DEPTH_RESPONSE_PROOF.md](/tmp/pde-gf-supervisor-worktree/GENERAL_DEPTH_RESPONSE_PROOF.md).
The concise statement is
[GF_RESULT.md](/tmp/pde-gf-supervisor-worktree/GF_RESULT.md).

Three fresh reviewers received the written proof and its dependencies without
the derivation history. None relied on the other reviewers' verdicts. All
returned PASS and identified no remaining mathematical gap requiring repair.

- [Review A](/tmp/pde-gf-supervisor-worktree/INDEPENDENT_REVIEW_A.md): exact
  response laws, weighted sensitivities, cap order, source hypotheses, operator
  construction, unbounded-readout proxy, and C1,1 passage.
- [Review B](/tmp/pde-gf-supervisor-worktree/INDEPENDENT_REVIEW_B.md): all of
  those bridges, with detailed checks of velocity, path, probe, general-loss,
  and initialization-perturbation assertions.
- [Review C](/tmp/pde-gf-supervisor-worktree/INDEPENDENT_REVIEW_C.md): response
  proof, convergence bridges, smoothing, and the strict two-layer activity
  proof including weighted constants and reused-matrix conditioning.

All checked the cited primary Tensor Programs sources. These are independent
mathematical reviews, not proof-assistant verification.

Reviewed theorem SHA-256, after adding activation examples:
792dbd8eca426dc8fd5434d67b183826025a7a301f42fd579d6332fa458005e2.
Reviewed response SHA-256:
3dfb63e3cac21ee15573af7f4107287f58dc2013db7e4a11083c90472bf8995b.
Reviewed activity-audit SHA-256:
3d91ef619477525519a7faacd293418b15e7f2f24699ed871df6eef11b194421.

The final theorem differs from that reviewed version only in its status
paragraph and an explicit repetition of the already-declared Gaussian
first-weight hypothesis in the strict-activity corollary. No estimate,
assumption, or theorem scope was broadened after review. The final artifact
hashes are recorded in FINAL_SHA256SUMS.txt.

The result is local in physical time, at every fixed depth and fixed dataset.
Existence allows degenerate geometry and nonzero subGaussian readout. The
strict feature-activity result remains two-hidden-layer, zero limiting readout,
Gaussian first weights, nonaffine activations, positive scales, pairwise
nonparallel normalized inputs, and nonzero labels. The review does not establish
all-time control, a depth-uniform interval, ReLU, non-Gaussian middle-matrix
universality, or publication priority.
