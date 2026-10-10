# Source and candidate audit record

Date: 2026-10-10. This study uses no other study's research.

## Primary inputs

- Current task's explicit proposed theorem and derivative grammar.
- `docs/index.qmd`, completely read; SHA256 `8246e044093b241d51b5eb964d65932dbe5d4e7f97a61f1389c9f16eb5402a68`.
- `docs/notation.qmd`, completely read; SHA256 `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
- `docs/12-three-sample-learning.qmd`, complete relevant finite-program theorem and proof III.F.1-III.F.6, lines 316-688, read in full. Whole-file SHA256 `6811e9e8c0557416920c9a1bd8a144807c4f3a9d4aaac134259130c81c7f148d`. No other chapter passage is an unstated dependency of the candidate.
- Golikov and Yang, *Non-Gaussian Tensor Programs*, NeurIPS 2022: main paper downloaded from the official proceedings and read; PDF SHA256 `05569ae157ef8e5adb43cadcae39426949ba1f855112a227c7145ea9639d3dac`.
- The official supplementary ZIP's `appendix.pdf`, SHA256 `d72e99b926952aa133d28f21216783f46ea652c5877a68bd5d765563a7f4adb8`. Complete relevant Appendix I and J moment argument read (extracted lines 1080-1720), together with the elementary inequality/Taylor/chain-rule conventions in Appendix H. Unrelated application, numerical and interpolation sections are not dependencies of our direct Gaussian proof.

Downloads and extracted text live in `data/generated/mfp_gaussian_master_proof_20261010/sources/`. The archive's code and notebooks were not run. Public URLs are in the candidate's source list.

## Main source finding

Theorem 3.7 of the 2022 paper already asserts all-finite-Lp scalar convergence for polynomially smooth Tensor Programs, under entry moment assumptions satisfied by Gaussian matrices. Its Appendix J supplies uniform moments with constants controlled by finitely many derivative/moment bounds. The candidate does not invoke that conclusion as an unexplained hypothesis: it gives the elementary moment induction and combines it with a reproduced Gaussian conditioning/clipping proof. The mixed finite-difference cancellation refinement was supplied by the scoped moment agent after independently freezing its Meyer route.

This corrects the earlier impression that the required polynomial-growth/moment bridge lacked a suitable existing result. No mathematical novelty claim is made for the probability theorem.

## Internal review packet v1

Frozen candidate: `master_proof.md`, SHA256 `c4abad79d33496a1d8259d88faa6a6747d58c0017a3d8401298629d506b1d823`.

Fresh reviewers `master_review_one` and `master_review_two` received no inherited task discussion. Each was assigned only the complete frozen candidate, neutral instructions to reconstruct every step and seek gaps/counterexamples, and required proof/notation skills. Neither may read the study README, history, route files, another review, or external scientific sources. Their separate owned outputs are `review_one_v1.md` and `review_two_v1.md`.

Required checks: uniform all-order raw-entry derivatives over Gaussian variance profiles; exact singleton finite-difference cancellation; constants uniform in cutoff; error interpolation in the joint neuron/probability measure; true matrix reuse without independence shortcuts; Gaussian conditional law; degenerate-Gram removal without inverse continuity; scalar feedback; exact gradient scaling and moving-direction jets; restricted activation-moment closure; all expectation/limit exchanges.

This is internal checking, not book promotion or proof-assistant verification. The candidate remained unverified until both reports were complete and read by the root agent.

## Final resolution

Both fresh isolated reviewers returned PASS for the exact declared finite-program theorem, with no mathematical correction required. Both read every line of the frozen candidate and reconstructed the complete proof, including the moment induction, singular conditioning, clipping, derivative compilation, and restricted activation-moment reduction. The root agent read both complete reports and checked their findings against the proof. No unresolved mathematical dependency is retained from either alternative route.

After review, the only change to `master_proof.md` was its single status line, changed from candidate/awaiting reconstruction to complete/internally checked. Replacing that line with its old text reproduces the frozen SHA256 exactly; the reviewed scientific body is unchanged.

- Final `master_proof.md`: SHA256 `55d979e9dbab1c13bc1f84a43b001efe9fefa6bd1b565d4479245ef5128a3388`.
- `review_one_v1.md`: SHA256 `a57d00ae76277cd21f3bb0bb7dc5ac4a127b309b187ed5c6d10a18901903185d`.
- `review_two_v1.md`: SHA256 `5f9c0262326e7c539c2ad72b9fa373094881fea4b529379ddceecc9e270bc9e5`.

Read-only text validation also checked paired display-math delimiters, the unique ordered equation tags 1 through 30, and absence of trailing whitespace. These are presentation checks, not mathematical evidence; the mathematical checks are the proof reconstructions above. No numerical experiment or formal proof assistant was used. No maintained-book file, Git staging, or commit was changed by this study.
