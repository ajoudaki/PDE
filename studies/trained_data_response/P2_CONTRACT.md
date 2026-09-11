# Milestone 2: nonlinear trained-law continuation

Author/coordinator: task `01a09106-41c4-7193-9db9-8068144fd825`, `/root`.
Claim status: full author candidate frozen for two fresh complete reviews.
No A–C success or promotion is asserted before those gates pass.

## Fixed contract

Use the exact two-hidden-layer tanh model on normalized circle inputs,
stored Gaussian variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved
exact squared-loss integrals, full Gaussian first row and actual finite
random readout. The reference is the equally weighted opposite-label law
on the two coordinate directions. All statements fix physical time 40.

A: find a positive width/sample-independent Wasserstein radius among all
bounded-label Borel laws, with autonomous strong population GF, uniqueness
from initialization and unique restart from reached states. Retain the
canonical initialized Gaussian action and actual adjoint, full row w,
Hilbert–Schmidt learned increment K and readout c. Prove every additional
trajectory regularity assumption used. Ambient arbitrary-state uniqueness
is not required.

B: prove quantitative raw-state law continuity and uniform whole-circle
prediction continuity. Identify actual finite GF for each fixed Borel law
and every simultaneous empirical-law/width limit without a relative rate;
derive independent iid sampling. Keep same-carrier finite-program state
approximations, both action orientations, second moments and paired
initial/current hidden observables. No cross-carrier operator subtraction.

C: uniformly over all contaminating laws nu, prove an o(epsilon) prediction
remainder for `(1-epsilon)nu_*+epsilon nu`, with linear term exactly P1's
response. Bridge to actual finite nonlinear GF and actual finite right
derivatives in the order width first at fixed epsilon, then epsilon to zero.
Quadratic bounds, arbitrary joint epsilon/width rates and GD derivatives are
not required.

No training experiments, sweeps, global changed-law dynamics, universal
fitting, new architecture or promotion edits are authorized. A proof-route
failure does not refute this target. Completion needs a full frozen A–C
proof and two fresh complete isolated adversarial reviews, then the separate
promotion gates if applicable. The existing reviewed P1 proof is the
mathematical input, not its review verdicts.

## Current evidence and routes

All ten P1 manifest inputs verify; P1_SECTION is byte-identical to the
incorporated C.4.6. Current book/guide hashes differ from the pre-promotion
base precisely as recorded by the approved incorporation. Other frozen
scientific base hashes match. See the fresh run's startup_hashes.json.

| Route | Mechanism | Exact deliverable | Status |
|---|---|---|---|
| reached tails | actual finite column removal / weighted bounds | P2_REACHED_TAILS.md | frozen; exponential/cavity premise open |
| continuation | reference-tail completion / reached-state construction | P2_CONTINUATION.md | frozen conditional A–B theorem |
| variation | abstract variation along reachable curves | P2_VARIATION.md | frozen conditional remainder theorem; scoped independent check passed |
| mature combination | active tails, probe atoms, radial saturation | P2_COMBINED_TAIL_CONTRACT.md | conditional H implies A–C; full conditional audit passed |
| bounded-feature alternative | correlated-row stability and coordinates | P2_TAIL_ALTERNATIVE.md | frozen exact route obstructions; no neural refutation |
| source bootstrap | named-response coefficient comparison | P2_SOURCE_BOOTSTRAP.md | complete author H proof, frozen for full review |
| independent kernel check | conditional weighted coefficient inequality | P2_KERNEL_CHECK.md | frozen separate derivation confirms the conditional inequality |
| coordinator | dependency audit and finite comparison | P2_REPORT.md, P2_RUN_RECORD.md | full exact gap and evidence preserved |

The new source proof claims H, the averaged backward tail estimate for all
fine raw Euler programs on one positive law neighborhood through40. It
uses fresh-query coefficient extraction and two causal bootstraps;
propagation or fixed reference proximity alone remain insufficient.
P2_THEOREM.md and P2_MANIFEST.json freeze the complete A–C candidate.
Its correctness must now survive the two fresh complete isolated reviews.
