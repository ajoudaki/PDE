# Independent implementation check

Scope: internal implementation checking of this new study, not promotion or a
population-limit claim. The checker did not author the producer or train any
trajectory. Its independent derivation and numerical oracles precede outcome
inspection. The preflight and complete retained-array replay passed. This
verdict concerns implementation and saved-output consistency; the separate
analysis controls integration accuracy and the scientific comparison.

## Inputs and independence

The assigned scientific inputs were the experiment assignment, the complete
`docs/NOTATION.md`, `code/pde/finite_network.py`, `finite_torch.py`,
`closure_comparison.py`, `observable_torch_circle.py`, `observable_solver.py`,
and actual direct imports needed. The checker read those files completely,
including `observable_torch_p1.py`, the input/state dependency of
`finite_torch.py`. It then read the complete frozen `PROTOCOL.md`, producer
`flow_benchmark.py`, and supervisor `flow_runner.py` within this study. No other
study, historical research message, outcome, or code was an input. Shared
workflow instructions and the required rigorous-mathematics and research
skills were read as process instructions. A fresh prompt-only subagent checked
the calculus and target normalization, without repository scientific retrieval.

The maintained circle-specific frontends require unit-norm normalized inputs;
they therefore cannot directly implement this study's `||u||^2=1/2` convention.
The final producer uses its explicitly stated inputs without this substitution.
The actual canonical Gaussian readout is retained, including for the closure.

## Independent calculus

Write `N=126` for the sample count, with input rows `u_a`, residual
`r=f-y`, and the fixed dictionary matrices `B1,B2`. For any moving closure
state, its exact effective dense matrix is

\[
\widehat A=B_2MB_1^T/n,\quad
Z_1=WU^T,\quad H_1=\tanh Z_1,\quad
Z_2=\widehat A H_1,\quad H_2=\tanh Z_2,\quad f=H_2^Tc/n.
\]

Let `S_l=sech^2(Z_l)`. Differentiating the unhalved mean squared loss gives

\[
\begin{aligned}
D_2&=c\odot S_2,&D_1&=S_1\odot(\widehat A^TD_2),\\
G_W&=\frac{2}{Nn}(D_1\odot r)U,&
G_A&=\frac{2}{Nn}(D_2\odot r)H_1^T,\\
G_c&=\frac{2}{Nn}H_2r,&
G_M&=B_2^TG_AB_1/n.
\end{aligned}
\]

Here products by `c` and `r` broadcast over population rows and input columns,
respectively. The last identity follows from
`d Ahat=B2 (dM) B1.T/n` and the ordinary Frobenius inner product. The physical
velocities are `(-n G_W,-G_M,-n G_c)`. For a dense network, replace `Ahat` by
the actual matrix `A`, with middle velocity `-G_A`.

Consequently the continuous chain-rule identity is

\[
\dot{\mathcal L}
=-n\|G_W\|_F^2-\|G_M\|_F^2-n\|G_c\|_2^2
=-\|\dot W\|_F^2/n-\|\dot M\|_F^2-\|\dot c\|_2^2/n.
\]

This identity concerns the vector field; it is not a claim that arbitrary
finite numerical steps decrease loss. The accepted-step and refinement gates
are separate checks.

The primary NumPy oracle explicitly constructs `Ahat`, differentiates the
dense map, then projects `G_A` back to `G_M`. It does not use the producer's
fields or derivative implementation. A second implementation keeps the basis
sums unnormalized until its final contractions. It agrees with the dense
oracle in the preflight and permits inexpensive replay of every saved RHS.
Centered differences evaluate only an independently implemented scalar loss.

For either regularized Gram `F.T F/n + rho I = L L.T`, `B=F L^(-T)` satisfies

\[
B^TB/n=I-\rho L^{-1}L^{-T},\qquad \rho=1/4096.
\]

The checker tests this identity and does not assume exact orthonormality after
adding the ridge. Canonical source arrays, raw dictionaries, Cholesky factors,
normalized dictionaries, and `M0` are reproduced independently.

Discrete Fourier orthogonality on 126 equally spaced points eliminates every
cross term among modes 1,3,5 and gives mean square one-half to each constituent
sine/cosine. Thus the target mean square is
`(32/21)*(1/2)*(1+1/4+1/16)=1`. The three odd frequencies give
`y(theta+pi)=-y(theta)`, as do the bias-free predictors. The checker also
verifies the shifted 1024-point passive panel and input norm squared one-half.

## Executed deterministic preflight

Command, from `/home/amir/Codes/PDE`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /usr/bin/time -p /home/amir/miniconda3/bin/python -B studies/smooth_circle_canonical_flow_20260921/flow_check.py preflight --output data/generated/smooth_circle_canonical_flow_20260921/check_scratch/preflight_01
```

Result: **PASS, 456 gates**, exit status zero. External process wall time was
0.85 seconds; recorded internal time was 0.733425 seconds. The authoritative
per-gate evidence and input hashes are in
`data/generated/smooth_circle_canonical_flow_20260921/check_scratch/preflight_01/preflight.json`.
An earlier prompt-only synthetic calculus check took about 0.3 seconds of
process wall and did not integrate a trajectory.

The preflight includes all three canonical seeds for each model, source and
basis reconstruction, initial predictions/RHS, synthetic nonzero-readout
states for each model, blockwise aligned and random centered differences,
the directional dissipation identity, zero-residual velocity, odd predictions,
and first/second-layer saturation cases for each dense width. Saturation cases
use large synthetic readouts to make erroneous cancellation in
`1-tanh(z)^2` observable. No synthetic state is a training initialization.

Ordinary-state producer/oracle RHS disagreement was at most
`4.441e-16` absolute. Basis reconstruction was exact in this environment.
The largest best directional-difference absolute error, including the
dissipation check, was `1.072e-10`. Every comparison passed the frozen protocol
tolerances. The large-readout saturation cases also passed their relative and
absolute gates; their maximum absolute error alone is not comparable to the
ordinary-state statistic because the readout velocity scale is `1e8`.

Frozen hashes:

- Producer: `e3dfab2aad9e57f889cb5597288e59af61242a0b24ce25119d893bda906a60dd`.
- Protocol: `4216873a1246566c05fd9ce3815940801787c59df2a297faa9025a4c4ce02966`.
- Checker: `753aa6dc1ad44d4c58262a789a59419444bf626346e339253688fa46d981dc60`.

The complete source read found the requested bias-free model, mobilities,
canonical initialization, fixed dictionary, and stable derivative. The
producer uses DOP853 on the simultaneous raw-state RHS, restarts at each
required observation boundary, and saves accepted endpoints. Passive labels
do not enter the RHS; dictionary construction accesses no labels. The
supervisor's selected-pair criteria match the frozen tolerances and keeps
failed coarse comparisons. Its source-freeze and process-budget checks are
operational safeguards, not mathematical error bounds.

## Replay scope and limitations

The frozen checker provides `replay --campaign PATH --output FRESH_DIR` and
`audit --run PATH --output FRESH_DIR`. Replay reconstructs the canonical source,
dictionaries and data, verifies recorded file hashes, and recomputes every
retained training/passive prediction and loss, every saved RHS, dissipation,
and hidden RMS displacement at all checkpoints and the final state. It also
checks accepted-step time ordering and records maximum loss increase.

Replay `passed` concerns internal consistency of all retained arrays;
`completed` is separate. The independent aggregate analysis checks full-horizon
completion, the selected refinement pair, reproduction, Fourier errors, and
the precommitted architecture-comparison rule. A preflight PASS alone does
not establish integration accuracy, a fitting outcome, or a closure advantage.
The checker does not independently re-prove DOP853 or audit unrelated
maintained library functionality. This is an internal study check only.

The frozen replay parser was additionally exercised on a fresh producer export
with a ten-second wall allowance, all of which the producer reserves for export.
It therefore stopped at initialization: physical time zero, zero ODE RHS calls,
zero accepted steps, status `wall_censored`. Its 45 replay gates passed. This
was a no-training archive-format check, not a campaign attempt. Evidence is in
`check_scratch/export_zero_01/` and `check_scratch/audit_zero_01/audit.json` under
the study's generated-data namespace. External process wall time was 0.27 seconds.

## Complete campaign replay

The checker replayed `data/generated/smooth_circle_canonical_flow_20260921/run01`
using its frozen source, after verifying that producer, protocol, and checker
hashes still exactly matched the preflight. The current shared `AGENTS.md`
was reread; the scoped checking instructions and study boundary were unchanged.
The fresh command from `/home/amir/Codes/PDE` was:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 /usr/bin/time -p /home/amir/miniconda3/bin/python -B studies/smooth_circle_canonical_flow_20260921/flow_check.py replay --campaign data/generated/smooth_circle_canonical_flow_20260921/run01 --output data/generated/smooth_circle_canonical_flow_20260921/check_scratch/replay_01
```

Result: **PASS, 3661 replay gates, zero failed gates**, exit status zero.
All 21 distinct retained attempts were replayed: primary/fine for the three
models and three seeds, plus each model's seed-20260921 fine reproduction.
Their archives each contained the exact 19 prescribed checkpoints through
`T=1000`, for 399 checkpoints and 21 final states. Completion was checked from
the retained archives and individual result records; the supervisor's aggregate
success flag was not used as numerical evidence. Every archived output-file
hash checked by replay matched, as did the canonical source arrays, prescribed
data, dictionaries, and the producer/protocol/maintained-flow source hashes.

Across the 420 replayed checkpoint/final states:

| Recomputed quantity | Maximum absolute discrepancy | Frozen gate |
|---|---:|---:|
| Training prediction | `3.886e-15` | `1e-9` absolute |
| Passive prediction | `1.110e-15` | `1e-9` absolute |
| Packed physical RHS | `6.717e-16` | `2e-12` absolute + `2e-10` relative |
| Training loss | `4.441e-16` | `1e-10` absolute |
| Passive loss | `5.552e-17` | `1e-10` absolute |
| Physical dissipation | `2.221e-16` | `2e-12` absolute + `2e-10` relative |
| Hidden RMS displacement | `1.110e-16` | `1e-9` absolute |

Authoritative evidence is
`data/generated/smooth_circle_canonical_flow_20260921/check_scratch/replay_01/replay.json`;
its SHA-256 is
`93147de0a890f447d205746415dcae848f76ccd40788b4d8f81557c85c915dfa`.
The adjacent `summary.json` reports per-run coverage, gate counts, and the
maxima above. The original per-gate numerical errors and tolerances remain in
the full replay JSON.

External replay process wall time was **15.08 seconds**; internal recorded
wall time was 14.943259 seconds. This brings the supervisor's conservative
20-second prior checking allocation to 35.08 seconds before final aggregation
and figures, well within the separate 600-second allowance. No producer,
protocol, or checker source was modified for this replay, and no trajectory
was integrated by the checker.

The all-checkpoint replay verifies the saved numerical objects, not a global
ODE error bound. The independent aggregate analysis must still establish the
prescribed refinement and reproduction gates and calculate the target errors
before making a scientific comparison. Saturation diagnostics were inspected
in the producer source but are not independently recomputed by this replay.
The result carries no architecture-separation, asymptotic, or promotion claim.
