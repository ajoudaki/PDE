# Attention route: bounded algebra check, frozen before execution

Date: 2026-10-02. Scope: arithmetic validation only; no training, GPU, dataset search, or scientific performance claim.

Question: can the paired endpoint defect drive query/key balance away from the exact gradient-flow invariant, and can a head-space correction cancel that drift without changing the instantaneous logits? Does RoPE require the smaller plane-wise correction?

Setup: one head, head dimension 4, input width 16, six tokens; one NumPy RNG seed 20261002. Gaussian weights/features; exact softmax of standard scores divided by sqrt(4). A fixed random linear functional of the attention probabilities supplies a differentiable scalar loss. Analytically evaluate Q/K gradients. Construct paired-form defects from random forward/backward endpoint residual arrays. These arrays are not claimed to arise on a trained trajectory.

Checks: (1) dense standard-attention matrix balance derivative; (2) nonzero uncorrected defect-induced drift; (3) Sylvester-corrected balance derivative and zero correction to logit velocity; (4) RoPE plane-wise balance derivatives under the exact gradient; (5) plane-wise corrected balance derivative and zero correction to RoPE logit velocity; (6) show a generic full-matrix correction changes RoPE logit velocity; (7) verify the analytic change in future dense routing velocity after a loss-preserving finite gauge move by central differences, at steps 1e-3, 1e-4, 1e-5.

Pass: exact-identity relative residuals <1e-10, finite-difference relative discrepancy at 1e-5 <1e-6, and both nonzero controls >1e-6 in their natural Frobenius norm. Failure of an identity triggers correction of algebra, not a training run. Small nonzero controls make only that control inconclusive; do not resample.

Validity: float64; Gram sum condition number below 1e6. Single process, <30 CPU seconds, <256 MiB, one seed, one run. No extension branch. Save code hash, dimensions, metrics, and environment to the assigned generated directory. A pass establishes implementation consistency of the stated identities only. Novelty and practical usefulness remain untested.
