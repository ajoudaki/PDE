# Internal check of the real fitting certificate

2026-10-04. This is a collaborative internal reconstruction, not a promotion
review. The geometry-note author checked the complete
DATASET_LABEL_DEPENDENCE.md after freezing their own geometry proof.
The complete GENERAL_WEIGHTED_COMPARISON.md was also read; its model,
weighted construction, and deterministic comparison definitions were used.
No linked study, manuscript, book, or external source was fetched, and no
experiments were run. Required mathematical skills and shared process
instructions were applied.

Reviewed hashes:

- DATASET_LABEL_DEPENDENCE.md:
  b5d44373013c67b25a44d7907eef69b4458049eaca11f846b6c64df56b7400d3.
- GENERAL_WEIGHTED_COMPARISON.md:
  1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306.
- Previously frozen DATASET_GEOMETRY_EXAMPLE.md:
  e2e8c961297329ce2bb9260ed6b5cb92a06affc1b52c0ebf00bd5fd3284eb5b5.

**Verdict:** the real deterministic fitting proposition, its constants, the
weighted extension, tails, and actual-to-limiting gap conversion pass this
check. No quantitative correction is needed. The separate initialization
concentration, carrier, and analytic-source theorems are not certified here.

The source uses \(f_a=w^\top h_a^{(L)}/n\), mean squared loss
\(\mathcal L=\rho^2=m^{-1}\sum_a(y_a-f_a)^2\), zero initial readout, and
mobilities \((n,1,\ldots,1,n)\). Direct differentiation gives
\(\nabla_A\mathcal L=-2(mn)^{-1}\sum_a c_a\delta_a^{(1)}v_a^\top\),
\(\nabla_{W^{(\ell)}}\mathcal L=-2(mn)^{-1}\sum_a
c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}\), and
\(\nabla_w\mathcal L=-2(mn)^{-1}\sum_a c_ah_a^{(L)}\).
Thus its updates and inverse-mobility energy metric give exactly

\[
p^2:=\|\dot\theta\|_{\rm mob}^2
=-\frac{d}{dt}\rho^2
=4\langle c,\Gamma c\rangle_m.
\]

The first-layer tangent term is the Gram of the tensor products
\(\delta_a^{(1)}\otimes v_a\); it remains positive for correlated inputs.
Hence \(\Gamma\succeq\Gamma_w\). Before the proposed Gram exit,
\(\Gamma_w\succeq\lambda I_m/4\), so

\[
-\dot\rho\ge\lambda\rho/2,\qquad
p\ge\sqrt\lambda\,\rho,\qquad
p\le2(-\dot\rho)/\sqrt\lambda.
\]

At positive residual this follows by substituting
\(p^2=-2\rho\dot\rho\). At zero residual all velocities vanish and uniqueness
gives the stationary continuation. Integrating and using \(w(0)=0\) yields
\(\|w(t)\|_n\le2(Y-\rho(t))/\sqrt\lambda\).
The source's velocity estimates then use

\[
\int_0^t\rho(Y-\rho)\,du
\le\frac2\lambda\int_0^t(-\dot\rho)(Y-\rho)\,du
=\frac{(Y-\rho(t))^2}{\lambda}.
\]

This verifies the exact displacement constants
\(4b_1Y^2/\lambda^{3/2}\) and
\(4Bb_\ell Y^2/\lambda^{3/2}\).
Forward subtraction gives precisely
\(F_1=sb_1\) and \(F_\ell=s(B^2b_\ell+RF_{\ell-1})\), including its factor
\(B^2\), and top feature displacement at most
\(4F_LY^2/\lambda^{3/2}\).

For \(T=H_L/\sqrt{mn}\), the Frobenius norm of its perturbation is the RMS
over samples of the normalized feature perturbations. Thus no extra factor
of \(m\) enters. Under \(Y\le\lambda/(4\sqrt{C_*})\),
\(\|T(t)-T(0)\|_{\rm op}\le\sqrt\lambda/4\), so its smallest singular value
is at least \(3\sqrt\lambda/4\), proving the \(9\lambda/16\) Gram margin.
Also \(b_\ell\le b_1\) and the trace bound
\(\lambda\le B^2/m\le B^2\) give

\[
\|W^{(\ell)}(t)-W_0^{(\ell)}\|_{\rm op}
\le\frac{Bb_\ell\sqrt\lambda}{4C_*}
\le\frac{B^2b_1}{4C_*}\le\frac14.
\]

Both exits have strict margins, including equality in the label threshold.
The \(C^2\) assumptions give a locally Lipschitz finite-dimensional vector
field. Finite mobility path length bounds the entire finite parameter state
and supplies a limit at any putative finite maximal time, so local existence
extends it. The same argument at infinite time proves parameter convergence;
residual decay makes the limiting state interpolating. A bound on \(A_0\)
is unnecessary for this argument.

The tail constants check exactly:

\[
\int_t^\infty\rho\le2\rho(t)/\lambda,\qquad
\int_t^\infty p\le2\rho(t)/\sqrt\lambda.
\]

Differentiation of the forward pass gives
\(\|\dot h^{(\ell)}(t,v)\|_n\le2F_\ell\rho\|w\|_n\) for every unit query.
Consequently
\[
|\dot f(t,v)|
\le2B^2\rho+2F_L\rho\|w\|_n^2
\le(2B^2+8F_LY^2/\lambda)\rho.
\]
Integrating gives the claimed query-tail coefficient
\(4B^2/\lambda+16F_LY^2/\lambda^2\).

The activity-only comparison also checks. Its top feature perturbation is
at most \(2BF_LS^2\), where \(S=\int_0^t\rho\).
Since \(\|T(t)\|_{\rm op},\|T(0)\|_{\rm op}\le B\), the direct Gram
perturbation is at most \(4B^2F_LS^2\). This gives sufficient label power
\(3/2\), while perturbing singular values gives power \(5/4\).
At the displayed \(S_0^2=\sqrt\lambda/(8BC_*)\), feature and operator
margins are respectively \(\sqrt\lambda/4\) and \(1/4\).
Source (20) gives \(2Y/\lambda\le S_0/2\), closing that argument.
Neither comparison establishes an optimal label threshold.

For the weighted model, the hidden metric is
\(\langle X,E\rangle_{\rm HS}
=\operatorname{tr}(D_{\ell-1}^{-1}X^\top D_\ell E)\).
Pairing the loss differential
\(-2m^{-1}\sum_a c_a\delta_a^{(\ell)\top}D_\ell E
h_a^{(\ell-1)}\) with this metric gives exactly its autonomous hidden
velocity. The first-weight metric \(\operatorname{tr}(A^\top D_1A)\) and
readout metric \(w^\top D_Lw\) give its remaining velocities.
Thus loss dissipation is again the sum of squared block velocities.
The rank-one Hilbert--Schmidt norm is
\(\|\delta\|_{D_\ell}\|h\|_{D_{\ell-1}}\); positive masses of total one
preserve the activation bound \(B\) and slope bound \(s\).
The weighted adjoint preserves operator norms.
Finally \(D_L^{1/2}H_L/\sqrt m\) supplies the same singular-value argument,
and the comparison construction preserves the initialized Gram and initial
operator bound. No reciprocal smallest mass enters.
Positive initial Gram implicitly requires at least \(m\) top coordinates;
exact Gram preservation already enforces this condition.

The actual-to-limiting conversion is deterministic and correct: on event
(22), the Rayleigh quotient bound gives actual normalized gap at least
\(\lambda_\infty/2\). Substitution yields
\(Y\le\lambda_\infty/(8\sqrt{C_*})\).
If \(Q^{(L)}\succeq\gamma I_m\) is stated without sample normalization,
the sufficient bound becomes \(Y\le\gamma/(8m\sqrt{C_*})\).
The label norm here is RMS; converting to Euclidean norm multiplies that
bound by \(\sqrt m\). This check does not re-prove the probability of (22)
or the cited positivity criterion. The two-input geometry proof separately
verifies that the initialized normalized gap can tend to zero at fixed
sample count, without proving unrestricted fitting failure.

The conditional comparison algebra is correct under the trajectory
regularity discussed below. Integrating its first inequality and dropping
the nonnegative terminal value gives
\[
d(t)\le C_{\rm cmp}\int_0^t\rho(d+\epsilon),\qquad
C_{\rm cmp}=A_2+A_1B_{\rm cmp}/\kappa.
\]
Finite-time suprema give \(\sup d\le\Theta\epsilon/(1-\Theta)\) for
\(\Theta=C_{\rm cmp}\int_0^\infty\rho<1\); an integrating factor gives
\(\sup d\le(e^\Theta-1)\epsilon\) without that restriction.
For example, if
\(A_1\le a_1\), \(A_2\le a_2(1+M)\), and
\(B_{\rm cmp}\le b(1+M)\), with gap-independent constants, then
\[
\Theta\le
2(1+M)Y\left(\frac{a_2}{\lambda}
+\frac{2a_1b}{\lambda^2}\right)
\le2\max(a_2,2a_1b)
\frac{(1+M)(1+\lambda)Y}{\lambda^2}.
\]
This verifies the conditional absorption scale (27).
It does not identify the full analytic-source label threshold or certify
gap-independent source constants. Replacing the real Gram argument alone
does not remove restrictions from the remaining source proof.

The original reviewed version needed two wording clarifications:

1. The complex-strip sentence should say a bounded **holomorphic** extension.
   Boundedness alone does not imply derivative bounds; Cauchy's formula
   supplies them for a holomorphic extension on a narrower strip.
2. The abstract Dini-comparison paragraph should state local absolute
   continuity, or the corresponding continuous Dini-comparison hypotheses.
   A forward Dini inequality alone does not exclude upward jumps in an
   arbitrary discontinuous function. Actual finite-network state and
   residual norms have the required local absolute continuity.

These are clarifications of conditions already present in the intended
application. The recorded verdict concerns the real fitting certificate and
the displayed conditional comparison algebra, not the complete compression
theorem or attribution to unread sources.

**Revision check:** the author applied both wording changes, and the corrected
passages were reread. The current source SHA-256 is
bfd01ccacf6c78337331cf16a0c7137353d31c9a7e4d3b08357af7e32f356f52.
Both notes are resolved. The quantitative proof is unchanged and the final
bounded verdict is **PASS**, with the scope exclusions stated above.
