# A second-power sufficient coefficient for the complete two-input theorem

2026-09-07. Complete candidate assembly; final independent-review status
is recorded in REVIEW_STATUS.md. Earlier mathematical files are unchanged.

## 1. The theorem and the unchanged numerical coefficient

Retain the precise finite model, initialization, raw metric, population
spaces and conclusions of
../two_sample_odd_activation_theorem/PROOF.md. There are two deterministic
inputs with squared norm d, arbitrary binary labels, and three hidden
layers using the same activation. In particular, the initialized finite
readout is retained and raw GD is simultaneous raw Euler with step n^-2.

Define exactly the previous numerical constants
\[
 C_0=1296000\exp(1404),\qquad C_z=1500C_0,\qquad C_g=14400C_0,
\]
\[
 H=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4,
 \qquad c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.       \tag{1}
\]
Here c_* is the explicit primal/nonaffinity constant in equation (10) of
../two_sample_odd_activation_quantitative/PROOF.md. It is fixed before
choosing the data or any trajectory.

For every \(0<\delta\le1\), every such two-input dataset with
\[
 |\rho|=|\langle x_1,x_2\rangle/d|\le1-\delta,
\]
and all
\[
 \tfrac12\le a\le1,\qquad 0<e\le c_{\rm poly}\delta^2,
 \qquad \phi_{a,e}(z)=az+e\arctan z,                       \tag{2}
\]
the complete original theorem holds. Consequently every
\[
 0<\theta_\delta\le c_{\rm poly}\delta^2,\qquad
 \phi_\delta(z)=(1-\theta_\delta)z+
                         \theta_\delta\arctan z           \tag{3}
\]
is admissible. The requested \(c_{\rm poly}\delta^3\) choice is
included, as are the previous fourth-, tenth- and eight-hundredth-power
choices.

The conclusions include one autonomous global strong population flow,
uniqueness against nonsymmetric bounded-primal strong competitors on
the same canonical action spaces, restart from every reached state,
and full-width-sequence joint GF/raw-GD convergence in probability on
every fixed finite physical interval. All original action orientations
and actual adjoints, all four full sample kernel matrices, prediction
and loss limits, same-layer preactivation/feature path and velocity
laws, second moments and integrated squared speeds are retained.
Activation-regression nonaffinity holds at every finite physical time;
the original initial hidden-block/sample/layer motion certificates hold.

The amplitude depends on delta alone. The width convergence is for each
fixed dataset and finite interval. Exponent two is sufficient; its
optimality and a practical-size prefactor are not established. The
three-input analysis is separate and does not assert the analogous
complete theorem.

## 2. Exact scale and a weighted primal comparison

Fold labels by oddness and set
\[
 r=\sqrt{(1+y_1y_2\rho)/2},\quad \lambda=a^3r,
 \quad M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\]
The affine normalized clock is \(t=\lambda s\). Its first prediction
target 3/2 occurs at \(T<2\), with feature duration \(S=T/\lambda\).
The prior affine proof gives
\[
 S\le M^4,\qquad r=\frac3{\sqrt2a^3}M^{-4},\qquad
 M\le24^{1/4}\delta^{-1/8}.                              \tag{4}
\]
Negative powers of r below use this exact intrinsic M, not a uniform
upper envelope substituted into an identity.

Let \(w(t)=\sqrt{1+\|D_0(t)\|^2}\). The fourth-power affine
propagator proof, including its radius-one tube, gives
\[
 G(t,u)\le\exp(2100)\frac{w(t)^3}{w(u)^3}.
\]
At a common raw state in that tube, the capped nonlinear field differs
from the affine field by at most \(Ce\,w(u)^3\) in feature time,
uniformly in cap. Duhamel's inequality in normalized time therefore
proves
\[
 E(t):=\|\Theta_e(t)-\Theta_0(t)\|_{\rm raw,sum}
 \le C\frac e\lambda w(t)^3\int_0^tdu
 \le H\frac e\lambda w(t)^3.                            \tag{5}
\]
This comparison differentiates only the affine field. Every primary
norm is bounded by a numerical multiple of w on the tube. The previous
restriction \(e\le c_*\delta^{7/4}\), which is implied by (2),
already closes the tube and supplies the endpoint/nonaffinity margins.
Thus (5) is a valid improvement on the actual capped program, before
any new source bootstrap closes. At the endpoint it is \(O(eM^7)\),
improving the earlier \(O(eM^{12})\) comparison. Deterministic Euler
approximation transfers the estimate to sufficiently fine fixed meshes.

SECTOR_RESPONSE.md proves the needed consequences of (5) in full.
For clarity, an important distinction is between the active and inactive
sample combinations. With \(P=(z_1+z_2)/2\), \(Q=(z_1-z_2)/2\),
oddness and the Lipschitz bound for arctangent give
\[
 \left|\frac{\arctan(P+Q)+\arctan(P-Q)}2\right|\le|P|.
\]
Consequently the active first and second feature discrepancies are
bounded by \(Ce\,w^3\) and \(Ce\,w^4\), while their affine norms
are bounded by \(Crw\) and \(Crw^2\). Their active learned-moment
strict-density errors are therefore bounded by
\[
 Ce\,r w^4\le Ce,\qquad Ce\,r w^6\le CeM^2.             \tag{6}
\]
The inactive forward errors have larger bounds but only need a fixed
strict-density margin in the coefficient comparison.

The actual raw L2 incoming-field bounds remain
\[
 \|q^1\|_2\le HM^3,\qquad
 \|q^2\|_2\le HM^2,\qquad \|C\|_2\le HM.
\]
The inactive backward fields are smaller: their top and middle norms
are \(O(eM)\) and \(O(eM^2)\). The common readout makes the top
contrast purely nonlinear; applying the actual bounded adjoint and
then the next capped gate gives the middle contrast bound. These
facts concern actual source output laws, not a formal affine covariance
comparison.

## 3. Weighted affine kernels and a source box with distinct sectors

WEIGHTED_AFFINE_AND_CLOSURE.md proves the following exact deterministic
interface. It uses the existing independent-root source probes, with
injection costs evaluated at their own source time and output costs at
the terminal time. In normalized active coordinates, strict densities
obey
\[
 F(t,u),T(t,u)\le C\frac{w(t)^3}{w(u)^3},\qquad
 V(t,u),W(t,u)\le C\frac{w(t)^4}{w(u)^2}.
\]
All current resolvent identities remain present. The affine B3 also
contains its learned-moment term \(Cw(t)w(u)\), which is retained
when multiplying kernels.

The radial estimates imply
\[
 \int w\le C,\qquad \int_0^t w^2\le C\log(\mathrm e w(t)),
 \qquad\int_0^t w^4\le Cw(t)^2,
 \qquad\int_u^T w^{-2}\le Cw(u)^{-4}.
\]
The exact identities \(FL=F+FB_3V\) and \(RF=F+VB_3F\), followed
by these weighted integrals, give
\[
 (FL)(t,u)\le C\frac{w(t)^3}{w(u)^2},\qquad
 (RF)(t,u)\le C\frac{w(t)^4}{w(u)^3}.                  \tag{7}
\]
This avoids the much larger estimate obtained by multiplying uniform
endpoint bounds. Every inequality holds on sufficiently fine positive
meshes, with no minimum-step assumption.

At the same outer beta reference as before, use active backward excess
radius \(H^{-100}M^3\) and inactive radius \(H^{-100}M^{-4}\).
Active forward coefficients are bounded by that affine beta reference;
inactive forward coefficients have their baseline plus density one.
The normalized active backward excess has size \(O(rH^{-100}M^3)\).
Weighted Neumann ratios cost at most this quantity times
\(C\log(\mathrm e30M)\), so they stay uniformly small. The inactive
integration row costs \(M^4\) and is controlled by its separate
radius. Thus this larger box retains the precise forward and backward
transfer bounds needed for the source proof.

Let \(E_2^\pm,E_3^\pm\) bound the two signed forward coefficient
defects in strict density, and \(J_2^\pm,J_3^\pm\) the two backward
defects in complete causal row norm, including current diagonals.
The supersolution companion proves the sufficient criterion
\[
 \begin{split}
 \mathcal D={}&M^{10}(E_2^++E_3^+)+M J_2^++M^3J_3^+\\
 &+E_2^-+E_3^-+M^4(J_2^-+J_3^-)
 \le H^{-200}.                                          \tag{8}
 \end{split}
\]
It uses exactly the previous positive beta supersolution, reconstructing
backward coefficients by \(W^*-W=a^2LJ_3R^*\). Causal weights in
(7) control the two strict factors around an arbitrary backward row
error. The \(VJ_3V\) term is also retained; it is why (8) charges
\(M^3J_3^+\). Signed coefficients are handled by the positive
finite chronological map, rather than assuming positivity of the
actual nonlinear blocks. The comparison gives strict interior margins
in both sectors.

## 4. Source response with all random sample mixing retained

SECTOR_RESPONSE.md supplies the complete source calculation on that box.
All deterministic coefficient blocks are sector diagonal by the
existing exchange-equivariance induction. Individual random gates mix
the sectors. A scalar enlarged gain is not substituted for those gates.

First, the actual source covariance bounds from Section 2 give inactive
reverse Gaussian scales \(CeM^2,CeM\), and active forward Gaussian
scales \(CM^{-3},CM^{-2}\). The latter follow from (5), the r factors
in the affine active fields, and the sufficient condition
\(eH^{200}M^{16}\le1\). Solving the exact same-array value equations
then gives incoming subGaussian exponents
\[
 q^1:\ M^{10},\qquad q^2:\ M^9,\qquad C:\ M^7.           \tag{9}
\]
These are uniform individual-time norms, not a norm of a random time
supremum. The source derivative exponential consequently requires only
\(eCM^{14}\) small. The numerical condition used below is stronger.

For each local source population, with \(U=(I-a^2KB)^{-1}K\) and
\(L=(I-a^2BK)^{-1}\), the exact derivative identities are
\[
 J-J_{\rm aff}=U[\Delta V I^\zeta+PJ],\qquad
 D\delta-D\delta_{\rm aff}=L[\Delta V I^\zeta+PJ],
\]
\[
 P=L_{\rm gate}+a\Delta V B+aB\Delta G+\Delta V B\Delta G.
                                                               \tag{10}
\]
The gate perturbations are bounded by \(Ce\), and the curvature
term by \(CeQ\). The fixed coefficient arrays and covariances are
frozen in every named-source derivative, as in the original source
construction.

The calculation separates diagonal paths from paths that leave a
sector and return. A sector change introduces a perturbative gate;
a return introduces a second one. Weighted affine kernels bound the
diagonal terms. The off-diagonal terms are estimated with their two
e factors and the already controlled exponential moments. No current
backward factor or terminal feature gate is discarded. Raw L2 bounds
are used after the exponential has been controlled; higher source
moments are used where two unbounded multipliers occur.

The complete sufficient forcing table, including learned moments, is
\[
\begin{array}{c|cc}
 & + & -\\ \hline
 E_2 & H^{200}eM^3 & H^{200}eM^{13}\\
 E_3 & H^{200}eM^5 & H^{200}eM^{11}\\
 J_2 & H^{200}eM^{15} & H^{200}eM^3\\
 J_3 & H^{200}eM^{12} & H^{200}eM
\end{array}                                                   \tag{11}
\]
under \(eH^{200}M^{16}\le1\). Backward row estimates mean
\(\max_k E[\sum_{j\le k}|\text{defect}_{kj}|]\), with the
terminal-time maximum outside expectation. This quantity controls the
row norm of the deterministic expected coefficients.

The companion checks every value, derivative, covariance and numerical
factor. In particular the bounded gate perturbations involving B in
(10) remain present, and the inactive learned backward moments begin
quadratically in e because their affine fields vanish.

## 5. Numerical closure and the complete theorem

By (4),
\[
 M^{16}\le24^4\delta^{-2}.
\]
The unchanged choice (1)--(2) therefore gives
\[
 eM^{16}\le10^{-70}24^4H^{-400},\qquad
 eH^{200}M^{16}\le10^{-70}24^4H^{-200}<1.             \tag{12}
\]
Combining (8) and (11), every term in \(\mathcal D\) is at most
\(H^{200}eM^{16}\). There are eight terms, so
\[
 \mathcal D\le8H^{200}eM^{16}
 \le8\cdot24^4\cdot10^{-70}H^{-200}<H^{-200}.          \tag{13}
\]
The actual largest exponent is 16, from the active middle-backward
term; the active second-forward and top-backward terms cost 15.
It is useful here to retain the numerical factor \(24^4\), rather
than replace it by H and unnecessarily spend another power of H.

At fixed cap and sufficiently fine fixed mesh, continue the actual
source program continuously in amplitude from zero to e. At a proposed
first exit from the box, (11)--(13) apply, and the positive supersolution
puts all inequalities strictly inside. This contradiction closes the
source construction uniformly in cap and mesh.

The remaining original bridges now have their required inputs: bounded
primal feature paths through their endpoint, uniform incoming-field
subGaussian tails, and endpoint prediction at least 5/4. Asymmetric cap
comparison constructs the uncut autonomous strong feature flow; its
first-hit clock constructs one global physical population flow. The
physical comparison retains both actual residuals and proves
nonsymmetric bounded-primal uniqueness and restart from reached states.
No old exponent-four response threshold is imposed after replacing its
source proof by the present one.

At fixed cap/auxiliary mesh, the original Gaussian conditioning,
singular-query, common-action and adjunction arguments apply to the
same model. Width is taken first; deterministic Euler estimates remove
the auxiliary mesh; asymmetric comparison removes the cap. The actual
finite Gaussian readout is retained. Raw GD has its original
\(C_{R,T}n^{-2}\) reference error. No growing-transcript Gaussian law
or cross-width trained operator-norm convergence is invoked.

The original velocity bridge retains product-query truncation and the
order of cap removal at fixed reference-velocity truncation, then
truncation removal. The uncut velocity has a compact continuous L2 time
image. This gives the original velocity/path laws, second moments and
integrated speeds, together with all kernels and both action
orientations. The old absolute regression margin and initial-motion
proof require no further amplitude restriction. The normalization
\((z+r_0\arctan z)/\|G+r_0\arctan G\|_2\) also remains covered for
\(0<r_0\le c_{\rm poly}\delta^2\), since its gain lies in [1/2,1]
and its nonlinear coefficient is at most r_0.

This proves (2)--(3). The corresponding complete three-input theorem
is not a consequence of this proof; THREE_INPUT_ANALYSIS.md records
what is established and the exact remaining global-construction gap.
