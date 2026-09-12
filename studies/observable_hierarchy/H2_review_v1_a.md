# C-H2 review A, frozen version 1 — interrupted and incomplete

Reviewer: `/root/h2_review_v1_a`. Date: 2026-09-12. Repository cwd: `/home/amir/Codes/PDE`.

**No overall review verdict is issued.** This report is an original record of an interrupted review, not a complete review or an acceptance decision. I stopped substantive review at the supervisor's explicit instruction. The supplied reason was: “A parallel code relevance selector requires two small code-guide assembly clarifications (actual parameter name and standalone description of later milestones). The proof/module/tests are unchanged, but we will preserve v1 and issue a new frozen packet before fresh complete paired reviews.” I did not inspect that selector's findings, make those changes, or read a replacement packet.

## Identity, isolation and authority

I did not author, assemble, or select the package. My scientific input scope was solely the neutral `H2_review_assignment_v1.md`, `H2_review_inputs_v1.json`, and the explicitly listed frozen inputs. The scoped assignment replaced ordinary author startup. I did not read the study README, other studies, prior reports/verdicts/history, Git history, or another reviewer's work. No research subagent was spawned. The supervisor's stop instruction supplied procedural information only. All writes are confined to this report and `data/generated/observable_hierarchy/H2_review_v1_a/`. No input or Git state was modified.

I independently read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and `/etc/codex/skills/investigate-conjectures/SKILL.md`, plus the latter's references `research-contract.md`, `adversarial-audit.md`, `evidence-ledger.md`, and `decisive-experiments.md`. The review had authority for mathematical analysis and bounded deterministic static checks only. No training or empirical campaign was authorized or performed.

## Exact completed reading

The following scientific inputs were read completely: assignment (151 lines), proposed section (470), C-H1 candidate (642), dependencies (3569), prototype module (693), tests (283), and prototype notes (277). This is 6085 complete-read manifest lines. The manifest itself was read completely (186 lines). No scientific file was treated as read merely because its bytes were hashed.

Read calls and truncation repairs were:

- `cat studies/observable_hierarchy/H2_review_assignment_v1.md studies/observable_hierarchy/H2_review_inputs_v1.json` — complete output.
- `cat /etc/codex/skills/solve-math-rigorously/SKILL.md /etc/codex/skills/investigate-conjectures/SKILL.md` — complete output.
- `cat` of the four required investigate-conjectures references, followed in the same tool batch by `sed -n '1,520p' studies/observable_hierarchy/H2_proposed_section_v1.md` — the combined output was truncated. I repaired the reference tail by reading `decisive-experiments.md` alone, and the proposed-section prefix by `sed -n '1,180p'`. The displayed proposed-section tail and that repaired prefix cover every line 1–470. The other three references were fully visible in the original batch.
- `sed -n '1,642p' studies/observable_hierarchy/candidate_v3.md` — complete.
- Dependencies were read by `sed -n` ranges `1,500`, `501,780`, `781,1210`, `1211,1650`, `1651,2070`, `2071,2500`, `2501,2910`, `2911,3330`, and `3331,3569`. The first output was truncated around III.F.4–5; I repaired it with `230,350`, including the entire missing substitution and singular-query proof. The union covers every dependency line 1–3569.
- Prototype module: `sed -n '1,360p'` and `sed -n '361,693p'` — complete.
- `cat studies/observable_hierarchy/H2_test_prototype.py studies/observable_hierarchy/H2_prototype_notes.md` — complete.

Not yet read: obstruction packet, full guide packet, proposed book/code guides, assembly/edition/check/validation recipes and manifests, maintained API files. Correspondence-only full sources were hashed but neither excerpt correspondence nor their required portions were independently inspected. These outstanding obligations alone prohibit a completed review verdict.

## Independent derivations and adversarial work completed

These are provisional checks, conditional on completing the entire assigned audit. They are not component acceptance verdicts.

1. **Finite dictionary and information boundary.** I checked the Cantor decoding termination: every parent code is smaller than its constructed code. Rational scales, addition, bounded products, unary gates and both orientations can encode each finite tree; unfolded DAGs are included. The pilot has 14 nodes, so adding at most N+1 codes gives at most N+15 nodes before retaining bounded outputs. The retained spans are nested even though their ridge coordinates vary. The matrix M has observable-basis indices, independent of width; its D initialization consists of deterministic limiting contractions. Thus the displayed representation does not immediately collapse to a coordinate transform of an n-by-n trainable middle array. Actual population laws, with nonlinear w/c coordinates outside the feature span, are explicitly permitted by the assignment. I checked the absence of target trajectory values or time-indexed forcing in H2.4–H2.6.

2. **Filter and density calculation.** For S a synthesis map with Gram G, Q=S(G+eta I)^(-1)S*. On v=Sa, `(I-Q)v=eta S(G+eta I)^(-1)a`. The spectral multiplier is `eta sqrt(lambda)/(lambda+eta)`, whose maximum over nonnegative lambda is `sqrt(eta)/2`. Zero-padding an earlier coefficient vector keeps its norm fixed. Dense bounded Fourier cylinders and contraction bounds then yield strong convergence without a minimum Gram eigenvalue. I explicitly distinguished strong convergence from operator-norm convergence; finite-rank Q cannot be assumed to approach identity in operator norm on an infinite-dimensional space.

3. **Gradient metric and filtering.** With a=E1[b1 h1], d=E2[b2 c phi'(z2)], variation in M gives `delta f=d^T delta M a`. Thus the Euclidean coefficient gradient is `2 integral r d a^T`. Variation in w and c yields the stated reverse contraction M^T and physical factor two. Writing `K_N=U2(M-D)U1*`, its velocity is `Q2 F_K Q1`, not an unrestricted raw HS gradient. This establishes the algebra needed for H2.7 and H2.14 without falsely identifying the Frobenius coefficient norm with the induced HS norm. The inequality `||K_N||HS <= ||M-D||F` uses contraction of U1/U2.

4. **A priori bounds and fixed-order existence.** The local characteristic variables are `(w-g,c,M)` in supremum/finite Euclidean spaces; bounded b and bounded gates give a finite local Lipschitz constant at each fixed N. The unbounded Gaussian g is a frozen argument inside globally Lipschitz bounded gates. Energy gives `integral |r| <= Y`, then `||c||infinity <= 2Yt`, `||M'||F <= 4Y^2 t`, and `||M-D||F <= 2Y^2 t^2`. The row L2 bound follows from `||A_N|| <= 2+2Y^2t^2`; a separate fixed-N feature-envelope bound controls the row supremum increment for continuation. I checked the distinction between bounds uniform in N for comparison and bounds allowed to depend on N for fixed-order well-posedness.

5. **Error production and nonlinear propagation.** Compact target argument sets follow from L2 continuity in `(t,u)` on a compact parameter domain. Uniformly bounded strong convergence is uniform on such sets by a finite epsilon net. Strong two-sided Q approximation extends from finite-rank tensors to a compact HS curve K' through HS contraction. These facts provide the actual small source eps_N; eps_N is not used by the scheme. Subtracting the upper backward field uses bounded reference c. The lower multiplier is split at the tail of the unchanged target Q, producing one factor R and one target tail. I checked the Osgood substitution: for v=e+eps+eta, choose `R=1+a^(-1)log(1/v)` while v<=1; `z=log(e/v)` satisfies `z' >= -Lz`, giving the displayed positive-power modulus. This compares directly to canonical GF and avoids an appeal to uniqueness of arbitrary formal hierarchies. The dependency tail proof was read completely, including the separate reference-clock-to-raw and raw-reference-to-nearby-law bootstraps; no numerical confirmation of it was substituted for a proof.

6. **Joint observations and activity.** The same-carrier coupling bounds joint Euclidean W2 by the sum of node L2 errors, rather than separately coupling marginal observations. Both action directions use the same matrix and its transpose. Quadratic contractions follow by two Cauchy–Schwarz terms. I checked the reference small-time activity factors: weights one half and physical factor two give c(t)=tS+o(t), lower displacement `(y_a/2)t^2 V_a`, and analogous upper displacement. The adjoint pairing and positive sum in H17–H18 supply nonzero coefficients without an analyticity assumption. The fixed law-radius/activity continuity argument is distinct from the order limit.

7. **Module inspection.** I read the Gaussian compiler and its derivative mechanism completely. It forms uncentered source covariances, computes derivatives in named correlated-source slots with coefficients frozen, retains both response directions, and extends sources by a factor/QR conditional representation. It retains positive innovations and reports small negative-Schur corrections. I followed initialization through compilation of the full contraction union before extracting the two joint laws and normalizations. Runtime actions are explicit weighted finite contractions, and the RHS uses the coefficient gradient derived above. State save/load includes current populations, frozen marks, M, D, data and metadata, with no time/history coordinate. This is inspection only: I did not execute the prototype or validate numerical behavior.

Adversarial alternatives considered included loss-factor mismatch, treating the coefficient metric as an isometric middle reparametrization, discarded singular Gram modes, independent reverse Gaussian substitution, arbitrary-vector Gaussian oracle use, operator-norm convergence replacing strong convergence, assumed rather than proved small error production, two unrestricted L2 factors in a claimed L2 algebra estimate, independent marginal coupling, and temporal analyticity used for activity. I did not identify a decisive counterexample during this partial inspection; this statement supplies no assurance about the unread obligations or checks not performed.

## Commands, deterministic outcomes, and limits

All read commands above ran from `/home/amir/Codes/PDE`, exited zero, and only displayed frozen text. After the stop instruction I performed a metadata-only SHA-256/line-count check of the exact manifest-listed paths using Python 3.10.12, `python -B`, pathlib/hashlib/json, and recorded its full structured result in `data/generated/observable_hierarchy/H2_review_v1_a/input_hash_check.json`. No scientific source outside the manifest was fetched. Environment reported `Linux-5.15.0-151-generic-x86_64-with-glibc2.35`; Python was `3.10.12 (main, Aug 31 2026, 10:18:17) [GCC 11.4.0]`. Exit zero. Result: all 32 input hashes match, all 32 line counts match. Hashing reads bytes for integrity only, not scientific coverage.

The manifest itself has SHA-256 `8ed8b5f15ff38835b4b03139300c4b94050316d7399870df448d59bbaaf616a2`, 186 lines.

**Not executed:** supplied 13-test suite, document/source correspondence check, fresh-edition assembly, relocated suite, code-guide API example, or new adversarial numerical checks. No OPENBLAS/OMP-controlled test process was started. No training trajectory, accuracy exploration, Monte Carlo, or time-40 solver was run. Existing test assertions and author-reported passes are not independent execution evidence.

## Component status

| Required component | Status at interruption |
|---|---|
| Finite closure and nonvacuity | Provisional derivations completed; no verdict |
| Gaussian initialization | Mathematical/source implementation inspection completed; static execution outstanding; no verdict |
| Well-posedness and own-state restart | Provisional proof inspection completed; restart test outstanding; no verdict |
| Convergence and dynamic identification | Proposed proof and complete dependency bodies read; obstruction/guide audit outstanding; no verdict |
| Joint observations and second moments | Provisional derivations completed; numerical maps unchecked by execution; no verdict |
| Activity and admitted family | Provisional derivations completed; no verdict |
| Code producer, RHS and maps | Complete module/test inspection; all actual tests outstanding; no verdict |
| Reusable API and numerical limitations | Prototype notes read; code guide, recipe, relocation and example outstanding; no verdict |
| Complete-read and source correspondence obligations | Incomplete |

No required scientific correction or optional editorial change is being proposed by this incomplete review. The supervisor's supplied assembly-clarification reason is recorded above without independent adjudication. A complete fresh frozen-packet review is required before any overall PASS can be issued.

## Exact frozen input hashes and coverage

Every actual hash below equaled the manifest's expected hash. `Not read` and `correspondence not checked` remain incomplete even though their hashes match.

| Frozen input | Lines | Actual SHA-256 | Scientific read coverage |
|---|---:|---|---|
| `studies/observable_hierarchy/H2_review_assignment_v1.md` | 151 | `ebb34a26a88c15021663cbd4037a21b38c42675d64004080552f163dd7cd96a8` | 1–151 |
| `studies/observable_hierarchy/H2_proposed_section_v1.md` | 470 | `3f142c4f5f364f65cb5a5c487fdbca38efccd1872741cd5815a661647c6f5b99` | 1–470 |
| `studies/observable_hierarchy/candidate_v3.md` | 642 | `f9a20bf6519c802581d293e3cde02218020c127c683699b0a93be9eda277aae2` | 1–642 |
| `studies/observable_hierarchy/dependencies_v1.md` | 3569 | `6a40bc9ee6e6de49fbefd9118298c4ab807b1ef52ecf29b99a71937eab0a63d7` | 1–3569 |
| `studies/observable_hierarchy/H2_obstructions_v1.md` | 875 | `9cc2a505a70368e6b042f6b7449bbd9f38b3866838a62e78427644ec2edfd77d` | Not read |
| `studies/observable_hierarchy/H2_guides_v1.md` | 1673 | `c6b78aa9fa374db2f949b15dcf8f38f630423f94f0281425bf39bfcb64eb1faa` | Not read |
| `studies/observable_hierarchy/H2_docs_README_v1.md` | 668 | `3fdc01dc3bca4c1e8ea4888e8f2fa01ec056ffc45658f53486c82e2532f04341` | Not read |
| `studies/observable_hierarchy/H2_code_README_v1.md` | 744 | `0661c6549469082d0f1174977a5775111876e5d5e40f9c940c8b9b537f5df874` | Not read |
| `studies/observable_hierarchy/H2_prototype.py` | 693 | `0b2ef5c283698ae077f8dedda1fd485728bbfe00d7624681d74ff4a39d35afd2` | 1–693 |
| `studies/observable_hierarchy/H2_test_prototype.py` | 283 | `fe976db10472fc877c2ad6b8f08419b2d390e25f0f9f62c3640a17a502c2d058` | 1–283 |
| `studies/observable_hierarchy/H2_prototype_notes.md` | 277 | `af26490945a4e5e604afc1f7c3ad00f6a3ab2042206f4f4de4147624e5bf0eca` | 1–277 |
| `studies/observable_hierarchy/H2_assemble_edition_v1.py` | 67 | `27af5fbffc6a03972b4cf02f0eb1125b90b0b17f44447cfbb125d15af0022d5a` | Not read |
| `studies/observable_hierarchy/H2_edition_inputs_v1.json` | 46 | `b6890ed36dcc62f6321d37432b7e6256074a9d8a6deccdd336fcbe261ce8ae10` | Not read |
| `studies/observable_hierarchy/H2_check_documents.py` | 63 | `716c6d51ba20e4bc87692af8bdade84f95cd69e856b2c240370574320bec8906` | Not read |
| `studies/observable_hierarchy/H2_validate_edition_v1.py` | 75 | `224505f69ab9d4b61820c9c02321207e46d64613e76272ffc91c7fbba7b9f21d` | Not read |
| `studies/observable_hierarchy/H2_source_hashes.json` | 12 | `09aeeaad1ee3b6081d7604113f0a414226c4e60a7fdcda5cfb11ae608c3f307a` | Not read |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` | Not read |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` | Not read |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` | Not read |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | Correspondence not checked |
| `docs/README.md` | 654 | `a402cd21b58fe889500ca9ba9e79aa8d2e1fbbbe371ea2a577f3fafdae69455d` | Correspondence not checked |
| `docs/arctan_limits.md` | 3117 | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` | Correspondence not checked |
| `docs/continuous_depth.md` | 2825 | `12be7aafbf37cb3651facdcac9c5333281b793c96b96a8a52a1232cd86ca006d` | Correspondence not checked |
| `docs/finite_dynamics.md` | 1275 | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` | Correspondence not checked |
| `docs/finite_optimization_and_controls.md` | 5112 | `80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628` | Correspondence not checked |
| `docs/gaussian_calculus.md` | 9580 | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` | Correspondence not checked |
| `docs/global_nonlinear.md` | 19396 | `434b3e6bfcdd71576e271ea35910fc1994b3a9c1bfb01acad92f302bdeb07e14` | Correspondence not checked |
| `docs/linear_dynamics.md` | 2803 | `8de3beaca0cd6f970c27a25eb8c2bc4a1fefa2e7840bd97e7bccfc4f41281c1d` | Correspondence not checked |
| `docs/special_data_limits.md` | 27274 | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` | Correspondence not checked |
| `AGENTS.md` | 47 | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` | Correspondence not checked |
| `RESEARCH_WORKFLOW.md` | 224 | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` | Correspondence not checked |
| `code/README.md` | 621 | `3cb90e55b630870c391e56158432a909fc60872b4af724756b2be19884ef7d6e` | Correspondence not checked |

Required skill/reference hashes (all read completely):

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
- `/etc/codex/skills/investigate-conjectures/SKILL.md`: `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de`.
- `/etc/codex/skills/investigate-conjectures/references/research-contract.md`: `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e`.
- `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md`: `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501`.
- `/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md`: `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e`.
- `/etc/codex/skills/investigate-conjectures/references/decisive-experiments.md`: `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9`.
