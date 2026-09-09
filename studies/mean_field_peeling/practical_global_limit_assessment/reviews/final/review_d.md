# Independent adversarial audit

**Verdict: PASS. No required corrections.**

I read only `/home/amir/Codes/PDE/studies/mean_field_peeling/practical_global_limit_assessment/reviews/final/ASSESSMENT.md` as mathematical input. I did not inspect the cited manuscripts, literature, other reviews, or prior discussions. Statements about existing results are therefore treated as attributed premises, not independently certified results. This verdict concerns the assessment and its elementary deductions; it does not certify any of its explicitly open trained-limit conjectures.

## Constants and relative nonlinearity

The displayed gain selection has the stated separation asymptotics: with fixed positive shape constant, its two terms scale respectively as delta^(-2) and delta^(-8/5), so their maximum is of order delta^(-2). The first term gives reciprocal bounds approximately 5.2081e-17 and 5.2083e-21 at the two displayed separations. The stated, slightly weaker numerical bounds are correct.

The affine-regression identity is exact because adding an affine function does not change the orthogonal residual to the affine subspace, and multiplication by e scales its squared norm by e^2. For centered Gaussian Z with variance sigma^2, integration by parts gives

    E[Z phi(Z)] / sigma^2 = a + e E[psi'(Z)].

Projection onto Z consequently bounds E[phi(Z)^2] below by sigma^2(a-e)^2. The numerator is at most e^2, and a-e >= a/2 under the stated assumptions. Thus the relative fraction is at most 4e^2/a^2. There is no missing contribution from the activation's nonzero mean, since projection onto Z alone is a valid lower bound.

Three distinct points on a sphere are affinely independent: affine dependence of three distinct points would put them on a line, whereas a line meets a sphere in at most two points. Therefore the warning that interpolation of three labels does not by itself certify a nonlinear function is correct.

## Compact-time existence, fitting, and continuation

For a true gradient flow in a fixed finite-dimensional raw metric, differentiating the loss gives dE/dt = -||dot Theta||^2. Integrating and applying Cauchy--Schwarz gives both displayed bounds. For any finite candidate maximal time, the path is bounded and is Cauchy as that time is approached. Smooth local existence then extends it. This proves finite-width continuation without a kernel lower bound, separation, exponential fitting, or a finite total residual clock. It does not provide the missing population compactness or uniqueness.

The assessment correctly distinguishes these issues. A bounded set in an infinite-dimensional Hilbert space need not be strongly precompact, and an L2 control on q does not generally make multiplication by q bounded on L2. The backward-gate example therefore identifies a real gap in an ambient-ball Lipschitz argument without asserting a counterexample for reached states.

The proposed Gaussian-type L2 tail bound beats a comparison factor exp(CR): for every fixed positive c, exp(CR-cR^2) tends to zero. This is a consistent sufficient research obligation given the attributed cap comparison and the requisite conversion of incoming-field tails into a gradient cap-error bound. The document correctly leaves this obligation unproved and leaves the finite-width and observation bridges to verification.

The proposed stopped energy argument is also logically sound and need not be circular in the stopping radius. To make the implication explicit, suppose the gradient error on a stopped radius-M trajectory is bounded by epsilon_R(T,M), tending to zero at each fixed T,M. Writing A = integral_0^t ||G_R||^2 and using nonnegativity of E gives

    A <= E(0) + epsilon_R sqrt(t A).

Consequently,

    sqrt(t A) <= [epsilon_R t + sqrt(epsilon_R^2 t^2 + 4t E(0))]/2.

The right side tends to sqrt(t E(0)). A displacement radius M strictly above sqrt(T E(0)) can therefore be fixed first; sufficiently large caps stay strictly inside that radius. If a raw ball is centered at the origin rather than initialization, its radius must also contain the initial state. Neither the energy identity nor this conditional stopping argument establishes the unproved tail or gradient-comparison estimate.

The ascent counterexample is exact: sec' = sec tan and tan' = sec^2 yield all three equations, and the solution blows up at pi/2. Constant prescribed ascent feedback is bounded but does not satisfy squared-loss dissipation. The example validly refutes replacing physical feedback with arbitrary bounded controls.

## Residual composition versus Gaussian composition

The residual Jacobian product bound follows from submultiplicativity and 1+x <= exp(x). For the scalar residual example, differentiating sinh(h) gives beta sinh(h), yielding the displayed exact solution. Its derivative equals exp(beta) at zero and tends to one at either infinity, so it is nonaffine for beta>0. Boundedness and Lipschitz continuity of tanh justify the ordinary Euler convergence claim.

The dense Gaussian Jacobian retains its Gaussian matrix factor when the scalar activation approaches identity. Thus the assessment correctly rejects the inference that this architecture becomes an identity-plus-small-perturbation residual composition.

For equal Gaussian marginal variances, integration by parts gives the displayed cross term Q_ij a(q). Expanding the activation product then gives Q^+, and subtracting the normalized matrices yields exactly

    C^+ - C = e^2 (B-bC)/q^+.

Here Q^+ is the next centered preactivation covariance after fresh Gaussian mixing, determined by the uncentered second moments of the activated features. No centering of the activation itself is required.

The lower variance bound follows by projection onto a standard Gaussian and |a(q)| <= 1. For e=beta/L <= 1/2, log(1-e) >= -2e gives the uniform lower bound exp(-4 beta) over at most L layers. The upper bound follows by iterating the L2 triangle inequality. Since correlations have modulus at most one and |B_ij|, b <= ||psi||_infinity^2, summing the normalized increments gives exactly the stated O(1/L) estimate. These depth claims are asymptotic for fixed beta; the explicitly stated e <= 1/2 condition holds once L >= 2 beta.

The affine-offset calculation is likewise exact: each fresh Gaussian mixing adds beta^2 b^2/L^2 times the all-ones matrix to the preactivation covariance. It therefore adds beta^2 b^2/L in total, not a coherent first-order shift of size beta b.

## Calibrated Gaussian candidate

The choice a0=E[G atan(G)] makes E[G r(G)]=0. The variance v is strictly positive because atan is not linear, and is finite because r has at most linear growth. Its derivatives of positive order are bounded. The explicit warning that r itself is unbounded is correct and prevents an illicit transfer into the earlier bounded-perturbation class.

The normalization makes the initialized variance exactly one. Conditional Gaussian expectation eliminates both mixed correlation terms, giving the stated exact recursion. With e_L^2=beta^2/L, its increment is

    (beta^2/L) [R(c)-vc] / (1+beta^2 v/L).

Its difference from the Euler increment is uniformly O(L^(-2)); R is bounded by v and is Lipschitz by Gaussian covariance differentiation and bounded r'. These facts justify convergence of the mesh values, or their standard interpolation, uniformly over the unit depth interval. The Gaussian feature interpretation ensures every discrete correlation stays in [-1,1].

Oddness gives R(0)=0. Gaussian integration by parts gives E[r'(G)]=0, and covariance differentiation at zero gives R'(0)=0. Since R(1)=v>0, R and the limiting generator are not affine. The resulting time-one correlation flow is also nonaffine: it fixes both endpoints, while its nonzero scalar vector field moves at least one interior point, so it cannot be the identity or any other affine endpoint-fixing map. The nonlinear effect need not change every special input correlation, which the assessment does not claim.

The budget beta^2 v can be fixed at order one independently of separation by choosing a fixed beta. All of this concerns initialization. The text explicitly and correctly withholds any claim about trained nonlinearity, global trained continuation for this candidate, or a joint width-depth limit.

## Metrics and claim levels

Under the stated uniform sensitivity bounds, a 1/L residual factor gives an O(1/L) parameter derivative. Summing squared derivatives over L independently parameterized branches in an unaveraged metric gives an O(1/L) branch kernel contribution. The conclusion that training-time or metric normalization must be analyzed is appropriate; no lower kernel bound or universal normalization theorem is claimed. The warning that readout scaling must also be specified is pertinent.

The residual-particle manuscript and cited ResNet paper are clearly presented as different models or methodological references. Their attributed theorem descriptions are not used as a substitute for proving the target architecture, metric, initialization, or observables. The distinction between pointwise-time and uniform-time probability statements is preserved.

Overall, the ledger accurately separates elementary forward/initialization results, attributed earlier results, conditional proof mechanisms, and open trained-limit obligations. I found no elementary mathematical error or implication requiring correction.
