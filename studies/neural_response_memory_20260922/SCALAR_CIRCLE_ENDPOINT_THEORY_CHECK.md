# Passive circle predictor: scoped mathematical check

2026-09-25. Read-only scientific check of the assigned equations and frozen
endpoint protocol, followed by this assigned report. No research experiment,
external research, implementation edit or Git mutation was performed. This is
a scoped algebra/protocol check, not a promotion review or an empirical verdict.

## Conclusion and normalization

The passive output formula in SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md is consistent
with the order-four hierarchy. It introduces no feedback from probe inputs and
defines a prediction at every angle wherever the training closure exists. The
finite Fourier construction is an additional, explicitly checked spatial
approximation. The protocol's separate first-loss-crossing endpoints answer a
different question from the completed matched-time trajectory experiment.

Preserve the actual runner normalization: scalar_aggregate_run.py::task_data
returns U=(cos(angle),sin(angle)), and the engine consumes these rows directly.
Its statement U=x/sqrt(d), at d=2, is compatible with original x=sqrt(2)U.
Do not divide these U rows by sqrt(2) again. An earlier conversational suggestion
from this checker to do so was incorrect and is superseded by this source check.

## Exact ordered-integral derivation

Let b,c,d range only over the M training samples and let q denote any passive
input. Write alpha=2/M and z'_b=-alpha(f_b-y_b), with z(0)=0. Under the frozen-Q
closure, the passive equations are

    f'_q   = K_qb z'_b,
    K'_qb  = C_qbc z'_c,
    C'_qbc = Q^0_qbcd z'_d,
    Q'_qbcd = 0.

Repeated training indices are summed. Integrating the third equation gives

    C_qbc = C^0_qbc + Q^0_qbcd z_d.

Define I_bc(0)=0 and I'_bc=z_c z'_b. Substitution and integration in the second
equation give

    K_qb = K^0_qb + C^0_qbc z_c + Q^0_qbcd I_cd.

Define J_bcd(0)=0 and J'_bcd=I_cd z'_b. Integrating the first equation yields

    f_q = f^0_q + K^0_qb z_b + C^0_qbc I_bc + Q^0_qbcd J_bcd.

These identities are exact for the specified truncated system, not for the
untruncated dense network. They contain no factorials. The ordering of c,d is
essential: D_d D_c need not equal D_c D_d. Replacing I_bc by z_b z_c/2 or J_bcd
by z_b z_c z_d/6 is generally invalid. For order two only f^0+K^0 z remains;
for order three one additionally retains C^0 I.

The state (z,I,J), together with the existing training hierarchy, evolves
autonomously from its own residuals. It has M+M^2+M^3 additional moving scalars.
Restarting requires preserving these accumulated scalars as well as the
training state; resetting them to zero would reset the readout history.

## Initialization and no-feedback requirements

For q and b, initialize K_qb=(grad f_q)^T B grad f_b. A rectangular cross-kernel
calculation between probe and training forward/backward fields suffices.
All differentiated directions remain training directions g_c=B grad f_c.
For each ordered training pair c,d, the parameter bi-jet

    theta(s,t)=theta0+s g_c+t g_d+st Dg_c[g_d]

has the cross-kernel mixed coefficient

    D^2 K_qb[g_c,g_d] + DK_qb[Dg_c[g_d]] = D_d D_c K_qb.

Thus the mixed coefficient is precisely Q^0_qbcd. The acceleration term must
be included even though q is passive. No probe direction, probe residual,
probe label, dense endpoint or trained parameter enters this initializer or
the reduced dynamics. Adding probes must not change alpha=2/M or the M training
residuals. Taking q equal to a training input provides a consistency check
against the existing training closure and signature formula.

## Every-angle definition and finite scalar storage

At finite width the initialized functions f^0_q,K^0_qb,C^0_qbc,Q^0_qbcd are
smooth periodic functions of q's angle. Their contraction with a finite
signature defines a smooth periodic passive function. This mathematical
definition alone does not supply exact finite-scalar storage of arbitrary
initialized functions after discarding the dense initializer.

A real Fourier polynomial through mode K supplies that finite representation:
store the constant, cosine and sine coefficients of each initialized scalar
function. The count is (2K+1)(1+M+M^2+M^3) real scalar coefficients, independently
of neural width and the number of later query angles. Fourier projection and
the terminal signature contraction commute by linearity. Runtime evaluation
then requires only scalar contractions and trigonometric functions, with no
neuron fields or network evaluator. The approximation affects the passive
readout only; the original training closure must remain unchanged.

For comparison, a saved grid of N direct probes costs N(1+M+M^2+M^3) scalar
coefficients and specifies only those N probe values without an interpolation
rule. The protocol correctly distinguishes this from the Fourier predictor.
Its on-grid and off-grid final-readout checks test the complete contraction,
which can amplify small coefficient errors through large z,I,J values.
Passing these finite checks is numerical evidence, not a rigorous uniform
bound between all checked angles or a proof of exact continuum compression.

## Endpoint metric and numerical interpretation

The protocol fixes, separately for each model, the first training-MSE crossing
of 1e-6, with an explicit time/resource cap. Comparing the two functions at
their own stopping times is a coherent predeclared endpoint comparison. It
does not choose times to minimize their mutual disagreement. A pair without
two resolved crossings has no qualified matched-loss endpoint verdict.

First crossing is a tolerance-defined stopping convention, not an infinite-time
limit. In particular, the truncated kernel can become indefinite and its loss
need not remain below threshold after a first crossing. Do not infer a stable
or converged learned function from that event alone. The report should retain
the actual stopping times, losses and statuses prescribed by the protocol.

For N uniform angles phi_j=2*pi*j/N, with no duplicated 2*pi endpoint, use

    E_N = sqrt(mean_j((f_scalar(phi_j,T_scalar)
                       - f_dense(phi_j,T_dense))^2)).

For fixed existing endpoints, continuity implies that E_N converges as N grows
to the protocol's normalized full-circle L2 metric. The 512/1024 comparison
and permitted 2048 refinement diagnose quadrature resolution; they are not
certified integration error bounds. The dense endpoint function is the target,
so this measures imitation rather than risk against unknown circle labels.
Relative RMS requires a nonzero dense-function RMS; zero must be represented
as undefined rather than silently divided by zero.

Check integration refinement on endpoint functions at each resolution's own
stopping time, as specified, not just on training outputs at a common time.
Appending passive signatures can change an adaptive integrator's error
weighting although the exact training equations are unchanged. Terminal
contractions can also magnify cancellation. Consequently prior training-path
refinement checks do not establish numerical accuracy of the new endpoint
readouts. The frozen separate integration, Fourier and quadrature checks
address distinct errors and must retain their separate statuses.

The new criterion does not supersede the earlier negative trajectory result;
it evaluates whether the same candidate can approximate a different observable.

## Inputs and scope

Complete assigned scientific sources read: SCALAR_AGGREGATE_CANDIDATE_THEORY.md,
SCALAR_AGGREGATE_RESULTS.md, scalar_aggregate_engine.py,
SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md and scalar_aggregate_run.py. Required process
skill used: solve-math-rigorously. No other study, referenced case file, generated
trajectory, external scientific source or independent review was read. No
numerical test was executed by this checker. Only this assigned report was
written.
