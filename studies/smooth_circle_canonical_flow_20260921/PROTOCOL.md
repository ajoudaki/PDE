# Frozen canonical-flow mixed-frequency comparison

User authorization: the 2026-09-21 request to implement the specified smooth
target and test for a closure advantage with canonical initialization and
gradient flow. This authorizes this bounded experiment, not a search for a
different target after seeing its results. Frozen before scientific training.

## Scientific question and fixed data

Does the n=1024, p=1 initialized-observable finite closure achieve substantially
lower regression error than either parameter-matched dense network under the
canonical physical gradient flow at a common time T=1000? Alternatives include
both fitting, both failing, a dense advantage, a closure advantage, or numerical
inconclusiveness. No representation lower bound, all-time conclusion,
population approximation theorem or asymptotic rate is sought.

Use m=126 fixed locations theta_j=2*pi*j/126, x_j=(cos(theta_j),sin(theta_j)),
u_j=x_j/sqrt(2). Input radius is one in x coordinates; do not renormalize u
to length one. The regression labels are

    y(theta)=sqrt(32/21)*(cos(theta)+sin(3*theta)/2+cos(5*theta)/4).

Their discrete and continuous-circle mean square is exactly one in exact
arithmetic. Labels have odd antipodal symmetry. They are smooth real-valued
regression labels, not binary labels or signs. A passive evaluation panel has
1024 equally spaced angles 2*pi*(j+1/2)/1024 and the same analytic target.
Passive points do not enter the updates. No rotation replicates or target
changes are allowed. Fixed initialization seeds are 20260921,20260922,20260923.

## Canonical dense network and explicit finite dictionary

Two bias-free tanh hidden layers, scalar prediction and unhalved mean square:

    f=(c/n).T tanh(A tanh(W u)),  L=mean((f-y)^2).

The maintained finite initializer draws independent W~N(0,1), A~N(0,1/n),
and stored c~N(0,1/n^2), in that order with NumPy default_rng(seed). No extra
gain, zero-readout substitution, warm start or output rescaling is used.
The dense models have n=55 and n=105, with all W,A,c trainable.

For the closure initialize a canonical source at n=1024. Form

    H=tanh(W), U=tanh(A H), R=tanh(A.T U),
    rawB1=[1,H,R], rawB2=[1,U],
    L_i L_i.T=rawB_i.T rawB_i/n+I/4096,
    B_i=rawB_i L_i^(-T), M0=B2.T A B1/n.

Keep B1[n,5], B2[n,3] fixed; evolve W[n,2], M[3,5], c[n], initialized with
the actual source W and c. Its prediction is

    f=(c/n).T tanh(B2 M (B1.T tanh(W u)/n)).

Both orientations use the same M and transpose. The source A is saved for
provenance but is not used by the evolving predictor. The dictionaries use
no labels, learned target or future trajectory. Their ridge is part of the
specified dictionary, not optimization regularization.

Dense55 has 3190 trainable scalars versus closure3087. Dense105 has11340
retained predictor scalars versus closure11279, including8192 fixed dictionary
entries. Compare these two conventions separately; no best-of-baselines
aggregate. Same integer seeds across widths are not a neuronwise coupling.
Source and diagnostic arrays, ODE stages and optimizer workspace do not enter
these predictor counts, but are not claimed to be absent from runtime memory.

## Actual physical flow and numerical integration

Integrate simultaneous raw-parameter ODEs

    Wdot=-n*grad_W L, middle_dot=-grad_middle L, cdot=-n*grad_c L,

with middle=A or M. This is the canonical fixed block metric, kappa=1, with
the loss's factor two included. There is no Adam, momentum, clipping, decay,
Armijo optimization, least-squares readout solve, curriculum or label scaling.
Adaptive ODE steps control integration error, not optimizer learning rates.

Use CPU float64 NumPy analytic contractions and SciPy DOP853 with one BLAS
numerical thread. Use a stable tanh derivative matching the maintained NumPy
model, evaluated as sech^2(z) from exp(-abs(z)), rather than losing derivatives
through 1-tanh(z)^2 cancellation. Save saturation diagnostics. Local solver
error estimates are not global error certificates; independent refinement is
mandatory. Explicit levels are:

| Level | relative tolerance | absolute tolerance | maximum physical step |
|---|---:|---:|---:|
| primary | 1e-6 | 1e-9 | 2 |
| fine | 1e-8 | 1e-11 | 1 |
| finer, conditional | 1e-10 | 1e-13 | 0.5 |

The packed raw-state error scaling uses the solver's ordinary componentwise
absolute-plus-relative scales; different state dimensions are addressed by
the common observable/state refinement checks below. Tolerances are numerical
settings, not modifications of the ODE. Record the SciPy version and actual
solver source hashes. Integrate from initialization at every level; no coarse
trajectory warm start. No early stop on fitting: all valid runs go to T=1000.

Save accepted endpoints at the fixed observation times
0,.01,.03,.1,.3,1,3,5,10,20,40,60,100,160,250,400,630,800,1000.
Force integration boundaries there; do not interpolate an unverified loss
minimum. Save every accepted step's time, loss, step size and RHS count,
and saved-checkpoint state, RHS, training/passive predictions, losses,
physical squared-gradient norm and hidden-motion/saturation diagnostics.
Save canonical source arrays, raw/normalized dictionaries and data exactly.

## Metrics, decisions and numerical gates

Primary outcome: training RMSE at common T=1000, with all three seed values
and median. Report passive-panel RMSE separately, along with curves against
physical time and actual wall time/RHS counts. A regression fit is MSE<=0.001;
sign accuracy is only a secondary diagnostic for real-valued labels.

For each of harmonics1,3,5, report cosine and sine coefficients and error
energy .5*((a_hat-a_target)^2+(b_hat-b_target)^2), on training and passive
panels. Report residual energy outside those three frequencies. This prevents
fitting only the fundamental from concealing failure on the harder components.
Also report first saved time at MSE<=0.001, which brackets rather than exactly
locates the hitting time. Hidden motion is descriptive, not a nonlazy theorem.

Evaluate a strong separation independently against each dense width: closure
fits at least2/3 seeds, dense fits0/3, and closure median RMSE is at most
one-third the dense median RMSE at T=1000. All required runs must be valid and
complete, and fit decisions must agree at both selected numerical levels.
Other outcomes retain their actual error ratios and fit counts; they are not
renamed a separation. The three fixed seeds provide descriptive replication,
not a confidence interval or universal architecture claim.

Before training, an independent checker must verify the canonical source,
target/data, dictionary/normalization, forward map and physical RHS against
independent NumPy derivation, maintained dense flow, and autograd or centered
per-block finite differences at nonzero-readout states. Target unit RMS,
input norm^2=1/2 and antipodal symmetry tolerance5e-13. Forward/RHS numerical
comparisons use atol2e-12,rtol2e-10; nonzero directional derivative comparisons
use relative1e-6 with absolute floor1e-9. Basis reconstruction uses
atol2e-13,rtol2e-12. Verify parameter counts and gradient dissipation identity.

For every model/seed compare primary and fine at ALL fixed checkpoint times
on training and passive predictions. Require maximum prediction difference
<=2e-4, maximum RMSE difference<=5e-5, and each packed parameter block's RMS
difference <=2e-4*(1+RMS(finer block)). Require equal T=1000 fit decisions.
Accepted-step loss increases must be <=5e-7*max(1,old loss) at the selected
fine resolution. Independent saved-array replay must agree to prediction
max1e-9 and loss absolute1e-10, and RHS to atol2e-12,rtol2e-10. A failure
cannot count as scientific success or failure of fitting.

If the primary/fine accuracy or monotonicity gate fails, run exactly one finer
level for that model/seed, compare fine/finer with the same gates, and use the
finer outcome only if they pass. Preserve the failed coarse comparison. No
further tolerance tuning. Numerical failure or censoring without a resolved
pair makes the affected comparison inconclusive.

## Execution sequence, replication and hard bounds

1. Complete deterministic no-training preflight and freeze producer/protocol
   hashes. Every actual integration binds those hashes and configuration.
2. Run primary and fine for each of the nine model/seed combinations.
   Order seeds increasingly; within each seed width55,closure1024,width105;
   primary then fine. At most two independent workers at once.
3. Execute only the conditional finer runs selected by the frozen gates,
   in the same model/seed order.
4. Reproduce the selected fine-or-finer run for seed20260921 of each model in
   a fresh directory, irrespective of which model wins. Same source/settings.
   Require maximum prediction and parameter discrepancy<=1e-10 and same fit
   decision over all checkpoints. A censored reproduction does not pass.
5. Independently replay/analyze all retained arrays and publish the complete
   comparison with loss/component plots. Stop regardless of outcome.

At most18 primary/fine,9 conditional finer and3 reproduction attempts.
Hard cumulative worker-process wall budget4200 seconds including imports,
failed attempts and output. Each launch reserves430 worker seconds and is
killed by the supervisor at429 seconds. Each worker has400 seconds from CLI
entry for initialization/integration/export, reserves10 seconds for final
export, at most150000 RHS evaluations and30000 accepted steps. Timed-out
workers retain last accepted states and actual common observation prefixes;
they are not treated as converged endpoints. No further launches when the
next reserved batch would exceed the cumulative budget. Checking and analysis
have a separate600-second cumulative process allowance, including meaningful
preflights/replay and figure generation. No GPU training is needed.

Record commands, cwd, environment/thread policy, Python/NumPy/SciPy versions,
HEAD and hashes of all used study/maintained source, process times, stop reasons,
outputs and hashes. Never overwrite a run directory. The runner may be repaired
for operational issues without changing frozen scientific methods; all such
versions and failed attempts remain recorded. A scientific-method repair
requires a documented new frozen version before affected runs, preserving
old evidence. No new targets, seeds, widths, gains, orders, horizons or
optimizers may be added after outcomes. This study does not promote changes
to maintained theory/code. Root alone uses the shared Git-writer lock.

Resource calibration before scientific training: a deterministic initialization
and ten-RHS microbenchmark estimated about0.01064 seconds per closure RHS.
The finer level has a floor of roughly24000 RHS calls at T=1000; therefore
the per-attempt wall allowance was set to400 seconds before source freeze.
No loss trajectory or fitting outcome was used to choose this allowance.
