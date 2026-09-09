# The explicit mixing coefficient with exponent ten

2026-09-07. Complete candidate assembled for independent adversarial
review. Current review status is recorded in REVIEW_STATUS.md. All
earlier theorem files remain unchanged.

## 1. Statement and the same explicit prefactor

Retain the precise model and complete conclusion of
../two_sample_odd_activation_theorem/PROOF.md: two deterministic
RMS-unit inputs, all binary labels, three hidden layers, the independent
Gaussian initialization with its original finite readout, the raw
gradient metric and simultaneous raw GD with step \(n^{-2}\).

Let \(c_*,C_0,C_z,C_g,C_B\) be the explicit constants in equations
(9), (10), and (15) of
../two_sample_odd_activation_quantitative/PROOF.md. Thus
\[
C_0=1296000\exp(1404),\qquad C_z=1500C_0,\qquad C_g=14400C_0,
\]
\[
H=C_B=10^{30}(1+C_0+C_z+C_g+\exp(1410))^4,\qquad
c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}.          \tag{1}
\]
Here H is a numerical constant, not a time integration operator.

For every \(0<\delta\le1\), every dataset with
\[
\|x_i\|^2=d,\quad
|\langle x_1,x_2\rangle/d|\le1-\delta,\quad
y_i\in\{-1,1\},
\]
and every
\[
1/2\le a\le1,\qquad 0<e\le c_{\rm poly}\delta^{10},
\qquad \phi_{a,e}(z)=az+e\arctan z,                  \tag{2}
\]
the complete original theorem holds. In particular,
\[
\theta_\delta=c_{\rm poly}\delta^{10},\qquad
\phi_\delta(z)=(1-\theta_\delta)z+
                       \theta_\delta\arctan z       \tag{3}
\]
is admissible, and every smaller positive mixing coefficient is
admissible as well.

The conclusions include one autonomous global strong population flow,
uniqueness against bounded-primal nonsymmetric competitors on the same
canonical action spaces, restart from reached states, and the
full-width-sequence GF/raw-GD population limits on every fixed finite
physical interval. All four raw kernel matrices, action orientations
and adjoints on generated probes, the original same-layer feature/path/
velocity laws and second moments are retained. Activation regression
nonaffinity holds at every finite physical time; the original initial
hidden-block and sample/layer motion certificates are retained.

The activation depends on delta alone. Neither uniform width convergence
over datasets or over the infinite time half-line, nor a three-input
extension is asserted. The numerical prefactor in (1) is exactly the
one previously used with exponent 800 and remains extremely small.
This result improves the separation exponent. It proves neither a
practical-size prefactor nor optimality of exponent ten.

## 2. Inputs and the correct intrinsic scale

Fold labels exactly using oddness. Let
\[
v=(1+y_1y_2\rho)/2,\quad r=\sqrt v,\quad
\lambda=a^3r,\quad
M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\tag{4}
\]
The affine companion reaches prediction \(3/2\) on a feature interval
of duration \(S_{\rm time}\), with
\[
S_{\rm time}\le2/\lambda\le M^4,\quad
r=\frac3{\sqrt2a^3}M^{-4},\quad
M\le24^{1/4}\delta^{-1/8}.                           \tag{5}
\]
The exact balances and integrated Hessian estimate of
AFFINE_POLYNOMIAL_BOUNDS.md in the earlier quantitative directory give
raw primary sizes \(CM\), affine variational propagator \(CM^5\), and
cap-uniform nonlinear raw discrepancy \(CeM^{12}\).
The forward preactivation discrepancy is \(CeM^{14}\).
Every learned-moment coefficient discrepancy is at most
\(CeM^{15}h_j\); a backward row sum costs at most \(M^4\).
All these input coefficients are at most H.

The earlier comparison, endpoint and nonaffinity restrictions are
already satisfied: (2) implies \(e\le c_*\delta^{7/4}\).
It therefore gives the original radius-one tube, the endpoint margin
\(g_e(S_{\rm time})\ge5/4\), and the same absolute Gaussian regression
margin used in that proof. The only new obligation is the source
estimate on this longer admissible amplitude interval.

AFFINE_SOURCE_CERTIFICATE.md proves the needed actual affine source
bounds. Its notation \(m\) is M in (4); its uppercase M is only the
uniform upper envelope in (5). It uses exact time/sample normalization
to establish the bounds, then converts back to the original feature
time. No rescaled optimizer is used.

Use the original strict density norm
\(|U|_d=\max_{j<k}|U_{kj}|/h_j\) and causal row norm
\(|Q|_r=\max_k\sum_{j\le k}|Q_{kj}|\), including the current diagonal.
The required safe bounds are
\[
|A_2|_d,|F|_d\le HM^5,\quad
|A_3|_d,|V|_d\le HM^7,
\]
\[
|B_3|_r,|T|_r\le HM^9,\quad
|B_2|_r,|W|_r\le HM^{11},                            \tag{6}
\]
and all forward/backward source resolvent rows are at most \(HM^{11}\).
The top strict transfer has density at most \(HM^9\). The source
Gaussian standard deviations have the respective elementary powers
\(1,M,M^2\) given in REFINED_RESPONSE.md.

The same bounds hold at the intrinsic enlarged initialization scales
\[
\beta_j=1+\frac{j}{10^6(200+M^2)},\quad j=1,2,3,
\qquad
\beta_{\rm far}=1+\frac1{10^5(200+M^2)}.              \tag{7}
\]
Adjacent gaps are at least \(H^{-1}M^{-2}\); all scaled affine paths
exist on the same original interval. These scales are proof devices
and may depend on the data. The activation in (3) does not.

The certificate proves the additional source bounds through explicit
Gaussian coordinate probes at fixed programs, including the first
preactivation and top backward answer. It retains their current direct
terms and both orientations, and takes the probe-amplitude limit after
the fixed-program identification. It does not differentiate through a
width limit or infer a coefficient bound from a raw tangent without
that probe identity.

## 3. Positive coefficient comparison replaces the large inverse bound

POSITIVE_SUPERSOLUTION.md contains the complete deterministic argument
and its numerical ledger. We state the mechanism and its precise
interface here.

In the sample mean/contrast basis every actual deterministic coefficient
block is diagonal. This follows by induction through the exchange-
equivariant finite source program, including expected formal derivatives.
The individual random gates still mix sample sectors. No symmetry
assumption is imposed on physical competitors.

At an affine Gaussian initialization scale beta, the four coefficients
satisfy
\[
\mathcal C_\beta=\beta^2\mathcal T_0(\mathcal C_\beta)
                         +\mathcal M_\beta,\qquad
\mathcal T_0=(F,V,T,W).                              \tag{8}
\]
The active entries and learned moments are nonnegative polynomials in
beta, by Wick positivity and the exact chronological source recursions.
Differentiating the A3 equation, and using the enlargement in (7), gives
\[
R_\beta F_\beta L_\beta
 \le\frac{\partial_\beta A_{3,\beta}}{2\beta^3a^2},
\quad
|F_\beta L_\beta|_d,\ |R_\beta F_\beta|_d
                                         \le H^3M^9. \tag{9}
\]
The active leading terms also satisfy
\(F_{\beta,kj},V_{\beta,kj}\ge H^{-1}M^{-8}h_j\).

For arbitrary nonnegative backward row errors \(J_3,J_2\), fix
\(\beta=\beta_1\) and set
\[
A_2^*=A_{2,\beta},\quad A_3^*=A_{3,\beta},\quad
B_3^*=B_{3,\beta}+J_3,
\]
\[
R^*=(I-a^2A_{2,\beta}B_3^*)^{-1},\quad
W^*=a^2B_3^*R^*,\quad
B_2^*=B_{2,\beta}+(W^*-W_\beta)+J_2.                 \tag{10}
\]
The two backward supersolution inequalities are exact. For the forward
ones the identities
\[
W^*-W_\beta=a^2L_\beta J_3R^*,\qquad
F_\beta(B_2^*-B_{2,\beta})F_\beta
=F_\beta J_2F_\beta+
 a^2(F_\beta L_\beta)J_3(R^*F_\beta)                 \tag{11}
\]
retain strict factors on both sides of every arbitrary row error.
The strict/row/strict sandwich estimate preserves \(h_j\), without a
smallest-step assumption. The positive scale margin \(\beta^2-1\)
absorbs the resulting forward errors. Signed actual coefficients are
handled by
\(|\mathcal T_0(\mathcal C)|\le\mathcal T_0(|\mathcal C|)\).
Finite chronological comparison then gives the desired majorant.

The inactive affine backward coefficients vanish. Its forced equations
close directly with backward rows \(O(q)\) and additional forward
density \(O(M^4q)\). This is proved separately; no active-only assertion
is used for that sector.

The precise numerical closure criterion, including the outer-box
margin, is
\[
q\le H^{-16}M^{-34}.                                \tag{12}
\]
Here q bounds both forward strict-density defects and complete backward
row defects, including current diagonals. The outer box uses
\(\beta_2\) for active forward majorants and backward excess radius
\(H^{-10}M^{-12}\). The supersolution at \(\beta_1\) is strictly
interior to that box under (12). The active forward comparison alone
needs power 32; the complete backward margin needs power 34.

## 4. Nonlinear defects without the old exponent losses

REFINED_RESPONSE.md proves, on the preceding outer box,
\[
q\le H^{30}eM^{43},\qquad
 \text{provided } eH^{22}M^{32}\le1.                 \tag{13}
\]
This includes the independently bounded learned-moment errors.
The source value equations are first solved with their exact affine
resolvents at the same coefficient arrays. Their remaining nonlinear
self terms have a factor e and are absorbed. In particular,
\[
\|q^1_k\|_p\le H^{10}M^{22}\sqrt p,\quad
\|q^2_k\|_p\le H^{10}M^{21}\sqrt p,\quad
\|C_k\|_p\le H^{10}M^{17}\sqrt p
\quad(p\ge2).                                      \tag{14}
\]
These give cap/mesh-uniform subGaussian incoming fields.

The key derivative improvement is an exact backward identity.
For a local source population write
\[
Z=\xi+K\delta,\quad q=\zeta+Bh,\quad
h=\phi(Z),\quad \delta=D_{\rm cap}(Z,q).
\]
Let
\[
U=(I-a^2KB)^{-1}K,\quad L=(I-a^2BK)^{-1},
\]
and let P collect the gate perturbations, each containing e or e times
an incoming field. With coefficients and covariances frozen, the
derivative differences satisfy exactly
\[
J-J_{\rm aff}=U[\Delta V I^\zeta+PJ],\qquad
D\delta-D\delta_{\rm aff}
                      =L[\Delta V I^\zeta+PJ].       \tag{15}
\]
Thus the final backward estimate uses L directly. Separately bounding
the terms before this identity would waste additional powers of M.

The strict U kernels produce an exponential derivative envelope whose
exponent is proportional to e, with deterministic time weights.
Weighted Jensen and (14) bound its required fixed moments under
(13). There is no random supremum over source times. The complete
forward-source row and the single transpose-source entry are estimated
in their respective norms; current backward factors are included.
The largest resulting defect is the middle backward row:
\[
e\underbrace{M^{11}}_{\text{backward resolvent}}
 \underbrace{M^{11}}_{\text{forward derivative row}}
 \underbrace{M^{21}}_{\text{incoming field}}
=eM^{43}.                                         \tag{16}
\]
The companion proves all other rows, source-time factors, moment
products and numerical prefactors in (13), rather than treating (16)
alone as a proof.

## 5. Closing the constants and transferring the complete theorem

By (5), \(M^{80}\le24^{20}\delta^{-10}\), and \(24^{20}<H\).
Consequently (2) and (1) imply
\[
eM^{80}\le10^{-70}H^{-400}24^{20}
                         \le10^{-70}H^{-399}.       \tag{17}
\]
This gives \(eH^{22}M^{32}\le10^{-70}H^{-377}\).
Using (13),
\[
qM^{34}\le H^{30}eM^{77}
                     \le10^{-70}H^{-369}<H^{-16}.   \tag{18}
\]
The amplitude homotopy at each fixed cap and mesh starts at the
affine coefficients. On a proposed first exit from the outer box,
(13) and (18) apply, and the supersolution makes all box inequalities
strict. This contradicts first exit. The estimates therefore hold on
the full source program, uniformly in cap and sufficiently fine mesh.
No probability theorem for growing transcripts is invoked.

All prerequisites for the old construction and limit bridges are now
available: bounded primal feature paths, cap/mesh-uniform subGaussian
incoming fields, and endpoint prediction exceeding one. Their actual
proofs apply with the new constants. The asymmetric cap comparison
removes the cap and proves strong path/direction convergence. The
population scalar clock produces one global physical flow. Physical
comparison retains both residuals and gives uniqueness against
nonsymmetric bounded-primal competitors and restart from reached states.

The finite-width identification keeps the original initialized readout.
It takes width at fixed cap and auxiliary mesh, removes the auxiliary
mesh by deterministic Euler estimates, and then removes the cap.
The prescribed simultaneous raw GD contributes \(C_{R,T}n^{-2}\)
at fixed cap and finite physical horizon. The original velocity proof
truncates product queries, removes caps at fixed reference-velocity
truncation, and only then removes that truncation. The continuous
uncut velocity's compact L2 time image supplies uniform tails.
Thus all the original action, adjoint, kernel, path, velocity and
second-moment conclusions are preserved.

Finally, the prior absolute regression margin survives the strong
limits, and the original odd-family initial-motion argument works for
every positive e in the gain rectangle. Neither step imposes another
angle-dependent restriction. This completes the full theorem under
(2), hence the convex-mixture assertion (3).

The sufficient exponent ten is not asserted sharp. The proof also
does not improve the deliberately conservative numerical prefactor.
