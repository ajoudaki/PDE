# Independent bounded solver identity and code audit

Date: 2026-09-12. This is an internal code/scientific identity check, not a
promotion review, an empirical convergence study, or a population-accuracy
certificate.

The inspected recurrence agrees with the supplied candidate specification and
the frozen-coordinate algebra of C.4.7.N2–N8. Independent finite-program checks
passed. Three actionable checkpoint/reporting findings were communicated and
corrected during the audit. The remaining qualifications concern the empirical
process, numerical/environment limits, and the scope of the tests; they are
not resolved by a code pass.

## Scope and versions

The complete assigned inputs were `directional_solver_spec.md`,
`directional_solver.py`, `test_directional_solver.py`, `validation_plan.md`,
`run_validation.py`, and `validation_cases.json`, all in this study. Scientific
inputs were exactly `docs/global_nonlinear.md:9351–9471` and
`docs/special_data_limits.md:3850–4070`. The solve-math-rigorously skill was read.
No other study, theory report, implementation note, run directory, or prior
review was used. A narrowly scoped subagent independently examined only
checkpoint/cost/driver code and its specification. It ran no trajectories.

The initial implementation freeze was
`91ad237f17cc815afe78bdc8bdbf12ba12f1a24056292fb0f6c9af9021b3f4b5`.
The initial independent results retain this hash in
`data/generated/population_flow_computation/solver_code_check/initial_freeze_results.json`.

After the supervisor corrected the RNG-name validation, the final inspected
solver hash became
`eef9c3b2d039d1911d036c068ef52708681f921961d21c73e2b5c999fc9dee23`.
Only checkpoint loading changed in that solver revision. The corrected driver
hash is
`81c086b95fe4d25817031e1a06818a0b35317db9e045b53854e6730f845206c4`.
Touched portions were reread, the independent algebra checks were extended and
rerun, and the corrected error paths were exercised without training steps.

The supervisor also requested rereading amended validation metadata. That
amendment embeds numerical outcomes in the plan; those outcomes were excluded
from this audit's reasoning. The amended count budget was checked statically:
nine main configurations plus three implementation trajectories give twelve
trajectories and 2490 training calls. This audit itself ran **zero initialized
training trajectories** and inspected no main-run numerical evidence.

## Model and directional identities

The implementation uses separate lower and upper statistical populations,
initializes `w=g`, `c=0`, and zero coordinate tangents, and retains rank-update
histories rather than a trainable representative-by-representative connector.
For each active node, `gamma=-2*h*p*(prediction-label)` is exactly the coefficient
in N2. All right sides use the preceding state; `w`, `c` and their tangents are
committed together. The old rank updates contribute `gamma_old*HH` to the forward
coefficient and `gamma_old*DD` to the old reverse coefficient, with no current
rank-update term in the reverse block. Current forward calls precede the
reverse calls, as required by N5–N6. The signs, factor 2, mass, step size, and
old/current placement agree with those equations.

Let a fixed named-source coordinate expression be \(F(z)\), with all empirical
coefficients frozen. Set \(R_i=\epsilon_i/\sqrt{\omega_i}\), where the signs are
independent and \(\omega_i=h p_i>0\). Its directional derivative is

\[
\dot F=\sum_j R_j\partial_jF,
\qquad
\mathbb E_\epsilon[\omega_iR_i\dot F]
=\sum_j\sqrt{\omega_i/\omega_j}\,
\mathbb E[\epsilon_i\epsilon_j]\partial_jF
=\partial_iF.
\]

This identity applies pointwise at fixed sources when the expression and its
coefficients do not depend on the probe signs. It justifies the weighted dual
probe and the coordinate-tangent formulas. It does **not** make the finite
feedback implementation's response estimates unbiased: its realized empirical
coefficients depend on previous probes and representatives. The specification
correctly states that distinction.

The current direct upper tangent is removed before estimating old beta:

\[
\dot D_{\rm old}=v_c\phi'(Z)+c\phi''(Z)(\dot D_{\rm history}F).
\]

The remaining current response is the analytic diagonal
\(\beta_{ka,kb}=\mathbf1_{a=b}\,\mathrm{mean}[c\phi''(Z_a)]\).
This retains separate formal source names even for duplicate clean inputs.
The lower and upper propagated tangents implement N7 and N8 with coefficients,
residuals and covariance construction frozen. In particular the code does not
differentiate the conditional innovation representation when taking formal
named-source derivatives. That agrees with III.F.9–10.

The independent tanh test supplies a two-stage, two-direction frozen graph
with a nonzero supplied interior readout, two old and two current sources per
orientation, unequal weights, duplicate directions, three fixed source/root
tuples, and all \(2^8=256\) probe-sign vectors. The nonzero supplied readout
makes both forward and reverse reuse terms nontrivial; it is a local algebra
fixture, not a trajectory from the model's zero-readout initialization.
Full named-source Jacobians were derived independently. A separate complex-step
evaluation of the complete frozen graph checked both final tangents. Current
plus signs were then deliberately aliased to old signs as an algebra stress
test: pointwise current-source removal left the physical proposal and lower
tangent exactly unchanged. No independence claim is made for that adversarial
test input.

Results: weighted alpha error at most \(6.91\times10^{-16}\), weighted old-beta
error \(3.13\times10^{-16}\), model-update errors at most
\(5.56\times10^{-17}\), and full-graph tangent errors at most
\(1.12\times10^{-16}\). These are floating-point checks of finite identities.

## Sources, causality and passive observations

For fixed field arrays, covariance extension uses the uncentered Gram and
preserves every old factor block. If \(L L^T=G_{\rm old}+s^2I\), the new lower
factor block is \(V^T\), where \(LV=B\). Consequently the source construction
is the required prefix of \(E L_{\rm extended}^T\). The independent test compared
this incremental construction against a fresh dense Cholesky factorization
of the full fixed Gram, including singular clean forward Grams, and checked
eight old history/factor prefixes byte-for-byte.

The exact Schur floor follows from positivity of the empirical Gram: replacing
the old block by its ridge-augmented block cannot make the residual clean
Gram negative. Adding the independent new \(s^2 I\) therefore gives a Schur
complement at least \(s^2I\) in exact arithmetic. The implementation checks a
roundoff allowance and positive definiteness and adds no silent jitter.

Five separate generators create lower roots and the two innovation/probe
orientations. The empirical factors and responses nevertheless couple the
realized populations. For adaptively random empirical factors, a stored
factorization is an algebraic construction, not proof that the full finite
transcript has the exact Gaussian conditional law of the deterministic
population source program. No finite-sample iid assertion is justified here.

Clean passive forward queries correctly use no new \(s^2I\) on their own
diagonal. For training covariance \(C=H^TH/P+s^2I\) and passive cross matrix
\(B=H^Th/P\), the mean is \(B_{\rm plus}C^{-1}B\) and the conditional covariance
is \(h^Th/P-B^TC^{-1}B\). The code's innovation-factor representation is
algebraically equal to these dense formulas. Initial and current lower
features use the same saved root tuple. Their joint source covariance is
computed together, the initial correction is zero, and the current correction
is retained. Identical fields share a clean action by deduplication. The
one-dimensional Gauss–Hermite predictor has an explicit finite order and does
not mutate training state or consume training randomness.

The reverse passive query uses the same sampled current upper activation to
form \(D=c\phi'(Z)\). Its covariance is conditioned against the stored minus
history, its old response uses the old-source tangent, and its fresh current
response is exactly one diagonal contribution \(h_a\mathrm{mean}[c\phi''(Z_a)]\).
The initial passive forward slots contribute no derivative to the current
readout expression. Initial \(D,Q\) are identically zero for the model's
zero initial readout; the returned nonzero `upper_D` and `lower_Q` are current
observations on their separate populations.

Independent checks compared the passive means and full initial/current joint
covariance with dense conditional-normal formulas. A controlled fresh-query
fixture then set reverse innovations to zero and repeated fixed plus draws
over all signs. Full analytic old-source Jacobians gave an independent exact
reverse conditional-mean oracle. Its \(Q\) discrepancy was at most
\(4.58\times10^{-16}\); \(D\) agreed exactly. Duplicate directions produced
bitwise equal initial/current preactivations and \(D,Q\) columns. State arrays
and all training RNG states were unchanged after ordinary passive queries.

The polynomial check independently verifies Gaussian Stein identities for
correlated and singular covariance matrices using degree-exact order-five
Gaussian quadrature. For a reused action, take \(Wg=\xi\),
\(u=\xi^2+a\xi\), \(W^*u=\zeta+ag=q\), and \(h=q^2+bq\). Then

\[
\mathbb E[u']=a,\quad
\mathbb E[\partial_\zeta h]=b,\quad
\mathbb E[h g]=ab,\quad
\mathbb E[h^2]=3(3+2a^2)^2+b^2(3+2a^2),
\]

so the reused forward response is \(Wh=\xi_h+b u\). These derivative and
covariance identities were checked at \(a=.6,b=-.7\), with maximum discrepancy
\(7.82\times10^{-14}\). This polynomial fixture checks the finite source
algebra; it does not invoke a global theorem for unbounded nonlinearities.

## Restart completeness and corrections

Ordinary checkpoints contain all 26 persistent arrays, the complete law and
precision configuration, the physical step count, and all five RNG states.
They include roots, current coordinates/tangents, ten full histories, both
covariance factors, masses and update coefficients. Derived law arrays are
reconstructed from the saved configuration. A failed prepared step restores
RNG states and commits no array update. Nothing needed to continue the finite
recurrence is intentionally compressed away.

The existing test source contains a split/uninterrupted trajectory comparison;
it was read but not rerun and its external results were not inspected. This
independent audit instead serialized the supplied synthetic state, compared
all 26 arrays bitwise, compared all five saved RNG states, and verified the
next seven draws in every stream. This demonstrates the serialization path
on that complete state; it is not an independent rerun of the trajectory test.

The original loader accepted a checkpoint whose `rng_state` dictionary omitted
a required stream, leaving that stream at its constructor state. That was a
malformed-file robustness defect, not a missing field in ordinary saved files.
The revised loader requires exactly the five stream names. Independently
constructed missing-key and extra-key checkpoint copies are now rejected;
the intact checkpoint preserves all RNG states.

The driver originally omitted an elapsed-budget skip from saved `outcomes.json`
because it appended the record and broke before writing. The corrected path
was independently exercised with a controlled clock that expired before the
first case: it writes the skipped record and returns failure without creating
a solver trajectory.

The driver originally measured per-case wall time/RSS before reading the whole
checkpoint for hashing. It now hashes in 1 MiB chunks before sampling those
measurements. Its streaming digest was checked against a direct digest of the
synthetic checkpoint. These fixes do not retrospectively change measurements
in old run artifacts. The standalone solver CLI still performs its final
whole-file hash after evaluating its wall-time field; that limitation does not
affect the corrected validation driver.

## Actual cost and remaining limits

Write \(P\) for each population size, \(N\) for physical steps, \(m\) for active
directions, \(J=mN\), and \(b\in\{4,8\}\) for scalar bytes. Including triangular
solves, covariance work, whole-history copying and finiteness scans, a step
with \(j\) old calls costs

\[
O(Pjm+Pm^2+j^2m+jm^2+m^3+Pj+j^2).
\]

Summed over steps, this is \(O(PJ^2+J^3)\), as specified. A passive prediction
at \(M\) directions and order \(q\) costs
\(O(PJM+J^2M+PqM)\), apart from constructing the quadrature rule. Full diagnostic
Gram and factor reconstruction adds \(O(PJ^2+J^3)\) per invocation; the supplied
driver uses it at case completion. Paired queries additionally retain
\(O(\text{draws}\,P M)\) arrays and factor \(O(M)\)-sized query covariances. With
the fixed query counts in the driver they do not change trajectory order.

The exact persistent array payload is

\[
b(10PJ+2J^2+8P+6J)+8J+40N.
\]

Derived law arrays add \(4bm\) bytes. Array headers, JSON/configuration objects,
BLAS workspace, simultaneous old/new arrays and query buffers are additional.
For the largest amended configuration \(P=4096,N=256,m=2,b=8\), persistent arrays
alone occupy 172,267,520 bytes (164.287 MiB). This is a schema calculation,
not a measured peak RSS. Frequent retained checkpoints can make aggregate disk
usage \(O(PJ^2+J^3)\), despite \(O(PJ+J^2)\) resident state.

The following limits remain:

- Time checks occur between calls and cannot interrupt a large step, query,
  diagnostic or save. A hard wall-time or memory guarantee is not implemented.
  Thread settings are recorded, rather than enforced, by the driver.
- `ru_maxrss` is a cumulative process high-water mark across cases. It is not
  an isolated per-case peak. Corrected hashing removes one undercounted phase
  but does not change that interpretation.
- On a numerical failure, the driver saves the last complete checkpoint and
  failure text but can skip the full diagnostics JSON. History-based
  diagnostics can be recovered from that checkpoint.
- Library versions are recorded but not checked on load. Structural restart
  completeness is not a guarantee of bitwise equality across numerical
  environments. Validation checks shape, precision, finiteness, triangularity
  and bookkeeping; it is not a cryptographic or full algebraic consistency
  check of arbitrary checkpoint contents.
- A positive noise level defines the stated noisy empirical process. Neither
  the fixed-program source theorem nor the sign identity supplies convergence
  of that process as \(P\to\infty\), \(h\to0\), or \(s\to0\), a simultaneous
  refinement theorem, uniform time/whole-circle error, or a useful accuracy
  bound at physical time 40. Finite quadrature and joint-query sampling add
  their own uncertified errors.

Executable audit fixtures and measured errors are in
`data/generated/population_flow_computation/solver_code_check/`:
`check_frozen_program.py`, `initial_freeze_results.json`, `results.json`,
`check_reporting_fixes.py`, and `reporting_fix_results.json`. The fixtures use
256 sign vectors, at most 768 array rows, small exact polynomial quadrature,
and no initialized training trajectories. A successful code audit therefore
supports the finite recurrence implementation, and nothing stronger.
