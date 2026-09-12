# Internal check of the endpoint curvature certificate reduction

Checker: `/root/geometry_route`, 2026-09-12.

Checked frozen input: `CURVATURE_CERTIFICATE_REDUCTION.md`, all 749 lines,
SHA256 `24a69ef255c14e15cfb666332ea0f772ed9ae8deeb74938b6450ffb7f9918039`.
The input has not been edited. This is a scoped internal mathematical check,
not an independent promotion review or an evaluated numerical certificate.

## 1. Verdict and required correction

**The central reduction passes for the unchanged geometry family and its
specified finite approximations. The advertised arbitrary-probe extension
requires an explicit scope correction.** I reconstructed C1–C27, including
the clock error constants, retained source history, derivative tails, anchor
projection, covariance singularities, and the termination argument. I found
no additional substantive defect in the central-family approximation claim.
No favorable cubic sign, finite-time advantage, or E₀ theorem follows from
this check.

The correction concerns the sentence at input lines 48–50 allowing “any
bounded fixed r, including polarization probes,” and its use at lines
699–704. Several later constants specialize to

\[
r=F_*-q,\qquad |q|\le1,\qquad
\|r\|_\infty\le B_0=\sqrt{10}+1,
\qquad \|r-\bar r\|_\infty\le L\delta.
\]

These specializations occur in the force error after C9, the row error
after C12, and C18. They do not apply unchanged to arbitrary signed sums
of such residuals. For example, three-term polarization probes have the
available bounds

\[
\|r_\varepsilon\|_\infty\le3B_0,
\qquad
\|r_\varepsilon-\bar r_\varepsilon\|_\infty
\le3L\delta
\]

when each summand contains an approximated copy of the endpoint predictor.
The exact coefficient of that predictor can sometimes improve the second
bound, but it must be accounted for. The C18 product subtraction requires
the actual residual bound multiplying the derivative-feature error; the
displayed fixed coefficient B0 cannot simply be retained. The example
choice of U after C11 and all bounds derived from V_*, B_beta and U must
also cover the probe under evaluation. The polarization identity itself,
including its factor 1/48, is correct.

A sufficient repair is to declare for every permitted probe an explicit
bound B_r, an endpoint-residual error e_r, and a spatial modulus, and use
these in each force, direction, projection and cubic error. In particular,
the two specialized state errors become

\[
e_v^{\rm state}\le L e_r+B_r e_g,
\qquad
e_{v_w,4}^{\rm state}\le Q_4 e_r+B_r e_{g_w,4},
\]

and C18 uses B_r in place of B0. Alternatively, one can normalize probes
and propagate the resulting linear and cubic scale factors explicitly.
This check does not silently make either repair to the frozen input.

The same scope sentence also needs an effectiveness qualification. A bound
on an arbitrary measurable r alone gives neither a spatial quadrature
modulus nor computable integral data. Explicit finite combinations of the
given Lipschitz dictionary and rational net representatives do supply these
data. The claimed uniform-family reduction by computable finite nets is
not affected: it covers arbitrary members of the original family without
requiring an algorithm to query each member separately. Effective evaluation
of an individually supplied arbitrary input instead needs an effective
representation or suitable integration oracle. This is part of the same
probe-scope correction, not a counterexample to the central-family result.

## 2. Exact reference approximation and its constants: C1–C7

The sign and factors in C1–C2 are correct. In the direction b, the actual
initial velocity is -2b. Differentiating the full projected feature map
therefore gives D'_0 a=-2 integral a dot-d_b p, and
<r,K'_0 r>=-4 C_p(r). The anchor Hessian subtraction remains present.

The coarse clock calculation is valid in the sum metric stated in §2.
The three column sums of the velocity comparison are bounded by
2862s+32, 12+108s, and 54. On [0,10] they are at most Lambda=28674.
The speed bound is ac+c+1=595. Summing the Euler defects
Lambda V h_j²/2 and applying the scalar discrepancy recurrence gives
C4 for arbitrary step sizes with maximum h. The one-Lipschitz property
of J in its clock coordinate transfers this bound to raw state distance.
The enormous exponential affects practical cost, not validity.

For C5, a grid point within h of the true fitting clock has exact fitting
error at most L²h. Minimization over the approximating program increases
this to at most L²h+2L delta_h on the exact curve. Since the fitting
observable has derivative at least m0, the clock displacement is bounded
by this quantity divided by m0; multiplying by the raw speed L and adding
delta_h gives the displayed delta_end. Certified scalar fitting errors
add precisely 2L epsilon_b/m0. No task-performance criterion enters this
selection, and the whole curve remains on [0,10].

I reconstructed the retained-source estimate C6 as follows. The time
integral of 54+2862s gives the exponent 54S+1431S². A forward source pulse
has initial clock discrepancy at most h_j P; its effect on a later passive
delta query is at most h_j P K_q E. Two anchor slots summed over total
clock length S give 2S P K_q E. The learned-rank contribution is bounded
by S c² and the immediate response by 2S. A reverse source pulse enters
the relevant clock coordinate with coefficient h_j/2. These are the
orientations and weights required by the established source recursion.
They do not create fresh independent sources after previous queries.

The enlargement from unforced action/readout bounds 52 and 10 to a=53,
c=11 supplies the slack needed by the small-forcing argument. Finite-width
source extraction is performed at a fixed graph before the forcing tends
to zero. The sharp initialized-action convergence in the allowed A.3
source, together with the finite-rank limit, supplies this slack; replacing
it by only a cruder finite-width operator bound would not be the same
justification.

C7 then follows from Minkowski's inequality and the Gaussian moment
formula. In particular E|G|^8=105 and E|(g1,g2)|^8=384. Integrating the
clock velocity gives the stated W_j bound for j=2,4,8. This establishes
moments for the actual passive Q queries, not an L4 or L8 operator norm
for A0 or its adjoint. The distinction is maintained in the later proof.

## 3. Base features, controls and directional derivatives: C8–C18

The base-field subtraction in C8 is valid on the common carrier. The
changed first gate has L4 norm at most sqrt(2) sqrt(delta); multiplying
by the uniform Q4 bound gives the only non-Lipschitz term in e_g.
The C9 interpolation exponent is correct:
1/4=(1/3)/2+(2/3)/8. Its other term uses the first-gate difference in L8,
bounded by 2^(1/4) delta^(1/4), and Q8. This supplies the stronger row
norm needed for the Hessian contractions.

The Gram perturbation bounds are e_G=sqrt(2)e_g and e_M=4L e_g.
A lower enclosure for the approximating Gram eigenvalue exceeding
e_M+gamma certifies both gaps. The projector bound
e_Pi=2sqrt(2)e_g/sqrt(gamma) follows from the subspace projection
difference identity. Expanding the two inverse-Gram factors gives exactly
the three terms of e_beta in C10; the projected force bound e_b follows
by one further subtraction. Eventual success uses the established strict
anchor Gram gap, not an unevaluated guessed numerical value.

With the actual measure bound U in C11, the row, middle and readout bounds
for b are correct. C12 correctly subtracts the anchor coefficients and
the row features separately. The supplied U example and specialized
force errors pass for the original family. Their unrestricted use for
polarization probes is precisely the correction in §1 of this check.

I differentiated all three feature components in C13. Both terms in the
upper preactivation direction, both terms in delta_z, both actual adjoint
terms in Q_z, and all three raw feature blocks occur with the proper
coefficients. C14 follows by L2 operator bounds, row L4 products, and the
readout supremum. It assumes no Lp action estimate and covers both the
exact and approximating fields under the declared common bounds.

The two tail terms in C15 are necessary and sufficient for the displayed
comparison. Changed bounded multipliers paired with bar B_z or bar Q_z
are split at R. The low part uses the raw multiplier difference times R;
the high part uses the multiplier supremum times the corresponding L2
tail. The row term involving the difference of phi'' uses

\[
\|\phi''(w\cdot u)-\phi''(\bar w\cdot u)\|_4
\le\sqrt{24}\sqrt\delta,
\]

which follows from supremum 4 and Lipschitz constant 6. Its other two
factors are controlled by Z8 and Q8. The terms involving direction error
use e_(z,4), not merely raw e_z. I checked the separate e_a, e_B, e_D,
e_Qz, row, middle and readout bounds. No derivative-answer L4 estimate
has been substituted for either tail.

C16 differentiates both anchor geometry and the off-anchor feature.
Writing the pseudoinverse as M^-1 G*, the bound for its difference is
e_BG. Subtracting the formula
dot-Pi=-Pi dot-G M^-1G* minus its adjoint gives the three displayed
terms of e_(dot Pi). The final dot-d error contains all four necessary
terms: changed Pi, changed dot-g, changed dot-Pi, and changed g. Thus the
certificate does not discard the fitted-reference controls.

The finite-rank D' certificate is legitimate on the actual prediction
space. Its cellwise raw output vectors belong to a finite Gaussian
program; its operator error is bounded by the L2 norm of the feature-map
error. It does not require a finite-rank approximation to A0 in operator
norm. C17 is the four-term subtraction of D'^*D+D*D', using norm bounds
covering both exact and approximating factors. Finally, the two-stage
inner-product subtraction in C18 is correct, subject to the residual
scope correction already stated.

## 4. Spatial and deterministic Gaussian integration: C19–C26

The base spatial modulus C19 follows by separating the explicit input
vector, first gate, Q, upper delta, and hidden features. C20 uses the
same valid L2–L8 interpolation for Q in L4, followed by the row product
estimate. These bounds control both raw and row-L4 force quadrature.

C21 gives the upper directional-preactivation modulus using the middle
direction and the first-layer directional feature. The elementary tail
comparison C22 is valid with its stated constants. In C23 the difference
of the upper directional multiplier is split against B_z; the actual
bounded adjoint then controls the Q_z difference. The subsequent row,
middle, readout and explicit-input terms include every product from C13.
Thus the spatial errors e_x and e_I can be built from the displayed
bounds by finite sums and products, without an undefined Hessian norm.
For the central family, the target and density moduli needed alongside
these feature moduli are available from the declared Lipschitz bounds.

The fixed source graph can be enlarged by the finitely many passive and
directional queries needed at quadrature nodes. The new forward input
a_z is a bounded gate times a direction already built from finitely many
base queries. The new reverse input delta_z is a bounded coefficient
times B_z plus the readout-direction term. These action-query inputs
have the growth permitted by the established finite-program result.
The quadratic lower-row product is a final observation; the proof does
not require feeding a general quadratic function into an action theorem
that only permits linear growth. Every new answer retains all previous
opposite-orientation response contractions and the same source covariance.

The required named source derivatives have polynomial envelopes at each
fixed graph: clock-source derivatives of J are bounded through J_X,
and the remaining operations are bounded tanh derivatives, finite sums,
products, and finite-rank/source recursions. Root derivatives of J are
not needed for source extraction. Its compact-set root sensitivity is
finite and can be bounded as in §8. This permits deterministic compact
quadrature after tail truncation; it is not a statement about arbitrary
derivative order or a growing-width transcript.

C24 remains valid at singular covariances. After adding delta I, the
Sylvester equation for the square-root difference has inverse norm at
most 1/(2sqrt(delta)) in Frobenius norm. The two regularizations cost
sqrt(m delta) each, giving exactly (2sqrt(m)+1/2)sqrt(delta).
Positive-semidefinite projection of an approximate covariance increases
the certified discrepancy by at most a factor two. These bounds permit
causal error propagation even when a source covariance loses rank.

C25 is Cauchy–Schwarz combined with the Gaussian coordinate union bound.
The Gaussian radial moment product is correct. Finite cube quadrature
can use computable Lipschitz bounds and enclosed Gaussian cell weights.
C26 holds because |X|<=2(|X|-R/2)_+ on {|X|>R}; its right side is a
continuous finite-Gaussian integrand with the same kind of envelope.
Consequently neither hard-cutoff quadrature nor random sampling is
needed to enclose the derivative tails. Effective input data are needed
as specified in §1; a bare arbitrary bounded residual is insufficient.

## 5. Termination and unchanged-family scope: §9 and C27

The a posteriori construction need not have a useful a priori tail rate.
The convergence argument supplies the required existence of successful
finite choices. Raw endpoint convergence is explicit by C5. C9 and C12
give row-L4 convergence, which gives strong L2 convergence of a_b and
B_b. For delta_b, bounded multiplier convergence in probability can be
paired with a fixed limiting B_b by first truncating that L2 field.
Actual bounded adjunction gives Q_b convergence; the lower-row product
converges using its two L4 factors and bounded multiplier convergence.
This proves strong L2 derivative convergence without an ambient Hessian.

The uniform-input step can be reconstructed from the displayed spatial
bounds. C21 makes the B_b fields equicontinuous on the compact input
circle. A finite spatial net and C22 then give uniformly small B_b tails.
C23 gives Q_b equicontinuity after choosing those tails, and another
finite net gives uniformly small Q_b tails. Thus the cutoffs in C15 and
the spatial errors can be made uniform in u. First choose cutoffs, then
make the cutoff-amplified base errors small. This fills out the pointwise
strong-convergence paragraph without adding an Lp action hypothesis.

Enumerating reference meshes, fitting precisions, cutoffs, spatial meshes,
and Gaussian integral accuracies therefore eventually produces an error
strictly below any positive requested tolerance for the permitted effective
probe/net data. The Gram gap test can stabilize at any sufficiently small
positive gamma. Although the existence proof uses uniform integrability,
the acceptance test uses only certified finite quantities, so the absence
of an a priori tail rate does not prevent a terminating dovetailed search.
No reasonable operation count is established.

For C27, the total variation of the projected measure representing b_h is
at most (1+2L²/gamma)||h||_1. Applying C14 with unit measure mass gives
the stated J1; applying it to three arguments gives the trilinear bound
L J1 C_proj³. Telescoping the cubic produces the factor 3H1². The
linear derivative-feature bound and the conjugation by sqrt(p) correctly
account for changes of the prediction metric. The scalar identity for
sqrt(p)-sqrt(tilde p) gives the denominator sqrt(p_min) with the
displayed factor from D'.

Finite angular grids with quantized values, density normalization, and
odd symmetrization give effective covers of the original compact family.
The small enlarged bounding class does not select a target by outcome;
the strict factorized-target margin and positive density lower bound
permit those representatives. The density/target estimate for h is valid
on the original family, and the enlarged normalized representatives can
use an appropriately enlarged H1. This uniform net argument remains
valid independently of the defective unrestricted-probe sentence.

Arbitrary-accuracy approximation does not imply that a sign certificate
will be negative or that exact zero is decidable by interval refinement.
The termination proved here is for an approximation tolerance. A search
for a uniformly negative sign only has the corresponding strict-sign
conditional guarantee; the input explicitly makes no evaluated sign
claim. I read its remark about possibly certifying zero as permitting an
additional exact zero argument, not as a general zero-decision theorem.

## 6. Read coverage and provenance

The candidate was read completely in consecutive scopes 1–260, 261–520,
and 521–749. Its scope, error specializations, Gaussian integration, and
termination sections were reread during this audit. No other current
route or follow-up was read for this check. In particular, the references
to ROUTE_ENERGY.md and COMPARISON_TRANSFER.md in the candidate were not
followed. No external source, other study, Git history, training run,
quadrature run, or random simulation was used.

The allowed established sources had already been read completely in the
following scopes in this agent context; their hashes were rechecked:

- `docs/global_nonlinear.md`: 12994–17016, complete C.4.9–C.4.10;
  1840–1898, A.1–A.4 (reread 1840–1902 in this check); 5475–5782,
  C.4.5.1 §§1–3; 5999–6103,
  rational constant certificate; 6104–6521, C.4.5.2 §§1–4. A truncated
  earlier middle output was repaired by the explicit 16324–16540 reread;
  no unread complement is claimed checked.
- `docs/special_data_limits.md`: 3785–4326, complete III.F, explicitly
  added to the allowed scope by the supervisor.
- `docs/NOTATION.md` and the neutral study contract: complete.
- Own frozen geometry reports and own quantitative drift check: complete
  prior authorship/read coverage, used only within this study.
- `RESEARCH_WORKFLOW.md`: complete process read. Required rigorous-math
  and conjecture-investigation skills and the research-contract,
  adversarial-audit, and proof-search-orchestration references: complete.

Relevant frozen content hashes:

| Input | SHA256 |
|---|---|
| RESEARCH_CONTRACT.md | `0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| docs/special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| ROUTE_GEOMETRY.md | `e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04` |
| GEOMETRY_SIGN_FOLLOWUP.md | `7400b12eb9655a24f8ba23af2fd41b60733947ca5fc184850d2629eafd980719` |
| REFERENCE_SIGN_ATTEMPT.md | `6cfef322be7e9ee1d49c8287e3bfd94e6069c17ce40dfdf6619745472c1afa6f` |
| QUANTITATIVE_DRIFT_CHECK_G.md | `92a2af4304836d216aa48a9bbcdb33f8c08d229ecfa7b1c77c71772b7c9b44cf` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| /etc/codex/skills/solve-math-rigorously/SKILL.md | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| /etc/codex/skills/investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| research-contract reference | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| adversarial-audit reference | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| proof-search-orchestration reference | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |

The three named skill references are respectively
`/etc/codex/skills/investigate-conjectures/references/research-contract.md`,
`/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md`,
and `/etc/codex/skills/investigate-conjectures/references/proof-search-orchestration.md`.

The only new file written by this check is this report. The frozen input
and earlier frozen reports are preserved. The required probe-scope
correction was reported to the supervisor before freezing this check.
