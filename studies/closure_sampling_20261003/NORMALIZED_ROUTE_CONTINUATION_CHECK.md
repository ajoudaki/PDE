# Reconstruction and scope of the normalized-route continuation

2026-10-04. Coordinator internal check, not an independent promotion review.
This report covers the two independently authored routes listed below and
records the interfaces between the new results. Both inputs were read in
full, and their calculations were reconstructed without treating a prior
check label as proof. The normalized neural convention, rigorous proof
instructions and study boundary were retained. No experiment was run.

Frozen inputs:

- NEARCRITICAL_GEOMETRY_ROUTE.md:
  99f088dfdfb41b7e5ec560a1df74096b983af7d6958a2f4206e172758d474441.
- EXPLICIT_UNBOUNDED_NORMALIZATION_ROUTE.md:
  35471064d8a9c21828085123f8ad1d561a887e89dba7663c3d8f4eef88948ffc.

Verdict: their stated initialized geometry and real dense fitting theorems
pass this reconstruction. Neither input proves the requested all-time
polynomial-depth autonomous compression theorem. No numerical label,
error or size bound for that missing theorem is certified by this report.

## 1. Near-critical initialized geometry

Let chi=E phi'(Z)^2>0, E phi(Z)^2=1, and
kappa=E phi''(Z)^2<infinity when second derivatives are used. The Hermite
construction in the input proves F(c)=sum p_k c^k with p_k>=0,
sum p_k=1, sum k p_k=chi, and sum k(k-1)p_k=kappa. The cutoff integration
by parts is legitimate under the stated Gaussian L2 assumptions; the
completeness proof uses an integrable Gaussian-weighted function, entire
Gaussian Laplace transform, and a Gaussian approximate identity.

The chain rule for K_L=F composed L times gives A_(l+1)=chi A_l and
B_(l+1)=kappa A_l^2+chi B_l. Iterating gives exactly
A_L=chi^L and B_L=kappa chi^(L-1) sum_(j=0)^(L-1)chi^j. In the degree-k
tensor feature, a circle derivative has norm squared k and a second
derivative norm squared 3k^2-2k. Summation gives A_L and A_L+3B_L,
respectively. Their finite sums also justify the Hilbert derivatives by
integral difference quotients and dominated convergence. The finite-network
jet argument conditions only on lower initialized layers; bounded scalar
derivatives give the required finite polynomial Gaussian moments. It does
not differentiate a pointwise-in-probability limit.

The Gram lower bound has an additional input-gap premise, explicitly scoped
to that bound. For C>=eta I with diagonal one, the diagonal difference
between C^{circ k} and (C-eta I)^{circ k} is
1-(1-eta)^k. Tensor Gram positivity gives the matrix comparison.
The elementary scalar inequality
1-(1-eta)^k>=k eta/[1+(k-1)eta], followed by Jensen with weights
kp_k/chi, gives eta_next>=chi eta/[1+(kappa/chi)eta]. Its reciprocal
recursion yields
gamma_L>=chi^L/[gamma_0^(-1)+(kappa/chi)S_L]. In the subcritical
two-input example, the error ratios relative to chi are 1+O(delta_l),
with summable positive delta_l; their product has a finite nonzero limit.
Thus the asserted exponentially small two-point gap for fixed chi<1 is
not just a one-sided upper estimate. These assertions are about initialized
features, not a compressor lower bound.

For the unbounded linear-plus-erf family, direct integration gives
E erf(Z/sqrt2)^2=1/3,
E[Z erf(Z/sqrt2)]=1/sqrt(pi),
E[(erf)'(Z/sqrt2) with the chain factor]^2=2/(pi sqrt3).
These reconstruct Q,D and both normalizations. The variance map cross
term is 2alpha sqrt(2/pi) q/sqrt(1+q); its derivative at one is
3alpha/(2sqrt(pi)). The last arcsine term contributes 1/(pi sqrt3).
Therefore the displayed N and a=chi N/D are correct. Since chi<=D/Q
and N<Q, the real variance derivative is strictly less than one
throughout the admitted interval, not just at chi=1. Strip slopes follow
from the exact modulus of exp(-z^2/2). The finite-width norm CLT uses
the exact Gaussian conditional transition, independent limiting innovations,
and a fourth-moment uniform-integrability argument. The boundedness of
(phi^2)'' needed there holds because phi grows linearly and phi'' is
a decaying Gaussian times a polynomial.

For the complex scalar calculation, pseudocovariance stays one by the
Gaussian heat identity applied to phi^2. The Hermitian derivative is
E|phi'|^2, which is the displayed F'(r); the integral
E exp(-U^2/2)=1/sqrt2 uses absolute integrability on r<2. The value
F''(3/2)=24chi/(7pi sqrt7D) is the exact upper curvature B. The
normalized excess u_j=e_j/chi^j has increment at most
(B/(2chi))chi^j u_j^2. The chosen e_0 implies u_j<=3e_0/2<2e_0,
so the bootstrap is strict. Taking logarithms gives the derivative
product bound exp(1/2)chi^L. The reverse reciprocal comparison sums
with weight chi^(j+1) and yields the asserted necessary S_(L-1)^(-1)
covariance scale. This verifies both sufficient and necessary orders of
the population complex radius.

Finite-network convergence in that complex paragraph is explicitly only
in probability on covariance neighborhoods strictly inside the integrability
region. It is compatible with infinite unconditional finite-width moments.
No expectation limit is being inferred. Fixed-depth limits are retained;
no growing-depth width threshold has been supplied.

## 2. Explicit real fitting with no activation-value bound

The physical metric is ||A||_F^2/n+sum ||W_l||_F^2+||w||^2/n, exactly
inverse to the mobilities in the squared-loss flow. Thus
-d rho^2/dt=||theta_dot||_par^2 with no missing m or n factor.
The feature Gram is H^top H/(mn), with initial limiting gap gamma/m,
not gamma. On its stopped margin gamma/(4m), the readout contribution
is at least (gamma/m)rho^2. Consequently -rho_dot>=gamma rho/(2m).
Changing variables from time to rho in the path length yields
2Y sqrt(m/gamma), exactly as stated.

On the stopped sphere RMS cap two and matrix cap nine, the backward
constant is D_l=s(9s)^(L-l). The first-weight update has norm at most
2rho D_1 ||w||_n, and a hidden-matrix update has Frobenius norm at most
4rho D_l ||w||_n. Thus U_1=D_1, U_l=2D_l are correct. Multiplying
the readout bound by the residual integral gives hidden displacement
8U_l Y^2(m/gamma)^(3/2). The forward subtraction coefficient obeys
F_1=sU_1, F_l=s(2U_l+9F_(l-1)). Expanding this finite recurrence gives

F_L=s^2[(9s)^(2L-2)+4 sum_(j=0)^(L-2)(9s)^(2j)],

which dominates every prior F_l and U_l for s>=1,L>=2. At
Y<=(gamma/m)/(8sqrt(F_L)), all displacements used in the bootstrap
are at most sqrt(gamma/m)/8. The feature map singular value therefore
stays at least sqrt(gamma/(2m))-sqrt(gamma/m)/8, strictly above
sqrt(gamma/(4m)). Sphere RMS is at most 13/8 and each stopped
operator at most 65/8. These strict inequalities close every stop.
The finite path length and local C2 regularity supply global continuation
and a parameter limit at each fixed finite width.

For the tail, ||w_dot||_n<=4rho, ||h_L||_n<=2, and
||h_L_dot||_n<=2rho F_L(2Y/sqrt(gamma/m)). The product rule yields
|f_dot|<=8[1+F_L Y^2/(gamma/m)]rho, uniformly over the real sphere.
Integration gives the factor 16, and the label cap reduces it to 65/4.
This is an output tail of the original flow, not a compression error.

The initialization probability proof is also consistent. Bilinear
1/4-nets give exactly the stated Gaussian operator tails at cap eight.
Normalized activation moments give pointwise initialized RMS convergence
to one at every layer. On the operator event the input map is
(8s)^l-Lipschitz; a fixed mesh [4(8s)^L]^(-1) therefore upgrades the
pointwise convergence on its finite net to the stated whole-sphere cap.
This can have a very large but finite net; no polynomial bound on the
width threshold follows from this proof. Covariance convergence on the
fixed training set includes singular lower-layer covariances and gives
the top Gram event. No trained Gaussian approximation is used.

The remote-bump family in the route has exactly unit forward second
moment, derivative second moment tending to one, diverging real slope,
and no analytic extension. The Gaussian support estimate, the integration
by parts E b_N'=E Z b_N, and the ratio formula for chi_N-1 check
directly. It refutes the inference that the two moments alone specify
the needed regularity constants. It does not refute all compression
schemes for smooth functions.

## 3. Logical assembly

The two checked results cannot be substituted into one another to obtain
the desired new compressor. Initialized moment maps have a Gaussian law;
the finite trained products do not. The real fitting theorem uses the
actual slope supremum and worst-case mixer bounds; it has not replaced
them with chi. It therefore retains an exponential-depth label coefficient.
Its sphere RMS estimate gives no coordinate concentration for unbounded
top carriers. The explicit reciprocal inequalities in the unbounded route
still need their own numerical trace and Gaussian budget coefficients.

Two coordinator candidates have separate nonauthor reconstructions:
NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md proves a finite-width
unconditional complex-moment obstruction; NEARCRITICAL_ALL_ORDER_ROUTE.md
proves a radius controlling all initialized population derivative orders.
The checks preserve their distinct quantifiers. Neither result implies
that a stopped high-probability trained source theorem is impossible.

The trained two-layer route and the subsequent loss-integrated tangent
route provide genuine finite-network progress in explicitly restricted
input directions. Their local estimates do not supply the general-data,
whole-query, all-order comparison required by the full theorem. All
new results remain internally checked study material. No manuscript or
established-book claim is changed or promoted.
