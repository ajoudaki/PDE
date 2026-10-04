# Independent multidata implementation and evidence audit

2026-10-04. Scoped internal implementation/evidence audit by
`multidata_audit`; this is not a promotion review. No scientific training was
performed by this auditor. The audit writes only this report,
`audit_gpu_multidata.py`, and its own generated audit directories.

## Scope and scientific conventions

Inputs read: the complete original numerical sampler and GPU runners,
`neuron_sampling_multidata.py`, `gpu_multidata_experiment.py`,
`analyze_gpu_multidata.py`, the frozen `GPU_MULTIDATA_PROTOCOL.md`, the
multidata configuration generator, the earlier GPU sampling/RMS protocols and
result/selection reports, and directly used maintained network equations and
initialization. Required shared instructions and the canonical-notation skill
were read. No other study, archived book, or other reviewer's findings were used.

There are m training directions, each a unit row of U in dimension d; physical
inputs are sqrt(d) times those rows. The unhalved mean squared loss is
sum_a(f_a-y_a)^2/m. Consequently every parameter velocity contains 2/m.
The maintained Torch engine already accepts normalized directions: applying
another input factor 1/sqrt(d) would change the model.

For N selected neurons in each hidden layer, the model retains A of shape
(N,d), K of shape (N,N), readout w of length N, and positive mass vectors
mu and nu of length N. Its forward map is

    h = tanh(A u),
    g = tanh(K diag(mu) h),
    f = w^T diag(nu) g.

The equivalent mixer B=K diag(mu) has weighted adjoint
B*=diag(mu)^(-1) B^T diag(nu). The ordinary transpose is not that adjoint.
Moving coordinates number N^2+(d+1)N; masses and training directions/labels
add 2N+m(d+1). Thus the full retained count is

    P = N^2+(d+3)N+m(d+1).

Setup arrays, source bases, selected-index diagnostic archives and the dense
experimental controls are separate from this runtime count. This count is
not a claim that the entire experimental process has small memory.

## Initial construction checks

`audit_gpu_multidata.py` differentiates the scalar dense loss using Torch
autograd, then differentiates its gradient-flow vector using a Jacobian-vector
product. This independently checks the first reverse and second forward
physical-time derivatives supplied by the sampler. At zero initial readout,
both hidden parameter velocities vanish, so the second derivative of a hidden
feature is its state derivative applied to the parameter acceleration.

The configurations (d,m)=(2,2),(2,4),(2,8),(3,4),(5,8) all passed. The largest
absolute discrepancy across h'', g'', delta', W0^T delta' and W0 h'' was
5.56e-17. This includes the extra 2/m factor in parameter accelerations.

Tiny construction fixtures with (d,m)=(3,4),(5,8), N=20 and rank8 passed
strictly positive unit-sum masses, weighted-adjoint identity, exact P counts,
zero initialized readout, selected A shapes, and rejection of a witness with
different labels or setup probes. Both final cubature solves succeeded.
SciPy emitted its documented intermediate bound-clipping warning on one
fixture; no final optimizer failure occurred.

The first executed check is archived in
`data/generated/closure_sampling_20261003/gpu_multidata_audit_jets_20261004/`.
Its JSON retains source hashes, exact command and software versions. The
general-dimension adapter hash at this check was
`0f00a5ab8f63b2e57ea4f7e66ab67536f9815b2f5f57da00c4993e4d6aebecc0`.

## Query and witness limitations to retain in the result

Sphere queries use normalized-Gaussian directions from a seed distinct from
setup probes and training directions. Embedded-circle tasks use full ambient
sphere queries, so their metric is not circle RMS. Sphere panel doubling is
a prefix extension; circle doubling contains the original points.

For comparability the circle panel preserves the earlier odd-sized half-cell
grid. It contains one direction antipodal to a setup direction. Because the
bias-free tanh predictor is odd, this is one effectively repeated setup
direction. The frozen protocol explicitly discloses this; the circle panel
must not be described as wholly disjoint from setup up to antipodes.

At m=8 the second-layer priority matrix [G_train,Z_train] can have rank16.
Thus rank16 can allocate the entire second-layer basis to training priorities,
with no additional basis directions for the other derivative sources. This
is the unchanged constructor's behavior, not a coding defect. Report priority
rank and measured source defects rather than attributing all changes to N.

## Runtime checks

The new runner applies the common factor 2/m to the old right-hand side, and
calls the old simultaneous Heun step with dt times 2/m. This is exactly Heun
for the rescaled vector field; reported physical observation times retain dt.
General-dimension initialization calls the maintained NetworkEngine with d.
Packing and retained-state reconstruction use the actual input dimension.

On all five (d,m) fixtures listed above, the independently checked dense RHS
agreed with the maintained public engine within 1.39e-17. Heun agreed
bitwise. A separately constructed rectangular nonuniform weighted-loss
autograd oracle agreed with the reduced RHS within 1.22e-17. The explicit
probe adapter produced a bitwise-identical witness to the original constructor
on its original two-input 32-probe circle task.

Evidence is in
`data/generated/closure_sampling_20261003/gpu_multidata_audit_core_20261004/`.
An additional run at `gpu_multidata_audit_core_restart_20261004/` saved only
the reduced state, masses, training directions/labels and current time for
all five fixtures. Four steps after reload matched the corresponding
uninterrupted eight-step path bitwise. The general-dimension initialization
factory also reproduced the maintained A0 and W0 arrays bitwise.
The complete audited runner hash is
`c067cabcff67c9774a57bb0ebd8c721de3b4bd03fb3cded47cc3d5242c715e73`.
Before launch, both the auditor and coordinator identified two configuration
startup mismatches (an unused include_frozen field and a short protocol path).
The coordinator corrected the configuration generator and files before any
scientific worker started. No numerical equations or sampler parameters were
altered in response to outcomes.

## Independent raw evidence checks

An early audit independently recomputed all completed archives available at
that point: 22 baseline cases across the two workers. It checked source and
configuration snapshots/hashes; artifact hashes; actual directions, labels
and setup probes; both RMS/time orders, endpoint RMS and maximum error;
sqrt(n) scalings and paired dense ratios; exact P and maximal affordable N;
full-tail settlement; zero initial readouts; selected original A rows; and
prediction reconstruction solely from each reduced restart.

All checks passed. The largest restart reconstruction difference was
1.12e-16. The check separately saved the error over the common initial horizon
[0,120], which avoids interpreting unequal stopping horizons as a width trend.
Evidence is in
`data/generated/closure_sampling_20261003/gpu_multidata_audit_archives_early_20261004/`.

These checks validate adverse as well as favorable observations. In particular,
the two completed embedded-circle d5, n512 cases had scaled errors about .236
and .256, exceeding the frozen .15 ceiling, and many m8 trajectories reached
T1200 without settlement. These are recorded outcomes, not implementation
errors or grounds to omit a case.

The completed baseline audit subsequently covered all 72 prescribed cases
across the two original workers and their unchanged resume roots: 70 reduced
trajectories and two preserved construction failures. All raw checks passed,
with maximum reduced prediction reconstruction error 1.67e-16. The evidence
is `gpu_multidata_audit_baseline_complete_20261004/` in the generated namespace.

Both original workers reached their 900-second limits. The repeated
`sphere3_tetra4`, n2048, seed9412 case reproduced every archived query,
training, residual and feature-motion value through time 233 bitwise
(234 observations). The repeated `sphere3_eight_smooth` case at the same
width/seed reproduced all four traces through time 715 bitwise
(716 observations). The two previously unstarted cases also completed.
Earlier partial records remain preserved, and are not additional replicates.

The independent baseline summaries preserve the distinct protocol outcomes.
Both close-pair tasks fit and pass the ceiling and growth criteria. The
four-point harmonic case stays below .15 but has median scaled-error growth
2.674; the tetrahedron case also stays below .15 but has growth 1.519, narrowly
above the frozen 1.5 cutoff. Eight-point circle errors can be small while
settlement remains unresolved. Embedded-circle sphere tasks exceed the error
ceiling, with maximum scaled discrepancies .338733 (d3) and .462494 (d5).

The final confirmation, refinement and resource audit appears below.
This audit does not turn sampled finite-panel/finite-time evidence into a
uniform all-sphere, all-time, or asymptotic guarantee.

## Checked initialization diagnostic

A further independent audit reconstructed the original dense initialization
at n2048, seed9411 for the eight-point smooth circle and the same training
geometry embedded in dimensions 3 and 5. Let A0 and W0 be that original
read-in and mixer. Evaluating the training directions and 32 setup directions
gives H0=tanh(A0 directions^T), Z0=W0 H0 and G0=tanh(Z0). The priority matrix
concatenates the m training columns of G0 and Z0. In all three cases its
resolved rank is 16, exactly the entire second-layer rank budget.

The auditor formed an orthonormal basis Q of this priority matrix directly
using an independent SVD, then recomputed
norm(G0-Q(Q^T G0),F)/norm(G0,F). No saved sampler basis or trained state was
used. This gives:

| Training geometry and query dimension | Relative initialized G0 projection defect |
|---|---:|
| Eight-point circle, d2 | .005332559080317207 |
| Same circle embedded in d3 | .5586958308542835 |
| Same circle embedded in d5 | .6802938988225843 |

The independently reconstructed values agree with the archived diagnostics
within 2.61e-18. The directions in this diagnostic are the constructor's
initial source directions, not the separate prediction evaluation panel.
At a fixed initialization and rank, adding cubature nodes does not change
this priority span. These defects identify a source-representation limitation
of the selected basis; they do not prove that it causes every later prediction
error, or that a particular alternative basis or rank repairs the trajectory.

Evidence: `gpu_multidata_audit_source_defects_20261004/deterministic_checks.json`
under the study's generated namespace. That run also independently checked
all 68 baseline records available at the time, with maximum restart error
1.67e-16.

Two construction failures were present at that checkpoint, both with n2048,
seed9411 and N72. `circle4_smooth` failed the second-layer cubature;
`sphere3_eight_smooth` failed the first-layer cubature. Both rejected invalid
positive-mass output under the unchanged numerical feasibility check. Their
requested P counts were 5556 and 5648, respectively. Dense-only trajectories,
tracebacks, requested samplers and empty reduced-model lists remain archived;
the missing reduced trajectory must not be counted as an accuracy pass.

## Prespecified diagnostic evidence

The independent audit of the two diagnostic roots passed for all four
completed cases: seven constructed reduced trajectories and five constructor
failures. Every constructed candidate had successful final cubature statuses
and retained all selected frame modes. Maximum reconstructed prediction
error was 8.33e-17. Evidence is
`gpu_multidata_audit_diagnostics_20261004/deterministic_checks.json`.

All diagnostic cases use n2048 and seed9411. At `circle4_smooth`, the 2x/rank16
and 2x/rank24 candidates settled with scaled errors .0043123 and .0119433;
both store P=11348. The 4x/rank32 constructor failed in its second layer.
This is an adaptive diagnostic result, not an independent validation.

For `embedded_circle8_d3`, scaled errors were .307524, .072420 and .050051
for 2x/rank16, 2x/rank24 and 4x/rank32, respectively. Actual counts were
11259, 11259, 22523. All remain unsettled at T1200. Enriching the response basis
is associated with a large finite-horizon improvement in this one case;
endpoint accuracy and a general rate remain unresolved.

For `embedded_circle8_d5`, only 2x/rank16 constructed, with P=11268 and scaled
error .437489, still above the ceiling. The rank24 and rank32 candidates
failed construction in layers two and one, respectively. For
`sphere3_eight_smooth`, only 2x/rank24 constructed (P=11259, scaled error
.040163); the rank16 and rank32 candidates failed first-layer cubature.
These completed sphere cases were also unsettled at T1200.

The fifth diagnostic, `sphere5_eight_smooth`, reached its worker deadline
during evolution at time 84.2, leaving 85 saved observations and a partial
record. It was not included among the four completed cases or treated as a
failed prediction test at the full prescribed horizon. No optimizer
tolerance or source construction was changed to suppress these failures.

## Final confirmations, refinement and resources

The final independent audit covered all nine scientific output roots and all
83 complete case records. They contain 84 complete reduced trajectories:
70 baseline, seven diagnostic, five confirmation and two refinement models.
The two baseline and five diagnostic constructor failures remain separate.
Every complete record passed source/configuration/artifact checks, metric and
settlement recomputation, state counting, and reduced-state reconstruction;
the largest reconstruction difference remained 1.67e-16.

Five of the six prescribed multi-circle confirmation cases completed under
the selected 2x/rank16 budget. At seed9412, `circle4_smooth` had scaled errors
.00977570 at n512 and .00736063 at n2048, giving growth .752952; both settled.
The corresponding `circle4_harmonic` errors were .04566473 and .09218027.
Both settled and met the ceiling, but their growth 2.018632 failed the 1.5
criterion. `circle8_harmonic` at n512 remained unsettled, while its n2048 run
was stopped by the campaign deadline at state time 507, with saved observations
through time 506. Thus the increased budget is not validated for the whole
multi-circle group.

The circle resolution case was `circle2_close_opposite`, n512, seed9412,
through T240. The sphere case was `embedded_circle8_d5` at the same width
and seed, through T1200. Both halved dt, halved observation spacing and
doubled nested query panels. Their initialized reduced arrays and setup
directions matched the coarse run bitwise, independently checked from the
saved runtime initialization.

Both resolution checks passed their prespecified gates. Across all models,
the maximum matched prediction changes were 1.53619e-6 (circle) and
1.99838e-5 (sphere). For the reduced model, the changes in the primary error
on the original queries were 1.10653e-7 and 3.30371e-7. The sphere's added
queries changed that metric by 3.16454e-4, about 2.8% of the original error.
This is finite-panel quadrature sensitivity and was kept separate from the
time-step check. Doubling a finite sphere panel does not certify sphere-wide
accuracy.

The union of all nine worker intervals was 1496.853589 seconds, below the
1500-second cap by 3.146411 seconds. This calculation uses provenance-file
mtime through final-status-file mtime, merges overlapping intervals and
excludes idle gaps; it includes model construction, completed evolution and
failed/interrupted attempts. Worker timer estimates agree with these starts
within a few milliseconds. This timing convention starts after environment
startup and source archival. Maximum reported GPU allocation was 421450752
bytes, below 8 GiB per worker. The final confirmation was interrupted before
the computed campaign deadline; no additional scientific training followed.

Complete final evidence, exact commands, source snapshots and hashes are in
`data/generated/closure_sampling_20261003/gpu_multidata_audit_final_20261004/`.
`deterministic_checks.json` contains every raw-record, resume-prefix and
refinement result. `worker_budget.json` separately preserves the interval
endpoints and union calculation. The final audited scientific runner and
sampler-adapter hashes remain the hashes recorded above.

The implementation and recorded finite-grid evidence pass this internal
audit. The audit does not resolve unfinished diagnostic/confirmation paths,
unsettled endpoints, sparse replication, constructor robustness or any
asymptotic/all-time approximation claim. No promotion review or independent
full-campaign scientific rerun was performed by this auditor.
