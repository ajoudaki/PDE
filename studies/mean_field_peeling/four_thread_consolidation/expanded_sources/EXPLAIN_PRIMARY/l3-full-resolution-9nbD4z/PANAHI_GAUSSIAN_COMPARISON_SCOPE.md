# Panahi comparison: bounded source-scope check

Status: no established training-mesh-uniform transfer to the canonical theorem.
Checked [arXiv:2603.09310v1, primary PDF](https://arxiv.org/pdf/2603.09310v1),
Sections 2–5 and Appendices B–C. Equation numbers below are PDF numbers;
the HTML numbering differs.

Equations (2)–(3) use differentiable causal queries of both orientations:
\(q=X\omega/m\), \(p=X^T\theta\).
For finite query count, Theorem 1 equates the laws of the surrogate and
the **perturbed** process (9), for \(\sigma>0,z\in\mathbb R\):
\[
\phi'=\phi+
\sigma\binom{m^{-1/2}\sum_\zeta R_\zeta^{1/2}U_\zeta}{V}
+\sqrt{(1+z^2)/m}
\binom{\sum_\zeta R_\zeta\Theta A_{\theta,\zeta}^{-1}
 (\Gamma_\zeta A_{\omega,\zeta})_{u}}
 {[\Omega_\zeta A_{\omega,\zeta}^{-1}
 (\Gamma_\zeta^T A_{\theta,\zeta})_{U}]_\zeta}.
\]
Here \(u/U\) retain/exclude diagonal blocks;
\(A_\theta^TA_\theta=\Theta^TR\Theta+\sigma^2I\),
\(A_\omega^TA_\omega=\Omega_\zeta^T\Omega_\zeta/m+\sigma^2I\).
The mechanism is covariance and derivative-covariance matching (22)
for causal inverse Jacobians; exact comparison needs no response-amplitude estimate.

Theorem 2 fixes \(J,L,d_z,n/m\), requires common Lipschitz query control,
bounded mixture means/covariances, and Assumption 1's DMF existence and
overlap/contraction concentration. Its conclusion (20) concerns bounded
Lipschitz tests in the norm
\(\max_l\{\|q(l)\|_2,\|p(l)\|_2/\sqrt m\}\).
Appendix C sets \(z=0,\sigma_m\to0\); items 2–3 remove errors by recursive
query-stability bounds, without tracking horizon dependence.
Claim 1's complex continuation is unproved and unused.

The canonical transfer remains open for specific reasons. Its GD horizon
requires a query count \(K\asymp Tn^2\), whereas the depth is three.
Even granting an exact encoding of both trained matrices through initial
Gaussian queries and stored updates, finite-horizon comparison does not
control this triangular array. The raw \(KJ\times KJ\) Gaussian
matrix has growing norm, but this observation is inconclusive after
contraction with the history and Euler integration. The subsequent
[frozen-history lemma](PANAHI_EULER_PERTURBATION_SIZE.md) now overcomes
that raw-size concern for deterministic time-regular histories: a
regularized effective-rank estimate makes both integrated perturbations
vanish in mean-square supremum norm for \(K\asymp m^2\).
Its exact Gaussian isometry does not apply by conditioning on the
actual perturbed histories, which themselves depend on \(\Gamma\).
The adaptive covariance and nonlinear propagation steps remain open.

Nor does arctangent smoothness verify query Lipschitz control: the middle
backprop query \(D(z)b\) has derivative \(\operatorname{diag}(\phi''(z)b)\).
An RMS bound on \(b\) does not uniformly bound this multiplier. The exact
comparison therefore supplies a finite perturbed representation; removing
its real-parameter perturbations and obtaining autonomous restart still
need new canonical estimates. No literature-wide exclusion or failure of
the target theorem is inferred. No experiments were performed.
