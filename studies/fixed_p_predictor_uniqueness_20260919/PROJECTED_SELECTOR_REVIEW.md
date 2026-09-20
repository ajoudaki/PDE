# Informed internal review of the projected selector

2026-09-19. Reviewer: scoped `natural_constrained_route` agent, after freezing
its own independent candidate. This is an informed internal adversarial check,
not an isolated promotion review.

Reviewed candidate: complete `PROJECTED_SELECTOR_LEAD.md`, final verified SHA-256
`96df35354d2b54f111db6d60bba3b5ebc01b8211d0ab61530cba1ec6118a827d`.
The initial review used frozen hash
`9747a05126057682600652a36c47c17dc9f2f184dc307fd9d9383dbe9b9e5233`;
the complete final revision was reread after the lead corrected the optional
clock statement and clarified the readout/KKT notation. Those changes preserve
the mathematics and close the sole minor clarification raised in this review.
Allowed dependencies read completely: `UNIQUE_NOISY_SELECTOR.md` and
`PASSIVE_LIMITS.md`, together with the previously read complete
`MODEL_AND_GEOMETRY.md` and `CANONICAL_FEATURES.md`. No other study, external
scientific source, experimental output, or unassigned route was consulted.
No candidate file was edited and no experiment was run.

**Verdict: the central theorem passes this internal mathematical check.**
The displayed constants establish global confinement, exact unhalved-loss
dissipation, exponential convergence to a unique physical state, a common
predictor on the full circle, and a nontrivial random state process for every
finite merged sample count. The minor clock clarification raised during review
has been corrected in the final hash. I found no unresolved proof issue in the
candidate as stated.

The theorem is about the explicitly modified optimizer with a fixed, possibly
very unequal layer learning-rate ratio. It does not prove uniqueness for the
canonical physical gradient flow, or for unrestricted gradient noise, or a
strict hidden displacement for every dataset.

## 1. Constants and localization

The input theorem supplies \(\sigma>0\) for the merged data, and
\(\sigma\le\|K_{h_0}\|\le1\). Thus
\(\epsilon=\sigma/8>0\), \(b^2=2/\sigma\), and
\(0<\eta\le\sqrt{\sigma/32}<1\). All conditions on \(\rho\) are finite
and computable from fixed inputs. The prescription using
\((4a_1/d)^2\) and \(2a_3R/d\) indeed makes the two summands defining
\(\ell\) each at most \(d/2\); the other first-line constraints can be
satisfied by taking the corresponding squared lower bounds on \(\rho\).
There is no circular dependence on an unknown reached state.

For \(z=(\sqrt\rho(h-h_0),c)\), the full derivative is

\[
 T_z(v_h,v_c)=\rho^{-1/2}(DA_h[v_h])c+A_hv_c.
\]

On the radius-\(R\) ball, the source's \(C^{1,1}\) estimates give precisely
\(\|T_z\|\le\sqrt{1+a_1^2\|z\|^2/\rho}\) and
\(\operatorname{Lip}(T)\le2a_1/\sqrt\rho+a_3R/\rho=\ell\).
The hidden displacement is at most \(R/\sqrt\rho\le r\), whereas the
source proves positive Gram on the larger radius-\(2r\) ball. Hence
\(T_zT_z^*\succeq K_h\succeq(\sigma/2)I\) throughout the required ball.

In particular \(P_z\) exists and is an orthogonal projection. This is a
projection in the declared fixed weighted coordinates, not in the original
physical state metric; the physical learning-rate interpretation in section 2
of the candidate identifies that distinction correctly.

The radial estimate is valid, including at zero. Away from zero,

\[
 \frac{d}{dt}\|z\|
 \le2\|T_z\||e|+\eta|e|
 \le(2+\eta+2a_1\|z\|/\sqrt\rho)|e|,
\]

because the secondary contribution is
\(-\epsilon\|P_zz\|^2/\|z\|\le0\). At zero, the norm of the velocity
is bounded by the same constant term, so the one-sided version remains valid.
Integration using \(\int_0^t|e(s)|ds\le1/\sigma\) yields the displayed
bound below \(9/\sigma<R=12/\sigma\). This leaves a strict margin for the
first-exit argument. It does not assume confinement before proving it: the
residual estimate and radial bound are used only up to the putative first exit.

The existence argument also works in the infinite-dimensional Hilbert space.
Uniform bounds for \(T\), \(T_zT_z^*\) inverse, and their Lipschitz constants
make the vector field uniformly Lipschitz on the relevant bounded region.
It is bounded there; a finite maximal-time trajectory consequently has a strong
Cauchy endpoint. The hidden endpoint is strictly within the open
positive-Gram neighborhood. At most finitely many prescribed refreshes occur
before a finite time, so continuation also works if the endpoint time is a
refresh. No compactness of a Hilbert-space ball is invoked.

## 2. Full moving-feature chain rule and the loss clock

The projection is onto the kernel of the **full** prediction derivative. It
therefore satisfies

\[
 T_zP_z=0,
 \qquad \dot e=T_z\dot z=-2T_zT_z^*e.
\]

The hidden variation of the features is already included in \(T_z\). The
chain rule differentiates \(f(z(t))\), not the projector; no \(\dot P\)
term is missing. Such a term would arise if one separately prescribed or
transported a moving projected coordinate, which this rule does not do.
The matrix and lower-field adjoints remain the actual adjoints of the
current model, including the genuine middle transpose.

For the unhalved loss \(L=|e|^2\), the exact identity is

\[
 \dot L=-4\|T_z^*e\|^2
       =-4\bigl(\rho^{-1}\|(DA_h[\cdot]c)^*e\|^2
                         +\|A_h^*e\|^2\bigr)
       \le-2\sigma L.
\]

Thus \(L(t)\le e^{-2\sigma t}L(0)\) and
\(|e(t)|\le e^{-\sigma t}\) are correct in the candidate's declared clock.
The positive readout Gram alone gives this lower bound; it does not require a
positive hidden Jacobian contribution. The factor of two in the vector field
has not been lost.

**Clock clarification, resolved in the final revision.** Multiplying the entire
vector field by \(\rho\) gives path equivalence under the time change
\(\widetilde z(t)=z(\rho t)\) only when the forcing is also changed to
\(\widetilde U_t=U_{\rho t}\). A held-direction refresh interval \(\Delta\)
then becomes \(\Delta/\rho\). Keeping the original forcing schedule while
multiplying the drift is a different pathwise process. The common-endpoint
result remains true for either allowed schedule; this is a clarification of
path equivalence, not a defect in the principal theorem or its time bounds.
The final candidate explicitly reparameterizes both forcing and refresh
interval, so this issue is closed.

## 3. Selected target and the normal/tangent estimates

The target argument in `UNIQUE_NOISY_SELECTOR.md` uses strong convexity of
\(J(h)+\rho\|h-h_0\|^2/2\) only in the radius-\(r\) hidden ball. Its
proof works verbatim when the specified \(\rho\) is replaced by any larger
one. The midpoint inequality makes a minimizing sequence strongly Cauchy;
continuity and completeness prove attainment without weak compactness.
Boundary energy exceeds the feasible initial-hidden energy, proving
interiority. Therefore the target and its stationarity relation are established
independently of the flow.

The minimum-norm readout decomposition then gives

\[
 \|z_*\|^2\le2J(h_0)\le1/\sigma,
 \qquad z_*=-T_{z_*}^*\lambda_*,
 \qquad \lambda_*=-K_{h_*}^{-1}Y.
\]

The signs in this relation are consistent: the hidden stationarity equation
is \(\rho(h_*-h_0)-(DA_{h_*}[\cdot]c_*)^*K_{h_*}^{-1}Y=0\).
No hidden endpoint is supplied to the update rule.

For \(\delta=z-z_*\), write \(d=\|\delta\|\). Integrating the Lipschitz
Jacobian along the connecting segment proves
\(T_z\delta=e+v\), \(|v|\le\ell d^2/2\). Both endpoints and the segment
lie in the same convex ball. The right-inverse norm is at most
\(b=\sqrt{2/\sigma}\), so

\[
 \|(I-P_z)\delta\|\le b|e|+b\ell R d\le b|e|+d/4.
\]

Squaring with \((a+b)^2\le2a^2+2b^2\) gives exactly
\(\|P_z\delta\|^2\ge7d^2/8-2b^2|e|^2\).
Meanwhile

\[
 \|P_zz_*\|\le\ell|\lambda_*|d\le d/8
\]

because \(\ell\le\sigma/16\) and \(|\lambda_*|\le2/\sigma\).
Thus \(\langle\delta,P_zz\rangle\ge3d^2/4-2b^2|e|^2\), with no sign
assumption hidden in the estimate.

The remaining three coefficients sum as follows:

\[
 \tfrac12(d^2)'
 \le(-3\epsilon/4+\ell+\epsilon/8)d^2
   +(-2+2\epsilon b^2+2\eta^2/\epsilon)|e|^2.
\]

The stipulated bounds give respectively at most \(-\epsilon/2\) and
\(-1\), since
\(\ell\le\epsilon/8\), \(2\epsilon b^2=1/2\), and
\(2\eta^2/\epsilon\le1/2\). This checks the decisive estimate (11),
including the noise allowance. The use of \(|e|\le1\) in the curvature
term is licensed by the prior loss dissipation proof.

## 4. Physical coercivity, predictor convergence, and finite travel

The fixed-target potential is an ordinary squared norm with a fixed positive
weight:

\[
 \Psi=\tfrac12\bigl(\rho\|h-h_*\|^2+\|c-c_*\|^2\bigr).
\]

Since \(\rho\ge1\), it dominates half the squared physical Hilbert state
distance. The metric does not degenerate in time or become blind to readout
null directions. Estimate (11) yields
\(\dot\Psi\le-\epsilon\Psi-|e|^2\), so the slightly weaker displayed
\(\dot\Psi\le-\epsilon\Psi\) and rate
\(d(t)\le e^{-\epsilon t/2}\|z_*\|\) are correct.
The bound \(L\le D^2d^2=2D^2\Psi\) follows by integrating the derivative
on the connecting segment. It concerns the actual unhalved loss.

The passive dependency's estimate (3) is sufficient to turn this strong
physical state convergence into uniform predictor convergence on every
bounded query set. The physical quadratic product norm here and the sum norm
there differ by fixed finite factors. That dependency explicitly distinguishes
per-run convergence from a common endpoint; the latter is supplied here by the
same deterministic \(z_*\) for every forcing path. The argument does not
infer cross-path agreement from training-point agreement or a finite mesh.

The finite-travel claim can be made explicit, eliminating any concern that
mere local Lipschitz continuity on a noncompact ball is being used as a
uniform bound. On the radius-\(R\) ball set

\[
 C_P=2Db^2\ell+2D^3b^4\ell.
\]

Subtracting \(P=I-T^*(TT^*)^{-1}T\) and using the inverse identity gives
\(\operatorname{Lip}(P)\le C_P\). Since \(P_{z_*}z_*=0\),

\[
 \|\dot z\|
 \le\bigl[2D^2+\epsilon(1+C_P\|z_*\|)\bigr]d(t)
              +\eta e^{-\sigma t}.
\]

Both terms are integrable. Mapping back to physical coordinates has operator
norm at most one, so total physical Hilbert travel is finite as claimed.

## 5. Noise, current information, and invariance

The noise term is an ordinary held-direction forcing. The map
\(z\mapsto|f(z)-Y|P_zU\) is locally Lipschitz, including where the residual
vanishes, because norm is Lipschitz. There is no quadratic-variation term.
Its amplitude is bounded by \(\eta\sqrt L\) and its effect on training
residual velocity vanishes exactly. Every conclusion is pathwise for all
permitted unit-bounded direction sequences, not merely almost sure.

The proposed odd powers \(Z_1,Z_1^3,\ldots,Z_1^{2m+1}\) are linearly
independent in the upper population: a polynomial vanishing almost everywhere
under a density positive on \((-1,1)\) vanishes on that interval and hence has
zero coefficients. Every one has positive finite norm and is bounded after
normalization. At initialization, \(T_0=(0,A_{h_0})\), so its normal space
has dimension exactly \(m\). At least one of the \(m+1\) directions has
nonzero projection. The positive-probability signed pair produces distinct
initial velocities and, by the short-time integral equation, distinct state
trajectories. This works also for \(m=1\); it does not rely on a nonexistent
scalar residual tangent direction.

The fields depend only on existing upper marks. Those marks are recoverable
from \(b_2\) by the fixed invertible whitening map. Together with current
\(\Gamma_1=\operatorname{Law}(b_1,g,w)\),
\(\Gamma_2=\operatorname{Law}(b_2,c)\), and \(M\), all contractions and
adjoints in the update are current-state quantities. Saving the current noise
index and refresh phase, or providing the future external forcing path,
suffices for restartability. No evolving neuron mark, future endpoint, or
untracked cross-population correlation is required.

Under measure-preserving population relabeling, the corresponding pullbacks
are unitary, \(T\) and \(P\) transform equivariantly, and the noise fields
pull back with their existing marks. The represented predictor is therefore
invariant. Orthogonal re-expressions of the dictionary coordinates likewise
preserve the physical Frobenius and population norms when the fixed tensors
and noise fields are transformed together. Arbitrary non-isometric changes
of the physical metric are not asserted invariances.

**Scope distinction, not a flaw:** the independence/dimension argument proves
nontrivial *state* randomness. It does not by itself prove distinct transient
predictions at an unseen input; a readout variation can in principle be
orthogonal to an entire represented query family. The candidate only claims a
nontrivial process and distinct initial velocities, so its stated conclusion
is correct. A stronger observable-randomness requirement would need its own
argument or a different declared direction set.

## 6. Honest limits and final disposition

The candidate expressly changes the hidden loss learning rate by
\(1/\rho\), adds a secondary direction that continues to act on the zero-loss
manifold, and uses a full finite-Jacobian inverse. Large \(\rho\) may be
required by difficult data geometry. These are substantive restrictions and
are not described as a small perturbation or as ordinary minibatch noise.

The selected hidden state can remain \(h_0\) when
\(\nabla J(h_0)=0\). Its dependency explicitly disclaims universal nonzero
hidden displacement; the candidate's statement that the rule *permits*
data-dependent changes is consistent with that limit. No all-data strict
movement theorem has been supplied or silently inferred from Gram positivity.

No correction to the main construction, constants, confinement proof, or
convergence argument is required by this review. The final revision has
corrected the forcing schedule in the optional time-rescaling sentence and
clarified the KKT display. Preserve the stated boundaries:
exact population integration at the canonical fixed order; data-dependent
conditioning and large hidden weight; specified vanishing projected random-ODE
noise; selected predictor uniqueness for this optimizer rather than for every
interpolating model or the original physical gradient flow.
