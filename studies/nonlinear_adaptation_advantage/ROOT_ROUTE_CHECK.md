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

## Continuation: actual-reference sign and quantitative remainder

Root completely read REFERENCE_SIGN_ATTEMPT.md, SHA256
`6cfef322be7e9ee1d49c8287e3bfd94e6069c17ce40dfdf6619745472c1afa6f`.
The five terms in R5 follow by expanding the two readout-linear Hessians;
R6–R7 follow by the exact reference history and integration by parts.
Root checked the hidden mixed-term norm in R9 using the two-dimensional
row/middle Cauchy–Schwarz inequality. The absolute bounds in R10–R12 have
the stated factors, and the lower bound greater than 120/11 is a lower
bound on the *certificate's right-hand side*, not on the unknown actual
ratio. The PSD readout diagnostic has the stated signs. R13–R14 retain
the whole task and reference history. No required scientific correction
was found, and no actual favorable sign was inferred.

Root authored the frozen QUANTITATIVE_CURVATURE_DRIFT.md, SHA256
`5bfd6b4c1683d172e3c7a543e8b9e7faa17b2b14f0299ea4242a3776cbcee7d5`.
Its new directional forward-query fourth moment uses CT29's *whole-history*
pulse bound, two gate terms, current direct injections, and the old memory
row sum. It does not invoke an Lp action norm. The scalar-Hessian drift
then uses the new L4 bound only for the upper curvature product; all other
differences use already proved L2/L4 state and direction bounds. The
changing anchor measure and changing residual both contribute to Q12.
This yields an explicit operator time-Lipschitz modulus and finite risk
remainder, with source conditioning still unevaluated.

Root read SOURCE_MOMENT_AUDIT_H.md, QUANTITATIVE_DRIFT_CHECK_G.md and
QUANTITATIVE_DRIFT_CHECK_H.md completely, including provenance and boundary
checks. All three independently reconstructed their assigned claims and
reported no required correction. Their input hashes match the frozen
candidate and established sources. The H full check explicitly retains
G24's separate |alpha|T<=1 condition when using the scalar-clock remainder.
These reports validate the new quantitative lemma internally; they do not
provide the absent signed coefficients or satisfy promotion review gates.

Root also read all 749 lines of CURVATURE_CERTIFICATE_REDUCTION.md, all
388 lines of CURVATURE_CERTIFICATE_CORRECTION.md, and the complete
CURVATURE_REDUCTION_CHECK_G.md. The original's coarse clock constants,
source pulse amplification, derivative cutoffs, projector products,
Gaussian square-root bound and tail quadrature argument were reconstructed.
The G check correctly identified that arbitrary polarization sums need
their own residual and endpoint-approximation constants and effective
spatial input data. The separate correction supplies these in P1–P15,
including all downstream force and derivative bounds. Root verified the
1/48 and 27/48 polarization factors and error multipliers E/6 and 9E/2.
Root read the fresh full CORRECTED_CURVATURE_CHECK_H.md completely at SHA256
`610b59c30f840ada4185f344dccc1ca6fbb8b895955fcaac7e475eb87fc7f24b`.
It finds no remaining required correction when the original and correction
are used together. Root verified the report's input hashes and reconstructed
its additional explicit conventions: the spatial error for the projected
derivative includes the normal-projector term, and the Gram search finds
and then retains some certified positive gap. No numerical curvature
enclosure was executed. Arbitrary-accuracy approximation is not
a general exact-zero decision procedure; a certified zero would require an
additional exact argument. The central unchanged-family approximation and
the corrected auxiliary probes must be distinguished from a negative sign
certificate, which is still absent.

Root read ROUTE_GAUSSIAN_SIGN.md completely at SHA256
`2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c`.
The actual reference limit c(s)/s=(tanh X+tanh Y)/2 uses Y=-Z2(0)
and the even upper derivative, so both mixed-covariance rows have the
claimed signs and factors. Root rechecked the contained A.3 Gaussian
Poincaré proof and its variance scaling: Var(S)<=4v0 E[T²S²], giving
eta-mu²<=-2D/5 from v0<.4. Gaussian integration by parts proves eta>0.
The event 1<=|G|<=2 gives G8's positive lower bound. Gate derivatives and
G10's two signs were recomputed. The physical covariance uses fixed actual
initial observations, avoiding an assertion about representation-dependent
individual response coefficients. Kernel block/projector identities and
the first/third harmonic swap signs in G16–G17 were also reconstructed.
No actual endpoint or added-data sign follows. Root read the complete
GAUSSIAN_SIGN_CHECK_G.md at SHA256
`a715b568e4837eb4a241f9d8894eeaa5de97203addf665c9978c2a40cf4d5ea7`
and verified its frozen input/source hashes. It finds no required correction
and independently reconstructs the variance factors, strong-limit argument,
source ambiguity, full-kernel symmetry and density caveats. Its density
example has weighted cross-sector inner product epsilon/2, as direct
integration confirms. These are checks of the route's exact limitations;
no source beyond the recorded established units was imported.

## Further bounded sign follow-ups

Root read PARITY_SIGN_REDUCTION.md completely at SHA256
`41767114a3d7a6dd81c519eee306f06107bc6f4ca1c538b9f751b34b499d10c1`.
The actual raw symmetry acts on predictions by minus the coordinate swap,
so the polarized cubic vanishes precisely in the 16 formal slots with an
odd number of swap-symmetric arguments. Root enumerated the remaining ten
AAA and nine ASS slots and expanded the polynomial independently. Its
constant, linear, quadratic and cubic monomial counts are 1, 2, 6 and 10.
The inverse coefficient change gives the exact coupled domain P12, not an
independent rectangle in the four new coordinates. The worst sign of w
retains 2|q12|z|w|, and the original midpoint has y=R/32, z=3R/32, giving
the factor 27R²/1024 in P19. No sign of a surviving actual-neural entry is
provided. The necessary midpoint test concerns the proposed uniform
negative-cubic proof, not every possible finite-time E₀ theorem.

Root read all 602 lines of GAUSSIAN_SIGN_TRANSPORT.md at SHA256
`5f44ec005410cbdfa4557580c243ea77c1abce6a067882a722d2552578cb484c`.
For its source specialization root reread global_nonlinear.md 6310–6521
and special_data_limits.md 3860–4053, within the previously complete units.
The label-oriented change v2=-w2 gives two plus-sign feature updates and
the exact first-row term A(sech⁴(v_a)A*delta_a)/2. Root reconstructed both
covariance derivatives, the integrating factor, and the bounds T11–T13.
The fitted feature time is at least one because |c|<=s and |h|<=1.

The localized source bound has Q L4 norm at most C_Q s: the old response
sum, learned ranks and current injections each carry the horizon factor S,
and the source standard deviation is at most S. Integrating the full-row
equation gives an L4 displacement of order s². Root then checked each
product subtraction in T21–T23, including the tanh remainder bounded by
the squared row displacement. This yields a strong L2 remainder O(s⁴),
without an ambient Hessian or an assumed Taylor radius.

The two initial reverse responses have the stated eta/2 and mu²/2
coefficients. In the appended forward query the response is
bar_m(d1-d2), which must be retained. The reverse-Gaussian part of the
new input is conditionally centered given the first-row root, hence
orthogonal to every root-only function. Its covariance lower bound is
2(gamma_d-gamma_o)E sech⁸G>0. This proves a nondegenerate forward innovation
independent of the initial X,Y by Gaussian projection, without treating
actual forward and reverse answers as independent. Root verified the
event probability of order s², the leading negative difference of order
s², and the O(s⁴) probability bound for remainder failure. They prove the
actual pointwise ordering-cone failure for every sufficiently small fixed
positive feature time. The earlier expected negative covariance remains
compatible with that event. Root read the complete separate
GAUSSIAN_TRANSPORT_CHECK_H.md at SHA256
`6f751bc7879b9598220690a6c11346533081c98723edb5886095d8f15ea5d4a9`.
It finds no required correction. Root reconstructed its explicit constants
H1–H4, the variance projection H5, and the probability lower bounds H6–H7,
and verified every recorded scientific input hash. The report was written
before root sent its agreement message. The cone implies a nonpositive
expected covariance; strict negativity additionally requires a positive
integral. The crossing theorem's fixed-time quantifier does not assert one
positive-probability event crossing at all arbitrarily small times.

Root also checked the scale of C3–C5 in the corrected endpoint reduction.
For a mesh covering [0,10] with N intervals, h>=10/N. Even with exact
Gaussian integrals, the displayed bound can be at most 1/100 only if

    N >= 580093872438150000 exp(286740) > 10^122903.

Indeed L²=340011, 1+20L²=6800221, and the nonnegative first term of C5
alone gives the necessary inequality. The last strict bound uses
sum_{k=0}^{11} 7^k/k!=2959911103/2851200>1000 and
floor(286740/7)=40962. These integer/rational calculations were checked
with Python's standard Fraction arithmetic, exit 0, from the repository
root. No Gaussian integral, reference trajectory, or training was computed.
This is a limitation of the stated error bound, not a lower bound on the
actual number of steps needed by a sharper certified approximation.

## Completed checks retained at the user-directed stop

Root completely read and reconstructed EXPECTED_SIGN_ATTEMPT.md at SHA256
`c88d6eab7be97171e1fd36ff0cf17ce7573d90744a2e645205f35dca6d1a048d`
before the stop. The normalization by v0, differentiation through every
named source slot with fixed coefficients, and endpoint passage of the
whole invariant mixed moment were checked. Canonical-expression symmetry,
not value-law symmetry alone, is needed at singular source covariance.
The auxiliary delay solution, rational positive covariance bound and smooth
memory stability estimate were reconstructed. They give no neural endpoint
sign. At closure root read the completed EXPECTED_SIGN_CHECK_H.md in full,
SHA256 `7fdc1a0af50e1acc41be520516898322f8904ec63d540e45a54621fcc1bdf0e0`,
and verified its input hashes. It finds no required correction, retaining
the same scope. Its scientific check was completed before the stop.

Root completely read FAMILY_SIGN_ATTEMPT_H.md at SHA256
`ba2131a746324a05e9bcec684d96082571c0138e2edd95524960da7291ed3ecb`
before the stop. The polarized mixed-cubic factors, anchor-normal subtraction,
and exact conditional coefficient averages on the coupled domain were
reconstructed. The favorable hidden-force square has same-order unsigned
partners. The averaging identity does not imply a uniform sign. No actual
hidden-force coercivity or favorable neural comparison was accepted.

Root authored VARIANCE_ARGUMENT_CHECK.md at SHA256
`40942327a54d47fef88a7d644590f7767c57c2ab5b94026af8069d4d03d00209`.
Before the stop root checked its scalar invariant, full tangent kernel,
continuation, exact Fourier Gram and whitening, anchor-preserving projection,
and finite adverse gap over the original unperturbed coefficient box.
Root read VARIANCE_CHECK_G.md completely at SHA256
`f35de5480ad9ab00688ea66fda052851caf89b2a34fc94fd41ca0598993de7d1`
and checked its input hash and exact constants. The report finds no required
correction. This is an auxiliary-model obstruction to a generic variance
argument, not an E₀ counterexample. No training or neural integration was run.

All five files are preserved at their frozen hashes. These are internal
checks, not promotion reviews. The user stopped the proof campaign on
2026-09-12; closure work only records and commits already completed results.
The uniform positive population margin and beneficial component effect
remain unproved. No further research is authorized by these notes.
