# Consequence screen: function-preserving restoration of adaptability

**Recommendation: one inexpensive gate only; do not yet call this a continual-learning contribution.** The consequential question is whether paired feature–credit histories permit a *label-blind change of learning state that restores useful adaptation after repeated distribution shifts, while preserving the complete currently learned function*. The strongest competing explanation is ordinary conditioning of factor coordinates. A win against an untouched closure is insufficient. This is an optimizer-state intervention in a proposed learner, not a discovery that dense gradient flow secretly depends on histories beyond its physical weights.

The motivation is forward adaptability, not retaining contradictory old labels. Loss of plasticity and forgetting are different problems; work on continual backpropagation already offers strong rejuvenation mechanisms by replacing underused units. An intervention that preserves the current function exactly could be useful if it obtains comparable adaptation without the initial disruption of parameter replacement. This is an opportunity, not a demonstrated advantage. [Dohare et al., Nature 2024](https://www.nature.com/articles/s41586-024-07711-7).

## Exact object and intervention

Use the prompt's two-hidden-layer tanh learner and squared loss \(\mathcal L=m^{-1}\sum_a r_a^2\), with first-layer weights \(A\in\mathbb R^{n\times d}\), middle matrix \(B\in\mathbb R^{n\times n}\), readout \(w\in\mathbb R^n\), and \(r_a=f(x_a)-y_a\). For order one, collect the stored vectors in \(H=[H_1,\ldots,H_m]\) and \(D=[D_1,\ldots,D_m]\). The reconstruction is

\[
B=W_0-\frac{2}{mn\tau}DH^\top,
\qquad \dot H_a=\rho h_a,\quad \dot D_a=r_a\delta_a,\quad \dot\tau=\rho.
\]

Here \(h_a=\tanh(Ax_a/\sqrt d)\), \(\delta_a=w\odot[1-\tanh^2(Bh_a)]\), and \(\rho=\sqrt{\mathcal L}\); the first layer and readout follow the supplied equations. The paper's initialization has \(w(0)=0\), \(D(0)=0\), \(H_a(0)=h_a(0)\), and \(\tau(0)=1\). **Only the finite-order learner is intervened on.**

At a distribution switch, form \(\bar H=H/\tau\) and the current feature matrix \(h=[h_1,\ldots,h_m]\). With no new labels, solve

\[
R_0=(\bar H^\top\bar H+\lambda I)^{-1}
       (\bar H^\top h+\lambda I),\qquad
\lambda=0.1\,\operatorname{tr}(\bar H^\top\bar H)/m.
\]

Clip the singular values of \(R_0\) to \([1/2,2]\), obtaining an invertible \(R\), and replace

\[
H\leftarrow HR,\qquad D\leftarrow DR^{-\top}.
\]

If the trace is zero, skip the intervention. Keep \(A,w,\tau,W_0\) unchanged. Because \(DR^{-\top}(HR)^\top=DH^\top\), this preserves \(B\), hence **every current prediction on every input**, exactly in real arithmetic. It tries to align the stored feature span with current features while preserving the learned feature–credit product. It cannot repair feature directions outside that span. Afterward the arrays are legal learner states but generally cease to be literal moments of the original trajectory; that change of interpretation must be explicit.

Why this is more specific than a reset: writing \(\bar h_a=H_a/\tau\) and \(\bar\delta_a=D_a/\tau\), direct differentiation gives

\[
\dot B_{\rm closure}-\dot B_{\rm dense}(A,B,w)
=-\frac{2}{mn}\sum_a
(r_a\delta_a-\rho\bar\delta_a)(\bar h_a-h_a)^\top.
\]

Feature staleness influences the update through its pairing with changing credit. This identity supplies a mechanistic diagnostic, **not the research result**. A coordinate surgery that helps only this artificial defect, with no useful adaptation advantage against ordinary optimizers, fails the consequence screen.

## Strongest rival and what would matter

The primary rival is the *same feature-alignment gauge applied to directly trained factors*. Write \(B=W_0+UV^\top\), initialize \(U=-2D/(mn\tau)\), \(V=H\), and apply \(V\leftarrow VR\), \(U\leftarrow UR^{-\top}\). Train factors by their actual chain-rule gradients, alongside the same \(A,w\) updates. Both learners have the same current function, rank, factor count and allowed feature information. Include ordinary factor balancing as a label-blind gauge, plus a scalar learning-rate control. This grants the generic-conditioning explanation its strongest relevant version.

Dense gradient flow from the identical physical \((A,B,w)\) is the reference: it has no optimizer state to reset. A momentum reset is therefore not a distinct intervention on this reference. A momentum/Adam learner would be a separate comparator, with its own legitimately accumulated state. No claim about superiority to those methods follows from the first gate.

Replay and orthogonal-gradient methods target retention as well as adaptation; old contradictory targets should not be replayed in this concept-drift test. No replay-free retention claim is allowed. If the proposed contribution later changes to task retention, memory-matched replay and stored-gradient subspace projection become mandatory. Feature transport is a particularly close rival: the proposed \(R\) is itself a transport within the stored span, rather than a new general solution to representation drift. Existing work explicitly compensates feature drift in continual learning. [Cotogni et al.](https://arxiv.org/abs/2211.12292). TTT/DeltaNet-style fast-weight updates are also conceptually close competitors, not evidence for novelty from outer-product memory alone; DeltaNet already studies selective associative-memory updates. [Yang et al.](https://arxiv.org/abs/2406.06484).

**A result that would matter:** across prespecified aged states, the intervention improves held-out post-switch adaptation by at least 25% over the strongest matched factor-gauge and learning-rate control, while preserving the initial function and avoiding a comparable loss of later plasticity. This would motivate a new optimizer-state capability, independently of dense-flow approximation. It would not establish a continual-learning solution, hierarchy convergence, or superiority on realistic streams. A gain only over the untreated closure is an implementation repair and should be screened out for this user's purpose.

## Executable-sized gate; no execution authorized here

**Testbed.** CPU float64; seeds 0, 1, 2; \(d=2,n=128,m=8,q=1\). Let \(x_a=\sqrt2(\cos\theta_a,\sin\theta_a)\), \(\theta_a=2\pi(a+0.37)/8\), and use 256 uniformly spaced held-out angles. Twelve warm-up blocks use labels \(y_a=\sin(3\theta_a+k\pi/2)\), block \(k=0,\ldots,11\), with duration 8 each. The probe block uses phase \(\pi/4\). These fixed inputs preserve the original sample-indexed state; this is concept drift, not an unsupported extension to an unbounded input stream. All methods receive identical data. No task identity enters the gauge.

**Arms from one identical checkpoint per seed.** (1) unchanged closure; (2) feature-aligned closure above; (3) closure with norm-balancing gauge \(H\leftarrow cH,D\leftarrow D/c\), \(c=\sqrt{\|D\|_F/\|H\|_F}\), clipped to \([1/2,2]\); (4) factor gradient descent; (5) feature-aligned factor gradient descent; (6) dense gradient flow. Include learning-rate multipliers \(1/4,1,4\), multiplying all state velocities, for arms 1 and 4–6 and compare against their best result, explicitly labeling that selection as an oracle-strength control, not a deployable tuned method. A positive result must beat even that advantage. For factor methods put \(G_B=\nabla_B\mathcal L\), use \(\dot U=-\eta G_BV\), \(\dot V=-\eta G_B^\top U\), and test both \(\eta=1\) and \(\eta=\|G_B\|_F/\|G_BVV^\top+UU^\top G_B\|_F\), evaluated at every solver stage. Set the latter to one when both numerator and denominator vanish and invalidate that arm when only its denominator vanishes. Keep the supplied first-layer/readout mobilities. Thus scalar factor speed receives an explicit, strong control.

**Metrics.** Primary: integral over the 8-unit probe block of held-out squared error, divided by the same integral for the untouched closure. Report paired raw integrals, training loss, the current-function jump at surgery, and the exact middle-layer velocity defect above. Secondary: run one additional fixed phase \(3\pi/4\) block without surgery; check that gains do not merely borrow plasticity from the next shift. No history-erasure or old-task-retention metric substitutes for new-task held-out error.

**Validity.** RK2 with step 0.05; rerun only the strongest comparison at 0.025. Require primary-metric changes below 2%, surgery prediction jumps below \(10^{-10}\), finite states, and old-task warm-up training MSE below 0.1 at the checkpoint. Require relative forward-feature movement \(\|h_{\rm end}-h_{\rm start}\|_F/\|h_{\rm start}\|_F\ge0.1\) during warm-up and a dense middle-layer contribution of at least 10% to time-integrated dissipation during the probe; otherwise this test did not expose the proposed mechanism. Here dense dissipation is \(\|\dot A\|_F^2/n+\|\dot B\|_F^2+\|\dot w\|_2^2/n\), using the specified mobilities. An invalid gate is inconclusive, with no search for a favorable task.

**Decision and stop.** Continue only if all three valid seeds achieve at least 25% primary improvement over the strongest matched ordinary-factor/learning-rate arm, with no more than 5% degradation on the second probe block. Kill this candidate capability if any valid seed shows no gain over that rival, or if improvement disappears under scalar speed matching. Intermediate results are inconclusive and do not authorize a campaign. Stop at 15 CPU minutes or completion of the specified arms, whichever comes first; no GPU, task grid, architecture sweep or new mechanism after inspecting outcomes. Save configurations, raw trajectories, source hashes and numerical-gate results in the new study if execution is later authorized. The fixed initialized matrix still costs \(n^2\) numbers; reduced moving state is not reduced total storage.

```text
for seed in (0, 1, 2):
    state = initialize_exact_prompt_model(seed)
    for k in range(12):
        state = integrate_closure(state, phase=k*pi/2, T=8, dt=.05)
    checkpoint = deep_copy(state)
    for arm, speed in preregistered_arms:
        trial = convert_or_gauge(checkpoint, arm)  # assert same A, B, w
        probe1 = integrate(trial, phase=pi/4, T=8, dt=.05, speed=speed)
        probe2 = integrate(probe1.final, phase=3*pi/4, T=8, dt=.05, speed=speed)
        save_raw_and_metrics(probe1, probe2)
    refine_only_strongest_comparison(dt=.025)
classify_using_frozen_gates_and_stop()
```

This screen used only the authorized paper passages, required skills, and three targeted literature searches. No experiments were run and no repository files were changed.
