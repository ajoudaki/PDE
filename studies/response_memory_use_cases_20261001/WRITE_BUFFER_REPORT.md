# Response-memory consolidation as a buffer for dense updates

The tested construction supports a concrete, bounded use: carry approximately canonical feature learning between infrequent writes to the hidden base matrix, then consolidate and continue on a new small training support. On five fresh seeds with eight successive supports, order-three response memory used eight consolidations and had mean whole-circle discrepancy **0.00108** from the dense reference, versus **0.2525** for matched delayed updates and **0.0475** for trained rank-24 factors. Every buffer fit every block to training RMS below 0.00085. Halved-step checks preserve the comparison; a width 512 check also passes.

This is evidence about preserving the dense learning trajectory under an infrequent-write constraint. It is **not** evidence of better classification, lower GPU memory, a GPU speedup or reduced energy. The buffer was approximately twice as slow as dense training in this eager PyTorch implementation. The dense base remains stored and is read in every forward/backward pass. These are internally checked empirical results, not promoted established material or a hardware benchmark.

## Construction and exact checks

Use two hidden tanh layers, width n, m=8 examples, first-layer matrix $W^{(1)}\in\mathbb R^{n\times2}$, hidden matrix $W^{(2)}\in\mathbb R^{n\times n}$, and readout $w\in\mathbb R^n$. The implementation receives normalized input rows $u=x/\sqrt2$. Its forward equations are

\[
h_a^{(1)}=\tanh(W^{(1)}u_a),\qquad
h_a^{(2)}=\tanh(\widehat W^{(2)}h_a^{(1)}),\qquad
f_a=w^\top h_a^{(2)}/n.
\]

For residual $r_a=f_a-y_a$ and unhalved loss $\mathcal L=m^{-1}\sum_a r_a^2$, let $\rho=\sqrt{\mathcal L}$. Backward responses exclude residuals; $\mathbf1$ denotes the all-ones vector:

\[
\delta_a^{(2)}=w\odot(\mathbf1-h_a^{(2)}\odot h_a^{(2)}),\qquad
\delta_a^{(1)}=(\mathbf1-h_a^{(1)}\odot h_a^{(1)})\odot(\widehat W^{(2)\top}\delta_a^{(2)}).
\]

The first layer and readout follow the canonical mobilities $n$, while the hidden matrix has mobility 1. Their velocities and the dense hidden velocity are

\[
\begin{aligned}
\dot W^{(1)}&=-\frac2m\sum_a r_a\delta_a^{(1)}u_a^\top, &
\dot w&=-\frac2m\sum_a r_a h_a^{(2)},\\
F_{W^{(2)}}&=-\frac{2}{nm}\sum_a r_a\delta_a^{(2)}h_a^{(1)\top}.
\end{aligned}
\]

Ordinary activity-clock memories use $\dot\tau=\rho$, $\tau(0)=1$, and $q$ raw Legendre moments of the forward and residual-weighted backward histories. For j=0,...,q-1,

\[
\begin{aligned}
\dot{\bar h}_{a,j}&=\rho h_a^{(1)}-\frac\rho\tau
 \left(j\bar h_{a,j}+\sum_{k<j}(2k+1)\bar h_{a,k}\right),\\
\dot{\bar\delta}_{a,j}&=r_a\delta_a^{(2)}-\frac\rho\tau
 \left(j\bar\delta_{a,j}+\sum_{k<j}(2k+1)\bar\delta_{a,k}\right),\\
\widehat W^{(2)}&=W_{\rm base}^{(2)}-\frac{2}{nm\tau}
 \sum_{a,j}(2j+1)\bar\delta_{a,j}\bar h_{a,j}^{\top}.
\end{aligned}
\]

Each $\bar h_{a,j}$ or $\bar\delta_{a,j}$ is an $n$-vector for a sample and mode; layer indices are suppressed because there is only one hidden-to-hidden link. Initially $\bar h_{a,0}=h_a^{(1)}$, while higher forward moments and every backward moment are zero. First-layer entries are N(0,1), hidden entries N(0,1/n), and readout is explicitly zero before the first step. There are no biases or normalization. This adapts the study's unchanged baseline `Flow`, with hidden gain 1, rather than introducing a different network or prefix.

A consolidation sets $W_{\rm base}^{(2)}$ to the current reconstructed matrix, then resets $\tau$ to 1 and the moments to the current-forward/zero-backward prefix. Hence the represented matrix, and thus the function on **every** input, is unchanged at that instant. Future dynamics change because the stored history was reset. At a support change, the new prefix uses the current first-layer features of the new inputs. This algorithm is outside the paper's uninterrupted all-time regime and is not native streaming over arbitrary new samples.

For endpoint projections

\[
h_a^*=\tau^{-1}\sum_j(2j+1)\bar h_{a,j},\qquad
b_a^*=\tau^{-1}\sum_j(2j+1)\bar\delta_{a,j},
\]

differentiating the reconstruction and substituting the moment equations gives the exact continuous hidden-velocity defect

\[
\dot{\widehat W}^{(2)}=F_{W^{(2)}}+E,\qquad
E=\frac{2}{nm}\sum_a(r_a\delta_a^{(2)}-\rho b_a^*)
 (h_a^{(1)}-h_a^*)^\top.
\]

No division by $\rho$ is needed. Write $U,V\in\mathbb R^{n\times m}$ for the matrices with these backward- and forward-error columns. Then $\|E\|_F^2=(2/(nm))^2\sum_{a,b}(U^\top U)_{ab}(V^\top V)_{ab}$, which uses small $m\times m$ Gram matrices rather than forming $E$. Vector norms are Euclidean and $\|\cdot\|_F$ is the Frobenius norm. The triangle inequality and $\|uv^\top\|_F=\|u\|\|v\|$ give

\[
\|E\|_F\le\frac{2}{nm}\sum_a
 \|r_a\delta_a^{(2)}-\rho b_a^*\|\,
 \|h_a^{(1)}-h_a^*\|.
\]

The scalar bound is cheap once the current responses are available. Computing those responses still requires a forward/backward pass. A sampled physical-time sum of the bound is a heuristic local flush signal, not a certified integral or a global output-error bound.

Float64 algebra checks at n=17, m=5, q=1/3 passed: forward application and true transpose agree with explicit materialization within 1.4e-15; consolidation query changes are below 7e-18; the defect identity agrees with differentiated reconstruction to relative 4e-16 and with centered finite differences to relative 1.2e-8. The computed defect norm is below its scalar upper bound. These checks are in `write_buffer_diagnostics/` under the generated-data root. Code variables `.w`, `.c`, `.s`, `A` and `B` correspond to $W^{(1)}$, $w$, $\tau-1$, $\bar\delta$ and $\bar h$, respectively.

## Protocol and controls

The full pre-execution protocol and its dated decision amendments are in [WRITE_BUFFER_PROTOCOL.md](WRITE_BUFFER_PROTOCOL.md). Static pilots used seeds 101..103, n=256, unit labels sign(cos(3 theta)), and angles $\theta_a=2\pi(a+0.13)/8$ for $a=0,\ldots,7$. Orders 1/3 unflushed closures, fixed flush intervals 8/32, an order 1 defect controller, two delayed-update multipliers and two factor initializations were retained. No failed run was discarded.

The static screen revealed that fitting largely finished before the first 32-time-unit flush, so it exercised little useful consolidation. At the supervisor's request, the decisive test instead used eight prescribed 32-time-unit support blocks, adding pi/16 to every support angle at each boundary and recomputing labels from the same target function. There are seven support changes and a final consolidation. This strengthens the original practical question; the static results are pilots, not independent confirmations.

The buffer, dense reference, delayed control and factor control share initial physical weights, support schedules, 4,096 accepted midpoint steps, and horizon 256. The selected order is q=3. The delayed control freezes only the hidden matrix between writes; its first layer and readout continue training. It records **every midpoint forward/backward gradient factor**, without compression, and adds their accumulated outer-product update at exactly the same eight boundaries. Thus it neither pays for an n×n accumulator every step nor loses gradient history. Its multiplier 0.25 was selected from {1, 0.25} using only static pilot performance. Direct factors use W_base+AB at rank 24, A(0)=0, Gaussian B, unit factor mobilities and canonical outer-layer mobilities; their stronger of two pilot initializations was frozen. Pilot calibration may use the dense reference; control dynamics receive no dense trajectory.

After three repeated-support pilots passed, confirmation used fresh seeds 201..205. The primary metric averages RMS query-grid difference from dense at t=16,32,...,256 on 513 uniformly spaced angles, exposing both mid-block and end-block behavior. Pass criteria were a factor-two advantage over matched delay, error<=0.1, final training RMS<=0.1, at least 10-fold fewer accepted-step dense updates, and success on at least 4/5 confirmation seeds. Step refinement to 1/32 on 201/202 and a width 512 check on 201 were precommitted follow-ups. The construction passes all these tests.

## Fresh confirmation results

Means over five fresh seeds at width 256 and step 1/16:

| Method | Primary grid discrepancy | Mid-block discrepancy | End-block discrepancy | Dense base consolidations | Wall time per fit |
|---|---:|---:|---:|---:|---:|
| Dense reference |0|0|0|4,096 accepted updates|3.63 s|
| Response-memory buffer q=3 |0.001081|0.001077|0.001084|8|7.16 s|
| Matched delayed updates |0.2525|0.1737|0.3313|8|3.25 s|
| Trained rank-24 factors |0.04753|0.04984|0.04523|0|4.89 s|

The buffer's primary discrepancy ranges 0.001007–0.001145 across the five seeds. Its largest block-end training RMS is 0.000850; the delayed control's per-seed maximum block-end RMS ranges 0.645–0.773. Thus an easy final block is not hiding unsuccessful earlier buffer adaptation. Direct factors also fit the block endpoints well, while selecting a different function between training points.

Final target classification accuracy averages 92.87% for dense, 92.83% for the buffer, 91.93% for delay and 92.71% for factors. These differences do not establish a predictive advantage. In the original static screen, factors actually had higher target accuracy than dense despite their larger dense-function discrepancy.

The confirmation figure displays all recorded 8-time-unit observations, not only the primary 16-time-unit subset:

![Repeated adaptation confirmation](../../data/generated/response_memory_use_cases_20261001/write_buffer_analysis/repeated_confirmation.png)

### Numerical scope

The saved `feature_rms` diagnostic compares hidden features on the current, rotated support with `initial_h` evaluated on the original support. In repeated-support runs it therefore mixes learned feature changes with changes caused by the inputs themselves, and must not be used as evidence of feature learning. The static-support feature-change measurements retain their intended interpretation because their inputs are fixed. This diagnostic limitation does not affect predictions, losses, trajectory discrepancies, consolidation counts or resource measurements; the frozen runs are unchanged.

At step 1/32, buffer primary discrepancies are 0.000824 and 0.000941 for seeds 201/202; delayed discrepancies remain 0.2661 and 0.2464. The maximum coarse/fine query RMS change of any compared method is 0.00226, below the 0.01 gate. Individual dense/buffer trajectory changes can be of the same order as the approximately 0.001 discrepancy. Consequently those decimal values describe finite-step runs, not a high-precision measurement of continuous-flow error; the large buffer-versus-delay separation and the 0.1 decision threshold are well resolved.

At width 512, seed 201, the buffer's primary discrepancy is 0.001020, delay 0.2600 and direct factors 0.06324; buffer final training RMS is 1.91e-7. This is one width check, not a scaling study.

## What the resource comparison actually says

At n=256 the buffer updates 13,057 state coordinates every integration substep: 512 first-layer weights, 256 readout entries, 12,288 moment entries and one clock. It additionally retains 65,536 base-matrix entries, which change at eight consolidations. Dense has 66,304 parameter coordinates. Factors have 13,056 frequently updated coordinates plus the same 65,536 base entries. The delayed baseline has 768 frequently updated outer coordinates and a 2,097,152-scalar uncompressed history buffer at this step and write interval.

The base matrix is fixed **within** an interval, not throughout the whole experiment. Accordingly the consolidated algorithm does not have a formally subquadratic total autonomous state or lower total persistent storage. The base matrix is still read at every step.

There are 4,096 accepted dense optimizer steps versus 8 consolidations, a 512-fold reduction in the frequency of persistent hidden-matrix updates. The explicit midpoint implementation physically overwrites its hidden parameter array twice per accepted step: 8,192 such stage writes at step 1/16, and 16,384 at the refined step 1/32. These counts concern parameter-array mutations, not total device writes. Backups, matrix-product temporaries, reads, first-layer/readout updates and intermediate work are additional.

For the coarse runs, the eight buffer materializations contract rank 24 factors, for 25,165,824 multiply-add-counted-as-two FLOPs. The matched delayed contractions total 4,294,967,296 FLOPs because each retains 512 midpoint samples times 8 examples per interval. These are arithmetic counts for materialization only, excluding the shared dense base actions and all other work. Mean measured materialization time was 0.00292 s for the buffer and 0.00121 s for delay; the large arithmetic-count difference therefore does **not** translate into a measured materialization speedup in this tiny test. Mean whole-fit timings likewise favor dense and delay over the buffer.

Measured peak allocated CUDA memory was 10,648,576 bytes for dense, 11,602,944 for the buffer, 25,861,632 for delay and 11,535,360 for factors. These are PyTorch allocation peaks for these runs, including activation and temporary work, not a deployment memory model. No power or device-energy measurements were taken.

The static order 1 defect controller is a useful secondary result: it made 7 writes per seed and reduced mean discrepancy from 0.01785 unflushed to 0.002215, compared with 0.04283 for its stronger matched delayed control. It checks the exact norm and scalar bound every eight accepted steps (512 diagnostic calls per run); the total measured diagnostic time averages 0.375 s within a 5.58 s fit. The trigger threshold is $0.002\sqrt n$ on the sampled accumulated norm bound. Seed 101 flushes at times 2.5, 4, 5.5, 7, 8.5, 10.5 and 14.5. This remains a three-seed pilot with sampled diagnostics and is not part of the fresh repeated-support confirmation.

## Evidence status and surviving limitations

- **Exact and checked:** reconstruction/transpose consistency; function-continuous consolidation; the continuous product-form velocity defect and its scalar norm bound.
- **Empirically supported here:** repeated consolidation can preserve a canonical dense trajectory while reducing the frequency of hidden base updates, on this small-support tanh task and prescribed support schedule.
- **Disfavored in this test:** full delayed-gradient accumulation alone, at the same write times and tested pilot-calibrated multiplier, is sufficient to preserve the selected dense function equally well. Ordinary rank-matched factor training is also less faithful here.
- **Not established:** GPU acceleration, lower device energy, lower total memory, predictive superiority, optimality among low-rank optimizers, new-input streaming without resetting sample-indexed memory, large-data performance, arbitrary support changes, or a theorem covering repeated consolidation.

The strongest surviving alternative is a different carefully optimized low-rank or delayed-update method. Only the explicitly stated control families were tested. The geometry is also highly structured: eight points on a circle, repeated hundreds of times per block. This is a mechanism-preserving demonstration of a candidate write-limited training algorithm, not validation on realistic continual-learning workloads or specialized memory hardware.

## Reproduction and retained artifacts

All route products are under `data/generated/response_memory_use_cases_20261001/write_buffer_*`. Each fit has `config.json`, `summary.json`, `predictions.npz` and `defects.json`; repeated-adaptation fits additionally retain their exact `source.py` and training predictions/labels. Configurations contain source/baseline hashes, seed, device, dtype, environment and every experimental argument. All 87 scientific fits completed; no scientific fit was excluded. There are also two retained CPU smoke checks. Summed measured training-loop time is 430.06 s, approximately 7.17 GPU-minutes, well below the initial 20-minute runtime ceiling; the amended 100-fit ceiling was needed for the 87 fits.

- [Adapted implementation](write_buffer_experiment.py), [campaign driver](write_buffer_campaign.py), [aggregation/figure script](write_buffer_summarize.py).
- [Frozen original static implementation](write_buffer_experiment_static_v1.py), with SHA256 `2c82217c8f12c178a9e0093ada421fff3cbe83612096f31fcc421339a36e01b9`; later maintenance only resized the delayed allocation and added explicit repeated supports and provenance outputs.
- [Aggregate metrics](../../data/generated/response_memory_use_cases_20261001/write_buffer_analysis/aggregate.json), [confirmation figure PDF](../../data/generated/response_memory_use_cases_20261001/write_buffer_analysis/repeated_confirmation.pdf), and generated `write_buffer_diagnostics/` for algebra checks and static tables.

Representative reproduction commands, replacing output directories by fresh paths:

```bash
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/write_buffer_experiment.py --check --out /tmp/write_buffer_checks.json
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/write_buffer_campaign.py --phase switch --seeds 201,202,203,204,205 --selected fixed3_32 --selected-multiplier .25 --factor-seed 7319 --out FRESH_CONFIRMATION
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/write_buffer_campaign.py --phase refine --repeated --methods dense,fixed3_32,delay_selected --seeds 201,202 --selected fixed3_32 --selected-multiplier .25 --factor-seed 7319 --out FRESH_REFINEMENT
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/write_buffer_campaign.py --phase width --repeated --seeds 201 --selected fixed3_32 --selected-multiplier .25 --factor-seed 7319 --out FRESH_WIDTH_CHECK
/home/amir/miniconda3/bin/python studies/response_memory_use_cases_20261001/write_buffer_summarize.py
```

GPU execution used an escalated Python invocation because the ordinary sandbox hides the device nodes. TF32 was disabled and CPU threads fixed to one. Source verification checked all 42 retained repeated-adaptation source snapshots against their recorded hashes and confirmed the baseline copy is unchanged. No manuscript, maintained code, other route, shared README or Git index was changed by this agent.
