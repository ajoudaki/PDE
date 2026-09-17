# Author-side reconstruction and scope checks

2026-09-16. This record is not an isolated review.

Reconstructed the full `resolution_open_family.md` argument against the
complete symmetric candidate and its canonical setup. Its frozen review
version is SHA256 6c949bdec4e78fb895ae71281edd328623a662cba433fba618d65e82055fe337.

* Label absorption uses the architecture's exact oddness, so the third
  physical label remains -1. The p=1 dictionary is fixed in d=3; no rotation
  or reduction to the d=2 dictionary is used.
* At the coincident reference a_s=B M^T d, not a frozen-feature derivative.
  Together with M_s=d a^T this gives (Ma)_s=(|a|^2 I+M B M^T)d. Positive
  common upper preactivation makes the readout and common reverse response
  have the required signs. The first-zero proof closes persistence without
  assuming the desired sign.
* The value of d_parallel/s at s=0 is positive. Uniform finite-interval
  continuity follows from c(s)/s=integral_0^1 U(sv)dv, rather than dividing an
  uncontrolled small error by s. This closes the possible initial boundary
  gap in the nearby-seed argument.
* Active lower features are linearly independent despite their retained
  correlations: independent reverse noises have positive conditional
  variances, and the residual first marks have independent nonzero variances.
  Hence a nonzero reverse coefficient yields a nonzero lower query.
* For each distinct nearby symmetric seed, the input matrix has eigenvalues
  e,e,e+3 divided by sqrt(3+2e+e^2). The first-layer Gram estimate is pointwise
  in marks before taking expectation; it needs no false independence of
  lower gates and reverse queries. Strict positivity of the gates suffices.
* Initial upper Gram rank is supplied by the complete initialized kappa
  proof. It is used only at s=0. Later rank is proved separately from the
  lower backward response, so no initial-rank propagation is assumed.
* Hilbert input continuity is valid with Gaussian g: use ||w||2 times input
  displacement. Supnorm input continuity of gates would be false and is
  never used. Bounded finite dictionary fields control the reverse factors.
* Kernel positivity persists in a tube by uniform Lipschitz bounds on a
  bounded Hilbert ball. The full-state length bound is
  integral ||X_dot||<=sqrt(L/k), since L_dot=-||X_dot||^2 and
  ||X_dot||>=2 sqrt(kL). It makes the later tube invariant by a first-exit
  contradiction. The finite initial interval is handled separately.
* For the mixed potential, W>=1, grad W is explicitly differentiated, and
  |W_dot|<=2B sqrt(Lambda L). Choosing the residual threshold gives
  Phi_dot<=-2k Phi in the tail. Strict negative reference derivative on the
  compact initial interval survives by continuity. This produces one
  positive rate from t=0 with Phi(0)=2, not merely a delayed or prefactor
  statement. Phi<=2L is NOT claimed for nonsymmetric data.
* Reference curves are proof objects on an explicitly fixed finite auxiliary
  horizon. Neither the potential nor the autonomous closure uses a future
  endpoint. All potential ingredients are current-state expectations or the
  declared initialized constant C_0.

The full physical state converges in Hilbert norm, giving W2 convergence
of the complete saved joint laws under their common frozen-mark coupling.
No uniqueness of the hidden fitting endpoint or monotone pairwise alignment
is asserted. The constants and neighborhood may deteriorate at coalescence.

Also read and checked the complete frozen `resolution_endpoint.md`,
`resolution_positive.md`, and `resolution_metric.md`. The first two agree
after converting normalized versus unnormalized upper marks: at a rank-loss
time all hidden velocities vanish, c_s is the common upper field, and the
derivative of the common reverse coefficient is a strictly signed expectation.
The positive quadratic coefficient includes the lower gate-weighted square.
Closedness plus isolation gives finiteness on compact intervals. It does not
exclude one designated endpoint or amplitude. The analytic route separately
uses fixed-input bounded increments; it correctly avoids claiming real
analyticity of the unrestricted L2 Nemytskii map or in input supnorm.

The secondary generic-amplitude proof's endpoint trap and mixed-potential
derivative are valid at its stated nonexceptional amplitudes. That is not a
substitute for the exact unit-label theorem. No inference that amplitude one
is generic, or that neighborhoods remain uniform approaching it, is used.

## Quantitative addendum

Read the complete frozen `resolution_rate.md`. Its estimate for
(a_i-a_j)_s uses the exact common w_s, the gate Lipschitz bound, and the
feature-adjoint contraction; it is O(|v_i-v_j| s). Integration gives an
O(e s^2) upper-preactivation contrast error without input differentiation.
The initialized contrast is sqrt(2 tau)[kappa(a_e)-kappa(b_e)], and kappa'
has positive min and finite max on [1/sqrt(6),2/sqrt(6)]. The fixed initial
interval therefore retains a contrast at least a constant times e. Uniformly
bounded upper preactivations make tanh's lower slope strictly positive.
After division by the probability factor, the transverse upper eigenvalue
is ||H_i-H_j||2^2/6, giving the stated early constant with denominator 72.

On the remaining interval s>=s_0>0, lower response convergence is uniform
in the correct L2/L-infinity finite-coefficient topology, so R_i>=r_0/2.
The exact input eigenvalue is e^2/(3+2e+e^2); the normalized first-layer Gram
thus gives r_0 e^2/36. The initial upper contrast gives the matching upper
bound tau k_+^2 e^2/9. All factors of three and both time intervals agree.
Therefore mu_e is bounded above and below by positive constants times e^2.
The refinement concerns full three-direction conditioning, not the faster
one-direction symmetric residual. It supplies a potential decay rate at
least a positive constant times e^2 on the reduced open neighborhood; the
neighborhood radius itself remains unquantified.
