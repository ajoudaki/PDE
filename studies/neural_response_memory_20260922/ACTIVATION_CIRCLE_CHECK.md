# Activation-circle internal independent audit

Auditor: `/root/activation_audit`, 2026-09-25. This is an internal implementation
and algebra check, not an independent promotion review. The audit is scoped to
the frozen activation protocol and its new implementation. It has not read
older result/review verdicts or other studies.

## Current disposition

**Pre-execution algebra checks pass.** All 632 independent CPU checks passed;
the largest absolute discrepancy was `1.3322676295501878e-15`. This does not
establish training fit, closure fidelity, solver convergence, or nonsmooth
well-posedness. Saved-trajectory replay, final numerical gates and repetition
checks remain pending until the authorized campaign produces their inputs.

The independent source is `check_activation_circle.py`; raw evidence is
`data/generated/neural_response_memory_20260922/activation_circle_audit01/selftest_02.json`.
The earlier 608-check pass remains preserved in `selftest_01.json`; the second
version adds 24 checks of independent panel prediction and feature diagnostics.
The evidence records checked source hashes, NumPy/Torch versions, every check
and its error. CPU execution used `/home/amir/miniconda3/bin/python`, one
numerical thread, and `PYTHONDONTWRITEBYTECODE=1`. No training trajectory or GPU
operation was launched by this auditor during the pre-execution audit.

## Exact theory checks

For the declared output `c^T h3/n`, unhalved mean squared loss, actual unit
circle rows, and mobilities `(n,1,1,n)`, independent differentiation gives

\[
 \dot w=-\frac2M(\delta_1r)U,\qquad
 \dot W_\ell=-\frac2{Mn}(\delta_\ell r)h_{\ell-1}^T,
 \qquad\dot c=-\frac2M h_3r.
\]

The backward fields use the actual matrix transposes and exclude residuals.
These formulas match all four production physical blocks against independent
Torch automatic differentiation at noninitial small dense states.

For each link write `L=1+s`, `v_k=2k+1`, `u=r delta/rho`, and retain the
declared unnormalized Legendre moments `A_k,B_k`. Differentiating
`J=sum_k v_k A_k B_k^T/L` with the lower-triangular transport gives

\[
 \dot J=\rho\{u h_P^T+u_P h^T-u_P h_P^T\}.
\]

The diagonal coefficient is `1+2k=v_k`; the two triangular sums give the
off-diagonal coefficients `v_j v_k`. Therefore the physical defect is

\[
 E_\ell=\dot{\widehat W}_\ell+
 \frac2{Mn}(r\delta_\ell)h_{\ell-1}^T
 =\frac2{Mn}(r\delta_\ell-\rho u_P)(h_{\ell-1}-h_P)^T,
\]

with the sample contraction understood. The sign and both link indices in
the derivation and implementation agree. The division-free formula remains
defined when `rho=0`. Initial B moments use the selected activation, so the
initial defects vanish and all physical initial tangents match. Arbitrary
noninitial moment arrays were used for the numerical identity checks; these
were not restricted to a specially favorable reachable initialization.

The derivation's covariance residual, rank counts, and loss-defect pairing
are correct under its stated integrability and trajectory assumptions. The
smooth local uniqueness argument applies to GELU and sigmoid on `L>0`:
the residual norm is locally Lipschitz, which is sufficient even at zero
residual. The zero-residual absorption argument is valid for an existing
absolutely continuous selected-field trajectory with locally bounded state.
It does not assume nonsmooth uniqueness elsewhere.

ReLU uses derivative zero at zero; SELU uses `lambda*alpha` there. Those are
selected reverse-mode values, not ordinary derivatives at the kinks. Their
stage fields can be discontinuous. The text correctly avoids a general
existence/uniqueness or smooth-Heun-order claim across switches. The optional
sigmoid and GELU rational lifts are distinct from the implemented direct
coordinates; the stated compatibility identities follow by differentiation.

No activation in this continuation is odd. The former bias-free odd-network
argument supplies no quotient for these activations; all eight literal rows
and labels are retained. The shared initialization checks confirm no gain,
centering, readout rescaling, or extra first-input normalization was inserted.

## Independent numerical algebra checks

The 632 checks cover:

- Values and derivatives against independent Torch primitives/autograd for
  ReLU, exact GELU, SELU and sigmoid, including each declared kink value.
- Values and derivatives at finite inputs through magnitude `1e300` against
  independent NumPy/SciPy formulas. These inputs have representable selected
  outputs; this is not a claim that every finite-input network product can
  never overflow.
- All four physical gradients and prediction formulas at noninitial states.
- Exact NumPy draw order and identical parameter initialization across all
  activations and P=1,2,3, with activation-specific initial B moments.
- Both explicit physical matrices, both transpose actions, physical forward
  and backward fields, independent P=1,2,3 transport, clock velocity, physical
  derivative factors, defects and defect Frobenius norms at noninitial states.
- Exactly vanishing state velocities and defects at noninitial states whose
  labels are set to their current predictions, exercising the zero-residual
  boundary without a division by residual RMS.
- Independent explicit-matrix query prediction and activation/derivative
  distribution diagnostics at all twelve activation/order combinations.

The independent saved-state checker uses explicit physical matrices and
independent Torch activation primitives. It does not import production
engines for replay. It checks hashes and every archive-member CRC, regenerates
the initialization from NumPy, evaluates training/panel predictions from
every available selected checkpoint, recomputes training MSE, and independently
scores paired panels and solver sensitivities. Repetition checks compare
common accepted trace prefixes and common event states/predictions exactly,
while excluding unequal capped endpoints and checking the swapped GPU/config.

## Issues found and their disposition

1. **Endpoint-bracketed events are not certified first crossings.** Moment
   loss need not decrease, and loss along a Heun state interpolant need not
   be monotone. Bisection certifies a bracketed root but does not exclude an
   earlier crossing within the same accepted step. This was reported before
   execution. The new runner sorts observations by computed event time and
   excludes events after its selected target fraction; fixed-time observations
   are strictly before a target endpoint. Those changes address event order
   and out-of-interval observations. First-crossing certification remains
   outside the numerical method and must not be claimed in the result text.
2. **External wall watchdog allowance.** The initially inspected launcher
   reserves five seconds but kills an integrating worker three seconds after
   its wall cap. A last accepted step that includes event bisections, an
   8192-point panel, state serialization and CRC could exceed that allowance.
   This was reported before execution and repaired before the first pilot:
   the reread protocol and launcher now reserve 35 seconds with 30 seconds of
   watchdog grace. The remaining five seconds cover polling/termination.
   Final saving occurs after the integration lifecycle ends and is excluded
   from that watchdog. Any external termination still remains a preserved
   execution failure, not evidence against the closure. Actual dispositions
   will be checked after execution.
3. **No algebra failure found.** The independent checks had no failed cases
   to repair. Numerical gate failure, a training cap, or lack of a shared loss
   milestone remains logically separate from a wrong implementation.
4. **Paired dense refinement was initially missing from analysis requests.**
   The first analyzer implementation requested only the affected closure when
   dense sensitivity passed. The protocol requires a same-case dense third
   tolerance alongside every eligible closure third tolerance. This mismatch
   was reported before branch selection. The analyzer now adds the paired
   dense request with an explicit protocol reason, unless that resolution has
   already been executed.
5. **Failed refinement could expose older comparisons as apparently valid.**
   The inherited selector keeps only valid archived runs. The new analyzer now
   records failed/pending extra attempts, consumes/reserves their single
   allowed branch, prevents retries, and marks affected older comparisons
   numerically unresolved. Missing additional evidence is filtered out of
   trigger reasons, so it cannot itself authorize another solver experiment.
6. **Inherited provenance validation was insufficiently specific.** The old
   generic loader accepted arbitrary self-consistent declared source lists
   and did not enforce every frozen solver control. The new wrapper now
   requires the exact four producer source names, phase/tolerance pairing,
   fixed scientific controls and observation schedule. The inherited
   analyzer and frozen producer were not edited for these repairs.

## Independent analysis check

The lead expanded the scoped inputs to the complete new
`analyze_activation_circle.py`, `test_activation_analysis.py`, and the exact
inherited helper source `analyze_deep_circle.py`; no old generated evidence
was read. Full-source review confirms that actual stored training predictions
determine milestone MSE, nested panels use alternate points from the same
8192 grid, and every order uses one common finest valid dense reference.
Separate absolute and relative sensitivity gates and the summed-sensitivity
order-ranking margin agree with the protocol.

Fourteen independently constructed Fourier checks all passed in
`activation_circle_audit01/analysis_checks_01.json`. They verify analytic
RMS values, one dense reference, a correctly detected P3 worsening, absence
of unneeded refinement, paired dense inclusion, deferral until the primary
schedule finishes, failed-extra invalidation and no retry, pairwise primary
availability when P3 is capped, a separately identified all-model common
fallback, and physical-loss-triggered refinement of the affected closure
plus dense. These are synthetic reporting fixtures with zero training runs.
Source hashes are retained with the results. They do not count as scientific
campaign evidence.

## Frozen continuation coordinator review

At the lead's explicit request, the complete new
`finish_activation_circle_campaign.py` was reviewed as an additional scoped
source, at SHA256
`7fe3210a92c4afa6fd13d8ac79e993fc011e0a3f8e6b63cba9452df399763f5c`.
This review ran no process and changed no frozen source.

The coordinator requires every one of the 64 scheduled primary configurations
to have a terminal summary/failure receipt. It independently compares their
literal scheduled configurations and paths, checks frozen source hashes, and
then invokes the fixed analyzer. Its only conditional scientific launch is
one batch of at most 32 prescribed third-tolerance selections, with a paired
dense selection for each closure. The second analysis cannot launch a new
branch: remaining requests are retained as unexecuted evidence.

Exactly eight dense/P3 outlier repetitions are selected at their finest
attempted scientific tolerance, including failed attempts, with the launcher's
GPU-swap check. All scientific stages inherit the launcher's cumulative
integration budget and attempt ceiling. Final accounting is checked against
33000 seconds and 112 attempts. Replay selection balances only panel counts,
includes available pilot/science/repetition states, and does not select by
observed scientific accuracy.

Per-run replay errors remain explicit failed checker records. A failed or
missing original/repetition yields its own preserved reproduction-failure
receipt, and the other independent pairs are still checked. One operational
limitation is retained: if an entire replay subprocess crashes or produces
no output, the coordinator stops before reproduction audits and records an
orchestration failure. This preserves existing evidence but leaves those
later audits incomplete. It supplies no scientific pass/fail conclusion.
No unauthorized experiment, retry, fourth tolerance, activation tuning,
additional seed, order search, or overwrite of prior audit evidence was
found in the coordinator.

## Supplemental initial-kernel diagnostic review

The lead separately authorized review of the complete
`ACTIVATION_INITIAL_KERNEL_NOTE.md`, `activation_initial_kernel.py`, and the
named authoritative `activation_circle_initial_kernel02` JSON evidence. The
initially assigned `verification_receipt.json` did not exist; the lead corrected
that input to `correction_verification.json`. Only the corrected receipt and
the hashes it references inside the `02` directory were inspected. No older
kernel result was read, no kernel calculation or training was rerun, and no
GPU or frozen checker source was used or changed.

**The finite-width formulas and reported aggregate numbers check out.** With
the declared mobility, the first-layer and readout Gram blocks carry `1/n`,
and each internal block carries `1/n²`. The residual dynamics give exactly
`r_dot = -2 K r/M` and `-loss_dot = 4 r^T K r/M²` at differentiable states.
The receipt reports zero exact-zero preactivations at all three layers of
each initialized network, consistent with applying ordinary differentiation
there. For the internal quadratic, reduced QR gives
`A B^T = Q_A (R_A R_B^T) Q_B^T`; orthonormal columns preserve its Frobenius
norm, including the width-7 check where the number of samples exceeds width.
The squared-norm calculation avoids subtracting large Gram entries to obtain
a small label quadratic.

Every displayed table rate, eigenvalue/condition entry and modal percentage
agrees with the supplied authoritative metrics at its printed precision.
Independent scalar recomputation from those metrics confirms the loss-rate
factors, block trace sums, and heuristic resolution screens. All four recorded
source hashes match the current allowed files; all eight raw archive hashes
match the authoritative metrics; the correction receipt's current source and
metrics hashes match. Reconstructing only the literal scalar input arithmetic
independently reproduces all eight recorded input/data hashes. The recorded
input check covers eight frozen launcher configurations per case, or 64 total.

The supplied tiny autograd receipt contains 16 passing block comparisons,
with maximum kernel-entry discrepancy `1.6653345369377348e-16` and quadratic
discrepancy `7.771561172376096e-16`. The minimum readout contributions are
99.9999782330% of trace and 99.9999122566% of label quadratic, matching the
note's bounds. The correction receipt's maximum changes are `8.32667e-16`
in inputs, `7.18176e-16` in kernel entries, `8.88178e-16` in eigenvalues,
and `5.55112e-17` in actual initial loss-decay rate. These are checked as
receipt/report alignment; the superseded `01` data were not independently
recomputed. The receipt's bitwise forward claim concerns the corrected
diagnostic's own NumPy evaluation, not bitwise equality with GPU training.

The precision interpretation is appropriately limited. The stated screen is
heuristic rather than certified; sigmoid's condition numbers remain withheld,
and small eigenvalues or individual modal directions are not claimed accurate
to a certified relative tolerance. Strong initial anisotropy and weak initial
label response do not establish why later training is slow, whether feature
learning remains small, or whether any closure tracks dense predictions.
This supplemental initial-state diagnostic contributes no closure-fidelity
evidence and authorizes no change to the frozen campaign.

## User-directed GPU restriction and continuation audit

The user subsequently required GPU 1 to remain free until further explicit
authorization. The lead authorized a scoped review of the execution amendment,
the finalized interruption receipts, and the complete new
`continue_activation_circle_campaign.py`. The audited final controller SHA256 is
`8145ce7381180a6c5137f1e13f0d6db103538ac53a1526bb9027cfdc5bfee3ad`.
No frozen producer, analyzer, launcher or checker was edited for this review.

The actual original-primary receipt contains 34 completed attempts, one
external interruption and 29 configurations cancelled before launch. The
interrupted run is exactly
`33_selu__two_outliers_alternating_P1_rtol1.25e-05`. Its charge independently
recomputes to `272.5433204174042` seconds from the release-command timestamp,
original integration-start timestamp and one-second signal allowance. The
preserved original lifecycle hash matches. Original-primary plus pilot
accounting independently sums to `8130.628391414881` seconds across 43
actually launched attempts; paused-scheduler idle time is not charged.

**The resource continuation has no identified launch blocker.** Its default
policy permits only GPU 0 for training and saved-state replay. GPU 1 requires
an explicit policy enabling it with nonempty user-authorization text recorded
by the lead; the controller cannot establish authorization independently of
that trusted lead record. Policy is reread before assignment. The exact
external-interruption flag and release receipt authorize one fresh replacement
only; other terminal failures are not retried, and a completed summary cannot
use this exception. The resulting 30 jobs preserve every original scientific
configuration before resource assignment. Device overrides are separately
recorded. The amended ceiling is 113 launched attempts, and the integration
budget remains 33000 seconds including the interruption.

Analysis receives both original and continuation primary roots. Conditional
third-tolerance refinement remains one bounded batch and includes the paired
dense reference; no residual request causes another batch. Repetitions retain
their configurations and finest executed tolerance. The unmodified checker's
raw `gpu_swapped` flag is preserved. The resource-amended assessment separates
cross-device coverage from numerical reproduction by excluding only
`gpu_swapped` from the latter conjunction. Actual numerical failures and
missing reproduction evidence still fail that assessment. Thus a same-GPU
repeat can establish numerical reproduction without falsely claiming a
cross-GPU comparison.

Twelve independent CPU checks pass in
`activation_circle_engine_check01/independent_resource_review01/checks.json`.
They cover actual 30-job selection, exactly one restart, unchanged old receipts
and scientific configurations, the actual prior charge/attempt count, the
113-attempt arithmetic, blocked/unauthorized/synthetic-authorized policy
parsing, and separation of reproduction success, device coverage and missing
evidence. Synthetic policy files are explicitly test fixtures, not real
resource authorizations. The implementation author's separate eight-fixture
receipt matches the same final controller hash. No process was launched, no
signal was sent, and no GPU was accessed by this independent review.

## Interim independent GELU saved-panel rescore

The lead authorized a bounded CPU verification of the six GELU primary rows
and 42 GELU matched-loss rows in `activation_circle_partial_check03`. A scoped
subagent, `/root/activation_audit/gelu_rescore`, independently recomputed the
panel arithmetic using NumPy and no producer/analyzer imports while the
resource-controller review proceeded. Its complete audit source was then read
by this auditor. The input metrics SHA256 is
`214ad0cb0518aca5d4bcfd9928b196696081f32a2be9bf1012e8260491fd5307`.
The executable audit and raw results are retained as
`activation_circle_audit_interim01/gelu_rescore.py` and `gelu_rescore.json`.
The exact executed source remains unchanged at SHA256
`cb52b299e3125e517f37064c43f47b2b1d015716428e40732d34af1ef64cbf51`.
Its reusable source is additionally retained in the flat study as
`check_activation_gelu_panels.py`, SHA256
`1d398752dac0e53ead6b1e06a876b8cda2dadd7f52ac2ea01748675e1064f4ed`.
Only path handling, CLI help and the provenance docstring changed: this version
requires explicit `--metrics` and `--output` arguments and resolves the study
directory from its own location. Numerical checks and formulas are unchanged.
`activation_circle_audit_interim01/gelu_source_retention_receipt.json` records
both versions, the unchanged evidence hash and a full reproduction command.
Retention validation checked the complete diff and command-line help only;
the scientific audit was not rerun.

To reproduce using the retained source, use one numerical CPU thread and a
fresh output filename:

```bash
/home/amir/miniconda3/bin/python -B \
  studies/neural_response_memory_20260922/check_activation_gelu_panels.py \
  --metrics data/generated/neural_response_memory_20260922/activation_circle_partial_check03/metrics_summary.json \
  --output data/generated/neural_response_memory_20260922/activation_circle_audit_interim01/gelu_rescore_recheck_NEW.json
```

All 42 milestone rows, six primary rows and 42 pairwise order comparisons
match their independently recomputed scalars exactly. All 16 referenced GELU
run archives pass their SHA256 and CRC checks; config, summary, saved data,
query, protocol and case checks also pass. Producer source-hash dictionaries
are consistent across all runs and match the recorded provenance. This audit
does not independently replay physical checkpoints or rehash producer source
files; those checks remain separately scoped.

| GELU task | P1 primary RMS | P2 primary RMS | P3 primary RMS |
|---|---:|---:|---:|
| Two outliers, alternating | 1.439745958626305 | 0.2423888054943654 | 0.02485443211732128 |
| Quadrant, alternating | 5.783894821570329 | 0.6634861734344981 | 0.2601037862958665 |

All 42 shared-loss numerical gates pass. Only the two-outlier P3 primary
comparison meets the frozen RMS `<=0.1` criterion. The other five primary
comparisons exceed it despite passing the numerical checks. Every one of the
42 tested order comparisons resolves improvement with higher order using the
prescribed summed-sensitivity margin; that finite observation is not hierarchy
convergence. The maximum nested-grid change is `1.7763568394002505e-15`, the
maximum closure refinement RMS is `0.0007827452684317953`, and the maximum
dense refinement RMS across milestones is `0.0007815631724932486`. The maximum
actual milestone-MSE relative error is `1.8877233110004e-11`.

This is an interim verification of saved-panel evidence, not a final verdict
for the activation campaign. Physical saved-state replay, repetition checks,
remaining activations and the final authorized campaign inventory remain
pending. No training, GPU use, process signal or frozen-source edit occurred
during the rescore.

## Inputs and remaining work

Complete allowed scientific/source inputs read: the current
`ACTIVATION_CIRCLE_PROTOCOL.md`, `activation_circle_cases.json`,
`ACTIVATION_CIRCLE_DERIVATION.md`, `activation_moment_engine.py`,
`activation_circle_run.py`, `run_activation_circle_campaign.py`,
`test_activation_moment_engine.py`, inherited `deep_moment_engine.py`,
`deep_circle_run.py`, `moment_engine.py`, established `docs/NOTATION.md`, and
`code/pde/finite_network.py`. Required process skills were
`investigate-conjectures` and `solve-math-rigorously`, with the former's
adversarial-audit and decisive-experiments references. No external scientific
claim was needed beyond directly checked formulas in these inputs.

Pending campaign outputs: archive integrity and explicit checkpoint replay,
independent shared-loss/time scoring and gate decisions, one common finest
dense reference, all capped/failure dispositions, and exact repetition checks.
The empirical scientific conclusion is intentionally left open here.
