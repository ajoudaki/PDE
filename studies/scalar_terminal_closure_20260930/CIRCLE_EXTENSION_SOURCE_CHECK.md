# Internal source check of supplemental endpoint continuation

Date: 2026-09-30.

Verdict: **PASS for the admitted continuation of the original validated
coarse/fine pair.** The final source restores the complete states, preserves
the original physical-time history and handoffs, continues the same RK4
systems, and reconstructs the same scalar/Fourier observer at the new
endpoint. The previously identified refined-selection eligibility edge
is now explicitly rejected before training. No mathematical correction
remains for the admitted path.

This is a source audit, not a claim that the supplemental experiment has
run, fitted, or passed its numerical sensitivity gates. No training or
validation program was launched by this checker. Only this report was
written; no producer, plan, input, or running process was changed.

## Frozen inputs and scope

The complete final `extend_circle_experiment.py` was read. Its SHA256 is

`57d0aa355b9dbde474168a88bd0a02d3e4c1ea6795837c66fce8720f55f4c16c`.

The complete `CIRCLE_ENDPOINT_EXTENSION_PLAN.md` was read, SHA256

`b46eae6b10def119e39616c38c325a2ffd36c8a794f4c104abb0864ed930a560`.

The allowed dependency is the previously read and checked complete frozen
producer in `data/generated/scalar_terminal_closure_20260930/circle_width1024_02/`,
SHA256

`f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba`.

That producer's digest was reverified during this check. The supplemental
source also verifies it at runtime before importing any model routines.
Shared instructions and the previously read `solve-math-rigorously` skill
apply. No other study, research route, new empirical outcome, or external
source was read. The author coordinated a final source freeze before this
verdict.

## Restoration, model identity, and absolute time

`load_states` reconstructs the dense state in the original order
\((A,W,w)\), and the q=1 state in the order
\((A,w,V,K,\tau)\). It copies each array from the saved endpoint and
checks every state block for finiteness and the activity clock for
positivity. The fixed q=1 mixer is loaded from the original
`initialization.npz`; the dense model uses its saved current middle matrix.
There is no reinitialization or resampling.

The final `task_arrays` function accepts either the stored \(8\times2\)
input layout or the producer's \(2\times8\) column-sample layout and
requires the final shapes \((2,8)\) and \((8,)\) for inputs and labels.
It does not apply any further normalization. Before advancing, `resume_case`
recomputes both training losses from the restored states and checks them
against the saved last losses; it also compares the complete q=1 residual
vector to the saved last residual.

`advance_pair` invokes the frozen producer's `velocity` and `rk4` functions
without changing their arguments, signs, mobilities, or factors. Dense and
q=1 are independent systems; computing their proposed steps sequentially
does not couple their states. The full pair is accepted only after both
proposed states and losses pass their checks and the guard still permits
continuation. An interruption while computing the second proposed model
does not advance the saved first model alone.

If the saved endpoint is \(t_0\), the new accepted times are
\(t_0+jh\), \(j=1,2,\ldots\), using the original \(h\in\{1/8,1/16\}\).
The saved endpoint is not duplicated or advanced twice. The target duration
must be a nonnegative integer number of those steps. These dyadic step
sizes and original endpoints give exact binary compatibility for the common
physical-time comparison.

The original time, dense-loss, q=1-loss, and q=1-residual arrays are copied
into lists and new observations appended. Their original prefixes are not
recomputed or altered. New endpoint query arrays replace endpoint arrays
only in the fresh supplemental copy; the original run remains the source
of the original comparison.

## Eligibility, stopping rules, and sensitivity

Normal training mode requires an original `results.json` marked complete
with the five prescribed task names. Eligibility depends only on the
selected original full-model losses exceeding \(10^{-6}\) and the
original numerical refinement gate having passed. It does not select
tasks by scalar imitation error or query appearance.

An important edge in the earlier version was that an original
`selected='refined'` task could be eligible even though its original
coarse/fine pair had failed. The final source checks this before output
creation and training: any unfitted, passed-refinement task whose selected
resolution is not `fine` is rejected. This accurately limits the current
implementation to the original validated \(1/8\)-versus-\(1/16\) pair.
It does not silently resume a previously rejected pair or claim generic
support for a \(1/32\) selection.

The coarse continuation stops at its first accepted time when both losses
are at most \(10^{-7}\), or at physical time 1024. The check at the next
loop entrance stops before another step, so the returned endpoint is that
first qualifying accepted time. The fine continuation is then required to
reach the identical coarse-selected time; it does not stop early on its
own fitting threshold. Both coarse and fine summary `fitted` flags require
their two final losses to be at most \(10^{-6}\).

The supplemental comparison calls the frozen producer's refinement
function on the completed same-time pair. It retains the existing dense,
q=1, and primary-scalar endpoint RMS thresholds and the dense/q=1 common-
time loss thresholds. The complete historical curves are supplied, so
the sensitivity check includes the original prefix and the extension.
There is no further step refinement or horizon extension.

The source saves the returned sensitivity result even if it fails. Its
`supplemental_completed` status means that the computations completed;
it is not an accuracy verdict. Reporting a fitted, numerically validated
endpoint still requires both the selected full-model fitting test and
the sensitivity gate to pass. A completed run at time 1024 can remain an
unresolved fit, and the report must say so.

## Original handoffs and scalar/Fourier reconstruction

Each resolution's original handoff files are copied unchanged. No new
handoff is captured, no response coefficient is recomputed at the new
endpoint, and no additional Fourier mode is introduced.

For each original handoff, `guarded_scalar` solves the same system from
its original handoff time through the extended endpoint:

\[
\dot r=-Cr+\|r\|_2b,\qquad
\dot z=r,\qquad\dot s=\|r\|_2,
\]
\[
r(t_h)=r_h,\qquad z(t_h)=0,\quad s(t_h)=0.
\]

It uses DOP853 with the unchanged tolerances \(10^{-10}\) and \(10^{-12}\).
This is full reintegration from the original handoff, not a restart with
the accumulated integrals incorrectly reset at the original endpoint.
The reference history supplies only requested physical observation times;
the scalar right-hand side never reads future full-model residuals.

The original Fourier coefficient matrix is multiplied by
\((1,-z_1,\ldots,-z_m,s)^T\). Thus the readout remains

\[
\widehat f(\theta,t)=f_{0,32}(\theta)
-C_{0,32}(\theta,:)z(t)+b_{0,32}(\theta)s(t).
\]

The untruncated diagnostic panel readout uses the saved original
\(f_0,C_0,b_0\) on that panel. The exact training observer is
\(y+r_h-Cz+bs\); the code correctly compares it with \(y+r(t)\).
Fourier training MSE is separately reconstructed at the original training
angles, and its consistency error is also recorded. Scalar loss remains
\(\|r\|_2^2/m\), so these two losses are not silently conflated.

Dense and q=1 endpoint functions are reevaluated from their new complete
states on the original query grid. The scalar-versus-reference RMS,
maximum, sign, direct-observer, Fourier-error, and static-control metrics
use the appropriate same-time vectors and retain their original formulas.
An empty away-from-boundary mask now yields a null disagreement metric
rather than a NaN serialization failure.

Reintegrating an adaptive ODE to a longer horizon can slightly change
previously sampled scalar values within numerical tolerance. The source
labels its scalar history as reintegrated; it does not claim bitwise
preservation of that history. Original scalar outputs remain available
in the source run and in the retained original comparison. The full-model
loss/residual prefixes are directly preserved.

The scalar state and stored coefficients have not changed: 17 moving
scalars, 712 fixed model numbers, and 729 total under the original counting
convention. Extended reference trajectories and diagnostic output files
are experiment artifacts, not new coordinates of the scalar evaluator.

## Budget, memory, checkpoints, and preservation

The supplemental `Guard` enforces its supplied remaining wall-time
allocation, and in check mode also imposes a 30-second process-CPU limit.
It is called before every full-model RHS evaluation, before acceptance of
a proposed full step, before endpoint evaluations, and within every scalar
RHS evaluation. These checks address the original producer's omission of
deadline checks during scalar analysis.

The guard reads the Linux process high-water RSS through
`resource.getrusage(...).ru_maxrss * 1024` and stops above 4 GiB. This is
the correct unit conversion for the current Linux execution environment.
Every accepted full state and all completed curve arrays are checked for
finiteness. The q=1 clock is also checked positive. The thread-pool context
limits loaded BLAS libraries to two threads, and task/resolution loops
remain sequential.

The program receives a **remaining** allocation; it does not derive that
allocation from elapsed original-run and analysis time, nor subtract the
120-second reserve itself. Its provenance explicitly assigns both
cumulative accounting and the reserve to the caller. Correct invocation
therefore requires a budget no larger than the unspent part of the
original 3600 seconds after all prior work and the reserve. This source
check cannot certify an external caller's accounting. A single already
started numerical/file operation can run until the next guard check;
the reserve must also cover checkpoint writing after a guard exception.

During normal guarded interruption, `resume_case` catches the exception
and saves the last jointly accepted dense/q=1 state, the complete valid
loss/residual history through that time, and an interruption record. The
new full pair is assigned to the accepted variables only after its checks,
so the checkpoint's physical time and both state blocks stay aligned.
An interruption during endpoint/scalar evaluation also retains the valid
full-model endpoint and trajectory, without reporting unfinished scalar
outputs as completed results.

Original input artifacts are copied to a fresh supplemental directory,
hashed, and preserved. Continuations are first written under
`continuation_pending`. A completed same-time pair is then placed in the
supplemental case's main resolution directories, with the original copied
comparison moved under `initial_comparison`. The original source files
are not moved or overwritten. If a normal guarded interruption occurs
before that publication step, the original comparison remains the
reported fallback and the pending partial artifacts remain available.
As with ordinary filesystem operations, this sequence of directory renames
is not a crash-atomic multi-directory transaction; the source original
remains the authoritative recovery copy if an external process kill or
filesystem failure interrupts publication itself.

The JSON writer uses a temporary file followed by replacement, avoiding
partially written result JSON. Copy-stage failure bookkeeping includes
only cases whose original artifact copies completed. Successful scalar
evaluation, a complete same-time pair, and a sensitivity result are
required before the new result replaces the copied original comparison.

## Preflight validation and remaining evidence

The source's `--check` path implements the requested bounded validations:

1. A discarded one-step guarded continuation is compared blockwise with
   a direct call to the frozen producer's RK4 step.
2. Saved-state losses and residuals are reconstructed before any resumed
   step, including in zero-duration continuation.
3. Zero extra duration recomputes all endpoint/scalar arrays and compares
   every original curve array, with a \(10^{-10}\) maximum-error limit.
4. An intentionally expired guard exercises checkpoint creation and
   verifies that the retained full states equal the original accepted
   states.

These checks are appropriate for detecting restoration, time-origin,
integral-reset, and observer-reconstruction mistakes. Their design was
audited here; this checker did not run them or inspect a final frozen-
source validation output. Author-reported success is not substituted for
independently reconstructed supplemental empirical metrics.

Before interpreting supplemental outcomes, independent analysis still
needs to reconstruct saved-state losses, Fourier and direct scalar outputs,
the original-history prefix, unchanged handoff hashes, both time grids,
and coarse/fine sensitivity. The original capped-horizon results and the
supplemental results must be reported separately. The source provides the
needed artifacts; no unobserved fitting or fidelity result is claimed by
this audit.
