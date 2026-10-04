# Shared response bases beyond sample-indexed history memory

New investigation, 2026-09-29. Owner: current root task.

## Question and contract

Can an autonomous, restartable compression of canonical nonlinear deep-network training replace the O(Lmnq) sample-indexed response moments by a shared evolving state whose size has no explicit dependence on the number m of training samples? Fixed initialized matrices remain exact. The target is the original empirical gradient flow (or an explicitly quantified time discretization), not ordinary low-rank factor training or a snapshot-only representation. Training data may remain available as static input; full-batch computation can still depend on m.

We will separate finite-width finite-horizon tracking, sample-uniform constants under uniformly bounded data, width-uniform results, and all-time results. No latter scope is inferred from the former. No prescribed favorable spectrum, unseen reference trajectory, or unproved statistical independence is admissible as an unconditional input.

## Scope and inputs

User-authorized new theoretical investigation. Inputs: current paper/main.tex explicitly referenced by the user; maintained docs/ notation and relevant theory; external primary sources. No other studies are inputs. No changes to paper/, maintained docs/, or maintained code/ are planned. No training campaign is authorized or needed initially.

## Results and evidence

The main report is [RESULT.md](RESULT.md), with the complete canonical algorithm and proofs in [CAUSAL_ROUTE.md](CAUSAL_ROUTE.md).

1. A shared, moving singular basis can replace sample-indexed memory. For arbitrary adaptive signed rank-one atoms, the retained rank-R matrix has accumulated operator defect at most V/(R+1) and Frobenius defect at most V/sqrt(R+1), where V is the sum of incoming nuclear norms. The nuclear potential pays for all discarded directions together.
2. Feeding this sketch with the canonical gradients of its own reconstructed network yields a restartable discrete scheme with O(LnR) evolving hidden state. At fixed width/depth and every finite horizon it tracks dense gradient flow with prediction error C_{T,n}(1/(R+1)+eta), uniformly in sample count for fixed input and label-RMS bounds.
3. For globally bounded activations and first derivatives, with locally Lipschitz first derivative (including tanh), the tracking theorem holds for every rank and step size. No small-label, fitting, or data-Gram assumption is used. Large errors remain possible. General locally C^{1,1} activations have a sufficient-rank/small-step version proved by first exit.
4. Norm optimization has a precise meaning: normalized paired-atom l1 cost is nuclear norm, l0 is rank, and orthogonal coefficient l2 energy is invariant. The streaming update is a nuclear-norm proximal step with threshold determined by the storage cap.
5. The norm-only operator rate 1/R cannot be improved uniformly over a nuclear ball. Separate exact polynomial-activation input-moment and expensive coreset alternatives are retained in [FUNCTIONAL_ROUTE.md](FUNCTIONAL_ROUTE.md). Their conditional/degree costs remain separate from the spectral construction.

**Status:** internally checked for the precise finite-width, finite-horizon, sample-uniform discrete theorem; not promoted to the paper or book. [CHECK.md](CHECK.md) records complete within-study argument/code inspection, exact hashes, acceptance scope, and a fresh deterministic rerun. Root checked the canonical equations against the current paper and maintained notation, read all route reports, and checked the noncircular bounded-gate argument. No full neural training implementation or benchmark is claimed.

**Important gaps:** a width-uniform nonlinear feedback constant; all-time tracking; a unique smooth continuous-time compressed ODE at fixed rank; useful subdense ranks for every task; and priority for the full neural application. Full data access and fixed dense initialization remain. Runtime still depends on m. The source budget itself and forward prediction Lipschitz bound can be width uniform under bounded normalized initialization, but that does not remove width from feedback.

The matrix-sketching precedent is Mroueh, Marcheret and Goel, AISTATS 2017, *Co-Occurring Directions Sketching for Approximate Matrix Multiply*, Algorithm 2/Theorem 2. Its full nine-page primary text was inspected. The mechanism is not claimed as a new invention. See RESULT.md for the primary link and the exact novelty boundary.

## Contributors and independent routes

- Root: current paper/book setup, nuclear/proximal interpretation, bounded-gate strengthening, synthesis, and `spectral_memory.py`.
- `shared_basis_causal`: initially independent PSD-lift route; direct shrinkage cross-check after root supplied it; complete canonical nonlinear tracking proof in `CAUSAL_ROUTE.md`.
- `shared_basis_limits`: independent direct shrinkage discovery, sharp norm-rate limits and generic trajectory proof in `LIMITS_ROUTE.md`.
- `shared_basis_functional`: independent functional, polynomial-moment and coreset route; after candidates froze, complete within-study cross-check in `CHECK.md`.

Initial agents had prompt-only scientific scope with no inherited discussion. Cross-pollination occurred only after concrete candidates existed. The final cross-check was within-study, not a fresh independent promotion review. One polynomial-route correction was made: the residual-RMS clock also requires the scalar empirical moment E[y^2].

## Reproduction

Algebra-only implementation check, not a training experiment:

```sh
OPENBLAS_NUM_THREADS=1 python -B studies/shared_response_basis_20260929/spectral_memory.py --out data/generated/shared_response_basis_20260929/algebra_001
```

Use a fresh output directory for each run. Original `algebra_001` and reviewer `algebra_functional_crosscheck_001` both passed under NumPy 1.26.4, exit code 0. Each checked 480 adaptive prefixes against dense SVD/accumulator oracles, plus sharp diagonal and repeated-discard examples. Maximum dense-SVD discrepancy: 2.7006733775686547e-14. The source hash and exact result locations are retained in CHECK.md. Working source HEAD was 7fce699; the current paper source SHA-256 was fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605. The main paper was not edited. Other tasks' inherited changes were preserved, and nothing was staged or committed.

## Next action

Current theoretical request is answered by the completed report and proof. The strongest practical next check would be a small, matched canonical neural benchmark of the explicit spectral-memory integrator, including step refinement and moving-basis behavior. No training campaign has been launched or preauthorized by this note. A continuous-time fixed-rank law and width-uniform feedback require additional proofs.
