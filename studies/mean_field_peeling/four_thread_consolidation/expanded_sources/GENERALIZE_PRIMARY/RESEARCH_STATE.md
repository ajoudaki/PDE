# Destination supervisor research state

Current task: Generalize non-local GF limit, 01a07193-3b8a-77a1-a00f-4ae928368b82.
Verified host: remote-ssh-discovered:black-chatgpt; OS hostname ubuntu22-black.
Verified saved project: PDE, /home/amir/Codes/PDE. Current app project id:
bb66c3ec-020d-4fb6-b0b8-88d81725eece (the handoff's earlier id is stale).
Work isolated in /tmp/pde-gf-supervisor-worktree on codex/gf-population-generalization,
from commit 6300e92. Existing checkout and its user changes were not edited.
The source task remains idle; no old subagent was resumed or assigned work.

Authority: theoretical extension and independent adversarial checking. No
numerical experiments or external messages are required. No goal was created.

Contract: fixed finite data and fixed depth, stored muP scaling, arbitrary
eta_n->0 jointly with n->infinity, a positive width/step-independent physical
time horizon, current field/operator state, actual feedback GD. A fixed-mesh
oracle is only a proof construction, not the limiting state or an algorithm
substituted for actual GD. Separate convergence from strict nonlinear activity.

Source identities (available on this destination):

- THREE_INPUT_LOCAL_LIMIT_PROOF.md, sha256
  08c96e9b4dff421d99e7213509bb3bec3adf1d7c897ea9cc436e4e6f02d1a95b.
- THREE_INPUT_LOCAL_LIMIT_REVIEW.md, sha256
  2c84f5dee8998ad39a9e56d0c2ce89b81f6663b2ef4dde3a387e26e2119431c1.
- THREE_INPUT_SCALED_LIMIT_EXTENSION_CHECK.md, sha256
  eeb5b0b2b206fa5318e50840b5b9dcec663b1f4433239d3d602dfbbfe963a051.
- three_input_activity_lemma.md, sha256
  02a7c6e3862d0c72b75d93e95d9e26cf3c7efe077bb17f5473e3da580f3d0c00.
- GENERAL_ACTIVATION_ACTIVITY.md, sha256
  c6bfa76ac200ce59f91109b31a40d22d668ec678e2ea60386f93f7d7604b4e89.
- GENERAL_DEPTH_LIMIT_CHECK.md, sha256
  e5c19b1e79111e8aea0d634fa519c5384b741a9dd48704f7a7a28bda5d3a5113.
- L2_FULL_AUDITED_PROOF.md, sha256
  e9f963cde5061f4f5b4d8d3913a62ccd013af451334e46356134f624759d42fb.

All original sources are in /tmp and are left unchanged. The old depth note
is a draft for bounded activations, not evidence for unbounded activations.

| Claim | Present status | Required evidence |
|---|---|---|
| Prior local two-layer arctan theorem | Previously reviewed; bridges rechecked | Original proof/review |
| Smooth globally Lipschitz, subGaussian-readout response bound | Proved, independently reviewed | Detailed response proof; all three reviews |
| Arbitrary fixed-depth response bound | Proved, independently reviewed | Weighted pulse and noncircular bootstrap; all three reviews |
| C1,1 joint width/step theorem | Proved, independently reviewed | Full proof; all three reviews |
| Broad two-layer strict activity | Proved within the constructed-flow class | Activity audit and independent reviews |
| Arbitrary-depth strict activity | Open here | Separate proof |
| ReLU or non-Gaussian middle universality | Open here | New estimates/theorem |
| All finite horizons or novelty priority | Not claimed | Separate analysis |

Three fresh reviewers, given the written theorem and necessary response lemma
without derivation history, completed independent adversarial reviews. All
returned PASS with no required mathematical repairs. They checked primary
sources directly. Their reports and reviewed hashes are retained in
INDEPENDENT_REVIEW_A.md, INDEPENDENT_REVIEW_B.md, INDEPENDENT_REVIEW_C.md.
After their reviews only the proof's status lines and the explicit repetition
of its existing Gaussian-first-weight activity hypothesis were changed.

The former bounded-activation-only depth draft is superseded for existence by
GENERAL_DEPTH_RESPONSE_PROOF.md plus GENERAL_POPULATION_GF_PROOF.md. Its scope
exclusions remain valid descriptions of what that older draft alone proved.
Strict arbitrary-depth activity, ReLU, and non-Gaussian middle universality
remain separate open extensions here. No numerical experiment was performed.

The copied baseline and activity sources in sources/ preserve their original
hashes. GF_RESULT.md is the readable result; REVIEW_RECORD.md indexes evidence.
