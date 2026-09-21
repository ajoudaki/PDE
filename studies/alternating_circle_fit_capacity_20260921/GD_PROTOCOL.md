# Frozen full-batch GD-only extension

Authorized by the user's 2026-09-21 instruction “ok, then test that!”, following
the proposed GD-only, smaller-sample comparison. This continues this task's
same alternating-label fitting investigation. The completed Adam campaign and
its PROTOCOL.md are immutable historical evidence. This file is fixed before
GD training; the new user instruction authorizes only the bounded extension
below, independently of unused budget from the completed campaign.

## Decision and model

Question: does physical-mobility full-batch gradient descent give a finite
closure fitting advantage over parameter-matched dense networks at fewer than
254 alternating circle samples? Competing outcomes are a checked separation,
both fitting, both failing, or numerical/step-size inconclusiveness. All concern
the tested finite optimization protocol, not representation lower bounds,
continuous-flow convergence, asymptotic rates or generalization.

Use the same actual model, source initialization, scalar accounting and label
recipe as PROTOCOL.md. Inputs theta_j=2*pi*j/m, x_j=(cos,sin), u_j=x_j/sqrt(2),
y_j=(-1)^j, uniform unhalved MSE; m=30,62,126,254, in that order. The odd m/2
makes antipodal labels opposite. No rotated replications or changed samples.
Seeds20260921,20260922,20260923 are literal and fixed.

Dense networks have two equal-width bias-free tanh hidden layers, n=55 or105,
f=(c/n).T*tanh(A*tanh(W*u)), all W,A,c moving. Closure n=1024,p=1 has frozen
B1[n,5],B2[n,3], moving W[n,2],M[3,5],c[n], and
f=(c/n).T*tanh(B2*M*(B1.T*tanh(W*u)/n)). Width55 matches trainables approximately:
3190 versus3087. Width105 separately matches total retained predictor scalars:
11340 versus11279, including8192 fixed dictionary scalars for the closure.

Regenerate the same initialized finite dictionary from Gaussian source W,A,c,
using H=tanh(W),U=tanh(AH),R=tanh(A.T U), rawB1=[1,H,R],rawB2=[1,U],
B_i=rawB_i*L_i^(-T), L_i L_i.T=rawB_i.T rawB_i/n+I/4096,
and M0=B2.T A B1/n. Actual Gaussian c is retained. Source A is diagnostic
provenance, not a trainable closure parameter or retained predictor component.
The high-gain regime multiplies initial W by m/2 before constructing the
closure; the canonical control uses gain1. Other initial distributions remain
W~N(0,1), A~N(0,1/n), c~N(0,1/n^2) in the maintained draw order.

## GD and numerical checks

Use simultaneous full-batch raw-parameter updates with unit kappa multipliers:
W_new=W-eta*n*grad_W L; middle_new=middle-eta*grad_middle L;
c_new=c-eta*n*grad_c L. Middle means A for dense, M for closure.
Equivalently in v=c/n coordinates the mobilities are(n,1,1/n).
The loss already supplies its factor2. No Adam, momentum, coordinate-wise
adaptive rates, clipping, weight decay, quasi-Newton steps, Heun updates,
readout solves or optimizer warm starts are permitted.

This is GD with scalar Armijo backtracking, not fixed-step GD or an exact
continuous-flow computation. Maximum eta=1 for the primary runs; eta=.5 for
the registered sensitivity runs. First trial eta is the maximum; later trials
start at min(maximum,2*previous_accepted_eta,remaining_physical_clock).
For Q=n||grad_W||F^2+||grad_middle||F^2+n||grad_c||2^2,
accept a finite candidate only when
Lnew <= Lold-1e-4*eta*Q+1e-14*max(1,Lold).
Reject and halve up to30 times (31 trials). Failed line search is numerically
unresolved, not a capacity failure. Q<1e-28 is a numerical gradient-floor stop,
not proof of convergence; finite replay-checked floor endpoints remain part of
this declared finite algorithm and must be labelled precision-limited.
Physical clock is the sum of accepted eta values.
Only accepted GD states can supply fitting evidence or the best checkpoint.

Every attempt has the same caps:30000 accepted steps,90000 full-batch forward
evaluations including the initial state, physical clock10000, and75 seconds
for initialization/training/export, with5 seconds reserved for export. Stop on
fit (MSE<=0.001 AND every y*f>0), caps, nonfinite state, gradient floor or failed
line search. Numerical policy: CUDA float64, no TF32, deterministic arithmetic,
one CPU numerical thread. Tanh backward uses1-h^2, as in the maintained Torch
engines; saturation can round this derivative to zero and is reported.
Save initial/best/final weights, actual train and
circle-grid predictions, every accepted-step loss/eta/Q/clock, rejected trial
counts, terminal reason, gradient and weight norms, timings and source hashes.
Save auditable GD before/after state pairs at first/last and selected internal
steps. A wall/step/clock stop is only a finite-budget endpoint, not a converged
minimum. Compare and report all actual stopping times and gradient diagnostics.

Before training, independently check nonzero-readout gradients and simultaneous
GD steps against maintained engines, including both GPU devices and initialized
high-gain models. Replay retained predictions with max discrepancy1e-8 and MSE
discrepancy1e-9, check source/dataset/dictionary construction and exact update
pairs, and verify Armijo/clock/seed/gate/budget arithmetic. Any unexplained
numerical error blocks the affected fitting comparison. Higher-precision
replay of saved weights may diagnose cancellation; it authorizes no training.

## Predeclared sequence

1. At each m in30,62,126,254, run dense55 and closure1024 with high gain and
   eta_max1, three seeds each. Primary candidate separation means closure
   fits at least2/3 seeds and dense55 fits0/3, with all runs numerically valid.
   Stop this ladder at the first candidate. If none qualifies, finish at254;
   that final case is the diagnostic comparison, with no candidate claim.
2. At the selected case (first candidate, otherwise254), run dense105 with
   high gain and eta_max1, all three seeds.
3. At that case run all three models with high gain and eta_max.5, all three
   seeds, keeping all other caps fixed. Call the width55 separation insensitive
   to this step-cap change only if closure fits>=2/3 and dense55 fits0/3 at
   BOTH caps. Assess the width105 comparison separately using the same rule.
   Halving a maximum step is a learning-rate sensitivity check, not a proof
   of Euler convergence; inspect realized steps and physical clocks as well.
4. At that case run all three models with canonical gain1 and eta_max1, all
   three seeds, explicitly separate from the high-gain primary comparison.
5. For each of the three models and each high-gain step cap, reproduce the
   first successful seed in increasing seed order, or seed20260921 if no seed
   fitted, in a fresh directory with the exact same settings/device. Repeated
   fit status must match and endpoint MSE must differ by<=1e-6. Otherwise the
   endpoint reproduction does not pass. If a wall cap produces different
   accepted-step counts, label it time-censored and additionally compare the
   shared accepted-step trace prefix, distinguishing this from an arithmetic
   discrepancy at identical steps. No extra training follows either failure.
   Reproductions are not additional seeds.

No additional sizes, seeds, gains, optimizers, rates, schedules, horizons or
continuations may be added after observing outcomes. At most24 ladder,3 size
control,9 step-sensitivity,9 canonical and6 reproduction runs:51 attempts.
Each launch reserves85 worker seconds, supervisor kills at84 seconds, at most
two workers on different GPUs. Hard cumulative worker-process wall budget2500s,
including imports/output and failed attempts. Stop launches if the next reserved
batch would exceed the cap; retain a budget-limited result and all completed
attempts. Independent no-training preflight/replay/analysis limit300s. Stop after
these stages regardless of winner; no promotion or maintained-code edits.

## Evidence and responsibilities

Generated evidence: data/generated/alternating_circle_fit_capacity_20260921/
gd_run01 and separately named gd_check_scratch/gd_analysis01 products. Existing
Adam artifacts are read-only. Each run binds source/configuration/this protocol
hashes and records commands, environment, hardware and all attempts.
Root owns this protocol, README updates, GD runner, execution and sole Git writes.
Scoped producer owns gd_benchmark.py; independently scoped checker owns gd_check.py
and gd_check.md; analysis ownership will be assigned before its edits. Existing
fit_benchmark.py may supply already checked initialization/data helpers only;
its optimizer routines are never used in a GD run.
