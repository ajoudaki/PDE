# Validation and experiments

No training experiment, historical campaign or empirical scientific experiment
was required or run. The user authorized workflow implementation and independent
audits. Bounded deterministic tests and a read-only application discovery probe
validate that implementation; they are not scientific evidence for PDE dynamics.

`VALIDATION.json` records the coordinator's exact ten-test invocation, environment,
exit status, helper/test hashes and generated log hash. Both reviewers additionally
ran supplied tests and independent rejection/rollback checks. Their full commands,
results and isolation qualifications are in the original reports; artifact hashes
are in `reviews/EVIDENCE.json`. The exact independent scripts are retained as source
under `reviews/evidence_A1/` and `reviews/evidence_B1/`, alongside the frozen inputs
needed to rerun them. `REPLAY_REVIEWS.md` restores their exact expected scratch
layout in a fresh selected-packet workspace; do not execute the preserved source
copies directly from their source-tree paths.

`AUTO_LOADING.json` records the fresh read-only Codex invocation, prompt/input
hashes, actual session, sole file-read command, result and raw event hashes.
The full long guide was read exactly; it was not itself automatically injected.
There are no seeds or stochastic scientific conclusions in these diagnostics.

All generated artifacts are in this study's `data/generated/` namespace.
Bootstrap coordinator/probe logs used distinct named files at the namespace root;
they are preserved as originally written. Reviewer/test workspaces use distinct
subdirectories. Future runs use fresh run directories under the permanent policy.
