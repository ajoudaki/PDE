# Recurrent pilot: compression worked, distinct mechanism did not emerge

2026-10-02. This result supersedes the open pilot recommendation in
[RECURRENCE_CANDIDATE.md](RECURRENCE_CANDIDATE.md). **Stop this experimental
branch.** A generic online SVD update of the same rank reproduced the dense
trained recurrent response much more accurately than the paired-memory model.
The run supplies no reason to invest in a specialized accelerated solver for
this candidate. It does not refute the response-memory method in general.

## What was actually learned

The frozen nonlinear diffusion-inference task used eight complete forcing and
solution fields on a 16-by-16 grid, with 32 held-out fields. Dense, memory
order \(q=4\), and online rank-32 SVD updates began with bitwise-identical
weights and predictions. The learned variable was the entire \(256\times256\)
recurrent matrix. Every model used its own current equilibria and exact
implicit credit. No dense histories were supplied to either reduced learner.

The task did elicit learned, nonlinear recurrent response. Dense training
through physical time \(T=40\) reduced training MSE from 0.013480 to 0.0007366
(94.5%) and held-out MSE from 0.015333 to 0.003571 (76.7%). Feature RMS movement
was 0.1071. The largest training-state norm of the inverse residual Jacobian
\(K_a^{-1}=(I-D_aW)^{-1}\) rose from 2.47 to 7.40, almost threefold. At the
terminal state, 22.5% of training gate coordinates satisfied \(1-D_{a,ii}>0.05\).
This documents nonlinearity; it is not a claim that a linear surrogate was
experimentally excluded.

The teacher increment was numerically full rank (256 at relative singular
threshold \(10^{-10}\)), with effective rank 152 for 99% squared singular
energy. It was not planted low rank. Nevertheless the **learned dense
increment** had effective rank only five at \(T=40\), compared with both
reduced methods' rank budget 32. The low-data solution selected by dense
training was therefore unusually easy for generic low-rank tracking.

## The discriminator

Numbers below are maximum errors over the positive common-time checkpoints
\(t=5,10,20,40\), relative to the matched dense Heun trajectory. Prediction
error is held-out RMS discrepancy divided by held-out target RMS. Adjoint
error is the concatenated own-state \(\lambda_a=K_a^{-\top}(h_a-y_a)\)
discrepancy divided by the dense adjoint norm.

| Method | Moving model coordinates | Prediction error | Adjoint error | Timed trajectory |
|---|---:|---:|---:|---:|
| Dense | 65,536 | reference | reference | 16.55 s |
| Paired memory, \(q=4\), rank at most 32 | 16,385 | \(2.732\times10^{-3}\) | \(3.065\times10^{-2}\) | 16.55 s |
| Online SVD, rank 32 | 16,384 factor entries | \(3.714\times10^{-9}\) | \(1.794\times10^{-9}\) | 17.31 s |

The SVD control uses current low-rank factors plus the two rank-eight gradient
terms of a Heun update, then thin QR and a small SVD to truncate. It does not
read the dense reference or obtain a post-hoc optimal factorization. All
gradients and equilibria come from its own model. Its agreement is at the
same discretization, not a theorem about continuous gradient flow.

The small timing difference is not a meaningful speed claim: this prototype
materializes \(W\) and batched \(K_a\), solves adjoints directly, evaluates
held-out fields, and computes SVD diagnostics. All arms retain the same fixed
\(W_0\); raw model coordinates exclude common equilibrium and temporary solve
workspace. Peak allocated device storage across these runs was 36,328,960
bytes. An optimized matrix-free comparison would have different accounting.

The memory result is good dense-trajectory tracking at one quarter of the
moving learned state. But generic same-rank tracking preserves the response
much better. The experiment therefore fails to distinguish a useful special
role for paired temporal organization in this recurrent setting. The
precommitted strongest alternative survived, so the supervisor's stop rule
was applied before additional seeds or solver engineering.

## Validity and failure accounting

Float64 Heun used step 0.25. Every saved equilibrium had relative residual
below \(9.1\times10^{-12}\), and every saved adjoint solve had relative
residual below \(1.1\times10^{-15}\). Independent checks gave:

| Check | Relative error |
|---|---:|
| Implicit gradient versus central finite difference | \(4.14\times10^{-10}\) |
| Implicit gradient versus unrolled autograd | \(7.39\times10^{-12}\) |
| Moment-induced weight velocity versus product-defect formula, autograd JVP | \(2.56\times10^{-16}\) |
| Initial zero-memory reconstruction | exactly zero |
| Trained-state Schur adjoint versus direct solve | \(5.30\times10^{-16}\) |
| Trained-state Schur adjoint residual | \(9.17\times10^{-16}\) |

The Schur check verifies the algebra on a trained memory state. Its existence
is not novel and it supplies no solver-speed evidence.

The first memory attempt failed **before any training update** because the
Legendre integer-index tensor was passed to a CUDA contraction expecting
floating-point values. The original source and metadata were preserved as
runner_initial.py and initial_metadata.json; explicitly casting the two index
tensors to float64 fixed it. The dense formulas were unchanged. The successful
memory source is preserved as runner_memory.py. Later code additions supplied
the SVD control and validation oracles without changing either dense or memory
updates. Source hashes are in each process metadata file.

Three trained trajectories completed, plus the zero-update failed attempt.
Total measured GPU-process time was 54.73 seconds on physical GPU 1, far below
the authorized 25 minutes. No additional training, refinement, or seed was
run. The result is a **one-seed headroom decision**. No temporal convergence
rate, across-seed conclusion, or best possible low-rank algorithm is claimed.
Step refinement was not needed to decide the precommitted headroom test:
SVD already matches the chosen dense discrete reference by many orders of
magnitude more closely, while memory already met its broad fidelity gate.

## Research consequence

Retain the exact equilibrium-gradient outer-product identity, the autonomous
moment construction, and the conditional joint-clock regular-branch theorem
in the frozen candidate. That theorem was not numerically tested here:
the pilot used the simpler residual-speed clock with a zero backward prefix.
It still requires fresh independent mathematical review.

Downgrade the practical mechanism claim: this nonlinear, learned-response
pilot gives **no evidence that paired histories outperform generic dynamic
low-rank compression**, and no end-to-end solver gain has been established.
A different task chosen because this one failed would be exploratory and
requires a new preregistration; none was tried.

Artifacts:

- [Runner](recurrence_pilot.py) and [read-only summarizer](recurrence_summarize.py).
- [Raw generated directory](../../data/generated/response_memory_frontiers_20261002/recurrence_seed4101/).
- [Consolidated summary](../../data/generated/response_memory_frontiers_20261002/recurrence_seed4101/summary.json).
- [Preserved initial attempt](../../data/generated/response_memory_frontiers_20261002/recurrence_seed4101/initial_metadata.json),
  [successful memory process](../../data/generated/response_memory_frontiers_20261002/recurrence_seed4101/memory_metadata.json),
  and [SVD process](../../data/generated/response_memory_frontiers_20261002/recurrence_seed4101/metadata_svd32.json).
