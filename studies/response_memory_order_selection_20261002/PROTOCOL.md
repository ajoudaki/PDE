# First decision: persistent order selection beyond ordinary rivals

Frozen before outcomes on 2026-10-02. This protocol supersedes the screening memo's weak one-epoch contrast and correlated signal coordinates. No response-memory computation is authorized by a mere order effect.

## Model and data

Use precisely the paper's bias-free two-hidden-layer tanh network, squared mean loss, Gaussian first weights N(0,1), hidden weights N(0,1/n), zero stored readout, and block mobilities (n,1,n). Raw simultaneous SGD has batch size 64 and fixed step eta=0.01; do not substitute a flow or adaptive optimizer. Wide reference n=512; ordinary cheaper nonlinear rival n=64. Manual derivatives will be checked against automatic differentiation and directional finite differences before scientific execution.

There are m=1280 examples, d=16 inputs. Independent standard Gaussian z1,z2,z3 give y=tanh(z1 z2 z3). Their independence eliminates the target's linear Hermite component. Input coordinate 4 is s=e*y+0.1*epsilon, epsilon independent standard Gaussian; remaining 12 are independent standard Gaussians. Exactly1152 examples have e=+1 and128 have e=-1. Every source count is divisible by64; batches have equal size. The nonlinear signal competes with a directly accessible shortcut. Data and model seeds are101,102,103,104,105, with deterministic separately tagged RNG streams.

Primary OOD test has8192 fresh examples, the same invariant signal and nuisance distributions, and s=y'+0.1*epsilon for an independent y' from the same label distribution. This preserves the shortcut marginal while breaking label association. A zero-shortcut probe is separate and never called OOD risk. A second independent shortcut draw defines S=E[(f(x)-f(x with s replaced))^2]. V_y=E[y^2] normalizes risks and dependence. Fixed balanced calibration examples,1024 total, are reserved for conditional final-feature readout refitting and never enter training, ordering choice or checkpoints.

## Fixed substantial intervention

Train one common mixed prefix of128 epochs. A mixed epoch uses18 majority batches and2 minority batches, placing one minority batch after each9 majority batches. Permutations are fixed by seed.

Validity gate at this fixed switching point: wide training predictions and updates finite, no single parameter RMS above100; hidden activation change RMS from initialization at least0.05 in one layer; shortcut dependence S/V_y at least0.1; zero-shortcut risk below0.95 V_y. The last two require actual competition between shortcut use and useful invariant prediction. Failure is an inconclusive witness and stops this study's computation; no data/activation/rate search.

The intervention presents each training example exactly64 times. AB contains all1152 majority minibatches followed by all128 minority minibatches. BA reverses these two complete blocks, preserving within-block minibatch sequence. This is64 epochs or physical step time12.8. Both then receive exactly the same256-epoch mixed continuation. The prefix, intervention duration and continuation are never selected from outcomes.

## Forecasts and strongest affordable ordinary controls

Before executing either wide target branch, run the n=64 ordinary nonlinear network through its own canonical prefix and the same two schedules. Its signed OOD risk contrast is an ordinary low-cost forecast, with no future wide-branch access.

Also compute a wide first-order schedule-response forecast about a common mixed reference continuation from the wide switching state. For reference batch field F_ref and target batch field F_target, evolve v_+=v+eta*DF_ref(theta)[v]+eta*(F_target(theta)-F_ref(theta)), v=0 at switching, alongside theta_+=theta+eta*F_ref(theta). After the intervention the forcing is zero and both tangents continue under the exact Jacobian of the same mixed updates. Forward and backward directional derivatives are analytic. Forecast output is f(theta)+Df(theta)[v], not a new trained branch. Save this forecast before running wide AB or BA. This gives ordinary moving nonlinear reference dynamics their best inexpensive local response, rather than comparing only to an initialization-frozen kernel.

## Decisions, validity and budget

Primary outcome is signed difference (BA minus AB) in OOD squared risk after the full common continuation, normalized by V_y. A consequential effect requires absolute contrast at least0.05. Compare also at the first training-MSE0.001 crossing during common continuation; both crossings must exist. A secondary common-loss comparison uses the lowest loss attained by both branches within the cap, with an explicit interpolation diagnostic. No crossing means the fitted-selection claim is untested, even if finite-time risk differs.

An ordinary rival captures the contrast if it predicts the correct sign and its error is at most25% of the wide contrast or0.02 V_y, whichever is larger. If either rival does so, stop: no q/proof campaign. If the wide effect is below0.05 after continuation, stop. A strong first-seed effect with neither rival successful is reported to root immediately before further design or interpretation. This author may only replicate that exact contrast on four additional seeds; meaningful replication requires same sign in at least4/5 and median absolute normalized contrast at least0.05.

Only if the consequential contrast survives, refit each final hidden representation's readout by ridge regression on the same balanced calibration set, with normalized objective MSE+0.001*||beta||^2 and features h/sqrt(n). Evaluate the same OOD test. If this reduces the gap below0.02 V_y, downgrade from useful representation selection to readout selection. This is the cheaper mechanistic rival suggested by deep-feature-reweighting work; it is not optional evidence for a representation claim.

Pre-outcome amendment: if the wide persistent contrast passes and neither narrow nor first-order rivals capture it, a conditional ordinary nonlinear rival freezes only the initialized middle matrix while training the first layer and readout with their canonical mobilities, from the same initialization, through the same prefix and both schedules. This preserves nonlinear feature learning while removing learned middle-matrix interactions. If it captures the contrast under the same criterion, no essential paired-hidden-memory claim follows. Execute only within the original budget and after reporting the first contrast to root.

Raw SGD is the target, so no eta-refinement convergence claim. Float32, disabled TF32, recorded environment. Save every epoch's train/test risks, shortcut dependence, zero-shortcut risk and feature motion; save update norms and finite checks, endpoint predictions and model checkpoints. Derivative checks require relative error below1e-5 in float64 against autograd and below1e-4 for centered finite differences. Every run retains actual numerical failures. Repeat endpoint metric calculation in float64 if any scientific difference is near a threshold.

GPU0 only; at most20 cumulative GPU-process minutes and30 wall minutes including implementation. Scientific first seed has a600-second process cap; total producer tracks a1200-second process cap. No new packages, shared changes or Git mutations. All source remains in this study; products under data/generated/response_memory_order_selection_20261002/. No invented conditional extension, parameter grid, q forecast or proof campaign follows a failed gate.
