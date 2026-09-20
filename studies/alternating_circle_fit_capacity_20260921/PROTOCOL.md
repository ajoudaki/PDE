# Alternating-circle fitting at a matched training budget

The user authorized a sequential test: first test whether a width-55 network
can fit many alternating circle labels, then test the comparable finite
closure if the smaller network does not fit. This new study concerns fitting
the labels, not approximation of a particular trained full-network endpoint.
No prior study's code, data or empirical conclusions are research inputs.
The mathematical model and dictionary words are evaluated independently from
the established `code/` interfaces. The shared checkout and other work remain
unchanged.

Status: protocol fixed before training; implementation and preflight underway.
Root owns this README, execution, analysis, report and sole Git-writer role.
Scoped producer owns `fit_benchmark.py`; independent checker owns `fit_check.py`
and `fit_check.md`. All generated evidence belongs under
`data/generated/alternating_circle_fit_capacity_20260921/`.

## Frozen scientific design

Inputs: m=30,62,126,254 in that literal order, theta_j=2*pi*j/m,
x_j=(cos(theta_j),sin(theta_j)), u_j=x_j/sqrt(2), y_j=(-1)^j,
equal probabilities. Since m/2 is odd, antipodal labels are opposite,
compatible with the bias-free odd tanh architecture. No rotated replications,
sample selection, held-out labels or between-sample teacher is introduced.

Dense model: two equal-width tanh hidden layers, width55, no biases,
f=c.T*tanh(A*tanh(W*u))/n. All W,A,c train; 3190 trainable scalars.
Canonical initialization is maintained `finite_network.initialize`: independent
W entries N(0,1), A entries N(0,1/n), c entries N(0,1/n^2).
Seeds are 20260921,20260922,20260923, fixed before outcomes.

Closure model, when the gate opens: n=1024, p=1, frozen B1[n,5], B2[n,3],
moving W[n,2], M[3,5], c[n]. Prediction is
f=(c/n).T*tanh(B2*M*(B1.T*tanh(W*u)/n)).
This has 3087 trainable and11279 minimal retained predictor scalars.
The latter counts W,c,M,B1,B2, excluding solver workspace, cached transposes,
uniform implicit weights, initial diagnostic copies and the temporary dense
initial matrix. Its separate total-size control is dense width105,11340 scalars.

Finite dictionaries evaluate the maintained order-one initialized words on
one independently generated full initial network: H=tanh(W0), U=tanh(A0*H),
R=tanh(A0.T*U); raw first basis=[1,H,R], second=[1,U], in maintained word order.
Normalize each raw basis as raw*L^(-T), with L*L.T=raw.T*raw/n+I/4096.
Set M0=B2.T*A0*B1/n. Retain the actual random initial c. Labels and future
states do not enter this construction. The source A0 is not a moving parameter.

Primary initialization has input gain1. The prescribed rescue multiplies
only the initial W by m/2, before constructing any dictionary. This allows
initial angular features on the spacing scale. It is a separately reported,
noncanonical initialization, applied identically to both architectures.
Each model uses its own width in initialization and output scaling; no prefix
selection or favorable initialization coupling is imposed.

## Optimization and endpoint

This is a finite optimization experiment, not numerical integration of physical
gradient flow. Both models optimize equivalent coordinates W,middle,v=c/n;
canonical c=n*v is saved. Use CUDA float64, no TF32/mixed precision,
one CPU numerical thread and full-batch unhalved mean squared error.

Per attempt: Adam, at most8000 steps, learning rate0.01 for the first4000 and
0.003 for the remainder, default betas(0.9,0.999), eps1e-8, no weight decay;
then LBFGS from the best finite state, lr1, strong-Wolfe search, history50,
max_iter1000, max_eval2000, tolerance_grad1e-12, tolerance_change1e-14.
Track every evaluated finite state, including line-search trials; a fitted
trial is a valid parameter witness and is labelled as such. Keep the state
with lowest evaluated training MSE, not a selected test metric.

Finally, where time permits, freeze the best hidden features and solve the
linear readout by float64 least squares with rcond1e-12. Record effective rank,
singular values/condition, readout norms and actual recomputed loss; retain it
only if it improves the training MSE. This uses no additional model parameters.
No weight norm constraint is imposed. Large coefficients require numerical
replay before a fitting claim, rather than being silently accepted or excluded.

Fit means MSE<=0.001 and y_j*f_j>0 for every sample. Stop an attempt on a
verified fit, nonfinite failure, optimizer completion or wall cap. Reserve
the last5 of60 attempt seconds for final readout/export where feasible.
Save initial, terminal and best states; all attempted outcomes remain visible.
Report sign errors, MSE, maximum residual, gradient norm, weight norms,
hidden saturation, evaluations, steps, timing and terminal reason.

## Gates, replication and terminal stop

Stage A: run all three canonical seeds for width55 at each of the four m.
If no seed fits at a given m, run its three prescribed high-gain rescues.
One numerically verified fit suffices to refute failure-to-fit at that m;
report all attempts and success counts, not an aggregate best-of-baselines score.

Stage B: select the smallest m>55 for which none of the six Stage-A attempts
fits. Run the n1024,p1 closure and width105 total-size control at that m,
three canonical seeds each, plus three high-gain rescues for each model if
none of its canonical seeds fits. If there is no qualifying m, do not run
the closure: the requested failure case was not found in the bounded ladder.
Only this one selected case receives the conditional comparison.

For each model in the selected comparison, reproduce the lowest-MSE attempt
in a fresh output directory with the exact same settings; this is a numerical
reproduction, not another seed or an extra optimization opportunity. If no
Stage-B case exists, reproduce the lowest-MSE width55 attempt at m254.
At most24 Stage-A,12 Stage-B and3 reproduction attempts:39 total.
No further width, m, seed, optimizer, gain or dictionary-order search.

Maximum attempt wall time60s. Total worker-process wall budget2500s, including
Python setup and output; root reserves per-launch allowances and stops launching
when the remaining allowance is insufficient. At most two GPU workers at once,
one per available GPU. Ordinary independent CPU preflight/replay checks are
separately limited to300s. Stop after these branches irrespective of winner.

## Validity and interpretation

Before training: verify data/parity, counts, canonical initialization,
dictionary word ordering/algebra and forward/gradient agreement against the
maintained engines. Independently construct finite-weight fitted dense-network
witnesses with q=m/2 active neurons (padded to55 when q<=55). These are explicit
representability controls, not trained baselines and never optimizer warm starts.
They prevent confusing optimization failure at m30/62 with lack of capacity.

Independently replay all retained initial/best/terminal predictions and losses
from raw arrays, check frozen-dictionary construction and source/config hashes,
and verify fit flags. Baseline independent tolerances are maximum prediction
discrepancy1e-8 and MSE discrepancy1e-9; failures are numerically unresolved,
not scientific wins. Investigate large-coefficient cancellation with higher
precision replay only; no new training is authorized by that diagnostic.
Same-settings fresh reproductions must agree on fit status and MSE to1e-6;
otherwise mark the affected conclusion numerically unstable.

Evidence favoring closure fitting is a checked closure fit while no width55
attempt fits the same labels in the declared suite. If both fail there is no
demonstrated closure advantage; if width55 fits, it solved that instance.
Every failure is failure within the tested optimization/time budget, never a
representation lower bound. No asymptotic rate or generalization claim follows.
Width105 remains a separate total-size comparison. Numerical errors/timeouts
remain labelled; they are not silently converted to capacity failures.

## Evidence and reproduction

Exact commands, source hashes, environment, raw arrays and accounting will be
recorded in this study's generated run directories and linked here on completion.
No established-code edit or promotion is authorized or planned.
