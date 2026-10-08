# Phase-two approximation and evidence check

2026-10-07. Bounded, scoped check of the completed unequal-residual phase.
This is an internal implementation/evidence check, not an independent promotion
review or a dense-limit theorem. No training run, new cohort, or coefficient fit
was performed. Only this report was written.

The ordered cubic implementation matches the stated tensor formulas and output
derivative. Saved-array recomputation confirms that retaining ordered response
does **not** improve the tested passive prediction. The full causal system's
reported matched-Euler comparisons also reproduce. The main qualifications are
the meaning of the potential model's saved zero area, the distinction between
three different passive decompositions, and the descriptive scope of the
finite-cohort comparisons.

## Inputs and checks

Read ASYMMETRIC_RESPONSE_APPROXIMATION.md, ordered_response_approximation.py,
analyze_response_phase2.py, and, with the supervisor's scope extension,
passive_clock_quadrature.py, dense_response_phase2.py, and
causal_response_phase2.py. Read the saved approximation record and arrays,
analysis/summary.json, and selected raw phase-two trajectories under
data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1/.
The prior scoped inputs CANDIDATE_SYSTEM.md, ANALYTICAL_LEARNING_PROFILES.md,
PASSIVE_CLOCK_CHECK.md, and BEYOND_INITIALIZATION_RESULT.md supply the source
normalizations and phase-one coefficients. No other study was consulted.

Read-only NumPy checks independently recomputed ensemble means, output errors,
source-sum reconstruction, control differences, and the signed area from saved
paths. Explicit index loops were compared with the implementation's tensor
contractions. These checks loaded saved data and evaluated algebraic formulas;
they did not integrate a new training trajectory. The underlying full population
simulator was not re-audited internally in this check.

The supervisor subsequently added UNEQUAL_RESIDUALS_RESULT.md to the input
scope. Its full draft was read and its numerical tables were checked against
the same saved evidence. A missing plus sign between the two terms of its
first-layer defect-velocity formula was reported for correction. Its source,
gate, seed-count, and comparison qualifications otherwise agree with this
check. The separate instrumentation report and its additional tiny tests were
not inputs to this audit and were not independently repeated here.

## Tensor indexing and the six-state derivative

The approximation uses panel indices \(a,q\in\{1,2,3\}\), training indices
\(j,b\in\{1,2\}\), residuals \(c_b=y_b-f_b\), accumulated residuals
\(u_b=\int_0^t c_b\), and ordered integrals
\(I_{jb}=\int_0^t c_j u_b\). The first index j is the current hidden write;
the second b identifies the earlier readout write. Its saved tensors have shape
\((3,3,2,2)\), with the code order

\[
\texttt{m1[a,q,j,b]}=M^1_{aq;jb},\qquad
\texttt{m2[a,q,j,b]}=M^2_{aq;jb}.
\]

The Gaussian integrator's fourth moment has this same ordering:
\(\mathbb E[g(Z_a)T(Z_q)g(Z_j)T(Z_b)]\), where \(T=\tanh\) and
\(g=T'\). Its transpose after reshape places the initial feature index q
before the training write indices. The lower gate-feature array has ordering
\(\mathbb E[g(X_a)g(X_j)H_cH_d]\), with \(H_c=T(X_c)\).
Thus the m1 contraction with its q slice and the two m2 reaction indices
implement equations (7)--(8) of the analytical note. The response arrays also
handle \(a=q\) by adding both derivative terms; they do not overwrite one.

Let \(J_{qjb}=\int_0^t c_qI_{jb}\). The retained cubic output functional is

\[
f_a=\sum_{q\le2}C^{2,0}_{aq}u_q
+\sum_{q,j,b\le2}u_q I_{jb}M^2_{aq;jb}
+\sum_{q,j,b\le2}M^2_{qa;jb}J_{qjb}.
\]

Here equality refers to this truncated model. Differentiating its middle term
gives \(c_qI_{jb}M^2_{aq;jb}+u_qc_ju_bM^2_{aq;jb}\), while differentiating
the last gives \(M^2_{qa;jb}c_qI_{jb}\). Relabeling the current driving index
in the second middle contribution yields

\[
\dot f_a=\sum_{q\le2}c_q\left[
C^{2,0}_{aq}
+\sum_{j,b\le2}I_{jb}(M^2_{aq;jb}+M^2_{qa;jb})
+\sum_{d,b\le2}u_du_bM^2_{ad;qb}\right].
\]

This is exactly response_kernel(), including its last
\(\texttt{einsum('d,b,adqb->aq',...)}\). The transposes in the Gram and
potential functions swap only a and q; they preserve the write order j,b.
At a nonzero test state \(u=(0.17,-0.12)\), \(\mathcal A=0.07\), explicit
index loops and the tensor contractions agreed exactly in floating-point
arithmetic for both the response kernel and the potential output.

The integrated state is \((u_1,u_2,\mathcal A,f_1,f_2,f_3)\). Residuals use
only state entries for \(f_1,f_2\); the passive output supplies no force.
The code reconstructs
\(I_{12}=(u_1u_2+\mathcal A)/2\) and
\(I_{21}=(u_1u_2-\mathcal A)/2\), consistently with
\(\dot{\mathcal A}=c_1u_2-c_2u_1\).

The stored training-tensor discrepancy is \(5.55\,10^{-17}\), and the
training-kernel identity discrepancy is \(8.33\,10^{-17}\). These check the
stated sparse training tensor and its reduction; they are algebraic consistency
checks, not evidence of accuracy at moderate labels. The smaller potential and
the ordered model share the cubic small-label expansion for the constant-label,
orthogonal-input setup. The ordered model retains selected higher-order effects
after closing the residual; it is not a complete fifth-order label expansion.

## Coefficient provenance and numerical resolution

The coefficient routine reads no trained data. It calls only deterministic
Gaussian rules and moment integrators before solving either approximation.
Saved coefficients are therefore initialization-derived and unfitted. Inspection
of the imported helper confirms that its moment routines do not read trajectories.
The current approximation script and helper hashes both match record.json:

- ordered_response_approximation.py:
  f8f8f8bf295e93ca04a64052752a004a0f092fca608398194894d26accc2eab3.
- passive_clock_quadrature.py:
  a3b47d2fd026c45ca4b00e4c8006ffe332aa04c3c28ea10cf0760fa741d8feb1.

The saved constants are
\(\nu=0.236450410504\), \(\lambda=0.080246070909\), and
\(\mu=0.191482884135\). The independent training expression gives
\(2(\lambda+\mu)/3=0.181152636696\), matching the earlier symmetric cubic.

Orders 40, 64, and 96 were computed, followed by a rotated order-96 rule.
The recorded maximum 64-to-96 changes are \(3.93\,10^{-7}\) for M1 and
\(1.43\,10^{-7}\) for M2 and the constants; the largest recorded rotation
change is \(4.24\,10^{-9}\). These are convergence diagnostics, not rigorous
error bounds. The phase-two script does not impose the earlier phase-one
\(10^{-7}\) target freeze gate, so its result must not inherit that earlier
PASS statement. Saved ODE tolerance refinements change outputs by at most
\(2.30\,10^{-11}\) for the potential and \(1.20\,10^{-11}\) for the ordered
model, separating solver tolerance from the much larger model discrepancy.

## Predictions and full-system comparisons reproduce

For case A, the training inputs are orthogonal, the labels are (0.6, -0.3),
and the passive input is \((2e_1+e_2)/\sqrt5\). Recomputing from the saved
three width-1024 dense RK4 trajectories and both approximation arrays gives:

| Quantity | Dense RK4 mean | Potential | Ordered |
|---|---:|---:|---:|
| Passive output at time 24 | 0.482637079154 | 0.448760060938 | 0.447235876494 |
| Maximum passive error against dense mean on the saved grid | — | 0.033964561309 | 0.035401202659 |
| Maximum error across both training outputs and saved times | — | 0.010855219755 | 0.013111362444 |

The ordered model has slightly larger observed errors in both columns. Its
endpoint training residuals are smaller, which does not establish better
trajectory or passive accuracy. The statement that ordered cubic response
fails to repair passive prediction is supported by these arrays.

For the full causal solver, the comparison uses three dense width-1024 and
three population-size-4096 trajectories per case, all on the Euler step-0.4
mesh. Maximum discrepancies compare the two ensemble means over the entire
saved grid and all three outputs. The dense reference variability statistic
averages the three pairwise dense grid-supremum discrepancies:

| Case | Maximum mean-output discrepancy | Mean pairwise dense discrepancy |
|---|---:|---:|
| A | 0.005173531403 | 0.013066909231 |
| B | 0.005485750814 | 0.016889459214 |

Both rows reproduce exactly from the saved trajectories. These are different
descriptive statistics; the inequality between their values is not a
probabilistic guarantee or a confidence statement. Case B has training inputs
\(e_1\) and \(0.6e_1+0.8e_2\). Its full continuum-approximation claim must
also distinguish Euler from RK4: its mean final signed area is 0.067136 in
dense Euler and 0.028634 in dense RK4. The matched-Euler comparison is the
supported common-discretization claim.

The zero excess in the saved empirical envelope includes three combined run
standard errors, the observed population-size change, and the observed dense
RK4 width change. The width term is not an Euler width extrapolation. With two
or three seeds these terms do not provide simultaneous coverage or certify
unknown systematic bias. The labels remain exploratory instances outside any
certified use of the conservative original label cap.

## Source attribution and ablations measure different things

For each geometry the dense code solves
\(v_3=\alpha_1v_1+\alpha_2v_2\). Thus
\(\alpha=(2,1)/\sqrt5\) in A, but
\(\alpha=(0.559016994375,0.559016994375)\) in B. Define
\(q_2=h_{2,3}-\alpha_1h_{2,1}-\alpha_2h_{2,2}\) and
\(\varepsilon=f_3-\alpha_1f_1-\alpha_2f_2\).

The three entries of source_integrals integrate the readout, middle-weight,
and lower-feature contributions to \(\dot\varepsilon\), respectively.
Their endpoint means are:

| Cohort | Readout | Middle writes | Lower motion | Sum |
|---|---:|---:|---:|---:|
| A, full, width 1024, three seeds | 0.024590 | 0.015273 | 0.040291 | 0.080154 |
| B, full, width 1024, three seeds | 0.020705 | 0.015313 | 0.031598 | 0.067617 |
| Symmetric full, width 512, two seeds | 0.030746 | 0.014777 | 0.040183 | 0.085706 |
| Symmetric frozen middle, same two seeds | 0.031178 | 0 | 0.052304 | 0.083482 |
| Symmetric anchored affine, same two seeds | 0.018086 | 0.007392 | 0.021760 | 0.047238 |

For the A/B RK4 trajectories checked directly, the source sum reconstructs
\(\varepsilon\) within \(4.07\,10^{-9}\). The overall saved campaign maximum
is \(8.82\,10^{-9}\). Source integration uses the same RK stages as the
network. Euler source integrals do not obey the continuous product rule exactly
and are correctly excluded from this attribution claim.
Each of the three integrated endpoint sources is positive in every checked
A/B seed, as stated in the main report. This describes endpoint integrals,
not a claim that every instantaneous rate is positive.

Three array meanings must remain distinct:

- initial_readout_integral integrates
  \(\langle\dot w,q_2(0)\rangle_n\), so it represents the inherited-defect
  projection \(\langle w(t),q_2(0)\rangle_n\), up to integration error.
- passive_split contains
  \(\langle w,h_{2,3}(0)\rangle_n\) and
  \(\langle w,h_{2,3}(t)-h_{2,3}(0)\rangle_n\). It sums to the entire
  passive output f3, not to \(\varepsilon\); reconstruction errors in the
  checked A/B arrays are below \(9\,10^{-16}\).
- gate_drift_integrals substitutes only
  \(g(z_{2,a}(t))-g(z_{2,a}(0))\) for the upper gate in the actual middle
  and lower source terms. It is a partition of those terms on the full
  trajectory. It is not the total influence of changing gates, and it is
  not the full-minus-affine intervention difference.

For the symmetric two-seed controls, full-minus-frozen-middle passive output
is 0.002240680195, whereas the full-trajectory middle source is 0.014777486578.
The frozen-middle lower source increases to 0.052304006094. These observations
support redistribution of learning between blocks and directly show why the
middle-source integral must not be called the effect of deleting middle
learning. Full-minus-affine output is 0.038467296070, while the two full-path
upper-gate-drift integrals sum to 0.017741572443. They are different quantities.

For B's reciprocal deletion, the saved three-seed full causal passive mean is
0.234898869733 and the two-seed no-reciprocal mean is 0.201302051582. If a
paired ablation contrast is desired, restrict the full cohort to the same two
seeds: its mean is 0.235515878605 and the paired difference is 0.034213827023.
Use the correct cohort size when describing the comparison. This is a
counterfactual causal-law comparison, not one more additive source of the
unchanged full trajectory or a dense gradient-model identity.

## One misleading interpretation to avoid in the approximation arrays

potential.npz stores area identically zero because its observables use the
radial substitution \(I=uu^\top/2\). Its actual residual path can turn.
Integrating \(c_1u_2-c_2u_1\) by the trapezoidal rule on that saved path gives
approximately -0.231465, whereas its saved area column is zero. The same
read-only calculation for the ordered path gives -0.172870902, agreeing with
its evolved area -0.172870903 at the accuracy of the saved-grid quadrature.
Therefore the potential model's zero column is an imposed reconstruction
convention, not evidence that its residual trajectory has zero signed area.

No material tensor-indexing or output-derivative error was found. The evidence
supports the stated negative approximation result and the qualified full-system
comparisons. It does not certify the global original-scope guarantee, a
controlled moderate-amplitude truncation error, or superiority of the ordered
approximation.
