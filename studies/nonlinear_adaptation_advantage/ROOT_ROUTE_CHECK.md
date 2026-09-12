# Root's internal reconstruction of frozen routes

Reviewer: root, 2026-09-12. This is an internal mathematical check, not a
promotion review. Root authored the contract and comparator/sampling note,
but did not author the three independent initial routes. Their complete
reports were read only after their authors declared them frozen.

## G: geometry

Complete input read: ROUTE_GEOMETRY.md, SHA256
`e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04`.
Root's complete established dependency scope is in SOURCE_AND_CHECK_RECORD.md.

Checks performed:

- Expanded h=(1-cos(4 alpha))/2. The four fifth/seventh coefficients and
  their perturbation margins in G1–G4 are correct. Swap symmetry makes the
  baseline antisymmetric; the symmetric target component gives the stated
  nonstationarity lower bound on the whole box, independently of its sign
  of curvature.
- Reconstructed the raw projector derivative using B=GM^-1 and the anchor
  Gram bound k/2. The bounds ||Pi'||<=4T_g A_s/sqrt(k), ||d'||<=D_G and
  ||K_prediction'||<=2L D_G follow. Integration yields the actual-trajectory
  unsigned O(T²) discrepancy. It supplies no positive risk comparison.
- Reconstructed G12 by differentiating the scalar prediction along an
  affine raw direction. The row square needs L4, the upper square is L1
  paired with bounded endpoint readout, and the two cross terms are finite
  by L2/HS bounds. These are directional derivatives, not an ambient L2
  second Fréchet derivative.
- Differentiated ||Pi v_r||² holding r fixed, including the derivative of
  the anchor projection. This gives <r,K'_0 r>=-4 C_p(r), and the
  unhalved-loss matched-clock risk term is -8 C_p(r)T². Omitting the anchor
  subtraction would invalidate the comparison.
- Recomputed the Duhamel remainder integrals: integral s²=T³/3 and
  integral s(T-s)=T³/6 give G21; norm factorization gives G22. The
  prediction-orthogonal scalar quotient has ||xi||<=||K'_0 r||, and the
  time shift stays nonnegative under |alpha|T<=1. The constants in G23–G24
  bound the scalar-clock and component interactions as stated.
- Checked both small polynomial-map counterchecks directly: their signs
  agree with the factor -8. They refute general inferences from curvature
  or shape change to benefit; they are not examples of the neural model.

Disposition: the displayed identities and bounds are correct within their
stated scopes. G20 is an unevaluated trajectory-dependent modulus, explicitly
identified as such; it cannot certify the requested positive stop. The
endpoint cubic sign, favorable normalized component sign, and finite-time
positive margins are open. No success claim or promotion inference is accepted.

## H: harmonic structure

Complete input read: ROUTE_HARMONICS.md, SHA256
`43f46b4f15dff0127370765446a92f4c9a15514c3affeee6af9b8018de707225`.

Checks performed:

- The raw swap/readout-sign transformation preserves the reference law,
  the metric and the anchor tangent span. Its kernel commutes with swap
  for swap-invariant densities. This leaves two infinite sectors, not
  individual Fourier frequencies.
- Reconstructed the anchor argument: a continuous function in an odd
  sine/cosine plane that vanishes at both anchors is zero. Since K_0 maps
  into continuous anchor-vanishing predictions and is injective on odd
  L2 residuals, no such nonzero plane can be invariant. The same separation
  proof applies to bounded positive densities: the absolutely continuous
  odd measure has density a p_s, with p_s bounded below. No extra smoothness
  of the density is needed for this particular claim.
- Checked H6's weighted budget using |t+z|+|t-z|=2t when t>=|z|. The
  frequency-1 and frequency-11 components have disjoint Fourier support
  after multiplication by h, norm squared 3/8 and fixed nonzero lower
  bounds. The initial risk lower bound H8 is conservative and positive.
- Reconstructed the density Gram perturbation and inverse-square-root
  bound. The common-metric two-band initial coefficients remain nonzero;
  their normalization has an independent band-recovery interpretation.
  H10 and H15 keep the entire residual, including off-band interactions.
- For H17, B=(K_0 psi) tensor (K_0 psi)/<psi,K_0 psi> obeys 0<=B<=K_0
  by Cauchy–Schwarz in the D_0 image. It is rank one and cannot be
  proportional to injective K_0 on the infinite odd space. Both paths
  K_0±sB are positive on [0,1], preserve the anchors and the swap symmetry.
  Symmetry gives <r_0,B r_0>=a²<psi,K_0 psi>>0.
- Recomputed H18's finite remainder. Duhamel gives error at most
  (10/3)MN sqrt(E0)T³. Risk factorization contributes at most
  (8+20/3+1)MNE0T³<16MNE0T³ for T<=1. Thus the opposite finite-time
  signs follow at the stated stop. These are auxiliary kernel paths;
  no equation identifies them with the actual neural path.
- The matched-sample calculation agrees independently with root's raw
  affine comparator calculation. Its positive conclusion remains
  conditional on the unavailable population margin.

Disposition: the listed structural obstructions and finite-time auxiliary
counterexample are internally checked for their exact scope. They eliminate
Fourier diagonalization and symmetry/PSD/nonproportionality-only proofs.
They do not show failure of H6 on the actual neural trajectory or disprove E₀.
There is no beneficial component or positive total-risk theorem to promote.

## E: finite-time energy and scalar clocks

Complete input read: ROUTE_ENERGY.md, SHA256
`01779adf6e60fde92fb6979c3e421b3bc5061850bc3051399714b7d4aa58993b`.

Checks performed:

- Recomputed the four-feature uniform Gram in E3: diagonal 3/16, cosine
  cross -1/8 and sine cross +1/8. Its smallest eigenvalue is 1/16. The
  resulting coefficient perturbation bound and C1 radius have the stated
  factors. The two symmetric generators have Gram with diagonal 3/8 and
  cross -1/4, yielding the nonstationarity margin E4.
- Reconstructed E7–E13. The actual kernel's time Lipschitz constant is the
  same independently derived bound as in G and H. Subtracting quadratic
  residual forms costs (4L^4+Gamma)R0²t; its integral gives E13's lower
  total-learning bound and upper bound on the relative possible advantage.
- Checked the scalar tanh counterexample by separation of its residual
  equation: strict saturation reduces its scalar kernel, making nonlinear
  risk larger than frozen risk. This is a different model and only refutes
  the proposed generic implication.
- Diagonalized E's noncommuting 2x2 example. A=[[2,1],[1,3]] has smaller
  eigenvalue (5-sqrt(5))/2 and e2 overlap (1-1/sqrt(5))/2. Their lower risk
  bound exceeds exp(-8) by the stated elementary inequalities. The smoothing
  error is at most 2||C||delta by Duhamel and contraction. Thus even Loewner
  enlargement does not imply the required finite-time order in general.
- Reconstructed E16. Frozen risk dissipation bounds its norm's derivative
  away from zero throughout the stated scalar-clock budget. This bounds
  the minimizing clock's distance from T by 2Gamma T²/lambda; projection
  removes the frozen velocity, and its second derivative gives the
  8L0^4 R0 Gamma² T^4/lambda² remainder. The positive transverse displacement
  needed to use this criterion is not proved. The criterion itself asserts
  no stronger risk superiority to task-specific clock tuning.
- Verified the frozen empirical Hilbert forcing bound and its factors of
  two and L0, agreeing with root's separate derivation.

Disposition: these exact finite-time criteria, bounds and proof-rule
counterexamples pass internal reconstruction. The actual signed neural
interaction and beneficial component sign remain open. The pointwise kernel
order counterexample concerns a different flow, not the E₀ network.

Typographical clarification for the unchanged frozen E report: its opening
description of the raw norm as a sum of squares means the **squared** raw
norm. Its formulas and this study's metric contract use the correct metric.
This does not alter any stated bound or scientific conclusion.

## G follow-up: readout and tanh saturation balances

Complete input read: GEOMETRY_SIGN_FOLLOWUP.md, SHA256
`7400b12eb9655a24f8ba23af2fd41b60733947ca5fc184850d2629eafd980719`.

Checks performed:

- Differentiated the projected force with both the anchor span and residual
  changing. The normal term in B8 and all factors in B9 are retained.
  Pairing the actual acceleration with the readout direction gives B10;
  swap parity removes only the displayed residual-feedback cross term in
  its pure symmetric diagnostic. The two anchor/curvature contractions
  remain at the same order as the positive squared norm.
- Recomputed the reference contrast factors My=2B_s y and
  GM^-1 y=g_B/B_s. These give precisely B11. Positive B_s does not
  determine the numerator's sign.
- Checked the finite renormalized middle-action quantity in B12. The raw
  initialized Gaussian action is bounded but not assumed Hilbert–Schmidt.
  The reached increment is nuclear: its reference and selected velocities
  are integrable rank operators. The trace pairing with the initialized
  action is continuous in the nuclear norm. Thus differentiation of B12
  uses finite terms, not a difference of undefined infinite norms.
- Substituted the actual middle and row velocities and the actual adjoint
  into the norm derivatives. This yields B13–B14 with the factor -4.
  The scalar tanh defect is odd, bounded by one and nondecreasing, but its
  multiplier and signed control measure prevent a sign inference.
- Directly differentiated the quadratic prediction energy under the
  additional hypotheses explicitly stated in B15–B16. The coefficients
  -48 and +4 in B15, and 8 in B16, are correct. The positive square in
  B16 has a same-order signed partner. These conditional identities prove
  neither the extra derivative hypotheses nor a finite E₀ margin.
- Confirmed the follow-up returns to the original fixed family. Its
  reference residual cannot be made small merely by decreasing the family
  coefficient scale, and the symmetric diagnostic is not a new target
  family centered on the trained prediction.

Disposition: exact reached-curve balances are internally checked. No actual
favorable sign, beneficial component inequality or successful E₀ theorem
follows. The frozen original routes and family definitions are unchanged.

## Cross-check reports read by root

Root read INTERNAL_CROSSCHECK_E.md, INTERNAL_CROSSCHECK_H.md and
INTERNAL_BALANCE_CHECK_H.md completely, including scope and caveats. Their
input hashes match the frozen files. All give no required scientific
correction within their assigned scope; none claims E₀ is proved. The last
report's explicit rank-series construction additionally verifies the trace
legitimacy in B12, with ||K_dagger||_nuc<=50 and selected increment at most
c_b A_s tau. All report and input hashes are in SOURCE_AND_CHECK_RECORD.md.

All checks above are manual algebraic reconstruction against complete frozen
inputs and the recorded established sources. No numerical training or formal
proof checker was used. The rational upstream certificate has a separate
executed check. These checks are internal, not independent promotion reviews.
